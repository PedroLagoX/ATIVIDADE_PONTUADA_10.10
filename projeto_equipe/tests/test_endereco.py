import pytest
from ..models.Endereco import Endereco
from projeto_equipe.models.Endereco import Endereco

@pytest.fixture

def criar_endereco():
    endereco_1 = Endereco("Rua A", "123", "ap0", "0000-000", "Salvador")
    return endereco_1

def test_criar_endereco_logradouro(criar_endereco):
    assert criar_endereco.logradouro == "Rua A"

def test_criar_endereco_numero(criar_endereco):
    assert criar_endereco.numero == "123"

def test_criar_endereco_complemento(criar_endereco):
    assert criar_endereco.complemento == "ap0"

def test_criar_endereco_cep(criar_endereco):
    assert criar_endereco.cep == "0000-000"

def test_criar_endereco_cidade(criar_endereco):
    assert criar_endereco.cidade == "Salvador"
