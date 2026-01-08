# EBP 計畫：語音引導輔助系統提升 CPR 品質

> 整理自實證競賽報告與師長回饋 (2025.12)

---

## 一、研究題目

**原始題目**：語音引導輔助系統能否有效提升醫護人員執行心肺復甦流程遵循率

**建議修改方向**（依師長建議）：
- 避免使用「遵從度」→ 改為「高品質 CPR」或具體成效指標
- 聚焦於按壓深度、按壓頻率、按壓成效等臨床指標

**修訂題目建議**：
> 「語音引導輔助系統對非急救專責人員執行高品質心肺復甦術之成效」

---

## 二、臨床情境與痛點

### 臨床情境
- 夜班護理師在病房時常僅有 2 人值班
- 非 ICU 或急診病房較少執行急救
- 突發 IHCA（院內心跳停止）狀況導致緊張、害怕、壓力
- 只能憑記憶回想流程

### 臨床痛點
1. 病房/門診護理師不常執行 CPR
2. 只能靠記憶完成急救流程
3. 按壓速度、深度、頻率不確定
4. 何時給藥、確認心律等流程混亂
5. 無法達到 AHA CPR guideline 標準

### 文獻支持：IHCA CPR 品質問題

#### Abella et al. 2005 (JAMA, PMID: 15657323)

**Quality of cardiopulmonary resuscitation during in-hospital cardiac arrest**

| CPR 品質參數 | 發現 | 指引標準 |
|-------------|------|---------|
| 壓胸頻率不足 | **28.1%** 的時段 < 90/min | 100-120/min |
| 壓胸深度不足 | **37.4%** 的壓胸 < 38 mm | ≥ 50 mm |
| 過度換氣 | **60.9%** 的時段 > 20/min | 10-12/min |

> 「The quality of CPR was inconsistent and **often did not meet guideline recommendations**, even when performed by **well-trained hospital staff**」

#### 夜間/週末（Off-Hours）更糟

| 來源 | 發現 |
|------|------|
| 27 篇系統性文獻 | 夜間/週末 IHCA 存活率**顯著較低** |
| 瑞典研究 2023 | 日間 30 天存活 36.8%，夜間下降 |
| Singapore GH 2024 | 急救團隊反應時間 **3-5 分鐘**，first responder 需獨撐 |

#### First Responder 困境

```
急救團隊抵達前 3-5 分鐘
┌─────────────────────────────────────┐
│  First Responder 獨自面對：         │
│  • 壓胸頻率/深度難維持標準          │
│  • 2 分鐘循環計時困難               │
│  • 壓力大、焦慮高、自信心不足       │
│  • 夜間人力少，可能單獨急救         │
└─────────────────────────────────────┘
```

詳細文獻見：`literature/文獻回顧_IHCA問題.md`

---

## 三、介入定義釐清

### 本專案介入：自動語音提示計時器 (Automated Voice Prompt Timer)

| 特徵 | 說明 |
|------|------|
| **核心功能** | **預錄語音提示 + 時間點提醒**：在關鍵節點自動播報（2 分鐘循環、心律檢查、換手、給藥等） |
| **節拍器（可選模組）** | 100–120 BPM（預設 110）用於壓胸頻率引導；**非本次 EBP 的核心結論來源** |
| **回饋類型** | 純聽覺（無視覺回饋），降低施作者視覺負荷 |
| **應用場景** | 臨床/模擬急救情境的即時引導 |

### 與相似概念區分

| 概念 | 定義 | 與本專案關係 |
|------|------|-------------|
| **Automated Voice Prompt** | 自動語音提示系統（計時器播放語音引導） | ✅ 本專案介入 |
| **Metronome/Rhythm Guide** | 節拍器（維持按壓頻率） | 🟡 可選功能（非核心） |
| **Pre-recorded Audio Instructions** | 預錄語音指導 | ✅ 高度相關 |
| **Voice Advisory Manikin (VAM)** | 訓練用假人內建回饋系統 | ❌ 非研究主體 |
| **Real-time Visual Feedback** | 即時視覺回饋（如螢幕顯示） | ❌ 本專案排除 |

---

## 四、PICO 架構

### 原始 PICO
| 元素 | 內容 |
|------|------|
| **P** | 急救醫護人員（IHCA 事件發生時的團隊） |
| **I** | 輔助系統（音效輔助系統、節拍器） |
| **C** | 標準傳統急救流程（依照傳統知識執行） |
| **O** | 整體 CPR 品質改善 |

### 師長建議修正

#### Population 問題
> ⚠️ **龍子老師指出**：背景講的是「急救小組來之前大家很慌亂」，但 PICO 搜尋用 "emergency team"。到底是給急救團隊還是「普羅大眾醫護人員」（800 年才急救一次的人）？

**建議修正**：
- P 應為：**非急救專責之一般醫護人員**（病房護理師、門診護理師、值班住院醫師等）
- 而非急救小組成員

#### Intervention 關鍵字問題
> ⚠️ 第一篇文獻用的是 "music tempo"，但 PICO 的 I 沒有用到這個 term

#### Outcome 問題
> ⚠️ 「遵從度」在實證競賽上不討喜（遵從就是勾勾勾，100%）

**建議修正 Outcome**：
- 按壓深度 (compression depth)
- 按壓頻率 (compression rate)
- 按壓品質分數
- Hands-off time / No-flow fraction
- 施作者自信心/自我效能
- 施作者焦慮程度

### 修訂後 PICO

| 元素 | 修訂內容 |
|------|---------|
| **P** | 非急救專責之一般醫護人員（病房/門診護理師、值班住院醫師）於模擬 IHCA 情境 |
| **I** | 自動語音提示計時器（**預錄語音 prompts + 2 分鐘循環/心律檢查/給藥等時間提醒；純聽覺回饋**）<br>（節拍器 100–120 BPM 可作為可選模組，但不作為本次 EBP 的主要結論依據） |
| **C** | 傳統急救流程（無語音引導，自行計時管理） |
| **O** | **Primary**: 按壓深度、按壓頻率達 AHA 標準之比率<br>**Secondary**: 流程時間偏差、施作者自我效能、焦慮程度 |

---

## 五、文獻搜尋策略

### 介入特性與搜尋範圍

本專案介入為 **預錄語音提示 (Pre-recorded Audio Prompt)**，具以下特性：
- 預先錄製的語音指令
- 固定時間點自動播放
- 單向提示（非互動式）
- 純聽覺引導

### 搜尋概念架構

| PICO 元素 | 搜尋概念 | 關鍵字 |
|-----------|---------|--------|
| **P** | CPR 執行者 | healthcare provider, nurse, physician, rescuer, layperson |
| **I** | 預錄語音提示 | 見下方詳細關鍵字 |
| **C** | 標準 CPR | standard CPR, conventional CPR, no audio aid |
| **O** | CPR 品質 | CPR quality, compression depth, compression rate, guideline compliance |

### Intervention 搜尋關鍵字

#### 納入關鍵字（Include）
| 類別 | 關鍵字 | 說明 |
|------|--------|------|
| **預錄語音** | pre-recorded audio, pre-recorded instructions, audio prompt | 核心概念 |
| **語音輔助** | audio aid, audio assistance, voice prompt, voice guidance | 語音提示形式 |
| **自動化指導** | automated instructions, automated voice, automated audio | 自動播放特性 |
| **聽覺引導** | auditory guidance, auditory cue, audio-guided CPR | 聽覺引導概念 |

#### 排除關鍵字（Exclude）
| 類別 | 關鍵字 | 排除原因 |
|------|--------|---------|
| **音樂** | music, musical, song, tempo-guided | 非語音提示，機制不同 |
| **Dispatcher** | dispatcher-assisted, telephone CPR, DA-CPR | 即時互動式，非預錄 |
| **即時回饋裝置** | real-time feedback device, CPR feedback device | 根據表現即時調整，非固定提示 |
| **VAM 系統** | Voice Advisory Manikin, VAM system | VAM 作為「介入」本身，非外部語音引導 |
| **視覺回饋** | visual feedback, visual display, screen | 本專案聚焦純聽覺 |
| **AED 內建** | defibrillator feedback, AED prompt | 非獨立系統 |

> **注意**：`manikin` 或 `simulation` 不應排除，因多數 CPR 研究皆於模擬情境進行。
> 排除的是 **VAM 作為介入**（假人內建回饋系統），而非在假人上進行的模擬研究。

### 建議搜尋字串

#### 策略一：精準搜尋（Primary Search）
聚焦於 audio prompt 核心概念，預期結果 10-20 篇
```
("cardiopulmonary resuscitation"[MeSH] OR "CPR"[tiab] OR "chest compression"[tiab])
AND
("audio prompt"[tiab] OR "audio-prompt"[tiab] OR "voice prompt"[tiab]
 OR "auditory prompt"[tiab] OR "timed prompt"[tiab] OR "audio guidance"[tiab])
```

#### 策略二：擴充搜尋（Expanded Search）
加入 metronome 與 auditory feedback，預期結果 50-80 篇，需人工篩選
```
("cardiopulmonary resuscitation"[MeSH] OR "CPR"[tiab] OR "chest compression"[tiab])
AND
("audio prompt"[tiab] OR "voice prompt"[tiab] OR "auditory feedback"[tiab]
 OR "auditory guidance"[tiab] OR "tonal guidance"[tiab] OR "metronome"[tiab])
AND
("quality"[tiab] OR "rate"[tiab] OR "depth"[tiab] OR "guideline"[tiab])
```

#### 策略三：敏感性搜尋（Sensitive Search）
最廣泛搜尋，預期結果 100+ 篇
```
("cardiopulmonary resuscitation"[MeSH] OR "CPR"[tiab] OR "chest compression"[tiab])
AND
("audio"[tiab] OR "voice"[tiab] OR "auditory"[tiab] OR "sound"[tiab])
AND
("prompt"[tiab] OR "guidance"[tiab] OR "instruction"[tiab] OR "feedback"[tiab])
```

#### Cochrane/CINAHL 搜尋策略
```
(cardiopulmonary resuscitation OR CPR OR chest compression)
AND
(audio prompt OR voice prompt OR auditory feedback OR auditory guidance
 OR timed prompt OR metronome)
AND
(quality OR compression rate OR compression depth OR guideline)
```

### 搜尋策略說明

> **注意**：經 PubMed 實測，`pre-recorded` 一詞在文獻中較少使用。
> 文獻多使用 `audio prompt`、`voice prompt`、`auditory feedback` 等術語。
>
> **建議流程**：
> 1. 先執行策略一（精準搜尋）
> 2. 若結果不足，再執行策略二（擴充搜尋）
> 3. 人工篩選排除：music-only、dispatcher-only、real-time feedback device

### 納入/排除標準

#### 納入標準 (Inclusion Criteria)
1. 研究對象：執行 CPR 之人員（醫護人員或一般民眾）
2. 介入：使用預錄語音提示或自動化語音引導
3. 結果：報告 CPR 品質相關指標
4. 設計：RCT、quasi-experimental、前後比較研究

#### 排除標準 (Exclusion Criteria)
1. 介入為音樂或節奏引導（無語音內容）
2. 介入為即時 dispatcher 電話指導
3. 介入為根據表現即時調整的回饋裝置
4. 介入為 Voice Advisory Manikin (VAM) 系統本身（假人內建回饋）
5. 介入包含視覺回饋成分且無法分離聽覺效果

> **注意**：模擬研究（simulation study）或使用假人（manikin）作為研究場域者，不予排除。

### 資料庫與預期篩選

| 資料庫 | 預期策略 |
|--------|---------|
| PubMed | 主要搜尋，使用 MeSH + 自由詞 |
| Cochrane Library | 搜尋 systematic reviews 與 RCTs |
| CINAHL | 護理相關文獻 |
| Embase | 補充搜尋，需去重 |

### 策略一搜尋結果（2025-12-20 實測）

| 項目 | 數量 |
|------|------|
| 總篇數 | 11 |
| 高度相關 | 2 |
| 可能相關 | 1 |
| 需排除 | 8 |

詳細結果見：`literature/文獻搜尋結果_策略一.md`

### 策略二搜尋結果（2025-12-20 實測）

| 項目 | 數量 |
|------|------|
| 總篇數 | 76 |
| ⭐⭐⭐ 高度相關（Audio/Voice Prompt） | 6 |
| ⭐⭐ 中度相關（Metronome 研究） | 22 |
| ⭐ 低相關或需排除 | 48 |

**新增高度相關文獻**：
- Bohn 2011 (PMID: 21146279) — Voice prompts + AV feedback（負面結果）
- Cason 2011 (PMID: 21810239) — Visual vs auditory vs no feedback
- Lukas 2013 (PMID: 23702601) — CPR guidance 改善 adherence
- van Tulder 2015 (PMID: 29094836) — Voice metronome 於電話 CPR

詳細結果見：`literature/文獻搜尋結果_策略二.md`

---

## 六、文獻評讀結果

### 收錄文獻總覽

| # | 文獻 | 年份 | 設計 | 介入類型 | 相關性 | 來源 |
|---|------|------|------|---------|--------|------|
| 1 | Chiang et al. | 2005 | 前後比較 | Audio-prompts | ⭐⭐⭐ 高 | 策略一搜尋 |
| 2 | Milander et al. | 1995 | 實驗室研究 | Audible tone | ⭐⭐⭐ 高 | 策略一搜尋 |
| 3 | Birkun et al. | 2018 | RCT | Pre-recorded audio | ⭐⭐⭐ 高 | 文獻考證資料夾 |
| 4 | Bohn et al. | 2011 | 觀察研究 | Voice prompts + AV | ⭐⭐⭐ 高 | 策略二搜尋 |
| 5 | Cason et al. | 2011 | 交叉試驗 | Auditory feedback | ⭐⭐ 中 | 策略二搜尋 |
| 6 | Lukas et al. | 2013 | 模擬研究 | CPR guidance | ⭐⭐ 中 | 策略二搜尋 |
| 7 | van Tulder et al. | 2015 | RCT | Voice metronome | ⭐⭐ 中 | 策略二搜尋 |
| 8 | 智慧手錶研究 | - | RCT | 視覺+聽覺回饋 | ⭐⭐ 中 | 原始 EBP |
| 9 | 音樂節奏研究 | - | RCT | 音樂節奏 | ⭐ 低 | 原始 EBP |
| 10 | Wik et al. (VAM) | 2001 | 模擬研究 | VAM 系統 | ⭐ 低 | 文獻考證資料夾 |
| 11 | Sutton et al. (VAM) | 2007 | RCT | VAM 系統 | ⭐ 低 | 文獻考證資料夾 |

---

### ⭐⭐⭐ 高度相關文獻（直接支持本專案）

#### 1. Chiang et al. 2005 (PMID: 15733757) — 台灣研究

**Better adherence to the guidelines during cardiopulmonary resuscitation through the provision of audio-prompts**

| 項目 | 內容 |
|------|------|
| **設計** | 兩階段研究（觀察期 + 介入期） |
| **場域** | 臨床急救（影片分析） |
| **對象** | 急救團隊 |
| **介入** | Audio-prompts（語音提示） |
| **主要發現** | |
| Hands-off periods | 16.9±7.9s → **12.7±5.3s** |
| Total hands-off time | 273±153s → **164±94s** |
| Intubation <20s | 10% → **56.3%** |
| **結論** | Audio-prompts 可顯著改善臨床 CPR guideline adherence |
| **DOI** | [10.1016/j.resuscitation.2004.09.010](https://doi.org/10.1016/j.resuscitation.2004.09.010) |

**與本專案關聯**：直接研究 audio-prompts，介入概念相同，且為台灣研究

---

#### 2. Milander et al. 1995 (PMID: 7584749)

**Chest compression and ventilation rates during cardiopulmonary resuscitation: the effects of audible tone guidance**

| 項目 | 內容 |
|------|------|
| **設計** | 觀察研究 + 實驗室研究 |
| **對象** | 12 例 IHCA + 41 名志願者 |
| **介入** | Audible tone guidance（聽覺音調引導） |
| **主要發現** | |
| Compression rate | 74±22 → **100±3 /min** (p<0.01) |
| End-tidal CO₂ | 15±7 → **17±7 torr** (p<0.01) |
| **結論** | Audible tones 可顯著提升壓胸頻率 |
| **DOI** | [10.1111/j.1553-2712.1995.tb03622.x](https://doi.org/10.1111/j.1553-2712.1995.tb03622.x) |

**與本專案關聯**：聽覺引導提升壓胸頻率，支持語音提示的效果

---

#### 3. Birkun et al. 2018 (PMID: 29580863)

**Pre-recorded instructional audio vs. dispatchers' conversational assistance in telephone cardiopulmonary resuscitation: A randomized controlled simulation study**

| 項目 | 內容 |
|------|------|
| **設計** | RCT |
| **對象** | 109 名醫學生（無 CPR 經驗） |
| **介入** | Pre-recorded instructional audio vs Dispatcher 口頭指導 |
| **主要發現** | |
| Overall score | 5.6±2.2 vs 5.1±1.9 (P>0.05) 無顯著差異 |
| Time to 1st compression | **86.0±14.3s** vs 91.2±14.2s (P<0.05) |
| Total compressions | **170.2±48.0** vs 156.2±60.7 (P<0.05) |
| Compression rate | **94.9±26.4** vs 89.1±32.8 /min |
| **結論** | 預錄語音引導與 dispatcher 指導效果相當，但開始時間更快 |
| **DOI** | [10.5847/wjem.j.1920-8642.2018.03.001](https://doi.org/10.5847/wjem.j.1920-8642.2018.03.001) |

**與本專案關聯**：直接比較 pre-recorded audio，證實預錄語音的可行性

---

#### 4. Bohn et al. 2011 (PMID: 21146279) — ⚠️ 負面結果

**The addition of voice prompts to audiovisual feedback and debriefing does not modify CPR quality or outcomes in out of hospital cardiac arrest**

| 項目 | 內容 |
|------|------|
| **設計** | 前瞻性觀察研究 |
| **場域** | 德國 EMS，OHCA 真實案例 |
| **對象** | 3,177 例院外心跳停止 |
| **介入** | AED with voice prompts + audiovisual feedback vs AED only |
| **主要發現** | Voice prompts 未額外改善 CPR 品質 |
| **結論** | Adding voice prompts 在 EMS 專業人員中未顯著改善結果 |
| **DOI** | [10.1016/j.resuscitation.2010.11.006](https://doi.org/10.1016/j.resuscitation.2010.11.006) |

**與本專案關聯**：
- ⚠️ 負面結果需討論
- 對象為 EMS 專業人員（非本專案目標族群）
- 情境為 OHCA（非本專案院內情境）
- 已有 AV feedback，voice prompts 為「額外」加入

---

### ⭐⭐ 中度相關文獻

#### 5. Cason et al. 2011 (PMID: 21810239)

**Counterbalanced cross-over study of visual, auditory and no feedback on CPR**

| 項目 | 內容 |
|------|------|
| **設計** | 交叉試驗（counterbalanced） |
| **對象** | 護理學生 |
| **介入** | Visual feedback vs Auditory feedback vs No feedback |
| **主要發現** | 三組在按壓深度、頻率均無顯著差異 |
| **DOI** | [10.1186/1472-6955-10-13](https://doi.org/10.1186/1472-6955-10-13) |

**與本專案關聯**：需釐清其 auditory feedback 的具體形式（是否為純語音提示）

---

#### 6. Lukas et al. 2013 (PMID: 23702601)

**CPR guidance improves medical students' adherence to guidelines in simulated cardiac arrest**

| 項目 | 內容 |
|------|------|
| **設計** | 模擬研究 |
| **對象** | 醫學生 |
| **介入** | CPR guidance（時間提示系統） |
| **主要發現** | Guidance 組 guideline adherence 顯著提升 |
| **DOI** | [10.1097/EJA.0b013e32835e61d5](https://doi.org/10.1097/EJA.0b013e32835e61d5) |

**與本專案關聯**：支持時間提示系統的效果，對象為學生（接近本專案非急救專責人員）

---

#### 7. van Tulder et al. 2015 (PMID: 29094836)

**Effects of a voice metronome on compression rate and depth in telephone-assisted bystander CPR**

| 項目 | 內容 |
|------|------|
| **設計** | RCT |
| **對象** | 一般民眾 |
| **介入** | Voice metronome 透過電話播放 |
| **主要發現** | 提升按壓頻率準確度 |

**與本專案關聯**：Voice + metronome 結合的研究，支持語音節拍引導

---

#### 8. 智慧手錶提高高品質 CPR（台灣研究）

| 項目 | 內容 |
|------|------|
| **設計** | RCT，80 名受試者 |
| **介入** | Smart Watch（視覺回饋 + 揚聲器 + 110 BPM 節拍器） |
| **結論** | 可改善 CPR 速率、深度與品質 |
| **限制** | 無法區分視覺/聽覺哪種回饋更有效 |
| **與本專案關聯** | 支持聽覺引導有效，但混合視覺回饋 |

---

### ⭐ 低相關文獻（概念不同或介入差異大）

| 文獻 | 介入 | 排除/低相關原因 |
|------|------|----------------|
| 音樂節奏研究 | 音樂節奏引導 | 非語音提示，機制不同 |
| Wik 2001 (VAM) | Voice Advisory Manikin | VAM 為訓練假人回饋系統，非外部語音引導 |
| Sutton 2007 (VAM) | Voice Advisory Manikin | 同上 |

---

### 文獻證據總結

| 發現 | 支持文獻 | 證據強度 |
|------|---------|---------|
| Audio-prompts 改善 guideline adherence | Chiang 2005 | 中（前後比較） |
| Audible tone 提升壓胸頻率 | Milander 1995 | 中（實驗室研究） |
| Pre-recorded audio 與 dispatcher 效果相當 | Birkun 2018 | 高（RCT） |
| CPR guidance 改善 adherence | Lukas 2013 | 中（模擬研究） |
| Voice metronome 改善頻率準確度 | van Tulder 2015 | 高（RCT） |
| 混合視聽回饋改善 CPR 品質 | 智慧手錶研究 | 高（RCT） |
| Voice prompts 對 EMS 未額外改善 | Bohn 2011 | 中（觀察研究）⚠️ |

**整體結論**：
- 現有證據**支持**聽覺引導（audio prompts, audible tones）可改善 CPR 品質
- 策略二新增 4 篇高/中相關文獻，包含 1 篇負面結果（Bohn 2011）
- **負面結果解讀**：Bohn 2011 對象為 EMS 專業人員、已有 AV feedback，與本專案情境不同
- **Research Gap 確認**：缺乏針對「純聽覺預錄語音提示」於「非急救專責人員」的近期 RCT

---

## 七、Research Gap 分析

### 為何近期預錄語音提示 RCT 稀少？

| 時期 | 研究焦點 | 代表技術 |
|------|---------|---------|
| 1990-2005 | 基礎聽覺引導 | Audio prompts, audible tones |
| 2005-2015 | 即時回饋裝置 | CPR feedback devices, accelerometers |
| 2015-present | 多模式回饋 | Audiovisual feedback, wearables, AI |

**可能原因**：
1. **商業驅動**：Feedback devices 有廠商支持（ZOLL, Philips），預錄語音無商業利益
2. **AED 整合**：現代 AED 已內建語音提示，獨立系統被視為過時
3. **問題被認為「已解決」**：早期研究顯示正向結果，學界轉向新議題
4. **Dispatcher-assisted CPR 興起**：研究資源流向 DA-CPR 優化

### 現有文獻的 Research Gap

| Gap | 說明 | 本專案如何填補 |
|-----|------|---------------|
| **純聽覺回饋** | 現有研究多混合視覺+聽覺 | 聚焦純聽覺引導 |
| **ACLS 流程時間** | 缺乏 2 分鐘循環、給藥時間研究 | 設計含流程時間提示 |
| **非急救專責人員** | 多數研究對象為學員 | 對象為病房護理師 |
| **院內情境 (IHCA)** | 多數聚焦 OHCA | 聚焦院內急救 |
| **近期證據** | 高相關文獻多為 2005 年前 | 提供 2025 年新證據 |

### 本專案的創新點與臨床意義

> 「儘管早期研究顯示 audio prompts 有效，但近年研究轉向即時回饋裝置與 dispatcher-assisted CPR。然而，對於**資源有限的院內情境**（如夜班病房），複雜的回饋裝置不切實際。本研究重新檢視**低成本、易部署的預錄語音提示系統**對非急救專責人員執行高品質 CPR 之效果。」

---

## 八、師長回饋重點整理

### 龍子老師

#### 1. 文獻評讀與結論的 Gap
> 「評讀完兩篇都說不確定，但最後可以提出一個很確定的結論，所以你的實證跟你想要做的事情是有 gap 的。」

**建議**：
- 呈現方式要更 precise
- 結論請從 conclusion/result 截取，不要從 discussion
- 要 highlight 哪些是有可信度的

#### 2. 效果量報告
> 「介入措施效果不是問你用 SPSS/R 分析什麼（how），是問 intervention 到底有沒有效（what）。」

**應報告**：
- Intervention 是否有效
- 效果量多精確（95% CI）
- 利弊權衡後是否值得

#### 3. 評讀量表填答
- 沒有交代 → **Can't tell**，不是自動變成 **No**
- 例如：受試者因有戴手錶無法盲化 → 應交代「無法盲化」

### 其他老師建議

#### Research Gap 作為亮點
> 「如果這兩篇無法告訴除了 tempo 以外的結論（如按壓深度），那就是你們的 research gap，下一步可以回答的。」

**亮點**：
- 安妮假人可以匯出按壓深度數據
- 可聚焦於「純聽覺」回饋的效果（排除視覺干擾）

#### 應用價值
- **橫向應用**：其他不常做 CPR 的單位
- **縱向應用**：新人訓練
- **升等研究**：可考慮升等計畫來進行

---

## 九、計畫導入方向

### 介入設計：自動語音提示計時器
1. **語音提示（核心）**於預設時間點播放：
   - 急救開始、角色確認
   - 1:55 準備停止提醒
   - 2:00 停止壓胸、心律檢查
   - 4:00 給 Epinephrine 提醒
   - 每 2 分鐘循環重複
2. **節拍器（可選）**設定 110 BPM（AHA 標準 100-120），僅作為按壓頻率輔助
3. **不做視覺回饋**：希望視覺留給臨床評估病人狀態

### 預期成效指標
| 指標類型 | 指標 | 測量方式 |
|---------|------|---------|
| **Primary** | 按壓頻率達標率 | 安妮假人數據 |
| **Primary** | 按壓深度達標率 | 安妮假人數據 |
| **Secondary** | 2 分鐘循環時間偏差 (Δt) | 計時記錄 |
| **Secondary** | Epinephrine 給藥時間準確度 | 觀察紀錄 |
| **Secondary** | 施作者自我效能 | 問卷量表 |
| **Secondary** | 施作者焦慮程度 | 問卷量表 |

### 研究設計建議
- **類型**：Prospective Randomized Controlled Simulation Study
- **場域**：臨床技能中心 / 模擬中心
- **對象**：病房護理師、值班住院醫師
- **先做模擬情境**，未來再推廣至臨床

---

## 十、待辦事項

- [ ] 使用更新後搜尋策略重新搜尋文獻
- [ ] 納入 Birkun 2018 等預錄語音相關研究
- [ ] 重新評讀文獻，聚焦於 conclusion/result
- [ ] 報告效果量與 95% CI
- [ ] 確認 Population 定義（非急救專責人員）
- [ ] 完善語音引導計時器內容設計
- [ ] 規劃模擬情境研究流程
- [ ] 準備 IRB 送審文件

---

## 十一、相關資源

- [EBP 專案頁面 (Notion)](https://languid-sassafras-99b.notion.site/EBP-2025-12-31-20abe56f2cf2802eb38ef4ebe81dc573)
- EBP 流程（回到 Audio Prompt 核心）：`../S/prompts/EBP_process_audio_prompt.md`
- CPR 語音引導計時器：`cpr_timer_app/`
- 語音提示音檔：`cpr_timer_app/voice_mp3/`
- 文獻考證：`文獻考證/`

---

*文件整理日期：2025-12-20*
*最後更新：2025-12-20（新增 IHCA 問題文獻支持、策略二搜尋結果）*
