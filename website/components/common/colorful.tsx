import { HTMLAttributes, useEffect, useRef, useState } from "react"

import { range } from "utils/range"

export interface ColorfulProps extends HTMLAttributes<HTMLDivElement> {
    value: string
    interval?: number
    colors?: string[]
    backward?: boolean
}

/* Default colors for the component */
export const DEFAULT_COLORS =
    ["#ffffff", "#ff0080", "#ff00ff", "#ff0000", "#ff8000", "#ffff00", "#80ff00",
        "#00ff00", "#00ff80", "#00ffff", "#0080ff", "#0000ff", "#8000ff", "#000000"];

export const Colorful = ({ value, interval, backward, colors, ...props }: ColorfulProps) => {
    const [iteration, setIteration] = useState(0);
    const currentInterval = useRef<any>(null);
    interval = interval ? interval : 50

    useEffect(() => {
        currentInterval.current = setInterval(() => {
            setIteration(i => {
                if (i >= ((colors ?? DEFAULT_COLORS).length + value.length)) {
                    clearInterval(currentInterval.current)
                    return i
                }
                return i + 1
            })
        }, interval)
        return () => { clearInterval(currentInterval.current) }
    }, [])

    return <div {...props}>
        {
            range(value.length).map((position, i) => {
                const currentPosition = backward ? (value.length - position) : position
                let currentIteration = iteration - currentPosition
                if (currentIteration < 0) {
                    currentIteration = 0
                } else if (currentIteration > ((colors ?? DEFAULT_COLORS).length)) {
                    currentIteration = (colors ?? DEFAULT_COLORS).length
                }
                return <span style={{
                    transition: `color linear ${interval}ms`,
                    color: (colors ?? DEFAULT_COLORS)[currentIteration]
                }} key={i}>{value.charAt(position)}</span>
            })
        }
    </div>
}