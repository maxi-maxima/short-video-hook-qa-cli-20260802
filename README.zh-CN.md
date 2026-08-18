# short-video-hook-qa-cli

一个轻量的短视频脚本质检工具，用来检查开头 hook、CTA 覆盖和分镜节奏，帮助创作者在录制前先修掉明显问题。

## 解决的痛点
短视频脚本很容易在第一句太平、缺少 CTA，或者分镜太模糊的时候直接失去留存。

## 为什么现在值得做
AI 辅助视频内容产出越来越多，一个简单的 QA 步骤可以防止明显的留存失误。

## 安装
无额外依赖，使用 Python 3.11+ 即可。

## 运行
```bash
python main.py --file script.txt
python main.py --file script.txt --genre tutorial --json
```

`--genre` 可以开启 `tutorial`、`product`、`story` 三类题材模板检查。

## 示例
输入：
```text
Stop scrolling.
Today I will show you a faster way to review code.
Scene 1: screen share.
CTA: save this for later.
```

输出：
```text
score: 94
hook: strong
cta: present
issues: 0
```

## 测试
```bash
python -m unittest discover -s tests -v
```

## 路线图
- 增加批量模式
- 增加适配 shorts / reels 的字数阈值
