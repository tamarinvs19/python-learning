trs = $("tr.ng-scope:not(.greenRow):not(.redRow)")
// days = $(trs[i]).children("[ng-repeat='day in listDates']")
// lessons = $(days[0]).children('div').children('div')
// scores = $(lessons[0]).children('div').children('div')
// number = $($($($(scores[0]).children('div')[0]).children('span')[0]).children('span')[0]).children('span')[0].innerHTML
// k = $(scores[0]).children('div')[0].style['background-color']

function scores(i) {
    days = $(trs[i]).children("[ng-repeat='day in listDates']")
    res = []
    for (var j=0; j<days.length; j++) {
        ls = $(days[j]).children('div').children('div')
        //console.log(days[j], ls)
        for (var n=0; n<ls.length; n++) {
            ss = $(ls[n]).children('div').children('div')
            //console.log('ss', ss, ss[0])
            for (var m=0; m<ss.length; m++) {
                color = $(ss[m]).children('div')[0].style['background-color'].toString().slice(5,-6)
                numbers = $($($(ss[m]).children('div')[0]).children('span')[0]).children('span')
                //console.log('numbers', numbers)
                for (var o=0; o<numbers.length; o++) {
                    number = $(numbers[o]).children('span')[0]
                    //console.log('number', number)
                    if (number != undefined) {
                        number = number.innerHTML
                        console.log(number, color)
                        if (number != "") {
                            res.push([number, color])
                        }
                    }
                }
            }
        }
    }
    return res
}
//console.log(scores(10))


function get_koef() {
    xs = $("[ng-if='listPart.length']").children('span')
    for (var i=0;i<xs.length;i++) {
        d = $(xs[i]).children('div')[0]
        t = xs[i].innerText.slice(3,-1)
        k = prompt(t)
        //console.log(d)
        xs[i] = [d.style['backgroundColor'].slice(4, -5), t, k]
    }
    return xs
}
console.log(get_koef())

ks = {…}
​
0: Array(3) [ "56, 112", "вычислит. раб., ", "1" ]
​
1: Array(3) [ "255, 223,", "Географический диктант, ", "1.25" ]
​
2: Array(3) [ "229, 122,", "Диагностическая, ", "0.5" ]
​
3: Array(3) [ "3, 9", "Диктант, ", "2" ]
​
4: Array(3) [ "229, 122,", "Дом. задание, ", "0.5" ]
​
5: Array(3) [ "178, 255,", "Зачет , ", "2.75" ]
​
6: Array(3) [ "7, 111,", "Зачет по карте, ", "1" ]
​
7: Array(3) [ "255, 247,", "Зачет по содержанию, ", "1.5" ]
​
8: Array(3) [ "255, 247,", "Зачет по теме, ", "1.75" ]
​
9: Array(3) [ "0, 150,", "Зачет по теме (гуманитарный) , ", "1.75" ]
​
10: Array(3) [ "255, 247,", "Конспект, ", "0.75" ]
​
11: Array(3) [ "102, 0,", "Контрольная работа, ", "2" ]
​
12: Array(3) [ "229, 122,", "Лабораторн.раб., ", "0.75" ]
​
13: Array(3) [ "156, 229,", "Опрос, ", "1" ]
​
14: Array(3) [ "104, 218,", "Опрос устный, ", "1" ]
​
15: Array(3) [ "235, 4", "Орфогр.дикт., ", "1.5" ]
​
16: Array(3) [ "255, 21", "Полугодовая к/р, ", "3" ]
​
17: Array(3) [ "0, 154", "Практическая, ", "1" ]
​
18: Array(3) [ "119, 255,", "Практическая по карте, ", "1" ]
​
19: Array(3) [ "211, 8,", "Проверочная раб, ", "1.75" ]
​
20: Array(3) [ "255, 247,", "Проверочная работа по теме раздела, ", "1.5" ]
​
21: Array(3) [ "255, 182,", "Пятиминутка (ПРОЕКТ), ", "2.5" ]
​
22: Array(3) [ "255, 247,", "работа на уроке, ", "1.35" ]
​
23: Array(3) [ "255, 6", "работа над ошиб, ", "0.5" ]
​
24: Array(3) [ "118, ", "Работа по д/з, ", "1.3" ]
​
25: Array(3) [ "177, 23", "Реш. задач в кл, ", "1" ]
​
26: Array(3) [ "130, 255,", "Реш.задач в классе, ", "1" ]
​
27: Array(3) [ "239, 111,", "Решение комп.задач дома, ", "1" ]
​
28: Array(3) [ "104, 255,", "Самостоятельная, ", "1.25" ]
​
29: Array(3) [ "3, 7,", "Сочинение, ", "2" ]
​
30: Array(3) [ "161, 122,", "Стихи наизусть C АНАЛИЗОМ, ", "1.5" ]
​
31: Array(3) [ "218, 8", "Тест, ", "1.25" ]
​
32: Array(3) [ "255, 247,", "Тест по ОБ", "1.25" ]
