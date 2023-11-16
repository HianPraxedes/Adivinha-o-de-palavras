import json
import random
from collections import Counter

class AgenteAdivinhacaoPalavras:
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra = random.choice(palavras)
        self.palavra_oculta = ['_' for _ in self.palavra]
        self.palavras_tentadas = set()

    def adivinhar_palavra(self):
        # Filtrar palavras que têm o mesmo comprimento que a palavra oculta
        palavras_possiveis = [palavra for palavra in self.palavras if len(palavra) == len(self.palavra) and palavra not in self.palavras_tentadas]

        # Contar a frequência das letras nas palavras possíveis
        frequencia_letras = Counter(''.join(palavras_possiveis))

        # Ordenar as letras pela frequência
        letras_ordenadas = sorted(frequencia_letras, key=frequencia_letras.get, reverse=True)

        # Tentar adivinhar com base na frequência das letras
        for letra in letras_ordenadas:
            for palavra in palavras_possiveis:
                if all(palavra[i] == self.palavra_oculta[i] or self.palavra_oculta[i] == '_' for i in range(len(palavra))):
                    return palavra

        # Se não houver correspondência, tentar adivinhar uma palavra aleatória
        if palavras_possiveis:
            return random.choice(palavras_possiveis)

    def jogar(self):
        print("Bem-vindo ao jogo de adivinhação de palavras!")
        tentativas = 0

        while True:
            print(' '.join(self.palavra_oculta))
            palpite = self.adivinhar_palavra()
            self.palavras_tentadas.add(palpite)
            tentativas += 1

            print(f"Palpite do agente: {palpite}")  # Mostrar o palpite do agente

            acertos = [i for i, letra in enumerate(self.palavra) if letra == palpite[i]]
            for i in acertos:
                self.palavra_oculta[i] = self.palavra[i]

            if palpite == self.palavra:
                print(f"Parabéns! O agente adivinhou a palavra '{self.palavra}' em {tentativas} tentativas.")
                break

# Carregar a lista de palavras do arquivo JSON
with open('Adivinha-o-de-palavras\palavras.json', 'r') as f:
    data = json.load(f)
    palavras = data['palavras']

# Agora você pode usar a lista de palavras no seu jogo
agente = AgenteAdivinhacaoPalavras(palavras)
agente.jogar()
