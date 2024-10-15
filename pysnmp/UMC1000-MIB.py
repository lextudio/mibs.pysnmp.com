# SNMP MIB module (UMC1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMC1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:28 2024
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

(umc1000,) = mibBuilder.importSymbols(
    "AFC-OIDS",
    "umc1000")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TerminalIdType(Integer32):
    """Custom type TerminalIdType based on Integer32"""




class ShelfIdType(Integer32):
    """Custom type ShelfIdType based on Integer32"""




class SlotIdType(Integer32):
    """Custom type SlotIdType based on Integer32"""




class PlugInType(Integer32):
    """Custom type PlugInType based on Integer32"""




class DbActionType(Integer32):
    """Custom type DbActionType based on Integer32"""




class V5GroupIdType(Integer32):
    """Custom type V5GroupIdType based on Integer32"""




class DataOperation(Integer32):
    """Custom type DataOperation based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Umc1System_ObjectIdentity = ObjectIdentity
umc1System = _Umc1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1)
)


class _Umc1SystemDateTime_Type(OctetString):
    """Custom type umc1SystemDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Umc1SystemDateTime_Type.__name__ = "OctetString"
_Umc1SystemDateTime_Object = MibScalar
umc1SystemDateTime = _Umc1SystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 1),
    _Umc1SystemDateTime_Type()
)
umc1SystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemDateTime.setStatus("mandatory")
_Umc1SystemSysProv_ObjectIdentity = ObjectIdentity
umc1SystemSysProv = _Umc1SystemSysProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2)
)
_Umc1SystemSysProvBerTable_Object = MibTable
umc1SystemSysProvBerTable = _Umc1SystemSysProvBerTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    umc1SystemSysProvBerTable.setStatus("mandatory")
_Umc1SystemSysProvBerEntry_Object = MibTableRow
umc1SystemSysProvBerEntry = _Umc1SystemSysProvBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1, 1)
)
umc1SystemSysProvBerEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemSysProvBerPit"),
)
if mibBuilder.loadTexts:
    umc1SystemSysProvBerEntry.setStatus("mandatory")
_Umc1SystemSysProvBerPit_Type = PlugInType
_Umc1SystemSysProvBerPit_Object = MibTableColumn
umc1SystemSysProvBerPit = _Umc1SystemSysProvBerPit_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1, 1, 1),
    _Umc1SystemSysProvBerPit_Type()
)
umc1SystemSysProvBerPit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvBerPit.setStatus("mandatory")
_Umc1SystemSysProvBerRedThresh_Type = Integer32
_Umc1SystemSysProvBerRedThresh_Object = MibTableColumn
umc1SystemSysProvBerRedThresh = _Umc1SystemSysProvBerRedThresh_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1, 1, 2),
    _Umc1SystemSysProvBerRedThresh_Type()
)
umc1SystemSysProvBerRedThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvBerRedThresh.setStatus("mandatory")
_Umc1SystemSysProvBerMaintThresh_Type = Integer32
_Umc1SystemSysProvBerMaintThresh_Object = MibTableColumn
umc1SystemSysProvBerMaintThresh = _Umc1SystemSysProvBerMaintThresh_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1, 1, 3),
    _Umc1SystemSysProvBerMaintThresh_Type()
)
umc1SystemSysProvBerMaintThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvBerMaintThresh.setStatus("mandatory")
_Umc1SystemSysProvBerMarginData_Type = Integer32
_Umc1SystemSysProvBerMarginData_Object = MibTableColumn
umc1SystemSysProvBerMarginData = _Umc1SystemSysProvBerMarginData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 1, 1, 4),
    _Umc1SystemSysProvBerMarginData_Type()
)
umc1SystemSysProvBerMarginData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvBerMarginData.setStatus("mandatory")
_Umc1SystemSysProvSystemCcsThresh_Type = Integer32
_Umc1SystemSysProvSystemCcsThresh_Object = MibScalar
umc1SystemSysProvSystemCcsThresh = _Umc1SystemSysProvSystemCcsThresh_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 2),
    _Umc1SystemSysProvSystemCcsThresh_Type()
)
umc1SystemSysProvSystemCcsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvSystemCcsThresh.setStatus("mandatory")
_Umc1SystemSysProvPsuRingVoltage_Type = Integer32
_Umc1SystemSysProvPsuRingVoltage_Object = MibScalar
umc1SystemSysProvPsuRingVoltage = _Umc1SystemSysProvPsuRingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 3),
    _Umc1SystemSysProvPsuRingVoltage_Type()
)
umc1SystemSysProvPsuRingVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvPsuRingVoltage.setStatus("mandatory")
_Umc1SystemSysProvPsuPulseMeterTone_Type = Integer32
_Umc1SystemSysProvPsuPulseMeterTone_Object = MibScalar
umc1SystemSysProvPsuPulseMeterTone = _Umc1SystemSysProvPsuPulseMeterTone_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 4),
    _Umc1SystemSysProvPsuPulseMeterTone_Type()
)
umc1SystemSysProvPsuPulseMeterTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvPsuPulseMeterTone.setStatus("mandatory")
_Umc1SystemSysProvPsuRingFreq_Type = Integer32
_Umc1SystemSysProvPsuRingFreq_Object = MibScalar
umc1SystemSysProvPsuRingFreq = _Umc1SystemSysProvPsuRingFreq_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 5),
    _Umc1SystemSysProvPsuRingFreq_Type()
)
umc1SystemSysProvPsuRingFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvPsuRingFreq.setStatus("mandatory")
_Umc1SystemSysProvChgTable_Object = MibTable
umc1SystemSysProvChgTable = _Umc1SystemSysProvChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    umc1SystemSysProvChgTable.setStatus("mandatory")
_Umc1SystemSysProvChgEntry_Object = MibTableRow
umc1SystemSysProvChgEntry = _Umc1SystemSysProvChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 6, 1)
)
umc1SystemSysProvChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemSysProvChgSeqNbr"),
)
if mibBuilder.loadTexts:
    umc1SystemSysProvChgEntry.setStatus("mandatory")
_Umc1SystemSysProvChgSeqNbr_Type = Integer32
_Umc1SystemSysProvChgSeqNbr_Object = MibTableColumn
umc1SystemSysProvChgSeqNbr = _Umc1SystemSysProvChgSeqNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 6, 1, 1),
    _Umc1SystemSysProvChgSeqNbr_Type()
)
umc1SystemSysProvChgSeqNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemSysProvChgSeqNbr.setStatus("mandatory")


class _Umc1SystemSysProvChgData_Type(OctetString):
    """Custom type umc1SystemSysProvChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemSysProvChgData_Type.__name__ = "OctetString"
_Umc1SystemSysProvChgData_Object = MibTableColumn
umc1SystemSysProvChgData = _Umc1SystemSysProvChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 6, 1, 2),
    _Umc1SystemSysProvChgData_Type()
)
umc1SystemSysProvChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemSysProvChgData.setStatus("mandatory")


class _Umc1SystemSysProvTableChangeSeqNum_Type(Integer32):
    """Custom type umc1SystemSysProvTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemSysProvTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1SystemSysProvTableChangeSeqNum_Object = MibScalar
umc1SystemSysProvTableChangeSeqNum = _Umc1SystemSysProvTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 7),
    _Umc1SystemSysProvTableChangeSeqNum_Type()
)
umc1SystemSysProvTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemSysProvTableChangeSeqNum.setStatus("mandatory")
_Umc1SystemSysProvACOConfig_Type = Integer32
_Umc1SystemSysProvACOConfig_Object = MibScalar
umc1SystemSysProvACOConfig = _Umc1SystemSysProvACOConfig_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 8),
    _Umc1SystemSysProvACOConfig_Type()
)
umc1SystemSysProvACOConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvACOConfig.setStatus("mandatory")


class _Umc1SystemSysTimingSource_Type(OctetString):
    """Custom type umc1SystemSysTimingSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemSysTimingSource_Type.__name__ = "OctetString"
_Umc1SystemSysTimingSource_Object = MibScalar
umc1SystemSysTimingSource = _Umc1SystemSysTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 9),
    _Umc1SystemSysTimingSource_Type()
)
umc1SystemSysTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysTimingSource.setStatus("mandatory")
_Umc1SystemSysTemperature_Type = Integer32
_Umc1SystemSysTemperature_Object = MibScalar
umc1SystemSysTemperature = _Umc1SystemSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 10),
    _Umc1SystemSysTemperature_Type()
)
umc1SystemSysTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysTemperature.setStatus("mandatory")
_Umc1SystemSysProvCATable_Object = MibTable
umc1SystemSysProvCATable = _Umc1SystemSysProvCATable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    umc1SystemSysProvCATable.setStatus("mandatory")
_Umc1SystemSysProvCAEntry_Object = MibTableRow
umc1SystemSysProvCAEntry = _Umc1SystemSysProvCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 11, 1)
)
umc1SystemSysProvCAEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemSysProvCAIndex"),
)
if mibBuilder.loadTexts:
    umc1SystemSysProvCAEntry.setStatus("mandatory")


class _Umc1SystemSysProvCAIndex_Type(OctetString):
    """Custom type umc1SystemSysProvCAIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemSysProvCAIndex_Type.__name__ = "OctetString"
_Umc1SystemSysProvCAIndex_Object = MibTableColumn
umc1SystemSysProvCAIndex = _Umc1SystemSysProvCAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 11, 1, 1),
    _Umc1SystemSysProvCAIndex_Type()
)
umc1SystemSysProvCAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemSysProvCAIndex.setStatus("mandatory")


class _Umc1SystemSysProvCAData_Type(OctetString):
    """Custom type umc1SystemSysProvCAData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemSysProvCAData_Type.__name__ = "OctetString"
_Umc1SystemSysProvCAData_Object = MibTableColumn
umc1SystemSysProvCAData = _Umc1SystemSysProvCAData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 2, 11, 1, 2),
    _Umc1SystemSysProvCAData_Type()
)
umc1SystemSysProvCAData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemSysProvCAData.setStatus("mandatory")
_Umc1SystemPitProv_ObjectIdentity = ObjectIdentity
umc1SystemPitProv = _Umc1SystemPitProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3)
)
_Umc1SystemPitProvTable_Object = MibTable
umc1SystemPitProvTable = _Umc1SystemPitProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    umc1SystemPitProvTable.setStatus("mandatory")
_Umc1SystemPitProvEntry_Object = MibTableRow
umc1SystemPitProvEntry = _Umc1SystemPitProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1)
)
umc1SystemPitProvEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemPitProvTerminalId"),
    (0, "UMC1000-MIB", "umc1SystemPitProvShelfId"),
    (0, "UMC1000-MIB", "umc1SystemPitProvSlotId"),
    (0, "UMC1000-MIB", "umc1SystemPitProvPit"),
)
if mibBuilder.loadTexts:
    umc1SystemPitProvEntry.setStatus("mandatory")
_Umc1SystemPitProvTerminalId_Type = TerminalIdType
_Umc1SystemPitProvTerminalId_Object = MibTableColumn
umc1SystemPitProvTerminalId = _Umc1SystemPitProvTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1, 1),
    _Umc1SystemPitProvTerminalId_Type()
)
umc1SystemPitProvTerminalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemPitProvTerminalId.setStatus("mandatory")
_Umc1SystemPitProvShelfId_Type = ShelfIdType
_Umc1SystemPitProvShelfId_Object = MibTableColumn
umc1SystemPitProvShelfId = _Umc1SystemPitProvShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1, 2),
    _Umc1SystemPitProvShelfId_Type()
)
umc1SystemPitProvShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemPitProvShelfId.setStatus("mandatory")
_Umc1SystemPitProvSlotId_Type = SlotIdType
_Umc1SystemPitProvSlotId_Object = MibTableColumn
umc1SystemPitProvSlotId = _Umc1SystemPitProvSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1, 3),
    _Umc1SystemPitProvSlotId_Type()
)
umc1SystemPitProvSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemPitProvSlotId.setStatus("mandatory")
_Umc1SystemPitProvPit_Type = PlugInType
_Umc1SystemPitProvPit_Object = MibTableColumn
umc1SystemPitProvPit = _Umc1SystemPitProvPit_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1, 4),
    _Umc1SystemPitProvPit_Type()
)
umc1SystemPitProvPit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemPitProvPit.setStatus("mandatory")


class _Umc1SystemPitProvData_Type(OctetString):
    """Custom type umc1SystemPitProvData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemPitProvData_Type.__name__ = "OctetString"
_Umc1SystemPitProvData_Object = MibTableColumn
umc1SystemPitProvData = _Umc1SystemPitProvData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 1, 1, 5),
    _Umc1SystemPitProvData_Type()
)
umc1SystemPitProvData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemPitProvData.setStatus("mandatory")
_Umc1SystemDefPitProvTable_Object = MibTable
umc1SystemDefPitProvTable = _Umc1SystemDefPitProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    umc1SystemDefPitProvTable.setStatus("mandatory")
_Umc1SystemDefPitProvEntry_Object = MibTableRow
umc1SystemDefPitProvEntry = _Umc1SystemDefPitProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1)
)
umc1SystemDefPitProvEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemDefPitProvTerminalId"),
    (0, "UMC1000-MIB", "umc1SystemDefPitProvShelfId"),
    (0, "UMC1000-MIB", "umc1SystemDefPitProvSlotId"),
    (0, "UMC1000-MIB", "umc1SystemDefPitProvPit"),
)
if mibBuilder.loadTexts:
    umc1SystemDefPitProvEntry.setStatus("mandatory")
_Umc1SystemDefPitProvTerminalId_Type = TerminalIdType
_Umc1SystemDefPitProvTerminalId_Object = MibTableColumn
umc1SystemDefPitProvTerminalId = _Umc1SystemDefPitProvTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1, 1),
    _Umc1SystemDefPitProvTerminalId_Type()
)
umc1SystemDefPitProvTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemDefPitProvTerminalId.setStatus("mandatory")
_Umc1SystemDefPitProvShelfId_Type = ShelfIdType
_Umc1SystemDefPitProvShelfId_Object = MibTableColumn
umc1SystemDefPitProvShelfId = _Umc1SystemDefPitProvShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1, 2),
    _Umc1SystemDefPitProvShelfId_Type()
)
umc1SystemDefPitProvShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemDefPitProvShelfId.setStatus("mandatory")
_Umc1SystemDefPitProvSlotId_Type = SlotIdType
_Umc1SystemDefPitProvSlotId_Object = MibTableColumn
umc1SystemDefPitProvSlotId = _Umc1SystemDefPitProvSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1, 3),
    _Umc1SystemDefPitProvSlotId_Type()
)
umc1SystemDefPitProvSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemDefPitProvSlotId.setStatus("mandatory")
_Umc1SystemDefPitProvPit_Type = PlugInType
_Umc1SystemDefPitProvPit_Object = MibTableColumn
umc1SystemDefPitProvPit = _Umc1SystemDefPitProvPit_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1, 4),
    _Umc1SystemDefPitProvPit_Type()
)
umc1SystemDefPitProvPit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemDefPitProvPit.setStatus("mandatory")


class _Umc1SystemDefPitProvData_Type(OctetString):
    """Custom type umc1SystemDefPitProvData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemDefPitProvData_Type.__name__ = "OctetString"
_Umc1SystemDefPitProvData_Object = MibTableColumn
umc1SystemDefPitProvData = _Umc1SystemDefPitProvData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 2, 1, 5),
    _Umc1SystemDefPitProvData_Type()
)
umc1SystemDefPitProvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemDefPitProvData.setStatus("mandatory")
_Umc1SystemPitProvChgTable_Object = MibTable
umc1SystemPitProvChgTable = _Umc1SystemPitProvChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    umc1SystemPitProvChgTable.setStatus("mandatory")
_Umc1SystemPitProvChgEntry_Object = MibTableRow
umc1SystemPitProvChgEntry = _Umc1SystemPitProvChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 3, 1)
)
umc1SystemPitProvChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemPitProvChgSeqNbr"),
)
if mibBuilder.loadTexts:
    umc1SystemPitProvChgEntry.setStatus("mandatory")
_Umc1SystemPitProvChgSeqNbr_Type = Integer32
_Umc1SystemPitProvChgSeqNbr_Object = MibTableColumn
umc1SystemPitProvChgSeqNbr = _Umc1SystemPitProvChgSeqNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 3, 1, 1),
    _Umc1SystemPitProvChgSeqNbr_Type()
)
umc1SystemPitProvChgSeqNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemPitProvChgSeqNbr.setStatus("mandatory")


class _Umc1SystemPitProvChgData_Type(OctetString):
    """Custom type umc1SystemPitProvChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 255),
    )


_Umc1SystemPitProvChgData_Type.__name__ = "OctetString"
_Umc1SystemPitProvChgData_Object = MibTableColumn
umc1SystemPitProvChgData = _Umc1SystemPitProvChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 3, 1, 2),
    _Umc1SystemPitProvChgData_Type()
)
umc1SystemPitProvChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemPitProvChgData.setStatus("mandatory")


class _Umc1SystemPitProvTableChangeSeqNum_Type(Integer32):
    """Custom type umc1SystemPitProvTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemPitProvTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1SystemPitProvTableChangeSeqNum_Object = MibScalar
umc1SystemPitProvTableChangeSeqNum = _Umc1SystemPitProvTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 4),
    _Umc1SystemPitProvTableChangeSeqNum_Type()
)
umc1SystemPitProvTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemPitProvTableChangeSeqNum.setStatus("mandatory")


class _Umc1FacAlmStringTableChangeSeqNum_Type(Integer32):
    """Custom type umc1FacAlmStringTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1FacAlmStringTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1FacAlmStringTableChangeSeqNum_Object = MibScalar
umc1FacAlmStringTableChangeSeqNum = _Umc1FacAlmStringTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 5),
    _Umc1FacAlmStringTableChangeSeqNum_Type()
)
umc1FacAlmStringTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1FacAlmStringTableChangeSeqNum.setStatus("mandatory")
_Umc1FacAlmStringTable_Object = MibTable
umc1FacAlmStringTable = _Umc1FacAlmStringTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    umc1FacAlmStringTable.setStatus("mandatory")
_Umc1FacAlmStringEntry_Object = MibTableRow
umc1FacAlmStringEntry = _Umc1FacAlmStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1)
)
umc1FacAlmStringEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1FacAlmStringTerminalId"),
    (0, "UMC1000-MIB", "umc1FacAlmStringShelfId"),
    (0, "UMC1000-MIB", "umc1FacAlmStringSlotId"),
    (0, "UMC1000-MIB", "umc1FacAlmStringFacilityId"),
    (0, "UMC1000-MIB", "umc1FacAlmStringPluginType"),
)
if mibBuilder.loadTexts:
    umc1FacAlmStringEntry.setStatus("mandatory")
_Umc1FacAlmStringTerminalId_Type = TerminalIdType
_Umc1FacAlmStringTerminalId_Object = MibTableColumn
umc1FacAlmStringTerminalId = _Umc1FacAlmStringTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 1),
    _Umc1FacAlmStringTerminalId_Type()
)
umc1FacAlmStringTerminalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringTerminalId.setStatus("mandatory")
_Umc1FacAlmStringShelfId_Type = ShelfIdType
_Umc1FacAlmStringShelfId_Object = MibTableColumn
umc1FacAlmStringShelfId = _Umc1FacAlmStringShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 2),
    _Umc1FacAlmStringShelfId_Type()
)
umc1FacAlmStringShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringShelfId.setStatus("mandatory")
_Umc1FacAlmStringSlotId_Type = SlotIdType
_Umc1FacAlmStringSlotId_Object = MibTableColumn
umc1FacAlmStringSlotId = _Umc1FacAlmStringSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 3),
    _Umc1FacAlmStringSlotId_Type()
)
umc1FacAlmStringSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringSlotId.setStatus("mandatory")
_Umc1FacAlmStringFacilityId_Type = Integer32
_Umc1FacAlmStringFacilityId_Object = MibTableColumn
umc1FacAlmStringFacilityId = _Umc1FacAlmStringFacilityId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 4),
    _Umc1FacAlmStringFacilityId_Type()
)
umc1FacAlmStringFacilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringFacilityId.setStatus("mandatory")
_Umc1FacAlmStringPluginType_Type = PlugInType
_Umc1FacAlmStringPluginType_Object = MibTableColumn
umc1FacAlmStringPluginType = _Umc1FacAlmStringPluginType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 5),
    _Umc1FacAlmStringPluginType_Type()
)
umc1FacAlmStringPluginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringPluginType.setStatus("mandatory")


class _Umc1FacAlmStringData_Type(DisplayString):
    """Custom type umc1FacAlmStringData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1FacAlmStringData_Type.__name__ = "DisplayString"
_Umc1FacAlmStringData_Object = MibTableColumn
umc1FacAlmStringData = _Umc1FacAlmStringData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 6, 1, 6),
    _Umc1FacAlmStringData_Type()
)
umc1FacAlmStringData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1FacAlmStringData.setStatus("mandatory")
_Umc1FacAlmStringChgTable_Object = MibTable
umc1FacAlmStringChgTable = _Umc1FacAlmStringChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    umc1FacAlmStringChgTable.setStatus("mandatory")
_Umc1FacAlmStringChgEntry_Object = MibTableRow
umc1FacAlmStringChgEntry = _Umc1FacAlmStringChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 7, 1)
)
umc1FacAlmStringChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1FacAlmStringChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1FacAlmStringChgEntry.setStatus("mandatory")
_Umc1FacAlmStringChgSeqNum_Type = Integer32
_Umc1FacAlmStringChgSeqNum_Object = MibTableColumn
umc1FacAlmStringChgSeqNum = _Umc1FacAlmStringChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 7, 1, 1),
    _Umc1FacAlmStringChgSeqNum_Type()
)
umc1FacAlmStringChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1FacAlmStringChgSeqNum.setStatus("mandatory")


class _Umc1FacAlmStringChgData_Type(OctetString):
    """Custom type umc1FacAlmStringChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1FacAlmStringChgData_Type.__name__ = "OctetString"
_Umc1FacAlmStringChgData_Object = MibTableColumn
umc1FacAlmStringChgData = _Umc1FacAlmStringChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 7, 1, 2),
    _Umc1FacAlmStringChgData_Type()
)
umc1FacAlmStringChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1FacAlmStringChgData.setStatus("mandatory")


class _Umc1TL1IfProvTableChangeSeqNum_Type(Integer32):
    """Custom type umc1TL1IfProvTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1TL1IfProvTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1TL1IfProvTableChangeSeqNum_Object = MibScalar
umc1TL1IfProvTableChangeSeqNum = _Umc1TL1IfProvTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 8),
    _Umc1TL1IfProvTableChangeSeqNum_Type()
)
umc1TL1IfProvTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TL1IfProvTableChangeSeqNum.setStatus("mandatory")
_Umc1TL1IfProvTable_Object = MibTable
umc1TL1IfProvTable = _Umc1TL1IfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    umc1TL1IfProvTable.setStatus("mandatory")
_Umc1TL1IfProvEntry_Object = MibTableRow
umc1TL1IfProvEntry = _Umc1TL1IfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1)
)
umc1TL1IfProvEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TL1IfProvTerminalId"),
    (0, "UMC1000-MIB", "umc1TL1IfProvShelfId"),
    (0, "UMC1000-MIB", "umc1TL1IfProvSlotId"),
    (0, "UMC1000-MIB", "umc1TL1IfProvInterfaceId"),
)
if mibBuilder.loadTexts:
    umc1TL1IfProvEntry.setStatus("mandatory")
_Umc1TL1IfProvTerminalId_Type = TerminalIdType
_Umc1TL1IfProvTerminalId_Object = MibTableColumn
umc1TL1IfProvTerminalId = _Umc1TL1IfProvTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 1),
    _Umc1TL1IfProvTerminalId_Type()
)
umc1TL1IfProvTerminalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvTerminalId.setStatus("mandatory")
_Umc1TL1IfProvShelfId_Type = ShelfIdType
_Umc1TL1IfProvShelfId_Object = MibTableColumn
umc1TL1IfProvShelfId = _Umc1TL1IfProvShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 2),
    _Umc1TL1IfProvShelfId_Type()
)
umc1TL1IfProvShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvShelfId.setStatus("mandatory")
_Umc1TL1IfProvSlotId_Type = SlotIdType
_Umc1TL1IfProvSlotId_Object = MibTableColumn
umc1TL1IfProvSlotId = _Umc1TL1IfProvSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 3),
    _Umc1TL1IfProvSlotId_Type()
)
umc1TL1IfProvSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvSlotId.setStatus("mandatory")
_Umc1TL1IfProvInterfaceId_Type = Integer32
_Umc1TL1IfProvInterfaceId_Object = MibTableColumn
umc1TL1IfProvInterfaceId = _Umc1TL1IfProvInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 4),
    _Umc1TL1IfProvInterfaceId_Type()
)
umc1TL1IfProvInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvInterfaceId.setStatus("mandatory")
_Umc1TL1IfProvPluginType_Type = PlugInType
_Umc1TL1IfProvPluginType_Object = MibTableColumn
umc1TL1IfProvPluginType = _Umc1TL1IfProvPluginType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 5),
    _Umc1TL1IfProvPluginType_Type()
)
umc1TL1IfProvPluginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvPluginType.setStatus("mandatory")


class _Umc1TL1IfProvData_Type(OctetString):
    """Custom type umc1TL1IfProvData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1TL1IfProvData_Type.__name__ = "OctetString"
_Umc1TL1IfProvData_Object = MibTableColumn
umc1TL1IfProvData = _Umc1TL1IfProvData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 9, 1, 6),
    _Umc1TL1IfProvData_Type()
)
umc1TL1IfProvData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TL1IfProvData.setStatus("mandatory")
_Umc1TL1IfProvChgTable_Object = MibTable
umc1TL1IfProvChgTable = _Umc1TL1IfProvChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 10)
)
if mibBuilder.loadTexts:
    umc1TL1IfProvChgTable.setStatus("mandatory")
_Umc1TL1IfProvChgEntry_Object = MibTableRow
umc1TL1IfProvChgEntry = _Umc1TL1IfProvChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 10, 1)
)
umc1TL1IfProvChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TL1IfProvChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1TL1IfProvChgEntry.setStatus("mandatory")
_Umc1TL1IfProvChgSeqNum_Type = Integer32
_Umc1TL1IfProvChgSeqNum_Object = MibTableColumn
umc1TL1IfProvChgSeqNum = _Umc1TL1IfProvChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 10, 1, 1),
    _Umc1TL1IfProvChgSeqNum_Type()
)
umc1TL1IfProvChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TL1IfProvChgSeqNum.setStatus("mandatory")


class _Umc1TL1IfProvChgData_Type(OctetString):
    """Custom type umc1TL1IfProvChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1TL1IfProvChgData_Type.__name__ = "OctetString"
_Umc1TL1IfProvChgData_Object = MibTableColumn
umc1TL1IfProvChgData = _Umc1TL1IfProvChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 3, 10, 1, 2),
    _Umc1TL1IfProvChgData_Type()
)
umc1TL1IfProvChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TL1IfProvChgData.setStatus("mandatory")


class _Umc1CpuSoftwareFeatures_Type(OctetString):
    """Custom type umc1CpuSoftwareFeatures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1CpuSoftwareFeatures_Type.__name__ = "OctetString"
_Umc1CpuSoftwareFeatures_Object = MibScalar
umc1CpuSoftwareFeatures = _Umc1CpuSoftwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 4),
    _Umc1CpuSoftwareFeatures_Type()
)
umc1CpuSoftwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CpuSoftwareFeatures.setStatus("mandatory")
_Umc1SystemRelearnTrapSeqNum_Type = Integer32
_Umc1SystemRelearnTrapSeqNum_Object = MibScalar
umc1SystemRelearnTrapSeqNum = _Umc1SystemRelearnTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 5),
    _Umc1SystemRelearnTrapSeqNum_Type()
)
umc1SystemRelearnTrapSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemRelearnTrapSeqNum.setStatus("mandatory")


class _Umc1RestrictedAccess_Type(Integer32):
    """Custom type umc1RestrictedAccess based on Integer32"""
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


_Umc1RestrictedAccess_Type.__name__ = "Integer32"
_Umc1RestrictedAccess_Object = MibScalar
umc1RestrictedAccess = _Umc1RestrictedAccess_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 6),
    _Umc1RestrictedAccess_Type()
)
umc1RestrictedAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1RestrictedAccess.setStatus("mandatory")
_Umc1Service_ObjectIdentity = ObjectIdentity
umc1Service = _Umc1Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7)
)
_Umc1GR303Grp_ObjectIdentity = ObjectIdentity
umc1GR303Grp = _Umc1GR303Grp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1)
)


class _Umc1GR303TableChangeSeqNum_Type(Integer32):
    """Custom type umc1GR303TableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1GR303TableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1GR303TableChangeSeqNum_Object = MibScalar
umc1GR303TableChangeSeqNum = _Umc1GR303TableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1, 1),
    _Umc1GR303TableChangeSeqNum_Type()
)
umc1GR303TableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1GR303TableChangeSeqNum.setStatus("mandatory")
_Umc1GR303Table_Object = MibTable
umc1GR303Table = _Umc1GR303Table_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    umc1GR303Table.setStatus("mandatory")
_Umc1GR303Entry_Object = MibTableRow
umc1GR303Entry = _Umc1GR303Entry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1, 2, 1)
)
umc1GR303Entry.setIndexNames(
    (0, "UMC1000-MIB", "umc1Gr303Index"),
)
if mibBuilder.loadTexts:
    umc1GR303Entry.setStatus("mandatory")


class _Umc1Gr303Index_Type(OctetString):
    """Custom type umc1Gr303Index based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1Gr303Index_Type.__name__ = "OctetString"
_Umc1Gr303Index_Object = MibTableColumn
umc1Gr303Index = _Umc1Gr303Index_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1, 2, 1, 1),
    _Umc1Gr303Index_Type()
)
umc1Gr303Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1Gr303Index.setStatus("mandatory")


class _Umc1Gr303Data_Type(OctetString):
    """Custom type umc1Gr303Data based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1Gr303Data_Type.__name__ = "OctetString"
_Umc1Gr303Data_Object = MibTableColumn
umc1Gr303Data = _Umc1Gr303Data_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 1, 2, 1, 2),
    _Umc1Gr303Data_Type()
)
umc1Gr303Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1Gr303Data.setStatus("mandatory")
_Umc1GR303ChgTable_Object = MibTable
umc1GR303ChgTable = _Umc1GR303ChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    umc1GR303ChgTable.setStatus("mandatory")
_Umc1GR303ChgEntry_Object = MibTableRow
umc1GR303ChgEntry = _Umc1GR303ChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 2, 1)
)
umc1GR303ChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1GR303ChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1GR303ChgEntry.setStatus("mandatory")
_Umc1GR303ChgSeqNum_Type = Integer32
_Umc1GR303ChgSeqNum_Object = MibTableColumn
umc1GR303ChgSeqNum = _Umc1GR303ChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 2, 1, 1),
    _Umc1GR303ChgSeqNum_Type()
)
umc1GR303ChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1GR303ChgSeqNum.setStatus("mandatory")


class _Umc1GR303ChgData_Type(OctetString):
    """Custom type umc1GR303ChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1GR303ChgData_Type.__name__ = "OctetString"
_Umc1GR303ChgData_Object = MibTableColumn
umc1GR303ChgData = _Umc1GR303ChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 2, 1, 2),
    _Umc1GR303ChgData_Type()
)
umc1GR303ChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1GR303ChgData.setStatus("mandatory")
_Umc1TR8Grp_ObjectIdentity = ObjectIdentity
umc1TR8Grp = _Umc1TR8Grp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3)
)


class _Umc1TR8TableChangeSeqNum_Type(Integer32):
    """Custom type umc1TR8TableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1TR8TableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1TR8TableChangeSeqNum_Object = MibScalar
umc1TR8TableChangeSeqNum = _Umc1TR8TableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3, 1),
    _Umc1TR8TableChangeSeqNum_Type()
)
umc1TR8TableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TR8TableChangeSeqNum.setStatus("mandatory")
_Umc1TR8Table_Object = MibTable
umc1TR8Table = _Umc1TR8Table_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    umc1TR8Table.setStatus("mandatory")
_Umc1TR8Entry_Object = MibTableRow
umc1TR8Entry = _Umc1TR8Entry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3, 2, 1)
)
umc1TR8Entry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TR8Index"),
)
if mibBuilder.loadTexts:
    umc1TR8Entry.setStatus("mandatory")


class _Umc1TR8Index_Type(OctetString):
    """Custom type umc1TR8Index based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1TR8Index_Type.__name__ = "OctetString"
_Umc1TR8Index_Object = MibTableColumn
umc1TR8Index = _Umc1TR8Index_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3, 2, 1, 1),
    _Umc1TR8Index_Type()
)
umc1TR8Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TR8Index.setStatus("mandatory")


class _Umc1TR8Data_Type(OctetString):
    """Custom type umc1TR8Data based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1TR8Data_Type.__name__ = "OctetString"
_Umc1TR8Data_Object = MibTableColumn
umc1TR8Data = _Umc1TR8Data_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 3, 2, 1, 2),
    _Umc1TR8Data_Type()
)
umc1TR8Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TR8Data.setStatus("mandatory")
_Umc1TR8ChgTable_Object = MibTable
umc1TR8ChgTable = _Umc1TR8ChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    umc1TR8ChgTable.setStatus("mandatory")
_Umc1TR8ChgEntry_Object = MibTableRow
umc1TR8ChgEntry = _Umc1TR8ChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 4, 1)
)
umc1TR8ChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TR8ChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1TR8ChgEntry.setStatus("mandatory")
_Umc1TR8ChgSeqNum_Type = Integer32
_Umc1TR8ChgSeqNum_Object = MibTableColumn
umc1TR8ChgSeqNum = _Umc1TR8ChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 4, 1, 1),
    _Umc1TR8ChgSeqNum_Type()
)
umc1TR8ChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TR8ChgSeqNum.setStatus("mandatory")


class _Umc1TR8ChgData_Type(OctetString):
    """Custom type umc1TR8ChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1TR8ChgData_Type.__name__ = "OctetString"
_Umc1TR8ChgData_Object = MibTableColumn
umc1TR8ChgData = _Umc1TR8ChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 4, 1, 2),
    _Umc1TR8ChgData_Type()
)
umc1TR8ChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TR8ChgData.setStatus("mandatory")
_Umc1V5Grp_ObjectIdentity = ObjectIdentity
umc1V5Grp = _Umc1V5Grp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5)
)


class _Umc1V5TableChangeSeqNum_Type(Integer32):
    """Custom type umc1V5TableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1V5TableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1V5TableChangeSeqNum_Object = MibScalar
umc1V5TableChangeSeqNum = _Umc1V5TableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5, 1),
    _Umc1V5TableChangeSeqNum_Type()
)
umc1V5TableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1V5TableChangeSeqNum.setStatus("mandatory")
_Umc1V5Table_Object = MibTable
umc1V5Table = _Umc1V5Table_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5, 2)
)
if mibBuilder.loadTexts:
    umc1V5Table.setStatus("mandatory")
_Umc1V5Entry_Object = MibTableRow
umc1V5Entry = _Umc1V5Entry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5, 2, 1)
)
umc1V5Entry.setIndexNames(
    (0, "UMC1000-MIB", "umc1V5Index"),
)
if mibBuilder.loadTexts:
    umc1V5Entry.setStatus("mandatory")


class _Umc1V5Index_Type(OctetString):
    """Custom type umc1V5Index based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_Umc1V5Index_Type.__name__ = "OctetString"
_Umc1V5Index_Object = MibTableColumn
umc1V5Index = _Umc1V5Index_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5, 2, 1, 1),
    _Umc1V5Index_Type()
)
umc1V5Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1V5Index.setStatus("mandatory")


class _Umc1V5Data_Type(OctetString):
    """Custom type umc1V5Data based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1V5Data_Type.__name__ = "OctetString"
_Umc1V5Data_Object = MibTableColumn
umc1V5Data = _Umc1V5Data_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 5, 2, 1, 2),
    _Umc1V5Data_Type()
)
umc1V5Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1V5Data.setStatus("mandatory")
_Umc1V5ChgTable_Object = MibTable
umc1V5ChgTable = _Umc1V5ChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    umc1V5ChgTable.setStatus("mandatory")
_Umc1V5ChgEntry_Object = MibTableRow
umc1V5ChgEntry = _Umc1V5ChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 6, 1)
)
umc1V5ChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1V5ChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1V5ChgEntry.setStatus("mandatory")
_Umc1V5ChgSeqNum_Type = Integer32
_Umc1V5ChgSeqNum_Object = MibTableColumn
umc1V5ChgSeqNum = _Umc1V5ChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 6, 1, 1),
    _Umc1V5ChgSeqNum_Type()
)
umc1V5ChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1V5ChgSeqNum.setStatus("mandatory")


class _Umc1V5ChgData_Type(OctetString):
    """Custom type umc1V5ChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1V5ChgData_Type.__name__ = "OctetString"
_Umc1V5ChgData_Object = MibTableColumn
umc1V5ChgData = _Umc1V5ChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 7, 6, 1, 2),
    _Umc1V5ChgData_Type()
)
umc1V5ChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1V5ChgData.setStatus("mandatory")
_Umc1XConnect_ObjectIdentity = ObjectIdentity
umc1XConnect = _Umc1XConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8)
)


class _Umc1XCTableChangeSeqNum_Type(Integer32):
    """Custom type umc1XCTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1XCTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1XCTableChangeSeqNum_Object = MibScalar
umc1XCTableChangeSeqNum = _Umc1XCTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 1),
    _Umc1XCTableChangeSeqNum_Type()
)
umc1XCTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1XCTableChangeSeqNum.setStatus("mandatory")
_Umc1XCTable_Object = MibTable
umc1XCTable = _Umc1XCTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    umc1XCTable.setStatus("mandatory")
_Umc1XCEntry_Object = MibTableRow
umc1XCEntry = _Umc1XCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 2, 1)
)
umc1XCEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1XCIndex"),
)
if mibBuilder.loadTexts:
    umc1XCEntry.setStatus("mandatory")


class _Umc1XCIndex_Type(OctetString):
    """Custom type umc1XCIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1XCIndex_Type.__name__ = "OctetString"
_Umc1XCIndex_Object = MibTableColumn
umc1XCIndex = _Umc1XCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 2, 1, 1),
    _Umc1XCIndex_Type()
)
umc1XCIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1XCIndex.setStatus("mandatory")


class _Umc1XCData_Type(OctetString):
    """Custom type umc1XCData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1XCData_Type.__name__ = "OctetString"
_Umc1XCData_Object = MibTableColumn
umc1XCData = _Umc1XCData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 2, 1, 2),
    _Umc1XCData_Type()
)
umc1XCData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1XCData.setStatus("mandatory")
_Umc1XCChgTable_Object = MibTable
umc1XCChgTable = _Umc1XCChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    umc1XCChgTable.setStatus("mandatory")
_Umc1XCChgEntry_Object = MibTableRow
umc1XCChgEntry = _Umc1XCChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 3, 1)
)
umc1XCChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1XCChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1XCChgEntry.setStatus("mandatory")
_Umc1XCChgSeqNum_Type = Integer32
_Umc1XCChgSeqNum_Object = MibTableColumn
umc1XCChgSeqNum = _Umc1XCChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 3, 1, 1),
    _Umc1XCChgSeqNum_Type()
)
umc1XCChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1XCChgSeqNum.setStatus("mandatory")


class _Umc1XCChgData_Type(OctetString):
    """Custom type umc1XCChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1XCChgData_Type.__name__ = "OctetString"
_Umc1XCChgData_Object = MibTableColumn
umc1XCChgData = _Umc1XCChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 8, 3, 1, 2),
    _Umc1XCChgData_Type()
)
umc1XCChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1XCChgData.setStatus("mandatory")


class _Umc1SystemAllSeqNbr_Type(OctetString):
    """Custom type umc1SystemAllSeqNbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemAllSeqNbr_Type.__name__ = "OctetString"
_Umc1SystemAllSeqNbr_Object = MibScalar
umc1SystemAllSeqNbr = _Umc1SystemAllSeqNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 9),
    _Umc1SystemAllSeqNbr_Type()
)
umc1SystemAllSeqNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemAllSeqNbr.setStatus("mandatory")


class _Umc1AtmProtTableChangeSeqNum_Type(Integer32):
    """Custom type umc1AtmProtTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1AtmProtTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1AtmProtTableChangeSeqNum_Object = MibScalar
umc1AtmProtTableChangeSeqNum = _Umc1AtmProtTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 10),
    _Umc1AtmProtTableChangeSeqNum_Type()
)
umc1AtmProtTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AtmProtTableChangeSeqNum.setStatus("mandatory")
_Umc1AtmProtGrpTable_Object = MibTable
umc1AtmProtGrpTable = _Umc1AtmProtGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    umc1AtmProtGrpTable.setStatus("mandatory")
_Umc1AtmProtGrpEntry_Object = MibTableRow
umc1AtmProtGrpEntry = _Umc1AtmProtGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 11, 1)
)
umc1AtmProtGrpEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1AtmProtGrpIndex"),
)
if mibBuilder.loadTexts:
    umc1AtmProtGrpEntry.setStatus("mandatory")


class _Umc1AtmProtGrpIndex_Type(OctetString):
    """Custom type umc1AtmProtGrpIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1AtmProtGrpIndex_Type.__name__ = "OctetString"
_Umc1AtmProtGrpIndex_Object = MibTableColumn
umc1AtmProtGrpIndex = _Umc1AtmProtGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 11, 1, 1),
    _Umc1AtmProtGrpIndex_Type()
)
umc1AtmProtGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1AtmProtGrpIndex.setStatus("mandatory")


class _Umc1AtmProtGrpData_Type(OctetString):
    """Custom type umc1AtmProtGrpData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1AtmProtGrpData_Type.__name__ = "OctetString"
_Umc1AtmProtGrpData_Object = MibTableColumn
umc1AtmProtGrpData = _Umc1AtmProtGrpData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 11, 1, 2),
    _Umc1AtmProtGrpData_Type()
)
umc1AtmProtGrpData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1AtmProtGrpData.setStatus("mandatory")
_Umc1AtmProtGrpChgTable_Object = MibTable
umc1AtmProtGrpChgTable = _Umc1AtmProtGrpChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    umc1AtmProtGrpChgTable.setStatus("mandatory")
_Umc1AtmProtGrpChgEntry_Object = MibTableRow
umc1AtmProtGrpChgEntry = _Umc1AtmProtGrpChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 12, 1)
)
umc1AtmProtGrpChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1AtmProtGrpChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1AtmProtGrpChgEntry.setStatus("mandatory")
_Umc1AtmProtGrpChgSeqNum_Type = Integer32
_Umc1AtmProtGrpChgSeqNum_Object = MibTableColumn
umc1AtmProtGrpChgSeqNum = _Umc1AtmProtGrpChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 12, 1, 1),
    _Umc1AtmProtGrpChgSeqNum_Type()
)
umc1AtmProtGrpChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AtmProtGrpChgSeqNum.setStatus("mandatory")


class _Umc1AtmProtGrpChgData_Type(OctetString):
    """Custom type umc1AtmProtGrpChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1AtmProtGrpChgData_Type.__name__ = "OctetString"
_Umc1AtmProtGrpChgData_Object = MibTableColumn
umc1AtmProtGrpChgData = _Umc1AtmProtGrpChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 12, 1, 2),
    _Umc1AtmProtGrpChgData_Type()
)
umc1AtmProtGrpChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AtmProtGrpChgData.setStatus("mandatory")


class _Umc1PortProfTableChangeSeqNum_Type(Integer32):
    """Custom type umc1PortProfTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1PortProfTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1PortProfTableChangeSeqNum_Object = MibScalar
umc1PortProfTableChangeSeqNum = _Umc1PortProfTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 13),
    _Umc1PortProfTableChangeSeqNum_Type()
)
umc1PortProfTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1PortProfTableChangeSeqNum.setStatus("mandatory")
_Umc1PortProfTable_Object = MibTable
umc1PortProfTable = _Umc1PortProfTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 14)
)
if mibBuilder.loadTexts:
    umc1PortProfTable.setStatus("mandatory")
_Umc1PortProfEntry_Object = MibTableRow
umc1PortProfEntry = _Umc1PortProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 14, 1)
)
umc1PortProfEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1PortProfIndex"),
)
if mibBuilder.loadTexts:
    umc1PortProfEntry.setStatus("mandatory")


class _Umc1PortProfIndex_Type(OctetString):
    """Custom type umc1PortProfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1PortProfIndex_Type.__name__ = "OctetString"
_Umc1PortProfIndex_Object = MibTableColumn
umc1PortProfIndex = _Umc1PortProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 14, 1, 1),
    _Umc1PortProfIndex_Type()
)
umc1PortProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1PortProfIndex.setStatus("mandatory")


class _Umc1PortProfData_Type(OctetString):
    """Custom type umc1PortProfData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1PortProfData_Type.__name__ = "OctetString"
_Umc1PortProfData_Object = MibTableColumn
umc1PortProfData = _Umc1PortProfData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 14, 1, 2),
    _Umc1PortProfData_Type()
)
umc1PortProfData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1PortProfData.setStatus("mandatory")
_Umc1PortProfChgTable_Object = MibTable
umc1PortProfChgTable = _Umc1PortProfChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    umc1PortProfChgTable.setStatus("mandatory")
_Umc1PortProfChgEntry_Object = MibTableRow
umc1PortProfChgEntry = _Umc1PortProfChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 15, 1)
)
umc1PortProfChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1PortProfChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1PortProfChgEntry.setStatus("mandatory")
_Umc1PortProfChgSeqNum_Type = Integer32
_Umc1PortProfChgSeqNum_Object = MibTableColumn
umc1PortProfChgSeqNum = _Umc1PortProfChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 15, 1, 1),
    _Umc1PortProfChgSeqNum_Type()
)
umc1PortProfChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1PortProfChgSeqNum.setStatus("mandatory")


class _Umc1PortProfChgData_Type(OctetString):
    """Custom type umc1PortProfChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1PortProfChgData_Type.__name__ = "OctetString"
_Umc1PortProfChgData_Object = MibTableColumn
umc1PortProfChgData = _Umc1PortProfChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 15, 1, 2),
    _Umc1PortProfChgData_Type()
)
umc1PortProfChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1PortProfChgData.setStatus("mandatory")


class _Umc1MyAgentSoftwareFeatures_Type(OctetString):
    """Custom type umc1MyAgentSoftwareFeatures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1MyAgentSoftwareFeatures_Type.__name__ = "OctetString"
_Umc1MyAgentSoftwareFeatures_Object = MibScalar
umc1MyAgentSoftwareFeatures = _Umc1MyAgentSoftwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 16),
    _Umc1MyAgentSoftwareFeatures_Type()
)
umc1MyAgentSoftwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1MyAgentSoftwareFeatures.setStatus("mandatory")
_Umc1Security_ObjectIdentity = ObjectIdentity
umc1Security = _Umc1Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17)
)


class _Umc1SecurityDataTableChangeSeqNum_Type(Integer32):
    """Custom type umc1SecurityDataTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SecurityDataTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1SecurityDataTableChangeSeqNum_Object = MibScalar
umc1SecurityDataTableChangeSeqNum = _Umc1SecurityDataTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 1),
    _Umc1SecurityDataTableChangeSeqNum_Type()
)
umc1SecurityDataTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SecurityDataTableChangeSeqNum.setStatus("mandatory")
_Umc1SecurityDataTable_Object = MibTable
umc1SecurityDataTable = _Umc1SecurityDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 2)
)
if mibBuilder.loadTexts:
    umc1SecurityDataTable.setStatus("mandatory")
_Umc1SecurityDataEntry_Object = MibTableRow
umc1SecurityDataEntry = _Umc1SecurityDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 2, 1)
)
umc1SecurityDataEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SecurityDataTableIndex"),
)
if mibBuilder.loadTexts:
    umc1SecurityDataEntry.setStatus("mandatory")


class _Umc1SecurityDataTableIndex_Type(OctetString):
    """Custom type umc1SecurityDataTableIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SecurityDataTableIndex_Type.__name__ = "OctetString"
_Umc1SecurityDataTableIndex_Object = MibTableColumn
umc1SecurityDataTableIndex = _Umc1SecurityDataTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 2, 1, 1),
    _Umc1SecurityDataTableIndex_Type()
)
umc1SecurityDataTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SecurityDataTableIndex.setStatus("mandatory")


class _Umc1SecurityDataTableData_Type(OctetString):
    """Custom type umc1SecurityDataTableData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1SecurityDataTableData_Type.__name__ = "OctetString"
_Umc1SecurityDataTableData_Object = MibTableColumn
umc1SecurityDataTableData = _Umc1SecurityDataTableData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 2, 1, 2),
    _Umc1SecurityDataTableData_Type()
)
umc1SecurityDataTableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SecurityDataTableData.setStatus("mandatory")
_Umc1SecurityDataChgTable_Object = MibTable
umc1SecurityDataChgTable = _Umc1SecurityDataChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 3)
)
if mibBuilder.loadTexts:
    umc1SecurityDataChgTable.setStatus("mandatory")
_Umc1SecurityDataChgEntry_Object = MibTableRow
umc1SecurityDataChgEntry = _Umc1SecurityDataChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 3, 1)
)
umc1SecurityDataChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SecurityDataChgSeqNum"),
)
if mibBuilder.loadTexts:
    umc1SecurityDataChgEntry.setStatus("mandatory")
_Umc1SecurityDataChgSeqNum_Type = Integer32
_Umc1SecurityDataChgSeqNum_Object = MibTableColumn
umc1SecurityDataChgSeqNum = _Umc1SecurityDataChgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 3, 1, 1),
    _Umc1SecurityDataChgSeqNum_Type()
)
umc1SecurityDataChgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SecurityDataChgSeqNum.setStatus("mandatory")


class _Umc1SecurityDataChgData_Type(OctetString):
    """Custom type umc1SecurityDataChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SecurityDataChgData_Type.__name__ = "OctetString"
_Umc1SecurityDataChgData_Object = MibTableColumn
umc1SecurityDataChgData = _Umc1SecurityDataChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 17, 3, 1, 2),
    _Umc1SecurityDataChgData_Type()
)
umc1SecurityDataChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SecurityDataChgData.setStatus("mandatory")
_Umc1SystemGenericDbProv_ObjectIdentity = ObjectIdentity
umc1SystemGenericDbProv = _Umc1SystemGenericDbProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18)
)


class _Umc1SystemGenericDbProvTableSeqNum_Type(Integer32):
    """Custom type umc1SystemGenericDbProvTableSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemGenericDbProvTableSeqNum_Type.__name__ = "Integer32"
_Umc1SystemGenericDbProvTableSeqNum_Object = MibScalar
umc1SystemGenericDbProvTableSeqNum = _Umc1SystemGenericDbProvTableSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 1),
    _Umc1SystemGenericDbProvTableSeqNum_Type()
)
umc1SystemGenericDbProvTableSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvTableSeqNum.setStatus("mandatory")
_Umc1SystemGenericDbProvTable_Object = MibTable
umc1SystemGenericDbProvTable = _Umc1SystemGenericDbProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvTable.setStatus("mandatory")
_Umc1SystemGenericDbProvEntry_Object = MibTableRow
umc1SystemGenericDbProvEntry = _Umc1SystemGenericDbProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 2, 1)
)
umc1SystemGenericDbProvEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemGenericDbProvIndex"),
)
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvEntry.setStatus("mandatory")


class _Umc1SystemGenericDbProvIndex_Type(OctetString):
    """Custom type umc1SystemGenericDbProvIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemGenericDbProvIndex_Type.__name__ = "OctetString"
_Umc1SystemGenericDbProvIndex_Object = MibTableColumn
umc1SystemGenericDbProvIndex = _Umc1SystemGenericDbProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 2, 1, 1),
    _Umc1SystemGenericDbProvIndex_Type()
)
umc1SystemGenericDbProvIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvIndex.setStatus("mandatory")


class _Umc1SystemGenericDbProvData_Type(OctetString):
    """Custom type umc1SystemGenericDbProvData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemGenericDbProvData_Type.__name__ = "OctetString"
_Umc1SystemGenericDbProvData_Object = MibTableColumn
umc1SystemGenericDbProvData = _Umc1SystemGenericDbProvData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 2, 1, 2),
    _Umc1SystemGenericDbProvData_Type()
)
umc1SystemGenericDbProvData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvData.setStatus("mandatory")
_Umc1SystemGenericDbProvChgTable_Object = MibTable
umc1SystemGenericDbProvChgTable = _Umc1SystemGenericDbProvChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 3)
)
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvChgTable.setStatus("mandatory")
_Umc1SystemGenericDbProvChgEntry_Object = MibTableRow
umc1SystemGenericDbProvChgEntry = _Umc1SystemGenericDbProvChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 3, 1)
)
umc1SystemGenericDbProvChgEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemGenericDbProvChgTableSeqNum"),
)
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvChgEntry.setStatus("mandatory")
_Umc1SystemGenericDbProvChgTableSeqNum_Type = Integer32
_Umc1SystemGenericDbProvChgTableSeqNum_Object = MibTableColumn
umc1SystemGenericDbProvChgTableSeqNum = _Umc1SystemGenericDbProvChgTableSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 3, 1, 1),
    _Umc1SystemGenericDbProvChgTableSeqNum_Type()
)
umc1SystemGenericDbProvChgTableSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvChgTableSeqNum.setStatus("mandatory")


class _Umc1SystemGenericDbProvChgData_Type(OctetString):
    """Custom type umc1SystemGenericDbProvChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemGenericDbProvChgData_Type.__name__ = "OctetString"
_Umc1SystemGenericDbProvChgData_Object = MibTableColumn
umc1SystemGenericDbProvChgData = _Umc1SystemGenericDbProvChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 18, 3, 1, 2),
    _Umc1SystemGenericDbProvChgData_Type()
)
umc1SystemGenericDbProvChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemGenericDbProvChgData.setStatus("mandatory")


class _Umc1MibVersion_Type(OctetString):
    """Custom type umc1MibVersion based on OctetString"""
    defaultHexValue = "01050003"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Umc1MibVersion_Type.__name__ = "OctetString"
_Umc1MibVersion_Object = MibScalar
umc1MibVersion = _Umc1MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 19),
    _Umc1MibVersion_Type()
)
umc1MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1MibVersion.setStatus("mandatory")


class _Umc1DbRecordChangeTrapHandleMask_Type(OctetString):
    """Custom type umc1DbRecordChangeTrapHandleMask based on OctetString"""
    defaultHexValue = "010100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Umc1DbRecordChangeTrapHandleMask_Type.__name__ = "OctetString"
_Umc1DbRecordChangeTrapHandleMask_Object = MibScalar
umc1DbRecordChangeTrapHandleMask = _Umc1DbRecordChangeTrapHandleMask_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 20),
    _Umc1DbRecordChangeTrapHandleMask_Type()
)
umc1DbRecordChangeTrapHandleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1DbRecordChangeTrapHandleMask.setStatus("mandatory")
_Umc1SystemAutonomousEvent_ObjectIdentity = ObjectIdentity
umc1SystemAutonomousEvent = _Umc1SystemAutonomousEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21)
)


class _Umc1SystemAutonomousEventSeqNum_Type(Integer32):
    """Custom type umc1SystemAutonomousEventSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemAutonomousEventSeqNum_Type.__name__ = "Integer32"
_Umc1SystemAutonomousEventSeqNum_Object = MibScalar
umc1SystemAutonomousEventSeqNum = _Umc1SystemAutonomousEventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21, 1),
    _Umc1SystemAutonomousEventSeqNum_Type()
)
umc1SystemAutonomousEventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemAutonomousEventSeqNum.setStatus("mandatory")
_Umc1SystemAutonomousEventTable_Object = MibTable
umc1SystemAutonomousEventTable = _Umc1SystemAutonomousEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    umc1SystemAutonomousEventTable.setStatus("mandatory")
_Umc1SystemAutonomousEventTableEntry_Object = MibTableRow
umc1SystemAutonomousEventTableEntry = _Umc1SystemAutonomousEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21, 2, 1)
)
umc1SystemAutonomousEventTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemAutonomousEventTableSeqNum"),
)
if mibBuilder.loadTexts:
    umc1SystemAutonomousEventTableEntry.setStatus("mandatory")
_Umc1SystemAutonomousEventTableSeqNum_Type = Integer32
_Umc1SystemAutonomousEventTableSeqNum_Object = MibTableColumn
umc1SystemAutonomousEventTableSeqNum = _Umc1SystemAutonomousEventTableSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21, 2, 1, 1),
    _Umc1SystemAutonomousEventTableSeqNum_Type()
)
umc1SystemAutonomousEventTableSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemAutonomousEventTableSeqNum.setStatus("mandatory")


class _Umc1SystemAutonomousEventTableData_Type(OctetString):
    """Custom type umc1SystemAutonomousEventTableData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemAutonomousEventTableData_Type.__name__ = "OctetString"
_Umc1SystemAutonomousEventTableData_Object = MibTableColumn
umc1SystemAutonomousEventTableData = _Umc1SystemAutonomousEventTableData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 1, 21, 2, 1, 2),
    _Umc1SystemAutonomousEventTableData_Type()
)
umc1SystemAutonomousEventTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemAutonomousEventTableData.setStatus("mandatory")
_Umc1Inventory_ObjectIdentity = ObjectIdentity
umc1Inventory = _Umc1Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2)
)
_Umc1InventoryShelf_ObjectIdentity = ObjectIdentity
umc1InventoryShelf = _Umc1InventoryShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1)
)


class _Umc1InventoryShelfTableChangeSeqNum_Type(Integer32):
    """Custom type umc1InventoryShelfTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1InventoryShelfTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1InventoryShelfTableChangeSeqNum_Object = MibScalar
umc1InventoryShelfTableChangeSeqNum = _Umc1InventoryShelfTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 1),
    _Umc1InventoryShelfTableChangeSeqNum_Type()
)
umc1InventoryShelfTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfTableChangeSeqNum.setStatus("mandatory")
_Umc1InventoryShelfTable_Object = MibTable
umc1InventoryShelfTable = _Umc1InventoryShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    umc1InventoryShelfTable.setStatus("mandatory")
_Umc1InventoryShelfEntry_Object = MibTableRow
umc1InventoryShelfEntry = _Umc1InventoryShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 2, 1)
)
umc1InventoryShelfEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryShelfTerminalId"),
    (0, "UMC1000-MIB", "umc1InventoryShelfShelfId"),
)
if mibBuilder.loadTexts:
    umc1InventoryShelfEntry.setStatus("mandatory")
_Umc1InventoryShelfTerminalId_Type = TerminalIdType
_Umc1InventoryShelfTerminalId_Object = MibTableColumn
umc1InventoryShelfTerminalId = _Umc1InventoryShelfTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 2, 1, 1),
    _Umc1InventoryShelfTerminalId_Type()
)
umc1InventoryShelfTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfTerminalId.setStatus("mandatory")
_Umc1InventoryShelfShelfId_Type = ShelfIdType
_Umc1InventoryShelfShelfId_Object = MibTableColumn
umc1InventoryShelfShelfId = _Umc1InventoryShelfShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 2, 1, 2),
    _Umc1InventoryShelfShelfId_Type()
)
umc1InventoryShelfShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfShelfId.setStatus("mandatory")


class _Umc1InventoryShelfType_Type(OctetString):
    """Custom type umc1InventoryShelfType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Umc1InventoryShelfType_Type.__name__ = "OctetString"
_Umc1InventoryShelfType_Object = MibTableColumn
umc1InventoryShelfType = _Umc1InventoryShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 2, 1, 3),
    _Umc1InventoryShelfType_Type()
)
umc1InventoryShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfType.setStatus("mandatory")
_Umc1InventoryShelfTableChangeHistoryTable_Object = MibTable
umc1InventoryShelfTableChangeHistoryTable = _Umc1InventoryShelfTableChangeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    umc1InventoryShelfTableChangeHistoryTable.setStatus("mandatory")
_Umc1InventoryShelfTableChangeHistoryEntry_Object = MibTableRow
umc1InventoryShelfTableChangeHistoryEntry = _Umc1InventoryShelfTableChangeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 3, 1)
)
umc1InventoryShelfTableChangeHistoryEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryShelfTableChangeHistoryIndex"),
)
if mibBuilder.loadTexts:
    umc1InventoryShelfTableChangeHistoryEntry.setStatus("mandatory")
_Umc1InventoryShelfTableChangeHistoryIndex_Type = Integer32
_Umc1InventoryShelfTableChangeHistoryIndex_Object = MibTableColumn
umc1InventoryShelfTableChangeHistoryIndex = _Umc1InventoryShelfTableChangeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 3, 1, 1),
    _Umc1InventoryShelfTableChangeHistoryIndex_Type()
)
umc1InventoryShelfTableChangeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfTableChangeHistoryIndex.setStatus("mandatory")


class _Umc1InventoryShelfTableChangeHistoryData_Type(OctetString):
    """Custom type umc1InventoryShelfTableChangeHistoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1InventoryShelfTableChangeHistoryData_Type.__name__ = "OctetString"
_Umc1InventoryShelfTableChangeHistoryData_Object = MibTableColumn
umc1InventoryShelfTableChangeHistoryData = _Umc1InventoryShelfTableChangeHistoryData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 1, 3, 1, 2),
    _Umc1InventoryShelfTableChangeHistoryData_Type()
)
umc1InventoryShelfTableChangeHistoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfTableChangeHistoryData.setStatus("mandatory")
_Umc1InventoryShelfExtended_ObjectIdentity = ObjectIdentity
umc1InventoryShelfExtended = _Umc1InventoryShelfExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2)
)
_Umc1InventoryShelfExtendedTable_Object = MibTable
umc1InventoryShelfExtendedTable = _Umc1InventoryShelfExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedTable.setStatus("mandatory")
_Umc1InventoryShelfExtendedEntry_Object = MibTableRow
umc1InventoryShelfExtendedEntry = _Umc1InventoryShelfExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1)
)
umc1InventoryShelfExtendedEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryShelfExtendedTerminalId"),
    (0, "UMC1000-MIB", "umc1InventoryShelfExtendedShelfId"),
)
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedEntry.setStatus("mandatory")
_Umc1InventoryShelfExtendedTerminalId_Type = TerminalIdType
_Umc1InventoryShelfExtendedTerminalId_Object = MibTableColumn
umc1InventoryShelfExtendedTerminalId = _Umc1InventoryShelfExtendedTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 1),
    _Umc1InventoryShelfExtendedTerminalId_Type()
)
umc1InventoryShelfExtendedTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedTerminalId.setStatus("mandatory")
_Umc1InventoryShelfExtendedShelfId_Type = ShelfIdType
_Umc1InventoryShelfExtendedShelfId_Object = MibTableColumn
umc1InventoryShelfExtendedShelfId = _Umc1InventoryShelfExtendedShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 2),
    _Umc1InventoryShelfExtendedShelfId_Type()
)
umc1InventoryShelfExtendedShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedShelfId.setStatus("mandatory")


class _Umc1InventoryShelfExtendedVersion_Type(OctetString):
    """Custom type umc1InventoryShelfExtendedVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Umc1InventoryShelfExtendedVersion_Type.__name__ = "OctetString"
_Umc1InventoryShelfExtendedVersion_Object = MibTableColumn
umc1InventoryShelfExtendedVersion = _Umc1InventoryShelfExtendedVersion_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 3),
    _Umc1InventoryShelfExtendedVersion_Type()
)
umc1InventoryShelfExtendedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedVersion.setStatus("mandatory")


class _Umc1InventoryShelfExtendedAssemblyNumber_Type(DisplayString):
    """Custom type umc1InventoryShelfExtendedAssemblyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Umc1InventoryShelfExtendedAssemblyNumber_Type.__name__ = "DisplayString"
_Umc1InventoryShelfExtendedAssemblyNumber_Object = MibTableColumn
umc1InventoryShelfExtendedAssemblyNumber = _Umc1InventoryShelfExtendedAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 4),
    _Umc1InventoryShelfExtendedAssemblyNumber_Type()
)
umc1InventoryShelfExtendedAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedAssemblyNumber.setStatus("mandatory")


class _Umc1InventoryShelfExtendedSerialNumber_Type(DisplayString):
    """Custom type umc1InventoryShelfExtendedSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Umc1InventoryShelfExtendedSerialNumber_Type.__name__ = "DisplayString"
_Umc1InventoryShelfExtendedSerialNumber_Object = MibTableColumn
umc1InventoryShelfExtendedSerialNumber = _Umc1InventoryShelfExtendedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 5),
    _Umc1InventoryShelfExtendedSerialNumber_Type()
)
umc1InventoryShelfExtendedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedSerialNumber.setStatus("mandatory")


class _Umc1InventoryShelfExtendedCLEICode_Type(DisplayString):
    """Custom type umc1InventoryShelfExtendedCLEICode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Umc1InventoryShelfExtendedCLEICode_Type.__name__ = "DisplayString"
_Umc1InventoryShelfExtendedCLEICode_Object = MibTableColumn
umc1InventoryShelfExtendedCLEICode = _Umc1InventoryShelfExtendedCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 2, 1, 1, 6),
    _Umc1InventoryShelfExtendedCLEICode_Type()
)
umc1InventoryShelfExtendedCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryShelfExtendedCLEICode.setStatus("mandatory")
_Umc1InventoryPlugin_ObjectIdentity = ObjectIdentity
umc1InventoryPlugin = _Umc1InventoryPlugin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3)
)


class _Umc1InventoryPluginTableChangeSeqNum_Type(Integer32):
    """Custom type umc1InventoryPluginTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1InventoryPluginTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1InventoryPluginTableChangeSeqNum_Object = MibScalar
umc1InventoryPluginTableChangeSeqNum = _Umc1InventoryPluginTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 1),
    _Umc1InventoryPluginTableChangeSeqNum_Type()
)
umc1InventoryPluginTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginTableChangeSeqNum.setStatus("mandatory")
_Umc1InventoryPluginTable_Object = MibTable
umc1InventoryPluginTable = _Umc1InventoryPluginTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    umc1InventoryPluginTable.setStatus("mandatory")
_Umc1InventoryPluginEntry_Object = MibTableRow
umc1InventoryPluginEntry = _Umc1InventoryPluginEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2, 1)
)
umc1InventoryPluginEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryPluginTerminalId"),
    (0, "UMC1000-MIB", "umc1InventoryPluginShelfId"),
    (0, "UMC1000-MIB", "umc1InventoryPluginSlotId"),
)
if mibBuilder.loadTexts:
    umc1InventoryPluginEntry.setStatus("mandatory")
_Umc1InventoryPluginTerminalId_Type = TerminalIdType
_Umc1InventoryPluginTerminalId_Object = MibTableColumn
umc1InventoryPluginTerminalId = _Umc1InventoryPluginTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2, 1, 1),
    _Umc1InventoryPluginTerminalId_Type()
)
umc1InventoryPluginTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginTerminalId.setStatus("mandatory")
_Umc1InventoryPluginShelfId_Type = ShelfIdType
_Umc1InventoryPluginShelfId_Object = MibTableColumn
umc1InventoryPluginShelfId = _Umc1InventoryPluginShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2, 1, 2),
    _Umc1InventoryPluginShelfId_Type()
)
umc1InventoryPluginShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginShelfId.setStatus("mandatory")
_Umc1InventoryPluginSlotId_Type = SlotIdType
_Umc1InventoryPluginSlotId_Object = MibTableColumn
umc1InventoryPluginSlotId = _Umc1InventoryPluginSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2, 1, 3),
    _Umc1InventoryPluginSlotId_Type()
)
umc1InventoryPluginSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginSlotId.setStatus("mandatory")
_Umc1InventoryPluginType_Type = PlugInType
_Umc1InventoryPluginType_Object = MibTableColumn
umc1InventoryPluginType = _Umc1InventoryPluginType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 2, 1, 4),
    _Umc1InventoryPluginType_Type()
)
umc1InventoryPluginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginType.setStatus("mandatory")
_Umc1InventoryPluginTableChangeHistoryTable_Object = MibTable
umc1InventoryPluginTableChangeHistoryTable = _Umc1InventoryPluginTableChangeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    umc1InventoryPluginTableChangeHistoryTable.setStatus("mandatory")
_Umc1InventoryPluginTableChangeHistoryEntry_Object = MibTableRow
umc1InventoryPluginTableChangeHistoryEntry = _Umc1InventoryPluginTableChangeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 3, 1)
)
umc1InventoryPluginTableChangeHistoryEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryPluginTableChangeHistoryIndex"),
)
if mibBuilder.loadTexts:
    umc1InventoryPluginTableChangeHistoryEntry.setStatus("mandatory")
_Umc1InventoryPluginTableChangeHistoryIndex_Type = Integer32
_Umc1InventoryPluginTableChangeHistoryIndex_Object = MibTableColumn
umc1InventoryPluginTableChangeHistoryIndex = _Umc1InventoryPluginTableChangeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 3, 1, 1),
    _Umc1InventoryPluginTableChangeHistoryIndex_Type()
)
umc1InventoryPluginTableChangeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginTableChangeHistoryIndex.setStatus("mandatory")


class _Umc1InventoryPluginTableChangeHistoryData_Type(OctetString):
    """Custom type umc1InventoryPluginTableChangeHistoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1InventoryPluginTableChangeHistoryData_Type.__name__ = "OctetString"
_Umc1InventoryPluginTableChangeHistoryData_Object = MibTableColumn
umc1InventoryPluginTableChangeHistoryData = _Umc1InventoryPluginTableChangeHistoryData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 3, 3, 1, 2),
    _Umc1InventoryPluginTableChangeHistoryData_Type()
)
umc1InventoryPluginTableChangeHistoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginTableChangeHistoryData.setStatus("mandatory")
_Umc1InventoryPluginExtended_ObjectIdentity = ObjectIdentity
umc1InventoryPluginExtended = _Umc1InventoryPluginExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4)
)
_Umc1InventoryPluginExtendedTable_Object = MibTable
umc1InventoryPluginExtendedTable = _Umc1InventoryPluginExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedTable.setStatus("mandatory")
_Umc1InventoryPluginExtendedEntry_Object = MibTableRow
umc1InventoryPluginExtendedEntry = _Umc1InventoryPluginExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1)
)
umc1InventoryPluginExtendedEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1InventoryPluginExtendedTerminalId"),
    (0, "UMC1000-MIB", "umc1InventoryPluginExtendedShelfId"),
    (0, "UMC1000-MIB", "umc1InventoryPluginExtendedSlotId"),
)
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedEntry.setStatus("mandatory")
_Umc1InventoryPluginExtendedTerminalId_Type = TerminalIdType
_Umc1InventoryPluginExtendedTerminalId_Object = MibTableColumn
umc1InventoryPluginExtendedTerminalId = _Umc1InventoryPluginExtendedTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 1),
    _Umc1InventoryPluginExtendedTerminalId_Type()
)
umc1InventoryPluginExtendedTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedTerminalId.setStatus("mandatory")
_Umc1InventoryPluginExtendedShelfId_Type = ShelfIdType
_Umc1InventoryPluginExtendedShelfId_Object = MibTableColumn
umc1InventoryPluginExtendedShelfId = _Umc1InventoryPluginExtendedShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 2),
    _Umc1InventoryPluginExtendedShelfId_Type()
)
umc1InventoryPluginExtendedShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedShelfId.setStatus("mandatory")
_Umc1InventoryPluginExtendedSlotId_Type = SlotIdType
_Umc1InventoryPluginExtendedSlotId_Object = MibTableColumn
umc1InventoryPluginExtendedSlotId = _Umc1InventoryPluginExtendedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 3),
    _Umc1InventoryPluginExtendedSlotId_Type()
)
umc1InventoryPluginExtendedSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedSlotId.setStatus("mandatory")
_Umc1InventoryPluginExtendedStatus_Type = Integer32
_Umc1InventoryPluginExtendedStatus_Object = MibTableColumn
umc1InventoryPluginExtendedStatus = _Umc1InventoryPluginExtendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 4),
    _Umc1InventoryPluginExtendedStatus_Type()
)
umc1InventoryPluginExtendedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedStatus.setStatus("mandatory")


class _Umc1InventoryPluginExtendedVersion_Type(OctetString):
    """Custom type umc1InventoryPluginExtendedVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Umc1InventoryPluginExtendedVersion_Type.__name__ = "OctetString"
_Umc1InventoryPluginExtendedVersion_Object = MibTableColumn
umc1InventoryPluginExtendedVersion = _Umc1InventoryPluginExtendedVersion_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 5),
    _Umc1InventoryPluginExtendedVersion_Type()
)
umc1InventoryPluginExtendedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedVersion.setStatus("mandatory")


class _Umc1InventoryPluginExtendedAssemblyNumber_Type(DisplayString):
    """Custom type umc1InventoryPluginExtendedAssemblyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Umc1InventoryPluginExtendedAssemblyNumber_Type.__name__ = "DisplayString"
_Umc1InventoryPluginExtendedAssemblyNumber_Object = MibTableColumn
umc1InventoryPluginExtendedAssemblyNumber = _Umc1InventoryPluginExtendedAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 6),
    _Umc1InventoryPluginExtendedAssemblyNumber_Type()
)
umc1InventoryPluginExtendedAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedAssemblyNumber.setStatus("mandatory")


class _Umc1InventoryPluginExtendedSerialNumber_Type(DisplayString):
    """Custom type umc1InventoryPluginExtendedSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Umc1InventoryPluginExtendedSerialNumber_Type.__name__ = "DisplayString"
_Umc1InventoryPluginExtendedSerialNumber_Object = MibTableColumn
umc1InventoryPluginExtendedSerialNumber = _Umc1InventoryPluginExtendedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 7),
    _Umc1InventoryPluginExtendedSerialNumber_Type()
)
umc1InventoryPluginExtendedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedSerialNumber.setStatus("mandatory")


class _Umc1InventoryPluginExtendedCLEICode_Type(DisplayString):
    """Custom type umc1InventoryPluginExtendedCLEICode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Umc1InventoryPluginExtendedCLEICode_Type.__name__ = "DisplayString"
_Umc1InventoryPluginExtendedCLEICode_Object = MibTableColumn
umc1InventoryPluginExtendedCLEICode = _Umc1InventoryPluginExtendedCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 2, 4, 1, 1, 8),
    _Umc1InventoryPluginExtendedCLEICode_Type()
)
umc1InventoryPluginExtendedCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1InventoryPluginExtendedCLEICode.setStatus("mandatory")
_Umc1Terminal_ObjectIdentity = ObjectIdentity
umc1Terminal = _Umc1Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3)
)


class _Umc1TerminalStatusChangeSeqNum_Type(Integer32):
    """Custom type umc1TerminalStatusChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1TerminalStatusChangeSeqNum_Type.__name__ = "Integer32"
_Umc1TerminalStatusChangeSeqNum_Object = MibScalar
umc1TerminalStatusChangeSeqNum = _Umc1TerminalStatusChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 1),
    _Umc1TerminalStatusChangeSeqNum_Type()
)
umc1TerminalStatusChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalStatusChangeSeqNum.setStatus("mandatory")
_Umc1TerminalStatusTable_Object = MibTable
umc1TerminalStatusTable = _Umc1TerminalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    umc1TerminalStatusTable.setStatus("mandatory")
_Umc1TerminalStatusEntry_Object = MibTableRow
umc1TerminalStatusEntry = _Umc1TerminalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 2, 1)
)
umc1TerminalStatusEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TerminalStatusTerminalId"),
)
if mibBuilder.loadTexts:
    umc1TerminalStatusEntry.setStatus("mandatory")
_Umc1TerminalStatusTerminalId_Type = TerminalIdType
_Umc1TerminalStatusTerminalId_Object = MibTableColumn
umc1TerminalStatusTerminalId = _Umc1TerminalStatusTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 2, 1, 1),
    _Umc1TerminalStatusTerminalId_Type()
)
umc1TerminalStatusTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalStatusTerminalId.setStatus("mandatory")


class _Umc1TerminalStatusValue_Type(Integer32):
    """Custom type umc1TerminalStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("normal", 1),
          ("unreachable", 255))
    )


_Umc1TerminalStatusValue_Type.__name__ = "Integer32"
_Umc1TerminalStatusValue_Object = MibTableColumn
umc1TerminalStatusValue = _Umc1TerminalStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 2, 1, 2),
    _Umc1TerminalStatusValue_Type()
)
umc1TerminalStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalStatusValue.setStatus("mandatory")
_Umc1TerminalInfoChangeSeqNum_Type = Integer32
_Umc1TerminalInfoChangeSeqNum_Object = MibScalar
umc1TerminalInfoChangeSeqNum = _Umc1TerminalInfoChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 3),
    _Umc1TerminalInfoChangeSeqNum_Type()
)
umc1TerminalInfoChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalInfoChangeSeqNum.setStatus("mandatory")
_Umc1TerminalInfoTable_Object = MibTable
umc1TerminalInfoTable = _Umc1TerminalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    umc1TerminalInfoTable.setStatus("mandatory")
_Umc1TerminalInfoEntry_Object = MibTableRow
umc1TerminalInfoEntry = _Umc1TerminalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1)
)
umc1TerminalInfoEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TerminalInfoTerminalId"),
)
if mibBuilder.loadTexts:
    umc1TerminalInfoEntry.setStatus("mandatory")
_Umc1TerminalInfoTerminalId_Type = TerminalIdType
_Umc1TerminalInfoTerminalId_Object = MibTableColumn
umc1TerminalInfoTerminalId = _Umc1TerminalInfoTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1, 1),
    _Umc1TerminalInfoTerminalId_Type()
)
umc1TerminalInfoTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalInfoTerminalId.setStatus("mandatory")


class _Umc1TerminalInfoName_Type(DisplayString):
    """Custom type umc1TerminalInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Umc1TerminalInfoName_Type.__name__ = "DisplayString"
_Umc1TerminalInfoName_Object = MibTableColumn
umc1TerminalInfoName = _Umc1TerminalInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1, 2),
    _Umc1TerminalInfoName_Type()
)
umc1TerminalInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TerminalInfoName.setStatus("mandatory")


class _Umc1TerminalInfoSerialDeviceType_Type(Integer32):
    """Custom type umc1TerminalInfoSerialDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("modem", 1),
          ("other", 255))
    )


_Umc1TerminalInfoSerialDeviceType_Type.__name__ = "Integer32"
_Umc1TerminalInfoSerialDeviceType_Object = MibTableColumn
umc1TerminalInfoSerialDeviceType = _Umc1TerminalInfoSerialDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1, 3),
    _Umc1TerminalInfoSerialDeviceType_Type()
)
umc1TerminalInfoSerialDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TerminalInfoSerialDeviceType.setStatus("mandatory")


class _Umc1TerminalInfoBaudRate_Type(Integer32):
    """Custom type umc1TerminalInfoBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 1),
          ("baud1200", 2),
          ("baud2400", 3),
          ("baud9600", 4),
          ("other", 255))
    )


_Umc1TerminalInfoBaudRate_Type.__name__ = "Integer32"
_Umc1TerminalInfoBaudRate_Object = MibTableColumn
umc1TerminalInfoBaudRate = _Umc1TerminalInfoBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1, 4),
    _Umc1TerminalInfoBaudRate_Type()
)
umc1TerminalInfoBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TerminalInfoBaudRate.setStatus("mandatory")
_Umc1TerminalInfoNewTerminalId_Type = TerminalIdType
_Umc1TerminalInfoNewTerminalId_Object = MibTableColumn
umc1TerminalInfoNewTerminalId = _Umc1TerminalInfoNewTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 3, 4, 1, 5),
    _Umc1TerminalInfoNewTerminalId_Type()
)
umc1TerminalInfoNewTerminalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1TerminalInfoNewTerminalId.setStatus("mandatory")
_Umc1ACOSnapTopology_ObjectIdentity = ObjectIdentity
umc1ACOSnapTopology = _Umc1ACOSnapTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4)
)


class _Umc1ACOSnapTopologySeqNum_Type(Integer32):
    """Custom type umc1ACOSnapTopologySeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1ACOSnapTopologySeqNum_Type.__name__ = "Integer32"
_Umc1ACOSnapTopologySeqNum_Object = MibScalar
umc1ACOSnapTopologySeqNum = _Umc1ACOSnapTopologySeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4, 1),
    _Umc1ACOSnapTopologySeqNum_Type()
)
umc1ACOSnapTopologySeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ACOSnapTopologySeqNum.setStatus("mandatory")
_Umc1ACOSnapTopologyLinkTable_Object = MibTable
umc1ACOSnapTopologyLinkTable = _Umc1ACOSnapTopologyLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    umc1ACOSnapTopologyLinkTable.setStatus("mandatory")
_Umc1ACOSnapTopologyLinkEntry_Object = MibTableRow
umc1ACOSnapTopologyLinkEntry = _Umc1ACOSnapTopologyLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4, 2, 1)
)
umc1ACOSnapTopologyLinkEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1ACOSnapTopologyLinkTerminalA"),
    (0, "UMC1000-MIB", "umc1ACOSnapTopologyLinkTerminalB"),
)
if mibBuilder.loadTexts:
    umc1ACOSnapTopologyLinkEntry.setStatus("mandatory")
_Umc1ACOSnapTopologyLinkTerminalA_Type = TerminalIdType
_Umc1ACOSnapTopologyLinkTerminalA_Object = MibTableColumn
umc1ACOSnapTopologyLinkTerminalA = _Umc1ACOSnapTopologyLinkTerminalA_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4, 2, 1, 1),
    _Umc1ACOSnapTopologyLinkTerminalA_Type()
)
umc1ACOSnapTopologyLinkTerminalA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ACOSnapTopologyLinkTerminalA.setStatus("mandatory")
_Umc1ACOSnapTopologyLinkTerminalB_Type = TerminalIdType
_Umc1ACOSnapTopologyLinkTerminalB_Object = MibTableColumn
umc1ACOSnapTopologyLinkTerminalB = _Umc1ACOSnapTopologyLinkTerminalB_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 4, 2, 1, 2),
    _Umc1ACOSnapTopologyLinkTerminalB_Type()
)
umc1ACOSnapTopologyLinkTerminalB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ACOSnapTopologyLinkTerminalB.setStatus("mandatory")
_Umc1CommandResponse_ObjectIdentity = ObjectIdentity
umc1CommandResponse = _Umc1CommandResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5)
)
_Umc1CommandTable_Object = MibTable
umc1CommandTable = _Umc1CommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    umc1CommandTable.setStatus("mandatory")
_Umc1CommandTableEntry_Object = MibTableRow
umc1CommandTableEntry = _Umc1CommandTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 1, 1)
)
umc1CommandTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1CommandId"),
    (0, "UMC1000-MIB", "umc1CommandArg"),
)
if mibBuilder.loadTexts:
    umc1CommandTableEntry.setStatus("mandatory")
_Umc1CommandId_Type = Integer32
_Umc1CommandId_Object = MibTableColumn
umc1CommandId = _Umc1CommandId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 1, 1, 1),
    _Umc1CommandId_Type()
)
umc1CommandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CommandId.setStatus("mandatory")


class _Umc1CommandArg_Type(OctetString):
    """Custom type umc1CommandArg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1CommandArg_Type.__name__ = "OctetString"
_Umc1CommandArg_Object = MibTableColumn
umc1CommandArg = _Umc1CommandArg_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 1, 1, 2),
    _Umc1CommandArg_Type()
)
umc1CommandArg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CommandArg.setStatus("mandatory")
_Umc1CommandTransNbr_Type = Integer32
_Umc1CommandTransNbr_Object = MibTableColumn
umc1CommandTransNbr = _Umc1CommandTransNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 1, 1, 3),
    _Umc1CommandTransNbr_Type()
)
umc1CommandTransNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CommandTransNbr.setStatus("mandatory")
_Umc1ResponseTable_Object = MibTable
umc1ResponseTable = _Umc1ResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    umc1ResponseTable.setStatus("mandatory")
_Umc1ResponseTableEntry_Object = MibTableRow
umc1ResponseTableEntry = _Umc1ResponseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 2, 1)
)
umc1ResponseTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1ResponseTransNbr"),
    (0, "UMC1000-MIB", "umc1ResponseSeqNbr"),
)
if mibBuilder.loadTexts:
    umc1ResponseTableEntry.setStatus("mandatory")
_Umc1ResponseTransNbr_Type = Integer32
_Umc1ResponseTransNbr_Object = MibTableColumn
umc1ResponseTransNbr = _Umc1ResponseTransNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 2, 1, 1),
    _Umc1ResponseTransNbr_Type()
)
umc1ResponseTransNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ResponseTransNbr.setStatus("mandatory")
_Umc1ResponseSeqNbr_Type = Integer32
_Umc1ResponseSeqNbr_Object = MibTableColumn
umc1ResponseSeqNbr = _Umc1ResponseSeqNbr_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 2, 1, 2),
    _Umc1ResponseSeqNbr_Type()
)
umc1ResponseSeqNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ResponseSeqNbr.setStatus("mandatory")


class _Umc1ResponseData_Type(OctetString):
    """Custom type umc1ResponseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1ResponseData_Type.__name__ = "OctetString"
_Umc1ResponseData_Object = MibTableColumn
umc1ResponseData = _Umc1ResponseData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 5, 2, 1, 3),
    _Umc1ResponseData_Type()
)
umc1ResponseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ResponseData.setStatus("mandatory")
_Umc1Span_ObjectIdentity = ObjectIdentity
umc1Span = _Umc1Span_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6)
)


class _Umc1TerminalSpanTableChangeSeqNum_Type(Integer32):
    """Custom type umc1TerminalSpanTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1TerminalSpanTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1TerminalSpanTableChangeSeqNum_Object = MibScalar
umc1TerminalSpanTableChangeSeqNum = _Umc1TerminalSpanTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 1),
    _Umc1TerminalSpanTableChangeSeqNum_Type()
)
umc1TerminalSpanTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalSpanTableChangeSeqNum.setStatus("mandatory")
_Umc1TerminalSpanTable_Object = MibTable
umc1TerminalSpanTable = _Umc1TerminalSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    umc1TerminalSpanTable.setStatus("mandatory")
_Umc1TerminalSpanTableEntry_Object = MibTableRow
umc1TerminalSpanTableEntry = _Umc1TerminalSpanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1)
)
umc1TerminalSpanTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TermSpanNearEndTerminalId"),
    (0, "UMC1000-MIB", "umc1TermSpanNearEndShelfId"),
    (0, "UMC1000-MIB", "umc1TermSpanNearEndSlotId"),
)
if mibBuilder.loadTexts:
    umc1TerminalSpanTableEntry.setStatus("mandatory")
_Umc1TermSpanNearEndTerminalId_Type = TerminalIdType
_Umc1TermSpanNearEndTerminalId_Object = MibTableColumn
umc1TermSpanNearEndTerminalId = _Umc1TermSpanNearEndTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 1),
    _Umc1TermSpanNearEndTerminalId_Type()
)
umc1TermSpanNearEndTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanNearEndTerminalId.setStatus("mandatory")
_Umc1TermSpanNearEndShelfId_Type = ShelfIdType
_Umc1TermSpanNearEndShelfId_Object = MibTableColumn
umc1TermSpanNearEndShelfId = _Umc1TermSpanNearEndShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 2),
    _Umc1TermSpanNearEndShelfId_Type()
)
umc1TermSpanNearEndShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanNearEndShelfId.setStatus("mandatory")
_Umc1TermSpanNearEndSlotId_Type = SlotIdType
_Umc1TermSpanNearEndSlotId_Object = MibTableColumn
umc1TermSpanNearEndSlotId = _Umc1TermSpanNearEndSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 3),
    _Umc1TermSpanNearEndSlotId_Type()
)
umc1TermSpanNearEndSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanNearEndSlotId.setStatus("mandatory")
_Umc1TermSpanNearEndPitType_Type = PlugInType
_Umc1TermSpanNearEndPitType_Object = MibTableColumn
umc1TermSpanNearEndPitType = _Umc1TermSpanNearEndPitType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 4),
    _Umc1TermSpanNearEndPitType_Type()
)
umc1TermSpanNearEndPitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanNearEndPitType.setStatus("mandatory")
_Umc1TermSpanFarEndTerminalId_Type = TerminalIdType
_Umc1TermSpanFarEndTerminalId_Object = MibTableColumn
umc1TermSpanFarEndTerminalId = _Umc1TermSpanFarEndTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 5),
    _Umc1TermSpanFarEndTerminalId_Type()
)
umc1TermSpanFarEndTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanFarEndTerminalId.setStatus("mandatory")
_Umc1TermSpanFarEndShelfId_Type = ShelfIdType
_Umc1TermSpanFarEndShelfId_Object = MibTableColumn
umc1TermSpanFarEndShelfId = _Umc1TermSpanFarEndShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 6),
    _Umc1TermSpanFarEndShelfId_Type()
)
umc1TermSpanFarEndShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanFarEndShelfId.setStatus("mandatory")
_Umc1TermSpanFarEndSlotId_Type = SlotIdType
_Umc1TermSpanFarEndSlotId_Object = MibTableColumn
umc1TermSpanFarEndSlotId = _Umc1TermSpanFarEndSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 2, 1, 7),
    _Umc1TermSpanFarEndSlotId_Type()
)
umc1TermSpanFarEndSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TermSpanFarEndSlotId.setStatus("mandatory")
_Umc1TerminalSpanTableChangeHistoryTable_Object = MibTable
umc1TerminalSpanTableChangeHistoryTable = _Umc1TerminalSpanTableChangeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    umc1TerminalSpanTableChangeHistoryTable.setStatus("mandatory")
_Umc1TerminalSpanTableChangeHistoryEntry_Object = MibTableRow
umc1TerminalSpanTableChangeHistoryEntry = _Umc1TerminalSpanTableChangeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 3, 1)
)
umc1TerminalSpanTableChangeHistoryEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TerminalSpanTableChangeHistoryIndex"),
)
if mibBuilder.loadTexts:
    umc1TerminalSpanTableChangeHistoryEntry.setStatus("mandatory")
_Umc1TerminalSpanTableChangeHistoryIndex_Type = Integer32
_Umc1TerminalSpanTableChangeHistoryIndex_Object = MibTableColumn
umc1TerminalSpanTableChangeHistoryIndex = _Umc1TerminalSpanTableChangeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 3, 1, 1),
    _Umc1TerminalSpanTableChangeHistoryIndex_Type()
)
umc1TerminalSpanTableChangeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalSpanTableChangeHistoryIndex.setStatus("mandatory")


class _Umc1TerminalSpanTableChangeHistoryData_Type(OctetString):
    """Custom type umc1TerminalSpanTableChangeHistoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1TerminalSpanTableChangeHistoryData_Type.__name__ = "OctetString"
_Umc1TerminalSpanTableChangeHistoryData_Object = MibTableColumn
umc1TerminalSpanTableChangeHistoryData = _Umc1TerminalSpanTableChangeHistoryData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 3, 1, 2),
    _Umc1TerminalSpanTableChangeHistoryData_Type()
)
umc1TerminalSpanTableChangeHistoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TerminalSpanTableChangeHistoryData.setStatus("mandatory")


class _Umc1ShelfSpanTableChangeSeqNum_Type(Integer32):
    """Custom type umc1ShelfSpanTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1ShelfSpanTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1ShelfSpanTableChangeSeqNum_Object = MibScalar
umc1ShelfSpanTableChangeSeqNum = _Umc1ShelfSpanTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 4),
    _Umc1ShelfSpanTableChangeSeqNum_Type()
)
umc1ShelfSpanTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanTableChangeSeqNum.setStatus("mandatory")
_Umc1ShelfSpanTable_Object = MibTable
umc1ShelfSpanTable = _Umc1ShelfSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    umc1ShelfSpanTable.setStatus("mandatory")
_Umc1ShelfSpanTableEntry_Object = MibTableRow
umc1ShelfSpanTableEntry = _Umc1ShelfSpanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1)
)
umc1ShelfSpanTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1ShelfSpanNearEndTerminalId"),
    (0, "UMC1000-MIB", "umc1ShelfSpanNearEndShelfId"),
    (0, "UMC1000-MIB", "umc1ShelfSpanNearEndSlotId"),
)
if mibBuilder.loadTexts:
    umc1ShelfSpanTableEntry.setStatus("mandatory")
_Umc1ShelfSpanNearEndTerminalId_Type = TerminalIdType
_Umc1ShelfSpanNearEndTerminalId_Object = MibTableColumn
umc1ShelfSpanNearEndTerminalId = _Umc1ShelfSpanNearEndTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 1),
    _Umc1ShelfSpanNearEndTerminalId_Type()
)
umc1ShelfSpanNearEndTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanNearEndTerminalId.setStatus("mandatory")
_Umc1ShelfSpanNearEndShelfId_Type = ShelfIdType
_Umc1ShelfSpanNearEndShelfId_Object = MibTableColumn
umc1ShelfSpanNearEndShelfId = _Umc1ShelfSpanNearEndShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 2),
    _Umc1ShelfSpanNearEndShelfId_Type()
)
umc1ShelfSpanNearEndShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanNearEndShelfId.setStatus("mandatory")
_Umc1ShelfSpanNearEndSlotId_Type = SlotIdType
_Umc1ShelfSpanNearEndSlotId_Object = MibTableColumn
umc1ShelfSpanNearEndSlotId = _Umc1ShelfSpanNearEndSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 3),
    _Umc1ShelfSpanNearEndSlotId_Type()
)
umc1ShelfSpanNearEndSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanNearEndSlotId.setStatus("mandatory")
_Umc1ShelfSpanNearEndPitType_Type = PlugInType
_Umc1ShelfSpanNearEndPitType_Object = MibTableColumn
umc1ShelfSpanNearEndPitType = _Umc1ShelfSpanNearEndPitType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 4),
    _Umc1ShelfSpanNearEndPitType_Type()
)
umc1ShelfSpanNearEndPitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanNearEndPitType.setStatus("mandatory")
_Umc1ShelfSpanFarEndShelfId_Type = ShelfIdType
_Umc1ShelfSpanFarEndShelfId_Object = MibTableColumn
umc1ShelfSpanFarEndShelfId = _Umc1ShelfSpanFarEndShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 5),
    _Umc1ShelfSpanFarEndShelfId_Type()
)
umc1ShelfSpanFarEndShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanFarEndShelfId.setStatus("mandatory")
_Umc1ShelfSpanFarEndSlotId_Type = SlotIdType
_Umc1ShelfSpanFarEndSlotId_Object = MibTableColumn
umc1ShelfSpanFarEndSlotId = _Umc1ShelfSpanFarEndSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 6),
    _Umc1ShelfSpanFarEndSlotId_Type()
)
umc1ShelfSpanFarEndSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanFarEndSlotId.setStatus("mandatory")
_Umc1ShelfSpanFarEndPitType_Type = PlugInType
_Umc1ShelfSpanFarEndPitType_Object = MibTableColumn
umc1ShelfSpanFarEndPitType = _Umc1ShelfSpanFarEndPitType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 5, 1, 7),
    _Umc1ShelfSpanFarEndPitType_Type()
)
umc1ShelfSpanFarEndPitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanFarEndPitType.setStatus("mandatory")
_Umc1ShelfSpanTableChangeHistoryTable_Object = MibTable
umc1ShelfSpanTableChangeHistoryTable = _Umc1ShelfSpanTableChangeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    umc1ShelfSpanTableChangeHistoryTable.setStatus("mandatory")
_Umc1ShelfSpanTableChangeHistoryEntry_Object = MibTableRow
umc1ShelfSpanTableChangeHistoryEntry = _Umc1ShelfSpanTableChangeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 6, 1)
)
umc1ShelfSpanTableChangeHistoryEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1ShelfSpanTableChangeHistoryIndex"),
)
if mibBuilder.loadTexts:
    umc1ShelfSpanTableChangeHistoryEntry.setStatus("mandatory")
_Umc1ShelfSpanTableChangeHistoryIndex_Type = Integer32
_Umc1ShelfSpanTableChangeHistoryIndex_Object = MibTableColumn
umc1ShelfSpanTableChangeHistoryIndex = _Umc1ShelfSpanTableChangeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 6, 1, 1),
    _Umc1ShelfSpanTableChangeHistoryIndex_Type()
)
umc1ShelfSpanTableChangeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanTableChangeHistoryIndex.setStatus("mandatory")


class _Umc1ShelfSpanTableChangeHistoryData_Type(OctetString):
    """Custom type umc1ShelfSpanTableChangeHistoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1ShelfSpanTableChangeHistoryData_Type.__name__ = "OctetString"
_Umc1ShelfSpanTableChangeHistoryData_Object = MibTableColumn
umc1ShelfSpanTableChangeHistoryData = _Umc1ShelfSpanTableChangeHistoryData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 6, 6, 1, 2),
    _Umc1ShelfSpanTableChangeHistoryData_Type()
)
umc1ShelfSpanTableChangeHistoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1ShelfSpanTableChangeHistoryData.setStatus("mandatory")
_Umc1Alarm_ObjectIdentity = ObjectIdentity
umc1Alarm = _Umc1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8)
)


class _Umc1AlmSeqTableChangeSeqNum_Type(Integer32):
    """Custom type umc1AlmSeqTableChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1AlmSeqTableChangeSeqNum_Type.__name__ = "Integer32"
_Umc1AlmSeqTableChangeSeqNum_Object = MibScalar
umc1AlmSeqTableChangeSeqNum = _Umc1AlmSeqTableChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 1),
    _Umc1AlmSeqTableChangeSeqNum_Type()
)
umc1AlmSeqTableChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AlmSeqTableChangeSeqNum.setStatus("mandatory")
_Umc1AlmSeqTable_Object = MibTable
umc1AlmSeqTable = _Umc1AlmSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    umc1AlmSeqTable.setStatus("mandatory")
_Umc1AlmSeqEntry_Object = MibTableRow
umc1AlmSeqEntry = _Umc1AlmSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 2, 1)
)
umc1AlmSeqEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1AlmSeqTerminalId"),
)
if mibBuilder.loadTexts:
    umc1AlmSeqEntry.setStatus("mandatory")
_Umc1AlmSeqTerminalId_Type = TerminalIdType
_Umc1AlmSeqTerminalId_Object = MibTableColumn
umc1AlmSeqTerminalId = _Umc1AlmSeqTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 2, 1, 1),
    _Umc1AlmSeqTerminalId_Type()
)
umc1AlmSeqTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AlmSeqTerminalId.setStatus("mandatory")
_Umc1AlmSeqNumber_Type = Integer32
_Umc1AlmSeqNumber_Object = MibTableColumn
umc1AlmSeqNumber = _Umc1AlmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 2, 1, 2),
    _Umc1AlmSeqNumber_Type()
)
umc1AlmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1AlmSeqNumber.setStatus("mandatory")
_Umc1CurAlmTable_Object = MibTable
umc1CurAlmTable = _Umc1CurAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    umc1CurAlmTable.setStatus("mandatory")
_Umc1CurAlmEntry_Object = MibTableRow
umc1CurAlmEntry = _Umc1CurAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3, 1)
)
umc1CurAlmEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1CurAlmTerminalId"),
    (0, "UMC1000-MIB", "umc1CurAlmOccurrenceIndex"),
)
if mibBuilder.loadTexts:
    umc1CurAlmEntry.setStatus("mandatory")
_Umc1CurAlmTerminalId_Type = TerminalIdType
_Umc1CurAlmTerminalId_Object = MibTableColumn
umc1CurAlmTerminalId = _Umc1CurAlmTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3, 1, 1),
    _Umc1CurAlmTerminalId_Type()
)
umc1CurAlmTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CurAlmTerminalId.setStatus("mandatory")


class _Umc1CurAlmOccurrenceIndex_Type(OctetString):
    """Custom type umc1CurAlmOccurrenceIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Umc1CurAlmOccurrenceIndex_Type.__name__ = "OctetString"
_Umc1CurAlmOccurrenceIndex_Object = MibTableColumn
umc1CurAlmOccurrenceIndex = _Umc1CurAlmOccurrenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3, 1, 2),
    _Umc1CurAlmOccurrenceIndex_Type()
)
umc1CurAlmOccurrenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CurAlmOccurrenceIndex.setStatus("mandatory")
_Umc1CurAlmTL1Message_Type = DisplayString
_Umc1CurAlmTL1Message_Object = MibTableColumn
umc1CurAlmTL1Message = _Umc1CurAlmTL1Message_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3, 1, 3),
    _Umc1CurAlmTL1Message_Type()
)
umc1CurAlmTL1Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CurAlmTL1Message.setStatus("mandatory")
_Umc1CurAlmDetails_Type = OctetString
_Umc1CurAlmDetails_Object = MibTableColumn
umc1CurAlmDetails = _Umc1CurAlmDetails_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 8, 3, 1, 4),
    _Umc1CurAlmDetails_Type()
)
umc1CurAlmDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1CurAlmDetails.setStatus("mandatory")
_Umc1ManagerIf_ObjectIdentity = ObjectIdentity
umc1ManagerIf = _Umc1ManagerIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9)
)
_Umc1Snmp_ObjectIdentity = ObjectIdentity
umc1Snmp = _Umc1Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1)
)


class _Umc1SnmpCommName_Type(DisplayString):
    """Custom type umc1SnmpCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Umc1SnmpCommName_Type.__name__ = "DisplayString"
_Umc1SnmpCommName_Object = MibScalar
umc1SnmpCommName = _Umc1SnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 1),
    _Umc1SnmpCommName_Type()
)
umc1SnmpCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpCommName.setStatus("mandatory")
_Umc1SnmpTrapTypesEnabled_Type = Integer32
_Umc1SnmpTrapTypesEnabled_Object = MibScalar
umc1SnmpTrapTypesEnabled = _Umc1SnmpTrapTypesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 3),
    _Umc1SnmpTrapTypesEnabled_Type()
)
umc1SnmpTrapTypesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpTrapTypesEnabled.setStatus("mandatory")
_Umc1SnmpTrapRcvrAddress_Type = IpAddress
_Umc1SnmpTrapRcvrAddress_Object = MibScalar
umc1SnmpTrapRcvrAddress = _Umc1SnmpTrapRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 4),
    _Umc1SnmpTrapRcvrAddress_Type()
)
umc1SnmpTrapRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpTrapRcvrAddress.setStatus("mandatory")
_Umc1SnmpTrapRcvrPort_Type = Integer32
_Umc1SnmpTrapRcvrPort_Object = MibScalar
umc1SnmpTrapRcvrPort = _Umc1SnmpTrapRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 5),
    _Umc1SnmpTrapRcvrPort_Type()
)
umc1SnmpTrapRcvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpTrapRcvrPort.setStatus("mandatory")
_Umc1SnmpMgmtHost2Address_Type = IpAddress
_Umc1SnmpMgmtHost2Address_Object = MibScalar
umc1SnmpMgmtHost2Address = _Umc1SnmpMgmtHost2Address_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 6),
    _Umc1SnmpMgmtHost2Address_Type()
)
umc1SnmpMgmtHost2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpMgmtHost2Address.setStatus("mandatory")
_Umc1SnmpMgmtHost2TrapsEnabled_Type = Integer32
_Umc1SnmpMgmtHost2TrapsEnabled_Object = MibScalar
umc1SnmpMgmtHost2TrapsEnabled = _Umc1SnmpMgmtHost2TrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 7),
    _Umc1SnmpMgmtHost2TrapsEnabled_Type()
)
umc1SnmpMgmtHost2TrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpMgmtHost2TrapsEnabled.setStatus("mandatory")
_Umc1SnmpMgmtHost3Address_Type = IpAddress
_Umc1SnmpMgmtHost3Address_Object = MibScalar
umc1SnmpMgmtHost3Address = _Umc1SnmpMgmtHost3Address_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 8),
    _Umc1SnmpMgmtHost3Address_Type()
)
umc1SnmpMgmtHost3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpMgmtHost3Address.setStatus("mandatory")
_Umc1SnmpMgmtHost3TrapsEnabled_Type = Integer32
_Umc1SnmpMgmtHost3TrapsEnabled_Object = MibScalar
umc1SnmpMgmtHost3TrapsEnabled = _Umc1SnmpMgmtHost3TrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 9),
    _Umc1SnmpMgmtHost3TrapsEnabled_Type()
)
umc1SnmpMgmtHost3TrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpMgmtHost3TrapsEnabled.setStatus("mandatory")
_Umc1SnmpTrustedHostsEnabled_Type = Integer32
_Umc1SnmpTrustedHostsEnabled_Object = MibScalar
umc1SnmpTrustedHostsEnabled = _Umc1SnmpTrustedHostsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 10),
    _Umc1SnmpTrustedHostsEnabled_Type()
)
umc1SnmpTrustedHostsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpTrustedHostsEnabled.setStatus("mandatory")
_Umc1SnmpTelnetPort_Type = Integer32
_Umc1SnmpTelnetPort_Object = MibScalar
umc1SnmpTelnetPort = _Umc1SnmpTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 9, 1, 11),
    _Umc1SnmpTelnetPort_Type()
)
umc1SnmpTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1SnmpTelnetPort.setStatus("mandatory")
_Umc1Topology_ObjectIdentity = ObjectIdentity
umc1Topology = _Umc1Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10)
)


class _Umc1TopologyChangeSeqNum_Type(Integer32):
    """Custom type umc1TopologyChangeSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1TopologyChangeSeqNum_Type.__name__ = "Integer32"
_Umc1TopologyChangeSeqNum_Object = MibScalar
umc1TopologyChangeSeqNum = _Umc1TopologyChangeSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 1),
    _Umc1TopologyChangeSeqNum_Type()
)
umc1TopologyChangeSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TopologyChangeSeqNum.setStatus("mandatory")
_Umc1TopologyThisTerminal_Type = Integer32
_Umc1TopologyThisTerminal_Object = MibScalar
umc1TopologyThisTerminal = _Umc1TopologyThisTerminal_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 2),
    _Umc1TopologyThisTerminal_Type()
)
umc1TopologyThisTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TopologyThisTerminal.setStatus("mandatory")
_Umc1TopologyLinkTable_Object = MibTable
umc1TopologyLinkTable = _Umc1TopologyLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    umc1TopologyLinkTable.setStatus("mandatory")
_Umc1TopologyLinkEntry_Object = MibTableRow
umc1TopologyLinkEntry = _Umc1TopologyLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 3, 1)
)
umc1TopologyLinkEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1TopologyLinkTerminalA"),
    (0, "UMC1000-MIB", "umc1TopologyLinkTerminalB"),
)
if mibBuilder.loadTexts:
    umc1TopologyLinkEntry.setStatus("mandatory")
_Umc1TopologyLinkTerminalA_Type = Integer32
_Umc1TopologyLinkTerminalA_Object = MibTableColumn
umc1TopologyLinkTerminalA = _Umc1TopologyLinkTerminalA_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 3, 1, 1),
    _Umc1TopologyLinkTerminalA_Type()
)
umc1TopologyLinkTerminalA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TopologyLinkTerminalA.setStatus("mandatory")
_Umc1TopologyLinkTerminalB_Type = Integer32
_Umc1TopologyLinkTerminalB_Object = MibTableColumn
umc1TopologyLinkTerminalB = _Umc1TopologyLinkTerminalB_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 10, 3, 1, 2),
    _Umc1TopologyLinkTerminalB_Type()
)
umc1TopologyLinkTerminalB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TopologyLinkTerminalB.setStatus("mandatory")
_Umc1DataService_ObjectIdentity = ObjectIdentity
umc1DataService = _Umc1DataService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11)
)
_Umc1DsPlugInNameTable_Object = MibTable
umc1DsPlugInNameTable = _Umc1DsPlugInNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    umc1DsPlugInNameTable.setStatus("mandatory")
_Umc1DsPlugInNameEntry_Object = MibTableRow
umc1DsPlugInNameEntry = _Umc1DsPlugInNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 1, 1)
)
umc1DsPlugInNameEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1DsPlugInType"),
)
if mibBuilder.loadTexts:
    umc1DsPlugInNameEntry.setStatus("mandatory")
_Umc1DsPlugInType_Type = Integer32
_Umc1DsPlugInType_Object = MibTableColumn
umc1DsPlugInType = _Umc1DsPlugInType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 1, 1, 1),
    _Umc1DsPlugInType_Type()
)
umc1DsPlugInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1DsPlugInType.setStatus("mandatory")
_Umc1DsPlugInName_Type = DisplayString
_Umc1DsPlugInName_Object = MibTableColumn
umc1DsPlugInName = _Umc1DsPlugInName_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 1, 1, 2),
    _Umc1DsPlugInName_Type()
)
umc1DsPlugInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1DsPlugInName.setStatus("mandatory")
_Umc1DsAlarmStringTable_Object = MibTable
umc1DsAlarmStringTable = _Umc1DsAlarmStringTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    umc1DsAlarmStringTable.setStatus("mandatory")
_Umc1DsAlarmStringEntry_Object = MibTableRow
umc1DsAlarmStringEntry = _Umc1DsAlarmStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 2, 1)
)
umc1DsAlarmStringEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1DsAlarmFacilityNumber"),
)
if mibBuilder.loadTexts:
    umc1DsAlarmStringEntry.setStatus("mandatory")
_Umc1DsAlarmFacilityNumber_Type = Integer32
_Umc1DsAlarmFacilityNumber_Object = MibTableColumn
umc1DsAlarmFacilityNumber = _Umc1DsAlarmFacilityNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 2, 1, 1),
    _Umc1DsAlarmFacilityNumber_Type()
)
umc1DsAlarmFacilityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1DsAlarmFacilityNumber.setStatus("mandatory")
_Umc1DsAlarmString_Type = DisplayString
_Umc1DsAlarmString_Object = MibTableColumn
umc1DsAlarmString = _Umc1DsAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 11, 2, 1, 2),
    _Umc1DsAlarmString_Type()
)
umc1DsAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1DsAlarmString.setStatus("mandatory")
_Umc1TriggerTrapAllSeqNumbers_Type = Integer32
_Umc1TriggerTrapAllSeqNumbers_Object = MibScalar
umc1TriggerTrapAllSeqNumbers = _Umc1TriggerTrapAllSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 12),
    _Umc1TriggerTrapAllSeqNumbers_Type()
)
umc1TriggerTrapAllSeqNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1TriggerTrapAllSeqNumbers.setStatus("mandatory")
_Umc1SystemTcaEvent_ObjectIdentity = ObjectIdentity
umc1SystemTcaEvent = _Umc1SystemTcaEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13)
)


class _Umc1SystemTCASeqNum_Type(Integer32):
    """Custom type umc1SystemTCASeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemTCASeqNum_Type.__name__ = "Integer32"
_Umc1SystemTCASeqNum_Object = MibScalar
umc1SystemTCASeqNum = _Umc1SystemTCASeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13, 1),
    _Umc1SystemTCASeqNum_Type()
)
umc1SystemTCASeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemTCASeqNum.setStatus("mandatory")
_Umc1SystemTCAHistoryTable_Object = MibTable
umc1SystemTCAHistoryTable = _Umc1SystemTCAHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    umc1SystemTCAHistoryTable.setStatus("mandatory")
_Umc1SystemTCAHistoryTableEntry_Object = MibTableRow
umc1SystemTCAHistoryTableEntry = _Umc1SystemTCAHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13, 2, 1)
)
umc1SystemTCAHistoryTableEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1SystemTCAHistoryTableSeqNum"),
)
if mibBuilder.loadTexts:
    umc1SystemTCAHistoryTableEntry.setStatus("mandatory")


class _Umc1SystemTCAHistoryTableSeqNum_Type(Integer32):
    """Custom type umc1SystemTCAHistoryTableSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1SystemTCAHistoryTableSeqNum_Type.__name__ = "Integer32"
_Umc1SystemTCAHistoryTableSeqNum_Object = MibTableColumn
umc1SystemTCAHistoryTableSeqNum = _Umc1SystemTCAHistoryTableSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13, 2, 1, 1),
    _Umc1SystemTCAHistoryTableSeqNum_Type()
)
umc1SystemTCAHistoryTableSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemTCAHistoryTableSeqNum.setStatus("mandatory")


class _Umc1SystemTCAHistoryTableChgData_Type(OctetString):
    """Custom type umc1SystemTCAHistoryTableChgData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Umc1SystemTCAHistoryTableChgData_Type.__name__ = "OctetString"
_Umc1SystemTCAHistoryTableChgData_Object = MibTableColumn
umc1SystemTCAHistoryTableChgData = _Umc1SystemTCAHistoryTableChgData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 13, 2, 1, 2),
    _Umc1SystemTCAHistoryTableChgData_Type()
)
umc1SystemTCAHistoryTableChgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SystemTCAHistoryTableChgData.setStatus("mandatory")
_Umc1F5Loopback_ObjectIdentity = ObjectIdentity
umc1F5Loopback = _Umc1F5Loopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17)
)
_Umc1F5LoopbackRequestTable_Object = MibTable
umc1F5LoopbackRequestTable = _Umc1F5LoopbackRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    umc1F5LoopbackRequestTable.setStatus("mandatory")
_Umc1F5LoopbackRequestEntry_Object = MibTableRow
umc1F5LoopbackRequestEntry = _Umc1F5LoopbackRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17, 1, 1)
)
umc1F5LoopbackRequestEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1F5LoopbackTransactionNumber"),
)
if mibBuilder.loadTexts:
    umc1F5LoopbackRequestEntry.setStatus("mandatory")


class _Umc1F5LoopbackTransactionNumber_Type(Integer32):
    """Custom type umc1F5LoopbackTransactionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1F5LoopbackTransactionNumber_Type.__name__ = "Integer32"
_Umc1F5LoopbackTransactionNumber_Object = MibTableColumn
umc1F5LoopbackTransactionNumber = _Umc1F5LoopbackTransactionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17, 1, 1, 1),
    _Umc1F5LoopbackTransactionNumber_Type()
)
umc1F5LoopbackTransactionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1F5LoopbackTransactionNumber.setStatus("mandatory")
_Umc1F5LoopbackTransactionIpAddress_Type = IpAddress
_Umc1F5LoopbackTransactionIpAddress_Object = MibTableColumn
umc1F5LoopbackTransactionIpAddress = _Umc1F5LoopbackTransactionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17, 1, 1, 2),
    _Umc1F5LoopbackTransactionIpAddress_Type()
)
umc1F5LoopbackTransactionIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1F5LoopbackTransactionIpAddress.setStatus("mandatory")


class _Umc1F5LoopbackTransactionIbMessage_Type(OctetString):
    """Custom type umc1F5LoopbackTransactionIbMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_Umc1F5LoopbackTransactionIbMessage_Type.__name__ = "OctetString"
_Umc1F5LoopbackTransactionIbMessage_Object = MibTableColumn
umc1F5LoopbackTransactionIbMessage = _Umc1F5LoopbackTransactionIbMessage_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 17, 1, 1, 3),
    _Umc1F5LoopbackTransactionIbMessage_Type()
)
umc1F5LoopbackTransactionIbMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1F5LoopbackTransactionIbMessage.setStatus("mandatory")
_Umc1LoopDiagnostics_ObjectIdentity = ObjectIdentity
umc1LoopDiagnostics = _Umc1LoopDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18)
)
_Umc1LoopDiagnosticsRequestTable_Object = MibTable
umc1LoopDiagnosticsRequestTable = _Umc1LoopDiagnosticsRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsRequestTable.setStatus("mandatory")
_Umc1LoopDiagnosticsRequestEntry_Object = MibTableRow
umc1LoopDiagnosticsRequestEntry = _Umc1LoopDiagnosticsRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 1, 1)
)
umc1LoopDiagnosticsRequestEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1LoopDiagnosticsRequestTransactionNumber"),
    (0, "UMC1000-MIB", "umc1LoopDiagnosticsRequestIpAddress"),
)
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsRequestEntry.setStatus("mandatory")


class _Umc1LoopDiagnosticsRequestTransactionNumber_Type(Integer32):
    """Custom type umc1LoopDiagnosticsRequestTransactionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1LoopDiagnosticsRequestTransactionNumber_Type.__name__ = "Integer32"
_Umc1LoopDiagnosticsRequestTransactionNumber_Object = MibTableColumn
umc1LoopDiagnosticsRequestTransactionNumber = _Umc1LoopDiagnosticsRequestTransactionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 1, 1, 1),
    _Umc1LoopDiagnosticsRequestTransactionNumber_Type()
)
umc1LoopDiagnosticsRequestTransactionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsRequestTransactionNumber.setStatus("mandatory")
_Umc1LoopDiagnosticsRequestIpAddress_Type = IpAddress
_Umc1LoopDiagnosticsRequestIpAddress_Object = MibTableColumn
umc1LoopDiagnosticsRequestIpAddress = _Umc1LoopDiagnosticsRequestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 1, 1, 2),
    _Umc1LoopDiagnosticsRequestIpAddress_Type()
)
umc1LoopDiagnosticsRequestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsRequestIpAddress.setStatus("mandatory")


class _Umc1LoopDiagnosticsRequestData_Type(OctetString):
    """Custom type umc1LoopDiagnosticsRequestData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Umc1LoopDiagnosticsRequestData_Type.__name__ = "OctetString"
_Umc1LoopDiagnosticsRequestData_Object = MibTableColumn
umc1LoopDiagnosticsRequestData = _Umc1LoopDiagnosticsRequestData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 1, 1, 3),
    _Umc1LoopDiagnosticsRequestData_Type()
)
umc1LoopDiagnosticsRequestData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsRequestData.setStatus("mandatory")
_Umc1LoopDiagnosticsResponseTable_Object = MibTable
umc1LoopDiagnosticsResponseTable = _Umc1LoopDiagnosticsResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseTable.setStatus("mandatory")
_Umc1LoopDiagnosticsResponseEntry_Object = MibTableRow
umc1LoopDiagnosticsResponseEntry = _Umc1LoopDiagnosticsResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1)
)
umc1LoopDiagnosticsResponseEntry.setIndexNames(
    (0, "UMC1000-MIB", "umc1LoopDiagnosticsResponseTransactionNumber"),
    (0, "UMC1000-MIB", "umc1LoopDiagnosticsResponseIpAddress"),
    (0, "UMC1000-MIB", "umc1LoopDiagnosticsResponseStartToneIdentifier"),
)
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseEntry.setStatus("mandatory")


class _Umc1LoopDiagnosticsResponseTransactionNumber_Type(Integer32):
    """Custom type umc1LoopDiagnosticsResponseTransactionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1LoopDiagnosticsResponseTransactionNumber_Type.__name__ = "Integer32"
_Umc1LoopDiagnosticsResponseTransactionNumber_Object = MibTableColumn
umc1LoopDiagnosticsResponseTransactionNumber = _Umc1LoopDiagnosticsResponseTransactionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1, 1),
    _Umc1LoopDiagnosticsResponseTransactionNumber_Type()
)
umc1LoopDiagnosticsResponseTransactionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseTransactionNumber.setStatus("mandatory")
_Umc1LoopDiagnosticsResponseIpAddress_Type = IpAddress
_Umc1LoopDiagnosticsResponseIpAddress_Object = MibTableColumn
umc1LoopDiagnosticsResponseIpAddress = _Umc1LoopDiagnosticsResponseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1, 2),
    _Umc1LoopDiagnosticsResponseIpAddress_Type()
)
umc1LoopDiagnosticsResponseIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseIpAddress.setStatus("mandatory")


class _Umc1LoopDiagnosticsResponseStartToneIdentifier_Type(Integer32):
    """Custom type umc1LoopDiagnosticsResponseStartToneIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1LoopDiagnosticsResponseStartToneIdentifier_Type.__name__ = "Integer32"
_Umc1LoopDiagnosticsResponseStartToneIdentifier_Object = MibTableColumn
umc1LoopDiagnosticsResponseStartToneIdentifier = _Umc1LoopDiagnosticsResponseStartToneIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1, 3),
    _Umc1LoopDiagnosticsResponseStartToneIdentifier_Type()
)
umc1LoopDiagnosticsResponseStartToneIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseStartToneIdentifier.setStatus("mandatory")


class _Umc1LoopDiagnosticsResponseEndToneIdentifier_Type(Integer32):
    """Custom type umc1LoopDiagnosticsResponseEndToneIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Umc1LoopDiagnosticsResponseEndToneIdentifier_Type.__name__ = "Integer32"
_Umc1LoopDiagnosticsResponseEndToneIdentifier_Object = MibTableColumn
umc1LoopDiagnosticsResponseEndToneIdentifier = _Umc1LoopDiagnosticsResponseEndToneIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1, 4),
    _Umc1LoopDiagnosticsResponseEndToneIdentifier_Type()
)
umc1LoopDiagnosticsResponseEndToneIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseEndToneIdentifier.setStatus("mandatory")


class _Umc1LoopDiagnosticsResponseData_Type(OctetString):
    """Custom type umc1LoopDiagnosticsResponseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_Umc1LoopDiagnosticsResponseData_Type.__name__ = "OctetString"
_Umc1LoopDiagnosticsResponseData_Object = MibScalar
umc1LoopDiagnosticsResponseData = _Umc1LoopDiagnosticsResponseData_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 18, 2, 1, 6),
    _Umc1LoopDiagnosticsResponseData_Type()
)
umc1LoopDiagnosticsResponseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1LoopDiagnosticsResponseData.setStatus("mandatory")
_Umc1Trap_ObjectIdentity = ObjectIdentity
umc1Trap = _Umc1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 100)
)


class _Umc1SoftwareDiagMessageTimestamp_Type(OctetString):
    """Custom type umc1SoftwareDiagMessageTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_Umc1SoftwareDiagMessageTimestamp_Type.__name__ = "OctetString"
_Umc1SoftwareDiagMessageTimestamp_Object = MibScalar
umc1SoftwareDiagMessageTimestamp = _Umc1SoftwareDiagMessageTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 100, 1),
    _Umc1SoftwareDiagMessageTimestamp_Type()
)
umc1SoftwareDiagMessageTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SoftwareDiagMessageTimestamp.setStatus("mandatory")


class _Umc1SoftwareDiagMessageType_Type(OctetString):
    """Custom type umc1SoftwareDiagMessageType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Umc1SoftwareDiagMessageType_Type.__name__ = "OctetString"
_Umc1SoftwareDiagMessageType_Object = MibScalar
umc1SoftwareDiagMessageType = _Umc1SoftwareDiagMessageType_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 100, 2),
    _Umc1SoftwareDiagMessageType_Type()
)
umc1SoftwareDiagMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SoftwareDiagMessageType.setStatus("mandatory")
_Umc1SoftwareDiagMessageString_Type = DisplayString
_Umc1SoftwareDiagMessageString_Object = MibScalar
umc1SoftwareDiagMessageString = _Umc1SoftwareDiagMessageString_Object(
    (1, 3, 6, 1, 4, 1, 2067, 1, 1, 2, 100, 3),
    _Umc1SoftwareDiagMessageString_Type()
)
umc1SoftwareDiagMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umc1SoftwareDiagMessageString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMC1000-MIB",
    **{"TerminalIdType": TerminalIdType,
       "ShelfIdType": ShelfIdType,
       "SlotIdType": SlotIdType,
       "PlugInType": PlugInType,
       "DbActionType": DbActionType,
       "V5GroupIdType": V5GroupIdType,
       "DataOperation": DataOperation,
       "umc1System": umc1System,
       "umc1SystemDateTime": umc1SystemDateTime,
       "umc1SystemSysProv": umc1SystemSysProv,
       "umc1SystemSysProvBerTable": umc1SystemSysProvBerTable,
       "umc1SystemSysProvBerEntry": umc1SystemSysProvBerEntry,
       "umc1SystemSysProvBerPit": umc1SystemSysProvBerPit,
       "umc1SystemSysProvBerRedThresh": umc1SystemSysProvBerRedThresh,
       "umc1SystemSysProvBerMaintThresh": umc1SystemSysProvBerMaintThresh,
       "umc1SystemSysProvBerMarginData": umc1SystemSysProvBerMarginData,
       "umc1SystemSysProvSystemCcsThresh": umc1SystemSysProvSystemCcsThresh,
       "umc1SystemSysProvPsuRingVoltage": umc1SystemSysProvPsuRingVoltage,
       "umc1SystemSysProvPsuPulseMeterTone": umc1SystemSysProvPsuPulseMeterTone,
       "umc1SystemSysProvPsuRingFreq": umc1SystemSysProvPsuRingFreq,
       "umc1SystemSysProvChgTable": umc1SystemSysProvChgTable,
       "umc1SystemSysProvChgEntry": umc1SystemSysProvChgEntry,
       "umc1SystemSysProvChgSeqNbr": umc1SystemSysProvChgSeqNbr,
       "umc1SystemSysProvChgData": umc1SystemSysProvChgData,
       "umc1SystemSysProvTableChangeSeqNum": umc1SystemSysProvTableChangeSeqNum,
       "umc1SystemSysProvACOConfig": umc1SystemSysProvACOConfig,
       "umc1SystemSysTimingSource": umc1SystemSysTimingSource,
       "umc1SystemSysTemperature": umc1SystemSysTemperature,
       "umc1SystemSysProvCATable": umc1SystemSysProvCATable,
       "umc1SystemSysProvCAEntry": umc1SystemSysProvCAEntry,
       "umc1SystemSysProvCAIndex": umc1SystemSysProvCAIndex,
       "umc1SystemSysProvCAData": umc1SystemSysProvCAData,
       "umc1SystemPitProv": umc1SystemPitProv,
       "umc1SystemPitProvTable": umc1SystemPitProvTable,
       "umc1SystemPitProvEntry": umc1SystemPitProvEntry,
       "umc1SystemPitProvTerminalId": umc1SystemPitProvTerminalId,
       "umc1SystemPitProvShelfId": umc1SystemPitProvShelfId,
       "umc1SystemPitProvSlotId": umc1SystemPitProvSlotId,
       "umc1SystemPitProvPit": umc1SystemPitProvPit,
       "umc1SystemPitProvData": umc1SystemPitProvData,
       "umc1SystemDefPitProvTable": umc1SystemDefPitProvTable,
       "umc1SystemDefPitProvEntry": umc1SystemDefPitProvEntry,
       "umc1SystemDefPitProvTerminalId": umc1SystemDefPitProvTerminalId,
       "umc1SystemDefPitProvShelfId": umc1SystemDefPitProvShelfId,
       "umc1SystemDefPitProvSlotId": umc1SystemDefPitProvSlotId,
       "umc1SystemDefPitProvPit": umc1SystemDefPitProvPit,
       "umc1SystemDefPitProvData": umc1SystemDefPitProvData,
       "umc1SystemPitProvChgTable": umc1SystemPitProvChgTable,
       "umc1SystemPitProvChgEntry": umc1SystemPitProvChgEntry,
       "umc1SystemPitProvChgSeqNbr": umc1SystemPitProvChgSeqNbr,
       "umc1SystemPitProvChgData": umc1SystemPitProvChgData,
       "umc1SystemPitProvTableChangeSeqNum": umc1SystemPitProvTableChangeSeqNum,
       "umc1FacAlmStringTableChangeSeqNum": umc1FacAlmStringTableChangeSeqNum,
       "umc1FacAlmStringTable": umc1FacAlmStringTable,
       "umc1FacAlmStringEntry": umc1FacAlmStringEntry,
       "umc1FacAlmStringTerminalId": umc1FacAlmStringTerminalId,
       "umc1FacAlmStringShelfId": umc1FacAlmStringShelfId,
       "umc1FacAlmStringSlotId": umc1FacAlmStringSlotId,
       "umc1FacAlmStringFacilityId": umc1FacAlmStringFacilityId,
       "umc1FacAlmStringPluginType": umc1FacAlmStringPluginType,
       "umc1FacAlmStringData": umc1FacAlmStringData,
       "umc1FacAlmStringChgTable": umc1FacAlmStringChgTable,
       "umc1FacAlmStringChgEntry": umc1FacAlmStringChgEntry,
       "umc1FacAlmStringChgSeqNum": umc1FacAlmStringChgSeqNum,
       "umc1FacAlmStringChgData": umc1FacAlmStringChgData,
       "umc1TL1IfProvTableChangeSeqNum": umc1TL1IfProvTableChangeSeqNum,
       "umc1TL1IfProvTable": umc1TL1IfProvTable,
       "umc1TL1IfProvEntry": umc1TL1IfProvEntry,
       "umc1TL1IfProvTerminalId": umc1TL1IfProvTerminalId,
       "umc1TL1IfProvShelfId": umc1TL1IfProvShelfId,
       "umc1TL1IfProvSlotId": umc1TL1IfProvSlotId,
       "umc1TL1IfProvInterfaceId": umc1TL1IfProvInterfaceId,
       "umc1TL1IfProvPluginType": umc1TL1IfProvPluginType,
       "umc1TL1IfProvData": umc1TL1IfProvData,
       "umc1TL1IfProvChgTable": umc1TL1IfProvChgTable,
       "umc1TL1IfProvChgEntry": umc1TL1IfProvChgEntry,
       "umc1TL1IfProvChgSeqNum": umc1TL1IfProvChgSeqNum,
       "umc1TL1IfProvChgData": umc1TL1IfProvChgData,
       "umc1CpuSoftwareFeatures": umc1CpuSoftwareFeatures,
       "umc1SystemRelearnTrapSeqNum": umc1SystemRelearnTrapSeqNum,
       "umc1RestrictedAccess": umc1RestrictedAccess,
       "umc1Service": umc1Service,
       "umc1GR303Grp": umc1GR303Grp,
       "umc1GR303TableChangeSeqNum": umc1GR303TableChangeSeqNum,
       "umc1GR303Table": umc1GR303Table,
       "umc1GR303Entry": umc1GR303Entry,
       "umc1Gr303Index": umc1Gr303Index,
       "umc1Gr303Data": umc1Gr303Data,
       "umc1GR303ChgTable": umc1GR303ChgTable,
       "umc1GR303ChgEntry": umc1GR303ChgEntry,
       "umc1GR303ChgSeqNum": umc1GR303ChgSeqNum,
       "umc1GR303ChgData": umc1GR303ChgData,
       "umc1TR8Grp": umc1TR8Grp,
       "umc1TR8TableChangeSeqNum": umc1TR8TableChangeSeqNum,
       "umc1TR8Table": umc1TR8Table,
       "umc1TR8Entry": umc1TR8Entry,
       "umc1TR8Index": umc1TR8Index,
       "umc1TR8Data": umc1TR8Data,
       "umc1TR8ChgTable": umc1TR8ChgTable,
       "umc1TR8ChgEntry": umc1TR8ChgEntry,
       "umc1TR8ChgSeqNum": umc1TR8ChgSeqNum,
       "umc1TR8ChgData": umc1TR8ChgData,
       "umc1V5Grp": umc1V5Grp,
       "umc1V5TableChangeSeqNum": umc1V5TableChangeSeqNum,
       "umc1V5Table": umc1V5Table,
       "umc1V5Entry": umc1V5Entry,
       "umc1V5Index": umc1V5Index,
       "umc1V5Data": umc1V5Data,
       "umc1V5ChgTable": umc1V5ChgTable,
       "umc1V5ChgEntry": umc1V5ChgEntry,
       "umc1V5ChgSeqNum": umc1V5ChgSeqNum,
       "umc1V5ChgData": umc1V5ChgData,
       "umc1XConnect": umc1XConnect,
       "umc1XCTableChangeSeqNum": umc1XCTableChangeSeqNum,
       "umc1XCTable": umc1XCTable,
       "umc1XCEntry": umc1XCEntry,
       "umc1XCIndex": umc1XCIndex,
       "umc1XCData": umc1XCData,
       "umc1XCChgTable": umc1XCChgTable,
       "umc1XCChgEntry": umc1XCChgEntry,
       "umc1XCChgSeqNum": umc1XCChgSeqNum,
       "umc1XCChgData": umc1XCChgData,
       "umc1SystemAllSeqNbr": umc1SystemAllSeqNbr,
       "umc1AtmProtTableChangeSeqNum": umc1AtmProtTableChangeSeqNum,
       "umc1AtmProtGrpTable": umc1AtmProtGrpTable,
       "umc1AtmProtGrpEntry": umc1AtmProtGrpEntry,
       "umc1AtmProtGrpIndex": umc1AtmProtGrpIndex,
       "umc1AtmProtGrpData": umc1AtmProtGrpData,
       "umc1AtmProtGrpChgTable": umc1AtmProtGrpChgTable,
       "umc1AtmProtGrpChgEntry": umc1AtmProtGrpChgEntry,
       "umc1AtmProtGrpChgSeqNum": umc1AtmProtGrpChgSeqNum,
       "umc1AtmProtGrpChgData": umc1AtmProtGrpChgData,
       "umc1PortProfTableChangeSeqNum": umc1PortProfTableChangeSeqNum,
       "umc1PortProfTable": umc1PortProfTable,
       "umc1PortProfEntry": umc1PortProfEntry,
       "umc1PortProfIndex": umc1PortProfIndex,
       "umc1PortProfData": umc1PortProfData,
       "umc1PortProfChgTable": umc1PortProfChgTable,
       "umc1PortProfChgEntry": umc1PortProfChgEntry,
       "umc1PortProfChgSeqNum": umc1PortProfChgSeqNum,
       "umc1PortProfChgData": umc1PortProfChgData,
       "umc1MyAgentSoftwareFeatures": umc1MyAgentSoftwareFeatures,
       "umc1Security": umc1Security,
       "umc1SecurityDataTableChangeSeqNum": umc1SecurityDataTableChangeSeqNum,
       "umc1SecurityDataTable": umc1SecurityDataTable,
       "umc1SecurityDataEntry": umc1SecurityDataEntry,
       "umc1SecurityDataTableIndex": umc1SecurityDataTableIndex,
       "umc1SecurityDataTableData": umc1SecurityDataTableData,
       "umc1SecurityDataChgTable": umc1SecurityDataChgTable,
       "umc1SecurityDataChgEntry": umc1SecurityDataChgEntry,
       "umc1SecurityDataChgSeqNum": umc1SecurityDataChgSeqNum,
       "umc1SecurityDataChgData": umc1SecurityDataChgData,
       "umc1SystemGenericDbProv": umc1SystemGenericDbProv,
       "umc1SystemGenericDbProvTableSeqNum": umc1SystemGenericDbProvTableSeqNum,
       "umc1SystemGenericDbProvTable": umc1SystemGenericDbProvTable,
       "umc1SystemGenericDbProvEntry": umc1SystemGenericDbProvEntry,
       "umc1SystemGenericDbProvIndex": umc1SystemGenericDbProvIndex,
       "umc1SystemGenericDbProvData": umc1SystemGenericDbProvData,
       "umc1SystemGenericDbProvChgTable": umc1SystemGenericDbProvChgTable,
       "umc1SystemGenericDbProvChgEntry": umc1SystemGenericDbProvChgEntry,
       "umc1SystemGenericDbProvChgTableSeqNum": umc1SystemGenericDbProvChgTableSeqNum,
       "umc1SystemGenericDbProvChgData": umc1SystemGenericDbProvChgData,
       "umc1MibVersion": umc1MibVersion,
       "umc1DbRecordChangeTrapHandleMask": umc1DbRecordChangeTrapHandleMask,
       "umc1SystemAutonomousEvent": umc1SystemAutonomousEvent,
       "umc1SystemAutonomousEventSeqNum": umc1SystemAutonomousEventSeqNum,
       "umc1SystemAutonomousEventTable": umc1SystemAutonomousEventTable,
       "umc1SystemAutonomousEventTableEntry": umc1SystemAutonomousEventTableEntry,
       "umc1SystemAutonomousEventTableSeqNum": umc1SystemAutonomousEventTableSeqNum,
       "umc1SystemAutonomousEventTableData": umc1SystemAutonomousEventTableData,
       "umc1Inventory": umc1Inventory,
       "umc1InventoryShelf": umc1InventoryShelf,
       "umc1InventoryShelfTableChangeSeqNum": umc1InventoryShelfTableChangeSeqNum,
       "umc1InventoryShelfTable": umc1InventoryShelfTable,
       "umc1InventoryShelfEntry": umc1InventoryShelfEntry,
       "umc1InventoryShelfTerminalId": umc1InventoryShelfTerminalId,
       "umc1InventoryShelfShelfId": umc1InventoryShelfShelfId,
       "umc1InventoryShelfType": umc1InventoryShelfType,
       "umc1InventoryShelfTableChangeHistoryTable": umc1InventoryShelfTableChangeHistoryTable,
       "umc1InventoryShelfTableChangeHistoryEntry": umc1InventoryShelfTableChangeHistoryEntry,
       "umc1InventoryShelfTableChangeHistoryIndex": umc1InventoryShelfTableChangeHistoryIndex,
       "umc1InventoryShelfTableChangeHistoryData": umc1InventoryShelfTableChangeHistoryData,
       "umc1InventoryShelfExtended": umc1InventoryShelfExtended,
       "umc1InventoryShelfExtendedTable": umc1InventoryShelfExtendedTable,
       "umc1InventoryShelfExtendedEntry": umc1InventoryShelfExtendedEntry,
       "umc1InventoryShelfExtendedTerminalId": umc1InventoryShelfExtendedTerminalId,
       "umc1InventoryShelfExtendedShelfId": umc1InventoryShelfExtendedShelfId,
       "umc1InventoryShelfExtendedVersion": umc1InventoryShelfExtendedVersion,
       "umc1InventoryShelfExtendedAssemblyNumber": umc1InventoryShelfExtendedAssemblyNumber,
       "umc1InventoryShelfExtendedSerialNumber": umc1InventoryShelfExtendedSerialNumber,
       "umc1InventoryShelfExtendedCLEICode": umc1InventoryShelfExtendedCLEICode,
       "umc1InventoryPlugin": umc1InventoryPlugin,
       "umc1InventoryPluginTableChangeSeqNum": umc1InventoryPluginTableChangeSeqNum,
       "umc1InventoryPluginTable": umc1InventoryPluginTable,
       "umc1InventoryPluginEntry": umc1InventoryPluginEntry,
       "umc1InventoryPluginTerminalId": umc1InventoryPluginTerminalId,
       "umc1InventoryPluginShelfId": umc1InventoryPluginShelfId,
       "umc1InventoryPluginSlotId": umc1InventoryPluginSlotId,
       "umc1InventoryPluginType": umc1InventoryPluginType,
       "umc1InventoryPluginTableChangeHistoryTable": umc1InventoryPluginTableChangeHistoryTable,
       "umc1InventoryPluginTableChangeHistoryEntry": umc1InventoryPluginTableChangeHistoryEntry,
       "umc1InventoryPluginTableChangeHistoryIndex": umc1InventoryPluginTableChangeHistoryIndex,
       "umc1InventoryPluginTableChangeHistoryData": umc1InventoryPluginTableChangeHistoryData,
       "umc1InventoryPluginExtended": umc1InventoryPluginExtended,
       "umc1InventoryPluginExtendedTable": umc1InventoryPluginExtendedTable,
       "umc1InventoryPluginExtendedEntry": umc1InventoryPluginExtendedEntry,
       "umc1InventoryPluginExtendedTerminalId": umc1InventoryPluginExtendedTerminalId,
       "umc1InventoryPluginExtendedShelfId": umc1InventoryPluginExtendedShelfId,
       "umc1InventoryPluginExtendedSlotId": umc1InventoryPluginExtendedSlotId,
       "umc1InventoryPluginExtendedStatus": umc1InventoryPluginExtendedStatus,
       "umc1InventoryPluginExtendedVersion": umc1InventoryPluginExtendedVersion,
       "umc1InventoryPluginExtendedAssemblyNumber": umc1InventoryPluginExtendedAssemblyNumber,
       "umc1InventoryPluginExtendedSerialNumber": umc1InventoryPluginExtendedSerialNumber,
       "umc1InventoryPluginExtendedCLEICode": umc1InventoryPluginExtendedCLEICode,
       "umc1Terminal": umc1Terminal,
       "umc1TerminalStatusChangeSeqNum": umc1TerminalStatusChangeSeqNum,
       "umc1TerminalStatusTable": umc1TerminalStatusTable,
       "umc1TerminalStatusEntry": umc1TerminalStatusEntry,
       "umc1TerminalStatusTerminalId": umc1TerminalStatusTerminalId,
       "umc1TerminalStatusValue": umc1TerminalStatusValue,
       "umc1TerminalInfoChangeSeqNum": umc1TerminalInfoChangeSeqNum,
       "umc1TerminalInfoTable": umc1TerminalInfoTable,
       "umc1TerminalInfoEntry": umc1TerminalInfoEntry,
       "umc1TerminalInfoTerminalId": umc1TerminalInfoTerminalId,
       "umc1TerminalInfoName": umc1TerminalInfoName,
       "umc1TerminalInfoSerialDeviceType": umc1TerminalInfoSerialDeviceType,
       "umc1TerminalInfoBaudRate": umc1TerminalInfoBaudRate,
       "umc1TerminalInfoNewTerminalId": umc1TerminalInfoNewTerminalId,
       "umc1ACOSnapTopology": umc1ACOSnapTopology,
       "umc1ACOSnapTopologySeqNum": umc1ACOSnapTopologySeqNum,
       "umc1ACOSnapTopologyLinkTable": umc1ACOSnapTopologyLinkTable,
       "umc1ACOSnapTopologyLinkEntry": umc1ACOSnapTopologyLinkEntry,
       "umc1ACOSnapTopologyLinkTerminalA": umc1ACOSnapTopologyLinkTerminalA,
       "umc1ACOSnapTopologyLinkTerminalB": umc1ACOSnapTopologyLinkTerminalB,
       "umc1CommandResponse": umc1CommandResponse,
       "umc1CommandTable": umc1CommandTable,
       "umc1CommandTableEntry": umc1CommandTableEntry,
       "umc1CommandId": umc1CommandId,
       "umc1CommandArg": umc1CommandArg,
       "umc1CommandTransNbr": umc1CommandTransNbr,
       "umc1ResponseTable": umc1ResponseTable,
       "umc1ResponseTableEntry": umc1ResponseTableEntry,
       "umc1ResponseTransNbr": umc1ResponseTransNbr,
       "umc1ResponseSeqNbr": umc1ResponseSeqNbr,
       "umc1ResponseData": umc1ResponseData,
       "umc1Span": umc1Span,
       "umc1TerminalSpanTableChangeSeqNum": umc1TerminalSpanTableChangeSeqNum,
       "umc1TerminalSpanTable": umc1TerminalSpanTable,
       "umc1TerminalSpanTableEntry": umc1TerminalSpanTableEntry,
       "umc1TermSpanNearEndTerminalId": umc1TermSpanNearEndTerminalId,
       "umc1TermSpanNearEndShelfId": umc1TermSpanNearEndShelfId,
       "umc1TermSpanNearEndSlotId": umc1TermSpanNearEndSlotId,
       "umc1TermSpanNearEndPitType": umc1TermSpanNearEndPitType,
       "umc1TermSpanFarEndTerminalId": umc1TermSpanFarEndTerminalId,
       "umc1TermSpanFarEndShelfId": umc1TermSpanFarEndShelfId,
       "umc1TermSpanFarEndSlotId": umc1TermSpanFarEndSlotId,
       "umc1TerminalSpanTableChangeHistoryTable": umc1TerminalSpanTableChangeHistoryTable,
       "umc1TerminalSpanTableChangeHistoryEntry": umc1TerminalSpanTableChangeHistoryEntry,
       "umc1TerminalSpanTableChangeHistoryIndex": umc1TerminalSpanTableChangeHistoryIndex,
       "umc1TerminalSpanTableChangeHistoryData": umc1TerminalSpanTableChangeHistoryData,
       "umc1ShelfSpanTableChangeSeqNum": umc1ShelfSpanTableChangeSeqNum,
       "umc1ShelfSpanTable": umc1ShelfSpanTable,
       "umc1ShelfSpanTableEntry": umc1ShelfSpanTableEntry,
       "umc1ShelfSpanNearEndTerminalId": umc1ShelfSpanNearEndTerminalId,
       "umc1ShelfSpanNearEndShelfId": umc1ShelfSpanNearEndShelfId,
       "umc1ShelfSpanNearEndSlotId": umc1ShelfSpanNearEndSlotId,
       "umc1ShelfSpanNearEndPitType": umc1ShelfSpanNearEndPitType,
       "umc1ShelfSpanFarEndShelfId": umc1ShelfSpanFarEndShelfId,
       "umc1ShelfSpanFarEndSlotId": umc1ShelfSpanFarEndSlotId,
       "umc1ShelfSpanFarEndPitType": umc1ShelfSpanFarEndPitType,
       "umc1ShelfSpanTableChangeHistoryTable": umc1ShelfSpanTableChangeHistoryTable,
       "umc1ShelfSpanTableChangeHistoryEntry": umc1ShelfSpanTableChangeHistoryEntry,
       "umc1ShelfSpanTableChangeHistoryIndex": umc1ShelfSpanTableChangeHistoryIndex,
       "umc1ShelfSpanTableChangeHistoryData": umc1ShelfSpanTableChangeHistoryData,
       "umc1Alarm": umc1Alarm,
       "umc1AlmSeqTableChangeSeqNum": umc1AlmSeqTableChangeSeqNum,
       "umc1AlmSeqTable": umc1AlmSeqTable,
       "umc1AlmSeqEntry": umc1AlmSeqEntry,
       "umc1AlmSeqTerminalId": umc1AlmSeqTerminalId,
       "umc1AlmSeqNumber": umc1AlmSeqNumber,
       "umc1CurAlmTable": umc1CurAlmTable,
       "umc1CurAlmEntry": umc1CurAlmEntry,
       "umc1CurAlmTerminalId": umc1CurAlmTerminalId,
       "umc1CurAlmOccurrenceIndex": umc1CurAlmOccurrenceIndex,
       "umc1CurAlmTL1Message": umc1CurAlmTL1Message,
       "umc1CurAlmDetails": umc1CurAlmDetails,
       "umc1ManagerIf": umc1ManagerIf,
       "umc1Snmp": umc1Snmp,
       "umc1SnmpCommName": umc1SnmpCommName,
       "umc1SnmpTrapTypesEnabled": umc1SnmpTrapTypesEnabled,
       "umc1SnmpTrapRcvrAddress": umc1SnmpTrapRcvrAddress,
       "umc1SnmpTrapRcvrPort": umc1SnmpTrapRcvrPort,
       "umc1SnmpMgmtHost2Address": umc1SnmpMgmtHost2Address,
       "umc1SnmpMgmtHost2TrapsEnabled": umc1SnmpMgmtHost2TrapsEnabled,
       "umc1SnmpMgmtHost3Address": umc1SnmpMgmtHost3Address,
       "umc1SnmpMgmtHost3TrapsEnabled": umc1SnmpMgmtHost3TrapsEnabled,
       "umc1SnmpTrustedHostsEnabled": umc1SnmpTrustedHostsEnabled,
       "umc1SnmpTelnetPort": umc1SnmpTelnetPort,
       "umc1Topology": umc1Topology,
       "umc1TopologyChangeSeqNum": umc1TopologyChangeSeqNum,
       "umc1TopologyThisTerminal": umc1TopologyThisTerminal,
       "umc1TopologyLinkTable": umc1TopologyLinkTable,
       "umc1TopologyLinkEntry": umc1TopologyLinkEntry,
       "umc1TopologyLinkTerminalA": umc1TopologyLinkTerminalA,
       "umc1TopologyLinkTerminalB": umc1TopologyLinkTerminalB,
       "umc1DataService": umc1DataService,
       "umc1DsPlugInNameTable": umc1DsPlugInNameTable,
       "umc1DsPlugInNameEntry": umc1DsPlugInNameEntry,
       "umc1DsPlugInType": umc1DsPlugInType,
       "umc1DsPlugInName": umc1DsPlugInName,
       "umc1DsAlarmStringTable": umc1DsAlarmStringTable,
       "umc1DsAlarmStringEntry": umc1DsAlarmStringEntry,
       "umc1DsAlarmFacilityNumber": umc1DsAlarmFacilityNumber,
       "umc1DsAlarmString": umc1DsAlarmString,
       "umc1TriggerTrapAllSeqNumbers": umc1TriggerTrapAllSeqNumbers,
       "umc1SystemTcaEvent": umc1SystemTcaEvent,
       "umc1SystemTCASeqNum": umc1SystemTCASeqNum,
       "umc1SystemTCAHistoryTable": umc1SystemTCAHistoryTable,
       "umc1SystemTCAHistoryTableEntry": umc1SystemTCAHistoryTableEntry,
       "umc1SystemTCAHistoryTableSeqNum": umc1SystemTCAHistoryTableSeqNum,
       "umc1SystemTCAHistoryTableChgData": umc1SystemTCAHistoryTableChgData,
       "umc1F5Loopback": umc1F5Loopback,
       "umc1F5LoopbackRequestTable": umc1F5LoopbackRequestTable,
       "umc1F5LoopbackRequestEntry": umc1F5LoopbackRequestEntry,
       "umc1F5LoopbackTransactionNumber": umc1F5LoopbackTransactionNumber,
       "umc1F5LoopbackTransactionIpAddress": umc1F5LoopbackTransactionIpAddress,
       "umc1F5LoopbackTransactionIbMessage": umc1F5LoopbackTransactionIbMessage,
       "umc1LoopDiagnostics": umc1LoopDiagnostics,
       "umc1LoopDiagnosticsRequestTable": umc1LoopDiagnosticsRequestTable,
       "umc1LoopDiagnosticsRequestEntry": umc1LoopDiagnosticsRequestEntry,
       "umc1LoopDiagnosticsRequestTransactionNumber": umc1LoopDiagnosticsRequestTransactionNumber,
       "umc1LoopDiagnosticsRequestIpAddress": umc1LoopDiagnosticsRequestIpAddress,
       "umc1LoopDiagnosticsRequestData": umc1LoopDiagnosticsRequestData,
       "umc1LoopDiagnosticsResponseTable": umc1LoopDiagnosticsResponseTable,
       "umc1LoopDiagnosticsResponseEntry": umc1LoopDiagnosticsResponseEntry,
       "umc1LoopDiagnosticsResponseTransactionNumber": umc1LoopDiagnosticsResponseTransactionNumber,
       "umc1LoopDiagnosticsResponseIpAddress": umc1LoopDiagnosticsResponseIpAddress,
       "umc1LoopDiagnosticsResponseStartToneIdentifier": umc1LoopDiagnosticsResponseStartToneIdentifier,
       "umc1LoopDiagnosticsResponseEndToneIdentifier": umc1LoopDiagnosticsResponseEndToneIdentifier,
       "umc1LoopDiagnosticsResponseData": umc1LoopDiagnosticsResponseData,
       "umc1Trap": umc1Trap,
       "umc1SoftwareDiagMessageTimestamp": umc1SoftwareDiagMessageTimestamp,
       "umc1SoftwareDiagMessageType": umc1SoftwareDiagMessageType,
       "umc1SoftwareDiagMessageString": umc1SoftwareDiagMessageString}
)
