import cv2
from handDetection import HandDetection

# Inisialisasi deteksi tangan
handDetection = HandDetection(max_num_hands=2)

# Id ujung dan pangkal untuk masing-masing jari
fingers_tip_ids = [4, 8, 12, 16, 20]
fingers_base_ids = [2, 6, 10, 14, 18]

# Mulai webcam
webcam = cv2.VideoCapture(0)

while True:
    status, frame = webcam.read()
    if not status:
        break

    # Membalik gambar agar lebih nyaman
    frame = cv2.flip(frame, 1)

    # Dapatkan hasil deteksi tangan
    processed_frame, handLandmarksList = handDetection.findHandLandMarks(frame, draw=True)

    for hand in handLandmarksList:
        fingers_up = []

        # Deteksi Jempol
        if hand[fingers_tip_ids[0]][2] < hand[fingers_base_ids[0]][2]:  # Cek Y posisi tip vs base jempol
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Deteksi Telunjuk
        if hand[fingers_tip_ids[1]][2] < hand[fingers_base_ids[1]][2]:  # Cek Y posisi telunjuk
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Deteksi Tengah
        if hand[fingers_tip_ids[2]][2] < hand[fingers_base_ids[2]][2]:  # Cek Y posisi tengah
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Deteksi Manis
        if hand[fingers_tip_ids[3]][2] < hand[fingers_base_ids[3]][2]:  # Cek Y posisi manis
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Deteksi Kelingking
        if hand[fingers_tip_ids[4]][2] < hand[fingers_base_ids[4]][2]:  # Cek Y posisi kelingking
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        # Menampilkan teks berdasarkan jari yang terangkat
        if fingers_up[0] == 1:
            cv2.putText(processed_frame, "I", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[1] == 1:
            cv2.putText(processed_frame, "LOVE", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[2] == 1:
            cv2.putText(processed_frame, "YOU", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[3] == 1:
            cv2.putText(processed_frame, "SO", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[4] == 1:
            cv2.putText(processed_frame, "MUCH", (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

    # Tampilkan hasil deteksi di layar
    cv2.imshow("Hand Landmark Detection", processed_frame)

    # Tekan 'a' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Tutup webcam dan jendela OpenCV
webcam.release()
cv2.destroyAllWindows()
