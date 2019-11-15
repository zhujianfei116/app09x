from selenium.webdriver.common.by import By


class PageElements:
    """定义所有页面元素"""

    """短信首页"""
    home_new_btn_id = (By.ID, "com.android.mms:id/action_compose_new")

    """短信新建页面"""
    # 接收人
    new_recv_phone_id = (By.ID, "com.android.mms:id/recipients_editor")
    # 短信输入框
    new_input_text_id = (By.ID, "com.android.mms:id/embedded_text_editor")
    # 短信发送按钮
    new_send_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
    # 发送结果
    new_send_sms_result_ids = (By.ID, "com.android.mms:id/text_view")

    """设置首页"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")

    """设置-搜索页面元素"""
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 结果列表
    search_result = (By.ID, "com.android.settings:id/title")
