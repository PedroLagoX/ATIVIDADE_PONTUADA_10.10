import pytest
from ..models.Endereco import Endereco
from projeto_equipe.models.Endereco import Endereco

@pytest.fixture

def criar_endereco():
    endereco_1 = Endereco("", "", "", "", "")
    return endereco_1

def test_criar_endereco_logradouro(criar_endereco):
    try:
        assert criar_endereco.logradouro == "Rua A"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_numero(criar_endereco):
    try:
        assert criar_endereco.numero == "123"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_complemento(criar_endereco):
    try:
        assert criar_endereco.complemento == "ap0"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cep(criar_endereco):
    try:
        assert criar_endereco.cep == "0000-000"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cidade(criar_endereco):
    try:
        assert criar_endereco.cidade == "Salvador"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise
