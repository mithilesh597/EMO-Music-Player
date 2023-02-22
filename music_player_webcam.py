
import time
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 5

classifier = cv2.CascadeClassifier('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/haarcascade_frontalface_alt.xml')
global text
webcam = cv2.VideoCapture(0)  
now = time.time()
future = now + 20  
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  
    
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    
    faces = classifier.detectMultiScale(mini)
    
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  
        text = text.title()  
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Happy':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)
			
	   
        if text == 'Surprised':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == 'Sad':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)
		
        if text == 'Drowsy':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255) , 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)			
			
    
    cv2.imshow('Music player with Emotion recognition', im)
    key = cv2.waitKey(30)& 0xff
    if time.time() > future:
        try:
            cv2.destroyAllWindows()
            mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
            if text == 'Angry':
                randomfile = random.choice(os.listdir("C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/angry/"))
                print('Emotion detected angry :' + randomfile)
                file = ('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/angry/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Happy':
                randomfile = random.choice(os.listdir("C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/happy/"))
                print('Emotion detected happy ' + randomfile)
                file = ('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/happy/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Surprised':
                randomfile = random.choice(os.listdir("C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/surprised/"))
                print('Emotion detected Surprised ' + randomfile)
                file = ('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/surprised/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Sad':
                randomfile = random.choice(os.listdir("C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/sad/"))
                print('Emotion detected Sad ' + randomfile)
                file = ('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/sad/' + randomfile)
                subprocess.call([mp, file])
			
            if text == 'Drowsy':
                randomfile = random.choice(os.listdir("C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/drowsy/"))
                print('Emotion detected drowsy ' + randomfile)
                file = ('C:/Users/1/Desktop/Music_player_with_Emotions_recognition-master/songs/drowsy/' + randomfile)
                subprocess.call([mp, file])
            break

        except :
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break

    if key == 27:  # The Esc key
        break