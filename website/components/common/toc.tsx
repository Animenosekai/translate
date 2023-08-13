import { DocumentationElement } from "localizations/eng";
import Link from "next/link";
import classNames from "classnames";

export interface TableOfContentProps {
    data: DocumentationElement,
    level?: number,
    query?: string[]
    path?: string
}

export const TableOfContent = ({ data, level, query, path }: TableOfContentProps) => {
    if (data.name === "README") {
        return
    }
    let finalPath = (path ? path : "/documentation") + "/" + data.name
    return <div className="my-2">
        <Link passHref={true} href={finalPath}>
            <a>
                <span className={classNames("cursor-pointer", {
                    "text-blue-500": query && (query[0] === data.name),
                    "font-medium": level === 1,
                    "font-normal": level === 2,
                    "font-light": level > 2
                })}>{data.name}</span>
            </a>
        </Link>
        {
            data.children
                ? <ul style={{
                    paddingLeft: (level ?? 0) * 15
                }}>
                    {
                        data.children.map((value, i) => {
                            return <li key={i}>
                                {<TableOfContent data={value} level={(level ?? 0) + 1} query={query.slice(1)} path={finalPath} />}
                            </li>
                        })
                    }
                </ul>
                : ""
        }
    </div >
}