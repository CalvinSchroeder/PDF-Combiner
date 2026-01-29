
from PyPDF2 import PdfReader, PdfWriter

def combine_pdfs(input_files, output_file):
    pdf_writer = PdfWriter()

    for file in input_files:
        file = file.strip().strip('"')
        print(f'Processing file: {file}')
        pdf_reader = PdfReader(file)
        # Assuming each file is one page; if not, iterate over pages:
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
    
    print(f'Combined PDF saved as {output_file}')

if __name__ == "__main__":
    # Take input of PDF files, separate each complete directory, code assumes each file name given with double quotation marks
    input_files = input("Enter the names of the PDF files to combine, separated by commas: ").split(',')

    output_file_name = input("Enter the name of the output file: ")
    
    output = "C:\\Users\\NAME\\Downloads\\" + output_file_name + ".pdf" #Hardcoded directory, change as desired

    combine_pdfs(input_files, output)

