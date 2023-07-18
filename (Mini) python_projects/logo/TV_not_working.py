import png
import numpy

# PNG size = 250x250p
Arr = numpy.random.randint(1, 255, size=(255, 255))
Arr = numpy.random.randint(1, 255, size=(255, 255))
Arr = numpy.random.randint(1, 255, size=(255, 255))
Arr = numpy.random.randint(1, 255, size=(255, 255))
print(Arr)

f = open('wikilogo.png', 'wb')
w = png.Writer(255, 255, greyscale=True)
w.write(f, Arr) #[range(256)]
f.close()
