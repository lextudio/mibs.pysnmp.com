# SNMP MIB module (CISCO-PFR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PFR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:44 2024
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

(CiscoPdProtocolIndex,) = mibBuilder.importSymbols(
    "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB",
    "CiscoPdProtocolIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "InterfaceIndexOrZero")

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPfrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772)
)
ciscoPfrMIB.setRevisions(
        ("2012-11-13 00:00",
         "2011-04-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PfrMetricPolicyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relative", 1),
          ("threshold", 2))
    )



class PfrLastUncontrolReason(Integer32, TextualConvention):
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("activatingUnsedFcdTgt", 2),
          ("allProtoCouldNtControl", 32),
          ("applControlOnBrFailed", 31),
          ("borderDown", 6),
          ("cantSelectEntrances", 38),
          ("clearOnePfx", 16),
          ("clearOneTc", 17),
          ("controledExitIsNotCurrent", 51),
          ("controlledExitIsNotCurrForUpd", 55),
          ("couldntChooseExitInPfxTimeout", 47),
          ("couldntControl", 30),
          ("couldntControlPasPfxInSpecMode", 56),
          ("couldntExclude", 35),
          ("couldntFindBestExit", 42),
          ("couldntFindBestExitInAllLinkGrps", 41),
          ("couldntMonitor", 29),
          ("dontDowngradeAllEntrances", 36),
          ("endOfProbing", 44),
          ("excludePfxFailed", 33),
          ("exitMisMatch", 52),
          ("failedToControlRoute", 43),
          ("fcdTgtAssRemMod", 23),
          ("firstTargetWithDscpAdded", 26),
          ("forcedNextHop", 14),
          ("forwardToNull0", 15),
          ("grantUpdated", 18),
          ("ifaceDown", 3),
          ("inconsistentView", 48),
          ("insideEnabled", 13),
          ("ipflowRestFailed", 34),
          ("last", 61),
          ("lastTargetWithDscpRemoved", 28),
          ("maxDownGrade", 37),
          ("modeRouteChange", 10),
          ("nbarIdStateUpdated", 50),
          ("nbarInternalIfAddedRemoved", 58),
          ("newExitWhileInpolicy", 53),
          ("newProbeTargetAssigned", 4),
          ("newTargetAssigned", 5),
          ("noPassiveData", 59),
          ("noStatusInPfxTimeout", 46),
          ("none", 1),
          ("oopModeSelectExitGood", 40),
          ("pbrBRTopologyChange", 20),
          ("pfrReqNotMet", 21),
          ("pfxEnabled", 11),
          ("policyChangedAddedNewFcdProbeTgt", 24),
          ("probeFrequencyChange", 22),
          ("probeNumPktsChanged", 60),
          ("recontrolNull0Pfx", 8),
          ("recontrolSinkHolePfx", 9),
          ("remoteStatsNotFound", 57),
          ("retryForcedNextHop", 45),
          ("tcInFastMode", 19),
          ("unableToSendControlMsg", 49),
          ("uncontrolModeMonitorChange", 12),
          ("uncontrolNonOptimizedPfx", 7),
          ("unhandledOopReasonInChooseExit", 39),
          ("unknownExit", 54),
          ("usingFcdTgtNow", 25),
          ("usingLmNow", 27))
    )



class PfRMasterControllerIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrBorderRouterIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrExitIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrMapIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrMapPolicyIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrMapIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class PfrLearnListIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PfrLearnListIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class PfrResolvePolicyType(Integer32, TextualConvention):
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
        *(("cost", 1),
          ("delay", 2),
          ("jitter", 3),
          ("loss", 4),
          ("mos", 5),
          ("none", 0),
          ("range", 6),
          ("utilization", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPfrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPfrMIBNotifs = _CiscoPfrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0)
)
_CiscoPfrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPfrMIBObjects = _CiscoPfrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1)
)
_CpfrMCTable_Object = MibTable
cpfrMCTable = _CpfrMCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1)
)
if mibBuilder.loadTexts:
    cpfrMCTable.setStatus("current")
_CpfrMCEntry_Object = MibTableRow
cpfrMCEntry = _CpfrMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1)
)
cpfrMCEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
)
if mibBuilder.loadTexts:
    cpfrMCEntry.setStatus("current")
_CpfrMCIndex_Type = PfRMasterControllerIndex
_CpfrMCIndex_Object = MibTableColumn
cpfrMCIndex = _CpfrMCIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 1),
    _CpfrMCIndex_Type()
)
cpfrMCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrMCIndex.setStatus("current")


class _CpfrMCStorageType_Type(StorageType):
    """Custom type cpfrMCStorageType based on StorageType"""


_CpfrMCStorageType_Object = MibTableColumn
cpfrMCStorageType = _CpfrMCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 2),
    _CpfrMCStorageType_Type()
)
cpfrMCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCStorageType.setStatus("current")
_CpfrMCRowStatus_Type = RowStatus
_CpfrMCRowStatus_Object = MibTableColumn
cpfrMCRowStatus = _CpfrMCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 3),
    _CpfrMCRowStatus_Type()
)
cpfrMCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCRowStatus.setStatus("current")


class _CpfrMCMapIndex_Type(PfrMapIndexOrZero):
    """Custom type cpfrMCMapIndex based on PfrMapIndexOrZero"""
    defaultValue = 0


_CpfrMCMapIndex_Object = MibTableColumn
cpfrMCMapIndex = _CpfrMCMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 4),
    _CpfrMCMapIndex_Type()
)
cpfrMCMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCMapIndex.setStatus("current")


class _CpfrMCKeepAliveTimer_Type(Unsigned32):
    """Custom type cpfrMCKeepAliveTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCKeepAliveTimer_Type.__name__ = "Unsigned32"
_CpfrMCKeepAliveTimer_Object = MibTableColumn
cpfrMCKeepAliveTimer = _CpfrMCKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 5),
    _CpfrMCKeepAliveTimer_Type()
)
cpfrMCKeepAliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCKeepAliveTimer.setUnits("seconds")


class _CpfrMCMaxPrefixTotal_Type(Unsigned32):
    """Custom type cpfrMCMaxPrefixTotal based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCMaxPrefixTotal_Type.__name__ = "Unsigned32"
_CpfrMCMaxPrefixTotal_Object = MibTableColumn
cpfrMCMaxPrefixTotal = _CpfrMCMaxPrefixTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 6),
    _CpfrMCMaxPrefixTotal_Type()
)
cpfrMCMaxPrefixTotal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCMaxPrefixTotal.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCMaxPrefixTotal.setUnits("prefixes")


class _CpfrMCMaxPrefixLearn_Type(Unsigned32):
    """Custom type cpfrMCMaxPrefixLearn based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCMaxPrefixLearn_Type.__name__ = "Unsigned32"
_CpfrMCMaxPrefixLearn_Object = MibTableColumn
cpfrMCMaxPrefixLearn = _CpfrMCMaxPrefixLearn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 7),
    _CpfrMCMaxPrefixLearn_Type()
)
cpfrMCMaxPrefixLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCMaxPrefixLearn.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCMaxPrefixLearn.setUnits("prefixes")


class _CpfrMCEntranceLinksMaxUtil_Type(Unsigned32):
    """Custom type cpfrMCEntranceLinksMaxUtil based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpfrMCEntranceLinksMaxUtil_Type.__name__ = "Unsigned32"
_CpfrMCEntranceLinksMaxUtil_Object = MibTableColumn
cpfrMCEntranceLinksMaxUtil = _CpfrMCEntranceLinksMaxUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 8),
    _CpfrMCEntranceLinksMaxUtil_Type()
)
cpfrMCEntranceLinksMaxUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCEntranceLinksMaxUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCEntranceLinksMaxUtil.setUnits("percent")


class _CpfrMCExitLinksMaxUtil_Type(Unsigned32):
    """Custom type cpfrMCExitLinksMaxUtil based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpfrMCExitLinksMaxUtil_Type.__name__ = "Unsigned32"
_CpfrMCExitLinksMaxUtil_Object = MibTableColumn
cpfrMCExitLinksMaxUtil = _CpfrMCExitLinksMaxUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 9),
    _CpfrMCExitLinksMaxUtil_Type()
)
cpfrMCExitLinksMaxUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCExitLinksMaxUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCExitLinksMaxUtil.setUnits("percent")


class _CpfrMCPortNumber_Type(InetPortNumber):
    """Custom type cpfrMCPortNumber based on InetPortNumber"""
    defaultValue = 3949


_CpfrMCPortNumber_Object = MibTableColumn
cpfrMCPortNumber = _CpfrMCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 10),
    _CpfrMCPortNumber_Type()
)
cpfrMCPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCPortNumber.setStatus("current")


class _CpfrMCTracerouteProbeDelay_Type(Unsigned32):
    """Custom type cpfrMCTracerouteProbeDelay based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCTracerouteProbeDelay_Type.__name__ = "Unsigned32"
_CpfrMCTracerouteProbeDelay_Object = MibTableColumn
cpfrMCTracerouteProbeDelay = _CpfrMCTracerouteProbeDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 11),
    _CpfrMCTracerouteProbeDelay_Type()
)
cpfrMCTracerouteProbeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCTracerouteProbeDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCTracerouteProbeDelay.setUnits("milliseconds")


class _CpfrMCRsvpPostDialDelay_Type(Unsigned32):
    """Custom type cpfrMCRsvpPostDialDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCRsvpPostDialDelay_Type.__name__ = "Unsigned32"
_CpfrMCRsvpPostDialDelay_Object = MibTableColumn
cpfrMCRsvpPostDialDelay = _CpfrMCRsvpPostDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 12),
    _CpfrMCRsvpPostDialDelay_Type()
)
cpfrMCRsvpPostDialDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCRsvpPostDialDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCRsvpPostDialDelay.setUnits("milliseconds")


class _CpfrMCRsvpSignalingRetries_Type(Unsigned32):
    """Custom type cpfrMCRsvpSignalingRetries based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCRsvpSignalingRetries_Type.__name__ = "Unsigned32"
_CpfrMCRsvpSignalingRetries_Object = MibTableColumn
cpfrMCRsvpSignalingRetries = _CpfrMCRsvpSignalingRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 13),
    _CpfrMCRsvpSignalingRetries_Type()
)
cpfrMCRsvpSignalingRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCRsvpSignalingRetries.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCRsvpSignalingRetries.setUnits("retries")
_CpfrMCNetflowExporter_Type = SnmpAdminString
_CpfrMCNetflowExporter_Object = MibTableColumn
cpfrMCNetflowExporter = _CpfrMCNetflowExporter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 14),
    _CpfrMCNetflowExporter_Type()
)
cpfrMCNetflowExporter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCNetflowExporter.setStatus("current")


class _CpfrMCAdminStatus_Type(Integer32):
    """Custom type cpfrMCAdminStatus based on Integer32"""
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


_CpfrMCAdminStatus_Type.__name__ = "Integer32"
_CpfrMCAdminStatus_Object = MibTableColumn
cpfrMCAdminStatus = _CpfrMCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 15),
    _CpfrMCAdminStatus_Type()
)
cpfrMCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCAdminStatus.setStatus("current")


class _CpfrMCOperStatus_Type(Integer32):
    """Custom type cpfrMCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CpfrMCOperStatus_Type.__name__ = "Integer32"
_CpfrMCOperStatus_Object = MibTableColumn
cpfrMCOperStatus = _CpfrMCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 16),
    _CpfrMCOperStatus_Type()
)
cpfrMCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCOperStatus.setStatus("current")


class _CpfrMCConnStatus_Type(Integer32):
    """Custom type cpfrMCConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("success", 1))
    )


_CpfrMCConnStatus_Type.__name__ = "Integer32"
_CpfrMCConnStatus_Object = MibTableColumn
cpfrMCConnStatus = _CpfrMCConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 17),
    _CpfrMCConnStatus_Type()
)
cpfrMCConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCConnStatus.setStatus("current")


class _CpfrMCNumofBorderRouters_Type(Gauge32):
    """Custom type cpfrMCNumofBorderRouters based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCNumofBorderRouters_Type.__name__ = "Gauge32"
_CpfrMCNumofBorderRouters_Object = MibTableColumn
cpfrMCNumofBorderRouters = _CpfrMCNumofBorderRouters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 18),
    _CpfrMCNumofBorderRouters_Type()
)
cpfrMCNumofBorderRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCNumofBorderRouters.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCNumofBorderRouters.setUnits("border routers")


class _CpfrMCNumofExits_Type(Gauge32):
    """Custom type cpfrMCNumofExits based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMCNumofExits_Type.__name__ = "Gauge32"
_CpfrMCNumofExits_Object = MibTableColumn
cpfrMCNumofExits = _CpfrMCNumofExits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 19),
    _CpfrMCNumofExits_Type()
)
cpfrMCNumofExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCNumofExits.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCNumofExits.setUnits("exits")


class _CpfrMCLearnState_Type(Integer32):
    """Custom type cpfrMCLearnState based on Integer32"""
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
        *(("disabled", 1),
          ("retry", 5),
          ("sleep", 4),
          ("started", 2),
          ("writing", 3))
    )


_CpfrMCLearnState_Type.__name__ = "Integer32"
_CpfrMCLearnState_Object = MibTableColumn
cpfrMCLearnState = _CpfrMCLearnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 20),
    _CpfrMCLearnState_Type()
)
cpfrMCLearnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCLearnState.setStatus("current")
_CpfrMCLearnStateTimeRemain_Type = Unsigned32
_CpfrMCLearnStateTimeRemain_Object = MibTableColumn
cpfrMCLearnStateTimeRemain = _CpfrMCLearnStateTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 21),
    _CpfrMCLearnStateTimeRemain_Type()
)
cpfrMCLearnStateTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCLearnStateTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCLearnStateTimeRemain.setUnits("seconds")
_CpfrMCPrefixCount_Type = Counter32
_CpfrMCPrefixCount_Object = MibTableColumn
cpfrMCPrefixCount = _CpfrMCPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 22),
    _CpfrMCPrefixCount_Type()
)
cpfrMCPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCPrefixCount.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCPrefixCount.setUnits("prefixes")
_CpfrMCPrefixLearned_Type = Counter32
_CpfrMCPrefixLearned_Object = MibTableColumn
cpfrMCPrefixLearned = _CpfrMCPrefixLearned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 23),
    _CpfrMCPrefixLearned_Type()
)
cpfrMCPrefixLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCPrefixLearned.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMCPrefixLearned.setUnits("prefixes")
_CpfrMCPrefixConfigured_Type = Counter32
_CpfrMCPrefixConfigured_Object = MibTableColumn
cpfrMCPrefixConfigured = _CpfrMCPrefixConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 24),
    _CpfrMCPrefixConfigured_Type()
)
cpfrMCPrefixConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCPrefixConfigured.setStatus("current")
_CpfrMCPbrMet_Type = TruthValue
_CpfrMCPbrMet_Object = MibTableColumn
cpfrMCPbrMet = _CpfrMCPbrMet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 25),
    _CpfrMCPbrMet_Type()
)
cpfrMCPbrMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCPbrMet.setStatus("current")


class _CpfrMCLoggingAdminStatus_Type(Integer32):
    """Custom type cpfrMCLoggingAdminStatus based on Integer32"""
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


_CpfrMCLoggingAdminStatus_Type.__name__ = "Integer32"
_CpfrMCLoggingAdminStatus_Object = MibTableColumn
cpfrMCLoggingAdminStatus = _CpfrMCLoggingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 26),
    _CpfrMCLoggingAdminStatus_Type()
)
cpfrMCLoggingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCLoggingAdminStatus.setStatus("current")


class _CpfrMCControlMode_Type(Integer32):
    """Custom type cpfrMCControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("observe", 1))
    )


_CpfrMCControlMode_Type.__name__ = "Integer32"
_CpfrMCControlMode_Object = MibTableColumn
cpfrMCControlMode = _CpfrMCControlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 27),
    _CpfrMCControlMode_Type()
)
cpfrMCControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCControlMode.setStatus("current")


class _CpfrMCClear_Type(Integer32):
    """Custom type cpfrMCClear based on Integer32"""
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
        *(("clearAll", 2),
          ("clearAllBorders", 4),
          ("clearAllPrefixes", 3),
          ("none", 1))
    )


_CpfrMCClear_Type.__name__ = "Integer32"
_CpfrMCClear_Object = MibTableColumn
cpfrMCClear = _CpfrMCClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 28),
    _CpfrMCClear_Type()
)
cpfrMCClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCClear.setStatus("current")
_CpfrMCLastClearTime_Type = TimeStamp
_CpfrMCLastClearTime_Object = MibTableColumn
cpfrMCLastClearTime = _CpfrMCLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 29),
    _CpfrMCLastClearTime_Type()
)
cpfrMCLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMCLastClearTime.setStatus("current")


class _CpfrMCNotifisControl_Type(Integer32):
    """Custom type cpfrMCNotifisControl based on Integer32"""
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


_CpfrMCNotifisControl_Type.__name__ = "Integer32"
_CpfrMCNotifisControl_Object = MibTableColumn
cpfrMCNotifisControl = _CpfrMCNotifisControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 30),
    _CpfrMCNotifisControl_Type()
)
cpfrMCNotifisControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMCNotifisControl.setStatus("current")


class _CpfrMCChangeConfigType_Type(Integer32):
    """Custom type cpfrMCChangeConfigType based on Integer32"""
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
        *(("cpfrMCAdminStatus", 2),
          ("cpfrMCClear", 4),
          ("cpfrMCControlMode", 3),
          ("cpfrMCLoggingAdminStatus", 1))
    )


_CpfrMCChangeConfigType_Type.__name__ = "Integer32"
_CpfrMCChangeConfigType_Object = MibTableColumn
cpfrMCChangeConfigType = _CpfrMCChangeConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 31),
    _CpfrMCChangeConfigType_Type()
)
cpfrMCChangeConfigType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cpfrMCChangeConfigType.setStatus("current")
_CpfrMCChangeConfigValue_Type = Integer32
_CpfrMCChangeConfigValue_Object = MibTableColumn
cpfrMCChangeConfigValue = _CpfrMCChangeConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 1, 1, 32),
    _CpfrMCChangeConfigValue_Type()
)
cpfrMCChangeConfigValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cpfrMCChangeConfigValue.setStatus("current")
_CpfrMapTable_Object = MibTable
cpfrMapTable = _CpfrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2)
)
if mibBuilder.loadTexts:
    cpfrMapTable.setStatus("current")
_CpfrMapEntry_Object = MibTableRow
cpfrMapEntry = _CpfrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1)
)
cpfrMapEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMapIndex"),
    (0, "CISCO-PFR-MIB", "cpfrMapPolicyIndex"),
)
if mibBuilder.loadTexts:
    cpfrMapEntry.setStatus("current")
_CpfrMapIndex_Type = PfrMapIndex
_CpfrMapIndex_Object = MibTableColumn
cpfrMapIndex = _CpfrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 1),
    _CpfrMapIndex_Type()
)
cpfrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrMapIndex.setStatus("current")
_CpfrMapPolicyIndex_Type = PfrMapPolicyIndex
_CpfrMapPolicyIndex_Object = MibTableColumn
cpfrMapPolicyIndex = _CpfrMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 2),
    _CpfrMapPolicyIndex_Type()
)
cpfrMapPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrMapPolicyIndex.setStatus("current")


class _CpfrMapStorageType_Type(StorageType):
    """Custom type cpfrMapStorageType based on StorageType"""


_CpfrMapStorageType_Object = MibTableColumn
cpfrMapStorageType = _CpfrMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 3),
    _CpfrMapStorageType_Type()
)
cpfrMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapStorageType.setStatus("current")
_CpfrMapRowStatus_Type = RowStatus
_CpfrMapRowStatus_Object = MibTableColumn
cpfrMapRowStatus = _CpfrMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 4),
    _CpfrMapRowStatus_Type()
)
cpfrMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapRowStatus.setStatus("current")
_CpfrMapName_Type = SnmpAdminString
_CpfrMapName_Object = MibTableColumn
cpfrMapName = _CpfrMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 5),
    _CpfrMapName_Type()
)
cpfrMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapName.setStatus("current")


class _CpfrMapBackoffMinTimer_Type(Unsigned32):
    """Custom type cpfrMapBackoffMinTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapBackoffMinTimer_Type.__name__ = "Unsigned32"
_CpfrMapBackoffMinTimer_Object = MibTableColumn
cpfrMapBackoffMinTimer = _CpfrMapBackoffMinTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 6),
    _CpfrMapBackoffMinTimer_Type()
)
cpfrMapBackoffMinTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapBackoffMinTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapBackoffMinTimer.setUnits("seconds")


class _CpfrMapBackoffMaxTimer_Type(Unsigned32):
    """Custom type cpfrMapBackoffMaxTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapBackoffMaxTimer_Type.__name__ = "Unsigned32"
_CpfrMapBackoffMaxTimer_Object = MibTableColumn
cpfrMapBackoffMaxTimer = _CpfrMapBackoffMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 7),
    _CpfrMapBackoffMaxTimer_Type()
)
cpfrMapBackoffMaxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapBackoffMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapBackoffMaxTimer.setUnits("seconds")


class _CpfrMapBackoffStepTimer_Type(Unsigned32):
    """Custom type cpfrMapBackoffStepTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapBackoffStepTimer_Type.__name__ = "Unsigned32"
_CpfrMapBackoffStepTimer_Object = MibTableColumn
cpfrMapBackoffStepTimer = _CpfrMapBackoffStepTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 8),
    _CpfrMapBackoffStepTimer_Type()
)
cpfrMapBackoffStepTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapBackoffStepTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapBackoffStepTimer.setUnits("seconds")
_CpfrMapDelayType_Type = PfrMetricPolicyType
_CpfrMapDelayType_Object = MibTableColumn
cpfrMapDelayType = _CpfrMapDelayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 9),
    _CpfrMapDelayType_Type()
)
cpfrMapDelayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapDelayType.setStatus("current")


class _CpfrMapDelayRelativePercent_Type(Unsigned32):
    """Custom type cpfrMapDelayRelativePercent based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CpfrMapDelayRelativePercent_Type.__name__ = "Unsigned32"
_CpfrMapDelayRelativePercent_Object = MibTableColumn
cpfrMapDelayRelativePercent = _CpfrMapDelayRelativePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 10),
    _CpfrMapDelayRelativePercent_Type()
)
cpfrMapDelayRelativePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapDelayRelativePercent.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapDelayRelativePercent.setUnits("tenths of percent")


class _CpfrMapDelayThresholdMax_Type(Unsigned32):
    """Custom type cpfrMapDelayThresholdMax based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapDelayThresholdMax_Type.__name__ = "Unsigned32"
_CpfrMapDelayThresholdMax_Object = MibTableColumn
cpfrMapDelayThresholdMax = _CpfrMapDelayThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 11),
    _CpfrMapDelayThresholdMax_Type()
)
cpfrMapDelayThresholdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapDelayThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapDelayThresholdMax.setUnits("milliseconds")


class _CpfrMapHolddownTimer_Type(Unsigned32):
    """Custom type cpfrMapHolddownTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapHolddownTimer_Type.__name__ = "Unsigned32"
_CpfrMapHolddownTimer_Object = MibTableColumn
cpfrMapHolddownTimer = _CpfrMapHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 12),
    _CpfrMapHolddownTimer_Type()
)
cpfrMapHolddownTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapHolddownTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapHolddownTimer.setUnits("seconds")


class _CpfrMapPrefixForwardInterface_Type(InterfaceIndexOrZero):
    """Custom type cpfrMapPrefixForwardInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CpfrMapPrefixForwardInterface_Object = MibTableColumn
cpfrMapPrefixForwardInterface = _CpfrMapPrefixForwardInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 13),
    _CpfrMapPrefixForwardInterface_Type()
)
cpfrMapPrefixForwardInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapPrefixForwardInterface.setStatus("current")


class _CpfrMapJitterThresholdMax_Type(Unsigned32):
    """Custom type cpfrMapJitterThresholdMax based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapJitterThresholdMax_Type.__name__ = "Unsigned32"
_CpfrMapJitterThresholdMax_Object = MibTableColumn
cpfrMapJitterThresholdMax = _CpfrMapJitterThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 14),
    _CpfrMapJitterThresholdMax_Type()
)
cpfrMapJitterThresholdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapJitterThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapJitterThresholdMax.setUnits("milliseconds")
_CpfrMapLinkGroupName_Type = SnmpAdminString
_CpfrMapLinkGroupName_Object = MibTableColumn
cpfrMapLinkGroupName = _CpfrMapLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 15),
    _CpfrMapLinkGroupName_Type()
)
cpfrMapLinkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapLinkGroupName.setStatus("current")
_CpfrMapFallbackLinkGroupName_Type = SnmpAdminString
_CpfrMapFallbackLinkGroupName_Object = MibTableColumn
cpfrMapFallbackLinkGroupName = _CpfrMapFallbackLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 16),
    _CpfrMapFallbackLinkGroupName_Type()
)
cpfrMapFallbackLinkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapFallbackLinkGroupName.setStatus("current")
_CpfrMapLossType_Type = PfrMetricPolicyType
_CpfrMapLossType_Object = MibTableColumn
cpfrMapLossType = _CpfrMapLossType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 17),
    _CpfrMapLossType_Type()
)
cpfrMapLossType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapLossType.setStatus("current")


class _CpfrMapLossRelativeAvg_Type(Unsigned32):
    """Custom type cpfrMapLossRelativeAvg based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapLossRelativeAvg_Type.__name__ = "Unsigned32"
_CpfrMapLossRelativeAvg_Object = MibTableColumn
cpfrMapLossRelativeAvg = _CpfrMapLossRelativeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 18),
    _CpfrMapLossRelativeAvg_Type()
)
cpfrMapLossRelativeAvg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapLossRelativeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapLossRelativeAvg.setUnits("tenths of percent")


class _CpfrMapLossThresholdMax_Type(Unsigned32):
    """Custom type cpfrMapLossThresholdMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapLossThresholdMax_Type.__name__ = "Unsigned32"
_CpfrMapLossThresholdMax_Object = MibTableColumn
cpfrMapLossThresholdMax = _CpfrMapLossThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 19),
    _CpfrMapLossThresholdMax_Type()
)
cpfrMapLossThresholdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapLossThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapLossThresholdMax.setUnits("packets-per-million")


class _CpfrMapModeMonitor_Type(Integer32):
    """Custom type cpfrMapModeMonitor based on Integer32"""
    defaultValue = 3

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
        *(("active", 1),
          ("activeThroughput", 2),
          ("both", 3),
          ("fast", 4),
          ("passive", 5))
    )


_CpfrMapModeMonitor_Type.__name__ = "Integer32"
_CpfrMapModeMonitor_Object = MibTableColumn
cpfrMapModeMonitor = _CpfrMapModeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 20),
    _CpfrMapModeMonitor_Type()
)
cpfrMapModeMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapModeMonitor.setStatus("current")


class _CpfrMapModeRouteOpts_Type(Integer32):
    """Custom type cpfrMapModeRouteOpts based on Integer32"""
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
        *(("control", 1),
          ("metric", 3),
          ("observe", 2))
    )


_CpfrMapModeRouteOpts_Type.__name__ = "Integer32"
_CpfrMapModeRouteOpts_Object = MibTableColumn
cpfrMapModeRouteOpts = _CpfrMapModeRouteOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 21),
    _CpfrMapModeRouteOpts_Type()
)
cpfrMapModeRouteOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapModeRouteOpts.setStatus("current")


class _CpfrMapRouteMetricBgpLocalPref_Type(Unsigned32):
    """Custom type cpfrMapRouteMetricBgpLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapRouteMetricBgpLocalPref_Type.__name__ = "Unsigned32"
_CpfrMapRouteMetricBgpLocalPref_Object = MibTableColumn
cpfrMapRouteMetricBgpLocalPref = _CpfrMapRouteMetricBgpLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 22),
    _CpfrMapRouteMetricBgpLocalPref_Type()
)
cpfrMapRouteMetricBgpLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapRouteMetricBgpLocalPref.setStatus("current")


class _CpfrMapRouteMetricEigrpTagCommunity_Type(Unsigned32):
    """Custom type cpfrMapRouteMetricEigrpTagCommunity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapRouteMetricEigrpTagCommunity_Type.__name__ = "Unsigned32"
_CpfrMapRouteMetricEigrpTagCommunity_Object = MibTableColumn
cpfrMapRouteMetricEigrpTagCommunity = _CpfrMapRouteMetricEigrpTagCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 23),
    _CpfrMapRouteMetricEigrpTagCommunity_Type()
)
cpfrMapRouteMetricEigrpTagCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapRouteMetricEigrpTagCommunity.setStatus("current")


class _CpfrMapRouteMetricStaticTag_Type(Unsigned32):
    """Custom type cpfrMapRouteMetricStaticTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapRouteMetricStaticTag_Type.__name__ = "Unsigned32"
_CpfrMapRouteMetricStaticTag_Object = MibTableColumn
cpfrMapRouteMetricStaticTag = _CpfrMapRouteMetricStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 24),
    _CpfrMapRouteMetricStaticTag_Type()
)
cpfrMapRouteMetricStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapRouteMetricStaticTag.setStatus("current")


class _CpfrMapModeSelectExitType_Type(Integer32):
    """Custom type cpfrMapModeSelectExitType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("best", 1),
          ("good", 2))
    )


_CpfrMapModeSelectExitType_Type.__name__ = "Integer32"
_CpfrMapModeSelectExitType_Object = MibTableColumn
cpfrMapModeSelectExitType = _CpfrMapModeSelectExitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 25),
    _CpfrMapModeSelectExitType_Type()
)
cpfrMapModeSelectExitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapModeSelectExitType.setStatus("current")


class _CpfrMapMOSThresholdMin_Type(Unsigned32):
    """Custom type cpfrMapMOSThresholdMin based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapMOSThresholdMin_Type.__name__ = "Unsigned32"
_CpfrMapMOSThresholdMin_Object = MibTableColumn
cpfrMapMOSThresholdMin = _CpfrMapMOSThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 26),
    _CpfrMapMOSThresholdMin_Type()
)
cpfrMapMOSThresholdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapMOSThresholdMin.setStatus("current")


class _CpfrMapMOSPercentage_Type(Unsigned32):
    """Custom type cpfrMapMOSPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapMOSPercentage_Type.__name__ = "Unsigned32"
_CpfrMapMOSPercentage_Object = MibTableColumn
cpfrMapMOSPercentage = _CpfrMapMOSPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 27),
    _CpfrMapMOSPercentage_Type()
)
cpfrMapMOSPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapMOSPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapMOSPercentage.setUnits("percent")
_CpfrMapNextHopAddressType_Type = InetAddressType
_CpfrMapNextHopAddressType_Object = MibTableColumn
cpfrMapNextHopAddressType = _CpfrMapNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 28),
    _CpfrMapNextHopAddressType_Type()
)
cpfrMapNextHopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapNextHopAddressType.setStatus("current")
_CpfrMapNextHopAddress_Type = InetAddress
_CpfrMapNextHopAddress_Object = MibTableColumn
cpfrMapNextHopAddress = _CpfrMapNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 29),
    _CpfrMapNextHopAddress_Type()
)
cpfrMapNextHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapNextHopAddress.setStatus("current")


class _CpfrMapPeriodicTimer_Type(Unsigned32):
    """Custom type cpfrMapPeriodicTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapPeriodicTimer_Type.__name__ = "Unsigned32"
_CpfrMapPeriodicTimer_Object = MibTableColumn
cpfrMapPeriodicTimer = _CpfrMapPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 30),
    _CpfrMapPeriodicTimer_Type()
)
cpfrMapPeriodicTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapPeriodicTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapPeriodicTimer.setUnits("seconds")


class _CpfrMapActiveProbeFrequency_Type(Unsigned32):
    """Custom type cpfrMapActiveProbeFrequency based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapActiveProbeFrequency_Type.__name__ = "Unsigned32"
_CpfrMapActiveProbeFrequency_Object = MibTableColumn
cpfrMapActiveProbeFrequency = _CpfrMapActiveProbeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 31),
    _CpfrMapActiveProbeFrequency_Type()
)
cpfrMapActiveProbeFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapActiveProbeFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapActiveProbeFrequency.setUnits("seconds")


class _CpfrMapActiveProbePackets_Type(Unsigned32):
    """Custom type cpfrMapActiveProbePackets based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapActiveProbePackets_Type.__name__ = "Unsigned32"
_CpfrMapActiveProbePackets_Object = MibTableColumn
cpfrMapActiveProbePackets = _CpfrMapActiveProbePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 32),
    _CpfrMapActiveProbePackets_Type()
)
cpfrMapActiveProbePackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapActiveProbePackets.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapActiveProbePackets.setUnits("packets")


class _CpfrMapTracerouteReporting_Type(Bits):
    """Custom type cpfrMapTracerouteReporting based on Bits"""
    namedValues = NamedValues(
        *(("delay", 1),
          ("loss", 2),
          ("none", 0),
          ("unreachable", 3))
    )

_CpfrMapTracerouteReporting_Type.__name__ = "Bits"
_CpfrMapTracerouteReporting_Object = MibTableColumn
cpfrMapTracerouteReporting = _CpfrMapTracerouteReporting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 33),
    _CpfrMapTracerouteReporting_Type()
)
cpfrMapTracerouteReporting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapTracerouteReporting.setStatus("current")


class _CpfrMapUnreachableType_Type(PfrMetricPolicyType):
    """Custom type cpfrMapUnreachableType based on PfrMetricPolicyType"""


_CpfrMapUnreachableType_Object = MibTableColumn
cpfrMapUnreachableType = _CpfrMapUnreachableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 34),
    _CpfrMapUnreachableType_Type()
)
cpfrMapUnreachableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapUnreachableType.setStatus("current")


class _CpfrMapUnreachableRelativeAvg_Type(Unsigned32):
    """Custom type cpfrMapUnreachableRelativeAvg based on Unsigned32"""
    defaultValue = 50


_CpfrMapUnreachableRelativeAvg_Object = MibTableColumn
cpfrMapUnreachableRelativeAvg = _CpfrMapUnreachableRelativeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 35),
    _CpfrMapUnreachableRelativeAvg_Type()
)
cpfrMapUnreachableRelativeAvg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapUnreachableRelativeAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapUnreachableRelativeAvg.setUnits("tenths of percent")


class _CpfrMapUnreachableThresholdMax_Type(Unsigned32):
    """Custom type cpfrMapUnreachableThresholdMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrMapUnreachableThresholdMax_Type.__name__ = "Unsigned32"
_CpfrMapUnreachableThresholdMax_Object = MibTableColumn
cpfrMapUnreachableThresholdMax = _CpfrMapUnreachableThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 36),
    _CpfrMapUnreachableThresholdMax_Type()
)
cpfrMapUnreachableThresholdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapUnreachableThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cpfrMapUnreachableThresholdMax.setUnits("flows per million")


class _CpfrMapRoundRobinResolver_Type(Integer32):
    """Custom type cpfrMapRoundRobinResolver based on Integer32"""
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


_CpfrMapRoundRobinResolver_Type.__name__ = "Integer32"
_CpfrMapRoundRobinResolver_Object = MibTableColumn
cpfrMapRoundRobinResolver = _CpfrMapRoundRobinResolver_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 37),
    _CpfrMapRoundRobinResolver_Type()
)
cpfrMapRoundRobinResolver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapRoundRobinResolver.setStatus("current")


class _CpfrMapEventNotifCtrlType_Type(PfrMetricPolicyType):
    """Custom type cpfrMapEventNotifCtrlType based on PfrMetricPolicyType"""


_CpfrMapEventNotifCtrlType_Object = MibTableColumn
cpfrMapEventNotifCtrlType = _CpfrMapEventNotifCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 38),
    _CpfrMapEventNotifCtrlType_Type()
)
cpfrMapEventNotifCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapEventNotifCtrlType.setStatus("current")
_CpfrMapEventNotifCtrlThreshold_Type = Unsigned32
_CpfrMapEventNotifCtrlThreshold_Object = MibTableColumn
cpfrMapEventNotifCtrlThreshold = _CpfrMapEventNotifCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 39),
    _CpfrMapEventNotifCtrlThreshold_Type()
)
cpfrMapEventNotifCtrlThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrMapEventNotifCtrlThreshold.setStatus("current")
_CpfrMapEventTCCount_Type = Unsigned32
_CpfrMapEventTCCount_Object = MibTableColumn
cpfrMapEventTCCount = _CpfrMapEventTCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 2, 1, 40),
    _CpfrMapEventTCCount_Type()
)
cpfrMapEventTCCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMapEventTCCount.setStatus("current")
_CpfrMatchTable_Object = MibTable
cpfrMatchTable = _CpfrMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3)
)
if mibBuilder.loadTexts:
    cpfrMatchTable.setStatus("current")
_CpfrMatchEntry_Object = MibTableRow
cpfrMatchEntry = _CpfrMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1)
)
cpfrMatchEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMapIndex"),
    (0, "CISCO-PFR-MIB", "cpfrMapPolicyIndex"),
)
if mibBuilder.loadTexts:
    cpfrMatchEntry.setStatus("current")


class _CpfrMatchValid_Type(Bits):
    """Custom type cpfrMatchValid based on Bits"""
    namedValues = NamedValues(
        *(("accessList", 0),
          ("learn", 2),
          ("nbarApplicationList", 4),
          ("prefixList", 1),
          ("trafficClassACL", 3),
          ("trafficClassPfx", 5))
    )

_CpfrMatchValid_Type.__name__ = "Bits"
_CpfrMatchValid_Object = MibTableColumn
cpfrMatchValid = _CpfrMatchValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 1),
    _CpfrMatchValid_Type()
)
cpfrMatchValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchValid.setStatus("current")
_CpfrMatchAddrAccessList_Type = SnmpAdminString
_CpfrMatchAddrAccessList_Object = MibTableColumn
cpfrMatchAddrAccessList = _CpfrMatchAddrAccessList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 2),
    _CpfrMatchAddrAccessList_Type()
)
cpfrMatchAddrAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchAddrAccessList.setStatus("current")
_CpfrMatchAddrPrefixList_Type = SnmpAdminString
_CpfrMatchAddrPrefixList_Object = MibTableColumn
cpfrMatchAddrPrefixList = _CpfrMatchAddrPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 3),
    _CpfrMatchAddrPrefixList_Type()
)
cpfrMatchAddrPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchAddrPrefixList.setStatus("current")


class _CpfrMatchAddrPrefixInside_Type(TruthValue):
    """Custom type cpfrMatchAddrPrefixInside based on TruthValue"""


_CpfrMatchAddrPrefixInside_Object = MibTableColumn
cpfrMatchAddrPrefixInside = _CpfrMatchAddrPrefixInside_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 4),
    _CpfrMatchAddrPrefixInside_Type()
)
cpfrMatchAddrPrefixInside.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchAddrPrefixInside.setStatus("current")


class _CpfrMatchLearnMode_Type(Integer32):
    """Custom type cpfrMatchLearnMode based on Integer32"""
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
        *(("delay", 1),
          ("inside", 2),
          ("list", 4),
          ("throughput", 3))
    )


_CpfrMatchLearnMode_Type.__name__ = "Integer32"
_CpfrMatchLearnMode_Object = MibTableColumn
cpfrMatchLearnMode = _CpfrMatchLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 5),
    _CpfrMatchLearnMode_Type()
)
cpfrMatchLearnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchLearnMode.setStatus("current")
_CpfrMatchLearnListName_Type = SnmpAdminString
_CpfrMatchLearnListName_Object = MibTableColumn
cpfrMatchLearnListName = _CpfrMatchLearnListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 6),
    _CpfrMatchLearnListName_Type()
)
cpfrMatchLearnListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchLearnListName.setStatus("current")
_CpfrMatchTCNbarListName_Type = SnmpAdminString
_CpfrMatchTCNbarListName_Object = MibTableColumn
cpfrMatchTCNbarListName = _CpfrMatchTCNbarListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 7),
    _CpfrMatchTCNbarListName_Type()
)
cpfrMatchTCNbarListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchTCNbarListName.setStatus("current")
_CpfrMatchTCNbarApplPfxList_Type = SnmpAdminString
_CpfrMatchTCNbarApplPfxList_Object = MibTableColumn
cpfrMatchTCNbarApplPfxList = _CpfrMatchTCNbarApplPfxList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 8),
    _CpfrMatchTCNbarApplPfxList_Type()
)
cpfrMatchTCNbarApplPfxList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchTCNbarApplPfxList.setStatus("current")


class _CpfrMatchTCPfxInside_Type(TruthValue):
    """Custom type cpfrMatchTCPfxInside based on TruthValue"""


_CpfrMatchTCPfxInside_Object = MibTableColumn
cpfrMatchTCPfxInside = _CpfrMatchTCPfxInside_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 3, 1, 9),
    _CpfrMatchTCPfxInside_Type()
)
cpfrMatchTCPfxInside.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrMatchTCPfxInside.setStatus("current")
_CpfrResolveTable_Object = MibTable
cpfrResolveTable = _CpfrResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4)
)
if mibBuilder.loadTexts:
    cpfrResolveTable.setStatus("current")
_CpfrResolveEntry_Object = MibTableRow
cpfrResolveEntry = _CpfrResolveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1)
)
cpfrResolveEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrResolveIndex"),
)
if mibBuilder.loadTexts:
    cpfrResolveEntry.setStatus("current")


class _CpfrResolveIndex_Type(Unsigned32):
    """Custom type cpfrResolveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpfrResolveIndex_Type.__name__ = "Unsigned32"
_CpfrResolveIndex_Object = MibTableColumn
cpfrResolveIndex = _CpfrResolveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 1),
    _CpfrResolveIndex_Type()
)
cpfrResolveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrResolveIndex.setStatus("current")


class _CpfrResolveStorageType_Type(StorageType):
    """Custom type cpfrResolveStorageType based on StorageType"""


_CpfrResolveStorageType_Object = MibTableColumn
cpfrResolveStorageType = _CpfrResolveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 2),
    _CpfrResolveStorageType_Type()
)
cpfrResolveStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolveStorageType.setStatus("current")
_CpfrResolveRowStatus_Type = RowStatus
_CpfrResolveRowStatus_Object = MibTableColumn
cpfrResolveRowStatus = _CpfrResolveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 3),
    _CpfrResolveRowStatus_Type()
)
cpfrResolveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolveRowStatus.setStatus("current")


class _CpfrResolvePriority_Type(Unsigned32):
    """Custom type cpfrResolvePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrResolvePriority_Type.__name__ = "Unsigned32"
_CpfrResolvePriority_Object = MibTableColumn
cpfrResolvePriority = _CpfrResolvePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 4),
    _CpfrResolvePriority_Type()
)
cpfrResolvePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolvePriority.setStatus("current")


class _CpfrResolvePolicyType_Type(PfrResolvePolicyType):
    """Custom type cpfrResolvePolicyType based on PfrResolvePolicyType"""


_CpfrResolvePolicyType_Object = MibTableColumn
cpfrResolvePolicyType = _CpfrResolvePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 5),
    _CpfrResolvePolicyType_Type()
)
cpfrResolvePolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolvePolicyType.setStatus("current")


class _CpfrResolveVariance_Type(Unsigned32):
    """Custom type cpfrResolveVariance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrResolveVariance_Type.__name__ = "Unsigned32"
_CpfrResolveVariance_Object = MibTableColumn
cpfrResolveVariance = _CpfrResolveVariance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 6),
    _CpfrResolveVariance_Type()
)
cpfrResolveVariance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolveVariance.setStatus("current")


class _CpfrResolveMapIndex_Type(PfrMapIndexOrZero):
    """Custom type cpfrResolveMapIndex based on PfrMapIndexOrZero"""
    defaultValue = 0


_CpfrResolveMapIndex_Object = MibTableColumn
cpfrResolveMapIndex = _CpfrResolveMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 7),
    _CpfrResolveMapIndex_Type()
)
cpfrResolveMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolveMapIndex.setStatus("current")
_CpfrResolveMapPolicyIndex_Type = PfrMapPolicyIndex
_CpfrResolveMapPolicyIndex_Object = MibTableColumn
cpfrResolveMapPolicyIndex = _CpfrResolveMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 4, 1, 8),
    _CpfrResolveMapPolicyIndex_Type()
)
cpfrResolveMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrResolveMapPolicyIndex.setStatus("current")
if mibBuilder.loadTexts:
    cpfrResolveMapPolicyIndex.setUnits("0")
_CpfrLearnTable_Object = MibTable
cpfrLearnTable = _CpfrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5)
)
if mibBuilder.loadTexts:
    cpfrLearnTable.setStatus("current")
_CpfrLearnEntry_Object = MibTableRow
cpfrLearnEntry = _CpfrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1)
)
cpfrLearnEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
)
if mibBuilder.loadTexts:
    cpfrLearnEntry.setStatus("current")


class _CpfrLearnAggregationType_Type(Integer32):
    """Custom type cpfrLearnAggregationType based on Integer32"""
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
        *(("bgp", 1),
          ("nonBgp", 2),
          ("prefixLength", 3))
    )


_CpfrLearnAggregationType_Type.__name__ = "Integer32"
_CpfrLearnAggregationType_Object = MibTableColumn
cpfrLearnAggregationType = _CpfrLearnAggregationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 1),
    _CpfrLearnAggregationType_Type()
)
cpfrLearnAggregationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnAggregationType.setStatus("current")


class _CpfrLearnAggregationPrefixLen_Type(Unsigned32):
    """Custom type cpfrLearnAggregationPrefixLen based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnAggregationPrefixLen_Type.__name__ = "Unsigned32"
_CpfrLearnAggregationPrefixLen_Object = MibTableColumn
cpfrLearnAggregationPrefixLen = _CpfrLearnAggregationPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 2),
    _CpfrLearnAggregationPrefixLen_Type()
)
cpfrLearnAggregationPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnAggregationPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnAggregationPrefixLen.setUnits("bits")


class _CpfrLearnMethod_Type(Bits):
    """Custom type cpfrLearnMethod based on Bits"""
    namedValues = NamedValues(
        *(("delay", 0),
          ("insideBgp", 2),
          ("throughput", 1))
    )

_CpfrLearnMethod_Type.__name__ = "Bits"
_CpfrLearnMethod_Object = MibTableColumn
cpfrLearnMethod = _CpfrLearnMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 3),
    _CpfrLearnMethod_Type()
)
cpfrLearnMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnMethod.setStatus("current")


class _CpfrLearnExpireType_Type(Integer32):
    """Custom type cpfrLearnExpireType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("session", 1),
          ("time", 2))
    )


_CpfrLearnExpireType_Type.__name__ = "Integer32"
_CpfrLearnExpireType_Object = MibTableColumn
cpfrLearnExpireType = _CpfrLearnExpireType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 4),
    _CpfrLearnExpireType_Type()
)
cpfrLearnExpireType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnExpireType.setStatus("current")


class _CpfrLearnExpireSessionNum_Type(Unsigned32):
    """Custom type cpfrLearnExpireSessionNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnExpireSessionNum_Type.__name__ = "Unsigned32"
_CpfrLearnExpireSessionNum_Object = MibTableColumn
cpfrLearnExpireSessionNum = _CpfrLearnExpireSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 5),
    _CpfrLearnExpireSessionNum_Type()
)
cpfrLearnExpireSessionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnExpireSessionNum.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnExpireSessionNum.setUnits("monitoring periods")


class _CpfrLearnExpireTime_Type(Unsigned32):
    """Custom type cpfrLearnExpireTime based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnExpireTime_Type.__name__ = "Unsigned32"
_CpfrLearnExpireTime_Object = MibTableColumn
cpfrLearnExpireTime = _CpfrLearnExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 6),
    _CpfrLearnExpireTime_Type()
)
cpfrLearnExpireTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnExpireTime.setUnits("minutes")


class _CpfrLearnMonitorPeriod_Type(Unsigned32):
    """Custom type cpfrLearnMonitorPeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnMonitorPeriod_Type.__name__ = "Unsigned32"
_CpfrLearnMonitorPeriod_Object = MibTableColumn
cpfrLearnMonitorPeriod = _CpfrLearnMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 7),
    _CpfrLearnMonitorPeriod_Type()
)
cpfrLearnMonitorPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnMonitorPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnMonitorPeriod.setUnits("minutes")


class _CpfrLearnPeriodInterval_Type(Unsigned32):
    """Custom type cpfrLearnPeriodInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnPeriodInterval_Type.__name__ = "Unsigned32"
_CpfrLearnPeriodInterval_Object = MibTableColumn
cpfrLearnPeriodInterval = _CpfrLearnPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 8),
    _CpfrLearnPeriodInterval_Type()
)
cpfrLearnPeriodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnPeriodInterval.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnPeriodInterval.setUnits("minutes")


class _CpfrLearnPrefixesNumber_Type(Unsigned32):
    """Custom type cpfrLearnPrefixesNumber based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnPrefixesNumber_Type.__name__ = "Unsigned32"
_CpfrLearnPrefixesNumber_Object = MibTableColumn
cpfrLearnPrefixesNumber = _CpfrLearnPrefixesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 9),
    _CpfrLearnPrefixesNumber_Type()
)
cpfrLearnPrefixesNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnPrefixesNumber.setStatus("current")
if mibBuilder.loadTexts:
    cpfrLearnPrefixesNumber.setUnits("prefixes")
_CpfrLearnAggAccesslistName_Type = SnmpAdminString
_CpfrLearnAggAccesslistName_Object = MibTableColumn
cpfrLearnAggAccesslistName = _CpfrLearnAggAccesslistName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 10),
    _CpfrLearnAggAccesslistName_Type()
)
cpfrLearnAggAccesslistName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnAggAccesslistName.setStatus("current")
_CpfrLearnFilterAccessListName_Type = SnmpAdminString
_CpfrLearnFilterAccessListName_Object = MibTableColumn
cpfrLearnFilterAccessListName = _CpfrLearnFilterAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 5, 1, 11),
    _CpfrLearnFilterAccessListName_Type()
)
cpfrLearnFilterAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnFilterAccessListName.setStatus("current")
_CpfrLearnListTable_Object = MibTable
cpfrLearnListTable = _CpfrLearnListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6)
)
if mibBuilder.loadTexts:
    cpfrLearnListTable.setStatus("current")
_CpfrLearnListEntry_Object = MibTableRow
cpfrLearnListEntry = _CpfrLearnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1)
)
cpfrLearnListEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrLearnListIndex"),
)
if mibBuilder.loadTexts:
    cpfrLearnListEntry.setStatus("current")
_CpfrLearnListIndex_Type = PfrLearnListIndex
_CpfrLearnListIndex_Object = MibTableColumn
cpfrLearnListIndex = _CpfrLearnListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 1),
    _CpfrLearnListIndex_Type()
)
cpfrLearnListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrLearnListIndex.setStatus("current")


class _CpfrLearnListStorageType_Type(StorageType):
    """Custom type cpfrLearnListStorageType based on StorageType"""


_CpfrLearnListStorageType_Object = MibTableColumn
cpfrLearnListStorageType = _CpfrLearnListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 2),
    _CpfrLearnListStorageType_Type()
)
cpfrLearnListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListStorageType.setStatus("current")
_CpfrLearnListRowStatus_Type = RowStatus
_CpfrLearnListRowStatus_Object = MibTableColumn
cpfrLearnListRowStatus = _CpfrLearnListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 3),
    _CpfrLearnListRowStatus_Type()
)
cpfrLearnListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListRowStatus.setStatus("current")
_CpfrLearnListReferenceName_Type = SnmpAdminString
_CpfrLearnListReferenceName_Object = MibTableColumn
cpfrLearnListReferenceName = _CpfrLearnListReferenceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 4),
    _CpfrLearnListReferenceName_Type()
)
cpfrLearnListReferenceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListReferenceName.setStatus("current")


class _CpfrLearnListSequenceNum_Type(Unsigned32):
    """Custom type cpfrLearnListSequenceNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrLearnListSequenceNum_Type.__name__ = "Unsigned32"
_CpfrLearnListSequenceNum_Object = MibTableColumn
cpfrLearnListSequenceNum = _CpfrLearnListSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 5),
    _CpfrLearnListSequenceNum_Type()
)
cpfrLearnListSequenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListSequenceNum.setStatus("current")


class _CpfrLearnListMethod_Type(Bits):
    """Custom type cpfrLearnListMethod based on Bits"""
    namedValues = NamedValues(
        *(("delay", 0),
          ("rsvp", 2),
          ("throughput", 1))
    )

_CpfrLearnListMethod_Type.__name__ = "Bits"
_CpfrLearnListMethod_Object = MibTableColumn
cpfrLearnListMethod = _CpfrLearnListMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 6),
    _CpfrLearnListMethod_Type()
)
cpfrLearnListMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListMethod.setStatus("current")
_CpfrLearnListAclName_Type = SnmpAdminString
_CpfrLearnListAclName_Object = MibTableColumn
cpfrLearnListAclName = _CpfrLearnListAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 7),
    _CpfrLearnListAclName_Type()
)
cpfrLearnListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListAclName.setStatus("current")
_CpfrLearnListPfxName_Type = SnmpAdminString
_CpfrLearnListPfxName_Object = MibTableColumn
cpfrLearnListPfxName = _CpfrLearnListPfxName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 8),
    _CpfrLearnListPfxName_Type()
)
cpfrLearnListPfxName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListPfxName.setStatus("current")


class _CpfrLearnListPfxInside_Type(TruthValue):
    """Custom type cpfrLearnListPfxInside based on TruthValue"""


_CpfrLearnListPfxInside_Object = MibTableColumn
cpfrLearnListPfxInside = _CpfrLearnListPfxInside_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 9),
    _CpfrLearnListPfxInside_Type()
)
cpfrLearnListPfxInside.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListPfxInside.setStatus("current")
_CpfrLearnListNbarAppl_Type = SnmpAdminString
_CpfrLearnListNbarAppl_Object = MibTableColumn
cpfrLearnListNbarAppl = _CpfrLearnListNbarAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 10),
    _CpfrLearnListNbarAppl_Type()
)
cpfrLearnListNbarAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListNbarAppl.setStatus("current")
_CpfrLearnListFilterPfxName_Type = SnmpAdminString
_CpfrLearnListFilterPfxName_Object = MibTableColumn
cpfrLearnListFilterPfxName = _CpfrLearnListFilterPfxName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 6, 1, 11),
    _CpfrLearnListFilterPfxName_Type()
)
cpfrLearnListFilterPfxName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLearnListFilterPfxName.setStatus("current")
_CpfrActiveProbeTable_Object = MibTable
cpfrActiveProbeTable = _CpfrActiveProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7)
)
if mibBuilder.loadTexts:
    cpfrActiveProbeTable.setStatus("current")
_CpfrActiveProbeEntry_Object = MibTableRow
cpfrActiveProbeEntry = _CpfrActiveProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1)
)
cpfrActiveProbeEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrActiveProbeIndex"),
)
if mibBuilder.loadTexts:
    cpfrActiveProbeEntry.setStatus("current")


class _CpfrActiveProbeIndex_Type(Unsigned32):
    """Custom type cpfrActiveProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpfrActiveProbeIndex_Type.__name__ = "Unsigned32"
_CpfrActiveProbeIndex_Object = MibTableColumn
cpfrActiveProbeIndex = _CpfrActiveProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 1),
    _CpfrActiveProbeIndex_Type()
)
cpfrActiveProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrActiveProbeIndex.setStatus("current")


class _CpfrActiveProbeStorageType_Type(StorageType):
    """Custom type cpfrActiveProbeStorageType based on StorageType"""


_CpfrActiveProbeStorageType_Object = MibTableColumn
cpfrActiveProbeStorageType = _CpfrActiveProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 2),
    _CpfrActiveProbeStorageType_Type()
)
cpfrActiveProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeStorageType.setStatus("current")
_CpfrActiveProbeRowStatus_Type = RowStatus
_CpfrActiveProbeRowStatus_Object = MibTableColumn
cpfrActiveProbeRowStatus = _CpfrActiveProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 3),
    _CpfrActiveProbeRowStatus_Type()
)
cpfrActiveProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeRowStatus.setStatus("current")


class _CpfrActiveProbeType_Type(Integer32):
    """Custom type cpfrActiveProbeType based on Integer32"""
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
        *(("echo", 1),
          ("jitter", 2),
          ("tcpConn", 3),
          ("udpEcho", 4))
    )


_CpfrActiveProbeType_Type.__name__ = "Integer32"
_CpfrActiveProbeType_Object = MibTableColumn
cpfrActiveProbeType = _CpfrActiveProbeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 4),
    _CpfrActiveProbeType_Type()
)
cpfrActiveProbeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeType.setStatus("current")
_CpfrActiveProbeTargetAddressType_Type = InetAddressType
_CpfrActiveProbeTargetAddressType_Object = MibTableColumn
cpfrActiveProbeTargetAddressType = _CpfrActiveProbeTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 5),
    _CpfrActiveProbeTargetAddressType_Type()
)
cpfrActiveProbeTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeTargetAddressType.setStatus("current")
_CpfrActiveProbeTargetAddress_Type = InetAddress
_CpfrActiveProbeTargetAddress_Object = MibTableColumn
cpfrActiveProbeTargetAddress = _CpfrActiveProbeTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 6),
    _CpfrActiveProbeTargetAddress_Type()
)
cpfrActiveProbeTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeTargetAddress.setStatus("current")
_CpfrActiveProbeTargetPortNumber_Type = CiscoPort
_CpfrActiveProbeTargetPortNumber_Object = MibTableColumn
cpfrActiveProbeTargetPortNumber = _CpfrActiveProbeTargetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 7),
    _CpfrActiveProbeTargetPortNumber_Type()
)
cpfrActiveProbeTargetPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeTargetPortNumber.setStatus("current")
_CpfrActiveProbePfrMapIndex_Type = PfrMapIndexOrZero
_CpfrActiveProbePfrMapIndex_Object = MibTableColumn
cpfrActiveProbePfrMapIndex = _CpfrActiveProbePfrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 8),
    _CpfrActiveProbePfrMapIndex_Type()
)
cpfrActiveProbePfrMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbePfrMapIndex.setStatus("current")


class _CpfrActiveProbeDscpValue_Type(Unsigned32):
    """Custom type cpfrActiveProbeDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrActiveProbeDscpValue_Type.__name__ = "Unsigned32"
_CpfrActiveProbeDscpValue_Object = MibTableColumn
cpfrActiveProbeDscpValue = _CpfrActiveProbeDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 9),
    _CpfrActiveProbeDscpValue_Type()
)
cpfrActiveProbeDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeDscpValue.setStatus("current")


class _CpfrActiveProbeCodecName_Type(Integer32):
    """Custom type cpfrActiveProbeCodecName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 2),
          ("g729a", 3))
    )


_CpfrActiveProbeCodecName_Type.__name__ = "Integer32"
_CpfrActiveProbeCodecName_Object = MibTableColumn
cpfrActiveProbeCodecName = _CpfrActiveProbeCodecName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 10),
    _CpfrActiveProbeCodecName_Type()
)
cpfrActiveProbeCodecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeCodecName.setStatus("current")
_CpfrActiveProbeMapIndex_Type = PfrMapIndexOrZero
_CpfrActiveProbeMapIndex_Object = MibTableColumn
cpfrActiveProbeMapIndex = _CpfrActiveProbeMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 11),
    _CpfrActiveProbeMapIndex_Type()
)
cpfrActiveProbeMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeMapIndex.setStatus("current")
_CpfrActiveProbeMapPolicyIndex_Type = PfrMapIndexOrZero
_CpfrActiveProbeMapPolicyIndex_Object = MibTableColumn
cpfrActiveProbeMapPolicyIndex = _CpfrActiveProbeMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 12),
    _CpfrActiveProbeMapPolicyIndex_Type()
)
cpfrActiveProbeMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeMapPolicyIndex.setStatus("current")


class _CpfrActiveProbeAdminStatus_Type(Integer32):
    """Custom type cpfrActiveProbeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("forced", 3),
          ("unassigned", 2))
    )


_CpfrActiveProbeAdminStatus_Type.__name__ = "Integer32"
_CpfrActiveProbeAdminStatus_Object = MibTableColumn
cpfrActiveProbeAdminStatus = _CpfrActiveProbeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 13),
    _CpfrActiveProbeAdminStatus_Type()
)
cpfrActiveProbeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrActiveProbeAdminStatus.setStatus("current")


class _CpfrActiveProbeOperStatus_Type(Integer32):
    """Custom type cpfrActiveProbeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_CpfrActiveProbeOperStatus_Type.__name__ = "Integer32"
_CpfrActiveProbeOperStatus_Object = MibTableColumn
cpfrActiveProbeOperStatus = _CpfrActiveProbeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 14),
    _CpfrActiveProbeOperStatus_Type()
)
cpfrActiveProbeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrActiveProbeOperStatus.setStatus("current")
_CpfrActiveProbeAssignedPfxAddressType_Type = InetAddressType
_CpfrActiveProbeAssignedPfxAddressType_Object = MibTableColumn
cpfrActiveProbeAssignedPfxAddressType = _CpfrActiveProbeAssignedPfxAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 15),
    _CpfrActiveProbeAssignedPfxAddressType_Type()
)
cpfrActiveProbeAssignedPfxAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrActiveProbeAssignedPfxAddressType.setStatus("current")
_CpfrActiveProbeAssignedPfxAddress_Type = InetAddress
_CpfrActiveProbeAssignedPfxAddress_Object = MibTableColumn
cpfrActiveProbeAssignedPfxAddress = _CpfrActiveProbeAssignedPfxAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 16),
    _CpfrActiveProbeAssignedPfxAddress_Type()
)
cpfrActiveProbeAssignedPfxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrActiveProbeAssignedPfxAddress.setStatus("current")


class _CpfrActiveProbeAssignedPfxLen_Type(Unsigned32):
    """Custom type cpfrActiveProbeAssignedPfxLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrActiveProbeAssignedPfxLen_Type.__name__ = "Unsigned32"
_CpfrActiveProbeAssignedPfxLen_Object = MibTableColumn
cpfrActiveProbeAssignedPfxLen = _CpfrActiveProbeAssignedPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 17),
    _CpfrActiveProbeAssignedPfxLen_Type()
)
cpfrActiveProbeAssignedPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrActiveProbeAssignedPfxLen.setStatus("current")


class _CpfrActiveProbeMethod_Type(Integer32):
    """Custom type cpfrActiveProbeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("learned", 1))
    )


_CpfrActiveProbeMethod_Type.__name__ = "Integer32"
_CpfrActiveProbeMethod_Object = MibTableColumn
cpfrActiveProbeMethod = _CpfrActiveProbeMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 7, 1, 18),
    _CpfrActiveProbeMethod_Type()
)
cpfrActiveProbeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrActiveProbeMethod.setStatus("current")
_CpfrBRTable_Object = MibTable
cpfrBRTable = _CpfrBRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8)
)
if mibBuilder.loadTexts:
    cpfrBRTable.setStatus("current")
_CpfrBREntry_Object = MibTableRow
cpfrBREntry = _CpfrBREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1)
)
cpfrBREntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrBRIndex"),
)
if mibBuilder.loadTexts:
    cpfrBREntry.setStatus("current")
_CpfrBRIndex_Type = PfrBorderRouterIndex
_CpfrBRIndex_Object = MibTableColumn
cpfrBRIndex = _CpfrBRIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 1),
    _CpfrBRIndex_Type()
)
cpfrBRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrBRIndex.setStatus("current")


class _CpfrBRStorageType_Type(StorageType):
    """Custom type cpfrBRStorageType based on StorageType"""


_CpfrBRStorageType_Object = MibTableColumn
cpfrBRStorageType = _CpfrBRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 2),
    _CpfrBRStorageType_Type()
)
cpfrBRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBRStorageType.setStatus("current")
_CpfrBRRowStatus_Type = RowStatus
_CpfrBRRowStatus_Object = MibTableColumn
cpfrBRRowStatus = _CpfrBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 3),
    _CpfrBRRowStatus_Type()
)
cpfrBRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBRRowStatus.setStatus("current")
_CpfrBRAddressType_Type = InetAddressType
_CpfrBRAddressType_Object = MibTableColumn
cpfrBRAddressType = _CpfrBRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 4),
    _CpfrBRAddressType_Type()
)
cpfrBRAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBRAddressType.setStatus("current")
_CpfrBRAddress_Type = InetAddress
_CpfrBRAddress_Object = MibTableColumn
cpfrBRAddress = _CpfrBRAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 5),
    _CpfrBRAddress_Type()
)
cpfrBRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBRAddress.setStatus("current")
_CpfrBRKeyName_Type = SnmpAdminString
_CpfrBRKeyName_Object = MibTableColumn
cpfrBRKeyName = _CpfrBRKeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 6),
    _CpfrBRKeyName_Type()
)
cpfrBRKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBRKeyName.setStatus("current")


class _CpfrBROperStatus_Type(Integer32):
    """Custom type cpfrBROperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CpfrBROperStatus_Type.__name__ = "Integer32"
_CpfrBROperStatus_Object = MibTableColumn
cpfrBROperStatus = _CpfrBROperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 7),
    _CpfrBROperStatus_Type()
)
cpfrBROperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrBROperStatus.setStatus("current")


class _CpfrBRConnStatus_Type(Integer32):
    """Custom type cpfrBRConnStatus based on Integer32"""
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


_CpfrBRConnStatus_Type.__name__ = "Integer32"
_CpfrBRConnStatus_Object = MibTableColumn
cpfrBRConnStatus = _CpfrBRConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 8),
    _CpfrBRConnStatus_Type()
)
cpfrBRConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrBRConnStatus.setStatus("current")
_CpfrBRUpTime_Type = TimeTicks
_CpfrBRUpTime_Object = MibTableColumn
cpfrBRUpTime = _CpfrBRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 9),
    _CpfrBRUpTime_Type()
)
cpfrBRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrBRUpTime.setStatus("current")


class _CpfrBRConnFailureReason_Type(Integer32):
    """Custom type cpfrBRConnFailureReason based on Integer32"""
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
        *(("authFailure", 3),
          ("none", 2),
          ("socketError", 4),
          ("timerExpired", 5),
          ("versionMismatch", 1))
    )


_CpfrBRConnFailureReason_Type.__name__ = "Integer32"
_CpfrBRConnFailureReason_Object = MibTableColumn
cpfrBRConnFailureReason = _CpfrBRConnFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 10),
    _CpfrBRConnFailureReason_Type()
)
cpfrBRConnFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrBRConnFailureReason.setStatus("current")
_CpfrBRAuthFailCount_Type = Counter32
_CpfrBRAuthFailCount_Object = MibTableColumn
cpfrBRAuthFailCount = _CpfrBRAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 8, 1, 11),
    _CpfrBRAuthFailCount_Type()
)
cpfrBRAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrBRAuthFailCount.setStatus("current")
_CpfrExitTable_Object = MibTable
cpfrExitTable = _CpfrExitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9)
)
if mibBuilder.loadTexts:
    cpfrExitTable.setStatus("current")
_CpfrExitEntry_Object = MibTableRow
cpfrExitEntry = _CpfrExitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1)
)
cpfrExitEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrBRIndex"),
    (0, "CISCO-PFR-MIB", "cpfrExitIndex"),
)
if mibBuilder.loadTexts:
    cpfrExitEntry.setStatus("current")
_CpfrExitIndex_Type = PfrExitIndex
_CpfrExitIndex_Object = MibTableColumn
cpfrExitIndex = _CpfrExitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 1),
    _CpfrExitIndex_Type()
)
cpfrExitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrExitIndex.setStatus("current")


class _CpfrExitStorageType_Type(StorageType):
    """Custom type cpfrExitStorageType based on StorageType"""


_CpfrExitStorageType_Object = MibTableColumn
cpfrExitStorageType = _CpfrExitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 2),
    _CpfrExitStorageType_Type()
)
cpfrExitStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitStorageType.setStatus("current")
_CpfrExitRowStatus_Type = RowStatus
_CpfrExitRowStatus_Object = MibTableColumn
cpfrExitRowStatus = _CpfrExitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 3),
    _CpfrExitRowStatus_Type()
)
cpfrExitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitRowStatus.setStatus("current")
_CpfrExitName_Type = SnmpAdminString
_CpfrExitName_Object = MibTableColumn
cpfrExitName = _CpfrExitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 4),
    _CpfrExitName_Type()
)
cpfrExitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitName.setStatus("current")


class _CpfrExitType_Type(Integer32):
    """Custom type cpfrExitType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_CpfrExitType_Type.__name__ = "Integer32"
_CpfrExitType_Object = MibTableColumn
cpfrExitType = _CpfrExitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 5),
    _CpfrExitType_Type()
)
cpfrExitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitType.setStatus("current")


class _CpfrDowngradeBgpCommunity_Type(Unsigned32):
    """Custom type cpfrDowngradeBgpCommunity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrDowngradeBgpCommunity_Type.__name__ = "Unsigned32"
_CpfrDowngradeBgpCommunity_Object = MibTableColumn
cpfrDowngradeBgpCommunity = _CpfrDowngradeBgpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 6),
    _CpfrDowngradeBgpCommunity_Type()
)
cpfrDowngradeBgpCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrDowngradeBgpCommunity.setStatus("current")


class _CpfrExitMaxUtilRxType_Type(PfrMetricPolicyType):
    """Custom type cpfrExitMaxUtilRxType based on PfrMetricPolicyType"""


_CpfrExitMaxUtilRxType_Object = MibTableColumn
cpfrExitMaxUtilRxType = _CpfrExitMaxUtilRxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 7),
    _CpfrExitMaxUtilRxType_Type()
)
cpfrExitMaxUtilRxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilRxType.setStatus("current")


class _CpfrExitMaxUtilRxAbsolute_Type(Unsigned32):
    """Custom type cpfrExitMaxUtilRxAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitMaxUtilRxAbsolute_Type.__name__ = "Unsigned32"
_CpfrExitMaxUtilRxAbsolute_Object = MibTableColumn
cpfrExitMaxUtilRxAbsolute = _CpfrExitMaxUtilRxAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 8),
    _CpfrExitMaxUtilRxAbsolute_Type()
)
cpfrExitMaxUtilRxAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilRxAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilRxAbsolute.setUnits("Kbps")


class _CpfrExitMaxUtilRxPercentage_Type(Unsigned32):
    """Custom type cpfrExitMaxUtilRxPercentage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpfrExitMaxUtilRxPercentage_Type.__name__ = "Unsigned32"
_CpfrExitMaxUtilRxPercentage_Object = MibTableColumn
cpfrExitMaxUtilRxPercentage = _CpfrExitMaxUtilRxPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 9),
    _CpfrExitMaxUtilRxPercentage_Type()
)
cpfrExitMaxUtilRxPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilRxPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilRxPercentage.setUnits("percent")


class _CpfrExitMaxUtilTxType_Type(PfrMetricPolicyType):
    """Custom type cpfrExitMaxUtilTxType based on PfrMetricPolicyType"""


_CpfrExitMaxUtilTxType_Object = MibTableColumn
cpfrExitMaxUtilTxType = _CpfrExitMaxUtilTxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 10),
    _CpfrExitMaxUtilTxType_Type()
)
cpfrExitMaxUtilTxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilTxType.setStatus("current")


class _CpfrExitMaxUtilTxAbsolute_Type(Unsigned32):
    """Custom type cpfrExitMaxUtilTxAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitMaxUtilTxAbsolute_Type.__name__ = "Unsigned32"
_CpfrExitMaxUtilTxAbsolute_Object = MibTableColumn
cpfrExitMaxUtilTxAbsolute = _CpfrExitMaxUtilTxAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 11),
    _CpfrExitMaxUtilTxAbsolute_Type()
)
cpfrExitMaxUtilTxAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilTxAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilTxAbsolute.setUnits("Kbps")


class _CpfrExitMaxUtilTxPercentage_Type(Unsigned32):
    """Custom type cpfrExitMaxUtilTxPercentage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpfrExitMaxUtilTxPercentage_Type.__name__ = "Unsigned32"
_CpfrExitMaxUtilTxPercentage_Object = MibTableColumn
cpfrExitMaxUtilTxPercentage = _CpfrExitMaxUtilTxPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 12),
    _CpfrExitMaxUtilTxPercentage_Type()
)
cpfrExitMaxUtilTxPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilTxPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitMaxUtilTxPercentage.setUnits("percent")


class _CpfrExitCostCalcMethod_Type(Integer32):
    """Custom type cpfrExitCostCalcMethod based on Integer32"""
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
        *(("combined", 1),
          ("separate", 2),
          ("sum", 3))
    )


_CpfrExitCostCalcMethod_Type.__name__ = "Integer32"
_CpfrExitCostCalcMethod_Object = MibTableColumn
cpfrExitCostCalcMethod = _CpfrExitCostCalcMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 13),
    _CpfrExitCostCalcMethod_Type()
)
cpfrExitCostCalcMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostCalcMethod.setStatus("current")


class _CpfrExitCostDiscard_Type(Integer32):
    """Custom type cpfrExitCostDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("monthly", 2))
    )


_CpfrExitCostDiscard_Type.__name__ = "Integer32"
_CpfrExitCostDiscard_Object = MibTableColumn
cpfrExitCostDiscard = _CpfrExitCostDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 14),
    _CpfrExitCostDiscard_Type()
)
cpfrExitCostDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostDiscard.setStatus("current")


class _CpfrExitCostDiscardType_Type(Integer32):
    """Custom type cpfrExitCostDiscardType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percent", 2))
    )


_CpfrExitCostDiscardType_Type.__name__ = "Integer32"
_CpfrExitCostDiscardType_Object = MibTableColumn
cpfrExitCostDiscardType = _CpfrExitCostDiscardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 15),
    _CpfrExitCostDiscardType_Type()
)
cpfrExitCostDiscardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostDiscardType.setStatus("current")


class _CpfrExitCostDiscardAbsolute_Type(Unsigned32):
    """Custom type cpfrExitCostDiscardAbsolute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostDiscardAbsolute_Type.__name__ = "Unsigned32"
_CpfrExitCostDiscardAbsolute_Object = MibTableColumn
cpfrExitCostDiscardAbsolute = _CpfrExitCostDiscardAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 16),
    _CpfrExitCostDiscardAbsolute_Type()
)
cpfrExitCostDiscardAbsolute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostDiscardAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostDiscardAbsolute.setUnits("samples")


class _CpfrExitCostDiscardPercent_Type(Unsigned32):
    """Custom type cpfrExitCostDiscardPercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CpfrExitCostDiscardPercent_Type.__name__ = "Unsigned32"
_CpfrExitCostDiscardPercent_Object = MibTableColumn
cpfrExitCostDiscardPercent = _CpfrExitCostDiscardPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 17),
    _CpfrExitCostDiscardPercent_Type()
)
cpfrExitCostDiscardPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostDiscardPercent.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostDiscardPercent.setUnits("percent")


class _CpfrExitCostEndDayOfMonth_Type(Unsigned32):
    """Custom type cpfrExitCostEndDayOfMonth based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CpfrExitCostEndDayOfMonth_Type.__name__ = "Unsigned32"
_CpfrExitCostEndDayOfMonth_Object = MibTableColumn
cpfrExitCostEndDayOfMonth = _CpfrExitCostEndDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 18),
    _CpfrExitCostEndDayOfMonth_Type()
)
cpfrExitCostEndDayOfMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostEndDayOfMonth.setStatus("current")


class _CpfrExitCostEndOffsetType_Type(Integer32):
    """Custom type cpfrExitCostEndOffsetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_CpfrExitCostEndOffsetType_Type.__name__ = "Integer32"
_CpfrExitCostEndOffsetType_Object = MibTableColumn
cpfrExitCostEndOffsetType = _CpfrExitCostEndOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 19),
    _CpfrExitCostEndOffsetType_Type()
)
cpfrExitCostEndOffsetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostEndOffsetType.setStatus("current")
_CpfrExitCostEndOffset_Type = TimeInterval
_CpfrExitCostEndOffset_Object = MibTableColumn
cpfrExitCostEndOffset = _CpfrExitCostEndOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 20),
    _CpfrExitCostEndOffset_Type()
)
cpfrExitCostEndOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostEndOffset.setStatus("current")


class _CpfrExitCostFixedFeeCost_Type(Unsigned32):
    """Custom type cpfrExitCostFixedFeeCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostFixedFeeCost_Type.__name__ = "Unsigned32"
_CpfrExitCostFixedFeeCost_Object = MibTableColumn
cpfrExitCostFixedFeeCost = _CpfrExitCostFixedFeeCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 21),
    _CpfrExitCostFixedFeeCost_Type()
)
cpfrExitCostFixedFeeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostFixedFeeCost.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostFixedFeeCost.setUnits("dollars")
_CpfrExitCostNickName_Type = SnmpAdminString
_CpfrExitCostNickName_Object = MibTableColumn
cpfrExitCostNickName = _CpfrExitCostNickName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 22),
    _CpfrExitCostNickName_Type()
)
cpfrExitCostNickName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostNickName.setStatus("current")


class _CpfrExitCostSamplingPeriod_Type(Unsigned32):
    """Custom type cpfrExitCostSamplingPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostSamplingPeriod_Type.__name__ = "Unsigned32"
_CpfrExitCostSamplingPeriod_Object = MibTableColumn
cpfrExitCostSamplingPeriod = _CpfrExitCostSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 23),
    _CpfrExitCostSamplingPeriod_Type()
)
cpfrExitCostSamplingPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostSamplingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostSamplingPeriod.setUnits("minutes")


class _CpfrExitCostRollupPeriod_Type(Unsigned32):
    """Custom type cpfrExitCostRollupPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostRollupPeriod_Type.__name__ = "Unsigned32"
_CpfrExitCostRollupPeriod_Object = MibTableColumn
cpfrExitCostRollupPeriod = _CpfrExitCostRollupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 24),
    _CpfrExitCostRollupPeriod_Type()
)
cpfrExitCostRollupPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostRollupPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostRollupPeriod.setUnits("minutes")
_CpfrExitCostSummerTimeStart_Type = DateAndTime
_CpfrExitCostSummerTimeStart_Object = MibTableColumn
cpfrExitCostSummerTimeStart = _CpfrExitCostSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 25),
    _CpfrExitCostSummerTimeStart_Type()
)
cpfrExitCostSummerTimeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostSummerTimeStart.setStatus("current")


class _CpfrExitCostSummerTimeOffset_Type(Unsigned32):
    """Custom type cpfrExitCostSummerTimeOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CpfrExitCostSummerTimeOffset_Type.__name__ = "Unsigned32"
_CpfrExitCostSummerTimeOffset_Object = MibTableColumn
cpfrExitCostSummerTimeOffset = _CpfrExitCostSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 26),
    _CpfrExitCostSummerTimeOffset_Type()
)
cpfrExitCostSummerTimeOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostSummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCostSummerTimeOffset.setUnits("minutes")
_CpfrExitCostSummerTimeEnd_Type = DateAndTime
_CpfrExitCostSummerTimeEnd_Object = MibTableColumn
cpfrExitCostSummerTimeEnd = _CpfrExitCostSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 27),
    _CpfrExitCostSummerTimeEnd_Type()
)
cpfrExitCostSummerTimeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostSummerTimeEnd.setStatus("current")
_CpfrExitCapacity_Type = CounterBasedGauge64
_CpfrExitCapacity_Object = MibTableColumn
cpfrExitCapacity = _CpfrExitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 28),
    _CpfrExitCapacity_Type()
)
cpfrExitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitCapacity.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCapacity.setUnits("Kbps")
_CpfrExitRxBandwidth_Type = CounterBasedGauge64
_CpfrExitRxBandwidth_Object = MibTableColumn
cpfrExitRxBandwidth = _CpfrExitRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 29),
    _CpfrExitRxBandwidth_Type()
)
cpfrExitRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRxBandwidth.setUnits("Kbps")
_CpfrExitTxBandwidth_Type = CounterBasedGauge64
_CpfrExitTxBandwidth_Object = MibTableColumn
cpfrExitTxBandwidth = _CpfrExitTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 30),
    _CpfrExitTxBandwidth_Type()
)
cpfrExitTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitTxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitTxBandwidth.setUnits("Kbps")


class _CpfrExitTxLoad_Type(Gauge32):
    """Custom type cpfrExitTxLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitTxLoad_Type.__name__ = "Gauge32"
_CpfrExitTxLoad_Object = MibTableColumn
cpfrExitTxLoad = _CpfrExitTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 31),
    _CpfrExitTxLoad_Type()
)
cpfrExitTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitTxLoad.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitTxLoad.setUnits("percent")


class _CpfrExitRxLoad_Type(Gauge32):
    """Custom type cpfrExitRxLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRxLoad_Type.__name__ = "Gauge32"
_CpfrExitRxLoad_Object = MibTableColumn
cpfrExitRxLoad = _CpfrExitRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 32),
    _CpfrExitRxLoad_Type()
)
cpfrExitRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRxLoad.setStatus("current")
_CpfrExitNickName_Type = SnmpAdminString
_CpfrExitNickName_Object = MibTableColumn
cpfrExitNickName = _CpfrExitNickName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 33),
    _CpfrExitNickName_Type()
)
cpfrExitNickName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitNickName.setStatus("current")


class _CpfrExitCost1_Type(Gauge32):
    """Custom type cpfrExitCost1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCost1_Type.__name__ = "Gauge32"
_CpfrExitCost1_Object = MibTableColumn
cpfrExitCost1 = _CpfrExitCost1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 34),
    _CpfrExitCost1_Type()
)
cpfrExitCost1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitCost1.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCost1.setUnits("dollars")


class _CpfrExitSustainedUtil1_Type(Gauge32):
    """Custom type cpfrExitSustainedUtil1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitSustainedUtil1_Type.__name__ = "Gauge32"
_CpfrExitSustainedUtil1_Object = MibTableColumn
cpfrExitSustainedUtil1 = _CpfrExitSustainedUtil1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 35),
    _CpfrExitSustainedUtil1_Type()
)
cpfrExitSustainedUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil1.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil1.setUnits("Kbps")


class _CpfrExitCost2_Type(Gauge32):
    """Custom type cpfrExitCost2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCost2_Type.__name__ = "Gauge32"
_CpfrExitCost2_Object = MibTableColumn
cpfrExitCost2 = _CpfrExitCost2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 36),
    _CpfrExitCost2_Type()
)
cpfrExitCost2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitCost2.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCost2.setUnits("dollars")


class _CpfrExitSustainedUtil2_Type(Gauge32):
    """Custom type cpfrExitSustainedUtil2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitSustainedUtil2_Type.__name__ = "Gauge32"
_CpfrExitSustainedUtil2_Object = MibTableColumn
cpfrExitSustainedUtil2 = _CpfrExitSustainedUtil2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 37),
    _CpfrExitSustainedUtil2_Type()
)
cpfrExitSustainedUtil2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil2.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil2.setUnits("Kbps")


class _CpfrExitCost3_Type(Gauge32):
    """Custom type cpfrExitCost3 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCost3_Type.__name__ = "Gauge32"
_CpfrExitCost3_Object = MibTableColumn
cpfrExitCost3 = _CpfrExitCost3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 38),
    _CpfrExitCost3_Type()
)
cpfrExitCost3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitCost3.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitCost3.setUnits("dollars")


class _CpfrExitSustainedUtil3_Type(Gauge32):
    """Custom type cpfrExitSustainedUtil3 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitSustainedUtil3_Type.__name__ = "Gauge32"
_CpfrExitSustainedUtil3_Object = MibTableColumn
cpfrExitSustainedUtil3 = _CpfrExitSustainedUtil3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 39),
    _CpfrExitSustainedUtil3_Type()
)
cpfrExitSustainedUtil3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil3.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitSustainedUtil3.setUnits("Kbps")


class _CpfrExitRollupTotal_Type(Gauge32):
    """Custom type cpfrExitRollupTotal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupTotal_Type.__name__ = "Gauge32"
_CpfrExitRollupTotal_Object = MibTableColumn
cpfrExitRollupTotal = _CpfrExitRollupTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 40),
    _CpfrExitRollupTotal_Type()
)
cpfrExitRollupTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupTotal.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRollupTotal.setUnits("minutes")


class _CpfrExitRollupDiscard_Type(Gauge32):
    """Custom type cpfrExitRollupDiscard based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupDiscard_Type.__name__ = "Gauge32"
_CpfrExitRollupDiscard_Object = MibTableColumn
cpfrExitRollupDiscard = _CpfrExitRollupDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 41),
    _CpfrExitRollupDiscard_Type()
)
cpfrExitRollupDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupDiscard.setStatus("current")


class _CpfrExitRollupLeft_Type(Gauge32):
    """Custom type cpfrExitRollupLeft based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupLeft_Type.__name__ = "Gauge32"
_CpfrExitRollupLeft_Object = MibTableColumn
cpfrExitRollupLeft = _CpfrExitRollupLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 42),
    _CpfrExitRollupLeft_Type()
)
cpfrExitRollupLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupLeft.setStatus("current")


class _CpfrExitRollupCollected_Type(Gauge32):
    """Custom type cpfrExitRollupCollected based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupCollected_Type.__name__ = "Gauge32"
_CpfrExitRollupCollected_Object = MibTableColumn
cpfrExitRollupCollected = _CpfrExitRollupCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 43),
    _CpfrExitRollupCollected_Type()
)
cpfrExitRollupCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupCollected.setStatus("current")


class _CpfrExitRollupMomTgtUtil_Type(Gauge32):
    """Custom type cpfrExitRollupMomTgtUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupMomTgtUtil_Type.__name__ = "Gauge32"
_CpfrExitRollupMomTgtUtil_Object = MibTableColumn
cpfrExitRollupMomTgtUtil = _CpfrExitRollupMomTgtUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 44),
    _CpfrExitRollupMomTgtUtil_Type()
)
cpfrExitRollupMomTgtUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupMomTgtUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRollupMomTgtUtil.setUnits("Kbps")


class _CpfrExitRollupStartingTgtUtil_Type(Gauge32):
    """Custom type cpfrExitRollupStartingTgtUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupStartingTgtUtil_Type.__name__ = "Gauge32"
_CpfrExitRollupStartingTgtUtil_Object = MibTableColumn
cpfrExitRollupStartingTgtUtil = _CpfrExitRollupStartingTgtUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 45),
    _CpfrExitRollupStartingTgtUtil_Type()
)
cpfrExitRollupStartingTgtUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupStartingTgtUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRollupStartingTgtUtil.setUnits("Kbps")


class _CpfrExitRollupCurrentTgtUtil_Type(Gauge32):
    """Custom type cpfrExitRollupCurrentTgtUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitRollupCurrentTgtUtil_Type.__name__ = "Gauge32"
_CpfrExitRollupCurrentTgtUtil_Object = MibTableColumn
cpfrExitRollupCurrentTgtUtil = _CpfrExitRollupCurrentTgtUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 46),
    _CpfrExitRollupCurrentTgtUtil_Type()
)
cpfrExitRollupCurrentTgtUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupCurrentTgtUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRollupCurrentTgtUtil.setUnits("kbps")
_CpfrExitRollupCumRxBytes_Type = Counter32
_CpfrExitRollupCumRxBytes_Object = MibTableColumn
cpfrExitRollupCumRxBytes = _CpfrExitRollupCumRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 47),
    _CpfrExitRollupCumRxBytes_Type()
)
cpfrExitRollupCumRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupCumRxBytes.setStatus("current")
_CpfrExitRollupCumTxBytes_Type = Counter32
_CpfrExitRollupCumTxBytes_Object = MibTableColumn
cpfrExitRollupCumTxBytes = _CpfrExitRollupCumTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 48),
    _CpfrExitRollupCumTxBytes_Type()
)
cpfrExitRollupCumTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupCumTxBytes.setStatus("current")
_CpfrExitRollupTimeRemain_Type = TimeInterval
_CpfrExitRollupTimeRemain_Object = MibTableColumn
cpfrExitRollupTimeRemain = _CpfrExitRollupTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 49),
    _CpfrExitRollupTimeRemain_Type()
)
cpfrExitRollupTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRollupTimeRemain.setStatus("current")


class _CpfrExitOperStatus_Type(Integer32):
    """Custom type cpfrExitOperStatus based on Integer32"""
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


_CpfrExitOperStatus_Type.__name__ = "Integer32"
_CpfrExitOperStatus_Object = MibTableColumn
cpfrExitOperStatus = _CpfrExitOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 50),
    _CpfrExitOperStatus_Type()
)
cpfrExitOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitOperStatus.setStatus("current")
_CpfrExitRsvpBandwidthPool_Type = CounterBasedGauge64
_CpfrExitRsvpBandwidthPool_Object = MibTableColumn
cpfrExitRsvpBandwidthPool = _CpfrExitRsvpBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 9, 1, 51),
    _CpfrExitRsvpBandwidthPool_Type()
)
cpfrExitRsvpBandwidthPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrExitRsvpBandwidthPool.setStatus("current")
if mibBuilder.loadTexts:
    cpfrExitRsvpBandwidthPool.setUnits("bytes")
_CpfrExitCostTierTable_Object = MibTable
cpfrExitCostTierTable = _CpfrExitCostTierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10)
)
if mibBuilder.loadTexts:
    cpfrExitCostTierTable.setStatus("current")
_CpfrExitCostTierEntry_Object = MibTableRow
cpfrExitCostTierEntry = _CpfrExitCostTierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10, 1)
)
cpfrExitCostTierEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrBRIndex"),
    (0, "CISCO-PFR-MIB", "cpfrExitIndex"),
    (0, "CISCO-PFR-MIB", "cpfrExitCostTierIndex"),
)
if mibBuilder.loadTexts:
    cpfrExitCostTierEntry.setStatus("current")


class _CpfrExitCostTierIndex_Type(Unsigned32):
    """Custom type cpfrExitCostTierIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostTierIndex_Type.__name__ = "Unsigned32"
_CpfrExitCostTierIndex_Object = MibTableColumn
cpfrExitCostTierIndex = _CpfrExitCostTierIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10, 1, 1),
    _CpfrExitCostTierIndex_Type()
)
cpfrExitCostTierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrExitCostTierIndex.setStatus("current")


class _CpfrExitCostTierStorageType_Type(StorageType):
    """Custom type cpfrExitCostTierStorageType based on StorageType"""


_CpfrExitCostTierStorageType_Object = MibTableColumn
cpfrExitCostTierStorageType = _CpfrExitCostTierStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10, 1, 2),
    _CpfrExitCostTierStorageType_Type()
)
cpfrExitCostTierStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostTierStorageType.setStatus("current")
_CpfrExitCostTierRowStatus_Type = RowStatus
_CpfrExitCostTierRowStatus_Object = MibTableColumn
cpfrExitCostTierRowStatus = _CpfrExitCostTierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10, 1, 3),
    _CpfrExitCostTierRowStatus_Type()
)
cpfrExitCostTierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostTierRowStatus.setStatus("current")


class _CpfrExitCostTierFee_Type(Unsigned32):
    """Custom type cpfrExitCostTierFee based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrExitCostTierFee_Type.__name__ = "Unsigned32"
_CpfrExitCostTierFee_Object = MibTableColumn
cpfrExitCostTierFee = _CpfrExitCostTierFee_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 10, 1, 4),
    _CpfrExitCostTierFee_Type()
)
cpfrExitCostTierFee.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrExitCostTierFee.setStatus("current")
_CpfrTrafficClassTable_Object = MibTable
cpfrTrafficClassTable = _CpfrTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11)
)
if mibBuilder.loadTexts:
    cpfrTrafficClassTable.setStatus("current")
_CpfrTrafficClassEntry_Object = MibTableRow
cpfrTrafficClassEntry = _CpfrTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1)
)
cpfrTrafficClassEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    cpfrTrafficClassEntry.setStatus("current")


class _CpfrTrafficClassIndex_Type(Unsigned32):
    """Custom type cpfrTrafficClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpfrTrafficClassIndex_Type.__name__ = "Unsigned32"
_CpfrTrafficClassIndex_Object = MibTableColumn
cpfrTrafficClassIndex = _CpfrTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 1),
    _CpfrTrafficClassIndex_Type()
)
cpfrTrafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrTrafficClassIndex.setStatus("current")


class _CpfrTCBRIndex_Type(PfrBorderRouterIndex):
    """Custom type cpfrTCBRIndex based on PfrBorderRouterIndex"""
    subtypeSpec = PfrBorderRouterIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpfrTCBRIndex_Type.__name__ = "PfrBorderRouterIndex"
_CpfrTCBRIndex_Object = MibTableColumn
cpfrTCBRIndex = _CpfrTCBRIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 2),
    _CpfrTCBRIndex_Type()
)
cpfrTCBRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCBRIndex.setStatus("current")
_CpfrTCBRExitIndex_Type = PfrExitIndex
_CpfrTCBRExitIndex_Object = MibTableColumn
cpfrTCBRExitIndex = _CpfrTCBRExitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 3),
    _CpfrTCBRExitIndex_Type()
)
cpfrTCBRExitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCBRExitIndex.setStatus("current")
_CpfrTCMapIndex_Type = PfrMapIndexOrZero
_CpfrTCMapIndex_Object = MibTableColumn
cpfrTCMapIndex = _CpfrTCMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 4),
    _CpfrTCMapIndex_Type()
)
cpfrTCMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMapIndex.setStatus("current")
_CpfrTCMapPolicyIndex_Type = PfrMapPolicyIndex
_CpfrTCMapPolicyIndex_Object = MibTableColumn
cpfrTCMapPolicyIndex = _CpfrTCMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 5),
    _CpfrTCMapPolicyIndex_Type()
)
cpfrTCMapPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMapPolicyIndex.setStatus("current")


class _CpfrTrafficClassValid_Type(Bits):
    """Custom type cpfrTrafficClassValid based on Bits"""
    namedValues = NamedValues(
        *(("destination", 1),
          ("destinationPort", 3),
          ("dscp", 4),
          ("nbar", 6),
          ("protocol", 5),
          ("source", 0),
          ("sourcePort", 2))
    )

_CpfrTrafficClassValid_Type.__name__ = "Bits"
_CpfrTrafficClassValid_Object = MibTableColumn
cpfrTrafficClassValid = _CpfrTrafficClassValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 6),
    _CpfrTrafficClassValid_Type()
)
cpfrTrafficClassValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTrafficClassValid.setStatus("current")
_CpfrTCSrcPrefixType_Type = InetAddressType
_CpfrTCSrcPrefixType_Object = MibTableColumn
cpfrTCSrcPrefixType = _CpfrTCSrcPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 7),
    _CpfrTCSrcPrefixType_Type()
)
cpfrTCSrcPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSrcPrefixType.setStatus("current")
_CpfrTCSrcPrefix_Type = InetAddress
_CpfrTCSrcPrefix_Object = MibTableColumn
cpfrTCSrcPrefix = _CpfrTCSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 8),
    _CpfrTCSrcPrefix_Type()
)
cpfrTCSrcPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSrcPrefix.setStatus("current")


class _CpfrTCSrcPrefixLen_Type(Gauge32):
    """Custom type cpfrTCSrcPrefixLen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCSrcPrefixLen_Type.__name__ = "Gauge32"
_CpfrTCSrcPrefixLen_Object = MibTableColumn
cpfrTCSrcPrefixLen = _CpfrTCSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 9),
    _CpfrTCSrcPrefixLen_Type()
)
cpfrTCSrcPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSrcPrefixLen.setStatus("current")
_CpfrTCSrcMinPort_Type = CiscoPort
_CpfrTCSrcMinPort_Object = MibTableColumn
cpfrTCSrcMinPort = _CpfrTCSrcMinPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 10),
    _CpfrTCSrcMinPort_Type()
)
cpfrTCSrcMinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSrcMinPort.setStatus("current")
_CpfrTCSrcMaxPort_Type = CiscoPort
_CpfrTCSrcMaxPort_Object = MibTableColumn
cpfrTCSrcMaxPort = _CpfrTCSrcMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 11),
    _CpfrTCSrcMaxPort_Type()
)
cpfrTCSrcMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSrcMaxPort.setStatus("current")
_CpfrTCDstPrefixType_Type = InetAddressType
_CpfrTCDstPrefixType_Object = MibTableColumn
cpfrTCDstPrefixType = _CpfrTCDstPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 12),
    _CpfrTCDstPrefixType_Type()
)
cpfrTCDstPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDstPrefixType.setStatus("current")
_CpfrTCDstPrefix_Type = InetAddress
_CpfrTCDstPrefix_Object = MibTableColumn
cpfrTCDstPrefix = _CpfrTCDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 13),
    _CpfrTCDstPrefix_Type()
)
cpfrTCDstPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDstPrefix.setStatus("current")


class _CpfrTCDstPrefixLen_Type(Gauge32):
    """Custom type cpfrTCDstPrefixLen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCDstPrefixLen_Type.__name__ = "Gauge32"
_CpfrTCDstPrefixLen_Object = MibTableColumn
cpfrTCDstPrefixLen = _CpfrTCDstPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 14),
    _CpfrTCDstPrefixLen_Type()
)
cpfrTCDstPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDstPrefixLen.setStatus("current")
_CpfrTCDstMinPort_Type = CiscoPort
_CpfrTCDstMinPort_Object = MibTableColumn
cpfrTCDstMinPort = _CpfrTCDstMinPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 15),
    _CpfrTCDstMinPort_Type()
)
cpfrTCDstMinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDstMinPort.setStatus("current")
_CpfrTCDstMaxPort_Type = CiscoPort
_CpfrTCDstMaxPort_Object = MibTableColumn
cpfrTCDstMaxPort = _CpfrTCDstMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 16),
    _CpfrTCDstMaxPort_Type()
)
cpfrTCDstMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDstMaxPort.setStatus("current")


class _CpfrTCDscpValue_Type(DscpOrAny):
    """Custom type cpfrTCDscpValue based on DscpOrAny"""
    subtypeSpec = DscpOrAny.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_CpfrTCDscpValue_Type.__name__ = "DscpOrAny"
_CpfrTCDscpValue_Object = MibTableColumn
cpfrTCDscpValue = _CpfrTCDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 17),
    _CpfrTCDscpValue_Type()
)
cpfrTCDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCDscpValue.setStatus("current")


class _CpfrTCProtocol_Type(Integer32):
    """Custom type cpfrTCProtocol based on Integer32"""
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
        *(("bgp", 4),
          ("cce", 6),
          ("eigrp", 2),
          ("pbr", 5),
          ("ribpbr", 3),
          ("static", 1),
          ("unknown", 7))
    )


_CpfrTCProtocol_Type.__name__ = "Integer32"
_CpfrTCProtocol_Object = MibTableColumn
cpfrTCProtocol = _CpfrTCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 18),
    _CpfrTCProtocol_Type()
)
cpfrTCProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCProtocol.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCProtocol.setUnits("bgp")
_CpfrTCNbarApplication_Type = CiscoPdProtocolIndex
_CpfrTCNbarApplication_Object = MibTableColumn
cpfrTCNbarApplication = _CpfrTCNbarApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 11, 1, 19),
    _CpfrTCNbarApplication_Type()
)
cpfrTCNbarApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCNbarApplication.setStatus("current")
_CpfrTrafficClassStatusTable_Object = MibTable
cpfrTrafficClassStatusTable = _CpfrTrafficClassStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12)
)
if mibBuilder.loadTexts:
    cpfrTrafficClassStatusTable.setStatus("current")
_CpfrTrafficClassStatusEntry_Object = MibTableRow
cpfrTrafficClassStatusEntry = _CpfrTrafficClassStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1)
)
cpfrTrafficClassStatusEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    cpfrTrafficClassStatusEntry.setStatus("current")


class _CpfrTCStatus_Type(Integer32):
    """Custom type cpfrTCStatus based on Integer32"""
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
        *(("choose", 2),
          ("default", 1),
          ("holddown", 3),
          ("inpolicy", 4),
          ("oopolicy", 5))
    )


_CpfrTCStatus_Type.__name__ = "Integer32"
_CpfrTCStatus_Object = MibTableColumn
cpfrTCStatus = _CpfrTCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 1),
    _CpfrTCStatus_Type()
)
cpfrTCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCStatus.setStatus("current")


class _CpfrTCSType_Type(Integer32):
    """Custom type cpfrTCSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("learned", 1))
    )


_CpfrTCSType_Type.__name__ = "Integer32"
_CpfrTCSType_Object = MibTableColumn
cpfrTCSType = _CpfrTCSType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 2),
    _CpfrTCSType_Type()
)
cpfrTCSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSType.setStatus("current")
_CpfrTCSLearnListIndex_Type = PfrLearnListIndexOrZero
_CpfrTCSLearnListIndex_Object = MibTableColumn
cpfrTCSLearnListIndex = _CpfrTCSLearnListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 3),
    _CpfrTCSLearnListIndex_Type()
)
cpfrTCSLearnListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSLearnListIndex.setStatus("current")


class _CpfrTCSTimeOnCurrExit_Type(Gauge32):
    """Custom type cpfrTCSTimeOnCurrExit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCSTimeOnCurrExit_Type.__name__ = "Gauge32"
_CpfrTCSTimeOnCurrExit_Object = MibTableColumn
cpfrTCSTimeOnCurrExit = _CpfrTCSTimeOnCurrExit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 4),
    _CpfrTCSTimeOnCurrExit_Type()
)
cpfrTCSTimeOnCurrExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSTimeOnCurrExit.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCSTimeOnCurrExit.setUnits("seconds")


class _CpfrTCSControlState_Type(Integer32):
    """Custom type cpfrTCSControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 1),
          ("uncontrolled", 2))
    )


_CpfrTCSControlState_Type.__name__ = "Integer32"
_CpfrTCSControlState_Object = MibTableColumn
cpfrTCSControlState = _CpfrTCSControlState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 5),
    _CpfrTCSControlState_Type()
)
cpfrTCSControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSControlState.setStatus("current")


class _CpfrTCSControlBy_Type(Integer32):
    """Custom type cpfrTCSControlBy based on Integer32"""
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
        *(("bgp", 4),
          ("cce", 6),
          ("eigrp", 2),
          ("pbr", 5),
          ("ribpbr", 3),
          ("static", 1),
          ("unknown", 7))
    )


_CpfrTCSControlBy_Type.__name__ = "Integer32"
_CpfrTCSControlBy_Object = MibTableColumn
cpfrTCSControlBy = _CpfrTCSControlBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 6),
    _CpfrTCSControlBy_Type()
)
cpfrTCSControlBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSControlBy.setStatus("current")


class _CpfrTCSTimeRemainCurrState_Type(Gauge32):
    """Custom type cpfrTCSTimeRemainCurrState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCSTimeRemainCurrState_Type.__name__ = "Gauge32"
_CpfrTCSTimeRemainCurrState_Object = MibTableColumn
cpfrTCSTimeRemainCurrState = _CpfrTCSTimeRemainCurrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 7),
    _CpfrTCSTimeRemainCurrState_Type()
)
cpfrTCSTimeRemainCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSTimeRemainCurrState.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCSTimeRemainCurrState.setUnits("seconds")
_CpfrTCSLastOOPEventTime_Type = TimeStamp
_CpfrTCSLastOOPEventTime_Object = MibTableColumn
cpfrTCSLastOOPEventTime = _CpfrTCSLastOOPEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 8),
    _CpfrTCSLastOOPEventTime_Type()
)
cpfrTCSLastOOPEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSLastOOPEventTime.setStatus("current")


class _CpfrTCSLastOOPReason_Type(Integer32):
    """Custom type cpfrTCSLastOOPReason based on Integer32"""
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
        *(("delayOOPActiveMode", 4),
          ("delayOOPPassiveMode", 1),
          ("jitterOOPActiveMode", 7),
          ("lossOOPActiveMode", 5),
          ("lossOOPPassiveMode", 2),
          ("mosOOPActiveMode", 8),
          ("none", 9),
          ("rsvpOOPRecomputeExclude", 10),
          ("unreachableOOPActiveMode", 6),
          ("unreachableOOPPassiveMode", 3))
    )


_CpfrTCSLastOOPReason_Type.__name__ = "Integer32"
_CpfrTCSLastOOPReason_Object = MibTableColumn
cpfrTCSLastOOPReason = _CpfrTCSLastOOPReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 9),
    _CpfrTCSLastOOPReason_Type()
)
cpfrTCSLastOOPReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSLastOOPReason.setStatus("current")
_CpfrTCSLastRouteChangeEvent_Type = TimeStamp
_CpfrTCSLastRouteChangeEvent_Object = MibTableColumn
cpfrTCSLastRouteChangeEvent = _CpfrTCSLastRouteChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 10),
    _CpfrTCSLastRouteChangeEvent_Type()
)
cpfrTCSLastRouteChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSLastRouteChangeEvent.setStatus("current")
_CpfrTCSLastRouteChangeReason_Type = PfrLastUncontrolReason
_CpfrTCSLastRouteChangeReason_Object = MibTableColumn
cpfrTCSLastRouteChangeReason = _CpfrTCSLastRouteChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 12, 1, 11),
    _CpfrTCSLastRouteChangeReason_Type()
)
cpfrTCSLastRouteChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCSLastRouteChangeReason.setStatus("current")
_CpfrTrafficClassMetricTable_Object = MibTable
cpfrTrafficClassMetricTable = _CpfrTrafficClassMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13)
)
if mibBuilder.loadTexts:
    cpfrTrafficClassMetricTable.setStatus("current")
_CpfrTrafficClassMetricEntry_Object = MibTableRow
cpfrTrafficClassMetricEntry = _CpfrTrafficClassMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1)
)
cpfrTrafficClassMetricEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    cpfrTrafficClassMetricEntry.setStatus("current")
_CpfrTCMLastUpdateTime_Type = TimeStamp
_CpfrTCMLastUpdateTime_Object = MibTableColumn
cpfrTCMLastUpdateTime = _CpfrTCMLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 1),
    _CpfrTCMLastUpdateTime_Type()
)
cpfrTCMLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMLastUpdateTime.setStatus("current")


class _CpfrTCMAge_Type(Gauge32):
    """Custom type cpfrTCMAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMAge_Type.__name__ = "Gauge32"
_CpfrTCMAge_Object = MibTableColumn
cpfrTCMAge = _CpfrTCMAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 2),
    _CpfrTCMAge_Type()
)
cpfrTCMAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMAge.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMAge.setUnits("seconds")


class _CpfrTCMetricsValid_Type(Bits):
    """Custom type cpfrTCMetricsValid based on Bits"""
    namedValues = NamedValues(
        *(("activeLTDelayAvg", 13),
          ("activeLTUnreachableAvg", 12),
          ("activeSTDelayAvg", 8),
          ("activeSTJitterAvg", 0),
          ("activeSTUnreachableAvg", 7),
          ("attempts", 2),
          ("mosPercentage", 1),
          ("packets", 3),
          ("passiveLTDelayAvg", 10),
          ("passiveLTLossAvg", 11),
          ("passiveLTUnreachableAvg", 9),
          ("passiveSTLossAvg", 6),
          ("passiveSTUnreachableAvg", 4),
          ("passiveSTdelayAvg", 5))
    )

_CpfrTCMetricsValid_Type.__name__ = "Bits"
_CpfrTCMetricsValid_Object = MibTableColumn
cpfrTCMetricsValid = _CpfrTCMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 3),
    _CpfrTCMetricsValid_Type()
)
cpfrTCMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMetricsValid.setStatus("current")


class _CpfrTCMActiveSTJitterAvg_Type(Gauge32):
    """Custom type cpfrTCMActiveSTJitterAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMActiveSTJitterAvg_Type.__name__ = "Gauge32"
_CpfrTCMActiveSTJitterAvg_Object = MibTableColumn
cpfrTCMActiveSTJitterAvg = _CpfrTCMActiveSTJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 4),
    _CpfrTCMActiveSTJitterAvg_Type()
)
cpfrTCMActiveSTJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMActiveSTJitterAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMActiveSTJitterAvg.setUnits("percent")


class _CpfrTCMMOSPercentage_Type(Gauge32):
    """Custom type cpfrTCMMOSPercentage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpfrTCMMOSPercentage_Type.__name__ = "Gauge32"
_CpfrTCMMOSPercentage_Object = MibTableColumn
cpfrTCMMOSPercentage = _CpfrTCMMOSPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 5),
    _CpfrTCMMOSPercentage_Type()
)
cpfrTCMMOSPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMMOSPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMMOSPercentage.setUnits("percent")


class _CpfrTCMAttempts_Type(Gauge32):
    """Custom type cpfrTCMAttempts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMAttempts_Type.__name__ = "Gauge32"
_CpfrTCMAttempts_Object = MibTableColumn
cpfrTCMAttempts = _CpfrTCMAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 6),
    _CpfrTCMAttempts_Type()
)
cpfrTCMAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMAttempts.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMAttempts.setUnits("attempts")


class _CpfrTCMPackets_Type(Gauge32):
    """Custom type cpfrTCMPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPackets_Type.__name__ = "Gauge32"
_CpfrTCMPackets_Object = MibTableColumn
cpfrTCMPackets = _CpfrTCMPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 7),
    _CpfrTCMPackets_Type()
)
cpfrTCMPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMPackets.setUnits("Packets/probe")


class _CpfrTCMPassiveSTUnreachableAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveSTUnreachableAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveSTUnreachableAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveSTUnreachableAvg_Object = MibTableColumn
cpfrTCMPassiveSTUnreachableAvg = _CpfrTCMPassiveSTUnreachableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 8),
    _CpfrTCMPassiveSTUnreachableAvg_Type()
)
cpfrTCMPassiveSTUnreachableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveSTUnreachableAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMPassiveSTUnreachableAvg.setUnits("flows-per-million")


class _CpfrTCMPassiveSTDelayAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveSTDelayAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveSTDelayAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveSTDelayAvg_Object = MibTableColumn
cpfrTCMPassiveSTDelayAvg = _CpfrTCMPassiveSTDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 9),
    _CpfrTCMPassiveSTDelayAvg_Type()
)
cpfrTCMPassiveSTDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveSTDelayAvg.setStatus("current")


class _CpfrTCMPassiveSTLossAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveSTLossAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveSTLossAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveSTLossAvg_Object = MibTableColumn
cpfrTCMPassiveSTLossAvg = _CpfrTCMPassiveSTLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 10),
    _CpfrTCMPassiveSTLossAvg_Type()
)
cpfrTCMPassiveSTLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveSTLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMPassiveSTLossAvg.setUnits("packets")


class _CpfrTCMActiveSTUnreachableAvg_Type(Gauge32):
    """Custom type cpfrTCMActiveSTUnreachableAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMActiveSTUnreachableAvg_Type.__name__ = "Gauge32"
_CpfrTCMActiveSTUnreachableAvg_Object = MibTableColumn
cpfrTCMActiveSTUnreachableAvg = _CpfrTCMActiveSTUnreachableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 11),
    _CpfrTCMActiveSTUnreachableAvg_Type()
)
cpfrTCMActiveSTUnreachableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMActiveSTUnreachableAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpfrTCMActiveSTUnreachableAvg.setUnits("flows-per-million")


class _CpfrTCMActiveSTDelayAvg_Type(Gauge32):
    """Custom type cpfrTCMActiveSTDelayAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMActiveSTDelayAvg_Type.__name__ = "Gauge32"
_CpfrTCMActiveSTDelayAvg_Object = MibTableColumn
cpfrTCMActiveSTDelayAvg = _CpfrTCMActiveSTDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 12),
    _CpfrTCMActiveSTDelayAvg_Type()
)
cpfrTCMActiveSTDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMActiveSTDelayAvg.setStatus("current")


class _CpfrTCMPassiveLTUnreachableAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveLTUnreachableAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveLTUnreachableAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveLTUnreachableAvg_Object = MibTableColumn
cpfrTCMPassiveLTUnreachableAvg = _CpfrTCMPassiveLTUnreachableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 13),
    _CpfrTCMPassiveLTUnreachableAvg_Type()
)
cpfrTCMPassiveLTUnreachableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveLTUnreachableAvg.setStatus("current")


class _CpfrTCMPassiveLTDelayAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveLTDelayAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveLTDelayAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveLTDelayAvg_Object = MibTableColumn
cpfrTCMPassiveLTDelayAvg = _CpfrTCMPassiveLTDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 14),
    _CpfrTCMPassiveLTDelayAvg_Type()
)
cpfrTCMPassiveLTDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveLTDelayAvg.setStatus("current")


class _CpfrTCMPassiveLTLossAvg_Type(Gauge32):
    """Custom type cpfrTCMPassiveLTLossAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMPassiveLTLossAvg_Type.__name__ = "Gauge32"
_CpfrTCMPassiveLTLossAvg_Object = MibTableColumn
cpfrTCMPassiveLTLossAvg = _CpfrTCMPassiveLTLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 15),
    _CpfrTCMPassiveLTLossAvg_Type()
)
cpfrTCMPassiveLTLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMPassiveLTLossAvg.setStatus("current")


class _CpfrTCMActiveLTUnreachableAvg_Type(Gauge32):
    """Custom type cpfrTCMActiveLTUnreachableAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMActiveLTUnreachableAvg_Type.__name__ = "Gauge32"
_CpfrTCMActiveLTUnreachableAvg_Object = MibTableColumn
cpfrTCMActiveLTUnreachableAvg = _CpfrTCMActiveLTUnreachableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 16),
    _CpfrTCMActiveLTUnreachableAvg_Type()
)
cpfrTCMActiveLTUnreachableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMActiveLTUnreachableAvg.setStatus("current")


class _CpfrTCMActiveLTDelayAvg_Type(Gauge32):
    """Custom type cpfrTCMActiveLTDelayAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpfrTCMActiveLTDelayAvg_Type.__name__ = "Gauge32"
_CpfrTCMActiveLTDelayAvg_Object = MibTableColumn
cpfrTCMActiveLTDelayAvg = _CpfrTCMActiveLTDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 13, 1, 17),
    _CpfrTCMActiveLTDelayAvg_Type()
)
cpfrTCMActiveLTDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrTCMActiveLTDelayAvg.setStatus("current")
_CpfrLinkGroupExitTable_Object = MibTable
cpfrLinkGroupExitTable = _CpfrLinkGroupExitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14)
)
if mibBuilder.loadTexts:
    cpfrLinkGroupExitTable.setStatus("current")
_CpfrLinkGroupExitEntry_Object = MibTableRow
cpfrLinkGroupExitEntry = _CpfrLinkGroupExitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1)
)
cpfrLinkGroupExitEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrMCIndex"),
    (0, "CISCO-PFR-MIB", "cpfrLinkGroupName"),
    (0, "CISCO-PFR-MIB", "cpfrLinkGroupIndex"),
)
if mibBuilder.loadTexts:
    cpfrLinkGroupExitEntry.setStatus("current")


class _CpfrLinkGroupName_Type(SnmpAdminString):
    """Custom type cpfrLinkGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpfrLinkGroupName_Type.__name__ = "SnmpAdminString"
_CpfrLinkGroupName_Object = MibTableColumn
cpfrLinkGroupName = _CpfrLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 1),
    _CpfrLinkGroupName_Type()
)
cpfrLinkGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrLinkGroupName.setStatus("current")
_CpfrLinkGroupIndex_Type = Unsigned32
_CpfrLinkGroupIndex_Object = MibTableColumn
cpfrLinkGroupIndex = _CpfrLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 2),
    _CpfrLinkGroupIndex_Type()
)
cpfrLinkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrLinkGroupIndex.setStatus("current")


class _CpfrLinkGroupStorageType_Type(StorageType):
    """Custom type cpfrLinkGroupStorageType based on StorageType"""


_CpfrLinkGroupStorageType_Object = MibTableColumn
cpfrLinkGroupStorageType = _CpfrLinkGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 3),
    _CpfrLinkGroupStorageType_Type()
)
cpfrLinkGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLinkGroupStorageType.setStatus("current")
_CpfrLinkGroupRowStatus_Type = RowStatus
_CpfrLinkGroupRowStatus_Object = MibTableColumn
cpfrLinkGroupRowStatus = _CpfrLinkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 4),
    _CpfrLinkGroupRowStatus_Type()
)
cpfrLinkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLinkGroupRowStatus.setStatus("current")
_CpfrLinkGroupBRIndex_Type = PfrBorderRouterIndex
_CpfrLinkGroupBRIndex_Object = MibTableColumn
cpfrLinkGroupBRIndex = _CpfrLinkGroupBRIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 5),
    _CpfrLinkGroupBRIndex_Type()
)
cpfrLinkGroupBRIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLinkGroupBRIndex.setStatus("current")
_CpfrLinkGroupExitIndex_Type = PfrExitIndex
_CpfrLinkGroupExitIndex_Object = MibTableColumn
cpfrLinkGroupExitIndex = _CpfrLinkGroupExitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 6),
    _CpfrLinkGroupExitIndex_Type()
)
cpfrLinkGroupExitIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrLinkGroupExitIndex.setStatus("current")


class _CpfrLinkGroupType_Type(Integer32):
    """Custom type cpfrLinkGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallbackLinkGroup", 2),
          ("none", 3),
          ("primaryLinkGroup", 1))
    )


_CpfrLinkGroupType_Type.__name__ = "Integer32"
_CpfrLinkGroupType_Object = MibTableColumn
cpfrLinkGroupType = _CpfrLinkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 14, 1, 7),
    _CpfrLinkGroupType_Type()
)
cpfrLinkGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfrLinkGroupType.setStatus("current")
_CpfrNbarApplListTable_Object = MibTable
cpfrNbarApplListTable = _CpfrNbarApplListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15)
)
if mibBuilder.loadTexts:
    cpfrNbarApplListTable.setStatus("current")
_CpfrNbarApplListEntry_Object = MibTableRow
cpfrNbarApplListEntry = _CpfrNbarApplListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1)
)
cpfrNbarApplListEntry.setIndexNames(
    (0, "CISCO-PFR-MIB", "cpfrNbarApplListName"),
    (0, "CISCO-PFR-MIB", "cpfrNbarApplIndex"),
)
if mibBuilder.loadTexts:
    cpfrNbarApplListEntry.setStatus("current")


class _CpfrNbarApplListName_Type(SnmpAdminString):
    """Custom type cpfrNbarApplListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpfrNbarApplListName_Type.__name__ = "SnmpAdminString"
_CpfrNbarApplListName_Object = MibTableColumn
cpfrNbarApplListName = _CpfrNbarApplListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1, 1),
    _CpfrNbarApplListName_Type()
)
cpfrNbarApplListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrNbarApplListName.setStatus("current")
_CpfrNbarApplIndex_Type = Unsigned32
_CpfrNbarApplIndex_Object = MibTableColumn
cpfrNbarApplIndex = _CpfrNbarApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1, 2),
    _CpfrNbarApplIndex_Type()
)
cpfrNbarApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfrNbarApplIndex.setStatus("current")


class _CpfrNbarApplListStorageType_Type(StorageType):
    """Custom type cpfrNbarApplListStorageType based on StorageType"""


_CpfrNbarApplListStorageType_Object = MibTableColumn
cpfrNbarApplListStorageType = _CpfrNbarApplListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1, 3),
    _CpfrNbarApplListStorageType_Type()
)
cpfrNbarApplListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrNbarApplListStorageType.setStatus("current")
_CpfrNbarApplListRowStatus_Type = RowStatus
_CpfrNbarApplListRowStatus_Object = MibTableColumn
cpfrNbarApplListRowStatus = _CpfrNbarApplListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1, 4),
    _CpfrNbarApplListRowStatus_Type()
)
cpfrNbarApplListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrNbarApplListRowStatus.setStatus("current")
_CpfrNbarApplPdIndex_Type = CiscoPdProtocolIndex
_CpfrNbarApplPdIndex_Object = MibTableColumn
cpfrNbarApplPdIndex = _CpfrNbarApplPdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 1, 15, 1, 5),
    _CpfrNbarApplPdIndex_Type()
)
cpfrNbarApplPdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpfrNbarApplPdIndex.setStatus("current")
_CiscoPfrMIBConform_ObjectIdentity = ObjectIdentity
ciscoPfrMIBConform = _CiscoPfrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2)
)
_CiscoPfrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPfrMIBCompliances = _CiscoPfrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 1)
)
_CiscoPfrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPfrMIBGroups = _CiscoPfrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2)
)

# Managed Objects groups

cpfrMasterControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 1)
)
cpfrMasterControllerGroup.setObjects(
      *(("CISCO-PFR-MIB", "cpfrMCStorageType"),
        ("CISCO-PFR-MIB", "cpfrMCRowStatus"),
        ("CISCO-PFR-MIB", "cpfrMCKeepAliveTimer"),
        ("CISCO-PFR-MIB", "cpfrMCMaxPrefixTotal"),
        ("CISCO-PFR-MIB", "cpfrMCMaxPrefixLearn"),
        ("CISCO-PFR-MIB", "cpfrMCEntranceLinksMaxUtil"),
        ("CISCO-PFR-MIB", "cpfrMCExitLinksMaxUtil"),
        ("CISCO-PFR-MIB", "cpfrMCPortNumber"),
        ("CISCO-PFR-MIB", "cpfrMCTracerouteProbeDelay"),
        ("CISCO-PFR-MIB", "cpfrMCRsvpPostDialDelay"),
        ("CISCO-PFR-MIB", "cpfrMCRsvpSignalingRetries"),
        ("CISCO-PFR-MIB", "cpfrMCNetflowExporter"),
        ("CISCO-PFR-MIB", "cpfrMCAdminStatus"),
        ("CISCO-PFR-MIB", "cpfrMCOperStatus"),
        ("CISCO-PFR-MIB", "cpfrMCConnStatus"),
        ("CISCO-PFR-MIB", "cpfrMCNumofBorderRouters"),
        ("CISCO-PFR-MIB", "cpfrMCNumofExits"),
        ("CISCO-PFR-MIB", "cpfrMCLearnState"),
        ("CISCO-PFR-MIB", "cpfrMCLearnStateTimeRemain"),
        ("CISCO-PFR-MIB", "cpfrMCPrefixCount"),
        ("CISCO-PFR-MIB", "cpfrMCPrefixLearned"),
        ("CISCO-PFR-MIB", "cpfrMCPrefixConfigured"),
        ("CISCO-PFR-MIB", "cpfrMCPbrMet"),
        ("CISCO-PFR-MIB", "cpfrMapStorageType"),
        ("CISCO-PFR-MIB", "cpfrMapRowStatus"),
        ("CISCO-PFR-MIB", "cpfrMapName"),
        ("CISCO-PFR-MIB", "cpfrMapBackoffMinTimer"),
        ("CISCO-PFR-MIB", "cpfrMapBackoffMaxTimer"),
        ("CISCO-PFR-MIB", "cpfrMapBackoffStepTimer"),
        ("CISCO-PFR-MIB", "cpfrMapDelayType"),
        ("CISCO-PFR-MIB", "cpfrMapDelayRelativePercent"),
        ("CISCO-PFR-MIB", "cpfrMapDelayThresholdMax"),
        ("CISCO-PFR-MIB", "cpfrMapHolddownTimer"),
        ("CISCO-PFR-MIB", "cpfrMapPrefixForwardInterface"),
        ("CISCO-PFR-MIB", "cpfrMapJitterThresholdMax"),
        ("CISCO-PFR-MIB", "cpfrMapLinkGroupName"),
        ("CISCO-PFR-MIB", "cpfrMapFallbackLinkGroupName"),
        ("CISCO-PFR-MIB", "cpfrMapLossType"),
        ("CISCO-PFR-MIB", "cpfrMapLossRelativeAvg"),
        ("CISCO-PFR-MIB", "cpfrMapLossThresholdMax"),
        ("CISCO-PFR-MIB", "cpfrMapModeMonitor"),
        ("CISCO-PFR-MIB", "cpfrMapModeRouteOpts"),
        ("CISCO-PFR-MIB", "cpfrMapRouteMetricBgpLocalPref"),
        ("CISCO-PFR-MIB", "cpfrMapRouteMetricEigrpTagCommunity"),
        ("CISCO-PFR-MIB", "cpfrMapRouteMetricStaticTag"),
        ("CISCO-PFR-MIB", "cpfrMapModeSelectExitType"),
        ("CISCO-PFR-MIB", "cpfrMapMOSThresholdMin"),
        ("CISCO-PFR-MIB", "cpfrMapMOSPercentage"),
        ("CISCO-PFR-MIB", "cpfrMapNextHopAddressType"),
        ("CISCO-PFR-MIB", "cpfrMapNextHopAddress"),
        ("CISCO-PFR-MIB", "cpfrMapPeriodicTimer"),
        ("CISCO-PFR-MIB", "cpfrMapActiveProbeFrequency"),
        ("CISCO-PFR-MIB", "cpfrMapActiveProbePackets"),
        ("CISCO-PFR-MIB", "cpfrMapTracerouteReporting"),
        ("CISCO-PFR-MIB", "cpfrMapUnreachableType"),
        ("CISCO-PFR-MIB", "cpfrMapUnreachableRelativeAvg"),
        ("CISCO-PFR-MIB", "cpfrMapUnreachableThresholdMax"),
        ("CISCO-PFR-MIB", "cpfrMapRoundRobinResolver"),
        ("CISCO-PFR-MIB", "cpfrMatchValid"),
        ("CISCO-PFR-MIB", "cpfrMatchAddrAccessList"),
        ("CISCO-PFR-MIB", "cpfrMatchAddrPrefixList"),
        ("CISCO-PFR-MIB", "cpfrMatchAddrPrefixInside"),
        ("CISCO-PFR-MIB", "cpfrMatchLearnMode"),
        ("CISCO-PFR-MIB", "cpfrMatchLearnListName"),
        ("CISCO-PFR-MIB", "cpfrMatchTCNbarListName"),
        ("CISCO-PFR-MIB", "cpfrMatchTCNbarApplPfxList"),
        ("CISCO-PFR-MIB", "cpfrMatchTCPfxInside"),
        ("CISCO-PFR-MIB", "cpfrLearnListStorageType"),
        ("CISCO-PFR-MIB", "cpfrLearnListRowStatus"),
        ("CISCO-PFR-MIB", "cpfrLearnListReferenceName"),
        ("CISCO-PFR-MIB", "cpfrLearnListSequenceNum"),
        ("CISCO-PFR-MIB", "cpfrLearnListMethod"),
        ("CISCO-PFR-MIB", "cpfrLearnListAclName"),
        ("CISCO-PFR-MIB", "cpfrLearnListPfxName"),
        ("CISCO-PFR-MIB", "cpfrLearnListPfxInside"),
        ("CISCO-PFR-MIB", "cpfrLearnListNbarAppl"),
        ("CISCO-PFR-MIB", "cpfrLearnListFilterPfxName"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeStorageType"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeRowStatus"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeType"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeTargetAddressType"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeTargetAddress"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeTargetPortNumber"),
        ("CISCO-PFR-MIB", "cpfrActiveProbePfrMapIndex"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeDscpValue"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeCodecName"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeMapIndex"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeMapPolicyIndex"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeAdminStatus"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeOperStatus"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeAssignedPfxAddressType"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeAssignedPfxAddress"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeAssignedPfxLen"),
        ("CISCO-PFR-MIB", "cpfrActiveProbeMethod"),
        ("CISCO-PFR-MIB", "cpfrResolveStorageType"),
        ("CISCO-PFR-MIB", "cpfrResolveRowStatus"),
        ("CISCO-PFR-MIB", "cpfrResolvePolicyType"),
        ("CISCO-PFR-MIB", "cpfrResolveVariance"),
        ("CISCO-PFR-MIB", "cpfrResolveMapIndex"),
        ("CISCO-PFR-MIB", "cpfrResolveMapPolicyIndex"),
        ("CISCO-PFR-MIB", "cpfrLearnAggregationType"),
        ("CISCO-PFR-MIB", "cpfrLearnAggregationPrefixLen"),
        ("CISCO-PFR-MIB", "cpfrLearnMethod"),
        ("CISCO-PFR-MIB", "cpfrLearnExpireType"),
        ("CISCO-PFR-MIB", "cpfrLearnExpireSessionNum"),
        ("CISCO-PFR-MIB", "cpfrLearnExpireTime"),
        ("CISCO-PFR-MIB", "cpfrLearnMonitorPeriod"),
        ("CISCO-PFR-MIB", "cpfrLearnPeriodInterval"),
        ("CISCO-PFR-MIB", "cpfrLearnPrefixesNumber"),
        ("CISCO-PFR-MIB", "cpfrLearnAggAccesslistName"),
        ("CISCO-PFR-MIB", "cpfrLearnFilterAccessListName"),
        ("CISCO-PFR-MIB", "cpfrNbarApplListStorageType"),
        ("CISCO-PFR-MIB", "cpfrNbarApplListRowStatus"),
        ("CISCO-PFR-MIB", "cpfrNbarApplPdIndex"),
        ("CISCO-PFR-MIB", "cpfrResolvePriority"),
        ("CISCO-PFR-MIB", "cpfrMCMapIndex"))
)
if mibBuilder.loadTexts:
    cpfrMasterControllerGroup.setStatus("current")

cpfrBorderRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 2)
)
cpfrBorderRouterGroup.setObjects(
      *(("CISCO-PFR-MIB", "cpfrBRStorageType"),
        ("CISCO-PFR-MIB", "cpfrBRRowStatus"),
        ("CISCO-PFR-MIB", "cpfrBRAddressType"),
        ("CISCO-PFR-MIB", "cpfrBRAddress"),
        ("CISCO-PFR-MIB", "cpfrBRKeyName"),
        ("CISCO-PFR-MIB", "cpfrBROperStatus"),
        ("CISCO-PFR-MIB", "cpfrBRConnStatus"),
        ("CISCO-PFR-MIB", "cpfrBRUpTime"),
        ("CISCO-PFR-MIB", "cpfrBRConnFailureReason"),
        ("CISCO-PFR-MIB", "cpfrBRAuthFailCount"),
        ("CISCO-PFR-MIB", "cpfrExitStorageType"),
        ("CISCO-PFR-MIB", "cpfrExitRowStatus"),
        ("CISCO-PFR-MIB", "cpfrExitName"),
        ("CISCO-PFR-MIB", "cpfrExitType"),
        ("CISCO-PFR-MIB", "cpfrDowngradeBgpCommunity"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilRxType"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilRxAbsolute"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilRxPercentage"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilTxType"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilTxAbsolute"),
        ("CISCO-PFR-MIB", "cpfrExitMaxUtilTxPercentage"),
        ("CISCO-PFR-MIB", "cpfrExitCostCalcMethod"),
        ("CISCO-PFR-MIB", "cpfrExitCostDiscard"),
        ("CISCO-PFR-MIB", "cpfrExitCostDiscardType"),
        ("CISCO-PFR-MIB", "cpfrExitCostDiscardAbsolute"),
        ("CISCO-PFR-MIB", "cpfrExitCostDiscardPercent"),
        ("CISCO-PFR-MIB", "cpfrExitCostEndDayOfMonth"),
        ("CISCO-PFR-MIB", "cpfrExitCostEndOffsetType"),
        ("CISCO-PFR-MIB", "cpfrExitCostEndOffset"),
        ("CISCO-PFR-MIB", "cpfrExitCostFixedFeeCost"),
        ("CISCO-PFR-MIB", "cpfrExitCostNickName"),
        ("CISCO-PFR-MIB", "cpfrExitCostSamplingPeriod"),
        ("CISCO-PFR-MIB", "cpfrExitCostRollupPeriod"),
        ("CISCO-PFR-MIB", "cpfrExitCostSummerTimeStart"),
        ("CISCO-PFR-MIB", "cpfrExitCostSummerTimeOffset"),
        ("CISCO-PFR-MIB", "cpfrExitCostSummerTimeEnd"),
        ("CISCO-PFR-MIB", "cpfrExitCapacity"),
        ("CISCO-PFR-MIB", "cpfrExitRxBandwidth"),
        ("CISCO-PFR-MIB", "cpfrExitTxBandwidth"),
        ("CISCO-PFR-MIB", "cpfrExitTxLoad"),
        ("CISCO-PFR-MIB", "cpfrExitNickName"),
        ("CISCO-PFR-MIB", "cpfrExitCost1"),
        ("CISCO-PFR-MIB", "cpfrExitSustainedUtil1"),
        ("CISCO-PFR-MIB", "cpfrExitCost2"),
        ("CISCO-PFR-MIB", "cpfrExitSustainedUtil2"),
        ("CISCO-PFR-MIB", "cpfrExitCost3"),
        ("CISCO-PFR-MIB", "cpfrExitSustainedUtil3"),
        ("CISCO-PFR-MIB", "cpfrExitRollupTotal"),
        ("CISCO-PFR-MIB", "cpfrExitRollupDiscard"),
        ("CISCO-PFR-MIB", "cpfrExitRollupLeft"),
        ("CISCO-PFR-MIB", "cpfrExitRollupCollected"),
        ("CISCO-PFR-MIB", "cpfrExitRollupMomTgtUtil"),
        ("CISCO-PFR-MIB", "cpfrExitRollupStartingTgtUtil"),
        ("CISCO-PFR-MIB", "cpfrExitRollupCurrentTgtUtil"),
        ("CISCO-PFR-MIB", "cpfrExitRollupCumRxBytes"),
        ("CISCO-PFR-MIB", "cpfrExitRollupCumTxBytes"),
        ("CISCO-PFR-MIB", "cpfrExitRollupTimeRemain"),
        ("CISCO-PFR-MIB", "cpfrExitOperStatus"),
        ("CISCO-PFR-MIB", "cpfrExitRsvpBandwidthPool"),
        ("CISCO-PFR-MIB", "cpfrExitCostTierStorageType"),
        ("CISCO-PFR-MIB", "cpfrExitCostTierRowStatus"),
        ("CISCO-PFR-MIB", "cpfrExitCostTierFee"),
        ("CISCO-PFR-MIB", "cpfrLinkGroupStorageType"),
        ("CISCO-PFR-MIB", "cpfrLinkGroupRowStatus"),
        ("CISCO-PFR-MIB", "cpfrLinkGroupBRIndex"),
        ("CISCO-PFR-MIB", "cpfrLinkGroupExitIndex"),
        ("CISCO-PFR-MIB", "cpfrExitRxLoad"))
)
if mibBuilder.loadTexts:
    cpfrBorderRouterGroup.setStatus("current")

cpfrTrafficClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 3)
)
cpfrTrafficClassGroup.setObjects(
      *(("CISCO-PFR-MIB", "cpfrTrafficClassValid"),
        ("CISCO-PFR-MIB", "cpfrTCSrcPrefixType"),
        ("CISCO-PFR-MIB", "cpfrTCSrcPrefix"),
        ("CISCO-PFR-MIB", "cpfrTCSrcPrefixLen"),
        ("CISCO-PFR-MIB", "cpfrTCSrcMinPort"),
        ("CISCO-PFR-MIB", "cpfrTCDstPrefixType"),
        ("CISCO-PFR-MIB", "cpfrTCDstPrefix"),
        ("CISCO-PFR-MIB", "cpfrTCDstPrefixLen"),
        ("CISCO-PFR-MIB", "cpfrTCDstMinPort"),
        ("CISCO-PFR-MIB", "cpfrTCDscpValue"),
        ("CISCO-PFR-MIB", "cpfrTCProtocol"),
        ("CISCO-PFR-MIB", "cpfrTCNbarApplication"),
        ("CISCO-PFR-MIB", "cpfrTCBRIndex"),
        ("CISCO-PFR-MIB", "cpfrTCBRExitIndex"),
        ("CISCO-PFR-MIB", "cpfrTCMapIndex"),
        ("CISCO-PFR-MIB", "cpfrTCMapPolicyIndex"),
        ("CISCO-PFR-MIB", "cpfrTCStatus"),
        ("CISCO-PFR-MIB", "cpfrTCSType"),
        ("CISCO-PFR-MIB", "cpfrTCSLearnListIndex"),
        ("CISCO-PFR-MIB", "cpfrTCSTimeOnCurrExit"),
        ("CISCO-PFR-MIB", "cpfrTCSControlState"),
        ("CISCO-PFR-MIB", "cpfrTCSControlBy"),
        ("CISCO-PFR-MIB", "cpfrTCSTimeRemainCurrState"),
        ("CISCO-PFR-MIB", "cpfrTCSLastOOPEventTime"),
        ("CISCO-PFR-MIB", "cpfrTCSLastOOPReason"),
        ("CISCO-PFR-MIB", "cpfrTCSLastRouteChangeEvent"),
        ("CISCO-PFR-MIB", "cpfrTCSLastRouteChangeReason"),
        ("CISCO-PFR-MIB", "cpfrTCMLastUpdateTime"),
        ("CISCO-PFR-MIB", "cpfrTCMAge"),
        ("CISCO-PFR-MIB", "cpfrTCMetricsValid"),
        ("CISCO-PFR-MIB", "cpfrTCMActiveSTJitterAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMMOSPercentage"),
        ("CISCO-PFR-MIB", "cpfrTCMAttempts"),
        ("CISCO-PFR-MIB", "cpfrTCMPackets"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveSTUnreachableAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveSTDelayAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveSTLossAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMActiveSTUnreachableAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMActiveSTDelayAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveLTUnreachableAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveLTDelayAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMPassiveLTLossAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMActiveLTUnreachableAvg"),
        ("CISCO-PFR-MIB", "cpfrTCMActiveLTDelayAvg"),
        ("CISCO-PFR-MIB", "cpfrTCSrcMaxPort"),
        ("CISCO-PFR-MIB", "cpfrTCDstMaxPort"))
)
if mibBuilder.loadTexts:
    cpfrTrafficClassGroup.setStatus("current")

cpfrMasterControllerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 4)
)
cpfrMasterControllerGroupRev1.setObjects(
      *(("CISCO-PFR-MIB", "cpfrMCLoggingAdminStatus"),
        ("CISCO-PFR-MIB", "cpfrMCControlMode"),
        ("CISCO-PFR-MIB", "cpfrMCClear"),
        ("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlType"),
        ("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlThreshold"),
        ("CISCO-PFR-MIB", "cpfrMapEventTCCount"),
        ("CISCO-PFR-MIB", "cpfrMCLastClearTime"),
        ("CISCO-PFR-MIB", "cpfrMCNotifisControl"),
        ("CISCO-PFR-MIB", "cpfrMCChangeConfigType"),
        ("CISCO-PFR-MIB", "cpfrMCChangeConfigValue"))
)
if mibBuilder.loadTexts:
    cpfrMasterControllerGroupRev1.setStatus("current")

cpfrBorderRouterGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 5)
)
cpfrBorderRouterGroupRev1.setObjects(
    ("CISCO-PFR-MIB", "cpfrLinkGroupType")
)
if mibBuilder.loadTexts:
    cpfrBorderRouterGroupRev1.setStatus("current")


# Notification objects

cpfrMCStatusChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 1)
)
cpfrMCStatusChangeNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrMCChangeConfigType"),
        ("CISCO-PFR-MIB", "cpfrMCChangeConfigValue"))
)
if mibBuilder.loadTexts:
    cpfrMCStatusChangeNotify.setStatus(
        "current"
    )

cpfrBRStatusChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 2)
)
cpfrBRStatusChangeNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrBRAddressType"),
        ("CISCO-PFR-MIB", "cpfrBRAddress"),
        ("CISCO-PFR-MIB", "cpfrBROperStatus"),
        ("CISCO-PFR-MIB", "cpfrBRConnStatus"),
        ("CISCO-PFR-MIB", "cpfrBRConnFailureReason"))
)
if mibBuilder.loadTexts:
    cpfrBRStatusChangeNotify.setStatus(
        "current"
    )

cpfrExitStatusChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 3)
)
cpfrExitStatusChangeNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrExitName"),
        ("CISCO-PFR-MIB", "cpfrExitType"),
        ("CISCO-PFR-MIB", "cpfrExitOperStatus"),
        ("CISCO-PFR-MIB", "cpfrBRAddressType"),
        ("CISCO-PFR-MIB", "cpfrBRAddress"))
)
if mibBuilder.loadTexts:
    cpfrExitStatusChangeNotify.setStatus(
        "current"
    )

cpfrTrafficClassEventNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 4)
)
cpfrTrafficClassEventNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrTCStatus"),
        ("CISCO-PFR-MIB", "cpfrTCSLastOOPReason"),
        ("CISCO-PFR-MIB", "cpfrBRAddressType"),
        ("CISCO-PFR-MIB", "cpfrBRAddress"),
        ("CISCO-PFR-MIB", "cpfrExitName"),
        ("CISCO-PFR-MIB", "cpfrLinkGroupType"))
)
if mibBuilder.loadTexts:
    cpfrTrafficClassEventNotify.setStatus(
        "current"
    )

cpfrTCInpolicyThresholdBelowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 5)
)
cpfrTCInpolicyThresholdBelowNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlType"),
        ("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlThreshold"),
        ("CISCO-PFR-MIB", "cpfrMapEventTCCount"))
)
if mibBuilder.loadTexts:
    cpfrTCInpolicyThresholdBelowNotify.setStatus(
        "current"
    )

cpfrTCPrimaryThresholdBelowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 0, 6)
)
cpfrTCPrimaryThresholdBelowNotify.setObjects(
      *(("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlType"),
        ("CISCO-PFR-MIB", "cpfrMapEventNotifCtrlThreshold"),
        ("CISCO-PFR-MIB", "cpfrMapEventTCCount"))
)
if mibBuilder.loadTexts:
    cpfrTCPrimaryThresholdBelowNotify.setStatus(
        "current"
    )


# Notifications groups

cpfrMCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 2, 6)
)
cpfrMCNotificationGroup.setObjects(
      *(("CISCO-PFR-MIB", "cpfrBRStatusChangeNotify"),
        ("CISCO-PFR-MIB", "cpfrExitStatusChangeNotify"),
        ("CISCO-PFR-MIB", "cpfrTrafficClassEventNotify"),
        ("CISCO-PFR-MIB", "cpfrTCInpolicyThresholdBelowNotify"),
        ("CISCO-PFR-MIB", "cpfrTCPrimaryThresholdBelowNotify"),
        ("CISCO-PFR-MIB", "cpfrMCStatusChangeNotify"))
)
if mibBuilder.loadTexts:
    cpfrMCNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPfrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPfrMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPfrMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 772, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPfrMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PFR-MIB",
    **{"PfrMetricPolicyType": PfrMetricPolicyType,
       "PfrLastUncontrolReason": PfrLastUncontrolReason,
       "PfRMasterControllerIndex": PfRMasterControllerIndex,
       "PfrBorderRouterIndex": PfrBorderRouterIndex,
       "PfrExitIndex": PfrExitIndex,
       "PfrMapIndex": PfrMapIndex,
       "PfrMapPolicyIndex": PfrMapPolicyIndex,
       "PfrMapIndexOrZero": PfrMapIndexOrZero,
       "PfrLearnListIndex": PfrLearnListIndex,
       "PfrLearnListIndexOrZero": PfrLearnListIndexOrZero,
       "PfrResolvePolicyType": PfrResolvePolicyType,
       "ciscoPfrMIB": ciscoPfrMIB,
       "ciscoPfrMIBNotifs": ciscoPfrMIBNotifs,
       "cpfrMCStatusChangeNotify": cpfrMCStatusChangeNotify,
       "cpfrBRStatusChangeNotify": cpfrBRStatusChangeNotify,
       "cpfrExitStatusChangeNotify": cpfrExitStatusChangeNotify,
       "cpfrTrafficClassEventNotify": cpfrTrafficClassEventNotify,
       "cpfrTCInpolicyThresholdBelowNotify": cpfrTCInpolicyThresholdBelowNotify,
       "cpfrTCPrimaryThresholdBelowNotify": cpfrTCPrimaryThresholdBelowNotify,
       "ciscoPfrMIBObjects": ciscoPfrMIBObjects,
       "cpfrMCTable": cpfrMCTable,
       "cpfrMCEntry": cpfrMCEntry,
       "cpfrMCIndex": cpfrMCIndex,
       "cpfrMCStorageType": cpfrMCStorageType,
       "cpfrMCRowStatus": cpfrMCRowStatus,
       "cpfrMCMapIndex": cpfrMCMapIndex,
       "cpfrMCKeepAliveTimer": cpfrMCKeepAliveTimer,
       "cpfrMCMaxPrefixTotal": cpfrMCMaxPrefixTotal,
       "cpfrMCMaxPrefixLearn": cpfrMCMaxPrefixLearn,
       "cpfrMCEntranceLinksMaxUtil": cpfrMCEntranceLinksMaxUtil,
       "cpfrMCExitLinksMaxUtil": cpfrMCExitLinksMaxUtil,
       "cpfrMCPortNumber": cpfrMCPortNumber,
       "cpfrMCTracerouteProbeDelay": cpfrMCTracerouteProbeDelay,
       "cpfrMCRsvpPostDialDelay": cpfrMCRsvpPostDialDelay,
       "cpfrMCRsvpSignalingRetries": cpfrMCRsvpSignalingRetries,
       "cpfrMCNetflowExporter": cpfrMCNetflowExporter,
       "cpfrMCAdminStatus": cpfrMCAdminStatus,
       "cpfrMCOperStatus": cpfrMCOperStatus,
       "cpfrMCConnStatus": cpfrMCConnStatus,
       "cpfrMCNumofBorderRouters": cpfrMCNumofBorderRouters,
       "cpfrMCNumofExits": cpfrMCNumofExits,
       "cpfrMCLearnState": cpfrMCLearnState,
       "cpfrMCLearnStateTimeRemain": cpfrMCLearnStateTimeRemain,
       "cpfrMCPrefixCount": cpfrMCPrefixCount,
       "cpfrMCPrefixLearned": cpfrMCPrefixLearned,
       "cpfrMCPrefixConfigured": cpfrMCPrefixConfigured,
       "cpfrMCPbrMet": cpfrMCPbrMet,
       "cpfrMCLoggingAdminStatus": cpfrMCLoggingAdminStatus,
       "cpfrMCControlMode": cpfrMCControlMode,
       "cpfrMCClear": cpfrMCClear,
       "cpfrMCLastClearTime": cpfrMCLastClearTime,
       "cpfrMCNotifisControl": cpfrMCNotifisControl,
       "cpfrMCChangeConfigType": cpfrMCChangeConfigType,
       "cpfrMCChangeConfigValue": cpfrMCChangeConfigValue,
       "cpfrMapTable": cpfrMapTable,
       "cpfrMapEntry": cpfrMapEntry,
       "cpfrMapIndex": cpfrMapIndex,
       "cpfrMapPolicyIndex": cpfrMapPolicyIndex,
       "cpfrMapStorageType": cpfrMapStorageType,
       "cpfrMapRowStatus": cpfrMapRowStatus,
       "cpfrMapName": cpfrMapName,
       "cpfrMapBackoffMinTimer": cpfrMapBackoffMinTimer,
       "cpfrMapBackoffMaxTimer": cpfrMapBackoffMaxTimer,
       "cpfrMapBackoffStepTimer": cpfrMapBackoffStepTimer,
       "cpfrMapDelayType": cpfrMapDelayType,
       "cpfrMapDelayRelativePercent": cpfrMapDelayRelativePercent,
       "cpfrMapDelayThresholdMax": cpfrMapDelayThresholdMax,
       "cpfrMapHolddownTimer": cpfrMapHolddownTimer,
       "cpfrMapPrefixForwardInterface": cpfrMapPrefixForwardInterface,
       "cpfrMapJitterThresholdMax": cpfrMapJitterThresholdMax,
       "cpfrMapLinkGroupName": cpfrMapLinkGroupName,
       "cpfrMapFallbackLinkGroupName": cpfrMapFallbackLinkGroupName,
       "cpfrMapLossType": cpfrMapLossType,
       "cpfrMapLossRelativeAvg": cpfrMapLossRelativeAvg,
       "cpfrMapLossThresholdMax": cpfrMapLossThresholdMax,
       "cpfrMapModeMonitor": cpfrMapModeMonitor,
       "cpfrMapModeRouteOpts": cpfrMapModeRouteOpts,
       "cpfrMapRouteMetricBgpLocalPref": cpfrMapRouteMetricBgpLocalPref,
       "cpfrMapRouteMetricEigrpTagCommunity": cpfrMapRouteMetricEigrpTagCommunity,
       "cpfrMapRouteMetricStaticTag": cpfrMapRouteMetricStaticTag,
       "cpfrMapModeSelectExitType": cpfrMapModeSelectExitType,
       "cpfrMapMOSThresholdMin": cpfrMapMOSThresholdMin,
       "cpfrMapMOSPercentage": cpfrMapMOSPercentage,
       "cpfrMapNextHopAddressType": cpfrMapNextHopAddressType,
       "cpfrMapNextHopAddress": cpfrMapNextHopAddress,
       "cpfrMapPeriodicTimer": cpfrMapPeriodicTimer,
       "cpfrMapActiveProbeFrequency": cpfrMapActiveProbeFrequency,
       "cpfrMapActiveProbePackets": cpfrMapActiveProbePackets,
       "cpfrMapTracerouteReporting": cpfrMapTracerouteReporting,
       "cpfrMapUnreachableType": cpfrMapUnreachableType,
       "cpfrMapUnreachableRelativeAvg": cpfrMapUnreachableRelativeAvg,
       "cpfrMapUnreachableThresholdMax": cpfrMapUnreachableThresholdMax,
       "cpfrMapRoundRobinResolver": cpfrMapRoundRobinResolver,
       "cpfrMapEventNotifCtrlType": cpfrMapEventNotifCtrlType,
       "cpfrMapEventNotifCtrlThreshold": cpfrMapEventNotifCtrlThreshold,
       "cpfrMapEventTCCount": cpfrMapEventTCCount,
       "cpfrMatchTable": cpfrMatchTable,
       "cpfrMatchEntry": cpfrMatchEntry,
       "cpfrMatchValid": cpfrMatchValid,
       "cpfrMatchAddrAccessList": cpfrMatchAddrAccessList,
       "cpfrMatchAddrPrefixList": cpfrMatchAddrPrefixList,
       "cpfrMatchAddrPrefixInside": cpfrMatchAddrPrefixInside,
       "cpfrMatchLearnMode": cpfrMatchLearnMode,
       "cpfrMatchLearnListName": cpfrMatchLearnListName,
       "cpfrMatchTCNbarListName": cpfrMatchTCNbarListName,
       "cpfrMatchTCNbarApplPfxList": cpfrMatchTCNbarApplPfxList,
       "cpfrMatchTCPfxInside": cpfrMatchTCPfxInside,
       "cpfrResolveTable": cpfrResolveTable,
       "cpfrResolveEntry": cpfrResolveEntry,
       "cpfrResolveIndex": cpfrResolveIndex,
       "cpfrResolveStorageType": cpfrResolveStorageType,
       "cpfrResolveRowStatus": cpfrResolveRowStatus,
       "cpfrResolvePriority": cpfrResolvePriority,
       "cpfrResolvePolicyType": cpfrResolvePolicyType,
       "cpfrResolveVariance": cpfrResolveVariance,
       "cpfrResolveMapIndex": cpfrResolveMapIndex,
       "cpfrResolveMapPolicyIndex": cpfrResolveMapPolicyIndex,
       "cpfrLearnTable": cpfrLearnTable,
       "cpfrLearnEntry": cpfrLearnEntry,
       "cpfrLearnAggregationType": cpfrLearnAggregationType,
       "cpfrLearnAggregationPrefixLen": cpfrLearnAggregationPrefixLen,
       "cpfrLearnMethod": cpfrLearnMethod,
       "cpfrLearnExpireType": cpfrLearnExpireType,
       "cpfrLearnExpireSessionNum": cpfrLearnExpireSessionNum,
       "cpfrLearnExpireTime": cpfrLearnExpireTime,
       "cpfrLearnMonitorPeriod": cpfrLearnMonitorPeriod,
       "cpfrLearnPeriodInterval": cpfrLearnPeriodInterval,
       "cpfrLearnPrefixesNumber": cpfrLearnPrefixesNumber,
       "cpfrLearnAggAccesslistName": cpfrLearnAggAccesslistName,
       "cpfrLearnFilterAccessListName": cpfrLearnFilterAccessListName,
       "cpfrLearnListTable": cpfrLearnListTable,
       "cpfrLearnListEntry": cpfrLearnListEntry,
       "cpfrLearnListIndex": cpfrLearnListIndex,
       "cpfrLearnListStorageType": cpfrLearnListStorageType,
       "cpfrLearnListRowStatus": cpfrLearnListRowStatus,
       "cpfrLearnListReferenceName": cpfrLearnListReferenceName,
       "cpfrLearnListSequenceNum": cpfrLearnListSequenceNum,
       "cpfrLearnListMethod": cpfrLearnListMethod,
       "cpfrLearnListAclName": cpfrLearnListAclName,
       "cpfrLearnListPfxName": cpfrLearnListPfxName,
       "cpfrLearnListPfxInside": cpfrLearnListPfxInside,
       "cpfrLearnListNbarAppl": cpfrLearnListNbarAppl,
       "cpfrLearnListFilterPfxName": cpfrLearnListFilterPfxName,
       "cpfrActiveProbeTable": cpfrActiveProbeTable,
       "cpfrActiveProbeEntry": cpfrActiveProbeEntry,
       "cpfrActiveProbeIndex": cpfrActiveProbeIndex,
       "cpfrActiveProbeStorageType": cpfrActiveProbeStorageType,
       "cpfrActiveProbeRowStatus": cpfrActiveProbeRowStatus,
       "cpfrActiveProbeType": cpfrActiveProbeType,
       "cpfrActiveProbeTargetAddressType": cpfrActiveProbeTargetAddressType,
       "cpfrActiveProbeTargetAddress": cpfrActiveProbeTargetAddress,
       "cpfrActiveProbeTargetPortNumber": cpfrActiveProbeTargetPortNumber,
       "cpfrActiveProbePfrMapIndex": cpfrActiveProbePfrMapIndex,
       "cpfrActiveProbeDscpValue": cpfrActiveProbeDscpValue,
       "cpfrActiveProbeCodecName": cpfrActiveProbeCodecName,
       "cpfrActiveProbeMapIndex": cpfrActiveProbeMapIndex,
       "cpfrActiveProbeMapPolicyIndex": cpfrActiveProbeMapPolicyIndex,
       "cpfrActiveProbeAdminStatus": cpfrActiveProbeAdminStatus,
       "cpfrActiveProbeOperStatus": cpfrActiveProbeOperStatus,
       "cpfrActiveProbeAssignedPfxAddressType": cpfrActiveProbeAssignedPfxAddressType,
       "cpfrActiveProbeAssignedPfxAddress": cpfrActiveProbeAssignedPfxAddress,
       "cpfrActiveProbeAssignedPfxLen": cpfrActiveProbeAssignedPfxLen,
       "cpfrActiveProbeMethod": cpfrActiveProbeMethod,
       "cpfrBRTable": cpfrBRTable,
       "cpfrBREntry": cpfrBREntry,
       "cpfrBRIndex": cpfrBRIndex,
       "cpfrBRStorageType": cpfrBRStorageType,
       "cpfrBRRowStatus": cpfrBRRowStatus,
       "cpfrBRAddressType": cpfrBRAddressType,
       "cpfrBRAddress": cpfrBRAddress,
       "cpfrBRKeyName": cpfrBRKeyName,
       "cpfrBROperStatus": cpfrBROperStatus,
       "cpfrBRConnStatus": cpfrBRConnStatus,
       "cpfrBRUpTime": cpfrBRUpTime,
       "cpfrBRConnFailureReason": cpfrBRConnFailureReason,
       "cpfrBRAuthFailCount": cpfrBRAuthFailCount,
       "cpfrExitTable": cpfrExitTable,
       "cpfrExitEntry": cpfrExitEntry,
       "cpfrExitIndex": cpfrExitIndex,
       "cpfrExitStorageType": cpfrExitStorageType,
       "cpfrExitRowStatus": cpfrExitRowStatus,
       "cpfrExitName": cpfrExitName,
       "cpfrExitType": cpfrExitType,
       "cpfrDowngradeBgpCommunity": cpfrDowngradeBgpCommunity,
       "cpfrExitMaxUtilRxType": cpfrExitMaxUtilRxType,
       "cpfrExitMaxUtilRxAbsolute": cpfrExitMaxUtilRxAbsolute,
       "cpfrExitMaxUtilRxPercentage": cpfrExitMaxUtilRxPercentage,
       "cpfrExitMaxUtilTxType": cpfrExitMaxUtilTxType,
       "cpfrExitMaxUtilTxAbsolute": cpfrExitMaxUtilTxAbsolute,
       "cpfrExitMaxUtilTxPercentage": cpfrExitMaxUtilTxPercentage,
       "cpfrExitCostCalcMethod": cpfrExitCostCalcMethod,
       "cpfrExitCostDiscard": cpfrExitCostDiscard,
       "cpfrExitCostDiscardType": cpfrExitCostDiscardType,
       "cpfrExitCostDiscardAbsolute": cpfrExitCostDiscardAbsolute,
       "cpfrExitCostDiscardPercent": cpfrExitCostDiscardPercent,
       "cpfrExitCostEndDayOfMonth": cpfrExitCostEndDayOfMonth,
       "cpfrExitCostEndOffsetType": cpfrExitCostEndOffsetType,
       "cpfrExitCostEndOffset": cpfrExitCostEndOffset,
       "cpfrExitCostFixedFeeCost": cpfrExitCostFixedFeeCost,
       "cpfrExitCostNickName": cpfrExitCostNickName,
       "cpfrExitCostSamplingPeriod": cpfrExitCostSamplingPeriod,
       "cpfrExitCostRollupPeriod": cpfrExitCostRollupPeriod,
       "cpfrExitCostSummerTimeStart": cpfrExitCostSummerTimeStart,
       "cpfrExitCostSummerTimeOffset": cpfrExitCostSummerTimeOffset,
       "cpfrExitCostSummerTimeEnd": cpfrExitCostSummerTimeEnd,
       "cpfrExitCapacity": cpfrExitCapacity,
       "cpfrExitRxBandwidth": cpfrExitRxBandwidth,
       "cpfrExitTxBandwidth": cpfrExitTxBandwidth,
       "cpfrExitTxLoad": cpfrExitTxLoad,
       "cpfrExitRxLoad": cpfrExitRxLoad,
       "cpfrExitNickName": cpfrExitNickName,
       "cpfrExitCost1": cpfrExitCost1,
       "cpfrExitSustainedUtil1": cpfrExitSustainedUtil1,
       "cpfrExitCost2": cpfrExitCost2,
       "cpfrExitSustainedUtil2": cpfrExitSustainedUtil2,
       "cpfrExitCost3": cpfrExitCost3,
       "cpfrExitSustainedUtil3": cpfrExitSustainedUtil3,
       "cpfrExitRollupTotal": cpfrExitRollupTotal,
       "cpfrExitRollupDiscard": cpfrExitRollupDiscard,
       "cpfrExitRollupLeft": cpfrExitRollupLeft,
       "cpfrExitRollupCollected": cpfrExitRollupCollected,
       "cpfrExitRollupMomTgtUtil": cpfrExitRollupMomTgtUtil,
       "cpfrExitRollupStartingTgtUtil": cpfrExitRollupStartingTgtUtil,
       "cpfrExitRollupCurrentTgtUtil": cpfrExitRollupCurrentTgtUtil,
       "cpfrExitRollupCumRxBytes": cpfrExitRollupCumRxBytes,
       "cpfrExitRollupCumTxBytes": cpfrExitRollupCumTxBytes,
       "cpfrExitRollupTimeRemain": cpfrExitRollupTimeRemain,
       "cpfrExitOperStatus": cpfrExitOperStatus,
       "cpfrExitRsvpBandwidthPool": cpfrExitRsvpBandwidthPool,
       "cpfrExitCostTierTable": cpfrExitCostTierTable,
       "cpfrExitCostTierEntry": cpfrExitCostTierEntry,
       "cpfrExitCostTierIndex": cpfrExitCostTierIndex,
       "cpfrExitCostTierStorageType": cpfrExitCostTierStorageType,
       "cpfrExitCostTierRowStatus": cpfrExitCostTierRowStatus,
       "cpfrExitCostTierFee": cpfrExitCostTierFee,
       "cpfrTrafficClassTable": cpfrTrafficClassTable,
       "cpfrTrafficClassEntry": cpfrTrafficClassEntry,
       "cpfrTrafficClassIndex": cpfrTrafficClassIndex,
       "cpfrTCBRIndex": cpfrTCBRIndex,
       "cpfrTCBRExitIndex": cpfrTCBRExitIndex,
       "cpfrTCMapIndex": cpfrTCMapIndex,
       "cpfrTCMapPolicyIndex": cpfrTCMapPolicyIndex,
       "cpfrTrafficClassValid": cpfrTrafficClassValid,
       "cpfrTCSrcPrefixType": cpfrTCSrcPrefixType,
       "cpfrTCSrcPrefix": cpfrTCSrcPrefix,
       "cpfrTCSrcPrefixLen": cpfrTCSrcPrefixLen,
       "cpfrTCSrcMinPort": cpfrTCSrcMinPort,
       "cpfrTCSrcMaxPort": cpfrTCSrcMaxPort,
       "cpfrTCDstPrefixType": cpfrTCDstPrefixType,
       "cpfrTCDstPrefix": cpfrTCDstPrefix,
       "cpfrTCDstPrefixLen": cpfrTCDstPrefixLen,
       "cpfrTCDstMinPort": cpfrTCDstMinPort,
       "cpfrTCDstMaxPort": cpfrTCDstMaxPort,
       "cpfrTCDscpValue": cpfrTCDscpValue,
       "cpfrTCProtocol": cpfrTCProtocol,
       "cpfrTCNbarApplication": cpfrTCNbarApplication,
       "cpfrTrafficClassStatusTable": cpfrTrafficClassStatusTable,
       "cpfrTrafficClassStatusEntry": cpfrTrafficClassStatusEntry,
       "cpfrTCStatus": cpfrTCStatus,
       "cpfrTCSType": cpfrTCSType,
       "cpfrTCSLearnListIndex": cpfrTCSLearnListIndex,
       "cpfrTCSTimeOnCurrExit": cpfrTCSTimeOnCurrExit,
       "cpfrTCSControlState": cpfrTCSControlState,
       "cpfrTCSControlBy": cpfrTCSControlBy,
       "cpfrTCSTimeRemainCurrState": cpfrTCSTimeRemainCurrState,
       "cpfrTCSLastOOPEventTime": cpfrTCSLastOOPEventTime,
       "cpfrTCSLastOOPReason": cpfrTCSLastOOPReason,
       "cpfrTCSLastRouteChangeEvent": cpfrTCSLastRouteChangeEvent,
       "cpfrTCSLastRouteChangeReason": cpfrTCSLastRouteChangeReason,
       "cpfrTrafficClassMetricTable": cpfrTrafficClassMetricTable,
       "cpfrTrafficClassMetricEntry": cpfrTrafficClassMetricEntry,
       "cpfrTCMLastUpdateTime": cpfrTCMLastUpdateTime,
       "cpfrTCMAge": cpfrTCMAge,
       "cpfrTCMetricsValid": cpfrTCMetricsValid,
       "cpfrTCMActiveSTJitterAvg": cpfrTCMActiveSTJitterAvg,
       "cpfrTCMMOSPercentage": cpfrTCMMOSPercentage,
       "cpfrTCMAttempts": cpfrTCMAttempts,
       "cpfrTCMPackets": cpfrTCMPackets,
       "cpfrTCMPassiveSTUnreachableAvg": cpfrTCMPassiveSTUnreachableAvg,
       "cpfrTCMPassiveSTDelayAvg": cpfrTCMPassiveSTDelayAvg,
       "cpfrTCMPassiveSTLossAvg": cpfrTCMPassiveSTLossAvg,
       "cpfrTCMActiveSTUnreachableAvg": cpfrTCMActiveSTUnreachableAvg,
       "cpfrTCMActiveSTDelayAvg": cpfrTCMActiveSTDelayAvg,
       "cpfrTCMPassiveLTUnreachableAvg": cpfrTCMPassiveLTUnreachableAvg,
       "cpfrTCMPassiveLTDelayAvg": cpfrTCMPassiveLTDelayAvg,
       "cpfrTCMPassiveLTLossAvg": cpfrTCMPassiveLTLossAvg,
       "cpfrTCMActiveLTUnreachableAvg": cpfrTCMActiveLTUnreachableAvg,
       "cpfrTCMActiveLTDelayAvg": cpfrTCMActiveLTDelayAvg,
       "cpfrLinkGroupExitTable": cpfrLinkGroupExitTable,
       "cpfrLinkGroupExitEntry": cpfrLinkGroupExitEntry,
       "cpfrLinkGroupName": cpfrLinkGroupName,
       "cpfrLinkGroupIndex": cpfrLinkGroupIndex,
       "cpfrLinkGroupStorageType": cpfrLinkGroupStorageType,
       "cpfrLinkGroupRowStatus": cpfrLinkGroupRowStatus,
       "cpfrLinkGroupBRIndex": cpfrLinkGroupBRIndex,
       "cpfrLinkGroupExitIndex": cpfrLinkGroupExitIndex,
       "cpfrLinkGroupType": cpfrLinkGroupType,
       "cpfrNbarApplListTable": cpfrNbarApplListTable,
       "cpfrNbarApplListEntry": cpfrNbarApplListEntry,
       "cpfrNbarApplListName": cpfrNbarApplListName,
       "cpfrNbarApplIndex": cpfrNbarApplIndex,
       "cpfrNbarApplListStorageType": cpfrNbarApplListStorageType,
       "cpfrNbarApplListRowStatus": cpfrNbarApplListRowStatus,
       "cpfrNbarApplPdIndex": cpfrNbarApplPdIndex,
       "ciscoPfrMIBConform": ciscoPfrMIBConform,
       "ciscoPfrMIBCompliances": ciscoPfrMIBCompliances,
       "ciscoPfrMIBCompliance": ciscoPfrMIBCompliance,
       "ciscoPfrMIBComplianceRev1": ciscoPfrMIBComplianceRev1,
       "ciscoPfrMIBGroups": ciscoPfrMIBGroups,
       "cpfrMasterControllerGroup": cpfrMasterControllerGroup,
       "cpfrBorderRouterGroup": cpfrBorderRouterGroup,
       "cpfrTrafficClassGroup": cpfrTrafficClassGroup,
       "cpfrMasterControllerGroupRev1": cpfrMasterControllerGroupRev1,
       "cpfrBorderRouterGroupRev1": cpfrBorderRouterGroupRev1,
       "cpfrMCNotificationGroup": cpfrMCNotificationGroup}
)
