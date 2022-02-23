function square() {
    var numberClient = document.getElementById("number").value;

    var url = "/square";

    axios({
        method: "post",
        url: url,
        data: {
            number: numberClient,
        },
        headers: {
            "Content-Type": "application/json"
        }
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    )
}

function scoreConv() {
    var score = document.getElementById("score").value;

    var url = "/score_Conv";  // url for the python
    axios({
        method: "post",
        url: url,
        data: {
            score: score,
        },
        headers: {
            "Content-Type": "application/json",
        },
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("convert_score_result").value = result["result"];
        },
        (error) => {
            console.log(error);
        }
    );
}


function hypotenuse() {
    var baseNumber = document.getElementById("base").value;
    var heightNumber = document.getElementById("height").value;

    var url = "/hypotenuse";  // url for the python
    axios({
        method: "post",
        url: url,
        data: {
            baseNumber: baseNumber,
            heightNumber: heightNumber,
        },
        headers: {
            "Content-Type": "application/json",
        },
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("hyp_result").value = result["result"];
        },
        (error) => {
            console.log(error);
        }
    );
}