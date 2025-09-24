import pytest
from vigenere import encrypt, decrypt

def test_encrypt_simple():
    assert encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"

def test_decrypt_simple():
    assert decrypt("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"

def test_encrypt_lowercase():
    assert encrypt("attackatdawn", "lemon") == "LXFOPVEFRNHR"

def test_decrypt_lowercase():
    assert decrypt("lxfopvefrnhr", "lemon") == "ATTACKATDAWN"

def test_encrypt_with_spaces_and_punct():
    assert encrypt("ATTACK AT DAWN!", "LEMON") == "LXFOPV EF RNHR!"

def test_decrypt_with_spaces_and_punct():
    assert decrypt("LXFOPV EF RNHR!", "LEMON") == "ATTACK AT DAWN!"
