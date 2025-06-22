from PIL import Image
import numpy as np

# Helper function to convert a message to binary
def message_to_bin(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message

# Helper function to convert binary to a message
def bin_to_message(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# Function to encode a message into the image
def encode_message(image_path, message, output_image_path):
    image = Image.open(image_path)
    pixels = np.array(image)

    binary_message = message_to_bin(message) + '1111111111111110'  # End of message delimiter

    if len(binary_message) > pixels.size:
        raise ValueError("Message is too long to encode in the given image.")

    binary_index = 0

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(pixels.shape[2]):
                if binary_index < len(binary_message):
                    pixel_bin = format(pixels[i, j, k], '08b')
                    new_pixel_bin = pixel_bin[:-1] + binary_message[binary_index]
                    pixels[i, j, k] = int(new_pixel_bin, 2)
                    binary_index += 1

    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_image_path)
    print(f"Message encoded and saved as {output_image_path}")

# Function to decode the message from an image
def decode_message(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)

    binary_message = ""
    
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(pixels.shape[2]):
                binary_message += format(pixels[i, j, k], '08b')[-1]
                if binary_message[-16:] == '1111111111111110':  # End of message delimiter
                    return bin_to_message(binary_message[:-16])
    
    raise ValueError("No message found in the image.")

# Example usage:
# Encode a message into the image
encode_message('input_image.png', 'hellolion', 'output_image.png')

# Decode the message from the image
message = decode_message('output_image.png')
print(f"Decoded message: {message}")
