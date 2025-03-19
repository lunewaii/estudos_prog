var arr = [1, 2, 3, 4, 5];
//com for, fazemos:
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

var arr2 = ["gabs", "rebs", "garebs"];

//com forEach, fazemos:
arr2.forEach(function (value, index) {
  console.log(value + " tem o index: " + index);
});