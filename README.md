# Flask blog

Welcome to Flask blog This is a fully functional blog application built using Flask and HTML, CSS, & JavaScript. It allows users to create, manage, and share blog posts, along with a wide range of features including user authentication, commenting, notifications, and more.

## Screenshots

Insert some screenshots of your application to showcase its UI and features.

## Features & Functionality

- User Authentication:
  - Allow users to Register & log in their accounts.
  - Users also register with social accounts (Google & Github).
  - Users can recover their passwords using email address.
  - Users also change their current email to new email address.
- User Management:
  - User can edit their profile detail and also added profile image.
  - User can change their password after log in.
  - User can delete their account and data.
- Blog Post Management:
  - Create & edit blog posts with a rich text editor.
  - Only author can delete their blog post.
- Likes & Saves Post:
  - Readers can like and save the post after login.
- Commenting System:
  - Engage with readers through comments to the blog posts.
  - Also replies to the comments.
- Notifications:
  - Get notified about new comments, likes to your blog post.
  - Get notified about someone follows you.
- Dark and Light Modes:
  - Enjoy a comfortable reading experience with both light and dark themes.
- User Interaction:
  - Follow other users and stay updated with their posts.
- Advanced Search:
  - Easily find posts by keywords or categories.
- Internationalization (i18n):
  - Supports multiple languages for a global audience.
- Responsive Design:
  - Enjoy a seamless experience on different devices and screen sizes.

## Installation & Set up

### Prerequisites

- Python 3.x
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- Git (optional, but recommended for cloning the repository)

### 1. Clone the git repository.

```bash
git clone https://github.com/yourusername/flask-blog.git
```

### 2. Go to the project directory.

```bash
cd flask-blog
```

### 3. Create virtual environment.

```bash
python3 -m venv venv
```

### 4. Activate the environment.

On Windows

```bash
venv\Scripts\activate
```

On MacOS/Linux

```bash
source venv/bin/activate
```

### 5. Install the requirement package.

```bash
pip install -r requirements.txt
```

To run this project locally, you will need to set `.env.example` file to `.env` on base directory and set values to environment variables.


### 6. Migrate/Create a database.

Initialize the database migration directory.

```bash
flask db init
```

Run migrate command.

```bash
flask db migrate -m "initial_migration"
```

Upgrade the database for latest migration.

```bash
flask db upgrade
```

### 7. Last to run the application.

```bash
flask run
```

Access the application at `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
For more information checkout ![CONTRIBUTING.md](https://github.com/anuraagnagar/flask-blog/blob/master/CONTRIBUTING.md)
