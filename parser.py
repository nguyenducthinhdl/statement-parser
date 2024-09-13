import pymupdf
import csv

file_path = 'file-sao-ke.pdf'


def process_file(input_pdf, output_file_csv):
    doc = pymupdf.open(input_pdf)  # open a document

    with open(output_file_csv, 'w', newline='') as csvfile:
        fieldnames = ['date', 'amount', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(doc)):
            page = doc[i]
            text = page.get_text().split('Transactions in detail\n')[1].split('Page {0} of 12028'.format(i + 1))[0]
            text = text.split('\n')
            state = 1
            for line in text:
                if state == 1 and len(line) == len('04/09/2024') and line[len(line) - 4:] == '2024':
                    if 'data' in locals() or 'data' in globals():
                        writer.writerow(data)
                    # data = {'date': line, 'time': 'xxx', 'amount': -1, 'message': ''}
                    data = {'date': line, 'amount': -1, 'message': ''}
                    state = state + 1
                elif state == 2:
                    # data['time'] = line
                    state = state + 1
                elif state == 3:
                    data['amount'] = float(line.replace('.', ''))
                    state = 1
                elif state == 1:
                    data['message'] += line

            if data['amount'] != -1:
                writer.writerow(data)


if __name__ == '__main__':
    process_file(file_path, 'output.csv')
    print("End processing")