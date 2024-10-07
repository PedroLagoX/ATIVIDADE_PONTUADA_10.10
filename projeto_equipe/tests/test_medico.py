import pytest
from projeto_equipe.models.medico import Medico
from projeto_equipe.models.Endereco import Endereco

endereco3=Endereco("Rua C","40","500","123023-123","Salvador")

@pytest.fixture
def medico_valido():
    return Medico("Caio Fernando","719828213","caiofernando@gmail.com",endereco3,"232302131")


def test_criar_medico_nome(medico_valido):
    assert medico_valido.nome== "Caio Fernando"

def test_criar_medico_telefone(medico_valido):
    assert medico_valido.telefone== "719828213"

def test_criar_medico_email(medico_valido):
    assert medico_valido.email== "caiofernando@gmail.com"

def test_criar_medico_crm(medico_valido):
    assert medico_valido.crm== "232302131"


