import os.path as osp
import cv2
from tqdm import tqdm
from natsort import natsorted
import glob

def frame2vid(edited_frames_dir, fps, image_scale_factor=0.5):
    # Getting all frames
    frames = glob.glob(edited_frames_dir + "/" + "*.png")
    frames = natsorted(frames)

    # Get images size
    img = cv2.imread(frames[0])
    height, width, layers = img.shape
    size = (int(width*image_scale_factor), int(height*image_scale_factor))

    # Video writer Object
    video_out_dir = "video_fps_" + str(fps) + ".avi"
    print(video_out_dir)
    out = cv2.VideoWriter(video_out_dir, cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)

    for frame in tqdm(frames):
        img = cv2.imread(frame)
        img = cv2.resize(img, (0,0), fx=image_scale_factor, fy=image_scale_factor)
        out.write(img)
    
    out.release()
    print("Completed")

if __name__ == "__main__":
    import os
    try:
        os.system("clear")
    except:
        pass
    frames_dir = "/home/ibad/Documents/Stabelised_Sim_Datasets/Stabelised_from_GT_pos/images/"
    frame2vid(frames_dir, 33)
