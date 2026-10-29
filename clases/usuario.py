class Usuario:
    def __init__(self, correo, contrasena):
        self.correo = correo
        self.contrasena = contrasena
 
    def correo_valido(self):
        return "@" in self.correo and "." in self.correo
 
    def contrasena_correcta(self, contrasena):
        return self.contrasena == contrasena
