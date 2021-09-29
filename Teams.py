teams = ['Boca', 'River', 'Independiente', 'Racing', 'San lorenzo', 'Velez', 'Estudiantes', 'Gimnasia']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + "vs" + away_team)

