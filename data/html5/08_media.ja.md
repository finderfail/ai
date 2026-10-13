# HTML5：音声、動画、iframe

```html
<video controls width="640" poster="preview.jpg" preload="metadata">
  <source src="movie.webm" type="video/webm">
  <source src="movie.mp4" type="video/mp4">
  <track src="subs-ja.vtt" kind="subtitles" srclang="ja" label="日本語" default>
  お使いのブラウザは動画に対応していません。
</video>

<video autoplay muted loop playsinline src="bg.mp4"></video>

<audio controls src="podcast.mp3"></audio>

<iframe src="https://www.youtube-nocookie.com/embed/ID"
        width="560" height="315" loading="lazy"
        title="動画" allowfullscreen></iframe>
```

- 音声付きの自動再生はブラウザがブロックする。背景動画には `muted` と `playsinline` が必要。
- 複数の `<source>` があれば、ブラウザは対応する最初の形式を使う。
- 字幕は WebVTT 形式を `<track>` で指定する。
- `iframe` には `title` を付ける。外部コンテンツには `sandbox` を使う。
