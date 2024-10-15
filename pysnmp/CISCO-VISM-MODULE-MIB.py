# SNMP MIB module (CISCO-VISM-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:53 2024
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

(cardSpecific,
 voice) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardSpecific",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVismModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 82)
)
ciscoVismModuleMIB.setRevisions(
        ("2005-10-17 00:00",
         "2005-03-01 00:00",
         "2004-05-24 00:00",
         "2004-03-09 00:00",
         "2003-10-31 00:00",
         "2003-06-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VismFaxDeJitterMode(Integer32, TextualConvention):
    status = "current"
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
        *(("adaptive", 2),
          ("fixedWithTS", 3),
          ("fixedWithoutTS", 4),
          ("passThrough", 5),
          ("unSpecified", 1))
    )



class VismFaxDeJitterInitDelay(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eighty", 80),
          ("eightyfive", 85),
          ("fifteen", 15),
          ("fifty", 50),
          ("fiftyfive", 55),
          ("five", 5),
          ("forty", 40),
          ("fortyfive", 45),
          ("hundred", 100),
          ("ninety", 90),
          ("ninetyfive", 95),
          ("seventy", 70),
          ("seventyfive", 75),
          ("sixty", 60),
          ("sixtyfive", 65),
          ("ten", 10),
          ("thirty", 30),
          ("thirtyfive", 35),
          ("twenty", 20),
          ("twentyfive", 25),
          ("unSpecified", 0))
    )



# MIB Managed Objects in the order of their OIDs

_VismConfig_ObjectIdentity = ObjectIdentity
vismConfig = _VismConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17)
)
_VismIpGrp_ObjectIdentity = ObjectIdentity
vismIpGrp = _VismIpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1)
)
_VismIpAddress_Type = IpAddress
_VismIpAddress_Object = MibScalar
vismIpAddress = _VismIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1, 1),
    _VismIpAddress_Type()
)
vismIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismIpAddress.setStatus("current")
_VismSubNetMask_Type = IpAddress
_VismSubNetMask_Object = MibScalar
vismSubNetMask = _VismSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1, 2),
    _VismSubNetMask_Type()
)
vismSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSubNetMask.setStatus("current")


class _VismControlTos_Type(Integer32):
    """Custom type vismControlTos based on Integer32"""
    defaultValue = 96

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismControlTos_Type.__name__ = "Integer32"
_VismControlTos_Object = MibScalar
vismControlTos = _VismControlTos_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1, 3),
    _VismControlTos_Type()
)
vismControlTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismControlTos.setStatus("current")
_VismBearerIpAddress_Type = IpAddress
_VismBearerIpAddress_Object = MibScalar
vismBearerIpAddress = _VismBearerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1, 4),
    _VismBearerIpAddress_Type()
)
vismBearerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerIpAddress.setStatus("current")
_VismBearerSubNetMask_Type = IpAddress
_VismBearerSubNetMask_Object = MibScalar
vismBearerSubNetMask = _VismBearerSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 1, 5),
    _VismBearerSubNetMask_Type()
)
vismBearerSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerSubNetMask.setStatus("current")
_VismVoIpGrp_ObjectIdentity = ObjectIdentity
vismVoIpGrp = _VismVoIpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2)
)


class _VismBearerTos_Type(Integer32):
    """Custom type vismBearerTos based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismBearerTos_Type.__name__ = "Integer32"
_VismBearerTos_Object = MibScalar
vismBearerTos = _VismBearerTos_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 1),
    _VismBearerTos_Type()
)
vismBearerTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerTos.setStatus("current")


class _VismRtcpRepInterval_Type(Integer32):
    """Custom type vismRtcpRepInterval based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 15000),
    )


_VismRtcpRepInterval_Type.__name__ = "Integer32"
_VismRtcpRepInterval_Object = MibScalar
vismRtcpRepInterval = _VismRtcpRepInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 2),
    _VismRtcpRepInterval_Type()
)
vismRtcpRepInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRtcpRepInterval.setStatus("current")
if mibBuilder.loadTexts:
    vismRtcpRepInterval.setUnits("milliseconds")


class _VismRtpReceiveTimer_Type(Integer32):
    """Custom type vismRtpReceiveTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VismRtpReceiveTimer_Type.__name__ = "Integer32"
_VismRtpReceiveTimer_Object = MibScalar
vismRtpReceiveTimer = _VismRtpReceiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 3),
    _VismRtpReceiveTimer_Type()
)
vismRtpReceiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRtpReceiveTimer.setStatus("current")


class _VismPacketizationPeriod_Type(Integer32):
    """Custom type vismPacketizationPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40)
        )
    )
    namedValues = NamedValues(
        *(("fourtyms", 40),
          ("tenms", 10),
          ("thirtyms", 30),
          ("twentyms", 20))
    )


_VismPacketizationPeriod_Type.__name__ = "Integer32"
_VismPacketizationPeriod_Object = MibScalar
vismPacketizationPeriod = _VismPacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 4),
    _VismPacketizationPeriod_Type()
)
vismPacketizationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPacketizationPeriod.setStatus("deprecated")


class _VismVoIpDtmfRelay_Type(TruthValue):
    """Custom type vismVoIpDtmfRelay based on TruthValue"""


_VismVoIpDtmfRelay_Object = MibScalar
vismVoIpDtmfRelay = _VismVoIpDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 5),
    _VismVoIpDtmfRelay_Type()
)
vismVoIpDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpDtmfRelay.setStatus("current")


class _VismVoIpCasTransport_Type(TruthValue):
    """Custom type vismVoIpCasTransport based on TruthValue"""


_VismVoIpCasTransport_Object = MibScalar
vismVoIpCasTransport = _VismVoIpCasTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 6),
    _VismVoIpCasTransport_Type()
)
vismVoIpCasTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpCasTransport.setStatus("current")


class _VismVoIpTripleRedundancy_Type(TruthValue):
    """Custom type vismVoIpTripleRedundancy based on TruthValue"""


_VismVoIpTripleRedundancy_Object = MibScalar
vismVoIpTripleRedundancy = _VismVoIpTripleRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 7),
    _VismVoIpTripleRedundancy_Type()
)
vismVoIpTripleRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpTripleRedundancy.setStatus("current")


class _VismVoIpVADTimer_Type(Integer32):
    """Custom type vismVoIpVADTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 65535),
    )


_VismVoIpVADTimer_Type.__name__ = "Integer32"
_VismVoIpVADTimer_Object = MibScalar
vismVoIpVADTimer = _VismVoIpVADTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 8),
    _VismVoIpVADTimer_Type()
)
vismVoIpVADTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpVADTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismVoIpVADTimer.setUnits("milliseconds")


class _VismVoIpNTECapabilityNegotiate_Type(TruthValue):
    """Custom type vismVoIpNTECapabilityNegotiate based on TruthValue"""


_VismVoIpNTECapabilityNegotiate_Object = MibScalar
vismVoIpNTECapabilityNegotiate = _VismVoIpNTECapabilityNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 9),
    _VismVoIpNTECapabilityNegotiate_Type()
)
vismVoIpNTECapabilityNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpNTECapabilityNegotiate.setStatus("current")


class _VismVoIpSIDPayloadType_Type(Integer32):
    """Custom type vismVoIpSIDPayloadType based on Integer32"""
    defaultValue = 13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismVoIpSIDPayloadType_Type.__name__ = "Integer32"
_VismVoIpSIDPayloadType_Object = MibScalar
vismVoIpSIDPayloadType = _VismVoIpSIDPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 10),
    _VismVoIpSIDPayloadType_Type()
)
vismVoIpSIDPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpSIDPayloadType.setStatus("current")


class _VismVoIpDPvcOamCellGap_Type(Integer32):
    """Custom type vismVoIpDPvcOamCellGap based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_VismVoIpDPvcOamCellGap_Type.__name__ = "Integer32"
_VismVoIpDPvcOamCellGap_Object = MibScalar
vismVoIpDPvcOamCellGap = _VismVoIpDPvcOamCellGap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 11),
    _VismVoIpDPvcOamCellGap_Type()
)
vismVoIpDPvcOamCellGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpDPvcOamCellGap.setStatus("current")
if mibBuilder.loadTexts:
    vismVoIpDPvcOamCellGap.setUnits("milliseconds")


class _VismVoIpDPvcRetryCnt_Type(Integer32):
    """Custom type vismVoIpDPvcRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_VismVoIpDPvcRetryCnt_Type.__name__ = "Integer32"
_VismVoIpDPvcRetryCnt_Object = MibScalar
vismVoIpDPvcRetryCnt = _VismVoIpDPvcRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 12),
    _VismVoIpDPvcRetryCnt_Type()
)
vismVoIpDPvcRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpDPvcRetryCnt.setStatus("current")


class _VismVoIpDPvcRecoverCnt_Type(Integer32):
    """Custom type vismVoIpDPvcRecoverCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_VismVoIpDPvcRecoverCnt_Type.__name__ = "Integer32"
_VismVoIpDPvcRecoverCnt_Object = MibScalar
vismVoIpDPvcRecoverCnt = _VismVoIpDPvcRecoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 13),
    _VismVoIpDPvcRecoverCnt_Type()
)
vismVoIpDPvcRecoverCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpDPvcRecoverCnt.setStatus("current")


class _VismRtcpRecvMultiplier_Type(Integer32):
    """Custom type vismRtcpRecvMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VismRtcpRecvMultiplier_Type.__name__ = "Integer32"
_VismRtcpRecvMultiplier_Object = MibScalar
vismRtcpRecvMultiplier = _VismRtcpRecvMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 14),
    _VismRtcpRecvMultiplier_Type()
)
vismRtcpRecvMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRtcpRecvMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    vismRtcpRecvMultiplier.setUnits("milliseconds")


class _VismVoIpLapdTrunkPVC_Type(Integer32):
    """Custom type vismVoIpLapdTrunkPVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bearer", 2),
          ("control", 1))
    )


_VismVoIpLapdTrunkPVC_Type.__name__ = "Integer32"
_VismVoIpLapdTrunkPVC_Object = MibScalar
vismVoIpLapdTrunkPVC = _VismVoIpLapdTrunkPVC_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 15),
    _VismVoIpLapdTrunkPVC_Type()
)
vismVoIpLapdTrunkPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpLapdTrunkPVC.setStatus("current")


class _VismVoIpEventNegotiationPolicy_Type(Integer32):
    """Custom type vismVoIpEventNegotiationPolicy based on Integer32"""
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
        *(("all", 3),
          ("none", 1),
          ("proprietary", 2))
    )


_VismVoIpEventNegotiationPolicy_Type.__name__ = "Integer32"
_VismVoIpEventNegotiationPolicy_Object = MibScalar
vismVoIpEventNegotiationPolicy = _VismVoIpEventNegotiationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 2, 16),
    _VismVoIpEventNegotiationPolicy_Type()
)
vismVoIpEventNegotiationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVoIpEventNegotiationPolicy.setStatus("current")
_VismDspGrp_ObjectIdentity = ObjectIdentity
vismDspGrp = _VismDspGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3)
)


class _VismEcanCnfIdlePattern_Type(Integer32):
    """Custom type vismEcanCnfIdlePattern based on Integer32"""
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
        *(("pattern1", 1),
          ("pattern2", 2),
          ("pattern3", 3),
          ("pattern4", 4))
    )


_VismEcanCnfIdlePattern_Type.__name__ = "Integer32"
_VismEcanCnfIdlePattern_Object = MibScalar
vismEcanCnfIdlePattern = _VismEcanCnfIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 1),
    _VismEcanCnfIdlePattern_Type()
)
vismEcanCnfIdlePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismEcanCnfIdlePattern.setStatus("deprecated")


class _VismEcanCnfIdleDirection_Type(Integer32):
    """Custom type vismEcanCnfIdleDirection based on Integer32"""
    defaultValue = 1

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
        *(("both", 1),
          ("either", 2),
          ("receive", 4),
          ("send", 3))
    )


_VismEcanCnfIdleDirection_Type.__name__ = "Integer32"
_VismEcanCnfIdleDirection_Object = MibScalar
vismEcanCnfIdleDirection = _VismEcanCnfIdleDirection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 2),
    _VismEcanCnfIdleDirection_Type()
)
vismEcanCnfIdleDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismEcanCnfIdleDirection.setStatus("deprecated")


class _VismCompCnfPacketSize_Type(Integer32):
    """Custom type vismCompCnfPacketSize based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
    )


_VismCompCnfPacketSize_Type.__name__ = "Integer32"
_VismCompCnfPacketSize_Object = MibScalar
vismCompCnfPacketSize = _VismCompCnfPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 3),
    _VismCompCnfPacketSize_Type()
)
vismCompCnfPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCompCnfPacketSize.setStatus("current")


class _VismERL_Type(Integer32):
    """Custom type vismERL based on Integer32"""
    defaultValue = 3

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
        *(("sixdb", 3),
          ("threedb", 2),
          ("worstdb", 4),
          ("zerodb", 1))
    )


_VismERL_Type.__name__ = "Integer32"
_VismERL_Object = MibScalar
vismERL = _VismERL_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 4),
    _VismERL_Type()
)
vismERL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismERL.setStatus("current")


class _VismJitterDelayMode_Type(Integer32):
    """Custom type vismJitterDelayMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_VismJitterDelayMode_Type.__name__ = "Integer32"
_VismJitterDelayMode_Object = MibScalar
vismJitterDelayMode = _VismJitterDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 5),
    _VismJitterDelayMode_Type()
)
vismJitterDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismJitterDelayMode.setStatus("deprecated")


class _VismJitterInitialDelay_Type(Integer32):
    """Custom type vismJitterInitialDelay based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eighty", 80),
          ("eightyfive", 85),
          ("fifteen", 15),
          ("fifty", 50),
          ("fiftyfive", 55),
          ("five", 5),
          ("fortyfive", 45),
          ("fourty", 40),
          ("hundred", 100),
          ("ninetyfive", 95),
          ("ninty", 90),
          ("seventy", 70),
          ("seventyfive", 75),
          ("sixty", 60),
          ("sixtyfive", 65),
          ("ten", 10),
          ("thirty", 30),
          ("thirtyfive", 35),
          ("twenty", 20),
          ("twentyfive", 25),
          ("zero", 1))
    )


_VismJitterInitialDelay_Type.__name__ = "Integer32"
_VismJitterInitialDelay_Object = MibScalar
vismJitterInitialDelay = _VismJitterInitialDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 6),
    _VismJitterInitialDelay_Type()
)
vismJitterInitialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismJitterInitialDelay.setStatus("deprecated")


class _VismAdaptiveGainControl_Type(Integer32):
    """Custom type vismAdaptiveGainControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_VismAdaptiveGainControl_Type.__name__ = "Integer32"
_VismAdaptiveGainControl_Object = MibScalar
vismAdaptiveGainControl = _VismAdaptiveGainControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 7),
    _VismAdaptiveGainControl_Type()
)
vismAdaptiveGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAdaptiveGainControl.setStatus("current")


class _VismDspHealth_Type(Integer32):
    """Custom type vismDspHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismDspHealth_Type.__name__ = "Integer32"
_VismDspHealth_Object = MibScalar
vismDspHealth = _VismDspHealth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 8),
    _VismDspHealth_Type()
)
vismDspHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDspHealth.setStatus("current")


class _VismUpspeedCodec_Type(Integer32):
    """Custom type vismUpspeedCodec based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 4),
          ("g-711a", 2),
          ("g-711u", 1),
          ("g-723h", 5),
          ("g-723l", 6),
          ("g-726-16", 7),
          ("g-726-24", 8),
          ("g-726-32", 3),
          ("g-726-40", 9))
    )


_VismUpspeedCodec_Type.__name__ = "Integer32"
_VismUpspeedCodec_Object = MibScalar
vismUpspeedCodec = _VismUpspeedCodec_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 9),
    _VismUpspeedCodec_Type()
)
vismUpspeedCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismUpspeedCodec.setStatus("current")


class _VismPayloadType_Type(Integer32):
    """Custom type vismPayloadType based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_VismPayloadType_Type.__name__ = "Integer32"
_VismPayloadType_Object = MibScalar
vismPayloadType = _VismPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 10),
    _VismPayloadType_Type()
)
vismPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismPayloadType.setStatus("current")


class _VismDSPHeartbeat_Type(Integer32):
    """Custom type vismDSPHeartbeat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismDSPHeartbeat_Type.__name__ = "Integer32"
_VismDSPHeartbeat_Object = MibScalar
vismDSPHeartbeat = _VismDSPHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 11),
    _VismDSPHeartbeat_Type()
)
vismDSPHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDSPHeartbeat.setStatus("current")


class _VismFaxDeJitterMode_Type(VismFaxDeJitterMode):
    """Custom type vismFaxDeJitterMode based on VismFaxDeJitterMode"""


_VismFaxDeJitterMode_Object = MibScalar
vismFaxDeJitterMode = _VismFaxDeJitterMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 12),
    _VismFaxDeJitterMode_Type()
)
vismFaxDeJitterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFaxDeJitterMode.setStatus("current")


class _VismFaxDeJitterInitialDelay_Type(VismFaxDeJitterInitDelay):
    """Custom type vismFaxDeJitterInitialDelay based on VismFaxDeJitterInitDelay"""


_VismFaxDeJitterInitialDelay_Object = MibScalar
vismFaxDeJitterInitialDelay = _VismFaxDeJitterInitialDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 3, 13),
    _VismFaxDeJitterInitialDelay_Type()
)
vismFaxDeJitterInitialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFaxDeJitterInitialDelay.setStatus("current")
_VismSystemGrp_ObjectIdentity = ObjectIdentity
vismSystemGrp = _VismSystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4)
)


class _VismDaughterCardSerialNum_Type(SnmpAdminString):
    """Custom type vismDaughterCardSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_VismDaughterCardSerialNum_Type.__name__ = "SnmpAdminString"
_VismDaughterCardSerialNum_Object = MibScalar
vismDaughterCardSerialNum = _VismDaughterCardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 1),
    _VismDaughterCardSerialNum_Type()
)
vismDaughterCardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDaughterCardSerialNum.setStatus("current")


class _VismDaughterCardDescription_Type(SnmpAdminString):
    """Custom type vismDaughterCardDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VismDaughterCardDescription_Type.__name__ = "SnmpAdminString"
_VismDaughterCardDescription_Object = MibScalar
vismDaughterCardDescription = _VismDaughterCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 2),
    _VismDaughterCardDescription_Type()
)
vismDaughterCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDaughterCardDescription.setStatus("current")


class _VismDaughterCardHWRev_Type(SnmpAdminString):
    """Custom type vismDaughterCardHWRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_VismDaughterCardHWRev_Type.__name__ = "SnmpAdminString"
_VismDaughterCardHWRev_Object = MibScalar
vismDaughterCardHWRev = _VismDaughterCardHWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 3),
    _VismDaughterCardHWRev_Type()
)
vismDaughterCardHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDaughterCardHWRev.setStatus("current")


class _VismEcanEncoding_Type(Integer32):
    """Custom type vismEcanEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 2),
          ("mu-law", 1))
    )


_VismEcanEncoding_Type.__name__ = "Integer32"
_VismEcanEncoding_Object = MibScalar
vismEcanEncoding = _VismEcanEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 4),
    _VismEcanEncoding_Type()
)
vismEcanEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismEcanEncoding.setStatus("current")


class _VismMode_Type(Integer32):
    """Custom type vismMode based on Integer32"""
    defaultValue = 1

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
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("aal1Svc", 3),
          ("aal2Trunking", 2),
          ("superMode", 99),
          ("switchedAal2CASBh", 6),
          ("switchedAal2Pvc", 8),
          ("switchedAal2Svc", 7),
          ("switchedVoipCASBh", 4),
          ("switchedVoipPRIBh", 5),
          ("unknownMode", 100),
          ("voipAndAal1Svc", 9),
          ("voipAndAal2Trunking", 10),
          ("voipSwitching", 1))
    )


_VismMode_Type.__name__ = "Integer32"
_VismMode_Object = MibScalar
vismMode = _VismMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 5),
    _VismMode_Type()
)
vismMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismMode.setStatus("current")


class _VismPrevMode_Type(Integer32):
    """Custom type vismPrevMode based on Integer32"""
    defaultValue = 1

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
        *(("aal1Svc", 3),
          ("aal2PvcSwitching", 4),
          ("aal2Trunking", 2),
          ("voipSwitching", 1))
    )


_VismPrevMode_Type.__name__ = "Integer32"
_VismPrevMode_Object = MibScalar
vismPrevMode = _VismPrevMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 6),
    _VismPrevMode_Type()
)
vismPrevMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPrevMode.setStatus("deprecated")


class _VismCacEnable_Type(Integer32):
    """Custom type vismCacEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VismCacEnable_Type.__name__ = "Integer32"
_VismCacEnable_Object = MibScalar
vismCacEnable = _VismCacEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 7),
    _VismCacEnable_Type()
)
vismCacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCacEnable.setStatus("current")


class _VismAvailableDs0Count_Type(Integer32):
    """Custom type vismAvailableDs0Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 248),
    )


_VismAvailableDs0Count_Type.__name__ = "Integer32"
_VismAvailableDs0Count_Object = MibScalar
vismAvailableDs0Count = _VismAvailableDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 8),
    _VismAvailableDs0Count_Type()
)
vismAvailableDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAvailableDs0Count.setStatus("current")


class _VismAppliedTemplate_Type(Integer32):
    """Custom type vismAppliedTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismAppliedTemplate_Type.__name__ = "Integer32"
_VismAppliedTemplate_Object = MibScalar
vismAppliedTemplate = _VismAppliedTemplate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 9),
    _VismAppliedTemplate_Type()
)
vismAppliedTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAppliedTemplate.setStatus("current")


class _VismTftpServerDn_Type(SnmpAdminString):
    """Custom type vismTftpServerDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismTftpServerDn_Type.__name__ = "SnmpAdminString"
_VismTftpServerDn_Object = MibScalar
vismTftpServerDn = _VismTftpServerDn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 11),
    _VismTftpServerDn_Type()
)
vismTftpServerDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismTftpServerDn.setStatus("current")


class _VismXgcpBearerNetworkType_Type(Integer32):
    """Custom type vismXgcpBearerNetworkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("ip", 1))
    )


_VismXgcpBearerNetworkType_Type.__name__ = "Integer32"
_VismXgcpBearerNetworkType_Object = MibScalar
vismXgcpBearerNetworkType = _VismXgcpBearerNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 12),
    _VismXgcpBearerNetworkType_Type()
)
vismXgcpBearerNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpBearerNetworkType.setStatus("current")


class _VismXgcpBearerVCType_Type(Integer32):
    """Custom type vismXgcpBearerVCType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_VismXgcpBearerVCType_Type.__name__ = "Integer32"
_VismXgcpBearerVCType_Object = MibScalar
vismXgcpBearerVCType = _VismXgcpBearerVCType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 13),
    _VismXgcpBearerVCType_Type()
)
vismXgcpBearerVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpBearerVCType.setStatus("current")


class _VismXgcpBearerConnectionType_Type(Integer32):
    """Custom type vismXgcpBearerConnectionType based on Integer32"""
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
        *(("aal1Sdt", 1),
          ("aal2", 2),
          ("notApplicable", 3))
    )


_VismXgcpBearerConnectionType_Type.__name__ = "Integer32"
_VismXgcpBearerConnectionType_Object = MibScalar
vismXgcpBearerConnectionType = _VismXgcpBearerConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 14),
    _VismXgcpBearerConnectionType_Type()
)
vismXgcpBearerConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpBearerConnectionType.setStatus("current")


class _VismBearerContinuityTimer_Type(Integer32):
    """Custom type vismBearerContinuityTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VismBearerContinuityTimer_Type.__name__ = "Integer32"
_VismBearerContinuityTimer_Object = MibScalar
vismBearerContinuityTimer = _VismBearerContinuityTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 15),
    _VismBearerContinuityTimer_Type()
)
vismBearerContinuityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerContinuityTimer.setStatus("current")


class _VismCodecNegotiationOption_Type(Integer32):
    """Custom type vismCodecNegotiationOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lclLcoRcd", 5),
          ("lclRcdLco", 6),
          ("lcoLclRcd", 2),
          ("lcoRcdLcl", 1),
          ("rcdLclLco", 4),
          ("rcdLcoLcl", 3))
    )


_VismCodecNegotiationOption_Type.__name__ = "Integer32"
_VismCodecNegotiationOption_Object = MibScalar
vismCodecNegotiationOption = _VismCodecNegotiationOption_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 16),
    _VismCodecNegotiationOption_Type()
)
vismCodecNegotiationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecNegotiationOption.setStatus("current")


class _VismProfileNegotiationOption_Type(Integer32):
    """Custom type vismProfileNegotiationOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lclLcoRcd", 5),
          ("lclRcdLco", 6),
          ("lcoLclRcd", 2),
          ("lcoRcdLcl", 1),
          ("rcdLclLco", 4),
          ("rcdLcoLcl", 3))
    )


_VismProfileNegotiationOption_Type.__name__ = "Integer32"
_VismProfileNegotiationOption_Object = MibScalar
vismProfileNegotiationOption = _VismProfileNegotiationOption_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 17),
    _VismProfileNegotiationOption_Type()
)
vismProfileNegotiationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismProfileNegotiationOption.setStatus("current")


class _VismCarrierLossPolicy_Type(Integer32):
    """Custom type vismCarrierLossPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("previousCodec", 1),
          ("upspeedCodec", 2))
    )


_VismCarrierLossPolicy_Type.__name__ = "Integer32"
_VismCarrierLossPolicy_Object = MibScalar
vismCarrierLossPolicy = _VismCarrierLossPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 18),
    _VismCarrierLossPolicy_Type()
)
vismCarrierLossPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCarrierLossPolicy.setStatus("current")


class _VismCacRejectionPolicy_Type(Integer32):
    """Custom type vismCacRejectionPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("maintain", 2))
    )


_VismCacRejectionPolicy_Type.__name__ = "Integer32"
_VismCacRejectionPolicy_Object = MibScalar
vismCacRejectionPolicy = _VismCacRejectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 19),
    _VismCacRejectionPolicy_Type()
)
vismCacRejectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCacRejectionPolicy.setStatus("current")


class _VismExtDnsServerDn_Type(SnmpAdminString):
    """Custom type vismExtDnsServerDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismExtDnsServerDn_Type.__name__ = "SnmpAdminString"
_VismExtDnsServerDn_Object = MibScalar
vismExtDnsServerDn = _VismExtDnsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 20),
    _VismExtDnsServerDn_Type()
)
vismExtDnsServerDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismExtDnsServerDn.setStatus("current")


class _VismFeatureBitMap_Type(Integer32):
    """Custom type vismFeatureBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismFeatureBitMap_Type.__name__ = "Integer32"
_VismFeatureBitMap_Object = MibScalar
vismFeatureBitMap = _VismFeatureBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 21),
    _VismFeatureBitMap_Type()
)
vismFeatureBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFeatureBitMap.setStatus("current")


class _VismVADTolerance_Type(Integer32):
    """Custom type vismVADTolerance based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VismVADTolerance_Type.__name__ = "Integer32"
_VismVADTolerance_Object = MibScalar
vismVADTolerance = _VismVADTolerance_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 22),
    _VismVADTolerance_Type()
)
vismVADTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVADTolerance.setStatus("current")


class _VismVADDutyCycle_Type(Integer32):
    """Custom type vismVADDutyCycle based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismVADDutyCycle_Type.__name__ = "Integer32"
_VismVADDutyCycle_Object = MibScalar
vismVADDutyCycle = _VismVADDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 23),
    _VismVADDutyCycle_Type()
)
vismVADDutyCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVADDutyCycle.setStatus("current")


class _VismAggregateTrafficClipping_Type(Integer32):
    """Custom type vismAggregateTrafficClipping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VismAggregateTrafficClipping_Type.__name__ = "Integer32"
_VismAggregateTrafficClipping_Object = MibScalar
vismAggregateTrafficClipping = _VismAggregateTrafficClipping_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 24),
    _VismAggregateTrafficClipping_Type()
)
vismAggregateTrafficClipping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAggregateTrafficClipping.setStatus("current")


class _VismAggregateSvcBandwidth_Type(Integer32):
    """Custom type vismAggregateSvcBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VismAggregateSvcBandwidth_Type.__name__ = "Integer32"
_VismAggregateSvcBandwidth_Object = MibScalar
vismAggregateSvcBandwidth = _VismAggregateSvcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 25),
    _VismAggregateSvcBandwidth_Type()
)
vismAggregateSvcBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAggregateSvcBandwidth.setStatus("current")


class _VismBearerContinuityTest_Type(TruthValue):
    """Custom type vismBearerContinuityTest based on TruthValue"""


_VismBearerContinuityTest_Object = MibScalar
vismBearerContinuityTest = _VismBearerContinuityTest_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 26),
    _VismBearerContinuityTest_Type()
)
vismBearerContinuityTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerContinuityTest.setStatus("current")


class _VismCaleaEnable_Type(TruthValue):
    """Custom type vismCaleaEnable based on TruthValue"""


_VismCaleaEnable_Object = MibScalar
vismCaleaEnable = _VismCaleaEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 27),
    _VismCaleaEnable_Type()
)
vismCaleaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCaleaEnable.setStatus("current")


class _VismMaxConfNum_Type(Integer32):
    """Custom type vismMaxConfNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VismMaxConfNum_Type.__name__ = "Integer32"
_VismMaxConfNum_Object = MibScalar
vismMaxConfNum = _VismMaxConfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 28),
    _VismMaxConfNum_Type()
)
vismMaxConfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismMaxConfNum.setStatus("current")


class _VismLongDurationTimer_Type(Integer32):
    """Custom type vismLongDurationTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_VismLongDurationTimer_Type.__name__ = "Integer32"
_VismLongDurationTimer_Object = MibScalar
vismLongDurationTimer = _VismLongDurationTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 29),
    _VismLongDurationTimer_Type()
)
vismLongDurationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLongDurationTimer.setStatus("current")


class _VismContinuityCo1Timer_Type(Integer32):
    """Custom type vismContinuityCo1Timer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_VismContinuityCo1Timer_Type.__name__ = "Integer32"
_VismContinuityCo1Timer_Object = MibScalar
vismContinuityCo1Timer = _VismContinuityCo1Timer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 30),
    _VismContinuityCo1Timer_Type()
)
vismContinuityCo1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismContinuityCo1Timer.setStatus("current")


class _VismContinuityCo2Timer_Type(Integer32):
    """Custom type vismContinuityCo2Timer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_VismContinuityCo2Timer_Type.__name__ = "Integer32"
_VismContinuityCo2Timer_Object = MibScalar
vismContinuityCo2Timer = _VismContinuityCo2Timer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 31),
    _VismContinuityCo2Timer_Type()
)
vismContinuityCo2Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismContinuityCo2Timer.setStatus("current")


class _VismReverseCotTone_Type(TruthValue):
    """Custom type vismReverseCotTone based on TruthValue"""


_VismReverseCotTone_Object = MibScalar
vismReverseCotTone = _VismReverseCotTone_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 32),
    _VismReverseCotTone_Type()
)
vismReverseCotTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismReverseCotTone.setStatus("current")


class _VismSendDnEnable_Type(TruthValue):
    """Custom type vismSendDnEnable based on TruthValue"""


_VismSendDnEnable_Object = MibScalar
vismSendDnEnable = _VismSendDnEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 33),
    _VismSendDnEnable_Type()
)
vismSendDnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSendDnEnable.setStatus("current")


class _VismSendDataGramSize_Type(Integer32):
    """Custom type vismSendDataGramSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VismSendDataGramSize_Type.__name__ = "Integer32"
_VismSendDataGramSize_Object = MibScalar
vismSendDataGramSize = _VismSendDataGramSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 34),
    _VismSendDataGramSize_Type()
)
vismSendDataGramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSendDataGramSize.setStatus("current")


class _VismOamLoopThreshold_Type(Integer32):
    """Custom type vismOamLoopThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VismOamLoopThreshold_Type.__name__ = "Integer32"
_VismOamLoopThreshold_Object = MibScalar
vismOamLoopThreshold = _VismOamLoopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 35),
    _VismOamLoopThreshold_Type()
)
vismOamLoopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismOamLoopThreshold.setStatus("current")


class _VismFreeDs0Threshold_Type(Integer32):
    """Custom type vismFreeDs0Threshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 248),
    )


_VismFreeDs0Threshold_Type.__name__ = "Integer32"
_VismFreeDs0Threshold_Object = MibScalar
vismFreeDs0Threshold = _VismFreeDs0Threshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 36),
    _VismFreeDs0Threshold_Type()
)
vismFreeDs0Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFreeDs0Threshold.setStatus("current")


class _VismCPUUtilizationThreshold_Type(Integer32):
    """Custom type vismCPUUtilizationThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismCPUUtilizationThreshold_Type.__name__ = "Integer32"
_VismCPUUtilizationThreshold_Object = MibScalar
vismCPUUtilizationThreshold = _VismCPUUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 37),
    _VismCPUUtilizationThreshold_Type()
)
vismCPUUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCPUUtilizationThreshold.setStatus("current")


class _VismMemoryUtilizationThreshold_Type(Integer32):
    """Custom type vismMemoryUtilizationThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismMemoryUtilizationThreshold_Type.__name__ = "Integer32"
_VismMemoryUtilizationThreshold_Object = MibScalar
vismMemoryUtilizationThreshold = _VismMemoryUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 38),
    _VismMemoryUtilizationThreshold_Type()
)
vismMemoryUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismMemoryUtilizationThreshold.setStatus("current")


class _VismDualToneDetect_Type(TruthValue):
    """Custom type vismDualToneDetect based on TruthValue"""


_VismDualToneDetect_Object = MibScalar
vismDualToneDetect = _VismDualToneDetect_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 39),
    _VismDualToneDetect_Type()
)
vismDualToneDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDualToneDetect.setStatus("current")


class _VismAisSuppression_Type(Integer32):
    """Custom type vismAisSuppression based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VismAisSuppression_Type.__name__ = "Integer32"
_VismAisSuppression_Object = MibScalar
vismAisSuppression = _VismAisSuppression_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 40),
    _VismAisSuppression_Type()
)
vismAisSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAisSuppression.setStatus("deprecated")


class _VismBearerIpPingEnable_Type(TruthValue):
    """Custom type vismBearerIpPingEnable based on TruthValue"""


_VismBearerIpPingEnable_Object = MibScalar
vismBearerIpPingEnable = _VismBearerIpPingEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 41),
    _VismBearerIpPingEnable_Type()
)
vismBearerIpPingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerIpPingEnable.setStatus("current")


class _VismTrapFilteringEnable_Type(TruthValue):
    """Custom type vismTrapFilteringEnable based on TruthValue"""


_VismTrapFilteringEnable_Object = MibScalar
vismTrapFilteringEnable = _VismTrapFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 42),
    _VismTrapFilteringEnable_Type()
)
vismTrapFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismTrapFilteringEnable.setStatus("current")


class _VismSplModemToneBitMap_Type(Bits):
    """Custom type vismSplModemToneBitMap based on Bits"""
    namedValues = NamedValues(
        ("vism1560980Tone", 0)
    )

_VismSplModemToneBitMap_Type.__name__ = "Bits"
_VismSplModemToneBitMap_Object = MibScalar
vismSplModemToneBitMap = _VismSplModemToneBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 43),
    _VismSplModemToneBitMap_Type()
)
vismSplModemToneBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSplModemToneBitMap.setStatus("current")


class _VismSSRCEnable_Type(TruthValue):
    """Custom type vismSSRCEnable based on TruthValue"""


_VismSSRCEnable_Object = MibScalar
vismSSRCEnable = _VismSSRCEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 44),
    _VismSSRCEnable_Type()
)
vismSSRCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSSRCEnable.setStatus("current")


class _VismOamLoopbackSetCLP_Type(TruthValue):
    """Custom type vismOamLoopbackSetCLP based on TruthValue"""


_VismOamLoopbackSetCLP_Object = MibScalar
vismOamLoopbackSetCLP = _VismOamLoopbackSetCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 45),
    _VismOamLoopbackSetCLP_Type()
)
vismOamLoopbackSetCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismOamLoopbackSetCLP.setStatus("current")


class _VismPvcAlarmLogEnable_Type(TruthValue):
    """Custom type vismPvcAlarmLogEnable based on TruthValue"""


_VismPvcAlarmLogEnable_Object = MibScalar
vismPvcAlarmLogEnable = _VismPvcAlarmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 46),
    _VismPvcAlarmLogEnable_Type()
)
vismPvcAlarmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismPvcAlarmLogEnable.setStatus("current")


class _VismPvcAlarmLogAdminTimer_Type(Unsigned32):
    """Custom type vismPvcAlarmLogAdminTimer based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismPvcAlarmLogAdminTimer_Type.__name__ = "Unsigned32"
_VismPvcAlarmLogAdminTimer_Object = MibScalar
vismPvcAlarmLogAdminTimer = _VismPvcAlarmLogAdminTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 47),
    _VismPvcAlarmLogAdminTimer_Type()
)
vismPvcAlarmLogAdminTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismPvcAlarmLogAdminTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismPvcAlarmLogAdminTimer.setUnits("minutes")


class _VismPvcAlarmLogOperTimer_Type(Unsigned32):
    """Custom type vismPvcAlarmLogOperTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismPvcAlarmLogOperTimer_Type.__name__ = "Unsigned32"
_VismPvcAlarmLogOperTimer_Object = MibScalar
vismPvcAlarmLogOperTimer = _VismPvcAlarmLogOperTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 48),
    _VismPvcAlarmLogOperTimer_Type()
)
vismPvcAlarmLogOperTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPvcAlarmLogOperTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismPvcAlarmLogOperTimer.setUnits("minutes")


class _VismContinuityCheckCellEnable_Type(TruthValue):
    """Custom type vismContinuityCheckCellEnable based on TruthValue"""


_VismContinuityCheckCellEnable_Object = MibScalar
vismContinuityCheckCellEnable = _VismContinuityCheckCellEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 4, 49),
    _VismContinuityCheckCellEnable_Type()
)
vismContinuityCheckCellEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismContinuityCheckCellEnable.setStatus("current")
_VismTrapObjGrp_ObjectIdentity = ObjectIdentity
vismTrapObjGrp = _VismTrapObjGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5)
)


class _VismConfigChangeTypeBitMap_Type(Integer32):
    """Custom type vismConfigChangeTypeBitMap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismConfigChangeTypeBitMap_Type.__name__ = "Integer32"
_VismConfigChangeTypeBitMap_Object = MibScalar
vismConfigChangeTypeBitMap = _VismConfigChangeTypeBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5, 1),
    _VismConfigChangeTypeBitMap_Type()
)
vismConfigChangeTypeBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismConfigChangeTypeBitMap.setStatus("current")


class _VismTrapIntIndex1_Type(Integer32):
    """Custom type vismTrapIntIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismTrapIntIndex1_Type.__name__ = "Integer32"
_VismTrapIntIndex1_Object = MibScalar
vismTrapIntIndex1 = _VismTrapIntIndex1_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5, 2),
    _VismTrapIntIndex1_Type()
)
vismTrapIntIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismTrapIntIndex1.setStatus("current")


class _VismTrapIntIndex2_Type(Integer32):
    """Custom type vismTrapIntIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismTrapIntIndex2_Type.__name__ = "Integer32"
_VismTrapIntIndex2_Object = MibScalar
vismTrapIntIndex2 = _VismTrapIntIndex2_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5, 3),
    _VismTrapIntIndex2_Type()
)
vismTrapIntIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismTrapIntIndex2.setStatus("current")


class _VismTrapStrIndex1_Type(OctetString):
    """Custom type vismTrapStrIndex1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_VismTrapStrIndex1_Type.__name__ = "OctetString"
_VismTrapStrIndex1_Object = MibScalar
vismTrapStrIndex1 = _VismTrapStrIndex1_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5, 4),
    _VismTrapStrIndex1_Type()
)
vismTrapStrIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismTrapStrIndex1.setStatus("current")


class _VismTrapIntegerValue_Type(Integer32):
    """Custom type vismTrapIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismTrapIntegerValue_Type.__name__ = "Integer32"
_VismTrapIntegerValue_Object = MibScalar
vismTrapIntegerValue = _VismTrapIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 5, 5),
    _VismTrapIntegerValue_Type()
)
vismTrapIntegerValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vismTrapIntegerValue.setStatus("current")
_VismAal2Grp_ObjectIdentity = ObjectIdentity
vismAal2Grp = _VismAal2Grp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6)
)
_VismAal2SubcellMuxing_Type = TruthValue
_VismAal2SubcellMuxing_Object = MibScalar
vismAal2SubcellMuxing = _VismAal2SubcellMuxing_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 1),
    _VismAal2SubcellMuxing_Type()
)
vismAal2SubcellMuxing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2SubcellMuxing.setStatus("current")


class _VismAal2DtmfRelay_Type(TruthValue):
    """Custom type vismAal2DtmfRelay based on TruthValue"""


_VismAal2DtmfRelay_Object = MibScalar
vismAal2DtmfRelay = _VismAal2DtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 2),
    _VismAal2DtmfRelay_Type()
)
vismAal2DtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2DtmfRelay.setStatus("current")


class _VismAal2CasTransport_Type(TruthValue):
    """Custom type vismAal2CasTransport based on TruthValue"""


_VismAal2CasTransport_Object = MibScalar
vismAal2CasTransport = _VismAal2CasTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 3),
    _VismAal2CasTransport_Type()
)
vismAal2CasTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CasTransport.setStatus("current")


class _VismAal2Type3Redundancy_Type(TruthValue):
    """Custom type vismAal2Type3Redundancy based on TruthValue"""


_VismAal2Type3Redundancy_Object = MibScalar
vismAal2Type3Redundancy = _VismAal2Type3Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 4),
    _VismAal2Type3Redundancy_Type()
)
vismAal2Type3Redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2Type3Redundancy.setStatus("current")


class _VismAal2VADTimer_Type(Integer32):
    """Custom type vismAal2VADTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 65535),
    )


_VismAal2VADTimer_Type.__name__ = "Integer32"
_VismAal2VADTimer_Object = MibScalar
vismAal2VADTimer = _VismAal2VADTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 5),
    _VismAal2VADTimer_Type()
)
vismAal2VADTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2VADTimer.setStatus("current")


class _VismAal2CidFillTimer_Type(Integer32):
    """Custom type vismAal2CidFillTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_VismAal2CidFillTimer_Type.__name__ = "Integer32"
_VismAal2CidFillTimer_Object = MibScalar
vismAal2CidFillTimer = _VismAal2CidFillTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 6, 6),
    _VismAal2CidFillTimer_Type()
)
vismAal2CidFillTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidFillTimer.setStatus("current")
_VismInteropGrp_ObjectIdentity = ObjectIdentity
vismInteropGrp = _VismInteropGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 7)
)


class _VismXgcpSdpOst_Type(Integer32):
    """Custom type vismXgcpSdpOst based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VismXgcpSdpOst_Type.__name__ = "Integer32"
_VismXgcpSdpOst_Object = MibScalar
vismXgcpSdpOst = _VismXgcpSdpOst_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 7, 1),
    _VismXgcpSdpOst_Type()
)
vismXgcpSdpOst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpSdpOst.setStatus("current")


class _VismDynamicPT_Type(Integer32):
    """Custom type vismDynamicPT based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VismDynamicPT_Type.__name__ = "Integer32"
_VismDynamicPT_Object = MibScalar
vismDynamicPT = _VismDynamicPT_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 17, 7, 2),
    _VismDynamicPT_Type()
)
vismDynamicPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDynamicPT.setStatus("current")
_VismSystemPerfStats_ObjectIdentity = ObjectIdentity
vismSystemPerfStats = _VismSystemPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 25)
)


class _VismCPUUtilization_Type(Integer32):
    """Custom type vismCPUUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismCPUUtilization_Type.__name__ = "Integer32"
_VismCPUUtilization_Object = MibScalar
vismCPUUtilization = _VismCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 25, 1),
    _VismCPUUtilization_Type()
)
vismCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCPUUtilization.setStatus("current")


class _VismMemoryUtilization_Type(Integer32):
    """Custom type vismMemoryUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismMemoryUtilization_Type.__name__ = "Integer32"
_VismMemoryUtilization_Object = MibScalar
vismMemoryUtilization = _VismMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 25, 2),
    _VismMemoryUtilization_Type()
)
vismMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismMemoryUtilization.setStatus("current")


class _VismSysPerfClrButton_Type(Integer32):
    """Custom type vismSysPerfClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_VismSysPerfClrButton_Type.__name__ = "Integer32"
_VismSysPerfClrButton_Object = MibScalar
vismSysPerfClrButton = _VismSysPerfClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 25, 3),
    _VismSysPerfClrButton_Type()
)
vismSysPerfClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSysPerfClrButton.setStatus("current")
_VismCallStats_ObjectIdentity = ObjectIdentity
vismCallStats = _VismCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 13)
)


class _VismTotalCalls_Type(Integer32):
    """Custom type vismTotalCalls based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismTotalCalls_Type.__name__ = "Integer32"
_VismTotalCalls_Object = MibScalar
vismTotalCalls = _VismTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 13, 1),
    _VismTotalCalls_Type()
)
vismTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismTotalCalls.setStatus("current")


class _VismSuccessfulCalls_Type(Integer32):
    """Custom type vismSuccessfulCalls based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSuccessfulCalls_Type.__name__ = "Integer32"
_VismSuccessfulCalls_Object = MibScalar
vismSuccessfulCalls = _VismSuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 13, 2),
    _VismSuccessfulCalls_Type()
)
vismSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSuccessfulCalls.setStatus("current")


class _VismFailedCalls_Type(Integer32):
    """Custom type vismFailedCalls based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismFailedCalls_Type.__name__ = "Integer32"
_VismFailedCalls_Object = MibScalar
vismFailedCalls = _VismFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 13, 3),
    _VismFailedCalls_Type()
)
vismFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismFailedCalls.setStatus("current")


class _VismCallStatsClrButton_Type(Integer32):
    """Custom type vismCallStatsClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_VismCallStatsClrButton_Type.__name__ = "Integer32"
_VismCallStatsClrButton_Object = MibScalar
vismCallStatsClrButton = _VismCallStatsClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 13, 4),
    _VismCallStatsClrButton_Type()
)
vismCallStatsClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCallStatsClrButton.setStatus("current")
_CiscoVismModuleMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismModuleMIBConformance = _CiscoVismModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2)
)
_CiscoVismModuleMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismModuleMIBGroups = _CiscoVismModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1)
)
_CiscoVismModuleMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismModuleMIBCompliances = _CiscoVismModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2)
)

# Managed Objects groups

ciscoVismPerfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 1)
)
ciscoVismPerfStatsGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismCPUUtilization"),
        ("CISCO-VISM-MODULE-MIB", "vismMemoryUtilization"),
        ("CISCO-VISM-MODULE-MIB", "vismSysPerfClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismPerfStatsGroup.setStatus("current")

ciscoVismCallStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 2)
)
ciscoVismCallStatsGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismTotalCalls"),
        ("CISCO-VISM-MODULE-MIB", "vismSuccessfulCalls"),
        ("CISCO-VISM-MODULE-MIB", "vismFailedCalls"),
        ("CISCO-VISM-MODULE-MIB", "vismCallStatsClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismCallStatsGroup.setStatus("current")

ciscoVismIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 3)
)
ciscoVismIpGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismIpAddress"),
        ("CISCO-VISM-MODULE-MIB", "vismSubNetMask"),
        ("CISCO-VISM-MODULE-MIB", "vismControlTos"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerIpAddress"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerSubNetMask"))
)
if mibBuilder.loadTexts:
    ciscoVismIpGroup.setStatus("current")

ciscoVismVoIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 4)
)
ciscoVismVoIpGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismBearerTos"),
        ("CISCO-VISM-MODULE-MIB", "vismRtcpRepInterval"),
        ("CISCO-VISM-MODULE-MIB", "vismRtpReceiveTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpDtmfRelay"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpCasTransport"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpTripleRedundancy"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpVADTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpNTECapabilityNegotiate"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpSIDPayloadType"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpDPvcOamCellGap"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpDPvcRetryCnt"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpDPvcRecoverCnt"),
        ("CISCO-VISM-MODULE-MIB", "vismRtcpRecvMultiplier"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpLapdTrunkPVC"),
        ("CISCO-VISM-MODULE-MIB", "vismVoIpEventNegotiationPolicy"))
)
if mibBuilder.loadTexts:
    ciscoVismVoIpGroup.setStatus("current")

ciscoVismDspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 5)
)
ciscoVismDspGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismCompCnfPacketSize"),
        ("CISCO-VISM-MODULE-MIB", "vismERL"),
        ("CISCO-VISM-MODULE-MIB", "vismAdaptiveGainControl"),
        ("CISCO-VISM-MODULE-MIB", "vismDspHealth"),
        ("CISCO-VISM-MODULE-MIB", "vismUpspeedCodec"),
        ("CISCO-VISM-MODULE-MIB", "vismPayloadType"),
        ("CISCO-VISM-MODULE-MIB", "vismDSPHeartbeat"))
)
if mibBuilder.loadTexts:
    ciscoVismDspGroup.setStatus("current")

ciscoVismSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 6)
)
ciscoVismSystemGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismDaughterCardSerialNum"),
        ("CISCO-VISM-MODULE-MIB", "vismDaughterCardDescription"),
        ("CISCO-VISM-MODULE-MIB", "vismDaughterCardHWRev"),
        ("CISCO-VISM-MODULE-MIB", "vismEcanEncoding"),
        ("CISCO-VISM-MODULE-MIB", "vismMode"),
        ("CISCO-VISM-MODULE-MIB", "vismCacEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismAvailableDs0Count"),
        ("CISCO-VISM-MODULE-MIB", "vismAppliedTemplate"),
        ("CISCO-VISM-MODULE-MIB", "vismTftpServerDn"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerNetworkType"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerVCType"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerConnectionType"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerContinuityTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismCodecNegotiationOption"),
        ("CISCO-VISM-MODULE-MIB", "vismProfileNegotiationOption"),
        ("CISCO-VISM-MODULE-MIB", "vismCarrierLossPolicy"),
        ("CISCO-VISM-MODULE-MIB", "vismCacRejectionPolicy"),
        ("CISCO-VISM-MODULE-MIB", "vismExtDnsServerDn"),
        ("CISCO-VISM-MODULE-MIB", "vismFeatureBitMap"),
        ("CISCO-VISM-MODULE-MIB", "vismVADTolerance"),
        ("CISCO-VISM-MODULE-MIB", "vismVADDutyCycle"),
        ("CISCO-VISM-MODULE-MIB", "vismAggregateTrafficClipping"),
        ("CISCO-VISM-MODULE-MIB", "vismAggregateSvcBandwidth"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerContinuityTest"),
        ("CISCO-VISM-MODULE-MIB", "vismCaleaEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismMaxConfNum"),
        ("CISCO-VISM-MODULE-MIB", "vismLongDurationTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismContinuityCo1Timer"),
        ("CISCO-VISM-MODULE-MIB", "vismContinuityCo2Timer"),
        ("CISCO-VISM-MODULE-MIB", "vismReverseCotTone"),
        ("CISCO-VISM-MODULE-MIB", "vismSendDnEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismSendDataGramSize"),
        ("CISCO-VISM-MODULE-MIB", "vismOamLoopThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismFreeDs0Threshold"),
        ("CISCO-VISM-MODULE-MIB", "vismCPUUtilizationThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismMemoryUtilizationThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismDualToneDetect"),
        ("CISCO-VISM-MODULE-MIB", "vismAisSuppression"))
)
if mibBuilder.loadTexts:
    ciscoVismSystemGroup.setStatus("deprecated")

ciscoVismInteropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 7)
)
ciscoVismInteropGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismXgcpSdpOst"),
        ("CISCO-VISM-MODULE-MIB", "vismDynamicPT"))
)
if mibBuilder.loadTexts:
    ciscoVismInteropGroup.setStatus("current")

ciscoVismTrapObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 8)
)
ciscoVismTrapObjGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismConfigChangeTypeBitMap"),
        ("CISCO-VISM-MODULE-MIB", "vismTrapIntIndex1"),
        ("CISCO-VISM-MODULE-MIB", "vismTrapIntIndex2"),
        ("CISCO-VISM-MODULE-MIB", "vismTrapStrIndex1"))
)
if mibBuilder.loadTexts:
    ciscoVismTrapObjGroup.setStatus("current")

ciscoVismAal2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 9)
)
ciscoVismAal2Group.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismAal2SubcellMuxing"),
        ("CISCO-VISM-MODULE-MIB", "vismAal2DtmfRelay"),
        ("CISCO-VISM-MODULE-MIB", "vismAal2CasTransport"),
        ("CISCO-VISM-MODULE-MIB", "vismAal2Type3Redundancy"),
        ("CISCO-VISM-MODULE-MIB", "vismAal2VADTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismAal2CidFillTimer"))
)
if mibBuilder.loadTexts:
    ciscoVismAal2Group.setStatus("current")

ciscoVismDspDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 10)
)
ciscoVismDspDeprecatedGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismEcanCnfIdlePattern"),
        ("CISCO-VISM-MODULE-MIB", "vismEcanCnfIdleDirection"),
        ("CISCO-VISM-MODULE-MIB", "vismJitterDelayMode"),
        ("CISCO-VISM-MODULE-MIB", "vismJitterInitialDelay"))
)
if mibBuilder.loadTexts:
    ciscoVismDspDeprecatedGroup.setStatus("deprecated")

ciscoVismSystemDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 11)
)
ciscoVismSystemDeprecatedGroup.setObjects(
    ("CISCO-VISM-MODULE-MIB", "vismPrevMode")
)
if mibBuilder.loadTexts:
    ciscoVismSystemDeprecatedGroup.setStatus("deprecated")

ciscoVismVoIpDeprecateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 12)
)
ciscoVismVoIpDeprecateGroup.setObjects(
    ("CISCO-VISM-MODULE-MIB", "vismPacketizationPeriod")
)
if mibBuilder.loadTexts:
    ciscoVismVoIpDeprecateGroup.setStatus("deprecated")

ciscoVismSystemGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 13)
)
ciscoVismSystemGroup1.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismDaughterCardSerialNum"),
        ("CISCO-VISM-MODULE-MIB", "vismDaughterCardDescription"),
        ("CISCO-VISM-MODULE-MIB", "vismDaughterCardHWRev"),
        ("CISCO-VISM-MODULE-MIB", "vismEcanEncoding"),
        ("CISCO-VISM-MODULE-MIB", "vismMode"),
        ("CISCO-VISM-MODULE-MIB", "vismCacEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismAvailableDs0Count"),
        ("CISCO-VISM-MODULE-MIB", "vismAppliedTemplate"),
        ("CISCO-VISM-MODULE-MIB", "vismTftpServerDn"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerNetworkType"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerVCType"),
        ("CISCO-VISM-MODULE-MIB", "vismXgcpBearerConnectionType"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerContinuityTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismCodecNegotiationOption"),
        ("CISCO-VISM-MODULE-MIB", "vismProfileNegotiationOption"),
        ("CISCO-VISM-MODULE-MIB", "vismCarrierLossPolicy"),
        ("CISCO-VISM-MODULE-MIB", "vismCacRejectionPolicy"),
        ("CISCO-VISM-MODULE-MIB", "vismExtDnsServerDn"),
        ("CISCO-VISM-MODULE-MIB", "vismFeatureBitMap"),
        ("CISCO-VISM-MODULE-MIB", "vismVADTolerance"),
        ("CISCO-VISM-MODULE-MIB", "vismVADDutyCycle"),
        ("CISCO-VISM-MODULE-MIB", "vismAggregateTrafficClipping"),
        ("CISCO-VISM-MODULE-MIB", "vismAggregateSvcBandwidth"),
        ("CISCO-VISM-MODULE-MIB", "vismBearerContinuityTest"),
        ("CISCO-VISM-MODULE-MIB", "vismCaleaEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismMaxConfNum"),
        ("CISCO-VISM-MODULE-MIB", "vismLongDurationTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismContinuityCo1Timer"),
        ("CISCO-VISM-MODULE-MIB", "vismContinuityCo2Timer"),
        ("CISCO-VISM-MODULE-MIB", "vismReverseCotTone"),
        ("CISCO-VISM-MODULE-MIB", "vismSendDnEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismSendDataGramSize"),
        ("CISCO-VISM-MODULE-MIB", "vismOamLoopThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismFreeDs0Threshold"),
        ("CISCO-VISM-MODULE-MIB", "vismCPUUtilizationThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismMemoryUtilizationThreshold"),
        ("CISCO-VISM-MODULE-MIB", "vismDualToneDetect"))
)
if mibBuilder.loadTexts:
    ciscoVismSystemGroup1.setStatus("current")

ciscoVismSystemFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 14)
)
ciscoVismSystemFeatureGroup.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismBearerIpPingEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismTrapFilteringEnable"))
)
if mibBuilder.loadTexts:
    ciscoVismSystemFeatureGroup.setStatus("deprecated")

ciscoVismTrapVarbindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 15)
)
ciscoVismTrapVarbindGroup.setObjects(
    ("CISCO-VISM-MODULE-MIB", "vismTrapIntegerValue")
)
if mibBuilder.loadTexts:
    ciscoVismTrapVarbindGroup.setStatus("current")

ciscoVismSystemFeatureGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 16)
)
ciscoVismSystemFeatureGroupRev1.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismBearerIpPingEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismTrapFilteringEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismSplModemToneBitMap"),
        ("CISCO-VISM-MODULE-MIB", "vismSSRCEnable"))
)
if mibBuilder.loadTexts:
    ciscoVismSystemFeatureGroupRev1.setStatus("current")

ciscoVismSystemGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 17)
)
ciscoVismSystemGroupSup1.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismOamLoopbackSetCLP"),
        ("CISCO-VISM-MODULE-MIB", "vismPvcAlarmLogEnable"),
        ("CISCO-VISM-MODULE-MIB", "vismPvcAlarmLogAdminTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismPvcAlarmLogOperTimer"),
        ("CISCO-VISM-MODULE-MIB", "vismContinuityCheckCellEnable"))
)
if mibBuilder.loadTexts:
    ciscoVismSystemGroupSup1.setStatus("current")

ciscoVismDspGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 1, 18)
)
ciscoVismDspGroupSup1.setObjects(
      *(("CISCO-VISM-MODULE-MIB", "vismFaxDeJitterMode"),
        ("CISCO-VISM-MODULE-MIB", "vismFaxDeJitterInitialDelay"))
)
if mibBuilder.loadTexts:
    ciscoVismDspGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismModuleCompliance.setStatus(
        "deprecated"
    )

ciscoVismModuleCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoVismModuleCompliance1.setStatus(
        "deprecated"
    )

ciscoVismModuleComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ciscoVismModuleComplianceRev2.setStatus(
        "deprecated"
    )

ciscoVismModuleComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ciscoVismModuleComplianceRev3.setStatus(
        "deprecated"
    )

ciscoVismModuleComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 82, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ciscoVismModuleComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-MODULE-MIB",
    **{"VismFaxDeJitterMode": VismFaxDeJitterMode,
       "VismFaxDeJitterInitDelay": VismFaxDeJitterInitDelay,
       "vismConfig": vismConfig,
       "vismIpGrp": vismIpGrp,
       "vismIpAddress": vismIpAddress,
       "vismSubNetMask": vismSubNetMask,
       "vismControlTos": vismControlTos,
       "vismBearerIpAddress": vismBearerIpAddress,
       "vismBearerSubNetMask": vismBearerSubNetMask,
       "vismVoIpGrp": vismVoIpGrp,
       "vismBearerTos": vismBearerTos,
       "vismRtcpRepInterval": vismRtcpRepInterval,
       "vismRtpReceiveTimer": vismRtpReceiveTimer,
       "vismPacketizationPeriod": vismPacketizationPeriod,
       "vismVoIpDtmfRelay": vismVoIpDtmfRelay,
       "vismVoIpCasTransport": vismVoIpCasTransport,
       "vismVoIpTripleRedundancy": vismVoIpTripleRedundancy,
       "vismVoIpVADTimer": vismVoIpVADTimer,
       "vismVoIpNTECapabilityNegotiate": vismVoIpNTECapabilityNegotiate,
       "vismVoIpSIDPayloadType": vismVoIpSIDPayloadType,
       "vismVoIpDPvcOamCellGap": vismVoIpDPvcOamCellGap,
       "vismVoIpDPvcRetryCnt": vismVoIpDPvcRetryCnt,
       "vismVoIpDPvcRecoverCnt": vismVoIpDPvcRecoverCnt,
       "vismRtcpRecvMultiplier": vismRtcpRecvMultiplier,
       "vismVoIpLapdTrunkPVC": vismVoIpLapdTrunkPVC,
       "vismVoIpEventNegotiationPolicy": vismVoIpEventNegotiationPolicy,
       "vismDspGrp": vismDspGrp,
       "vismEcanCnfIdlePattern": vismEcanCnfIdlePattern,
       "vismEcanCnfIdleDirection": vismEcanCnfIdleDirection,
       "vismCompCnfPacketSize": vismCompCnfPacketSize,
       "vismERL": vismERL,
       "vismJitterDelayMode": vismJitterDelayMode,
       "vismJitterInitialDelay": vismJitterInitialDelay,
       "vismAdaptiveGainControl": vismAdaptiveGainControl,
       "vismDspHealth": vismDspHealth,
       "vismUpspeedCodec": vismUpspeedCodec,
       "vismPayloadType": vismPayloadType,
       "vismDSPHeartbeat": vismDSPHeartbeat,
       "vismFaxDeJitterMode": vismFaxDeJitterMode,
       "vismFaxDeJitterInitialDelay": vismFaxDeJitterInitialDelay,
       "vismSystemGrp": vismSystemGrp,
       "vismDaughterCardSerialNum": vismDaughterCardSerialNum,
       "vismDaughterCardDescription": vismDaughterCardDescription,
       "vismDaughterCardHWRev": vismDaughterCardHWRev,
       "vismEcanEncoding": vismEcanEncoding,
       "vismMode": vismMode,
       "vismPrevMode": vismPrevMode,
       "vismCacEnable": vismCacEnable,
       "vismAvailableDs0Count": vismAvailableDs0Count,
       "vismAppliedTemplate": vismAppliedTemplate,
       "vismTftpServerDn": vismTftpServerDn,
       "vismXgcpBearerNetworkType": vismXgcpBearerNetworkType,
       "vismXgcpBearerVCType": vismXgcpBearerVCType,
       "vismXgcpBearerConnectionType": vismXgcpBearerConnectionType,
       "vismBearerContinuityTimer": vismBearerContinuityTimer,
       "vismCodecNegotiationOption": vismCodecNegotiationOption,
       "vismProfileNegotiationOption": vismProfileNegotiationOption,
       "vismCarrierLossPolicy": vismCarrierLossPolicy,
       "vismCacRejectionPolicy": vismCacRejectionPolicy,
       "vismExtDnsServerDn": vismExtDnsServerDn,
       "vismFeatureBitMap": vismFeatureBitMap,
       "vismVADTolerance": vismVADTolerance,
       "vismVADDutyCycle": vismVADDutyCycle,
       "vismAggregateTrafficClipping": vismAggregateTrafficClipping,
       "vismAggregateSvcBandwidth": vismAggregateSvcBandwidth,
       "vismBearerContinuityTest": vismBearerContinuityTest,
       "vismCaleaEnable": vismCaleaEnable,
       "vismMaxConfNum": vismMaxConfNum,
       "vismLongDurationTimer": vismLongDurationTimer,
       "vismContinuityCo1Timer": vismContinuityCo1Timer,
       "vismContinuityCo2Timer": vismContinuityCo2Timer,
       "vismReverseCotTone": vismReverseCotTone,
       "vismSendDnEnable": vismSendDnEnable,
       "vismSendDataGramSize": vismSendDataGramSize,
       "vismOamLoopThreshold": vismOamLoopThreshold,
       "vismFreeDs0Threshold": vismFreeDs0Threshold,
       "vismCPUUtilizationThreshold": vismCPUUtilizationThreshold,
       "vismMemoryUtilizationThreshold": vismMemoryUtilizationThreshold,
       "vismDualToneDetect": vismDualToneDetect,
       "vismAisSuppression": vismAisSuppression,
       "vismBearerIpPingEnable": vismBearerIpPingEnable,
       "vismTrapFilteringEnable": vismTrapFilteringEnable,
       "vismSplModemToneBitMap": vismSplModemToneBitMap,
       "vismSSRCEnable": vismSSRCEnable,
       "vismOamLoopbackSetCLP": vismOamLoopbackSetCLP,
       "vismPvcAlarmLogEnable": vismPvcAlarmLogEnable,
       "vismPvcAlarmLogAdminTimer": vismPvcAlarmLogAdminTimer,
       "vismPvcAlarmLogOperTimer": vismPvcAlarmLogOperTimer,
       "vismContinuityCheckCellEnable": vismContinuityCheckCellEnable,
       "vismTrapObjGrp": vismTrapObjGrp,
       "vismConfigChangeTypeBitMap": vismConfigChangeTypeBitMap,
       "vismTrapIntIndex1": vismTrapIntIndex1,
       "vismTrapIntIndex2": vismTrapIntIndex2,
       "vismTrapStrIndex1": vismTrapStrIndex1,
       "vismTrapIntegerValue": vismTrapIntegerValue,
       "vismAal2Grp": vismAal2Grp,
       "vismAal2SubcellMuxing": vismAal2SubcellMuxing,
       "vismAal2DtmfRelay": vismAal2DtmfRelay,
       "vismAal2CasTransport": vismAal2CasTransport,
       "vismAal2Type3Redundancy": vismAal2Type3Redundancy,
       "vismAal2VADTimer": vismAal2VADTimer,
       "vismAal2CidFillTimer": vismAal2CidFillTimer,
       "vismInteropGrp": vismInteropGrp,
       "vismXgcpSdpOst": vismXgcpSdpOst,
       "vismDynamicPT": vismDynamicPT,
       "vismSystemPerfStats": vismSystemPerfStats,
       "vismCPUUtilization": vismCPUUtilization,
       "vismMemoryUtilization": vismMemoryUtilization,
       "vismSysPerfClrButton": vismSysPerfClrButton,
       "vismCallStats": vismCallStats,
       "vismTotalCalls": vismTotalCalls,
       "vismSuccessfulCalls": vismSuccessfulCalls,
       "vismFailedCalls": vismFailedCalls,
       "vismCallStatsClrButton": vismCallStatsClrButton,
       "ciscoVismModuleMIB": ciscoVismModuleMIB,
       "ciscoVismModuleMIBConformance": ciscoVismModuleMIBConformance,
       "ciscoVismModuleMIBGroups": ciscoVismModuleMIBGroups,
       "ciscoVismPerfStatsGroup": ciscoVismPerfStatsGroup,
       "ciscoVismCallStatsGroup": ciscoVismCallStatsGroup,
       "ciscoVismIpGroup": ciscoVismIpGroup,
       "ciscoVismVoIpGroup": ciscoVismVoIpGroup,
       "ciscoVismDspGroup": ciscoVismDspGroup,
       "ciscoVismSystemGroup": ciscoVismSystemGroup,
       "ciscoVismInteropGroup": ciscoVismInteropGroup,
       "ciscoVismTrapObjGroup": ciscoVismTrapObjGroup,
       "ciscoVismAal2Group": ciscoVismAal2Group,
       "ciscoVismDspDeprecatedGroup": ciscoVismDspDeprecatedGroup,
       "ciscoVismSystemDeprecatedGroup": ciscoVismSystemDeprecatedGroup,
       "ciscoVismVoIpDeprecateGroup": ciscoVismVoIpDeprecateGroup,
       "ciscoVismSystemGroup1": ciscoVismSystemGroup1,
       "ciscoVismSystemFeatureGroup": ciscoVismSystemFeatureGroup,
       "ciscoVismTrapVarbindGroup": ciscoVismTrapVarbindGroup,
       "ciscoVismSystemFeatureGroupRev1": ciscoVismSystemFeatureGroupRev1,
       "ciscoVismSystemGroupSup1": ciscoVismSystemGroupSup1,
       "ciscoVismDspGroupSup1": ciscoVismDspGroupSup1,
       "ciscoVismModuleMIBCompliances": ciscoVismModuleMIBCompliances,
       "ciscoVismModuleCompliance": ciscoVismModuleCompliance,
       "ciscoVismModuleCompliance1": ciscoVismModuleCompliance1,
       "ciscoVismModuleComplianceRev2": ciscoVismModuleComplianceRev2,
       "ciscoVismModuleComplianceRev3": ciscoVismModuleComplianceRev3,
       "ciscoVismModuleComplianceRev4": ciscoVismModuleComplianceRev4}
)
