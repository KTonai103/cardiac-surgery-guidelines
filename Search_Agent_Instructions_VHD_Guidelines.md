# AIエージェント指示文：弁膜症ガイドライン最新版 網羅的検索

**目的：** 大動脈弁狭窄症（AS）を含む弁膜症治療ガイドラインの最新版を、主要な国際・各国学会のウェブサイトから網羅的に収集する。

---

## タスク概要

以下の手順で、各地域・各学会の弁膜症（Valvular Heart Disease）に関するガイドライン・ステートメントの最新版を検索し、PDF公開URLおよびバージョン情報を報告してください。

現在リポジトリに収載されているバージョン（比較対象）：
- 🇯🇵 JCS 2020 弁膜症治療ガイドライン
- 🇪🇺 ESC/EACTS 2025 Valvular Heart Disease Guidelines
- 🇺🇸 ACC/AHA 2020 Valvular Heart Disease Guidelines

---

## Step 1：日本（JCS）の検索

### 検索先URL（優先順）
1. 日本循環器学会 ガイドラインページ：`https://www.j-circ.or.jp/guideline/`
2. J-STAGE（国内学術論文）：`https://www.jstage.jst.go.jp/`

### 検索クエリ
- `site:j-circ.or.jp 弁膜症 ガイドライン 2024`
- `site:j-circ.or.jp 弁膜症 ガイドライン 2025`
- `JCS 弁膜症治療ガイドライン 2024 OR 2025 PDF`
- `"弁膜症治療ガイドライン" 改訂 2024 OR 2025`

### 確認事項
- [ ] 2020年版以降に新たな「弁膜症治療ガイドライン」が発行されているか
- [ ] 2021年以降に「Focused Update」または「追補」が発行されているか
- [ ] 大動脈弁狭窄症・TAVI に特化した独立したステートメントが存在するか
- [ ] JCS/CVIT 合同ガイドライン（TAVI関連）の最新版

---

## Step 2：米国（ACC/AHA）の検索

### 検索先URL（優先順）
1. ACC ガイドラインページ：`https://www.acc.org/guidelines`
2. AHA ガイドラインページ：`https://professional.heart.org/en/guidelines-and-statements`
3. JACC 公式ジャーナル：`https://www.jacc.org/`

### 検索クエリ
- `site:acc.org valvular heart disease guideline 2021 OR 2022 OR 2023 OR 2024 OR 2025`
- `site:jacc.org "valvular heart disease" guideline focused update`
- `ACC AHA valvular heart disease guideline 2021 focused update PDF`
- `ACC AHA aortic stenosis TAVR guideline 2022 OR 2023 OR 2024`
- `"AHA/ACC" "valvular heart disease" "focused update" site:ahajournals.org`

### 確認事項
- [ ] 2020年版以降に「Focused Update」が発行されているか（特に2021年）
- [ ] TAVR/TAVI の適応に関する独立したコンセンサス文書の有無
- [ ] STS（Society of Thoracic Surgeons）による関連ガイドライン・ステートメントの有無
- [ ] AATS（American Association for Thoracic Surgery）による関連ガイドライン

### STS 追加検索
- `site:sts.org valvular heart disease guideline 2022 OR 2023 OR 2024 OR 2025`
- `STS aortic stenosis TAVR expert consensus 2023 OR 2024`

---

## Step 3：欧州（ESC/EACTS）の検索

### 検索先URL（優先順）
1. ESC ガイドラインページ：`https://www.escardio.org/Guidelines`
2. EACTS ガイドラインページ：`https://www.eacts.org/resources/guidelines/`
3. European Heart Journal：`https://academic.oup.com/eurheartj`

### 検索クエリ
- `site:escardio.org valvular heart disease guidelines 2025`
- `ESC EACTS 2025 valvular heart disease guidelines PDF download`
- `"2025 ESC Guidelines" "valvular heart disease"`

### 確認事項
- [ ] 2025年版が最新であることの確認（発表日・公式発行日）
- [ ] ESC 2025版からの主要変更点サマリーの有無
- [ ] EACTS 独自のコンセンサス文書（TAVI・SAVR関連）の追加分

---

## Step 4：その他の関連ガイドライン・コンセンサス文書の検索

### 対象学会・文書
| 学会 | 検索クエリ |
|-----|-----------|
| **TVT Registry / STS/ACC** | `STS ACC TVT registry TAVR outcomes 2024` |
| **VARC（弁置換術研究コンソーシアム）** | `VARC-3 valve academic research consortium 2021 criteria` |
| **EORP-VHD（欧州レジストリ）** | `EORP valvular heart disease registry 2024 update` |
| **PCR（EuroPCR）** | `PCR consensus TAVI low risk 2023 OR 2024` |
| **アジア太平洋地域** | `APSC Asia Pacific aortic stenosis TAVI guideline 2023 OR 2024` |

---

## Step 5：重要RCT・エビデンスの最新情報検索

AS/TAVR領域の近年の主要トライアルについても確認してください。

### 検索クエリ
- `AVATAR trial aortic stenosis asymptomatic 2024`
- `RECOVERY trial aortic stenosis surgery 2024`
- `EVOLVED trial asymptomatic aortic stenosis 2024`
- `NOTION-2 trial TAVI young patients 2024`
- `PARTNER 3 5-year outcomes TAVI low risk 2024`
- `Evolut Low Risk trial 5-year outcomes 2024`
- `RHEIA trial TAVI women 2024`

---

## 報告フォーマット

検索結果は以下の形式で報告してください。

```markdown
### [学会名] [年] [文書名]

- **発行年月：** YYYY年MM月
- **発行学会：** ○○学会
- **文書種別：** Full Guideline / Focused Update / Expert Consensus / Scientific Statement
- **公開URL：** https://...
- **PDF直接リンク：** https://... （存在すれば）
- **リポジトリ収載版との差分：** 新規 / 更新あり（YYYY版から改訂） / 変更なし
- **主要変更点：**（更新があれば概要を3点以内で箇条書き）
```

---

## 注意事項

1. **学会公式サイトを優先する**：二次サイト（医療情報まとめサイト等）ではなく、必ず学会または学術誌の公式ページからの情報を確認すること。
2. **PDF直接リンクが無料公開かどうか確認する**：有料（会員限定）の場合はその旨を記載する。
3. **発行日と改訂日を区別する**：Web掲載日ではなく、ガイドラインの公式発行日（Publication date）を確認する。
4. **日本語ガイドラインは和文・英文の両方を確認する**：JCSは同一ガイドラインの英文・和文両版がある場合がある。
5. **2020年1月以降に発行されたもののみを対象とする**：それ以前のものは既に収載済みとして除外する。
