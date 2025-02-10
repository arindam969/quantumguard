import win32print
import win32con
import threading
from queue import Queue

class QuantumGuard:
    def __init__(self):
        self.printer_queue = Queue()
        self.lock = threading.Lock()
        self.initialize_printer()

    def initialize_printer(self):
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        if not printers:
            raise RuntimeError("No printers found.")
        self.default_printer = printers[0][2]
        win32print.SetDefaultPrinter(self.default_printer)

    def add_print_task(self, document_path):
        print(f"Adding document to queue: {document_path}")
        self.printer_queue.put(document_path)
        threading.Thread(target=self.process_print_queue).start()

    def process_print_queue(self):
        self.lock.acquire()
        try:
            while not self.printer_queue.empty():
                document_path = self.printer_queue.get()
                self.print_document(document_path)
        finally:
            self.lock.release()

    def print_document(self, document_path):
        try:
            hPrinter = win32print.OpenPrinter(self.default_printer)
            try:
                hJob = win32print.StartDocPrinter(hPrinter, 1, ("QuantumGuard Print Job", None, "RAW"))
                try:
                    win32print.StartPagePrinter(hPrinter)
                    with open(document_path, "rb") as f:
                        data = f.read()
                        win32print.WritePrinter(hPrinter, data)
                    win32print.EndPagePrinter(hPrinter)
                finally:
                    win32print.EndDocPrinter(hPrinter)
            finally:
                win32print.ClosePrinter(hPrinter)
            print(f"Successfully printed: {document_path}")
        except Exception as e:
            print(f"Failed to print {document_path}: {e}")

# Example usage
if __name__ == "__main__":
    qg = QuantumGuard()
    qg.add_print_task("example_document.txt")