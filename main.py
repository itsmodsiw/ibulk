from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QScrollBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QPixmap, QClipboard, QIcon
from PIL import Image
import os
import shutil
import traceback

class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setGeometry(300, 300, 600, 600)  # Set initial size and position
        self.setWindowTitle("modsiw's Image Converter")  # Set window title
        self.setWindowIcon(QIcon('app_icon.png'))  # Set window icon

        # Styling
        self.setStyleSheet("""
            QWidget {
                background: #2F3136;
            }
            QPushButton {
                background-color: #7289DA;
                border-radius: 4px;
                padding: 5px;
                color: white;
                height: 30px;
            }
            QPushButton:hover {
                background-color: #5865F2;
            }
            QLabel, QComboBox, QTableWidget {
                color: white;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Logos
        logo_layout = QHBoxLayout()
        freebsd_logo = QLabel()
        freebsd_logo.setPixmap(QPixmap("freebsd_logo.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        bitcoin_logo = QLabel()
        bitcoin_logo.setPixmap(QPixmap("bitcoin_logo.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        logo_layout.addWidget(freebsd_logo)
        logo_layout.addStretch()
        logo_layout.addWidget(bitcoin_logo)
        layout.addLayout(logo_layout)

        # Buttons and Labels
        self.select_button = QPushButton("Select Folder")
        self.select_button.clicked.connect(self.select_folder)
        self.convert_button = QPushButton("Convert Images")
        self.convert_button.clicked.connect(self.convert_images)
        self.convert_button.setEnabled(False)
        self.status_label = QLabel()
        self.copy_button = QPushButton("Copy Error Log")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setEnabled(False)
        self.file_list_table = QTableWidget(10, 1)  # initialize with 10 rows and 1 column
        self.file_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.file_list_table.setHorizontalHeaderLabels(["Files"])
        self.file_list_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)  # enable vertical scrollbar
        self.format_combobox = QComboBox()
        self.format_combobox.addItems(["png", "jpg", "jpeg", "gif"])
        layout.addWidget(self.select_button)
        layout.addWidget(self.file_list_table)
        layout.addWidget(self.format_combobox)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.copy_button)

    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory()
        if self.folder:
            self.file_list = [f for f in os.listdir(self.folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            num_files = len(self.file_list)
            num_columns = (num_files + 9) // 10  # round up to nearest 10
            self.file_list_table.setColumnCount(num_columns)
            for i, file in enumerate(self.file_list):
                row = i % 10
                column = i // 10
                self.file_list_table.setItem(row, column, QTableWidgetItem(file))
            self.convert_button.setEnabled(True)
        else:
            self.status_label.setText("No folder selected")

    def convert_images(self):
        output_folder = QFileDialog.getExistingDirectory()
        if output_folder:
            output_format = self.format_combobox.currentText()
            for filename in self.file_list:
                try:
                    img = Image.open(os.path.join(self.folder, filename))
                    img = img.convert('RGB')  # ensure image is in RGB mode
                    img.thumbnail((800, 800))
                    base_filename, _ = os.path.splitext(filename)
                    img.save(os.path.join(output_folder, base_filename + '.' + output_format))
                except Exception as e:
                    error_message = f"Error converting {filename}: {str(e)}\n{traceback.format_exc()}"
                    self.status_label.setText(error_message)
                    self.copy_button.setEnabled(True)
                    return
            self.status_label.setText("Images converted and moved to: " + output_folder)
        else:
            self.status_label.setText("No output folder selected")

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.status_label.text())

app = QApplication([])
window = ImageConverter()
window.show()
app.exec()
