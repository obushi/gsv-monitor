#!/usr/bin/env python3
"""data.json から日本＋石川県の撮影予定を抽出し state/streetview-ishikawa.json に保存する。

出力ファイルには実行時刻などの揺れる値を入れない（内容が変わった時だけ
git コミットが発生し、クラウド側の差分検知がノイズなく効くようにするため）。
"""
import json
import os

COUNTRY = "Japan"
REGION = "Ishikawa"

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

japan = [x for x in data if x.get("country", "") == COUNTRY]
ishi = next((x for x in japan if x.get("region", "") == REGION), None)


def d10(v):
    return (v or "None")[:10]


if ishi:
    line = "Ishikawa | districts: {d} | publish: {p} | {s}〜{e}".format(
        d=ishi.get("districts", "None"),
        p=ishi.get("publish", "None"),
        s=d10(ishi.get("datestart")),
        e=d10(ishi.get("dateend")),
    )
else:
    line = "石川県のエントリなし（現在、撮影予定に石川は含まれていません）"

out = {
    "ishikawa": line,
    "ishikawaRaw": ishi,
    "japanRegionsPublished": [x["region"] for x in japan if x.get("publish") == "Yes"],
}

os.makedirs("state", exist_ok=True)
with open("state/streetview-ishikawa.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(line)
