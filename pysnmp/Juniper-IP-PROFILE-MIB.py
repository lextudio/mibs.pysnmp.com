# SNMP MIB module (Juniper-IP-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IP-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:30 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniName,
 JuniSetMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniName",
    "JuniSetMap")

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


# MODULE-IDENTITY

juniIpProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26)
)
juniIpProfileMIB.setRevisions(
        ("2006-09-08 10:26",
         "2005-09-13 17:21",
         "2004-10-05 14:04",
         "2003-09-24 15:33",
         "2002-10-11 13:20",
         "2001-01-24 20:06",
         "2000-05-08 00:00",
         "1999-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniIpProfileObjects_ObjectIdentity = ObjectIdentity
juniIpProfileObjects = _JuniIpProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1)
)
_JuniIpProfile_ObjectIdentity = ObjectIdentity
juniIpProfile = _JuniIpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1)
)
_JuniIpProfileTable_Object = MibTable
juniIpProfileTable = _JuniIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpProfileTable.setStatus("current")
_JuniIpProfileEntry_Object = MibTableRow
juniIpProfileEntry = _JuniIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1)
)
juniIpProfileEntry.setIndexNames(
    (0, "Juniper-IP-PROFILE-MIB", "juniIpProfileId"),
)
if mibBuilder.loadTexts:
    juniIpProfileEntry.setStatus("current")
_JuniIpProfileId_Type = Unsigned32
_JuniIpProfileId_Object = MibTableColumn
juniIpProfileId = _JuniIpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 1),
    _JuniIpProfileId_Type()
)
juniIpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpProfileId.setStatus("current")
_JuniIpProfileRowStatus_Type = RowStatus
_JuniIpProfileRowStatus_Object = MibTableColumn
juniIpProfileRowStatus = _JuniIpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 2),
    _JuniIpProfileRowStatus_Type()
)
juniIpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileRowStatus.setStatus("deprecated")
_JuniIpProfileRouterName_Type = JuniName
_JuniIpProfileRouterName_Object = MibTableColumn
juniIpProfileRouterName = _JuniIpProfileRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 3),
    _JuniIpProfileRouterName_Type()
)
juniIpProfileRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileRouterName.setStatus("current")


class _JuniIpProfileIpAddr_Type(IpAddress):
    """Custom type juniIpProfileIpAddr based on IpAddress"""
    defaultValue = 0


_JuniIpProfileIpAddr_Object = MibTableColumn
juniIpProfileIpAddr = _JuniIpProfileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 4),
    _JuniIpProfileIpAddr_Type()
)
juniIpProfileIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileIpAddr.setStatus("current")


class _JuniIpProfileIpMask_Type(IpAddress):
    """Custom type juniIpProfileIpMask based on IpAddress"""
    defaultValue = 0


_JuniIpProfileIpMask_Object = MibTableColumn
juniIpProfileIpMask = _JuniIpProfileIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 5),
    _JuniIpProfileIpMask_Type()
)
juniIpProfileIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileIpMask.setStatus("current")


class _JuniIpProfileDirectedBcastEnable_Type(JuniEnable):
    """Custom type juniIpProfileDirectedBcastEnable based on JuniEnable"""


_JuniIpProfileDirectedBcastEnable_Object = MibTableColumn
juniIpProfileDirectedBcastEnable = _JuniIpProfileDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 6),
    _JuniIpProfileDirectedBcastEnable_Type()
)
juniIpProfileDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileDirectedBcastEnable.setStatus("current")


class _JuniIpProfileIcmpRedirectEnable_Type(JuniEnable):
    """Custom type juniIpProfileIcmpRedirectEnable based on JuniEnable"""


_JuniIpProfileIcmpRedirectEnable_Object = MibTableColumn
juniIpProfileIcmpRedirectEnable = _JuniIpProfileIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 7),
    _JuniIpProfileIcmpRedirectEnable_Type()
)
juniIpProfileIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileIcmpRedirectEnable.setStatus("current")


class _JuniIpProfileAccessRoute_Type(JuniEnable):
    """Custom type juniIpProfileAccessRoute based on JuniEnable"""


_JuniIpProfileAccessRoute_Object = MibTableColumn
juniIpProfileAccessRoute = _JuniIpProfileAccessRoute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 8),
    _JuniIpProfileAccessRoute_Type()
)
juniIpProfileAccessRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileAccessRoute.setStatus("current")


class _JuniIpProfileMtu_Type(Integer32):
    """Custom type juniIpProfileMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 10240),
    )


_JuniIpProfileMtu_Type.__name__ = "Integer32"
_JuniIpProfileMtu_Object = MibTableColumn
juniIpProfileMtu = _JuniIpProfileMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 9),
    _JuniIpProfileMtu_Type()
)
juniIpProfileMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileMtu.setStatus("current")


class _JuniIpProfileLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type juniIpProfileLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniIpProfileLoopbackIfIndex_Object = MibTableColumn
juniIpProfileLoopbackIfIndex = _JuniIpProfileLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 10),
    _JuniIpProfileLoopbackIfIndex_Type()
)
juniIpProfileLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileLoopbackIfIndex.setStatus("obsolete")


class _JuniIpProfileLoopback_Type(Integer32):
    """Custom type juniIpProfileLoopback based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniIpProfileLoopback_Type.__name__ = "Integer32"
_JuniIpProfileLoopback_Object = MibTableColumn
juniIpProfileLoopback = _JuniIpProfileLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 11),
    _JuniIpProfileLoopback_Type()
)
juniIpProfileLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileLoopback.setStatus("obsolete")
_JuniIpProfileSetMap_Type = JuniSetMap
_JuniIpProfileSetMap_Object = MibTableColumn
juniIpProfileSetMap = _JuniIpProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 12),
    _JuniIpProfileSetMap_Type()
)
juniIpProfileSetMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileSetMap.setStatus("current")


class _JuniIpProfileSrcAddrValidEnable_Type(JuniEnable):
    """Custom type juniIpProfileSrcAddrValidEnable based on JuniEnable"""


_JuniIpProfileSrcAddrValidEnable_Object = MibTableColumn
juniIpProfileSrcAddrValidEnable = _JuniIpProfileSrcAddrValidEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 13),
    _JuniIpProfileSrcAddrValidEnable_Type()
)
juniIpProfileSrcAddrValidEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileSrcAddrValidEnable.setStatus("current")


class _JuniIpProfileInheritNumString_Type(DisplayString):
    """Custom type juniIpProfileInheritNumString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpProfileInheritNumString_Type.__name__ = "DisplayString"
_JuniIpProfileInheritNumString_Object = MibTableColumn
juniIpProfileInheritNumString = _JuniIpProfileInheritNumString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 14),
    _JuniIpProfileInheritNumString_Type()
)
juniIpProfileInheritNumString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileInheritNumString.setStatus("current")


class _JuniIpProfileTcpMss_Type(Integer32):
    """Custom type juniIpProfileTcpMss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_JuniIpProfileTcpMss_Type.__name__ = "Integer32"
_JuniIpProfileTcpMss_Object = MibTableColumn
juniIpProfileTcpMss = _JuniIpProfileTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 15),
    _JuniIpProfileTcpMss_Type()
)
juniIpProfileTcpMss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileTcpMss.setStatus("current")


class _JuniIpProfileFilterOptionsAll_Type(JuniEnable):
    """Custom type juniIpProfileFilterOptionsAll based on JuniEnable"""


_JuniIpProfileFilterOptionsAll_Object = MibTableColumn
juniIpProfileFilterOptionsAll = _JuniIpProfileFilterOptionsAll_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 16),
    _JuniIpProfileFilterOptionsAll_Type()
)
juniIpProfileFilterOptionsAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileFilterOptionsAll.setStatus("current")


class _JuniIpProfileFlowStats_Type(JuniEnable):
    """Custom type juniIpProfileFlowStats based on JuniEnable"""


_JuniIpProfileFlowStats_Object = MibTableColumn
juniIpProfileFlowStats = _JuniIpProfileFlowStats_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 17),
    _JuniIpProfileFlowStats_Type()
)
juniIpProfileFlowStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileFlowStats.setStatus("current")


class _JuniIpProfileBlockMulticastSources_Type(JuniEnable):
    """Custom type juniIpProfileBlockMulticastSources based on JuniEnable"""


_JuniIpProfileBlockMulticastSources_Object = MibTableColumn
juniIpProfileBlockMulticastSources = _JuniIpProfileBlockMulticastSources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 18),
    _JuniIpProfileBlockMulticastSources_Type()
)
juniIpProfileBlockMulticastSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpProfileBlockMulticastSources.setStatus("current")
_JuniIpProfileMIBConformance_ObjectIdentity = ObjectIdentity
juniIpProfileMIBConformance = _JuniIpProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4)
)
_JuniIpProfileMIBCompliances_ObjectIdentity = ObjectIdentity
juniIpProfileMIBCompliances = _JuniIpProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1)
)
_JuniIpProfileMIBGroups_ObjectIdentity = ObjectIdentity
juniIpProfileMIBGroups = _JuniIpProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2)
)

# Managed Objects groups

juniIpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 1)
)
juniIpProfileGroup.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopbackIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup.setStatus("obsolete")

juniIpProfileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 2)
)
juniIpProfileGroup1.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup1.setStatus("obsolete")

juniIpProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 3)
)
juniIpProfileGroup2.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup2.setStatus("obsolete")

juniIpProfileDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 4)
)
juniIpProfileDeprecatedGroup.setObjects(
    ("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus")
)
if mibBuilder.loadTexts:
    juniIpProfileDeprecatedGroup.setStatus("deprecated")

juniIpProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 5)
)
juniIpProfileGroup3.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup3.setStatus("obsolete")

juniIpProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 6)
)
juniIpProfileGroup4.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup4.setStatus("obsolete")

juniIpProfileGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 7)
)
juniIpProfileGroup5.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup5.setStatus("obsolete")

juniIpProfileGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 8)
)
juniIpProfileGroup6.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup6.setStatus("obsolete")

juniIpProfileGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 9)
)
juniIpProfileGroup7.setObjects(
      *(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"),
        ("Juniper-IP-PROFILE-MIB", "juniIpProfileBlockMulticastSources"))
)
if mibBuilder.loadTexts:
    juniIpProfileGroup7.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIpProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance.setStatus(
        "obsolete"
    )

juniIpProfileCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance1.setStatus(
        "obsolete"
    )

juniIpProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance2.setStatus(
        "obsolete"
    )

juniIpProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance3.setStatus(
        "obsolete"
    )

juniIpProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance4.setStatus(
        "obsolete"
    )

juniIpProfileCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance5.setStatus(
        "current"
    )

juniIpProfileCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance6.setStatus(
        "current"
    )

juniIpProfileCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniIpProfileCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-PROFILE-MIB",
    **{"juniIpProfileMIB": juniIpProfileMIB,
       "juniIpProfileObjects": juniIpProfileObjects,
       "juniIpProfile": juniIpProfile,
       "juniIpProfileTable": juniIpProfileTable,
       "juniIpProfileEntry": juniIpProfileEntry,
       "juniIpProfileId": juniIpProfileId,
       "juniIpProfileRowStatus": juniIpProfileRowStatus,
       "juniIpProfileRouterName": juniIpProfileRouterName,
       "juniIpProfileIpAddr": juniIpProfileIpAddr,
       "juniIpProfileIpMask": juniIpProfileIpMask,
       "juniIpProfileDirectedBcastEnable": juniIpProfileDirectedBcastEnable,
       "juniIpProfileIcmpRedirectEnable": juniIpProfileIcmpRedirectEnable,
       "juniIpProfileAccessRoute": juniIpProfileAccessRoute,
       "juniIpProfileMtu": juniIpProfileMtu,
       "juniIpProfileLoopbackIfIndex": juniIpProfileLoopbackIfIndex,
       "juniIpProfileLoopback": juniIpProfileLoopback,
       "juniIpProfileSetMap": juniIpProfileSetMap,
       "juniIpProfileSrcAddrValidEnable": juniIpProfileSrcAddrValidEnable,
       "juniIpProfileInheritNumString": juniIpProfileInheritNumString,
       "juniIpProfileTcpMss": juniIpProfileTcpMss,
       "juniIpProfileFilterOptionsAll": juniIpProfileFilterOptionsAll,
       "juniIpProfileFlowStats": juniIpProfileFlowStats,
       "juniIpProfileBlockMulticastSources": juniIpProfileBlockMulticastSources,
       "juniIpProfileMIBConformance": juniIpProfileMIBConformance,
       "juniIpProfileMIBCompliances": juniIpProfileMIBCompliances,
       "juniIpProfileCompliance": juniIpProfileCompliance,
       "juniIpProfileCompliance1": juniIpProfileCompliance1,
       "juniIpProfileCompliance2": juniIpProfileCompliance2,
       "juniIpProfileCompliance3": juniIpProfileCompliance3,
       "juniIpProfileCompliance4": juniIpProfileCompliance4,
       "juniIpProfileCompliance5": juniIpProfileCompliance5,
       "juniIpProfileCompliance6": juniIpProfileCompliance6,
       "juniIpProfileCompliance7": juniIpProfileCompliance7,
       "juniIpProfileMIBGroups": juniIpProfileMIBGroups,
       "juniIpProfileGroup": juniIpProfileGroup,
       "juniIpProfileGroup1": juniIpProfileGroup1,
       "juniIpProfileGroup2": juniIpProfileGroup2,
       "juniIpProfileDeprecatedGroup": juniIpProfileDeprecatedGroup,
       "juniIpProfileGroup3": juniIpProfileGroup3,
       "juniIpProfileGroup4": juniIpProfileGroup4,
       "juniIpProfileGroup5": juniIpProfileGroup5,
       "juniIpProfileGroup6": juniIpProfileGroup6,
       "juniIpProfileGroup7": juniIpProfileGroup7}
)
