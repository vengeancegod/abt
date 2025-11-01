from gym_duckietown.tasks.task_solution import TaskSolution
import time

class Ride1MTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']

        start_pos = env.cur_pos
        distance = 0
        while distance < 1.0:
            linear_velocity = 0.2
            angular_velocity = 0.0

            obs, reward, done, info = env.step([linear_velocity, angular_velocity])
            env.render()

            distance = env.cur_pos[0] - start_pos[0]
            if done:
                break

            time.sleep(0.1)

        env.close()

if __name__ == "__main__":
    from gym_duckietown.tasks.default.task_generator import DefaultTaskGenerator

    task_generator = DefaultTaskGenerator()
    task_generator.generate_task()
    solution = Ride1MTaskSolution(task_generator.generated_task)
    solution.solve()
