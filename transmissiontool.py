import wx
import teraframe
import configparser
import os, sys
import logging
import datetime
from collections import OrderedDict
import serial
from time import sleep
from threading import Event, Thread
import socket
import signal

"""----------------------------------------------
通信用ソフト
グローバル定数
path    : 実行ファイルのディレクトリ
today   : 今日の日付
now     : 今の時間
INI     : 設定ファイルの場所
----------------------------------------------"""
path = os.path.dirname( sys.argv[0] )
INI = path + "/INI.conf"
conf = configparser.SafeConfigParser()
conf.read(INI)
version = "Ver. 0.90"
if not os.path.exists( path+"/log" ):
    os.mkdir(path+"/log")
if not os.path.exists( INI ):
    conf["DEFAULT"] = {"host":"localhost",
                        "port":"23",
                        "serial":"COM1",
                        "baudrate":"9600",
                        "data_bit":"8",
                        "parity":"No",
                        "stopbit":"1",
                        "flow_ctrl":"No",
                        "timeout":"20",
                        "lfcode":"CR"}
if not "option" in conf:
    conf.add_section("option")
if not "window" in conf:
    conf.add_section("window")
default = conf["DEFAULT"]
option = conf["option"]

print("設定を読み出す")
for key in option:
    print(key)
    print(option[key])

with open(INI,"w") as configfile:
    conf.write(configfile)

now = datetime.datetime.now()
today = now.strftime( "%Y-%m-%d" )          # 日付 YYYY-MM-DD
today1 = now.strftime( "%y/%m/%d" )         # 日付 YY/MM/DD
now = now.strftime( "%H:%M:%S" )            # 時刻 HH:MM:SS

# ログファイルの設定
logformat = '[%(asctime)s][%(levelname)s] %(message)s'
logname = path + '\log\logfile' +  today + '.log'
logging.basicConfig(level    = logging.DEBUG,
                    format   = logformat,
                    filename = logname,
                    filemode = 'a')
file_information = None

class Mainframe( teraframe.MyFrame1 ):
    def __init__( self, parent ):
        teraframe.MyFrame1.__init__( self, parent )
        logging.info( "ソフト起動" )
        self.SetTitle("通信ソフト "+version)
        IP_log = os.path.join( path, "IP_log.txt")
        subframe = MyDialog1( None )
        result = subframe.ShowModal()
        if result == wx.ID_OK:
            print("OK")
            x,y =  subframe.GetScreenPosition()
            conf["window"]["s_frame"] = str(x) + "," + str(y)
            if "m_pos" in conf["window"]:
                pos = conf["window"]["m_pos"]
                x,y = pos.split(",")
                self.SetPosition((int(x),int(y)))
            if "m_size" in conf["window"]:
                size = conf["window"]["m_size"]
                w,h = size.split(",")
                self.SetSize((int(w),int(h)))
            option["host"] = subframe.m_comboBox1.GetValue()
            option["port"] = subframe.m_textCtrl1.GetValue()
            option["serial"] = subframe.m_comboBox3.GetValue()
            print(option["host"])
            IP = option["host"]
            port = option["port"]
            service = subframe.m_checkBox1.GetValue()
            com = option["serial"]
            self.encoding = self.m_comboBox8.GetValue()
            self.m_timer1.Stop()
            self.m_comboBox6.SetValue( option["lfcode"] )
            with open(INI,"w") as configfile:
                conf.write(configfile)
            if subframe.m_checkBox3.GetValue():
                with open(IP_log, "w") as iplog:
                    iplog.write("")
                with open(IP_log,"a") as iplog:
                    subframe.IP_Dict[IP] = port
                    connectlog = []
                    for i in subframe.IP_Dict.keys():
                        if i == "":
                            continue
                        connectlog.append("{},{}\n".format(i,subframe.IP_Dict[i]))
                    iplog.writelines(connectlog)
            if service:
                # socket使用の宣言
                self.m_staticText12.SetLabel( "telnet" )
                self.m_staticText13.SetLabel( "{} : {}".format(IP,port) )
                self.m_staticText14.SetLabel( "" )
                self.mode = "telnet"
                thread = Thread( target = self.Telnet_receive,
                name="telnetloop",args=())
                thread.start()
                logging.info("telnet: {}:{}接続要求".format(IP,port))
            else:
                self.m_staticText12.SetLabel( "シリアル" )
                self.m_staticText13.SetLabel( com )
                self.m_staticText14.SetLabel( option["baudrate"]+"bps" +', data_bit : ' + option["data_bit"] +', parity : ' + option["parity"] +', stopbit : ' + option["stopbit"] +', flow_ctrl : ' + option["flow_ctrl"] +', timeout : ' + option["timeout"] )
                self.mode = "serial"
                thread = Thread( target = self.Serial_receive, name="serialloop",args=())
                thread.start()
                self.m_timer3.Start(500)
                logging.info("serial: {}".format(com))
        else:
            exit()

    def Telnet_receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(2)
        try:
            HOST, PORT = int(option["host"]), int(option["port"])
        except:
            HOST, PORT = option["host"], int(option["port"])
        try:
            logging.info( "接続成功" )
            self.s.connect((HOST, PORT))
            self.s.settimeout(None)
            self.org_txt = b""
            while not threadevent.wait(0.01):
                recv_data = self.s.recv(1024)
                if recv_data == b"":
                    logging.info("telnet通信終了")
                    print("telnet通信終了")
                    break
                print(recv_data)

                self.org_txt += recv_data
                try:
                    self.m_textCtrl12.SetValue(str(len(self.org_txt.decode("utf-8")))+str("({})".format(len(self.org_txt))))
                    logging.info("受信：{}".format(recv_data.decode("utf-8")))
                except:
                    self.m_textCtrl12.SetValue(str(len(self.org_txt.decode("shift-jis")))+str("({})".format(len(self.org_txt))))
                    logging.info("受信：{}".format(recv_data.decode("shift-jis")))
                self.m_textCtrl11.SetValue(self.org_txt.decode(self.encoding,errors="backslashreplace"))
        except OSError as strerror:
            e_msg = "ERROR: " + str( strerror )
            logging.error( e_msg )
            box = wx.MessageDialog(None,e_msg.upper() + "\n" + HOST + "へ接続できませんでした","通信ソフト",wx.OK | wx.ICON_ERROR)
            anser = box.ShowModal()
            self.s.close()
            os._exit(1)
        except EOFError as strerror:
            e_msg = "ERROR: " + str( strerror )
            logging.error( e_msg )
            box = wx.MessageDialog(None,e_msg.upper() + "\n" + HOST + "へ接続できませんでした","通信ソフト",wx.OK | wx.ICON_ERROR)
            anser = box.ShowModal()
            self.s.close()
            os._exit(1)
        threadevent.clear()

    def Serial_receive(self):
        parity = option["parity"]
        if parity == "No":
            parity = serial.PARITY_NONE
        elif parity == "Odd":
            parity = serial.PARITY_ODD
        elif parity == "Even":
            parity == serila.PARITY_EVEN
        else:
            parity = serial.PARITY_NONE
        stopbit = option["stopbit"]
        if stopbit == "1":
            stopbit = serial.STOPBITS_ONE
        if stopbit == "1.5":
            stopbit = serial.STOPBITS_ONE_POINT_FIVE
        if stopbit == "2":
            stopbit = serial.STOPBITS_TWO
        flow_ctrl = option["flow_ctrl"]
        print(flow_ctrl)
        if flow_ctrl == "Xon/Xoff":
            xonxoff = True
            rtscts = False
            dsrdtr = False
        elif flow_ctrl == "No":
            xonxoff = True
            rtscts = False
            dsrdtr = False
        else:
            xonxoff = False
            rtscts = True
            dsrdtr = True

        self.ser = serial.Serial(
                option["serial"],
                baudrate = option["baudrate"],
                timeout=int(option["timeout"])*0.0001,
                write_timeout=int(option["timeout"])*0.0001,
                bytesize=int(option["data_bit"]),
                parity = parity,
                stopbits = stopbit,
                xonxoff = xonxoff,
                rtscts = rtscts,
                dsrdtr = dsrdtr
                                )
        logging.info( "シリアル通信開始" )
        print("シリアル通信")
        self.ser.reset_input_buffer()
        recv_buffa = b""
        self.org_txt = b""
        try:
            while not threadevent.wait(0.01):
                recv_data = self.ser.read(100)
                if len(recv_data) > 0:
                    print(recv_data)
                    self.org_txt += recv_data
                    try:
                        self.m_textCtrl12.SetValue(str(len(self.org_txt.decode("utf-8")))+str("({})".format(len(self.org_txt))))
                        logging.info("受信：{}".format(recv_data.decode("utf-8")))
                    except:
                        self.m_textCtrl12.SetValue(str(len(self.org_txt.decode("shift-jis")))+str("({})".format(len(self.org_txt))))
                        logging.info("受信：{}".format(recv_data.decode("shift-jis")))
                    self.m_textCtrl11.SetValue(self.org_txt.decode(self.encoding,errors="backslashreplace"))
        except serial.serialutil.SerialException as strerror:
            e_msg = "ERROR: " + str( strerror )
            logging.error( e_msg )
            box = wx.MessageDialog(None,e_msg.upper(),"通信ソフト",wx.OK | wx.ICON_ERROR)
            anser = box.ShowModal()
            self.ser.close()
            os._exit(1)
        logging.info("シリアル通信終了")
        print("シリアル通信終わり")
        self.ser.close()
        threadevent.clear()

    def DTR_ctrl( self, event ):
        if self.m_checkBox5.GetValue():
            self.ser.setDTR(True)
        else:
            self.ser.setDTR(False)
    def RTS_ctrl( self, event ):
        if self.m_checkBox6.GetValue():
            self.ser.setRTS(True)
        else:
            self.ser.setRTS(False)

    def Auto_Send( self, event ):
        time = self.m_comboBox7.GetSelection()
        if time == 0:
            self.m_timer1.Stop()
        elif time == 1:
            self.m_timer1.Start(100)
        elif time == 2:
            self.m_timer1.Start(500)
        elif time == 3:
            self.m_timer1.Start(1000)
        elif time == 4:
            self.m_timer1.Start(5000)
        elif time == 5:
            self.m_timer1.Start(10000)

    def change_encode( self, event ):
        print("change")
        self.encoding = self.m_comboBox8.GetValue()
        txt = self.org_txt
        self.m_textCtrl11.SetValue(txt.decode(self.encoding,errors="backslashreplace"))

    def recv_clear( self, event ):
        self.org_txt = b""
        self.m_textCtrl11.SetValue(self.org_txt)
        self.m_textCtrl12.SetValue("0(0)")

    def Send_text( self, event ):
        now = datetime.datetime.now()
        today1 = now.strftime( "%y/%m/%d" )         # 日付 YY/MM/DD
        now = now.strftime( "%H:%M:%S" )            # 時刻 HH:MM:SS


        text = self.m_textCtrl9.GetValue()
        linecode = self.m_comboBox6.GetValue()
        if "\n" in text:
            if linecode == "CR":
                text = text.replace("\n", "\r")
            elif linecode == "CRLF":
                text = text.replace("\n", "\r\n")
        if "_time" in text:
            text = text.replace("_time", now )
        if "_today" in text:
            text = text.replace("_today", today1)
        text = text.encode("utf-8")
        if self.mode == "serial":
            try:
                self.ser.write(text)
                logging.info("送信：{}".format(text.decode("utf-8")))
            except serial.serialutil.SerialTimeoutException as strerror:
                e_msg = "ERROR:" + str(strerror)
                logging.error( strerror )
                box = wx.MessageDialog(None,e_msg.upper(),"通信ソフト",wx.OK | wx.ICON_ERROR)
                anser=box.ShowModal()
                self.m_timer1.Stop()
                return
        elif self.mode == "telnet":
            self.s.send(text)
            logging.info("送信：{}".format(text.decode("utf-8")))
        if self.m_checkBox4.GetValue():
            self.send_clear(self)
        print("send:",text)

    def send_clear( self, event ):
        self.m_textCtrl9.SetValue("")

    def Serial_option( self, event ):
        if self.mode == "serial":
            self.m_timer3.Stop()
            threadevent.set()
        option_dlg = MyDialog2( self )
        result = option_dlg.ShowModal()
        if self.mode == "serial":
            thread = Thread( target = self.Serial_receive, name="serialloop",args=())
            thread.start()
            self.m_timer3.Start(500)

    def Input_text( self, event ):
        self.m_textCtrl8.SetValue(str(len(self.m_textCtrl9.GetValue()))+
        str("({})".format(len(self.m_textCtrl9.GetValue().encode("utf-8")))))

    def Open_file( self, event ):
        self.m_comboBox7.SetSelection(0)
        txtpath = self.m_filePicker1.GetPath()
        txtframe = MyFrame2( frame, txtpath )
        result = txtframe.Show()

    def Modem_line( self, event ):
        try:
            g = self.ser
            if self.mode == "serial":
                dsr, cts, cd, ri = str(g.dsr), str(g.cts), str(g.cd), str(g.ri)
                self.m_staticText35.SetLabel(
                    "DSR(6):{}, CTS(8): {}, DCD(1): {}, RI(9): {}, GND(5)".format(dsr.rjust(6," "), cts.rjust(6," "), cd.rjust(6," "), ri.rjust(6," ")))
            else:
                self.m_timer3.Stop()
        except serial.serialutil.SerialException as strerror:
            e_msg = "ERROR: " + str( strerror )
            logging.error( e_msg )
            box = wx.MessageDialog(None,e_msg.upper() + "\n" + HOST + "接続できませんでした","通信ソフト",wx.OK | wx.ICON_ERROR)
            anser = box.ShowModal()
            self.ser.close()
            os._exit(1)

    def ExitHandler( self, event ):
        dlg = wx.MessageDialog( None, '通信ソフトを終了します。\nよろしいですか？',
                            "通信ソフト", style = wx.YES_NO )
        result = dlg.ShowModal()        #ダイアログの表示
        if result == wx.ID_YES:              #はいを押した時終了
            threadevent.set()
            self.m_timer1.Stop()
            if self.mode == "selial":
                self.ser.close()
            elif self.mode == "telnet":
                try:
                    self.s.shutdown(1)
                    sleep(1)
                    self.s.close()
                except:
                    pass
            self.INI_save()
            logging.info( "ソフト終了" )
            print("終了")
            sys.exit()                      #プログラム終了
        else:                           #いいえの時は何もしない
            return

    def INI_save(self):
        option["mode"] = self.mode
        option["lfcode"] = self.m_comboBox6.GetValue()
        print(self.GetScreenPosition())
        print(self.GetSize())
        x,y = self.GetScreenPosition()
        conf["window"]["m_pos"] = str(x) + "," + str(y)
        w,h = self.GetSize()
        conf["window"]["m_size"] = str(w) + "," + str(h)
        with open(INI,"w") as configfile:
            conf.write(configfile)

class MyFrame2( teraframe.MyFrame2 ):
    def __init__( self, parent, txtpath ):
        teraframe.MyFrame2.__init__( self, parent )
        self.SetTitle(txtpath)
        self.m_listBox1.Clear()
        self.parent = parent
        text = txtpath
        with open(text,"r") as t:
            lines = t.readlines()
        self.m_listBox1.SetItems(lines)

    def Txt_select( self, event ):
        strset = self.m_listBox1.GetStringSelection()
        self.m_timer2.Stop()
        print(strset)

    def Txt_execute( self, event ):
        strset = self.m_listBox1.GetStringSelection()
        self.parent.m_textCtrl9.WriteText(strset)

    def Send_Order( self, event ):
        selection, strset, timer = self.Auto_Send( self )
        if timer > 0:
            self.m_timer2.Start(timer)
        else:
            self.m_timer2.Stop()

    def Auto_Send( self, event ):
        selection = self.m_listBox1.GetSelection()
        strset = self.m_listBox1.GetStringSelection()
        timer = int(self.m_comboBox14.GetValue())
        self.parent.m_textCtrl9.Clear()
        self.parent.m_textCtrl9.SetValue( strset )
        self.parent.Send_text( self.parent )
        try:
            self.m_listBox1.SetSelection(selection+1)
            if timer > 0:
                self.m_timer2.Start(timer)
            else:
                self.m_timer2.Stop()
        except:
            self.m_listBox1.SetSelection(0)
            self.m_timer2.Stop()
        finally:
            return selection, strset, timer

    def Send_Selection( self, event ):
        selection = self.m_listBox1.GetSelection()
        strset = self.m_listBox1.GetStringSelection()
        timer = int(self.m_comboBox14.GetValue())
        self.parent.m_textCtrl9.Clear()
        self.parent.m_textCtrl9.SetValue( strset )
        self.parent.Send_text( self.parent )

class MyDialog1( teraframe.MyDialog1 ):
    def __init__( self, parent ):
        teraframe.MyDialog1.__init__( self, parent )
        if "s_frame" in conf["window"]:
            pos = conf["window"]["s_frame"]
            x,y = pos.split(",")
            self.SetPosition((int(x),int(y)))
        IP_log = os.path.join( path, "IP_log.txt")
        port_array = ["COM"+str(i+1) for i in range(32)]
        portlist = []
        for i in port_array:    # 生きているポートを調べる
            try:
                ser = serial.Serial(i,9600)
                portlist.append(i)
                ser.close()
            except:
                pass

        self.m_comboBox3.SetItems(portlist)
        if option["serial"] in portlist:
            self.m_comboBox3.SetValue(option["serial"])
        else:
            self.m_comboBox3.SetSelection(0)
        print("host:",option["host"])

        if os.path.exists( IP_log ):
            self.IP_Dict = OrderedDict()
            self.IP_Dict = self.txt_list( IP_log )     # 接続ログを呼んで辞書型{IP:port}にする
            IP_list = list( self.IP_Dict.keys() )[::-1]        # 辞書のキーをリストにするのと最近の物を上にする
            self.m_comboBox1.SetItems( IP_list )    # コンボボックスに追加する
            if option["host"] in IP_list:
                self.m_comboBox1.SetStringSelection(option["host"])        # 選択する
            else:
                self.m_comboBox1.SetSelection(0)
            key = self.m_comboBox1.GetValue()
            try:
                self.m_textCtrl1.SetValue(self.IP_Dict[key])
            except:
                self.m_textCtrl1.SetValue(option["port"])
        else:
            with open( IP_log, "w") as file:
                file.write("")


    def IP_Set(self,event):
        key = self.m_comboBox1.GetValue()
        self.m_textCtrl1.SetValue(self.IP_Dict[key])

    def txt_list( self, txt_file ):   # テキストファイルを読み取ってリストにする
        IP_Dict = OrderedDict()
        file = open(txt_file,"r")
        data = file.read()
        file.close()
        lines = data.split("\n")
        for x in lines:
            if (x.count(",") == 1):
                data = x.split(",")
                IP = data[0]
                port = data[1]
                IP_Dict[IP] = port

        return IP_Dict

    def Checked_IP(self,event):
        self.m_checkBox1.SetValue(True)
        self.m_checkBox2.SetValue(False)
    def Checked_Serial(self,event):
        self.m_checkBox1.SetValue(False)
        self.m_checkBox2.SetValue(True)

class MyDialog2( teraframe.MyDialog2 ):
    def __init__( self, parent ):
        teraframe.MyDialog2.__init__( self, parent )
        port_array = ["COM"+str(i+1) for i in range(32)]
        self.m_comboBox7.SetItems(port_array)
        self.m_comboBox7.SetValue(option["serial"])
        self.m_comboBox8.SetValue(option["baudrate"])
        self.m_comboBox9.SetValue(option["data_bit"])
        self.m_comboBox10.SetValue(option["parity"])
        self.m_comboBox11.SetValue(option["stopbit"])
        self.m_comboBox12.SetValue(option["flow_ctrl"])
        self.m_spinCtrl1.SetValue(int(option["timeout"]))

    def Serial_save( self, event ):
        option["serial"] = self.m_comboBox7.GetValue()
        option["baudrate"] = self.m_comboBox8.GetValue()
        option["data_bit"] = self.m_comboBox9.GetValue()
        option["parity"] = self.m_comboBox10.GetValue()
        option["stopbit"] = self.m_comboBox11.GetValue()
        option["flow_ctrl"] = self.m_comboBox12.GetValue()
        option["timeout"] = str(self.m_spinCtrl1.GetValue())

        with open(INI,"w") as configfile:
            conf.write(configfile)
        self.Destroy()

    def option_reset( self, event ):
        self.m_comboBox8.SetValue(default["baudrate"])
        self.m_comboBox9.SetValue(default["data_bit"])
        self.m_comboBox10.SetValue(default["parity"])
        self.m_comboBox11.SetValue(default["stopbit"])
        self.m_comboBox12.SetValue(default["flow_ctrl"])
        self.m_spinCtrl1.SetValue(int(default["timeout"]))

thread = Thread(target = Mainframe)
threadevent = Event()
app = wx.App( False )
frame = Mainframe( None )
frame.Show(True)
app.MainLoop()
