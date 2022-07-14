# this code identifies all the people in a code out of the images it has and labels them
import face_recognition
from PIL import Image, ImageDraw

bill_image=face_recognition.load_image_file('./known/Bill Gates.jpg')
bill_face_encoding=face_recognition.face_encodings(bill_image)[0]

steve_image=face_recognition.load_image_file('./known/Steve Jobs.jpg')
steve_face_encoding=face_recognition.face_encodings(steve_image)[0]

# Create an array of encodings and names
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs"
]

#Load test images to find faces in
test_image=face_recognition.load_image_file('groups/bill-steve-elon.jpg')

#Find faces in test image
face_locations=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image, face_locations)

#Convert to PIL format
pil_image=Image.fromarray(test_image)

#create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right , bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)

    name="Unknown person"

    #If match
    if True in matches:
        match_index=matches.index(True)
        name=known_face_names[match_index]

    #draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    #draw Label
    text_width, text_height = draw.textsize(name)
    draw. rectangle(((left, bottom - text_height -10), (right, bottom)), fill = (0,0,0), outline=(0,0,0))

    draw.text((left+6, bottom-text_height-5), name, fill=(255,255,255,255))

del draw

#display image
pil_image.show()