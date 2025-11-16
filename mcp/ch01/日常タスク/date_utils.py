"""
Date and Time Utility Functions
--------------------------------
このファイルは、日付・時間に関する便利なユーティリティ関数をまとめたものです。
初心者でも読みやすいよう、関数の説明(docstring)を添えています。
"""

from datetime import datetime, timedelta, timezone
import pytz


def get_today_str(fmt: str = "%Y-%m-%d") -> str:
    """
    今日の日付を指定フォーマットの文字列で返す。

    Parameters:
        fmt (str): 日付フォーマット。例: "%Y-%m-%d" "=" "2025-01-01"

    Returns:
        str: フォーマットされた今日の日付。
    """
    return datetime.now().strftime(fmt)


def get_now_jst() -> datetime:
    """
    現在時刻を日本時間(JST)の datetime オブジェクトとして返す。

    Returns:
        datetime: JST の現在時刻。
    """
    jst = timezone(timedelta(hours=9))
    return datetime.now(jst)


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    datetime オブジェクトを指定フォーマットで文字列に変換する。

    Parameters:
        dt (datetime): 変換したい datetime オブジェクト
        fmt (str): 変換後のフォーマット

    Returns:
        str: フォーマットされた文字列
    """
    return dt.strftime(fmt)


def add_days(dt: datetime, days: int) -> datetime:
    """
    指定した日数だけ datetime を加算する。

    Parameters:
        dt (datetime): 元になる日時
        days (int): 加算する日数（負の数も可）

    Returns:
        datetime: 加算後の日時
    """
    return dt + timedelta(days=days)


def parse_datetime(text: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    日付文字列を datetime オブジェクトに変換する。

    Parameters:
        text (str): パース対象の文字列
        fmt (str): 適用するフォーマット

    Returns:
        datetime: 変換された datetime オブジェクト
    """
    return datetime.strptime(text, fmt)


def convert_timezone(dt: datetime, tz_name: str = "Asia/Tokyo") -> datetime:
    """
    datetime オブジェクトを指定タイムゾーンに変換する。

    Parameters:
        dt (datetime): 元の日時
        tz_name (str): タイムゾーン名（例: "Asia/Tokyo", "UTC"）

    Returns:
        datetime: 変換後の日時
    """
    tz = pytz.timezone(tz_name)
    if dt.tzinfo is None:
        # naive datetime の場合は UTC とみなした上で変換
        dt = pytz.utc.localize(dt)
    return dt.astimezone(tz)
