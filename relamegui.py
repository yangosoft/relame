
# -*- coding: utf-8 -*-

# RELameGUI es un pequeño script escrito en Python que permite recodificar mp3s de una forma sencilla usando lame y el módulo para Python eyeD3

###############################################################################
#  Copyright (C) 2002-2007  Yango http://usuarios.lycos.es/sisar
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
################################################################################

from qt import *
import sys
import os
import eyeD3

global version 
version = "0.0.2"	
class frmProgreso(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("frmProgreso")

        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.sizePolicy().hasHeightForWidth()))
        self.setMinimumSize(QSize(600,50))
        self.setSizeGripEnabled(0)


        self.progressBar1 = QProgressBar(self,"progressBar1")
        self.progressBar1.setGeometry(QRect(20,10,511,23))

        self.languageChange()

        self.resize(QSize(600,50).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Progreso"))


    def __tr(self,s,c = None):
        return qApp.translate("frmProgreso",s,c)






class relamegui(QMainWindow):
    
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        if not name:
            self.setName("relamegui")

        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred,0,0,self.sizePolicy().hasHeightForWidth()))

        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.btnGuardar = QPushButton(self.centralWidget(),"btnGuardar")
        self.btnGuardar.setGeometry(QRect(548,106,43,24))

        self.textLabel3 = QLabel(self.centralWidget(),"textLabel3")
        self.textLabel3.setGeometry(QRect(11,136,125,20))

        self.textLabel4 = QLabel(self.centralWidget(),"textLabel4")
        self.textLabel4.setGeometry(QRect(11,216,125,27))

        self.textLabel2 = QLabel(self.centralWidget(),"textLabel2")
        self.textLabel2.setGeometry(QRect(11,74,173,26))

        self.btnAbrir = QPushButton(self.centralWidget(),"btnAbrir")
        self.btnAbrir.setGeometry(QRect(548,44,43,24))

        self.textLabel1 = QLabel(self.centralWidget(),"textLabel1")
        self.textLabel1.setGeometry(QRect(11,11,125,27))

        self.lineEdit2 = QLineEdit(self.centralWidget(),"lineEdit2")
        self.lineEdit2.setGeometry(QRect(11,107,510,22))

        self.btnIniciar = QPushButton(self.centralWidget(),"btnIniciar")
        self.btnIniciar.setGeometry(QRect(530,300,60,24))

        self.lineEdit1 = QLineEdit(self.centralWidget(),"lineEdit1")
        self.lineEdit1.setGeometry(QRect(11,45,510,22))

        self.listBitrate = QComboBox(0,self.centralWidget(),"listBitrate")
        self.listBitrate.setGeometry(QRect(11,162,125,22))

        self.listBitrate_2 = QComboBox(0,self.centralWidget(),"listBitrate_2")
        self.listBitrate_2.setGeometry(QRect(11,249,125,22))

        self.groupBox1 = QGroupBox(self.centralWidget(),"groupBox1")
        self.groupBox1.setGeometry(QRect(330,130,260,135))

        self.textLabel3_2 = QLabel(self.groupBox1,"textLabel3_2")
        self.textLabel3_2.setGeometry(QRect(10,20,130,21))

        self.listBitrateMaximo = QComboBox(0,self.groupBox1,"listBitrateMaximo")
        self.listBitrateMaximo.setGeometry(QRect(10,40,111,20))

        self.ckbVbrnew = QCheckBox(self.groupBox1,"ckbVbrnew")
        self.ckbVbrnew.setGeometry(QRect(10,70,90,20))
        self.ckbVbrnew.setChecked(1)

        self.buttonGroup1 = QButtonGroup(self.centralWidget(),"buttonGroup1")
        self.buttonGroup1.setGeometry(QRect(160,130,120,90))

        self.rbConstante = QRadioButton(self.buttonGroup1,"rbConstante")
        self.rbConstante.setGeometry(QRect(10,60,90,20))

        self.rbVariable = QRadioButton(self.buttonGroup1,"rbVariable")
        self.rbVariable.setGeometry(QRect(10,40,90,20))

        self.rbMedia = QRadioButton(self.buttonGroup1,"rbMedia")
        self.rbMedia.setGeometry(QRect(10,20,90,20))

        self.fileExitAction = QAction(self,"fileExitAction")
        self.aboutAction = QAction(self,"aboutAction")
	
	#about box
        self.aboutAction=QAction(self, "About")
        self.aboutAction.setText("About")
        self.aboutAction.setMenuText("&About")
        self.aboutAction.setStatusTip("About")
        self.connect(self.aboutAction, SIGNAL("activated()"), self.slotAbout)
	#



        self.MenuBar = QMenuBar(self,"MenuBar")


        self.fileMenu = QPopupMenu(self)
        self.fileExitAction.addTo(self.fileMenu)
	self.connect(self.fileExitAction, SIGNAL("activated()"), self.slotMenuExit)
        self.MenuBar.insertItem(QString(""),self.fileMenu,1)

        self.unnamed = QPopupMenu(self)
        self.aboutAction.addTo(self.unnamed)
        self.MenuBar.insertItem(QString(""),self.unnamed,2)


        self.languageChange()

        self.resize(QSize(604,377).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)
	
    def slotAbout(self):
	QMessageBox.about(ifrmGui, "RELame " + version, u"Un pequeño GUI para lame que permite recodificar mp3s fácilmente.\n\nYango\nhttp://usuarios.lycos.es/sisar")

    def slotMenuExit(self):
	exit()

    def languageChange(self):
        self.setCaption(self.__tr("RELame"))
        self.btnGuardar.setText(self.__tr("..."))
        self.textLabel3.setText(self.__tr("Bitrate (-b):"))
        self.textLabel4.setText(self.__tr("Calidad (-q):"))
        self.textLabel2.setText(self.__tr("Destino:"))
        self.btnAbrir.setText(self.__tr("..."))
        self.textLabel1.setText(self.__tr("Ruta a los archivos:"))
        self.btnIniciar.setText(self.__tr("&Iniciar"))
        self.btnIniciar.setAccel(QKeySequence(self.__tr("Alt+I")))
        self.listBitrate.clear()
        self.listBitrate.insertItem(self.__tr("32"))
        self.listBitrate.insertItem(self.__tr("40"))
        self.listBitrate.insertItem(self.__tr("48"))
        self.listBitrate.insertItem(self.__tr("56"))
        self.listBitrate.insertItem(self.__tr("64"))
        self.listBitrate.insertItem(self.__tr("80"))
        self.listBitrate.insertItem(self.__tr("96"))
        self.listBitrate.insertItem(self.__tr("112"))
        self.listBitrate.insertItem(self.__tr("128"))
        self.listBitrate.insertItem(self.__tr("160"))
        self.listBitrate.insertItem(self.__tr("192"))
        self.listBitrate.insertItem(self.__tr("224"))
        self.listBitrate.insertItem(self.__tr("256"))
        self.listBitrate.insertItem(self.__tr("320"))
        self.listBitrate.setCurrentItem(10)
        self.listBitrate_2.clear()
        self.listBitrate_2.insertItem(self.__tr("0"))
        self.listBitrate_2.insertItem(self.__tr("1"))
        self.listBitrate_2.insertItem(self.__tr("2"))
        self.listBitrate_2.insertItem(self.__tr("3"))
        self.listBitrate_2.insertItem(self.__tr("4"))
        self.listBitrate_2.insertItem(self.__tr("5"))
        self.listBitrate_2.insertItem(self.__tr("6"))
        self.listBitrate_2.insertItem(self.__tr("7"))
        self.listBitrate_2.insertItem(self.__tr("8"))
        self.listBitrate_2.insertItem(self.__tr("9"))
        self.listBitrate_2.setCurrentItem(2)
        self.groupBox1.setTitle(self.__tr("VBR y ABR"))
        self.textLabel3_2.setText(self.__trUtf8("\x42\x69\x74\x72\x61\x74\x65\x20\x6d\xc3\xa1\x78\x69\x6d\x6f\x20\x28\x2d\x42\x29\x3a"))
        self.listBitrateMaximo.clear()
        self.listBitrateMaximo.insertItem(self.__tr("32"))
        self.listBitrateMaximo.insertItem(self.__tr("40"))
        self.listBitrateMaximo.insertItem(self.__tr("48"))
        self.listBitrateMaximo.insertItem(self.__tr("56"))
        self.listBitrateMaximo.insertItem(self.__tr("64"))
        self.listBitrateMaximo.insertItem(self.__tr("80"))
        self.listBitrateMaximo.insertItem(self.__tr("96"))
        self.listBitrateMaximo.insertItem(self.__tr("112"))
        self.listBitrateMaximo.insertItem(self.__tr("128"))
        self.listBitrateMaximo.insertItem(self.__tr("160"))
        self.listBitrateMaximo.insertItem(self.__tr("192"))
        self.listBitrateMaximo.insertItem(self.__tr("224"))
        self.listBitrateMaximo.insertItem(self.__tr("256"))
        self.listBitrateMaximo.insertItem(self.__tr("320"))
        self.listBitrateMaximo.setCurrentItem(10)
        self.ckbVbrnew.setText(self.__tr("VBR Nuevo"))
        self.buttonGroup1.setTitle(self.__tr("Tipo Bitrate:"))
        self.rbConstante.setText(self.__tr("Constante"))
        self.rbVariable.setText(self.__tr("Variable"))
        self.rbMedia.setText(self.__tr("Medio"))
        self.fileExitAction.setText(self.__tr("Exit"))
        self.fileExitAction.setMenuText(self.__tr("E&xit"))
        self.fileExitAction.setAccel(QString.null)
        self.aboutAction.setText(self.__tr("about"))
        self.aboutAction.setMenuText(self.__tr("about"))
        if self.MenuBar.findItem(1):
            self.MenuBar.findItem(1).setText(self.__tr("&File"))
        if self.MenuBar.findItem(2):
            self.MenuBar.findItem(2).setText(self.__tr("?"))


    def __tr(self,s,c = None):
        return qApp.translate("relamegui",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("relamegui",s,c,QApplication.UnicodeUTF8)


def copyTags(fromFile, toFile):
	print "Copiando tags..."
	tagsFrom = eyeD3.Tag()
	tagsTo = eyeD3.Tag()
	if (tagsFrom.link(fromFile) == False):
		return
	tagsTo.link(toFile)
	tagsTo.header.setVersion(eyeD3.ID3_V2_3)
	tagsTo.setArtist(tagsFrom.getArtist())
	tagsTo.setAlbum(tagsFrom.getAlbum())
	tagsTo.setDate(tagsFrom.getYear())
	tagsTo.setTitle(tagsFrom.getTitle())
	tagsTo.setTrackNum(tagsFrom.getTrackNum())
	tagsTo.update()
	print "Listo"
    

def recodificar(inPath, outPath, bitrate, quality, maxBitrate, vbrNew, cte, var, avg):
    
   
    renombrar=False
    argumentos="-h"
    argumentos+=" -q " + quality
    
    if(inPath==""):
	print u"Seleccione el directorio origen de los archivos"
	QMessageBox.critical(ifrmGui, u"Error", u"Seleccione el directorio origen de los archivos", QMessageBox.Ok)
        return  
    if(outPath==""):
	print u"Seleccione el directorio destino de los archivos"
	QMessageBox.critical(ifrmGui, u"Error", u"Seleccione el directorio destino de los archivos", QMessageBox.Ok)
        return 
    
    if(inPath==outPath):
	print u"El directorio origen y el directorio destino son el mismo!"
	QMessageBox.critical(ifrmGui, u"Advertencia", u"El directorio origen y el directorio destino son el mismo. Para no sobreescribir los archivos originales se renombrarán los nuevos archivos", QMessageBox.Ok)
	renombrar=True
    
    
    if not(inPath.endswith("/")):
	    inPath=inPath+"/"
	     
    if not(outPath.endswith("/")):
	    outPath=outPath+"/"
   
        
    if(var==True):
        argumentos +=" -B " + maxBitrate
        argumentos += " -b " + bitrate
	if(vbrNew==True):
        	argumentos += " --vbr-new "
    elif(avg==True):
        argumentos += " --abr " + bitrate
    elif(cte==True):
        argumentos += " -b " + bitrate
    else:
        print "Selecciona el método de codificación"
	QMessageBox.critical(ifrmGui, u"Error", u"Seleccione el método de codificación", QMessageBox.Ok)
        return
        
    argumentos=argumentos + " "
    print argumentos
   
    dirList=os.listdir(inPath)
    #print dirList
    frmprogreso= frmProgreso(ifrmGui)
    frmprogreso.show()
    frmprogreso.progressBar1.setTotalSteps=len(dirList)
    i=0
    for fname in dirList:
	i=i+1
	frmprogreso.progressBar1.setProgress(i)
	newname = fname.replace(" ", "_")
	if (renombrar==True):
		newname="["+str(bitrate)+"]" + newname
	fname=os.path.join(inPath,fname)
        #print fname
        if (str(fname).endswith(".mp3")):
            #print "outPath vale: " + str(outPath)
	    #print "newname vale: " + str(newname)
	    newname = os.path.join(outPath,newname)
            #print "despues del join: " + str(newname)
	    os.system("lame " + str(argumentos) + " '" + str(fname)+"' '" + str(newname) + "'")
	    copyTags(str(fname),str(newname))
	    #print "lame " + str(argumentos) + "'" + str(fname)+"' '" + str(newname) + "'"
        #else:
            #print "archivo descartado: " + fname

    frmprogreso.close()
    QMessageBox.information(ifrmGui, u"Terminado", u"Se han transcodificado todos los archivos", QMessageBox.Ok)
            
#acciones de los botones 
def btnIniciar():
	print  "path:" + str(ifrmGui.lineEdit1.text())
	print  "new path:" + str(ifrmGui.lineEdit2.text())
	print  "-b:" + str(ifrmGui.listBitrate.currentText())
	print  "-q:" + str(ifrmGui.listBitrate_2.currentText())
	print  "-B:" + str(ifrmGui.listBitrateMaximo.currentText())
	print  "VBR Nuevo:" + str(ifrmGui.ckbVbrnew.isChecked())
	print  "Cte:" + str(ifrmGui.rbConstante.isChecked())
	print  "Variable:" + str(ifrmGui.rbVariable.isChecked())
    	print  "Media:" + str(ifrmGui.rbMedia.isChecked())
   	recodificar(str(ifrmGui.lineEdit1.text()).strip() , str(ifrmGui.lineEdit2.text()).strip() , str(ifrmGui.listBitrate.currentText()).strip() ,str(ifrmGui.listBitrate_2.currentText()).strip() , str(ifrmGui.listBitrateMaximo.currentText()).strip() , ifrmGui.ckbVbrnew.isChecked() , ifrmGui.rbConstante.isChecked() , ifrmGui.rbVariable.isChecked() , ifrmGui.rbMedia.isChecked())
	
def btnAbrir():
	folder=QFileDialog.getExistingDirectory('',None,'Directorio Origen','Directorio Origen',1)
	ifrmGui.lineEdit1.setText(str(folder))
	
def btnGuardar():
	folder=QFileDialog.getExistingDirectory('',None,'Directorio Destino','Directorio Destino',1)
	ifrmGui.lineEdit2.setText(str(folder))
	


if __name__=="__main__":
	app = QApplication(sys.argv)
	
	QObject.connect(app,SIGNAL('lastWindowClosed()'),app,SLOT('quit()'))
	
	ifrmGui = relamegui()
	ifrmGui.show()
	
	ifrmGui.connect(ifrmGui.btnIniciar,SIGNAL('clicked()'),btnIniciar)
	ifrmGui.connect(ifrmGui.btnAbrir,SIGNAL('clicked()'),btnAbrir)
	ifrmGui.connect(ifrmGui.btnGuardar,SIGNAL('clicked()'),btnGuardar)

	app.exec_loop()
