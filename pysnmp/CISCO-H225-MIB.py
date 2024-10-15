# SNMP MIB module (CISCO-H225-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-H225-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:06 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoH225MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397)
)
ciscoH225MIB.setRevisions(
        ("2004-11-24 00:00",
         "2004-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CauseCodeType(Integer32, TextualConvention):
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
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
              49,
              50,
              53,
              55,
              57,
              58,
              62,
              63,
              65,
              66,
              69,
              70,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              90,
              91,
              93,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              110,
              111,
              126,
              127,
              128,
              129,
              160,
              170,
              171,
              172,
              180,
              250,
              251,
              256)
        )
    )
    namedValues = NamedValues(
        *(("accessInformationDiscarded", 43),
          ("allParametersNotSupported", 93),
          ("bearerCapabilityNotAuthorized", 57),
          ("bearerCapabilityNotAvailable", 58),
          ("bearerCapabilityNotImplemented", 65),
          ("callAwardedAndDelivered", 7),
          ("callExistsButCallIdentityDoesNot", 83),
          ("callIdentityInUse", 84),
          ("callRejected", 21),
          ("cellRateNotAvailable", 37),
          ("channelTypeNotImplemented", 66),
          ("channelUnacceptable", 6),
          ("codecIncompatible", 171),
          ("destinationOutOfOrder", 27),
          ("dspError", 172),
          ("dtlTransitNotNodeId", 160),
          ("exchangeRoutingError", 25),
          ("facilityRejected", 29),
          ("glare", 15),
          ("glaringSwitchPRI", 180),
          ("htspmOutOfService", 129),
          ("identifiedChannelDoesNotExist", 82),
          ("incomingCallsBarredWithinCUG", 55),
          ("incompatibleDestination", 88),
          ("inconsistencyInOutgoingInfo", 62),
          ("infoElementORNotImplemented", 99),
          ("interworkingUnspecified", 127),
          ("invalidCallReferenceValue", 81),
          ("invalidInfoElementContents", 100),
          ("invalidMessageUnspecified", 95),
          ("invalidNumberORAddressIncomplete", 28),
          ("invalidTransitNetworkSelection", 91),
          ("mandatoryInfoElementMissing", 96),
          ("messageInCompatible", 98),
          ("messageInCompatibleCallState", 101),
          ("messageTypeNotImplemented", 97),
          ("misdialledTrunkPrefix", 5),
          ("networkOutOfOrder", 38),
          ("nextNodeUnreachable", 128),
          ("noAnswerFromUser", 19),
          ("noCallSuspended", 85),
          ("noDSPChannel", 170),
          ("noRequestedCircuitORchannel", 44),
          ("noRouteToDestination", 3),
          ("noRouteToSpecifiedTransitNetwork", 2),
          ("noServiceOROption", 63),
          ("noUserResponding", 18),
          ("noVPCIorVCIAvailable", 45),
          ("noVoiceResource", 126),
          ("nocircuitORchannelAvailable", 34),
          ("nonExistentCUG", 90),
          ("nonImplementedParamPassedon", 103),
          ("nonSelectedUserClearing", 26),
          ("normalCallClearing", 16),
          ("normalUnspecified", 31),
          ("numberChanged", 22),
          ("onlyRestrictedDigitalInfoBC", 70),
          ("outgoingCallsBarredWithinCUG", 53),
          ("permanentFrameModeOperational", 40),
          ("permanentFrameModeOutOfService", 39),
          ("precedenceCallBlocked", 46),
          ("preemption", 8),
          ("preemptionCircuitReserved", 9),
          ("protocolErrorUnspecified", 111),
          ("qualityOfServiceNotAvailable", 49),
          ("recoveryOnTimerExpiry", 102),
          ("redirectionToNewDestination", 23),
          ("requestedCallIdentityCleared", 86),
          ("requestedFacilityNotImplemented", 69),
          ("requestedFacilityNotSubscribed", 50),
          ("requestedVPCIorVCINotAvailable", 35),
          ("resourceUnavailableUnspecified", 47),
          ("responseToSTATUSENQUIRY", 30),
          ("sendSpecialInformationTone", 4),
          ("serviceOROptionNotImplemented", 79),
          ("sipUndefinedMapped", 250),
          ("sipUndefinedUnmapped", 251),
          ("subscriberAbsent", 20),
          ("switchingEquipmentCongestion", 42),
          ("temporaryFailure", 41),
          ("unallocatedNumber", 1),
          ("unknownCauseCodeType", 256),
          ("unrecognizedParamMSGDiscarded", 110),
          ("userBusy", 17),
          ("userNotMemberOfCUG", 87),
          ("vpciORvciAssignmentFailure", 36))
    )



# MIB Managed Objects in the order of their OIDs

_H225MIBObjects_ObjectIdentity = ObjectIdentity
h225MIBObjects = _H225MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1)
)
_H225CallSignal_ObjectIdentity = ObjectIdentity
h225CallSignal = _H225CallSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1)
)
_H225CallSignalStats_ObjectIdentity = ObjectIdentity
h225CallSignalStats = _H225CallSignalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1)
)
_H225CallSignalStatsSetupIns_Type = Counter32
_H225CallSignalStatsSetupIns_Object = MibScalar
h225CallSignalStatsSetupIns = _H225CallSignalStatsSetupIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 1),
    _H225CallSignalStatsSetupIns_Type()
)
h225CallSignalStatsSetupIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupIns.setStatus("current")
_H225CallSignalStatsSetupOuts_Type = Counter32
_H225CallSignalStatsSetupOuts_Object = MibScalar
h225CallSignalStatsSetupOuts = _H225CallSignalStatsSetupOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 2),
    _H225CallSignalStatsSetupOuts_Type()
)
h225CallSignalStatsSetupOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupOuts.setStatus("current")
_H225CallSignalStatsSetupFails_Type = Counter32
_H225CallSignalStatsSetupFails_Object = MibScalar
h225CallSignalStatsSetupFails = _H225CallSignalStatsSetupFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 3),
    _H225CallSignalStatsSetupFails_Type()
)
h225CallSignalStatsSetupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupFails.setStatus("current")
_H225CallSignalStatsSetupConfIns_Type = Counter32
_H225CallSignalStatsSetupConfIns_Object = MibScalar
h225CallSignalStatsSetupConfIns = _H225CallSignalStatsSetupConfIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 4),
    _H225CallSignalStatsSetupConfIns_Type()
)
h225CallSignalStatsSetupConfIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupConfIns.setStatus("current")
_H225CallSignalStatsSetupConfOuts_Type = Counter32
_H225CallSignalStatsSetupConfOuts_Object = MibScalar
h225CallSignalStatsSetupConfOuts = _H225CallSignalStatsSetupConfOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 5),
    _H225CallSignalStatsSetupConfOuts_Type()
)
h225CallSignalStatsSetupConfOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupConfOuts.setStatus("current")
_H225CallSignalStatsSetupConFails_Type = Counter32
_H225CallSignalStatsSetupConFails_Object = MibScalar
h225CallSignalStatsSetupConFails = _H225CallSignalStatsSetupConFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 6),
    _H225CallSignalStatsSetupConFails_Type()
)
h225CallSignalStatsSetupConFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsSetupConFails.setStatus("current")
_H225CallSignalStatsAlertingIns_Type = Counter32
_H225CallSignalStatsAlertingIns_Object = MibScalar
h225CallSignalStatsAlertingIns = _H225CallSignalStatsAlertingIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 7),
    _H225CallSignalStatsAlertingIns_Type()
)
h225CallSignalStatsAlertingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsAlertingIns.setStatus("current")
_H225CallSignalStatsAlertingOuts_Type = Counter32
_H225CallSignalStatsAlertingOuts_Object = MibScalar
h225CallSignalStatsAlertingOuts = _H225CallSignalStatsAlertingOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 8),
    _H225CallSignalStatsAlertingOuts_Type()
)
h225CallSignalStatsAlertingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsAlertingOuts.setStatus("current")
_H225CallSignalStatsAlertingFails_Type = Counter32
_H225CallSignalStatsAlertingFails_Object = MibScalar
h225CallSignalStatsAlertingFails = _H225CallSignalStatsAlertingFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 9),
    _H225CallSignalStatsAlertingFails_Type()
)
h225CallSignalStatsAlertingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsAlertingFails.setStatus("current")
_H225CallSignalStatsProgIns_Type = Counter32
_H225CallSignalStatsProgIns_Object = MibScalar
h225CallSignalStatsProgIns = _H225CallSignalStatsProgIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 10),
    _H225CallSignalStatsProgIns_Type()
)
h225CallSignalStatsProgIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsProgIns.setStatus("current")
_H225CallSignalStatsProgOuts_Type = Counter32
_H225CallSignalStatsProgOuts_Object = MibScalar
h225CallSignalStatsProgOuts = _H225CallSignalStatsProgOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 11),
    _H225CallSignalStatsProgOuts_Type()
)
h225CallSignalStatsProgOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsProgOuts.setStatus("current")
_H225CallSignalStatsProgFails_Type = Counter32
_H225CallSignalStatsProgFails_Object = MibScalar
h225CallSignalStatsProgFails = _H225CallSignalStatsProgFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 12),
    _H225CallSignalStatsProgFails_Type()
)
h225CallSignalStatsProgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsProgFails.setStatus("current")
_H225CallSignalStatsCallProcsIns_Type = Counter32
_H225CallSignalStatsCallProcsIns_Object = MibScalar
h225CallSignalStatsCallProcsIns = _H225CallSignalStatsCallProcsIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 13),
    _H225CallSignalStatsCallProcsIns_Type()
)
h225CallSignalStatsCallProcsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsCallProcsIns.setStatus("current")
_H225CallSignalStatsCallProcsOuts_Type = Counter32
_H225CallSignalStatsCallProcsOuts_Object = MibScalar
h225CallSignalStatsCallProcsOuts = _H225CallSignalStatsCallProcsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 14),
    _H225CallSignalStatsCallProcsOuts_Type()
)
h225CallSignalStatsCallProcsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsCallProcsOuts.setStatus("current")
_H225CallSignalStatsCallProcFails_Type = Counter32
_H225CallSignalStatsCallProcFails_Object = MibScalar
h225CallSignalStatsCallProcFails = _H225CallSignalStatsCallProcFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 15),
    _H225CallSignalStatsCallProcFails_Type()
)
h225CallSignalStatsCallProcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsCallProcFails.setStatus("current")
_H225CallSignalStatsNotifyIns_Type = Counter32
_H225CallSignalStatsNotifyIns_Object = MibScalar
h225CallSignalStatsNotifyIns = _H225CallSignalStatsNotifyIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 16),
    _H225CallSignalStatsNotifyIns_Type()
)
h225CallSignalStatsNotifyIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsNotifyIns.setStatus("current")
_H225CallSignalStatsNotifyOuts_Type = Counter32
_H225CallSignalStatsNotifyOuts_Object = MibScalar
h225CallSignalStatsNotifyOuts = _H225CallSignalStatsNotifyOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 17),
    _H225CallSignalStatsNotifyOuts_Type()
)
h225CallSignalStatsNotifyOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsNotifyOuts.setStatus("current")
_H225CallSignalStatsNotifyFails_Type = Counter32
_H225CallSignalStatsNotifyFails_Object = MibScalar
h225CallSignalStatsNotifyFails = _H225CallSignalStatsNotifyFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 18),
    _H225CallSignalStatsNotifyFails_Type()
)
h225CallSignalStatsNotifyFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsNotifyFails.setStatus("current")
_H225CallSignalStatsInfoIns_Type = Counter32
_H225CallSignalStatsInfoIns_Object = MibScalar
h225CallSignalStatsInfoIns = _H225CallSignalStatsInfoIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 19),
    _H225CallSignalStatsInfoIns_Type()
)
h225CallSignalStatsInfoIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsInfoIns.setStatus("current")
_H225CallSignalStatsInfoOuts_Type = Counter32
_H225CallSignalStatsInfoOuts_Object = MibScalar
h225CallSignalStatsInfoOuts = _H225CallSignalStatsInfoOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 20),
    _H225CallSignalStatsInfoOuts_Type()
)
h225CallSignalStatsInfoOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsInfoOuts.setStatus("current")
_H225CallSignalStatsInfoFails_Type = Counter32
_H225CallSignalStatsInfoFails_Object = MibScalar
h225CallSignalStatsInfoFails = _H225CallSignalStatsInfoFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 21),
    _H225CallSignalStatsInfoFails_Type()
)
h225CallSignalStatsInfoFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsInfoFails.setStatus("current")
_H225CallSignalStatsUserInfoIns_Type = Counter32
_H225CallSignalStatsUserInfoIns_Object = MibScalar
h225CallSignalStatsUserInfoIns = _H225CallSignalStatsUserInfoIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 22),
    _H225CallSignalStatsUserInfoIns_Type()
)
h225CallSignalStatsUserInfoIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsUserInfoIns.setStatus("current")
_H225CallSignalStatsUserInfoOuts_Type = Counter32
_H225CallSignalStatsUserInfoOuts_Object = MibScalar
h225CallSignalStatsUserInfoOuts = _H225CallSignalStatsUserInfoOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 23),
    _H225CallSignalStatsUserInfoOuts_Type()
)
h225CallSignalStatsUserInfoOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsUserInfoOuts.setStatus("current")
_H225CallSignalStatsUserInfoFails_Type = Counter32
_H225CallSignalStatsUserInfoFails_Object = MibScalar
h225CallSignalStatsUserInfoFails = _H225CallSignalStatsUserInfoFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 24),
    _H225CallSignalStatsUserInfoFails_Type()
)
h225CallSignalStatsUserInfoFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsUserInfoFails.setStatus("current")
_H225CallSignalStatsFacilityIns_Type = Counter32
_H225CallSignalStatsFacilityIns_Object = MibScalar
h225CallSignalStatsFacilityIns = _H225CallSignalStatsFacilityIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 25),
    _H225CallSignalStatsFacilityIns_Type()
)
h225CallSignalStatsFacilityIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsFacilityIns.setStatus("current")
_H225CallSignalStatsFacilityOuts_Type = Counter32
_H225CallSignalStatsFacilityOuts_Object = MibScalar
h225CallSignalStatsFacilityOuts = _H225CallSignalStatsFacilityOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 26),
    _H225CallSignalStatsFacilityOuts_Type()
)
h225CallSignalStatsFacilityOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsFacilityOuts.setStatus("current")
_H225CallSignalStatsFacilityFails_Type = Counter32
_H225CallSignalStatsFacilityFails_Object = MibScalar
h225CallSignalStatsFacilityFails = _H225CallSignalStatsFacilityFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 27),
    _H225CallSignalStatsFacilityFails_Type()
)
h225CallSignalStatsFacilityFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsFacilityFails.setStatus("current")
_H225CallSignalStatsReleaseIns_Type = Counter32
_H225CallSignalStatsReleaseIns_Object = MibScalar
h225CallSignalStatsReleaseIns = _H225CallSignalStatsReleaseIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 28),
    _H225CallSignalStatsReleaseIns_Type()
)
h225CallSignalStatsReleaseIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsReleaseIns.setStatus("current")
_H225CallSignalStatsReleaseOuts_Type = Counter32
_H225CallSignalStatsReleaseOuts_Object = MibScalar
h225CallSignalStatsReleaseOuts = _H225CallSignalStatsReleaseOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 29),
    _H225CallSignalStatsReleaseOuts_Type()
)
h225CallSignalStatsReleaseOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsReleaseOuts.setStatus("current")
_H225CallSignalStatsReleaseFails_Type = Counter32
_H225CallSignalStatsReleaseFails_Object = MibScalar
h225CallSignalStatsReleaseFails = _H225CallSignalStatsReleaseFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 30),
    _H225CallSignalStatsReleaseFails_Type()
)
h225CallSignalStatsReleaseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsReleaseFails.setStatus("current")
_H225CallSignalStatsRejectIns_Type = Counter32
_H225CallSignalStatsRejectIns_Object = MibScalar
h225CallSignalStatsRejectIns = _H225CallSignalStatsRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 31),
    _H225CallSignalStatsRejectIns_Type()
)
h225CallSignalStatsRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsRejectIns.setStatus("current")
_H225CallSignalStatsRejectOuts_Type = Counter32
_H225CallSignalStatsRejectOuts_Object = MibScalar
h225CallSignalStatsRejectOuts = _H225CallSignalStatsRejectOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 32),
    _H225CallSignalStatsRejectOuts_Type()
)
h225CallSignalStatsRejectOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsRejectOuts.setStatus("current")
_H225CallSignalStatsRejectFails_Type = Counter32
_H225CallSignalStatsRejectFails_Object = MibScalar
h225CallSignalStatsRejectFails = _H225CallSignalStatsRejectFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 33),
    _H225CallSignalStatsRejectFails_Type()
)
h225CallSignalStatsRejectFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsRejectFails.setStatus("current")
_H225CallSignalStatsPassthroIns_Type = Counter32
_H225CallSignalStatsPassthroIns_Object = MibScalar
h225CallSignalStatsPassthroIns = _H225CallSignalStatsPassthroIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 34),
    _H225CallSignalStatsPassthroIns_Type()
)
h225CallSignalStatsPassthroIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsPassthroIns.setStatus("current")
_H225CallSignalStatsPassthroOuts_Type = Counter32
_H225CallSignalStatsPassthroOuts_Object = MibScalar
h225CallSignalStatsPassthroOuts = _H225CallSignalStatsPassthroOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 35),
    _H225CallSignalStatsPassthroOuts_Type()
)
h225CallSignalStatsPassthroOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsPassthroOuts.setStatus("current")
_H225CallSignalStatsPassthroFails_Type = Counter32
_H225CallSignalStatsPassthroFails_Object = MibScalar
h225CallSignalStatsPassthroFails = _H225CallSignalStatsPassthroFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 1, 1, 36),
    _H225CallSignalStatsPassthroFails_Type()
)
h225CallSignalStatsPassthroFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CallSignalStatsPassthroFails.setStatus("current")
_H225Ras_ObjectIdentity = ObjectIdentity
h225Ras = _H225Ras_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2)
)
_H225RasStats_ObjectIdentity = ObjectIdentity
h225RasStats = _H225RasStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1)
)
_H225RasStatsGkDiscoveryReqIns_Type = Counter32
_H225RasStatsGkDiscoveryReqIns_Object = MibScalar
h225RasStatsGkDiscoveryReqIns = _H225RasStatsGkDiscoveryReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 1),
    _H225RasStatsGkDiscoveryReqIns_Type()
)
h225RasStatsGkDiscoveryReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryReqIns.setStatus("current")
_H225RasStatsGkDiscoveryReqOuts_Type = Counter32
_H225RasStatsGkDiscoveryReqOuts_Object = MibScalar
h225RasStatsGkDiscoveryReqOuts = _H225RasStatsGkDiscoveryReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 2),
    _H225RasStatsGkDiscoveryReqOuts_Type()
)
h225RasStatsGkDiscoveryReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryReqOuts.setStatus("current")
_H225RasStatsGkDiscoveryConfIns_Type = Counter32
_H225RasStatsGkDiscoveryConfIns_Object = MibScalar
h225RasStatsGkDiscoveryConfIns = _H225RasStatsGkDiscoveryConfIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 3),
    _H225RasStatsGkDiscoveryConfIns_Type()
)
h225RasStatsGkDiscoveryConfIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryConfIns.setStatus("current")
_H225RasStatsGkDiscoveryConfOuts_Type = Counter32
_H225RasStatsGkDiscoveryConfOuts_Object = MibScalar
h225RasStatsGkDiscoveryConfOuts = _H225RasStatsGkDiscoveryConfOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 4),
    _H225RasStatsGkDiscoveryConfOuts_Type()
)
h225RasStatsGkDiscoveryConfOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryConfOuts.setStatus("current")
_H225RasStatsGkDiscoveryRejectIns_Type = Counter32
_H225RasStatsGkDiscoveryRejectIns_Object = MibScalar
h225RasStatsGkDiscoveryRejectIns = _H225RasStatsGkDiscoveryRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 5),
    _H225RasStatsGkDiscoveryRejectIns_Type()
)
h225RasStatsGkDiscoveryRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryRejectIns.setStatus("current")
_H225RasStatsGkDiscoveryRejOuts_Type = Counter32
_H225RasStatsGkDiscoveryRejOuts_Object = MibScalar
h225RasStatsGkDiscoveryRejOuts = _H225RasStatsGkDiscoveryRejOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 6),
    _H225RasStatsGkDiscoveryRejOuts_Type()
)
h225RasStatsGkDiscoveryRejOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsGkDiscoveryRejOuts.setStatus("current")
_H225RasStatsRegistrationReqIns_Type = Counter32
_H225RasStatsRegistrationReqIns_Object = MibScalar
h225RasStatsRegistrationReqIns = _H225RasStatsRegistrationReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 7),
    _H225RasStatsRegistrationReqIns_Type()
)
h225RasStatsRegistrationReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationReqIns.setStatus("current")
_H225RasStatsRegistrationReqOuts_Type = Counter32
_H225RasStatsRegistrationReqOuts_Object = MibScalar
h225RasStatsRegistrationReqOuts = _H225RasStatsRegistrationReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 8),
    _H225RasStatsRegistrationReqOuts_Type()
)
h225RasStatsRegistrationReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationReqOuts.setStatus("current")
_H225RasStatsRegistrationConfIns_Type = Counter32
_H225RasStatsRegistrationConfIns_Object = MibScalar
h225RasStatsRegistrationConfIns = _H225RasStatsRegistrationConfIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 9),
    _H225RasStatsRegistrationConfIns_Type()
)
h225RasStatsRegistrationConfIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationConfIns.setStatus("current")
_H225RasStatsRegistrationConfOuts_Type = Counter32
_H225RasStatsRegistrationConfOuts_Object = MibScalar
h225RasStatsRegistrationConfOuts = _H225RasStatsRegistrationConfOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 10),
    _H225RasStatsRegistrationConfOuts_Type()
)
h225RasStatsRegistrationConfOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationConfOuts.setStatus("current")
_H225RasStatsRegistrationRejIns_Type = Counter32
_H225RasStatsRegistrationRejIns_Object = MibScalar
h225RasStatsRegistrationRejIns = _H225RasStatsRegistrationRejIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 11),
    _H225RasStatsRegistrationRejIns_Type()
)
h225RasStatsRegistrationRejIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationRejIns.setStatus("current")
_H225RasStatsRegistrationRejOuts_Type = Counter32
_H225RasStatsRegistrationRejOuts_Object = MibScalar
h225RasStatsRegistrationRejOuts = _H225RasStatsRegistrationRejOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 12),
    _H225RasStatsRegistrationRejOuts_Type()
)
h225RasStatsRegistrationRejOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRegistrationRejOuts.setStatus("current")
_H225RasStatsAdmissionReqIns_Type = Counter32
_H225RasStatsAdmissionReqIns_Object = MibScalar
h225RasStatsAdmissionReqIns = _H225RasStatsAdmissionReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 13),
    _H225RasStatsAdmissionReqIns_Type()
)
h225RasStatsAdmissionReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionReqIns.setStatus("current")
_H225RasStatsAdmissionReqOuts_Type = Counter32
_H225RasStatsAdmissionReqOuts_Object = MibScalar
h225RasStatsAdmissionReqOuts = _H225RasStatsAdmissionReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 14),
    _H225RasStatsAdmissionReqOuts_Type()
)
h225RasStatsAdmissionReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionReqOuts.setStatus("current")
_H225RasStatsAdmissionConfirmIns_Type = Counter32
_H225RasStatsAdmissionConfirmIns_Object = MibScalar
h225RasStatsAdmissionConfirmIns = _H225RasStatsAdmissionConfirmIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 15),
    _H225RasStatsAdmissionConfirmIns_Type()
)
h225RasStatsAdmissionConfirmIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionConfirmIns.setStatus("current")
_H225RasStatsAdmissionConfirmOuts_Type = Counter32
_H225RasStatsAdmissionConfirmOuts_Object = MibScalar
h225RasStatsAdmissionConfirmOuts = _H225RasStatsAdmissionConfirmOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 16),
    _H225RasStatsAdmissionConfirmOuts_Type()
)
h225RasStatsAdmissionConfirmOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionConfirmOuts.setStatus("current")
_H225RasStatsAdmissionRejectIns_Type = Counter32
_H225RasStatsAdmissionRejectIns_Object = MibScalar
h225RasStatsAdmissionRejectIns = _H225RasStatsAdmissionRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 17),
    _H225RasStatsAdmissionRejectIns_Type()
)
h225RasStatsAdmissionRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionRejectIns.setStatus("current")
_H225RasStatsAdmissionRejectOuts_Type = Counter32
_H225RasStatsAdmissionRejectOuts_Object = MibScalar
h225RasStatsAdmissionRejectOuts = _H225RasStatsAdmissionRejectOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 18),
    _H225RasStatsAdmissionRejectOuts_Type()
)
h225RasStatsAdmissionRejectOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsAdmissionRejectOuts.setStatus("current")
_H225RasStatsBandwidthReqIns_Type = Counter32
_H225RasStatsBandwidthReqIns_Object = MibScalar
h225RasStatsBandwidthReqIns = _H225RasStatsBandwidthReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 19),
    _H225RasStatsBandwidthReqIns_Type()
)
h225RasStatsBandwidthReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthReqIns.setStatus("current")
_H225RasStatsBandwidthReqOuts_Type = Counter32
_H225RasStatsBandwidthReqOuts_Object = MibScalar
h225RasStatsBandwidthReqOuts = _H225RasStatsBandwidthReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 20),
    _H225RasStatsBandwidthReqOuts_Type()
)
h225RasStatsBandwidthReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthReqOuts.setStatus("current")
_H225RasStatsBandwidthConfirmIns_Type = Counter32
_H225RasStatsBandwidthConfirmIns_Object = MibScalar
h225RasStatsBandwidthConfirmIns = _H225RasStatsBandwidthConfirmIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 21),
    _H225RasStatsBandwidthConfirmIns_Type()
)
h225RasStatsBandwidthConfirmIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthConfirmIns.setStatus("current")
_H225RasStatsBandwidthConfirmOuts_Type = Counter32
_H225RasStatsBandwidthConfirmOuts_Object = MibScalar
h225RasStatsBandwidthConfirmOuts = _H225RasStatsBandwidthConfirmOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 22),
    _H225RasStatsBandwidthConfirmOuts_Type()
)
h225RasStatsBandwidthConfirmOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthConfirmOuts.setStatus("current")
_H225RasStatsBandwidthRejectIns_Type = Counter32
_H225RasStatsBandwidthRejectIns_Object = MibScalar
h225RasStatsBandwidthRejectIns = _H225RasStatsBandwidthRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 23),
    _H225RasStatsBandwidthRejectIns_Type()
)
h225RasStatsBandwidthRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthRejectIns.setStatus("current")
_H225RasStatsBandwidthRejectOuts_Type = Counter32
_H225RasStatsBandwidthRejectOuts_Object = MibScalar
h225RasStatsBandwidthRejectOuts = _H225RasStatsBandwidthRejectOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 24),
    _H225RasStatsBandwidthRejectOuts_Type()
)
h225RasStatsBandwidthRejectOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsBandwidthRejectOuts.setStatus("current")
_H225RasStatsDisengageReqIns_Type = Counter32
_H225RasStatsDisengageReqIns_Object = MibScalar
h225RasStatsDisengageReqIns = _H225RasStatsDisengageReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 25),
    _H225RasStatsDisengageReqIns_Type()
)
h225RasStatsDisengageReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageReqIns.setStatus("current")
_H225RasStatsDisengageReqOuts_Type = Counter32
_H225RasStatsDisengageReqOuts_Object = MibScalar
h225RasStatsDisengageReqOuts = _H225RasStatsDisengageReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 26),
    _H225RasStatsDisengageReqOuts_Type()
)
h225RasStatsDisengageReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageReqOuts.setStatus("current")
_H225RasStatsDisengageConfirmIns_Type = Counter32
_H225RasStatsDisengageConfirmIns_Object = MibScalar
h225RasStatsDisengageConfirmIns = _H225RasStatsDisengageConfirmIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 27),
    _H225RasStatsDisengageConfirmIns_Type()
)
h225RasStatsDisengageConfirmIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageConfirmIns.setStatus("current")
_H225RasStatsDisengageConfirmOuts_Type = Counter32
_H225RasStatsDisengageConfirmOuts_Object = MibScalar
h225RasStatsDisengageConfirmOuts = _H225RasStatsDisengageConfirmOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 28),
    _H225RasStatsDisengageConfirmOuts_Type()
)
h225RasStatsDisengageConfirmOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageConfirmOuts.setStatus("current")
_H225RasStatsDisengageRejectIns_Type = Counter32
_H225RasStatsDisengageRejectIns_Object = MibScalar
h225RasStatsDisengageRejectIns = _H225RasStatsDisengageRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 29),
    _H225RasStatsDisengageRejectIns_Type()
)
h225RasStatsDisengageRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageRejectIns.setStatus("current")
_H225RasStatsDisengageRejectOuts_Type = Counter32
_H225RasStatsDisengageRejectOuts_Object = MibScalar
h225RasStatsDisengageRejectOuts = _H225RasStatsDisengageRejectOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 30),
    _H225RasStatsDisengageRejectOuts_Type()
)
h225RasStatsDisengageRejectOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsDisengageRejectOuts.setStatus("current")
_H225RasStatsUnregisterReqIns_Type = Counter32
_H225RasStatsUnregisterReqIns_Object = MibScalar
h225RasStatsUnregisterReqIns = _H225RasStatsUnregisterReqIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 31),
    _H225RasStatsUnregisterReqIns_Type()
)
h225RasStatsUnregisterReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterReqIns.setStatus("current")
_H225RasStatsUnregisterReqOuts_Type = Counter32
_H225RasStatsUnregisterReqOuts_Object = MibScalar
h225RasStatsUnregisterReqOuts = _H225RasStatsUnregisterReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 32),
    _H225RasStatsUnregisterReqOuts_Type()
)
h225RasStatsUnregisterReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterReqOuts.setStatus("current")
_H225RasStatsUnregisterConfirmIns_Type = Counter32
_H225RasStatsUnregisterConfirmIns_Object = MibScalar
h225RasStatsUnregisterConfirmIns = _H225RasStatsUnregisterConfirmIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 33),
    _H225RasStatsUnregisterConfirmIns_Type()
)
h225RasStatsUnregisterConfirmIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterConfirmIns.setStatus("current")
_H225RasStatsUnregisterConfOuts_Type = Counter32
_H225RasStatsUnregisterConfOuts_Object = MibScalar
h225RasStatsUnregisterConfOuts = _H225RasStatsUnregisterConfOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 34),
    _H225RasStatsUnregisterConfOuts_Type()
)
h225RasStatsUnregisterConfOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterConfOuts.setStatus("current")
_H225RasStatsUnregisterRejectIns_Type = Counter32
_H225RasStatsUnregisterRejectIns_Object = MibScalar
h225RasStatsUnregisterRejectIns = _H225RasStatsUnregisterRejectIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 35),
    _H225RasStatsUnregisterRejectIns_Type()
)
h225RasStatsUnregisterRejectIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterRejectIns.setStatus("current")
_H225RasStatsUnregisterRejectOuts_Type = Counter32
_H225RasStatsUnregisterRejectOuts_Object = MibScalar
h225RasStatsUnregisterRejectOuts = _H225RasStatsUnregisterRejectOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 36),
    _H225RasStatsUnregisterRejectOuts_Type()
)
h225RasStatsUnregisterRejectOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsUnregisterRejectOuts.setStatus("current")
_H225RasStatsResourceAvailIndIns_Type = Counter32
_H225RasStatsResourceAvailIndIns_Object = MibScalar
h225RasStatsResourceAvailIndIns = _H225RasStatsResourceAvailIndIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 37),
    _H225RasStatsResourceAvailIndIns_Type()
)
h225RasStatsResourceAvailIndIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsResourceAvailIndIns.setStatus("current")
_H225RasStatsResourceAvailIndOuts_Type = Counter32
_H225RasStatsResourceAvailIndOuts_Object = MibScalar
h225RasStatsResourceAvailIndOuts = _H225RasStatsResourceAvailIndOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 38),
    _H225RasStatsResourceAvailIndOuts_Type()
)
h225RasStatsResourceAvailIndOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsResourceAvailIndOuts.setStatus("current")
_H225RasStatsResourceAvailConfIns_Type = Counter32
_H225RasStatsResourceAvailConfIns_Object = MibScalar
h225RasStatsResourceAvailConfIns = _H225RasStatsResourceAvailConfIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 39),
    _H225RasStatsResourceAvailConfIns_Type()
)
h225RasStatsResourceAvailConfIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsResourceAvailConfIns.setStatus("current")
_H225RasStatsResourceAvailConOuts_Type = Counter32
_H225RasStatsResourceAvailConOuts_Object = MibScalar
h225RasStatsResourceAvailConOuts = _H225RasStatsResourceAvailConOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 40),
    _H225RasStatsResourceAvailConOuts_Type()
)
h225RasStatsResourceAvailConOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsResourceAvailConOuts.setStatus("current")
_H225RasStatsRequestInProgIns_Type = Counter32
_H225RasStatsRequestInProgIns_Object = MibScalar
h225RasStatsRequestInProgIns = _H225RasStatsRequestInProgIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 41),
    _H225RasStatsRequestInProgIns_Type()
)
h225RasStatsRequestInProgIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRequestInProgIns.setStatus("current")
_H225RasStatsRequestInProgOuts_Type = Counter32
_H225RasStatsRequestInProgOuts_Object = MibScalar
h225RasStatsRequestInProgOuts = _H225RasStatsRequestInProgOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 2, 1, 42),
    _H225RasStatsRequestInProgOuts_Type()
)
h225RasStatsRequestInProgOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225RasStatsRequestInProgOuts.setStatus("current")
_H225MIBConformance_ObjectIdentity = ObjectIdentity
h225MIBConformance = _H225MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3)
)
_H225MIBCompliances_ObjectIdentity = ObjectIdentity
h225MIBCompliances = _H225MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 1)
)
_H225MIBGroups_ObjectIdentity = ObjectIdentity
h225MIBGroups = _H225MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 2)
)
_H225DisconnectCauseCode_ObjectIdentity = ObjectIdentity
h225DisconnectCauseCode = _H225DisconnectCauseCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4)
)
_H225DisconnectCauseCodeTable_Object = MibTable
h225DisconnectCauseCodeTable = _H225DisconnectCauseCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h225DisconnectCauseCodeTable.setStatus("current")
_H225DisconnectCauseCodeEntry_Object = MibTableRow
h225DisconnectCauseCodeEntry = _H225DisconnectCauseCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1, 1)
)
h225DisconnectCauseCodeEntry.setIndexNames(
    (0, "CISCO-H225-MIB", "h225CauseCode"),
)
if mibBuilder.loadTexts:
    h225DisconnectCauseCodeEntry.setStatus("current")
_H225CauseCode_Type = CauseCodeType
_H225CauseCode_Object = MibTableColumn
h225CauseCode = _H225CauseCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1, 1, 1),
    _H225CauseCode_Type()
)
h225CauseCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h225CauseCode.setStatus("current")
_H225CauseCodeDescription_Type = DisplayString
_H225CauseCodeDescription_Object = MibTableColumn
h225CauseCodeDescription = _H225CauseCodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1, 1, 2),
    _H225CauseCodeDescription_Type()
)
h225CauseCodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225CauseCodeDescription.setStatus("current")
_H225FromOtherPeerDisconnects_Type = Counter32
_H225FromOtherPeerDisconnects_Object = MibTableColumn
h225FromOtherPeerDisconnects = _H225FromOtherPeerDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1, 1, 3),
    _H225FromOtherPeerDisconnects_Type()
)
h225FromOtherPeerDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225FromOtherPeerDisconnects.setStatus("current")
_H225FromH323PeerDisconnects_Type = Counter32
_H225FromH323PeerDisconnects_Object = MibTableColumn
h225FromH323PeerDisconnects = _H225FromH323PeerDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 4, 1, 1, 4),
    _H225FromH323PeerDisconnects_Type()
)
h225FromH323PeerDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h225FromH323PeerDisconnects.setStatus("current")

# Managed Objects groups

h225CallSignalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 2, 1)
)
h225CallSignalStatsGroup.setObjects(
      *(("CISCO-H225-MIB", "h225CallSignalStatsSetupIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsSetupOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsSetupFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsSetupConfIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsSetupConfOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsSetupConFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsAlertingIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsAlertingOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsAlertingFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsProgIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsProgOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsProgFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsCallProcsIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsCallProcsOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsCallProcFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsNotifyIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsNotifyOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsNotifyFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsInfoIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsInfoOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsInfoFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsUserInfoIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsUserInfoOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsUserInfoFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsFacilityIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsFacilityOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsFacilityFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsReleaseIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsReleaseOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsReleaseFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsRejectIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsRejectOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsRejectFails"),
        ("CISCO-H225-MIB", "h225CallSignalStatsPassthroIns"),
        ("CISCO-H225-MIB", "h225CallSignalStatsPassthroOuts"),
        ("CISCO-H225-MIB", "h225CallSignalStatsPassthroFails"))
)
if mibBuilder.loadTexts:
    h225CallSignalStatsGroup.setStatus("current")

h225RasStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 2, 2)
)
h225RasStatsGroup.setObjects(
      *(("CISCO-H225-MIB", "h225RasStatsGkDiscoveryReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsGkDiscoveryReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsGkDiscoveryConfIns"),
        ("CISCO-H225-MIB", "h225RasStatsGkDiscoveryConfOuts"),
        ("CISCO-H225-MIB", "h225RasStatsGkDiscoveryRejectIns"),
        ("CISCO-H225-MIB", "h225RasStatsGkDiscoveryRejOuts"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationConfIns"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationConfOuts"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationRejIns"),
        ("CISCO-H225-MIB", "h225RasStatsRegistrationRejOuts"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionConfirmIns"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionConfirmOuts"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionRejectIns"),
        ("CISCO-H225-MIB", "h225RasStatsAdmissionRejectOuts"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthConfirmIns"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthConfirmOuts"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthRejectIns"),
        ("CISCO-H225-MIB", "h225RasStatsBandwidthRejectOuts"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageConfirmIns"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageConfirmOuts"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageRejectIns"),
        ("CISCO-H225-MIB", "h225RasStatsDisengageRejectOuts"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterReqIns"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterReqOuts"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterConfirmIns"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterConfOuts"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterRejectIns"),
        ("CISCO-H225-MIB", "h225RasStatsUnregisterRejectOuts"),
        ("CISCO-H225-MIB", "h225RasStatsResourceAvailIndIns"),
        ("CISCO-H225-MIB", "h225RasStatsResourceAvailIndOuts"),
        ("CISCO-H225-MIB", "h225RasStatsResourceAvailConfIns"),
        ("CISCO-H225-MIB", "h225RasStatsResourceAvailConOuts"),
        ("CISCO-H225-MIB", "h225RasStatsRequestInProgIns"),
        ("CISCO-H225-MIB", "h225RasStatsRequestInProgOuts"))
)
if mibBuilder.loadTexts:
    h225RasStatsGroup.setStatus("current")

h225DisconnectCauseCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 2, 3)
)
h225DisconnectCauseCodeGroup.setObjects(
      *(("CISCO-H225-MIB", "h225CauseCodeDescription"),
        ("CISCO-H225-MIB", "h225FromOtherPeerDisconnects"),
        ("CISCO-H225-MIB", "h225FromH323PeerDisconnects"))
)
if mibBuilder.loadTexts:
    h225DisconnectCauseCodeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h225MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h225MIBCompliance.setStatus(
        "deprecated"
    )

h225MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 397, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    h225MIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-H225-MIB",
    **{"CauseCodeType": CauseCodeType,
       "ciscoH225MIB": ciscoH225MIB,
       "h225MIBObjects": h225MIBObjects,
       "h225CallSignal": h225CallSignal,
       "h225CallSignalStats": h225CallSignalStats,
       "h225CallSignalStatsSetupIns": h225CallSignalStatsSetupIns,
       "h225CallSignalStatsSetupOuts": h225CallSignalStatsSetupOuts,
       "h225CallSignalStatsSetupFails": h225CallSignalStatsSetupFails,
       "h225CallSignalStatsSetupConfIns": h225CallSignalStatsSetupConfIns,
       "h225CallSignalStatsSetupConfOuts": h225CallSignalStatsSetupConfOuts,
       "h225CallSignalStatsSetupConFails": h225CallSignalStatsSetupConFails,
       "h225CallSignalStatsAlertingIns": h225CallSignalStatsAlertingIns,
       "h225CallSignalStatsAlertingOuts": h225CallSignalStatsAlertingOuts,
       "h225CallSignalStatsAlertingFails": h225CallSignalStatsAlertingFails,
       "h225CallSignalStatsProgIns": h225CallSignalStatsProgIns,
       "h225CallSignalStatsProgOuts": h225CallSignalStatsProgOuts,
       "h225CallSignalStatsProgFails": h225CallSignalStatsProgFails,
       "h225CallSignalStatsCallProcsIns": h225CallSignalStatsCallProcsIns,
       "h225CallSignalStatsCallProcsOuts": h225CallSignalStatsCallProcsOuts,
       "h225CallSignalStatsCallProcFails": h225CallSignalStatsCallProcFails,
       "h225CallSignalStatsNotifyIns": h225CallSignalStatsNotifyIns,
       "h225CallSignalStatsNotifyOuts": h225CallSignalStatsNotifyOuts,
       "h225CallSignalStatsNotifyFails": h225CallSignalStatsNotifyFails,
       "h225CallSignalStatsInfoIns": h225CallSignalStatsInfoIns,
       "h225CallSignalStatsInfoOuts": h225CallSignalStatsInfoOuts,
       "h225CallSignalStatsInfoFails": h225CallSignalStatsInfoFails,
       "h225CallSignalStatsUserInfoIns": h225CallSignalStatsUserInfoIns,
       "h225CallSignalStatsUserInfoOuts": h225CallSignalStatsUserInfoOuts,
       "h225CallSignalStatsUserInfoFails": h225CallSignalStatsUserInfoFails,
       "h225CallSignalStatsFacilityIns": h225CallSignalStatsFacilityIns,
       "h225CallSignalStatsFacilityOuts": h225CallSignalStatsFacilityOuts,
       "h225CallSignalStatsFacilityFails": h225CallSignalStatsFacilityFails,
       "h225CallSignalStatsReleaseIns": h225CallSignalStatsReleaseIns,
       "h225CallSignalStatsReleaseOuts": h225CallSignalStatsReleaseOuts,
       "h225CallSignalStatsReleaseFails": h225CallSignalStatsReleaseFails,
       "h225CallSignalStatsRejectIns": h225CallSignalStatsRejectIns,
       "h225CallSignalStatsRejectOuts": h225CallSignalStatsRejectOuts,
       "h225CallSignalStatsRejectFails": h225CallSignalStatsRejectFails,
       "h225CallSignalStatsPassthroIns": h225CallSignalStatsPassthroIns,
       "h225CallSignalStatsPassthroOuts": h225CallSignalStatsPassthroOuts,
       "h225CallSignalStatsPassthroFails": h225CallSignalStatsPassthroFails,
       "h225Ras": h225Ras,
       "h225RasStats": h225RasStats,
       "h225RasStatsGkDiscoveryReqIns": h225RasStatsGkDiscoveryReqIns,
       "h225RasStatsGkDiscoveryReqOuts": h225RasStatsGkDiscoveryReqOuts,
       "h225RasStatsGkDiscoveryConfIns": h225RasStatsGkDiscoveryConfIns,
       "h225RasStatsGkDiscoveryConfOuts": h225RasStatsGkDiscoveryConfOuts,
       "h225RasStatsGkDiscoveryRejectIns": h225RasStatsGkDiscoveryRejectIns,
       "h225RasStatsGkDiscoveryRejOuts": h225RasStatsGkDiscoveryRejOuts,
       "h225RasStatsRegistrationReqIns": h225RasStatsRegistrationReqIns,
       "h225RasStatsRegistrationReqOuts": h225RasStatsRegistrationReqOuts,
       "h225RasStatsRegistrationConfIns": h225RasStatsRegistrationConfIns,
       "h225RasStatsRegistrationConfOuts": h225RasStatsRegistrationConfOuts,
       "h225RasStatsRegistrationRejIns": h225RasStatsRegistrationRejIns,
       "h225RasStatsRegistrationRejOuts": h225RasStatsRegistrationRejOuts,
       "h225RasStatsAdmissionReqIns": h225RasStatsAdmissionReqIns,
       "h225RasStatsAdmissionReqOuts": h225RasStatsAdmissionReqOuts,
       "h225RasStatsAdmissionConfirmIns": h225RasStatsAdmissionConfirmIns,
       "h225RasStatsAdmissionConfirmOuts": h225RasStatsAdmissionConfirmOuts,
       "h225RasStatsAdmissionRejectIns": h225RasStatsAdmissionRejectIns,
       "h225RasStatsAdmissionRejectOuts": h225RasStatsAdmissionRejectOuts,
       "h225RasStatsBandwidthReqIns": h225RasStatsBandwidthReqIns,
       "h225RasStatsBandwidthReqOuts": h225RasStatsBandwidthReqOuts,
       "h225RasStatsBandwidthConfirmIns": h225RasStatsBandwidthConfirmIns,
       "h225RasStatsBandwidthConfirmOuts": h225RasStatsBandwidthConfirmOuts,
       "h225RasStatsBandwidthRejectIns": h225RasStatsBandwidthRejectIns,
       "h225RasStatsBandwidthRejectOuts": h225RasStatsBandwidthRejectOuts,
       "h225RasStatsDisengageReqIns": h225RasStatsDisengageReqIns,
       "h225RasStatsDisengageReqOuts": h225RasStatsDisengageReqOuts,
       "h225RasStatsDisengageConfirmIns": h225RasStatsDisengageConfirmIns,
       "h225RasStatsDisengageConfirmOuts": h225RasStatsDisengageConfirmOuts,
       "h225RasStatsDisengageRejectIns": h225RasStatsDisengageRejectIns,
       "h225RasStatsDisengageRejectOuts": h225RasStatsDisengageRejectOuts,
       "h225RasStatsUnregisterReqIns": h225RasStatsUnregisterReqIns,
       "h225RasStatsUnregisterReqOuts": h225RasStatsUnregisterReqOuts,
       "h225RasStatsUnregisterConfirmIns": h225RasStatsUnregisterConfirmIns,
       "h225RasStatsUnregisterConfOuts": h225RasStatsUnregisterConfOuts,
       "h225RasStatsUnregisterRejectIns": h225RasStatsUnregisterRejectIns,
       "h225RasStatsUnregisterRejectOuts": h225RasStatsUnregisterRejectOuts,
       "h225RasStatsResourceAvailIndIns": h225RasStatsResourceAvailIndIns,
       "h225RasStatsResourceAvailIndOuts": h225RasStatsResourceAvailIndOuts,
       "h225RasStatsResourceAvailConfIns": h225RasStatsResourceAvailConfIns,
       "h225RasStatsResourceAvailConOuts": h225RasStatsResourceAvailConOuts,
       "h225RasStatsRequestInProgIns": h225RasStatsRequestInProgIns,
       "h225RasStatsRequestInProgOuts": h225RasStatsRequestInProgOuts,
       "h225MIBConformance": h225MIBConformance,
       "h225MIBCompliances": h225MIBCompliances,
       "h225MIBCompliance": h225MIBCompliance,
       "h225MIBComplianceRev1": h225MIBComplianceRev1,
       "h225MIBGroups": h225MIBGroups,
       "h225CallSignalStatsGroup": h225CallSignalStatsGroup,
       "h225RasStatsGroup": h225RasStatsGroup,
       "h225DisconnectCauseCodeGroup": h225DisconnectCauseCodeGroup,
       "h225DisconnectCauseCode": h225DisconnectCauseCode,
       "h225DisconnectCauseCodeTable": h225DisconnectCauseCodeTable,
       "h225DisconnectCauseCodeEntry": h225DisconnectCauseCodeEntry,
       "h225CauseCode": h225CauseCode,
       "h225CauseCodeDescription": h225CauseCodeDescription,
       "h225FromOtherPeerDisconnects": h225FromOtherPeerDisconnects,
       "h225FromH323PeerDisconnects": h225FromH323PeerDisconnects}
)
