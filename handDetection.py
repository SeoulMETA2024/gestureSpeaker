import cv2
from cvzone.HandTrackingModule import HandDetector
from music_controller.music_controller import MusicControll

musicList = ['music_1.mp3','music_2.mp3','music_3.mp3']
music = MusicControll(musicList)



def get_2D_dist(vec1,vec2):
    vec1_x = vec1[0]
    vec1_y = vec1[1]
    vec2_x = vec2[0]
    vec2_y = vec2[1]

    dist = (((vec1_x-vec2_x)**2)+((vec1_y-vec2_y)**2))**(1/2)

    return dist

def isPinch(dist):
    if dist < 35:
        return True

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1, detectionCon=0.8)
while True:
    ret, frame = cap.read()
    
    hands, frame = detector.findHands(frame)
    
    
    try:
        hand = hands[0]['lmList']
        thumb = hand[4]
        index_f = hand[8]
        mid_f = hand[12]
        ring_f = hand[16]
        little_f = hand[20]
        
        
        dist_1 = get_2D_dist(thumb, index_f)
        dist_2 = get_2D_dist(thumb, mid_f)
        dist_3 = get_2D_dist(thumb, ring_f)
        dist_4 = get_2D_dist(thumb, little_f)

        #print(dist_1)

        if isPinch(dist_1):
            music.music_stop()
            #print('Gesture1')
        
        if isPinch(dist_2):
            music.music_start()
            #print('Gesture2')
        
        if isPinch(dist_3):
            music.next_song()
            
            #print('Gesture3')

        if isPinch(dist_4):
            music.previous_song()
            #print('Gesture4')
        
        

    except:
        pass




    if not ret:
        break

    cv2.imshow('Webcam',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()




