import torchvision


class CocoDetection(torchvision.datasets.coco.CocoDetection):
    num_classes = 80
    default_resolution = (512, 512)
    mean = [0.40789654, 0.44719302, 0.47026115]
    std = [0.28863828, 0.27408164, 0.27809835]
    # PCA
    eigen_val = [0.2175, 0.0188, 0.0045]
    eigen_vec = [[-0.5675, 0.7192, 0.4009],
                 [-0.5808, -0.0045, -0.8140],
                 [-0.5836, -0.6948, 0.4203]]

    max_objs = 128
    class_name = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
        'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
        'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
        'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
        'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
        'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
        'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
        'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
        'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy bear', 'hair drier', 'toothbrush']
    valid_ids = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 27, 28, 31, 32, 33, 34, 35, 36,
        37, 38, 39, 40, 41, 42, 43, 44, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 67, 70,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
        82, 84, 85, 86, 87, 88, 89, 90
    ]
