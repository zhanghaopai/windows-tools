import json


def format_json_content(input_edit, output_edit):
    """
    JSON格式化核心逻辑（纯业务逻辑，与UI解耦）
    :param input_edit: 输入文本框控件
    :param output_edit: 输出文本框控件
    """
    try:
        input_text = input_edit.toPlainText().strip()
        if not input_text:
            output_edit.setText("⚠️ 请输入JSON内容！")
            return

        # 解析并格式化JSON（支持中文）
        json_data = json.loads(input_text)
        formatted_json = json.dumps(
            json_data,
            indent=4,  # 缩进4个空格
            ensure_ascii=False,  # 保留中文
            sort_keys=False  # 不排序键
        )
        output_edit.setText(formatted_json)

    except json.JSONDecodeError as e:
        output_edit.setText(f"❌ JSON解析失败：\n{str(e)}")
    except Exception as e:
        output_edit.setText(f"❌ 处理失败：\n{str(e)}")


# 扩展：可添加JSON压缩功能（一行显示）
def compress_json_content(input_edit, output_edit):
    """JSON压缩（去掉空格和换行）"""
    try:
        input_text = input_edit.toPlainText().strip()
        if not input_text:
            output_edit.setText("⚠️ 请输入JSON内容！")
            return

        json_data = json.loads(input_text)
        compressed_json = json.dumps(
            json_data,
            separators=(",", ":"),  # 压缩分隔符
            ensure_ascii=False
        )
        output_edit.setText(compressed_json)

    except Exception as e:
        output_edit.setText(f"❌ 压缩失败：\n{str(e)}")