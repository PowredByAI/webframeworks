import { Application, Router, Context } from "https://deno.land/x/oak/mod.ts";

const http = new Application();
const router = new Router();
router.get("/", async (context: Context) => {
    context.response.body = "Hello world!";
})
http.use(router.routes());
http.use(router.allowedMethods());
http.listen({ port: 3030 });