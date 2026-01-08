# G — Acceptance Criteria（Definition of Done）

> 這份檔案只放「可驗收」描述；細節設計與理由放在 `C/`。

## Prototype：CPR 語音引導計時器（`cpr_timer_app/`）

### 可驗收條件（MVP）
- 能在本機以瀏覽器開啟 `cpr_timer_app/index.html` 正常使用（iPad/桌機皆可）。
- 具備 2 分鐘循環倒數與心律檢查提示（含語音提示與必要視覺警示）。
- 具備 Epinephrine 提示（符合 `cpr_timer_app/README.md` 描述的 v2.1 動態邏輯）。
- 具備事件記錄（電擊 / Epi / ROSC）與重置。
- 語音提示音檔維護方式可重現（見 `cpr_timer_app/generate_tts.py` 與 `cpr_timer_app/voice_mp3/`）。

### 待補（研究面）
- 研究設計與量測定義（Primary/Secondary outcomes）與資料收集流程（放 `C/`，並在完成後於此追加「如何驗收」）。

