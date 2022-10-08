import sys
import time
from functools import partial
from typing import List, Set
from threading import Thread
from PySide6.QtCore import Qt, QMetaMethod, QObject
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton
from ui.epoch import ShopUI

num_shops = 3


def test():
    print(124)


class ShopWidget(QWidget):
    def __init__(self, game_manager: 'GameManager'):
        self.game_manager = game_manager
        super(ShopWidget, self).__init__()
        # 加载Designer生成的ui
        self.ui = ShopUI()
        self.ui.setupUi(self)
        self.cur_shop = self.game_manager.shop_list[0]
        self.update_shop_info(self.cur_shop)
        # 切换店铺
        self.ui.eat_shop_btn.clicked.connect(partial(self.change_shop, 0))
        self.ui.flower_shop_btn.clicked.connect(partial(self.change_shop, 2))
        self.ui.groceryshop_btn.clicked.connect(partial(self.change_shop, 1))
        # 加减
        self.ui.serve_add_btn.clicked.connect(partial(self.add_indicator, 'serve', 20000))
        self.ui.quality_add_btn.clicked.connect(partial(self.add_indicator, 'quality', 20000))
        self.ui.efficiency_add_btn.clicked.connect(partial(self.add_indicator, 'efficiency', 20000))

        self.ui.serve_sub_btn.clicked.connect(partial(self.sub_indicator, 'serve', 20000))
        self.ui.quality_sub_btn.clicked.connect(partial(self.sub_indicator, 'quality', 20000))
        self.ui.efficiency_sub_btn.clicked.connect(partial(self.sub_indicator, 'efficiency', 20000))

    def add_indicator(self, indicator, num):
        self.game_manager.player.improve_indicator(self.cur_shop, indicator, num)
        self.update_shop_info(self.cur_shop)

    def sub_indicator(self, indicator, num):
        self.game_manager.player.cancel_improve_indicator(self.cur_shop, indicator, num)
        self.update_shop_info(self.cur_shop)

    def update_shop_info(self, shop: 'Shop'):
        # 修改title
        self.setWindowTitle(shop.name)
        # 修改 label
        self.ui.left_money_label.setText(str(self.game_manager.player.money))
        self.ui.cost_money_label.setText(str(shop.used_money))
        self.ui.epoch_label.setText(str(self.game_manager.epoch))
        self.ui.target_money_label.setText(str(self.game_manager.target_money))
        # 修改 progress bar
        indicators = shop.show_indicators()
        print(indicators)
        print(shop.max_indicator())
        self.ui.serve_progressBar.setMaximum(shop.max_indicator())
        self.ui.serve_progressBar.setValue(indicators['serve'])

        self.ui.quality_progressBar.setMaximum(shop.max_indicator())
        self.ui.quality_progressBar.setValue(indicators['quality'])

        self.ui.efficiency_progressBar.setMaximum(shop.max_indicator())
        self.ui.efficiency_progressBar.setValue(indicators['efficiency'])

    def change_shop(self, shop_idx):
        self.cur_shop = self.game_manager.shop_list[shop_idx]
        self.update_shop_info(self.cur_shop)


class Player:
    def __init__(self, money: int = 0, strategies=None):
        if strategies is None:
            strategies = set()

        self.money = money
        self.strategies = strategies
        self.used_strategies = set()

    def add_strategy(self, shop, strategy):
        # ToDo 判断当前策略是否已经被使用
        if strategy not in self.used_strategies:
            self.used_strategies.add(strategy)
            return shop.add_strategy(strategy)

    def remove_strategy(self, shop, strategy):
        if strategy in self.used_strategies:
            self.used_strategies.remove(strategy)
            return shop.remove_strategy(strategy)

    def improve_indicator(self, shop, indicator, num: int) -> bool:
        if self.money - num >= 0:
            if shop.improve_indicator(indicator, num):
                self.money -= num
                return True
            else:
                return False
        else:
            return False

    def cancel_improve_indicator(self, shop, indicator, num: int) -> bool:
        if shop.cancel_improve_indicator(indicator, num):
            self.money += num
            return True
        else:
            return False


class Shop:
    def __init__(self, shop_name):
        self.name = shop_name
        # 基础指标
        self.__indicators = {
            'quality': 0,
            'efficiency': 0,
            'serve': 0
        }
        # 运行时指标
        self.__added_indicators = {
            'quality': 0,
            'efficiency': 0,
            'serve': 0
        }
        # 目标指标
        self.__target_indicators = {
            'quality': 1000,
            'efficiency': 1000,
            'serve': 1000
        }
        # 最大值
        self.__max_indicator = 100000
        # 策略
        self.__strategy_list: Set[Strategy] = set()
        self.max_strategy_len = num_shops
        #
        self.used_money = 0

    def max_indicator(self):
        return self.__max_indicator

    def can_add_strategy(self) -> bool:
        if len(self.__strategy_list) < self.max_strategy_len:
            return True
        else:
            return False

    def can_remove_strategy(self) -> bool:
        return not self.can_add_strategy()

    def add_strategy(self, strategy: 'Strategy'):
        if strategy not in self.__strategy_list and self.can_add_strategy():
            self.__strategy_list.add(strategy)
            return True
        else:
            return False

    def remove_strategy(self, strategy):
        if strategy in self.__strategy_list and self.can_remove_strategy():
            self.__strategy_list.remove(strategy)
        else:
            return True

    def improve_indicator(self, indicator, num) -> bool:
        """
        :param indicator: 需要提升的指标
        :param num: 花费的money数量
        :return: 提升成功与否
        """
        _ = self.show_indicators()  # 获取最终计算后的指标值 进行比较
        if _[indicator] + num > self.__max_indicator:
            return False
        else:
            self.__added_indicators[indicator] += num
            self.used_money += num
            return True

    def cancel_improve_indicator(self, indicator, num) -> bool:
        if self.__added_indicators[indicator] - num < self.__indicators[indicator]:
            return False
        else:
            self.__added_indicators[indicator] -= num
            self.used_money -= num
            return True

    def show_indicators(self):
        """
        :return:返回分配时指标副本在策略作用下的副本
        """
        show_indicators = self.__added_indicators.copy()
        for strategy in self.__strategy_list:
            # ToDo 完成 策略影响 运行时指标数量
            pass
        return show_indicators

    def settlement(self) -> int:
        """
        确认结算资金,更新基本指标
        :return:
        """
        self.__indicators = self.__added_indicators.copy()
        # TODo 完成收益函数 --> 想要使用边际递减函数
        earnings = 10000
        # ToDo 优化更新下一局的目标
        for indicator, target in self.__target_indicators:
            self.__target_indicators[indicator] = int(target * 1.5)
        return earnings


class Strategy:
    def __init__(self):
        pass

    def __call__(self, indicators: dict):
        return indicators.copy()


class Event:
    pass


class GameManager:
    def __init__(self):
        self.epoch = 1
        self.start_money = 10000000000
        self.target_money = 1000000
        self.player = Player(self.start_money, set())
        self.shop_list = [Shop('小吃店'), Shop('百货店'), Shop('花卉店')]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_manager = GameManager()
    widget = ShopWidget(game_manager)
    widget.show()
    app.exec()
