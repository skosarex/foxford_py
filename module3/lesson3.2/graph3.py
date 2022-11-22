E = "АБ АГ АД БГ ДГ ГЖ ДЖ ЕЖ ГЕ ГВ ВЕ ВЗ ВК ЕИ ЖИ ИМ ЕК ЕМ ЗК ЗЛ КЛ КН КМ МН ЛН"
E = E.split()


def K(start, v):
    if v == start:
        return 1
    else:
        return sum(K(start, n) for n in [a for a, b in E if b == v])


print(K("А", "В") * K("В", "Н"))
print(K("А", "К") * K("К", "Н"))
print(K("А", "В") * K("В", "К") * K("К", "Н") + K("А", "К") * K("К", "В") * K("В", "Н"))
