print("=== MONITORING SERVEUR ===")
cpu_usage = 87.5
ram_go = 16
ram_utilisee_go = 14
en_ligne = True
ram_pourcentage = ram_utilisee_go / ram_go * 100
if cpu_usage >= 90 :
    print(f"CPU : CRITIQUE — {cpu_usage}%")
elif cpu_usage >= 75 :
    print(f"CPU : AVERTISSEMENT — {cpu_usage}%")
else: 
    print(f"CPU : Normal — {cpu_usage}%")
          

if ram_pourcentage >= 90 :
    print(f"RAM : CRITIQUE — {ram_pourcentage}%")
elif ram_pourcentage >= 70 : 
    print(f"RAM : AVERTISSEMENT — {ram_pourcentage}%")
else: 
    print(f"ram : {ram_pourcentage}%")


if en_ligne : 
    print ("Service : Service EN LIGNE")
else:
    print ("Service : Service HORS LIGNE")