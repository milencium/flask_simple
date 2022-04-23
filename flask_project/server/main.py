from flask import Flask, jsonify
from functions import load_files, parse_file


app = Flask(__name__)


@app.route('/data')
def get():
    all_files = load_files("Data")
    file1 = all_files[0]
    data_table, channels = parse_file(file1)
    data_table_2 = data_table.tolist()
    return jsonify(channels, data_table_2)


if __name__ == '__main__':
    app.run(debug=True)
