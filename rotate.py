import pathlib
import PyPDF2
import sys


def rotate(filepath: pathlib.Path, angle: int) -> None:
    if not filepath.exists():
        print(f'File not found: {filepath}', file=sys.stderr)
        return

    filepathOut = ('rotated_' + filepath.name)
    if filepath.parent:
        filepathOut = filepath.parent / filepathOut
    print(f'Source file: {filepath.name}')
    print(f'Rotated file will be saved as: {filepathOut.name}')

    try:
        with open(filepath, 'rb') as fin, open(filepathOut, 'wb') as fout:
            reader = PyPDF2.PdfReader(fin)
            writer = PyPDF2.PdfWriter(fout)

            page = reader.pages[-1]
            page.rotate(angle)
            writer.add_page(page)
            writer.write(fout)

    except (FileNotFoundError, PermissionError) as e:
        print(e, file=sys.stderr)

    return

def rotateMultiPage(filepath : pathlib.Path, angle : int) -> None:
    if not filepath.exists():
        print(f'File not found: {filepath}', file=sys.stderr)
        return

    filepathOut = ('rotated_' + filepath.name)
    if filepath.parent:
        filepathOut = filepath.parent / filepathOut
    print(f'Source file: {filepath.name}')
    print(f'Rotated file will be saved as: {filepathOut.name}')

    try:
        with open(filepath, 'rb') as fin, open(filepathOut, 'wb') as fout:
            reader = PyPDF2.PdfReader(fin)
            writer = PyPDF2.PdfWriter(fout)

            for page in reader.pages:
                page.rotate(angle)
                writer.add_page(page)

    except PermissionError as e:
        print(e, file = sys.stderr)

    return


def main(argv: list[str]):
    filepath = pathlib.Path.home() / 'Lyn Documents/Security/IS Training/Signed/IS_Training_2023.pdf'
    rotate(filepath, 90)


if __name__ == '__main__':
    main(sys.argv)
