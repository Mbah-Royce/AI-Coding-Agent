import os
from google.genai import types

def get_file_info(working_dir:str, dir:str='.') -> str:
    
    abs_working_dir = os.path.abspath(working_dir)
    abs_dir = ''
    if dir == '.':
        abs_dir = abs_working_dir
    else:
        abs_dir = os.path.abspath(os.path.join(working_dir, dir))

    if not abs_dir.startswith(abs_working_dir):
        return f'Error: "{dir}" is not a directory'
    
    res = ''
    contents = os.listdir(abs_dir)
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        res += f"- {content}: file_size {size} bytes, is_dir={is_dir}\n"
    
    return res

schema_get_file_info = types.FunctionDeclaration(
    name="get_file_info",
    description='List files in the specified directory along with their sizes constrained to the working directory',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir": types.Schema(
                type=types.Type.STRING,
                description='The directory to list files from relative to the working directory. If not provided, list files in the working directory itself, use "." for the current working directory'
            ),
        },
    ),
)
