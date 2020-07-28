"""Module to load multiple files into the database.

Module loads multiple models into database from MODELS_DIR of tf and tflite.
The file naming format should be of the form modelname_subcategory.tflite or
modelname_subcategory_(SavedModel/FrozenGraph).pb.
Can only load one type of "model_type" models at a time.

Attributes:
    IMAGE_SUB_CATEGORIES (list of str) : Sub categories that belong to the 
        Image category.
    AUDIO_SUB_CATEGORIES (list of str) : Sub categories that belong to the
        Audio category.
    MODEL_TYPE (list of str) : String to denote type of model architecture, if a 
        model is the first of its architecture, then value is set to 
        "canonical", if it is a module then set to "module", else "additional".
    TFLITE_MODELS_DIR (str) : Directory where tflite models are present,
        should corrrespond to the MODELS_DIR in TFLite/src/main.py.
    TF_MODELS_DIR (str) : Directory where tf models are present,
        should corrrespond to the MODELS_DIR in TF/src/main.py.
"""

import os

IMAGE_SUB_CATEGORIES = [
    "FaceDetection", "EmotionRecognition", "PalmDetection"
    ]
AUDIO_SUB_CATEGORIES = ["AutomaticSpeechRecognition"]
MODEL_TYPE = "additional"
TFLITE_MODELS_DIR = "./TFLite/models"
TF_MODELS_DIR = "./TF/models"

# bazel build for tflite files
os.system('bazel build tflite_init')
os.system('bazel-bin/tflite_init')
os.system('bazel build tflite_main')

for file_name in os.listdir(TFLITE_MODELS_DIR):
    # Extracting command options from filename
    file_name = file_name[:-7]
    file_info = file_name.rsplit("_", 1)

    sub_category = file_info[1]
    model_name = file_info[0]

    # Extracting category from sub_category
    if sub_category.startswith("Image") or sub_category in IMAGE_SUB_CATEGORIES:
        category = "Image"
    elif sub_category.startswith("Text"):
        category = "Text"
    elif sub_category.startswith("Video"):
        category = "Video"
    elif sub_category.startswith("Audio") or sub_category in AUDIO_SUB_CATEGORIES:
        category = "Audio"
    else:
        category = "None"

    os.system(
        'bazel-bin/tflite_main --filename ' + file_name + '.tflite'
        ' --model_name ' + model_name + ' --category ' + category +
        ' --sub_category ' + sub_category + ' --model_type ' + MODEL_TYPE
        )

# bazel build for tf files
os.system('bazel build tf_main')

for file_name in os.listdir(TF_MODELS_DIR):
    # Extracting command options from filename
    file_name = file_name[:-3]
    file_info = file_name.rsplit("_", 2)

    is_saved_model = "True"
    if file_info[2] != "SavedModel":
        is_saved_model = "False"

    sub_category = file_info[1]
    model_name = file_info[0]

    # Extracting category from sub_category
    if sub_category.startswith("Image") or sub_category in IMAGE_SUB_CATEGORIES:
        category = "Image"
    elif sub_category.startswith("Text"):
        category = "Text"
    elif sub_category.startswith("Video"):
        category = "Video"
    elif sub_category.startswith("Audio") or sub_category in AUDIO_SUB_CATEGORIES:
        category = "Audio"
    else:
        category = "None"

    os.system(
        'bazel-bin/tf_main --filename ' + file_name + '.pb'
        ' --model_name ' + model_name + ' --category ' + category +
        ' --sub_category ' + sub_category + ' --model_type ' + MODEL_TYPE +
        ' --is_saved_model ' + is_saved_model
        )
