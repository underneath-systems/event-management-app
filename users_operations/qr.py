import qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def create_qr(event, id):
    img = qrcode.make(id)
    file_save = "media/media/invitations/" + str(id) + "_" + event + "_invitation.png"
    path = "media/invitations/" + str(id) + "_" + event + "_invitation.png"
    aux = open(file_save, "wb")
    img.save(aux)
    aux.close()
    return path


def barcodeReader(image, bgr):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)

    for decodedObject in barcodes:
        points = decodedObject.polygon

        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

    for bc in barcodes:
        cv2.putText(image, bc.data.decode("utf-8") + " - " + bc.type, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    bgr, 2)

        return int(bc.data.decode("utf-8"))


def read_qr():
    bgr = (8, 70, 208)
    cap = cv2.VideoCapture(0)
    while (True):
        ret, frame = cap.read()
        barcode = barcodeReader(frame, bgr)
        cv2.imshow('Barcode reader', frame)
        if barcode is not None:
            #a = barcode.data.decode("utf-8")
            #print(barcode)
            break
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
    cv2.destroyAllWindows()
    return barcode



#create_qr("Othello", 15)

"""image = cv2.imread("15_Othello_invitation.png")

read_qr(image)

delete_tmp("15_Othello_invitation.png")"""

