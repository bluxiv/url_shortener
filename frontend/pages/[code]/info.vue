<template>
  <v-row v-if="data">
    <v-col cols="6" offset="3">
      <v-card class="text-center rounded-xl" flat>
        <v-card-title class="ga-2 d-flex flex-column">
          <div class="text-mono pa-2">
            {{
              (runtimeConfig.public.domainRoot + data?.short_code)
                .replace("http://", "")
                .replace("https://", "")
            }}
          </div>
        </v-card-title>
        <v-card-subtitle>
          <v-row>
            <v-col cols="6">
              <div class="d-flex ga-2 align-center justify-center">
                <v-icon size="large">mdi-calendar</v-icon>
                <span class="text-body-1">{{
                  date.format(data.created_at, "fullDateTime12h")
                }}</span>
              </div>
            </v-col>
            <v-col cols="6">
              <div class="d-flex ga-2 align-center justify-center">
                <v-icon size="large">mdi-link-variant</v-icon>
                <span class="text-body-1">{{ data.url }}</span>
              </div>
            </v-col>
          </v-row>
        </v-card-subtitle>
        <v-divider class="opacity-50 mt-2" />
        <v-card-text>
          <div class="d-flex ga-2">
            <v-btn
              class="flex-grow-1"
              rounded="pill"
              variant="flat"
              color="light-blue"
              prepend-icon="mdi-open-in-new"
              text="visit"
              :href="runtimeConfig.public.domainRoot + data.short_code"
              target="_blank"
            />
            <template v-if="linkCopied">
              <v-btn
                class="w-50"
                rounded="pill"
                variant="tonal"
                color="light-blue"
                prepend-icon="mdi-check-bold"
                text="link Copied"
              />
            </template>
            <template v-else>
              <v-btn
                class="w-50"
                rounded="pill"
                variant="outlined"
                color="light-blue"
                prepend-icon="mdi-content-copy"
                text="copy"
                @click="copyLink()"
              />
            </template>
          </div>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12">
      <VisitsHistory />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import type { Link } from "~/ts/interfaces";
import { useDate } from "vuetify";

const runtimeConfig = useRuntimeConfig();
const route = useRoute();
const date = useDate();
const linkCopied = ref(false);

const { data, status, error } = await useFetch<Link>(
  `${runtimeConfig.public.apiBase}api/links/${route.params.code}`
);

function copyLink() {
  if (data.value) {
    navigator.clipboard.writeText(
      runtimeConfig.public.domainRoot + data.value.short_code
    );
    linkCopied.value = true;
    setTimeout(() => (linkCopied.value = false), 2000);
  } else {
    alert("error!");
  }
}
</script>

<style scoped></style>
