# 🪄 Harry Potter Invisibility Cloak (White Edition)

import cv2
import numpy as np
import time

# 🎥 STEP 1: Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not found! Try changing index to 1 or 2.")
    exit()

time.sleep(2)  # Allow camera to adjust lighting

# 🖼️ STEP 2: Capture background
print("📸 Capturing background... Stand still!")
for i in range(60):
    ret, background = cap.read()
    if ret:
        background = cv2.flip(background, 1)
print("✅ Background captured!")

# 🎨 STEP 3: Define white color range in HSV
# White = Low Saturation (S), High Brightness (V)
lower_white = np.array([0, 0, 200])     # Lower bound for white
upper_white = np.array([180, 40, 255])  # Upper bound for white

print("🎬 White cloak mode ON! Press ESC to quit, B to reset background.")

# 🖥️ STEP 4: Start capturing frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Mirror view
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV
    
    # 🖌️ STEP 5: Create mask for white cloak
    cloak_mask = cv2.inRange(hsv, lower_white, upper_white)
    
    # 🧹 STEP 6: Clean the mask (remove noise)
    kernel = np.ones((3, 3), np.uint8)
    cloak_mask = cv2.morphologyEx(cloak_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    cloak_mask = cv2.dilate(cloak_mask, kernel, iterations=1)
    mask_inv = cv2.bitwise_not(cloak_mask)
    
    # 🪄 STEP 7: Replace white cloak area with background
    cloak_area = cv2.bitwise_and(background, background, mask=cloak_mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)
    
    # 🎥 STEP 8: Show output
    cv2.imshow("🪄 Invisibility Cloak (White)", final_output)
    # cv2.imshow("Mask Debug", cloak_mask)  # Uncomment to see detection mask
    
    # 🎮 STEP 9: Controls
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to quit
        print("👋 Exiting...")
        break
    elif key == ord('b'):  # B to recapture background
        print("♻️ Re-capturing background...")
        for i in range(60):
            ret, background = cap.read()
            if ret:
                background = cv2.flip(background, 1)
        print("✅ Background updated!")

# 🛑 STEP 10: Release resources
cap.release()
cv2.destroyAllWindows()
