from pyboxen import boxen

print(
    boxen(
        "Titles and subtitles!",
        title="Hello, [black on cyan] World [/]",
        subtitle="Cool subtitle goes here",
        subtitle_alignment="center",
        color="yellow",
        padding=1,
    )
)