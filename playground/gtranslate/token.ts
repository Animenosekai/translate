const t = (a, b, c) => {
    null == a && (a = ec);
    ec = void 0;
    if (null == a) {
        var d = 96;
        c ? (a = [c],
            d |= 512) : a = [];
        b && (d = d & -2095105 | (b & 1023) << 11)
    } else {
        if (!Array.isArray(a))
            throw Error();
        d = (0,
            _.ub)(a);
        if (d & 64)
            return _.hc && delete a[_.hc],
                a;
        d |= 64;
        if (c && (d |= 512,
            c !== a[0]))
            throw Error();
        a: {
            c = a;
            var e = c.length;
            if (e) {
                var f = e - 1
                    , g = c[f];
                if (_.Hb(g)) {
                    d |= 256;
                    b = +!!(d & 512) - 1;
                    e = f - b;
                    1024 <= e && (Naa(c, b, g),
                        e = 1023);
                    d = d & -2095105 | (e & 1023) << 11;
                    break a
                }
            }
            b && (g = +!!(d & 512) - 1,
                b = Math.max(b, e - g),
                1024 < b && (Naa(c, g, {}),
                    d |= 256,
                    b = 1023),
                d = d & -2095105 | (b & 1023) << 11)
        }
    }
    (0,
        _.vb)(a, d);
    return a
}

/**
 * Copies the prototype of `obj2` into `obj1`
 * 
 * @param obj1 The object to copy to
 * @param obj2 The object to copy from
 */
const copyPrototype = (obj1, obj2) => {
    obj1.prototype = Object.create(obj2.prototype);
    obj1.prototype.constructor = obj1;
    if (Object.setPrototypeOf) {
        Object.setPrototypeOf(obj1, obj2);
    }
    else {
        for (var attr in obj2) {
            if ("prototype" != attr) {
                // @ts-ignore
                if (Object.defineProperties) {
                    var d = Object.getOwnPropertyDescriptor(obj2, attr);
                    if (d) {
                        Object.defineProperty(obj1, attr, d)
                    }
                } else {
                    obj1[attr] = obj2[attr];
                }
            }
        }
    }
    obj1.Fd = obj2.prototype
}

const EM = function (a) {
    this.va = t(a)
}

const temp = (a, b, c) => {
    this.va = t(a, b, c)
}

copyPrototype(EM, temp);

const I = (a, b, c) => {
    if (c === undefined) {
        return Fc(kj(a, b), "")
    }
    return Fc(kj(a, b), c)
}

EM.prototype.Qa = () => {
    return I(this, 16)
}
EM.prototype.iz = () => {
    return _.G(this, _.DM, 63)
}
EM.kb = [26, 80];

const ZM = (a, b?: {
    Cz?: boolean,
    uG?: boolean,
    nJ?: boolean,
}) => {
    const Cz = b?.Cz ? b.Cz : false
    const uG = b?.uG ? b.uG : false
    const nJ = b?.nJ ? b.nJ : false

    c = new EM;
    c = _.zj(c, 65, 2);
    c = _.yj(c, 50, a.hb);

    if (nJ) {
        var f = _.WM(_.VM(_.GM(_.FM(c, a.Ra), a.Ya), a.xc), a.j);
        var g = new MM;
        g = _.wj(g, 1, a.Ja);
        _.H(f, MM, 70, g)
    } else {
        _.WM(_.VM(_.GM(_.FM(c, a.oa), a.Fa), a.qa), a.i);
    }

    if (uG) {
        _.zj(c, 53, a.g);
    }

    if (Cz) {
        _.zj(c, 32, e ? a.Ma : a.W ? 3 : a.s);
    }

    if (a.ya != 0) {
        Cz = new _.LM;
        a = _.zj(Cz, 1, a.ya);
        _.H(c, _.LM, 121, a);
    }

    a = _.SF();

    _.zj(c, 81, a);

    return c
}


const generator = (a, b, source_text: string, d, e, obj: GObject) => {
    var generatorContext = this;
    // const case1 = () => {
    //     source_text = source_text.trim();
    //     // `generatorContext.i` is the limit of characters allowed
    //     if (source_text.length > generatorContext.i) {
    //         _.RF("translateText query over character limit. Length: " + source_text.length + " Limit: " + generatorContext.i);
    //         source_text = source_text.substring(0, generatorContext.i).trim();
    //     }
    //     var u = new Eq;
    //     u = _.Id(u, 2, a);
    //     u = _.Id(u, 3, b);
    //     g = _.Dc(u, 4, _.Ob(d), false).Tb(source_text);
    //     e && (u = new _.DX,
    //         u = _.zj(u, 1, e),
    //         _.H(g, _.DX, 5, u));
    //     u = new _.Oq;
    //     u = _.H(u, _.Eq, 1, g);
    //     var v = generatorContext.g;
    //     var w = new DZ;
    //     v = v.g;
    //     w = _.Aj(w, 1, Zfb(v.W ? 3 : v.s));
    //     k = _.H(u, DZ, 2, w);
    //     _.Rf(r, 2, 3);
    //     m = Date.now();
    //     return _.C(r, generatorContext.j.g(_.Xja.qb(k)), 5);
    // }

    const case3 = () => {
        obj.Fa = [obj.j];
        obj.V = 0;
        obj.s = 0;
        const u = generatorContext.g;
        const w = ZM(u.g, {
            Cz: true,
            uG: true
        });
        w = _.zj(w, 31, 1);
        _.bN(u, w);
        generatorContext.g.g.g = 0;
        _.Wf(r, 0);
    }

    const case5 = () => {

    }
}


function(r) {
    switch (r.g) {
        case 1:
            c = c.trim();
            c.length > f.i && (_.RF("translateText query over character limit. Length: " + c.length + " Limit: " + f.i),
                c = c.substring(0, f.i).trim());
            var u = new _.Eq;
            u = _.Id(u, 2, a);
            u = _.Id(u, 3, b);
            g = _.Dc(u, 4, _.Ob(d), false).Tb(c);
            e && (u = new _.DX,
                u = _.zj(u, 1, e),
                _.H(g, _.DX, 5, u));
            u = new _.Oq;
            u = _.H(u, _.Eq, 1, g);
            var v = f.g;
            var w = new DZ;
            v = v.g;
            w = _.Aj(w, 1, Zfb(v.W ? 3 : v.s));
            k = _.H(u, DZ, 2, w);
            _.Rf(r, 2, 3);
            m = Date.now();
            return _.C(r, f.j.g(_.Xja.qb(k)), 5);
        case 5:
            n = r.i;
            f.g.g.qa = _.I(n, 3);
            u = f.g;
            w = {
                kp: Date.now() - m,
                a2: _.BC(n),
                S3: _.Nq(n)
            };
            w = undefined === w ? {} : w;
            v = w.kp;
            var x = w.a2
                , E = w.S3;
            w = _.aN(u, 338);
            if (v) {
                var D = new _.iO;
                v = _.wj(D, 1, v);
                _.H(w, _.iO, 82, v)
            }
            if (x) {
                v = new HZ;
                D = _.Lq(x);
                D = _.A(D);
                for (var K = D.next(); !K.done; K = D.next())
                    K = $fb(K.value),
                        _.hj(v, 1, FZ, K);
                (x = _.AC(x)) && (_.kj(w, 16) !== x.Qa() || _.kj(w, 1) !== _.I(x, 3) || _.kj(w, 52).trim() !== x.Ua()) && _.vj(v, 2, true);
                if (E) {
                    x = [];
                    E = _.A(E);
                    for (D = E.next(); !D.done; D = E.next())
                        if (K = _.Lq(D.value),
                            0 !== K.length) {
                            D = new GZ;
                            K = _.A(K);
                            for (var T = K.next(); !T.done; T = K.next())
                                T = $fb(T.value),
                                    _.hj(D, 1, FZ, T);
                            x.push(D)
                        }
                    _.gj(v, 3, x)
                }
                _.H(w, HZ, 115, v)
            }
            _.bN(u, w);
            if (u = !_.Pg(c))
                a: {
                    if (_.dj(n, _.Kq, 2))
                        for (u = 0; u < _.Lq(_.BC(n)).length; u++)
                            if (w = _.Lq(_.BC(n))[u],
                                !_.Pg(_.dJ(w))) {
                                u = false;
                                break a
                            }
                    u = true
                }
            u && (u = f.g,
                w = c,
                v = _.I(n, 3),
                E = _.fN(u, 166),
                _.WM(_.VM(_.GM(_.FM(E, a), b), v), w),
                _.YM(u.i, 166),
                _.bN(u, E));
            return r.return(n);
        case 3:
            _.Vf(r);
            u = f.g;
            w = _.ZM(u.g, {
                Cz: true,
                uG: true
            });
            w = _.zj(w, 31, 1);
            _.bN(u, w);
            f.g.g.g = 0;
            _.Wf(r, 0);
            break;
        case 2:
            throw q = _.Uf(r),
            _.RF("Error getting translation", q),
            q;
    }
}