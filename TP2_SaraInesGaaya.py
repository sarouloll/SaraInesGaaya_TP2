from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox, QFileDialog
from PySide6 import QtWidgets
from pathlib import Path


class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__()  # Constructeur QWidget
        self.setWindowTitle("Outliner Organiser")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Enter JSON path")
        #label.resize(50, 10)
        layout.addWidget(label)
        
        self.message = QtWidgets.QTextEdit()
        layout.addWidget(self.message)

        # button = QtWidgets.QPushButton()
        # layout.addWidget(button)
        # button.setText("OK")

        # button.clicked.connect(self.on_click)
        

    # def on_click(self):
    #     print("on click called")
    #     message = self.message.toPlainText()
    #     QMessageBox.information (self, "message", message)
        
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()

#https://help.autodesk.com/view/MAYAUL/2017/CHS/?guid=__files_GUID_3F96AF53_A47E_4351_A86A_396E7BFD6665_htm
#https://download.autodesk.com/us/maya/maya_2014_gettingstarted/index.html?url=files/Using_Python_in_Maya_Entering_Python_commands.htm,topicNumber=d30e44398
#https://help.autodesk.com/cloudhelp/ENU/MayaCRE-Tech-Docs/CommandsPython/outlinerEditor.html
#https://www.youtube.com/watch?v=ul73LAOjj8k
#https://www.youtube.com/watch?v=uBctU-a_9JI
#https://vimeo.com/122424605?turnstile=1.iBWppgfN2LAtIz1q_YcuizQzVbWHpd4941ngccaSDdwcECOYLkwTHW-kNTiY1AdmGZKBdoPzBPlwcrs2qpBeCjunEVTSLpXsuNzu5XVfVpaPrn6ka6bgaPlUMYdvCuHxax4Wc1jEDiIqUKpxDTSR5_iXekYn6Eg7lslQb8jqPbEvuWzIgLRrTwRHx6oXDzW-ShRuFgfjoNiEr6QzVz9gJQgOfzbBEKkCyW-h-XVlcdK6018Crk56pHGADipSAnu2H1YVYXpGwz08CsCae5_onY4EGqOp6eVJKQjbdj8D_O_7b_xPvZ-dlnfTTkuq7fzyD-_gIMiducNxSuTKm7yXRc0ML7UkHqSUrCGXVSeQ8UB63mC8niIWcPcBU9QfRx5WtQ18Lk7vdijpnR5l-muBClZGQhw5JgMLjI1zZkbyRBdRvl8iCir0mXHuUe_AajPMDcIfBuCEk5lnUUvHAob4nOUa5b0otTgyDyKwadeVuEFFsk4nVbadSmSjWtfILBxFRRv_Bj1AvcJIWYTTSm31kBzDjbOmKRxuPzpPEIMeqGaRtAR_r9VqhtyVaiSa7Gl8WjKL9vMlKRv5zuhUVF7fL7_xZnKxzBr0GZcx6oAbsfI2n-blZTrvaKwtPugINm_a2izNUkLI4bQAHo5rz8EOtg.DB6j4rYRMenPEr5xWZaidQ.66ea8c2f655098b0273f393364ae6cd0611bf24b64f1d85bd49a890a565ff503
#https://forums.autodesk.com/t5/maya-programming-forum/how-to-set-quot-use-outliner-color-quot-with-python/td-p/11445228
#https://doc.qt.io/qt-6/layout.html