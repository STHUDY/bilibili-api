"""
bilibili_api

哔哩哔哩的各种 API 调用便捷整合（视频、动态、直播等），另外附加一些常用的功能。
"""

import asyncio
import platform

from . import (
    album,
    app,
    article,
    article_category,
    ass,
    audio,
    bangumi,
    black_room,
    channel,
    channel_series,
    cheese,
    client,
    comment,
    creative_center,
    dynamic,
    emoji,
    favorite_list,
    game,
    homepage,
    hot,
    interactive_video,
    live,
    live_area,
    login,
    login_func,
    manga,
    note,
    rank,
    search,
    session,
    settings,
    topic,
    user,
    video,
    video_tag,
    video_uploader,
    video_zone,
    vote,
)
from .errors import (
    ApiException,
    ArgsException,
    CredentialNoBiliJctException,
    CredentialNoBuvid3Exception,
    CredentialNoDedeUserIDException,
    CredentialNoSessdataException,
    DanmakuClosedException,
    DynamicExceedImagesException,
    LiveException,
    LoginError,
    NetworkException,
    ResponseCodeException,
    ResponseException,
    VideoUploadException,
)
from .credential import Credential
from .utils.aid_bvid_transformer import aid2bvid, bvid2aid
from .utils.danmaku import Danmaku, DmFontSize, DmMode, SpecialDanmaku
from .utils.network_httpx import HEADERS, Api, check_valid, enc_wbi, get_mixin_key, get_nav, get_session, request, retry, set_session
from .utils.parse_link import ResourceType, parse_link
from .utils.picture import Picture
from .utils.short import get_real_url
from .utils.sync import sync

BILIBILI_API_VERSION = "15.5.0"

# 如果系统为 Windows，则修改默认策略，以解决代理报错问题
if "windows" in platform.system().lower():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore

__all__ = [
    "Api",
    "ApiException",
    "ArgsException",
    "BILIBILI_API_VERSION",
    "check_valid",
    "Credential",
    "CredentialNoBiliJctException",
    "CredentialNoBuvid3Exception",
    "CredentialNoDedeUserIDException",
    "CredentialNoSessdataException",
    "Danmaku",
    "DanmakuClosedException",
    "DmFontSize",
    "DmMode",
    "DynamicExceedImagesException",
    "enc_wbi",
    "HEADERS",
    "LiveException",
    "LoginError",
    "NetworkException",
    "Picture",
    "ResourceType",
    "ResponseCodeException",
    "ResponseException",
    "SpecialDanmaku",
    "VideoUploadException",
    "aid2bvid",
    "album",
    "app",
    "article",
    "article_category",
    "ass",
    "asyncio",
    "audio",
    "bangumi",
    "black_room",
    "bvid2aid",
    "channel",
    "channel_series",
    "cheese",
    "client",
    "comment",
    "creative_center",
    "dynamic",
    "emoji",
    "favorite_list",
    "game",
    "get_mixin_key",
    "get_nav",
    "get_real_url",
    "get_session",
    "homepage",
    "hot",
    "interactive_video",
    "live",
    "live_area",
    "login",
    "login_func",
    "manga",
    "note",
    "parse_link",
    "platform",
    "rank",
    "request",
    "retry",
    "search",
    "session",
    "set_session",
    "settings",
    "sync",
    "topic",
    "user",
    "video",
    "video_tag",
    "video_uploader",
    "video_zone",
    "vote"
]
