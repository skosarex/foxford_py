V = set('АБВГДЕЖЗ')
E = {'АБ', 'АВ', 'АГ',
     'БВ', 'БД',
     'ВД', 'ВЕ', 'ВЗ', 'ВЖ',
     'ГВ', 'ГЖ',
     'ДЕ',
     'ЕЗ',
     'ЖЗ'}


def K(vertex):
    if vertex == 'А':
        return 1

    previous_neighbours = [edge[0] for edge in E if edge[1] == vertex]
    sum_tracks = 0
    for neighbour in previous_neighbours:
        sum_tracks += K(neighbour)
    return sum_tracks


print(K('В'))
