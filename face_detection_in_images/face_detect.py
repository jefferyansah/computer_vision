
#This experiment was built by resuing and modifying code from

#https://github.com/shantnu/FaceDetect/blob/master/face_detect.py
#import dependencies
import cv2,  sys,  glob,  os


#join path of cwd to image location path
dirname = os.path.dirname(__file__) 
image_location = os.path.join(dirname,  'image_repo')


# Now lets create the Haar Cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#Read the Images in the image for folder and detect faces
for item in glob.glob( image_location +  "/*.*"):
    
    #read the image
    image= cv2.imread(item)

    #Convert the image to gray scale
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray_scale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    print("Found {0} faces!".format(len(faces)))

    #Add a bounding box to images
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow("Faces found", image)
    #press any key to view the next image
    cv2.waitKey(0)
    

