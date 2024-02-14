from utils import load_data, load_template, adicionar_item_arquivo, build_response
import urllib.parse

def index(request):


    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        i = 0
        q = 0
        string_codificada_titulo = ""
        string_codificada_detalhes = ""
        print(corpo.split('&'))
        
        for chave_valor in corpo.split('&'):
            for p in chave_valor:
                if p=="=":
                   i=1
                elif i==1 and q==0:
                    string_codificada_titulo = string_codificada_titulo + p
                elif i==1 and q==1:
                    string_codificada_detalhes = string_codificada_detalhes + p
            i= 0             
            q = 1            

           
        params['titulo'] = urllib.parse.unquote_plus(string_codificada_titulo)
        params['detalhes'] = urllib.parse.unquote_plus(string_codificada_detalhes)
        adicionar_item_arquivo(params)
        return build_response(code=303, reason='See Other', headers='Location: /')                  
                    
            # AQUI É COM VOCÊ
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
          
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))