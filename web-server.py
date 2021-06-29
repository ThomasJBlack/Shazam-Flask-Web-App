from flask import Flask, request, render_template
from searchFuncs import requestFunc

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/songSearchResults", methods=["POST", "GET"])
def songSearchResults():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        song_search = form_data['Search Results']
        hits_list = requestFunc(song_search, "search")['tracks']['hits']
        return render_template('songSearchResults.html', hits_list=hits_list)


@app.route("/songRecomendations", methods=["POST"])
def songRecomendations():
    form_data = request.form
    key = form_data["song_key"]
    tracks_data = requestFunc(key, "songs/list-recommendations")

    if tracks_data:
        tracks_list = tracks_data['tracks']
        return render_template("songRecomendations.html", tracks_list=tracks_list)
    else:
        return render_template("noRecomendations.html")
