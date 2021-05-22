from config import setProjectPath  # type: ignore
setProjectPath()

if __name__ == "__main__":
    from src.app.appRunner import App

    app = App()
    app.run()
