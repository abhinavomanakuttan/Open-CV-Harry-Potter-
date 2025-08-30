#  Harry Potter Invisibility Cloak using OpenCV
# Made simple for school students to understand step by step!

import cv2      # OpenCV for computer vision tasks
import numpy as np  # Numpy for numerical operations
import time     # Time module to add delays

#  STEP 1: Open the webcam
cap = cv2.VideoCapture(0)  # 0 = Default camera
if not cap.isOpened():
    print(" Camera not found! Try plugging in a webcam or changing index to 1 or 2.")
    exit()

# Give the camera 2 seconds to adjust brightness
time.sleep(2)

#  STEP 2: Capture the background (without the cloak)
print("📸 Capturing background... Stand still for 3 seconds!")
for i in range(60):  # Take multiple frames for a clean background
    ret, background = cap.read()
    if ret:
        background = cv2.flip(background, 1)  # Flip to avoid mirror effect
print(" Background captured successfully!")

#  STEP 3: Define cloak color range (Here we use RED)
# NOTE: HSV (Hue, Saturation, Value) is better for color detection than RGB
lower_red1 = np.array([0, 120, 70])     # Lower range for red
upper_red1 = np.array([10, 255, 255])   # Upper range for red
lower_red2 = np.array([170, 120, 70])   # Red wraps around, so a second range
upper_red2 = np.array([180, 255, 255])  # Second upper range

print(" Starting Invisibility Cloak! Press 'ESC' to quit, 'b' to recapture background.")

#  STEP 4: Start reading frames continuously
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame to match mirror view
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #  STEP 5: Create a mask to detect red cloak
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)  # First range
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)  # Second range
    cloak_mask = mask1 + mask2  # Combine both
    
    #  STEP 6: Clean the mask (remove small spots)
    kernel = np.ones((3, 3), np.uint8)  # Small matrix for cleaning
    cloak_mask = cv2.morphologyEx(cloak_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    cloak_mask = cv2.dilate(cloak_mask, kernel, iterations=1)  # Make cloak edges stronger
    
    # Invert mask: Areas that are NOT cloak
    mask_inv = cv2.bitwise_not(cloak_mask)
    
    #  STEP 7: Replace cloak area with background
    cloak_part = cv2.bitwise_and(background, background, mask=cloak_mask)
    rest_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(cloak_part, 1, rest_part, 1, 0)
    
    #  STEP 8: Show results
    cv2.imshow("🪄 Invisibility Cloak", final_output)  # Main output
    # Uncomment below if you want to see what the computer detects
    # cv2.imshow("Cloak Mask", cloak_mask)
    
    #  STEP 9: Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        print("👋 Exiting...")
        break
    elif key == ord('b'):  # Press 'b' to re-capture background
        print(" Re-capturing background... Stand still!")
        for i in range(60):
            ret, background = cap.read()
            if ret:
                background = cv2.flip(background, 1)
        print(" Background updated!")

#  STEP 10: Release resources
cap.release()
cv2.destroyAllWindows()
