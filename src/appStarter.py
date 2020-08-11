from config import setProjectPath
setProjectPath()

if __name__ == "__main__": 
    from app.appRunner import App
    App().run()
