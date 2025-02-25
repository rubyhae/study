let players = {
    boys : {
        Bergkamp: "Striker"
    }
}

let persons = players

```>> 레퍼런스 카운트는 올라가고 가비지는 등록되지 않는 상태```

plyaers = ["Son", "Park"]

let human = persons.boys

persons = "persons"
human = null

```boys는 레퍼런스 카운트가 0이 되어서 소멸대상이 된다.```