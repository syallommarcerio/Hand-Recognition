import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

class HandDetection:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = mpHands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def findHandLandMarks(self, image, draw=False):
        originalImage = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)

        allHandsLandmarks = []

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                singleHandLandmarks = []
                imgH, imgW, _ = originalImage.shape
                for id, landMark in enumerate(hand.landmark):
                    xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                    singleHandLandmarks.append([id, xPos, yPos])

                allHandsLandmarks.append(singleHandLandmarks)

                if draw:
                    mpDraw.draw_landmarks(originalImage, hand, mpHands.HAND_CONNECTIONS)

        return originalImage, allHandsLandmarks
