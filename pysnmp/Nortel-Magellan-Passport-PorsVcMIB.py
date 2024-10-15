# SNMP MIB module (Nortel-Magellan-Passport-PorsVcMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-PorsVcMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:17 2024
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

(rtg,
 rtgIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-BaseRoutingMIB",
    "rtg",
    "rtgIndex")

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtgRs_ObjectIdentity = ObjectIdentity
rtgRs = _RtgRs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2)
)
_RtgRsRowStatusTable_Object = MibTable
rtgRsRowStatusTable = _RtgRsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1)
)
if mibBuilder.loadTexts:
    rtgRsRowStatusTable.setStatus("mandatory")
_RtgRsRowStatusEntry_Object = MibTableRow
rtgRsRowStatusEntry = _RtgRsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1, 1)
)
rtgRsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
)
if mibBuilder.loadTexts:
    rtgRsRowStatusEntry.setStatus("mandatory")
_RtgRsRowStatus_Type = RowStatus
_RtgRsRowStatus_Object = MibTableColumn
rtgRsRowStatus = _RtgRsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1, 1, 1),
    _RtgRsRowStatus_Type()
)
rtgRsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRowStatus.setStatus("mandatory")
_RtgRsComponentName_Type = DisplayString
_RtgRsComponentName_Object = MibTableColumn
rtgRsComponentName = _RtgRsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1, 1, 2),
    _RtgRsComponentName_Type()
)
rtgRsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsComponentName.setStatus("mandatory")
_RtgRsStorageType_Type = StorageType
_RtgRsStorageType_Object = MibTableColumn
rtgRsStorageType = _RtgRsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1, 1, 4),
    _RtgRsStorageType_Type()
)
rtgRsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsStorageType.setStatus("mandatory")
_RtgRsIndex_Type = NonReplicated
_RtgRsIndex_Object = MibTableColumn
rtgRsIndex = _RtgRsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 1, 1, 10),
    _RtgRsIndex_Type()
)
rtgRsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgRsIndex.setStatus("mandatory")
_RtgRsSelectedRouteTable_Object = MibTable
rtgRsSelectedRouteTable = _RtgRsSelectedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10)
)
if mibBuilder.loadTexts:
    rtgRsSelectedRouteTable.setStatus("mandatory")
_RtgRsSelectedRouteEntry_Object = MibTableRow
rtgRsSelectedRouteEntry = _RtgRsSelectedRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1)
)
rtgRsSelectedRouteEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
)
if mibBuilder.loadTexts:
    rtgRsSelectedRouteEntry.setStatus("mandatory")


class _RtgRsRouteCostMetric_Type(Unsigned32):
    """Custom type rtgRsRouteCostMetric based on Unsigned32"""
    defaultValue = 999999

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_RtgRsRouteCostMetric_Type.__name__ = "Unsigned32"
_RtgRsRouteCostMetric_Object = MibTableColumn
rtgRsRouteCostMetric = _RtgRsRouteCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 1),
    _RtgRsRouteCostMetric_Type()
)
rtgRsRouteCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRouteCostMetric.setStatus("mandatory")


class _RtgRsRouteDelayMetric_Type(Unsigned32):
    """Custom type rtgRsRouteDelayMetric based on Unsigned32"""
    defaultValue = 999999

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_RtgRsRouteDelayMetric_Type.__name__ = "Unsigned32"
_RtgRsRouteDelayMetric_Object = MibTableColumn
rtgRsRouteDelayMetric = _RtgRsRouteDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 2),
    _RtgRsRouteDelayMetric_Type()
)
rtgRsRouteDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRouteDelayMetric.setStatus("mandatory")


class _RtgRsBumpingPriority_Type(Unsigned32):
    """Custom type rtgRsBumpingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgRsBumpingPriority_Type.__name__ = "Unsigned32"
_RtgRsBumpingPriority_Object = MibTableColumn
rtgRsBumpingPriority = _RtgRsBumpingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 3),
    _RtgRsBumpingPriority_Type()
)
rtgRsBumpingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsBumpingPriority.setStatus("mandatory")


class _RtgRsReasonForNoRoute_Type(Integer32):
    """Custom type rtgRsReasonForNoRoute based on Integer32"""
    defaultValue = 0

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
              14)
        )
    )
    namedValues = NamedValues(
        *(("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("internalReason", 12),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routeDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_RtgRsReasonForNoRoute_Type.__name__ = "Integer32"
_RtgRsReasonForNoRoute_Object = MibTableColumn
rtgRsReasonForNoRoute = _RtgRsReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 4),
    _RtgRsReasonForNoRoute_Type()
)
rtgRsReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsReasonForNoRoute.setStatus("mandatory")


class _RtgRsAttributeNotMet_Type(Integer32):
    """Custom type rtgRsAttributeNotMet based on Integer32"""
    defaultValue = 1

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("allAttributesMet", 1),
          ("maximumAcceptableCost", 5),
          ("maximumAcceptableDelay", 6),
          ("maximumAcceptableGatewayCost", 12),
          ("maximumGatewayHops", 13),
          ("maximumTransmissionUnit", 11),
          ("permittedTrunkTypes", 8),
          ("requiredCustomerParm", 10),
          ("requiredRxBandwidth", 2),
          ("requiredSecurity", 9),
          ("requiredTrafficType", 7),
          ("requiredTrunkModes", 4),
          ("requiredTxBandwidth", 3),
          ("unknownAttributeNotMet", 0))
    )


_RtgRsAttributeNotMet_Type.__name__ = "Integer32"
_RtgRsAttributeNotMet_Object = MibTableColumn
rtgRsAttributeNotMet = _RtgRsAttributeNotMet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 5),
    _RtgRsAttributeNotMet_Type()
)
rtgRsAttributeNotMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsAttributeNotMet.setStatus("mandatory")


class _RtgRsRouteGatewayCostMetric_Type(Unsigned32):
    """Custom type rtgRsRouteGatewayCostMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_RtgRsRouteGatewayCostMetric_Type.__name__ = "Unsigned32"
_RtgRsRouteGatewayCostMetric_Object = MibTableColumn
rtgRsRouteGatewayCostMetric = _RtgRsRouteGatewayCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 6),
    _RtgRsRouteGatewayCostMetric_Type()
)
rtgRsRouteGatewayCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRouteGatewayCostMetric.setStatus("mandatory")


class _RtgRsRouteType_Type(Integer32):
    """Custom type rtgRsRouteType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
        *(("destinationNode", 5),
          ("destinationNodeLegacy", 6),
          ("gatewayLink", 8),
          ("gatewayNode", 7),
          ("manual", 10),
          ("noRoute", 3),
          ("routingGateway", 9),
          ("sameNode", 4))
    )


_RtgRsRouteType_Type.__name__ = "Integer32"
_RtgRsRouteType_Object = MibTableColumn
rtgRsRouteType = _RtgRsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 10, 1, 8),
    _RtgRsRouteType_Type()
)
rtgRsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRouteType.setStatus("mandatory")
_RtgRsControlsTable_Object = MibTable
rtgRsControlsTable = _RtgRsControlsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 11)
)
if mibBuilder.loadTexts:
    rtgRsControlsTable.setStatus("mandatory")
_RtgRsControlsEntry_Object = MibTableRow
rtgRsControlsEntry = _RtgRsControlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 11, 1)
)
rtgRsControlsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
)
if mibBuilder.loadTexts:
    rtgRsControlsEntry.setStatus("mandatory")


class _RtgRsRouteSelectionAttributes_Type(Integer32):
    """Custom type rtgRsRouteSelectionAttributes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fromLastRouteRequest", 1),
          ("fromOperator", 0))
    )


_RtgRsRouteSelectionAttributes_Type.__name__ = "Integer32"
_RtgRsRouteSelectionAttributes_Object = MibTableColumn
rtgRsRouteSelectionAttributes = _RtgRsRouteSelectionAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 11, 1, 1),
    _RtgRsRouteSelectionAttributes_Type()
)
rtgRsRouteSelectionAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRouteSelectionAttributes.setStatus("obsolete")


class _RtgRsOperationMode_Type(Integer32):
    """Custom type rtgRsOperationMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_RtgRsOperationMode_Type.__name__ = "Integer32"
_RtgRsOperationMode_Object = MibTableColumn
rtgRsOperationMode = _RtgRsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 11, 1, 2),
    _RtgRsOperationMode_Type()
)
rtgRsOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsOperationMode.setStatus("mandatory")


class _RtgRsLastRouteSelectionTime_Type(EnterpriseDateAndTime):
    """Custom type rtgRsLastRouteSelectionTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_RtgRsLastRouteSelectionTime_Type.__name__ = "EnterpriseDateAndTime"
_RtgRsLastRouteSelectionTime_Object = MibTableColumn
rtgRsLastRouteSelectionTime = _RtgRsLastRouteSelectionTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 11, 1, 3),
    _RtgRsLastRouteSelectionTime_Type()
)
rtgRsLastRouteSelectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsLastRouteSelectionTime.setStatus("mandatory")
_RtgRsPathAttributesTable_Object = MibTable
rtgRsPathAttributesTable = _RtgRsPathAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12)
)
if mibBuilder.loadTexts:
    rtgRsPathAttributesTable.setStatus("mandatory")
_RtgRsPathAttributesEntry_Object = MibTableRow
rtgRsPathAttributesEntry = _RtgRsPathAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1)
)
rtgRsPathAttributesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
)
if mibBuilder.loadTexts:
    rtgRsPathAttributesEntry.setStatus("mandatory")


class _RtgRsSourceId_Type(Unsigned32):
    """Custom type rtgRsSourceId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RtgRsSourceId_Type.__name__ = "Unsigned32"
_RtgRsSourceId_Object = MibTableColumn
rtgRsSourceId = _RtgRsSourceId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 1),
    _RtgRsSourceId_Type()
)
rtgRsSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsSourceId.setStatus("mandatory")


class _RtgRsRemoteName_Type(AsciiString):
    """Custom type rtgRsRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 40),
    )


_RtgRsRemoteName_Type.__name__ = "AsciiString"
_RtgRsRemoteName_Object = MibTableColumn
rtgRsRemoteName = _RtgRsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 2),
    _RtgRsRemoteName_Type()
)
rtgRsRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRemoteName.setStatus("obsolete")


class _RtgRsSetupPriority_Type(Unsigned32):
    """Custom type rtgRsSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgRsSetupPriority_Type.__name__ = "Unsigned32"
_RtgRsSetupPriority_Object = MibTableColumn
rtgRsSetupPriority = _RtgRsSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 3),
    _RtgRsSetupPriority_Type()
)
rtgRsSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsSetupPriority.setStatus("mandatory")


class _RtgRsRequiredTxBandwidth_Type(Unsigned32):
    """Custom type rtgRsRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgRsRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_RtgRsRequiredTxBandwidth_Object = MibTableColumn
rtgRsRequiredTxBandwidth = _RtgRsRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 4),
    _RtgRsRequiredTxBandwidth_Type()
)
rtgRsRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRequiredTxBandwidth.setStatus("mandatory")


class _RtgRsRequiredRxBandwidth_Type(Unsigned32):
    """Custom type rtgRsRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgRsRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_RtgRsRequiredRxBandwidth_Object = MibTableColumn
rtgRsRequiredRxBandwidth = _RtgRsRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 5),
    _RtgRsRequiredRxBandwidth_Type()
)
rtgRsRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRequiredRxBandwidth.setStatus("mandatory")


class _RtgRsMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type rtgRsMaximumTransmissionUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_RtgRsMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_RtgRsMaximumTransmissionUnit_Object = MibTableColumn
rtgRsMaximumTransmissionUnit = _RtgRsMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 6),
    _RtgRsMaximumTransmissionUnit_Type()
)
rtgRsMaximumTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsMaximumTransmissionUnit.setStatus("mandatory")


class _RtgRsSecurity_Type(Unsigned32):
    """Custom type rtgRsSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgRsSecurity_Type.__name__ = "Unsigned32"
_RtgRsSecurity_Object = MibTableColumn
rtgRsSecurity = _RtgRsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 7),
    _RtgRsSecurity_Type()
)
rtgRsSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsSecurity.setStatus("mandatory")


class _RtgRsTrafficType_Type(Integer32):
    """Custom type rtgRsTrafficType based on Integer32"""
    defaultValue = 0

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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_RtgRsTrafficType_Type.__name__ = "Integer32"
_RtgRsTrafficType_Object = MibTableColumn
rtgRsTrafficType = _RtgRsTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 8),
    _RtgRsTrafficType_Type()
)
rtgRsTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsTrafficType.setStatus("mandatory")


class _RtgRsPermittedTrunkTypes_Type(OctetString):
    """Custom type rtgRsPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RtgRsPermittedTrunkTypes_Type.__name__ = "OctetString"
_RtgRsPermittedTrunkTypes_Object = MibTableColumn
rtgRsPermittedTrunkTypes = _RtgRsPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 9),
    _RtgRsPermittedTrunkTypes_Type()
)
rtgRsPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsPermittedTrunkTypes.setStatus("mandatory")


class _RtgRsCustomerParameter_Type(Unsigned32):
    """Custom type rtgRsCustomerParameter based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgRsCustomerParameter_Type.__name__ = "Unsigned32"
_RtgRsCustomerParameter_Object = MibTableColumn
rtgRsCustomerParameter = _RtgRsCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 10),
    _RtgRsCustomerParameter_Type()
)
rtgRsCustomerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsCustomerParameter.setStatus("mandatory")


class _RtgRsPathAttributeToMinimize_Type(Integer32):
    """Custom type rtgRsPathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_RtgRsPathAttributeToMinimize_Type.__name__ = "Integer32"
_RtgRsPathAttributeToMinimize_Object = MibTableColumn
rtgRsPathAttributeToMinimize = _RtgRsPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 11),
    _RtgRsPathAttributeToMinimize_Type()
)
rtgRsPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsPathAttributeToMinimize.setStatus("mandatory")


class _RtgRsMaximumAcceptableCost_Type(Unsigned32):
    """Custom type rtgRsMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgRsMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_RtgRsMaximumAcceptableCost_Object = MibTableColumn
rtgRsMaximumAcceptableCost = _RtgRsMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 12),
    _RtgRsMaximumAcceptableCost_Type()
)
rtgRsMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsMaximumAcceptableCost.setStatus("mandatory")


class _RtgRsMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type rtgRsMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RtgRsMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_RtgRsMaximumAcceptableDelay_Object = MibTableColumn
rtgRsMaximumAcceptableDelay = _RtgRsMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 13),
    _RtgRsMaximumAcceptableDelay_Type()
)
rtgRsMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsMaximumAcceptableDelay.setStatus("mandatory")


class _RtgRsBumpPreference_Type(Integer32):
    """Custom type rtgRsBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_RtgRsBumpPreference_Type.__name__ = "Integer32"
_RtgRsBumpPreference_Object = MibTableColumn
rtgRsBumpPreference = _RtgRsBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 14),
    _RtgRsBumpPreference_Type()
)
rtgRsBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsBumpPreference.setStatus("mandatory")


class _RtgRsRequiredTrunkModes_Type(Integer32):
    """Custom type rtgRsRequiredTrunkModes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("mapping", 1))
    )


_RtgRsRequiredTrunkModes_Type.__name__ = "Integer32"
_RtgRsRequiredTrunkModes_Object = MibTableColumn
rtgRsRequiredTrunkModes = _RtgRsRequiredTrunkModes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 15),
    _RtgRsRequiredTrunkModes_Type()
)
rtgRsRequiredTrunkModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRequiredTrunkModes.setStatus("mandatory")


class _RtgRsMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type rtgRsMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgRsMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_RtgRsMaximumAcceptableGatewayCost_Object = MibTableColumn
rtgRsMaximumAcceptableGatewayCost = _RtgRsMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 16),
    _RtgRsMaximumAcceptableGatewayCost_Type()
)
rtgRsMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsMaximumAcceptableGatewayCost.setStatus("mandatory")


class _RtgRsRouteRequestor_Type(Integer32):
    """Custom type rtgRsRouteRequestor based on Integer32"""
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
        *(("applicationService", 0),
          ("inboundRGty", 1),
          ("outboundRGty", 2))
    )


_RtgRsRouteRequestor_Type.__name__ = "Integer32"
_RtgRsRouteRequestor_Object = MibTableColumn
rtgRsRouteRequestor = _RtgRsRouteRequestor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 17),
    _RtgRsRouteRequestor_Type()
)
rtgRsRouteRequestor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsRouteRequestor.setStatus("mandatory")


class _RtgRsGatewaySelectionAlg_Type(Integer32):
    """Custom type rtgRsGatewaySelectionAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("costBased", 1),
          ("legacy", 4),
          ("random", 2))
    )


_RtgRsGatewaySelectionAlg_Type.__name__ = "Integer32"
_RtgRsGatewaySelectionAlg_Object = MibTableColumn
rtgRsGatewaySelectionAlg = _RtgRsGatewaySelectionAlg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 18),
    _RtgRsGatewaySelectionAlg_Type()
)
rtgRsGatewaySelectionAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsGatewaySelectionAlg.setStatus("mandatory")


class _RtgRsDestination_Type(AsciiString):
    """Custom type rtgRsDestination based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_RtgRsDestination_Type.__name__ = "AsciiString"
_RtgRsDestination_Object = MibTableColumn
rtgRsDestination = _RtgRsDestination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 12, 1, 20),
    _RtgRsDestination_Type()
)
rtgRsDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRsDestination.setStatus("mandatory")
_RtgRsSrdTable_Object = MibTable
rtgRsSrdTable = _RtgRsSrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 224)
)
if mibBuilder.loadTexts:
    rtgRsSrdTable.setStatus("mandatory")
_RtgRsSrdEntry_Object = MibTableRow
rtgRsSrdEntry = _RtgRsSrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 224, 1)
)
rtgRsSrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsSrdIndex"),
)
if mibBuilder.loadTexts:
    rtgRsSrdEntry.setStatus("mandatory")


class _RtgRsSrdIndex_Type(Integer32):
    """Custom type rtgRsSrdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RtgRsSrdIndex_Type.__name__ = "Integer32"
_RtgRsSrdIndex_Object = MibTableColumn
rtgRsSrdIndex = _RtgRsSrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 224, 1, 1),
    _RtgRsSrdIndex_Type()
)
rtgRsSrdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgRsSrdIndex.setStatus("mandatory")


class _RtgRsSrdValue_Type(AsciiString):
    """Custom type rtgRsSrdValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtgRsSrdValue_Type.__name__ = "AsciiString"
_RtgRsSrdValue_Object = MibTableColumn
rtgRsSrdValue = _RtgRsSrdValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 224, 1, 2),
    _RtgRsSrdValue_Type()
)
rtgRsSrdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsSrdValue.setStatus("mandatory")
_RtgRsRouteStatisticsTable_Object = MibTable
rtgRsRouteStatisticsTable = _RtgRsRouteStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 225)
)
if mibBuilder.loadTexts:
    rtgRsRouteStatisticsTable.setStatus("mandatory")
_RtgRsRouteStatisticsEntry_Object = MibTableRow
rtgRsRouteStatisticsEntry = _RtgRsRouteStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 225, 1)
)
rtgRsRouteStatisticsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsRouteStatisticsSetupPriorityIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsRouteStatisticsStatisticsTableIndex"),
)
if mibBuilder.loadTexts:
    rtgRsRouteStatisticsEntry.setStatus("mandatory")


class _RtgRsRouteStatisticsSetupPriorityIndex_Type(Integer32):
    """Custom type rtgRsRouteStatisticsSetupPriorityIndex based on Integer32"""
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
        *(("routesRequested", 0),
          ("routesSelectedAtBp0", 1),
          ("routesSelectedAtBp1", 2),
          ("routesSelectedAtBp2", 3),
          ("routesSelectedAtBp3", 4),
          ("routesSelectedAtBp4", 5))
    )


_RtgRsRouteStatisticsSetupPriorityIndex_Type.__name__ = "Integer32"
_RtgRsRouteStatisticsSetupPriorityIndex_Object = MibTableColumn
rtgRsRouteStatisticsSetupPriorityIndex = _RtgRsRouteStatisticsSetupPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 225, 1, 1),
    _RtgRsRouteStatisticsSetupPriorityIndex_Type()
)
rtgRsRouteStatisticsSetupPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgRsRouteStatisticsSetupPriorityIndex.setStatus("mandatory")


class _RtgRsRouteStatisticsStatisticsTableIndex_Type(Integer32):
    """Custom type rtgRsRouteStatisticsStatisticsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgRsRouteStatisticsStatisticsTableIndex_Type.__name__ = "Integer32"
_RtgRsRouteStatisticsStatisticsTableIndex_Object = MibTableColumn
rtgRsRouteStatisticsStatisticsTableIndex = _RtgRsRouteStatisticsStatisticsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 225, 1, 2),
    _RtgRsRouteStatisticsStatisticsTableIndex_Type()
)
rtgRsRouteStatisticsStatisticsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgRsRouteStatisticsStatisticsTableIndex.setStatus("mandatory")


class _RtgRsRouteStatisticsValue_Type(Unsigned32):
    """Custom type rtgRsRouteStatisticsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgRsRouteStatisticsValue_Type.__name__ = "Unsigned32"
_RtgRsRouteStatisticsValue_Object = MibTableColumn
rtgRsRouteStatisticsValue = _RtgRsRouteStatisticsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 225, 1, 3),
    _RtgRsRouteStatisticsValue_Type()
)
rtgRsRouteStatisticsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsRouteStatisticsValue.setStatus("mandatory")
_RtgRsDgnTable_Object = MibTable
rtgRsDgnTable = _RtgRsDgnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 650)
)
if mibBuilder.loadTexts:
    rtgRsDgnTable.setStatus("mandatory")
_RtgRsDgnEntry_Object = MibTableRow
rtgRsDgnEntry = _RtgRsDgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 650, 1)
)
rtgRsDgnEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgRsDgnValue"),
)
if mibBuilder.loadTexts:
    rtgRsDgnEntry.setStatus("mandatory")


class _RtgRsDgnValue_Type(Integer32):
    """Custom type rtgRsDgnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RtgRsDgnValue_Type.__name__ = "Integer32"
_RtgRsDgnValue_Object = MibTableColumn
rtgRsDgnValue = _RtgRsDgnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 2, 650, 1, 1),
    _RtgRsDgnValue_Type()
)
rtgRsDgnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgRsDgnValue.setStatus("mandatory")
_RtgPors_ObjectIdentity = ObjectIdentity
rtgPors = _RtgPors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6)
)
_RtgPorsRowStatusTable_Object = MibTable
rtgPorsRowStatusTable = _RtgPorsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1)
)
if mibBuilder.loadTexts:
    rtgPorsRowStatusTable.setStatus("mandatory")
_RtgPorsRowStatusEntry_Object = MibTableRow
rtgPorsRowStatusEntry = _RtgPorsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1, 1)
)
rtgPorsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsRowStatusEntry.setStatus("mandatory")
_RtgPorsRowStatus_Type = RowStatus
_RtgPorsRowStatus_Object = MibTableColumn
rtgPorsRowStatus = _RtgPorsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1, 1, 1),
    _RtgPorsRowStatus_Type()
)
rtgPorsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsRowStatus.setStatus("mandatory")
_RtgPorsComponentName_Type = DisplayString
_RtgPorsComponentName_Object = MibTableColumn
rtgPorsComponentName = _RtgPorsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1, 1, 2),
    _RtgPorsComponentName_Type()
)
rtgPorsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsComponentName.setStatus("mandatory")
_RtgPorsStorageType_Type = StorageType
_RtgPorsStorageType_Object = MibTableColumn
rtgPorsStorageType = _RtgPorsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1, 1, 4),
    _RtgPorsStorageType_Type()
)
rtgPorsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsStorageType.setStatus("mandatory")
_RtgPorsIndex_Type = NonReplicated
_RtgPorsIndex_Object = MibTableColumn
rtgPorsIndex = _RtgPorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 1, 1, 10),
    _RtgPorsIndex_Type()
)
rtgPorsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgPorsIndex.setStatus("mandatory")
_RtgPorsProf_ObjectIdentity = ObjectIdentity
rtgPorsProf = _RtgPorsProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7)
)
_RtgPorsProfRowStatusTable_Object = MibTable
rtgPorsProfRowStatusTable = _RtgPorsProfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1)
)
if mibBuilder.loadTexts:
    rtgPorsProfRowStatusTable.setStatus("mandatory")
_RtgPorsProfRowStatusEntry_Object = MibTableRow
rtgPorsProfRowStatusEntry = _RtgPorsProfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1, 1)
)
rtgPorsProfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsProfIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsProfRowStatusEntry.setStatus("mandatory")
_RtgPorsProfRowStatus_Type = RowStatus
_RtgPorsProfRowStatus_Object = MibTableColumn
rtgPorsProfRowStatus = _RtgPorsProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1, 1, 1),
    _RtgPorsProfRowStatus_Type()
)
rtgPorsProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRowStatus.setStatus("mandatory")
_RtgPorsProfComponentName_Type = DisplayString
_RtgPorsProfComponentName_Object = MibTableColumn
rtgPorsProfComponentName = _RtgPorsProfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1, 1, 2),
    _RtgPorsProfComponentName_Type()
)
rtgPorsProfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsProfComponentName.setStatus("mandatory")
_RtgPorsProfStorageType_Type = StorageType
_RtgPorsProfStorageType_Object = MibTableColumn
rtgPorsProfStorageType = _RtgPorsProfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1, 1, 4),
    _RtgPorsProfStorageType_Type()
)
rtgPorsProfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsProfStorageType.setStatus("mandatory")


class _RtgPorsProfIndex_Type(Integer32):
    """Custom type rtgPorsProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtgPorsProfIndex_Type.__name__ = "Integer32"
_RtgPorsProfIndex_Object = MibTableColumn
rtgPorsProfIndex = _RtgPorsProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 1, 1, 10),
    _RtgPorsProfIndex_Type()
)
rtgPorsProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgPorsProfIndex.setStatus("mandatory")
_RtgPorsProfProvTable_Object = MibTable
rtgPorsProfProvTable = _RtgPorsProfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11)
)
if mibBuilder.loadTexts:
    rtgPorsProfProvTable.setStatus("mandatory")
_RtgPorsProfProvEntry_Object = MibTableRow
rtgPorsProfProvEntry = _RtgPorsProfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1)
)
rtgPorsProfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsProfIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsProfProvEntry.setStatus("mandatory")


class _RtgPorsProfSetupPriority_Type(Unsigned32):
    """Custom type rtgPorsProfSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgPorsProfSetupPriority_Type.__name__ = "Unsigned32"
_RtgPorsProfSetupPriority_Object = MibTableColumn
rtgPorsProfSetupPriority = _RtgPorsProfSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 3),
    _RtgPorsProfSetupPriority_Type()
)
rtgPorsProfSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfSetupPriority.setStatus("mandatory")


class _RtgPorsProfHoldingPriority_Type(Unsigned32):
    """Custom type rtgPorsProfHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgPorsProfHoldingPriority_Type.__name__ = "Unsigned32"
_RtgPorsProfHoldingPriority_Object = MibTableColumn
rtgPorsProfHoldingPriority = _RtgPorsProfHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 4),
    _RtgPorsProfHoldingPriority_Type()
)
rtgPorsProfHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfHoldingPriority.setStatus("mandatory")


class _RtgPorsProfRequiredTxBandwidth_Type(Unsigned32):
    """Custom type rtgPorsProfRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155520000),
    )


_RtgPorsProfRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_RtgPorsProfRequiredTxBandwidth_Object = MibTableColumn
rtgPorsProfRequiredTxBandwidth = _RtgPorsProfRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 5),
    _RtgPorsProfRequiredTxBandwidth_Type()
)
rtgPorsProfRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRequiredTxBandwidth.setStatus("mandatory")


class _RtgPorsProfRequiredRxBandwidth_Type(Unsigned32):
    """Custom type rtgPorsProfRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155520000),
    )


_RtgPorsProfRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_RtgPorsProfRequiredRxBandwidth_Object = MibTableColumn
rtgPorsProfRequiredRxBandwidth = _RtgPorsProfRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 6),
    _RtgPorsProfRequiredRxBandwidth_Type()
)
rtgPorsProfRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRequiredRxBandwidth.setStatus("mandatory")


class _RtgPorsProfRequiredTrafficType_Type(Integer32):
    """Custom type rtgPorsProfRequiredTrafficType based on Integer32"""
    defaultValue = 1

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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_RtgPorsProfRequiredTrafficType_Type.__name__ = "Integer32"
_RtgPorsProfRequiredTrafficType_Object = MibTableColumn
rtgPorsProfRequiredTrafficType = _RtgPorsProfRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 7),
    _RtgPorsProfRequiredTrafficType_Type()
)
rtgPorsProfRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRequiredTrafficType.setStatus("mandatory")


class _RtgPorsProfPermittedTrunkTypes_Type(OctetString):
    """Custom type rtgPorsProfPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RtgPorsProfPermittedTrunkTypes_Type.__name__ = "OctetString"
_RtgPorsProfPermittedTrunkTypes_Object = MibTableColumn
rtgPorsProfPermittedTrunkTypes = _RtgPorsProfPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 8),
    _RtgPorsProfPermittedTrunkTypes_Type()
)
rtgPorsProfPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfPermittedTrunkTypes.setStatus("mandatory")


class _RtgPorsProfRequiredSecurity_Type(Unsigned32):
    """Custom type rtgPorsProfRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgPorsProfRequiredSecurity_Type.__name__ = "Unsigned32"
_RtgPorsProfRequiredSecurity_Object = MibTableColumn
rtgPorsProfRequiredSecurity = _RtgPorsProfRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 9),
    _RtgPorsProfRequiredSecurity_Type()
)
rtgPorsProfRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRequiredSecurity.setStatus("mandatory")


class _RtgPorsProfRequiredCustomerParm_Type(Unsigned32):
    """Custom type rtgPorsProfRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgPorsProfRequiredCustomerParm_Type.__name__ = "Unsigned32"
_RtgPorsProfRequiredCustomerParm_Object = MibTableColumn
rtgPorsProfRequiredCustomerParm = _RtgPorsProfRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 10),
    _RtgPorsProfRequiredCustomerParm_Type()
)
rtgPorsProfRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfRequiredCustomerParm.setStatus("mandatory")


class _RtgPorsProfPathAttributeToMinimize_Type(Integer32):
    """Custom type rtgPorsProfPathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_RtgPorsProfPathAttributeToMinimize_Type.__name__ = "Integer32"
_RtgPorsProfPathAttributeToMinimize_Object = MibTableColumn
rtgPorsProfPathAttributeToMinimize = _RtgPorsProfPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 11),
    _RtgPorsProfPathAttributeToMinimize_Type()
)
rtgPorsProfPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfPathAttributeToMinimize.setStatus("mandatory")


class _RtgPorsProfMaximumAcceptableCost_Type(Unsigned32):
    """Custom type rtgPorsProfMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgPorsProfMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_RtgPorsProfMaximumAcceptableCost_Object = MibTableColumn
rtgPorsProfMaximumAcceptableCost = _RtgPorsProfMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 12),
    _RtgPorsProfMaximumAcceptableCost_Type()
)
rtgPorsProfMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfMaximumAcceptableCost.setStatus("mandatory")


class _RtgPorsProfMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type rtgPorsProfMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RtgPorsProfMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_RtgPorsProfMaximumAcceptableDelay_Object = MibTableColumn
rtgPorsProfMaximumAcceptableDelay = _RtgPorsProfMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 13),
    _RtgPorsProfMaximumAcceptableDelay_Type()
)
rtgPorsProfMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfMaximumAcceptableDelay.setStatus("mandatory")


class _RtgPorsProfEmissionPriority_Type(Integer32):
    """Custom type rtgPorsProfEmissionPriority based on Integer32"""
    defaultValue = 3

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
        *(("ep0", 0),
          ("ep1", 1),
          ("ep2", 2),
          ("sameAsApplication", 3))
    )


_RtgPorsProfEmissionPriority_Type.__name__ = "Integer32"
_RtgPorsProfEmissionPriority_Object = MibTableColumn
rtgPorsProfEmissionPriority = _RtgPorsProfEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 14),
    _RtgPorsProfEmissionPriority_Type()
)
rtgPorsProfEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfEmissionPriority.setStatus("mandatory")


class _RtgPorsProfDiscardPriority_Type(Integer32):
    """Custom type rtgPorsProfDiscardPriority based on Integer32"""
    defaultValue = 0

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
        *(("dp1", 1),
          ("dp2", 2),
          ("dp3", 3),
          ("sameAsApplication", 0))
    )


_RtgPorsProfDiscardPriority_Type.__name__ = "Integer32"
_RtgPorsProfDiscardPriority_Object = MibTableColumn
rtgPorsProfDiscardPriority = _RtgPorsProfDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 15),
    _RtgPorsProfDiscardPriority_Type()
)
rtgPorsProfDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfDiscardPriority.setStatus("mandatory")


class _RtgPorsProfPathFailureAction_Type(Integer32):
    """Custom type rtgPorsProfPathFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_RtgPorsProfPathFailureAction_Type.__name__ = "Integer32"
_RtgPorsProfPathFailureAction_Object = MibTableColumn
rtgPorsProfPathFailureAction = _RtgPorsProfPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 17),
    _RtgPorsProfPathFailureAction_Type()
)
rtgPorsProfPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfPathFailureAction.setStatus("mandatory")


class _RtgPorsProfBumpPreference_Type(Integer32):
    """Custom type rtgPorsProfBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_RtgPorsProfBumpPreference_Type.__name__ = "Integer32"
_RtgPorsProfBumpPreference_Object = MibTableColumn
rtgPorsProfBumpPreference = _RtgPorsProfBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 18),
    _RtgPorsProfBumpPreference_Type()
)
rtgPorsProfBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfBumpPreference.setStatus("mandatory")


class _RtgPorsProfOptimization_Type(Integer32):
    """Custom type rtgPorsProfOptimization based on Integer32"""
    defaultValue = 1

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


_RtgPorsProfOptimization_Type.__name__ = "Integer32"
_RtgPorsProfOptimization_Object = MibTableColumn
rtgPorsProfOptimization = _RtgPorsProfOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 11, 1, 19),
    _RtgPorsProfOptimization_Type()
)
rtgPorsProfOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsProfOptimization.setStatus("mandatory")
_RtgPorsProfUsrTable_Object = MibTable
rtgPorsProfUsrTable = _RtgPorsProfUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 400)
)
if mibBuilder.loadTexts:
    rtgPorsProfUsrTable.setStatus("mandatory")
_RtgPorsProfUsrEntry_Object = MibTableRow
rtgPorsProfUsrEntry = _RtgPorsProfUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 400, 1)
)
rtgPorsProfUsrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsProfIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsProfUsrValue"),
)
if mibBuilder.loadTexts:
    rtgPorsProfUsrEntry.setStatus("mandatory")
_RtgPorsProfUsrValue_Type = Link
_RtgPorsProfUsrValue_Object = MibTableColumn
rtgPorsProfUsrValue = _RtgPorsProfUsrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 7, 400, 1, 1),
    _RtgPorsProfUsrValue_Type()
)
rtgPorsProfUsrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsProfUsrValue.setStatus("mandatory")
_RtgPorsMpath_ObjectIdentity = ObjectIdentity
rtgPorsMpath = _RtgPorsMpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8)
)
_RtgPorsMpathRowStatusTable_Object = MibTable
rtgPorsMpathRowStatusTable = _RtgPorsMpathRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1)
)
if mibBuilder.loadTexts:
    rtgPorsMpathRowStatusTable.setStatus("mandatory")
_RtgPorsMpathRowStatusEntry_Object = MibTableRow
rtgPorsMpathRowStatusEntry = _RtgPorsMpathRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1, 1)
)
rtgPorsMpathRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsMpathRowStatusEntry.setStatus("mandatory")
_RtgPorsMpathRowStatus_Type = RowStatus
_RtgPorsMpathRowStatus_Object = MibTableColumn
rtgPorsMpathRowStatus = _RtgPorsMpathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1, 1, 1),
    _RtgPorsMpathRowStatus_Type()
)
rtgPorsMpathRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsMpathRowStatus.setStatus("mandatory")
_RtgPorsMpathComponentName_Type = DisplayString
_RtgPorsMpathComponentName_Object = MibTableColumn
rtgPorsMpathComponentName = _RtgPorsMpathComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1, 1, 2),
    _RtgPorsMpathComponentName_Type()
)
rtgPorsMpathComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathComponentName.setStatus("mandatory")
_RtgPorsMpathStorageType_Type = StorageType
_RtgPorsMpathStorageType_Object = MibTableColumn
rtgPorsMpathStorageType = _RtgPorsMpathStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1, 1, 4),
    _RtgPorsMpathStorageType_Type()
)
rtgPorsMpathStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathStorageType.setStatus("mandatory")


class _RtgPorsMpathIndex_Type(Integer32):
    """Custom type rtgPorsMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtgPorsMpathIndex_Type.__name__ = "Integer32"
_RtgPorsMpathIndex_Object = MibTableColumn
rtgPorsMpathIndex = _RtgPorsMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 1, 1, 10),
    _RtgPorsMpathIndex_Type()
)
rtgPorsMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgPorsMpathIndex.setStatus("mandatory")
_RtgPorsMpathOperTable_Object = MibTable
rtgPorsMpathOperTable = _RtgPorsMpathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 12)
)
if mibBuilder.loadTexts:
    rtgPorsMpathOperTable.setStatus("mandatory")
_RtgPorsMpathOperEntry_Object = MibTableRow
rtgPorsMpathOperEntry = _RtgPorsMpathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 12, 1)
)
rtgPorsMpathOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsMpathOperEntry.setStatus("mandatory")


class _RtgPorsMpathLastSetupFailureReason_Type(Integer32):
    """Custom type rtgPorsMpathLastSetupFailureReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              14,
              15,
              17,
              19,
              20,
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("operatorForced", 6),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14))
    )


_RtgPorsMpathLastSetupFailureReason_Type.__name__ = "Integer32"
_RtgPorsMpathLastSetupFailureReason_Object = MibTableColumn
rtgPorsMpathLastSetupFailureReason = _RtgPorsMpathLastSetupFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 12, 1, 1),
    _RtgPorsMpathLastSetupFailureReason_Type()
)
rtgPorsMpathLastSetupFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathLastSetupFailureReason.setStatus("mandatory")


class _RtgPorsMpathLastSetupFailurePoint_Type(AsciiString):
    """Custom type rtgPorsMpathLastSetupFailurePoint based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtgPorsMpathLastSetupFailurePoint_Type.__name__ = "AsciiString"
_RtgPorsMpathLastSetupFailurePoint_Object = MibTableColumn
rtgPorsMpathLastSetupFailurePoint = _RtgPorsMpathLastSetupFailurePoint_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 12, 1, 2),
    _RtgPorsMpathLastSetupFailurePoint_Type()
)
rtgPorsMpathLastSetupFailurePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathLastSetupFailurePoint.setStatus("mandatory")
_RtgPorsMpathLastSetupFailedUser_Type = RowPointer
_RtgPorsMpathLastSetupFailedUser_Object = MibTableColumn
rtgPorsMpathLastSetupFailedUser = _RtgPorsMpathLastSetupFailedUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 12, 1, 3),
    _RtgPorsMpathLastSetupFailedUser_Type()
)
rtgPorsMpathLastSetupFailedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathLastSetupFailedUser.setStatus("mandatory")
_RtgPorsMpathRouteTable_Object = MibTable
rtgPorsMpathRouteTable = _RtgPorsMpathRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 408)
)
if mibBuilder.loadTexts:
    rtgPorsMpathRouteTable.setStatus("mandatory")
_RtgPorsMpathRouteEntry_Object = MibTableRow
rtgPorsMpathRouteEntry = _RtgPorsMpathRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 408, 1)
)
rtgPorsMpathRouteEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathRouteIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsMpathRouteEntry.setStatus("mandatory")


class _RtgPorsMpathRouteIndex_Type(Integer32):
    """Custom type rtgPorsMpathRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_RtgPorsMpathRouteIndex_Type.__name__ = "Integer32"
_RtgPorsMpathRouteIndex_Object = MibTableColumn
rtgPorsMpathRouteIndex = _RtgPorsMpathRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 408, 1, 1),
    _RtgPorsMpathRouteIndex_Type()
)
rtgPorsMpathRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgPorsMpathRouteIndex.setStatus("mandatory")


class _RtgPorsMpathRouteValue_Type(AsciiString):
    """Custom type rtgPorsMpathRouteValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtgPorsMpathRouteValue_Type.__name__ = "AsciiString"
_RtgPorsMpathRouteValue_Object = MibTableColumn
rtgPorsMpathRouteValue = _RtgPorsMpathRouteValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 408, 1, 2),
    _RtgPorsMpathRouteValue_Type()
)
rtgPorsMpathRouteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsMpathRouteValue.setStatus("mandatory")
_RtgPorsMpathUsrTable_Object = MibTable
rtgPorsMpathUsrTable = _RtgPorsMpathUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 409)
)
if mibBuilder.loadTexts:
    rtgPorsMpathUsrTable.setStatus("mandatory")
_RtgPorsMpathUsrEntry_Object = MibTableRow
rtgPorsMpathUsrEntry = _RtgPorsMpathUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 409, 1)
)
rtgPorsMpathUsrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsMpathUsrValue"),
)
if mibBuilder.loadTexts:
    rtgPorsMpathUsrEntry.setStatus("mandatory")
_RtgPorsMpathUsrValue_Type = Link
_RtgPorsMpathUsrValue_Object = MibTableColumn
rtgPorsMpathUsrValue = _RtgPorsMpathUsrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 8, 409, 1, 1),
    _RtgPorsMpathUsrValue_Type()
)
rtgPorsMpathUsrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsMpathUsrValue.setStatus("mandatory")
_RtgPorsProvTable_Object = MibTable
rtgPorsProvTable = _RtgPorsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 10)
)
if mibBuilder.loadTexts:
    rtgPorsProvTable.setStatus("mandatory")
_RtgPorsProvEntry_Object = MibTableRow
rtgPorsProvEntry = _RtgPorsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 10, 1)
)
rtgPorsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsProvEntry.setStatus("mandatory")


class _RtgPorsOptimizationInterval_Type(Unsigned32):
    """Custom type rtgPorsOptimizationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_RtgPorsOptimizationInterval_Type.__name__ = "Unsigned32"
_RtgPorsOptimizationInterval_Object = MibTableColumn
rtgPorsOptimizationInterval = _RtgPorsOptimizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 10, 1, 1),
    _RtgPorsOptimizationInterval_Type()
)
rtgPorsOptimizationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgPorsOptimizationInterval.setStatus("mandatory")
_RtgPorsInfoTable_Object = MibTable
rtgPorsInfoTable = _RtgPorsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11)
)
if mibBuilder.loadTexts:
    rtgPorsInfoTable.setStatus("mandatory")
_RtgPorsInfoEntry_Object = MibTableRow
rtgPorsInfoEntry = _RtgPorsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1)
)
rtgPorsInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-PorsVcMIB", "rtgPorsIndex"),
)
if mibBuilder.loadTexts:
    rtgPorsInfoEntry.setStatus("mandatory")


class _RtgPorsActiveConnections_Type(Unsigned32):
    """Custom type rtgPorsActiveConnections based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgPorsActiveConnections_Type.__name__ = "Unsigned32"
_RtgPorsActiveConnections_Object = MibTableColumn
rtgPorsActiveConnections = _RtgPorsActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 1),
    _RtgPorsActiveConnections_Type()
)
rtgPorsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsActiveConnections.setStatus("mandatory")


class _RtgPorsOptimizationState_Type(Integer32):
    """Custom type rtgPorsOptimizationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("optimizing", 2),
          ("scheduled", 1))
    )


_RtgPorsOptimizationState_Type.__name__ = "Integer32"
_RtgPorsOptimizationState_Object = MibTableColumn
rtgPorsOptimizationState = _RtgPorsOptimizationState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 2),
    _RtgPorsOptimizationState_Type()
)
rtgPorsOptimizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsOptimizationState.setStatus("mandatory")


class _RtgPorsLastOptimizationTime_Type(EnterpriseDateAndTime):
    """Custom type rtgPorsLastOptimizationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_RtgPorsLastOptimizationTime_Type.__name__ = "EnterpriseDateAndTime"
_RtgPorsLastOptimizationTime_Object = MibTableColumn
rtgPorsLastOptimizationTime = _RtgPorsLastOptimizationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 3),
    _RtgPorsLastOptimizationTime_Type()
)
rtgPorsLastOptimizationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsLastOptimizationTime.setStatus("mandatory")


class _RtgPorsNextOptimizationTime_Type(EnterpriseDateAndTime):
    """Custom type rtgPorsNextOptimizationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_RtgPorsNextOptimizationTime_Type.__name__ = "EnterpriseDateAndTime"
_RtgPorsNextOptimizationTime_Object = MibTableColumn
rtgPorsNextOptimizationTime = _RtgPorsNextOptimizationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 4),
    _RtgPorsNextOptimizationTime_Type()
)
rtgPorsNextOptimizationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsNextOptimizationTime.setStatus("mandatory")


class _RtgPorsOptimizationPasses_Type(Unsigned32):
    """Custom type rtgPorsOptimizationPasses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgPorsOptimizationPasses_Type.__name__ = "Unsigned32"
_RtgPorsOptimizationPasses_Object = MibTableColumn
rtgPorsOptimizationPasses = _RtgPorsOptimizationPasses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 5),
    _RtgPorsOptimizationPasses_Type()
)
rtgPorsOptimizationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsOptimizationPasses.setStatus("mandatory")


class _RtgPorsOptimizationProgress_Type(Unsigned32):
    """Custom type rtgPorsOptimizationProgress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgPorsOptimizationProgress_Type.__name__ = "Unsigned32"
_RtgPorsOptimizationProgress_Object = MibTableColumn
rtgPorsOptimizationProgress = _RtgPorsOptimizationProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 6),
    _RtgPorsOptimizationProgress_Type()
)
rtgPorsOptimizationProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsOptimizationProgress.setStatus("mandatory")


class _RtgPorsPathsOptimized_Type(Unsigned32):
    """Custom type rtgPorsPathsOptimized based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgPorsPathsOptimized_Type.__name__ = "Unsigned32"
_RtgPorsPathsOptimized_Object = MibTableColumn
rtgPorsPathsOptimized = _RtgPorsPathsOptimized_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 7),
    _RtgPorsPathsOptimized_Type()
)
rtgPorsPathsOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsPathsOptimized.setStatus("mandatory")


class _RtgPorsTotalPathsOptimized_Type(Unsigned32):
    """Custom type rtgPorsTotalPathsOptimized based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgPorsTotalPathsOptimized_Type.__name__ = "Unsigned32"
_RtgPorsTotalPathsOptimized_Object = MibTableColumn
rtgPorsTotalPathsOptimized = _RtgPorsTotalPathsOptimized_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 6, 11, 1, 8),
    _RtgPorsTotalPathsOptimized_Type()
)
rtgPorsTotalPathsOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgPorsTotalPathsOptimized.setStatus("mandatory")
_PorsVcMIB_ObjectIdentity = ObjectIdentity
porsVcMIB = _PorsVcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37)
)
_PorsVcGroup_ObjectIdentity = ObjectIdentity
porsVcGroup = _PorsVcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 1)
)
_PorsVcGroupBE_ObjectIdentity = ObjectIdentity
porsVcGroupBE = _PorsVcGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 1, 5)
)
_PorsVcGroupBE00_ObjectIdentity = ObjectIdentity
porsVcGroupBE00 = _PorsVcGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 1, 5, 1)
)
_PorsVcGroupBE00A_ObjectIdentity = ObjectIdentity
porsVcGroupBE00A = _PorsVcGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 1, 5, 1, 2)
)
_PorsVcCapabilities_ObjectIdentity = ObjectIdentity
porsVcCapabilities = _PorsVcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 3)
)
_PorsVcCapabilitiesBE_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesBE = _PorsVcCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 3, 5)
)
_PorsVcCapabilitiesBE00_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesBE00 = _PorsVcCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 3, 5, 1)
)
_PorsVcCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesBE00A = _PorsVcCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 37, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-PorsVcMIB",
    **{"rtgRs": rtgRs,
       "rtgRsRowStatusTable": rtgRsRowStatusTable,
       "rtgRsRowStatusEntry": rtgRsRowStatusEntry,
       "rtgRsRowStatus": rtgRsRowStatus,
       "rtgRsComponentName": rtgRsComponentName,
       "rtgRsStorageType": rtgRsStorageType,
       "rtgRsIndex": rtgRsIndex,
       "rtgRsSelectedRouteTable": rtgRsSelectedRouteTable,
       "rtgRsSelectedRouteEntry": rtgRsSelectedRouteEntry,
       "rtgRsRouteCostMetric": rtgRsRouteCostMetric,
       "rtgRsRouteDelayMetric": rtgRsRouteDelayMetric,
       "rtgRsBumpingPriority": rtgRsBumpingPriority,
       "rtgRsReasonForNoRoute": rtgRsReasonForNoRoute,
       "rtgRsAttributeNotMet": rtgRsAttributeNotMet,
       "rtgRsRouteGatewayCostMetric": rtgRsRouteGatewayCostMetric,
       "rtgRsRouteType": rtgRsRouteType,
       "rtgRsControlsTable": rtgRsControlsTable,
       "rtgRsControlsEntry": rtgRsControlsEntry,
       "rtgRsRouteSelectionAttributes": rtgRsRouteSelectionAttributes,
       "rtgRsOperationMode": rtgRsOperationMode,
       "rtgRsLastRouteSelectionTime": rtgRsLastRouteSelectionTime,
       "rtgRsPathAttributesTable": rtgRsPathAttributesTable,
       "rtgRsPathAttributesEntry": rtgRsPathAttributesEntry,
       "rtgRsSourceId": rtgRsSourceId,
       "rtgRsRemoteName": rtgRsRemoteName,
       "rtgRsSetupPriority": rtgRsSetupPriority,
       "rtgRsRequiredTxBandwidth": rtgRsRequiredTxBandwidth,
       "rtgRsRequiredRxBandwidth": rtgRsRequiredRxBandwidth,
       "rtgRsMaximumTransmissionUnit": rtgRsMaximumTransmissionUnit,
       "rtgRsSecurity": rtgRsSecurity,
       "rtgRsTrafficType": rtgRsTrafficType,
       "rtgRsPermittedTrunkTypes": rtgRsPermittedTrunkTypes,
       "rtgRsCustomerParameter": rtgRsCustomerParameter,
       "rtgRsPathAttributeToMinimize": rtgRsPathAttributeToMinimize,
       "rtgRsMaximumAcceptableCost": rtgRsMaximumAcceptableCost,
       "rtgRsMaximumAcceptableDelay": rtgRsMaximumAcceptableDelay,
       "rtgRsBumpPreference": rtgRsBumpPreference,
       "rtgRsRequiredTrunkModes": rtgRsRequiredTrunkModes,
       "rtgRsMaximumAcceptableGatewayCost": rtgRsMaximumAcceptableGatewayCost,
       "rtgRsRouteRequestor": rtgRsRouteRequestor,
       "rtgRsGatewaySelectionAlg": rtgRsGatewaySelectionAlg,
       "rtgRsDestination": rtgRsDestination,
       "rtgRsSrdTable": rtgRsSrdTable,
       "rtgRsSrdEntry": rtgRsSrdEntry,
       "rtgRsSrdIndex": rtgRsSrdIndex,
       "rtgRsSrdValue": rtgRsSrdValue,
       "rtgRsRouteStatisticsTable": rtgRsRouteStatisticsTable,
       "rtgRsRouteStatisticsEntry": rtgRsRouteStatisticsEntry,
       "rtgRsRouteStatisticsSetupPriorityIndex": rtgRsRouteStatisticsSetupPriorityIndex,
       "rtgRsRouteStatisticsStatisticsTableIndex": rtgRsRouteStatisticsStatisticsTableIndex,
       "rtgRsRouteStatisticsValue": rtgRsRouteStatisticsValue,
       "rtgRsDgnTable": rtgRsDgnTable,
       "rtgRsDgnEntry": rtgRsDgnEntry,
       "rtgRsDgnValue": rtgRsDgnValue,
       "rtgPors": rtgPors,
       "rtgPorsRowStatusTable": rtgPorsRowStatusTable,
       "rtgPorsRowStatusEntry": rtgPorsRowStatusEntry,
       "rtgPorsRowStatus": rtgPorsRowStatus,
       "rtgPorsComponentName": rtgPorsComponentName,
       "rtgPorsStorageType": rtgPorsStorageType,
       "rtgPorsIndex": rtgPorsIndex,
       "rtgPorsProf": rtgPorsProf,
       "rtgPorsProfRowStatusTable": rtgPorsProfRowStatusTable,
       "rtgPorsProfRowStatusEntry": rtgPorsProfRowStatusEntry,
       "rtgPorsProfRowStatus": rtgPorsProfRowStatus,
       "rtgPorsProfComponentName": rtgPorsProfComponentName,
       "rtgPorsProfStorageType": rtgPorsProfStorageType,
       "rtgPorsProfIndex": rtgPorsProfIndex,
       "rtgPorsProfProvTable": rtgPorsProfProvTable,
       "rtgPorsProfProvEntry": rtgPorsProfProvEntry,
       "rtgPorsProfSetupPriority": rtgPorsProfSetupPriority,
       "rtgPorsProfHoldingPriority": rtgPorsProfHoldingPriority,
       "rtgPorsProfRequiredTxBandwidth": rtgPorsProfRequiredTxBandwidth,
       "rtgPorsProfRequiredRxBandwidth": rtgPorsProfRequiredRxBandwidth,
       "rtgPorsProfRequiredTrafficType": rtgPorsProfRequiredTrafficType,
       "rtgPorsProfPermittedTrunkTypes": rtgPorsProfPermittedTrunkTypes,
       "rtgPorsProfRequiredSecurity": rtgPorsProfRequiredSecurity,
       "rtgPorsProfRequiredCustomerParm": rtgPorsProfRequiredCustomerParm,
       "rtgPorsProfPathAttributeToMinimize": rtgPorsProfPathAttributeToMinimize,
       "rtgPorsProfMaximumAcceptableCost": rtgPorsProfMaximumAcceptableCost,
       "rtgPorsProfMaximumAcceptableDelay": rtgPorsProfMaximumAcceptableDelay,
       "rtgPorsProfEmissionPriority": rtgPorsProfEmissionPriority,
       "rtgPorsProfDiscardPriority": rtgPorsProfDiscardPriority,
       "rtgPorsProfPathFailureAction": rtgPorsProfPathFailureAction,
       "rtgPorsProfBumpPreference": rtgPorsProfBumpPreference,
       "rtgPorsProfOptimization": rtgPorsProfOptimization,
       "rtgPorsProfUsrTable": rtgPorsProfUsrTable,
       "rtgPorsProfUsrEntry": rtgPorsProfUsrEntry,
       "rtgPorsProfUsrValue": rtgPorsProfUsrValue,
       "rtgPorsMpath": rtgPorsMpath,
       "rtgPorsMpathRowStatusTable": rtgPorsMpathRowStatusTable,
       "rtgPorsMpathRowStatusEntry": rtgPorsMpathRowStatusEntry,
       "rtgPorsMpathRowStatus": rtgPorsMpathRowStatus,
       "rtgPorsMpathComponentName": rtgPorsMpathComponentName,
       "rtgPorsMpathStorageType": rtgPorsMpathStorageType,
       "rtgPorsMpathIndex": rtgPorsMpathIndex,
       "rtgPorsMpathOperTable": rtgPorsMpathOperTable,
       "rtgPorsMpathOperEntry": rtgPorsMpathOperEntry,
       "rtgPorsMpathLastSetupFailureReason": rtgPorsMpathLastSetupFailureReason,
       "rtgPorsMpathLastSetupFailurePoint": rtgPorsMpathLastSetupFailurePoint,
       "rtgPorsMpathLastSetupFailedUser": rtgPorsMpathLastSetupFailedUser,
       "rtgPorsMpathRouteTable": rtgPorsMpathRouteTable,
       "rtgPorsMpathRouteEntry": rtgPorsMpathRouteEntry,
       "rtgPorsMpathRouteIndex": rtgPorsMpathRouteIndex,
       "rtgPorsMpathRouteValue": rtgPorsMpathRouteValue,
       "rtgPorsMpathUsrTable": rtgPorsMpathUsrTable,
       "rtgPorsMpathUsrEntry": rtgPorsMpathUsrEntry,
       "rtgPorsMpathUsrValue": rtgPorsMpathUsrValue,
       "rtgPorsProvTable": rtgPorsProvTable,
       "rtgPorsProvEntry": rtgPorsProvEntry,
       "rtgPorsOptimizationInterval": rtgPorsOptimizationInterval,
       "rtgPorsInfoTable": rtgPorsInfoTable,
       "rtgPorsInfoEntry": rtgPorsInfoEntry,
       "rtgPorsActiveConnections": rtgPorsActiveConnections,
       "rtgPorsOptimizationState": rtgPorsOptimizationState,
       "rtgPorsLastOptimizationTime": rtgPorsLastOptimizationTime,
       "rtgPorsNextOptimizationTime": rtgPorsNextOptimizationTime,
       "rtgPorsOptimizationPasses": rtgPorsOptimizationPasses,
       "rtgPorsOptimizationProgress": rtgPorsOptimizationProgress,
       "rtgPorsPathsOptimized": rtgPorsPathsOptimized,
       "rtgPorsTotalPathsOptimized": rtgPorsTotalPathsOptimized,
       "porsVcMIB": porsVcMIB,
       "porsVcGroup": porsVcGroup,
       "porsVcGroupBE": porsVcGroupBE,
       "porsVcGroupBE00": porsVcGroupBE00,
       "porsVcGroupBE00A": porsVcGroupBE00A,
       "porsVcCapabilities": porsVcCapabilities,
       "porsVcCapabilitiesBE": porsVcCapabilitiesBE,
       "porsVcCapabilitiesBE00": porsVcCapabilitiesBE00,
       "porsVcCapabilitiesBE00A": porsVcCapabilitiesBE00A}
)
