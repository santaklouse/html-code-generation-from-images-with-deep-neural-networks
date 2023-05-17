from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Taneem Jan, taneemishere.github.io'

import os.path
from os.path import basename

from classes.Sampler import *
from classes.model.Main_Model import *


def dsl_code_generation(input_image):
    trained_weights_path = "classes/model/bin"
    trained_model_name = "Main_Model"
    input_path = input_image
    output_path = "data/output/"
    search_method = "greedy"
    meta_dataset = np.load("{}/meta_dataset.npy".format(trained_weights_path), allow_pickle=True)
    input_shape = meta_dataset[0]
    output_size = meta_dataset[1]

    model = Main_Model(input_shape, output_size, trained_weights_path)
    model.load(trained_model_name)

    sampler = Sampler(trained_weights_path, input_shape, output_size, CONTEXT_LENGTH)

    file_name = 'input_image_from_interface.png'
    file_name = basename(file_name)[:basename(file_name).find(".")]
    evaluation_img = Utils.get_preprocessed_img(input_path, IMAGE_SIZE)

    if search_method == "greedy":
        result, _ = sampler.predict_greedy(model, np.array([evaluation_img]))
        print("Result greedy: \n {}".format(result))

    with open("{}/{}.gui".format(output_path, file_name), 'w') as out_f:
        out_f.write(result.replace(START_TOKEN, "").replace(END_TOKEN, ""))

    return file_name, output_path


def compile_gui(file_path, filename):
    from os.path import basename
    from compiler.Utils import Utils
    from compiler.Compiler import Compiler

    input_path = (file_path + filename)

    # remove the path
    file_ = os.path.basename(input_path)
    # remove the extension
    file_ = os.path.splitext(file_)[0]
    # add the extension of gui
    file_ = "data/output/" + file_ + ".gui"

    input_file = file_

    FILL_WITH_RANDOM_TEXT = True
    TEXT_PLACE_HOLDER = "[]"

    dsl_path = "compiler/assets/web-dsl-mapping.json"
    compiler = Compiler(dsl_path)

    def render_content_with_text(key, value):
        if FILL_WITH_RANDOM_TEXT:
            if key.find("btn") != -1:
                value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text())
            elif key.find("title") != -1:
                value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text(length_text=5, space_number=0))
            elif key.find("text") != -1:
                value = value.replace(TEXT_PLACE_HOLDER,
                                      Utils.get_random_text(length_text=56, space_number=7, with_upper_case=False))
        return value

    file_uid = basename(input_file)[:basename(input_file).find(".")]
    path = input_file[:input_file.find(file_uid)]

    input_file_path = "{}{}.gui".format(path, file_uid)
    output_file_path = "{}{}.html".format(path, file_uid)

    html_code = compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)
    print("Generated code is compiled..!!")
    return html_code


def main_method(input_image_from_interface):
    file_name, file_output_path = dsl_code_generation(input_image_from_interface)
    result = compile_gui(file_output_path, file_name)
    return result
