from Base.base import Base
from Page.pageElements import PageElements


class SenSmsPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def recv_phone(self, phone):
        """
        输入接收人
        :param phone: 手机号
        :return:
        """
        self.send_ele(PageElements.new_recv_phone_id, phone)

    def send_sms(self, text):
        """
        发送短信
        :param text: 发送短信内容
        :return:
        """
        # 输入
        self.send_ele(PageElements.new_input_text_id, text)
        # 点击发送
        self.click_ele(PageElements.new_send_btn_id)

    def get_sms_result(self):
        """获取短信发送结果"""
        # 定位所有已发送内容
        results = self.search_eles(PageElements.new_send_sms_result_ids)
        # 返回所有text列表
        return [i.text for i in results]
