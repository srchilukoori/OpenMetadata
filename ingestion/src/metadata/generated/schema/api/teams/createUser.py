# generated by datamodel-codegen:
#   filename:  schema/api/teams/createUser.json
#   timestamp: 2021-10-31T21:55:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.teams import user
from ...type import basic, profile


class CreateUserEntityRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: user.UserName
    description: Optional[str] = Field(None, description='Used for user biography.')
    displayName: Optional[str] = Field(
        None, description="Name used for display purposes. Example 'FirstName LastName'"
    )
    email: basic.Email
    timezone: Optional[str] = Field(None, description='Timezone of the user')
    isBot: Optional[bool] = Field(
        None,
        description='When true indicates user is a bot with appropriate privileges',
    )
    isAdmin: Optional[bool] = Field(
        False,
        description='When true indicates user is an administrator for the system with superuser privileges',
    )
    profile: Optional[profile.Profile] = None
    teams: Optional[List[basic.Uuid]] = Field(
        None, description='Teams that the user belongs to'
    )
