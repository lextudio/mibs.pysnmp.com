# SNMP MIB module (PORTGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PORTGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:17 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

swPortGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPortGroupMIBObjects_ObjectIdentity = ObjectIdentity
swPortGroupMIBObjects = _SwPortGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1)
)
_SwPortGroupTable_Object = MibTable
swPortGroupTable = _SwPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1)
)
if mibBuilder.loadTexts:
    swPortGroupTable.setStatus("current")
_SwPortGroupEntry_Object = MibTableRow
swPortGroupEntry = _SwPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1)
)
swPortGroupEntry.setIndexNames(
    (0, "PORTGROUP-MIB", "swPortGroupID"),
)
if mibBuilder.loadTexts:
    swPortGroupEntry.setStatus("current")
_SwPortGroupID_Type = Integer32
_SwPortGroupID_Object = MibTableColumn
swPortGroupID = _SwPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 1),
    _SwPortGroupID_Type()
)
swPortGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortGroupID.setStatus("current")
_SwPortGroupRowStatus_Type = RowStatus
_SwPortGroupRowStatus_Object = MibTableColumn
swPortGroupRowStatus = _SwPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 2),
    _SwPortGroupRowStatus_Type()
)
swPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortGroupRowStatus.setStatus("current")


class _SwPortGroupName_Type(DisplayString):
    """Custom type swPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwPortGroupName_Type.__name__ = "DisplayString"
_SwPortGroupName_Object = MibTableColumn
swPortGroupName = _SwPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 3),
    _SwPortGroupName_Type()
)
swPortGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortGroupName.setStatus("current")
_SwPortGroupPorts_Type = PortList
_SwPortGroupPorts_Object = MibTableColumn
swPortGroupPorts = _SwPortGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 88, 1, 1, 1, 4),
    _SwPortGroupPorts_Type()
)
swPortGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortGroupPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PORTGROUP-MIB",
    **{"swPortGroupMIB": swPortGroupMIB,
       "swPortGroupMIBObjects": swPortGroupMIBObjects,
       "swPortGroupTable": swPortGroupTable,
       "swPortGroupEntry": swPortGroupEntry,
       "swPortGroupID": swPortGroupID,
       "swPortGroupRowStatus": swPortGroupRowStatus,
       "swPortGroupName": swPortGroupName,
       "swPortGroupPorts": swPortGroupPorts}
)
