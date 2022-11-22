# supr smll prgrm
E = set('АБ АВ АГ БВ БД ВД ВЕ ВЗ ВЖ ГВ ГЖ ДЕ ЕЗ ЖЗ'.split())
def K(vertex):
    return 1 if vertex == 'А' else sum(K(neighbour) for neighbour in [edge[0] for edge in E if edge[1] == vertex])
print(K('З'))
