from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
<style>
    .row {
        display: flex;
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
      }
      
      .column {
        flex: 50%;
      }
</style>


<div class="row">
    <div class="column">
        <iframe src="https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/" frameborder="0" scrolling="no" width="100%" height="100%"></iframe>
    </div>
    <div class="column">
        <iframe src="https://vscode.dev/github/streamlit/demo-uber-nyc-pickups/blob/master/streamlit_app.py" frameborder="0" scrolling="no" width="100%" height="100%"></iframe>
    </div>
  </div>

<!--

<div class="box">
    <iframe src="https://embed.spotify.com/?uri=spotify:user:1290230929:playlist:6nTIVNGZfnZ4urUiwHIgpT" frameborder="0" scrolling="no" width="100%" height="512" align="left"> </iframe>
</div>

<div class="box">
    <iframe src="https://embed.spotify.com/?uri=spotify:user:1285279066:playlist:56KI83cMiMTOocIdXq2R5j" frameborder="0" scrolling="no" width="100%" height="512" align="right"></iframe>
</div>-->
"""