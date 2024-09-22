#pip install pytest

import pytest
from validacao import (
    validar_cpf, validar_cnpj, validar_data, validar_telefone, validar_campo_obrigatorio
)

def test_validar_cpf():
    assert validar_cpf("123.456.789-09") == True # <======================== Válido apesar de não pertencer a nenhum brasileiro
    assert validar_cpf("111.444.777-35") == True # Válido apesar de não pertencer a nenhum brasileiro
    assert validar_cpf("111.222.333-77") == False # Inválido, todos os números repetidos
    assert validar_cpf("111.111.111-11") == False # Inválido, todos os números repetidos
    assert validar_cpf("555.444.333-22") == False # Inválido, números repetidos alternados

def test_validar_cnpj():
    assert validar_cnpj("12.345.678/0001-95") == True
    assert validar_cnpj("12.345.678/0001-9") == False

def test_validar_data():
    assert validar_data("14021998") == True
    assert validar_data("31021998") == False

def test_validar_telefone():
    assert validar_telefone("11987654321") == True
    assert validar_telefone("987654321") == False

def test_validar_campo_obrigatorio():
    assert validar_campo_obrigatorio("Nome") == True
    assert validar_campo_obrigatorio("") == False
