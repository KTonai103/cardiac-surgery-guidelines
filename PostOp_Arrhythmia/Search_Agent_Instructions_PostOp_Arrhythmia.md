# 心臓外科 術後不整脈 — 追加文献ダウンロード指示書（Agentコピペ用）

**目的：** 成人心臓外科**術後不整脈**（術後心房細動 POAF を最重点に、心房粗動・SVT・心室性不整脈 VT/VF・徐脈／房室ブロック／ペーシング適応・洞機能不全）の統合ドキュメントを作成するための追加文献を、本リポジトリに**まだ無いもの**だけ網羅的に収集する。
特に「日本で採用されている抗不整脈薬の **一般名・商品名・希釈方法・投与方法**」まで記載するために、ガイドラインには載らない **PMDA 電子添文（添付文書）／インタビューフォーム** を一次資料として確保する。

調査日：2026-06-10 ／ 既存リポジトリの自動サーベイ（PDF全文 grep）＋ PubMed/PMDA 書誌の敵対的検証済み。

---

## 0. このドキュメントの使い方（Agentへの依頼文）

> 以下の **Part 2〜3** に列挙した文献・添付文書を、各エントリの DOI/PMID/URL/YJコードを使って収集してほしい。
> - 学会・学術誌の**公式ページ**を優先（まとめサイト不可）。`🆓` は無料/PMC、`💰` は有料、`📄` は学会PDF、`PMDA` は電子添文。
> - **Part 1 の命名規則・保存先**に従って `reference/` 配下へ保存し、最後に「報告フォーマット」で結果一覧（取得可否・実URL・版）を返す。
> - **Part 0 の「既収載リスト」に挙げたものは再ダウンロード不要**（重複回避）。
> - PMDA 添付文書は版サフィックス（`_1_xx`）が改訂で変わるため、**YJコードまたは商品名で `https://www.pmda.go.jp/PmdaSearch/iyakuSearch/` を検索し、最新の電子添文PDFを取得**すること（直リンクは404になり得る）。
> - **販売中止・適応外**のフラグが付いた薬剤は、その旨と現行代替品も併せて確認・記録すること。

---

## Part 0. 既存リポジトリ調査結果（=再DL不要／カバー範囲／ギャップ）

### 0-1. 既に収載済みで術後不整脈に使える資料（★は中核）

| 資料（repo内パス） | 術後不整脈での主な内容 | 薬剤の用量/希釈 |
|---|---|---|
| ★ `reference/US/STS_2026_Postoperative_Atrial_Fibrillation_Guidelines.pdf` | **POAF専用GL**。15推奨（予防8/術中3/治療4）。発生率20–50%、危険因子、レート vs リズム、抗凝固。 | クラス/レベルのみ。希釈・投与法は**無し**（用量は引用試験/他GL転載のみ） |
| `reference/Europe/Arrhythmia/ESC_EACTS_2024_Atrial_Fibrillation_Guidelines.pdf` | §9.6 術後AF。発生率30–50%。**ランジオロール**用量を唯一明記（欧州）。 | 一般急性AFレートコントロール表（ボーラス+持続）。希釈はアミオダロン1件のみ |
| `reference/US/Arrhythmia/ACC_AHA_HRS_2023_Atrial_Fibrillation_Guidelines.pdf` | §10.9 心臓外科後AF（予防/治療）、§10.10 急性疾患AF。抗凝固60日。 | 急性レートコントロール用量表（希釈なし）。ランジオロール記載**無し** |
| ★ `reference/Japan/Arrhythmia/JCS_JHRS_2020_Arrhythmia_Pharmacotherapy_Guidelines_EN.pdf` | **日本の薬物療法の本体**。表74/表48に**IV抗不整脈薬の用量＋希釈**（ランジオロール術後レジメン、ニフェカラント、ジルチアゼム、ベラパミル、ピルシカイニド、リドカイン、プロカインアミド、Mg、ATP等）。 | **detailed（希釈あり）**。ただしアミオダロンIV/ジゴキシンIVは「添付文書に従う」と委譲 |
| `reference/Japan/Arrhythmia/JCS_JHRS_2024_不整脈治療_Guidelines.pdf`（+EN） | フォーカスアップデート（デバイス/アブレーション/抗凝固）。**術後不整脈の記載はほぼ無し**。 | IV抗不整脈薬の用量表**無し** |
| `reference/Japan/Arrhythmia/JCS_JHRS_2021_不整脈非薬物治療_Guidelines.pdf` | リードレスPM/CSP/リード抜去/デバイス検出AF。**術後AVブロックのPPM適応は含まれない**（親GL=2018側）。 | 抗凝固DOAC用量のみ |
| `reference/Europe/ESC_2022_Ventricular_Arrhythmias_SCD_Guidelines.pdf` | **electrical storm**、VT/VF、TdP。術後は付随的。 | VA用IV用量表（希釈なし） |
| ★ `reference/US/STS_2017_Resuscitation_After_Cardiac_Surgery_CSU_ALS_Expert_Consensus.pdf` | **術後心停止アルゴリズム**（3連続shock→5分以内再開胸、エピネフリン制限、一時心外膜ペーシングDDD 80–100bpm）。 | アミオダロン300→150→900mg/24h等（クラス/レベル付） |
| `reference/Europe/EACTS_2009_Cardiac_Arrest_After_Cardiac_Surgery_CALS_Guidelines.pdf` | 上記の欧州版（同一プロトコル）。 | 同用量だが**COR/LOEラベル無し**（コンセンサス） |
| `reference/US/AHA_2025_Part9_Adult_Advanced_Life_Support_Guidelines.pdf` | 一般ALS（術後心停止はPart10へ委譲）＋**Table 2 IVレートコントロール用量**。 | ボーラス+持続（希釈なし） |
| `reference/US/ERAS_Cardiac_2019_...pdf` / `reference/US/Perioperative_Management/ERAS_STS_2023_...pdf` / `reference/Europe/Perioperative_Management/EACTS_2024_Perioperative_Medication_Guidelines.pdf` | **POAF予防**（β遮断継続・アミオダロン・Mg・後心膜切開）。EACTSが唯一COR/LOE付。 | 経口維持量(mg/日)のみ。IV希釈・投与法は**無し** |
| ★ `CVCU_Emergency_Response/CVCU_Emergency_Response_Protocol.md`（既著） | **既に**§4–§8で薬剤投与プロトコル（希釈・経路）＋§7 POAF（疫学＋IVアミオダロン希釈表）を保有。8GLを統合・fact-check済。 | **detailed（希釈あり）**。ただし希釈量は一部ACLS/添付文書/慣用量ベース |
| `AF_Surgery/AF_Surgery_Indications_Guideline_Comparison.md`（既著） | 外科的AF治療（Maze/PVI/LAA）。POAFは予防1表＋分類概念のみ。 | 薬剤投与なし |

### 0-2. 中核的発見（統合ドキュメント設計の前提）

1. **ガイドラインは「希釈方法・投与方法」を載せない。** STS2026・ESC/EACTS2024・ACC/AHA2023・ERAS/EACTS周術期はいずれもクラス/レベル＋ボーラス/持続レートまで。日本式の「○mgを△mLで希釈し□分」や γ(μg/kg/min) 調製手順は**PMDA電子添文／IF が唯一の原典** → **Part 3 が必須。**
2. **日本のIV薬用量・希釈は JCS/JHRS 2020 EN 表74（既収載）が宝庫。** ランジオロール術後レジメン、ニフェカラント、ジルチアゼム、ベラパミル、ピルシカイニド、フレカイニド、リドカイン、プロカインアミド、シベンゾリン、ジソピラミド、メキシレチン、アプリンジン、Mg、ATP まで具体値あり。**ただしアミオダロンIV／ジゴキシンIVは「添付文書参照」と委譲** → これらは Part 3 で補完。
3. **既著 `CVCU_Emergency_Response_Protocol.md` が大部分の薬剤希釈表を保有。** 統合ドキュメントはこれを**重複させず**、(a) 日本添付文書での正式ソース化、(b) ニフェカラント／ピルシカイニド／ベラパミル／ランジオロールの希釈レシピ、(c) POAF以外の不整脈（粗動・SVT・徐脈/AVブロック・洞機能不全）の体系化、で**拡張**するのが妥当。

### 0-3. 確定したギャップ（=追加DLの根拠）

| ギャップ | 何が無いか | 補完先（Part） |
|---|---|---|
| **術後AVブロック／恒久ペースメーカ適応** | repoの非薬物GLは2021FU（リードレス等）で、術後AVブロックのPPM適応は親GL=2018側。欧米の徐脈/ペーシングGLも無し | Part 2-A |
| **心室性不整脈/SCD（米国版）** | ESC 2022のみ。米国 AHA/ACC/HRS 2017 VA/SCD が無い | Part 2-B |
| **POAF 一次エビデンス（RCT/メタ）** | ランジオロール(PASCAL/PLATON)、PAPABEAR、PALACS、COPPS-2、Mg、Cochrane等の原著が無い | Part 2-C |
| **日本の薬剤 希釈/投与法の一次資料** | ガイドラインに無い（上記2）。PMDA電子添文/IFが必要 | **Part 3** |
| **POAF 総説（背景・機序）** | 機序/予防の state-of-the-art レビューが無い | Part 2-C |

---

## Part 1. Agentタスク指示（検索・DL・保存・報告）

### 手順
1. **Part 2** の各文献を DOI/PMID で取得。無料/PMC優先、有料は landing ページURLを記録。
2. **Part 3** の各薬剤は PMDA で **YJコードまたは商品名検索** → 最新「電子添文」（＋可能なら「インタビューフォーム」）PDF を取得。版が変わるため直リンクではなく検索経由。
3. 既存命名規則で `reference/` 配下に保存（**Part 4** 参照）。添付文書は `reference/Japan/Drug_PackageInserts/` に保存。
4. 取得不能・販売中止・適応外は明記。

### 報告フォーマット（各エントリ）
```markdown
### [学会/製造販売元] [年] [文書名]
- 種別：Guideline / Focused Update / Expert Consensus / RCT / Meta-analysis / Review / 添付文書(IF)
- 取得：成功/失敗（理由）
- 実URL（落としたPDFの直リンク）：
- 版・改訂日：
- アクセス：🆓/💰/📄/PMDA
- 備考：（適応外/販売中止/代替品など）
```

---

## Part 2. 追加DL文献リスト（書誌・検証済み）

> すべて PubMed / DOIリゾルバ / 学会サイトで **PMID↔DOI↔タイトル** を照合済み。`⚠️訂正` は今回の検証で識別子・著者・製造販売元を修正した項目。

### A. 徐脈・伝導障害・ペーシング（術後AVブロック／一時・恒久ペーシング） — *repoに無い*

1. **2018 ACC/AHA/HRS Guideline on Bradycardia and Cardiac Conduction Delay（Full）** — Kusumoto FM, Schoenfeld MH, Barrett C, et al. *Circulation* 2019;140(8):e382-e482. DOI `10.1161/CIR.0000000000000628` / PMID `30586772`. 🆓
   - JACC版（同一内容）：*J Am Coll Cardiol* 2019;74(7):e51-e156. DOI `10.1016/j.jacc.2018.10.044` / PMID `30412709`.
   - 用途：後天性AVブロック・伝導遅延のPPM適応（**心臓弁手術後・TAVR後**の徐脈/AVブロック節を含む）。
2. （任意）**同 Executive Summary** — *Circulation* 2019;140(8):e333-e381. DOI `10.1161/CIR.0000000000000627` / PMID `30586771`. 🆓（推奨表の早見版）
3. **2021 ESC Guidelines on Cardiac Pacing and CRT** — Glikson M, Nielsen JC, Kronborg MB, et al. *Eur Heart J* 2021;42(35):3427-3520. DOI `10.1093/eurheartj/ehab364` / PMID `34455430`. 🆓
   - Europace版：*Europace* 2022;24(1):71-164. DOI `10.1093/europace/euab232` / PMID `34455427`.
   - 用途：**心臓手術後／TAVI後の伝導障害とペーシング適応**、一時心外膜ワイヤーの役割・タイミング。
4. **JCS/JHRS 2019 Guideline on Non-Pharmacotherapy of Cardiac Arrhythmias（=2018年改訂版 本体, 英文）** — Nogami A, Kurita T, Abe H, et al. *J Arrhythm* 2021;37(4):709-870. DOI `10.1002/joa3.12491` / PMID `34386109`. 🆓（PMC8339126）
   - Circ J版：*Circ J* 2021;85(7):1104-1244. DOI `10.1253/circj.CJ-20-0637` / PMID `34078838`. ／ 和文PDF：`https://www.j-circ.or.jp/cms/wp-content/uploads/2018/07/JCS2018_kurita_nogami.pdf`
   - 用途：repo既収載の**2021フォーカスアップデートの親GL**。ペースメーカ/ICD/CRT適応表（**術後AVブロック含む**）の本体。
5. （任意）**2023 HRS/APHRS/LAHRS Cardiac Physiologic Pacing Guideline** — Chung MK, et al. *Heart Rhythm* 2023;20(9):e17-e91. DOI `10.1016/j.hrthm.2023.03.1538` / PMID `37283271`. 🆓（J Arrhythm版 PMID `37799799`）
   - 用途：術後AVブロックで高頻度心室ペーシングが必要な例の His束/左脚領域ペーシング。
6. （任意）**Management of Conduction Disturbances Associated With TAVR: JACC Expert Panel** — Rodés-Cabau J, Ellenbogen KA, Krahn AD, et al. *J Am Coll Cardiol* 2019;74(8):1086-1106. DOI `10.1016/j.jacc.2019.07.014` / PMID `31439219`. 💰
   - 用途：TAVI後 新規LBBB/高度AVブロックのPPMタイミング・アルゴリズム。

### B. 心室性不整脈・心臓突然死（米国版） — *repoはESC 2022のみ*

7. **2017 AHA/ACC/HRS Guideline for Management of Ventricular Arrhythmias and the Prevention of SCD（Full）** — Al-Khatib SM, Stevenson WG, et al. *Circulation* 2018;138(13):e272-e391. DOI `10.1161/CIR.0000000000000549` / PMID `29084731`. 🆓
   - JACC版：*J Am Coll Cardiol* 2018;72(14):e91-e220. DOI `10.1016/j.jacc.2017.10.054` / PMID `29097296`.
   - 用途：既収載 ESC 2022 VA/SCD の**米国対応版**。術後VT/VF・electrical storm・抗不整脈薬・ICD/WCD のクラス/レベル。
8. （任意）**同 Executive Summary** — *Circulation* 2018;138(13):e210-e271. DOI `10.1161/CIR.0000000000000548` / PMID `29084733`. 🆓
   - ⚠️訂正：正誤表（Correction/Erratum）あり — *Circulation* 2018;138(13):e419-e420. DOI `10.1161/CIR.0000000000000614` / PMID `30354425`（必要時のみ）。

### C. POAF 予防・治療：主要RCT／メタ解析／総説

**■ 予防 — ランジオロール（日本のキーエビデンス）**

9. **PASCAL trial** — Sezai A, et al. Landiolol for prevention of AF after CABG. *J Thorac Cardiovasc Surg* 2011;141(6):1478-87. DOI `10.1016/j.jtcvs.2010.10.045` / PMID `21269646`. 💰
   - n=140 CABG、POAF 34.3%→10%。日本採用ランジオロール予防の基幹試験。
10. **PLATON trial** — Sezai A, et al. Landiolol for POAF in LV dysfunction. *J Thorac Cardiovasc Surg* 2015;150(4):957-964. DOI `10.1016/j.jtcvs.2015.07.003` / PMID `26254752`. 💰
    - n=60、LVEF<35%、POAF 40%→10%（血圧低下なし）。低心機能コホート。
11. **Cafaro 2023（メタ解析）** — Cafaro T, et al. Landiolol for prevention of POAF after cardiac surgery: systematic review & meta-analysis. *Can J Anaesth* 2023;70(11):1828-1838. DOI `10.1007/s12630-023-02586-0` / PMID `37917331`. 💰
12. **Kowalik 2024（メタ解析）** — Kowalik K, et al. Landiolol for perioperative atrial tachyarrhythmias. *Br J Anaesth* 2024;133(1):222-225. DOI `10.1016/j.bja.2024.03.036` / PMID `38724326`.
13. **LANDIPROTEC 2026（反証RCT）** — Amour J, et al. Low-dose landiolol does NOT prevent POAF in non-Asian patients. *Br J Anaesth* 2026;136(1):65-73. DOI `10.1016/j.bja.2025.09.019` / PMID `41203473`. 💰
    - **民族差・用量の重要な反証**（低用量2 μg/kg/min は非アジア人で無効）。日本データを一般化する際の必須caveat。

**■ 予防 — アミオダロン**

14. **PAPABEAR trial** — Mitchell LB, et al. Prophylactic oral amiodarone. *JAMA* 2005;294(24):3093-3100. DOI `10.1001/jama.294.24.3093` / PMID `16380589`. 💰
    - ⚠️訂正：landing URL は `https://jamanetwork.com/journals/jama/fullarticle/202097`（旧記載 …/202055 は別記事）。n=601、心房頻脈性不整脈 29.5%→16.1%。
15. **Daoud 1997** — Daoud EG, et al. *Preoperative amiodarone as prophylaxis against atrial fibrillation after heart surgery.* *N Engl J Med* 1997;337(25):1785-1791. DOI `10.1056/NEJM199712183372501` / PMID `9400034`. 💰
    - ⚠️訂正：正式タイトルは上記（"Preoperative amiodarone as prophylaxis…"）。n=124、POAF 53%→25%。

**■ 予防 — コルヒチン／外科手技／スタチン／マグネシウム**

16. **COPPS-2 trial** — Imazio M, et al. Colchicine for postpericardiotomy syndrome & POAF. *JAMA* 2014;312(10):1016-1023. DOI `10.1001/jama.2014.11026` / PMID `25172965`. 💰
17. **PALACS trial** — Gaudino M, et al. Posterior left pericardiotomy for prevention of POAF. *Lancet* 2021;398(10316):2075-2083. DOI `10.1016/S0140-6736(21)02490-9` / PMID `34788640`. 💰
    - POAF 32%→17%（RR 0.55）。外科医がとれる予防手技。
18. **ARMYDA-3 trial** — Patti G, et al. Atorvastatin for reduction of POAF. *Circulation* 2006;114(14):1455-61. DOI `10.1161/CIRCULATIONAHA.106.621763` / PMID `17000910`. 🆓（新GLでは格下げ、歴史的経緯用）
19. **Magnesium（陽性メタ解析）** — ⚠️訂正：Miller S, Crystal E, Garfinkle M, et al. *Effects of magnesium on atrial fibrillation after cardiac surgery: a meta-analysis.* *Heart* 2005;91(5):618-623. DOI `10.1136/hrt.2004.033811` / PMID `15831645`. 🆓（PMC1768903）
    - ※当初候補の「Shiga 2004」識別子は誤り（無関係論文に解決）。Shiga の真の論文は別物：Shiga T, et al. *Am J Med* 2004;117(5):325-333. DOI `10.1016/j.amjmed.2004.03.030` / PMID `15336582`（💰、Mg予防メタ解析）。
20. **Magnesium（陰性メタ解析）** — ⚠️訂正：**Cook RC**, et al.（※"Gu"ではない）*Prophylactic magnesium does not prevent AF after cardiac surgery: a meta-analysis.* *Ann Thorac Surg* 2013;95(2):533-41. DOI `10.1016/j.athoracsur.2012.09.008` / PMID `23141526`. 💰（バイアス低い試験のみで効果消失＝バランス用）
21. **Cochrane 2013** — Arsenault KA, et al. Interventions for preventing POAF in patients undergoing heart surgery. *Cochrane Database Syst Rev* 2013;(1):CD003611.pub3. DOI `10.1002/14651858.CD003611.pub3` / PMID `23440790`. 💰（β遮断/ソタロール/アミオダロン/Mg/スタチン/ペーシングの統括）

**■ 総説（背景・機序・薬理）**

22. **Dobrev 2019** — Dobrev D, Aguilar M, Heijman J, et al. Postoperative atrial fibrillation: mechanisms, manifestations and management. *Nat Rev Cardiol* 2019;16(7):417-436. DOI `10.1038/s41569-019-0166-5` / PMID `30792496`. 💰（機序の定本）
23. **Gaudino 2023** — Gaudino M, Di Franco A, Rong LQ, et al. Postoperative atrial fibrillation: from mechanisms to treatment. *Eur Heart J* 2023;44(12):1020-1039. DOI `10.1093/eurheartj/ehad019` / PMID `36721960`.（心臓外科特化の最新総説 / Editor's Choice）
24. **Floria 2024（ランジオロールPK/PD）** — Floria M, Oancea AF, Morariu PC, et al. PK/PD of landiolol in AF. *Pharmaceutics* 2024;16(4):517. DOI `10.3390/pharmaceutics16040517` / PMID `38675178`. 🆓（PMC11054558）
    - 用途：ランジオロールの希釈・力価調整・投与（半減期~4分、β1選択性、エステラーゼ代謝）の薬理学的裏付け。

### D. 日本の学会資料／周術期

25. **JCS 2022 Guideline on Perioperative Cardiovascular Assessment for Non-Cardiac Surgery** — Hiraoka E, et al. *Circ J* 2023;87(9):1253-1337. DOI `10.1253/circj.CJ-22-0609` / PMID `37558469`. 🆓
    - 用途：周術期の不整脈・β遮断の**一般原則**のみ（**非心臓手術**が対象＝心臓外科POAFには限定的）。
26. **NOTE（要捏造防止）：** 日本心臓血管外科学会（JSCVS）には**独立した POAF／術後不整脈ガイドラインは存在しない**（`jscvs.or.jp/guidelines/` は JCS/JHRS 2021 非薬物の再掲。JSCVS独自は Maze手術と肺動脈カテーテルのステートメントのみ。"心外膜ペーシングワイヤー抜去" は医療安全指針であってPOAF文書ではない）。**存在しない日本GLを作らないこと。**

---

## Part 3. 日本の抗不整脈薬 PMDA 電子添文／IF ダウンロード表 — 「一般名・商品名・希釈方法・投与方法」の原典

> **取得方法：** `https://www.pmda.go.jp/PmdaSearch/iyakuSearch/` で **YJコード**または**商品名**を検索 → 最新「電子添文」＋「インタビューフォーム(IF)」PDF を取得（版サフィックスは改訂で変わるため直リンク非推奨）。保存先 `reference/Japan/Drug_PackageInserts/`。
> **⚠️ は今回の検証で製造販売元・適応・販売状況を訂正/注意喚起した項目**（統合ドキュメントにそのまま反映すること）。
> 多くの IV薬の用量・希釈は **JCS/JHRS 2020 EN 表74（既収載）にも具体値あり** → 添付文書は「現行の正式な希釈/投与法」確定と、表74が委譲したアミオダロンIV/ジゴキシンIVの補完に使う。

### 3-1. レートコントロール（β遮断薬・Ca拮抗薬・ジギタリス）

| 一般名 | 代表的商品名（製造販売元） | YJコード | 術後不整脈での用途・注意 |
|---|---|---|---|
| ランジオロール塩酸塩 | **オノアクト点滴静注用 50mg/150mg**（小野薬品工業） | 2123404D1033 / 2123404D3028 | POAF・術後頻脈の**レートコントロール第一選択**（超短時間β1）。希釈：50mgを生食/5%ブドウ糖≥5mLで溶解→μg/kg/min持続。術後レジメンは表74にも記載 |
| （参考）ランジオロール塩酸塩 | コアベータ静注用 12.5mg（小野薬品工業） | 2123404D2021 | ⚠️適応＝**冠動脈CTの高心拍補正のみ（不整脈は適応外）**。同一一般名2製剤の区別用に併記 |
| ビソプロロールフマル酸塩 | **メインテート錠 0.625/2.5/5mg**（⚠️田辺ファーマ＝旧田辺三菱、2025-12改称）／**ビソノテープ 2/4/8mg**（トーアエイヨー） | 錠 2123016F1107 | 経口/貼付のレート調整・POAF予防。NPO例はテープが有用（経口⇔テープ換算はIF） |
| カルベジロール | アーチスト錠 1.25/2.5/10/20mg（第一三共） | 2149032F1021 | 低心機能/慢性心不全合併のレート調整（αβ遮断）。1.25mg×2から漸増 |
| メトプロロール酒石酸塩 | （セロケン/ロプレソール錠） | — | ⚠️**国内に静注製剤は実質無し**（STS2026の経口12.5–25mgはこれに相当）。IV第一選択は日本ではランジオロール |
| ジルチアゼム塩酸塩 | **ヘルベッサー注射用 10/50**、**250**（⚠️田辺ファーマ＝旧田辺三菱） | 注10/50: 2171405D4050 ／ 注250: 2171405D3020（別添文） | 術後AF/AFLレート調整（β禁忌・喘息例の代替）。希釈：生食/ブドウ糖、10分静注 or 5–15 μg/kg/min持続 |
| ベラパミル塩酸塩 | ワソラン静注 5mg（エーザイ） | 2129402A1040 | PSVT・ベラパミル感受性VT。5mgを生食/ブドウ糖希釈し≥5分緩徐静注。LVEF≤40%は回避 |
| ジゴキシン | **ジゴシン注 0.25mg**（⚠️太陽ファルマ） | 2113400A1032 | 低心機能/HF合併AFのレート調整。緩徐飽和・血中濃度・腎補正はIFが原典（表74はIV量を添付文書委譲） |
| メチルジゴキシン | ラニラピッド錠 0.05/0.1mg（中外製薬） | 2113005F1030 ほか | 経口ジギタリス |

### 3-2. リズムコントロール（Class III・I）

| 一般名 | 代表的商品名（製造販売元） | YJコード | 術後不整脈での用途・注意 |
|---|---|---|---|
| アミオダロン塩酸塩（注） | **アンカロン注 150**（⚠️**サノフィ**／販売 大正製薬。ジェネリック＝アミオダロン塩酸塩静注150mg「TE」トーアエイヨー 2129410A1036） | 2129410A1028 | 難治性VT/VF・術後血行動態不安定AFの第一選択。**5%ブドウ糖で溶解（生食不可・析出）**、初期急速/負荷/維持の3相、専用ライン。表74が委譲した項目＝**添付文書が原典** |
| アミオダロン塩酸塩（経口） | **アンカロン錠 100**（⚠️**サノフィ**） | 2129010F1022 | IV後の経口継続・維持。導入400mg/日→維持200mg/日、甲状腺/肺/肝モニタ |
| ニフェカラント塩酸塩 | **シンビット静注用 50mg**（トーアエイヨー） | 2129407D1030 | **日本独自の純粋IKr遮断薬**。除細動抵抗性VT/VF（術後電気ストーム）。0.3mg/kg単回(5分)＋0.4mg/kg/hr維持、生食/ブドウ糖溶解、QT監視 |
| ソタロール塩酸塩 | ソタコール錠 40/80mg（サンドファーマ／サンド） | 2129013F1026 | ⚠️**販売中止**（経過措置満了 2026-03）→代替＝**ソタロール塩酸塩錠「TE」（トーアエイヨー）**。生命に関わるVT/VF・AF、腎機能依存漸増・入院QT監視 |
| ベプリジル塩酸塩水和物 | ベプリコール錠 50/100mg（⚠️**オルガノン**。2023-10に第一三共から**販売**移管） | 2129011F1035 / 2129011F2031 | **日本特有**の多チャネル遮断。持続性/長期持続性AFのリズムコントロール（他剤抵抗）。QT/TdP監視 |
| ピルシカイニド塩酸塩水和物 | サンリズム注射液 50（第一三共） | 2129408A1020 | **日本独自の純粋Ic**。発作性AFの薬理学的除細動（器質心疾患なし）。0.75–1.0mg/kgを生食/ブドウ糖希釈し10分静注、腎排泄＝腎補正 |
| プロカインアミド塩酸塩 | アミサリン注 100/200mg（⚠️**アルフレッサファーマ**） | 2121400A1034 / 2121400A2030 | 安定monomorphic VT、WPW+AF、麻酔関連不整脈。緩徐静注、QRS/QT/血圧で中止基準 |
| リドカイン塩酸塩 | 静注用キシロカイン 2%（サンドファーマ／サンド） | 1214401A5022 | 虚血性VT/VFの第二選択・アミオダロン代替。1–2mg/kg→0.5–4mg/min持続、肝/低心拍出で減量 |
| ジソピラミドリン酸塩 | リスモダンP静注 50mg（クリニジェン） | 2129401A1070 | ⚠️**販売中止（2025-06）**＝歴史的原典としてのみ可。Ia群、陰性変力・抗コリン・QT監視 |
| フレカイニド/シベンゾリン/ピルメノール 等 | （タンボコール/シベノール 等） | — | IV用量・希釈は**JCS/JHRS 2020 EN 表74（既収載）に具体値あり**。必要時のみ各添付文書を追加取得 |

### 3-3. 電解質

| 一般名 | 代表的商品名（製造販売元） | YJコード | 用途・注意 |
|---|---|---|---|
| 硫酸マグネシウム水和物 | **硫酸Mg補正液 1mEq/mL**（大塚製薬工場）／静注用マグネゾール・マグセント注（あすか製薬） | 補正液 1244401A1069 | TdP・難治性VF・低Mg補正・POAF予防のMg負荷。⚠️**いずれも不整脈は適応外**（補正液＝電解質補正、マグネゾール/マグセント＝産科適応のみ）→**適応外使用である旨を明記** |
| カリウム製剤 | （KCl注 等／補正液） | — | ⚠️POAFのルーチンK補正は**Class III no-benefit**（TIGHT-K）。低K是正の文脈で |

### 3-4. 徐脈・ペーシング隣接／蘇生

| 一般名 | 代表的商品名（製造販売元） | YJコード | 用途・注意 |
|---|---|---|---|
| アトロピン硫酸塩水和物 | ⚠️**アトロピン硫酸塩注0.5mg「ニプロ」**（ニプロ。旧「タナベ」は廃止/経過措置終了）／アトロピン注0.05%シリンジ「テルモ」（テルモ） | ニプロ 1242405A1089 ／ テルモ 1242406G1035 | 迷走神経性/症候性徐脈・AVブロックのブリッジ（ペーシング前/不全時）。0.5mg静注・反復上限 |
| l-イソプレナリン塩酸塩 | プロタノールL注 **0.2mg**（興和） | 0.2mg 2119400A1036 | ⚠️**1mg（2119400A2032）は販売中止**→0.2mgを使用。アトロピン抵抗性徐脈・完全AVブロックの心拍維持、TdP予防のoverdrive。0.2–1.0mgを等張液200–500mLで希釈し持続 |
| アデノシン三リン酸二ナトリウム水和物(ATP) | アデホス-Lコーワ注 20/40mg（興和）／トリノシンS注（⚠️**製造＝アルフレッサファーマ、販売＝トーアエイヨー**。"持田"は誤り） | アデホス 3992400A2138(20)/3992400A3045(40) | PSVT(AVNRT/AVRT)の急速ワンショット静注＋後押しフラッシュ（海外adenosine代替）。⚠️**PSVTは添付文書上の適応外**（適応＝頭部外傷後遺症/心不全等） |
| アドレナリン | ボスミン注 1mg（第一三共）／アドレナリン注0.1%シリンジ「テルモ」（テルモ） | ボスミン 2451400A1030 ／ テルモ 2451402G1040 | 心停止蘇生・術後昇圧。⚠️**術後はSTS2017の「少量50–300μgボーラス・ルーチン投与回避」原則**に注意 |

---

## Part 4. 推奨ディレクトリ配置（既存構造に整合）

```
reference/
├── Japan/
│   ├── Arrhythmia/
│   │   └── JCS_JHRS_2018_Non_Pharmacotherapy_Arrhythmia_Base_EN.pdf      # 文献4（親GL本体）
│   ├── Perioperative_Management/
│   │   └── JCS_2022_NonCardiac_Surgery_Perioperative_Guidelines.pdf       # 文献25
│   └── Drug_PackageInserts/                                               # Part 3（PMDA電子添文/IF）
│       ├── Landiolol_Onoact_PI.pdf
│       ├── Amiodarone_Ancaron_IV_PI.pdf
│       ├── Nifekalant_Shinbit_PI.pdf
│       ├── Diltiazem_Herbesser_IV_PI.pdf
│       ├── ...（各薬剤）
├── Europe/
│   └── Arrhythmia/
│       └── ESC_2021_Cardiac_Pacing_CRT_Guidelines.pdf                     # 文献3
└── US/
    └── Arrhythmia/
        ├── ACC_AHA_HRS_2018_Bradycardia_Conduction_Delay_Guidelines.pdf   # 文献1
        └── AHA_ACC_HRS_2017_Ventricular_Arrhythmias_SCD_Guidelines.pdf    # 文献7
（POAF RCT/総説 = 文献9-24 は reference 配下に Literature/POAF_Trials/ 等を新設して保存可）
```

---

## 凡例・注意
1. `🆓`無料/PMC ／ `💰`有料 ／ `📄`学会PDF ／ `PMDA`電子添文。`⚠️訂正`は今回の検証で識別子・著者・製造販売元・適応・販売状況を修正した項目。
2. **発行日と命名年を区別**（例：「2018 ガイドライン」が Circulation 2019 掲載＝正常）。
3. PMDA 添付文書は **PMIDなし／版サフィックス変動**。YJコード or 商品名検索で最新版を取得。
4. **適応外（PSVTのATP、不整脈のMg製剤、コアベータ）・販売中止（ソタコール/リスモダンP静注/プロタノールL注1mg/アトロピン「タナベ」）**は統合ドキュメントで明記し、現行代替品を併記する。
5. 日本のIV抗不整脈薬の多くは **JCS/JHRS 2020 EN 表74（既収載）** に用量・希釈の具体値あり。添付文書はこれを正式ソース化＋アミオダロンIV/ジゴキシンIVの補完に用いる。
