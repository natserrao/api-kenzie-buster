from django.db import models


class RatingMovie(models.TextChoices):
    RATED_G = "G", ("General audiences")
    PG = "PG", ("Parental suggested")
    PG_13 = "PG-13", ("Parents cautioned")
    RATED_R = "R", ("Restricted")
    NC_17 = "NC-17", ("Adults Only")


class Movie(models.Model):
    title = models.CharField(max_length=127, blank=False)
    duration = models.CharField(max_length=10, blank=True, null=True)
    rating = models.CharField(
        max_length=20,
        choices=RatingMovie.choices,
        default=RatingMovie.RATED_G,
        blank=True,
    )
    synopsis = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    orders = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="ordered_movies",
    )

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_movie_order",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order",
    )

    buyed_at = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)

    def __repr__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.price}>"
