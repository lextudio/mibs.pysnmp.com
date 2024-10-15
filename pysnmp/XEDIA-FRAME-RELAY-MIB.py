# SNMP MIB module (XEDIA-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:51 2024
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

(frCircuitEntry,) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XfrObjects_ObjectIdentity = ObjectIdentity
xfrObjects = _XfrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1)
)
_XfrArpTable_Object = MibTable
xfrArpTable = _XfrArpTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1)
)
if mibBuilder.loadTexts:
    xfrArpTable.setStatus("current")
_XfrArpEntry_Object = MibTableRow
xfrArpEntry = _XfrArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1)
)
xfrArpEntry.setIndexNames(
    (0, "XEDIA-FRAME-RELAY-MIB", "xfrArpIfIndex"),
    (0, "XEDIA-FRAME-RELAY-MIB", "xfrArpNetAddress"),
)
if mibBuilder.loadTexts:
    xfrArpEntry.setStatus("current")


class _XfrArpIfIndex_Type(Integer32):
    """Custom type xfrArpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XfrArpIfIndex_Type.__name__ = "Integer32"
_XfrArpIfIndex_Object = MibTableColumn
xfrArpIfIndex = _XfrArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 1),
    _XfrArpIfIndex_Type()
)
xfrArpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xfrArpIfIndex.setStatus("current")
_XfrArpNetAddress_Type = IpAddress
_XfrArpNetAddress_Object = MibTableColumn
xfrArpNetAddress = _XfrArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 2),
    _XfrArpNetAddress_Type()
)
xfrArpNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xfrArpNetAddress.setStatus("current")


class _XfrArpType_Type(Integer32):
    """Custom type xfrArpType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_XfrArpType_Type.__name__ = "Integer32"
_XfrArpType_Object = MibTableColumn
xfrArpType = _XfrArpType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 3),
    _XfrArpType_Type()
)
xfrArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xfrArpType.setStatus("current")


class _XfrArpDlci_Type(Integer32):
    """Custom type xfrArpDlci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_XfrArpDlci_Type.__name__ = "Integer32"
_XfrArpDlci_Object = MibTableColumn
xfrArpDlci = _XfrArpDlci_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 4),
    _XfrArpDlci_Type()
)
xfrArpDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xfrArpDlci.setStatus("current")
_XfrArpIfStack_Type = DisplayString
_XfrArpIfStack_Object = MibTableColumn
xfrArpIfStack = _XfrArpIfStack_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 5),
    _XfrArpIfStack_Type()
)
xfrArpIfStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfrArpIfStack.setStatus("current")
_XFrCircuitTable_Object = MibTable
xFrCircuitTable = _XFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2)
)
if mibBuilder.loadTexts:
    xFrCircuitTable.setStatus("current")
_XFrCircuitEntry_Object = MibTableRow
xFrCircuitEntry = _XFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xFrCircuitEntry.setStatus("current")


class _XfrCircuitType_Type(Integer32):
    """Custom type xfrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_XfrCircuitType_Type.__name__ = "Integer32"
_XfrCircuitType_Object = MibTableColumn
xfrCircuitType = _XfrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2, 1, 1),
    _XfrCircuitType_Type()
)
xfrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfrCircuitType.setStatus("current")
_XfrNotifications_ObjectIdentity = ObjectIdentity
xfrNotifications = _XfrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 2)
)
_XfrConformance_ObjectIdentity = ObjectIdentity
xfrConformance = _XfrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 3)
)
_XfrCompliances_ObjectIdentity = ObjectIdentity
xfrCompliances = _XfrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 1)
)
_XfrGroups_ObjectIdentity = ObjectIdentity
xfrGroups = _XfrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 2)
)
frCircuitEntry.registerAugmentions(
    ("XEDIA-FRAME-RELAY-MIB",
     "xFrCircuitEntry")
)
xFrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

xfrAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 2, 1)
)
xfrAllGroup.setObjects(
      *(("XEDIA-FRAME-RELAY-MIB", "xfrArpIfIndex"),
        ("XEDIA-FRAME-RELAY-MIB", "xfrArpNetAddress"),
        ("XEDIA-FRAME-RELAY-MIB", "xfrArpDlci"),
        ("XEDIA-FRAME-RELAY-MIB", "xfrArpIfStack"),
        ("XEDIA-FRAME-RELAY-MIB", "xfrArpType"),
        ("XEDIA-FRAME-RELAY-MIB", "xfrCircuitType"))
)
if mibBuilder.loadTexts:
    xfrAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xfrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-FRAME-RELAY-MIB",
    **{"xediaFrameRelayMIB": xediaFrameRelayMIB,
       "xfrObjects": xfrObjects,
       "xfrArpTable": xfrArpTable,
       "xfrArpEntry": xfrArpEntry,
       "xfrArpIfIndex": xfrArpIfIndex,
       "xfrArpNetAddress": xfrArpNetAddress,
       "xfrArpType": xfrArpType,
       "xfrArpDlci": xfrArpDlci,
       "xfrArpIfStack": xfrArpIfStack,
       "xFrCircuitTable": xFrCircuitTable,
       "xFrCircuitEntry": xFrCircuitEntry,
       "xfrCircuitType": xfrCircuitType,
       "xfrNotifications": xfrNotifications,
       "xfrConformance": xfrConformance,
       "xfrCompliances": xfrCompliances,
       "xfrCompliance": xfrCompliance,
       "xfrGroups": xfrGroups,
       "xfrAllGroup": xfrAllGroup}
)
