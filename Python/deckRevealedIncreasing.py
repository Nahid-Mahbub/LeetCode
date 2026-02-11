class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        len_deck = len(deck)
        deck.sort()
        flag = 0
        output = [0] * len_deck        
        index_queue = [i  for i in range(len_deck)]

        print(index_queue)
        for card in deck:
            print(index_queue[0])
            output[index_queue[0]] = card
            index_queue.pop(0)
            if index_queue:
                index_queue.append(index_queue.pop(0))

        return output
solution = Solution()
deck = [1,2,3,4]
result = solution.deckRevealedIncreasing(deck)
print(result)