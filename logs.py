import datetime
file_path = "logs.txt"
def log_to_file (message, level="INFO"):
    """"
    funkcja zapisująca logi do pliku logs.txt
    :param message: Treść logu.
    :param level: Poziom logu (INFO, ERROR).
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open(file_path, "a") as log:
        log.write(f"[{timestamp}] {level}: {message}\n")


log_to_file("hej")
