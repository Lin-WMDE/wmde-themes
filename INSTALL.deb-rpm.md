# Установка на deb/rpm-дистрибутивах без сборки из сырцов вручную

Шаблон: см. предыдущие компоненты. Автор собирает пакеты у себя локально, как сейчас `makepkg -si`.

Опорные платформы — Debian stable и Fedora: `.deb` собираем на Debian (встаёт и на Ubuntu/Mint),
`.rpm` — на Fedora (встаёт и на RHEL/openSUSE). Наоборот не гарантируется.

Пакет data-only: компиляции нет, только `just install` + nFPM. Тулчейн не нужен.

## Собрать

```sh
# зависимости сборки: just + nfpm
cargo install --locked nfpm  # или бинарник с github.com/goreleaser/nfpm/releases

just deb   # -> target/wmde-themes_*.deb
just rpm   # -> target/wmde-themes-*.rpm
```

Версия — `1.10.0.<commits>.g<sha>`, как `pkgver()` в `PKGBUILD`.

## Поставить

```sh
# Debian/Ubuntu/Mint
sudo apt install ./target/wmde-themes_*.deb

# Fedora/RHEL/openSUSE
sudo dnf install ./target/wmde-themes-*.rpm
```

Шрифты Noto тянутся жёстко (тема их называет). `wmde-icons-base` — в recommends:
в PKGBUILD это hard dep, но пакета пока нет в репозиториях дистрибутивов.
Когда выйдет единый репозиторий WMDE — переключить в depends.
Обоина темой только называется (путь), рисует её `wmde-bg`.
