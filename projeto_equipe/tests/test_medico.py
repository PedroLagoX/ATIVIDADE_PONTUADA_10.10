import pytest
from projeto_equipe.models.medico import Medico
from projeto_equipe.models.endereco import Endereco

@pytest.fixture
def criar_endereco2():
    endereco3=Endereco("Rua C","42","500","0000-000","Salvador")
    return endereco3

@pytest.fixture
def medico_valido(criar_endereco2):
    return Medico("Caio Fernando","719828213","caiofernando@gmail.com",criar_endereco2,"232302131")

def test_criar_medico_nome(medico_valido):
    try:
        assert medico_valido.nome== "Caio Fernando"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_medico_telefone(medico_valido):
    try:
        assert medico_valido.telefone== "719828213"
    except AssertionError as erro:
        print(f"Erro de Asserção: {erro}")
        raise

def test_criar_medico_email(medico_valido):
    try:
        assert medico_valido.email== "caiofernando@gmail.com"
    except AssertionError as erro:
        print(f"Erro de Asserção: {erro}")
        raise

def test_criar_medico_crm(medico_valido):
    try:
        assert medico_valido.crm== "232302131"
    except AssertionError as erro:
        print(f"Erro de Asserção: {erro}")
        raise

def test_criar_endereco_logradouro(criar_endereco2):
    try:
        assert criar_endereco2.logradouro == "Rua C"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_numero(criar_endereco2):
    try:
        assert criar_endereco2.numero == "42"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_complemento(criar_endereco2):
    try:
        assert criar_endereco2.complemento == "500"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cep(criar_endereco2):
    try:
        assert criar_endereco2.cep == "0000-000"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cidade(criar_endereco2):
    try:
        assert criar_endereco2.cidade == "Salvador"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise


