# Five Styles - iOS通讯录头像集

一个精美的iOS通讯录头像集合，包含40个可爱的头像，专为个性化您的通讯录而设计。

## 📱 兼容应用

本项目需要配合以下iOS应用使用：
- **StevePinyin** - [App Store下载链接](https://apps.apple.com/us/app/stevepinyin/id6737565099?l=zh-Hans-CN)

## 🎨 头像预览

本头像集包含40个不同风格的头像：
- avatar_1.png - avatar_40.png
- 每个头像都经过精心设计，适合作为通讯录联系人头像
- 支持高清显示，适配各种iOS设备

## 📦 项目结构

```
ios_contact_avatar/
├── config.json          # 头像配置文件
├── full_bg.py           # 背景生成脚本
├── original/            # 原始图片文件夹
│   ├── avatar_1.png     # 原始头像文件1
│   ├── avatar_2.png     # 原始头像文件2
│   └── ...              # 其他原始头像文件
├── avatar_1.png         # 处理后的头像文件1
├── avatar_2.png         # 处理后的头像文件2
├── ...                  # 其他处理后的头像文件
├── avatar_40.png        # 处理后的头像文件40
└── README.md           # 项目说明文档
```

## 🚀 使用方法

### 1. 下载StevePinyin应用
- 在App Store中搜索"StevePinyin"或点击上方链接下载

### 2. 导入头像集
- 将本项目下载到本地
- 在StevePinyin应用中导入config.json文件
- 应用会自动读取配置并加载所有头像

### 3. 设置头像
- 在通讯录中选择联系人
- 从导入的头像集中选择喜欢的头像
- 保存设置

## 🛠️ 开发者工具

### full_bg.py 脚本使用

`full_bg.py` 是一个用于为头像添加随机彩色背景的Python脚本。

#### 安装依赖
```bash
pip install pillow
```

#### 使用方法

1. **准备原始图片**
   - 将原始头像图片放入 `original/` 文件夹中
   - 支持的格式：PNG, JPG, JPEG, WEBP

2. **运行脚本**
   ```bash
   python full_bg.py
   ```

3. **自定义配置**
   
   编辑 `full_bg.py` 中的参数：
   ```python
   # 背景透明度 (0-255)，数值越小越透明
   bg_alpha = 50   # 例如 80 就是大约 30% 不透明
   ```

#### 脚本功能
- 为 `original/` 文件夹中的所有图片添加随机彩色背景
- 自动保持原始图片的透明通道
- 支持多种图片格式
- 生成随机的RGB颜色背景
- 可自定义背景透明度

#### 输出结果
- 处理后的图片保存在项目根目录
- 控制台显示每个文件的处理信息，包括生成的背景颜色和透明度设置

## ⚙️ 配置文件说明

`config.json`文件包含头像的基本信息：
```json
{
  "name": "FiveStyles",
  "description": "",
  "icons": [
    {
      "name": "avatar_1",
      "url": "https://raw.githubusercontent.com/netxvul/ios_contact_avatar/main/avatar_1.png"
    },
    {
      "name": "avatar_2",
      "url": "https://raw.githubusercontent.com/netxvul/ios_contact_avatar/main/avatar_2.png"
    },
    // ... 其他头像配置
    {
      "name": "FiveStyles",
      "url": "https://raw.githubusercontent.com/netxvul/ios_contact_avatar/main/avatar_35.png"
    }
  ]
}
```

## 🌟 特性

- ✅ 40个精心设计的头像
- ✅ 高清图片质量
- ✅ 完整的配置文件
- ✅ 支持StevePinyin应用
- ✅ 开源免费使用
- ✅ 持续更新维护
- ✅ 包含背景生成工具
- ✅ 支持自定义背景样式

## 📄 许可证

本项目采用开源许可证，您可以自由使用、修改和分发。

## 🤝 贡献

欢迎提交问题报告和功能建议。如果您想为本项目贡献头像，请确保：
- 图片格式为PNG
- 建议尺寸为512x512像素
- 内容符合社区规范
- 更新相应的配置文件

### 贡献流程
1. 将新头像放入 `original/` 文件夹
2. 运行 `full_bg.py` 生成带背景的版本
3. 更新 `config.json` 文件添加新头像信息
4. 提交Pull Request

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- GitHub Issues: [提交问题](https://github.com/netxvul/ios_contact_avatar/issues)

## 🔗 相关链接

- [StevePinyin App Store](https://apps.apple.com/us/app/stevepinyin/id6737565099?l=zh-Hans-CN)
- [GitHub仓库](https://github.com/netxvul/ios_contact_avatar)
- [Pillow库文档](https://pillow.readthedocs.io/)

## 🔧 故障排除

### 常见问题

**Q: 运行full_bg.py时提示"没有找到pillow模块"**
A: 请先安装依赖：`pip install pillow`

**Q: 处理后的图片质量下降**
A: 可以调整脚本中的参数，使用更高透明度值

**Q: StevePinyin无法加载头像**
A: 请检查config.json文件格式和URL地址是否正确

---

**注意**: 本头像集仅用于个人通讯录个性化，请勿用于商业用途。使用前请确保已安装StevePinyin应用。