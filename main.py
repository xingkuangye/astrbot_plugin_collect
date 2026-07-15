from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("astrbot_plugin_collect", "星星旁の旷野", "一个简单的 用户反馈收集 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("举报")
    async def report(self, event: AstrMessageEvent):
        """接收用户举报"""
        try:
            user_name = event.get_sender_name()
            message_str = event.message_str # 用户发的纯文本消息字符串
            feedback_num = await self.get_kv_data("feedback_num", 0) + 1
            await self.put_kv_data("feedback_num", feedback_num)
            feedback_message = f"用户 {user_name} 举报了第 {feedback_num} 条消息：\n\n{message_str}"
            await self.put_kv_data(f"feedback_{feedback_num}", feedback_message) # 将反馈消息存储到 KV 数据库中
            yield event.plain_result(f"感谢您提供的举报信息~\n> 爱丽丝会因此变得更好的！") # 发送一条纯文本消息
        except Exception as e:
            yield event.plain_result(f"处理您的举报时出现了错误，请稍后再试")
            logger.error(f"处理用户举报时出错: {e}")


    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("反馈")
    async def feedback(self, event: AstrMessageEvent):
        """接收用户反馈"""
        try:
            user_name = event.get_sender_name()
            message_str = event.message_str # 用户发的纯文本消息字符串
            feedback_num = await self.get_kv_data("feedback_num", 0) + 1
            await self.put_kv_data("feedback_num", feedback_num)
            feedback_message = f"用户 {user_name} 反馈了第 {feedback_num} 条消息：\n\n{message_str}"
            await self.put_kv_data(f"feedback_{feedback_num}", feedback_message) # 将反馈消息存储到 KV 数据库中
            yield event.plain_result(f"感谢您的反馈~\n> 爱丽丝会因此变得更好的！") # 发送一条纯文本消息
        except Exception as e:
            yield event.plain_result(f"处理您的反馈时出现了错误，请稍后再试")
            logger.error(f"处理用户反馈时出错: {e}")

    @filter.command("get_feedback")
    async def get_feedback(self, event: AstrMessageEvent, feedback_num: str):
        """获取用户反馈"""
        feedback_message = await self.get_kv_data(f"feedback_{feedback_num}", None)
        if feedback_message is None:
            yield event.plain_result(f"未找到第 {feedback_num} 条反馈消息。")
            return
        chain = event.plain_result(f"第 {feedback_num} 条反馈消息：\n\n{feedback_message}")
        chain.use_markdown_ = False
        yield chain
    
    @filter.command("feedback_count")
    async def feedback_count(self, event: AstrMessageEvent):
        """获取反馈消息总数"""
        feedback_num = await self.get_kv_data("feedback_num", 0)
        yield event.plain_result(f"当前共有 {feedback_num} 条反馈消息。")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
