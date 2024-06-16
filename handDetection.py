import cv2
from cvzone.HandTrackingModule import HandDetector
from music_controller.music_controller import MusicControll
import time

MUSICLIST = ['music_1.mp3', 'music_2.mp3', 'music_3.mp3']
music = MusicControll(MUSICLIST)

last_executed = {
    'stop': 0,
    'start': 0,
    'next': 0,
    'previous': 0
}
delay = 2  

def get_2D_dist(vec1, vec2):
    vec1_x = vec1[0]
    vec1_y = vec1[1]
    vec2_x = vec2[0]
    vec2_y = vec2[1]

    dist = (((vec1_x - vec2_x) ** 2) + ((vec1_y - vec2_y) ** 2)) ** (1 / 2)
    return dist

def isPinch(dist):
    return dist < 35

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
Status = "STOPPED"

while True:


    ret, frame = cap.read()
    hands, frame = detector.findHands(frame)

    cv2.putText(frame, Status, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
    
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

        current_time = time.time()

        if isPinch(dist_1) and (current_time - last_executed['stop'] > delay):
            music.music_stop()
            last_executed['stop'] = current_time
            Status = "PAUSE"
            

        if isPinch(dist_2) and (current_time - last_executed['start'] > delay):
            music.music_start()
            last_executed['start'] = current_time
            Status = "PLAY"

        if isPinch(dist_3) and (current_time - last_executed['next'] > delay):
            music.next_song()
            last_executed['next'] = current_time
            Status = "NEXT"

        if isPinch(dist_4) and (current_time - last_executed['previous'] > delay):
            music.previous_song()
            last_executed['previous'] = current_time
            Status = "BACK"

    except IndexError:
        # hands not found
        # print("ERR: hands not found")
        pass

    if not ret:
        break

    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



