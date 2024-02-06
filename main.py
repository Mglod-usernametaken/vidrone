
import cv2
import time

def show_and_record_video(device=0, output_file="output.avi"):
    cap = cv2.VideoCapture(device)
    cap.set(cv2.CAP_PROP_FPS, 60)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    if not cap.isOpened():
        print("error - could not open device")
        return
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_file, fourcc, 30.0, (1440, 1080))  # Adjust parameters as needed
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("error - could not read frame")
                break
            fps = cap.get(cv2.CAP_PROP_FPS)
            # print(f"fps: {fps:.2f}")
            cv2.putText(frame,f'fps: {fps:.2f}',(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4) 
            # Write the frame to the output file
            frame = cv2.resize(frame, (960, 720), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)


        
           # out.write(frame)
            
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_device = 0
    output_file = "output.avi"
    show_and_record_video(video_device, output_file)

