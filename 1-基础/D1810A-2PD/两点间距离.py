class 坐标:
    def __init__(此,横,纵):
        此.x, 此.y = 横,纵

    def __repr__(i):  # 显示坐标; 例： print (坐标(1,1))
        print(
            "X="+i.x+" Y="+i.y)

def 计算(A:坐标,B:坐标):  # 这里用了py3.5+的type hint
    开方 = __import__('math').sqrt
    Δx = B.x - A.x
    Δy = B.y - A.y
    距离 = 开方(Δx**2+Δy**2)
    return 距离

def 解():
    p1,p2 = 坐标(1,2),坐标(5,7)
    结果 = 计算(p1,p2)
    print(p1)
    print(结果)

if __name__ == '__main__':
    解()
