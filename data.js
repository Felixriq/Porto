/* IDENTITAS & KONTAK */
var SITE = {
  name:  'Muhammad Thoriq Salahudin Haryoto',
  email: 'thoriqharyoto@gmail.com',
  cv: 'Dokumen/Dokumen/CV Muhamad Thoriq Salahudin Haryoto.pdf',
  foto: 'Dokumen/Profil.jpg',
  logo: 'MT',
  kontakJudul: 'Mari mengerjakan sesuatu bersama.',
  kontakTeks:  'Terbuka untuk kolaborasi, proyek, dan kesempatan baru.',
  soc: [
    ['GitHub',    'https://github.com/Felixriq'],
    ['LinkedIn',  'https://www.linkedin.com/in/muhammad-thoriq-salahudin-haryoto-093245329/'],
    ['Instagram', 'https://instagram.com/thoriqharyoto_']
  ]
};

var GH = 'https://github.com/Felixriq';
var P = [
   {
     t:'Aplikasi BMR BMI', 
     s:'Aplikasi Terminal', 
     c:'Pemrograman Bahasa C', 
     k:'GitHub', 
     img:'Proyek/Aplikasi BMR BMI.png',
     d:'Aplikasi Gizi yang menghitung BMR dan BMI berbasis terminal dengan bahasa C.',
     l:[['GitHub', 'https://github.com/Danlions/Aplikasi_BMR_BMI']]},
   {
     t:'Arm Manipulator', 
     s:'Prototipe Hardware', 
     c:'Hidrolik', 
     k:'Google Drive', 
     img:'Proyek/Arm Manipulator.png',
     d:'Proyek Arm Manipulator yang bergerak dengan tenaga kerja hidrolik.',
     l:[['Google Drive','https://drive.google.com/file/d/1UguEo3sYAD_Tot8RvDvcMIK8npNTgNe_/view?usp=drive_link']]},
   {
     t:'Gerbang Logika', 
     s:'Dokumentasi Praktikum', 
     c:'Sistem Digital', 
     k:'Google Drive', 
     img:'Proyek/Sistem Digital.png',
     d:'Mengimplementasikan cara kerja dari bermacam-macam gerbang logika dengan Decoder dan Encoder.',
     l:[['Google Drive','https://drive.google.com/file/d/1CeRb-HbjCBvEv0oFfq2O6peWsMQSXubM/view?usp=drive_link']]},
   {
     t:'Steam Kendaraan', 
     s:'Aplikasi Dekstop', 
     c:'Pemrograman Bahasa Java', 
     k:'GitHub', 
     img:'Proyek/Steam Kendaraan.png',
     d:'Proyek aplikasi Steam Kendaraan menggunakan netbeans dan pembuatan ui scene builder serta terintegrasi dengan database MySQL dengan bahasa Java.',
     l:[['GitHub', 'https://github.com/Danlions/SteamKendaraan']]},
   {
     t:'Sampah Pintar', 
     s:'Prototipe Hardware', 
     c:'Sensor dan Sistem Tertanam', 
     k:'Google Drive', 
     img:'Proyek/Smart Trash Bin.png',
     d:'Proyek prototipe tempat sampah pintar dengan sensor ultrasonik sebagai tanda sampah penuh dan sensor MQ-135 sebagai tanda kebusukan sampah.',
     l:[['Google Drive','https://drive.google.com/drive/folders/1gWlqXRRsQeG_LsKE_dB8E441iou95GrS?usp=drive_link']]},
   {
     t:'Stairpoint', 
     s:'Prototipe Hardware + Software', 
     c:'Desain Interaksi', 
     k:'Google Drive + Figma',
     img:'Proyek/Stairpoint.png',
     d:'Proyek prototipe Stairpoint yang terdiri dari sistem scan rfid dengan desain aplikasi android, alat ini memotivasi pengguna untuk lebih menggunakan tangga untuk tujuan kesehatan dengan sistem poin yang bisa ditukar dengan benefit di dalam aplikasi Stairpoint.',
     l:[['Google Drive','https://drive.google.com/drive/folders/1mOqLdpstIWoZsfKHevWyLIrnGOa_aq86?usp=sharing'],['Figma','https://www.figma.com/design/ksEbT7dhCwe58sz4lYnQcZ/Untitled?node-id=0-1&p=f']]},
   {
     t:'Simulasi Conveyor Sorting', 
     s:'Wokwii + Firebase', 
     c:'Internet Of Things', 
     k:'Google Drive + Youtube', 
     img:'Proyek/Conveyor Sorting.png',
     d:'Proyek simulasi IoT di Wokwi yang terintegrasi dengan database Firebase, simulasi ini mendeteksi gangguan pada sensor, barang yang macet dan situasi darurat.',
     l:[['Google Drive', 'https://drive.google.com/drive/folders/1AkAfrnCVk52F6jVmTkJFe8bezaL5ry-T?usp=sharing'],['Youtube','https://youtu.be/EnWbhDzTwLU?si=0SNzQVF6LQO50RB0']]},
   {
     t:'Dobot Arm Manipulator', 
     s:'Program dan Logika', 
     c:'Robotika', 
     k:'Google Drive', 
     img:'Proyek/Dobot.png',
     d:'Praktikum menjalankan dengan program dan logika dari aplikasi dobot lab untuk menggerakkan robot dobot dengan blockly dan manual training.',
     l:[['Google Drive','https://drive.google.com/drive/folders/1sG-1Ixx9NI4PMLl-JJmxsFfLUXx6CqeA?usp=sharing']]}
];

/* SKILL SOFTWARE */
var SKILLS = [
  /* Desain & Grafis */
  {k:'Desain & Grafis', n:'Figma', d:'Desain antarmuka', i:'figma', m:'Fg'},
  {k:'Desain & Grafis', n:'Canva', d:'Desain grafis', i:'canva', m:'Cv'},
  {k:'Desain & Grafis', n:'AutoCAD', d:'Gambar teknik 2D dan 3D', i:'autocad', m:'AC'},
  {k:'Desain & Grafis', n:'SketchUp', d:'Pemodelan 3D', i:'sketchup', m:'SU'},

  /* Pengeditan Video & Kreatif */
  {k:'Pengeditan Video & Kreatif', n:'Adobe Premiere Pro', d:'Editing video profesional', i:'premiere', m:'Pr'},
  {k:'Pengeditan Video & Kreatif', n:'CapCut', d:'Editing video', i:'capcut', m:'Cc'},
  {k:'Pengeditan Video & Kreatif', n:'OBS Studio', d:'Rekaman dan streaming', i:'obs', m:'OBS'},

  /* Aplikasi Produktivitas */
  {k:'Aplikasi Produktivitas', n:'Microsoft Excel', d:'Pengolahan data', i:'excel', m:'Xl'},
  {k:'Aplikasi Produktivitas', n:'Microsoft Word', d:'Dokumen dan laporan', i:'word', m:'Wd'},
  {k:'Aplikasi Produktivitas', n:'Microsoft PowerPoint', d:'Presentasi', i:'powerpoint', m:'Pp'},

  /* Pemrograman & Perangkat Keras */
  {k:'Pemrograman & Perangkat Keras', n:'Visual Studio Code (VS Code)', d:'Editor kode', i:'vscode', m:'VS'},
  {k:'Pemrograman & Perangkat Keras', n:'Arduino IDE', d:'Pemrograman mikrokontroler', i:'arduino', m:'Ar'},
  {k:'Pemrograman & Perangkat Keras', n:'Python', d:'Bahasa pemrograman', i:'python', m:'Py'},
  {k:'Pemrograman & Perangkat Keras', n:'C / C++', d:'Bahasa pemrograman', i:'cplusplus', m:'C+'},
  {k:'Pemrograman & Perangkat Keras', n:'Wokwi', d:'Simulasi IoT', i:'wokwi', m:'Wk'},
  {k:'Pemrograman & Perangkat Keras', n:'Firebase', d:'Backend dan database', i:'firebase', m:'Fb'},
  {k:'Pemrograman & Perangkat Keras', n:'Git & GitHub', d:'Version control', i:'git', m:'Git'}
];

var CERTS = [
  /* Cognitive Class AI (8 Sertifikat PDF Anda) */
  {k:'Cognitive Class AI', t:'Machine Learning Basics', s:'Cognitive Class (IBM)', y:'2026', f:'Machine Learning Basics.pdf', u:'https://cognitiveclass.ai/certificates/3e57a30f-4acb-4cdb-b977-d33cbba11aa7'},
  {k:'Cognitive Class AI', t:'A Quick Introduction to Machine Learning', s:'Cognitive Class (IBM)', y:'2026', f:'A quick introduction to machine learning.pdf', u:'https://courses.cognitiveclass.ai/certificates/ccb9a800cddf4a478fbdf8de212f0926'},
  {k:'Cognitive Class AI', t:'Precise Predictions: Classification for Flower and Tumors', s:'Cognitive Class (IBM)', y:'2026', f:'Classification for flower and Tumors.pdf', u:'https://courses.cognitiveclass.ai/certificates/93b0fe1b6db4417fa4ed88a4746a21f5'},
  {k:'Cognitive Class AI', t:'Customer Clustering with KMeans to Boost Business Strategy', s:'Cognitive Class (IBM)', y:'2026', f:'Customer Clustering with Kmeans to Boost Business Straregy.pdf', u:'https://courses.cognitiveclass.ai/certificates/470b16bde4f4477089d75253700c97b7'},
  {k:'Cognitive Class AI', t:'Predictions: Regression for Car Mileage and Diamond Price', s:'Cognitive Class (IBM)', y:'2026', f:'Regression For Car Mileage and Diamond Price.pdf', u:'https://courses.cognitiveclass.ai/certificates/8e766ddf32274e678fb8a6a37c9047b6'},
  {k:'Cognitive Class AI', t:'Data Analysis with Python', s:'Cognitive Class (IBM)', y:'2026', f:'Data Analysis With Python.pdf', u:'https://courses.cognitiveclass.ai/certificates/19f9030bcb3f4268b8b04fdb0ab2cc50'},
  {k:'Cognitive Class AI', t:'Machine Learning with Python', s:'Cognitive Class (IBM)', y:'2026', f:'Machine Learning with Python.pdf', u:'https://courses.cognitiveclass.ai/certificates/2d2edeb5983d407a912c613e279c8b01'},
  {k:'Cognitive Class AI', t:'Python 101 for Data Science', s:'Cognitive Class (IBM)', y:'2026', f:'Python 101 For Data Science.pdf', u:'https://courses.cognitiveclass.ai/certificates/5a95582dbaa147f3a17ce4005f78d614'}
];

/* ISI PAPAN TULIS DOBOT */
var INFO = [
  {l:'NAMA', v:[SITE.name]},
  {l:'PROGRAM STUDI', v:['Mechatronics & Artificial Intelligence']},
  {l:'KAMPUS', v:['Universitas Pendidikan Indonesia']},
  {l:'SEMESTER', v:['5 (Five)']},
  {l:'FOKUS', v:['Robotics, IoT, Interaction design']},
  {l:'KOTA', v:['Jakarta Pusat']}
];
