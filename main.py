import cv2
import numpy as np
from encryption import encrypt
from decryption import decrypt
from audioencoder import decode, encode


def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


# Function to hide the secret message into the image

def hideData(image, secret_message):
    # calculate the maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maximum bytes to encode:", n_bytes)

    # Check if the number of bytes to encode is less than the maximum bytes in the image
    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")

    secret_message += "#####"  # you can use any string as the delimeter

    data_index = 0
    # convert input data to binary format using messageToBinary() fucntion
    binary_secret_msg = messageToBinary(secret_message)

    data_len = len(binary_secret_msg)  # Find the length of data that needs to be hidden
    for values in image:
        for pixel in values:
            # convert RGB values to binary format
            r, g, b = messageToBinary(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # hide the data into least significant bit of red pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of green pixel
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of  blue pixel
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break

    return image


def showData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel)  # convert the red,green and blue values into binary format
            binary_data += r[-1]  # extracting data from the least significant bit of red pixel
            binary_data += g[-1]  # extracting data from the least significant bit of red pixel
            binary_data += b[-1]  # extracting data from the least significant bit of red pixel
    # split by 8-bits
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # check if we have reached the delimeter which is "#####"
            break
    # print(decoded_data)
    return decoded_data[:-5]  # remove the delimeter to show the original hidden message


# Encode data into image
def encodeText(status, img_name, data, file_nam, msg, file_status):
    if file_status == 1:
        encode(status, img_name, data, file_nam, msg)
    else:
        image = cv2.imread(img_name)  # Read the input image using OpenCV-Python.
        # It is a library of Python bindings designed to solve computer vision problems.

        if len(data) == 0:
            raise ValueError('Data is empty')

        if status == 2:
            enc_data, key = encrypt(data)
            final_data = enc_data + str(key)
        else:
            final_data = data
        filename = str(file_nam) + ".png"
        encoded_image = hideData(image, final_data)
        cv2.imwrite(filename, encoded_image)
        txt = f" |---->successfully encoded inside {file_nam}"
        msg.config(text=txt)


# Decode the data in the image
def decodeText(img_name):
    # read the image that contains the hidden image

    image = cv2.imread(img_name)  # read the image using cv2.imread()

    text = showData(image)
    return text


def finalDecode(img_name, status, msg, file_status):
    if file_status == 1:
        decode(img_name, status, msg)
    else:
        decoded = decodeText(img_name)
        if status == 2:
            de = decoded.split("b'")
            message = de[0]
            key = de[1][0:-1]
            message = decrypt(message, key)
        else:
            message = decoded

        msg.config(text=message)
