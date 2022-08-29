import cv2
from tqdm import tqdm
from natsort import natsorted
import glob

# pip install opencv-python tqdm natsort --quiet

def images_to_video(frames_dir="", fps=30, image_scale_factor=0.5, image_format=".png"):
    """
        frames_dir: folder in which images are present
        fps: frame rate (frames per second) for the output video 
        image_scale_factor: Factor by which images is resized. =1 if we dont want to resize 
        image_format: Format of images: .png or jpg (or other -> not tested)
    """
    # Getting all frames
    frame_dir = frames_dir + "/" + f"*{image_format}"
    frames = glob.glob(frame_dir)
    frames = natsorted(frames)

    # Get images size
    img = cv2.imread(frames[0])
    height, width, channels = img.shape
    size = (int(width*image_scale_factor), int(height*image_scale_factor))

    # Video writer Object
    video_out_dir = "video_fps_" + str(fps) + ".avi"
    out = cv2.VideoWriter(video_out_dir, cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)

    for frame in tqdm(frames):
        img = cv2.imread(frame)
        img = cv2.resize(img, (0,0), fx=image_scale_factor, fy=image_scale_factor)
        out.write(img)
    
    out.release()
    print("Video saved to: ", video_out_dir)
    print("Completed")

    return


def main():
    import os
    try:
        os.system("clear")
    except:
        pass
    frames_dir = "/home/ibad/Documents/Stabelised_Sim_Datasets/Stabelised_from_GT_pos/images/"
    image_format = ".png"
    
    # Convert
    images_to_video(frames_dir, 
                    fps=33, 
                    image_format=image_format, 
                    image_scale_factor=1)
    
    return


if __name__ == "__main__":
    main()
