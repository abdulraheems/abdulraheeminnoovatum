(window["aioseopjsonp"]=window["aioseopjsonp"]||[]).push([["seo-analysis-AnalyzeCompetitorSite-vue"],{"3b33":function(t,e,s){"use strict";s("cfffe")},cfffe:function(t,e,s){},e638:function(t,e,s){"use strict";s.r(e);var i=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"aioseo-analyze-competitor-site"},[s("core-analyze-competitor-site-header",{scopedSlots:t._u([{key:"competitor-results",fn:function(){return t._l(t.competitorResults,(function(e,i){return s("core-card",{key:i,attrs:{id:"aioseo-competitor-results"+t.hashCode(i),slug:"analyzeCompetitorSite"+i,"save-toggle-status":!1},scopedSlots:t._u([{key:"header",fn:function(){return[s("core-analyze-score",{attrs:{score:t.parseResults(e).score}}),t._v(" "+t._s(i)+" "),s("svg-trash",{nativeOn:{click:function(e){return t.startDeleteSite(i)}}})]},proxy:!0}],null,!0)},[s("div",{staticClass:"competitor-results-main"},[s("core-site-score-competitor",{attrs:{site:i,score:t.parseResults(e).score,loading:t.analyzing,summary:t.getSummary(t.parseResults(e).results),"mobile-snapshot":t.parseResults(e).results.advanced.mobileSnapshot}}),s("div",{staticClass:"competitor-results-body"},[s("core-seo-site-analysis-results",{attrs:{section:"all-items","all-results":t.parseResults(e).results,"show-google-preview":""}})],1)],1)])}))},proxy:!0}])},[s("core-analyze",{attrs:{header:t.strings.enterCompetitorUrl,description:t.strings.performInDepthAnalysis,inputError:t.inputError,isAnalyzing:t.isAnalyzing,analyzeTime:t.analyzeTime,placeholder:"https://competitorwebsite.com"},on:{startAnalyzing:t.startAnalyzing},scopedSlots:t._u([{key:"errors",fn:function(){return[t.inputError?s("div",{staticClass:"aioseo-description aioseo-error"},[t._v(" "+t._s(t.strings.pleaseEnterValidUrl)+" ")]):t._e(),"competitor-site"===t.analyzer&&t.analyzeError?s("div",{staticClass:"analyze-errors aioseo-description aioseo-error",domProps:{innerHTML:t._s(t.analyzeError)}}):t._e()]},proxy:!0}])})],1)],1)},r=[],o=s("5530"),n=(s("ac1f"),s("5319"),s("2ca0"),s("b64b"),s("159b"),s("2f62")),a=s("9c0e"),l=s("5c0f"),c={mixins:[a["o"]],data:function(){return{competitorUrl:null,isAnalyzing:!1,inputError:!1,competitorResults:{},analyzeTime:8,strings:{enterCompetitorUrl:this.$t.__("Enter Competitor URL",this.$td),performInDepthAnalysis:this.$t.__("Perform in-depth SEO Analysis of your competitor's website.",this.$td),analyze:this.$t.__("Analyze",this.$td),pleaseEnterValidUrl:this.$t.__("Please enter a valid URL.",this.$td)}}},watch:{analyzeError:function(t){t&&(this.isAnalyzing=!1)}},computed:Object(o["a"])(Object(o["a"])(Object(o["a"])({},Object(n["e"])(["options","analyzer","analyzing","analyzeError"])),Object(n["c"])(["getCompetitorSiteAnalysisResults","goodCount","recommendedCount","criticalCount"])),{},{getError:function(){switch(this.analyzeError){case"invalid-url":return this.$t.__("The URL provided is invalid.",this.$td);case"missing-content":return this.$t.sprintf("%1$s %2$s",this.$t.__("We were unable to parse the content for this site.",this.$td),this.$links.getDocLink(this.$constants.GLOBAL_STRINGS.learnMore,"seoAnalyzerIssues",!0));case"invalid-token":return this.$t.sprintf(this.$t.__("Your site is not connected. Please connect to %1$s, then try again.",this.$td),"AIOSEO")}return this.analyzeError}}),methods:Object(o["a"])(Object(o["a"])(Object(o["a"])({},Object(n["b"])(["runSiteAnalyzer","deleteCompetitorSite","saveConnectToken"])),Object(n["d"])(["toggleCard","closeCard"])),{},{parseResults:function(t){return JSON.parse(t)},getSummary:function(t){return{recommended:this.recommendedCount(t),critical:this.criticalCount(t),good:this.goodCount(t)}},startAnalyzing:function(t){this.inputError=!1,this.competitorUrl=t.replace("http://","https://"),this.competitorUrl.startsWith("https://")||(this.competitorUrl="https://"+this.competitorUrl),Object(l["a"])(this.competitorUrl)?(this.$store.commit("analyzing",!0),this.$store.commit("analyzeError",!1),this.runSiteAnalyzer({url:this.competitorUrl}),this.isAnalyzing=!0,setTimeout(this.checkStatus,1e3*this.analyzeTime),this.closeAllCards()):this.inputError=!0},checkStatus:function(){var t=this;this.isAnalyzing=!1,this.analyzing?this.$nextTick((function(){t.isAnalyzing=!0,2>t.analyzeTime&&(t.analyzeTime=8),t.analyzeTime=t.analyzeTime/2,setTimeout(t.checkStatus,1e3*t.analyzeTime)})):(this.competitorUrl=null,this.competitorResults=this.getCompetitorSiteAnalysisResults,this.toggleFirstCard(),this.$nextTick((function(){var e=Object.keys(t.competitorResults),s=document.querySelector(".aioseo-header"),i=s.offsetHeight+s.offsetTop+30;t.$scrollTo("#aioseo-competitor-results"+t.hashCode(e[0]),{offset:-i})})))},startDeleteSite:function(t){var e=this;this.closeAllCards(),this.$delete(this.competitorResults,t),this.deleteCompetitorSite(t).then((function(){e.competitorResults=e.getCompetitorSiteAnalysisResults}))},closeAllCards:function(){var t=this,e=Object.keys(this.competitorResults);e.forEach((function(e){t.closeCard("analyzeCompetitorSite"+e)}))},toggleFirstCard:function(){var t=Object.keys(this.competitorResults);this.toggleCard("analyzeCompetitorSite"+t[0])},hashCode:function(t){if(t){var e,s,i=0;for(e=0;e<t.length;e++)s=t.charCodeAt(e),i=(i<<5)-i+s,i|=0;return i}}}),mounted:function(){this.$store.commit("analyzeError",!1),this.competitorResults=this.getCompetitorSiteAnalysisResults,this.toggleFirstCard()}},u=c,h=(s("3b33"),s("2877")),p=Object(h["a"])(u,i,r,!1,null,null,null);e["default"]=p.exports}}]);