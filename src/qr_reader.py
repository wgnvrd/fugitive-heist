import qrcode
import cv2
import urllib
import numpy as np
from pyzbar.pyzbar import decode

def read_qr(url):
    # get image from url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib.request.Request(url, headers=hdr)
    con = urllib.request.urlopen(req)
    arr = np.asarray(bytearray(con.read()), dtype=np.uint8)
    print(arr)
    img = cv2.imdecode(arr, -1) 
    barcodes = decode(img)
    # qr_detector = cv2.QRCodeDetector()
    # data, bbox, straight_qrcode = qr_detector.detectAndDecode(img)
    # if bbox is not None:
    if len(barcodes) > 0:
        print("QR Code detected")
        data = barcodes[0].data.decode("utf-8")
        print("Decoded Data : {}".format(data))
        # print("Straight QR Code : {}".format(straight_qrcode))
        if data:
            return data
        else:
            return "QR code detected, No data found in QR code"
    else:
        print("QR Code not detected")
        return None