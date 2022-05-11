<?php

function domain($url)
{
    $domainName = parse_url($url);
    return $domainName['host'];
}

function rSS($url)
{
    $buildRSS = simplexml_load_file($url); // converting webpage into object
    $result = array();
    if (!filter_var($url, FILTER_VALIDATE_URL) === false){ // if the url is valid, new object will be built
        foreach ($buildRSS->channel->item as $item) {
            $title = $item->title;
            $link = $item->link;
            $description =  substr($item->description, 0, 140) . '....'; // in order to keep cards responsive and manageable, description is sliced to len of a tweet 
            $dateOnly = substr($item->pubDate, 0, -14);
            $time =  date("g:iA", strtotime(substr($item->pubDate, 16, -5)));
            $result[] = array(
                'title' => $title,
                'link' => $link,
                'description' =>  $description,
                'time' => $dateOnly . ' ' . $time, // concatenating date and time variables for ease of use 
            );
        };;
        return $result;
    } else {
        $result[] = array(
            'title' => 'invalid url',
            'link' => 'invalid url',
            'description' => 'invalid url',
            'time' => 'invalid url' . ' ' . 'invalid url',
        );
        echo '<h1> This URL is not valid, please try again </h1>';
        return $result;
    }
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=IBM+Plex+Mono:wght@200&family=Montserrat:wght@300&display=swap" rel="stylesheet">
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
    <title>RSS FEEDER</title>
</head>

<body>
    <h1 class="text-center">RSS Feeder</h1>
    <div class="container">
        <form action="index.php" method="post">
            <div class="form-group">
                <label for="url"></label>
                <div class="row justify-content-center">
                    <div class="col-4">
                        <input type="text" class="form-control" name="rssurl" placeholder="Enter the url you want RSS from">
                    </div>
                </div>
                </label>
            </div>
            <div class="row my-1 ">
                <div class="d-grid gap-2 col-4 mx-auto text-center">
                    <input type="submit" class=" btn btn-primary" value="submit" name="submit">
                </div>
            </div>
        </form>
        <div class="content container-fluid">
            <div class="row justify-content-center align-items-center">
                <?php if (isset($_POST['submit'])) {
                    echo '<h2 class="text-center">'. 'Fed from ' . '<strong>'. domain($_POST['rssurl']). '</strong>' . '</h2>';
                    $result = rss($_POST['rssurl']);
                    foreach ($result as $results) {
                        echo '<div class=col>';
                        echo '<div class="card mx-1 my-1" style="width: 18rem; ">';
                        echo '<div class="card-body">';
                        echo '<h5 class="card-title text-center" style="font-size: 1rem;">' . '<strong>'. $results['title'] . '</strong>' . '</h5>';
                        echo '<p class="card-text text-center">' . $results['description'] . '</p>';
                        echo "<a href='" . $results['link'] . "' class='card-link' >" . "Link" . "</a>";
                        echo '</div>';
                        echo '</div>';
                        echo '</div>';
                    }
                } ?>
            </div>
        </div>
    </div>
</body>

</html>