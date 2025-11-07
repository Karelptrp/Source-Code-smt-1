"""
Nama: Muhamad Kharel Putra Pradana
NIM: 23090250017
Saya menyatakan dengan ini bahwa kode yang saya tulis dalam ujian ini adalah
hasil karya saya sendiri. Saya tidak menerima atau memberikan bantuan dalam
bentuk apa pun selama ujian berlangsung.
"""
nim = "23090250017"  
list_nim = []
for digit in nim:
    list_nim.append(int(digit))
digit_terakhir = list_nim[-1]
status = "Genap" if digit_terakhir % 2 == 0 else "Ganjil"
def kalkulasi_nim(list_nim):
    total = sum(list_nim)
    hasil = total * list_nim[0]
    return hasil
hasil_kalkulasi = kalkulasi_nim(list_nim)
print(f"Analisis untuk NIM {nim}: Status digit terakhir adalah {status}, "
      f"dengan hasil kalkulasi {hasil_kalkulasi}.")
