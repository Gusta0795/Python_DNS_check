import sys
import dns.resolver
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel, QComboBox

class DNSChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DNS Propagation Checker")
        self.setGeometry(100, 100, 500, 300)

        # Criando a interface manualmente
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.label = QLabel("Digite o domínio:")
        self.input_domain = QLineEdit()
        self.input_domain.setPlaceholderText("exemplo.com")

        self.label_record = QLabel("Escolha o tipo de registro:")
        self.combo_record = QComboBox()
        self.combo_record.addItems(["A", "CNAME", "MX", "TXT", "NS", "AAAA"])

        self.button = QPushButton("Verificar DNS")
        self.button.clicked.connect(self.check_dns)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)

        # Adicionando os widgets ao layout
        layout.addWidget(self.label)
        layout.addWidget(self.input_domain)
        layout.addWidget(self.label_record)
        layout.addWidget(self.combo_record)
        layout.addWidget(self.button)
        layout.addWidget(self.result_box)

        central_widget.setLayout(layout)

    def check_dns(self):
        domain = self.input_domain.text().strip()
        record_type = self.combo_record.currentText()

        if not domain:
            self.result_box.setPlainText("Erro: O domínio não pode estar vazio.")
            return

        try:
            answers = dns.resolver.resolve(domain, record_type)
            result_text = f"Resultados para {domain} ({record_type}):\n"
            for rdata in answers:
                result_text += f"{rdata}\n"
        except Exception as e:
            result_text = f"Erro: {str(e)}"

        self.result_box.setPlainText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DNSChecker()
    window.show()
    sys.exit(app.exec())
