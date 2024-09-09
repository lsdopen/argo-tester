from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    # Fetch required environment variables
    env_vars = {
        'Database Password': os.environ.get('database_password', 'Not Set'),
        'Database URL': os.environ.get('database_url', 'Not Set'),
        'Database Username': os.environ.get('database_username', 'Not Set'),
        'Background Colour': os.environ.get('colour', '#FFFFFF'),
        'Hostname': os.environ.get('HOSTNAME', 'Not Set')
    }

    # HTML and CSS for the page layout
    html_content = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: {env_vars['Background Colour']};
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                max-width: 500px;
                width: 100%;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                text-align: left;
                padding: 8px 12px;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f4f4f4;
            }}
            tr:last-child td {{
                border-bottom: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Environment Variables</h2>
            <table>
                <tr><th>Key</th><th>Value</th></tr>
                <tr><td>Version</td><td>v1</td></tr>
                <tr><td>Database Password</td><td>{env_vars['Database Password']}</td></tr>
                <tr><td>Database URL</td><td>{env_vars['Database URL']}</td></tr>
                <tr><td>Database Username</td><td>{env_vars['Database Username']}</td></tr>
                <tr><td>Hostname</td><td>{env_vars['Hostname']}</td></tr>
            </table>
        </div>
    </body>
    </html>
    '''

    return html_content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
