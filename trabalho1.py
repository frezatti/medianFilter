import cv2
import numpy as np

# Função para adicionar ruído de sal e pimenta a uma imagem
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.shape[0] * image.shape[1]
    
    # Adicionar ruído de sal
    salt_pixels = int(total_pixels * salt_prob)
    salt_coordinates = [np.random.randint(0, i - 1, salt_pixels) for i in image.shape]
    noisy_image[salt_coordinates[0], salt_coordinates[1]] = 255

    # Adicionar ruído de pimenta
    pepper_pixels = int(total_pixels * pepper_prob)
    pepper_coordinates = [np.random.randint(0, i - 1, pepper_pixels) for i in image.shape]
    noisy_image[pepper_coordinates[0], pepper_coordinates[1]] = 0

    return noisy_image


def remove_noise(image, kernel_size):

    denoised_image = np.copy(image)
    offset = kernel_size // 2
    height, width = denoised_image.shape
    
    for i in range (offset, height - offset):
        for j in range (offset, width - offset):
            neighborhood = []
            for k in range (0 - offset, offset + 1):
                for l in range (0 - offset, offset + 1):
                    neighborhood.append(image[i + k, j + l])
            denoised_image[i,j] = np.median(neighborhood)
    
    return denoised_image
            
            
    # return cv2.medianBlur(image, kernel_size)

# Carregar uma imagem
image = cv2.imread('cameraman.pgm', cv2.IMREAD_GRAYSCALE)

# Parâmetros para adicionar ruído de sal e pimenta
salt_prob = 0.2  # Probabilidade de ruído de sal
pepper_prob = 0.2 # Probabilidade de ruído de pimenta

# Adicionar ruído à imagem
noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Parâmetro do tamanho do kernel para a filtragem de média
kernel_size = 31 
# Remover o ruído
denoised_image = remove_noise(noisy_image, kernel_size)
denoised_image = remove_noise( denoised_image,kernel_size)

# Exibir as imagens
#cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem com Ruído', noisy_image)
cv2.imshow('Imagem Denoised', denoised_image)
#io.imshow
cv2.waitKey(0)
cv2.destroyAllWindows()
