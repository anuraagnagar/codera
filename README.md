# Codera

Welcome to Codera This is a fully functional blog application built using Flask\Python and HTML, CSS, & JavaScript.

## Live Demo

You can checkout a live preview of this Application by clicking [HERE]().

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation--set-up)
4. [Contributing](#contributing)
5. [License](#license)
6. [Author](#author)

## Features

For a detailed list of features, please refer to [FEATURES.md](https://github.com/anuraagnagar/codera/blob/master/FEATURES.md).

## Prerequisites

- Python 3.x
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- Git (optional, but recommended for cloning the repository)

## Installation & Set up

### 1. Clone the git repository.

```bash
git clone https://github.com/anuraagnagar/codera.git
```

### 2. Go to the project directory.

```bash
cd codera
```

### 3. Create and Activate virtual environment.

On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

On MacOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install the requirement package.

```bash
pip install -r requirements.txt
```

To run this project locally, you will need to set `.env.example` file to `.env` on base directory and set values to environment variables.

### 5. Migrate/Create a database.

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

### 6. Run the application.

```bash
flask run
```

Access the application at `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
For more information checkout [CONTRIBUTING.md](https://github.com/anuraagnagar/codera/blob/master/CONTRIBUTING.md)

## License

By contributing to this project, you agree that your contributions will be licensed under the [BSD-3-Clause](https://github.com/anuraagnagar/codera/blob/master/LICENSE)

## Author

[Anurag Nagar](mailto:nagaranurag1999@gmail.com)
