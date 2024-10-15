# SNMP MIB module (NBS-ODSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-ODSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:53 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(NbsTcMilliAmp,
 NbsTcMilliVolt,
 NbsTcPartIndex,
 NbsTcStatusLevel,
 NbsTcStatusSimple,
 NbsTcTemperature,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMilliAmp",
    "NbsTcMilliVolt",
    "NbsTcPartIndex",
    "NbsTcStatusLevel",
    "NbsTcStatusSimple",
    "NbsTcTemperature",
    "nbs")

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

nbsOdsysMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsOdsysChasGrp_ObjectIdentity = ObjectIdentity
nbsOdsysChasGrp = _NbsOdsysChasGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 2)
)
if mibBuilder.loadTexts:
    nbsOdsysChasGrp.setStatus("current")
_NbsOdsysChasTable_Object = MibTable
nbsOdsysChasTable = _NbsOdsysChasTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1)
)
if mibBuilder.loadTexts:
    nbsOdsysChasTable.setStatus("current")
_NbsOdsysChasEntry_Object = MibTableRow
nbsOdsysChasEntry = _NbsOdsysChasEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1)
)
nbsOdsysChasEntry.setIndexNames(
    (0, "NBS-ODSYS-MIB", "nbsOdsysChasIndex"),
)
if mibBuilder.loadTexts:
    nbsOdsysChasEntry.setStatus("current")
_NbsOdsysChasIndex_Type = Integer32
_NbsOdsysChasIndex_Object = MibTableColumn
nbsOdsysChasIndex = _NbsOdsysChasIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 1),
    _NbsOdsysChasIndex_Type()
)
nbsOdsysChasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysChasIndex.setStatus("current")
_NbsOdsysChasCcMaxCount_Type = Integer32
_NbsOdsysChasCcMaxCount_Object = MibTableColumn
nbsOdsysChasCcMaxCount = _NbsOdsysChasCcMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 10),
    _NbsOdsysChasCcMaxCount_Type()
)
nbsOdsysChasCcMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysChasCcMaxCount.setStatus("current")
_NbsOdsysChasPsMaxCount_Type = Integer32
_NbsOdsysChasPsMaxCount_Object = MibTableColumn
nbsOdsysChasPsMaxCount = _NbsOdsysChasPsMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 20),
    _NbsOdsysChasPsMaxCount_Type()
)
nbsOdsysChasPsMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysChasPsMaxCount.setStatus("current")
_NbsOdsysChasFtMaxCount_Type = Integer32
_NbsOdsysChasFtMaxCount_Object = MibTableColumn
nbsOdsysChasFtMaxCount = _NbsOdsysChasFtMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 30),
    _NbsOdsysChasFtMaxCount_Type()
)
nbsOdsysChasFtMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysChasFtMaxCount.setStatus("current")
_NbsOdsysCcGrp_ObjectIdentity = ObjectIdentity
nbsOdsysCcGrp = _NbsOdsysCcGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 3)
)
if mibBuilder.loadTexts:
    nbsOdsysCcGrp.setStatus("current")
_NbsOdsysCcTable_Object = MibTable
nbsOdsysCcTable = _NbsOdsysCcTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1)
)
if mibBuilder.loadTexts:
    nbsOdsysCcTable.setStatus("current")
_NbsOdsysCcEntry_Object = MibTableRow
nbsOdsysCcEntry = _NbsOdsysCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1)
)
nbsOdsysCcEntry.setIndexNames(
    (0, "NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
    (0, "NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"),
)
if mibBuilder.loadTexts:
    nbsOdsysCcEntry.setStatus("current")
_NbsOdsysCcChasIndex_Type = Integer32
_NbsOdsysCcChasIndex_Object = MibTableColumn
nbsOdsysCcChasIndex = _NbsOdsysCcChasIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 1),
    _NbsOdsysCcChasIndex_Type()
)
nbsOdsysCcChasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcChasIndex.setStatus("current")
_NbsOdsysCcBayIndex_Type = Integer32
_NbsOdsysCcBayIndex_Object = MibTableColumn
nbsOdsysCcBayIndex = _NbsOdsysCcBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 2),
    _NbsOdsysCcBayIndex_Type()
)
nbsOdsysCcBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcBayIndex.setStatus("current")
_NbsOdsysCcChIfIndex_Type = InterfaceIndex
_NbsOdsysCcChIfIndex_Object = MibTableColumn
nbsOdsysCcChIfIndex = _NbsOdsysCcChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 10),
    _NbsOdsysCcChIfIndex_Type()
)
nbsOdsysCcChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcChIfIndex.setStatus("current")
_NbsOdsysCcPartIndex_Type = NbsTcPartIndex
_NbsOdsysCcPartIndex_Object = MibTableColumn
nbsOdsysCcPartIndex = _NbsOdsysCcPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 11),
    _NbsOdsysCcPartIndex_Type()
)
nbsOdsysCcPartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcPartIndex.setStatus("current")
_NbsOdsysCcThermActual_Type = NbsTcTemperature
_NbsOdsysCcThermActual_Object = MibTableColumn
nbsOdsysCcThermActual = _NbsOdsysCcThermActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 30),
    _NbsOdsysCcThermActual_Type()
)
nbsOdsysCcThermActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermActual.setStatus("current")
_NbsOdsysCcThermLevel_Type = NbsTcStatusLevel
_NbsOdsysCcThermLevel_Object = MibTableColumn
nbsOdsysCcThermLevel = _NbsOdsysCcThermLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 40),
    _NbsOdsysCcThermLevel_Type()
)
nbsOdsysCcThermLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermLevel.setStatus("current")
_NbsOdsysCcThermThreshLoErr_Type = NbsTcTemperature
_NbsOdsysCcThermThreshLoErr_Object = MibTableColumn
nbsOdsysCcThermThreshLoErr = _NbsOdsysCcThermThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 41),
    _NbsOdsysCcThermThreshLoErr_Type()
)
nbsOdsysCcThermThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermThreshLoErr.setStatus("current")
_NbsOdsysCcThermThreshLoWarn_Type = NbsTcTemperature
_NbsOdsysCcThermThreshLoWarn_Object = MibTableColumn
nbsOdsysCcThermThreshLoWarn = _NbsOdsysCcThermThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 42),
    _NbsOdsysCcThermThreshLoWarn_Type()
)
nbsOdsysCcThermThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermThreshLoWarn.setStatus("current")
_NbsOdsysCcThermThreshHiWarn_Type = NbsTcTemperature
_NbsOdsysCcThermThreshHiWarn_Object = MibTableColumn
nbsOdsysCcThermThreshHiWarn = _NbsOdsysCcThermThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 43),
    _NbsOdsysCcThermThreshHiWarn_Type()
)
nbsOdsysCcThermThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermThreshHiWarn.setStatus("current")
_NbsOdsysCcThermThreshHiErr_Type = NbsTcTemperature
_NbsOdsysCcThermThreshHiErr_Object = MibTableColumn
nbsOdsysCcThermThreshHiErr = _NbsOdsysCcThermThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 44),
    _NbsOdsysCcThermThreshHiErr_Type()
)
nbsOdsysCcThermThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcThermThreshHiErr.setStatus("current")
_NbsOdsysCcOperationalStatus_Type = NbsTcStatusSimple
_NbsOdsysCcOperationalStatus_Object = MibTableColumn
nbsOdsysCcOperationalStatus = _NbsOdsysCcOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 50),
    _NbsOdsysCcOperationalStatus_Type()
)
nbsOdsysCcOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysCcOperationalStatus.setStatus("current")
_NbsOdsysFtGrp_ObjectIdentity = ObjectIdentity
nbsOdsysFtGrp = _NbsOdsysFtGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 4)
)
if mibBuilder.loadTexts:
    nbsOdsysFtGrp.setStatus("current")
_NbsOdsysFtTable_Object = MibTable
nbsOdsysFtTable = _NbsOdsysFtTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1)
)
if mibBuilder.loadTexts:
    nbsOdsysFtTable.setStatus("current")
_NbsOdsysFtEntry_Object = MibTableRow
nbsOdsysFtEntry = _NbsOdsysFtEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1)
)
nbsOdsysFtEntry.setIndexNames(
    (0, "NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"),
    (0, "NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"),
)
if mibBuilder.loadTexts:
    nbsOdsysFtEntry.setStatus("current")
_NbsOdsysFtChasIndex_Type = Integer32
_NbsOdsysFtChasIndex_Object = MibTableColumn
nbsOdsysFtChasIndex = _NbsOdsysFtChasIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 1),
    _NbsOdsysFtChasIndex_Type()
)
nbsOdsysFtChasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtChasIndex.setStatus("current")
_NbsOdsysFtBayIndex_Type = Integer32
_NbsOdsysFtBayIndex_Object = MibTableColumn
nbsOdsysFtBayIndex = _NbsOdsysFtBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 2),
    _NbsOdsysFtBayIndex_Type()
)
nbsOdsysFtBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtBayIndex.setStatus("current")
_NbsOdsysFtOperationalStatus_Type = NbsTcStatusSimple
_NbsOdsysFtOperationalStatus_Object = MibTableColumn
nbsOdsysFtOperationalStatus = _NbsOdsysFtOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 3),
    _NbsOdsysFtOperationalStatus_Type()
)
nbsOdsysFtOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtOperationalStatus.setStatus("current")
_NbsOdsysFtChIfIndex_Type = InterfaceIndex
_NbsOdsysFtChIfIndex_Object = MibTableColumn
nbsOdsysFtChIfIndex = _NbsOdsysFtChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 10),
    _NbsOdsysFtChIfIndex_Type()
)
nbsOdsysFtChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtChIfIndex.setStatus("current")
_NbsOdsysFtPartIndex_Type = NbsTcPartIndex
_NbsOdsysFtPartIndex_Object = MibTableColumn
nbsOdsysFtPartIndex = _NbsOdsysFtPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 11),
    _NbsOdsysFtPartIndex_Type()
)
nbsOdsysFtPartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtPartIndex.setStatus("current")
_NbsOdsysFtFanCount_Type = Integer32
_NbsOdsysFtFanCount_Object = MibTableColumn
nbsOdsysFtFanCount = _NbsOdsysFtFanCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 20),
    _NbsOdsysFtFanCount_Type()
)
nbsOdsysFtFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtFanCount.setStatus("current")
_NbsOdsysFtThermActual_Type = NbsTcTemperature
_NbsOdsysFtThermActual_Object = MibTableColumn
nbsOdsysFtThermActual = _NbsOdsysFtThermActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 30),
    _NbsOdsysFtThermActual_Type()
)
nbsOdsysFtThermActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermActual.setStatus("current")
_NbsOdsysFtThermLevel_Type = NbsTcStatusLevel
_NbsOdsysFtThermLevel_Object = MibTableColumn
nbsOdsysFtThermLevel = _NbsOdsysFtThermLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 40),
    _NbsOdsysFtThermLevel_Type()
)
nbsOdsysFtThermLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermLevel.setStatus("current")
_NbsOdsysFtThermThreshLoErr_Type = NbsTcTemperature
_NbsOdsysFtThermThreshLoErr_Object = MibTableColumn
nbsOdsysFtThermThreshLoErr = _NbsOdsysFtThermThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 41),
    _NbsOdsysFtThermThreshLoErr_Type()
)
nbsOdsysFtThermThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermThreshLoErr.setStatus("current")
_NbsOdsysFtThermThreshLoWarn_Type = NbsTcTemperature
_NbsOdsysFtThermThreshLoWarn_Object = MibTableColumn
nbsOdsysFtThermThreshLoWarn = _NbsOdsysFtThermThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 42),
    _NbsOdsysFtThermThreshLoWarn_Type()
)
nbsOdsysFtThermThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermThreshLoWarn.setStatus("current")
_NbsOdsysFtThermThreshHiWarn_Type = NbsTcTemperature
_NbsOdsysFtThermThreshHiWarn_Object = MibTableColumn
nbsOdsysFtThermThreshHiWarn = _NbsOdsysFtThermThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 43),
    _NbsOdsysFtThermThreshHiWarn_Type()
)
nbsOdsysFtThermThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermThreshHiWarn.setStatus("current")
_NbsOdsysFtThermThreshHiErr_Type = NbsTcTemperature
_NbsOdsysFtThermThreshHiErr_Object = MibTableColumn
nbsOdsysFtThermThreshHiErr = _NbsOdsysFtThermThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 44),
    _NbsOdsysFtThermThreshHiErr_Type()
)
nbsOdsysFtThermThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysFtThermThreshHiErr.setStatus("current")
_NbsOdsysPsGrp_ObjectIdentity = ObjectIdentity
nbsOdsysPsGrp = _NbsOdsysPsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 5)
)
if mibBuilder.loadTexts:
    nbsOdsysPsGrp.setStatus("current")
_NbsOdsysPsTable_Object = MibTable
nbsOdsysPsTable = _NbsOdsysPsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2)
)
if mibBuilder.loadTexts:
    nbsOdsysPsTable.setStatus("current")
_NbsOdsysPsEntry_Object = MibTableRow
nbsOdsysPsEntry = _NbsOdsysPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1)
)
nbsOdsysPsEntry.setIndexNames(
    (0, "NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
    (0, "NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
)
if mibBuilder.loadTexts:
    nbsOdsysPsEntry.setStatus("current")
_NbsOdsysPsChasIndex_Type = Integer32
_NbsOdsysPsChasIndex_Object = MibTableColumn
nbsOdsysPsChasIndex = _NbsOdsysPsChasIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 1),
    _NbsOdsysPsChasIndex_Type()
)
nbsOdsysPsChasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsChasIndex.setStatus("current")
_NbsOdsysPsBayIndex_Type = Integer32
_NbsOdsysPsBayIndex_Object = MibTableColumn
nbsOdsysPsBayIndex = _NbsOdsysPsBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 2),
    _NbsOdsysPsBayIndex_Type()
)
nbsOdsysPsBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsBayIndex.setStatus("current")
_NbsOdsysPsOperationalStatus_Type = NbsTcStatusSimple
_NbsOdsysPsOperationalStatus_Object = MibTableColumn
nbsOdsysPsOperationalStatus = _NbsOdsysPsOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 3),
    _NbsOdsysPsOperationalStatus_Type()
)
nbsOdsysPsOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsOperationalStatus.setStatus("current")
_NbsOdsysPsChIfIndex_Type = InterfaceIndex
_NbsOdsysPsChIfIndex_Object = MibTableColumn
nbsOdsysPsChIfIndex = _NbsOdsysPsChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 10),
    _NbsOdsysPsChIfIndex_Type()
)
nbsOdsysPsChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsChIfIndex.setStatus("current")
_NbsOdsysPsPartIndex_Type = NbsTcPartIndex
_NbsOdsysPsPartIndex_Object = MibTableColumn
nbsOdsysPsPartIndex = _NbsOdsysPsPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 11),
    _NbsOdsysPsPartIndex_Type()
)
nbsOdsysPsPartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsPartIndex.setStatus("current")
_NbsOdsysPsFanCount_Type = Integer32
_NbsOdsysPsFanCount_Object = MibTableColumn
nbsOdsysPsFanCount = _NbsOdsysPsFanCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 30),
    _NbsOdsysPsFanCount_Type()
)
nbsOdsysPsFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsFanCount.setStatus("current")
_NbsOdsysPsThermActual_Type = NbsTcTemperature
_NbsOdsysPsThermActual_Object = MibTableColumn
nbsOdsysPsThermActual = _NbsOdsysPsThermActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 40),
    _NbsOdsysPsThermActual_Type()
)
nbsOdsysPsThermActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermActual.setStatus("current")
_NbsOdsysPsThermLevel_Type = NbsTcStatusLevel
_NbsOdsysPsThermLevel_Object = MibTableColumn
nbsOdsysPsThermLevel = _NbsOdsysPsThermLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 41),
    _NbsOdsysPsThermLevel_Type()
)
nbsOdsysPsThermLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermLevel.setStatus("current")
_NbsOdsysPsThermThreshLoErr_Type = NbsTcTemperature
_NbsOdsysPsThermThreshLoErr_Object = MibTableColumn
nbsOdsysPsThermThreshLoErr = _NbsOdsysPsThermThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 42),
    _NbsOdsysPsThermThreshLoErr_Type()
)
nbsOdsysPsThermThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermThreshLoErr.setStatus("current")
_NbsOdsysPsThermThreshLoWarn_Type = NbsTcTemperature
_NbsOdsysPsThermThreshLoWarn_Object = MibTableColumn
nbsOdsysPsThermThreshLoWarn = _NbsOdsysPsThermThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 43),
    _NbsOdsysPsThermThreshLoWarn_Type()
)
nbsOdsysPsThermThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermThreshLoWarn.setStatus("current")
_NbsOdsysPsThermThreshHiWarn_Type = NbsTcTemperature
_NbsOdsysPsThermThreshHiWarn_Object = MibTableColumn
nbsOdsysPsThermThreshHiWarn = _NbsOdsysPsThermThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 44),
    _NbsOdsysPsThermThreshHiWarn_Type()
)
nbsOdsysPsThermThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermThreshHiWarn.setStatus("current")
_NbsOdsysPsThermThreshHiErr_Type = NbsTcTemperature
_NbsOdsysPsThermThreshHiErr_Object = MibTableColumn
nbsOdsysPsThermThreshHiErr = _NbsOdsysPsThermThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 45),
    _NbsOdsysPsThermThreshHiErr_Type()
)
nbsOdsysPsThermThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsThermThreshHiErr.setStatus("current")
_NbsOdsysPsVInActual_Type = NbsTcMilliVolt
_NbsOdsysPsVInActual_Object = MibTableColumn
nbsOdsysPsVInActual = _NbsOdsysPsVInActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 50),
    _NbsOdsysPsVInActual_Type()
)
nbsOdsysPsVInActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInActual.setStatus("current")
_NbsOdsysPsVInLevel_Type = NbsTcStatusLevel
_NbsOdsysPsVInLevel_Object = MibTableColumn
nbsOdsysPsVInLevel = _NbsOdsysPsVInLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 51),
    _NbsOdsysPsVInLevel_Type()
)
nbsOdsysPsVInLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInLevel.setStatus("current")
_NbsOdsysPsVInThreshLoErr_Type = NbsTcMilliVolt
_NbsOdsysPsVInThreshLoErr_Object = MibTableColumn
nbsOdsysPsVInThreshLoErr = _NbsOdsysPsVInThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 52),
    _NbsOdsysPsVInThreshLoErr_Type()
)
nbsOdsysPsVInThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInThreshLoErr.setStatus("current")
_NbsOdsysPsVInThreshLoWarn_Type = NbsTcMilliVolt
_NbsOdsysPsVInThreshLoWarn_Object = MibTableColumn
nbsOdsysPsVInThreshLoWarn = _NbsOdsysPsVInThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 53),
    _NbsOdsysPsVInThreshLoWarn_Type()
)
nbsOdsysPsVInThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInThreshLoWarn.setStatus("current")
_NbsOdsysPsVInThreshHiWarn_Type = NbsTcMilliVolt
_NbsOdsysPsVInThreshHiWarn_Object = MibTableColumn
nbsOdsysPsVInThreshHiWarn = _NbsOdsysPsVInThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 54),
    _NbsOdsysPsVInThreshHiWarn_Type()
)
nbsOdsysPsVInThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInThreshHiWarn.setStatus("current")
_NbsOdsysPsVInThreshHiErr_Type = NbsTcMilliVolt
_NbsOdsysPsVInThreshHiErr_Object = MibTableColumn
nbsOdsysPsVInThreshHiErr = _NbsOdsysPsVInThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 55),
    _NbsOdsysPsVInThreshHiErr_Type()
)
nbsOdsysPsVInThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVInThreshHiErr.setStatus("current")
_NbsOdsysPsVOutActual_Type = NbsTcMilliVolt
_NbsOdsysPsVOutActual_Object = MibTableColumn
nbsOdsysPsVOutActual = _NbsOdsysPsVOutActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 60),
    _NbsOdsysPsVOutActual_Type()
)
nbsOdsysPsVOutActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutActual.setStatus("current")
_NbsOdsysPsVOutLevel_Type = NbsTcStatusLevel
_NbsOdsysPsVOutLevel_Object = MibTableColumn
nbsOdsysPsVOutLevel = _NbsOdsysPsVOutLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 61),
    _NbsOdsysPsVOutLevel_Type()
)
nbsOdsysPsVOutLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutLevel.setStatus("current")
_NbsOdsysPsVOutThreshLoErr_Type = NbsTcMilliVolt
_NbsOdsysPsVOutThreshLoErr_Object = MibTableColumn
nbsOdsysPsVOutThreshLoErr = _NbsOdsysPsVOutThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 62),
    _NbsOdsysPsVOutThreshLoErr_Type()
)
nbsOdsysPsVOutThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutThreshLoErr.setStatus("current")
_NbsOdsysPsVOutThreshLoWarn_Type = NbsTcMilliVolt
_NbsOdsysPsVOutThreshLoWarn_Object = MibTableColumn
nbsOdsysPsVOutThreshLoWarn = _NbsOdsysPsVOutThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 63),
    _NbsOdsysPsVOutThreshLoWarn_Type()
)
nbsOdsysPsVOutThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutThreshLoWarn.setStatus("current")
_NbsOdsysPsVOutThreshHiWarn_Type = NbsTcMilliVolt
_NbsOdsysPsVOutThreshHiWarn_Object = MibTableColumn
nbsOdsysPsVOutThreshHiWarn = _NbsOdsysPsVOutThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 64),
    _NbsOdsysPsVOutThreshHiWarn_Type()
)
nbsOdsysPsVOutThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutThreshHiWarn.setStatus("current")
_NbsOdsysPsVOutThreshHiErr_Type = NbsTcMilliVolt
_NbsOdsysPsVOutThreshHiErr_Object = MibTableColumn
nbsOdsysPsVOutThreshHiErr = _NbsOdsysPsVOutThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 65),
    _NbsOdsysPsVOutThreshHiErr_Type()
)
nbsOdsysPsVOutThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsVOutThreshHiErr.setStatus("current")
_NbsOdsysPsIInActual_Type = NbsTcMilliAmp
_NbsOdsysPsIInActual_Object = MibTableColumn
nbsOdsysPsIInActual = _NbsOdsysPsIInActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 70),
    _NbsOdsysPsIInActual_Type()
)
nbsOdsysPsIInActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInActual.setStatus("current")
_NbsOdsysPsIInLevel_Type = NbsTcStatusLevel
_NbsOdsysPsIInLevel_Object = MibTableColumn
nbsOdsysPsIInLevel = _NbsOdsysPsIInLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 71),
    _NbsOdsysPsIInLevel_Type()
)
nbsOdsysPsIInLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInLevel.setStatus("current")
_NbsOdsysPsIInThreshLoErr_Type = NbsTcMilliAmp
_NbsOdsysPsIInThreshLoErr_Object = MibTableColumn
nbsOdsysPsIInThreshLoErr = _NbsOdsysPsIInThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 72),
    _NbsOdsysPsIInThreshLoErr_Type()
)
nbsOdsysPsIInThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInThreshLoErr.setStatus("current")
_NbsOdsysPsIInThreshLoWarn_Type = NbsTcMilliAmp
_NbsOdsysPsIInThreshLoWarn_Object = MibTableColumn
nbsOdsysPsIInThreshLoWarn = _NbsOdsysPsIInThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 73),
    _NbsOdsysPsIInThreshLoWarn_Type()
)
nbsOdsysPsIInThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInThreshLoWarn.setStatus("current")
_NbsOdsysPsIInThreshHiWarn_Type = NbsTcMilliAmp
_NbsOdsysPsIInThreshHiWarn_Object = MibTableColumn
nbsOdsysPsIInThreshHiWarn = _NbsOdsysPsIInThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 74),
    _NbsOdsysPsIInThreshHiWarn_Type()
)
nbsOdsysPsIInThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInThreshHiWarn.setStatus("current")
_NbsOdsysPsIInThreshHiErr_Type = NbsTcMilliAmp
_NbsOdsysPsIInThreshHiErr_Object = MibTableColumn
nbsOdsysPsIInThreshHiErr = _NbsOdsysPsIInThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 75),
    _NbsOdsysPsIInThreshHiErr_Type()
)
nbsOdsysPsIInThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIInThreshHiErr.setStatus("current")
_NbsOdsysPsIOutActual_Type = NbsTcMilliAmp
_NbsOdsysPsIOutActual_Object = MibTableColumn
nbsOdsysPsIOutActual = _NbsOdsysPsIOutActual_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 80),
    _NbsOdsysPsIOutActual_Type()
)
nbsOdsysPsIOutActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutActual.setStatus("current")
_NbsOdsysPsIOutLevel_Type = NbsTcStatusLevel
_NbsOdsysPsIOutLevel_Object = MibTableColumn
nbsOdsysPsIOutLevel = _NbsOdsysPsIOutLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 81),
    _NbsOdsysPsIOutLevel_Type()
)
nbsOdsysPsIOutLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutLevel.setStatus("current")
_NbsOdsysPsIOutThreshLoErr_Type = NbsTcMilliAmp
_NbsOdsysPsIOutThreshLoErr_Object = MibTableColumn
nbsOdsysPsIOutThreshLoErr = _NbsOdsysPsIOutThreshLoErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 82),
    _NbsOdsysPsIOutThreshLoErr_Type()
)
nbsOdsysPsIOutThreshLoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutThreshLoErr.setStatus("current")
_NbsOdsysPsIOutThreshLoWarn_Type = NbsTcMilliAmp
_NbsOdsysPsIOutThreshLoWarn_Object = MibTableColumn
nbsOdsysPsIOutThreshLoWarn = _NbsOdsysPsIOutThreshLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 83),
    _NbsOdsysPsIOutThreshLoWarn_Type()
)
nbsOdsysPsIOutThreshLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutThreshLoWarn.setStatus("current")
_NbsOdsysPsIOutThreshHiWarn_Type = NbsTcMilliAmp
_NbsOdsysPsIOutThreshHiWarn_Object = MibTableColumn
nbsOdsysPsIOutThreshHiWarn = _NbsOdsysPsIOutThreshHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 84),
    _NbsOdsysPsIOutThreshHiWarn_Type()
)
nbsOdsysPsIOutThreshHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutThreshHiWarn.setStatus("current")
_NbsOdsysPsIOutThreshHiErr_Type = NbsTcMilliAmp
_NbsOdsysPsIOutThreshHiErr_Object = MibTableColumn
nbsOdsysPsIOutThreshHiErr = _NbsOdsysPsIOutThreshHiErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 85),
    _NbsOdsysPsIOutThreshHiErr_Type()
)
nbsOdsysPsIOutThreshHiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOdsysPsIOutThreshHiErr.setStatus("current")
_NbsOdsysEventsGrp_ObjectIdentity = ObjectIdentity
nbsOdsysEventsGrp = _NbsOdsysEventsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 100)
)
if mibBuilder.loadTexts:
    nbsOdsysEventsGrp.setStatus("current")
_NbsOdsysEvents_ObjectIdentity = ObjectIdentity
nbsOdsysEvents = _NbsOdsysEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0)
)
if mibBuilder.loadTexts:
    nbsOdsysEvents.setStatus("current")

# Managed Objects groups


# Notification objects

nbsOdsysTrapCcThermLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 30)
)
nbsOdsysTrapCcThermLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcThermLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapCcThermLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 31)
)
nbsOdsysTrapCcThermLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcThermLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapFtThermLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 40)
)
nbsOdsysTrapFtThermLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapFtThermLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapFtThermLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 41)
)
nbsOdsysTrapFtThermLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysFtThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapFtThermLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapPsThermLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 50)
)
nbsOdsysTrapPsThermLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsThermLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapPsThermLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 51)
)
nbsOdsysTrapPsThermLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsThermActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsThermLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsThermLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapPsVInLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 60)
)
nbsOdsysTrapPsVInLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVInActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVInLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsVInLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapPsVInLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 61)
)
nbsOdsysTrapPsVInLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVInActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVInLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsVInLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapPsVOutLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 70)
)
nbsOdsysTrapPsVOutLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVOutActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVOutLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsVOutLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapPsVOutLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 71)
)
nbsOdsysTrapPsVOutLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVOutActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsVOutLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsVOutLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapPsIInLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 80)
)
nbsOdsysTrapPsIInLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIInActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIInLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsIInLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapPsIInLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 81)
)
nbsOdsysTrapPsIInLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIInActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIInLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsIInLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapPsIOutLevelBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 90)
)
nbsOdsysTrapPsIOutLevelBad.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIOutActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIOutLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsIOutLevelBad.setStatus(
        "current"
    )

nbsOdsysTrapPsIOutLevelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 91)
)
nbsOdsysTrapPsIOutLevelOk.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIOutActual"),
        ("NBS-ODSYS-MIB", "nbsOdsysPsIOutLevel"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapPsIOutLevelOk.setStatus(
        "current"
    )

nbsOdsysTrapCcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 131)
)
nbsOdsysTrapCcFailed.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcFailed.setStatus(
        "current"
    )

nbsOdsysTrapCcRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 132)
)
nbsOdsysTrapCcRestored.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcRestored.setStatus(
        "current"
    )

nbsOdsysTrapCcRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 133)
)
nbsOdsysTrapCcRemoved.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcRemoved.setStatus(
        "current"
    )

nbsOdsysTrapCcInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 134)
)
nbsOdsysTrapCcInserted.setObjects(
      *(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"),
        ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
)
if mibBuilder.loadTexts:
    nbsOdsysTrapCcInserted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-ODSYS-MIB",
    **{"nbsOdsysMib": nbsOdsysMib,
       "nbsOdsysChasGrp": nbsOdsysChasGrp,
       "nbsOdsysChasTable": nbsOdsysChasTable,
       "nbsOdsysChasEntry": nbsOdsysChasEntry,
       "nbsOdsysChasIndex": nbsOdsysChasIndex,
       "nbsOdsysChasCcMaxCount": nbsOdsysChasCcMaxCount,
       "nbsOdsysChasPsMaxCount": nbsOdsysChasPsMaxCount,
       "nbsOdsysChasFtMaxCount": nbsOdsysChasFtMaxCount,
       "nbsOdsysCcGrp": nbsOdsysCcGrp,
       "nbsOdsysCcTable": nbsOdsysCcTable,
       "nbsOdsysCcEntry": nbsOdsysCcEntry,
       "nbsOdsysCcChasIndex": nbsOdsysCcChasIndex,
       "nbsOdsysCcBayIndex": nbsOdsysCcBayIndex,
       "nbsOdsysCcChIfIndex": nbsOdsysCcChIfIndex,
       "nbsOdsysCcPartIndex": nbsOdsysCcPartIndex,
       "nbsOdsysCcThermActual": nbsOdsysCcThermActual,
       "nbsOdsysCcThermLevel": nbsOdsysCcThermLevel,
       "nbsOdsysCcThermThreshLoErr": nbsOdsysCcThermThreshLoErr,
       "nbsOdsysCcThermThreshLoWarn": nbsOdsysCcThermThreshLoWarn,
       "nbsOdsysCcThermThreshHiWarn": nbsOdsysCcThermThreshHiWarn,
       "nbsOdsysCcThermThreshHiErr": nbsOdsysCcThermThreshHiErr,
       "nbsOdsysCcOperationalStatus": nbsOdsysCcOperationalStatus,
       "nbsOdsysFtGrp": nbsOdsysFtGrp,
       "nbsOdsysFtTable": nbsOdsysFtTable,
       "nbsOdsysFtEntry": nbsOdsysFtEntry,
       "nbsOdsysFtChasIndex": nbsOdsysFtChasIndex,
       "nbsOdsysFtBayIndex": nbsOdsysFtBayIndex,
       "nbsOdsysFtOperationalStatus": nbsOdsysFtOperationalStatus,
       "nbsOdsysFtChIfIndex": nbsOdsysFtChIfIndex,
       "nbsOdsysFtPartIndex": nbsOdsysFtPartIndex,
       "nbsOdsysFtFanCount": nbsOdsysFtFanCount,
       "nbsOdsysFtThermActual": nbsOdsysFtThermActual,
       "nbsOdsysFtThermLevel": nbsOdsysFtThermLevel,
       "nbsOdsysFtThermThreshLoErr": nbsOdsysFtThermThreshLoErr,
       "nbsOdsysFtThermThreshLoWarn": nbsOdsysFtThermThreshLoWarn,
       "nbsOdsysFtThermThreshHiWarn": nbsOdsysFtThermThreshHiWarn,
       "nbsOdsysFtThermThreshHiErr": nbsOdsysFtThermThreshHiErr,
       "nbsOdsysPsGrp": nbsOdsysPsGrp,
       "nbsOdsysPsTable": nbsOdsysPsTable,
       "nbsOdsysPsEntry": nbsOdsysPsEntry,
       "nbsOdsysPsChasIndex": nbsOdsysPsChasIndex,
       "nbsOdsysPsBayIndex": nbsOdsysPsBayIndex,
       "nbsOdsysPsOperationalStatus": nbsOdsysPsOperationalStatus,
       "nbsOdsysPsChIfIndex": nbsOdsysPsChIfIndex,
       "nbsOdsysPsPartIndex": nbsOdsysPsPartIndex,
       "nbsOdsysPsFanCount": nbsOdsysPsFanCount,
       "nbsOdsysPsThermActual": nbsOdsysPsThermActual,
       "nbsOdsysPsThermLevel": nbsOdsysPsThermLevel,
       "nbsOdsysPsThermThreshLoErr": nbsOdsysPsThermThreshLoErr,
       "nbsOdsysPsThermThreshLoWarn": nbsOdsysPsThermThreshLoWarn,
       "nbsOdsysPsThermThreshHiWarn": nbsOdsysPsThermThreshHiWarn,
       "nbsOdsysPsThermThreshHiErr": nbsOdsysPsThermThreshHiErr,
       "nbsOdsysPsVInActual": nbsOdsysPsVInActual,
       "nbsOdsysPsVInLevel": nbsOdsysPsVInLevel,
       "nbsOdsysPsVInThreshLoErr": nbsOdsysPsVInThreshLoErr,
       "nbsOdsysPsVInThreshLoWarn": nbsOdsysPsVInThreshLoWarn,
       "nbsOdsysPsVInThreshHiWarn": nbsOdsysPsVInThreshHiWarn,
       "nbsOdsysPsVInThreshHiErr": nbsOdsysPsVInThreshHiErr,
       "nbsOdsysPsVOutActual": nbsOdsysPsVOutActual,
       "nbsOdsysPsVOutLevel": nbsOdsysPsVOutLevel,
       "nbsOdsysPsVOutThreshLoErr": nbsOdsysPsVOutThreshLoErr,
       "nbsOdsysPsVOutThreshLoWarn": nbsOdsysPsVOutThreshLoWarn,
       "nbsOdsysPsVOutThreshHiWarn": nbsOdsysPsVOutThreshHiWarn,
       "nbsOdsysPsVOutThreshHiErr": nbsOdsysPsVOutThreshHiErr,
       "nbsOdsysPsIInActual": nbsOdsysPsIInActual,
       "nbsOdsysPsIInLevel": nbsOdsysPsIInLevel,
       "nbsOdsysPsIInThreshLoErr": nbsOdsysPsIInThreshLoErr,
       "nbsOdsysPsIInThreshLoWarn": nbsOdsysPsIInThreshLoWarn,
       "nbsOdsysPsIInThreshHiWarn": nbsOdsysPsIInThreshHiWarn,
       "nbsOdsysPsIInThreshHiErr": nbsOdsysPsIInThreshHiErr,
       "nbsOdsysPsIOutActual": nbsOdsysPsIOutActual,
       "nbsOdsysPsIOutLevel": nbsOdsysPsIOutLevel,
       "nbsOdsysPsIOutThreshLoErr": nbsOdsysPsIOutThreshLoErr,
       "nbsOdsysPsIOutThreshLoWarn": nbsOdsysPsIOutThreshLoWarn,
       "nbsOdsysPsIOutThreshHiWarn": nbsOdsysPsIOutThreshHiWarn,
       "nbsOdsysPsIOutThreshHiErr": nbsOdsysPsIOutThreshHiErr,
       "nbsOdsysEventsGrp": nbsOdsysEventsGrp,
       "nbsOdsysEvents": nbsOdsysEvents,
       "nbsOdsysTrapCcThermLevelBad": nbsOdsysTrapCcThermLevelBad,
       "nbsOdsysTrapCcThermLevelOk": nbsOdsysTrapCcThermLevelOk,
       "nbsOdsysTrapFtThermLevelBad": nbsOdsysTrapFtThermLevelBad,
       "nbsOdsysTrapFtThermLevelOk": nbsOdsysTrapFtThermLevelOk,
       "nbsOdsysTrapPsThermLevelBad": nbsOdsysTrapPsThermLevelBad,
       "nbsOdsysTrapPsThermLevelOk": nbsOdsysTrapPsThermLevelOk,
       "nbsOdsysTrapPsVInLevelBad": nbsOdsysTrapPsVInLevelBad,
       "nbsOdsysTrapPsVInLevelOk": nbsOdsysTrapPsVInLevelOk,
       "nbsOdsysTrapPsVOutLevelBad": nbsOdsysTrapPsVOutLevelBad,
       "nbsOdsysTrapPsVOutLevelOk": nbsOdsysTrapPsVOutLevelOk,
       "nbsOdsysTrapPsIInLevelBad": nbsOdsysTrapPsIInLevelBad,
       "nbsOdsysTrapPsIInLevelOk": nbsOdsysTrapPsIInLevelOk,
       "nbsOdsysTrapPsIOutLevelBad": nbsOdsysTrapPsIOutLevelBad,
       "nbsOdsysTrapPsIOutLevelOk": nbsOdsysTrapPsIOutLevelOk,
       "nbsOdsysTrapCcFailed": nbsOdsysTrapCcFailed,
       "nbsOdsysTrapCcRestored": nbsOdsysTrapCcRestored,
       "nbsOdsysTrapCcRemoved": nbsOdsysTrapCcRemoved,
       "nbsOdsysTrapCcInserted": nbsOdsysTrapCcInserted}
)
