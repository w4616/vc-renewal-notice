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

// 查询数据库，检查 ID 是否存在
$sql = "SELECT id FROM data WHERE id = '$id'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 如果 ID 存在，从数据库中删除该 ID 的数据
    $sql = "DELETE FROM data WHERE id = '$id'";
    if ($conn->query($sql) === TRUE) {
        echo "删除成功，id:$id!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    // 否则输出错误消息
    echo "Error: ID".$id."不存在!";
}

// 关闭数据库连接
$conn->close();
?>