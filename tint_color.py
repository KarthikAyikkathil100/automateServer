from PIL import Image
import numpy as np
import os
from helpers import upload_multiple_files


image_directory_path = 'old_arrows/'
new_image_directory_path = 'images/'
bucket_name = 'media.rtme.us'
files = os.listdir(image_directory_path)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return (r, g, b)
    raise ValueError("Input should be a 6-character hex code.")

def tint_image(hex, env = 'dev'):
    try:
        r, g, b = hex_to_rgb(hex)
        new_color = (r, g, b) # Your desired color
        hex_color = hex.lstrip('#')

        for file_name in files:
            # Open image with alpha channel

            img = Image.open(f'{image_directory_path}{file_name}').convert('RGBA')
            img_np = np.array(img)

            # Separate channels
            r, g, b, a = img_np[:, :, 0], img_np[:, :, 1], img_np[:, :, 2], img_np[:, :, 3]

            # Calculate brightness (simple average or use luminosity)
            brightness = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0  # Normalize to 0–1

            # Target color (R, G, B)
            tr, tg, tb = new_color

            # Multiply brightness by target color
            new_r = (brightness * tr).astype(np.uint8)
            new_g = (brightness * tg).astype(np.uint8)
            new_b = (brightness * tb).astype(np.uint8)

            # Combine new RGB with original alpha
            tinted = np.stack([new_r, new_g, new_b, a], axis=-1)

            # Save result
            tinted_img = Image.fromarray(tinted, mode='RGBA')
            tinted_img.save(f'{new_image_directory_path}{hex_color}-{file_name}')

        # Upload the files to S3
        upload_color_arrows(hex_color, env)
        return True
    except Exception as e:
        print('Error in tint_color_arrows() fn')
        print(e)
        return None
    



def upload_color_arrows(hex_color, env):
    try:
        keys = ['left-arrow.png', 'right-arrow.png', 'slight-left-arrow.png', 'slight-right-arrow.png', 'straight-arrow.png']
        upload_keys = []
        for arrow_name in keys:
            local_path = f'images/{hex_color}-{arrow_name}'
            s3_path = f'{env}/location_arrows/{hex_color}-{arrow_name}'
            upload_keys.append((local_path, s3_path))
        upload_multiple_files(upload_keys, bucket_name)
    except Exception as e:
        return None