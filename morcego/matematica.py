from colorama import Fore, Style

def multiplos(nu, qua=None):
    try:
        nu2 = 1
        if qua:
            if isinstance(qua, int):
                if qua >= 0:
                    for i in range(qua):
                        total = nu * nu2
                        print(total, "é múltiplo de", nu, "e", nu2)
                        nu2 += 1
            else:
                print(Fore.RED + "O argumento 'qua' deve ser um inteiro." + Style.RESET_ALL)
        else:
            for i in range(5):
                total = nu * nu2
                print(total, "é múltiplo de", nu, "e", nu2)
                nu2 += 1

    except:
        print(Fore.RED + "NaN = Não é Número" + Style.RESET_ALL)
        