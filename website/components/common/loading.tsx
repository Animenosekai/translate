/**
 * A visual `Loading` component
 */

export const Loading = () => {
    return <div className="relative flex">
        <span className="inline-block h-2 w-2 bg-white rounded-full mx-1 animate-loading-blink"></span>
        <span className="inline-block h-2 w-2 bg-white rounded-full mx-1 animate-loading-blink delay-500"></span>
        <span className="inline-block h-2 w-2 bg-white rounded-full mx-1 animate-loading-blink delay-1000"></span>
    </div>
}