from rest_framework.routers import DefaultRouter

from chats.views import ConversationViewSet, MessageViewSet

router = DefaultRouter()

router.register('conversation', ConversationViewSet)
router.register('message', MessageViewSet)


urlpatterns = router.urls
