/**
 * A visual `Loading` component
 */

export const Loading = () => {
    return <div className="relative flex">
        <span className="inline-block h-1 w-1 bg-white rounded-full m-1 animate-loading-blink"></span>
        <span style={{
            animationDelay: "500ms"
        }} className="inline-block h-1 w-1 bg-white rounded-full m-1 animate-loading-blink"></span>
        <span style={{
            animation: "1000ms"
        }} className="inline-block h-1 w-1 bg-white rounded-full m-1 animate-loading-blink"></span>
    </div>
}