from PIL import Image, ImageFilter

# 打开一个jpg图像文件，如果不加盘符是当前路径:
image = Image.open('D:/test/uploud/1/1/15435636727107260.jpg')
# 获得图像尺寸（宽、高）:
w, h = im.size
print('print image size: %sx%s' % (w, h))

# 处理图片应用模糊滤镜:
image2 = image.filter(ImageFilter.BLUR)
# 将缩放的图片采用jpeg进行保存:
image.save('D:/test/uploud/1/1/blur.jpg', 'jpe   g')