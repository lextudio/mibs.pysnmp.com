# SNMP MIB module (Juniper-PPP-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPP-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:58 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniPppAuthentication,) = mibBuilder.importSymbols(
    "Juniper-PPP-MIB",
    "JuniPppAuthentication")

(JuniEnable,
 JuniName,
 JuniNibbleConfig,
 JuniSetMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniName",
    "JuniNibbleConfig",
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

juniPppProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45)
)
juniPppProfileMIB.setRevisions(
        ("2009-09-18 07:24",
         "2009-08-10 14:23",
         "2007-07-12 12:15",
         "2005-10-19 16:26",
         "2003-11-03 21:10",
         "2003-09-29 18:58",
         "2003-03-11 21:59",
         "2002-09-16 21:44",
         "2002-09-03 22:38",
         "2002-01-25 14:00",
         "2002-01-16 17:58",
         "2002-01-08 19:43",
         "2001-10-02 12:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniPppProfileMulticlassTcName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_JuniPppProfileObjects_ObjectIdentity = ObjectIdentity
juniPppProfileObjects = _JuniPppProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1)
)
_JuniPppProfile_ObjectIdentity = ObjectIdentity
juniPppProfile = _JuniPppProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1)
)
_JuniPppProfileTable_Object = MibTable
juniPppProfileTable = _JuniPppProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppProfileTable.setStatus("current")
_JuniPppProfileEntry_Object = MibTableRow
juniPppProfileEntry = _JuniPppProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1)
)
juniPppProfileEntry.setIndexNames(
    (0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileId"),
)
if mibBuilder.loadTexts:
    juniPppProfileEntry.setStatus("current")
_JuniPppProfileId_Type = Unsigned32
_JuniPppProfileId_Object = MibTableColumn
juniPppProfileId = _JuniPppProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 1),
    _JuniPppProfileId_Type()
)
juniPppProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppProfileId.setStatus("current")
_JuniPppProfileSetMap_Type = JuniSetMap
_JuniPppProfileSetMap_Object = MibTableColumn
juniPppProfileSetMap = _JuniPppProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 2),
    _JuniPppProfileSetMap_Type()
)
juniPppProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileSetMap.setStatus("current")


class _JuniPppProfileLcpMagicNumber_Type(Integer32):
    """Custom type juniPppProfileLcpMagicNumber based on Integer32"""
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


_JuniPppProfileLcpMagicNumber_Type.__name__ = "Integer32"
_JuniPppProfileLcpMagicNumber_Object = MibTableColumn
juniPppProfileLcpMagicNumber = _JuniPppProfileLcpMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 3),
    _JuniPppProfileLcpMagicNumber_Type()
)
juniPppProfileLcpMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileLcpMagicNumber.setStatus("current")


class _JuniPppProfileLcpKeepalive_Type(Integer32):
    """Custom type juniPppProfileLcpKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 64800),
    )


_JuniPppProfileLcpKeepalive_Type.__name__ = "Integer32"
_JuniPppProfileLcpKeepalive_Object = MibTableColumn
juniPppProfileLcpKeepalive = _JuniPppProfileLcpKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 4),
    _JuniPppProfileLcpKeepalive_Type()
)
juniPppProfileLcpKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileLcpKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    juniPppProfileLcpKeepalive.setUnits("seconds")


class _JuniPppProfileLcpAuthentication_Type(JuniPppAuthentication):
    """Custom type juniPppProfileLcpAuthentication based on JuniPppAuthentication"""


_JuniPppProfileLcpAuthentication_Object = MibTableColumn
juniPppProfileLcpAuthentication = _JuniPppProfileLcpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 5),
    _JuniPppProfileLcpAuthentication_Type()
)
juniPppProfileLcpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileLcpAuthentication.setStatus("deprecated")


class _JuniPppProfileIpPeerDnsPriority_Type(JuniEnable):
    """Custom type juniPppProfileIpPeerDnsPriority based on JuniEnable"""


_JuniPppProfileIpPeerDnsPriority_Object = MibTableColumn
juniPppProfileIpPeerDnsPriority = _JuniPppProfileIpPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 6),
    _JuniPppProfileIpPeerDnsPriority_Type()
)
juniPppProfileIpPeerDnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIpPeerDnsPriority.setStatus("current")


class _JuniPppProfileIpPeerWinsPriority_Type(JuniEnable):
    """Custom type juniPppProfileIpPeerWinsPriority based on JuniEnable"""


_JuniPppProfileIpPeerWinsPriority_Object = MibTableColumn
juniPppProfileIpPeerWinsPriority = _JuniPppProfileIpPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 7),
    _JuniPppProfileIpPeerWinsPriority_Type()
)
juniPppProfileIpPeerWinsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIpPeerWinsPriority.setStatus("current")


class _JuniPppProfileLcpInitialMRU_Type(Integer32):
    """Custom type juniPppProfileLcpInitialMRU based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(64, 65535),
    )


_JuniPppProfileLcpInitialMRU_Type.__name__ = "Integer32"
_JuniPppProfileLcpInitialMRU_Object = MibTableColumn
juniPppProfileLcpInitialMRU = _JuniPppProfileLcpInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 8),
    _JuniPppProfileLcpInitialMRU_Type()
)
juniPppProfileLcpInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileLcpInitialMRU.setStatus("current")


class _JuniPppProfilePacketLog_Type(JuniEnable):
    """Custom type juniPppProfilePacketLog based on JuniEnable"""


_JuniPppProfilePacketLog_Object = MibTableColumn
juniPppProfilePacketLog = _JuniPppProfilePacketLog_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 9),
    _JuniPppProfilePacketLog_Type()
)
juniPppProfilePacketLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfilePacketLog.setStatus("current")


class _JuniPppProfileStateLog_Type(JuniEnable):
    """Custom type juniPppProfileStateLog based on JuniEnable"""


_JuniPppProfileStateLog_Object = MibTableColumn
juniPppProfileStateLog = _JuniPppProfileStateLog_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 10),
    _JuniPppProfileStateLog_Type()
)
juniPppProfileStateLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileStateLog.setStatus("current")


class _JuniPppProfileChapMinChallengeLength_Type(Integer32):
    """Custom type juniPppProfileChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppProfileChapMinChallengeLength_Type.__name__ = "Integer32"
_JuniPppProfileChapMinChallengeLength_Object = MibTableColumn
juniPppProfileChapMinChallengeLength = _JuniPppProfileChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 11),
    _JuniPppProfileChapMinChallengeLength_Type()
)
juniPppProfileChapMinChallengeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileChapMinChallengeLength.setStatus("current")


class _JuniPppProfileChapMaxChallengeLength_Type(Integer32):
    """Custom type juniPppProfileChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppProfileChapMaxChallengeLength_Type.__name__ = "Integer32"
_JuniPppProfileChapMaxChallengeLength_Object = MibTableColumn
juniPppProfileChapMaxChallengeLength = _JuniPppProfileChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 12),
    _JuniPppProfileChapMaxChallengeLength_Type()
)
juniPppProfileChapMaxChallengeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileChapMaxChallengeLength.setStatus("current")


class _JuniPppProfilePassiveMode_Type(JuniEnable):
    """Custom type juniPppProfilePassiveMode based on JuniEnable"""


_JuniPppProfilePassiveMode_Object = MibTableColumn
juniPppProfilePassiveMode = _JuniPppProfilePassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 13),
    _JuniPppProfilePassiveMode_Type()
)
juniPppProfilePassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfilePassiveMode.setStatus("current")


class _JuniPppProfileMlppp_Type(JuniEnable):
    """Custom type juniPppProfileMlppp based on JuniEnable"""


_JuniPppProfileMlppp_Object = MibTableColumn
juniPppProfileMlppp = _JuniPppProfileMlppp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 14),
    _JuniPppProfileMlppp_Type()
)
juniPppProfileMlppp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileMlppp.setStatus("current")


class _JuniPppProfileIpcpNetmask_Type(JuniEnable):
    """Custom type juniPppProfileIpcpNetmask based on JuniEnable"""


_JuniPppProfileIpcpNetmask_Object = MibTableColumn
juniPppProfileIpcpNetmask = _JuniPppProfileIpcpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 15),
    _JuniPppProfileIpcpNetmask_Type()
)
juniPppProfileIpcpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIpcpNetmask.setStatus("current")
_JuniPppProfileAuthenticatorVirtualRouter_Type = JuniName
_JuniPppProfileAuthenticatorVirtualRouter_Object = MibTableColumn
juniPppProfileAuthenticatorVirtualRouter = _JuniPppProfileAuthenticatorVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 16),
    _JuniPppProfileAuthenticatorVirtualRouter_Type()
)
juniPppProfileAuthenticatorVirtualRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileAuthenticatorVirtualRouter.setStatus("current")
_JuniPppProfileAaaProfile_Type = JuniName
_JuniPppProfileAaaProfile_Object = MibTableColumn
juniPppProfileAaaProfile = _JuniPppProfileAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 17),
    _JuniPppProfileAaaProfile_Type()
)
juniPppProfileAaaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileAaaProfile.setStatus("current")


class _JuniPppProfileInitiateIp_Type(JuniEnable):
    """Custom type juniPppProfileInitiateIp based on JuniEnable"""


_JuniPppProfileInitiateIp_Object = MibTableColumn
juniPppProfileInitiateIp = _JuniPppProfileInitiateIp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 18),
    _JuniPppProfileInitiateIp_Type()
)
juniPppProfileInitiateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileInitiateIp.setStatus("current")


class _JuniPppProfileInitiateIpv6_Type(JuniEnable):
    """Custom type juniPppProfileInitiateIpv6 based on JuniEnable"""


_JuniPppProfileInitiateIpv6_Object = MibTableColumn
juniPppProfileInitiateIpv6 = _JuniPppProfileInitiateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 19),
    _JuniPppProfileInitiateIpv6_Type()
)
juniPppProfileInitiateIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileInitiateIpv6.setStatus("current")


class _JuniPppProfileFragmentation_Type(JuniEnable):
    """Custom type juniPppProfileFragmentation based on JuniEnable"""


_JuniPppProfileFragmentation_Object = MibTableColumn
juniPppProfileFragmentation = _JuniPppProfileFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 20),
    _JuniPppProfileFragmentation_Type()
)
juniPppProfileFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileFragmentation.setStatus("current")


class _JuniPppProfileReassembly_Type(JuniEnable):
    """Custom type juniPppProfileReassembly based on JuniEnable"""


_JuniPppProfileReassembly_Object = MibTableColumn
juniPppProfileReassembly = _JuniPppProfileReassembly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 21),
    _JuniPppProfileReassembly_Type()
)
juniPppProfileReassembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileReassembly.setStatus("current")


class _JuniPppProfileMaxReceiveReconstructedUnit_Type(Integer32):
    """Custom type juniPppProfileMaxReceiveReconstructedUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(64, 65535),
    )


_JuniPppProfileMaxReceiveReconstructedUnit_Type.__name__ = "Integer32"
_JuniPppProfileMaxReceiveReconstructedUnit_Object = MibTableColumn
juniPppProfileMaxReceiveReconstructedUnit = _JuniPppProfileMaxReceiveReconstructedUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 22),
    _JuniPppProfileMaxReceiveReconstructedUnit_Type()
)
juniPppProfileMaxReceiveReconstructedUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileMaxReceiveReconstructedUnit.setStatus("current")


class _JuniPppProfileFragmentSize_Type(Integer32):
    """Custom type juniPppProfileFragmentSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(128, 65535),
    )


_JuniPppProfileFragmentSize_Type.__name__ = "Integer32"
_JuniPppProfileFragmentSize_Object = MibTableColumn
juniPppProfileFragmentSize = _JuniPppProfileFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 23),
    _JuniPppProfileFragmentSize_Type()
)
juniPppProfileFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileFragmentSize.setStatus("current")


class _JuniPppProfileHashLinkSelection_Type(JuniEnable):
    """Custom type juniPppProfileHashLinkSelection based on JuniEnable"""


_JuniPppProfileHashLinkSelection_Object = MibTableColumn
juniPppProfileHashLinkSelection = _JuniPppProfileHashLinkSelection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 24),
    _JuniPppProfileHashLinkSelection_Type()
)
juniPppProfileHashLinkSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileHashLinkSelection.setStatus("current")


class _JuniPppProfileLcpAuthentication2_Type(JuniNibbleConfig):
    """Custom type juniPppProfileLcpAuthentication2 based on JuniNibbleConfig"""
    defaultValue = 0


_JuniPppProfileLcpAuthentication2_Object = MibTableColumn
juniPppProfileLcpAuthentication2 = _JuniPppProfileLcpAuthentication2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 25),
    _JuniPppProfileLcpAuthentication2_Type()
)
juniPppProfileLcpAuthentication2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileLcpAuthentication2.setStatus("current")


class _JuniPppProfileIgnoreMagicNumberMismatch_Type(JuniEnable):
    """Custom type juniPppProfileIgnoreMagicNumberMismatch based on JuniEnable"""


_JuniPppProfileIgnoreMagicNumberMismatch_Object = MibTableColumn
juniPppProfileIgnoreMagicNumberMismatch = _JuniPppProfileIgnoreMagicNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 26),
    _JuniPppProfileIgnoreMagicNumberMismatch_Type()
)
juniPppProfileIgnoreMagicNumberMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIgnoreMagicNumberMismatch.setStatus("current")


class _JuniPppProfileIpcpPromptDnsOption_Type(JuniEnable):
    """Custom type juniPppProfileIpcpPromptDnsOption based on JuniEnable"""


_JuniPppProfileIpcpPromptDnsOption_Object = MibTableColumn
juniPppProfileIpcpPromptDnsOption = _JuniPppProfileIpcpPromptDnsOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 27),
    _JuniPppProfileIpcpPromptDnsOption_Type()
)
juniPppProfileIpcpPromptDnsOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIpcpPromptDnsOption.setStatus("current")


class _JuniPppProfileIpcpLockout_Type(JuniEnable):
    """Custom type juniPppProfileIpcpLockout based on JuniEnable"""


_JuniPppProfileIpcpLockout_Object = MibTableColumn
juniPppProfileIpcpLockout = _JuniPppProfileIpcpLockout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 28),
    _JuniPppProfileIpcpLockout_Type()
)
juniPppProfileIpcpLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileIpcpLockout.setStatus("current")


class _JuniPppProfileMultilinkMulticlass_Type(JuniEnable):
    """Custom type juniPppProfileMultilinkMulticlass based on JuniEnable"""


_JuniPppProfileMultilinkMulticlass_Object = MibTableColumn
juniPppProfileMultilinkMulticlass = _JuniPppProfileMultilinkMulticlass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 29),
    _JuniPppProfileMultilinkMulticlass_Type()
)
juniPppProfileMultilinkMulticlass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppProfileMultilinkMulticlass.setStatus("current")


class _JuniPppProfileMultilinkMaxMultiClasses_Type(Integer32):
    """Custom type juniPppProfileMultilinkMaxMultiClasses based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_JuniPppProfileMultilinkMaxMultiClasses_Type.__name__ = "Integer32"
_JuniPppProfileMultilinkMaxMultiClasses_Object = MibTableColumn
juniPppProfileMultilinkMaxMultiClasses = _JuniPppProfileMultilinkMaxMultiClasses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 30),
    _JuniPppProfileMultilinkMaxMultiClasses_Type()
)
juniPppProfileMultilinkMaxMultiClasses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppProfileMultilinkMaxMultiClasses.setStatus("current")
_JuniPppProfileMulticlassTraffiClassTable_Object = MibTable
juniPppProfileMulticlassTraffiClassTable = _JuniPppProfileMulticlassTraffiClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniPppProfileMulticlassTraffiClassTable.setStatus("current")
_JuniPppProfileMulticlassTrafficClassEntry_Object = MibTableRow
juniPppProfileMulticlassTrafficClassEntry = _JuniPppProfileMulticlassTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1)
)
juniPppProfileMulticlassTrafficClassEntry.setIndexNames(
    (0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileId"),
    (0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassIndex"),
)
if mibBuilder.loadTexts:
    juniPppProfileMulticlassTrafficClassEntry.setStatus("current")
_JuniPppProfileMulticlassId_Type = Unsigned32
_JuniPppProfileMulticlassId_Object = MibTableColumn
juniPppProfileMulticlassId = _JuniPppProfileMulticlassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 1),
    _JuniPppProfileMulticlassId_Type()
)
juniPppProfileMulticlassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppProfileMulticlassId.setStatus("current")


class _JuniPppProfileMulticlassIndex_Type(Integer32):
    """Custom type juniPppProfileMulticlassIndex based on Integer32"""
    defaultValue = 15


_JuniPppProfileMulticlassIndex_Object = MibTableColumn
juniPppProfileMulticlassIndex = _JuniPppProfileMulticlassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 2),
    _JuniPppProfileMulticlassIndex_Type()
)
juniPppProfileMulticlassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppProfileMulticlassIndex.setStatus("current")
_JuniPppProfileMulticlassTcName_Type = JuniPppProfileMulticlassTcName
_JuniPppProfileMulticlassTcName_Object = MibTableColumn
juniPppProfileMulticlassTcName = _JuniPppProfileMulticlassTcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 3),
    _JuniPppProfileMulticlassTcName_Type()
)
juniPppProfileMulticlassTcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileMulticlassTcName.setStatus("current")


class _JuniPppProfileMulticlassFragmentation_Type(JuniEnable):
    """Custom type juniPppProfileMulticlassFragmentation based on JuniEnable"""


_JuniPppProfileMulticlassFragmentation_Object = MibTableColumn
juniPppProfileMulticlassFragmentation = _JuniPppProfileMulticlassFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 4),
    _JuniPppProfileMulticlassFragmentation_Type()
)
juniPppProfileMulticlassFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileMulticlassFragmentation.setStatus("current")


class _JuniPppProfileMulticlassReassembly_Type(JuniEnable):
    """Custom type juniPppProfileMulticlassReassembly based on JuniEnable"""


_JuniPppProfileMulticlassReassembly_Object = MibTableColumn
juniPppProfileMulticlassReassembly = _JuniPppProfileMulticlassReassembly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 5),
    _JuniPppProfileMulticlassReassembly_Type()
)
juniPppProfileMulticlassReassembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppProfileMulticlassReassembly.setStatus("current")
_JuniPppProfileConformance_ObjectIdentity = ObjectIdentity
juniPppProfileConformance = _JuniPppProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4)
)
_JuniPppProfileCompliances_ObjectIdentity = ObjectIdentity
juniPppProfileCompliances = _JuniPppProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1)
)
_JuniPppProfileGroups_ObjectIdentity = ObjectIdentity
juniPppProfileGroups = _JuniPppProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2)
)

# Managed Objects groups

juniPppProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 1)
)
juniPppProfileGroup.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup.setStatus("obsolete")

juniPppProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 2)
)
juniPppProfileGroup2.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup2.setStatus("obsolete")

juniPppProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 3)
)
juniPppProfileGroup3.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup3.setStatus("obsolete")

juniPppProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 4)
)
juniPppProfileGroup4.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup4.setStatus("obsolete")

juniPppProfileGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 5)
)
juniPppProfileGroup5.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup5.setStatus("obsolete")

juniPppProfileGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 6)
)
juniPppProfileGroup6.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup6.setStatus("obsolete")

juniPppProfileGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 7)
)
juniPppProfileGroup7.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup7.setStatus("obsolete")

juniPppProfileGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 8)
)
juniPppProfileGroup8.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup8.setStatus("obsolete")

juniPppProfileGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 9)
)
juniPppProfileGroup9.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup9.setStatus("obsolete")

juniPppProfileGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 10)
)
juniPppProfileGroup10.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup10.setStatus("obsolete")

juniPppProfileGroup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 11)
)
juniPppProfileGroup11.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpPromptDnsOption"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpLockout"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup11.setStatus("current")

juniPppProfileGroup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 12)
)
juniPppProfileGroup12.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMultilinkMulticlass"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMultilinkMaxMultiClasses"))
)
if mibBuilder.loadTexts:
    juniPppProfileGroup12.setStatus("current")

juniPppProfileMulticlassTrafficClassGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 13)
)
juniPppProfileMulticlassTrafficClassGroup1.setObjects(
      *(("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassTcName"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassFragmentation"),
        ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassReassembly"))
)
if mibBuilder.loadTexts:
    juniPppProfileMulticlassTrafficClassGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPppProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance.setStatus(
        "obsolete"
    )

juniPppProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance2.setStatus(
        "obsolete"
    )

juniPppProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance3.setStatus(
        "obsolete"
    )

juniPppProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance4.setStatus(
        "obsolete"
    )

juniPppProfileCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance5.setStatus(
        "obsolete"
    )

juniPppProfileCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance6.setStatus(
        "obsolete"
    )

juniPppProfileCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance7.setStatus(
        "obsolete"
    )

juniPppProfileCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance8.setStatus(
        "obsolete"
    )

juniPppProfileCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance9.setStatus(
        "obsolete"
    )

juniPppProfileCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniPppProfileCompliance10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPP-PROFILE-MIB",
    **{"JuniPppProfileMulticlassTcName": JuniPppProfileMulticlassTcName,
       "juniPppProfileMIB": juniPppProfileMIB,
       "juniPppProfileObjects": juniPppProfileObjects,
       "juniPppProfile": juniPppProfile,
       "juniPppProfileTable": juniPppProfileTable,
       "juniPppProfileEntry": juniPppProfileEntry,
       "juniPppProfileId": juniPppProfileId,
       "juniPppProfileSetMap": juniPppProfileSetMap,
       "juniPppProfileLcpMagicNumber": juniPppProfileLcpMagicNumber,
       "juniPppProfileLcpKeepalive": juniPppProfileLcpKeepalive,
       "juniPppProfileLcpAuthentication": juniPppProfileLcpAuthentication,
       "juniPppProfileIpPeerDnsPriority": juniPppProfileIpPeerDnsPriority,
       "juniPppProfileIpPeerWinsPriority": juniPppProfileIpPeerWinsPriority,
       "juniPppProfileLcpInitialMRU": juniPppProfileLcpInitialMRU,
       "juniPppProfilePacketLog": juniPppProfilePacketLog,
       "juniPppProfileStateLog": juniPppProfileStateLog,
       "juniPppProfileChapMinChallengeLength": juniPppProfileChapMinChallengeLength,
       "juniPppProfileChapMaxChallengeLength": juniPppProfileChapMaxChallengeLength,
       "juniPppProfilePassiveMode": juniPppProfilePassiveMode,
       "juniPppProfileMlppp": juniPppProfileMlppp,
       "juniPppProfileIpcpNetmask": juniPppProfileIpcpNetmask,
       "juniPppProfileAuthenticatorVirtualRouter": juniPppProfileAuthenticatorVirtualRouter,
       "juniPppProfileAaaProfile": juniPppProfileAaaProfile,
       "juniPppProfileInitiateIp": juniPppProfileInitiateIp,
       "juniPppProfileInitiateIpv6": juniPppProfileInitiateIpv6,
       "juniPppProfileFragmentation": juniPppProfileFragmentation,
       "juniPppProfileReassembly": juniPppProfileReassembly,
       "juniPppProfileMaxReceiveReconstructedUnit": juniPppProfileMaxReceiveReconstructedUnit,
       "juniPppProfileFragmentSize": juniPppProfileFragmentSize,
       "juniPppProfileHashLinkSelection": juniPppProfileHashLinkSelection,
       "juniPppProfileLcpAuthentication2": juniPppProfileLcpAuthentication2,
       "juniPppProfileIgnoreMagicNumberMismatch": juniPppProfileIgnoreMagicNumberMismatch,
       "juniPppProfileIpcpPromptDnsOption": juniPppProfileIpcpPromptDnsOption,
       "juniPppProfileIpcpLockout": juniPppProfileIpcpLockout,
       "juniPppProfileMultilinkMulticlass": juniPppProfileMultilinkMulticlass,
       "juniPppProfileMultilinkMaxMultiClasses": juniPppProfileMultilinkMaxMultiClasses,
       "juniPppProfileMulticlassTraffiClassTable": juniPppProfileMulticlassTraffiClassTable,
       "juniPppProfileMulticlassTrafficClassEntry": juniPppProfileMulticlassTrafficClassEntry,
       "juniPppProfileMulticlassId": juniPppProfileMulticlassId,
       "juniPppProfileMulticlassIndex": juniPppProfileMulticlassIndex,
       "juniPppProfileMulticlassTcName": juniPppProfileMulticlassTcName,
       "juniPppProfileMulticlassFragmentation": juniPppProfileMulticlassFragmentation,
       "juniPppProfileMulticlassReassembly": juniPppProfileMulticlassReassembly,
       "juniPppProfileConformance": juniPppProfileConformance,
       "juniPppProfileCompliances": juniPppProfileCompliances,
       "juniPppProfileCompliance": juniPppProfileCompliance,
       "juniPppProfileCompliance2": juniPppProfileCompliance2,
       "juniPppProfileCompliance3": juniPppProfileCompliance3,
       "juniPppProfileCompliance4": juniPppProfileCompliance4,
       "juniPppProfileCompliance5": juniPppProfileCompliance5,
       "juniPppProfileCompliance6": juniPppProfileCompliance6,
       "juniPppProfileCompliance7": juniPppProfileCompliance7,
       "juniPppProfileCompliance8": juniPppProfileCompliance8,
       "juniPppProfileCompliance9": juniPppProfileCompliance9,
       "juniPppProfileCompliance10": juniPppProfileCompliance10,
       "juniPppProfileGroups": juniPppProfileGroups,
       "juniPppProfileGroup": juniPppProfileGroup,
       "juniPppProfileGroup2": juniPppProfileGroup2,
       "juniPppProfileGroup3": juniPppProfileGroup3,
       "juniPppProfileGroup4": juniPppProfileGroup4,
       "juniPppProfileGroup5": juniPppProfileGroup5,
       "juniPppProfileGroup6": juniPppProfileGroup6,
       "juniPppProfileGroup7": juniPppProfileGroup7,
       "juniPppProfileGroup8": juniPppProfileGroup8,
       "juniPppProfileGroup9": juniPppProfileGroup9,
       "juniPppProfileGroup10": juniPppProfileGroup10,
       "juniPppProfileGroup11": juniPppProfileGroup11,
       "juniPppProfileGroup12": juniPppProfileGroup12,
       "juniPppProfileMulticlassTrafficClassGroup1": juniPppProfileMulticlassTrafficClassGroup1}
)
