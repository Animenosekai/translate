// _.Br = function (a, b, c) {
//     a.remove(b);
//     0 < c.length && (a.j = null,
//         a.g.set(zr(a, b), _.ta(c)),
//         a.i += c.length)
// }

_.ia = function (a) {
    return a[a.length - 1]
}

var lfa = function (a) {
    0 === a.i.length && (a.i = a.g,
        a.i.reverse(),
        a.g = [])
}

_.mfa = function (a) {
    lfa(a);
    return _.ia(a.i)
}



// This seems to create the batchexecute header value
DDa.prototype.Oe = function (a) {
    var b = this;
    return _.F(function (c) {
        if (1 == c.g)
            return b.g ? c.Qb(2) : _.C(c, b.i(), 3);
        2 != c.g && (b.g = c.i);
        return c.return(b.g.Oe(a))
    })
}

/**
 * Generates the token for the request
 * Minified Location: function _.F at line 123
 * 
 * @param payload The payload for the request
 * @returns A promise for the request header value
 */
const generateToken = (payload: string) => {
    return promiseLogic(
        initPromise(
            initRequestObject(payload)
        )
    )
}

/**
 * Files found on
 * 
 * https://www.gstatic.com/_/mss/boq-translate/_/js/k=boq-translate.TranslateWebserverUi.en.tMZedlnc7vY.es5.O/am=r1gwzMgGC4E/d=1/excm=_b,_tp,mainview/ed=1/dg=0/wt=2/ujg=1/rs=ANkVxDlPnLw1tT_kFerG7pPenWMBrSXJ5w/m=_b,_tp
 */

/**
 * An object inside the `RequestObject`
 */
interface GObject {
    qa: boolean,
    W?: any,
    i: any,
    g: number,
    s: number,
    V: number,
    Fa?: any,
    /** Probably the return value ? */
    j: {
        /** Return value when successull */
        return?: any,
        /** Error value when errored out */
        oF?: Error,
        /** Flag to indicate that there is an error */
        zG?: boolean
    } | null,
    /**
     * Sets the value of `i` in the object
     * 
     * @param val The value for `i`
     */
    oa: (val) => void,
    /**
     * Sets the value of `j` and copies `s` into `g`
     * 
     * @param val The value for `j.return`
     */
    return: (val) => void,
    /**
     * Sets the value of `g` in the object
     * 
     * @param val The value for `g`
     */
    Qb: (val) => void
}

/**
 * This keeps all of the information for the request
 */
interface RequestObject {
    g: GObject,
    i: string
}

/**
 * Creates a request object
 * Minified Location: function yca at line 120
 * 
 * @param payload The payload for the batchexecute request
 * @returns The request object
 */
const initRequestObject = (payload: string): RequestObject => {
    return {
        g: {
            qa: false,
            W: null,
            i: undefined,
            g: 1,
            s: 0,
            V: 0,
            Fa: null,
            j: null,
            oa: (val) => {
                this.i = val
            },
            return: (val) => {
                this.j = {
                    return: val
                };
                this.g = this.s;
            },
            Qb: (val) => {
                this.g = val;
            }
        },
        i: payload
    }
}

/**
 * Flags the object as being processed
 * Minified Location: function Pf at line 118
 * 
 * @param obj The `RequestObject.g` object ("GObject")
 */
const flagAsProcessed = (obj: GObject) => {
    if (obj.qa) {
        throw new TypeError("`obj.qa` is already set to `true`");
    }
    obj.qa = true;
}

/**
 * Sets the return value when errored out
 * Minified Location: function Qf at line 118
 * 
 * @param obj The `RequestObject.g` object ("GObject")
 * @param err The error object
 */
const setError = (obj: GObject, err: Error) => {
    obj.j = {
        oF: err,
        zG: true // indicate that there is an error
    };
    obj.g = obj.V || obj.s
}

const Xf = (reqObj: RequestObject, returnFunc: (val) => any, returnValue, oa: (val) => void) => {
    try {
        // Sets the return values for `reqObj.g.W`
        var e = returnFunc.call(reqObj.g.W, returnValue);
        if (!(e instanceof Object)) {
            throw new TypeError("f`" + e);
        }
        if (!e.done) {
            reqObj.g.qa = false;
            return e;
        }
    } catch (error) {
        reqObj.g.W = null
        setError(reqObj.g, error)
        return Yf(reqObj)
    }
    reqObj.g.W = null;

    // Sets `i` for `reqObj.g`
    oa.call(reqObj.g, e.value);
    return Yf(reqObj)
}

const Yf = (reqObj: RequestObject) => {
    while (reqObj.g.g) {
        try {
            var b = reqObj.i(reqObj.g);
            if (b) {
                reqObj.g.qa = false
                return {
                    value: b.value,
                    done: false
                }
            }
        } catch (c) {
            reqObj.g.i = undefined;
            setError(reqObj.g, c); // this should set `reqObj.g.g` for the loop to continue or stop
        }
    }
    reqObj.g.qa = false;
    if (reqObj.g.j) {
        const jCopy = reqObj.g.j;
        reqObj.g.j = null;
        if (jCopy.zG) {
            throw jCopy.oF;
        }
        return {
            value: jCopy.return,
            done: true
        }
    }
    return {
        value: undefined,
        done: true
    }
}

const zca = (reqObj: RequestObject, returnVal) => {
    flagAsProcessed(reqObj.g);
    if (reqObj.g.W) {
        let returnFunction;
        if ("return" in reqObj.g.W) {
            returnFunction = reqObj.g.W["return"]
        } else {
            returnFunction = (val) => {
                return {
                    value: val,
                    done: true
                }
            }
        }
        return Xf(reqObj, returnFunction, returnVal, reqObj.g.return)
    }
    reqObj.g.return(returnVal);
    return Yf(reqObj)
}

/**
 * Initialize the Promise with the adequate functions to handle its lifecycles
 * Minified Location: function Aca at line 122
 * 
 * @param reqObj The request object
 */
const initPromise = (reqObj: RequestObject) => {
    return {
        next: (value) => {
            flagAsProcessed(reqObj.g);
            if (reqObj.g.W) {
                return Xf(reqObj, reqObj.g.W.next, value, reqObj.g.oa)
            } else {
                reqObj.g.oa(value); // sets `i`
                return Yf(reqObj)
            }
        },
        throw: (value) => {
            flagAsProcessed(reqObj.g);
            if (reqObj.g.W) {
                return Xf(reqObj, reqObj.g.W.throw, value, reqObj.g.oa)
            } else {
                setError(reqObj.g, value);
                return Yf(reqObj)
            }
        },
        return: function (b) {
            return zca(reqObj, b)
        },
        [Symbol.iterator]: () => {
            return this
        }
    }
}


/**
 * Creates a new `Promise` object
 * 
 * Minified Location: function Bca at line 122
 * 
 * @param resolve When the value is being resolved (done)
 */
const promiseLogic = (a) => {
    /**
     * Handles the Promise logic
     * 
     * @param resolve When the value is being resolved (done)
     * @param reject When the promise rejected the promise (errored out)
     */
    const executor = (
        resolve: (value: any) => void,
        reject: (reason?: any) => void
    ) => {
        /**
         * Solves the Promise (handles a step in the Promise cycle)
         * 
         * @param promise The promise to handle
         */
        const resolver = (promise) => {
            if (promise.done) {
                resolve(promise.value) // calling the successfull handler
            } else {
                Promise
                    .resolve(promise.value)
                    .then(a.next, a.throw)
                    .then(resolver, reject) // process the next step
            }
        }
        resolver(a.next())
    }
    return new Promise(executor)
}
