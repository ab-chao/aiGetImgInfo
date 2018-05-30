from flask import send_from_directory, app


@app.route('/getImg/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)