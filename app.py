from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    env_vars = os.environ
    colour = env_vars.get('colour', '#FFFFFF')  # Default to white if not set
    env_table = ''.join([f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in env_vars.items()])
    return f'''
    <html>
    <body style="background-color:{colour};">
    <h1>Environment Variables</h1>
    <table border="1">
    <tr><th>Key</th><th>Value</th></tr>
    {env_table}
    </table>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
