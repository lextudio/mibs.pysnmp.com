# SNMP MIB module (ASCEND-MIBATMPNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMPNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:10 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibpnniNodeConfig_ObjectIdentity = ObjectIdentity
mibpnniNodeConfig = _MibpnniNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 43)
)
_MibpnniNodeConfigTable_Object = MibTable
mibpnniNodeConfigTable = _MibpnniNodeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1)
)
if mibBuilder.loadTexts:
    mibpnniNodeConfigTable.setStatus("mandatory")
_MibpnniNodeConfigEntry_Object = MibTableRow
mibpnniNodeConfigEntry = _MibpnniNodeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1)
)
mibpnniNodeConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniNodeConfig-NodeIndex"),
)
if mibBuilder.loadTexts:
    mibpnniNodeConfigEntry.setStatus("mandatory")
_PnniNodeConfig_NodeIndex_Type = Integer32
_PnniNodeConfig_NodeIndex_Object = MibScalar
pnniNodeConfig_NodeIndex = _PnniNodeConfig_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 1),
    _PnniNodeConfig_NodeIndex_Type()
)
pnniNodeConfig_NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeIndex.setStatus("mandatory")
_PnniNodeConfig_NodeLevel_Type = Integer32
_PnniNodeConfig_NodeLevel_Object = MibScalar
pnniNodeConfig_NodeLevel = _PnniNodeConfig_NodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 2),
    _PnniNodeConfig_NodeLevel_Type()
)
pnniNodeConfig_NodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeLevel.setStatus("mandatory")
_PnniNodeConfig_NodeId_Type = DisplayString
_PnniNodeConfig_NodeId_Object = MibScalar
pnniNodeConfig_NodeId = _PnniNodeConfig_NodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 3),
    _PnniNodeConfig_NodeId_Type()
)
pnniNodeConfig_NodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeId.setStatus("mandatory")
_PnniNodeConfig_CurrNodeId_Type = DisplayString
_PnniNodeConfig_CurrNodeId_Object = MibScalar
pnniNodeConfig_CurrNodeId = _PnniNodeConfig_CurrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 4),
    _PnniNodeConfig_CurrNodeId_Type()
)
pnniNodeConfig_CurrNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeConfig_CurrNodeId.setStatus("mandatory")


class _PnniNodeConfig_NodeLowest_Type(Integer32):
    """Custom type pnniNodeConfig_NodeLowest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniNodeConfig_NodeLowest_Type.__name__ = "Integer32"
_PnniNodeConfig_NodeLowest_Object = MibScalar
pnniNodeConfig_NodeLowest = _PnniNodeConfig_NodeLowest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 5),
    _PnniNodeConfig_NodeLowest_Type()
)
pnniNodeConfig_NodeLowest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeLowest.setStatus("mandatory")


class _PnniNodeConfig_NodeAdminStatus_Type(Integer32):
    """Custom type pnniNodeConfig_NodeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_PnniNodeConfig_NodeAdminStatus_Type.__name__ = "Integer32"
_PnniNodeConfig_NodeAdminStatus_Object = MibScalar
pnniNodeConfig_NodeAdminStatus = _PnniNodeConfig_NodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 6),
    _PnniNodeConfig_NodeAdminStatus_Type()
)
pnniNodeConfig_NodeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeAdminStatus.setStatus("mandatory")
_PnniNodeConfig_NodeDomainName_Type = DisplayString
_PnniNodeConfig_NodeDomainName_Object = MibScalar
pnniNodeConfig_NodeDomainName = _PnniNodeConfig_NodeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 7),
    _PnniNodeConfig_NodeDomainName_Type()
)
pnniNodeConfig_NodeDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeDomainName.setStatus("mandatory")
_PnniNodeConfig_NodeAtmAddress_Type = DisplayString
_PnniNodeConfig_NodeAtmAddress_Object = MibScalar
pnniNodeConfig_NodeAtmAddress = _PnniNodeConfig_NodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 8),
    _PnniNodeConfig_NodeAtmAddress_Type()
)
pnniNodeConfig_NodeAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeAtmAddress.setStatus("mandatory")
_PnniNodeConfig_NodePeerGroupId_Type = DisplayString
_PnniNodeConfig_NodePeerGroupId_Object = MibScalar
pnniNodeConfig_NodePeerGroupId = _PnniNodeConfig_NodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 9),
    _PnniNodeConfig_NodePeerGroupId_Type()
)
pnniNodeConfig_NodePeerGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePeerGroupId.setStatus("mandatory")
_PnniNodeConfig_CurrNodePeerGroupId_Type = DisplayString
_PnniNodeConfig_CurrNodePeerGroupId_Object = MibScalar
pnniNodeConfig_CurrNodePeerGroupId = _PnniNodeConfig_CurrNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 10),
    _PnniNodeConfig_CurrNodePeerGroupId_Type()
)
pnniNodeConfig_CurrNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeConfig_CurrNodePeerGroupId.setStatus("mandatory")


class _PnniNodeConfig_NodeRestrictedTransit_Type(Integer32):
    """Custom type pnniNodeConfig_NodeRestrictedTransit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniNodeConfig_NodeRestrictedTransit_Type.__name__ = "Integer32"
_PnniNodeConfig_NodeRestrictedTransit_Object = MibScalar
pnniNodeConfig_NodeRestrictedTransit = _PnniNodeConfig_NodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 11),
    _PnniNodeConfig_NodeRestrictedTransit_Type()
)
pnniNodeConfig_NodeRestrictedTransit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeRestrictedTransit.setStatus("mandatory")


class _PnniNodeConfig_NodeComplexRep_Type(Integer32):
    """Custom type pnniNodeConfig_NodeComplexRep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniNodeConfig_NodeComplexRep_Type.__name__ = "Integer32"
_PnniNodeConfig_NodeComplexRep_Object = MibScalar
pnniNodeConfig_NodeComplexRep = _PnniNodeConfig_NodeComplexRep_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 12),
    _PnniNodeConfig_NodeComplexRep_Type()
)
pnniNodeConfig_NodeComplexRep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeComplexRep.setStatus("mandatory")
_PnniNodeConfig_NodePgl_LeadershipPriority_Type = Integer32
_PnniNodeConfig_NodePgl_LeadershipPriority_Object = MibScalar
pnniNodeConfig_NodePgl_LeadershipPriority = _PnniNodeConfig_NodePgl_LeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 13),
    _PnniNodeConfig_NodePgl_LeadershipPriority_Type()
)
pnniNodeConfig_NodePgl_LeadershipPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePgl_LeadershipPriority.setStatus("mandatory")
_PnniNodeConfig_NodePgl_ParentNodeIndex_Type = Integer32
_PnniNodeConfig_NodePgl_ParentNodeIndex_Object = MibScalar
pnniNodeConfig_NodePgl_ParentNodeIndex = _PnniNodeConfig_NodePgl_ParentNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 14),
    _PnniNodeConfig_NodePgl_ParentNodeIndex_Type()
)
pnniNodeConfig_NodePgl_ParentNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePgl_ParentNodeIndex.setStatus("mandatory")
_PnniNodeConfig_NodePgl_InitTime_Type = Integer32
_PnniNodeConfig_NodePgl_InitTime_Object = MibScalar
pnniNodeConfig_NodePgl_InitTime = _PnniNodeConfig_NodePgl_InitTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 15),
    _PnniNodeConfig_NodePgl_InitTime_Type()
)
pnniNodeConfig_NodePgl_InitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePgl_InitTime.setStatus("mandatory")
_PnniNodeConfig_NodePgl_OverrideDelay_Type = Integer32
_PnniNodeConfig_NodePgl_OverrideDelay_Object = MibScalar
pnniNodeConfig_NodePgl_OverrideDelay = _PnniNodeConfig_NodePgl_OverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 16),
    _PnniNodeConfig_NodePgl_OverrideDelay_Type()
)
pnniNodeConfig_NodePgl_OverrideDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePgl_OverrideDelay.setStatus("mandatory")
_PnniNodeConfig_NodePgl_ReelectTime_Type = Integer32
_PnniNodeConfig_NodePgl_ReelectTime_Object = MibScalar
pnniNodeConfig_NodePgl_ReelectTime = _PnniNodeConfig_NodePgl_ReelectTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 17),
    _PnniNodeConfig_NodePgl_ReelectTime_Type()
)
pnniNodeConfig_NodePgl_ReelectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodePgl_ReelectTime.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_PtseHolddown_Type = Integer32
_PnniNodeConfig_NodeTimer_PtseHolddown_Object = MibScalar
pnniNodeConfig_NodeTimer_PtseHolddown = _PnniNodeConfig_NodeTimer_PtseHolddown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 18),
    _PnniNodeConfig_NodeTimer_PtseHolddown_Type()
)
pnniNodeConfig_NodeTimer_PtseHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_PtseHolddown.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_HelloHolddown_Type = Integer32
_PnniNodeConfig_NodeTimer_HelloHolddown_Object = MibScalar
pnniNodeConfig_NodeTimer_HelloHolddown = _PnniNodeConfig_NodeTimer_HelloHolddown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 19),
    _PnniNodeConfig_NodeTimer_HelloHolddown_Type()
)
pnniNodeConfig_NodeTimer_HelloHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_HelloHolddown.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_HelloInterval_Type = Integer32
_PnniNodeConfig_NodeTimer_HelloInterval_Object = MibScalar
pnniNodeConfig_NodeTimer_HelloInterval = _PnniNodeConfig_NodeTimer_HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 20),
    _PnniNodeConfig_NodeTimer_HelloInterval_Type()
)
pnniNodeConfig_NodeTimer_HelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_HelloInterval.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_HelloInactivityFactor_Type = Integer32
_PnniNodeConfig_NodeTimer_HelloInactivityFactor_Object = MibScalar
pnniNodeConfig_NodeTimer_HelloInactivityFactor = _PnniNodeConfig_NodeTimer_HelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 21),
    _PnniNodeConfig_NodeTimer_HelloInactivityFactor_Type()
)
pnniNodeConfig_NodeTimer_HelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_HelloInactivityFactor.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_HlinkInact_Type = Integer32
_PnniNodeConfig_NodeTimer_HlinkInact_Object = MibScalar
pnniNodeConfig_NodeTimer_HlinkInact = _PnniNodeConfig_NodeTimer_HlinkInact_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 22),
    _PnniNodeConfig_NodeTimer_HlinkInact_Type()
)
pnniNodeConfig_NodeTimer_HlinkInact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_HlinkInact.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_PtseRefreshInterval_Type = Integer32
_PnniNodeConfig_NodeTimer_PtseRefreshInterval_Object = MibScalar
pnniNodeConfig_NodeTimer_PtseRefreshInterval = _PnniNodeConfig_NodeTimer_PtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 23),
    _PnniNodeConfig_NodeTimer_PtseRefreshInterval_Type()
)
pnniNodeConfig_NodeTimer_PtseRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_PtseRefreshInterval.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_PtseLifetimeFactor_Type = Integer32
_PnniNodeConfig_NodeTimer_PtseLifetimeFactor_Object = MibScalar
pnniNodeConfig_NodeTimer_PtseLifetimeFactor = _PnniNodeConfig_NodeTimer_PtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 24),
    _PnniNodeConfig_NodeTimer_PtseLifetimeFactor_Type()
)
pnniNodeConfig_NodeTimer_PtseLifetimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_PtseLifetimeFactor.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_RxmtInterval_Type = Integer32
_PnniNodeConfig_NodeTimer_RxmtInterval_Object = MibScalar
pnniNodeConfig_NodeTimer_RxmtInterval = _PnniNodeConfig_NodeTimer_RxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 25),
    _PnniNodeConfig_NodeTimer_RxmtInterval_Type()
)
pnniNodeConfig_NodeTimer_RxmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_RxmtInterval.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_PeerDelayedAckInterval_Type = Integer32
_PnniNodeConfig_NodeTimer_PeerDelayedAckInterval_Object = MibScalar
pnniNodeConfig_NodeTimer_PeerDelayedAckInterval = _PnniNodeConfig_NodeTimer_PeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 26),
    _PnniNodeConfig_NodeTimer_PeerDelayedAckInterval_Type()
)
pnniNodeConfig_NodeTimer_PeerDelayedAckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_PeerDelayedAckInterval.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_AvcrPm_Type = Integer32
_PnniNodeConfig_NodeTimer_AvcrPm_Object = MibScalar
pnniNodeConfig_NodeTimer_AvcrPm = _PnniNodeConfig_NodeTimer_AvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 27),
    _PnniNodeConfig_NodeTimer_AvcrPm_Type()
)
pnniNodeConfig_NodeTimer_AvcrPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_AvcrPm.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_AvcrMt_Type = Integer32
_PnniNodeConfig_NodeTimer_AvcrMt_Object = MibScalar
pnniNodeConfig_NodeTimer_AvcrMt = _PnniNodeConfig_NodeTimer_AvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 28),
    _PnniNodeConfig_NodeTimer_AvcrMt_Type()
)
pnniNodeConfig_NodeTimer_AvcrMt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_AvcrMt.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_CdvPm_Type = Integer32
_PnniNodeConfig_NodeTimer_CdvPm_Object = MibScalar
pnniNodeConfig_NodeTimer_CdvPm = _PnniNodeConfig_NodeTimer_CdvPm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 29),
    _PnniNodeConfig_NodeTimer_CdvPm_Type()
)
pnniNodeConfig_NodeTimer_CdvPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_CdvPm.setStatus("mandatory")
_PnniNodeConfig_NodeTimer_CtdPm_Type = Integer32
_PnniNodeConfig_NodeTimer_CtdPm_Object = MibScalar
pnniNodeConfig_NodeTimer_CtdPm = _PnniNodeConfig_NodeTimer_CtdPm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 30),
    _PnniNodeConfig_NodeTimer_CtdPm_Type()
)
pnniNodeConfig_NodeTimer_CtdPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeTimer_CtdPm.setStatus("mandatory")
_PnniNodeConfig_NodeSvccRcc_InitTime_Type = Integer32
_PnniNodeConfig_NodeSvccRcc_InitTime_Object = MibScalar
pnniNodeConfig_NodeSvccRcc_InitTime = _PnniNodeConfig_NodeSvccRcc_InitTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 31),
    _PnniNodeConfig_NodeSvccRcc_InitTime_Type()
)
pnniNodeConfig_NodeSvccRcc_InitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeSvccRcc_InitTime.setStatus("mandatory")
_PnniNodeConfig_NodeSvccRcc_RetryTime_Type = Integer32
_PnniNodeConfig_NodeSvccRcc_RetryTime_Object = MibScalar
pnniNodeConfig_NodeSvccRcc_RetryTime = _PnniNodeConfig_NodeSvccRcc_RetryTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 32),
    _PnniNodeConfig_NodeSvccRcc_RetryTime_Type()
)
pnniNodeConfig_NodeSvccRcc_RetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeSvccRcc_RetryTime.setStatus("mandatory")
_PnniNodeConfig_NodeSvccRcc_CallingIntegrityTime_Type = Integer32
_PnniNodeConfig_NodeSvccRcc_CallingIntegrityTime_Object = MibScalar
pnniNodeConfig_NodeSvccRcc_CallingIntegrityTime = _PnniNodeConfig_NodeSvccRcc_CallingIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 33),
    _PnniNodeConfig_NodeSvccRcc_CallingIntegrityTime_Type()
)
pnniNodeConfig_NodeSvccRcc_CallingIntegrityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeSvccRcc_CallingIntegrityTime.setStatus("mandatory")
_PnniNodeConfig_NodeSvccRcc_CalledIntegrityTime_Type = Integer32
_PnniNodeConfig_NodeSvccRcc_CalledIntegrityTime_Object = MibScalar
pnniNodeConfig_NodeSvccRcc_CalledIntegrityTime = _PnniNodeConfig_NodeSvccRcc_CalledIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 34),
    _PnniNodeConfig_NodeSvccRcc_CalledIntegrityTime_Type()
)
pnniNodeConfig_NodeSvccRcc_CalledIntegrityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeSvccRcc_CalledIntegrityTime.setStatus("mandatory")
_PnniNodeConfig_NodeSvccRcc_TrafficDescrIndex_Type = Integer32
_PnniNodeConfig_NodeSvccRcc_TrafficDescrIndex_Object = MibScalar
pnniNodeConfig_NodeSvccRcc_TrafficDescrIndex = _PnniNodeConfig_NodeSvccRcc_TrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 35),
    _PnniNodeConfig_NodeSvccRcc_TrafficDescrIndex_Type()
)
pnniNodeConfig_NodeSvccRcc_TrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeSvccRcc_TrafficDescrIndex.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_LocalNet_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_LocalNet_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_LocalNet = _PnniNodeConfig_NodeScopeMapping_LocalNet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 36),
    _PnniNodeConfig_NodeScopeMapping_LocalNet_Type()
)
pnniNodeConfig_NodeScopeMapping_LocalNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_LocalNet.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_LocalNetPlus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_LocalNetPlus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_LocalNetPlus1 = _PnniNodeConfig_NodeScopeMapping_LocalNetPlus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 37),
    _PnniNodeConfig_NodeScopeMapping_LocalNetPlus1_Type()
)
pnniNodeConfig_NodeScopeMapping_LocalNetPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_LocalNetPlus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_LocalNetPlus2_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_LocalNetPlus2_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_LocalNetPlus2 = _PnniNodeConfig_NodeScopeMapping_LocalNetPlus2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 38),
    _PnniNodeConfig_NodeScopeMapping_LocalNetPlus2_Type()
)
pnniNodeConfig_NodeScopeMapping_LocalNetPlus2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_LocalNetPlus2.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_SiteMinus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_SiteMinus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_SiteMinus1 = _PnniNodeConfig_NodeScopeMapping_SiteMinus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 39),
    _PnniNodeConfig_NodeScopeMapping_SiteMinus1_Type()
)
pnniNodeConfig_NodeScopeMapping_SiteMinus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_SiteMinus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_IntraSite_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_IntraSite_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_IntraSite = _PnniNodeConfig_NodeScopeMapping_IntraSite_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 40),
    _PnniNodeConfig_NodeScopeMapping_IntraSite_Type()
)
pnniNodeConfig_NodeScopeMapping_IntraSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_IntraSite.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_SitePlus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_SitePlus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_SitePlus1 = _PnniNodeConfig_NodeScopeMapping_SitePlus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 41),
    _PnniNodeConfig_NodeScopeMapping_SitePlus1_Type()
)
pnniNodeConfig_NodeScopeMapping_SitePlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_SitePlus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_OrganizationMinus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_OrganizationMinus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_OrganizationMinus1 = _PnniNodeConfig_NodeScopeMapping_OrganizationMinus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 42),
    _PnniNodeConfig_NodeScopeMapping_OrganizationMinus1_Type()
)
pnniNodeConfig_NodeScopeMapping_OrganizationMinus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_OrganizationMinus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_IntraOrganization_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_IntraOrganization_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_IntraOrganization = _PnniNodeConfig_NodeScopeMapping_IntraOrganization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 43),
    _PnniNodeConfig_NodeScopeMapping_IntraOrganization_Type()
)
pnniNodeConfig_NodeScopeMapping_IntraOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_IntraOrganization.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_OrganizationPlus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_OrganizationPlus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_OrganizationPlus1 = _PnniNodeConfig_NodeScopeMapping_OrganizationPlus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 44),
    _PnniNodeConfig_NodeScopeMapping_OrganizationPlus1_Type()
)
pnniNodeConfig_NodeScopeMapping_OrganizationPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_OrganizationPlus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_CommunityMinus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_CommunityMinus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_CommunityMinus1 = _PnniNodeConfig_NodeScopeMapping_CommunityMinus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 45),
    _PnniNodeConfig_NodeScopeMapping_CommunityMinus1_Type()
)
pnniNodeConfig_NodeScopeMapping_CommunityMinus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_CommunityMinus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_IntraCommunity_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_IntraCommunity_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_IntraCommunity = _PnniNodeConfig_NodeScopeMapping_IntraCommunity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 46),
    _PnniNodeConfig_NodeScopeMapping_IntraCommunity_Type()
)
pnniNodeConfig_NodeScopeMapping_IntraCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_IntraCommunity.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_CommunityPlus1_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_CommunityPlus1_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_CommunityPlus1 = _PnniNodeConfig_NodeScopeMapping_CommunityPlus1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 47),
    _PnniNodeConfig_NodeScopeMapping_CommunityPlus1_Type()
)
pnniNodeConfig_NodeScopeMapping_CommunityPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_CommunityPlus1.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_Regional_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_Regional_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_Regional = _PnniNodeConfig_NodeScopeMapping_Regional_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 48),
    _PnniNodeConfig_NodeScopeMapping_Regional_Type()
)
pnniNodeConfig_NodeScopeMapping_Regional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_Regional.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_InterRegional_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_InterRegional_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_InterRegional = _PnniNodeConfig_NodeScopeMapping_InterRegional_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 49),
    _PnniNodeConfig_NodeScopeMapping_InterRegional_Type()
)
pnniNodeConfig_NodeScopeMapping_InterRegional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_InterRegional.setStatus("mandatory")
_PnniNodeConfig_NodeScopeMapping_Global_Type = Integer32
_PnniNodeConfig_NodeScopeMapping_Global_Object = MibScalar
pnniNodeConfig_NodeScopeMapping_Global = _PnniNodeConfig_NodeScopeMapping_Global_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 50),
    _PnniNodeConfig_NodeScopeMapping_Global_Type()
)
pnniNodeConfig_NodeScopeMapping_Global.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_NodeScopeMapping_Global.setStatus("mandatory")


class _PnniNodeConfig_Action_o_Type(Integer32):
    """Custom type pnniNodeConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniNodeConfig_Action_o_Type.__name__ = "Integer32"
_PnniNodeConfig_Action_o_Object = MibScalar
pnniNodeConfig_Action_o = _PnniNodeConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 43, 1, 1, 51),
    _PnniNodeConfig_Action_o_Type()
)
pnniNodeConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeConfig_Action_o.setStatus("mandatory")
_MibpnniSummaryAddrEntry_ObjectIdentity = ObjectIdentity
mibpnniSummaryAddrEntry = _MibpnniSummaryAddrEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 44)
)
_MibpnniSummaryAddrEntryTable_Object = MibTable
mibpnniSummaryAddrEntryTable = _MibpnniSummaryAddrEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1)
)
if mibBuilder.loadTexts:
    mibpnniSummaryAddrEntryTable.setStatus("mandatory")
_MibpnniSummaryAddrEntryEntry_Object = MibTableRow
mibpnniSummaryAddrEntryEntry = _MibpnniSummaryAddrEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1)
)
mibpnniSummaryAddrEntryEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniSummaryAddrEntry-IndexName"),
)
if mibBuilder.loadTexts:
    mibpnniSummaryAddrEntryEntry.setStatus("mandatory")
_PnniSummaryAddrEntry_IndexName_Type = DisplayString
_PnniSummaryAddrEntry_IndexName_Object = MibScalar
pnniSummaryAddrEntry_IndexName = _PnniSummaryAddrEntry_IndexName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 1),
    _PnniSummaryAddrEntry_IndexName_Type()
)
pnniSummaryAddrEntry_IndexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_IndexName.setStatus("mandatory")
_PnniSummaryAddrEntry_AddrIndex_NodeIndex_Type = Integer32
_PnniSummaryAddrEntry_AddrIndex_NodeIndex_Object = MibScalar
pnniSummaryAddrEntry_AddrIndex_NodeIndex = _PnniSummaryAddrEntry_AddrIndex_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 2),
    _PnniSummaryAddrEntry_AddrIndex_NodeIndex_Type()
)
pnniSummaryAddrEntry_AddrIndex_NodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_AddrIndex_NodeIndex.setStatus("mandatory")


class _PnniSummaryAddrEntry_AddrIndex_Type_Type(Integer32):
    """Custom type pnniSummaryAddrEntry_AddrIndex_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externalSummary", 3),
          ("internalSummary", 2))
    )


_PnniSummaryAddrEntry_AddrIndex_Type_Type.__name__ = "Integer32"
_PnniSummaryAddrEntry_AddrIndex_Type_Object = MibScalar
pnniSummaryAddrEntry_AddrIndex_Type = _PnniSummaryAddrEntry_AddrIndex_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 3),
    _PnniSummaryAddrEntry_AddrIndex_Type_Type()
)
pnniSummaryAddrEntry_AddrIndex_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_AddrIndex_Type.setStatus("mandatory")
_PnniSummaryAddrEntry_AddrIndex_Address_Type = DisplayString
_PnniSummaryAddrEntry_AddrIndex_Address_Object = MibScalar
pnniSummaryAddrEntry_AddrIndex_Address = _PnniSummaryAddrEntry_AddrIndex_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 4),
    _PnniSummaryAddrEntry_AddrIndex_Address_Type()
)
pnniSummaryAddrEntry_AddrIndex_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_AddrIndex_Address.setStatus("mandatory")
_PnniSummaryAddrEntry_AddrIndex_PrefixLen_Type = Integer32
_PnniSummaryAddrEntry_AddrIndex_PrefixLen_Object = MibScalar
pnniSummaryAddrEntry_AddrIndex_PrefixLen = _PnniSummaryAddrEntry_AddrIndex_PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 5),
    _PnniSummaryAddrEntry_AddrIndex_PrefixLen_Type()
)
pnniSummaryAddrEntry_AddrIndex_PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_AddrIndex_PrefixLen.setStatus("mandatory")


class _PnniSummaryAddrEntry_Suppress_Type(Integer32):
    """Custom type pnniSummaryAddrEntry_Suppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniSummaryAddrEntry_Suppress_Type.__name__ = "Integer32"
_PnniSummaryAddrEntry_Suppress_Object = MibScalar
pnniSummaryAddrEntry_Suppress = _PnniSummaryAddrEntry_Suppress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 6),
    _PnniSummaryAddrEntry_Suppress_Type()
)
pnniSummaryAddrEntry_Suppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_Suppress.setStatus("mandatory")


class _PnniSummaryAddrEntry_State_Type(Integer32):
    """Custom type pnniSummaryAddrEntry_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 2),
          ("inactive", 4),
          ("suppressing", 3))
    )


_PnniSummaryAddrEntry_State_Type.__name__ = "Integer32"
_PnniSummaryAddrEntry_State_Object = MibScalar
pnniSummaryAddrEntry_State = _PnniSummaryAddrEntry_State_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 7),
    _PnniSummaryAddrEntry_State_Type()
)
pnniSummaryAddrEntry_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_State.setStatus("mandatory")


class _PnniSummaryAddrEntry_Active_Type(Integer32):
    """Custom type pnniSummaryAddrEntry_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniSummaryAddrEntry_Active_Type.__name__ = "Integer32"
_PnniSummaryAddrEntry_Active_Object = MibScalar
pnniSummaryAddrEntry_Active = _PnniSummaryAddrEntry_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 8),
    _PnniSummaryAddrEntry_Active_Type()
)
pnniSummaryAddrEntry_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_Active.setStatus("mandatory")


class _PnniSummaryAddrEntry_Action_o_Type(Integer32):
    """Custom type pnniSummaryAddrEntry_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniSummaryAddrEntry_Action_o_Type.__name__ = "Integer32"
_PnniSummaryAddrEntry_Action_o_Object = MibScalar
pnniSummaryAddrEntry_Action_o = _PnniSummaryAddrEntry_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 44, 1, 1, 9),
    _PnniSummaryAddrEntry_Action_o_Type()
)
pnniSummaryAddrEntry_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSummaryAddrEntry_Action_o.setStatus("mandatory")
_MibpnniIfConfig_ObjectIdentity = ObjectIdentity
mibpnniIfConfig = _MibpnniIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 45)
)
_MibpnniIfConfigTable_Object = MibTable
mibpnniIfConfigTable = _MibpnniIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1)
)
if mibBuilder.loadTexts:
    mibpnniIfConfigTable.setStatus("mandatory")
_MibpnniIfConfigEntry_Object = MibTableRow
mibpnniIfConfigEntry = _MibpnniIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1)
)
mibpnniIfConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniIfConfig-Shelf-o"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniIfConfig-Slot-o"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniIfConfig-Item-o"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniIfConfig-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibpnniIfConfigEntry.setStatus("mandatory")
_PnniIfConfig_Shelf_o_Type = Integer32
_PnniIfConfig_Shelf_o_Object = MibScalar
pnniIfConfig_Shelf_o = _PnniIfConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 1),
    _PnniIfConfig_Shelf_o_Type()
)
pnniIfConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfConfig_Shelf_o.setStatus("mandatory")
_PnniIfConfig_Slot_o_Type = Integer32
_PnniIfConfig_Slot_o_Object = MibScalar
pnniIfConfig_Slot_o = _PnniIfConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 2),
    _PnniIfConfig_Slot_o_Type()
)
pnniIfConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfConfig_Slot_o.setStatus("mandatory")
_PnniIfConfig_Item_o_Type = Integer32
_PnniIfConfig_Item_o_Object = MibScalar
pnniIfConfig_Item_o = _PnniIfConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 3),
    _PnniIfConfig_Item_o_Type()
)
pnniIfConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfConfig_Item_o.setStatus("mandatory")
_PnniIfConfig_LogicalItem_o_Type = Integer32
_PnniIfConfig_LogicalItem_o_Object = MibScalar
pnniIfConfig_LogicalItem_o = _PnniIfConfig_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 4),
    _PnniIfConfig_LogicalItem_o_Type()
)
pnniIfConfig_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfConfig_LogicalItem_o.setStatus("mandatory")


class _PnniIfConfig_Address_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type pnniIfConfig_Address_PhysicalAddress_Shelf based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("anyShelf", 1),
          ("shelf1", 2),
          ("shelf2", 3),
          ("shelf3", 4),
          ("shelf4", 5),
          ("shelf5", 6),
          ("shelf6", 7),
          ("shelf7", 8),
          ("shelf8", 9),
          ("shelf9", 10))
    )


_PnniIfConfig_Address_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_PnniIfConfig_Address_PhysicalAddress_Shelf_Object = MibScalar
pnniIfConfig_Address_PhysicalAddress_Shelf = _PnniIfConfig_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 5),
    _PnniIfConfig_Address_PhysicalAddress_Shelf_Type()
)
pnniIfConfig_Address_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_Address_PhysicalAddress_Shelf.setStatus("mandatory")


class _PnniIfConfig_Address_PhysicalAddress_Slot_Type(Integer32):
    """Custom type pnniIfConfig_Address_PhysicalAddress_Slot based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_PnniIfConfig_Address_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_PnniIfConfig_Address_PhysicalAddress_Slot_Object = MibScalar
pnniIfConfig_Address_PhysicalAddress_Slot = _PnniIfConfig_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 6),
    _PnniIfConfig_Address_PhysicalAddress_Slot_Type()
)
pnniIfConfig_Address_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_Address_PhysicalAddress_Slot.setStatus("mandatory")
_PnniIfConfig_Address_PhysicalAddress_ItemNumber_Type = Integer32
_PnniIfConfig_Address_PhysicalAddress_ItemNumber_Object = MibScalar
pnniIfConfig_Address_PhysicalAddress_ItemNumber = _PnniIfConfig_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 7),
    _PnniIfConfig_Address_PhysicalAddress_ItemNumber_Type()
)
pnniIfConfig_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_PnniIfConfig_Address_LogicalItem_Type = Integer32
_PnniIfConfig_Address_LogicalItem_Object = MibScalar
pnniIfConfig_Address_LogicalItem = _PnniIfConfig_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 8),
    _PnniIfConfig_Address_LogicalItem_Type()
)
pnniIfConfig_Address_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_Address_LogicalItem.setStatus("mandatory")
_PnniIfConfig_IfNodeIndex_Type = Integer32
_PnniIfConfig_IfNodeIndex_Object = MibScalar
pnniIfConfig_IfNodeIndex = _PnniIfConfig_IfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 9),
    _PnniIfConfig_IfNodeIndex_Type()
)
pnniIfConfig_IfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfNodeIndex.setStatus("mandatory")
_PnniIfConfig_IfAggrToken_Type = Integer32
_PnniIfConfig_IfAggrToken_Object = MibScalar
pnniIfConfig_IfAggrToken = _PnniIfConfig_IfAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 10),
    _PnniIfConfig_IfAggrToken_Type()
)
pnniIfConfig_IfAggrToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAggrToken.setStatus("mandatory")


class _PnniIfConfig_IfVpCapability_Type(Integer32):
    """Custom type pnniIfConfig_IfVpCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniIfConfig_IfVpCapability_Type.__name__ = "Integer32"
_PnniIfConfig_IfVpCapability_Object = MibScalar
pnniIfConfig_IfVpCapability = _PnniIfConfig_IfVpCapability_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 11),
    _PnniIfConfig_IfVpCapability_Type()
)
pnniIfConfig_IfVpCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfConfig_IfVpCapability.setStatus("mandatory")
_PnniIfConfig_IfAdmWeightCbr_Type = Integer32
_PnniIfConfig_IfAdmWeightCbr_Object = MibScalar
pnniIfConfig_IfAdmWeightCbr = _PnniIfConfig_IfAdmWeightCbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 12),
    _PnniIfConfig_IfAdmWeightCbr_Type()
)
pnniIfConfig_IfAdmWeightCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAdmWeightCbr.setStatus("mandatory")
_PnniIfConfig_IfAdmWeightRtVbr_Type = Integer32
_PnniIfConfig_IfAdmWeightRtVbr_Object = MibScalar
pnniIfConfig_IfAdmWeightRtVbr = _PnniIfConfig_IfAdmWeightRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 13),
    _PnniIfConfig_IfAdmWeightRtVbr_Type()
)
pnniIfConfig_IfAdmWeightRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAdmWeightRtVbr.setStatus("mandatory")
_PnniIfConfig_IfAdmWeightNrtVbr_Type = Integer32
_PnniIfConfig_IfAdmWeightNrtVbr_Object = MibScalar
pnniIfConfig_IfAdmWeightNrtVbr = _PnniIfConfig_IfAdmWeightNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 14),
    _PnniIfConfig_IfAdmWeightNrtVbr_Type()
)
pnniIfConfig_IfAdmWeightNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAdmWeightNrtVbr.setStatus("mandatory")
_PnniIfConfig_IfAdmWeightAbr_Type = Integer32
_PnniIfConfig_IfAdmWeightAbr_Object = MibScalar
pnniIfConfig_IfAdmWeightAbr = _PnniIfConfig_IfAdmWeightAbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 15),
    _PnniIfConfig_IfAdmWeightAbr_Type()
)
pnniIfConfig_IfAdmWeightAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAdmWeightAbr.setStatus("mandatory")
_PnniIfConfig_IfAdmWeightUbr_Type = Integer32
_PnniIfConfig_IfAdmWeightUbr_Object = MibScalar
pnniIfConfig_IfAdmWeightUbr = _PnniIfConfig_IfAdmWeightUbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 16),
    _PnniIfConfig_IfAdmWeightUbr_Type()
)
pnniIfConfig_IfAdmWeightUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfAdmWeightUbr.setStatus("mandatory")


class _PnniIfConfig_IfRccServiceCategory_Type(Integer32):
    """Custom type pnniIfConfig_IfRccServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abr", 6),
          ("cbr", 3),
          ("nrtVbr", 5),
          ("other", 2),
          ("rtVbr", 4),
          ("ubr", 7))
    )


_PnniIfConfig_IfRccServiceCategory_Type.__name__ = "Integer32"
_PnniIfConfig_IfRccServiceCategory_Object = MibScalar
pnniIfConfig_IfRccServiceCategory = _PnniIfConfig_IfRccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 17),
    _PnniIfConfig_IfRccServiceCategory_Type()
)
pnniIfConfig_IfRccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfRccServiceCategory.setStatus("mandatory")
_PnniIfConfig_IfRccQosName_Type = DisplayString
_PnniIfConfig_IfRccQosName_Object = MibScalar
pnniIfConfig_IfRccQosName = _PnniIfConfig_IfRccQosName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 18),
    _PnniIfConfig_IfRccQosName_Type()
)
pnniIfConfig_IfRccQosName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_IfRccQosName.setStatus("mandatory")


class _PnniIfConfig_Action_o_Type(Integer32):
    """Custom type pnniIfConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniIfConfig_Action_o_Type.__name__ = "Integer32"
_PnniIfConfig_Action_o_Object = MibScalar
pnniIfConfig_Action_o = _PnniIfConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 45, 1, 1, 19),
    _PnniIfConfig_Action_o_Type()
)
pnniIfConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfConfig_Action_o.setStatus("mandatory")
_MibpnniMetricsConfig_ObjectIdentity = ObjectIdentity
mibpnniMetricsConfig = _MibpnniMetricsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 46)
)
_MibpnniMetricsConfigTable_Object = MibTable
mibpnniMetricsConfigTable = _MibpnniMetricsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1)
)
if mibBuilder.loadTexts:
    mibpnniMetricsConfigTable.setStatus("mandatory")
_MibpnniMetricsConfigEntry_Object = MibTableRow
mibpnniMetricsConfigEntry = _MibpnniMetricsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1)
)
mibpnniMetricsConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniMetricsConfig-MetricsIndex-NodeIndex"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniMetricsConfig-MetricsIndex-MetricsTag"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniMetricsConfig-MetricsIndex-MetricsDirection"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniMetricsConfig-MetricsIndex-MetricsIndex"),
)
if mibBuilder.loadTexts:
    mibpnniMetricsConfigEntry.setStatus("mandatory")
_PnniMetricsConfig_MetricsIndex_NodeIndex_Type = Integer32
_PnniMetricsConfig_MetricsIndex_NodeIndex_Object = MibScalar
pnniMetricsConfig_MetricsIndex_NodeIndex = _PnniMetricsConfig_MetricsIndex_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 1),
    _PnniMetricsConfig_MetricsIndex_NodeIndex_Type()
)
pnniMetricsConfig_MetricsIndex_NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsIndex_NodeIndex.setStatus("mandatory")
_PnniMetricsConfig_MetricsIndex_MetricsTag_Type = Integer32
_PnniMetricsConfig_MetricsIndex_MetricsTag_Object = MibScalar
pnniMetricsConfig_MetricsIndex_MetricsTag = _PnniMetricsConfig_MetricsIndex_MetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 2),
    _PnniMetricsConfig_MetricsIndex_MetricsTag_Type()
)
pnniMetricsConfig_MetricsIndex_MetricsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsIndex_MetricsTag.setStatus("mandatory")
_PnniMetricsConfig_MetricsIndex_MetricsDirection_Type = Integer32
_PnniMetricsConfig_MetricsIndex_MetricsDirection_Object = MibScalar
pnniMetricsConfig_MetricsIndex_MetricsDirection = _PnniMetricsConfig_MetricsIndex_MetricsDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 3),
    _PnniMetricsConfig_MetricsIndex_MetricsDirection_Type()
)
pnniMetricsConfig_MetricsIndex_MetricsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsIndex_MetricsDirection.setStatus("mandatory")
_PnniMetricsConfig_MetricsIndex_MetricsIndex_Type = Integer32
_PnniMetricsConfig_MetricsIndex_MetricsIndex_Object = MibScalar
pnniMetricsConfig_MetricsIndex_MetricsIndex = _PnniMetricsConfig_MetricsIndex_MetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 4),
    _PnniMetricsConfig_MetricsIndex_MetricsIndex_Type()
)
pnniMetricsConfig_MetricsIndex_MetricsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsIndex_MetricsIndex.setStatus("mandatory")
_PnniMetricsConfig_MetricsClasses_Type = Integer32
_PnniMetricsConfig_MetricsClasses_Object = MibScalar
pnniMetricsConfig_MetricsClasses = _PnniMetricsConfig_MetricsClasses_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 5),
    _PnniMetricsConfig_MetricsClasses_Type()
)
pnniMetricsConfig_MetricsClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsClasses.setStatus("mandatory")


class _PnniMetricsConfig_MetricsGcacClp_Type(Integer32):
    """Custom type pnniMetricsConfig_MetricsGcacClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clpequal0", 2),
          ("clpequal0or1", 3))
    )


_PnniMetricsConfig_MetricsGcacClp_Type.__name__ = "Integer32"
_PnniMetricsConfig_MetricsGcacClp_Object = MibScalar
pnniMetricsConfig_MetricsGcacClp = _PnniMetricsConfig_MetricsGcacClp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 6),
    _PnniMetricsConfig_MetricsGcacClp_Type()
)
pnniMetricsConfig_MetricsGcacClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsGcacClp.setStatus("mandatory")
_PnniMetricsConfig_MetricsAdminWeight_Type = Integer32
_PnniMetricsConfig_MetricsAdminWeight_Object = MibScalar
pnniMetricsConfig_MetricsAdminWeight = _PnniMetricsConfig_MetricsAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 7),
    _PnniMetricsConfig_MetricsAdminWeight_Type()
)
pnniMetricsConfig_MetricsAdminWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_MetricsAdminWeight.setStatus("mandatory")
_PnniMetricsConfig_Metrics1_Type = Integer32
_PnniMetricsConfig_Metrics1_Object = MibScalar
pnniMetricsConfig_Metrics1 = _PnniMetricsConfig_Metrics1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 8),
    _PnniMetricsConfig_Metrics1_Type()
)
pnniMetricsConfig_Metrics1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics1.setStatus("mandatory")
_PnniMetricsConfig_Metrics2_Type = Integer32
_PnniMetricsConfig_Metrics2_Object = MibScalar
pnniMetricsConfig_Metrics2 = _PnniMetricsConfig_Metrics2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 9),
    _PnniMetricsConfig_Metrics2_Type()
)
pnniMetricsConfig_Metrics2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics2.setStatus("mandatory")
_PnniMetricsConfig_Metrics3_Type = Integer32
_PnniMetricsConfig_Metrics3_Object = MibScalar
pnniMetricsConfig_Metrics3 = _PnniMetricsConfig_Metrics3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 10),
    _PnniMetricsConfig_Metrics3_Type()
)
pnniMetricsConfig_Metrics3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics3.setStatus("mandatory")
_PnniMetricsConfig_Metrics4_Type = Integer32
_PnniMetricsConfig_Metrics4_Object = MibScalar
pnniMetricsConfig_Metrics4 = _PnniMetricsConfig_Metrics4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 11),
    _PnniMetricsConfig_Metrics4_Type()
)
pnniMetricsConfig_Metrics4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics4.setStatus("mandatory")
_PnniMetricsConfig_Metrics5_Type = Integer32
_PnniMetricsConfig_Metrics5_Object = MibScalar
pnniMetricsConfig_Metrics5 = _PnniMetricsConfig_Metrics5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 12),
    _PnniMetricsConfig_Metrics5_Type()
)
pnniMetricsConfig_Metrics5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics5.setStatus("mandatory")
_PnniMetricsConfig_Metrics6_Type = Integer32
_PnniMetricsConfig_Metrics6_Object = MibScalar
pnniMetricsConfig_Metrics6 = _PnniMetricsConfig_Metrics6_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 13),
    _PnniMetricsConfig_Metrics6_Type()
)
pnniMetricsConfig_Metrics6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics6.setStatus("mandatory")
_PnniMetricsConfig_Metrics7_Type = Integer32
_PnniMetricsConfig_Metrics7_Object = MibScalar
pnniMetricsConfig_Metrics7 = _PnniMetricsConfig_Metrics7_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 14),
    _PnniMetricsConfig_Metrics7_Type()
)
pnniMetricsConfig_Metrics7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics7.setStatus("mandatory")
_PnniMetricsConfig_Metrics8_Type = Integer32
_PnniMetricsConfig_Metrics8_Object = MibScalar
pnniMetricsConfig_Metrics8 = _PnniMetricsConfig_Metrics8_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 15),
    _PnniMetricsConfig_Metrics8_Type()
)
pnniMetricsConfig_Metrics8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Metrics8.setStatus("mandatory")


class _PnniMetricsConfig_Active_Type(Integer32):
    """Custom type pnniMetricsConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniMetricsConfig_Active_Type.__name__ = "Integer32"
_PnniMetricsConfig_Active_Object = MibScalar
pnniMetricsConfig_Active = _PnniMetricsConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 16),
    _PnniMetricsConfig_Active_Type()
)
pnniMetricsConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Active.setStatus("mandatory")


class _PnniMetricsConfig_Action_o_Type(Integer32):
    """Custom type pnniMetricsConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniMetricsConfig_Action_o_Type.__name__ = "Integer32"
_PnniMetricsConfig_Action_o_Object = MibScalar
pnniMetricsConfig_Action_o = _PnniMetricsConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 46, 1, 1, 17),
    _PnniMetricsConfig_Action_o_Type()
)
pnniMetricsConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMetricsConfig_Action_o.setStatus("mandatory")
_MibpnniRouteNodeConfig_ObjectIdentity = ObjectIdentity
mibpnniRouteNodeConfig = _MibpnniRouteNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 47)
)
_MibpnniRouteNodeConfigTable_Object = MibTable
mibpnniRouteNodeConfigTable = _MibpnniRouteNodeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1)
)
if mibBuilder.loadTexts:
    mibpnniRouteNodeConfigTable.setStatus("mandatory")
_MibpnniRouteNodeConfigEntry_Object = MibTableRow
mibpnniRouteNodeConfigEntry = _MibpnniRouteNodeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1)
)
mibpnniRouteNodeConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteNodeConfig-Index-NodeIndex"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteNodeConfig-Index-RouteNodeClass"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteNodeConfig-Index-RouteNodeDestNodeId"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteNodeConfig-Index-RouteNodeDtl"),
)
if mibBuilder.loadTexts:
    mibpnniRouteNodeConfigEntry.setStatus("mandatory")
_PnniRouteNodeConfig_Index_NodeIndex_Type = Integer32
_PnniRouteNodeConfig_Index_NodeIndex_Object = MibScalar
pnniRouteNodeConfig_Index_NodeIndex = _PnniRouteNodeConfig_Index_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 1),
    _PnniRouteNodeConfig_Index_NodeIndex_Type()
)
pnniRouteNodeConfig_Index_NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Index_NodeIndex.setStatus("mandatory")
_PnniRouteNodeConfig_Index_RouteNodeClass_Type = Integer32
_PnniRouteNodeConfig_Index_RouteNodeClass_Object = MibScalar
pnniRouteNodeConfig_Index_RouteNodeClass = _PnniRouteNodeConfig_Index_RouteNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 2),
    _PnniRouteNodeConfig_Index_RouteNodeClass_Type()
)
pnniRouteNodeConfig_Index_RouteNodeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Index_RouteNodeClass.setStatus("mandatory")
_PnniRouteNodeConfig_Index_RouteNodeDestNodeId_Type = DisplayString
_PnniRouteNodeConfig_Index_RouteNodeDestNodeId_Object = MibScalar
pnniRouteNodeConfig_Index_RouteNodeDestNodeId = _PnniRouteNodeConfig_Index_RouteNodeDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 3),
    _PnniRouteNodeConfig_Index_RouteNodeDestNodeId_Type()
)
pnniRouteNodeConfig_Index_RouteNodeDestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Index_RouteNodeDestNodeId.setStatus("mandatory")
_PnniRouteNodeConfig_Index_RouteNodeDtl_Type = Integer32
_PnniRouteNodeConfig_Index_RouteNodeDtl_Object = MibScalar
pnniRouteNodeConfig_Index_RouteNodeDtl = _PnniRouteNodeConfig_Index_RouteNodeDtl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 4),
    _PnniRouteNodeConfig_Index_RouteNodeDtl_Type()
)
pnniRouteNodeConfig_Index_RouteNodeDtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Index_RouteNodeDtl.setStatus("mandatory")
_PnniRouteNodeConfig_DestPortId_Type = Integer32
_PnniRouteNodeConfig_DestPortId_Object = MibScalar
pnniRouteNodeConfig_DestPortId = _PnniRouteNodeConfig_DestPortId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 5),
    _PnniRouteNodeConfig_DestPortId_Type()
)
pnniRouteNodeConfig_DestPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_DestPortId.setStatus("mandatory")


class _PnniRouteNodeConfig_Proto_Type(Integer32):
    """Custom type pnniRouteNodeConfig_Proto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("mgmt", 4),
          ("other", 2),
          ("pnni", 5))
    )


_PnniRouteNodeConfig_Proto_Type.__name__ = "Integer32"
_PnniRouteNodeConfig_Proto_Object = MibScalar
pnniRouteNodeConfig_Proto = _PnniRouteNodeConfig_Proto_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 6),
    _PnniRouteNodeConfig_Proto_Type()
)
pnniRouteNodeConfig_Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Proto.setStatus("mandatory")
_PnniRouteNodeConfig_TimeStamp_Type = Integer32
_PnniRouteNodeConfig_TimeStamp_Object = MibScalar
pnniRouteNodeConfig_TimeStamp = _PnniRouteNodeConfig_TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 7),
    _PnniRouteNodeConfig_TimeStamp_Type()
)
pnniRouteNodeConfig_TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_TimeStamp.setStatus("mandatory")
_PnniRouteNodeConfig_NodeInfo_Type = DisplayString
_PnniRouteNodeConfig_NodeInfo_Object = MibScalar
pnniRouteNodeConfig_NodeInfo = _PnniRouteNodeConfig_NodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 8),
    _PnniRouteNodeConfig_NodeInfo_Type()
)
pnniRouteNodeConfig_NodeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_NodeInfo.setStatus("mandatory")


class _PnniRouteNodeConfig_GcacClp_Type(Integer32):
    """Custom type pnniRouteNodeConfig_GcacClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clpequal0", 2),
          ("clpequal0or1", 3))
    )


_PnniRouteNodeConfig_GcacClp_Type.__name__ = "Integer32"
_PnniRouteNodeConfig_GcacClp_Object = MibScalar
pnniRouteNodeConfig_GcacClp = _PnniRouteNodeConfig_GcacClp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 9),
    _PnniRouteNodeConfig_GcacClp_Type()
)
pnniRouteNodeConfig_GcacClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_GcacClp.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetricAw_Type = Integer32
_PnniRouteNodeConfig_FwdMetricAw_Object = MibScalar
pnniRouteNodeConfig_FwdMetricAw = _PnniRouteNodeConfig_FwdMetricAw_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 10),
    _PnniRouteNodeConfig_FwdMetricAw_Type()
)
pnniRouteNodeConfig_FwdMetricAw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetricAw.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetric1_Type = Integer32
_PnniRouteNodeConfig_FwdMetric1_Object = MibScalar
pnniRouteNodeConfig_FwdMetric1 = _PnniRouteNodeConfig_FwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 11),
    _PnniRouteNodeConfig_FwdMetric1_Type()
)
pnniRouteNodeConfig_FwdMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetric1.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetric2_Type = Integer32
_PnniRouteNodeConfig_FwdMetric2_Object = MibScalar
pnniRouteNodeConfig_FwdMetric2 = _PnniRouteNodeConfig_FwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 12),
    _PnniRouteNodeConfig_FwdMetric2_Type()
)
pnniRouteNodeConfig_FwdMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetric2.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetric3_Type = Integer32
_PnniRouteNodeConfig_FwdMetric3_Object = MibScalar
pnniRouteNodeConfig_FwdMetric3 = _PnniRouteNodeConfig_FwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 13),
    _PnniRouteNodeConfig_FwdMetric3_Type()
)
pnniRouteNodeConfig_FwdMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetric3.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetric4_Type = Integer32
_PnniRouteNodeConfig_FwdMetric4_Object = MibScalar
pnniRouteNodeConfig_FwdMetric4 = _PnniRouteNodeConfig_FwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 14),
    _PnniRouteNodeConfig_FwdMetric4_Type()
)
pnniRouteNodeConfig_FwdMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetric4.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMetric5_Type = Integer32
_PnniRouteNodeConfig_FwdMetric5_Object = MibScalar
pnniRouteNodeConfig_FwdMetric5 = _PnniRouteNodeConfig_FwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 15),
    _PnniRouteNodeConfig_FwdMetric5_Type()
)
pnniRouteNodeConfig_FwdMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMetric5.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMeteric6_Type = Integer32
_PnniRouteNodeConfig_FwdMeteric6_Object = MibScalar
pnniRouteNodeConfig_FwdMeteric6 = _PnniRouteNodeConfig_FwdMeteric6_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 16),
    _PnniRouteNodeConfig_FwdMeteric6_Type()
)
pnniRouteNodeConfig_FwdMeteric6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMeteric6.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMeteric7_Type = Integer32
_PnniRouteNodeConfig_FwdMeteric7_Object = MibScalar
pnniRouteNodeConfig_FwdMeteric7 = _PnniRouteNodeConfig_FwdMeteric7_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 17),
    _PnniRouteNodeConfig_FwdMeteric7_Type()
)
pnniRouteNodeConfig_FwdMeteric7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMeteric7.setStatus("mandatory")
_PnniRouteNodeConfig_FwdMeteric8_Type = Integer32
_PnniRouteNodeConfig_FwdMeteric8_Object = MibScalar
pnniRouteNodeConfig_FwdMeteric8 = _PnniRouteNodeConfig_FwdMeteric8_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 18),
    _PnniRouteNodeConfig_FwdMeteric8_Type()
)
pnniRouteNodeConfig_FwdMeteric8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_FwdMeteric8.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetricAw_Type = Integer32
_PnniRouteNodeConfig_BwdMetricAw_Object = MibScalar
pnniRouteNodeConfig_BwdMetricAw = _PnniRouteNodeConfig_BwdMetricAw_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 19),
    _PnniRouteNodeConfig_BwdMetricAw_Type()
)
pnniRouteNodeConfig_BwdMetricAw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetricAw.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric1_Type = Integer32
_PnniRouteNodeConfig_BwdMetric1_Object = MibScalar
pnniRouteNodeConfig_BwdMetric1 = _PnniRouteNodeConfig_BwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 20),
    _PnniRouteNodeConfig_BwdMetric1_Type()
)
pnniRouteNodeConfig_BwdMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric1.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric2_Type = Integer32
_PnniRouteNodeConfig_BwdMetric2_Object = MibScalar
pnniRouteNodeConfig_BwdMetric2 = _PnniRouteNodeConfig_BwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 21),
    _PnniRouteNodeConfig_BwdMetric2_Type()
)
pnniRouteNodeConfig_BwdMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric2.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric3_Type = Integer32
_PnniRouteNodeConfig_BwdMetric3_Object = MibScalar
pnniRouteNodeConfig_BwdMetric3 = _PnniRouteNodeConfig_BwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 22),
    _PnniRouteNodeConfig_BwdMetric3_Type()
)
pnniRouteNodeConfig_BwdMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric3.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric4_Type = Integer32
_PnniRouteNodeConfig_BwdMetric4_Object = MibScalar
pnniRouteNodeConfig_BwdMetric4 = _PnniRouteNodeConfig_BwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 23),
    _PnniRouteNodeConfig_BwdMetric4_Type()
)
pnniRouteNodeConfig_BwdMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric4.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric5_Type = Integer32
_PnniRouteNodeConfig_BwdMetric5_Object = MibScalar
pnniRouteNodeConfig_BwdMetric5 = _PnniRouteNodeConfig_BwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 24),
    _PnniRouteNodeConfig_BwdMetric5_Type()
)
pnniRouteNodeConfig_BwdMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric5.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric6_Type = Integer32
_PnniRouteNodeConfig_BwdMetric6_Object = MibScalar
pnniRouteNodeConfig_BwdMetric6 = _PnniRouteNodeConfig_BwdMetric6_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 25),
    _PnniRouteNodeConfig_BwdMetric6_Type()
)
pnniRouteNodeConfig_BwdMetric6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric6.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric7_Type = Integer32
_PnniRouteNodeConfig_BwdMetric7_Object = MibScalar
pnniRouteNodeConfig_BwdMetric7 = _PnniRouteNodeConfig_BwdMetric7_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 26),
    _PnniRouteNodeConfig_BwdMetric7_Type()
)
pnniRouteNodeConfig_BwdMetric7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric7.setStatus("mandatory")
_PnniRouteNodeConfig_BwdMetric8_Type = Integer32
_PnniRouteNodeConfig_BwdMetric8_Object = MibScalar
pnniRouteNodeConfig_BwdMetric8 = _PnniRouteNodeConfig_BwdMetric8_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 27),
    _PnniRouteNodeConfig_BwdMetric8_Type()
)
pnniRouteNodeConfig_BwdMetric8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_BwdMetric8.setStatus("mandatory")


class _PnniRouteNodeConfig_VpCapability_Type(Integer32):
    """Custom type pnniRouteNodeConfig_VpCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniRouteNodeConfig_VpCapability_Type.__name__ = "Integer32"
_PnniRouteNodeConfig_VpCapability_Object = MibScalar
pnniRouteNodeConfig_VpCapability = _PnniRouteNodeConfig_VpCapability_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 28),
    _PnniRouteNodeConfig_VpCapability_Type()
)
pnniRouteNodeConfig_VpCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_VpCapability.setStatus("mandatory")


class _PnniRouteNodeConfig_Active_Type(Integer32):
    """Custom type pnniRouteNodeConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniRouteNodeConfig_Active_Type.__name__ = "Integer32"
_PnniRouteNodeConfig_Active_Object = MibScalar
pnniRouteNodeConfig_Active = _PnniRouteNodeConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 29),
    _PnniRouteNodeConfig_Active_Type()
)
pnniRouteNodeConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Active.setStatus("mandatory")


class _PnniRouteNodeConfig_Action_o_Type(Integer32):
    """Custom type pnniRouteNodeConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniRouteNodeConfig_Action_o_Type.__name__ = "Integer32"
_PnniRouteNodeConfig_Action_o_Object = MibScalar
pnniRouteNodeConfig_Action_o = _PnniRouteNodeConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 47, 1, 1, 30),
    _PnniRouteNodeConfig_Action_o_Type()
)
pnniRouteNodeConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteNodeConfig_Action_o.setStatus("mandatory")
_MibpnniDTLConfig_ObjectIdentity = ObjectIdentity
mibpnniDTLConfig = _MibpnniDTLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 48)
)
_MibpnniDTLConfigTable_Object = MibTable
mibpnniDTLConfigTable = _MibpnniDTLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1)
)
if mibBuilder.loadTexts:
    mibpnniDTLConfigTable.setStatus("mandatory")
_MibpnniDTLConfigEntry_Object = MibTableRow
mibpnniDTLConfigEntry = _MibpnniDTLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1)
)
mibpnniDTLConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniDTLConfig-DtlIndex-NodeIndex"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniDTLConfig-DtlIndex-DtlIndex"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniDTLConfig-DtlIndex-DtlEntryIndex"),
)
if mibBuilder.loadTexts:
    mibpnniDTLConfigEntry.setStatus("mandatory")
_PnniDTLConfig_DtlIndex_NodeIndex_Type = Integer32
_PnniDTLConfig_DtlIndex_NodeIndex_Object = MibScalar
pnniDTLConfig_DtlIndex_NodeIndex = _PnniDTLConfig_DtlIndex_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 1),
    _PnniDTLConfig_DtlIndex_NodeIndex_Type()
)
pnniDTLConfig_DtlIndex_NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlIndex_NodeIndex.setStatus("mandatory")
_PnniDTLConfig_DtlIndex_DtlIndex_Type = Integer32
_PnniDTLConfig_DtlIndex_DtlIndex_Object = MibScalar
pnniDTLConfig_DtlIndex_DtlIndex = _PnniDTLConfig_DtlIndex_DtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 2),
    _PnniDTLConfig_DtlIndex_DtlIndex_Type()
)
pnniDTLConfig_DtlIndex_DtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlIndex_DtlIndex.setStatus("mandatory")
_PnniDTLConfig_DtlIndex_DtlEntryIndex_Type = Integer32
_PnniDTLConfig_DtlIndex_DtlEntryIndex_Object = MibScalar
pnniDTLConfig_DtlIndex_DtlEntryIndex = _PnniDTLConfig_DtlIndex_DtlEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 3),
    _PnniDTLConfig_DtlIndex_DtlEntryIndex_Type()
)
pnniDTLConfig_DtlIndex_DtlEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlIndex_DtlEntryIndex.setStatus("mandatory")
_PnniDTLConfig_DtlNodeId_Type = DisplayString
_PnniDTLConfig_DtlNodeId_Object = MibScalar
pnniDTLConfig_DtlNodeId = _PnniDTLConfig_DtlNodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 4),
    _PnniDTLConfig_DtlNodeId_Type()
)
pnniDTLConfig_DtlNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlNodeId.setStatus("mandatory")
_PnniDTLConfig_DtlPortId_Type = Integer32
_PnniDTLConfig_DtlPortId_Object = MibScalar
pnniDTLConfig_DtlPortId = _PnniDTLConfig_DtlPortId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 5),
    _PnniDTLConfig_DtlPortId_Type()
)
pnniDTLConfig_DtlPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlPortId.setStatus("mandatory")


class _PnniDTLConfig_DtlLinkType_Type(Integer32):
    """Custom type pnniDTLConfig_DtlLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 3),
          ("invalid", 2),
          ("last", 5),
          ("uplink", 4))
    )


_PnniDTLConfig_DtlLinkType_Type.__name__ = "Integer32"
_PnniDTLConfig_DtlLinkType_Object = MibScalar
pnniDTLConfig_DtlLinkType = _PnniDTLConfig_DtlLinkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 6),
    _PnniDTLConfig_DtlLinkType_Type()
)
pnniDTLConfig_DtlLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDTLConfig_DtlLinkType.setStatus("mandatory")


class _PnniDTLConfig_Active_Type(Integer32):
    """Custom type pnniDTLConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniDTLConfig_Active_Type.__name__ = "Integer32"
_PnniDTLConfig_Active_Object = MibScalar
pnniDTLConfig_Active = _PnniDTLConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 7),
    _PnniDTLConfig_Active_Type()
)
pnniDTLConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDTLConfig_Active.setStatus("mandatory")


class _PnniDTLConfig_Action_o_Type(Integer32):
    """Custom type pnniDTLConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniDTLConfig_Action_o_Type.__name__ = "Integer32"
_PnniDTLConfig_Action_o_Object = MibScalar
pnniDTLConfig_Action_o = _PnniDTLConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 48, 1, 1, 8),
    _PnniDTLConfig_Action_o_Type()
)
pnniDTLConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDTLConfig_Action_o.setStatus("mandatory")
_MibpnniRouteAddrConfig_ObjectIdentity = ObjectIdentity
mibpnniRouteAddrConfig = _MibpnniRouteAddrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 49)
)
_MibpnniRouteAddrConfigTable_Object = MibTable
mibpnniRouteAddrConfigTable = _MibpnniRouteAddrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1)
)
if mibBuilder.loadTexts:
    mibpnniRouteAddrConfigTable.setStatus("mandatory")
_MibpnniRouteAddrConfigEntry_Object = MibTableRow
mibpnniRouteAddrConfigEntry = _MibpnniRouteAddrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1)
)
mibpnniRouteAddrConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteAddrConfig-Name"),
)
if mibBuilder.loadTexts:
    mibpnniRouteAddrConfigEntry.setStatus("mandatory")
_PnniRouteAddrConfig_Name_Type = DisplayString
_PnniRouteAddrConfig_Name_Object = MibScalar
pnniRouteAddrConfig_Name = _PnniRouteAddrConfig_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 1),
    _PnniRouteAddrConfig_Name_Type()
)
pnniRouteAddrConfig_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Name.setStatus("mandatory")
_PnniRouteAddrConfig_AddrIndex_NodeIndex_Type = Integer32
_PnniRouteAddrConfig_AddrIndex_NodeIndex_Object = MibScalar
pnniRouteAddrConfig_AddrIndex_NodeIndex = _PnniRouteAddrConfig_AddrIndex_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 2),
    _PnniRouteAddrConfig_AddrIndex_NodeIndex_Type()
)
pnniRouteAddrConfig_AddrIndex_NodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AddrIndex_NodeIndex.setStatus("mandatory")
_PnniRouteAddrConfig_AddrIndex_Address_Type = DisplayString
_PnniRouteAddrConfig_AddrIndex_Address_Object = MibScalar
pnniRouteAddrConfig_AddrIndex_Address = _PnniRouteAddrConfig_AddrIndex_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 3),
    _PnniRouteAddrConfig_AddrIndex_Address_Type()
)
pnniRouteAddrConfig_AddrIndex_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AddrIndex_Address.setStatus("mandatory")
_PnniRouteAddrConfig_AddrIndex_PrefixLen_Type = Integer32
_PnniRouteAddrConfig_AddrIndex_PrefixLen_Object = MibScalar
pnniRouteAddrConfig_AddrIndex_PrefixLen = _PnniRouteAddrConfig_AddrIndex_PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 4),
    _PnniRouteAddrConfig_AddrIndex_PrefixLen_Type()
)
pnniRouteAddrConfig_AddrIndex_PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AddrIndex_PrefixLen.setStatus("mandatory")
_PnniRouteAddrConfig_AddrIndex_Index_Type = Integer32
_PnniRouteAddrConfig_AddrIndex_Index_Object = MibScalar
pnniRouteAddrConfig_AddrIndex_Index = _PnniRouteAddrConfig_AddrIndex_Index_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 5),
    _PnniRouteAddrConfig_AddrIndex_Index_Type()
)
pnniRouteAddrConfig_AddrIndex_Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AddrIndex_Index.setStatus("mandatory")
_PnniRouteAddrConfig_IfIndex_Type = Integer32
_PnniRouteAddrConfig_IfIndex_Object = MibScalar
pnniRouteAddrConfig_IfIndex = _PnniRouteAddrConfig_IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 6),
    _PnniRouteAddrConfig_IfIndex_Type()
)
pnniRouteAddrConfig_IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_IfIndex.setStatus("mandatory")
_PnniRouteAddrConfig_AdvNodeId_Type = DisplayString
_PnniRouteAddrConfig_AdvNodeId_Object = MibScalar
pnniRouteAddrConfig_AdvNodeId = _PnniRouteAddrConfig_AdvNodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 7),
    _PnniRouteAddrConfig_AdvNodeId_Type()
)
pnniRouteAddrConfig_AdvNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AdvNodeId.setStatus("mandatory")
_PnniRouteAddrConfig_AdvPortId_Type = Integer32
_PnniRouteAddrConfig_AdvPortId_Object = MibScalar
pnniRouteAddrConfig_AdvPortId = _PnniRouteAddrConfig_AdvPortId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 8),
    _PnniRouteAddrConfig_AdvPortId_Type()
)
pnniRouteAddrConfig_AdvPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_AdvPortId.setStatus("mandatory")


class _PnniRouteAddrConfig_Type_Type(Integer32):
    """Custom type pnniRouteAddrConfig_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 5),
          ("internal", 4),
          ("other", 2),
          ("reject", 3))
    )


_PnniRouteAddrConfig_Type_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_Type_Object = MibScalar
pnniRouteAddrConfig_Type = _PnniRouteAddrConfig_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 9),
    _PnniRouteAddrConfig_Type_Type()
)
pnniRouteAddrConfig_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Type.setStatus("mandatory")


class _PnniRouteAddrConfig_Proto_Type(Integer32):
    """Custom type pnniRouteAddrConfig_Proto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("mgmt", 4),
          ("other", 2),
          ("pnni", 5))
    )


_PnniRouteAddrConfig_Proto_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_Proto_Object = MibScalar
pnniRouteAddrConfig_Proto = _PnniRouteAddrConfig_Proto_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 10),
    _PnniRouteAddrConfig_Proto_Type()
)
pnniRouteAddrConfig_Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Proto.setStatus("mandatory")
_PnniRouteAddrConfig_PnniScope_Type = Integer32
_PnniRouteAddrConfig_PnniScope_Object = MibScalar
pnniRouteAddrConfig_PnniScope = _PnniRouteAddrConfig_PnniScope_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 11),
    _PnniRouteAddrConfig_PnniScope_Type()
)
pnniRouteAddrConfig_PnniScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_PnniScope.setStatus("mandatory")


class _PnniRouteAddrConfig_VpCapability_Type(Integer32):
    """Custom type pnniRouteAddrConfig_VpCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniRouteAddrConfig_VpCapability_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_VpCapability_Object = MibScalar
pnniRouteAddrConfig_VpCapability = _PnniRouteAddrConfig_VpCapability_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 12),
    _PnniRouteAddrConfig_VpCapability_Type()
)
pnniRouteAddrConfig_VpCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_VpCapability.setStatus("mandatory")
_PnniRouteAddrConfig_MetricsTag_Type = Integer32
_PnniRouteAddrConfig_MetricsTag_Object = MibScalar
pnniRouteAddrConfig_MetricsTag = _PnniRouteAddrConfig_MetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 13),
    _PnniRouteAddrConfig_MetricsTag_Type()
)
pnniRouteAddrConfig_MetricsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_MetricsTag.setStatus("mandatory")
_PnniRouteAddrConfig_PtseIdPtseId_Type = Integer32
_PnniRouteAddrConfig_PtseIdPtseId_Object = MibScalar
pnniRouteAddrConfig_PtseIdPtseId = _PnniRouteAddrConfig_PtseIdPtseId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 14),
    _PnniRouteAddrConfig_PtseIdPtseId_Type()
)
pnniRouteAddrConfig_PtseIdPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_PtseIdPtseId.setStatus("mandatory")


class _PnniRouteAddrConfig_OriginateAdvert_Type(Integer32):
    """Custom type pnniRouteAddrConfig_OriginateAdvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniRouteAddrConfig_OriginateAdvert_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_OriginateAdvert_Object = MibScalar
pnniRouteAddrConfig_OriginateAdvert = _PnniRouteAddrConfig_OriginateAdvert_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 15),
    _PnniRouteAddrConfig_OriginateAdvert_Type()
)
pnniRouteAddrConfig_OriginateAdvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_OriginateAdvert.setStatus("mandatory")
_PnniRouteAddrConfig_Info_Type = DisplayString
_PnniRouteAddrConfig_Info_Object = MibScalar
pnniRouteAddrConfig_Info = _PnniRouteAddrConfig_Info_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 16),
    _PnniRouteAddrConfig_Info_Type()
)
pnniRouteAddrConfig_Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Info.setStatus("mandatory")


class _PnniRouteAddrConfig_OperStatus_Type(Integer32):
    """Custom type pnniRouteAddrConfig_OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("advertised", 4),
          ("inactive", 2))
    )


_PnniRouteAddrConfig_OperStatus_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_OperStatus_Object = MibScalar
pnniRouteAddrConfig_OperStatus = _PnniRouteAddrConfig_OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 17),
    _PnniRouteAddrConfig_OperStatus_Type()
)
pnniRouteAddrConfig_OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_OperStatus.setStatus("mandatory")
_PnniRouteAddrConfig_TimeStamp_Type = Integer32
_PnniRouteAddrConfig_TimeStamp_Object = MibScalar
pnniRouteAddrConfig_TimeStamp = _PnniRouteAddrConfig_TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 18),
    _PnniRouteAddrConfig_TimeStamp_Type()
)
pnniRouteAddrConfig_TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_TimeStamp.setStatus("mandatory")


class _PnniRouteAddrConfig_Active_Type(Integer32):
    """Custom type pnniRouteAddrConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniRouteAddrConfig_Active_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_Active_Object = MibScalar
pnniRouteAddrConfig_Active = _PnniRouteAddrConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 19),
    _PnniRouteAddrConfig_Active_Type()
)
pnniRouteAddrConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Active.setStatus("mandatory")


class _PnniRouteAddrConfig_Action_o_Type(Integer32):
    """Custom type pnniRouteAddrConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniRouteAddrConfig_Action_o_Type.__name__ = "Integer32"
_PnniRouteAddrConfig_Action_o_Object = MibScalar
pnniRouteAddrConfig_Action_o = _PnniRouteAddrConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 49, 1, 1, 20),
    _PnniRouteAddrConfig_Action_o_Type()
)
pnniRouteAddrConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteAddrConfig_Action_o.setStatus("mandatory")
_MibpnniRouteTnsConfig_ObjectIdentity = ObjectIdentity
mibpnniRouteTnsConfig = _MibpnniRouteTnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 50)
)
_MibpnniRouteTnsConfigTable_Object = MibTable
mibpnniRouteTnsConfigTable = _MibpnniRouteTnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1)
)
if mibBuilder.loadTexts:
    mibpnniRouteTnsConfigTable.setStatus("mandatory")
_MibpnniRouteTnsConfigEntry_Object = MibTableRow
mibpnniRouteTnsConfigEntry = _MibpnniRouteTnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1)
)
mibpnniRouteTnsConfigEntry.setIndexNames(
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteTnsConfig-TnsIndex-NodeIndex"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteTnsConfig-TnsIndex-RouteTnsType"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteTnsConfig-TnsIndex-RouteTnsPlan"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteTnsConfig-TnsIndex-RouteTnsId"),
    (0, "ASCEND-MIBATMPNNI-MIB", "pnniRouteTnsConfig-TnsIndex-RouteTnsIndex"),
)
if mibBuilder.loadTexts:
    mibpnniRouteTnsConfigEntry.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIndex_NodeIndex_Type = Integer32
_PnniRouteTnsConfig_TnsIndex_NodeIndex_Object = MibScalar
pnniRouteTnsConfig_TnsIndex_NodeIndex = _PnniRouteTnsConfig_TnsIndex_NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 1),
    _PnniRouteTnsConfig_TnsIndex_NodeIndex_Type()
)
pnniRouteTnsConfig_TnsIndex_NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIndex_NodeIndex.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIndex_RouteTnsType_Type = Integer32
_PnniRouteTnsConfig_TnsIndex_RouteTnsType_Object = MibScalar
pnniRouteTnsConfig_TnsIndex_RouteTnsType = _PnniRouteTnsConfig_TnsIndex_RouteTnsType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 2),
    _PnniRouteTnsConfig_TnsIndex_RouteTnsType_Type()
)
pnniRouteTnsConfig_TnsIndex_RouteTnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIndex_RouteTnsType.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIndex_RouteTnsPlan_Type = Integer32
_PnniRouteTnsConfig_TnsIndex_RouteTnsPlan_Object = MibScalar
pnniRouteTnsConfig_TnsIndex_RouteTnsPlan = _PnniRouteTnsConfig_TnsIndex_RouteTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 3),
    _PnniRouteTnsConfig_TnsIndex_RouteTnsPlan_Type()
)
pnniRouteTnsConfig_TnsIndex_RouteTnsPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIndex_RouteTnsPlan.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIndex_RouteTnsId_Type = DisplayString
_PnniRouteTnsConfig_TnsIndex_RouteTnsId_Object = MibScalar
pnniRouteTnsConfig_TnsIndex_RouteTnsId = _PnniRouteTnsConfig_TnsIndex_RouteTnsId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 4),
    _PnniRouteTnsConfig_TnsIndex_RouteTnsId_Type()
)
pnniRouteTnsConfig_TnsIndex_RouteTnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIndex_RouteTnsId.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIndex_RouteTnsIndex_Type = Integer32
_PnniRouteTnsConfig_TnsIndex_RouteTnsIndex_Object = MibScalar
pnniRouteTnsConfig_TnsIndex_RouteTnsIndex = _PnniRouteTnsConfig_TnsIndex_RouteTnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 5),
    _PnniRouteTnsConfig_TnsIndex_RouteTnsIndex_Type()
)
pnniRouteTnsConfig_TnsIndex_RouteTnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIndex_RouteTnsIndex.setStatus("mandatory")
_PnniRouteTnsConfig_TnsIfIndex_Type = Integer32
_PnniRouteTnsConfig_TnsIfIndex_Object = MibScalar
pnniRouteTnsConfig_TnsIfIndex = _PnniRouteTnsConfig_TnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 6),
    _PnniRouteTnsConfig_TnsIfIndex_Type()
)
pnniRouteTnsConfig_TnsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsIfIndex.setStatus("mandatory")
_PnniRouteTnsConfig_TnsAdvertisingNodeId_Type = DisplayString
_PnniRouteTnsConfig_TnsAdvertisingNodeId_Object = MibScalar
pnniRouteTnsConfig_TnsAdvertisingNodeId = _PnniRouteTnsConfig_TnsAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 7),
    _PnniRouteTnsConfig_TnsAdvertisingNodeId_Type()
)
pnniRouteTnsConfig_TnsAdvertisingNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsAdvertisingNodeId.setStatus("mandatory")
_PnniRouteTnsConfig_TnsAdvertisedPortId_Type = Integer32
_PnniRouteTnsConfig_TnsAdvertisedPortId_Object = MibScalar
pnniRouteTnsConfig_TnsAdvertisedPortId = _PnniRouteTnsConfig_TnsAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 8),
    _PnniRouteTnsConfig_TnsAdvertisedPortId_Type()
)
pnniRouteTnsConfig_TnsAdvertisedPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsAdvertisedPortId.setStatus("mandatory")


class _PnniRouteTnsConfig_TnsRouteType_Type(Integer32):
    """Custom type pnniRouteTnsConfig_TnsRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 5),
          ("other", 2))
    )


_PnniRouteTnsConfig_TnsRouteType_Type.__name__ = "Integer32"
_PnniRouteTnsConfig_TnsRouteType_Object = MibScalar
pnniRouteTnsConfig_TnsRouteType = _PnniRouteTnsConfig_TnsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 9),
    _PnniRouteTnsConfig_TnsRouteType_Type()
)
pnniRouteTnsConfig_TnsRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsRouteType.setStatus("mandatory")
_PnniRouteTnsConfig_TnsPnniScope_Type = Integer32
_PnniRouteTnsConfig_TnsPnniScope_Object = MibScalar
pnniRouteTnsConfig_TnsPnniScope = _PnniRouteTnsConfig_TnsPnniScope_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 10),
    _PnniRouteTnsConfig_TnsPnniScope_Type()
)
pnniRouteTnsConfig_TnsPnniScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsPnniScope.setStatus("mandatory")


class _PnniRouteTnsConfig_TnsVpCapability_Type(Integer32):
    """Custom type pnniRouteTnsConfig_TnsVpCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniRouteTnsConfig_TnsVpCapability_Type.__name__ = "Integer32"
_PnniRouteTnsConfig_TnsVpCapability_Object = MibScalar
pnniRouteTnsConfig_TnsVpCapability = _PnniRouteTnsConfig_TnsVpCapability_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 11),
    _PnniRouteTnsConfig_TnsVpCapability_Type()
)
pnniRouteTnsConfig_TnsVpCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsVpCapability.setStatus("mandatory")
_PnniRouteTnsConfig_TnsMetricsTag_Type = Integer32
_PnniRouteTnsConfig_TnsMetricsTag_Object = MibScalar
pnniRouteTnsConfig_TnsMetricsTag = _PnniRouteTnsConfig_TnsMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 12),
    _PnniRouteTnsConfig_TnsMetricsTag_Type()
)
pnniRouteTnsConfig_TnsMetricsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsMetricsTag.setStatus("mandatory")


class _PnniRouteTnsConfig_TnsOriginateAdvertisement_Type(Integer32):
    """Custom type pnniRouteTnsConfig_TnsOriginateAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2))
    )


_PnniRouteTnsConfig_TnsOriginateAdvertisement_Type.__name__ = "Integer32"
_PnniRouteTnsConfig_TnsOriginateAdvertisement_Object = MibScalar
pnniRouteTnsConfig_TnsOriginateAdvertisement = _PnniRouteTnsConfig_TnsOriginateAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 13),
    _PnniRouteTnsConfig_TnsOriginateAdvertisement_Type()
)
pnniRouteTnsConfig_TnsOriginateAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_TnsOriginateAdvertisement.setStatus("mandatory")


class _PnniRouteTnsConfig_Active_Type(Integer32):
    """Custom type pnniRouteTnsConfig_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniRouteTnsConfig_Active_Type.__name__ = "Integer32"
_PnniRouteTnsConfig_Active_Object = MibScalar
pnniRouteTnsConfig_Active = _PnniRouteTnsConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 14),
    _PnniRouteTnsConfig_Active_Type()
)
pnniRouteTnsConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_Active.setStatus("mandatory")


class _PnniRouteTnsConfig_Action_o_Type(Integer32):
    """Custom type pnniRouteTnsConfig_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PnniRouteTnsConfig_Action_o_Type.__name__ = "Integer32"
_PnniRouteTnsConfig_Action_o_Object = MibScalar
pnniRouteTnsConfig_Action_o = _PnniRouteTnsConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 50, 1, 1, 15),
    _PnniRouteTnsConfig_Action_o_Type()
)
pnniRouteTnsConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniRouteTnsConfig_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMPNNI-MIB",
    **{"DisplayString": DisplayString,
       "mibpnniNodeConfig": mibpnniNodeConfig,
       "mibpnniNodeConfigTable": mibpnniNodeConfigTable,
       "mibpnniNodeConfigEntry": mibpnniNodeConfigEntry,
       "pnniNodeConfig-NodeIndex": pnniNodeConfig_NodeIndex,
       "pnniNodeConfig-NodeLevel": pnniNodeConfig_NodeLevel,
       "pnniNodeConfig-NodeId": pnniNodeConfig_NodeId,
       "pnniNodeConfig-CurrNodeId": pnniNodeConfig_CurrNodeId,
       "pnniNodeConfig-NodeLowest": pnniNodeConfig_NodeLowest,
       "pnniNodeConfig-NodeAdminStatus": pnniNodeConfig_NodeAdminStatus,
       "pnniNodeConfig-NodeDomainName": pnniNodeConfig_NodeDomainName,
       "pnniNodeConfig-NodeAtmAddress": pnniNodeConfig_NodeAtmAddress,
       "pnniNodeConfig-NodePeerGroupId": pnniNodeConfig_NodePeerGroupId,
       "pnniNodeConfig-CurrNodePeerGroupId": pnniNodeConfig_CurrNodePeerGroupId,
       "pnniNodeConfig-NodeRestrictedTransit": pnniNodeConfig_NodeRestrictedTransit,
       "pnniNodeConfig-NodeComplexRep": pnniNodeConfig_NodeComplexRep,
       "pnniNodeConfig-NodePgl-LeadershipPriority": pnniNodeConfig_NodePgl_LeadershipPriority,
       "pnniNodeConfig-NodePgl-ParentNodeIndex": pnniNodeConfig_NodePgl_ParentNodeIndex,
       "pnniNodeConfig-NodePgl-InitTime": pnniNodeConfig_NodePgl_InitTime,
       "pnniNodeConfig-NodePgl-OverrideDelay": pnniNodeConfig_NodePgl_OverrideDelay,
       "pnniNodeConfig-NodePgl-ReelectTime": pnniNodeConfig_NodePgl_ReelectTime,
       "pnniNodeConfig-NodeTimer-PtseHolddown": pnniNodeConfig_NodeTimer_PtseHolddown,
       "pnniNodeConfig-NodeTimer-HelloHolddown": pnniNodeConfig_NodeTimer_HelloHolddown,
       "pnniNodeConfig-NodeTimer-HelloInterval": pnniNodeConfig_NodeTimer_HelloInterval,
       "pnniNodeConfig-NodeTimer-HelloInactivityFactor": pnniNodeConfig_NodeTimer_HelloInactivityFactor,
       "pnniNodeConfig-NodeTimer-HlinkInact": pnniNodeConfig_NodeTimer_HlinkInact,
       "pnniNodeConfig-NodeTimer-PtseRefreshInterval": pnniNodeConfig_NodeTimer_PtseRefreshInterval,
       "pnniNodeConfig-NodeTimer-PtseLifetimeFactor": pnniNodeConfig_NodeTimer_PtseLifetimeFactor,
       "pnniNodeConfig-NodeTimer-RxmtInterval": pnniNodeConfig_NodeTimer_RxmtInterval,
       "pnniNodeConfig-NodeTimer-PeerDelayedAckInterval": pnniNodeConfig_NodeTimer_PeerDelayedAckInterval,
       "pnniNodeConfig-NodeTimer-AvcrPm": pnniNodeConfig_NodeTimer_AvcrPm,
       "pnniNodeConfig-NodeTimer-AvcrMt": pnniNodeConfig_NodeTimer_AvcrMt,
       "pnniNodeConfig-NodeTimer-CdvPm": pnniNodeConfig_NodeTimer_CdvPm,
       "pnniNodeConfig-NodeTimer-CtdPm": pnniNodeConfig_NodeTimer_CtdPm,
       "pnniNodeConfig-NodeSvccRcc-InitTime": pnniNodeConfig_NodeSvccRcc_InitTime,
       "pnniNodeConfig-NodeSvccRcc-RetryTime": pnniNodeConfig_NodeSvccRcc_RetryTime,
       "pnniNodeConfig-NodeSvccRcc-CallingIntegrityTime": pnniNodeConfig_NodeSvccRcc_CallingIntegrityTime,
       "pnniNodeConfig-NodeSvccRcc-CalledIntegrityTime": pnniNodeConfig_NodeSvccRcc_CalledIntegrityTime,
       "pnniNodeConfig-NodeSvccRcc-TrafficDescrIndex": pnniNodeConfig_NodeSvccRcc_TrafficDescrIndex,
       "pnniNodeConfig-NodeScopeMapping-LocalNet": pnniNodeConfig_NodeScopeMapping_LocalNet,
       "pnniNodeConfig-NodeScopeMapping-LocalNetPlus1": pnniNodeConfig_NodeScopeMapping_LocalNetPlus1,
       "pnniNodeConfig-NodeScopeMapping-LocalNetPlus2": pnniNodeConfig_NodeScopeMapping_LocalNetPlus2,
       "pnniNodeConfig-NodeScopeMapping-SiteMinus1": pnniNodeConfig_NodeScopeMapping_SiteMinus1,
       "pnniNodeConfig-NodeScopeMapping-IntraSite": pnniNodeConfig_NodeScopeMapping_IntraSite,
       "pnniNodeConfig-NodeScopeMapping-SitePlus1": pnniNodeConfig_NodeScopeMapping_SitePlus1,
       "pnniNodeConfig-NodeScopeMapping-OrganizationMinus1": pnniNodeConfig_NodeScopeMapping_OrganizationMinus1,
       "pnniNodeConfig-NodeScopeMapping-IntraOrganization": pnniNodeConfig_NodeScopeMapping_IntraOrganization,
       "pnniNodeConfig-NodeScopeMapping-OrganizationPlus1": pnniNodeConfig_NodeScopeMapping_OrganizationPlus1,
       "pnniNodeConfig-NodeScopeMapping-CommunityMinus1": pnniNodeConfig_NodeScopeMapping_CommunityMinus1,
       "pnniNodeConfig-NodeScopeMapping-IntraCommunity": pnniNodeConfig_NodeScopeMapping_IntraCommunity,
       "pnniNodeConfig-NodeScopeMapping-CommunityPlus1": pnniNodeConfig_NodeScopeMapping_CommunityPlus1,
       "pnniNodeConfig-NodeScopeMapping-Regional": pnniNodeConfig_NodeScopeMapping_Regional,
       "pnniNodeConfig-NodeScopeMapping-InterRegional": pnniNodeConfig_NodeScopeMapping_InterRegional,
       "pnniNodeConfig-NodeScopeMapping-Global": pnniNodeConfig_NodeScopeMapping_Global,
       "pnniNodeConfig-Action-o": pnniNodeConfig_Action_o,
       "mibpnniSummaryAddrEntry": mibpnniSummaryAddrEntry,
       "mibpnniSummaryAddrEntryTable": mibpnniSummaryAddrEntryTable,
       "mibpnniSummaryAddrEntryEntry": mibpnniSummaryAddrEntryEntry,
       "pnniSummaryAddrEntry-IndexName": pnniSummaryAddrEntry_IndexName,
       "pnniSummaryAddrEntry-AddrIndex-NodeIndex": pnniSummaryAddrEntry_AddrIndex_NodeIndex,
       "pnniSummaryAddrEntry-AddrIndex-Type": pnniSummaryAddrEntry_AddrIndex_Type,
       "pnniSummaryAddrEntry-AddrIndex-Address": pnniSummaryAddrEntry_AddrIndex_Address,
       "pnniSummaryAddrEntry-AddrIndex-PrefixLen": pnniSummaryAddrEntry_AddrIndex_PrefixLen,
       "pnniSummaryAddrEntry-Suppress": pnniSummaryAddrEntry_Suppress,
       "pnniSummaryAddrEntry-State": pnniSummaryAddrEntry_State,
       "pnniSummaryAddrEntry-Active": pnniSummaryAddrEntry_Active,
       "pnniSummaryAddrEntry-Action-o": pnniSummaryAddrEntry_Action_o,
       "mibpnniIfConfig": mibpnniIfConfig,
       "mibpnniIfConfigTable": mibpnniIfConfigTable,
       "mibpnniIfConfigEntry": mibpnniIfConfigEntry,
       "pnniIfConfig-Shelf-o": pnniIfConfig_Shelf_o,
       "pnniIfConfig-Slot-o": pnniIfConfig_Slot_o,
       "pnniIfConfig-Item-o": pnniIfConfig_Item_o,
       "pnniIfConfig-LogicalItem-o": pnniIfConfig_LogicalItem_o,
       "pnniIfConfig-Address-PhysicalAddress-Shelf": pnniIfConfig_Address_PhysicalAddress_Shelf,
       "pnniIfConfig-Address-PhysicalAddress-Slot": pnniIfConfig_Address_PhysicalAddress_Slot,
       "pnniIfConfig-Address-PhysicalAddress-ItemNumber": pnniIfConfig_Address_PhysicalAddress_ItemNumber,
       "pnniIfConfig-Address-LogicalItem": pnniIfConfig_Address_LogicalItem,
       "pnniIfConfig-IfNodeIndex": pnniIfConfig_IfNodeIndex,
       "pnniIfConfig-IfAggrToken": pnniIfConfig_IfAggrToken,
       "pnniIfConfig-IfVpCapability": pnniIfConfig_IfVpCapability,
       "pnniIfConfig-IfAdmWeightCbr": pnniIfConfig_IfAdmWeightCbr,
       "pnniIfConfig-IfAdmWeightRtVbr": pnniIfConfig_IfAdmWeightRtVbr,
       "pnniIfConfig-IfAdmWeightNrtVbr": pnniIfConfig_IfAdmWeightNrtVbr,
       "pnniIfConfig-IfAdmWeightAbr": pnniIfConfig_IfAdmWeightAbr,
       "pnniIfConfig-IfAdmWeightUbr": pnniIfConfig_IfAdmWeightUbr,
       "pnniIfConfig-IfRccServiceCategory": pnniIfConfig_IfRccServiceCategory,
       "pnniIfConfig-IfRccQosName": pnniIfConfig_IfRccQosName,
       "pnniIfConfig-Action-o": pnniIfConfig_Action_o,
       "mibpnniMetricsConfig": mibpnniMetricsConfig,
       "mibpnniMetricsConfigTable": mibpnniMetricsConfigTable,
       "mibpnniMetricsConfigEntry": mibpnniMetricsConfigEntry,
       "pnniMetricsConfig-MetricsIndex-NodeIndex": pnniMetricsConfig_MetricsIndex_NodeIndex,
       "pnniMetricsConfig-MetricsIndex-MetricsTag": pnniMetricsConfig_MetricsIndex_MetricsTag,
       "pnniMetricsConfig-MetricsIndex-MetricsDirection": pnniMetricsConfig_MetricsIndex_MetricsDirection,
       "pnniMetricsConfig-MetricsIndex-MetricsIndex": pnniMetricsConfig_MetricsIndex_MetricsIndex,
       "pnniMetricsConfig-MetricsClasses": pnniMetricsConfig_MetricsClasses,
       "pnniMetricsConfig-MetricsGcacClp": pnniMetricsConfig_MetricsGcacClp,
       "pnniMetricsConfig-MetricsAdminWeight": pnniMetricsConfig_MetricsAdminWeight,
       "pnniMetricsConfig-Metrics1": pnniMetricsConfig_Metrics1,
       "pnniMetricsConfig-Metrics2": pnniMetricsConfig_Metrics2,
       "pnniMetricsConfig-Metrics3": pnniMetricsConfig_Metrics3,
       "pnniMetricsConfig-Metrics4": pnniMetricsConfig_Metrics4,
       "pnniMetricsConfig-Metrics5": pnniMetricsConfig_Metrics5,
       "pnniMetricsConfig-Metrics6": pnniMetricsConfig_Metrics6,
       "pnniMetricsConfig-Metrics7": pnniMetricsConfig_Metrics7,
       "pnniMetricsConfig-Metrics8": pnniMetricsConfig_Metrics8,
       "pnniMetricsConfig-Active": pnniMetricsConfig_Active,
       "pnniMetricsConfig-Action-o": pnniMetricsConfig_Action_o,
       "mibpnniRouteNodeConfig": mibpnniRouteNodeConfig,
       "mibpnniRouteNodeConfigTable": mibpnniRouteNodeConfigTable,
       "mibpnniRouteNodeConfigEntry": mibpnniRouteNodeConfigEntry,
       "pnniRouteNodeConfig-Index-NodeIndex": pnniRouteNodeConfig_Index_NodeIndex,
       "pnniRouteNodeConfig-Index-RouteNodeClass": pnniRouteNodeConfig_Index_RouteNodeClass,
       "pnniRouteNodeConfig-Index-RouteNodeDestNodeId": pnniRouteNodeConfig_Index_RouteNodeDestNodeId,
       "pnniRouteNodeConfig-Index-RouteNodeDtl": pnniRouteNodeConfig_Index_RouteNodeDtl,
       "pnniRouteNodeConfig-DestPortId": pnniRouteNodeConfig_DestPortId,
       "pnniRouteNodeConfig-Proto": pnniRouteNodeConfig_Proto,
       "pnniRouteNodeConfig-TimeStamp": pnniRouteNodeConfig_TimeStamp,
       "pnniRouteNodeConfig-NodeInfo": pnniRouteNodeConfig_NodeInfo,
       "pnniRouteNodeConfig-GcacClp": pnniRouteNodeConfig_GcacClp,
       "pnniRouteNodeConfig-FwdMetricAw": pnniRouteNodeConfig_FwdMetricAw,
       "pnniRouteNodeConfig-FwdMetric1": pnniRouteNodeConfig_FwdMetric1,
       "pnniRouteNodeConfig-FwdMetric2": pnniRouteNodeConfig_FwdMetric2,
       "pnniRouteNodeConfig-FwdMetric3": pnniRouteNodeConfig_FwdMetric3,
       "pnniRouteNodeConfig-FwdMetric4": pnniRouteNodeConfig_FwdMetric4,
       "pnniRouteNodeConfig-FwdMetric5": pnniRouteNodeConfig_FwdMetric5,
       "pnniRouteNodeConfig-FwdMeteric6": pnniRouteNodeConfig_FwdMeteric6,
       "pnniRouteNodeConfig-FwdMeteric7": pnniRouteNodeConfig_FwdMeteric7,
       "pnniRouteNodeConfig-FwdMeteric8": pnniRouteNodeConfig_FwdMeteric8,
       "pnniRouteNodeConfig-BwdMetricAw": pnniRouteNodeConfig_BwdMetricAw,
       "pnniRouteNodeConfig-BwdMetric1": pnniRouteNodeConfig_BwdMetric1,
       "pnniRouteNodeConfig-BwdMetric2": pnniRouteNodeConfig_BwdMetric2,
       "pnniRouteNodeConfig-BwdMetric3": pnniRouteNodeConfig_BwdMetric3,
       "pnniRouteNodeConfig-BwdMetric4": pnniRouteNodeConfig_BwdMetric4,
       "pnniRouteNodeConfig-BwdMetric5": pnniRouteNodeConfig_BwdMetric5,
       "pnniRouteNodeConfig-BwdMetric6": pnniRouteNodeConfig_BwdMetric6,
       "pnniRouteNodeConfig-BwdMetric7": pnniRouteNodeConfig_BwdMetric7,
       "pnniRouteNodeConfig-BwdMetric8": pnniRouteNodeConfig_BwdMetric8,
       "pnniRouteNodeConfig-VpCapability": pnniRouteNodeConfig_VpCapability,
       "pnniRouteNodeConfig-Active": pnniRouteNodeConfig_Active,
       "pnniRouteNodeConfig-Action-o": pnniRouteNodeConfig_Action_o,
       "mibpnniDTLConfig": mibpnniDTLConfig,
       "mibpnniDTLConfigTable": mibpnniDTLConfigTable,
       "mibpnniDTLConfigEntry": mibpnniDTLConfigEntry,
       "pnniDTLConfig-DtlIndex-NodeIndex": pnniDTLConfig_DtlIndex_NodeIndex,
       "pnniDTLConfig-DtlIndex-DtlIndex": pnniDTLConfig_DtlIndex_DtlIndex,
       "pnniDTLConfig-DtlIndex-DtlEntryIndex": pnniDTLConfig_DtlIndex_DtlEntryIndex,
       "pnniDTLConfig-DtlNodeId": pnniDTLConfig_DtlNodeId,
       "pnniDTLConfig-DtlPortId": pnniDTLConfig_DtlPortId,
       "pnniDTLConfig-DtlLinkType": pnniDTLConfig_DtlLinkType,
       "pnniDTLConfig-Active": pnniDTLConfig_Active,
       "pnniDTLConfig-Action-o": pnniDTLConfig_Action_o,
       "mibpnniRouteAddrConfig": mibpnniRouteAddrConfig,
       "mibpnniRouteAddrConfigTable": mibpnniRouteAddrConfigTable,
       "mibpnniRouteAddrConfigEntry": mibpnniRouteAddrConfigEntry,
       "pnniRouteAddrConfig-Name": pnniRouteAddrConfig_Name,
       "pnniRouteAddrConfig-AddrIndex-NodeIndex": pnniRouteAddrConfig_AddrIndex_NodeIndex,
       "pnniRouteAddrConfig-AddrIndex-Address": pnniRouteAddrConfig_AddrIndex_Address,
       "pnniRouteAddrConfig-AddrIndex-PrefixLen": pnniRouteAddrConfig_AddrIndex_PrefixLen,
       "pnniRouteAddrConfig-AddrIndex-Index": pnniRouteAddrConfig_AddrIndex_Index,
       "pnniRouteAddrConfig-IfIndex": pnniRouteAddrConfig_IfIndex,
       "pnniRouteAddrConfig-AdvNodeId": pnniRouteAddrConfig_AdvNodeId,
       "pnniRouteAddrConfig-AdvPortId": pnniRouteAddrConfig_AdvPortId,
       "pnniRouteAddrConfig-Type": pnniRouteAddrConfig_Type,
       "pnniRouteAddrConfig-Proto": pnniRouteAddrConfig_Proto,
       "pnniRouteAddrConfig-PnniScope": pnniRouteAddrConfig_PnniScope,
       "pnniRouteAddrConfig-VpCapability": pnniRouteAddrConfig_VpCapability,
       "pnniRouteAddrConfig-MetricsTag": pnniRouteAddrConfig_MetricsTag,
       "pnniRouteAddrConfig-PtseIdPtseId": pnniRouteAddrConfig_PtseIdPtseId,
       "pnniRouteAddrConfig-OriginateAdvert": pnniRouteAddrConfig_OriginateAdvert,
       "pnniRouteAddrConfig-Info": pnniRouteAddrConfig_Info,
       "pnniRouteAddrConfig-OperStatus": pnniRouteAddrConfig_OperStatus,
       "pnniRouteAddrConfig-TimeStamp": pnniRouteAddrConfig_TimeStamp,
       "pnniRouteAddrConfig-Active": pnniRouteAddrConfig_Active,
       "pnniRouteAddrConfig-Action-o": pnniRouteAddrConfig_Action_o,
       "mibpnniRouteTnsConfig": mibpnniRouteTnsConfig,
       "mibpnniRouteTnsConfigTable": mibpnniRouteTnsConfigTable,
       "mibpnniRouteTnsConfigEntry": mibpnniRouteTnsConfigEntry,
       "pnniRouteTnsConfig-TnsIndex-NodeIndex": pnniRouteTnsConfig_TnsIndex_NodeIndex,
       "pnniRouteTnsConfig-TnsIndex-RouteTnsType": pnniRouteTnsConfig_TnsIndex_RouteTnsType,
       "pnniRouteTnsConfig-TnsIndex-RouteTnsPlan": pnniRouteTnsConfig_TnsIndex_RouteTnsPlan,
       "pnniRouteTnsConfig-TnsIndex-RouteTnsId": pnniRouteTnsConfig_TnsIndex_RouteTnsId,
       "pnniRouteTnsConfig-TnsIndex-RouteTnsIndex": pnniRouteTnsConfig_TnsIndex_RouteTnsIndex,
       "pnniRouteTnsConfig-TnsIfIndex": pnniRouteTnsConfig_TnsIfIndex,
       "pnniRouteTnsConfig-TnsAdvertisingNodeId": pnniRouteTnsConfig_TnsAdvertisingNodeId,
       "pnniRouteTnsConfig-TnsAdvertisedPortId": pnniRouteTnsConfig_TnsAdvertisedPortId,
       "pnniRouteTnsConfig-TnsRouteType": pnniRouteTnsConfig_TnsRouteType,
       "pnniRouteTnsConfig-TnsPnniScope": pnniRouteTnsConfig_TnsPnniScope,
       "pnniRouteTnsConfig-TnsVpCapability": pnniRouteTnsConfig_TnsVpCapability,
       "pnniRouteTnsConfig-TnsMetricsTag": pnniRouteTnsConfig_TnsMetricsTag,
       "pnniRouteTnsConfig-TnsOriginateAdvertisement": pnniRouteTnsConfig_TnsOriginateAdvertisement,
       "pnniRouteTnsConfig-Active": pnniRouteTnsConfig_Active,
       "pnniRouteTnsConfig-Action-o": pnniRouteTnsConfig_Action_o}
)
