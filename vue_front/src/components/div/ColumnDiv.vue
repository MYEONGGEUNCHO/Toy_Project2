<template>
  <div class="eg-layout" :class="classObject" :style="styleObject">
    <slot></slot>
  </div>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps(["span", "px"]);
const classObject = ref({
  column: true,
  fit: true,
});

const styleObject = ref({});

// 12등분 중 너비(높이) 처리
if (!isNaN(+props.span)) {
  classObject.value.fit = false;
  classObject.value.col = true;
  classObject.value["col-shrink"] = true;
  classObject.value["col-" + props.span] = true;
}

// 고정 픽셀 처리
if (!isNaN(+props.px)) {
  classObject.value.fit = false;
  classObject.value.col = true;
  classObject.value["col-shrink"] = true;
  styleObject.value.flexBasis = props.px + "px";
}
</script>

