# SNMP MIB module (Nortel-MsCarrier-MscPassport-PorsVcMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-PorsVcMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:57 2024
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

(mscRtg,
 mscRtgIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseRoutingMIB",
    "mscRtg",
    "mscRtgIndex")

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Link",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscRtgRs_ObjectIdentity = ObjectIdentity
mscRtgRs = _MscRtgRs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2)
)
_MscRtgRsRowStatusTable_Object = MibTable
mscRtgRsRowStatusTable = _MscRtgRsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgRsRowStatusTable.setStatus("mandatory")
_MscRtgRsRowStatusEntry_Object = MibTableRow
mscRtgRsRowStatusEntry = _MscRtgRsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1, 1)
)
mscRtgRsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsRowStatusEntry.setStatus("mandatory")
_MscRtgRsRowStatus_Type = RowStatus
_MscRtgRsRowStatus_Object = MibTableColumn
mscRtgRsRowStatus = _MscRtgRsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1, 1, 1),
    _MscRtgRsRowStatus_Type()
)
mscRtgRsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRowStatus.setStatus("mandatory")
_MscRtgRsComponentName_Type = DisplayString
_MscRtgRsComponentName_Object = MibTableColumn
mscRtgRsComponentName = _MscRtgRsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1, 1, 2),
    _MscRtgRsComponentName_Type()
)
mscRtgRsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsComponentName.setStatus("mandatory")
_MscRtgRsStorageType_Type = StorageType
_MscRtgRsStorageType_Object = MibTableColumn
mscRtgRsStorageType = _MscRtgRsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1, 1, 4),
    _MscRtgRsStorageType_Type()
)
mscRtgRsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsStorageType.setStatus("mandatory")
_MscRtgRsIndex_Type = NonReplicated
_MscRtgRsIndex_Object = MibTableColumn
mscRtgRsIndex = _MscRtgRsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 1, 1, 10),
    _MscRtgRsIndex_Type()
)
mscRtgRsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgRsIndex.setStatus("mandatory")
_MscRtgRsSelectedRouteTable_Object = MibTable
mscRtgRsSelectedRouteTable = _MscRtgRsSelectedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgRsSelectedRouteTable.setStatus("mandatory")
_MscRtgRsSelectedRouteEntry_Object = MibTableRow
mscRtgRsSelectedRouteEntry = _MscRtgRsSelectedRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1)
)
mscRtgRsSelectedRouteEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsSelectedRouteEntry.setStatus("mandatory")


class _MscRtgRsRouteCostMetric_Type(Unsigned32):
    """Custom type mscRtgRsRouteCostMetric based on Unsigned32"""
    defaultValue = 999999

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_MscRtgRsRouteCostMetric_Type.__name__ = "Unsigned32"
_MscRtgRsRouteCostMetric_Object = MibTableColumn
mscRtgRsRouteCostMetric = _MscRtgRsRouteCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 1),
    _MscRtgRsRouteCostMetric_Type()
)
mscRtgRsRouteCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRouteCostMetric.setStatus("mandatory")


class _MscRtgRsRouteDelayMetric_Type(Unsigned32):
    """Custom type mscRtgRsRouteDelayMetric based on Unsigned32"""
    defaultValue = 999999

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_MscRtgRsRouteDelayMetric_Type.__name__ = "Unsigned32"
_MscRtgRsRouteDelayMetric_Object = MibTableColumn
mscRtgRsRouteDelayMetric = _MscRtgRsRouteDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 2),
    _MscRtgRsRouteDelayMetric_Type()
)
mscRtgRsRouteDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRouteDelayMetric.setStatus("mandatory")


class _MscRtgRsBumpingPriority_Type(Unsigned32):
    """Custom type mscRtgRsBumpingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgRsBumpingPriority_Type.__name__ = "Unsigned32"
_MscRtgRsBumpingPriority_Object = MibTableColumn
mscRtgRsBumpingPriority = _MscRtgRsBumpingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 3),
    _MscRtgRsBumpingPriority_Type()
)
mscRtgRsBumpingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsBumpingPriority.setStatus("mandatory")


class _MscRtgRsReasonForNoRoute_Type(Integer32):
    """Custom type mscRtgRsReasonForNoRoute based on Integer32"""
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


_MscRtgRsReasonForNoRoute_Type.__name__ = "Integer32"
_MscRtgRsReasonForNoRoute_Object = MibTableColumn
mscRtgRsReasonForNoRoute = _MscRtgRsReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 4),
    _MscRtgRsReasonForNoRoute_Type()
)
mscRtgRsReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsReasonForNoRoute.setStatus("mandatory")


class _MscRtgRsAttributeNotMet_Type(Integer32):
    """Custom type mscRtgRsAttributeNotMet based on Integer32"""
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


_MscRtgRsAttributeNotMet_Type.__name__ = "Integer32"
_MscRtgRsAttributeNotMet_Object = MibTableColumn
mscRtgRsAttributeNotMet = _MscRtgRsAttributeNotMet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 5),
    _MscRtgRsAttributeNotMet_Type()
)
mscRtgRsAttributeNotMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsAttributeNotMet.setStatus("mandatory")


class _MscRtgRsRouteGatewayCostMetric_Type(Unsigned32):
    """Custom type mscRtgRsRouteGatewayCostMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_MscRtgRsRouteGatewayCostMetric_Type.__name__ = "Unsigned32"
_MscRtgRsRouteGatewayCostMetric_Object = MibTableColumn
mscRtgRsRouteGatewayCostMetric = _MscRtgRsRouteGatewayCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 6),
    _MscRtgRsRouteGatewayCostMetric_Type()
)
mscRtgRsRouteGatewayCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRouteGatewayCostMetric.setStatus("mandatory")


class _MscRtgRsRouteType_Type(Integer32):
    """Custom type mscRtgRsRouteType based on Integer32"""
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


_MscRtgRsRouteType_Type.__name__ = "Integer32"
_MscRtgRsRouteType_Object = MibTableColumn
mscRtgRsRouteType = _MscRtgRsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 10, 1, 8),
    _MscRtgRsRouteType_Type()
)
mscRtgRsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRouteType.setStatus("mandatory")
_MscRtgRsControlsTable_Object = MibTable
mscRtgRsControlsTable = _MscRtgRsControlsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 11)
)
if mibBuilder.loadTexts:
    mscRtgRsControlsTable.setStatus("mandatory")
_MscRtgRsControlsEntry_Object = MibTableRow
mscRtgRsControlsEntry = _MscRtgRsControlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 11, 1)
)
mscRtgRsControlsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsControlsEntry.setStatus("mandatory")


class _MscRtgRsRouteSelectionAttributes_Type(Integer32):
    """Custom type mscRtgRsRouteSelectionAttributes based on Integer32"""
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


_MscRtgRsRouteSelectionAttributes_Type.__name__ = "Integer32"
_MscRtgRsRouteSelectionAttributes_Object = MibTableColumn
mscRtgRsRouteSelectionAttributes = _MscRtgRsRouteSelectionAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 11, 1, 1),
    _MscRtgRsRouteSelectionAttributes_Type()
)
mscRtgRsRouteSelectionAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRouteSelectionAttributes.setStatus("obsolete")


class _MscRtgRsOperationMode_Type(Integer32):
    """Custom type mscRtgRsOperationMode based on Integer32"""
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


_MscRtgRsOperationMode_Type.__name__ = "Integer32"
_MscRtgRsOperationMode_Object = MibTableColumn
mscRtgRsOperationMode = _MscRtgRsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 11, 1, 2),
    _MscRtgRsOperationMode_Type()
)
mscRtgRsOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsOperationMode.setStatus("mandatory")


class _MscRtgRsLastRouteSelectionTime_Type(EnterpriseDateAndTime):
    """Custom type mscRtgRsLastRouteSelectionTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscRtgRsLastRouteSelectionTime_Type.__name__ = "EnterpriseDateAndTime"
_MscRtgRsLastRouteSelectionTime_Object = MibTableColumn
mscRtgRsLastRouteSelectionTime = _MscRtgRsLastRouteSelectionTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 11, 1, 3),
    _MscRtgRsLastRouteSelectionTime_Type()
)
mscRtgRsLastRouteSelectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsLastRouteSelectionTime.setStatus("mandatory")
_MscRtgRsPathAttributesTable_Object = MibTable
mscRtgRsPathAttributesTable = _MscRtgRsPathAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12)
)
if mibBuilder.loadTexts:
    mscRtgRsPathAttributesTable.setStatus("mandatory")
_MscRtgRsPathAttributesEntry_Object = MibTableRow
mscRtgRsPathAttributesEntry = _MscRtgRsPathAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1)
)
mscRtgRsPathAttributesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsPathAttributesEntry.setStatus("mandatory")


class _MscRtgRsSourceId_Type(Unsigned32):
    """Custom type mscRtgRsSourceId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_MscRtgRsSourceId_Type.__name__ = "Unsigned32"
_MscRtgRsSourceId_Object = MibTableColumn
mscRtgRsSourceId = _MscRtgRsSourceId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 1),
    _MscRtgRsSourceId_Type()
)
mscRtgRsSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsSourceId.setStatus("mandatory")


class _MscRtgRsRemoteName_Type(AsciiString):
    """Custom type mscRtgRsRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 40),
    )


_MscRtgRsRemoteName_Type.__name__ = "AsciiString"
_MscRtgRsRemoteName_Object = MibTableColumn
mscRtgRsRemoteName = _MscRtgRsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 2),
    _MscRtgRsRemoteName_Type()
)
mscRtgRsRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRemoteName.setStatus("obsolete")


class _MscRtgRsSetupPriority_Type(Unsigned32):
    """Custom type mscRtgRsSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgRsSetupPriority_Type.__name__ = "Unsigned32"
_MscRtgRsSetupPriority_Object = MibTableColumn
mscRtgRsSetupPriority = _MscRtgRsSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 3),
    _MscRtgRsSetupPriority_Type()
)
mscRtgRsSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsSetupPriority.setStatus("mandatory")


class _MscRtgRsRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscRtgRsRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgRsRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscRtgRsRequiredTxBandwidth_Object = MibTableColumn
mscRtgRsRequiredTxBandwidth = _MscRtgRsRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 4),
    _MscRtgRsRequiredTxBandwidth_Type()
)
mscRtgRsRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRequiredTxBandwidth.setStatus("mandatory")


class _MscRtgRsRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscRtgRsRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgRsRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscRtgRsRequiredRxBandwidth_Object = MibTableColumn
mscRtgRsRequiredRxBandwidth = _MscRtgRsRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 5),
    _MscRtgRsRequiredRxBandwidth_Type()
)
mscRtgRsRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRequiredRxBandwidth.setStatus("mandatory")


class _MscRtgRsMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type mscRtgRsMaximumTransmissionUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscRtgRsMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_MscRtgRsMaximumTransmissionUnit_Object = MibTableColumn
mscRtgRsMaximumTransmissionUnit = _MscRtgRsMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 6),
    _MscRtgRsMaximumTransmissionUnit_Type()
)
mscRtgRsMaximumTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsMaximumTransmissionUnit.setStatus("mandatory")


class _MscRtgRsSecurity_Type(Unsigned32):
    """Custom type mscRtgRsSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgRsSecurity_Type.__name__ = "Unsigned32"
_MscRtgRsSecurity_Object = MibTableColumn
mscRtgRsSecurity = _MscRtgRsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 7),
    _MscRtgRsSecurity_Type()
)
mscRtgRsSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsSecurity.setStatus("mandatory")


class _MscRtgRsTrafficType_Type(Integer32):
    """Custom type mscRtgRsTrafficType based on Integer32"""
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


_MscRtgRsTrafficType_Type.__name__ = "Integer32"
_MscRtgRsTrafficType_Object = MibTableColumn
mscRtgRsTrafficType = _MscRtgRsTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 8),
    _MscRtgRsTrafficType_Type()
)
mscRtgRsTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsTrafficType.setStatus("mandatory")


class _MscRtgRsPermittedTrunkTypes_Type(OctetString):
    """Custom type mscRtgRsPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscRtgRsPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscRtgRsPermittedTrunkTypes_Object = MibTableColumn
mscRtgRsPermittedTrunkTypes = _MscRtgRsPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 9),
    _MscRtgRsPermittedTrunkTypes_Type()
)
mscRtgRsPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsPermittedTrunkTypes.setStatus("mandatory")


class _MscRtgRsCustomerParameter_Type(Unsigned32):
    """Custom type mscRtgRsCustomerParameter based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgRsCustomerParameter_Type.__name__ = "Unsigned32"
_MscRtgRsCustomerParameter_Object = MibTableColumn
mscRtgRsCustomerParameter = _MscRtgRsCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 10),
    _MscRtgRsCustomerParameter_Type()
)
mscRtgRsCustomerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsCustomerParameter.setStatus("mandatory")


class _MscRtgRsPathAttributeToMinimize_Type(Integer32):
    """Custom type mscRtgRsPathAttributeToMinimize based on Integer32"""
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


_MscRtgRsPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscRtgRsPathAttributeToMinimize_Object = MibTableColumn
mscRtgRsPathAttributeToMinimize = _MscRtgRsPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 11),
    _MscRtgRsPathAttributeToMinimize_Type()
)
mscRtgRsPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsPathAttributeToMinimize.setStatus("mandatory")


class _MscRtgRsMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscRtgRsMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgRsMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscRtgRsMaximumAcceptableCost_Object = MibTableColumn
mscRtgRsMaximumAcceptableCost = _MscRtgRsMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 12),
    _MscRtgRsMaximumAcceptableCost_Type()
)
mscRtgRsMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsMaximumAcceptableCost.setStatus("mandatory")


class _MscRtgRsMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscRtgRsMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscRtgRsMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscRtgRsMaximumAcceptableDelay_Object = MibTableColumn
mscRtgRsMaximumAcceptableDelay = _MscRtgRsMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 13),
    _MscRtgRsMaximumAcceptableDelay_Type()
)
mscRtgRsMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsMaximumAcceptableDelay.setStatus("mandatory")


class _MscRtgRsBumpPreference_Type(Integer32):
    """Custom type mscRtgRsBumpPreference based on Integer32"""
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


_MscRtgRsBumpPreference_Type.__name__ = "Integer32"
_MscRtgRsBumpPreference_Object = MibTableColumn
mscRtgRsBumpPreference = _MscRtgRsBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 14),
    _MscRtgRsBumpPreference_Type()
)
mscRtgRsBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsBumpPreference.setStatus("mandatory")


class _MscRtgRsRequiredTrunkModes_Type(Integer32):
    """Custom type mscRtgRsRequiredTrunkModes based on Integer32"""
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


_MscRtgRsRequiredTrunkModes_Type.__name__ = "Integer32"
_MscRtgRsRequiredTrunkModes_Object = MibTableColumn
mscRtgRsRequiredTrunkModes = _MscRtgRsRequiredTrunkModes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 15),
    _MscRtgRsRequiredTrunkModes_Type()
)
mscRtgRsRequiredTrunkModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRequiredTrunkModes.setStatus("mandatory")


class _MscRtgRsMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type mscRtgRsMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgRsMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_MscRtgRsMaximumAcceptableGatewayCost_Object = MibTableColumn
mscRtgRsMaximumAcceptableGatewayCost = _MscRtgRsMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 16),
    _MscRtgRsMaximumAcceptableGatewayCost_Type()
)
mscRtgRsMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsMaximumAcceptableGatewayCost.setStatus("mandatory")


class _MscRtgRsRouteRequestor_Type(Integer32):
    """Custom type mscRtgRsRouteRequestor based on Integer32"""
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


_MscRtgRsRouteRequestor_Type.__name__ = "Integer32"
_MscRtgRsRouteRequestor_Object = MibTableColumn
mscRtgRsRouteRequestor = _MscRtgRsRouteRequestor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 17),
    _MscRtgRsRouteRequestor_Type()
)
mscRtgRsRouteRequestor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsRouteRequestor.setStatus("mandatory")


class _MscRtgRsGatewaySelectionAlg_Type(Integer32):
    """Custom type mscRtgRsGatewaySelectionAlg based on Integer32"""
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


_MscRtgRsGatewaySelectionAlg_Type.__name__ = "Integer32"
_MscRtgRsGatewaySelectionAlg_Object = MibTableColumn
mscRtgRsGatewaySelectionAlg = _MscRtgRsGatewaySelectionAlg_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 18),
    _MscRtgRsGatewaySelectionAlg_Type()
)
mscRtgRsGatewaySelectionAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsGatewaySelectionAlg.setStatus("mandatory")


class _MscRtgRsDestination_Type(AsciiString):
    """Custom type mscRtgRsDestination based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MscRtgRsDestination_Type.__name__ = "AsciiString"
_MscRtgRsDestination_Object = MibTableColumn
mscRtgRsDestination = _MscRtgRsDestination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 12, 1, 20),
    _MscRtgRsDestination_Type()
)
mscRtgRsDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRsDestination.setStatus("mandatory")
_MscRtgRsSrdTable_Object = MibTable
mscRtgRsSrdTable = _MscRtgRsSrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 224)
)
if mibBuilder.loadTexts:
    mscRtgRsSrdTable.setStatus("mandatory")
_MscRtgRsSrdEntry_Object = MibTableRow
mscRtgRsSrdEntry = _MscRtgRsSrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 224, 1)
)
mscRtgRsSrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsSrdIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsSrdEntry.setStatus("mandatory")


class _MscRtgRsSrdIndex_Type(Integer32):
    """Custom type mscRtgRsSrdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscRtgRsSrdIndex_Type.__name__ = "Integer32"
_MscRtgRsSrdIndex_Object = MibTableColumn
mscRtgRsSrdIndex = _MscRtgRsSrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 224, 1, 1),
    _MscRtgRsSrdIndex_Type()
)
mscRtgRsSrdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgRsSrdIndex.setStatus("mandatory")


class _MscRtgRsSrdValue_Type(AsciiString):
    """Custom type mscRtgRsSrdValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscRtgRsSrdValue_Type.__name__ = "AsciiString"
_MscRtgRsSrdValue_Object = MibTableColumn
mscRtgRsSrdValue = _MscRtgRsSrdValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 224, 1, 2),
    _MscRtgRsSrdValue_Type()
)
mscRtgRsSrdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsSrdValue.setStatus("mandatory")
_MscRtgRsRouteStatisticsTable_Object = MibTable
mscRtgRsRouteStatisticsTable = _MscRtgRsRouteStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 225)
)
if mibBuilder.loadTexts:
    mscRtgRsRouteStatisticsTable.setStatus("mandatory")
_MscRtgRsRouteStatisticsEntry_Object = MibTableRow
mscRtgRsRouteStatisticsEntry = _MscRtgRsRouteStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 225, 1)
)
mscRtgRsRouteStatisticsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsRouteStatisticsSetupPriorityIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsRouteStatisticsStatisticsTableIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRsRouteStatisticsEntry.setStatus("mandatory")


class _MscRtgRsRouteStatisticsSetupPriorityIndex_Type(Integer32):
    """Custom type mscRtgRsRouteStatisticsSetupPriorityIndex based on Integer32"""
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


_MscRtgRsRouteStatisticsSetupPriorityIndex_Type.__name__ = "Integer32"
_MscRtgRsRouteStatisticsSetupPriorityIndex_Object = MibTableColumn
mscRtgRsRouteStatisticsSetupPriorityIndex = _MscRtgRsRouteStatisticsSetupPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 225, 1, 1),
    _MscRtgRsRouteStatisticsSetupPriorityIndex_Type()
)
mscRtgRsRouteStatisticsSetupPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgRsRouteStatisticsSetupPriorityIndex.setStatus("mandatory")


class _MscRtgRsRouteStatisticsStatisticsTableIndex_Type(Integer32):
    """Custom type mscRtgRsRouteStatisticsStatisticsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgRsRouteStatisticsStatisticsTableIndex_Type.__name__ = "Integer32"
_MscRtgRsRouteStatisticsStatisticsTableIndex_Object = MibTableColumn
mscRtgRsRouteStatisticsStatisticsTableIndex = _MscRtgRsRouteStatisticsStatisticsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 225, 1, 2),
    _MscRtgRsRouteStatisticsStatisticsTableIndex_Type()
)
mscRtgRsRouteStatisticsStatisticsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgRsRouteStatisticsStatisticsTableIndex.setStatus("mandatory")


class _MscRtgRsRouteStatisticsValue_Type(Unsigned32):
    """Custom type mscRtgRsRouteStatisticsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgRsRouteStatisticsValue_Type.__name__ = "Unsigned32"
_MscRtgRsRouteStatisticsValue_Object = MibTableColumn
mscRtgRsRouteStatisticsValue = _MscRtgRsRouteStatisticsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 225, 1, 3),
    _MscRtgRsRouteStatisticsValue_Type()
)
mscRtgRsRouteStatisticsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsRouteStatisticsValue.setStatus("mandatory")
_MscRtgRsDgnTable_Object = MibTable
mscRtgRsDgnTable = _MscRtgRsDgnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 650)
)
if mibBuilder.loadTexts:
    mscRtgRsDgnTable.setStatus("mandatory")
_MscRtgRsDgnEntry_Object = MibTableRow
mscRtgRsDgnEntry = _MscRtgRsDgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 650, 1)
)
mscRtgRsDgnEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgRsDgnValue"),
)
if mibBuilder.loadTexts:
    mscRtgRsDgnEntry.setStatus("mandatory")


class _MscRtgRsDgnValue_Type(Integer32):
    """Custom type mscRtgRsDgnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscRtgRsDgnValue_Type.__name__ = "Integer32"
_MscRtgRsDgnValue_Object = MibTableColumn
mscRtgRsDgnValue = _MscRtgRsDgnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 2, 650, 1, 1),
    _MscRtgRsDgnValue_Type()
)
mscRtgRsDgnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgRsDgnValue.setStatus("mandatory")
_MscRtgPors_ObjectIdentity = ObjectIdentity
mscRtgPors = _MscRtgPors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6)
)
_MscRtgPorsRowStatusTable_Object = MibTable
mscRtgPorsRowStatusTable = _MscRtgPorsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1)
)
if mibBuilder.loadTexts:
    mscRtgPorsRowStatusTable.setStatus("mandatory")
_MscRtgPorsRowStatusEntry_Object = MibTableRow
mscRtgPorsRowStatusEntry = _MscRtgPorsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1, 1)
)
mscRtgPorsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsRowStatusEntry.setStatus("mandatory")
_MscRtgPorsRowStatus_Type = RowStatus
_MscRtgPorsRowStatus_Object = MibTableColumn
mscRtgPorsRowStatus = _MscRtgPorsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1, 1, 1),
    _MscRtgPorsRowStatus_Type()
)
mscRtgPorsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsRowStatus.setStatus("mandatory")
_MscRtgPorsComponentName_Type = DisplayString
_MscRtgPorsComponentName_Object = MibTableColumn
mscRtgPorsComponentName = _MscRtgPorsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1, 1, 2),
    _MscRtgPorsComponentName_Type()
)
mscRtgPorsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsComponentName.setStatus("mandatory")
_MscRtgPorsStorageType_Type = StorageType
_MscRtgPorsStorageType_Object = MibTableColumn
mscRtgPorsStorageType = _MscRtgPorsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1, 1, 4),
    _MscRtgPorsStorageType_Type()
)
mscRtgPorsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsStorageType.setStatus("mandatory")
_MscRtgPorsIndex_Type = NonReplicated
_MscRtgPorsIndex_Object = MibTableColumn
mscRtgPorsIndex = _MscRtgPorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 1, 1, 10),
    _MscRtgPorsIndex_Type()
)
mscRtgPorsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgPorsIndex.setStatus("mandatory")
_MscRtgPorsProf_ObjectIdentity = ObjectIdentity
mscRtgPorsProf = _MscRtgPorsProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7)
)
_MscRtgPorsProfRowStatusTable_Object = MibTable
mscRtgPorsProfRowStatusTable = _MscRtgPorsProfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mscRtgPorsProfRowStatusTable.setStatus("mandatory")
_MscRtgPorsProfRowStatusEntry_Object = MibTableRow
mscRtgPorsProfRowStatusEntry = _MscRtgPorsProfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1, 1)
)
mscRtgPorsProfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsProfIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsProfRowStatusEntry.setStatus("mandatory")
_MscRtgPorsProfRowStatus_Type = RowStatus
_MscRtgPorsProfRowStatus_Object = MibTableColumn
mscRtgPorsProfRowStatus = _MscRtgPorsProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1, 1, 1),
    _MscRtgPorsProfRowStatus_Type()
)
mscRtgPorsProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRowStatus.setStatus("mandatory")
_MscRtgPorsProfComponentName_Type = DisplayString
_MscRtgPorsProfComponentName_Object = MibTableColumn
mscRtgPorsProfComponentName = _MscRtgPorsProfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1, 1, 2),
    _MscRtgPorsProfComponentName_Type()
)
mscRtgPorsProfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsProfComponentName.setStatus("mandatory")
_MscRtgPorsProfStorageType_Type = StorageType
_MscRtgPorsProfStorageType_Object = MibTableColumn
mscRtgPorsProfStorageType = _MscRtgPorsProfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1, 1, 4),
    _MscRtgPorsProfStorageType_Type()
)
mscRtgPorsProfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsProfStorageType.setStatus("mandatory")


class _MscRtgPorsProfIndex_Type(Integer32):
    """Custom type mscRtgPorsProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscRtgPorsProfIndex_Type.__name__ = "Integer32"
_MscRtgPorsProfIndex_Object = MibTableColumn
mscRtgPorsProfIndex = _MscRtgPorsProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 1, 1, 10),
    _MscRtgPorsProfIndex_Type()
)
mscRtgPorsProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgPorsProfIndex.setStatus("mandatory")
_MscRtgPorsProfProvTable_Object = MibTable
mscRtgPorsProfProvTable = _MscRtgPorsProfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11)
)
if mibBuilder.loadTexts:
    mscRtgPorsProfProvTable.setStatus("mandatory")
_MscRtgPorsProfProvEntry_Object = MibTableRow
mscRtgPorsProfProvEntry = _MscRtgPorsProfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1)
)
mscRtgPorsProfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsProfIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsProfProvEntry.setStatus("mandatory")


class _MscRtgPorsProfSetupPriority_Type(Unsigned32):
    """Custom type mscRtgPorsProfSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgPorsProfSetupPriority_Type.__name__ = "Unsigned32"
_MscRtgPorsProfSetupPriority_Object = MibTableColumn
mscRtgPorsProfSetupPriority = _MscRtgPorsProfSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 3),
    _MscRtgPorsProfSetupPriority_Type()
)
mscRtgPorsProfSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfSetupPriority.setStatus("mandatory")


class _MscRtgPorsProfHoldingPriority_Type(Unsigned32):
    """Custom type mscRtgPorsProfHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgPorsProfHoldingPriority_Type.__name__ = "Unsigned32"
_MscRtgPorsProfHoldingPriority_Object = MibTableColumn
mscRtgPorsProfHoldingPriority = _MscRtgPorsProfHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 4),
    _MscRtgPorsProfHoldingPriority_Type()
)
mscRtgPorsProfHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfHoldingPriority.setStatus("mandatory")


class _MscRtgPorsProfRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscRtgPorsProfRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155520000),
    )


_MscRtgPorsProfRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscRtgPorsProfRequiredTxBandwidth_Object = MibTableColumn
mscRtgPorsProfRequiredTxBandwidth = _MscRtgPorsProfRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 5),
    _MscRtgPorsProfRequiredTxBandwidth_Type()
)
mscRtgPorsProfRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRequiredTxBandwidth.setStatus("mandatory")


class _MscRtgPorsProfRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscRtgPorsProfRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155520000),
    )


_MscRtgPorsProfRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscRtgPorsProfRequiredRxBandwidth_Object = MibTableColumn
mscRtgPorsProfRequiredRxBandwidth = _MscRtgPorsProfRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 6),
    _MscRtgPorsProfRequiredRxBandwidth_Type()
)
mscRtgPorsProfRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRequiredRxBandwidth.setStatus("mandatory")


class _MscRtgPorsProfRequiredTrafficType_Type(Integer32):
    """Custom type mscRtgPorsProfRequiredTrafficType based on Integer32"""
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


_MscRtgPorsProfRequiredTrafficType_Type.__name__ = "Integer32"
_MscRtgPorsProfRequiredTrafficType_Object = MibTableColumn
mscRtgPorsProfRequiredTrafficType = _MscRtgPorsProfRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 7),
    _MscRtgPorsProfRequiredTrafficType_Type()
)
mscRtgPorsProfRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRequiredTrafficType.setStatus("mandatory")


class _MscRtgPorsProfPermittedTrunkTypes_Type(OctetString):
    """Custom type mscRtgPorsProfPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscRtgPorsProfPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscRtgPorsProfPermittedTrunkTypes_Object = MibTableColumn
mscRtgPorsProfPermittedTrunkTypes = _MscRtgPorsProfPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 8),
    _MscRtgPorsProfPermittedTrunkTypes_Type()
)
mscRtgPorsProfPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfPermittedTrunkTypes.setStatus("mandatory")


class _MscRtgPorsProfRequiredSecurity_Type(Unsigned32):
    """Custom type mscRtgPorsProfRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgPorsProfRequiredSecurity_Type.__name__ = "Unsigned32"
_MscRtgPorsProfRequiredSecurity_Object = MibTableColumn
mscRtgPorsProfRequiredSecurity = _MscRtgPorsProfRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 9),
    _MscRtgPorsProfRequiredSecurity_Type()
)
mscRtgPorsProfRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRequiredSecurity.setStatus("mandatory")


class _MscRtgPorsProfRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscRtgPorsProfRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgPorsProfRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscRtgPorsProfRequiredCustomerParm_Object = MibTableColumn
mscRtgPorsProfRequiredCustomerParm = _MscRtgPorsProfRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 10),
    _MscRtgPorsProfRequiredCustomerParm_Type()
)
mscRtgPorsProfRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfRequiredCustomerParm.setStatus("mandatory")


class _MscRtgPorsProfPathAttributeToMinimize_Type(Integer32):
    """Custom type mscRtgPorsProfPathAttributeToMinimize based on Integer32"""
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


_MscRtgPorsProfPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscRtgPorsProfPathAttributeToMinimize_Object = MibTableColumn
mscRtgPorsProfPathAttributeToMinimize = _MscRtgPorsProfPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 11),
    _MscRtgPorsProfPathAttributeToMinimize_Type()
)
mscRtgPorsProfPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfPathAttributeToMinimize.setStatus("mandatory")


class _MscRtgPorsProfMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscRtgPorsProfMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgPorsProfMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscRtgPorsProfMaximumAcceptableCost_Object = MibTableColumn
mscRtgPorsProfMaximumAcceptableCost = _MscRtgPorsProfMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 12),
    _MscRtgPorsProfMaximumAcceptableCost_Type()
)
mscRtgPorsProfMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfMaximumAcceptableCost.setStatus("mandatory")


class _MscRtgPorsProfMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscRtgPorsProfMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscRtgPorsProfMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscRtgPorsProfMaximumAcceptableDelay_Object = MibTableColumn
mscRtgPorsProfMaximumAcceptableDelay = _MscRtgPorsProfMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 13),
    _MscRtgPorsProfMaximumAcceptableDelay_Type()
)
mscRtgPorsProfMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfMaximumAcceptableDelay.setStatus("mandatory")


class _MscRtgPorsProfEmissionPriority_Type(Integer32):
    """Custom type mscRtgPorsProfEmissionPriority based on Integer32"""
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


_MscRtgPorsProfEmissionPriority_Type.__name__ = "Integer32"
_MscRtgPorsProfEmissionPriority_Object = MibTableColumn
mscRtgPorsProfEmissionPriority = _MscRtgPorsProfEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 14),
    _MscRtgPorsProfEmissionPriority_Type()
)
mscRtgPorsProfEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfEmissionPriority.setStatus("mandatory")


class _MscRtgPorsProfDiscardPriority_Type(Integer32):
    """Custom type mscRtgPorsProfDiscardPriority based on Integer32"""
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


_MscRtgPorsProfDiscardPriority_Type.__name__ = "Integer32"
_MscRtgPorsProfDiscardPriority_Object = MibTableColumn
mscRtgPorsProfDiscardPriority = _MscRtgPorsProfDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 15),
    _MscRtgPorsProfDiscardPriority_Type()
)
mscRtgPorsProfDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfDiscardPriority.setStatus("mandatory")


class _MscRtgPorsProfPathFailureAction_Type(Integer32):
    """Custom type mscRtgPorsProfPathFailureAction based on Integer32"""
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


_MscRtgPorsProfPathFailureAction_Type.__name__ = "Integer32"
_MscRtgPorsProfPathFailureAction_Object = MibTableColumn
mscRtgPorsProfPathFailureAction = _MscRtgPorsProfPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 17),
    _MscRtgPorsProfPathFailureAction_Type()
)
mscRtgPorsProfPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfPathFailureAction.setStatus("mandatory")


class _MscRtgPorsProfBumpPreference_Type(Integer32):
    """Custom type mscRtgPorsProfBumpPreference based on Integer32"""
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


_MscRtgPorsProfBumpPreference_Type.__name__ = "Integer32"
_MscRtgPorsProfBumpPreference_Object = MibTableColumn
mscRtgPorsProfBumpPreference = _MscRtgPorsProfBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 18),
    _MscRtgPorsProfBumpPreference_Type()
)
mscRtgPorsProfBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfBumpPreference.setStatus("mandatory")


class _MscRtgPorsProfOptimization_Type(Integer32):
    """Custom type mscRtgPorsProfOptimization based on Integer32"""
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


_MscRtgPorsProfOptimization_Type.__name__ = "Integer32"
_MscRtgPorsProfOptimization_Object = MibTableColumn
mscRtgPorsProfOptimization = _MscRtgPorsProfOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 11, 1, 19),
    _MscRtgPorsProfOptimization_Type()
)
mscRtgPorsProfOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsProfOptimization.setStatus("mandatory")
_MscRtgPorsProfUsrTable_Object = MibTable
mscRtgPorsProfUsrTable = _MscRtgPorsProfUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 400)
)
if mibBuilder.loadTexts:
    mscRtgPorsProfUsrTable.setStatus("mandatory")
_MscRtgPorsProfUsrEntry_Object = MibTableRow
mscRtgPorsProfUsrEntry = _MscRtgPorsProfUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 400, 1)
)
mscRtgPorsProfUsrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsProfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsProfUsrValue"),
)
if mibBuilder.loadTexts:
    mscRtgPorsProfUsrEntry.setStatus("mandatory")
_MscRtgPorsProfUsrValue_Type = Link
_MscRtgPorsProfUsrValue_Object = MibTableColumn
mscRtgPorsProfUsrValue = _MscRtgPorsProfUsrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 7, 400, 1, 1),
    _MscRtgPorsProfUsrValue_Type()
)
mscRtgPorsProfUsrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsProfUsrValue.setStatus("mandatory")
_MscRtgPorsMpath_ObjectIdentity = ObjectIdentity
mscRtgPorsMpath = _MscRtgPorsMpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8)
)
_MscRtgPorsMpathRowStatusTable_Object = MibTable
mscRtgPorsMpathRowStatusTable = _MscRtgPorsMpathRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1)
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathRowStatusTable.setStatus("mandatory")
_MscRtgPorsMpathRowStatusEntry_Object = MibTableRow
mscRtgPorsMpathRowStatusEntry = _MscRtgPorsMpathRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1, 1)
)
mscRtgPorsMpathRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathRowStatusEntry.setStatus("mandatory")
_MscRtgPorsMpathRowStatus_Type = RowStatus
_MscRtgPorsMpathRowStatus_Object = MibTableColumn
mscRtgPorsMpathRowStatus = _MscRtgPorsMpathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1, 1, 1),
    _MscRtgPorsMpathRowStatus_Type()
)
mscRtgPorsMpathRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsMpathRowStatus.setStatus("mandatory")
_MscRtgPorsMpathComponentName_Type = DisplayString
_MscRtgPorsMpathComponentName_Object = MibTableColumn
mscRtgPorsMpathComponentName = _MscRtgPorsMpathComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1, 1, 2),
    _MscRtgPorsMpathComponentName_Type()
)
mscRtgPorsMpathComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathComponentName.setStatus("mandatory")
_MscRtgPorsMpathStorageType_Type = StorageType
_MscRtgPorsMpathStorageType_Object = MibTableColumn
mscRtgPorsMpathStorageType = _MscRtgPorsMpathStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1, 1, 4),
    _MscRtgPorsMpathStorageType_Type()
)
mscRtgPorsMpathStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathStorageType.setStatus("mandatory")


class _MscRtgPorsMpathIndex_Type(Integer32):
    """Custom type mscRtgPorsMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscRtgPorsMpathIndex_Type.__name__ = "Integer32"
_MscRtgPorsMpathIndex_Object = MibTableColumn
mscRtgPorsMpathIndex = _MscRtgPorsMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 1, 1, 10),
    _MscRtgPorsMpathIndex_Type()
)
mscRtgPorsMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgPorsMpathIndex.setStatus("mandatory")
_MscRtgPorsMpathOperTable_Object = MibTable
mscRtgPorsMpathOperTable = _MscRtgPorsMpathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 12)
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathOperTable.setStatus("mandatory")
_MscRtgPorsMpathOperEntry_Object = MibTableRow
mscRtgPorsMpathOperEntry = _MscRtgPorsMpathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 12, 1)
)
mscRtgPorsMpathOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathOperEntry.setStatus("mandatory")


class _MscRtgPorsMpathLastSetupFailureReason_Type(Integer32):
    """Custom type mscRtgPorsMpathLastSetupFailureReason based on Integer32"""
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


_MscRtgPorsMpathLastSetupFailureReason_Type.__name__ = "Integer32"
_MscRtgPorsMpathLastSetupFailureReason_Object = MibTableColumn
mscRtgPorsMpathLastSetupFailureReason = _MscRtgPorsMpathLastSetupFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 12, 1, 1),
    _MscRtgPorsMpathLastSetupFailureReason_Type()
)
mscRtgPorsMpathLastSetupFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathLastSetupFailureReason.setStatus("mandatory")


class _MscRtgPorsMpathLastSetupFailurePoint_Type(AsciiString):
    """Custom type mscRtgPorsMpathLastSetupFailurePoint based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscRtgPorsMpathLastSetupFailurePoint_Type.__name__ = "AsciiString"
_MscRtgPorsMpathLastSetupFailurePoint_Object = MibTableColumn
mscRtgPorsMpathLastSetupFailurePoint = _MscRtgPorsMpathLastSetupFailurePoint_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 12, 1, 2),
    _MscRtgPorsMpathLastSetupFailurePoint_Type()
)
mscRtgPorsMpathLastSetupFailurePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathLastSetupFailurePoint.setStatus("mandatory")
_MscRtgPorsMpathLastSetupFailedUser_Type = RowPointer
_MscRtgPorsMpathLastSetupFailedUser_Object = MibTableColumn
mscRtgPorsMpathLastSetupFailedUser = _MscRtgPorsMpathLastSetupFailedUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 12, 1, 3),
    _MscRtgPorsMpathLastSetupFailedUser_Type()
)
mscRtgPorsMpathLastSetupFailedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathLastSetupFailedUser.setStatus("mandatory")
_MscRtgPorsMpathRouteTable_Object = MibTable
mscRtgPorsMpathRouteTable = _MscRtgPorsMpathRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 408)
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathRouteTable.setStatus("mandatory")
_MscRtgPorsMpathRouteEntry_Object = MibTableRow
mscRtgPorsMpathRouteEntry = _MscRtgPorsMpathRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 408, 1)
)
mscRtgPorsMpathRouteEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathRouteIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathRouteEntry.setStatus("mandatory")


class _MscRtgPorsMpathRouteIndex_Type(Integer32):
    """Custom type mscRtgPorsMpathRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_MscRtgPorsMpathRouteIndex_Type.__name__ = "Integer32"
_MscRtgPorsMpathRouteIndex_Object = MibTableColumn
mscRtgPorsMpathRouteIndex = _MscRtgPorsMpathRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 408, 1, 1),
    _MscRtgPorsMpathRouteIndex_Type()
)
mscRtgPorsMpathRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgPorsMpathRouteIndex.setStatus("mandatory")


class _MscRtgPorsMpathRouteValue_Type(AsciiString):
    """Custom type mscRtgPorsMpathRouteValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscRtgPorsMpathRouteValue_Type.__name__ = "AsciiString"
_MscRtgPorsMpathRouteValue_Object = MibTableColumn
mscRtgPorsMpathRouteValue = _MscRtgPorsMpathRouteValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 408, 1, 2),
    _MscRtgPorsMpathRouteValue_Type()
)
mscRtgPorsMpathRouteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsMpathRouteValue.setStatus("mandatory")
_MscRtgPorsMpathUsrTable_Object = MibTable
mscRtgPorsMpathUsrTable = _MscRtgPorsMpathUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 409)
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathUsrTable.setStatus("mandatory")
_MscRtgPorsMpathUsrEntry_Object = MibTableRow
mscRtgPorsMpathUsrEntry = _MscRtgPorsMpathUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 409, 1)
)
mscRtgPorsMpathUsrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsMpathUsrValue"),
)
if mibBuilder.loadTexts:
    mscRtgPorsMpathUsrEntry.setStatus("mandatory")
_MscRtgPorsMpathUsrValue_Type = Link
_MscRtgPorsMpathUsrValue_Object = MibTableColumn
mscRtgPorsMpathUsrValue = _MscRtgPorsMpathUsrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 8, 409, 1, 1),
    _MscRtgPorsMpathUsrValue_Type()
)
mscRtgPorsMpathUsrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsMpathUsrValue.setStatus("mandatory")
_MscRtgPorsProvTable_Object = MibTable
mscRtgPorsProvTable = _MscRtgPorsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 10)
)
if mibBuilder.loadTexts:
    mscRtgPorsProvTable.setStatus("mandatory")
_MscRtgPorsProvEntry_Object = MibTableRow
mscRtgPorsProvEntry = _MscRtgPorsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 10, 1)
)
mscRtgPorsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsProvEntry.setStatus("mandatory")


class _MscRtgPorsOptimizationInterval_Type(Unsigned32):
    """Custom type mscRtgPorsOptimizationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_MscRtgPorsOptimizationInterval_Type.__name__ = "Unsigned32"
_MscRtgPorsOptimizationInterval_Object = MibTableColumn
mscRtgPorsOptimizationInterval = _MscRtgPorsOptimizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 10, 1, 1),
    _MscRtgPorsOptimizationInterval_Type()
)
mscRtgPorsOptimizationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgPorsOptimizationInterval.setStatus("mandatory")
_MscRtgPorsInfoTable_Object = MibTable
mscRtgPorsInfoTable = _MscRtgPorsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11)
)
if mibBuilder.loadTexts:
    mscRtgPorsInfoTable.setStatus("mandatory")
_MscRtgPorsInfoEntry_Object = MibTableRow
mscRtgPorsInfoEntry = _MscRtgPorsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1)
)
mscRtgPorsInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsVcMIB", "mscRtgPorsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgPorsInfoEntry.setStatus("mandatory")


class _MscRtgPorsActiveConnections_Type(Unsigned32):
    """Custom type mscRtgPorsActiveConnections based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgPorsActiveConnections_Type.__name__ = "Unsigned32"
_MscRtgPorsActiveConnections_Object = MibTableColumn
mscRtgPorsActiveConnections = _MscRtgPorsActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 1),
    _MscRtgPorsActiveConnections_Type()
)
mscRtgPorsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsActiveConnections.setStatus("mandatory")


class _MscRtgPorsOptimizationState_Type(Integer32):
    """Custom type mscRtgPorsOptimizationState based on Integer32"""
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


_MscRtgPorsOptimizationState_Type.__name__ = "Integer32"
_MscRtgPorsOptimizationState_Object = MibTableColumn
mscRtgPorsOptimizationState = _MscRtgPorsOptimizationState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 2),
    _MscRtgPorsOptimizationState_Type()
)
mscRtgPorsOptimizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsOptimizationState.setStatus("mandatory")


class _MscRtgPorsLastOptimizationTime_Type(EnterpriseDateAndTime):
    """Custom type mscRtgPorsLastOptimizationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscRtgPorsLastOptimizationTime_Type.__name__ = "EnterpriseDateAndTime"
_MscRtgPorsLastOptimizationTime_Object = MibTableColumn
mscRtgPorsLastOptimizationTime = _MscRtgPorsLastOptimizationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 3),
    _MscRtgPorsLastOptimizationTime_Type()
)
mscRtgPorsLastOptimizationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsLastOptimizationTime.setStatus("mandatory")


class _MscRtgPorsNextOptimizationTime_Type(EnterpriseDateAndTime):
    """Custom type mscRtgPorsNextOptimizationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscRtgPorsNextOptimizationTime_Type.__name__ = "EnterpriseDateAndTime"
_MscRtgPorsNextOptimizationTime_Object = MibTableColumn
mscRtgPorsNextOptimizationTime = _MscRtgPorsNextOptimizationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 4),
    _MscRtgPorsNextOptimizationTime_Type()
)
mscRtgPorsNextOptimizationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsNextOptimizationTime.setStatus("mandatory")


class _MscRtgPorsOptimizationPasses_Type(Unsigned32):
    """Custom type mscRtgPorsOptimizationPasses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgPorsOptimizationPasses_Type.__name__ = "Unsigned32"
_MscRtgPorsOptimizationPasses_Object = MibTableColumn
mscRtgPorsOptimizationPasses = _MscRtgPorsOptimizationPasses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 5),
    _MscRtgPorsOptimizationPasses_Type()
)
mscRtgPorsOptimizationPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsOptimizationPasses.setStatus("mandatory")


class _MscRtgPorsOptimizationProgress_Type(Unsigned32):
    """Custom type mscRtgPorsOptimizationProgress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgPorsOptimizationProgress_Type.__name__ = "Unsigned32"
_MscRtgPorsOptimizationProgress_Object = MibTableColumn
mscRtgPorsOptimizationProgress = _MscRtgPorsOptimizationProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 6),
    _MscRtgPorsOptimizationProgress_Type()
)
mscRtgPorsOptimizationProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsOptimizationProgress.setStatus("mandatory")


class _MscRtgPorsPathsOptimized_Type(Unsigned32):
    """Custom type mscRtgPorsPathsOptimized based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgPorsPathsOptimized_Type.__name__ = "Unsigned32"
_MscRtgPorsPathsOptimized_Object = MibTableColumn
mscRtgPorsPathsOptimized = _MscRtgPorsPathsOptimized_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 7),
    _MscRtgPorsPathsOptimized_Type()
)
mscRtgPorsPathsOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsPathsOptimized.setStatus("mandatory")


class _MscRtgPorsTotalPathsOptimized_Type(Unsigned32):
    """Custom type mscRtgPorsTotalPathsOptimized based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgPorsTotalPathsOptimized_Type.__name__ = "Unsigned32"
_MscRtgPorsTotalPathsOptimized_Object = MibTableColumn
mscRtgPorsTotalPathsOptimized = _MscRtgPorsTotalPathsOptimized_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 6, 11, 1, 8),
    _MscRtgPorsTotalPathsOptimized_Type()
)
mscRtgPorsTotalPathsOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgPorsTotalPathsOptimized.setStatus("mandatory")
_PorsVcMIB_ObjectIdentity = ObjectIdentity
porsVcMIB = _PorsVcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37)
)
_PorsVcGroup_ObjectIdentity = ObjectIdentity
porsVcGroup = _PorsVcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 1)
)
_PorsVcGroupCA_ObjectIdentity = ObjectIdentity
porsVcGroupCA = _PorsVcGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 1, 1)
)
_PorsVcGroupCA02_ObjectIdentity = ObjectIdentity
porsVcGroupCA02 = _PorsVcGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 1, 1, 3)
)
_PorsVcGroupCA02A_ObjectIdentity = ObjectIdentity
porsVcGroupCA02A = _PorsVcGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 1, 1, 3, 2)
)
_PorsVcCapabilities_ObjectIdentity = ObjectIdentity
porsVcCapabilities = _PorsVcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 3)
)
_PorsVcCapabilitiesCA_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesCA = _PorsVcCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 3, 1)
)
_PorsVcCapabilitiesCA02_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesCA02 = _PorsVcCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 3, 1, 3)
)
_PorsVcCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
porsVcCapabilitiesCA02A = _PorsVcCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 37, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-PorsVcMIB",
    **{"mscRtgRs": mscRtgRs,
       "mscRtgRsRowStatusTable": mscRtgRsRowStatusTable,
       "mscRtgRsRowStatusEntry": mscRtgRsRowStatusEntry,
       "mscRtgRsRowStatus": mscRtgRsRowStatus,
       "mscRtgRsComponentName": mscRtgRsComponentName,
       "mscRtgRsStorageType": mscRtgRsStorageType,
       "mscRtgRsIndex": mscRtgRsIndex,
       "mscRtgRsSelectedRouteTable": mscRtgRsSelectedRouteTable,
       "mscRtgRsSelectedRouteEntry": mscRtgRsSelectedRouteEntry,
       "mscRtgRsRouteCostMetric": mscRtgRsRouteCostMetric,
       "mscRtgRsRouteDelayMetric": mscRtgRsRouteDelayMetric,
       "mscRtgRsBumpingPriority": mscRtgRsBumpingPriority,
       "mscRtgRsReasonForNoRoute": mscRtgRsReasonForNoRoute,
       "mscRtgRsAttributeNotMet": mscRtgRsAttributeNotMet,
       "mscRtgRsRouteGatewayCostMetric": mscRtgRsRouteGatewayCostMetric,
       "mscRtgRsRouteType": mscRtgRsRouteType,
       "mscRtgRsControlsTable": mscRtgRsControlsTable,
       "mscRtgRsControlsEntry": mscRtgRsControlsEntry,
       "mscRtgRsRouteSelectionAttributes": mscRtgRsRouteSelectionAttributes,
       "mscRtgRsOperationMode": mscRtgRsOperationMode,
       "mscRtgRsLastRouteSelectionTime": mscRtgRsLastRouteSelectionTime,
       "mscRtgRsPathAttributesTable": mscRtgRsPathAttributesTable,
       "mscRtgRsPathAttributesEntry": mscRtgRsPathAttributesEntry,
       "mscRtgRsSourceId": mscRtgRsSourceId,
       "mscRtgRsRemoteName": mscRtgRsRemoteName,
       "mscRtgRsSetupPriority": mscRtgRsSetupPriority,
       "mscRtgRsRequiredTxBandwidth": mscRtgRsRequiredTxBandwidth,
       "mscRtgRsRequiredRxBandwidth": mscRtgRsRequiredRxBandwidth,
       "mscRtgRsMaximumTransmissionUnit": mscRtgRsMaximumTransmissionUnit,
       "mscRtgRsSecurity": mscRtgRsSecurity,
       "mscRtgRsTrafficType": mscRtgRsTrafficType,
       "mscRtgRsPermittedTrunkTypes": mscRtgRsPermittedTrunkTypes,
       "mscRtgRsCustomerParameter": mscRtgRsCustomerParameter,
       "mscRtgRsPathAttributeToMinimize": mscRtgRsPathAttributeToMinimize,
       "mscRtgRsMaximumAcceptableCost": mscRtgRsMaximumAcceptableCost,
       "mscRtgRsMaximumAcceptableDelay": mscRtgRsMaximumAcceptableDelay,
       "mscRtgRsBumpPreference": mscRtgRsBumpPreference,
       "mscRtgRsRequiredTrunkModes": mscRtgRsRequiredTrunkModes,
       "mscRtgRsMaximumAcceptableGatewayCost": mscRtgRsMaximumAcceptableGatewayCost,
       "mscRtgRsRouteRequestor": mscRtgRsRouteRequestor,
       "mscRtgRsGatewaySelectionAlg": mscRtgRsGatewaySelectionAlg,
       "mscRtgRsDestination": mscRtgRsDestination,
       "mscRtgRsSrdTable": mscRtgRsSrdTable,
       "mscRtgRsSrdEntry": mscRtgRsSrdEntry,
       "mscRtgRsSrdIndex": mscRtgRsSrdIndex,
       "mscRtgRsSrdValue": mscRtgRsSrdValue,
       "mscRtgRsRouteStatisticsTable": mscRtgRsRouteStatisticsTable,
       "mscRtgRsRouteStatisticsEntry": mscRtgRsRouteStatisticsEntry,
       "mscRtgRsRouteStatisticsSetupPriorityIndex": mscRtgRsRouteStatisticsSetupPriorityIndex,
       "mscRtgRsRouteStatisticsStatisticsTableIndex": mscRtgRsRouteStatisticsStatisticsTableIndex,
       "mscRtgRsRouteStatisticsValue": mscRtgRsRouteStatisticsValue,
       "mscRtgRsDgnTable": mscRtgRsDgnTable,
       "mscRtgRsDgnEntry": mscRtgRsDgnEntry,
       "mscRtgRsDgnValue": mscRtgRsDgnValue,
       "mscRtgPors": mscRtgPors,
       "mscRtgPorsRowStatusTable": mscRtgPorsRowStatusTable,
       "mscRtgPorsRowStatusEntry": mscRtgPorsRowStatusEntry,
       "mscRtgPorsRowStatus": mscRtgPorsRowStatus,
       "mscRtgPorsComponentName": mscRtgPorsComponentName,
       "mscRtgPorsStorageType": mscRtgPorsStorageType,
       "mscRtgPorsIndex": mscRtgPorsIndex,
       "mscRtgPorsProf": mscRtgPorsProf,
       "mscRtgPorsProfRowStatusTable": mscRtgPorsProfRowStatusTable,
       "mscRtgPorsProfRowStatusEntry": mscRtgPorsProfRowStatusEntry,
       "mscRtgPorsProfRowStatus": mscRtgPorsProfRowStatus,
       "mscRtgPorsProfComponentName": mscRtgPorsProfComponentName,
       "mscRtgPorsProfStorageType": mscRtgPorsProfStorageType,
       "mscRtgPorsProfIndex": mscRtgPorsProfIndex,
       "mscRtgPorsProfProvTable": mscRtgPorsProfProvTable,
       "mscRtgPorsProfProvEntry": mscRtgPorsProfProvEntry,
       "mscRtgPorsProfSetupPriority": mscRtgPorsProfSetupPriority,
       "mscRtgPorsProfHoldingPriority": mscRtgPorsProfHoldingPriority,
       "mscRtgPorsProfRequiredTxBandwidth": mscRtgPorsProfRequiredTxBandwidth,
       "mscRtgPorsProfRequiredRxBandwidth": mscRtgPorsProfRequiredRxBandwidth,
       "mscRtgPorsProfRequiredTrafficType": mscRtgPorsProfRequiredTrafficType,
       "mscRtgPorsProfPermittedTrunkTypes": mscRtgPorsProfPermittedTrunkTypes,
       "mscRtgPorsProfRequiredSecurity": mscRtgPorsProfRequiredSecurity,
       "mscRtgPorsProfRequiredCustomerParm": mscRtgPorsProfRequiredCustomerParm,
       "mscRtgPorsProfPathAttributeToMinimize": mscRtgPorsProfPathAttributeToMinimize,
       "mscRtgPorsProfMaximumAcceptableCost": mscRtgPorsProfMaximumAcceptableCost,
       "mscRtgPorsProfMaximumAcceptableDelay": mscRtgPorsProfMaximumAcceptableDelay,
       "mscRtgPorsProfEmissionPriority": mscRtgPorsProfEmissionPriority,
       "mscRtgPorsProfDiscardPriority": mscRtgPorsProfDiscardPriority,
       "mscRtgPorsProfPathFailureAction": mscRtgPorsProfPathFailureAction,
       "mscRtgPorsProfBumpPreference": mscRtgPorsProfBumpPreference,
       "mscRtgPorsProfOptimization": mscRtgPorsProfOptimization,
       "mscRtgPorsProfUsrTable": mscRtgPorsProfUsrTable,
       "mscRtgPorsProfUsrEntry": mscRtgPorsProfUsrEntry,
       "mscRtgPorsProfUsrValue": mscRtgPorsProfUsrValue,
       "mscRtgPorsMpath": mscRtgPorsMpath,
       "mscRtgPorsMpathRowStatusTable": mscRtgPorsMpathRowStatusTable,
       "mscRtgPorsMpathRowStatusEntry": mscRtgPorsMpathRowStatusEntry,
       "mscRtgPorsMpathRowStatus": mscRtgPorsMpathRowStatus,
       "mscRtgPorsMpathComponentName": mscRtgPorsMpathComponentName,
       "mscRtgPorsMpathStorageType": mscRtgPorsMpathStorageType,
       "mscRtgPorsMpathIndex": mscRtgPorsMpathIndex,
       "mscRtgPorsMpathOperTable": mscRtgPorsMpathOperTable,
       "mscRtgPorsMpathOperEntry": mscRtgPorsMpathOperEntry,
       "mscRtgPorsMpathLastSetupFailureReason": mscRtgPorsMpathLastSetupFailureReason,
       "mscRtgPorsMpathLastSetupFailurePoint": mscRtgPorsMpathLastSetupFailurePoint,
       "mscRtgPorsMpathLastSetupFailedUser": mscRtgPorsMpathLastSetupFailedUser,
       "mscRtgPorsMpathRouteTable": mscRtgPorsMpathRouteTable,
       "mscRtgPorsMpathRouteEntry": mscRtgPorsMpathRouteEntry,
       "mscRtgPorsMpathRouteIndex": mscRtgPorsMpathRouteIndex,
       "mscRtgPorsMpathRouteValue": mscRtgPorsMpathRouteValue,
       "mscRtgPorsMpathUsrTable": mscRtgPorsMpathUsrTable,
       "mscRtgPorsMpathUsrEntry": mscRtgPorsMpathUsrEntry,
       "mscRtgPorsMpathUsrValue": mscRtgPorsMpathUsrValue,
       "mscRtgPorsProvTable": mscRtgPorsProvTable,
       "mscRtgPorsProvEntry": mscRtgPorsProvEntry,
       "mscRtgPorsOptimizationInterval": mscRtgPorsOptimizationInterval,
       "mscRtgPorsInfoTable": mscRtgPorsInfoTable,
       "mscRtgPorsInfoEntry": mscRtgPorsInfoEntry,
       "mscRtgPorsActiveConnections": mscRtgPorsActiveConnections,
       "mscRtgPorsOptimizationState": mscRtgPorsOptimizationState,
       "mscRtgPorsLastOptimizationTime": mscRtgPorsLastOptimizationTime,
       "mscRtgPorsNextOptimizationTime": mscRtgPorsNextOptimizationTime,
       "mscRtgPorsOptimizationPasses": mscRtgPorsOptimizationPasses,
       "mscRtgPorsOptimizationProgress": mscRtgPorsOptimizationProgress,
       "mscRtgPorsPathsOptimized": mscRtgPorsPathsOptimized,
       "mscRtgPorsTotalPathsOptimized": mscRtgPorsTotalPathsOptimized,
       "porsVcMIB": porsVcMIB,
       "porsVcGroup": porsVcGroup,
       "porsVcGroupCA": porsVcGroupCA,
       "porsVcGroupCA02": porsVcGroupCA02,
       "porsVcGroupCA02A": porsVcGroupCA02A,
       "porsVcCapabilities": porsVcCapabilities,
       "porsVcCapabilitiesCA": porsVcCapabilitiesCA,
       "porsVcCapabilitiesCA02": porsVcCapabilitiesCA02,
       "porsVcCapabilitiesCA02A": porsVcCapabilitiesCA02A}
)
