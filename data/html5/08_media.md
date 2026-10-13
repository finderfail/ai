# HTML5: аудио, видео, iframe

```html
<video controls width="640" poster="preview.jpg" preload="metadata">
  <source src="movie.webm" type="video/webm">
  <source src="movie.mp4" type="video/mp4">
  <track src="subs-ru.vtt" kind="subtitles" srclang="ru" label="Русский" default>
  Ваш браузер не поддерживает видео.
</video>

<video autoplay muted loop playsinline src="bg.mp4"></video>

<audio controls src="podcast.mp3"></audio>

<iframe src="https://www.youtube-nocookie.com/embed/ID"
        width="560" height="315" loading="lazy"
        title="Видео" allowfullscreen></iframe>
```

- Автовоспроизведение со звуком браузеры блокируют: для фонового видео нужны `muted` и `playsinline`.
- Несколько `<source>` — браузер возьмёт первый поддерживаемый формат.
- Субтитры — формат WebVTT через `<track>`.
- У `iframe` указывайте `title`; для чужого содержимого используйте `sandbox`.
