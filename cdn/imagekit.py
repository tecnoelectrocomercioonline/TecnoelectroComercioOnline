from imagekitio import ImageKit
imagekit = ImageKit(
    private_key='private_LoyP/7BRnXZKci25YcGyUqV3Xkw=',
    public_key='public_ZYAWyTf3Z1mDntD50znHaHd5Y5Y=',
    url_endpoint='https://ik.imagekit.io/tecnoelectrocr'
)
# 1. Using Image path and image hostname or endpoint
imagekit_url = imagekit.url({
    "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
}
)

