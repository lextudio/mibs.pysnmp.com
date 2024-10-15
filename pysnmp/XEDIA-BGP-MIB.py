# SNMP MIB module (XEDIA-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:43 2024
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

(bgp4PathAttrEntry,
 bgpPeerEntry) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrEntry",
    "bgpPeerEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XbgpObjects_ObjectIdentity = ObjectIdentity
xbgpObjects = _XbgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1)
)


class _XbgpAdminStatus_Type(Integer32):
    """Custom type xbgpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XbgpAdminStatus_Type.__name__ = "Integer32"
_XbgpAdminStatus_Object = MibScalar
xbgpAdminStatus = _XbgpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 1),
    _XbgpAdminStatus_Type()
)
xbgpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpAdminStatus.setStatus("current")


class _XbgpOperStatus_Type(Integer32):
    """Custom type xbgpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XbgpOperStatus_Type.__name__ = "Integer32"
_XbgpOperStatus_Object = MibScalar
xbgpOperStatus = _XbgpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 2),
    _XbgpOperStatus_Type()
)
xbgpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgpOperStatus.setStatus("current")


class _XbgpReflection_Type(Integer32):
    """Custom type xbgpReflection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("noClientToClient", 2),
          ("none", 3))
    )


_XbgpReflection_Type.__name__ = "Integer32"
_XbgpReflection_Object = MibScalar
xbgpReflection = _XbgpReflection_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 3),
    _XbgpReflection_Type()
)
xbgpReflection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpReflection.setStatus("current")


class _XbgpClusterId_Type(Integer32):
    """Custom type xbgpClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XbgpClusterId_Type.__name__ = "Integer32"
_XbgpClusterId_Object = MibScalar
xbgpClusterId = _XbgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 4),
    _XbgpClusterId_Type()
)
xbgpClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpClusterId.setStatus("current")


class _XbgpConfiguredMaxRoutes_Type(Integer32):
    """Custom type xbgpConfiguredMaxRoutes based on Integer32"""
    defaultValue = 81920

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_XbgpConfiguredMaxRoutes_Type.__name__ = "Integer32"
_XbgpConfiguredMaxRoutes_Object = MibScalar
xbgpConfiguredMaxRoutes = _XbgpConfiguredMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 5),
    _XbgpConfiguredMaxRoutes_Type()
)
xbgpConfiguredMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpConfiguredMaxRoutes.setStatus("current")


class _XbgpOperationalMaxRoutes_Type(Integer32):
    """Custom type xbgpOperationalMaxRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_XbgpOperationalMaxRoutes_Type.__name__ = "Integer32"
_XbgpOperationalMaxRoutes_Object = MibScalar
xbgpOperationalMaxRoutes = _XbgpOperationalMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 6),
    _XbgpOperationalMaxRoutes_Type()
)
xbgpOperationalMaxRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgpOperationalMaxRoutes.setStatus("current")


class _XbgpConfiguredMaxPaths_Type(Integer32):
    """Custom type xbgpConfiguredMaxPaths based on Integer32"""
    defaultValue = 20480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_XbgpConfiguredMaxPaths_Type.__name__ = "Integer32"
_XbgpConfiguredMaxPaths_Object = MibScalar
xbgpConfiguredMaxPaths = _XbgpConfiguredMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 7),
    _XbgpConfiguredMaxPaths_Type()
)
xbgpConfiguredMaxPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpConfiguredMaxPaths.setStatus("current")


class _XbgpOperationalMaxPaths_Type(Integer32):
    """Custom type xbgpOperationalMaxPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_XbgpOperationalMaxPaths_Type.__name__ = "Integer32"
_XbgpOperationalMaxPaths_Object = MibScalar
xbgpOperationalMaxPaths = _XbgpOperationalMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 8),
    _XbgpOperationalMaxPaths_Type()
)
xbgpOperationalMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgpOperationalMaxPaths.setStatus("current")
_XBgpPeerTable_Object = MibTable
xBgpPeerTable = _XBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 10)
)
if mibBuilder.loadTexts:
    xBgpPeerTable.setStatus("current")
_XBgpPeerEntry_Object = MibTableRow
xBgpPeerEntry = _XBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 10, 1)
)
if mibBuilder.loadTexts:
    xBgpPeerEntry.setStatus("current")
_XbgpPeerRowStatus_Type = RowStatus
_XbgpPeerRowStatus_Object = MibTableColumn
xbgpPeerRowStatus = _XbgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 10, 1, 1),
    _XbgpPeerRowStatus_Type()
)
xbgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpPeerRowStatus.setStatus("current")


class _XbgpPeerReflectionClient_Type(TruthValue):
    """Custom type xbgpPeerReflectionClient based on TruthValue"""


_XbgpPeerReflectionClient_Object = MibTableColumn
xbgpPeerReflectionClient = _XbgpPeerReflectionClient_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 10, 1, 2),
    _XbgpPeerReflectionClient_Type()
)
xbgpPeerReflectionClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xbgpPeerReflectionClient.setStatus("current")
_XBgp4PathAttrTable_Object = MibTable
xBgp4PathAttrTable = _XBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11)
)
if mibBuilder.loadTexts:
    xBgp4PathAttrTable.setStatus("current")
_XBgp4PathAttrEntry_Object = MibTableRow
xBgp4PathAttrEntry = _XBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11, 1)
)
if mibBuilder.loadTexts:
    xBgp4PathAttrEntry.setStatus("current")


class _Xbgp4PathAttrCommunity_Type(OctetString):
    """Custom type xbgp4PathAttrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Xbgp4PathAttrCommunity_Type.__name__ = "OctetString"
_Xbgp4PathAttrCommunity_Object = MibTableColumn
xbgp4PathAttrCommunity = _Xbgp4PathAttrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11, 1, 1),
    _Xbgp4PathAttrCommunity_Type()
)
xbgp4PathAttrCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgp4PathAttrCommunity.setStatus("current")
_Xbgp4PathAttrOrigId_Type = IpAddress
_Xbgp4PathAttrOrigId_Object = MibTableColumn
xbgp4PathAttrOrigId = _Xbgp4PathAttrOrigId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11, 1, 2),
    _Xbgp4PathAttrOrigId_Type()
)
xbgp4PathAttrOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgp4PathAttrOrigId.setStatus("current")


class _Xbgp4PathAttrClusterList_Type(OctetString):
    """Custom type xbgp4PathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Xbgp4PathAttrClusterList_Type.__name__ = "OctetString"
_Xbgp4PathAttrClusterList_Object = MibTableColumn
xbgp4PathAttrClusterList = _Xbgp4PathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11, 1, 3),
    _Xbgp4PathAttrClusterList_Type()
)
xbgp4PathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgp4PathAttrClusterList.setStatus("current")


class _Xbgp4PathAttrDistance_Type(Integer32):
    """Custom type xbgp4PathAttrDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xbgp4PathAttrDistance_Type.__name__ = "Integer32"
_Xbgp4PathAttrDistance_Object = MibTableColumn
xbgp4PathAttrDistance = _Xbgp4PathAttrDistance_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 11, 1, 4),
    _Xbgp4PathAttrDistance_Type()
)
xbgp4PathAttrDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgp4PathAttrDistance.setStatus("current")
_XbgpConfiguredPeers_Type = Integer32
_XbgpConfiguredPeers_Object = MibScalar
xbgpConfiguredPeers = _XbgpConfiguredPeers_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 12),
    _XbgpConfiguredPeers_Type()
)
xbgpConfiguredPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgpConfiguredPeers.setStatus("current")
_XbgpEstablishedPeers_Type = Integer32
_XbgpEstablishedPeers_Object = MibScalar
xbgpEstablishedPeers = _XbgpEstablishedPeers_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 1, 13),
    _XbgpEstablishedPeers_Type()
)
xbgpEstablishedPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xbgpEstablishedPeers.setStatus("current")
_XbgpConformance_ObjectIdentity = ObjectIdentity
xbgpConformance = _XbgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 2)
)
_XbgpCompliances_ObjectIdentity = ObjectIdentity
xbgpCompliances = _XbgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 2, 1)
)
_XbgpGroups_ObjectIdentity = ObjectIdentity
xbgpGroups = _XbgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 2, 2)
)
bgpPeerEntry.registerAugmentions(
    ("XEDIA-BGP-MIB",
     "xBgpPeerEntry")
)
xBgpPeerEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgp4PathAttrEntry.registerAugmentions(
    ("XEDIA-BGP-MIB",
     "xBgp4PathAttrEntry")
)
xBgp4PathAttrEntry.setIndexNames(*bgp4PathAttrEntry.getIndexNames())

# Managed Objects groups

xbgpAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 2, 2, 1)
)
xbgpAllGroup.setObjects(
      *(("XEDIA-BGP-MIB", "xbgpAdminStatus"),
        ("XEDIA-BGP-MIB", "xbgpOperStatus"),
        ("XEDIA-BGP-MIB", "xbgpReflection"),
        ("XEDIA-BGP-MIB", "xbgpClusterId"),
        ("XEDIA-BGP-MIB", "xbgpConfiguredMaxRoutes"),
        ("XEDIA-BGP-MIB", "xbgpOperationalMaxRoutes"),
        ("XEDIA-BGP-MIB", "xbgpConfiguredMaxPaths"),
        ("XEDIA-BGP-MIB", "xbgpOperationalMaxPaths"),
        ("XEDIA-BGP-MIB", "xbgpConfiguredPeers"),
        ("XEDIA-BGP-MIB", "xbgpEstablishedPeers"),
        ("XEDIA-BGP-MIB", "xbgpPeerRowStatus"),
        ("XEDIA-BGP-MIB", "xbgpPeerReflectionClient"),
        ("XEDIA-BGP-MIB", "xbgp4PathAttrCommunity"),
        ("XEDIA-BGP-MIB", "xbgp4PathAttrOrigId"),
        ("XEDIA-BGP-MIB", "xbgp4PathAttrClusterList"),
        ("XEDIA-BGP-MIB", "xbgp4PathAttrDistance"))
)
if mibBuilder.loadTexts:
    xbgpAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xbgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xbgpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-BGP-MIB",
    **{"xediaBgpMIB": xediaBgpMIB,
       "xbgpObjects": xbgpObjects,
       "xbgpAdminStatus": xbgpAdminStatus,
       "xbgpOperStatus": xbgpOperStatus,
       "xbgpReflection": xbgpReflection,
       "xbgpClusterId": xbgpClusterId,
       "xbgpConfiguredMaxRoutes": xbgpConfiguredMaxRoutes,
       "xbgpOperationalMaxRoutes": xbgpOperationalMaxRoutes,
       "xbgpConfiguredMaxPaths": xbgpConfiguredMaxPaths,
       "xbgpOperationalMaxPaths": xbgpOperationalMaxPaths,
       "xBgpPeerTable": xBgpPeerTable,
       "xBgpPeerEntry": xBgpPeerEntry,
       "xbgpPeerRowStatus": xbgpPeerRowStatus,
       "xbgpPeerReflectionClient": xbgpPeerReflectionClient,
       "xBgp4PathAttrTable": xBgp4PathAttrTable,
       "xBgp4PathAttrEntry": xBgp4PathAttrEntry,
       "xbgp4PathAttrCommunity": xbgp4PathAttrCommunity,
       "xbgp4PathAttrOrigId": xbgp4PathAttrOrigId,
       "xbgp4PathAttrClusterList": xbgp4PathAttrClusterList,
       "xbgp4PathAttrDistance": xbgp4PathAttrDistance,
       "xbgpConfiguredPeers": xbgpConfiguredPeers,
       "xbgpEstablishedPeers": xbgpEstablishedPeers,
       "xbgpConformance": xbgpConformance,
       "xbgpCompliances": xbgpCompliances,
       "xbgpCompliance": xbgpCompliance,
       "xbgpGroups": xbgpGroups,
       "xbgpAllGroup": xbgpAllGroup}
)
