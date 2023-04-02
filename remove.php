<?php
// 连接数据库
$servername = "localhost";
$username = "111";
$password = "111";
$dbname = "111";

$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// 获取日期参数
$date = $_GET["date"];

// 从数据库中删除指定日期的所有 ID
$sql = "DELETE FROM data WHERE date = '$date'";
if ($conn->query($sql) === TRUE) {
    echo "已经删除" . $date . "的数据!";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// 关闭数据库连接
$conn->close();
?>