from PIL import Image

file_names = ["20231111_husky.jpg",
              "20240511_coastal.jpg",
              "20240511_sea.jpg",
              "20240905_storr_cliff.jpg"]

for img in file_names:
    in_img = Image.open(f'WanderingAnna/original_images/{img}')
    in_img.size  # (200, 374)

    if in_img.size == (4000, 3000):
        to_size = (1024, 768)

    if to_size:
        out_img = in_img.resize(to_size, Image.Resampling.LANCZOS)

    out_img.save(f'WanderingAnna/assets/{img}', quality=95, optimize=True)
