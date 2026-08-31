from .functions.get_file_content import get_file_content
from .functions.get_file_info import get_file_info
from .functions.run_python_file import run_python_file
from .functions.write_file import write_file
from google.genai import types
working_dir =  'calculator'

def call_function(function_call_part, verbose:bool=False):
    if verbose:
        print(f'calling function: {function_call_part.name}({function_call_part.args})')
    else:
        print(f'calling function: {function_call_part.name}')

    result = ''
    if function_call_part.name == 'get_file_info':
        result = get_file_info(working_dir, **function_call_part.args)
    if function_call_part.name == 'get_file_content':
        result = get_file_content(working_dir, **function_call_part.args)
    if function_call_part.name == 'run_python_file':
        result = run_python_file(working_dir, **function_call_part.args)
    if function_call_part.name == 'write_file':
        result = write_file(working_dir, **function_call_part.args)

    if result == '':
        response={
            "error": f'Unknown function: {function_call_part.name}'
        }
    else:
        response = {"results": result}

    return types.Content(
        role='user',
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response=response
            )
        ]
    )