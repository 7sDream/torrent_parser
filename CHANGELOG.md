# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## Unreleased

### Add

- cli add `--hash-row`, `-r` option to use raw hash strategy.

### Fixed

- Fix fields order in CLI output may not as same as it in origin files.

## [0.4.0] - 2022.01.17

### Added

- Add `usebytes` error handler. It will use `strict` mode when decoding bytes to string, but if error happened, it returns raw bytes instead of raise exception.
- Add `TorrentFileCreator` class.
- **Internal** Add `DataWrapper` and `JSONEncoderDataWrapperBytesToString` for output convert `bytes` into `string` when output using json format. CLI output needs them, but normal users should not use those two class.

### Changed

- Default mode of `parse_torrent_file` and `TorrentFileParser` change to `usebytes`.
- **BREAK!**`BEcoder` and `BDecoder` will not treat any field as hash fields by default.
- `BDecoder` accept file-like object as input.

## [0.3.0] - 2018.06.23

### Added

- Add `errors` option in `TorrentFileParser` and `parse_torrent_file` to let user set the encoding error handler. (Thanks [@yasuotakei])
- Add `-e`/`--error` to CLI option to set the `errors` option of `parse_torrent_file`.
- `BDecoder` class and `decode` shortcut function to directly decode bytes.
- `decode` shortcut function to directly encode data to bytes.
- Added `hash_fields` parameter and method to customize hash field list.
- Added `hash_raw` parameter to let all hash field be parsed as raw bytes.

### Changed

- **BreakChange** `TorrentFileCreator` rename to `BEncoder` as the origin name don't describe its function.
- `TorrentFileParser` don't need the outmost level of parsed data to be a `dict` now.
- `BEncoder` don't need the outmost level of encoded data to be a `dict` now.
- `BEncoder` now support encode raw bytes.

## [0.2.0] - 2018.5.25

### Changed

- Just bump version to 0.2.0 to follow semver.

## [0.1.5rc1] - 2018.4.28

### Added

- `TorrentFileCreator` class and `create_torrent_file` shortcut function for write back data to a torrent file.

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
[@yasuotakei]: https://github.com/yasuotakei
[Unreleased]: https://github.com/7sDream/torrent_parser/compare/v0.3.0...HEAD
[0.4.0]: https://github.com/7sDream/torrent_parser/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/7sDream/torrent_parser/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/7sDream/torrent_parser/compare/v0.1.5rc1...v0.2.0
[0.1.5rc1]: https://github.com/7sDream/torrent_parser/compare/v0.1.4...v0.1.5rc1
[0.1.4]: https://github.com/7sDream/torrent_parser/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/7sDream/torrent_parser/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/7sDream/torrent_parser/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/7sDream/torrent_parser/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/7sDream/torrent_parser/tree/v0.1.0
