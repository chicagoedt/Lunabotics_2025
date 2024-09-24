import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

#we want to launch 3 nodes: the Arduino Node, the Motor Controller and the Joystick

def generate_launch_description():

    # spawn Arduino node from the py_pkg pkg

    Arduino_NANO = Node(package='py_pkg',
                 executable= 'Arduino_NANO_v4',
                 output = 'screen'
                 )
    
    Arduino_UNO = Node(package='py_pkg',
                 executable= 'Arduino_UNO_v4',
                 output = 'screen'
                 )

    MotorController = Node(package='py_pkg',
                 executable= 'Motor_Controller_v2',
                 output = 'screen'
                 )

    PID_lift = Node(package='py_pkg',
                 executable= 'PID_linact_v2',
                 parameters=[
                     {"PID": [1.0,0.0,0.0]}
                 ],
                 output = 'screen'
                 )

    PID_tilt = Node(package='py_pkg',
                 executable= 'PID_linact_v2',
                 parameters=[
                     {"feedback_topic":'tilt_feedback_filt',
                      "command_topic":'tilt_vel',
                      "command_server":'des_tilt_pos',
                      "range":4,
                      "feedback_off_range":[130,696,90,760],
                      "PID": [1.0,0.0,0.0],
                      "v_max": 2.0}
                 ],
                 name='PID_tilt',
                 output = 'screen'
                 )

    PID_motor = Node(package='py_pkg',
                 executable= 'PID_motor_v2',
                 parameters=[
                     {"PID": [1.0,0.0,0.0]}
                 ],
                 output = 'screen'
                 )
    
    Digging_aut = Node(package='py_pkg',
                 executable= 'Main_aut_v2',
                 output = 'screen'
                 )
    
    Brain = Node(package='py_pkg',
                 executable= 'Brain_command_v2',
                 output = 'screen'
                 )

    Jetson = Node(package='py_pkg',
                 executable= 'Jetson_v2',
                 output = 'screen'
                 )
    
    Filter_lift = Node(package='py_pkg',
                 executable= 'Filter_v2',
                 parameters=[
                     {"subscriber_topic":'lift_feedback',
                      "publisher_topic":'lift_feedback_filt',
                      "percent_taken":0.9}
                 ],
                 name='filter_lift',
                 output = 'screen'
                 )
    
    Filter_tilt = Node(package='py_pkg',
                 executable= 'Filter_v2',
                 parameters=[
                     {"subscriber_topic":'tilt_feedback',
                      "publisher_topic":'tilt_feedback_filt',
                      "percent_taken":0.9}
                 ],
                 name='filter_tilt',
                 output = 'screen'
                 )
        
    #launch all 3 
    return LaunchDescription([
            Arduino_NANO,
            Arduino_UNO,
            MotorController,
            PID_lift,
            PID_tilt,
            PID_motor,
            Digging_aut,
            Jetson,
            Filter_tilt,
            Filter_lift
            #Brain

    ])
