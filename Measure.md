# Measure

- Source: https://claude.ai/share/20418e67-6bef-446c-89d7-4e714863bb91
- Author: Taku
- Created: 2025-12-11
- Messages: 12

---

## Human

１つ前のチャット(Define)の内容も加味しながら、現在のサイトで取得しているイベント一覧に加え、新たに取得するべきイベントやカスタムディメンションを一緒に相談しながら決めていきましょう。

まずは既存で取得しているイベントを確認し、わからないものがあれば私に確認してください。

---

## Assistant

前回のDefineフェーズの内容を確認しつつ、現在GA4で取得しているイベント一覧を確認していきましょう。

まず、前回のチャット内容と現在のイベント取得状況を確認します。
```
This block is not supported on your current device yet.
```

前回のDefineフェーズの内容を確認できました。現在のゴール・KPI設計が明確になっています。

次に、現在GA4で取得されているイベント一覧を確認しましょう。
```
This block is not supported on your current device yet.
```

イベント一覧を確認できました。次にカスタムディメンションの設定状況も確認します。
```
This block is not supported on your current device yet.
```

BigQueryのテーブルスキーマを確認して、カスタムパラメータの設定状況を見てみましょう。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

BigQueryからイベントパラメータの詳細を確認します。
```
This block is not supported on your current device yet.
```

データが取得できました。現在のイベント設計を整理させてください。

---

## 現在取得されているイベント一覧（2025年11月）

### 📊 GA4標準イベント

| イベント名 | 11月発生数 | 用途 |
|:--|--:|:--|
| `page_view` | 27,636 | ページ閲覧 |
| `session_start` | 25,340 | セッション開始 |
| `first_visit` | 21,924 | 初回訪問 |
| `scroll` | 20,096 | 90%スクロール（GA4拡張計測） |
| `user_engagement` | 4,690 | エンゲージメント |
| `click` | 322 | 外部リンククリック（GA4拡張計測） |
| `view_search_results` | 230 | サイト内検索（GA4拡張計測） |
| `form_start` | 184 | フォーム入力開始（GA4拡張計測） |
| `form_submit` | 189 | フォーム送信（GA4拡張計測）**← ゴール** |

---

### 🎯 カスタムイベント

| イベント名 | 11月発生数 | 用途 | 主なパラメータ |
|:--|--:|:--|:--|
| `custom_scroll` | 127,862 | 細かいスクロール計測 | `percent_custom_scroll` |
| `article_finished_reading` | 15,318 | 記事読了 **← KPI** | `page_title`, `Directory1/2/3` |
| `お問い合わせ完了ページ` | 2,747 | フォームページ閲覧 **← KPI** | `Directory1/2/3` |
| `Detail` | 1,717 | 詳細閲覧？ | GA標準パラメータのみ |
| `article_same_category_click` | 889 | 同カテゴリ記事クリック | `Click_URL`, `Click_Text` |
| `header_menu_click` | 526 | ヘッダーメニュークリック | `Click_URL`, `Click_Text` |
| `運営情報_問合せ` | 65 | 運営情報ページ閲覧？ | `Directory1/2/3` |
| `top_recent_click` | 39 | トップページ新着クリック | — |
| `article_inpage_link_click` | 28 | ページ内リンククリック | `Click_Text` |
| `HA_link_click` | 9 | HAPPY ANALYTICSリンククリック | — |
| `参考になったか` | 3 | 記事評価クリック | — |
| `article_review_good` | 2 | 記事評価（良い） | — |
| `article_review_bad` | 1 | 記事評価（悪い） | — |
| `inquiry_complete` | 1 | 問い合わせ完了？ | — |
| `social_click` | 1 | SNSクリック | — |
| `ソーシャルボタンクリック` | 1 | SNSクリック | — |

---

### 📝 現在取得されているカスタムパラメータ（カスタムディメンション候補）

| パラメータ名 | 取得イベント | 用途推測 |
|:--|:--|:--|
| `Directory1` | 多数 | URL階層1（カテゴリ？） |
| `Directory2` | 多数 | URL階層2 |
| `Directory3` | 多数 | URL階層3 |
| `percent_custom_scroll` | custom_scroll | スクロール率（10%刻み？） |
| `Click_URL` | same_category, header_menu | クリック先URL |
| `Click_Text` | same_category, header_menu, inpage | クリックテキスト |
| `search_term` | view_search_results | サイト内検索語 |

---

## ❓ 確認事項

いくつか不明点がありますので、教えてください：

### 1. `Detail` イベント（月1,717回）
- これは何を計測していますか？
- GA標準パラメータしか付いていないのですが、意図したイベントでしょうか？

### 2. イベント名の重複
以下のイベントは同じ目的のように見えますが、違いはありますか？
- `social_click` と `ソーシャルボタンクリック`
- `inquiry_complete` と `form_submit`
- `運営情報_問合せ` と `お問い合わせ完了ページ`

### 3. `custom_scroll` の `percent_custom_scroll` の値
- 10%、25%、50%、75%、90%など、どのような閾値で発火していますか？

### 4. `Directory1/2/3` の定義
- 例えば `/ga4-guide/admin/` の場合：
  - Directory1 = `ga4-guide`？
  - Directory2 = `admin`？

---

これらを確認した上で、**新たに取得すべきイベント・パラメータ**を一緒に検討できればと思います。

---

## Human

1.現在使っていないので無視してください
2.`social_click` と `ソーシャルボタンクリック` は同じはずです。前者を利用してください
　`inquiry_complete` と `form_submit` は同じはずです。前者を利用してください
　`運営情報_問合せ` は/admin-info/含むページを見た場合に計測と `お問い合わせ完了ページ`は/what-is-ga4/を見た場合に計測。問い合わせのKPIとしては前者を利用してください。

1. 0%,20%,40%,60%,80%,100% で計測しています。
2. 書いてもらったケースの場合　Directory1= www.ga4.guide/ga4-guide/ Directory2=www.ga4.guide/ga4-guide/admin

となります。
上記情報に関して今後も使うため本プロジェクトの「手順」に追加をしてください。

---

## Assistant

ありがとうございます！情報が明確になりました。

1点だけ確認させてください：

> `inquiry_complete` と `form_submit` は同じはずです。前者を利用してください

`inquiry_complete` は月1回しか発生していないのですが、`form_submit`（月189回）ではなく `inquiry_complete` を使う形で合っていますか？前回のDefineフェーズでは `form_submit` をゴールとして設定しましたが、変更でしょうか？

---

それでは、プロジェクトの「手順」に追加する形式で情報をまとめます。以下の内容をプロジェクト設定の「手順」にコピー＆ペーストしてください：

---

## 追加する手順テキスト

```
### イベント定義と利用ルール

#### 利用するイベント一覧
| イベント名 | 用途 | 備考 |
|:--|:--|:--|
| `form_submit` | ゴール（問い合わせ完了） | GA4拡張計測 |
| `article_finished_reading` | KPI（記事読了） | カスタムイベント |
| `運営情報_問合せ` | KPI（フォームページ到達） | /admin-info/を含むページ閲覧時に発火 |
| `custom_scroll` | スクロール深度計測 | 0%,20%,40%,60%,80%,100%で発火 |
| `article_same_category_click` | 同カテゴリ記事クリック | |
| `header_menu_click` | ヘッダーメニュークリック | |
| `view_search_results` | サイト内検索 | GA4拡張計測 |
| `social_click` | SNSボタンクリック | |
| `HA_link_click` | HAPPY ANALYTICSリンククリック | |
| `article_review_good` / `article_review_bad` | 記事評価 | |

#### 無視するイベント（使用しない）
- `Detail` - 現在使っていない
- `ソーシャルボタンクリック` - `social_click` と重複
- `inquiry_complete` - `form_submit` と重複
- `お問い合わせ完了ページ` - /what-is-ga4/閲覧時に発火（問い合わせKPIには使わない）

#### カスタムパラメータ定義
| パラメータ名 | 説明 | 例 |
|:--|:--|:--|
| `Directory1` | URL階層1（ドメイン含む） | www.ga4.guide/ga4-guide/ |
| `Directory2` | URL階層2（ドメイン含む） | www.ga4.guide/ga4-guide/admin |
| `Directory3` | URL階層3（ドメイン含む） | |
| `percent_custom_scroll` | スクロール率 | 0, 20, 40, 60, 80, 100 |
| `Click_URL` | クリック先URL | |
| `Click_Text` | クリックしたテキスト | |
| `search_term` | サイト内検索語 | |
```

---

上記をプロジェクトの手順に追加いただけましたら、次に**新たに取得すべきイベント・カスタムディメンション**の検討に進みましょう。

`inquiry_complete` vs `form_submit` の確認をお願いできますか？

---

## Human

>`form_submit`（月189回）ではなく `inquiry_complete` を使う形で合っていますか？前回のDefineフェーズでは `form_submit` をゴールとして設定しましたが、変更でしょうか？

こちらですがform_submitの利用でお願いいたします。

---

## Assistant

承知しました！`form_submit` をゴールとして使用しますね。

それでは、プロジェクトの「手順」に追加する最終版をお伝えします：

---

## プロジェクト手順に追加するテキスト

```
### イベント定義と利用ルール

#### 利用するイベント一覧
| イベント名 | 用途 | 備考 |
|:--|:--|:--|
| `form_submit` | ゴール（問い合わせ完了） | GA4拡張計測 |
| `article_finished_reading` | KPI（記事読了） | カスタムイベント |
| `運営情報_問合せ` | KPI（フォームページ到達） | /admin-info/を含むページ閲覧時に発火 |
| `custom_scroll` | スクロール深度計測 | 0%,20%,40%,60%,80%,100%で発火 |
| `article_same_category_click` | 同カテゴリ記事クリック | |
| `header_menu_click` | ヘッダーメニュークリック | |
| `view_search_results` | サイト内検索 | GA4拡張計測 |
| `social_click` | SNSボタンクリック | |
| `HA_link_click` | HAPPY ANALYTICSリンククリック | |
| `article_review_good` / `article_review_bad` | 記事評価 | |

#### 無視するイベント（使用しない）
- `Detail` - 現在使っていない
- `ソーシャルボタンクリック` - `social_click` と重複
- `inquiry_complete` - `form_submit` と重複
- `お問い合わせ完了ページ` - /what-is-ga4/閲覧時に発火（問い合わせKPIには使わない）

#### カスタムパラメータ定義
| パラメータ名 | 説明 | 例 |
|:--|:--|:--|
| `Directory1` | URL階層1（ドメイン含む） | www.ga4.guide/ga4-guide/ |
| `Directory2` | URL階層2（ドメイン含む） | www.ga4.guide/ga4-guide/admin/ |
| `Directory3` | URL階層3（ドメイン含む） | |
| `percent_custom_scroll` | スクロール率 | 0, 20, 40, 60, 80, 100 |
| `Click_URL` | クリック先URL | |
| `Click_Text` | クリックしたテキスト | |
| `search_term` | サイト内検索語 | |
```

---

上記をプロジェクトの手順に追加できましたら、お知らせください。

次に、**新たに取得すべきイベント・カスタムディメンション**の検討に進みます。現在の計測状況とKPI・ゴールを踏まえて、追加提案をさせていただきます。

---

## Human

はい、検討を進めてください。

---

## Assistant

それでは、新たに取得すべきイベント・カスタムディメンションを検討します。まずサイトの構造を確認させてください。
```
This block is not supported on your current device yet.
```

サイト構造を確認できました。記事ページの詳細も確認させてください。
```
This block is not supported on your current device yet.
```

記事ページの構造を確認できました。現在の計測状況とサイトのゴール・KPIを踏まえて、追加すべきイベント・カスタムディメンションを提案します。

---

## 新たに取得すべきイベント・カスタムディメンション提案

### 現状の課題と追加計測の目的

| 課題 | 追加計測の目的 |
|:--|:--|
| CVR改善のためのボトルネックが不明 | ファネル分析の強化 |
| どのコンテンツがCVに貢献しているか不明 | コンテンツ→CV貢献度の可視化 |
| 問い合わせフォームの離脱理由が不明 | フォーム離脱分析の強化 |
| コンテンツの質の評価軸が限定的 | エンゲージメント深度の計測 |

---

## 🟢 追加推奨イベント

### 優先度：高（CVR改善に直結）

| イベント名 | 用途 | パラメータ案 | 理由 |
|:--|:--|:--|:--|
| `cta_banner_click` | CTAバナークリック | `banner_position`（top/sidebar/bottom/inline）, `banner_type` | セミナー講座バナー等のクリックを計測し、どの位置のCTAが効果的か分析 |
| `inquiry_link_click` | 問い合わせ導線クリック | `link_position`, `link_text` | 記事内・サイドバー・フッターの問い合わせリンククリックを個別計測 |
| `form_field_focus` | フォームフィールドフォーカス | `field_name`, `field_order` | どの項目で離脱しているか特定 |
| `form_error` | フォームエラー発生 | `field_name`, `error_type` | バリデーションエラーの発生状況把握 |

### 優先度：中（コンテンツ評価強化）

| イベント名 | 用途 | パラメータ案 | 理由 |
|:--|:--|:--|:--|
| `toc_click` | 目次クリック | `click_heading`, `click_order` | 現在`article_inpage_link_click`があるが、目次専用で分離するとより明確に |
| `time_on_page_milestone` | 滞在時間マイルストーン | `milestone`（30s/60s/180s/300s） | 記事読了以外のエンゲージメント深度を計測 |
| `copy_text` | テキストコピー | `copy_type`（code/text） | コードブロックや本文のコピー＝実用的な価値の証明 |
| `external_link_click` | 外部リンククリック | `link_url`, `link_text`, `link_type`（reference/official） | 公式ヘルプや参考リンクへの送客状況把握 |

### 優先度：低（あれば便利）

| イベント名 | 用途 | パラメータ案 | 理由 |
|:--|:--|:--|:--|
| `sidebar_nav_click` | サイドバーナビクリック | `nav_category`, `nav_text` | 回遊パターンの詳細把握 |
| `breadcrumb_click` | パンくずクリック | `click_level`, `click_text` | ナビゲーション利用状況 |
| `image_zoom` | 画像拡大 | `image_alt`, `image_src` | ビジュアルコンテンツへの関心度 |

---

## 🟢 追加推奨カスタムディメンション

### 優先度：高（分析に必須）

| パラメータ名 | スコープ | 用途 | 理由 |
|:--|:--|:--|:--|
| `article_category` | イベント | 記事カテゴリ名 | Directory1より明確。「UAとGA4」「探索機能」など |
| `article_publish_date` | イベント | 記事公開日（YYYY-MM-DD） | 古い記事のリライト優先度判断、鮮度と読了率の相関分析 |
| `content_type` | イベント | コンテンツタイプ | 「記事」「カテゴリ一覧」「トップ」など |
| `cv_contribution_page` | ユーザー | CV貢献ページ | CVしたユーザーが読んだ記事を特定（セッションスコープで取得） |

### 優先度：中（詳細分析用）

| パラメータ名 | スコープ | 用途 | 理由 |
|:--|:--|:--|:--|
| `article_update_date` | イベント | 記事更新日 | 更新頻度と読了率の相関分析 |
| `article_word_count` | イベント | 記事文字数 | 文字数と読了率・滞在時間の相関分析 |
| `reading_progress` | イベント | 読了進捗 | custom_scrollと併用、ページ毎の離脱ポイント特定 |
| `session_page_depth` | セッション | セッション内閲覧ページ数 | 回遊深度とCVの相関分析 |

---

## 📊 追加計測による分析可能項目

追加計測を行うことで、以下の分析が可能になります：

| 分析項目 | 必要なイベント/ディメンション |
|:--|:--|
| **CVに貢献している記事TOP10** | `cv_contribution_page` + `form_submit` |
| **フォーム離脱箇所の特定** | `form_field_focus` + `form_submit` |
| **CTAバナーの最適配置検証** | `cta_banner_click`（banner_position別） |
| **古い記事のリライト優先度** | `article_publish_date` + `article_finished_reading` |
| **コンテンツ長と読了率の相関** | `article_word_count` + `article_finished_reading` |
| **エンゲージメント深度別CV率** | `time_on_page_milestone` + `form_submit` |

---

## ❓ ご相談事項

1. **優先度について**
   上記の「優先度：高」から実装を進めるのがよいと思いますが、実装リソースの観点からどの程度対応可能でしょうか？

2. **`cta_banner_click` について**
   サイト内にセミナー講座販売バナー以外にも、HAPPY ANALYTICSへの導線CTAはありますか？あれば `banner_type` で区別したいです。

3. **フォーム分析について**
   現在のお問い合わせフォームの項目数と、主なフィールドを教えていただけますか？`form_field_focus` の設計に活かしたいです。

4. **記事メタ情報について**
   `article_publish_date` や `article_word_count` をGTMで取得する場合、HTMLのどこかに埋め込まれていますか？それとも新規実装が必要ですか？

---

上記についてご意見・ご質問があればお聞かせください。優先順位を確定した上で、具体的な実装仕様を詰めていきましょう。

---

## Human

1.優先度高のみまずは進めたいです
2.他にはありません
3.名前・メール・メッセージの３項目となります。
4.article_published_dateに関しては <time datetime="2021-10-20T16:47:21+09:00">2021年10月20日</time> から取ってこれそうですがどうでしょうか？word_countは新規実装が必要です。

---

## Assistant

ありがとうございます！情報が揃いました。

`article_publish_date` はおっしゃる通り `<time datetime="...">` から取得可能です。GTMでDOM要素変数を使って `datetime` 属性を取得できます。

それでは、**優先度：高**の実装仕様を具体的にまとめます。

---

## 優先度：高 実装仕様書

### 1. 追加イベント一覧

| イベント名 | 発火タイミング | パラメータ |
|:--|:--|:--|
| `cta_banner_click` | セミナー講座バナークリック時 | `banner_position`, `banner_text` |
| `inquiry_link_click` | 問い合わせ導線クリック時 | `link_position`, `link_text` |
| `form_field_focus` | フォームフィールドにフォーカス時 | `field_name`, `field_order` |
| `form_error` | フォームバリデーションエラー時 | `field_name`, `error_type` |

### 2. 追加カスタムディメンション一覧

| パラメータ名 | スコープ | 取得方法 |
|:--|:--|:--|
| `article_category` | イベント | URL階層 or パンくずから取得 |
| `article_publish_date` | イベント | `<time datetime>` 属性から取得 |
| `content_type` | イベント | URLパターンで判定 |

---

## 📋 各イベント詳細仕様

### 1. `cta_banner_click`

**目的**: セミナー講座バナーのクリック効果測定

| 項目 | 内容 |
|:--|:--|
| **発火条件** | セミナー講座バナー（happyanalytics.co.jp/ga4_recording へのリンク）クリック時 |
| **パラメータ** | |
| `banner_position` | `sidebar` / `inline` / `bottom` など配置位置 |
| `banner_text` | バナー内テキスト or alt属性 |

**GTM実装案**:
```
トリガー: クリック - リンクのみ
条件: Click URL が "happyanalytics.co.jp/ga4_recording" を含む
```

---

### 2. `inquiry_link_click`

**目的**: 問い合わせページへの導線効果測定

| 項目 | 内容 |
|:--|:--|
| **発火条件** | `/admin-info/` へのリンククリック時（ただしナビゲーションメニュー以外） |
| **パラメータ** | |
| `link_position` | `article_body` / `sidebar` / `footer` / `breadcrumb` |
| `link_text` | リンクテキスト |

**補足**: `header_menu_click` と区別するため、ヘッダーナビからのクリックは除外

---

### 3. `form_field_focus`

**目的**: フォーム離脱箇所の特定

| 項目 | 内容 |
|:--|:--|
| **発火条件** | フォームフィールドにフォーカスした時（各フィールド最初の1回のみ） |
| **パラメータ** | |
| `field_name` | `name` / `email` / `message` |
| `field_order` | `1` / `2` / `3` |

**分析方法**:
```
フォーム到達者のうち：
- field_order=1（名前）到達率: 〇%
- field_order=2（メール）到達率: 〇%
- field_order=3（メッセージ）到達率: 〇%
- form_submit 完了率: 〇%

→ どのフィールドで離脱が多いか特定
```

---

### 4. `form_error`

**目的**: バリデーションエラーによる離脱防止

| 項目 | 内容 |
|:--|:--|
| **発火条件** | フォーム送信時にバリデーションエラーが発生した時 |
| **パラメータ** | |
| `field_name` | `name` / `email` / `message` |
| `error_type` | `required`（必須未入力） / `invalid_format`（形式エラー） |

**確認事項**: 現在のフォームでバリデーションエラー時にJavaScriptイベントやDOM変化はありますか？それによって実装方法が変わります。

---

## 📋 カスタムディメンション詳細仕様

### 1. `article_category`

| 項目 | 内容 |
|:--|:--|
| **取得方法** | URL第1階層から判定 |
| **値の例** | `UAとGA4` / `計測手順` / `探索機能` / `BigQuery` など |

**マッピング表**:

| URL階層 | article_category |
|:--|:--|
| `/what-is-ga4/` | UAとGA4 |
| `/measure-flow/` | 計測手順 |
| `/report-and-ads/` | レポートと広告 |
| `/explore/` | 探索機能 |
| `/setting-implementation/` | 計測の設定と実装 |
| `/related-service/` | BigQuery |
| `/admin/` | 管理画面 |
| `/glossary-help/` | 用語集・FAQ等 |
| `/admin-info/` | 運営情報・問合せ |
| `/home/` | お知らせ・ブログ |

---

### 2. `article_publish_date`

| 項目 | 内容 |
|:--|:--|
| **取得方法** | `<time datetime="...">` のdatetime属性 |
| **値の形式** | `YYYY-MM-DD`（例: `2022-03-28`） |

**GTM実装案**:
```javascript
// DOM要素変数
要素: time[datetime]
属性: datetime
→ 取得した値を YYYY-MM-DD 形式に変換
```

---

### 3. `content_type`

| 項目 | 内容 |
|:--|:--|
| **取得方法** | URLパターンで判定 |
| **値** | `top` / `category` / `article` / `form` |

**判定ロジック**:

| 条件 | content_type |
|:--|:--|
| URL = `/` | `top` |
| URL = `/admin-info/` | `form` |
| URLが `/xxx/` のみ（第1階層のみ） | `category` |
| URLが `/xxx/yyy/` 以上（第2階層以上） | `article` |

---

## 📊 追加計測による分析例

### CVR改善のためのファネル分析

```
セッション開始
    ↓
記事閲覧（article_finished_reading）
    ↓
CTA認知（cta_banner_click / inquiry_link_click）
    ↓
フォームページ到達（運営情報_問合せ）
    ↓
フォーム入力開始（form_field_focus field_order=1）
    ↓
フォーム入力継続（form_field_focus field_order=2, 3）
    ↓
フォーム送信（form_submit）
```

**分析で明らかになること**:
- CTAバナーと問い合わせリンク、どちらが効果的か
- フォームのどのフィールドで離脱しているか
- エラー発生率と離脱の相関

---

## ❓ 確認事項

実装を進める前に、以下を確認させてください：

1. **セミナー講座バナーの配置場所**
   現在サイドバーにあることは確認しましたが、記事内やフッターにも配置されていますか？

2. **フォームのバリデーション**
   エラー発生時にエラーメッセージがDOM上に表示されますか？それともalertなどで表示されますか？

3. **GTM実装について**
   GTMは導入済みでしょうか？また、カスタムHTMLタグの追加は可能ですか？

---

上記で問題なければ、GTMの具体的な設定手順書を作成いたします。

---

## Human

1.はい、あります。
2.技術的なことはわかりませんが、必須項目を入力せずに押した場合「入力してください。」という文字列がページ上に表示されます
3.導入済み＆カスタムHTMLタグの追加は出来ます。

---

## Assistant

ありがとうございます！実装に必要な情報が揃いました。

GTMの設定手順書を作成します。
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

GTM設定手順書を作成します。
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

GTM実装手順書を作成しました。

---

## 📋 手順書の内容サマリー

手順書には以下の内容が含まれています：

### 追加イベント（4種類）
| イベント名 | 用途 |
|:--|:--|
| `cta_banner_click` | セミナー講座バナークリック |
| `inquiry_link_click` | 問い合わせ導線クリック（ヘッダー以外） |
| `form_field_focus` | フォームフィールドフォーカス |
| `form_error` | フォームバリデーションエラー |

### カスタムディメンション（3種類）
| パラメータ名 | 用途 |
|:--|:--|
| `article_category` | 記事カテゴリ名 |
| `article_publish_date` | 記事公開日 |
| `content_type` | コンテンツタイプ |

---

## ⚠️ 実装前の確認事項

手順書内のカスタムHTMLコードで、フォームのフィールド識別子を仮で設定しています：

```javascript
var fieldConfig = {
  'your-name': { name: 'name', order: 1 },
  'your-email': { name: 'email', order: 2 },
  'your-message': { name: 'message', order: 3 }
};
```

**確認をお願いしたい点：**
問い合わせフォームの各フィールドの `name` 属性または `id` 属性を教えていただけますか？実際の値に合わせてコードを修正する必要があります。

確認方法：
1. https://www.ga4.guide/admin-info/ を開く
2. フォームの各入力欄を右クリック → 「検証」
3. `<input name="xxx">` または `<input id="xxx">` の値を確認

---

フィールド名を確認いただければ、手順書を更新いたします。
