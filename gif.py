import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
import cv2

def create_gif():
    # Open file explorer to select video file
    root = tk.Tk()
    root.withdraw()
    video_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

    # Use MoviePy to create a GIF from the video
    video_clip = mp.VideoFileClip(video_file)
    def resize_frame(frame):
        return cv2.resize(frame, (640, 480))
    gif_clip = video_clip.fl_image(resize_frame)
    gif_clip.write_gif('output.gif')

    print("GIF created successfully!")

    # Display the GIF
    cap = cv2.VideoCapture('output.gif')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('GIF', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    create_gif()