from arboles import BinarySearchtree

abb=BinarySearchtree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(15)
abb.insert(23)
abb.insert(110)
abb.insert(90)
abb.insert(120)
abb.insert(100)
abb.insert(55)
abb.insert(58)
abb.insert(115)
abb.transversal()
abb.remove(58)
abb.transversal()

abb.remove(90)
abb.transversal()
"""
abb.transversal("posorden")
res=abb.search(35)
print(f"el resultado es{res}")
abb.remove(25)
abb.transversal("preorden")
"""
