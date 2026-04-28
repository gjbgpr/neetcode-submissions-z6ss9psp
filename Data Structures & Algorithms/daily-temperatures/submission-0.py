class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        st = []
        for current_day, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                prev_day = st.pop()
                answer[prev_day] = current_day - prev_day
            st.append(current_day)
        
        return answer