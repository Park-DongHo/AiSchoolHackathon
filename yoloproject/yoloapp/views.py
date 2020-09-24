from django.shortcuts import render
from .models import BookList, PetList
from .models import Walk

# Create your views here.
def home(request):

    return render(request, 'home.html')

def result(request):
    # Yolo 로드
    # net = cv2.dnn.readNet("yolov4.weights", "yolov4-obj.cfg")
    # classes = []
    # with open("objects.names", "r") as f:
    #     classes = [line.strip() for line in f.readlines()]    # strip : 공백제거
    # print(len(classes))       # 7
    # print(classes)

    # layer_names = net.getLayerNames()
    # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    # colors = np.random.uniform(0, 255, size=(len(classes), 3))
    # print(colors)

    # 이미지 가져오기
    # img = cv2.imread("test_data/sample10.jpg")
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)
    # height, width, channels = img.shape

    # Detecting objects
    # blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    # net.setInput(blob)
    # outs = net.forward(output_layers)

    # 정보를 화면에 표시
    # class_ids = []
    # confidences = []
    # boxes = []
    # for out in outs:
    #     for detection in out:
    #         scores = detection[5:]
    #         class_id = np.argmax(scores)
    #         confidence = scores[class_id]
            
    #         if confidence > 0.5:
    #             # Object detected
    #             center_x = int(detection[0] * width)
    #             center_y = int(detection[1] * height)
    #             w = int(detection[2] * width)
    #             h = int(detection[3] * height)
    #             # 좌표
    #             x = int(center_x - w / 2)
    #             y = int(center_y - h / 2)
    #             boxes.append([x, y, w, h])
    #             confidences.append(float(confidence))
    #             class_ids.append(class_id)

    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # font = cv2.FONT_HERSHEY_PLAIN
    # for i in range(len(boxes)):
    #     if i in indexes:
    #         x, y, w, h = boxes[i]
    #         label = str(classes[class_ids[i]])
    #         color = colors[class_ids[i]]
    #         cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    #         cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return render(request, 'result.html')

def book(request):
    BookList_obj=BookList.objects.all().values()
    
    context = {
        'BookList': BookList_obj
    }
    return render(request, 'book.html', context)
    
def walk(request,category):
    cate ={
        1 : '광주',
        2 : '서울',
        3 : '대전',
        4 : '대구',
        5 : '경기도',
    }
    # 광주
    if category == 1:
        Walk_obj=Walk.objects.filter(adress__contains='광주')
        updown=[35.177519,126.811916]
    # # 서울
    elif category == 2:
        Walk_obj=Walk.objects.filter(adress__contains='서울')
        updown=[37.528546,126.862274]
    # # 대전
    elif category == 3:
        Walk_obj=Walk.objects.filter(adress__contains='대전')
        updown=[36.346429,127.381419]
    # # 대구
    elif category == 4:
        Walk_obj=Walk.objects.filter(adress__contains='대구')
        updown=[35.87810,128.59392]
    # # 경기도
    elif category == 5:
        Walk_obj=Walk.objects.filter(adress__contains='경기도')
        updown=[37.33385,126.850319]
    # print(walk_up)
    context={
        'walk_obj':Walk_obj,
        'cate' : cate[category],
        'up' : updown[0],
        'down' : updown[1]
    }

    return render(request, 'walk.html', context)

    
def pet(request):
    PetList_obj = PetList.objects.all().values()
    context = {
        'PetList': PetList_obj
    }
    return render(request, 'pet.html', context)

def products(request):
    return render(request, 'products.html')