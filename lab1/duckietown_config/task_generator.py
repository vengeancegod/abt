from gym_duckietown.simulator import PositionOnInitialRoadTile
from gym_duckietown.tasks.task_generator import TaskGenerator
from gym_duckietown.tasks.tracking_duckietown_env_with_rec import TrackingDuckietownEnvWithRec
import numpy as np
from numpy.linalg import norm


class DefaultTaskGenerator(TaskGenerator):
    def __init__(self, args=None):
        super().__init__(args)

    def generate_task(self):
        env_loader = TrackingDuckietownEnvWithRec
        env = env_loader(
            map_name="straight_road",  # loop_only_duckies    loop_pedestrians
            domain_rand=False,
            draw_bbox=False,
            user_tile_start=(0,0)
        )

        self.generated_task['env'] = env
        env.render()
        return self.generated_task
