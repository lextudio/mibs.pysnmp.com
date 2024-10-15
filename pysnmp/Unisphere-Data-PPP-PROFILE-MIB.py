# SNMP MIB module (Unisphere-Data-PPP-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPP-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:19 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdPppAuthentication,) = mibBuilder.importSymbols(
    "Unisphere-Data-PPP-MIB",
    "UsdPppAuthentication")

(UsdEnable,
 UsdName,
 UsdSetMap) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdName",
    "UsdSetMap")


# MODULE-IDENTITY

usdPppProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45)
)
usdPppProfileMIB.setRevisions(
        ("2002-01-25 14:00",
         "2002-01-16 17:58",
         "2002-01-08 19:43",
         "2001-10-02 12:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdPppProfileObjects_ObjectIdentity = ObjectIdentity
usdPppProfileObjects = _UsdPppProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1)
)
_UsdPppProfile_ObjectIdentity = ObjectIdentity
usdPppProfile = _UsdPppProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1)
)
_UsdPppProfileTable_Object = MibTable
usdPppProfileTable = _UsdPppProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppProfileTable.setStatus("current")
_UsdPppProfileEntry_Object = MibTableRow
usdPppProfileEntry = _UsdPppProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1)
)
usdPppProfileEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileId"),
)
if mibBuilder.loadTexts:
    usdPppProfileEntry.setStatus("current")
_UsdPppProfileId_Type = Unsigned32
_UsdPppProfileId_Object = MibTableColumn
usdPppProfileId = _UsdPppProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 1),
    _UsdPppProfileId_Type()
)
usdPppProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppProfileId.setStatus("current")
_UsdPppProfileSetMap_Type = UsdSetMap
_UsdPppProfileSetMap_Object = MibTableColumn
usdPppProfileSetMap = _UsdPppProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 2),
    _UsdPppProfileSetMap_Type()
)
usdPppProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileSetMap.setStatus("current")


class _UsdPppProfileLcpMagicNumber_Type(Integer32):
    """Custom type usdPppProfileLcpMagicNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_UsdPppProfileLcpMagicNumber_Type.__name__ = "Integer32"
_UsdPppProfileLcpMagicNumber_Object = MibTableColumn
usdPppProfileLcpMagicNumber = _UsdPppProfileLcpMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 3),
    _UsdPppProfileLcpMagicNumber_Type()
)
usdPppProfileLcpMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileLcpMagicNumber.setStatus("current")


class _UsdPppProfileLcpKeepalive_Type(Integer32):
    """Custom type usdPppProfileLcpKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 300),
    )


_UsdPppProfileLcpKeepalive_Type.__name__ = "Integer32"
_UsdPppProfileLcpKeepalive_Object = MibTableColumn
usdPppProfileLcpKeepalive = _UsdPppProfileLcpKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 4),
    _UsdPppProfileLcpKeepalive_Type()
)
usdPppProfileLcpKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileLcpKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    usdPppProfileLcpKeepalive.setUnits("seconds")


class _UsdPppProfileLcpAuthentication_Type(UsdPppAuthentication):
    """Custom type usdPppProfileLcpAuthentication based on UsdPppAuthentication"""


_UsdPppProfileLcpAuthentication_Object = MibTableColumn
usdPppProfileLcpAuthentication = _UsdPppProfileLcpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 5),
    _UsdPppProfileLcpAuthentication_Type()
)
usdPppProfileLcpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileLcpAuthentication.setStatus("current")


class _UsdPppProfileIpPeerDnsPriority_Type(UsdEnable):
    """Custom type usdPppProfileIpPeerDnsPriority based on UsdEnable"""


_UsdPppProfileIpPeerDnsPriority_Object = MibTableColumn
usdPppProfileIpPeerDnsPriority = _UsdPppProfileIpPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 6),
    _UsdPppProfileIpPeerDnsPriority_Type()
)
usdPppProfileIpPeerDnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileIpPeerDnsPriority.setStatus("current")


class _UsdPppProfileIpPeerWinsPriority_Type(UsdEnable):
    """Custom type usdPppProfileIpPeerWinsPriority based on UsdEnable"""


_UsdPppProfileIpPeerWinsPriority_Object = MibTableColumn
usdPppProfileIpPeerWinsPriority = _UsdPppProfileIpPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 7),
    _UsdPppProfileIpPeerWinsPriority_Type()
)
usdPppProfileIpPeerWinsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileIpPeerWinsPriority.setStatus("current")


class _UsdPppProfileLcpInitialMRU_Type(Integer32):
    """Custom type usdPppProfileLcpInitialMRU based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(64, 65535),
    )


_UsdPppProfileLcpInitialMRU_Type.__name__ = "Integer32"
_UsdPppProfileLcpInitialMRU_Object = MibTableColumn
usdPppProfileLcpInitialMRU = _UsdPppProfileLcpInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 8),
    _UsdPppProfileLcpInitialMRU_Type()
)
usdPppProfileLcpInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileLcpInitialMRU.setStatus("current")


class _UsdPppProfilePacketLog_Type(UsdEnable):
    """Custom type usdPppProfilePacketLog based on UsdEnable"""


_UsdPppProfilePacketLog_Object = MibTableColumn
usdPppProfilePacketLog = _UsdPppProfilePacketLog_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 9),
    _UsdPppProfilePacketLog_Type()
)
usdPppProfilePacketLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfilePacketLog.setStatus("current")


class _UsdPppProfileStateLog_Type(UsdEnable):
    """Custom type usdPppProfileStateLog based on UsdEnable"""


_UsdPppProfileStateLog_Object = MibTableColumn
usdPppProfileStateLog = _UsdPppProfileStateLog_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 10),
    _UsdPppProfileStateLog_Type()
)
usdPppProfileStateLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileStateLog.setStatus("current")


class _UsdPppProfileChapMinChallengeLength_Type(Integer32):
    """Custom type usdPppProfileChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_UsdPppProfileChapMinChallengeLength_Type.__name__ = "Integer32"
_UsdPppProfileChapMinChallengeLength_Object = MibTableColumn
usdPppProfileChapMinChallengeLength = _UsdPppProfileChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 11),
    _UsdPppProfileChapMinChallengeLength_Type()
)
usdPppProfileChapMinChallengeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileChapMinChallengeLength.setStatus("current")


class _UsdPppProfileChapMaxChallengeLength_Type(Integer32):
    """Custom type usdPppProfileChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_UsdPppProfileChapMaxChallengeLength_Type.__name__ = "Integer32"
_UsdPppProfileChapMaxChallengeLength_Object = MibTableColumn
usdPppProfileChapMaxChallengeLength = _UsdPppProfileChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 12),
    _UsdPppProfileChapMaxChallengeLength_Type()
)
usdPppProfileChapMaxChallengeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileChapMaxChallengeLength.setStatus("current")


class _UsdPppProfilePassiveMode_Type(UsdEnable):
    """Custom type usdPppProfilePassiveMode based on UsdEnable"""


_UsdPppProfilePassiveMode_Object = MibTableColumn
usdPppProfilePassiveMode = _UsdPppProfilePassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 13),
    _UsdPppProfilePassiveMode_Type()
)
usdPppProfilePassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfilePassiveMode.setStatus("current")


class _UsdPppProfileMlppp_Type(UsdEnable):
    """Custom type usdPppProfileMlppp based on UsdEnable"""


_UsdPppProfileMlppp_Object = MibTableColumn
usdPppProfileMlppp = _UsdPppProfileMlppp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 14),
    _UsdPppProfileMlppp_Type()
)
usdPppProfileMlppp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileMlppp.setStatus("current")


class _UsdPppProfileIpcpNetmask_Type(UsdEnable):
    """Custom type usdPppProfileIpcpNetmask based on UsdEnable"""


_UsdPppProfileIpcpNetmask_Object = MibTableColumn
usdPppProfileIpcpNetmask = _UsdPppProfileIpcpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 15),
    _UsdPppProfileIpcpNetmask_Type()
)
usdPppProfileIpcpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileIpcpNetmask.setStatus("current")
_UsdPppProfileAuthenticatorVirtualRouter_Type = UsdName
_UsdPppProfileAuthenticatorVirtualRouter_Object = MibTableColumn
usdPppProfileAuthenticatorVirtualRouter = _UsdPppProfileAuthenticatorVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 16),
    _UsdPppProfileAuthenticatorVirtualRouter_Type()
)
usdPppProfileAuthenticatorVirtualRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppProfileAuthenticatorVirtualRouter.setStatus("current")
_UsdPppProfileConformance_ObjectIdentity = ObjectIdentity
usdPppProfileConformance = _UsdPppProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4)
)
_UsdPppProfileCompliances_ObjectIdentity = ObjectIdentity
usdPppProfileCompliances = _UsdPppProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1)
)
_UsdPppProfileGroups_ObjectIdentity = ObjectIdentity
usdPppProfileGroups = _UsdPppProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2)
)

# Managed Objects groups

usdPppProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 1)
)
usdPppProfileGroup.setObjects(
      *(("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileSetMap"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpMagicNumber"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpKeepalive"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpAuthentication"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerDnsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerWinsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpInitialMRU"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePacketLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileStateLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMinChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMaxChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePassiveMode"))
)
if mibBuilder.loadTexts:
    usdPppProfileGroup.setStatus("obsolete")

usdPppProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 2)
)
usdPppProfileGroup2.setObjects(
      *(("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileSetMap"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpMagicNumber"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpKeepalive"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpAuthentication"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerDnsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerWinsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpInitialMRU"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePacketLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileStateLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMinChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMaxChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePassiveMode"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileMlppp"))
)
if mibBuilder.loadTexts:
    usdPppProfileGroup2.setStatus("obsolete")

usdPppProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 3)
)
usdPppProfileGroup3.setObjects(
      *(("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileSetMap"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpMagicNumber"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpKeepalive"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpAuthentication"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerDnsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerWinsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpInitialMRU"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePacketLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileStateLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMinChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMaxChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePassiveMode"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileMlppp"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpcpNetmask"))
)
if mibBuilder.loadTexts:
    usdPppProfileGroup3.setStatus("obsolete")

usdPppProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 4)
)
usdPppProfileGroup4.setObjects(
      *(("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileSetMap"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpMagicNumber"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpKeepalive"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpAuthentication"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerDnsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpPeerWinsPriority"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileLcpInitialMRU"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePacketLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileStateLog"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMinChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileChapMaxChallengeLength"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfilePassiveMode"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileMlppp"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileIpcpNetmask"),
        ("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileAuthenticatorVirtualRouter"))
)
if mibBuilder.loadTexts:
    usdPppProfileGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPppProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppProfileCompliance.setStatus(
        "obsolete"
    )

usdPppProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdPppProfileCompliance2.setStatus(
        "obsolete"
    )

usdPppProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdPppProfileCompliance3.setStatus(
        "obsolete"
    )

usdPppProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdPppProfileCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPP-PROFILE-MIB",
    **{"usdPppProfileMIB": usdPppProfileMIB,
       "usdPppProfileObjects": usdPppProfileObjects,
       "usdPppProfile": usdPppProfile,
       "usdPppProfileTable": usdPppProfileTable,
       "usdPppProfileEntry": usdPppProfileEntry,
       "usdPppProfileId": usdPppProfileId,
       "usdPppProfileSetMap": usdPppProfileSetMap,
       "usdPppProfileLcpMagicNumber": usdPppProfileLcpMagicNumber,
       "usdPppProfileLcpKeepalive": usdPppProfileLcpKeepalive,
       "usdPppProfileLcpAuthentication": usdPppProfileLcpAuthentication,
       "usdPppProfileIpPeerDnsPriority": usdPppProfileIpPeerDnsPriority,
       "usdPppProfileIpPeerWinsPriority": usdPppProfileIpPeerWinsPriority,
       "usdPppProfileLcpInitialMRU": usdPppProfileLcpInitialMRU,
       "usdPppProfilePacketLog": usdPppProfilePacketLog,
       "usdPppProfileStateLog": usdPppProfileStateLog,
       "usdPppProfileChapMinChallengeLength": usdPppProfileChapMinChallengeLength,
       "usdPppProfileChapMaxChallengeLength": usdPppProfileChapMaxChallengeLength,
       "usdPppProfilePassiveMode": usdPppProfilePassiveMode,
       "usdPppProfileMlppp": usdPppProfileMlppp,
       "usdPppProfileIpcpNetmask": usdPppProfileIpcpNetmask,
       "usdPppProfileAuthenticatorVirtualRouter": usdPppProfileAuthenticatorVirtualRouter,
       "usdPppProfileConformance": usdPppProfileConformance,
       "usdPppProfileCompliances": usdPppProfileCompliances,
       "usdPppProfileCompliance": usdPppProfileCompliance,
       "usdPppProfileCompliance2": usdPppProfileCompliance2,
       "usdPppProfileCompliance3": usdPppProfileCompliance3,
       "usdPppProfileCompliance4": usdPppProfileCompliance4,
       "usdPppProfileGroups": usdPppProfileGroups,
       "usdPppProfileGroup": usdPppProfileGroup,
       "usdPppProfileGroup2": usdPppProfileGroup2,
       "usdPppProfileGroup3": usdPppProfileGroup3,
       "usdPppProfileGroup4": usdPppProfileGroup4}
)
