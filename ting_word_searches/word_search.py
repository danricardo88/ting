def exists_word(word, instance):
    """Aqui irá sua implementação"""
    resultado = list()
    data = instance._data
    for item in data:
        ocorrencias = list()
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1})
        if len(ocorrencias) > 0:
            resultado.append({
              "palavra": word,
              "arquivo": item["nome_do_arquivo"],
              "ocorrencias": ocorrencias
            })
    return resultado


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    resultado = list()
    data = instance._data
    for item in data:
        ocorrencias = list()
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1, "conteudo": line})
        if len(ocorrencias) > 0:
            resultado.append({
              "palavra": word,
              "arquivo": item["nome_do_arquivo"],
              "ocorrencias": ocorrencias
            })

    return resultado
