import math
from SBoxes import *
from boolean_function import *
from evaluate_sbox import *
from main import *
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget

sbox=[]
N = 0
M = 0
xuebeng=[]


class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.textEditChooseBf.setReadOnly(True)
        self.pushButtonTxtOut.setDisabled(True)
        self.pushButtonPath.setDisabled(True)
        self.pushButtonBegin2.setDisabled(True)
        self.lineEditFileName.setDisabled(True)
        self.textBrowserFaultRemind.clear()
        self.center()
        self.pushButtonBegin.clicked.connect(lambda: self.custom_sboxinitial())
        self.pushButtonBegin2.clicked.connect(lambda: self.output2())
        self.pushButtonPath.clicked.connect(lambda:self.choosepath())
        self.pushButtonTxtOut.clicked.connect(lambda:self.txtoutput())
        self.pushButtonChooseTab.clicked.connect(lambda:self.choose_tab())
        #传入内置的S盒
        self.actionKASUMI_S7.triggered.connect(lambda:self.buildin_sboxinitial(self.actionKASUMI_S7.text()))
        self.actionKASUMI_S9.triggered.connect(lambda:self.buildin_sboxinitial(self.actionKASUMI_S9.text()))
        self.actionNESSIE.triggered.connect(lambda: self.buildin_sboxinitial(self.actionNESSIE.text()))
        self.actionAES.triggered.connect(lambda: self.buildin_sboxinitial(self.actionAES.text()))
        self.actionSEED_S0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSEED_S0.text()))
        self.actionSEED_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSEED_S1.text()))
        self.actionCamellia_S0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionCamellia_S0.text()))
        self.actionCamellia_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionCamellia_S1.text()))
        self.actionCamellia_S2.triggered.connect(lambda: self.buildin_sboxinitial(self.actionCamellia_S2.text()))
        self.actionCamellia_S3.triggered.connect(lambda: self.buildin_sboxinitial(self.actionCamellia_S3.text()))
        self.actionSM4.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSM4.text()))
        self.actionZUC_S0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionZUC_S0.text()))
        self.actionZUC_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionZUC_S1.text()))
        self.actionARIA_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionARIA_S1.text()))
        self.actionARIA_S2.triggered.connect(lambda: self.buildin_sboxinitial(self.actionARIA_S2.text()))
        self.actionSkipjack.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSkipjack.text()))
        self.actionMisty.triggered.connect(lambda:self.buildin_sboxinitial(self.actionMisty.text()))
        self.actionSERPENT_S0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S0.text()))
        self.actionSERPENT_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S1.text()))
        self.actionSERPENT_S2.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S2.text()))
        self.actionSERPENT_S3.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S3.text()))
        self.actionSERPENT_S4.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S4.text()))
        self.actionSERPENT_S5.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S5.text()))
        self.actionSERPENT_S6.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S6.text()))
        self.actionSERPENT_S7.triggered.connect(lambda: self.buildin_sboxinitial(self.actionSERPENT_S7.text()))
        self.actionLBlock_0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_0.text()))
        self.actionLBlock_1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_1.text()))
        self.actionLBlock_2.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_2.text()))
        self.actionLBlock_3.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_3.text()))
        self.actionLBlock_4.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_4.text()))
        self.actionLBlock_5.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_5.text()))
        self.actionLBlock_6.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_6.text()))
        self.actionLBlock_7.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_7.text()))
        self.actionLBlock_8.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_8.text()))
        self.actionLBlock_9.triggered.connect(lambda: self.buildin_sboxinitial(self.actionLBlock_9.text()))
        self.actionDES_S0.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S0.text()))
        self.actionDES_S1.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S1.text()))
        self.actionDES_S2.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S2.text()))
        self.actionDES_S3.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S3.text()))
        self.actionDES_S4.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S4.text()))
        self.actionDES_S5.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S5.text()))
        self.actionDES_S6.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S6.text()))
        self.actionDES_S7.triggered.connect(lambda: self.buildin_sboxinitial(self.actionDES_S7.text()))

    def center(self):  # 主窗口居中显示函数
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

    def buildin_sboxinitial(self,var):
        """ 预处理内置的S盒
        """
        self.textEditSboxInput.clear()
        self.textEditChooseBf.setReadOnly(False)
        self.pushButtonPath.setDisabled(False)
        self.pushButtonBegin2.setDisabled(False)
        
        global sbox
        sbox.clear()
        sbox = (eval(var))
        global N
        global M
        (N,M) = get_size(sbox)
        print("[-]=====>running buildin_sboxinitial()\n")
        print("正在处理的内置S盒为：",sbox,N,M)
        self.textEditSboxInput.setText(str(sbox))
        self.textBrowserFaultRemind.setText("当前处理的{}x{}的S盒是内置的{}".format(N,M,var))
        self.sbox_output()

    def custom_sboxinitial(self):
        """ 预处理手动输入的S盒
            pro: 增加更多的输入方式
        """
        self.textEditChooseBf.setReadOnly(False)
        self.pushButtonPath.setDisabled(False)
        self.pushButtonBegin2.setDisabled(False)
        sbox.clear()
        S = self.textEditSboxInput.toPlainText()
        S=S.replace("[","")
        S=S.replace("]","")
        S = S.split(",")
        
        # DEL：S盒测试
        print("[-]=====>running custom_sboxinitial()\n")
        print("正在处理的手动输入的S盒为：",S)
        numsys = int(self.comboBoxJinZhi.currentText())  # 输入S盒时选择的进制
        try:
            if numsys == 10:
                for i in S:
                    sbox.append(int(i))
            else:
                for i in S:
                    sbox.append(int(i, 16))
            global M
            global N
            (N, M) = get_size(sbox)
            print("输入输出位数为：",N,M)
            self.textBrowserFaultRemind.setText("当前处理的是自定义输入的S盒\n输出位数为：%d,输出位数为：%d" % (N,M))
            self.sbox_output()
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setWindowTitle("Failed")
            msg.setText("S盒输入有问题，请重新检查后使用")
            x = msg.exec()

    def sbox_output(self):
        """S盒初始化后点击计算，将结果显示在屏幕上"""
        #清空窗口中的内容
        self.textBrowserPath.clear()
        self.lineEditFileName.clear()
        self.comboBoxComponentbf.clear()
        self.comboBoxComponentbf.addItems(["f{}".format(i) for i in range(M)])
        self.textBrowserNonlinerity.clear()
        self.textBrowserLuBang.clear()
        self.textBrowserLinearAppro.clear()
        self.textBrowserDifferUniformity.clear()
        self.textBrowserDiffusion.clear()
        self.textBrowserXiangshuFanwei.clear()
        self.textBrowserBalance.clear()
        self.textBrowserMaxdegree.clear()
        self.textBrowserBoolFunTT.clear()
        self.textBrowserBoolFunANF.clear()
        self.textBrowserDiffusionBf.clear()
        self.textBrowserRotation.clear()
        self.textBrowserXiangshu.clear()
        self.textBrowserBoolDegree.clear()
        self.checkBox.setChecked(False)
        self.textEditChooseBf.clear()
        # TODO clear
        self.textBrowserBu.clear()
        self.textBrowserDiffBranchnum.clear()
        #创建多线程，防止页面卡死
        self.latworker = LatWorkerThread()
        self.latworker.start()
        self.latworker.lat_appro_signal.connect(self.latbiasshow)
        self.worker = WorkerThread()
        self.worker.start()
        # test for NEW 性质 TODO
        self.worker.bu_signal.connect(self.bushow) 
        self.worker.diffBranchnum_signal.connect(self.diffBrnumshow)
        # old settings
        self.worker.term_dis_signal.connect(self.termdistributionshow)
        self.worker.dif_uni_signal.connect(self.diffuniformityshow)
        self.worker.nonlinearity_signal.connect(self.nonlinearityshow)
        self.worker.maxdegree_signal.connect(self.maxdegreeshow)
        self.worker.robust_signal.connect(self.robustshow)
        self.worker.balance_signal.connect(self.balanceshow)
        self.worker.diffusion_signal.connect(self.diffusionshow)
        self.worker.fault_signal.connect(self.faultshow)
        #完全雪崩准则表
        self.show_SAC_table(sbox,N,M)
        time.sleep(1.5)
        self.showmsg()

    def show_SAC_table(self,sbox,N,M):
        sac_table = SAC_table(sbox,N,M)
        global xuebeng
        xuebeng= sac_table
        self.tableWidget.setRowCount(N+1)
        self.tableWidget.setColumnCount(M)
        self.tableWidget.setHorizontalHeaderLabels(["j{}".format(i) for i in range(M-1, -1, -1)])
        verheadlabel = ["i{}".format(i) for i in range(1,N+1)]
        verheadlabel.append("平均值")
        self.tableWidget.setVerticalHeaderLabels(verheadlabel)
        for i in range(N):
            for j in range(M):
                item = QtWidgets.QTableWidgetItem("{:.6f}".format(sac_table[i][j]))
                self.tableWidget.setItem(i, j, item)
        a = []
        for i in range(M):
            a.append(sum(b[i] for b in sac_table)/N)
        for i in range(M):
            item = QtWidgets.QTableWidgetItem("{:.6f}".format(a[i]))
            self.tableWidget.setItem(N,i,item)
        avga = sum(a)/M*100
        self.textBrowserAvgSAC.setText("任一输入比特改变时，某一输出比特发生改变的平均概率约为{:.2f}%".format(avga))


    # =============> TODO 性质显示出来
    def diffBrnumshow(self,var):
        self.textBrowserDiffBranchnum.setText(str(var))
    def bushow(self,var):
        self.textBrowserBu.setText(str(var))
    # old 
    def termdistributionshow(self, var):
        self.textBrowserXiangshuFanwei.setText(str(var))
    def diffuniformityshow(self,var):
        self.textBrowserDifferUniformity.setText(var)
    def nonlinearityshow(self,var):
        self.textBrowserNonlinerity.setText(var)
    def maxdegreeshow(self,var):
        self.textBrowserMaxdegree.setText(var)
    def robustshow(self,var):
        self.textBrowserLuBang.setText(var)
        # time.sleep(1.2)
        # self.showmsg()
    def balanceshow(self,var):
        self.textBrowserBalance.setText(var)
    def diffusionshow(self,var):
        self.textBrowserDiffusion.setText(var)
    def latbiasshow(self,var):
        self.textBrowserLinearAppro.setText(var)
    def faultshow(self,var):
        msg = QMessageBox()
        msg.setWindowTitle("Failed")
        msg.setText(var)
        x = msg.exec()

    def output2(self):
        if self.checkBox.isChecked():
            choosebf = self.textEditChooseBf.toPlainText()
        else:
            choosebf = self.comboBoxComponentbf.currentText()
        try:
            (bf,num) = choose_bf(sbox,choosebf)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Failed")
            msg.setText("请确定自定义选择的函数正确且输入格式是按照 eg.x0或x1+x2+x3...")
            x = msg.exec()
            return 0
        if(num>=len(sbox)):
            msg = QMessageBox()
            msg.setWindowTitle("Failed")
            msg.setText("请确定选择的函数正确，在该S盒组成布尔函数的线性组合集合中")
            x = msg.exec()
        else:
            self.textBrowserBoolFunTT.setText("".join(map(str,bf)))
            (anf,degree) = ANF(bf)
            is_rotation = is_bf_rotation_symmetric(bf)
            self.textBrowserBoolFunANF.setText(anf)
            self.textBrowserBoolDegree.setText(str(degree))
            self.textBrowserXiangshu.setText(str(anf.count("+")+1))
            if is_rotation:
                self.textBrowserRotation.setText("具备")
            else:
                self.textBrowserRotation.setText("不具备")
            k = diffusion(bf,N,M)
            if k==0:
                self.textBrowserDiffusionBf.setText("不满足")
            else:
                self.textBrowserDiffusionBf.setText("k="+str(k))

    def showmsg(self):
        # global count
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("S盒性质已计算完毕，可以开始计算S盒的坐标函数等相关性质")
        x = msg.exec()

    def choosepath(self):
        self.pushButtonTxtOut.setDisabled(False)
        outputpath = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "C:")
        self.textBrowserPath.setText(outputpath)
        self.lineEditFileName.setDisabled(False)
    
    def tab2str(self,lis):
        row = ""
        for i in lis:
            row += str(i)
            row += "\n"
        print(row)
        
    def txtoutput(self):
        if self.lineEditFileName.text()=="":
            msg = QMessageBox()
            msg.setWindowTitle("Failed")
            msg.setText("请输入文件名")
            x = msg.exec()
        else:
            try:
                msg1 = QMessageBox()
                msg1.setWindowTitle("提醒")
                msg1.setText("正在生成S盒检测报告，请稍候。")
                x = msg1.exec()
                cmbf = get_coordinate_function(sbox,N,M)
                # 获取已有的输入
                diffBranchnum = self.textBrowserDiffBranchnum.toPlainText()
                boomerang_uni = self.textBrowserBu.toPlainText()
                nonli = self.textBrowserNonlinerity.toPlainText()
                latbias = self.textBrowserLinearAppro.toPlainText()
                diffuni = self.textBrowserDifferUniformity.toPlainText()
                is_diffusion = self.textBrowserDiffusion.toPlainText()
                robust = self.textBrowserLuBang.toPlainText()
                maxde = self.textBrowserMaxdegree.toPlainText()
                termrange = self.textBrowserXiangshuFanwei.toPlainText()
                is_balance = self.textBrowserBalance.toPlainText()
                avgsac = self.textBrowserAvgSAC.toPlainText()
                anfstr = ""
                cmn = len(cmbf)
                flag = 1
                for i in range(cmn):
                    (anf, degree) = ANF(cmbf[i])
                    rota = is_bf_rotation_symmetric(cmbf[i])
                    bfis_diffusion = diffusion(cmbf[i],N,M)
                    if rota == 1:
                        a = "具备"
                    else:
                        a = "不具备"
                        flag = 0
                    if bfis_diffusion==0:
                        bfis_diffusion_out="不满足"
                    else:
                        bfis_diffusion_out="满足"+str(bfis_diffusion)+"次扩散特性"
                    anfstr += "f{}的代数表达式为：{}\n\t其代数次数为：{}\t是否满足轮换对称性： {}\t扩散特性：{}\n\n".format(i, anf, degree,a,bfis_diffusion_out)
                filepath = self.textBrowserPath.toPlainText() + "/" + self.lineEditFileName.text()
                report = open(filepath, 'w')
                if flag == 0:
                    b = "不具备"
                else:
                    b = "具备"
                report.write("============================================\n")
                report.write("S盒检测报告\n")
                report.write("==================S盒的性质==================\n")
                a = "非线性度：\t\t" + nonli + '\n' + "代数次数：\t\t" + maxde + "\n" + "项数范围：\t\t" + termrange + "\n" + "线性逼近优势：\t\t" + latbias + "\n" + "差分均匀度：\t\t" + diffuni + "\n" + "鲁棒性：\t\t\t" + robust + "\n" + "扩散特性：\t\t" + is_diffusion + "\n"+"平衡性：\t\t\t" + is_balance + "\n"+"是否满足轮换对称性：\t"+b+"\n"+"雪崩概率指标：\t\t"+avgsac+"\n"+"差分分支数 \t\t"+diffBranchnum+"\n"+"回旋镖均匀度 \t\t"+boomerang_uni+"\n\n"
                report.write(a)
                report.write("================S盒的坐标函数================\n")
                report.write(anfstr)
                report.write("====================表格=====================\n")
                report.write("具体LAT、ACT、DDT等信息参见主页面")
                report.close()
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("检测报告已成功生成")
                x = msg.exec()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("请确定文件名输入正确")
                x = msg.exec()
    
    def show_BCT_table(self,sbox,N):
        bct1 = boomerang_connectivity_table(sbox,N)
        self.tableWidget.setRowCount(2**N)
        self.tableWidget.setColumnCount(2**N)
        self.tableWidget.setHorizontalHeaderLabels(["{} ".format(i) for i in range(1,2**N,1)])
        verheadlabel = ["{} ".format(i) for i in range(1,2**N,1)]
        self.tableWidget.setVerticalHeaderLabels(verheadlabel)
        for i in range(2**N):
            for j in range(2**N):
                item = QtWidgets.QTableWidgetItem("{}".format(bct1[i][j]))
                self.tableWidget.setItem(i, j, item)

    def show_table(self,sbox,N,M,tab):
        self.tableWidget.setRowCount(2**N)
        self.tableWidget.setColumnCount(2**M)
        self.tableWidget.setHorizontalHeaderLabels(["{} ".format(i) for i in range(1,2**N)])
        verheadlabel = ["{} ".format(i) for i in range(1,2**N)]
        self.tableWidget.setVerticalHeaderLabels(verheadlabel)
        for i in range(2**N):
            for j in range(2**M):
                item = QtWidgets.QTableWidgetItem("{}".format(tab[i][j]))
                self.tableWidget.setItem(i, j, item)
    
    def choose_tab(self):
        self.tableWidget.clear()
        tab = self.comboBoxTable.currentText()
        print("name = ",tab)
        if tab == "严格雪崩概率表SAC_TABLE":
            print("NO need to change")
        elif tab == "回旋镖连接表BCT":
            self.show_BCT_table(sbox,N)
        elif tab == "线性逼近表LAT":
            LAT = linear_approximation_table(sbox,N,M)
            self.show_table(sbox,N,M,LAT)
        elif tab == "差分分布表DDT":
            DDT = differential_distribution_table(sbox,N,M)
            self.show_table(sbox,N,M,DDT)
        elif tab == "自相关表ACT":
            ACT = autocorrelation_table(sbox,N,M)
            self.show_table(sbox,N,M,ACT)
        else:
            print("tab is other todo\n",tab)


class WorkerThread(QThread):
    # TODO
    diffBranchnum_signal = pyqtSignal(str)
    bu_signal = pyqtSignal(str)
    term_dis_signal = pyqtSignal(str)
    dif_uni_signal = pyqtSignal(str)
    nonlinearity_signal = pyqtSignal(str)
    maxdegree_signal = pyqtSignal(str)
    robust_signal = pyqtSignal(str)
    balance_signal = pyqtSignal(str)
    diffusion_signal = pyqtSignal(str)
    fault_signal = pyqtSignal(str)
    def run(self):
        try:
            # ===============》TODO
            diffBranchnum = get_diff_branch_number(sbox,N,M)
            self.diffBranchnum_signal.emit(str(diffBranchnum))
            boomerang_uni = boomerang_uniformity(sbox,N)
            self.bu_signal.emit(str(boomerang_uni))
            termnum = term_number_distribution(sbox,N,M)
            a = "{} ~ {}".format(min(termnum), max(termnum))
            self.term_dis_signal.emit(a)
            nonli = nonlinearity(sbox, N, M)
            self.nonlinearity_signal.emit(str(nonli))
            maxde = degree(sbox,N,M)[0]
            self.maxdegree_signal.emit(str(maxde))
            if (is_balanced(sbox, N, M) == True):
                self.balance_signal.emit("具备")
            else:
                self.balance_signal.emit("不具备")
            k = diffusion(sbox, N, M)
            print("computing diff_k=",k)
            if k==0:
                self.diffusion_signal.emit("不满足")
            else:
                self.diffusion_signal.emit("满足"+str(k)+"次扩散特性")
            diffuniformity= differential_uniformity(sbox, N, M)
            self.dif_uni_signal.emit("{}".format(diffuniformity))
            robust = robustness(sbox,N,M)
            self.robust_signal.emit("{:.6f}".format(robust))
        except IOError as e:
            self.fault_signal.emit("IOError",e)
        except ValueError as e:
            self.fault_signal.emit("IOValueError",e)

class LatWorkerThread(QThread):
    lat_appro_signal = pyqtSignal(str)
    fault_signal = pyqtSignal(str)
    def run(self):
        try:
            bias = int(2**(N-1)-nonlinearity(sbox,N,M))
            self.lat_appro_signal.emit("{}/{}={}".format(bias,2**N,bias/2**N))
        except:
            self.fault_signal.emit("进制或S盒输入有问题，请重新检查后使用")


if __name__=="__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    mshow=mywindow()
    mshow.show()
    sys.exit(app.exec_())

