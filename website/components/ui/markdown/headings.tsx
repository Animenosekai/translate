import { headingLink } from "utils/heading"

export const Heading1 = ({ node, level, children, key, ...props }) => {
    return <section id={headingLink(children.toString())}>
        <div className="flex flex-col gap-2 mt-8 mb-6">
            <h1 className="text-2xl font-bold">{children}</h1>
            <hr />
        </div>
    </section>
}

export const Heading2 = ({ node, level, children, key, ...props }) => {
    return <section id={headingLink(children.toString())}>
        <h2 className="text-xl font-semibold mt-6 mb-4">{children}</h2>
    </section>
}

export const Heading3 = ({ node, level, children, key, ...props }) => {
    return <section id={headingLink(children.toString())}>
        <h3 className="text-lg font-medium mt-4 mb-2">{children}</h3>
    </section>
}

export const Heading4 = ({ node, level, children, key, ...props }) => {
    return <section id={headingLink(children.toString())}>
        <h4 className="text-base font-medium mt-3 mb-1">{children}</h4>
    </section>
}

export const Heading5 = ({ node, level, children, key, ...props }) => {
    return <section id={headingLink(children.toString())}>
        <h5 className="text-base font-normal mt-3 mb-1">{children}</h5>
    </section>
}
