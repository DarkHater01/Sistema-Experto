import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt

class InferenceEngine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inference Engine")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0; color: #333333;")

        # Reglas
        self.rules = [
            
    {"IF": [("Mandíbulas", "No"), ("Número de aletas", "Impar"), ("Esqueleto", "Cartilaginoso"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Agnatos")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "Par"), ("Esqueleto", "Cartilaginoso"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Condricties")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "Par"), ("Esqueleto", "Óseo"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Osteicties")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "No"), ("Esqueleto", "Óseo"), ("Escamas", "No"), 
            ("Respiración", "Branquial"), ("Piel", "Lisa y húmeda"), ("Temperatura", "Variable"), 
            ("Reproducción", "Ovíparo"), ("Metamorfosis", "Sí")], "THEN": ("Clase", "Anfibios")},
    {"IF": [("Clase", "Anfibios"), ("Cuerpo", "Alargado"), ("Cola", "Sí"), ("Miembros", "Sí")], "THEN": ("Orden", "Urodelos")},
    {"IF": [("Mandíbulas", "Sí"), ("Aletas", "No"), ("Piel", "Escamas duras"), ("Temperatura", "Variable"), 
            ("Respiración", "Pulmonar"), ("Esqueleto", "Óseo"), ("Reproducción", "Ovíparo")], "THEN": ("Clase", "Reptiles")},
    {"IF": [("Clase", "Reptiles"), ("Cuerpo", "Alargado"), ("Miembros", "No")], "THEN": ("Orden", "Ofidios")},
    {"IF": [("Mandíbulas", "Sí"), ("Esqueleto", "Óseo"), ("Aletas", "No"), ("Escamas", "No"), 
            ("Respiración", "Pulmonar"), ("Piel", "Plumas"), ("Temperatura", "Constante"), 
            ("Reproducción", "Ovíparo"), ("Poseen", "Pico y Cloaca")], "THEN": ("Clase", "Aves")},
    {"IF": [("Clase", "Aves"), ("Orden", "Carenadas"), ("Patas", "Palmeadas"), 
            ("Plumaje", "Espeso"), ("Habilidad", "Nadar")], "THEN": ("Suborden", "Palmípedas")},
    {"IF": [("Mandíbulas", "Sí"), ("Esqueleto", "Óseo"), ("Respiración", "Pulmonar"), 
            ("Piel", "Pelos"), ("Temperatura", "Constante"), ("Escamas", "No"), 
            ("Glándulas mamarias", "Sí")], "THEN": ("Clase", "Mamíferos")}
]


        # Hechos
        self.facts = [
            ("Mandíbulas", "Sí"),
            ("Número de aletas", "Par"),
            ("Esqueleto", "Óseo"),
            ("Escamas", "Sí"),
            ("Respiración", "Branquial"),
            ("Hábitat", "Agua")
        ]

        # Crear la interfaz gráfica
        self.create_ui()

    def create_ui(self):
        # Tabla de hechos
        self.facts_table = QTableWidget(len(self.facts), 2)
        self.facts_table.setHorizontalHeaderLabels(["Atributo", "Valor"])
        self.facts_table.setStyleSheet("background-color: #ffffff; color: #333333;")
        self.facts_table.setFont(QFont("Arial", 12))
        self.facts_table.setAlternatingRowColors(True)
        self.facts_table.setColumnWidth(0, 200)
        self.facts_table.setColumnWidth(1, 200)

        for i, fact in enumerate(self.facts):
            self.facts_table.setItem(i, 0, QTableWidgetItem(fact[0]))
            self.facts_table.setItem(i, 1, QTableWidgetItem(fact[1]))

        # Entrada de un nuevo hecho
        new_fact_layout = QHBoxLayout()
        self.new_fact_label = QLabel("Nuevo hecho:")
        self.new_fact_label.setFont(QFont("Arial", 12))
        self.new_fact_attribute = QLineEdit()
        self.new_fact_attribute.setFont(QFont("Arial", 12))
        self.new_fact_value = QLineEdit()
        self.new_fact_value.setFont(QFont("Arial", 12))
        self.add_fact_button = QPushButton("Agregar hecho")
        self.add_fact_button.setFont(QFont("Arial", 12))
        self.add_fact_button.setStyleSheet("background-color: #4CAF50; color: #ffffff; padding: 5px 10px;")
        self.add_fact_button.clicked.connect(self.add_fact)
        new_fact_layout.addWidget(self.new_fact_label)
        new_fact_layout.addWidget(self.new_fact_attribute)
        new_fact_layout.addWidget(self.new_fact_value)
        new_fact_layout.addWidget(self.add_fact_button)

        # Verificar hipótesis
        hypothesis_layout = QHBoxLayout()
        self.hypothesis_label = QLabel("Verificar hipótesis:")
        self.hypothesis_label.setFont(QFont("Arial", 12))
        self.hypothesis_attribute = QLineEdit()
        self.hypothesis_attribute.setFont(QFont("Arial", 12))
        self.hypothesis_value = QLineEdit()
        self.hypothesis_value.setFont(QFont("Arial", 12))
        self.verify_hypothesis_button = QPushButton("Verificar")
        self.verify_hypothesis_button.setFont(QFont("Arial", 12))
        self.verify_hypothesis_button.setStyleSheet("background-color: #2196F3; color: #ffffff; padding: 5px 10px;")
        self.verify_hypothesis_button.clicked.connect(self.verify_hypothesis)
        hypothesis_layout.addWidget(self.hypothesis_label)
        hypothesis_layout.addWidget(self.hypothesis_attribute)
        hypothesis_layout.addWidget(self.hypothesis_value)
        hypothesis_layout.addWidget(self.verify_hypothesis_button)

        # Mostrar resultados
        self.result_label = QLabel()
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setStyleSheet("color: #4CAF50;")

        # Diseño de la interfaz
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Hechos:"))
        main_layout.addWidget(self.facts_table)
        main_layout.addLayout(new_fact_layout)
        main_layout.addLayout(hypothesis_layout)
        main_layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_fact(self):
        new_fact = (
            self.new_fact_attribute.text(),
            self.new_fact_value.text()
        )
        self.facts.append(new_fact)
        row = self.facts_table.rowCount()
        self.facts_table.setRowCount(row + 1)
        self.facts_table.setItem(row, 0, QTableWidgetItem(new_fact[0]))
        self.facts_table.setItem(row, 1, QTableWidgetItem(new_fact[1]))
        self.new_fact_attribute.clear()
        self.new_fact_value.clear()

    def verify_hypothesis(self):
        goal = (
            self.hypothesis_attribute.text(),
            self.hypothesis_value.text()
        )
        result = self.backward_chaining(goal, self.rules, self.facts)
        if result:
            self.result_label.setText(f"El objetivo {goal} es verdadero basado en los hechos y reglas dadas.")
        else:
            self.result_label.setText(f"El objetivo {goal} no se puede inferir de los hechos y reglas dadas.")
        self.hypothesis_attribute.clear()
        self.hypothesis_value.clear()

    def backward_chaining(self, goal, rules, facts):
        if goal in facts:
            return True

        for rule in rules:
            if rule["THEN"] == goal:
                all_conditions_met = True
                for condition in rule["IF"]:
                    if not self.backward_chaining(condition, rules, facts):
                        all_conditions_met = False
                        break
                if all_conditions_met:
                    return True

        return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = InferenceEngine()
    engine.show()
    sys.exit(app.exec_())