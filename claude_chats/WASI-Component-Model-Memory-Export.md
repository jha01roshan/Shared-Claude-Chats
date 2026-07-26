# WASI Component Model Memory Export

- Source: https://claude.ai/share/d5b1eabc-8a25-4026-a4d0-a29ad81231b6
- Author: iwate
- Created: 2025-10-06
- Messages: 8

---

## Human

wasm component を学習しています。
何もせずただ終了する次のプログラムを書きました。

```
;; A minimal component that can be run with `wasmtime run minimum.wat`
(component
    (core module $mymodule
        (func (export "main") (result i32)
            (i32.const 0)
        )
    )
    (core instance $myinstance (instantiate $mymodule))
    (func $main (result (result)) (canon lift (core func $myinstance "main")))

    (component $Comp
        (import "main" (func $g (result (result))))
        (export "run" (func $g))
    )

    (instance $c (instantiate $Comp
        (with "main" (func $main)))
    )

    (export "wasi:cli/run@0.2.0" (instance $c))
)
```

wasi preview1のときはmemoryをエクスポートすることが必須でしたが上記のコードは得にエラーができました。component modelを使用したpreview2では必要なくなったのでしょうか？

---

## Assistant

はい、その通りです。WASI Preview 2（Component Model）では、メモリの明示的なエクスポートは必須ではなくなりました。

## WASI Preview 1 vs Preview 2 の違い

**WASI Preview 1:**
- WebAssembly Core Module を直接使用
- `memory` のエクスポートが必須
- WASI 関数は直接メモリにアクセス
- 線形メモリを介したデータのやり取り

**WASI Preview 2 (Component Model):**
- WebAssembly Component を使用
- メモリは Component の内部実装詳細
- データは Component Interface を通じて型安全にやり取り
- メモリの直接エクスポートは不要

## あなたのコードについて

あなたの例では：

```wat
(core module $mymodule
    (func (export "main") (result i32)
        (i32.const 0)
    )
)
```

この Core Module 内で `memory` を宣言・エクスポートしていませんが、`main` 関数が単純に定数を返すだけなので問題ありません。

もし Core Module 内でメモリを使用する必要がある場合は、従来通り宣言できます：

```wat
(core module $mymodule
    (memory (export "memory") 1)  ; 必要に応じて
    (func (export "main") (result i32)
        ;; メモリを使った処理
        (i32.const 0)
    )
)
```

## Component Model の利点

1. **型安全性**: Interface Types により型安全なデータ交換
2. **カプセル化**: メモリは実装詳細として隠蔽
3. **相互運用性**: 言語間でのより自然なデータ交換
4. **セキュリティ**: メモリへの直接アクセスを制限

つまり、Preview 2 では Component の境界を越えてメモリを直接共有するのではなく、型定義されたインターフェースを通じてデータをやり取りするため、メモリのエクスポートが必須ではなくなったということです。

---

## Human

$mymodule "main"をliftした$mainを"wasi:cli/run@0.2.0"としてエクスポートするために$compを作っていますが冗長な気がします。もっと短くかけますか？"main"という関数名をかえることも許可するので最小のコードにしてください。

---

## Assistant

はい、確かに冗長です。中間のコンポーネント `$Comp` を省略して、直接エクスポートできます。
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

これが最小形です。変更点：

1. **中間コンポーネント `$Comp` を削除**
2. **中間インスタンス `$c` を削除**
3. **関数名を "main" から "run" に変更**
4. **変数名を短縮** (`$mymodule` → `$m`, `$myinstance` → `$i`)
5. **直接エクスポート**: `canon lift` を直接 `wasi:cli/run@0.2.0` のエクスポートで使用

元のコードでは：
```
core module → core instance → canon lift → 中間コンポーネント → インスタンス → エクスポート
```

新しいコードでは：
```
core module → core instance → canon lift → 直接エクスポート
```

これで `wasmtime run` で実行可能な最小のWASI Component になります。

---

## Human

Error: failed to run main module `minimum.wasm`

Caused by:
    instance export `wasi:cli/run@0.2.0` does not have export `run`

---

## Assistant

エラーの原因は、WASI CLI インターface の要求する形式と一致していないことです。`wasi:cli/run@0.2.0` は `run` という名前の関数をエクスポートするインスタンスを期待しています。
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

修正点：

1. **インスタンスとしてエクスポート**: `wasi:cli/run@0.2.0` は関数ではなく、`run` 関数を持つインスタンスをエクスポートする必要があります
2. **インライン インスタンス作成**: `(instance (export "run" (func $run)))` でその場でインスタンスを作成
3. **core関数名を短縮**: "f" に変更してさらに簡潔に

これで `wasmtime run` が期待する形式：
- `wasi:cli/run@0.2.0` という名前のインスタンス
- そのインスタンスが `run` という名前の関数をエクスポート

という要求を満たします。

---

## Human

```
Error: unexpected token, expected an index or an identifier
     --> minimum.wat:11:44
      |
   11 |     (export "wasi:cli/run@0.2.0" (instance (export "run" (func $run))))
      |                                            ^
```

---

## Assistant

インライン インスタンス構文が正しくありませんでした。正しい構文に修正します：
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

修正点：

1. **コンポーネント定義**: `run` 関数をインポートしてエクスポートするコンポーネント `$c` を定義
2. **インスタンス化**: そのコンポーネントを実際の `$run` 関数でインスタンス化
3. **エクスポート**: 作成されたインスタンスを `wasi:cli/run@0.2.0` としてエクスポート

WAT構文では、インライン インスタンス作成はサポートされていないため、明示的にコンポーネントを定義してからインスタンス化する必要があります。
