
### `src/ui.py`

The user interface (e.g., using Flask for a web interface).

#### Example `ui.py`:

```python
from flask import Flask, render_template, request
from config import SPOILER_KEYWORDS
from spoiler_detection import detect_spoilers
from notifications import send_notification

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_content():
    content = request.form['content']
    spoilers_detected = detect_spoilers(content, SPOILER_KEYWORDS)
    if spoilers_detected:
        send_notification("Spoiler Alert!", "Potential spoilers detected in the content.")
    return render_template('result.html', spoilers=spoilers_detected)

if __name__ == '__main__':
    app.run(debug=True)
