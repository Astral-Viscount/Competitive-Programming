#
# @lc app=leetcode id=3386 lang=python3
#
# [3386] Button with Longest Push Time
#

# @lc code=start
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        best_index = events[0][0]
        best_time = events[0][1]

        for i in range(1, len(events)):
            current_index = events[i][0]
            current_time = events[i][1] - events[i-1][1]

            if current_time > best_time:
                best_time = current_time
                best_index = current_index
            elif current_time == best_time:
                if current_index < best_index:
                    best_index = current_index
                    
        return best_index

        # buttons = {}
        # buttons[events[0][0]] = events[0][1]

        # for i in range(1, len(events)):
        #     current = events[i][0]
        #     calc = events[i][1] - events[i-1][1]

        #     if current in buttons:
        #         if buttons.get(current) < calc:
        #             buttons[current] = calc
        #     else:
        #         buttons[current] = calc

        # buttons = sorted(buttons.items(), key= lambda x: x[1], reverse=True)

        # if buttons[0][1] == buttons[1][1]:
        #     buttons = sorted(buttons, key= lambda x: x[0])

        # print(buttons)

        # return buttons[0][0]
# @lc code=end

