import sys
import dns.resolver
from PyQt6.QtWidgets import QApplication, QMainWindow
from layout import Ui_MainWindow  # Importa a interface gerada

class DNSChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar o botão à função de consulta DNS
        self.ui.pushButton.clicked.connect(self.check_dns)

    def check_dns(self):
        domain = self.ui.lineEdit.text()  # Obtém o domínio inserido
        record_type = self.ui.comboBox.currentText()  # Obtém o tipo de registro escolhido

        try:
            answers = dns.resolver.resolve(domain, record_type)
            result_text = f"Resultados para {domain} ({record_type}):\n"
            for rdata in answers:
                result_text += f"{rdata}\n"
        except Exception as e:
            result_text = f"Erro: {str(e)}"

        self.ui.textEdit.setPlainText(result_text)  # Exibe os resultados

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DNSChecker()
    window.show()
    sys.exit(app.exec())

