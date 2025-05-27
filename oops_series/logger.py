 

class Logger:
    def __init__(self):
        print("logger has been created")
    
    def __del__(self):
        print("logger has been deleted")

log = Logger()
