import requests #library yang kita gunakan untuk mengakses API/json
import pandas as pd
import json
 
# Alamat URL API
api_url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jmlh_kpdtn_pnddk_brdsrkn_kcmtn_d_kt_bndng_rkp_smstr"

try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
    response2 = requests.get(api_url + "?page=2")
    response3 = requests.get(api_url + "?page=3")
    response4 = requests.get(api_url + "?page=4")
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        data_ = response.json()['data']
        data_ += response2.json()['data']
        data_ += response3.json()['data']
        data_ += response4.json()['data']

        print(data_)
        with open("data.json", "w") as json_file:
            json.dump(data_, json_file)
 
        # Baca data JSON dari file
        with open('data.json', 'r') as json_file:
            data = json_file.read()

        # Ubah JSON menjadi DataFrame pandas
        df = pd.read_json(data)
 
        # Simpan DataFrame ke dalam file Excel
        excel_file = 'kepadatan penduduk di kota bandung.xlsx'
        df.to_excel(excel_file, index=False)
 
        print(f"Data telah disimpan dalam file Excel: {excel_file}")
 
        # True jika ingin menampilkan hasil
        # False jika tidak ingin menampilkan hasil

        INGIN_DI_PRINT = False

        if INGIN_DI_PRINT:
            # Menampilkan hasil
            for padat_pendu in data_:
                print(f"id: {padat_pendu['id']}")
                print(f"kod_prov: {padat_pendu['kode_provinsi']}")
                print(f"nm_prov: {padat_pendu['nama_provinsi']}")
                print(f"bps_kod_kab: {padat_pendu['bps_kode_kabupaten_kota']}")
                print(f"bps_nm_kab: {padat_pendu['bps_nama_kabupaten_kota']}")
                print(f"bps_kod_kec: {padat_pendu['bps_kode_kecamatan']}")
                print(f"bps_nm_kec: {padat_pendu['bps_nama_kecamatan']}")
                print(f"keme_kode_kec: {padat_pendu['kemendagri_kode_kecamatan']}")
                print(f"keme_nm_kec: {padat_pendu['kemendagri_nama_kecamatan']}")
                print(f"semes: {padat_pendu['semester']}")
                print(f"kepadat_pendu: {padat_pendu['kepadatan_penduduk']}")
                print(f"satuan: {padat_pendu['satuan']}")
                print(f"tahun: {padat_pendu['tahun']}")
                print("-" * 30)
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 
 

