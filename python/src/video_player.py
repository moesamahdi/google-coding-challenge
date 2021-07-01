"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random ,re

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._curr_playing = None
        self._playing_state = False
        self._pause_state = False
        self._playlists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for vid in self._video_library.get_all_videos():
            print("  " , vid.title , " (" , vid.video_id , ") " ,
                "[" , sep="" , end="")
            for tag in vid.tags: 
                print(tag , end="")
                if tag != vid.tags[-1]:
                    print(" " , end="")
            print("]")


    def is_playing(self , video_id):
        self._curr_playing = video_id
        self._playing_state = True


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # Check if submited video id is valid 
        bool_list = []
        for vid_id in self._video_library.get_video_ids():
            if video_id == vid_id:
                bool_list.append(True)
            else:
                bool_list.append(False)
        if not any(bool_list):
            print("Cannot play video: Video does not exist")
            return None

        if self._playing_state == True:
            vid_title = self._video_library.get_video(self._curr_playing).title
            print("Stopping video:" , vid_title )
            self._pause_state = False

        self.is_playing(video_id)
        
        vid_title = self._video_library.get_video(self._curr_playing).title
        print( "Playing video:" , vid_title )


    def stop_video(self):
        """Stops the current video."""
        
        if self._playing_state == False:
            prinlt("Cannot stop video: No video is currently playing")
        else:
            vid_title = self._video_library.get_video(self._curr_playing).title
            print("Stopping video:" , vid_title)
            self._playing_state = False
            self._pause_state = False


    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video = random.choice(self._video_library.get_video_ids())
        self.play_video(random_video)


    def pause_video(self):
        """Pauses the current video."""

        if self._playing_state == False:
            print("Cannot pause video: No video is currently playing")

        elif self._playing_state == True and self._pause_state == True:
            vid_title = self._video_library.get_video(self._curr_playing).title
            print("Video already paused:" , vid_title )

        elif self._playing_state == True and self._pause_state == False:
            vid_title = self._video_library.get_video(self._curr_playing).title
            print("Pausing video:" , vid_title)
            self._pause_state = True


    def continue_video(self):
        """Resumes playing the current video."""

        if self._playing_state == False:
            print("Cannot continue video: No video is currently playing")

        elif self._playing_state == True and self._pause_state == False:
            print("Cannot continue video: Video is not paused")

        elif self._playing_state == True and self._pause_state == True:
            vid_title = self._video_library.get_video(self._curr_playing).title
            print("Continuing video:" , vid_title)
            self._pause_state = False


    def show_playing(self):
        """Displays video currently playing."""

        if self._playing_state == False:
            print("No video is currently playing")
            return None

        curr_video = self._video_library.get_video(self._curr_playing)
        print("Currently playing: " , curr_video.title , " (" ,
            curr_video.video_id , ") " , "[" , sep="" , end="" )
        for tag in curr_video.tags: 
            print(tag , end="")
            if tag != curr_video.tags[-1]:
                print(" " , end="")
        print("]" , end="")
        if self._pause_state == True:
            print(" - PAUSED")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if re.search(r'\s' , playlist_name):
            return None

        elif len(self._playlists) > 0:
            for pl in self._playlists:
                if pl.name.lower() == playlist_name.lower():
                    print("Cannot create playlist: A playlist with the same name already exists")
                    return None

        playlist = Playlist(playlist_name)
        self._playlists.append(playlist)
        print("Successfully created new playlist:" , playlist.name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        

        for pl in self._playlists:
            if playlist_name.lower() == pl.name.lower(): 
                # Check if submited video id is valid 
                bool_list = []
                for vid_id in self._video_library.get_video_ids():
                    if video_id == vid_id:
                        bool_list.append(True)
                    else:
                        bool_list.append(False)
                if not any(bool_list):
                    print("Cannot add video to ", playlist_name , ": Video does not exist" , sep="")
                    return None

                for v in pl.get_videos():
                    if v.video_id == video_id:
                        print("Cannot add video to " , playlist_name , ": Video already added" , sep="")
                        return None

                vid = self._video_library.get_video(video_id)
                pl.add_video(vid)
                print("Added video to " , playlist_name , ": " , vid.title , sep="")
                return None

        print("Cannot add video to " , playlist_name , ": Playlist does not exist" , sep="")


    def show_all_playlists(self):
        """Display all playlists."""

        self._playlists.sort(key=lambda x: x.name)

        if len(self._playlists) == 0:
            print("No playlists exist yet")
            return None

        print("Showing all playlists:")
        for pl in self._playlists:
            print("  " , pl.name , sep="")



    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for pl in self._playlists:
            if playlist_name.lower() == pl.name.lower():
                print("Showing playlist:" , playlist_name)
                if len(pl.get_videos()) == 0:
                    print("  No videos here yet")
                    return None
                for vid in pl.get_videos():
                    print("  " , vid.title , " (" , vid.video_id , ") " ,
                        "[" , sep="" , end="")
                    for tag in vid.tags: 
                        print(tag , end="")
                        if tag != vid.tags[-1]:
                            print(" " , end="")
                    print("]")
                return None

        print("Cannot show playlist " , playlist_name , ": Playlist does not exist" , sep="")


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        for pl in self._playlists:
            if playlist_name.lower() == pl.name.lower():
                
                for v in pl.get_videos():
                    if v.video_id == video_id:
                        vid = self._video_library.get_video(video_id)
                        pl.remove_video(vid)
                        print("Removed video from " , playlist_name , ": " , vid.title , sep="")
                        return None

                bool_list = []
                for vid_id in self._video_library.get_video_ids():
                    if video_id == vid_id:
                        bool_list.append(True)
                    else:
                        bool_list.append(False)
                if not any(bool_list):
                    print("Cannot remove video from ", playlist_name , ": Video does not exist" , sep="")
                    return None

                print("Cannot remove video from " , playlist_name , ": Video is not in playlist" , sep="")
                return None
                    
        print("Cannot remove video from " , playlist_name , ": Playlist does not exist" , sep="")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for pl in self._playlists:
            if playlist_name.lower() == pl.name.lower():
                pl.remove_all_videos()
                print("Successfully removed all videos from" , playlist_name)
                return None

        print("Cannot clear playlist " , playlist_name , ": Playlist does not exist" , sep="")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for pl in self._playlists:
            if playlist_name.lower() == pl.name.lower():
                self._playlists.remove(pl)
                print("Deleted playlist:" , playlist_name)
                return None
        print("Cannot delete playlist " , playlist_name , ": Playlist does not exist" , sep="")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        id_container = []
        counter = 0
        match_bool = False
        for vid in self._video_library.get_all_videos():
            if re.search(search_term.lower() , vid.title.lower()):
                counter += 1
                match_bool = True
                id_container.append(vid.video_id)
                if counter == 1:
                    print("Here are the results for " , search_term , ":" , sep="")
                print("  " , counter , ") " , vid.title , " (" , vid.video_id , ") " , "[" , sep="" , end="")
                for tag in vid.tags: 
                    print(tag , end="")
                    if tag != vid.tags[-1]:
                        print(" " , end="")
                print("]")
        if match_bool == False:
            print("No search results for" , search_term)
            return None

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        id_choice = input()
        try:
            self.play_video(id_container[int(id_choice)-1])
        except:
            return None


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        id_container = []
        counter = 0
        match_bool = False
        for vid in self._video_library.get_all_videos():
            if len(list(filter(re.compile(video_tag.lower()).match , [x.lower() for x in vid.tags] ))) > 0:
                counter += 1
                match_bool = True
                id_container.append(vid.video_id)
                if counter == 1:
                    print("Here are the results for " , video_tag , ":" , sep="")
                print("  " , counter , ") " , vid.title , " (" , vid.video_id , ") " , "[" , sep="" , end="")
                for tag in vid.tags: 
                    print(tag , end="")
                    if tag != vid.tags[-1]:
                        print(" " , end="")
                print("]")
        if match_bool == False:
            print("No search results for" , video_tag)
            return None

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        id_choice = input()
        try:
            self.play_video(id_container[int(id_choice)-1])
        except:
            return None


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")


    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
