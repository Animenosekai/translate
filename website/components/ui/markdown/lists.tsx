export const OrderedList = ({ node, index, depth, ordered, className, children, key, ...props }) => {
    return <ol className="pl-8 list-disc">{children}</ol>
}

export const UnorderedList = ({ node, index, depth, ordered, className, children, key, ...props }) => {
    return <ul className="pl-8 list-disc">{children}</ul>
}

export const ListItem = ({ node, index, ordered, checked, className, children, key, ...props }) => {
    return <li className="list-item">{children}</li>
}