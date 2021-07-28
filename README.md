# Kort Information
Denna kod skrevs inte i hopp om att skada Kronofogden eller liknande. 
Koden är till för andra unga programmerare som vill utveckla sitt sinne inom programmeringen.

# Exempel
```
Vänligen fyll i sökord som du vill söka efter.
Om du är ute efter flera olika artiklar separera varje sökord med ', '.
Sökord: vapen
Vänligen fyll i det högsta betalbara priset du har tänkt dig.
Om du inte vill filtrera artiklar efter pris kan du skriva 0 eller trycka på Enter tangenten.
Pris: 0
| Sökord   | Id     | Artikel                 | Högsta Bud   |
|----------+--------+-------------------------+--------------|
| vapen    | F48872 | Kulgevär Heym           | 5000 SEK     |
| vapen    | F49289 | Revolver Smith & Wesson | 4000 SEK     |
| vapen    | F49291 | Pistol Wahlter          | 5000 SEK     |
| vapen    | F49360 | Kulgevär Savage         | 1000 SEK     |
| vapen    | F48312 | Luftpistol Daisy 5501   | 600 SEK      |
```

# To-do
- [x] Implement a check for amount of children before indexing.
- [x] Make the process work on multiple pages, as of now it only scans one page at a time. (There is no need to do this one)
- [x] Make the process of scanning multiple pages multi-threaded, once it's supported. (There is no need to do this one)
- [x] Add a maximum price so that the user can filter out prices that doesn't fit him/her.
- [ ] Make the process multi-threaded to improve speed when searching for multiple keywords.
