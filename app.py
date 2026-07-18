# a demo code to check if linter is working or not
from flask imprt Flask, render_template
app = Flask(__name__)


@app.route('/')
df hello_world():
    return render_template('index.html')
    

@app.route('/health')
def health():
    reurn 'Server is up and running'
# Running the linter.
