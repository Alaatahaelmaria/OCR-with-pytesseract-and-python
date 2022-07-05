#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"F:\Downloads\tesseract.exe"
img = cv2.imread("C:\\Users\\FreeComp\\Desktop\\font example.jpg")
img = cv2.resize(img, (400, 450))
cv2.imshow("Image", img)
text = pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




