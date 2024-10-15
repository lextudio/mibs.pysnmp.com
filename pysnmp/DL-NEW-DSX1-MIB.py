# SNMP MIB module (DL-NEW-DSX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL-NEW-DSX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:30 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class PortId(Integer32):
    """Custom type PortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("aux", 2),
          ("commPort", 8),
          ("data1", 11),
          ("data10", 20),
          ("data11", 21),
          ("data12", 22),
          ("data13", 23),
          ("data14", 24),
          ("data15", 25),
          ("data16", 26),
          ("data17", 27),
          ("data18", 28),
          ("data19", 29),
          ("data2", 12),
          ("data20", 30),
          ("data21", 31),
          ("data22", 32),
          ("data23", 33),
          ("data24", 34),
          ("data25", 35),
          ("data26", 36),
          ("data27", 37),
          ("data28", 38),
          ("data29", 39),
          ("data3", 13),
          ("data30", 40),
          ("data31", 41),
          ("data32", 42),
          ("data4", 14),
          ("data5", 15),
          ("data6", 16),
          ("data7", 17),
          ("data8", 18),
          ("data9", 19),
          ("ethPort", 7),
          ("ext-clock", 10),
          ("int-clock", 9),
          ("mainNet", 1),
          ("noPort", 43),
          ("otherNet", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6))
    )





class AlarmType(Integer32):
    """Custom type AlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("detectedAIS", 4),
          ("detectedCntlCardMissing", 11),
          ("detectedExternalAlarm", 5),
          ("detectedPSfailure", 10),
          ("detectedYellow", 3),
          ("exceededBpvThreshold", 6),
          ("exceededCrcThreshold", 8),
          ("exceededIbCrcThreshold", 13),
          ("exceededOofThreshold", 7),
          ("lmiSpoofing", 15),
          ("lostDlcFdlLink", 12),
          ("lostDlcInbandLink", 14),
          ("lostSignal", 1),
          ("lostSync", 2),
          ("remoteAlarmBitSet", 9))
    )





class TestType(Integer32):
    """Custom type TestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("dteLoopback", 5),
          ("dteNetLoopback", 24),
          ("lampTest", 31),
          ("loopDownRemote", 7),
          ("loopUpRemote", 6),
          ("netLoopback", 3),
          ("noTest", 1),
          ("payloadLoopback", 4),
          ("reserved1", 25),
          ("reserved2", 26),
          ("reserved3", 27),
          ("reserved4", 28),
          ("reserved5", 29),
          ("reserved6", 30),
          ("selfTest", 2),
          ("send1in1Pattern", 10),
          ("send1in3Pattern", 11),
          ("send1in5Pattern", 12),
          ("send1in8Pattern", 9),
          ("send2in3Pattern", 14),
          ("send3in24Pattern", 16),
          ("send4in5Pattern", 15),
          ("sendAPatternError", 23),
          ("sendAllOnePattern", 17),
          ("sendAllZeroPattern", 18),
          ("sendQrwPattern", 8),
          ("sendSmartJackReset", 22),
          ("sendSmartJackSet", 21),
          ("sendUser1Pattern", 19),
          ("sendUser2Pattern", 20))
    )





class LoopCodeType(Integer32):
    """Custom type LoopCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("disable", 7),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("standard", 1),
          ("v54", 3))
    )





class UnitStatusItem(Integer32):
    """Custom type UnitStatusItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("noClock", 2),
          ("normal", 1),
          ("reserved1", 32),
          ("reserved2", 64),
          ("reserved3", 128),
          ("reserved4", 256),
          ("reserved5", 512),
          ("sendKeepAlive", 8),
          ("sendYellowAlarm", 16),
          ("testInProgress", 4))
    )





class PortStatusItem(Integer32):
    """Custom type PortStatusItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("blueAlarmDetected", 5),
          ("eBitReceived", 10),
          ("excessiveErrorRate", 8),
          ("localTest", 9),
          ("lossOfSignal", 2),
          ("lossOfSync", 3),
          ("normal", 1),
          ("reserved1", 11),
          ("reserved2", 12),
          ("reserved3", 13),
          ("reserved4", 14),
          ("resetCodeReceived", 7),
          ("setCodeReceived", 6),
          ("yellowAlarmDetected", 4))
    )





class FramedUnframed(Integer32):
    """Custom type FramedUnframed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framed", 1),
          ("unframed", 2))
    )





class RemoteCommunicationsMode(Integer32):
    """Custom type RemoteCommunicationsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansi-T1-403", 4),
          ("att-TR54016", 3),
          ("digital-link", 2),
          ("none", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Digital_link_ObjectIdentity = ObjectIdentity
digital_link = _Digital_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300)
)
_Dl_new_t1_ObjectIdentity = ObjectIdentity
dl_new_t1 = _Dl_new_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200)
)
_DlcUnitHwConfig_ObjectIdentity = ObjectIdentity
dlcUnitHwConfig = _DlcUnitHwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 1)
)


class _DlcUnitModelType_Type(Integer32):
    """Custom type dlcUnitModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dl100Encore", 2),
          ("dl1200", 3),
          ("dl2400", 4),
          ("dl4200E1", 18),
          ("dl4200T1", 17),
          ("dl5440E1", 20),
          ("dl5440T1", 19),
          ("dl600", 5),
          ("dl600Encore", 6),
          ("ensembleE1Encore", 10),
          ("ensembleEncore", 7),
          ("ensembleT1CSU", 12),
          ("soloE1Encore", 9),
          ("soloEncore", 8),
          ("soloSelectE1", 16),
          ("soloSelectE1Module", 14),
          ("soloSelectT1", 15),
          ("soloSelectT1Module", 13),
          ("soloT1CSU", 11),
          ("vxEncore", 1))
    )


_DlcUnitModelType_Type.__name__ = "Integer32"
_DlcUnitModelType_Object = MibScalar
dlcUnitModelType = _DlcUnitModelType_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 1),
    _DlcUnitModelType_Type()
)
dlcUnitModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitModelType.setStatus("mandatory")


class _DlcUnitHwRev_Type(DisplayString):
    """Custom type dlcUnitHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DlcUnitHwRev_Type.__name__ = "DisplayString"
_DlcUnitHwRev_Object = MibScalar
dlcUnitHwRev = _DlcUnitHwRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 2),
    _DlcUnitHwRev_Type()
)
dlcUnitHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitHwRev.setStatus("mandatory")


class _DlcUnitHwOptions_Type(Integer32):
    """Custom type dlcUnitHwOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DlcUnitHwOptions_Type.__name__ = "Integer32"
_DlcUnitHwOptions_Object = MibScalar
dlcUnitHwOptions = _DlcUnitHwOptions_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 3),
    _DlcUnitHwOptions_Type()
)
dlcUnitHwOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitHwOptions.setStatus("mandatory")


class _DlcUnitSwRev_Type(DisplayString):
    """Custom type dlcUnitSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DlcUnitSwRev_Type.__name__ = "DisplayString"
_DlcUnitSwRev_Object = MibScalar
dlcUnitSwRev = _DlcUnitSwRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 4),
    _DlcUnitSwRev_Type()
)
dlcUnitSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitSwRev.setStatus("mandatory")


class _DlcUnitDataPorts_Type(Integer32):
    """Custom type dlcUnitDataPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DlcUnitDataPorts_Type.__name__ = "Integer32"
_DlcUnitDataPorts_Object = MibScalar
dlcUnitDataPorts = _DlcUnitDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 5),
    _DlcUnitDataPorts_Type()
)
dlcUnitDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitDataPorts.setStatus("mandatory")
_DlcUnitRam_Type = Integer32
_DlcUnitRam_Object = MibScalar
dlcUnitRam = _DlcUnitRam_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 6),
    _DlcUnitRam_Type()
)
dlcUnitRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitRam.setStatus("mandatory")
_DlcUnitRom_Type = Integer32
_DlcUnitRom_Object = MibScalar
dlcUnitRom = _DlcUnitRom_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 7),
    _DlcUnitRom_Type()
)
dlcUnitRom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitRom.setStatus("mandatory")
_DlcUnitFlash_Type = Integer32
_DlcUnitFlash_Object = MibScalar
dlcUnitFlash = _DlcUnitFlash_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 8),
    _DlcUnitFlash_Type()
)
dlcUnitFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitFlash.setStatus("mandatory")


class _DlcUnitSlotNum_Type(Integer32):
    """Custom type dlcUnitSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DlcUnitSlotNum_Type.__name__ = "Integer32"
_DlcUnitSlotNum_Object = MibScalar
dlcUnitSlotNum = _DlcUnitSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 9),
    _DlcUnitSlotNum_Type()
)
dlcUnitSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitSlotNum.setStatus("mandatory")


class _DlcUnitMibRev_Type(DisplayString):
    """Custom type dlcUnitMibRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DlcUnitMibRev_Type.__name__ = "DisplayString"
_DlcUnitMibRev_Object = MibScalar
dlcUnitMibRev = _DlcUnitMibRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 10),
    _DlcUnitMibRev_Type()
)
dlcUnitMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitMibRev.setStatus("mandatory")


class _DlcUnitFeatures_Type(Integer32):
    """Custom type dlcUnitFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("dni", 32),
          ("dte2", 64),
          ("inband", 1),
          ("ipm32", 2),
          ("ipm96", 4),
          ("reserved4", 128),
          ("reserved5", 256),
          ("reserved6", 512),
          ("reserved7", 1024),
          ("reserved8", 2048),
          ("rmon2", 8),
          ("sla", 16))
    )


_DlcUnitFeatures_Type.__name__ = "Integer32"
_DlcUnitFeatures_Object = MibScalar
dlcUnitFeatures = _DlcUnitFeatures_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 1, 11),
    _DlcUnitFeatures_Type()
)
dlcUnitFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitFeatures.setStatus("mandatory")
_DlcUnitConfig_ObjectIdentity = ObjectIdentity
dlcUnitConfig = _DlcUnitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2)
)


class _DlcUnitId_Type(DisplayString):
    """Custom type dlcUnitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_DlcUnitId_Type.__name__ = "DisplayString"
_DlcUnitId_Object = MibScalar
dlcUnitId = _DlcUnitId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 1),
    _DlcUnitId_Type()
)
dlcUnitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitId.setStatus("mandatory")
_DlcUnitProtectMode_Type = Boolean
_DlcUnitProtectMode_Object = MibScalar
dlcUnitProtectMode = _DlcUnitProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 2),
    _DlcUnitProtectMode_Type()
)
dlcUnitProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitProtectMode.setStatus("mandatory")
_DlcUnitYellowEnable_Type = Boolean
_DlcUnitYellowEnable_Object = MibScalar
dlcUnitYellowEnable = _DlcUnitYellowEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 3),
    _DlcUnitYellowEnable_Type()
)
dlcUnitYellowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitYellowEnable.setStatus("mandatory")
_DlcUnitNetPassFdl_Type = PortId
_DlcUnitNetPassFdl_Object = MibScalar
dlcUnitNetPassFdl = _DlcUnitNetPassFdl_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 4),
    _DlcUnitNetPassFdl_Type()
)
dlcUnitNetPassFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitNetPassFdl.setStatus("mandatory")
_DlcUnitMainClockSource_Type = PortId
_DlcUnitMainClockSource_Object = MibScalar
dlcUnitMainClockSource = _DlcUnitMainClockSource_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 5),
    _DlcUnitMainClockSource_Type()
)
dlcUnitMainClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitMainClockSource.setStatus("mandatory")
_DlcUnitAltClockSource_Type = PortId
_DlcUnitAltClockSource_Object = MibScalar
dlcUnitAltClockSource = _DlcUnitAltClockSource_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 6),
    _DlcUnitAltClockSource_Type()
)
dlcUnitAltClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitAltClockSource.setStatus("mandatory")


class _DlcUnitExtClockRate_Type(Integer32):
    """Custom type dlcUnitExtClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 2048),
    )


_DlcUnitExtClockRate_Type.__name__ = "Integer32"
_DlcUnitExtClockRate_Object = MibScalar
dlcUnitExtClockRate = _DlcUnitExtClockRate_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 7),
    _DlcUnitExtClockRate_Type()
)
dlcUnitExtClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExtClockRate.setStatus("mandatory")
_DlcUnitFullBandwidthLoopCode_Type = LoopCodeType
_DlcUnitFullBandwidthLoopCode_Object = MibScalar
dlcUnitFullBandwidthLoopCode = _DlcUnitFullBandwidthLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 8),
    _DlcUnitFullBandwidthLoopCode_Type()
)
dlcUnitFullBandwidthLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitFullBandwidthLoopCode.setStatus("mandatory")
_DlcUnitFractionalLoopCode_Type = LoopCodeType
_DlcUnitFractionalLoopCode_Object = MibScalar
dlcUnitFractionalLoopCode = _DlcUnitFractionalLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 9),
    _DlcUnitFractionalLoopCode_Type()
)
dlcUnitFractionalLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitFractionalLoopCode.setStatus("mandatory")
_DlcUnitTestLength_Type = Integer32
_DlcUnitTestLength_Object = MibScalar
dlcUnitTestLength = _DlcUnitTestLength_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 10),
    _DlcUnitTestLength_Type()
)
dlcUnitTestLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTestLength.setStatus("mandatory")


class _DlcUnitUserPattern1_Type(DisplayString):
    """Custom type dlcUnitUserPattern1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DlcUnitUserPattern1_Type.__name__ = "DisplayString"
_DlcUnitUserPattern1_Object = MibScalar
dlcUnitUserPattern1 = _DlcUnitUserPattern1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 11),
    _DlcUnitUserPattern1_Type()
)
dlcUnitUserPattern1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitUserPattern1.setStatus("mandatory")


class _DlcUnitUserPattern2_Type(DisplayString):
    """Custom type dlcUnitUserPattern2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DlcUnitUserPattern2_Type.__name__ = "DisplayString"
_DlcUnitUserPattern2_Object = MibScalar
dlcUnitUserPattern2 = _DlcUnitUserPattern2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 12),
    _DlcUnitUserPattern2_Type()
)
dlcUnitUserPattern2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitUserPattern2.setStatus("mandatory")
_DlcUnitBlockAllAlarms_Type = Boolean
_DlcUnitBlockAllAlarms_Object = MibScalar
dlcUnitBlockAllAlarms = _DlcUnitBlockAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 13),
    _DlcUnitBlockAllAlarms_Type()
)
dlcUnitBlockAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitBlockAllAlarms.setStatus("mandatory")
_DlcUnitDsx1TrapEnableTable_Object = MibTable
dlcUnitDsx1TrapEnableTable = _DlcUnitDsx1TrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14)
)
if mibBuilder.loadTexts:
    dlcUnitDsx1TrapEnableTable.setStatus("mandatory")
_DlcDsx1TrapEnableEntry_Object = MibTableRow
dlcDsx1TrapEnableEntry = _DlcDsx1TrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1)
)
dlcDsx1TrapEnableEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDsx1TrapPortId"),
)
if mibBuilder.loadTexts:
    dlcDsx1TrapEnableEntry.setStatus("mandatory")
_DlcDsx1TrapPortId_Type = PortId
_DlcDsx1TrapPortId_Object = MibTableColumn
dlcDsx1TrapPortId = _DlcDsx1TrapPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 1),
    _DlcDsx1TrapPortId_Type()
)
dlcDsx1TrapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDsx1TrapPortId.setStatus("mandatory")


class _DlcDsx1BpvThresholdTrap_Type(Integer32):
    """Custom type dlcDsx1BpvThresholdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DlcDsx1BpvThresholdTrap_Type.__name__ = "Integer32"
_DlcDsx1BpvThresholdTrap_Object = MibTableColumn
dlcDsx1BpvThresholdTrap = _DlcDsx1BpvThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 2),
    _DlcDsx1BpvThresholdTrap_Type()
)
dlcDsx1BpvThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1BpvThresholdTrap.setStatus("mandatory")


class _DlcDsx1OofThresholdTrap_Type(Integer32):
    """Custom type dlcDsx1OofThresholdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DlcDsx1OofThresholdTrap_Type.__name__ = "Integer32"
_DlcDsx1OofThresholdTrap_Object = MibTableColumn
dlcDsx1OofThresholdTrap = _DlcDsx1OofThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 3),
    _DlcDsx1OofThresholdTrap_Type()
)
dlcDsx1OofThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1OofThresholdTrap.setStatus("mandatory")


class _DlcDsx1CrcThresholdTrap_Type(Integer32):
    """Custom type dlcDsx1CrcThresholdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DlcDsx1CrcThresholdTrap_Type.__name__ = "Integer32"
_DlcDsx1CrcThresholdTrap_Object = MibTableColumn
dlcDsx1CrcThresholdTrap = _DlcDsx1CrcThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 4),
    _DlcDsx1CrcThresholdTrap_Type()
)
dlcDsx1CrcThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1CrcThresholdTrap.setStatus("mandatory")
_DlcDsx1LossOfSignalTrapEnable_Type = Boolean
_DlcDsx1LossOfSignalTrapEnable_Object = MibTableColumn
dlcDsx1LossOfSignalTrapEnable = _DlcDsx1LossOfSignalTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 5),
    _DlcDsx1LossOfSignalTrapEnable_Type()
)
dlcDsx1LossOfSignalTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1LossOfSignalTrapEnable.setStatus("mandatory")
_DlcDsx1LossOfSyncTrapEnable_Type = Boolean
_DlcDsx1LossOfSyncTrapEnable_Object = MibTableColumn
dlcDsx1LossOfSyncTrapEnable = _DlcDsx1LossOfSyncTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 6),
    _DlcDsx1LossOfSyncTrapEnable_Type()
)
dlcDsx1LossOfSyncTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1LossOfSyncTrapEnable.setStatus("mandatory")
_DlcDsx1ReceiveAIStrapEnable_Type = Boolean
_DlcDsx1ReceiveAIStrapEnable_Object = MibTableColumn
dlcDsx1ReceiveAIStrapEnable = _DlcDsx1ReceiveAIStrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 7),
    _DlcDsx1ReceiveAIStrapEnable_Type()
)
dlcDsx1ReceiveAIStrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1ReceiveAIStrapEnable.setStatus("mandatory")
_DlcDsx1ReceiveYellowAlarmTrapEnable_Type = Boolean
_DlcDsx1ReceiveYellowAlarmTrapEnable_Object = MibTableColumn
dlcDsx1ReceiveYellowAlarmTrapEnable = _DlcDsx1ReceiveYellowAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 8),
    _DlcDsx1ReceiveYellowAlarmTrapEnable_Type()
)
dlcDsx1ReceiveYellowAlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1ReceiveYellowAlarmTrapEnable.setStatus("mandatory")
_DlcDsx1ReceiveRemoteAlarmTrapEnable_Type = Boolean
_DlcDsx1ReceiveRemoteAlarmTrapEnable_Object = MibTableColumn
dlcDsx1ReceiveRemoteAlarmTrapEnable = _DlcDsx1ReceiveRemoteAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 9),
    _DlcDsx1ReceiveRemoteAlarmTrapEnable_Type()
)
dlcDsx1ReceiveRemoteAlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1ReceiveRemoteAlarmTrapEnable.setStatus("mandatory")
_DlcDsx1PSfailureTrapEnable_Type = Boolean
_DlcDsx1PSfailureTrapEnable_Object = MibTableColumn
dlcDsx1PSfailureTrapEnable = _DlcDsx1PSfailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 10),
    _DlcDsx1PSfailureTrapEnable_Type()
)
dlcDsx1PSfailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1PSfailureTrapEnable.setStatus("mandatory")
_DlcDsx1CntlCrdMissingTrapEnable_Type = Boolean
_DlcDsx1CntlCrdMissingTrapEnable_Object = MibTableColumn
dlcDsx1CntlCrdMissingTrapEnable = _DlcDsx1CntlCrdMissingTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 11),
    _DlcDsx1CntlCrdMissingTrapEnable_Type()
)
dlcDsx1CntlCrdMissingTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1CntlCrdMissingTrapEnable.setStatus("mandatory")
_DlcDsx1FdlLinkTrapEnable_Type = Boolean
_DlcDsx1FdlLinkTrapEnable_Object = MibTableColumn
dlcDsx1FdlLinkTrapEnable = _DlcDsx1FdlLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 12),
    _DlcDsx1FdlLinkTrapEnable_Type()
)
dlcDsx1FdlLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1FdlLinkTrapEnable.setStatus("mandatory")


class _DlcDsx1IbCrcThresholdTrap_Type(Integer32):
    """Custom type dlcDsx1IbCrcThresholdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DlcDsx1IbCrcThresholdTrap_Type.__name__ = "Integer32"
_DlcDsx1IbCrcThresholdTrap_Object = MibTableColumn
dlcDsx1IbCrcThresholdTrap = _DlcDsx1IbCrcThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 13),
    _DlcDsx1IbCrcThresholdTrap_Type()
)
dlcDsx1IbCrcThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1IbCrcThresholdTrap.setStatus("mandatory")
_DlcDsx1InbandLinkTrapEnable_Type = Boolean
_DlcDsx1InbandLinkTrapEnable_Object = MibTableColumn
dlcDsx1InbandLinkTrapEnable = _DlcDsx1InbandLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 14, 1, 14),
    _DlcDsx1InbandLinkTrapEnable_Type()
)
dlcDsx1InbandLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1InbandLinkTrapEnable.setStatus("mandatory")
_DlcUnitDataDteLossTrapEnableTable_Object = MibTable
dlcUnitDataDteLossTrapEnableTable = _DlcUnitDataDteLossTrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 15)
)
if mibBuilder.loadTexts:
    dlcUnitDataDteLossTrapEnableTable.setStatus("mandatory")
_DlcDataDteLossTrapEnableEntry_Object = MibTableRow
dlcDataDteLossTrapEnableEntry = _DlcDataDteLossTrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 15, 1)
)
dlcDataDteLossTrapEnableEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDataLossPortId"),
)
if mibBuilder.loadTexts:
    dlcDataDteLossTrapEnableEntry.setStatus("mandatory")
_DlcDataLossPortId_Type = PortId
_DlcDataLossPortId_Object = MibTableColumn
dlcDataLossPortId = _DlcDataLossPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 15, 1, 1),
    _DlcDataLossPortId_Type()
)
dlcDataLossPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDataLossPortId.setStatus("mandatory")
_DlcDataLossEnable_Type = Boolean
_DlcDataLossEnable_Object = MibTableColumn
dlcDataLossEnable = _DlcDataLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 15, 1, 2),
    _DlcDataLossEnable_Type()
)
dlcDataLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataLossEnable.setStatus("mandatory")
_DlcUnitExternalAlarmInputTrapEnable_Type = Boolean
_DlcUnitExternalAlarmInputTrapEnable_Object = MibScalar
dlcUnitExternalAlarmInputTrapEnable = _DlcUnitExternalAlarmInputTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 16),
    _DlcUnitExternalAlarmInputTrapEnable_Type()
)
dlcUnitExternalAlarmInputTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExternalAlarmInputTrapEnable.setStatus("mandatory")


class _DlcUnitExternalAlarmInputContacts_Type(Integer32):
    """Custom type dlcUnitExternalAlarmInputContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 2),
          ("normallyOpen", 1))
    )


_DlcUnitExternalAlarmInputContacts_Type.__name__ = "Integer32"
_DlcUnitExternalAlarmInputContacts_Object = MibScalar
dlcUnitExternalAlarmInputContacts = _DlcUnitExternalAlarmInputContacts_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 17),
    _DlcUnitExternalAlarmInputContacts_Type()
)
dlcUnitExternalAlarmInputContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExternalAlarmInputContacts.setStatus("mandatory")


class _DlcUnitExternalAlarmInputMessage_Type(DisplayString):
    """Custom type dlcUnitExternalAlarmInputMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DlcUnitExternalAlarmInputMessage_Type.__name__ = "DisplayString"
_DlcUnitExternalAlarmInputMessage_Object = MibScalar
dlcUnitExternalAlarmInputMessage = _DlcUnitExternalAlarmInputMessage_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 18),
    _DlcUnitExternalAlarmInputMessage_Type()
)
dlcUnitExternalAlarmInputMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExternalAlarmInputMessage.setStatus("mandatory")


class _DlcUnitExternalAlarmOutputContacts_Type(Integer32):
    """Custom type dlcUnitExternalAlarmOutputContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 2),
          ("normallyOpen", 1))
    )


_DlcUnitExternalAlarmOutputContacts_Type.__name__ = "Integer32"
_DlcUnitExternalAlarmOutputContacts_Object = MibScalar
dlcUnitExternalAlarmOutputContacts = _DlcUnitExternalAlarmOutputContacts_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 19),
    _DlcUnitExternalAlarmOutputContacts_Type()
)
dlcUnitExternalAlarmOutputContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExternalAlarmOutputContacts.setStatus("mandatory")
_DlcUnitExternalAlarmOutputTrapEnable_Type = Boolean
_DlcUnitExternalAlarmOutputTrapEnable_Object = MibScalar
dlcUnitExternalAlarmOutputTrapEnable = _DlcUnitExternalAlarmOutputTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 20),
    _DlcUnitExternalAlarmOutputTrapEnable_Type()
)
dlcUnitExternalAlarmOutputTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitExternalAlarmOutputTrapEnable.setStatus("mandatory")
_DlcUnitDsx1ConfigTable_Object = MibTable
dlcUnitDsx1ConfigTable = _DlcUnitDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21)
)
if mibBuilder.loadTexts:
    dlcUnitDsx1ConfigTable.setStatus("mandatory")
_DlcDsx1ConfigEntry_Object = MibTableRow
dlcDsx1ConfigEntry = _DlcDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1)
)
dlcDsx1ConfigEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDsx1ConfigPortId"),
)
if mibBuilder.loadTexts:
    dlcDsx1ConfigEntry.setStatus("mandatory")
_DlcDsx1ConfigPortId_Type = PortId
_DlcDsx1ConfigPortId_Object = MibTableColumn
dlcDsx1ConfigPortId = _DlcDsx1ConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 1),
    _DlcDsx1ConfigPortId_Type()
)
dlcDsx1ConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDsx1ConfigPortId.setStatus("mandatory")


class _DlcDsx1Framing_Type(Integer32):
    """Custom type dlcDsx1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crc4Disabled", 4),
          ("crc4Enabled", 3),
          ("d4Framing", 2),
          ("esfFraming", 1),
          ("unstructured", 5))
    )


_DlcDsx1Framing_Type.__name__ = "Integer32"
_DlcDsx1Framing_Object = MibTableColumn
dlcDsx1Framing = _DlcDsx1Framing_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 2),
    _DlcDsx1Framing_Type()
)
dlcDsx1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1Framing.setStatus("mandatory")


class _DlcDsx1LineCode_Type(Integer32):
    """Custom type dlcDsx1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("amiCode", 2),
          ("b8zsCode", 1),
          ("hdb3Code", 3))
    )


_DlcDsx1LineCode_Type.__name__ = "Integer32"
_DlcDsx1LineCode_Object = MibTableColumn
dlcDsx1LineCode = _DlcDsx1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 3),
    _DlcDsx1LineCode_Type()
)
dlcDsx1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1LineCode.setStatus("mandatory")


class _DlcDsx1LineMatching_Type(Integer32):
    """Custom type dlcDsx1LineMatching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("buildOut0", 1),
          ("buildOut15", 3),
          ("buildOut7p5", 2),
          ("length0", 4),
          ("length133", 5),
          ("length266", 6),
          ("length399", 7),
          ("length533", 8),
          ("ohms120", 10),
          ("ohms75", 9))
    )


_DlcDsx1LineMatching_Type.__name__ = "Integer32"
_DlcDsx1LineMatching_Object = MibTableColumn
dlcDsx1LineMatching = _DlcDsx1LineMatching_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 4),
    _DlcDsx1LineMatching_Type()
)
dlcDsx1LineMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1LineMatching.setStatus("mandatory")
_DlcDsx1DacsMode_Type = Boolean
_DlcDsx1DacsMode_Object = MibTableColumn
dlcDsx1DacsMode = _DlcDsx1DacsMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 5),
    _DlcDsx1DacsMode_Type()
)
dlcDsx1DacsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1DacsMode.setStatus("mandatory")
_DlcDsx1UseDlcFdlProtocol_Type = Boolean
_DlcDsx1UseDlcFdlProtocol_Object = MibTableColumn
dlcDsx1UseDlcFdlProtocol = _DlcDsx1UseDlcFdlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 6),
    _DlcDsx1UseDlcFdlProtocol_Type()
)
dlcDsx1UseDlcFdlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1UseDlcFdlProtocol.setStatus("mandatory")
_DlcDsx1UseAnsiProtocol_Type = Boolean
_DlcDsx1UseAnsiProtocol_Object = MibTableColumn
dlcDsx1UseAnsiProtocol = _DlcDsx1UseAnsiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 7),
    _DlcDsx1UseAnsiProtocol_Type()
)
dlcDsx1UseAnsiProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1UseAnsiProtocol.setStatus("mandatory")
_DlcDsx1Bit7Stuffing_Type = Boolean
_DlcDsx1Bit7Stuffing_Object = MibTableColumn
dlcDsx1Bit7Stuffing = _DlcDsx1Bit7Stuffing_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 8),
    _DlcDsx1Bit7Stuffing_Type()
)
dlcDsx1Bit7Stuffing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1Bit7Stuffing.setStatus("mandatory")


class _DlcDsx1InBandBit_Type(Integer32):
    """Custom type dlcDsx1InBandBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DlcDsx1InBandBit_Type.__name__ = "Integer32"
_DlcDsx1InBandBit_Object = MibTableColumn
dlcDsx1InBandBit = _DlcDsx1InBandBit_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 21, 1, 9),
    _DlcDsx1InBandBit_Type()
)
dlcDsx1InBandBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDsx1InBandBit.setStatus("mandatory")
_DlcUnitDataDteConfigTable_Object = MibTable
dlcUnitDataDteConfigTable = _DlcUnitDataDteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22)
)
if mibBuilder.loadTexts:
    dlcUnitDataDteConfigTable.setStatus("mandatory")
_DlcDataDteConfigEntry_Object = MibTableRow
dlcDataDteConfigEntry = _DlcDataDteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1)
)
dlcDataDteConfigEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDataConfigPortId"),
)
if mibBuilder.loadTexts:
    dlcDataDteConfigEntry.setStatus("mandatory")
_DlcDataConfigPortId_Type = PortId
_DlcDataConfigPortId_Object = MibTableColumn
dlcDataConfigPortId = _DlcDataConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 1),
    _DlcDataConfigPortId_Type()
)
dlcDataConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDataConfigPortId.setStatus("mandatory")


class _DlcDataConfigEncoding_Type(Integer32):
    """Custom type dlcDataConfigEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deferred", 3),
          ("forced", 4),
          ("hdlc", 2),
          ("normal", 1))
    )


_DlcDataConfigEncoding_Type.__name__ = "Integer32"
_DlcDataConfigEncoding_Object = MibTableColumn
dlcDataConfigEncoding = _DlcDataConfigEncoding_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 2),
    _DlcDataConfigEncoding_Type()
)
dlcDataConfigEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataConfigEncoding.setStatus("mandatory")


class _DlcDataConfigLoss_Type(Integer32):
    """Custom type dlcDataConfigLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dataDependentLoss", 4),
          ("dtrLoss", 3),
          ("never", 1),
          ("rtsLoss", 2))
    )


_DlcDataConfigLoss_Type.__name__ = "Integer32"
_DlcDataConfigLoss_Object = MibTableColumn
dlcDataConfigLoss = _DlcDataConfigLoss_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 3),
    _DlcDataConfigLoss_Type()
)
dlcDataConfigLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataConfigLoss.setStatus("mandatory")


class _DlcDataConfigMode_Type(Integer32):
    """Custom type dlcDataConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dceMode", 2),
          ("dteMode", 1))
    )


_DlcDataConfigMode_Type.__name__ = "Integer32"
_DlcDataConfigMode_Object = MibTableColumn
dlcDataConfigMode = _DlcDataConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 4),
    _DlcDataConfigMode_Type()
)
dlcDataConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataConfigMode.setStatus("mandatory")


class _DlcDataConfigFormat_Type(Integer32):
    """Custom type dlcDataConfigFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs449", 2),
          ("v35", 1))
    )


_DlcDataConfigFormat_Type.__name__ = "Integer32"
_DlcDataConfigFormat_Object = MibTableColumn
dlcDataConfigFormat = _DlcDataConfigFormat_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 5),
    _DlcDataConfigFormat_Type()
)
dlcDataConfigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataConfigFormat.setStatus("mandatory")


class _DlcDataConfigTransmitTiming_Type(Integer32):
    """Custom type dlcDataConfigTransmitTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sct", 2),
          ("sctInverted", 3),
          ("scte", 1))
    )


_DlcDataConfigTransmitTiming_Type.__name__ = "Integer32"
_DlcDataConfigTransmitTiming_Object = MibTableColumn
dlcDataConfigTransmitTiming = _DlcDataConfigTransmitTiming_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 22, 1, 6),
    _DlcDataConfigTransmitTiming_Type()
)
dlcDataConfigTransmitTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDataConfigTransmitTiming.setStatus("mandatory")
_DlcUnitMuxConfigTable_Object = MibTable
dlcUnitMuxConfigTable = _DlcUnitMuxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 23)
)
if mibBuilder.loadTexts:
    dlcUnitMuxConfigTable.setStatus("mandatory")
_DlcMuxConfigEntry_Object = MibTableRow
dlcMuxConfigEntry = _DlcMuxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 23, 1)
)
dlcMuxConfigEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcMuxConfigBusId"),
    (0, "DL-NEW-DSX1-MIB", "dlcMuxConfigSlotNumber"),
)
if mibBuilder.loadTexts:
    dlcMuxConfigEntry.setStatus("mandatory")


class _DlcMuxConfigBusId_Type(Integer32):
    """Custom type dlcMuxConfigBusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_DlcMuxConfigBusId_Type.__name__ = "Integer32"
_DlcMuxConfigBusId_Object = MibTableColumn
dlcMuxConfigBusId = _DlcMuxConfigBusId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 23, 1, 1),
    _DlcMuxConfigBusId_Type()
)
dlcMuxConfigBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcMuxConfigBusId.setStatus("mandatory")


class _DlcMuxConfigSlotNumber_Type(Integer32):
    """Custom type dlcMuxConfigSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DlcMuxConfigSlotNumber_Type.__name__ = "Integer32"
_DlcMuxConfigSlotNumber_Object = MibTableColumn
dlcMuxConfigSlotNumber = _DlcMuxConfigSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 23, 1, 2),
    _DlcMuxConfigSlotNumber_Type()
)
dlcMuxConfigSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcMuxConfigSlotNumber.setStatus("mandatory")
_DlcMuxConfigPortId_Type = PortId
_DlcMuxConfigPortId_Object = MibTableColumn
dlcMuxConfigPortId = _DlcMuxConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 23, 1, 3),
    _DlcMuxConfigPortId_Type()
)
dlcMuxConfigPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcMuxConfigPortId.setStatus("mandatory")
_DlcUnitSnmpConfig_ObjectIdentity = ObjectIdentity
dlcUnitSnmpConfig = _DlcUnitSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24)
)
_DlcSnmpUnitIpAddr_Type = IpAddress
_DlcSnmpUnitIpAddr_Object = MibScalar
dlcSnmpUnitIpAddr = _DlcSnmpUnitIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 1),
    _DlcSnmpUnitIpAddr_Type()
)
dlcSnmpUnitIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpUnitIpAddr.setStatus("mandatory")
_DlcSnmpUnitNetMask_Type = IpAddress
_DlcSnmpUnitNetMask_Object = MibScalar
dlcSnmpUnitNetMask = _DlcSnmpUnitNetMask_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 2),
    _DlcSnmpUnitNetMask_Type()
)
dlcSnmpUnitNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpUnitNetMask.setStatus("mandatory")
_DlcSnmpTrapAddr1_Type = IpAddress
_DlcSnmpTrapAddr1_Object = MibScalar
dlcSnmpTrapAddr1 = _DlcSnmpTrapAddr1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 3),
    _DlcSnmpTrapAddr1_Type()
)
dlcSnmpTrapAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapAddr1.setStatus("mandatory")
_DlcSnmpTrapAddr2_Type = IpAddress
_DlcSnmpTrapAddr2_Object = MibScalar
dlcSnmpTrapAddr2 = _DlcSnmpTrapAddr2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 4),
    _DlcSnmpTrapAddr2_Type()
)
dlcSnmpTrapAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapAddr2.setStatus("mandatory")
_DlcSnmpTrapAddr3_Type = IpAddress
_DlcSnmpTrapAddr3_Object = MibScalar
dlcSnmpTrapAddr3 = _DlcSnmpTrapAddr3_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 5),
    _DlcSnmpTrapAddr3_Type()
)
dlcSnmpTrapAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapAddr3.setStatus("mandatory")
_DlcSnmpTrapDlci1_Type = Gauge32
_DlcSnmpTrapDlci1_Object = MibScalar
dlcSnmpTrapDlci1 = _DlcSnmpTrapDlci1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 6),
    _DlcSnmpTrapDlci1_Type()
)
dlcSnmpTrapDlci1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDlci1.setStatus("mandatory")
_DlcSnmpTrapDlci2_Type = Gauge32
_DlcSnmpTrapDlci2_Object = MibScalar
dlcSnmpTrapDlci2 = _DlcSnmpTrapDlci2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 7),
    _DlcSnmpTrapDlci2_Type()
)
dlcSnmpTrapDlci2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDlci2.setStatus("mandatory")
_DlcSnmpTrapDlci3_Type = Gauge32
_DlcSnmpTrapDlci3_Object = MibScalar
dlcSnmpTrapDlci3 = _DlcSnmpTrapDlci3_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 8),
    _DlcSnmpTrapDlci3_Type()
)
dlcSnmpTrapDlci3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDlci3.setStatus("mandatory")


class _DlcSnmpTrapDirection1_Type(Integer32):
    """Custom type dlcSnmpTrapDirection1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commDirection", 1),
          ("dteDirection", 3),
          ("ethDirection", 5),
          ("fdlDirection", 4),
          ("netDirection", 2))
    )


_DlcSnmpTrapDirection1_Type.__name__ = "Integer32"
_DlcSnmpTrapDirection1_Object = MibScalar
dlcSnmpTrapDirection1 = _DlcSnmpTrapDirection1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 9),
    _DlcSnmpTrapDirection1_Type()
)
dlcSnmpTrapDirection1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDirection1.setStatus("mandatory")


class _DlcSnmpTrapDirection2_Type(Integer32):
    """Custom type dlcSnmpTrapDirection2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commDirection", 1),
          ("dteDirection", 3),
          ("ethDirection", 5),
          ("fdlDirection", 4),
          ("netDirection", 2))
    )


_DlcSnmpTrapDirection2_Type.__name__ = "Integer32"
_DlcSnmpTrapDirection2_Object = MibScalar
dlcSnmpTrapDirection2 = _DlcSnmpTrapDirection2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 10),
    _DlcSnmpTrapDirection2_Type()
)
dlcSnmpTrapDirection2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDirection2.setStatus("mandatory")


class _DlcSnmpTrapDirection3_Type(Integer32):
    """Custom type dlcSnmpTrapDirection3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commDirection", 1),
          ("dteDirection", 3),
          ("ethDirection", 5),
          ("fdlDirection", 4),
          ("netDirection", 2))
    )


_DlcSnmpTrapDirection3_Type.__name__ = "Integer32"
_DlcSnmpTrapDirection3_Object = MibScalar
dlcSnmpTrapDirection3 = _DlcSnmpTrapDirection3_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 11),
    _DlcSnmpTrapDirection3_Type()
)
dlcSnmpTrapDirection3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDirection3.setStatus("mandatory")


class _DlcSnmpTrapDirection_Type(Integer32):
    """Custom type dlcSnmpTrapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commDirection", 1),
          ("ibcDirection", 2))
    )


_DlcSnmpTrapDirection_Type.__name__ = "Integer32"
_DlcSnmpTrapDirection_Object = MibScalar
dlcSnmpTrapDirection = _DlcSnmpTrapDirection_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 12),
    _DlcSnmpTrapDirection_Type()
)
dlcSnmpTrapDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSnmpTrapDirection.setStatus("mandatory")
_DlcSnmpEthernetConfiguration_ObjectIdentity = ObjectIdentity
dlcSnmpEthernetConfiguration = _DlcSnmpEthernetConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 13)
)
_DlcEthernetIpAddr_Type = IpAddress
_DlcEthernetIpAddr_Object = MibScalar
dlcEthernetIpAddr = _DlcEthernetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 13, 1),
    _DlcEthernetIpAddr_Type()
)
dlcEthernetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcEthernetIpAddr.setStatus("mandatory")
_DlcEthernetIpMask_Type = IpAddress
_DlcEthernetIpMask_Object = MibScalar
dlcEthernetIpMask = _DlcEthernetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 13, 2),
    _DlcEthernetIpMask_Type()
)
dlcEthernetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcEthernetIpMask.setStatus("mandatory")
_DlcEthernetGatewayAddr_Type = IpAddress
_DlcEthernetGatewayAddr_Object = MibScalar
dlcEthernetGatewayAddr = _DlcEthernetGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 13, 3),
    _DlcEthernetGatewayAddr_Type()
)
dlcEthernetGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcEthernetGatewayAddr.setStatus("mandatory")
_DlcEthernetMacAddr_Type = MacAddress
_DlcEthernetMacAddr_Object = MibScalar
dlcEthernetMacAddr = _DlcEthernetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 24, 13, 4),
    _DlcEthernetMacAddr_Type()
)
dlcEthernetMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcEthernetMacAddr.setStatus("mandatory")
_DlcUnitConfigTime_ObjectIdentity = ObjectIdentity
dlcUnitConfigTime = _DlcUnitConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25)
)


class _DlcUnitTimeYear_Type(Integer32):
    """Custom type dlcUnitTimeYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1992, 2037),
    )


_DlcUnitTimeYear_Type.__name__ = "Integer32"
_DlcUnitTimeYear_Object = MibScalar
dlcUnitTimeYear = _DlcUnitTimeYear_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 1),
    _DlcUnitTimeYear_Type()
)
dlcUnitTimeYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeYear.setStatus("mandatory")


class _DlcUnitTimeMonth_Type(Integer32):
    """Custom type dlcUnitTimeMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DlcUnitTimeMonth_Type.__name__ = "Integer32"
_DlcUnitTimeMonth_Object = MibScalar
dlcUnitTimeMonth = _DlcUnitTimeMonth_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 2),
    _DlcUnitTimeMonth_Type()
)
dlcUnitTimeMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeMonth.setStatus("mandatory")


class _DlcUnitTimeDay_Type(Integer32):
    """Custom type dlcUnitTimeDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DlcUnitTimeDay_Type.__name__ = "Integer32"
_DlcUnitTimeDay_Object = MibScalar
dlcUnitTimeDay = _DlcUnitTimeDay_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 3),
    _DlcUnitTimeDay_Type()
)
dlcUnitTimeDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeDay.setStatus("mandatory")


class _DlcUnitTimeHour_Type(Integer32):
    """Custom type dlcUnitTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DlcUnitTimeHour_Type.__name__ = "Integer32"
_DlcUnitTimeHour_Object = MibScalar
dlcUnitTimeHour = _DlcUnitTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 4),
    _DlcUnitTimeHour_Type()
)
dlcUnitTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeHour.setStatus("mandatory")


class _DlcUnitTimeMinute_Type(Integer32):
    """Custom type dlcUnitTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DlcUnitTimeMinute_Type.__name__ = "Integer32"
_DlcUnitTimeMinute_Object = MibScalar
dlcUnitTimeMinute = _DlcUnitTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 5),
    _DlcUnitTimeMinute_Type()
)
dlcUnitTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeMinute.setStatus("mandatory")


class _DlcUnitTimeSecond_Type(Integer32):
    """Custom type dlcUnitTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DlcUnitTimeSecond_Type.__name__ = "Integer32"
_DlcUnitTimeSecond_Object = MibScalar
dlcUnitTimeSecond = _DlcUnitTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 25, 6),
    _DlcUnitTimeSecond_Type()
)
dlcUnitTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTimeSecond.setStatus("mandatory")


class _DlcUnitSerialNum_Type(DisplayString):
    """Custom type dlcUnitSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DlcUnitSerialNum_Type.__name__ = "DisplayString"
_DlcUnitSerialNum_Object = MibScalar
dlcUnitSerialNum = _DlcUnitSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 26),
    _DlcUnitSerialNum_Type()
)
dlcUnitSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitSerialNum.setStatus("mandatory")
_DlcUnitModemConfig_ObjectIdentity = ObjectIdentity
dlcUnitModemConfig = _DlcUnitModemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 27)
)


class _DlcModemPhoneNum1_Type(DisplayString):
    """Custom type dlcModemPhoneNum1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DlcModemPhoneNum1_Type.__name__ = "DisplayString"
_DlcModemPhoneNum1_Object = MibScalar
dlcModemPhoneNum1 = _DlcModemPhoneNum1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 27, 1),
    _DlcModemPhoneNum1_Type()
)
dlcModemPhoneNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcModemPhoneNum1.setStatus("mandatory")


class _DlcModemPhoneNum2_Type(DisplayString):
    """Custom type dlcModemPhoneNum2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DlcModemPhoneNum2_Type.__name__ = "DisplayString"
_DlcModemPhoneNum2_Object = MibScalar
dlcModemPhoneNum2 = _DlcModemPhoneNum2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 27, 2),
    _DlcModemPhoneNum2_Type()
)
dlcModemPhoneNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcModemPhoneNum2.setStatus("mandatory")


class _DlcModemInitString1_Type(DisplayString):
    """Custom type dlcModemInitString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlcModemInitString1_Type.__name__ = "DisplayString"
_DlcModemInitString1_Object = MibScalar
dlcModemInitString1 = _DlcModemInitString1_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 27, 3),
    _DlcModemInitString1_Type()
)
dlcModemInitString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcModemInitString1.setStatus("mandatory")


class _DlcModemInitString2_Type(DisplayString):
    """Custom type dlcModemInitString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_DlcModemInitString2_Type.__name__ = "DisplayString"
_DlcModemInitString2_Object = MibScalar
dlcModemInitString2 = _DlcModemInitString2_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 27, 4),
    _DlcModemInitString2_Type()
)
dlcModemInitString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcModemInitString2.setStatus("mandatory")


class _DlcUnitInbandMode_Type(Integer32):
    """Custom type dlcUnitInbandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ciscoHdlc", 3),
          ("frameRelay", 2),
          ("noInband", 1))
    )


_DlcUnitInbandMode_Type.__name__ = "Integer32"
_DlcUnitInbandMode_Object = MibScalar
dlcUnitInbandMode = _DlcUnitInbandMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 28),
    _DlcUnitInbandMode_Type()
)
dlcUnitInbandMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitInbandMode.setStatus("mandatory")


class _DlcUnitDialOutTimeInterval_Type(Integer32):
    """Custom type dlcUnitDialOutTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlcUnitDialOutTimeInterval_Type.__name__ = "Integer32"
_DlcUnitDialOutTimeInterval_Object = MibScalar
dlcUnitDialOutTimeInterval = _DlcUnitDialOutTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 29),
    _DlcUnitDialOutTimeInterval_Type()
)
dlcUnitDialOutTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitDialOutTimeInterval.setStatus("mandatory")
_DlcAlarmSignal_Type = FramedUnframed
_DlcAlarmSignal_Object = MibScalar
dlcAlarmSignal = _DlcAlarmSignal_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 30),
    _DlcAlarmSignal_Type()
)
dlcAlarmSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcAlarmSignal.setStatus("mandatory")


class _DlcUnitIdleCode_Type(Integer32):
    """Custom type dlcUnitIdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlcUnitIdleCode_Type.__name__ = "Integer32"
_DlcUnitIdleCode_Object = MibScalar
dlcUnitIdleCode = _DlcUnitIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 31),
    _DlcUnitIdleCode_Type()
)
dlcUnitIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitIdleCode.setStatus("mandatory")
_DlcRemoteCommunicationsMode_Type = RemoteCommunicationsMode
_DlcRemoteCommunicationsMode_Object = MibScalar
dlcRemoteCommunicationsMode = _DlcRemoteCommunicationsMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 32),
    _DlcRemoteCommunicationsMode_Type()
)
dlcRemoteCommunicationsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcRemoteCommunicationsMode.setStatus("mandatory")
_DlcUnitConfigLinkTest_ObjectIdentity = ObjectIdentity
dlcUnitConfigLinkTest = _DlcUnitConfigLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33)
)


class _DlcLinkTestState_Type(Integer32):
    """Custom type dlcLinkTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("idle", 4),
          ("running", 3))
    )


_DlcLinkTestState_Type.__name__ = "Integer32"
_DlcLinkTestState_Object = MibScalar
dlcLinkTestState = _DlcLinkTestState_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 1),
    _DlcLinkTestState_Type()
)
dlcLinkTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestState.setStatus("mandatory")
_DlcLinkTestAddress_Type = IpAddress
_DlcLinkTestAddress_Object = MibScalar
dlcLinkTestAddress = _DlcLinkTestAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 2),
    _DlcLinkTestAddress_Type()
)
dlcLinkTestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestAddress.setStatus("mandatory")


class _DlcLinkTestDlci_Type(Integer32):
    """Custom type dlcLinkTestDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DlcLinkTestDlci_Type.__name__ = "Integer32"
_DlcLinkTestDlci_Object = MibScalar
dlcLinkTestDlci = _DlcLinkTestDlci_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 3),
    _DlcLinkTestDlci_Type()
)
dlcLinkTestDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestDlci.setStatus("mandatory")


class _DlcLinkTestPort_Type(Integer32):
    """Custom type dlcLinkTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("comm", 1),
          ("dte", 3),
          ("eth", 4),
          ("net", 2))
    )


_DlcLinkTestPort_Type.__name__ = "Integer32"
_DlcLinkTestPort_Object = MibScalar
dlcLinkTestPort = _DlcLinkTestPort_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 4),
    _DlcLinkTestPort_Type()
)
dlcLinkTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestPort.setStatus("mandatory")
_DlcLinkTestLength_Type = Integer32
_DlcLinkTestLength_Object = MibScalar
dlcLinkTestLength = _DlcLinkTestLength_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 5),
    _DlcLinkTestLength_Type()
)
dlcLinkTestLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestLength.setStatus("mandatory")


class _DlcLinkTestInterval_Type(Integer32):
    """Custom type dlcLinkTestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_DlcLinkTestInterval_Type.__name__ = "Integer32"
_DlcLinkTestInterval_Object = MibScalar
dlcLinkTestInterval = _DlcLinkTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 6),
    _DlcLinkTestInterval_Type()
)
dlcLinkTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestInterval.setStatus("mandatory")


class _DlcLinkTestPacketSize_Type(Integer32):
    """Custom type dlcLinkTestPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DlcLinkTestPacketSize_Type.__name__ = "Integer32"
_DlcLinkTestPacketSize_Object = MibScalar
dlcLinkTestPacketSize = _DlcLinkTestPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 7),
    _DlcLinkTestPacketSize_Type()
)
dlcLinkTestPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestPacketSize.setStatus("mandatory")


class _DlcLinkTestPattern_Type(Integer32):
    """Custom type dlcLinkTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ping-all-0", 5),
          ("ping-all-1", 4),
          ("ping1-0", 3),
          ("ping2047", 2),
          ("ping511", 1))
    )


_DlcLinkTestPattern_Type.__name__ = "Integer32"
_DlcLinkTestPattern_Object = MibScalar
dlcLinkTestPattern = _DlcLinkTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 33, 8),
    _DlcLinkTestPattern_Type()
)
dlcLinkTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkTestPattern.setStatus("mandatory")
_DlcUnitInbandConfig_Type = Boolean
_DlcUnitInbandConfig_Object = MibScalar
dlcUnitInbandConfig = _DlcUnitInbandConfig_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 34),
    _DlcUnitInbandConfig_Type()
)
dlcUnitInbandConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitInbandConfig.setStatus("mandatory")


class _DlcUnitInbandTrafficType_Type(Integer32):
    """Custom type dlcUnitInbandTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ciscoHdlc", 2),
          ("frameRelay", 1))
    )


_DlcUnitInbandTrafficType_Type.__name__ = "Integer32"
_DlcUnitInbandTrafficType_Object = MibScalar
dlcUnitInbandTrafficType = _DlcUnitInbandTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 35),
    _DlcUnitInbandTrafficType_Type()
)
dlcUnitInbandTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitInbandTrafficType.setStatus("mandatory")
_DlcUnitPerformanceMonitoring_Type = Boolean
_DlcUnitPerformanceMonitoring_Object = MibScalar
dlcUnitPerformanceMonitoring = _DlcUnitPerformanceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 36),
    _DlcUnitPerformanceMonitoring_Type()
)
dlcUnitPerformanceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitPerformanceMonitoring.setStatus("mandatory")
_DlcUnitPvcAutoDiscovery_Type = Boolean
_DlcUnitPvcAutoDiscovery_Object = MibScalar
dlcUnitPvcAutoDiscovery = _DlcUnitPvcAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 37),
    _DlcUnitPvcAutoDiscovery_Type()
)
dlcUnitPvcAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitPvcAutoDiscovery.setStatus("mandatory")
_DlcUnitDelayMonitorConfig_ObjectIdentity = ObjectIdentity
dlcUnitDelayMonitorConfig = _DlcUnitDelayMonitorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38)
)
_DlcDelayMonitorConfigTable_Object = MibTable
dlcDelayMonitorConfigTable = _DlcDelayMonitorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1)
)
if mibBuilder.loadTexts:
    dlcDelayMonitorConfigTable.setStatus("mandatory")
_DlcDelayMonitorConfigEntry_Object = MibTableRow
dlcDelayMonitorConfigEntry = _DlcDelayMonitorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1)
)
dlcDelayMonitorConfigEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDelayMonitorConfigIndex"),
)
if mibBuilder.loadTexts:
    dlcDelayMonitorConfigEntry.setStatus("mandatory")


class _DlcDelayMonitorConfigIndex_Type(Integer32):
    """Custom type dlcDelayMonitorConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DlcDelayMonitorConfigIndex_Type.__name__ = "Integer32"
_DlcDelayMonitorConfigIndex_Object = MibTableColumn
dlcDelayMonitorConfigIndex = _DlcDelayMonitorConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 1),
    _DlcDelayMonitorConfigIndex_Type()
)
dlcDelayMonitorConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorConfigIndex.setStatus("mandatory")


class _DlcDelayMonitorState_Type(Integer32):
    """Custom type dlcDelayMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("idle", 4),
          ("running", 3))
    )


_DlcDelayMonitorState_Type.__name__ = "Integer32"
_DlcDelayMonitorState_Object = MibTableColumn
dlcDelayMonitorState = _DlcDelayMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 2),
    _DlcDelayMonitorState_Type()
)
dlcDelayMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorState.setStatus("mandatory")
_DlcDelayMonitorTargetAddress_Type = IpAddress
_DlcDelayMonitorTargetAddress_Object = MibTableColumn
dlcDelayMonitorTargetAddress = _DlcDelayMonitorTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 3),
    _DlcDelayMonitorTargetAddress_Type()
)
dlcDelayMonitorTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorTargetAddress.setStatus("mandatory")


class _DlcDelayMonitorDlci_Type(Integer32):
    """Custom type dlcDelayMonitorDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DlcDelayMonitorDlci_Type.__name__ = "Integer32"
_DlcDelayMonitorDlci_Object = MibTableColumn
dlcDelayMonitorDlci = _DlcDelayMonitorDlci_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 4),
    _DlcDelayMonitorDlci_Type()
)
dlcDelayMonitorDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorDlci.setStatus("mandatory")


class _DlcDelayMonitorPort_Type(Integer32):
    """Custom type dlcDelayMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("comm", 1),
          ("dte", 3),
          ("eth", 4),
          ("net", 2))
    )


_DlcDelayMonitorPort_Type.__name__ = "Integer32"
_DlcDelayMonitorPort_Object = MibTableColumn
dlcDelayMonitorPort = _DlcDelayMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 5),
    _DlcDelayMonitorPort_Type()
)
dlcDelayMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorPort.setStatus("mandatory")


class _DlcDelayMonitorInterval_Type(Integer32):
    """Custom type dlcDelayMonitorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_DlcDelayMonitorInterval_Type.__name__ = "Integer32"
_DlcDelayMonitorInterval_Object = MibTableColumn
dlcDelayMonitorInterval = _DlcDelayMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 6),
    _DlcDelayMonitorInterval_Type()
)
dlcDelayMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorInterval.setStatus("mandatory")


class _DlcDelayMonitorPacketSize_Type(Integer32):
    """Custom type dlcDelayMonitorPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DlcDelayMonitorPacketSize_Type.__name__ = "Integer32"
_DlcDelayMonitorPacketSize_Object = MibTableColumn
dlcDelayMonitorPacketSize = _DlcDelayMonitorPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 7),
    _DlcDelayMonitorPacketSize_Type()
)
dlcDelayMonitorPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorPacketSize.setStatus("mandatory")


class _DlcDelayMonitorPattern_Type(Integer32):
    """Custom type dlcDelayMonitorPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ping-all-0", 5),
          ("ping-all-1", 4),
          ("ping1-0", 3),
          ("ping2047", 2),
          ("ping511", 1))
    )


_DlcDelayMonitorPattern_Type.__name__ = "Integer32"
_DlcDelayMonitorPattern_Object = MibTableColumn
dlcDelayMonitorPattern = _DlcDelayMonitorPattern_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 38, 1, 1, 8),
    _DlcDelayMonitorPattern_Type()
)
dlcDelayMonitorPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDelayMonitorPattern.setStatus("mandatory")
_DlcDLCItable_Object = MibTable
dlcDLCItable = _DlcDLCItable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39)
)
if mibBuilder.loadTexts:
    dlcDLCItable.setStatus("mandatory")
_DlcDLCItableEntry_Object = MibTableRow
dlcDLCItableEntry = _DlcDLCItableEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39, 1)
)
dlcDLCItableEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDLCInumber"),
    (0, "DL-NEW-DSX1-MIB", "dlcDTECIR"),
    (0, "DL-NEW-DSX1-MIB", "dlcNETCIR"),
)
if mibBuilder.loadTexts:
    dlcDLCItableEntry.setStatus("mandatory")


class _DlcDLCInumber_Type(Integer32):
    """Custom type dlcDLCInumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_DlcDLCInumber_Type.__name__ = "Integer32"
_DlcDLCInumber_Object = MibTableColumn
dlcDLCInumber = _DlcDLCInumber_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39, 1, 1),
    _DlcDLCInumber_Type()
)
dlcDLCInumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDLCInumber.setStatus("mandatory")
_DlcDTECIR_Type = Integer32
_DlcDTECIR_Object = MibTableColumn
dlcDTECIR = _DlcDTECIR_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39, 1, 2),
    _DlcDTECIR_Type()
)
dlcDTECIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDTECIR.setStatus("mandatory")
_DlcNETCIR_Type = Integer32
_DlcNETCIR_Object = MibTableColumn
dlcNETCIR = _DlcNETCIR_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39, 1, 3),
    _DlcNETCIR_Type()
)
dlcNETCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcNETCIR.setStatus("mandatory")


class _DlcDLCIstatus_Type(Integer32):
    """Custom type dlcDLCIstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("inactive", 4))
    )


_DlcDLCIstatus_Type.__name__ = "Integer32"
_DlcDLCIstatus_Object = MibTableColumn
dlcDLCIstatus = _DlcDLCIstatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 39, 1, 4),
    _DlcDLCIstatus_Type()
)
dlcDLCIstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDLCIstatus.setStatus("mandatory")
_DlcLMIConditioningGroup_ObjectIdentity = ObjectIdentity
dlcLMIConditioningGroup = _DlcLMIConditioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41)
)
_DlcLMIConfiguration_ObjectIdentity = ObjectIdentity
dlcLMIConfiguration = _DlcLMIConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1)
)


class _DlcLMIEnable_Type(Integer32):
    """Custom type dlcLMIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DlcLMIEnable_Type.__name__ = "Integer32"
_DlcLMIEnable_Object = MibScalar
dlcLMIEnable = _DlcLMIEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 1),
    _DlcLMIEnable_Type()
)
dlcLMIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIEnable.setStatus("mandatory")


class _DlcMaintenanceDLCI_Type(Integer32):
    """Custom type dlcMaintenanceDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DlcMaintenanceDLCI_Type.__name__ = "Integer32"
_DlcMaintenanceDLCI_Object = MibScalar
dlcMaintenanceDLCI = _DlcMaintenanceDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 2),
    _DlcMaintenanceDLCI_Type()
)
dlcMaintenanceDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcMaintenanceDLCI.setStatus("mandatory")


class _DlcManagementDLCI_Type(Integer32):
    """Custom type dlcManagementDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DlcManagementDLCI_Type.__name__ = "Integer32"
_DlcManagementDLCI_Object = MibScalar
dlcManagementDLCI = _DlcManagementDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 3),
    _DlcManagementDLCI_Type()
)
dlcManagementDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcManagementDLCI.setStatus("mandatory")


class _DlcManagementDLCIEnable_Type(Integer32):
    """Custom type dlcManagementDLCIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DlcManagementDLCIEnable_Type.__name__ = "Integer32"
_DlcManagementDLCIEnable_Object = MibScalar
dlcManagementDLCIEnable = _DlcManagementDLCIEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 4),
    _DlcManagementDLCIEnable_Type()
)
dlcManagementDLCIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcManagementDLCIEnable.setStatus("mandatory")


class _DlcSpoofingProtocolType_Type(Integer32):
    """Custom type dlcSpoofingProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annex-a", 3),
          ("annex-d", 2),
          ("frf1-0", 1))
    )


_DlcSpoofingProtocolType_Type.__name__ = "Integer32"
_DlcSpoofingProtocolType_Object = MibScalar
dlcSpoofingProtocolType = _DlcSpoofingProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 5),
    _DlcSpoofingProtocolType_Type()
)
dlcSpoofingProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcSpoofingProtocolType.setStatus("mandatory")


class _DlcDTESpoofingEnable_Type(Integer32):
    """Custom type dlcDTESpoofingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DlcDTESpoofingEnable_Type.__name__ = "Integer32"
_DlcDTESpoofingEnable_Object = MibScalar
dlcDTESpoofingEnable = _DlcDTESpoofingEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 6),
    _DlcDTESpoofingEnable_Type()
)
dlcDTESpoofingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDTESpoofingEnable.setStatus("mandatory")


class _DlcNetSpoofingEnable_Type(Integer32):
    """Custom type dlcNetSpoofingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DlcNetSpoofingEnable_Type.__name__ = "Integer32"
_DlcNetSpoofingEnable_Object = MibScalar
dlcNetSpoofingEnable = _DlcNetSpoofingEnable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 7),
    _DlcNetSpoofingEnable_Type()
)
dlcNetSpoofingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcNetSpoofingEnable.setStatus("mandatory")


class _DlcLinkIntegrityVerificationPollingTimer_Type(Integer32):
    """Custom type dlcLinkIntegrityVerificationPollingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_DlcLinkIntegrityVerificationPollingTimer_Type.__name__ = "Integer32"
_DlcLinkIntegrityVerificationPollingTimer_Object = MibScalar
dlcLinkIntegrityVerificationPollingTimer = _DlcLinkIntegrityVerificationPollingTimer_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 8),
    _DlcLinkIntegrityVerificationPollingTimer_Type()
)
dlcLinkIntegrityVerificationPollingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLinkIntegrityVerificationPollingTimer.setStatus("mandatory")


class _DlcFullStatusPollingCounter_Type(Integer32):
    """Custom type dlcFullStatusPollingCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlcFullStatusPollingCounter_Type.__name__ = "Integer32"
_DlcFullStatusPollingCounter_Object = MibScalar
dlcFullStatusPollingCounter = _DlcFullStatusPollingCounter_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 9),
    _DlcFullStatusPollingCounter_Type()
)
dlcFullStatusPollingCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcFullStatusPollingCounter.setStatus("mandatory")


class _DlcLMIErrorEvent_Type(Integer32):
    """Custom type dlcLMIErrorEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DlcLMIErrorEvent_Type.__name__ = "Integer32"
_DlcLMIErrorEvent_Object = MibScalar
dlcLMIErrorEvent = _DlcLMIErrorEvent_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 10),
    _DlcLMIErrorEvent_Type()
)
dlcLMIErrorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIErrorEvent.setStatus("mandatory")


class _DlcLMIErrorMonitorEvent_Type(Integer32):
    """Custom type dlcLMIErrorMonitorEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DlcLMIErrorMonitorEvent_Type.__name__ = "Integer32"
_DlcLMIErrorMonitorEvent_Object = MibScalar
dlcLMIErrorMonitorEvent = _DlcLMIErrorMonitorEvent_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 11),
    _DlcLMIErrorMonitorEvent_Type()
)
dlcLMIErrorMonitorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIErrorMonitorEvent.setStatus("mandatory")


class _DlcLMIErrorFreeEvent_Type(Integer32):
    """Custom type dlcLMIErrorFreeEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DlcLMIErrorFreeEvent_Type.__name__ = "Integer32"
_DlcLMIErrorFreeEvent_Object = MibScalar
dlcLMIErrorFreeEvent = _DlcLMIErrorFreeEvent_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 12),
    _DlcLMIErrorFreeEvent_Type()
)
dlcLMIErrorFreeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIErrorFreeEvent.setStatus("mandatory")


class _DlcLMIErrorFreeMonitorEvent_Type(Integer32):
    """Custom type dlcLMIErrorFreeMonitorEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DlcLMIErrorFreeMonitorEvent_Type.__name__ = "Integer32"
_DlcLMIErrorFreeMonitorEvent_Object = MibScalar
dlcLMIErrorFreeMonitorEvent = _DlcLMIErrorFreeMonitorEvent_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 13),
    _DlcLMIErrorFreeMonitorEvent_Type()
)
dlcLMIErrorFreeMonitorEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIErrorFreeMonitorEvent.setStatus("mandatory")


class _DlcDTEResponseTimer_Type(Integer32):
    """Custom type dlcDTEResponseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_DlcDTEResponseTimer_Type.__name__ = "Integer32"
_DlcDTEResponseTimer_Object = MibScalar
dlcDTEResponseTimer = _DlcDTEResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 14),
    _DlcDTEResponseTimer_Type()
)
dlcDTEResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcDTEResponseTimer.setStatus("mandatory")


class _DlcLMIUnitLocation_Type(Integer32):
    """Custom type dlcLMIUnitLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co", 2),
          ("cpe", 1))
    )


_DlcLMIUnitLocation_Type.__name__ = "Integer32"
_DlcLMIUnitLocation_Object = MibScalar
dlcLMIUnitLocation = _DlcLMIUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 1, 15),
    _DlcLMIUnitLocation_Type()
)
dlcLMIUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLMIUnitLocation.setStatus("mandatory")
_DlcLMIStatus_ObjectIdentity = ObjectIdentity
dlcLMIStatus = _DlcLMIStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 2)
)


class _DlcSpoofingStatus_Type(Integer32):
    """Custom type dlcSpoofingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dte-and-net-spoofing", 4),
          ("dte-spoofing", 2),
          ("net-spoofing", 3),
          ("normal", 1))
    )


_DlcSpoofingStatus_Type.__name__ = "Integer32"
_DlcSpoofingStatus_Object = MibScalar
dlcSpoofingStatus = _DlcSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 2, 1),
    _DlcSpoofingStatus_Type()
)
dlcSpoofingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcSpoofingStatus.setStatus("mandatory")


class _DlcDTEInterfaceLMIStatus_Type(Integer32):
    """Custom type dlcDTEInterfaceLMIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lmi-down", 3),
          ("lmi-up", 2),
          ("unknown", 1))
    )


_DlcDTEInterfaceLMIStatus_Type.__name__ = "Integer32"
_DlcDTEInterfaceLMIStatus_Object = MibScalar
dlcDTEInterfaceLMIStatus = _DlcDTEInterfaceLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 2, 2),
    _DlcDTEInterfaceLMIStatus_Type()
)
dlcDTEInterfaceLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDTEInterfaceLMIStatus.setStatus("mandatory")


class _DlcNetInterfaceLMIStatus_Type(Integer32):
    """Custom type dlcNetInterfaceLMIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lmi-down", 3),
          ("lmi-up", 2),
          ("unknown", 1))
    )


_DlcNetInterfaceLMIStatus_Type.__name__ = "Integer32"
_DlcNetInterfaceLMIStatus_Object = MibScalar
dlcNetInterfaceLMIStatus = _DlcNetInterfaceLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 41, 2, 3),
    _DlcNetInterfaceLMIStatus_Type()
)
dlcNetInterfaceLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcNetInterfaceLMIStatus.setStatus("mandatory")


class _DlcInbandDtePort_Type(Integer32):
    """Custom type dlcInbandDtePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data1", 1),
          ("data2", 2))
    )


_DlcInbandDtePort_Type.__name__ = "Integer32"
_DlcInbandDtePort_Object = MibScalar
dlcInbandDtePort = _DlcInbandDtePort_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 2, 42),
    _DlcInbandDtePort_Type()
)
dlcInbandDtePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcInbandDtePort.setStatus("mandatory")
_DlcUnitStatus_ObjectIdentity = ObjectIdentity
dlcUnitStatus = _DlcUnitStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 3)
)
_DlcUnitCurrentStatus_Type = UnitStatusItem
_DlcUnitCurrentStatus_Object = MibScalar
dlcUnitCurrentStatus = _DlcUnitCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 1),
    _DlcUnitCurrentStatus_Type()
)
dlcUnitCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitCurrentStatus.setStatus("mandatory")
_DlcUnitErrorFreeSeconds_Type = Gauge32
_DlcUnitErrorFreeSeconds_Object = MibScalar
dlcUnitErrorFreeSeconds = _DlcUnitErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 2),
    _DlcUnitErrorFreeSeconds_Type()
)
dlcUnitErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitErrorFreeSeconds.setStatus("mandatory")


class _DlcUnitLastSelfTestResult_Type(Integer32):
    """Custom type dlcUnitLastSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DlcUnitLastSelfTestResult_Type.__name__ = "Integer32"
_DlcUnitLastSelfTestResult_Object = MibScalar
dlcUnitLastSelfTestResult = _DlcUnitLastSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 3),
    _DlcUnitLastSelfTestResult_Type()
)
dlcUnitLastSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitLastSelfTestResult.setStatus("mandatory")
_DlcUnitPortStatusTable_Object = MibTable
dlcUnitPortStatusTable = _DlcUnitPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4)
)
if mibBuilder.loadTexts:
    dlcUnitPortStatusTable.setStatus("mandatory")
_DlcPortStatusEntry_Object = MibTableRow
dlcPortStatusEntry = _DlcPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4, 1)
)
dlcPortStatusEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcPortStatusId"),
    (0, "DL-NEW-DSX1-MIB", "dlcPortStatus"),
)
if mibBuilder.loadTexts:
    dlcPortStatusEntry.setStatus("mandatory")
_DlcPortStatusId_Type = PortId
_DlcPortStatusId_Object = MibTableColumn
dlcPortStatusId = _DlcPortStatusId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4, 1, 1),
    _DlcPortStatusId_Type()
)
dlcPortStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcPortStatusId.setStatus("mandatory")
_DlcPortStatus_Type = PortStatusItem
_DlcPortStatus_Object = MibTableColumn
dlcPortStatus = _DlcPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4, 1, 2),
    _DlcPortStatus_Type()
)
dlcPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcPortStatus.setStatus("mandatory")
_DlcPortStatusNetRxBwUtilization_Type = Gauge32
_DlcPortStatusNetRxBwUtilization_Object = MibTableColumn
dlcPortStatusNetRxBwUtilization = _DlcPortStatusNetRxBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4, 1, 3),
    _DlcPortStatusNetRxBwUtilization_Type()
)
dlcPortStatusNetRxBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcPortStatusNetRxBwUtilization.setStatus("mandatory")
_DlcPortStatusNetTxBwUtilization_Type = Gauge32
_DlcPortStatusNetTxBwUtilization_Object = MibTableColumn
dlcPortStatusNetTxBwUtilization = _DlcPortStatusNetTxBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 4, 1, 4),
    _DlcPortStatusNetTxBwUtilization_Type()
)
dlcPortStatusNetTxBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcPortStatusNetTxBwUtilization.setStatus("mandatory")
_DlcUnitAlarmTable_Object = MibTable
dlcUnitAlarmTable = _DlcUnitAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 5)
)
if mibBuilder.loadTexts:
    dlcUnitAlarmTable.setStatus("mandatory")
_DlcAlarmEntry_Object = MibTableRow
dlcAlarmEntry = _DlcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 5, 1)
)
dlcAlarmEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcAlarmPort"),
    (0, "DL-NEW-DSX1-MIB", "dlcAlarmType"),
)
if mibBuilder.loadTexts:
    dlcAlarmEntry.setStatus("mandatory")
_DlcAlarmPort_Type = PortId
_DlcAlarmPort_Object = MibTableColumn
dlcAlarmPort = _DlcAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 5, 1, 1),
    _DlcAlarmPort_Type()
)
dlcAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcAlarmPort.setStatus("mandatory")
_DlcAlarmType_Type = AlarmType
_DlcAlarmType_Object = MibTableColumn
dlcAlarmType = _DlcAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 5, 1, 2),
    _DlcAlarmType_Type()
)
dlcAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcAlarmType.setStatus("mandatory")
_DlcUnitErrorSecondsRatio_Type = Gauge32
_DlcUnitErrorSecondsRatio_Object = MibScalar
dlcUnitErrorSecondsRatio = _DlcUnitErrorSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 6),
    _DlcUnitErrorSecondsRatio_Type()
)
dlcUnitErrorSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitErrorSecondsRatio.setStatus("mandatory")
_DlcUnitSeverelyErroredSecondsRatio_Type = Gauge32
_DlcUnitSeverelyErroredSecondsRatio_Object = MibScalar
dlcUnitSeverelyErroredSecondsRatio = _DlcUnitSeverelyErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 7),
    _DlcUnitSeverelyErroredSecondsRatio_Type()
)
dlcUnitSeverelyErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitSeverelyErroredSecondsRatio.setStatus("mandatory")
_DlcUnitBackgroundBlockErrorRatio_Type = Gauge32
_DlcUnitBackgroundBlockErrorRatio_Object = MibScalar
dlcUnitBackgroundBlockErrorRatio = _DlcUnitBackgroundBlockErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 3, 8),
    _DlcUnitBackgroundBlockErrorRatio_Type()
)
dlcUnitBackgroundBlockErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitBackgroundBlockErrorRatio.setStatus("mandatory")
_DlcUnitUserArchive_ObjectIdentity = ObjectIdentity
dlcUnitUserArchive = _DlcUnitUserArchive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 4)
)
_DlcUnitUserArchiveValidTable_Object = MibTable
dlcUnitUserArchiveValidTable = _DlcUnitUserArchiveValidTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 1)
)
if mibBuilder.loadTexts:
    dlcUnitUserArchiveValidTable.setStatus("mandatory")
_DlcUserArchiveValidEntry_Object = MibTableRow
dlcUserArchiveValidEntry = _DlcUserArchiveValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 1, 1)
)
dlcUserArchiveValidEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcValidPortId"),
)
if mibBuilder.loadTexts:
    dlcUserArchiveValidEntry.setStatus("mandatory")
_DlcValidPortId_Type = PortId
_DlcValidPortId_Object = MibTableColumn
dlcValidPortId = _DlcValidPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 1, 1, 1),
    _DlcValidPortId_Type()
)
dlcValidPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcValidPortId.setStatus("mandatory")


class _DlcValidIntervals_Type(Integer32):
    """Custom type dlcValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DlcValidIntervals_Type.__name__ = "Integer32"
_DlcValidIntervals_Object = MibTableColumn
dlcValidIntervals = _DlcValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 1, 1, 2),
    _DlcValidIntervals_Type()
)
dlcValidIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcValidIntervals.setStatus("mandatory")
_DlcUnitUserLifetimeTable_Object = MibTable
dlcUnitUserLifetimeTable = _DlcUnitUserLifetimeTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2)
)
if mibBuilder.loadTexts:
    dlcUnitUserLifetimeTable.setStatus("mandatory")
_DlcUserLifetimeEntry_Object = MibTableRow
dlcUserLifetimeEntry = _DlcUserLifetimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1)
)
dlcUserLifetimeEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcLifetimePortId"),
)
if mibBuilder.loadTexts:
    dlcUserLifetimeEntry.setStatus("mandatory")
_DlcLifetimePortId_Type = PortId
_DlcLifetimePortId_Object = MibTableColumn
dlcLifetimePortId = _DlcLifetimePortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 1),
    _DlcLifetimePortId_Type()
)
dlcLifetimePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLifetimePortId.setStatus("mandatory")
_DlcLifetimeES_Type = Gauge32
_DlcLifetimeES_Object = MibTableColumn
dlcLifetimeES = _DlcLifetimeES_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 2),
    _DlcLifetimeES_Type()
)
dlcLifetimeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeES.setStatus("mandatory")
_DlcLifetimeUAS_Type = Gauge32
_DlcLifetimeUAS_Object = MibTableColumn
dlcLifetimeUAS = _DlcLifetimeUAS_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 3),
    _DlcLifetimeUAS_Type()
)
dlcLifetimeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeUAS.setStatus("mandatory")
_DlcLifetimeCrcErrors_Type = Gauge32
_DlcLifetimeCrcErrors_Object = MibTableColumn
dlcLifetimeCrcErrors = _DlcLifetimeCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 4),
    _DlcLifetimeCrcErrors_Type()
)
dlcLifetimeCrcErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeCrcErrors.setStatus("mandatory")
_DlcLifetimeBpvErrors_Type = Gauge32
_DlcLifetimeBpvErrors_Object = MibTableColumn
dlcLifetimeBpvErrors = _DlcLifetimeBpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 5),
    _DlcLifetimeBpvErrors_Type()
)
dlcLifetimeBpvErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeBpvErrors.setStatus("mandatory")
_DlcLifetimeOofErrors_Type = Gauge32
_DlcLifetimeOofErrors_Object = MibTableColumn
dlcLifetimeOofErrors = _DlcLifetimeOofErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 6),
    _DlcLifetimeOofErrors_Type()
)
dlcLifetimeOofErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeOofErrors.setStatus("mandatory")
_DlcLifetimeIbCrcErrors_Type = Gauge32
_DlcLifetimeIbCrcErrors_Object = MibTableColumn
dlcLifetimeIbCrcErrors = _DlcLifetimeIbCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 2, 1, 7),
    _DlcLifetimeIbCrcErrors_Type()
)
dlcLifetimeIbCrcErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcLifetimeIbCrcErrors.setStatus("mandatory")
_DlcUnitUserCurrentTable_Object = MibTable
dlcUnitUserCurrentTable = _DlcUnitUserCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3)
)
if mibBuilder.loadTexts:
    dlcUnitUserCurrentTable.setStatus("mandatory")
_DlcUserCurrentEntry_Object = MibTableRow
dlcUserCurrentEntry = _DlcUserCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1)
)
dlcUserCurrentEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcCurrentPortId"),
)
if mibBuilder.loadTexts:
    dlcUserCurrentEntry.setStatus("mandatory")
_DlcCurrentPortId_Type = PortId
_DlcCurrentPortId_Object = MibTableColumn
dlcCurrentPortId = _DlcCurrentPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 1),
    _DlcCurrentPortId_Type()
)
dlcCurrentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentPortId.setStatus("mandatory")
_DlcCurrentES_Type = Counter32
_DlcCurrentES_Object = MibTableColumn
dlcCurrentES = _DlcCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 2),
    _DlcCurrentES_Type()
)
dlcCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentES.setStatus("mandatory")
_DlcCurrentUAS_Type = Counter32
_DlcCurrentUAS_Object = MibTableColumn
dlcCurrentUAS = _DlcCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 3),
    _DlcCurrentUAS_Type()
)
dlcCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentUAS.setStatus("mandatory")
_DlcCurrentCrcErrors_Type = Counter32
_DlcCurrentCrcErrors_Object = MibTableColumn
dlcCurrentCrcErrors = _DlcCurrentCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 4),
    _DlcCurrentCrcErrors_Type()
)
dlcCurrentCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentCrcErrors.setStatus("mandatory")
_DlcCurrentBpvErrors_Type = Counter32
_DlcCurrentBpvErrors_Object = MibTableColumn
dlcCurrentBpvErrors = _DlcCurrentBpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 5),
    _DlcCurrentBpvErrors_Type()
)
dlcCurrentBpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentBpvErrors.setStatus("mandatory")
_DlcCurrentOofErrors_Type = Counter32
_DlcCurrentOofErrors_Object = MibTableColumn
dlcCurrentOofErrors = _DlcCurrentOofErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 6),
    _DlcCurrentOofErrors_Type()
)
dlcCurrentOofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentOofErrors.setStatus("mandatory")


class _DlcCurrentTimeElapsed_Type(Integer32):
    """Custom type dlcCurrentTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_DlcCurrentTimeElapsed_Type.__name__ = "Integer32"
_DlcCurrentTimeElapsed_Object = MibTableColumn
dlcCurrentTimeElapsed = _DlcCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 7),
    _DlcCurrentTimeElapsed_Type()
)
dlcCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentTimeElapsed.setStatus("mandatory")
_DlcCurrentIbCrcErrors_Type = Counter32
_DlcCurrentIbCrcErrors_Object = MibTableColumn
dlcCurrentIbCrcErrors = _DlcCurrentIbCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 3, 1, 8),
    _DlcCurrentIbCrcErrors_Type()
)
dlcCurrentIbCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcCurrentIbCrcErrors.setStatus("mandatory")
_DlcUnitUserArchiveTable_Object = MibTable
dlcUnitUserArchiveTable = _DlcUnitUserArchiveTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4)
)
if mibBuilder.loadTexts:
    dlcUnitUserArchiveTable.setStatus("mandatory")
_DlcUserArchiveEntry_Object = MibTableRow
dlcUserArchiveEntry = _DlcUserArchiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1)
)
dlcUserArchiveEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcArchivePortId"),
    (0, "DL-NEW-DSX1-MIB", "dlcArchiveInterval"),
)
if mibBuilder.loadTexts:
    dlcUserArchiveEntry.setStatus("mandatory")
_DlcArchivePortId_Type = PortId
_DlcArchivePortId_Object = MibTableColumn
dlcArchivePortId = _DlcArchivePortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 1),
    _DlcArchivePortId_Type()
)
dlcArchivePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchivePortId.setStatus("mandatory")


class _DlcArchiveInterval_Type(Integer32):
    """Custom type dlcArchiveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DlcArchiveInterval_Type.__name__ = "Integer32"
_DlcArchiveInterval_Object = MibTableColumn
dlcArchiveInterval = _DlcArchiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 2),
    _DlcArchiveInterval_Type()
)
dlcArchiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveInterval.setStatus("mandatory")
_DlcArchiveES_Type = Counter32
_DlcArchiveES_Object = MibTableColumn
dlcArchiveES = _DlcArchiveES_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 3),
    _DlcArchiveES_Type()
)
dlcArchiveES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveES.setStatus("mandatory")
_DlcArchiveUAS_Type = Counter32
_DlcArchiveUAS_Object = MibTableColumn
dlcArchiveUAS = _DlcArchiveUAS_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 4),
    _DlcArchiveUAS_Type()
)
dlcArchiveUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveUAS.setStatus("mandatory")
_DlcArchiveCrcErrors_Type = Counter32
_DlcArchiveCrcErrors_Object = MibTableColumn
dlcArchiveCrcErrors = _DlcArchiveCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 5),
    _DlcArchiveCrcErrors_Type()
)
dlcArchiveCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveCrcErrors.setStatus("mandatory")
_DlcArchiveBpvErrors_Type = Counter32
_DlcArchiveBpvErrors_Object = MibTableColumn
dlcArchiveBpvErrors = _DlcArchiveBpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 6),
    _DlcArchiveBpvErrors_Type()
)
dlcArchiveBpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveBpvErrors.setStatus("mandatory")
_DlcArchiveOofErrors_Type = Counter32
_DlcArchiveOofErrors_Object = MibTableColumn
dlcArchiveOofErrors = _DlcArchiveOofErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 7),
    _DlcArchiveOofErrors_Type()
)
dlcArchiveOofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveOofErrors.setStatus("mandatory")
_DlcArchiveIbCrcErrors_Type = Counter32
_DlcArchiveIbCrcErrors_Object = MibTableColumn
dlcArchiveIbCrcErrors = _DlcArchiveIbCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 8),
    _DlcArchiveIbCrcErrors_Type()
)
dlcArchiveIbCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveIbCrcErrors.setStatus("mandatory")
_DlcArchiveNetRxBwUtilization_Type = Gauge32
_DlcArchiveNetRxBwUtilization_Object = MibTableColumn
dlcArchiveNetRxBwUtilization = _DlcArchiveNetRxBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 9),
    _DlcArchiveNetRxBwUtilization_Type()
)
dlcArchiveNetRxBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveNetRxBwUtilization.setStatus("mandatory")
_DlcArchiveNetRxPackets_Type = Counter32
_DlcArchiveNetRxPackets_Object = MibTableColumn
dlcArchiveNetRxPackets = _DlcArchiveNetRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 10),
    _DlcArchiveNetRxPackets_Type()
)
dlcArchiveNetRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveNetRxPackets.setStatus("mandatory")
_DlcArchiveNetTxBwUtilization_Type = Gauge32
_DlcArchiveNetTxBwUtilization_Object = MibTableColumn
dlcArchiveNetTxBwUtilization = _DlcArchiveNetTxBwUtilization_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 11),
    _DlcArchiveNetTxBwUtilization_Type()
)
dlcArchiveNetTxBwUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveNetTxBwUtilization.setStatus("mandatory")
_DlcArchiveNetTxPackets_Type = Counter32
_DlcArchiveNetTxPackets_Object = MibTableColumn
dlcArchiveNetTxPackets = _DlcArchiveNetTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 4, 4, 1, 12),
    _DlcArchiveNetTxPackets_Type()
)
dlcArchiveNetTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcArchiveNetTxPackets.setStatus("mandatory")
_DlcUnitTest_ObjectIdentity = ObjectIdentity
dlcUnitTest = _DlcUnitTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 5)
)
_DlcUnitTestTable_Object = MibTable
dlcUnitTestTable = _DlcUnitTestTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1)
)
if mibBuilder.loadTexts:
    dlcUnitTestTable.setStatus("mandatory")
_DlcUnitTestEntry_Object = MibTableRow
dlcUnitTestEntry = _DlcUnitTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1)
)
dlcUnitTestEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcUnitTestPortId"),
)
if mibBuilder.loadTexts:
    dlcUnitTestEntry.setStatus("mandatory")
_DlcUnitTestPortId_Type = PortId
_DlcUnitTestPortId_Object = MibTableColumn
dlcUnitTestPortId = _DlcUnitTestPortId_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 1),
    _DlcUnitTestPortId_Type()
)
dlcUnitTestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitTestPortId.setStatus("mandatory")
_DlcUnitTestType_Type = TestType
_DlcUnitTestType_Object = MibTableColumn
dlcUnitTestType = _DlcUnitTestType_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 2),
    _DlcUnitTestType_Type()
)
dlcUnitTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTestType.setStatus("mandatory")


class _DlcUnitTestPatternStatus_Type(Integer32):
    """Custom type dlcUnitTestPatternStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("lockedAfterLoss", 5),
          ("off", 4),
          ("overflow", 3),
          ("search", 1))
    )


_DlcUnitTestPatternStatus_Type.__name__ = "Integer32"
_DlcUnitTestPatternStatus_Object = MibTableColumn
dlcUnitTestPatternStatus = _DlcUnitTestPatternStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 3),
    _DlcUnitTestPatternStatus_Type()
)
dlcUnitTestPatternStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUnitTestPatternStatus.setStatus("mandatory")
_DlcUnitTestPatternErrors_Type = Gauge32
_DlcUnitTestPatternErrors_Object = MibTableColumn
dlcUnitTestPatternErrors = _DlcUnitTestPatternErrors_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 4),
    _DlcUnitTestPatternErrors_Type()
)
dlcUnitTestPatternErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlcUnitTestPatternErrors.setStatus("mandatory")
_DlcLinkTestSentPackets_Type = Gauge32
_DlcLinkTestSentPackets_Object = MibTableColumn
dlcLinkTestSentPackets = _DlcLinkTestSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 5),
    _DlcLinkTestSentPackets_Type()
)
dlcLinkTestSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestSentPackets.setStatus("mandatory")
_DlcLinkTestReceivedPackets_Type = Gauge32
_DlcLinkTestReceivedPackets_Object = MibTableColumn
dlcLinkTestReceivedPackets = _DlcLinkTestReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 6),
    _DlcLinkTestReceivedPackets_Type()
)
dlcLinkTestReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestReceivedPackets.setStatus("mandatory")
_DlcLinkTestErroredPackets_Type = Gauge32
_DlcLinkTestErroredPackets_Object = MibTableColumn
dlcLinkTestErroredPackets = _DlcLinkTestErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 7),
    _DlcLinkTestErroredPackets_Type()
)
dlcLinkTestErroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestErroredPackets.setStatus("mandatory")
_DlcLinkTestMissingPackets_Type = Gauge32
_DlcLinkTestMissingPackets_Object = MibTableColumn
dlcLinkTestMissingPackets = _DlcLinkTestMissingPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 8),
    _DlcLinkTestMissingPackets_Type()
)
dlcLinkTestMissingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestMissingPackets.setStatus("mandatory")
_DlcLinkTestAverageRoundTrip_Type = Gauge32
_DlcLinkTestAverageRoundTrip_Object = MibTableColumn
dlcLinkTestAverageRoundTrip = _DlcLinkTestAverageRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 9),
    _DlcLinkTestAverageRoundTrip_Type()
)
dlcLinkTestAverageRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestAverageRoundTrip.setStatus("mandatory")
_DlcLinkTestMaximumRoundTrip_Type = Gauge32
_DlcLinkTestMaximumRoundTrip_Object = MibTableColumn
dlcLinkTestMaximumRoundTrip = _DlcLinkTestMaximumRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 5, 1, 1, 10),
    _DlcLinkTestMaximumRoundTrip_Type()
)
dlcLinkTestMaximumRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcLinkTestMaximumRoundTrip.setStatus("mandatory")
_DlcUnitDelayMonitorStatus_ObjectIdentity = ObjectIdentity
dlcUnitDelayMonitorStatus = _DlcUnitDelayMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 200, 6)
)
_DlcDelayMonitorStatusTable_Object = MibTable
dlcDelayMonitorStatusTable = _DlcDelayMonitorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1)
)
if mibBuilder.loadTexts:
    dlcDelayMonitorStatusTable.setStatus("mandatory")
_DlcDelayMonitorStatusEntry_Object = MibTableRow
dlcDelayMonitorStatusEntry = _DlcDelayMonitorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1)
)
dlcDelayMonitorStatusEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcDelayMonitorStatusIndex"),
)
if mibBuilder.loadTexts:
    dlcDelayMonitorStatusEntry.setStatus("mandatory")


class _DlcDelayMonitorStatusIndex_Type(Integer32):
    """Custom type dlcDelayMonitorStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DlcDelayMonitorStatusIndex_Type.__name__ = "Integer32"
_DlcDelayMonitorStatusIndex_Object = MibTableColumn
dlcDelayMonitorStatusIndex = _DlcDelayMonitorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 1),
    _DlcDelayMonitorStatusIndex_Type()
)
dlcDelayMonitorStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorStatusIndex.setStatus("mandatory")
_DlcDelayMonitorSentPackets_Type = Gauge32
_DlcDelayMonitorSentPackets_Object = MibTableColumn
dlcDelayMonitorSentPackets = _DlcDelayMonitorSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 2),
    _DlcDelayMonitorSentPackets_Type()
)
dlcDelayMonitorSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorSentPackets.setStatus("mandatory")
_DlcDelayMonitorReceivedPackets_Type = Gauge32
_DlcDelayMonitorReceivedPackets_Object = MibTableColumn
dlcDelayMonitorReceivedPackets = _DlcDelayMonitorReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 3),
    _DlcDelayMonitorReceivedPackets_Type()
)
dlcDelayMonitorReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorReceivedPackets.setStatus("mandatory")
_DlcDelayMonitorErroredPackets_Type = Gauge32
_DlcDelayMonitorErroredPackets_Object = MibTableColumn
dlcDelayMonitorErroredPackets = _DlcDelayMonitorErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 4),
    _DlcDelayMonitorErroredPackets_Type()
)
dlcDelayMonitorErroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorErroredPackets.setStatus("mandatory")
_DlcDelayMonitorMissingPackets_Type = Gauge32
_DlcDelayMonitorMissingPackets_Object = MibTableColumn
dlcDelayMonitorMissingPackets = _DlcDelayMonitorMissingPackets_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 5),
    _DlcDelayMonitorMissingPackets_Type()
)
dlcDelayMonitorMissingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorMissingPackets.setStatus("mandatory")
_DlcDelayMonitorAverageRoundTrip_Type = Gauge32
_DlcDelayMonitorAverageRoundTrip_Object = MibTableColumn
dlcDelayMonitorAverageRoundTrip = _DlcDelayMonitorAverageRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 6),
    _DlcDelayMonitorAverageRoundTrip_Type()
)
dlcDelayMonitorAverageRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorAverageRoundTrip.setStatus("mandatory")
_DlcDelayMonitorMaximumRoundTrip_Type = Gauge32
_DlcDelayMonitorMaximumRoundTrip_Object = MibTableColumn
dlcDelayMonitorMaximumRoundTrip = _DlcDelayMonitorMaximumRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 6, 1, 1, 7),
    _DlcDelayMonitorMaximumRoundTrip_Type()
)
dlcDelayMonitorMaximumRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcDelayMonitorMaximumRoundTrip.setStatus("mandatory")
_DlcUtilizationTable_Object = MibTable
dlcUtilizationTable = _DlcUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7)
)
if mibBuilder.loadTexts:
    dlcUtilizationTable.setStatus("mandatory")
_DlcUtilTableEntry_Object = MibTableRow
dlcUtilTableEntry = _DlcUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1)
)
dlcUtilTableEntry.setIndexNames(
    (0, "DL-NEW-DSX1-MIB", "dlcUtilDLCINumber"),
)
if mibBuilder.loadTexts:
    dlcUtilTableEntry.setStatus("mandatory")
_DlcUtilDLCINumber_Type = Integer32
_DlcUtilDLCINumber_Object = MibTableColumn
dlcUtilDLCINumber = _DlcUtilDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 1),
    _DlcUtilDLCINumber_Type()
)
dlcUtilDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtilDLCINumber.setStatus("mandatory")
_DlcUtilEncodedValue_Type = OctetString
_DlcUtilEncodedValue_Object = MibTableColumn
dlcUtilEncodedValue = _DlcUtilEncodedValue_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 2),
    _DlcUtilEncodedValue_Type()
)
dlcUtilEncodedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtilEncodedValue.setStatus("mandatory")
_DlcUtilTimestamp_Type = Counter32
_DlcUtilTimestamp_Object = MibTableColumn
dlcUtilTimestamp = _DlcUtilTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 3),
    _DlcUtilTimestamp_Type()
)
dlcUtilTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtilTimestamp.setStatus("mandatory")
_DlcUtilLessThan20_Type = Counter32
_DlcUtilLessThan20_Object = MibTableColumn
dlcUtilLessThan20 = _DlcUtilLessThan20_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 4),
    _DlcUtilLessThan20_Type()
)
dlcUtilLessThan20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtilLessThan20.setStatus("mandatory")
_DlcUtil20_40_Type = Counter32
_DlcUtil20_40_Object = MibScalar
dlcUtil20_40 = _DlcUtil20_40_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 5),
    _DlcUtil20_40_Type()
)
dlcUtil20_40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtil20_40.setStatus("mandatory")
_DlcUtil40_60_Type = Counter32
_DlcUtil40_60_Object = MibScalar
dlcUtil40_60 = _DlcUtil40_60_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 6),
    _DlcUtil40_60_Type()
)
dlcUtil40_60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtil40_60.setStatus("mandatory")
_DlcUtil60_80_Type = Counter32
_DlcUtil60_80_Object = MibScalar
dlcUtil60_80 = _DlcUtil60_80_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 7),
    _DlcUtil60_80_Type()
)
dlcUtil60_80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtil60_80.setStatus("mandatory")
_DlcUtil80_100_Type = Counter32
_DlcUtil80_100_Object = MibScalar
dlcUtil80_100 = _DlcUtil80_100_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 8),
    _DlcUtil80_100_Type()
)
dlcUtil80_100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtil80_100.setStatus("mandatory")
_DlcUtilMoreThan100_Type = Counter32
_DlcUtilMoreThan100_Object = MibTableColumn
dlcUtilMoreThan100 = _DlcUtilMoreThan100_Object(
    (1, 3, 6, 1, 4, 1, 300, 200, 7, 1, 9),
    _DlcUtilMoreThan100_Type()
)
dlcUtilMoreThan100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlcUtilMoreThan100.setStatus("mandatory")

# Managed Objects groups


# Notification objects

startTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 200, 0, 1)
)
startTest.setObjects(
      *(("DL-NEW-DSX1-MIB", "dlcUnitTestPortId"),
        ("DL-NEW-DSX1-MIB", "dlcUnitTestType"))
)
if mibBuilder.loadTexts:
    startTest.setStatus(
        ""
    )

endTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 200, 0, 2)
)
endTest.setObjects(
      *(("DL-NEW-DSX1-MIB", "dlcUnitTestPortId"),
        ("DL-NEW-DSX1-MIB", "dlcUnitTestType"))
)
if mibBuilder.loadTexts:
    endTest.setStatus(
        ""
    )

startAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 200, 0, 3)
)
startAlarm.setObjects(
      *(("DL-NEW-DSX1-MIB", "dlcAlarmPort"),
        ("DL-NEW-DSX1-MIB", "dlcAlarmType"))
)
if mibBuilder.loadTexts:
    startAlarm.setStatus(
        ""
    )

endAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 200, 0, 4)
)
endAlarm.setObjects(
      *(("DL-NEW-DSX1-MIB", "dlcAlarmPort"),
        ("DL-NEW-DSX1-MIB", "dlcAlarmType"))
)
if mibBuilder.loadTexts:
    endAlarm.setStatus(
        ""
    )

manualConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 200, 0, 5)
)
if mibBuilder.loadTexts:
    manualConfigChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL-NEW-DSX1-MIB",
    **{"MacAddress": MacAddress,
       "Boolean": Boolean,
       "PortId": PortId,
       "AlarmType": AlarmType,
       "TestType": TestType,
       "LoopCodeType": LoopCodeType,
       "UnitStatusItem": UnitStatusItem,
       "PortStatusItem": PortStatusItem,
       "FramedUnframed": FramedUnframed,
       "RemoteCommunicationsMode": RemoteCommunicationsMode,
       "digital-link": digital_link,
       "dl-new-t1": dl_new_t1,
       "startTest": startTest,
       "endTest": endTest,
       "startAlarm": startAlarm,
       "endAlarm": endAlarm,
       "manualConfigChange": manualConfigChange,
       "dlcUnitHwConfig": dlcUnitHwConfig,
       "dlcUnitModelType": dlcUnitModelType,
       "dlcUnitHwRev": dlcUnitHwRev,
       "dlcUnitHwOptions": dlcUnitHwOptions,
       "dlcUnitSwRev": dlcUnitSwRev,
       "dlcUnitDataPorts": dlcUnitDataPorts,
       "dlcUnitRam": dlcUnitRam,
       "dlcUnitRom": dlcUnitRom,
       "dlcUnitFlash": dlcUnitFlash,
       "dlcUnitSlotNum": dlcUnitSlotNum,
       "dlcUnitMibRev": dlcUnitMibRev,
       "dlcUnitFeatures": dlcUnitFeatures,
       "dlcUnitConfig": dlcUnitConfig,
       "dlcUnitId": dlcUnitId,
       "dlcUnitProtectMode": dlcUnitProtectMode,
       "dlcUnitYellowEnable": dlcUnitYellowEnable,
       "dlcUnitNetPassFdl": dlcUnitNetPassFdl,
       "dlcUnitMainClockSource": dlcUnitMainClockSource,
       "dlcUnitAltClockSource": dlcUnitAltClockSource,
       "dlcUnitExtClockRate": dlcUnitExtClockRate,
       "dlcUnitFullBandwidthLoopCode": dlcUnitFullBandwidthLoopCode,
       "dlcUnitFractionalLoopCode": dlcUnitFractionalLoopCode,
       "dlcUnitTestLength": dlcUnitTestLength,
       "dlcUnitUserPattern1": dlcUnitUserPattern1,
       "dlcUnitUserPattern2": dlcUnitUserPattern2,
       "dlcUnitBlockAllAlarms": dlcUnitBlockAllAlarms,
       "dlcUnitDsx1TrapEnableTable": dlcUnitDsx1TrapEnableTable,
       "dlcDsx1TrapEnableEntry": dlcDsx1TrapEnableEntry,
       "dlcDsx1TrapPortId": dlcDsx1TrapPortId,
       "dlcDsx1BpvThresholdTrap": dlcDsx1BpvThresholdTrap,
       "dlcDsx1OofThresholdTrap": dlcDsx1OofThresholdTrap,
       "dlcDsx1CrcThresholdTrap": dlcDsx1CrcThresholdTrap,
       "dlcDsx1LossOfSignalTrapEnable": dlcDsx1LossOfSignalTrapEnable,
       "dlcDsx1LossOfSyncTrapEnable": dlcDsx1LossOfSyncTrapEnable,
       "dlcDsx1ReceiveAIStrapEnable": dlcDsx1ReceiveAIStrapEnable,
       "dlcDsx1ReceiveYellowAlarmTrapEnable": dlcDsx1ReceiveYellowAlarmTrapEnable,
       "dlcDsx1ReceiveRemoteAlarmTrapEnable": dlcDsx1ReceiveRemoteAlarmTrapEnable,
       "dlcDsx1PSfailureTrapEnable": dlcDsx1PSfailureTrapEnable,
       "dlcDsx1CntlCrdMissingTrapEnable": dlcDsx1CntlCrdMissingTrapEnable,
       "dlcDsx1FdlLinkTrapEnable": dlcDsx1FdlLinkTrapEnable,
       "dlcDsx1IbCrcThresholdTrap": dlcDsx1IbCrcThresholdTrap,
       "dlcDsx1InbandLinkTrapEnable": dlcDsx1InbandLinkTrapEnable,
       "dlcUnitDataDteLossTrapEnableTable": dlcUnitDataDteLossTrapEnableTable,
       "dlcDataDteLossTrapEnableEntry": dlcDataDteLossTrapEnableEntry,
       "dlcDataLossPortId": dlcDataLossPortId,
       "dlcDataLossEnable": dlcDataLossEnable,
       "dlcUnitExternalAlarmInputTrapEnable": dlcUnitExternalAlarmInputTrapEnable,
       "dlcUnitExternalAlarmInputContacts": dlcUnitExternalAlarmInputContacts,
       "dlcUnitExternalAlarmInputMessage": dlcUnitExternalAlarmInputMessage,
       "dlcUnitExternalAlarmOutputContacts": dlcUnitExternalAlarmOutputContacts,
       "dlcUnitExternalAlarmOutputTrapEnable": dlcUnitExternalAlarmOutputTrapEnable,
       "dlcUnitDsx1ConfigTable": dlcUnitDsx1ConfigTable,
       "dlcDsx1ConfigEntry": dlcDsx1ConfigEntry,
       "dlcDsx1ConfigPortId": dlcDsx1ConfigPortId,
       "dlcDsx1Framing": dlcDsx1Framing,
       "dlcDsx1LineCode": dlcDsx1LineCode,
       "dlcDsx1LineMatching": dlcDsx1LineMatching,
       "dlcDsx1DacsMode": dlcDsx1DacsMode,
       "dlcDsx1UseDlcFdlProtocol": dlcDsx1UseDlcFdlProtocol,
       "dlcDsx1UseAnsiProtocol": dlcDsx1UseAnsiProtocol,
       "dlcDsx1Bit7Stuffing": dlcDsx1Bit7Stuffing,
       "dlcDsx1InBandBit": dlcDsx1InBandBit,
       "dlcUnitDataDteConfigTable": dlcUnitDataDteConfigTable,
       "dlcDataDteConfigEntry": dlcDataDteConfigEntry,
       "dlcDataConfigPortId": dlcDataConfigPortId,
       "dlcDataConfigEncoding": dlcDataConfigEncoding,
       "dlcDataConfigLoss": dlcDataConfigLoss,
       "dlcDataConfigMode": dlcDataConfigMode,
       "dlcDataConfigFormat": dlcDataConfigFormat,
       "dlcDataConfigTransmitTiming": dlcDataConfigTransmitTiming,
       "dlcUnitMuxConfigTable": dlcUnitMuxConfigTable,
       "dlcMuxConfigEntry": dlcMuxConfigEntry,
       "dlcMuxConfigBusId": dlcMuxConfigBusId,
       "dlcMuxConfigSlotNumber": dlcMuxConfigSlotNumber,
       "dlcMuxConfigPortId": dlcMuxConfigPortId,
       "dlcUnitSnmpConfig": dlcUnitSnmpConfig,
       "dlcSnmpUnitIpAddr": dlcSnmpUnitIpAddr,
       "dlcSnmpUnitNetMask": dlcSnmpUnitNetMask,
       "dlcSnmpTrapAddr1": dlcSnmpTrapAddr1,
       "dlcSnmpTrapAddr2": dlcSnmpTrapAddr2,
       "dlcSnmpTrapAddr3": dlcSnmpTrapAddr3,
       "dlcSnmpTrapDlci1": dlcSnmpTrapDlci1,
       "dlcSnmpTrapDlci2": dlcSnmpTrapDlci2,
       "dlcSnmpTrapDlci3": dlcSnmpTrapDlci3,
       "dlcSnmpTrapDirection1": dlcSnmpTrapDirection1,
       "dlcSnmpTrapDirection2": dlcSnmpTrapDirection2,
       "dlcSnmpTrapDirection3": dlcSnmpTrapDirection3,
       "dlcSnmpTrapDirection": dlcSnmpTrapDirection,
       "dlcSnmpEthernetConfiguration": dlcSnmpEthernetConfiguration,
       "dlcEthernetIpAddr": dlcEthernetIpAddr,
       "dlcEthernetIpMask": dlcEthernetIpMask,
       "dlcEthernetGatewayAddr": dlcEthernetGatewayAddr,
       "dlcEthernetMacAddr": dlcEthernetMacAddr,
       "dlcUnitConfigTime": dlcUnitConfigTime,
       "dlcUnitTimeYear": dlcUnitTimeYear,
       "dlcUnitTimeMonth": dlcUnitTimeMonth,
       "dlcUnitTimeDay": dlcUnitTimeDay,
       "dlcUnitTimeHour": dlcUnitTimeHour,
       "dlcUnitTimeMinute": dlcUnitTimeMinute,
       "dlcUnitTimeSecond": dlcUnitTimeSecond,
       "dlcUnitSerialNum": dlcUnitSerialNum,
       "dlcUnitModemConfig": dlcUnitModemConfig,
       "dlcModemPhoneNum1": dlcModemPhoneNum1,
       "dlcModemPhoneNum2": dlcModemPhoneNum2,
       "dlcModemInitString1": dlcModemInitString1,
       "dlcModemInitString2": dlcModemInitString2,
       "dlcUnitInbandMode": dlcUnitInbandMode,
       "dlcUnitDialOutTimeInterval": dlcUnitDialOutTimeInterval,
       "dlcAlarmSignal": dlcAlarmSignal,
       "dlcUnitIdleCode": dlcUnitIdleCode,
       "dlcRemoteCommunicationsMode": dlcRemoteCommunicationsMode,
       "dlcUnitConfigLinkTest": dlcUnitConfigLinkTest,
       "dlcLinkTestState": dlcLinkTestState,
       "dlcLinkTestAddress": dlcLinkTestAddress,
       "dlcLinkTestDlci": dlcLinkTestDlci,
       "dlcLinkTestPort": dlcLinkTestPort,
       "dlcLinkTestLength": dlcLinkTestLength,
       "dlcLinkTestInterval": dlcLinkTestInterval,
       "dlcLinkTestPacketSize": dlcLinkTestPacketSize,
       "dlcLinkTestPattern": dlcLinkTestPattern,
       "dlcUnitInbandConfig": dlcUnitInbandConfig,
       "dlcUnitInbandTrafficType": dlcUnitInbandTrafficType,
       "dlcUnitPerformanceMonitoring": dlcUnitPerformanceMonitoring,
       "dlcUnitPvcAutoDiscovery": dlcUnitPvcAutoDiscovery,
       "dlcUnitDelayMonitorConfig": dlcUnitDelayMonitorConfig,
       "dlcDelayMonitorConfigTable": dlcDelayMonitorConfigTable,
       "dlcDelayMonitorConfigEntry": dlcDelayMonitorConfigEntry,
       "dlcDelayMonitorConfigIndex": dlcDelayMonitorConfigIndex,
       "dlcDelayMonitorState": dlcDelayMonitorState,
       "dlcDelayMonitorTargetAddress": dlcDelayMonitorTargetAddress,
       "dlcDelayMonitorDlci": dlcDelayMonitorDlci,
       "dlcDelayMonitorPort": dlcDelayMonitorPort,
       "dlcDelayMonitorInterval": dlcDelayMonitorInterval,
       "dlcDelayMonitorPacketSize": dlcDelayMonitorPacketSize,
       "dlcDelayMonitorPattern": dlcDelayMonitorPattern,
       "dlcDLCItable": dlcDLCItable,
       "dlcDLCItableEntry": dlcDLCItableEntry,
       "dlcDLCInumber": dlcDLCInumber,
       "dlcDTECIR": dlcDTECIR,
       "dlcNETCIR": dlcNETCIR,
       "dlcDLCIstatus": dlcDLCIstatus,
       "dlcLMIConditioningGroup": dlcLMIConditioningGroup,
       "dlcLMIConfiguration": dlcLMIConfiguration,
       "dlcLMIEnable": dlcLMIEnable,
       "dlcMaintenanceDLCI": dlcMaintenanceDLCI,
       "dlcManagementDLCI": dlcManagementDLCI,
       "dlcManagementDLCIEnable": dlcManagementDLCIEnable,
       "dlcSpoofingProtocolType": dlcSpoofingProtocolType,
       "dlcDTESpoofingEnable": dlcDTESpoofingEnable,
       "dlcNetSpoofingEnable": dlcNetSpoofingEnable,
       "dlcLinkIntegrityVerificationPollingTimer": dlcLinkIntegrityVerificationPollingTimer,
       "dlcFullStatusPollingCounter": dlcFullStatusPollingCounter,
       "dlcLMIErrorEvent": dlcLMIErrorEvent,
       "dlcLMIErrorMonitorEvent": dlcLMIErrorMonitorEvent,
       "dlcLMIErrorFreeEvent": dlcLMIErrorFreeEvent,
       "dlcLMIErrorFreeMonitorEvent": dlcLMIErrorFreeMonitorEvent,
       "dlcDTEResponseTimer": dlcDTEResponseTimer,
       "dlcLMIUnitLocation": dlcLMIUnitLocation,
       "dlcLMIStatus": dlcLMIStatus,
       "dlcSpoofingStatus": dlcSpoofingStatus,
       "dlcDTEInterfaceLMIStatus": dlcDTEInterfaceLMIStatus,
       "dlcNetInterfaceLMIStatus": dlcNetInterfaceLMIStatus,
       "dlcInbandDtePort": dlcInbandDtePort,
       "dlcUnitStatus": dlcUnitStatus,
       "dlcUnitCurrentStatus": dlcUnitCurrentStatus,
       "dlcUnitErrorFreeSeconds": dlcUnitErrorFreeSeconds,
       "dlcUnitLastSelfTestResult": dlcUnitLastSelfTestResult,
       "dlcUnitPortStatusTable": dlcUnitPortStatusTable,
       "dlcPortStatusEntry": dlcPortStatusEntry,
       "dlcPortStatusId": dlcPortStatusId,
       "dlcPortStatus": dlcPortStatus,
       "dlcPortStatusNetRxBwUtilization": dlcPortStatusNetRxBwUtilization,
       "dlcPortStatusNetTxBwUtilization": dlcPortStatusNetTxBwUtilization,
       "dlcUnitAlarmTable": dlcUnitAlarmTable,
       "dlcAlarmEntry": dlcAlarmEntry,
       "dlcAlarmPort": dlcAlarmPort,
       "dlcAlarmType": dlcAlarmType,
       "dlcUnitErrorSecondsRatio": dlcUnitErrorSecondsRatio,
       "dlcUnitSeverelyErroredSecondsRatio": dlcUnitSeverelyErroredSecondsRatio,
       "dlcUnitBackgroundBlockErrorRatio": dlcUnitBackgroundBlockErrorRatio,
       "dlcUnitUserArchive": dlcUnitUserArchive,
       "dlcUnitUserArchiveValidTable": dlcUnitUserArchiveValidTable,
       "dlcUserArchiveValidEntry": dlcUserArchiveValidEntry,
       "dlcValidPortId": dlcValidPortId,
       "dlcValidIntervals": dlcValidIntervals,
       "dlcUnitUserLifetimeTable": dlcUnitUserLifetimeTable,
       "dlcUserLifetimeEntry": dlcUserLifetimeEntry,
       "dlcLifetimePortId": dlcLifetimePortId,
       "dlcLifetimeES": dlcLifetimeES,
       "dlcLifetimeUAS": dlcLifetimeUAS,
       "dlcLifetimeCrcErrors": dlcLifetimeCrcErrors,
       "dlcLifetimeBpvErrors": dlcLifetimeBpvErrors,
       "dlcLifetimeOofErrors": dlcLifetimeOofErrors,
       "dlcLifetimeIbCrcErrors": dlcLifetimeIbCrcErrors,
       "dlcUnitUserCurrentTable": dlcUnitUserCurrentTable,
       "dlcUserCurrentEntry": dlcUserCurrentEntry,
       "dlcCurrentPortId": dlcCurrentPortId,
       "dlcCurrentES": dlcCurrentES,
       "dlcCurrentUAS": dlcCurrentUAS,
       "dlcCurrentCrcErrors": dlcCurrentCrcErrors,
       "dlcCurrentBpvErrors": dlcCurrentBpvErrors,
       "dlcCurrentOofErrors": dlcCurrentOofErrors,
       "dlcCurrentTimeElapsed": dlcCurrentTimeElapsed,
       "dlcCurrentIbCrcErrors": dlcCurrentIbCrcErrors,
       "dlcUnitUserArchiveTable": dlcUnitUserArchiveTable,
       "dlcUserArchiveEntry": dlcUserArchiveEntry,
       "dlcArchivePortId": dlcArchivePortId,
       "dlcArchiveInterval": dlcArchiveInterval,
       "dlcArchiveES": dlcArchiveES,
       "dlcArchiveUAS": dlcArchiveUAS,
       "dlcArchiveCrcErrors": dlcArchiveCrcErrors,
       "dlcArchiveBpvErrors": dlcArchiveBpvErrors,
       "dlcArchiveOofErrors": dlcArchiveOofErrors,
       "dlcArchiveIbCrcErrors": dlcArchiveIbCrcErrors,
       "dlcArchiveNetRxBwUtilization": dlcArchiveNetRxBwUtilization,
       "dlcArchiveNetRxPackets": dlcArchiveNetRxPackets,
       "dlcArchiveNetTxBwUtilization": dlcArchiveNetTxBwUtilization,
       "dlcArchiveNetTxPackets": dlcArchiveNetTxPackets,
       "dlcUnitTest": dlcUnitTest,
       "dlcUnitTestTable": dlcUnitTestTable,
       "dlcUnitTestEntry": dlcUnitTestEntry,
       "dlcUnitTestPortId": dlcUnitTestPortId,
       "dlcUnitTestType": dlcUnitTestType,
       "dlcUnitTestPatternStatus": dlcUnitTestPatternStatus,
       "dlcUnitTestPatternErrors": dlcUnitTestPatternErrors,
       "dlcLinkTestSentPackets": dlcLinkTestSentPackets,
       "dlcLinkTestReceivedPackets": dlcLinkTestReceivedPackets,
       "dlcLinkTestErroredPackets": dlcLinkTestErroredPackets,
       "dlcLinkTestMissingPackets": dlcLinkTestMissingPackets,
       "dlcLinkTestAverageRoundTrip": dlcLinkTestAverageRoundTrip,
       "dlcLinkTestMaximumRoundTrip": dlcLinkTestMaximumRoundTrip,
       "dlcUnitDelayMonitorStatus": dlcUnitDelayMonitorStatus,
       "dlcDelayMonitorStatusTable": dlcDelayMonitorStatusTable,
       "dlcDelayMonitorStatusEntry": dlcDelayMonitorStatusEntry,
       "dlcDelayMonitorStatusIndex": dlcDelayMonitorStatusIndex,
       "dlcDelayMonitorSentPackets": dlcDelayMonitorSentPackets,
       "dlcDelayMonitorReceivedPackets": dlcDelayMonitorReceivedPackets,
       "dlcDelayMonitorErroredPackets": dlcDelayMonitorErroredPackets,
       "dlcDelayMonitorMissingPackets": dlcDelayMonitorMissingPackets,
       "dlcDelayMonitorAverageRoundTrip": dlcDelayMonitorAverageRoundTrip,
       "dlcDelayMonitorMaximumRoundTrip": dlcDelayMonitorMaximumRoundTrip,
       "dlcUtilizationTable": dlcUtilizationTable,
       "dlcUtilTableEntry": dlcUtilTableEntry,
       "dlcUtilDLCINumber": dlcUtilDLCINumber,
       "dlcUtilEncodedValue": dlcUtilEncodedValue,
       "dlcUtilTimestamp": dlcUtilTimestamp,
       "dlcUtilLessThan20": dlcUtilLessThan20,
       "dlcUtil20-40": dlcUtil20_40,
       "dlcUtil40-60": dlcUtil40_60,
       "dlcUtil60-80": dlcUtil60_80,
       "dlcUtil80-100": dlcUtil80_100,
       "dlcUtilMoreThan100": dlcUtilMoreThan100}
)
