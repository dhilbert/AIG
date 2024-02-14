<template>
  <v-container fluid>
    <v-row></v-row>

    <v-row>
      <!-- Learning Objectives -->
      <v-col xs="12" sm="12" md="12" lg="5" xl="5">
        <v-card class="mr-1 pa-1" outlined tile>
          <LearningObjectives />
        </v-card>
      </v-col>
      <!-- Question Preview List-->
      <v-col xs="12" sm="12" md="12" lg="7" xl="7">
        <v-card class="mr-1 pa-1" outlined tile>
          <QuestionPreviewList v-on:qsnoData="setQsnoData"></QuestionPreviewList>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <!-- Generated Questions-->
      <v-col xs="12" sm="12" md="12" lg="12" xl="12">
        <v-card outlined tile>
          <GeneratedQuestions v-on:testData="setTestData" v-bind:qsnoData="qsno_list"></GeneratedQuestions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <!-- 시험지 이미지 -->
      <div class="downloadimg" style="position: absolute; top:-20000px; width: 1000px; max-width:1000px height:500px; overflow-y:auto;">
        <!-- 문제지 -->
        <div id="capture1">
          <div v-for="stem in test_data['stem']" :key="stem">
            <div v-html="stem"></div>
          </div>
        </div>
        <!-- 해설지 -->
        <div id="capture2">
          <div v-for="answer in test_data['answer']" :key="answer">
            <div v-html="answer"></div>
          </div>
        </div>
      </div>
      <!--<TestPreview v-on:toggle="setOverlay" v-bind:htmlData="this.test_data" style="position:relative; width:100%; top: 0px; left:25%"/>-->
    </v-row>
    <v-row justify="center">
      <v-dialog v-model="alertDialog" persistent max-width="290" @keydown="alertDialog = false">
        <v-card>
          <v-card-title class="headline text-red">ALERT</v-card-title>
          <v-card-text v-text="alertMessage">Loading...</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="alertDialog = false">CLOSE</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <v-row align-content="center" justify="center">
      <v-dialog
        v-model="progressDialog"
        persistent
        max-width="350"
        @keydown="progressDialog = false"
      >
        <v-card>
          <v-col class="subtitle-1 text-center" cols="12">문항 생성중...</v-col>
          <v-col cols="12">
            <v-progress-linear indeterminate rounded height="6" color="lime darken-4"></v-progress-linear>
          </v-col>
          <v-col class="subtitle-1 text-center" cols="12">생성 개수에 따라 시간이 소요될 수 있습니다.</v-col>
        </v-card>
      </v-dialog>
    </v-row>
    <v-row align-content="center" justify="center">
      <v-dialog
        v-model="progressDownload"
        persistent
        max-width="350"
        @keydown="progressDownload = false"
      >
        <v-card>
          <v-col class="subtitle-1 text-center" cols="12">문항 다운로드 중...</v-col>
          <v-col cols="12">
            <v-progress-linear indeterminate rounded height="6" color="lime darken-4"></v-progress-linear>
          </v-col>
          <v-col class="subtitle-1 text-center" cols="12">생성 개수에 따라 시간이 소요될 수 있습니다.</v-col>
        </v-card>
      </v-dialog>
    </v-row>

    <v-snackbar v-model="snackbar" :multi-line="multiLine" color="brown lighten-2" right bottom>
      {{ alertMessage }}
      <v-btn color="white" text @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
import LearningObjectives from "../components/LearningObjectives";
import QuestionPreviewList from "../components/QuestionPreviewList";
import GeneratedQuestions from "../components/GeneratedQuestions";
//import TestPreview from "../components/TestPreview";
/* eslint-disable no-console */
export default {
  name: "home",
  components: {
    LearningObjectives,
    QuestionPreviewList,
    GeneratedQuestions,
    //TestPreview,
  },
  data() {
    return {
      overlay: false,
      alertDialog: false,
      alertMessage: null,
      progressDialog: false,
      progressDownload: false,
      progressMessage: "문항 생성중...",
      multiLine: true,
      snackbar: false,
      qsno_list: [],
      test_data: {}
    };
  },
  updated() {
    var MathJax = window.MathJax; // eslint-disable-line no-unused-vars

    window.MathJax.Hub.Config({
      showMathMenu: false,
      tex2jax: { displayMath: [["$$", "$$"]] },
      displayAlign: "left"
    });

    window.cdml_mathjax_init();
    window.cdml_mathjax_rerender();
  },
  created() {
    this.$EventBus.$on(
      "popAlertMessageToHome",
      function(alertMessage) {
        this.popAlertMessage(alertMessage);
      }.bind(this)
    );

    this.$EventBus.$on(
      "popProgressBarToHome",
      function(progressMessage, isStart) {
        this.popProgressBar(progressMessage, isStart);
      }.bind(this)
    );

    this.$EventBus.$on(
      "popDownloadBarToHome",
      function(progressMessage, isStart) {
        this.popDownloadBar(progressMessage, isStart);
      }.bind(this)
    );

    this.$EventBus.$on(
      "generaionSnackBarToHome",
      function(alertMessage) {
        this.generaionSnackBar(alertMessage);
      }.bind(this)
    );
  },
  methods: {
    setTestData(data) {
      this.test_data = data["res"];
      this.overlay = data["overlay"];
      window.scrollTo(0,0);
      //document.querySelector("html").style.overflowY = "hidden";
    },
    setOverlay(data) {
      this.overlay = data;
      document.querySelector("html").style.overflowY = "auto";
    },
    setQsnoData(data){
      this.qsno_list = data;
      console.log(this.qsno_list)
    },
    popAlertMessage(alertMessage) {
      this.alertDialog = true;
      this.alertMessage = alertMessage;
    },
    popProgressBar(progressMessage, isStart) {
      this.progressDialog = isStart;
      this.progressMessage = progressMessage;
    },
    popDownloadBar(progressMessage, isStart) {
      this.progressDownload = isStart;
      this.progressMessage = progressMessage;
    },
    generaionSnackBar(alertMessage) {
      this.alertMessage = alertMessage;
      this.snackbar = true;
    }
  }
};
</script>
