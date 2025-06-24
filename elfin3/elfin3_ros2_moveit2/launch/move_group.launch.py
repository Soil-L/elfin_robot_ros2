from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("elfin3", package_name="elfin_config")
        .sensors_3d(file_path=os.path.join(
            get_package_share_directory("elfin_config"),
            "config",
            "sensors_3d.yaml")
        )
        .to_moveit_configs()
    )
    return generate_move_group_launch(moveit_config)


