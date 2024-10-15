# SNMP MIB module (OCTOPUSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OCTOPUSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:39 2024
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

octopusE = ModuleIdentity(
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
_OctoControlGroup_ObjectIdentity = ObjectIdentity
octoControlGroup = _OctoControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1)
)


class _OctoSysState_Type(Integer32):
    """Custom type octoSysState based on Integer32"""
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


_OctoSysState_Type.__name__ = "Integer32"
_OctoSysState_Object = MibScalar
octoSysState = _OctoSysState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 1),
    _OctoSysState_Type()
)
octoSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoSysState.setStatus("current")
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


class _OctoResetControl_Type(Integer32):
    """Custom type octoResetControl based on Integer32"""
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


_OctoResetControl_Type.__name__ = "Integer32"
_OctoResetControl_Object = MibScalar
octoResetControl = _OctoResetControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 4),
    _OctoResetControl_Type()
)
octoResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoResetControl.setStatus("current")


class _OctoSwitchoverState_Type(Integer32):
    """Custom type octoSwitchoverState based on Integer32"""
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


_OctoSwitchoverState_Type.__name__ = "Integer32"
_OctoSwitchoverState_Object = MibScalar
octoSwitchoverState = _OctoSwitchoverState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 5),
    _OctoSwitchoverState_Type()
)
octoSwitchoverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoSwitchoverState.setStatus("current")


class _OctoShadowFlashState_Type(Integer32):
    """Custom type octoShadowFlashState based on Integer32"""
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


_OctoShadowFlashState_Type.__name__ = "Integer32"
_OctoShadowFlashState_Object = MibScalar
octoShadowFlashState = _OctoShadowFlashState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 6),
    _OctoShadowFlashState_Type()
)
octoShadowFlashState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoShadowFlashState.setStatus("current")


class _OctoLoadLevel_Type(Integer32):
    """Custom type octoLoadLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OctoLoadLevel_Type.__name__ = "Integer32"
_OctoLoadLevel_Object = MibScalar
octoLoadLevel = _OctoLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 7),
    _OctoLoadLevel_Type()
)
octoLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoLoadLevel.setStatus("current")


class _OctoTrapRepetitions_Type(Integer32):
    """Custom type octoTrapRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_OctoTrapRepetitions_Type.__name__ = "Integer32"
_OctoTrapRepetitions_Object = MibScalar
octoTrapRepetitions = _OctoTrapRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 8),
    _OctoTrapRepetitions_Type()
)
octoTrapRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoTrapRepetitions.setStatus("current")


class _OctoCdrBufferState_Type(Integer32):
    """Custom type octoCdrBufferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("deleteBufferNow", 2))
    )


_OctoCdrBufferState_Type.__name__ = "Integer32"
_OctoCdrBufferState_Object = MibScalar
octoCdrBufferState = _OctoCdrBufferState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 9),
    _OctoCdrBufferState_Type()
)
octoCdrBufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrBufferState.setStatus("current")


class _OctoLogBufferState_Type(Integer32):
    """Custom type octoLogBufferState based on Integer32"""
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


_OctoLogBufferState_Type.__name__ = "Integer32"
_OctoLogBufferState_Object = MibScalar
octoLogBufferState = _OctoLogBufferState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 10),
    _OctoLogBufferState_Type()
)
octoLogBufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoLogBufferState.setStatus("current")
_OctoErrorHistoryGroup_ObjectIdentity = ObjectIdentity
octoErrorHistoryGroup = _OctoErrorHistoryGroup_ObjectIdentity(
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
_OctoErrorHistoryTable_Object = MibTable
octoErrorHistoryTable = _OctoErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    octoErrorHistoryTable.setStatus("current")
_OctoErrorHistoryEntry_Object = MibTableRow
octoErrorHistoryEntry = _OctoErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1)
)
octoErrorHistoryEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "octoErrorIndex"),
)
if mibBuilder.loadTexts:
    octoErrorHistoryEntry.setStatus("current")


class _OctoErrorIndex_Type(Integer32):
    """Custom type octoErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoErrorIndex_Type.__name__ = "Integer32"
_OctoErrorIndex_Object = MibTableColumn
octoErrorIndex = _OctoErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 1),
    _OctoErrorIndex_Type()
)
octoErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorIndex.setStatus("current")
_OctoErrorDateTime_Type = DateAndTime
_OctoErrorDateTime_Object = MibTableColumn
octoErrorDateTime = _OctoErrorDateTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 2),
    _OctoErrorDateTime_Type()
)
octoErrorDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorDateTime.setStatus("current")


class _OctoErrorClass_Type(Integer32):
    """Custom type octoErrorClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoErrorClass_Type.__name__ = "Integer32"
_OctoErrorClass_Object = MibTableColumn
octoErrorClass = _OctoErrorClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 3),
    _OctoErrorClass_Type()
)
octoErrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorClass.setStatus("current")


class _OctoErrorCode_Type(Integer32):
    """Custom type octoErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoErrorCode_Type.__name__ = "Integer32"
_OctoErrorCode_Object = MibTableColumn
octoErrorCode = _OctoErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 4),
    _OctoErrorCode_Type()
)
octoErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorCode.setStatus("current")


class _OctoAccessSlot_Type(Integer32):
    """Custom type octoAccessSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoAccessSlot_Type.__name__ = "Integer32"
_OctoAccessSlot_Object = MibTableColumn
octoAccessSlot = _OctoAccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 5),
    _OctoAccessSlot_Type()
)
octoAccessSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoAccessSlot.setStatus("current")


class _OctoAccessPort_Type(Integer32):
    """Custom type octoAccessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoAccessPort_Type.__name__ = "Integer32"
_OctoAccessPort_Object = MibTableColumn
octoAccessPort = _OctoAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 6),
    _OctoAccessPort_Type()
)
octoAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoAccessPort.setStatus("current")


class _OctoErrorDescription_Type(DisplayString):
    """Custom type octoErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OctoErrorDescription_Type.__name__ = "DisplayString"
_OctoErrorDescription_Object = MibTableColumn
octoErrorDescription = _OctoErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 7),
    _OctoErrorDescription_Type()
)
octoErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorDescription.setStatus("current")


class _OctoErrorSeverity_Type(Integer32):
    """Custom type octoErrorSeverity based on Integer32"""
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


_OctoErrorSeverity_Type.__name__ = "Integer32"
_OctoErrorSeverity_Object = MibTableColumn
octoErrorSeverity = _OctoErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 8),
    _OctoErrorSeverity_Type()
)
octoErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoErrorSeverity.setStatus("current")
_OctoSystemInfoGroup_ObjectIdentity = ObjectIdentity
octoSystemInfoGroup = _OctoSystemInfoGroup_ObjectIdentity(
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
_OctoSlotTable_Object = MibTable
octoSlotTable = _OctoSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    octoSlotTable.setStatus("current")
_OctoSlotTableEntry_Object = MibTableRow
octoSlotTableEntry = _OctoSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1)
)
octoSlotTableEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "cardIndex"),
)
if mibBuilder.loadTexts:
    octoSlotTableEntry.setStatus("current")


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
_OctoPortTable_Object = MibTable
octoPortTable = _OctoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8)
)
if mibBuilder.loadTexts:
    octoPortTable.setStatus("current")
_OctoPortTableEntry_Object = MibTableRow
octoPortTableEntry = _OctoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1)
)
octoPortTableEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    octoPortTableEntry.setStatus("current")


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
_OctoExtensionTable_Object = MibTable
octoExtensionTable = _OctoExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10)
)
if mibBuilder.loadTexts:
    octoExtensionTable.setStatus("current")
_OctoExtensionTableEntry_Object = MibTableRow
octoExtensionTableEntry = _OctoExtensionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1)
)
octoExtensionTableEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "extensionIndex"),
)
if mibBuilder.loadTexts:
    octoExtensionTableEntry.setStatus("current")


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
_OctoLanConnTable_Object = MibTable
octoLanConnTable = _OctoLanConnTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12)
)
if mibBuilder.loadTexts:
    octoLanConnTable.setStatus("current")
_OctoLanConnTableEntry_Object = MibTableRow
octoLanConnTableEntry = _OctoLanConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1)
)
octoLanConnTableEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "lanConnIndex"),
)
if mibBuilder.loadTexts:
    octoLanConnTableEntry.setStatus("current")


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
_OctoStatisticsGroup_ObjectIdentity = ObjectIdentity
octoStatisticsGroup = _OctoStatisticsGroup_ObjectIdentity(
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
_OctoFeatureStatTable_Object = MibTable
octoFeatureStatTable = _OctoFeatureStatTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    octoFeatureStatTable.setStatus("current")
_OctoFeatureStatEntry_Object = MibTableRow
octoFeatureStatEntry = _OctoFeatureStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1)
)
octoFeatureStatEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "featureIndex"),
)
if mibBuilder.loadTexts:
    octoFeatureStatEntry.setStatus("current")


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
_OctoCdrConfigGroup_ObjectIdentity = ObjectIdentity
octoCdrConfigGroup = _OctoCdrConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5)
)


class _OctoCdrSeparator_Type(Integer32):
    """Custom type octoCdrSeparator based on Integer32"""
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


_OctoCdrSeparator_Type.__name__ = "Integer32"
_OctoCdrSeparator_Object = MibScalar
octoCdrSeparator = _OctoCdrSeparator_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 1),
    _OctoCdrSeparator_Type()
)
octoCdrSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrSeparator.setStatus("current")


class _OctoCdrElementSeparator_Type(Integer32):
    """Custom type octoCdrElementSeparator based on Integer32"""
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


_OctoCdrElementSeparator_Type.__name__ = "Integer32"
_OctoCdrElementSeparator_Object = MibScalar
octoCdrElementSeparator = _OctoCdrElementSeparator_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 2),
    _OctoCdrElementSeparator_Type()
)
octoCdrElementSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrElementSeparator.setStatus("current")


class _OctoCdrThresholdValue_Type(Integer32):
    """Custom type octoCdrThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoCdrThresholdValue_Type.__name__ = "Integer32"
_OctoCdrThresholdValue_Object = MibScalar
octoCdrThresholdValue = _OctoCdrThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 3),
    _OctoCdrThresholdValue_Type()
)
octoCdrThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrThresholdValue.setStatus("current")


class _OctoCdrTftpFileCounter_Type(Integer32):
    """Custom type octoCdrTftpFileCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoCdrTftpFileCounter_Type.__name__ = "Integer32"
_OctoCdrTftpFileCounter_Object = MibScalar
octoCdrTftpFileCounter = _OctoCdrTftpFileCounter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 4),
    _OctoCdrTftpFileCounter_Type()
)
octoCdrTftpFileCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTftpFileCounter.setStatus("current")
_OctoCdrTftpServerDestAddress_Type = IpAddress
_OctoCdrTftpServerDestAddress_Object = MibScalar
octoCdrTftpServerDestAddress = _OctoCdrTftpServerDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 5),
    _OctoCdrTftpServerDestAddress_Type()
)
octoCdrTftpServerDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTftpServerDestAddress.setStatus("current")
_OctoCdrTftpServerAlternateDestAddress_Type = IpAddress
_OctoCdrTftpServerAlternateDestAddress_Object = MibScalar
octoCdrTftpServerAlternateDestAddress = _OctoCdrTftpServerAlternateDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 6),
    _OctoCdrTftpServerAlternateDestAddress_Type()
)
octoCdrTftpServerAlternateDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTftpServerAlternateDestAddress.setStatus("current")


class _OctoCdrTftpClientTimer_Type(Integer32):
    """Custom type octoCdrTftpClientTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoCdrTftpClientTimer_Type.__name__ = "Integer32"
_OctoCdrTftpClientTimer_Object = MibScalar
octoCdrTftpClientTimer = _OctoCdrTftpClientTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 7),
    _OctoCdrTftpClientTimer_Type()
)
octoCdrTftpClientTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTftpClientTimer.setStatus("current")
_OctoCdrTcpServerDestAddress_Type = IpAddress
_OctoCdrTcpServerDestAddress_Object = MibScalar
octoCdrTcpServerDestAddress = _OctoCdrTcpServerDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 8),
    _OctoCdrTcpServerDestAddress_Type()
)
octoCdrTcpServerDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTcpServerDestAddress.setStatus("current")


class _OctoCdrTcpServerDestPort_Type(Integer32):
    """Custom type octoCdrTcpServerDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoCdrTcpServerDestPort_Type.__name__ = "Integer32"
_OctoCdrTcpServerDestPort_Object = MibScalar
octoCdrTcpServerDestPort = _OctoCdrTcpServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 9),
    _OctoCdrTcpServerDestPort_Type()
)
octoCdrTcpServerDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrTcpServerDestPort.setStatus("current")


class _OctoCdrOutputMode_Type(Integer32):
    """Custom type octoCdrOutputMode based on Integer32"""
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


_OctoCdrOutputMode_Type.__name__ = "Integer32"
_OctoCdrOutputMode_Object = MibScalar
octoCdrOutputMode = _OctoCdrOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 10),
    _OctoCdrOutputMode_Type()
)
octoCdrOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoCdrOutputMode.setStatus("current")


class _OctoIndexOfLastCdrNotificationTrap_Type(Integer32):
    """Custom type octoIndexOfLastCdrNotificationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoIndexOfLastCdrNotificationTrap_Type.__name__ = "Integer32"
_OctoIndexOfLastCdrNotificationTrap_Object = MibScalar
octoIndexOfLastCdrNotificationTrap = _OctoIndexOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 11),
    _OctoIndexOfLastCdrNotificationTrap_Type()
)
octoIndexOfLastCdrNotificationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    octoIndexOfLastCdrNotificationTrap.setStatus("current")


class _OctoTypeOfLastCdrNotificationTrap_Type(Integer32):
    """Custom type octoTypeOfLastCdrNotificationTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_OctoTypeOfLastCdrNotificationTrap_Type.__name__ = "Integer32"
_OctoTypeOfLastCdrNotificationTrap_Object = MibScalar
octoTypeOfLastCdrNotificationTrap = _OctoTypeOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 12),
    _OctoTypeOfLastCdrNotificationTrap_Type()
)
octoTypeOfLastCdrNotificationTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoTypeOfLastCdrNotificationTrap.setStatus("current")


class _OctoDescriptionOfLastCdrNotificationTrap_Type(DisplayString):
    """Custom type octoDescriptionOfLastCdrNotificationTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OctoDescriptionOfLastCdrNotificationTrap_Type.__name__ = "DisplayString"
_OctoDescriptionOfLastCdrNotificationTrap_Object = MibScalar
octoDescriptionOfLastCdrNotificationTrap = _OctoDescriptionOfLastCdrNotificationTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 13),
    _OctoDescriptionOfLastCdrNotificationTrap_Type()
)
octoDescriptionOfLastCdrNotificationTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octoDescriptionOfLastCdrNotificationTrap.setStatus("current")
_OctoTrapSpecifications_ObjectIdentity = ObjectIdentity
octoTrapSpecifications = _OctoTrapSpecifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6)
)
_OctoNetworkGroup_ObjectIdentity = ObjectIdentity
octoNetworkGroup = _OctoNetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7)
)


class _NumberOfIpConnControlTableEntries_Type(Integer32):
    """Custom type numberOfIpConnControlTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_NumberOfIpConnControlTableEntries_Type.__name__ = "Integer32"
_NumberOfIpConnControlTableEntries_Object = MibScalar
numberOfIpConnControlTableEntries = _NumberOfIpConnControlTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 1),
    _NumberOfIpConnControlTableEntries_Type()
)
numberOfIpConnControlTableEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfIpConnControlTableEntries.setStatus("current")
_IpConnControlTable_Object = MibTable
ipConnControlTable = _IpConnControlTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2)
)
if mibBuilder.loadTexts:
    ipConnControlTable.setStatus("current")
_IpConnControlEntry_Object = MibTableRow
ipConnControlEntry = _IpConnControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1)
)
ipConnControlEntry.setIndexNames(
    (0, "OCTOPUSE-MIB", "connControlIndex"),
)
if mibBuilder.loadTexts:
    ipConnControlEntry.setStatus("current")


class _ConnControlIndex_Type(Integer32):
    """Custom type connControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_ConnControlIndex_Type.__name__ = "Integer32"
_ConnControlIndex_Object = MibTableColumn
connControlIndex = _ConnControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 1),
    _ConnControlIndex_Type()
)
connControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connControlIndex.setStatus("current")
_ConnPartnerIpAddress_Type = IpAddress
_ConnPartnerIpAddress_Object = MibTableColumn
connPartnerIpAddress = _ConnPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 2),
    _ConnPartnerIpAddress_Type()
)
connPartnerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPartnerIpAddress.setStatus("current")


class _ConnTimeout_Type(Integer32):
    """Custom type connTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_ConnTimeout_Type.__name__ = "Integer32"
_ConnTimeout_Object = MibTableColumn
connTimeout = _ConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 3),
    _ConnTimeout_Type()
)
connTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connTimeout.setStatus("current")


class _ConnRetries_Type(Integer32):
    """Custom type connRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_ConnRetries_Type.__name__ = "Integer32"
_ConnRetries_Object = MibTableColumn
connRetries = _ConnRetries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 4),
    _ConnRetries_Type()
)
connRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRetries.setStatus("current")


class _ConnRetryTimer_Type(Integer32):
    """Custom type connRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483187),
    )


_ConnRetryTimer_Type.__name__ = "Integer32"
_ConnRetryTimer_Object = MibTableColumn
connRetryTimer = _ConnRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 5),
    _ConnRetryTimer_Type()
)
connRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRetryTimer.setStatus("current")


class _ConnResult_Type(Integer32):
    """Custom type connResult based on Integer32"""
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
        *(("activated", 4),
          ("connected", 2),
          ("disconnected", 1),
          ("notActivated", 3))
    )


_ConnResult_Type.__name__ = "Integer32"
_ConnResult_Object = MibTableColumn
connResult = _ConnResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 6),
    _ConnResult_Type()
)
connResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connResult.setStatus("current")


class _ConnControlState_Type(Integer32):
    """Custom type connControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 3),
          ("periodicalTest", 2),
          ("singleTest", 1))
    )


_ConnControlState_Type.__name__ = "Integer32"
_ConnControlState_Object = MibTableColumn
connControlState = _ConnControlState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 7),
    _ConnControlState_Type()
)
connControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connControlState.setStatus("current")

# Managed Objects groups


# Notification objects

sendAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 1)
)
sendAlarm.setObjects(
      *(("OCTOPUSE-MIB", "octoErrorIndex"),
        ("OCTOPUSE-MIB", "octoErrorDateTime"),
        ("OCTOPUSE-MIB", "octoErrorClass"),
        ("OCTOPUSE-MIB", "octoErrorCode"),
        ("OCTOPUSE-MIB", "octoAccessSlot"),
        ("OCTOPUSE-MIB", "octoAccessPort"),
        ("OCTOPUSE-MIB", "octoErrorDescription"),
        ("OCTOPUSE-MIB", "octoSysState"),
        ("OCTOPUSE-MIB", "octoErrorSeverity"))
)
if mibBuilder.loadTexts:
    sendAlarm.setStatus(
        "current"
    )

sendCdrNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 2)
)
sendCdrNotification.setObjects(
      *(("OCTOPUSE-MIB", "octoIndexOfLastCdrNotificationTrap"),
        ("OCTOPUSE-MIB", "octoTypeOfLastCdrNotificationTrap"),
        ("OCTOPUSE-MIB", "octoDescriptionOfLastCdrNotificationTrap"))
)
if mibBuilder.loadTexts:
    sendCdrNotification.setStatus(
        "current"
    )

sendPortStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 3)
)
sendPortStatusNotification.setObjects(
    ("OCTOPUSE-MIB", "indexOfLastPortStatusNotificationTrap")
)
if mibBuilder.loadTexts:
    sendPortStatusNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCTOPUSE-MIB",
    **{"DisplayString": DisplayString,
       "DateAndTime": DateAndTime,
       "ReadWrite": ReadWrite,
       "sni": sni,
       "siemensUnits": siemensUnits,
       "pn": pn,
       "octopusE": octopusE,
       "octoControlGroup": octoControlGroup,
       "octoSysState": octoSysState,
       "tftpSwitchoverDateTime": tftpSwitchoverDateTime,
       "tftpDownloadAction": tftpDownloadAction,
       "octoResetControl": octoResetControl,
       "octoSwitchoverState": octoSwitchoverState,
       "octoShadowFlashState": octoShadowFlashState,
       "octoLoadLevel": octoLoadLevel,
       "octoTrapRepetitions": octoTrapRepetitions,
       "octoCdrBufferState": octoCdrBufferState,
       "octoLogBufferState": octoLogBufferState,
       "octoErrorHistoryGroup": octoErrorHistoryGroup,
       "numberOfErrorHistoryEntries": numberOfErrorHistoryEntries,
       "octoErrorHistoryTable": octoErrorHistoryTable,
       "octoErrorHistoryEntry": octoErrorHistoryEntry,
       "octoErrorIndex": octoErrorIndex,
       "octoErrorDateTime": octoErrorDateTime,
       "octoErrorClass": octoErrorClass,
       "octoErrorCode": octoErrorCode,
       "octoAccessSlot": octoAccessSlot,
       "octoAccessPort": octoAccessPort,
       "octoErrorDescription": octoErrorDescription,
       "octoErrorSeverity": octoErrorSeverity,
       "octoSystemInfoGroup": octoSystemInfoGroup,
       "sysHardwareVersion": sysHardwareVersion,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysCodeNumber": sysCodeNumber,
       "sysSoftwareLocation": sysSoftwareLocation,
       "numberOfSlotTableEntries": numberOfSlotTableEntries,
       "octoSlotTable": octoSlotTable,
       "octoSlotTableEntry": octoSlotTableEntry,
       "cardIndex": cardIndex,
       "cardBoxNum": cardBoxNum,
       "cardSlotNum": cardSlotNum,
       "cardType": cardType,
       "cardDescription": cardDescription,
       "cardCodeNumber": cardCodeNumber,
       "cardState": cardState,
       "numberOfPortTableEntries": numberOfPortTableEntries,
       "octoPortTable": octoPortTable,
       "octoPortTableEntry": octoPortTableEntry,
       "portIndex": portIndex,
       "portCardIndex": portCardIndex,
       "portType": portType,
       "portState": portState,
       "portLock": portLock,
       "numberOfExtensionTableEntries": numberOfExtensionTableEntries,
       "octoExtensionTable": octoExtensionTable,
       "octoExtensionTableEntry": octoExtensionTableEntry,
       "extensionIndex": extensionIndex,
       "extensionDescription": extensionDescription,
       "extensionCodeNumber": extensionCodeNumber,
       "numberOfLanConnTableEntries": numberOfLanConnTableEntries,
       "octoLanConnTable": octoLanConnTable,
       "octoLanConnTableEntry": octoLanConnTableEntry,
       "lanConnIndex": lanConnIndex,
       "lanConnDescription": lanConnDescription,
       "lanConnIpAddress": lanConnIpAddress,
       "lanConnSubnetMask": lanConnSubnetMask,
       "lanConnStatus": lanConnStatus,
       "hiPathAllServeServerIpAddress": hiPathAllServeServerIpAddress,
       "indexOfLastPortStatusNotificationTrap": indexOfLastPortStatusNotificationTrap,
       "sysSnmpAgentVersion": sysSnmpAgentVersion,
       "octoStatisticsGroup": octoStatisticsGroup,
       "numberOfFeatureStatTableEntries": numberOfFeatureStatTableEntries,
       "octoFeatureStatTable": octoFeatureStatTable,
       "octoFeatureStatEntry": octoFeatureStatEntry,
       "featureIndex": featureIndex,
       "featureDescription": featureDescription,
       "featureCounter": featureCounter,
       "featureStatTableReset": featureStatTableReset,
       "octoCdrConfigGroup": octoCdrConfigGroup,
       "octoCdrSeparator": octoCdrSeparator,
       "octoCdrElementSeparator": octoCdrElementSeparator,
       "octoCdrThresholdValue": octoCdrThresholdValue,
       "octoCdrTftpFileCounter": octoCdrTftpFileCounter,
       "octoCdrTftpServerDestAddress": octoCdrTftpServerDestAddress,
       "octoCdrTftpServerAlternateDestAddress": octoCdrTftpServerAlternateDestAddress,
       "octoCdrTftpClientTimer": octoCdrTftpClientTimer,
       "octoCdrTcpServerDestAddress": octoCdrTcpServerDestAddress,
       "octoCdrTcpServerDestPort": octoCdrTcpServerDestPort,
       "octoCdrOutputMode": octoCdrOutputMode,
       "octoIndexOfLastCdrNotificationTrap": octoIndexOfLastCdrNotificationTrap,
       "octoTypeOfLastCdrNotificationTrap": octoTypeOfLastCdrNotificationTrap,
       "octoDescriptionOfLastCdrNotificationTrap": octoDescriptionOfLastCdrNotificationTrap,
       "octoTrapSpecifications": octoTrapSpecifications,
       "sendAlarm": sendAlarm,
       "sendCdrNotification": sendCdrNotification,
       "sendPortStatusNotification": sendPortStatusNotification,
       "octoNetworkGroup": octoNetworkGroup,
       "numberOfIpConnControlTableEntries": numberOfIpConnControlTableEntries,
       "ipConnControlTable": ipConnControlTable,
       "ipConnControlEntry": ipConnControlEntry,
       "connControlIndex": connControlIndex,
       "connPartnerIpAddress": connPartnerIpAddress,
       "connTimeout": connTimeout,
       "connRetries": connRetries,
       "connRetryTimer": connRetryTimer,
       "connResult": connResult,
       "connControlState": connControlState}
)
