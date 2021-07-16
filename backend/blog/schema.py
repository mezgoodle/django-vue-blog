from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from .models import Profile, Tag, Post

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class AuthorType(DjangoObjectType):
    class Meta:
        model = Profile

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    @classmethod
    def resolve_all_posts(root, info):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    @classmethod
    def resolve_author_by_username(root, info, username):
        return Profile.objects.select_related("user").get(
            user__username=username
        )

    @classmethod
    def resolve_post_by_slug(root, info, slug):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    @classmethod
    def resolve_posts_by_author(root, info, username):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    @classmethod
    def resolve_posts_by_tag(root, info, tag):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

schema = graphene.Schema(query=Query)
