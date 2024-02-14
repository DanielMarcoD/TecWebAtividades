import json
from pathlib import Path
def extract_route(palavra):
    return palavra.split()[1][1:]


def read_file(path):
    with open(path,"rb") as file:
        cont = file.read()
    return cont


def load_data(filename):
   
    with open("data/" + filename, 'r') as file:
        data = json.load(file)
    return data


def load_template(filename):
    
    with open("templates/" + filename, 'r') as file:
        template_content = file.read()
    return template_content

def adicionar_item_arquivo(novo_item):
    # Abre o arquivo JSON para leitura
    with open('./data/notes.json', 'r') as file:
        data = json.load(file)  # Carrega o conteúdo do arquivo em uma estrutura de dados Python

    # Adiciona o novo item à lista
    data.append(novo_item)

    # Escreve a estrutura de dados atualizada de volta ao arquivo JSON
    with open('./data/notes.json', 'w') as file:
        json.dump(data, file, indent=4)  # Salva os dados de volta no arquivo JSON com formatação
def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'
    return response.encode()        


                