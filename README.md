**DOTA_YOLOv2** provides the data convertion code, parameter files while training <a href="http://captain.whu.edu.cn/DOTAweb/dataset.html">DOTA<a> using <a href="https://pjreddie.com/darknet/yolov2/">YOLOv2<a>, and the trained model is also provided. So it's convenient for you to use them.<br>
<br>
Our code is tested on official <a href="https://github.com/pjreddie/darknet">darknet@(commit f6d8617)<a> with cuda-8.0 and cudnn-6.0 on Ubuntu 16.04.1 LTS.<br>
## Installation
* install darknet<br>
  See <a href="https://pjreddie.com/darknet/install/">Installing Darknet<a> for instructions.<br>
* development kit<br>
  The <a href="https://github.com/CAPTAIN-WHU/DOTA_devkit">Development kit<a> provides the following functions. You can easily install it following the instructions.<br> 
    * Load and visulize the data.
    * Evaluate the result.
    * Split and merge the picture and label.<br>
## Training YOLO on DOTA
* Get the <a href="http://captain.whu.edu.cn/DOTAweb/dataset.html">DOTA<a> Dataset<br>

* Convert the Label Format<br>
  In DOTA, the annotation format is:
  ```
      x1 y1 x2 y2 x3 y3 x4 y4 category difficult
  ```
  While Darknet wants a .txt file for each image with a line for each ground truth object in the image that looks like:
  ```
      category-id x y width height
  ```
  Where x, y, width, and height are relative to the image's width and height.
  Here, you can refer to <a href="https://github.com/ringringyi/DOTA_YOLOv2/tree/master/data_transform">data_transform/YOLO_Transform.py<a> to convert the format.<br>
  
  Note that this code is for the image of size 1024*1024. If not, you should modify it accroding to your image size. For DOTA, you can refer to  <a href="https://github.com/CAPTAIN-WHU/DOTA_devkit/blob/master/ImgSplit.py">DOTA_devkit/ImgSplit.py<a> to split the images and labels.

* Train the Model<br>
  ```
      wget https://pjreddie.com/media/files/darknet19_448.conv.23
      sh train-dota.sh 
  ```
* Evaluate the Results<br>
  You can download the pre-trained model on DOTA from <a href="https://pan.baidu.com/s/1A23G8zlmJxj0o3MgG7rkrA">Baidu Drive<a> or <a href="https://drive.google.com/open?id=1bE1WU0HhVd2ZGZur2TC9QcTWnmgHtwZ6">Google Drive<a>, and use it to test all the test images.
  ```
      sh valid-dota.sh 
  ```
  Then you will obtain 15 files stored in the `results/` subdirectory, and each file contains all the results for a specific category.Each file is in the following format:<br>
  ```
      imgname score xmin ymin xmax ymax 
  ```
  If you have split the images before, please first use <a href="https://github.com/CAPTAIN-WHU/DOTA_devkit/blob/master/ResultMerge.py"> DOTA_devkit/ResultMerge.py<a> to merge the results.<br>
  <br>
  For DOTA, You can submit your results on the <a href="http://www.icdar2017chinese.site:5084/evaluation2/"> Evaluation Server<a> for evaluation. See the official website of <a href="http://captain.whu.edu.cn/DOTAweb/dataset.html">DOTA<a> for details.<br>
    
