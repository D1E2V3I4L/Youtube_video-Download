from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = r"C:\Users\HARSH THAKUR\Desktop\Youtuve video"  # Replace with your desired directory path
        stream.download(output_path=download_path)
        return f"Downloaded {yt.title} to {download_path}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
