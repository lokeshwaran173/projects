import csv
import cv2
from pyzbar import pyzbar
import winsound

def scan_barcodes(ip_address):
    # Create the video stream URL using the IP address and port of the IP Webcam app
    video_url = f"http://{ip_address}:8080/video"

    # Initialize the video capture device using the video stream URL
    cap = cv2.VideoCapture(video_url)

    # Specify the CSV file path
    csv_file = 'D:/desk/Downloads/barcode/barcodes.csv'

    detected_barcodes = []

    while True:
        # Read frame from the video capture device
        _, frame = cap.read()

        # Convert the frame to grayscale for barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect barcodes in the frame
        barcodes = pyzbar.decode(gray)

        # Display the frame with barcode detection
        cv2.imshow("Barcode Scanner", frame)

        # Process each detected barcode
        for barcode in barcodes:
            # Extract the barcode value
            barcode_value = barcode.data.decode("utf-8")

            # If the barcode is not already detected, add it to the list
            if barcode_value not in detected_barcodes:
                detected_barcodes.append(barcode_value)
                print("Scanned barcode:", barcode_value)
                add_to_csv(barcode_value, csv_file)
                print("Barcode added to CSV file.")
                # Add a beep sound
                frequency = 2500  # Set the beep frequency (in Hz)
                duration = 1000  # Set the beep duration (in milliseconds)
                winsound.Beep(frequency, duration)

        # Check for the "q" key to quit the program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture device
    cap.release()

    # Close the OpenCV windows
    cv2.destroyAllWindows()

def add_to_csv(barcode_value, csv_file):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([barcode_value])

if __name__ == "__main__":
    # Prompt the user to enter the IP address of the mobile device running the IP Webcam app
    ip_address = input("Enter the IP address of the mobile device: ")

    # Call the scan_barcodes function with the IP address provided
    scan_barcodes(ip_address)
