import os
from google.genai import types
# from config import MAX_CHARS 


MAX_CHARS = 10000

def get_file_content(working_dir:str, file_path:str) -> str:
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    file_content_string = ''
    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[.... File "{file_path}" truncates at {MAX_CHARS} characters]'
        
        return file_content_string
    except Exception as e:
        return f'Exception reading file: {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description='Get the contents of the given filse as a string. Constrained to the working directory',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='The path to the file, from the working directory'
            ),
        },
    ),
)