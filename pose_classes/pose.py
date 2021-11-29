import json

class PoseSequence:
    pose_sequence_2D = []
    pose_sequence_3D = []

    # Pass json path to PoseSequence object for it to create a PoseSequence object that represents the video
    def __init__(self, json_path):

        video_pose_sequence = []
        
        with open(json_path) as f:
            
            data = json.load(f)
            #print(type(data[0]))
            last_entry = data[-1]
            num_frames = int(last_entry["image_id"].split(".")[0]) + 1
            print(f"num of frames: { num_frames }")

            cur_frame = int(data[0]["image_id"].split(".")[0])

            for entry in data:
                frame = int(entry["image_id"].split(".")[0])
                
                if frame == cur_frame:
                    pose_obj = Pose_2D(entry["keypoints"])
                    video_pose_sequence.append(pose_obj)
                    cur_frame += 1           

        self.pose_sequence_2D = video_pose_sequence

    def convert_2D_to_3D(self):
        pass



class Pose_2D:

    # Stores keypoints as a dictionary of tuples.
    # The key is the name of the body part, and tuples have the form (x, y, confidence)
    def __init__(self, keypoints):

        self.keypoints = {
            "Nose": (keypoints[0], keypoints[1], keypoints[2]),
            "LEye": (keypoints[3], keypoints[4], keypoints[5]),
            "REye": (keypoints[6], keypoints[7], keypoints[8]),
            "LEar": (keypoints[9], keypoints[10], keypoints[11]),
            "REar": (keypoints[12], keypoints[13], keypoints[14]),
            "LShoulder": (keypoints[15], keypoints[16], keypoints[17]),
            "RShoulder": (keypoints[18], keypoints[19], keypoints[20]),
            "LElbow": (keypoints[21], keypoints[22], keypoints[23]),
            "RElbow": (keypoints[24], keypoints[25], keypoints[26]),
            "LWrist": (keypoints[27], keypoints[28], keypoints[29]),
            "RWrist": (keypoints[30], keypoints[31], keypoints[32]),
            "LHip": (keypoints[33], keypoints[34], keypoints[35]),
            "RHip": (keypoints[36], keypoints[37], keypoints[38]),
            "LKnee": (keypoints[39], keypoints[40], keypoints[41]),
            "RKnee": (keypoints[42], keypoints[43], keypoints[44]),
            "LAnkle": (keypoints[45], keypoints[46], keypoints[47]),
            "RAnkle": (keypoints[48], keypoints[49], keypoints[50]),
        }
                