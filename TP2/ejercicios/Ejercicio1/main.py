import OS
import sys
import threading
opciones = ["alternativa_1", "alternativa_2"]
def main():
  if len(sys.argv) != 2:
    print("Ingrese un argumento: alternativa_1 o alternativa_2")
    return
  elif sys.argv[1] not in opciones:
    print("Argumento invalido. Usar alternativa_1 o alternativa_2")
  else:
    threading.Thread(target=OS.run, args=(sys.argv[1],)).start()
main()

