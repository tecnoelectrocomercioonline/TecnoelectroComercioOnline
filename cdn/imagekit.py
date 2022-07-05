from imagekitio import ImageKit
imagekit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY,
    public_key=IMAGEKIT_PUBLIC_KEY,
    url_endpoint=IMAGEKIT_URL_ENDPOINT
)
# 1. Using Image path and image hostname or endpoint
imagekit_url = imagekit.url({
    "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/tecnoelectrocr/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
}
)

