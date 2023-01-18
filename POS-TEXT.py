import pytesseract
import cv2
from pytesseract import Output
from Word import Word


def damePosCentralDePalabraEnImagen(rutaImagen , nombrePalabraBuscada , verbose):
    rta = None

    img = cv2.imread(rutaImagen)
    BW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    results = pytesseract.image_to_data(BW ,output_type=Output.DICT)
    arrResultadosTexto = results["text"]

    arrPalabras = []
    i = 0
    for nombre in arrResultadosTexto:
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        wordLoop = Word(nombre,x,y,h,w)

        if len(str(nombre).strip()) > 1:
            arrPalabras.append(wordLoop)
        i = i + 1


    for palabraLoop in arrPalabras:
        if verbose:
            print(str(palabraLoop))
        if palabraLoop.nombre == nombrePalabraBuscada:
            rta = palabraLoop
            break

    return rta







print("RESULTADO: " + str(damePosCentralDePalabraEnImagen("img3.png", "Oficina", False)))





# print("results:" + str(type(results)))
# print("results:" + str(results))
# print("results:" + str(results["text"]))
# print("results:" + str(results["left"]))
# print("results:" + str(results["top"]))
# print("results:" + str(results["top"]))
# print("results:" + str(results["width"]))
# print("results:" + str(results["height"]))
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# for i in len(results["text"]):
#     # We can then extract the bounding box coordinates
#     # of the text region from  the current result

    # print("encontre : " + str(i))
    # x = results["left"][i]
    # y = results["top"][i]
    # w = results["width"][i]
    # h = results["height"][i]
    #
    # print("ENCONTRÉ  BANDICAM EN: " + str(x) + "," + str(y))