# SNMP MIB module (HUAWEI-VO-CALL-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-CALL-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:28 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hwVoiceCallHistoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7)
)
hwVoiceCallHistoryMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoCallHistoryObjects_ObjectIdentity = ObjectIdentity
hwVoCallHistoryObjects = _HwVoCallHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1)
)


class _HwVoCallHistoryMaxLen_Type(Integer32):
    """Custom type hwVoCallHistoryMaxLen based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_HwVoCallHistoryMaxLen_Type.__name__ = "Integer32"
_HwVoCallHistoryMaxLen_Object = MibScalar
hwVoCallHistoryMaxLen = _HwVoCallHistoryMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 1),
    _HwVoCallHistoryMaxLen_Type()
)
hwVoCallHistoryMaxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoCallHistoryMaxLen.setStatus("current")
_HwVoCallHistoryGenericTable_Object = MibTable
hwVoCallHistoryGenericTable = _HwVoCallHistoryGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericTable.setStatus("current")
_HwVoCallHistoryGenericEntry_Object = MibTableRow
hwVoCallHistoryGenericEntry = _HwVoCallHistoryGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1)
)
hwVoCallHistoryGenericEntry.setIndexNames(
    (0, "HUAWEI-VO-CALL-HISTORY-MIB", "hwVoCallHistoryGenericIndex"),
)
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericEntry.setStatus("current")


class _HwVoCallHistoryGenericIndex_Type(Integer32):
    """Custom type hwVoCallHistoryGenericIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoCallHistoryGenericIndex_Type.__name__ = "Integer32"
_HwVoCallHistoryGenericIndex_Object = MibTableColumn
hwVoCallHistoryGenericIndex = _HwVoCallHistoryGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 1),
    _HwVoCallHistoryGenericIndex_Type()
)
hwVoCallHistoryGenericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericIndex.setStatus("current")


class _HwVoCallHistoryGenericCallerNumber_Type(OctetString):
    """Custom type hwVoCallHistoryGenericCallerNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoCallHistoryGenericCallerNumber_Type.__name__ = "OctetString"
_HwVoCallHistoryGenericCallerNumber_Object = MibTableColumn
hwVoCallHistoryGenericCallerNumber = _HwVoCallHistoryGenericCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 2),
    _HwVoCallHistoryGenericCallerNumber_Type()
)
hwVoCallHistoryGenericCallerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericCallerNumber.setStatus("current")


class _HwVoCallHistoryGenericCalledNumber_Type(OctetString):
    """Custom type hwVoCallHistoryGenericCalledNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoCallHistoryGenericCalledNumber_Type.__name__ = "OctetString"
_HwVoCallHistoryGenericCalledNumber_Object = MibTableColumn
hwVoCallHistoryGenericCalledNumber = _HwVoCallHistoryGenericCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 3),
    _HwVoCallHistoryGenericCalledNumber_Type()
)
hwVoCallHistoryGenericCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericCalledNumber.setStatus("current")


class _HwVoCallHistoryGenericEncodeType_Type(Integer32):
    """Custom type hwVoCallHistoryGenericEncodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711u", 2),
          ("g723", 3),
          ("g729", 4),
          ("g729a", 5),
          ("unknown", 0))
    )


_HwVoCallHistoryGenericEncodeType_Type.__name__ = "Integer32"
_HwVoCallHistoryGenericEncodeType_Object = MibTableColumn
hwVoCallHistoryGenericEncodeType = _HwVoCallHistoryGenericEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 4),
    _HwVoCallHistoryGenericEncodeType_Type()
)
hwVoCallHistoryGenericEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericEncodeType.setStatus("current")
_HwVoCallHistoryGenericChannel_Type = Integer32
_HwVoCallHistoryGenericChannel_Object = MibTableColumn
hwVoCallHistoryGenericChannel = _HwVoCallHistoryGenericChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 5),
    _HwVoCallHistoryGenericChannel_Type()
)
hwVoCallHistoryGenericChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericChannel.setStatus("current")
_HwVoCallHistoryGenericLocalAddress_Type = IpAddress
_HwVoCallHistoryGenericLocalAddress_Object = MibTableColumn
hwVoCallHistoryGenericLocalAddress = _HwVoCallHistoryGenericLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 6),
    _HwVoCallHistoryGenericLocalAddress_Type()
)
hwVoCallHistoryGenericLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericLocalAddress.setStatus("current")
_HwVoCallHistoryGenericPeerAddress_Type = IpAddress
_HwVoCallHistoryGenericPeerAddress_Object = MibTableColumn
hwVoCallHistoryGenericPeerAddress = _HwVoCallHistoryGenericPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 7),
    _HwVoCallHistoryGenericPeerAddress_Type()
)
hwVoCallHistoryGenericPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericPeerAddress.setStatus("current")


class _HwVoCallHistoryGenericDisconnectText_Type(Integer32):
    """Custom type hwVoCallHistoryGenericDisconnectText based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("calledHookOn", 14),
          ("calledLimit", 10),
          ("callerHookOn", 13),
          ("cardNumberNotExist", 2),
          ("creditLimit", 7),
          ("invalidParameter", 12),
          ("invalidPassword", 3),
          ("maxRedialTimesLimit", 11),
          ("networkProblem", 15),
          ("noEnoughBalance", 5),
          ("normalRelease", 1),
          ("serviceInvalid", 9),
          ("theAccountsIsExpired", 6),
          ("thisAccountsIsUsing", 4),
          ("unknownReason", 16),
          ("userReject", 8))
    )


_HwVoCallHistoryGenericDisconnectText_Type.__name__ = "Integer32"
_HwVoCallHistoryGenericDisconnectText_Object = MibTableColumn
hwVoCallHistoryGenericDisconnectText = _HwVoCallHistoryGenericDisconnectText_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 8),
    _HwVoCallHistoryGenericDisconnectText_Type()
)
hwVoCallHistoryGenericDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericDisconnectText.setStatus("current")
_HwVoCallHistoryGenericCallDuration_Type = TimeTicks
_HwVoCallHistoryGenericCallDuration_Object = MibTableColumn
hwVoCallHistoryGenericCallDuration = _HwVoCallHistoryGenericCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 9),
    _HwVoCallHistoryGenericCallDuration_Type()
)
hwVoCallHistoryGenericCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericCallDuration.setStatus("current")
_HwVoCallHistoryGenericVoiceCallDuration_Type = TimeTicks
_HwVoCallHistoryGenericVoiceCallDuration_Object = MibTableColumn
hwVoCallHistoryGenericVoiceCallDuration = _HwVoCallHistoryGenericVoiceCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 10),
    _HwVoCallHistoryGenericVoiceCallDuration_Type()
)
hwVoCallHistoryGenericVoiceCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericVoiceCallDuration.setStatus("current")
_HwVoCallHistoryGenericFaxCallDuration_Type = TimeTicks
_HwVoCallHistoryGenericFaxCallDuration_Object = MibTableColumn
hwVoCallHistoryGenericFaxCallDuration = _HwVoCallHistoryGenericFaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 11),
    _HwVoCallHistoryGenericFaxCallDuration_Type()
)
hwVoCallHistoryGenericFaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericFaxCallDuration.setStatus("current")
_HwVoCallHistoryGenericImgPages_Type = Integer32
_HwVoCallHistoryGenericImgPages_Object = MibTableColumn
hwVoCallHistoryGenericImgPages = _HwVoCallHistoryGenericImgPages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 12),
    _HwVoCallHistoryGenericImgPages_Type()
)
hwVoCallHistoryGenericImgPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericImgPages.setStatus("current")


class _HwVoCallHistoryGenericCallOrigin_Type(Integer32):
    """Custom type hwVoCallHistoryGenericCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("caller", 1))
    )


_HwVoCallHistoryGenericCallOrigin_Type.__name__ = "Integer32"
_HwVoCallHistoryGenericCallOrigin_Object = MibTableColumn
hwVoCallHistoryGenericCallOrigin = _HwVoCallHistoryGenericCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 2, 1, 13),
    _HwVoCallHistoryGenericCallOrigin_Type()
)
hwVoCallHistoryGenericCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryGenericCallOrigin.setStatus("current")
_HwVoCallHistoryVoIPTable_Object = MibTable
hwVoCallHistoryVoIPTable = _HwVoCallHistoryVoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPTable.setStatus("current")
_HwVoCallHistoryVoIPEntry_Object = MibTableRow
hwVoCallHistoryVoIPEntry = _HwVoCallHistoryVoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1)
)
hwVoCallHistoryVoIPEntry.setIndexNames(
    (0, "HUAWEI-VO-CALL-HISTORY-MIB", "hwVoCallHistoryVoIPIndex"),
)
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPEntry.setStatus("current")


class _HwVoCallHistoryVoIPIndex_Type(Integer32):
    """Custom type hwVoCallHistoryVoIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoCallHistoryVoIPIndex_Type.__name__ = "Integer32"
_HwVoCallHistoryVoIPIndex_Object = MibTableColumn
hwVoCallHistoryVoIPIndex = _HwVoCallHistoryVoIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 1),
    _HwVoCallHistoryVoIPIndex_Type()
)
hwVoCallHistoryVoIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPIndex.setStatus("current")
_HwVoCallHistoryVoIPSetupTime_Type = DateAndTime
_HwVoCallHistoryVoIPSetupTime_Object = MibTableColumn
hwVoCallHistoryVoIPSetupTime = _HwVoCallHistoryVoIPSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 2),
    _HwVoCallHistoryVoIPSetupTime_Type()
)
hwVoCallHistoryVoIPSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPSetupTime.setStatus("current")
_HwVoCallHistoryVoIPConnectTime_Type = DateAndTime
_HwVoCallHistoryVoIPConnectTime_Object = MibTableColumn
hwVoCallHistoryVoIPConnectTime = _HwVoCallHistoryVoIPConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 3),
    _HwVoCallHistoryVoIPConnectTime_Type()
)
hwVoCallHistoryVoIPConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPConnectTime.setStatus("current")
_HwVoCallHistoryVoIPDisconectTime_Type = DateAndTime
_HwVoCallHistoryVoIPDisconectTime_Object = MibTableColumn
hwVoCallHistoryVoIPDisconectTime = _HwVoCallHistoryVoIPDisconectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 4),
    _HwVoCallHistoryVoIPDisconectTime_Type()
)
hwVoCallHistoryVoIPDisconectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPDisconectTime.setStatus("current")
_HwVoCallHistoryVoIPSendPackets_Type = Integer32
_HwVoCallHistoryVoIPSendPackets_Object = MibTableColumn
hwVoCallHistoryVoIPSendPackets = _HwVoCallHistoryVoIPSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 5),
    _HwVoCallHistoryVoIPSendPackets_Type()
)
hwVoCallHistoryVoIPSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPSendPackets.setStatus("current")
_HwVoCallHistoryVoIPSendBytes_Type = Integer32
_HwVoCallHistoryVoIPSendBytes_Object = MibTableColumn
hwVoCallHistoryVoIPSendBytes = _HwVoCallHistoryVoIPSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 6),
    _HwVoCallHistoryVoIPSendBytes_Type()
)
hwVoCallHistoryVoIPSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPSendBytes.setStatus("current")
_HwVoCallHistoryVoIPReceivePackets_Type = Integer32
_HwVoCallHistoryVoIPReceivePackets_Object = MibTableColumn
hwVoCallHistoryVoIPReceivePackets = _HwVoCallHistoryVoIPReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 7),
    _HwVoCallHistoryVoIPReceivePackets_Type()
)
hwVoCallHistoryVoIPReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPReceivePackets.setStatus("current")
_HwVoCallHistoryVoIPReceiveBytes_Type = Integer32
_HwVoCallHistoryVoIPReceiveBytes_Object = MibTableColumn
hwVoCallHistoryVoIPReceiveBytes = _HwVoCallHistoryVoIPReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 3, 1, 8),
    _HwVoCallHistoryVoIPReceiveBytes_Type()
)
hwVoCallHistoryVoIPReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryVoIPReceiveBytes.setStatus("current")
_HwVoCallHistoryPSTNTable_Object = MibTable
hwVoCallHistoryPSTNTable = _HwVoCallHistoryPSTNTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNTable.setStatus("current")
_HwVoCallHistoryPSTNEntry_Object = MibTableRow
hwVoCallHistoryPSTNEntry = _HwVoCallHistoryPSTNEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1)
)
hwVoCallHistoryPSTNEntry.setIndexNames(
    (0, "HUAWEI-VO-CALL-HISTORY-MIB", "hwVoCallHistoryPSTNIndex"),
)
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNEntry.setStatus("current")


class _HwVoCallHistoryPSTNIndex_Type(Integer32):
    """Custom type hwVoCallHistoryPSTNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoCallHistoryPSTNIndex_Type.__name__ = "Integer32"
_HwVoCallHistoryPSTNIndex_Object = MibTableColumn
hwVoCallHistoryPSTNIndex = _HwVoCallHistoryPSTNIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 1),
    _HwVoCallHistoryPSTNIndex_Type()
)
hwVoCallHistoryPSTNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNIndex.setStatus("current")
_HwVoCallHistoryPSTNSetupTime_Type = DateAndTime
_HwVoCallHistoryPSTNSetupTime_Object = MibTableColumn
hwVoCallHistoryPSTNSetupTime = _HwVoCallHistoryPSTNSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 2),
    _HwVoCallHistoryPSTNSetupTime_Type()
)
hwVoCallHistoryPSTNSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNSetupTime.setStatus("current")
_HwVoCallHistoryPSTNConnectTime_Type = DateAndTime
_HwVoCallHistoryPSTNConnectTime_Object = MibTableColumn
hwVoCallHistoryPSTNConnectTime = _HwVoCallHistoryPSTNConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 3),
    _HwVoCallHistoryPSTNConnectTime_Type()
)
hwVoCallHistoryPSTNConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNConnectTime.setStatus("current")
_HwVoCallHistoryPSTNDisconectTime_Type = DateAndTime
_HwVoCallHistoryPSTNDisconectTime_Object = MibTableColumn
hwVoCallHistoryPSTNDisconectTime = _HwVoCallHistoryPSTNDisconectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 4),
    _HwVoCallHistoryPSTNDisconectTime_Type()
)
hwVoCallHistoryPSTNDisconectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNDisconectTime.setStatus("current")
_HwVoCallHistoryPSTNSendPackets_Type = Integer32
_HwVoCallHistoryPSTNSendPackets_Object = MibTableColumn
hwVoCallHistoryPSTNSendPackets = _HwVoCallHistoryPSTNSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 5),
    _HwVoCallHistoryPSTNSendPackets_Type()
)
hwVoCallHistoryPSTNSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNSendPackets.setStatus("current")
_HwVoCallHistoryPSTNSendBytes_Type = Integer32
_HwVoCallHistoryPSTNSendBytes_Object = MibTableColumn
hwVoCallHistoryPSTNSendBytes = _HwVoCallHistoryPSTNSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 6),
    _HwVoCallHistoryPSTNSendBytes_Type()
)
hwVoCallHistoryPSTNSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNSendBytes.setStatus("current")
_HwVoCallHistoryPSTNReceivePackets_Type = Integer32
_HwVoCallHistoryPSTNReceivePackets_Object = MibTableColumn
hwVoCallHistoryPSTNReceivePackets = _HwVoCallHistoryPSTNReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 7),
    _HwVoCallHistoryPSTNReceivePackets_Type()
)
hwVoCallHistoryPSTNReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNReceivePackets.setStatus("current")
_HwVoCallHistoryPSTNReceiveBytes_Type = Integer32
_HwVoCallHistoryPSTNReceiveBytes_Object = MibTableColumn
hwVoCallHistoryPSTNReceiveBytes = _HwVoCallHistoryPSTNReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 4, 1, 8),
    _HwVoCallHistoryPSTNReceiveBytes_Type()
)
hwVoCallHistoryPSTNReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoCallHistoryPSTNReceiveBytes.setStatus("current")


class _HwVoCallHistoryMaxRetainTime_Type(Integer32):
    """Custom type hwVoCallHistoryMaxRetainTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoCallHistoryMaxRetainTime_Type.__name__ = "Integer32"
_HwVoCallHistoryMaxRetainTime_Object = MibScalar
hwVoCallHistoryMaxRetainTime = _HwVoCallHistoryMaxRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 7, 1, 5),
    _HwVoCallHistoryMaxRetainTime_Type()
)
hwVoCallHistoryMaxRetainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoCallHistoryMaxRetainTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-CALL-HISTORY-MIB",
    **{"hwVoiceCallHistoryMIB": hwVoiceCallHistoryMIB,
       "hwVoCallHistoryObjects": hwVoCallHistoryObjects,
       "hwVoCallHistoryMaxLen": hwVoCallHistoryMaxLen,
       "hwVoCallHistoryGenericTable": hwVoCallHistoryGenericTable,
       "hwVoCallHistoryGenericEntry": hwVoCallHistoryGenericEntry,
       "hwVoCallHistoryGenericIndex": hwVoCallHistoryGenericIndex,
       "hwVoCallHistoryGenericCallerNumber": hwVoCallHistoryGenericCallerNumber,
       "hwVoCallHistoryGenericCalledNumber": hwVoCallHistoryGenericCalledNumber,
       "hwVoCallHistoryGenericEncodeType": hwVoCallHistoryGenericEncodeType,
       "hwVoCallHistoryGenericChannel": hwVoCallHistoryGenericChannel,
       "hwVoCallHistoryGenericLocalAddress": hwVoCallHistoryGenericLocalAddress,
       "hwVoCallHistoryGenericPeerAddress": hwVoCallHistoryGenericPeerAddress,
       "hwVoCallHistoryGenericDisconnectText": hwVoCallHistoryGenericDisconnectText,
       "hwVoCallHistoryGenericCallDuration": hwVoCallHistoryGenericCallDuration,
       "hwVoCallHistoryGenericVoiceCallDuration": hwVoCallHistoryGenericVoiceCallDuration,
       "hwVoCallHistoryGenericFaxCallDuration": hwVoCallHistoryGenericFaxCallDuration,
       "hwVoCallHistoryGenericImgPages": hwVoCallHistoryGenericImgPages,
       "hwVoCallHistoryGenericCallOrigin": hwVoCallHistoryGenericCallOrigin,
       "hwVoCallHistoryVoIPTable": hwVoCallHistoryVoIPTable,
       "hwVoCallHistoryVoIPEntry": hwVoCallHistoryVoIPEntry,
       "hwVoCallHistoryVoIPIndex": hwVoCallHistoryVoIPIndex,
       "hwVoCallHistoryVoIPSetupTime": hwVoCallHistoryVoIPSetupTime,
       "hwVoCallHistoryVoIPConnectTime": hwVoCallHistoryVoIPConnectTime,
       "hwVoCallHistoryVoIPDisconectTime": hwVoCallHistoryVoIPDisconectTime,
       "hwVoCallHistoryVoIPSendPackets": hwVoCallHistoryVoIPSendPackets,
       "hwVoCallHistoryVoIPSendBytes": hwVoCallHistoryVoIPSendBytes,
       "hwVoCallHistoryVoIPReceivePackets": hwVoCallHistoryVoIPReceivePackets,
       "hwVoCallHistoryVoIPReceiveBytes": hwVoCallHistoryVoIPReceiveBytes,
       "hwVoCallHistoryPSTNTable": hwVoCallHistoryPSTNTable,
       "hwVoCallHistoryPSTNEntry": hwVoCallHistoryPSTNEntry,
       "hwVoCallHistoryPSTNIndex": hwVoCallHistoryPSTNIndex,
       "hwVoCallHistoryPSTNSetupTime": hwVoCallHistoryPSTNSetupTime,
       "hwVoCallHistoryPSTNConnectTime": hwVoCallHistoryPSTNConnectTime,
       "hwVoCallHistoryPSTNDisconectTime": hwVoCallHistoryPSTNDisconectTime,
       "hwVoCallHistoryPSTNSendPackets": hwVoCallHistoryPSTNSendPackets,
       "hwVoCallHistoryPSTNSendBytes": hwVoCallHistoryPSTNSendBytes,
       "hwVoCallHistoryPSTNReceivePackets": hwVoCallHistoryPSTNReceivePackets,
       "hwVoCallHistoryPSTNReceiveBytes": hwVoCallHistoryPSTNReceiveBytes,
       "hwVoCallHistoryMaxRetainTime": hwVoCallHistoryMaxRetainTime}
)
