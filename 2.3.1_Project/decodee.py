from PIL import Image

img = Image.open("output.png").convert('RGB')
BLOCK_SIZE = 15  # Must match your encoder
decoded_msg = ""

# 1. FIND THE FIRST BLOCK (Improved)
found_x, found_y = -1, -1

for y in range(img.height):
    for x in range(img.width):
        r, g, b = img.getpixel((x, y))
        if r < 250 or g < 250 or b < 250:
            found_x, found_y = x, y
            break
    if found_x != -1: break

if found_x == -1:
    print("No blocks found.")
    exit()

# NEW STEP: Instead of using the corner, we aim for the center of the first block
start_x = found_x + (BLOCK_SIZE // 2)
start_y = found_y + (BLOCK_SIZE // 2)

print(f"Calibrated center of first block: {start_x}, {start_y}")

# 2. THE SCANNING LOOP
last_chunk = "" # Track the previous 3 characters

for row in range(50): 
    for col in range(20): 
        pixel_x = start_x + (col * BLOCK_SIZE)
        pixel_y = start_y + (row * BLOCK_SIZE)
        
        if pixel_x < img.width and pixel_y < img.height:
            r, g, b = img.getpixel((pixel_x, pixel_y))
            
            if r > 250 and g > 250 and b > 250:
                continue 
            
            try:
                # Convert to characters
                c1, c2, c3 = chr(r), chr(g), chr(b)
                current_chunk = c1 + c2 + c3
                
                # SAFETY CHECK: Only add if it's not a duplicate of the last block
                if current_chunk != last_chunk:
                    decoded_msg += current_chunk
                    last_chunk = current_chunk # Update the tracker
            except:
                continue

print("--- DECODED MESSAGE ---")
print(decoded_msg.strip())