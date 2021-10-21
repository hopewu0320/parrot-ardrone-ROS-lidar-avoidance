# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_video_stream.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class navdata_video_stream(genpy.Message):
  _md5sum = "caf560356d435eb563ce5b9e8278da00"
  _type = "ardrone_autonomy/navdata_video_stream"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
uint8 quant
uint32 frame_size
uint32 frame_number
uint32 atcmd_ref_seq
uint32 atcmd_mean_ref_gap
float32 atcmd_var_ref_gap
uint32 atcmd_ref_quality
uint32 desired_bitrate
int32 data2
int32 data3
int32 data4
int32 data5
uint32 fifo_queue_level

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','drone_time','tag','size','quant','frame_size','frame_number','atcmd_ref_seq','atcmd_mean_ref_gap','atcmd_var_ref_gap','atcmd_ref_quality','desired_bitrate','data2','data3','data4','data5','fifo_queue_level']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','uint8','uint32','uint32','uint32','uint32','float32','uint32','uint32','int32','int32','int32','int32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,quant,frame_size,frame_number,atcmd_ref_seq,atcmd_mean_ref_gap,atcmd_var_ref_gap,atcmd_ref_quality,desired_bitrate,data2,data3,data4,data5,fifo_queue_level

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_video_stream, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.quant is None:
        self.quant = 0
      if self.frame_size is None:
        self.frame_size = 0
      if self.frame_number is None:
        self.frame_number = 0
      if self.atcmd_ref_seq is None:
        self.atcmd_ref_seq = 0
      if self.atcmd_mean_ref_gap is None:
        self.atcmd_mean_ref_gap = 0
      if self.atcmd_var_ref_gap is None:
        self.atcmd_var_ref_gap = 0.
      if self.atcmd_ref_quality is None:
        self.atcmd_ref_quality = 0
      if self.desired_bitrate is None:
        self.desired_bitrate = 0
      if self.data2 is None:
        self.data2 = 0
      if self.data3 is None:
        self.data3 = 0
      if self.data4 is None:
        self.data4 = 0
      if self.data5 is None:
        self.data5 = 0
      if self.fifo_queue_level is None:
        self.fifo_queue_level = 0
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.quant = 0
      self.frame_size = 0
      self.frame_number = 0
      self.atcmd_ref_seq = 0
      self.atcmd_mean_ref_gap = 0
      self.atcmd_var_ref_gap = 0.
      self.atcmd_ref_quality = 0
      self.desired_bitrate = 0
      self.data2 = 0
      self.data3 = 0
      self.data4 = 0
      self.data5 = 0
      self.fifo_queue_level = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d2HB4If2I4iI().pack(_x.drone_time, _x.tag, _x.size, _x.quant, _x.frame_size, _x.frame_number, _x.atcmd_ref_seq, _x.atcmd_mean_ref_gap, _x.atcmd_var_ref_gap, _x.atcmd_ref_quality, _x.desired_bitrate, _x.data2, _x.data3, _x.data4, _x.data5, _x.fifo_queue_level))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.drone_time, _x.tag, _x.size, _x.quant, _x.frame_size, _x.frame_number, _x.atcmd_ref_seq, _x.atcmd_mean_ref_gap, _x.atcmd_var_ref_gap, _x.atcmd_ref_quality, _x.desired_bitrate, _x.data2, _x.data3, _x.data4, _x.data5, _x.fifo_queue_level,) = _get_struct_d2HB4If2I4iI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d2HB4If2I4iI().pack(_x.drone_time, _x.tag, _x.size, _x.quant, _x.frame_size, _x.frame_number, _x.atcmd_ref_seq, _x.atcmd_mean_ref_gap, _x.atcmd_var_ref_gap, _x.atcmd_ref_quality, _x.desired_bitrate, _x.data2, _x.data3, _x.data4, _x.data5, _x.fifo_queue_level))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.drone_time, _x.tag, _x.size, _x.quant, _x.frame_size, _x.frame_number, _x.atcmd_ref_seq, _x.atcmd_mean_ref_gap, _x.atcmd_var_ref_gap, _x.atcmd_ref_quality, _x.desired_bitrate, _x.data2, _x.data3, _x.data4, _x.data5, _x.fifo_queue_level,) = _get_struct_d2HB4If2I4iI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d2HB4If2I4iI = None
def _get_struct_d2HB4If2I4iI():
    global _struct_d2HB4If2I4iI
    if _struct_d2HB4If2I4iI is None:
        _struct_d2HB4If2I4iI = struct.Struct("<d2HB4If2I4iI")
    return _struct_d2HB4If2I4iI
