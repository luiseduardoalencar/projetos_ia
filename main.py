import cv2
import time 
import numpy as np 

Colors = [(0,255,255), (255,255,0), (0,255,0), (255,0,0)]

class_name = []
with open("coco.names", "r") as f :
    class_name = [cname.strip() for cname in f.readlines()]

#cap = cv2.VideoCapture("walking.mp4")
cap = cv2.VideoCapture(0)

net =  cv2.dnn.readNet("yolov4-tiny.weights","yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale= 1/255)

while True:
    _, frame =cap.read()
    #start e end é para calcular o fps
    start = time.time()
    classes, scores, boxes = model.detect (frame,0.1,0.2) #mudar o pesos para melhorar a rede 
    end =time.time()
    for(classid,scores,box) in zip(classes,scores,boxes):
        color = Colors[int(classid) % len(Colors)]
        label = f"{class_name[int (classid)]} : {scores:.2f}" #pega o id para classificar o tipo e o score é o a certeza que o modelo tem de que ta certo 
        cv2.rectangle(frame, box , color, 2)
        cv2.putText(frame,label,(box[0],box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    fps = 1 / (end - start) #calculo do fps
    fps_label = f"FPS: {fps:.2f}"
    
    cv2.putText(frame,fps_label,(0,25), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5 )
    cv2.putText(frame,fps_label,(0,25), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3 )

    cv2.imshow("detections", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
