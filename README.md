# Web Crawler and Text Analysis

> Finalidade para pesquisa de algoritmos de análise textual. 

O projeto tem o propósito de dar apoio técnico e prático para uma pesquisa de aplicação de algoritmos de análise textual com foco em identificação de 
paǵinas web duplicadas, fornecendo um ambiente de fácil interação e entendimento.

O projeto possui um Web Crawler para a captura de HTML's, e um diretório com os algoritmos de análise textual, juntamente com rotinas de pré-processamento de texto.

## Conteúdo

- [Quick Start](#quick-start)
- [Web Crawler](#web-crawler)
- [Pré Processamento de Texto](#pre-process)
- [Algoritmos de Análise Textual](#text-analysis)
- [Contribuição](#contributing)
- [Contribuidores](#contributors)

## <a name="quick-start"></a>Quick Start

### Pré-requisitos

 - Instalar [Python 3](https://www.python.org/downloads/) e [pip](https://pip.pypa.io/en/stable/installing/) (gerenciador de pacotes do Python).
    - Verifique se estão instalados corretamente no sistema usando os seguintes comandos de terminal:
    
        ```bash
        $ python --version
        Python 3.7.1
        $ pip --version 
        pip 18.1 
        ```
 - Baixar o [geckodriver](https://github.com/mozilla/geckodriver/releases) (Driver do Firefox/Chrome para o Selenium).

### Instalando as bibliotecas

1. Faça download do código fonte ou clone o repositório;
2. Acesse a pasta do projeto;
3. Rode o comando `pip install -r requirements.txt` para instalar todas as dependências do projeto; 

### Configurando geckoriver
1. Com o [geckodriver](https://github.com/mozilla/geckodriver/releases) já baixado, coloque o arquivo em um diretório de sua escolha;
2. Salve o path do local do arquivo;
2. Acesse o diretório `crawler/` , edite o arquivo [settings.py](crawler/settings.py) e acrescente o path do arquivo do geckodriver, conforme exemplo abaixo:
```bash
####################### SELENIUM #######################
GECKODRIVER = "/var/driver/geckodriver"
```

## <a name="web-crawler"></a>Web Crawler

### Executando Web Crawler

1. Acesse o diretório `crawler/` e edite o arquivo [settings.py](crawler/settings.py) para acrescentar os links da web que deseja capturar o HTML;
```bash
####################### CRAWLING #######################
SITES = {'pronounced-dead-michigan': 'https://www.mlive.com/news/2020/08/pronounced-dead-michigan-woman-found-alive-at-funeral-home.html',
         'police-identify-northern': 'https://www.mlive.com/news/saginaw-bay-city/2020/08/police-identify-northern-michigan-woman-whose-burned-body-was-found-in-bay-county.html',
         'pirates-claim-former': 'https://www.mlive.com/tigers/2020/08/pirates-claim-former-tigers-pitcher-off-waivers.html',
         'tigers-cubs-lineup':  'https://www.mlive.com/tigers/2020/08/tigers-cubs-lineup-schoop-returns-candelario-remains-in-the-clean-up-spot.html'}
```
> **Note**: Os links desejados para captura são dispostos em um estrutura de dicionário (chave-valor), onde a chave é o nome do arquivo em que o HTML vai ser salvo, e o valor é o link para a captura.

Ao fim, dentro do diretório `crawler/`, execute o arquivo [main.py](crawler/main.py) com o seguinte comando:
```bash
$ python main.py
```

O processo de crawling será iniciado e os HTML's serão salvos no diretório `crawler/htmls/` que, por sua vez, é criado automaticamente.

## <a name="pre-process"></a>Pré Processamento de Texto

1. Acesse o diretório `text_analysis/preprocessing`;

- Em desenvolvimento.

## <a name="text-analysis"></a>Algoritmos de análise textual

- Em desenvolvimento.

## <a name="contributing"></a>Contribuição

Sua ajuda é muito bem vinda!

> Dar uma estrela no GitHub é também uma maravilhosa maneira de mostrar seu apoio :star:

## <a name="contributors"></a>Contribuidores

 - **Fillipe Vieira** - fillipe.vieira2@gmail.com