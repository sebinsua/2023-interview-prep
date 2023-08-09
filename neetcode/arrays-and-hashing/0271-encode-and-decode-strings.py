import string
from collections import Counter
from itertools import permutations


class Solution:
    def encode(self, strs, max_delim_length=None):
        """
        Encodes a list of strings to a single string.

        :param strs: a list of strings
        :param max_delim_length: maximum length for the delimiter, default is determined by input length
        :return: encoded string
        """
        combined_str = "".join(strs)
        char_count = Counter(combined_str)

        # Generate a set of unused characters
        unused_chars = (
            set(string.printable)
            - set(string.whitespace)
            - set(string.digits)
            - set(combined_str)
        )

        # List of least common characters
        least_common_chars = [item[0] for item in char_count.most_common()[::-1]]

        potential_delimiters = list(unused_chars) + least_common_chars

        if max_delim_length is None:
            max_delim_length = max(2, len(combined_str))

        def generate_delimiters():
            for length in range(1, max_delim_length):
                for perm in permutations(potential_delimiters, length):
                    delimiter = "".join(perm)
                    if delimiter not in combined_str:
                        yield delimiter

        delimiter = next(generate_delimiters(), None)

        if delimiter:
            return str(len(delimiter)) + delimiter + delimiter.join(strs)

        raise Exception("Unable to find a suitable delimiter.")

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        :param s: encoded string
        :return: list of decoded strings
        """
        # Find the index where the delimiter starts (first non-digit character)
        delimiter_start_idx = next(
            (idx for idx, char in enumerate(s) if not char.isdigit()), None
        )

        if delimiter_start_idx is None:
            raise ValueError("Invalid encoded string format")

        # Extract the delimiter length and delimiter
        delimiter_length = int(s[:delimiter_start_idx])
        delimiter = s[delimiter_start_idx : delimiter_start_idx + delimiter_length]

        # Return the split values after removing the delimiter
        return s[delimiter_start_idx + delimiter_length :].split(delimiter)


if __name__ == "__main__":
    solution = Solution()

    # Test 1: Basic test
    encoded_str = solution.encode(["hello", "world"])
    print(encoded_str)  # Expected to print the encoded string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected ["hello", "world"]

    # Test 2: Strings with repeated characters
    encoded_str = solution.encode(["a" * 100, "b" * 100])
    print(encoded_str)  # Expected to print the encoded string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected [a*100, b*100]

    # Test 3: Empty list
    encoded_str = solution.encode([])
    print(encoded_str)  # Expected to print an encoded empty string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected []

    # Test 4: List with empty strings
    encoded_str = solution.encode(["", "", ""])
    print(encoded_str)  # Expected to print the encoded string for empty strings
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected ["", "", ""]

    # Test 5: Strings with all characters
    all_chars = string.printable
    encoded_str = solution.encode([all_chars, all_chars])
    print(encoded_str)  # Expected to print the encoded string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected [all_chars, all_chars]

    # Test 6: Long list with same strings
    encoded_str = solution.encode(["test"] * 1000)
    print(encoded_str)  # Expected to print the encoded string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected ["test", "test", ...] repeated 1000 times

    # Test 7: Single character strings
    encoded_str = solution.encode(list(string.ascii_lowercase))
    print(encoded_str)  # Expected to print the encoded string
    decoded_list = solution.decode(encoded_str)
    print(decoded_list)  # Expected ['a', 'b', 'c', ... 'z']
