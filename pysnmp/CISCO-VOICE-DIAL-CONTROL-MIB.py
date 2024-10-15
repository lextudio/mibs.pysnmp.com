# SNMP MIB module (CISCO-VOICE-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:23 2024
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

(cCallHistoryCallOrigin,
 cCallHistoryIndex) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryCallOrigin",
    "cCallHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcCallReferenceIdOrZero,
 CvcCoderTypeRate,
 CvcFaxTransmitRate,
 CvcGUid,
 CvcInBandSignaling,
 CvcSpeechCoderRate,
 cvCommonDcCallHistoryCoderTypeRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCallReferenceIdOrZero",
    "CvcCoderTypeRate",
    "CvcFaxTransmitRate",
    "CvcGUid",
    "CvcInBandSignaling",
    "CvcSpeechCoderRate",
    "cvCommonDcCallHistoryCoderTypeRate")

(DnisMapname,) = mibBuilder.importSymbols(
    "CISCO-VOICE-DNIS-MIB",
    "DnisMapname")

(AbsoluteCounter32,
 callActiveIndex,
 callActivePeerAddress,
 callActivePeerId,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32",
    "callActiveIndex",
    "callActivePeerAddress",
    "callActivePeerId",
    "callActiveSetupTime")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(QosService,) = mibBuilder.importSymbols(
    "INT-SERV-MIB",
    "QosService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVoiceDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63)
)
ciscoVoiceDialControlMIB.setRevisions(
        ("2012-05-15 00:00",
         "2011-07-11 00:00",
         "2011-05-31 00:00",
         "2010-07-26 00:00",
         "2009-05-07 00:00",
         "2009-04-20 00:00",
         "2009-01-12 00:00",
         "2006-03-12 00:00",
         "2005-09-29 00:00",
         "2005-07-25 00:00",
         "2005-03-02 00:00",
         "2005-03-01 00:00",
         "2004-04-30 00:00",
         "2004-04-16 00:00",
         "2004-03-09 00:00",
         "2004-01-20 00:00",
         "2003-06-26 00:00",
         "2003-04-14 00:00",
         "2002-12-31 00:00",
         "2002-12-02 00:00",
         "2002-10-31 00:00",
         "2002-07-12 00:00",
         "2001-08-20 00:00",
         "2001-07-02 00:00",
         "2001-04-10 00:00",
         "2001-03-25 00:00",
         "2000-05-04 00:00",
         "2000-04-19 00:00",
         "2000-03-13 00:00",
         "1999-06-28 00:00",
         "1999-01-29 00:00",
         "1998-09-11 00:00",
         "1998-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvCallVolumeWMIntvlType(Integer32, TextualConvention):
    status = "current"
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
        *(("fromReloadStats", 4),
          ("hourStats", 3),
          ("minuteStats", 2),
          ("secondStats", 1))
    )



class CvCallVolumeStatsIntvlType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hourStats", 3),
          ("minuteStats", 2),
          ("secondStats", 1))
    )



class CvSessionProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("cisco", 2),
          ("multicast", 5),
          ("other", 1),
          ("sccp", 6),
          ("sdp", 3),
          ("sip", 4))
    )



class CvCasGroup(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 30),
    )



class CvAmrNbBitRateMode(Bits, TextualConvention):
    status = "current"


class CvAmrNbRtpEncap(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rfc3267", 1)
    )



class CvIlbcFrameMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("frameMode20", 20),
          ("frameMode30", 30))
    )



class CvCallConnectionType(Integer32, TextualConvention):
    status = "current"
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
        *(("cacontrol", 6),
          ("h323", 1),
          ("mgcp", 3),
          ("multicast", 5),
          ("sccp", 4),
          ("sip", 2),
          ("telephony", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CvdcMIBObjects_ObjectIdentity = ObjectIdentity
cvdcMIBObjects = _CvdcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1)
)
_CvGeneralConfiguration_ObjectIdentity = ObjectIdentity
cvGeneralConfiguration = _CvGeneralConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 1)
)


class _CvGeneralPoorQoVNotificationEnable_Type(TruthValue):
    """Custom type cvGeneralPoorQoVNotificationEnable based on TruthValue"""


_CvGeneralPoorQoVNotificationEnable_Object = MibScalar
cvGeneralPoorQoVNotificationEnable = _CvGeneralPoorQoVNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 1, 1),
    _CvGeneralPoorQoVNotificationEnable_Type()
)
cvGeneralPoorQoVNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvGeneralPoorQoVNotificationEnable.setStatus("current")


class _CvGeneralFallbackNotificationEnable_Type(TruthValue):
    """Custom type cvGeneralFallbackNotificationEnable based on TruthValue"""


_CvGeneralFallbackNotificationEnable_Object = MibScalar
cvGeneralFallbackNotificationEnable = _CvGeneralFallbackNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 1, 2),
    _CvGeneralFallbackNotificationEnable_Type()
)
cvGeneralFallbackNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvGeneralFallbackNotificationEnable.setStatus("current")


class _CvGeneralDSCPPolicyNotificationEnable_Type(TruthValue):
    """Custom type cvGeneralDSCPPolicyNotificationEnable based on TruthValue"""


_CvGeneralDSCPPolicyNotificationEnable_Object = MibScalar
cvGeneralDSCPPolicyNotificationEnable = _CvGeneralDSCPPolicyNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 1, 3),
    _CvGeneralDSCPPolicyNotificationEnable_Type()
)
cvGeneralDSCPPolicyNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvGeneralDSCPPolicyNotificationEnable.setStatus("current")


class _CvGeneralMediaPolicyNotificationEnable_Type(TruthValue):
    """Custom type cvGeneralMediaPolicyNotificationEnable based on TruthValue"""


_CvGeneralMediaPolicyNotificationEnable_Object = MibScalar
cvGeneralMediaPolicyNotificationEnable = _CvGeneralMediaPolicyNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 1, 4),
    _CvGeneralMediaPolicyNotificationEnable_Type()
)
cvGeneralMediaPolicyNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvGeneralMediaPolicyNotificationEnable.setStatus("current")
_CvPeer_ObjectIdentity = ObjectIdentity
cvPeer = _CvPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2)
)
_CvPeerCfgTable_Object = MibTable
cvPeerCfgTable = _CvPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvPeerCfgTable.setStatus("current")
_CvPeerCfgEntry_Object = MibTableRow
cvPeerCfgEntry = _CvPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1)
)
cvPeerCfgEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIndex"),
)
if mibBuilder.loadTexts:
    cvPeerCfgEntry.setStatus("current")


class _CvPeerCfgIndex_Type(Integer32):
    """Custom type cvPeerCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvPeerCfgIndex_Type.__name__ = "Integer32"
_CvPeerCfgIndex_Object = MibTableColumn
cvPeerCfgIndex = _CvPeerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1, 1),
    _CvPeerCfgIndex_Type()
)
cvPeerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvPeerCfgIndex.setStatus("current")
_CvPeerCfgIfIndex_Type = InterfaceIndexOrZero
_CvPeerCfgIfIndex_Object = MibTableColumn
cvPeerCfgIfIndex = _CvPeerCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1, 2),
    _CvPeerCfgIfIndex_Type()
)
cvPeerCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvPeerCfgIfIndex.setStatus("current")


class _CvPeerCfgType_Type(Integer32):
    """Custom type cvPeerCfgType based on Integer32"""
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
        *(("mmail", 3),
          ("voatm", 4),
          ("vofr", 5),
          ("voice", 1),
          ("voip", 2))
    )


_CvPeerCfgType_Type.__name__ = "Integer32"
_CvPeerCfgType_Object = MibTableColumn
cvPeerCfgType = _CvPeerCfgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1, 3),
    _CvPeerCfgType_Type()
)
cvPeerCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvPeerCfgType.setStatus("current")
_CvPeerCfgRowStatus_Type = RowStatus
_CvPeerCfgRowStatus_Object = MibTableColumn
cvPeerCfgRowStatus = _CvPeerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1, 4),
    _CvPeerCfgRowStatus_Type()
)
cvPeerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvPeerCfgRowStatus.setStatus("current")


class _CvPeerCfgPeerType_Type(Integer32):
    """Custom type cvPeerCfgPeerType based on Integer32"""
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


_CvPeerCfgPeerType_Type.__name__ = "Integer32"
_CvPeerCfgPeerType_Object = MibTableColumn
cvPeerCfgPeerType = _CvPeerCfgPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 1, 1, 5),
    _CvPeerCfgPeerType_Type()
)
cvPeerCfgPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvPeerCfgPeerType.setStatus("current")
_CvVoicePeerCfgTable_Object = MibTable
cvVoicePeerCfgTable = _CvVoicePeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvVoicePeerCfgTable.setStatus("current")
_CvVoicePeerCfgEntry_Object = MibTableRow
cvVoicePeerCfgEntry = _CvVoicePeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1)
)
cvVoicePeerCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvVoicePeerCfgEntry.setStatus("current")


class _CvVoicePeerCfgSessionTarget_Type(DisplayString):
    """Custom type cvVoicePeerCfgSessionTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvVoicePeerCfgSessionTarget_Type.__name__ = "DisplayString"
_CvVoicePeerCfgSessionTarget_Object = MibTableColumn
cvVoicePeerCfgSessionTarget = _CvVoicePeerCfgSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 1),
    _CvVoicePeerCfgSessionTarget_Type()
)
cvVoicePeerCfgSessionTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgSessionTarget.setStatus("current")


class _CvVoicePeerCfgDialDigitsPrefix_Type(DisplayString):
    """Custom type cvVoicePeerCfgDialDigitsPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvVoicePeerCfgDialDigitsPrefix_Type.__name__ = "DisplayString"
_CvVoicePeerCfgDialDigitsPrefix_Object = MibTableColumn
cvVoicePeerCfgDialDigitsPrefix = _CvVoicePeerCfgDialDigitsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 2),
    _CvVoicePeerCfgDialDigitsPrefix_Type()
)
cvVoicePeerCfgDialDigitsPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgDialDigitsPrefix.setStatus("current")


class _CvVoicePeerCfgDIDCallEnable_Type(TruthValue):
    """Custom type cvVoicePeerCfgDIDCallEnable based on TruthValue"""


_CvVoicePeerCfgDIDCallEnable_Object = MibTableColumn
cvVoicePeerCfgDIDCallEnable = _CvVoicePeerCfgDIDCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 3),
    _CvVoicePeerCfgDIDCallEnable_Type()
)
cvVoicePeerCfgDIDCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgDIDCallEnable.setStatus("current")


class _CvVoicePeerCfgCasGroup_Type(CvCasGroup):
    """Custom type cvVoicePeerCfgCasGroup based on CvCasGroup"""
    defaultValue = -1


_CvVoicePeerCfgCasGroup_Object = MibTableColumn
cvVoicePeerCfgCasGroup = _CvVoicePeerCfgCasGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 4),
    _CvVoicePeerCfgCasGroup_Type()
)
cvVoicePeerCfgCasGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgCasGroup.setStatus("current")


class _CvVoicePeerCfgRegisterE164_Type(TruthValue):
    """Custom type cvVoicePeerCfgRegisterE164 based on TruthValue"""


_CvVoicePeerCfgRegisterE164_Object = MibTableColumn
cvVoicePeerCfgRegisterE164 = _CvVoicePeerCfgRegisterE164_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 5),
    _CvVoicePeerCfgRegisterE164_Type()
)
cvVoicePeerCfgRegisterE164.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgRegisterE164.setStatus("current")


class _CvVoicePeerCfgForwardDigits_Type(Integer32):
    """Custom type cvVoicePeerCfgForwardDigits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 32),
    )


_CvVoicePeerCfgForwardDigits_Type.__name__ = "Integer32"
_CvVoicePeerCfgForwardDigits_Object = MibTableColumn
cvVoicePeerCfgForwardDigits = _CvVoicePeerCfgForwardDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 6),
    _CvVoicePeerCfgForwardDigits_Type()
)
cvVoicePeerCfgForwardDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgForwardDigits.setStatus("current")


class _CvVoicePeerCfgEchoCancellerTest_Type(Integer32):
    """Custom type cvVoicePeerCfgEchoCancellerTest based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("echoCancellerG168Test2A", 2),
          ("echoCancellerG168Test2B", 3),
          ("echoCancellerG168Test2Ca", 4),
          ("echoCancellerG168Test2Cb", 5),
          ("echoCancellerG168Test3A", 6),
          ("echoCancellerG168Test3B", 7),
          ("echoCancellerG168Test3C", 8),
          ("echoCancellerG168Test4", 9),
          ("echoCancellerG168Test5", 12),
          ("echoCancellerG168Test6", 10),
          ("echoCancellerG168Test7", 13),
          ("echoCancellerG168Test9", 11),
          ("echoCancellerTestNone", 1))
    )


_CvVoicePeerCfgEchoCancellerTest_Type.__name__ = "Integer32"
_CvVoicePeerCfgEchoCancellerTest_Object = MibTableColumn
cvVoicePeerCfgEchoCancellerTest = _CvVoicePeerCfgEchoCancellerTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 2, 1, 7),
    _CvVoicePeerCfgEchoCancellerTest_Type()
)
cvVoicePeerCfgEchoCancellerTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoicePeerCfgEchoCancellerTest.setStatus("current")
_CvVoIPPeerCfgTable_Object = MibTable
cvVoIPPeerCfgTable = _CvVoIPPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cvVoIPPeerCfgTable.setStatus("current")
_CvVoIPPeerCfgEntry_Object = MibTableRow
cvVoIPPeerCfgEntry = _CvVoIPPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1)
)
cvVoIPPeerCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvVoIPPeerCfgEntry.setStatus("current")


class _CvVoIPPeerCfgSessionProtocol_Type(CvSessionProtocol):
    """Custom type cvVoIPPeerCfgSessionProtocol based on CvSessionProtocol"""


_CvVoIPPeerCfgSessionProtocol_Object = MibTableColumn
cvVoIPPeerCfgSessionProtocol = _CvVoIPPeerCfgSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 1),
    _CvVoIPPeerCfgSessionProtocol_Type()
)
cvVoIPPeerCfgSessionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgSessionProtocol.setStatus("current")


class _CvVoIPPeerCfgDesiredQoS_Type(QosService):
    """Custom type cvVoIPPeerCfgDesiredQoS based on QosService"""


_CvVoIPPeerCfgDesiredQoS_Object = MibTableColumn
cvVoIPPeerCfgDesiredQoS = _CvVoIPPeerCfgDesiredQoS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 2),
    _CvVoIPPeerCfgDesiredQoS_Type()
)
cvVoIPPeerCfgDesiredQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgDesiredQoS.setStatus("current")


class _CvVoIPPeerCfgMinAcceptableQoS_Type(QosService):
    """Custom type cvVoIPPeerCfgMinAcceptableQoS based on QosService"""


_CvVoIPPeerCfgMinAcceptableQoS_Object = MibTableColumn
cvVoIPPeerCfgMinAcceptableQoS = _CvVoIPPeerCfgMinAcceptableQoS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 3),
    _CvVoIPPeerCfgMinAcceptableQoS_Type()
)
cvVoIPPeerCfgMinAcceptableQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgMinAcceptableQoS.setStatus("current")
_CvVoIPPeerCfgSessionTarget_Type = DisplayString
_CvVoIPPeerCfgSessionTarget_Object = MibTableColumn
cvVoIPPeerCfgSessionTarget = _CvVoIPPeerCfgSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 4),
    _CvVoIPPeerCfgSessionTarget_Type()
)
cvVoIPPeerCfgSessionTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgSessionTarget.setStatus("current")


class _CvVoIPPeerCfgCoderRate_Type(CvcSpeechCoderRate):
    """Custom type cvVoIPPeerCfgCoderRate based on CvcSpeechCoderRate"""


_CvVoIPPeerCfgCoderRate_Object = MibTableColumn
cvVoIPPeerCfgCoderRate = _CvVoIPPeerCfgCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 5),
    _CvVoIPPeerCfgCoderRate_Type()
)
cvVoIPPeerCfgCoderRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCoderRate.setStatus("current")


class _CvVoIPPeerCfgFaxRate_Type(CvcFaxTransmitRate):
    """Custom type cvVoIPPeerCfgFaxRate based on CvcFaxTransmitRate"""


_CvVoIPPeerCfgFaxRate_Object = MibTableColumn
cvVoIPPeerCfgFaxRate = _CvVoIPPeerCfgFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 6),
    _CvVoIPPeerCfgFaxRate_Type()
)
cvVoIPPeerCfgFaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgFaxRate.setStatus("current")


class _CvVoIPPeerCfgVADEnable_Type(TruthValue):
    """Custom type cvVoIPPeerCfgVADEnable based on TruthValue"""


_CvVoIPPeerCfgVADEnable_Object = MibTableColumn
cvVoIPPeerCfgVADEnable = _CvVoIPPeerCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 7),
    _CvVoIPPeerCfgVADEnable_Type()
)
cvVoIPPeerCfgVADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgVADEnable.setStatus("current")


class _CvVoIPPeerCfgExpectFactor_Type(Integer32):
    """Custom type cvVoIPPeerCfgExpectFactor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CvVoIPPeerCfgExpectFactor_Type.__name__ = "Integer32"
_CvVoIPPeerCfgExpectFactor_Object = MibTableColumn
cvVoIPPeerCfgExpectFactor = _CvVoIPPeerCfgExpectFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 8),
    _CvVoIPPeerCfgExpectFactor_Type()
)
cvVoIPPeerCfgExpectFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgExpectFactor.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgExpectFactor.setUnits("equipment impairment factor (eif)")


class _CvVoIPPeerCfgIcpif_Type(Integer32):
    """Custom type cvVoIPPeerCfgIcpif based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 55),
    )


_CvVoIPPeerCfgIcpif_Type.__name__ = "Integer32"
_CvVoIPPeerCfgIcpif_Object = MibTableColumn
cvVoIPPeerCfgIcpif = _CvVoIPPeerCfgIcpif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 9),
    _CvVoIPPeerCfgIcpif_Type()
)
cvVoIPPeerCfgIcpif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgIcpif.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgIcpif.setUnits("equipment impairment factor (eif)")


class _CvVoIPPeerCfgPoorQoVNotificationEnable_Type(TruthValue):
    """Custom type cvVoIPPeerCfgPoorQoVNotificationEnable based on TruthValue"""


_CvVoIPPeerCfgPoorQoVNotificationEnable_Object = MibTableColumn
cvVoIPPeerCfgPoorQoVNotificationEnable = _CvVoIPPeerCfgPoorQoVNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 10),
    _CvVoIPPeerCfgPoorQoVNotificationEnable_Type()
)
cvVoIPPeerCfgPoorQoVNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgPoorQoVNotificationEnable.setStatus("current")


class _CvVoIPPeerCfgUDPChecksumEnable_Type(TruthValue):
    """Custom type cvVoIPPeerCfgUDPChecksumEnable based on TruthValue"""


_CvVoIPPeerCfgUDPChecksumEnable_Object = MibTableColumn
cvVoIPPeerCfgUDPChecksumEnable = _CvVoIPPeerCfgUDPChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 11),
    _CvVoIPPeerCfgUDPChecksumEnable_Type()
)
cvVoIPPeerCfgUDPChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgUDPChecksumEnable.setStatus("current")


class _CvVoIPPeerCfgIPPrecedence_Type(Integer32):
    """Custom type cvVoIPPeerCfgIPPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CvVoIPPeerCfgIPPrecedence_Type.__name__ = "Integer32"
_CvVoIPPeerCfgIPPrecedence_Object = MibTableColumn
cvVoIPPeerCfgIPPrecedence = _CvVoIPPeerCfgIPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 12),
    _CvVoIPPeerCfgIPPrecedence_Type()
)
cvVoIPPeerCfgIPPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgIPPrecedence.setStatus("current")


class _CvVoIPPeerCfgTechPrefix_Type(DisplayString):
    """Custom type cvVoIPPeerCfgTechPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvVoIPPeerCfgTechPrefix_Type.__name__ = "DisplayString"
_CvVoIPPeerCfgTechPrefix_Object = MibTableColumn
cvVoIPPeerCfgTechPrefix = _CvVoIPPeerCfgTechPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 13),
    _CvVoIPPeerCfgTechPrefix_Type()
)
cvVoIPPeerCfgTechPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgTechPrefix.setStatus("current")


class _CvVoIPPeerCfgDigitRelay_Type(Bits):
    """Custom type cvVoIPPeerCfgDigitRelay based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("h245Alphanumeric", 2),
          ("h245Signal", 1),
          ("rtpCisco", 0),
          ("rtpNte", 3),
          ("sipKpml", 5),
          ("sipNotify", 4))
    )

_CvVoIPPeerCfgDigitRelay_Type.__name__ = "Bits"
_CvVoIPPeerCfgDigitRelay_Object = MibTableColumn
cvVoIPPeerCfgDigitRelay = _CvVoIPPeerCfgDigitRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 14),
    _CvVoIPPeerCfgDigitRelay_Type()
)
cvVoIPPeerCfgDigitRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgDigitRelay.setStatus("current")


class _CvVoIPPeerCfgCoderBytes_Type(Integer32):
    """Custom type cvVoIPPeerCfgCoderBytes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 240),
    )


_CvVoIPPeerCfgCoderBytes_Type.__name__ = "Integer32"
_CvVoIPPeerCfgCoderBytes_Object = MibTableColumn
cvVoIPPeerCfgCoderBytes = _CvVoIPPeerCfgCoderBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 15),
    _CvVoIPPeerCfgCoderBytes_Type()
)
cvVoIPPeerCfgCoderBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCoderBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCoderBytes.setUnits("bytes")


class _CvVoIPPeerCfgFaxBytes_Type(Integer32):
    """Custom type cvVoIPPeerCfgFaxBytes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 255),
    )


_CvVoIPPeerCfgFaxBytes_Type.__name__ = "Integer32"
_CvVoIPPeerCfgFaxBytes_Object = MibTableColumn
cvVoIPPeerCfgFaxBytes = _CvVoIPPeerCfgFaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 16),
    _CvVoIPPeerCfgFaxBytes_Type()
)
cvVoIPPeerCfgFaxBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgFaxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgFaxBytes.setUnits("bytes")


class _CvVoIPPeerCfgInBandSignaling_Type(CvcInBandSignaling):
    """Custom type cvVoIPPeerCfgInBandSignaling based on CvcInBandSignaling"""


_CvVoIPPeerCfgInBandSignaling_Object = MibTableColumn
cvVoIPPeerCfgInBandSignaling = _CvVoIPPeerCfgInBandSignaling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 17),
    _CvVoIPPeerCfgInBandSignaling_Type()
)
cvVoIPPeerCfgInBandSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgInBandSignaling.setStatus("current")


class _CvVoIPPeerCfgMediaSetting_Type(Integer32):
    """Custom type cvVoIPPeerCfgMediaSetting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowAround", 2),
          ("flowThrough", 1))
    )


_CvVoIPPeerCfgMediaSetting_Type.__name__ = "Integer32"
_CvVoIPPeerCfgMediaSetting_Object = MibTableColumn
cvVoIPPeerCfgMediaSetting = _CvVoIPPeerCfgMediaSetting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 23),
    _CvVoIPPeerCfgMediaSetting_Type()
)
cvVoIPPeerCfgMediaSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgMediaSetting.setStatus("current")


class _CvVoIPPeerCfgDesiredQoSVideo_Type(QosService):
    """Custom type cvVoIPPeerCfgDesiredQoSVideo based on QosService"""


_CvVoIPPeerCfgDesiredQoSVideo_Object = MibTableColumn
cvVoIPPeerCfgDesiredQoSVideo = _CvVoIPPeerCfgDesiredQoSVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 24),
    _CvVoIPPeerCfgDesiredQoSVideo_Type()
)
cvVoIPPeerCfgDesiredQoSVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgDesiredQoSVideo.setStatus("current")


class _CvVoIPPeerCfgMinAcceptableQoSVideo_Type(QosService):
    """Custom type cvVoIPPeerCfgMinAcceptableQoSVideo based on QosService"""


_CvVoIPPeerCfgMinAcceptableQoSVideo_Object = MibTableColumn
cvVoIPPeerCfgMinAcceptableQoSVideo = _CvVoIPPeerCfgMinAcceptableQoSVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 25),
    _CvVoIPPeerCfgMinAcceptableQoSVideo_Type()
)
cvVoIPPeerCfgMinAcceptableQoSVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgMinAcceptableQoSVideo.setStatus("current")


class _CvVoIPPeerCfgRedirectip2ip_Type(TruthValue):
    """Custom type cvVoIPPeerCfgRedirectip2ip based on TruthValue"""


_CvVoIPPeerCfgRedirectip2ip_Object = MibTableColumn
cvVoIPPeerCfgRedirectip2ip = _CvVoIPPeerCfgRedirectip2ip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 26),
    _CvVoIPPeerCfgRedirectip2ip_Type()
)
cvVoIPPeerCfgRedirectip2ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgRedirectip2ip.setStatus("current")


class _CvVoIPPeerCfgOctetAligned_Type(TruthValue):
    """Custom type cvVoIPPeerCfgOctetAligned based on TruthValue"""


_CvVoIPPeerCfgOctetAligned_Object = MibTableColumn
cvVoIPPeerCfgOctetAligned = _CvVoIPPeerCfgOctetAligned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 27),
    _CvVoIPPeerCfgOctetAligned_Type()
)
cvVoIPPeerCfgOctetAligned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgOctetAligned.setStatus("current")


class _CvVoIPPeerCfgBitRates_Type(CvAmrNbBitRateMode):
    """Custom type cvVoIPPeerCfgBitRates based on CvAmrNbBitRateMode"""
    defaultBinValue = "0"


_CvVoIPPeerCfgBitRates_Object = MibTableColumn
cvVoIPPeerCfgBitRates = _CvVoIPPeerCfgBitRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 28),
    _CvVoIPPeerCfgBitRates_Type()
)
cvVoIPPeerCfgBitRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgBitRates.setStatus("current")


class _CvVoIPPeerCfgCRC_Type(TruthValue):
    """Custom type cvVoIPPeerCfgCRC based on TruthValue"""


_CvVoIPPeerCfgCRC_Object = MibTableColumn
cvVoIPPeerCfgCRC = _CvVoIPPeerCfgCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 29),
    _CvVoIPPeerCfgCRC_Type()
)
cvVoIPPeerCfgCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCRC.setStatus("current")


class _CvVoIPPeerCfgCoderMode_Type(CvIlbcFrameMode):
    """Custom type cvVoIPPeerCfgCoderMode based on CvIlbcFrameMode"""


_CvVoIPPeerCfgCoderMode_Object = MibTableColumn
cvVoIPPeerCfgCoderMode = _CvVoIPPeerCfgCoderMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 30),
    _CvVoIPPeerCfgCoderMode_Type()
)
cvVoIPPeerCfgCoderMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCoderMode.setStatus("current")


class _CvVoIPPeerCfgCodingMode_Type(Integer32):
    """Custom type cvVoIPPeerCfgCodingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("independent", 2))
    )


_CvVoIPPeerCfgCodingMode_Type.__name__ = "Integer32"
_CvVoIPPeerCfgCodingMode_Object = MibTableColumn
cvVoIPPeerCfgCodingMode = _CvVoIPPeerCfgCodingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 31),
    _CvVoIPPeerCfgCodingMode_Type()
)
cvVoIPPeerCfgCodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgCodingMode.setStatus("current")


class _CvVoIPPeerCfgBitRate_Type(Unsigned32):
    """Custom type cvVoIPPeerCfgBitRate based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 32000),
    )


_CvVoIPPeerCfgBitRate_Type.__name__ = "Unsigned32"
_CvVoIPPeerCfgBitRate_Object = MibTableColumn
cvVoIPPeerCfgBitRate = _CvVoIPPeerCfgBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 32),
    _CvVoIPPeerCfgBitRate_Type()
)
cvVoIPPeerCfgBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgBitRate.setStatus("current")


class _CvVoIPPeerCfgFrameSize_Type(Integer32):
    """Custom type cvVoIPPeerCfgFrameSize based on Integer32"""
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
        *(("frameSize30", 1),
          ("frameSize30fixed", 3),
          ("frameSize60", 2),
          ("frameSize60fixed", 4))
    )


_CvVoIPPeerCfgFrameSize_Type.__name__ = "Integer32"
_CvVoIPPeerCfgFrameSize_Object = MibTableColumn
cvVoIPPeerCfgFrameSize = _CvVoIPPeerCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 33),
    _CvVoIPPeerCfgFrameSize_Type()
)
cvVoIPPeerCfgFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgFrameSize.setStatus("current")


class _CvVoIPPeerCfgDSCPPolicyNotificationEnable_Type(TruthValue):
    """Custom type cvVoIPPeerCfgDSCPPolicyNotificationEnable based on TruthValue"""


_CvVoIPPeerCfgDSCPPolicyNotificationEnable_Object = MibTableColumn
cvVoIPPeerCfgDSCPPolicyNotificationEnable = _CvVoIPPeerCfgDSCPPolicyNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 34),
    _CvVoIPPeerCfgDSCPPolicyNotificationEnable_Type()
)
cvVoIPPeerCfgDSCPPolicyNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgDSCPPolicyNotificationEnable.setStatus("current")


class _CvVoIPPeerCfgMediaPolicyNotificationEnable_Type(TruthValue):
    """Custom type cvVoIPPeerCfgMediaPolicyNotificationEnable based on TruthValue"""


_CvVoIPPeerCfgMediaPolicyNotificationEnable_Object = MibTableColumn
cvVoIPPeerCfgMediaPolicyNotificationEnable = _CvVoIPPeerCfgMediaPolicyNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 3, 1, 35),
    _CvVoIPPeerCfgMediaPolicyNotificationEnable_Type()
)
cvVoIPPeerCfgMediaPolicyNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvVoIPPeerCfgMediaPolicyNotificationEnable.setStatus("current")
_CvPeerCommonCfgTable_Object = MibTable
cvPeerCommonCfgTable = _CvPeerCommonCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cvPeerCommonCfgTable.setStatus("current")
_CvPeerCommonCfgEntry_Object = MibTableRow
cvPeerCommonCfgEntry = _CvPeerCommonCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1)
)
cvPeerCommonCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvPeerCommonCfgEntry.setStatus("current")


class _CvPeerCommonCfgIncomingDnisDigits_Type(DisplayString):
    """Custom type cvPeerCommonCfgIncomingDnisDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvPeerCommonCfgIncomingDnisDigits_Type.__name__ = "DisplayString"
_CvPeerCommonCfgIncomingDnisDigits_Object = MibTableColumn
cvPeerCommonCfgIncomingDnisDigits = _CvPeerCommonCfgIncomingDnisDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 1),
    _CvPeerCommonCfgIncomingDnisDigits_Type()
)
cvPeerCommonCfgIncomingDnisDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgIncomingDnisDigits.setStatus("current")


class _CvPeerCommonCfgMaxConnections_Type(Integer32):
    """Custom type cvPeerCommonCfgMaxConnections based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_CvPeerCommonCfgMaxConnections_Type.__name__ = "Integer32"
_CvPeerCommonCfgMaxConnections_Object = MibTableColumn
cvPeerCommonCfgMaxConnections = _CvPeerCommonCfgMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 2),
    _CvPeerCommonCfgMaxConnections_Type()
)
cvPeerCommonCfgMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgMaxConnections.setStatus("current")
if mibBuilder.loadTexts:
    cvPeerCommonCfgMaxConnections.setUnits("connections")
_CvPeerCommonCfgApplicationName_Type = DisplayString
_CvPeerCommonCfgApplicationName_Object = MibTableColumn
cvPeerCommonCfgApplicationName = _CvPeerCommonCfgApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 3),
    _CvPeerCommonCfgApplicationName_Type()
)
cvPeerCommonCfgApplicationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgApplicationName.setStatus("current")


class _CvPeerCommonCfgPreference_Type(Integer32):
    """Custom type cvPeerCommonCfgPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CvPeerCommonCfgPreference_Type.__name__ = "Integer32"
_CvPeerCommonCfgPreference_Object = MibTableColumn
cvPeerCommonCfgPreference = _CvPeerCommonCfgPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 4),
    _CvPeerCommonCfgPreference_Type()
)
cvPeerCommonCfgPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgPreference.setStatus("current")


class _CvPeerCommonCfgHuntStop_Type(TruthValue):
    """Custom type cvPeerCommonCfgHuntStop based on TruthValue"""


_CvPeerCommonCfgHuntStop_Object = MibTableColumn
cvPeerCommonCfgHuntStop = _CvPeerCommonCfgHuntStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 5),
    _CvPeerCommonCfgHuntStop_Type()
)
cvPeerCommonCfgHuntStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgHuntStop.setStatus("current")
_CvPeerCommonCfgDnisMappingName_Type = DnisMapname
_CvPeerCommonCfgDnisMappingName_Object = MibTableColumn
cvPeerCommonCfgDnisMappingName = _CvPeerCommonCfgDnisMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 6),
    _CvPeerCommonCfgDnisMappingName_Type()
)
cvPeerCommonCfgDnisMappingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgDnisMappingName.setStatus("current")
_CvPeerCommonCfgSourceCarrierId_Type = SnmpAdminString
_CvPeerCommonCfgSourceCarrierId_Object = MibTableColumn
cvPeerCommonCfgSourceCarrierId = _CvPeerCommonCfgSourceCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 7),
    _CvPeerCommonCfgSourceCarrierId_Type()
)
cvPeerCommonCfgSourceCarrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgSourceCarrierId.setStatus("current")
_CvPeerCommonCfgTargetCarrierId_Type = SnmpAdminString
_CvPeerCommonCfgTargetCarrierId_Object = MibTableColumn
cvPeerCommonCfgTargetCarrierId = _CvPeerCommonCfgTargetCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 8),
    _CvPeerCommonCfgTargetCarrierId_Type()
)
cvPeerCommonCfgTargetCarrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgTargetCarrierId.setStatus("current")
_CvPeerCommonCfgSourceTrunkGrpLabel_Type = SnmpAdminString
_CvPeerCommonCfgSourceTrunkGrpLabel_Object = MibTableColumn
cvPeerCommonCfgSourceTrunkGrpLabel = _CvPeerCommonCfgSourceTrunkGrpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 9),
    _CvPeerCommonCfgSourceTrunkGrpLabel_Type()
)
cvPeerCommonCfgSourceTrunkGrpLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgSourceTrunkGrpLabel.setStatus("current")
_CvPeerCommonCfgTargetTrunkGrpLabel_Type = SnmpAdminString
_CvPeerCommonCfgTargetTrunkGrpLabel_Object = MibTableColumn
cvPeerCommonCfgTargetTrunkGrpLabel = _CvPeerCommonCfgTargetTrunkGrpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 2, 4, 1, 10),
    _CvPeerCommonCfgTargetTrunkGrpLabel_Type()
)
cvPeerCommonCfgTargetTrunkGrpLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvPeerCommonCfgTargetTrunkGrpLabel.setStatus("current")
_CvGatewayCallActive_ObjectIdentity = ObjectIdentity
cvGatewayCallActive = _CvGatewayCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3)
)
_CvCallActiveTable_Object = MibTable
cvCallActiveTable = _CvCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvCallActiveTable.setStatus("current")
_CvCallActiveEntry_Object = MibTableRow
cvCallActiveEntry = _CvCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1)
)
cvCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cvCallActiveEntry.setStatus("current")
_CvCallActiveConnectionId_Type = CvcGUid
_CvCallActiveConnectionId_Object = MibTableColumn
cvCallActiveConnectionId = _CvCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 1),
    _CvCallActiveConnectionId_Type()
)
cvCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveConnectionId.setStatus("current")
_CvCallActiveTxDuration_Type = AbsoluteCounter32
_CvCallActiveTxDuration_Object = MibTableColumn
cvCallActiveTxDuration = _CvCallActiveTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 2),
    _CvCallActiveTxDuration_Type()
)
cvCallActiveTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveTxDuration.setUnits("milliseconds")
_CvCallActiveVoiceTxDuration_Type = AbsoluteCounter32
_CvCallActiveVoiceTxDuration_Object = MibTableColumn
cvCallActiveVoiceTxDuration = _CvCallActiveVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 3),
    _CvCallActiveVoiceTxDuration_Type()
)
cvCallActiveVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveVoiceTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveVoiceTxDuration.setUnits("milliseconds")
_CvCallActiveFaxTxDuration_Type = AbsoluteCounter32
_CvCallActiveFaxTxDuration_Object = MibTableColumn
cvCallActiveFaxTxDuration = _CvCallActiveFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 4),
    _CvCallActiveFaxTxDuration_Type()
)
cvCallActiveFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveFaxTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveFaxTxDuration.setUnits("milliseconds")
_CvCallActiveCoderTypeRate_Type = CvcCoderTypeRate
_CvCallActiveCoderTypeRate_Object = MibTableColumn
cvCallActiveCoderTypeRate = _CvCallActiveCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 5),
    _CvCallActiveCoderTypeRate_Type()
)
cvCallActiveCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveCoderTypeRate.setStatus("current")


class _CvCallActiveNoiseLevel_Type(Integer32):
    """Custom type cvCallActiveNoiseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 8),
    )


_CvCallActiveNoiseLevel_Type.__name__ = "Integer32"
_CvCallActiveNoiseLevel_Object = MibTableColumn
cvCallActiveNoiseLevel = _CvCallActiveNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 6),
    _CvCallActiveNoiseLevel_Type()
)
cvCallActiveNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveNoiseLevel.setUnits("dBm")


class _CvCallActiveACOMLevel_Type(Integer32):
    """Custom type cvCallActiveACOMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CvCallActiveACOMLevel_Type.__name__ = "Integer32"
_CvCallActiveACOMLevel_Object = MibTableColumn
cvCallActiveACOMLevel = _CvCallActiveACOMLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 7),
    _CvCallActiveACOMLevel_Type()
)
cvCallActiveACOMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveACOMLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveACOMLevel.setUnits("dB")


class _CvCallActiveOutSignalLevel_Type(Integer32):
    """Custom type cvCallActiveOutSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 8),
    )


_CvCallActiveOutSignalLevel_Type.__name__ = "Integer32"
_CvCallActiveOutSignalLevel_Object = MibTableColumn
cvCallActiveOutSignalLevel = _CvCallActiveOutSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 8),
    _CvCallActiveOutSignalLevel_Type()
)
cvCallActiveOutSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveOutSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveOutSignalLevel.setUnits("dBm")


class _CvCallActiveInSignalLevel_Type(Integer32):
    """Custom type cvCallActiveInSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 8),
    )


_CvCallActiveInSignalLevel_Type.__name__ = "Integer32"
_CvCallActiveInSignalLevel_Object = MibTableColumn
cvCallActiveInSignalLevel = _CvCallActiveInSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 9),
    _CvCallActiveInSignalLevel_Type()
)
cvCallActiveInSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveInSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveInSignalLevel.setUnits("dBm")


class _CvCallActiveERLLevel_Type(Integer32):
    """Custom type cvCallActiveERLLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 45),
    )


_CvCallActiveERLLevel_Type.__name__ = "Integer32"
_CvCallActiveERLLevel_Object = MibTableColumn
cvCallActiveERLLevel = _CvCallActiveERLLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 10),
    _CvCallActiveERLLevel_Type()
)
cvCallActiveERLLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveERLLevel.setStatus("deprecated")
if mibBuilder.loadTexts:
    cvCallActiveERLLevel.setUnits("dB")


class _CvCallActiveSessionTarget_Type(DisplayString):
    """Custom type cvCallActiveSessionTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvCallActiveSessionTarget_Type.__name__ = "DisplayString"
_CvCallActiveSessionTarget_Object = MibTableColumn
cvCallActiveSessionTarget = _CvCallActiveSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 11),
    _CvCallActiveSessionTarget_Type()
)
cvCallActiveSessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveSessionTarget.setStatus("current")
_CvCallActiveImgPageCount_Type = AbsoluteCounter32
_CvCallActiveImgPageCount_Object = MibTableColumn
cvCallActiveImgPageCount = _CvCallActiveImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 12),
    _CvCallActiveImgPageCount_Type()
)
cvCallActiveImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveImgPageCount.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveImgPageCount.setUnits("pages")
_CvCallActiveCallingName_Type = SnmpAdminString
_CvCallActiveCallingName_Object = MibTableColumn
cvCallActiveCallingName = _CvCallActiveCallingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 13),
    _CvCallActiveCallingName_Type()
)
cvCallActiveCallingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveCallingName.setStatus("current")
_CvCallActiveCallerIDBlock_Type = TruthValue
_CvCallActiveCallerIDBlock_Object = MibTableColumn
cvCallActiveCallerIDBlock = _CvCallActiveCallerIDBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 14),
    _CvCallActiveCallerIDBlock_Type()
)
cvCallActiveCallerIDBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveCallerIDBlock.setStatus("current")


class _CvCallActiveEcanReflectorLocation_Type(Integer32):
    """Custom type cvCallActiveEcanReflectorLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CvCallActiveEcanReflectorLocation_Type.__name__ = "Integer32"
_CvCallActiveEcanReflectorLocation_Object = MibTableColumn
cvCallActiveEcanReflectorLocation = _CvCallActiveEcanReflectorLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 15),
    _CvCallActiveEcanReflectorLocation_Type()
)
cvCallActiveEcanReflectorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveEcanReflectorLocation.setStatus("current")


class _CvCallActiveAccountCode_Type(SnmpAdminString):
    """Custom type cvCallActiveAccountCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CvCallActiveAccountCode_Type.__name__ = "SnmpAdminString"
_CvCallActiveAccountCode_Object = MibTableColumn
cvCallActiveAccountCode = _CvCallActiveAccountCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 16),
    _CvCallActiveAccountCode_Type()
)
cvCallActiveAccountCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveAccountCode.setStatus("current")


class _CvCallActiveERLLevelRev1_Type(Integer32):
    """Custom type cvCallActiveERLLevelRev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 200),
    )


_CvCallActiveERLLevelRev1_Type.__name__ = "Integer32"
_CvCallActiveERLLevelRev1_Object = MibTableColumn
cvCallActiveERLLevelRev1 = _CvCallActiveERLLevelRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 17),
    _CvCallActiveERLLevelRev1_Type()
)
cvCallActiveERLLevelRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveERLLevelRev1.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveERLLevelRev1.setUnits("dB")


class _CvCallActiveCallId_Type(Unsigned32):
    """Custom type cvCallActiveCallId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvCallActiveCallId_Type.__name__ = "Unsigned32"
_CvCallActiveCallId_Object = MibTableColumn
cvCallActiveCallId = _CvCallActiveCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 1, 1, 18),
    _CvCallActiveCallId_Type()
)
cvCallActiveCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveCallId.setStatus("current")
_CvVoIPCallActiveTable_Object = MibTable
cvVoIPCallActiveTable = _CvVoIPCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cvVoIPCallActiveTable.setStatus("current")
_CvVoIPCallActiveEntry_Object = MibTableRow
cvVoIPCallActiveEntry = _CvVoIPCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1)
)
cvVoIPCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cvVoIPCallActiveEntry.setStatus("current")
_CvVoIPCallActiveConnectionId_Type = CvcGUid
_CvVoIPCallActiveConnectionId_Object = MibTableColumn
cvVoIPCallActiveConnectionId = _CvVoIPCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 1),
    _CvVoIPCallActiveConnectionId_Type()
)
cvVoIPCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveConnectionId.setStatus("current")
_CvVoIPCallActiveRemoteIPAddress_Type = IpAddress
_CvVoIPCallActiveRemoteIPAddress_Object = MibTableColumn
cvVoIPCallActiveRemoteIPAddress = _CvVoIPCallActiveRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 2),
    _CvVoIPCallActiveRemoteIPAddress_Type()
)
cvVoIPCallActiveRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemoteIPAddress.setStatus("deprecated")


class _CvVoIPCallActiveRemoteUDPPort_Type(Integer32):
    """Custom type cvVoIPCallActiveRemoteUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallActiveRemoteUDPPort_Type.__name__ = "Integer32"
_CvVoIPCallActiveRemoteUDPPort_Object = MibTableColumn
cvVoIPCallActiveRemoteUDPPort = _CvVoIPCallActiveRemoteUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 3),
    _CvVoIPCallActiveRemoteUDPPort_Type()
)
cvVoIPCallActiveRemoteUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemoteUDPPort.setStatus("deprecated")
_CvVoIPCallActiveRoundTripDelay_Type = Gauge32
_CvVoIPCallActiveRoundTripDelay_Object = MibTableColumn
cvVoIPCallActiveRoundTripDelay = _CvVoIPCallActiveRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 4),
    _CvVoIPCallActiveRoundTripDelay_Type()
)
cvVoIPCallActiveRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRoundTripDelay.setUnits("milliseconds")
_CvVoIPCallActiveSelectedQoS_Type = QosService
_CvVoIPCallActiveSelectedQoS_Object = MibTableColumn
cvVoIPCallActiveSelectedQoS = _CvVoIPCallActiveSelectedQoS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 5),
    _CvVoIPCallActiveSelectedQoS_Type()
)
cvVoIPCallActiveSelectedQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveSelectedQoS.setStatus("current")
_CvVoIPCallActiveSessionProtocol_Type = CvSessionProtocol
_CvVoIPCallActiveSessionProtocol_Object = MibTableColumn
cvVoIPCallActiveSessionProtocol = _CvVoIPCallActiveSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 6),
    _CvVoIPCallActiveSessionProtocol_Type()
)
cvVoIPCallActiveSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveSessionProtocol.setStatus("current")
_CvVoIPCallActiveSessionTarget_Type = DisplayString
_CvVoIPCallActiveSessionTarget_Object = MibTableColumn
cvVoIPCallActiveSessionTarget = _CvVoIPCallActiveSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 7),
    _CvVoIPCallActiveSessionTarget_Type()
)
cvVoIPCallActiveSessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveSessionTarget.setStatus("current")
_CvVoIPCallActiveOnTimeRvPlayout_Type = AbsoluteCounter32
_CvVoIPCallActiveOnTimeRvPlayout_Object = MibTableColumn
cvVoIPCallActiveOnTimeRvPlayout = _CvVoIPCallActiveOnTimeRvPlayout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 8),
    _CvVoIPCallActiveOnTimeRvPlayout_Type()
)
cvVoIPCallActiveOnTimeRvPlayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveOnTimeRvPlayout.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveOnTimeRvPlayout.setUnits("milliseconds")
_CvVoIPCallActiveGapFillWithSilence_Type = AbsoluteCounter32
_CvVoIPCallActiveGapFillWithSilence_Object = MibTableColumn
cvVoIPCallActiveGapFillWithSilence = _CvVoIPCallActiveGapFillWithSilence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 9),
    _CvVoIPCallActiveGapFillWithSilence_Type()
)
cvVoIPCallActiveGapFillWithSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithSilence.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithSilence.setUnits("milliseconds")
_CvVoIPCallActiveGapFillWithPrediction_Type = AbsoluteCounter32
_CvVoIPCallActiveGapFillWithPrediction_Object = MibTableColumn
cvVoIPCallActiveGapFillWithPrediction = _CvVoIPCallActiveGapFillWithPrediction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 10),
    _CvVoIPCallActiveGapFillWithPrediction_Type()
)
cvVoIPCallActiveGapFillWithPrediction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithPrediction.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithPrediction.setUnits("milliseconds")
_CvVoIPCallActiveGapFillWithInterpolation_Type = AbsoluteCounter32
_CvVoIPCallActiveGapFillWithInterpolation_Object = MibTableColumn
cvVoIPCallActiveGapFillWithInterpolation = _CvVoIPCallActiveGapFillWithInterpolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 11),
    _CvVoIPCallActiveGapFillWithInterpolation_Type()
)
cvVoIPCallActiveGapFillWithInterpolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithInterpolation.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithInterpolation.setUnits("milliseconds")
_CvVoIPCallActiveGapFillWithRedundancy_Type = AbsoluteCounter32
_CvVoIPCallActiveGapFillWithRedundancy_Object = MibTableColumn
cvVoIPCallActiveGapFillWithRedundancy = _CvVoIPCallActiveGapFillWithRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 12),
    _CvVoIPCallActiveGapFillWithRedundancy_Type()
)
cvVoIPCallActiveGapFillWithRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithRedundancy.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveGapFillWithRedundancy.setUnits("milliseconds")
_CvVoIPCallActiveHiWaterPlayoutDelay_Type = AbsoluteCounter32
_CvVoIPCallActiveHiWaterPlayoutDelay_Object = MibTableColumn
cvVoIPCallActiveHiWaterPlayoutDelay = _CvVoIPCallActiveHiWaterPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 13),
    _CvVoIPCallActiveHiWaterPlayoutDelay_Type()
)
cvVoIPCallActiveHiWaterPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveHiWaterPlayoutDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveHiWaterPlayoutDelay.setUnits("milliseconds")
_CvVoIPCallActiveLoWaterPlayoutDelay_Type = Gauge32
_CvVoIPCallActiveLoWaterPlayoutDelay_Object = MibTableColumn
cvVoIPCallActiveLoWaterPlayoutDelay = _CvVoIPCallActiveLoWaterPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 14),
    _CvVoIPCallActiveLoWaterPlayoutDelay_Type()
)
cvVoIPCallActiveLoWaterPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLoWaterPlayoutDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLoWaterPlayoutDelay.setUnits("milliseconds")
_CvVoIPCallActiveReceiveDelay_Type = Gauge32
_CvVoIPCallActiveReceiveDelay_Object = MibTableColumn
cvVoIPCallActiveReceiveDelay = _CvVoIPCallActiveReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 15),
    _CvVoIPCallActiveReceiveDelay_Type()
)
cvVoIPCallActiveReceiveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveReceiveDelay.setStatus("current")
_CvVoIPCallActiveVADEnable_Type = TruthValue
_CvVoIPCallActiveVADEnable_Object = MibTableColumn
cvVoIPCallActiveVADEnable = _CvVoIPCallActiveVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 16),
    _CvVoIPCallActiveVADEnable_Type()
)
cvVoIPCallActiveVADEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveVADEnable.setStatus("deprecated")
_CvVoIPCallActiveCoderTypeRate_Type = CvcCoderTypeRate
_CvVoIPCallActiveCoderTypeRate_Object = MibTableColumn
cvVoIPCallActiveCoderTypeRate = _CvVoIPCallActiveCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 17),
    _CvVoIPCallActiveCoderTypeRate_Type()
)
cvVoIPCallActiveCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCoderTypeRate.setStatus("deprecated")
_CvVoIPCallActiveLostPackets_Type = AbsoluteCounter32
_CvVoIPCallActiveLostPackets_Object = MibTableColumn
cvVoIPCallActiveLostPackets = _CvVoIPCallActiveLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 18),
    _CvVoIPCallActiveLostPackets_Type()
)
cvVoIPCallActiveLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLostPackets.setUnits("packets")
_CvVoIPCallActiveEarlyPackets_Type = AbsoluteCounter32
_CvVoIPCallActiveEarlyPackets_Object = MibTableColumn
cvVoIPCallActiveEarlyPackets = _CvVoIPCallActiveEarlyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 19),
    _CvVoIPCallActiveEarlyPackets_Type()
)
cvVoIPCallActiveEarlyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveEarlyPackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveEarlyPackets.setUnits("packets")
_CvVoIPCallActiveLatePackets_Type = AbsoluteCounter32
_CvVoIPCallActiveLatePackets_Object = MibTableColumn
cvVoIPCallActiveLatePackets = _CvVoIPCallActiveLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 20),
    _CvVoIPCallActiveLatePackets_Type()
)
cvVoIPCallActiveLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLatePackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveLatePackets.setUnits("packets")


class _CvVoIPCallActiveUsername_Type(SnmpAdminString):
    """Custom type cvVoIPCallActiveUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CvVoIPCallActiveUsername_Type.__name__ = "SnmpAdminString"
_CvVoIPCallActiveUsername_Object = MibTableColumn
cvVoIPCallActiveUsername = _CvVoIPCallActiveUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 21),
    _CvVoIPCallActiveUsername_Type()
)
cvVoIPCallActiveUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveUsername.setStatus("current")


class _CvVoIPCallActiveProtocolCallId_Type(OctetString):
    """Custom type cvVoIPCallActiveProtocolCallId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvVoIPCallActiveProtocolCallId_Type.__name__ = "OctetString"
_CvVoIPCallActiveProtocolCallId_Object = MibTableColumn
cvVoIPCallActiveProtocolCallId = _CvVoIPCallActiveProtocolCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 22),
    _CvVoIPCallActiveProtocolCallId_Type()
)
cvVoIPCallActiveProtocolCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveProtocolCallId.setStatus("current")
_CvVoIPCallActiveRemSigIPAddrT_Type = InetAddressType
_CvVoIPCallActiveRemSigIPAddrT_Object = MibTableColumn
cvVoIPCallActiveRemSigIPAddrT = _CvVoIPCallActiveRemSigIPAddrT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 23),
    _CvVoIPCallActiveRemSigIPAddrT_Type()
)
cvVoIPCallActiveRemSigIPAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemSigIPAddrT.setStatus("current")
_CvVoIPCallActiveRemSigIPAddr_Type = InetAddress
_CvVoIPCallActiveRemSigIPAddr_Object = MibTableColumn
cvVoIPCallActiveRemSigIPAddr = _CvVoIPCallActiveRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 24),
    _CvVoIPCallActiveRemSigIPAddr_Type()
)
cvVoIPCallActiveRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemSigIPAddr.setStatus("current")


class _CvVoIPCallActiveRemSigPort_Type(Integer32):
    """Custom type cvVoIPCallActiveRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallActiveRemSigPort_Type.__name__ = "Integer32"
_CvVoIPCallActiveRemSigPort_Object = MibTableColumn
cvVoIPCallActiveRemSigPort = _CvVoIPCallActiveRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 25),
    _CvVoIPCallActiveRemSigPort_Type()
)
cvVoIPCallActiveRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemSigPort.setStatus("current")
_CvVoIPCallActiveRemMediaIPAddrT_Type = InetAddressType
_CvVoIPCallActiveRemMediaIPAddrT_Object = MibTableColumn
cvVoIPCallActiveRemMediaIPAddrT = _CvVoIPCallActiveRemMediaIPAddrT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 26),
    _CvVoIPCallActiveRemMediaIPAddrT_Type()
)
cvVoIPCallActiveRemMediaIPAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemMediaIPAddrT.setStatus("current")
_CvVoIPCallActiveRemMediaIPAddr_Type = InetAddress
_CvVoIPCallActiveRemMediaIPAddr_Object = MibTableColumn
cvVoIPCallActiveRemMediaIPAddr = _CvVoIPCallActiveRemMediaIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 27),
    _CvVoIPCallActiveRemMediaIPAddr_Type()
)
cvVoIPCallActiveRemMediaIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemMediaIPAddr.setStatus("current")


class _CvVoIPCallActiveRemMediaPort_Type(Integer32):
    """Custom type cvVoIPCallActiveRemMediaPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallActiveRemMediaPort_Type.__name__ = "Integer32"
_CvVoIPCallActiveRemMediaPort_Object = MibTableColumn
cvVoIPCallActiveRemMediaPort = _CvVoIPCallActiveRemMediaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 28),
    _CvVoIPCallActiveRemMediaPort_Type()
)
cvVoIPCallActiveRemMediaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRemMediaPort.setStatus("current")
_CvVoIPCallActiveSRTPEnable_Type = TruthValue
_CvVoIPCallActiveSRTPEnable_Object = MibTableColumn
cvVoIPCallActiveSRTPEnable = _CvVoIPCallActiveSRTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 29),
    _CvVoIPCallActiveSRTPEnable_Type()
)
cvVoIPCallActiveSRTPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveSRTPEnable.setStatus("current")
_CvVoIPCallActiveOctetAligned_Type = TruthValue
_CvVoIPCallActiveOctetAligned_Object = MibTableColumn
cvVoIPCallActiveOctetAligned = _CvVoIPCallActiveOctetAligned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 30),
    _CvVoIPCallActiveOctetAligned_Type()
)
cvVoIPCallActiveOctetAligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveOctetAligned.setStatus("current")
_CvVoIPCallActiveBitRates_Type = CvAmrNbBitRateMode
_CvVoIPCallActiveBitRates_Object = MibTableColumn
cvVoIPCallActiveBitRates = _CvVoIPCallActiveBitRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 31),
    _CvVoIPCallActiveBitRates_Type()
)
cvVoIPCallActiveBitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveBitRates.setStatus("current")


class _CvVoIPCallActiveModeChgPeriod_Type(Integer32):
    """Custom type cvVoIPCallActiveModeChgPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CvVoIPCallActiveModeChgPeriod_Type.__name__ = "Integer32"
_CvVoIPCallActiveModeChgPeriod_Object = MibTableColumn
cvVoIPCallActiveModeChgPeriod = _CvVoIPCallActiveModeChgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 32),
    _CvVoIPCallActiveModeChgPeriod_Type()
)
cvVoIPCallActiveModeChgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveModeChgPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveModeChgPeriod.setUnits("frame-blocks")
_CvVoIPCallActiveModeChgNeighbor_Type = TruthValue
_CvVoIPCallActiveModeChgNeighbor_Object = MibTableColumn
cvVoIPCallActiveModeChgNeighbor = _CvVoIPCallActiveModeChgNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 33),
    _CvVoIPCallActiveModeChgNeighbor_Type()
)
cvVoIPCallActiveModeChgNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveModeChgNeighbor.setStatus("current")


class _CvVoIPCallActiveMaxPtime_Type(Integer32):
    """Custom type cvVoIPCallActiveMaxPtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CvVoIPCallActiveMaxPtime_Type.__name__ = "Integer32"
_CvVoIPCallActiveMaxPtime_Object = MibTableColumn
cvVoIPCallActiveMaxPtime = _CvVoIPCallActiveMaxPtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 34),
    _CvVoIPCallActiveMaxPtime_Type()
)
cvVoIPCallActiveMaxPtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveMaxPtime.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveMaxPtime.setUnits("milliseconds")
_CvVoIPCallActiveCRC_Type = TruthValue
_CvVoIPCallActiveCRC_Object = MibTableColumn
cvVoIPCallActiveCRC = _CvVoIPCallActiveCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 35),
    _CvVoIPCallActiveCRC_Type()
)
cvVoIPCallActiveCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCRC.setStatus("current")
_CvVoIPCallActiveRobustSorting_Type = TruthValue
_CvVoIPCallActiveRobustSorting_Object = MibTableColumn
cvVoIPCallActiveRobustSorting = _CvVoIPCallActiveRobustSorting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 36),
    _CvVoIPCallActiveRobustSorting_Type()
)
cvVoIPCallActiveRobustSorting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveRobustSorting.setStatus("current")
_CvVoIPCallActiveEncap_Type = CvAmrNbRtpEncap
_CvVoIPCallActiveEncap_Object = MibTableColumn
cvVoIPCallActiveEncap = _CvVoIPCallActiveEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 37),
    _CvVoIPCallActiveEncap_Type()
)
cvVoIPCallActiveEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveEncap.setStatus("current")


class _CvVoIPCallActiveInterleaving_Type(Integer32):
    """Custom type cvVoIPCallActiveInterleaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CvVoIPCallActiveInterleaving_Type.__name__ = "Integer32"
_CvVoIPCallActiveInterleaving_Object = MibTableColumn
cvVoIPCallActiveInterleaving = _CvVoIPCallActiveInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 38),
    _CvVoIPCallActiveInterleaving_Type()
)
cvVoIPCallActiveInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveInterleaving.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveInterleaving.setUnits("frame-blocks")


class _CvVoIPCallActivePtime_Type(Integer32):
    """Custom type cvVoIPCallActivePtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CvVoIPCallActivePtime_Type.__name__ = "Integer32"
_CvVoIPCallActivePtime_Object = MibTableColumn
cvVoIPCallActivePtime = _CvVoIPCallActivePtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 39),
    _CvVoIPCallActivePtime_Type()
)
cvVoIPCallActivePtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActivePtime.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActivePtime.setUnits("milliseconds")


class _CvVoIPCallActiveChannels_Type(Integer32):
    """Custom type cvVoIPCallActiveChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CvVoIPCallActiveChannels_Type.__name__ = "Integer32"
_CvVoIPCallActiveChannels_Object = MibTableColumn
cvVoIPCallActiveChannels = _CvVoIPCallActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 40),
    _CvVoIPCallActiveChannels_Type()
)
cvVoIPCallActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveChannels.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveChannels.setUnits("channels")
_CvVoIPCallActiveCoderMode_Type = CvIlbcFrameMode
_CvVoIPCallActiveCoderMode_Object = MibTableColumn
cvVoIPCallActiveCoderMode = _CvVoIPCallActiveCoderMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 41),
    _CvVoIPCallActiveCoderMode_Type()
)
cvVoIPCallActiveCoderMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCoderMode.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCoderMode.setUnits("milliseconds")


class _CvVoIPCallActiveCallId_Type(Unsigned32):
    """Custom type cvVoIPCallActiveCallId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvVoIPCallActiveCallId_Type.__name__ = "Unsigned32"
_CvVoIPCallActiveCallId_Object = MibTableColumn
cvVoIPCallActiveCallId = _CvVoIPCallActiveCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 42),
    _CvVoIPCallActiveCallId_Type()
)
cvVoIPCallActiveCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCallId.setStatus("current")
_CvVoIPCallActiveCallReferenceId_Type = CvcCallReferenceIdOrZero
_CvVoIPCallActiveCallReferenceId_Object = MibTableColumn
cvVoIPCallActiveCallReferenceId = _CvVoIPCallActiveCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 43),
    _CvVoIPCallActiveCallReferenceId_Type()
)
cvVoIPCallActiveCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveCallReferenceId.setStatus("current")
_CcVoIPCallActivePolicyName_Type = DisplayString
_CcVoIPCallActivePolicyName_Object = MibTableColumn
ccVoIPCallActivePolicyName = _CcVoIPCallActivePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 44),
    _CcVoIPCallActivePolicyName_Type()
)
ccVoIPCallActivePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccVoIPCallActivePolicyName.setStatus("current")
_CvVoIPCallActiveReversedDirectionPeerAddress_Type = DisplayString
_CvVoIPCallActiveReversedDirectionPeerAddress_Object = MibTableColumn
cvVoIPCallActiveReversedDirectionPeerAddress = _CvVoIPCallActiveReversedDirectionPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 45),
    _CvVoIPCallActiveReversedDirectionPeerAddress_Type()
)
cvVoIPCallActiveReversedDirectionPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveReversedDirectionPeerAddress.setStatus("current")
_CvVoIPCallActiveSessionId_Type = Unsigned32
_CvVoIPCallActiveSessionId_Object = MibTableColumn
cvVoIPCallActiveSessionId = _CvVoIPCallActiveSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 2, 1, 46),
    _CvVoIPCallActiveSessionId_Type()
)
cvVoIPCallActiveSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallActiveSessionId.setStatus("current")
_CvCallActiveDS0s_Type = Gauge32
_CvCallActiveDS0s_Object = MibScalar
cvCallActiveDS0s = _CvCallActiveDS0s_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 3),
    _CvCallActiveDS0s_Type()
)
cvCallActiveDS0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallActiveDS0s.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveDS0s.setUnits("interfaces")


class _CvCallActiveDS0sHighThreshold_Type(Unsigned32):
    """Custom type cvCallActiveDS0sHighThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CvCallActiveDS0sHighThreshold_Type.__name__ = "Unsigned32"
_CvCallActiveDS0sHighThreshold_Object = MibScalar
cvCallActiveDS0sHighThreshold = _CvCallActiveDS0sHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 4),
    _CvCallActiveDS0sHighThreshold_Type()
)
cvCallActiveDS0sHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallActiveDS0sHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveDS0sHighThreshold.setUnits("percent")


class _CvCallActiveDS0sLowThreshold_Type(Unsigned32):
    """Custom type cvCallActiveDS0sLowThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CvCallActiveDS0sLowThreshold_Type.__name__ = "Unsigned32"
_CvCallActiveDS0sLowThreshold_Object = MibScalar
cvCallActiveDS0sLowThreshold = _CvCallActiveDS0sLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 5),
    _CvCallActiveDS0sLowThreshold_Type()
)
cvCallActiveDS0sLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallActiveDS0sLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cvCallActiveDS0sLowThreshold.setUnits("percent")


class _CvCallActiveDS0sHighNotifyEnable_Type(TruthValue):
    """Custom type cvCallActiveDS0sHighNotifyEnable based on TruthValue"""


_CvCallActiveDS0sHighNotifyEnable_Object = MibScalar
cvCallActiveDS0sHighNotifyEnable = _CvCallActiveDS0sHighNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 6),
    _CvCallActiveDS0sHighNotifyEnable_Type()
)
cvCallActiveDS0sHighNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallActiveDS0sHighNotifyEnable.setStatus("current")


class _CvCallActiveDS0sLowNotifyEnable_Type(TruthValue):
    """Custom type cvCallActiveDS0sLowNotifyEnable based on TruthValue"""


_CvCallActiveDS0sLowNotifyEnable_Object = MibScalar
cvCallActiveDS0sLowNotifyEnable = _CvCallActiveDS0sLowNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 7),
    _CvCallActiveDS0sLowNotifyEnable_Type()
)
cvCallActiveDS0sLowNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallActiveDS0sLowNotifyEnable.setStatus("current")
_CvCallVolume_ObjectIdentity = ObjectIdentity
cvCallVolume = _CvCallVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8)
)
_CvCallVolConnTable_Object = MibTable
cvCallVolConnTable = _CvCallVolConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    cvCallVolConnTable.setStatus("current")
_CvCallVolConnEntry_Object = MibTableRow
cvCallVolConnEntry = _CvCallVolConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 1, 1)
)
cvCallVolConnEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolConnIndex"),
)
if mibBuilder.loadTexts:
    cvCallVolConnEntry.setStatus("current")
_CvCallVolConnIndex_Type = CvCallConnectionType
_CvCallVolConnIndex_Object = MibTableColumn
cvCallVolConnIndex = _CvCallVolConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 1, 1, 1),
    _CvCallVolConnIndex_Type()
)
cvCallVolConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallVolConnIndex.setStatus("current")


class _CvCallVolConnActiveConnection_Type(Gauge32):
    """Custom type cvCallVolConnActiveConnection based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolConnActiveConnection_Type.__name__ = "Gauge32"
_CvCallVolConnActiveConnection_Object = MibTableColumn
cvCallVolConnActiveConnection = _CvCallVolConnActiveConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 1, 1, 2),
    _CvCallVolConnActiveConnection_Type()
)
cvCallVolConnActiveConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolConnActiveConnection.setStatus("current")


class _CvCallVolConnTotalActiveConnections_Type(Gauge32):
    """Custom type cvCallVolConnTotalActiveConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolConnTotalActiveConnections_Type.__name__ = "Gauge32"
_CvCallVolConnTotalActiveConnections_Object = MibScalar
cvCallVolConnTotalActiveConnections = _CvCallVolConnTotalActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 2),
    _CvCallVolConnTotalActiveConnections_Type()
)
cvCallVolConnTotalActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolConnTotalActiveConnections.setStatus("current")


class _CvCallVolConnMaxCallConnectionLicenese_Type(Unsigned32):
    """Custom type cvCallVolConnMaxCallConnectionLicenese based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolConnMaxCallConnectionLicenese_Type.__name__ = "Unsigned32"
_CvCallVolConnMaxCallConnectionLicenese_Object = MibScalar
cvCallVolConnMaxCallConnectionLicenese = _CvCallVolConnMaxCallConnectionLicenese_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 3),
    _CvCallVolConnMaxCallConnectionLicenese_Type()
)
cvCallVolConnMaxCallConnectionLicenese.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolConnMaxCallConnectionLicenese.setStatus("current")
_CvCallVolPeerTable_Object = MibTable
cvCallVolPeerTable = _CvCallVolPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    cvCallVolPeerTable.setStatus("current")
_CvCallVolPeerEntry_Object = MibTableRow
cvCallVolPeerEntry = _CvCallVolPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 4, 1)
)
if mibBuilder.loadTexts:
    cvCallVolPeerEntry.setStatus("current")


class _CvCallVolPeerIncomingCalls_Type(Gauge32):
    """Custom type cvCallVolPeerIncomingCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolPeerIncomingCalls_Type.__name__ = "Gauge32"
_CvCallVolPeerIncomingCalls_Object = MibTableColumn
cvCallVolPeerIncomingCalls = _CvCallVolPeerIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 4, 1, 1),
    _CvCallVolPeerIncomingCalls_Type()
)
cvCallVolPeerIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolPeerIncomingCalls.setStatus("current")


class _CvCallVolPeerOutgoingCalls_Type(Gauge32):
    """Custom type cvCallVolPeerOutgoingCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolPeerOutgoingCalls_Type.__name__ = "Gauge32"
_CvCallVolPeerOutgoingCalls_Object = MibTableColumn
cvCallVolPeerOutgoingCalls = _CvCallVolPeerOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 4, 1, 2),
    _CvCallVolPeerOutgoingCalls_Type()
)
cvCallVolPeerOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolPeerOutgoingCalls.setStatus("current")
_CvCallVolIfTable_Object = MibTable
cvCallVolIfTable = _CvCallVolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 5)
)
if mibBuilder.loadTexts:
    cvCallVolIfTable.setStatus("current")
_CvCallVolIfEntry_Object = MibTableRow
cvCallVolIfEntry = _CvCallVolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 5, 1)
)
cvCallVolIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvCallVolIfEntry.setStatus("current")


class _CvCallVolMediaIncomingCalls_Type(Gauge32):
    """Custom type cvCallVolMediaIncomingCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolMediaIncomingCalls_Type.__name__ = "Gauge32"
_CvCallVolMediaIncomingCalls_Object = MibTableColumn
cvCallVolMediaIncomingCalls = _CvCallVolMediaIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 5, 1, 1),
    _CvCallVolMediaIncomingCalls_Type()
)
cvCallVolMediaIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolMediaIncomingCalls.setStatus("current")


class _CvCallVolMediaOutgoingCalls_Type(Gauge32):
    """Custom type cvCallVolMediaOutgoingCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallVolMediaOutgoingCalls_Type.__name__ = "Gauge32"
_CvCallVolMediaOutgoingCalls_Object = MibTableColumn
cvCallVolMediaOutgoingCalls = _CvCallVolMediaOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 8, 5, 1, 2),
    _CvCallVolMediaOutgoingCalls_Type()
)
cvCallVolMediaOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallVolMediaOutgoingCalls.setStatus("current")
_CvCallRateMonitor_ObjectIdentity = ObjectIdentity
cvCallRateMonitor = _CvCallRateMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 11)
)


class _CvCallRateMonitorEnable_Type(TruthValue):
    """Custom type cvCallRateMonitorEnable based on TruthValue"""


_CvCallRateMonitorEnable_Object = MibScalar
cvCallRateMonitorEnable = _CvCallRateMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 11, 1),
    _CvCallRateMonitorEnable_Type()
)
cvCallRateMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallRateMonitorEnable.setStatus("current")


class _CvCallRateMonitorTime_Type(Unsigned32):
    """Custom type cvCallRateMonitorTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CvCallRateMonitorTime_Type.__name__ = "Unsigned32"
_CvCallRateMonitorTime_Object = MibScalar
cvCallRateMonitorTime = _CvCallRateMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 11, 2),
    _CvCallRateMonitorTime_Type()
)
cvCallRateMonitorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallRateMonitorTime.setStatus("current")
if mibBuilder.loadTexts:
    cvCallRateMonitorTime.setUnits("five seconds")


class _CvCallRate_Type(Gauge32):
    """Custom type cvCallRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallRate_Type.__name__ = "Gauge32"
_CvCallRate_Object = MibScalar
cvCallRate = _CvCallRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 11, 3),
    _CvCallRate_Type()
)
cvCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRate.setStatus("current")


class _CvCallRateHiWaterMark_Type(Unsigned32):
    """Custom type cvCallRateHiWaterMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvCallRateHiWaterMark_Type.__name__ = "Unsigned32"
_CvCallRateHiWaterMark_Object = MibScalar
cvCallRateHiWaterMark = _CvCallRateHiWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 3, 11, 4),
    _CvCallRateHiWaterMark_Type()
)
cvCallRateHiWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRateHiWaterMark.setStatus("current")
_CvGatewayCallHistory_ObjectIdentity = ObjectIdentity
cvGatewayCallHistory = _CvGatewayCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4)
)
_CvCallHistoryTable_Object = MibTable
cvCallHistoryTable = _CvCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvCallHistoryTable.setStatus("current")
_CvCallHistoryEntry_Object = MibTableRow
cvCallHistoryEntry = _CvCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1)
)
cvCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvCallHistoryEntry.setStatus("current")
_CvCallHistoryConnectionId_Type = CvcGUid
_CvCallHistoryConnectionId_Object = MibTableColumn
cvCallHistoryConnectionId = _CvCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 1),
    _CvCallHistoryConnectionId_Type()
)
cvCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryConnectionId.setStatus("current")
_CvCallHistoryTxDuration_Type = AbsoluteCounter32
_CvCallHistoryTxDuration_Object = MibTableColumn
cvCallHistoryTxDuration = _CvCallHistoryTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 2),
    _CvCallHistoryTxDuration_Type()
)
cvCallHistoryTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryTxDuration.setUnits("milliseconds")
_CvCallHistoryVoiceTxDuration_Type = AbsoluteCounter32
_CvCallHistoryVoiceTxDuration_Object = MibTableColumn
cvCallHistoryVoiceTxDuration = _CvCallHistoryVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 3),
    _CvCallHistoryVoiceTxDuration_Type()
)
cvCallHistoryVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryVoiceTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryVoiceTxDuration.setUnits("milliseconds")
_CvCallHistoryFaxTxDuration_Type = AbsoluteCounter32
_CvCallHistoryFaxTxDuration_Object = MibTableColumn
cvCallHistoryFaxTxDuration = _CvCallHistoryFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 4),
    _CvCallHistoryFaxTxDuration_Type()
)
cvCallHistoryFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryFaxTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryFaxTxDuration.setUnits("milliseconds")
_CvCallHistoryCoderTypeRate_Type = CvcCoderTypeRate
_CvCallHistoryCoderTypeRate_Object = MibTableColumn
cvCallHistoryCoderTypeRate = _CvCallHistoryCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 5),
    _CvCallHistoryCoderTypeRate_Type()
)
cvCallHistoryCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryCoderTypeRate.setStatus("current")


class _CvCallHistoryNoiseLevel_Type(Integer32):
    """Custom type cvCallHistoryNoiseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 8),
    )


_CvCallHistoryNoiseLevel_Type.__name__ = "Integer32"
_CvCallHistoryNoiseLevel_Object = MibTableColumn
cvCallHistoryNoiseLevel = _CvCallHistoryNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 6),
    _CvCallHistoryNoiseLevel_Type()
)
cvCallHistoryNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryNoiseLevel.setUnits("dBm")


class _CvCallHistoryACOMLevel_Type(Integer32):
    """Custom type cvCallHistoryACOMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CvCallHistoryACOMLevel_Type.__name__ = "Integer32"
_CvCallHistoryACOMLevel_Object = MibTableColumn
cvCallHistoryACOMLevel = _CvCallHistoryACOMLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 7),
    _CvCallHistoryACOMLevel_Type()
)
cvCallHistoryACOMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryACOMLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryACOMLevel.setUnits("dB")


class _CvCallHistorySessionTarget_Type(DisplayString):
    """Custom type cvCallHistorySessionTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvCallHistorySessionTarget_Type.__name__ = "DisplayString"
_CvCallHistorySessionTarget_Object = MibTableColumn
cvCallHistorySessionTarget = _CvCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 8),
    _CvCallHistorySessionTarget_Type()
)
cvCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistorySessionTarget.setStatus("current")
_CvCallHistoryImgPageCount_Type = AbsoluteCounter32
_CvCallHistoryImgPageCount_Object = MibTableColumn
cvCallHistoryImgPageCount = _CvCallHistoryImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 9),
    _CvCallHistoryImgPageCount_Type()
)
cvCallHistoryImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryImgPageCount.setStatus("current")
if mibBuilder.loadTexts:
    cvCallHistoryImgPageCount.setUnits("pages")
_CvCallHistoryCallingName_Type = SnmpAdminString
_CvCallHistoryCallingName_Object = MibTableColumn
cvCallHistoryCallingName = _CvCallHistoryCallingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 10),
    _CvCallHistoryCallingName_Type()
)
cvCallHistoryCallingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryCallingName.setStatus("current")
_CvCallHistoryCallerIDBlock_Type = TruthValue
_CvCallHistoryCallerIDBlock_Object = MibTableColumn
cvCallHistoryCallerIDBlock = _CvCallHistoryCallerIDBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 11),
    _CvCallHistoryCallerIDBlock_Type()
)
cvCallHistoryCallerIDBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryCallerIDBlock.setStatus("current")


class _CvCallHistoryAccountCode_Type(SnmpAdminString):
    """Custom type cvCallHistoryAccountCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CvCallHistoryAccountCode_Type.__name__ = "SnmpAdminString"
_CvCallHistoryAccountCode_Object = MibTableColumn
cvCallHistoryAccountCode = _CvCallHistoryAccountCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 12),
    _CvCallHistoryAccountCode_Type()
)
cvCallHistoryAccountCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryAccountCode.setStatus("current")


class _CvCallHistoryCallId_Type(Unsigned32):
    """Custom type cvCallHistoryCallId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvCallHistoryCallId_Type.__name__ = "Unsigned32"
_CvCallHistoryCallId_Object = MibTableColumn
cvCallHistoryCallId = _CvCallHistoryCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 1, 1, 13),
    _CvCallHistoryCallId_Type()
)
cvCallHistoryCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallHistoryCallId.setStatus("current")
_CvVoIPCallHistoryTable_Object = MibTable
cvVoIPCallHistoryTable = _CvVoIPCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cvVoIPCallHistoryTable.setStatus("current")
_CvVoIPCallHistoryEntry_Object = MibTableRow
cvVoIPCallHistoryEntry = _CvVoIPCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1)
)
cvVoIPCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvVoIPCallHistoryEntry.setStatus("current")
_CvVoIPCallHistoryConnectionId_Type = CvcGUid
_CvVoIPCallHistoryConnectionId_Object = MibTableColumn
cvVoIPCallHistoryConnectionId = _CvVoIPCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 1),
    _CvVoIPCallHistoryConnectionId_Type()
)
cvVoIPCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryConnectionId.setStatus("current")
_CvVoIPCallHistoryRemoteIPAddress_Type = IpAddress
_CvVoIPCallHistoryRemoteIPAddress_Object = MibTableColumn
cvVoIPCallHistoryRemoteIPAddress = _CvVoIPCallHistoryRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 2),
    _CvVoIPCallHistoryRemoteIPAddress_Type()
)
cvVoIPCallHistoryRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemoteIPAddress.setStatus("deprecated")


class _CvVoIPCallHistoryRemoteUDPPort_Type(Integer32):
    """Custom type cvVoIPCallHistoryRemoteUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallHistoryRemoteUDPPort_Type.__name__ = "Integer32"
_CvVoIPCallHistoryRemoteUDPPort_Object = MibTableColumn
cvVoIPCallHistoryRemoteUDPPort = _CvVoIPCallHistoryRemoteUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 3),
    _CvVoIPCallHistoryRemoteUDPPort_Type()
)
cvVoIPCallHistoryRemoteUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemoteUDPPort.setStatus("deprecated")
_CvVoIPCallHistoryRoundTripDelay_Type = Gauge32
_CvVoIPCallHistoryRoundTripDelay_Object = MibTableColumn
cvVoIPCallHistoryRoundTripDelay = _CvVoIPCallHistoryRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 4),
    _CvVoIPCallHistoryRoundTripDelay_Type()
)
cvVoIPCallHistoryRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRoundTripDelay.setUnits("milliseconds")
_CvVoIPCallHistorySelectedQoS_Type = QosService
_CvVoIPCallHistorySelectedQoS_Object = MibTableColumn
cvVoIPCallHistorySelectedQoS = _CvVoIPCallHistorySelectedQoS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 5),
    _CvVoIPCallHistorySelectedQoS_Type()
)
cvVoIPCallHistorySelectedQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistorySelectedQoS.setStatus("current")
_CvVoIPCallHistorySessionProtocol_Type = CvSessionProtocol
_CvVoIPCallHistorySessionProtocol_Object = MibTableColumn
cvVoIPCallHistorySessionProtocol = _CvVoIPCallHistorySessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 6),
    _CvVoIPCallHistorySessionProtocol_Type()
)
cvVoIPCallHistorySessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistorySessionProtocol.setStatus("current")
_CvVoIPCallHistorySessionTarget_Type = DisplayString
_CvVoIPCallHistorySessionTarget_Object = MibTableColumn
cvVoIPCallHistorySessionTarget = _CvVoIPCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 7),
    _CvVoIPCallHistorySessionTarget_Type()
)
cvVoIPCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistorySessionTarget.setStatus("current")
_CvVoIPCallHistoryOnTimeRvPlayout_Type = AbsoluteCounter32
_CvVoIPCallHistoryOnTimeRvPlayout_Object = MibTableColumn
cvVoIPCallHistoryOnTimeRvPlayout = _CvVoIPCallHistoryOnTimeRvPlayout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 8),
    _CvVoIPCallHistoryOnTimeRvPlayout_Type()
)
cvVoIPCallHistoryOnTimeRvPlayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryOnTimeRvPlayout.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryOnTimeRvPlayout.setUnits("milliseconds")
_CvVoIPCallHistoryGapFillWithSilence_Type = AbsoluteCounter32
_CvVoIPCallHistoryGapFillWithSilence_Object = MibTableColumn
cvVoIPCallHistoryGapFillWithSilence = _CvVoIPCallHistoryGapFillWithSilence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 9),
    _CvVoIPCallHistoryGapFillWithSilence_Type()
)
cvVoIPCallHistoryGapFillWithSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithSilence.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithSilence.setUnits("milliseconds")
_CvVoIPCallHistoryGapFillWithPrediction_Type = AbsoluteCounter32
_CvVoIPCallHistoryGapFillWithPrediction_Object = MibTableColumn
cvVoIPCallHistoryGapFillWithPrediction = _CvVoIPCallHistoryGapFillWithPrediction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 10),
    _CvVoIPCallHistoryGapFillWithPrediction_Type()
)
cvVoIPCallHistoryGapFillWithPrediction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithPrediction.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithPrediction.setUnits("milliseconds")
_CvVoIPCallHistoryGapFillWithInterpolation_Type = AbsoluteCounter32
_CvVoIPCallHistoryGapFillWithInterpolation_Object = MibTableColumn
cvVoIPCallHistoryGapFillWithInterpolation = _CvVoIPCallHistoryGapFillWithInterpolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 11),
    _CvVoIPCallHistoryGapFillWithInterpolation_Type()
)
cvVoIPCallHistoryGapFillWithInterpolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithInterpolation.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithInterpolation.setUnits("milliseconds")
_CvVoIPCallHistoryGapFillWithRedundancy_Type = AbsoluteCounter32
_CvVoIPCallHistoryGapFillWithRedundancy_Object = MibTableColumn
cvVoIPCallHistoryGapFillWithRedundancy = _CvVoIPCallHistoryGapFillWithRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 12),
    _CvVoIPCallHistoryGapFillWithRedundancy_Type()
)
cvVoIPCallHistoryGapFillWithRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithRedundancy.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryGapFillWithRedundancy.setUnits("milliseconds")
_CvVoIPCallHistoryHiWaterPlayoutDelay_Type = AbsoluteCounter32
_CvVoIPCallHistoryHiWaterPlayoutDelay_Object = MibTableColumn
cvVoIPCallHistoryHiWaterPlayoutDelay = _CvVoIPCallHistoryHiWaterPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 13),
    _CvVoIPCallHistoryHiWaterPlayoutDelay_Type()
)
cvVoIPCallHistoryHiWaterPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryHiWaterPlayoutDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryHiWaterPlayoutDelay.setUnits("milliseconds")
_CvVoIPCallHistoryLoWaterPlayoutDelay_Type = Gauge32
_CvVoIPCallHistoryLoWaterPlayoutDelay_Object = MibTableColumn
cvVoIPCallHistoryLoWaterPlayoutDelay = _CvVoIPCallHistoryLoWaterPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 14),
    _CvVoIPCallHistoryLoWaterPlayoutDelay_Type()
)
cvVoIPCallHistoryLoWaterPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLoWaterPlayoutDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLoWaterPlayoutDelay.setUnits("milliseconds")
_CvVoIPCallHistoryReceiveDelay_Type = Gauge32
_CvVoIPCallHistoryReceiveDelay_Object = MibTableColumn
cvVoIPCallHistoryReceiveDelay = _CvVoIPCallHistoryReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 15),
    _CvVoIPCallHistoryReceiveDelay_Type()
)
cvVoIPCallHistoryReceiveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryReceiveDelay.setStatus("current")
_CvVoIPCallHistoryVADEnable_Type = TruthValue
_CvVoIPCallHistoryVADEnable_Object = MibTableColumn
cvVoIPCallHistoryVADEnable = _CvVoIPCallHistoryVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 16),
    _CvVoIPCallHistoryVADEnable_Type()
)
cvVoIPCallHistoryVADEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryVADEnable.setStatus("deprecated")
_CvVoIPCallHistoryCoderTypeRate_Type = CvcCoderTypeRate
_CvVoIPCallHistoryCoderTypeRate_Object = MibTableColumn
cvVoIPCallHistoryCoderTypeRate = _CvVoIPCallHistoryCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 17),
    _CvVoIPCallHistoryCoderTypeRate_Type()
)
cvVoIPCallHistoryCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCoderTypeRate.setStatus("deprecated")


class _CvVoIPCallHistoryIcpif_Type(Integer32):
    """Custom type cvVoIPCallHistoryIcpif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 55),
    )


_CvVoIPCallHistoryIcpif_Type.__name__ = "Integer32"
_CvVoIPCallHistoryIcpif_Object = MibTableColumn
cvVoIPCallHistoryIcpif = _CvVoIPCallHistoryIcpif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 18),
    _CvVoIPCallHistoryIcpif_Type()
)
cvVoIPCallHistoryIcpif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryIcpif.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryIcpif.setUnits("equipment impairment factor (eif)")
_CvVoIPCallHistoryLostPackets_Type = AbsoluteCounter32
_CvVoIPCallHistoryLostPackets_Object = MibTableColumn
cvVoIPCallHistoryLostPackets = _CvVoIPCallHistoryLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 19),
    _CvVoIPCallHistoryLostPackets_Type()
)
cvVoIPCallHistoryLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLostPackets.setUnits("packets")
_CvVoIPCallHistoryEarlyPackets_Type = AbsoluteCounter32
_CvVoIPCallHistoryEarlyPackets_Object = MibTableColumn
cvVoIPCallHistoryEarlyPackets = _CvVoIPCallHistoryEarlyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 20),
    _CvVoIPCallHistoryEarlyPackets_Type()
)
cvVoIPCallHistoryEarlyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryEarlyPackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryEarlyPackets.setUnits("packets")
_CvVoIPCallHistoryLatePackets_Type = AbsoluteCounter32
_CvVoIPCallHistoryLatePackets_Object = MibTableColumn
cvVoIPCallHistoryLatePackets = _CvVoIPCallHistoryLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 21),
    _CvVoIPCallHistoryLatePackets_Type()
)
cvVoIPCallHistoryLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLatePackets.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryLatePackets.setUnits("packets")


class _CvVoIPCallHistoryUsername_Type(SnmpAdminString):
    """Custom type cvVoIPCallHistoryUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CvVoIPCallHistoryUsername_Type.__name__ = "SnmpAdminString"
_CvVoIPCallHistoryUsername_Object = MibTableColumn
cvVoIPCallHistoryUsername = _CvVoIPCallHistoryUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 22),
    _CvVoIPCallHistoryUsername_Type()
)
cvVoIPCallHistoryUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryUsername.setStatus("current")


class _CvVoIPCallHistoryProtocolCallId_Type(OctetString):
    """Custom type cvVoIPCallHistoryProtocolCallId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvVoIPCallHistoryProtocolCallId_Type.__name__ = "OctetString"
_CvVoIPCallHistoryProtocolCallId_Object = MibTableColumn
cvVoIPCallHistoryProtocolCallId = _CvVoIPCallHistoryProtocolCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 23),
    _CvVoIPCallHistoryProtocolCallId_Type()
)
cvVoIPCallHistoryProtocolCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryProtocolCallId.setStatus("current")
_CvVoIPCallHistoryRemSigIPAddrT_Type = InetAddressType
_CvVoIPCallHistoryRemSigIPAddrT_Object = MibTableColumn
cvVoIPCallHistoryRemSigIPAddrT = _CvVoIPCallHistoryRemSigIPAddrT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 24),
    _CvVoIPCallHistoryRemSigIPAddrT_Type()
)
cvVoIPCallHistoryRemSigIPAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemSigIPAddrT.setStatus("current")
_CvVoIPCallHistoryRemSigIPAddr_Type = InetAddress
_CvVoIPCallHistoryRemSigIPAddr_Object = MibTableColumn
cvVoIPCallHistoryRemSigIPAddr = _CvVoIPCallHistoryRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 25),
    _CvVoIPCallHistoryRemSigIPAddr_Type()
)
cvVoIPCallHistoryRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemSigIPAddr.setStatus("current")


class _CvVoIPCallHistoryRemSigPort_Type(Integer32):
    """Custom type cvVoIPCallHistoryRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallHistoryRemSigPort_Type.__name__ = "Integer32"
_CvVoIPCallHistoryRemSigPort_Object = MibTableColumn
cvVoIPCallHistoryRemSigPort = _CvVoIPCallHistoryRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 26),
    _CvVoIPCallHistoryRemSigPort_Type()
)
cvVoIPCallHistoryRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemSigPort.setStatus("current")
_CvVoIPCallHistoryRemMediaIPAddrT_Type = InetAddressType
_CvVoIPCallHistoryRemMediaIPAddrT_Object = MibTableColumn
cvVoIPCallHistoryRemMediaIPAddrT = _CvVoIPCallHistoryRemMediaIPAddrT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 27),
    _CvVoIPCallHistoryRemMediaIPAddrT_Type()
)
cvVoIPCallHistoryRemMediaIPAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemMediaIPAddrT.setStatus("current")
_CvVoIPCallHistoryRemMediaIPAddr_Type = InetAddress
_CvVoIPCallHistoryRemMediaIPAddr_Object = MibTableColumn
cvVoIPCallHistoryRemMediaIPAddr = _CvVoIPCallHistoryRemMediaIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 28),
    _CvVoIPCallHistoryRemMediaIPAddr_Type()
)
cvVoIPCallHistoryRemMediaIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemMediaIPAddr.setStatus("current")


class _CvVoIPCallHistoryRemMediaPort_Type(Integer32):
    """Custom type cvVoIPCallHistoryRemMediaPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvVoIPCallHistoryRemMediaPort_Type.__name__ = "Integer32"
_CvVoIPCallHistoryRemMediaPort_Object = MibTableColumn
cvVoIPCallHistoryRemMediaPort = _CvVoIPCallHistoryRemMediaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 29),
    _CvVoIPCallHistoryRemMediaPort_Type()
)
cvVoIPCallHistoryRemMediaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRemMediaPort.setStatus("current")
_CvVoIPCallHistorySRTPEnable_Type = TruthValue
_CvVoIPCallHistorySRTPEnable_Object = MibTableColumn
cvVoIPCallHistorySRTPEnable = _CvVoIPCallHistorySRTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 30),
    _CvVoIPCallHistorySRTPEnable_Type()
)
cvVoIPCallHistorySRTPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistorySRTPEnable.setStatus("current")
_CvVoIPCallHistoryFallbackIcpif_Type = Integer32
_CvVoIPCallHistoryFallbackIcpif_Object = MibTableColumn
cvVoIPCallHistoryFallbackIcpif = _CvVoIPCallHistoryFallbackIcpif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 31),
    _CvVoIPCallHistoryFallbackIcpif_Type()
)
cvVoIPCallHistoryFallbackIcpif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryFallbackIcpif.setStatus("current")
_CvVoIPCallHistoryFallbackLoss_Type = AbsoluteCounter32
_CvVoIPCallHistoryFallbackLoss_Object = MibTableColumn
cvVoIPCallHistoryFallbackLoss = _CvVoIPCallHistoryFallbackLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 32),
    _CvVoIPCallHistoryFallbackLoss_Type()
)
cvVoIPCallHistoryFallbackLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryFallbackLoss.setStatus("current")
_CvVoIPCallHistoryFallbackDelay_Type = Gauge32
_CvVoIPCallHistoryFallbackDelay_Object = MibTableColumn
cvVoIPCallHistoryFallbackDelay = _CvVoIPCallHistoryFallbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 33),
    _CvVoIPCallHistoryFallbackDelay_Type()
)
cvVoIPCallHistoryFallbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryFallbackDelay.setStatus("current")
_CvVoIPCallHistoryOctetAligned_Type = TruthValue
_CvVoIPCallHistoryOctetAligned_Object = MibTableColumn
cvVoIPCallHistoryOctetAligned = _CvVoIPCallHistoryOctetAligned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 34),
    _CvVoIPCallHistoryOctetAligned_Type()
)
cvVoIPCallHistoryOctetAligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryOctetAligned.setStatus("current")
_CvVoIPCallHistoryBitRates_Type = CvAmrNbBitRateMode
_CvVoIPCallHistoryBitRates_Object = MibTableColumn
cvVoIPCallHistoryBitRates = _CvVoIPCallHistoryBitRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 35),
    _CvVoIPCallHistoryBitRates_Type()
)
cvVoIPCallHistoryBitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryBitRates.setStatus("current")


class _CvVoIPCallHistoryModeChgPeriod_Type(Integer32):
    """Custom type cvVoIPCallHistoryModeChgPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CvVoIPCallHistoryModeChgPeriod_Type.__name__ = "Integer32"
_CvVoIPCallHistoryModeChgPeriod_Object = MibTableColumn
cvVoIPCallHistoryModeChgPeriod = _CvVoIPCallHistoryModeChgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 36),
    _CvVoIPCallHistoryModeChgPeriod_Type()
)
cvVoIPCallHistoryModeChgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryModeChgPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryModeChgPeriod.setUnits("frame-blocks")
_CvVoIPCallHistoryModeChgNeighbor_Type = TruthValue
_CvVoIPCallHistoryModeChgNeighbor_Object = MibTableColumn
cvVoIPCallHistoryModeChgNeighbor = _CvVoIPCallHistoryModeChgNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 37),
    _CvVoIPCallHistoryModeChgNeighbor_Type()
)
cvVoIPCallHistoryModeChgNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryModeChgNeighbor.setStatus("current")


class _CvVoIPCallHistoryMaxPtime_Type(Integer32):
    """Custom type cvVoIPCallHistoryMaxPtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CvVoIPCallHistoryMaxPtime_Type.__name__ = "Integer32"
_CvVoIPCallHistoryMaxPtime_Object = MibTableColumn
cvVoIPCallHistoryMaxPtime = _CvVoIPCallHistoryMaxPtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 38),
    _CvVoIPCallHistoryMaxPtime_Type()
)
cvVoIPCallHistoryMaxPtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryMaxPtime.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryMaxPtime.setUnits("milliseconds")
_CvVoIPCallHistoryCRC_Type = TruthValue
_CvVoIPCallHistoryCRC_Object = MibTableColumn
cvVoIPCallHistoryCRC = _CvVoIPCallHistoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 39),
    _CvVoIPCallHistoryCRC_Type()
)
cvVoIPCallHistoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCRC.setStatus("current")
_CvVoIPCallHistoryRobustSorting_Type = TruthValue
_CvVoIPCallHistoryRobustSorting_Object = MibTableColumn
cvVoIPCallHistoryRobustSorting = _CvVoIPCallHistoryRobustSorting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 40),
    _CvVoIPCallHistoryRobustSorting_Type()
)
cvVoIPCallHistoryRobustSorting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryRobustSorting.setStatus("current")
_CvVoIPCallHistoryEncap_Type = CvAmrNbRtpEncap
_CvVoIPCallHistoryEncap_Object = MibTableColumn
cvVoIPCallHistoryEncap = _CvVoIPCallHistoryEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 41),
    _CvVoIPCallHistoryEncap_Type()
)
cvVoIPCallHistoryEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryEncap.setStatus("current")


class _CvVoIPCallHistoryInterleaving_Type(Integer32):
    """Custom type cvVoIPCallHistoryInterleaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CvVoIPCallHistoryInterleaving_Type.__name__ = "Integer32"
_CvVoIPCallHistoryInterleaving_Object = MibTableColumn
cvVoIPCallHistoryInterleaving = _CvVoIPCallHistoryInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 42),
    _CvVoIPCallHistoryInterleaving_Type()
)
cvVoIPCallHistoryInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryInterleaving.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryInterleaving.setUnits("frame-blocks")


class _CvVoIPCallHistoryPtime_Type(Integer32):
    """Custom type cvVoIPCallHistoryPtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CvVoIPCallHistoryPtime_Type.__name__ = "Integer32"
_CvVoIPCallHistoryPtime_Object = MibTableColumn
cvVoIPCallHistoryPtime = _CvVoIPCallHistoryPtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 43),
    _CvVoIPCallHistoryPtime_Type()
)
cvVoIPCallHistoryPtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryPtime.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryPtime.setUnits("milliseconds")


class _CvVoIPCallHistoryChannels_Type(Integer32):
    """Custom type cvVoIPCallHistoryChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CvVoIPCallHistoryChannels_Type.__name__ = "Integer32"
_CvVoIPCallHistoryChannels_Object = MibTableColumn
cvVoIPCallHistoryChannels = _CvVoIPCallHistoryChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 44),
    _CvVoIPCallHistoryChannels_Type()
)
cvVoIPCallHistoryChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryChannels.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryChannels.setUnits("channels")
_CvVoIPCallHistoryCoderMode_Type = CvIlbcFrameMode
_CvVoIPCallHistoryCoderMode_Object = MibTableColumn
cvVoIPCallHistoryCoderMode = _CvVoIPCallHistoryCoderMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 45),
    _CvVoIPCallHistoryCoderMode_Type()
)
cvVoIPCallHistoryCoderMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCoderMode.setStatus("current")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCoderMode.setUnits("milliseconds")


class _CvVoIPCallHistoryCallId_Type(Unsigned32):
    """Custom type cvVoIPCallHistoryCallId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvVoIPCallHistoryCallId_Type.__name__ = "Unsigned32"
_CvVoIPCallHistoryCallId_Object = MibTableColumn
cvVoIPCallHistoryCallId = _CvVoIPCallHistoryCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 46),
    _CvVoIPCallHistoryCallId_Type()
)
cvVoIPCallHistoryCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCallId.setStatus("current")
_CvVoIPCallHistoryCallReferenceId_Type = CvcCallReferenceIdOrZero
_CvVoIPCallHistoryCallReferenceId_Object = MibTableColumn
cvVoIPCallHistoryCallReferenceId = _CvVoIPCallHistoryCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 47),
    _CvVoIPCallHistoryCallReferenceId_Type()
)
cvVoIPCallHistoryCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistoryCallReferenceId.setStatus("current")
_CvVoIPCallHistorySessionId_Type = Unsigned32
_CvVoIPCallHistorySessionId_Object = MibTableColumn
cvVoIPCallHistorySessionId = _CvVoIPCallHistorySessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 2, 1, 48),
    _CvVoIPCallHistorySessionId_Type()
)
cvVoIPCallHistorySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvVoIPCallHistorySessionId.setStatus("current")
_CvCallVolumeStatsHistory_ObjectIdentity = ObjectIdentity
cvCallVolumeStatsHistory = _CvCallVolumeStatsHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3)
)
_CvCallRateStatsTable_Object = MibTable
cvCallRateStatsTable = _CvCallRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cvCallRateStatsTable.setStatus("current")
_CvCallRateStatsEntry_Object = MibTableRow
cvCallRateStatsEntry = _CvCallRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1, 1)
)
cvCallRateStatsEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateStatsIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateStatsIntvlDur"),
)
if mibBuilder.loadTexts:
    cvCallRateStatsEntry.setStatus("current")
_CvCallRateStatsIntvlDurUnits_Type = CvCallVolumeStatsIntvlType
_CvCallRateStatsIntvlDurUnits_Object = MibTableColumn
cvCallRateStatsIntvlDurUnits = _CvCallRateStatsIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1, 1, 1),
    _CvCallRateStatsIntvlDurUnits_Type()
)
cvCallRateStatsIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallRateStatsIntvlDurUnits.setStatus("current")


class _CvCallRateStatsIntvlDur_Type(Unsigned32):
    """Custom type cvCallRateStatsIntvlDur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_CvCallRateStatsIntvlDur_Type.__name__ = "Unsigned32"
_CvCallRateStatsIntvlDur_Object = MibTableColumn
cvCallRateStatsIntvlDur = _CvCallRateStatsIntvlDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1, 1, 2),
    _CvCallRateStatsIntvlDur_Type()
)
cvCallRateStatsIntvlDur.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallRateStatsIntvlDur.setStatus("current")
_CvCallRateStatsMaxVal_Type = Unsigned32
_CvCallRateStatsMaxVal_Object = MibTableColumn
cvCallRateStatsMaxVal = _CvCallRateStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1, 1, 3),
    _CvCallRateStatsMaxVal_Type()
)
cvCallRateStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRateStatsMaxVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallRateStatsMaxVal.setUnits("calls-per-second")
_CvCallRateStatsAvgVal_Type = Unsigned32
_CvCallRateStatsAvgVal_Object = MibTableColumn
cvCallRateStatsAvgVal = _CvCallRateStatsAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 1, 1, 4),
    _CvCallRateStatsAvgVal_Type()
)
cvCallRateStatsAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRateStatsAvgVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallRateStatsAvgVal.setUnits("calls-per-second")
_CvCallLegRateStatsTable_Object = MibTable
cvCallLegRateStatsTable = _CvCallLegRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    cvCallLegRateStatsTable.setStatus("current")
_CvCallLegRateStatsEntry_Object = MibTableRow
cvCallLegRateStatsEntry = _CvCallLegRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2, 1)
)
cvCallLegRateStatsEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateStatsIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateStatsIntvlDur"),
)
if mibBuilder.loadTexts:
    cvCallLegRateStatsEntry.setStatus("current")
_CvCallLegRateStatsIntvlDurUnits_Type = CvCallVolumeStatsIntvlType
_CvCallLegRateStatsIntvlDurUnits_Object = MibTableColumn
cvCallLegRateStatsIntvlDurUnits = _CvCallLegRateStatsIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2, 1, 1),
    _CvCallLegRateStatsIntvlDurUnits_Type()
)
cvCallLegRateStatsIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallLegRateStatsIntvlDurUnits.setStatus("current")


class _CvCallLegRateStatsIntvlDur_Type(Unsigned32):
    """Custom type cvCallLegRateStatsIntvlDur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_CvCallLegRateStatsIntvlDur_Type.__name__ = "Unsigned32"
_CvCallLegRateStatsIntvlDur_Object = MibTableColumn
cvCallLegRateStatsIntvlDur = _CvCallLegRateStatsIntvlDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2, 1, 2),
    _CvCallLegRateStatsIntvlDur_Type()
)
cvCallLegRateStatsIntvlDur.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallLegRateStatsIntvlDur.setStatus("current")
_CvCallLegRateStatsMaxVal_Type = Unsigned32
_CvCallLegRateStatsMaxVal_Object = MibTableColumn
cvCallLegRateStatsMaxVal = _CvCallLegRateStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2, 1, 3),
    _CvCallLegRateStatsMaxVal_Type()
)
cvCallLegRateStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallLegRateStatsMaxVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallLegRateStatsMaxVal.setUnits("call-legs per second")
_CvCallLegRateStatsAvgVal_Type = Unsigned32
_CvCallLegRateStatsAvgVal_Object = MibTableColumn
cvCallLegRateStatsAvgVal = _CvCallLegRateStatsAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 2, 1, 4),
    _CvCallLegRateStatsAvgVal_Type()
)
cvCallLegRateStatsAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallLegRateStatsAvgVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallLegRateStatsAvgVal.setUnits("call-legs per second")
_CvActiveCallStatsTable_Object = MibTable
cvActiveCallStatsTable = _CvActiveCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    cvActiveCallStatsTable.setStatus("current")
_CvActiveCallStatsEntry_Object = MibTableRow
cvActiveCallStatsEntry = _CvActiveCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3, 1)
)
cvActiveCallStatsEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallStatsIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallStatsIntvlDur"),
)
if mibBuilder.loadTexts:
    cvActiveCallStatsEntry.setStatus("current")
_CvActiveCallStatsIntvlDurUnits_Type = CvCallVolumeStatsIntvlType
_CvActiveCallStatsIntvlDurUnits_Object = MibTableColumn
cvActiveCallStatsIntvlDurUnits = _CvActiveCallStatsIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3, 1, 1),
    _CvActiveCallStatsIntvlDurUnits_Type()
)
cvActiveCallStatsIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvActiveCallStatsIntvlDurUnits.setStatus("current")


class _CvActiveCallStatsIntvlDur_Type(Unsigned32):
    """Custom type cvActiveCallStatsIntvlDur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_CvActiveCallStatsIntvlDur_Type.__name__ = "Unsigned32"
_CvActiveCallStatsIntvlDur_Object = MibTableColumn
cvActiveCallStatsIntvlDur = _CvActiveCallStatsIntvlDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3, 1, 2),
    _CvActiveCallStatsIntvlDur_Type()
)
cvActiveCallStatsIntvlDur.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvActiveCallStatsIntvlDur.setStatus("current")
_CvActiveCallStatsMaxVal_Type = Unsigned32
_CvActiveCallStatsMaxVal_Object = MibTableColumn
cvActiveCallStatsMaxVal = _CvActiveCallStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3, 1, 3),
    _CvActiveCallStatsMaxVal_Type()
)
cvActiveCallStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvActiveCallStatsMaxVal.setStatus("current")
if mibBuilder.loadTexts:
    cvActiveCallStatsMaxVal.setUnits("calls")
_CvActiveCallStatsAvgVal_Type = Unsigned32
_CvActiveCallStatsAvgVal_Object = MibTableColumn
cvActiveCallStatsAvgVal = _CvActiveCallStatsAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 3, 1, 4),
    _CvActiveCallStatsAvgVal_Type()
)
cvActiveCallStatsAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvActiveCallStatsAvgVal.setStatus("current")
if mibBuilder.loadTexts:
    cvActiveCallStatsAvgVal.setUnits("calls")
_CvCallDurationStatsTable_Object = MibTable
cvCallDurationStatsTable = _CvCallDurationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    cvCallDurationStatsTable.setStatus("current")
_CvCallDurationStatsEntry_Object = MibTableRow
cvCallDurationStatsEntry = _CvCallDurationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4, 1)
)
cvCallDurationStatsEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallDurationStatsIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallDurationStatsIntvlDur"),
)
if mibBuilder.loadTexts:
    cvCallDurationStatsEntry.setStatus("current")
_CvCallDurationStatsIntvlDurUnits_Type = CvCallVolumeStatsIntvlType
_CvCallDurationStatsIntvlDurUnits_Object = MibTableColumn
cvCallDurationStatsIntvlDurUnits = _CvCallDurationStatsIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4, 1, 1),
    _CvCallDurationStatsIntvlDurUnits_Type()
)
cvCallDurationStatsIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallDurationStatsIntvlDurUnits.setStatus("current")


class _CvCallDurationStatsIntvlDur_Type(Unsigned32):
    """Custom type cvCallDurationStatsIntvlDur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_CvCallDurationStatsIntvlDur_Type.__name__ = "Unsigned32"
_CvCallDurationStatsIntvlDur_Object = MibTableColumn
cvCallDurationStatsIntvlDur = _CvCallDurationStatsIntvlDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4, 1, 2),
    _CvCallDurationStatsIntvlDur_Type()
)
cvCallDurationStatsIntvlDur.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallDurationStatsIntvlDur.setStatus("current")
_CvCallDurationStatsMaxVal_Type = Unsigned32
_CvCallDurationStatsMaxVal_Object = MibTableColumn
cvCallDurationStatsMaxVal = _CvCallDurationStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4, 1, 3),
    _CvCallDurationStatsMaxVal_Type()
)
cvCallDurationStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallDurationStatsMaxVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallDurationStatsMaxVal.setUnits("calls")
_CvCallDurationStatsAvgVal_Type = Unsigned32
_CvCallDurationStatsAvgVal_Object = MibTableColumn
cvCallDurationStatsAvgVal = _CvCallDurationStatsAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 4, 1, 4),
    _CvCallDurationStatsAvgVal_Type()
)
cvCallDurationStatsAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallDurationStatsAvgVal.setStatus("current")
if mibBuilder.loadTexts:
    cvCallDurationStatsAvgVal.setUnits("calls")
_CvSipMsgRateStatsTable_Object = MibTable
cvSipMsgRateStatsTable = _CvSipMsgRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    cvSipMsgRateStatsTable.setStatus("current")
_CvSipMsgRateStatsEntry_Object = MibTableRow
cvSipMsgRateStatsEntry = _CvSipMsgRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5, 1)
)
cvSipMsgRateStatsEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateStatsIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateStatsIntvlDur"),
)
if mibBuilder.loadTexts:
    cvSipMsgRateStatsEntry.setStatus("current")
_CvSipMsgRateStatsIntvlDurUnits_Type = CvCallVolumeStatsIntvlType
_CvSipMsgRateStatsIntvlDurUnits_Object = MibTableColumn
cvSipMsgRateStatsIntvlDurUnits = _CvSipMsgRateStatsIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5, 1, 1),
    _CvSipMsgRateStatsIntvlDurUnits_Type()
)
cvSipMsgRateStatsIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsIntvlDurUnits.setStatus("current")


class _CvSipMsgRateStatsIntvlDur_Type(Unsigned32):
    """Custom type cvSipMsgRateStatsIntvlDur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_CvSipMsgRateStatsIntvlDur_Type.__name__ = "Unsigned32"
_CvSipMsgRateStatsIntvlDur_Object = MibTableColumn
cvSipMsgRateStatsIntvlDur = _CvSipMsgRateStatsIntvlDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5, 1, 2),
    _CvSipMsgRateStatsIntvlDur_Type()
)
cvSipMsgRateStatsIntvlDur.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsIntvlDur.setStatus("current")
_CvSipMsgRateStatsMaxVal_Type = Unsigned32
_CvSipMsgRateStatsMaxVal_Object = MibTableColumn
cvSipMsgRateStatsMaxVal = _CvSipMsgRateStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5, 1, 3),
    _CvSipMsgRateStatsMaxVal_Type()
)
cvSipMsgRateStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsMaxVal.setStatus("current")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsMaxVal.setUnits("SIP messages per second")
_CvSipMsgRateStatsAvgVal_Type = Unsigned32
_CvSipMsgRateStatsAvgVal_Object = MibTableColumn
cvSipMsgRateStatsAvgVal = _CvSipMsgRateStatsAvgVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 5, 1, 4),
    _CvSipMsgRateStatsAvgVal_Type()
)
cvSipMsgRateStatsAvgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsAvgVal.setStatus("current")
if mibBuilder.loadTexts:
    cvSipMsgRateStatsAvgVal.setUnits("SIP messages per second")
_CvCallRateWMTable_Object = MibTable
cvCallRateWMTable = _CvCallRateWMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    cvCallRateWMTable.setStatus("current")
_CvCallRateWMEntry_Object = MibTableRow
cvCallRateWMEntry = _CvCallRateWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6, 1)
)
cvCallRateWMEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateWMIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateWMIndex"),
)
if mibBuilder.loadTexts:
    cvCallRateWMEntry.setStatus("current")
_CvCallRateWMIntvlDurUnits_Type = CvCallVolumeWMIntvlType
_CvCallRateWMIntvlDurUnits_Object = MibTableColumn
cvCallRateWMIntvlDurUnits = _CvCallRateWMIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6, 1, 1),
    _CvCallRateWMIntvlDurUnits_Type()
)
cvCallRateWMIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallRateWMIntvlDurUnits.setStatus("current")


class _CvCallRateWMIndex_Type(Unsigned32):
    """Custom type cvCallRateWMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvCallRateWMIndex_Type.__name__ = "Unsigned32"
_CvCallRateWMIndex_Object = MibTableColumn
cvCallRateWMIndex = _CvCallRateWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6, 1, 2),
    _CvCallRateWMIndex_Type()
)
cvCallRateWMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallRateWMIndex.setStatus("current")
_CvCallRateWMValue_Type = Unsigned32
_CvCallRateWMValue_Object = MibTableColumn
cvCallRateWMValue = _CvCallRateWMValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6, 1, 3),
    _CvCallRateWMValue_Type()
)
cvCallRateWMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRateWMValue.setStatus("current")
if mibBuilder.loadTexts:
    cvCallRateWMValue.setUnits("calls per second")
_CvCallRateWMts_Type = DateAndTime
_CvCallRateWMts_Object = MibTableColumn
cvCallRateWMts = _CvCallRateWMts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 6, 1, 4),
    _CvCallRateWMts_Type()
)
cvCallRateWMts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallRateWMts.setStatus("current")
_CvCallLegRateWMTable_Object = MibTable
cvCallLegRateWMTable = _CvCallLegRateWMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    cvCallLegRateWMTable.setStatus("current")
_CvCallLegRateWMEntry_Object = MibTableRow
cvCallLegRateWMEntry = _CvCallLegRateWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7, 1)
)
cvCallLegRateWMEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateWMIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateWMIndex"),
)
if mibBuilder.loadTexts:
    cvCallLegRateWMEntry.setStatus("current")
_CvCallLegRateWMIntvlDurUnits_Type = CvCallVolumeWMIntvlType
_CvCallLegRateWMIntvlDurUnits_Object = MibTableColumn
cvCallLegRateWMIntvlDurUnits = _CvCallLegRateWMIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7, 1, 1),
    _CvCallLegRateWMIntvlDurUnits_Type()
)
cvCallLegRateWMIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallLegRateWMIntvlDurUnits.setStatus("current")


class _CvCallLegRateWMIndex_Type(Unsigned32):
    """Custom type cvCallLegRateWMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvCallLegRateWMIndex_Type.__name__ = "Unsigned32"
_CvCallLegRateWMIndex_Object = MibTableColumn
cvCallLegRateWMIndex = _CvCallLegRateWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7, 1, 2),
    _CvCallLegRateWMIndex_Type()
)
cvCallLegRateWMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvCallLegRateWMIndex.setStatus("current")
_CvCallLegRateWMValue_Type = Unsigned32
_CvCallLegRateWMValue_Object = MibTableColumn
cvCallLegRateWMValue = _CvCallLegRateWMValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7, 1, 3),
    _CvCallLegRateWMValue_Type()
)
cvCallLegRateWMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallLegRateWMValue.setStatus("current")
if mibBuilder.loadTexts:
    cvCallLegRateWMValue.setUnits("call legs per second")
_CvCallLegRateWMts_Type = DateAndTime
_CvCallLegRateWMts_Object = MibTableColumn
cvCallLegRateWMts = _CvCallLegRateWMts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 7, 1, 4),
    _CvCallLegRateWMts_Type()
)
cvCallLegRateWMts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCallLegRateWMts.setStatus("current")
_CvActiveCallWMTable_Object = MibTable
cvActiveCallWMTable = _CvActiveCallWMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8)
)
if mibBuilder.loadTexts:
    cvActiveCallWMTable.setStatus("current")
_CvActiveCallWMEntry_Object = MibTableRow
cvActiveCallWMEntry = _CvActiveCallWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8, 1)
)
cvActiveCallWMEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallWMIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallWMIndex"),
)
if mibBuilder.loadTexts:
    cvActiveCallWMEntry.setStatus("current")
_CvActiveCallWMIntvlDurUnits_Type = CvCallVolumeWMIntvlType
_CvActiveCallWMIntvlDurUnits_Object = MibTableColumn
cvActiveCallWMIntvlDurUnits = _CvActiveCallWMIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8, 1, 1),
    _CvActiveCallWMIntvlDurUnits_Type()
)
cvActiveCallWMIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvActiveCallWMIntvlDurUnits.setStatus("current")


class _CvActiveCallWMIndex_Type(Unsigned32):
    """Custom type cvActiveCallWMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvActiveCallWMIndex_Type.__name__ = "Unsigned32"
_CvActiveCallWMIndex_Object = MibTableColumn
cvActiveCallWMIndex = _CvActiveCallWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8, 1, 2),
    _CvActiveCallWMIndex_Type()
)
cvActiveCallWMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvActiveCallWMIndex.setStatus("current")
_CvActiveCallWMValue_Type = Unsigned32
_CvActiveCallWMValue_Object = MibTableColumn
cvActiveCallWMValue = _CvActiveCallWMValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8, 1, 3),
    _CvActiveCallWMValue_Type()
)
cvActiveCallWMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvActiveCallWMValue.setStatus("current")
if mibBuilder.loadTexts:
    cvActiveCallWMValue.setUnits("calls")
_CvActiveCallWMts_Type = DateAndTime
_CvActiveCallWMts_Object = MibTableColumn
cvActiveCallWMts = _CvActiveCallWMts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 8, 1, 4),
    _CvActiveCallWMts_Type()
)
cvActiveCallWMts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvActiveCallWMts.setStatus("current")
_CvSipMsgRateWMTable_Object = MibTable
cvSipMsgRateWMTable = _CvSipMsgRateWMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9)
)
if mibBuilder.loadTexts:
    cvSipMsgRateWMTable.setStatus("current")
_CvSipMsgRateWMEntry_Object = MibTableRow
cvSipMsgRateWMEntry = _CvSipMsgRateWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9, 1)
)
cvSipMsgRateWMEntry.setIndexNames(
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateWMIntvlDurUnits"),
    (0, "CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateWMIndex"),
)
if mibBuilder.loadTexts:
    cvSipMsgRateWMEntry.setStatus("current")
_CvSipMsgRateWMIntvlDurUnits_Type = CvCallVolumeWMIntvlType
_CvSipMsgRateWMIntvlDurUnits_Object = MibTableColumn
cvSipMsgRateWMIntvlDurUnits = _CvSipMsgRateWMIntvlDurUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9, 1, 1),
    _CvSipMsgRateWMIntvlDurUnits_Type()
)
cvSipMsgRateWMIntvlDurUnits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvSipMsgRateWMIntvlDurUnits.setStatus("current")


class _CvSipMsgRateWMIndex_Type(Unsigned32):
    """Custom type cvSipMsgRateWMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvSipMsgRateWMIndex_Type.__name__ = "Unsigned32"
_CvSipMsgRateWMIndex_Object = MibTableColumn
cvSipMsgRateWMIndex = _CvSipMsgRateWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9, 1, 2),
    _CvSipMsgRateWMIndex_Type()
)
cvSipMsgRateWMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvSipMsgRateWMIndex.setStatus("current")
_CvSipMsgRateWMValue_Type = Unsigned32
_CvSipMsgRateWMValue_Object = MibTableColumn
cvSipMsgRateWMValue = _CvSipMsgRateWMValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9, 1, 3),
    _CvSipMsgRateWMValue_Type()
)
cvSipMsgRateWMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvSipMsgRateWMValue.setStatus("current")
if mibBuilder.loadTexts:
    cvSipMsgRateWMValue.setUnits("SIP messages per second")
_CvSipMsgRateWMts_Type = DateAndTime
_CvSipMsgRateWMts_Object = MibTableColumn
cvSipMsgRateWMts = _CvSipMsgRateWMts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 9, 1, 4),
    _CvSipMsgRateWMts_Type()
)
cvSipMsgRateWMts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvSipMsgRateWMts.setStatus("current")


class _CvCallDurationStatsThreshold_Type(Unsigned32):
    """Custom type cvCallDurationStatsThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CvCallDurationStatsThreshold_Type.__name__ = "Unsigned32"
_CvCallDurationStatsThreshold_Object = MibScalar
cvCallDurationStatsThreshold = _CvCallDurationStatsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 10),
    _CvCallDurationStatsThreshold_Type()
)
cvCallDurationStatsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallDurationStatsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cvCallDurationStatsThreshold.setUnits("seconds")


class _CvCallVolumeWMTableSize_Type(Unsigned32):
    """Custom type cvCallVolumeWMTableSize based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_CvCallVolumeWMTableSize_Type.__name__ = "Unsigned32"
_CvCallVolumeWMTableSize_Object = MibScalar
cvCallVolumeWMTableSize = _CvCallVolumeWMTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 1, 4, 3, 11),
    _CvCallVolumeWMTableSize_Type()
)
cvCallVolumeWMTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCallVolumeWMTableSize.setStatus("current")
_CvdcMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cvdcMIBNotificationPrefix = _CvdcMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2)
)
_CvdcMIBNotifications_ObjectIdentity = ObjectIdentity
cvdcMIBNotifications = _CvdcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0)
)
_CvdcMIBConformance_ObjectIdentity = ObjectIdentity
cvdcMIBConformance = _CvdcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3)
)
_CvdcMIBCompliances_ObjectIdentity = ObjectIdentity
cvdcMIBCompliances = _CvdcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1)
)
_CvdcMIBGroups_ObjectIdentity = ObjectIdentity
cvdcMIBGroups = _CvdcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2)
)
cvPeerCfgEntry.registerAugmentions(
    ("CISCO-VOICE-DIAL-CONTROL-MIB",
     "cvCallVolPeerEntry")
)
cvCallVolPeerEntry.setIndexNames(*cvPeerCfgEntry.getIndexNames())

# Managed Objects groups

cvdcGeneralCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 1)
)
cvdcGeneralCfgGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroup.setStatus("deprecated")

cvdcVoiceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 2)
)
cvdcVoiceCfgGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgDialDigitsPrefix"))
)
if mibBuilder.loadTexts:
    cvdcVoiceCfgGroup.setStatus("deprecated")

cvdcVoIPCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 3)
)
cvdcVoIPCfgGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgExpectFactor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgUDPChecksumEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIPPrecedence"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgGroup.setStatus("deprecated")

cvCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 4)
)
cvCallGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"))
)
if mibBuilder.loadTexts:
    cvCallGroup.setStatus("deprecated")

cvVoIPCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 5)
)
cvVoIPCallGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroup.setStatus("deprecated")

cvdcGeneralCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 6)
)
cvdcGeneralCfgGroupRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev1.setStatus("deprecated")

cvdcVoiceCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 7)
)
cvdcVoiceCfgGroupRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgDialDigitsPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgDIDCallEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgCasGroup"))
)
if mibBuilder.loadTexts:
    cvdcVoiceCfgGroupRev1.setStatus("deprecated")

cvVoIPCallGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 8)
)
cvVoIPCallGroupRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEarlyPackets"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupRev1.setStatus("deprecated")

cvCallGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 9)
)
cvCallGroupRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryImgPageCount"))
)
if mibBuilder.loadTexts:
    cvCallGroupRev1.setStatus("deprecated")

cvdcGeneralCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 10)
)
cvdcGeneralCfgGroupRev2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgPreference"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev2.setStatus("deprecated")

cvdcVoIPCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 11)
)
cvdcVoIPCfgGroupRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgExpectFactor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgUDPChecksumEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIPPrecedence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgTechPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDigitRelay"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgGroupRev1.setStatus("deprecated")

cvdcGeneralCfgGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 12)
)
cvdcGeneralCfgGroupRev3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgPreference"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgHuntStop"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev3.setStatus("deprecated")

cvdcVoiceCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 13)
)
cvdcVoiceCfgGroupRev2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgDialDigitsPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgDIDCallEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgCasGroup"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgRegisterE164"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgForwardDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoicePeerCfgEchoCancellerTest"))
)
if mibBuilder.loadTexts:
    cvdcVoiceCfgGroupRev2.setStatus("current")

cvdcVoIPCfgGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 14)
)
cvdcVoIPCfgGroupRev2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgExpectFactor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgUDPChecksumEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIPPrecedence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgTechPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDigitRelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgInBandSignaling"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgGroupRev2.setStatus("deprecated")

cvVoIPCallGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 15)
)
cvVoIPCallGroupRev3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteIPAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteUDPPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEarlyPackets"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupRev3.setStatus("deprecated")

cvCallGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 17)
)
cvCallGroupRev2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveEcanReflectorLocation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallerIDBlock"))
)
if mibBuilder.loadTexts:
    cvCallGroupRev2.setStatus("deprecated")

cvdcGeneralCfgGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 18)
)
cvdcGeneralCfgGroupRev4.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgPreference"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgHuntStop"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgDnisMappingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceTrunkGrpLabel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetTrunkGrpLabel"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev4.setStatus("deprecated")

cvVoIPCallGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 19)
)
cvVoIPCallGroupRev4.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaPort"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupRev4.setStatus("deprecated")

cvdcVoIPCfgGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 21)
)
cvdcVoIPCfgGroupRev3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgExpectFactor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgUDPChecksumEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIPPrecedence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgTechPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDigitRelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgInBandSignaling"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgGroupRev3.setStatus("deprecated")

cvdcGeneralCfgGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 22)
)
cvdcGeneralCfgGroupRev5.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgPeerType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgPreference"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgHuntStop"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgDnisMappingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceTrunkGrpLabel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetTrunkGrpLabel"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev5.setStatus("deprecated")

cvdcVoIPCfgGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 23)
)
cvdcVoIPCfgGroupRev4.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgVADEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgExpectFactor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgUDPChecksumEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgIPPrecedence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgTechPrefix"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDigitRelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFaxBytes"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgInBandSignaling"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMediaSetting"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDesiredQoSVideo"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMinAcceptableQoSVideo"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgRedirectip2ip"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgDSCPPolicyNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgMediaPolicyNotificationEnable"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgGroupRev4.setStatus("current")

cvCallGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 24)
)
cvCallGroupRev3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveEcanReflectorLocation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevelRev1"))
)
if mibBuilder.loadTexts:
    cvCallGroupRev3.setStatus("deprecated")

cvCallGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 25)
)
cvCallGroupRev4.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveEcanReflectorLocation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevelRev1"))
)
if mibBuilder.loadTexts:
    cvCallGroupRev4.setStatus("deprecated")

cvVoIPCallGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 26)
)
cvVoIPCallGroupRev5.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSRTPEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySRTPEnable"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupRev5.setStatus("deprecated")

cvCallGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 27)
)
cvCallGroupRev5.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0s"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sHighThreshold"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sLowThreshold"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sHighNotifyEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sLowNotifyEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveOutSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveInSignalLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveEcanReflectorLocation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryVoiceTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryFaxTxDuration"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryNoiseLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryACOMLevel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryImgPageCount"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallerIDBlock"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryAccountCode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveERLLevelRev1"))
)
if mibBuilder.loadTexts:
    cvCallGroupRev5.setStatus("current")

cvVoIPCallGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 29)
)
cvVoIPCallGroupRev6.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRemMediaPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSRTPEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRoundTripDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySelectedQoS"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionProtocol"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionTarget"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOnTimeRvPlayout"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithSilence"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithPrediction"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithInterpolation"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryGapFillWithRedundancy"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryHiWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLoWaterPlayoutDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryReceiveDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLostPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryLatePackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEarlyPackets"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryUsername"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryProtocolCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaPort"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySRTPEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackLoss"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackDelay"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupRev6.setStatus("current")

cvdcGeneralCfgGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 30)
)
cvdcGeneralCfgGroupRev6.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralPoorQoVNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralFallbackNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgIfIndex"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgRowStatus"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCfgPeerType"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgIncomingDnisDigits"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgMaxConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgApplicationName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgPreference"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgHuntStop"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgDnisMappingName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetCarrierId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgSourceTrunkGrpLabel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvPeerCommonCfgTargetTrunkGrpLabel"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralDSCPPolicyNotificationEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvGeneralMediaPolicyNotificationEnable"))
)
if mibBuilder.loadTexts:
    cvdcGeneralCfgGroupRev6.setStatus("current")

cvdcVoIPCfgAmrNbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 32)
)
cvdcVoIPCfgAmrNbGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgOctetAligned"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgBitRates"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCRC"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgAmrNbGroup.setStatus("current")

cvVoIPCallAmrNbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 33)
)
cvVoIPCallAmrNbGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveOctetAligned"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveBitRates"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveModeChgPeriod"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveModeChgNeighbor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveMaxPtime"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCRC"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveRobustSorting"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveEncap"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveInterleaving"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActivePtime"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveChannels"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryOctetAligned"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryBitRates"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryModeChgPeriod"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryModeChgNeighbor"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryMaxPtime"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCRC"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRobustSorting"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryEncap"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryInterleaving"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryPtime"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryChannels"))
)
if mibBuilder.loadTexts:
    cvVoIPCallAmrNbGroup.setStatus("current")

cvdcVoIPCfgIlbcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 34)
)
cvdcVoIPCfgIlbcGroup.setObjects(
    ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCoderMode")
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgIlbcGroup.setStatus("current")

cvVoIPCallIlbcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 35)
)
cvVoIPCallIlbcGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCoderMode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCoderMode"))
)
if mibBuilder.loadTexts:
    cvVoIPCallIlbcGroup.setStatus("current")

cvCallGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 36)
)
cvCallGroupSup1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallHistoryCallId"))
)
if mibBuilder.loadTexts:
    cvCallGroupSup1.setStatus("current")

cvVoIPCallGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 37)
)
cvVoIPCallGroupSup1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallReferenceId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallReferenceId"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupSup1.setStatus("deprecated")

cvCallVolumeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 38)
)
cvCallVolumeGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolConnActiveConnection"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolConnTotalActiveConnections"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolConnMaxCallConnectionLicenese"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolPeerIncomingCalls"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolPeerOutgoingCalls"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolMediaIncomingCalls"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolMediaOutgoingCalls"))
)
if mibBuilder.loadTexts:
    cvCallVolumeGroup.setStatus("current")

cvCallRateMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 39)
)
cvCallRateMonitorGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateMonitorEnable"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateMonitorTime"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateHiWaterMark"))
)
if mibBuilder.loadTexts:
    cvCallRateMonitorGroup.setStatus("current")

cvdcVoIPCfgISACGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 40)
)
cvdcVoIPCfgISACGroup.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgCodingMode"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgBitRate"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPPeerCfgFrameSize"))
)
if mibBuilder.loadTexts:
    cvdcVoIPCfgISACGroup.setStatus("current")

cvVoIPCallGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 42)
)
cvVoIPCallGroupSup2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReversedDirectionPeerAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "ccVoIPCallActivePolicyName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallReferenceId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallReferenceId"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupSup2.setStatus("deprecated")

cvVoIPCallGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 43)
)
cvVoIPCallGroupSup3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReversedDirectionPeerAddress"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "ccVoIPCallActivePolicyName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveCallReferenceId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveSessionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryCallReferenceId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistorySessionId"))
)
if mibBuilder.loadTexts:
    cvVoIPCallGroupSup3.setStatus("current")

cvdcCallVolumeStatsHistory = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 44)
)
cvdcCallVolumeStatsHistory.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateStatsMaxVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateStatsAvgVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateStatsMaxVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateStatsAvgVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallStatsMaxVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallStatsAvgVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallDurationStatsMaxVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallDurationStatsAvgVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateStatsMaxVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateStatsAvgVal"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateWMValue"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallRateWMts"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallWMValue"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvActiveCallWMts"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateWMValue"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvSipMsgRateWMts"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallDurationStatsThreshold"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallVolumeWMTableSize"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateWMValue"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallLegRateWMts"))
)
if mibBuilder.loadTexts:
    cvdcCallVolumeStatsHistory.setStatus("current")


# Notification objects

cvdcPoorQoVNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 1)
)
cvdcPoorQoVNotification.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemoteIPAddress"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"))
)
if mibBuilder.loadTexts:
    cvdcPoorQoVNotification.setStatus(
        "deprecated"
    )

cvdcPoorQoVNotificationRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 2)
)
cvdcPoorQoVNotificationRev1.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddr"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"))
)
if mibBuilder.loadTexts:
    cvdcPoorQoVNotificationRev1.setStatus(
        "current"
    )

cvdcActiveDS0sHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 3)
)
cvdcActiveDS0sHighNotification.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0s"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sHighThreshold"))
)
if mibBuilder.loadTexts:
    cvdcActiveDS0sHighNotification.setStatus(
        "current"
    )

cvdcActiveDS0sLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 4)
)
cvdcActiveDS0sLowNotification.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0s"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvCallActiveDS0sLowThreshold"))
)
if mibBuilder.loadTexts:
    cvdcActiveDS0sLowNotification.setStatus(
        "current"
    )

cvdcFallbackNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 5)
)
cvdcFallbackNotification.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryConnectionId"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackIcpif"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackLoss"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryFallbackDelay"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemSigIPAddr"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddrT"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallHistoryRemMediaIPAddr"),
        ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"))
)
if mibBuilder.loadTexts:
    cvdcFallbackNotification.setStatus(
        "current"
    )

cvdcPolicyViolationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 2, 0, 6)
)
cvdcPolicyViolationNotification.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "ccVoIPCallActivePolicyName"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvVoIPCallActiveReversedDirectionPeerAddress"),
        ("DIAL-CONTROL-MIB", "callActivePeerId"),
        ("DIAL-CONTROL-MIB", "callActivePeerAddress"))
)
if mibBuilder.loadTexts:
    cvdcPolicyViolationNotification.setStatus(
        "current"
    )


# Notifications groups

cvdcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 16)
)
cvdcNotificationGroup.setObjects(
    ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPoorQoVNotification")
)
if mibBuilder.loadTexts:
    cvdcNotificationGroup.setStatus(
        "deprecated"
    )

cvdcNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 20)
)
cvdcNotificationGroupRev1.setObjects(
    ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPoorQoVNotificationRev1")
)
if mibBuilder.loadTexts:
    cvdcNotificationGroupRev1.setStatus(
        "deprecated"
    )

cvdcNotificationGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 28)
)
cvdcNotificationGroupRev2.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPoorQoVNotificationRev1"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sHighNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sLowNotification"))
)
if mibBuilder.loadTexts:
    cvdcNotificationGroupRev2.setStatus(
        "deprecated"
    )

cvdcNotificationGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 31)
)
cvdcNotificationGroupRev3.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPoorQoVNotificationRev1"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sHighNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sLowNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcFallbackNotification"))
)
if mibBuilder.loadTexts:
    cvdcNotificationGroupRev3.setStatus(
        "deprecated"
    )

cvdcNotificationGroupRev4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 2, 41)
)
cvdcNotificationGroupRev4.setObjects(
      *(("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPoorQoVNotificationRev1"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sHighNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcActiveDS0sLowNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcFallbackNotification"),
        ("CISCO-VOICE-DIAL-CONTROL-MIB", "cvdcPolicyViolationNotification"))
)
if mibBuilder.loadTexts:
    cvdcNotificationGroupRev4.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvdcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvdcMIBCompliance.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev1.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev2.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev3.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev4.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev5.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev6.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev7.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev8.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev9.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev10.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev11.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev12.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 14)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev13.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 15)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev14.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 16)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev15.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 17)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev16.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 18)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev17.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 19)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev18.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 20)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev19.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 21)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev20.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 22)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev21.setStatus(
        "deprecated"
    )

cvdcMIBComplianceRev22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 63, 3, 1, 23)
)
if mibBuilder.loadTexts:
    cvdcMIBComplianceRev22.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-DIAL-CONTROL-MIB",
    **{"CvCallVolumeWMIntvlType": CvCallVolumeWMIntvlType,
       "CvCallVolumeStatsIntvlType": CvCallVolumeStatsIntvlType,
       "CvSessionProtocol": CvSessionProtocol,
       "CvCasGroup": CvCasGroup,
       "CvAmrNbBitRateMode": CvAmrNbBitRateMode,
       "CvAmrNbRtpEncap": CvAmrNbRtpEncap,
       "CvIlbcFrameMode": CvIlbcFrameMode,
       "CvCallConnectionType": CvCallConnectionType,
       "ciscoVoiceDialControlMIB": ciscoVoiceDialControlMIB,
       "cvdcMIBObjects": cvdcMIBObjects,
       "cvGeneralConfiguration": cvGeneralConfiguration,
       "cvGeneralPoorQoVNotificationEnable": cvGeneralPoorQoVNotificationEnable,
       "cvGeneralFallbackNotificationEnable": cvGeneralFallbackNotificationEnable,
       "cvGeneralDSCPPolicyNotificationEnable": cvGeneralDSCPPolicyNotificationEnable,
       "cvGeneralMediaPolicyNotificationEnable": cvGeneralMediaPolicyNotificationEnable,
       "cvPeer": cvPeer,
       "cvPeerCfgTable": cvPeerCfgTable,
       "cvPeerCfgEntry": cvPeerCfgEntry,
       "cvPeerCfgIndex": cvPeerCfgIndex,
       "cvPeerCfgIfIndex": cvPeerCfgIfIndex,
       "cvPeerCfgType": cvPeerCfgType,
       "cvPeerCfgRowStatus": cvPeerCfgRowStatus,
       "cvPeerCfgPeerType": cvPeerCfgPeerType,
       "cvVoicePeerCfgTable": cvVoicePeerCfgTable,
       "cvVoicePeerCfgEntry": cvVoicePeerCfgEntry,
       "cvVoicePeerCfgSessionTarget": cvVoicePeerCfgSessionTarget,
       "cvVoicePeerCfgDialDigitsPrefix": cvVoicePeerCfgDialDigitsPrefix,
       "cvVoicePeerCfgDIDCallEnable": cvVoicePeerCfgDIDCallEnable,
       "cvVoicePeerCfgCasGroup": cvVoicePeerCfgCasGroup,
       "cvVoicePeerCfgRegisterE164": cvVoicePeerCfgRegisterE164,
       "cvVoicePeerCfgForwardDigits": cvVoicePeerCfgForwardDigits,
       "cvVoicePeerCfgEchoCancellerTest": cvVoicePeerCfgEchoCancellerTest,
       "cvVoIPPeerCfgTable": cvVoIPPeerCfgTable,
       "cvVoIPPeerCfgEntry": cvVoIPPeerCfgEntry,
       "cvVoIPPeerCfgSessionProtocol": cvVoIPPeerCfgSessionProtocol,
       "cvVoIPPeerCfgDesiredQoS": cvVoIPPeerCfgDesiredQoS,
       "cvVoIPPeerCfgMinAcceptableQoS": cvVoIPPeerCfgMinAcceptableQoS,
       "cvVoIPPeerCfgSessionTarget": cvVoIPPeerCfgSessionTarget,
       "cvVoIPPeerCfgCoderRate": cvVoIPPeerCfgCoderRate,
       "cvVoIPPeerCfgFaxRate": cvVoIPPeerCfgFaxRate,
       "cvVoIPPeerCfgVADEnable": cvVoIPPeerCfgVADEnable,
       "cvVoIPPeerCfgExpectFactor": cvVoIPPeerCfgExpectFactor,
       "cvVoIPPeerCfgIcpif": cvVoIPPeerCfgIcpif,
       "cvVoIPPeerCfgPoorQoVNotificationEnable": cvVoIPPeerCfgPoorQoVNotificationEnable,
       "cvVoIPPeerCfgUDPChecksumEnable": cvVoIPPeerCfgUDPChecksumEnable,
       "cvVoIPPeerCfgIPPrecedence": cvVoIPPeerCfgIPPrecedence,
       "cvVoIPPeerCfgTechPrefix": cvVoIPPeerCfgTechPrefix,
       "cvVoIPPeerCfgDigitRelay": cvVoIPPeerCfgDigitRelay,
       "cvVoIPPeerCfgCoderBytes": cvVoIPPeerCfgCoderBytes,
       "cvVoIPPeerCfgFaxBytes": cvVoIPPeerCfgFaxBytes,
       "cvVoIPPeerCfgInBandSignaling": cvVoIPPeerCfgInBandSignaling,
       "cvVoIPPeerCfgMediaSetting": cvVoIPPeerCfgMediaSetting,
       "cvVoIPPeerCfgDesiredQoSVideo": cvVoIPPeerCfgDesiredQoSVideo,
       "cvVoIPPeerCfgMinAcceptableQoSVideo": cvVoIPPeerCfgMinAcceptableQoSVideo,
       "cvVoIPPeerCfgRedirectip2ip": cvVoIPPeerCfgRedirectip2ip,
       "cvVoIPPeerCfgOctetAligned": cvVoIPPeerCfgOctetAligned,
       "cvVoIPPeerCfgBitRates": cvVoIPPeerCfgBitRates,
       "cvVoIPPeerCfgCRC": cvVoIPPeerCfgCRC,
       "cvVoIPPeerCfgCoderMode": cvVoIPPeerCfgCoderMode,
       "cvVoIPPeerCfgCodingMode": cvVoIPPeerCfgCodingMode,
       "cvVoIPPeerCfgBitRate": cvVoIPPeerCfgBitRate,
       "cvVoIPPeerCfgFrameSize": cvVoIPPeerCfgFrameSize,
       "cvVoIPPeerCfgDSCPPolicyNotificationEnable": cvVoIPPeerCfgDSCPPolicyNotificationEnable,
       "cvVoIPPeerCfgMediaPolicyNotificationEnable": cvVoIPPeerCfgMediaPolicyNotificationEnable,
       "cvPeerCommonCfgTable": cvPeerCommonCfgTable,
       "cvPeerCommonCfgEntry": cvPeerCommonCfgEntry,
       "cvPeerCommonCfgIncomingDnisDigits": cvPeerCommonCfgIncomingDnisDigits,
       "cvPeerCommonCfgMaxConnections": cvPeerCommonCfgMaxConnections,
       "cvPeerCommonCfgApplicationName": cvPeerCommonCfgApplicationName,
       "cvPeerCommonCfgPreference": cvPeerCommonCfgPreference,
       "cvPeerCommonCfgHuntStop": cvPeerCommonCfgHuntStop,
       "cvPeerCommonCfgDnisMappingName": cvPeerCommonCfgDnisMappingName,
       "cvPeerCommonCfgSourceCarrierId": cvPeerCommonCfgSourceCarrierId,
       "cvPeerCommonCfgTargetCarrierId": cvPeerCommonCfgTargetCarrierId,
       "cvPeerCommonCfgSourceTrunkGrpLabel": cvPeerCommonCfgSourceTrunkGrpLabel,
       "cvPeerCommonCfgTargetTrunkGrpLabel": cvPeerCommonCfgTargetTrunkGrpLabel,
       "cvGatewayCallActive": cvGatewayCallActive,
       "cvCallActiveTable": cvCallActiveTable,
       "cvCallActiveEntry": cvCallActiveEntry,
       "cvCallActiveConnectionId": cvCallActiveConnectionId,
       "cvCallActiveTxDuration": cvCallActiveTxDuration,
       "cvCallActiveVoiceTxDuration": cvCallActiveVoiceTxDuration,
       "cvCallActiveFaxTxDuration": cvCallActiveFaxTxDuration,
       "cvCallActiveCoderTypeRate": cvCallActiveCoderTypeRate,
       "cvCallActiveNoiseLevel": cvCallActiveNoiseLevel,
       "cvCallActiveACOMLevel": cvCallActiveACOMLevel,
       "cvCallActiveOutSignalLevel": cvCallActiveOutSignalLevel,
       "cvCallActiveInSignalLevel": cvCallActiveInSignalLevel,
       "cvCallActiveERLLevel": cvCallActiveERLLevel,
       "cvCallActiveSessionTarget": cvCallActiveSessionTarget,
       "cvCallActiveImgPageCount": cvCallActiveImgPageCount,
       "cvCallActiveCallingName": cvCallActiveCallingName,
       "cvCallActiveCallerIDBlock": cvCallActiveCallerIDBlock,
       "cvCallActiveEcanReflectorLocation": cvCallActiveEcanReflectorLocation,
       "cvCallActiveAccountCode": cvCallActiveAccountCode,
       "cvCallActiveERLLevelRev1": cvCallActiveERLLevelRev1,
       "cvCallActiveCallId": cvCallActiveCallId,
       "cvVoIPCallActiveTable": cvVoIPCallActiveTable,
       "cvVoIPCallActiveEntry": cvVoIPCallActiveEntry,
       "cvVoIPCallActiveConnectionId": cvVoIPCallActiveConnectionId,
       "cvVoIPCallActiveRemoteIPAddress": cvVoIPCallActiveRemoteIPAddress,
       "cvVoIPCallActiveRemoteUDPPort": cvVoIPCallActiveRemoteUDPPort,
       "cvVoIPCallActiveRoundTripDelay": cvVoIPCallActiveRoundTripDelay,
       "cvVoIPCallActiveSelectedQoS": cvVoIPCallActiveSelectedQoS,
       "cvVoIPCallActiveSessionProtocol": cvVoIPCallActiveSessionProtocol,
       "cvVoIPCallActiveSessionTarget": cvVoIPCallActiveSessionTarget,
       "cvVoIPCallActiveOnTimeRvPlayout": cvVoIPCallActiveOnTimeRvPlayout,
       "cvVoIPCallActiveGapFillWithSilence": cvVoIPCallActiveGapFillWithSilence,
       "cvVoIPCallActiveGapFillWithPrediction": cvVoIPCallActiveGapFillWithPrediction,
       "cvVoIPCallActiveGapFillWithInterpolation": cvVoIPCallActiveGapFillWithInterpolation,
       "cvVoIPCallActiveGapFillWithRedundancy": cvVoIPCallActiveGapFillWithRedundancy,
       "cvVoIPCallActiveHiWaterPlayoutDelay": cvVoIPCallActiveHiWaterPlayoutDelay,
       "cvVoIPCallActiveLoWaterPlayoutDelay": cvVoIPCallActiveLoWaterPlayoutDelay,
       "cvVoIPCallActiveReceiveDelay": cvVoIPCallActiveReceiveDelay,
       "cvVoIPCallActiveVADEnable": cvVoIPCallActiveVADEnable,
       "cvVoIPCallActiveCoderTypeRate": cvVoIPCallActiveCoderTypeRate,
       "cvVoIPCallActiveLostPackets": cvVoIPCallActiveLostPackets,
       "cvVoIPCallActiveEarlyPackets": cvVoIPCallActiveEarlyPackets,
       "cvVoIPCallActiveLatePackets": cvVoIPCallActiveLatePackets,
       "cvVoIPCallActiveUsername": cvVoIPCallActiveUsername,
       "cvVoIPCallActiveProtocolCallId": cvVoIPCallActiveProtocolCallId,
       "cvVoIPCallActiveRemSigIPAddrT": cvVoIPCallActiveRemSigIPAddrT,
       "cvVoIPCallActiveRemSigIPAddr": cvVoIPCallActiveRemSigIPAddr,
       "cvVoIPCallActiveRemSigPort": cvVoIPCallActiveRemSigPort,
       "cvVoIPCallActiveRemMediaIPAddrT": cvVoIPCallActiveRemMediaIPAddrT,
       "cvVoIPCallActiveRemMediaIPAddr": cvVoIPCallActiveRemMediaIPAddr,
       "cvVoIPCallActiveRemMediaPort": cvVoIPCallActiveRemMediaPort,
       "cvVoIPCallActiveSRTPEnable": cvVoIPCallActiveSRTPEnable,
       "cvVoIPCallActiveOctetAligned": cvVoIPCallActiveOctetAligned,
       "cvVoIPCallActiveBitRates": cvVoIPCallActiveBitRates,
       "cvVoIPCallActiveModeChgPeriod": cvVoIPCallActiveModeChgPeriod,
       "cvVoIPCallActiveModeChgNeighbor": cvVoIPCallActiveModeChgNeighbor,
       "cvVoIPCallActiveMaxPtime": cvVoIPCallActiveMaxPtime,
       "cvVoIPCallActiveCRC": cvVoIPCallActiveCRC,
       "cvVoIPCallActiveRobustSorting": cvVoIPCallActiveRobustSorting,
       "cvVoIPCallActiveEncap": cvVoIPCallActiveEncap,
       "cvVoIPCallActiveInterleaving": cvVoIPCallActiveInterleaving,
       "cvVoIPCallActivePtime": cvVoIPCallActivePtime,
       "cvVoIPCallActiveChannels": cvVoIPCallActiveChannels,
       "cvVoIPCallActiveCoderMode": cvVoIPCallActiveCoderMode,
       "cvVoIPCallActiveCallId": cvVoIPCallActiveCallId,
       "cvVoIPCallActiveCallReferenceId": cvVoIPCallActiveCallReferenceId,
       "ccVoIPCallActivePolicyName": ccVoIPCallActivePolicyName,
       "cvVoIPCallActiveReversedDirectionPeerAddress": cvVoIPCallActiveReversedDirectionPeerAddress,
       "cvVoIPCallActiveSessionId": cvVoIPCallActiveSessionId,
       "cvCallActiveDS0s": cvCallActiveDS0s,
       "cvCallActiveDS0sHighThreshold": cvCallActiveDS0sHighThreshold,
       "cvCallActiveDS0sLowThreshold": cvCallActiveDS0sLowThreshold,
       "cvCallActiveDS0sHighNotifyEnable": cvCallActiveDS0sHighNotifyEnable,
       "cvCallActiveDS0sLowNotifyEnable": cvCallActiveDS0sLowNotifyEnable,
       "cvCallVolume": cvCallVolume,
       "cvCallVolConnTable": cvCallVolConnTable,
       "cvCallVolConnEntry": cvCallVolConnEntry,
       "cvCallVolConnIndex": cvCallVolConnIndex,
       "cvCallVolConnActiveConnection": cvCallVolConnActiveConnection,
       "cvCallVolConnTotalActiveConnections": cvCallVolConnTotalActiveConnections,
       "cvCallVolConnMaxCallConnectionLicenese": cvCallVolConnMaxCallConnectionLicenese,
       "cvCallVolPeerTable": cvCallVolPeerTable,
       "cvCallVolPeerEntry": cvCallVolPeerEntry,
       "cvCallVolPeerIncomingCalls": cvCallVolPeerIncomingCalls,
       "cvCallVolPeerOutgoingCalls": cvCallVolPeerOutgoingCalls,
       "cvCallVolIfTable": cvCallVolIfTable,
       "cvCallVolIfEntry": cvCallVolIfEntry,
       "cvCallVolMediaIncomingCalls": cvCallVolMediaIncomingCalls,
       "cvCallVolMediaOutgoingCalls": cvCallVolMediaOutgoingCalls,
       "cvCallRateMonitor": cvCallRateMonitor,
       "cvCallRateMonitorEnable": cvCallRateMonitorEnable,
       "cvCallRateMonitorTime": cvCallRateMonitorTime,
       "cvCallRate": cvCallRate,
       "cvCallRateHiWaterMark": cvCallRateHiWaterMark,
       "cvGatewayCallHistory": cvGatewayCallHistory,
       "cvCallHistoryTable": cvCallHistoryTable,
       "cvCallHistoryEntry": cvCallHistoryEntry,
       "cvCallHistoryConnectionId": cvCallHistoryConnectionId,
       "cvCallHistoryTxDuration": cvCallHistoryTxDuration,
       "cvCallHistoryVoiceTxDuration": cvCallHistoryVoiceTxDuration,
       "cvCallHistoryFaxTxDuration": cvCallHistoryFaxTxDuration,
       "cvCallHistoryCoderTypeRate": cvCallHistoryCoderTypeRate,
       "cvCallHistoryNoiseLevel": cvCallHistoryNoiseLevel,
       "cvCallHistoryACOMLevel": cvCallHistoryACOMLevel,
       "cvCallHistorySessionTarget": cvCallHistorySessionTarget,
       "cvCallHistoryImgPageCount": cvCallHistoryImgPageCount,
       "cvCallHistoryCallingName": cvCallHistoryCallingName,
       "cvCallHistoryCallerIDBlock": cvCallHistoryCallerIDBlock,
       "cvCallHistoryAccountCode": cvCallHistoryAccountCode,
       "cvCallHistoryCallId": cvCallHistoryCallId,
       "cvVoIPCallHistoryTable": cvVoIPCallHistoryTable,
       "cvVoIPCallHistoryEntry": cvVoIPCallHistoryEntry,
       "cvVoIPCallHistoryConnectionId": cvVoIPCallHistoryConnectionId,
       "cvVoIPCallHistoryRemoteIPAddress": cvVoIPCallHistoryRemoteIPAddress,
       "cvVoIPCallHistoryRemoteUDPPort": cvVoIPCallHistoryRemoteUDPPort,
       "cvVoIPCallHistoryRoundTripDelay": cvVoIPCallHistoryRoundTripDelay,
       "cvVoIPCallHistorySelectedQoS": cvVoIPCallHistorySelectedQoS,
       "cvVoIPCallHistorySessionProtocol": cvVoIPCallHistorySessionProtocol,
       "cvVoIPCallHistorySessionTarget": cvVoIPCallHistorySessionTarget,
       "cvVoIPCallHistoryOnTimeRvPlayout": cvVoIPCallHistoryOnTimeRvPlayout,
       "cvVoIPCallHistoryGapFillWithSilence": cvVoIPCallHistoryGapFillWithSilence,
       "cvVoIPCallHistoryGapFillWithPrediction": cvVoIPCallHistoryGapFillWithPrediction,
       "cvVoIPCallHistoryGapFillWithInterpolation": cvVoIPCallHistoryGapFillWithInterpolation,
       "cvVoIPCallHistoryGapFillWithRedundancy": cvVoIPCallHistoryGapFillWithRedundancy,
       "cvVoIPCallHistoryHiWaterPlayoutDelay": cvVoIPCallHistoryHiWaterPlayoutDelay,
       "cvVoIPCallHistoryLoWaterPlayoutDelay": cvVoIPCallHistoryLoWaterPlayoutDelay,
       "cvVoIPCallHistoryReceiveDelay": cvVoIPCallHistoryReceiveDelay,
       "cvVoIPCallHistoryVADEnable": cvVoIPCallHistoryVADEnable,
       "cvVoIPCallHistoryCoderTypeRate": cvVoIPCallHistoryCoderTypeRate,
       "cvVoIPCallHistoryIcpif": cvVoIPCallHistoryIcpif,
       "cvVoIPCallHistoryLostPackets": cvVoIPCallHistoryLostPackets,
       "cvVoIPCallHistoryEarlyPackets": cvVoIPCallHistoryEarlyPackets,
       "cvVoIPCallHistoryLatePackets": cvVoIPCallHistoryLatePackets,
       "cvVoIPCallHistoryUsername": cvVoIPCallHistoryUsername,
       "cvVoIPCallHistoryProtocolCallId": cvVoIPCallHistoryProtocolCallId,
       "cvVoIPCallHistoryRemSigIPAddrT": cvVoIPCallHistoryRemSigIPAddrT,
       "cvVoIPCallHistoryRemSigIPAddr": cvVoIPCallHistoryRemSigIPAddr,
       "cvVoIPCallHistoryRemSigPort": cvVoIPCallHistoryRemSigPort,
       "cvVoIPCallHistoryRemMediaIPAddrT": cvVoIPCallHistoryRemMediaIPAddrT,
       "cvVoIPCallHistoryRemMediaIPAddr": cvVoIPCallHistoryRemMediaIPAddr,
       "cvVoIPCallHistoryRemMediaPort": cvVoIPCallHistoryRemMediaPort,
       "cvVoIPCallHistorySRTPEnable": cvVoIPCallHistorySRTPEnable,
       "cvVoIPCallHistoryFallbackIcpif": cvVoIPCallHistoryFallbackIcpif,
       "cvVoIPCallHistoryFallbackLoss": cvVoIPCallHistoryFallbackLoss,
       "cvVoIPCallHistoryFallbackDelay": cvVoIPCallHistoryFallbackDelay,
       "cvVoIPCallHistoryOctetAligned": cvVoIPCallHistoryOctetAligned,
       "cvVoIPCallHistoryBitRates": cvVoIPCallHistoryBitRates,
       "cvVoIPCallHistoryModeChgPeriod": cvVoIPCallHistoryModeChgPeriod,
       "cvVoIPCallHistoryModeChgNeighbor": cvVoIPCallHistoryModeChgNeighbor,
       "cvVoIPCallHistoryMaxPtime": cvVoIPCallHistoryMaxPtime,
       "cvVoIPCallHistoryCRC": cvVoIPCallHistoryCRC,
       "cvVoIPCallHistoryRobustSorting": cvVoIPCallHistoryRobustSorting,
       "cvVoIPCallHistoryEncap": cvVoIPCallHistoryEncap,
       "cvVoIPCallHistoryInterleaving": cvVoIPCallHistoryInterleaving,
       "cvVoIPCallHistoryPtime": cvVoIPCallHistoryPtime,
       "cvVoIPCallHistoryChannels": cvVoIPCallHistoryChannels,
       "cvVoIPCallHistoryCoderMode": cvVoIPCallHistoryCoderMode,
       "cvVoIPCallHistoryCallId": cvVoIPCallHistoryCallId,
       "cvVoIPCallHistoryCallReferenceId": cvVoIPCallHistoryCallReferenceId,
       "cvVoIPCallHistorySessionId": cvVoIPCallHistorySessionId,
       "cvCallVolumeStatsHistory": cvCallVolumeStatsHistory,
       "cvCallRateStatsTable": cvCallRateStatsTable,
       "cvCallRateStatsEntry": cvCallRateStatsEntry,
       "cvCallRateStatsIntvlDurUnits": cvCallRateStatsIntvlDurUnits,
       "cvCallRateStatsIntvlDur": cvCallRateStatsIntvlDur,
       "cvCallRateStatsMaxVal": cvCallRateStatsMaxVal,
       "cvCallRateStatsAvgVal": cvCallRateStatsAvgVal,
       "cvCallLegRateStatsTable": cvCallLegRateStatsTable,
       "cvCallLegRateStatsEntry": cvCallLegRateStatsEntry,
       "cvCallLegRateStatsIntvlDurUnits": cvCallLegRateStatsIntvlDurUnits,
       "cvCallLegRateStatsIntvlDur": cvCallLegRateStatsIntvlDur,
       "cvCallLegRateStatsMaxVal": cvCallLegRateStatsMaxVal,
       "cvCallLegRateStatsAvgVal": cvCallLegRateStatsAvgVal,
       "cvActiveCallStatsTable": cvActiveCallStatsTable,
       "cvActiveCallStatsEntry": cvActiveCallStatsEntry,
       "cvActiveCallStatsIntvlDurUnits": cvActiveCallStatsIntvlDurUnits,
       "cvActiveCallStatsIntvlDur": cvActiveCallStatsIntvlDur,
       "cvActiveCallStatsMaxVal": cvActiveCallStatsMaxVal,
       "cvActiveCallStatsAvgVal": cvActiveCallStatsAvgVal,
       "cvCallDurationStatsTable": cvCallDurationStatsTable,
       "cvCallDurationStatsEntry": cvCallDurationStatsEntry,
       "cvCallDurationStatsIntvlDurUnits": cvCallDurationStatsIntvlDurUnits,
       "cvCallDurationStatsIntvlDur": cvCallDurationStatsIntvlDur,
       "cvCallDurationStatsMaxVal": cvCallDurationStatsMaxVal,
       "cvCallDurationStatsAvgVal": cvCallDurationStatsAvgVal,
       "cvSipMsgRateStatsTable": cvSipMsgRateStatsTable,
       "cvSipMsgRateStatsEntry": cvSipMsgRateStatsEntry,
       "cvSipMsgRateStatsIntvlDurUnits": cvSipMsgRateStatsIntvlDurUnits,
       "cvSipMsgRateStatsIntvlDur": cvSipMsgRateStatsIntvlDur,
       "cvSipMsgRateStatsMaxVal": cvSipMsgRateStatsMaxVal,
       "cvSipMsgRateStatsAvgVal": cvSipMsgRateStatsAvgVal,
       "cvCallRateWMTable": cvCallRateWMTable,
       "cvCallRateWMEntry": cvCallRateWMEntry,
       "cvCallRateWMIntvlDurUnits": cvCallRateWMIntvlDurUnits,
       "cvCallRateWMIndex": cvCallRateWMIndex,
       "cvCallRateWMValue": cvCallRateWMValue,
       "cvCallRateWMts": cvCallRateWMts,
       "cvCallLegRateWMTable": cvCallLegRateWMTable,
       "cvCallLegRateWMEntry": cvCallLegRateWMEntry,
       "cvCallLegRateWMIntvlDurUnits": cvCallLegRateWMIntvlDurUnits,
       "cvCallLegRateWMIndex": cvCallLegRateWMIndex,
       "cvCallLegRateWMValue": cvCallLegRateWMValue,
       "cvCallLegRateWMts": cvCallLegRateWMts,
       "cvActiveCallWMTable": cvActiveCallWMTable,
       "cvActiveCallWMEntry": cvActiveCallWMEntry,
       "cvActiveCallWMIntvlDurUnits": cvActiveCallWMIntvlDurUnits,
       "cvActiveCallWMIndex": cvActiveCallWMIndex,
       "cvActiveCallWMValue": cvActiveCallWMValue,
       "cvActiveCallWMts": cvActiveCallWMts,
       "cvSipMsgRateWMTable": cvSipMsgRateWMTable,
       "cvSipMsgRateWMEntry": cvSipMsgRateWMEntry,
       "cvSipMsgRateWMIntvlDurUnits": cvSipMsgRateWMIntvlDurUnits,
       "cvSipMsgRateWMIndex": cvSipMsgRateWMIndex,
       "cvSipMsgRateWMValue": cvSipMsgRateWMValue,
       "cvSipMsgRateWMts": cvSipMsgRateWMts,
       "cvCallDurationStatsThreshold": cvCallDurationStatsThreshold,
       "cvCallVolumeWMTableSize": cvCallVolumeWMTableSize,
       "cvdcMIBNotificationPrefix": cvdcMIBNotificationPrefix,
       "cvdcMIBNotifications": cvdcMIBNotifications,
       "cvdcPoorQoVNotification": cvdcPoorQoVNotification,
       "cvdcPoorQoVNotificationRev1": cvdcPoorQoVNotificationRev1,
       "cvdcActiveDS0sHighNotification": cvdcActiveDS0sHighNotification,
       "cvdcActiveDS0sLowNotification": cvdcActiveDS0sLowNotification,
       "cvdcFallbackNotification": cvdcFallbackNotification,
       "cvdcPolicyViolationNotification": cvdcPolicyViolationNotification,
       "cvdcMIBConformance": cvdcMIBConformance,
       "cvdcMIBCompliances": cvdcMIBCompliances,
       "cvdcMIBCompliance": cvdcMIBCompliance,
       "cvdcMIBComplianceRev1": cvdcMIBComplianceRev1,
       "cvdcMIBComplianceRev2": cvdcMIBComplianceRev2,
       "cvdcMIBComplianceRev3": cvdcMIBComplianceRev3,
       "cvdcMIBComplianceRev4": cvdcMIBComplianceRev4,
       "cvdcMIBComplianceRev5": cvdcMIBComplianceRev5,
       "cvdcMIBComplianceRev6": cvdcMIBComplianceRev6,
       "cvdcMIBComplianceRev7": cvdcMIBComplianceRev7,
       "cvdcMIBComplianceRev8": cvdcMIBComplianceRev8,
       "cvdcMIBComplianceRev9": cvdcMIBComplianceRev9,
       "cvdcMIBComplianceRev10": cvdcMIBComplianceRev10,
       "cvdcMIBComplianceRev11": cvdcMIBComplianceRev11,
       "cvdcMIBComplianceRev12": cvdcMIBComplianceRev12,
       "cvdcMIBComplianceRev13": cvdcMIBComplianceRev13,
       "cvdcMIBComplianceRev14": cvdcMIBComplianceRev14,
       "cvdcMIBComplianceRev15": cvdcMIBComplianceRev15,
       "cvdcMIBComplianceRev16": cvdcMIBComplianceRev16,
       "cvdcMIBComplianceRev17": cvdcMIBComplianceRev17,
       "cvdcMIBComplianceRev18": cvdcMIBComplianceRev18,
       "cvdcMIBComplianceRev19": cvdcMIBComplianceRev19,
       "cvdcMIBComplianceRev20": cvdcMIBComplianceRev20,
       "cvdcMIBComplianceRev21": cvdcMIBComplianceRev21,
       "cvdcMIBComplianceRev22": cvdcMIBComplianceRev22,
       "cvdcMIBGroups": cvdcMIBGroups,
       "cvdcGeneralCfgGroup": cvdcGeneralCfgGroup,
       "cvdcVoiceCfgGroup": cvdcVoiceCfgGroup,
       "cvdcVoIPCfgGroup": cvdcVoIPCfgGroup,
       "cvCallGroup": cvCallGroup,
       "cvVoIPCallGroup": cvVoIPCallGroup,
       "cvdcGeneralCfgGroupRev1": cvdcGeneralCfgGroupRev1,
       "cvdcVoiceCfgGroupRev1": cvdcVoiceCfgGroupRev1,
       "cvVoIPCallGroupRev1": cvVoIPCallGroupRev1,
       "cvCallGroupRev1": cvCallGroupRev1,
       "cvdcGeneralCfgGroupRev2": cvdcGeneralCfgGroupRev2,
       "cvdcVoIPCfgGroupRev1": cvdcVoIPCfgGroupRev1,
       "cvdcGeneralCfgGroupRev3": cvdcGeneralCfgGroupRev3,
       "cvdcVoiceCfgGroupRev2": cvdcVoiceCfgGroupRev2,
       "cvdcVoIPCfgGroupRev2": cvdcVoIPCfgGroupRev2,
       "cvVoIPCallGroupRev3": cvVoIPCallGroupRev3,
       "cvdcNotificationGroup": cvdcNotificationGroup,
       "cvCallGroupRev2": cvCallGroupRev2,
       "cvdcGeneralCfgGroupRev4": cvdcGeneralCfgGroupRev4,
       "cvVoIPCallGroupRev4": cvVoIPCallGroupRev4,
       "cvdcNotificationGroupRev1": cvdcNotificationGroupRev1,
       "cvdcVoIPCfgGroupRev3": cvdcVoIPCfgGroupRev3,
       "cvdcGeneralCfgGroupRev5": cvdcGeneralCfgGroupRev5,
       "cvdcVoIPCfgGroupRev4": cvdcVoIPCfgGroupRev4,
       "cvCallGroupRev3": cvCallGroupRev3,
       "cvCallGroupRev4": cvCallGroupRev4,
       "cvVoIPCallGroupRev5": cvVoIPCallGroupRev5,
       "cvCallGroupRev5": cvCallGroupRev5,
       "cvdcNotificationGroupRev2": cvdcNotificationGroupRev2,
       "cvVoIPCallGroupRev6": cvVoIPCallGroupRev6,
       "cvdcGeneralCfgGroupRev6": cvdcGeneralCfgGroupRev6,
       "cvdcNotificationGroupRev3": cvdcNotificationGroupRev3,
       "cvdcVoIPCfgAmrNbGroup": cvdcVoIPCfgAmrNbGroup,
       "cvVoIPCallAmrNbGroup": cvVoIPCallAmrNbGroup,
       "cvdcVoIPCfgIlbcGroup": cvdcVoIPCfgIlbcGroup,
       "cvVoIPCallIlbcGroup": cvVoIPCallIlbcGroup,
       "cvCallGroupSup1": cvCallGroupSup1,
       "cvVoIPCallGroupSup1": cvVoIPCallGroupSup1,
       "cvCallVolumeGroup": cvCallVolumeGroup,
       "cvCallRateMonitorGroup": cvCallRateMonitorGroup,
       "cvdcVoIPCfgISACGroup": cvdcVoIPCfgISACGroup,
       "cvdcNotificationGroupRev4": cvdcNotificationGroupRev4,
       "cvVoIPCallGroupSup2": cvVoIPCallGroupSup2,
       "cvVoIPCallGroupSup3": cvVoIPCallGroupSup3,
       "cvdcCallVolumeStatsHistory": cvdcCallVolumeStatsHistory}
)
