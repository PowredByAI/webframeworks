<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Psr\Http\Server\RequestHandlerInterface;
use Slim\Factory\AppFactory;

require __DIR__ . '/../vendor/autoload.php';

$app = AppFactory::create();

//cors
$app->add(function (Request $request, RequestHandlerInterface $handler): Response {
    $response = $handler->handle($request);
    $response = $response->withHeader('Access-Control-Allow-Origin', '*');
    return $response;
});

$app->get('/', function (Request $request, Response $response, $args) {
    $response->getBody()->write("Hi~");
    return $response;
});

$app->run();
