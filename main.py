class Estacionamento:

    def __init__(self):

        self.pilha = []
        self.fim = -1

    def retirarVeiculo(self, placa):

        while True:
            ultimo_carro = self.pilha[self.fim] # Atualizando o ultimo carro

            if ultimo_carro == placa: # Se achar o carro
                print(f'Achamos o seu carro de placa: {ultimo_carro}')
                break

            print(f'Retirando o carro de placa: {ultimo_carro}')
            self.pilha.remove(self.pilha[self.fim]) # Removendo o ultimo carro.

            if not self.pilha: # Se o estacionamento estiver vazio
                print('Não encontramos seu carro aqui.')
                break

    def armazenarVeiculo(self, placa):
        self.pilha.append(placa) # Estacionando o veiculo.
        print('Veiculo estacionado!')


estacionamento = Estacionamento()
estacionamento.armazenarVeiculo(5445)
estacionamento.armazenarVeiculo(6662)
estacionamento.armazenarVeiculo(4850)
estacionamento.armazenarVeiculo(4584)
estacionamento.armazenarVeiculo(5588)
estacionamento.armazenarVeiculo(9898)
estacionamento.retirarVeiculo(4850)