# gradio簡介

gradio是什麼？

* gradio是一個讓開發者可以**快速替程式建立使用介面**讓別人可以從網路上使用該程式**的python套件**。

gradio官網

* [gradio官網](https://gradio.app/)

gradio安裝

```bash
pip install gradio
```

gradio基本使用

```python
import gradio as gr
gr.Interface(fn, inputs, outputs).launch()
# fn: 你的函式
# inputs: 你的函式的輸入
# outputs: 你的函式的輸出
```

基礎：

* 基本使用
* 網路分享 (share)
* 保護存取 (auth)
* 即時運算 (live=True)
* 程式偵錯 (debug)
* 異常標註 (flag)
* 輸入及輸出 (inputs & outputs)
* 組件及縮寫 (components & shortcuts)
* 自訂區塊 (blocks)

應用：

* 寫一個字典服務
* 寫一個影像處理服務
* 佈署到 Huggingface spaces

