from tkinter import *
import cv2
import numpy as np
import youtube_dl

def faceblur():
    face_cascade = cv2.CascadeClassifier(r'C:\Users\MY PC\open-cv-resources\Computer-Vision-with-Python\DATA\haarcascades\haarcascade_frontalface_default.xml')

    if __name__ == '__main__':
        global e

        video_url = str(e.get())


        ydl_opts = {}

        # create youtube-dl object
        ydl = youtube_dl.YoutubeDL(ydl_opts)

        # set video url, extract video information
        info_dict = ydl.extract_info(video_url, download=False)

        # get video formats available
        formats = info_dict.get('formats', None)

        for f in formats:

            # Set resolution
            if f.get('format_note', None) == '360p':

                # get the video url
                url = f.get('url', None)

                # open url with opencv
                cap = cv2.VideoCapture(url)

                # check if url was opened
                if not cap.isOpened():
                    print('video not opened')
                    exit(-1)

                while True:
                    # read frame
                    ret, frame = cap.read()

                    # check if frame is empty
                    if not ret:
                        break

                    face_rects = face_cascade.detectMultiScale(frame)

                    for (x, y, w, h) in face_rects:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), -1)
                        # frame[x:x + w, y:y + h] =

                    # display frame
                    cv2.imshow('frame', frame)

                    if cv2.waitKey(30) & 0xFF == ord('q'):
                        break

                # release VideoCapture
                cap.release()

        cv2.destroyAllWindows()








root = Tk()
e = Entry(root)
e.pack()
frame = Frame(root,height = 400,width = 400)
frame.pack()
button = Button(frame,text = 'press',command = faceblur)
button.pack()

root.mainloop()



