import { Heading1, Heading2, Heading3, Heading4 } from "./headings";
import { ListItem, OrderedList, UnorderedList } from "./lists";

import { CodeBlock } from "./code";

export const MarkdownComponent = {
    code: CodeBlock,
    h1: Heading1,
    h2: Heading2,
    h3: Heading3,
    h4: Heading4,
    li: ListItem,
    ol: OrderedList,
    ul: UnorderedList
}