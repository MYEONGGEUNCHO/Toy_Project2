<template>
  <q-page class="flex flex-center" padding>
    <Row px="1024">
      <div class="col-6">
        <div class="row justify-center items-center q-mr-sm">
          <Row>
            <Cell>
              <q-input v-model="dept" type="number" label="부채" />
              <q-input v-model="capital" type="text" label="자본" />
              <q-input v-model="interest" type="text" label="이자율" />
            </Cell>
          </Row>
          <Row>
            <q-btn color="primary" icon="calculate" label="계산" @click="calculateHandler" style="width: 100%"
              class="q-mb-xs" />
          </Row>
          <Row>
            <q-btn color="negative" icon="refresh" label="초기화" @click="clearHandler" style="width: 100%"
              class="q-mt-xs" />
          </Row>
        </div>
      </div>
      <Column span="6">
        <q-table virtual-scroll title="테이블" :rows="tableData" :columns="tableColumns" row-key="profitRate"
          rows-per-page-options="0" style="height: 800px" />
      </Column>
    </Row>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import Cell from 'src/components/div/CellDiv.vue'
import Row from 'src/components/div/RowDiv.vue'
import Column from 'src/components/div/ColumnDiv.vue'
import { question, leverage, answer, user } from 'src/boot/apiList';
import { useQuasar } from 'quasar'

const $q = useQuasar();

const dept = ref(600);
const capital = ref(400);
const interest = ref(0.06);

const revenueRateList = {
  "-2": "-200.0%",
  "-1.9": "-190.0%",
  "-1.8": "-180.0%",
  "-1.7": "-170.0%",
  "-1.6": "-160.0%",
  "-1.5": "-150.0%",
  "-1.4": "-140.0%",
  "-1.3": "-130.0%",
  "-1.2": "-120.0%",
  "-1.1": "-110.0%",
  "-1": "-100.0%",
  "-0.9": "-90.0%",
  "-0.8": "-80.0%",
  "-0.7": "-70.0%",
  "-0.6": "-60.0%",
  "-0.5": "-50.0%",
  "-0.4": "-40.0%",
  "-0.3": "-30.0%",
  "-0.2": "-20.0%",
  "-0.1": "-10.0%",
  "0": "0.0%",
  "0.1": "10.0%",
  "0.2": "20.0%",
  "0.3": "30.0%",
  "0.4": "40.0%",
  "0.5": "50.0%",
  "0.6": "60.0%",
  "0.7": "70.0%",
  "0.8": "80.0%",
  "0.9": "90.0%",
  "1": "100.0%",
  "1.1": "110.0%",
  "1.2": "120.0%",
  "1.3": "130.0%",
  "1.4": "140.0%",
  "1.5": "150.0%",
  "1.6": "160.0%",
  "1.7": "170.0%",
  "1.8": "180.0%",
  "1.9": "190.0%",
  "2": "200.0%",
};

const tableData = ref([]);

const tableColumns = [
  { name: 'revenueRate', label: '수익률', align: 'right', field: 'revenueRate' },
  { name: 'revenue', label: '수익', align: 'right', field: 'revenue' },
  { name: 'interestRate', label: '이자율', align: 'right', field: 'interestRate' },
  { name: 'cost', label: '이자(비용)', align: 'right', field: 'cost' },
  { name: 'profit', label: '이자깐수익', align: 'right', field: 'profit' },
  { name: 'profit_rate', label: '총수익률', align: 'right', field: 'profit_rate' },
]

// handler

const calculateHandler = () => {
  leverage.calculater(
    {
      capital: capital.value,
      debt: dept.value,
      interest_rate: interest.value
    }
  ).then((res) => {
    let data = res.data;
    let keys = Object.keys(data).sort((a, b) => { return b - a; });
    console.log(data)
    keys.forEach(key => {
      let ele = data[key];
      let revenueName = revenueRateList[key];
      tableData.value.push({
        revenueRate: revenueName,
        revenue: ele.revenue,
        interestRate: interest.value + "%",
        cost: ele.cost,
        profit: ele.profit,
        profit_rate: Number(ele.profit_rate).toFixed(2) + "%",
      })
    })
  }).catch((err) => {
    $q.notify("뭐가 비었는데");
  })
}

const clearHandler = () => {
  dept.value = null;
  capital.value = null;
  interest.value = null;
}
</script>
