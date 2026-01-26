from emotion_detection import emotion_detector2
import unittest

class TestEmotionDetector2(unittest.TestCase):
    def test_emotion_detector2(self):
        # Test case for joy sentiment
        result_1 = emotion_detector2('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Test case for anger sentiment
        result_2 = emotion_detector2('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Test case for disgust
        result_3 = emotion_detector2('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        result_4 = emotion_detector2('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        result_5 = emotion_detector2('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')
if __name__ == "__main__":
    unittest.main(verbosity=2)
    


        