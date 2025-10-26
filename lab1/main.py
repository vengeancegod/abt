from gym_duckietown.tasks.task_solution import TaskSolution
import time

class DefaultTaskSolution(TaskSolution): #DefaultTaskSolution (docker) #NoMoveTaskSolution (host)
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']

        for i in range(150):
            linear_velocity = 0
            angular_velocity = 0

            obs, reward, done, info = env.step([linear_velocity, angular_velocity])
            env.render()

            time.sleep(0.1)

        env.close()

if __name__ == "__main__":
    # код ниже требуется для возможности запуска вашего решения в описываемом образе, при отправки решения в систему проверки данный код не требуется
    from gym_duckietown.tasks.default.task_generator import DefaultTaskGenerator

    task_generator = DefaultTaskGenerator()
    task_generator.generate_task()
    solution = DefaultTaskSolution(task_generator.generated_task)
    solution.solve()
