import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# img = cv2.imread('rossi.jpg')
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#
# for rectangle in face_coordinates:
#     (x, y, width, height) = rectangle
#     cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)

# print(face_coordinates)

# cv2.imshow('Rossi: ', img)
# cv2.waitKey()


webcam = cv2.VideoCapture(0)
while True:
    successful_frame, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, width, height) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow('face detector', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

webcam.release()





