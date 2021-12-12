import numpy as np

def evaluate_exercise(skeleton, exercise_type):
    if exercise_type == "curl":
        corrections = evaluate_curl(skeleton)
    
    if corrections == "":
        print("Your form is quite good! I can't find anything to correct!")
    else:
        print(corrections)
    return

def evaluate_curl(skeleton):
    corrections = ""
    corrections += check_forearm_swing(skeleton) 

    return corrections


def check_forearm_swing(skeleton):
    body_parts_of_angle = ('C', 'Elbow', 'Shoulder', 'Hip')

    min_ang = skeleton.angle_dict[0][body_parts_of_angle]
    max_ang = skeleton.angle_dict[0][body_parts_of_angle]
    mean_ang = 0
    num_nonnan = 0
    for i, v in enumerate(skeleton.angle_dict):
        if not np.isnan(v[body_parts_of_angle]):
            num_nonnan += 1
            mean_ang += v[body_parts_of_angle]

        if v[body_parts_of_angle] > max_ang:
            max_ang = v[body_parts_of_angle]
        if v[body_parts_of_angle] < min_ang:
            min_ang = v[body_parts_of_angle]

    mean_ang = mean_ang / num_nonnan
    mean_ang = np.degrees(mean_ang)

    if mean_ang > 8:
        return "You are swinging your arm too much! Try to keep your forearm parallel to your spine."
    else:
        return ""

def check_spine_swing(skeleton):

    body_parts_of_angle = ('C', 'Knee', 'Hip', 'Shoulder')

    angles = list()

    for i, v in enumerate(skeleton.angle_dict):
        if not np.isnan(v[body_parts_of_angle]):
            angles.append(v[body_parts_of_angle])

    angles = np.array(angles)
    angles = skeleton.reject_outliers(angles, m=100)
    angles = np.degrees(angles)
    print("rejected:", angles.min(), angles.max(), angles.mean())
    if angles.mean() 