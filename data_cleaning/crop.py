import cv2
import os
import shutil

def cut_and_save_img(input_directory, output_directory):
    # Process each file in the input_directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Read the image
        img = cv2.imread(input_path)
        height, width, _ = img.shape

        # Check if the image has greater height than width
        if height > width:
            # Calculate the new height and crop the image (from bottom)
            new_height = width
            img_cropped = img[0:new_height, :]
            cv2.imwrite(output_path, img_cropped)
            print(f"Ritagliata e salvata l'immagine: {output_path}")

        elif width > height:
            # Calculate the new width
            new_width = height
            # Calculate the amount to cut on both sides and crop the image
            cut_amount = (width - new_width) // 2
            img_cropped = img[:, cut_amount:cut_amount + new_width, :]
            cv2.imwrite(output_path, img_cropped)
            print(f"Image cropped and saved: {output_path}")

        else:
            # The image is already square
            shutil.copy2(input_path, output_directory)
            print(f"Copiata l'immagine quadrata: {filename}")

if __name__ == "__main__":
    input_directory = 'percorso/input'
    output_directory = 'percorso/output'

    cut_and_save_img(input_directory, output_directory)

