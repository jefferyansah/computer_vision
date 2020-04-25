# Face Detection in Images


* Goal: Detect faces in photso.
The Haar Cascade Classifer (HCC) is used to detect faces in images.


* To use:
1. Install dependencies `cv2` by running the requirements.txt file
2. Load your images into the `image_repo` folder or use the existing images
3. Run the  'face_detect.py`
4. The scripts will run by :
*looking for images in the `image_repo`. 
*For every image the facial detection algorithm with try detect faces using the Haar Cascade Classifier.
* Once the image has been detected  a bounded box will be drawn around the facial region
* The Image will then appear on your screen with the bounding box
* Hit enter to see the next image.

NB: You can change the parameters in the HCC (Haar Cascade Classifer) to improve the detection accurary.


This experiment was built with inspiration from https://github.com/shantnu/FaceDetect/blob/master/face_detect.py. I modified the code to loop through images in the repo and 
run the HCC algorithm on those images.
