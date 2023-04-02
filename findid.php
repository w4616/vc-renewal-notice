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

$id = $_GET["id"];

// 查询数据库中的数据
$sql = "SELECT id, date FROM data WHERE id = '$id'";
$result = $conn->query($sql);

// 将结果输出为数组
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo "id=". $row["id"] ." 日期=". $row["date"];
} else {
    echo "没有结果";
}

// 关闭连接
$conn->close();
?>