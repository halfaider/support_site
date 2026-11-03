import os
import sys
import subprocess
import traceback
from typing import Sequence


def check_packages(packages: Sequence[tuple[str, str]]) -> None:
    for pkg, pi in packages:
        try:
            __import__(pkg)
        except Exception:
            subprocess.check_call((sys.executable, "-m", "pip", "install", pi))


# support_site 에 필요한 파이썬 패키지 설치
# 그 외 패키지는 모듈 관리자에 의해 설치되도록
check_packages((
    ("xmltodict", "xmltodict"),
    ("lxml", "lxml"),
    ("curl_cffi", "curl_cffi"),
))

from support import SupportSC

from .site_util import SiteUtil
from .util_nfo import UtilNfo

try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'wavve.py')):
        from .wavve import SupportWavve
    else:
        SupportWavve = SupportSC.load_module_f(__file__, 'wavve').SupportWavve
except Exception:
    print(traceback.format_exc())


try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'tving.py')):
        from .tving import SupportTving
    else:
        SupportTving = SupportSC.load_module_f(__file__, 'tving').SupportTving
except Exception:
    print(traceback.format_exc())


try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'cppl.py')):
        from .cppl import SupportCppl
    else:
        SupportCppl = SupportSC.load_module_f(__file__, 'cppl').SupportCppl
except Exception:
    print(traceback.format_exc())


from .server_util import MetadataServerUtil
from .site_daum import SiteDaum
from .site_daum_movie import SiteDaumMovie
from .site_daum_tv import SiteDaumTv
from .site_lastfm import SiteLastfm
from .site_melon import SiteMelon
from .site_naver import SiteNaver, SiteNaverMovie
from .site_naver_book import SiteNaverBook
from .site_tmdb import SiteTmdbFtv, SiteTmdbMovie, SiteTmdbTv
from .site_tvdb import SiteTvdbTv
from .site_tving import SiteTvingMovie, SiteTvingTv
from .site_vibe import SiteVibe
from .site_watcha import SiteWatcha, SiteWatchaKTv, SiteWatchaMovie, SiteWatchaTv
from .site_wavve import SiteWavveMovie, SiteWavveTv
from .tool_imgur import ToolImgur
from .tool_naver_cafe import ToolNaverCafe

