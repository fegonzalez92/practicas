usuarios_noconfirmados = ["alicia","pedro", "carola"]
usuarios_confirmados = []

while usuarios_noconfirmados:
    usuario_actual = usuarios_noconfirmados.pop()
    print("verificando usuario.." + usuario_actual.title())
    usuarios_confirmados.append(usuario_actual)

#mostrar usuarios confirmados
print("los siguientes usuarios fueron confirmados")
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.tittle())
