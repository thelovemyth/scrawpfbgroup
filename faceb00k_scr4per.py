from facebook_scraper import get_posts
from datetime import datetime, timedelta

# Cấu hình nhóm Facebook
GROUP_ID = "620662156508971"  # ID của nhóm Facebook
SINCE_TIME = datetime.now() - timedelta(days=1)  # Lấy bài viết trong 24 giờ qua

try:
    # Lấy bài viết từ nhóm
    print(f"Đang lấy bài viết từ nhóm {GROUP_ID}...")
    for post in get_posts(group=GROUP_ID, pages=10, options={"allow_extra_requests": False}):
        # Kiểm tra thời gian bài viết
        post_time = post.get("time")
        if post_time and post_time >= SINCE_TIME:
            post_text = post.get("text", "Không có nội dung")
            post_link = post.get("post_url", "Không có link")

            # In thông tin bài viết
            print(f"Thời gian: {post_time}")
            print(f"Nội dung: {post_text}")
            print(f"Link: {post_link}")
            print("-" * 80)
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
