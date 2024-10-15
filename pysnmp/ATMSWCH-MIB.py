# SNMP MIB module (ATMSWCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATMSWCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:14 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )





class AtmPrefix(OctetString):
    """Custom type AtmPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmSwch_ObjectIdentity = ObjectIdentity
atmSwch = _AtmSwch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33)
)
_AtmSwchBase_ObjectIdentity = ObjectIdentity
atmSwchBase = _AtmSwchBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 1)
)
_AtmSwchBaseCurrentPrefix_Type = AtmPrefix
_AtmSwchBaseCurrentPrefix_Object = MibScalar
atmSwchBaseCurrentPrefix = _AtmSwchBaseCurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 1, 1),
    _AtmSwchBaseCurrentPrefix_Type()
)
atmSwchBaseCurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchBaseCurrentPrefix.setStatus("mandatory")
_AtmSwchBaseConfigPrefix_Type = AtmPrefix
_AtmSwchBaseConfigPrefix_Object = MibScalar
atmSwchBaseConfigPrefix = _AtmSwchBaseConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 1, 2),
    _AtmSwchBaseConfigPrefix_Type()
)
atmSwchBaseConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchBaseConfigPrefix.setStatus("mandatory")


class _AtmSwchBaseEpdThreshold_Type(Integer32):
    """Custom type atmSwchBaseEpdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_AtmSwchBaseEpdThreshold_Type.__name__ = "Integer32"
_AtmSwchBaseEpdThreshold_Object = MibScalar
atmSwchBaseEpdThreshold = _AtmSwchBaseEpdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 1, 3),
    _AtmSwchBaseEpdThreshold_Type()
)
atmSwchBaseEpdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchBaseEpdThreshold.setStatus("mandatory")


class _AtmSwchBaseAmonAdminState_Type(Integer32):
    """Custom type atmSwchBaseAmonAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AtmSwchBaseAmonAdminState_Type.__name__ = "Integer32"
_AtmSwchBaseAmonAdminState_Object = MibScalar
atmSwchBaseAmonAdminState = _AtmSwchBaseAmonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 1, 4),
    _AtmSwchBaseAmonAdminState_Type()
)
atmSwchBaseAmonAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchBaseAmonAdminState.setStatus("mandatory")
_AtmSwchCpu_ObjectIdentity = ObjectIdentity
atmSwchCpu = _AtmSwchCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 2)
)
_AtmSwchCpuTable_Object = MibTable
atmSwchCpuTable = _AtmSwchCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1)
)
if mibBuilder.loadTexts:
    atmSwchCpuTable.setStatus("mandatory")
_AtmSwchCpuEntry_Object = MibTableRow
atmSwchCpuEntry = _AtmSwchCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1)
)
atmSwchCpuEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchCpuIndex"),
)
if mibBuilder.loadTexts:
    atmSwchCpuEntry.setStatus("mandatory")
_AtmSwchCpuIndex_Type = Integer32
_AtmSwchCpuIndex_Object = MibTableColumn
atmSwchCpuIndex = _AtmSwchCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 1),
    _AtmSwchCpuIndex_Type()
)
atmSwchCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuIndex.setStatus("mandatory")


class _AtmSwchCpuHwVersion_Type(OctetString):
    """Custom type atmSwchCpuHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtmSwchCpuHwVersion_Type.__name__ = "OctetString"
_AtmSwchCpuHwVersion_Object = MibTableColumn
atmSwchCpuHwVersion = _AtmSwchCpuHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 2),
    _AtmSwchCpuHwVersion_Type()
)
atmSwchCpuHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuHwVersion.setStatus("mandatory")
_AtmSwchCpuSoftErrCode_Type = Integer32
_AtmSwchCpuSoftErrCode_Object = MibTableColumn
atmSwchCpuSoftErrCode = _AtmSwchCpuSoftErrCode_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 3),
    _AtmSwchCpuSoftErrCode_Type()
)
atmSwchCpuSoftErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSoftErrCode.setStatus("mandatory")


class _AtmSwchCpuSoftErrString_Type(DisplayString):
    """Custom type atmSwchCpuSoftErrString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AtmSwchCpuSoftErrString_Type.__name__ = "DisplayString"
_AtmSwchCpuSoftErrString_Object = MibTableColumn
atmSwchCpuSoftErrString = _AtmSwchCpuSoftErrString_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 4),
    _AtmSwchCpuSoftErrString_Type()
)
atmSwchCpuSoftErrString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSoftErrString.setStatus("mandatory")


class _AtmSwchCpuUtilization_Type(Integer32):
    """Custom type atmSwchCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AtmSwchCpuUtilization_Type.__name__ = "Integer32"
_AtmSwchCpuUtilization_Object = MibTableColumn
atmSwchCpuUtilization = _AtmSwchCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 5),
    _AtmSwchCpuUtilization_Type()
)
atmSwchCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuUtilization.setStatus("mandatory")
_AtmSwchCpuRamSize_Type = Gauge32
_AtmSwchCpuRamSize_Object = MibTableColumn
atmSwchCpuRamSize = _AtmSwchCpuRamSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 6),
    _AtmSwchCpuRamSize_Type()
)
atmSwchCpuRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuRamSize.setStatus("mandatory")
_AtmSwchCpuRamUsed_Type = Gauge32
_AtmSwchCpuRamUsed_Object = MibTableColumn
atmSwchCpuRamUsed = _AtmSwchCpuRamUsed_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 7),
    _AtmSwchCpuRamUsed_Type()
)
atmSwchCpuRamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuRamUsed.setStatus("mandatory")
_AtmSwchCpuFlashSize_Type = Gauge32
_AtmSwchCpuFlashSize_Object = MibTableColumn
atmSwchCpuFlashSize = _AtmSwchCpuFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 8),
    _AtmSwchCpuFlashSize_Type()
)
atmSwchCpuFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuFlashSize.setStatus("mandatory")
_AtmSwchCpuFlashUsed_Type = Gauge32
_AtmSwchCpuFlashUsed_Object = MibTableColumn
atmSwchCpuFlashUsed = _AtmSwchCpuFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 9),
    _AtmSwchCpuFlashUsed_Type()
)
atmSwchCpuFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuFlashUsed.setStatus("mandatory")
_AtmSwchCpuEepromSize_Type = Gauge32
_AtmSwchCpuEepromSize_Object = MibTableColumn
atmSwchCpuEepromSize = _AtmSwchCpuEepromSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 10),
    _AtmSwchCpuEepromSize_Type()
)
atmSwchCpuEepromSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuEepromSize.setStatus("mandatory")
_AtmSwchCpuEepromUsed_Type = Gauge32
_AtmSwchCpuEepromUsed_Object = MibTableColumn
atmSwchCpuEepromUsed = _AtmSwchCpuEepromUsed_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 11),
    _AtmSwchCpuEepromUsed_Type()
)
atmSwchCpuEepromUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuEepromUsed.setStatus("mandatory")
_AtmSwchCpuTime_Type = Integer32
_AtmSwchCpuTime_Object = MibTableColumn
atmSwchCpuTime = _AtmSwchCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 12),
    _AtmSwchCpuTime_Type()
)
atmSwchCpuTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchCpuTime.setStatus("mandatory")
_AtmSwchCpuSysUpTime_Type = TimeTicks
_AtmSwchCpuSysUpTime_Object = MibTableColumn
atmSwchCpuSysUpTime = _AtmSwchCpuSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 13),
    _AtmSwchCpuSysUpTime_Type()
)
atmSwchCpuSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSysUpTime.setStatus("mandatory")


class _AtmSwchCpuSvcPtPtInConns_Type(Integer32):
    """Custom type atmSwchCpuSvcPtPtInConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchCpuSvcPtPtInConns_Type.__name__ = "Integer32"
_AtmSwchCpuSvcPtPtInConns_Object = MibTableColumn
atmSwchCpuSvcPtPtInConns = _AtmSwchCpuSvcPtPtInConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 14),
    _AtmSwchCpuSvcPtPtInConns_Type()
)
atmSwchCpuSvcPtPtInConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSvcPtPtInConns.setStatus("mandatory")


class _AtmSwchCpuSvcPtPtOutConns_Type(Integer32):
    """Custom type atmSwchCpuSvcPtPtOutConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchCpuSvcPtPtOutConns_Type.__name__ = "Integer32"
_AtmSwchCpuSvcPtPtOutConns_Object = MibTableColumn
atmSwchCpuSvcPtPtOutConns = _AtmSwchCpuSvcPtPtOutConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 15),
    _AtmSwchCpuSvcPtPtOutConns_Type()
)
atmSwchCpuSvcPtPtOutConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSvcPtPtOutConns.setStatus("mandatory")


class _AtmSwchCpuSvcPtMptRootConns_Type(Integer32):
    """Custom type atmSwchCpuSvcPtMptRootConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchCpuSvcPtMptRootConns_Type.__name__ = "Integer32"
_AtmSwchCpuSvcPtMptRootConns_Object = MibTableColumn
atmSwchCpuSvcPtMptRootConns = _AtmSwchCpuSvcPtMptRootConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 16),
    _AtmSwchCpuSvcPtMptRootConns_Type()
)
atmSwchCpuSvcPtMptRootConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSvcPtMptRootConns.setStatus("mandatory")


class _AtmSwchCpuSvcPtMptLeafConns_Type(Integer32):
    """Custom type atmSwchCpuSvcPtMptLeafConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchCpuSvcPtMptLeafConns_Type.__name__ = "Integer32"
_AtmSwchCpuSvcPtMptLeafConns_Object = MibTableColumn
atmSwchCpuSvcPtMptLeafConns = _AtmSwchCpuSvcPtMptLeafConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 17),
    _AtmSwchCpuSvcPtMptLeafConns_Type()
)
atmSwchCpuSvcPtMptLeafConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuSvcPtMptLeafConns.setStatus("mandatory")


class _AtmSwchCpuPvcPtPtConns_Type(Integer32):
    """Custom type atmSwchCpuPvcPtPtConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchCpuPvcPtPtConns_Type.__name__ = "Integer32"
_AtmSwchCpuPvcPtPtConns_Object = MibTableColumn
atmSwchCpuPvcPtPtConns = _AtmSwchCpuPvcPtPtConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 18),
    _AtmSwchCpuPvcPtPtConns_Type()
)
atmSwchCpuPvcPtPtConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchCpuPvcPtPtConns.setStatus("mandatory")
_AtmSwchSlot_ObjectIdentity = ObjectIdentity
atmSwchSlot = _AtmSwchSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 5)
)
_AtmSwchSlotTable_Object = MibTable
atmSwchSlotTable = _AtmSwchSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1)
)
if mibBuilder.loadTexts:
    atmSwchSlotTable.setStatus("mandatory")
_AtmSwchSlotEntry_Object = MibTableRow
atmSwchSlotEntry = _AtmSwchSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1)
)
atmSwchSlotEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchSlotIndex"),
)
if mibBuilder.loadTexts:
    atmSwchSlotEntry.setStatus("mandatory")
_AtmSwchSlotIndex_Type = Integer32
_AtmSwchSlotIndex_Object = MibTableColumn
atmSwchSlotIndex = _AtmSwchSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 1),
    _AtmSwchSlotIndex_Type()
)
atmSwchSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotIndex.setStatus("mandatory")
_AtmSwchSlotRxCellDiscards_Type = Integer32
_AtmSwchSlotRxCellDiscards_Object = MibTableColumn
atmSwchSlotRxCellDiscards = _AtmSwchSlotRxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 2),
    _AtmSwchSlotRxCellDiscards_Type()
)
atmSwchSlotRxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotRxCellDiscards.setStatus("mandatory")
_AtmSwchSlotRouteNextId_Type = Integer32
_AtmSwchSlotRouteNextId_Object = MibTableColumn
atmSwchSlotRouteNextId = _AtmSwchSlotRouteNextId_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 3),
    _AtmSwchSlotRouteNextId_Type()
)
atmSwchSlotRouteNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotRouteNextId.setStatus("mandatory")


class _AtmSwchSlotAPSMode_Type(Integer32):
    """Custom type atmSwchSlotAPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("uniDirectionalNonRevertive", 1)
    )


_AtmSwchSlotAPSMode_Type.__name__ = "Integer32"
_AtmSwchSlotAPSMode_Object = MibTableColumn
atmSwchSlotAPSMode = _AtmSwchSlotAPSMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 4),
    _AtmSwchSlotAPSMode_Type()
)
atmSwchSlotAPSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAPSMode.setStatus("mandatory")


class _AtmSwchSlotAPSCurrentState_Type(Integer32):
    """Custom type atmSwchSlotAPSCurrentState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 6),
          ("forcedSwitch", 4),
          ("manualSwitch", 5),
          ("noAPS", 7),
          ("noRequest", 1),
          ("notActive", 8),
          ("sd", 3),
          ("sf", 2))
    )


_AtmSwchSlotAPSCurrentState_Type.__name__ = "Integer32"
_AtmSwchSlotAPSCurrentState_Object = MibTableColumn
atmSwchSlotAPSCurrentState = _AtmSwchSlotAPSCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 5),
    _AtmSwchSlotAPSCurrentState_Type()
)
atmSwchSlotAPSCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAPSCurrentState.setStatus("mandatory")


class _AtmSwchSlotAPSSwitchCommand_Type(Integer32):
    """Custom type atmSwchSlotAPSSwitchCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("forcedSwitchProtectToWork", 4),
          ("forcedSwitchWorkToProtect", 3),
          ("manualSwitchProtectToWork", 6),
          ("manualSwitchWorkToProtect", 5),
          ("noCmd", 1))
    )


_AtmSwchSlotAPSSwitchCommand_Type.__name__ = "Integer32"
_AtmSwchSlotAPSSwitchCommand_Object = MibTableColumn
atmSwchSlotAPSSwitchCommand = _AtmSwchSlotAPSSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 6),
    _AtmSwchSlotAPSSwitchCommand_Type()
)
atmSwchSlotAPSSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotAPSSwitchCommand.setStatus("mandatory")


class _AtmSwchSlotAPSSFBerThreshold_Type(Integer32):
    """Custom type atmSwchSlotAPSSFBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_AtmSwchSlotAPSSFBerThreshold_Type.__name__ = "Integer32"
_AtmSwchSlotAPSSFBerThreshold_Object = MibTableColumn
atmSwchSlotAPSSFBerThreshold = _AtmSwchSlotAPSSFBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 7),
    _AtmSwchSlotAPSSFBerThreshold_Type()
)
atmSwchSlotAPSSFBerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAPSSFBerThreshold.setStatus("mandatory")


class _AtmSwchSlotAPSSDBerThreshold_Type(Integer32):
    """Custom type atmSwchSlotAPSSDBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_AtmSwchSlotAPSSDBerThreshold_Type.__name__ = "Integer32"
_AtmSwchSlotAPSSDBerThreshold_Object = MibTableColumn
atmSwchSlotAPSSDBerThreshold = _AtmSwchSlotAPSSDBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 8),
    _AtmSwchSlotAPSSDBerThreshold_Type()
)
atmSwchSlotAPSSDBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotAPSSDBerThreshold.setStatus("mandatory")


class _AtmSwchSlotAPSDecision_Type(Integer32):
    """Custom type atmSwchSlotAPSDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-Active", 3),
          ("protection", 2),
          ("working", 1))
    )


_AtmSwchSlotAPSDecision_Type.__name__ = "Integer32"
_AtmSwchSlotAPSDecision_Object = MibTableColumn
atmSwchSlotAPSDecision = _AtmSwchSlotAPSDecision_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 9),
    _AtmSwchSlotAPSDecision_Type()
)
atmSwchSlotAPSDecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAPSDecision.setStatus("mandatory")
_AtmSwchPort_ObjectIdentity = ObjectIdentity
atmSwchPort = _AtmSwchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 6)
)
_AtmSwchPortTable_Object = MibTable
atmSwchPortTable = _AtmSwchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1)
)
if mibBuilder.loadTexts:
    atmSwchPortTable.setStatus("mandatory")
_AtmSwchPortEntry_Object = MibTableRow
atmSwchPortEntry = _AtmSwchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1)
)
atmSwchPortEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchSlotIndex"),
    (0, "ATMSWCH-MIB", "atmSwchPortIndex"),
)
if mibBuilder.loadTexts:
    atmSwchPortEntry.setStatus("mandatory")
_AtmSwchPortIndex_Type = Integer32
_AtmSwchPortIndex_Object = MibTableColumn
atmSwchPortIndex = _AtmSwchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 1),
    _AtmSwchPortIndex_Type()
)
atmSwchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortIndex.setStatus("mandatory")
_AtmSwchPortRootVportIndex_Type = Integer32
_AtmSwchPortRootVportIndex_Object = MibTableColumn
atmSwchPortRootVportIndex = _AtmSwchPortRootVportIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 2),
    _AtmSwchPortRootVportIndex_Type()
)
atmSwchPortRootVportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortRootVportIndex.setStatus("mandatory")
_AtmSwchPortNumVPorts_Type = Integer32
_AtmSwchPortNumVPorts_Object = MibTableColumn
atmSwchPortNumVPorts = _AtmSwchPortNumVPorts_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 3),
    _AtmSwchPortNumVPorts_Type()
)
atmSwchPortNumVPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortNumVPorts.setStatus("mandatory")


class _AtmSwchPortPayloadScramble_Type(Integer32):
    """Custom type atmSwchPortPayloadScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AtmSwchPortPayloadScramble_Type.__name__ = "Integer32"
_AtmSwchPortPayloadScramble_Object = MibTableColumn
atmSwchPortPayloadScramble = _AtmSwchPortPayloadScramble_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 4),
    _AtmSwchPortPayloadScramble_Type()
)
atmSwchPortPayloadScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchPortPayloadScramble.setStatus("mandatory")


class _AtmSwchPortPhysicalType_Type(Integer32):
    """Custom type atmSwchPortPhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_AtmSwchPortPhysicalType_Type.__name__ = "Integer32"
_AtmSwchPortPhysicalType_Object = MibTableColumn
atmSwchPortPhysicalType = _AtmSwchPortPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 5),
    _AtmSwchPortPhysicalType_Type()
)
atmSwchPortPhysicalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchPortPhysicalType.setStatus("mandatory")
_AtmSwchPortMaxTxRate_Type = Integer32
_AtmSwchPortMaxTxRate_Object = MibTableColumn
atmSwchPortMaxTxRate = _AtmSwchPortMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 6),
    _AtmSwchPortMaxTxRate_Type()
)
atmSwchPortMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchPortMaxTxRate.setStatus("mandatory")


class _AtmSwchPortSvcPtPtInConns_Type(Integer32):
    """Custom type atmSwchPortSvcPtPtInConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortSvcPtPtInConns_Type.__name__ = "Integer32"
_AtmSwchPortSvcPtPtInConns_Object = MibTableColumn
atmSwchPortSvcPtPtInConns = _AtmSwchPortSvcPtPtInConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 7),
    _AtmSwchPortSvcPtPtInConns_Type()
)
atmSwchPortSvcPtPtInConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortSvcPtPtInConns.setStatus("mandatory")


class _AtmSwchPortSvcPtPtOutConns_Type(Integer32):
    """Custom type atmSwchPortSvcPtPtOutConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortSvcPtPtOutConns_Type.__name__ = "Integer32"
_AtmSwchPortSvcPtPtOutConns_Object = MibTableColumn
atmSwchPortSvcPtPtOutConns = _AtmSwchPortSvcPtPtOutConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 8),
    _AtmSwchPortSvcPtPtOutConns_Type()
)
atmSwchPortSvcPtPtOutConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortSvcPtPtOutConns.setStatus("mandatory")


class _AtmSwchPortSvcPtMptRootConns_Type(Integer32):
    """Custom type atmSwchPortSvcPtMptRootConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortSvcPtMptRootConns_Type.__name__ = "Integer32"
_AtmSwchPortSvcPtMptRootConns_Object = MibTableColumn
atmSwchPortSvcPtMptRootConns = _AtmSwchPortSvcPtMptRootConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 9),
    _AtmSwchPortSvcPtMptRootConns_Type()
)
atmSwchPortSvcPtMptRootConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortSvcPtMptRootConns.setStatus("mandatory")


class _AtmSwchPortSvcPtMptLeafConns_Type(Integer32):
    """Custom type atmSwchPortSvcPtMptLeafConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortSvcPtMptLeafConns_Type.__name__ = "Integer32"
_AtmSwchPortSvcPtMptLeafConns_Object = MibTableColumn
atmSwchPortSvcPtMptLeafConns = _AtmSwchPortSvcPtMptLeafConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 10),
    _AtmSwchPortSvcPtMptLeafConns_Type()
)
atmSwchPortSvcPtMptLeafConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortSvcPtMptLeafConns.setStatus("mandatory")


class _AtmSwchPortPvcPtPtConns_Type(Integer32):
    """Custom type atmSwchPortPvcPtPtConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvcPtPtConns_Type.__name__ = "Integer32"
_AtmSwchPortPvcPtPtConns_Object = MibTableColumn
atmSwchPortPvcPtPtConns = _AtmSwchPortPvcPtPtConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 11),
    _AtmSwchPortPvcPtPtConns_Type()
)
atmSwchPortPvcPtPtConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvcPtPtConns.setStatus("mandatory")


class _AtmSwchPortPvcPtMptRootConns_Type(Integer32):
    """Custom type atmSwchPortPvcPtMptRootConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvcPtMptRootConns_Type.__name__ = "Integer32"
_AtmSwchPortPvcPtMptRootConns_Object = MibTableColumn
atmSwchPortPvcPtMptRootConns = _AtmSwchPortPvcPtMptRootConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 12),
    _AtmSwchPortPvcPtMptRootConns_Type()
)
atmSwchPortPvcPtMptRootConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvcPtMptRootConns.setStatus("mandatory")


class _AtmSwchPortPvcPtMptLeafConns_Type(Integer32):
    """Custom type atmSwchPortPvcPtMptLeafConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvcPtMptLeafConns_Type.__name__ = "Integer32"
_AtmSwchPortPvcPtMptLeafConns_Object = MibTableColumn
atmSwchPortPvcPtMptLeafConns = _AtmSwchPortPvcPtMptLeafConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 13),
    _AtmSwchPortPvcPtMptLeafConns_Type()
)
atmSwchPortPvcPtMptLeafConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvcPtMptLeafConns.setStatus("mandatory")


class _AtmSwchPortPvpPtPtConns_Type(Integer32):
    """Custom type atmSwchPortPvpPtPtConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvpPtPtConns_Type.__name__ = "Integer32"
_AtmSwchPortPvpPtPtConns_Object = MibTableColumn
atmSwchPortPvpPtPtConns = _AtmSwchPortPvpPtPtConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 14),
    _AtmSwchPortPvpPtPtConns_Type()
)
atmSwchPortPvpPtPtConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvpPtPtConns.setStatus("mandatory")


class _AtmSwchPortPvpPtMptRootConns_Type(Integer32):
    """Custom type atmSwchPortPvpPtMptRootConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvpPtMptRootConns_Type.__name__ = "Integer32"
_AtmSwchPortPvpPtMptRootConns_Object = MibTableColumn
atmSwchPortPvpPtMptRootConns = _AtmSwchPortPvpPtMptRootConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 15),
    _AtmSwchPortPvpPtMptRootConns_Type()
)
atmSwchPortPvpPtMptRootConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvpPtMptRootConns.setStatus("mandatory")


class _AtmSwchPortPvpPtMptLeafConns_Type(Integer32):
    """Custom type atmSwchPortPvpPtMptLeafConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchPortPvpPtMptLeafConns_Type.__name__ = "Integer32"
_AtmSwchPortPvpPtMptLeafConns_Object = MibTableColumn
atmSwchPortPvpPtMptLeafConns = _AtmSwchPortPvpPtMptLeafConns_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 16),
    _AtmSwchPortPvpPtMptLeafConns_Type()
)
atmSwchPortPvpPtMptLeafConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchPortPvpPtMptLeafConns.setStatus("mandatory")


class _AtmSwchPortdsx3CellMaping_Type(Integer32):
    """Custom type atmSwchPortdsx3CellMaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx3ADM", 1),
          ("dsx3PLCP", 2))
    )


_AtmSwchPortdsx3CellMaping_Type.__name__ = "Integer32"
_AtmSwchPortdsx3CellMaping_Object = MibTableColumn
atmSwchPortdsx3CellMaping = _AtmSwchPortdsx3CellMaping_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 17),
    _AtmSwchPortdsx3CellMaping_Type()
)
atmSwchPortdsx3CellMaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchPortdsx3CellMaping.setStatus("mandatory")
_AtmSwchVPort_ObjectIdentity = ObjectIdentity
atmSwchVPort = _AtmSwchVPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 7)
)
_AtmSwchVPortTable_Object = MibTable
atmSwchVPortTable = _AtmSwchVPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1)
)
if mibBuilder.loadTexts:
    atmSwchVPortTable.setStatus("mandatory")
_AtmSwchVPortEntry_Object = MibTableRow
atmSwchVPortEntry = _AtmSwchVPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1)
)
atmSwchVPortEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchSlotIndex"),
    (0, "ATMSWCH-MIB", "atmSwchPortIndex"),
    (0, "ATMSWCH-MIB", "atmSwchVPortIndex"),
)
if mibBuilder.loadTexts:
    atmSwchVPortEntry.setStatus("mandatory")
_AtmSwchVPortIndex_Type = Integer32
_AtmSwchVPortIndex_Object = MibTableColumn
atmSwchVPortIndex = _AtmSwchVPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 1),
    _AtmSwchVPortIndex_Type()
)
atmSwchVPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortIndex.setStatus("mandatory")


class _AtmSwchVPortIsRoot_Type(Integer32):
    """Custom type atmSwchVPortIsRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isRoot", 1),
          ("notRoot", 2))
    )


_AtmSwchVPortIsRoot_Type.__name__ = "Integer32"
_AtmSwchVPortIsRoot_Object = MibTableColumn
atmSwchVPortIsRoot = _AtmSwchVPortIsRoot_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 2),
    _AtmSwchVPortIsRoot_Type()
)
atmSwchVPortIsRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortIsRoot.setStatus("mandatory")


class _AtmSwchVPortAdminStatus_Type(Integer32):
    """Custom type atmSwchVPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmSwchVPortAdminStatus_Type.__name__ = "Integer32"
_AtmSwchVPortAdminStatus_Object = MibTableColumn
atmSwchVPortAdminStatus = _AtmSwchVPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 3),
    _AtmSwchVPortAdminStatus_Type()
)
atmSwchVPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortAdminStatus.setStatus("mandatory")


class _AtmSwchVPortOperStatus_Type(Integer32):
    """Custom type atmSwchVPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmSwchVPortOperStatus_Type.__name__ = "Integer32"
_AtmSwchVPortOperStatus_Object = MibTableColumn
atmSwchVPortOperStatus = _AtmSwchVPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 4),
    _AtmSwchVPortOperStatus_Type()
)
atmSwchVPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortOperStatus.setStatus("mandatory")


class _AtmSwchVPortCurrentSignallingState_Type(Integer32):
    """Custom type atmSwchVPortCurrentSignallingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_AtmSwchVPortCurrentSignallingState_Type.__name__ = "Integer32"
_AtmSwchVPortCurrentSignallingState_Object = MibTableColumn
atmSwchVPortCurrentSignallingState = _AtmSwchVPortCurrentSignallingState_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 5),
    _AtmSwchVPortCurrentSignallingState_Type()
)
atmSwchVPortCurrentSignallingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortCurrentSignallingState.setStatus("mandatory")


class _AtmSwchVPortCurrentILMIState_Type(Integer32):
    """Custom type atmSwchVPortCurrentILMIState based on Integer32"""
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
          ("stackOff", 3),
          ("up", 1))
    )


_AtmSwchVPortCurrentILMIState_Type.__name__ = "Integer32"
_AtmSwchVPortCurrentILMIState_Object = MibTableColumn
atmSwchVPortCurrentILMIState = _AtmSwchVPortCurrentILMIState_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 6),
    _AtmSwchVPortCurrentILMIState_Type()
)
atmSwchVPortCurrentILMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortCurrentILMIState.setStatus("mandatory")


class _AtmSwchVPortCurrentAddrRegEn_Type(Integer32):
    """Custom type atmSwchVPortCurrentAddrRegEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_AtmSwchVPortCurrentAddrRegEn_Type.__name__ = "Integer32"
_AtmSwchVPortCurrentAddrRegEn_Object = MibTableColumn
atmSwchVPortCurrentAddrRegEn = _AtmSwchVPortCurrentAddrRegEn_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 7),
    _AtmSwchVPortCurrentAddrRegEn_Type()
)
atmSwchVPortCurrentAddrRegEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortCurrentAddrRegEn.setStatus("mandatory")


class _AtmSwchVPortCurrentLinkType_Type(Integer32):
    """Custom type atmSwchVPortCurrentLinkType based on Integer32"""
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
        *(("iisp30", 4),
          ("iisp31", 5),
          ("pnni10", 6),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 7),
          ("unknown", 1))
    )


_AtmSwchVPortCurrentLinkType_Type.__name__ = "Integer32"
_AtmSwchVPortCurrentLinkType_Object = MibTableColumn
atmSwchVPortCurrentLinkType = _AtmSwchVPortCurrentLinkType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 8),
    _AtmSwchVPortCurrentLinkType_Type()
)
atmSwchVPortCurrentLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortCurrentLinkType.setStatus("mandatory")


class _AtmSwchVPortCurrentTermType_Type(Integer32):
    """Custom type atmSwchVPortCurrentTermType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 3),
          ("unknown", 1),
          ("user", 2))
    )


_AtmSwchVPortCurrentTermType_Type.__name__ = "Integer32"
_AtmSwchVPortCurrentTermType_Object = MibTableColumn
atmSwchVPortCurrentTermType = _AtmSwchVPortCurrentTermType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 9),
    _AtmSwchVPortCurrentTermType_Type()
)
atmSwchVPortCurrentTermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortCurrentTermType.setStatus("mandatory")


class _AtmSwchVPortConfigILMIState_Type(Integer32):
    """Custom type atmSwchVPortConfigILMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stackDisabled", 2),
          ("stackEnabled", 1))
    )


_AtmSwchVPortConfigILMIState_Type.__name__ = "Integer32"
_AtmSwchVPortConfigILMIState_Object = MibTableColumn
atmSwchVPortConfigILMIState = _AtmSwchVPortConfigILMIState_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 10),
    _AtmSwchVPortConfigILMIState_Type()
)
atmSwchVPortConfigILMIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfigILMIState.setStatus("mandatory")


class _AtmSwchVPortConfigAddrRegEn_Type(Integer32):
    """Custom type atmSwchVPortConfigAddrRegEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("disabled", 3),
          ("enabled", 2))
    )


_AtmSwchVPortConfigAddrRegEn_Type.__name__ = "Integer32"
_AtmSwchVPortConfigAddrRegEn_Object = MibTableColumn
atmSwchVPortConfigAddrRegEn = _AtmSwchVPortConfigAddrRegEn_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 11),
    _AtmSwchVPortConfigAddrRegEn_Type()
)
atmSwchVPortConfigAddrRegEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfigAddrRegEn.setStatus("mandatory")


class _AtmSwchVPortConfigLinkType_Type(Integer32):
    """Custom type atmSwchVPortConfigLinkType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("iisp30", 5),
          ("iisp31", 6),
          ("pnni10", 7),
          ("uni30", 3),
          ("uni31", 4),
          ("uni40", 8),
          ("unknown", 2))
    )


_AtmSwchVPortConfigLinkType_Type.__name__ = "Integer32"
_AtmSwchVPortConfigLinkType_Object = MibTableColumn
atmSwchVPortConfigLinkType = _AtmSwchVPortConfigLinkType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 12),
    _AtmSwchVPortConfigLinkType_Type()
)
atmSwchVPortConfigLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfigLinkType.setStatus("mandatory")


class _AtmSwchVPortConfigTermType_Type(Integer32):
    """Custom type atmSwchVPortConfigTermType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("network", 3),
          ("user", 2))
    )


_AtmSwchVPortConfigTermType_Type.__name__ = "Integer32"
_AtmSwchVPortConfigTermType_Object = MibTableColumn
atmSwchVPortConfigTermType = _AtmSwchVPortConfigTermType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 13),
    _AtmSwchVPortConfigTermType_Type()
)
atmSwchVPortConfigTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfigTermType.setStatus("mandatory")


class _AtmSwchVPortNeighbourSysName_Type(DisplayString):
    """Custom type atmSwchVPortNeighbourSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtmSwchVPortNeighbourSysName_Type.__name__ = "DisplayString"
_AtmSwchVPortNeighbourSysName_Object = MibTableColumn
atmSwchVPortNeighbourSysName = _AtmSwchVPortNeighbourSysName_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 14),
    _AtmSwchVPortNeighbourSysName_Type()
)
atmSwchVPortNeighbourSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortNeighbourSysName.setStatus("mandatory")


class _AtmSwchVPortNeighbourUNIVersion_Type(Integer32):
    """Custom type atmSwchVPortNeighbourUNIVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 5),
          ("notKnown", 1),
          ("pnni10", 6),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 4))
    )


_AtmSwchVPortNeighbourUNIVersion_Type.__name__ = "Integer32"
_AtmSwchVPortNeighbourUNIVersion_Object = MibTableColumn
atmSwchVPortNeighbourUNIVersion = _AtmSwchVPortNeighbourUNIVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 15),
    _AtmSwchVPortNeighbourUNIVersion_Type()
)
atmSwchVPortNeighbourUNIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortNeighbourUNIVersion.setStatus("mandatory")
_AtmSwchVPortNeighbourATMAddress_Type = AtmAddress
_AtmSwchVPortNeighbourATMAddress_Object = MibTableColumn
atmSwchVPortNeighbourATMAddress = _AtmSwchVPortNeighbourATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 16),
    _AtmSwchVPortNeighbourATMAddress_Type()
)
atmSwchVPortNeighbourATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortNeighbourATMAddress.setStatus("mandatory")
_AtmSwchVPortNeighbourIfName_Type = DisplayString
_AtmSwchVPortNeighbourIfName_Object = MibTableColumn
atmSwchVPortNeighbourIfName = _AtmSwchVPortNeighbourIfName_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 17),
    _AtmSwchVPortNeighbourIfName_Type()
)
atmSwchVPortNeighbourIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortNeighbourIfName.setStatus("mandatory")


class _AtmSwchVPortMibProbe_Type(Integer32):
    """Custom type atmSwchVPortMibProbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AtmSwchVPortMibProbe_Type.__name__ = "Integer32"
_AtmSwchVPortMibProbe_Object = MibTableColumn
atmSwchVPortMibProbe = _AtmSwchVPortMibProbe_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 18),
    _AtmSwchVPortMibProbe_Type()
)
atmSwchVPortMibProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortMibProbe.setStatus("mandatory")


class _AtmSwchVPortConfMinSvccVci_Type(Integer32):
    """Custom type atmSwchVPortConfMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchVPortConfMinSvccVci_Type.__name__ = "Integer32"
_AtmSwchVPortConfMinSvccVci_Object = MibTableColumn
atmSwchVPortConfMinSvccVci = _AtmSwchVPortConfMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 19),
    _AtmSwchVPortConfMinSvccVci_Type()
)
atmSwchVPortConfMinSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfMinSvccVci.setStatus("mandatory")


class _AtmSwchVPortConfMaxSvccVci_Type(Integer32):
    """Custom type atmSwchVPortConfMaxSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchVPortConfMaxSvccVci_Type.__name__ = "Integer32"
_AtmSwchVPortConfMaxSvccVci_Object = MibTableColumn
atmSwchVPortConfMaxSvccVci = _AtmSwchVPortConfMaxSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 20),
    _AtmSwchVPortConfMaxSvccVci_Type()
)
atmSwchVPortConfMaxSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfMaxSvccVci.setStatus("mandatory")


class _AtmSwchVPortConfMinVpi_Type(Integer32):
    """Custom type atmSwchVPortConfMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSwchVPortConfMinVpi_Type.__name__ = "Integer32"
_AtmSwchVPortConfMinVpi_Object = MibTableColumn
atmSwchVPortConfMinVpi = _AtmSwchVPortConfMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 21),
    _AtmSwchVPortConfMinVpi_Type()
)
atmSwchVPortConfMinVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfMinVpi.setStatus("mandatory")


class _AtmSwchVPortConfMaxVpi_Type(Integer32):
    """Custom type atmSwchVPortConfMaxVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSwchVPortConfMaxVpi_Type.__name__ = "Integer32"
_AtmSwchVPortConfMaxVpi_Object = MibTableColumn
atmSwchVPortConfMaxVpi = _AtmSwchVPortConfMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 22),
    _AtmSwchVPortConfMaxVpi_Type()
)
atmSwchVPortConfMaxVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortConfMaxVpi.setStatus("mandatory")
_AtmSwchVPortNeighbourIpAddress_Type = IpAddress
_AtmSwchVPortNeighbourIpAddress_Object = MibTableColumn
atmSwchVPortNeighbourIpAddress = _AtmSwchVPortNeighbourIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 23),
    _AtmSwchVPortNeighbourIpAddress_Type()
)
atmSwchVPortNeighbourIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchVPortNeighbourIpAddress.setStatus("mandatory")
_AtmSwchVPortPcr_Type = Integer32
_AtmSwchVPortPcr_Object = MibTableColumn
atmSwchVPortPcr = _AtmSwchVPortPcr_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 24),
    _AtmSwchVPortPcr_Type()
)
atmSwchVPortPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortPcr.setStatus("mandatory")
_AtmSwchVPortRowStatus_Type = RowStatus
_AtmSwchVPortRowStatus_Object = MibTableColumn
atmSwchVPortRowStatus = _AtmSwchVPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 25),
    _AtmSwchVPortRowStatus_Type()
)
atmSwchVPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchVPortRowStatus.setStatus("mandatory")
_AtmSwchSlotRoute_ObjectIdentity = ObjectIdentity
atmSwchSlotRoute = _AtmSwchSlotRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 8)
)
_AtmSwchSlotRouteTable_Object = MibTable
atmSwchSlotRouteTable = _AtmSwchSlotRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1)
)
if mibBuilder.loadTexts:
    atmSwchSlotRouteTable.setStatus("mandatory")
_AtmSwchSlotRouteEntry_Object = MibTableRow
atmSwchSlotRouteEntry = _AtmSwchSlotRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1)
)
atmSwchSlotRouteEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchSlotIndex"),
    (0, "ATMSWCH-MIB", "atmSwchSlotRouteId"),
)
if mibBuilder.loadTexts:
    atmSwchSlotRouteEntry.setStatus("mandatory")
_AtmSwchSlotRouteId_Type = Integer32
_AtmSwchSlotRouteId_Object = MibTableColumn
atmSwchSlotRouteId = _AtmSwchSlotRouteId_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 1),
    _AtmSwchSlotRouteId_Type()
)
atmSwchSlotRouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotRouteId.setStatus("mandatory")
_AtmSwchSlotRouteRowStatus_Type = RowStatus
_AtmSwchSlotRouteRowStatus_Object = MibTableColumn
atmSwchSlotRouteRowStatus = _AtmSwchSlotRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 2),
    _AtmSwchSlotRouteRowStatus_Type()
)
atmSwchSlotRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRouteRowStatus.setStatus("mandatory")
_AtmSwchSlotRouteAddressPrefix_Type = AtmAddress
_AtmSwchSlotRouteAddressPrefix_Object = MibTableColumn
atmSwchSlotRouteAddressPrefix = _AtmSwchSlotRouteAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 3),
    _AtmSwchSlotRouteAddressPrefix_Type()
)
atmSwchSlotRouteAddressPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRouteAddressPrefix.setStatus("mandatory")


class _AtmSwchSlotRoutePrefixLength_Type(Integer32):
    """Custom type atmSwchSlotRoutePrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )


_AtmSwchSlotRoutePrefixLength_Type.__name__ = "Integer32"
_AtmSwchSlotRoutePrefixLength_Object = MibTableColumn
atmSwchSlotRoutePrefixLength = _AtmSwchSlotRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 4),
    _AtmSwchSlotRoutePrefixLength_Type()
)
atmSwchSlotRoutePrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRoutePrefixLength.setStatus("mandatory")


class _AtmSwchSlotRoutePriority_Type(Integer32):
    """Custom type atmSwchSlotRoutePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AtmSwchSlotRoutePriority_Type.__name__ = "Integer32"
_AtmSwchSlotRoutePriority_Object = MibTableColumn
atmSwchSlotRoutePriority = _AtmSwchSlotRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 5),
    _AtmSwchSlotRoutePriority_Type()
)
atmSwchSlotRoutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRoutePriority.setStatus("mandatory")


class _AtmSwchSlotRouteSlot_Type(Integer32):
    """Custom type atmSwchSlotRouteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmSwchSlotRouteSlot_Type.__name__ = "Integer32"
_AtmSwchSlotRouteSlot_Object = MibTableColumn
atmSwchSlotRouteSlot = _AtmSwchSlotRouteSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 6),
    _AtmSwchSlotRouteSlot_Type()
)
atmSwchSlotRouteSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRouteSlot.setStatus("mandatory")


class _AtmSwchSlotRoutePort_Type(Integer32):
    """Custom type atmSwchSlotRoutePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmSwchSlotRoutePort_Type.__name__ = "Integer32"
_AtmSwchSlotRoutePort_Object = MibTableColumn
atmSwchSlotRoutePort = _AtmSwchSlotRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 7),
    _AtmSwchSlotRoutePort_Type()
)
atmSwchSlotRoutePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRoutePort.setStatus("mandatory")


class _AtmSwchSlotRouteVport_Type(Integer32):
    """Custom type atmSwchSlotRouteVport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmSwchSlotRouteVport_Type.__name__ = "Integer32"
_AtmSwchSlotRouteVport_Object = MibTableColumn
atmSwchSlotRouteVport = _AtmSwchSlotRouteVport_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 8),
    _AtmSwchSlotRouteVport_Type()
)
atmSwchSlotRouteVport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwchSlotRouteVport.setStatus("mandatory")


class _AtmSwchSlotRouteOrigin_Type(Integer32):
    """Custom type atmSwchSlotRouteOrigin based on Integer32"""
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
        *(("dynamic", 5),
          ("ilmi", 3),
          ("lane", 4),
          ("nonVolatile", 1),
          ("snmp", 2))
    )


_AtmSwchSlotRouteOrigin_Type.__name__ = "Integer32"
_AtmSwchSlotRouteOrigin_Object = MibTableColumn
atmSwchSlotRouteOrigin = _AtmSwchSlotRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 9),
    _AtmSwchSlotRouteOrigin_Type()
)
atmSwchSlotRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotRouteOrigin.setStatus("mandatory")


class _AtmSwchSlotRouteOperStatus_Type(Integer32):
    """Custom type atmSwchSlotRouteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmSwchSlotRouteOperStatus_Type.__name__ = "Integer32"
_AtmSwchSlotRouteOperStatus_Object = MibTableColumn
atmSwchSlotRouteOperStatus = _AtmSwchSlotRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 10),
    _AtmSwchSlotRouteOperStatus_Type()
)
atmSwchSlotRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotRouteOperStatus.setStatus("mandatory")
_AtmSwchSlotAddrVcl_ObjectIdentity = ObjectIdentity
atmSwchSlotAddrVcl = _AtmSwchSlotAddrVcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 33, 9)
)
_AtmSwchSlotAddrVclTable_Object = MibTable
atmSwchSlotAddrVclTable = _AtmSwchSlotAddrVclTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1)
)
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclTable.setStatus("mandatory")
_AtmSwchSlotAddrVclEntry_Object = MibTableRow
atmSwchSlotAddrVclEntry = _AtmSwchSlotAddrVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1)
)
atmSwchSlotAddrVclEntry.setIndexNames(
    (0, "ATMSWCH-MIB", "atmSwchSlotIndex"),
    (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclAddr"),
    (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclAtmIfIndex"),
    (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclVpi"),
    (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclVci"),
)
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclEntry.setStatus("mandatory")
_AtmSwchSlotAddrVclAddr_Type = AtmAddress
_AtmSwchSlotAddrVclAddr_Object = MibTableColumn
atmSwchSlotAddrVclAddr = _AtmSwchSlotAddrVclAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 1),
    _AtmSwchSlotAddrVclAddr_Type()
)
atmSwchSlotAddrVclAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclAddr.setStatus("mandatory")
_AtmSwchSlotAddrVclAtmIfIndex_Type = Integer32
_AtmSwchSlotAddrVclAtmIfIndex_Object = MibTableColumn
atmSwchSlotAddrVclAtmIfIndex = _AtmSwchSlotAddrVclAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 2),
    _AtmSwchSlotAddrVclAtmIfIndex_Type()
)
atmSwchSlotAddrVclAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclAtmIfIndex.setStatus("mandatory")


class _AtmSwchSlotAddrVclVpi_Type(Integer32):
    """Custom type atmSwchSlotAddrVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSwchSlotAddrVclVpi_Type.__name__ = "Integer32"
_AtmSwchSlotAddrVclVpi_Object = MibTableColumn
atmSwchSlotAddrVclVpi = _AtmSwchSlotAddrVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 3),
    _AtmSwchSlotAddrVclVpi_Type()
)
atmSwchSlotAddrVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclVpi.setStatus("mandatory")


class _AtmSwchSlotAddrVclVci_Type(Integer32):
    """Custom type atmSwchSlotAddrVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSwchSlotAddrVclVci_Type.__name__ = "Integer32"
_AtmSwchSlotAddrVclVci_Object = MibTableColumn
atmSwchSlotAddrVclVci = _AtmSwchSlotAddrVclVci_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 4),
    _AtmSwchSlotAddrVclVci_Type()
)
atmSwchSlotAddrVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclVci.setStatus("mandatory")


class _AtmSwchSlotAddrVclAddrType_Type(Integer32):
    """Custom type atmSwchSlotAddrVclAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calledParty", 2),
          ("callingParty", 1))
    )


_AtmSwchSlotAddrVclAddrType_Type.__name__ = "Integer32"
_AtmSwchSlotAddrVclAddrType_Object = MibTableColumn
atmSwchSlotAddrVclAddrType = _AtmSwchSlotAddrVclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 5),
    _AtmSwchSlotAddrVclAddrType_Type()
)
atmSwchSlotAddrVclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSwchSlotAddrVclAddrType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMSWCH-MIB",
    **{"AtmAddress": AtmAddress,
       "AtmPrefix": AtmPrefix,
       "atmSwch": atmSwch,
       "atmSwchBase": atmSwchBase,
       "atmSwchBaseCurrentPrefix": atmSwchBaseCurrentPrefix,
       "atmSwchBaseConfigPrefix": atmSwchBaseConfigPrefix,
       "atmSwchBaseEpdThreshold": atmSwchBaseEpdThreshold,
       "atmSwchBaseAmonAdminState": atmSwchBaseAmonAdminState,
       "atmSwchCpu": atmSwchCpu,
       "atmSwchCpuTable": atmSwchCpuTable,
       "atmSwchCpuEntry": atmSwchCpuEntry,
       "atmSwchCpuIndex": atmSwchCpuIndex,
       "atmSwchCpuHwVersion": atmSwchCpuHwVersion,
       "atmSwchCpuSoftErrCode": atmSwchCpuSoftErrCode,
       "atmSwchCpuSoftErrString": atmSwchCpuSoftErrString,
       "atmSwchCpuUtilization": atmSwchCpuUtilization,
       "atmSwchCpuRamSize": atmSwchCpuRamSize,
       "atmSwchCpuRamUsed": atmSwchCpuRamUsed,
       "atmSwchCpuFlashSize": atmSwchCpuFlashSize,
       "atmSwchCpuFlashUsed": atmSwchCpuFlashUsed,
       "atmSwchCpuEepromSize": atmSwchCpuEepromSize,
       "atmSwchCpuEepromUsed": atmSwchCpuEepromUsed,
       "atmSwchCpuTime": atmSwchCpuTime,
       "atmSwchCpuSysUpTime": atmSwchCpuSysUpTime,
       "atmSwchCpuSvcPtPtInConns": atmSwchCpuSvcPtPtInConns,
       "atmSwchCpuSvcPtPtOutConns": atmSwchCpuSvcPtPtOutConns,
       "atmSwchCpuSvcPtMptRootConns": atmSwchCpuSvcPtMptRootConns,
       "atmSwchCpuSvcPtMptLeafConns": atmSwchCpuSvcPtMptLeafConns,
       "atmSwchCpuPvcPtPtConns": atmSwchCpuPvcPtPtConns,
       "atmSwchSlot": atmSwchSlot,
       "atmSwchSlotTable": atmSwchSlotTable,
       "atmSwchSlotEntry": atmSwchSlotEntry,
       "atmSwchSlotIndex": atmSwchSlotIndex,
       "atmSwchSlotRxCellDiscards": atmSwchSlotRxCellDiscards,
       "atmSwchSlotRouteNextId": atmSwchSlotRouteNextId,
       "atmSwchSlotAPSMode": atmSwchSlotAPSMode,
       "atmSwchSlotAPSCurrentState": atmSwchSlotAPSCurrentState,
       "atmSwchSlotAPSSwitchCommand": atmSwchSlotAPSSwitchCommand,
       "atmSwchSlotAPSSFBerThreshold": atmSwchSlotAPSSFBerThreshold,
       "atmSwchSlotAPSSDBerThreshold": atmSwchSlotAPSSDBerThreshold,
       "atmSwchSlotAPSDecision": atmSwchSlotAPSDecision,
       "atmSwchPort": atmSwchPort,
       "atmSwchPortTable": atmSwchPortTable,
       "atmSwchPortEntry": atmSwchPortEntry,
       "atmSwchPortIndex": atmSwchPortIndex,
       "atmSwchPortRootVportIndex": atmSwchPortRootVportIndex,
       "atmSwchPortNumVPorts": atmSwchPortNumVPorts,
       "atmSwchPortPayloadScramble": atmSwchPortPayloadScramble,
       "atmSwchPortPhysicalType": atmSwchPortPhysicalType,
       "atmSwchPortMaxTxRate": atmSwchPortMaxTxRate,
       "atmSwchPortSvcPtPtInConns": atmSwchPortSvcPtPtInConns,
       "atmSwchPortSvcPtPtOutConns": atmSwchPortSvcPtPtOutConns,
       "atmSwchPortSvcPtMptRootConns": atmSwchPortSvcPtMptRootConns,
       "atmSwchPortSvcPtMptLeafConns": atmSwchPortSvcPtMptLeafConns,
       "atmSwchPortPvcPtPtConns": atmSwchPortPvcPtPtConns,
       "atmSwchPortPvcPtMptRootConns": atmSwchPortPvcPtMptRootConns,
       "atmSwchPortPvcPtMptLeafConns": atmSwchPortPvcPtMptLeafConns,
       "atmSwchPortPvpPtPtConns": atmSwchPortPvpPtPtConns,
       "atmSwchPortPvpPtMptRootConns": atmSwchPortPvpPtMptRootConns,
       "atmSwchPortPvpPtMptLeafConns": atmSwchPortPvpPtMptLeafConns,
       "atmSwchPortdsx3CellMaping": atmSwchPortdsx3CellMaping,
       "atmSwchVPort": atmSwchVPort,
       "atmSwchVPortTable": atmSwchVPortTable,
       "atmSwchVPortEntry": atmSwchVPortEntry,
       "atmSwchVPortIndex": atmSwchVPortIndex,
       "atmSwchVPortIsRoot": atmSwchVPortIsRoot,
       "atmSwchVPortAdminStatus": atmSwchVPortAdminStatus,
       "atmSwchVPortOperStatus": atmSwchVPortOperStatus,
       "atmSwchVPortCurrentSignallingState": atmSwchVPortCurrentSignallingState,
       "atmSwchVPortCurrentILMIState": atmSwchVPortCurrentILMIState,
       "atmSwchVPortCurrentAddrRegEn": atmSwchVPortCurrentAddrRegEn,
       "atmSwchVPortCurrentLinkType": atmSwchVPortCurrentLinkType,
       "atmSwchVPortCurrentTermType": atmSwchVPortCurrentTermType,
       "atmSwchVPortConfigILMIState": atmSwchVPortConfigILMIState,
       "atmSwchVPortConfigAddrRegEn": atmSwchVPortConfigAddrRegEn,
       "atmSwchVPortConfigLinkType": atmSwchVPortConfigLinkType,
       "atmSwchVPortConfigTermType": atmSwchVPortConfigTermType,
       "atmSwchVPortNeighbourSysName": atmSwchVPortNeighbourSysName,
       "atmSwchVPortNeighbourUNIVersion": atmSwchVPortNeighbourUNIVersion,
       "atmSwchVPortNeighbourATMAddress": atmSwchVPortNeighbourATMAddress,
       "atmSwchVPortNeighbourIfName": atmSwchVPortNeighbourIfName,
       "atmSwchVPortMibProbe": atmSwchVPortMibProbe,
       "atmSwchVPortConfMinSvccVci": atmSwchVPortConfMinSvccVci,
       "atmSwchVPortConfMaxSvccVci": atmSwchVPortConfMaxSvccVci,
       "atmSwchVPortConfMinVpi": atmSwchVPortConfMinVpi,
       "atmSwchVPortConfMaxVpi": atmSwchVPortConfMaxVpi,
       "atmSwchVPortNeighbourIpAddress": atmSwchVPortNeighbourIpAddress,
       "atmSwchVPortPcr": atmSwchVPortPcr,
       "atmSwchVPortRowStatus": atmSwchVPortRowStatus,
       "atmSwchSlotRoute": atmSwchSlotRoute,
       "atmSwchSlotRouteTable": atmSwchSlotRouteTable,
       "atmSwchSlotRouteEntry": atmSwchSlotRouteEntry,
       "atmSwchSlotRouteId": atmSwchSlotRouteId,
       "atmSwchSlotRouteRowStatus": atmSwchSlotRouteRowStatus,
       "atmSwchSlotRouteAddressPrefix": atmSwchSlotRouteAddressPrefix,
       "atmSwchSlotRoutePrefixLength": atmSwchSlotRoutePrefixLength,
       "atmSwchSlotRoutePriority": atmSwchSlotRoutePriority,
       "atmSwchSlotRouteSlot": atmSwchSlotRouteSlot,
       "atmSwchSlotRoutePort": atmSwchSlotRoutePort,
       "atmSwchSlotRouteVport": atmSwchSlotRouteVport,
       "atmSwchSlotRouteOrigin": atmSwchSlotRouteOrigin,
       "atmSwchSlotRouteOperStatus": atmSwchSlotRouteOperStatus,
       "atmSwchSlotAddrVcl": atmSwchSlotAddrVcl,
       "atmSwchSlotAddrVclTable": atmSwchSlotAddrVclTable,
       "atmSwchSlotAddrVclEntry": atmSwchSlotAddrVclEntry,
       "atmSwchSlotAddrVclAddr": atmSwchSlotAddrVclAddr,
       "atmSwchSlotAddrVclAtmIfIndex": atmSwchSlotAddrVclAtmIfIndex,
       "atmSwchSlotAddrVclVpi": atmSwchSlotAddrVclVpi,
       "atmSwchSlotAddrVclVci": atmSwchSlotAddrVclVci,
       "atmSwchSlotAddrVclAddrType": atmSwchSlotAddrVclAddrType}
)
