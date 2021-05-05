import graphene
from graphene_django.types import DjangoObjectType
from .models import User, Topic
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql_relay import from_global_id
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model
import graphql_jwt


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains'],
            'is_staff': ['exact']
        }
        interfaces = (relay.Node,)


class UserCreateMutation(relay.ClientIDMutation):
    class Input:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserNode)

    def mutate_and_get_payload(root, info, **input):
        user = get_user_model()(
            username=input.get('username'),
        )
        user.set_password(input.get('password'))
        user.save()

        return UserCreateMutation(user=user)


class TopicNode(DjangoObjectType):
    class Meta:
        model = Topic
        filter_fields = {
            'title': ['exact', 'icontains'],
            'is_talking': ['exact'],
            'is_closed': ['exact'],
        }
        interfaces = (relay.Node,)



class TopicCreateMutation(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)

    topic = graphene.Field(TopicNode)

    def mutate_and_get_payload(root, info, **input):

        topic = Topic(
            title=input.get('title'),
        )
        topic.save()

        return TopicCreateMutation(topic=topic)




class TopicUpdateMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        is_talking = graphene.Boolean(required=True)
        is_closed = graphene.Boolean(required=True)

    topic = graphene.Field(TopicNode)

    @login_required
    def mutate_and_get_payload(root, info, **input):

        topic = Topic(
            id=from_global_id(input.get('id'))[1]
        )
        topic.title = input.get('title')
        topic.is_talking = input.get('is_talking')
        topic.is_closed = input.get('is_closed')

        topic.save()

        return TopicUpdateMutation(topic=topic)



class TopicDeleteMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    topic = graphene.Field(TopicNode)

    @login_required
    def mutate_and_get_payload(root, info, **input):

        topic = Topic(
            id=from_global_id(input.get('id'))[1]
        )
        topic.delete()

        return TopicDeleteMutation(topic=None)



class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    create_topic = TopicCreateMutation.Field()
    update_topic = TopicUpdateMutation.Field()
    delete_topic = TopicDeleteMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()



class Query(graphene.ObjectType):
    user = graphene.Field(UserNode, id=graphene.NonNull(graphene.ID))
    all_users = DjangoFilterConnectionField(UserNode)
    topic = graphene.Field(TopicNode, id=graphene.NonNull(graphene.ID))
    all_topics = DjangoFilterConnectionField(TopicNode)


    @login_required
    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        return get_user_model().objects.get(id=from_global_id(id)[1])
    
    @login_required
    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()


    def resolve_topic(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Topic.objects.get(id=from_global_id(id)[1])

    def resolve_all_topics(self, info, **kwargs):
        return Topic.objects.all()