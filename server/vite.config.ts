import { defineConfig } from "vite";

export default defineConfig({
    build: {
        outDir: "src/storage/.web_output",
        lib: {
            entry: {},
            formats: ["es"]
        },
        rollupOptions: {
            input: {
                zindex: "./src/storage/web/pages/zindex.ts",
                zlogin: "./src/storage/web/pages/zlogin.ts",
                zadmin: "./src/storage/web/modules/zadmin.ts",
                zcredrpa: "./src/storage/web/modules/zcredrpa.ts"
            },
            output: {
                format: "es",
                entryFileNames: (chunkInfo) => {
                    if (["zindex", "zlogin"].includes(chunkInfo.name)) {
                        return "pages/[name].js";
                    } else {
                        return "modules/[name].js";
                    }
                },
            },
        },
        emptyOutDir: true
    }
});