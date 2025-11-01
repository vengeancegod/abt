from gym_duckietown.tasks.task_solution import TaskSolution


class DefaultTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']            
