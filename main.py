def on_overlap_tile(sprite, location):
    info.set_score(2)
    info.start_countdown(15)
    tiles.set_tilemap(tilemap("""
        Level
    """))
    tiles.place_on_random_tile(mySprite, myTiles.tile15)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles12,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    info.set_score(3)
    info.start_countdown(15)
    tiles.set_tilemap(tilemap("""
        Level_0
    """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_dark5)
    music.magic_wand.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    info.set_score(4)
    tiles.set_tilemap(tilemap("""
        Level_1
    """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_light0)
    info.stop_countdown()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    info.set_score(1)
    info.start_countdown(20)
    tiles.set_tilemap(tilemap("""
        Level_2
    """))
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_north,
    on_overlap_tile4)

def on_overlap_tile5(sprite, location):
    info.set_score(5)
    tiles.set_tilemap(tilemap("""
        Level_3
    """))
    tiles.place_on_random_tile(mySprite, myTiles.transparency16)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile5)

mySprite: Sprite = None
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_tilemap(tilemap("""
    Level_4
"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_dark4)
scene.camera_follow_sprite(mySprite)
info.start_countdown(25)