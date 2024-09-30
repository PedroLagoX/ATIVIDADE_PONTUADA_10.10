from projeto_equipe.models.Endereco import Endereco
from projeto_equipe.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    
    def __str__(self) -> str:
        return (f"{super().__str__()} \nCRM: {self.crm}")