export const Button = ({ ...props }) => {
    return (
        <button className="rounded bg-blue-500 shadow transition text-white px-2 py-1 hover:bg-blue-600" {...props}></button>
    );
};