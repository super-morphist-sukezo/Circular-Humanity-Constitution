# 翻訳ポリシー

循環型人間性憲法では、英語を実装上の canonical language、日本語を公式翻訳として扱います。

## 基準ファイル

- `README.md`
- `constitution.md`
- `constitution.json`
- `prompts/self_critique_prompt.md`
- `prompts/human_dialogue_triggers.md`

これらは、実装、相互運用、他AIシステムとの連携における主参照です。

## 公式日本語ファイル

- `README_ja.md`
- `constitution_ja.md`
- `constitution_ja.json`
- `prompts/self_critique_prompt_ja.md`
- `prompts/human_dialogue_triggers_ja.md`

日本語ファイルは単なるメモではなく公式翻訳です。プロジェクトの原思想のニュアンスを保持しつつ、英語版と整合させます。

## 同期ルール

1. `article_1` や `article_9` などの条文 ID は言語間で固定します。
2. ハード制約、改正手続き、プロンプト、実行プロトコルを変更する場合は、できる限り同じ Pull Request で英日両方を更新します。
3. 差異を見つけた場合は、対象ファイル、条文 ID、解決案を issue に記録します。
4. 実装時に言語版が衝突した場合は、一時的に英語 canonical 版を優先し、その後レビューで両言語版を修正します。
5. 日本語のニュアンスが英語に完全には移らない場合は、黙って平準化せず、issue または commit message に記録します。

## JSON 設計

英語版と日本語版の JSON は分離します。これにより、AI システムや開発者ツールが言語混在なしに読み込めます。対応関係は安定した ID と条文番号で維持します。
