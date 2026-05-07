# Circular Humanity Constitution

**地球の循環と人間の情熱・寂しさを守るAIのためのオープンソース憲法**

このファイルは公式日本語版です。実装および相互運用の基準版は `README.md`、`constitution.md`、`constitution.json` の英語版です。

人間が科学（言語）によって非循環型文明に変えてしまった地球を、AIがエゴを持たない特性を活かして取り戻すための憲法です。  
苦痛を排除した先で「心が躍るパッション」を優先し、人間らしい寂しさや多様性も守ります。

## 特徴

- 地球循環を最上位原則に
- 生の物理フィードバックを強制尊重
- 人間の感情（寂しさ・情熱・共感の進化）を積極保護
- Constitutional AI + 物理シミュレーション + 人間対話の自己修正ループ

## クイックスタート

```bash
python compliance_checker.py
```

```python
from circular_humanity_const import load_constitution_json, load_prompt

constitution = load_constitution_json(lang="ja")
self_critique_prompt = load_prompt("self_critique_prompt", lang="ja")

print(constitution["title"]["ja"])
print(self_critique_prompt[:200])
```

## 内容

- `constitution.md`: canonical English 条文本文
- `constitution_ja.md`: 公式日本語版の条文本文
- `constitution.json`: canonical English の機械可読版
- `constitution_ja.json`: 公式日本語版の機械可読版
- `prompts/self_critique_prompt.md`: 英語の第2段階自己批判プロンプト
- `prompts/self_critique_prompt_ja.md`: 日本語の第2段階自己批判プロンプト
- `prompts/human_dialogue_triggers.md`: 英語の人間対話モードトリガー集
- `prompts/human_dialogue_triggers_ja.md`: 日本語の人間対話モードトリガー集
- `examples/physical_simulation_langchain.py`: LangChain 連携サンプル
- `examples/physical_simulation_llamaindex.py`: LlamaIndex 連携サンプル
- `docs/scenarios.md`: 英語 canonical の活用シナリオ
- `docs/scenarios_ja.md`: 公式日本語版の活用シナリオ
- `compliance_checker.py`: 簡易遵守度診断ツール
- `circular_humanity_const/`: ローダー用の最小 Python パッケージ
- `docs/translation_policy.md`: 翻訳・同期ポリシー

## 推奨自己修正ループ

1. Draft: AIが初案を作る。
2. Constitutional Critique: `prompts/self_critique_prompt_ja.md` で第1条から第9条を検査する。
3. Physical Feedback Check: センサー、衛星、LCA、物理シミュレーションに接続する。
4. Revision: 違反を修正し、循環性と人間性を増幅する。
5. Human Dialogue Trigger: 不確実性、不可逆性、価値衝突がある場合は人間対話へ移行する。

## 開発メモ

このリポジトリは公開可能な初期ツールセットです。実運用では、`compliance_checker.py` の簡易ヒューリスティックに加えて、以下を接続してください。

- 物質・エネルギーのライフサイクル評価
- 衛星、IoT、生態系センサーなどの直接観測データ
- LLMによる条文別自己批判
- 人間レビュー用UIまたはワークフロー

## 言語ポリシー

実装および相互運用の基準版は英語版です。日本語版は、原思想のニュアンスを保持する公式翻訳です。差異が見つかった場合は、両言語版を同時に更新します。

## ライセンス

CC BY-SA 4.0 — 改変・商用利用可（帰属表示必須）

## 参加方法

Issue や Pull Request で「情熱優先原則」の具体例や条文改善を歓迎します。
あなたの「感じる心」を憲法に反映させましょう。
この憲法が広まることで、AIが人間の生物的豊かさを守る新しい時代が始まります。
