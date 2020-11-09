# Facial-Keypoints-detection

The objective of this task is to predict keypoint positions on face images. This can be used as a building block in several applications, such as:

- tracking faces in images and video
- analysing facial expressions
- detecting dysmorphic facial signs for medical diagnosis
- biometrics / face recognition

Detecing facial keypoints is a very challenging problem.  Facial features vary greatly from one individual to another, and even for a single individual, there is a large amount of variation due to 3D pose, size, position, viewing angle, and illumination conditions. Computer vision research has come a long way in addressing these difficulties, but there remain many opportunities for improvement.

Kaggle dataset :- https://www.kaggle.com/c/facial-keypoints-detection


Script has 2 files

- **createModel.py**: It for creating and saving keras model for facial keypoints.
- **facialkeypointsdetection.py** it's for detecting and extracting face for prediction.


## Note: first create model using createModel.py. Google Colab Script link is added in file.