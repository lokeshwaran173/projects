import cv2

# RTSP URL for your CCTV camera
rtsp_url = "rtsp://username:password@your_camera_ip:port/video"

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('CCTV Stream', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
