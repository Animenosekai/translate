import { HTMLAttributes, useEffect, useState } from 'react'

import { Colorful } from 'components/common/colorful'
import Configuration from 'config'
import Link from 'next/link'
import { MarkdownComponent } from 'components/ui/markdown'
import type { NextPage } from 'next'
import ReactMarkdown from 'react-markdown'
import { SEO } from 'components/common/seo'
import { TableOfContent } from 'components/common/toc'
import classNames from 'classnames'
import rehypeRaw from 'rehype-raw'
// import rehypeSanitize from 'rehype-sanitize'
import remarkGfm from 'remark-gfm'
import { request } from 'lib/request'
import { useHeadings } from 'contexts/headings'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'

export const TOC = ({ className, ...props }: HTMLAttributes<HTMLDivElement>) => {
    const { strings } = useLanguage();
    const { query } = useRouter();
    const [path, setPath] = useState<string[]>((query.path as string[]) || []);

    useEffect(() => {
        setPath((query.path as string[]) || [])
    }, [query])

    return <div className={classNames("flex flex-col", className)} {...props}>
        {
            strings.documentation
                ? strings.documentation.map((value, i) => {
                    return <TableOfContent data={value} key={i} level={1} query={path} />
                })
                : ""
        }
    </div>
}

const Documentation: NextPage = () => {
    const { strings } = useLanguage();
    const router = useRouter();
    const [path, setPath] = useState<string[]>((router.query.path as string[]) || []);

    const [content, setContent] = useState<string>();

    const { setHeadings } = useHeadings();

    useEffect(() => {
        setPath((router.query.path as string[]) || [])
    }, [router.query])

    useEffect(() => {
        setHeadings([])
    }, [content])

    useEffect(() => {
        const __path__ = path.join("|")
        let documentationItems = strings.documentation
        let resultPath = ""
        for (const i in path) {
            const result = documentationItems.find(value => value.name === path[i])
            if (!result) { break }
            resultPath += `/${encodeURIComponent(result.name)}`
            if (!result.children) {
                resultPath += ".md"
                break
            }
            documentationItems = result.children
        }
        if (!resultPath.endsWith(".md")) {
            resultPath += "/README.md"
        }
        request<{ markdown: string }>(`${Configuration.request.host}/docs${resultPath}`, {
            params: {
                lang: strings.language
            }
        })
            .then(({ markdown }) => {
                if (path.join("|") === __path__) {
                    setContent(markdown)
                }
            })
    }, [path, strings])

    return <div className='h-full'>
        <SEO title='Documentation' description='Learn how to use translatepy!' />
        <div className='flex gap-2 w-screen'>
            <div className="p-5 ml-3 overflow-y-auto h-screen w-max flex-col gap-2 sticky top-0 sm:flex hidden">
                <Link passHref={true} href="/documentation">
                    <a>
                        <span className='mx-auto self-center text-xl font-semibold m-5 cursor-pointer'>translatepy {<Colorful value='docs' />}</span>
                    </a>
                </Link>
                <div className='flex flex-row'>
                    <TOC />
                    {/* <div className="border-l-[1px] border-l-slate-300 opacity-50 ml-5 h-[70vh]" /> */}
                </div>
            </div>
            <div className='sm:w-3/4 sm:mx-0 mb-5 w-full mx-5'>
                <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]} components={MarkdownComponent}>{content}</ReactMarkdown>
            </div>
        </div>
    </div>
}

export default Documentation
