import cv2

# print('hello  opencv', cv2.__version__)
 

src = cv2.imread('images/cat.bmp', cv2.IMREAD_COLOR )
logo = cv2.imread('images/logo.png',cv2.IMREAD_UNCHANGED)

mask = logo[:,:,3]
logo = logo[:,:,:-1]
h,w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]

cv2.copyTo(logo,mask,crop)

# dst[mask > 0] = src[mask > 0]
cv2.imshow('logo', src)
cv2.waitKey()
cv2.destroyAllWindows()

