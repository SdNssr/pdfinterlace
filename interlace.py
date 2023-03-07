#!/usr/bin/env python3
import sys
import pypdf

def main():
    if len(sys.argv) != 3:
        print("./interlace.py <input pdf> <output pdf>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_pdf = pypdf.PdfReader(input_path)
    num_pages = len(input_pdf.pages)

    if (num_pages % 2) != 0:
        print("error: expected an even number of pages")
        print("(scan document front to back, and then flip over to scan the back)")
        sys.exit(1)

    output_pdf = pypdf.PdfWriter()

    # Pages are laid out ascending odd, and then descending even
    # i.e 1 3 5 7 8 6 4 2

    for page in range(1, num_pages + 1):
        if (page % 2) == 0:
            page_index = num_pages - (page // 2)
        else:
            page_index = (page // 2)
        print(page, page_index)
        output_pdf.add_page(input_pdf.pages[page_index])

    output_pdf.write(output_path)

if __name__ == "__main__":
    main()

