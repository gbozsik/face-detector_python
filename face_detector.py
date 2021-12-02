import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('rossi_hamy.jpg')
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# for rectangle in face_coordinates:
#     (x, y, width, height) = rectangle
#     cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)



webcam = cv2.VideoCapture(0)
while True:
    successful_frame, frame = webcam.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    cv2.imshow('face detector', grayscale_img)
    cv2.waitKey(1)


print(face_coordinates)

cv2.imshow('Rossi: ', img)
cv2.waitKey()



print('hali')
