# -*- coding:utf-8 -*-
import base64
import hashlib
import time
from tkinter import Button, Entry, Frame, Label, LabelFrame, Text, Tk

from utils import set_window_center

__author__ = 'doudoudzj'
__version__ = '0.0.1'
__license__ = 'BSD'


# 获取当前时间
def get_current_time():
    current_time = time.localtime(time.time())
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', current_time)
    return current_time


class GUI():
    def __init__(self, master):
        self.master = master
        master.title('文本处理工具 V%s' % __version__)
        master.configure(relief='ridge', padx=5, pady=5)
        set_window_center(master, 700, 600)
        self.init_area_source()
        self.init_area_btns()
        self.init_area_target()
        self.init_area_log()

    def init_area_source(self):
        # 待处理区
        frm_source = LabelFrame(self.master,
                                text='待处理数据',
                                padx=5,
                                pady=5)
        frm_source.pack(fill='both', expand=True)

        # 待处理文本
        self.init_data_Text = Text(frm_source,
                                    width=50,
                                    height=10,
                                    borderwidth=1,
                                    highlightcolor='#ddd',
                                    insertborderwidth=1)
        self.init_data_Text.pack(fill='both', expand=True)

    def init_area_btns(self):
        # 中间：功能区
        frm_btns = Frame(self.master)
        frm_btns.pack(fill='x')

        # 按钮 MD5 生成
        Button(frm_btns, text='MD5 生成', command=self.md5str).pack(side='left')
        # 按钮 Base64 编码
        Button(frm_btns, text='Base64 编码', command=self.b64encode).pack(side='left')
        # 按钮 Base64 解码
        Button(frm_btns, text='Base64 解码', command=self.b64decode).pack(side='left')
        # 按钮 Base32 编码
        Button(frm_btns, text='Base32 编码', command=self.b32encode).pack(side='left')
        # 按钮 Base32 解码
        Button(frm_btns, text='Base32 解码', command=self.b32decode).pack(side='left')

    def init_area_target(self):
        # 输出区
        frm_target = LabelFrame(self.master,
                                text='输出结果',
                                padx=5,
                                pady=5)
        frm_target.pack(fill='both', expand=True)

        # 处理结果展示
        self.res_data = Text(frm_target,
                            width=50,
                            height=10,
                            borderwidth=1,
                            highlightcolor='#ddd')
        self.res_data.pack(fill='both', expand=True)

    def init_area_log(self):
        # 日志区
        frm_log = LabelFrame(self.master,
                            text='日志',
                            padx=5,
                            pady=5)
        frm_log.grid(row=1, column=0, columnspan=3, sticky='ew')
        frm_log.pack(fill='both', expand=True)

        # 日志
        self.log_text = Text(frm_log, 
                            borderwidth=1,
                            highlightcolor='#ddd')
        self.log_text.pack(fill='both', expand=True)

    def md5str(self):
        # MD5 生成
        src = self.init_data_Text.get(1.0, 'end')
        if src is not None:
            try:
                md5 = hashlib.md5()
                md5.update(src.encode())
                md5_str = md5.hexdigest()
                # 清空
                self.res_data.delete(1.0, 'end')
                # 输出
                self.res_data.insert(1.0, md5_str)
                # 日志
                self.print_log('INFO:MD5 成功 %s' % md5_str)
            except:
                self.res_data.delete(1.0, 'end')
                self.res_data.insert(1.0, '字符串转MD5失败')
        else:
            self.print_log('ERROR:MD5 failed')

    def b64encode(self):
        # Base64 编码
        src = self.init_data_Text.get(1.0, 'end')
        if src is not None:
            try:
                res = base64.b64encode(src.encode('ascii'))
                res = res.decode('ascii')
                # 清空
                self.res_data.delete(1.0, 'end')
                # 输出
                self.res_data.insert(1.0, res)
                self.print_log('INFO:Base64 success %s' % res)
            except:
                self.res_data.delete(1.0, 'end')
                self.res_data.insert(1.0, 'Base64 编码失败')
        else:
            self.print_log('ERROR:Base64 编码失败')

    def b64decode(self):
        # Base64 解码
        src = self.init_data_Text.get(1.0, 'end')
        if src is not None:
            try:
                res = base64.b64decode(src.encode('ascii'))
                # 清空
                self.res_data.delete(1.0, 'end')
                # 输出
                self.res_data.insert(1.0, res)
                self.print_log('INFO:Base64 解码成功 %s' % res)
            except:
                self.res_data.delete(1.0, 'end')
                self.res_data.insert(1.0, 'Base64 解码失败')
        else:
            self.print_log('ERROR:Base64 解码失败')

    def b32encode(self):
        # Base32 编码
        src = self.init_data_Text.get(1.0, 'end')
        if src is not None:
            try:
                res = base64.b32encode(src.encode('ascii'))
                res = res.decode('ascii')
                # 清空
                self.res_data.delete(1.0, 'end')
                # 输出
                self.res_data.insert(1.0, res)
                self.print_log('INFO:Base32 success %s' % res)
            except:
                self.res_data.delete(1.0, 'end')
                self.res_data.insert(1.0, 'Base32 编码失败')
        else:
            self.print_log('ERROR:Base32 编码失败')

    def b32decode(self):
        # Base32 解码
        src = self.init_data_Text.get(1.0, 'end')
        if src is not None:
            try:
                res = base64.b32decode(src.encode('ascii'))
                # 清空
                self.res_data.delete(1.0, 'end')
                # 输出
                self.res_data.insert(1.0, res)
                self.print_log('INFO:Base32 解码成功 %s' % res)
            except:
                self.res_data.delete(1.0, 'end')
                self.res_data.insert(1.0, 'Base32 解码失败')
        else:
            self.print_log('ERROR:Base32 解码失败')

    def print_log(self, msg):
        # 日志动态打印
        current_time = get_current_time()
        msg_str = str(current_time) + ' ' + str(msg) + '\n'
        self.log_text.insert('end', msg_str)


if __name__ == '__main__':
    root = Tk()
    App = GUI(root)

    root.mainloop()
