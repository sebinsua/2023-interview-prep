from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Each index contains the number of days until a warmer day.
        # By default keep `answer[i] == 0` if there is no future warmer day.
        answers = [0] * len(temperatures)

        # We will use the `stack` to keep track of the indexes of previous
        # temperatures and we will drop temperatures from this if they
        # are cooler than the current temperature.
        #
        # The `stack` will be a list of temperatures waiting for a future
        # warmer temperature.
        stack = []
        for current_index, current_temperature in enumerate(temperatures):
            # We traverse backwards through past temperatures in the stack
            # while the current temperature is warmer.
            #
            # On each iteration we drop the cooler past temperature and
            # store the offset between that temperature and the current
            # warmer temperature in its `answers[index]`.
            #
            # Once this loop exits, the temperatures remaining in the stack
            # will all be warmer than the current temperature.
            while stack and current_temperature > temperatures[stack[-1]]:
                last_index = stack.pop()
                answers[last_index] = current_index - last_index

            stack.append(current_index)

        return answers
