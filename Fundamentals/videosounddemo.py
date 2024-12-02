import cv2
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import threading

# Function to update video frame
def update_frame():
    global cap, lbl_video, img_tk

    ret, frame = cap.read()
    if ret:
        # Resize the frame
        frame = cv2.resize(frame, (640, 480))
        
        # Convert BGR to RGB (Tkinter uses RGB format)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create an image object from the frame
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)
        
        # Update the label with the new image
        lbl_video.config(image=img_tk)
        
        # Schedule the next frame update
        lbl_video.after(10, update_frame)
    else:
        cap.release()

# Function to play audio using system command
def play_audio():
    # Command to play audio using ffplay
    subprocess.run(['ffplay', '-autoexit', '-nodisp', 'video.mp4'])

# Create a Tkinter window
root = tk.Tk()
root.title("Video Player")

# Open the video file
cap = cv2.VideoCapture('video.mp4')

# Create a label widget to display the video
lbl_video = tk.Label(root)
lbl_video.pack()

# Start audio playback in a separate thread
threading.Thread(target=play_audio, daemon=True).start()

# Start the video update function
update_frame()

# Run the Tkinter event loop
root.mainloop()
