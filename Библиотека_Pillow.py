from PIL import Image

# Меняем размер изображения на новый.
# ozero = Image.open("Ozero.jpg")
# ozero = ozero.resize((200, 200))
# ozero.show()


ozero = Image.open("Ozero.jpg")
width, height = ozero.size
new_width = 500  # ширина
new_height = int(new_width * height / width)
ozero = ozero.resize((new_width, new_height))
ozero.show()



# ozero = Image.open("Ozero.jpg")
# width, height = ozero.size
# new_height = 100  # Высота
# new_width = int(new_height * width / height)
# ozero = ozero.resize((new_width, new_height))
# ozero.show()