class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        length = len(n_str)
        new_str = []
        i = length
        for c in n_str:
            new_str.append(c)
            i -= 1
            if (i > 0 and i % 3 == 0):
                new_str.append(".")

        return "".join(new_str)