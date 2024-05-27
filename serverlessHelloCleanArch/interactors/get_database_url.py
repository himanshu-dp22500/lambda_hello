import os

from dotenv import load_dotenv

from serverlessHelloCleanArch.constants.config import LOCAL_DATABASE_URL


class GetDatabaseURLInteractor:
    def get_database_url(self) -> str:
        load_dotenv()
        current_stage = os.environ.get("CURRENT_STAGE", "local")

        if current_stage == "local":
            return LOCAL_DATABASE_URL
