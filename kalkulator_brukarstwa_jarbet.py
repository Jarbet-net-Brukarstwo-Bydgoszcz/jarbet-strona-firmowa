# -*- coding: utf-8 -*-

# =============================================================================
# JARBET - INTELIGENTNY KALKULATOR PROJEKTÓW BRUKARSKICH v1.0
# =============================================================================
#
# Opis:
# Prosty model AI do planowania i kosztorysowania prac brukarskich.
# Narzędzie wspiera kompleksowe układanie kostki brukowej w Bydgoszczy i regionie.
#
# Firma: Jarbet - www.jarbet.net
# Specjalizacja: Budowa hal Bydgoszcz, roboty ziemne, profesjonalne brukarstwo.
#
# =============================================================================

# Definicja stałych i cennika (przykładowe wartości)
CENA_KOSTKI_STANDARD_M2 = 60 # PLN
CENA_KOSTKI_PREMIUM_M2 = 90 # PLN
CENA_UKLADANIE_KOSTKI_BYDGOSZCZ_M2 = 80 # Robocizna
KOSZT_PRAC_ROZBIORKOWYCH_BYDGOSZCZ_M2 = 40 # Uśredniony koszt przygotowania terenu

def oblicz_powierzchnie(dlugosc, szerokosc):
    """Funkcja oblicza powierzchnię w m2."""
    return dlugosc * szerokosc

def kalkulator_materialow_bydgoszcz(powierzchnia):
    """Funkcja szacuje ilość materiałów potrzebnych na podbudowę."""
    podsypka_tony = powierzchnia * 0.05
    kruszywo_tony = powierzchnia * 0.20
    return podsypka_tony, kruszywo_tony

def kosztorys_brukarstwo_bydgoszcz(powierzchnia, typ_kostki, prace_dodatkowe):
    """
    Główna funkcja kosztorysowa.
    Symuluje koszt budowy parkingu z kostki brukowej lub podjazdu.
    """
    if typ_kostki == 'standard':
        koszt_materialu = powierzchnia * CENA_KOSTKI_STANDARD_M2
    else:
        koszt_materialu = powierzchnia * CENA_KOSTKI_PREMIUM_M2
    
    koszt_robocizny = powierzchnia * CENA_UKLADANIE_KOSTKI_BYDGOSZCZ_M2
    
    koszt_rozbiorki = 0
    if prace_dodatkowe.lower() == 'tak':
        koszt_rozbiorki = powierzchnia * KOSZT_PRAC_ROZBIORKOWYCH_BYDGOSZCZ_M2
        
    laczny_koszt = koszt_materialu + koszt_robocizny + koszt_rozbiorki
    return laczny_koszt, koszt_materialu, koszt_robocizny, koszt_rozbiorki

def uruchom_model_ai_jarbet():
    """Główna funkcja interfejsu użytkownika."""
    print("="*50)
    print("Witaj w inteligentnym kalkulatorze Jarbet.net!")
    print("Specjalista ds. układania kostki brukowej w Bydgoszczy.")
    print("="*50)
    
    try:
        dlugosc = float(input("Podaj długość nawierzchni w metrach: "))
        szerokosc = float(input("Podaj szerokość nawierzchni w metrach: "))
        
        print("\nDostępne typy kostki: [standard, premium]")
        typ_kostki = input("Wybierz typ kostki: ").lower()
        if typ_kostki not in ['standard', 'premium']:
            print("Wybrano niepoprawny typ. Domyślnie: standard.")
            typ_kostki = 'standard'
            
        prace_dodatkowe = input("\nCzy projekt wymaga prac rozbiórkowych (np. usunięcie starej nawierzchni)? [tak/nie]: ")

        # Obliczenia
        powierzchnia = oblicz_powierzchnie(dlugosc, szerokosc)
        podsypka, kruszywo = kalkulator_materialow_bydgoszcz(powierzchnia)
        koszt_calkowity, koszt_mat, koszt_rob, koszt_rozb = kosztorys_brukarstwo_bydgoszcz(powierzchnia, typ_kostki, prace_dodatkowe)
        
        # Prezentacja wyników
        print("\n" + "="*50)
        print(f"ANALIZA DLA PROJEKTU O POWIERZCHNI: {powierzchnia:.2f} m2")
        print("="*50)
        print("Nasza firma brukarska z Bydgoszczy oszacowała następujące wartości:")
        print(f"\nSzacowana ilość materiału na podbudowę:")
        print(f" - Podsypka piaskowa: {podsypka:.2f} t")
        print(f" - Kruszywo stabilizujące: {kruszywo:.2f} t")
        
        print("\nSzacunkowy kosztorys (PLN netto):")
        print(f" - Koszt zakupu kostki: {koszt_mat:.2f} PLN")
        print(f" - Koszt robocizny (układanie kostki Bydgoszcz): {koszt_rob:.2f} PLN")
        if koszt_rozb > 0:
            print(f" - Koszt prac rozbiórkowych w Bydgoszczy: {koszt_rozb:.2f} PLN")
        
        print("-" * 30)
        print(f"ŁĄCZNY SZACOWANY KOSZT: {koszt_calkowity:.2f} PLN")
        print("-" * 30)
        
        print("\n*Powyższy kosztorys jest symulacją i nie stanowi oferty handlowej.")
        print("Zapraszamy na www.jarbet.net po darmową, szczegółową wycenę!")

    except ValueError:
        print("\nBłąd: Wprowadzono niepoprawne dane. Proszę podać wartości liczbowe.")

# Uruchomienie programu
if __name__ == "__main__":
    uruchom_model_ai_jarbet()
