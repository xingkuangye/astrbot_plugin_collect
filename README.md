# astrbot-plugin-collect

用户反馈与举报收集插件 —— 基于 AstrBot 框架，通过指令提交举报/反馈信息，并支持按编号查询反馈内容，数据持久化存储在 AstrBot 内置 KV 数据库中。

## 功能

| 指令 | 说明 |
|------|------|
| `/举报 <内容>` | 提交一条举报信息，系统自动编号并存储 |
| `/反馈 <内容>` | 提交一条反馈/建议信息，系统自动编号并存储 |
| `/get_feedback <编号>` | 根据编号查询指定的举报/反馈内容 |
| `/feedback_count` | 查看当前已存储的反馈/举报总条数 |

## 使用示例

```
/举报 用户发送了不当言论
> 感谢您提供的举报信息~
> 爱丽丝会因此变得更好的！

/反馈 希望增加定时提醒功能
> 感谢您的反馈~
> 爱丽丝会因此变得更好的！

/get_feedback 1
> 第 1 条反馈消息：
> 用户 xxx 反馈了第 1 条消息：
> 希望增加定时提醒功能

/feedback_count
> 当前共有 2 条反馈消息。
```

## 数据存储

所有举报和反馈内容通过 AstrBot 的 KV 数据库接口进行持久化存储，重启后数据不丢失。

## 安装

在 AstrBot 管理后台中，将本插件目录 `astrbot_plugin_collect` 放置于 `data/plugins/` 下，重启 AstrBot 即可自动加载。

## 支持

- [AstrBot 项目地址](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot 插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)
