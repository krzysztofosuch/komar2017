import json
import os
import pygame
import uuid
import zipfile


class Pyxel:
    def __init__(self, file_location, tmp_dir):
        self.location = tmp_dir + '/' + str(uuid.uuid4())
        os.mkdir(self.location)

        ref = zipfile.ZipFile(file_location, 'r')
        ref.extractall(self.location)
        ref.close()

        with open(self.location + '/docData.json', 'r') as f:
            data = json.load(f)

        self.layers = []
        tiles = dict()

        for index, layer in data['canvas']['layers'].items():
            for tile_ref in layer['tileRefs'].values():
                if tile_ref['index'] not in tiles:
                    tiles[tile_ref['index']] = Tile(self.location, tile_ref['index'])

        for index, layer in data['canvas']['layers'].items():
            self.layers.append(Layer(self.location, index, layer['tileRefs'], tiles))


class Layer:
    def __init__(self, file_location, index, tile_refs, tiles):
        self.index = index
        path = os.path.join(file_location, 'layer' + str(self.index) + '.png')
        self.image = pygame.image.load(path)
        self.tiles = []

        for ref in tile_refs.values():
            ref_tile = RefTile(tiles[ref['index']])
            self.tiles.append(ref_tile)


class RefTile:
    def __init__(self, tile):
        self.tile = tile


class Tile:
    def __init__(self, file_location, index):
        self.index = index
        path = os.path.join(file_location, 'tile' + str(self.index) + '.png')
        self.image = pygame.image.load(path)
