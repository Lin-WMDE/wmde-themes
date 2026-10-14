rootdir := ''
prefix := '/usr'

base-dir := absolute_path(clean(rootdir / prefix))
# cosmic-config finds the system default through XDG_DATA_DIRS with the "wmde" prefix,
# so the tree has to land at <datadir>/wmde/<config-id>/v<N>/<key>.
default-schema-target := base-dir / 'share' / 'wmde'
# The boot splash theme; Plymouth finds themes by name under this directory.
plymouth-target := base-dir / 'share' / 'plymouth' / 'themes' / 'wmde'

default:
    @just --list

# Install every default that makes up the theme.
install:
    cd default_schema && find * -type f -exec install -Dm0644 '{}' '{{default-schema-target}}/{}' \;
    cd plymouth/wmde && find * -type f -exec install -Dm0644 '{}' '{{plymouth-target}}/{}' \;

# Uninstalls everything (requires same arguments as given to install).
# Removes exactly the files this package installed - never a glob over the shared
# wmde/ directory, which other packages also write into.
uninstall:
    cd default_schema && find * -type f -exec rm -f '{{default-schema-target}}/{}' \;
    cd plymouth/wmde && find * -type f -exec rm -f '{{plymouth-target}}/{}' \;

# Show the current git commit
git-rev:
    @git rev-parse --short HEAD
