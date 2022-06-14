from PIL import Image
image = Image.open('flower.jpg')
red,green,blue = image.split()
convert_image = Image.merge('RGB',(red,blue,green))
convert_image.show()
convert_image.save('kadai10.jpg')
