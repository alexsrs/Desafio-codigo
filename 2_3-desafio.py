class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def verificar_saldo(self):
        return self.saldo

    def mensagem_personalizada(self):
        if self.saldo < 10:
            return f"Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.saldo >= 50:
            return f"Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return f"Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo_e_mensagem_personalizada(self):
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem

nome_usuario = input("Digite o nome do usuário: ")
nome_plano = input("Digite o nome do plano: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo_e_mensagem_personalizada()
print(mensagem_usuario)
