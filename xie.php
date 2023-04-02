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

// 获取 ID 和日期参数
$id = $_GET["id"];
$date = $_GET["date"];

// 将数据插入数据库
$sql = "INSERT INTO data (id, date) VALUES ('$id', '$date')";
if ($conn->query($sql) === TRUE) {
    $sql = "SELECT date FROM data WHERE id = $id";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
    echo "创建成功!到期时间:". $row["date"];
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// 关闭数据库连接
$conn->close();