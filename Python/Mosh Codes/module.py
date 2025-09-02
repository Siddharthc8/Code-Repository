import converters        # command to import module
import utils
import package_ecommerce.shipping
from converters import kgs_to_lbs, lbs_to_kgs
from package_ecommerce import shipping

print(kgs_to_lbs(100))
print(converters.kgs_to_lbs(100))

numbers = [1, 5, 2, 5, 7, 10, 35, 64, 1]
print(utils.find_max(numbers))

shipping.shipping_cost()

