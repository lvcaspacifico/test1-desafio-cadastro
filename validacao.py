#validacao contém apenas as funções de validação e a função obter_input_valido. Não deve ser executado diretamente para interagir com o usuário; em vez disso, ele deve ser importado e usado por main.py

import re
from datetime import datetime

def validar_cpf(cpf: str) -> bool:
    cpf_limpo = re.sub(r'\D', '', cpf)
    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
        return False
    if cpf_limpo == cpf_limpo[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf_limpo[num]) * ((i + 1) - num) for num in range(0, i))
        digito_verificador = ((soma * 10) % 11) % 10
        if digito_verificador != int(cpf_limpo[i]):
            return False
    return True

def validar_cnpj(cnpj: str) -> bool:
    cnpj_limpo = re.sub(r'\D', '', cnpj)
    return len(cnpj_limpo) == 14 and cnpj_limpo.isdigit()

def validar_data(data_str: str) -> bool:
    if len(data_str) != 8 or not data_str.isdigit():
        return False
    try:
        datetime.strptime(data_str, '%d%m%Y')
        return True
    except ValueError:
        return False

def validar_telefone(telefone: str) -> bool:
    telefone_limpo = re.sub(r'\D', '', telefone)
    return len(telefone_limpo) in [10, 11] and telefone_limpo.isdigit()

def validar_campo_obrigatorio(campo: str) -> bool:
    return bool(campo.strip())

def obter_input_valido(mensagem: str, validacao) -> str:
    while True:
        valor = input(mensagem)
        if validacao(valor):
            return valor
        else:
            print("Entrada inválida. Por favor, tente novamente.")
