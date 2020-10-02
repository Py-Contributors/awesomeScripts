## Converting Image to Pencil Sketch <br>
### OVERVIEW: <br>
'Img_to_PencilSketch_convertor.py' is a program to convert Original RGB Colored Images to Pencil Sketches, much similar in appearance to a professional painter's pencil sketch.
'requirements.txt' is a file that specifies all the essentials required to run the above mentioned program. <br>
### TOOLS REQUIRED :<br>

<ul> Python - 3.7 Version </ul>
<ul> OpenCV - 4.4.1 </ul>

### CODE EXPLANATION :
<ol> <b>Step-1:  Importing Required libraries </b></ol>

<ol> import cv2 </ol>
<ol>import sys </ol>

<ol> <b> Step-2:  Loading the Image </b></ol>
<ul> filename = 'Enter Your File path'   # Eg: E:/Friends_family/IMG-20190406-WA0023.jpg </ul>
<ul>image = cv2.imread(filename) </ul>
<ol> <b> Step-3: Converting the Input Image into Gray Scale image </b> </ol>
<ul> gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) </ul>
<ol> <b> Step-4: Inverting the Gray Scaled Image</b> </ol>
<ul> inverted_images = 255 - gray_image </ul>
<ol>  <b>Step-5: Smoothing the Inverted Image Using Gaussian Blur Technique</b> </ol>
<ul> inverted_images = cv2.GaussianBlur(inverted_images, (21, 21), 0) </ul>

### SUGGESTIONS: <br>
If any upgradation or Bug fixes kindly, Fork the Repo and make a PR. I Assure you that if it's good to be Merged, it will be Merged into Main branch.

