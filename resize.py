#!/usr/bin/env python3

import os, glob, cv2

preprocess_path = 'preprocess/'
postprocess_path = 'postprocess/'
types = ( '*.png','*.jpg','*.jpeg')
i=1
dim = (416, 416)#W H

for ext in types:
    for infile in glob.glob( os.path.join(preprocess_path, ext )):
        img = cv2.imread(infile, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(str(postprocess_path)+"gbr"+str(i)+".jpg", resized)
        print('Ori Path:', infile, ' Ori Dim:', img.shape, 'Res Dim: ', resized.shape, 'Res Path:', str(postprocess_path)+"gbr"+str(i)+".jpg")
        i=i+1
