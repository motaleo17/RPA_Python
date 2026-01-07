- Necessário ambos os python 64 e 32bits
- Adicionar as bibliotecas para ambas as versoes
- Chamada py -3.9-64 / py -3.9-32
- Criar as .bat para inserir no path
- linha de comando -> py .\scriptWeb.py 07-01-2026 "https://www.bcb.gov.br/"


- STATUS DE ERROS PADROES 

Status,Categoria,Descrição da Falha
11,Ambiente,Falha ao lançar o navegador (Chrome/Edge).
12,A 
21,Navegação,Erro ao carregar a URL (Página fora do ar ou Timeout).
22,Navegação,URL validada está incorreta (Não é o site esperado).
31,Identificação,"Elemento não encontrado (Lupa, Botão, Menu)."
32,Identificação,Múltiplos elementos encontrados (Ambiguidade de seletor).
41,Ação,Falha ao clicar no elemento (Elemento interceptado ou invisível).
42,Ação,Falha ao digitar/preencher campo (Input desabilitado).
51,Dados,Falha ao extrair texto (Cotação não encontrada ou vazia).
52,Dados,Erro de conversão de dados (Ex: Ponto por vírgula no Dólar).
61,Fluxo,Falha ao trocar de aba ou fechar Pop-up.
62,Fluxo,Download não iniciado ou falha ao salvar arquivo.
99,Crítico,Erro desconhecido (Exceção genérica de sistema).
