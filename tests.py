from src.aiagent.functions.get_file_info import get_file_info
from src.aiagent.functions.get_file_content import get_file_content
from src.aiagent.functions.write_file import write_file
from src.aiagent.functions.run_python_file import run_python_file

def test_get_file_info():
    working_dir = 'calculator'
    contents = get_file_info(working_dir)
    print(contents)
    contents = get_file_info(working_dir, 'pkg')
    print(contents)
    contents = get_file_info(working_dir, '/bin')
    print(contents)
    contents = get_file_info(working_dir, '../')
    print(contents)

def test_get_file_content():
    working_dir = 'calculator'
    print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "/Desktop/text.txt"))
    print(get_file_content(working_dir, "pkg/cal.py"))

def test_write_file():
    working_dir = 'calculator'
    print(write_file(working_dir, 'lorem.txt', 'almost done'))
    print(write_file(working_dir, 'pkg/lorem.txt', 'almost done'))
    print(write_file(working_dir, 'pkg2/lorem.txt', 'almost done'))
    print(write_file(working_dir, '/Desktop/lorem.txt', 'almost done'))


def test_run_python_file():
    working_dir = 'calculator'
    print(run_python_file(working_dir, 'main.py', ["3 + 5"]))
    print(run_python_file(working_dir, 'tests.py'))
    print(run_python_file(working_dir, '../main.py'))
    print(run_python_file(working_dir, 'nonexistent.py'))


test_run_python_file()