<template>
  <h2 class="text-h4 mb-4">Most Visited Links:</h2>
  <v-table class="rounded-xl">
    <thead>
      <tr>
        <th class="text-start">Short Link</th>
        <th class="text-start">Original Link</th>
        <th class="text-start">Created</th>
        <th class="text-start">Visit Count</th>
        <th class="text-start">Last Visited</th>
        <th class="text-center">Actions</th>
      </tr>
    </thead>
    <tbody v-if="status === 'success'">
      <tr v-for="item in (data?.results as Link[])" :key="item.short_code">
        <td>
          {{
            (runtimeConfig.public.domainRoot + item.short_code)
              .replace("http://", "")
              .replace("https://", "")
          }}
        </td>
        <td>{{ item.url }}</td>
        <td>{{ date.format(item.created_at, "fullDateTime12h") }}</td>
        <td>{{ item.visit_count }}</td>
        <td>{{ date.format(item.last_visit_at, "fullDateTime12h") }}</td>
        <td>
          <div class="d-flex flex-wrap ga-2 justify-center">
            <v-btn
              rounded="pill"
              variant="flat"
              color="light-blue"
              append-icon="mdi-open-in-new"
              text="visit"
              :href="runtimeConfig.public.domainRoot + item.short_code"
              target="_blank"
            />
            <v-btn
              rounded="pill"
              variant="outlined"
              color="light-blue"
              append-icon="mdi-arrow-right"
              text="stats"
              :to="{
                name: 'code-info',
                params: {
                  code: item.short_code,
                },
              }"
            />
          </div>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup lang="ts">
import type { Link, Page } from "~/ts/interfaces";

const runtimeConfig = useRuntimeConfig();

const { data, status, error } = await useFetch<Page>(
  `${runtimeConfig.public.apiBase}api/links/`
);

import { useDate } from "vuetify";

const date = useDate();
</script>

<style></style>
