<?php
// 连接到数据库
$servername = "localhost";
$username = "111";
$password = "111";
$dbname = "111";

$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

// 处理表单提交
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $date = $_POST["date"];

    // 查询数据库中的数据
    $sql = "SELECT id FROM data WHERE date = '$date'";
    $result = $conn->query($sql);

    // 将结果输出为指定格式
    if ($result->num_rows > 0) {
        echo "匹配的 ID 为：";
        while ($row = $result->fetch_assoc()) {
            echo $row["id"] . " ";
        }
    } else {
        echo "没有匹配的 ID";
    }
}

// 关闭连接
$conn->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>查询数据库中的 ID</title>
</head>
<body>
    <h2>查询数据库中的 ID</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        日期: <input type="date" name="date"><br>
        <input type="submit" value="确定">
    </form>
</body>
</html>