# Maintainer: WMDE <https://wmde.fun>
#
# The WMDE theme: every default that decides how the desktop looks. Data-only, no Rust
# build - the files are baked by tools/wmde-theme-gen and committed here.
#
# This package is what makes a CLEAN INSTALL and a NEW USER look like WMDE without a
# single line of code having run: cosmic-config reads /usr/share/wmde/<id>/v<N>/<key> as
# the system default whenever the user has no value of their own.
#
# Mandatory on purpose - wmde-desktop depends on it. A stack without it falls back to the
# values compiled into libcosmic, which are upstream COSMIC's and drift on every merge.
pkgname=wmde-themes
pkgver=1.0.0
pkgrel=1
pkgdesc="WMDE theme - the palettes, fonts, metrics, panel, dock and wallpaper defaults"
arch=('any')
url="https://wmde.fun"
license=('GPL-3.0-only')
# The theme NAMES resources, so it has to guarantee they exist. Without these the desktop
# does not fall back to something sane - it falls back to whatever fontconfig substitutes,
# which is how a missing font family turns into a desktop that looks broken rather than
# plain.
#  - noto-fonts carries both families the theme names, Noto Sans and Noto Sans Mono.
#    libcosmic's compiled fallback is Open Sans, which nothing in this stack installs.
#  - wmde-icons-base owns the WMDE icon theme that fun.wmde.Tk/icon_theme points at.
# The wallpaper is the exception: it is named by path and drawn by wmde-bg, and depending
# on the daemon would invert the relationship - the theme says what to show, it does not
# own what shows it.
depends=('noto-fonts' 'wmde-icons-base')
# The boot splash theme is dead files without Plymouth, but the distribution decides whether
# to boot with a splash, not the theme.
optdepends=('plymouth: the WMDE boot splash')
makedepends=('just' 'git')
source=("$pkgname::git+https://github.com/Lin-WMDE/wmde-themes.git#branch=wmde")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  # WMDE version: <COSMIC major.minor>.<WMDE release>.<commits since the nearest tag>.g<short>.
  local desc
  desc=$(git describe --long --tags --abbrev=7 2>/dev/null || true)
  if [ -n "$desc" ]; then
    printf '1.11.1.%s.g%s' "$(printf '%s' "$desc" | sed -E 's/.*-([0-9]+)-g[0-9a-f]+$/\1/')" "$(git rev-parse --short=7 HEAD)"
  else
    printf '1.11.1.%s.g%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  fi
}

package() {
  cd "$srcdir/$pkgname"
  just rootdir="$pkgdir" install
}
