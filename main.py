import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QTableWidget, QTableWidgetItem
import re
import smtplib
from smtplib import SMTPException

def is_valid_email(email):
    """Basit bir e-posta formatı doğrulaması. Gerekirse SMTP üzerinden kontrol eklenebilir."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

class EmailSenderThread(QThread):
    success_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)

    def __init__(self, send_from_mail, send_from_password, subject, main_text_template, recipients):
        super().__init__()
        self.send_from_mail = send_from_mail
        self.send_from_password = send_from_password
        self.subject = subject
        self.main_text_template = main_text_template
        self.recipients = recipients

    def run(self):
        success_count = 0
        error_messages = []

        for name, email in self.recipients:
            main_text = f"Merhabalar! {name}.\n\n" + self.main_text_template.format(name=name)
            if self.send_email(email, self.subject, main_text, self.send_from_mail, self.send_from_password):
                success_count += 1
            else:
                error_messages.append(f"{email} - Geçersiz e-posta adresi.")

        self.success_signal.emit(success_count)

        if error_messages:
            self.error_signal.emit("\n".join(error_messages))

    def send_email(self, send_to_mail, subject, main_text, send_from_mail, send_from_password):
        try:
            msg = MIMEMultipart()
            msg['From'] = send_from_mail
            msg['To'] = send_to_mail
            msg['Subject'] = subject
            msg.attach(MIMEText(main_text, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(send_from_mail, send_from_password)

            server.sendmail(send_from_mail, send_to_mail, msg.as_string())
            server.quit()

            print(f"Email sent to {send_to_mail}")
            return True
        except Exception as e:
            print(f"Error sending email to {send_to_mail}: {e}")
            return False


class EmailAutomationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('E-posta Otomasyon Sistemi')
        self.setGeometry(100, 100, 600, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.email_label = QLabel('Gönderen E-posta Adresi:')
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText('Örnek: ornek@domain.com')

        self.password_label = QLabel('Gönderen E-posta Şifresi:')
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('E-posta şifrenizi girin...')
        self.password_input.setEchoMode(QLineEdit.Password)

        self.subject_label = QLabel('E-posta Konusu:')
        self.subject_input = QLineEdit(self)
        self.subject_input.setPlaceholderText('Konu başlığını girin...')

        self.main_text_label = QLabel('E-posta İçeriği:')
        self.main_text_input = QTextEdit(self)
        self.main_text_input.setPlaceholderText('E-posta içeriğinizi yazın...')

        self.recipients_table = QTableWidget(self)
        self.recipients_table.setColumnCount(2)
        self.recipients_table.setHorizontalHeaderLabels(['Ad', 'E-posta'])
        self.recipients_table.setRowCount(1)

        self.add_button = QPushButton('Alıcı Ekle', self)
        self.add_button.clicked.connect(self.add_recipient)

        self.send_button = QPushButton('E-posta Gönder', self)
        self.send_button.clicked.connect(self.send_bulk_emails)

        self.success_label = QLabel('', self)
        self.success_label.setText('')

        self.error_label = QLabel('', self)
        self.error_label.setText('')

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)
        layout.addWidget(self.main_text_label)
        layout.addWidget(self.main_text_input)
        layout.addWidget(self.recipients_table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.send_button)
        layout.addWidget(self.success_label)
        layout.addWidget(self.error_label)

        self.setLayout(layout)

    def add_recipient(self):
        current_row_count = self.recipients_table.rowCount()
        self.recipients_table.setRowCount(current_row_count + 1)

    def send_bulk_emails(self):
        send_from_mail = self.email_input.text()
        send_from_password = self.password_input.text()
        subject = self.subject_input.text()
        main_text_template = self.main_text_input.toPlainText()

        if not send_from_mail or not send_from_password or not subject or not main_text_template:
            self.success_label.setText("Eksik bilgi var. Lütfen tüm alanları doldurun.")
            return

        recipients = []

        for row in range(self.recipients_table.rowCount()):
            name_item = self.recipients_table.item(row, 0)
            email_item = self.recipients_table.item(row, 1)

            if name_item and email_item:
                name = name_item.text()
                email = email_item.text()


                if not is_valid_email(email):
                    print(f"E-posta formatı hatalı: {email}")
                    continue 

                recipients.append((name, email))

        if not recipients:
            self.success_label.setText("Geçerli e-posta adresi yok!")
            return

        self.sender_thread = EmailSenderThread(send_from_mail, send_from_password, subject, main_text_template, recipients)
        self.sender_thread.success_signal.connect(self.update_success_count)
        self.sender_thread.error_signal.connect(self.update_error_messages)
        self.sender_thread.start()

    def update_success_count(self, success_count):
        self.success_label.setText(f"Başarıyla {success_count} e-posta gönderildi.")

    def update_error_messages(self, error_messages):
        self.error_label.setText(f"Hatalı e-posta adresleri:\n{error_messages}")
        self.error_label.setStyleSheet("color: red;")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailAutomationApp()
    window.show()
    sys.exit(app.exec_())
