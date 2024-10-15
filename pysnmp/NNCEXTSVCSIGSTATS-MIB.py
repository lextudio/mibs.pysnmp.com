# SNMP MIB module (NNCEXTSVCSIGSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTSVCSIGSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:22 2024
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

(NncExtAbsIntvlNumberType,
 NncExtIntvlDurationType,
 NncExtIntvlStateType,
 NncExtRelIntvlNumberType) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtAbsIntvlNumberType",
    "NncExtIntvlDurationType",
    "NncExtIntvlStateType",
    "NncExtRelIntvlNumberType")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncExtSVCSigStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NncExtSetupAttemptsType(Counter32, TextualConvention):
    status = "current"


class NncExtConnectedCallsType(Counter32, TextualConvention):
    status = "current"


class NncExtTransitedCallsType(Counter32, TextualConvention):
    status = "current"


class NncExtCalledPtyEventsType(Counter32, TextualConvention):
    status = "current"


class NncExtCallingPtyEventsType(Counter32, TextualConvention):
    status = "current"


class NncExtResUnavailableType(Counter32, TextualConvention):
    status = "current"


class NncExtRoutingFailureType(Counter32, TextualConvention):
    status = "current"


class NncExtInvalidMessageType(Counter32, TextualConvention):
    status = "current"


class NncExtTimerExpirationType(Counter32, TextualConvention):
    status = "current"


class NncExtNormalCallClrType(Counter32, TextualConvention):
    status = "current"


class NncExtOtherCausesType(Counter32, TextualConvention):
    status = "current"


class NncExtScreeningFailuresType(Counter32, TextualConvention):
    status = "current"


class NncExtActiveCallsType(Gauge32, TextualConvention):
    status = "current"


class NncExtSelectiveCallsType(Counter32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_NncExtSVCSigStatsObjects_ObjectIdentity = ObjectIdentity
nncExtSVCSigStatsObjects = _NncExtSVCSigStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1)
)
_NncExtSVCSigStatsCurrShortTable_Object = MibTable
nncExtSVCSigStatsCurrShortTable = _NncExtSVCSigStatsCurrShortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTable.setStatus("current")
_NncExtSVCSigStatsCurrShortEntry_Object = MibTableRow
nncExtSVCSigStatsCurrShortEntry = _NncExtSVCSigStatsCurrShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1)
)
nncExtSVCSigStatsCurrShortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortEntry.setStatus("current")
_NncExtSVCSigStatsCurrShortIntvlState_Type = NncExtIntvlStateType
_NncExtSVCSigStatsCurrShortIntvlState_Object = MibTableColumn
nncExtSVCSigStatsCurrShortIntvlState = _NncExtSVCSigStatsCurrShortIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 1),
    _NncExtSVCSigStatsCurrShortIntvlState_Type()
)
nncExtSVCSigStatsCurrShortIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortIntvlState.setStatus("current")
_NncExtSVCSigStatsCurrShortAbsIntvlNumber_Type = NncExtAbsIntvlNumberType
_NncExtSVCSigStatsCurrShortAbsIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsCurrShortAbsIntvlNumber = _NncExtSVCSigStatsCurrShortAbsIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 2),
    _NncExtSVCSigStatsCurrShortAbsIntvlNumber_Type()
)
nncExtSVCSigStatsCurrShortAbsIntvlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortAbsIntvlNumber.setStatus("current")
_NncExtSVCSigStatsCurrShortIntvlStartTime_Type = DateAndTime
_NncExtSVCSigStatsCurrShortIntvlStartTime_Object = MibTableColumn
nncExtSVCSigStatsCurrShortIntvlStartTime = _NncExtSVCSigStatsCurrShortIntvlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 3),
    _NncExtSVCSigStatsCurrShortIntvlStartTime_Type()
)
nncExtSVCSigStatsCurrShortIntvlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortIntvlStartTime.setStatus("current")
_NncExtSVCSigStatsCurrShortIntvlDuration_Type = NncExtIntvlDurationType
_NncExtSVCSigStatsCurrShortIntvlDuration_Object = MibTableColumn
nncExtSVCSigStatsCurrShortIntvlDuration = _NncExtSVCSigStatsCurrShortIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 4),
    _NncExtSVCSigStatsCurrShortIntvlDuration_Type()
)
nncExtSVCSigStatsCurrShortIntvlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortIntvlDuration.setStatus("current")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortIntvlDuration.setUnits("seconds")
_NncExtSVCSigStatsCurrShortInSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsCurrShortInSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsCurrShortInSetupAttempts = _NncExtSVCSigStatsCurrShortInSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 5),
    _NncExtSVCSigStatsCurrShortInSetupAttempts_Type()
)
nncExtSVCSigStatsCurrShortInSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortInSetupAttempts.setStatus("current")
_NncExtSVCSigStatsCurrShortInConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsCurrShortInConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortInConnectedCalls = _NncExtSVCSigStatsCurrShortInConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 6),
    _NncExtSVCSigStatsCurrShortInConnectedCalls_Type()
)
nncExtSVCSigStatsCurrShortInConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortInConnectedCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortInTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsCurrShortInTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortInTransitedCalls = _NncExtSVCSigStatsCurrShortInTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 7),
    _NncExtSVCSigStatsCurrShortInTransitedCalls_Type()
)
nncExtSVCSigStatsCurrShortInTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortInTransitedCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortOutSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsCurrShortOutSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsCurrShortOutSetupAttempts = _NncExtSVCSigStatsCurrShortOutSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 8),
    _NncExtSVCSigStatsCurrShortOutSetupAttempts_Type()
)
nncExtSVCSigStatsCurrShortOutSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortOutSetupAttempts.setStatus("current")
_NncExtSVCSigStatsCurrShortOutConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsCurrShortOutConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortOutConnectedCalls = _NncExtSVCSigStatsCurrShortOutConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 9),
    _NncExtSVCSigStatsCurrShortOutConnectedCalls_Type()
)
nncExtSVCSigStatsCurrShortOutConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortOutConnectedCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortOutTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsCurrShortOutTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortOutTransitedCalls = _NncExtSVCSigStatsCurrShortOutTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 10),
    _NncExtSVCSigStatsCurrShortOutTransitedCalls_Type()
)
nncExtSVCSigStatsCurrShortOutTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortOutTransitedCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortRxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsCurrShortRxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxCalledPtyEvents = _NncExtSVCSigStatsCurrShortRxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 11),
    _NncExtSVCSigStatsCurrShortRxCalledPtyEvents_Type()
)
nncExtSVCSigStatsCurrShortRxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrShortRxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsCurrShortRxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxCallingPtyEvents = _NncExtSVCSigStatsCurrShortRxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 12),
    _NncExtSVCSigStatsCurrShortRxCallingPtyEvents_Type()
)
nncExtSVCSigStatsCurrShortRxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrShortRxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsCurrShortRxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxResUnavailable = _NncExtSVCSigStatsCurrShortRxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 13),
    _NncExtSVCSigStatsCurrShortRxResUnavailable_Type()
)
nncExtSVCSigStatsCurrShortRxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxResUnavailable.setStatus("current")
_NncExtSVCSigStatsCurrShortRxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsCurrShortRxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxRoutingFailure = _NncExtSVCSigStatsCurrShortRxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 14),
    _NncExtSVCSigStatsCurrShortRxRoutingFailure_Type()
)
nncExtSVCSigStatsCurrShortRxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsCurrShortRxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsCurrShortRxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxInvalidMessage = _NncExtSVCSigStatsCurrShortRxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 15),
    _NncExtSVCSigStatsCurrShortRxInvalidMessage_Type()
)
nncExtSVCSigStatsCurrShortRxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsCurrShortRxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsCurrShortRxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxTimerExpiration = _NncExtSVCSigStatsCurrShortRxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 16),
    _NncExtSVCSigStatsCurrShortRxTimerExpiration_Type()
)
nncExtSVCSigStatsCurrShortRxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsCurrShortRxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsCurrShortRxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxNormalCallClr = _NncExtSVCSigStatsCurrShortRxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 17),
    _NncExtSVCSigStatsCurrShortRxNormalCallClr_Type()
)
nncExtSVCSigStatsCurrShortRxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsCurrShortRxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsCurrShortRxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsCurrShortRxOtherCauses = _NncExtSVCSigStatsCurrShortRxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 18),
    _NncExtSVCSigStatsCurrShortRxOtherCauses_Type()
)
nncExtSVCSigStatsCurrShortRxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortRxOtherCauses.setStatus("current")
_NncExtSVCSigStatsCurrShortTxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsCurrShortTxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxCalledPtyEvents = _NncExtSVCSigStatsCurrShortTxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 19),
    _NncExtSVCSigStatsCurrShortTxCalledPtyEvents_Type()
)
nncExtSVCSigStatsCurrShortTxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrShortTxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsCurrShortTxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxCallingPtyEvents = _NncExtSVCSigStatsCurrShortTxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 20),
    _NncExtSVCSigStatsCurrShortTxCallingPtyEvents_Type()
)
nncExtSVCSigStatsCurrShortTxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrShortTxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsCurrShortTxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxResUnavailable = _NncExtSVCSigStatsCurrShortTxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 21),
    _NncExtSVCSigStatsCurrShortTxResUnavailable_Type()
)
nncExtSVCSigStatsCurrShortTxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxResUnavailable.setStatus("current")
_NncExtSVCSigStatsCurrShortTxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsCurrShortTxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxRoutingFailure = _NncExtSVCSigStatsCurrShortTxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 22),
    _NncExtSVCSigStatsCurrShortTxRoutingFailure_Type()
)
nncExtSVCSigStatsCurrShortTxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsCurrShortTxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsCurrShortTxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxInvalidMessage = _NncExtSVCSigStatsCurrShortTxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 23),
    _NncExtSVCSigStatsCurrShortTxInvalidMessage_Type()
)
nncExtSVCSigStatsCurrShortTxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsCurrShortTxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsCurrShortTxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxTimerExpiration = _NncExtSVCSigStatsCurrShortTxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 24),
    _NncExtSVCSigStatsCurrShortTxTimerExpiration_Type()
)
nncExtSVCSigStatsCurrShortTxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsCurrShortTxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsCurrShortTxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxNormalCallClr = _NncExtSVCSigStatsCurrShortTxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 25),
    _NncExtSVCSigStatsCurrShortTxNormalCallClr_Type()
)
nncExtSVCSigStatsCurrShortTxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsCurrShortTxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsCurrShortTxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsCurrShortTxOtherCauses = _NncExtSVCSigStatsCurrShortTxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 26),
    _NncExtSVCSigStatsCurrShortTxOtherCauses_Type()
)
nncExtSVCSigStatsCurrShortTxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortTxOtherCauses.setStatus("current")
_NncExtSVCSigStatsCurrShortScreeningFailures_Type = NncExtScreeningFailuresType
_NncExtSVCSigStatsCurrShortScreeningFailures_Object = MibTableColumn
nncExtSVCSigStatsCurrShortScreeningFailures = _NncExtSVCSigStatsCurrShortScreeningFailures_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 27),
    _NncExtSVCSigStatsCurrShortScreeningFailures_Type()
)
nncExtSVCSigStatsCurrShortScreeningFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortScreeningFailures.setStatus("current")
_NncExtSVCSigStatsCurrShortInCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrShortInCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortInCDNSelectiveCalls = _NncExtSVCSigStatsCurrShortInCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 28),
    _NncExtSVCSigStatsCurrShortInCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrShortInCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortInCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortInCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrShortInCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortInCGNSelectiveCalls = _NncExtSVCSigStatsCurrShortInCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 29),
    _NncExtSVCSigStatsCurrShortInCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrShortInCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortInCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortOutCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrShortOutCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls = _NncExtSVCSigStatsCurrShortOutCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 30),
    _NncExtSVCSigStatsCurrShortOutCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrShortOutCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrShortOutCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls = _NncExtSVCSigStatsCurrShortOutCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 1, 1, 31),
    _NncExtSVCSigStatsCurrShortOutCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortTable_Object = MibTable
nncExtSVCSigStatsPrevShortTable = _NncExtSVCSigStatsPrevShortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTable.setStatus("current")
_NncExtSVCSigStatsPrevShortEntry_Object = MibTableRow
nncExtSVCSigStatsPrevShortEntry = _NncExtSVCSigStatsPrevShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1)
)
nncExtSVCSigStatsPrevShortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortIntvlNumber"),
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortEntry.setStatus("current")
_NncExtSVCSigStatsPrevShortIntvlNumber_Type = NncExtRelIntvlNumberType
_NncExtSVCSigStatsPrevShortIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsPrevShortIntvlNumber = _NncExtSVCSigStatsPrevShortIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 1),
    _NncExtSVCSigStatsPrevShortIntvlNumber_Type()
)
nncExtSVCSigStatsPrevShortIntvlNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortIntvlNumber.setStatus("current")
_NncExtSVCSigStatsPrevShortIntvlState_Type = NncExtIntvlStateType
_NncExtSVCSigStatsPrevShortIntvlState_Object = MibTableColumn
nncExtSVCSigStatsPrevShortIntvlState = _NncExtSVCSigStatsPrevShortIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 2),
    _NncExtSVCSigStatsPrevShortIntvlState_Type()
)
nncExtSVCSigStatsPrevShortIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortIntvlState.setStatus("current")
_NncExtSVCSigStatsPrevShortAbsIntvlNumber_Type = NncExtAbsIntvlNumberType
_NncExtSVCSigStatsPrevShortAbsIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsPrevShortAbsIntvlNumber = _NncExtSVCSigStatsPrevShortAbsIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 3),
    _NncExtSVCSigStatsPrevShortAbsIntvlNumber_Type()
)
nncExtSVCSigStatsPrevShortAbsIntvlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortAbsIntvlNumber.setStatus("current")
_NncExtSVCSigStatsPrevShortIntvlStartTime_Type = DateAndTime
_NncExtSVCSigStatsPrevShortIntvlStartTime_Object = MibTableColumn
nncExtSVCSigStatsPrevShortIntvlStartTime = _NncExtSVCSigStatsPrevShortIntvlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 4),
    _NncExtSVCSigStatsPrevShortIntvlStartTime_Type()
)
nncExtSVCSigStatsPrevShortIntvlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortIntvlStartTime.setStatus("current")
_NncExtSVCSigStatsPrevShortIntvlDuration_Type = NncExtIntvlDurationType
_NncExtSVCSigStatsPrevShortIntvlDuration_Object = MibTableColumn
nncExtSVCSigStatsPrevShortIntvlDuration = _NncExtSVCSigStatsPrevShortIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 5),
    _NncExtSVCSigStatsPrevShortIntvlDuration_Type()
)
nncExtSVCSigStatsPrevShortIntvlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortIntvlDuration.setStatus("current")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortIntvlDuration.setUnits("seconds")
_NncExtSVCSigStatsPrevShortInSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsPrevShortInSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsPrevShortInSetupAttempts = _NncExtSVCSigStatsPrevShortInSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 6),
    _NncExtSVCSigStatsPrevShortInSetupAttempts_Type()
)
nncExtSVCSigStatsPrevShortInSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortInSetupAttempts.setStatus("current")
_NncExtSVCSigStatsPrevShortInConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsPrevShortInConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortInConnectedCalls = _NncExtSVCSigStatsPrevShortInConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 7),
    _NncExtSVCSigStatsPrevShortInConnectedCalls_Type()
)
nncExtSVCSigStatsPrevShortInConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortInConnectedCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortInTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsPrevShortInTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortInTransitedCalls = _NncExtSVCSigStatsPrevShortInTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 8),
    _NncExtSVCSigStatsPrevShortInTransitedCalls_Type()
)
nncExtSVCSigStatsPrevShortInTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortInTransitedCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortOutSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsPrevShortOutSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsPrevShortOutSetupAttempts = _NncExtSVCSigStatsPrevShortOutSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 9),
    _NncExtSVCSigStatsPrevShortOutSetupAttempts_Type()
)
nncExtSVCSigStatsPrevShortOutSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortOutSetupAttempts.setStatus("current")
_NncExtSVCSigStatsPrevShortOutConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsPrevShortOutConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortOutConnectedCalls = _NncExtSVCSigStatsPrevShortOutConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 10),
    _NncExtSVCSigStatsPrevShortOutConnectedCalls_Type()
)
nncExtSVCSigStatsPrevShortOutConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortOutConnectedCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortOutTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsPrevShortOutTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortOutTransitedCalls = _NncExtSVCSigStatsPrevShortOutTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 11),
    _NncExtSVCSigStatsPrevShortOutTransitedCalls_Type()
)
nncExtSVCSigStatsPrevShortOutTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortOutTransitedCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortRxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsPrevShortRxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxCalledPtyEvents = _NncExtSVCSigStatsPrevShortRxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 12),
    _NncExtSVCSigStatsPrevShortRxCalledPtyEvents_Type()
)
nncExtSVCSigStatsPrevShortRxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevShortRxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsPrevShortRxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxCallingPtyEvents = _NncExtSVCSigStatsPrevShortRxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 13),
    _NncExtSVCSigStatsPrevShortRxCallingPtyEvents_Type()
)
nncExtSVCSigStatsPrevShortRxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevShortRxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsPrevShortRxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxResUnavailable = _NncExtSVCSigStatsPrevShortRxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 14),
    _NncExtSVCSigStatsPrevShortRxResUnavailable_Type()
)
nncExtSVCSigStatsPrevShortRxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxResUnavailable.setStatus("current")
_NncExtSVCSigStatsPrevShortRxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsPrevShortRxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxRoutingFailure = _NncExtSVCSigStatsPrevShortRxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 15),
    _NncExtSVCSigStatsPrevShortRxRoutingFailure_Type()
)
nncExtSVCSigStatsPrevShortRxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsPrevShortRxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsPrevShortRxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxInvalidMessage = _NncExtSVCSigStatsPrevShortRxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 16),
    _NncExtSVCSigStatsPrevShortRxInvalidMessage_Type()
)
nncExtSVCSigStatsPrevShortRxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsPrevShortRxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsPrevShortRxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxTimerExpiration = _NncExtSVCSigStatsPrevShortRxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 17),
    _NncExtSVCSigStatsPrevShortRxTimerExpiration_Type()
)
nncExtSVCSigStatsPrevShortRxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsPrevShortRxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsPrevShortRxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxNormalCallClr = _NncExtSVCSigStatsPrevShortRxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 18),
    _NncExtSVCSigStatsPrevShortRxNormalCallClr_Type()
)
nncExtSVCSigStatsPrevShortRxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsPrevShortRxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsPrevShortRxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsPrevShortRxOtherCauses = _NncExtSVCSigStatsPrevShortRxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 19),
    _NncExtSVCSigStatsPrevShortRxOtherCauses_Type()
)
nncExtSVCSigStatsPrevShortRxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortRxOtherCauses.setStatus("current")
_NncExtSVCSigStatsPrevShortTxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsPrevShortTxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxCalledPtyEvents = _NncExtSVCSigStatsPrevShortTxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 20),
    _NncExtSVCSigStatsPrevShortTxCalledPtyEvents_Type()
)
nncExtSVCSigStatsPrevShortTxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevShortTxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsPrevShortTxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxCallingPtyEvents = _NncExtSVCSigStatsPrevShortTxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 21),
    _NncExtSVCSigStatsPrevShortTxCallingPtyEvents_Type()
)
nncExtSVCSigStatsPrevShortTxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevShortTxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsPrevShortTxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxResUnavailable = _NncExtSVCSigStatsPrevShortTxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 22),
    _NncExtSVCSigStatsPrevShortTxResUnavailable_Type()
)
nncExtSVCSigStatsPrevShortTxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxResUnavailable.setStatus("current")
_NncExtSVCSigStatsPrevShortTxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsPrevShortTxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxRoutingFailure = _NncExtSVCSigStatsPrevShortTxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 23),
    _NncExtSVCSigStatsPrevShortTxRoutingFailure_Type()
)
nncExtSVCSigStatsPrevShortTxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsPrevShortTxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsPrevShortTxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxInvalidMessage = _NncExtSVCSigStatsPrevShortTxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 24),
    _NncExtSVCSigStatsPrevShortTxInvalidMessage_Type()
)
nncExtSVCSigStatsPrevShortTxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsPrevShortTxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsPrevShortTxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxTimerExpiration = _NncExtSVCSigStatsPrevShortTxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 25),
    _NncExtSVCSigStatsPrevShortTxTimerExpiration_Type()
)
nncExtSVCSigStatsPrevShortTxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsPrevShortTxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsPrevShortTxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxNormalCallClr = _NncExtSVCSigStatsPrevShortTxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 26),
    _NncExtSVCSigStatsPrevShortTxNormalCallClr_Type()
)
nncExtSVCSigStatsPrevShortTxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsPrevShortTxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsPrevShortTxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsPrevShortTxOtherCauses = _NncExtSVCSigStatsPrevShortTxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 27),
    _NncExtSVCSigStatsPrevShortTxOtherCauses_Type()
)
nncExtSVCSigStatsPrevShortTxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortTxOtherCauses.setStatus("current")
_NncExtSVCSigStatsPrevShortScreeningFailures_Type = NncExtScreeningFailuresType
_NncExtSVCSigStatsPrevShortScreeningFailures_Object = MibTableColumn
nncExtSVCSigStatsPrevShortScreeningFailures = _NncExtSVCSigStatsPrevShortScreeningFailures_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 28),
    _NncExtSVCSigStatsPrevShortScreeningFailures_Type()
)
nncExtSVCSigStatsPrevShortScreeningFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortScreeningFailures.setStatus("current")
_NncExtSVCSigStatsPrevShortInCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevShortInCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortInCDNSelectiveCalls = _NncExtSVCSigStatsPrevShortInCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 29),
    _NncExtSVCSigStatsPrevShortInCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevShortInCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortInCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortInCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevShortInCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortInCGNSelectiveCalls = _NncExtSVCSigStatsPrevShortInCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 30),
    _NncExtSVCSigStatsPrevShortInCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevShortInCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortInCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortOutCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevShortOutCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls = _NncExtSVCSigStatsPrevShortOutCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 31),
    _NncExtSVCSigStatsPrevShortOutCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevShortOutCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevShortOutCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls = _NncExtSVCSigStatsPrevShortOutCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 2, 1, 32),
    _NncExtSVCSigStatsPrevShortOutCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongTable_Object = MibTable
nncExtSVCSigStatsCurrLongTable = _NncExtSVCSigStatsCurrLongTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTable.setStatus("current")
_NncExtSVCSigStatsCurrLongEntry_Object = MibTableRow
nncExtSVCSigStatsCurrLongEntry = _NncExtSVCSigStatsCurrLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1)
)
nncExtSVCSigStatsCurrLongEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongEntry.setStatus("current")
_NncExtSVCSigStatsCurrLongIntvlState_Type = NncExtIntvlStateType
_NncExtSVCSigStatsCurrLongIntvlState_Object = MibTableColumn
nncExtSVCSigStatsCurrLongIntvlState = _NncExtSVCSigStatsCurrLongIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 1),
    _NncExtSVCSigStatsCurrLongIntvlState_Type()
)
nncExtSVCSigStatsCurrLongIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongIntvlState.setStatus("current")
_NncExtSVCSigStatsCurrLongAbsIntvlNumber_Type = NncExtAbsIntvlNumberType
_NncExtSVCSigStatsCurrLongAbsIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsCurrLongAbsIntvlNumber = _NncExtSVCSigStatsCurrLongAbsIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 2),
    _NncExtSVCSigStatsCurrLongAbsIntvlNumber_Type()
)
nncExtSVCSigStatsCurrLongAbsIntvlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongAbsIntvlNumber.setStatus("current")
_NncExtSVCSigStatsCurrLongIntvlStartTime_Type = DateAndTime
_NncExtSVCSigStatsCurrLongIntvlStartTime_Object = MibTableColumn
nncExtSVCSigStatsCurrLongIntvlStartTime = _NncExtSVCSigStatsCurrLongIntvlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 3),
    _NncExtSVCSigStatsCurrLongIntvlStartTime_Type()
)
nncExtSVCSigStatsCurrLongIntvlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongIntvlStartTime.setStatus("current")
_NncExtSVCSigStatsCurrLongIntvlDuration_Type = NncExtIntvlDurationType
_NncExtSVCSigStatsCurrLongIntvlDuration_Object = MibTableColumn
nncExtSVCSigStatsCurrLongIntvlDuration = _NncExtSVCSigStatsCurrLongIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 4),
    _NncExtSVCSigStatsCurrLongIntvlDuration_Type()
)
nncExtSVCSigStatsCurrLongIntvlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongIntvlDuration.setStatus("current")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongIntvlDuration.setUnits("seconds")
_NncExtSVCSigStatsCurrLongInSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsCurrLongInSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsCurrLongInSetupAttempts = _NncExtSVCSigStatsCurrLongInSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 5),
    _NncExtSVCSigStatsCurrLongInSetupAttempts_Type()
)
nncExtSVCSigStatsCurrLongInSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongInSetupAttempts.setStatus("current")
_NncExtSVCSigStatsCurrLongInConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsCurrLongInConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongInConnectedCalls = _NncExtSVCSigStatsCurrLongInConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 6),
    _NncExtSVCSigStatsCurrLongInConnectedCalls_Type()
)
nncExtSVCSigStatsCurrLongInConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongInConnectedCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongInTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsCurrLongInTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongInTransitedCalls = _NncExtSVCSigStatsCurrLongInTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 7),
    _NncExtSVCSigStatsCurrLongInTransitedCalls_Type()
)
nncExtSVCSigStatsCurrLongInTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongInTransitedCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongOutSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsCurrLongOutSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsCurrLongOutSetupAttempts = _NncExtSVCSigStatsCurrLongOutSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 8),
    _NncExtSVCSigStatsCurrLongOutSetupAttempts_Type()
)
nncExtSVCSigStatsCurrLongOutSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongOutSetupAttempts.setStatus("current")
_NncExtSVCSigStatsCurrLongOutConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsCurrLongOutConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongOutConnectedCalls = _NncExtSVCSigStatsCurrLongOutConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 9),
    _NncExtSVCSigStatsCurrLongOutConnectedCalls_Type()
)
nncExtSVCSigStatsCurrLongOutConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongOutConnectedCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongOutTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsCurrLongOutTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongOutTransitedCalls = _NncExtSVCSigStatsCurrLongOutTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 10),
    _NncExtSVCSigStatsCurrLongOutTransitedCalls_Type()
)
nncExtSVCSigStatsCurrLongOutTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongOutTransitedCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongRxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsCurrLongRxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxCalledPtyEvents = _NncExtSVCSigStatsCurrLongRxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 11),
    _NncExtSVCSigStatsCurrLongRxCalledPtyEvents_Type()
)
nncExtSVCSigStatsCurrLongRxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrLongRxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsCurrLongRxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxCallingPtyEvents = _NncExtSVCSigStatsCurrLongRxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 12),
    _NncExtSVCSigStatsCurrLongRxCallingPtyEvents_Type()
)
nncExtSVCSigStatsCurrLongRxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrLongRxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsCurrLongRxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxResUnavailable = _NncExtSVCSigStatsCurrLongRxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 13),
    _NncExtSVCSigStatsCurrLongRxResUnavailable_Type()
)
nncExtSVCSigStatsCurrLongRxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxResUnavailable.setStatus("current")
_NncExtSVCSigStatsCurrLongRxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsCurrLongRxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxRoutingFailure = _NncExtSVCSigStatsCurrLongRxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 14),
    _NncExtSVCSigStatsCurrLongRxRoutingFailure_Type()
)
nncExtSVCSigStatsCurrLongRxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsCurrLongRxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsCurrLongRxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxInvalidMessage = _NncExtSVCSigStatsCurrLongRxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 15),
    _NncExtSVCSigStatsCurrLongRxInvalidMessage_Type()
)
nncExtSVCSigStatsCurrLongRxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsCurrLongRxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsCurrLongRxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxTimerExpiration = _NncExtSVCSigStatsCurrLongRxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 16),
    _NncExtSVCSigStatsCurrLongRxTimerExpiration_Type()
)
nncExtSVCSigStatsCurrLongRxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsCurrLongRxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsCurrLongRxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxNormalCallClr = _NncExtSVCSigStatsCurrLongRxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 17),
    _NncExtSVCSigStatsCurrLongRxNormalCallClr_Type()
)
nncExtSVCSigStatsCurrLongRxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsCurrLongRxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsCurrLongRxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsCurrLongRxOtherCauses = _NncExtSVCSigStatsCurrLongRxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 18),
    _NncExtSVCSigStatsCurrLongRxOtherCauses_Type()
)
nncExtSVCSigStatsCurrLongRxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongRxOtherCauses.setStatus("current")
_NncExtSVCSigStatsCurrLongTxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsCurrLongTxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxCalledPtyEvents = _NncExtSVCSigStatsCurrLongTxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 19),
    _NncExtSVCSigStatsCurrLongTxCalledPtyEvents_Type()
)
nncExtSVCSigStatsCurrLongTxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrLongTxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsCurrLongTxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxCallingPtyEvents = _NncExtSVCSigStatsCurrLongTxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 20),
    _NncExtSVCSigStatsCurrLongTxCallingPtyEvents_Type()
)
nncExtSVCSigStatsCurrLongTxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsCurrLongTxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsCurrLongTxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxResUnavailable = _NncExtSVCSigStatsCurrLongTxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 21),
    _NncExtSVCSigStatsCurrLongTxResUnavailable_Type()
)
nncExtSVCSigStatsCurrLongTxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxResUnavailable.setStatus("current")
_NncExtSVCSigStatsCurrLongTxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsCurrLongTxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxRoutingFailure = _NncExtSVCSigStatsCurrLongTxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 22),
    _NncExtSVCSigStatsCurrLongTxRoutingFailure_Type()
)
nncExtSVCSigStatsCurrLongTxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsCurrLongTxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsCurrLongTxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxInvalidMessage = _NncExtSVCSigStatsCurrLongTxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 23),
    _NncExtSVCSigStatsCurrLongTxInvalidMessage_Type()
)
nncExtSVCSigStatsCurrLongTxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsCurrLongTxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsCurrLongTxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxTimerExpiration = _NncExtSVCSigStatsCurrLongTxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 24),
    _NncExtSVCSigStatsCurrLongTxTimerExpiration_Type()
)
nncExtSVCSigStatsCurrLongTxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsCurrLongTxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsCurrLongTxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxNormalCallClr = _NncExtSVCSigStatsCurrLongTxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 25),
    _NncExtSVCSigStatsCurrLongTxNormalCallClr_Type()
)
nncExtSVCSigStatsCurrLongTxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsCurrLongTxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsCurrLongTxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsCurrLongTxOtherCauses = _NncExtSVCSigStatsCurrLongTxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 26),
    _NncExtSVCSigStatsCurrLongTxOtherCauses_Type()
)
nncExtSVCSigStatsCurrLongTxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongTxOtherCauses.setStatus("current")
_NncExtSVCSigStatsCurrLongScreeningFailures_Type = NncExtScreeningFailuresType
_NncExtSVCSigStatsCurrLongScreeningFailures_Object = MibTableColumn
nncExtSVCSigStatsCurrLongScreeningFailures = _NncExtSVCSigStatsCurrLongScreeningFailures_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 27),
    _NncExtSVCSigStatsCurrLongScreeningFailures_Type()
)
nncExtSVCSigStatsCurrLongScreeningFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongScreeningFailures.setStatus("current")
_NncExtSVCSigStatsCurrLongInCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrLongInCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongInCDNSelectiveCalls = _NncExtSVCSigStatsCurrLongInCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 28),
    _NncExtSVCSigStatsCurrLongInCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrLongInCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongInCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongInCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrLongInCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongInCGNSelectiveCalls = _NncExtSVCSigStatsCurrLongInCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 29),
    _NncExtSVCSigStatsCurrLongInCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrLongInCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongInCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongOutCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrLongOutCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls = _NncExtSVCSigStatsCurrLongOutCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 30),
    _NncExtSVCSigStatsCurrLongOutCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsCurrLongOutCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsCurrLongOutCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls = _NncExtSVCSigStatsCurrLongOutCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 3, 1, 31),
    _NncExtSVCSigStatsCurrLongOutCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongTable_Object = MibTable
nncExtSVCSigStatsPrevLongTable = _NncExtSVCSigStatsPrevLongTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTable.setStatus("current")
_NncExtSVCSigStatsPrevLongEntry_Object = MibTableRow
nncExtSVCSigStatsPrevLongEntry = _NncExtSVCSigStatsPrevLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1)
)
nncExtSVCSigStatsPrevLongEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongIntvlNumber"),
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongEntry.setStatus("current")
_NncExtSVCSigStatsPrevLongIntvlNumber_Type = NncExtRelIntvlNumberType
_NncExtSVCSigStatsPrevLongIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsPrevLongIntvlNumber = _NncExtSVCSigStatsPrevLongIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 1),
    _NncExtSVCSigStatsPrevLongIntvlNumber_Type()
)
nncExtSVCSigStatsPrevLongIntvlNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongIntvlNumber.setStatus("current")
_NncExtSVCSigStatsPrevLongIntvlState_Type = NncExtIntvlStateType
_NncExtSVCSigStatsPrevLongIntvlState_Object = MibTableColumn
nncExtSVCSigStatsPrevLongIntvlState = _NncExtSVCSigStatsPrevLongIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 2),
    _NncExtSVCSigStatsPrevLongIntvlState_Type()
)
nncExtSVCSigStatsPrevLongIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongIntvlState.setStatus("current")
_NncExtSVCSigStatsPrevLongAbsIntvlNumber_Type = NncExtAbsIntvlNumberType
_NncExtSVCSigStatsPrevLongAbsIntvlNumber_Object = MibTableColumn
nncExtSVCSigStatsPrevLongAbsIntvlNumber = _NncExtSVCSigStatsPrevLongAbsIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 3),
    _NncExtSVCSigStatsPrevLongAbsIntvlNumber_Type()
)
nncExtSVCSigStatsPrevLongAbsIntvlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongAbsIntvlNumber.setStatus("current")
_NncExtSVCSigStatsPrevLongIntvlStartTime_Type = DateAndTime
_NncExtSVCSigStatsPrevLongIntvlStartTime_Object = MibTableColumn
nncExtSVCSigStatsPrevLongIntvlStartTime = _NncExtSVCSigStatsPrevLongIntvlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 4),
    _NncExtSVCSigStatsPrevLongIntvlStartTime_Type()
)
nncExtSVCSigStatsPrevLongIntvlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongIntvlStartTime.setStatus("current")
_NncExtSVCSigStatsPrevLongIntvlDuration_Type = NncExtIntvlDurationType
_NncExtSVCSigStatsPrevLongIntvlDuration_Object = MibTableColumn
nncExtSVCSigStatsPrevLongIntvlDuration = _NncExtSVCSigStatsPrevLongIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 5),
    _NncExtSVCSigStatsPrevLongIntvlDuration_Type()
)
nncExtSVCSigStatsPrevLongIntvlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongIntvlDuration.setStatus("current")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongIntvlDuration.setUnits("seconds")
_NncExtSVCSigStatsPrevLongInSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsPrevLongInSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsPrevLongInSetupAttempts = _NncExtSVCSigStatsPrevLongInSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 6),
    _NncExtSVCSigStatsPrevLongInSetupAttempts_Type()
)
nncExtSVCSigStatsPrevLongInSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongInSetupAttempts.setStatus("current")
_NncExtSVCSigStatsPrevLongInConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsPrevLongInConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongInConnectedCalls = _NncExtSVCSigStatsPrevLongInConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 7),
    _NncExtSVCSigStatsPrevLongInConnectedCalls_Type()
)
nncExtSVCSigStatsPrevLongInConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongInConnectedCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongInTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsPrevLongInTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongInTransitedCalls = _NncExtSVCSigStatsPrevLongInTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 8),
    _NncExtSVCSigStatsPrevLongInTransitedCalls_Type()
)
nncExtSVCSigStatsPrevLongInTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongInTransitedCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongOutSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsPrevLongOutSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsPrevLongOutSetupAttempts = _NncExtSVCSigStatsPrevLongOutSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 9),
    _NncExtSVCSigStatsPrevLongOutSetupAttempts_Type()
)
nncExtSVCSigStatsPrevLongOutSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongOutSetupAttempts.setStatus("current")
_NncExtSVCSigStatsPrevLongOutConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsPrevLongOutConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongOutConnectedCalls = _NncExtSVCSigStatsPrevLongOutConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 10),
    _NncExtSVCSigStatsPrevLongOutConnectedCalls_Type()
)
nncExtSVCSigStatsPrevLongOutConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongOutConnectedCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongOutTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsPrevLongOutTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongOutTransitedCalls = _NncExtSVCSigStatsPrevLongOutTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 11),
    _NncExtSVCSigStatsPrevLongOutTransitedCalls_Type()
)
nncExtSVCSigStatsPrevLongOutTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongOutTransitedCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongRxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsPrevLongRxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxCalledPtyEvents = _NncExtSVCSigStatsPrevLongRxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 12),
    _NncExtSVCSigStatsPrevLongRxCalledPtyEvents_Type()
)
nncExtSVCSigStatsPrevLongRxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevLongRxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsPrevLongRxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxCallingPtyEvents = _NncExtSVCSigStatsPrevLongRxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 13),
    _NncExtSVCSigStatsPrevLongRxCallingPtyEvents_Type()
)
nncExtSVCSigStatsPrevLongRxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevLongRxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsPrevLongRxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxResUnavailable = _NncExtSVCSigStatsPrevLongRxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 14),
    _NncExtSVCSigStatsPrevLongRxResUnavailable_Type()
)
nncExtSVCSigStatsPrevLongRxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxResUnavailable.setStatus("current")
_NncExtSVCSigStatsPrevLongRxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsPrevLongRxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxRoutingFailure = _NncExtSVCSigStatsPrevLongRxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 15),
    _NncExtSVCSigStatsPrevLongRxRoutingFailure_Type()
)
nncExtSVCSigStatsPrevLongRxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsPrevLongRxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsPrevLongRxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxInvalidMessage = _NncExtSVCSigStatsPrevLongRxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 16),
    _NncExtSVCSigStatsPrevLongRxInvalidMessage_Type()
)
nncExtSVCSigStatsPrevLongRxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsPrevLongRxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsPrevLongRxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxTimerExpiration = _NncExtSVCSigStatsPrevLongRxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 17),
    _NncExtSVCSigStatsPrevLongRxTimerExpiration_Type()
)
nncExtSVCSigStatsPrevLongRxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsPrevLongRxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsPrevLongRxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxNormalCallClr = _NncExtSVCSigStatsPrevLongRxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 18),
    _NncExtSVCSigStatsPrevLongRxNormalCallClr_Type()
)
nncExtSVCSigStatsPrevLongRxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsPrevLongRxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsPrevLongRxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsPrevLongRxOtherCauses = _NncExtSVCSigStatsPrevLongRxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 19),
    _NncExtSVCSigStatsPrevLongRxOtherCauses_Type()
)
nncExtSVCSigStatsPrevLongRxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongRxOtherCauses.setStatus("current")
_NncExtSVCSigStatsPrevLongTxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsPrevLongTxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxCalledPtyEvents = _NncExtSVCSigStatsPrevLongTxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 20),
    _NncExtSVCSigStatsPrevLongTxCalledPtyEvents_Type()
)
nncExtSVCSigStatsPrevLongTxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevLongTxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsPrevLongTxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxCallingPtyEvents = _NncExtSVCSigStatsPrevLongTxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 21),
    _NncExtSVCSigStatsPrevLongTxCallingPtyEvents_Type()
)
nncExtSVCSigStatsPrevLongTxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsPrevLongTxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsPrevLongTxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxResUnavailable = _NncExtSVCSigStatsPrevLongTxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 22),
    _NncExtSVCSigStatsPrevLongTxResUnavailable_Type()
)
nncExtSVCSigStatsPrevLongTxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxResUnavailable.setStatus("current")
_NncExtSVCSigStatsPrevLongTxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsPrevLongTxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxRoutingFailure = _NncExtSVCSigStatsPrevLongTxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 23),
    _NncExtSVCSigStatsPrevLongTxRoutingFailure_Type()
)
nncExtSVCSigStatsPrevLongTxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsPrevLongTxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsPrevLongTxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxInvalidMessage = _NncExtSVCSigStatsPrevLongTxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 24),
    _NncExtSVCSigStatsPrevLongTxInvalidMessage_Type()
)
nncExtSVCSigStatsPrevLongTxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsPrevLongTxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsPrevLongTxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxTimerExpiration = _NncExtSVCSigStatsPrevLongTxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 25),
    _NncExtSVCSigStatsPrevLongTxTimerExpiration_Type()
)
nncExtSVCSigStatsPrevLongTxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsPrevLongTxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsPrevLongTxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxNormalCallClr = _NncExtSVCSigStatsPrevLongTxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 26),
    _NncExtSVCSigStatsPrevLongTxNormalCallClr_Type()
)
nncExtSVCSigStatsPrevLongTxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsPrevLongTxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsPrevLongTxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsPrevLongTxOtherCauses = _NncExtSVCSigStatsPrevLongTxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 27),
    _NncExtSVCSigStatsPrevLongTxOtherCauses_Type()
)
nncExtSVCSigStatsPrevLongTxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongTxOtherCauses.setStatus("current")
_NncExtSVCSigStatsPrevLongScreeningFailures_Type = NncExtScreeningFailuresType
_NncExtSVCSigStatsPrevLongScreeningFailures_Object = MibTableColumn
nncExtSVCSigStatsPrevLongScreeningFailures = _NncExtSVCSigStatsPrevLongScreeningFailures_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 28),
    _NncExtSVCSigStatsPrevLongScreeningFailures_Type()
)
nncExtSVCSigStatsPrevLongScreeningFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongScreeningFailures.setStatus("current")
_NncExtSVCSigStatsPrevLongInCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevLongInCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongInCDNSelectiveCalls = _NncExtSVCSigStatsPrevLongInCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 29),
    _NncExtSVCSigStatsPrevLongInCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevLongInCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongInCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongInCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevLongInCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongInCGNSelectiveCalls = _NncExtSVCSigStatsPrevLongInCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 30),
    _NncExtSVCSigStatsPrevLongInCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevLongInCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongInCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongOutCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevLongOutCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls = _NncExtSVCSigStatsPrevLongOutCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 31),
    _NncExtSVCSigStatsPrevLongOutCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsPrevLongOutCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsPrevLongOutCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls = _NncExtSVCSigStatsPrevLongOutCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 4, 1, 32),
    _NncExtSVCSigStatsPrevLongOutCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsRawTable_Object = MibTable
nncExtSVCSigStatsRawTable = _NncExtSVCSigStatsRawTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTable.setStatus("current")
_NncExtSVCSigStatsRawEntry_Object = MibTableRow
nncExtSVCSigStatsRawEntry = _NncExtSVCSigStatsRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1)
)
nncExtSVCSigStatsRawEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawEntry.setStatus("current")
_NncExtSVCSigStatsRawState_Type = NncExtIntvlStateType
_NncExtSVCSigStatsRawState_Object = MibTableColumn
nncExtSVCSigStatsRawState = _NncExtSVCSigStatsRawState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 1),
    _NncExtSVCSigStatsRawState_Type()
)
nncExtSVCSigStatsRawState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawState.setStatus("current")
_NncExtSVCSigStatsRawStartTime_Type = DateAndTime
_NncExtSVCSigStatsRawStartTime_Object = MibTableColumn
nncExtSVCSigStatsRawStartTime = _NncExtSVCSigStatsRawStartTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 2),
    _NncExtSVCSigStatsRawStartTime_Type()
)
nncExtSVCSigStatsRawStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawStartTime.setStatus("current")
_NncExtSVCSigStatsRawDuration_Type = NncExtIntvlDurationType
_NncExtSVCSigStatsRawDuration_Object = MibTableColumn
nncExtSVCSigStatsRawDuration = _NncExtSVCSigStatsRawDuration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 3),
    _NncExtSVCSigStatsRawDuration_Type()
)
nncExtSVCSigStatsRawDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawDuration.setStatus("current")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawDuration.setUnits("seconds")
_NncExtSVCSigStatsRawActiveCalls_Type = NncExtActiveCallsType
_NncExtSVCSigStatsRawActiveCalls_Object = MibTableColumn
nncExtSVCSigStatsRawActiveCalls = _NncExtSVCSigStatsRawActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 4),
    _NncExtSVCSigStatsRawActiveCalls_Type()
)
nncExtSVCSigStatsRawActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawActiveCalls.setStatus("current")
_NncExtSVCSigStatsRawInSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsRawInSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsRawInSetupAttempts = _NncExtSVCSigStatsRawInSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 5),
    _NncExtSVCSigStatsRawInSetupAttempts_Type()
)
nncExtSVCSigStatsRawInSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawInSetupAttempts.setStatus("current")
_NncExtSVCSigStatsRawInConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsRawInConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsRawInConnectedCalls = _NncExtSVCSigStatsRawInConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 6),
    _NncExtSVCSigStatsRawInConnectedCalls_Type()
)
nncExtSVCSigStatsRawInConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawInConnectedCalls.setStatus("current")
_NncExtSVCSigStatsRawInTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsRawInTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsRawInTransitedCalls = _NncExtSVCSigStatsRawInTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 7),
    _NncExtSVCSigStatsRawInTransitedCalls_Type()
)
nncExtSVCSigStatsRawInTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawInTransitedCalls.setStatus("current")
_NncExtSVCSigStatsRawOutSetupAttempts_Type = NncExtSetupAttemptsType
_NncExtSVCSigStatsRawOutSetupAttempts_Object = MibTableColumn
nncExtSVCSigStatsRawOutSetupAttempts = _NncExtSVCSigStatsRawOutSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 8),
    _NncExtSVCSigStatsRawOutSetupAttempts_Type()
)
nncExtSVCSigStatsRawOutSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawOutSetupAttempts.setStatus("current")
_NncExtSVCSigStatsRawOutConnectedCalls_Type = NncExtConnectedCallsType
_NncExtSVCSigStatsRawOutConnectedCalls_Object = MibTableColumn
nncExtSVCSigStatsRawOutConnectedCalls = _NncExtSVCSigStatsRawOutConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 9),
    _NncExtSVCSigStatsRawOutConnectedCalls_Type()
)
nncExtSVCSigStatsRawOutConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawOutConnectedCalls.setStatus("current")
_NncExtSVCSigStatsRawOutTransitedCalls_Type = NncExtTransitedCallsType
_NncExtSVCSigStatsRawOutTransitedCalls_Object = MibTableColumn
nncExtSVCSigStatsRawOutTransitedCalls = _NncExtSVCSigStatsRawOutTransitedCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 10),
    _NncExtSVCSigStatsRawOutTransitedCalls_Type()
)
nncExtSVCSigStatsRawOutTransitedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawOutTransitedCalls.setStatus("current")
_NncExtSVCSigStatsRawRxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsRawRxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsRawRxCalledPtyEvents = _NncExtSVCSigStatsRawRxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 11),
    _NncExtSVCSigStatsRawRxCalledPtyEvents_Type()
)
nncExtSVCSigStatsRawRxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsRawRxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsRawRxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsRawRxCallingPtyEvents = _NncExtSVCSigStatsRawRxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 12),
    _NncExtSVCSigStatsRawRxCallingPtyEvents_Type()
)
nncExtSVCSigStatsRawRxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsRawRxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsRawRxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsRawRxResUnavailable = _NncExtSVCSigStatsRawRxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 13),
    _NncExtSVCSigStatsRawRxResUnavailable_Type()
)
nncExtSVCSigStatsRawRxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxResUnavailable.setStatus("current")
_NncExtSVCSigStatsRawRxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsRawRxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsRawRxRoutingFailure = _NncExtSVCSigStatsRawRxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 14),
    _NncExtSVCSigStatsRawRxRoutingFailure_Type()
)
nncExtSVCSigStatsRawRxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsRawRxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsRawRxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsRawRxInvalidMessage = _NncExtSVCSigStatsRawRxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 15),
    _NncExtSVCSigStatsRawRxInvalidMessage_Type()
)
nncExtSVCSigStatsRawRxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsRawRxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsRawRxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsRawRxTimerExpiration = _NncExtSVCSigStatsRawRxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 16),
    _NncExtSVCSigStatsRawRxTimerExpiration_Type()
)
nncExtSVCSigStatsRawRxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsRawRxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsRawRxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsRawRxNormalCallClr = _NncExtSVCSigStatsRawRxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 17),
    _NncExtSVCSigStatsRawRxNormalCallClr_Type()
)
nncExtSVCSigStatsRawRxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsRawRxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsRawRxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsRawRxOtherCauses = _NncExtSVCSigStatsRawRxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 18),
    _NncExtSVCSigStatsRawRxOtherCauses_Type()
)
nncExtSVCSigStatsRawRxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawRxOtherCauses.setStatus("current")
_NncExtSVCSigStatsRawTxCalledPtyEvents_Type = NncExtCalledPtyEventsType
_NncExtSVCSigStatsRawTxCalledPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsRawTxCalledPtyEvents = _NncExtSVCSigStatsRawTxCalledPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 19),
    _NncExtSVCSigStatsRawTxCalledPtyEvents_Type()
)
nncExtSVCSigStatsRawTxCalledPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxCalledPtyEvents.setStatus("current")
_NncExtSVCSigStatsRawTxCallingPtyEvents_Type = NncExtCallingPtyEventsType
_NncExtSVCSigStatsRawTxCallingPtyEvents_Object = MibTableColumn
nncExtSVCSigStatsRawTxCallingPtyEvents = _NncExtSVCSigStatsRawTxCallingPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 20),
    _NncExtSVCSigStatsRawTxCallingPtyEvents_Type()
)
nncExtSVCSigStatsRawTxCallingPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxCallingPtyEvents.setStatus("current")
_NncExtSVCSigStatsRawTxResUnavailable_Type = NncExtResUnavailableType
_NncExtSVCSigStatsRawTxResUnavailable_Object = MibTableColumn
nncExtSVCSigStatsRawTxResUnavailable = _NncExtSVCSigStatsRawTxResUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 21),
    _NncExtSVCSigStatsRawTxResUnavailable_Type()
)
nncExtSVCSigStatsRawTxResUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxResUnavailable.setStatus("current")
_NncExtSVCSigStatsRawTxRoutingFailure_Type = NncExtRoutingFailureType
_NncExtSVCSigStatsRawTxRoutingFailure_Object = MibTableColumn
nncExtSVCSigStatsRawTxRoutingFailure = _NncExtSVCSigStatsRawTxRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 22),
    _NncExtSVCSigStatsRawTxRoutingFailure_Type()
)
nncExtSVCSigStatsRawTxRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxRoutingFailure.setStatus("current")
_NncExtSVCSigStatsRawTxInvalidMessage_Type = NncExtInvalidMessageType
_NncExtSVCSigStatsRawTxInvalidMessage_Object = MibTableColumn
nncExtSVCSigStatsRawTxInvalidMessage = _NncExtSVCSigStatsRawTxInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 23),
    _NncExtSVCSigStatsRawTxInvalidMessage_Type()
)
nncExtSVCSigStatsRawTxInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxInvalidMessage.setStatus("current")
_NncExtSVCSigStatsRawTxTimerExpiration_Type = NncExtTimerExpirationType
_NncExtSVCSigStatsRawTxTimerExpiration_Object = MibTableColumn
nncExtSVCSigStatsRawTxTimerExpiration = _NncExtSVCSigStatsRawTxTimerExpiration_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 24),
    _NncExtSVCSigStatsRawTxTimerExpiration_Type()
)
nncExtSVCSigStatsRawTxTimerExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxTimerExpiration.setStatus("current")
_NncExtSVCSigStatsRawTxNormalCallClr_Type = NncExtNormalCallClrType
_NncExtSVCSigStatsRawTxNormalCallClr_Object = MibTableColumn
nncExtSVCSigStatsRawTxNormalCallClr = _NncExtSVCSigStatsRawTxNormalCallClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 25),
    _NncExtSVCSigStatsRawTxNormalCallClr_Type()
)
nncExtSVCSigStatsRawTxNormalCallClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxNormalCallClr.setStatus("current")
_NncExtSVCSigStatsRawTxOtherCauses_Type = NncExtOtherCausesType
_NncExtSVCSigStatsRawTxOtherCauses_Object = MibTableColumn
nncExtSVCSigStatsRawTxOtherCauses = _NncExtSVCSigStatsRawTxOtherCauses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 26),
    _NncExtSVCSigStatsRawTxOtherCauses_Type()
)
nncExtSVCSigStatsRawTxOtherCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawTxOtherCauses.setStatus("current")
_NncExtSVCSigStatsRawScreeningFailures_Type = NncExtScreeningFailuresType
_NncExtSVCSigStatsRawScreeningFailures_Object = MibTableColumn
nncExtSVCSigStatsRawScreeningFailures = _NncExtSVCSigStatsRawScreeningFailures_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 27),
    _NncExtSVCSigStatsRawScreeningFailures_Type()
)
nncExtSVCSigStatsRawScreeningFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawScreeningFailures.setStatus("current")
_NncExtSVCSigStatsRawInCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsRawInCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsRawInCDNSelectiveCalls = _NncExtSVCSigStatsRawInCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 28),
    _NncExtSVCSigStatsRawInCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsRawInCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawInCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsRawInCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsRawInCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsRawInCGNSelectiveCalls = _NncExtSVCSigStatsRawInCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 29),
    _NncExtSVCSigStatsRawInCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsRawInCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawInCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsRawOutCDNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsRawOutCDNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsRawOutCDNSelectiveCalls = _NncExtSVCSigStatsRawOutCDNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 30),
    _NncExtSVCSigStatsRawOutCDNSelectiveCalls_Type()
)
nncExtSVCSigStatsRawOutCDNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawOutCDNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsRawOutCGNSelectiveCalls_Type = NncExtSelectiveCallsType
_NncExtSVCSigStatsRawOutCGNSelectiveCalls_Object = MibTableColumn
nncExtSVCSigStatsRawOutCGNSelectiveCalls = _NncExtSVCSigStatsRawOutCGNSelectiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 1, 5, 1, 31),
    _NncExtSVCSigStatsRawOutCGNSelectiveCalls_Type()
)
nncExtSVCSigStatsRawOutCGNSelectiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawOutCGNSelectiveCalls.setStatus("current")
_NncExtSVCSigStatsTraps_ObjectIdentity = ObjectIdentity
nncExtSVCSigStatsTraps = _NncExtSVCSigStatsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 2)
)
_NncExtSVCSigStatsGroups_ObjectIdentity = ObjectIdentity
nncExtSVCSigStatsGroups = _NncExtSVCSigStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3)
)
_NncExtSVCSigStatsCompliances_ObjectIdentity = ObjectIdentity
nncExtSVCSigStatsCompliances = _NncExtSVCSigStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 4)
)

# Managed Objects groups

nncExtSVCSigStatsCurrShortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3, 1)
)
nncExtSVCSigStatsCurrShortGroup.setObjects(
      *(("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortIntvlState"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortAbsIntvlNumber"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortIntvlStartTime"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortIntvlDuration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortInSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortInConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortInTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortOutSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortOutConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortOutTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortRxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortTxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortScreeningFailures"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortInCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortInCGNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls"))
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrShortGroup.setStatus("current")

nncExtSVCSigStatsPrevShortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3, 2)
)
nncExtSVCSigStatsPrevShortGroup.setObjects(
      *(("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortIntvlState"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortAbsIntvlNumber"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortIntvlStartTime"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortIntvlDuration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortInSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortInConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortInTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortOutSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortOutConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortOutTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortRxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortTxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortScreeningFailures"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortInCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortInCGNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls"))
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevShortGroup.setStatus("current")

nncExtSVCSigStatsCurrLongGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3, 3)
)
nncExtSVCSigStatsCurrLongGroup.setObjects(
      *(("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongIntvlState"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongAbsIntvlNumber"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongIntvlStartTime"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongIntvlDuration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongInSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongInConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongInTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongOutSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongOutConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongOutTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongRxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongTxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongScreeningFailures"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongInCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongInCGNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls"))
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCurrLongGroup.setStatus("current")

nncExtSVCSigStatsPrevLongGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3, 4)
)
nncExtSVCSigStatsPrevLongGroup.setObjects(
      *(("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongIntvlState"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongAbsIntvlNumber"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongIntvlStartTime"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongIntvlDuration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongInSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongInConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongInTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongOutSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongOutConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongOutTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongRxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongTxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongScreeningFailures"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongInCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongInCGNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls"))
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsPrevLongGroup.setStatus("current")

nncExtSVCSigStatsRawGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 3, 5)
)
nncExtSVCSigStatsRawGroup.setObjects(
      *(("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawState"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawStartTime"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawDuration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawActiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawInSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawInConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawInTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawOutSetupAttempts"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawOutConnectedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawOutTransitedCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawRxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxCalledPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxCallingPtyEvents"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxResUnavailable"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxRoutingFailure"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxInvalidMessage"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxTimerExpiration"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxNormalCallClr"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawTxOtherCauses"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawScreeningFailures"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawInCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawInCGNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawOutCDNSelectiveCalls"),
        ("NNCEXTSVCSIGSTATS-MIB", "nncExtSVCSigStatsRawOutCGNSelectiveCalls"))
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsRawGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncExtSVCSigStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 32, 4, 1)
)
if mibBuilder.loadTexts:
    nncExtSVCSigStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTSVCSIGSTATS-MIB",
    **{"NncExtSetupAttemptsType": NncExtSetupAttemptsType,
       "NncExtConnectedCallsType": NncExtConnectedCallsType,
       "NncExtTransitedCallsType": NncExtTransitedCallsType,
       "NncExtCalledPtyEventsType": NncExtCalledPtyEventsType,
       "NncExtCallingPtyEventsType": NncExtCallingPtyEventsType,
       "NncExtResUnavailableType": NncExtResUnavailableType,
       "NncExtRoutingFailureType": NncExtRoutingFailureType,
       "NncExtInvalidMessageType": NncExtInvalidMessageType,
       "NncExtTimerExpirationType": NncExtTimerExpirationType,
       "NncExtNormalCallClrType": NncExtNormalCallClrType,
       "NncExtOtherCausesType": NncExtOtherCausesType,
       "NncExtScreeningFailuresType": NncExtScreeningFailuresType,
       "NncExtActiveCallsType": NncExtActiveCallsType,
       "NncExtSelectiveCallsType": NncExtSelectiveCallsType,
       "nncExtSVCSigStats": nncExtSVCSigStats,
       "nncExtSVCSigStatsObjects": nncExtSVCSigStatsObjects,
       "nncExtSVCSigStatsCurrShortTable": nncExtSVCSigStatsCurrShortTable,
       "nncExtSVCSigStatsCurrShortEntry": nncExtSVCSigStatsCurrShortEntry,
       "nncExtSVCSigStatsCurrShortIntvlState": nncExtSVCSigStatsCurrShortIntvlState,
       "nncExtSVCSigStatsCurrShortAbsIntvlNumber": nncExtSVCSigStatsCurrShortAbsIntvlNumber,
       "nncExtSVCSigStatsCurrShortIntvlStartTime": nncExtSVCSigStatsCurrShortIntvlStartTime,
       "nncExtSVCSigStatsCurrShortIntvlDuration": nncExtSVCSigStatsCurrShortIntvlDuration,
       "nncExtSVCSigStatsCurrShortInSetupAttempts": nncExtSVCSigStatsCurrShortInSetupAttempts,
       "nncExtSVCSigStatsCurrShortInConnectedCalls": nncExtSVCSigStatsCurrShortInConnectedCalls,
       "nncExtSVCSigStatsCurrShortInTransitedCalls": nncExtSVCSigStatsCurrShortInTransitedCalls,
       "nncExtSVCSigStatsCurrShortOutSetupAttempts": nncExtSVCSigStatsCurrShortOutSetupAttempts,
       "nncExtSVCSigStatsCurrShortOutConnectedCalls": nncExtSVCSigStatsCurrShortOutConnectedCalls,
       "nncExtSVCSigStatsCurrShortOutTransitedCalls": nncExtSVCSigStatsCurrShortOutTransitedCalls,
       "nncExtSVCSigStatsCurrShortRxCalledPtyEvents": nncExtSVCSigStatsCurrShortRxCalledPtyEvents,
       "nncExtSVCSigStatsCurrShortRxCallingPtyEvents": nncExtSVCSigStatsCurrShortRxCallingPtyEvents,
       "nncExtSVCSigStatsCurrShortRxResUnavailable": nncExtSVCSigStatsCurrShortRxResUnavailable,
       "nncExtSVCSigStatsCurrShortRxRoutingFailure": nncExtSVCSigStatsCurrShortRxRoutingFailure,
       "nncExtSVCSigStatsCurrShortRxInvalidMessage": nncExtSVCSigStatsCurrShortRxInvalidMessage,
       "nncExtSVCSigStatsCurrShortRxTimerExpiration": nncExtSVCSigStatsCurrShortRxTimerExpiration,
       "nncExtSVCSigStatsCurrShortRxNormalCallClr": nncExtSVCSigStatsCurrShortRxNormalCallClr,
       "nncExtSVCSigStatsCurrShortRxOtherCauses": nncExtSVCSigStatsCurrShortRxOtherCauses,
       "nncExtSVCSigStatsCurrShortTxCalledPtyEvents": nncExtSVCSigStatsCurrShortTxCalledPtyEvents,
       "nncExtSVCSigStatsCurrShortTxCallingPtyEvents": nncExtSVCSigStatsCurrShortTxCallingPtyEvents,
       "nncExtSVCSigStatsCurrShortTxResUnavailable": nncExtSVCSigStatsCurrShortTxResUnavailable,
       "nncExtSVCSigStatsCurrShortTxRoutingFailure": nncExtSVCSigStatsCurrShortTxRoutingFailure,
       "nncExtSVCSigStatsCurrShortTxInvalidMessage": nncExtSVCSigStatsCurrShortTxInvalidMessage,
       "nncExtSVCSigStatsCurrShortTxTimerExpiration": nncExtSVCSigStatsCurrShortTxTimerExpiration,
       "nncExtSVCSigStatsCurrShortTxNormalCallClr": nncExtSVCSigStatsCurrShortTxNormalCallClr,
       "nncExtSVCSigStatsCurrShortTxOtherCauses": nncExtSVCSigStatsCurrShortTxOtherCauses,
       "nncExtSVCSigStatsCurrShortScreeningFailures": nncExtSVCSigStatsCurrShortScreeningFailures,
       "nncExtSVCSigStatsCurrShortInCDNSelectiveCalls": nncExtSVCSigStatsCurrShortInCDNSelectiveCalls,
       "nncExtSVCSigStatsCurrShortInCGNSelectiveCalls": nncExtSVCSigStatsCurrShortInCGNSelectiveCalls,
       "nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls": nncExtSVCSigStatsCurrShortOutCDNSelectiveCalls,
       "nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls": nncExtSVCSigStatsCurrShortOutCGNSelectiveCalls,
       "nncExtSVCSigStatsPrevShortTable": nncExtSVCSigStatsPrevShortTable,
       "nncExtSVCSigStatsPrevShortEntry": nncExtSVCSigStatsPrevShortEntry,
       "nncExtSVCSigStatsPrevShortIntvlNumber": nncExtSVCSigStatsPrevShortIntvlNumber,
       "nncExtSVCSigStatsPrevShortIntvlState": nncExtSVCSigStatsPrevShortIntvlState,
       "nncExtSVCSigStatsPrevShortAbsIntvlNumber": nncExtSVCSigStatsPrevShortAbsIntvlNumber,
       "nncExtSVCSigStatsPrevShortIntvlStartTime": nncExtSVCSigStatsPrevShortIntvlStartTime,
       "nncExtSVCSigStatsPrevShortIntvlDuration": nncExtSVCSigStatsPrevShortIntvlDuration,
       "nncExtSVCSigStatsPrevShortInSetupAttempts": nncExtSVCSigStatsPrevShortInSetupAttempts,
       "nncExtSVCSigStatsPrevShortInConnectedCalls": nncExtSVCSigStatsPrevShortInConnectedCalls,
       "nncExtSVCSigStatsPrevShortInTransitedCalls": nncExtSVCSigStatsPrevShortInTransitedCalls,
       "nncExtSVCSigStatsPrevShortOutSetupAttempts": nncExtSVCSigStatsPrevShortOutSetupAttempts,
       "nncExtSVCSigStatsPrevShortOutConnectedCalls": nncExtSVCSigStatsPrevShortOutConnectedCalls,
       "nncExtSVCSigStatsPrevShortOutTransitedCalls": nncExtSVCSigStatsPrevShortOutTransitedCalls,
       "nncExtSVCSigStatsPrevShortRxCalledPtyEvents": nncExtSVCSigStatsPrevShortRxCalledPtyEvents,
       "nncExtSVCSigStatsPrevShortRxCallingPtyEvents": nncExtSVCSigStatsPrevShortRxCallingPtyEvents,
       "nncExtSVCSigStatsPrevShortRxResUnavailable": nncExtSVCSigStatsPrevShortRxResUnavailable,
       "nncExtSVCSigStatsPrevShortRxRoutingFailure": nncExtSVCSigStatsPrevShortRxRoutingFailure,
       "nncExtSVCSigStatsPrevShortRxInvalidMessage": nncExtSVCSigStatsPrevShortRxInvalidMessage,
       "nncExtSVCSigStatsPrevShortRxTimerExpiration": nncExtSVCSigStatsPrevShortRxTimerExpiration,
       "nncExtSVCSigStatsPrevShortRxNormalCallClr": nncExtSVCSigStatsPrevShortRxNormalCallClr,
       "nncExtSVCSigStatsPrevShortRxOtherCauses": nncExtSVCSigStatsPrevShortRxOtherCauses,
       "nncExtSVCSigStatsPrevShortTxCalledPtyEvents": nncExtSVCSigStatsPrevShortTxCalledPtyEvents,
       "nncExtSVCSigStatsPrevShortTxCallingPtyEvents": nncExtSVCSigStatsPrevShortTxCallingPtyEvents,
       "nncExtSVCSigStatsPrevShortTxResUnavailable": nncExtSVCSigStatsPrevShortTxResUnavailable,
       "nncExtSVCSigStatsPrevShortTxRoutingFailure": nncExtSVCSigStatsPrevShortTxRoutingFailure,
       "nncExtSVCSigStatsPrevShortTxInvalidMessage": nncExtSVCSigStatsPrevShortTxInvalidMessage,
       "nncExtSVCSigStatsPrevShortTxTimerExpiration": nncExtSVCSigStatsPrevShortTxTimerExpiration,
       "nncExtSVCSigStatsPrevShortTxNormalCallClr": nncExtSVCSigStatsPrevShortTxNormalCallClr,
       "nncExtSVCSigStatsPrevShortTxOtherCauses": nncExtSVCSigStatsPrevShortTxOtherCauses,
       "nncExtSVCSigStatsPrevShortScreeningFailures": nncExtSVCSigStatsPrevShortScreeningFailures,
       "nncExtSVCSigStatsPrevShortInCDNSelectiveCalls": nncExtSVCSigStatsPrevShortInCDNSelectiveCalls,
       "nncExtSVCSigStatsPrevShortInCGNSelectiveCalls": nncExtSVCSigStatsPrevShortInCGNSelectiveCalls,
       "nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls": nncExtSVCSigStatsPrevShortOutCDNSelectiveCalls,
       "nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls": nncExtSVCSigStatsPrevShortOutCGNSelectiveCalls,
       "nncExtSVCSigStatsCurrLongTable": nncExtSVCSigStatsCurrLongTable,
       "nncExtSVCSigStatsCurrLongEntry": nncExtSVCSigStatsCurrLongEntry,
       "nncExtSVCSigStatsCurrLongIntvlState": nncExtSVCSigStatsCurrLongIntvlState,
       "nncExtSVCSigStatsCurrLongAbsIntvlNumber": nncExtSVCSigStatsCurrLongAbsIntvlNumber,
       "nncExtSVCSigStatsCurrLongIntvlStartTime": nncExtSVCSigStatsCurrLongIntvlStartTime,
       "nncExtSVCSigStatsCurrLongIntvlDuration": nncExtSVCSigStatsCurrLongIntvlDuration,
       "nncExtSVCSigStatsCurrLongInSetupAttempts": nncExtSVCSigStatsCurrLongInSetupAttempts,
       "nncExtSVCSigStatsCurrLongInConnectedCalls": nncExtSVCSigStatsCurrLongInConnectedCalls,
       "nncExtSVCSigStatsCurrLongInTransitedCalls": nncExtSVCSigStatsCurrLongInTransitedCalls,
       "nncExtSVCSigStatsCurrLongOutSetupAttempts": nncExtSVCSigStatsCurrLongOutSetupAttempts,
       "nncExtSVCSigStatsCurrLongOutConnectedCalls": nncExtSVCSigStatsCurrLongOutConnectedCalls,
       "nncExtSVCSigStatsCurrLongOutTransitedCalls": nncExtSVCSigStatsCurrLongOutTransitedCalls,
       "nncExtSVCSigStatsCurrLongRxCalledPtyEvents": nncExtSVCSigStatsCurrLongRxCalledPtyEvents,
       "nncExtSVCSigStatsCurrLongRxCallingPtyEvents": nncExtSVCSigStatsCurrLongRxCallingPtyEvents,
       "nncExtSVCSigStatsCurrLongRxResUnavailable": nncExtSVCSigStatsCurrLongRxResUnavailable,
       "nncExtSVCSigStatsCurrLongRxRoutingFailure": nncExtSVCSigStatsCurrLongRxRoutingFailure,
       "nncExtSVCSigStatsCurrLongRxInvalidMessage": nncExtSVCSigStatsCurrLongRxInvalidMessage,
       "nncExtSVCSigStatsCurrLongRxTimerExpiration": nncExtSVCSigStatsCurrLongRxTimerExpiration,
       "nncExtSVCSigStatsCurrLongRxNormalCallClr": nncExtSVCSigStatsCurrLongRxNormalCallClr,
       "nncExtSVCSigStatsCurrLongRxOtherCauses": nncExtSVCSigStatsCurrLongRxOtherCauses,
       "nncExtSVCSigStatsCurrLongTxCalledPtyEvents": nncExtSVCSigStatsCurrLongTxCalledPtyEvents,
       "nncExtSVCSigStatsCurrLongTxCallingPtyEvents": nncExtSVCSigStatsCurrLongTxCallingPtyEvents,
       "nncExtSVCSigStatsCurrLongTxResUnavailable": nncExtSVCSigStatsCurrLongTxResUnavailable,
       "nncExtSVCSigStatsCurrLongTxRoutingFailure": nncExtSVCSigStatsCurrLongTxRoutingFailure,
       "nncExtSVCSigStatsCurrLongTxInvalidMessage": nncExtSVCSigStatsCurrLongTxInvalidMessage,
       "nncExtSVCSigStatsCurrLongTxTimerExpiration": nncExtSVCSigStatsCurrLongTxTimerExpiration,
       "nncExtSVCSigStatsCurrLongTxNormalCallClr": nncExtSVCSigStatsCurrLongTxNormalCallClr,
       "nncExtSVCSigStatsCurrLongTxOtherCauses": nncExtSVCSigStatsCurrLongTxOtherCauses,
       "nncExtSVCSigStatsCurrLongScreeningFailures": nncExtSVCSigStatsCurrLongScreeningFailures,
       "nncExtSVCSigStatsCurrLongInCDNSelectiveCalls": nncExtSVCSigStatsCurrLongInCDNSelectiveCalls,
       "nncExtSVCSigStatsCurrLongInCGNSelectiveCalls": nncExtSVCSigStatsCurrLongInCGNSelectiveCalls,
       "nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls": nncExtSVCSigStatsCurrLongOutCDNSelectiveCalls,
       "nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls": nncExtSVCSigStatsCurrLongOutCGNSelectiveCalls,
       "nncExtSVCSigStatsPrevLongTable": nncExtSVCSigStatsPrevLongTable,
       "nncExtSVCSigStatsPrevLongEntry": nncExtSVCSigStatsPrevLongEntry,
       "nncExtSVCSigStatsPrevLongIntvlNumber": nncExtSVCSigStatsPrevLongIntvlNumber,
       "nncExtSVCSigStatsPrevLongIntvlState": nncExtSVCSigStatsPrevLongIntvlState,
       "nncExtSVCSigStatsPrevLongAbsIntvlNumber": nncExtSVCSigStatsPrevLongAbsIntvlNumber,
       "nncExtSVCSigStatsPrevLongIntvlStartTime": nncExtSVCSigStatsPrevLongIntvlStartTime,
       "nncExtSVCSigStatsPrevLongIntvlDuration": nncExtSVCSigStatsPrevLongIntvlDuration,
       "nncExtSVCSigStatsPrevLongInSetupAttempts": nncExtSVCSigStatsPrevLongInSetupAttempts,
       "nncExtSVCSigStatsPrevLongInConnectedCalls": nncExtSVCSigStatsPrevLongInConnectedCalls,
       "nncExtSVCSigStatsPrevLongInTransitedCalls": nncExtSVCSigStatsPrevLongInTransitedCalls,
       "nncExtSVCSigStatsPrevLongOutSetupAttempts": nncExtSVCSigStatsPrevLongOutSetupAttempts,
       "nncExtSVCSigStatsPrevLongOutConnectedCalls": nncExtSVCSigStatsPrevLongOutConnectedCalls,
       "nncExtSVCSigStatsPrevLongOutTransitedCalls": nncExtSVCSigStatsPrevLongOutTransitedCalls,
       "nncExtSVCSigStatsPrevLongRxCalledPtyEvents": nncExtSVCSigStatsPrevLongRxCalledPtyEvents,
       "nncExtSVCSigStatsPrevLongRxCallingPtyEvents": nncExtSVCSigStatsPrevLongRxCallingPtyEvents,
       "nncExtSVCSigStatsPrevLongRxResUnavailable": nncExtSVCSigStatsPrevLongRxResUnavailable,
       "nncExtSVCSigStatsPrevLongRxRoutingFailure": nncExtSVCSigStatsPrevLongRxRoutingFailure,
       "nncExtSVCSigStatsPrevLongRxInvalidMessage": nncExtSVCSigStatsPrevLongRxInvalidMessage,
       "nncExtSVCSigStatsPrevLongRxTimerExpiration": nncExtSVCSigStatsPrevLongRxTimerExpiration,
       "nncExtSVCSigStatsPrevLongRxNormalCallClr": nncExtSVCSigStatsPrevLongRxNormalCallClr,
       "nncExtSVCSigStatsPrevLongRxOtherCauses": nncExtSVCSigStatsPrevLongRxOtherCauses,
       "nncExtSVCSigStatsPrevLongTxCalledPtyEvents": nncExtSVCSigStatsPrevLongTxCalledPtyEvents,
       "nncExtSVCSigStatsPrevLongTxCallingPtyEvents": nncExtSVCSigStatsPrevLongTxCallingPtyEvents,
       "nncExtSVCSigStatsPrevLongTxResUnavailable": nncExtSVCSigStatsPrevLongTxResUnavailable,
       "nncExtSVCSigStatsPrevLongTxRoutingFailure": nncExtSVCSigStatsPrevLongTxRoutingFailure,
       "nncExtSVCSigStatsPrevLongTxInvalidMessage": nncExtSVCSigStatsPrevLongTxInvalidMessage,
       "nncExtSVCSigStatsPrevLongTxTimerExpiration": nncExtSVCSigStatsPrevLongTxTimerExpiration,
       "nncExtSVCSigStatsPrevLongTxNormalCallClr": nncExtSVCSigStatsPrevLongTxNormalCallClr,
       "nncExtSVCSigStatsPrevLongTxOtherCauses": nncExtSVCSigStatsPrevLongTxOtherCauses,
       "nncExtSVCSigStatsPrevLongScreeningFailures": nncExtSVCSigStatsPrevLongScreeningFailures,
       "nncExtSVCSigStatsPrevLongInCDNSelectiveCalls": nncExtSVCSigStatsPrevLongInCDNSelectiveCalls,
       "nncExtSVCSigStatsPrevLongInCGNSelectiveCalls": nncExtSVCSigStatsPrevLongInCGNSelectiveCalls,
       "nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls": nncExtSVCSigStatsPrevLongOutCDNSelectiveCalls,
       "nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls": nncExtSVCSigStatsPrevLongOutCGNSelectiveCalls,
       "nncExtSVCSigStatsRawTable": nncExtSVCSigStatsRawTable,
       "nncExtSVCSigStatsRawEntry": nncExtSVCSigStatsRawEntry,
       "nncExtSVCSigStatsRawState": nncExtSVCSigStatsRawState,
       "nncExtSVCSigStatsRawStartTime": nncExtSVCSigStatsRawStartTime,
       "nncExtSVCSigStatsRawDuration": nncExtSVCSigStatsRawDuration,
       "nncExtSVCSigStatsRawActiveCalls": nncExtSVCSigStatsRawActiveCalls,
       "nncExtSVCSigStatsRawInSetupAttempts": nncExtSVCSigStatsRawInSetupAttempts,
       "nncExtSVCSigStatsRawInConnectedCalls": nncExtSVCSigStatsRawInConnectedCalls,
       "nncExtSVCSigStatsRawInTransitedCalls": nncExtSVCSigStatsRawInTransitedCalls,
       "nncExtSVCSigStatsRawOutSetupAttempts": nncExtSVCSigStatsRawOutSetupAttempts,
       "nncExtSVCSigStatsRawOutConnectedCalls": nncExtSVCSigStatsRawOutConnectedCalls,
       "nncExtSVCSigStatsRawOutTransitedCalls": nncExtSVCSigStatsRawOutTransitedCalls,
       "nncExtSVCSigStatsRawRxCalledPtyEvents": nncExtSVCSigStatsRawRxCalledPtyEvents,
       "nncExtSVCSigStatsRawRxCallingPtyEvents": nncExtSVCSigStatsRawRxCallingPtyEvents,
       "nncExtSVCSigStatsRawRxResUnavailable": nncExtSVCSigStatsRawRxResUnavailable,
       "nncExtSVCSigStatsRawRxRoutingFailure": nncExtSVCSigStatsRawRxRoutingFailure,
       "nncExtSVCSigStatsRawRxInvalidMessage": nncExtSVCSigStatsRawRxInvalidMessage,
       "nncExtSVCSigStatsRawRxTimerExpiration": nncExtSVCSigStatsRawRxTimerExpiration,
       "nncExtSVCSigStatsRawRxNormalCallClr": nncExtSVCSigStatsRawRxNormalCallClr,
       "nncExtSVCSigStatsRawRxOtherCauses": nncExtSVCSigStatsRawRxOtherCauses,
       "nncExtSVCSigStatsRawTxCalledPtyEvents": nncExtSVCSigStatsRawTxCalledPtyEvents,
       "nncExtSVCSigStatsRawTxCallingPtyEvents": nncExtSVCSigStatsRawTxCallingPtyEvents,
       "nncExtSVCSigStatsRawTxResUnavailable": nncExtSVCSigStatsRawTxResUnavailable,
       "nncExtSVCSigStatsRawTxRoutingFailure": nncExtSVCSigStatsRawTxRoutingFailure,
       "nncExtSVCSigStatsRawTxInvalidMessage": nncExtSVCSigStatsRawTxInvalidMessage,
       "nncExtSVCSigStatsRawTxTimerExpiration": nncExtSVCSigStatsRawTxTimerExpiration,
       "nncExtSVCSigStatsRawTxNormalCallClr": nncExtSVCSigStatsRawTxNormalCallClr,
       "nncExtSVCSigStatsRawTxOtherCauses": nncExtSVCSigStatsRawTxOtherCauses,
       "nncExtSVCSigStatsRawScreeningFailures": nncExtSVCSigStatsRawScreeningFailures,
       "nncExtSVCSigStatsRawInCDNSelectiveCalls": nncExtSVCSigStatsRawInCDNSelectiveCalls,
       "nncExtSVCSigStatsRawInCGNSelectiveCalls": nncExtSVCSigStatsRawInCGNSelectiveCalls,
       "nncExtSVCSigStatsRawOutCDNSelectiveCalls": nncExtSVCSigStatsRawOutCDNSelectiveCalls,
       "nncExtSVCSigStatsRawOutCGNSelectiveCalls": nncExtSVCSigStatsRawOutCGNSelectiveCalls,
       "nncExtSVCSigStatsTraps": nncExtSVCSigStatsTraps,
       "nncExtSVCSigStatsGroups": nncExtSVCSigStatsGroups,
       "nncExtSVCSigStatsCurrShortGroup": nncExtSVCSigStatsCurrShortGroup,
       "nncExtSVCSigStatsPrevShortGroup": nncExtSVCSigStatsPrevShortGroup,
       "nncExtSVCSigStatsCurrLongGroup": nncExtSVCSigStatsCurrLongGroup,
       "nncExtSVCSigStatsPrevLongGroup": nncExtSVCSigStatsPrevLongGroup,
       "nncExtSVCSigStatsRawGroup": nncExtSVCSigStatsRawGroup,
       "nncExtSVCSigStatsCompliances": nncExtSVCSigStatsCompliances,
       "nncExtSVCSigStatsCompliance": nncExtSVCSigStatsCompliance}
)
