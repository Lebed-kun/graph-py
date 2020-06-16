from utils import Set

def test_product():
    set1 = {1, 2}
    set2 = {'a', 'b', 'c'}

    product = Set.product(set1, set2)

    print("Set 1: ", set1)
    print("Set 2: ", set2)
    print("Cartesian product: ", product)

test_product()