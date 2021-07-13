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



file_path = os.path.abspath('../../..') + r'/files/'
if not os.path.exists(file_path):
    os.makedirs(file_path)

if __name__ == '__main__':
    pass
