import pytest
from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.Endereco import Endereco



endereco2=Endereco("Rua B","41","600","321021-213","Salvador")

@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Julio Cesar","7198291283","juliocesar@gmail.com",endereco2,"67732421")


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

