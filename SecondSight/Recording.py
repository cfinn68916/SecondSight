import SecondSight
import cv2
import numpy as np
import time


class RecordingManager:
    instance = None

    @classmethod
    def getInst(cls):
        if cls.instance is None:
            cls.instance = RecordingManager()
        return cls.instance

    def __init__(self):
        self.isRecording = False
        cams = SecondSight.Cameras.CameraManager.getCameras()
        self.res = (cams[0].width, cams[0].height)
        self.out = None

    def startRecording(self):
        if not self.isRecording:
            self.isRecording = True
            fourcc = cv2.VideoWriter_fourcc(*'MP4V')
            cams = SecondSight.Cameras.CameraManager.getCameras()
            self.out = cv2.VideoWriter(f'{time.time()}.mp4', fourcc, 20.0, (self.res[0] * len(cams), self.res[1]))

    def step(self):
        if self.isRecording:
            cams = SecondSight.Cameras.CameraManager.getCameras()
            vis = np.concatenate(tuple([cv2.resize(cam.frame, self.res, interpolation=cv2.INTER_LINEAR) for cam in cams]), axis=1)
            self.out.write(vis)

    def stopRecording(self):
        if self.isRecording:
            self.isRecording = False
            self.out.release()
            self.out = None
