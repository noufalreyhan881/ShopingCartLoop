'''

Program ini dibuat untuk simulasi Shoping list. Yang beroperasi untuk memasukan barang 
dan mengurangi barang dari Shoping cart tersebut, dan mengetahui total belanja.

'''


# KELAS BERIKUT INI DIGUNAKAN UNTUK MEMASUKAN INPUT BARANG DAN HARGA 
class CartItem :
    def __init__(self, name , price):
        self.name = name
        self.price = price

# KELAS BERIKUT INI DIGUNAKAN UNTUK OPERASI YANG AKAN DILAKUKAN SAAT INPUT DIMASUKAN , SAYA MERUBAH INPUT KEDALAM BENTUK LIST
class ShoppingCart :
    def __init__(self):
        self.items = []

# BERIKUT INI ADALAH CARA UNTUK MENAMBAHKAN BARANG KE LIST MENGGUNAKAN FUNGSI APPEND    
    def add_item (self,item):              
        self.items.append(item)

# BERIKUT INI ADALAH CARA UNTUK MENGHAPUS BARANG DARI LIST MENGGUNAKAN FUNSGI REMOVE    
    def remove_item (self,item):            
        self.items.remove(item)

# BERIKUT INI ADALAH CARA UNTUK MENGHITUNG TOTAL HARGA DI KERANJANG MENGGUNAKAN FOR LOOP, AGAR TERUS DIHITUNG SESUAI DENGAN JUMLAH BARANG DALAM KERANJANG

# CONTOHNYA: BARANG ADA 3, MAKA TOTAL AKAN DITAMBAHKAN SEBANYAK 3x    
    def calculate_total (self):             
        total = 0                           
        for item in self.items:
            total += item.price
        return total
    
# BERIKUT INI ADALAH CARA UNTUK MENAMPILKAN KONDISI KERANJANG BARANG SETELAH PROSES PENAMBAHAN DAN PENGURANGAN BARANG    
    def get_item_data(self):                                                   
        total_item = []
        
# BERIKUT INI ADALAH CARA UNTUK  MEMASUKAN INPUT BARANG YANG ADA DI LIST SELF.ITEM        
        for item in self.items:                                                
            total_item.append({"Nama":item.name, "Harga":item.price})
        return total_item

def main():
    cart = ShoppingCart()
    print ("Selamat Datang di Keranjang Belanja Toko Makmur!")

# CARA BERIKUT INI YAITU MENGGUNAKAN WHILE LOOP, AGAR TAMPILAN UTAMA INI KEMBALI DITAMPILKAN, SETELAH SELESAI MEMASUKAN INPUT 
    while True :                                                
        print ("\nMenu: ")                                      
        print ("1. Menambah Barang")
        print ("2. Menghapus Barang")
        print ("3. Tampilkan Barang yang ada di Keranjang")
        print ("4. Lihat Total Belanja")
        print ("5. Exit")
        choice = input ("Pilihan: ")

# PILIHAN 1 ADALAH CARA UNTUK MELAKUKAN INPUT BARANG DAN HARGA , LALU DIMASUKAN KE CART ITEM
        if choice == "1":                                                       
            nama = input ("Silahkan masukan nama barang: ")
            harga = int(input ("Silahkan masukan harga: "))
            item = CartItem (nama,harga)
            cart.add_item(item)
            print (f'Barang "{nama}" berhasil dimasukan kedalam keranjang.') 
        
# PILIHAN 2 ADALAH CARA UNTUK MELAKUKAN PENGHAPUSAN BARANG YANG TELAH DI INPUT SEBELUMNYA
        elif choice == "2":                                                             
            cart.get_item_data()
            item_name = input ("Silahkan masukan nama barang yang ingin di hapus: ")
            found_item = None
            for item in cart.items:
                if item.name == item_name:
                    found_item = item
                    break
            if found_item:
# BARANG YANG INGIN DIHAPUS AKAN DIMASUKAN KEDALAM FUNGSI REMOVE ITEM                
                cart.remove_item(found_item)                                                    
                print (f"Barang {item_name} berhasil dihapus dari keranjang belanja. \n")
            else :
                print (f"Barang {item_name} tidak ditemukan dalam keranjang belanja. \n")

# PILIHAN 3 ADALAH CARA UNTUK MEMERIKSA BARANG DI KERANJANG, DENGAN CARA MEMANGGIL FUNGSI GET ITEM DATA            
        elif choice == "3":                                                                     
            item_data = cart.get_item_data()                                                    
            print ("Barang yang ada di Keranjang:")                                                      
            for idx, item in enumerate(item_data):
                print(f"{idx}. {item['Nama']} - Rp {item['Harga']:.2f}")                        
                print()

# UNTUK MELIHAT TOTAL BELANJA, HARUS MEMANGGIL CALCULATE_TOTAL DI CLASS SHOPPINGCART 
        elif choice == "4":                                                         
            total = cart.calculate_total()
            print (total)
    
        elif choice == "5":  
            print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")                                          
# MEMASUKAN BREAK DI INPUT KE 5 UNTUK MENYELESAIKAN WHILE LOOP 
            break

        else :
            print ("Menu tidak valid. Silakan pilih Menu yang sudah disediakan.")

# BILA NAMA FILE YANG DIJALANKAN SAMA DENGAN MAIN , MAKA FUNGSI MAIN AKAN DI JALANKAN
if __name__ == "__main__":                                      
    main()
