from pdf2image import convert_from_path
import os
# function to extact images from images object


def extractImages(images):
    i = 1   # i for indexing page numbers for each and every jpg extract from pdf
    os.mkdir(f'pathtopdffile/{pdf_file_name}')
    for image in images:
        image = image.rotate(-90, expand=True)
        image.save(f'Images_for_each_pdf/{pdf_file_name}/{pdf_file_name}-page-00{i}.jpg', 'JPEG')
        i += 1
# main function with loop through the given pdf files and the extract jpg from each pdf file


if __name__ == "__main__":
    for pdf in range(151, 180):
        if pdf == 175:   # 175 pdf is not available in given data set cuz we skip that in our loop
            continue
        pdf_file_name = str(pdf)   # extarct pdf file name
# create images object using pdf to convert pdf to jpg files
        pdf_file_to_convert_jpg = f"./151-180/{pdf_file_name}.pdf"
        images = convert_from_path(pdf_file_to_convert_jpg, 300)
        extractImages(images)   # call above function
        print("Success!")
