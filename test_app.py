import pytest
from app import tambah, kurang, kali, bagi

def test_tambah():
    assert tambah(10, 5) == 15

def test_kurang():
    assert kurang(10, 5) == 5

def test_kali():
    assert kali(4, 5) == 20

def test_bagi():
    assert bagi(20, 4) == 5