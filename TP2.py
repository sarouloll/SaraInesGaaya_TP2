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
        self.data = None

        self.setWindowTitle("Outliner Organiser")   # Titre de la fenetre

        #Items à ajouter à la fenetre
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
        # Fonction qui ouvre explorateur de fichier
        json_button = QtWidgets.QPushButton() 
        self.layout.addWidget(json_button)  # Ajout du bouton
        json_button.setText("Find JSON in file explorer")
        json_button.clicked.connect(self.load_json) # Connection entre le bouton et la fonction load_json

        
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


    # Configuration du bouton principal
    def button(self):
        button = QtWidgets.QPushButton()
        self.layout.addWidget(button)
        button.setText("APPLY")

        # Relie bouton d'execution avec la fonction
        button.clicked.connect(self.verify_checkbox)

     
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
        cmds.undoInfo(openChunk=True) # CTRL Z 

        # Activation de la sélection
        if self.checkbox_selected.isChecked():
            objects = cmds.ls("SM_*", "FX_*", "LGT_*", selection=True)

        else:
            objects = cmds.ls("SM_*", "FX_*", "LGT_*")

        #Main logic de couleurs
        if self.checkbox_color.isChecked():
            prefix = self.data

            for obj in objects:

                for prefix, rgb in self.data.items():

                    if obj.startswith(prefix):
                        cmds.setAttr(obj + ".useOutlinerColor", 1)
                        cmds.setAttr(obj + ".outlinerColor", rgb[0], rgb[1], rgb[2], type="double3")


        if self.checkbox_reorder.isChecked():
            objects = sorted(objects)
            
            for obj in reversed(objects):
                cmds.reorder(obj, front=True) 

        cmds.undoInfo(closeChunk=True) # CTRL Z



def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()
