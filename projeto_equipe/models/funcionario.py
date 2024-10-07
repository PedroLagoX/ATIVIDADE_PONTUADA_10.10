import os 
from projeto_equipe.models.Endereco import Endereco
from abc import ABC


os.system("cls||clear")

class Funcionario(ABC):
    def __init__(self,nome:str,telefone:str,email:str,endereco:Endereco) -> None:
        self.nome=self.__verificar_nome(nome)
        self.telefone=self.__verificar_telefone(telefone)
        self.email=self.__verificar_email(email)
        self.endereco=endereco

    
        
    def __verificar_email(self,email):
        try:
            if not email:
                raise ValueError("O email não pode estar vazio")
            if not isinstance(email,str):
                raise TypeError("O email só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)


    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail:{self.email}"
                f"\nEndereco:{self.endereco}")