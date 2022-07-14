# this code will count or show the locations of all the faces in a pic
import face_recognition

image=face_recognition.load_image_file('./groups/team2.jpg')
face_locations=face_recognition.face_locations(image)

# a=[1,2,3,4]
# print(len(a))

#array of co ordinates of each face
# print(face_locations)

print(f'There are {len(face_locations)} people in this image.')