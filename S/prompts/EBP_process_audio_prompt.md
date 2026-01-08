# EBP 流程（回到 Audio Prompt 核心）

> 目的：把 EBP 的「介入」重新鎖定在 **預錄語音提示／時間點語音引導（audio/voice prompts）**，避免主論點被「節拍器/音樂節奏」帶走。
> 更新：2025-12-22

---

## 0) Scope Guardrails（先把界線畫清楚）

### 什麼算本專案的介入（✅）
- **預錄語音提示（pre-recorded voice / audio prompts）**：在特定時間點自動播報，協助記憶流程與時間管理（例如：2 分鐘循環、心律檢查、換手、給藥提醒）。
- **純聽覺引導**：不依賴螢幕/視覺回饋，降低急救現場視覺負荷。

### 容易跑偏、但只作「背景補充」的介入（🟡）
- **節拍器（metronome / tonal guidance）**：可改善按壓頻率，但常被研究成「唯一介入」，會把討論焦點拉走。

### 明確排除（❌）
- 只有音樂節奏（music tempo）而無語音提示
- 即時 dispatcher 電話指導（DA-CPR）
- 依表現即時調整的回饋裝置（real-time feedback device）
- 以 **VAM（voice advisory manikin）本體**作為介入（訓練假人內建回饋）

> 專案文件的核心結論與推薦，應主要建立在「✅ audio/voice prompts」的證據上；節拍器只放在「補充討論」。

---

## 1) ASK：把問題問對（PICO）

### 建議的最終問題句
在模擬 IHCA 情境中，**非急救專責**的一般醫護人員，使用「**自動語音提示計時器（預錄語音 prompts + 重要時間點提醒）**」相較於傳統無語音引導的急救流程，是否能提升 **高品質 CPR**（壓胸深度/頻率達標、減少中斷、流程時間更準確）？

### PICO（精簡版）
| 元素 | 定義 |
|---|---|
| P | 病房/門診護理師、值班住院醫師等非急救專責醫護人員（模擬 IHCA） |
| I | 自動語音提示計時器（預錄語音 prompts + 2 分鐘循環/心律檢查/給藥等時間提醒；純聽覺） |
| C | 傳統急救流程（無語音引導，自行計時與流程管理） |
| O | Primary：壓胸深度/頻率達標率；Secondary：hands-off/no-flow、2 分鐘循環偏差、給藥時間準確度、自我效能/焦慮 |

---

## 2) ACQUIRE：找得到「對的」證據

### 核心檢索
- 先跑 `../../C/literature/文獻搜尋結果_策略一.md`（audio/voice prompt 直球）
- 再用 `../../C/literature/文獻搜尋結果_策略二.md` 做敏感性擴充（但主結論不依賴純 metronome）

### 檢索與篩選要留下的紀錄（之後要做 PRISMA）
- 每個資料庫：日期、完整字串、命中篇數
- 去重後篇數
- Title/abstract 排除的原因（用固定分類：music-only / dispatcher-only / real-time feedback / pediatric-only / non-CPR 等）

---

## 3) APPRAISE：評讀時只抓「結果」與「可信度」

### 先選 2–3 篇最能直接回答 PICO 的核心文獻
優先順序建議：
1. 臨床情境 + audio prompts（例如：Chiang 2005）
2. 預錄語音指令（例如：Birkun 2018）
3. 以「流程/時間提示」為介入的模擬研究（例如：Lukas 2013）

### 每篇文獻至少要抽取（可直接貼回 `../../C/EBP_plan.md`）
- 研究設計與場域（IHCA/OHCA、模擬/臨床）
- 受試者（是否接近「非急救專責」）
- 介入內容（有沒有「語音提示」與「時間點提醒」，能否與其他回饋分離）
- 主要結果（用 result/conclusion，不從 discussion 推論）
- 效果量與精確度（差值、RR/OR、95% CI；若沒有就註記缺失）
- 偏差風險重點（隨機化、盲化、資料遺失、混雜）

---

## 4) APPLY：把證據轉成你的「語音流程設計」

### 介入設計原則（以認知輔助為主，不是只控頻率）
- **時間軸明確**：2:00 停止壓胸/心律檢查、換手、（符合條件時）給藥提醒
- **語句短、可執行、可驗證**：避免冗長衛教式語音
- **事件觸發比固定時間更貼近臨床**：例如 Epi 根據上次給藥時間動態提示（參考 `cpr_timer_app/README.md`）
- **節拍器可選**：把 metronome 當作「按壓頻率輔助」而非主介入

---

## 5) ASSESS：用一個可落地的研究設計驗證

### 最小可行（MVP）研究設計
- Prospective randomized controlled simulation study
- 對象：病房護理師／值班住院醫師
- 比較：語音提示計時器 vs 傳統流程

### 建議量測（和你要回答的 O 一致）
- Manikin 資料：壓胸深度/頻率達標率、chest compression fraction、hands-off
- 流程時間：2 分鐘循環偏差、心律檢查時間點、給藥時間準確度
- 主觀量表：自我效能、焦慮程度

---

## 對應到本資料夾的「真實來源」
- 研究題目/PICO/評讀摘要：`../../C/EBP_plan.md`
- 搜尋紀錄：`../../C/literature/文獻搜尋結果_策略一.md`、`../../C/literature/文獻搜尋結果_策略二.md`
- 背景（IHCA/first responder 痛點）：`../../C/literature/文獻回顧_IHCA問題.md`
- PDF 原文：`文獻考證/`
- 介入原型（語音提示計時器）：`cpr_timer_app/`
