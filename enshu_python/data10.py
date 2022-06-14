text = 'remon cherry apple'
splitted = text.split()
print(splitted)

text = 'remon:cherry:apple'
splitted = text.split(':')
print(splitted)

text = 'remon:cherry:apple'
fruit1,fruit2,fruit3 = text.split(':')
print(fruit2)

#from PIL import Image
#image = Image.open('flower.jpg')
#red,green,blue = image.split()
#convert_image = Image.merge('RGB',(blue,green,red))
#convert_image.show()
#convert_image.save('rgb_to_bgr.jpg')

#from PIL import Image
#image = Image.open('flower.jpg')
#black_and_white = image.convert('L')
#black_and_white.show()
#black_and_white.save('b_and_w.jpg')

from PIL import Image
image = Image.open('flower.jpg')
image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('ROTATE_90.jpg')  #transpose=転置(置き場所を変える)
