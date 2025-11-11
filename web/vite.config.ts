import { defineConfig } from "vite";
import path from "path";

export default defineConfig({
    build: {
        outDir: path.resolve(__dirname, ".package", "storage"),
        emptyOutDir: true,
        lib: {
            entry: path.resolve(__dirname, "main.ts"),
            name: "zbot",
            fileName: () => "bundle.js",
            formats: ["es"]
        }
    },
});