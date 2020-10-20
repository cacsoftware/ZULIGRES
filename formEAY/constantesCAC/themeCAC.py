


import formEAY.constantesCAC.coloresCAC as color

class FormularioCAC():
    def __init__(self, frm_fondoColor=color.gris10, frm_letraColor=color.negro, panelControles_fondoColor=color.gris30,
                 panelControles_letraColor=color.negro,
                 labelInformacion_fondoColor=color.gris10, labelInformacion_letraColor=color.negro,
                 labelTipoFormulario_fondoColor=color.azul, labelTipoFormulario_letraColor=color.blanco,
                 panelFrame_fondoColor=color.gris20, panelFrame_letraColor=color.negro
                 ):
        self.frm_fondoColor=frm_fondoColor
        self.frm_letraColor=frm_letraColor

        self.panelControles_fondoColor=panelControles_fondoColor
        self.panelControles_letraColor=panelControles_letraColor

        self.labelInformacion_fondoColor=labelInformacion_fondoColor
        self.labelInformacion_letraColor=labelInformacion_letraColor

        self.labelTipoFormulario_fondoColor=labelTipoFormulario_fondoColor
        self.labelTipoFormulario_letraColor=labelTipoFormulario_letraColor

        self.panelFrame_fondoColor=panelFrame_fondoColor
        self.panelFrame_letraColor=panelFrame_letraColor

# frm_fondoColor=color.gris10
# frm_letraColor=color.negro
# panelControles_fondoColor=color.gris30
# panelControles_letraColor=color.negro
# labelInformacion_fondoColor=color.gris20
# labelInformacion_letraColor=color.negro

frm_buscarCliente=FormularioCAC(panelControles_fondoColor=color.blanco)

panelControles_fondoColor=color.gris30
frm_nuevoCliente=FormularioCAC(labelTipoFormulario_fondoColor=color.azulMar
                               )

frm_editarCliente=FormularioCAC(labelTipoFormulario_fondoColor=color.rojo
                               )

frm_nuevoProducto=FormularioCAC(labelTipoFormulario_fondoColor=color.azulMar
                                )