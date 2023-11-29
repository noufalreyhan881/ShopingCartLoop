'''

UNIT TEST

'''


# MENGIMPORT UNITTEST AGAR DAPAT DIGUNAKAN DI FILE INI
import unittest                        
                                             
# DARI FILE NoufalRifata_app , IMPORT CLASS CartItem dan ShoppingCart agar dapat digunakan di file ini
from NoufalRifata_app import CartItem, ShoppingCart   


class TestShoppingCart(unittest.TestCase): 
    def test_add_item(self):
        cart = ShoppingCart()
# INPUT BARANG DISINI SECARA MANUAL,BUKAN MELALUI USER INPUT SAAT PROGRAM DIJALANKAN        
        item = CartItem("Product A", 30.0)                                           
        cart.add_item(item)
# MEMASTIKAN BAHWA PANJANG KARAKTER YANG ADA DI LIST cart.items = 1 , JIKA SAMA MAKA TESTING BERHASIL                                                                   
        self.assertEqual(len(cart.items), 1)                                          

    def test_remove_item(self):
        cart = ShoppingCart()
        item = CartItem("Product A", 30.0)
        cart.add_item(item)
# SETELAH MEMASUKAN PRODUK A KE LIST, LALU DI REMOVE DENGAN MEMANGGIL FUNGSI REMOVE_ITEM           
        cart.remove_item(item)                                                          
# SETELAH DIMASUKAN BARANG 1, DAN DI REMOVE 1 , MAKA JUMLAH BARANG DI KERANJANG BELANJA SEHARUSNYA = 0         
        self.assertEqual(len(cart.items), 0)                                            

    def test_calculate_total(self):                                                                                
        cart = ShoppingCart()
# MEMASUKAN BARANG DENGAN HARGA 30 DAN 20        
        item1 = CartItem("Product A", 30.0)                                             
        item2 = CartItem("Product B", 20.0)
        cart.add_item(item1)
        cart.add_item(item2)
        total = cart.calculate_total()
# MENGECEK APAKAH SETELAH DIMASUKAN BARANG SEHARGA 30 dan 20 HASILNYA 50?        
        self.assertEqual(total, 50.0)                                               
# KALAU 50 MAKA TESTING BERHASIL   
                                                                                   
if __name__ == '__main__':
    unittest.main()