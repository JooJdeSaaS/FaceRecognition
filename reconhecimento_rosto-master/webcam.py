import cv2
import face_recognition as fr
import numpy as np
from engine import get_rostos

# Carrega rostos conhecidos
rostos_conhecidos, nomes_dos_rostos = get_rostos()

# Inicializa a câmera
video_capture = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta corretamente
if not video_capture.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

while True:
    # Captura um frame da câmera
    ret, frame = video_capture.read()

    # Verifica se o frame foi capturado corretamente
    if not ret:
        print("Falha ao capturar o frame.")
        break

    # Converte o frame para RGB
    rgb_small_frame = np.ascontiguousarray(frame[:, :, ::-1])

    # Detecta os rostos no frame
    localizacao_dos_rostos = fr.face_locations(rgb_small_frame)
    
    # Verifique se rostos foram detectados
    if localizacao_dos_rostos:
        rosto_desconhecidos = fr.face_encodings(rgb_small_frame, localizacao_dos_rostos)

        # Para cada rosto encontrado, tenta comparar com os rostos conhecidos
        for (top, right, bottom, left), rosto_desconhecidos in zip(localizacao_dos_rostos, rosto_desconhecidos):
            # Verifica se o rosto foi comparado com algum rosto conhecido
            if len(rostos_conhecidos) > 0:
                resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecidos)
                face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecidos)

                melhor_id = np.argmin(face_distances)

                nome = nomes_dos_rostos[melhor_id] if resultados[melhor_id] else "Desconhecido"
            else:
                nome = "Desconhecido"

            # Desenha o retângulo ao redor do rosto
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Exibe o frame com os rostos detectados
    cv2.imshow('Webcam Face Recognition', frame)

    # Verifica se a tecla 'q' foi pressionada para finalizar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Fechando a câmera...")
        break

# Libera a câmera e fecha a janela
video_capture.release()
cv2.destroyAllWindows()
