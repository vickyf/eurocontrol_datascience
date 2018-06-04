print(
    list(
        filter(lambda x: x%2 == 0,
               map(lambda x:x**2, range(11))
              )
    )
)