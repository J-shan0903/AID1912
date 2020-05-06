from threading import Thread

def sprider():
    print('I am sprider man')

t_list = []

for i in range(5):
    t = Thread(target=sprider)
    t_list.append(t)
    t.start()


for t in t_list:
    t.join()