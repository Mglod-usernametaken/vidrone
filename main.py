import cv2

def show_video(device = 0):
    cap = cv2.VideoCapture(device)
    if not cap.isOpened():
        print("error - could not open device")
        return
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("error - could not read frame")
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    finally:
        cap.release()
        cv2.destroyallWindows()

if __name__ == "__main__":
    video_device = 0
    show_video(video_device)

