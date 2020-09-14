import cv2
def read():
    image = cv2.imread('kamran1.png')
    image1 = cv2.resize(image,(70,50))
    cv2.imwrite('kam.jpg', image1)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    return image1
char = ['@','#','$','&','+','(',')','^']
def conver(image):
    l = [0 for i in range(0,255)]
    f = open('kamran','w')
    for i in image:
        print(len(i))
        for j in i:
            l[j] = l[j]+1

    for i in image:
        st = ""
        for j in i:
           st = st +char[j//32]
        f.write(st+'\n')

    print(l)
if __name__ == '__main__':
    conver(read())