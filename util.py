def getBackground(type_name):
    if (type_name == 'Intervention'):
        return 'blue'
    if (type_name == 'Impediment'):
        return 'orange'
    raise("unkown type of row")
