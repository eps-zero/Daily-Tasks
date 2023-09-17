from ui import create_ui
from database import initialize_database

def main():

    initialize_database()
    
    root = create_ui()

    root.mainloop()

if __name__ == "__main__":
    main()
