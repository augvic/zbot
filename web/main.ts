import { Controller } from "./src/controller_layer/controller_module/controller";

const controller = new Controller();
await controller.init();
controller.run_process();
