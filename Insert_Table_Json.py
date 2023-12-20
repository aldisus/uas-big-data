import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'uas_big_data'
}
 
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
        user_data = response.json()['data']
        user_data += response2.json()['data']
        user_data += response3.json()['data']
        user_data += response4.json()['data']
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for padat_pendu in user_data:
            cursor.execute('''
                INSERT INTO padat_pendu (id, kod_prov, nm_prov, bps_kod_kab, bps_nm_kab, bps_kod_kec, bps_nm_kec, keme_kode_kec, keme_nm_kec, semes, kepadat_pendu, satuan, tahun)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (padat_pendu['id'], padat_pendu['kode_provinsi'], padat_pendu['nama_provinsi'], 
                    padat_pendu['bps_kode_kabupaten_kota'], padat_pendu['bps_nama_kabupaten_kota'], padat_pendu['bps_kode_kecamatan'], 
                    padat_pendu['bps_nama_kecamatan'], padat_pendu['kemendagri_kode_kecamatan'], padat_pendu['kemendagri_nama_kecamatan'], 
                    padat_pendu['semester'], padat_pendu['kepadatan_penduduk'], padat_pendu['satuan'], 
                    padat_pendu['tahun']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 