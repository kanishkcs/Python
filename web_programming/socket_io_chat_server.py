from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
from flask_cors import CORS, cross_origin

app = Flask(__name__)    #Creating APp 
app.config['SECRET_KEY'] = "secret!" # Adding the Secret Key to Config File.

# Setting Up Cors Origins
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['transports'] = 'websocket'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading') # Creating Socket with allowed all cors Origins
cors = CORS(app) # Settins Cors
@socketio.on('message') # Checking For Messages


def handle_message(data):  # Function to Handle Message
    global list1
    if data!='I am Connected!':
        send(data,broadcast=True)
    else:
        print(data)

@app.route("/")
def home_page():  # Rendring Index File
    return render_template("index.html")

if __name__ == '__main__':  # Starting the Socketio app WebServer
    socketio.run(app,debug=True)
