import pytest
from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.endereco import Endereco


@pytest.fixture
def criar_endereco():
    endereco2=Endereco("Rua B","41","600","321021-213","Salvador")
    return endereco2

@pytest.fixture
def engenheiro_valido(criar_endereco):
    return Engenheiro("Julio Cesar","7198291283","juliocesar@gmail.com",criar_endereco,"67732421")


def test_criar_engenheiro_nome(engenheiro_valido):
    try:
        assert engenheiro_valido.nome== "Julio Cesar"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise
def test_criar_engenheiro_telefone(engenheiro_valido):
    try:
        assert engenheiro_valido.telefone== "7198291283"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise
def test_criar_engenheiro_email(engenheiro_valido):
    try:
        assert engenheiro_valido.email== "juliocesar@gmail.com"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise
def test_criar_engenheiro_crea(engenheiro_valido):
    try:
        assert engenheiro_valido.crea== "67732421"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
    
        raise

def test_criar_endereco_logradouro(criar_endereco):
    try:
        assert criar_endereco.logradouro == "Rua B"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_numero(criar_endereco):
    try:
        assert criar_endereco.numero == "41"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_complemento(criar_endereco):
    try:
        assert criar_endereco.complemento == "600"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cep(criar_endereco):
    try:
        assert criar_endereco.cep == "321021-213"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

def test_criar_endereco_cidade(criar_endereco):
    try:
        assert criar_endereco.cidade == "Salvador"
    except AssertionError as erro:
        print(f"Erro de Asserção:{erro}")
        raise

