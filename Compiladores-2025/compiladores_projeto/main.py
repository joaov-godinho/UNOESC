# main.py

import ascii_text_processor
import advanced_features

def main():
    print("Escolha o programa para executar:")
    print("1. Processador de Texto ASCII")
    print("2. Funções Avançadas")
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        print("\nVocê escolheu o Processador de Texto ASCII.\n")
        ascii_text_processor.main()
    elif escolha == "2":
        print("\nVocê escolheu Funções Avançadas.\n")
        advanced_features.main()
    else:
        print("\nEscolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
