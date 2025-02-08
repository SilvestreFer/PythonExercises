from time import sleep
import emoji

for c in range(10,0,-1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks::sparkler:")*11)
print(emoji.emojize('I :red_heart: Python :smiling_face_with_hearts:'))