$E.prototype.j({
    "j": {},
    "o": 2,
    "v": null,
    "H": false
})


const xya = function (a) {
    const newSet = new Set;

    for (let c of a) {
        newSet.add(c.getName())
        newSet.add(c.ua)
    }

    return (d) => {
        // d.ya("rpcids")
        const rpcids = d.j.o.j.rpcids // => "QShL0"
        if (!d) {
            return true
        }

        for (let char of rpcids) {
            if (newSet.has(char)) { // if e in set
                return true
            }
        }

        return false
    }
}

const this_H = xya("...TRANSLATEPY__UNKNOWN_VALUE") // what do I need to put ?

$E.prototype.j = function (a) {
    var b = ["[[[\"QShL0\",\"[\\\"fr\\\",\\\"en\\\",[\\\"Salut le monde, comment vas-tu\\\",\\\"Bonjour le monde, comment allez-vous\\\"]]\",null,\"generic\"]]]"]
    if (b && this_H(a)) {
        var c = this_N_jf(b)
            .then(
                (d) => {
                    a.na.set("X-Goog-BatchExecute-Bgr", d);
                    return a
                },
                () => a // rejection
            );
        return _.Xh(c)
    }
};

const ya = (a) => {
    return this.j.o.get(a)
}

const _B = (a) => {
    var newIterator = Symbol.iterator && a[Symbol.iterator];
    return newIterator ? newIterator.call(a) : {
        next: pe(a)
    }
}



const this_N_jf = function (a) {
    return H.promise.then(function () {
        return N_state_jf(a)
    })
}

const this_N_state_jf = function (a) {
    var currentDateTime = Date.now();
    if (this.j < currentDateTime) {
        return kF(this.service), this.service.jf(a);
    }
    var c = Eya(this.service);
    try {
        return this.o(a)
            .then((d) => { // fullfilled
                c.kf(0);
                _.A(c, 1, d);
                gF(c, Date.now() - currentDateTime);
                return c.od()
            }, () => { // rejected
                c.kf(2);
                gF(c, Date.now() - currentDateTime);
                return c.od()
            })
    } catch (d) {
        return c.kf(2), gF(c, Date.now() - currentDateTime), Promise.resolve(c.od())
    }
}


const a = {
    N: {
        "j": {
            "f.req": ["[[[\"QShL0\",\"[\\\"fr\\\",\\\"en\\\",[\\\"Salut le monde, comment vas-tu\\\",\\\"Bonjour le monde, comment allez-vous\\\"]]\",null,\"generic\"]]]"],
            "at": "AAaZcx0lrxcKw6kC7PCAN-wnkVpE:1657560161959"
        },
        "o": 2,
        "v": null,
        "H": false
    },
    Pt: "BEST_EFFORT",
    Va: true,
    Wa: 769763,
    fR: false,
    j: {
        "H": "",
        "ua": "",
        "v": "",
        "wa": null,
        "j": "/_/TranslateWebserverUi/data/batchexecute",
        "na": "",
        "N": false,
        "o": {
            "j": {
                'rpcids': 'QShL0',
                'source-path': '/',
                'f.sid': '-6597052306162989274',
                'bl': 'boq_translate-webserver_20220706.08_p0',
                'hl': 'en',
                'soc-app': '1',
                'soc-platform': '1',
                'soc-device': '1'
            },
            "o": 8,
            "v": null,
            "H": false
        }
    },
    kc: false,
    na: {
        "o": {},
        "j": [],
        "size": 0,
        "v": 0
    },
    v: "POST",
    wa: "...TRANSLATEPY__CONTAINS_CYCLIC_REFERENCE...",
    xc: 7,
    yb: -1
}