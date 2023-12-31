# ChatPuppy: Control Robot dog with Natural Language

ChatPuppy is an innovative project that unites Language Logic Models (LLMs) with the control of robot dogs. It enables users to command robot dogs using uncomplicated, everyday language. The project operates on ROS2 (Robot Operating System) Humble and runs simulations in the Gazebo environment, ensuring a reliable and realistic testing platform for robot dog behavior.

Complementing ChatPuppy is a straightforward web application, providing an easy-to-use interface for users to input commands. This melding of leading-edge technology with a user-friendly interface allows controlling robot dogs to be both accessible and intuitive.

While ChatPuppy is currently operating within a simulated environment for comprehensive testing and development, it is also designed for real-world application. This means it has the potential to translate ordinary language into precise commands for actual robot dogs when necessary.

Key features include:
- A user-friendly web application providing an interactive interface for robot puppy control

  [![output-onlinegiftools-7-1.gif](https://i.postimg.cc/Kj22RxZm/output-onlinegiftools-7-1.gif)](https://postimg.cc/KkJVWXkW)
- Full control over the robot's directional movement, including forward, backward, left, right and robot rotation clockwise and anticlockwise (through the head or torso) commands
[![pupper-2-1.gif](https://i.postimg.cc/dthBLdxt/pupper-2-1.gif)](https://postimg.cc/kBd8HVCk)

- Support for commands in multiple languages
[![output-onlinegiftools-10-1.gif](https://i.postimg.cc/HxLMF1Gs/output-onlinegiftools-10-1.gif)](https://postimg.cc/XZTXyh7T)

## ROSGPT Architecture

![Screenshot from 2023-07-04 20-49-50](https://github.com/Gaurang-1402/ChatDrones/assets/71042887/f3534fd5-1ac8-4d55-8e67-fb5f6c0ddf8d)

1. The first component, "rosgpt.py", serves as the primary translator. As a REST server in a ROS2 node, it receives instructions in the form of POST requests, then processes these instructions into structured JSON commands using the ChatGPT API. Once the translation is complete, the commands are published on the /voice_cmd topic, ready for the next stage.

2. The next component is "rosgpt_client_node.py", a ROS2 client node that acts as a liaison between the user and rosgpt.py. It sends POST requests with the user's commands to the ROSGPT REST server and awaits the transformed JSON commands, displaying them upon receipt.

3. Another key component is "rosgpt_client.py", which fulfills a similar role to rosgpt_client_node.py. The main difference is that this script functions solely as a REST client for ROSGPT, without the ROS2 node involvement.

4. Once the commands are translated, they are received by "rosgptparser_puppy.py". This script, dubbed the ROSGPTParser, executes the commands. It subscribes to the /voice_cmd topic, receives the JSON commands, parses them, and then carries out the necessary puppy maneuvers.


## Getting started

Clone the repository

```
mkdir ros_ws
cd ros_ws
git clone <repo_url>
```

Install rosgpt libraries from the rosgpt folder

```
cd ~/src/rosgpt
pip3 install -r requirements.txt
```

Install ROS requirements

```
sudo apt-get install python-rosdep
sudo rosdep init
rosdep update
```

```
cd ~/ros_ws
rosdep install --from-paths src --ignore-src --rosdistro=<rosdistro> -y
```


Add your OpenAI API Key in your ```.bashrc``` as an environment variable 

```
echo 'export OPENAI_API_KEY=your_api_key' >> ~/.bashrc
```


## Running ROSGPT

First, navigate to the root directory of your workspace and build the project

```
cd ~/ros_ws
colcon build --symlink-install
```
Now run each of these commands on new terminals

```
source install/setup.sh
ros2 run rosgpt rosgpt
```

```
source install/setup.sh
ros2 run rosgpt rosgpt_client_node 
```

```
source install/setup.sh
ros2 run rosgpt rosgptparser_puppy 
```

## Running the simulation

### Test in RViz

Note: This step is only for PC

```sh
# Terminal 1
source install/setup.sh
ros2 launch mini_pupper_bringup bringup.launch.py joint_hardware_connected:=false rviz:=true
```

### Test in Gazebo

Note: This step is only for PC

```sh
# Terminal 1
source install/setup.sh
ros2 launch mini_pupper_gazebo gazebo.launch.py rviz:=true
```

Note: Please replace `<repository_url>` and `<your_api_key>` with the actual repository URL and your OpenAI API key, respectively.

## Credits
Simulation adapted from: https://github.com/mangdangroboticsclub/mini_pupper_ros

```
@article{koubaa2023rosgpt,
  title={ROSGPT: Next-Generation Human-Robot Interaction with ChatGPT and ROS},
  author={Koubaa, Anis},
  journal={Preprints.org},
  year={2023},
  volume={2023},
  pages={2023040827},
  doi={10.20944/preprints202304.0827.v2}
}

```

I am deeply appreciative of these individuals/teams for sharing their work to build on top of!
