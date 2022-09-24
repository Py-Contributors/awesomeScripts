import hashlib
import os 

def checksum_file(file_address : str) -> str:
    hasher = hashlib.md5()
    with open(file_address,'rb') as open_file:
        content = open_file.read()
        hasher.update(content)
        print(len(hasher.hexdigest()))
        return hasher.hexdigest()


print(checksum_file(os.environ.get('FILE_ADDRESS')))

