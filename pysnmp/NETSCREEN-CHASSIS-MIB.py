# SNMP MIB module (NETSCREEN-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:44 2024
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

(netscreen,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreen")

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

netscreenChassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsPowerTable_Object = MibTable
nsPowerTable = _NsPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 1)
)
if mibBuilder.loadTexts:
    nsPowerTable.setStatus("current")
_NsPowerEntry_Object = MibTableRow
nsPowerEntry = _NsPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 1, 1)
)
nsPowerEntry.setIndexNames(
    (0, "NETSCREEN-CHASSIS-MIB", "nsPowerId"),
)
if mibBuilder.loadTexts:
    nsPowerEntry.setStatus("current")
_NsPowerId_Type = Integer32
_NsPowerId_Object = MibTableColumn
nsPowerId = _NsPowerId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 1, 1, 1),
    _NsPowerId_Type()
)
nsPowerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPowerId.setStatus("current")
_NsPowerStatus_Type = Integer32
_NsPowerStatus_Object = MibTableColumn
nsPowerStatus = _NsPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 1, 1, 2),
    _NsPowerStatus_Type()
)
nsPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPowerStatus.setStatus("current")
_NsPowerDesc_Type = DisplayString
_NsPowerDesc_Object = MibTableColumn
nsPowerDesc = _NsPowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 1, 1, 3),
    _NsPowerDesc_Type()
)
nsPowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPowerDesc.setStatus("current")
_NsFanTable_Object = MibTable
nsFanTable = _NsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 2)
)
if mibBuilder.loadTexts:
    nsFanTable.setStatus("current")
_NsFanEntry_Object = MibTableRow
nsFanEntry = _NsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 2, 1)
)
nsFanEntry.setIndexNames(
    (0, "NETSCREEN-CHASSIS-MIB", "nsFanId"),
)
if mibBuilder.loadTexts:
    nsFanEntry.setStatus("current")
_NsFanId_Type = Integer32
_NsFanId_Object = MibTableColumn
nsFanId = _NsFanId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 2, 1, 1),
    _NsFanId_Type()
)
nsFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFanId.setStatus("current")
_NsFanStatus_Type = Integer32
_NsFanStatus_Object = MibTableColumn
nsFanStatus = _NsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 2, 1, 2),
    _NsFanStatus_Type()
)
nsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFanStatus.setStatus("current")
_NsFanDesc_Type = DisplayString
_NsFanDesc_Object = MibTableColumn
nsFanDesc = _NsFanDesc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 2, 1, 3),
    _NsFanDesc_Type()
)
nsFanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFanDesc.setStatus("current")
_SysBatteryStatus_Type = Integer32
_SysBatteryStatus_Object = MibScalar
sysBatteryStatus = _SysBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 3),
    _SysBatteryStatus_Type()
)
sysBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBatteryStatus.setStatus("current")
_NsTemperatureTable_Object = MibTable
nsTemperatureTable = _NsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4)
)
if mibBuilder.loadTexts:
    nsTemperatureTable.setStatus("current")
_NsTemperatureEntry_Object = MibTableRow
nsTemperatureEntry = _NsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4, 1)
)
nsTemperatureEntry.setIndexNames(
    (0, "NETSCREEN-CHASSIS-MIB", "nsTemperatureId"),
)
if mibBuilder.loadTexts:
    nsTemperatureEntry.setStatus("current")
_NsTemperatureId_Type = Integer32
_NsTemperatureId_Object = MibTableColumn
nsTemperatureId = _NsTemperatureId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4, 1, 1),
    _NsTemperatureId_Type()
)
nsTemperatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTemperatureId.setStatus("current")
_NsTemperatureSlotId_Type = Integer32
_NsTemperatureSlotId_Object = MibTableColumn
nsTemperatureSlotId = _NsTemperatureSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4, 1, 2),
    _NsTemperatureSlotId_Type()
)
nsTemperatureSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTemperatureSlotId.setStatus("current")
_NsTemperatureCur_Type = Integer32
_NsTemperatureCur_Object = MibTableColumn
nsTemperatureCur = _NsTemperatureCur_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4, 1, 3),
    _NsTemperatureCur_Type()
)
nsTemperatureCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTemperatureCur.setStatus("current")
_NsTemperatureDesc_Type = DisplayString
_NsTemperatureDesc_Object = MibTableColumn
nsTemperatureDesc = _NsTemperatureDesc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 4, 1, 4),
    _NsTemperatureDesc_Type()
)
nsTemperatureDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTemperatureDesc.setStatus("current")
_NsSlotTable_Object = MibTable
nsSlotTable = _NsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5)
)
if mibBuilder.loadTexts:
    nsSlotTable.setStatus("current")
_NsSlotEntry_Object = MibTableRow
nsSlotEntry = _NsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5, 1)
)
nsSlotEntry.setIndexNames(
    (0, "NETSCREEN-CHASSIS-MIB", "nsSlotId"),
    (0, "NETSCREEN-CHASSIS-MIB", "nsSubSlotId"),
)
if mibBuilder.loadTexts:
    nsSlotEntry.setStatus("current")
_NsSlotId_Type = Integer32
_NsSlotId_Object = MibTableColumn
nsSlotId = _NsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5, 1, 1),
    _NsSlotId_Type()
)
nsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSlotId.setStatus("current")
_NsSlotType_Type = DisplayString
_NsSlotType_Object = MibTableColumn
nsSlotType = _NsSlotType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5, 1, 2),
    _NsSlotType_Type()
)
nsSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSlotType.setStatus("current")
_NsSlotStatus_Type = Integer32
_NsSlotStatus_Object = MibTableColumn
nsSlotStatus = _NsSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5, 1, 3),
    _NsSlotStatus_Type()
)
nsSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSlotStatus.setStatus("current")
_NsSlotSN_Type = DisplayString
_NsSlotSN_Object = MibTableColumn
nsSlotSN = _NsSlotSN_Object(
    (1, 3, 6, 1, 4, 1, 3224, 21, 5, 1, 4),
    _NsSlotSN_Type()
)
nsSlotSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSlotSN.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-CHASSIS-MIB",
    **{"netscreenChassis": netscreenChassis,
       "nsPowerTable": nsPowerTable,
       "nsPowerEntry": nsPowerEntry,
       "nsPowerId": nsPowerId,
       "nsPowerStatus": nsPowerStatus,
       "nsPowerDesc": nsPowerDesc,
       "nsFanTable": nsFanTable,
       "nsFanEntry": nsFanEntry,
       "nsFanId": nsFanId,
       "nsFanStatus": nsFanStatus,
       "nsFanDesc": nsFanDesc,
       "sysBatteryStatus": sysBatteryStatus,
       "nsTemperatureTable": nsTemperatureTable,
       "nsTemperatureEntry": nsTemperatureEntry,
       "nsTemperatureId": nsTemperatureId,
       "nsTemperatureSlotId": nsTemperatureSlotId,
       "nsTemperatureCur": nsTemperatureCur,
       "nsTemperatureDesc": nsTemperatureDesc,
       "nsSlotTable": nsSlotTable,
       "nsSlotEntry": nsSlotEntry,
       "nsSlotId": nsSlotId,
       "nsSlotType": nsSlotType,
       "nsSlotStatus": nsSlotStatus,
       "nsSlotSN": nsSlotSN}
)
