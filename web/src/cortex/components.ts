import { TableControllerComponent } from "../components/table_controller";
import { RequestHandlerComponent } from "../components/request_handler";
import { WebSocketComponent } from "../components/web_socket";

export class Components {
    
    registrationsTableController: TableControllerComponent
    requestHandlerComponent: RequestHandlerComponent
    webSocketComponent: WebSocketComponent
    
    constructor() {
        this.requestHandlerComponent = new RequestHandlerComponent();
        this.webSocketComponent = new WebSocketComponent();
        this.registrationsTableController = new TableControllerComponent({
            status: [] as HTMLElement[],
            cnpj: [] as HTMLElement[],
            opening: [] as HTMLElement[],
            registration_status: [] as HTMLElement[],
            company_name: [] as HTMLElement[],
            trade_name: [] as HTMLElement[],
            legal_nature: [] as HTMLElement[],
            legal_nature_id: [] as HTMLElement[],
            street: [] as HTMLElement[],
            number: [] as HTMLElement[],
            complement: [] as HTMLElement[],
            neighborhood: [] as HTMLElement[],
            pac: [] as HTMLElement[],
            city: [] as HTMLElement[],
            state: [] as HTMLElement[],
            fone: [] as HTMLElement[],
            email: [] as HTMLElement[],
            tax_regime: [] as HTMLElement[],
            comission_receipt: [] as HTMLElement[],
            client_type: [] as HTMLElement[],
            suggested_limit: [] as HTMLElement[],
            seller: [] as HTMLElement[],
            cpf: [] as HTMLElement[],
            cpf_person: [] as HTMLElement[],
            buttons: [] as HTMLElement[]
        });
    }
    
}
