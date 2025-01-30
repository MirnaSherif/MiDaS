import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_index:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_index += 1

    cap.release()
    print(f"Extracted {frame_index} frames to '{output_folder}'")


# Function call

video_path = r"C:\Users\MernaSherif\Desktop\SVMRepo\MiDaS_MyRepo\video\undistorted_part_1.mp4"
output_folder = r"C:\Users\MernaSherif\Desktop\SVMRepo\MiDaS_MyRepo\input"

extract_frames(video_path, output_folder)


