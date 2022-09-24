class TV:
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        self.channelList = [1, 2, 3, 12, 18, 43, 78]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOL_MIN = 0
        self.VOL_MAX = 10
        self.volume = self.VOL_MAX

    def power(self):
        self.isOn = not self.isOn

    def volume_up(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOL_MAX:
            self.volume += 1

    def volume_down(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOL_MIN:
            self.volume -= 1

    def channel_up(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0

    def channel_down(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def set_channel(self, new_channel):
        if not self.isOn:
            return
        if new_channel in self.channelList:
            self.channelIndex = self.channelList.index(new_channel)

    def status(self):
        print()
        print(f"        The brand of the TV is: {self.brand}")
        print(f"        The location of the TV is: {self.location}")
        if self.isOn:
            print("        The TV is currently On")
            print(f"        Channel is: {self.channelList[self.channelIndex]}")
            if self.isMuted:
                print(f"        Volume is: {self.volume} (soung is muted)")
            else:
                print(f"        Volume is: {self.volume}")
        else:
            print("        The TV is currently Off")


tv1 = TV("Samsung", "Bedroom")
tv2 = TV("Sony", "Livingroom")

tv1.power()
tv1.channel_up()
tv1.channel_up()
tv1.volume_down()
tv1.volume_down()
tv1.status()


tv2.status()
