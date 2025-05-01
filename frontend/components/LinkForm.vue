<template>
  <div>
    <v-form v-model="valid">
      <v-text-field
        v-model="linkInput.value"
        :error-messages="linkInput.error"
        :rules="[rules.required]"
        label="Enter the link here."
        prepend-inner-icon="mdi-link-variant"
        variant="solo"
        flat
        rounded="pill"
        oneline
      >
        <template #append-inner>
          <div class="me-n2 pa-2">
            <template v-if="valid">
              <v-btn
                icon="mdi-arrow-right"
                variant="flat"
                color="light-blue"
                type="submit"
                @click="submitForm()"
              />
            </template>
            <template v-else>
              <v-btn
                icon="mdi-arrow-right"
                variant="flat"
                color="light-blue"
                disabled
              />
            </template>
          </div>
        </template>
      </v-text-field>
    </v-form>
  </div>
</template>

<script setup lang="ts">
import type { Link } from "~/ts/interfaces";

const runtimeConfig = useRuntimeConfig();

const linkInput = ref({
  value: "",
  error: "",
});
const valid = ref(false);
const rules = {
  required: (value: string) => !!value || "This field is required",
};

watch(
  () => linkInput.value.value,
  (newValue, oldValue) => {
    linkInput.value.error = "";
  }
);

async function submitForm() {
  await $fetch<Link>(runtimeConfig.public.apiBase + "api/links/", {
    method: "POST",
    body: {
      url: linkInput.value.value,
    },
  })
    .then(async (response) => {
      await navigateTo({
        name: "code-info",
        params: {
          code: response.short_code,
        },
      });
    })
    .catch((err) => {
      linkInput.value.error = err.data.url;
    });
}
</script>

<style scoped></style>
