var Main = {
    data: function () {
        return {
            columns8: [
                {
                    "title": "Name",
                    "key": "name",
                    "fixed": "left",
                    "width": 200
                }, {
                    "title": "Show",
                    "key": "show",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Weak",
                    "key": "weak",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Signin",
                    "key": "signin",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Click",
                    "key": "click",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Active",
                    "key": "active",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "7, retained",
                    "key": "day7",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "30, retained",
                    "key": "day30",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "The next day left",
                    "key": "tomorrow",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Day Active",
                    "key": "day",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Week Active",
                    "key": "week",
                    "width": 150,
                    "sortable": true
                }, {
                    "title": "Month Active",
                    "key": "month",
                    "width": 150,
                    "sortable": true
                }],
            data7: [{
                "name": "Name1",
                "fav": 0,
                "show": 7302,
                "weak": 5627,
                "signin": 1563,
                "click": 4254,
                "active": 1438,
                "day7": 274,
                "day30": 285,
                "tomorrow": 1727,
                "day": 558,
                "week": 4440,
                "month": 5610
            }, {
                "name": "Name2",
                "fav": 0,
                "show": 4720,
                "weak": 4086,
                "signin": 3792,
                "click": 8690,
                "active": 8470,
                "day7": 8172,
                "day30": 5197,
                "tomorrow": 1684,
                "day": 2593,
                "week": 2507,
                "month": 1537
            }, {
                "name": "Name3",
                "fav": 0,
                "show": 7181,
                "weak": 8007,
                "signin": 8477,
                "click": 1879,
                "active": 16,
                "day7": 2249,
                "day30": 3450,
                "tomorrow": 377,
                "day": 1561,
                "week": 3219,
                "month": 1588
            }, {
                "name": "Name4",
                "fav": 0,
                "show": 9911,
                "weak": 8976,
                "signin": 8807,
                "click": 8050,
                "active": 7668,
                "day7": 1547,
                "day30": 2357,
                "tomorrow": 7278,
                "day": 5309,
                "week": 1655,
                "month": 9043
            }, {
                "name": "Name5",
                "fav": 0,
                "show": 934,
                "weak": 1394,
                "signin": 6463,
                "click": 5278,
                "active": 9256,
                "day7": 209,
                "day30": 3563,
                "tomorrow": 8285,
                "day": 1230,
                "week": 4840,
                "month": 9908
            }, {
                "name": "Name6",
                "fav": 0,
                "show": 6856,
                "weak": 1608,
                "signin": 457,
                "click": 4949,
                "active": 2909,
                "day7": 4525,
                "day30": 6171,
                "tomorrow": 1920,
                "day": 1966,
                "week": 904,
                "month": 6851
            }, {
                "name": "Name7",
                "fav": 0,
                "show": 5107,
                "weak": 6407,
                "signin": 4166,
                "click": 7970,
                "active": 1002,
                "day7": 8701,
                "day30": 9040,
                "tomorrow": 7632,
                "day": 4061,
                "week": 4359,
                "month": 3676
            }]
        }
    }
};

// var Component = Vue.extend(Main)
// new Component().$mount('#app')

// Vue.component('my-component', {
//     props: ['message'],
//     template: '<div>{{ message }}</div>'
// });

// Vue.component('i-table', Main)
//
// new Vue({
//   el: '#app'
// });

var Component = Vue.extend(Main);

Vue.component('i-table',Component)
// new Component().$mount('#app')
new Vue({
  el: '#app'
});





