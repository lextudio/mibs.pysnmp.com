# SNMP MIB module (PW-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:02 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(IANAPwCapabilities,
 IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "IANA-PWE3-MIB",
    "IANAPwCapabilities",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PwAttachmentIdentifierType,
 PwCwStatusTC,
 PwFragSize,
 PwFragStatus,
 PwGenIdType,
 PwGroupID,
 PwIDType,
 PwIndexOrZeroType,
 PwIndexType,
 PwOperStatusTC,
 PwStatus) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwAttachmentIdentifierType",
    "PwCwStatusTC",
    "PwFragSize",
    "PwFragStatus",
    "PwGenIdType",
    "PwGroupID",
    "PwIDType",
    "PwIndexOrZeroType",
    "PwIndexType",
    "PwOperStatusTC",
    "PwStatus")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pwStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246)
)
pwStdMIB.setRevisions(
        ("2009-06-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PwNotifications_ObjectIdentity = ObjectIdentity
pwNotifications = _PwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246, 0)
)
_PwObjects_ObjectIdentity = ObjectIdentity
pwObjects = _PwObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246, 1)
)
_PwIndexNext_Type = Unsigned32
_PwIndexNext_Object = MibScalar
pwIndexNext = _PwIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 1),
    _PwIndexNext_Type()
)
pwIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwIndexNext.setStatus("current")
_PwTable_Object = MibTable
pwTable = _PwTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2)
)
if mibBuilder.loadTexts:
    pwTable.setStatus("current")
_PwEntry_Object = MibTableRow
pwEntry = _PwEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1)
)
pwEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwEntry.setStatus("current")
_PwIndex_Type = PwIndexType
_PwIndex_Object = MibTableColumn
pwIndex = _PwIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 1),
    _PwIndex_Type()
)
pwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndex.setStatus("current")
_PwType_Type = IANAPwTypeTC
_PwType_Object = MibTableColumn
pwType = _PwType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 2),
    _PwType_Type()
)
pwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwType.setStatus("current")


class _PwOwner_Type(Integer32):
    """Custom type pwOwner based on Integer32"""
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
        *(("genFecSignaling", 3),
          ("l2tpControlProtocol", 4),
          ("manual", 1),
          ("other", 5),
          ("pwIdFecSignaling", 2))
    )


_PwOwner_Type.__name__ = "Integer32"
_PwOwner_Object = MibTableColumn
pwOwner = _PwOwner_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 3),
    _PwOwner_Type()
)
pwOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOwner.setStatus("current")
_PwPsnType_Type = IANAPwPsnTypeTC
_PwPsnType_Object = MibTableColumn
pwPsnType = _PwPsnType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 4),
    _PwPsnType_Type()
)
pwPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPsnType.setStatus("current")


class _PwSetUpPriority_Type(Integer32):
    """Custom type pwSetUpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PwSetUpPriority_Type.__name__ = "Integer32"
_PwSetUpPriority_Object = MibTableColumn
pwSetUpPriority = _PwSetUpPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 5),
    _PwSetUpPriority_Type()
)
pwSetUpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwSetUpPriority.setStatus("current")


class _PwHoldingPriority_Type(Integer32):
    """Custom type pwHoldingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PwHoldingPriority_Type.__name__ = "Integer32"
_PwHoldingPriority_Object = MibTableColumn
pwHoldingPriority = _PwHoldingPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 6),
    _PwHoldingPriority_Type()
)
pwHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwHoldingPriority.setStatus("current")


class _PwPeerAddrType_Type(InetAddressType):
    """Custom type pwPeerAddrType based on InetAddressType"""


_PwPeerAddrType_Object = MibTableColumn
pwPeerAddrType = _PwPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 8),
    _PwPeerAddrType_Type()
)
pwPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPeerAddrType.setStatus("current")
_PwPeerAddr_Type = InetAddress
_PwPeerAddr_Object = MibTableColumn
pwPeerAddr = _PwPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 9),
    _PwPeerAddr_Type()
)
pwPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPeerAddr.setStatus("current")


class _PwAttachedPwIndex_Type(PwIndexOrZeroType):
    """Custom type pwAttachedPwIndex based on PwIndexOrZeroType"""
    defaultValue = 0


_PwAttachedPwIndex_Object = MibTableColumn
pwAttachedPwIndex = _PwAttachedPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 10),
    _PwAttachedPwIndex_Type()
)
pwAttachedPwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAttachedPwIndex.setStatus("current")


class _PwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PwIfIndex_Object = MibTableColumn
pwIfIndex = _PwIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 11),
    _PwIfIndex_Type()
)
pwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwIfIndex.setStatus("current")
_PwID_Type = PwIDType
_PwID_Object = MibTableColumn
pwID = _PwID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 12),
    _PwID_Type()
)
pwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwID.setStatus("current")
_PwLocalGroupID_Type = PwGroupID
_PwLocalGroupID_Object = MibTableColumn
pwLocalGroupID = _PwLocalGroupID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 13),
    _PwLocalGroupID_Type()
)
pwLocalGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalGroupID.setStatus("current")
_PwGroupAttachmentID_Type = PwAttachmentIdentifierType
_PwGroupAttachmentID_Object = MibTableColumn
pwGroupAttachmentID = _PwGroupAttachmentID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 14),
    _PwGroupAttachmentID_Type()
)
pwGroupAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGroupAttachmentID.setStatus("current")
_PwLocalAttachmentID_Type = PwAttachmentIdentifierType
_PwLocalAttachmentID_Object = MibTableColumn
pwLocalAttachmentID = _PwLocalAttachmentID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 15),
    _PwLocalAttachmentID_Type()
)
pwLocalAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalAttachmentID.setStatus("current")
_PwRemoteAttachmentID_Type = PwAttachmentIdentifierType
_PwRemoteAttachmentID_Object = MibTableColumn
pwRemoteAttachmentID = _PwRemoteAttachmentID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 16),
    _PwRemoteAttachmentID_Type()
)
pwRemoteAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwRemoteAttachmentID.setStatus("current")


class _PwCwPreference_Type(TruthValue):
    """Custom type pwCwPreference based on TruthValue"""


_PwCwPreference_Object = MibTableColumn
pwCwPreference = _PwCwPreference_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 17),
    _PwCwPreference_Type()
)
pwCwPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCwPreference.setStatus("current")


class _PwLocalIfMtu_Type(Unsigned32):
    """Custom type pwLocalIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PwLocalIfMtu_Type.__name__ = "Unsigned32"
_PwLocalIfMtu_Object = MibTableColumn
pwLocalIfMtu = _PwLocalIfMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 18),
    _PwLocalIfMtu_Type()
)
pwLocalIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalIfMtu.setStatus("current")


class _PwLocalIfString_Type(TruthValue):
    """Custom type pwLocalIfString based on TruthValue"""


_PwLocalIfString_Object = MibTableColumn
pwLocalIfString = _PwLocalIfString_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 19),
    _PwLocalIfString_Type()
)
pwLocalIfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalIfString.setStatus("current")
_PwLocalCapabAdvert_Type = IANAPwCapabilities
_PwLocalCapabAdvert_Object = MibTableColumn
pwLocalCapabAdvert = _PwLocalCapabAdvert_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 20),
    _PwLocalCapabAdvert_Type()
)
pwLocalCapabAdvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalCapabAdvert.setStatus("current")
_PwRemoteGroupID_Type = PwGroupID
_PwRemoteGroupID_Object = MibTableColumn
pwRemoteGroupID = _PwRemoteGroupID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 21),
    _PwRemoteGroupID_Type()
)
pwRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteGroupID.setStatus("current")
_PwCwStatus_Type = PwCwStatusTC
_PwCwStatus_Object = MibTableColumn
pwCwStatus = _PwCwStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 22),
    _PwCwStatus_Type()
)
pwCwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCwStatus.setStatus("current")
_PwRemoteIfMtu_Type = Unsigned32
_PwRemoteIfMtu_Object = MibTableColumn
pwRemoteIfMtu = _PwRemoteIfMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 23),
    _PwRemoteIfMtu_Type()
)
pwRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteIfMtu.setStatus("current")


class _PwRemoteIfString_Type(SnmpAdminString):
    """Custom type pwRemoteIfString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PwRemoteIfString_Type.__name__ = "SnmpAdminString"
_PwRemoteIfString_Object = MibTableColumn
pwRemoteIfString = _PwRemoteIfString_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 24),
    _PwRemoteIfString_Type()
)
pwRemoteIfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteIfString.setStatus("current")
_PwRemoteCapabilities_Type = IANAPwCapabilities
_PwRemoteCapabilities_Object = MibTableColumn
pwRemoteCapabilities = _PwRemoteCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 25),
    _PwRemoteCapabilities_Type()
)
pwRemoteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteCapabilities.setStatus("current")


class _PwFragmentCfgSize_Type(PwFragSize):
    """Custom type pwFragmentCfgSize based on PwFragSize"""
    defaultValue = 0


_PwFragmentCfgSize_Object = MibTableColumn
pwFragmentCfgSize = _PwFragmentCfgSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 26),
    _PwFragmentCfgSize_Type()
)
pwFragmentCfgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwFragmentCfgSize.setStatus("current")
if mibBuilder.loadTexts:
    pwFragmentCfgSize.setUnits("bytes")
_PwRmtFragCapability_Type = PwFragStatus
_PwRmtFragCapability_Object = MibTableColumn
pwRmtFragCapability = _PwRmtFragCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 27),
    _PwRmtFragCapability_Type()
)
pwRmtFragCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRmtFragCapability.setStatus("current")


class _PwFcsRetentionCfg_Type(Integer32):
    """Custom type pwFcsRetentionCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcsRetentionDisable", 1),
          ("fcsRetentionEnable", 2))
    )


_PwFcsRetentionCfg_Type.__name__ = "Integer32"
_PwFcsRetentionCfg_Object = MibTableColumn
pwFcsRetentionCfg = _PwFcsRetentionCfg_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 28),
    _PwFcsRetentionCfg_Type()
)
pwFcsRetentionCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwFcsRetentionCfg.setStatus("current")


class _PwFcsRetentionStatus_Type(Bits):
    """Custom type pwFcsRetentionStatus based on Bits"""
    namedValues = NamedValues(
        *(("fcsRetentionDisabled", 3),
          ("fcsRetentionEnabled", 2),
          ("fcsRetentionFcsSizeMismatch", 5),
          ("localFcsRetentionCfgErr", 4),
          ("remoteIndicationUnknown", 0),
          ("remoteRequestFcsRetention", 1))
    )

_PwFcsRetentionStatus_Type.__name__ = "Bits"
_PwFcsRetentionStatus_Object = MibTableColumn
pwFcsRetentionStatus = _PwFcsRetentionStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 29),
    _PwFcsRetentionStatus_Type()
)
pwFcsRetentionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFcsRetentionStatus.setStatus("current")
_PwOutboundLabel_Type = Unsigned32
_PwOutboundLabel_Object = MibTableColumn
pwOutboundLabel = _PwOutboundLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 30),
    _PwOutboundLabel_Type()
)
pwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOutboundLabel.setStatus("current")
_PwInboundLabel_Type = Unsigned32
_PwInboundLabel_Object = MibTableColumn
pwInboundLabel = _PwInboundLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 31),
    _PwInboundLabel_Type()
)
pwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwInboundLabel.setStatus("current")
_PwName_Type = SnmpAdminString
_PwName_Object = MibTableColumn
pwName = _PwName_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 32),
    _PwName_Type()
)
pwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwName.setStatus("current")
_PwDescr_Type = SnmpAdminString
_PwDescr_Object = MibTableColumn
pwDescr = _PwDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 33),
    _PwDescr_Type()
)
pwDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwDescr.setStatus("current")
_PwCreateTime_Type = TimeStamp
_PwCreateTime_Object = MibTableColumn
pwCreateTime = _PwCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 34),
    _PwCreateTime_Type()
)
pwCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCreateTime.setStatus("current")
_PwUpTime_Type = TimeTicks
_PwUpTime_Object = MibTableColumn
pwUpTime = _PwUpTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 35),
    _PwUpTime_Type()
)
pwUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwUpTime.setStatus("current")
_PwLastChange_Type = TimeTicks
_PwLastChange_Object = MibTableColumn
pwLastChange = _PwLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 36),
    _PwLastChange_Type()
)
pwLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwLastChange.setStatus("current")


class _PwAdminStatus_Type(Integer32):
    """Custom type pwAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_PwAdminStatus_Type.__name__ = "Integer32"
_PwAdminStatus_Object = MibTableColumn
pwAdminStatus = _PwAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 37),
    _PwAdminStatus_Type()
)
pwAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAdminStatus.setStatus("current")
_PwOperStatus_Type = PwOperStatusTC
_PwOperStatus_Object = MibTableColumn
pwOperStatus = _PwOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 38),
    _PwOperStatus_Type()
)
pwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwOperStatus.setStatus("current")
_PwLocalStatus_Type = PwStatus
_PwLocalStatus_Object = MibTableColumn
pwLocalStatus = _PwLocalStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 39),
    _PwLocalStatus_Type()
)
pwLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwLocalStatus.setStatus("current")


class _PwRemoteStatusCapable_Type(Integer32):
    """Custom type pwRemoteStatusCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notYetKnown", 2),
          ("remoteCapable", 3),
          ("remoteNotCapable", 4))
    )


_PwRemoteStatusCapable_Type.__name__ = "Integer32"
_PwRemoteStatusCapable_Object = MibTableColumn
pwRemoteStatusCapable = _PwRemoteStatusCapable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 40),
    _PwRemoteStatusCapable_Type()
)
pwRemoteStatusCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteStatusCapable.setStatus("current")
_PwRemoteStatus_Type = PwStatus
_PwRemoteStatus_Object = MibTableColumn
pwRemoteStatus = _PwRemoteStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 41),
    _PwRemoteStatus_Type()
)
pwRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteStatus.setStatus("current")
_PwTimeElapsed_Type = HCPerfTimeElapsed
_PwTimeElapsed_Object = MibTableColumn
pwTimeElapsed = _PwTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 42),
    _PwTimeElapsed_Type()
)
pwTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTimeElapsed.setStatus("current")
_PwValidIntervals_Type = HCPerfValidIntervals
_PwValidIntervals_Object = MibTableColumn
pwValidIntervals = _PwValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 43),
    _PwValidIntervals_Type()
)
pwValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwValidIntervals.setStatus("current")
_PwRowStatus_Type = RowStatus
_PwRowStatus_Object = MibTableColumn
pwRowStatus = _PwRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 44),
    _PwRowStatus_Type()
)
pwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwRowStatus.setStatus("current")


class _PwStorageType_Type(StorageType):
    """Custom type pwStorageType based on StorageType"""


_PwStorageType_Object = MibTableColumn
pwStorageType = _PwStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 45),
    _PwStorageType_Type()
)
pwStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStorageType.setStatus("current")


class _PwOamEnable_Type(TruthValue):
    """Custom type pwOamEnable based on TruthValue"""


_PwOamEnable_Object = MibTableColumn
pwOamEnable = _PwOamEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 46),
    _PwOamEnable_Type()
)
pwOamEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOamEnable.setStatus("current")


class _PwGenAGIType_Type(PwGenIdType):
    """Custom type pwGenAGIType based on PwGenIdType"""
    defaultValue = 0


_PwGenAGIType_Object = MibTableColumn
pwGenAGIType = _PwGenAGIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 47),
    _PwGenAGIType_Type()
)
pwGenAGIType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenAGIType.setStatus("current")


class _PwGenLocalAIIType_Type(PwGenIdType):
    """Custom type pwGenLocalAIIType based on PwGenIdType"""
    defaultValue = 0


_PwGenLocalAIIType_Object = MibTableColumn
pwGenLocalAIIType = _PwGenLocalAIIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 48),
    _PwGenLocalAIIType_Type()
)
pwGenLocalAIIType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenLocalAIIType.setStatus("current")


class _PwGenRemoteAIIType_Type(PwGenIdType):
    """Custom type pwGenRemoteAIIType based on PwGenIdType"""
    defaultValue = 0


_PwGenRemoteAIIType_Object = MibTableColumn
pwGenRemoteAIIType = _PwGenRemoteAIIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 49),
    _PwGenRemoteAIIType_Type()
)
pwGenRemoteAIIType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGenRemoteAIIType.setStatus("current")
_PwPerfCurrentTable_Object = MibTable
pwPerfCurrentTable = _PwPerfCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3)
)
if mibBuilder.loadTexts:
    pwPerfCurrentTable.setStatus("current")
_PwPerfCurrentEntry_Object = MibTableRow
pwPerfCurrentEntry = _PwPerfCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1)
)
pwPerfCurrentEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwPerfCurrentEntry.setStatus("current")
_PwPerfCurrentInHCPackets_Type = HCPerfCurrentCount
_PwPerfCurrentInHCPackets_Object = MibTableColumn
pwPerfCurrentInHCPackets = _PwPerfCurrentInHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 1),
    _PwPerfCurrentInHCPackets_Type()
)
pwPerfCurrentInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInHCPackets.setStatus("current")
_PwPerfCurrentInHCBytes_Type = HCPerfCurrentCount
_PwPerfCurrentInHCBytes_Object = MibTableColumn
pwPerfCurrentInHCBytes = _PwPerfCurrentInHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 2),
    _PwPerfCurrentInHCBytes_Type()
)
pwPerfCurrentInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInHCBytes.setStatus("current")
_PwPerfCurrentOutHCPackets_Type = HCPerfCurrentCount
_PwPerfCurrentOutHCPackets_Object = MibTableColumn
pwPerfCurrentOutHCPackets = _PwPerfCurrentOutHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 3),
    _PwPerfCurrentOutHCPackets_Type()
)
pwPerfCurrentOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutHCPackets.setStatus("current")
_PwPerfCurrentOutHCBytes_Type = HCPerfCurrentCount
_PwPerfCurrentOutHCBytes_Object = MibTableColumn
pwPerfCurrentOutHCBytes = _PwPerfCurrentOutHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 4),
    _PwPerfCurrentOutHCBytes_Type()
)
pwPerfCurrentOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutHCBytes.setStatus("current")
_PwPerfCurrentInPackets_Type = PerfCurrentCount
_PwPerfCurrentInPackets_Object = MibTableColumn
pwPerfCurrentInPackets = _PwPerfCurrentInPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 5),
    _PwPerfCurrentInPackets_Type()
)
pwPerfCurrentInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInPackets.setStatus("current")
_PwPerfCurrentInBytes_Type = PerfCurrentCount
_PwPerfCurrentInBytes_Object = MibTableColumn
pwPerfCurrentInBytes = _PwPerfCurrentInBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 6),
    _PwPerfCurrentInBytes_Type()
)
pwPerfCurrentInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInBytes.setStatus("current")
_PwPerfCurrentOutPackets_Type = PerfCurrentCount
_PwPerfCurrentOutPackets_Object = MibTableColumn
pwPerfCurrentOutPackets = _PwPerfCurrentOutPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 7),
    _PwPerfCurrentOutPackets_Type()
)
pwPerfCurrentOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutPackets.setStatus("current")
_PwPerfCurrentOutBytes_Type = PerfCurrentCount
_PwPerfCurrentOutBytes_Object = MibTableColumn
pwPerfCurrentOutBytes = _PwPerfCurrentOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 8),
    _PwPerfCurrentOutBytes_Type()
)
pwPerfCurrentOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutBytes.setStatus("current")
_PwPerfIntervalTable_Object = MibTable
pwPerfIntervalTable = _PwPerfIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4)
)
if mibBuilder.loadTexts:
    pwPerfIntervalTable.setStatus("current")
_PwPerfIntervalEntry_Object = MibTableRow
pwPerfIntervalEntry = _PwPerfIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1)
)
pwPerfIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-STD-MIB", "pwPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwPerfIntervalEntry.setStatus("current")


class _PwPerfIntervalNumber_Type(Integer32):
    """Custom type pwPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PwPerfIntervalNumber_Type.__name__ = "Integer32"
_PwPerfIntervalNumber_Object = MibTableColumn
pwPerfIntervalNumber = _PwPerfIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 1),
    _PwPerfIntervalNumber_Type()
)
pwPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPerfIntervalNumber.setStatus("current")
_PwPerfIntervalValidData_Type = TruthValue
_PwPerfIntervalValidData_Object = MibTableColumn
pwPerfIntervalValidData = _PwPerfIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 2),
    _PwPerfIntervalValidData_Type()
)
pwPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalValidData.setStatus("current")
_PwPerfIntervalTimeElapsed_Type = HCPerfTimeElapsed
_PwPerfIntervalTimeElapsed_Object = MibTableColumn
pwPerfIntervalTimeElapsed = _PwPerfIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 3),
    _PwPerfIntervalTimeElapsed_Type()
)
pwPerfIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalTimeElapsed.setStatus("current")
_PwPerfIntervalInHCPackets_Type = HCPerfIntervalCount
_PwPerfIntervalInHCPackets_Object = MibTableColumn
pwPerfIntervalInHCPackets = _PwPerfIntervalInHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 4),
    _PwPerfIntervalInHCPackets_Type()
)
pwPerfIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInHCPackets.setStatus("current")
_PwPerfIntervalInHCBytes_Type = HCPerfIntervalCount
_PwPerfIntervalInHCBytes_Object = MibTableColumn
pwPerfIntervalInHCBytes = _PwPerfIntervalInHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 5),
    _PwPerfIntervalInHCBytes_Type()
)
pwPerfIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInHCBytes.setStatus("current")
_PwPerfIntervalOutHCPackets_Type = HCPerfIntervalCount
_PwPerfIntervalOutHCPackets_Object = MibTableColumn
pwPerfIntervalOutHCPackets = _PwPerfIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 6),
    _PwPerfIntervalOutHCPackets_Type()
)
pwPerfIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutHCPackets.setStatus("current")
_PwPerfIntervalOutHCBytes_Type = HCPerfIntervalCount
_PwPerfIntervalOutHCBytes_Object = MibTableColumn
pwPerfIntervalOutHCBytes = _PwPerfIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 7),
    _PwPerfIntervalOutHCBytes_Type()
)
pwPerfIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutHCBytes.setStatus("current")
_PwPerfIntervalInPackets_Type = PerfIntervalCount
_PwPerfIntervalInPackets_Object = MibTableColumn
pwPerfIntervalInPackets = _PwPerfIntervalInPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 8),
    _PwPerfIntervalInPackets_Type()
)
pwPerfIntervalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInPackets.setStatus("current")
_PwPerfIntervalInBytes_Type = PerfIntervalCount
_PwPerfIntervalInBytes_Object = MibTableColumn
pwPerfIntervalInBytes = _PwPerfIntervalInBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 9),
    _PwPerfIntervalInBytes_Type()
)
pwPerfIntervalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInBytes.setStatus("current")
_PwPerfIntervalOutPackets_Type = PerfIntervalCount
_PwPerfIntervalOutPackets_Object = MibTableColumn
pwPerfIntervalOutPackets = _PwPerfIntervalOutPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 10),
    _PwPerfIntervalOutPackets_Type()
)
pwPerfIntervalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutPackets.setStatus("current")
_PwPerfIntervalOutBytes_Type = PerfIntervalCount
_PwPerfIntervalOutBytes_Object = MibTableColumn
pwPerfIntervalOutBytes = _PwPerfIntervalOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 11),
    _PwPerfIntervalOutBytes_Type()
)
pwPerfIntervalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutBytes.setStatus("current")
_PwPerf1DayIntervalTable_Object = MibTable
pwPerf1DayIntervalTable = _PwPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5)
)
if mibBuilder.loadTexts:
    pwPerf1DayIntervalTable.setStatus("current")
_PwPerf1DayIntervalEntry_Object = MibTableRow
pwPerf1DayIntervalEntry = _PwPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1)
)
pwPerf1DayIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-STD-MIB", "pwPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwPerf1DayIntervalEntry.setStatus("current")


class _PwPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type pwPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PwPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PwPerf1DayIntervalNumber_Object = MibTableColumn
pwPerf1DayIntervalNumber = _PwPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 1),
    _PwPerf1DayIntervalNumber_Type()
)
pwPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalNumber.setStatus("current")
_PwPerf1DayIntervalValidData_Type = TruthValue
_PwPerf1DayIntervalValidData_Object = MibTableColumn
pwPerf1DayIntervalValidData = _PwPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 2),
    _PwPerf1DayIntervalValidData_Type()
)
pwPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalValidData.setStatus("current")
_PwPerf1DayIntervalTimeElapsed_Type = HCPerfTimeElapsed
_PwPerf1DayIntervalTimeElapsed_Object = MibTableColumn
pwPerf1DayIntervalTimeElapsed = _PwPerf1DayIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 3),
    _PwPerf1DayIntervalTimeElapsed_Type()
)
pwPerf1DayIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalTimeElapsed.setUnits("seconds")
_PwPerf1DayIntervalInHCPackets_Type = Counter64
_PwPerf1DayIntervalInHCPackets_Object = MibTableColumn
pwPerf1DayIntervalInHCPackets = _PwPerf1DayIntervalInHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 4),
    _PwPerf1DayIntervalInHCPackets_Type()
)
pwPerf1DayIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalInHCPackets.setStatus("current")
_PwPerf1DayIntervalInHCBytes_Type = Counter64
_PwPerf1DayIntervalInHCBytes_Object = MibTableColumn
pwPerf1DayIntervalInHCBytes = _PwPerf1DayIntervalInHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 5),
    _PwPerf1DayIntervalInHCBytes_Type()
)
pwPerf1DayIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalInHCBytes.setStatus("current")
_PwPerf1DayIntervalOutHCPackets_Type = Counter64
_PwPerf1DayIntervalOutHCPackets_Object = MibTableColumn
pwPerf1DayIntervalOutHCPackets = _PwPerf1DayIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 6),
    _PwPerf1DayIntervalOutHCPackets_Type()
)
pwPerf1DayIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalOutHCPackets.setStatus("current")
_PwPerf1DayIntervalOutHCBytes_Type = Counter64
_PwPerf1DayIntervalOutHCBytes_Object = MibTableColumn
pwPerf1DayIntervalOutHCBytes = _PwPerf1DayIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 7),
    _PwPerf1DayIntervalOutHCBytes_Type()
)
pwPerf1DayIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerf1DayIntervalOutHCBytes.setStatus("current")
_PwPerfTotalErrorPackets_Type = Counter32
_PwPerfTotalErrorPackets_Object = MibScalar
pwPerfTotalErrorPackets = _PwPerfTotalErrorPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 6),
    _PwPerfTotalErrorPackets_Type()
)
pwPerfTotalErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalErrorPackets.setStatus("current")
_PwIndexMappingTable_Object = MibTable
pwIndexMappingTable = _PwIndexMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7)
)
if mibBuilder.loadTexts:
    pwIndexMappingTable.setStatus("current")
_PwIndexMappingEntry_Object = MibTableRow
pwIndexMappingEntry = _PwIndexMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1)
)
pwIndexMappingEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndexMappingPwType"),
    (0, "PW-STD-MIB", "pwIndexMappingPwID"),
    (0, "PW-STD-MIB", "pwIndexMappingPeerAddrType"),
    (0, "PW-STD-MIB", "pwIndexMappingPeerAddr"),
)
if mibBuilder.loadTexts:
    pwIndexMappingEntry.setStatus("current")
_PwIndexMappingPwType_Type = IANAPwTypeTC
_PwIndexMappingPwType_Object = MibTableColumn
pwIndexMappingPwType = _PwIndexMappingPwType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 1),
    _PwIndexMappingPwType_Type()
)
pwIndexMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPwType.setStatus("current")
_PwIndexMappingPwID_Type = PwIDType
_PwIndexMappingPwID_Object = MibTableColumn
pwIndexMappingPwID = _PwIndexMappingPwID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 2),
    _PwIndexMappingPwID_Type()
)
pwIndexMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPwID.setStatus("current")
_PwIndexMappingPeerAddrType_Type = InetAddressType
_PwIndexMappingPeerAddrType_Object = MibTableColumn
pwIndexMappingPeerAddrType = _PwIndexMappingPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 3),
    _PwIndexMappingPeerAddrType_Type()
)
pwIndexMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPeerAddrType.setStatus("current")
_PwIndexMappingPeerAddr_Type = InetAddress
_PwIndexMappingPeerAddr_Object = MibTableColumn
pwIndexMappingPeerAddr = _PwIndexMappingPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 4),
    _PwIndexMappingPeerAddr_Type()
)
pwIndexMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPeerAddr.setStatus("current")
_PwIndexMappingPwIndex_Type = PwIndexType
_PwIndexMappingPwIndex_Object = MibTableColumn
pwIndexMappingPwIndex = _PwIndexMappingPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 5),
    _PwIndexMappingPwIndex_Type()
)
pwIndexMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwIndexMappingPwIndex.setStatus("current")
_PwPeerMappingTable_Object = MibTable
pwPeerMappingTable = _PwPeerMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8)
)
if mibBuilder.loadTexts:
    pwPeerMappingTable.setStatus("current")
_PwPeerMappingEntry_Object = MibTableRow
pwPeerMappingEntry = _PwPeerMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1)
)
pwPeerMappingEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwPeerMappingPeerAddrType"),
    (0, "PW-STD-MIB", "pwPeerMappingPeerAddr"),
    (0, "PW-STD-MIB", "pwPeerMappingPwType"),
    (0, "PW-STD-MIB", "pwPeerMappingPwID"),
)
if mibBuilder.loadTexts:
    pwPeerMappingEntry.setStatus("current")
_PwPeerMappingPeerAddrType_Type = InetAddressType
_PwPeerMappingPeerAddrType_Object = MibTableColumn
pwPeerMappingPeerAddrType = _PwPeerMappingPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 1),
    _PwPeerMappingPeerAddrType_Type()
)
pwPeerMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPeerAddrType.setStatus("current")
_PwPeerMappingPeerAddr_Type = InetAddress
_PwPeerMappingPeerAddr_Object = MibTableColumn
pwPeerMappingPeerAddr = _PwPeerMappingPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 2),
    _PwPeerMappingPeerAddr_Type()
)
pwPeerMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPeerAddr.setStatus("current")
_PwPeerMappingPwType_Type = IANAPwTypeTC
_PwPeerMappingPwType_Object = MibTableColumn
pwPeerMappingPwType = _PwPeerMappingPwType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 3),
    _PwPeerMappingPwType_Type()
)
pwPeerMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPwType.setStatus("current")
_PwPeerMappingPwID_Type = PwIDType
_PwPeerMappingPwID_Object = MibTableColumn
pwPeerMappingPwID = _PwPeerMappingPwID_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 4),
    _PwPeerMappingPwID_Type()
)
pwPeerMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPwID.setStatus("current")
_PwPeerMappingPwIndex_Type = PwIndexType
_PwPeerMappingPwIndex_Object = MibTableColumn
pwPeerMappingPwIndex = _PwPeerMappingPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 5),
    _PwPeerMappingPwIndex_Type()
)
pwPeerMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPeerMappingPwIndex.setStatus("current")


class _PwUpDownNotifEnable_Type(TruthValue):
    """Custom type pwUpDownNotifEnable based on TruthValue"""


_PwUpDownNotifEnable_Object = MibScalar
pwUpDownNotifEnable = _PwUpDownNotifEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 9),
    _PwUpDownNotifEnable_Type()
)
pwUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwUpDownNotifEnable.setStatus("current")


class _PwDeletedNotifEnable_Type(TruthValue):
    """Custom type pwDeletedNotifEnable based on TruthValue"""


_PwDeletedNotifEnable_Object = MibScalar
pwDeletedNotifEnable = _PwDeletedNotifEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 10),
    _PwDeletedNotifEnable_Type()
)
pwDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwDeletedNotifEnable.setStatus("current")
_PwNotifRate_Type = Unsigned32
_PwNotifRate_Object = MibScalar
pwNotifRate = _PwNotifRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 11),
    _PwNotifRate_Type()
)
pwNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwNotifRate.setStatus("current")
_PwGenFecIndexMappingTable_Object = MibTable
pwGenFecIndexMappingTable = _PwGenFecIndexMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12)
)
if mibBuilder.loadTexts:
    pwGenFecIndexMappingTable.setStatus("current")
_PwGenFecIndexMappingEntry_Object = MibTableRow
pwGenFecIndexMappingEntry = _PwGenFecIndexMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1)
)
pwGenFecIndexMappingEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwGenFecIndexMappingAGIType"),
    (0, "PW-STD-MIB", "pwGenFecIndexMappingAGI"),
    (0, "PW-STD-MIB", "pwGenFecIndexMappingLocalAIIType"),
    (0, "PW-STD-MIB", "pwGenFecIndexMappingLocalAII"),
    (0, "PW-STD-MIB", "pwGenFecIndexMappingRemoteAIIType"),
    (0, "PW-STD-MIB", "pwGenFecIndexMappingRemoteAII"),
)
if mibBuilder.loadTexts:
    pwGenFecIndexMappingEntry.setStatus("current")
_PwGenFecIndexMappingAGIType_Type = PwGenIdType
_PwGenFecIndexMappingAGIType_Object = MibTableColumn
pwGenFecIndexMappingAGIType = _PwGenFecIndexMappingAGIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 1),
    _PwGenFecIndexMappingAGIType_Type()
)
pwGenFecIndexMappingAGIType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingAGIType.setStatus("current")
_PwGenFecIndexMappingAGI_Type = PwAttachmentIdentifierType
_PwGenFecIndexMappingAGI_Object = MibTableColumn
pwGenFecIndexMappingAGI = _PwGenFecIndexMappingAGI_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 2),
    _PwGenFecIndexMappingAGI_Type()
)
pwGenFecIndexMappingAGI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingAGI.setStatus("current")
_PwGenFecIndexMappingLocalAIIType_Type = PwGenIdType
_PwGenFecIndexMappingLocalAIIType_Object = MibTableColumn
pwGenFecIndexMappingLocalAIIType = _PwGenFecIndexMappingLocalAIIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 3),
    _PwGenFecIndexMappingLocalAIIType_Type()
)
pwGenFecIndexMappingLocalAIIType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingLocalAIIType.setStatus("current")
_PwGenFecIndexMappingLocalAII_Type = PwAttachmentIdentifierType
_PwGenFecIndexMappingLocalAII_Object = MibTableColumn
pwGenFecIndexMappingLocalAII = _PwGenFecIndexMappingLocalAII_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 4),
    _PwGenFecIndexMappingLocalAII_Type()
)
pwGenFecIndexMappingLocalAII.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingLocalAII.setStatus("current")
_PwGenFecIndexMappingRemoteAIIType_Type = PwGenIdType
_PwGenFecIndexMappingRemoteAIIType_Object = MibTableColumn
pwGenFecIndexMappingRemoteAIIType = _PwGenFecIndexMappingRemoteAIIType_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 5),
    _PwGenFecIndexMappingRemoteAIIType_Type()
)
pwGenFecIndexMappingRemoteAIIType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingRemoteAIIType.setStatus("current")
_PwGenFecIndexMappingRemoteAII_Type = PwAttachmentIdentifierType
_PwGenFecIndexMappingRemoteAII_Object = MibTableColumn
pwGenFecIndexMappingRemoteAII = _PwGenFecIndexMappingRemoteAII_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 6),
    _PwGenFecIndexMappingRemoteAII_Type()
)
pwGenFecIndexMappingRemoteAII.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingRemoteAII.setStatus("current")
_PwGenFecIndexMappingPwIndex_Type = PwIndexType
_PwGenFecIndexMappingPwIndex_Object = MibTableColumn
pwGenFecIndexMappingPwIndex = _PwGenFecIndexMappingPwIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 7),
    _PwGenFecIndexMappingPwIndex_Type()
)
pwGenFecIndexMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwGenFecIndexMappingPwIndex.setStatus("current")
_PwConformance_ObjectIdentity = ObjectIdentity
pwConformance = _PwConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246, 2)
)
_PwGroups_ObjectIdentity = ObjectIdentity
pwGroups = _PwGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1)
)
_PwCompliances_ObjectIdentity = ObjectIdentity
pwCompliances = _PwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 2)
)

# Managed Objects groups

pwBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 1)
)
pwBasicGroup.setObjects(
      *(("PW-STD-MIB", "pwType"),
        ("PW-STD-MIB", "pwOwner"),
        ("PW-STD-MIB", "pwPsnType"),
        ("PW-STD-MIB", "pwIfIndex"),
        ("PW-STD-MIB", "pwCwPreference"),
        ("PW-STD-MIB", "pwLocalIfMtu"),
        ("PW-STD-MIB", "pwOutboundLabel"),
        ("PW-STD-MIB", "pwInboundLabel"),
        ("PW-STD-MIB", "pwName"),
        ("PW-STD-MIB", "pwDescr"),
        ("PW-STD-MIB", "pwCreateTime"),
        ("PW-STD-MIB", "pwUpTime"),
        ("PW-STD-MIB", "pwLastChange"),
        ("PW-STD-MIB", "pwAdminStatus"),
        ("PW-STD-MIB", "pwOperStatus"),
        ("PW-STD-MIB", "pwLocalStatus"),
        ("PW-STD-MIB", "pwRowStatus"),
        ("PW-STD-MIB", "pwStorageType"),
        ("PW-STD-MIB", "pwOamEnable"))
)
if mibBuilder.loadTexts:
    pwBasicGroup.setStatus("current")

pwPwIdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 2)
)
pwPwIdGroup.setObjects(
    ("PW-STD-MIB", "pwID")
)
if mibBuilder.loadTexts:
    pwPwIdGroup.setStatus("current")

pwGeneralizedFecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 3)
)
pwGeneralizedFecGroup.setObjects(
      *(("PW-STD-MIB", "pwGroupAttachmentID"),
        ("PW-STD-MIB", "pwLocalAttachmentID"),
        ("PW-STD-MIB", "pwRemoteAttachmentID"),
        ("PW-STD-MIB", "pwGenAGIType"),
        ("PW-STD-MIB", "pwGenLocalAIIType"),
        ("PW-STD-MIB", "pwGenRemoteAIIType"))
)
if mibBuilder.loadTexts:
    pwGeneralizedFecGroup.setStatus("current")

pwFcsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 4)
)
pwFcsGroup.setObjects(
      *(("PW-STD-MIB", "pwFcsRetentionCfg"),
        ("PW-STD-MIB", "pwFcsRetentionStatus"))
)
if mibBuilder.loadTexts:
    pwFcsGroup.setStatus("current")

pwFragGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 5)
)
pwFragGroup.setObjects(
      *(("PW-STD-MIB", "pwFragmentCfgSize"),
        ("PW-STD-MIB", "pwRmtFragCapability"))
)
if mibBuilder.loadTexts:
    pwFragGroup.setStatus("current")

pwPwStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 6)
)
pwPwStatusGroup.setObjects(
      *(("PW-STD-MIB", "pwRemoteCapabilities"),
        ("PW-STD-MIB", "pwRemoteStatusCapable"),
        ("PW-STD-MIB", "pwRemoteStatus"))
)
if mibBuilder.loadTexts:
    pwPwStatusGroup.setStatus("current")

pwGetNextGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 7)
)
pwGetNextGroup.setObjects(
    ("PW-STD-MIB", "pwIndexNext")
)
if mibBuilder.loadTexts:
    pwGetNextGroup.setStatus("current")

pwPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 8)
)
pwPriorityGroup.setObjects(
      *(("PW-STD-MIB", "pwSetUpPriority"),
        ("PW-STD-MIB", "pwHoldingPriority"))
)
if mibBuilder.loadTexts:
    pwPriorityGroup.setStatus("current")

pwAttachmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 9)
)
pwAttachmentGroup.setObjects(
    ("PW-STD-MIB", "pwAttachedPwIndex")
)
if mibBuilder.loadTexts:
    pwAttachmentGroup.setStatus("current")

pwPerformanceGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 10)
)
pwPerformanceGeneralGroup.setObjects(
    ("PW-STD-MIB", "pwPerfTotalErrorPackets")
)
if mibBuilder.loadTexts:
    pwPerformanceGeneralGroup.setStatus("current")

pwPeformance1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 11)
)
pwPeformance1DayIntervalGroup.setObjects(
      *(("PW-STD-MIB", "pwPerf1DayIntervalValidData"),
        ("PW-STD-MIB", "pwPerf1DayIntervalTimeElapsed"),
        ("PW-STD-MIB", "pwPerf1DayIntervalInHCPackets"),
        ("PW-STD-MIB", "pwPerf1DayIntervalInHCBytes"),
        ("PW-STD-MIB", "pwPerf1DayIntervalOutHCPackets"),
        ("PW-STD-MIB", "pwPerf1DayIntervalOutHCBytes"))
)
if mibBuilder.loadTexts:
    pwPeformance1DayIntervalGroup.setStatus("current")

pwPerformanceIntervalGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 12)
)
pwPerformanceIntervalGeneralGroup.setObjects(
      *(("PW-STD-MIB", "pwTimeElapsed"),
        ("PW-STD-MIB", "pwValidIntervals"),
        ("PW-STD-MIB", "pwPerfIntervalValidData"),
        ("PW-STD-MIB", "pwPerfIntervalTimeElapsed"))
)
if mibBuilder.loadTexts:
    pwPerformanceIntervalGeneralGroup.setStatus("current")

pwPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 13)
)
pwPeformanceIntervalGroup.setObjects(
      *(("PW-STD-MIB", "pwPerfCurrentInPackets"),
        ("PW-STD-MIB", "pwPerfCurrentInBytes"),
        ("PW-STD-MIB", "pwPerfCurrentOutPackets"),
        ("PW-STD-MIB", "pwPerfCurrentOutBytes"),
        ("PW-STD-MIB", "pwPerfIntervalInPackets"),
        ("PW-STD-MIB", "pwPerfIntervalInBytes"),
        ("PW-STD-MIB", "pwPerfIntervalOutPackets"),
        ("PW-STD-MIB", "pwPerfIntervalOutBytes"))
)
if mibBuilder.loadTexts:
    pwPeformanceIntervalGroup.setStatus("current")

pwHCPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 14)
)
pwHCPeformanceIntervalGroup.setObjects(
      *(("PW-STD-MIB", "pwPerfCurrentInHCPackets"),
        ("PW-STD-MIB", "pwPerfCurrentInHCBytes"),
        ("PW-STD-MIB", "pwPerfCurrentOutHCPackets"),
        ("PW-STD-MIB", "pwPerfCurrentOutHCBytes"),
        ("PW-STD-MIB", "pwPerfIntervalInHCPackets"),
        ("PW-STD-MIB", "pwPerfIntervalInHCBytes"),
        ("PW-STD-MIB", "pwPerfIntervalOutHCPackets"),
        ("PW-STD-MIB", "pwPerfIntervalOutHCBytes"))
)
if mibBuilder.loadTexts:
    pwHCPeformanceIntervalGroup.setStatus("current")

pwMappingTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 15)
)
pwMappingTablesGroup.setObjects(
      *(("PW-STD-MIB", "pwIndexMappingPwIndex"),
        ("PW-STD-MIB", "pwPeerMappingPwIndex"),
        ("PW-STD-MIB", "pwGenFecIndexMappingPwIndex"))
)
if mibBuilder.loadTexts:
    pwMappingTablesGroup.setStatus("current")

pwNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 16)
)
pwNotificationControlGroup.setObjects(
      *(("PW-STD-MIB", "pwUpDownNotifEnable"),
        ("PW-STD-MIB", "pwDeletedNotifEnable"),
        ("PW-STD-MIB", "pwNotifRate"))
)
if mibBuilder.loadTexts:
    pwNotificationControlGroup.setStatus("current")

pwSignalingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 18)
)
pwSignalingGroup.setObjects(
      *(("PW-STD-MIB", "pwPeerAddrType"),
        ("PW-STD-MIB", "pwPeerAddr"),
        ("PW-STD-MIB", "pwLocalGroupID"),
        ("PW-STD-MIB", "pwLocalIfString"),
        ("PW-STD-MIB", "pwLocalCapabAdvert"),
        ("PW-STD-MIB", "pwRemoteGroupID"),
        ("PW-STD-MIB", "pwCwStatus"),
        ("PW-STD-MIB", "pwRemoteIfMtu"),
        ("PW-STD-MIB", "pwRemoteIfString"))
)
if mibBuilder.loadTexts:
    pwSignalingGroup.setStatus("current")


# Notification objects

pwDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 246, 0, 1)
)
pwDown.setObjects(
      *(("PW-STD-MIB", "pwOperStatus"),
        ("PW-STD-MIB", "pwOperStatus"))
)
if mibBuilder.loadTexts:
    pwDown.setStatus(
        "current"
    )

pwUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 246, 0, 2)
)
pwUp.setObjects(
      *(("PW-STD-MIB", "pwOperStatus"),
        ("PW-STD-MIB", "pwOperStatus"))
)
if mibBuilder.loadTexts:
    pwUp.setStatus(
        "current"
    )

pwDeleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 246, 0, 3)
)
pwDeleted.setObjects(
      *(("PW-STD-MIB", "pwType"),
        ("PW-STD-MIB", "pwID"),
        ("PW-STD-MIB", "pwPeerAddrType"),
        ("PW-STD-MIB", "pwPeerAddr"))
)
if mibBuilder.loadTexts:
    pwDeleted.setStatus(
        "current"
    )


# Notifications groups

pwNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 17)
)
pwNotificationGroup.setObjects(
      *(("PW-STD-MIB", "pwUp"),
        ("PW-STD-MIB", "pwDown"),
        ("PW-STD-MIB", "pwDeleted"))
)
if mibBuilder.loadTexts:
    pwNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pwModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pwModuleFullCompliance.setStatus(
        "current"
    )

pwModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 246, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pwModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-STD-MIB",
    **{"pwStdMIB": pwStdMIB,
       "pwNotifications": pwNotifications,
       "pwDown": pwDown,
       "pwUp": pwUp,
       "pwDeleted": pwDeleted,
       "pwObjects": pwObjects,
       "pwIndexNext": pwIndexNext,
       "pwTable": pwTable,
       "pwEntry": pwEntry,
       "pwIndex": pwIndex,
       "pwType": pwType,
       "pwOwner": pwOwner,
       "pwPsnType": pwPsnType,
       "pwSetUpPriority": pwSetUpPriority,
       "pwHoldingPriority": pwHoldingPriority,
       "pwPeerAddrType": pwPeerAddrType,
       "pwPeerAddr": pwPeerAddr,
       "pwAttachedPwIndex": pwAttachedPwIndex,
       "pwIfIndex": pwIfIndex,
       "pwID": pwID,
       "pwLocalGroupID": pwLocalGroupID,
       "pwGroupAttachmentID": pwGroupAttachmentID,
       "pwLocalAttachmentID": pwLocalAttachmentID,
       "pwRemoteAttachmentID": pwRemoteAttachmentID,
       "pwCwPreference": pwCwPreference,
       "pwLocalIfMtu": pwLocalIfMtu,
       "pwLocalIfString": pwLocalIfString,
       "pwLocalCapabAdvert": pwLocalCapabAdvert,
       "pwRemoteGroupID": pwRemoteGroupID,
       "pwCwStatus": pwCwStatus,
       "pwRemoteIfMtu": pwRemoteIfMtu,
       "pwRemoteIfString": pwRemoteIfString,
       "pwRemoteCapabilities": pwRemoteCapabilities,
       "pwFragmentCfgSize": pwFragmentCfgSize,
       "pwRmtFragCapability": pwRmtFragCapability,
       "pwFcsRetentionCfg": pwFcsRetentionCfg,
       "pwFcsRetentionStatus": pwFcsRetentionStatus,
       "pwOutboundLabel": pwOutboundLabel,
       "pwInboundLabel": pwInboundLabel,
       "pwName": pwName,
       "pwDescr": pwDescr,
       "pwCreateTime": pwCreateTime,
       "pwUpTime": pwUpTime,
       "pwLastChange": pwLastChange,
       "pwAdminStatus": pwAdminStatus,
       "pwOperStatus": pwOperStatus,
       "pwLocalStatus": pwLocalStatus,
       "pwRemoteStatusCapable": pwRemoteStatusCapable,
       "pwRemoteStatus": pwRemoteStatus,
       "pwTimeElapsed": pwTimeElapsed,
       "pwValidIntervals": pwValidIntervals,
       "pwRowStatus": pwRowStatus,
       "pwStorageType": pwStorageType,
       "pwOamEnable": pwOamEnable,
       "pwGenAGIType": pwGenAGIType,
       "pwGenLocalAIIType": pwGenLocalAIIType,
       "pwGenRemoteAIIType": pwGenRemoteAIIType,
       "pwPerfCurrentTable": pwPerfCurrentTable,
       "pwPerfCurrentEntry": pwPerfCurrentEntry,
       "pwPerfCurrentInHCPackets": pwPerfCurrentInHCPackets,
       "pwPerfCurrentInHCBytes": pwPerfCurrentInHCBytes,
       "pwPerfCurrentOutHCPackets": pwPerfCurrentOutHCPackets,
       "pwPerfCurrentOutHCBytes": pwPerfCurrentOutHCBytes,
       "pwPerfCurrentInPackets": pwPerfCurrentInPackets,
       "pwPerfCurrentInBytes": pwPerfCurrentInBytes,
       "pwPerfCurrentOutPackets": pwPerfCurrentOutPackets,
       "pwPerfCurrentOutBytes": pwPerfCurrentOutBytes,
       "pwPerfIntervalTable": pwPerfIntervalTable,
       "pwPerfIntervalEntry": pwPerfIntervalEntry,
       "pwPerfIntervalNumber": pwPerfIntervalNumber,
       "pwPerfIntervalValidData": pwPerfIntervalValidData,
       "pwPerfIntervalTimeElapsed": pwPerfIntervalTimeElapsed,
       "pwPerfIntervalInHCPackets": pwPerfIntervalInHCPackets,
       "pwPerfIntervalInHCBytes": pwPerfIntervalInHCBytes,
       "pwPerfIntervalOutHCPackets": pwPerfIntervalOutHCPackets,
       "pwPerfIntervalOutHCBytes": pwPerfIntervalOutHCBytes,
       "pwPerfIntervalInPackets": pwPerfIntervalInPackets,
       "pwPerfIntervalInBytes": pwPerfIntervalInBytes,
       "pwPerfIntervalOutPackets": pwPerfIntervalOutPackets,
       "pwPerfIntervalOutBytes": pwPerfIntervalOutBytes,
       "pwPerf1DayIntervalTable": pwPerf1DayIntervalTable,
       "pwPerf1DayIntervalEntry": pwPerf1DayIntervalEntry,
       "pwPerf1DayIntervalNumber": pwPerf1DayIntervalNumber,
       "pwPerf1DayIntervalValidData": pwPerf1DayIntervalValidData,
       "pwPerf1DayIntervalTimeElapsed": pwPerf1DayIntervalTimeElapsed,
       "pwPerf1DayIntervalInHCPackets": pwPerf1DayIntervalInHCPackets,
       "pwPerf1DayIntervalInHCBytes": pwPerf1DayIntervalInHCBytes,
       "pwPerf1DayIntervalOutHCPackets": pwPerf1DayIntervalOutHCPackets,
       "pwPerf1DayIntervalOutHCBytes": pwPerf1DayIntervalOutHCBytes,
       "pwPerfTotalErrorPackets": pwPerfTotalErrorPackets,
       "pwIndexMappingTable": pwIndexMappingTable,
       "pwIndexMappingEntry": pwIndexMappingEntry,
       "pwIndexMappingPwType": pwIndexMappingPwType,
       "pwIndexMappingPwID": pwIndexMappingPwID,
       "pwIndexMappingPeerAddrType": pwIndexMappingPeerAddrType,
       "pwIndexMappingPeerAddr": pwIndexMappingPeerAddr,
       "pwIndexMappingPwIndex": pwIndexMappingPwIndex,
       "pwPeerMappingTable": pwPeerMappingTable,
       "pwPeerMappingEntry": pwPeerMappingEntry,
       "pwPeerMappingPeerAddrType": pwPeerMappingPeerAddrType,
       "pwPeerMappingPeerAddr": pwPeerMappingPeerAddr,
       "pwPeerMappingPwType": pwPeerMappingPwType,
       "pwPeerMappingPwID": pwPeerMappingPwID,
       "pwPeerMappingPwIndex": pwPeerMappingPwIndex,
       "pwUpDownNotifEnable": pwUpDownNotifEnable,
       "pwDeletedNotifEnable": pwDeletedNotifEnable,
       "pwNotifRate": pwNotifRate,
       "pwGenFecIndexMappingTable": pwGenFecIndexMappingTable,
       "pwGenFecIndexMappingEntry": pwGenFecIndexMappingEntry,
       "pwGenFecIndexMappingAGIType": pwGenFecIndexMappingAGIType,
       "pwGenFecIndexMappingAGI": pwGenFecIndexMappingAGI,
       "pwGenFecIndexMappingLocalAIIType": pwGenFecIndexMappingLocalAIIType,
       "pwGenFecIndexMappingLocalAII": pwGenFecIndexMappingLocalAII,
       "pwGenFecIndexMappingRemoteAIIType": pwGenFecIndexMappingRemoteAIIType,
       "pwGenFecIndexMappingRemoteAII": pwGenFecIndexMappingRemoteAII,
       "pwGenFecIndexMappingPwIndex": pwGenFecIndexMappingPwIndex,
       "pwConformance": pwConformance,
       "pwGroups": pwGroups,
       "pwBasicGroup": pwBasicGroup,
       "pwPwIdGroup": pwPwIdGroup,
       "pwGeneralizedFecGroup": pwGeneralizedFecGroup,
       "pwFcsGroup": pwFcsGroup,
       "pwFragGroup": pwFragGroup,
       "pwPwStatusGroup": pwPwStatusGroup,
       "pwGetNextGroup": pwGetNextGroup,
       "pwPriorityGroup": pwPriorityGroup,
       "pwAttachmentGroup": pwAttachmentGroup,
       "pwPerformanceGeneralGroup": pwPerformanceGeneralGroup,
       "pwPeformance1DayIntervalGroup": pwPeformance1DayIntervalGroup,
       "pwPerformanceIntervalGeneralGroup": pwPerformanceIntervalGeneralGroup,
       "pwPeformanceIntervalGroup": pwPeformanceIntervalGroup,
       "pwHCPeformanceIntervalGroup": pwHCPeformanceIntervalGroup,
       "pwMappingTablesGroup": pwMappingTablesGroup,
       "pwNotificationControlGroup": pwNotificationControlGroup,
       "pwNotificationGroup": pwNotificationGroup,
       "pwSignalingGroup": pwSignalingGroup,
       "pwCompliances": pwCompliances,
       "pwModuleFullCompliance": pwModuleFullCompliance,
       "pwModuleReadOnlyCompliance": pwModuleReadOnlyCompliance}
)
