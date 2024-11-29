import face_recognition as fr
import os

def reconhece_face(url_foto):
    """
    Carrega uma imagem e verifica se há rostos reconhecíveis.
    
    Args:
        url_foto (str): Caminho para o arquivo de imagem.

    Returns:
        tuple: Um booleano indicando se rostos foram encontrados e uma lista com os encodings dos rostos.
    """
    try:
        foto = fr.load_image_file(url_foto)
        rostos = fr.face_encodings(foto)
        return bool(rostos), rostos
    except Exception as e:
        print(f"Erro ao processar a imagem {url_foto}: {e}")
        return False, []

def get_rostos():
    """
    Carrega os rostos conhecidos e seus respectivos nomes.
    
    Returns:
        tuple: Lista de encodings de rostos conhecidos e lista de nomes correspondentes.
    """
    rostos_conhecidos = []
    nomes_dos_rostos = []

    # Caminho base para a pasta 'img'
    caminho_base = os.path.join(os.getcwd(), 'img')

    # Verifica se o diretório existe
    if not os.path.exists(caminho_base):
        print(f"Pasta 'img' não encontrada no caminho: {caminho_base}")
        return rostos_conhecidos, nomes_dos_rostos

    # Mapeia as imagens e nomes esperados
    imagens = {
        "Joao": "Joao.jpg",
        "Matheus": "Matheus.jpg",
        "Lucas": "Lucas.jpg",
        "Caique": "Caique.jpg",
        "Isabella": "Isabella.jpg",
        "Carol": "Carol.jpg",
        "Alex": "Alex.jpg",
    }

    for nome, arquivo in imagens.items():
        caminho_imagem = os.path.join(caminho_base, arquivo)
        rosto = reconhece_face(caminho_imagem)
        if rosto[0]:
            rostos_conhecidos.append(rosto[1][0])
            nomes_dos_rostos.append(nome)
        else:
            print(f"Rosto não encontrado em {arquivo} ou erro ao processar.")

    return rostos_conhecidos, nomes_dos_rostos