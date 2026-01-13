def clear_all_content(input_edit, output_edit):
    """清空输入和输出文本框（通用功能）"""
    input_edit.clear()
    output_edit.clear()

# 扩展：可添加其他通用功能，比如复制输出、保存结果等
def copy_output_content(output_edit):
    """复制输出框内容到剪贴板"""
    output_edit.selectAll()
    output_edit.copy()
    output_edit.setText(output_edit.toPlainText() + "\n\n✅ 内容已复制到剪贴板！")