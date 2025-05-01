export default defineNuxtRouteMiddleware((to, from) => {
  const runtimeConfig = useRuntimeConfig();
  if (to.params.code) {
    navigateTo(`${runtimeConfig.public.apiBase}/${to.params.code}`, {
      external: true,
    });
  } else {
    navigateTo({ name: "index" });
  }
});
