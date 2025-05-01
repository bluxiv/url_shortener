<template>
  <h2 class="text-h4 mb-4">Visits History:</h2>
  <v-table class="rounded-xl">
    <thead>
      <tr>
        <th class="text-start">Date</th>
        <th class="text-start">IP Adress</th>
        <th class="text-start">User Agent</th>
      </tr>
    </thead>
    <tbody v-if="status === 'success'">
      <tr v-if="data?.results.length" v-for="item in (data?.results as Visit[])">
        <td>{{ date.format(item.timestamp, "fullDateTime12h") }}</td>
        <td>{{ item.ip_address }}</td>
        <td>{{ item.user_agent }}</td>
      </tr>
      <tr v-else>
        <td class="text-center" colspan="3">No Visits Yet</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup lang="ts">
import type { Visit, Page } from "~/ts/interfaces";
import { useDate } from "vuetify";

const date = useDate();

const runtimeConfig = useRuntimeConfig();
const route = useRoute();

const { data, status, error } = await useFetch<Page>(
  `${runtimeConfig.public.apiBase}api/links/${route.params.code}/visits/`
);
</script>

<style></style>
