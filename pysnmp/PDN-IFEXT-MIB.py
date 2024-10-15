# SNMP MIB module (PDN-IFEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-IFEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:44 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnIfExt,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnIfExt")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnIfExtConfig_ObjectIdentity = ObjectIdentity
pdnIfExtConfig = _PdnIfExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1)
)
_PdnIfExtTable_Object = MibTable
pdnIfExtTable = _PdnIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIfExtTable.setStatus("mandatory")
_PdnIfExtEntry_Object = MibTableRow
pdnIfExtEntry = _PdnIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1, 1)
)
pdnIfExtEntry.setIndexNames(
    (0, "PDN-IFEXT-MIB", "pdnIfExtIndex"),
)
if mibBuilder.loadTexts:
    pdnIfExtEntry.setStatus("mandatory")
_PdnIfExtIndex_Type = Integer32
_PdnIfExtIndex_Object = MibTableColumn
pdnIfExtIndex = _PdnIfExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1, 1, 1),
    _PdnIfExtIndex_Type()
)
pdnIfExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfExtIndex.setStatus("mandatory")
_PdnIfExtInOctetRollovers_Type = Counter32
_PdnIfExtInOctetRollovers_Object = MibTableColumn
pdnIfExtInOctetRollovers = _PdnIfExtInOctetRollovers_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1, 1, 2),
    _PdnIfExtInOctetRollovers_Type()
)
pdnIfExtInOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfExtInOctetRollovers.setStatus("mandatory")
_PdnIfExtOutOctetRollovers_Type = Counter32
_PdnIfExtOutOctetRollovers_Object = MibTableColumn
pdnIfExtOutOctetRollovers = _PdnIfExtOutOctetRollovers_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1, 1, 3),
    _PdnIfExtOutOctetRollovers_Type()
)
pdnIfExtOutOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfExtOutOctetRollovers.setStatus("mandatory")
_PdnIfExtTotalUASs_Type = Counter32
_PdnIfExtTotalUASs_Object = MibTableColumn
pdnIfExtTotalUASs = _PdnIfExtTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 1, 1, 4),
    _PdnIfExtTotalUASs_Type()
)
pdnIfExtTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfExtTotalUASs.setStatus("mandatory")
_PdnIfTable_Object = MibTable
pdnIfTable = _PdnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 2)
)
if mibBuilder.loadTexts:
    pdnIfTable.setStatus("mandatory")
_PdnIfEntry_Object = MibTableRow
pdnIfEntry = _PdnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 2, 1)
)
pdnIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-IFEXT-MIB", "pdnIfAddr"),
)
if mibBuilder.loadTexts:
    pdnIfEntry.setStatus("mandatory")
_PdnIfAddr_Type = IpAddress
_PdnIfAddr_Object = MibTableColumn
pdnIfAddr = _PdnIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 2, 1, 1),
    _PdnIfAddr_Type()
)
pdnIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfAddr.setStatus("mandatory")
_PdnIfAddrMask_Type = IpAddress
_PdnIfAddrMask_Object = MibTableColumn
pdnIfAddrMask = _PdnIfAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 2, 1, 2),
    _PdnIfAddrMask_Type()
)
pdnIfAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfAddrMask.setStatus("mandatory")
_PdnIfStatus_Type = RowStatus
_PdnIfStatus_Object = MibTableColumn
pdnIfStatus = _PdnIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 2, 1, 3),
    _PdnIfStatus_Type()
)
pdnIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfStatus.setStatus("mandatory")
_PdnIfExtTestConfig_ObjectIdentity = ObjectIdentity
pdnIfExtTestConfig = _PdnIfExtTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2)
)
_PdnIfExtTestConfigTable_Object = MibTable
pdnIfExtTestConfigTable = _PdnIfExtTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2, 1)
)
if mibBuilder.loadTexts:
    pdnIfExtTestConfigTable.setStatus("mandatory")
_PdnIfExtTestConfigEntry_Object = MibTableRow
pdnIfExtTestConfigEntry = _PdnIfExtTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2, 1, 1)
)
pdnIfExtTestConfigEntry.setIndexNames(
    (0, "PDN-IFEXT-MIB", "pdnIfExtTestConfigIfIndex"),
)
if mibBuilder.loadTexts:
    pdnIfExtTestConfigEntry.setStatus("mandatory")
_PdnIfExtTestConfigIfIndex_Type = Integer32
_PdnIfExtTestConfigIfIndex_Object = MibTableColumn
pdnIfExtTestConfigIfIndex = _PdnIfExtTestConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2, 1, 1, 1),
    _PdnIfExtTestConfigIfIndex_Type()
)
pdnIfExtTestConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfExtTestConfigIfIndex.setStatus("mandatory")
_PdnIfExtTestConfigNearTimer_Type = Integer32
_PdnIfExtTestConfigNearTimer_Object = MibTableColumn
pdnIfExtTestConfigNearTimer = _PdnIfExtTestConfigNearTimer_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2, 1, 1, 2),
    _PdnIfExtTestConfigNearTimer_Type()
)
pdnIfExtTestConfigNearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfExtTestConfigNearTimer.setStatus("mandatory")
_PdnIfExtTestConfigFarTimer_Type = Integer32
_PdnIfExtTestConfigFarTimer_Object = MibTableColumn
pdnIfExtTestConfigFarTimer = _PdnIfExtTestConfigFarTimer_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 2, 1, 1, 3),
    _PdnIfExtTestConfigFarTimer_Type()
)
pdnIfExtTestConfigFarTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfExtTestConfigFarTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-IFEXT-MIB",
    **{"pdnIfExtConfig": pdnIfExtConfig,
       "pdnIfExtTable": pdnIfExtTable,
       "pdnIfExtEntry": pdnIfExtEntry,
       "pdnIfExtIndex": pdnIfExtIndex,
       "pdnIfExtInOctetRollovers": pdnIfExtInOctetRollovers,
       "pdnIfExtOutOctetRollovers": pdnIfExtOutOctetRollovers,
       "pdnIfExtTotalUASs": pdnIfExtTotalUASs,
       "pdnIfTable": pdnIfTable,
       "pdnIfEntry": pdnIfEntry,
       "pdnIfAddr": pdnIfAddr,
       "pdnIfAddrMask": pdnIfAddrMask,
       "pdnIfStatus": pdnIfStatus,
       "pdnIfExtTestConfig": pdnIfExtTestConfig,
       "pdnIfExtTestConfigTable": pdnIfExtTestConfigTable,
       "pdnIfExtTestConfigEntry": pdnIfExtTestConfigEntry,
       "pdnIfExtTestConfigIfIndex": pdnIfExtTestConfigIfIndex,
       "pdnIfExtTestConfigNearTimer": pdnIfExtTestConfigNearTimer,
       "pdnIfExtTestConfigFarTimer": pdnIfExtTestConfigFarTimer}
)
