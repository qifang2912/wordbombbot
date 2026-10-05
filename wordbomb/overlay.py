from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

from word_finder import load_words, find_word
from keyboard_controller import type_word


class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.words = load_words()
        self.used_words = set()

        self.setWindowTitle("Word Bomb Helper")
        self.setFixedSize(350, 180)

        # Keep window above the browser
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint
        )

        # Fragment input
        self.fragment_label = QLabel("Input fragment:")

        self.fragment_input = QLineEdit()
        self.fragment_input.setPlaceholderText("Enter fragment...")

        # Generated word
        self.word_label = QLabel("Word:")
        self.word_display = QLabel("")

        # Clear button
        self.clear_button = QPushButton("Clear")

        # Main layout
        layout = QVBoxLayout()

        layout.addWidget(self.fragment_label)
        layout.addWidget(self.fragment_input)

        layout.addWidget(self.word_label)
        layout.addWidget(self.word_display)

        layout.addWidget(self.clear_button)

        self.setLayout(layout)

        # Pressing Enter generates and submits the next unused word
        self.fragment_input.returnPressed.connect(self.generate_word)

        # Clear resets the current fragment
        self.clear_button.clicked.connect(self.clear)

    def generate_word(self):
        fragment = self.fragment_input.text()

        word = find_word(
            fragment,
            self.words,
            self.used_words
        )

        if word:
            self.word_display.setText(word)

            # Send word to the game
            self.hide()
            type_word(word)
            self.show()

            # Return to input and select the current fragment
            self.fragment_input.setFocus()
            self.fragment_input.selectAll()

        else:
            self.word_display.setText("No unused word found")

    def clear(self):
        self.fragment_input.clear()
        self.word_display.clear()
        self.fragment_input.setFocus()