# SPLINE-DRAWER-API
This project contains a simple and tiny backend application and related APIs for the Spline drawer project related to danaXa interview challenges.

## Contents
1. Install requirements
2. How to run project
3. Use served APIs

#### Install requirements
This project contains a [requirements.txt](requirements.txt) file. Using this file, you are able to install required packages. First of all,
create a python3 virtual environments then install packages inside the virtual environmnt.
```shell script
git clone https://gitlab.com/ehsanmqn/spline-drawer
cd spline-drawer
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

#### How to run project
In order to run development server perform as follow:
```shell script
python -m flask run --reload
```

#### Use served APIs
This is a tiny flask project that serves 2 separate APIs for the B-spline drawer. The first API, draw a B-Spline curve on a selected image 
giving spline control polygon points. The other, finds interpolate and draw B-spline curve that go through determined points
and or in other words a curve fitting using a cubic B-spline curve.
Theses APIs are served using folowing paths:
```shell script
http://{server_ip}:{server_port}/spline/draw/

http://{server_ip}:{server_port}/spline/interpolate/
``` 
You are able to use thease APIs using Postman or any other tools you usually use for this purpose. API documentations can 
be reached from [API Documentation](https://documenter.getpostman.com/view/5584679/TzCTaRNj). Furthermore, a simple HTML form also prepared for each API. For
this mean you should open above links in your browser.

As you didnt' provide an input template and test case, I've uploaded an [image](uploads/test.jpg) from the challenges document in the [uploads](uploads) folder. 
In order to test APIs, I cut this image from the document and extract your selected points according to the image size. 
You are free to use this image using following parameters.
```requirements.txt
x: 282,286,335,252,256,259,244
y: 64,127,257,396,492,568,578
k: 3
```

Happy codding!!!