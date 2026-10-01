#!/usr/bin/env python3
"""Roll a compact Chinese-language story prompt."""

import argparse
import random


PLACES = (
    "只在雨夜的镜子里出现的旧集市",
    "会吞掉回声的山中旅馆",
    "每晚少一条街的港口城",
    "建在巨鲸背上的邮局",
    "所有钟都比太阳快七分钟的小镇",
    "只收失物、不收钱的火车站",
    "地图上会随着传闻移动的森林",
    "每扇门后都通往同一间厨房的公寓",
)

TROUBLES = (
    "城里所有人的影子都在日落后离家出走",
    "一封写给明天的信提前送到了",
    "每把钥匙都能打开同一扇没人承认的门",
    "一场暴雨只淋湿撒谎的人",
    "收藏家丢失了最后一个不会说话的东西",
    "整座城忘了昨天，只有一只猫记得",
    "午夜的列车每次都少带回一位乘客",
    "一个陌生人的名字出现在所有人的梦里",
)

TWISTS = (
    "求助者其实是多年后的你自己",
    "所谓的宝藏，是一件迟迟没送出的道歉",
    "解决问题的代价，是留下一个小小的谜团",
    "看起来最可疑的人，正在保护真正的故事",
    "线索全都是真的，只是顺序被打乱了",
    "反派并不想赢，只想让某个人亲口拒绝",
    "事情会在有人说出愿望时立刻结束",
    "最后的选择由最不起眼的旁观者决定",
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="生成一个离线中文故事灵感。")
    parser.add_argument("--seed", type=int, help="指定数字种子，方便复现")
    args = parser.parse_args(argv)

    seed = args.seed
    if seed is None:
        seed = random.SystemRandom().randrange(2**32)
    rng = random.Random(seed)

    print("故事种子")
    print(f"地点：{rng.choice(PLACES)}")
    print(f"麻烦：{rng.choice(TROUBLES)}")
    print(f"反转：{rng.choice(TWISTS)}")
    print(f"复现用种子：{seed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
