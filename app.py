import os
from flask import Flask, request, send_file, render_template

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
    if request.method == 'GET':
        return '''
                <h1>Spline new File</h1>
                <form method="post" enctype="multipart/form-data">
                    <p> 
                        Select image file (JPEG or PNG format)
                        <input type="file" name="image">
                    </p>

                    <p> 
                        Enter comma separated vector X:
                        <input type="text" name="x">
                    </p>

                    <p> 
                        Enter comma separated vector Y:
                        <input type="text" name="y">
                    </p>

                    <p> 
                        Enter curve degree:
                        <input type="text" name="k">
                    </p>

                    <p>
                    <input type="submit">
                </form>
                '''

    form = SplineInputFormValidator(request.form)
    print(form.validate())
    if request.method == 'POST' and form.validate():
        if 'image' not in request.files:
            return 'There is no image in form!'

        coefficientsX = [int(item) for item in form.x.data.split(',')]
        coefficientsY = [int(item) for item in form.y.data.split(',')]
        curve_degree = int(form.k.data)

        imageFile = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], imageFile.filename)
        imageFile.save(path)

        result = spline.draw_spline_by_points(coefficientsX, coefficientsY, curve_degree, path)

        return send_file(result, mimetype='image/gif')
    else:
        if 'x' not in request.form:
            return 'X vector is not provided'

        if 'y' not in request.form:
            return 'Y vector is not provided'

        if 'k' not in request.form:
            return 'k is not provided'

@app.route('/spline/interpolate/', methods = ['GET', 'POST'])
def interpolate_spline():
    if request.method == 'POST':

        data = request.form
        coefficientsX = [int(item) for item in data['x'].split(',')]
        coefficientsY = [int(item) for item in data['y'].split(',')]
        curve_degree = int(data['k'])

        if 'image' not in request.files:
            return 'There is no image in form!'

        imageFile = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], imageFile.filename)
        imageFile.save(path)

        result = spline.interpolate_and_draw_spline_by_points(coefficientsX, coefficientsY, curve_degree, path)

        return send_file(result, mimetype='image/gif')

    return '''
                <h1>Spline new File</h1>
                <form method="post" enctype="multipart/form-data">
                    <p> 
                        Select image file (JPEG or PNG format)
                        <input type="file" name="image">
                    </p>

                    <p> 
                        Enter comma separated vector X:
                        <input type="text" name="x">
                    </p>

                    <p> 
                        Enter comma separated vector Y:
                        <input type="text" name="y">
                    </p>

                    <p> 
                        Enter curve degree:
                        <input type="text" name="k">
                    </p>

                    <p>
                    <input type="submit">
                </form>
                '''

if __name__ == '__main__':
    app.run()
