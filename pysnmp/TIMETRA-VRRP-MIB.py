# SNMP MIB module (TIMETRA-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:11 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ipv6RouterAdvertEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipv6RouterAdvertEntry")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(LAGInterfaceNumber,) = mibBuilder.importSymbols(
    "TIMETRA-LAG-MIB",
    "LAGInterfaceNumber")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxPortID",
    "TmnxServId")

(vrrpNewMasterReason,
 vrrpOperationsEntry,
 vrrpOperationsMasterIpAddr,
 vrrpOperationsVrId,
 vrrpRouterStatisticsEntry) = mibBuilder.importSymbols(
    "TIMETRA-VRRP-V3-MIB",
    "vrrpNewMasterReason",
    "vrrpOperationsEntry",
    "vrrpOperationsMasterIpAddr",
    "vrrpOperationsVrId",
    "vrrpRouterStatisticsEntry")

(vrrpOperEntry,
 vrrpOperMasterIpAddr,
 vrrpOperVrId,
 vrrpRouterStatsEntry) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperEntry",
    "vrrpOperMasterIpAddr",
    "vrrpOperVrId",
    "vrrpRouterStatsEntry")


# MODULE-IDENTITY

timetraVrrpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 20)
)
timetraVrrpMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1907-01-01 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "2003-01-20 00:00",
         "2002-05-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxVrrpPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )



class TmnxVrrpPriority(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class TmnxEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delta", 1),
          ("explicit", 2))
    )



class TmnxEventHoldSet(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class TmnxEventHoldClear(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class TmnxPortDownEventOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("setDown", 3),
          ("setNotPopulated", 2),
          ("setNotProvisioned", 1))
    )



class TmnxLagPortDownEventOperState(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 0),
          ("setEightPortDown", 9),
          ("setElevenPortDown", 12),
          ("setFifteenPortDown", 16),
          ("setFivePortDown", 6),
          ("setFourPortDown", 5),
          ("setFourteenPortDown", 15),
          ("setNinePortDown", 10),
          ("setNonExistant", 1),
          ("setOnePortDown", 2),
          ("setSevenPortDown", 8),
          ("setSixPortDown", 7),
          ("setSixteenPortDown", 17),
          ("setTenPortDown", 11),
          ("setThirteenPortDown", 14),
          ("setThreePortDown", 4),
          ("setTwelvePortDown", 13),
          ("setTwoPortDown", 3))
    )



class TmnxHostUnreachableEventOperState(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("clearedHostUnreachable", 2),
          ("clearedNoArp", 0),
          ("clearedNoReply", 3),
          ("clearedNoRoute", 1),
          ("clearedReplyReceived", 4),
          ("setHostUnreachable", 7),
          ("setNoArp", 5),
          ("setNoReply", 8),
          ("setNoRoute", 6),
          ("setReplyReceived", 9))
    )



class TmnxRouteUnknownEventOperState(Integer32, TextualConvention):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clearedFound", 1),
          ("clearedLessSpecificFound", 0),
          ("setDefaultBestMatch", 7),
          ("setInActive", 3),
          ("setLessSpecificFound", 6),
          ("setNonExistent", 2),
          ("setWrongNextHop", 4),
          ("setWrongProtocol", 5))
    )



class TmnxVrrpAssoBfdIntfSessOperState(Integer32, TextualConvention):
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
        *(("broken", 3),
          ("connected", 2),
          ("noResources", 6),
          ("notConfigured", 5),
          ("peerDetectsDown", 4),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxVrrpConformance_ObjectIdentity = ObjectIdentity
tmnxVrrpConformance = _TmnxVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20)
)
_TmnxVrrpCompliances_ObjectIdentity = ObjectIdentity
tmnxVrrpCompliances = _TmnxVrrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1)
)
_TmnxVrrpGroups_ObjectIdentity = ObjectIdentity
tmnxVrrpGroups = _TmnxVrrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2)
)
_TmnxVrrpMibObjects_ObjectIdentity = ObjectIdentity
tmnxVrrpMibObjects = _TmnxVrrpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20)
)
_TmnxVrrpObjects_ObjectIdentity = ObjectIdentity
tmnxVrrpObjects = _TmnxVrrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1)
)
_TmnxVrrpOperTable_Object = MibTable
tmnxVrrpOperTable = _TmnxVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxVrrpOperTable.setStatus("current")
_TmnxVrrpOperEntry_Object = MibTableRow
tmnxVrrpOperEntry = _TmnxVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxVrrpOperEntry.setStatus("current")


class _TmnxVrrpOperState_Type(Integer32):
    """Custom type tmnxVrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TmnxVrrpOperState_Type.__name__ = "Integer32"
_TmnxVrrpOperState_Object = MibTableColumn
tmnxVrrpOperState = _TmnxVrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 1),
    _TmnxVrrpOperState_Type()
)
tmnxVrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperState.setStatus("current")


class _TmnxVrrpOperVirtualMacAddr_Type(MacAddress):
    """Custom type tmnxVrrpOperVirtualMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxVrrpOperVirtualMacAddr_Object = MibTableColumn
tmnxVrrpOperVirtualMacAddr = _TmnxVrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 2),
    _TmnxVrrpOperVirtualMacAddr_Type()
)
tmnxVrrpOperVirtualMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperVirtualMacAddr.setStatus("current")


class _TmnxVrrpOperMismatchDiscard_Type(TruthValue):
    """Custom type tmnxVrrpOperMismatchDiscard based on TruthValue"""


_TmnxVrrpOperMismatchDiscard_Object = MibTableColumn
tmnxVrrpOperMismatchDiscard = _TmnxVrrpOperMismatchDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 3),
    _TmnxVrrpOperMismatchDiscard_Type()
)
tmnxVrrpOperMismatchDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperMismatchDiscard.setStatus("current")


class _TmnxVrrpOperPingReply_Type(TruthValue):
    """Custom type tmnxVrrpOperPingReply based on TruthValue"""


_TmnxVrrpOperPingReply_Object = MibTableColumn
tmnxVrrpOperPingReply = _TmnxVrrpOperPingReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 4),
    _TmnxVrrpOperPingReply_Type()
)
tmnxVrrpOperPingReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperPingReply.setStatus("current")


class _TmnxVrrpOperTelnetReply_Type(TruthValue):
    """Custom type tmnxVrrpOperTelnetReply based on TruthValue"""


_TmnxVrrpOperTelnetReply_Object = MibTableColumn
tmnxVrrpOperTelnetReply = _TmnxVrrpOperTelnetReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 5),
    _TmnxVrrpOperTelnetReply_Type()
)
tmnxVrrpOperTelnetReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperTelnetReply.setStatus("current")


class _TmnxVrrpOperSshReply_Type(TruthValue):
    """Custom type tmnxVrrpOperSshReply based on TruthValue"""


_TmnxVrrpOperSshReply_Object = MibTableColumn
tmnxVrrpOperSshReply = _TmnxVrrpOperSshReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 6),
    _TmnxVrrpOperSshReply_Type()
)
tmnxVrrpOperSshReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperSshReply.setStatus("current")


class _TmnxVrrpOperPolicyId_Type(Unsigned32):
    """Custom type tmnxVrrpOperPolicyId based on Unsigned32"""
    defaultValue = 0


_TmnxVrrpOperPolicyId_Object = MibTableColumn
tmnxVrrpOperPolicyId = _TmnxVrrpOperPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 7),
    _TmnxVrrpOperPolicyId_Type()
)
tmnxVrrpOperPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperPolicyId.setStatus("current")


class _TmnxVrrpOperInUsePriority_Type(Unsigned32):
    """Custom type tmnxVrrpOperInUsePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxVrrpOperInUsePriority_Type.__name__ = "Unsigned32"
_TmnxVrrpOperInUsePriority_Object = MibTableColumn
tmnxVrrpOperInUsePriority = _TmnxVrrpOperInUsePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 8),
    _TmnxVrrpOperInUsePriority_Type()
)
tmnxVrrpOperInUsePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperInUsePriority.setStatus("current")
_TmnxVrrpOperMasterSince_Type = TimeStamp
_TmnxVrrpOperMasterSince_Object = MibTableColumn
tmnxVrrpOperMasterSince = _TmnxVrrpOperMasterSince_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 9),
    _TmnxVrrpOperMasterSince_Type()
)
tmnxVrrpOperMasterSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterSince.setStatus("current")


class _TmnxVrrpOperMasterPriority_Type(Unsigned32):
    """Custom type tmnxVrrpOperMasterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxVrrpOperMasterPriority_Type.__name__ = "Unsigned32"
_TmnxVrrpOperMasterPriority_Object = MibTableColumn
tmnxVrrpOperMasterPriority = _TmnxVrrpOperMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 10),
    _TmnxVrrpOperMasterPriority_Type()
)
tmnxVrrpOperMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterPriority.setStatus("current")


class _TmnxVrrpOperOwner_Type(TruthValue):
    """Custom type tmnxVrrpOperOwner based on TruthValue"""


_TmnxVrrpOperOwner_Object = MibTableColumn
tmnxVrrpOperOwner = _TmnxVrrpOperOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 11),
    _TmnxVrrpOperOwner_Type()
)
tmnxVrrpOperOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperOwner.setStatus("current")
_TmnxVrrpOperMasterDownInterval_Type = TimeInterval
_TmnxVrrpOperMasterDownInterval_Object = MibTableColumn
tmnxVrrpOperMasterDownInterval = _TmnxVrrpOperMasterDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 12),
    _TmnxVrrpOperMasterDownInterval_Type()
)
tmnxVrrpOperMasterDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterDownInterval.setUnits("milliseconds")
_TmnxVrrpOperMasterDownTimer_Type = TimeInterval
_TmnxVrrpOperMasterDownTimer_Object = MibTableColumn
tmnxVrrpOperMasterDownTimer = _TmnxVrrpOperMasterDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 13),
    _TmnxVrrpOperMasterDownTimer_Type()
)
tmnxVrrpOperMasterDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpOperMasterDownTimer.setUnits("milliseconds")


class _TmnxVrrpOperAdvIntervalInherit_Type(TruthValue):
    """Custom type tmnxVrrpOperAdvIntervalInherit based on TruthValue"""


_TmnxVrrpOperAdvIntervalInherit_Object = MibTableColumn
tmnxVrrpOperAdvIntervalInherit = _TmnxVrrpOperAdvIntervalInherit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 14),
    _TmnxVrrpOperAdvIntervalInherit_Type()
)
tmnxVrrpOperAdvIntervalInherit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperAdvIntervalInherit.setStatus("current")
_TmnxVrrpOperInUseAdvInterval_Type = Integer32
_TmnxVrrpOperInUseAdvInterval_Object = MibTableColumn
tmnxVrrpOperInUseAdvInterval = _TmnxVrrpOperInUseAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 15),
    _TmnxVrrpOperInUseAdvInterval_Type()
)
tmnxVrrpOperInUseAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperInUseAdvInterval.setStatus("current")


class _TmnxVrrpOperTracerouteReply_Type(TruthValue):
    """Custom type tmnxVrrpOperTracerouteReply based on TruthValue"""


_TmnxVrrpOperTracerouteReply_Object = MibTableColumn
tmnxVrrpOperTracerouteReply = _TmnxVrrpOperTracerouteReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 16),
    _TmnxVrrpOperTracerouteReply_Type()
)
tmnxVrrpOperTracerouteReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperTracerouteReply.setStatus("current")


class _TmnxVrrpOperStandbyFwding_Type(TruthValue):
    """Custom type tmnxVrrpOperStandbyFwding based on TruthValue"""


_TmnxVrrpOperStandbyFwding_Object = MibTableColumn
tmnxVrrpOperStandbyFwding = _TmnxVrrpOperStandbyFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 17),
    _TmnxVrrpOperStandbyFwding_Type()
)
tmnxVrrpOperStandbyFwding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperStandbyFwding.setStatus("current")


class _TmnxVrrpOperAdvIntervalMilSec_Type(Unsigned32):
    """Custom type tmnxVrrpOperAdvIntervalMilSec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 900),
    )


_TmnxVrrpOperAdvIntervalMilSec_Type.__name__ = "Unsigned32"
_TmnxVrrpOperAdvIntervalMilSec_Object = MibTableColumn
tmnxVrrpOperAdvIntervalMilSec = _TmnxVrrpOperAdvIntervalMilSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 18),
    _TmnxVrrpOperAdvIntervalMilSec_Type()
)
tmnxVrrpOperAdvIntervalMilSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperAdvIntervalMilSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpOperAdvIntervalMilSec.setUnits("milliseconds")


class _TmnxVrrpOperInUseAdvIntlMilSec_Type(Unsigned32):
    """Custom type tmnxVrrpOperInUseAdvIntlMilSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 900),
    )


_TmnxVrrpOperInUseAdvIntlMilSec_Type.__name__ = "Unsigned32"
_TmnxVrrpOperInUseAdvIntlMilSec_Object = MibTableColumn
tmnxVrrpOperInUseAdvIntlMilSec = _TmnxVrrpOperInUseAdvIntlMilSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 19),
    _TmnxVrrpOperInUseAdvIntlMilSec_Type()
)
tmnxVrrpOperInUseAdvIntlMilSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperInUseAdvIntlMilSec.setStatus("current")


class _TmnxVrrpOperInitDelay_Type(Unsigned32):
    """Custom type tmnxVrrpOperInitDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxVrrpOperInitDelay_Type.__name__ = "Unsigned32"
_TmnxVrrpOperInitDelay_Object = MibTableColumn
tmnxVrrpOperInitDelay = _TmnxVrrpOperInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 20),
    _TmnxVrrpOperInitDelay_Type()
)
tmnxVrrpOperInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpOperInitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpOperInitDelay.setUnits("seconds")
_TmnxVrrpOperInitTimer_Type = TimeInterval
_TmnxVrrpOperInitTimer_Object = MibTableColumn
tmnxVrrpOperInitTimer = _TmnxVrrpOperInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 1, 1, 21),
    _TmnxVrrpOperInitTimer_Type()
)
tmnxVrrpOperInitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpOperInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpOperInitTimer.setUnits("milliseconds")
_TmnxVrrpRouterStatsTable_Object = MibTable
tmnxVrrpRouterStatsTable = _TmnxVrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxVrrpRouterStatsTable.setStatus("current")
_TmnxVrrpRouterStatsEntry_Object = MibTableRow
tmnxVrrpRouterStatsEntry = _TmnxVrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxVrrpRouterStatsEntry.setStatus("current")
_TmnxVrrpStatsAdvertiseSent_Type = Counter32
_TmnxVrrpStatsAdvertiseSent_Object = MibTableColumn
tmnxVrrpStatsAdvertiseSent = _TmnxVrrpStatsAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 1),
    _TmnxVrrpStatsAdvertiseSent_Type()
)
tmnxVrrpStatsAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsAdvertiseSent.setStatus("current")
_TmnxVrrpStatsPreemptEvents_Type = Counter32
_TmnxVrrpStatsPreemptEvents_Object = MibTableColumn
tmnxVrrpStatsPreemptEvents = _TmnxVrrpStatsPreemptEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 2),
    _TmnxVrrpStatsPreemptEvents_Type()
)
tmnxVrrpStatsPreemptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsPreemptEvents.setStatus("current")
_TmnxVrrpStatsPreemptedEvents_Type = Counter32
_TmnxVrrpStatsPreemptedEvents_Object = MibTableColumn
tmnxVrrpStatsPreemptedEvents = _TmnxVrrpStatsPreemptedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 3),
    _TmnxVrrpStatsPreemptedEvents_Type()
)
tmnxVrrpStatsPreemptedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsPreemptedEvents.setStatus("current")
_TmnxVrrpStatsMasterChanges_Type = Counter32
_TmnxVrrpStatsMasterChanges_Object = MibTableColumn
tmnxVrrpStatsMasterChanges = _TmnxVrrpStatsMasterChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 4),
    _TmnxVrrpStatsMasterChanges_Type()
)
tmnxVrrpStatsMasterChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsMasterChanges.setStatus("current")
_TmnxVrrpStatsAdvertiseIntervalDiscards_Type = Counter32
_TmnxVrrpStatsAdvertiseIntervalDiscards_Object = MibTableColumn
tmnxVrrpStatsAdvertiseIntervalDiscards = _TmnxVrrpStatsAdvertiseIntervalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 5),
    _TmnxVrrpStatsAdvertiseIntervalDiscards_Type()
)
tmnxVrrpStatsAdvertiseIntervalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsAdvertiseIntervalDiscards.setStatus("current")
_TmnxVrrpStatsAddressListDiscards_Type = Counter32
_TmnxVrrpStatsAddressListDiscards_Object = MibTableColumn
tmnxVrrpStatsAddressListDiscards = _TmnxVrrpStatsAddressListDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 6),
    _TmnxVrrpStatsAddressListDiscards_Type()
)
tmnxVrrpStatsAddressListDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsAddressListDiscards.setStatus("current")
_TmnxVrrpStatsTotalDiscards_Type = Counter32
_TmnxVrrpStatsTotalDiscards_Object = MibTableColumn
tmnxVrrpStatsTotalDiscards = _TmnxVrrpStatsTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 2, 1, 7),
    _TmnxVrrpStatsTotalDiscards_Type()
)
tmnxVrrpStatsTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpStatsTotalDiscards.setStatus("current")
_TmnxVrrpRouterMasterTable_Object = MibTable
tmnxVrrpRouterMasterTable = _TmnxVrrpRouterMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterTable.setStatus("current")
_TmnxVrrpRouterMasterEntry_Object = MibTableRow
tmnxVrrpRouterMasterEntry = _TmnxVrrpRouterMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1)
)
tmnxVrrpRouterMasterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterPrimaryAddr"),
)
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterEntry.setStatus("current")
_TmnxVrrpRouterMasterPrimaryAddr_Type = IpAddress
_TmnxVrrpRouterMasterPrimaryAddr_Object = MibTableColumn
tmnxVrrpRouterMasterPrimaryAddr = _TmnxVrrpRouterMasterPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1, 1),
    _TmnxVrrpRouterMasterPrimaryAddr_Type()
)
tmnxVrrpRouterMasterPrimaryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterPrimaryAddr.setStatus("current")
_TmnxVrrpRouterMasterLastSeen_Type = TimeStamp
_TmnxVrrpRouterMasterLastSeen_Object = MibTableColumn
tmnxVrrpRouterMasterLastSeen = _TmnxVrrpRouterMasterLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1, 2),
    _TmnxVrrpRouterMasterLastSeen_Type()
)
tmnxVrrpRouterMasterLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterLastSeen.setStatus("current")
_TmnxVrrpRouterMasterMessageCount_Type = Counter32
_TmnxVrrpRouterMasterMessageCount_Object = MibTableColumn
tmnxVrrpRouterMasterMessageCount = _TmnxVrrpRouterMasterMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1, 3),
    _TmnxVrrpRouterMasterMessageCount_Type()
)
tmnxVrrpRouterMasterMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterMessageCount.setStatus("current")
_TmnxVrrpRouterMasterAuthSequence_Type = Integer32
_TmnxVrrpRouterMasterAuthSequence_Object = MibTableColumn
tmnxVrrpRouterMasterAuthSequence = _TmnxVrrpRouterMasterAuthSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1, 4),
    _TmnxVrrpRouterMasterAuthSequence_Type()
)
tmnxVrrpRouterMasterAuthSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterAuthSequence.setStatus("current")
_TmnxVrrpRouterMasterIPListMatch_Type = TruthValue
_TmnxVrrpRouterMasterIPListMatch_Object = MibTableColumn
tmnxVrrpRouterMasterIPListMatch = _TmnxVrrpRouterMasterIPListMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 3, 1, 5),
    _TmnxVrrpRouterMasterIPListMatch_Type()
)
tmnxVrrpRouterMasterIPListMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouterMasterIPListMatch.setStatus("current")
_TmnxVrrpAssoBfdIntfTblLastChgd_Type = TimeStamp
_TmnxVrrpAssoBfdIntfTblLastChgd_Object = MibScalar
tmnxVrrpAssoBfdIntfTblLastChgd = _TmnxVrrpAssoBfdIntfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 4),
    _TmnxVrrpAssoBfdIntfTblLastChgd_Type()
)
tmnxVrrpAssoBfdIntfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfTblLastChgd.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfTable_Object = MibTable
tmnxVrrpAssoBfdIntfTable = _TmnxVrrpAssoBfdIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfTable.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfEntry_Object = MibTableRow
tmnxVrrpAssoBfdIntfEntry = _TmnxVrrpAssoBfdIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1)
)
tmnxVrrpAssoBfdIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSvcId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfIfName"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfDestIpType"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfDestIp"),
)
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfEntry.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfSvcId_Type = TmnxServId
_TmnxVrrpAssoBfdIntfSvcId_Object = MibTableColumn
tmnxVrrpAssoBfdIntfSvcId = _TmnxVrrpAssoBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 1),
    _TmnxVrrpAssoBfdIntfSvcId_Type()
)
tmnxVrrpAssoBfdIntfSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfSvcId.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfIfName_Type = TNamedItem
_TmnxVrrpAssoBfdIntfIfName_Object = MibTableColumn
tmnxVrrpAssoBfdIntfIfName = _TmnxVrrpAssoBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 2),
    _TmnxVrrpAssoBfdIntfIfName_Type()
)
tmnxVrrpAssoBfdIntfIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfIfName.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfDestIpType_Type = InetAddressType
_TmnxVrrpAssoBfdIntfDestIpType_Object = MibTableColumn
tmnxVrrpAssoBfdIntfDestIpType = _TmnxVrrpAssoBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 3),
    _TmnxVrrpAssoBfdIntfDestIpType_Type()
)
tmnxVrrpAssoBfdIntfDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfDestIpType.setStatus("obsolete")


class _TmnxVrrpAssoBfdIntfDestIp_Type(InetAddress):
    """Custom type tmnxVrrpAssoBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVrrpAssoBfdIntfDestIp_Type.__name__ = "InetAddress"
_TmnxVrrpAssoBfdIntfDestIp_Object = MibTableColumn
tmnxVrrpAssoBfdIntfDestIp = _TmnxVrrpAssoBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 4),
    _TmnxVrrpAssoBfdIntfDestIp_Type()
)
tmnxVrrpAssoBfdIntfDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfDestIp.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfRowStatus_Type = RowStatus
_TmnxVrrpAssoBfdIntfRowStatus_Object = MibTableColumn
tmnxVrrpAssoBfdIntfRowStatus = _TmnxVrrpAssoBfdIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 5),
    _TmnxVrrpAssoBfdIntfRowStatus_Type()
)
tmnxVrrpAssoBfdIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfRowStatus.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfLastChgd_Type = TimeStamp
_TmnxVrrpAssoBfdIntfLastChgd_Object = MibTableColumn
tmnxVrrpAssoBfdIntfLastChgd = _TmnxVrrpAssoBfdIntfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 6),
    _TmnxVrrpAssoBfdIntfLastChgd_Type()
)
tmnxVrrpAssoBfdIntfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfLastChgd.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfSrcIpType_Type = InetAddressType
_TmnxVrrpAssoBfdIntfSrcIpType_Object = MibTableColumn
tmnxVrrpAssoBfdIntfSrcIpType = _TmnxVrrpAssoBfdIntfSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 7),
    _TmnxVrrpAssoBfdIntfSrcIpType_Type()
)
tmnxVrrpAssoBfdIntfSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfSrcIpType.setStatus("obsolete")


class _TmnxVrrpAssoBfdIntfSrcIp_Type(InetAddress):
    """Custom type tmnxVrrpAssoBfdIntfSrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVrrpAssoBfdIntfSrcIp_Type.__name__ = "InetAddress"
_TmnxVrrpAssoBfdIntfSrcIp_Object = MibTableColumn
tmnxVrrpAssoBfdIntfSrcIp = _TmnxVrrpAssoBfdIntfSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 8),
    _TmnxVrrpAssoBfdIntfSrcIp_Type()
)
tmnxVrrpAssoBfdIntfSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfSrcIp.setStatus("obsolete")
_TmnxVrrpAssoBfdIntfSessOperState_Type = TmnxVrrpAssoBfdIntfSessOperState
_TmnxVrrpAssoBfdIntfSessOperState_Object = MibTableColumn
tmnxVrrpAssoBfdIntfSessOperState = _TmnxVrrpAssoBfdIntfSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 5, 1, 9),
    _TmnxVrrpAssoBfdIntfSessOperState_Type()
)
tmnxVrrpAssoBfdIntfSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpAssoBfdIntfSessOperState.setStatus("obsolete")
_TVrrpOpTblLastChgd_Type = TimeStamp
_TVrrpOpTblLastChgd_Object = MibScalar
tVrrpOpTblLastChgd = _TVrrpOpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 6),
    _TVrrpOpTblLastChgd_Type()
)
tVrrpOpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpTblLastChgd.setStatus("current")
_TVrrpOpTable_Object = MibTable
tVrrpOpTable = _TVrrpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7)
)
if mibBuilder.loadTexts:
    tVrrpOpTable.setStatus("current")
_TVrrpOpEntry_Object = MibTableRow
tVrrpOpEntry = _TVrrpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tVrrpOpEntry.setStatus("current")


class _TVrrpOpState_Type(Integer32):
    """Custom type tVrrpOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TVrrpOpState_Type.__name__ = "Integer32"
_TVrrpOpState_Object = MibTableColumn
tVrrpOpState = _TVrrpOpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 1),
    _TVrrpOpState_Type()
)
tVrrpOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpState.setStatus("current")


class _TVrrpOpVirtualMacAddr_Type(MacAddress):
    """Custom type tVrrpOpVirtualMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TVrrpOpVirtualMacAddr_Object = MibTableColumn
tVrrpOpVirtualMacAddr = _TVrrpOpVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 2),
    _TVrrpOpVirtualMacAddr_Type()
)
tVrrpOpVirtualMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpVirtualMacAddr.setStatus("current")


class _TVrrpOpPingReply_Type(TruthValue):
    """Custom type tVrrpOpPingReply based on TruthValue"""


_TVrrpOpPingReply_Object = MibTableColumn
tVrrpOpPingReply = _TVrrpOpPingReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 3),
    _TVrrpOpPingReply_Type()
)
tVrrpOpPingReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpPingReply.setStatus("current")


class _TVrrpOpTelnetReply_Type(TruthValue):
    """Custom type tVrrpOpTelnetReply based on TruthValue"""


_TVrrpOpTelnetReply_Object = MibTableColumn
tVrrpOpTelnetReply = _TVrrpOpTelnetReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 4),
    _TVrrpOpTelnetReply_Type()
)
tVrrpOpTelnetReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpTelnetReply.setStatus("current")


class _TVrrpOpPolicyId_Type(Unsigned32):
    """Custom type tVrrpOpPolicyId based on Unsigned32"""
    defaultValue = 0


_TVrrpOpPolicyId_Object = MibTableColumn
tVrrpOpPolicyId = _TVrrpOpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 5),
    _TVrrpOpPolicyId_Type()
)
tVrrpOpPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpPolicyId.setStatus("current")


class _TVrrpOpInUsePriority_Type(Unsigned32):
    """Custom type tVrrpOpInUsePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TVrrpOpInUsePriority_Type.__name__ = "Unsigned32"
_TVrrpOpInUsePriority_Object = MibTableColumn
tVrrpOpInUsePriority = _TVrrpOpInUsePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 6),
    _TVrrpOpInUsePriority_Type()
)
tVrrpOpInUsePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpInUsePriority.setStatus("current")
_TVrrpOpMasterSince_Type = TimeStamp
_TVrrpOpMasterSince_Object = MibTableColumn
tVrrpOpMasterSince = _TVrrpOpMasterSince_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 7),
    _TVrrpOpMasterSince_Type()
)
tVrrpOpMasterSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpMasterSince.setStatus("current")


class _TVrrpOpMasterPriority_Type(Unsigned32):
    """Custom type tVrrpOpMasterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TVrrpOpMasterPriority_Type.__name__ = "Unsigned32"
_TVrrpOpMasterPriority_Object = MibTableColumn
tVrrpOpMasterPriority = _TVrrpOpMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 8),
    _TVrrpOpMasterPriority_Type()
)
tVrrpOpMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpMasterPriority.setStatus("current")


class _TVrrpOpOwner_Type(TruthValue):
    """Custom type tVrrpOpOwner based on TruthValue"""


_TVrrpOpOwner_Object = MibTableColumn
tVrrpOpOwner = _TVrrpOpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 9),
    _TVrrpOpOwner_Type()
)
tVrrpOpOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpOwner.setStatus("current")
_TVrrpOpMasterDownInterval_Type = TimeInterval
_TVrrpOpMasterDownInterval_Object = MibTableColumn
tVrrpOpMasterDownInterval = _TVrrpOpMasterDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 10),
    _TVrrpOpMasterDownInterval_Type()
)
tVrrpOpMasterDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpMasterDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpOpMasterDownInterval.setUnits("milliseconds")
_TVrrpOpMasterDownTimer_Type = TimeInterval
_TVrrpOpMasterDownTimer_Object = MibTableColumn
tVrrpOpMasterDownTimer = _TVrrpOpMasterDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 11),
    _TVrrpOpMasterDownTimer_Type()
)
tVrrpOpMasterDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpMasterDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpOpMasterDownTimer.setUnits("milliseconds")


class _TVrrpOpAdvIntervalInherit_Type(TruthValue):
    """Custom type tVrrpOpAdvIntervalInherit based on TruthValue"""


_TVrrpOpAdvIntervalInherit_Object = MibTableColumn
tVrrpOpAdvIntervalInherit = _TVrrpOpAdvIntervalInherit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 12),
    _TVrrpOpAdvIntervalInherit_Type()
)
tVrrpOpAdvIntervalInherit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpAdvIntervalInherit.setStatus("current")


class _TVrrpOpInUseAdvInterval_Type(TimeInterval):
    """Custom type tVrrpOpInUseAdvInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_TVrrpOpInUseAdvInterval_Type.__name__ = "TimeInterval"
_TVrrpOpInUseAdvInterval_Object = MibTableColumn
tVrrpOpInUseAdvInterval = _TVrrpOpInUseAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 13),
    _TVrrpOpInUseAdvInterval_Type()
)
tVrrpOpInUseAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpInUseAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpOpInUseAdvInterval.setUnits("centiseconds")


class _TVrrpOpTracerouteReply_Type(TruthValue):
    """Custom type tVrrpOpTracerouteReply based on TruthValue"""


_TVrrpOpTracerouteReply_Object = MibTableColumn
tVrrpOpTracerouteReply = _TVrrpOpTracerouteReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 14),
    _TVrrpOpTracerouteReply_Type()
)
tVrrpOpTracerouteReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpTracerouteReply.setStatus("current")


class _TVrrpOpStandbyFwding_Type(TruthValue):
    """Custom type tVrrpOpStandbyFwding based on TruthValue"""


_TVrrpOpStandbyFwding_Object = MibTableColumn
tVrrpOpStandbyFwding = _TVrrpOpStandbyFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 15),
    _TVrrpOpStandbyFwding_Type()
)
tVrrpOpStandbyFwding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpStandbyFwding.setStatus("current")


class _TVrrpOpInitDelay_Type(Unsigned32):
    """Custom type tVrrpOpInitDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TVrrpOpInitDelay_Type.__name__ = "Unsigned32"
_TVrrpOpInitDelay_Object = MibTableColumn
tVrrpOpInitDelay = _TVrrpOpInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 16),
    _TVrrpOpInitDelay_Type()
)
tVrrpOpInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpOpInitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpOpInitDelay.setUnits("seconds")
_TVrrpOpInitTimer_Type = TimeInterval
_TVrrpOpInitTimer_Object = MibTableColumn
tVrrpOpInitTimer = _TVrrpOpInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 17),
    _TVrrpOpInitTimer_Type()
)
tVrrpOpInitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpOpInitTimer.setUnits("milliseconds")
_TVrrpOpLastChgd_Type = TimeStamp
_TVrrpOpLastChgd_Object = MibTableColumn
tVrrpOpLastChgd = _TVrrpOpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 18),
    _TVrrpOpLastChgd_Type()
)
tVrrpOpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpLastChgd.setStatus("current")


class _TVrrpOpOperDownReason_Type(Integer32):
    """Custom type tVrrpOpOperDownReason based on Integer32"""
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
        *(("adminDown", 2),
          ("ifDown", 3),
          ("noLnkLclAddrCfg", 4),
          ("notActive", 1),
          ("rtrAdvNoProperCfg", 5),
          ("unknown", 0))
    )


_TVrrpOpOperDownReason_Type.__name__ = "Integer32"
_TVrrpOpOperDownReason_Object = MibTableColumn
tVrrpOpOperDownReason = _TVrrpOpOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 7, 1, 19),
    _TVrrpOpOperDownReason_Type()
)
tVrrpOpOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpOpOperDownReason.setStatus("current")
_TVrrpRtrStatisticsTable_Object = MibTable
tVrrpRtrStatisticsTable = _TVrrpRtrStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8)
)
if mibBuilder.loadTexts:
    tVrrpRtrStatisticsTable.setStatus("current")
_TVrrpRtrStatisticsEntry_Object = MibTableRow
tVrrpRtrStatisticsEntry = _TVrrpRtrStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tVrrpRtrStatisticsEntry.setStatus("current")
_TVrrpStatAdvertiseSent_Type = Counter32
_TVrrpStatAdvertiseSent_Object = MibTableColumn
tVrrpStatAdvertiseSent = _TVrrpStatAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 1),
    _TVrrpStatAdvertiseSent_Type()
)
tVrrpStatAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatAdvertiseSent.setStatus("current")
_TVrrpStatPreemptEvents_Type = Counter32
_TVrrpStatPreemptEvents_Object = MibTableColumn
tVrrpStatPreemptEvents = _TVrrpStatPreemptEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 2),
    _TVrrpStatPreemptEvents_Type()
)
tVrrpStatPreemptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatPreemptEvents.setStatus("current")
_TVrrpStatPreemptedEvents_Type = Counter32
_TVrrpStatPreemptedEvents_Object = MibTableColumn
tVrrpStatPreemptedEvents = _TVrrpStatPreemptedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 3),
    _TVrrpStatPreemptedEvents_Type()
)
tVrrpStatPreemptedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatPreemptedEvents.setStatus("current")
_TVrrpStatMasterChanges_Type = Counter32
_TVrrpStatMasterChanges_Object = MibTableColumn
tVrrpStatMasterChanges = _TVrrpStatMasterChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 4),
    _TVrrpStatMasterChanges_Type()
)
tVrrpStatMasterChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatMasterChanges.setStatus("current")
_TVrrpStatAdvIntvlDiscards_Type = Counter32
_TVrrpStatAdvIntvlDiscards_Object = MibTableColumn
tVrrpStatAdvIntvlDiscards = _TVrrpStatAdvIntvlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 5),
    _TVrrpStatAdvIntvlDiscards_Type()
)
tVrrpStatAdvIntvlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatAdvIntvlDiscards.setStatus("current")
_TVrrpStatTotalDiscards_Type = Counter32
_TVrrpStatTotalDiscards_Object = MibTableColumn
tVrrpStatTotalDiscards = _TVrrpStatTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 8, 1, 6),
    _TVrrpStatTotalDiscards_Type()
)
tVrrpStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpStatTotalDiscards.setStatus("current")
_TVrrpRtrMasterTable_Object = MibTable
tVrrpRtrMasterTable = _TVrrpRtrMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9)
)
if mibBuilder.loadTexts:
    tVrrpRtrMasterTable.setStatus("current")
_TVrrpRtrMasterEntry_Object = MibTableRow
tVrrpRtrMasterEntry = _TVrrpRtrMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1)
)
tVrrpRtrMasterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpOperationsVrId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtrMasterInetAddrType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtrMasterPrimaryAddr"),
)
if mibBuilder.loadTexts:
    tVrrpRtrMasterEntry.setStatus("current")
_TVrrpRtrMasterInetAddrType_Type = InetAddressType
_TVrrpRtrMasterInetAddrType_Object = MibTableColumn
tVrrpRtrMasterInetAddrType = _TVrrpRtrMasterInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 1),
    _TVrrpRtrMasterInetAddrType_Type()
)
tVrrpRtrMasterInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtrMasterInetAddrType.setStatus("current")


class _TVrrpRtrMasterPrimaryAddr_Type(InetAddress):
    """Custom type tVrrpRtrMasterPrimaryAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TVrrpRtrMasterPrimaryAddr_Type.__name__ = "InetAddress"
_TVrrpRtrMasterPrimaryAddr_Object = MibTableColumn
tVrrpRtrMasterPrimaryAddr = _TVrrpRtrMasterPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 2),
    _TVrrpRtrMasterPrimaryAddr_Type()
)
tVrrpRtrMasterPrimaryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtrMasterPrimaryAddr.setStatus("current")
_TVrrpRtrMasterLastSeen_Type = TimeStamp
_TVrrpRtrMasterLastSeen_Object = MibTableColumn
tVrrpRtrMasterLastSeen = _TVrrpRtrMasterLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 3),
    _TVrrpRtrMasterLastSeen_Type()
)
tVrrpRtrMasterLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtrMasterLastSeen.setStatus("current")
_TVrrpRtrMasterMessageCount_Type = Counter32
_TVrrpRtrMasterMessageCount_Object = MibTableColumn
tVrrpRtrMasterMessageCount = _TVrrpRtrMasterMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 4),
    _TVrrpRtrMasterMessageCount_Type()
)
tVrrpRtrMasterMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtrMasterMessageCount.setStatus("current")
_TVrrpRtrMasterAuthSequence_Type = Integer32
_TVrrpRtrMasterAuthSequence_Object = MibTableColumn
tVrrpRtrMasterAuthSequence = _TVrrpRtrMasterAuthSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 5),
    _TVrrpRtrMasterAuthSequence_Type()
)
tVrrpRtrMasterAuthSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtrMasterAuthSequence.setStatus("current")
_TVrrpRtrMasterIPListMatch_Type = TruthValue
_TVrrpRtrMasterIPListMatch_Object = MibTableColumn
tVrrpRtrMasterIPListMatch = _TVrrpRtrMasterIPListMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 9, 1, 6),
    _TVrrpRtrMasterIPListMatch_Type()
)
tVrrpRtrMasterIPListMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtrMasterIPListMatch.setStatus("current")
_TVrrpIpv6RouterAdvertTable_Object = MibTable
tVrrpIpv6RouterAdvertTable = _TVrrpIpv6RouterAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 10)
)
if mibBuilder.loadTexts:
    tVrrpIpv6RouterAdvertTable.setStatus("current")
_TVrrpIpv6RouterAdvertEntry_Object = MibTableRow
tVrrpIpv6RouterAdvertEntry = _TVrrpIpv6RouterAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tVrrpIpv6RouterAdvertEntry.setStatus("current")


class _TVrrpIpv6RouterAdvertUseVirtualMac_Type(TruthValue):
    """Custom type tVrrpIpv6RouterAdvertUseVirtualMac based on TruthValue"""


_TVrrpIpv6RouterAdvertUseVirtualMac_Object = MibTableColumn
tVrrpIpv6RouterAdvertUseVirtualMac = _TVrrpIpv6RouterAdvertUseVirtualMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 10, 1, 1),
    _TVrrpIpv6RouterAdvertUseVirtualMac_Type()
)
tVrrpIpv6RouterAdvertUseVirtualMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpIpv6RouterAdvertUseVirtualMac.setStatus("current")
_TVrrpAssoBfdIntfTblLastChgd_Type = TimeStamp
_TVrrpAssoBfdIntfTblLastChgd_Object = MibScalar
tVrrpAssoBfdIntfTblLastChgd = _TVrrpAssoBfdIntfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 11),
    _TVrrpAssoBfdIntfTblLastChgd_Type()
)
tVrrpAssoBfdIntfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfTblLastChgd.setStatus("current")
_TVrrpAssoBfdIntfTable_Object = MibTable
tVrrpAssoBfdIntfTable = _TVrrpAssoBfdIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12)
)
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfTable.setStatus("current")
_TVrrpAssoBfdIntfEntry_Object = MibTableRow
tVrrpAssoBfdIntfEntry = _TVrrpAssoBfdIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1)
)
tVrrpAssoBfdIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfVrIdIpType"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfSvcId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfIfName"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfDestIpType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfDestIp"),
)
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfEntry.setStatus("current")
_TVrrpAssoBfdIntfVrIdIpType_Type = InetAddressType
_TVrrpAssoBfdIntfVrIdIpType_Object = MibTableColumn
tVrrpAssoBfdIntfVrIdIpType = _TVrrpAssoBfdIntfVrIdIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 1),
    _TVrrpAssoBfdIntfVrIdIpType_Type()
)
tVrrpAssoBfdIntfVrIdIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfVrIdIpType.setStatus("current")
_TVrrpAssoBfdIntfSvcId_Type = TmnxServId
_TVrrpAssoBfdIntfSvcId_Object = MibTableColumn
tVrrpAssoBfdIntfSvcId = _TVrrpAssoBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 2),
    _TVrrpAssoBfdIntfSvcId_Type()
)
tVrrpAssoBfdIntfSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfSvcId.setStatus("current")
_TVrrpAssoBfdIntfIfName_Type = TNamedItem
_TVrrpAssoBfdIntfIfName_Object = MibTableColumn
tVrrpAssoBfdIntfIfName = _TVrrpAssoBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 3),
    _TVrrpAssoBfdIntfIfName_Type()
)
tVrrpAssoBfdIntfIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfIfName.setStatus("current")
_TVrrpAssoBfdIntfDestIpType_Type = InetAddressType
_TVrrpAssoBfdIntfDestIpType_Object = MibTableColumn
tVrrpAssoBfdIntfDestIpType = _TVrrpAssoBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 4),
    _TVrrpAssoBfdIntfDestIpType_Type()
)
tVrrpAssoBfdIntfDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfDestIpType.setStatus("current")


class _TVrrpAssoBfdIntfDestIp_Type(InetAddress):
    """Custom type tVrrpAssoBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TVrrpAssoBfdIntfDestIp_Type.__name__ = "InetAddress"
_TVrrpAssoBfdIntfDestIp_Object = MibTableColumn
tVrrpAssoBfdIntfDestIp = _TVrrpAssoBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 5),
    _TVrrpAssoBfdIntfDestIp_Type()
)
tVrrpAssoBfdIntfDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfDestIp.setStatus("current")
_TVrrpAssoBfdIntfRowStatus_Type = RowStatus
_TVrrpAssoBfdIntfRowStatus_Object = MibTableColumn
tVrrpAssoBfdIntfRowStatus = _TVrrpAssoBfdIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 6),
    _TVrrpAssoBfdIntfRowStatus_Type()
)
tVrrpAssoBfdIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfRowStatus.setStatus("current")
_TVrrpAssoBfdIntfLastChgd_Type = TimeStamp
_TVrrpAssoBfdIntfLastChgd_Object = MibTableColumn
tVrrpAssoBfdIntfLastChgd = _TVrrpAssoBfdIntfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 7),
    _TVrrpAssoBfdIntfLastChgd_Type()
)
tVrrpAssoBfdIntfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfLastChgd.setStatus("current")
_TVrrpAssoBfdIntfSrcIpType_Type = InetAddressType
_TVrrpAssoBfdIntfSrcIpType_Object = MibTableColumn
tVrrpAssoBfdIntfSrcIpType = _TVrrpAssoBfdIntfSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 8),
    _TVrrpAssoBfdIntfSrcIpType_Type()
)
tVrrpAssoBfdIntfSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfSrcIpType.setStatus("current")


class _TVrrpAssoBfdIntfSrcIp_Type(InetAddress):
    """Custom type tVrrpAssoBfdIntfSrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TVrrpAssoBfdIntfSrcIp_Type.__name__ = "InetAddress"
_TVrrpAssoBfdIntfSrcIp_Object = MibTableColumn
tVrrpAssoBfdIntfSrcIp = _TVrrpAssoBfdIntfSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 9),
    _TVrrpAssoBfdIntfSrcIp_Type()
)
tVrrpAssoBfdIntfSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfSrcIp.setStatus("current")
_TVrrpAssoBfdIntfSessOperState_Type = TmnxVrrpAssoBfdIntfSessOperState
_TVrrpAssoBfdIntfSessOperState_Object = MibTableColumn
tVrrpAssoBfdIntfSessOperState = _TVrrpAssoBfdIntfSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 1, 12, 1, 10),
    _TVrrpAssoBfdIntfSessOperState_Type()
)
tVrrpAssoBfdIntfSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpAssoBfdIntfSessOperState.setStatus("current")
_TmnxVrrpPolicyObjects_ObjectIdentity = ObjectIdentity
tmnxVrrpPolicyObjects = _TmnxVrrpPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2)
)
_TmnxVrrpPolicyTable_Object = MibTable
tmnxVrrpPolicyTable = _TmnxVrrpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxVrrpPolicyTable.setStatus("current")
_TmnxVrrpPolicyEntry_Object = MibTableRow
tmnxVrrpPolicyEntry = _TmnxVrrpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1)
)
tmnxVrrpPolicyEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxVrrpPolicyEntry.setStatus("current")
_TmnxVrrpPolicyId_Type = TmnxVrrpPolicyID
_TmnxVrrpPolicyId_Object = MibTableColumn
tmnxVrrpPolicyId = _TmnxVrrpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 1),
    _TmnxVrrpPolicyId_Type()
)
tmnxVrrpPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyId.setStatus("current")
_TmnxVrrpPolicyRowStatus_Type = RowStatus
_TmnxVrrpPolicyRowStatus_Object = MibTableColumn
tmnxVrrpPolicyRowStatus = _TmnxVrrpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 2),
    _TmnxVrrpPolicyRowStatus_Type()
)
tmnxVrrpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyRowStatus.setStatus("current")


class _TmnxVrrpPolicyDescription_Type(TItemDescription):
    """Custom type tmnxVrrpPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxVrrpPolicyDescription_Object = MibTableColumn
tmnxVrrpPolicyDescription = _TmnxVrrpPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 3),
    _TmnxVrrpPolicyDescription_Type()
)
tmnxVrrpPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyDescription.setStatus("current")


class _TmnxVrrpPolicyDeltaInUseLimit_Type(TmnxVrrpPriority):
    """Custom type tmnxVrrpPolicyDeltaInUseLimit based on TmnxVrrpPriority"""
    defaultValue = 1

    subtypeSpec = TmnxVrrpPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxVrrpPolicyDeltaInUseLimit_Type.__name__ = "TmnxVrrpPriority"
_TmnxVrrpPolicyDeltaInUseLimit_Object = MibTableColumn
tmnxVrrpPolicyDeltaInUseLimit = _TmnxVrrpPolicyDeltaInUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 4),
    _TmnxVrrpPolicyDeltaInUseLimit_Type()
)
tmnxVrrpPolicyDeltaInUseLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyDeltaInUseLimit.setStatus("current")
_TmnxVrrpPolicyReferenceCount_Type = Unsigned32
_TmnxVrrpPolicyReferenceCount_Object = MibTableColumn
tmnxVrrpPolicyReferenceCount = _TmnxVrrpPolicyReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 5),
    _TmnxVrrpPolicyReferenceCount_Type()
)
tmnxVrrpPolicyReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyReferenceCount.setStatus("current")
_TmnxVrrpPolicyCurrentExplicit_Type = TmnxVrrpPriority
_TmnxVrrpPolicyCurrentExplicit_Object = MibTableColumn
tmnxVrrpPolicyCurrentExplicit = _TmnxVrrpPolicyCurrentExplicit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 6),
    _TmnxVrrpPolicyCurrentExplicit_Type()
)
tmnxVrrpPolicyCurrentExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyCurrentExplicit.setStatus("current")
_TmnxVrrpPolicyCurrentDeltaSum_Type = TmnxVrrpPriority
_TmnxVrrpPolicyCurrentDeltaSum_Object = MibTableColumn
tmnxVrrpPolicyCurrentDeltaSum = _TmnxVrrpPolicyCurrentDeltaSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 7),
    _TmnxVrrpPolicyCurrentDeltaSum_Type()
)
tmnxVrrpPolicyCurrentDeltaSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPolicyCurrentDeltaSum.setStatus("current")


class _TmnxVrrpPolicySvcContext_Type(TmnxServId):
    """Custom type tmnxVrrpPolicySvcContext based on TmnxServId"""
    defaultValue = 0


_TmnxVrrpPolicySvcContext_Object = MibTableColumn
tmnxVrrpPolicySvcContext = _TmnxVrrpPolicySvcContext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 1, 1, 8),
    _TmnxVrrpPolicySvcContext_Type()
)
tmnxVrrpPolicySvcContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPolicySvcContext.setStatus("current")
_TmnxVrrpPortDownEventTable_Object = MibTable
tmnxVrrpPortDownEventTable = _TmnxVrrpPortDownEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventTable.setStatus("current")
_TmnxVrrpPortDownEventEntry_Object = MibTableRow
tmnxVrrpPortDownEventEntry = _TmnxVrrpPortDownEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1)
)
tmnxVrrpPortDownEventEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventPortId"),
)
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventEntry.setStatus("current")
_TmnxVrrpPortDownEventPortId_Type = TmnxPortID
_TmnxVrrpPortDownEventPortId_Object = MibTableColumn
tmnxVrrpPortDownEventPortId = _TmnxVrrpPortDownEventPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 1),
    _TmnxVrrpPortDownEventPortId_Type()
)
tmnxVrrpPortDownEventPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventPortId.setStatus("current")
_TmnxVrrpPortDownEventRowStatus_Type = RowStatus
_TmnxVrrpPortDownEventRowStatus_Object = MibTableColumn
tmnxVrrpPortDownEventRowStatus = _TmnxVrrpPortDownEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 2),
    _TmnxVrrpPortDownEventRowStatus_Type()
)
tmnxVrrpPortDownEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventRowStatus.setStatus("current")


class _TmnxVrrpPortDownEventPriority_Type(TmnxVrrpPriority):
    """Custom type tmnxVrrpPortDownEventPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TmnxVrrpPortDownEventPriority_Object = MibTableColumn
tmnxVrrpPortDownEventPriority = _TmnxVrrpPortDownEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 3),
    _TmnxVrrpPortDownEventPriority_Type()
)
tmnxVrrpPortDownEventPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventPriority.setStatus("current")


class _TmnxVrrpPortDownEventType_Type(TmnxEventType):
    """Custom type tmnxVrrpPortDownEventType based on TmnxEventType"""


_TmnxVrrpPortDownEventType_Object = MibTableColumn
tmnxVrrpPortDownEventType = _TmnxVrrpPortDownEventType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 4),
    _TmnxVrrpPortDownEventType_Type()
)
tmnxVrrpPortDownEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventType.setStatus("current")


class _TmnxVrrpPortDownEventHoldSet_Type(TmnxEventHoldSet):
    """Custom type tmnxVrrpPortDownEventHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TmnxVrrpPortDownEventHoldSet_Object = MibTableColumn
tmnxVrrpPortDownEventHoldSet = _TmnxVrrpPortDownEventHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 5),
    _TmnxVrrpPortDownEventHoldSet_Type()
)
tmnxVrrpPortDownEventHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldSet.setUnits("seconds")
_TmnxVrrpPortDownEventOperState_Type = TmnxPortDownEventOperState
_TmnxVrrpPortDownEventOperState_Object = MibTableColumn
tmnxVrrpPortDownEventOperState = _TmnxVrrpPortDownEventOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 6),
    _TmnxVrrpPortDownEventOperState_Type()
)
tmnxVrrpPortDownEventOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventOperState.setStatus("current")
_TmnxVrrpPortDownEventHoldSetRemaining_Type = TmnxEventHoldSet
_TmnxVrrpPortDownEventHoldSetRemaining_Object = MibTableColumn
tmnxVrrpPortDownEventHoldSetRemaining = _TmnxVrrpPortDownEventHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 7),
    _TmnxVrrpPortDownEventHoldSetRemaining_Type()
)
tmnxVrrpPortDownEventHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldSetRemaining.setUnits("seconds")
_TmnxVrrpPortDownEventPrevState_Type = TmnxPortDownEventOperState
_TmnxVrrpPortDownEventPrevState_Object = MibTableColumn
tmnxVrrpPortDownEventPrevState = _TmnxVrrpPortDownEventPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 8),
    _TmnxVrrpPortDownEventPrevState_Type()
)
tmnxVrrpPortDownEventPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventPrevState.setStatus("current")
_TmnxVrrpPortDownEventLastTransition_Type = TimeStamp
_TmnxVrrpPortDownEventLastTransition_Object = MibTableColumn
tmnxVrrpPortDownEventLastTransition = _TmnxVrrpPortDownEventLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 9),
    _TmnxVrrpPortDownEventLastTransition_Type()
)
tmnxVrrpPortDownEventLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventLastTransition.setStatus("current")
_TmnxVrrpPortDownEventSetCounter_Type = Counter32
_TmnxVrrpPortDownEventSetCounter_Object = MibTableColumn
tmnxVrrpPortDownEventSetCounter = _TmnxVrrpPortDownEventSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 10),
    _TmnxVrrpPortDownEventSetCounter_Type()
)
tmnxVrrpPortDownEventSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventSetCounter.setStatus("current")
_TmnxVrrpPortDownEventInUse_Type = TruthValue
_TmnxVrrpPortDownEventInUse_Object = MibTableColumn
tmnxVrrpPortDownEventInUse = _TmnxVrrpPortDownEventInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 11),
    _TmnxVrrpPortDownEventInUse_Type()
)
tmnxVrrpPortDownEventInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventInUse.setStatus("current")


class _TmnxVrrpPortDownEventHoldClear_Type(TmnxEventHoldClear):
    """Custom type tmnxVrrpPortDownEventHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TmnxVrrpPortDownEventHoldClear_Object = MibTableColumn
tmnxVrrpPortDownEventHoldClear = _TmnxVrrpPortDownEventHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 12),
    _TmnxVrrpPortDownEventHoldClear_Type()
)
tmnxVrrpPortDownEventHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldClear.setUnits("seconds")
_TmnxVrrpPortDownEventHoldClearRemaining_Type = TmnxEventHoldClear
_TmnxVrrpPortDownEventHoldClearRemaining_Object = MibTableColumn
tmnxVrrpPortDownEventHoldClearRemaining = _TmnxVrrpPortDownEventHoldClearRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 2, 1, 13),
    _TmnxVrrpPortDownEventHoldClearRemaining_Type()
)
tmnxVrrpPortDownEventHoldClearRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldClearRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpPortDownEventHoldClearRemaining.setUnits("seconds")
_TmnxVrrpLagPortDownEventTable_Object = MibTable
tmnxVrrpLagPortDownEventTable = _TmnxVrrpLagPortDownEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventTable.setStatus("current")
_TmnxVrrpLagPortDownEventEntry_Object = MibTableRow
tmnxVrrpLagPortDownEventEntry = _TmnxVrrpLagPortDownEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1)
)
tmnxVrrpLagPortDownEventEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventLagId"),
)
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventEntry.setStatus("current")
_TmnxVrrpLagPortDownEventLagId_Type = LAGInterfaceNumber
_TmnxVrrpLagPortDownEventLagId_Object = MibTableColumn
tmnxVrrpLagPortDownEventLagId = _TmnxVrrpLagPortDownEventLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 1),
    _TmnxVrrpLagPortDownEventLagId_Type()
)
tmnxVrrpLagPortDownEventLagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventLagId.setStatus("current")
_TmnxVrrpLagPortDownEventRowStatus_Type = RowStatus
_TmnxVrrpLagPortDownEventRowStatus_Object = MibTableColumn
tmnxVrrpLagPortDownEventRowStatus = _TmnxVrrpLagPortDownEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 2),
    _TmnxVrrpLagPortDownEventRowStatus_Type()
)
tmnxVrrpLagPortDownEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventRowStatus.setStatus("current")


class _TmnxVrrpLagPortDownEventHoldSet_Type(TmnxEventHoldSet):
    """Custom type tmnxVrrpLagPortDownEventHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TmnxVrrpLagPortDownEventHoldSet_Object = MibTableColumn
tmnxVrrpLagPortDownEventHoldSet = _TmnxVrrpLagPortDownEventHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 3),
    _TmnxVrrpLagPortDownEventHoldSet_Type()
)
tmnxVrrpLagPortDownEventHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldSet.setUnits("seconds")
_TmnxVrrpLagPortDownEventOperState_Type = TmnxLagPortDownEventOperState
_TmnxVrrpLagPortDownEventOperState_Object = MibTableColumn
tmnxVrrpLagPortDownEventOperState = _TmnxVrrpLagPortDownEventOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 4),
    _TmnxVrrpLagPortDownEventOperState_Type()
)
tmnxVrrpLagPortDownEventOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventOperState.setStatus("current")
_TmnxVrrpLagPortDownEventHoldSetRemaining_Type = TmnxEventHoldSet
_TmnxVrrpLagPortDownEventHoldSetRemaining_Object = MibTableColumn
tmnxVrrpLagPortDownEventHoldSetRemaining = _TmnxVrrpLagPortDownEventHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 5),
    _TmnxVrrpLagPortDownEventHoldSetRemaining_Type()
)
tmnxVrrpLagPortDownEventHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldSetRemaining.setUnits("seconds")
_TmnxVrrpLagPortDownEventPrevState_Type = TmnxLagPortDownEventOperState
_TmnxVrrpLagPortDownEventPrevState_Object = MibTableColumn
tmnxVrrpLagPortDownEventPrevState = _TmnxVrrpLagPortDownEventPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 6),
    _TmnxVrrpLagPortDownEventPrevState_Type()
)
tmnxVrrpLagPortDownEventPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventPrevState.setStatus("current")
_TmnxVrrpLagPortDownEventLastTransition_Type = TimeStamp
_TmnxVrrpLagPortDownEventLastTransition_Object = MibTableColumn
tmnxVrrpLagPortDownEventLastTransition = _TmnxVrrpLagPortDownEventLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 7),
    _TmnxVrrpLagPortDownEventLastTransition_Type()
)
tmnxVrrpLagPortDownEventLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventLastTransition.setStatus("current")
_TmnxVrrpLagPortDownEventSetCounter_Type = Counter32
_TmnxVrrpLagPortDownEventSetCounter_Object = MibTableColumn
tmnxVrrpLagPortDownEventSetCounter = _TmnxVrrpLagPortDownEventSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 8),
    _TmnxVrrpLagPortDownEventSetCounter_Type()
)
tmnxVrrpLagPortDownEventSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventSetCounter.setStatus("current")
_TmnxVrrpLagPortDownEventInUse_Type = TruthValue
_TmnxVrrpLagPortDownEventInUse_Object = MibTableColumn
tmnxVrrpLagPortDownEventInUse = _TmnxVrrpLagPortDownEventInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 9),
    _TmnxVrrpLagPortDownEventInUse_Type()
)
tmnxVrrpLagPortDownEventInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventInUse.setStatus("current")


class _TmnxVrrpLagPortDownEventHoldClear_Type(TmnxEventHoldClear):
    """Custom type tmnxVrrpLagPortDownEventHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TmnxVrrpLagPortDownEventHoldClear_Object = MibTableColumn
tmnxVrrpLagPortDownEventHoldClear = _TmnxVrrpLagPortDownEventHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 10),
    _TmnxVrrpLagPortDownEventHoldClear_Type()
)
tmnxVrrpLagPortDownEventHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldClear.setUnits("seconds")
_TmnxVrrpLagPortDownEventHoldClearRemaining_Type = TmnxEventHoldClear
_TmnxVrrpLagPortDownEventHoldClearRemaining_Object = MibTableColumn
tmnxVrrpLagPortDownEventHoldClearRemaining = _TmnxVrrpLagPortDownEventHoldClearRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 3, 1, 11),
    _TmnxVrrpLagPortDownEventHoldClearRemaining_Type()
)
tmnxVrrpLagPortDownEventHoldClearRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldClearRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpLagPortDownEventHoldClearRemaining.setUnits("seconds")
_TmnxVrrpLagNumberDownEventTable_Object = MibTable
tmnxVrrpLagNumberDownEventTable = _TmnxVrrpLagNumberDownEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDownEventTable.setStatus("current")
_TmnxVrrpLagNumberDownEventEntry_Object = MibTableRow
tmnxVrrpLagNumberDownEventEntry = _TmnxVrrpLagNumberDownEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4, 1)
)
tmnxVrrpLagNumberDownEventEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventLagId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpLagNumberDown"),
)
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDownEventEntry.setStatus("current")
_TmnxVrrpLagNumberDown_Type = Unsigned32
_TmnxVrrpLagNumberDown_Object = MibTableColumn
tmnxVrrpLagNumberDown = _TmnxVrrpLagNumberDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4, 1, 1),
    _TmnxVrrpLagNumberDown_Type()
)
tmnxVrrpLagNumberDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDown.setStatus("current")
_TmnxVrrpLagNumberDownEventRowStatus_Type = RowStatus
_TmnxVrrpLagNumberDownEventRowStatus_Object = MibTableColumn
tmnxVrrpLagNumberDownEventRowStatus = _TmnxVrrpLagNumberDownEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4, 1, 2),
    _TmnxVrrpLagNumberDownEventRowStatus_Type()
)
tmnxVrrpLagNumberDownEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDownEventRowStatus.setStatus("current")


class _TmnxVrrpLagNumberDownEventPriority_Type(TmnxVrrpPriority):
    """Custom type tmnxVrrpLagNumberDownEventPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TmnxVrrpLagNumberDownEventPriority_Object = MibTableColumn
tmnxVrrpLagNumberDownEventPriority = _TmnxVrrpLagNumberDownEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4, 1, 3),
    _TmnxVrrpLagNumberDownEventPriority_Type()
)
tmnxVrrpLagNumberDownEventPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDownEventPriority.setStatus("current")


class _TmnxVrrpLagNumberDownEventType_Type(TmnxEventType):
    """Custom type tmnxVrrpLagNumberDownEventType based on TmnxEventType"""


_TmnxVrrpLagNumberDownEventType_Object = MibTableColumn
tmnxVrrpLagNumberDownEventType = _TmnxVrrpLagNumberDownEventType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 4, 1, 4),
    _TmnxVrrpLagNumberDownEventType_Type()
)
tmnxVrrpLagNumberDownEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpLagNumberDownEventType.setStatus("current")
_TmnxVrrpHostUnreachableEventTable_Object = MibTable
tmnxVrrpHostUnreachableEventTable = _TmnxVrrpHostUnreachableEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventTable.setStatus("current")
_TmnxVrrpHostUnreachableEventEntry_Object = MibTableRow
tmnxVrrpHostUnreachableEventEntry = _TmnxVrrpHostUnreachableEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1)
)
tmnxVrrpHostUnreachableEventEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventEntry.setStatus("current")
_TmnxVrrpHostUnreachableEventIpAddr_Type = IpAddress
_TmnxVrrpHostUnreachableEventIpAddr_Object = MibTableColumn
tmnxVrrpHostUnreachableEventIpAddr = _TmnxVrrpHostUnreachableEventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 1),
    _TmnxVrrpHostUnreachableEventIpAddr_Type()
)
tmnxVrrpHostUnreachableEventIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventIpAddr.setStatus("current")
_TmnxVrrpHostUnreachableEventRowStatus_Type = RowStatus
_TmnxVrrpHostUnreachableEventRowStatus_Object = MibTableColumn
tmnxVrrpHostUnreachableEventRowStatus = _TmnxVrrpHostUnreachableEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 2),
    _TmnxVrrpHostUnreachableEventRowStatus_Type()
)
tmnxVrrpHostUnreachableEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventRowStatus.setStatus("current")


class _TmnxVrrpHostUnreachableEventPriority_Type(TmnxVrrpPriority):
    """Custom type tmnxVrrpHostUnreachableEventPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TmnxVrrpHostUnreachableEventPriority_Object = MibTableColumn
tmnxVrrpHostUnreachableEventPriority = _TmnxVrrpHostUnreachableEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 3),
    _TmnxVrrpHostUnreachableEventPriority_Type()
)
tmnxVrrpHostUnreachableEventPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventPriority.setStatus("current")


class _TmnxVrrpHostUnreachableEventType_Type(TmnxEventType):
    """Custom type tmnxVrrpHostUnreachableEventType based on TmnxEventType"""


_TmnxVrrpHostUnreachableEventType_Object = MibTableColumn
tmnxVrrpHostUnreachableEventType = _TmnxVrrpHostUnreachableEventType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 4),
    _TmnxVrrpHostUnreachableEventType_Type()
)
tmnxVrrpHostUnreachableEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventType.setStatus("current")


class _TmnxVrrpHostUnreachableEventHoldSet_Type(TmnxEventHoldSet):
    """Custom type tmnxVrrpHostUnreachableEventHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TmnxVrrpHostUnreachableEventHoldSet_Object = MibTableColumn
tmnxVrrpHostUnreachableEventHoldSet = _TmnxVrrpHostUnreachableEventHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 5),
    _TmnxVrrpHostUnreachableEventHoldSet_Type()
)
tmnxVrrpHostUnreachableEventHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldSet.setUnits("seconds")


class _TmnxVrrpHostUnreachableEventInterval_Type(Unsigned32):
    """Custom type tmnxVrrpHostUnreachableEventInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxVrrpHostUnreachableEventInterval_Type.__name__ = "Unsigned32"
_TmnxVrrpHostUnreachableEventInterval_Object = MibTableColumn
tmnxVrrpHostUnreachableEventInterval = _TmnxVrrpHostUnreachableEventInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 6),
    _TmnxVrrpHostUnreachableEventInterval_Type()
)
tmnxVrrpHostUnreachableEventInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventInterval.setUnits("seconds")


class _TmnxVrrpHostUnreachableEventTimeout_Type(Unsigned32):
    """Custom type tmnxVrrpHostUnreachableEventTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxVrrpHostUnreachableEventTimeout_Type.__name__ = "Unsigned32"
_TmnxVrrpHostUnreachableEventTimeout_Object = MibTableColumn
tmnxVrrpHostUnreachableEventTimeout = _TmnxVrrpHostUnreachableEventTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 7),
    _TmnxVrrpHostUnreachableEventTimeout_Type()
)
tmnxVrrpHostUnreachableEventTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventTimeout.setUnits("seconds")


class _TmnxVrrpHostUnreachableEventDropCount_Type(Unsigned32):
    """Custom type tmnxVrrpHostUnreachableEventDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxVrrpHostUnreachableEventDropCount_Type.__name__ = "Unsigned32"
_TmnxVrrpHostUnreachableEventDropCount_Object = MibTableColumn
tmnxVrrpHostUnreachableEventDropCount = _TmnxVrrpHostUnreachableEventDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 8),
    _TmnxVrrpHostUnreachableEventDropCount_Type()
)
tmnxVrrpHostUnreachableEventDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventDropCount.setStatus("current")
_TmnxVrrpHostUnreachableEventOperState_Type = TmnxHostUnreachableEventOperState
_TmnxVrrpHostUnreachableEventOperState_Object = MibTableColumn
tmnxVrrpHostUnreachableEventOperState = _TmnxVrrpHostUnreachableEventOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 9),
    _TmnxVrrpHostUnreachableEventOperState_Type()
)
tmnxVrrpHostUnreachableEventOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventOperState.setStatus("current")
_TmnxVrrpHostUnreachableEventHoldSetRemaining_Type = TmnxEventHoldSet
_TmnxVrrpHostUnreachableEventHoldSetRemaining_Object = MibTableColumn
tmnxVrrpHostUnreachableEventHoldSetRemaining = _TmnxVrrpHostUnreachableEventHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 10),
    _TmnxVrrpHostUnreachableEventHoldSetRemaining_Type()
)
tmnxVrrpHostUnreachableEventHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldSetRemaining.setUnits("seconds")
_TmnxVrrpHostUnreachableEventPrevState_Type = TmnxHostUnreachableEventOperState
_TmnxVrrpHostUnreachableEventPrevState_Object = MibTableColumn
tmnxVrrpHostUnreachableEventPrevState = _TmnxVrrpHostUnreachableEventPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 11),
    _TmnxVrrpHostUnreachableEventPrevState_Type()
)
tmnxVrrpHostUnreachableEventPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventPrevState.setStatus("current")
_TmnxVrrpHostUnreachableEventLastTransition_Type = TimeStamp
_TmnxVrrpHostUnreachableEventLastTransition_Object = MibTableColumn
tmnxVrrpHostUnreachableEventLastTransition = _TmnxVrrpHostUnreachableEventLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 12),
    _TmnxVrrpHostUnreachableEventLastTransition_Type()
)
tmnxVrrpHostUnreachableEventLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventLastTransition.setStatus("current")
_TmnxVrrpHostUnreachableEventSetCounter_Type = Counter32
_TmnxVrrpHostUnreachableEventSetCounter_Object = MibTableColumn
tmnxVrrpHostUnreachableEventSetCounter = _TmnxVrrpHostUnreachableEventSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 13),
    _TmnxVrrpHostUnreachableEventSetCounter_Type()
)
tmnxVrrpHostUnreachableEventSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventSetCounter.setStatus("current")
_TmnxVrrpHostUnreachableEventInUse_Type = TruthValue
_TmnxVrrpHostUnreachableEventInUse_Object = MibTableColumn
tmnxVrrpHostUnreachableEventInUse = _TmnxVrrpHostUnreachableEventInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 14),
    _TmnxVrrpHostUnreachableEventInUse_Type()
)
tmnxVrrpHostUnreachableEventInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventInUse.setStatus("current")


class _TmnxVrrpHostUnreachableEventHoldClear_Type(TmnxEventHoldClear):
    """Custom type tmnxVrrpHostUnreachableEventHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TmnxVrrpHostUnreachableEventHoldClear_Object = MibTableColumn
tmnxVrrpHostUnreachableEventHoldClear = _TmnxVrrpHostUnreachableEventHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 15),
    _TmnxVrrpHostUnreachableEventHoldClear_Type()
)
tmnxVrrpHostUnreachableEventHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldClear.setUnits("seconds")
_TmnxVrrpHostUnreachableEventHoldClearRemaining_Type = TmnxEventHoldClear
_TmnxVrrpHostUnreachableEventHoldClearRemaining_Object = MibTableColumn
tmnxVrrpHostUnreachableEventHoldClearRemaining = _TmnxVrrpHostUnreachableEventHoldClearRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 5, 1, 16),
    _TmnxVrrpHostUnreachableEventHoldClearRemaining_Type()
)
tmnxVrrpHostUnreachableEventHoldClearRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldClearRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpHostUnreachableEventHoldClearRemaining.setUnits("seconds")
_TmnxVrrpRouteUnknownEventTable_Object = MibTable
tmnxVrrpRouteUnknownEventTable = _TmnxVrrpRouteUnknownEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventTable.setStatus("current")
_TmnxVrrpRouteUnknownEventEntry_Object = MibTableRow
tmnxVrrpRouteUnknownEventEntry = _TmnxVrrpRouteUnknownEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1)
)
tmnxVrrpRouteUnknownEventEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventPrefix"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventMaskLen"),
)
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventEntry.setStatus("current")
_TmnxVrrpRouteUnknownEventPrefix_Type = IpAddress
_TmnxVrrpRouteUnknownEventPrefix_Object = MibTableColumn
tmnxVrrpRouteUnknownEventPrefix = _TmnxVrrpRouteUnknownEventPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 1),
    _TmnxVrrpRouteUnknownEventPrefix_Type()
)
tmnxVrrpRouteUnknownEventPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventPrefix.setStatus("current")


class _TmnxVrrpRouteUnknownEventMaskLen_Type(Unsigned32):
    """Custom type tmnxVrrpRouteUnknownEventMaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxVrrpRouteUnknownEventMaskLen_Type.__name__ = "Unsigned32"
_TmnxVrrpRouteUnknownEventMaskLen_Object = MibTableColumn
tmnxVrrpRouteUnknownEventMaskLen = _TmnxVrrpRouteUnknownEventMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 2),
    _TmnxVrrpRouteUnknownEventMaskLen_Type()
)
tmnxVrrpRouteUnknownEventMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventMaskLen.setStatus("current")
_TmnxVrrpRouteUnknownEventRowStatus_Type = RowStatus
_TmnxVrrpRouteUnknownEventRowStatus_Object = MibTableColumn
tmnxVrrpRouteUnknownEventRowStatus = _TmnxVrrpRouteUnknownEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 3),
    _TmnxVrrpRouteUnknownEventRowStatus_Type()
)
tmnxVrrpRouteUnknownEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventRowStatus.setStatus("current")


class _TmnxVrrpRouteUnknownEventPriority_Type(TmnxVrrpPriority):
    """Custom type tmnxVrrpRouteUnknownEventPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TmnxVrrpRouteUnknownEventPriority_Object = MibTableColumn
tmnxVrrpRouteUnknownEventPriority = _TmnxVrrpRouteUnknownEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 4),
    _TmnxVrrpRouteUnknownEventPriority_Type()
)
tmnxVrrpRouteUnknownEventPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventPriority.setStatus("current")


class _TmnxVrrpRouteUnknownEventType_Type(TmnxEventType):
    """Custom type tmnxVrrpRouteUnknownEventType based on TmnxEventType"""


_TmnxVrrpRouteUnknownEventType_Object = MibTableColumn
tmnxVrrpRouteUnknownEventType = _TmnxVrrpRouteUnknownEventType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 5),
    _TmnxVrrpRouteUnknownEventType_Type()
)
tmnxVrrpRouteUnknownEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventType.setStatus("current")


class _TmnxVrrpRouteUnknownEventHoldSet_Type(TmnxEventHoldSet):
    """Custom type tmnxVrrpRouteUnknownEventHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TmnxVrrpRouteUnknownEventHoldSet_Object = MibTableColumn
tmnxVrrpRouteUnknownEventHoldSet = _TmnxVrrpRouteUnknownEventHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 6),
    _TmnxVrrpRouteUnknownEventHoldSet_Type()
)
tmnxVrrpRouteUnknownEventHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldSet.setUnits("seconds")


class _TmnxVrrpRouteUnknownEventLessSpecific_Type(TruthValue):
    """Custom type tmnxVrrpRouteUnknownEventLessSpecific based on TruthValue"""


_TmnxVrrpRouteUnknownEventLessSpecific_Object = MibTableColumn
tmnxVrrpRouteUnknownEventLessSpecific = _TmnxVrrpRouteUnknownEventLessSpecific_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 7),
    _TmnxVrrpRouteUnknownEventLessSpecific_Type()
)
tmnxVrrpRouteUnknownEventLessSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventLessSpecific.setStatus("current")


class _TmnxVrrpRouteUnknownEventDefaultAllowed_Type(TruthValue):
    """Custom type tmnxVrrpRouteUnknownEventDefaultAllowed based on TruthValue"""


_TmnxVrrpRouteUnknownEventDefaultAllowed_Object = MibTableColumn
tmnxVrrpRouteUnknownEventDefaultAllowed = _TmnxVrrpRouteUnknownEventDefaultAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 8),
    _TmnxVrrpRouteUnknownEventDefaultAllowed_Type()
)
tmnxVrrpRouteUnknownEventDefaultAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventDefaultAllowed.setStatus("current")


class _TmnxVrrpRouteUnknownEventProtocol_Type(Bits):
    """Custom type tmnxVrrpRouteUnknownEventProtocol based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bgp", 0),
          ("bgpVpn", 5),
          ("isis", 2),
          ("ospf", 1),
          ("rip", 3),
          ("static", 4))
    )

_TmnxVrrpRouteUnknownEventProtocol_Type.__name__ = "Bits"
_TmnxVrrpRouteUnknownEventProtocol_Object = MibTableColumn
tmnxVrrpRouteUnknownEventProtocol = _TmnxVrrpRouteUnknownEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 9),
    _TmnxVrrpRouteUnknownEventProtocol_Type()
)
tmnxVrrpRouteUnknownEventProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventProtocol.setStatus("current")
_TmnxVrrpRouteUnknownEventOperState_Type = TmnxRouteUnknownEventOperState
_TmnxVrrpRouteUnknownEventOperState_Object = MibTableColumn
tmnxVrrpRouteUnknownEventOperState = _TmnxVrrpRouteUnknownEventOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 10),
    _TmnxVrrpRouteUnknownEventOperState_Type()
)
tmnxVrrpRouteUnknownEventOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventOperState.setStatus("current")
_TmnxVrrpRouteUnknownEventHoldSetRemaining_Type = TmnxEventHoldSet
_TmnxVrrpRouteUnknownEventHoldSetRemaining_Object = MibTableColumn
tmnxVrrpRouteUnknownEventHoldSetRemaining = _TmnxVrrpRouteUnknownEventHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 11),
    _TmnxVrrpRouteUnknownEventHoldSetRemaining_Type()
)
tmnxVrrpRouteUnknownEventHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldSetRemaining.setUnits("seconds")
_TmnxVrrpRouteUnknownEventPrevState_Type = TmnxRouteUnknownEventOperState
_TmnxVrrpRouteUnknownEventPrevState_Object = MibTableColumn
tmnxVrrpRouteUnknownEventPrevState = _TmnxVrrpRouteUnknownEventPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 12),
    _TmnxVrrpRouteUnknownEventPrevState_Type()
)
tmnxVrrpRouteUnknownEventPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventPrevState.setStatus("current")
_TmnxVrrpRouteUnknownEventLastTransition_Type = TimeStamp
_TmnxVrrpRouteUnknownEventLastTransition_Object = MibTableColumn
tmnxVrrpRouteUnknownEventLastTransition = _TmnxVrrpRouteUnknownEventLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 13),
    _TmnxVrrpRouteUnknownEventLastTransition_Type()
)
tmnxVrrpRouteUnknownEventLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventLastTransition.setStatus("current")
_TmnxVrrpRouteUnknownEventSetCounter_Type = Counter32
_TmnxVrrpRouteUnknownEventSetCounter_Object = MibTableColumn
tmnxVrrpRouteUnknownEventSetCounter = _TmnxVrrpRouteUnknownEventSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 14),
    _TmnxVrrpRouteUnknownEventSetCounter_Type()
)
tmnxVrrpRouteUnknownEventSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventSetCounter.setStatus("current")
_TmnxVrrpRouteUnknownEventInUse_Type = TruthValue
_TmnxVrrpRouteUnknownEventInUse_Object = MibTableColumn
tmnxVrrpRouteUnknownEventInUse = _TmnxVrrpRouteUnknownEventInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 15),
    _TmnxVrrpRouteUnknownEventInUse_Type()
)
tmnxVrrpRouteUnknownEventInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventInUse.setStatus("current")


class _TmnxVrrpRouteUnknownEventHoldClear_Type(TmnxEventHoldClear):
    """Custom type tmnxVrrpRouteUnknownEventHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TmnxVrrpRouteUnknownEventHoldClear_Object = MibTableColumn
tmnxVrrpRouteUnknownEventHoldClear = _TmnxVrrpRouteUnknownEventHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 16),
    _TmnxVrrpRouteUnknownEventHoldClear_Type()
)
tmnxVrrpRouteUnknownEventHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldClear.setUnits("seconds")
_TmnxVrrpRouteUnknownEventHoldClearRemaining_Type = TmnxEventHoldClear
_TmnxVrrpRouteUnknownEventHoldClearRemaining_Object = MibTableColumn
tmnxVrrpRouteUnknownEventHoldClearRemaining = _TmnxVrrpRouteUnknownEventHoldClearRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 6, 1, 17),
    _TmnxVrrpRouteUnknownEventHoldClearRemaining_Type()
)
tmnxVrrpRouteUnknownEventHoldClearRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldClearRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventHoldClearRemaining.setUnits("seconds")
_TmnxVrrpRouteUnknownEventNextHopTable_Object = MibTable
tmnxVrrpRouteUnknownEventNextHopTable = _TmnxVrrpRouteUnknownEventNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventNextHopTable.setStatus("current")
_TmnxVrrpRouteUnknownEventNextHopEntry_Object = MibTableRow
tmnxVrrpRouteUnknownEventNextHopEntry = _TmnxVrrpRouteUnknownEventNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 7, 1)
)
tmnxVrrpRouteUnknownEventNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventPrefix"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventMaskLen"),
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventNextHop"),
)
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventNextHopEntry.setStatus("current")
_TmnxVrrpRouteUnknownEventNextHop_Type = IpAddress
_TmnxVrrpRouteUnknownEventNextHop_Object = MibTableColumn
tmnxVrrpRouteUnknownEventNextHop = _TmnxVrrpRouteUnknownEventNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 7, 1, 1),
    _TmnxVrrpRouteUnknownEventNextHop_Type()
)
tmnxVrrpRouteUnknownEventNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventNextHop.setStatus("current")
_TmnxVrrpRouteUnknownEventNextHopRowStatus_Type = RowStatus
_TmnxVrrpRouteUnknownEventNextHopRowStatus_Object = MibTableColumn
tmnxVrrpRouteUnknownEventNextHopRowStatus = _TmnxVrrpRouteUnknownEventNextHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 7, 1, 2),
    _TmnxVrrpRouteUnknownEventNextHopRowStatus_Type()
)
tmnxVrrpRouteUnknownEventNextHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVrrpRouteUnknownEventNextHopRowStatus.setStatus("current")
_TVrrpHstUnrchEvtTblLastChgd_Type = TimeStamp
_TVrrpHstUnrchEvtTblLastChgd_Object = MibScalar
tVrrpHstUnrchEvtTblLastChgd = _TVrrpHstUnrchEvtTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 8),
    _TVrrpHstUnrchEvtTblLastChgd_Type()
)
tVrrpHstUnrchEvtTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtTblLastChgd.setStatus("current")
_TVrrpHstUnrchEvtTable_Object = MibTable
tVrrpHstUnrchEvtTable = _TVrrpHstUnrchEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9)
)
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtTable.setStatus("current")
_TVrrpHstUnrchEvtEntry_Object = MibTableRow
tVrrpHstUnrchEvtEntry = _TVrrpHstUnrchEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1)
)
tVrrpHstUnrchEvtEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtAddrType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtIpAddr"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtIfName"),
)
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtEntry.setStatus("current")
_TVrrpHstUnrchEvtAddrType_Type = InetAddressType
_TVrrpHstUnrchEvtAddrType_Object = MibTableColumn
tVrrpHstUnrchEvtAddrType = _TVrrpHstUnrchEvtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 1),
    _TVrrpHstUnrchEvtAddrType_Type()
)
tVrrpHstUnrchEvtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtAddrType.setStatus("current")


class _TVrrpHstUnrchEvtIpAddr_Type(InetAddress):
    """Custom type tVrrpHstUnrchEvtIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TVrrpHstUnrchEvtIpAddr_Type.__name__ = "InetAddress"
_TVrrpHstUnrchEvtIpAddr_Object = MibTableColumn
tVrrpHstUnrchEvtIpAddr = _TVrrpHstUnrchEvtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 2),
    _TVrrpHstUnrchEvtIpAddr_Type()
)
tVrrpHstUnrchEvtIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtIpAddr.setStatus("current")
_TVrrpHstUnrchEvtIfName_Type = TNamedItemOrEmpty
_TVrrpHstUnrchEvtIfName_Object = MibTableColumn
tVrrpHstUnrchEvtIfName = _TVrrpHstUnrchEvtIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 3),
    _TVrrpHstUnrchEvtIfName_Type()
)
tVrrpHstUnrchEvtIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtIfName.setStatus("current")
_TVrrpHstUnrchEvtRowStatus_Type = RowStatus
_TVrrpHstUnrchEvtRowStatus_Object = MibTableColumn
tVrrpHstUnrchEvtRowStatus = _TVrrpHstUnrchEvtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 4),
    _TVrrpHstUnrchEvtRowStatus_Type()
)
tVrrpHstUnrchEvtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtRowStatus.setStatus("current")


class _TVrrpHstUnrchEvtPriority_Type(TmnxVrrpPriority):
    """Custom type tVrrpHstUnrchEvtPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TVrrpHstUnrchEvtPriority_Object = MibTableColumn
tVrrpHstUnrchEvtPriority = _TVrrpHstUnrchEvtPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 5),
    _TVrrpHstUnrchEvtPriority_Type()
)
tVrrpHstUnrchEvtPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtPriority.setStatus("current")


class _TVrrpHstUnrchEvtType_Type(TmnxEventType):
    """Custom type tVrrpHstUnrchEvtType based on TmnxEventType"""


_TVrrpHstUnrchEvtType_Object = MibTableColumn
tVrrpHstUnrchEvtType = _TVrrpHstUnrchEvtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 6),
    _TVrrpHstUnrchEvtType_Type()
)
tVrrpHstUnrchEvtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtType.setStatus("current")


class _TVrrpHstUnrchEvtHoldSet_Type(TmnxEventHoldSet):
    """Custom type tVrrpHstUnrchEvtHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TVrrpHstUnrchEvtHoldSet_Object = MibTableColumn
tVrrpHstUnrchEvtHoldSet = _TVrrpHstUnrchEvtHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 7),
    _TVrrpHstUnrchEvtHoldSet_Type()
)
tVrrpHstUnrchEvtHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldSet.setUnits("seconds")


class _TVrrpHstUnrchEvtInterval_Type(Unsigned32):
    """Custom type tVrrpHstUnrchEvtInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TVrrpHstUnrchEvtInterval_Type.__name__ = "Unsigned32"
_TVrrpHstUnrchEvtInterval_Object = MibTableColumn
tVrrpHstUnrchEvtInterval = _TVrrpHstUnrchEvtInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 8),
    _TVrrpHstUnrchEvtInterval_Type()
)
tVrrpHstUnrchEvtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtInterval.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtInterval.setUnits("seconds")


class _TVrrpHstUnrchEvtTimeout_Type(Unsigned32):
    """Custom type tVrrpHstUnrchEvtTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TVrrpHstUnrchEvtTimeout_Type.__name__ = "Unsigned32"
_TVrrpHstUnrchEvtTimeout_Object = MibTableColumn
tVrrpHstUnrchEvtTimeout = _TVrrpHstUnrchEvtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 9),
    _TVrrpHstUnrchEvtTimeout_Type()
)
tVrrpHstUnrchEvtTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtTimeout.setUnits("seconds")


class _TVrrpHstUnrchEvtDropCount_Type(Unsigned32):
    """Custom type tVrrpHstUnrchEvtDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TVrrpHstUnrchEvtDropCount_Type.__name__ = "Unsigned32"
_TVrrpHstUnrchEvtDropCount_Object = MibTableColumn
tVrrpHstUnrchEvtDropCount = _TVrrpHstUnrchEvtDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 10),
    _TVrrpHstUnrchEvtDropCount_Type()
)
tVrrpHstUnrchEvtDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtDropCount.setStatus("current")
_TVrrpHstUnrchEvtOperState_Type = TmnxHostUnreachableEventOperState
_TVrrpHstUnrchEvtOperState_Object = MibTableColumn
tVrrpHstUnrchEvtOperState = _TVrrpHstUnrchEvtOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 11),
    _TVrrpHstUnrchEvtOperState_Type()
)
tVrrpHstUnrchEvtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtOperState.setStatus("current")
_TVrrpHstUnrchEvtHoldSetRemaining_Type = TmnxEventHoldSet
_TVrrpHstUnrchEvtHoldSetRemaining_Object = MibTableColumn
tVrrpHstUnrchEvtHoldSetRemaining = _TVrrpHstUnrchEvtHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 12),
    _TVrrpHstUnrchEvtHoldSetRemaining_Type()
)
tVrrpHstUnrchEvtHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldSetRemaining.setUnits("seconds")
_TVrrpHstUnrchEvtPrevState_Type = TmnxHostUnreachableEventOperState
_TVrrpHstUnrchEvtPrevState_Object = MibTableColumn
tVrrpHstUnrchEvtPrevState = _TVrrpHstUnrchEvtPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 13),
    _TVrrpHstUnrchEvtPrevState_Type()
)
tVrrpHstUnrchEvtPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtPrevState.setStatus("current")
_TVrrpHstUnrchEvtLastTransition_Type = TimeStamp
_TVrrpHstUnrchEvtLastTransition_Object = MibTableColumn
tVrrpHstUnrchEvtLastTransition = _TVrrpHstUnrchEvtLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 14),
    _TVrrpHstUnrchEvtLastTransition_Type()
)
tVrrpHstUnrchEvtLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtLastTransition.setStatus("current")
_TVrrpHstUnrchEvtSetCounter_Type = Counter32
_TVrrpHstUnrchEvtSetCounter_Object = MibTableColumn
tVrrpHstUnrchEvtSetCounter = _TVrrpHstUnrchEvtSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 15),
    _TVrrpHstUnrchEvtSetCounter_Type()
)
tVrrpHstUnrchEvtSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtSetCounter.setStatus("current")
_TVrrpHstUnrchEvtInUse_Type = TruthValue
_TVrrpHstUnrchEvtInUse_Object = MibTableColumn
tVrrpHstUnrchEvtInUse = _TVrrpHstUnrchEvtInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 16),
    _TVrrpHstUnrchEvtInUse_Type()
)
tVrrpHstUnrchEvtInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtInUse.setStatus("current")


class _TVrrpHstUnrchEvtHoldClear_Type(TmnxEventHoldClear):
    """Custom type tVrrpHstUnrchEvtHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TVrrpHstUnrchEvtHoldClear_Object = MibTableColumn
tVrrpHstUnrchEvtHoldClear = _TVrrpHstUnrchEvtHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 17),
    _TVrrpHstUnrchEvtHoldClear_Type()
)
tVrrpHstUnrchEvtHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHoldClear.setUnits("seconds")
_TVrrpHstUnrchEvtHldClrRemain_Type = TmnxEventHoldClear
_TVrrpHstUnrchEvtHldClrRemain_Object = MibTableColumn
tVrrpHstUnrchEvtHldClrRemain = _TVrrpHstUnrchEvtHldClrRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 18),
    _TVrrpHstUnrchEvtHldClrRemain_Type()
)
tVrrpHstUnrchEvtHldClrRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHldClrRemain.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtHldClrRemain.setUnits("seconds")
_TVrrpHstUnrchEvtLastChgd_Type = TimeStamp
_TVrrpHstUnrchEvtLastChgd_Object = MibTableColumn
tVrrpHstUnrchEvtLastChgd = _TVrrpHstUnrchEvtLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 9, 1, 19),
    _TVrrpHstUnrchEvtLastChgd_Type()
)
tVrrpHstUnrchEvtLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpHstUnrchEvtLastChgd.setStatus("current")
_TVrrpRtUnknEvtTblLastChgd_Type = TimeStamp
_TVrrpRtUnknEvtTblLastChgd_Object = MibScalar
tVrrpRtUnknEvtTblLastChgd = _TVrrpRtUnknEvtTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 10),
    _TVrrpRtUnknEvtTblLastChgd_Type()
)
tVrrpRtUnknEvtTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtTblLastChgd.setStatus("current")
_TVrrpRtUnknEvtTable_Object = MibTable
tVrrpRtUnknEvtTable = _TVrrpRtUnknEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11)
)
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtTable.setStatus("current")
_TVrrpRtUnknEvtEntry_Object = MibTableRow
tVrrpRtUnknEvtEntry = _TVrrpRtUnknEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1)
)
tVrrpRtUnknEvtEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPrefixType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPrefix"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtMaskLen"),
)
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtEntry.setStatus("current")
_TVrrpRtUnknEvtPrefixType_Type = InetAddressType
_TVrrpRtUnknEvtPrefixType_Object = MibTableColumn
tVrrpRtUnknEvtPrefixType = _TVrrpRtUnknEvtPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 1),
    _TVrrpRtUnknEvtPrefixType_Type()
)
tVrrpRtUnknEvtPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtPrefixType.setStatus("current")


class _TVrrpRtUnknEvtPrefix_Type(InetAddress):
    """Custom type tVrrpRtUnknEvtPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TVrrpRtUnknEvtPrefix_Type.__name__ = "InetAddress"
_TVrrpRtUnknEvtPrefix_Object = MibTableColumn
tVrrpRtUnknEvtPrefix = _TVrrpRtUnknEvtPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 2),
    _TVrrpRtUnknEvtPrefix_Type()
)
tVrrpRtUnknEvtPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtPrefix.setStatus("current")
_TVrrpRtUnknEvtMaskLen_Type = InetAddressPrefixLength
_TVrrpRtUnknEvtMaskLen_Object = MibTableColumn
tVrrpRtUnknEvtMaskLen = _TVrrpRtUnknEvtMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 3),
    _TVrrpRtUnknEvtMaskLen_Type()
)
tVrrpRtUnknEvtMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtMaskLen.setStatus("current")
_TVrrpRtUnknEvtRowStatus_Type = RowStatus
_TVrrpRtUnknEvtRowStatus_Object = MibTableColumn
tVrrpRtUnknEvtRowStatus = _TVrrpRtUnknEvtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 4),
    _TVrrpRtUnknEvtRowStatus_Type()
)
tVrrpRtUnknEvtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtRowStatus.setStatus("current")


class _TVrrpRtUnknEvtPriority_Type(TmnxVrrpPriority):
    """Custom type tVrrpRtUnknEvtPriority based on TmnxVrrpPriority"""
    defaultValue = 0


_TVrrpRtUnknEvtPriority_Object = MibTableColumn
tVrrpRtUnknEvtPriority = _TVrrpRtUnknEvtPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 5),
    _TVrrpRtUnknEvtPriority_Type()
)
tVrrpRtUnknEvtPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtPriority.setStatus("current")


class _TVrrpRtUnknEvtType_Type(TmnxEventType):
    """Custom type tVrrpRtUnknEvtType based on TmnxEventType"""


_TVrrpRtUnknEvtType_Object = MibTableColumn
tVrrpRtUnknEvtType = _TVrrpRtUnknEvtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 6),
    _TVrrpRtUnknEvtType_Type()
)
tVrrpRtUnknEvtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtType.setStatus("current")


class _TVrrpRtUnknEvtHoldSet_Type(TmnxEventHoldSet):
    """Custom type tVrrpRtUnknEvtHoldSet based on TmnxEventHoldSet"""
    defaultValue = 0


_TVrrpRtUnknEvtHoldSet_Object = MibTableColumn
tVrrpRtUnknEvtHoldSet = _TVrrpRtUnknEvtHoldSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 7),
    _TVrrpRtUnknEvtHoldSet_Type()
)
tVrrpRtUnknEvtHoldSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldSet.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldSet.setUnits("seconds")


class _TVrrpRtUnknEvtLessSpecific_Type(TruthValue):
    """Custom type tVrrpRtUnknEvtLessSpecific based on TruthValue"""


_TVrrpRtUnknEvtLessSpecific_Object = MibTableColumn
tVrrpRtUnknEvtLessSpecific = _TVrrpRtUnknEvtLessSpecific_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 8),
    _TVrrpRtUnknEvtLessSpecific_Type()
)
tVrrpRtUnknEvtLessSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtLessSpecific.setStatus("current")


class _TVrrpRtUnknEvtDefaultAllowed_Type(TruthValue):
    """Custom type tVrrpRtUnknEvtDefaultAllowed based on TruthValue"""


_TVrrpRtUnknEvtDefaultAllowed_Object = MibTableColumn
tVrrpRtUnknEvtDefaultAllowed = _TVrrpRtUnknEvtDefaultAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 9),
    _TVrrpRtUnknEvtDefaultAllowed_Type()
)
tVrrpRtUnknEvtDefaultAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtDefaultAllowed.setStatus("current")


class _TVrrpRtUnknEvtProtocol_Type(Bits):
    """Custom type tVrrpRtUnknEvtProtocol based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bgp", 0),
          ("bgpVpn", 5),
          ("isis", 2),
          ("ospf", 1),
          ("rip", 3),
          ("static", 4))
    )

_TVrrpRtUnknEvtProtocol_Type.__name__ = "Bits"
_TVrrpRtUnknEvtProtocol_Object = MibTableColumn
tVrrpRtUnknEvtProtocol = _TVrrpRtUnknEvtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 10),
    _TVrrpRtUnknEvtProtocol_Type()
)
tVrrpRtUnknEvtProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtProtocol.setStatus("current")
_TVrrpRtUnknEvtOperState_Type = TmnxRouteUnknownEventOperState
_TVrrpRtUnknEvtOperState_Object = MibTableColumn
tVrrpRtUnknEvtOperState = _TVrrpRtUnknEvtOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 11),
    _TVrrpRtUnknEvtOperState_Type()
)
tVrrpRtUnknEvtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtOperState.setStatus("current")
_TVrrpRtUnknEvtHoldSetRemaining_Type = TmnxEventHoldSet
_TVrrpRtUnknEvtHoldSetRemaining_Object = MibTableColumn
tVrrpRtUnknEvtHoldSetRemaining = _TVrrpRtUnknEvtHoldSetRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 12),
    _TVrrpRtUnknEvtHoldSetRemaining_Type()
)
tVrrpRtUnknEvtHoldSetRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldSetRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldSetRemaining.setUnits("seconds")
_TVrrpRtUnknEvtPrevState_Type = TmnxRouteUnknownEventOperState
_TVrrpRtUnknEvtPrevState_Object = MibTableColumn
tVrrpRtUnknEvtPrevState = _TVrrpRtUnknEvtPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 13),
    _TVrrpRtUnknEvtPrevState_Type()
)
tVrrpRtUnknEvtPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtPrevState.setStatus("current")
_TVrrpRtUnknEvtLastTransition_Type = TimeStamp
_TVrrpRtUnknEvtLastTransition_Object = MibTableColumn
tVrrpRtUnknEvtLastTransition = _TVrrpRtUnknEvtLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 14),
    _TVrrpRtUnknEvtLastTransition_Type()
)
tVrrpRtUnknEvtLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtLastTransition.setStatus("current")
_TVrrpRtUnknEvtSetCounter_Type = Counter32
_TVrrpRtUnknEvtSetCounter_Object = MibTableColumn
tVrrpRtUnknEvtSetCounter = _TVrrpRtUnknEvtSetCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 15),
    _TVrrpRtUnknEvtSetCounter_Type()
)
tVrrpRtUnknEvtSetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtSetCounter.setStatus("current")
_TVrrpRtUnknEvtInUse_Type = TruthValue
_TVrrpRtUnknEvtInUse_Object = MibTableColumn
tVrrpRtUnknEvtInUse = _TVrrpRtUnknEvtInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 16),
    _TVrrpRtUnknEvtInUse_Type()
)
tVrrpRtUnknEvtInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtInUse.setStatus("current")


class _TVrrpRtUnknEvtHoldClear_Type(TmnxEventHoldClear):
    """Custom type tVrrpRtUnknEvtHoldClear based on TmnxEventHoldClear"""
    defaultValue = 0


_TVrrpRtUnknEvtHoldClear_Object = MibTableColumn
tVrrpRtUnknEvtHoldClear = _TVrrpRtUnknEvtHoldClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 17),
    _TVrrpRtUnknEvtHoldClear_Type()
)
tVrrpRtUnknEvtHoldClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldClear.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldClear.setUnits("seconds")
_TVrrpRtUnknEvtHoldClearRemaining_Type = TmnxEventHoldClear
_TVrrpRtUnknEvtHoldClearRemaining_Object = MibTableColumn
tVrrpRtUnknEvtHoldClearRemaining = _TVrrpRtUnknEvtHoldClearRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 18),
    _TVrrpRtUnknEvtHoldClearRemaining_Type()
)
tVrrpRtUnknEvtHoldClearRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldClearRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtHoldClearRemaining.setUnits("seconds")
_TVrrpRtUnknEvtLastChgd_Type = TimeStamp
_TVrrpRtUnknEvtLastChgd_Object = MibTableColumn
tVrrpRtUnknEvtLastChgd = _TVrrpRtUnknEvtLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 11, 1, 19),
    _TVrrpRtUnknEvtLastChgd_Type()
)
tVrrpRtUnknEvtLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtLastChgd.setStatus("current")
_TVrrpRtUnknEvtNextHopTblLastChgd_Type = TimeStamp
_TVrrpRtUnknEvtNextHopTblLastChgd_Object = MibScalar
tVrrpRtUnknEvtNextHopTblLastChgd = _TVrrpRtUnknEvtNextHopTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 12),
    _TVrrpRtUnknEvtNextHopTblLastChgd_Type()
)
tVrrpRtUnknEvtNextHopTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopTblLastChgd.setStatus("current")
_TVrrpRtUnknEvtNextHopTable_Object = MibTable
tVrrpRtUnknEvtNextHopTable = _TVrrpRtUnknEvtNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13)
)
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopTable.setStatus("current")
_TVrrpRtUnknEvtNextHopEntry_Object = MibTableRow
tVrrpRtUnknEvtNextHopEntry = _TVrrpRtUnknEvtNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1)
)
tVrrpRtUnknEvtNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRRP-MIB", "tmnxVrrpPolicyId"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPrefixType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPrefix"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtMaskLen"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHopType"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHop"),
    (0, "TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHopIfName"),
)
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopEntry.setStatus("current")
_TVrrpRtUnknEvtNextHopType_Type = InetAddressType
_TVrrpRtUnknEvtNextHopType_Object = MibTableColumn
tVrrpRtUnknEvtNextHopType = _TVrrpRtUnknEvtNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1, 1),
    _TVrrpRtUnknEvtNextHopType_Type()
)
tVrrpRtUnknEvtNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopType.setStatus("current")


class _TVrrpRtUnknEvtNextHop_Type(InetAddress):
    """Custom type tVrrpRtUnknEvtNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TVrrpRtUnknEvtNextHop_Type.__name__ = "InetAddress"
_TVrrpRtUnknEvtNextHop_Object = MibTableColumn
tVrrpRtUnknEvtNextHop = _TVrrpRtUnknEvtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1, 2),
    _TVrrpRtUnknEvtNextHop_Type()
)
tVrrpRtUnknEvtNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHop.setStatus("current")
_TVrrpRtUnknEvtNextHopIfName_Type = TNamedItemOrEmpty
_TVrrpRtUnknEvtNextHopIfName_Object = MibTableColumn
tVrrpRtUnknEvtNextHopIfName = _TVrrpRtUnknEvtNextHopIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1, 3),
    _TVrrpRtUnknEvtNextHopIfName_Type()
)
tVrrpRtUnknEvtNextHopIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopIfName.setStatus("current")
_TVrrpRtUnknEvtNextHopRowStatus_Type = RowStatus
_TVrrpRtUnknEvtNextHopRowStatus_Object = MibTableColumn
tVrrpRtUnknEvtNextHopRowStatus = _TVrrpRtUnknEvtNextHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1, 4),
    _TVrrpRtUnknEvtNextHopRowStatus_Type()
)
tVrrpRtUnknEvtNextHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopRowStatus.setStatus("current")
_TVrrpRtUnknEvtNextHopLastChgd_Type = TimeStamp
_TVrrpRtUnknEvtNextHopLastChgd_Object = MibTableColumn
tVrrpRtUnknEvtNextHopLastChgd = _TVrrpRtUnknEvtNextHopLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 2, 13, 1, 5),
    _TVrrpRtUnknEvtNextHopLastChgd_Type()
)
tVrrpRtUnknEvtNextHopLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVrrpRtUnknEvtNextHopLastChgd.setStatus("current")
_TmnxVrrpNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxVrrpNotificationObjects = _TmnxVrrpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3)
)
_TmnxVrrpNotifBfdIntfSvcId_Type = TmnxServId
_TmnxVrrpNotifBfdIntfSvcId_Object = MibScalar
tmnxVrrpNotifBfdIntfSvcId = _TmnxVrrpNotifBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3, 1),
    _TmnxVrrpNotifBfdIntfSvcId_Type()
)
tmnxVrrpNotifBfdIntfSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVrrpNotifBfdIntfSvcId.setStatus("current")
_TmnxVrrpNotifBfdIntfIfName_Type = TNamedItem
_TmnxVrrpNotifBfdIntfIfName_Object = MibScalar
tmnxVrrpNotifBfdIntfIfName = _TmnxVrrpNotifBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3, 2),
    _TmnxVrrpNotifBfdIntfIfName_Type()
)
tmnxVrrpNotifBfdIntfIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVrrpNotifBfdIntfIfName.setStatus("current")
_TmnxVrrpNotifBfdIntfDestIpType_Type = InetAddressType
_TmnxVrrpNotifBfdIntfDestIpType_Object = MibScalar
tmnxVrrpNotifBfdIntfDestIpType = _TmnxVrrpNotifBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3, 3),
    _TmnxVrrpNotifBfdIntfDestIpType_Type()
)
tmnxVrrpNotifBfdIntfDestIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVrrpNotifBfdIntfDestIpType.setStatus("current")


class _TmnxVrrpNotifBfdIntfDestIp_Type(InetAddress):
    """Custom type tmnxVrrpNotifBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVrrpNotifBfdIntfDestIp_Type.__name__ = "InetAddress"
_TmnxVrrpNotifBfdIntfDestIp_Object = MibScalar
tmnxVrrpNotifBfdIntfDestIp = _TmnxVrrpNotifBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3, 4),
    _TmnxVrrpNotifBfdIntfDestIp_Type()
)
tmnxVrrpNotifBfdIntfDestIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVrrpNotifBfdIntfDestIp.setStatus("current")
_TmnxVrrpNotifBfdIntfSessState_Type = TmnxVrrpAssoBfdIntfSessOperState
_TmnxVrrpNotifBfdIntfSessState_Object = MibScalar
tmnxVrrpNotifBfdIntfSessState = _TmnxVrrpNotifBfdIntfSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 20, 3, 5),
    _TmnxVrrpNotifBfdIntfSessState_Type()
)
tmnxVrrpNotifBfdIntfSessState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVrrpNotifBfdIntfSessState.setStatus("current")
_TmnxVrrpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxVrrpNotifyPrefix = _TmnxVrrpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20)
)
_TmnxVrrpNotifications_ObjectIdentity = ObjectIdentity
tmnxVrrpNotifications = _TmnxVrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0)
)
vrrpOperEntry.registerAugmentions(
    ("TIMETRA-VRRP-MIB",
     "tmnxVrrpOperEntry")
)
tmnxVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
vrrpRouterStatsEntry.registerAugmentions(
    ("TIMETRA-VRRP-MIB",
     "tmnxVrrpRouterStatsEntry")
)
tmnxVrrpRouterStatsEntry.setIndexNames(*vrrpRouterStatsEntry.getIndexNames())
vrrpOperationsEntry.registerAugmentions(
    ("TIMETRA-VRRP-MIB",
     "tVrrpOpEntry")
)
tVrrpOpEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())
vrrpRouterStatisticsEntry.registerAugmentions(
    ("TIMETRA-VRRP-MIB",
     "tVrrpRtrStatisticsEntry")
)
tVrrpRtrStatisticsEntry.setIndexNames(*vrrpRouterStatisticsEntry.getIndexNames())
ipv6RouterAdvertEntry.registerAugmentions(
    ("TIMETRA-VRRP-MIB",
     "tVrrpIpv6RouterAdvertEntry")
)
tVrrpIpv6RouterAdvertEntry.setIndexNames(*ipv6RouterAdvertEntry.getIndexNames())

# Managed Objects groups

tmnxVrrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 2)
)
tmnxVrrpStatsGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpStatsAdvertiseSent"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsPreemptEvents"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsPreemptedEvents"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsMasterChanges"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsAdvertiseIntervalDiscards"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsAddressListDiscards"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpStatsTotalDiscards"))
)
if mibBuilder.loadTexts:
    tmnxVrrpStatsGroup.setStatus("current")

tmnxVrrpRouteMasterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 3)
)
tmnxVrrpRouteMasterGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterLastSeen"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterMessageCount"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterAuthSequence"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterIPListMatch"))
)
if mibBuilder.loadTexts:
    tmnxVrrpRouteMasterGroup.setStatus("current")

tmnxVrrpPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 4)
)
tmnxVrrpPolicyGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyDescription"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyDeltaInUseLimit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyReferenceCount"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyCurrentExplicit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyCurrentDeltaSum"))
)
if mibBuilder.loadTexts:
    tmnxVrrpPolicyGroup.setStatus("obsolete")

tmnxVrrpPriorityEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 5)
)
tmnxVrrpPriorityEventsGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventHoldSet"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventPrevState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventLastTransition"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventSetCounter"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventInUse"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventHoldClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPortDownEventHoldClearRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventHoldSet"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventPrevState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventLastTransition"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventSetCounter"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventInUse"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventHoldClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagPortDownEventHoldClearRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagNumberDownEventRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagNumberDownEventPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpLagNumberDownEventType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventHoldSet"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventTimeout"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventDropCount"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventPrevState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventLastTransition"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventSetCounter"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventInUse"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventHoldClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpHostUnreachableEventHoldClearRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventHoldSet"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventLessSpecific"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventDefaultAllowed"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventProtocol"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventPrevState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventLastTransition"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventSetCounter"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventInUse"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventHoldClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventHoldClearRemaining"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpRouteUnknownEventNextHopRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxVrrpPriorityEventsGroup.setStatus("current")

tmnxVrrpBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 6)
)
tmnxVrrpBfdGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfTblLastChgd"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfLastChgd"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSrcIpType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSrcIp"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSessOperState"))
)
if mibBuilder.loadTexts:
    tmnxVrrpBfdGroup.setStatus("obsolete")

tmnxVrrpOperV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 9)
)
tmnxVrrpOperV4v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperVirtualMacAddr"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMismatchDiscard"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPingReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTelnetReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperSshReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPolicyId"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUsePriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterSince"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperOwner"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownTimer"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperAdvIntervalInherit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUseAdvInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTracerouteReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperStandbyFwding"))
)
if mibBuilder.loadTexts:
    tmnxVrrpOperV4v0Group.setStatus("obsolete")

tmnxVrrpPolicyV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 10)
)
tmnxVrrpPolicyV5v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyDescription"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyDeltaInUseLimit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyReferenceCount"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyCurrentExplicit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicyCurrentDeltaSum"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpPolicySvcContext"))
)
if mibBuilder.loadTexts:
    tmnxVrrpPolicyV5v0Group.setStatus("current")

tmnxVrrpOperV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 11)
)
tmnxVrrpOperV5v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperVirtualMacAddr"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMismatchDiscard"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPingReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTelnetReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperSshReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPolicyId"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUsePriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterSince"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperOwner"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownTimer"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperAdvIntervalInherit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUseAdvInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTracerouteReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperStandbyFwding"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperAdvIntervalMilSec"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUseAdvIntlMilSec"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInitDelay"))
)
if mibBuilder.loadTexts:
    tmnxVrrpOperV5v0Group.setStatus("obsolete")

tmnxVrrpOperV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 13)
)
tmnxVrrpOperV6v1Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperVirtualMacAddr"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMismatchDiscard"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPingReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTelnetReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperSshReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperPolicyId"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUsePriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterSince"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterPriority"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperOwner"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperMasterDownTimer"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperAdvIntervalInherit"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUseAdvInterval"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperTracerouteReply"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperStandbyFwding"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperAdvIntervalMilSec"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInUseAdvIntlMilSec"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInitDelay"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpOperInitTimer"))
)
if mibBuilder.loadTexts:
    tmnxVrrpOperV6v1Group.setStatus("current")

tmnxVrrpNotificationObjV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 14)
)
tmnxVrrpNotificationObjV6v1Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfSvcId"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfIfName"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfDestIpType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfDestIp"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tmnxVrrpNotificationObjV6v1Group.setStatus("current")

tVrrpHostUnreachableV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 15)
)
tVrrpHostUnreachableV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtDropCount"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtHoldClear"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtHldClrRemain"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtHoldSet"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtInUse"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtInterval"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtLastTransition"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtOperState"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtPrevState"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtPriority"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtRowStatus"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtSetCounter"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtTimeout"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtType"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpHstUnrchEvtTblLastChgd"))
)
if mibBuilder.loadTexts:
    tVrrpHostUnreachableV7v0Group.setStatus("current")

tVrrpOpV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 16)
)
tVrrpOpV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpOpAdvIntervalInherit"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpInUseAdvInterval"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpInUsePriority"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpInitDelay"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpInitTimer"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpMasterDownInterval"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpMasterDownTimer"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpMasterPriority"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpMasterSince"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpOwner"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpPingReply"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpPolicyId"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpStandbyFwding"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpState"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpTelnetReply"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpTracerouteReply"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpVirtualMacAddr"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpOperDownReason"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpOpTblLastChgd"))
)
if mibBuilder.loadTexts:
    tVrrpOpV7v0Group.setStatus("current")

tVrrpRouteUnknownV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 17)
)
tVrrpRouteUnknownV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtDefaultAllowed"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtHoldClear"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtHoldClearRemaining"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtHoldSet"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtHoldSetRemaining"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtInUse"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtLastTransition"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtLessSpecific"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHopRowStatus"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtOperState"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPrevState"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtPriority"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtProtocol"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtRowStatus"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtSetCounter"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtType"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHopLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtNextHopTblLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtUnknEvtTblLastChgd"))
)
if mibBuilder.loadTexts:
    tVrrpRouteUnknownV7v0Group.setStatus("current")

tVrrpMasterV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 18)
)
tVrrpMasterV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpRtrMasterAuthSequence"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterIPListMatch"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterLastSeen"),
        ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterMessageCount"))
)
if mibBuilder.loadTexts:
    tVrrpMasterV7v0Group.setStatus("current")

tVrrpStatV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 19)
)
tVrrpStatV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpStatAdvIntvlDiscards"),
        ("TIMETRA-VRRP-MIB", "tVrrpStatAdvertiseSent"),
        ("TIMETRA-VRRP-MIB", "tVrrpStatMasterChanges"),
        ("TIMETRA-VRRP-MIB", "tVrrpStatPreemptEvents"),
        ("TIMETRA-VRRP-MIB", "tVrrpStatPreemptedEvents"),
        ("TIMETRA-VRRP-MIB", "tVrrpStatTotalDiscards"))
)
if mibBuilder.loadTexts:
    tVrrpStatV7v0Group.setStatus("current")

tVrrpRouterAdverV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 20)
)
tVrrpRouterAdverV7v0Group.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpIpv6RouterAdvertUseVirtualMac")
)
if mibBuilder.loadTexts:
    tVrrpRouterAdverV7v0Group.setStatus("current")

tVrrpBfdV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 22)
)
tVrrpBfdV9v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfLastChgd"),
        ("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfRowStatus"),
        ("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfSessOperState"),
        ("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfSrcIp"),
        ("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfSrcIpType"),
        ("TIMETRA-VRRP-MIB", "tVrrpAssoBfdIntfTblLastChgd"))
)
if mibBuilder.loadTexts:
    tVrrpBfdV9v0Group.setStatus("current")

tmnxVrrpObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 23)
)
tmnxVrrpObsoletedV9v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfLastChgd"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfRowStatus"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSessOperState"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSrcIp"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfSrcIpType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpAssoBfdIntfTblLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxVrrpObsoletedV9v0Group.setStatus("current")


# Notification objects

tmnxVrrpIPListMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 1)
)
tmnxVrrpIPListMismatch.setObjects(
    ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterIPListMatch")
)
if mibBuilder.loadTexts:
    tmnxVrrpIPListMismatch.setStatus(
        "current"
    )

tmnxVrrpIPListMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 2)
)
tmnxVrrpIPListMismatchClear.setObjects(
    ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterIPListMatch")
)
if mibBuilder.loadTexts:
    tmnxVrrpIPListMismatchClear.setStatus(
        "current"
    )

tmnxVrrpMultipleOwners = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 3)
)
tmnxVrrpMultipleOwners.setObjects(
    ("TIMETRA-VRRP-MIB", "tmnxVrrpRouterMasterLastSeen")
)
if mibBuilder.loadTexts:
    tmnxVrrpMultipleOwners.setStatus(
        "current"
    )

tmnxVrrpBecameBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 4)
)
tmnxVrrpBecameBackup.setObjects(
    ("VRRP-MIB", "vrrpOperMasterIpAddr")
)
if mibBuilder.loadTexts:
    tmnxVrrpBecameBackup.setStatus(
        "current"
    )

tmnxVrrpBfdIntfSessStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 5)
)
tmnxVrrpBfdIntfSessStateChgd.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfSvcId"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfIfName"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfDestIpType"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfDestIp"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tmnxVrrpBfdIntfSessStateChgd.setStatus(
        "current"
    )

tVrrpBecameBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 6)
)
tVrrpBecameBackup.setObjects(
    ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsMasterIpAddr")
)
if mibBuilder.loadTexts:
    tVrrpBecameBackup.setStatus(
        "current"
    )

tVrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 7)
)
tVrrpTrapNewMaster.setObjects(
      *(("TIMETRA-VRRP-V3-MIB", "vrrpOperationsMasterIpAddr"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpNewMasterReason"))
)
if mibBuilder.loadTexts:
    tVrrpTrapNewMaster.setStatus(
        "current"
    )

tVrrpIPListMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 8)
)
tVrrpIPListMismatch.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterIPListMatch")
)
if mibBuilder.loadTexts:
    tVrrpIPListMismatch.setStatus(
        "current"
    )

tVrrpIPListMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 9)
)
tVrrpIPListMismatchClear.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterIPListMatch")
)
if mibBuilder.loadTexts:
    tVrrpIPListMismatchClear.setStatus(
        "current"
    )

tVrrpMultipleOwners = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 10)
)
tVrrpMultipleOwners.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpRtrMasterLastSeen")
)
if mibBuilder.loadTexts:
    tVrrpMultipleOwners.setStatus(
        "current"
    )

tVrrpRouterAdvNotActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 11)
)
tVrrpRouterAdvNotActivated.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpOpState")
)
if mibBuilder.loadTexts:
    tVrrpRouterAdvNotActivated.setStatus(
        "current"
    )

tVrrpRouterAdvNotActivatedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 20, 0, 12)
)
tVrrpRouterAdvNotActivatedClear.setObjects(
    ("TIMETRA-VRRP-MIB", "tVrrpOpState")
)
if mibBuilder.loadTexts:
    tVrrpRouterAdvNotActivatedClear.setStatus(
        "current"
    )


# Notifications groups

tmnxVrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 7)
)
tmnxVrrpNotificationGroup.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpIPListMismatch"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpIPListMismatchClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpMultipleOwners"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpBecameBackup"))
)
if mibBuilder.loadTexts:
    tmnxVrrpNotificationGroup.setStatus(
        "obsolete"
    )

tmnxVrrpNotificationV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 12)
)
tmnxVrrpNotificationV6v1Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tmnxVrrpIPListMismatch"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpIPListMismatchClear"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpMultipleOwners"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpBecameBackup"),
        ("TIMETRA-VRRP-MIB", "tmnxVrrpBfdIntfSessStateChgd"))
)
if mibBuilder.loadTexts:
    tmnxVrrpNotificationV6v1Group.setStatus(
        "current"
    )

tVrrpNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 2, 21)
)
tVrrpNotificationV7v0Group.setObjects(
      *(("TIMETRA-VRRP-MIB", "tVrrpBecameBackup"),
        ("TIMETRA-VRRP-MIB", "tVrrpTrapNewMaster"),
        ("TIMETRA-VRRP-MIB", "tVrrpIPListMismatch"),
        ("TIMETRA-VRRP-MIB", "tVrrpIPListMismatchClear"),
        ("TIMETRA-VRRP-MIB", "tVrrpMultipleOwners"),
        ("TIMETRA-VRRP-MIB", "tVrrpRouterAdvNotActivated"),
        ("TIMETRA-VRRP-MIB", "tVrrpRouterAdvNotActivatedClear"))
)
if mibBuilder.loadTexts:
    tVrrpNotificationV7v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxVrrpV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxVrrpV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxVrrpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxVrrpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxVrrpV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxVrrpV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxVrrp77x0V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxVrrp77x0V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxVrrp7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxVrrp7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxVrrp77x0V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxVrrp77x0V9v0Compliance.setStatus(
        "current"
    )

tmnxVrrp7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 20, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxVrrp7450V9v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-VRRP-MIB",
    **{"TmnxVrrpPolicyID": TmnxVrrpPolicyID,
       "TmnxVrrpPriority": TmnxVrrpPriority,
       "TmnxEventType": TmnxEventType,
       "TmnxEventHoldSet": TmnxEventHoldSet,
       "TmnxEventHoldClear": TmnxEventHoldClear,
       "TmnxPortDownEventOperState": TmnxPortDownEventOperState,
       "TmnxLagPortDownEventOperState": TmnxLagPortDownEventOperState,
       "TmnxHostUnreachableEventOperState": TmnxHostUnreachableEventOperState,
       "TmnxRouteUnknownEventOperState": TmnxRouteUnknownEventOperState,
       "TmnxVrrpAssoBfdIntfSessOperState": TmnxVrrpAssoBfdIntfSessOperState,
       "timetraVrrpMIBModule": timetraVrrpMIBModule,
       "tmnxVrrpConformance": tmnxVrrpConformance,
       "tmnxVrrpCompliances": tmnxVrrpCompliances,
       "tmnxVrrpV4v0Compliance": tmnxVrrpV4v0Compliance,
       "tmnxVrrpV5v0Compliance": tmnxVrrpV5v0Compliance,
       "tmnxVrrpV6v1Compliance": tmnxVrrpV6v1Compliance,
       "tmnxVrrp77x0V7v0Compliance": tmnxVrrp77x0V7v0Compliance,
       "tmnxVrrp7450V7v0Compliance": tmnxVrrp7450V7v0Compliance,
       "tmnxVrrp77x0V9v0Compliance": tmnxVrrp77x0V9v0Compliance,
       "tmnxVrrp7450V9v0Compliance": tmnxVrrp7450V9v0Compliance,
       "tmnxVrrpGroups": tmnxVrrpGroups,
       "tmnxVrrpStatsGroup": tmnxVrrpStatsGroup,
       "tmnxVrrpRouteMasterGroup": tmnxVrrpRouteMasterGroup,
       "tmnxVrrpPolicyGroup": tmnxVrrpPolicyGroup,
       "tmnxVrrpPriorityEventsGroup": tmnxVrrpPriorityEventsGroup,
       "tmnxVrrpBfdGroup": tmnxVrrpBfdGroup,
       "tmnxVrrpNotificationGroup": tmnxVrrpNotificationGroup,
       "tmnxVrrpOperV4v0Group": tmnxVrrpOperV4v0Group,
       "tmnxVrrpPolicyV5v0Group": tmnxVrrpPolicyV5v0Group,
       "tmnxVrrpOperV5v0Group": tmnxVrrpOperV5v0Group,
       "tmnxVrrpNotificationV6v1Group": tmnxVrrpNotificationV6v1Group,
       "tmnxVrrpOperV6v1Group": tmnxVrrpOperV6v1Group,
       "tmnxVrrpNotificationObjV6v1Group": tmnxVrrpNotificationObjV6v1Group,
       "tVrrpHostUnreachableV7v0Group": tVrrpHostUnreachableV7v0Group,
       "tVrrpOpV7v0Group": tVrrpOpV7v0Group,
       "tVrrpRouteUnknownV7v0Group": tVrrpRouteUnknownV7v0Group,
       "tVrrpMasterV7v0Group": tVrrpMasterV7v0Group,
       "tVrrpStatV7v0Group": tVrrpStatV7v0Group,
       "tVrrpRouterAdverV7v0Group": tVrrpRouterAdverV7v0Group,
       "tVrrpNotificationV7v0Group": tVrrpNotificationV7v0Group,
       "tVrrpBfdV9v0Group": tVrrpBfdV9v0Group,
       "tmnxVrrpObsoletedV9v0Group": tmnxVrrpObsoletedV9v0Group,
       "tmnxVrrpMibObjects": tmnxVrrpMibObjects,
       "tmnxVrrpObjects": tmnxVrrpObjects,
       "tmnxVrrpOperTable": tmnxVrrpOperTable,
       "tmnxVrrpOperEntry": tmnxVrrpOperEntry,
       "tmnxVrrpOperState": tmnxVrrpOperState,
       "tmnxVrrpOperVirtualMacAddr": tmnxVrrpOperVirtualMacAddr,
       "tmnxVrrpOperMismatchDiscard": tmnxVrrpOperMismatchDiscard,
       "tmnxVrrpOperPingReply": tmnxVrrpOperPingReply,
       "tmnxVrrpOperTelnetReply": tmnxVrrpOperTelnetReply,
       "tmnxVrrpOperSshReply": tmnxVrrpOperSshReply,
       "tmnxVrrpOperPolicyId": tmnxVrrpOperPolicyId,
       "tmnxVrrpOperInUsePriority": tmnxVrrpOperInUsePriority,
       "tmnxVrrpOperMasterSince": tmnxVrrpOperMasterSince,
       "tmnxVrrpOperMasterPriority": tmnxVrrpOperMasterPriority,
       "tmnxVrrpOperOwner": tmnxVrrpOperOwner,
       "tmnxVrrpOperMasterDownInterval": tmnxVrrpOperMasterDownInterval,
       "tmnxVrrpOperMasterDownTimer": tmnxVrrpOperMasterDownTimer,
       "tmnxVrrpOperAdvIntervalInherit": tmnxVrrpOperAdvIntervalInherit,
       "tmnxVrrpOperInUseAdvInterval": tmnxVrrpOperInUseAdvInterval,
       "tmnxVrrpOperTracerouteReply": tmnxVrrpOperTracerouteReply,
       "tmnxVrrpOperStandbyFwding": tmnxVrrpOperStandbyFwding,
       "tmnxVrrpOperAdvIntervalMilSec": tmnxVrrpOperAdvIntervalMilSec,
       "tmnxVrrpOperInUseAdvIntlMilSec": tmnxVrrpOperInUseAdvIntlMilSec,
       "tmnxVrrpOperInitDelay": tmnxVrrpOperInitDelay,
       "tmnxVrrpOperInitTimer": tmnxVrrpOperInitTimer,
       "tmnxVrrpRouterStatsTable": tmnxVrrpRouterStatsTable,
       "tmnxVrrpRouterStatsEntry": tmnxVrrpRouterStatsEntry,
       "tmnxVrrpStatsAdvertiseSent": tmnxVrrpStatsAdvertiseSent,
       "tmnxVrrpStatsPreemptEvents": tmnxVrrpStatsPreemptEvents,
       "tmnxVrrpStatsPreemptedEvents": tmnxVrrpStatsPreemptedEvents,
       "tmnxVrrpStatsMasterChanges": tmnxVrrpStatsMasterChanges,
       "tmnxVrrpStatsAdvertiseIntervalDiscards": tmnxVrrpStatsAdvertiseIntervalDiscards,
       "tmnxVrrpStatsAddressListDiscards": tmnxVrrpStatsAddressListDiscards,
       "tmnxVrrpStatsTotalDiscards": tmnxVrrpStatsTotalDiscards,
       "tmnxVrrpRouterMasterTable": tmnxVrrpRouterMasterTable,
       "tmnxVrrpRouterMasterEntry": tmnxVrrpRouterMasterEntry,
       "tmnxVrrpRouterMasterPrimaryAddr": tmnxVrrpRouterMasterPrimaryAddr,
       "tmnxVrrpRouterMasterLastSeen": tmnxVrrpRouterMasterLastSeen,
       "tmnxVrrpRouterMasterMessageCount": tmnxVrrpRouterMasterMessageCount,
       "tmnxVrrpRouterMasterAuthSequence": tmnxVrrpRouterMasterAuthSequence,
       "tmnxVrrpRouterMasterIPListMatch": tmnxVrrpRouterMasterIPListMatch,
       "tmnxVrrpAssoBfdIntfTblLastChgd": tmnxVrrpAssoBfdIntfTblLastChgd,
       "tmnxVrrpAssoBfdIntfTable": tmnxVrrpAssoBfdIntfTable,
       "tmnxVrrpAssoBfdIntfEntry": tmnxVrrpAssoBfdIntfEntry,
       "tmnxVrrpAssoBfdIntfSvcId": tmnxVrrpAssoBfdIntfSvcId,
       "tmnxVrrpAssoBfdIntfIfName": tmnxVrrpAssoBfdIntfIfName,
       "tmnxVrrpAssoBfdIntfDestIpType": tmnxVrrpAssoBfdIntfDestIpType,
       "tmnxVrrpAssoBfdIntfDestIp": tmnxVrrpAssoBfdIntfDestIp,
       "tmnxVrrpAssoBfdIntfRowStatus": tmnxVrrpAssoBfdIntfRowStatus,
       "tmnxVrrpAssoBfdIntfLastChgd": tmnxVrrpAssoBfdIntfLastChgd,
       "tmnxVrrpAssoBfdIntfSrcIpType": tmnxVrrpAssoBfdIntfSrcIpType,
       "tmnxVrrpAssoBfdIntfSrcIp": tmnxVrrpAssoBfdIntfSrcIp,
       "tmnxVrrpAssoBfdIntfSessOperState": tmnxVrrpAssoBfdIntfSessOperState,
       "tVrrpOpTblLastChgd": tVrrpOpTblLastChgd,
       "tVrrpOpTable": tVrrpOpTable,
       "tVrrpOpEntry": tVrrpOpEntry,
       "tVrrpOpState": tVrrpOpState,
       "tVrrpOpVirtualMacAddr": tVrrpOpVirtualMacAddr,
       "tVrrpOpPingReply": tVrrpOpPingReply,
       "tVrrpOpTelnetReply": tVrrpOpTelnetReply,
       "tVrrpOpPolicyId": tVrrpOpPolicyId,
       "tVrrpOpInUsePriority": tVrrpOpInUsePriority,
       "tVrrpOpMasterSince": tVrrpOpMasterSince,
       "tVrrpOpMasterPriority": tVrrpOpMasterPriority,
       "tVrrpOpOwner": tVrrpOpOwner,
       "tVrrpOpMasterDownInterval": tVrrpOpMasterDownInterval,
       "tVrrpOpMasterDownTimer": tVrrpOpMasterDownTimer,
       "tVrrpOpAdvIntervalInherit": tVrrpOpAdvIntervalInherit,
       "tVrrpOpInUseAdvInterval": tVrrpOpInUseAdvInterval,
       "tVrrpOpTracerouteReply": tVrrpOpTracerouteReply,
       "tVrrpOpStandbyFwding": tVrrpOpStandbyFwding,
       "tVrrpOpInitDelay": tVrrpOpInitDelay,
       "tVrrpOpInitTimer": tVrrpOpInitTimer,
       "tVrrpOpLastChgd": tVrrpOpLastChgd,
       "tVrrpOpOperDownReason": tVrrpOpOperDownReason,
       "tVrrpRtrStatisticsTable": tVrrpRtrStatisticsTable,
       "tVrrpRtrStatisticsEntry": tVrrpRtrStatisticsEntry,
       "tVrrpStatAdvertiseSent": tVrrpStatAdvertiseSent,
       "tVrrpStatPreemptEvents": tVrrpStatPreemptEvents,
       "tVrrpStatPreemptedEvents": tVrrpStatPreemptedEvents,
       "tVrrpStatMasterChanges": tVrrpStatMasterChanges,
       "tVrrpStatAdvIntvlDiscards": tVrrpStatAdvIntvlDiscards,
       "tVrrpStatTotalDiscards": tVrrpStatTotalDiscards,
       "tVrrpRtrMasterTable": tVrrpRtrMasterTable,
       "tVrrpRtrMasterEntry": tVrrpRtrMasterEntry,
       "tVrrpRtrMasterInetAddrType": tVrrpRtrMasterInetAddrType,
       "tVrrpRtrMasterPrimaryAddr": tVrrpRtrMasterPrimaryAddr,
       "tVrrpRtrMasterLastSeen": tVrrpRtrMasterLastSeen,
       "tVrrpRtrMasterMessageCount": tVrrpRtrMasterMessageCount,
       "tVrrpRtrMasterAuthSequence": tVrrpRtrMasterAuthSequence,
       "tVrrpRtrMasterIPListMatch": tVrrpRtrMasterIPListMatch,
       "tVrrpIpv6RouterAdvertTable": tVrrpIpv6RouterAdvertTable,
       "tVrrpIpv6RouterAdvertEntry": tVrrpIpv6RouterAdvertEntry,
       "tVrrpIpv6RouterAdvertUseVirtualMac": tVrrpIpv6RouterAdvertUseVirtualMac,
       "tVrrpAssoBfdIntfTblLastChgd": tVrrpAssoBfdIntfTblLastChgd,
       "tVrrpAssoBfdIntfTable": tVrrpAssoBfdIntfTable,
       "tVrrpAssoBfdIntfEntry": tVrrpAssoBfdIntfEntry,
       "tVrrpAssoBfdIntfVrIdIpType": tVrrpAssoBfdIntfVrIdIpType,
       "tVrrpAssoBfdIntfSvcId": tVrrpAssoBfdIntfSvcId,
       "tVrrpAssoBfdIntfIfName": tVrrpAssoBfdIntfIfName,
       "tVrrpAssoBfdIntfDestIpType": tVrrpAssoBfdIntfDestIpType,
       "tVrrpAssoBfdIntfDestIp": tVrrpAssoBfdIntfDestIp,
       "tVrrpAssoBfdIntfRowStatus": tVrrpAssoBfdIntfRowStatus,
       "tVrrpAssoBfdIntfLastChgd": tVrrpAssoBfdIntfLastChgd,
       "tVrrpAssoBfdIntfSrcIpType": tVrrpAssoBfdIntfSrcIpType,
       "tVrrpAssoBfdIntfSrcIp": tVrrpAssoBfdIntfSrcIp,
       "tVrrpAssoBfdIntfSessOperState": tVrrpAssoBfdIntfSessOperState,
       "tmnxVrrpPolicyObjects": tmnxVrrpPolicyObjects,
       "tmnxVrrpPolicyTable": tmnxVrrpPolicyTable,
       "tmnxVrrpPolicyEntry": tmnxVrrpPolicyEntry,
       "tmnxVrrpPolicyId": tmnxVrrpPolicyId,
       "tmnxVrrpPolicyRowStatus": tmnxVrrpPolicyRowStatus,
       "tmnxVrrpPolicyDescription": tmnxVrrpPolicyDescription,
       "tmnxVrrpPolicyDeltaInUseLimit": tmnxVrrpPolicyDeltaInUseLimit,
       "tmnxVrrpPolicyReferenceCount": tmnxVrrpPolicyReferenceCount,
       "tmnxVrrpPolicyCurrentExplicit": tmnxVrrpPolicyCurrentExplicit,
       "tmnxVrrpPolicyCurrentDeltaSum": tmnxVrrpPolicyCurrentDeltaSum,
       "tmnxVrrpPolicySvcContext": tmnxVrrpPolicySvcContext,
       "tmnxVrrpPortDownEventTable": tmnxVrrpPortDownEventTable,
       "tmnxVrrpPortDownEventEntry": tmnxVrrpPortDownEventEntry,
       "tmnxVrrpPortDownEventPortId": tmnxVrrpPortDownEventPortId,
       "tmnxVrrpPortDownEventRowStatus": tmnxVrrpPortDownEventRowStatus,
       "tmnxVrrpPortDownEventPriority": tmnxVrrpPortDownEventPriority,
       "tmnxVrrpPortDownEventType": tmnxVrrpPortDownEventType,
       "tmnxVrrpPortDownEventHoldSet": tmnxVrrpPortDownEventHoldSet,
       "tmnxVrrpPortDownEventOperState": tmnxVrrpPortDownEventOperState,
       "tmnxVrrpPortDownEventHoldSetRemaining": tmnxVrrpPortDownEventHoldSetRemaining,
       "tmnxVrrpPortDownEventPrevState": tmnxVrrpPortDownEventPrevState,
       "tmnxVrrpPortDownEventLastTransition": tmnxVrrpPortDownEventLastTransition,
       "tmnxVrrpPortDownEventSetCounter": tmnxVrrpPortDownEventSetCounter,
       "tmnxVrrpPortDownEventInUse": tmnxVrrpPortDownEventInUse,
       "tmnxVrrpPortDownEventHoldClear": tmnxVrrpPortDownEventHoldClear,
       "tmnxVrrpPortDownEventHoldClearRemaining": tmnxVrrpPortDownEventHoldClearRemaining,
       "tmnxVrrpLagPortDownEventTable": tmnxVrrpLagPortDownEventTable,
       "tmnxVrrpLagPortDownEventEntry": tmnxVrrpLagPortDownEventEntry,
       "tmnxVrrpLagPortDownEventLagId": tmnxVrrpLagPortDownEventLagId,
       "tmnxVrrpLagPortDownEventRowStatus": tmnxVrrpLagPortDownEventRowStatus,
       "tmnxVrrpLagPortDownEventHoldSet": tmnxVrrpLagPortDownEventHoldSet,
       "tmnxVrrpLagPortDownEventOperState": tmnxVrrpLagPortDownEventOperState,
       "tmnxVrrpLagPortDownEventHoldSetRemaining": tmnxVrrpLagPortDownEventHoldSetRemaining,
       "tmnxVrrpLagPortDownEventPrevState": tmnxVrrpLagPortDownEventPrevState,
       "tmnxVrrpLagPortDownEventLastTransition": tmnxVrrpLagPortDownEventLastTransition,
       "tmnxVrrpLagPortDownEventSetCounter": tmnxVrrpLagPortDownEventSetCounter,
       "tmnxVrrpLagPortDownEventInUse": tmnxVrrpLagPortDownEventInUse,
       "tmnxVrrpLagPortDownEventHoldClear": tmnxVrrpLagPortDownEventHoldClear,
       "tmnxVrrpLagPortDownEventHoldClearRemaining": tmnxVrrpLagPortDownEventHoldClearRemaining,
       "tmnxVrrpLagNumberDownEventTable": tmnxVrrpLagNumberDownEventTable,
       "tmnxVrrpLagNumberDownEventEntry": tmnxVrrpLagNumberDownEventEntry,
       "tmnxVrrpLagNumberDown": tmnxVrrpLagNumberDown,
       "tmnxVrrpLagNumberDownEventRowStatus": tmnxVrrpLagNumberDownEventRowStatus,
       "tmnxVrrpLagNumberDownEventPriority": tmnxVrrpLagNumberDownEventPriority,
       "tmnxVrrpLagNumberDownEventType": tmnxVrrpLagNumberDownEventType,
       "tmnxVrrpHostUnreachableEventTable": tmnxVrrpHostUnreachableEventTable,
       "tmnxVrrpHostUnreachableEventEntry": tmnxVrrpHostUnreachableEventEntry,
       "tmnxVrrpHostUnreachableEventIpAddr": tmnxVrrpHostUnreachableEventIpAddr,
       "tmnxVrrpHostUnreachableEventRowStatus": tmnxVrrpHostUnreachableEventRowStatus,
       "tmnxVrrpHostUnreachableEventPriority": tmnxVrrpHostUnreachableEventPriority,
       "tmnxVrrpHostUnreachableEventType": tmnxVrrpHostUnreachableEventType,
       "tmnxVrrpHostUnreachableEventHoldSet": tmnxVrrpHostUnreachableEventHoldSet,
       "tmnxVrrpHostUnreachableEventInterval": tmnxVrrpHostUnreachableEventInterval,
       "tmnxVrrpHostUnreachableEventTimeout": tmnxVrrpHostUnreachableEventTimeout,
       "tmnxVrrpHostUnreachableEventDropCount": tmnxVrrpHostUnreachableEventDropCount,
       "tmnxVrrpHostUnreachableEventOperState": tmnxVrrpHostUnreachableEventOperState,
       "tmnxVrrpHostUnreachableEventHoldSetRemaining": tmnxVrrpHostUnreachableEventHoldSetRemaining,
       "tmnxVrrpHostUnreachableEventPrevState": tmnxVrrpHostUnreachableEventPrevState,
       "tmnxVrrpHostUnreachableEventLastTransition": tmnxVrrpHostUnreachableEventLastTransition,
       "tmnxVrrpHostUnreachableEventSetCounter": tmnxVrrpHostUnreachableEventSetCounter,
       "tmnxVrrpHostUnreachableEventInUse": tmnxVrrpHostUnreachableEventInUse,
       "tmnxVrrpHostUnreachableEventHoldClear": tmnxVrrpHostUnreachableEventHoldClear,
       "tmnxVrrpHostUnreachableEventHoldClearRemaining": tmnxVrrpHostUnreachableEventHoldClearRemaining,
       "tmnxVrrpRouteUnknownEventTable": tmnxVrrpRouteUnknownEventTable,
       "tmnxVrrpRouteUnknownEventEntry": tmnxVrrpRouteUnknownEventEntry,
       "tmnxVrrpRouteUnknownEventPrefix": tmnxVrrpRouteUnknownEventPrefix,
       "tmnxVrrpRouteUnknownEventMaskLen": tmnxVrrpRouteUnknownEventMaskLen,
       "tmnxVrrpRouteUnknownEventRowStatus": tmnxVrrpRouteUnknownEventRowStatus,
       "tmnxVrrpRouteUnknownEventPriority": tmnxVrrpRouteUnknownEventPriority,
       "tmnxVrrpRouteUnknownEventType": tmnxVrrpRouteUnknownEventType,
       "tmnxVrrpRouteUnknownEventHoldSet": tmnxVrrpRouteUnknownEventHoldSet,
       "tmnxVrrpRouteUnknownEventLessSpecific": tmnxVrrpRouteUnknownEventLessSpecific,
       "tmnxVrrpRouteUnknownEventDefaultAllowed": tmnxVrrpRouteUnknownEventDefaultAllowed,
       "tmnxVrrpRouteUnknownEventProtocol": tmnxVrrpRouteUnknownEventProtocol,
       "tmnxVrrpRouteUnknownEventOperState": tmnxVrrpRouteUnknownEventOperState,
       "tmnxVrrpRouteUnknownEventHoldSetRemaining": tmnxVrrpRouteUnknownEventHoldSetRemaining,
       "tmnxVrrpRouteUnknownEventPrevState": tmnxVrrpRouteUnknownEventPrevState,
       "tmnxVrrpRouteUnknownEventLastTransition": tmnxVrrpRouteUnknownEventLastTransition,
       "tmnxVrrpRouteUnknownEventSetCounter": tmnxVrrpRouteUnknownEventSetCounter,
       "tmnxVrrpRouteUnknownEventInUse": tmnxVrrpRouteUnknownEventInUse,
       "tmnxVrrpRouteUnknownEventHoldClear": tmnxVrrpRouteUnknownEventHoldClear,
       "tmnxVrrpRouteUnknownEventHoldClearRemaining": tmnxVrrpRouteUnknownEventHoldClearRemaining,
       "tmnxVrrpRouteUnknownEventNextHopTable": tmnxVrrpRouteUnknownEventNextHopTable,
       "tmnxVrrpRouteUnknownEventNextHopEntry": tmnxVrrpRouteUnknownEventNextHopEntry,
       "tmnxVrrpRouteUnknownEventNextHop": tmnxVrrpRouteUnknownEventNextHop,
       "tmnxVrrpRouteUnknownEventNextHopRowStatus": tmnxVrrpRouteUnknownEventNextHopRowStatus,
       "tVrrpHstUnrchEvtTblLastChgd": tVrrpHstUnrchEvtTblLastChgd,
       "tVrrpHstUnrchEvtTable": tVrrpHstUnrchEvtTable,
       "tVrrpHstUnrchEvtEntry": tVrrpHstUnrchEvtEntry,
       "tVrrpHstUnrchEvtAddrType": tVrrpHstUnrchEvtAddrType,
       "tVrrpHstUnrchEvtIpAddr": tVrrpHstUnrchEvtIpAddr,
       "tVrrpHstUnrchEvtIfName": tVrrpHstUnrchEvtIfName,
       "tVrrpHstUnrchEvtRowStatus": tVrrpHstUnrchEvtRowStatus,
       "tVrrpHstUnrchEvtPriority": tVrrpHstUnrchEvtPriority,
       "tVrrpHstUnrchEvtType": tVrrpHstUnrchEvtType,
       "tVrrpHstUnrchEvtHoldSet": tVrrpHstUnrchEvtHoldSet,
       "tVrrpHstUnrchEvtInterval": tVrrpHstUnrchEvtInterval,
       "tVrrpHstUnrchEvtTimeout": tVrrpHstUnrchEvtTimeout,
       "tVrrpHstUnrchEvtDropCount": tVrrpHstUnrchEvtDropCount,
       "tVrrpHstUnrchEvtOperState": tVrrpHstUnrchEvtOperState,
       "tVrrpHstUnrchEvtHoldSetRemaining": tVrrpHstUnrchEvtHoldSetRemaining,
       "tVrrpHstUnrchEvtPrevState": tVrrpHstUnrchEvtPrevState,
       "tVrrpHstUnrchEvtLastTransition": tVrrpHstUnrchEvtLastTransition,
       "tVrrpHstUnrchEvtSetCounter": tVrrpHstUnrchEvtSetCounter,
       "tVrrpHstUnrchEvtInUse": tVrrpHstUnrchEvtInUse,
       "tVrrpHstUnrchEvtHoldClear": tVrrpHstUnrchEvtHoldClear,
       "tVrrpHstUnrchEvtHldClrRemain": tVrrpHstUnrchEvtHldClrRemain,
       "tVrrpHstUnrchEvtLastChgd": tVrrpHstUnrchEvtLastChgd,
       "tVrrpRtUnknEvtTblLastChgd": tVrrpRtUnknEvtTblLastChgd,
       "tVrrpRtUnknEvtTable": tVrrpRtUnknEvtTable,
       "tVrrpRtUnknEvtEntry": tVrrpRtUnknEvtEntry,
       "tVrrpRtUnknEvtPrefixType": tVrrpRtUnknEvtPrefixType,
       "tVrrpRtUnknEvtPrefix": tVrrpRtUnknEvtPrefix,
       "tVrrpRtUnknEvtMaskLen": tVrrpRtUnknEvtMaskLen,
       "tVrrpRtUnknEvtRowStatus": tVrrpRtUnknEvtRowStatus,
       "tVrrpRtUnknEvtPriority": tVrrpRtUnknEvtPriority,
       "tVrrpRtUnknEvtType": tVrrpRtUnknEvtType,
       "tVrrpRtUnknEvtHoldSet": tVrrpRtUnknEvtHoldSet,
       "tVrrpRtUnknEvtLessSpecific": tVrrpRtUnknEvtLessSpecific,
       "tVrrpRtUnknEvtDefaultAllowed": tVrrpRtUnknEvtDefaultAllowed,
       "tVrrpRtUnknEvtProtocol": tVrrpRtUnknEvtProtocol,
       "tVrrpRtUnknEvtOperState": tVrrpRtUnknEvtOperState,
       "tVrrpRtUnknEvtHoldSetRemaining": tVrrpRtUnknEvtHoldSetRemaining,
       "tVrrpRtUnknEvtPrevState": tVrrpRtUnknEvtPrevState,
       "tVrrpRtUnknEvtLastTransition": tVrrpRtUnknEvtLastTransition,
       "tVrrpRtUnknEvtSetCounter": tVrrpRtUnknEvtSetCounter,
       "tVrrpRtUnknEvtInUse": tVrrpRtUnknEvtInUse,
       "tVrrpRtUnknEvtHoldClear": tVrrpRtUnknEvtHoldClear,
       "tVrrpRtUnknEvtHoldClearRemaining": tVrrpRtUnknEvtHoldClearRemaining,
       "tVrrpRtUnknEvtLastChgd": tVrrpRtUnknEvtLastChgd,
       "tVrrpRtUnknEvtNextHopTblLastChgd": tVrrpRtUnknEvtNextHopTblLastChgd,
       "tVrrpRtUnknEvtNextHopTable": tVrrpRtUnknEvtNextHopTable,
       "tVrrpRtUnknEvtNextHopEntry": tVrrpRtUnknEvtNextHopEntry,
       "tVrrpRtUnknEvtNextHopType": tVrrpRtUnknEvtNextHopType,
       "tVrrpRtUnknEvtNextHop": tVrrpRtUnknEvtNextHop,
       "tVrrpRtUnknEvtNextHopIfName": tVrrpRtUnknEvtNextHopIfName,
       "tVrrpRtUnknEvtNextHopRowStatus": tVrrpRtUnknEvtNextHopRowStatus,
       "tVrrpRtUnknEvtNextHopLastChgd": tVrrpRtUnknEvtNextHopLastChgd,
       "tmnxVrrpNotificationObjects": tmnxVrrpNotificationObjects,
       "tmnxVrrpNotifBfdIntfSvcId": tmnxVrrpNotifBfdIntfSvcId,
       "tmnxVrrpNotifBfdIntfIfName": tmnxVrrpNotifBfdIntfIfName,
       "tmnxVrrpNotifBfdIntfDestIpType": tmnxVrrpNotifBfdIntfDestIpType,
       "tmnxVrrpNotifBfdIntfDestIp": tmnxVrrpNotifBfdIntfDestIp,
       "tmnxVrrpNotifBfdIntfSessState": tmnxVrrpNotifBfdIntfSessState,
       "tmnxVrrpNotifyPrefix": tmnxVrrpNotifyPrefix,
       "tmnxVrrpNotifications": tmnxVrrpNotifications,
       "tmnxVrrpIPListMismatch": tmnxVrrpIPListMismatch,
       "tmnxVrrpIPListMismatchClear": tmnxVrrpIPListMismatchClear,
       "tmnxVrrpMultipleOwners": tmnxVrrpMultipleOwners,
       "tmnxVrrpBecameBackup": tmnxVrrpBecameBackup,
       "tmnxVrrpBfdIntfSessStateChgd": tmnxVrrpBfdIntfSessStateChgd,
       "tVrrpBecameBackup": tVrrpBecameBackup,
       "tVrrpTrapNewMaster": tVrrpTrapNewMaster,
       "tVrrpIPListMismatch": tVrrpIPListMismatch,
       "tVrrpIPListMismatchClear": tVrrpIPListMismatchClear,
       "tVrrpMultipleOwners": tVrrpMultipleOwners,
       "tVrrpRouterAdvNotActivated": tVrrpRouterAdvNotActivated,
       "tVrrpRouterAdvNotActivatedClear": tVrrpRouterAdvNotActivatedClear}
)
