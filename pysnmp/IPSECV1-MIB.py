# SNMP MIB module (IPSECV1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSECV1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:18 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class IPSIpAddress(OctetString):
    """Custom type IPSIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmIROCroutingIpSec_ObjectIdentity = ObjectIdentity
ibmIROCroutingIpSec = _IbmIROCroutingIpSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9)
)
_IpSecLevels_ObjectIdentity = ObjectIdentity
ipSecLevels = _IpSecLevels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 1)
)
_IpSecMibLevel_Type = Integer32
_IpSecMibLevel_Object = MibScalar
ipSecMibLevel = _IpSecMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 1, 1),
    _IpSecMibLevel_Type()
)
ipSecMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecMibLevel.setStatus("mandatory")
_IpSecPhaseOne_ObjectIdentity = ObjectIdentity
ipSecPhaseOne = _IpSecPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2)
)
_IkeTunnelTable_Object = MibTable
ikeTunnelTable = _IkeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1)
)
if mibBuilder.loadTexts:
    ikeTunnelTable.setStatus("mandatory")
_IkeTunnelEntry_Object = MibTableRow
ikeTunnelEntry = _IkeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1)
)
ikeTunnelEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ikeTunnelIndex"),
)
if mibBuilder.loadTexts:
    ikeTunnelEntry.setStatus("mandatory")


class _IkeTunnelIndex_Type(Integer32):
    """Custom type ikeTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IkeTunnelIndex_Type.__name__ = "Integer32"
_IkeTunnelIndex_Object = MibTableColumn
ikeTunnelIndex = _IkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 1),
    _IkeTunnelIndex_Type()
)
ikeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelIndex.setStatus("mandatory")
_IkeTunnelId_Type = OctetString
_IkeTunnelId_Object = MibTableColumn
ikeTunnelId = _IkeTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 2),
    _IkeTunnelId_Type()
)
ikeTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelId.setStatus("mandatory")
_IkeTunnelLocalAddr_Type = IPSIpAddress
_IkeTunnelLocalAddr_Object = MibTableColumn
ikeTunnelLocalAddr = _IkeTunnelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 3),
    _IkeTunnelLocalAddr_Type()
)
ikeTunnelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelLocalAddr.setStatus("mandatory")
_IkeTunnelLocalName_Type = DisplayString
_IkeTunnelLocalName_Object = MibTableColumn
ikeTunnelLocalName = _IkeTunnelLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 4),
    _IkeTunnelLocalName_Type()
)
ikeTunnelLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelLocalName.setStatus("mandatory")
_IkeTunnelRemoteAddr_Type = IPSIpAddress
_IkeTunnelRemoteAddr_Object = MibTableColumn
ikeTunnelRemoteAddr = _IkeTunnelRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 5),
    _IkeTunnelRemoteAddr_Type()
)
ikeTunnelRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelRemoteAddr.setStatus("mandatory")
_IkeTunnelRemoteName_Type = DisplayString
_IkeTunnelRemoteName_Object = MibTableColumn
ikeTunnelRemoteName = _IkeTunnelRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 6),
    _IkeTunnelRemoteName_Type()
)
ikeTunnelRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelRemoteName.setStatus("mandatory")


class _IkeTunnelNegoMode_Type(Integer32):
    """Custom type ikeTunnelNegoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_IkeTunnelNegoMode_Type.__name__ = "Integer32"
_IkeTunnelNegoMode_Object = MibTableColumn
ikeTunnelNegoMode = _IkeTunnelNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 7),
    _IkeTunnelNegoMode_Type()
)
ikeTunnelNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelNegoMode.setStatus("mandatory")


class _IkeTunnelLifetime_Type(Integer32):
    """Custom type ikeTunnelLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IkeTunnelLifetime_Type.__name__ = "Integer32"
_IkeTunnelLifetime_Object = MibTableColumn
ikeTunnelLifetime = _IkeTunnelLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 8),
    _IkeTunnelLifetime_Type()
)
ikeTunnelLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelLifetime.setStatus("mandatory")
_IkeTunnelActiveTime_Type = TimeTicks
_IkeTunnelActiveTime_Object = MibTableColumn
ikeTunnelActiveTime = _IkeTunnelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 9),
    _IkeTunnelActiveTime_Type()
)
ikeTunnelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelActiveTime.setStatus("mandatory")


class _IkeTunnelSaRefreshThreshold_Type(Integer32):
    """Custom type ikeTunnelSaRefreshThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IkeTunnelSaRefreshThreshold_Type.__name__ = "Integer32"
_IkeTunnelSaRefreshThreshold_Object = MibTableColumn
ikeTunnelSaRefreshThreshold = _IkeTunnelSaRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 10),
    _IkeTunnelSaRefreshThreshold_Type()
)
ikeTunnelSaRefreshThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelSaRefreshThreshold.setStatus("mandatory")
_IkeTunnelTotalRefreshes_Type = Counter32
_IkeTunnelTotalRefreshes_Object = MibTableColumn
ikeTunnelTotalRefreshes = _IkeTunnelTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 11),
    _IkeTunnelTotalRefreshes_Type()
)
ikeTunnelTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelTotalRefreshes.setStatus("mandatory")
_IkeTunnelInOctets_Type = Counter32
_IkeTunnelInOctets_Object = MibTableColumn
ikeTunnelInOctets = _IkeTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 12),
    _IkeTunnelInOctets_Type()
)
ikeTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInOctets.setStatus("mandatory")
_IkeTunnelInPkts_Type = Counter32
_IkeTunnelInPkts_Object = MibTableColumn
ikeTunnelInPkts = _IkeTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 13),
    _IkeTunnelInPkts_Type()
)
ikeTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInPkts.setStatus("mandatory")
_IkeTunnelInDropPkts_Type = Counter32
_IkeTunnelInDropPkts_Object = MibTableColumn
ikeTunnelInDropPkts = _IkeTunnelInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 14),
    _IkeTunnelInDropPkts_Type()
)
ikeTunnelInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInDropPkts.setStatus("mandatory")
_IkeTunnelInNotifys_Type = Counter32
_IkeTunnelInNotifys_Object = MibTableColumn
ikeTunnelInNotifys = _IkeTunnelInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 15),
    _IkeTunnelInNotifys_Type()
)
ikeTunnelInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInNotifys.setStatus("mandatory")
_IkeTunnelInP2Proposals_Type = Counter32
_IkeTunnelInP2Proposals_Object = MibTableColumn
ikeTunnelInP2Proposals = _IkeTunnelInP2Proposals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 16),
    _IkeTunnelInP2Proposals_Type()
)
ikeTunnelInP2Proposals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInP2Proposals.setStatus("mandatory")
_IkeTunnelInP2ProposalInvalids_Type = Counter32
_IkeTunnelInP2ProposalInvalids_Object = MibTableColumn
ikeTunnelInP2ProposalInvalids = _IkeTunnelInP2ProposalInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 17),
    _IkeTunnelInP2ProposalInvalids_Type()
)
ikeTunnelInP2ProposalInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInP2ProposalInvalids.setStatus("mandatory")
_IkeTunnelInP2ProposalRejects_Type = Counter32
_IkeTunnelInP2ProposalRejects_Object = MibTableColumn
ikeTunnelInP2ProposalRejects = _IkeTunnelInP2ProposalRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 18),
    _IkeTunnelInP2ProposalRejects_Type()
)
ikeTunnelInP2ProposalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInP2ProposalRejects.setStatus("mandatory")
_IkeTunnelInSaDeleteRequests_Type = Counter32
_IkeTunnelInSaDeleteRequests_Object = MibTableColumn
ikeTunnelInSaDeleteRequests = _IkeTunnelInSaDeleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 19),
    _IkeTunnelInSaDeleteRequests_Type()
)
ikeTunnelInSaDeleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelInSaDeleteRequests.setStatus("mandatory")
_IkeTunnelOutOctets_Type = Counter32
_IkeTunnelOutOctets_Object = MibTableColumn
ikeTunnelOutOctets = _IkeTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 20),
    _IkeTunnelOutOctets_Type()
)
ikeTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutOctets.setStatus("mandatory")
_IkeTunnelOutPkts_Type = Counter32
_IkeTunnelOutPkts_Object = MibTableColumn
ikeTunnelOutPkts = _IkeTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 21),
    _IkeTunnelOutPkts_Type()
)
ikeTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutPkts.setStatus("mandatory")
_IkeTunnelOutDropPkts_Type = Counter32
_IkeTunnelOutDropPkts_Object = MibTableColumn
ikeTunnelOutDropPkts = _IkeTunnelOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 22),
    _IkeTunnelOutDropPkts_Type()
)
ikeTunnelOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutDropPkts.setStatus("mandatory")
_IkeTunnelOutNotifys_Type = Counter32
_IkeTunnelOutNotifys_Object = MibTableColumn
ikeTunnelOutNotifys = _IkeTunnelOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 23),
    _IkeTunnelOutNotifys_Type()
)
ikeTunnelOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutNotifys.setStatus("mandatory")
_IkeTunnelOutP2Proposals_Type = Counter32
_IkeTunnelOutP2Proposals_Object = MibTableColumn
ikeTunnelOutP2Proposals = _IkeTunnelOutP2Proposals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 24),
    _IkeTunnelOutP2Proposals_Type()
)
ikeTunnelOutP2Proposals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutP2Proposals.setStatus("mandatory")
_IkeTunnelOutP2ProposalRejects_Type = Counter32
_IkeTunnelOutP2ProposalRejects_Object = MibTableColumn
ikeTunnelOutP2ProposalRejects = _IkeTunnelOutP2ProposalRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 25),
    _IkeTunnelOutP2ProposalRejects_Type()
)
ikeTunnelOutP2ProposalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutP2ProposalRejects.setStatus("mandatory")
_IkeTunnelOutSaDeleteRequests_Type = Counter32
_IkeTunnelOutSaDeleteRequests_Object = MibTableColumn
ikeTunnelOutSaDeleteRequests = _IkeTunnelOutSaDeleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 26),
    _IkeTunnelOutSaDeleteRequests_Type()
)
ikeTunnelOutSaDeleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeTunnelOutSaDeleteRequests.setStatus("mandatory")


class _IkeTunnelStatus_Type(Integer32):
    """Custom type ikeTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_IkeTunnelStatus_Type.__name__ = "Integer32"
_IkeTunnelStatus_Object = MibTableColumn
ikeTunnelStatus = _IkeTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 2, 1, 1, 27),
    _IkeTunnelStatus_Type()
)
ikeTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikeTunnelStatus.setStatus("mandatory")
_IpSecPhaseTwo_ObjectIdentity = ObjectIdentity
ipSecPhaseTwo = _IpSecPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3)
)
_IpSecGlobal_ObjectIdentity = ObjectIdentity
ipSecGlobal = _IpSecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1)
)
_IpSecGlobalActiveTunnels_Type = Counter32
_IpSecGlobalActiveTunnels_Object = MibScalar
ipSecGlobalActiveTunnels = _IpSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 1),
    _IpSecGlobalActiveTunnels_Type()
)
ipSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalActiveTunnels.setStatus("mandatory")
_IpSecGlobalPreviousTunnels_Type = Counter32
_IpSecGlobalPreviousTunnels_Object = MibScalar
ipSecGlobalPreviousTunnels = _IpSecGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 2),
    _IpSecGlobalPreviousTunnels_Type()
)
ipSecGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalPreviousTunnels.setStatus("mandatory")
_IpSecGlobalInOctets_Type = Counter32
_IpSecGlobalInOctets_Object = MibScalar
ipSecGlobalInOctets = _IpSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 3),
    _IpSecGlobalInOctets_Type()
)
ipSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInOctets.setStatus("mandatory")
_IpSecGlobalInPkts_Type = Counter32
_IpSecGlobalInPkts_Object = MibScalar
ipSecGlobalInPkts = _IpSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 4),
    _IpSecGlobalInPkts_Type()
)
ipSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInPkts.setStatus("mandatory")
_IpSecGlobalInDrops_Type = Counter32
_IpSecGlobalInDrops_Object = MibScalar
ipSecGlobalInDrops = _IpSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 5),
    _IpSecGlobalInDrops_Type()
)
ipSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInDrops.setStatus("mandatory")
_IpSecGlobalInAuths_Type = Counter32
_IpSecGlobalInAuths_Object = MibScalar
ipSecGlobalInAuths = _IpSecGlobalInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 6),
    _IpSecGlobalInAuths_Type()
)
ipSecGlobalInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInAuths.setStatus("mandatory")
_IpSecGlobalInAuthFails_Type = Counter32
_IpSecGlobalInAuthFails_Object = MibScalar
ipSecGlobalInAuthFails = _IpSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 7),
    _IpSecGlobalInAuthFails_Type()
)
ipSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInAuthFails.setStatus("mandatory")
_IpSecGlobalInDecrypts_Type = Counter32
_IpSecGlobalInDecrypts_Object = MibScalar
ipSecGlobalInDecrypts = _IpSecGlobalInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 8),
    _IpSecGlobalInDecrypts_Type()
)
ipSecGlobalInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInDecrypts.setStatus("mandatory")
_IpSecGlobalInDecryptFails_Type = Counter32
_IpSecGlobalInDecryptFails_Object = MibScalar
ipSecGlobalInDecryptFails = _IpSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 9),
    _IpSecGlobalInDecryptFails_Type()
)
ipSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInDecryptFails.setStatus("mandatory")
_IpSecGlobalOutOctets_Type = Counter32
_IpSecGlobalOutOctets_Object = MibScalar
ipSecGlobalOutOctets = _IpSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 10),
    _IpSecGlobalOutOctets_Type()
)
ipSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutOctets.setStatus("mandatory")
_IpSecGlobalOutPkts_Type = Counter32
_IpSecGlobalOutPkts_Object = MibScalar
ipSecGlobalOutPkts = _IpSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 11),
    _IpSecGlobalOutPkts_Type()
)
ipSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutPkts.setStatus("mandatory")
_IpSecGlobalOutDrops_Type = Counter32
_IpSecGlobalOutDrops_Object = MibScalar
ipSecGlobalOutDrops = _IpSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 12),
    _IpSecGlobalOutDrops_Type()
)
ipSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutDrops.setStatus("mandatory")
_IpSecGlobalOutAuths_Type = Counter32
_IpSecGlobalOutAuths_Object = MibScalar
ipSecGlobalOutAuths = _IpSecGlobalOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 13),
    _IpSecGlobalOutAuths_Type()
)
ipSecGlobalOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutAuths.setStatus("mandatory")
_IpSecGlobalOutAuthFails_Type = Counter32
_IpSecGlobalOutAuthFails_Object = MibScalar
ipSecGlobalOutAuthFails = _IpSecGlobalOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 14),
    _IpSecGlobalOutAuthFails_Type()
)
ipSecGlobalOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutAuthFails.setStatus("mandatory")
_IpSecGlobalOutEncrypts_Type = Counter32
_IpSecGlobalOutEncrypts_Object = MibScalar
ipSecGlobalOutEncrypts = _IpSecGlobalOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 15),
    _IpSecGlobalOutEncrypts_Type()
)
ipSecGlobalOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutEncrypts.setStatus("mandatory")
_IpSecGlobalOutEncryptFails_Type = Counter32
_IpSecGlobalOutEncryptFails_Object = MibScalar
ipSecGlobalOutEncryptFails = _IpSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 16),
    _IpSecGlobalOutEncryptFails_Type()
)
ipSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutEncryptFails.setStatus("mandatory")
_IpSecGlobalInOctWraps_Type = Counter32
_IpSecGlobalInOctWraps_Object = MibScalar
ipSecGlobalInOctWraps = _IpSecGlobalInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 17),
    _IpSecGlobalInOctWraps_Type()
)
ipSecGlobalInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalInOctWraps.setStatus("mandatory")
_IpSecGlobalOutOctWraps_Type = Counter32
_IpSecGlobalOutOctWraps_Object = MibScalar
ipSecGlobalOutOctWraps = _IpSecGlobalOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 1, 18),
    _IpSecGlobalOutOctWraps_Type()
)
ipSecGlobalOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecGlobalOutOctWraps.setStatus("mandatory")
_IpSecTunnelTable_Object = MibTable
ipSecTunnelTable = _IpSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2)
)
if mibBuilder.loadTexts:
    ipSecTunnelTable.setStatus("mandatory")
_IpSecTunnelEntry_Object = MibTableRow
ipSecTunnelEntry = _IpSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1)
)
ipSecTunnelEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ipSecTunnelIndex"),
)
if mibBuilder.loadTexts:
    ipSecTunnelEntry.setStatus("mandatory")


class _IpSecTunnelIndex_Type(Integer32):
    """Custom type ipSecTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSecTunnelIndex_Type.__name__ = "Integer32"
_IpSecTunnelIndex_Object = MibTableColumn
ipSecTunnelIndex = _IpSecTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 1),
    _IpSecTunnelIndex_Type()
)
ipSecTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelIndex.setStatus("mandatory")


class _IpSecTunnelId_Type(Integer32):
    """Custom type ipSecTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSecTunnelId_Type.__name__ = "Integer32"
_IpSecTunnelId_Object = MibTableColumn
ipSecTunnelId = _IpSecTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 2),
    _IpSecTunnelId_Type()
)
ipSecTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelId.setStatus("mandatory")
_IpSecTunnelIkeTunnelIndex_Type = Integer32
_IpSecTunnelIkeTunnelIndex_Object = MibTableColumn
ipSecTunnelIkeTunnelIndex = _IpSecTunnelIkeTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 3),
    _IpSecTunnelIkeTunnelIndex_Type()
)
ipSecTunnelIkeTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelIkeTunnelIndex.setStatus("mandatory")
_IpSecTunnelLocalAddr_Type = IPSIpAddress
_IpSecTunnelLocalAddr_Object = MibTableColumn
ipSecTunnelLocalAddr = _IpSecTunnelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 4),
    _IpSecTunnelLocalAddr_Type()
)
ipSecTunnelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelLocalAddr.setStatus("mandatory")
_IpSecTunnelRemoteAddr_Type = IPSIpAddress
_IpSecTunnelRemoteAddr_Object = MibTableColumn
ipSecTunnelRemoteAddr = _IpSecTunnelRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 5),
    _IpSecTunnelRemoteAddr_Type()
)
ipSecTunnelRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelRemoteAddr.setStatus("mandatory")


class _IpSecTunnelKeyType_Type(Integer32):
    """Custom type ipSecTunnelKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2))
    )


_IpSecTunnelKeyType_Type.__name__ = "Integer32"
_IpSecTunnelKeyType_Object = MibTableColumn
ipSecTunnelKeyType = _IpSecTunnelKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 6),
    _IpSecTunnelKeyType_Type()
)
ipSecTunnelKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelKeyType.setStatus("mandatory")


class _IpSecTunnelEncapMode_Type(Integer32):
    """Custom type ipSecTunnelEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_IpSecTunnelEncapMode_Type.__name__ = "Integer32"
_IpSecTunnelEncapMode_Object = MibTableColumn
ipSecTunnelEncapMode = _IpSecTunnelEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 7),
    _IpSecTunnelEncapMode_Type()
)
ipSecTunnelEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelEncapMode.setStatus("mandatory")
_IpSecTunnelLifetime_Type = TimeTicks
_IpSecTunnelLifetime_Object = MibTableColumn
ipSecTunnelLifetime = _IpSecTunnelLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 8),
    _IpSecTunnelLifetime_Type()
)
ipSecTunnelLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelLifetime.setStatus("mandatory")
_IpSecTunnelActiveTime_Type = TimeTicks
_IpSecTunnelActiveTime_Object = MibTableColumn
ipSecTunnelActiveTime = _IpSecTunnelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 9),
    _IpSecTunnelActiveTime_Type()
)
ipSecTunnelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelActiveTime.setStatus("mandatory")


class _IpSecTunnelSaRefreshThreshold_Type(Integer32):
    """Custom type ipSecTunnelSaRefreshThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpSecTunnelSaRefreshThreshold_Type.__name__ = "Integer32"
_IpSecTunnelSaRefreshThreshold_Object = MibTableColumn
ipSecTunnelSaRefreshThreshold = _IpSecTunnelSaRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 10),
    _IpSecTunnelSaRefreshThreshold_Type()
)
ipSecTunnelSaRefreshThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelSaRefreshThreshold.setStatus("mandatory")
_IpSecTunnelTotalRefreshes_Type = Counter32
_IpSecTunnelTotalRefreshes_Object = MibTableColumn
ipSecTunnelTotalRefreshes = _IpSecTunnelTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 11),
    _IpSecTunnelTotalRefreshes_Type()
)
ipSecTunnelTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelTotalRefreshes.setStatus("mandatory")
_IpSecTunnelExpiredSaInstances_Type = Counter32
_IpSecTunnelExpiredSaInstances_Object = MibTableColumn
ipSecTunnelExpiredSaInstances = _IpSecTunnelExpiredSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 12),
    _IpSecTunnelExpiredSaInstances_Type()
)
ipSecTunnelExpiredSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelExpiredSaInstances.setStatus("mandatory")
_IpSecTunnelCurrentSaInstances_Type = Gauge32
_IpSecTunnelCurrentSaInstances_Object = MibTableColumn
ipSecTunnelCurrentSaInstances = _IpSecTunnelCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 13),
    _IpSecTunnelCurrentSaInstances_Type()
)
ipSecTunnelCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelCurrentSaInstances.setStatus("mandatory")


class _IpSecTunnelInSaEncrypt_Type(Integer32):
    """Custom type ipSecTunnelInSaEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("esp3Des", 4),
          ("esp3iDes", 9),
          ("espBlowfish", 8),
          ("espCast", 7),
          ("espCdmf", 12),
          ("espDes", 3),
          ("espDesIv32", 10),
          ("espDesIv64", 2),
          ("espIdea", 6),
          ("espNone", 1),
          ("espRc4", 11),
          ("espRc5", 5))
    )


_IpSecTunnelInSaEncrypt_Type.__name__ = "Integer32"
_IpSecTunnelInSaEncrypt_Object = MibTableColumn
ipSecTunnelInSaEncrypt = _IpSecTunnelInSaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 14),
    _IpSecTunnelInSaEncrypt_Type()
)
ipSecTunnelInSaEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInSaEncrypt.setStatus("mandatory")


class _IpSecTunnelInSaAuthAlgo_Type(Integer32):
    """Custom type ipSecTunnelInSaAuthAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("desMac", 4),
          ("hmacMd5", 2),
          ("hmacSha", 3),
          ("kpdk", 5),
          ("none", 1))
    )


_IpSecTunnelInSaAuthAlgo_Type.__name__ = "Integer32"
_IpSecTunnelInSaAuthAlgo_Object = MibTableColumn
ipSecTunnelInSaAuthAlgo = _IpSecTunnelInSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 15),
    _IpSecTunnelInSaAuthAlgo_Type()
)
ipSecTunnelInSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInSaAuthAlgo.setStatus("mandatory")


class _IpSecTunnelOutSaEncrypt_Type(Integer32):
    """Custom type ipSecTunnelOutSaEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("esp3Des", 4),
          ("esp3iDes", 9),
          ("espBlowfish", 8),
          ("espCast", 7),
          ("espCdmf", 12),
          ("espDes", 3),
          ("espDesIv32", 10),
          ("espDesIv64", 2),
          ("espIdea", 6),
          ("espNone", 1),
          ("espRc4", 11),
          ("espRc5", 5))
    )


_IpSecTunnelOutSaEncrypt_Type.__name__ = "Integer32"
_IpSecTunnelOutSaEncrypt_Object = MibTableColumn
ipSecTunnelOutSaEncrypt = _IpSecTunnelOutSaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 16),
    _IpSecTunnelOutSaEncrypt_Type()
)
ipSecTunnelOutSaEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutSaEncrypt.setStatus("mandatory")


class _IpSecTunnelOutSaAuthAlgo_Type(Integer32):
    """Custom type ipSecTunnelOutSaAuthAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("desMac", 4),
          ("hmacMd5", 2),
          ("hmacSha", 3),
          ("kpdk", 5),
          ("none", 1))
    )


_IpSecTunnelOutSaAuthAlgo_Type.__name__ = "Integer32"
_IpSecTunnelOutSaAuthAlgo_Object = MibTableColumn
ipSecTunnelOutSaAuthAlgo = _IpSecTunnelOutSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 17),
    _IpSecTunnelOutSaAuthAlgo_Type()
)
ipSecTunnelOutSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutSaAuthAlgo.setStatus("mandatory")
_IpSecTunnelInOctets_Type = Counter32
_IpSecTunnelInOctets_Object = MibTableColumn
ipSecTunnelInOctets = _IpSecTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 18),
    _IpSecTunnelInOctets_Type()
)
ipSecTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInOctets.setStatus("mandatory")
_IpSecTunnelInDecompOctets_Type = Counter32
_IpSecTunnelInDecompOctets_Object = MibTableColumn
ipSecTunnelInDecompOctets = _IpSecTunnelInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 19),
    _IpSecTunnelInDecompOctets_Type()
)
ipSecTunnelInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInDecompOctets.setStatus("mandatory")
_IpSecTunnelInPkts_Type = Counter32
_IpSecTunnelInPkts_Object = MibTableColumn
ipSecTunnelInPkts = _IpSecTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 20),
    _IpSecTunnelInPkts_Type()
)
ipSecTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInPkts.setStatus("mandatory")
_IpSecTunnelInDropPkts_Type = Counter32
_IpSecTunnelInDropPkts_Object = MibTableColumn
ipSecTunnelInDropPkts = _IpSecTunnelInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 21),
    _IpSecTunnelInDropPkts_Type()
)
ipSecTunnelInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInDropPkts.setStatus("mandatory")
_IpSecTunnelInAuths_Type = Counter32
_IpSecTunnelInAuths_Object = MibTableColumn
ipSecTunnelInAuths = _IpSecTunnelInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 22),
    _IpSecTunnelInAuths_Type()
)
ipSecTunnelInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInAuths.setStatus("mandatory")
_IpSecTunnelInAuthFails_Type = Counter32
_IpSecTunnelInAuthFails_Object = MibTableColumn
ipSecTunnelInAuthFails = _IpSecTunnelInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 23),
    _IpSecTunnelInAuthFails_Type()
)
ipSecTunnelInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInAuthFails.setStatus("mandatory")
_IpSecTunnelInDecrypts_Type = Counter32
_IpSecTunnelInDecrypts_Object = MibTableColumn
ipSecTunnelInDecrypts = _IpSecTunnelInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 24),
    _IpSecTunnelInDecrypts_Type()
)
ipSecTunnelInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInDecrypts.setStatus("mandatory")
_IpSecTunnelInDecryptFails_Type = Counter32
_IpSecTunnelInDecryptFails_Object = MibTableColumn
ipSecTunnelInDecryptFails = _IpSecTunnelInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 25),
    _IpSecTunnelInDecryptFails_Type()
)
ipSecTunnelInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInDecryptFails.setStatus("mandatory")
_IpSecTunnelOutOctets_Type = Counter32
_IpSecTunnelOutOctets_Object = MibTableColumn
ipSecTunnelOutOctets = _IpSecTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 26),
    _IpSecTunnelOutOctets_Type()
)
ipSecTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutOctets.setStatus("mandatory")
_IpSecTunnelOutUncompOctets_Type = Counter32
_IpSecTunnelOutUncompOctets_Object = MibTableColumn
ipSecTunnelOutUncompOctets = _IpSecTunnelOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 27),
    _IpSecTunnelOutUncompOctets_Type()
)
ipSecTunnelOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutUncompOctets.setStatus("mandatory")
_IpSecTunnelOutPkts_Type = Counter32
_IpSecTunnelOutPkts_Object = MibTableColumn
ipSecTunnelOutPkts = _IpSecTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 28),
    _IpSecTunnelOutPkts_Type()
)
ipSecTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutPkts.setStatus("mandatory")
_IpSecTunnelOutDropPkts_Type = Counter32
_IpSecTunnelOutDropPkts_Object = MibTableColumn
ipSecTunnelOutDropPkts = _IpSecTunnelOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 29),
    _IpSecTunnelOutDropPkts_Type()
)
ipSecTunnelOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutDropPkts.setStatus("mandatory")
_IpSecTunnelOutAuths_Type = Counter32
_IpSecTunnelOutAuths_Object = MibTableColumn
ipSecTunnelOutAuths = _IpSecTunnelOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 30),
    _IpSecTunnelOutAuths_Type()
)
ipSecTunnelOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutAuths.setStatus("mandatory")
_IpSecTunnelOutAuthFails_Type = Counter32
_IpSecTunnelOutAuthFails_Object = MibTableColumn
ipSecTunnelOutAuthFails = _IpSecTunnelOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 31),
    _IpSecTunnelOutAuthFails_Type()
)
ipSecTunnelOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutAuthFails.setStatus("mandatory")
_IpSecTunnelOutEncrypts_Type = Counter32
_IpSecTunnelOutEncrypts_Object = MibTableColumn
ipSecTunnelOutEncrypts = _IpSecTunnelOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 32),
    _IpSecTunnelOutEncrypts_Type()
)
ipSecTunnelOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutEncrypts.setStatus("mandatory")
_IpSecTunnelOutEncryptFails_Type = Counter32
_IpSecTunnelOutEncryptFails_Object = MibTableColumn
ipSecTunnelOutEncryptFails = _IpSecTunnelOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 33),
    _IpSecTunnelOutEncryptFails_Type()
)
ipSecTunnelOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutEncryptFails.setStatus("mandatory")


class _IpSecTunnelStatus_Type(Integer32):
    """Custom type ipSecTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2),
          ("disabled", 3))
    )


_IpSecTunnelStatus_Type.__name__ = "Integer32"
_IpSecTunnelStatus_Object = MibTableColumn
ipSecTunnelStatus = _IpSecTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 34),
    _IpSecTunnelStatus_Type()
)
ipSecTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTunnelStatus.setStatus("mandatory")
_IpSecTunnelInOctWraps_Type = Counter32
_IpSecTunnelInOctWraps_Object = MibTableColumn
ipSecTunnelInOctWraps = _IpSecTunnelInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 35),
    _IpSecTunnelInOctWraps_Type()
)
ipSecTunnelInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInOctWraps.setStatus("mandatory")
_IpSecTunnelInDecompOctWraps_Type = Counter32
_IpSecTunnelInDecompOctWraps_Object = MibTableColumn
ipSecTunnelInDecompOctWraps = _IpSecTunnelInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 36),
    _IpSecTunnelInDecompOctWraps_Type()
)
ipSecTunnelInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelInDecompOctWraps.setStatus("mandatory")
_IpSecTunnelOutOctWraps_Type = Counter32
_IpSecTunnelOutOctWraps_Object = MibTableColumn
ipSecTunnelOutOctWraps = _IpSecTunnelOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 37),
    _IpSecTunnelOutOctWraps_Type()
)
ipSecTunnelOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutOctWraps.setStatus("mandatory")
_IpSecTunnelOutUncompOctWraps_Type = Counter32
_IpSecTunnelOutUncompOctWraps_Object = MibTableColumn
ipSecTunnelOutUncompOctWraps = _IpSecTunnelOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 2, 1, 38),
    _IpSecTunnelOutUncompOctWraps_Type()
)
ipSecTunnelOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelOutUncompOctWraps.setStatus("mandatory")
_IpSecClientTable_Object = MibTable
ipSecClientTable = _IpSecClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3)
)
if mibBuilder.loadTexts:
    ipSecClientTable.setStatus("mandatory")
_IpSecClientEntry_Object = MibTableRow
ipSecClientEntry = _IpSecClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1)
)
ipSecClientEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ipSecTunnelIndex"),
    (0, "IPSECV1-MIB", "ipSecClientIndex"),
)
if mibBuilder.loadTexts:
    ipSecClientEntry.setStatus("mandatory")


class _IpSecClientIndex_Type(Integer32):
    """Custom type ipSecClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSecClientIndex_Type.__name__ = "Integer32"
_IpSecClientIndex_Object = MibTableColumn
ipSecClientIndex = _IpSecClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 1),
    _IpSecClientIndex_Type()
)
ipSecClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientIndex.setStatus("mandatory")
_IpSecClientLocalName_Type = DisplayString
_IpSecClientLocalName_Object = MibTableColumn
ipSecClientLocalName = _IpSecClientLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 2),
    _IpSecClientLocalName_Type()
)
ipSecClientLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalName.setStatus("mandatory")


class _IpSecClientLocalType_Type(Integer32):
    """Custom type ipSecClientLocalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddrRangeEntry", 1),
          ("ipSubnetMaskEntry", 2))
    )


_IpSecClientLocalType_Type.__name__ = "Integer32"
_IpSecClientLocalType_Object = MibTableColumn
ipSecClientLocalType = _IpSecClientLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 3),
    _IpSecClientLocalType_Type()
)
ipSecClientLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalType.setStatus("mandatory")


class _IpSecClientLocalProtocol_Type(Integer32):
    """Custom type ipSecClientLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpSecClientLocalProtocol_Type.__name__ = "Integer32"
_IpSecClientLocalProtocol_Object = MibTableColumn
ipSecClientLocalProtocol = _IpSecClientLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 4),
    _IpSecClientLocalProtocol_Type()
)
ipSecClientLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalProtocol.setStatus("mandatory")
_IpSecClientLocalSubnetMask_Type = IPSIpAddress
_IpSecClientLocalSubnetMask_Object = MibTableColumn
ipSecClientLocalSubnetMask = _IpSecClientLocalSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 5),
    _IpSecClientLocalSubnetMask_Type()
)
ipSecClientLocalSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalSubnetMask.setStatus("mandatory")
_IpSecClientLocalHiAddr_Type = IPSIpAddress
_IpSecClientLocalHiAddr_Object = MibTableColumn
ipSecClientLocalHiAddr = _IpSecClientLocalHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 6),
    _IpSecClientLocalHiAddr_Type()
)
ipSecClientLocalHiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalHiAddr.setStatus("mandatory")
_IpSecClientLocalLoAddr_Type = IPSIpAddress
_IpSecClientLocalLoAddr_Object = MibTableColumn
ipSecClientLocalLoAddr = _IpSecClientLocalLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 7),
    _IpSecClientLocalLoAddr_Type()
)
ipSecClientLocalLoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalLoAddr.setStatus("mandatory")
_IpSecClientLocalPort_Type = Integer32
_IpSecClientLocalPort_Object = MibTableColumn
ipSecClientLocalPort = _IpSecClientLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 8),
    _IpSecClientLocalPort_Type()
)
ipSecClientLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientLocalPort.setStatus("mandatory")
_IpSecClientRemoteName_Type = DisplayString
_IpSecClientRemoteName_Object = MibTableColumn
ipSecClientRemoteName = _IpSecClientRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 9),
    _IpSecClientRemoteName_Type()
)
ipSecClientRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteName.setStatus("mandatory")


class _IpSecClientRemoteType_Type(Integer32):
    """Custom type ipSecClientRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddrRangeEntry", 1),
          ("ipSubnetMaskEntry", 2))
    )


_IpSecClientRemoteType_Type.__name__ = "Integer32"
_IpSecClientRemoteType_Object = MibTableColumn
ipSecClientRemoteType = _IpSecClientRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 10),
    _IpSecClientRemoteType_Type()
)
ipSecClientRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteType.setStatus("mandatory")


class _IpSecClientRemoteProtocol_Type(Integer32):
    """Custom type ipSecClientRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpSecClientRemoteProtocol_Type.__name__ = "Integer32"
_IpSecClientRemoteProtocol_Object = MibTableColumn
ipSecClientRemoteProtocol = _IpSecClientRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 11),
    _IpSecClientRemoteProtocol_Type()
)
ipSecClientRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteProtocol.setStatus("mandatory")
_IpSecClientRemoteSubnetMask_Type = IPSIpAddress
_IpSecClientRemoteSubnetMask_Object = MibTableColumn
ipSecClientRemoteSubnetMask = _IpSecClientRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 12),
    _IpSecClientRemoteSubnetMask_Type()
)
ipSecClientRemoteSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteSubnetMask.setStatus("mandatory")
_IpSecClientRemoteHiAddr_Type = IPSIpAddress
_IpSecClientRemoteHiAddr_Object = MibTableColumn
ipSecClientRemoteHiAddr = _IpSecClientRemoteHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 13),
    _IpSecClientRemoteHiAddr_Type()
)
ipSecClientRemoteHiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteHiAddr.setStatus("mandatory")
_IpSecClientRemoteLoAddr_Type = IPSIpAddress
_IpSecClientRemoteLoAddr_Object = MibTableColumn
ipSecClientRemoteLoAddr = _IpSecClientRemoteLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 14),
    _IpSecClientRemoteLoAddr_Type()
)
ipSecClientRemoteLoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemoteLoAddr.setStatus("mandatory")
_IpSecClientRemotePort_Type = Integer32
_IpSecClientRemotePort_Object = MibTableColumn
ipSecClientRemotePort = _IpSecClientRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 3, 1, 15),
    _IpSecClientRemotePort_Type()
)
ipSecClientRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecClientRemotePort.setStatus("mandatory")
_IpSecSpiTable_Object = MibTable
ipSecSpiTable = _IpSecSpiTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4)
)
if mibBuilder.loadTexts:
    ipSecSpiTable.setStatus("mandatory")
_IpSecSpiEntry_Object = MibTableRow
ipSecSpiEntry = _IpSecSpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1)
)
ipSecSpiEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ipSecTunnelIndex"),
    (0, "IPSECV1-MIB", "ipSecSpiIndex"),
)
if mibBuilder.loadTexts:
    ipSecSpiEntry.setStatus("mandatory")


class _IpSecSpiIndex_Type(Integer32):
    """Custom type ipSecSpiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSecSpiIndex_Type.__name__ = "Integer32"
_IpSecSpiIndex_Object = MibTableColumn
ipSecSpiIndex = _IpSecSpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1, 1),
    _IpSecSpiIndex_Type()
)
ipSecSpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecSpiIndex.setStatus("mandatory")


class _IpSecSpiDirection_Type(Integer32):
    """Custom type ipSecSpiDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_IpSecSpiDirection_Type.__name__ = "Integer32"
_IpSecSpiDirection_Object = MibTableColumn
ipSecSpiDirection = _IpSecSpiDirection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1, 2),
    _IpSecSpiDirection_Type()
)
ipSecSpiDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecSpiDirection.setStatus("mandatory")
_IpSecSpiValue_Type = Integer32
_IpSecSpiValue_Object = MibTableColumn
ipSecSpiValue = _IpSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1, 3),
    _IpSecSpiValue_Type()
)
ipSecSpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecSpiValue.setStatus("mandatory")


class _IpSecSpiProtocol_Type(Integer32):
    """Custom type ipSecSpiProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2),
          ("ipcomp", 3))
    )


_IpSecSpiProtocol_Type.__name__ = "Integer32"
_IpSecSpiProtocol_Object = MibTableColumn
ipSecSpiProtocol = _IpSecSpiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1, 4),
    _IpSecSpiProtocol_Type()
)
ipSecSpiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecSpiProtocol.setStatus("mandatory")


class _IpSecSpiStatus_Type(Integer32):
    """Custom type ipSecSpiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expiring", 2))
    )


_IpSecSpiStatus_Type.__name__ = "Integer32"
_IpSecSpiStatus_Object = MibTableColumn
ipSecSpiStatus = _IpSecSpiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 3, 4, 1, 5),
    _IpSecSpiStatus_Type()
)
ipSecSpiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecSpiStatus.setStatus("mandatory")
_IpSecHistory_ObjectIdentity = ObjectIdentity
ipSecHistory = _IpSecHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4)
)
_IpSecTunnelHistTable_Object = MibTable
ipSecTunnelHistTable = _IpSecTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2)
)
if mibBuilder.loadTexts:
    ipSecTunnelHistTable.setStatus("mandatory")
_IpSecTunnelHistEntry_Object = MibTableRow
ipSecTunnelHistEntry = _IpSecTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1)
)
ipSecTunnelHistEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ipSecTunnelHistIndex"),
)
if mibBuilder.loadTexts:
    ipSecTunnelHistEntry.setStatus("mandatory")


class _IpSecTunnelHistIndex_Type(Integer32):
    """Custom type ipSecTunnelHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSecTunnelHistIndex_Type.__name__ = "Integer32"
_IpSecTunnelHistIndex_Object = MibTableColumn
ipSecTunnelHistIndex = _IpSecTunnelHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 1),
    _IpSecTunnelHistIndex_Type()
)
ipSecTunnelHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistIndex.setStatus("mandatory")


class _IpSecTunnelHistId_Type(Integer32):
    """Custom type ipSecTunnelHistId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSecTunnelHistId_Type.__name__ = "Integer32"
_IpSecTunnelHistId_Object = MibTableColumn
ipSecTunnelHistId = _IpSecTunnelHistId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 2),
    _IpSecTunnelHistId_Type()
)
ipSecTunnelHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistId.setStatus("mandatory")
_IpSecTunnelHistLocalAddr_Type = IPSIpAddress
_IpSecTunnelHistLocalAddr_Object = MibTableColumn
ipSecTunnelHistLocalAddr = _IpSecTunnelHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 3),
    _IpSecTunnelHistLocalAddr_Type()
)
ipSecTunnelHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistLocalAddr.setStatus("mandatory")
_IpSecTunnelHistRemoteAddr_Type = IPSIpAddress
_IpSecTunnelHistRemoteAddr_Object = MibTableColumn
ipSecTunnelHistRemoteAddr = _IpSecTunnelHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 4),
    _IpSecTunnelHistRemoteAddr_Type()
)
ipSecTunnelHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistRemoteAddr.setStatus("mandatory")
_IpSecTunnelHistActiveTime_Type = TimeTicks
_IpSecTunnelHistActiveTime_Object = MibTableColumn
ipSecTunnelHistActiveTime = _IpSecTunnelHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 5),
    _IpSecTunnelHistActiveTime_Type()
)
ipSecTunnelHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistActiveTime.setStatus("mandatory")
_IpSecTunnelHistTotalRefreshes_Type = Counter32
_IpSecTunnelHistTotalRefreshes_Object = MibTableColumn
ipSecTunnelHistTotalRefreshes = _IpSecTunnelHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 6),
    _IpSecTunnelHistTotalRefreshes_Type()
)
ipSecTunnelHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistTotalRefreshes.setStatus("mandatory")
_IpSecTunnelHistTotalSas_Type = Counter32
_IpSecTunnelHistTotalSas_Object = MibTableColumn
ipSecTunnelHistTotalSas = _IpSecTunnelHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 7),
    _IpSecTunnelHistTotalSas_Type()
)
ipSecTunnelHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistTotalSas.setStatus("mandatory")
_IpSecTunnelHistInOctets_Type = Counter32
_IpSecTunnelHistInOctets_Object = MibTableColumn
ipSecTunnelHistInOctets = _IpSecTunnelHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 8),
    _IpSecTunnelHistInOctets_Type()
)
ipSecTunnelHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInOctets.setStatus("mandatory")
_IpSecTunnelHistInDecompOctets_Type = Counter32
_IpSecTunnelHistInDecompOctets_Object = MibTableColumn
ipSecTunnelHistInDecompOctets = _IpSecTunnelHistInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 9),
    _IpSecTunnelHistInDecompOctets_Type()
)
ipSecTunnelHistInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInDecompOctets.setStatus("mandatory")
_IpSecTunnelHistInPkts_Type = Counter32
_IpSecTunnelHistInPkts_Object = MibTableColumn
ipSecTunnelHistInPkts = _IpSecTunnelHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 10),
    _IpSecTunnelHistInPkts_Type()
)
ipSecTunnelHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInPkts.setStatus("mandatory")
_IpSecTunnelHistInDropPkts_Type = Counter32
_IpSecTunnelHistInDropPkts_Object = MibTableColumn
ipSecTunnelHistInDropPkts = _IpSecTunnelHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 11),
    _IpSecTunnelHistInDropPkts_Type()
)
ipSecTunnelHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInDropPkts.setStatus("mandatory")
_IpSecTunnelHistInAuths_Type = Counter32
_IpSecTunnelHistInAuths_Object = MibTableColumn
ipSecTunnelHistInAuths = _IpSecTunnelHistInAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 12),
    _IpSecTunnelHistInAuths_Type()
)
ipSecTunnelHistInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInAuths.setStatus("mandatory")
_IpSecTunnelHistInAuthFails_Type = Counter32
_IpSecTunnelHistInAuthFails_Object = MibTableColumn
ipSecTunnelHistInAuthFails = _IpSecTunnelHistInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 13),
    _IpSecTunnelHistInAuthFails_Type()
)
ipSecTunnelHistInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInAuthFails.setStatus("mandatory")
_IpSecTunnelHistInDecrypts_Type = Counter32
_IpSecTunnelHistInDecrypts_Object = MibTableColumn
ipSecTunnelHistInDecrypts = _IpSecTunnelHistInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 14),
    _IpSecTunnelHistInDecrypts_Type()
)
ipSecTunnelHistInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInDecrypts.setStatus("mandatory")
_IpSecTunnelHistInDecryptFails_Type = Counter32
_IpSecTunnelHistInDecryptFails_Object = MibTableColumn
ipSecTunnelHistInDecryptFails = _IpSecTunnelHistInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 15),
    _IpSecTunnelHistInDecryptFails_Type()
)
ipSecTunnelHistInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInDecryptFails.setStatus("mandatory")
_IpSecTunnelHistOutOctets_Type = Counter32
_IpSecTunnelHistOutOctets_Object = MibTableColumn
ipSecTunnelHistOutOctets = _IpSecTunnelHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 16),
    _IpSecTunnelHistOutOctets_Type()
)
ipSecTunnelHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutOctets.setStatus("mandatory")
_IpSecTunnelHistOutUncompOctets_Type = Counter32
_IpSecTunnelHistOutUncompOctets_Object = MibTableColumn
ipSecTunnelHistOutUncompOctets = _IpSecTunnelHistOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 17),
    _IpSecTunnelHistOutUncompOctets_Type()
)
ipSecTunnelHistOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutUncompOctets.setStatus("mandatory")
_IpSecTunnelHistOutPkts_Type = Counter32
_IpSecTunnelHistOutPkts_Object = MibTableColumn
ipSecTunnelHistOutPkts = _IpSecTunnelHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 18),
    _IpSecTunnelHistOutPkts_Type()
)
ipSecTunnelHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutPkts.setStatus("mandatory")
_IpSecTunnelHistOutDropPkts_Type = Counter32
_IpSecTunnelHistOutDropPkts_Object = MibTableColumn
ipSecTunnelHistOutDropPkts = _IpSecTunnelHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 19),
    _IpSecTunnelHistOutDropPkts_Type()
)
ipSecTunnelHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutDropPkts.setStatus("mandatory")
_IpSecTunnelHistOutAuths_Type = Counter32
_IpSecTunnelHistOutAuths_Object = MibTableColumn
ipSecTunnelHistOutAuths = _IpSecTunnelHistOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 20),
    _IpSecTunnelHistOutAuths_Type()
)
ipSecTunnelHistOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutAuths.setStatus("mandatory")
_IpSecTunnelHistOutAuthFails_Type = Counter32
_IpSecTunnelHistOutAuthFails_Object = MibTableColumn
ipSecTunnelHistOutAuthFails = _IpSecTunnelHistOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 21),
    _IpSecTunnelHistOutAuthFails_Type()
)
ipSecTunnelHistOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutAuthFails.setStatus("mandatory")
_IpSecTunnelHistOutEncrypts_Type = Counter32
_IpSecTunnelHistOutEncrypts_Object = MibTableColumn
ipSecTunnelHistOutEncrypts = _IpSecTunnelHistOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 22),
    _IpSecTunnelHistOutEncrypts_Type()
)
ipSecTunnelHistOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutEncrypts.setStatus("mandatory")
_IpSecTunnelHistOutEncryptFails_Type = Counter32
_IpSecTunnelHistOutEncryptFails_Object = MibTableColumn
ipSecTunnelHistOutEncryptFails = _IpSecTunnelHistOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 23),
    _IpSecTunnelHistOutEncryptFails_Type()
)
ipSecTunnelHistOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutEncryptFails.setStatus("mandatory")
_IpSecTunnelHistInOctWraps_Type = Counter32
_IpSecTunnelHistInOctWraps_Object = MibTableColumn
ipSecTunnelHistInOctWraps = _IpSecTunnelHistInOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 24),
    _IpSecTunnelHistInOctWraps_Type()
)
ipSecTunnelHistInOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInOctWraps.setStatus("mandatory")
_IpSecTunnelHistInDecompOctWraps_Type = Counter32
_IpSecTunnelHistInDecompOctWraps_Object = MibTableColumn
ipSecTunnelHistInDecompOctWraps = _IpSecTunnelHistInDecompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 25),
    _IpSecTunnelHistInDecompOctWraps_Type()
)
ipSecTunnelHistInDecompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistInDecompOctWraps.setStatus("mandatory")
_IpSecTunnelHistOutOctWraps_Type = Counter32
_IpSecTunnelHistOutOctWraps_Object = MibTableColumn
ipSecTunnelHistOutOctWraps = _IpSecTunnelHistOutOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 26),
    _IpSecTunnelHistOutOctWraps_Type()
)
ipSecTunnelHistOutOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutOctWraps.setStatus("mandatory")
_IpSecTunnelHistOutUncompOctWraps_Type = Counter32
_IpSecTunnelHistOutUncompOctWraps_Object = MibTableColumn
ipSecTunnelHistOutUncompOctWraps = _IpSecTunnelHistOutUncompOctWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 2, 1, 27),
    _IpSecTunnelHistOutUncompOctWraps_Type()
)
ipSecTunnelHistOutUncompOctWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecTunnelHistOutUncompOctWraps.setStatus("mandatory")
_IpSecFailTable_Object = MibTable
ipSecFailTable = _IpSecFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3)
)
if mibBuilder.loadTexts:
    ipSecFailTable.setStatus("mandatory")
_IpSecFailEntry_Object = MibTableRow
ipSecFailEntry = _IpSecFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1)
)
ipSecFailEntry.setIndexNames(
    (0, "IPSECV1-MIB", "ipSecFailIndex"),
)
if mibBuilder.loadTexts:
    ipSecFailEntry.setStatus("mandatory")


class _IpSecFailIndex_Type(Integer32):
    """Custom type ipSecFailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSecFailIndex_Type.__name__ = "Integer32"
_IpSecFailIndex_Object = MibTableColumn
ipSecFailIndex = _IpSecFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 1),
    _IpSecFailIndex_Type()
)
ipSecFailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailIndex.setStatus("mandatory")


class _IpSecFailReason_Type(Integer32):
    """Custom type ipSecFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("compression", 6),
          ("decompression", 7),
          ("decryption", 4),
          ("encryption", 5),
          ("other", 1),
          ("recvAuthentication", 3),
          ("sendAuthentication", 2))
    )


_IpSecFailReason_Type.__name__ = "Integer32"
_IpSecFailReason_Object = MibTableColumn
ipSecFailReason = _IpSecFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 2),
    _IpSecFailReason_Type()
)
ipSecFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailReason.setStatus("mandatory")
_IpSecFailTime_Type = TimeTicks
_IpSecFailTime_Object = MibTableColumn
ipSecFailTime = _IpSecFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 3),
    _IpSecFailTime_Type()
)
ipSecFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailTime.setStatus("mandatory")


class _IpSecFailTunnelIndex_Type(Integer32):
    """Custom type ipSecFailTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSecFailTunnelIndex_Type.__name__ = "Integer32"
_IpSecFailTunnelIndex_Object = MibTableColumn
ipSecFailTunnelIndex = _IpSecFailTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 4),
    _IpSecFailTunnelIndex_Type()
)
ipSecFailTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailTunnelIndex.setStatus("mandatory")


class _IpSecFailTunnelId_Type(Integer32):
    """Custom type ipSecFailTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSecFailTunnelId_Type.__name__ = "Integer32"
_IpSecFailTunnelId_Object = MibTableColumn
ipSecFailTunnelId = _IpSecFailTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 5),
    _IpSecFailTunnelId_Type()
)
ipSecFailTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailTunnelId.setStatus("mandatory")
_IpSecFailSaSpi_Type = Integer32
_IpSecFailSaSpi_Object = MibTableColumn
ipSecFailSaSpi = _IpSecFailSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 6),
    _IpSecFailSaSpi_Type()
)
ipSecFailSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailSaSpi.setStatus("mandatory")
_IpSecFailPktSrcAddr_Type = IPSIpAddress
_IpSecFailPktSrcAddr_Object = MibTableColumn
ipSecFailPktSrcAddr = _IpSecFailPktSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 7),
    _IpSecFailPktSrcAddr_Type()
)
ipSecFailPktSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailPktSrcAddr.setStatus("mandatory")
_IpSecFailPktDstAddr_Type = IPSIpAddress
_IpSecFailPktDstAddr_Object = MibTableColumn
ipSecFailPktDstAddr = _IpSecFailPktDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 4, 3, 1, 8),
    _IpSecFailPktDstAddr_Type()
)
ipSecFailPktDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecFailPktDstAddr.setStatus("mandatory")
_IpSecTrapCntl_ObjectIdentity = ObjectIdentity
ipSecTrapCntl = _IpSecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5)
)


class _IpSecTrapCntlIkeTunnelStart_Type(Integer32):
    """Custom type ipSecTrapCntlIkeTunnelStart based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlIkeTunnelStart_Type.__name__ = "Integer32"
_IpSecTrapCntlIkeTunnelStart_Object = MibScalar
ipSecTrapCntlIkeTunnelStart = _IpSecTrapCntlIkeTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 1),
    _IpSecTrapCntlIkeTunnelStart_Type()
)
ipSecTrapCntlIkeTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlIkeTunnelStart.setStatus("mandatory")


class _IpSecTrapCntlIkeTunnelStop_Type(Integer32):
    """Custom type ipSecTrapCntlIkeTunnelStop based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlIkeTunnelStop_Type.__name__ = "Integer32"
_IpSecTrapCntlIkeTunnelStop_Object = MibScalar
ipSecTrapCntlIkeTunnelStop = _IpSecTrapCntlIkeTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 2),
    _IpSecTrapCntlIkeTunnelStop_Type()
)
ipSecTrapCntlIkeTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlIkeTunnelStop.setStatus("mandatory")


class _IpSecTrapCntlP2TunnelStart_Type(Integer32):
    """Custom type ipSecTrapCntlP2TunnelStart based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlP2TunnelStart_Type.__name__ = "Integer32"
_IpSecTrapCntlP2TunnelStart_Object = MibScalar
ipSecTrapCntlP2TunnelStart = _IpSecTrapCntlP2TunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 3),
    _IpSecTrapCntlP2TunnelStart_Type()
)
ipSecTrapCntlP2TunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlP2TunnelStart.setStatus("mandatory")


class _IpSecTrapCntlP2TunnelStop_Type(Integer32):
    """Custom type ipSecTrapCntlP2TunnelStop based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlP2TunnelStop_Type.__name__ = "Integer32"
_IpSecTrapCntlP2TunnelStop_Object = MibScalar
ipSecTrapCntlP2TunnelStop = _IpSecTrapCntlP2TunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 4),
    _IpSecTrapCntlP2TunnelStop_Type()
)
ipSecTrapCntlP2TunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlP2TunnelStop.setStatus("mandatory")


class _IpSecTrapCntlAuthFail_Type(Integer32):
    """Custom type ipSecTrapCntlAuthFail based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlAuthFail_Type.__name__ = "Integer32"
_IpSecTrapCntlAuthFail_Object = MibScalar
ipSecTrapCntlAuthFail = _IpSecTrapCntlAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 5),
    _IpSecTrapCntlAuthFail_Type()
)
ipSecTrapCntlAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlAuthFail.setStatus("mandatory")


class _IpSecTrapCntlDecryptFail_Type(Integer32):
    """Custom type ipSecTrapCntlDecryptFail based on Integer32"""
    defaultValue = 1

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


_IpSecTrapCntlDecryptFail_Type.__name__ = "Integer32"
_IpSecTrapCntlDecryptFail_Object = MibScalar
ipSecTrapCntlDecryptFail = _IpSecTrapCntlDecryptFail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 5, 6),
    _IpSecTrapCntlDecryptFail_Type()
)
ipSecTrapCntlDecryptFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecTrapCntlDecryptFail.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ikeTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 1)
)
ikeTunnelStart.setObjects(
      *(("IPSECV1-MIB", "ikeTunnelIndex"),
        ("IPSECV1-MIB", "ikeTunnelId"))
)
if mibBuilder.loadTexts:
    ikeTunnelStart.setStatus(
        ""
    )

ikeTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 2)
)
ikeTunnelStop.setObjects(
      *(("IPSECV1-MIB", "ikeTunnelIndex"),
        ("IPSECV1-MIB", "ikeTunnelId"),
        ("IPSECV1-MIB", "ikeTunnelActiveTime"))
)
if mibBuilder.loadTexts:
    ikeTunnelStop.setStatus(
        ""
    )

ipSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 3)
)
ipSecTunnelStart.setObjects(
      *(("IPSECV1-MIB", "ipSecTunnelIndex"),
        ("IPSECV1-MIB", "ipSecTunnelId"))
)
if mibBuilder.loadTexts:
    ipSecTunnelStart.setStatus(
        ""
    )

ipSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 4)
)
ipSecTunnelStop.setObjects(
      *(("IPSECV1-MIB", "ipSecTunnelIndex"),
        ("IPSECV1-MIB", "ipSecTunnelId"),
        ("IPSECV1-MIB", "ipSecTunnelActiveTime"))
)
if mibBuilder.loadTexts:
    ipSecTunnelStop.setStatus(
        ""
    )

ipSecAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 5)
)
ipSecAuthFail.setObjects(
      *(("IPSECV1-MIB", "ipSecTunnelIndex"),
        ("IPSECV1-MIB", "ipSecTunnelId"),
        ("IPSECV1-MIB", "ipSecFailTime"),
        ("IPSECV1-MIB", "ipSecFailPktSrcAddr"),
        ("IPSECV1-MIB", "ipSecFailPktDstAddr"))
)
if mibBuilder.loadTexts:
    ipSecAuthFail.setStatus(
        ""
    )

ipSecDecryptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9, 0, 6)
)
ipSecDecryptFail.setObjects(
      *(("IPSECV1-MIB", "ipSecTunnelIndex"),
        ("IPSECV1-MIB", "ipSecTunnelId"),
        ("IPSECV1-MIB", "ipSecFailTime"),
        ("IPSECV1-MIB", "ipSecFailPktSrcAddr"),
        ("IPSECV1-MIB", "ipSecFailPktDstAddr"))
)
if mibBuilder.loadTexts:
    ipSecDecryptFail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSECV1-MIB",
    **{"IPSIpAddress": IPSIpAddress,
       "ibmIROCroutingIpSec": ibmIROCroutingIpSec,
       "ikeTunnelStart": ikeTunnelStart,
       "ikeTunnelStop": ikeTunnelStop,
       "ipSecTunnelStart": ipSecTunnelStart,
       "ipSecTunnelStop": ipSecTunnelStop,
       "ipSecAuthFail": ipSecAuthFail,
       "ipSecDecryptFail": ipSecDecryptFail,
       "ipSecLevels": ipSecLevels,
       "ipSecMibLevel": ipSecMibLevel,
       "ipSecPhaseOne": ipSecPhaseOne,
       "ikeTunnelTable": ikeTunnelTable,
       "ikeTunnelEntry": ikeTunnelEntry,
       "ikeTunnelIndex": ikeTunnelIndex,
       "ikeTunnelId": ikeTunnelId,
       "ikeTunnelLocalAddr": ikeTunnelLocalAddr,
       "ikeTunnelLocalName": ikeTunnelLocalName,
       "ikeTunnelRemoteAddr": ikeTunnelRemoteAddr,
       "ikeTunnelRemoteName": ikeTunnelRemoteName,
       "ikeTunnelNegoMode": ikeTunnelNegoMode,
       "ikeTunnelLifetime": ikeTunnelLifetime,
       "ikeTunnelActiveTime": ikeTunnelActiveTime,
       "ikeTunnelSaRefreshThreshold": ikeTunnelSaRefreshThreshold,
       "ikeTunnelTotalRefreshes": ikeTunnelTotalRefreshes,
       "ikeTunnelInOctets": ikeTunnelInOctets,
       "ikeTunnelInPkts": ikeTunnelInPkts,
       "ikeTunnelInDropPkts": ikeTunnelInDropPkts,
       "ikeTunnelInNotifys": ikeTunnelInNotifys,
       "ikeTunnelInP2Proposals": ikeTunnelInP2Proposals,
       "ikeTunnelInP2ProposalInvalids": ikeTunnelInP2ProposalInvalids,
       "ikeTunnelInP2ProposalRejects": ikeTunnelInP2ProposalRejects,
       "ikeTunnelInSaDeleteRequests": ikeTunnelInSaDeleteRequests,
       "ikeTunnelOutOctets": ikeTunnelOutOctets,
       "ikeTunnelOutPkts": ikeTunnelOutPkts,
       "ikeTunnelOutDropPkts": ikeTunnelOutDropPkts,
       "ikeTunnelOutNotifys": ikeTunnelOutNotifys,
       "ikeTunnelOutP2Proposals": ikeTunnelOutP2Proposals,
       "ikeTunnelOutP2ProposalRejects": ikeTunnelOutP2ProposalRejects,
       "ikeTunnelOutSaDeleteRequests": ikeTunnelOutSaDeleteRequests,
       "ikeTunnelStatus": ikeTunnelStatus,
       "ipSecPhaseTwo": ipSecPhaseTwo,
       "ipSecGlobal": ipSecGlobal,
       "ipSecGlobalActiveTunnels": ipSecGlobalActiveTunnels,
       "ipSecGlobalPreviousTunnels": ipSecGlobalPreviousTunnels,
       "ipSecGlobalInOctets": ipSecGlobalInOctets,
       "ipSecGlobalInPkts": ipSecGlobalInPkts,
       "ipSecGlobalInDrops": ipSecGlobalInDrops,
       "ipSecGlobalInAuths": ipSecGlobalInAuths,
       "ipSecGlobalInAuthFails": ipSecGlobalInAuthFails,
       "ipSecGlobalInDecrypts": ipSecGlobalInDecrypts,
       "ipSecGlobalInDecryptFails": ipSecGlobalInDecryptFails,
       "ipSecGlobalOutOctets": ipSecGlobalOutOctets,
       "ipSecGlobalOutPkts": ipSecGlobalOutPkts,
       "ipSecGlobalOutDrops": ipSecGlobalOutDrops,
       "ipSecGlobalOutAuths": ipSecGlobalOutAuths,
       "ipSecGlobalOutAuthFails": ipSecGlobalOutAuthFails,
       "ipSecGlobalOutEncrypts": ipSecGlobalOutEncrypts,
       "ipSecGlobalOutEncryptFails": ipSecGlobalOutEncryptFails,
       "ipSecGlobalInOctWraps": ipSecGlobalInOctWraps,
       "ipSecGlobalOutOctWraps": ipSecGlobalOutOctWraps,
       "ipSecTunnelTable": ipSecTunnelTable,
       "ipSecTunnelEntry": ipSecTunnelEntry,
       "ipSecTunnelIndex": ipSecTunnelIndex,
       "ipSecTunnelId": ipSecTunnelId,
       "ipSecTunnelIkeTunnelIndex": ipSecTunnelIkeTunnelIndex,
       "ipSecTunnelLocalAddr": ipSecTunnelLocalAddr,
       "ipSecTunnelRemoteAddr": ipSecTunnelRemoteAddr,
       "ipSecTunnelKeyType": ipSecTunnelKeyType,
       "ipSecTunnelEncapMode": ipSecTunnelEncapMode,
       "ipSecTunnelLifetime": ipSecTunnelLifetime,
       "ipSecTunnelActiveTime": ipSecTunnelActiveTime,
       "ipSecTunnelSaRefreshThreshold": ipSecTunnelSaRefreshThreshold,
       "ipSecTunnelTotalRefreshes": ipSecTunnelTotalRefreshes,
       "ipSecTunnelExpiredSaInstances": ipSecTunnelExpiredSaInstances,
       "ipSecTunnelCurrentSaInstances": ipSecTunnelCurrentSaInstances,
       "ipSecTunnelInSaEncrypt": ipSecTunnelInSaEncrypt,
       "ipSecTunnelInSaAuthAlgo": ipSecTunnelInSaAuthAlgo,
       "ipSecTunnelOutSaEncrypt": ipSecTunnelOutSaEncrypt,
       "ipSecTunnelOutSaAuthAlgo": ipSecTunnelOutSaAuthAlgo,
       "ipSecTunnelInOctets": ipSecTunnelInOctets,
       "ipSecTunnelInDecompOctets": ipSecTunnelInDecompOctets,
       "ipSecTunnelInPkts": ipSecTunnelInPkts,
       "ipSecTunnelInDropPkts": ipSecTunnelInDropPkts,
       "ipSecTunnelInAuths": ipSecTunnelInAuths,
       "ipSecTunnelInAuthFails": ipSecTunnelInAuthFails,
       "ipSecTunnelInDecrypts": ipSecTunnelInDecrypts,
       "ipSecTunnelInDecryptFails": ipSecTunnelInDecryptFails,
       "ipSecTunnelOutOctets": ipSecTunnelOutOctets,
       "ipSecTunnelOutUncompOctets": ipSecTunnelOutUncompOctets,
       "ipSecTunnelOutPkts": ipSecTunnelOutPkts,
       "ipSecTunnelOutDropPkts": ipSecTunnelOutDropPkts,
       "ipSecTunnelOutAuths": ipSecTunnelOutAuths,
       "ipSecTunnelOutAuthFails": ipSecTunnelOutAuthFails,
       "ipSecTunnelOutEncrypts": ipSecTunnelOutEncrypts,
       "ipSecTunnelOutEncryptFails": ipSecTunnelOutEncryptFails,
       "ipSecTunnelStatus": ipSecTunnelStatus,
       "ipSecTunnelInOctWraps": ipSecTunnelInOctWraps,
       "ipSecTunnelInDecompOctWraps": ipSecTunnelInDecompOctWraps,
       "ipSecTunnelOutOctWraps": ipSecTunnelOutOctWraps,
       "ipSecTunnelOutUncompOctWraps": ipSecTunnelOutUncompOctWraps,
       "ipSecClientTable": ipSecClientTable,
       "ipSecClientEntry": ipSecClientEntry,
       "ipSecClientIndex": ipSecClientIndex,
       "ipSecClientLocalName": ipSecClientLocalName,
       "ipSecClientLocalType": ipSecClientLocalType,
       "ipSecClientLocalProtocol": ipSecClientLocalProtocol,
       "ipSecClientLocalSubnetMask": ipSecClientLocalSubnetMask,
       "ipSecClientLocalHiAddr": ipSecClientLocalHiAddr,
       "ipSecClientLocalLoAddr": ipSecClientLocalLoAddr,
       "ipSecClientLocalPort": ipSecClientLocalPort,
       "ipSecClientRemoteName": ipSecClientRemoteName,
       "ipSecClientRemoteType": ipSecClientRemoteType,
       "ipSecClientRemoteProtocol": ipSecClientRemoteProtocol,
       "ipSecClientRemoteSubnetMask": ipSecClientRemoteSubnetMask,
       "ipSecClientRemoteHiAddr": ipSecClientRemoteHiAddr,
       "ipSecClientRemoteLoAddr": ipSecClientRemoteLoAddr,
       "ipSecClientRemotePort": ipSecClientRemotePort,
       "ipSecSpiTable": ipSecSpiTable,
       "ipSecSpiEntry": ipSecSpiEntry,
       "ipSecSpiIndex": ipSecSpiIndex,
       "ipSecSpiDirection": ipSecSpiDirection,
       "ipSecSpiValue": ipSecSpiValue,
       "ipSecSpiProtocol": ipSecSpiProtocol,
       "ipSecSpiStatus": ipSecSpiStatus,
       "ipSecHistory": ipSecHistory,
       "ipSecTunnelHistTable": ipSecTunnelHistTable,
       "ipSecTunnelHistEntry": ipSecTunnelHistEntry,
       "ipSecTunnelHistIndex": ipSecTunnelHistIndex,
       "ipSecTunnelHistId": ipSecTunnelHistId,
       "ipSecTunnelHistLocalAddr": ipSecTunnelHistLocalAddr,
       "ipSecTunnelHistRemoteAddr": ipSecTunnelHistRemoteAddr,
       "ipSecTunnelHistActiveTime": ipSecTunnelHistActiveTime,
       "ipSecTunnelHistTotalRefreshes": ipSecTunnelHistTotalRefreshes,
       "ipSecTunnelHistTotalSas": ipSecTunnelHistTotalSas,
       "ipSecTunnelHistInOctets": ipSecTunnelHistInOctets,
       "ipSecTunnelHistInDecompOctets": ipSecTunnelHistInDecompOctets,
       "ipSecTunnelHistInPkts": ipSecTunnelHistInPkts,
       "ipSecTunnelHistInDropPkts": ipSecTunnelHistInDropPkts,
       "ipSecTunnelHistInAuths": ipSecTunnelHistInAuths,
       "ipSecTunnelHistInAuthFails": ipSecTunnelHistInAuthFails,
       "ipSecTunnelHistInDecrypts": ipSecTunnelHistInDecrypts,
       "ipSecTunnelHistInDecryptFails": ipSecTunnelHistInDecryptFails,
       "ipSecTunnelHistOutOctets": ipSecTunnelHistOutOctets,
       "ipSecTunnelHistOutUncompOctets": ipSecTunnelHistOutUncompOctets,
       "ipSecTunnelHistOutPkts": ipSecTunnelHistOutPkts,
       "ipSecTunnelHistOutDropPkts": ipSecTunnelHistOutDropPkts,
       "ipSecTunnelHistOutAuths": ipSecTunnelHistOutAuths,
       "ipSecTunnelHistOutAuthFails": ipSecTunnelHistOutAuthFails,
       "ipSecTunnelHistOutEncrypts": ipSecTunnelHistOutEncrypts,
       "ipSecTunnelHistOutEncryptFails": ipSecTunnelHistOutEncryptFails,
       "ipSecTunnelHistInOctWraps": ipSecTunnelHistInOctWraps,
       "ipSecTunnelHistInDecompOctWraps": ipSecTunnelHistInDecompOctWraps,
       "ipSecTunnelHistOutOctWraps": ipSecTunnelHistOutOctWraps,
       "ipSecTunnelHistOutUncompOctWraps": ipSecTunnelHistOutUncompOctWraps,
       "ipSecFailTable": ipSecFailTable,
       "ipSecFailEntry": ipSecFailEntry,
       "ipSecFailIndex": ipSecFailIndex,
       "ipSecFailReason": ipSecFailReason,
       "ipSecFailTime": ipSecFailTime,
       "ipSecFailTunnelIndex": ipSecFailTunnelIndex,
       "ipSecFailTunnelId": ipSecFailTunnelId,
       "ipSecFailSaSpi": ipSecFailSaSpi,
       "ipSecFailPktSrcAddr": ipSecFailPktSrcAddr,
       "ipSecFailPktDstAddr": ipSecFailPktDstAddr,
       "ipSecTrapCntl": ipSecTrapCntl,
       "ipSecTrapCntlIkeTunnelStart": ipSecTrapCntlIkeTunnelStart,
       "ipSecTrapCntlIkeTunnelStop": ipSecTrapCntlIkeTunnelStop,
       "ipSecTrapCntlP2TunnelStart": ipSecTrapCntlP2TunnelStart,
       "ipSecTrapCntlP2TunnelStop": ipSecTrapCntlP2TunnelStop,
       "ipSecTrapCntlAuthFail": ipSecTrapCntlAuthFail,
       "ipSecTrapCntlDecryptFail": ipSecTrapCntlDecryptFail}
)
