(lambda A: str(print(f'2. feladat\n{". nap rendszám: ".join([[x[0],x[2]] for x in A if x[5]=="0"][-1])}\n3. feladat'))+str(print(f'Forgalom a(z) {(lambda n: (". napon:"+chr(0x0A)).join([n, chr(0x0A).join([" ".join([y[1],y[2],y[3],"ki" if y[5]=="0" else "be"]) for y in A if y[0] == n])]))(input("Nap: "))}\n4. feladat\nA hónap végén {abs(sum([sum([1 for y in A if (y[2]==x and y[5]=="1")])+sum([-1 for y in A if (y[2]==x and y[5]=="0")]) for x in list(set([x[2] for x in A]))]))} autót nem hoztak vissza.\n5. feladat\n{chr(0x0A).join([" ".join([x, str([int(y[4]) for y in A if y[2]==x][-1]-[int(y[4]) for y in A if y[2]==x][0]), "km"]) for x in sorted(list(set([x[2] for x in A])))])}\n6. feladat\nLeghosszabb út: {" km, személy: ".join(max([[str(max([e-s for s,e in zip([int(y[4]) for y in A if (y[3]==x and y[5]=="0")],[int(y[4]) for y in A if (y[3]==x and y[5]=="1")])])) if len([y for y in A if y[3]==x])>1 else 0, x] for x in sorted(list(set([x[3] for x in A])))],key=lambda x: int(x[0])))}\n7. feladat'))+str((lambda x: print("".join([f'{lst[3]}\t{lst[0]}.\t{lst[1]}\t{lst[4]} km\t' if lst[5]=="0" else f'{lst[0]}.\t{lst[1]}\t{lst[4]} km\n' for lst in A if lst[2]==x]), file=open(x+"_menetlevel.txt","w")))(input('Rendszám: ')))+str(print("Menetlevél kész.")))([x.strip().split() for x in open("autok.txt")])