# SNMP MIB module (Unisphere-Data-IP-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IP-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:54 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdName,
 UsdSetMap) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdName",
    "UsdSetMap")


# MODULE-IDENTITY

usdIpProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26)
)
usdIpProfileMIB.setRevisions(
        ("2001-01-24 20:06",
         "2000-05-08 00:00",
         "1999-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdIpProfileObjects_ObjectIdentity = ObjectIdentity
usdIpProfileObjects = _UsdIpProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1)
)
_UsdIpProfile_ObjectIdentity = ObjectIdentity
usdIpProfile = _UsdIpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1)
)
_UsdIpProfileTable_Object = MibTable
usdIpProfileTable = _UsdIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpProfileTable.setStatus("current")
_UsdIpProfileEntry_Object = MibTableRow
usdIpProfileEntry = _UsdIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1)
)
usdIpProfileEntry.setIndexNames(
    (0, "Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileId"),
)
if mibBuilder.loadTexts:
    usdIpProfileEntry.setStatus("current")
_UsdIpProfileId_Type = Unsigned32
_UsdIpProfileId_Object = MibTableColumn
usdIpProfileId = _UsdIpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 1),
    _UsdIpProfileId_Type()
)
usdIpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpProfileId.setStatus("current")
_UsdIpProfileRowStatus_Type = RowStatus
_UsdIpProfileRowStatus_Object = MibTableColumn
usdIpProfileRowStatus = _UsdIpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 2),
    _UsdIpProfileRowStatus_Type()
)
usdIpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileRowStatus.setStatus("deprecated")
_UsdIpProfileRouterName_Type = UsdName
_UsdIpProfileRouterName_Object = MibTableColumn
usdIpProfileRouterName = _UsdIpProfileRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 3),
    _UsdIpProfileRouterName_Type()
)
usdIpProfileRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileRouterName.setStatus("current")


class _UsdIpProfileIpAddr_Type(IpAddress):
    """Custom type usdIpProfileIpAddr based on IpAddress"""
    defaultValue = 0


_UsdIpProfileIpAddr_Object = MibTableColumn
usdIpProfileIpAddr = _UsdIpProfileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 4),
    _UsdIpProfileIpAddr_Type()
)
usdIpProfileIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileIpAddr.setStatus("current")


class _UsdIpProfileIpMask_Type(IpAddress):
    """Custom type usdIpProfileIpMask based on IpAddress"""
    defaultValue = 0


_UsdIpProfileIpMask_Object = MibTableColumn
usdIpProfileIpMask = _UsdIpProfileIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 5),
    _UsdIpProfileIpMask_Type()
)
usdIpProfileIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileIpMask.setStatus("current")


class _UsdIpProfileDirectedBcastEnable_Type(UsdEnable):
    """Custom type usdIpProfileDirectedBcastEnable based on UsdEnable"""


_UsdIpProfileDirectedBcastEnable_Object = MibTableColumn
usdIpProfileDirectedBcastEnable = _UsdIpProfileDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 6),
    _UsdIpProfileDirectedBcastEnable_Type()
)
usdIpProfileDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileDirectedBcastEnable.setStatus("current")


class _UsdIpProfileIcmpRedirectEnable_Type(UsdEnable):
    """Custom type usdIpProfileIcmpRedirectEnable based on UsdEnable"""


_UsdIpProfileIcmpRedirectEnable_Object = MibTableColumn
usdIpProfileIcmpRedirectEnable = _UsdIpProfileIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 7),
    _UsdIpProfileIcmpRedirectEnable_Type()
)
usdIpProfileIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileIcmpRedirectEnable.setStatus("current")


class _UsdIpProfileAccessRoute_Type(UsdEnable):
    """Custom type usdIpProfileAccessRoute based on UsdEnable"""


_UsdIpProfileAccessRoute_Object = MibTableColumn
usdIpProfileAccessRoute = _UsdIpProfileAccessRoute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 8),
    _UsdIpProfileAccessRoute_Type()
)
usdIpProfileAccessRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileAccessRoute.setStatus("current")


class _UsdIpProfileMtu_Type(Integer32):
    """Custom type usdIpProfileMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 10240),
    )


_UsdIpProfileMtu_Type.__name__ = "Integer32"
_UsdIpProfileMtu_Object = MibTableColumn
usdIpProfileMtu = _UsdIpProfileMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 9),
    _UsdIpProfileMtu_Type()
)
usdIpProfileMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileMtu.setStatus("current")


class _UsdIpProfileLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type usdIpProfileLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_UsdIpProfileLoopbackIfIndex_Object = MibTableColumn
usdIpProfileLoopbackIfIndex = _UsdIpProfileLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 10),
    _UsdIpProfileLoopbackIfIndex_Type()
)
usdIpProfileLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileLoopbackIfIndex.setStatus("obsolete")


class _UsdIpProfileLoopback_Type(Integer32):
    """Custom type usdIpProfileLoopback based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UsdIpProfileLoopback_Type.__name__ = "Integer32"
_UsdIpProfileLoopback_Object = MibTableColumn
usdIpProfileLoopback = _UsdIpProfileLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 11),
    _UsdIpProfileLoopback_Type()
)
usdIpProfileLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileLoopback.setStatus("current")
_UsdIpProfileSetMap_Type = UsdSetMap
_UsdIpProfileSetMap_Object = MibTableColumn
usdIpProfileSetMap = _UsdIpProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 12),
    _UsdIpProfileSetMap_Type()
)
usdIpProfileSetMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileSetMap.setStatus("current")


class _UsdIpProfileSrcAddrValidEnable_Type(UsdEnable):
    """Custom type usdIpProfileSrcAddrValidEnable based on UsdEnable"""


_UsdIpProfileSrcAddrValidEnable_Object = MibTableColumn
usdIpProfileSrcAddrValidEnable = _UsdIpProfileSrcAddrValidEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 13),
    _UsdIpProfileSrcAddrValidEnable_Type()
)
usdIpProfileSrcAddrValidEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpProfileSrcAddrValidEnable.setStatus("current")
_UsdIpProfileMIBConformance_ObjectIdentity = ObjectIdentity
usdIpProfileMIBConformance = _UsdIpProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4)
)
_UsdIpProfileMIBCompliances_ObjectIdentity = ObjectIdentity
usdIpProfileMIBCompliances = _UsdIpProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1)
)
_UsdIpProfileMIBGroups_ObjectIdentity = ObjectIdentity
usdIpProfileMIBGroups = _UsdIpProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2)
)

# Managed Objects groups

usdIpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 1)
)
usdIpProfileGroup.setObjects(
      *(("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRowStatus"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRouterName"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpAddr"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpMask"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileDirectedBcastEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIcmpRedirectEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileAccessRoute"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileMtu"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileLoopbackIfIndex"))
)
if mibBuilder.loadTexts:
    usdIpProfileGroup.setStatus("obsolete")

usdIpProfileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 2)
)
usdIpProfileGroup1.setObjects(
      *(("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRowStatus"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRouterName"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpAddr"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpMask"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileDirectedBcastEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIcmpRedirectEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileAccessRoute"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileMtu"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileLoopback"))
)
if mibBuilder.loadTexts:
    usdIpProfileGroup1.setStatus("obsolete")

usdIpProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 3)
)
usdIpProfileGroup2.setObjects(
      *(("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRouterName"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpAddr"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIpMask"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileDirectedBcastEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileIcmpRedirectEnable"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileAccessRoute"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileMtu"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileLoopback"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileSetMap"),
        ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileSrcAddrValidEnable"))
)
if mibBuilder.loadTexts:
    usdIpProfileGroup2.setStatus("current")

usdIpProfileDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 4)
)
usdIpProfileDeprecatedGroup.setObjects(
    ("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileRowStatus")
)
if mibBuilder.loadTexts:
    usdIpProfileDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIpProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpProfileCompliance.setStatus(
        "obsolete"
    )

usdIpProfileCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdIpProfileCompliance1.setStatus(
        "obsolete"
    )

usdIpProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdIpProfileCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IP-PROFILE-MIB",
    **{"usdIpProfileMIB": usdIpProfileMIB,
       "usdIpProfileObjects": usdIpProfileObjects,
       "usdIpProfile": usdIpProfile,
       "usdIpProfileTable": usdIpProfileTable,
       "usdIpProfileEntry": usdIpProfileEntry,
       "usdIpProfileId": usdIpProfileId,
       "usdIpProfileRowStatus": usdIpProfileRowStatus,
       "usdIpProfileRouterName": usdIpProfileRouterName,
       "usdIpProfileIpAddr": usdIpProfileIpAddr,
       "usdIpProfileIpMask": usdIpProfileIpMask,
       "usdIpProfileDirectedBcastEnable": usdIpProfileDirectedBcastEnable,
       "usdIpProfileIcmpRedirectEnable": usdIpProfileIcmpRedirectEnable,
       "usdIpProfileAccessRoute": usdIpProfileAccessRoute,
       "usdIpProfileMtu": usdIpProfileMtu,
       "usdIpProfileLoopbackIfIndex": usdIpProfileLoopbackIfIndex,
       "usdIpProfileLoopback": usdIpProfileLoopback,
       "usdIpProfileSetMap": usdIpProfileSetMap,
       "usdIpProfileSrcAddrValidEnable": usdIpProfileSrcAddrValidEnable,
       "usdIpProfileMIBConformance": usdIpProfileMIBConformance,
       "usdIpProfileMIBCompliances": usdIpProfileMIBCompliances,
       "usdIpProfileCompliance": usdIpProfileCompliance,
       "usdIpProfileCompliance1": usdIpProfileCompliance1,
       "usdIpProfileCompliance2": usdIpProfileCompliance2,
       "usdIpProfileMIBGroups": usdIpProfileMIBGroups,
       "usdIpProfileGroup": usdIpProfileGroup,
       "usdIpProfileGroup1": usdIpProfileGroup1,
       "usdIpProfileGroup2": usdIpProfileGroup2,
       "usdIpProfileDeprecatedGroup": usdIpProfileDeprecatedGroup}
)
