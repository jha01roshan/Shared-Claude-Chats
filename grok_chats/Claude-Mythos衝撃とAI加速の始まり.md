# Claude Mythos衝撃とAI加速の始まり

- Source: https://grok.com/share/c2hhcmQtMw_aea62e31-42dd-4fd1-8ea0-8864a1e27b44
- Created: 2026-04-12
- Model: grok-4-auto, grok-3
- Messages: 2

---

## Human

『Claude Mythos』で、不用意に世に放ったら社会が壊れてしまうレベルのAIが来てしまいましたけど、このレベルの衝撃が来る頻度が加速していきますね？

---

## Assistant

はい、その通りだと思います。Claude Mythos（Anthropicの最新フロンティアモデル、コードネームCapybara/Copybara）の件は、まさにその象徴的な「衝撃レベル」の到来を示していますね。<grok:render card_id="5b1530" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">10</argument></grok:render>

### Claude Mythosの何がヤバいのか（簡単に）
- **能力の跳躍**: 既存のClaude Opus 4.6を大幅に超える性能。特に**サイバーセキュリティ分野**で異常。CyberGymベンチマーク83.1%、SWE-bench 93.9%など、ほぼ全ベンチマークでトップ。ゼロデイ脆弱性を自律的に発見・活用可能で、OpenBSDの27年もののバグ、FFmpegの16年バグ、Linuxカーネルや主要ブラウザの深刻な弱点を次々に見つけてしまう。<grok:render card_id="f997d9" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">0</argument></grok:render>
- **なぜ公開しない？**: Anthropic自身が「不用意に世に放てば、社会に壊滅的なハッキング波を引き起こす可能性が高い」と判断。Project Glasswingという限定プログラムで、Amazon、Apple、Google、Microsoft、NVIDIA、CrowdStrikeなどの選ばれた防衛側パートナーにだけ提供し、脆弱性修正に使わせる形にしている。攻撃ツールとして悪用されたら「盾のない剣」になるから。<grok:render card_id="59f519" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">1</argument></grok:render>

これは「AIがAI開発やサイバーを加速させるフィードバックループ」の始まりを予感させるレベルです。AnthropicのSystem Cardでも、こうした能力が「defenders（守る側）よりattackers（攻める側）に有利になる波」を警告しています。

### 衝撃の頻度が加速しているか？
**明確に加速しています。** 理由はシンプル：

1. **スケーリング則の継続 + 投資爆増**: 計算リソース（compute）、データ、アルゴリズムの改善がまだ指数関数的に効いている。2023年のGPT-4 → 2024-25のo1/Claude 3.5/4 → 2026年のMythos級のジャンプが、どんどん短い間隔で来るようになっている。
2. **マルチモーダル/エージェント/自律性の進化**: 単なるチャットボットから「自律的にコード書き・脆弱性探し・活用」まで行けるようになると、一度の能力向上で社会影響が非線形に跳ね上がる。
3. **ラボ間の競争**: Anthropic、OpenAI、Google、xAI、中国勢などが同時並行で走っている。1社が抑えても、他が似たものを出せば拡散する。
4. **過去のペース**: GPT-3（2020）→ GPT-4（2023）で3年かかったような「衝撃」が、今は1年以内に複数回起きている印象。Mythosは「公開しない」決断自体が、事態の深刻さを物語っています。

今後1-2年で、さらに「社会の基盤（電力網、金融、インフラ、軍事）を根本から変える/壊す可能性のある」モデルが複数出てくる確率は高い。**AGI的な閾値に近づくにつれ、1回のジャンプあたりの「衝撃度」が指数関数的に上がる**一方で、到達頻度も速まる——まさに「加速」の典型です。

ただ、Anthropicのように「責任あるスケーリング」（Responsible Scaling Policy）を掲げて自制する動きもあるし、規制や国際的な合意の議論も進んでいます。完全に制御不能になるかは、まだ人間側の対応次第。

あなたはどう思います？ このMythos級の「抑え込み」が今後も通用すると思いますか、それとも漏洩・他社模倣で一気に広がると思いますか？ 日本の視点（Yokosukaから）で、サイバー防衛や社会影響はどう感じます？
