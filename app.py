from flask import Flask, request, redirect, url_for, render_template,jsonify
from werkzeug import secure_filename



app = Flask(__name__)



app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#
#def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


#@app.context_processor
#def override_url_for():
#    print("override url", file=sys.stderr)
#    return dict(url_for=dated_url_for)
#
#
#def dated_url_for(endpoint, **values):
#    if endpoint == 'js_static':
#        filename = values.get('filename', None)
#        print(filename, file=sys.stderr)
#        if filename:
#            file_path = os.path.join(app.root_path,
#                                     'static/js', filename)
#            values['q'] = int(os.stat(file_path).st_mtime)
#            print("value q", file=sys.stderr)
#            print(values['q'], file=sys.stderr)
#    elif endpoint == 'css_static':
#        filename = values.get('filename', None)
#        if filename:
#            file_path = os.path.join(app.root_path,
#                                     'static/css', filename)
#            values['q'] = int(os.stat(file_path).st_mtime)
#    return url_for(endpoint, **values)
#
#
#@app.route('/css/<path:filename>')
#def css_static(filename):
#    return send_from_directory(app.root_path + '/static/css/', filename)
#
#
#@app.route('/js/<path:filename>')
#def js_static(filename):
#    return send_from_directory(app.root_path + '/static/js/', filename)


@app.route('/')
def index():
    return "Hey"
#    return render_template('index.html')
#
#
#@app.route('/uploadajax', methods=['POST'])
#def upldfile():
#    if request.method == 'POST':
#        files = request.files['file']
#        if files and allowed_file(files.filename):
#            filename = secure_filename(files.filename)
#            app.logger.info('FileName: ' + filename)
#            updir = os.path.join(basedir, 'upload/')
#            files.save(os.path.join(updir, filename))
#            file_size = os.path.getsize(os.path.join(updir, filename))
#            return jsonify(name=filename, size=file_size)

#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
if __name__ == '__main__':
    app.run(debug=True)
