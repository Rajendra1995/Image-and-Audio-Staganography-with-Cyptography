import wave
from encryption import encrypt
from decryption import decrypt
import RSA_Encryption


def encode(status, audio_name, data, file_nam, msg):
    audio = wave.open(audio_name, mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    if status == 2:
        enc_data, file_name = encrypt(data)
        string = enc_data + str(file_name)

    elif status == 3:
        string1 = RSA_Encryption.Encrypt(data)
        string = [str(i) for i in string1]
        string = "a".join(string)

    elif status == 4:
        final_data = RSA_Encryption.Encrypt(data)
        string = [str(i) for i in final_data]
        final_data = "a".join(string)

        enc_data, key = encrypt(final_data)
        string = enc_data + str(key)

    else:
        string = data

    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    for i in range(0, 10):
        pass
        # print(frame_bytes[i])
    file_nam = str(file_nam) + ".wav"
    newAudio = wave.open(file_nam, 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)

    newAudio.close()
    audio.close()
    txt = f" |---->successfully encoded inside {file_nam}"
    msg.config(text=txt)


def decode(audio_name, status, msg):
    audio = wave.open(audio_name, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    audio.close()
    message = decoded
    if status == 2:
        de = decoded.split("b'")
        message = de[0]
        key = de[1][0:-1]
        message = decrypt(message, key)
    elif status == 3:
        string = decoded.split('a')
        message = RSA_Encryption.Decrypt(string)

    elif status == 4:
        de = decoded.split("b'")
        message = de[0]
        key = de[1][0:-1]
        message = decrypt(message, key)
        string = message.split('a')
        message = RSA_Encryption.Decrypt(string)

    msg.config(text=message)
