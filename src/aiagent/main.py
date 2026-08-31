import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from .functions.get_file_info import schema_get_file_info
from .functions.get_file_content import schema_get_file_content
from .functions.write_file import schema_write_file
from .functions.run_python_file import schema_run_python_file
from .call_functions import call_function

def main():

    
    if len(sys.argv) < 2:
        print("Prompt needed")
        sys.exit(1)

    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose_flag = True
    
    prompt = sys.argv[1]

    messages = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)]
        )
    ]
    
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

    client = genai.Client(api_key=api_key)

    system_prompt = '''
        You are a helpful AI coding agent
        When a user asks a question or makes a request, make a function call plan. You can perform the following operations
        
        - List file and directories
        - Read the content of a file
        - Write to a file (create or update)
        - Run a python file with optional arguments

        When the user asks about the code project - they are referring to the working directory.
        So always look at the project files (calculator) and figure out how to run the project and always test the tests before and after fix.
        Every user prompt would always related to the calculator project and files in them.
        For every fix also test the problem to see it exists before fixing and tests also after fixing.
        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function call as it is automaticall
        injected for security reasons.
    '''

    avaiable_function = types.Tool(
        function_declarations=[
            schema_get_file_info,
            schema_run_python_file,
            schema_write_file,
            schema_get_file_content
        ]
    )

    config=types.GenerateContentConfig(
        tools=[avaiable_function],
        system_instruction=system_prompt
    )

    max_iters = 20
    for i in range(0, max_iters):


        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=messages,
            config=config
        )

        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return

        if verbose_flag:
            print(f'{prompt}')
            print(f'Prompt Token: {response.usage_metadata.prompt_token_count}')
            print(f'Response Token: {response.usage_metadata.candidates_token_count}')


        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                results = call_function(function_call_part, verbose_flag)
                messages.append(results)
        else:
            print(response.text)
            return

    

    # interaction = client.interactions.create(
    #     model="gemini-3.6-flash",
    #     input=messages
    # )
    # print("Response", interaction.output_text)
    # print(interaction.usage.total_input_tokens)
    # print(interaction.usage.total_output_tokens)

if __name__ == "__main__":
    main()