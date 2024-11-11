import cv2
import imageio

cap = cv2.VideoCapture(0)

frames = []
image_count = 0
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(0)
    if key == ord("a"):
        image_count += 1
        frames.append(frame)
        print("Adding new image:", image_count)
    elif key == ord("q"):
        break
print("Images added: ", len(frames))

print("Saving GIF file")
with imageio.get_writer("gülümse.gif", mode="I") as writer:
    for idx, frame in enumerate(frames):
        print("Adding frame to GIF file: ", idx + 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)