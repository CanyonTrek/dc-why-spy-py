from app.data_clerk import DataClerk, FileLog  

def main():
    file_log = FileLog()
    clerk = DataClerk(file_log)
    clerk.process_data()

if __name__ == '__main__':
    main()

