# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'epoch.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class ShopUI(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(418, 298)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(418, 298))
        Form.setMaximumSize(QSize(418, 298))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.eat_shop_btn = QPushButton(Form)
        self.eat_shop_btn.setObjectName(u"eat_shop_btn")
        sizePolicy.setHeightForWidth(self.eat_shop_btn.sizePolicy().hasHeightForWidth())
        self.eat_shop_btn.setSizePolicy(sizePolicy)
        self.eat_shop_btn.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_4.addWidget(self.eat_shop_btn)

        self.flower_shop_btn = QPushButton(Form)
        self.flower_shop_btn.setObjectName(u"flowe_shop_btn")
        sizePolicy.setHeightForWidth(self.flower_shop_btn.sizePolicy().hasHeightForWidth())
        self.flower_shop_btn.setSizePolicy(sizePolicy)
        self.flower_shop_btn.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_4.addWidget(self.flower_shop_btn)

        self.groceryshop_btn = QPushButton(Form)
        self.groceryshop_btn.setObjectName(u"groceryshop_btn")
        sizePolicy.setHeightForWidth(self.groceryshop_btn.sizePolicy().hasHeightForWidth())
        self.groceryshop_btn.setSizePolicy(sizePolicy)
        self.groceryshop_btn.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_4.addWidget(self.groceryshop_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.epoch_label = QLabel(Form)
        self.epoch_label.setObjectName(u"epoch_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.epoch_label.sizePolicy().hasHeightForWidth())
        self.epoch_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.epoch_label, 0, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.left_money_label = QLabel(Form)
        self.left_money_label.setObjectName(u"left_money_label")
        sizePolicy1.setHeightForWidth(self.left_money_label.sizePolicy().hasHeightForWidth())
        self.left_money_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.left_money_label, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.cost_money_label = QLabel(Form)
        self.cost_money_label.setObjectName(u"cost_money_label")
        sizePolicy1.setHeightForWidth(self.cost_money_label.sizePolicy().hasHeightForWidth())
        self.cost_money_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.cost_money_label, 4, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.target_money_label = QLabel(Form)
        self.target_money_label.setObjectName(u"target_money_label")
        sizePolicy2.setHeightForWidth(self.target_money_label.sizePolicy().hasHeightForWidth())
        self.target_money_label.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.target_money_label, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.quality_progressBar = QProgressBar(Form)
        self.quality_progressBar.setObjectName(u"quality_progressBar")
        self.quality_progressBar.setValue(24)
        self.quality_progressBar.setTextVisible(False)

        self.horizontalLayout_3.addWidget(self.quality_progressBar)

        self.quality_add_btn = QPushButton(Form)
        self.quality_add_btn.setObjectName(u"quality_add_btn")
        self.quality_add_btn.setMinimumSize(QSize(30, 30))
        self.quality_add_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.quality_add_btn)

        self.quality_sub_btn = QPushButton(Form)
        self.quality_sub_btn.setObjectName(u"quality_sub_btn")
        self.quality_sub_btn.setMinimumSize(QSize(30, 30))
        self.quality_sub_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.quality_sub_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.efficiency_progressBar = QProgressBar(Form)
        self.efficiency_progressBar.setObjectName(u"efficiency_progressBar")
        self.efficiency_progressBar.setValue(24)
        self.efficiency_progressBar.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.efficiency_progressBar)

        self.efficiency_add_btn = QPushButton(Form)
        self.efficiency_add_btn.setObjectName(u"efficiency_add_btn")
        self.efficiency_add_btn.setMinimumSize(QSize(30, 30))
        self.efficiency_add_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.efficiency_add_btn)

        self.efficiency_sub_btn = QPushButton(Form)
        self.efficiency_sub_btn.setObjectName(u"efficiency_sub_btn")
        self.efficiency_sub_btn.setMinimumSize(QSize(30, 30))
        self.efficiency_sub_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.efficiency_sub_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.serve_progressBar = QProgressBar(Form)
        self.serve_progressBar.setObjectName(u"serve_progressBar")
        self.serve_progressBar.setValue(24)
        self.serve_progressBar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.serve_progressBar)

        self.serve_add_btn = QPushButton(Form)
        self.serve_add_btn.setObjectName(u"serve_add_btn")
        self.serve_add_btn.setMinimumSize(QSize(30, 30))
        self.serve_add_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.serve_add_btn)

        self.serve_sub_btn = QPushButton(Form)
        self.serve_sub_btn.setObjectName(u"serve_sub_btn")
        self.serve_sub_btn.setMinimumSize(QSize(30, 30))
        self.serve_sub_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.serve_sub_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.ensure_btn = QPushButton(Form)
        self.ensure_btn.setObjectName(u"ensure_btn")

        self.verticalLayout_2.addWidget(self.ensure_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e49\u5356\u5e97\u94fa", None))
        self.eat_shop_btn.setText(QCoreApplication.translate("Form", u"\u5c0f\u5403\u5e97", None))
        self.flower_shop_btn.setText(QCoreApplication.translate("Form", u"\u82b1\u5349\u5e97", None))
        self.groceryshop_btn.setText(QCoreApplication.translate("Form", u"\u767e\u8d27\u5e97", None))
        self.epoch_label.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8f6e\u6570", None))
        self.left_money_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u82b1\u8d39\u8d44\u91d1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5269\u4f59\u8d44\u91d1", None))
        self.cost_money_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u8d44\u91d1", None))
        self.target_money_label.setText(QCoreApplication.translate("Form", u"100000", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d28\u91cf", None))
        self.quality_add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.quality_sub_btn.setText(QCoreApplication.translate("Form", u"\u2014\u2014", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6548\u7387", None))
        self.efficiency_add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.efficiency_sub_btn.setText(QCoreApplication.translate("Form", u"\u2014\u2014", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u670d\u52a1", None))
        self.serve_add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.serve_sub_btn.setText(QCoreApplication.translate("Form", u"\u2014\u2014", None))
        self.ensure_btn.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi

