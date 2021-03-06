class Joint:
  def __init__(self) -> None:
      
      Hip = 3
      RightUpLeg = 6
      RightLeg = 9
      RightFoot = 12
      LeftUpLeg = 15
      LeftLeg = 18
      LeftFoot = 21
      Spine = 24
      Spine1 = 27
      Spine2 = 30
      Spine3 = 33
      Neck = 36
      Head = 39
      RightShoulder = 42
      RightArm = 45
      RightForeArm = 48
      RightHand = 51
      RightHandThumb1 = 54
      RightHandThumb2 = 57
      RightHandThumb3 = 60
      RightInHandIndex = 63
      RightHandIndex1 = 66
      RightHandIndex2 = 69
      RightHandIndex3 = 72
      RightInHandMiddle = 75
      RightHandMiddle1 = 78
      RightHandMiddle2 = 81
      RightHandMiddle3 = 84
      RightInHandRing = 87
      RightHandRing1 = 90
      RightHandRing2 = 93
      RightHandRing3 = 96
      RightInHandPinky = 99
      RightHandPinky1 = 102
      RightHandPinky2 = 105
      RightHandPinky3 = 108
      LeftShoulder = 111
      LeftArm = 114
      LeftForeArm = 117
      LeftHand = 120
      LeftHandThumb1 = 123
      LeftHandThumb2 = 126
      LeftHandThumb3 = 129
      LeftInHandIndex = 132
      LeftHandIndex1 = 135
      LeftHandIndex2 = 138
      LeftHandIndex3 = 141
      LeftInHandMiddle = 144
      LeftHandMiddle1 = 147
      LeftHandMiddle2 = 150
      LeftHandMiddle3 = 153
      LeftInHandRing = 156
      LeftHandRing1 = 159
      LeftHandRing2 = 162
      LeftHandRing3 = 165
      LeftInHandPinky = 168
      LeftHandPinky1 = 171
      LeftHandPinky2 = 174
      LeftHandPinky3 = 177

      self.hip = {'j_num': Hip, 'j_name': 'hip'}
      self.right_up_leg = {'j_num': RightUpLeg, 'j_name': 'right_up_leg'}
      self.right_leg = {'j_num': RightLeg, 'j_name': 'right_leg'}
      self.right_foot = {'j_num': RightFoot, 'j_name': 'right_foot'}
      self.left_up_leg = {'j_num': LeftUpLeg, 'j_name': 'left_up_leg'}
      self.left_leg = {'j_num': LeftLeg, 'j_name': 'left_leg'}
      self.left_foot = {'j_num': LeftFoot, 'j_name': 'left_foot'}
      self.spine = {'j_num': Spine, 'j_name': 'spine'}
      self.spine_1 = {'j_num': Spine1, 'j_name': 'spine1'}
      self.spine_2 = {'j_num': Spine2, 'j_name': 'spine2'}
      self.spine_3 = {'j_num': Spine3, 'j_name': 'spine3'}
      self.neck = {'j_num': Neck, 'j_name': 'neck'}
      self.head = {'j_num': Head, 'j_name': 'head'}
      self.right_shoulder = {'j_num': RightShoulder, 'j_name': 'right_shoulder'}
      self.right_arm = {'j_num': RightArm, 'j_name': 'right_arm'}
      self.right_fore_arm = {'j_num': RightForeArm, 'j_name': 'right_fore_arm'}
      self.right_hand = {'j_num': RightHand, 'j_name': 'right_hand'}
      self.right_hand_thumb1 = {'j_num': RightHandThumb1, 'j_name': 'right_hand_thumb1'}
      self.right_hand_thumb2 = {'j_num': RightHandThumb2, 'j_name': 'right_hand_thumb2'}
      self.right_hand_thumb3 = {'j_num': RightHandThumb3, 'j_name': 'right_hand_thumb3'}
      self.right_in_hand_index = {'j_num': RightInHandIndex, 'j_name': 'right_in_hand_index'}
      self.right_hand_index1 = {'j_num': RightHandIndex1, 'j_name': 'right_hand_index1'}
      self.right_hand_index2 = {'j_num': RightHandIndex2, 'j_name': 'right_hand_index2'}
      self.right_hand_index3 = {'j_num': RightHandIndex3, 'j_name': 'right_hand_index3'}
      self.right_in_hand_middle = {'j_num': RightInHandMiddle, 'j_name': 'right_in_hand_middle'}
      self.right_hand_middle1 = {'j_num': RightHandMiddle1, 'j_name': 'right_hand_middle1'}
      self.right_hand_middle2 = {'j_num': RightHandMiddle2, 'j_name': 'right_hand_middle2'}
      self.right_hand_middle3 = {'j_num': RightHandMiddle3, 'j_name': 'right_hand_middle3'}
      self.right_in_hand_ring = {'j_num': RightInHandRing, 'j_name': 'right_in_hand_ring'}
      self.right_hand_ring1 = {'j_num': RightHandRing1, 'j_name': 'right_hand_ring1'}
      self.right_hand_ring2 = {'j_num': RightHandRing2, 'j_name': 'right_hand_ring2'}
      self.right_hand_ring3 = {'j_num': RightHandRing3, 'j_name': 'right_hand_ring3'}
      self.right_in_hand_pinky = {'j_num': RightInHandPinky, 'j_name': 'right_in_hand_pinky'}
      self.right_hand_pinky1 = {'j_num': RightHandPinky1, 'j_name': 'right_hand_pinky1'}
      self.right_hand_pinky2 = {'j_num': RightHandPinky2, 'j_name': 'right_hand_pinky2'}
      self.right_hand_pinky3 = {'j_num': RightHandPinky3, 'j_name': 'right_hand_pinky3'}      
      self.left_shoulder = {'j_num': LeftShoulder, 'j_name': 'left_shoulder'}
      self.left_arm = {'j_num': LeftArm, 'j_name': 'left_arm'}
      self.left_fore_arm = {'j_num': LeftForeArm, 'j_name': 'left_fore_arm'}
      self.left_hand = {'j_num': LeftHand, 'j_name': 'left_hand'}
      self.left_hand_thumb1 = {'j_num': LeftHandThumb1, 'j_name': 'left_hand_thumb1'}
      self.left_hand_thumb2 = {'j_num': LeftHandThumb2, 'j_name': 'left_hand_thumb2'}
      self.left_hand_thumb3 = {'j_num': LeftHandThumb3, 'j_name': 'left_hand_thumb3'}
      self.left_in_hand_index = {'j_num': LeftInHandIndex, 'j_name': 'left_in_hand_index'}
      self.left_hand_index1 = {'j_num': LeftHandIndex1, 'j_name': 'left_hand_index1'}
      self.left_hand_index2 = {'j_num': LeftHandIndex2, 'j_name': 'left_hand_index2'}
      self.left_hand_index3 = {'j_num': LeftHandIndex3, 'j_name': 'left_hand_index3'}
      self.left_in_hand_middle = {'j_num': LeftInHandMiddle, 'j_name': 'left_in_hand_middle'}
      self.left_hand_middle1 = {'j_num': LeftHandMiddle1, 'j_name': 'left_in_hand_middle1'}
      self.left_hand_middle2 = {'j_num': LeftHandMiddle2, 'j_name': 'left_in_hand_middle2'}
      self.left_hand_middle3 = {'j_num': LeftHandMiddle3, 'j_name': 'left_in_hand_middle3'}
      self.left_in_hand_ring = {'j_num': LeftInHandRing, 'j_name': 'left_in_hand_ring'}
      self.left_hand_ring1 = {'j_num': LeftHandRing1, 'j_name': 'left_hand_ring1'}
      self.left_hand_ring2 = {'j_num': LeftHandRing2, 'j_name': 'left_hand_ring2'}
      self.left_hand_ring3 = {'j_num': LeftHandRing3, 'j_name': 'left_hand_ring3'}
      self.left_in_hand_pinky = {'j_num': LeftInHandPinky, 'j_name': 'left_in_hand_pinky'}
      self.left_hand_pinky1 = {'j_num': LeftHandPinky1, 'j_name': 'left_hand_pinky1'}
      self.left_hand_pinky2 = {'j_num': LeftHandPinky2, 'j_name': 'left_hand_pinky2'}
      self.left_hand_pinky3 = {'j_num': LeftHandPinky3, 'j_name': 'left_hand_pinky3'}

      self.joint = {
        'hip' : self.hip,
        'right_up_leg' : self.right_up_leg,
        'right_leg' : self.right_leg,
        'right_foot' : self.right_foot,
        'left_up_leg' : self.left_up_leg,
        'left_leg' : self.left_leg,
        'left_foot' : self.left_foot,
        'spine' : self.spine,
        'spine_1' : self.spine_1,
        'spine_2' : self.spine_2,
        'spine_3' : self.spine_3,
        'neck' : self.neck,
        'head' : self.head,
        'right_shoulder' : self.right_shoulder,
        'right_arm' : self.right_arm,
        'right_fore_arm' : self.right_fore_arm,
        'right_hand' : self.right_hand,
        'right_hand_thumb1' : self.right_hand_thumb1,
        'right_hand_thumb2' : self.right_hand_thumb2,
        'right_hand_thumb3' : self.right_hand_thumb3,
        'right_in_hand' : self.right_in_hand_index,
        'right_hand_index1' : self.right_hand_index1,
        'right_hand_index2' : self.right_hand_index2,
        'right_hand_index3' : self.right_hand_index3,
        'right_in_hand_middle' : self.right_in_hand_middle,
        'right_hand_middle1' : self.right_hand_middle1,
        'right_hand_middle2' : self.right_hand_middle2,
        'right_hand_middle3' : self.right_hand_middle3,
        'right_in_hand_ring' : self.right_in_hand_ring,
        'right_hand_ring1' : self.right_hand_ring1,
        'right_hand_ring2' : self.right_hand_ring2,
        'right_hand_ring3' : self.right_hand_ring3,
        'right_in_hand_pinky' : self.right_in_hand_pinky,
        'right_hand_pinky1' : self.right_hand_pinky1,
        'right_hand_pinky2' : self.right_hand_pinky2,
        'right_hand_pinky3' : self.right_hand_pinky3,
        'left_shoulder' : self.left_shoulder,
        'left_arm' : self.left_arm,
        'left_fore_arm' : self.left_fore_arm,
        'left_hand' : self.left_hand,
        'left_hand_thumb1' : self.left_hand_thumb1,
        'left_hand_thumb2' : self.left_hand_thumb2,
        'left_hand_thumb3' : self.left_hand_thumb3,
        'left_in_hand' : self.left_in_hand_index,
        'left_hand_index1' : self.left_hand_index1,
        'left_hand_index2' : self.left_hand_index2,
        'left_hand_index3' : self.left_hand_index3,
        'left_in_hand_middle' : self.left_in_hand_middle,
        'left_hand_middle1' : self.left_hand_middle1,
        'left_hand_middle2' : self.left_hand_middle2,
        'left_hand_middle3' : self.left_hand_middle3,
        'left_in_hand_ring' : self.left_in_hand_ring,
        'left_hand_ring1' : self.left_hand_ring1,
        'left_hand_ring2' : self.left_hand_ring2,
        'left_hand_ring3' : self.left_hand_ring3,
        'left_in_hand_pinky' : self.left_in_hand_pinky,
        'left_hand_pinky1' : self.left_hand_pinky1,
        'left_hand_pinky2' : self.left_hand_pinky2,
        'left_hand_pinky3' : self.left_hand_pinky3,
      }
