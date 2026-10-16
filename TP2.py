import sys
import json
import maya.cmds as cmds
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog


class MessageBoard(QWidget):

    def __init__(self): # Constructeur
        super().__init__()  # Constructeur QWidget

        self.setWindowTitle("Outliner Organiser")

        self.create_ui()
        self.create_json_find()
        self.create_checkbox()
        self.button()
        
    def create_ui(self):
        self.layout = QVBoxLayout(self)
        label = QLabel("Enter JSON path")
        self.layout.addWidget(label)

        self.message = QtWidgets.QLineEdit()
        self.message.setFixedSize(400, 40)
        self.layout.addWidget(self.message)


    def create_json_find(self):
        #faire bouton qui ouvre explorateur de fichier
        json_button = QtWidgets.QPushButton()
        self.layout.addWidget(json_button)
        json_button.setText("Find JSON in file explorer")
        json_button.clicked.connect(self.load_json)

        
    def load_json(self):
        json_path, _ = QFileDialog.getOpenFileName(None, "Select JSON file","", 
                                                    "Fichiers JSON (*.json)")
        if json_path:
            self.path = Path(json_path)

            try:
                with self.path.open("r", encoding="utf-8") as fichier:
                    self.data = json.load(fichier)
                    # Affiche le path obtenu dans la zone de texte
                    self.message.setText(str(self.path))

            # Erreur si incapable de lire le fichier
            except json.JSONDecodeError:
                print("Error, unable to read JSON file.")
                sys.exit()

            # Message d'erreur pour tout autre problème 
            except Exception as j:
                print(f"Error, JSON file {j} cannot be executed")
                sys.exit()

                # Va chercher le nom du fichier
                # Convertis tout les lettres en minuscules
                filename = path.stem.lower()


    def button(self):
        button = QtWidgets.QPushButton()
        self.layout.addWidget(button)
        button.setText("APPLY")

     
    def create_checkbox(self):
        # Nom et configuration des checkbox
        self.checkbox_selected = QtWidgets.QCheckBox("Apply on selected only")
        self.checkbox_color = QtWidgets.QCheckBox("Apply colors")
        self.checkbox_reorder = QtWidgets.QCheckBox("Apply reorder")

        # Ajoute les checkbox dans l'interface
        self.layout.addWidget(self.checkbox_selected)
        self.layout.addWidget(self.checkbox_color)
        self.layout.addWidget(self.checkbox_reorder)



    def verify_checkbox(self):
        #if self.button.clicked.connect(self.button):
        if self.checkbox_selected.isChecked():
            
            objects = cmds.ls(selection=True, type="transform", long=True) or []
        else:
            objects = cmds.ls(type="transform", long=True) or []

            #return objects

        if self.checkbox_reorder.isChecked():
            self.reorder_maya(objects)
        if self.checkbox_color.isChecked():
            self.color_maya(objects)


    def selected_maya(self, objects):
        # Get selected objects
        selected_objects = cmds.ls(select=True)

        if not selected_objects:
            print("No objects selected.")
            return


    # def reorder_maya(json_path):
    #     #for prefix in mapping.items():
    #         #item = data[i]
    #         #cmds.SM (ch=True, o=True, r=1.3)
    #         #select -r SM_
    #         #QSortFilterProxyModel
    #     for i in data(json):
    #         prefix = ("SM_", "FX_", "LGT_")

    def color_maya(self):
        #for obj in cmds.ls(type='transform'):
        prefix = self.data
        #cmds.ls( 'SM_', ap=True )
        for obj in object:
            # Extract base name
            base_name = obj.split("|")[-1] 

            for prefix, rgb in prefix.items():
                if base_name.startswith(prefix): 
                    #cmds.select(obj)
                    #cmds.hyperShade(outlinerColor=[1, 0, 0])
                    cmds.setAttr(obj + ".useOutlinerColor", 1)
                    cmds.setAttr(obj + ".outlinerColor", rgb[0], rgb[1], rgb[2], type="double3")

###CTRLz

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()

# cool links
#https://help.autodesk.com/view/MAYAUL/2017/CHS/?guid=__files_GUID_3F96AF53_A47E_4351_A86A_396E7BFD6665_htm
#https://download.autodesk.com/us/maya/maya_2014_gettingstarted/index.html?url=files/Using_Python_in_Maya_Entering_Python_commands.htm,topicNumber=d30e44398
#https://help.autodesk.com/cloudhelp/ENU/MayaCRE-Tech-Docs/CommandsPython/outlinerEditor.html
#https://www.youtube.com/watch?v=ul73LAOjj8k
#https://www.youtube.com/watch?v=uBctU-a_9JI
#https://vimeo.com/122424605?turnstile=1.iBWppgfN2LAtIz1q_YcuizQzVbWHpd4941ngccaSDdwcECOYLkwTHW-kNTiY1AdmGZKBdoPzBPlwcrs2qpBeCjunEVTSLpXsuNzu5XVfVpaPrn6ka6bgaPlUMYdvCuHxax4Wc1jEDiIqUKpxDTSR5_iXekYn6Eg7lslQb8jqPbEvuWzIgLRrTwRHx6oXDzW-ShRuFgfjoNiEr6QzVz9gJQgOfzbBEKkCyW-h-XVlcdK6018Crk56pHGADipSAnu2H1YVYXpGwz08CsCae5_onY4EGqOp6eVJKQjbdj8D_O_7b_xPvZ-dlnfTTkuq7fzyD-_gIMiducNxSuTKm7yXRc0ML7UkHqSUrCGXVSeQ8UB63mC8niIWcPcBU9QfRx5WtQ18Lk7vdijpnR5l-muBClZGQhw5JgMLjI1zZkbyRBdRvl8iCir0mXHuUe_AajPMDcIfBuCEk5lnUUvHAob4nOUa5b0otTgyDyKwadeVuEFFsk4nVbadSmSjWtfILBxFRRv_Bj1AvcJIWYTTSm31kBzDjbOmKRxuPzpPEIMeqGaRtAR_r9VqhtyVaiSa7Gl8WjKL9vMlKRv5zuhUVF7fL7_xZnKxzBr0GZcx6oAbsfI2n-blZTrvaKwtPugINm_a2izNUkLI4bQAHo5rz8EOtg.DB6j4rYRMenPEr5xWZaidQ.66ea8c2f655098b0273f393364ae6cd0611bf24b64f1d85bd49a890a565ff503
#https://forums.autodesk.com/t5/maya-programming-forum/how-to-set-quot-use-outliner-color-quot-with-python/td-p/11445228
#https://doc.qt.io/qt-6/layout.html
#https://www.pythonguis.com/tutorials/pyside6-widgets/#qcheckbox-adding-checkboxes-to-your-pyside6-app
