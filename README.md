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
27/9/26: beres sampai di menambahkan fitur editor bagi user yang memiliki akses edit. sebelumlangkah ini juga membuat group editor di django administration agar beberapa user yang dikehendaki menjadi editor bisa melakukan edit musik atau project dalam website. Oh iya, malam ini juga aku baru ingat ternyata fitur edit musik sudah ada? aku tidak ingat kapan menambakan fitur tersebut. Mungkin saat selesai tutorial 4 dan sedikit utak-atik kode..

Tadi pas kucek, ternyata ada yang kulupa bahwa tombol toggle star belum muncul. itu karena logika dalam projects.html salah. harusnya siapapun bisa star dan unstar suatu musik atau project

Oke tambahan lagi, jadi membetulkan musics.html soalnya beberapa hal harusnya tidak di sana. Editor hanya boleh edit. Hanya admin yang bisa lakukan semuanya. User biasa hanya bisa lihat.

28/9/26: beberapa tombol tampak hampir tidak terlihat di beberapa halaman seperti projects.html, login.html, dan register.html. Aku samakan semua tombol dengan tombol github, email, dan linkedin di halaman profile.

AI Disclosure untuk Tugas 4: Belum menerapkan strategi prompting yang begitu tepat. Aku pakai Gemini AI untuk membantu penyelesaian Tugas 4 dengan memahami kode, langkah-langkahnya, dan debug error.
Chat: https://gemini.google.com/share/d/1y6hdCPbC2dOZHkyALvZrJpJzdNcEbyvQ?usp=sharing

29/9/26: Nambah dark mode
Mulai Tutorial 5. Masuk ke materi javascript.

30/9/26: Beres Tutorial 5
Cerita malem-malem aku ngabisin waktu banyak buat nampilin card di musics.html... Wah pusing parah.
Chat sama AI: https://gemini.google.com/share/d/1ib0RcGqPEXFRUd47gLGwXfmbvqG5aW5z?usp=sharing
AI digunakan untuk debugging sih kebanyakan di chat ini. Aku rasa kodenya benar, tapi ketika aku mau tambah musik, datanya tidak muncul terus. Bingung kan, jadinya nanya-nanya AI.

Coba push pws

5/10/26: kemaren hari Ahad aslinya fix styling dark mode di beberapa halaman. lupa ketulis


### Tugas 5

1. Debouncing == teknik menunda eksekusi suatu fungsi hingga waktu tertentu tanpa adanya event baru. 
Pentingnya: - mencegah overload server
            - Menghemat sumber daya
            - mencegah race condition
2. Await digunakan untuk menghentikan kode sampai Promise dari fetch() selesai diproses dan mengembalikan objek Response secara nyata
Tanpa await: - baris kode berikutnya dieksekusi tanpa nunggu request server selesai
             - Variabel penampung respons isinya bukan data JSOn atau Response, tapi objek Promise <pending>
             - Kalau mengakses method response.json() atau response.ok secara langsung nanti TypeError atau undefined
3. Serangan XSS yaitu ketika si hacker kasih input berbahaya seperti<script>alert('XSS')</script>.... input bahaya begitu bisa saja mencuri cookie, session token, atau webnya jadi berantakan

Secara, django template punya pembersihan sendiri. Kalau AJAX, dia ngambil data raw JSON dari server, teks mentah. Misal di innerHTML ada music.title dan kalau tidak dibersihkan misal music title isinya ada tag script yang berbahaya, browsernya bakal eksekusi dan terjadilah serangan XSS. Makanya ada kita bikin escapeHtml.

AI Disclosure untuk Tugas 5:
chat: https://gemini.google.com/share/d/1NMX6E1xARzCYDvLO1W_gELXDYILLiRIM?usp=sharing

Gemini kadang ngasih kode kepanjangan. Aku jadi mengerjakannya dua kali. Dia begitu buta kalau tidak diberi konteks yang lengkap. Dibuat muter-muter aku sama kode yang dia kasih. Misal aku hanya tanya kenapa ini tidak bisa muncul music card setelah perubahan, 2-3 chat baru dia kasih jawaban yang bener.. hadeuhhh
Lebih terpakai buat debugging sih ya Gemini ini. walaupun kadang error jawaban dia. Alhasil tetep debug sendiri bagian yang salah.

Oke itu soal AI disclosure saya..
Oh iya satu hal lagi yang lupa. Aku baru pakai commit git conventional sejak 4/10/26. Maaf, aku terlalu bersemangat untuk menyelesaikan Tutorial dan Tugasnya

### Tugas 6
1. REST adalah rancangan komunikasi sistem berbasis web yang menggunakan protokol HTTP secara konvensional seperti client-server, stateless, cacheable, dan uniform interface

Mengmbalikan data dalam format JSON saja belum  cukup untuk membuat sebuah API disebut RESTful. JSON hanya bentuk representasi data(payload). Sebuah API  baru dapat dikategorikan Restful jika memenuhi prinsip-prinsip utama REST yang teridir dari Resoursce-Based Endpoints, HTTP Verbs Semantics, Penggunaan HTTP Status Code yang benar, Stateless ness dan Hypermedia As The Engine Of Application State

Perbedaan Put & PATCH
Pembaruan
PUT: FUll update
PATCH: partial update

Kelengkapan payload
PUT: Field yg tidak dikirm bisa di set null atau default
PATCH: field yang tidak dikirim akan tetap bernilai sama dengan sebelumnya

Idempotensi
PUT: ya
PATCH: secara umum tidak, tergantung logika pembaruan di server

Gunakan PUT:
Ketika user ingin update seluruh profilnya, username, email, bio, dan lain lain
Gunakam PATCH: 
Update judul proyek aja tanpa ubah ubah yang lain

2. Serializer pada DRF bertindak sebagai komponnen konversi dua arah
 1. Serialization: mengubah objek django jadi data python seperti list atau dict yg kemudian diubah ke JSON/XML untuk dikirm ke klien
 2. Deserialization: Terima payload JSON dari klien, Validasi data tersebut, kemudian konversi ke tipe data python atau Django yang bisa disimpan ke database

Keuntungan DRF Serializer dibanding Manual DIctionary, cukup panggil serializer.is_valid() untuk validasi data dan serializer.save() untuk simpan di database, daripada JSON yang harus tulis manual. Serializer dapat digunakan agar kode yang kepanjangan bisa disingkat. 
Penanganan relasi efisien dan rapi, daripada pakain .join(), serializer punya nested serializer, primarykeyrelatedfield, atau slugrelatedfield yang menangani serialisasi secara deklaratif dan konsisten.

Serializer secara otomatis memuat skema form interaktif pada tampilan Browsable API DRF, memudahkan pengujian via browser dan terintegrasi langsung dengan alat pembuat dokumentasi API otomatis seperti OpenAPI / Swagger

3. Perbedaan Otentikasi dan Ototrisasi

Otentikasi: untuk user, identifikasi pengguna
Otorisasi: Hak akses tiap pengguna. misal user biasa cuma bisa liat-liat. editor bisa ngubah ngubah, admin bisa hapus/buat

Pemeriksaan hak akses wajib dilakukan di sisi server menggunakan Permission Class dan tidak boleh hanya mengandalkan penyembunyian tombol di template HTML. Pengguna bisa saja hapus atribut disabled atau otak atik elemen DOM pakai DevTools atau F12

Menyembunyika tombol edit atau hapus, tapi penyerang bisa aja nebak nebak endpoint API secara langsung.
Kalau server backed tidak memeriksa otorisasi, server akan tetap memproses tindakan bahaya tersebut walaupun tombol di template tidak pernah di klik

4. CSRF Token pada SessionAuthentication & Testing DRF
Cara kerja SessionAutenticcation yaitu mengandalkan session cookie yang disimpan di browser untuk mengenali identitas pengguna.
Ketika request HTTP dikirim ke suatu domain, browser secara otomatis menyertakan cookie yang tersimpan untuk domain tersebut termasuk request yang dipicu oleh situs pihak ketiga(cross-site)
Jika seorang user sedang terautentikasi di aplikasi utama, terus buka web aneh aneh(bahaya), situs bahaya tersebut bisa eksekusi script dan bikin update ke API utama. Karena browser menyertakan session cookie, API utama akan menganggap request tersebut valid.
Makanya Django memerlukan CSRFToken, biasanya di header X-CSRFToken, agar situs bahaya tidak bisa baca cookie csrftoken milik domain utama, penyerang gabisa masukin tokenCSRF sembarangan.

Kenapa pengujian menggunakan force_authenticate tidak cukup membuktikan csrf berjalan?
Pada skenario unit test DRF, metode force_authentucate bekerja dengan menyuntikkan objek user langsung ke objek request. 
foce_authenticare memang dirancang ybtuk mempercpat pengujian logika view tanpa harus memuat alur autentikasi HTTP lengkap. AKibatnya, metode ini secara otomatis melewati seluruh proses pemeriksaan middleware autentikasi dan pengecekan token CSRF
Pengujian yang menggunakan force_authenticate akan selalu verhasil walau CSRF server sedng mati atau salah
Untuk menguji apakah CSRF benar aktif, pengujian harus mensimulasikan alur autentikasi berbasis sesi yang sesungguhnya dan mencoba mengirim permitaan update data anpa header X-CSRFToken. Test sukses kalau server menolak permintaan  tersebut, 403 Forbidden

