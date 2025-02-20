# Imports
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Node to be launched
    signal_processing_node = Node(
                        package = 'signal_processing_ROSario',
                        executable = 'signal_generator_ROSario',
                        output = 'screen'
                     )
    
    # Node to be launched
    process_node = Node(
                        package = 'signal_processing_ROSario',
                        executable = 'process_ROSario',
                        output = 'screen'
                     )
    
    l_d = LaunchDescription([signal_processing_node, process_node])
    return l_d