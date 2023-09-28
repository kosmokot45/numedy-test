import secrets
import string
from collections import defaultdict
import numpy as np

brands = ["Tefal", "Zagovor", "LG", "Dell", "Nokia", "Yandex"]

models = [
    f"model_{secrets.randbelow(10)}_{secrets.choice(string.ascii_lowercase)}"
    for model in range(100)]


def get_balance():
    items = np.random.default_rng().normal(loc=2.5, scale=1, size=100)
    numbers_dict = defaultdict(int)
    for item in items:
        number = int(item)
        if number < 0:
            number = 0
        elif number > 4:
            number = 4
        numbers_dict[number] += 1

    return [numbers_dict[i] for i in range(5)]


# a = get_balance()
# print(a)
# # x = np.arange(-3, 3, 0.001)

# # plot normal distribution with mean 0 and standard deviation 1
# # plt.plot(x, norm.pdf(x, 0, 1))
# # random.normalvariate(mu, sigma)


# # mu, sigma, n = 0., 1., 1000


# # def normal(x, mu, sigma):
# #     return (2.*np.pi*sigma**2.)**-.5 * np.exp(-.5 * (x-mu)**2. / sigma**2.)


# # x = np.random.normal(mu, sigma, n)
# # y = normal(x, mu, sigma)


# # plt.plot(x, y)
# # plt.show()


# # distr = random.gauss(100, 10, size=5)
# # print(distr.rvs())

# # lst = np.random.normal(20, .1, 5)
# # print(lst, sum(lst))
# # x = [el for el in range(5)]
# # plt.hist(a, bins=50)
# # plt.show()


# # labels = pd.date_range("11:00", "12:00", freq="5T").strftime("%H:%M")

# # fig, ax = plt.subplots()
# # n, bins, patches = ax.hist(np.random.default_rng().normal(
# #     loc=0.0, scale=.1, size=100), bins=5)
# # ax.set_xticks(bins, labels=patches)
# # plt.bar_label(patches)

# # plt.xticks(rotation=45)
# # plt.show()

# # def random_partition(n, sum):
# #     indices = [-1] + sorted(random.sample(range(sum - 1), n - 1)) + [sum - 1]
# #     return [indices[i + 1] - indices[i] for i in range(n)]


# # a = random_partition(12, 400)
# # print(a, sum(a))

# # plt.hist(a, bins=10)
# # plt.show()

# lst = [round(np.random.normal(20, .5)) for x in range(5)]
# print(lst, sum(lst))
# plt.hist(a, bins=5)
# plt.show()
