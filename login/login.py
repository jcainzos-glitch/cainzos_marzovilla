import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Carga el archivo login.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))

class LoginScreen(MDScreen):
    
    def volver(self):
        self.manager.current = "inicio"
        
    def iniciar_sesion(self):
        self.manager.current = "home"

    def validar_correo(self, correo):

        if "@" in correo and "." in correo:
            print("Correo válido:", correo)
            return True
        else:
            print("Correo inválido:", correo)
            return False
        
        if self.ids.correo.text == "":
            print("El correo no puede estar vacío.")
            return False

        if not self.ids.correo.text in self.usuarios:
            print("El correo no está registrado.")
            return False

    def contraseña_correcta(self, correo, contraseña):
        
        if correo in self.usuarios and self.usuarios[correo] == contraseña:
            print("Contraseña correcta para el correo:", correo)
            return True
        else:
            print("Contraseña incorrecta para el correo:", correo)
            return False
        
