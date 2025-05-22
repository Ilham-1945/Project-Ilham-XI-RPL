# Changelog

Semua perubahan penting pada proyek ini akan didokumentasikan dalam file ini.

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
dan proyek ini mengikuti [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 22 Mei 2025

### Ditambahkan
- Rilis awal Sistem PPDB Online
- Sistem autentikasi pengguna (login/register)
- Kontrol akses berbasis peran (admin/pengguna)
- Formulir pendaftaran online dengan field:
  - Data pribadi (nama, info kelahiran, alamat)
  - Data akademik (sekolah, nilai)
  - Upload file ijazah
- Fitur dashboard admin:
  - Gambaran statistik pendaftaran
  - Review pendaftaran yang menunggu
  - Terima/tolak pendaftaran
  - Lihat semua pendaftaran
- Fitur dashboard pengguna:
  - Pelacakan progres pendaftaran
  - Monitoring status aplikasi
  - Preview formulir
  - Upload dokumen
- Desain UI/UX modern dengan Bootstrap 5
- Tata letak responsif untuk perangkat mobile
- Sistem upload file untuk ijazah
- Pesan flash untuk umpan balik pengguna
- Enkripsi password yang aman
- Integrasi database SQLite

### Diperbaiki
- Manajemen sesi pengguna
- Validasi formulir
- Batasan ukuran file upload
- Kontrol akses admin
- Relasi database

## [0.2.0] - 15 Mei 2025

### Ditambahkan
- Antarmuka dashboard admin
- Sistem review pendaftaran
- Fitur pelacakan status
- Fungsionalitas upload file
- Indikator progres
- Kartu statistik
- Tombol aksi cepat

### Diubah
- Peningkatan validasi formulir
- Penyempurnaan desain UI/UX
- Pembaruan skema database
- Restrukturisasi file proyek

### Diperbaiki
- Bug penanganan sesi
- Masalah relasi database
- Error pengiriman formulir
- Validasi upload file

## [0.1.0] - 1 Mei 2025

### Ditambahkan
- Autentikasi pengguna dasar
- Formulir pendaftaran sederhana
- Pengaturan awal database
- Template dasar
- Struktur proyek

### Diubah
- Pembaruan dependensi
- Peningkatan penanganan error
- Peningkatan fitur keamanan

## [Akan Datang]

### Direncanakan
- Export data ke Excel
- Cetak laporan
- Notifikasi email
- Statistik dashboard
- Pemrosesan batch
- Filter pencarian lanjutan
- Manajemen profil pengguna
- Fungsi reset password
- Manajemen pengguna admin
- Backup/restore sistem