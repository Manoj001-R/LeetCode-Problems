class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result=0
        run_min=arrays[0][0]
        run_max=arrays[0][-1]

        for i in range(1,len(arrays)):
            cur_min=arrays[i][0]
            cur_max=arrays[i][-1]

            result=max(result,cur_max-run_min,run_max-cur_min)

            run_min=min(run_min,cur_min)
            run_max=max(run_max,cur_max)
        
        return result