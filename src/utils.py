from environs import env

CURRENT_SEM_CODE = "2526ODDSEM"


def is_ci() -> bool:
    """Distinguish from a CI or local run."""
    return env.bool("CI", False)


def get_user_id() -> str:
    """Get the user id for webkiosk login."""
    user_id = env.str("USSR_ID", None)
    if not user_id or (user_id := user_id.strip()) == "":
        raise ValueError("USSR_ID not provided! Required for webkiosk login")
    return user_id


def get_user_pass() -> str:
    """Get the user password for webkiosk login."""
    user_pass = env.str("PIN", None)
    if not user_pass or (user_pass := user_pass.strip()) == "":
        raise ValueError("PIN not provided! Required for webkiosk login")
    return user_pass


def get_sem_code():
    return CURRENT_SEM_CODE
