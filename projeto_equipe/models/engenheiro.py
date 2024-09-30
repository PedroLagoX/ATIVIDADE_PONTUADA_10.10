from projeto_equipe.models.Endereco import Endereco
from projeto_equipe.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def __str__(self) -> str:
        return (f"{super().__str__()} \nCREA: {self.crea}")