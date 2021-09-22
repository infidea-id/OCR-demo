import gradio as gr
import cv2
import numpy as np
import scipy
import easyocr 

reader = easyocr.Reader(["id", "en"])

def predict(inp):
    img = inp.astype('uint8')
    result = reader.readtext(img)

    empty_img = np.ones([img.shape[0], img.shape[1], img.shape[2]], dtype=np.uint8) * 255

    for text_info in result: 
        coor1, coor2, coor3, coor4 = text_info[0]
        left, top = coor4 
        right, down = coor2 
        text = text_info[1]
        
        color = (0,0,255)
        text_color = (255,0, 0)
        thickness = 2 
        try: 
        
            img = cv2.rectangle(img, (left, top), (right, down), color, thickness)
            empty_img = cv2.rectangle(empty_img, (left, top), (right, down), color, thickness)
            empty_img = cv2.putText(empty_img, "{}".format(text), (left, top - 5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                            text_color)
        except: 
            continue 

    output_img = cv2.hconcat([img, empty_img])

    return output_img, "Labeled Image"


title = "INFIDEA Optical Character Recognition"
desc = "Upload/Choose some images to show the texts inside the image"
# examples = [
#     ["example_images/3.png"],
#     ["example_images/2.png"],
#     ["example_images/1.png"],
# ]

examples = [
    ["example_images/1.jpg"]
]
inputs = gr.inputs.Image(label="Image Containing Texts")
outputs = [gr.outputs.Image(label="Predicted Texts"), gr.outputs.Label(label="Left: Bounding Boxed Image, Right: Showing Text")]
gr.Interface(fn=predict, inputs=inputs, outputs=outputs, title=title, description=desc, examples=examples,
             allow_flagging=False, server_name="0.0.0.0", server_port=8000).launch()