import cv2
from handDetection import HandDetection

# Inisialisasi deteksi tangan
handDetection = HandDetection(max_num_hands=2)

# Id ujung dan pangkal untuk masing-masing jari (sesuaikan dengan MediaPipe HandLandmarks)
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

    # Dapatkan hasil deteksi tangan (gambar sudah dicopy di findHandLandMarks)
    processed_frame, all_hands = handDetection.findHandLandMarks(frame, draw=True)

    for hand in all_hands:
        fingers_up = []

        # Cek masing-masing jari
        for tip_id, base_id in zip(fingers_tip_ids, fingers_base_ids):
            # Jika ujung jari (tip) lebih tinggi (nilai y lebih kecil karena koordinat layar)
            if hand[tip_id][2] < hand[base_id][2]:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

        # Tampilkan teks sesuai jari yang diangkat
        if fingers_up[0] == 1:
            cv2.putText(processed_frame, "EDGAR", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[1] == 1:
            cv2.putText(processed_frame, "LOVE", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[2] == 1:
            cv2.putText(processed_frame, "LANANG", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[3] == 1:
            cv2.putText(processed_frame, "SO", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        if fingers_up[4] == 1:
            cv2.putText(processed_frame, "MUCH", (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

    # Tampilkan frame
    cv2.imshow("Hand Landmark Detection", processed_frame)

    # Tekan 'a' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

webcam.release()
cv2.destroyAllWindows()
