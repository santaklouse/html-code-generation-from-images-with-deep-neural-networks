__author__ = 'Taneem Jan, taneemishere.github.io'

import gradio as gr
import main_program


# our model's i/o method that take image from gradio interface's inputs.Image()
def model_interface(image):
    return main_model(image)


# main method that call the main_program where code is generated and then compiled
def main_model(input_image):
    result = main_program.main_method(input_image)
    return result


interface_title = "<br> <p style='margin: 0% 8% 0% 8%'>HTML Code Generation from Images with Deep Neural Networks</p>"
interface_description = """<p style='margin: 0% 8% 2% 8%; text-align: justify;text-justify: inter-word;'> Writing 
code in a programming language for a designed mockup or a graphical user interface created by designers and UI 
engineers, is done mostly by developers to build and develop custom websites and software. The development work is 
not approachable by those unfamiliar with programming, to drive these personas capable of designing and developing 
the code bases and website structures we come up with an automated system. In this work, we showed and proposed that 
methods of deep learning and computer vision can be grasped to train a model that will automatically generate HTML 
code from a single input mockup image and try to build an end-to-end automated system with accuracy more than 
previous works for developing the structures of web pages.</p> """

interface_article = """<br><h2 style='text-align: center;'>Limitations of Model</h2> <p style='text-align: 
center;'>Certain limitations are there in the model some of them are listed below</p> <ul><li>Sometimes the model do 
produce all the buttons with the same green color instead of other colors</li><li>As the model has fed with the data 
provided, and so while producing the code on some other types of images might not generate the code we 
wanted</li><li>The model is only trained upon the learning and recognition of boxes and buttons etc. in the images 
and it do not write the text written exactly on the images</li></ul> 
<div style='text-align: center;'> <br><br><a 
href='https://twitter.com/taneemishere' target='_blank'>Developed by Taneem Jan</a> </div> <div style='text-align: 
center;'> <a href='https://taneemishere.github.io/projects/project-one.html' target='_blank'>Paper</a> &ensp; &emsp; 
<a href='https://github.com/taneemishere/html-code-generation-from-images-with-deep-neural-networks' 
target='_blank'>Code</a> </div> """

interface_examples = ['examples/example-1.png', 'examples/example-2.png', 'examples/example-3.png']

# a gradio interface to convert a image to HTML Code
interface = gr.Interface(
    model_interface,
    inputs='image',
    outputs='text',
    allow_flagging="manual",
    title=interface_title,
    description=interface_description,
    article=interface_article,
    examples=interface_examples
)

interface.launch(share=False)
