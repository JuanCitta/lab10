from contador import contar_palavras


def test_texto_vazio_devolve_dicionario_vazio():
    assert contar_palavras("") == {}

def test_uma_palavra_conta_uma_ocorrencia():
    assert contar_palavras("teste") == {"teste": 1}

def test_bom_dia_da_dois_itens():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}

def test_dia_a_dia_soma_ocorrencias_de_dia():
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}

def test_tres_espacos_entre_bom_e_dia_dao_dois_itens():
    assert contar_palavras("bom   dia") == {"bom": 1, "dia": 1}

def test_quebra_de_linha_separa_palavras():
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}

def test_maiusculas_contam_como_minusculas():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}

def test_ponto_e_exclamacao_nas_bordas_sao_ignorados():
    assert contar_palavras("fim. Fim!") == {"fim": 2}

def test_virgula_e_ponto_e_virgula_nas_bordas_sao_ignorados():
    assert contar_palavras(",dia, ;dia;") == {"dia": 2}

def test_dois_pontos_e_interrogacao_nas_bordas_sao_ignorados():
    assert contar_palavras(":dia: ?dia?") == {"dia": 2}

def test_hifen_interno_faz_parte_da_palavra():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}

def test_texto_so_de_pontuacao_devolve_dicionario_vazio():
    assert contar_palavras("... !") == {}