# Discord Bot Sample

シンプルなDiscord Botです。すべてのメッセージに「こんにちは」と返信します。

## 現在の状態

✅ **完了済み**：
- Discord Bot のコード作成完了
- .envファイルでトークン管理
- .gitignoreファイル作成
- Gitリポジトリ初期化
- 初期コミット作成済み
- Botは正常に動作中（バックグラウンドで実行中）
- GitHubリポジトリ作成完了
- コードをGitHubにプッシュ済み
  - URL: https://github.com/koubun-osho/discord-bot-sample

📝 **次回の作業候補**：
- Botの機能拡張（コマンド追加、リアクション機能など）
- エラーハンドリングの改善
- ログ機能の追加
- Docker化
- GitHub Actionsでの自動テスト設定

## セットアップ方法

1. 依存関係のインストール：
```bash
pip3 install -r requirements.txt
```

2. `.env`ファイルにDiscord Botトークンを設定（設定済み）

3. Botの起動：
```bash
python3 bot.py
```

## ファイル構成

- `bot.py` - メインのBotコード
- `requirements.txt` - 必要なパッケージ
- `.env` - トークン設定（Gitには含まれない）
- `.gitignore` - Git除外設定

## 次回再開時のコマンド

最新のコードを取得：
```bash
git pull origin main
```

Botを起動：
```bash
python3 bot.py
```