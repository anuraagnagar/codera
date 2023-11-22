from flask_blog import Codera
from config import production, development

app = Codera(config=production)

if __name__ == "__main__":
    app.run()
