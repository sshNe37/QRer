'use strict';

// タイマーの日付を設定
//var mine_time_left = $("#time_left").attr('data-time-left');
//var mine_left = new Date($("#time_left").attr('data-time-left'));
var countDownDate = new Date('27 Jan 2030 16:40:00');
//var countDownDate = new Date(mine_time_left).getTime();
//date.setDate( date.getDate() + 1 );
var now2 = new Date();
now2.setMinutes(now2.getMinutes() + 1);


// 1秒おきに更新
var x = setInterval(function() {
  // 今日の日付と時間を取得
  
  var now = new Date().getTime();

  // 日付と時間の計算
  var distance = now2 - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = "0" + Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))
  var seconds = "0" + Math.floor((distance % (1000 * 60)) / 1000);
  // 出力する内容
  document.getElementById("time_left").innerHTML = "残り " + minutes.slice(-2) + "<span>:</span>" + seconds.slice(-2);
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("time_left").innerHTML = "ボタンを押してQRコードを更新して下さい";
  }
}, 1000); 