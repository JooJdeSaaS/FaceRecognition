import face_recognition as fr
import os
from engine import reconhece_face, get_rostos

# Caminho relativo para a imagem desconhecida
caminho_imagem_desconhecido = os.path.join(os.getcwd(), 'img', 'desconhecido.jpg')

try:
    # Reconhece rosto na imagem desconhecida
    desconhecido = reconhece_face(caminho_imagem_desconhecido)

    if desconhecido[0]:  # Se encontrou rostos na imagem desconhecida
        rosto_desconhecido = desconhecido[1][0]

        # Obtém os rostos conhecidos e os nomes correspondentes
        rostos_conhecidos, nomes_dos_rostos = get_rostos()

        if rostos_conhecidos:  # Se houver rostos conhecidos para comparar
            # Compara o rosto desconhecido com os conhecidos
            resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)

            reconheceu_alguem = False
            for i, resultado in enumerate(resultados):
                if resultado:
                    print(f"Rosto de {nomes_dos_rostos[i]} foi reconhecido")
                    reconheceu_alguem = True

            if not reconheceu_alguem:
                print("Nenhum rosto conhecido foi reconhecido na imagem desconhecida.")
        else:
            print("Nenhum rosto conhecido foi carregado para comparação.")
    else:
        print("Não foi encontrado nenhum rosto na imagem desconhecida.")
except Exception as e:
    print(f"Erro ao processar a imagem desconhecida: {e}")

