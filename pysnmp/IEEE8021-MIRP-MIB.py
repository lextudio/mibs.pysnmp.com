# SNMP MIB module (IEEE8021-MIRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-MIRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:25 2024
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

(ieee8021BridgeBasePortEntry,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePortEntry")

(ieee8021PbbBackboneEdgeBridgeObjects,) = mibBuilder.importSymbols(
    "IEEE8021-PBB-MIB",
    "ieee8021PbbBackboneEdgeBridgeObjects")

(IEEE8021BridgePortNumberOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumberOrZero")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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

ieee8021MirpMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 23)
)
ieee8021MirpMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-04-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Ieee8021PbbMirpEnableStatus_Type(TruthValue):
    """Custom type ieee8021PbbMirpEnableStatus based on TruthValue"""


_Ieee8021PbbMirpEnableStatus_Object = MibScalar
ieee8021PbbMirpEnableStatus = _Ieee8021PbbMirpEnableStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 7),
    _Ieee8021PbbMirpEnableStatus_Type()
)
ieee8021PbbMirpEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbMirpEnableStatus.setStatus("current")


class _Ieee8021PbbMirpBvid_Type(VlanIdOrNone):
    """Custom type ieee8021PbbMirpBvid based on VlanIdOrNone"""
    defaultValue = 0


_Ieee8021PbbMirpBvid_Object = MibScalar
ieee8021PbbMirpBvid = _Ieee8021PbbMirpBvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 8),
    _Ieee8021PbbMirpBvid_Type()
)
ieee8021PbbMirpBvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbMirpBvid.setStatus("current")


class _Ieee8021PbbMirpDestSelector_Type(Integer32):
    """Custom type ieee8021PbbMirpDestSelector based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbpMirpGroup", 1),
          ("cbpMirpTable", 3),
          ("cbpMirpVlan", 2))
    )


_Ieee8021PbbMirpDestSelector_Type.__name__ = "Integer32"
_Ieee8021PbbMirpDestSelector_Object = MibScalar
ieee8021PbbMirpDestSelector = _Ieee8021PbbMirpDestSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 9),
    _Ieee8021PbbMirpDestSelector_Type()
)
ieee8021PbbMirpDestSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbMirpDestSelector.setStatus("current")


class _Ieee8021PbbMirpPnpEnable_Type(TruthValue):
    """Custom type ieee8021PbbMirpPnpEnable based on TruthValue"""


_Ieee8021PbbMirpPnpEnable_Object = MibScalar
ieee8021PbbMirpPnpEnable = _Ieee8021PbbMirpPnpEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 10),
    _Ieee8021PbbMirpPnpEnable_Type()
)
ieee8021PbbMirpPnpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbMirpPnpEnable.setStatus("current")


class _Ieee8021PbbMirpPnpPortNumber_Type(IEEE8021BridgePortNumberOrZero):
    """Custom type ieee8021PbbMirpPnpPortNumber based on IEEE8021BridgePortNumberOrZero"""
    defaultValue = 0


_Ieee8021PbbMirpPnpPortNumber_Object = MibScalar
ieee8021PbbMirpPnpPortNumber = _Ieee8021PbbMirpPnpPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 11),
    _Ieee8021PbbMirpPnpPortNumber_Type()
)
ieee8021PbbMirpPnpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbMirpPnpPortNumber.setStatus("current")
_Ieee8021MirpV2MIBObjects_ObjectIdentity = ObjectIdentity
ieee8021MirpV2MIBObjects = _Ieee8021MirpV2MIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 23, 1)
)
_Ieee8021MirpV2PortTable_Object = MibTable
ieee8021MirpV2PortTable = _Ieee8021MirpV2PortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MirpV2PortTable.setStatus("current")
_Ieee8021MirpV2PortEntry_Object = MibTableRow
ieee8021MirpV2PortEntry = _Ieee8021MirpV2PortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MirpV2PortEntry.setStatus("current")


class _Ieee8021MirpV2PortEnabledStatus_Type(TruthValue):
    """Custom type ieee8021MirpV2PortEnabledStatus based on TruthValue"""


_Ieee8021MirpV2PortEnabledStatus_Object = MibTableColumn
ieee8021MirpV2PortEnabledStatus = _Ieee8021MirpV2PortEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1, 1),
    _Ieee8021MirpV2PortEnabledStatus_Type()
)
ieee8021MirpV2PortEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MirpV2PortEnabledStatus.setStatus("current")
_Ieee8021MirpV2Conformance_ObjectIdentity = ObjectIdentity
ieee8021MirpV2Conformance = _Ieee8021MirpV2Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 23, 2)
)
_Ieee8021MirpV2Compliances_ObjectIdentity = ObjectIdentity
ieee8021MirpV2Compliances = _Ieee8021MirpV2Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 23, 2, 1)
)
_Ieee8021MirpV2Groups_ObjectIdentity = ObjectIdentity
ieee8021MirpV2Groups = _Ieee8021MirpV2Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 23, 2, 2)
)
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-MIRP-MIB",
     "ieee8021MirpV2PortEntry")
)
ieee8021MirpV2PortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

ieee8021MirpV2ReqdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 23, 2, 2, 1)
)
ieee8021MirpV2ReqdGroup.setObjects(
      *(("IEEE8021-MIRP-MIB", "ieee8021MirpV2PortEnabledStatus"),
        ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpEnableStatus"),
        ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpBvid"),
        ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpDestSelector"),
        ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpEnable"),
        ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpPortNumber"))
)
if mibBuilder.loadTexts:
    ieee8021MirpV2ReqdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021MirpV2BridgeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MirpV2BridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-MIRP-MIB",
    **{"ieee8021PbbMirpEnableStatus": ieee8021PbbMirpEnableStatus,
       "ieee8021PbbMirpBvid": ieee8021PbbMirpBvid,
       "ieee8021PbbMirpDestSelector": ieee8021PbbMirpDestSelector,
       "ieee8021PbbMirpPnpEnable": ieee8021PbbMirpPnpEnable,
       "ieee8021PbbMirpPnpPortNumber": ieee8021PbbMirpPnpPortNumber,
       "ieee8021MirpMib": ieee8021MirpMib,
       "ieee8021MirpV2MIBObjects": ieee8021MirpV2MIBObjects,
       "ieee8021MirpV2PortTable": ieee8021MirpV2PortTable,
       "ieee8021MirpV2PortEntry": ieee8021MirpV2PortEntry,
       "ieee8021MirpV2PortEnabledStatus": ieee8021MirpV2PortEnabledStatus,
       "ieee8021MirpV2Conformance": ieee8021MirpV2Conformance,
       "ieee8021MirpV2Compliances": ieee8021MirpV2Compliances,
       "ieee8021MirpV2BridgeCompliance": ieee8021MirpV2BridgeCompliance,
       "ieee8021MirpV2Groups": ieee8021MirpV2Groups,
       "ieee8021MirpV2ReqdGroup": ieee8021MirpV2ReqdGroup}
)
