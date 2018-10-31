var c = document.createElement( 'canvas' ),
    ctx = c.getContext( '2d' ),
    rows = cols = 36,
    gap = 1,
    grays = [
      [ 26, 29 ],
      [ 32, 37 ],
      [ 42, 50 ],
      [ 46, 56 ],
      [ 54, 66 ]
    ],
    sizes = [ 21, 24, 26 ],
    frequency = [ false, 30, 9 ],
    cw = ch = c.width = c.height = ( sizes[ 0 ] + gap ) * rows;

function random( max, min ) {
  var min = min || 0;
  return Math.random() * ( max - min ) + min;
}

function cell( x, y, size ) {
  var gray = Math.floor( random( grays.length ) ),
      fill = grays[ gray ][ 0 ],
      stroke = grays[ gray ][ 1 ];
  ctx.fillStyle = 'rgb(' + fill + ', ' + fill + ', ' + fill + ')';
  ctx.strokeStyle = 'rgb(' + stroke + ', ' + stroke + ', ' + stroke + ')';
  ctx.fillRect( x, y, size, size );
  ctx.strokeRect( x + 0.5, y + 0.5, size - 1, size - 1 );
}

function generate() {
  var store = [];

  ctx.fillStyle = 'rgb(18, 18, 18)';
  ctx.fillRect( 0, 0, cw, ch );

  for( var x = 0; x < cols; x ++ ){
    for( var y = 0; y < rows; y ++ ){
      cell(
        ( x * sizes[ 0 ] ) + ( x * gap ),
        ( y * sizes[ 0 ] ) + ( y * gap ),
        sizes[ 0 ]
      );
    }
  }

  for( var freq = 0; freq < frequency.length; freq++ ) {
    if( frequency[ freq ] ){
      for( var i = 0; i < frequency[ freq ]; ) {
        var canDraw = true,
            sizeNew = sizes[ freq ],
            pad = Math.ceil( ( sizeNew / cw ) * rows );
            xNew = Math.floor( random( 1, cols - pad ) ) * ( ch / cols ),
            yNew = Math.floor( random( 1, rows - pad ) ) * ( cw / rows ),
            storeLength = store.length;
        if( storeLength ) {
          for( var j = 0; j < storeLength; j++ ) {
            var storeCell = store[ j ];
            if( !(
              xNew + sizeNew + ( cw / cols ) < storeCell.x ||
              yNew + sizeNew + ( ch / rows ) < storeCell.y ||
              xNew > storeCell.x + storeCell.size + ( cw / cols ) ||
              yNew > storeCell.y + storeCell.size + ( ch / rows )
            ) ) {
              canDraw = false;
              break;
            }
          }
        }
        if( canDraw ) {
          cell( xNew, yNew, sizeNew );
          store.push( { x: xNew, y: yNew, size: sizeNew } );
          i++;
        }
      }
    }
  }

  document.body.style.background = 'url(' + c.toDataURL() + ')';
}

generate();
