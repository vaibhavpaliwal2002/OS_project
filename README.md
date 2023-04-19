# OS_project
**Video Surveillance**

----------------------------------------------------

## Contributors

* Yash Rajoria - 2020UEA6570
* Vaibhav Paliwal - 2020UEA6571
* Rohit Kumar - 2020UEA6573
* Ritik - 2020UEA6575

----------------------------------------------------
## [Dataset](https://paperswithcode.com/dataset/ucf-crime)

----------------------------------------------------
## Abstract

Nowadays, CCTV cameras are placed all over the places 
for surveillance and security. But surveillance is a 
very tedious and time-consuming job.
To improve upon this as the number of cameras is 
increasing, our objective is to make this process fast 
and automatic.

We propose using Slow Fast networks for video recognition.
The models achieve strong performance for both action 
classification and detection in video as oppose to traditional
convolution networks.

## Slow Fast networks

SlowFast uses a slow, high-definition CNN (Fast pathway) to 
analyse the static content of a video while running in parallel 
a fast, low-definition CNN (Slow pathway) whose goal is to analyse 
the dynamic content of a video.

## Methodology

Videos of 32 frames each are first extracted using the available CCTV
cameras. The frames are then fed into the model using a centralised 
system which manage feeds form multiple cameras simultaneously, 
if the model predicts some kind anomaly on the feed then a notification
is pushed to the concerned authorities regarding the anomaly, this includes 
location of the incident, type of anomaly detected and severity.

Additionally the system is also capable of running facial recognition to 
identify suspected criminals.

## Reference
https://www.google.com/url?sa=t&source=web&rct=j&url=https://openaccess.thecvf.com/content_ICCV_2019/papers/Feichtenhofer_SlowFast_Networks_for_Video_Recognition_ICCV_2019_paper.pdf&ved=2ahUKEwju14beo7X-AhXWSmwGHRwlBOkQFnoECBMQAQ&usg=AOvVaw1HXHzxENqssoWj4sNtQkJU
