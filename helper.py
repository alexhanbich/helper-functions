def is_str(data):
    if isinstance(data, str):
        return True
    else:
        return False

def is_bytes(data):
    if isinstance(data, bytes):
        return True
    else:
        return False

def is_int_list(data):
    if isinstance(data, list) and all(isinstance(x, int) for x in data):
        return True
    else:
        return False
        
def is_hex_list(data):
    def is_hex(data):
        try:
            int(data, 16)
            return True
        except ValueError:
            return False
    if isinstance(data, list) and all(isinstance(x, str) and is_hex(x) for x in data):
        return True
    else:
        return False

def to_str(data):
    if is_bytes(data):
        return data.decode('utf-8')
    elif is_int_list(data):
        return bytes(data).decode('utf-8')
    elif is_hex_list(data):
        return bytes([int(x, 16) for x in data]).decode('utf-8')
    elif is_str(data):
        return data
    else:
        raise Exception('cannot convert to string')

def to_bytes(data):
    if is_str(data):
        return data.encode('utf-8')
    elif is_int_list(data):
        return bytes(data)
    elif is_hex_list(data):
        return bytes([int(x, 16) for x in data])
    elif is_bytes(data):
        return data
    else:
        raise Exception('cannot convert to bytes')

def to_int_list(data):
    if is_bytes(data):
        return list(data)
    elif is_str(data):
        return list(data.encode('utf-8'))
    elif is_hex_list(data):
        return [int(x, 16) for x in data]
    elif is_int_list(data):
        return data
    else:
        raise Exception('cannot convert to int list')

def to_hex_list(data):
    if is_int_list(data):
        res = data
    elif is_bytes(data):
        res = list(data)
    elif is_str(data):
        res = list(data.encode('utf-8'))
    elif is_hex_list(data):
        return data
    else:
        raise Exception('cannot convert to int list')
    for i, val in enumerate(res):
        res[i] = hex(val)
    return res