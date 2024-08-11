# Based on: https://docs.unstructured.io/open-source/introduction/quick-start
## and https://docs.unstructured.io/open-source/installation/full-installation
# Full Installation in python venv enviroment
## pip install "unstructured[all-docs]"
 
from unstructured.partition.pdf import partition_pdf
from unstructured.cleaners.translate import translate_text
from transformers import MarianMTModel, MarianTokenizer
 
# Partition the PDF and process the elements
elements = partition_pdf(
    "./pdf_trans.pdf",                                 # name of pdf file to extract text from
    languages=["pl"],
    content_type="application/pdf",                    # content type is pdf. 
    include_page_breaks=True,
    strategy="fast",
    extract_image_block_types=["Table"],
    infer_table_structure=True,
    max_partition=None
)
 
# Combine the elements into a single string
pol_text = "\n\n".join([str(el) for el in elements])
 
# Write the original text to a file
with open("pl_pdf.txt", "w", encoding="utf-8") as f:      # name of translated text
    f.write(pol_text)
 
file_path = "./en_pdf.txt"    # name of a pdf file to translate
 
with open(file_path, 'w', encoding='utf-8') as file:
    for i, el in enumerate(elements):
        translated_chunk = translate_text(str(el),'pl','en')
        print(translated_chunk)
        file.write(f"{translated_chunk}\n\n")
