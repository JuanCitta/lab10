""	{} -> caso que não testa nada do conteúdo, apenas devolve o dicionário
"teste"	{"teste": 1} -> testa o conteúdo apenas com texto
"bom dia"	dois itens
"dia a dia"	{"dia": 2, "a": 1}
"bom dia" (três espaços)	dois itens
"bom\ndia"	dois itens
"Dia dia DIA"	{"dia": 3}
"fim. Fim!"	{"fim": 2}
",dia, ;dia;"	{"dia": 2}
1":dia: ?dia?"	{"dia": 2}
1"guarda-chuva"	um item
1"... !"	{}