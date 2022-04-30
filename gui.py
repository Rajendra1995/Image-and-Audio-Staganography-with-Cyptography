import os
import pathlib
import tkinter as tk
from getpass import getuser
from tkinter.filedialog import askopenfilename
from main import encodeText, finalDecode
from PIL import Image, ImageTk

global name, label_txt, message_file, msg_file
global label
global file_status


def mainScreen():
    root = tk.Tk()
    root.title("Steganography")
    root.maxsize(width=400, height=400)
    root.geometry("400x400")
    # Adding a background image
    background_image = Image.open("bg.jpg")

    newImageSizeWidth = 400
    newImageSizeHeight = 400

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
    Canvas1 = tk.Canvas(root)
    img = ImageTk.PhotoImage(background_image)
    Canvas1.create_image(0, 0, image=img, anchor="nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    headingFrame1 = tk.Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = tk.Label(headingFrame1, text="Welcome to \n Steganography",
                            bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    btn1 = tk.Button(root, text="Encoding", bg='black', fg='white', command=encodeScreen)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = tk.Button(root, text="Decoding", bg='black', fg='white', command=decodeScreen)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    root.mainloop()


def encodeScreen():
    global name, msg_file
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Steganography Encoding")
    root.maxsize(width=1000, height=900)
    canvas1 = tk.Canvas(root)
    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill="both")

    # HEADING
    headingFrame1 = tk.Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=0.1)

    headingLabel = tk.Label(headingFrame1, text="Encoding", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # File Selection
    labelFrame = tk.Frame(root, bg='#FFBB00', bd=5)
    labelFrame.place(relx=0.05, rely=0.17, relwidth=0.9, relheight=0.75)

    choose_audio_file = tk.Button(labelFrame, text="Choose an Audio File", bg="grey", font=("Times New Roman", 14),
                                  height=2,
                                  command=lambda: open_file(1))
    choose_audio_file.place(relx=0.1, rely=0.05, relwidth=0.35, relheight=0.08)

    choose_image_file = tk.Button(labelFrame, text="Choose an Image File", bg="grey", font=("Times New Roman", 14),
                                  height=2,
                                  command=lambda: open_file(2))
    choose_image_file.place(relx=0.55, rely=0.05, relwidth=0.35, relheight=0.08)

    # FILE NAME
    global label, label_txt
    label = tk.Label(labelFrame, text="No chosen file")
    label.place(relx=0.3, rely=.16, relwidth=0.4, relheight=0.08)

    # MESSAGE ENTRY
    msg_entry_label = tk.Label(labelFrame, text="Enter Secret Message :")
    msg_entry_label.place(relx=0.1, rely=.26, relwidth=0.25, relheight=0.08)
    message_entry = tk.Entry(labelFrame)
    message_entry.place(relx=0.4, rely=.26, relwidth=0.5, relheight=0.08)
    message_entry.insert(0, "Enter your secret msg")

    # Message file
    choose_message_file = tk.Button(labelFrame, text="Choose a Txt file", bg="grey", font=("Times New Roman", 14),
                                    height=2, command=lambda: open_file(3))
    choose_message_file.place(relx=0.1, rely=0.37, relwidth=0.30, relheight=0.08)

    label_txt = tk.Label(labelFrame, text="No Message file Selected")
    label_txt.place(relx=0.5, rely=.37, relwidth=0.4, relheight=0.08)

    # FILE NAME
    file_entry_label = tk.Label(labelFrame, text="New Encoded File Name :")
    file_entry_label.place(relx=0.1, rely=.49, relwidth=0.25, relheight=0.08)
    file_entry = tk.Entry(labelFrame)
    file_entry.place(relx=0.4, rely=0.49, relwidth=0.5, relheight=0.08)
    file_entry.insert(0, "Enter encoded file name")

    # NORMAL ENCRYPTION BUTTON
    message_button = tk.Button(labelFrame, text="Normal Encryption", bg="grey", font=("Times New Roman", 14), height=2,
                               command=lambda: encodeText(1, name, str(message_entry.get()),
                                                          str(file_entry.get()), msg, file_status, msg_file))
    message_button.place(relx=0.1, rely=0.62, relwidth=0.35, relheight=0.08)

    # CIPHERTEXT ENCRYPTION BUTTON

    message_button1 = tk.Button(labelFrame, text="Ciphertext Encryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: encodeText(2, name, str(message_entry.get()),
                                                           str(file_entry.get()), msg, file_status, msg_file))
    message_button1.place(relx=0.55, rely=0.62, relwidth=0.35, relheight=0.08)

    # Hybrid Encryption
    # RSA ENCRYPTION BUTTON

    message_button3 = tk.Button(labelFrame, text="Hybrid Encryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: encodeText(4, name, str(message_entry.get()),
                                                           str(file_entry.get()), msg, file_status, msg_file))
    message_button3.place(relx=0.1, rely=0.76, relwidth=0.35, relheight=0.08)

    # RSA ENCRYPTION BUTTON

    message_button2 = tk.Button(labelFrame, text="RSA Encryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: encodeText(3, name, str(message_entry.get()),
                                                           str(file_entry.get()), msg, file_status, msg_file))
    message_button2.place(relx=0.55, rely=0.76, relwidth=0.35, relheight=0.08)

    # Message
    msg_label = tk.Label(labelFrame, text="Status :")
    msg_label.place(relx=0.1, rely=0.90, relwidth=0.25, relheight=0.08)
    # SUCCESS MSG
    msg = tk.Label(labelFrame, text="")
    msg.place(relx=0.4, rely=0.90, relwidth=0.5, relheight=0.08)

    root.mainloop()


def open_file(status):
    global label, message_file, msg_file
    global name
    global file_status
    """
    This function open the file dialog box for choosing the file.
    And then making two buttons : encrypt_button, decrypt_button
    """
    if status == 1:
        file_status = status
        username = getuser()
        initial_directory = "C:/Users/{}".format(username)
        name = askopenfilename(initialdir=initial_directory,
                               filetypes=[("Audio Files", "*.wav"), ("Audio Files", "*.mp3")],
                               title="Choose a file."
                               )
        if name:
            file_name = get_file_name(name, extension=True)
            label.config(text=file_name)

    elif status == 2:
        file_status = status
        username = getuser()
        initial_directory = "C:/Users/{}".format(username)
        name = askopenfilename(initialdir=initial_directory,
                               filetypes=[("Image Files", "*.png"), ("Image Files", "*.jpg"),
                                          ("Image Files", "*.jpeg")],
                               title="Choose a file."
                               )
        if name:
            file_name = get_file_name(name, extension=True)
            label.config(text=file_name)

    elif status == 3:
        username = getuser()
        initial_directory = "C:/Users/{}".format(username)
        message_file = askopenfilename(initialdir=initial_directory,
                                       filetypes=[("Image Files", "*.txt")],
                                       title="Choose a file.")
        f = open(message_file, 'r')
        msg_file = f.read()
        print(msg_file)

        if name:
            file_name = get_file_name(name, extension=True)
            label_txt.config(text=file_name)


def get_file_name(file_path, extension=False):
    """Returns file name from given path
    either with extension or without extension

    :param file_path:
    :param extension:
    :return file_name:
    """
    if not extension:
        file_name = pathlib.Path(file_path).stem

    else:
        file_name = os.path.basename(file_path)

    return file_name


def decodeScreen():
    global name
    global label
    root = tk.Tk()
    root.geometry("750x600")
    root.title("Steganography Decoding")
    root.maxsize(width=1000, height=900)

    canvas1 = tk.Canvas(root)
    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill="both")

    # HEADING
    headingFrame1 = tk.Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=0.1)

    headingLabel = tk.Label(headingFrame1, text="Decoding", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # File Selection
    labelFrame = tk.Frame(root, bg='#FFBB00', bd=5)
    labelFrame.place(relx=0.05, rely=0.17, relwidth=0.9, relheight=0.75)

    choose_audio_file = tk.Button(labelFrame, text="Choose an Audio File", bg="grey", font=("Times New Roman", 14),
                                  height=2,
                                  command=lambda: open_file(1))
    choose_audio_file.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.08)

    choose_image_file = tk.Button(labelFrame, text="Choose an Image File", bg="grey", font=("Times New Roman", 14),
                                  height=2,
                                  command=lambda: open_file(2))
    choose_image_file.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.08)

    # FILE NAME

    label = tk.Label(labelFrame, text="No chosen file")
    label.place(relx=0.3, rely=.22, relwidth=0.4, relheight=0.08)

    message_button = tk.Button(labelFrame, text="Normal Decryption", bg="grey", font=("Times New Roman", 14), height=2,
                               command=lambda: finalDecode(name, 1, msg, file_status))
    message_button.place(relx=0.1, rely=0.34, relwidth=0.35, relheight=0.08)

    message_button1 = tk.Button(labelFrame, text="Ciphertext Decryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: finalDecode(name, 2, msg, file_status))
    message_button1.place(relx=0.55, rely=0.34, relwidth=0.35, relheight=0.08)

    message_button1 = tk.Button(labelFrame, text="Hybrid Decryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: finalDecode(name, 4, msg, file_status))
    message_button1.place(relx=0.1, rely=0.46, relwidth=0.35, relheight=0.08)

    message_button1 = tk.Button(labelFrame, text="RSA Decryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: finalDecode(name, 3, msg, file_status))
    message_button1.place(relx=0.55, rely=0.46, relwidth=0.35, relheight=0.08)

    # Message
    msg_label = tk.Label(labelFrame, text="Your Secret Message :")
    msg_label.place(relx=0.1, rely=0.58, relwidth=0.25, relheight=0.08)

    msg = tk.Label(labelFrame, text="")
    msg.place(relx=0.4, rely=0.58, relwidth=0.5, relheight=0.08)

    root.mainloop()


if __name__ == "__main__":
    mainScreen()
