export class TemplateString extends String {
    format(options?: { [key: string]: any }) {
        let str = this.toString();
        options &&
            Object.entries(options).map(([key, value]) => {
                str = str.replace(
                    new RegExp("\\{" + key + "\\}", "gi"),
                    value?.toString() || ""
                );
            });
        return str
    }
}

export default TemplateString