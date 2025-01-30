import cv2
import os

def create_video_from_frames(input_folder, output_video, fps=30):
    images = sorted([img for img in os.listdir(input_folder) if img.endswith(".png")])
    frame_path = os.path.join(input_folder, images[0])
    frame = cv2.imread(frame_path)

    height, width, _ = frame.shape
    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        frame = cv2.imread(os.path.join(input_folder, image))
        video_writer.write(frame)

    video_writer.release()
    print(f"Video saved to '{output_video}'")

# Function call
output_video = r"C:\Users\MernaSherif\Desktop\SVMRepo\MiDaS_MyRepo\output"
create_video_from_frames(output_video, "output/depth_video.mp4")
