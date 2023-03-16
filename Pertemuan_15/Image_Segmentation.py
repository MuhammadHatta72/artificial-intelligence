# K-Means clustering adalah algoritma mesin learning unsupervised yang bertujuan untuk mempartisi N pengamatan ke dalam K cluster di mana setiap pengamatan menjadi milik cluster dengan rata-rata terdekat. Cluster mengacu pada kumpulan titik data yang dikumpulkan bersama karena kesamaan tertentu. Untuk segmentasi gambar, cluster disini adalah warna gambar yang berbeda.

#install library
#pip3 install opencv-python numpy matplotlib

#import library
#cv2 berfungsi memodifikasi gambar. contoh mengubah pixel, mengubah BGR ke RGB.
import cv2
#numpy berfungsi untuk mengolah data array
import numpy as np
#matplotlib berfungsi untuk menampilkan gambar
import matplotlib.pyplot as plt

# membaca gambar dari direktori
image = cv2.imread("image.jpg")

# konversi gambar dari BGR ke RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# membentuk ulang gambar menjadi susunan piksel 2D dan 3 nilai warna (RGB)
pixel_values = image.reshape((-1, 3))
# konversi pixel ke tipe data float
pixel_values = np.float32(pixel_values)

# menampilkan hasil konversi
print(pixel_values.shape)

#Algoritma berhenti ketika tidak ada tugas cluster yang berubah. Maka saya set menjadi 100 iterasi dan 0,2 nilai epsilon. karena gambar yang dipakai memiliku sejumlah besar titik data, jadi akan memakan banyak waktu untuk memprosesnya, Jadi ketika sejumlah iterasi terlampaui (katakanlah 100), atau jika cluster bergerak kurang dari beberapa nilai epsilon (katakanlah 0,2)
# menghentikan algoritme ketika tidak ada tugas cluster yang berubah
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# menentukan jumlah cluster, kali ini menggunakan 3 cluster. karena ada tiga warna primer (hijau untuk pepohonan, biru untuk laut/danau, dan putih hingga jingga untuk langit).
# jumlah cluster
k = 3
# menentukan titik awal cluster dengan metode random atau acak
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# konversi lagi ke tipe data 8 bit
centers = np.uint8(centers)

# meratakan label cluster
labels = labels.flatten()

# konversi gambar ke warna yang sesuai dengan label cluster
segmented_image = centers[labels.flatten()]

# mengubah bentuk gambar ke bentuk aslinya
segmented_image = segmented_image.reshape(image.shape)

# menampilkan gambar
plt.imshow(segmented_image)
plt.show()


# dalam studi kasus beda, yaitu menggunakan 2 cluster maka gambar yang di tampilkan akan lebih gelap
# nonaktifkan hanya 2 cluster untuk mengubah piksel menjadi hitam
masked_image = np.copy(image)
# mengkonversi ke bentuk vektor nilai piksel
masked_image = masked_image.reshape((-1, 3))
# warna ketiga di nonaktifkan
cluster = 2
masked_image[labels == cluster] = [0, 0, 0]
# mengubah bentuk gambar ke bentuk aslinya
masked_image = masked_image.reshape(image.shape)
# menampilkan gambar
plt.imshow(masked_image)
plt.show()