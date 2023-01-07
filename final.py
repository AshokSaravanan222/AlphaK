import func
import cv2
import tensorflow as tf

image_path = 'images/image2.jpg'
img = cv2.imread(image_path)

score_model = tf.keras.models.load_model('digits.model')  # loads model for digits 6-9
time_model = tf.keras.models.load_model('time.model')  # loads model for digits 0-9

master, dash = func.detect_table(img)
master = master[1:]


master2 = []
for a in range(len(master)):
    temp = []
    date = func.date(master[a][0], img)
    if len(date) > 0:
        temp.append(date)

        IMAGE = func.resize(master[a][5], img)
        temp.append(func.time(IMAGE, time_model))  # time

        score = ''
        for b in master[a][6:]:
            IMAGE = func.adjust_box(b, img)
            if b not in dash and func.area(IMAGE) > 120:
                score += str(func.score(IMAGE, score_model))
            else:
                score += '-'
        temp.append(score)
        master2.append(temp)

name_id = func.name(img)
print(f'Name: {name_id[0]} {name_id[1]}')
print(f'ID: {name_id[2]}')

for i in master2:
    print(f'Date: {i[0]}   Time: {i[1]}   Score: {i[2]}')
