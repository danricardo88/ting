import sys
from ting_file_management.file_management import txt_importer


def process(pathfile, instance):
    """Aqui irá sua implementação"""
    for i in instance._data:
        if pathfile in i["nome_do_arquivo"]:
            return None

    textinho = txt_importer(pathfile)
    resultadoado = {
      "nome_do_arquivo": pathfile,
      "qtd_linhas": len(textinho),
      "linhas_do_arquivo": textinho
    }

    instance.enqueue(resultadoado)
    print(resultadoado)


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        resultado = instance.dequeue()
        nomedoarquivo = resultado["nome_do_arquivo"]
        print(f"Arquivo {nomedoarquivo} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        resultado = instance.search(position)
        print(resultado)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
