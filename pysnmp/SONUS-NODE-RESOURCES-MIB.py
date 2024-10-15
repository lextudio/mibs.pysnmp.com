# SNMP MIB module (SONUS-NODE-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-NODE-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:04 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")

(SonusAdminState,
 SonusName,
 SonusNameReference) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusName",
    "SonusNameReference")


# MODULE-IDENTITY

sonusNodeResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusNodeResourcesMIBObjects_ObjectIdentity = ObjectIdentity
sonusNodeResourcesMIBObjects = _SonusNodeResourcesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1)
)
_SonusServProfile_ObjectIdentity = ObjectIdentity
sonusServProfile = _SonusServProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1)
)
_SonusServProfileNextIndex_Type = Integer32
_SonusServProfileNextIndex_Object = MibScalar
sonusServProfileNextIndex = _SonusServProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 1),
    _SonusServProfileNextIndex_Type()
)
sonusServProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusServProfileNextIndex.setStatus("deprecated")
_SonusServProfileTable_Object = MibTable
sonusServProfileTable = _SonusServProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusServProfileTable.setStatus("deprecated")
_SonusServProfileEntry_Object = MibTableRow
sonusServProfileEntry = _SonusServProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1)
)
sonusServProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusServProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusServProfileEntry.setStatus("deprecated")
_SonusServProfileIndex_Type = Integer32
_SonusServProfileIndex_Object = MibTableColumn
sonusServProfileIndex = _SonusServProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 1),
    _SonusServProfileIndex_Type()
)
sonusServProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusServProfileIndex.setStatus("deprecated")


class _SonusServProfileState_Type(Integer32):
    """Custom type sonusServProfileState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusServProfileState_Type.__name__ = "Integer32"
_SonusServProfileState_Object = MibTableColumn
sonusServProfileState = _SonusServProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 2),
    _SonusServProfileState_Type()
)
sonusServProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileState.setStatus("deprecated")
_SonusServProfileName_Type = SonusName
_SonusServProfileName_Object = MibTableColumn
sonusServProfileName = _SonusServProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 3),
    _SonusServProfileName_Type()
)
sonusServProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileName.setStatus("deprecated")


class _SonusServProfileType_Type(Integer32):
    """Custom type sonusServProfileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("packet", 2))
    )


_SonusServProfileType_Type.__name__ = "Integer32"
_SonusServProfileType_Object = MibTableColumn
sonusServProfileType = _SonusServProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 4),
    _SonusServProfileType_Type()
)
sonusServProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileType.setStatus("deprecated")


class _SonusServProfileVCktEncoding_Type(Integer32):
    """Custom type sonusServProfileVCktEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 2),
          ("g711ulaw", 1),
          ("none", 5))
    )


_SonusServProfileVCktEncoding_Type.__name__ = "Integer32"
_SonusServProfileVCktEncoding_Object = MibTableColumn
sonusServProfileVCktEncoding = _SonusServProfileVCktEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 5),
    _SonusServProfileVCktEncoding_Type()
)
sonusServProfileVCktEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVCktEncoding.setStatus("deprecated")


class _SonusServProfileVCktBandwidth_Type(Integer32):
    """Custom type sonusServProfileVCktBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusServProfileVCktBandwidth_Type.__name__ = "Integer32"
_SonusServProfileVCktBandwidth_Object = MibTableColumn
sonusServProfileVCktBandwidth = _SonusServProfileVCktBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 6),
    _SonusServProfileVCktBandwidth_Type()
)
sonusServProfileVCktBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVCktBandwidth.setStatus("deprecated")


class _SonusServProfileVCktNecEnable_Type(Integer32):
    """Custom type sonusServProfileVCktNecEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusServProfileVCktNecEnable_Type.__name__ = "Integer32"
_SonusServProfileVCktNecEnable_Object = MibTableColumn
sonusServProfileVCktNecEnable = _SonusServProfileVCktNecEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 7),
    _SonusServProfileVCktNecEnable_Type()
)
sonusServProfileVCktNecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVCktNecEnable.setStatus("deprecated")


class _SonusServProfileVPktEncoding_Type(Integer32):
    """Custom type sonusServProfileVPktEncoding based on Integer32"""
    defaultValue = 1

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
        *(("g711alaw", 2),
          ("g711ulaw", 1),
          ("g7231", 3),
          ("g729a", 4),
          ("none", 5))
    )


_SonusServProfileVPktEncoding_Type.__name__ = "Integer32"
_SonusServProfileVPktEncoding_Object = MibTableColumn
sonusServProfileVPktEncoding = _SonusServProfileVPktEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 8),
    _SonusServProfileVPktEncoding_Type()
)
sonusServProfileVPktEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVPktEncoding.setStatus("deprecated")


class _SonusServProfileVPktFrameSize_Type(Integer32):
    """Custom type sonusServProfileVPktFrameSize based on Integer32"""
    defaultValue = 8


_SonusServProfileVPktFrameSize_Object = MibTableColumn
sonusServProfileVPktFrameSize = _SonusServProfileVPktFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 9),
    _SonusServProfileVPktFrameSize_Type()
)
sonusServProfileVPktFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVPktFrameSize.setStatus("deprecated")


class _SonusServProfileVPktFramesPerPacket_Type(Integer32):
    """Custom type sonusServProfileVPktFramesPerPacket based on Integer32"""
    defaultValue = 10


_SonusServProfileVPktFramesPerPacket_Object = MibTableColumn
sonusServProfileVPktFramesPerPacket = _SonusServProfileVPktFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 10),
    _SonusServProfileVPktFramesPerPacket_Type()
)
sonusServProfileVPktFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVPktFramesPerPacket.setStatus("deprecated")


class _SonusServProfileVPktMaxNetworkJitter_Type(Integer32):
    """Custom type sonusServProfileVPktMaxNetworkJitter based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 400),
    )


_SonusServProfileVPktMaxNetworkJitter_Type.__name__ = "Integer32"
_SonusServProfileVPktMaxNetworkJitter_Object = MibTableColumn
sonusServProfileVPktMaxNetworkJitter = _SonusServProfileVPktMaxNetworkJitter_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 11),
    _SonusServProfileVPktMaxNetworkJitter_Type()
)
sonusServProfileVPktMaxNetworkJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVPktMaxNetworkJitter.setStatus("deprecated")


class _SonusServProfileVPktTosValue_Type(Integer32):
    """Custom type sonusServProfileVPktTosValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusServProfileVPktTosValue_Type.__name__ = "Integer32"
_SonusServProfileVPktTosValue_Object = MibTableColumn
sonusServProfileVPktTosValue = _SonusServProfileVPktTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 12),
    _SonusServProfileVPktTosValue_Type()
)
sonusServProfileVPktTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileVPktTosValue.setStatus("deprecated")


class _SonusServProfileCttTestType_Type(Integer32):
    """Custom type sonusServProfileCttTestType based on Integer32"""
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
        *(("remote2Wire", 2),
          ("remote4Wire", 3),
          ("remoteLoopback", 1))
    )


_SonusServProfileCttTestType_Type.__name__ = "Integer32"
_SonusServProfileCttTestType_Object = MibTableColumn
sonusServProfileCttTestType = _SonusServProfileCttTestType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 13),
    _SonusServProfileCttTestType_Type()
)
sonusServProfileCttTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileCttTestType.setStatus("deprecated")


class _SonusServProfileCttTimeout_Type(Integer32):
    """Custom type sonusServProfileCttTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SonusServProfileCttTimeout_Type.__name__ = "Integer32"
_SonusServProfileCttTimeout_Object = MibTableColumn
sonusServProfileCttTimeout = _SonusServProfileCttTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 14),
    _SonusServProfileCttTimeout_Type()
)
sonusServProfileCttTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileCttTimeout.setStatus("deprecated")


class _SonusServProfileCttMinDetectTime_Type(Integer32):
    """Custom type sonusServProfileCttMinDetectTime based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_SonusServProfileCttMinDetectTime_Type.__name__ = "Integer32"
_SonusServProfileCttMinDetectTime_Object = MibTableColumn
sonusServProfileCttMinDetectTime = _SonusServProfileCttMinDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 15),
    _SonusServProfileCttMinDetectTime_Type()
)
sonusServProfileCttMinDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileCttMinDetectTime.setStatus("deprecated")


class _SonusServProfileCttMinReleaseTime_Type(Integer32):
    """Custom type sonusServProfileCttMinReleaseTime based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_SonusServProfileCttMinReleaseTime_Type.__name__ = "Integer32"
_SonusServProfileCttMinReleaseTime_Object = MibTableColumn
sonusServProfileCttMinReleaseTime = _SonusServProfileCttMinReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 16),
    _SonusServProfileCttMinReleaseTime_Type()
)
sonusServProfileCttMinReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileCttMinReleaseTime.setStatus("deprecated")


class _SonusServProfileCapability_Type(Integer32):
    """Custom type sonusServProfileCapability based on Integer32"""
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
        *(("circuitModeData", 2),
          ("voiceOnly", 1),
          ("voiceOrCircuitModeData", 3))
    )


_SonusServProfileCapability_Type.__name__ = "Integer32"
_SonusServProfileCapability_Object = MibTableColumn
sonusServProfileCapability = _SonusServProfileCapability_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 17),
    _SonusServProfileCapability_Type()
)
sonusServProfileCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileCapability.setStatus("deprecated")


class _SonusServProfileDPktRestrictedCfg_Type(Integer32):
    """Custom type sonusServProfileDPktRestrictedCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 2),
          ("unrestricted", 1))
    )


_SonusServProfileDPktRestrictedCfg_Type.__name__ = "Integer32"
_SonusServProfileDPktRestrictedCfg_Object = MibTableColumn
sonusServProfileDPktRestrictedCfg = _SonusServProfileDPktRestrictedCfg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 18),
    _SonusServProfileDPktRestrictedCfg_Type()
)
sonusServProfileDPktRestrictedCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileDPktRestrictedCfg.setStatus("deprecated")


class _SonusServProfileDPktRtpPayloadType_Type(Integer32):
    """Custom type sonusServProfileDPktRtpPayloadType based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusServProfileDPktRtpPayloadType_Type.__name__ = "Integer32"
_SonusServProfileDPktRtpPayloadType_Object = MibTableColumn
sonusServProfileDPktRtpPayloadType = _SonusServProfileDPktRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 19),
    _SonusServProfileDPktRtpPayloadType_Type()
)
sonusServProfileDPktRtpPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileDPktRtpPayloadType.setStatus("deprecated")


class _SonusServProfileDPktMaxNetworkJitter_Type(Integer32):
    """Custom type sonusServProfileDPktMaxNetworkJitter based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 400),
    )


_SonusServProfileDPktMaxNetworkJitter_Type.__name__ = "Integer32"
_SonusServProfileDPktMaxNetworkJitter_Object = MibTableColumn
sonusServProfileDPktMaxNetworkJitter = _SonusServProfileDPktMaxNetworkJitter_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 20),
    _SonusServProfileDPktMaxNetworkJitter_Type()
)
sonusServProfileDPktMaxNetworkJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileDPktMaxNetworkJitter.setStatus("deprecated")
_SonusServProfileRowStatus_Type = RowStatus
_SonusServProfileRowStatus_Object = MibTableColumn
sonusServProfileRowStatus = _SonusServProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 1, 2, 1, 21),
    _SonusServProfileRowStatus_Type()
)
sonusServProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusServProfileRowStatus.setStatus("deprecated")
_SonusSonicBusStatTable_Object = MibTable
sonusSonicBusStatTable = _SonusSonicBusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sonusSonicBusStatTable.setStatus("current")
_SonusSonicBusStatEntry_Object = MibTableRow
sonusSonicBusStatEntry = _SonusSonicBusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2, 1)
)
sonusSonicBusStatEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusSonicBusStatShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonicBusStatEntry.setStatus("current")


class _SonusSonicBusStatShelfIndex_Type(Integer32):
    """Custom type sonusSonicBusStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSonicBusStatShelfIndex_Type.__name__ = "Integer32"
_SonusSonicBusStatShelfIndex_Object = MibTableColumn
sonusSonicBusStatShelfIndex = _SonusSonicBusStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2, 1, 1),
    _SonusSonicBusStatShelfIndex_Type()
)
sonusSonicBusStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonicBusStatShelfIndex.setStatus("current")
_SonusSonicBusStatNumCalls_Type = Integer32
_SonusSonicBusStatNumCalls_Object = MibTableColumn
sonusSonicBusStatNumCalls = _SonusSonicBusStatNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2, 1, 2),
    _SonusSonicBusStatNumCalls_Type()
)
sonusSonicBusStatNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonicBusStatNumCalls.setStatus("current")
_SonusSonicBusStatBwAllocated_Type = Integer32
_SonusSonicBusStatBwAllocated_Object = MibTableColumn
sonusSonicBusStatBwAllocated = _SonusSonicBusStatBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2, 1, 3),
    _SonusSonicBusStatBwAllocated_Type()
)
sonusSonicBusStatBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonicBusStatBwAllocated.setStatus("current")
_SonusSonicBusStatSduCount_Type = Integer32
_SonusSonicBusStatSduCount_Object = MibTableColumn
sonusSonicBusStatSduCount = _SonusSonicBusStatSduCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 2, 1, 4),
    _SonusSonicBusStatSduCount_Type()
)
sonusSonicBusStatSduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonicBusStatSduCount.setStatus("current")
_SonusActiveCallTable_Object = MibTable
sonusActiveCallTable = _SonusActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sonusActiveCallTable.setStatus("current")
_SonusActiveCallEntry_Object = MibTableRow
sonusActiveCallEntry = _SonusActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1)
)
sonusActiveCallEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusActiveCallShelfIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusActiveCallSlotIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusActiveCallIndex"),
)
if mibBuilder.loadTexts:
    sonusActiveCallEntry.setStatus("current")


class _SonusActiveCallShelfIndex_Type(Integer32):
    """Custom type sonusActiveCallShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusActiveCallShelfIndex_Type.__name__ = "Integer32"
_SonusActiveCallShelfIndex_Object = MibTableColumn
sonusActiveCallShelfIndex = _SonusActiveCallShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 1),
    _SonusActiveCallShelfIndex_Type()
)
sonusActiveCallShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallShelfIndex.setStatus("current")


class _SonusActiveCallSlotIndex_Type(Integer32):
    """Custom type sonusActiveCallSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusActiveCallSlotIndex_Type.__name__ = "Integer32"
_SonusActiveCallSlotIndex_Object = MibTableColumn
sonusActiveCallSlotIndex = _SonusActiveCallSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 2),
    _SonusActiveCallSlotIndex_Type()
)
sonusActiveCallSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallSlotIndex.setStatus("current")
_SonusActiveCallIndex_Type = Integer32
_SonusActiveCallIndex_Object = MibTableColumn
sonusActiveCallIndex = _SonusActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 3),
    _SonusActiveCallIndex_Type()
)
sonusActiveCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIndex.setStatus("current")
_SonusActiveCallId_Type = Integer32
_SonusActiveCallId_Object = MibTableColumn
sonusActiveCallId = _SonusActiveCallId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 4),
    _SonusActiveCallId_Type()
)
sonusActiveCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallId.setStatus("current")
_SonusActiveCallSonicBusUnitsAllocated_Type = Integer32
_SonusActiveCallSonicBusUnitsAllocated_Object = MibTableColumn
sonusActiveCallSonicBusUnitsAllocated = _SonusActiveCallSonicBusUnitsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 5),
    _SonusActiveCallSonicBusUnitsAllocated_Type()
)
sonusActiveCallSonicBusUnitsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallSonicBusUnitsAllocated.setStatus("current")
_SonusActiveCallNumResources_Type = Integer32
_SonusActiveCallNumResources_Object = MibTableColumn
sonusActiveCallNumResources = _SonusActiveCallNumResources_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 6),
    _SonusActiveCallNumResources_Type()
)
sonusActiveCallNumResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallNumResources.setStatus("current")


class _SonusActiveCallState_Type(DisplayString):
    """Custom type sonusActiveCallState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallState_Type.__name__ = "DisplayString"
_SonusActiveCallState_Object = MibTableColumn
sonusActiveCallState = _SonusActiveCallState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 7),
    _SonusActiveCallState_Type()
)
sonusActiveCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallState.setStatus("current")


class _SonusActiveCallIngressServProfile_Type(DisplayString):
    """Custom type sonusActiveCallIngressServProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallIngressServProfile_Type.__name__ = "DisplayString"
_SonusActiveCallIngressServProfile_Object = MibTableColumn
sonusActiveCallIngressServProfile = _SonusActiveCallIngressServProfile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 8),
    _SonusActiveCallIngressServProfile_Type()
)
sonusActiveCallIngressServProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressServProfile.setStatus("current")


class _SonusActiveCallEgressServProfile_Type(DisplayString):
    """Custom type sonusActiveCallEgressServProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallEgressServProfile_Type.__name__ = "DisplayString"
_SonusActiveCallEgressServProfile_Object = MibTableColumn
sonusActiveCallEgressServProfile = _SonusActiveCallEgressServProfile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 9),
    _SonusActiveCallEgressServProfile_Type()
)
sonusActiveCallEgressServProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressServProfile.setStatus("current")


class _SonusActiveCallCallingNum_Type(DisplayString):
    """Custom type sonusActiveCallCallingNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusActiveCallCallingNum_Type.__name__ = "DisplayString"
_SonusActiveCallCallingNum_Object = MibTableColumn
sonusActiveCallCallingNum = _SonusActiveCallCallingNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 10),
    _SonusActiveCallCallingNum_Type()
)
sonusActiveCallCallingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallCallingNum.setStatus("current")


class _SonusActiveCallCalledNum_Type(DisplayString):
    """Custom type sonusActiveCallCalledNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusActiveCallCalledNum_Type.__name__ = "DisplayString"
_SonusActiveCallCalledNum_Object = MibTableColumn
sonusActiveCallCalledNum = _SonusActiveCallCalledNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 11),
    _SonusActiveCallCalledNum_Type()
)
sonusActiveCallCalledNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallCalledNum.setStatus("current")


class _SonusActiveCallAddressTransPerformed_Type(Integer32):
    """Custom type sonusActiveCallAddressTransPerformed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lnp", 2),
          ("none", 1),
          ("tollfree", 3))
    )


_SonusActiveCallAddressTransPerformed_Type.__name__ = "Integer32"
_SonusActiveCallAddressTransPerformed_Object = MibTableColumn
sonusActiveCallAddressTransPerformed = _SonusActiveCallAddressTransPerformed_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 12),
    _SonusActiveCallAddressTransPerformed_Type()
)
sonusActiveCallAddressTransPerformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallAddressTransPerformed.setStatus("current")


class _SonusActiveCallOrigCalledNum_Type(DisplayString):
    """Custom type sonusActiveCallOrigCalledNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusActiveCallOrigCalledNum_Type.__name__ = "DisplayString"
_SonusActiveCallOrigCalledNum_Object = MibTableColumn
sonusActiveCallOrigCalledNum = _SonusActiveCallOrigCalledNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 13),
    _SonusActiveCallOrigCalledNum_Type()
)
sonusActiveCallOrigCalledNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallOrigCalledNum.setStatus("current")


class _SonusActiveCallScenarioType_Type(DisplayString):
    """Custom type sonusActiveCallScenarioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallScenarioType_Type.__name__ = "DisplayString"
_SonusActiveCallScenarioType_Object = MibTableColumn
sonusActiveCallScenarioType = _SonusActiveCallScenarioType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 14),
    _SonusActiveCallScenarioType_Type()
)
sonusActiveCallScenarioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallScenarioType.setStatus("current")


class _SonusActiveCallIngressPstnSlotNum_Type(Integer32):
    """Custom type sonusActiveCallIngressPstnSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusActiveCallIngressPstnSlotNum_Type.__name__ = "Integer32"
_SonusActiveCallIngressPstnSlotNum_Object = MibTableColumn
sonusActiveCallIngressPstnSlotNum = _SonusActiveCallIngressPstnSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 15),
    _SonusActiveCallIngressPstnSlotNum_Type()
)
sonusActiveCallIngressPstnSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnSlotNum.setStatus("current")


class _SonusActiveCallIngressPstnPortNum_Type(Integer32):
    """Custom type sonusActiveCallIngressPstnPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SonusActiveCallIngressPstnPortNum_Type.__name__ = "Integer32"
_SonusActiveCallIngressPstnPortNum_Object = MibTableColumn
sonusActiveCallIngressPstnPortNum = _SonusActiveCallIngressPstnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 16),
    _SonusActiveCallIngressPstnPortNum_Type()
)
sonusActiveCallIngressPstnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnPortNum.setStatus("current")


class _SonusActiveCallIngressPstnChannelNum_Type(Integer32):
    """Custom type sonusActiveCallIngressPstnChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusActiveCallIngressPstnChannelNum_Type.__name__ = "Integer32"
_SonusActiveCallIngressPstnChannelNum_Object = MibTableColumn
sonusActiveCallIngressPstnChannelNum = _SonusActiveCallIngressPstnChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 17),
    _SonusActiveCallIngressPstnChannelNum_Type()
)
sonusActiveCallIngressPstnChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnChannelNum.setStatus("current")


class _SonusActiveCallIngressPstnChannelCount_Type(Integer32):
    """Custom type sonusActiveCallIngressPstnChannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusActiveCallIngressPstnChannelCount_Type.__name__ = "Integer32"
_SonusActiveCallIngressPstnChannelCount_Object = MibTableColumn
sonusActiveCallIngressPstnChannelCount = _SonusActiveCallIngressPstnChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 18),
    _SonusActiveCallIngressPstnChannelCount_Type()
)
sonusActiveCallIngressPstnChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnChannelCount.setStatus("current")
_SonusActiveCallIngressPstnChannelBitMap_Type = Integer32
_SonusActiveCallIngressPstnChannelBitMap_Object = MibTableColumn
sonusActiveCallIngressPstnChannelBitMap = _SonusActiveCallIngressPstnChannelBitMap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 19),
    _SonusActiveCallIngressPstnChannelBitMap_Type()
)
sonusActiveCallIngressPstnChannelBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnChannelBitMap.setStatus("current")


class _SonusActiveCallEgressPstnSlotNum_Type(Integer32):
    """Custom type sonusActiveCallEgressPstnSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusActiveCallEgressPstnSlotNum_Type.__name__ = "Integer32"
_SonusActiveCallEgressPstnSlotNum_Object = MibTableColumn
sonusActiveCallEgressPstnSlotNum = _SonusActiveCallEgressPstnSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 20),
    _SonusActiveCallEgressPstnSlotNum_Type()
)
sonusActiveCallEgressPstnSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnSlotNum.setStatus("current")


class _SonusActiveCallEgressPstnPortNum_Type(Integer32):
    """Custom type sonusActiveCallEgressPstnPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SonusActiveCallEgressPstnPortNum_Type.__name__ = "Integer32"
_SonusActiveCallEgressPstnPortNum_Object = MibTableColumn
sonusActiveCallEgressPstnPortNum = _SonusActiveCallEgressPstnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 21),
    _SonusActiveCallEgressPstnPortNum_Type()
)
sonusActiveCallEgressPstnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnPortNum.setStatus("current")


class _SonusActiveCallEgressPstnChannelNum_Type(Integer32):
    """Custom type sonusActiveCallEgressPstnChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusActiveCallEgressPstnChannelNum_Type.__name__ = "Integer32"
_SonusActiveCallEgressPstnChannelNum_Object = MibTableColumn
sonusActiveCallEgressPstnChannelNum = _SonusActiveCallEgressPstnChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 22),
    _SonusActiveCallEgressPstnChannelNum_Type()
)
sonusActiveCallEgressPstnChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnChannelNum.setStatus("current")


class _SonusActiveCallEgressPstnChannelCount_Type(Integer32):
    """Custom type sonusActiveCallEgressPstnChannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusActiveCallEgressPstnChannelCount_Type.__name__ = "Integer32"
_SonusActiveCallEgressPstnChannelCount_Object = MibTableColumn
sonusActiveCallEgressPstnChannelCount = _SonusActiveCallEgressPstnChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 23),
    _SonusActiveCallEgressPstnChannelCount_Type()
)
sonusActiveCallEgressPstnChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnChannelCount.setStatus("current")
_SonusActiveCallEgressPstnChannelBitMap_Type = Integer32
_SonusActiveCallEgressPstnChannelBitMap_Object = MibTableColumn
sonusActiveCallEgressPstnChannelBitMap = _SonusActiveCallEgressPstnChannelBitMap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 24),
    _SonusActiveCallEgressPstnChannelBitMap_Type()
)
sonusActiveCallEgressPstnChannelBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnChannelBitMap.setStatus("current")
_SonusActiveCallIngressLocalIpSockAddr_Type = IpAddress
_SonusActiveCallIngressLocalIpSockAddr_Object = MibTableColumn
sonusActiveCallIngressLocalIpSockAddr = _SonusActiveCallIngressLocalIpSockAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 25),
    _SonusActiveCallIngressLocalIpSockAddr_Type()
)
sonusActiveCallIngressLocalIpSockAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressLocalIpSockAddr.setStatus("current")
_SonusActiveCallIngressRemoteIpSockAddr_Type = IpAddress
_SonusActiveCallIngressRemoteIpSockAddr_Object = MibTableColumn
sonusActiveCallIngressRemoteIpSockAddr = _SonusActiveCallIngressRemoteIpSockAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 26),
    _SonusActiveCallIngressRemoteIpSockAddr_Type()
)
sonusActiveCallIngressRemoteIpSockAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressRemoteIpSockAddr.setStatus("current")
_SonusActiveCallEgressLocalIpSockAddr_Type = IpAddress
_SonusActiveCallEgressLocalIpSockAddr_Object = MibTableColumn
sonusActiveCallEgressLocalIpSockAddr = _SonusActiveCallEgressLocalIpSockAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 27),
    _SonusActiveCallEgressLocalIpSockAddr_Type()
)
sonusActiveCallEgressLocalIpSockAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressLocalIpSockAddr.setStatus("current")
_SonusActiveCallEgressRemoteIpSockAddr_Type = IpAddress
_SonusActiveCallEgressRemoteIpSockAddr_Object = MibTableColumn
sonusActiveCallEgressRemoteIpSockAddr = _SonusActiveCallEgressRemoteIpSockAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 28),
    _SonusActiveCallEgressRemoteIpSockAddr_Type()
)
sonusActiveCallEgressRemoteIpSockAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressRemoteIpSockAddr.setStatus("current")


class _SonusActiveCallIngressPstnTrunk_Type(DisplayString):
    """Custom type sonusActiveCallIngressPstnTrunk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallIngressPstnTrunk_Type.__name__ = "DisplayString"
_SonusActiveCallIngressPstnTrunk_Object = MibTableColumn
sonusActiveCallIngressPstnTrunk = _SonusActiveCallIngressPstnTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 29),
    _SonusActiveCallIngressPstnTrunk_Type()
)
sonusActiveCallIngressPstnTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressPstnTrunk.setStatus("current")


class _SonusActiveCallEgressPstnTrunk_Type(DisplayString):
    """Custom type sonusActiveCallEgressPstnTrunk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallEgressPstnTrunk_Type.__name__ = "DisplayString"
_SonusActiveCallEgressPstnTrunk_Object = MibTableColumn
sonusActiveCallEgressPstnTrunk = _SonusActiveCallEgressPstnTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 30),
    _SonusActiveCallEgressPstnTrunk_Type()
)
sonusActiveCallEgressPstnTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressPstnTrunk.setStatus("current")


class _SonusActiveCallIngressIpDestGwName_Type(DisplayString):
    """Custom type sonusActiveCallIngressIpDestGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallIngressIpDestGwName_Type.__name__ = "DisplayString"
_SonusActiveCallIngressIpDestGwName_Object = MibTableColumn
sonusActiveCallIngressIpDestGwName = _SonusActiveCallIngressIpDestGwName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 31),
    _SonusActiveCallIngressIpDestGwName_Type()
)
sonusActiveCallIngressIpDestGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressIpDestGwName.setStatus("current")


class _SonusActiveCallEgressIpDestGwName_Type(DisplayString):
    """Custom type sonusActiveCallEgressIpDestGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusActiveCallEgressIpDestGwName_Type.__name__ = "DisplayString"
_SonusActiveCallEgressIpDestGwName_Object = MibTableColumn
sonusActiveCallEgressIpDestGwName = _SonusActiveCallEgressIpDestGwName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 32),
    _SonusActiveCallEgressIpDestGwName_Type()
)
sonusActiveCallEgressIpDestGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressIpDestGwName.setStatus("current")
_SonusActiveCallDuration_Type = Integer32
_SonusActiveCallDuration_Object = MibTableColumn
sonusActiveCallDuration = _SonusActiveCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 33),
    _SonusActiveCallDuration_Type()
)
sonusActiveCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallDuration.setStatus("current")


class _SonusActiveCallIngressEpType_Type(Integer32):
    """Custom type sonusActiveCallIngressEpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("packet", 2),
          ("unknown", 0))
    )


_SonusActiveCallIngressEpType_Type.__name__ = "Integer32"
_SonusActiveCallIngressEpType_Object = MibTableColumn
sonusActiveCallIngressEpType = _SonusActiveCallIngressEpType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 34),
    _SonusActiveCallIngressEpType_Type()
)
sonusActiveCallIngressEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressEpType.setStatus("current")


class _SonusActiveCallEgressEpType_Type(Integer32):
    """Custom type sonusActiveCallEgressEpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("packet", 2),
          ("unknown", 0))
    )


_SonusActiveCallEgressEpType_Type.__name__ = "Integer32"
_SonusActiveCallEgressEpType_Object = MibTableColumn
sonusActiveCallEgressEpType = _SonusActiveCallEgressEpType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 35),
    _SonusActiveCallEgressEpType_Type()
)
sonusActiveCallEgressEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressEpType.setStatus("current")


class _SonusActiveCallIngressSgType_Type(Integer32):
    """Custom type sonusActiveCallIngressSgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("asg", 9),
          ("cas", 2),
          ("gwip", 5),
          ("h323", 4),
          ("internal1", 6),
          ("internal2", 7),
          ("isdn", 3),
          ("isup", 1),
          ("mg", 8),
          ("static", 10),
          ("unknown", 0))
    )


_SonusActiveCallIngressSgType_Type.__name__ = "Integer32"
_SonusActiveCallIngressSgType_Object = MibTableColumn
sonusActiveCallIngressSgType = _SonusActiveCallIngressSgType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 36),
    _SonusActiveCallIngressSgType_Type()
)
sonusActiveCallIngressSgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallIngressSgType.setStatus("current")


class _SonusActiveCallEgressSgType_Type(Integer32):
    """Custom type sonusActiveCallEgressSgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("asg", 9),
          ("cas", 2),
          ("gwip", 5),
          ("h323", 4),
          ("internal1", 6),
          ("internal2", 7),
          ("isdn", 3),
          ("isup", 1),
          ("mg", 8),
          ("static", 10),
          ("unknown", 0))
    )


_SonusActiveCallEgressSgType_Type.__name__ = "Integer32"
_SonusActiveCallEgressSgType_Object = MibTableColumn
sonusActiveCallEgressSgType = _SonusActiveCallEgressSgType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 37),
    _SonusActiveCallEgressSgType_Type()
)
sonusActiveCallEgressSgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallEgressSgType.setStatus("current")
_SonusActiveCallPacketsSent_Type = Integer32
_SonusActiveCallPacketsSent_Object = MibTableColumn
sonusActiveCallPacketsSent = _SonusActiveCallPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 38),
    _SonusActiveCallPacketsSent_Type()
)
sonusActiveCallPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallPacketsSent.setStatus("current")
_SonusActiveCallPacketsReceived_Type = Integer32
_SonusActiveCallPacketsReceived_Object = MibTableColumn
sonusActiveCallPacketsReceived = _SonusActiveCallPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 39),
    _SonusActiveCallPacketsReceived_Type()
)
sonusActiveCallPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallPacketsReceived.setStatus("current")
_SonusActiveCallOctetsSent_Type = Integer32
_SonusActiveCallOctetsSent_Object = MibTableColumn
sonusActiveCallOctetsSent = _SonusActiveCallOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 40),
    _SonusActiveCallOctetsSent_Type()
)
sonusActiveCallOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallOctetsSent.setStatus("current")
_SonusActiveCallOctetsReceived_Type = Integer32
_SonusActiveCallOctetsReceived_Object = MibTableColumn
sonusActiveCallOctetsReceived = _SonusActiveCallOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 41),
    _SonusActiveCallOctetsReceived_Type()
)
sonusActiveCallOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallOctetsReceived.setStatus("current")
_SonusActiveCallPacketsLost_Type = Integer32
_SonusActiveCallPacketsLost_Object = MibTableColumn
sonusActiveCallPacketsLost = _SonusActiveCallPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 42),
    _SonusActiveCallPacketsLost_Type()
)
sonusActiveCallPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallPacketsLost.setStatus("current")
_SonusActiveCallPacketsDiscarded_Type = Integer32
_SonusActiveCallPacketsDiscarded_Object = MibTableColumn
sonusActiveCallPacketsDiscarded = _SonusActiveCallPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 43),
    _SonusActiveCallPacketsDiscarded_Type()
)
sonusActiveCallPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallPacketsDiscarded.setStatus("current")
_SonusActiveCallInterarrivalJitter_Type = Integer32
_SonusActiveCallInterarrivalJitter_Object = MibTableColumn
sonusActiveCallInterarrivalJitter = _SonusActiveCallInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 44),
    _SonusActiveCallInterarrivalJitter_Type()
)
sonusActiveCallInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallInterarrivalJitter.setStatus("current")
_SonusActiveCallPacketLatency_Type = Integer32
_SonusActiveCallPacketLatency_Object = MibTableColumn
sonusActiveCallPacketLatency = _SonusActiveCallPacketLatency_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 3, 1, 45),
    _SonusActiveCallPacketLatency_Type()
)
sonusActiveCallPacketLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusActiveCallPacketLatency.setStatus("current")
_SonusCallResTable_Object = MibTable
sonusCallResTable = _SonusCallResTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sonusCallResTable.setStatus("current")
_SonusCallResEntry_Object = MibTableRow
sonusCallResEntry = _SonusCallResEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1)
)
sonusCallResEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallResShelfIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallResSlotIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallResCallIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallResIndex"),
)
if mibBuilder.loadTexts:
    sonusCallResEntry.setStatus("current")


class _SonusCallResShelfIndex_Type(Integer32):
    """Custom type sonusCallResShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusCallResShelfIndex_Type.__name__ = "Integer32"
_SonusCallResShelfIndex_Object = MibTableColumn
sonusCallResShelfIndex = _SonusCallResShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 1),
    _SonusCallResShelfIndex_Type()
)
sonusCallResShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResShelfIndex.setStatus("current")


class _SonusCallResSlotIndex_Type(Integer32):
    """Custom type sonusCallResSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusCallResSlotIndex_Type.__name__ = "Integer32"
_SonusCallResSlotIndex_Object = MibTableColumn
sonusCallResSlotIndex = _SonusCallResSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 2),
    _SonusCallResSlotIndex_Type()
)
sonusCallResSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResSlotIndex.setStatus("current")
_SonusCallResCallIndex_Type = Integer32
_SonusCallResCallIndex_Object = MibTableColumn
sonusCallResCallIndex = _SonusCallResCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 3),
    _SonusCallResCallIndex_Type()
)
sonusCallResCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResCallIndex.setStatus("current")
_SonusCallResIndex_Type = Integer32
_SonusCallResIndex_Object = MibTableColumn
sonusCallResIndex = _SonusCallResIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 4),
    _SonusCallResIndex_Type()
)
sonusCallResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResIndex.setStatus("current")
_SonusCallResId_Type = Integer32
_SonusCallResId_Object = MibTableColumn
sonusCallResId = _SonusCallResId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 5),
    _SonusCallResId_Type()
)
sonusCallResId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResId.setStatus("current")
_SonusCallResCallId_Type = Integer32
_SonusCallResCallId_Object = MibTableColumn
sonusCallResCallId = _SonusCallResCallId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 6),
    _SonusCallResCallId_Type()
)
sonusCallResCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResCallId.setStatus("current")


class _SonusCallResType_Type(Integer32):
    """Custom type sonusCallResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("aresAmq2Dsp", 15),
          ("atmres", 16),
          ("bresAtm2Sw", 8),
          ("bresDsp2Dsp", 5),
          ("bresDsp2Sonic", 6),
          ("bresIcm", 0),
          ("bresLe2Sonic", 7),
          ("bresSw2Atm", 9),
          ("bresSw2DspApps", 17),
          ("bresSw2DspCtrl", 2),
          ("bresSw2DspLocal", 3),
          ("bresSw2DspSonic", 4),
          ("bresSw2Nif", 1),
          ("dresPstn", 10),
          ("dresService", 11),
          ("pres", 12),
          ("xresCntrl", 13),
          ("xresUser", 14))
    )


_SonusCallResType_Type.__name__ = "Integer32"
_SonusCallResType_Object = MibTableColumn
sonusCallResType = _SonusCallResType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 7),
    _SonusCallResType_Type()
)
sonusCallResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResType.setStatus("current")
_SonusCallResMgrHandle_Type = Integer32
_SonusCallResMgrHandle_Object = MibTableColumn
sonusCallResMgrHandle = _SonusCallResMgrHandle_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 8),
    _SonusCallResMgrHandle_Type()
)
sonusCallResMgrHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResMgrHandle.setStatus("current")
_SonusCallResMgrShelfIndex_Type = Integer32
_SonusCallResMgrShelfIndex_Object = MibTableColumn
sonusCallResMgrShelfIndex = _SonusCallResMgrShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 9),
    _SonusCallResMgrShelfIndex_Type()
)
sonusCallResMgrShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResMgrShelfIndex.setStatus("current")
_SonusCallResMgrSlotIndex_Type = Integer32
_SonusCallResMgrSlotIndex_Object = MibTableColumn
sonusCallResMgrSlotIndex = _SonusCallResMgrSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 4, 1, 10),
    _SonusCallResMgrSlotIndex_Type()
)
sonusCallResMgrSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallResMgrSlotIndex.setStatus("current")
_SonusCallPegCountsTable_Object = MibTable
sonusCallPegCountsTable = _SonusCallPegCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    sonusCallPegCountsTable.setStatus("current")
_SonusCallPegCountsEntry_Object = MibTableRow
sonusCallPegCountsEntry = _SonusCallPegCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1)
)
sonusCallPegCountsEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallPegCountsShelfIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallPegCountsSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusCallPegCountsEntry.setStatus("current")


class _SonusCallPegCountsShelfIndex_Type(Integer32):
    """Custom type sonusCallPegCountsShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusCallPegCountsShelfIndex_Type.__name__ = "Integer32"
_SonusCallPegCountsShelfIndex_Object = MibTableColumn
sonusCallPegCountsShelfIndex = _SonusCallPegCountsShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 1),
    _SonusCallPegCountsShelfIndex_Type()
)
sonusCallPegCountsShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsShelfIndex.setStatus("current")


class _SonusCallPegCountsSlotIndex_Type(Integer32):
    """Custom type sonusCallPegCountsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusCallPegCountsSlotIndex_Type.__name__ = "Integer32"
_SonusCallPegCountsSlotIndex_Object = MibTableColumn
sonusCallPegCountsSlotIndex = _SonusCallPegCountsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 2),
    _SonusCallPegCountsSlotIndex_Type()
)
sonusCallPegCountsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsSlotIndex.setStatus("current")


class _SonusCallPegCountsReset_Type(Integer32):
    """Custom type sonusCallPegCountsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unknown", 1))
    )


_SonusCallPegCountsReset_Type.__name__ = "Integer32"
_SonusCallPegCountsReset_Object = MibTableColumn
sonusCallPegCountsReset = _SonusCallPegCountsReset_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 3),
    _SonusCallPegCountsReset_Type()
)
sonusCallPegCountsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusCallPegCountsReset.setStatus("current")
_SonusCallPegCountsAttempts_Type = Integer32
_SonusCallPegCountsAttempts_Object = MibTableColumn
sonusCallPegCountsAttempts = _SonusCallPegCountsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 4),
    _SonusCallPegCountsAttempts_Type()
)
sonusCallPegCountsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsAttempts.setStatus("current")
_SonusCallPegCountsCompletions_Type = Integer32
_SonusCallPegCountsCompletions_Object = MibTableColumn
sonusCallPegCountsCompletions = _SonusCallPegCountsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 5),
    _SonusCallPegCountsCompletions_Type()
)
sonusCallPegCountsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsCompletions.setStatus("current")
_SonusCallPegCountsActiveCalls_Type = Integer32
_SonusCallPegCountsActiveCalls_Object = MibTableColumn
sonusCallPegCountsActiveCalls = _SonusCallPegCountsActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 6),
    _SonusCallPegCountsActiveCalls_Type()
)
sonusCallPegCountsActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsActiveCalls.setStatus("current")
_SonusCallPegCountsStableCalls_Type = Integer32
_SonusCallPegCountsStableCalls_Object = MibTableColumn
sonusCallPegCountsStableCalls = _SonusCallPegCountsStableCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 7),
    _SonusCallPegCountsStableCalls_Type()
)
sonusCallPegCountsStableCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsStableCalls.setStatus("current")
_SonusCallPegCountsUpdates_Type = Integer32
_SonusCallPegCountsUpdates_Object = MibTableColumn
sonusCallPegCountsUpdates = _SonusCallPegCountsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 8),
    _SonusCallPegCountsUpdates_Type()
)
sonusCallPegCountsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsUpdates.setStatus("current")
_SonusCallPegCountsActiveCallsNonUser_Type = Integer32
_SonusCallPegCountsActiveCallsNonUser_Object = MibTableColumn
sonusCallPegCountsActiveCallsNonUser = _SonusCallPegCountsActiveCallsNonUser_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 9),
    _SonusCallPegCountsActiveCallsNonUser_Type()
)
sonusCallPegCountsActiveCallsNonUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsActiveCallsNonUser.setStatus("current")
_SonusCallPegCountsStableCallsNonUser_Type = Integer32
_SonusCallPegCountsStableCallsNonUser_Object = MibTableColumn
sonusCallPegCountsStableCallsNonUser = _SonusCallPegCountsStableCallsNonUser_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 5, 1, 10),
    _SonusCallPegCountsStableCallsNonUser_Type()
)
sonusCallPegCountsStableCallsNonUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallPegCountsStableCallsNonUser.setStatus("current")
_SonusToneObjects_ObjectIdentity = ObjectIdentity
sonusToneObjects = _SonusToneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6)
)
_SonusToneProfile_ObjectIdentity = ObjectIdentity
sonusToneProfile = _SonusToneProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1)
)
_SonusToneProfileNextIndex_Type = Integer32
_SonusToneProfileNextIndex_Object = MibScalar
sonusToneProfileNextIndex = _SonusToneProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 1),
    _SonusToneProfileNextIndex_Type()
)
sonusToneProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusToneProfileNextIndex.setStatus("current")
_SonusToneProfileTable_Object = MibTable
sonusToneProfileTable = _SonusToneProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    sonusToneProfileTable.setStatus("current")
_SonusToneProfileEntry_Object = MibTableRow
sonusToneProfileEntry = _SonusToneProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1)
)
sonusToneProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusToneProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusToneProfileEntry.setStatus("current")
_SonusToneProfileIndex_Type = Integer32
_SonusToneProfileIndex_Object = MibTableColumn
sonusToneProfileIndex = _SonusToneProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 1),
    _SonusToneProfileIndex_Type()
)
sonusToneProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusToneProfileIndex.setStatus("current")
_SonusToneProfileName_Type = SonusName
_SonusToneProfileName_Object = MibTableColumn
sonusToneProfileName = _SonusToneProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 2),
    _SonusToneProfileName_Type()
)
sonusToneProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileName.setStatus("current")


class _SonusToneProfileGenerationMethod_Type(Integer32):
    """Custom type sonusToneProfileGenerationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualTone", 2),
          ("modulatedTone", 3),
          ("singleTone", 1))
    )


_SonusToneProfileGenerationMethod_Type.__name__ = "Integer32"
_SonusToneProfileGenerationMethod_Object = MibTableColumn
sonusToneProfileGenerationMethod = _SonusToneProfileGenerationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 3),
    _SonusToneProfileGenerationMethod_Type()
)
sonusToneProfileGenerationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileGenerationMethod.setStatus("current")


class _SonusToneProfileTone1Freq_Type(Integer32):
    """Custom type sonusToneProfileTone1Freq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3999),
    )


_SonusToneProfileTone1Freq_Type.__name__ = "Integer32"
_SonusToneProfileTone1Freq_Object = MibTableColumn
sonusToneProfileTone1Freq = _SonusToneProfileTone1Freq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 4),
    _SonusToneProfileTone1Freq_Type()
)
sonusToneProfileTone1Freq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileTone1Freq.setStatus("current")


class _SonusToneProfileTone1Power_Type(Integer32):
    """Custom type sonusToneProfileTone1Power based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 3),
    )


_SonusToneProfileTone1Power_Type.__name__ = "Integer32"
_SonusToneProfileTone1Power_Object = MibTableColumn
sonusToneProfileTone1Power = _SonusToneProfileTone1Power_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 5),
    _SonusToneProfileTone1Power_Type()
)
sonusToneProfileTone1Power.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileTone1Power.setStatus("current")


class _SonusToneProfileTone2Freq_Type(Integer32):
    """Custom type sonusToneProfileTone2Freq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3999),
    )


_SonusToneProfileTone2Freq_Type.__name__ = "Integer32"
_SonusToneProfileTone2Freq_Object = MibTableColumn
sonusToneProfileTone2Freq = _SonusToneProfileTone2Freq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 6),
    _SonusToneProfileTone2Freq_Type()
)
sonusToneProfileTone2Freq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileTone2Freq.setStatus("current")


class _SonusToneProfileTone2Power_Type(Integer32):
    """Custom type sonusToneProfileTone2Power based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 3),
    )


_SonusToneProfileTone2Power_Type.__name__ = "Integer32"
_SonusToneProfileTone2Power_Object = MibTableColumn
sonusToneProfileTone2Power = _SonusToneProfileTone2Power_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 7),
    _SonusToneProfileTone2Power_Type()
)
sonusToneProfileTone2Power.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileTone2Power.setStatus("current")


class _SonusToneProfileCarrierFreq_Type(Integer32):
    """Custom type sonusToneProfileCarrierFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3999),
    )


_SonusToneProfileCarrierFreq_Type.__name__ = "Integer32"
_SonusToneProfileCarrierFreq_Object = MibTableColumn
sonusToneProfileCarrierFreq = _SonusToneProfileCarrierFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 8),
    _SonusToneProfileCarrierFreq_Type()
)
sonusToneProfileCarrierFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileCarrierFreq.setStatus("current")


class _SonusToneProfileSignalFreq_Type(Integer32):
    """Custom type sonusToneProfileSignalFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3999),
    )


_SonusToneProfileSignalFreq_Type.__name__ = "Integer32"
_SonusToneProfileSignalFreq_Object = MibTableColumn
sonusToneProfileSignalFreq = _SonusToneProfileSignalFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 9),
    _SonusToneProfileSignalFreq_Type()
)
sonusToneProfileSignalFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileSignalFreq.setStatus("current")


class _SonusToneProfileModPower_Type(Integer32):
    """Custom type sonusToneProfileModPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 3),
    )


_SonusToneProfileModPower_Type.__name__ = "Integer32"
_SonusToneProfileModPower_Object = MibTableColumn
sonusToneProfileModPower = _SonusToneProfileModPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 10),
    _SonusToneProfileModPower_Type()
)
sonusToneProfileModPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileModPower.setStatus("current")


class _SonusToneProfileModIndex_Type(Integer32):
    """Custom type sonusToneProfileModIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SonusToneProfileModIndex_Type.__name__ = "Integer32"
_SonusToneProfileModIndex_Object = MibTableColumn
sonusToneProfileModIndex = _SonusToneProfileModIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 11),
    _SonusToneProfileModIndex_Type()
)
sonusToneProfileModIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileModIndex.setStatus("current")


class _SonusToneProfileMake1_Type(Integer32):
    """Custom type sonusToneProfileMake1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileMake1_Type.__name__ = "Integer32"
_SonusToneProfileMake1_Object = MibTableColumn
sonusToneProfileMake1 = _SonusToneProfileMake1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 12),
    _SonusToneProfileMake1_Type()
)
sonusToneProfileMake1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileMake1.setStatus("current")


class _SonusToneProfileBreak1_Type(Integer32):
    """Custom type sonusToneProfileBreak1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileBreak1_Type.__name__ = "Integer32"
_SonusToneProfileBreak1_Object = MibTableColumn
sonusToneProfileBreak1 = _SonusToneProfileBreak1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 13),
    _SonusToneProfileBreak1_Type()
)
sonusToneProfileBreak1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileBreak1.setStatus("current")


class _SonusToneProfileMake2_Type(Integer32):
    """Custom type sonusToneProfileMake2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileMake2_Type.__name__ = "Integer32"
_SonusToneProfileMake2_Object = MibTableColumn
sonusToneProfileMake2 = _SonusToneProfileMake2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 14),
    _SonusToneProfileMake2_Type()
)
sonusToneProfileMake2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileMake2.setStatus("current")


class _SonusToneProfileBreak2_Type(Integer32):
    """Custom type sonusToneProfileBreak2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileBreak2_Type.__name__ = "Integer32"
_SonusToneProfileBreak2_Object = MibTableColumn
sonusToneProfileBreak2 = _SonusToneProfileBreak2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 15),
    _SonusToneProfileBreak2_Type()
)
sonusToneProfileBreak2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileBreak2.setStatus("current")


class _SonusToneProfileMake3_Type(Integer32):
    """Custom type sonusToneProfileMake3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileMake3_Type.__name__ = "Integer32"
_SonusToneProfileMake3_Object = MibTableColumn
sonusToneProfileMake3 = _SonusToneProfileMake3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 16),
    _SonusToneProfileMake3_Type()
)
sonusToneProfileMake3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileMake3.setStatus("current")


class _SonusToneProfileBreak3_Type(Integer32):
    """Custom type sonusToneProfileBreak3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_SonusToneProfileBreak3_Type.__name__ = "Integer32"
_SonusToneProfileBreak3_Object = MibTableColumn
sonusToneProfileBreak3 = _SonusToneProfileBreak3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 17),
    _SonusToneProfileBreak3_Type()
)
sonusToneProfileBreak3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileBreak3.setStatus("current")


class _SonusToneProfileRepeat_Type(Integer32):
    """Custom type sonusToneProfileRepeat based on Integer32"""
    defaultValue = 1


_SonusToneProfileRepeat_Object = MibTableColumn
sonusToneProfileRepeat = _SonusToneProfileRepeat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 18),
    _SonusToneProfileRepeat_Type()
)
sonusToneProfileRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileRepeat.setStatus("current")
_SonusToneProfileRowStatus_Type = RowStatus
_SonusToneProfileRowStatus_Object = MibTableColumn
sonusToneProfileRowStatus = _SonusToneProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 1, 2, 1, 19),
    _SonusToneProfileRowStatus_Type()
)
sonusToneProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneProfileRowStatus.setStatus("current")
_SonusToneType_ObjectIdentity = ObjectIdentity
sonusToneType = _SonusToneType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2)
)
_SonusToneTypeNextIndex_Type = Integer32
_SonusToneTypeNextIndex_Object = MibScalar
sonusToneTypeNextIndex = _SonusToneTypeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 1),
    _SonusToneTypeNextIndex_Type()
)
sonusToneTypeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusToneTypeNextIndex.setStatus("current")
_SonusToneTypeTable_Object = MibTable
sonusToneTypeTable = _SonusToneTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    sonusToneTypeTable.setStatus("current")
_SonusToneTypeEntry_Object = MibTableRow
sonusToneTypeEntry = _SonusToneTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 2, 1)
)
sonusToneTypeEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusToneTypeIndex"),
)
if mibBuilder.loadTexts:
    sonusToneTypeEntry.setStatus("current")
_SonusToneTypeIndex_Type = Integer32
_SonusToneTypeIndex_Object = MibTableColumn
sonusToneTypeIndex = _SonusToneTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 2, 1, 1),
    _SonusToneTypeIndex_Type()
)
sonusToneTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusToneTypeIndex.setStatus("current")
_SonusToneTypeName_Type = SonusName
_SonusToneTypeName_Object = MibTableColumn
sonusToneTypeName = _SonusToneTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 2, 1, 2),
    _SonusToneTypeName_Type()
)
sonusToneTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneTypeName.setStatus("current")
_SonusToneTypeRowStatus_Type = RowStatus
_SonusToneTypeRowStatus_Object = MibTableColumn
sonusToneTypeRowStatus = _SonusToneTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 2, 2, 1, 3),
    _SonusToneTypeRowStatus_Type()
)
sonusToneTypeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusToneTypeRowStatus.setStatus("current")
_SonusTonePackage_ObjectIdentity = ObjectIdentity
sonusTonePackage = _SonusTonePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3)
)
_SonusTonePackageNextIndex_Type = Integer32
_SonusTonePackageNextIndex_Object = MibScalar
sonusTonePackageNextIndex = _SonusTonePackageNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 1),
    _SonusTonePackageNextIndex_Type()
)
sonusTonePackageNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTonePackageNextIndex.setStatus("current")
_SonusTonePackageTable_Object = MibTable
sonusTonePackageTable = _SonusTonePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    sonusTonePackageTable.setStatus("current")
_SonusTonePackageEntry_Object = MibTableRow
sonusTonePackageEntry = _SonusTonePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 2, 1)
)
sonusTonePackageEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusTonePackageIndex"),
)
if mibBuilder.loadTexts:
    sonusTonePackageEntry.setStatus("current")
_SonusTonePackageIndex_Type = Integer32
_SonusTonePackageIndex_Object = MibTableColumn
sonusTonePackageIndex = _SonusTonePackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 2, 1, 1),
    _SonusTonePackageIndex_Type()
)
sonusTonePackageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTonePackageIndex.setStatus("current")
_SonusTonePackageName_Type = SonusName
_SonusTonePackageName_Object = MibTableColumn
sonusTonePackageName = _SonusTonePackageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 2, 1, 2),
    _SonusTonePackageName_Type()
)
sonusTonePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePackageName.setStatus("current")
_SonusTonePackageRowStatus_Type = RowStatus
_SonusTonePackageRowStatus_Object = MibTableColumn
sonusTonePackageRowStatus = _SonusTonePackageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 3, 2, 1, 3),
    _SonusTonePackageRowStatus_Type()
)
sonusTonePackageRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePackageRowStatus.setStatus("current")
_SonusTonePkgElem_ObjectIdentity = ObjectIdentity
sonusTonePkgElem = _SonusTonePkgElem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4)
)
_SonusTonePkgElemTable_Object = MibTable
sonusTonePkgElemTable = _SonusTonePkgElemTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    sonusTonePkgElemTable.setStatus("current")
_SonusTonePkgElemEntry_Object = MibTableRow
sonusTonePkgElemEntry = _SonusTonePkgElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1)
)
sonusTonePkgElemEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusTonePkgElemIndex"),
)
if mibBuilder.loadTexts:
    sonusTonePkgElemEntry.setStatus("current")
_SonusTonePkgElemIndex_Type = Integer32
_SonusTonePkgElemIndex_Object = MibTableColumn
sonusTonePkgElemIndex = _SonusTonePkgElemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1, 1),
    _SonusTonePkgElemIndex_Type()
)
sonusTonePkgElemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTonePkgElemIndex.setStatus("current")
_SonusTonePkgElemTonePackageRef_Type = SonusNameReference
_SonusTonePkgElemTonePackageRef_Object = MibTableColumn
sonusTonePkgElemTonePackageRef = _SonusTonePkgElemTonePackageRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1, 2),
    _SonusTonePkgElemTonePackageRef_Type()
)
sonusTonePkgElemTonePackageRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePkgElemTonePackageRef.setStatus("current")
_SonusTonePkgElemToneTypeRef_Type = SonusNameReference
_SonusTonePkgElemToneTypeRef_Object = MibTableColumn
sonusTonePkgElemToneTypeRef = _SonusTonePkgElemToneTypeRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1, 3),
    _SonusTonePkgElemToneTypeRef_Type()
)
sonusTonePkgElemToneTypeRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePkgElemToneTypeRef.setStatus("current")


class _SonusTonePkgElemToneProfileRef_Type(SonusNameReference):
    """Custom type sonusTonePkgElemToneProfileRef based on SonusNameReference"""
    defaultValue = OctetString("default")


_SonusTonePkgElemToneProfileRef_Object = MibTableColumn
sonusTonePkgElemToneProfileRef = _SonusTonePkgElemToneProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1, 4),
    _SonusTonePkgElemToneProfileRef_Type()
)
sonusTonePkgElemToneProfileRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePkgElemToneProfileRef.setStatus("current")
_SonusTonePkgElemRowStatus_Type = RowStatus
_SonusTonePkgElemRowStatus_Object = MibTableColumn
sonusTonePkgElemRowStatus = _SonusTonePkgElemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 6, 4, 1, 1, 5),
    _SonusTonePkgElemRowStatus_Type()
)
sonusTonePkgElemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTonePkgElemRowStatus.setStatus("current")
_SonusDigitProfile_ObjectIdentity = ObjectIdentity
sonusDigitProfile = _SonusDigitProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7)
)
_SonusDigitProfileNextIndex_Type = Integer32
_SonusDigitProfileNextIndex_Object = MibScalar
sonusDigitProfileNextIndex = _SonusDigitProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 1),
    _SonusDigitProfileNextIndex_Type()
)
sonusDigitProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDigitProfileNextIndex.setStatus("current")
_SonusDigitProfileTable_Object = MibTable
sonusDigitProfileTable = _SonusDigitProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    sonusDigitProfileTable.setStatus("current")
_SonusDigitProfileEntry_Object = MibTableRow
sonusDigitProfileEntry = _SonusDigitProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1)
)
sonusDigitProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDigitProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusDigitProfileEntry.setStatus("current")
_SonusDigitProfileIndex_Type = Integer32
_SonusDigitProfileIndex_Object = MibTableColumn
sonusDigitProfileIndex = _SonusDigitProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 1),
    _SonusDigitProfileIndex_Type()
)
sonusDigitProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDigitProfileIndex.setStatus("current")
_SonusDigitProfileName_Type = SonusName
_SonusDigitProfileName_Object = MibTableColumn
sonusDigitProfileName = _SonusDigitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 2),
    _SonusDigitProfileName_Type()
)
sonusDigitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileName.setStatus("current")


class _SonusDigitProfileType_Type(Integer32):
    """Custom type sonusDigitProfileType based on Integer32"""
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
        *(("dtmf", 1),
          ("mfr1", 2),
          ("mfr2b", 4),
          ("mfr2f", 3))
    )


_SonusDigitProfileType_Type.__name__ = "Integer32"
_SonusDigitProfileType_Object = MibTableColumn
sonusDigitProfileType = _SonusDigitProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 3),
    _SonusDigitProfileType_Type()
)
sonusDigitProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileType.setStatus("current")


class _SonusDigitProfileGenPower_Type(Integer32):
    """Custom type sonusDigitProfileGenPower based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 3),
    )


_SonusDigitProfileGenPower_Type.__name__ = "Integer32"
_SonusDigitProfileGenPower_Object = MibTableColumn
sonusDigitProfileGenPower = _SonusDigitProfileGenPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 4),
    _SonusDigitProfileGenPower_Type()
)
sonusDigitProfileGenPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileGenPower.setStatus("current")


class _SonusDigitProfileGenMake_Type(Integer32):
    """Custom type sonusDigitProfileGenMake based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SonusDigitProfileGenMake_Type.__name__ = "Integer32"
_SonusDigitProfileGenMake_Object = MibTableColumn
sonusDigitProfileGenMake = _SonusDigitProfileGenMake_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 5),
    _SonusDigitProfileGenMake_Type()
)
sonusDigitProfileGenMake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileGenMake.setStatus("current")


class _SonusDigitProfileGenBreak_Type(Integer32):
    """Custom type sonusDigitProfileGenBreak based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SonusDigitProfileGenBreak_Type.__name__ = "Integer32"
_SonusDigitProfileGenBreak_Object = MibTableColumn
sonusDigitProfileGenBreak = _SonusDigitProfileGenBreak_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 6),
    _SonusDigitProfileGenBreak_Type()
)
sonusDigitProfileGenBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileGenBreak.setStatus("current")


class _SonusDigitProfileDetMinPower_Type(Integer32):
    """Custom type sonusDigitProfileDetMinPower based on Integer32"""
    defaultValue = -45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -25),
    )


_SonusDigitProfileDetMinPower_Type.__name__ = "Integer32"
_SonusDigitProfileDetMinPower_Object = MibTableColumn
sonusDigitProfileDetMinPower = _SonusDigitProfileDetMinPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 7),
    _SonusDigitProfileDetMinPower_Type()
)
sonusDigitProfileDetMinPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileDetMinPower.setStatus("current")


class _SonusDigitProfileDetMinOnDuration_Type(Integer32):
    """Custom type sonusDigitProfileDetMinOnDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_SonusDigitProfileDetMinOnDuration_Type.__name__ = "Integer32"
_SonusDigitProfileDetMinOnDuration_Object = MibTableColumn
sonusDigitProfileDetMinOnDuration = _SonusDigitProfileDetMinOnDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 8),
    _SonusDigitProfileDetMinOnDuration_Type()
)
sonusDigitProfileDetMinOnDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileDetMinOnDuration.setStatus("current")


class _SonusDigitProfileDetMinOffDuration_Type(Integer32):
    """Custom type sonusDigitProfileDetMinOffDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SonusDigitProfileDetMinOffDuration_Type.__name__ = "Integer32"
_SonusDigitProfileDetMinOffDuration_Object = MibTableColumn
sonusDigitProfileDetMinOffDuration = _SonusDigitProfileDetMinOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 9),
    _SonusDigitProfileDetMinOffDuration_Type()
)
sonusDigitProfileDetMinOffDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileDetMinOffDuration.setStatus("current")


class _SonusDigitProfileDetFreqAcceptRange_Type(Integer32):
    """Custom type sonusDigitProfileDetFreqAcceptRange based on Integer32"""
    defaultValue = 2

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
        *(("medium", 2),
          ("narrow", 1),
          ("wide", 3),
          ("wider", 4))
    )


_SonusDigitProfileDetFreqAcceptRange_Type.__name__ = "Integer32"
_SonusDigitProfileDetFreqAcceptRange_Object = MibTableColumn
sonusDigitProfileDetFreqAcceptRange = _SonusDigitProfileDetFreqAcceptRange_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 10),
    _SonusDigitProfileDetFreqAcceptRange_Type()
)
sonusDigitProfileDetFreqAcceptRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileDetFreqAcceptRange.setStatus("current")


class _SonusDigitProfileDtmfDetTwistCutoff_Type(Integer32):
    """Custom type sonusDigitProfileDtmfDetTwistCutoff based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 12),
    )


_SonusDigitProfileDtmfDetTwistCutoff_Type.__name__ = "Integer32"
_SonusDigitProfileDtmfDetTwistCutoff_Object = MibTableColumn
sonusDigitProfileDtmfDetTwistCutoff = _SonusDigitProfileDtmfDetTwistCutoff_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 11),
    _SonusDigitProfileDtmfDetTwistCutoff_Type()
)
sonusDigitProfileDtmfDetTwistCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileDtmfDetTwistCutoff.setStatus("current")


class _SonusDigitProfileMfr1GenMakeKp_Type(Integer32):
    """Custom type sonusDigitProfileMfr1GenMakeKp based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SonusDigitProfileMfr1GenMakeKp_Type.__name__ = "Integer32"
_SonusDigitProfileMfr1GenMakeKp_Object = MibTableColumn
sonusDigitProfileMfr1GenMakeKp = _SonusDigitProfileMfr1GenMakeKp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 12),
    _SonusDigitProfileMfr1GenMakeKp_Type()
)
sonusDigitProfileMfr1GenMakeKp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileMfr1GenMakeKp.setStatus("current")
_SonusDigitProfileRowStatus_Type = RowStatus
_SonusDigitProfileRowStatus_Object = MibTableColumn
sonusDigitProfileRowStatus = _SonusDigitProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 7, 2, 1, 13),
    _SonusDigitProfileRowStatus_Type()
)
sonusDigitProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDigitProfileRowStatus.setStatus("current")
_SonusStaticCall_ObjectIdentity = ObjectIdentity
sonusStaticCall = _SonusStaticCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8)
)
_SonusStaticCallNextIndex_Type = Integer32
_SonusStaticCallNextIndex_Object = MibScalar
sonusStaticCallNextIndex = _SonusStaticCallNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 1),
    _SonusStaticCallNextIndex_Type()
)
sonusStaticCallNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallNextIndex.setStatus("current")
_SonusStaticCallAdmnTable_Object = MibTable
sonusStaticCallAdmnTable = _SonusStaticCallAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sonusStaticCallAdmnTable.setStatus("current")
_SonusStaticCallAdmnEntry_Object = MibTableRow
sonusStaticCallAdmnEntry = _SonusStaticCallAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1)
)
sonusStaticCallAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusStaticCallAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEntry.setStatus("current")
_SonusStaticCallAdmnIndex_Type = Integer32
_SonusStaticCallAdmnIndex_Object = MibTableColumn
sonusStaticCallAdmnIndex = _SonusStaticCallAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 1),
    _SonusStaticCallAdmnIndex_Type()
)
sonusStaticCallAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnIndex.setStatus("current")


class _SonusStaticCallAdmnState_Type(Integer32):
    """Custom type sonusStaticCallAdmnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStaticCallAdmnState_Type.__name__ = "Integer32"
_SonusStaticCallAdmnState_Object = MibTableColumn
sonusStaticCallAdmnState = _SonusStaticCallAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 2),
    _SonusStaticCallAdmnState_Type()
)
sonusStaticCallAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnState.setStatus("current")
_SonusStaticCallAdmnName_Type = SonusName
_SonusStaticCallAdmnName_Object = MibTableColumn
sonusStaticCallAdmnName = _SonusStaticCallAdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 3),
    _SonusStaticCallAdmnName_Type()
)
sonusStaticCallAdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnName.setStatus("current")


class _SonusStaticCallAdmnEndPointAShelf_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointAShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusStaticCallAdmnEndPointAShelf_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointAShelf_Object = MibTableColumn
sonusStaticCallAdmnEndPointAShelf = _SonusStaticCallAdmnEndPointAShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 4),
    _SonusStaticCallAdmnEndPointAShelf_Type()
)
sonusStaticCallAdmnEndPointAShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointAShelf.setStatus("current")


class _SonusStaticCallAdmnEndPointASlot_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointASlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusStaticCallAdmnEndPointASlot_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointASlot_Object = MibTableColumn
sonusStaticCallAdmnEndPointASlot = _SonusStaticCallAdmnEndPointASlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 5),
    _SonusStaticCallAdmnEndPointASlot_Type()
)
sonusStaticCallAdmnEndPointASlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointASlot.setStatus("current")


class _SonusStaticCallAdmnEndPointAPort_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointAPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusStaticCallAdmnEndPointAPort_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointAPort_Object = MibTableColumn
sonusStaticCallAdmnEndPointAPort = _SonusStaticCallAdmnEndPointAPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 6),
    _SonusStaticCallAdmnEndPointAPort_Type()
)
sonusStaticCallAdmnEndPointAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointAPort.setStatus("current")


class _SonusStaticCallAdmnEndPointAChannel_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointAChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusStaticCallAdmnEndPointAChannel_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointAChannel_Object = MibTableColumn
sonusStaticCallAdmnEndPointAChannel = _SonusStaticCallAdmnEndPointAChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 7),
    _SonusStaticCallAdmnEndPointAChannel_Type()
)
sonusStaticCallAdmnEndPointAChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointAChannel.setStatus("current")
_SonusStaticCallAdmnEndPointAServProfile_Type = SonusName
_SonusStaticCallAdmnEndPointAServProfile_Object = MibTableColumn
sonusStaticCallAdmnEndPointAServProfile = _SonusStaticCallAdmnEndPointAServProfile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 8),
    _SonusStaticCallAdmnEndPointAServProfile_Type()
)
sonusStaticCallAdmnEndPointAServProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointAServProfile.setStatus("current")


class _SonusStaticCallAdmnEndPointBType_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointBType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("packet", 2))
    )


_SonusStaticCallAdmnEndPointBType_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointBType_Object = MibTableColumn
sonusStaticCallAdmnEndPointBType = _SonusStaticCallAdmnEndPointBType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 9),
    _SonusStaticCallAdmnEndPointBType_Type()
)
sonusStaticCallAdmnEndPointBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBType.setStatus("current")


class _SonusStaticCallAdmnEndPointBShelf_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointBShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusStaticCallAdmnEndPointBShelf_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointBShelf_Object = MibTableColumn
sonusStaticCallAdmnEndPointBShelf = _SonusStaticCallAdmnEndPointBShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 10),
    _SonusStaticCallAdmnEndPointBShelf_Type()
)
sonusStaticCallAdmnEndPointBShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBShelf.setStatus("current")


class _SonusStaticCallAdmnEndPointBSlot_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointBSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusStaticCallAdmnEndPointBSlot_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointBSlot_Object = MibTableColumn
sonusStaticCallAdmnEndPointBSlot = _SonusStaticCallAdmnEndPointBSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 11),
    _SonusStaticCallAdmnEndPointBSlot_Type()
)
sonusStaticCallAdmnEndPointBSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBSlot.setStatus("current")


class _SonusStaticCallAdmnEndPointBPort_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointBPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusStaticCallAdmnEndPointBPort_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointBPort_Object = MibTableColumn
sonusStaticCallAdmnEndPointBPort = _SonusStaticCallAdmnEndPointBPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 12),
    _SonusStaticCallAdmnEndPointBPort_Type()
)
sonusStaticCallAdmnEndPointBPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBPort.setStatus("current")


class _SonusStaticCallAdmnEndPointBChannel_Type(Integer32):
    """Custom type sonusStaticCallAdmnEndPointBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusStaticCallAdmnEndPointBChannel_Type.__name__ = "Integer32"
_SonusStaticCallAdmnEndPointBChannel_Object = MibTableColumn
sonusStaticCallAdmnEndPointBChannel = _SonusStaticCallAdmnEndPointBChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 13),
    _SonusStaticCallAdmnEndPointBChannel_Type()
)
sonusStaticCallAdmnEndPointBChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBChannel.setStatus("current")
_SonusStaticCallAdmnEndPointBLocalRTPPort_Type = Integer32
_SonusStaticCallAdmnEndPointBLocalRTPPort_Object = MibTableColumn
sonusStaticCallAdmnEndPointBLocalRTPPort = _SonusStaticCallAdmnEndPointBLocalRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 14),
    _SonusStaticCallAdmnEndPointBLocalRTPPort_Type()
)
sonusStaticCallAdmnEndPointBLocalRTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBLocalRTPPort.setStatus("current")
_SonusStaticCallAdmnEndPointBLocalIpAddress_Type = IpAddress
_SonusStaticCallAdmnEndPointBLocalIpAddress_Object = MibTableColumn
sonusStaticCallAdmnEndPointBLocalIpAddress = _SonusStaticCallAdmnEndPointBLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 15),
    _SonusStaticCallAdmnEndPointBLocalIpAddress_Type()
)
sonusStaticCallAdmnEndPointBLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBLocalIpAddress.setStatus("current")
_SonusStaticCallAdmnEndPointBRemoteRTPPort_Type = Integer32
_SonusStaticCallAdmnEndPointBRemoteRTPPort_Object = MibTableColumn
sonusStaticCallAdmnEndPointBRemoteRTPPort = _SonusStaticCallAdmnEndPointBRemoteRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 16),
    _SonusStaticCallAdmnEndPointBRemoteRTPPort_Type()
)
sonusStaticCallAdmnEndPointBRemoteRTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBRemoteRTPPort.setStatus("current")
_SonusStaticCallAdmnEndPointBRemoteIpAddress_Type = IpAddress
_SonusStaticCallAdmnEndPointBRemoteIpAddress_Object = MibTableColumn
sonusStaticCallAdmnEndPointBRemoteIpAddress = _SonusStaticCallAdmnEndPointBRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 17),
    _SonusStaticCallAdmnEndPointBRemoteIpAddress_Type()
)
sonusStaticCallAdmnEndPointBRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBRemoteIpAddress.setStatus("current")
_SonusStaticCallAdmnEndPointBServProfile_Type = SonusName
_SonusStaticCallAdmnEndPointBServProfile_Object = MibTableColumn
sonusStaticCallAdmnEndPointBServProfile = _SonusStaticCallAdmnEndPointBServProfile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 18),
    _SonusStaticCallAdmnEndPointBServProfile_Type()
)
sonusStaticCallAdmnEndPointBServProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnEndPointBServProfile.setStatus("current")


class _SonusStaticCallAdmnCircuitMode_Type(Integer32):
    """Custom type sonusStaticCallAdmnCircuitMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("voice", 1))
    )


_SonusStaticCallAdmnCircuitMode_Type.__name__ = "Integer32"
_SonusStaticCallAdmnCircuitMode_Object = MibTableColumn
sonusStaticCallAdmnCircuitMode = _SonusStaticCallAdmnCircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 19),
    _SonusStaticCallAdmnCircuitMode_Type()
)
sonusStaticCallAdmnCircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnCircuitMode.setStatus("current")
_SonusStaticCallAdmnRowStatus_Type = RowStatus
_SonusStaticCallAdmnRowStatus_Object = MibTableColumn
sonusStaticCallAdmnRowStatus = _SonusStaticCallAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 8, 2, 1, 20),
    _SonusStaticCallAdmnRowStatus_Type()
)
sonusStaticCallAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAdmnRowStatus.setStatus("current")
_SonusStaticCallStatTable_Object = MibTable
sonusStaticCallStatTable = _SonusStaticCallStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    sonusStaticCallStatTable.setStatus("current")
_SonusStaticCallStatEntry_Object = MibTableRow
sonusStaticCallStatEntry = _SonusStaticCallStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9, 1)
)
sonusStaticCallStatEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusStaticCallStatIndex"),
)
if mibBuilder.loadTexts:
    sonusStaticCallStatEntry.setStatus("current")
_SonusStaticCallStatIndex_Type = Integer32
_SonusStaticCallStatIndex_Object = MibTableColumn
sonusStaticCallStatIndex = _SonusStaticCallStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9, 1, 1),
    _SonusStaticCallStatIndex_Type()
)
sonusStaticCallStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallStatIndex.setStatus("current")
_SonusStaticCallStatCallId_Type = Integer32
_SonusStaticCallStatCallId_Object = MibTableColumn
sonusStaticCallStatCallId = _SonusStaticCallStatCallId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9, 1, 2),
    _SonusStaticCallStatCallId_Type()
)
sonusStaticCallStatCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallStatCallId.setStatus("current")


class _SonusStaticCallStatState_Type(DisplayString):
    """Custom type sonusStaticCallStatState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusStaticCallStatState_Type.__name__ = "DisplayString"
_SonusStaticCallStatState_Object = MibTableColumn
sonusStaticCallStatState = _SonusStaticCallStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9, 1, 3),
    _SonusStaticCallStatState_Type()
)
sonusStaticCallStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallStatState.setStatus("current")


class _SonusStaticCallStatTime_Type(DisplayString):
    """Custom type sonusStaticCallStatTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusStaticCallStatTime_Type.__name__ = "DisplayString"
_SonusStaticCallStatTime_Object = MibTableColumn
sonusStaticCallStatTime = _SonusStaticCallStatTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 9, 1, 4),
    _SonusStaticCallStatTime_Type()
)
sonusStaticCallStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStaticCallStatTime.setStatus("current")
_SonusStaticCallActionObjects_ObjectIdentity = ObjectIdentity
sonusStaticCallActionObjects = _SonusStaticCallActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 10)
)
_SonusStaticCallGcid_Type = Integer32
_SonusStaticCallGcid_Object = MibScalar
sonusStaticCallGcid = _SonusStaticCallGcid_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 10, 1),
    _SonusStaticCallGcid_Type()
)
sonusStaticCallGcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallGcid.setStatus("current")


class _SonusStaticCallAction_Type(Integer32):
    """Custom type sonusStaticCallAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("none", 1))
    )


_SonusStaticCallAction_Type.__name__ = "Integer32"
_SonusStaticCallAction_Object = MibScalar
sonusStaticCallAction = _SonusStaticCallAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 10, 2),
    _SonusStaticCallAction_Type()
)
sonusStaticCallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStaticCallAction.setStatus("current")
_SonusCallTrace_ObjectIdentity = ObjectIdentity
sonusCallTrace = _SonusCallTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11)
)
_SonusCallTraceNextIndex_Type = Integer32
_SonusCallTraceNextIndex_Object = MibScalar
sonusCallTraceNextIndex = _SonusCallTraceNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 1),
    _SonusCallTraceNextIndex_Type()
)
sonusCallTraceNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallTraceNextIndex.setStatus("current")
_SonusCallTraceTable_Object = MibTable
sonusCallTraceTable = _SonusCallTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    sonusCallTraceTable.setStatus("current")
_SonusCallTraceEntry_Object = MibTableRow
sonusCallTraceEntry = _SonusCallTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1)
)
sonusCallTraceEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCallTraceIndex"),
)
if mibBuilder.loadTexts:
    sonusCallTraceEntry.setStatus("current")
_SonusCallTraceIndex_Type = Integer32
_SonusCallTraceIndex_Object = MibTableColumn
sonusCallTraceIndex = _SonusCallTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 1),
    _SonusCallTraceIndex_Type()
)
sonusCallTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallTraceIndex.setStatus("current")


class _SonusCallTraceState_Type(Integer32):
    """Custom type sonusCallTraceState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusCallTraceState_Type.__name__ = "Integer32"
_SonusCallTraceState_Object = MibTableColumn
sonusCallTraceState = _SonusCallTraceState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 2),
    _SonusCallTraceState_Type()
)
sonusCallTraceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceState.setStatus("current")
_SonusCallTraceName_Type = SonusName
_SonusCallTraceName_Object = MibTableColumn
sonusCallTraceName = _SonusCallTraceName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 3),
    _SonusCallTraceName_Type()
)
sonusCallTraceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceName.setStatus("current")


class _SonusCallTraceType_Type(Integer32):
    """Custom type sonusCallTraceType based on Integer32"""
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
        *(("calledcalling", 1),
          ("calledonly", 2),
          ("callingonly", 3))
    )


_SonusCallTraceType_Type.__name__ = "Integer32"
_SonusCallTraceType_Object = MibTableColumn
sonusCallTraceType = _SonusCallTraceType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 4),
    _SonusCallTraceType_Type()
)
sonusCallTraceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceType.setStatus("current")


class _SonusCallTraceCalledNumber_Type(DisplayString):
    """Custom type sonusCallTraceCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusCallTraceCalledNumber_Type.__name__ = "DisplayString"
_SonusCallTraceCalledNumber_Object = MibTableColumn
sonusCallTraceCalledNumber = _SonusCallTraceCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 5),
    _SonusCallTraceCalledNumber_Type()
)
sonusCallTraceCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceCalledNumber.setStatus("current")


class _SonusCallTraceCallingNumber_Type(DisplayString):
    """Custom type sonusCallTraceCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusCallTraceCallingNumber_Type.__name__ = "DisplayString"
_SonusCallTraceCallingNumber_Object = MibTableColumn
sonusCallTraceCallingNumber = _SonusCallTraceCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 6),
    _SonusCallTraceCallingNumber_Type()
)
sonusCallTraceCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceCallingNumber.setStatus("current")


class _SonusCallTraceLevel_Type(Integer32):
    """Custom type sonusCallTraceLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3))
    )


_SonusCallTraceLevel_Type.__name__ = "Integer32"
_SonusCallTraceLevel_Object = MibTableColumn
sonusCallTraceLevel = _SonusCallTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 7),
    _SonusCallTraceLevel_Type()
)
sonusCallTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceLevel.setStatus("current")
_SonusCallTraceRowStatus_Type = RowStatus
_SonusCallTraceRowStatus_Object = MibTableColumn
sonusCallTraceRowStatus = _SonusCallTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 11, 2, 1, 8),
    _SonusCallTraceRowStatus_Type()
)
sonusCallTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCallTraceRowStatus.setStatus("current")
_SonusCktServProfile_ObjectIdentity = ObjectIdentity
sonusCktServProfile = _SonusCktServProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12)
)
_SonusCktServProfileNextIndex_Type = Integer32
_SonusCktServProfileNextIndex_Object = MibScalar
sonusCktServProfileNextIndex = _SonusCktServProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 1),
    _SonusCktServProfileNextIndex_Type()
)
sonusCktServProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCktServProfileNextIndex.setStatus("current")
_SonusCktServProfileTable_Object = MibTable
sonusCktServProfileTable = _SonusCktServProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    sonusCktServProfileTable.setStatus("current")
_SonusCktServProfileEntry_Object = MibTableRow
sonusCktServProfileEntry = _SonusCktServProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1)
)
sonusCktServProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusCktServProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusCktServProfileEntry.setStatus("current")
_SonusCktServProfileIndex_Type = Integer32
_SonusCktServProfileIndex_Object = MibTableColumn
sonusCktServProfileIndex = _SonusCktServProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 1),
    _SonusCktServProfileIndex_Type()
)
sonusCktServProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCktServProfileIndex.setStatus("current")


class _SonusCktServProfileState_Type(Integer32):
    """Custom type sonusCktServProfileState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusCktServProfileState_Type.__name__ = "Integer32"
_SonusCktServProfileState_Object = MibTableColumn
sonusCktServProfileState = _SonusCktServProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 2),
    _SonusCktServProfileState_Type()
)
sonusCktServProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileState.setStatus("current")
_SonusCktServProfileName_Type = SonusName
_SonusCktServProfileName_Object = MibTableColumn
sonusCktServProfileName = _SonusCktServProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 3),
    _SonusCktServProfileName_Type()
)
sonusCktServProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileName.setStatus("current")


class _SonusCktServProfileAudioEncoding_Type(Integer32):
    """Custom type sonusCktServProfileAudioEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 2),
          ("g711ulaw", 1))
    )


_SonusCktServProfileAudioEncoding_Type.__name__ = "Integer32"
_SonusCktServProfileAudioEncoding_Object = MibTableColumn
sonusCktServProfileAudioEncoding = _SonusCktServProfileAudioEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 4),
    _SonusCktServProfileAudioEncoding_Type()
)
sonusCktServProfileAudioEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileAudioEncoding.setStatus("current")


class _SonusCktServProfileBandwidth_Type(Integer32):
    """Custom type sonusCktServProfileBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SonusCktServProfileBandwidth_Type.__name__ = "Integer32"
_SonusCktServProfileBandwidth_Object = MibTableColumn
sonusCktServProfileBandwidth = _SonusCktServProfileBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 5),
    _SonusCktServProfileBandwidth_Type()
)
sonusCktServProfileBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileBandwidth.setStatus("current")


class _SonusCktServProfileNecEnable_Type(Integer32):
    """Custom type sonusCktServProfileNecEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusCktServProfileNecEnable_Type.__name__ = "Integer32"
_SonusCktServProfileNecEnable_Object = MibTableColumn
sonusCktServProfileNecEnable = _SonusCktServProfileNecEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 6),
    _SonusCktServProfileNecEnable_Type()
)
sonusCktServProfileNecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileNecEnable.setStatus("current")


class _SonusCktServProfileCttTestType_Type(Integer32):
    """Custom type sonusCktServProfileCttTestType based on Integer32"""
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
        *(("remote2Wire", 2),
          ("remote4Wire", 3),
          ("remoteLoopback", 1))
    )


_SonusCktServProfileCttTestType_Type.__name__ = "Integer32"
_SonusCktServProfileCttTestType_Object = MibTableColumn
sonusCktServProfileCttTestType = _SonusCktServProfileCttTestType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 7),
    _SonusCktServProfileCttTestType_Type()
)
sonusCktServProfileCttTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileCttTestType.setStatus("current")


class _SonusCktServProfileCttTimeout_Type(Integer32):
    """Custom type sonusCktServProfileCttTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SonusCktServProfileCttTimeout_Type.__name__ = "Integer32"
_SonusCktServProfileCttTimeout_Object = MibTableColumn
sonusCktServProfileCttTimeout = _SonusCktServProfileCttTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 8),
    _SonusCktServProfileCttTimeout_Type()
)
sonusCktServProfileCttTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileCttTimeout.setStatus("current")


class _SonusCktServProfileCttMinDetectTime_Type(Integer32):
    """Custom type sonusCktServProfileCttMinDetectTime based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_SonusCktServProfileCttMinDetectTime_Type.__name__ = "Integer32"
_SonusCktServProfileCttMinDetectTime_Object = MibTableColumn
sonusCktServProfileCttMinDetectTime = _SonusCktServProfileCttMinDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 9),
    _SonusCktServProfileCttMinDetectTime_Type()
)
sonusCktServProfileCttMinDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileCttMinDetectTime.setStatus("current")


class _SonusCktServProfileCttMinReleaseTime_Type(Integer32):
    """Custom type sonusCktServProfileCttMinReleaseTime based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_SonusCktServProfileCttMinReleaseTime_Type.__name__ = "Integer32"
_SonusCktServProfileCttMinReleaseTime_Object = MibTableColumn
sonusCktServProfileCttMinReleaseTime = _SonusCktServProfileCttMinReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 10),
    _SonusCktServProfileCttMinReleaseTime_Type()
)
sonusCktServProfileCttMinReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileCttMinReleaseTime.setStatus("current")


class _SonusCktServProfileCapability_Type(Integer32):
    """Custom type sonusCktServProfileCapability based on Integer32"""
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
        *(("circuitModeData", 2),
          ("voiceOnly", 1),
          ("voiceOrCircuitModeData", 3))
    )


_SonusCktServProfileCapability_Type.__name__ = "Integer32"
_SonusCktServProfileCapability_Object = MibTableColumn
sonusCktServProfileCapability = _SonusCktServProfileCapability_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 11),
    _SonusCktServProfileCapability_Type()
)
sonusCktServProfileCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileCapability.setStatus("current")


class _SonusCktServProfileDataRestrictedCfg_Type(Integer32):
    """Custom type sonusCktServProfileDataRestrictedCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 2),
          ("unrestricted", 1))
    )


_SonusCktServProfileDataRestrictedCfg_Type.__name__ = "Integer32"
_SonusCktServProfileDataRestrictedCfg_Object = MibTableColumn
sonusCktServProfileDataRestrictedCfg = _SonusCktServProfileDataRestrictedCfg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 12),
    _SonusCktServProfileDataRestrictedCfg_Type()
)
sonusCktServProfileDataRestrictedCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileDataRestrictedCfg.setStatus("current")
_SonusCktServProfileDtmfProfileName_Type = SonusNameReference
_SonusCktServProfileDtmfProfileName_Object = MibTableColumn
sonusCktServProfileDtmfProfileName = _SonusCktServProfileDtmfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 13),
    _SonusCktServProfileDtmfProfileName_Type()
)
sonusCktServProfileDtmfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileDtmfProfileName.setStatus("current")
_SonusCktServProfileRowStatus_Type = RowStatus
_SonusCktServProfileRowStatus_Object = MibTableColumn
sonusCktServProfileRowStatus = _SonusCktServProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 14),
    _SonusCktServProfileRowStatus_Type()
)
sonusCktServProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileRowStatus.setStatus("current")


class _SonusCktServProfileInterworkingXfrCap_Type(Integer32):
    """Custom type sonusCktServProfileInterworkingXfrCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio31Khz", 2),
          ("speech", 1))
    )


_SonusCktServProfileInterworkingXfrCap_Type.__name__ = "Integer32"
_SonusCktServProfileInterworkingXfrCap_Object = MibTableColumn
sonusCktServProfileInterworkingXfrCap = _SonusCktServProfileInterworkingXfrCap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 12, 2, 1, 15),
    _SonusCktServProfileInterworkingXfrCap_Type()
)
sonusCktServProfileInterworkingXfrCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCktServProfileInterworkingXfrCap.setStatus("current")
_SonusPktServProfile_ObjectIdentity = ObjectIdentity
sonusPktServProfile = _SonusPktServProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13)
)
_SonusPktServProfileNextIndex_Type = Integer32
_SonusPktServProfileNextIndex_Object = MibScalar
sonusPktServProfileNextIndex = _SonusPktServProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 1),
    _SonusPktServProfileNextIndex_Type()
)
sonusPktServProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPktServProfileNextIndex.setStatus("current")
_SonusPktServProfileTable_Object = MibTable
sonusPktServProfileTable = _SonusPktServProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    sonusPktServProfileTable.setStatus("current")
_SonusPktServProfileEntry_Object = MibTableRow
sonusPktServProfileEntry = _SonusPktServProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1)
)
sonusPktServProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusPktServProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusPktServProfileEntry.setStatus("current")
_SonusPktServProfileIndex_Type = Integer32
_SonusPktServProfileIndex_Object = MibTableColumn
sonusPktServProfileIndex = _SonusPktServProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 1),
    _SonusPktServProfileIndex_Type()
)
sonusPktServProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPktServProfileIndex.setStatus("current")


class _SonusPktServProfileState_Type(Integer32):
    """Custom type sonusPktServProfileState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileState_Type.__name__ = "Integer32"
_SonusPktServProfileState_Object = MibTableColumn
sonusPktServProfileState = _SonusPktServProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 2),
    _SonusPktServProfileState_Type()
)
sonusPktServProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileState.setStatus("current")
_SonusPktServProfileName_Type = SonusName
_SonusPktServProfileName_Object = MibTableColumn
sonusPktServProfileName = _SonusPktServProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 3),
    _SonusPktServProfileName_Type()
)
sonusPktServProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileName.setStatus("current")


class _SonusPktServProfileDestProtocol_Type(Integer32):
    """Custom type sonusPktServProfileDestProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gsx", 1),
          ("h323", 2))
    )


_SonusPktServProfileDestProtocol_Type.__name__ = "Integer32"
_SonusPktServProfileDestProtocol_Object = MibTableColumn
sonusPktServProfileDestProtocol = _SonusPktServProfileDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 4),
    _SonusPktServProfileDestProtocol_Type()
)
sonusPktServProfileDestProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDestProtocol.setStatus("current")


class _SonusPktServProfilePrfdAudioEncoding_Type(Integer32):
    """Custom type sonusPktServProfilePrfdAudioEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711", 1),
          ("g711ss", 2),
          ("g729a", 4),
          ("g729ab", 5))
    )


_SonusPktServProfilePrfdAudioEncoding_Type.__name__ = "Integer32"
_SonusPktServProfilePrfdAudioEncoding_Object = MibTableColumn
sonusPktServProfilePrfdAudioEncoding = _SonusPktServProfilePrfdAudioEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 5),
    _SonusPktServProfilePrfdAudioEncoding_Type()
)
sonusPktServProfilePrfdAudioEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfilePrfdAudioEncoding.setStatus("current")


class _SonusPktServProfilePrfdFramesPerPacket_Type(Integer32):
    """Custom type sonusPktServProfilePrfdFramesPerPacket based on Integer32"""
    defaultValue = 10


_SonusPktServProfilePrfdFramesPerPacket_Object = MibTableColumn
sonusPktServProfilePrfdFramesPerPacket = _SonusPktServProfilePrfdFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 6),
    _SonusPktServProfilePrfdFramesPerPacket_Type()
)
sonusPktServProfilePrfdFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfilePrfdFramesPerPacket.setStatus("current")


class _SonusPktServProfileDefFramesPerPacket_Type(Integer32):
    """Custom type sonusPktServProfileDefFramesPerPacket based on Integer32"""
    defaultValue = 10


_SonusPktServProfileDefFramesPerPacket_Object = MibTableColumn
sonusPktServProfileDefFramesPerPacket = _SonusPktServProfileDefFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 7),
    _SonusPktServProfileDefFramesPerPacket_Type()
)
sonusPktServProfileDefFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDefFramesPerPacket.setStatus("current")


class _SonusPktServProfileDefAudioEnable_Type(Integer32):
    """Custom type sonusPktServProfileDefAudioEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileDefAudioEnable_Type.__name__ = "Integer32"
_SonusPktServProfileDefAudioEnable_Object = MibTableColumn
sonusPktServProfileDefAudioEnable = _SonusPktServProfileDefAudioEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 8),
    _SonusPktServProfileDefAudioEnable_Type()
)
sonusPktServProfileDefAudioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDefAudioEnable.setStatus("current")


class _SonusPktServProfileSilenceFactor_Type(Integer32):
    """Custom type sonusPktServProfileSilenceFactor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SonusPktServProfileSilenceFactor_Type.__name__ = "Integer32"
_SonusPktServProfileSilenceFactor_Object = MibTableColumn
sonusPktServProfileSilenceFactor = _SonusPktServProfileSilenceFactor_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 9),
    _SonusPktServProfileSilenceFactor_Type()
)
sonusPktServProfileSilenceFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileSilenceFactor.setStatus("current")


class _SonusPktServProfileVInitPlayoutBufDelay_Type(Integer32):
    """Custom type sonusPktServProfileVInitPlayoutBufDelay based on Integer32"""
    defaultValue = 10


_SonusPktServProfileVInitPlayoutBufDelay_Object = MibTableColumn
sonusPktServProfileVInitPlayoutBufDelay = _SonusPktServProfileVInitPlayoutBufDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 10),
    _SonusPktServProfileVInitPlayoutBufDelay_Type()
)
sonusPktServProfileVInitPlayoutBufDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileVInitPlayoutBufDelay.setStatus("current")


class _SonusPktServProfileFaxRelay_Type(Integer32):
    """Custom type sonusPktServProfileFaxRelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("never", 0),
          ("useIfCompressedAudio", 1))
    )


_SonusPktServProfileFaxRelay_Type.__name__ = "Integer32"
_SonusPktServProfileFaxRelay_Object = MibTableColumn
sonusPktServProfileFaxRelay = _SonusPktServProfileFaxRelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 11),
    _SonusPktServProfileFaxRelay_Type()
)
sonusPktServProfileFaxRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileFaxRelay.setStatus("current")


class _SonusPktServProfileDtmfRelay_Type(Integer32):
    """Custom type sonusPktServProfileDtmfRelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("never", 0),
          ("useIfCompressedAudio", 1))
    )


_SonusPktServProfileDtmfRelay_Type.__name__ = "Integer32"
_SonusPktServProfileDtmfRelay_Object = MibTableColumn
sonusPktServProfileDtmfRelay = _SonusPktServProfileDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 12),
    _SonusPktServProfileDtmfRelay_Type()
)
sonusPktServProfileDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDtmfRelay.setStatus("current")


class _SonusPktServProfileFallbackHandling_Type(Integer32):
    """Custom type sonusPktServProfileFallbackHandling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("disconnet", 1))
    )


_SonusPktServProfileFallbackHandling_Type.__name__ = "Integer32"
_SonusPktServProfileFallbackHandling_Object = MibTableColumn
sonusPktServProfileFallbackHandling = _SonusPktServProfileFallbackHandling_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 13),
    _SonusPktServProfileFallbackHandling_Type()
)
sonusPktServProfileFallbackHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileFallbackHandling.setStatus("current")


class _SonusPktServProfileTosValue_Type(Integer32):
    """Custom type sonusPktServProfileTosValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusPktServProfileTosValue_Type.__name__ = "Integer32"
_SonusPktServProfileTosValue_Object = MibTableColumn
sonusPktServProfileTosValue = _SonusPktServProfileTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 14),
    _SonusPktServProfileTosValue_Type()
)
sonusPktServProfileTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileTosValue.setStatus("current")


class _SonusPktServProfileDInitPlayoutBufDelay_Type(Integer32):
    """Custom type sonusPktServProfileDInitPlayoutBufDelay based on Integer32"""
    defaultValue = 50


_SonusPktServProfileDInitPlayoutBufDelay_Object = MibTableColumn
sonusPktServProfileDInitPlayoutBufDelay = _SonusPktServProfileDInitPlayoutBufDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 15),
    _SonusPktServProfileDInitPlayoutBufDelay_Type()
)
sonusPktServProfileDInitPlayoutBufDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDInitPlayoutBufDelay.setStatus("current")


class _SonusPktServProfileDataRtpPayloadType_Type(Integer32):
    """Custom type sonusPktServProfileDataRtpPayloadType based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPktServProfileDataRtpPayloadType_Type.__name__ = "Integer32"
_SonusPktServProfileDataRtpPayloadType_Object = MibTableColumn
sonusPktServProfileDataRtpPayloadType = _SonusPktServProfileDataRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 16),
    _SonusPktServProfileDataRtpPayloadType_Type()
)
sonusPktServProfileDataRtpPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDataRtpPayloadType.setStatus("current")
_SonusPktServProfileRowStatus_Type = RowStatus
_SonusPktServProfileRowStatus_Object = MibTableColumn
sonusPktServProfileRowStatus = _SonusPktServProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 17),
    _SonusPktServProfileRowStatus_Type()
)
sonusPktServProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileRowStatus.setStatus("current")


class _SonusPktServProfileG711SendSidPackets_Type(Integer32):
    """Custom type sonusPktServProfileG711SendSidPackets based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileG711SendSidPackets_Type.__name__ = "Integer32"
_SonusPktServProfileG711SendSidPackets_Object = MibTableColumn
sonusPktServProfileG711SendSidPackets = _SonusPktServProfileG711SendSidPackets_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 18),
    _SonusPktServProfileG711SendSidPackets_Type()
)
sonusPktServProfileG711SendSidPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileG711SendSidPackets.setStatus("current")


class _SonusPktServProfileG711SidRtpPayloadType_Type(Integer32):
    """Custom type sonusPktServProfileG711SidRtpPayloadType based on Integer32"""
    defaultValue = 19

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPktServProfileG711SidRtpPayloadType_Type.__name__ = "Integer32"
_SonusPktServProfileG711SidRtpPayloadType_Object = MibTableColumn
sonusPktServProfileG711SidRtpPayloadType = _SonusPktServProfileG711SidRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 19),
    _SonusPktServProfileG711SidRtpPayloadType_Type()
)
sonusPktServProfileG711SidRtpPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileG711SidRtpPayloadType.setStatus("current")


class _SonusPktServProfileSidHeartbeat_Type(Integer32):
    """Custom type sonusPktServProfileSidHeartbeat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileSidHeartbeat_Type.__name__ = "Integer32"
_SonusPktServProfileSidHeartbeat_Object = MibTableColumn
sonusPktServProfileSidHeartbeat = _SonusPktServProfileSidHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 20),
    _SonusPktServProfileSidHeartbeat_Type()
)
sonusPktServProfileSidHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileSidHeartbeat.setStatus("current")


class _SonusPktServProfileRtcp_Type(Integer32):
    """Custom type sonusPktServProfileRtcp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileRtcp_Type.__name__ = "Integer32"
_SonusPktServProfileRtcp_Object = MibTableColumn
sonusPktServProfileRtcp = _SonusPktServProfileRtcp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 21),
    _SonusPktServProfileRtcp_Type()
)
sonusPktServProfileRtcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileRtcp.setStatus("current")


class _SonusPktServProfilePacketLossThreshold_Type(Integer32):
    """Custom type sonusPktServProfilePacketLossThreshold based on Integer32"""
    defaultValue = 0


_SonusPktServProfilePacketLossThreshold_Object = MibTableColumn
sonusPktServProfilePacketLossThreshold = _SonusPktServProfilePacketLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 22),
    _SonusPktServProfilePacketLossThreshold_Type()
)
sonusPktServProfilePacketLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfilePacketLossThreshold.setStatus("current")


class _SonusPktServProfilePacketLossAction_Type(Integer32):
    """Custom type sonusPktServProfilePacketLossAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trap", 1),
          ("trapAndDisconnect", 3))
    )


_SonusPktServProfilePacketLossAction_Type.__name__ = "Integer32"
_SonusPktServProfilePacketLossAction_Object = MibTableColumn
sonusPktServProfilePacketLossAction = _SonusPktServProfilePacketLossAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 23),
    _SonusPktServProfilePacketLossAction_Type()
)
sonusPktServProfilePacketLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfilePacketLossAction.setStatus("current")


class _SonusPktServProfileRtpPeerAbsenceAction_Type(Integer32):
    """Custom type sonusPktServProfileRtpPeerAbsenceAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trap", 1),
          ("trapAndDisconnect", 3))
    )


_SonusPktServProfileRtpPeerAbsenceAction_Type.__name__ = "Integer32"
_SonusPktServProfileRtpPeerAbsenceAction_Object = MibTableColumn
sonusPktServProfileRtpPeerAbsenceAction = _SonusPktServProfileRtpPeerAbsenceAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 24),
    _SonusPktServProfileRtpPeerAbsenceAction_Type()
)
sonusPktServProfileRtpPeerAbsenceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileRtpPeerAbsenceAction.setStatus("current")


class _SonusPktServProfileDtmfRelayOutOfBand_Type(Integer32):
    """Custom type sonusPktServProfileDtmfRelayOutOfBand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileDtmfRelayOutOfBand_Type.__name__ = "Integer32"
_SonusPktServProfileDtmfRelayOutOfBand_Object = MibTableColumn
sonusPktServProfileDtmfRelayOutOfBand = _SonusPktServProfileDtmfRelayOutOfBand_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 25),
    _SonusPktServProfileDtmfRelayOutOfBand_Type()
)
sonusPktServProfileDtmfRelayOutOfBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDtmfRelayOutOfBand.setStatus("current")


class _SonusPktServProfileDtmfRelayRemoveDigits_Type(Integer32):
    """Custom type sonusPktServProfileDtmfRelayRemoveDigits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusPktServProfileDtmfRelayRemoveDigits_Type.__name__ = "Integer32"
_SonusPktServProfileDtmfRelayRemoveDigits_Object = MibTableColumn
sonusPktServProfileDtmfRelayRemoveDigits = _SonusPktServProfileDtmfRelayRemoveDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 13, 2, 1, 26),
    _SonusPktServProfileDtmfRelayRemoveDigits_Type()
)
sonusPktServProfileDtmfRelayRemoveDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPktServProfileDtmfRelayRemoveDigits.setStatus("current")
_SonusDisconnectTreatmentObjects_ObjectIdentity = ObjectIdentity
sonusDisconnectTreatmentObjects = _SonusDisconnectTreatmentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14)
)
_SonusDiscTreatProfile_ObjectIdentity = ObjectIdentity
sonusDiscTreatProfile = _SonusDiscTreatProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1)
)
_SonusDiscTreatProfileNextIndex_Type = Integer32
_SonusDiscTreatProfileNextIndex_Object = MibScalar
sonusDiscTreatProfileNextIndex = _SonusDiscTreatProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 1),
    _SonusDiscTreatProfileNextIndex_Type()
)
sonusDiscTreatProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDiscTreatProfileNextIndex.setStatus("current")
_SonusDiscTreatProfileTable_Object = MibTable
sonusDiscTreatProfileTable = _SonusDiscTreatProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDiscTreatProfileTable.setStatus("current")
_SonusDiscTreatProfileEntry_Object = MibTableRow
sonusDiscTreatProfileEntry = _SonusDiscTreatProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 2, 1)
)
sonusDiscTreatProfileEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscTreatProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusDiscTreatProfileEntry.setStatus("current")
_SonusDiscTreatProfileIndex_Type = Integer32
_SonusDiscTreatProfileIndex_Object = MibTableColumn
sonusDiscTreatProfileIndex = _SonusDiscTreatProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 2, 1, 1),
    _SonusDiscTreatProfileIndex_Type()
)
sonusDiscTreatProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscTreatProfileIndex.setStatus("current")
_SonusDiscTreatProfileName_Type = SonusName
_SonusDiscTreatProfileName_Object = MibTableColumn
sonusDiscTreatProfileName = _SonusDiscTreatProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 2, 1, 2),
    _SonusDiscTreatProfileName_Type()
)
sonusDiscTreatProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscTreatProfileName.setStatus("current")
_SonusDiscTreatProfileRowStatus_Type = RowStatus
_SonusDiscTreatProfileRowStatus_Object = MibTableColumn
sonusDiscTreatProfileRowStatus = _SonusDiscTreatProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 1, 2, 1, 3),
    _SonusDiscTreatProfileRowStatus_Type()
)
sonusDiscTreatProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscTreatProfileRowStatus.setStatus("current")
_SonusDiscTreatmentAdmnTable_Object = MibTable
sonusDiscTreatmentAdmnTable = _SonusDiscTreatmentAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    sonusDiscTreatmentAdmnTable.setStatus("current")
_SonusDiscTreatmentAdmnEntry_Object = MibTableRow
sonusDiscTreatmentAdmnEntry = _SonusDiscTreatmentAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1)
)
sonusDiscTreatmentAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscTreatmentProfileIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscTreatmentIndex"),
)
if mibBuilder.loadTexts:
    sonusDiscTreatmentAdmnEntry.setStatus("current")
_SonusDiscTreatmentProfileIndex_Type = Integer32
_SonusDiscTreatmentProfileIndex_Object = MibTableColumn
sonusDiscTreatmentProfileIndex = _SonusDiscTreatmentProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1, 1),
    _SonusDiscTreatmentProfileIndex_Type()
)
sonusDiscTreatmentProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscTreatmentProfileIndex.setStatus("current")
_SonusDiscTreatmentIndex_Type = Integer32
_SonusDiscTreatmentIndex_Object = MibTableColumn
sonusDiscTreatmentIndex = _SonusDiscTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1, 2),
    _SonusDiscTreatmentIndex_Type()
)
sonusDiscTreatmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscTreatmentIndex.setStatus("current")


class _SonusDiscTreatmentReason_Type(Integer32):
    """Custom type sonusDiscTreatmentReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusDiscTreatmentReason_Type.__name__ = "Integer32"
_SonusDiscTreatmentReason_Object = MibTableColumn
sonusDiscTreatmentReason = _SonusDiscTreatmentReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1, 3),
    _SonusDiscTreatmentReason_Type()
)
sonusDiscTreatmentReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDiscTreatmentReason.setStatus("current")
_SonusDiscTreatmentSigSeqProfileName_Type = SonusNameReference
_SonusDiscTreatmentSigSeqProfileName_Object = MibTableColumn
sonusDiscTreatmentSigSeqProfileName = _SonusDiscTreatmentSigSeqProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1, 4),
    _SonusDiscTreatmentSigSeqProfileName_Type()
)
sonusDiscTreatmentSigSeqProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscTreatmentSigSeqProfileName.setStatus("current")
_SonusDiscTreatmentRowStatus_Type = RowStatus
_SonusDiscTreatmentRowStatus_Object = MibTableColumn
sonusDiscTreatmentRowStatus = _SonusDiscTreatmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 2, 1, 5),
    _SonusDiscTreatmentRowStatus_Type()
)
sonusDiscTreatmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscTreatmentRowStatus.setStatus("current")
_SonusDiscSspGroupAdmn_ObjectIdentity = ObjectIdentity
sonusDiscSspGroupAdmn = _SonusDiscSspGroupAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3)
)
_SonusDiscSspNextIndex_Type = Integer32
_SonusDiscSspNextIndex_Object = MibScalar
sonusDiscSspNextIndex = _SonusDiscSspNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 1),
    _SonusDiscSspNextIndex_Type()
)
sonusDiscSspNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDiscSspNextIndex.setStatus("current")
_SonusDiscSspAdmnTable_Object = MibTable
sonusDiscSspAdmnTable = _SonusDiscSspAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    sonusDiscSspAdmnTable.setStatus("current")
_SonusDiscSspAdmnEntry_Object = MibTableRow
sonusDiscSspAdmnEntry = _SonusDiscSspAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 2, 1)
)
sonusDiscSspAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscSigSeqProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusDiscSspAdmnEntry.setStatus("current")
_SonusDiscSigSeqProfileIndex_Type = Integer32
_SonusDiscSigSeqProfileIndex_Object = MibTableColumn
sonusDiscSigSeqProfileIndex = _SonusDiscSigSeqProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 2, 1, 1),
    _SonusDiscSigSeqProfileIndex_Type()
)
sonusDiscSigSeqProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscSigSeqProfileIndex.setStatus("current")
_SonusDiscSigSeqProfileName_Type = SonusName
_SonusDiscSigSeqProfileName_Object = MibTableColumn
sonusDiscSigSeqProfileName = _SonusDiscSigSeqProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 2, 1, 2),
    _SonusDiscSigSeqProfileName_Type()
)
sonusDiscSigSeqProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSeqProfileName.setStatus("current")
_SonusDiscSigSeqProfileRowStatus_Type = RowStatus
_SonusDiscSigSeqProfileRowStatus_Object = MibTableColumn
sonusDiscSigSeqProfileRowStatus = _SonusDiscSigSeqProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 3, 2, 1, 3),
    _SonusDiscSigSeqProfileRowStatus_Type()
)
sonusDiscSigSeqProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSeqProfileRowStatus.setStatus("current")
_SonusDiscSigSeqAdmnTable_Object = MibTable
sonusDiscSigSeqAdmnTable = _SonusDiscSigSeqAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    sonusDiscSigSeqAdmnTable.setStatus("current")
_SonusDiscSigSeqAdmnEntry_Object = MibTableRow
sonusDiscSigSeqAdmnEntry = _SonusDiscSigSeqAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1)
)
sonusDiscSigSeqAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscSigSequenceProfileIndex"),
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusDiscSigSequenceIndex"),
)
if mibBuilder.loadTexts:
    sonusDiscSigSeqAdmnEntry.setStatus("current")
_SonusDiscSigSequenceProfileIndex_Type = Integer32
_SonusDiscSigSequenceProfileIndex_Object = MibTableColumn
sonusDiscSigSequenceProfileIndex = _SonusDiscSigSequenceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 1),
    _SonusDiscSigSequenceProfileIndex_Type()
)
sonusDiscSigSequenceProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceProfileIndex.setStatus("current")
_SonusDiscSigSequenceIndex_Type = Integer32
_SonusDiscSigSequenceIndex_Object = MibTableColumn
sonusDiscSigSequenceIndex = _SonusDiscSigSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 2),
    _SonusDiscSigSequenceIndex_Type()
)
sonusDiscSigSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceIndex.setStatus("current")


class _SonusDiscSigSequencePosition_Type(Integer32):
    """Custom type sonusDiscSigSequencePosition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SonusDiscSigSequencePosition_Type.__name__ = "Integer32"
_SonusDiscSigSequencePosition_Object = MibTableColumn
sonusDiscSigSequencePosition = _SonusDiscSigSequencePosition_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 3),
    _SonusDiscSigSequencePosition_Type()
)
sonusDiscSigSequencePosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequencePosition.setStatus("current")


class _SonusDiscSigSequenceToken_Type(Integer32):
    """Custom type sonusDiscSigSequenceToken based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("clear", 16),
          ("delay", 9),
          ("exec", 17),
          ("playAnn", 8),
          ("playTone", 7))
    )


_SonusDiscSigSequenceToken_Type.__name__ = "Integer32"
_SonusDiscSigSequenceToken_Object = MibTableColumn
sonusDiscSigSequenceToken = _SonusDiscSigSequenceToken_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 4),
    _SonusDiscSigSequenceToken_Type()
)
sonusDiscSigSequenceToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceToken.setStatus("current")


class _SonusDiscSigSequenceParam1_Type(DisplayString):
    """Custom type sonusDiscSigSequenceParam1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusDiscSigSequenceParam1_Type.__name__ = "DisplayString"
_SonusDiscSigSequenceParam1_Object = MibTableColumn
sonusDiscSigSequenceParam1 = _SonusDiscSigSequenceParam1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 5),
    _SonusDiscSigSequenceParam1_Type()
)
sonusDiscSigSequenceParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceParam1.setStatus("current")


class _SonusDiscSigSequenceParam2_Type(DisplayString):
    """Custom type sonusDiscSigSequenceParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusDiscSigSequenceParam2_Type.__name__ = "DisplayString"
_SonusDiscSigSequenceParam2_Object = MibTableColumn
sonusDiscSigSequenceParam2 = _SonusDiscSigSequenceParam2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 6),
    _SonusDiscSigSequenceParam2_Type()
)
sonusDiscSigSequenceParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceParam2.setStatus("current")


class _SonusDiscSigSequenceAdminState_Type(SonusAdminState):
    """Custom type sonusDiscSigSequenceAdminState based on SonusAdminState"""


_SonusDiscSigSequenceAdminState_Object = MibTableColumn
sonusDiscSigSequenceAdminState = _SonusDiscSigSequenceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 7),
    _SonusDiscSigSequenceAdminState_Type()
)
sonusDiscSigSequenceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceAdminState.setStatus("current")
_SonusDiscSigSequenceRowStatus_Type = RowStatus
_SonusDiscSigSequenceRowStatus_Object = MibTableColumn
sonusDiscSigSequenceRowStatus = _SonusDiscSigSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 14, 4, 1, 8),
    _SonusDiscSigSequenceRowStatus_Type()
)
sonusDiscSigSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDiscSigSequenceRowStatus.setStatus("current")
_SonusTestCall_ObjectIdentity = ObjectIdentity
sonusTestCall = _SonusTestCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15)
)
_SonusTestCallNextIndex_Type = Integer32
_SonusTestCallNextIndex_Object = MibScalar
sonusTestCallNextIndex = _SonusTestCallNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 1),
    _SonusTestCallNextIndex_Type()
)
sonusTestCallNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallNextIndex.setStatus("current")
_SonusTestCallAdmnTable_Object = MibTable
sonusTestCallAdmnTable = _SonusTestCallAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    sonusTestCallAdmnTable.setStatus("current")
_SonusTestCallAdmnEntry_Object = MibTableRow
sonusTestCallAdmnEntry = _SonusTestCallAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1)
)
sonusTestCallAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusTestCallAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusTestCallAdmnEntry.setStatus("current")
_SonusTestCallAdmnIndex_Type = Integer32
_SonusTestCallAdmnIndex_Object = MibTableColumn
sonusTestCallAdmnIndex = _SonusTestCallAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 1),
    _SonusTestCallAdmnIndex_Type()
)
sonusTestCallAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallAdmnIndex.setStatus("current")


class _SonusTestCallAdmnState_Type(Integer32):
    """Custom type sonusTestCallAdmnState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SonusTestCallAdmnState_Type.__name__ = "Integer32"
_SonusTestCallAdmnState_Object = MibTableColumn
sonusTestCallAdmnState = _SonusTestCallAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 2),
    _SonusTestCallAdmnState_Type()
)
sonusTestCallAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnState.setStatus("current")
_SonusTestCallAdmnName_Type = SonusName
_SonusTestCallAdmnName_Object = MibTableColumn
sonusTestCallAdmnName = _SonusTestCallAdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 3),
    _SonusTestCallAdmnName_Type()
)
sonusTestCallAdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnName.setStatus("current")


class _SonusTestCallAdmnEndPointShelf_Type(Integer32):
    """Custom type sonusTestCallAdmnEndPointShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusTestCallAdmnEndPointShelf_Type.__name__ = "Integer32"
_SonusTestCallAdmnEndPointShelf_Object = MibTableColumn
sonusTestCallAdmnEndPointShelf = _SonusTestCallAdmnEndPointShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 4),
    _SonusTestCallAdmnEndPointShelf_Type()
)
sonusTestCallAdmnEndPointShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnEndPointShelf.setStatus("current")


class _SonusTestCallAdmnEndPointSlot_Type(Integer32):
    """Custom type sonusTestCallAdmnEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusTestCallAdmnEndPointSlot_Type.__name__ = "Integer32"
_SonusTestCallAdmnEndPointSlot_Object = MibTableColumn
sonusTestCallAdmnEndPointSlot = _SonusTestCallAdmnEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 5),
    _SonusTestCallAdmnEndPointSlot_Type()
)
sonusTestCallAdmnEndPointSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnEndPointSlot.setStatus("current")


class _SonusTestCallAdmnEndPointPort_Type(Integer32):
    """Custom type sonusTestCallAdmnEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTestCallAdmnEndPointPort_Type.__name__ = "Integer32"
_SonusTestCallAdmnEndPointPort_Object = MibTableColumn
sonusTestCallAdmnEndPointPort = _SonusTestCallAdmnEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 6),
    _SonusTestCallAdmnEndPointPort_Type()
)
sonusTestCallAdmnEndPointPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnEndPointPort.setStatus("current")


class _SonusTestCallAdmnEndPointChannel_Type(Integer32):
    """Custom type sonusTestCallAdmnEndPointChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusTestCallAdmnEndPointChannel_Type.__name__ = "Integer32"
_SonusTestCallAdmnEndPointChannel_Object = MibTableColumn
sonusTestCallAdmnEndPointChannel = _SonusTestCallAdmnEndPointChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 7),
    _SonusTestCallAdmnEndPointChannel_Type()
)
sonusTestCallAdmnEndPointChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnEndPointChannel.setStatus("current")
_SonusTestCallAdmnRowStatus_Type = RowStatus
_SonusTestCallAdmnRowStatus_Object = MibTableColumn
sonusTestCallAdmnRowStatus = _SonusTestCallAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 8),
    _SonusTestCallAdmnRowStatus_Type()
)
sonusTestCallAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnRowStatus.setStatus("current")


class _SonusTestCallAdmnType_Type(Integer32):
    """Custom type sonusTestCallAdmnType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("listen", 0),
          ("play", 1))
    )


_SonusTestCallAdmnType_Type.__name__ = "Integer32"
_SonusTestCallAdmnType_Object = MibTableColumn
sonusTestCallAdmnType = _SonusTestCallAdmnType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 9),
    _SonusTestCallAdmnType_Type()
)
sonusTestCallAdmnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnType.setStatus("current")


class _SonusTestCallAdmnPower_Type(Integer32):
    """Custom type sonusTestCallAdmnPower based on Integer32"""
    defaultValue = -6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 3),
    )


_SonusTestCallAdmnPower_Type.__name__ = "Integer32"
_SonusTestCallAdmnPower_Object = MibTableColumn
sonusTestCallAdmnPower = _SonusTestCallAdmnPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 10),
    _SonusTestCallAdmnPower_Type()
)
sonusTestCallAdmnPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnPower.setStatus("current")


class _SonusTestCallAdmnFrequency_Type(Integer32):
    """Custom type sonusTestCallAdmnFrequency based on Integer32"""
    defaultValue = 1004

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3999),
    )


_SonusTestCallAdmnFrequency_Type.__name__ = "Integer32"
_SonusTestCallAdmnFrequency_Object = MibTableColumn
sonusTestCallAdmnFrequency = _SonusTestCallAdmnFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 11),
    _SonusTestCallAdmnFrequency_Type()
)
sonusTestCallAdmnFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnFrequency.setStatus("current")


class _SonusTestCallAdmnStatPower_Type(Integer32):
    """Custom type sonusTestCallAdmnStatPower based on Integer32"""
    defaultValue = -1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3),
    )


_SonusTestCallAdmnStatPower_Type.__name__ = "Integer32"
_SonusTestCallAdmnStatPower_Object = MibTableColumn
sonusTestCallAdmnStatPower = _SonusTestCallAdmnStatPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 12),
    _SonusTestCallAdmnStatPower_Type()
)
sonusTestCallAdmnStatPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnStatPower.setStatus("current")


class _SonusTestCallAdmnStatPowerTenths_Type(Integer32):
    """Custom type sonusTestCallAdmnStatPowerTenths based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_SonusTestCallAdmnStatPowerTenths_Type.__name__ = "Integer32"
_SonusTestCallAdmnStatPowerTenths_Object = MibTableColumn
sonusTestCallAdmnStatPowerTenths = _SonusTestCallAdmnStatPowerTenths_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 15, 2, 1, 13),
    _SonusTestCallAdmnStatPowerTenths_Type()
)
sonusTestCallAdmnStatPowerTenths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAdmnStatPowerTenths.setStatus("current")
_SonusTestCallStatTable_Object = MibTable
sonusTestCallStatTable = _SonusTestCallStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16)
)
if mibBuilder.loadTexts:
    sonusTestCallStatTable.setStatus("current")
_SonusTestCallStatEntry_Object = MibTableRow
sonusTestCallStatEntry = _SonusTestCallStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16, 1)
)
sonusTestCallStatEntry.setIndexNames(
    (0, "SONUS-NODE-RESOURCES-MIB", "sonusTestCallStatIndex"),
)
if mibBuilder.loadTexts:
    sonusTestCallStatEntry.setStatus("current")
_SonusTestCallStatIndex_Type = Integer32
_SonusTestCallStatIndex_Object = MibTableColumn
sonusTestCallStatIndex = _SonusTestCallStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16, 1, 1),
    _SonusTestCallStatIndex_Type()
)
sonusTestCallStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallStatIndex.setStatus("current")
_SonusTestCallStatCallId_Type = Integer32
_SonusTestCallStatCallId_Object = MibTableColumn
sonusTestCallStatCallId = _SonusTestCallStatCallId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16, 1, 2),
    _SonusTestCallStatCallId_Type()
)
sonusTestCallStatCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallStatCallId.setStatus("current")


class _SonusTestCallStatState_Type(DisplayString):
    """Custom type sonusTestCallStatState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTestCallStatState_Type.__name__ = "DisplayString"
_SonusTestCallStatState_Object = MibTableColumn
sonusTestCallStatState = _SonusTestCallStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16, 1, 3),
    _SonusTestCallStatState_Type()
)
sonusTestCallStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallStatState.setStatus("current")


class _SonusTestCallStatTime_Type(DisplayString):
    """Custom type sonusTestCallStatTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTestCallStatTime_Type.__name__ = "DisplayString"
_SonusTestCallStatTime_Object = MibTableColumn
sonusTestCallStatTime = _SonusTestCallStatTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 16, 1, 4),
    _SonusTestCallStatTime_Type()
)
sonusTestCallStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTestCallStatTime.setStatus("current")
_SonusTestCallActionObjects_ObjectIdentity = ObjectIdentity
sonusTestCallActionObjects = _SonusTestCallActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 17)
)
_SonusTestCallGcid_Type = Integer32
_SonusTestCallGcid_Object = MibScalar
sonusTestCallGcid = _SonusTestCallGcid_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 17, 1),
    _SonusTestCallGcid_Type()
)
sonusTestCallGcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallGcid.setStatus("current")


class _SonusTestCallAction_Type(Integer32):
    """Custom type sonusTestCallAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("none", 1))
    )


_SonusTestCallAction_Type.__name__ = "Integer32"
_SonusTestCallAction_Object = MibScalar
sonusTestCallAction = _SonusTestCallAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 1, 17, 2),
    _SonusTestCallAction_Type()
)
sonusTestCallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTestCallAction.setStatus("current")
_SonusNodeResourcesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusNodeResourcesMIBNotifications = _SonusNodeResourcesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2)
)
_SonusNodeResourcesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusNodeResourcesMIBNotificationsPrefix = _SonusNodeResourcesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 0)
)
_SonusNodeResourcesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusNodeResourcesMIBNotificationsObjects = _SonusNodeResourcesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 1)
)


class _SonusCallAdmissionChangeReason_Type(DisplayString):
    """Custom type sonusCallAdmissionChangeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 101),
    )


_SonusCallAdmissionChangeReason_Type.__name__ = "DisplayString"
_SonusCallAdmissionChangeReason_Object = MibScalar
sonusCallAdmissionChangeReason = _SonusCallAdmissionChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 1, 1),
    _SonusCallAdmissionChangeReason_Type()
)
sonusCallAdmissionChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCallAdmissionChangeReason.setStatus("current")

# Managed Objects groups


# Notification objects

sonusNodeResourcesCallAdmissionSuspendedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 0, 1)
)
sonusNodeResourcesCallAdmissionSuspendedNotification.setObjects(
      *(("SONUS-NODE-RESOURCES-MIB", "sonusCallAdmissionChangeReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeResourcesCallAdmissionSuspendedNotification.setStatus(
        "current"
    )

sonusNodeResourcesCallAdmissionEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 0, 2)
)
sonusNodeResourcesCallAdmissionEnabledNotification.setObjects(
      *(("SONUS-NODE-RESOURCES-MIB", "sonusCallAdmissionChangeReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeResourcesCallAdmissionEnabledNotification.setStatus(
        "current"
    )

sonusNodeResourcesCallTraceHitNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 2, 2, 0, 3)
)
sonusNodeResourcesCallTraceHitNotification.setObjects(
      *(("SONUS-NODE-RESOURCES-MIB", "sonusCallTraceCalledNumber"),
        ("SONUS-NODE-RESOURCES-MIB", "sonusCallTraceCallingNumber"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeResourcesCallTraceHitNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-NODE-RESOURCES-MIB",
    **{"sonusNodeResourcesMIB": sonusNodeResourcesMIB,
       "sonusNodeResourcesMIBObjects": sonusNodeResourcesMIBObjects,
       "sonusServProfile": sonusServProfile,
       "sonusServProfileNextIndex": sonusServProfileNextIndex,
       "sonusServProfileTable": sonusServProfileTable,
       "sonusServProfileEntry": sonusServProfileEntry,
       "sonusServProfileIndex": sonusServProfileIndex,
       "sonusServProfileState": sonusServProfileState,
       "sonusServProfileName": sonusServProfileName,
       "sonusServProfileType": sonusServProfileType,
       "sonusServProfileVCktEncoding": sonusServProfileVCktEncoding,
       "sonusServProfileVCktBandwidth": sonusServProfileVCktBandwidth,
       "sonusServProfileVCktNecEnable": sonusServProfileVCktNecEnable,
       "sonusServProfileVPktEncoding": sonusServProfileVPktEncoding,
       "sonusServProfileVPktFrameSize": sonusServProfileVPktFrameSize,
       "sonusServProfileVPktFramesPerPacket": sonusServProfileVPktFramesPerPacket,
       "sonusServProfileVPktMaxNetworkJitter": sonusServProfileVPktMaxNetworkJitter,
       "sonusServProfileVPktTosValue": sonusServProfileVPktTosValue,
       "sonusServProfileCttTestType": sonusServProfileCttTestType,
       "sonusServProfileCttTimeout": sonusServProfileCttTimeout,
       "sonusServProfileCttMinDetectTime": sonusServProfileCttMinDetectTime,
       "sonusServProfileCttMinReleaseTime": sonusServProfileCttMinReleaseTime,
       "sonusServProfileCapability": sonusServProfileCapability,
       "sonusServProfileDPktRestrictedCfg": sonusServProfileDPktRestrictedCfg,
       "sonusServProfileDPktRtpPayloadType": sonusServProfileDPktRtpPayloadType,
       "sonusServProfileDPktMaxNetworkJitter": sonusServProfileDPktMaxNetworkJitter,
       "sonusServProfileRowStatus": sonusServProfileRowStatus,
       "sonusSonicBusStatTable": sonusSonicBusStatTable,
       "sonusSonicBusStatEntry": sonusSonicBusStatEntry,
       "sonusSonicBusStatShelfIndex": sonusSonicBusStatShelfIndex,
       "sonusSonicBusStatNumCalls": sonusSonicBusStatNumCalls,
       "sonusSonicBusStatBwAllocated": sonusSonicBusStatBwAllocated,
       "sonusSonicBusStatSduCount": sonusSonicBusStatSduCount,
       "sonusActiveCallTable": sonusActiveCallTable,
       "sonusActiveCallEntry": sonusActiveCallEntry,
       "sonusActiveCallShelfIndex": sonusActiveCallShelfIndex,
       "sonusActiveCallSlotIndex": sonusActiveCallSlotIndex,
       "sonusActiveCallIndex": sonusActiveCallIndex,
       "sonusActiveCallId": sonusActiveCallId,
       "sonusActiveCallSonicBusUnitsAllocated": sonusActiveCallSonicBusUnitsAllocated,
       "sonusActiveCallNumResources": sonusActiveCallNumResources,
       "sonusActiveCallState": sonusActiveCallState,
       "sonusActiveCallIngressServProfile": sonusActiveCallIngressServProfile,
       "sonusActiveCallEgressServProfile": sonusActiveCallEgressServProfile,
       "sonusActiveCallCallingNum": sonusActiveCallCallingNum,
       "sonusActiveCallCalledNum": sonusActiveCallCalledNum,
       "sonusActiveCallAddressTransPerformed": sonusActiveCallAddressTransPerformed,
       "sonusActiveCallOrigCalledNum": sonusActiveCallOrigCalledNum,
       "sonusActiveCallScenarioType": sonusActiveCallScenarioType,
       "sonusActiveCallIngressPstnSlotNum": sonusActiveCallIngressPstnSlotNum,
       "sonusActiveCallIngressPstnPortNum": sonusActiveCallIngressPstnPortNum,
       "sonusActiveCallIngressPstnChannelNum": sonusActiveCallIngressPstnChannelNum,
       "sonusActiveCallIngressPstnChannelCount": sonusActiveCallIngressPstnChannelCount,
       "sonusActiveCallIngressPstnChannelBitMap": sonusActiveCallIngressPstnChannelBitMap,
       "sonusActiveCallEgressPstnSlotNum": sonusActiveCallEgressPstnSlotNum,
       "sonusActiveCallEgressPstnPortNum": sonusActiveCallEgressPstnPortNum,
       "sonusActiveCallEgressPstnChannelNum": sonusActiveCallEgressPstnChannelNum,
       "sonusActiveCallEgressPstnChannelCount": sonusActiveCallEgressPstnChannelCount,
       "sonusActiveCallEgressPstnChannelBitMap": sonusActiveCallEgressPstnChannelBitMap,
       "sonusActiveCallIngressLocalIpSockAddr": sonusActiveCallIngressLocalIpSockAddr,
       "sonusActiveCallIngressRemoteIpSockAddr": sonusActiveCallIngressRemoteIpSockAddr,
       "sonusActiveCallEgressLocalIpSockAddr": sonusActiveCallEgressLocalIpSockAddr,
       "sonusActiveCallEgressRemoteIpSockAddr": sonusActiveCallEgressRemoteIpSockAddr,
       "sonusActiveCallIngressPstnTrunk": sonusActiveCallIngressPstnTrunk,
       "sonusActiveCallEgressPstnTrunk": sonusActiveCallEgressPstnTrunk,
       "sonusActiveCallIngressIpDestGwName": sonusActiveCallIngressIpDestGwName,
       "sonusActiveCallEgressIpDestGwName": sonusActiveCallEgressIpDestGwName,
       "sonusActiveCallDuration": sonusActiveCallDuration,
       "sonusActiveCallIngressEpType": sonusActiveCallIngressEpType,
       "sonusActiveCallEgressEpType": sonusActiveCallEgressEpType,
       "sonusActiveCallIngressSgType": sonusActiveCallIngressSgType,
       "sonusActiveCallEgressSgType": sonusActiveCallEgressSgType,
       "sonusActiveCallPacketsSent": sonusActiveCallPacketsSent,
       "sonusActiveCallPacketsReceived": sonusActiveCallPacketsReceived,
       "sonusActiveCallOctetsSent": sonusActiveCallOctetsSent,
       "sonusActiveCallOctetsReceived": sonusActiveCallOctetsReceived,
       "sonusActiveCallPacketsLost": sonusActiveCallPacketsLost,
       "sonusActiveCallPacketsDiscarded": sonusActiveCallPacketsDiscarded,
       "sonusActiveCallInterarrivalJitter": sonusActiveCallInterarrivalJitter,
       "sonusActiveCallPacketLatency": sonusActiveCallPacketLatency,
       "sonusCallResTable": sonusCallResTable,
       "sonusCallResEntry": sonusCallResEntry,
       "sonusCallResShelfIndex": sonusCallResShelfIndex,
       "sonusCallResSlotIndex": sonusCallResSlotIndex,
       "sonusCallResCallIndex": sonusCallResCallIndex,
       "sonusCallResIndex": sonusCallResIndex,
       "sonusCallResId": sonusCallResId,
       "sonusCallResCallId": sonusCallResCallId,
       "sonusCallResType": sonusCallResType,
       "sonusCallResMgrHandle": sonusCallResMgrHandle,
       "sonusCallResMgrShelfIndex": sonusCallResMgrShelfIndex,
       "sonusCallResMgrSlotIndex": sonusCallResMgrSlotIndex,
       "sonusCallPegCountsTable": sonusCallPegCountsTable,
       "sonusCallPegCountsEntry": sonusCallPegCountsEntry,
       "sonusCallPegCountsShelfIndex": sonusCallPegCountsShelfIndex,
       "sonusCallPegCountsSlotIndex": sonusCallPegCountsSlotIndex,
       "sonusCallPegCountsReset": sonusCallPegCountsReset,
       "sonusCallPegCountsAttempts": sonusCallPegCountsAttempts,
       "sonusCallPegCountsCompletions": sonusCallPegCountsCompletions,
       "sonusCallPegCountsActiveCalls": sonusCallPegCountsActiveCalls,
       "sonusCallPegCountsStableCalls": sonusCallPegCountsStableCalls,
       "sonusCallPegCountsUpdates": sonusCallPegCountsUpdates,
       "sonusCallPegCountsActiveCallsNonUser": sonusCallPegCountsActiveCallsNonUser,
       "sonusCallPegCountsStableCallsNonUser": sonusCallPegCountsStableCallsNonUser,
       "sonusToneObjects": sonusToneObjects,
       "sonusToneProfile": sonusToneProfile,
       "sonusToneProfileNextIndex": sonusToneProfileNextIndex,
       "sonusToneProfileTable": sonusToneProfileTable,
       "sonusToneProfileEntry": sonusToneProfileEntry,
       "sonusToneProfileIndex": sonusToneProfileIndex,
       "sonusToneProfileName": sonusToneProfileName,
       "sonusToneProfileGenerationMethod": sonusToneProfileGenerationMethod,
       "sonusToneProfileTone1Freq": sonusToneProfileTone1Freq,
       "sonusToneProfileTone1Power": sonusToneProfileTone1Power,
       "sonusToneProfileTone2Freq": sonusToneProfileTone2Freq,
       "sonusToneProfileTone2Power": sonusToneProfileTone2Power,
       "sonusToneProfileCarrierFreq": sonusToneProfileCarrierFreq,
       "sonusToneProfileSignalFreq": sonusToneProfileSignalFreq,
       "sonusToneProfileModPower": sonusToneProfileModPower,
       "sonusToneProfileModIndex": sonusToneProfileModIndex,
       "sonusToneProfileMake1": sonusToneProfileMake1,
       "sonusToneProfileBreak1": sonusToneProfileBreak1,
       "sonusToneProfileMake2": sonusToneProfileMake2,
       "sonusToneProfileBreak2": sonusToneProfileBreak2,
       "sonusToneProfileMake3": sonusToneProfileMake3,
       "sonusToneProfileBreak3": sonusToneProfileBreak3,
       "sonusToneProfileRepeat": sonusToneProfileRepeat,
       "sonusToneProfileRowStatus": sonusToneProfileRowStatus,
       "sonusToneType": sonusToneType,
       "sonusToneTypeNextIndex": sonusToneTypeNextIndex,
       "sonusToneTypeTable": sonusToneTypeTable,
       "sonusToneTypeEntry": sonusToneTypeEntry,
       "sonusToneTypeIndex": sonusToneTypeIndex,
       "sonusToneTypeName": sonusToneTypeName,
       "sonusToneTypeRowStatus": sonusToneTypeRowStatus,
       "sonusTonePackage": sonusTonePackage,
       "sonusTonePackageNextIndex": sonusTonePackageNextIndex,
       "sonusTonePackageTable": sonusTonePackageTable,
       "sonusTonePackageEntry": sonusTonePackageEntry,
       "sonusTonePackageIndex": sonusTonePackageIndex,
       "sonusTonePackageName": sonusTonePackageName,
       "sonusTonePackageRowStatus": sonusTonePackageRowStatus,
       "sonusTonePkgElem": sonusTonePkgElem,
       "sonusTonePkgElemTable": sonusTonePkgElemTable,
       "sonusTonePkgElemEntry": sonusTonePkgElemEntry,
       "sonusTonePkgElemIndex": sonusTonePkgElemIndex,
       "sonusTonePkgElemTonePackageRef": sonusTonePkgElemTonePackageRef,
       "sonusTonePkgElemToneTypeRef": sonusTonePkgElemToneTypeRef,
       "sonusTonePkgElemToneProfileRef": sonusTonePkgElemToneProfileRef,
       "sonusTonePkgElemRowStatus": sonusTonePkgElemRowStatus,
       "sonusDigitProfile": sonusDigitProfile,
       "sonusDigitProfileNextIndex": sonusDigitProfileNextIndex,
       "sonusDigitProfileTable": sonusDigitProfileTable,
       "sonusDigitProfileEntry": sonusDigitProfileEntry,
       "sonusDigitProfileIndex": sonusDigitProfileIndex,
       "sonusDigitProfileName": sonusDigitProfileName,
       "sonusDigitProfileType": sonusDigitProfileType,
       "sonusDigitProfileGenPower": sonusDigitProfileGenPower,
       "sonusDigitProfileGenMake": sonusDigitProfileGenMake,
       "sonusDigitProfileGenBreak": sonusDigitProfileGenBreak,
       "sonusDigitProfileDetMinPower": sonusDigitProfileDetMinPower,
       "sonusDigitProfileDetMinOnDuration": sonusDigitProfileDetMinOnDuration,
       "sonusDigitProfileDetMinOffDuration": sonusDigitProfileDetMinOffDuration,
       "sonusDigitProfileDetFreqAcceptRange": sonusDigitProfileDetFreqAcceptRange,
       "sonusDigitProfileDtmfDetTwistCutoff": sonusDigitProfileDtmfDetTwistCutoff,
       "sonusDigitProfileMfr1GenMakeKp": sonusDigitProfileMfr1GenMakeKp,
       "sonusDigitProfileRowStatus": sonusDigitProfileRowStatus,
       "sonusStaticCall": sonusStaticCall,
       "sonusStaticCallNextIndex": sonusStaticCallNextIndex,
       "sonusStaticCallAdmnTable": sonusStaticCallAdmnTable,
       "sonusStaticCallAdmnEntry": sonusStaticCallAdmnEntry,
       "sonusStaticCallAdmnIndex": sonusStaticCallAdmnIndex,
       "sonusStaticCallAdmnState": sonusStaticCallAdmnState,
       "sonusStaticCallAdmnName": sonusStaticCallAdmnName,
       "sonusStaticCallAdmnEndPointAShelf": sonusStaticCallAdmnEndPointAShelf,
       "sonusStaticCallAdmnEndPointASlot": sonusStaticCallAdmnEndPointASlot,
       "sonusStaticCallAdmnEndPointAPort": sonusStaticCallAdmnEndPointAPort,
       "sonusStaticCallAdmnEndPointAChannel": sonusStaticCallAdmnEndPointAChannel,
       "sonusStaticCallAdmnEndPointAServProfile": sonusStaticCallAdmnEndPointAServProfile,
       "sonusStaticCallAdmnEndPointBType": sonusStaticCallAdmnEndPointBType,
       "sonusStaticCallAdmnEndPointBShelf": sonusStaticCallAdmnEndPointBShelf,
       "sonusStaticCallAdmnEndPointBSlot": sonusStaticCallAdmnEndPointBSlot,
       "sonusStaticCallAdmnEndPointBPort": sonusStaticCallAdmnEndPointBPort,
       "sonusStaticCallAdmnEndPointBChannel": sonusStaticCallAdmnEndPointBChannel,
       "sonusStaticCallAdmnEndPointBLocalRTPPort": sonusStaticCallAdmnEndPointBLocalRTPPort,
       "sonusStaticCallAdmnEndPointBLocalIpAddress": sonusStaticCallAdmnEndPointBLocalIpAddress,
       "sonusStaticCallAdmnEndPointBRemoteRTPPort": sonusStaticCallAdmnEndPointBRemoteRTPPort,
       "sonusStaticCallAdmnEndPointBRemoteIpAddress": sonusStaticCallAdmnEndPointBRemoteIpAddress,
       "sonusStaticCallAdmnEndPointBServProfile": sonusStaticCallAdmnEndPointBServProfile,
       "sonusStaticCallAdmnCircuitMode": sonusStaticCallAdmnCircuitMode,
       "sonusStaticCallAdmnRowStatus": sonusStaticCallAdmnRowStatus,
       "sonusStaticCallStatTable": sonusStaticCallStatTable,
       "sonusStaticCallStatEntry": sonusStaticCallStatEntry,
       "sonusStaticCallStatIndex": sonusStaticCallStatIndex,
       "sonusStaticCallStatCallId": sonusStaticCallStatCallId,
       "sonusStaticCallStatState": sonusStaticCallStatState,
       "sonusStaticCallStatTime": sonusStaticCallStatTime,
       "sonusStaticCallActionObjects": sonusStaticCallActionObjects,
       "sonusStaticCallGcid": sonusStaticCallGcid,
       "sonusStaticCallAction": sonusStaticCallAction,
       "sonusCallTrace": sonusCallTrace,
       "sonusCallTraceNextIndex": sonusCallTraceNextIndex,
       "sonusCallTraceTable": sonusCallTraceTable,
       "sonusCallTraceEntry": sonusCallTraceEntry,
       "sonusCallTraceIndex": sonusCallTraceIndex,
       "sonusCallTraceState": sonusCallTraceState,
       "sonusCallTraceName": sonusCallTraceName,
       "sonusCallTraceType": sonusCallTraceType,
       "sonusCallTraceCalledNumber": sonusCallTraceCalledNumber,
       "sonusCallTraceCallingNumber": sonusCallTraceCallingNumber,
       "sonusCallTraceLevel": sonusCallTraceLevel,
       "sonusCallTraceRowStatus": sonusCallTraceRowStatus,
       "sonusCktServProfile": sonusCktServProfile,
       "sonusCktServProfileNextIndex": sonusCktServProfileNextIndex,
       "sonusCktServProfileTable": sonusCktServProfileTable,
       "sonusCktServProfileEntry": sonusCktServProfileEntry,
       "sonusCktServProfileIndex": sonusCktServProfileIndex,
       "sonusCktServProfileState": sonusCktServProfileState,
       "sonusCktServProfileName": sonusCktServProfileName,
       "sonusCktServProfileAudioEncoding": sonusCktServProfileAudioEncoding,
       "sonusCktServProfileBandwidth": sonusCktServProfileBandwidth,
       "sonusCktServProfileNecEnable": sonusCktServProfileNecEnable,
       "sonusCktServProfileCttTestType": sonusCktServProfileCttTestType,
       "sonusCktServProfileCttTimeout": sonusCktServProfileCttTimeout,
       "sonusCktServProfileCttMinDetectTime": sonusCktServProfileCttMinDetectTime,
       "sonusCktServProfileCttMinReleaseTime": sonusCktServProfileCttMinReleaseTime,
       "sonusCktServProfileCapability": sonusCktServProfileCapability,
       "sonusCktServProfileDataRestrictedCfg": sonusCktServProfileDataRestrictedCfg,
       "sonusCktServProfileDtmfProfileName": sonusCktServProfileDtmfProfileName,
       "sonusCktServProfileRowStatus": sonusCktServProfileRowStatus,
       "sonusCktServProfileInterworkingXfrCap": sonusCktServProfileInterworkingXfrCap,
       "sonusPktServProfile": sonusPktServProfile,
       "sonusPktServProfileNextIndex": sonusPktServProfileNextIndex,
       "sonusPktServProfileTable": sonusPktServProfileTable,
       "sonusPktServProfileEntry": sonusPktServProfileEntry,
       "sonusPktServProfileIndex": sonusPktServProfileIndex,
       "sonusPktServProfileState": sonusPktServProfileState,
       "sonusPktServProfileName": sonusPktServProfileName,
       "sonusPktServProfileDestProtocol": sonusPktServProfileDestProtocol,
       "sonusPktServProfilePrfdAudioEncoding": sonusPktServProfilePrfdAudioEncoding,
       "sonusPktServProfilePrfdFramesPerPacket": sonusPktServProfilePrfdFramesPerPacket,
       "sonusPktServProfileDefFramesPerPacket": sonusPktServProfileDefFramesPerPacket,
       "sonusPktServProfileDefAudioEnable": sonusPktServProfileDefAudioEnable,
       "sonusPktServProfileSilenceFactor": sonusPktServProfileSilenceFactor,
       "sonusPktServProfileVInitPlayoutBufDelay": sonusPktServProfileVInitPlayoutBufDelay,
       "sonusPktServProfileFaxRelay": sonusPktServProfileFaxRelay,
       "sonusPktServProfileDtmfRelay": sonusPktServProfileDtmfRelay,
       "sonusPktServProfileFallbackHandling": sonusPktServProfileFallbackHandling,
       "sonusPktServProfileTosValue": sonusPktServProfileTosValue,
       "sonusPktServProfileDInitPlayoutBufDelay": sonusPktServProfileDInitPlayoutBufDelay,
       "sonusPktServProfileDataRtpPayloadType": sonusPktServProfileDataRtpPayloadType,
       "sonusPktServProfileRowStatus": sonusPktServProfileRowStatus,
       "sonusPktServProfileG711SendSidPackets": sonusPktServProfileG711SendSidPackets,
       "sonusPktServProfileG711SidRtpPayloadType": sonusPktServProfileG711SidRtpPayloadType,
       "sonusPktServProfileSidHeartbeat": sonusPktServProfileSidHeartbeat,
       "sonusPktServProfileRtcp": sonusPktServProfileRtcp,
       "sonusPktServProfilePacketLossThreshold": sonusPktServProfilePacketLossThreshold,
       "sonusPktServProfilePacketLossAction": sonusPktServProfilePacketLossAction,
       "sonusPktServProfileRtpPeerAbsenceAction": sonusPktServProfileRtpPeerAbsenceAction,
       "sonusPktServProfileDtmfRelayOutOfBand": sonusPktServProfileDtmfRelayOutOfBand,
       "sonusPktServProfileDtmfRelayRemoveDigits": sonusPktServProfileDtmfRelayRemoveDigits,
       "sonusDisconnectTreatmentObjects": sonusDisconnectTreatmentObjects,
       "sonusDiscTreatProfile": sonusDiscTreatProfile,
       "sonusDiscTreatProfileNextIndex": sonusDiscTreatProfileNextIndex,
       "sonusDiscTreatProfileTable": sonusDiscTreatProfileTable,
       "sonusDiscTreatProfileEntry": sonusDiscTreatProfileEntry,
       "sonusDiscTreatProfileIndex": sonusDiscTreatProfileIndex,
       "sonusDiscTreatProfileName": sonusDiscTreatProfileName,
       "sonusDiscTreatProfileRowStatus": sonusDiscTreatProfileRowStatus,
       "sonusDiscTreatmentAdmnTable": sonusDiscTreatmentAdmnTable,
       "sonusDiscTreatmentAdmnEntry": sonusDiscTreatmentAdmnEntry,
       "sonusDiscTreatmentProfileIndex": sonusDiscTreatmentProfileIndex,
       "sonusDiscTreatmentIndex": sonusDiscTreatmentIndex,
       "sonusDiscTreatmentReason": sonusDiscTreatmentReason,
       "sonusDiscTreatmentSigSeqProfileName": sonusDiscTreatmentSigSeqProfileName,
       "sonusDiscTreatmentRowStatus": sonusDiscTreatmentRowStatus,
       "sonusDiscSspGroupAdmn": sonusDiscSspGroupAdmn,
       "sonusDiscSspNextIndex": sonusDiscSspNextIndex,
       "sonusDiscSspAdmnTable": sonusDiscSspAdmnTable,
       "sonusDiscSspAdmnEntry": sonusDiscSspAdmnEntry,
       "sonusDiscSigSeqProfileIndex": sonusDiscSigSeqProfileIndex,
       "sonusDiscSigSeqProfileName": sonusDiscSigSeqProfileName,
       "sonusDiscSigSeqProfileRowStatus": sonusDiscSigSeqProfileRowStatus,
       "sonusDiscSigSeqAdmnTable": sonusDiscSigSeqAdmnTable,
       "sonusDiscSigSeqAdmnEntry": sonusDiscSigSeqAdmnEntry,
       "sonusDiscSigSequenceProfileIndex": sonusDiscSigSequenceProfileIndex,
       "sonusDiscSigSequenceIndex": sonusDiscSigSequenceIndex,
       "sonusDiscSigSequencePosition": sonusDiscSigSequencePosition,
       "sonusDiscSigSequenceToken": sonusDiscSigSequenceToken,
       "sonusDiscSigSequenceParam1": sonusDiscSigSequenceParam1,
       "sonusDiscSigSequenceParam2": sonusDiscSigSequenceParam2,
       "sonusDiscSigSequenceAdminState": sonusDiscSigSequenceAdminState,
       "sonusDiscSigSequenceRowStatus": sonusDiscSigSequenceRowStatus,
       "sonusTestCall": sonusTestCall,
       "sonusTestCallNextIndex": sonusTestCallNextIndex,
       "sonusTestCallAdmnTable": sonusTestCallAdmnTable,
       "sonusTestCallAdmnEntry": sonusTestCallAdmnEntry,
       "sonusTestCallAdmnIndex": sonusTestCallAdmnIndex,
       "sonusTestCallAdmnState": sonusTestCallAdmnState,
       "sonusTestCallAdmnName": sonusTestCallAdmnName,
       "sonusTestCallAdmnEndPointShelf": sonusTestCallAdmnEndPointShelf,
       "sonusTestCallAdmnEndPointSlot": sonusTestCallAdmnEndPointSlot,
       "sonusTestCallAdmnEndPointPort": sonusTestCallAdmnEndPointPort,
       "sonusTestCallAdmnEndPointChannel": sonusTestCallAdmnEndPointChannel,
       "sonusTestCallAdmnRowStatus": sonusTestCallAdmnRowStatus,
       "sonusTestCallAdmnType": sonusTestCallAdmnType,
       "sonusTestCallAdmnPower": sonusTestCallAdmnPower,
       "sonusTestCallAdmnFrequency": sonusTestCallAdmnFrequency,
       "sonusTestCallAdmnStatPower": sonusTestCallAdmnStatPower,
       "sonusTestCallAdmnStatPowerTenths": sonusTestCallAdmnStatPowerTenths,
       "sonusTestCallStatTable": sonusTestCallStatTable,
       "sonusTestCallStatEntry": sonusTestCallStatEntry,
       "sonusTestCallStatIndex": sonusTestCallStatIndex,
       "sonusTestCallStatCallId": sonusTestCallStatCallId,
       "sonusTestCallStatState": sonusTestCallStatState,
       "sonusTestCallStatTime": sonusTestCallStatTime,
       "sonusTestCallActionObjects": sonusTestCallActionObjects,
       "sonusTestCallGcid": sonusTestCallGcid,
       "sonusTestCallAction": sonusTestCallAction,
       "sonusNodeResourcesMIBNotifications": sonusNodeResourcesMIBNotifications,
       "sonusNodeResourcesMIBNotificationsPrefix": sonusNodeResourcesMIBNotificationsPrefix,
       "sonusNodeResourcesCallAdmissionSuspendedNotification": sonusNodeResourcesCallAdmissionSuspendedNotification,
       "sonusNodeResourcesCallAdmissionEnabledNotification": sonusNodeResourcesCallAdmissionEnabledNotification,
       "sonusNodeResourcesCallTraceHitNotification": sonusNodeResourcesCallTraceHitNotification,
       "sonusNodeResourcesMIBNotificationsObjects": sonusNodeResourcesMIBNotificationsObjects,
       "sonusCallAdmissionChangeReason": sonusCallAdmissionChangeReason}
)
