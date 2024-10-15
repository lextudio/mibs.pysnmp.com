# SNMP MIB module (Juniper-IPV6-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IPV6-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:34 2024
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

juniIpv6ProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68)
)
juniIpv6ProfileMIB.setRevisions(
        ("2007-07-19 18:19",
         "2003-09-29 17:58")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniIpv6ProfileObjects_ObjectIdentity = ObjectIdentity
juniIpv6ProfileObjects = _JuniIpv6ProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1)
)
_JuniIpv6Profile_ObjectIdentity = ObjectIdentity
juniIpv6Profile = _JuniIpv6Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1)
)
_JuniIpv6ProfileTable_Object = MibTable
juniIpv6ProfileTable = _JuniIpv6ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpv6ProfileTable.setStatus("current")
_JuniIpv6ProfileEntry_Object = MibTableRow
juniIpv6ProfileEntry = _JuniIpv6ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1)
)
juniIpv6ProfileEntry.setIndexNames(
    (0, "Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileId"),
)
if mibBuilder.loadTexts:
    juniIpv6ProfileEntry.setStatus("current")
_JuniIpv6ProfileId_Type = Unsigned32
_JuniIpv6ProfileId_Object = MibTableColumn
juniIpv6ProfileId = _JuniIpv6ProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 1),
    _JuniIpv6ProfileId_Type()
)
juniIpv6ProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpv6ProfileId.setStatus("current")
_JuniIpv6ProfileSetMap_Type = JuniSetMap
_JuniIpv6ProfileSetMap_Object = MibTableColumn
juniIpv6ProfileSetMap = _JuniIpv6ProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 2),
    _JuniIpv6ProfileSetMap_Type()
)
juniIpv6ProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileSetMap.setStatus("current")
_JuniIpv6ProfileRouterName_Type = JuniName
_JuniIpv6ProfileRouterName_Object = MibTableColumn
juniIpv6ProfileRouterName = _JuniIpv6ProfileRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 3),
    _JuniIpv6ProfileRouterName_Type()
)
juniIpv6ProfileRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileRouterName.setStatus("current")


class _JuniIpv6ProfileIpv6Addr_Type(InetAddressIPv6):
    """Custom type juniIpv6ProfileIpv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_JuniIpv6ProfileIpv6Addr_Object = MibTableColumn
juniIpv6ProfileIpv6Addr = _JuniIpv6ProfileIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 4),
    _JuniIpv6ProfileIpv6Addr_Type()
)
juniIpv6ProfileIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileIpv6Addr.setStatus("current")


class _JuniIpv6ProfileIpv6MaskLen_Type(Integer32):
    """Custom type juniIpv6ProfileIpv6MaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_JuniIpv6ProfileIpv6MaskLen_Type.__name__ = "Integer32"
_JuniIpv6ProfileIpv6MaskLen_Object = MibTableColumn
juniIpv6ProfileIpv6MaskLen = _JuniIpv6ProfileIpv6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 5),
    _JuniIpv6ProfileIpv6MaskLen_Type()
)
juniIpv6ProfileIpv6MaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileIpv6MaskLen.setStatus("current")


class _JuniIpv6ProfileMtu_Type(Integer32):
    """Custom type juniIpv6ProfileMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1280, 10240),
    )


_JuniIpv6ProfileMtu_Type.__name__ = "Integer32"
_JuniIpv6ProfileMtu_Object = MibTableColumn
juniIpv6ProfileMtu = _JuniIpv6ProfileMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 6),
    _JuniIpv6ProfileMtu_Type()
)
juniIpv6ProfileMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileMtu.setStatus("current")


class _JuniIpv6ProfileSrcAddrValidEnable_Type(JuniEnable):
    """Custom type juniIpv6ProfileSrcAddrValidEnable based on JuniEnable"""


_JuniIpv6ProfileSrcAddrValidEnable_Object = MibTableColumn
juniIpv6ProfileSrcAddrValidEnable = _JuniIpv6ProfileSrcAddrValidEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 7),
    _JuniIpv6ProfileSrcAddrValidEnable_Type()
)
juniIpv6ProfileSrcAddrValidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileSrcAddrValidEnable.setStatus("current")


class _JuniIpv6ProfileInheritNumString_Type(DisplayString):
    """Custom type juniIpv6ProfileInheritNumString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpv6ProfileInheritNumString_Type.__name__ = "DisplayString"
_JuniIpv6ProfileInheritNumString_Object = MibTableColumn
juniIpv6ProfileInheritNumString = _JuniIpv6ProfileInheritNumString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 8),
    _JuniIpv6ProfileInheritNumString_Type()
)
juniIpv6ProfileInheritNumString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileInheritNumString.setStatus("current")


class _JuniIpv6ProfileNdEnabled_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdEnabled based on JuniEnable"""


_JuniIpv6ProfileNdEnabled_Object = MibTableColumn
juniIpv6ProfileNdEnabled = _JuniIpv6ProfileNdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 9),
    _JuniIpv6ProfileNdEnabled_Type()
)
juniIpv6ProfileNdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdEnabled.setStatus("current")


class _JuniIpv6ProfileNdManagedConfig_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdManagedConfig based on JuniEnable"""


_JuniIpv6ProfileNdManagedConfig_Object = MibTableColumn
juniIpv6ProfileNdManagedConfig = _JuniIpv6ProfileNdManagedConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 10),
    _JuniIpv6ProfileNdManagedConfig_Type()
)
juniIpv6ProfileNdManagedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdManagedConfig.setStatus("current")


class _JuniIpv6ProfileNdOtherConfig_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdOtherConfig based on JuniEnable"""


_JuniIpv6ProfileNdOtherConfig_Object = MibTableColumn
juniIpv6ProfileNdOtherConfig = _JuniIpv6ProfileNdOtherConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 11),
    _JuniIpv6ProfileNdOtherConfig_Type()
)
juniIpv6ProfileNdOtherConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdOtherConfig.setStatus("current")


class _JuniIpv6ProfileNdSuppressRa_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdSuppressRa based on JuniEnable"""


_JuniIpv6ProfileNdSuppressRa_Object = MibTableColumn
juniIpv6ProfileNdSuppressRa = _JuniIpv6ProfileNdSuppressRa_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 12),
    _JuniIpv6ProfileNdSuppressRa_Type()
)
juniIpv6ProfileNdSuppressRa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdSuppressRa.setStatus("current")


class _JuniIpv6ProfileNdRaInterval_Type(Integer32):
    """Custom type juniIpv6ProfileNdRaInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_JuniIpv6ProfileNdRaInterval_Type.__name__ = "Integer32"
_JuniIpv6ProfileNdRaInterval_Object = MibTableColumn
juniIpv6ProfileNdRaInterval = _JuniIpv6ProfileNdRaInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 13),
    _JuniIpv6ProfileNdRaInterval_Type()
)
juniIpv6ProfileNdRaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdRaInterval.setStatus("current")


class _JuniIpv6ProfileNdRaLifeTime_Type(Integer32):
    """Custom type juniIpv6ProfileNdRaLifeTime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_JuniIpv6ProfileNdRaLifeTime_Type.__name__ = "Integer32"
_JuniIpv6ProfileNdRaLifeTime_Object = MibTableColumn
juniIpv6ProfileNdRaLifeTime = _JuniIpv6ProfileNdRaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 14),
    _JuniIpv6ProfileNdRaLifeTime_Type()
)
juniIpv6ProfileNdRaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdRaLifeTime.setStatus("current")


class _JuniIpv6ProfileNdReachableTime_Type(Integer32):
    """Custom type juniIpv6ProfileNdReachableTime based on Integer32"""
    defaultValue = 0


_JuniIpv6ProfileNdReachableTime_Object = MibTableColumn
juniIpv6ProfileNdReachableTime = _JuniIpv6ProfileNdReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 15),
    _JuniIpv6ProfileNdReachableTime_Type()
)
juniIpv6ProfileNdReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdReachableTime.setStatus("current")
_JuniIpv6ProfileNdPrefix_Type = Ipv6AddressPrefix
_JuniIpv6ProfileNdPrefix_Object = MibTableColumn
juniIpv6ProfileNdPrefix = _JuniIpv6ProfileNdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 16),
    _JuniIpv6ProfileNdPrefix_Type()
)
juniIpv6ProfileNdPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefix.setStatus("current")


class _JuniIpv6ProfileNdPrefixLength_Type(Integer32):
    """Custom type juniIpv6ProfileNdPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_JuniIpv6ProfileNdPrefixLength_Type.__name__ = "Integer32"
_JuniIpv6ProfileNdPrefixLength_Object = MibTableColumn
juniIpv6ProfileNdPrefixLength = _JuniIpv6ProfileNdPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 17),
    _JuniIpv6ProfileNdPrefixLength_Type()
)
juniIpv6ProfileNdPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefixLength.setStatus("current")


class _JuniIpv6ProfileNdPrefixOnLinkFlag_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdPrefixOnLinkFlag based on JuniEnable"""


_JuniIpv6ProfileNdPrefixOnLinkFlag_Object = MibTableColumn
juniIpv6ProfileNdPrefixOnLinkFlag = _JuniIpv6ProfileNdPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 18),
    _JuniIpv6ProfileNdPrefixOnLinkFlag_Type()
)
juniIpv6ProfileNdPrefixOnLinkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefixOnLinkFlag.setStatus("current")


class _JuniIpv6ProfileNdPrefixAutonomousFlag_Type(JuniEnable):
    """Custom type juniIpv6ProfileNdPrefixAutonomousFlag based on JuniEnable"""


_JuniIpv6ProfileNdPrefixAutonomousFlag_Object = MibTableColumn
juniIpv6ProfileNdPrefixAutonomousFlag = _JuniIpv6ProfileNdPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 19),
    _JuniIpv6ProfileNdPrefixAutonomousFlag_Type()
)
juniIpv6ProfileNdPrefixAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefixAutonomousFlag.setStatus("current")


class _JuniIpv6ProfileNdPrefixPreferredLifetime_Type(Integer32):
    """Custom type juniIpv6ProfileNdPrefixPreferredLifetime based on Integer32"""
    defaultValue = 604800


_JuniIpv6ProfileNdPrefixPreferredLifetime_Object = MibTableColumn
juniIpv6ProfileNdPrefixPreferredLifetime = _JuniIpv6ProfileNdPrefixPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 20),
    _JuniIpv6ProfileNdPrefixPreferredLifetime_Type()
)
juniIpv6ProfileNdPrefixPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefixPreferredLifetime.setStatus("current")


class _JuniIpv6ProfileNdPrefixValidLifetime_Type(Integer32):
    """Custom type juniIpv6ProfileNdPrefixValidLifetime based on Integer32"""
    defaultValue = 2592000


_JuniIpv6ProfileNdPrefixValidLifetime_Object = MibTableColumn
juniIpv6ProfileNdPrefixValidLifetime = _JuniIpv6ProfileNdPrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 1, 1, 1, 1, 21),
    _JuniIpv6ProfileNdPrefixValidLifetime_Type()
)
juniIpv6ProfileNdPrefixValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpv6ProfileNdPrefixValidLifetime.setStatus("current")
_JuniIpv6ProfileMIBConformance_ObjectIdentity = ObjectIdentity
juniIpv6ProfileMIBConformance = _JuniIpv6ProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4)
)
_JuniIpv6ProfileMIBCompliances_ObjectIdentity = ObjectIdentity
juniIpv6ProfileMIBCompliances = _JuniIpv6ProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 1)
)
_JuniIpv6ProfileMIBGroups_ObjectIdentity = ObjectIdentity
juniIpv6ProfileMIBGroups = _JuniIpv6ProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 2)
)

# Managed Objects groups

juniIpv6ProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 2, 1)
)
juniIpv6ProfileGroup.setObjects(
      *(("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileSetMap"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileRouterName"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileIpv6Addr"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileIpv6MaskLen"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileMtu"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileSrcAddrValidEnable"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileInheritNumString"))
)
if mibBuilder.loadTexts:
    juniIpv6ProfileGroup.setStatus("obsolete")

juniIpv6ProfileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 2, 2)
)
juniIpv6ProfileGroup1.setObjects(
      *(("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileSetMap"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileRouterName"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileIpv6Addr"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileIpv6MaskLen"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileMtu"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileSrcAddrValidEnable"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileInheritNumString"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdEnabled"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdManagedConfig"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdOtherConfig"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdSuppressRa"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdRaInterval"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdRaLifeTime"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdReachableTime"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefix"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefixLength"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefixOnLinkFlag"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefixAutonomousFlag"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefixPreferredLifetime"),
        ("Juniper-IPV6-PROFILE-MIB", "juniIpv6ProfileNdPrefixValidLifetime"))
)
if mibBuilder.loadTexts:
    juniIpv6ProfileGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIpv6ProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpv6ProfileCompliance.setStatus(
        "obsolete"
    )

juniIpv6ProfileCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpv6ProfileCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IPV6-PROFILE-MIB",
    **{"juniIpv6ProfileMIB": juniIpv6ProfileMIB,
       "juniIpv6ProfileObjects": juniIpv6ProfileObjects,
       "juniIpv6Profile": juniIpv6Profile,
       "juniIpv6ProfileTable": juniIpv6ProfileTable,
       "juniIpv6ProfileEntry": juniIpv6ProfileEntry,
       "juniIpv6ProfileId": juniIpv6ProfileId,
       "juniIpv6ProfileSetMap": juniIpv6ProfileSetMap,
       "juniIpv6ProfileRouterName": juniIpv6ProfileRouterName,
       "juniIpv6ProfileIpv6Addr": juniIpv6ProfileIpv6Addr,
       "juniIpv6ProfileIpv6MaskLen": juniIpv6ProfileIpv6MaskLen,
       "juniIpv6ProfileMtu": juniIpv6ProfileMtu,
       "juniIpv6ProfileSrcAddrValidEnable": juniIpv6ProfileSrcAddrValidEnable,
       "juniIpv6ProfileInheritNumString": juniIpv6ProfileInheritNumString,
       "juniIpv6ProfileNdEnabled": juniIpv6ProfileNdEnabled,
       "juniIpv6ProfileNdManagedConfig": juniIpv6ProfileNdManagedConfig,
       "juniIpv6ProfileNdOtherConfig": juniIpv6ProfileNdOtherConfig,
       "juniIpv6ProfileNdSuppressRa": juniIpv6ProfileNdSuppressRa,
       "juniIpv6ProfileNdRaInterval": juniIpv6ProfileNdRaInterval,
       "juniIpv6ProfileNdRaLifeTime": juniIpv6ProfileNdRaLifeTime,
       "juniIpv6ProfileNdReachableTime": juniIpv6ProfileNdReachableTime,
       "juniIpv6ProfileNdPrefix": juniIpv6ProfileNdPrefix,
       "juniIpv6ProfileNdPrefixLength": juniIpv6ProfileNdPrefixLength,
       "juniIpv6ProfileNdPrefixOnLinkFlag": juniIpv6ProfileNdPrefixOnLinkFlag,
       "juniIpv6ProfileNdPrefixAutonomousFlag": juniIpv6ProfileNdPrefixAutonomousFlag,
       "juniIpv6ProfileNdPrefixPreferredLifetime": juniIpv6ProfileNdPrefixPreferredLifetime,
       "juniIpv6ProfileNdPrefixValidLifetime": juniIpv6ProfileNdPrefixValidLifetime,
       "juniIpv6ProfileMIBConformance": juniIpv6ProfileMIBConformance,
       "juniIpv6ProfileMIBCompliances": juniIpv6ProfileMIBCompliances,
       "juniIpv6ProfileCompliance": juniIpv6ProfileCompliance,
       "juniIpv6ProfileCompliance1": juniIpv6ProfileCompliance1,
       "juniIpv6ProfileMIBGroups": juniIpv6ProfileMIBGroups,
       "juniIpv6ProfileGroup": juniIpv6ProfileGroup,
       "juniIpv6ProfileGroup1": juniIpv6ProfileGroup1}
)
