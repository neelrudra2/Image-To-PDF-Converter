# Rudraneel Bhattacharyya

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def image_to_pdf(input_image_path, output_pdf_path):
    # open the image using Pillow
    img = Image.open(r"input_image_location_in_jpg")

    # create a PDF file
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    # set the dimensions to fit the image on the page
    width, height = letter
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height

    if aspect_ratio > 1:
        img_width = width
        img_height = width / aspect_ratio
    else:
        img_height = height
        img_width = height * aspect_ratio

    # draw function
    c.drawInlineImage(r"input_image_location_in_jpg", 0, 0, width=img_width, height=img_height)

    # saving
    c.save()

if __name__ == "__main__":
    # Replace and create the output
    input_image_path = r"input_image_location_in_jpg"
    output_pdf_path = r"final_pdf_location_with_a_new_name"

    image_to_pdf(r"input_image_location_in_jpg", r"final_pdf_location_with_a_new_name")
