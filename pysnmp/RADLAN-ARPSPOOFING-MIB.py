# SNMP MIB module (RADLAN-ARPSPOOFING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-ARPSPOOFING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:37 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlArpSpoofing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 60)
)
rlArpSpoofing.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlArpSpoofingMibVersion_Type = Integer32
_RlArpSpoofingMibVersion_Object = MibScalar
rlArpSpoofingMibVersion = _RlArpSpoofingMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 1),
    _RlArpSpoofingMibVersion_Type()
)
rlArpSpoofingMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlArpSpoofingMibVersion.setStatus("current")
_RlArpSpoofingTable_Object = MibTable
rlArpSpoofingTable = _RlArpSpoofingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2)
)
if mibBuilder.loadTexts:
    rlArpSpoofingTable.setStatus("current")
_RlArpSpoofingEntry_Object = MibTableRow
rlArpSpoofingEntry = _RlArpSpoofingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1)
)
rlArpSpoofingEntry.setIndexNames(
    (0, "RADLAN-ARPSPOOFING-MIB", "rlArpSpoofingIfIndex"),
    (0, "RADLAN-ARPSPOOFING-MIB", "rlArpSpoofingLocalIpAddr"),
)
if mibBuilder.loadTexts:
    rlArpSpoofingEntry.setStatus("current")
_RlArpSpoofingIfIndex_Type = InterfaceIndex
_RlArpSpoofingIfIndex_Object = MibTableColumn
rlArpSpoofingIfIndex = _RlArpSpoofingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 1),
    _RlArpSpoofingIfIndex_Type()
)
rlArpSpoofingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingIfIndex.setStatus("current")
_RlArpSpoofingLocalIpAddr_Type = IpAddress
_RlArpSpoofingLocalIpAddr_Object = MibTableColumn
rlArpSpoofingLocalIpAddr = _RlArpSpoofingLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 2),
    _RlArpSpoofingLocalIpAddr_Type()
)
rlArpSpoofingLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingLocalIpAddr.setStatus("current")
_RlArpSpoofingMacAddr_Type = PhysAddress
_RlArpSpoofingMacAddr_Object = MibTableColumn
rlArpSpoofingMacAddr = _RlArpSpoofingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 3),
    _RlArpSpoofingMacAddr_Type()
)
rlArpSpoofingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingMacAddr.setStatus("current")
_RlArpSpoofingRemoteIpAddr_Type = IpAddress
_RlArpSpoofingRemoteIpAddr_Object = MibTableColumn
rlArpSpoofingRemoteIpAddr = _RlArpSpoofingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 4),
    _RlArpSpoofingRemoteIpAddr_Type()
)
rlArpSpoofingRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingRemoteIpAddr.setStatus("current")


class _RlArpSpoofingOutPhysIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlArpSpoofingOutPhysIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlArpSpoofingOutPhysIfIndex_Object = MibTableColumn
rlArpSpoofingOutPhysIfIndex = _RlArpSpoofingOutPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 5),
    _RlArpSpoofingOutPhysIfIndex_Type()
)
rlArpSpoofingOutPhysIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingOutPhysIfIndex.setStatus("current")
_RlArpSpoofingStatus_Type = RowStatus
_RlArpSpoofingStatus_Object = MibTableColumn
rlArpSpoofingStatus = _RlArpSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 6),
    _RlArpSpoofingStatus_Type()
)
rlArpSpoofingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-ARPSPOOFING-MIB",
    **{"rlArpSpoofing": rlArpSpoofing,
       "rlArpSpoofingMibVersion": rlArpSpoofingMibVersion,
       "rlArpSpoofingTable": rlArpSpoofingTable,
       "rlArpSpoofingEntry": rlArpSpoofingEntry,
       "rlArpSpoofingIfIndex": rlArpSpoofingIfIndex,
       "rlArpSpoofingLocalIpAddr": rlArpSpoofingLocalIpAddr,
       "rlArpSpoofingMacAddr": rlArpSpoofingMacAddr,
       "rlArpSpoofingRemoteIpAddr": rlArpSpoofingRemoteIpAddr,
       "rlArpSpoofingOutPhysIfIndex": rlArpSpoofingOutPhysIfIndex,
       "rlArpSpoofingStatus": rlArpSpoofingStatus}
)
