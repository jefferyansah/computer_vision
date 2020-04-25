#%%
import cv2,  sys,  glob,  os

#%%
dirname = os.path.dirname(__file__) 
image_location = os.path.join(dirname,  'image_repo')


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

for item in glob.glob( image_location +  "/*.*"):
    
    image= cv2.imread(item)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    

