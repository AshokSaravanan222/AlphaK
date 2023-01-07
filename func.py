import cv2
import numpy as np
import tensorflow as tf
import pytesseract


def detect_box(image, line_min_width=15):
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th1, img_bin = cv2.threshold(gray_scale, 230, 255, cv2.THRESH_BINARY)
    kernal6h = np.ones((1, line_min_width), np.uint8)
    kernal6v = np.ones((line_min_width, 1), np.uint8)
    img_bin_h = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal6h)
    img_bin_v = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal6v)
    img_bin_final = img_bin_h | img_bin_v
    final_kernel = np.ones((3, 3), np.uint8)
    img_bin_final = cv2.dilate(img_bin_final, final_kernel, iterations=1)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    return stats, labels


def detect_table(img):
    stats, labels = detect_box(img)
    # cc_out = imshow_components(labels)
    a = []
    b = []
    c = []
    d = []
    e = []
    for x, y, w, h, area in stats[2:]:
        if 125 <= area <= 2000 and h > 10:
            a.append([x, y, w, h, area])
            # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
        else:
            if 10 <= area <= 2000 and h > 1 and 15 < w < 20:
                d.append([x, y, w, h, area])
    for i in range(5):
        temp1 = []
        temp2 = []
        counter = 0
        for j in range(len(a)):
            temp1.append(a[j][i])
        temp1.sort()
        for k in range(len(temp1)):
            if k != (len(temp1) - 1):
                if (temp1[k + 1] - temp1[k]) > 10:
                    temp2.append(temp1[counter:k + 1])
                    counter = k + 1
        temp2.append(temp1[counter:len(temp1)])
        b.append(temp2)
    for m in range(len(b[1])):
        temp3 = []
        for n in range(len(a)):
            if a[n][1] in b[1][m]:
                temp3.append(a[n])
        temp3.sort()
        c.append(temp3)

    for p in range(len(c)):
        if p != 0:
            for q in range(len(d)):
                if d[q][1] - c[p][0][1] <= 2:
                    d[q][3] = c[p][0][3]
                    x, y, w, h = d[q][0], d[q][1], d[q][2], d[q][3]
                    for r in d:
                        if r != d[q]:
                            if y < r[1] < (y + h) and abs(r[0] - x) < 3:
                                e.append(r)
                else:
                    d[q][3] = c[p][0][3]
                    x, y, w, h = d[q][0], d[q][1], d[q][2], d[q][3]
                    for r in d:
                        if r != d[q]:
                            if y < r[1] < (y + h) and abs(r[0] - x) < 3:
                                e.append(r)
    for s in d:
        if s in e:
            d.remove(s)

    for t in range(len(c)):
        if t != 0:
            for u in range(len(d)):
                if abs(d[u][1] - c[t][0][1]) <= 5:
                    c[t].append(d[u])
                    c[t].sort()
    return c, d


def print_boxes(box, img):
    try:
        test = box[0][0][1]
    except:
        for i in box:
            x, y, w, h = i[0], i[1], i[2], i[3]
            cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 1)
    else:
        for i in box:
            for j in i:
                x, y, w, h = j[0], j[1], j[2], j[3]
                cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 1)
    return img


def adjust_box(bounding, img):
    x, y, w, h = bounding[0], bounding[1], bounding[2], bounding[3]
    img = img[y:y + h, x:x + w]
    img = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    if w > h:
        a = w - h
        img = cv2.copyMakeBorder(img, int(a / 2), round(a / 2), 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    else:
        a = h - w
        img = cv2.copyMakeBorder(img, 0, 0, int(a / 2), round(a / 2), cv2.BORDER_CONSTANT, value=(255, 255, 255))
    img = cv2.resize(img, (28, 28))
    return img


# returns a tuple (first_name, last_name, ID)
def name(image):
    hImg, wImg, _ = image.shape
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if x + w <= (wImg / 32) * 15 and y + h <= (hImg / 4) and w * h > 600:
            temp1.append(y)
            temp2.append([x, y, w, h])
    temp1.sort()
    temp1 = temp1[2:]
    for i in range(len(temp2)):
        if temp2[i][1] in temp1:
            temp3.append(temp2[i])
    for i in temp3:
        x, y, w, h = int(i[0]), int(i[1]), int(i[2]), int(i[3])
        img = image[y:y + h, x:x + w]
        boxes = pytesseract.image_to_data(img)
        for a, b in enumerate(boxes.splitlines()):
            if a != 0:
                b = b.split()
                if len(b) == 12:
                    temp4.append([y, x, b[11]])
    temp4.sort()
    if temp4[0][1] > temp4[1][1]:
        temp4.append(temp4[1][2])
        temp4.append(temp4[0][2])
    else:
        temp4.append(temp4[0][2])
        temp4.append(temp4[1][2])
    temp4.append(temp4[2][2])
    temp4 = temp4[3:]
    return temp4


# returns the date of a certain area of an image
def date(bounding, image):
    firstList = []
    thirdList = []
    dayList = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    x, y, w, h = int(bounding[0]), int(bounding[1]), int(bounding[2]), int(bounding[3])
    image = image[y:y + h, x:x + w]
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    blur = cv2.GaussianBlur(image, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        IMAGE = image[y:y + h, x:x + w]
        firstList.append(str(pytesseract.image_to_string(IMAGE, config='--psm 7')))
    second = str(pytesseract.image_to_string(image))
    for a in range(len(firstList)):
        firstList[a] = firstList[a].split("\x0c")[0]
        firstList[a] = firstList[a].split("\n")[0]
    second = second.split("\x0c")[0]
    second = second.split("\n")[0]
    secondList = second.split()

    if len(secondList) != 0:
        if len(firstList[0]) > len(secondList[0]):
            thirdList.append(firstList[0])
        else:
            thirdList.append(secondList[0])

        if firstList[1].lower() in dayList:
            thirdList.append(firstList[1])
        elif secondList[1].lower() in dayList:
            thirdList.append(secondList)
        else:
            for b in dayList:
                if secondList[1][0].lower() == b[0]:
                    if len(secondList[1]) == 3:
                        if secondList[1][1] == b[1]:
                            thirdList.append(b.title())
                    else:
                        thirdList.append(b.title())
        date = str(thirdList[0]) + ' ' + str(thirdList[1])
    else:
        date = ''
    return date


def resize(box, image):
    x, y, w, h = box[0], box[1], box[2], box[3]
    image = image[y:y + h, x:x + w]
    return image


def area(image):
    areaList = []
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    dilate = cv2.copyMakeBorder(dilate, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        areaList.append(w * h)
    return areaList[0]


def time(img, model):
    format_list = []
    hImg, wImg, _ = img.shape
    img = cv2.resize(img, (2 * wImg, 2 * hImg))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        image = adjust_box([x, y, w, h], img)

        thresh = 215  # normally 215
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] >= thresh:
                    image[i][j] = 255
                else:
                    image[i][j] = int(thresh * (image[i][j] / 255))
        image = cv2.bitwise_not(image)
        image = np.reshape(image, (1, 28, 28))
        prediction = model.predict(image)
        prediction = np.argmax(prediction)
        format_list.append([x, prediction])
    result = ''
    format_list.sort()
    for num in format_list:
        result += str(num[1])
    return result


def score(image, model):
    thresh = 215  # normally 215
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] >= thresh:
                image[i][j] = 255
            else:
                image[i][j] = int(thresh * (image[i][j] / 255))

    image = cv2.bitwise_not(image)
    image = np.reshape(image, (1, 28, 28))
    prediction = model.predict(image)
    prediction = np.argmax(prediction)
    prediction += 6
    return prediction
