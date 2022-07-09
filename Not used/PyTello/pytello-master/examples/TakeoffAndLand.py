from pytello.Tello import Tello

tello = Tello(video=True)

Connection = tello.connect()

if (Connection):
    print(" Connected! ")
    while True:
        tello.get_frame_read().frame
else:
    print(" Not Connected! ")