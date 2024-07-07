# Cartesian Controllers on Universal Robots

A minimal setup to get the latest UR driver up and running with the `cartesian_controllers` for a *UR5* robot.
Use this as a starting point to investigate basic mechanisms and to setup your own use case.

## Commit with bugs `bc18a75`:

- I changed all the UR10e characters to UR5. The launch was successful when I run

```bash{.line-numbers}
roslaunch cartesian_controllers_ur_robots robot.launch
```

I can drag the robot to different positions.

However, the robot is shaking, and there are several warnings in the terminal:

```bash{.line-numbers}
[ WARN] [1720125571.243673007]: Failed to load /my_cartesian_compliance_controller/target_frame_topic from parameter server. Will default to: /my_cartesian_compliance_controller/target_frame
[ INFO] [1720125571.247543677]: Failed to load /my_cartesian_compliance_controller/gravity from parameter server
[ INFO] [1720125571.247772849]: Failed to load /my_cartesian_compliance_controller/tool from parameter server
```

According to [Issues#47](https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/47)， I should not worry about the `Failed to load xxx` info.

According to [Issues#47](https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/47) [Issues#91](https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/pull/91) and [Issues#100](https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/100), this shaking may be caused by wrong gravity compensation.

## Current behavior

force controller does not work, and there are oscillations when use compliant controller.

<video controls src="medias/oscillation.mp4" title="oscillations"></video>

I have removed the 2f-85 gripper but the issue remains.

The oscillations escalate if turn up the speed.

## Current behavior
force controller works if the variable `error_scale` is non-zero. But still with oscillations just like compliance controller. 

And the robot gradually moves upward when there is no force applied to the topic `target_wrench`.

Now I guess both issues is caused by wrong end_effector mass and COM. Will fine-tune it later

## ToDos

> References
> - https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/92
> - https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/151
> - https://github.com/fzi-forschungszentrum-informatik/cartesian_controllers/issues/95 how to drag the robot by hand using force_controller, currently I cannot do that either.