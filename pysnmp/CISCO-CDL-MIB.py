# SNMP MIB module (CISCO-CDL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:09 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88)
)
ciscoCdlMIB.setRevisions(
        ("2002-10-02 00:00",
         "2002-05-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoCdlAggDefectIndStatus(Bits, TextualConvention):
    status = "current"


class CoCdlFlowDefectIndStatus(Bits, TextualConvention):
    status = "current"


class CoCdlNodeBehavior(Integer32, TextualConvention):
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
        *(("cdlRegenerator", 3),
          ("endOfAggPath", 1),
          ("endOfHop", 2))
    )



class CoCdlFlowIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CoCdlMIBNotifications_ObjectIdentity = ObjectIdentity
coCdlMIBNotifications = _CoCdlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 0)
)
_CoCdlMIBObjects_ObjectIdentity = ObjectIdentity
coCdlMIBObjects = _CoCdlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1)
)
_CoCdlBaseGroup_ObjectIdentity = ObjectIdentity
coCdlBaseGroup = _CoCdlBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1)
)
_CoCdlIntfTable_Object = MibTable
coCdlIntfTable = _CoCdlIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coCdlIntfTable.setStatus("current")
_CoCdlIntfEntry_Object = MibTableRow
coCdlIntfEntry = _CoCdlIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1)
)
coCdlIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coCdlIntfEntry.setStatus("current")
_CoCdlAdminStatus_Type = TruthValue
_CoCdlAdminStatus_Object = MibTableColumn
coCdlAdminStatus = _CoCdlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 1),
    _CoCdlAdminStatus_Type()
)
coCdlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlAdminStatus.setStatus("current")


class _CoCdlForceEndOfHop_Type(TruthValue):
    """Custom type coCdlForceEndOfHop based on TruthValue"""


_CoCdlForceEndOfHop_Object = MibTableColumn
coCdlForceEndOfHop = _CoCdlForceEndOfHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 2),
    _CoCdlForceEndOfHop_Type()
)
coCdlForceEndOfHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlForceEndOfHop.setStatus("current")
_CoCdlNodeBehavior_Type = CoCdlNodeBehavior
_CoCdlNodeBehavior_Object = MibTableColumn
coCdlNodeBehavior = _CoCdlNodeBehavior_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 3),
    _CoCdlNodeBehavior_Type()
)
coCdlNodeBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlNodeBehavior.setStatus("current")
_CoCdlRxAggDefectIndCurrStatus_Type = CoCdlAggDefectIndStatus
_CoCdlRxAggDefectIndCurrStatus_Object = MibTableColumn
coCdlRxAggDefectIndCurrStatus = _CoCdlRxAggDefectIndCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 4),
    _CoCdlRxAggDefectIndCurrStatus_Type()
)
coCdlRxAggDefectIndCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxAggDefectIndCurrStatus.setStatus("current")
_CoCdlRxAggDefectIndLastChange_Type = TimeStamp
_CoCdlRxAggDefectIndLastChange_Object = MibTableColumn
coCdlRxAggDefectIndLastChange = _CoCdlRxAggDefectIndLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 5),
    _CoCdlRxAggDefectIndLastChange_Type()
)
coCdlRxAggDefectIndLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxAggDefectIndLastChange.setStatus("current")
_CoCdlTxAggDefectIndCurrStatus_Type = CoCdlAggDefectIndStatus
_CoCdlTxAggDefectIndCurrStatus_Object = MibTableColumn
coCdlTxAggDefectIndCurrStatus = _CoCdlTxAggDefectIndCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 6),
    _CoCdlTxAggDefectIndCurrStatus_Type()
)
coCdlTxAggDefectIndCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlTxAggDefectIndCurrStatus.setStatus("current")
_CoCdlTxAggDefectIndLastChange_Type = TimeStamp
_CoCdlTxAggDefectIndLastChange_Object = MibTableColumn
coCdlTxAggDefectIndLastChange = _CoCdlTxAggDefectIndLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 7),
    _CoCdlTxAggDefectIndLastChange_Type()
)
coCdlTxAggDefectIndLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlTxAggDefectIndLastChange.setStatus("current")
_CoCdlTransmitMaxFlowIdentifier_Type = CoCdlFlowIdentifier
_CoCdlTransmitMaxFlowIdentifier_Object = MibTableColumn
coCdlTransmitMaxFlowIdentifier = _CoCdlTransmitMaxFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 8),
    _CoCdlTransmitMaxFlowIdentifier_Type()
)
coCdlTransmitMaxFlowIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlTransmitMaxFlowIdentifier.setStatus("current")
_CoCdlReceiveMaxFlowIdentifier_Type = CoCdlFlowIdentifier
_CoCdlReceiveMaxFlowIdentifier_Object = MibTableColumn
coCdlReceiveMaxFlowIdentifier = _CoCdlReceiveMaxFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 9),
    _CoCdlReceiveMaxFlowIdentifier_Type()
)
coCdlReceiveMaxFlowIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlReceiveMaxFlowIdentifier.setStatus("current")
_CoCdlRxHeaderCRCError_Type = Counter32
_CoCdlRxHeaderCRCError_Object = MibTableColumn
coCdlRxHeaderCRCError = _CoCdlRxHeaderCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 10),
    _CoCdlRxHeaderCRCError_Type()
)
coCdlRxHeaderCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxHeaderCRCError.setStatus("current")
_CoCdlRxHeaderCRCErrorOverflow_Type = Counter32
_CoCdlRxHeaderCRCErrorOverflow_Object = MibTableColumn
coCdlRxHeaderCRCErrorOverflow = _CoCdlRxHeaderCRCErrorOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 11),
    _CoCdlRxHeaderCRCErrorOverflow_Type()
)
coCdlRxHeaderCRCErrorOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxHeaderCRCErrorOverflow.setStatus("current")
_CoCdlHCRxHeaderCRCError_Type = Counter64
_CoCdlHCRxHeaderCRCError_Object = MibTableColumn
coCdlHCRxHeaderCRCError = _CoCdlHCRxHeaderCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 12),
    _CoCdlHCRxHeaderCRCError_Type()
)
coCdlHCRxHeaderCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlHCRxHeaderCRCError.setStatus("current")
_CoCdlRxInvalidFlowID_Type = Counter32
_CoCdlRxInvalidFlowID_Object = MibTableColumn
coCdlRxInvalidFlowID = _CoCdlRxInvalidFlowID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 13),
    _CoCdlRxInvalidFlowID_Type()
)
coCdlRxInvalidFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxInvalidFlowID.setStatus("current")
_CoCdlRxInvalidFlowIDOverflow_Type = Counter32
_CoCdlRxInvalidFlowIDOverflow_Object = MibTableColumn
coCdlRxInvalidFlowIDOverflow = _CoCdlRxInvalidFlowIDOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 14),
    _CoCdlRxInvalidFlowIDOverflow_Type()
)
coCdlRxInvalidFlowIDOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxInvalidFlowIDOverflow.setStatus("current")
_CoCdlHCRxInvalidFlowID_Type = Counter64
_CoCdlHCRxInvalidFlowID_Object = MibTableColumn
coCdlHCRxInvalidFlowID = _CoCdlHCRxInvalidFlowID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 15),
    _CoCdlHCRxInvalidFlowID_Type()
)
coCdlHCRxInvalidFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlHCRxInvalidFlowID.setStatus("current")
_CoCdlRxNonCdlPackets_Type = Counter32
_CoCdlRxNonCdlPackets_Object = MibTableColumn
coCdlRxNonCdlPackets = _CoCdlRxNonCdlPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 16),
    _CoCdlRxNonCdlPackets_Type()
)
coCdlRxNonCdlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxNonCdlPackets.setStatus("current")
_CoCdlRxNonCdlPacketsOverflow_Type = Counter32
_CoCdlRxNonCdlPacketsOverflow_Object = MibTableColumn
coCdlRxNonCdlPacketsOverflow = _CoCdlRxNonCdlPacketsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 17),
    _CoCdlRxNonCdlPacketsOverflow_Type()
)
coCdlRxNonCdlPacketsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlRxNonCdlPacketsOverflow.setStatus("current")
_CoCdlHCRxNonCdlPackets_Type = Counter64
_CoCdlHCRxNonCdlPackets_Object = MibTableColumn
coCdlHCRxNonCdlPackets = _CoCdlHCRxNonCdlPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 18),
    _CoCdlHCRxNonCdlPackets_Type()
)
coCdlHCRxNonCdlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlHCRxNonCdlPackets.setStatus("current")


class _CoCdlDefectIndNotifyEnable_Type(Integer32):
    """Custom type coCdlDefectIndNotifyEnable based on Integer32"""
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
        *(("disabled", 1),
          ("enabledAtAllInterfaces", 3),
          ("enabledAtTerminatingInterfaces", 2))
    )


_CoCdlDefectIndNotifyEnable_Type.__name__ = "Integer32"
_CoCdlDefectIndNotifyEnable_Object = MibScalar
coCdlDefectIndNotifyEnable = _CoCdlDefectIndNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 2),
    _CoCdlDefectIndNotifyEnable_Type()
)
coCdlDefectIndNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlDefectIndNotifyEnable.setStatus("current")


class _CoCdlDefectIndSetSoakInterval_Type(Unsigned32):
    """Custom type coCdlDefectIndSetSoakInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_CoCdlDefectIndSetSoakInterval_Type.__name__ = "Unsigned32"
_CoCdlDefectIndSetSoakInterval_Object = MibScalar
coCdlDefectIndSetSoakInterval = _CoCdlDefectIndSetSoakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 3),
    _CoCdlDefectIndSetSoakInterval_Type()
)
coCdlDefectIndSetSoakInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlDefectIndSetSoakInterval.setStatus("current")
if mibBuilder.loadTexts:
    coCdlDefectIndSetSoakInterval.setUnits("milliseconds")


class _CoCdlDefectIndClearSoakInterval_Type(Unsigned32):
    """Custom type coCdlDefectIndClearSoakInterval based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_CoCdlDefectIndClearSoakInterval_Type.__name__ = "Unsigned32"
_CoCdlDefectIndClearSoakInterval_Object = MibScalar
coCdlDefectIndClearSoakInterval = _CoCdlDefectIndClearSoakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 4),
    _CoCdlDefectIndClearSoakInterval_Type()
)
coCdlDefectIndClearSoakInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlDefectIndClearSoakInterval.setStatus("current")
if mibBuilder.loadTexts:
    coCdlDefectIndClearSoakInterval.setUnits("milliseconds")


class _CoCdlDINotifyThrottleInterval_Type(Unsigned32):
    """Custom type coCdlDINotifyThrottleInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_CoCdlDINotifyThrottleInterval_Type.__name__ = "Unsigned32"
_CoCdlDINotifyThrottleInterval_Object = MibScalar
coCdlDINotifyThrottleInterval = _CoCdlDINotifyThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 5),
    _CoCdlDINotifyThrottleInterval_Type()
)
coCdlDINotifyThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlDINotifyThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    coCdlDINotifyThrottleInterval.setUnits("milliseconds")
_CoCdlFlowTermGroup_ObjectIdentity = ObjectIdentity
coCdlFlowTermGroup = _CoCdlFlowTermGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2)
)
_CoCdlFlowTermTable_Object = MibTable
coCdlFlowTermTable = _CoCdlFlowTermTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coCdlFlowTermTable.setStatus("current")
_CoCdlFlowTermEntry_Object = MibTableRow
coCdlFlowTermEntry = _CoCdlFlowTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1)
)
coCdlFlowTermEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coCdlFlowTermEntry.setStatus("current")
_CoCdlFromCdlNetFlowIdentifier_Type = CoCdlFlowIdentifier
_CoCdlFromCdlNetFlowIdentifier_Object = MibTableColumn
coCdlFromCdlNetFlowIdentifier = _CoCdlFromCdlNetFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 1),
    _CoCdlFromCdlNetFlowIdentifier_Type()
)
coCdlFromCdlNetFlowIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlFromCdlNetFlowIdentifier.setStatus("current")
_CoCdlToCdlNetFlowIdentifier_Type = CoCdlFlowIdentifier
_CoCdlToCdlNetFlowIdentifier_Object = MibTableColumn
coCdlToCdlNetFlowIdentifier = _CoCdlToCdlNetFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 2),
    _CoCdlToCdlNetFlowIdentifier_Type()
)
coCdlToCdlNetFlowIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCdlToCdlNetFlowIdentifier.setStatus("current")
_CoCdlFromCdlNetFlowDICurrStatus_Type = CoCdlFlowDefectIndStatus
_CoCdlFromCdlNetFlowDICurrStatus_Object = MibTableColumn
coCdlFromCdlNetFlowDICurrStatus = _CoCdlFromCdlNetFlowDICurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 3),
    _CoCdlFromCdlNetFlowDICurrStatus_Type()
)
coCdlFromCdlNetFlowDICurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlFromCdlNetFlowDICurrStatus.setStatus("current")
_CoCdlFromCdlNetFlowDILastChange_Type = TimeStamp
_CoCdlFromCdlNetFlowDILastChange_Object = MibTableColumn
coCdlFromCdlNetFlowDILastChange = _CoCdlFromCdlNetFlowDILastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 4),
    _CoCdlFromCdlNetFlowDILastChange_Type()
)
coCdlFromCdlNetFlowDILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlFromCdlNetFlowDILastChange.setStatus("current")
_CoCdlToCdlNetFlowDICurrStatus_Type = CoCdlFlowDefectIndStatus
_CoCdlToCdlNetFlowDICurrStatus_Object = MibTableColumn
coCdlToCdlNetFlowDICurrStatus = _CoCdlToCdlNetFlowDICurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 5),
    _CoCdlToCdlNetFlowDICurrStatus_Type()
)
coCdlToCdlNetFlowDICurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlToCdlNetFlowDICurrStatus.setStatus("current")
_CoCdlToCdlNetFlowDILastChange_Type = TimeStamp
_CoCdlToCdlNetFlowDILastChange_Object = MibTableColumn
coCdlToCdlNetFlowDILastChange = _CoCdlToCdlNetFlowDILastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 6),
    _CoCdlToCdlNetFlowDILastChange_Type()
)
coCdlToCdlNetFlowDILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlToCdlNetFlowDILastChange.setStatus("current")
_CoCdlFromCdlNetEthernetCRC_Type = Counter32
_CoCdlFromCdlNetEthernetCRC_Object = MibTableColumn
coCdlFromCdlNetEthernetCRC = _CoCdlFromCdlNetEthernetCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 7),
    _CoCdlFromCdlNetEthernetCRC_Type()
)
coCdlFromCdlNetEthernetCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlFromCdlNetEthernetCRC.setStatus("current")
_CoCdlFromCdlNetEthernetCRCOvrflw_Type = Counter32
_CoCdlFromCdlNetEthernetCRCOvrflw_Object = MibTableColumn
coCdlFromCdlNetEthernetCRCOvrflw = _CoCdlFromCdlNetEthernetCRCOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 8),
    _CoCdlFromCdlNetEthernetCRCOvrflw_Type()
)
coCdlFromCdlNetEthernetCRCOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlFromCdlNetEthernetCRCOvrflw.setStatus("current")
_CoCdlFromCdlNetHCEthernetCRC_Type = Counter64
_CoCdlFromCdlNetHCEthernetCRC_Object = MibTableColumn
coCdlFromCdlNetHCEthernetCRC = _CoCdlFromCdlNetHCEthernetCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 9),
    _CoCdlFromCdlNetHCEthernetCRC_Type()
)
coCdlFromCdlNetHCEthernetCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCdlFromCdlNetHCEthernetCRC.setStatus("current")
_CoCdlMIBConformance_ObjectIdentity = ObjectIdentity
coCdlMIBConformance = _CoCdlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3)
)
_CoCdlMIBCompliances_ObjectIdentity = ObjectIdentity
coCdlMIBCompliances = _CoCdlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1)
)
_CoCdlMIBGroups_ObjectIdentity = ObjectIdentity
coCdlMIBGroups = _CoCdlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2)
)

# Managed Objects groups

coCdlMIBBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 1)
)
coCdlMIBBaseGroup.setObjects(
      *(("CISCO-CDL-MIB", "coCdlAdminStatus"),
        ("CISCO-CDL-MIB", "coCdlNodeBehavior"),
        ("CISCO-CDL-MIB", "coCdlRxHeaderCRCError"),
        ("CISCO-CDL-MIB", "coCdlRxHeaderCRCErrorOverflow"),
        ("CISCO-CDL-MIB", "coCdlHCRxHeaderCRCError"),
        ("CISCO-CDL-MIB", "coCdlRxNonCdlPackets"),
        ("CISCO-CDL-MIB", "coCdlRxNonCdlPacketsOverflow"),
        ("CISCO-CDL-MIB", "coCdlHCRxNonCdlPackets"))
)
if mibBuilder.loadTexts:
    coCdlMIBBaseGroup.setStatus("current")

coCdlMIBFlowIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 2)
)
coCdlMIBFlowIdGroup.setObjects(
      *(("CISCO-CDL-MIB", "coCdlTransmitMaxFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlReceiveMaxFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlRxInvalidFlowID"),
        ("CISCO-CDL-MIB", "coCdlRxInvalidFlowIDOverflow"),
        ("CISCO-CDL-MIB", "coCdlHCRxInvalidFlowID"))
)
if mibBuilder.loadTexts:
    coCdlMIBFlowIdGroup.setStatus("current")

coCdlMIBFlowTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 3)
)
coCdlMIBFlowTermGroup.setObjects(
      *(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDICurrStatus"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDILastChange"))
)
if mibBuilder.loadTexts:
    coCdlMIBFlowTermGroup.setStatus("deprecated")

coCdlDIConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 4)
)
coCdlDIConfigGroup.setObjects(
    ("CISCO-CDL-MIB", "coCdlForceEndOfHop")
)
if mibBuilder.loadTexts:
    coCdlDIConfigGroup.setStatus("current")

coCdlDIAggMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 5)
)
coCdlDIAggMandatoryGroup.setObjects(
      *(("CISCO-CDL-MIB", "coCdlRxAggDefectIndCurrStatus"),
        ("CISCO-CDL-MIB", "coCdlRxAggDefectIndLastChange"),
        ("CISCO-CDL-MIB", "coCdlTxAggDefectIndCurrStatus"),
        ("CISCO-CDL-MIB", "coCdlTxAggDefectIndLastChange"),
        ("CISCO-CDL-MIB", "coCdlDefectIndNotifyEnable"),
        ("CISCO-CDL-MIB", "coCdlDefectIndSetSoakInterval"),
        ("CISCO-CDL-MIB", "coCdlDefectIndClearSoakInterval"),
        ("CISCO-CDL-MIB", "coCdlDINotifyThrottleInterval"))
)
if mibBuilder.loadTexts:
    coCdlDIAggMandatoryGroup.setStatus("current")

coCdlMIBFlowTerm2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 8)
)
coCdlMIBFlowTerm2Group.setObjects(
      *(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowIdentifier"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDICurrStatus"),
        ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDILastChange"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetEthernetCRC"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetEthernetCRCOvrflw"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetHCEthernetCRC"))
)
if mibBuilder.loadTexts:
    coCdlMIBFlowTerm2Group.setStatus("current")


# Notification objects

coCdlRxAggDefectIndChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 0, 1)
)
coCdlRxAggDefectIndChange.setObjects(
      *(("CISCO-CDL-MIB", "coCdlRxAggDefectIndCurrStatus"),
        ("CISCO-CDL-MIB", "coCdlRxAggDefectIndLastChange"))
)
if mibBuilder.loadTexts:
    coCdlRxAggDefectIndChange.setStatus(
        "current"
    )

coCdlFromCdlNetFlowDIChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 0, 2)
)
coCdlFromCdlNetFlowDIChange.setObjects(
      *(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"),
        ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"))
)
if mibBuilder.loadTexts:
    coCdlFromCdlNetFlowDIChange.setStatus(
        "current"
    )


# Notifications groups

coCdlDIAggNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 6)
)
coCdlDIAggNotifGroup.setObjects(
    ("CISCO-CDL-MIB", "coCdlRxAggDefectIndChange")
)
if mibBuilder.loadTexts:
    coCdlDIAggNotifGroup.setStatus(
        "current"
    )

coCdlDIFlowNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 7)
)
coCdlDIFlowNotifGroup.setObjects(
    ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDIChange")
)
if mibBuilder.loadTexts:
    coCdlDIFlowNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

coCdlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coCdlMIBCompliance.setStatus(
        "deprecated"
    )

coCdlMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1, 2)
)
if mibBuilder.loadTexts:
    coCdlMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDL-MIB",
    **{"CoCdlAggDefectIndStatus": CoCdlAggDefectIndStatus,
       "CoCdlFlowDefectIndStatus": CoCdlFlowDefectIndStatus,
       "CoCdlNodeBehavior": CoCdlNodeBehavior,
       "CoCdlFlowIdentifier": CoCdlFlowIdentifier,
       "ciscoCdlMIB": ciscoCdlMIB,
       "coCdlMIBNotifications": coCdlMIBNotifications,
       "coCdlRxAggDefectIndChange": coCdlRxAggDefectIndChange,
       "coCdlFromCdlNetFlowDIChange": coCdlFromCdlNetFlowDIChange,
       "coCdlMIBObjects": coCdlMIBObjects,
       "coCdlBaseGroup": coCdlBaseGroup,
       "coCdlIntfTable": coCdlIntfTable,
       "coCdlIntfEntry": coCdlIntfEntry,
       "coCdlAdminStatus": coCdlAdminStatus,
       "coCdlForceEndOfHop": coCdlForceEndOfHop,
       "coCdlNodeBehavior": coCdlNodeBehavior,
       "coCdlRxAggDefectIndCurrStatus": coCdlRxAggDefectIndCurrStatus,
       "coCdlRxAggDefectIndLastChange": coCdlRxAggDefectIndLastChange,
       "coCdlTxAggDefectIndCurrStatus": coCdlTxAggDefectIndCurrStatus,
       "coCdlTxAggDefectIndLastChange": coCdlTxAggDefectIndLastChange,
       "coCdlTransmitMaxFlowIdentifier": coCdlTransmitMaxFlowIdentifier,
       "coCdlReceiveMaxFlowIdentifier": coCdlReceiveMaxFlowIdentifier,
       "coCdlRxHeaderCRCError": coCdlRxHeaderCRCError,
       "coCdlRxHeaderCRCErrorOverflow": coCdlRxHeaderCRCErrorOverflow,
       "coCdlHCRxHeaderCRCError": coCdlHCRxHeaderCRCError,
       "coCdlRxInvalidFlowID": coCdlRxInvalidFlowID,
       "coCdlRxInvalidFlowIDOverflow": coCdlRxInvalidFlowIDOverflow,
       "coCdlHCRxInvalidFlowID": coCdlHCRxInvalidFlowID,
       "coCdlRxNonCdlPackets": coCdlRxNonCdlPackets,
       "coCdlRxNonCdlPacketsOverflow": coCdlRxNonCdlPacketsOverflow,
       "coCdlHCRxNonCdlPackets": coCdlHCRxNonCdlPackets,
       "coCdlDefectIndNotifyEnable": coCdlDefectIndNotifyEnable,
       "coCdlDefectIndSetSoakInterval": coCdlDefectIndSetSoakInterval,
       "coCdlDefectIndClearSoakInterval": coCdlDefectIndClearSoakInterval,
       "coCdlDINotifyThrottleInterval": coCdlDINotifyThrottleInterval,
       "coCdlFlowTermGroup": coCdlFlowTermGroup,
       "coCdlFlowTermTable": coCdlFlowTermTable,
       "coCdlFlowTermEntry": coCdlFlowTermEntry,
       "coCdlFromCdlNetFlowIdentifier": coCdlFromCdlNetFlowIdentifier,
       "coCdlToCdlNetFlowIdentifier": coCdlToCdlNetFlowIdentifier,
       "coCdlFromCdlNetFlowDICurrStatus": coCdlFromCdlNetFlowDICurrStatus,
       "coCdlFromCdlNetFlowDILastChange": coCdlFromCdlNetFlowDILastChange,
       "coCdlToCdlNetFlowDICurrStatus": coCdlToCdlNetFlowDICurrStatus,
       "coCdlToCdlNetFlowDILastChange": coCdlToCdlNetFlowDILastChange,
       "coCdlFromCdlNetEthernetCRC": coCdlFromCdlNetEthernetCRC,
       "coCdlFromCdlNetEthernetCRCOvrflw": coCdlFromCdlNetEthernetCRCOvrflw,
       "coCdlFromCdlNetHCEthernetCRC": coCdlFromCdlNetHCEthernetCRC,
       "coCdlMIBConformance": coCdlMIBConformance,
       "coCdlMIBCompliances": coCdlMIBCompliances,
       "coCdlMIBCompliance": coCdlMIBCompliance,
       "coCdlMIBCompliance2": coCdlMIBCompliance2,
       "coCdlMIBGroups": coCdlMIBGroups,
       "coCdlMIBBaseGroup": coCdlMIBBaseGroup,
       "coCdlMIBFlowIdGroup": coCdlMIBFlowIdGroup,
       "coCdlMIBFlowTermGroup": coCdlMIBFlowTermGroup,
       "coCdlDIConfigGroup": coCdlDIConfigGroup,
       "coCdlDIAggMandatoryGroup": coCdlDIAggMandatoryGroup,
       "coCdlDIAggNotifGroup": coCdlDIAggNotifGroup,
       "coCdlDIFlowNotifGroup": coCdlDIFlowNotifGroup,
       "coCdlMIBFlowTerm2Group": coCdlMIBFlowTerm2Group}
)
