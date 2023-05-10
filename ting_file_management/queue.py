from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(proprio):
        """Inicialize sua estrutura aqui"""
        proprio._data = []

    def __len__(proprio):
        """Aqui irá sua implementação"""
        return len(proprio._data)

    def enqueue(proprio, valor):
        """Aqui irá sua implementação"""
        proprio._data.append(valor)

    def dequeue(proprio):
        """Aqui irá sua implementação"""
        if not proprio._data:
            raise IndexError("A fila está vazia")
        return proprio._data.pop(0)

    def search(proprio, index):
        """Aqui irá sua implementação"""
        datalength = proprio.__len__()
        if index < 0 or index > datalength - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return proprio._data[index]
