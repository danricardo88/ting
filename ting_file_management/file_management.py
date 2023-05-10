import sys


def txt_importer(pathfile):
    """Aqui irá sua implementação"""
    if not pathfile.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(pathfile) as file:
            textinho = file.read()
            return textinho.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {pathfile} não encontrado", file=sys.stderr)
