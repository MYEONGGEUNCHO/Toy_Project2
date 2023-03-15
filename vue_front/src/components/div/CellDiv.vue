<template>
  <div class="eg-layout eg-cell" :class="classObject" :style="styleObject">
    <div v-if="!!headerTitle" class="col col-shrink justify-between row q-pt-xs q-px-xs">
      <div class="col col-shrink flex flex-center">
        <slot name="left"></slot>
      </div>
      <div class="col col-grow">
        <div class="row">
          <span class="text-subtitle">{{ headerTitle }}</span>
          <div class="row q-ml-sm flex-center">
            <slot name="title-right"></slot>
          </div>
        </div>
      </div>
      <div class="col col-shrink flex flex-center">
        <slot name="right"></slot>
      </div>
    </div>
    <div class="col col-grow q-ma-xs">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
/**
* [props]
* - span : 해당 부모영역에서 차지하는 비율(x/12)
* - px : 해당 부모영역에서 차지하는 고정너비(높이)
* - headerTitle : 해당 영역 타이틀
* - fit : 현재 Cell 내부의 항목만큼만 차지할 지에 대한 여부
*/
import { ref } from "vue";

const props = defineProps(["span", "px", "headerTitle", "fit"]);

const classObject = ref({
  col: true,
  column: true,
});

const styleObject = ref({});
// 내부 영역에 맞출 때
if (props.fit === "Y") {
  classObject.value["col-shrink"] = true;
}

// 12등분 중 너비(높이) 처리
if (!isNaN(+props.span)) {
  classObject.value["col-shrink"] = true;
  classObject.value["col-" + props.span] = true;
}

// 고정 픽셀 처리
if (!isNaN(+props.px)) {
  classObject.value["col-shrink"] = true;
  styleObject.value.flexBasis = props.px + "px";
}
</script>