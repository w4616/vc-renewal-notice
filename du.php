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

// 从数据库中获取指定日期的所有 ID
$sql = "SELECT id FROM data WHERE date = '$date'";
$result = $conn->query($sql);

// 将结果转换为 JSON 格式并输出
if ($result->num_rows > 0) {
    $data = array();
    while($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    echo json_encode($data);
} else {
    echo "No results found.";
}

// 关闭数据库连接
$conn->close();
?>