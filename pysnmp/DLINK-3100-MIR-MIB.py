# SNMP MIB module (DLINK-3100-MIR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-MIR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:08 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

rlMir = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61)
)
rlMir.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlMirMibVersion_Type = Integer32
_RlMirMibVersion_Object = MibScalar
rlMirMibVersion = _RlMirMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 1),
    _RlMirMibVersion_Type()
)
rlMirMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMirMibVersion.setStatus("current")


class _RlMirMaxNumOfMRIsAfterReset_Type(Integer32):
    """Custom type rlMirMaxNumOfMRIsAfterReset based on Integer32"""
    defaultValue = 1


_RlMirMaxNumOfMRIsAfterReset_Object = MibScalar
rlMirMaxNumOfMRIsAfterReset = _RlMirMaxNumOfMRIsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 2),
    _RlMirMaxNumOfMRIsAfterReset_Type()
)
rlMirMaxNumOfMRIsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirMaxNumOfMRIsAfterReset.setStatus("current")
_RlMirMaxNumOfMRIs_Type = Integer32
_RlMirMaxNumOfMRIs_Object = MibScalar
rlMirMaxNumOfMRIs = _RlMirMaxNumOfMRIs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 3),
    _RlMirMaxNumOfMRIs_Type()
)
rlMirMaxNumOfMRIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMirMaxNumOfMRIs.setStatus("current")
_RlMirCurMriNum_Type = Integer32
_RlMirCurMriNum_Object = MibScalar
rlMirCurMriNum = _RlMirCurMriNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 4),
    _RlMirCurMriNum_Type()
)
rlMirCurMriNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirCurMriNum.setStatus("current")
_RlMirInterfaceTable_Object = MibTable
rlMirInterfaceTable = _RlMirInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5)
)
if mibBuilder.loadTexts:
    rlMirInterfaceTable.setStatus("current")
_RlMirInterfaceEntry_Object = MibTableRow
rlMirInterfaceEntry = _RlMirInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1)
)
rlMirInterfaceEntry.setIndexNames(
    (0, "DLINK-3100-MIR-MIB", "rlMirInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirInterfaceEntry.setStatus("current")
_RlMirInterfaceIfIndex_Type = InterfaceIndex
_RlMirInterfaceIfIndex_Object = MibTableColumn
rlMirInterfaceIfIndex = _RlMirInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1, 1),
    _RlMirInterfaceIfIndex_Type()
)
rlMirInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirInterfaceIfIndex.setStatus("current")


class _RlMirInterfaceMrid_Type(Integer32):
    """Custom type rlMirInterfaceMrid based on Integer32"""
    defaultValue = 0


_RlMirInterfaceMrid_Object = MibTableColumn
rlMirInterfaceMrid = _RlMirInterfaceMrid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1, 2),
    _RlMirInterfaceMrid_Type()
)
rlMirInterfaceMrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirInterfaceMrid.setStatus("current")
_RlMirVlanBaseReservedPortsTable_Object = MibTable
rlMirVlanBaseReservedPortsTable = _RlMirVlanBaseReservedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6)
)
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsTable.setStatus("current")
_RlMirVlanBaseReservedPortsEntry_Object = MibTableRow
rlMirVlanBaseReservedPortsEntry = _RlMirVlanBaseReservedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1)
)
rlMirVlanBaseReservedPortsEntry.setIndexNames(
    (0, "DLINK-3100-MIR-MIB", "rlMirVlanBaseReservedPortsIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsEntry.setStatus("current")
_RlMirVlanBaseReservedPortsIfIndex_Type = InterfaceIndex
_RlMirVlanBaseReservedPortsIfIndex_Object = MibTableColumn
rlMirVlanBaseReservedPortsIfIndex = _RlMirVlanBaseReservedPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1, 1),
    _RlMirVlanBaseReservedPortsIfIndex_Type()
)
rlMirVlanBaseReservedPortsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsIfIndex.setStatus("current")
_RlMirVlanBaseReservedPortsStatus_Type = RowStatus
_RlMirVlanBaseReservedPortsStatus_Object = MibTableColumn
rlMirVlanBaseReservedPortsStatus = _RlMirVlanBaseReservedPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1, 2),
    _RlMirVlanBaseReservedPortsStatus_Type()
)
rlMirVlanBaseReservedPortsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsStatus.setStatus("current")
_RlMirVlanBaseLogicalPortsTable_Object = MibTable
rlMirVlanBaseLogicalPortsTable = _RlMirVlanBaseLogicalPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7)
)
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsTable.setStatus("current")
_RlMirVlanBaseLogicalPortsEntry_Object = MibTableRow
rlMirVlanBaseLogicalPortsEntry = _RlMirVlanBaseLogicalPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1)
)
rlMirVlanBaseLogicalPortsEntry.setIndexNames(
    (0, "DLINK-3100-MIR-MIB", "rlMirVlanBaseLogicalPortsIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsEntry.setStatus("current")
_RlMirVlanBaseLogicalPortsIfIndex_Type = InterfaceIndex
_RlMirVlanBaseLogicalPortsIfIndex_Object = MibTableColumn
rlMirVlanBaseLogicalPortsIfIndex = _RlMirVlanBaseLogicalPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 1),
    _RlMirVlanBaseLogicalPortsIfIndex_Type()
)
rlMirVlanBaseLogicalPortsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsIfIndex.setStatus("current")
_RlMirVlanBaseLogicalPortsReservedIfIndex_Type = InterfaceIndex
_RlMirVlanBaseLogicalPortsReservedIfIndex_Object = MibTableColumn
rlMirVlanBaseLogicalPortsReservedIfIndex = _RlMirVlanBaseLogicalPortsReservedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 2),
    _RlMirVlanBaseLogicalPortsReservedIfIndex_Type()
)
rlMirVlanBaseLogicalPortsReservedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsReservedIfIndex.setStatus("current")


class _RlMirVlanBaseLogicalPortsVlanTag_Type(Integer32):
    """Custom type rlMirVlanBaseLogicalPortsVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RlMirVlanBaseLogicalPortsVlanTag_Type.__name__ = "Integer32"
_RlMirVlanBaseLogicalPortsVlanTag_Object = MibTableColumn
rlMirVlanBaseLogicalPortsVlanTag = _RlMirVlanBaseLogicalPortsVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 3),
    _RlMirVlanBaseLogicalPortsVlanTag_Type()
)
rlMirVlanBaseLogicalPortsVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsVlanTag.setStatus("current")
_RlMirVlanBaseLogicalPortsStatus_Type = RowStatus
_RlMirVlanBaseLogicalPortsStatus_Object = MibTableColumn
rlMirVlanBaseLogicalPortsStatus = _RlMirVlanBaseLogicalPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 4),
    _RlMirVlanBaseLogicalPortsStatus_Type()
)
rlMirVlanBaseLogicalPortsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-MIR-MIB",
    **{"rlMir": rlMir,
       "rlMirMibVersion": rlMirMibVersion,
       "rlMirMaxNumOfMRIsAfterReset": rlMirMaxNumOfMRIsAfterReset,
       "rlMirMaxNumOfMRIs": rlMirMaxNumOfMRIs,
       "rlMirCurMriNum": rlMirCurMriNum,
       "rlMirInterfaceTable": rlMirInterfaceTable,
       "rlMirInterfaceEntry": rlMirInterfaceEntry,
       "rlMirInterfaceIfIndex": rlMirInterfaceIfIndex,
       "rlMirInterfaceMrid": rlMirInterfaceMrid,
       "rlMirVlanBaseReservedPortsTable": rlMirVlanBaseReservedPortsTable,
       "rlMirVlanBaseReservedPortsEntry": rlMirVlanBaseReservedPortsEntry,
       "rlMirVlanBaseReservedPortsIfIndex": rlMirVlanBaseReservedPortsIfIndex,
       "rlMirVlanBaseReservedPortsStatus": rlMirVlanBaseReservedPortsStatus,
       "rlMirVlanBaseLogicalPortsTable": rlMirVlanBaseLogicalPortsTable,
       "rlMirVlanBaseLogicalPortsEntry": rlMirVlanBaseLogicalPortsEntry,
       "rlMirVlanBaseLogicalPortsIfIndex": rlMirVlanBaseLogicalPortsIfIndex,
       "rlMirVlanBaseLogicalPortsReservedIfIndex": rlMirVlanBaseLogicalPortsReservedIfIndex,
       "rlMirVlanBaseLogicalPortsVlanTag": rlMirVlanBaseLogicalPortsVlanTag,
       "rlMirVlanBaseLogicalPortsStatus": rlMirVlanBaseLogicalPortsStatus}
)
