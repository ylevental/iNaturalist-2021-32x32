from torchvision import datasets, transforms
import numpy as np
from PIL import Image
from os import path, makedirs

dataset = datasets.ImageFolder('./datatrain', transform = transforms.Resize((32,32)))

images = [];
labels = [];

for i, (data, data1) in enumerate(zip(dataset, dataset.imgs)): # i == Index
   image, label = data
   datatmp = str(data1[0])
   datatmp = datatmp[:27] + '_copy' + datatmp[27:]
   image = np.array(image)
   img = Image.fromarray(image, "RGB")
   #print(datatmp)
   dir = path.dirname(path.abspath(datatmp))
   if not path.isdir(dir):
        makedirs(dir)
   img.save(datatmp)
   if i%1000 == 0:
      print(i)
