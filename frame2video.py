import os
import cv2
from tqdm import tqdm
from natsort import natsorted
import glob

def frame2vid(edited_frames_dir, fps):
    vid_name = edited_frames_dir + "_" + str(fps)
    
    frames = glob.glob(edited_frames_dir + "/" + "*.png")
    frames = natsorted(frames)
    img_array = []
    print("Joining frames...")
    for frame in tqdm(frames):
        img = cv2.imread(frame)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(edited_frames_dir + "_fps_" + str(fps) + ".avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    print("Saving to a video...")
    for i in tqdm(range(len(img_array))):
        out.write(img_array[i])
    out.release()
    print("Video Saved")

if __name__ == "__main__":
    frame2vid("frames", 2)