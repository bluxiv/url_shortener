// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  ssr: false,
  devtools: { enabled: true },
  modules: ["vuetify-nuxt-module"],

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || "http://localhost:8000/",
      domainRoot:
        process.env.NUXT_PUBLIC_DOMAIN_ROOT || "localhost:3000/",
    },
  },

  experimental: {
    inlineRouteRules: true
  }
});
