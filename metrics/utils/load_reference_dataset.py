import tensorflow as tf
import os


# This function loads a style dataset from the specified directory path
def load_style_dataset(path, image_size=(256, 256)):
    # Initializing an empty list of images
    images = []
    for root, _, files in os.walk(path):
        for file in files:
            # Get the file_path by merging the path to the current directory (root) with the filename
            file_path = os.path.join(root, file)
            # Reads the contents of the file as a string
            img = tf.io.read_file(file_path)
            # Decodes the image string into an image tensor
            img = tf.image.decode_image(img, channels=3)
            img = tf.image.resize(img, image_size)
            # Adds a dimension to the image at the beginning of the tensor
            img = tf.expand_dims(img, 0)
            images.append(img)  # 0-255

    # Tensor representing the style dataset (concatenated style images along the 0 axis)
    return tf.concat(images, axis=0)