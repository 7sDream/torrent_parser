# Torrent file parser for Python

## Install

```
pip install torrent_parser
```

## Usage:

### CLI

```
$ pytp test.torrent
```

```
$ cat test.torrent | pytp
```

![][screenshots-help]

![][screenshots-normal]

![][screenshots-indent]


### As a module

```pycon
>>> import torrent_parser as tp
>>> data = tp.parse_torrent_file('test.torrent')
>>> print(data['announce'])
http://tracker.trackerfix.com:80/announce
```

## Test

```bash
python -m unittest test
```

## LICENSE

See [License][LICENSE].

[screenshots-help]: http://rikka-10066868.image.myqcloud.com/7c23f6d0-b23f-4c57-be93-d37fafe3292a.png
[screenshots-normal]: http://rikka-10066868.image.myqcloud.com/1492616d-9f14-4fe2-9146-9a3ac06c6868.png
[screenshots-indent]: http://rikka-10066868.image.myqcloud.com/eadc4184-6deb-42eb-bfd4-239da8f50c08.png
[LICENSE]: https://github.com/7sDream/torrent_parser/blob/master/LICENSE
