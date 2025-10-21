"""
Nama: Muhamad Kharel Putra Pradana
NIM: 23090250017
Program: Data Mahasiswa Sederhana
"""

def tampilkan_info():
    nama = "Muhamad Kharel Putra Pradana"
    nim = "23090250017"
    prodi = "Teknik Informatika"
    
    print("=" * 40)
    print("Data Mahasiswa")
    print("=" * 40)
    print(f"Nama  : {nama}")
    print(f"NIM   : {nim}")
    print(f"Prodi : {prodi}")
    print("=" * 40)

def hitung_nilai():
    try:
        tugas = float(input("Masukkan nilai tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        
        nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
        return nilai_akhir
    except ValueError:
        return "Error: Masukkan nilai dalam bentuk angka"

def main():
    tampilkan_info()
    print("\nPerhitungan Nilai Akhir")
    nilai = hitung_nilai()
    
    if isinstance(nilai, float):
        print(f"\nNilai akhir Anda adalah: {nilai:.2f}")
    else:
        print(nilai)

if __name__ == "__main__":
    main()
