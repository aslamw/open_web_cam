import cv2

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente
if not cap.isOpened():
    raise IOError("Não foi possível abrir a webcam")

# Loop principal
while True:
    # Lê o frame da webcam
    ret, frame = cap.read()

    # Mostra o frame em uma janela
    cv2.imshow('Webcam', frame)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()
