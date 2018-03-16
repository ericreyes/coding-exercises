def timeConversion(time_string):
    if time_string[8] == 'A' and time_string[0] == '1' and time_string[1] == '2':
        lista = list(time_string)
        lista[0] = '0'
        lista[1] = '0'
        return ''.join(lista)[:-2]
    elif time_string[8] == 'A' or (time_string[0] == '1' and time_string[1] == '2'):
        return time_string[:-2]

    cleansed = time_string[:-2]
    lista = cleansed.split(':')
    lista[0] = str(int(lista[0]) + 12)
    return ':'.join(lista)

print(timeConversion('12:05:39AM'))
