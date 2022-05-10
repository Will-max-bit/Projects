<?php

function domain($url)
{
    $domainName = parse_url($url);
    return $domainName['host'];
}

function rSS($url)
{
    $content = file_get_contents($url);

    $a = new SimpleXMLElement($content);
    $buildRSS = simplexml_load_file($url);
    $domainName = parse_url($url);
    $result = array();
    foreach ($buildRSS->channel->item as $item) {

        $title = $item->title;
        $link = $item->link;
        $description =  substr($item->description, 0, 140) . '....';
        $dateOnly = substr($item->pubDate, 0, -14);
        $time =  date("g:iA", strtotime(substr($item->pubDate, 16, -5)));
        $result[] = array(
            'title' => $title,
            'link' => $link,
            'description' =>  $description,
            'time' => $dateOnly . ' ' . $time,
        );
    };
    ;
    return $result;
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
    <title>RSS FEEDER</title>
</head>

<body>
    <h1>Rss Feeder</h1>
    <div class="container">
        <form action="index.php" method="post">
            <div class="form-group">
                <label for="url"></label>
                <input type="text" class="form-control" name="rssurl" placeholder="Enter the url you want RSS from">
                </label>
            </div>
            <div class="row my-1 ">
                <div class="d-grid gap-2 col-6 mx-auto text-center">
                    <input type="submit" class=" btn btn-primary" value="submit" name="submit">
                </div>
            </div>
        </form>

        <div class="content container-fluid">
            <div class="row justify-content-center align-items-center">
    
                <!-- <div class="col-sm text-center"> -->
                <?php if (isset($_POST['submit'])) {
                    echo '<h1 class="text-center">' . domain($_POST['rssurl']) . '</h1>';
                    $result = rss($_POST['rssurl']);
    
                    foreach ($result as $results) {
                        echo '<div class=col>';
                        echo '<div class="card mx-1 my-1" style="width: 18rem; ">';
                        echo '<div class="card-body">';
                        echo '<h5 class="card-title" style="font-size: 1rem;">' . $results['title'] . '</h5>';
                        echo '<p class="card-text text-center">' . $results['description'] . '</p>';
                        echo "<a href='" . $results['link'] . "' class='card-link' >" ."Link" . "</a>";
                        echo '</div>';
                        echo '</div>';
                        echo '</div>';
                    }
                } ?>
                </div>
            </div>
    
        <!-- </div> -->

    </div>

    
    


    <!-- //     echo $results['time'];
    // 'title' => $title,
    // 'link' => $link,
    // 'description' =>  $description,
    // 'time' => $dateOnly . ' ' . $time , -->


</body>

</html>