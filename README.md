Nama : Ali Jundi Qowi

NPM : 2506611585

Kelas : PBP E



7/9/26: Menambahkan Skills dan Mengubah Tampilan web. Git push ke pws  
### Tugas 1
1. Kadang pakai kadang juga tidak. Tergantung kebutuhan aja. tadinya mau coba pake aside dan lain-lain buat bagian skill. Tapi jadinya pakai card/carousel bootstrap soalnya udah kenal sedikit. Paling di bagian experience ada <article>.. dua aja sih. Tujuannya buat tampilan ke bawah (vertikal).
2. Tantangan nya yaitu saat coba flex, ada satu bagian teks menimpa teks lainnya. Setelah ditelurusi kelihatannya karena belum di-styling dan diatur sesuai tempat. Untungnya di beberapa bagian saya menggunakan bootstrap jadi bisa lebih cepat. Ukuran gambar harus diperkecil dan tidak memenuhi seisi website. 
3. Kalau mau nambah konten, misal skill atau pengalaman itu manual dan harus tulis ulang seluruh kode. Pengennya sih bisa langsung diubah seperti inspect atau semacamnya. Tambahan: mau buat dark mode tapi belum belajar js huhuhu.
-------------------------------------------------
Update 13/9/26: Sedikit cerita. Tentu saja saya gunakan AI karena sudah malam dan agak ngantuk. tapi ga semata-mata saya full copy paste. Hanya melihat beberapa baris kode yang perlu diubah dan kadang lupa beberapa hal(seperti cara nambahin musik lupa)...
### Tugas 2
1. urls.py terhubung dengan views.py. Di views.py ada fungsi-fungsi yang akan menampilkan masing-masing model, contoh Music dan Experience.
fungsi show akan mengarahkan ke url sesuai template(misal musics.html atau experience.html) yang diberikan pada fungsi

2. Karena lebih rapih. Meminimalisir pengembang seperti saya mengoprek-oprek kode panjang di template.

3. makemigrations membuat migrasi baru, misal saya membuat model baru bernama Music. Kemudian fungsi migrate itu untuk menerapkan migrasi tersebut. Contoh perubahan model saya tambahkan Music. Agar dapat teraplikasi di webnya saya gunakan kedua fungsi tersebut

Karena saya gak benar-benar lepas dari penggunaan AI untuk Tugas 2, jadi saya sertakan chat berikut:

https://gemini.google.com/share/d/1PCadbqBAjLSJzE5rnNK6G_FwFwb41P_1?usp=sharing
---------------------------------------------
14/9/26: coba push ke pws
        -ubah ke django~=5.0
        -oke tadi lupa nulis pip m install requirements.txt

15/9/26: oke ternyata aku lupa ubah beberap key dalam environment variable. coba push ulang biar ke deploy 

TAMBAHAN: aku lupa tadi malam sempa mengerjakan sedikit tutorial. commit sebelunya lupa kusebut pengerjaan ini. Tapi tutorialnya belum selesai.  

16/9/26: Selesai Tutorial 1. Tapi nampaknya desain webnya belum rapi.
Banyak sih yang ditambahin kayak project_delete, project create, tombol pencarian, dan lain-lain

20/9/26: oh iya tadi sebenernya ada beberapa yang belum dirapihin. Belum semuanya dirapiin setelah dicek. jadi kuperhatikan ulang kodenya dan kurapihkan lagi.

Udah beres tambah fitur add music, delete sama edit eh rupanya aku salah beberapa variabel misal harusnya "id" tapi malah "music_id" thanks to Gemini AI yang mau ngoreksi saya.

21/9/26: Aku mau nambahin tugas pertanyaan reflektif
### Tugas 3

1. Kita pakai yang sudah disediakan Django karena kalau pakai HTML manual, kita harus cek satu satu apakah ada serangan berbahaya dari input. Django forms memberi kemananan input. Model django juga terintegrasi dengan database langsung
Csrf token wajib di sini agar lebih aman dari serangan luar.

2. JSON lebih disukai karena lebih mudah dari XML. Developer web juga mau yang lebih cepat dan menghasilkan lebih besar kan. Jadi JSON lebih disukai. Intinya memudahkan developer. 

2. Misal ada dua kotak yang sama, yang satu lagu Indonesia Raya sementara di sebelahnya ada lagu Indonesia Raya juga, ID berguna untuk memberikan masing-masing kode unik. Jadi django tidak bingung kalau mau edit atau hapus
3. Alur dari request( klien minta akses http), lalu ke routing ke url, lanjut ambil data portofolio dari database. Data yang dihasilkan berbentuk kumpulan objek python, serialisasi kemudian mengubah objek objek model tersebut jadi format data sederhana seperti list atau dict. Kemudian dikonversi jadi string dengan format JSON. Response mengembalikan data JSON ke klien menggunakan HttpResponse atau JsonResponse. Data JSON siap dipakai.

Serialization diperlukan untuk mengatasi ketidakcocokan format dan standardisasi format data. JSON merupakan standar format pertukaran data secara universal di web. Serialization bertugas mengubaj objek django ke format teks JSON yang mudah dibaca dan diolah JavaScript di frontend

AI Disclosure untuk Tugas 3:
Dalam penyelesaian Tugas 3 ini, saya memanfaatkan AI Gemini
link: https://gemini.google.com/share/d/13nF-qHX0Uwndu-xSGauHjhG83Ia2HRb2?usp=sharing
1. Debugging dan memahami pesan error Djago ketika beberapa url tidak bekerja
2. Membantu menjelaskan konsep teori
-----------------------------------------
22/9/26: mulai tutorial 4, semoga selesai hari ini
Bagian 1 beres nambahin fitur login logout.
Bagian 2 dan 3 beres, lumayan lama ngerjainnya
Oh iya bagian yang opsional menarik sih, tapi nanti kukerjakan, mau istirahat dulu