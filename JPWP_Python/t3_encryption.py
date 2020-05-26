import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import json

############################################################
###                                                      ###
###---------------_USE !__CBC__! AES MODE_---------------###
###                                                      ###
############################################################

# TODO: Use !__lambda expressions__! to make pad() and unpad() functions
BLOCK_SIZE = 16
pad = lambda x: x + (BLOCK_SIZE - len(x) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(x) % BLOCK_SIZE)
unpad = lambda x: x[:-ord(x[len(x) - 1:])]


# TODO: Function below.
# The harder way is to use PBDKF2 function, but also the more secure way. If you will use it, you need to have salt.
# As salt use phrase: salt = b"Salty_MrPass_So_Salty"
def get_priv_key(password):
    """
    Function to generate AES encryption key
    :param password:
    :return: hash:
    """
    return hashlib.sha256(password.encode()).digest()


# TODO: Function below. Remember to fill the padding, so that blocks are full
def encrypt(raw_data, password):
    """
    Function used to encrypt data
    :param raw_data:
    :param password:
    :return: Encrypted data 
    """
    priv_key = get_priv_key(password)
    raw = pad(raw_data)
    i = Random.new().read(AES.block_size)
    ciph = AES.new(priv_key, AES.MODE_CBC, i)
    return i + ciph.encrypt(raw.encode('utf-8'))


# TODO: Function below. Remember to unpad decryprted data
def decrypt(encrypted_data, password):
    """
    Function used to decrypt data
    :param encrypted_data:
    :param password:
    :return:
    """
    private_key = get_priv_key(password)
    # enc = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data[16:]))

############################################################
###                                                      ###
###--------------DO NOT TOUCH MAIN FUNCTION--------------###
###                                                      ###
############################################################
if __name__ == "__main__":
    passwd = "JpWp_4W50#3_3nCrYpT10n_T45k"
    with open('./local.json', 'r') as fin:
        data = json.load(fin)
        fin.close()

    print(data)
    print()
    enc = encrypt(str(data), passwd)
    print(enc)
    print()
    dec = decrypt(enc, passwd)
    print(dec)
