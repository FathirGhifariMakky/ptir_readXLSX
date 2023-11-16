import openpyxl

def baca_file_excel(nama_file):
    try:
        workbook = openpyxl.load_workbook(nama_file)

        sheet = workbook.active

        for row in sheet.iter_rows():
            for cell in row:
                print(cell.value, end='\t')
            print()
    except FileNotFoundError:
        print(f"File '{nama_file}' Tidak ditemukan")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    nama_file = "V-class.xlsx"
    baca_file_excel(nama_file)