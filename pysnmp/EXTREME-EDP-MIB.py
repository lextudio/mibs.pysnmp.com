# SNMP MIB module (EXTREME-EDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(ExtremeDeviceId,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ExtremeDeviceId",
    "extremeAgent")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeEdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEdpTable_Object = MibTable
extremeEdpTable = _ExtremeEdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2)
)
if mibBuilder.loadTexts:
    extremeEdpTable.setStatus("current")
_ExtremeEdpEntry_Object = MibTableRow
extremeEdpEntry = _ExtremeEdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1)
)
extremeEdpEntry.setIndexNames(
    (0, "EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
    (0, "EXTREME-EDP-MIB", "extremeEdpNeighborId"),
)
if mibBuilder.loadTexts:
    extremeEdpEntry.setStatus("current")


class _ExtremeEdpPortIfIndex_Type(Integer32):
    """Custom type extremeEdpPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEdpPortIfIndex_Type.__name__ = "Integer32"
_ExtremeEdpPortIfIndex_Object = MibTableColumn
extremeEdpPortIfIndex = _ExtremeEdpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 1),
    _ExtremeEdpPortIfIndex_Type()
)
extremeEdpPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEdpPortIfIndex.setStatus("current")
_ExtremeEdpNeighborId_Type = ExtremeDeviceId
_ExtremeEdpNeighborId_Object = MibTableColumn
extremeEdpNeighborId = _ExtremeEdpNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 2),
    _ExtremeEdpNeighborId_Type()
)
extremeEdpNeighborId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEdpNeighborId.setStatus("current")
_ExtremeEdpNeighborName_Type = DisplayString
_ExtremeEdpNeighborName_Object = MibTableColumn
extremeEdpNeighborName = _ExtremeEdpNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 3),
    _ExtremeEdpNeighborName_Type()
)
extremeEdpNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborName.setStatus("current")
_ExtremeEdpNeighborSoftwareVersion_Type = DisplayString
_ExtremeEdpNeighborSoftwareVersion_Object = MibTableColumn
extremeEdpNeighborSoftwareVersion = _ExtremeEdpNeighborSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 4),
    _ExtremeEdpNeighborSoftwareVersion_Type()
)
extremeEdpNeighborSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborSoftwareVersion.setStatus("current")
_ExtremeEdpNeighborSlot_Type = Integer32
_ExtremeEdpNeighborSlot_Object = MibTableColumn
extremeEdpNeighborSlot = _ExtremeEdpNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 5),
    _ExtremeEdpNeighborSlot_Type()
)
extremeEdpNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborSlot.setStatus("current")
_ExtremeEdpNeighborPort_Type = Integer32
_ExtremeEdpNeighborPort_Object = MibTableColumn
extremeEdpNeighborPort = _ExtremeEdpNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 6),
    _ExtremeEdpNeighborPort_Type()
)
extremeEdpNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborPort.setStatus("current")
_ExtremeEdpEntryAge_Type = Integer32
_ExtremeEdpEntryAge_Object = MibTableColumn
extremeEdpEntryAge = _ExtremeEdpEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 2, 1, 7),
    _ExtremeEdpEntryAge_Type()
)
extremeEdpEntryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpEntryAge.setStatus("current")
_ExtremeEdpNeighborTable_Object = MibTable
extremeEdpNeighborTable = _ExtremeEdpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 3)
)
if mibBuilder.loadTexts:
    extremeEdpNeighborTable.setStatus("current")
_ExtremeEdpNeighborEntry_Object = MibTableRow
extremeEdpNeighborEntry = _ExtremeEdpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 3, 1)
)
extremeEdpNeighborEntry.setIndexNames(
    (0, "EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
    (0, "EXTREME-EDP-MIB", "extremeEdpNeighborId"),
    (0, "EXTREME-EDP-MIB", "extremeEdpNeighborVlanName"),
)
if mibBuilder.loadTexts:
    extremeEdpNeighborEntry.setStatus("current")


class _ExtremeEdpNeighborVlanName_Type(DisplayString):
    """Custom type extremeEdpNeighborVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeEdpNeighborVlanName_Type.__name__ = "DisplayString"
_ExtremeEdpNeighborVlanName_Object = MibTableColumn
extremeEdpNeighborVlanName = _ExtremeEdpNeighborVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 3, 1, 1),
    _ExtremeEdpNeighborVlanName_Type()
)
extremeEdpNeighborVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEdpNeighborVlanName.setStatus("current")
_ExtremeEdpNeighborVlanId_Type = Integer32
_ExtremeEdpNeighborVlanId_Object = MibTableColumn
extremeEdpNeighborVlanId = _ExtremeEdpNeighborVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 3, 1, 2),
    _ExtremeEdpNeighborVlanId_Type()
)
extremeEdpNeighborVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborVlanId.setStatus("current")
_ExtremeEdpNeighborVlanIpAddress_Type = IpAddress
_ExtremeEdpNeighborVlanIpAddress_Object = MibTableColumn
extremeEdpNeighborVlanIpAddress = _ExtremeEdpNeighborVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 3, 1, 3),
    _ExtremeEdpNeighborVlanIpAddress_Type()
)
extremeEdpNeighborVlanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEdpNeighborVlanIpAddress.setStatus("current")
_ExtremeEdpPortTable_Object = MibTable
extremeEdpPortTable = _ExtremeEdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 4)
)
if mibBuilder.loadTexts:
    extremeEdpPortTable.setStatus("current")
_ExtremeEdpPortEntry_Object = MibTableRow
extremeEdpPortEntry = _ExtremeEdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 4, 1)
)
extremeEdpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeEdpPortEntry.setStatus("current")
_ExtremeEdpPortState_Type = TruthValue
_ExtremeEdpPortState_Object = MibTableColumn
extremeEdpPortState = _ExtremeEdpPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13, 4, 1, 1),
    _ExtremeEdpPortState_Type()
)
extremeEdpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEdpPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-EDP-MIB",
    **{"extremeEdp": extremeEdp,
       "extremeEdpTable": extremeEdpTable,
       "extremeEdpEntry": extremeEdpEntry,
       "extremeEdpPortIfIndex": extremeEdpPortIfIndex,
       "extremeEdpNeighborId": extremeEdpNeighborId,
       "extremeEdpNeighborName": extremeEdpNeighborName,
       "extremeEdpNeighborSoftwareVersion": extremeEdpNeighborSoftwareVersion,
       "extremeEdpNeighborSlot": extremeEdpNeighborSlot,
       "extremeEdpNeighborPort": extremeEdpNeighborPort,
       "extremeEdpEntryAge": extremeEdpEntryAge,
       "extremeEdpNeighborTable": extremeEdpNeighborTable,
       "extremeEdpNeighborEntry": extremeEdpNeighborEntry,
       "extremeEdpNeighborVlanName": extremeEdpNeighborVlanName,
       "extremeEdpNeighborVlanId": extremeEdpNeighborVlanId,
       "extremeEdpNeighborVlanIpAddress": extremeEdpNeighborVlanIpAddress,
       "extremeEdpPortTable": extremeEdpPortTable,
       "extremeEdpPortEntry": extremeEdpPortEntry,
       "extremeEdpPortState": extremeEdpPortState}
)
