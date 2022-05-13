import base64

with open('encoded_msg.b64', 'r') as archivo_encrypt:
    mensaje = archivo_encrypt.readlines()


def decodes(a):
    mensaje2 = ' '.join(a)

    mensaje_bytes = base64.b64decode(mensaje2)

    return mensaje_bytes.decode()


def decode_file():
    with open('mystery_img1.txt', 'rb') as image_dec:
        imagen_bytes = image_dec.readlines()
        imagen_str = b''
        for i in imagen_bytes:
            imagen_str += i
    with open('imagen_decodificada.png', 'wb') as imagen_final:
        imagen_data = base64.decodebytes(imagen_str)
        imagen_final.write(imagen_data)


def encode_file():
    with open('uanl.png', 'rb') as imagen_uanl:
        imagen_data2 = imagen_uanl.read()
        imagen_base64 = base64.b64encode(imagen_data2)
        imagen_info = imagen_base64.decode('utf-8')
        print(imagen_info)


encode_file()
decode_file()
print(decodes(mensaje))
