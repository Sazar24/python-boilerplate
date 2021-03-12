## About
This is just a simple boilerplate to quick-start python app with some basic class-oriented architecture.

## podstawowe informacje rozruchowe:
- do każdego podfolderu wrzucać plik __init__.py
- inicjacja środowiska (venv - virtual environment):
- - python -m venv venv
- - venv\scripts\activate

- uwaga na importy: 
- - przy ścieżkach bezwględnych interpreter (w zależności od konfiguracji) może sypać błędem przez podanie 'src.' na początku. 


- start aplikacji:
- - python src\appStarter.py

- sprawdzenie że deployment zadziałał:
- - działa "przejdź do definicji" na dowolnej metodzie.

## propowavne ustawienia vscode (json):
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.linting.enabled": true,
    "files.exclude": {
        // ".vscode/": true,
        "**/__pycache__": true,
        "**/__init__.py": true
    },
    "search.exclude": {
        "/src/_proofs": true,
    },
    "workbench.panel.defaultLocation": "bottom",
    "python.linting.pylintArgs": [
        // "--ignore-relative-beyond-top-level-dupas"
        "--max-line-length=220"
    ],
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--ignore=E501,E722,E125,W503,W504,E116",
        "--max-line-length=220"
    ],
    "python.formatting.autopep8Args": [
        "--max-line-length=220"
    ],
    // "python.jediEnabled": false,  // <--- z tym eksperymentować, kiedy nie działa...
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./src",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true,
}
