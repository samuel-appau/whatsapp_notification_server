import base64
from typing import Tuple

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from config import settings


def decode_encryption_keys(key: str, iv: str):
    decoded_key = bytes(key.encode("latin-1").decode("unicode-escape"), "latin-1")
    decoded_iv = bytes(iv.encode("latin-1").decode("unicode-escape"), "latin-1")
    return decoded_key, decoded_iv


def encrypt_string(plaintext) -> Tuple[bytes, bytes, str]:
    """
    Encrypts the provided plaintext using AES-GCM authenticated encryption mode.

    :param plaintext: The string to be encrypted.
    :param key: The encryption key as bytes(32).
    :param iv: The initialization vector (IV) as bytes(16).
    :return: A tuple containing the ciphertext, authentication tag,
            and ciphertext in Base64 encoding.
    """
    key, iv = decode_encryption_keys(
        key=settings.encryption_key, iv=settings.initialization_vector
    )
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    ciphertext_base64 = base64.b64encode(ciphertext).decode()
    return ciphertext, encryptor.tag, ciphertext_base64


def decrypt_string(ciphertext: bytes, tag: bytes) -> str:
    """
    Decrypts the provided ciphertext using AES-GCM authenticated decryption mode.

    :param ciphertext: The ciphertext to be decrypted.
    :param key: The encryption key used for decryption as bytes.
    :param iv: The initialization vector (IV) used for decryption as bytes.
    :param tag: The authentication tag used for decryption as bytes.
    :return: The decrypted plaintext as a string.
    """
    key, iv = decode_encryption_keys(
        key=settings.encryption_key, iv=settings.initialization_vector
    )
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()
