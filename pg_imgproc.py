from imgproc import FSImageProcessing

img = FSImageProcessing('img/cat_high_res.png')

img.gray(0.0)
img.gray(0.5)
img.gray(1.0)
img.gray(1.5)
img.gray(2.0)

img.brighten(0.0)
img.brighten(0.5)
img.brighten(1.0)
img.brighten(1.5)
img.brighten(2.0)

img.show_image()
