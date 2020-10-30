from config import *
from imutils import paths
import random, shutil, os

originalPaths=list(paths.list_images(INPUT_DATASET))
random.seed(7)
random.shuffle(originalPaths)
index=int(len(originalPaths)*TRAIN_SPLIT)
trainPaths=originalPaths[:index]
testPaths=originalPaths[index:]
index=int(len(trainPaths)*VAL_SPLIT)
valPaths=trainPaths[:index]
trainPaths=trainPaths[index:]
datasets=[("training", trainPaths, TRAIN_PATH),
          ("validation", valPaths, VAL_PATH),
          ("testing", testPaths, TEST_PATH)
]
for (setType, originalPaths, basePath) in datasets:
        print(f'Building {setType} set')
        if not os.path.exists(basePath):
                print(f'Building directory {BASE_PATH}')
                os.makedirs(basePath)
        for path in originalPaths:
                file=path.split(os.path.sep)[-1]
                label=file[-5:-4]
                labelPath=os.path.sep.join([basePath,label])
                if not os.path.exists(labelPath):
                        print(f'Building directory {labelPath}')
                        os.makedirs(labelPath)
                newPath=os.path.sep.join([labelPath, file])
                print(newPath)
                shutil.copy2(path, newPath)