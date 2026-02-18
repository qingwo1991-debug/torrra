from dataclasses import asdict, dataclass
from typing import Any, Literal, TypedDict

import libtorrent as lt


# TORRENT TYPES
class TorrentDict(TypedDict):
    """Dict variant of Torrent dataclass."""

    magnet_uri: str
    title: str
    size: float
    seeders: int
    leechers: int
    source: str


class TorrentStatus(TypedDict):
    """Torrent status on upload and download."""

    # 修復：解決 AttributeError: module 'libtorrent' has no attribute 'torrent_status'
    # 由於 libtorrent 的 Python 綁定在不同環境下結構不同，直接引用 lt.torrent_status 會導致崩潰。
    # 改用 Any 或 int 可以確保程序正常啟動。
    state: Any  
    progress: float
    down_speed: float
    up_speed: float
    seeders: int
    leechers: int
    is_paused: bool


class TorrentRecord(TypedDict):
    """Torrent data stored in db."""

    magnet_uri: str
    title: str
    size: float
    source: str
    is_paused: bool
    is_notified: bool


@dataclass
class Torrent:
    """Torrent I/O dataclass."""

    magnet_uri: str
    title: str
    size: float
    seeders: int
    leechers: int
    source: str

    @classmethod
    def from_dict(cls, d: TorrentDict) -> "Torrent":
        return cls(**d)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# INDEXER TYPES
IndexerName = Literal["jackett", "prowlarr"]


@dataclass
class Indexer:
    """Indexer dataclass."""

    name: IndexerName
    url: str
    api_key: str
