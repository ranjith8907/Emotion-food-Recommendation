from flask import Flask,redirect,url_for,render_template,Response, jsonify
import gunicorn
from camera import *

app=Flask(__name__)

headings = ("Foods","Type","Restaurant")
df1 = music_rec()
df1 = df1.head(15)
global emo, emoation
emoation=""
emo=""

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/order/')
def order():
    return render_template("order.html")

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/emoation')
def emoation():
    return render_template("emoation.html" , emoation = emo)

@app.route('/face/')
def face():
    print(df1.to_json(orient='records'))
    return render_template('face.html', headings=headings, data=df1)   

def gen(camera):
    while True:
        global df1,frame
        frame,df1,emo = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        @app.route('/'+emo)
        def Happy():
            return render_template("order.html")
            
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')



if __name__=='__main__':
    app.run(debug=True)
