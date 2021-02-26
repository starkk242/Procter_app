#############Python Libraries#############################
import pynput
import socket
import os
import tempfile
import sys
import PySide2
import hashlib
from PySide2 import QtCore,QtWebEngineWidgets
from PySide2.QtWidgets import QApplication,QMessageBox,QGridLayout,QHBoxLayout,QLineEdit,QFormLayout,QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide2.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
from PySide2.QtCore import *
from PySide2.QtCore import QRect
from PySide2.QtCore import QUrl
from PySide2.QtGui import *
import qimage2ndarray
import cv2
import requests
import psutil
################ Fetching Face Recognition Harcascade file and Demo image file##################
if(not os.path.exists(tempfile.gettempdir()+"\\idprf.png")):
	os.system('powershell wget https://github.com/pat229988/just-img/raw/master/idprf.png -OutFile {}'.format(tempfile.gettempdir()+"\\idprf.png"))
	os.system('powershell wget https://github.com/pat229988/just-img/raw/master/haarcascade_frontalface_default.xml -OutFile {}'.format(tempfile.gettempdir()+"\\haarcascade_frontalface_default.xml"))

############### Importing internal libraries################
from vm_detect import vm_check
from display_check import display_check
from kill_all import kill_all
from s3_file_upload import upload_files
from keydisable import dis_keys
from network import vpn_setup
from azure_conn import update,connect

dis_keys()
vm_check()
display_check()
kill_all()
vpn_setup()

#############fetching Ip Address#######################
import time
time.sleep(35)
import ifcfg
ip=[]
for name, interface in ifcfg.interfaces().items():
    if(interface['inet4']):
        ip.append(interface['inet4'][0])
for x in ip:
    if("10.0" in x):
        global i__P
        i__P = "10.0.0"
        i__P = x
        print(x)


############connecting cosmos DB#################
db_link,client=connect()

#########################done######################################

pth=tempfile.gettempdir()+'\\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pth)
from random import randint

global u_rl
u_rl = "u"
global s_m
s_m = 0
global e_nr
enr = 0
global n_m
nm = "nn"
global s_ubj
subj = "sb"
########Test/ Temp SQL server###################
#import pymysql as mdb
#db_con = mdb.connect(host='remotemysql.com',port=3306,user='YPujtQclpQ', password='RRQf1LozNv', database='YPujtQclpQ')
#cursor = db_con.cursor()
#def recon():
#    db_con = mdb.connect(host='remotemysql.com',port=1136,user='YPujtQclpQ', password='RRQf1LozNv', database='YPujtQclpQ')
#    cursor = db_con.cursor()

class EXAMWindow(QWidget):
    """
    final window in whowing detilsof student and instructions and waiting till the link gets open
    """
    def __init__(self):
        super().__init__()
        #Window3.setObjectName("Window3")
        #Window3.resize(800,600)
        #layout for displaying student details
        ######keyboard.unhook_all()###########################enabeling hot keys one line only#####################
        ly1 = QFormLayout()
        self.std_det=QLabel("Student !! ")
        self.std_det.setFont(QFont('Arial', 10))
        self.std_det.setAlignment(Qt.AlignLeft)
        ly1.addRow(self.std_det)

        self.yr_nm=QLabel("your name : ")
        self.yr_nm.setFont(QFont('Arial', 10))
        self.yr_nm.setAlignment(Qt.AlignLeft)
        global n_m
        self.std_name=QLabel(n_m)
        self.std_name.setFont(QFont('Arial', 10))
        ly1.addRow(self.yr_nm,self.std_name)

        self.yr_en = QLabel("your enroll : ")
        self.yr_en.setFont(QFont('Arial', 10))
        global e_nr
        self.enroll_no = QLabel(str(e_nr))
        self.enroll_no.setFont(QFont('Arial', 10))
        ly1.addRow(self.yr_en,self.enroll_no)

        self.sbj_i = QLabel("today's subject : ")
        self.sbj_i.setFont(QFont('Arial', 10))
        global s_ubj
        self.sbj = QLabel(s_ubj)
        self.sbj.setFont(QFont('Arial', 10))
        ly1.addRow(self.sbj_i,self.sbj)
        ly1.setAlignment(Qt.AlignLeft)

        self.w=QWidget()
        self.w.setLayout(ly1)
        self.setup_camera()
        self.video_size = QSize(160, 120)
        self.setup_camera()
        self.image_label_img = QLabel()
        #self.image_label_img.setAlignment(Qt.AlignRight)
        self.image_label_img.setFixedSize(self.video_size)

        ly_img = QHBoxLayout()
        ly_img.addWidget(self.w)
        ly_img.addWidget(self.image_label_img)
        w_ly=QWidget()
        w_ly.setLayout(ly_img)

        global u_rl
        self.brws = QWebEngineView()
        self.brws.load(QUrl(u_rl))
        #w_web = QWidget()
        #w_web.setLayout(self.brws)
        
        sbt_F_ = QPushButton("FINAL SUBMIT")
        #sbt_F_.setGeometry(QtCore.QRect(280,210,111,51))
        sbt_F_.clicked.connect(self.sbmt)
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.w, 1, 0)
        grid.addWidget(self.image_label_img, 1, 1)
        grid.addWidget(self.brws,2,0)
        grid.addWidget(sbt_F_,3,0)
        self.setLayout(grid)

        """self.ly_V=QVBoxLayout()
        self.ly_V.addWidget(w_ly)
        self.ly_V.addWidget(self.brws)
        self.setLayout(grid)
        self.w_f_2=QWidget()
        self.w_f_2.setLayout(self.ly_V)
        Window3.setCentralWidget(self.w_f_2)
        Window3.showFullScreen()"""
        
        
    def sbmt(self):
        keyboard.unhook_all()###########################enabeling hot keys one line only#####################
        exit()
    

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture2 = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.display_video_stream2)
        self.timer2.start(30)

    def display_video_stream2(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture2.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)
        self.image_label_img.setPixmap(QPixmap.fromImage(image))
        #self.image_label_img.setAlignment(Qt.AlignRight)


class FinalWindow(object):
    """
    final window in whowing detilsof student and instructions and waiting till the link gets open
    """
    def __init__(self,Window2):
        super().__init__()
        Window2.setObjectName("Window2")
        Window2.resize(800,600)
        ly = QVBoxLayout()
        self.label = QLabel("this instructions are important!!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Times', 20,QFont.Bold))
        ly.addWidget(self.label)

        #layout for displaying student details 
        ly1 = QFormLayout()
        self.std_det=QLabel("Student !! ")
        self.std_det.setFont(QFont('Arial', 15))
        ly1.addRow(self.std_det)

        self.yr_nm=QLabel("your name : ")
        self.yr_nm.setFont(QFont('Arial', 15))
        global n_m
        self.std_name=QLabel(n_m)
        self.std_name.setFont(QFont('Arial', 15))
        ly1.addRow(self.yr_nm,self.std_name)

        self.yr_en = QLabel("your enroll : ")
        self.yr_en.setFont(QFont('Arial', 15))
        global e_nr
        self.enroll_no = QLabel(str(e_nr))
        self.enroll_no.setFont(QFont('Arial', 15))
        ly1.addRow(self.yr_en,self.enroll_no)

        self.sbj_i = QLabel("today's subject : ")
        self.sbj_i.setFont(QFont('Arial', 15))
        global s_ubj
        self.sbj = QLabel(s_ubj)
        self.sbj.setFont(QFont('Arial', 15))
        ly1.addRow(self.sbj_i,self.sbj)
        self.w=QWidget()
        self.w.setLayout(ly1)

        #for sudent image
        self.img_l = QLabel()
        path=tempfile.gettempdir()+"\\NewPicture.png"
        image = cv2.imread(path)
        image = cv2.resize(image,(160,120))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(image)
        self.img_l.setPixmap(QPixmap.fromImage(image))
        self.img_l.setAlignment(Qt.AlignRight)

        #combinig student details widget and image 
        ly_H = QHBoxLayout()
        ly_H.addWidget(self.w)
        ly_H.addWidget(self.img_l)
        w_H=QWidget()
        w_H.setLayout(ly_H)
        ly.addWidget(w_H)
        ##open link button
        #global u_rl
        #url="http://www.google.com"
        #u_rl=url
        op_lnk = QPushButton("open link")
        op_lnk.setGeometry(QtCore.QRect(280,210,111,51))
        op_lnk.clicked.connect(lambda : self.open_link_window(Window2))
        ly.addWidget(op_lnk)

        """self.setLayout(ly)
        """
        self.w_f=QWidget()
        self.w_f.setLayout(ly)
        Window2.setCentralWidget(self.w_f)

    def open_link_window(self,Window2):
        #Window3 = QMainWindow()
        #wth = EXAMWindow(Window3)
        #Window3.showFullScreen()
        global e_nr
        enrollno=e_nr
        path1=tempfile.gettempdir()+"\\NewPicture.png"
        path2=tempfile.gettempdir()+"\\NewPicture_doc.png"
        upload_files(enrollno,path1,path2)
        self.wth = QWidget()
        self.wth = EXAMWindow()
        self.wth.showFullScreen()
        Window2.hide()
        #ly.addWidget(self.browser)
        #self.setLayout(ly)

class AnotherWindow(object):
    """
    window to get picture of student and his/her icard
    """
    def __init__(self,Window1):
        super().__init__()
        Window1.setObjectName("Window1")
        Window1.resize(800,600)
        #displaying title
        ly = QFormLayout()
        self.label = QLabel("it's your exam get your ass steady!!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Times', 20,QFont.Bold))
        ly.addRow(self.label)

        #displaying student details
        self.std_det=QLabel("Student !! ")
        self.std_det = self.text_edt_L(self.std_det)
        ly.addRow(self.std_det)

        self.yr_nm=QLabel("your name : ")
        self.yr_nm = self.text_edt_L(self.yr_nm)
        global n_m
        print(n_m)
        self.std_name=QLabel(n_m)
        self.std_name=self.text_edt_R(self.std_name)
        ly.addRow(self.yr_nm,self.std_name)

        self.yr_en = QLabel("your enroll : ")
        self.yr_en = self.text_edt_L(self.yr_en)
        global e_nr
        self.enroll_no = QLabel(str(e_nr))
        self.enroll_no = self.text_edt_R(self.enroll_no)
        ly.addRow(self.yr_en,self.enroll_no)

        self.sbj_i = QLabel("today's subject : ")
        self.sbj_i = self.text_edt_L(self.sbj_i)
        global s_ubj
        self.sbj = QLabel(s_ubj)
        self.sbj = self.text_edt_R(self.sbj)
        ly.addRow(self.sbj_i,self.sbj)
        #ly1=QFormLayout()
        #widget for student details
        w=QWidget()
        w.setLayout(ly)

        #layout for picture clicking
        lb_std_pic=QLabel("student picture")
        lb_std_pic=self.text_edt_C(lb_std_pic)
        self.cap_btn = QPushButton("capcture")
        self.cap_btn.setGeometry(QtCore.QRect(280,210,111,51))
        self.cap_btn.clicked.connect(self.cap_pic)
        self.video_size = QSize(320, 240)
        self.setup_camera()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(self.video_size)
        ly_img = QHBoxLayout()
        ly_img.addWidget(self.image_label)
        w_img=QWidget()
        w_img.setLayout(ly_img)

        lay = QVBoxLayout()
        Qt.AlignCenter = lay.alignment()
        lay.addWidget(lb_std_pic)
        lay.addWidget(self.cap_btn)
        lay.addWidget(w_img)
        w1=QWidget()
        w1.setLayout(lay)

        #layout for picture of doccument
        lb_std_doc=QLabel("doccument picture")
        lb_std_doc=self.text_edt_C(lb_std_doc)
        self.cap_btn_doc = QPushButton("capcture")
        self.cap_btn_doc.setEnabled(False)
        self.cap_btn_doc.setGeometry(QtCore.QRect(280,210,111,51))
        self.cap_btn_doc.clicked.connect(self.cap_pic_doc)
        self.video_size = QSize(320, 240)
        self.image_label_doc = QLabel()
        self.image_label_doc.setAlignment(Qt.AlignCenter)
        self.image_label_doc.setFixedSize(self.video_size)
        pth=tempfile.gettempdir()+"\\idprf.png"
        self.read_img(pth)
        ly_img_doc = QHBoxLayout()
        ly_img_doc.addWidget(self.image_label_doc)
        w_img_doc=QWidget()
        w_img_doc.setLayout(ly_img_doc)

        lay2 = QVBoxLayout()
        Qt.AlignCenter = lay2.alignment()
        lay2.addWidget(lb_std_doc)
        lay2.addWidget(self.cap_btn_doc)
        lay2.addWidget(w_img_doc)
        w2=QWidget()
        w2.setLayout(lay2)

        #combining layouts of pics horizontally
        Hlay = QHBoxLayout()
        Hlay.addWidget(w1)
        Hlay.addWidget(w2)
        fw=QWidget()
        fw.setLayout(Hlay)

        #submit button
        self.sbt_btn=QPushButton("Submit")
        self.sbt_btn.setEnabled(False)
        self.sbt_btn.clicked.connect(lambda : self.call_to_third(Window1))
        self.sbt_btn.setGeometry(QtCore.QRect(280,210,111,51))

        #combined layout
        layout = QVBoxLayout()
        layout.addWidget(w)
        layout.addWidget(fw)
        layout.addWidget(self.sbt_btn)

        self.wf=QWidget()
        self.wf.setLayout(layout)
        Window1.setCentralWidget(self.wf)

    def text_edt_C(self,x):
        x.setAlignment(Qt.AlignCenter)
        x.setFont(QFont('Arial', 15))
        return x

    def text_edt_R(self,x):
        x.setAlignment(Qt.AlignRight)
        x.setFont(QFont('Arial', 15))
        return x

    def text_edt_L(self,x):
        x.setAlignment(Qt.AlignLeft)
        x.setFont(QFont('Arial', 15))
        return x

    def call_to_third(self,Window1):
        Window2 = QMainWindow()
        wth = FinalWindow(Window2)
        Window2.showFullScreen()
        Window1.hide()

    def cap_pic_doc(self):
        self.capture.release()
        self.timer.stop()
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
        ret,frame = cap.read()
        ptt=tempfile.gettempdir()+"\\NewPicture_doc.png"
        cv2.imwrite(ptt,frame)
        pth=tempfile.gettempdir()+"\\NewPicture_doc.png"
        image = cv2.imread(pth)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(image)
        self.image_label_doc.setPixmap(QPixmap.fromImage(image))
        self.image_label_doc.setAlignment(Qt.AlignCenter)
        cap.release()
        self.cap_btn_doc.setText("re capcture")
        self.sbt_btn.setEnabled(True)
        

    def cap_pic(self):
        self.capture.release()
        self.timer.stop()
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
        ret,frame = cap.read()
        ptt=tempfile.gettempdir()+"\\NewPicture.png"
        cv2.imwrite(ptt,frame)
        pth=tempfile.gettempdir()+"\\NewPicture.png"
        image = cv2.imread(pth)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(image)
        self.image_label.setPixmap(QPixmap.fromImage(image))
        self.image_label.setAlignment(Qt.AlignCenter)
        cap.release()
        self.setup_camera_2()
        self.display_video_stream_2()
        self.cap_btn.setText("re capcture")
        self.cap_btn_doc.setEnabled(True)
        #self.image_label=self.read_img(pth)


    def read_img(self,path):
        #path=r"E:\idprf.png"
        print(path)
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(image)
        self.image_label_doc.setPixmap(QPixmap.fromImage(image))
        self.image_label_doc.setAlignment(Qt.AlignCenter)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)
        self.image_label.setPixmap(QPixmap.fromImage(image))
        self.image_label.setAlignment(Qt.AlignCenter)

    def setup_camera_2(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream_2)
        self.timer.start(30)

    def display_video_stream_2(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)
        self.image_label_doc.setPixmap(QPixmap.fromImage(image))
        self.image_label_doc.setAlignment(Qt.AlignCenter)

    def displayFrame(self):
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        timer = QTimer()
        timer.timeout.connect()
        timer.start(30)
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.img_lb.setPixmap(QPixmap.fromImage(image))
        self.img_lb.setAlignment(Qt.AlignCenter)
        cap.release()

class Ui_MainWindow(object):
    
    def __init__(self,MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,600)
        #layout for inserting credentials i.e. enroll num and pass
        self.e1 = QLineEdit()
        self.e1.setMaxLength(12)
        self.e1.setAlignment(Qt.AlignRight)
        #self.e1.setGeometry()
        self.e1.setFont(QFont("Arial",15))
        self.e2 = QLineEdit()
        self.e2.setEchoMode(QLineEdit.Password)
        self.e2.setAlignment(Qt.AlignRight)
        self.e2.setFont(QFont("Arial",15))
        self.flo = QFormLayout()
        self.flo.addRow('Enter Enroll No. : ',self.e1)
        self.flo.addRow('Ebnter pass : ',self.e2)
        self.w1 = QWidget()
        self.w1.setLayout(self.flo)

        #layout for submit and exit
        self.btn = QPushButton("Submit")
        self.btn.setGeometry(QtCore.QRect(280,210,111,51))
        self.btn.clicked.connect(lambda : self.on_submit(MainWindow))
        self.btn2 = QPushButton("Exit")
        self.btn.setGeometry(QtCore.QRect(280,210,111,51))
        self.btn2.clicked.connect(self.exiting_wind)
        self.flo1 = QHBoxLayout()
        self.flo1.addWidget(self.btn)
        self.flo1.addWidget(self.btn2)
        self.w2 = QWidget()
        self.w2.setLayout(self.flo1)
        
        #combined both layouts mentioned above
        self.ly = QVBoxLayout()
        self.ly.addWidget(self.w1)
        self.ly.addWidget(self.w2)
        self.w = QWidget()
        self.w.setLayout(self.ly)
        MainWindow.setCentralWidget(self.w)


    def exiting_wind(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Tu ne exit pe click kiya hai sale !!!!")
        self.msg.setStandardButtons(QMessageBox.Discard | QMessageBox.Ok)
        x=self.msg.exec()
        if(x == QMessageBox.Ok):
            exit(0)

    def checkcred(self):
        e__R = self.e1.text()
        global e_nr
        e_nr = e__R
        p__S = self.e2.text()
        p__S = hashlib.md5(p__S.encode('utf-8')).hexdigest()
        print(p__S)
        
        coll_id = 'user'
        coll_query = "select * from r where r.id = '{0}'".format(coll_id)
        coll = list(client.QueryCollections(db_link, coll_query))[0]
        coll_link = coll['_self']
        print(coll_link)

        doc_id = e__R
        doc_qry = "select * from r where r.username = '{0}'".format(doc_id)
        doc = list(client.QueryDocuments(coll_link, doc_qry,{ "enableCrossPartitionQuery": True }))[0]
        doc_link = doc['_self']
        print(doc_link)
        print(doc)
        print(doc["sem"])
        
        global s_m
        s_m = doc["sem"]
        
        
        coll_id1 = 'exam'
        coll_query1 = "select * from r where r.id = '{0}'".format(coll_id1)
        coll1 = list(client.QueryCollections(db_link, coll_query1))[0]
        coll_link1 = coll1['_self']
        print(coll_link1)
        doc1_id = doc["sem"]
        doc1_qry = "select * from r where r.sem = '{0}'".format(doc1_id)
        doc1 = list(client.QueryDocuments(coll_link1, doc1_qry,{ "enableCrossPartitionQuery": True }))[0]
        doc1_link = doc1['_self']
        print(doc1_link)
        print(doc1)
        
        global s_ubj
        s_ubj = doc1["sub"]
        global u_rl
        u_rl = doc1["link"]
        print(u_rl)
        #qry="select pass,name,sub from user where enroll like {}".format(e__R)
        #cursor.execute(qry)
        #rs = cursor.fetchall()

        #Alert boxex if not entered credentials
        if((not self.e1.text()) or (not self.e2.text())):
            if(not self.e1.text()):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("eneter enrollment number first, dumbass!!")
                self.msg.setStandardButtons(QMessageBox.Discard)
                self.msg.exec()
            elif(not self.e2.text()):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("who is gonna enter pass, your father!! , dumbass!!")
                self.msg.setStandardButtons(QMessageBox.Discard)
                self.msg.exec()
            return False

        elif(doc):
            self.p=doc["pass"]
            #self.p=rs[0][0]
            print(self.p)
            global n_m
            n_m=doc["name"]
            
            #n_m = rs[0][1]
            
            #global s_ubj
            #s_ubj = rs[0][2]
            self.e2.setText('')
            #print(o)
            if(p__S==self.p):
                update(doc)
                print('valid cred')
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setText(" hurrey successful login !!")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.e1.setText('')
                self.msg.exec()
                return True
            elif(p__S!=self.p):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText(" check your pass again, dumbass!!")
                self.msg.setStandardButtons(QMessageBox.Discard)
                self.msg.exec()
                return False
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("pakka tu student hai sale")
            self.msg.setInformativeText("tera data record nai mila!!")
            self.msg.setStandardButtons(QMessageBox.Discard)
            self.msg.exec()
            return False

    def on_submit(self,MainWindow):
        vali = self.checkcred()
        if(vali):
            #self.w.hide()
            self.show_new_window(MainWindow)
            print("submitted")


    def show_new_window(self, MainWindow):
        Window1 = QMainWindow()
        w = AnotherWindow(Window1)
        Window1.showFullScreen()
        MainWindow.hide()


if __name__=="__main__":
    app = QApplication()
    MainWindow = QMainWindow()
    w = Ui_MainWindow(MainWindow)
    MainWindow.showFullScreen()
    app.exec_()
