import cv2

from utils.find_contures import process_image_and_return_contours, get_contours_positions, \
    get_display_contours_positions
from fastapi import FastAPI, Response , File
import io
from fastapi import UploadFile
from PIL import Image
app = FastAPI()


from typing import Annotated




@app.post("/files/")
def create_file(file: Annotated[bytes , File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploa-dfile/")
def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


@app.post("/find-contures")
def say_hello(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    #
    image_array = process_image_and_return_contours(file)
    image = Image.fromarray(image_array.astype('uint8'), 'RGB')

    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Return the image bytes with the correct content type
    return Response(content=img_bytes, media_type="image/png")



@app.post("/find-contures-positions")
def find_contours_positions(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    #
    positions = get_contours_positions(file)
    return {"positions": positions}


@app.post("/display-contures-positions")
def display_contours_positions(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    #
    image_array = get_display_contours_positions(file)
    image = Image.fromarray(image_array.astype('uint8'), 'RGB')
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Return the image bytes with the correct content type
    return Response(content=img_bytes, media_type="image/png")








'''
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/find-contures")
async def say_hello(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
    #
    print("asdfsad")
    image_array = process_image_and_return_contours(file)
    image = Image.fromarray(image_array.astype('uint8'), 'RGB')

    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Return the image bytes with the correct content type
    return Response(content=img_bytes, media_type="image/png")


'''