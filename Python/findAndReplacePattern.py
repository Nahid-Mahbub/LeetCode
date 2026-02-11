class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        
        # alphabet_dict = {
        # 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        # 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        # 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        
        # initial_value = pattern[0]
        # pattern_list = []
        # word_list = []
        # counter = 0
        # ans = []
        # for word in pattern:
        #     if(word == initial_value):
        #         counter += 1
        #     else:
        #         initial_value = word
        #         counter = 1
        #     pattern_list.append(counter)
        # print(pattern_list)
        # for word in words:
        #     initial_value = word[0]
        #     counter = 0
        #     for letter in word:
        #         if(letter == initial_value):
        #             counter += 1
        #         else:
        #             initial_value = letter
        #             counter = 1
        #         word_list.append(counter)
        #         print(word_list, word, letter, initial_value)
        #     if(word_list == pattern_list):
        #         ans.append(word)
        #     word_list = []
        # return ans

        ans_list = []
        pattern_list = []
        my_dic = {}
        i = 1
        my_dic[pattern[0]] = i
        for letter in pattern:
            if letter in my_dic:
                pattern_list.append(my_dic[letter])
            else:
                i += 1
                my_dic[letter] = i
                pattern_list.append(my_dic[letter])
        print(my_dic, pattern_list)
                
        for word in words:
            words_list = []
            i = 1
            my_dic.clear()
            my_dic[word[0]] = i
            for letter_word in word:
                if letter_word in my_dic:
                    words_list.append(my_dic[letter_word])
                else:
                    i += 1
                    my_dic[letter_word] = i
                    words_list.append(my_dic[letter_word])
            if(words_list == pattern_list):
                ans_list.append(word)
        return ans_list

solution = Solution()
words = ["abc","cba","xyx","yxx","yyx"]
pattern = "abc"
result = solution.findAndReplacePattern(words, pattern)
print(result)