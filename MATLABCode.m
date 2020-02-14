clc
close all 
FileConverterFxn( 'data_20190731_02_matrix.mat','data_20190731_02.dat','data_20190731_02_movie.avi',64,64,150,2000,33,1,64,64,1,1 ); % 12 W
tmpMatrix = importdata( 'data_20190731_02_matrix.mat' );
%figure
%imagesc( tmpMatrix( :, :, 390 ) );
%fclose( datFile );

function FileConverterFxn( filePath, datFileName, movieName, imgH, imgW, startFr, endFr ,cropx1, cropy1, cropx2, cropy2, save_Nosave_Flag, save_Nosave_Movie_Flag )
    datFile = fopen( datFileName, 'r' );
    frewind( datFile );
    matrix = zeros( cropy2-cropy1+1, cropx2-cropx1+1, endFr-startFr+1 )
    matrix1 = zeros( cropy2-cropy1+1, cropx2-cropx1+1 )
    
    frameSize = 48 + (imgW*imgH*2);
    for fr = startFr:151
        offset = 2060 + 48 + (frameSize * fr);
        fseek( datFile, offset, 'bof' );
        temp = zeros( imgH, imgW );
        temp = fread( datFile, [imgW imgH], '*int16', 'l' );
        for y = cropy1 : cropy2
            for x = cropx1 : cropx2
                matrix( y-cropy1+1, x-cropx1+1, fr-startFr+1 ) = temp ( y, x );
                matrix1( y-cropy1+1, x-cropx1+1) = temp ( y, x );
        %figure        
        %imshow(matrix(y-cropy1+1, x-cropx1+1, fr-startFr+1 ))        
            end
        end
    end
    m=matrix(1,1,1)
    disp(m)
    %save('m1.mat','matrix')
    

    r = matrix(:,:,48);
    %figure
    %imshow(r)
    %if save_Nosave_Flag == 1
     %   save( filePath, 'matrix' );
    %end
    if save_Nosave_Movie_Flag == 1
        %Un-comment the following code if you want a gray scale video
        %instead of full color video (You would also need to re-comment the
        %code from line 78 to 92
        %{
        matrix = matrix / max( matrix( : ) )
        VidObj = VideoWriter( movieName, 'Uncompressed AVI' );
        VidObj.FrameRate = 30;
        open( VidObj );
        for f = 1:size( matrix, 3 )
            writeVideo( VidObj, matrix( :, :, f ) );
        end
        close( VidObj );
        %}
%         VidObj = VideoWriter(movieName, 'Uncompressed AVI');
%         VidObj.FrameRate = 30;
%         open( VidObj );
%         maxV = max(matrix(:));
%         % disp (maxV);
%         scale = maxV / 255;
%         % scale = 7.4353
%         for fr = 1 : (endFr - startFr + 1)
%             for y = 1 : (cropy2 - cropy1 + 1)
%                 for x = 1 : (cropx2 - cropx1 + 1)
%                     matrix( y, x, fr ) = matrix( y, x, fr ) / scale;
%                     if matrix( y, x, fr ) < 1
%                         matrix( y, x, fr ) = 1;
%                     end
%                 end
%             end
%         end
%         M = permute( matrix, [1 2 4 3] );
%         movie = immovie( M, parula );
%         implay( movie );
%         writeVideo( VidObj, movie );
%         close( VidObj );
%     end
    end
end


