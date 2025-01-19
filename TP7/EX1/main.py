         #test
from conversion import dollars_to_dirhams, meters_to_kilometers

def main():
    dollars = 100  
    dirhams = dollars_to_dirhams(dollars)
    print(f"{dollars} USD équivalent à {dirhams:.2f} MAD.")

    meters = 1500  
    kilometers = meters_to_kilometers(meters)
    print(f"{meters} M équivalent à {kilometers:.2f} KM.")

if __name__ == "__main__":
    main()
