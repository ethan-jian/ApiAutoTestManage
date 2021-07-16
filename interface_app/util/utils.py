import os

def encode_object(obj):
    """ json.dumps转化时，先把属于bytes类型的解码，若解码失败返回str类型，和其他对象属性统一转化成str"""
    if isinstance(obj, bytes):
        try:
            return bytes.decode(obj)
        except Exception as e:
            return str(obj)
    else:
        return str(obj)


def get_files():
    FILE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/files/"
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)

    return FILE_PATH



if __name__ == '__main__':
    pass
    print(get_files())
