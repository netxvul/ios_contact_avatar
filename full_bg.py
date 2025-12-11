# 安装依赖
#  pip install pillow

import os
import random
from PIL import Image

input_dir = "original"
output_dir = "./"

os.makedirs(output_dir, exist_ok=True)

# 背景透明度 (0-255)，例如 80 就是大约 30% 不透明
bg_alpha = 50   # 你想更透明就改小，想更实就改大

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

for filename in os.listdir(input_dir):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        continue

    src_path = os.path.join(input_dir, filename)
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size

    # 生成随机背景
    r, g, b = random_color()
    bg = Image.new("RGBA", (w, h), (r, g, b, bg_alpha))

    # 合成背景和原图
    result = Image.alpha_composite(bg, img)

    # 保存
    out_path = os.path.join(output_dir, filename)
    result.save(out_path)

    print("完成:", filename, "背景:", (r, g, b), "透明度:", bg_alpha)

print("全部处理完了，你现在应该笑一个。")
