from fileinput import filename
import os
from flask import Flask,render_template


app=Flask(__name__)
img_folder=os.path.join('static','img')
app.config['UPLOAD_FOLDER']=img_folder


@app.route('/')
def home():
    duck_name=os.path.join(app.config['UPLOAD_FOLDER'],'duck_img.jpeg')
    crow_name=os.path.join(app.config['UPLOAD_FOLDER'],'crow_img.jpeg')
    chicken_name=os.path.join(app.config['UPLOAD_FOLDER'],'chicken_img.jpg')
    return render_template('home.html',duck_image=duck_name,crow_image=crow_name,chicken_image=chicken_name)


if __name__=='__main__':
    app.run(debug=True)