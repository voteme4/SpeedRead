from PIL import Image 
import pytesseract as OCR #OCR stands for Optical Character Recognition
import pdf2image
import sys
import tempfile
import time

def pdf2text(file_path, first_page, last_page):
    with tempfile.TemporaryDirectory() as path:
        images = pdf2image.convert_from_path(file_path, output_folder=path, first_page=int(first_page), last_page=int(last_page))
        print("Images extracted from PDF")
    pages = []
    for image in images:
        pages.append(OCR.image_to_string(image))
    print("Text extracted from Images")
    return pages

def main():
    try:
        pages = pdf2text(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print("Please provide a command line argument of a PDF filepath, first_page, and last_page.")
        sys.exit()
    except FileNotFoundError:
        print("Provided command line argument is not a valid PDF filepath.")
        sys.exit()
    except ValueError:
        print("Please provide a valid first and last page argument.")
        sys.exit()

    for page in pages:
        for line in page.split("\n"):
            for word in line.split(" "):
                print(word)
                time.sleep(0.05)

if __name__=="__main__":
    main()