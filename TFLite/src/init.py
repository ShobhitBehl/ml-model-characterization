import os

#function to compile schema.fbs with flatc and generate code files
def init_tflite_files():

    # Absolute path to schema.fbs and the path to store the generated code
    schema_path = '/home/shobhitbehl/ml-model-characterization/TFLite/schema.fbs'
    out_path = '/home/shobhitbehl/ml-model-characterization/TFLite/src/'

    print("Creating tflite files")

    # Compiling schema.fbs into python code
    os.system('flatc --python -o ' + out_path + ' ' + schema_path)

    #Echoing code to __init__.py for corect funtioning of 'from tflite import *'
    os.system(
        'echo "from os import path\n'
        'import glob\n\n'
        'modules = glob.glob(path.join(path.dirname(__file__), \'*.py\'))\n'
        'str_modules = str()\n'
        'for module in modules:\n'
        '   if path.isfile(module) and not module.endswith(\'__init__.py\'):\n'
        '       str_modules += path.basename(module)[:-3] + \' \'\n\n'
        'str_modules = str_modules[:-1]\n'
        '__all__ = str_modules.split(\' \')\n" '
        '> ' + out_path + 'tflite/__init__.py'
    )

if __name__ == "__main__":
    init_tflite_files()