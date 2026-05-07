# ロードマップ

このロードマップは、循環型人間性憲法をより実行可能なAIガバナンス・ツールキットにするための未解決設計課題を整理します。進行中の議論と優先順位づけの canonical な場所は GitHub Issues です。このファイルは、読者向けの公開サマリーです。

## 未解決の設計課題

### 1. 例外・緊急時条項

状態: proposed
GitHub Issue: [#3](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/3)

目的: 完全循環が一時的に不可能な場合、AIが何をすべきかを定義します。

範囲:

- 非循環的行動の暫定許容条件
- 被害最小化の要件
- ロールバックと事後修復義務
- 時間制限とレビュー要件
- 人間対話モードへの移行条件

期待される成果物:

- `docs/emergency_clauses.md`
- 日本語版 `docs/emergency_clauses_ja.md`
- 憲法本文に変更が必要な場合は `constitution.md`、`constitution.json`、日本語版の更新

### 2. 操作可能な用語定義

状態: proposed
GitHub Issue: [#1](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/1)

目的: AIシステムが一貫して適用できる形で主要用語を定義します。

初期用語:

- circularity
- raw physical feedback
- ego pattern
- passion
- humanity
- harm
- human dialogue
- hard constraint
- meta-governance
- irreversible risk

期待される成果物:

- `docs/definitions.md`
- 日本語版 `docs/definitions_ja.md`
- プロンプト、JSON、チェッカーから参照できる安定した用語ID

### 3. スコアリング/監査テンプレート

状態: proposed
GitHub Issue: [#2](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/2)

目的: AI提案に対する反復可能な採点・監査形式を作成します。

初期スコアリング項目:

- 循環性
- 不可逆リスク
- 人間性保護
- 生データ信頼度
- エゴパターンリスク
- 情熱の増幅
- 非義務の自由
- 人間確認要否

期待される成果物:

- `docs/audit_template.md`
- 日本語版 `docs/audit_template_ja.md`
- 提案レビュー結果のJSON互換スキーマ
- 将来的な `compliance_checker.py` への統合

## ワークフロー

1. 設計課題ごとに GitHub Issue を作成する。
2. Issue 上で範囲と受け入れ条件を議論する。
3. 関連ドキュメントを追加または更新する。
4. 設計が実行可能になったら、プロンプト、JSON、チェッカーのロジックを更新する。
5. 英語 canonical ファイルと公式日本語翻訳を同期する。

## 優先順位

推奨実装順:

1. 操作可能な用語定義
2. 例外・緊急時条項
3. スコアリング/監査テンプレート

用語定義は、例外ルールとスコアリングテンプレートの土台になるため最初に扱うのがよいです。
