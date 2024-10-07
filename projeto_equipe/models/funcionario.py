import os 
from projeto_equipe.models.Endereco import Endereco
from abc import ABC


os.system("cls||clear")

class Funcionario(ABC):
    def __init__(self,nome:str,telefone:str,email:str,endereco:Endereco) -> None:
        self.nome=nome
        self.telefone=telefone
        self.email=email
        self.endereco=endereco

    
        
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail:{self.email}"
                f"\nEndereco:{self.endereco}")