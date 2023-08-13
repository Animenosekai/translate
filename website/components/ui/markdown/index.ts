import { Heading1, Heading2, Heading3, Heading4, Heading5 } from "./headings";
import { ListItem, OrderedList, UnorderedList } from "./lists";
import { Table, TableD, TableH, TableHead, TableR } from "./table";

import { AnchorLink } from "./link";
import { BlockQuote } from "./quote";
import { CodeBlock } from "./code";

export const MarkdownComponent = {
    code: CodeBlock,
    h1: Heading1,
    h2: Heading2,
    h3: Heading3,
    h4: Heading4,
    h5: Heading5,
    li: ListItem,
    ol: OrderedList,
    ul: UnorderedList,
    table: Table,
    thead: TableHead,
    tr: TableR,
    th: TableH,
    td: TableD,
    a: AnchorLink,
    blockquote: BlockQuote
}