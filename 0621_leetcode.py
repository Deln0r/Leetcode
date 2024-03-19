class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = collections.Counter(tasks)
        max_count = max(task_count.values())
        max_tasks = sum(1 for count in task_count.values() if count == max_count)
        total_slots = (max_count - 1) * (n + 1) + max_tasks
        return max(total_slots, len(tasks))