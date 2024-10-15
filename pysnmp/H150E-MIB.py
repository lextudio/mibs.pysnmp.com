# SNMP MIB module (H150E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H150E-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:35 2024
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

h150eOffice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class ReadWrite(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 2),
          ("readWrite", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SiemensUnits_ObjectIdentity = ObjectIdentity
siemensUnits = _SiemensUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7)
)
_Pn_ObjectIdentity = ObjectIdentity
pn = _Pn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2)
)
_H150eControlGroup_ObjectIdentity = ObjectIdentity
h150eControlGroup = _H150eControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1)
)


class _H150eSysState_Type(Integer32):
    """Custom type h150eSysState based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_H150eSysState_Type.__name__ = "Integer32"
_H150eSysState_Object = MibScalar
h150eSysState = _H150eSysState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 1),
    _H150eSysState_Type()
)
h150eSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eSysState.setStatus("current")
_TftpSwitchoverDateTime_Type = DateAndTime
_TftpSwitchoverDateTime_Object = MibScalar
tftpSwitchoverDateTime = _TftpSwitchoverDateTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 2),
    _TftpSwitchoverDateTime_Type()
)
tftpSwitchoverDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSwitchoverDateTime.setStatus("current")


class _TftpDownloadAction_Type(Integer32):
    """Custom type tftpDownloadAction based on Integer32"""
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
        *(("downloadAndDelayedSwitchover", 3),
          ("downloadAndImmediateSwitchover", 2),
          ("downloadWithoutSwitchover", 4),
          ("notDownloading", 1))
    )


_TftpDownloadAction_Type.__name__ = "Integer32"
_TftpDownloadAction_Object = MibScalar
tftpDownloadAction = _TftpDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 3),
    _TftpDownloadAction_Type()
)
tftpDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAction.setStatus("current")


class _H150eResetControl_Type(Integer32):
    """Custom type h150eResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("warmBoot", 2))
    )


_H150eResetControl_Type.__name__ = "Integer32"
_H150eResetControl_Object = MibScalar
h150eResetControl = _H150eResetControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 4),
    _H150eResetControl_Type()
)
h150eResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eResetControl.setStatus("current")


class _H150eSwitchoverState_Type(Integer32):
    """Custom type h150eSwitchoverState based on Integer32"""
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
        *(("initSwitchoverDelayed", 4),
          ("initSwitchoverNow", 3),
          ("notReadyForSwitchover", 2),
          ("readyForSwitchover", 1))
    )


_H150eSwitchoverState_Type.__name__ = "Integer32"
_H150eSwitchoverState_Object = MibScalar
h150eSwitchoverState = _H150eSwitchoverState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 5),
    _H150eSwitchoverState_Type()
)
h150eSwitchoverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eSwitchoverState.setStatus("current")


class _H150eShadowFlashState_Type(Integer32):
    """Custom type h150eShadowFlashState based on Integer32"""
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
        *(("deleteFlashNow", 5),
          ("flashDeleted", 1),
          ("flashNotDeleted", 2),
          ("flashTooSmall", 4),
          ("flashWriteProtected", 3))
    )


_H150eShadowFlashState_Type.__name__ = "Integer32"
_H150eShadowFlashState_Object = MibScalar
h150eShadowFlashState = _H150eShadowFlashState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 6),
    _H150eShadowFlashState_Type()
)
h150eShadowFlashState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eShadowFlashState.setStatus("current")


class _H150eLoadLevel_Type(Integer32):
    """Custom type h150eLoadLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H150eLoadLevel_Type.__name__ = "Integer32"
_H150eLoadLevel_Object = MibScalar
h150eLoadLevel = _H150eLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 7),
    _H150eLoadLevel_Type()
)
h150eLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eLoadLevel.setStatus("current")


class _H150eTrapRepetitions_Type(Integer32):
    """Custom type h150eTrapRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_H150eTrapRepetitions_Type.__name__ = "Integer32"
_H150eTrapRepetitions_Object = MibScalar
h150eTrapRepetitions = _H150eTrapRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 8),
    _H150eTrapRepetitions_Type()
)
h150eTrapRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eTrapRepetitions.setStatus("current")


class _H150eCdrBufferState_Type(Integer32):
    """Custom type h150eCdrBufferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("deleteBufferNow", 2),
          ("notAccounting", 3))
    )


_H150eCdrBufferState_Type.__name__ = "Integer32"
_H150eCdrBufferState_Object = MibScalar
h150eCdrBufferState = _H150eCdrBufferState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 9),
    _H150eCdrBufferState_Type()
)
h150eCdrBufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrBufferState.setStatus("current")


class _H150eLogBufferState_Type(Integer32):
    """Custom type h150eLogBufferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteBufferNow", 2),
          ("logging", 1))
    )


_H150eLogBufferState_Type.__name__ = "Integer32"
_H150eLogBufferState_Object = MibScalar
h150eLogBufferState = _H150eLogBufferState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 10),
    _H150eLogBufferState_Type()
)
h150eLogBufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eLogBufferState.setStatus("current")
_H150eErrorHistoryGroup_ObjectIdentity = ObjectIdentity
h150eErrorHistoryGroup = _H150eErrorHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2)
)


class _NumberOfErrorHistoryEntries_Type(Integer32):
    """Custom type numberOfErrorHistoryEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_NumberOfErrorHistoryEntries_Type.__name__ = "Integer32"
_NumberOfErrorHistoryEntries_Object = MibScalar
numberOfErrorHistoryEntries = _NumberOfErrorHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 1),
    _NumberOfErrorHistoryEntries_Type()
)
numberOfErrorHistoryEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfErrorHistoryEntries.setStatus("current")
_H150eErrorHistoryTable_Object = MibTable
h150eErrorHistoryTable = _H150eErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    h150eErrorHistoryTable.setStatus("current")
_H150eErrorHistoryEntry_Object = MibTableRow
h150eErrorHistoryEntry = _H150eErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1)
)
h150eErrorHistoryEntry.setIndexNames(
    (0, "H150E-MIB", "h150eErrorIndex"),
)
if mibBuilder.loadTexts:
    h150eErrorHistoryEntry.setStatus("current")


class _H150eErrorIndex_Type(Integer32):
    """Custom type h150eErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eErrorIndex_Type.__name__ = "Integer32"
_H150eErrorIndex_Object = MibTableColumn
h150eErrorIndex = _H150eErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 1),
    _H150eErrorIndex_Type()
)
h150eErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorIndex.setStatus("current")
_H150eErrorDateTime_Type = DateAndTime
_H150eErrorDateTime_Object = MibTableColumn
h150eErrorDateTime = _H150eErrorDateTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 2),
    _H150eErrorDateTime_Type()
)
h150eErrorDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorDateTime.setStatus("current")


class _H150eErrorClass_Type(Integer32):
    """Custom type h150eErrorClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eErrorClass_Type.__name__ = "Integer32"
_H150eErrorClass_Object = MibTableColumn
h150eErrorClass = _H150eErrorClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 3),
    _H150eErrorClass_Type()
)
h150eErrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorClass.setStatus("current")


class _H150eErrorCode_Type(Integer32):
    """Custom type h150eErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eErrorCode_Type.__name__ = "Integer32"
_H150eErrorCode_Object = MibTableColumn
h150eErrorCode = _H150eErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 4),
    _H150eErrorCode_Type()
)
h150eErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorCode.setStatus("current")


class _H150eAccessSlot_Type(Integer32):
    """Custom type h150eAccessSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eAccessSlot_Type.__name__ = "Integer32"
_H150eAccessSlot_Object = MibTableColumn
h150eAccessSlot = _H150eAccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 5),
    _H150eAccessSlot_Type()
)
h150eAccessSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eAccessSlot.setStatus("current")


class _H150eAccessPort_Type(Integer32):
    """Custom type h150eAccessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eAccessPort_Type.__name__ = "Integer32"
_H150eAccessPort_Object = MibTableColumn
h150eAccessPort = _H150eAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 6),
    _H150eAccessPort_Type()
)
h150eAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eAccessPort.setStatus("current")


class _H150eErrorDescription_Type(DisplayString):
    """Custom type h150eErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H150eErrorDescription_Type.__name__ = "DisplayString"
_H150eErrorDescription_Object = MibTableColumn
h150eErrorDescription = _H150eErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 7),
    _H150eErrorDescription_Type()
)
h150eErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorDescription.setStatus("current")


class _H150eErrorSeverity_Type(Integer32):
    """Custom type h150eErrorSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_H150eErrorSeverity_Type.__name__ = "Integer32"
_H150eErrorSeverity_Object = MibTableColumn
h150eErrorSeverity = _H150eErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 8),
    _H150eErrorSeverity_Type()
)
h150eErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eErrorSeverity.setStatus("current")
_H150eSystemInfoGroup_ObjectIdentity = ObjectIdentity
h150eSystemInfoGroup = _H150eSystemInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3)
)


class _SysHardwareVersion_Type(DisplayString):
    """Custom type sysHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SysHardwareVersion_Type.__name__ = "DisplayString"
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 1),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("current")


class _SysSoftwareVersion_Type(DisplayString):
    """Custom type sysSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SysSoftwareVersion_Type.__name__ = "DisplayString"
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 2),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("current")


class _SysCodeNumber_Type(DisplayString):
    """Custom type sysCodeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SysCodeNumber_Type.__name__ = "DisplayString"
_SysCodeNumber_Object = MibScalar
sysCodeNumber = _SysCodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 3),
    _SysCodeNumber_Type()
)
sysCodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCodeNumber.setStatus("current")


class _SysSoftwareLocation_Type(Integer32):
    """Custom type sysSoftwareLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_SysSoftwareLocation_Type.__name__ = "Integer32"
_SysSoftwareLocation_Object = MibScalar
sysSoftwareLocation = _SysSoftwareLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 4),
    _SysSoftwareLocation_Type()
)
sysSoftwareLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareLocation.setStatus("current")


class _NumberOfSlotTableEntries_Type(Integer32):
    """Custom type numberOfSlotTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_NumberOfSlotTableEntries_Type.__name__ = "Integer32"
_NumberOfSlotTableEntries_Object = MibScalar
numberOfSlotTableEntries = _NumberOfSlotTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 5),
    _NumberOfSlotTableEntries_Type()
)
numberOfSlotTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSlotTableEntries.setStatus("current")
_H150eSlotTable_Object = MibTable
h150eSlotTable = _H150eSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    h150eSlotTable.setStatus("current")
_H150eSlotTableEntry_Object = MibTableRow
h150eSlotTableEntry = _H150eSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1)
)
h150eSlotTableEntry.setIndexNames(
    (0, "H150E-MIB", "cardIndex"),
)
if mibBuilder.loadTexts:
    h150eSlotTableEntry.setStatus("current")


class _CardIndex_Type(Integer32):
    """Custom type cardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_CardIndex_Type.__name__ = "Integer32"
_CardIndex_Object = MibTableColumn
cardIndex = _CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 1),
    _CardIndex_Type()
)
cardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndex.setStatus("current")


class _CardBoxNum_Type(Integer32):
    """Custom type cardBoxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_CardBoxNum_Type.__name__ = "Integer32"
_CardBoxNum_Object = MibTableColumn
cardBoxNum = _CardBoxNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 2),
    _CardBoxNum_Type()
)
cardBoxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBoxNum.setStatus("current")


class _CardSlotNum_Type(Integer32):
    """Custom type cardSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_CardSlotNum_Type.__name__ = "Integer32"
_CardSlotNum_Object = MibTableColumn
cardSlotNum = _CardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 3),
    _CardSlotNum_Type()
)
cardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSlotNum.setStatus("current")


class _CardType_Type(DisplayString):
    """Custom type cardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CardType_Type.__name__ = "DisplayString"
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 4),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("current")


class _CardDescription_Type(DisplayString):
    """Custom type cardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CardDescription_Type.__name__ = "DisplayString"
_CardDescription_Object = MibTableColumn
cardDescription = _CardDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 5),
    _CardDescription_Type()
)
cardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDescription.setStatus("current")


class _CardCodeNumber_Type(DisplayString):
    """Custom type cardCodeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_CardCodeNumber_Type.__name__ = "DisplayString"
_CardCodeNumber_Object = MibTableColumn
cardCodeNumber = _CardCodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 6),
    _CardCodeNumber_Type()
)
cardCodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCodeNumber.setStatus("current")


class _CardState_Type(Integer32):
    """Custom type cardState based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_CardState_Type.__name__ = "Integer32"
_CardState_Object = MibTableColumn
cardState = _CardState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 7),
    _CardState_Type()
)
cardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardState.setStatus("current")


class _NumberOfPortTableEntries_Type(Integer32):
    """Custom type numberOfPortTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_NumberOfPortTableEntries_Type.__name__ = "Integer32"
_NumberOfPortTableEntries_Object = MibScalar
numberOfPortTableEntries = _NumberOfPortTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 7),
    _NumberOfPortTableEntries_Type()
)
numberOfPortTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPortTableEntries.setStatus("current")
_H150ePortTable_Object = MibTable
h150ePortTable = _H150ePortTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8)
)
if mibBuilder.loadTexts:
    h150ePortTable.setStatus("current")
_H150ePortTableEntry_Object = MibTableRow
h150ePortTableEntry = _H150ePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1)
)
h150ePortTableEntry.setIndexNames(
    (0, "H150E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    h150ePortTableEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortCardIndex_Type(Integer32):
    """Custom type portCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_PortCardIndex_Type.__name__ = "Integer32"
_PortCardIndex_Object = MibTableColumn
portCardIndex = _PortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 2),
    _PortCardIndex_Type()
)
portCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardIndex.setStatus("current")


class _PortType_Type(DisplayString):
    """Custom type portType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_PortType_Type.__name__ = "DisplayString"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortState_Type(Integer32):
    """Custom type portState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PortState_Type.__name__ = "Integer32"
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 4),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("current")


class _PortLock_Type(Integer32):
    """Custom type portLock based on Integer32"""
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
        *(("lockedByHardware", 3),
          ("lockedBySoftAndHardware", 4),
          ("lockedBySoftware", 2),
          ("unlocked", 1))
    )


_PortLock_Type.__name__ = "Integer32"
_PortLock_Object = MibTableColumn
portLock = _PortLock_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 5),
    _PortLock_Type()
)
portLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLock.setStatus("current")


class _PortLogicalPortNumber_Type(Integer32):
    """Custom type portLogicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_PortLogicalPortNumber_Type.__name__ = "Integer32"
_PortLogicalPortNumber_Object = MibTableColumn
portLogicalPortNumber = _PortLogicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 6),
    _PortLogicalPortNumber_Type()
)
portLogicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLogicalPortNumber.setStatus("current")


class _NumberOfExtensionTableEntries_Type(Integer32):
    """Custom type numberOfExtensionTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_NumberOfExtensionTableEntries_Type.__name__ = "Integer32"
_NumberOfExtensionTableEntries_Object = MibScalar
numberOfExtensionTableEntries = _NumberOfExtensionTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 9),
    _NumberOfExtensionTableEntries_Type()
)
numberOfExtensionTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfExtensionTableEntries.setStatus("current")
_H150eExtensionTable_Object = MibTable
h150eExtensionTable = _H150eExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10)
)
if mibBuilder.loadTexts:
    h150eExtensionTable.setStatus("current")
_H150eExtensionTableEntry_Object = MibTableRow
h150eExtensionTableEntry = _H150eExtensionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1)
)
h150eExtensionTableEntry.setIndexNames(
    (0, "H150E-MIB", "extensionIndex"),
)
if mibBuilder.loadTexts:
    h150eExtensionTableEntry.setStatus("current")


class _ExtensionIndex_Type(Integer32):
    """Custom type extensionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_ExtensionIndex_Type.__name__ = "Integer32"
_ExtensionIndex_Object = MibTableColumn
extensionIndex = _ExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 1),
    _ExtensionIndex_Type()
)
extensionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionIndex.setStatus("current")


class _ExtensionDescription_Type(DisplayString):
    """Custom type extensionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ExtensionDescription_Type.__name__ = "DisplayString"
_ExtensionDescription_Object = MibTableColumn
extensionDescription = _ExtensionDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 2),
    _ExtensionDescription_Type()
)
extensionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionDescription.setStatus("current")


class _ExtensionCodeNumber_Type(DisplayString):
    """Custom type extensionCodeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ExtensionCodeNumber_Type.__name__ = "DisplayString"
_ExtensionCodeNumber_Object = MibTableColumn
extensionCodeNumber = _ExtensionCodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 3),
    _ExtensionCodeNumber_Type()
)
extensionCodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionCodeNumber.setStatus("current")


class _NumberOfLanConnTableEntries_Type(Integer32):
    """Custom type numberOfLanConnTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_NumberOfLanConnTableEntries_Type.__name__ = "Integer32"
_NumberOfLanConnTableEntries_Object = MibScalar
numberOfLanConnTableEntries = _NumberOfLanConnTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 11),
    _NumberOfLanConnTableEntries_Type()
)
numberOfLanConnTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfLanConnTableEntries.setStatus("current")
_H150eLanConnTable_Object = MibTable
h150eLanConnTable = _H150eLanConnTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12)
)
if mibBuilder.loadTexts:
    h150eLanConnTable.setStatus("current")
_H150eLanConnTableEntry_Object = MibTableRow
h150eLanConnTableEntry = _H150eLanConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1)
)
h150eLanConnTableEntry.setIndexNames(
    (0, "H150E-MIB", "lanConnIndex"),
)
if mibBuilder.loadTexts:
    h150eLanConnTableEntry.setStatus("current")


class _LanConnIndex_Type(Integer32):
    """Custom type lanConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_LanConnIndex_Type.__name__ = "Integer32"
_LanConnIndex_Object = MibTableColumn
lanConnIndex = _LanConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 1),
    _LanConnIndex_Type()
)
lanConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanConnIndex.setStatus("current")


class _LanConnDescription_Type(DisplayString):
    """Custom type lanConnDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LanConnDescription_Type.__name__ = "DisplayString"
_LanConnDescription_Object = MibTableColumn
lanConnDescription = _LanConnDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 2),
    _LanConnDescription_Type()
)
lanConnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanConnDescription.setStatus("current")
_LanConnIpAddress_Type = IpAddress
_LanConnIpAddress_Object = MibTableColumn
lanConnIpAddress = _LanConnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 3),
    _LanConnIpAddress_Type()
)
lanConnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanConnIpAddress.setStatus("current")
_LanConnSubnetMask_Type = IpAddress
_LanConnSubnetMask_Object = MibTableColumn
lanConnSubnetMask = _LanConnSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 4),
    _LanConnSubnetMask_Type()
)
lanConnSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanConnSubnetMask.setStatus("current")


class _LanConnStatus_Type(Integer32):
    """Custom type lanConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LanConnStatus_Type.__name__ = "Integer32"
_LanConnStatus_Object = MibTableColumn
lanConnStatus = _LanConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 5),
    _LanConnStatus_Type()
)
lanConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanConnStatus.setStatus("current")
_HiPathAllServeServerIpAddress_Type = IpAddress
_HiPathAllServeServerIpAddress_Object = MibScalar
hiPathAllServeServerIpAddress = _HiPathAllServeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 13),
    _HiPathAllServeServerIpAddress_Type()
)
hiPathAllServeServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPathAllServeServerIpAddress.setStatus("current")


class _IndexOfLastPortStatusNotificationTrap_Type(Integer32):
    """Custom type indexOfLastPortStatusNotificationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_IndexOfLastPortStatusNotificationTrap_Type.__name__ = "Integer32"
_IndexOfLastPortStatusNotificationTrap_Object = MibScalar
indexOfLastPortStatusNotificationTrap = _IndexOfLastPortStatusNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 14),
    _IndexOfLastPortStatusNotificationTrap_Type()
)
indexOfLastPortStatusNotificationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    indexOfLastPortStatusNotificationTrap.setStatus("current")


class _SysSnmpAgentVersion_Type(DisplayString):
    """Custom type sysSnmpAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSnmpAgentVersion_Type.__name__ = "DisplayString"
_SysSnmpAgentVersion_Object = MibScalar
sysSnmpAgentVersion = _SysSnmpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 15),
    _SysSnmpAgentVersion_Type()
)
sysSnmpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnmpAgentVersion.setStatus("current")


class _SysShadowSoftwareVersion_Type(DisplayString):
    """Custom type sysShadowSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SysShadowSoftwareVersion_Type.__name__ = "DisplayString"
_SysShadowSoftwareVersion_Object = MibScalar
sysShadowSoftwareVersion = _SysShadowSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 16),
    _SysShadowSoftwareVersion_Type()
)
sysShadowSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysShadowSoftwareVersion.setStatus("current")


class _SysHiPathSymbolSubInfo_Type(DisplayString):
    """Custom type sysHiPathSymbolSubInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHiPathSymbolSubInfo_Type.__name__ = "DisplayString"
_SysHiPathSymbolSubInfo_Object = MibScalar
sysHiPathSymbolSubInfo = _SysHiPathSymbolSubInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 17),
    _SysHiPathSymbolSubInfo_Type()
)
sysHiPathSymbolSubInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHiPathSymbolSubInfo.setStatus("current")


class _SysHiPathBranding_Type(DisplayString):
    """Custom type sysHiPathBranding based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHiPathBranding_Type.__name__ = "DisplayString"
_SysHiPathBranding_Object = MibScalar
sysHiPathBranding = _SysHiPathBranding_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 18),
    _SysHiPathBranding_Type()
)
sysHiPathBranding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHiPathBranding.setStatus("current")


class _SysTimezoneOffset_Type(Integer32):
    """Custom type sysTimezoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1440, 1440),
    )


_SysTimezoneOffset_Type.__name__ = "Integer32"
_SysTimezoneOffset_Object = MibScalar
sysTimezoneOffset = _SysTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 19),
    _SysTimezoneOffset_Type()
)
sysTimezoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimezoneOffset.setStatus("current")
_H150eStatisticsGroup_ObjectIdentity = ObjectIdentity
h150eStatisticsGroup = _H150eStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4)
)


class _NumberOfFeatureStatTableEntries_Type(Integer32):
    """Custom type numberOfFeatureStatTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_NumberOfFeatureStatTableEntries_Type.__name__ = "Integer32"
_NumberOfFeatureStatTableEntries_Object = MibScalar
numberOfFeatureStatTableEntries = _NumberOfFeatureStatTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 1),
    _NumberOfFeatureStatTableEntries_Type()
)
numberOfFeatureStatTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfFeatureStatTableEntries.setStatus("current")
_H150eFeatureStatTable_Object = MibTable
h150eFeatureStatTable = _H150eFeatureStatTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    h150eFeatureStatTable.setStatus("current")
_H150eFeatureStatEntry_Object = MibTableRow
h150eFeatureStatEntry = _H150eFeatureStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1)
)
h150eFeatureStatEntry.setIndexNames(
    (0, "H150E-MIB", "featureIndex"),
)
if mibBuilder.loadTexts:
    h150eFeatureStatEntry.setStatus("current")


class _FeatureIndex_Type(Integer32):
    """Custom type featureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_FeatureIndex_Type.__name__ = "Integer32"
_FeatureIndex_Object = MibTableColumn
featureIndex = _FeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 1),
    _FeatureIndex_Type()
)
featureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureIndex.setStatus("current")


class _FeatureDescription_Type(DisplayString):
    """Custom type featureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FeatureDescription_Type.__name__ = "DisplayString"
_FeatureDescription_Object = MibTableColumn
featureDescription = _FeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 2),
    _FeatureDescription_Type()
)
featureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureDescription.setStatus("current")


class _FeatureCounter_Type(Integer32):
    """Custom type featureCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_FeatureCounter_Type.__name__ = "Integer32"
_FeatureCounter_Object = MibTableColumn
featureCounter = _FeatureCounter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 3),
    _FeatureCounter_Type()
)
featureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureCounter.setStatus("current")


class _FeatureStatTableReset_Type(Integer32):
    """Custom type featureStatTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("counting", 1),
          ("reset", 2))
    )


_FeatureStatTableReset_Type.__name__ = "Integer32"
_FeatureStatTableReset_Object = MibScalar
featureStatTableReset = _FeatureStatTableReset_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 3),
    _FeatureStatTableReset_Type()
)
featureStatTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureStatTableReset.setStatus("current")
_H150eCdrConfigGroup_ObjectIdentity = ObjectIdentity
h150eCdrConfigGroup = _H150eCdrConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5)
)


class _H150eCdrSeparator_Type(Integer32):
    """Custom type h150eCdrSeparator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dosMode", 1),
          ("unixMode", 2))
    )


_H150eCdrSeparator_Type.__name__ = "Integer32"
_H150eCdrSeparator_Object = MibScalar
h150eCdrSeparator = _H150eCdrSeparator_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 1),
    _H150eCdrSeparator_Type()
)
h150eCdrSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrSeparator.setStatus("current")


class _H150eCdrElementSeparator_Type(Integer32):
    """Custom type h150eCdrElementSeparator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              59,
              124)
        )
    )
    namedValues = NamedValues(
        *(("blank", 32),
          ("pipe", 124),
          ("semicolon", 59))
    )


_H150eCdrElementSeparator_Type.__name__ = "Integer32"
_H150eCdrElementSeparator_Object = MibScalar
h150eCdrElementSeparator = _H150eCdrElementSeparator_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 2),
    _H150eCdrElementSeparator_Type()
)
h150eCdrElementSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrElementSeparator.setStatus("current")


class _H150eCdrThresholdValue_Type(Integer32):
    """Custom type h150eCdrThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eCdrThresholdValue_Type.__name__ = "Integer32"
_H150eCdrThresholdValue_Object = MibScalar
h150eCdrThresholdValue = _H150eCdrThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 3),
    _H150eCdrThresholdValue_Type()
)
h150eCdrThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrThresholdValue.setStatus("current")


class _H150eCdrTftpFileCounter_Type(Integer32):
    """Custom type h150eCdrTftpFileCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eCdrTftpFileCounter_Type.__name__ = "Integer32"
_H150eCdrTftpFileCounter_Object = MibScalar
h150eCdrTftpFileCounter = _H150eCdrTftpFileCounter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 4),
    _H150eCdrTftpFileCounter_Type()
)
h150eCdrTftpFileCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTftpFileCounter.setStatus("current")
_H150eCdrTftpServerDestAddress_Type = IpAddress
_H150eCdrTftpServerDestAddress_Object = MibScalar
h150eCdrTftpServerDestAddress = _H150eCdrTftpServerDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 5),
    _H150eCdrTftpServerDestAddress_Type()
)
h150eCdrTftpServerDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTftpServerDestAddress.setStatus("current")
_H150eCdrTftpServerAlternateDestAddress_Type = IpAddress
_H150eCdrTftpServerAlternateDestAddress_Object = MibScalar
h150eCdrTftpServerAlternateDestAddress = _H150eCdrTftpServerAlternateDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 6),
    _H150eCdrTftpServerAlternateDestAddress_Type()
)
h150eCdrTftpServerAlternateDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTftpServerAlternateDestAddress.setStatus("current")


class _H150eCdrTftpClientTimer_Type(Integer32):
    """Custom type h150eCdrTftpClientTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eCdrTftpClientTimer_Type.__name__ = "Integer32"
_H150eCdrTftpClientTimer_Object = MibScalar
h150eCdrTftpClientTimer = _H150eCdrTftpClientTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 7),
    _H150eCdrTftpClientTimer_Type()
)
h150eCdrTftpClientTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTftpClientTimer.setStatus("current")
_H150eCdrTcpServerDestAddress_Type = IpAddress
_H150eCdrTcpServerDestAddress_Object = MibScalar
h150eCdrTcpServerDestAddress = _H150eCdrTcpServerDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 8),
    _H150eCdrTcpServerDestAddress_Type()
)
h150eCdrTcpServerDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTcpServerDestAddress.setStatus("current")


class _H150eCdrTcpServerDestPort_Type(Integer32):
    """Custom type h150eCdrTcpServerDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eCdrTcpServerDestPort_Type.__name__ = "Integer32"
_H150eCdrTcpServerDestPort_Object = MibScalar
h150eCdrTcpServerDestPort = _H150eCdrTcpServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 9),
    _H150eCdrTcpServerDestPort_Type()
)
h150eCdrTcpServerDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrTcpServerDestPort.setStatus("current")


class _H150eCdrOutputMode_Type(Integer32):
    """Custom type h150eCdrOutputMode based on Integer32"""
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
        *(("noOutput", 7),
          ("pCVPLport", 3),
          ("tcpClient", 6),
          ("tftpClient", 4),
          ("tftpServer", 5),
          ("uPNport", 2),
          ("v24port", 1))
    )


_H150eCdrOutputMode_Type.__name__ = "Integer32"
_H150eCdrOutputMode_Object = MibScalar
h150eCdrOutputMode = _H150eCdrOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 10),
    _H150eCdrOutputMode_Type()
)
h150eCdrOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eCdrOutputMode.setStatus("current")


class _H150eIndexOfLastCdrNotificationTrap_Type(Integer32):
    """Custom type h150eIndexOfLastCdrNotificationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150eIndexOfLastCdrNotificationTrap_Type.__name__ = "Integer32"
_H150eIndexOfLastCdrNotificationTrap_Object = MibScalar
h150eIndexOfLastCdrNotificationTrap = _H150eIndexOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 11),
    _H150eIndexOfLastCdrNotificationTrap_Type()
)
h150eIndexOfLastCdrNotificationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h150eIndexOfLastCdrNotificationTrap.setStatus("current")


class _H150etypeOfLastCdrNotificationTrap_Type(Integer32):
    """Custom type h150etypeOfLastCdrNotificationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_H150etypeOfLastCdrNotificationTrap_Type.__name__ = "Integer32"
_H150etypeOfLastCdrNotificationTrap_Object = MibScalar
h150etypeOfLastCdrNotificationTrap = _H150etypeOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 12),
    _H150etypeOfLastCdrNotificationTrap_Type()
)
h150etypeOfLastCdrNotificationTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150etypeOfLastCdrNotificationTrap.setStatus("current")


class _H150eDescriptionOfLastCdrNotificationTrap_Type(DisplayString):
    """Custom type h150eDescriptionOfLastCdrNotificationTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H150eDescriptionOfLastCdrNotificationTrap_Type.__name__ = "DisplayString"
_H150eDescriptionOfLastCdrNotificationTrap_Object = MibScalar
h150eDescriptionOfLastCdrNotificationTrap = _H150eDescriptionOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 13),
    _H150eDescriptionOfLastCdrNotificationTrap_Type()
)
h150eDescriptionOfLastCdrNotificationTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h150eDescriptionOfLastCdrNotificationTrap.setStatus("current")
_H150eTrapSpecifications_ObjectIdentity = ObjectIdentity
h150eTrapSpecifications = _H150eTrapSpecifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6)
)
_UmProxyGroup_ObjectIdentity = ObjectIdentity
umProxyGroup = _UmProxyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8)
)
_UmNodeNumber_Type = DisplayString
_UmNodeNumber_Object = MibScalar
umNodeNumber = _UmNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 1),
    _UmNodeNumber_Type()
)
umNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umNodeNumber.setStatus("current")


class _UmSrsEnabled_Type(Integer32):
    """Custom type umSrsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UmSrsEnabled_Type.__name__ = "Integer32"
_UmSrsEnabled_Object = MibScalar
umSrsEnabled = _UmSrsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 2),
    _UmSrsEnabled_Type()
)
umSrsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umSrsEnabled.setStatus("current")


class _UmDefaultLanguage_Type(Integer32):
    """Custom type umDefaultLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("french", 3),
          ("german", 1))
    )


_UmDefaultLanguage_Type.__name__ = "Integer32"
_UmDefaultLanguage_Object = MibScalar
umDefaultLanguage = _UmDefaultLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 3),
    _UmDefaultLanguage_Type()
)
umDefaultLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umDefaultLanguage.setStatus("current")


class _UmNumberOfSubscriberEntries_Type(Integer32):
    """Custom type umNumberOfSubscriberEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_UmNumberOfSubscriberEntries_Type.__name__ = "Integer32"
_UmNumberOfSubscriberEntries_Object = MibScalar
umNumberOfSubscriberEntries = _UmNumberOfSubscriberEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 4),
    _UmNumberOfSubscriberEntries_Type()
)
umNumberOfSubscriberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umNumberOfSubscriberEntries.setStatus("current")
_UmSubscriberTable_Object = MibTable
umSubscriberTable = _UmSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5)
)
if mibBuilder.loadTexts:
    umSubscriberTable.setStatus("current")
_UmSubscriberTableEntry_Object = MibTableRow
umSubscriberTableEntry = _UmSubscriberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1)
)
umSubscriberTableEntry.setIndexNames(
    (0, "H150E-MIB", "umLogicalPortNumber"),
)
if mibBuilder.loadTexts:
    umSubscriberTableEntry.setStatus("current")


class _UmLogicalPortNumber_Type(Integer32):
    """Custom type umLogicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_UmLogicalPortNumber_Type.__name__ = "Integer32"
_UmLogicalPortNumber_Object = MibTableColumn
umLogicalPortNumber = _UmLogicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 1),
    _UmLogicalPortNumber_Type()
)
umLogicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umLogicalPortNumber.setStatus("current")
_UmInternalCallNumber_Type = DisplayString
_UmInternalCallNumber_Object = MibTableColumn
umInternalCallNumber = _UmInternalCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 2),
    _UmInternalCallNumber_Type()
)
umInternalCallNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umInternalCallNumber.setStatus("current")
_UmDIDNumber_Type = DisplayString
_UmDIDNumber_Object = MibTableColumn
umDIDNumber = _UmDIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 3),
    _UmDIDNumber_Type()
)
umDIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umDIDNumber.setStatus("current")
_UmE164Number_Type = DisplayString
_UmE164Number_Object = MibTableColumn
umE164Number = _UmE164Number_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 4),
    _UmE164Number_Type()
)
umE164Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umE164Number.setStatus("current")
_UmDisplayName_Type = DisplayString
_UmDisplayName_Object = MibTableColumn
umDisplayName = _UmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 5),
    _UmDisplayName_Type()
)
umDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umDisplayName.setStatus("current")


class _UmStationType_Type(Integer32):
    """Custom type umStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("hfa", 2),
          ("s0", 0),
          ("up0", 1))
    )


_UmStationType_Type.__name__ = "Integer32"
_UmStationType_Object = MibTableColumn
umStationType = _UmStationType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 6),
    _UmStationType_Type()
)
umStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umStationType.setStatus("current")


class _UmPortStatus_Type(Integer32):
    """Custom type umPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_UmPortStatus_Type.__name__ = "Integer32"
_UmPortStatus_Object = MibTableColumn
umPortStatus = _UmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 7),
    _UmPortStatus_Type()
)
umPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umPortStatus.setStatus("current")


class _UmClassOfService_Type(Integer32):
    """Custom type umClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UmClassOfService_Type.__name__ = "Integer32"
_UmClassOfService_Object = MibTableColumn
umClassOfService = _UmClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 8),
    _UmClassOfService_Type()
)
umClassOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umClassOfService.setStatus("current")


class _UmDisplayLanguage_Type(Integer32):
    """Custom type umDisplayLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("french", 3),
          ("german", 1))
    )


_UmDisplayLanguage_Type.__name__ = "Integer32"
_UmDisplayLanguage_Object = MibTableColumn
umDisplayLanguage = _UmDisplayLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 9),
    _UmDisplayLanguage_Type()
)
umDisplayLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umDisplayLanguage.setStatus("current")
_UmCfssTarget_Type = DisplayString
_UmCfssTarget_Object = MibTableColumn
umCfssTarget = _UmCfssTarget_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 10),
    _UmCfssTarget_Type()
)
umCfssTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umCfssTarget.setStatus("current")


class _UmNumberOfUnconfirmedTraps_Type(Integer32):
    """Custom type umNumberOfUnconfirmedTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_UmNumberOfUnconfirmedTraps_Type.__name__ = "Integer32"
_UmNumberOfUnconfirmedTraps_Object = MibScalar
umNumberOfUnconfirmedTraps = _UmNumberOfUnconfirmedTraps_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 6),
    _UmNumberOfUnconfirmedTraps_Type()
)
umNumberOfUnconfirmedTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umNumberOfUnconfirmedTraps.setStatus("current")
_UmUnconfirmedTrapTable_Object = MibTable
umUnconfirmedTrapTable = _UmUnconfirmedTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7)
)
if mibBuilder.loadTexts:
    umUnconfirmedTrapTable.setStatus("current")
_UmUnconfirmedTrapTableEntry_Object = MibTableRow
umUnconfirmedTrapTableEntry = _UmUnconfirmedTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1)
)
umUnconfirmedTrapTableEntry.setIndexNames(
    (0, "H150E-MIB", "umTrapIdentifier"),
)
if mibBuilder.loadTexts:
    umUnconfirmedTrapTableEntry.setStatus("current")


class _UmTrapIdentifier_Type(Integer32):
    """Custom type umTrapIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_UmTrapIdentifier_Type.__name__ = "Integer32"
_UmTrapIdentifier_Object = MibTableColumn
umTrapIdentifier = _UmTrapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 1),
    _UmTrapIdentifier_Type()
)
umTrapIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umTrapIdentifier.setStatus("current")


class _UmTrapType_Type(Integer32):
    """Custom type umTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modifyGeneral", 1),
          ("modifySubscriber", 2),
          ("startup", 0))
    )


_UmTrapType_Type.__name__ = "Integer32"
_UmTrapType_Object = MibTableColumn
umTrapType = _UmTrapType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 2),
    _UmTrapType_Type()
)
umTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umTrapType.setStatus("current")


class _UmTrapLogicalPortNumber_Type(Integer32):
    """Custom type umTrapLogicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483187),
    )


_UmTrapLogicalPortNumber_Type.__name__ = "Integer32"
_UmTrapLogicalPortNumber_Object = MibTableColumn
umTrapLogicalPortNumber = _UmTrapLogicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 3),
    _UmTrapLogicalPortNumber_Type()
)
umTrapLogicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umTrapLogicalPortNumber.setStatus("current")
_UmNetworkElementKey_Type = DisplayString
_UmNetworkElementKey_Object = MibScalar
umNetworkElementKey = _UmNetworkElementKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 8),
    _UmNetworkElementKey_Type()
)
umNetworkElementKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umNetworkElementKey.setStatus("current")

# Managed Objects groups


# Notification objects

sendAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 1)
)
sendAlarm.setObjects(
      *(("H150E-MIB", "h150eErrorIndex"),
        ("H150E-MIB", "h150eErrorDateTime"),
        ("H150E-MIB", "h150eErrorClass"),
        ("H150E-MIB", "h150eErrorCode"),
        ("H150E-MIB", "h150eAccessSlot"),
        ("H150E-MIB", "h150eAccessPort"),
        ("H150E-MIB", "h150eErrorDescription"),
        ("H150E-MIB", "h150eSysState"),
        ("H150E-MIB", "h150eErrorSeverity"))
)
if mibBuilder.loadTexts:
    sendAlarm.setStatus(
        "current"
    )

sendCdrNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 2)
)
sendCdrNotification.setObjects(
      *(("H150E-MIB", "h150eIndexOfLastCdrNotificationTrap"),
        ("H150E-MIB", "h150etypeOfLastCdrNotificationTrap"),
        ("H150E-MIB", "h150eDescriptionOfLastCdrNotificationTrap"))
)
if mibBuilder.loadTexts:
    sendCdrNotification.setStatus(
        "current"
    )

sendPortStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 3)
)
sendPortStatusNotification.setObjects(
    ("H150E-MIB", "indexOfLastPortStatusNotificationTrap")
)
if mibBuilder.loadTexts:
    sendPortStatusNotification.setStatus(
        "current"
    )

sendUmRelatedChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 4)
)
sendUmRelatedChangeNotification.setObjects(
      *(("H150E-MIB", "umTrapIdentifier"),
        ("H150E-MIB", "umTrapType"),
        ("H150E-MIB", "umTrapLogicalPortNumber"),
        ("H150E-MIB", "umNetworkElementKey"))
)
if mibBuilder.loadTexts:
    sendUmRelatedChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H150E-MIB",
    **{"DisplayString": DisplayString,
       "DateAndTime": DateAndTime,
       "ReadWrite": ReadWrite,
       "sni": sni,
       "siemensUnits": siemensUnits,
       "pn": pn,
       "h150eOffice": h150eOffice,
       "h150eControlGroup": h150eControlGroup,
       "h150eSysState": h150eSysState,
       "tftpSwitchoverDateTime": tftpSwitchoverDateTime,
       "tftpDownloadAction": tftpDownloadAction,
       "h150eResetControl": h150eResetControl,
       "h150eSwitchoverState": h150eSwitchoverState,
       "h150eShadowFlashState": h150eShadowFlashState,
       "h150eLoadLevel": h150eLoadLevel,
       "h150eTrapRepetitions": h150eTrapRepetitions,
       "h150eCdrBufferState": h150eCdrBufferState,
       "h150eLogBufferState": h150eLogBufferState,
       "h150eErrorHistoryGroup": h150eErrorHistoryGroup,
       "numberOfErrorHistoryEntries": numberOfErrorHistoryEntries,
       "h150eErrorHistoryTable": h150eErrorHistoryTable,
       "h150eErrorHistoryEntry": h150eErrorHistoryEntry,
       "h150eErrorIndex": h150eErrorIndex,
       "h150eErrorDateTime": h150eErrorDateTime,
       "h150eErrorClass": h150eErrorClass,
       "h150eErrorCode": h150eErrorCode,
       "h150eAccessSlot": h150eAccessSlot,
       "h150eAccessPort": h150eAccessPort,
       "h150eErrorDescription": h150eErrorDescription,
       "h150eErrorSeverity": h150eErrorSeverity,
       "h150eSystemInfoGroup": h150eSystemInfoGroup,
       "sysHardwareVersion": sysHardwareVersion,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysCodeNumber": sysCodeNumber,
       "sysSoftwareLocation": sysSoftwareLocation,
       "numberOfSlotTableEntries": numberOfSlotTableEntries,
       "h150eSlotTable": h150eSlotTable,
       "h150eSlotTableEntry": h150eSlotTableEntry,
       "cardIndex": cardIndex,
       "cardBoxNum": cardBoxNum,
       "cardSlotNum": cardSlotNum,
       "cardType": cardType,
       "cardDescription": cardDescription,
       "cardCodeNumber": cardCodeNumber,
       "cardState": cardState,
       "numberOfPortTableEntries": numberOfPortTableEntries,
       "h150ePortTable": h150ePortTable,
       "h150ePortTableEntry": h150ePortTableEntry,
       "portIndex": portIndex,
       "portCardIndex": portCardIndex,
       "portType": portType,
       "portState": portState,
       "portLock": portLock,
       "portLogicalPortNumber": portLogicalPortNumber,
       "numberOfExtensionTableEntries": numberOfExtensionTableEntries,
       "h150eExtensionTable": h150eExtensionTable,
       "h150eExtensionTableEntry": h150eExtensionTableEntry,
       "extensionIndex": extensionIndex,
       "extensionDescription": extensionDescription,
       "extensionCodeNumber": extensionCodeNumber,
       "numberOfLanConnTableEntries": numberOfLanConnTableEntries,
       "h150eLanConnTable": h150eLanConnTable,
       "h150eLanConnTableEntry": h150eLanConnTableEntry,
       "lanConnIndex": lanConnIndex,
       "lanConnDescription": lanConnDescription,
       "lanConnIpAddress": lanConnIpAddress,
       "lanConnSubnetMask": lanConnSubnetMask,
       "lanConnStatus": lanConnStatus,
       "hiPathAllServeServerIpAddress": hiPathAllServeServerIpAddress,
       "indexOfLastPortStatusNotificationTrap": indexOfLastPortStatusNotificationTrap,
       "sysSnmpAgentVersion": sysSnmpAgentVersion,
       "sysShadowSoftwareVersion": sysShadowSoftwareVersion,
       "sysHiPathSymbolSubInfo": sysHiPathSymbolSubInfo,
       "sysHiPathBranding": sysHiPathBranding,
       "sysTimezoneOffset": sysTimezoneOffset,
       "h150eStatisticsGroup": h150eStatisticsGroup,
       "numberOfFeatureStatTableEntries": numberOfFeatureStatTableEntries,
       "h150eFeatureStatTable": h150eFeatureStatTable,
       "h150eFeatureStatEntry": h150eFeatureStatEntry,
       "featureIndex": featureIndex,
       "featureDescription": featureDescription,
       "featureCounter": featureCounter,
       "featureStatTableReset": featureStatTableReset,
       "h150eCdrConfigGroup": h150eCdrConfigGroup,
       "h150eCdrSeparator": h150eCdrSeparator,
       "h150eCdrElementSeparator": h150eCdrElementSeparator,
       "h150eCdrThresholdValue": h150eCdrThresholdValue,
       "h150eCdrTftpFileCounter": h150eCdrTftpFileCounter,
       "h150eCdrTftpServerDestAddress": h150eCdrTftpServerDestAddress,
       "h150eCdrTftpServerAlternateDestAddress": h150eCdrTftpServerAlternateDestAddress,
       "h150eCdrTftpClientTimer": h150eCdrTftpClientTimer,
       "h150eCdrTcpServerDestAddress": h150eCdrTcpServerDestAddress,
       "h150eCdrTcpServerDestPort": h150eCdrTcpServerDestPort,
       "h150eCdrOutputMode": h150eCdrOutputMode,
       "h150eIndexOfLastCdrNotificationTrap": h150eIndexOfLastCdrNotificationTrap,
       "h150etypeOfLastCdrNotificationTrap": h150etypeOfLastCdrNotificationTrap,
       "h150eDescriptionOfLastCdrNotificationTrap": h150eDescriptionOfLastCdrNotificationTrap,
       "h150eTrapSpecifications": h150eTrapSpecifications,
       "sendAlarm": sendAlarm,
       "sendCdrNotification": sendCdrNotification,
       "sendPortStatusNotification": sendPortStatusNotification,
       "sendUmRelatedChangeNotification": sendUmRelatedChangeNotification,
       "umProxyGroup": umProxyGroup,
       "umNodeNumber": umNodeNumber,
       "umSrsEnabled": umSrsEnabled,
       "umDefaultLanguage": umDefaultLanguage,
       "umNumberOfSubscriberEntries": umNumberOfSubscriberEntries,
       "umSubscriberTable": umSubscriberTable,
       "umSubscriberTableEntry": umSubscriberTableEntry,
       "umLogicalPortNumber": umLogicalPortNumber,
       "umInternalCallNumber": umInternalCallNumber,
       "umDIDNumber": umDIDNumber,
       "umE164Number": umE164Number,
       "umDisplayName": umDisplayName,
       "umStationType": umStationType,
       "umPortStatus": umPortStatus,
       "umClassOfService": umClassOfService,
       "umDisplayLanguage": umDisplayLanguage,
       "umCfssTarget": umCfssTarget,
       "umNumberOfUnconfirmedTraps": umNumberOfUnconfirmedTraps,
       "umUnconfirmedTrapTable": umUnconfirmedTrapTable,
       "umUnconfirmedTrapTableEntry": umUnconfirmedTrapTableEntry,
       "umTrapIdentifier": umTrapIdentifier,
       "umTrapType": umTrapType,
       "umTrapLogicalPortNumber": umTrapLogicalPortNumber,
       "umNetworkElementKey": umNetworkElementKey}
)
