# Claudeのフィンガープリント取得について

- Source: https://claude.ai/share/3c97cb9e-7aff-4d67-8edd-ad7105096288
- Author: YSR
- Created: 2026-07-18
- Messages: 2

---

## Human

これはある人がスクショした、https://s-cdn.anthropic.com/s.jsのコードのスクショなんだけど、要するにClaudeはユーザーのフィンガープリントを取得している？

---

## Assistant

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

実物を取得して確認しました。結論から言うと、**このスクリプトは本物で、ブラウザ・フィンガープリンティングを行う計測ビーコンです**。ただし「Claude(AI本体)が取得している」のではなく、「claude.ai等のWebサイトに、フィンガープリント収集型のトラッキングスクリプトが設置されている」というのが正確な表現です。以下、裏取りの結果です。

**1. ファイル実物の確認(取得時刻: 2026-07-18 06:53 UTC)**

`https://s-cdn.anthropic.com/s.js` を直接取得したところ、gzip圧縮で19,660バイト(展開後57,981バイト、Last-Modified: 2026-06-16)。スクショと同一のコードで、以下の22個の「シグナル」を収集する構造でした:

adBlockSignal / browserAttributesSignal / canvasSignal / incognitoSignal / mimetypesSignal / pluginsSignal / screenAttributesSignal / timezoneOffsetSignal / webdriverSignal / tamperedBrowserSignal / tamperedLanguageSignal / tamperedOSSignal / tamperedResolutionSignal / referrerSignal / urlAndHostnameSignal / titleAndCharsetSignal / userIdSignal / partnerUserIdSignal / sessionIdSignal / userUuidSignal / cacheStableSignal / prioritySignal

ソース内のライセンスコメントから、オープンソースの **fingerprintjs2 / FingerprintJS v3**(まさに「Cwm fjordbank glyphs vext quiz 😃」のcanvas描画を行う定番フィンガープリントライブラリ)、**detectIncognito**(シークレットモード検知)、**crypto-js** を同梱していることが確認できます。canvas描画結果は `toDataURL()` をハッシュ化して `cf` パラメータとして送信する実装です。

**2. 送信先は第三者トラッカードメイン**

送信部は `new Image(1,1)` による古典的な1x1 GIFビーコンで、`https://{trackerUrl}/images/{乱数}.gif?...` に全パラメータを付けて送ります。そして **デフォルトの trackerUrl は `hexagon-analytics.com`** とハードコードされています(`_setTrackerUrl` で上書き可能なため、実運用でどのURLに送っているかは【未確認】)。APIは `_setAccount`(beaconToken)、`_setUserId`、`_setPartnerUserId`、`_trackPageview` という広告計測タグ然とした構造です。

hexagon-analytics.com は既知のトラッカーとして **EasyPrivacy**(`||hexagon-analytics.com^$third-party`、4939行目)と **AdGuard SpywareFilter** の両方に掲載済みです(いずれも本日取得の現行リストで確認)。GhosteryのtrackerDBではこのドメインは crimsonhexagon.com と同一グループ(organization: Brandwatch、category: site_analytics)に分類されていますが、現在の運営実体がどこかの確定情報は見つけられませんでした【未確認】。なお、urlscan.ioで検索するとこのドメインへのビーコンは flickr.com や dairyqueen.com など1万件以上のスキャンで観測されており、Anthropic専用ではなく広く使われている第三者計測タグです。

**3. どこで読み込まれているか**

urlscan.ioの検索(取得時刻: 2026-07-18 06:55 UTC頃)では、s-cdn.anthropic.com を読み込むスキャンが3,150件あり、直近のものは claude.ai のログインページ・シェアページ、platform.claude.com でした。claude.ai から hexagon-analytics.com への実際のビーコン発火が記録されたスキャンは2023-10-09の1件を確認。直近のスキャンで実際にどこへビーコンが飛んでいるか(hexagon-analytics.com のままか、上書き先か)は今回確認できませんでした【未確認】。

**4. 解釈**

集めているシグナルの構成(webdriver検知=自動化ブラウザ検知、UA改ざん検知4種、adblock検知、シークレットモード検知)を見ると、これは純粋な「個人追跡」というより、**広告アトリビューション+ボット/不正アカウント検知**の典型的な組み合わせです。Anthropicは大規模なアカウント不正・モデル蒸留攻撃への対策を公言しており、疑わしいパターンを特定するための分類器や行動フィンガープリンティングシステムを構築したと説明しています。ただし、このs.jsの具体的な用途(広告計測なのか不正検知なのか、両方なのか)はコードからは断定できません【未確認】。

技術的に言えることは明確で、①canvasフィンガープリントを含むデバイス識別情報を収集し、②第三者トラッカードメイン宛のビーコンとして送る設計であり、③スクリプト本体を自社CDN(s-cdn.anthropic.com)から配信することでスクリプト自体のサードパーティブロックを回避する、いわゆるファーストパーティ化の構成になっている、という点です。一方でビーコン送信先の hexagon-analytics.com はEasyPrivacy掲載済みなので、uBlock Origin等を使っていれば送信自体はブロックされます。

つまり「要するにフィンガープリントを取得しているか?」への答えは**Yes(ただし主体はclaude.ai等のWebプロパティで、用途は広告計測/不正検知系とみられるが未確定)**です。
