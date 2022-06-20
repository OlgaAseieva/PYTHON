from product import Product
from buyer import Buyer
from oder import Oder
import datetime

dish_1 = Product('salad', 250, 180)
dish_2 = Product('soup', 300, 140)
dish_3 = Product('meat_ch', 300, 220)
dish_4 = Product('steak', 400, 340)

buyer_1 = Buyer('Olha', 'As', 'o678945')
buyer_2 = Buyer('Georg', 'F', 'o508945')
buyer_3 = Buyer('Musay', 'G', 'o678345')

print(buyer_1, buyer_2, buyer_3, sep='\n')
print('\n', dish_1, dish_2, dish_3, dish_4, sep='\n')

oder_1 = Oder(buyer_1)
oder_1.add_cart(dish_1, 2)
oder_1.add_cart(dish_2, 1)

print(''.join(map(str, oder_1)))

