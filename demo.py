# 🧙 Harry Potter Invisibility Cloak with OpenCV
# 📚 Super easy explanation for school kids!

# 🔹 Importing libraries we need
import cv2      # OpenCV: A library that helps us work with cameras and images
import numpy as np  # Numpy: Helps us with math and image processing
import time     # Time: To add short breaks in the program

# 🎥 STEP 1: Start the camera
cap = cv2.VideoCapture(0)  # 0 means "use the laptop's main camera"
if not cap.isOpened():  # If camera is NOT found
    print("❌ Camera not found! Plug in a webcam or try 1 or 2 instead of 0.")
    exit()  # Stop the program

# Give the camera 2 seconds to get ready (adjust lighting)
time.sleep(2)

# 🎨 STEP 2: Take a photo of the background (without you in the frame)
print("📸 Capturing background... Stand still for 3 seconds!")
for i in range(60):  # Take 60 pictures quickly to make it smooth
    ret, background = cap.read()  # ret=True if camera worked, background=image
    if ret:
        background = cv2.flip(background, 1)  # Flip it like a mirror
print("✅ Background captured!")

# 🟥 STEP 3: Choose cloak color (we’re using RED)
# HSV is a way to represent colors: Hue, Saturation, Value
lower_red1 = np.array([0, 120, 70])     # Lowest red shade
upper_red1 = np.array([10, 255, 255])   # Highest red shade
lower_red2 = np.array([170, 120, 70])   # Red has a wrap-around range
upper_red2 = np.array([180, 255, 255])  # Second red range

print("🪄 Starting Invisibility Cloak! Press 'ESC' to quit, 'b' to re-capture background.")

# 🔄 STEP 4: Start video streaming
while cap.isOpened():  # Keep running until we say stop
    ret, frame = cap.read()  # Take a photo from camera
    if not ret:  # If camera fails
        break
    
    # Flip the frame like a mirror
    frame = cv2.flip(frame, 1)
    
    # Convert colors to HSV (better for detecting colors)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 🎭 STEP 5: Create a mask to find cloak parts
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)  # First red range
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)  # Second red range
    cloak_mask = mask1 + mask2  # Combine both masks
    
    # 🧽 STEP 6: Clean the mask (remove tiny dots)
    kernel = np.ones((3, 3), np.uint8)  # A tiny 3x3 square for cleaning
    cloak_mask = cv2.morphologyEx(cloak_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    cloak_mask = cv2.dilate(cloak_mask, kernel, iterations=1)  # Make edges stronger
    
    # Invert the mask to get everything else (not cloak)
    mask_inv = cv2.bitwise_not(cloak_mask)
    
    # 🖼️ STEP 7: Replace cloak with background
    cloak_part = cv2.bitwise_and(background, background, mask=cloak_mask)
    rest_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(cloak_part, 1, rest_part, 1, 0)
    
    # 👀 STEP 8: Show the magic!
    cv2.imshow("🪄 Invisibility Cloak", final_output)  # Main screen
    # cv2.imshow("Cloak Mask", cloak_mask)  # Uncomment to see cloak detection
    
    # 🎮 STEP 9: Controls
    key = cv2.waitKey(1) & 0xFF  # Wait for a key
    if key == 27:  # ESC key
        print("👋 Exiting...")
        break
    elif key == ord('b'):  # 'b' to reset background
        print("♻️ Re-capturing background... Stand still!")
        for i in range(60):
            ret, background = cap.read()
            if ret:
                background = cv2.flip(background, 1)
        print("✅ Background updated!")

# 🧹 STEP 10: Cleanup
cap.release()  # Stop the camera
cv2.destroyAllWindows()  # Close all windows
