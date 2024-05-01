# Conteúdo do script principal (main.py)

import retangulos_enem
import analise_regiao1
import analise_regiao2
import analise_regiao3
import analise_regiao4
import analise_regiao5
import analise_regiao6
# Importe outros módulos conforme necessárioq

def main():
    retangulos_enem.executar_retangulos_enem()
    analise_regiao1.executar_analise_regiao1()
    analise_regiao2.executar_analise_regiao2()
    analise_regiao3.executar_analise_regiao3()
    analise_regiao4.executar_analise_regiao4()
    analise_regiao5.executar_analise_regiao5()
    analise_regiao6.executar_analise_regiao6()
    # Chame outras funções conforme necessário

if __name__ == "__main__":
    main()
