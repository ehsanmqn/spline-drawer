import os
from flask import Flask, request, send_file, Response, render_template

import spline
from validators import SplineInputFormValidator

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'Hello dear examiner. This is a Spline plotting service. Use /spline/draw/ or /spline/interpolate/' \
           ' from Postman or any other tools you usually use!'

@app.route('/spline/draw/', methods = ['GET', 'POST'])
def draw_spline():
    # Handling GET in order to send HTML form to the browser
    if request.method == 'GET':
        return render_template('_input_form.html')

    # Get form data
    form = SplineInputFormValidator(request.form)

    # Validate form data
    if request.method == 'POST' and form.validate():
        if 'image' not in request.files:
            return 'There is no image in form!'

        # Read string data from input form then convert them to the integer
        coefficientsX = [int(item) for item in form.x.data.split(',')]
        coefficientsY = [int(item) for item in form.y.data.split(',')]
        curveDegree = int(form.k.data)

        # Read image file and save it to uploads folder
        imageFile = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], imageFile.filename)
        imageFile.save(path)

        # Draw spline using input data
        result = spline.draw_spline_by_points(coefficientsX, coefficientsY, curveDegree, path)

        return send_file(result, mimetype='image/gif')
    else:
        if 'x' not in request.form:
            return  Response("x vector is not provided",
                             status=400,
                             mimetype='application/json')

        if 'y' not in request.form:
            return Response("y vector is not provided",
                            status=400,
                            mimetype='application/json')

        if 'k' not in request.form:
            return  Response("curve degree k is not provided",
                             status=400,
                             mimetype='application/json')

@app.route('/spline/interpolate/', methods = ['GET', 'POST'])
def interpolate_spline():
    # Handling GET in order to send HTML form to the browser
    if request.method == 'GET':
        return render_template('_input_form.html')

    form = SplineInputFormValidator(request.form)
    if request.method == 'POST' and form.validate():
        if 'image' not in request.files:
            return 'There is no image in form!'

        coefficientsX = [int(item) for item in form.x.data.split(',')]
        coefficientsY = [int(item) for item in form.y.data.split(',')]
        curveDegree = int(form.k.data)

        imageFile = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], imageFile.filename)
        imageFile.save(path)

        result = spline.interpolate_and_draw_spline_by_points(coefficientsX, coefficientsY, curveDegree, path)

        return send_file(result, mimetype='image/gif')
    else:
        if 'x' not in request.form:
            return Response("x vector is not provided",
                            status=400,
                            mimetype='application/json')

        if 'y' not in request.form:
            return Response("y vector is not provided",
                            status=400,
                            mimetype='application/json')

        if 'k' not in request.form:
            return Response("curve degree k is not provided",
                            status=400,
                            mimetype='application/json')

if __name__ == '__main__':
    app.run()
