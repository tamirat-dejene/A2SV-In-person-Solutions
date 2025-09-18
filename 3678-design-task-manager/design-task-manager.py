class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.done = set() # taskId
        self.tasks = [] #(-priority, -taskId, userId) heap
        self.priority = defaultdict(int) # taskId: priority
        self.assignee = defaultdict(int) # taskId: userId

        for ui, ti, p in tasks:
            self.add(ui, ti, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        if taskId in self.done:
            self.done.remove(taskId)

        heappush(self.tasks, (-priority, -taskId, userId))
        self.priority[taskId] = priority
        self.assignee[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        if self.priority[taskId] == newPriority:
            return
        
        self.priority[taskId] = newPriority
        heappush(self.tasks, (-newPriority, -taskId, self.assignee[taskId]))

    def rmv(self, taskId: int) -> None:
        self.done.add(taskId)
        self.assignee.pop(taskId)
        self.priority.pop(taskId)

    def execTop(self) -> int:
        while self.tasks and (-self.tasks[0][1] in self.done or -self.tasks[0][0] != self.priority[-self.tasks[0][1]] or self.assignee[-self.tasks[0][1]] != self.tasks[0][2]):
            heappop(self.tasks) # invalidated
        
        uid = -1
        
        if self.tasks:
            _, tid, uid = heappop(self.tasks)
            self.rmv(abs(tid))

        return uid
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()