# Control

- Source: https://claude.ai/share/2a78cd7b-4bd0-48b4-b160-1652ba98334a
- Author: Taku
- Created: 2025-12-12
- Messages: 3

---

## Human

ファイルにある「Genspark_月次レポート」と同じフォーマットで2025年11月のレポートを作成したいです。ただしゴールやKPIに関しては本プロジェクトや手順・メモリーに入っている内容を優先してください。
アウトプットはmdファイル形式でこのタイミングでは大丈夫です。
以下が月次レポートを作成するために利用したプロンプトです。
こちらも参考にレポート作成をお願いいたします。
# GA4月次レポート作成プロンプト
## 基本設定
- **期間**: 前月 vs 前々月・前年同月
- **目的**: サイト診断&CV改善提案
- **形式**: PowerPoint想定Markdown
## 事前確認
1. ECサイトでpurchase等取得の有無 → 回答後に次へ
2. 複数キーイベント時の使用対象(「all」or特定名) → 回答後に分析開始
## 出力構成
### 1. エグゼクティブサマリー(300-500文字)
主要数値変化(AU/セッション/CV数/CVR)、伸長/減少チャネル・ページ・CV種類、重要点3つ
### 2. 改善施策TOP5
**表**: 番号|施策名|対象|実施内容|評価指標|期待効果|難易度(3段階)  
全施策実施時のセッション&CV数見込(悲観/平均/楽観)
### 3. サイト評価(10項目×10点)
**ヒートマップ表**(前月/前々月/前年同月): AU/セッション/CV数/CVR/検索流入/エンゲージメント率/平均PV/平均訪問回数/平均滞在時間/売上  
気づき300文字
### 4. 時系列流入推移
- 主要指標13か月推移(表)
- TOP5チャネル別セッション&CV数13か月(表)
- チャネル×LP TOP10セッション数13か月(表)
- デバイス別(前月vs前年同月)
- 都道府県別(前月vs前年同月)
- インサイト・課題・改善案
### 5. ページ閲覧
- LP TOP10(タイトル/セッション/エンゲージ率/前月比)
- 検索流入LP TOP10(表)
- PV TOP10(表)
- SEO改善TOP5(具体的title案/description案/コンテンツ追加案)
- インサイト・課題・改善案
### 6. イベント発生
- TOP20(表: 名/回数/UU/回数÷UU)  
※page_view超イベントは除外
- インサイト・課題・改善案
### 7. eコマース(purchase取得時)
- 購入回数・金額年間推移
- 1人当たり購入回数・単価
- TOP20商品(表)
- 成長TOP10(前々月比)
- インサイト・課題・改善案
### 8. 成功・失敗要因
良3点/悪3点
### 9. 来月施策
注目指標、重点3施策
## ルール
- 表タイトルに集計期間必須
- ページタイトルはtitleタグ文字列使用(URLや種別名不可)
- 定量的根拠ある提案
- 期待効果数値明記

---

## Assistant

2025年11月のGA4月次レポートを作成します。まずは必要なデータを収集していきます。

## データ収集開始

以下の期間のデータを取得します：
- **前月（分析対象）**: 2025年11月1日〜11月30日
- **前々月（比較）**: 2025年10月1日〜10月31日
- **前年同月（比較）**: 2024年11月1日〜11月30日
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

次に、コンバージョン（form_submit）とイベントデータを取得します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

次に、チャネル別データを取得します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

ランディングページ別のデータを取得します。
```
This block is not supported on your current device yet.
```

13ヶ月分の時系列データを取得します。
```
This block is not supported on your current device yet.
```

デバイス別データを取得します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

次にSearch Consoleからオーガニック検索の詳細データを取得します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

PVが多いページのデータを取得します。
```
This block is not supported on your current device yet.
```

---

## Assistant

トランスクリプトファイルを確認し、収集済みデータを基にレポートを作成します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

収集済みデータを確認しました。追加で必要なデータを取得しながらレポートを作成します。まず、CVR計算のため form_submit データを確認します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

データが揃いました。参考レポートのフォーマットに従って月次レポートを作成します。
```
This block is not supported on your current device yet.
```
