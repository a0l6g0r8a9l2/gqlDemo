from graphene import (Mutation, ID, Boolean)

from demoGql.services.followers import FollowersService
from demoGql.utils import dev_log


class FollowUp(Mutation):
    class Arguments:
        user_id = ID(required=True)
        follow_up_id = ID(required=True)

    ok = Boolean()

    @dev_log
    def mutate(self, info, user_id: int, follow_up_id: int):
        follow_up = FollowersService().follow_up(user_id=user_id, follow_up_user_id=follow_up_id)
        if follow_up:
            return FollowUp(ok=True)
        return FollowUp(ok=False)
