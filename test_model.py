from model.modello import Model
def main():
    model = Model()

    c =3
    b=7

    print(f"Costruisco il grafo con c = {c,b}...")

    model.build_graph(c,b)

    n_nodi, n_archi = model.get_stats()

    print(f" il grafo creato contiene {n_nodi} nodes e {n_archi} edges")
    k=model.top_5()
    for i in k:
        print(f"il nodo {i[0]} ha archi {i[1]}ha peso {i[2]}")

    """s = model.top3()

    print(f"{s}")
    n, path=model.connesse()
    print("aaaaaaaa"+str(n))
    for k in path:
        print(k)"""



if __name__ == "__main__":
    main()