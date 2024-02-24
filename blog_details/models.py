from django.db import models
from blog.models import postForm

# Bạn có thể thực hiện các thay đổi hoặc mở rộng model nếu cần
class blog_Detail(postForm):
    # Các trường khác của model
    description = models.TextField()

    def __str__(self):
        return self.title
