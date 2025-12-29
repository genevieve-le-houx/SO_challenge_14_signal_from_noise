from dataclasses import dataclass, field
from typing import List
from pathlib import Path


@dataclass
class Result:
    longuest_sequence: int | None = None

    temp_sequence: List[int] = field(default_factory=lambda: [])
    temp_missing_value: int | None = None
    temp_duplicate_value: int | None = None

    sequence: List[int] = field(default_factory=lambda: [])
    missing_value: int = None
    duplicate_value: int = None

    def save_longuest_sequence(self):
        self.sequence = self.temp_sequence.copy()
        self.missing_value = self.temp_missing_value
        self.duplicate_value = self.temp_duplicate_value
        self.longuest_sequence = len(self.temp_sequence)

    def reset_result(self):
        self.temp_sequence = []
        self.temp_missing_value = None
        self.temp_duplicate_value = None

    def start_new_sequence(self):
        if len(self.temp_sequence) > self.longuest_sequence:
            if self.temp_missing_value is not None and self.temp_duplicate_value is not None:
                self.save_longuest_sequence()

        self.reset_result()

    def print_result(self):
        print(
            f"Sequence is: {str(self.sequence[0]).rjust(3)} to {str(self.sequence[-1]).rjust(3)}; "
            f"missing {str(self.missing_value).rjust(3)} and duplicate {str(self.duplicate_value).rjust(3)}"
        )


def read_file(filename: Path) -> List[List[int]]:
    """
    Read the file and return the list of sequences
    :param filename: The path to the file
    :return: sequences: A list of sequences
    """
    sequences = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.replace("[", "")
            line = line.replace("]", "")
            sequences.append([int(x) for x in line.split(",")])

    return sequences


def find_sequences(signals: List[List[int]]) -> List[Result]:
    results = []
    for signal in signals:
        sorted_signal = sorted(signal)

        result = None

        for number in sorted_signal:
            if result is None:
                result = Result(longuest_sequence=1, temp_sequence=[number])

            else:
                # If diff is 0, duplicate. If diff is 2, missing value. If bigger, is a new sequence
                match (diff := number - result.temp_sequence[-1]):
                    case 0:
                        if result.temp_duplicate_value is None:
                            result.temp_duplicate_value = number
                        else:
                            # Two duplicate values
                            result.start_new_sequence()

                    case 2:
                        if result.temp_missing_value is None:
                            result.temp_missing_value = number - 1
                        else:
                            # Two missing values
                            result.start_new_sequence()

                    case _ if diff > 2:
                        result.start_new_sequence()

                result.temp_sequence.append(number)

        # Check if current sequence is the longest
        if len(result.temp_sequence) > result.longuest_sequence:
            if result.temp_missing_value is not None and result.temp_duplicate_value is not None:
                result.save_longuest_sequence()

        if result.missing_value is None or result.duplicate_value is None:
            # No valid sequence
            results.append(None)
            print(f"No valid sequence for {sorted_signal}")
        else:
            results.append(result)

    return results


def compute_sum(results: List[Result]) -> int:
    sum_ = 0

    for result in results:
        sum_ += result.sequence[0] + result.sequence[-1]

    return sum_


def main():
    signals = read_file(Path("number_sequences.txt"))


    results = find_sequences(signals)

    sum_ = compute_sum(results)

    print(f"Sum is {sum_}\n")

    print(f"Result are:")
    for result in results:
        result.print_result()


if __name__ == '__main__':
    main()