scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles12, function (sprite, location) {
    info.setScore(2)
    info.startCountdown(15)
    tiles.setTilemap(tilemap`Level`)
    tiles.placeOnRandomTile(mySprite, myTiles.tile15)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function (sprite, location) {
    info.setScore(3)
    info.startCountdown(15)
    tiles.setTilemap(tilemap`Level_0`)
    tiles.placeOnRandomTile(mySprite, sprites.dungeon.floorDark5)
    music.magicWand.play()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    info.setScore(4)
    tiles.setTilemap(tilemap`Level_1`)
    tiles.placeOnRandomTile(mySprite, sprites.dungeon.floorLight0)
    info.stopCountdown()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorOpenNorth, function (sprite, location) {
    info.setScore(1)
    info.startCountdown(20)
    tiles.setTilemap(tilemap`Level_2`)
    tiles.placeOnRandomTile(mySprite, sprites.castle.tileGrass1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    info.setScore(5)
    tiles.setTilemap(tilemap`Level_3`)
    tiles.placeOnRandomTile(mySprite, myTiles.transparency16)
})
let mySprite: Sprite = null
mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . 7 7 7 . . . . . . . . . . 
    . . 2 7 f 7 7 7 7 7 7 7 . . . . 
    . . . 7 7 7 . . . . . 7 7 7 7 . 
    . . . . . . . . . . . . . . 7 . 
    . . . . . . . . . . . . . . 7 . 
    . . . . . . . . . 7 7 . . 7 7 . 
    . . 7 7 7 7 7 7 7 . 7 7 7 7 . . 
    . 7 7 . . . . . . . . . . . . . 
    . 7 7 . 7 7 7 7 7 . . . . . . . 
    . . 7 . 7 . . . 7 7 7 7 7 7 . . 
    . . 7 7 7 . . . . . . 7 7 7 . . 
    . . . . . . . . . 7 7 7 . . . . 
    . . . . . 7 7 7 7 7 . . . . . . 
    . . . . 7 7 . . . . . . . . . . 
    . . . 7 7 . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.setTilemap(tilemap`Level_4`)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.floorDark4)
scene.cameraFollowSprite(mySprite)
info.startCountdown(25)
