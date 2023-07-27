from config import production, development
from flask_blog import CodeCircle

app = CodeCircle(config=production)

if __name__ == "__main__":
    app.run()
