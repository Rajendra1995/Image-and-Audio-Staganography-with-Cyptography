import os
import pathlib
import tkinter as tk
from getpass import getuser
from tkinter.filedialog import askopenfilename

from main import encodeText, finalDecode

global name
global label
global file_status


def mainScreen():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Steganography")

    button = tk.Button(root, text="Encode", bg="grey", font=("Times New Roman", 14), height=2, command=encodeScreen)
    button.grid(row=0, column=0, ipadx="50", pady="50", padx="50")

    button1 = tk.Button(root, text="Decode", bg="grey", font=("Times New Roman", 14), height=2, command=decodeScreen)
    button1.grid(row=1, column=0, ipadx="50", pady="20", padx="50")

    root.mainloop()


def encodeScreen():
    global name
    root = tk.Tk()
    root.geometry("750x700")
    root.title("Steganography")

    # File Selection
    choose_audio_file = tk.Button(root, text="Choose an Audio File", bg="grey", font=("Times New Roman", 14), height=2,
                                  command=lambda: open_file(1))
    choose_audio_file.grid(row=0, column=0, ipadx="50", pady="20", padx="50")

    choose_image_file = tk.Button(root, text="Choose an Image File", bg="grey", font=("Times New Roman", 14), height=2,
                                  command=lambda: open_file(2))
    choose_image_file.grid(row=0, column=1, ipadx="50", pady="20", padx="50")

    # FILE NAME
    global label
    label = tk.Label(root, text="No chosen file")
    label.grid(row=1, column=0, columnspan=2, ipadx="50", ipady="20", pady="20", padx="50")

    # MESSAGE ENTRY
    msg_entry_label = tk.Label(root, text="Enter Secret Message :")
    msg_entry_label.grid(row=2, column=0, ipadx="50", ipady="20", pady="20", padx="50")
    message_entry = tk.Entry(root)
    message_entry.grid(row=2, column=1, ipadx="50", ipady="20", pady="20", padx="50")
    message_entry.insert(0, "Enter your secret msg")

    # FILE NAME
    file_entry_label = tk.Label(root, text="Encoded File Name :")
    file_entry_label.grid(row=3, column=0, ipadx="50", ipady="20", pady="20", padx="50")
    file_entry = tk.Entry(root)
    file_entry.grid(row=3, column=1, ipadx="50", ipady="20", pady="20", padx="50")
    file_entry.insert(0, "Enter encoded file name")

    # NORMAL ENCRYPTION BUTTON
    message_button = tk.Button(root, text="Normal Encryption", bg="grey", font=("Times New Roman", 14), height=2,
                               command=lambda: encodeText(1, name, str(message_entry.get()),
                                                          str(file_entry.get()), msg, file_status))
    message_button.grid(row=4, column=0, ipadx="50", pady="20", padx="50")

    # CIPHERTEXT ENCRYPTION BUTTON

    message_button1 = tk.Button(root, text="Ciphertext Encryption", bg="grey", font=("Times New Roman", 14),
                                height=2,
                                command=lambda: encodeText(2, name, str(message_entry.get()),
                                                           str(file_entry.get()), msg, file_status))
    message_button1.grid(row=4, column=1, ipadx="50", pady="20", padx="50")

    msg_label = tk.Label(root, text="Status :")
    msg_label.grid(row=5, column=0, ipadx="50", ipady="20", pady="20", padx="50")
    # SUCCESS MSG
    msg = tk.Label(root, text="")
    msg.grid(row=5, column=1, ipadx="50", ipady="20", pady="20", padx="50")

    root.mainloop()


def open_file(status):
    global label
    global name
    global file_status
    file_status = status
    """
    This function open the file dialog box for choosing the file.
    And then making two buttons : encrypt_button, decrypt_button
    """
    username = getuser()
    initial_directory = "C:/Users/{}".format(username)
    name = askopenfilename(initialdir=initial_directory,
                           filetypes=[("All Files", "*.*")],
                           title="Choose a file."
                           )
    if name:
        file_name = get_file_name(name, extension=True)
        label.config(text=file_name)


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
    root = tk.Tk()
    root.geometry("750x600")
    root.title("Steganography")
    global name
    choose_audio_file = tk.Button(root, text="Choose an Audio File", bg="grey", font=("Times New Roman", 14), height=2,
                                  command=lambda: open_file(1))
    choose_audio_file.grid(row=0, column=0, ipadx="50", pady="20", padx="50")

    choose_image_file = tk.Button(root, text="Choose an Image File", bg="grey", font=("Times New Roman", 14), height=2,
                                  command=lambda: open_file(2))
    choose_image_file.grid(row=0, column=1, ipadx="50", pady="20", padx="50")

    global label
    label = tk.Label(root, text="No chosen file")
    label.grid(row=1, column=0, columnspan=2, ipadx="50", ipady="20", pady="20", padx="50")

    message_button = tk.Button(root, text="Normal Decryption", bg="grey", font=("Times New Roman", 14), height=2,
                               command=lambda: finalDecode(name, 1, msg, file_status))
    message_button.grid(row=2, column=0, ipadx="50", pady="20", padx="50")

    message_button1 = tk.Button(root, text="Ciphertext Decryption", bg="grey", font=("Times New Roman", 14), height=2,
                                command=lambda: finalDecode(name, 2, msg, file_status))
    message_button1.grid(row=2, column=1, ipadx="50", pady="20", padx="50")

    msg_label = tk.Label(root, text="Your Secret Message :")
    msg_label.grid(row=3, column=0, ipadx="50", ipady="20", pady="20", padx="50")

    msg = tk.Label(root, text="")
    msg.grid(row=3, column=1, ipadx="50", ipady="20", pady="20", padx="50")

    root.mainloop()


if __name__ == "__main__":
    mainScreen()
