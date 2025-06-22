# Steganography: Hiding Messages in Images

## Introduction
This project demonstrates a simple implementation of steganography, a technique used to hide secret messages inside images without altering their appearance. By modifying the Least Significant Bits (LSB) of image pixels, we can embed text messages in a way that remains undetectable to the human eye. This README file provides an overview of the project, the Python code, and instructions for using the solution.

## Problem Statement
Traditional encryption methods, while secure, can be easily detectable, raising suspicion about the communication. There is a need for a method to hide confidential messages within images in a way that ensures data security while maintaining the integrity of the cover image. Additionally, the solution should be accessible to non-technical users through a simple interface.

## Solution
This project uses steganography to encode and decode messages within images by modifying the Least Significant Bits (LSB) of pixel values. The approach maintains the original appearance of the image while securely hiding the message. Users can easily interact with the tool to encode or decode messages through a simple interface.

## Features
- Invisible message embedding into images.
- Maintains image quality and appearance.
- User-friendly encoding and decoding functions for easy usage.
- Cross-platform capability, works on various image file formats (e.g., PNG, BMP).

## Technologies Used
- **Python**: The core programming language used for the project.
- **PIL (Pillow)**: A Python imaging library used to handle images.

## How it Works
The project uses the Least Significant Bit (LSB) method, where each pixel's least significant bit is modified to encode a binary representation of the message. This change is subtle and does not alter the appearance of the image noticeably.

### Code Implementation
#### Dependencies
```bash
pip install pillow
```

#### Encoding the Message into an Image
```python
from PIL import Image

# Function to convert a message to binary
def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

# Function to encode a message into an image
def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()
    binary_message = message_to_binary(message) + '1111111111111110'  # Delimiter
    binary_message_index = 0
    pixels = encoded_image.load()

    for i in range(encoded_image.size[0]):
        for j in range(encoded_image.size[1]):
            pixel = list(pixels[i, j])
            for n in range(3):  # Modify RGB values
                if binary_message_index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[binary_message_index])
                    binary_message_index += 1
            pixels[i, j] = tuple(pixel)

    encoded_image.save(output_path)
    print(f'Message encoded and saved to {output_path}')

# Example usage
encode_message('cover_image.png', 'Secret message', 'encoded_image.png')
```

#### Decoding the Message from an Image
```python
# Function to decode the hidden message from an image

def decode_message(image_path):
    image = Image.open(image_path)
    binary_message = ''
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = list(pixels[i, j])
            for n in range(3):  # Read RGB values
                binary_message += str(pixel[n] & 1)

    # Split binary data by 8 bits and stop at the delimiter
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    delimiter_index = message.find('1111111111111110')

    return message[:delimiter_index] if delimiter_index != -1 else message

# Example usage
secret_message = decode_message('encoded_image.png')
print(f'Decoded message: {secret_message}')
```

## How to Use the Project
### Encoding a Message
1. Install the required dependencies using the command:
   ```bash
   pip install pillow
   ```
2. Use the `encode_message()` function, providing the path to the cover image, the message to encode, and the output image path. For example:
   ```python
   encode_message('cover_image.png', 'Your secret message', 'encoded_image.png')
   ```
   This will save the encoded image as `encoded_image.png`.

### Decoding a Message
1. Use the `decode_message()` function, providing the path to the image containing the hidden message:
   ```python
   secret_message = decode_message('encoded_image.png')
   print(secret_message)
   ```
   This will decode and print the hidden message from the image.

## Wow Factors
- **Undetectable Communication**: The hidden message is virtually impossible to detect visually.
- **Easy to Use**: The project provides simple functions for encoding and decoding, accessible even to non-technical users.
- **High Image Quality**: The image remains unchanged to the human eye after embedding the message.
- **Extensible**: The solution can be scaled to work with various file types or larger messages.

## Future Scope
- **Integration with AI**: Use AI-based techniques to make steganography even more secure and undetectable.
- **Quantum-Resistant Steganography**: Develop techniques resistant to quantum decryption.
- **Application in IoT**: Embed hidden messages in IoT devices for secure communication.

## Conclusion
This project provides a simple and effective solution for hiding confidential messages in images using steganography. With its user-friendly interface and undetectable message embedding, it is a practical tool for secure communication and data protection in various fields, including journalism, cybersecurity, and digital forensics.

