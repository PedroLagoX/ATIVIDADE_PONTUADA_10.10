class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"Número: {self.numero}"
            f"Complemento: {self.complemento}"
            f"CEP: {self.cep}"
            f"Cidade: {self.cidade}"
        )