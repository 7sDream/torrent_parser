# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.4] - 2018-04-06

### Added

- `encoding` option can be `auto`, which will use `chardet` package to decide which encoding to use. If `chardet` is noe installed, will raise a warning and fallback to 'utf-8'. (Thanks to [@ltfychrise])
- Add changelog.

### Change

- Reorganize test codes/files.

### Fixed

- Fix integer filed can't be negative bug. (Thanks to [@ltfychrise])
- Fix `_seek_back` method not make `_pos` back bug. (Thanks to [@ltfychrise])

## [0.1.3] - 2017-06-21

### Added

- Now `UnicodeDecodeError` is wrapped in `InvalidTorrentDataException`.

### Fixed

- Use `IOError` instead of `FileNotFoundError` in Python 2.

### Changed

- `InvalidTorrentFileException` rename to `InvalidTorrentDataException`.

## [0.1.2] - 2017-06-21

### Changed

- Emm, I don't know, I just changed the version code...

## [0.1.1] - 2017-06-20

### Added

- CLI add coding `--coding/-c` option for file string filed encoding.

### Changed

- `ed2k` and `filehash` field now use same structure as 'pieces'.

## [0.1.0] - 2017-05-23

### Added

- Parse torrent from file and data into a dict.
- CLI provided.
- Simple tests.
- Available on pip.

[@ltfychrise]: https://github.com/ltfychrise
[Unreleased]: https://github.com/7sDream/torrent_parser/compare/v0.1.4...HEAD
[0.1.4]: https://github.com/7sDream/torrent_parser/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/7sDream/torrent_parser/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/7sDream/torrent_parser/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/7sDream/torrent_parser/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/7sDream/torrent_parser/tree/v0.1.0
