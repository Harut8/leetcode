import heapq
# https://neetcode.io/problems/meeting-schedule-ii

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """
        Idea: We sort the intervals by start time. Then, we iterate through the intervals and for each interval,
        we check if the first meeting in the heap has finished. If it has, we remove it from the heap.
        Then, we add the current interval to the heap. At the end, the size of the heap will be the number of rooms we need.
        """
        heap = []
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            """
            If the heap is not empty and the end time of the first meeting in the heap is less than or equal to the start time of the current meeting, 
            it means that the first meeting in the heap has finished, so we remove it from the heap.
            """
            if heap and heap[0] <= start: # if the first meeting in the heap has finished
                heapq.heappop(heap) # remove it from the heap because we can use another room in the same day
            """
            We add the current interval to the heap.
            """
            heapq.heappush(heap, end)
        """
        At the end, the size of the heap will be the number of rooms we need.
        """
        return len(heap)