from flask import Flask
from flask import send_file
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)
server_port = 80
banned_user_agents = ["Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0"]

def log_everything_we_know(req):
    # Log everything we know to console
    print('\x1b[6;30;42m' + 'Request headers:' + '\x1b[0m')
    for header in req.headers:
        print(header)
    print('\x1b[6;30;42m' + 'Data as per request.environ:' + '\x1b[0m')
    for item in request.environ:
        print(item + " : " + str(request.environ.get(item)))
    print('\x1b[6;30;42m' + 'IP address as per HTTP_X_REAL_IP:' + '\x1b[0m')
    hdr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if not hdr:
        print("Header not available, see below for IP address")
    else:
        print(hdr)
    print('\x1b[6;30;42m' + 'IP address as per remote_addr:' + '\x1b[0m')
    print(request.remote_addr)
    print('\x1b[6;30;42m' + 'URL visited:' + '\x1b[0m')
    

@app.route('/image.jpeg')
def get_image():
    log_everything_we_know(request)
    if request.environ.get("HTTP_USER_AGENT") in banned_user_agents:
       print('\033[1;31m' + 'Banned user agent, not serving image' + '\x1b[0m')
       return render_template('404.html')
    else:
       filename = 'image.jpeg'
    return send_file(filename, mimetype='image/jpeg')

@app.errorhandler(404)
def page_not_found(e):
    log_everything_we_know(request)
    return render_template('404.html')

app.run(host="0.0.0.0",
        debug=True,
        use_reloader=True,
        port=server_port,
        passthrough_errors=True,
        threaded=True)