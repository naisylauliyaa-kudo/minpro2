# ------------------ DATABASE USER ------------------
users = {
    "admin": {"password": "naisyla", "role": "bos"},
    "user": {"password": "bayu", "role": "pengguna"}
}
# ------------------ DATABASE BENCANA ------------------
bencana = {
    1: {
        "nama": "Gempa bumi",
        "deskripsi": "Gempa bumi adalah getaran atau guncangan pada permukaan bumi yang disebabkan oleh pelepasan energi secara tiba-tiba di dalam bumi.",
        "tips": [
            "Lindungi kepala dan badan Anda dari reruntuhan bangunan",
            "Berlari keluar apabila masih dapat dilakukan",
            "Cari tempat yang paling aman dari goncangan",
            "Jauhi bangunan, pohon besar, dan tiang listrik"
        ],
        "kontak": "119"
    },
    2: {
        "nama": "Tsunami",
        "deskripsi": "Tsunami adalah gelombang air besar akibat gangguan di dasar laut, seperti gempa bumi atau letusan gunung berapi.",
        "tips": [
            "Segera evakuasi ke tempat tinggi atau aman",
            "Jauhi pantai setelah terjadi goncangan",
            "Hindari jembatan atau bangunan rapuh",
            "Dengarkan informasi resmi dari BMKG"
        ],
        "kontak": "115"
    },
    3: {
        "nama" : "Letusan vulkanik",
        "deskripsi": "Letusan gunung berapi merupakan peristiwa yang terjadi akibat magma di dalam perut bumi yang keluar oleh gas yang bertekanan tinggi. Peristiwa ini berhubungan dengan naiknya magma putih dari dalam perut bumi.",
        "tips": [
              "Gunakan pakaian tertutup untuk melindungi kulit",
              "Gunakan masker dan kacamata pelindung.",
              "Hindari daerah aliran sungai, karena bisa dilalui lahar.",
              "Ikuti jalur evakuasi resmi."
          ],
          "kontak": "12345"
    },
    4: {
        "nama": "Badai topan",
        "deskripsi": "Badai topan adalah angin puting beliung berskala besar dengan kecepatan tinggi, biasanya di atas 120 km/jam, yang terjadi di wilayah tropis di antara garis balik utara dan selatan.",
        "tips": [
            "Tetap di dalam rumah atau bangunan yang kokoh, jauh dari jendela.",
            "Matikan listrik jika ada genangan air untuk menghindari korslet.",
            "Jika rumah tidak aman, segera pindah ke tempat evakuasi yang disediakan",
            "Jangan keluar rumah sebelum pihak berwenang menyatakan aman."
        ],    
        "kontak": "96868"
    }   
}

# ------------------ LOGIN SYSTEM ------------------
kesempatan = 3
role = None  

print("===== Sistem Panduan Keselamatan Bencana Alam =====")

def login():
    kesempatan = 3
    while kesempatan > 0:
        try:
            username = input("Masukkan username Anda: ")
            password = input("Masukkan password Anda: ")

            if username in users and users[username]["password"] == password:
                print("Login berhasil ")
                return users[username]["role"]  
            else:
                kesempatan -= 1
                print("Login gagal, username atau password salah")
                if kesempatan == 0:
                    print("Kesempatan Anda habis ")
                    return None
        except Exception as e:
            print(f"Terjadi error: {e}")
            kesempatan -= 1

# ------------------ MENU MANAGER ------------------
def menu_manager():
    while True:
        try:
            print("\n=== MENU UTAMA MANAGER ===")
            print("1. Tambah Bencana")
            print("2. Update Bencana")
            print("3. Hapus Bencana")
            print("4. Lihat Semua Bencana")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tambah_bencana()
            elif pilihan == "2":
                update_bencana()
            elif pilihan == "3":
                hapus_bencana()
            elif pilihan == "4":
                lihat_bencana()
            elif pilihan == "5":
                print("Keluar dari sistem Manager")
                break
            else:
                print("Pilihan tidak valid!")
        except KeyboardInterrupt:
            print("\nJangan tekan CTRL + C!")
        except EOFError:
            print("\nJangan tekan CTRL + Z!")

# ------------------ CRUD ------------------
def tambah_bencana():
    id_baru = max(bencana.keys()) + 1
    nama = input("Masukkan nama bencana: ")
    deskripsi = input("Masukkan deskripsi: ")
    
    tips = []
    print("Masukkan tips (ketik 'done' jika selesai):")
    while True:
        tip = input(f"Tips ke-{len(tips)+1}: ")
        if tip.lower() == "done":
            break
        if tip.strip() != "":
            tips.append(tip)
    
    kontak = input("Masukkan nomor darurat: ")
    bencana[id_baru] = {
        "nama": nama,
        "deskripsi": deskripsi,
        "tips": tips,
        "kontak": kontak
    }
    print("Data bencana berhasil ditambahkan!")


def update_bencana():
    lihat_bencana()
    try:
        id_update = int(input("Masukkan nomor bencana yang ingin diupdate: "))
        if id_update in bencana:
            bencana[id_update]["nama"] = input("Nama baru: ")
            bencana[id_update]["deskripsi"] = input("Deskripsi baru: ")
            bencana[id_update]["tips"] = input("Masukkan tips baru (pisahkan dengan koma): ").split(",")
            bencana[id_update]["kontak"] = input("Nomor darurat baru: ")
            print("Data bencana berhasil diperbarui!")
        else:
            print("nomor tersebut tidak ditemukan!")
    except ValueError:
        print("Input Harus Berupa Angka")
    except KeyboardInterrupt:
        print("Jangan tekan CTRL + C!")
    except EOFError:
        print("Jangan tekan CTRL + Z!")


def hapus_bencana():
    lihat_bencana()
    try:
        id_hapus = int(input("Masukkan nomor bencana yang ingin dihapus: "))
        if id_hapus in bencana:
            del bencana[id_hapus]
            print("Data bencana berhasil dihapus!")
        else:
            print("nomor tersebut tidak ditemukan!")
    except ValueError:
        print("Input Harus Berupa Angka")
    except KeyboardInterrupt:
        print("Jangan tekan CTRL + C!")
    except EOFError:
        print("Jangan tekan CTRL + Z!")

def lihat_bencana():
    print("\n=== Database Bencana Alam ===")
    for id_bencana, data in bencana.items():
        print(f"{id_bencana}. {data['nama']} - {data['deskripsi']}")


# ------------------ MENU KARYAWAN ------------------
def menu_karyawan():
    while True:
        try:
            print("\n=== MENU KARYAWAN ===")
            print("1. Lihat Nama Bencana")
            print("2. Lihat Deskripsi Bencana")
            print("3. Lihat Tips Bencana")
            print("4. Lihat Nomor Darurat")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                for id_bencana, data in bencana.items():
                    print(f"{id_bencana}. {data['nama']}")


            elif pilihan == "2":
                print("\nDaftar Bencana:")
                for id_bencana, data in bencana.items():
                    print(f"{id_bencana}. {data['nama']}")
                try:
                    id_b = int(input("Masukkan nomor bencana untuk lihat deskripsi: "))
                    if id_b in bencana:
                        print(f"\nDeskripsi {bencana[id_b]['nama']}:")
                        print(bencana[id_b]["deskripsi"])
                    else:
                        print("nomor tersebut tidak ditemukan!")
                except ValueError:
                    print("Input Harus Berupa Angka")


            elif pilihan == "3":
                print("\nDaftar Bencana:")
                for id_bencana, data in bencana.items():
                    print(f"{id_bencana}. {data['nama']}")
                try:
                    id_b = int(input("Masukkan nomor bencana untuk lihat tips: "))
                    if id_b in bencana:
                        print(f"\nTips {bencana[id_b]['nama']}:")
                        for i, t in enumerate(bencana[id_b]["tips"], start=1):
                            print(f"{i}. {t}")
                    else:
                        print("nomor tersebut tidak ditemukan!")
                except ValueError:
                    print("Input Harus Berupa Angka")


            elif pilihan == "4":
                print("\nDaftar Bencana:")
                for id_bencana, data in bencana.items():
                    print(f"{id_bencana}. {data['nama']}")
                try:
                    id_b = int(input("Masukkan nomor bencana untuk lihat nomor darurat: "))
                    if id_b in bencana:
                        print(f"\nNomor darurat {bencana[id_b]['nama']}: {bencana[id_b]['kontak']}")
                    else:
                        print("nomor tidak ditemukan!")
                except ValueError:
                    print("Input Harus Berupa Angka")


            elif pilihan == "5":
                print("Keluar dari sistem Karyawan")
                break
            else:
                print("Pilihan tidak valid!")
        except KeyboardInterrupt:
            print("\nJangan tekan CTRL + C!")
        except EOFError:
            print("\nJangan tekan CTRL + Z!")


# ------------------ MAIN ------------------
role = login()  

if role == "bos":
    menu_manager()
elif role == "pengguna":
    menu_karyawan()
