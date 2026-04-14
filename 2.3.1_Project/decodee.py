from PIL import Image

img = Image.open("output.png").convert('RGB')
block_image = 15  
decoded_msg = ""

#1. Find the first block
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


start_x = found_x + (block_size // 2)
start_y = found_y + (block_size // 2)

print(f"Calibrated center of first block: {start_x}, {start_y}")

#2. Loop to go through the blocks
last_chunk = "" # Track the previous 3 characters

for row in range(50): 
    for col in range(20): 
        pixel_x = start_x + (col * block_size)
        pixel_y = start_y + (row * block_size)
        
        if pixel_x < img.width and pixel_y < img.height:
            r, g, b = img.getpixel((pixel_x, pixel_y))
            
            if r > 250 and g > 250 and b > 250:
                continue 
            
            try:
                # Convert to characters
                c1, c2, c3 = chr(r), chr(g), chr(b)
                current_chunk = c1 + c2 + c3
                
                # Safety check: Only add to the decoded message if it's not a duplicate of the last block
                if current_chunk != last_chunk:
                    decoded_msg += current_chunk
                    last_chunk = current_chunk # Update the tracker
            except:
                continue

print("--- DECODED MESSAGE ---")
print(decoded_msg.strip())
