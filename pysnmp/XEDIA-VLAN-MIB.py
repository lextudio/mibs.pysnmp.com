# SNMP MIB module (XEDIA-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:10 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 34)
)


# Types definitions



class Unsigned32(Gauge32):
    """Custom type Unsigned32 based on Gauge32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XVlanObjects_ObjectIdentity = ObjectIdentity
xVlanObjects = _XVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1)
)
_XVlanIDTable_Object = MibTable
xVlanIDTable = _XVlanIDTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1)
)
if mibBuilder.loadTexts:
    xVlanIDTable.setStatus("current")
_XVlanIDEntry_Object = MibTableRow
xVlanIDEntry = _XVlanIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1, 1)
)
xVlanIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xVlanIDEntry.setStatus("current")


class _XVlanID_Type(Unsigned32):
    """Custom type xVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_XVlanID_Type.__name__ = "Unsigned32"
_XVlanID_Object = MibTableColumn
xVlanID = _XVlanID_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1, 1, 1),
    _XVlanID_Type()
)
xVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xVlanID.setStatus("current")
_XVlanConfigTable_Object = MibTable
xVlanConfigTable = _XVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2)
)
if mibBuilder.loadTexts:
    xVlanConfigTable.setStatus("current")
_XVlanConfigEntry_Object = MibTableRow
xVlanConfigEntry = _XVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1)
)
xVlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xVlanConfigEntry.setStatus("current")


class _XVlanConfigAdmitTaggedFrames_Type(TruthValue):
    """Custom type xVlanConfigAdmitTaggedFrames based on TruthValue"""


_XVlanConfigAdmitTaggedFrames_Object = MibTableColumn
xVlanConfigAdmitTaggedFrames = _XVlanConfigAdmitTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 1),
    _XVlanConfigAdmitTaggedFrames_Type()
)
xVlanConfigAdmitTaggedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVlanConfigAdmitTaggedFrames.setStatus("current")


class _XVlanConfigAdmitConfiguredVlansOnly_Type(TruthValue):
    """Custom type xVlanConfigAdmitConfiguredVlansOnly based on TruthValue"""


_XVlanConfigAdmitConfiguredVlansOnly_Object = MibTableColumn
xVlanConfigAdmitConfiguredVlansOnly = _XVlanConfigAdmitConfiguredVlansOnly_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 2),
    _XVlanConfigAdmitConfiguredVlansOnly_Type()
)
xVlanConfigAdmitConfiguredVlansOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVlanConfigAdmitConfiguredVlansOnly.setStatus("current")


class _XVlanConfigStripBridgedTags_Type(TruthValue):
    """Custom type xVlanConfigStripBridgedTags based on TruthValue"""


_XVlanConfigStripBridgedTags_Object = MibTableColumn
xVlanConfigStripBridgedTags = _XVlanConfigStripBridgedTags_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 3),
    _XVlanConfigStripBridgedTags_Type()
)
xVlanConfigStripBridgedTags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVlanConfigStripBridgedTags.setStatus("current")


class _XVlanConfigGVRP_Type(TruthValue):
    """Custom type xVlanConfigGVRP based on TruthValue"""


_XVlanConfigGVRP_Object = MibTableColumn
xVlanConfigGVRP = _XVlanConfigGVRP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 4),
    _XVlanConfigGVRP_Type()
)
xVlanConfigGVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVlanConfigGVRP.setStatus("current")


class _XVlanConfigGARPJoinTime_Type(Integer32):
    """Custom type xVlanConfigGARPJoinTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21474800),
    )


_XVlanConfigGARPJoinTime_Type.__name__ = "Integer32"
_XVlanConfigGARPJoinTime_Object = MibTableColumn
xVlanConfigGARPJoinTime = _XVlanConfigGARPJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 5),
    _XVlanConfigGARPJoinTime_Type()
)
xVlanConfigGARPJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVlanConfigGARPJoinTime.setStatus("current")
_XVlanConformance_ObjectIdentity = ObjectIdentity
xVlanConformance = _XVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 2)
)
_XVlanCompliances_ObjectIdentity = ObjectIdentity
xVlanCompliances = _XVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 1)
)
_XVlanGroups_ObjectIdentity = ObjectIdentity
xVlanGroups = _XVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 2)
)

# Managed Objects groups

xVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 2, 1)
)
xVlanGroup.setObjects(
      *(("XEDIA-VLAN-MIB", "xVlanID"),
        ("XEDIA-VLAN-MIB", "xVlanConfigAdmitTaggedFrames"),
        ("XEDIA-VLAN-MIB", "xVlanConfigAdmitConfiguredVlansOnly"),
        ("XEDIA-VLAN-MIB", "xVlanConfigStripBridgedTags"),
        ("XEDIA-VLAN-MIB", "xVlanConfigGVRP"),
        ("XEDIA-VLAN-MIB", "xVlanConfigGARPJoinTime"))
)
if mibBuilder.loadTexts:
    xVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-VLAN-MIB",
    **{"Unsigned32": Unsigned32,
       "xediaVlanMIB": xediaVlanMIB,
       "xVlanObjects": xVlanObjects,
       "xVlanIDTable": xVlanIDTable,
       "xVlanIDEntry": xVlanIDEntry,
       "xVlanID": xVlanID,
       "xVlanConfigTable": xVlanConfigTable,
       "xVlanConfigEntry": xVlanConfigEntry,
       "xVlanConfigAdmitTaggedFrames": xVlanConfigAdmitTaggedFrames,
       "xVlanConfigAdmitConfiguredVlansOnly": xVlanConfigAdmitConfiguredVlansOnly,
       "xVlanConfigStripBridgedTags": xVlanConfigStripBridgedTags,
       "xVlanConfigGVRP": xVlanConfigGVRP,
       "xVlanConfigGARPJoinTime": xVlanConfigGARPJoinTime,
       "xVlanConformance": xVlanConformance,
       "xVlanCompliances": xVlanCompliances,
       "xVlanCompliance": xVlanCompliance,
       "xVlanGroups": xVlanGroups,
       "xVlanGroup": xVlanGroup}
)
