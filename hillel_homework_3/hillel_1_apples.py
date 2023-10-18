children = int(input("Скільки всього школярів? -> "))
apples = int(input("Скілько всбього яблук? -> "))
ch_ap = apples // children
ap_ch = apples % children
if children > apples:
    print(children - ap_ch, "школярів залишились без яблук.")
    print("Яблук залишилось в корзинці:", 0)
else:
    print("Кожному школяру дісталося яблук:", ch_ap)
    print("Яблук залишилось в корзинці:", ap_ch)