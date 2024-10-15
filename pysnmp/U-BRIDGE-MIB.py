# SNMP MIB module (U-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/U-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:12 2024
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge")

(dot1dGmrp,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "dot1dGmrp")

(dot1qPvid,
 dot1qVlan) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qPvid",
    "dot1qVlan")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

uBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 17, 12)
)
uBridgeMIB.setRevisions(
        ("2001-11-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot1dExtPortGmrpTable_Object = MibTable
dot1dExtPortGmrpTable = _Dot1dExtPortGmrpTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot1dExtPortGmrpTable.setStatus("current")
_Dot1dExtPortGmrpEntry_Object = MibTableRow
dot1dExtPortGmrpEntry = _Dot1dExtPortGmrpEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dExtPortGmrpEntry.setStatus("current")


class _Dot1dPortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type dot1dPortRestrictedGroupRegistration based on TruthValue"""


_Dot1dPortRestrictedGroupRegistration_Object = MibTableColumn
dot1dPortRestrictedGroupRegistration = _Dot1dPortRestrictedGroupRegistration_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 1),
    _Dot1dPortRestrictedGroupRegistration_Type()
)
dot1dPortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortRestrictedGroupRegistration.setStatus("current")
_Dot1dPortLastGroupFailed_Type = MacAddress
_Dot1dPortLastGroupFailed_Object = MibTableColumn
dot1dPortLastGroupFailed = _Dot1dPortLastGroupFailed_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 2),
    _Dot1dPortLastGroupFailed_Type()
)
dot1dPortLastGroupFailed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dot1dPortLastGroupFailed.setStatus("current")


class _Dot1dPortGmrpFailingReason_Type(Integer32):
    """Custom type dot1dPortGmrpFailingReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lackOfResources", 1),
          ("registrationRestricted", 2))
    )


_Dot1dPortGmrpFailingReason_Type.__name__ = "Integer32"
_Dot1dPortGmrpFailingReason_Object = MibTableColumn
dot1dPortGmrpFailingReason = _Dot1dPortGmrpFailingReason_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 3),
    _Dot1dPortGmrpFailingReason_Type()
)
dot1dPortGmrpFailingReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dot1dPortGmrpFailingReason.setStatus("current")
_Dot1qExtPortVlanTable_Object = MibTable
dot1qExtPortVlanTable = _Dot1qExtPortVlanTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11)
)
if mibBuilder.loadTexts:
    dot1qExtPortVlanTable.setStatus("current")
_Dot1qExtPortVlanEntry_Object = MibTableRow
dot1qExtPortVlanEntry = _Dot1qExtPortVlanEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    dot1qExtPortVlanEntry.setStatus("current")


class _Dot1qPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type dot1qPortRestrictedVlanRegistration based on TruthValue"""


_Dot1qPortRestrictedVlanRegistration_Object = MibTableColumn
dot1qPortRestrictedVlanRegistration = _Dot1qPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 1),
    _Dot1qPortRestrictedVlanRegistration_Type()
)
dot1qPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortRestrictedVlanRegistration.setStatus("current")


class _Dot1qPortGvrpFailingReason_Type(Integer32):
    """Custom type dot1qPortGvrpFailingReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lackOfResources", 1),
          ("registrationRestricted", 2),
          ("unsupportedVID", 3))
    )


_Dot1qPortGvrpFailingReason_Type.__name__ = "Integer32"
_Dot1qPortGvrpFailingReason_Object = MibTableColumn
dot1qPortGvrpFailingReason = _Dot1qPortGvrpFailingReason_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 2),
    _Dot1qPortGvrpFailingReason_Type()
)
dot1qPortGvrpFailingReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dot1qPortGvrpFailingReason.setStatus("current")
_UBridgeConformance_ObjectIdentity = ObjectIdentity
uBridgeConformance = _UBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 12, 1)
)
_UBridgeGroups_ObjectIdentity = ObjectIdentity
uBridgeGroups = _UBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 1)
)
_UBridgeCompliances_ObjectIdentity = ObjectIdentity
uBridgeCompliances = _UBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("U-BRIDGE-MIB",
     "dot1dExtPortGmrpEntry")
)
dot1dExtPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("U-BRIDGE-MIB",
     "dot1qExtPortVlanEntry")
)
dot1qExtPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

uBridgePortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 1)
)
uBridgePortVlanGroup.setObjects(
      *(("U-BRIDGE-MIB", "dot1qPortRestrictedVlanRegistration"),
        ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
)
if mibBuilder.loadTexts:
    uBridgePortVlanGroup.setStatus("current")

uBridgePortGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 2)
)
uBridgePortGmrpGroup.setObjects(
      *(("U-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"),
        ("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"),
        ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
)
if mibBuilder.loadTexts:
    uBridgePortGmrpGroup.setStatus("current")


# Notification objects

gmrpFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 3)
)
gmrpFailure.setObjects(
      *(("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"),
        ("BRIDGE-MIB", "dot1dBasePort"),
        ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
)
if mibBuilder.loadTexts:
    gmrpFailure.setStatus(
        "current"
    )

gvrpFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 4)
)
gvrpFailure.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qPvid"),
        ("BRIDGE-MIB", "dot1dBasePort"),
        ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
)
if mibBuilder.loadTexts:
    gvrpFailure.setStatus(
        "current"
    )


# Notifications groups

uBridgeTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 3)
)
uBridgeTrapGroup.setObjects(
      *(("U-BRIDGE-MIB", "gmrpFailure"),
        ("U-BRIDGE-MIB", "gvrpFailure"))
)
if mibBuilder.loadTexts:
    uBridgeTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

uBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    uBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "U-BRIDGE-MIB",
    **{"gmrpFailure": gmrpFailure,
       "gvrpFailure": gvrpFailure,
       "dot1dExtPortGmrpTable": dot1dExtPortGmrpTable,
       "dot1dExtPortGmrpEntry": dot1dExtPortGmrpEntry,
       "dot1dPortRestrictedGroupRegistration": dot1dPortRestrictedGroupRegistration,
       "dot1dPortLastGroupFailed": dot1dPortLastGroupFailed,
       "dot1dPortGmrpFailingReason": dot1dPortGmrpFailingReason,
       "dot1qExtPortVlanTable": dot1qExtPortVlanTable,
       "dot1qExtPortVlanEntry": dot1qExtPortVlanEntry,
       "dot1qPortRestrictedVlanRegistration": dot1qPortRestrictedVlanRegistration,
       "dot1qPortGvrpFailingReason": dot1qPortGvrpFailingReason,
       "uBridgeMIB": uBridgeMIB,
       "uBridgeConformance": uBridgeConformance,
       "uBridgeGroups": uBridgeGroups,
       "uBridgePortVlanGroup": uBridgePortVlanGroup,
       "uBridgePortGmrpGroup": uBridgePortGmrpGroup,
       "uBridgeTrapGroup": uBridgeTrapGroup,
       "uBridgeCompliances": uBridgeCompliances,
       "uBridgeCompliance": uBridgeCompliance}
)
