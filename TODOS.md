

1. Get some videos for [Squatting, Deadlifting, Curling, Power Cleans]
1. 2DKP = map(alphapose, videos)
1. ff
    - 3dKP = map(2dto3d, 2dKP)
    - Angles = map(3dangles_from_2d_keypoints, 2dKP) < -- more accurate
1. DTW on angles.