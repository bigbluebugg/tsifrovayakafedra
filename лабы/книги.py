# TODO Найдите количество книг, которое можно разместить на дискете
disket_space = 1.44 * 1024 * 1024
book = 100*50*25*4
s= disket_space // book
print("Количество книг, помещающихся на дискету:", int(s))
