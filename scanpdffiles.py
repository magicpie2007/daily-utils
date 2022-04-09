import os.path
import sys
import PyPDF4


def main(args):
    if len(args) != 2:
        print_usage()
        exit(1)

    scan_dir = args[0]
    output_file_path = args[1]

    pdf_files = scan_pdf_files(scan_dir)

    output_file = open(output_file_path, 'w')
    for pdf_file in pdf_files:
        line = [pdf_file, os.path.dirname(pdf_file), os.path.basename(pdf_file), str(get_num_of_pages(pdf_file))]
        print(line[2], line[3])
        output_file.write(','.join(line) + '\n')

    output_file.close()


def scan_pdf_files(scan_dir):
    pdf_files = []
    for file in os.listdir(scan_dir):
        path = os.path.join(scan_dir, file)
        if os.path.isdir(path):
            pdf_files = pdf_files + scan_pdf_files(path)
        elif file.endswith(".pdf"):
            pdf_files.append(path)

    return pdf_files


def get_num_of_pages(pdf_file):
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)
    return pdf_reader.getNumPages()


def print_usage():
    """Print usage"""
    print("Usage: scanpdffiles scan_dir output_csv")


if __name__ == '__main__':
    main(sys.argv[1:])

