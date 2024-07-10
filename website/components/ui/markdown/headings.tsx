import { headingLink } from "utils/heading"
import { useHeadings } from "contexts/headings"

export const Heading1 = ({ node, level, children, key, ...props }) => {
    const { headings, setHeadings } = useHeadings();
    const id = headingLink(children.toString(), headings)
    setHeadings(headings)
    return <section id={id}>
        <a href={`#${id}`}>
            <div className="flex flex-col gap-2 mt-8 mb-6 hover:opacity-90 opacity-100 cursor-pointer">
                <h1 className="text-2xl font-bold">{children}</h1>
                <hr />
            </div>
        </a>
    </section>
}

export const Heading2 = ({ node, level, children, key, ...props }) => {
    const { headings, setHeadings } = useHeadings();
    const id = headingLink(children.toString(), headings)
    setHeadings(headings)
    return <section id={id}>
        <a href={`#${id}`}>
            <h2 className="text-xl font-semibold mt-6 mb-4">{children}</h2>
        </a>
    </section>
}

export const Heading3 = ({ node, level, children, key, ...props }) => {
    const { headings, setHeadings } = useHeadings();
    const id = headingLink(children.toString(), headings)
    setHeadings(headings)
    return <section id={id}>
        <a href={`#${id}`}>
            <h3 className="text-lg font-medium mt-4 mb-2">{children}</h3>
        </a>
    </section>
}

export const Heading4 = ({ node, level, children, key, ...props }) => {
    const { headings, setHeadings } = useHeadings();
    const id = headingLink(children.toString(), headings)
    setHeadings(headings)
    return <section id={id}>
        <a href={`#${id}`}>
            <h4 className="text-base font-medium mt-3 mb-1">{children}</h4>
        </a>
    </section>
}

export const Heading5 = ({ node, level, children, key, ...props }) => {
    const { headings, setHeadings } = useHeadings();
    const id = headingLink(children.toString(), headings)
    setHeadings(headings)
    return <section id={id}>
        <a href={`#${id}`}>
            <h5 className="text-base font-normal mt-3 mb-1">{children}</h5>
        </a>
    </section>
}
