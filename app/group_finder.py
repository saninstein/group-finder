from typing import Dict, List, Tuple


class GroupFinder:
    """
    Finds groups in the list of strings by prefix
    """
    @classmethod
    def find(
            cls,
            strings: List[str],
            delimiter: str = '_'
    ) -> Dict[str, List[str]]:
        """
        Finds group of strings by common prefix

        :param strings: source list of string
        :param delimiter: word delimiter
        """
        tokens_array = cls._prepare_tokens(strings, delimiter)
        return {
            cls._build_group_name(group, token_deep): ['_'.join(x) for x in group]
            for token_deep, group in cls._find_groups(tokens_array)
        }

    @classmethod
    def _find_groups(
            cls,
            tokens_array: List[List[str]],
            _token_deep: int = 0
    ) -> List[Tuple[int, List[List[str]]]]:
        """
        Finds groups of tokens
        :param tokens_array: list of tokenized strings
        :param _token_deep: matched token index (recursion parameter)
        :return: list of tuples with matched token index and list of matched tokens
        """

        if not tokens_array:
            return []

        if len(tokens_array) == 1 or _token_deep != 0 and len(tokens_array) <= 3:
            return [(_token_deep - 1, tokens_array)]

        result = []
        cursor = 0

        while cursor < len(tokens_array):
            subarray = []
            next_cursor_start = cursor + 1
            for i in range(cursor, len(tokens_array)):
                if tokens_array[i][_token_deep] == tokens_array[cursor][_token_deep]:
                    next_cursor_start = i + 1
                    subarray.append(tokens_array[i])
                else:
                    break
            result.extend(cls._find_groups(subarray, _token_deep + 1))
            cursor = next_cursor_start

        return result

    @staticmethod
    def _prepare_tokens(strings: List[str], delimiter: str) -> List[List[str]]:
        """
        Creates list of the tokenized strings

        :param strings: source strings
        :param delimiter: delimiter for the tokens
        :return: list of the tokenized strings
        """
        return [
            string.split(delimiter)
            for string in sorted(strings, key=lambda e: (e, len(e)))
            if string
        ]

    @staticmethod
    def _build_group_name(group: List[List[str]], token_deep: int) -> str:
        """
        Finds longest common prefix of the group of tokenized strings
        :param group: the group of tokenized strings
        :param token_deep: matched token index
        :return: group name
        """
        if len(group) == 1:
            token_deep = len(group[0])
        else:
            for i in range(token_deep, len(group[0])):
                if all(group[0][i] == arr[i] for arr in group[1:]):
                    token_deep = i
                else:
                    break

        return '_'.join(group[0][:token_deep + 1])
