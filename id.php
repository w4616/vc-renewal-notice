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

// 获取 ID 参数
$id = $_GET["id"];

// 从数据库中查找指定的 ID
$sql = "SELECT id FROM data WHERE id = '$id'";
$result = $conn->query($sql);

// 输出结果
if ($result->num_rows > 0) {
    echo "yes";
} else {
    echo "no";
}

// 关闭数据库连接
$conn->close();