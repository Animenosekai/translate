export const Table = ({ node, children, key, ...props }) => {
    return <table className="w-max max-w-full overflow-auto block">{children}</table>
}

export const TableHead = ({ node, children, key, ...props }) => {
    return <thead>{children}</thead>
}

export const TableR = ({ node, isHeader, children, key, ...props }) => {
    return <tr className="border-t-[1px] even:bg-[#f6f8fa]">{children}</tr>
}

export const TableH = ({ node, style, isHeader, children, key, ...props }) => {
    return <th className="py-[6px] px-[13px] border-[1px]">{children}</th>
}

export const TableD = ({ node, style, isHeader, children, key, ...props }) => {
    return <td className="py-[6px] px-[13px] border-[1px]">{children}</td>
}