from gym_duckietown.tasks.task_solution import TaskSolution
import time
import numpy as np

class DefaultTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        env.cur_pos = np.array([0.305, 0.0, 0.305])
        env.cur_angle = 0.0

        start_x = env.cur_pos[0]

        for i in range(40):
            linear_velocity = 0.2
            angular_velocity = 0.0

            obs, _, done, info = env.step([linear_velocity, angular_velocity])
            env.render()

            if i % 5 == 0 and abs(env.cur_angle) > 0.1:
                env.cur_angle = 0.0

            if done:
                break
            time.sleep(0.1)

        # ПАУЗА после завершения движения (правильные отступы!)
        start_time = time.time()
        while time.time() - start_time < 30:
            obs, _, _, _ = env.step([0.0, 0.0])
            env.render()
            time.sleep(0.1)

        env.close()

if __name__ == "__main__":
    from gym_duckietown.tasks.default.task_generator import DefaultTaskGenerator

    task_generator = DefaultTaskGenerator()
    task_generator.generate_task()
    solution = DefaultTaskSolution(task_generator.generated_task)
    solution.solve()
