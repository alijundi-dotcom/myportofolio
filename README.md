Nama : Ali Jundi Qowi

NPM : 2506611585

Kelas : PBP E

Karena saya gak benar-benar lepas dari penggunaan AI, jadi saya sertakan chat berikut:

https://gemini.google.com/share/d/1PCadbqBAjLSJzE5rnNK6G_FwFwb41P_1?usp=sharing

7/9/26: Menambahkan Skills dan Mengubah Tampilan web. Git push ke pws  
### Tugas 1
1. Kadang pakai kadang juga tidak. Tergantung kebutuhan aja. tadinya mau coba pake aside dan lain-lain buat bagian skill. Tapi jadinya pakai card/carousel bootstrap soalnya udah kenal sedikit. Paling di bagian experience ada <article>.. dua aja sih. Tujuannya buat tampilan ke bawah (vertikal).
2. Tantangan nya yaitu saat coba flex, ada satu bagian teks menimpa teks lainnya. Setelah ditelurusi kelihatannya karena belum di-styling dan diatur sesuai tempat. Untungnya di beberapa bagian saya menggunakan bootstrap jadi bisa lebih cepat. Ukuran gambar harus diperkecil dan tidak memenuhi seisi website. 
3. Kalau mau nambah konten, misal skill atau pengalaman itu manual dan harus tulis ulang seluruh kode. Pengennya sih bisa langsung diubah seperti inspect atau semacamnya. Tambahan: mau buat dark mode tapi belum belajar js huhuhu.

Update 13/9/26: Sedikit cerita. Tentu saja saya gunakan AI karena sudah malam dan agak ngantuk. tapi ga semata-mata saya full copy paste. Hanya melihat beberapa baris kode yang perlu diubah dan kadang lupa beberapa hal(seperti cara nambahin musik lupa)...
### Tugas 2
1. urls.py terhubung dengan views.py. Di views.py ada fungsi-fungsi yang akan menampilkan masing-masing model, contoh Music dan Experience.
fungsi show akan mengarahkan ke url sesuai template(misal musics.html atau experience.html) yang diberikan pada fungsi

2. Karena lebih rapih. Meminimalisir pengembang seperti saya mengoprek-oprek kode panjang di template.

3. makemigrations membuat migrasi baru, misal saya membuat model baru bernama Music. Kemudian fungsi migrate itu untuk menerapkan migrasi tersebut. Contoh perubahan model saya tambahkan Music. Agar dapat teraplikasi di webnya saya gunakan kedua fungsi tersebut

14/9/26: coba push ke pws
        -ubah ke django~=5.0
        -oke tadi lupa nulis pip m install requirements.txt
15/9/26: oke ternyata aku lupa ubah beberap key dalam environment variable. coba push ulang biar ke deploy 