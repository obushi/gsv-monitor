# streetview-monitor

Google ストリートビューの「今月撮影を予定している場所」データ
(`https://www.google.com/streetview/static/feed/driving/data.json`) を
GitHub Actions で毎日取得し、**石川県 (Ishikawa)** の撮影予定を
`state/streetview-ishikawa.json` に書き出す。

Claude のクラウドルーティン（毎朝のデイリーダイジェスト）が、この state ファイルを
`raw.githubusercontent.com` 経由で読み、前回との差分（石川県の撮影予定の変化）を検知する。

## 仕組み
- `.github/workflows/streetview.yml` … 毎日 06:30 JST に実行（手動実行も可）
- `scripts/extract.py` … data.json から日本＋石川を抽出
- `state/streetview-ishikawa.json` … 抽出結果（内容が変わった時だけ更新）

## 初回セットアップ
1. このリポジトリを **public** で作成し push
2. Actions タブ → `streetview-monitor` → **Run workflow** で初回実行
3. `state/streetview-ishikawa.json` が生成されることを確認
