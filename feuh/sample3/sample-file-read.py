from pathlib import Path

from feuh.sample3.files.services.file_service import FileService

file_name = Path('C:\\Users\\Alfredo\\Downloads\\python_file.txt')
service = FileService()

result = service.read(str(file_name))
print(result)