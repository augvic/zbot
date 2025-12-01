import * as components from "./components";

export class UiFactory {
    
    public createContainer(
        orientation: string,
        width: string,
        height: string,
        verticalAlign: string,
        horizontalAlign: string,
        bgColor: boolean,
        blur: boolean,
        fixed: { verticalPosition: string, horizontalPosition: string } | null
    ) {
        return new components.Container(
            orientation,
            width,
            height,
            verticalAlign,
            horizontalAlign,
            bgColor,
            blur,
            fixed
        );
    }
    
    public createInput(
        placeholder: string,
        type: string,
        width: string,
        height: string
    ) {
        return new components.Input(
            placeholder,
            type,
            width,
            height
        )
    }
    
    public createLabel(
        text: string,
        bold: boolean,
        size: string
    ) {
        return new components.Label(
            text,
            bold,
            size
        )
    }
    
    public createButton(
        text: string,
        bgColor: string,
        width: string,
        height: string,
        icon: string | null,
        hoverSpan: { text: string, position: string, bgColor: string } | null
    ) {
        return new components.Button(
            text,
            bgColor,
            width,
            height,
            icon,
            hoverSpan
        )
    }
    
    public createNotification(
        message: string,
        color: string
    ) {
        return new components.Notification(
            message,
            color
        )
    }
    
    public createTable(
        width: string,
        height: string,
        rows: [{}]
    ) {
        return new components.Table(
            width,
            height,
            rows
        )
    }
    
}
