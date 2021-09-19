from random import randint
from graphene.test import Client

from ..api import schema

tests_users_names = [f'Daenerys Targaryen {randint(0, 100)}',
                     f'Jon Snow {randint(0, 100)}',
                     f'Cersei Lannister {randint(0, 100)}',
                     f'Tyrion Lannister {randint(0, 100)}']
tests_users_emails = [name.replace(' ', '') + '@mail.ru' for name in tests_users_names]
test_users_passwords = [item.split(' ')[0] + 'Pass' for item in tests_users_names]


def make_test_user():
    """
    :return dict representation of default_user
    """
    index = randint(0, 3)
    arguments = ['name', 'email', 'password']
    user = {}.fromkeys(arguments)
    for arg in arguments:
        if arg == 'name':
            user[arg] = tests_users_names[index]
        if arg == 'email':
            user[arg] = tests_users_emails[index]
        if arg == 'password':
            user[arg] = test_users_passwords[index]
    return user


class TestUser:
    default_user = make_test_user()
    subscriber = make_test_user()

    def test_create_user(self, is_subscriber: bool = False):
        """
        mutation {
          createUser(email: "JonSnow@mail.ru", password: "JonPass", name: "Jon Snow") {
            default_user {
              id
              name
              email
            }
          }
        }

        :return:
        """
        if not is_subscriber:
            user = self.default_user
        else:
            user = self.subscriber
        user_mutation_head = 'mutation { createUser( '
        user_mutation_args = f'email: "{user["email"]}", ' \
                             f'password: "{user["password"]}", ' \
                             f'name: "{user["name"]}"'
        user_mutation_tail = ') {user { id name email } } }'
        mutation = user_mutation_head + user_mutation_args + user_mutation_tail
        client = Client(schema)
        executed = client.execute(mutation)
        assert executed['data']['createUser']['user']['name'] == user['name']
        if not is_subscriber:
            self.default_user['id'] = executed['data']['createUser']['user']['id']
        else:
            self.subscriber['id'] = executed['data']['createUser']['user']['id']

    def test_query_user(self):
        """
        query {
          default_user(id: 1) {
            name
          }
        }
        """
        user_query_head = '{ user ('
        user_query_args = f'id: {self.default_user["id"]}'
        user_query_tail = ') { name } }'
        query = user_query_head + user_query_args + user_query_tail
        client = Client(schema)
        executed = client.execute(query)
        assert executed['data']['user']['name'] == self.default_user['name']

    def test_create_post(self):
        """
        mutation{
          createPost(content: "content from Mary", title: "Mary 2st post", postedBy:1){
            post{
              postId
              title
              content
              date
              author{
                id
                name
              }
            }
          }
        }
        """
        user_mutation_head = 'mutation { createPost( '
        user_mutation_args = f'content: "content from {self.default_user["name"]}", ' \
                             f'title: "{self.default_user["name"]}s {randint(0, 100)} post", ' \
                             f'postedBy: "{self.default_user["id"]}"'
        user_mutation_tail = '){ post{ postId title content date author{ id name } } } }'
        mutation = user_mutation_head + user_mutation_args + user_mutation_tail
        client = Client(schema)
        executed = client.execute(mutation)
        assert executed['data']['createPost']['post']['author']['id'] == self.default_user['id']
        self.default_user['posts'] = executed['data']['createPost']['post']

    def test_follow_up(self):
        """
        mutation{
          followUp(followUpId:1 userId:2){
            ok
          }
        }
        """
        self.test_create_user(is_subscriber=True)
        user_mutation_head = 'mutation { followUp( '
        user_mutation_args = f'followUpId: "1", ' \
                             f'userId: "{self.subscriber["id"]}"'
        user_mutation_tail = ') { ok } }'
        mutation = user_mutation_head + user_mutation_args + user_mutation_tail
        client = Client(schema)
        executed = client.execute(mutation)
        assert executed['data']['followUp']['ok']
