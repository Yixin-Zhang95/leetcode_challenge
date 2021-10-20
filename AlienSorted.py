class Solution:
    @staticmethod
    def isAlienSorted(words, order) -> bool:
        order_set = {}
        for i, value in enumerate(order): order_set[value] = i

        for i in range(0, len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                print(j, word1[j], word2[j], order_set[word1[j]], order_set[word2[j]])
                if word1[j] == word2[j] and j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2):
                    return False
                elif order_set[word1[j]] > order_set[word2[j]]:
                    return False
                elif order_set[word1[j]] < order_set[word2[j]]:
                    break

        return True

words = ["ubg","kwh"]
order = "qcipyamwvdjtesbghlorufnkzx"
print(Solution.isAlienSorted(words, order))