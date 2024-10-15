# SNMP MIB module (CXX25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXX25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:02 2024
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

(Alias,
 SapIndex,
 ThruputClass,
 cxX25) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "ThruputClass",
    "cxX25")

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
 NotificationType,
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
    "NotificationType",
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



class SapType(Integer32):
    """Custom type SapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )





class PacketSize(Integer32):
    """Custom type PacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes16", 4),
          ("bytes2048", 11),
          ("bytes256", 8),
          ("bytes32", 5),
          ("bytes4096", 12),
          ("bytes512", 9),
          ("bytes64", 6))
    )





class Ces(Integer32):
    """Custom type Ces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )





class Lcn(Integer32):
    """Custom type Lcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )





class CugIndex(Integer32):
    """Custom type CugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )





class CugIC(Integer32):
    """Custom type CugIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class RoutePartition(Integer32):
    """Custom type RoutePartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class RouteIndex(Integer32):
    """Custom type RouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )





class HGIndex(Integer32):
    """Custom type HGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )





class PvcIndex(Integer32):
    """Custom type PvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )





class X25Address(DisplayString):
    """Custom type X25Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _X25LowerPoolThreshold_Type(Integer32):
    """Custom type x25LowerPoolThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_X25LowerPoolThreshold_Type.__name__ = "Integer32"
_X25LowerPoolThreshold_Object = MibScalar
x25LowerPoolThreshold = _X25LowerPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 1),
    _X25LowerPoolThreshold_Type()
)
x25LowerPoolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LowerPoolThreshold.setStatus("mandatory")


class _X25UpperPoolThreshold_Type(Integer32):
    """Custom type x25UpperPoolThreshold based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_X25UpperPoolThreshold_Type.__name__ = "Integer32"
_X25UpperPoolThreshold_Object = MibScalar
x25UpperPoolThreshold = _X25UpperPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 2),
    _X25UpperPoolThreshold_Type()
)
x25UpperPoolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25UpperPoolThreshold.setStatus("mandatory")


class _X25RouteMask_Type(Integer32):
    """Custom type x25RouteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_X25RouteMask_Type.__name__ = "Integer32"
_X25RouteMask_Object = MibScalar
x25RouteMask = _X25RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 3),
    _X25RouteMask_Type()
)
x25RouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteMask.setStatus("mandatory")


class _X25BillingSegmentSize_Type(Integer32):
    """Custom type x25BillingSegmentSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_X25BillingSegmentSize_Type.__name__ = "Integer32"
_X25BillingSegmentSize_Object = MibScalar
x25BillingSegmentSize = _X25BillingSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 4),
    _X25BillingSegmentSize_Type()
)
x25BillingSegmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25BillingSegmentSize.setStatus("mandatory")


class _X25Billing_Type(Integer32):
    """Custom type x25Billing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_X25Billing_Type.__name__ = "Integer32"
_X25Billing_Object = MibScalar
x25Billing = _X25Billing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 5),
    _X25Billing_Type()
)
x25Billing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Billing.setStatus("mandatory")


class _X25NetworkType_Type(Integer32):
    """Custom type x25NetworkType based on Integer32"""
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
        *(("dteEndpoint", 3),
          ("privateDataNetwork", 2),
          ("publicDataNetwork", 1))
    )


_X25NetworkType_Type.__name__ = "Integer32"
_X25NetworkType_Object = MibScalar
x25NetworkType = _X25NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 6),
    _X25NetworkType_Type()
)
x25NetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25NetworkType.setStatus("mandatory")


class _X25HuntGroupRotation_Type(Integer32):
    """Custom type x25HuntGroupRotation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_X25HuntGroupRotation_Type.__name__ = "Integer32"
_X25HuntGroupRotation_Object = MibScalar
x25HuntGroupRotation = _X25HuntGroupRotation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 7),
    _X25HuntGroupRotation_Type()
)
x25HuntGroupRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25HuntGroupRotation.setStatus("mandatory")


class _X25Alarms_Type(Integer32):
    """Custom type x25Alarms based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_X25Alarms_Type.__name__ = "Integer32"
_X25Alarms_Object = MibScalar
x25Alarms = _X25Alarms_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 10),
    _X25Alarms_Type()
)
x25Alarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Alarms.setStatus("mandatory")


class _X25SapStatusEvent_Type(Integer32):
    """Custom type x25SapStatusEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noEvent", 1)
    )


_X25SapStatusEvent_Type.__name__ = "Integer32"
_X25SapStatusEvent_Object = MibScalar
x25SapStatusEvent = _X25SapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 11),
    _X25SapStatusEvent_Type()
)
x25SapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatusEvent.setStatus("mandatory")


class _X25ConfigErrorEvent_Type(Integer32):
    """Custom type x25ConfigErrorEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noError", 1)
    )


_X25ConfigErrorEvent_Type.__name__ = "Integer32"
_X25ConfigErrorEvent_Object = MibScalar
x25ConfigErrorEvent = _X25ConfigErrorEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 12),
    _X25ConfigErrorEvent_Type()
)
x25ConfigErrorEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ConfigErrorEvent.setStatus("mandatory")
_X25SoftwareVersions_Type = DisplayString
_X25SoftwareVersions_Object = MibScalar
x25SoftwareVersions = _X25SoftwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 19),
    _X25SoftwareVersions_Type()
)
x25SoftwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SoftwareVersions.setStatus("mandatory")
_X25LogicalLinkTable_Object = MibTable
x25LogicalLinkTable = _X25LogicalLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20)
)
if mibBuilder.loadTexts:
    x25LogicalLinkTable.setStatus("mandatory")
_X25LogicalLinkEntry_Object = MibTableRow
x25LogicalLinkEntry = _X25LogicalLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1)
)
x25LogicalLinkEntry.setIndexNames(
    (0, "CXX25-MIB", "x25LLNumber"),
    (0, "CXX25-MIB", "x25LLSapNumber"),
    (0, "CXX25-MIB", "x25LLSapCes"),
)
if mibBuilder.loadTexts:
    x25LogicalLinkEntry.setStatus("mandatory")
_X25LLNumber_Type = SapIndex
_X25LLNumber_Object = MibTableColumn
x25LLNumber = _X25LLNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 1),
    _X25LLNumber_Type()
)
x25LLNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LLNumber.setStatus("mandatory")
_X25LLSapNumber_Type = SapIndex
_X25LLSapNumber_Object = MibTableColumn
x25LLSapNumber = _X25LLSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 2),
    _X25LLSapNumber_Type()
)
x25LLSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LLSapNumber.setStatus("mandatory")
_X25LLSapCes_Type = Ces
_X25LLSapCes_Object = MibTableColumn
x25LLSapCes = _X25LLSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 3),
    _X25LLSapCes_Type()
)
x25LLSapCes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LLSapCes.setStatus("mandatory")


class _X25LLRowStatus_Type(Integer32):
    """Custom type x25LLRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25LLRowStatus_Type.__name__ = "Integer32"
_X25LLRowStatus_Object = MibTableColumn
x25LLRowStatus = _X25LLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 4),
    _X25LLRowStatus_Type()
)
x25LLRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LLRowStatus.setStatus("mandatory")


class _X25LLRouteAlgorithm_Type(Integer32):
    """Custom type x25LLRouteAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 1),
          ("prioritized", 2))
    )


_X25LLRouteAlgorithm_Type.__name__ = "Integer32"
_X25LLRouteAlgorithm_Object = MibTableColumn
x25LLRouteAlgorithm = _X25LLRouteAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 5),
    _X25LLRouteAlgorithm_Type()
)
x25LLRouteAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25LLRouteAlgorithm.setStatus("mandatory")


class _X25LLEntryState_Type(Integer32):
    """Custom type x25LLEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 1),
          ("onLine", 2))
    )


_X25LLEntryState_Type.__name__ = "Integer32"
_X25LLEntryState_Object = MibTableColumn
x25LLEntryState = _X25LLEntryState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 20, 1, 6),
    _X25LLEntryState_Type()
)
x25LLEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LLEntryState.setStatus("mandatory")
_X25SapTable_Object = MibTable
x25SapTable = _X25SapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21)
)
if mibBuilder.loadTexts:
    x25SapTable.setStatus("mandatory")
_X25SapEntry_Object = MibTableRow
x25SapEntry = _X25SapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1)
)
x25SapEntry.setIndexNames(
    (0, "CXX25-MIB", "x25SapNumber"),
    (0, "CXX25-MIB", "x25SapCes"),
)
if mibBuilder.loadTexts:
    x25SapEntry.setStatus("mandatory")
_X25SapNumber_Type = SapIndex
_X25SapNumber_Object = MibTableColumn
x25SapNumber = _X25SapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 1),
    _X25SapNumber_Type()
)
x25SapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapNumber.setStatus("mandatory")
_X25SapCes_Type = Ces
_X25SapCes_Object = MibTableColumn
x25SapCes = _X25SapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 2),
    _X25SapCes_Type()
)
x25SapCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapCes.setStatus("mandatory")


class _X25SapRowStatus_Type(Integer32):
    """Custom type x25SapRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25SapRowStatus_Type.__name__ = "Integer32"
_X25SapRowStatus_Object = MibTableColumn
x25SapRowStatus = _X25SapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 3),
    _X25SapRowStatus_Type()
)
x25SapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRowStatus.setStatus("mandatory")


class _X25SapType_Type(SapType):
    """Custom type x25SapType based on SapType"""


_X25SapType_Object = MibTableColumn
x25SapType = _X25SapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 4),
    _X25SapType_Type()
)
x25SapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapType.setStatus("mandatory")
_X25SapAlias_Type = Alias
_X25SapAlias_Object = MibTableColumn
x25SapAlias = _X25SapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 5),
    _X25SapAlias_Type()
)
x25SapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapAlias.setStatus("mandatory")
_X25SapCompanionAlias_Type = Alias
_X25SapCompanionAlias_Object = MibTableColumn
x25SapCompanionAlias = _X25SapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 6),
    _X25SapCompanionAlias_Type()
)
x25SapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapCompanionAlias.setStatus("mandatory")


class _X25SapInterfaceType_Type(Integer32):
    """Custom type x25SapInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_X25SapInterfaceType_Type.__name__ = "Integer32"
_X25SapInterfaceType_Object = MibTableColumn
x25SapInterfaceType = _X25SapInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 13),
    _X25SapInterfaceType_Type()
)
x25SapInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapInterfaceType.setStatus("mandatory")


class _X25SapLinkType_Type(Integer32):
    """Custom type x25SapLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x25Link", 1),
          ("x75Link", 2))
    )


_X25SapLinkType_Type.__name__ = "Integer32"
_X25SapLinkType_Object = MibTableColumn
x25SapLinkType = _X25SapLinkType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 14),
    _X25SapLinkType_Type()
)
x25SapLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLinkType.setStatus("mandatory")


class _X25SapRoutePartition_Type(RoutePartition):
    """Custom type x25SapRoutePartition based on RoutePartition"""
    defaultValue = 0


_X25SapRoutePartition_Object = MibTableColumn
x25SapRoutePartition = _X25SapRoutePartition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 19),
    _X25SapRoutePartition_Type()
)
x25SapRoutePartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRoutePartition.setStatus("mandatory")


class _X25SapRouteDirection_Type(Integer32):
    """Custom type x25SapRouteDirection based on Integer32"""
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
        *(("both", 1),
          ("lower", 3),
          ("upper", 2))
    )


_X25SapRouteDirection_Type.__name__ = "Integer32"
_X25SapRouteDirection_Object = MibTableColumn
x25SapRouteDirection = _X25SapRouteDirection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 20),
    _X25SapRouteDirection_Type()
)
x25SapRouteDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRouteDirection.setStatus("mandatory")


class _X25SapWildCardRouting_Type(Integer32):
    """Custom type x25SapWildCardRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapWildCardRouting_Type.__name__ = "Integer32"
_X25SapWildCardRouting_Object = MibTableColumn
x25SapWildCardRouting = _X25SapWildCardRouting_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 21),
    _X25SapWildCardRouting_Type()
)
x25SapWildCardRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapWildCardRouting.setStatus("obsolete")


class _X25SapWildCardRoutingMask_Type(Integer32):
    """Custom type x25SapWildCardRoutingMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_X25SapWildCardRoutingMask_Type.__name__ = "Integer32"
_X25SapWildCardRoutingMask_Object = MibTableColumn
x25SapWildCardRoutingMask = _X25SapWildCardRoutingMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 22),
    _X25SapWildCardRoutingMask_Type()
)
x25SapWildCardRoutingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapWildCardRoutingMask.setStatus("obsolete")


class _X25SapActivation_Type(Integer32):
    """Custom type x25SapActivation based on Integer32"""
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
        *(("dynamic", 2),
          ("dynamic-120s-delay", 6),
          ("dynamic-30s-delay", 3),
          ("dynamic-60s-delay", 4),
          ("dynamic-90s-delay", 5),
          ("normal", 1))
    )


_X25SapActivation_Type.__name__ = "Integer32"
_X25SapActivation_Object = MibTableColumn
x25SapActivation = _X25SapActivation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 26),
    _X25SapActivation_Type()
)
x25SapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapActivation.setStatus("mandatory")


class _X25SapPvcBillingTimer_Type(Integer32):
    """Custom type x25SapPvcBillingTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_X25SapPvcBillingTimer_Type.__name__ = "Integer32"
_X25SapPvcBillingTimer_Object = MibTableColumn
x25SapPvcBillingTimer = _X25SapPvcBillingTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 27),
    _X25SapPvcBillingTimer_Type()
)
x25SapPvcBillingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapPvcBillingTimer.setStatus("mandatory")


class _X25SapModulo_Type(Integer32):
    """Custom type x25SapModulo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25SapModulo_Type.__name__ = "Integer32"
_X25SapModulo_Object = MibTableColumn
x25SapModulo = _X25SapModulo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 31),
    _X25SapModulo_Type()
)
x25SapModulo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapModulo.setStatus("mandatory")


class _X25SapRxPacketSize_Type(PacketSize):
    """Custom type x25SapRxPacketSize based on PacketSize"""


_X25SapRxPacketSize_Object = MibTableColumn
x25SapRxPacketSize = _X25SapRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 32),
    _X25SapRxPacketSize_Type()
)
x25SapRxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRxPacketSize.setStatus("mandatory")


class _X25SapTxPacketSize_Type(PacketSize):
    """Custom type x25SapTxPacketSize based on PacketSize"""


_X25SapTxPacketSize_Object = MibTableColumn
x25SapTxPacketSize = _X25SapTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 33),
    _X25SapTxPacketSize_Type()
)
x25SapTxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapTxPacketSize.setStatus("mandatory")


class _X25SapRxWindowSize_Type(Integer32):
    """Custom type x25SapRxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25SapRxWindowSize_Type.__name__ = "Integer32"
_X25SapRxWindowSize_Object = MibTableColumn
x25SapRxWindowSize = _X25SapRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 34),
    _X25SapRxWindowSize_Type()
)
x25SapRxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRxWindowSize.setStatus("mandatory")


class _X25SapTxWindowSize_Type(Integer32):
    """Custom type x25SapTxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25SapTxWindowSize_Type.__name__ = "Integer32"
_X25SapTxWindowSize_Object = MibTableColumn
x25SapTxWindowSize = _X25SapTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 35),
    _X25SapTxWindowSize_Type()
)
x25SapTxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapTxWindowSize.setStatus("mandatory")


class _X25SapRxThruputClass_Type(ThruputClass):
    """Custom type x25SapRxThruputClass based on ThruputClass"""


_X25SapRxThruputClass_Object = MibTableColumn
x25SapRxThruputClass = _X25SapRxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 36),
    _X25SapRxThruputClass_Type()
)
x25SapRxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRxThruputClass.setStatus("mandatory")


class _X25SapTxThruputClass_Type(ThruputClass):
    """Custom type x25SapTxThruputClass based on ThruputClass"""


_X25SapTxThruputClass_Object = MibTableColumn
x25SapTxThruputClass = _X25SapTxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 37),
    _X25SapTxThruputClass_Type()
)
x25SapTxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapTxThruputClass.setStatus("mandatory")


class _X25SapRxWindowThreshold_Type(Integer32):
    """Custom type x25SapRxWindowThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25SapRxWindowThreshold_Type.__name__ = "Integer32"
_X25SapRxWindowThreshold_Object = MibTableColumn
x25SapRxWindowThreshold = _X25SapRxWindowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 38),
    _X25SapRxWindowThreshold_Type()
)
x25SapRxWindowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRxWindowThreshold.setStatus("mandatory")


class _X25SapLcnAllocation_Type(Integer32):
    """Custom type x25SapLcnAllocation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_X25SapLcnAllocation_Type.__name__ = "Integer32"
_X25SapLcnAllocation_Object = MibTableColumn
x25SapLcnAllocation = _X25SapLcnAllocation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 48),
    _X25SapLcnAllocation_Type()
)
x25SapLcnAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLcnAllocation.setStatus("mandatory")


class _X25SapLpvcLcn_Type(Integer32):
    """Custom type x25SapLpvcLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapLpvcLcn_Type.__name__ = "Integer32"
_X25SapLpvcLcn_Object = MibTableColumn
x25SapLpvcLcn = _X25SapLpvcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 49),
    _X25SapLpvcLcn_Type()
)
x25SapLpvcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLpvcLcn.setStatus("mandatory")


class _X25SapHpvcLcn_Type(Integer32):
    """Custom type x25SapHpvcLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapHpvcLcn_Type.__name__ = "Integer32"
_X25SapHpvcLcn_Object = MibTableColumn
x25SapHpvcLcn = _X25SapHpvcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 50),
    _X25SapHpvcLcn_Type()
)
x25SapHpvcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapHpvcLcn.setStatus("mandatory")


class _X25SapLicLcn_Type(Integer32):
    """Custom type x25SapLicLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapLicLcn_Type.__name__ = "Integer32"
_X25SapLicLcn_Object = MibTableColumn
x25SapLicLcn = _X25SapLicLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 51),
    _X25SapLicLcn_Type()
)
x25SapLicLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLicLcn.setStatus("mandatory")


class _X25SapHicLcn_Type(Integer32):
    """Custom type x25SapHicLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapHicLcn_Type.__name__ = "Integer32"
_X25SapHicLcn_Object = MibTableColumn
x25SapHicLcn = _X25SapHicLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 52),
    _X25SapHicLcn_Type()
)
x25SapHicLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapHicLcn.setStatus("mandatory")


class _X25SapLtcLcn_Type(Integer32):
    """Custom type x25SapLtcLcn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapLtcLcn_Type.__name__ = "Integer32"
_X25SapLtcLcn_Object = MibTableColumn
x25SapLtcLcn = _X25SapLtcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 53),
    _X25SapLtcLcn_Type()
)
x25SapLtcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLtcLcn.setStatus("mandatory")


class _X25SapHtcLcn_Type(Integer32):
    """Custom type x25SapHtcLcn based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapHtcLcn_Type.__name__ = "Integer32"
_X25SapHtcLcn_Object = MibTableColumn
x25SapHtcLcn = _X25SapHtcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 54),
    _X25SapHtcLcn_Type()
)
x25SapHtcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapHtcLcn.setStatus("mandatory")


class _X25SapLocLcn_Type(Integer32):
    """Custom type x25SapLocLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapLocLcn_Type.__name__ = "Integer32"
_X25SapLocLcn_Object = MibTableColumn
x25SapLocLcn = _X25SapLocLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 55),
    _X25SapLocLcn_Type()
)
x25SapLocLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapLocLcn.setStatus("mandatory")


class _X25SapHocLcn_Type(Integer32):
    """Custom type x25SapHocLcn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_X25SapHocLcn_Type.__name__ = "Integer32"
_X25SapHocLcn_Object = MibTableColumn
x25SapHocLcn = _X25SapHocLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 56),
    _X25SapHocLcn_Type()
)
x25SapHocLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapHocLcn.setStatus("mandatory")


class _X25SapConnectTimer_Type(Integer32):
    """Custom type x25SapConnectTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_X25SapConnectTimer_Type.__name__ = "Integer32"
_X25SapConnectTimer_Object = MibTableColumn
x25SapConnectTimer = _X25SapConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 61),
    _X25SapConnectTimer_Type()
)
x25SapConnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapConnectTimer.setStatus("mandatory")


class _X25SapDisconnectTimer_Type(Integer32):
    """Custom type x25SapDisconnectTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_X25SapDisconnectTimer_Type.__name__ = "Integer32"
_X25SapDisconnectTimer_Object = MibTableColumn
x25SapDisconnectTimer = _X25SapDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 62),
    _X25SapDisconnectTimer_Type()
)
x25SapDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapDisconnectTimer.setStatus("mandatory")


class _X25SapRestartTimer_Type(Integer32):
    """Custom type x25SapRestartTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapRestartTimer_Type.__name__ = "Integer32"
_X25SapRestartTimer_Object = MibTableColumn
x25SapRestartTimer = _X25SapRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 63),
    _X25SapRestartTimer_Type()
)
x25SapRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRestartTimer.setStatus("mandatory")


class _X25SapCallTimer_Type(Integer32):
    """Custom type x25SapCallTimer based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapCallTimer_Type.__name__ = "Integer32"
_X25SapCallTimer_Object = MibTableColumn
x25SapCallTimer = _X25SapCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 64),
    _X25SapCallTimer_Type()
)
x25SapCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapCallTimer.setStatus("mandatory")


class _X25SapResetTimer_Type(Integer32):
    """Custom type x25SapResetTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapResetTimer_Type.__name__ = "Integer32"
_X25SapResetTimer_Object = MibTableColumn
x25SapResetTimer = _X25SapResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 65),
    _X25SapResetTimer_Type()
)
x25SapResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapResetTimer.setStatus("mandatory")


class _X25SapClearTimer_Type(Integer32):
    """Custom type x25SapClearTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapClearTimer_Type.__name__ = "Integer32"
_X25SapClearTimer_Object = MibTableColumn
x25SapClearTimer = _X25SapClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 66),
    _X25SapClearTimer_Type()
)
x25SapClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapClearTimer.setStatus("mandatory")


class _X25SapInactivityTimer_Type(Integer32):
    """Custom type x25SapInactivityTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_X25SapInactivityTimer_Type.__name__ = "Integer32"
_X25SapInactivityTimer_Object = MibTableColumn
x25SapInactivityTimer = _X25SapInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 67),
    _X25SapInactivityTimer_Type()
)
x25SapInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapInactivityTimer.setStatus("mandatory")


class _X25SapFlowControlTimer_Type(Integer32):
    """Custom type x25SapFlowControlTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapFlowControlTimer_Type.__name__ = "Integer32"
_X25SapFlowControlTimer_Object = MibTableColumn
x25SapFlowControlTimer = _X25SapFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 68),
    _X25SapFlowControlTimer_Type()
)
x25SapFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapFlowControlTimer.setStatus("mandatory")


class _X25SapWindowStatusTimer_Type(Integer32):
    """Custom type x25SapWindowStatusTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_X25SapWindowStatusTimer_Type.__name__ = "Integer32"
_X25SapWindowStatusTimer_Object = MibTableColumn
x25SapWindowStatusTimer = _X25SapWindowStatusTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 69),
    _X25SapWindowStatusTimer_Type()
)
x25SapWindowStatusTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapWindowStatusTimer.setStatus("mandatory")


class _X25SapSbscrCalledAddressInsertion_Type(Integer32):
    """Custom type x25SapSbscrCalledAddressInsertion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCalledAddressInsertion_Type.__name__ = "Integer32"
_X25SapSbscrCalledAddressInsertion_Object = MibTableColumn
x25SapSbscrCalledAddressInsertion = _X25SapSbscrCalledAddressInsertion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 80),
    _X25SapSbscrCalledAddressInsertion_Type()
)
x25SapSbscrCalledAddressInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCalledAddressInsertion.setStatus("mandatory")


class _X25SapSbscrCallingAddressInsertion_Type(Integer32):
    """Custom type x25SapSbscrCallingAddressInsertion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCallingAddressInsertion_Type.__name__ = "Integer32"
_X25SapSbscrCallingAddressInsertion_Object = MibTableColumn
x25SapSbscrCallingAddressInsertion = _X25SapSbscrCallingAddressInsertion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 81),
    _X25SapSbscrCallingAddressInsertion_Type()
)
x25SapSbscrCallingAddressInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCallingAddressInsertion.setStatus("mandatory")


class _X25SapSbscrPktRetransmission_Type(Integer32):
    """Custom type x25SapSbscrPktRetransmission based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrPktRetransmission_Type.__name__ = "Integer32"
_X25SapSbscrPktRetransmission_Object = MibTableColumn
x25SapSbscrPktRetransmission = _X25SapSbscrPktRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 82),
    _X25SapSbscrPktRetransmission_Type()
)
x25SapSbscrPktRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrPktRetransmission.setStatus("mandatory")


class _X25SapSbscrInAccessBarred_Type(Integer32):
    """Custom type x25SapSbscrInAccessBarred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrInAccessBarred_Type.__name__ = "Integer32"
_X25SapSbscrInAccessBarred_Object = MibTableColumn
x25SapSbscrInAccessBarred = _X25SapSbscrInAccessBarred_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 83),
    _X25SapSbscrInAccessBarred_Type()
)
x25SapSbscrInAccessBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrInAccessBarred.setStatus("mandatory")


class _X25SapSbscrOutAccessBarred_Type(Integer32):
    """Custom type x25SapSbscrOutAccessBarred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrOutAccessBarred_Type.__name__ = "Integer32"
_X25SapSbscrOutAccessBarred_Object = MibTableColumn
x25SapSbscrOutAccessBarred = _X25SapSbscrOutAccessBarred_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 84),
    _X25SapSbscrOutAccessBarred_Type()
)
x25SapSbscrOutAccessBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrOutAccessBarred.setStatus("mandatory")


class _X25SapSbscrFlowCntrlParamNegotiation_Type(Integer32):
    """Custom type x25SapSbscrFlowCntrlParamNegotiation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrFlowCntrlParamNegotiation_Type.__name__ = "Integer32"
_X25SapSbscrFlowCntrlParamNegotiation_Object = MibTableColumn
x25SapSbscrFlowCntrlParamNegotiation = _X25SapSbscrFlowCntrlParamNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 85),
    _X25SapSbscrFlowCntrlParamNegotiation_Type()
)
x25SapSbscrFlowCntrlParamNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrFlowCntrlParamNegotiation.setStatus("mandatory")


class _X25SapSbscrThruputClassNegotiation_Type(Integer32):
    """Custom type x25SapSbscrThruputClassNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrThruputClassNegotiation_Type.__name__ = "Integer32"
_X25SapSbscrThruputClassNegotiation_Object = MibTableColumn
x25SapSbscrThruputClassNegotiation = _X25SapSbscrThruputClassNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 86),
    _X25SapSbscrThruputClassNegotiation_Type()
)
x25SapSbscrThruputClassNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrThruputClassNegotiation.setStatus("mandatory")


class _X25SapSbscrFastSelect_Type(Integer32):
    """Custom type x25SapSbscrFastSelect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrFastSelect_Type.__name__ = "Integer32"
_X25SapSbscrFastSelect_Object = MibTableColumn
x25SapSbscrFastSelect = _X25SapSbscrFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 87),
    _X25SapSbscrFastSelect_Type()
)
x25SapSbscrFastSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrFastSelect.setStatus("mandatory")


class _X25SapSbscrFastSelectAcceptance_Type(Integer32):
    """Custom type x25SapSbscrFastSelectAcceptance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrFastSelectAcceptance_Type.__name__ = "Integer32"
_X25SapSbscrFastSelectAcceptance_Object = MibTableColumn
x25SapSbscrFastSelectAcceptance = _X25SapSbscrFastSelectAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 88),
    _X25SapSbscrFastSelectAcceptance_Type()
)
x25SapSbscrFastSelectAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrFastSelectAcceptance.setStatus("mandatory")


class _X25SapSbscrReverseChargingAcceptance_Type(Integer32):
    """Custom type x25SapSbscrReverseChargingAcceptance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrReverseChargingAcceptance_Type.__name__ = "Integer32"
_X25SapSbscrReverseChargingAcceptance_Object = MibTableColumn
x25SapSbscrReverseChargingAcceptance = _X25SapSbscrReverseChargingAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 89),
    _X25SapSbscrReverseChargingAcceptance_Type()
)
x25SapSbscrReverseChargingAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrReverseChargingAcceptance.setStatus("mandatory")


class _X25SapSbscrLocalChargingPrevention_Type(Integer32):
    """Custom type x25SapSbscrLocalChargingPrevention based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrLocalChargingPrevention_Type.__name__ = "Integer32"
_X25SapSbscrLocalChargingPrevention_Object = MibTableColumn
x25SapSbscrLocalChargingPrevention = _X25SapSbscrLocalChargingPrevention_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 90),
    _X25SapSbscrLocalChargingPrevention_Type()
)
x25SapSbscrLocalChargingPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrLocalChargingPrevention.setStatus("mandatory")


class _X25SapSbscrChargingInformation_Type(Integer32):
    """Custom type x25SapSbscrChargingInformation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrChargingInformation_Type.__name__ = "Integer32"
_X25SapSbscrChargingInformation_Object = MibTableColumn
x25SapSbscrChargingInformation = _X25SapSbscrChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 91),
    _X25SapSbscrChargingInformation_Type()
)
x25SapSbscrChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrChargingInformation.setStatus("mandatory")


class _X25SapSbscrCallRedirection_Type(Integer32):
    """Custom type x25SapSbscrCallRedirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCallRedirection_Type.__name__ = "Integer32"
_X25SapSbscrCallRedirection_Object = MibTableColumn
x25SapSbscrCallRedirection = _X25SapSbscrCallRedirection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 92),
    _X25SapSbscrCallRedirection_Type()
)
x25SapSbscrCallRedirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCallRedirection.setStatus("mandatory")


class _X25SapSbscrPermissionToRedirect_Type(Integer32):
    """Custom type x25SapSbscrPermissionToRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrPermissionToRedirect_Type.__name__ = "Integer32"
_X25SapSbscrPermissionToRedirect_Object = MibTableColumn
x25SapSbscrPermissionToRedirect = _X25SapSbscrPermissionToRedirect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 93),
    _X25SapSbscrPermissionToRedirect_Type()
)
x25SapSbscrPermissionToRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrPermissionToRedirect.setStatus("mandatory")
_X25SapRedirectionAddress_Type = X25Address
_X25SapRedirectionAddress_Object = MibTableColumn
x25SapRedirectionAddress = _X25SapRedirectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 94),
    _X25SapRedirectionAddress_Type()
)
x25SapRedirectionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRedirectionAddress.setStatus("mandatory")


class _X25SapSbscrNetworkUserId_Type(Integer32):
    """Custom type x25SapSbscrNetworkUserId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrNetworkUserId_Type.__name__ = "Integer32"
_X25SapSbscrNetworkUserId_Object = MibTableColumn
x25SapSbscrNetworkUserId = _X25SapSbscrNetworkUserId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 95),
    _X25SapSbscrNetworkUserId_Type()
)
x25SapSbscrNetworkUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrNetworkUserId.setStatus("mandatory")


class _X25SapSbscrCallingAddressValidation_Type(Integer32):
    """Custom type x25SapSbscrCallingAddressValidation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCallingAddressValidation_Type.__name__ = "Integer32"
_X25SapSbscrCallingAddressValidation_Object = MibTableColumn
x25SapSbscrCallingAddressValidation = _X25SapSbscrCallingAddressValidation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 96),
    _X25SapSbscrCallingAddressValidation_Type()
)
x25SapSbscrCallingAddressValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCallingAddressValidation.setStatus("mandatory")
_X25SapSourceAddress_Type = X25Address
_X25SapSourceAddress_Object = MibTableColumn
x25SapSourceAddress = _X25SapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 97),
    _X25SapSourceAddress_Type()
)
x25SapSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSourceAddress.setStatus("mandatory")


class _X25SapSbscrRouteUsingCUDF_Type(Integer32):
    """Custom type x25SapSbscrRouteUsingCUDF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrRouteUsingCUDF_Type.__name__ = "Integer32"
_X25SapSbscrRouteUsingCUDF_Object = MibTableColumn
x25SapSbscrRouteUsingCUDF = _X25SapSbscrRouteUsingCUDF_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 98),
    _X25SapSbscrRouteUsingCUDF_Type()
)
x25SapSbscrRouteUsingCUDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrRouteUsingCUDF.setStatus("mandatory")


class _X25SapSbscrRouteUsingSubAddress_Type(Integer32):
    """Custom type x25SapSbscrRouteUsingSubAddress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrRouteUsingSubAddress_Type.__name__ = "Integer32"
_X25SapSbscrRouteUsingSubAddress_Object = MibTableColumn
x25SapSbscrRouteUsingSubAddress = _X25SapSbscrRouteUsingSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 99),
    _X25SapSbscrRouteUsingSubAddress_Type()
)
x25SapSbscrRouteUsingSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrRouteUsingSubAddress.setStatus("mandatory")


class _X25SapSbscrRouteUsingCAE_Type(Integer32):
    """Custom type x25SapSbscrRouteUsingCAE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrRouteUsingCAE_Type.__name__ = "Integer32"
_X25SapSbscrRouteUsingCAE_Object = MibTableColumn
x25SapSbscrRouteUsingCAE = _X25SapSbscrRouteUsingCAE_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 100),
    _X25SapSbscrRouteUsingCAE_Type()
)
x25SapSbscrRouteUsingCAE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrRouteUsingCAE.setStatus("mandatory")


class _X25SapRouteAddressLength_Type(Integer32):
    """Custom type x25SapRouteAddressLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_X25SapRouteAddressLength_Type.__name__ = "Integer32"
_X25SapRouteAddressLength_Object = MibTableColumn
x25SapRouteAddressLength = _X25SapRouteAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 101),
    _X25SapRouteAddressLength_Type()
)
x25SapRouteAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapRouteAddressLength.setStatus("mandatory")


class _X25SapSbscrTransitDelay_Type(Integer32):
    """Custom type x25SapSbscrTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrTransitDelay_Type.__name__ = "Integer32"
_X25SapSbscrTransitDelay_Object = MibTableColumn
x25SapSbscrTransitDelay = _X25SapSbscrTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 102),
    _X25SapSbscrTransitDelay_Type()
)
x25SapSbscrTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrTransitDelay.setStatus("mandatory")


class _X25SapTransitDelay_Type(Integer32):
    """Custom type x25SapTransitDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25SapTransitDelay_Type.__name__ = "Integer32"
_X25SapTransitDelay_Object = MibTableColumn
x25SapTransitDelay = _X25SapTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 103),
    _X25SapTransitDelay_Type()
)
x25SapTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapTransitDelay.setStatus("mandatory")


class _X25SapSbscrCugIncomingAccess_Type(Integer32):
    """Custom type x25SapSbscrCugIncomingAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCugIncomingAccess_Type.__name__ = "Integer32"
_X25SapSbscrCugIncomingAccess_Object = MibTableColumn
x25SapSbscrCugIncomingAccess = _X25SapSbscrCugIncomingAccess_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 104),
    _X25SapSbscrCugIncomingAccess_Type()
)
x25SapSbscrCugIncomingAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCugIncomingAccess.setStatus("mandatory")


class _X25SapSbscrCugOutgoingAccess_Type(Integer32):
    """Custom type x25SapSbscrCugOutgoingAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25SapSbscrCugOutgoingAccess_Type.__name__ = "Integer32"
_X25SapSbscrCugOutgoingAccess_Object = MibTableColumn
x25SapSbscrCugOutgoingAccess = _X25SapSbscrCugOutgoingAccess_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 105),
    _X25SapSbscrCugOutgoingAccess_Type()
)
x25SapSbscrCugOutgoingAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapSbscrCugOutgoingAccess.setStatus("mandatory")


class _X25SapPreferentialCugIndex_Type(CugIndex):
    """Custom type x25SapPreferentialCugIndex based on CugIndex"""
    defaultValue = 0


_X25SapPreferentialCugIndex_Object = MibTableColumn
x25SapPreferentialCugIndex = _X25SapPreferentialCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 106),
    _X25SapPreferentialCugIndex_Type()
)
x25SapPreferentialCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25SapPreferentialCugIndex.setStatus("mandatory")


class _X25SapControl_Type(Integer32):
    """Custom type x25SapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 1),
          ("disableSap", 3),
          ("enableSap", 2))
    )


_X25SapControl_Type.__name__ = "Integer32"
_X25SapControl_Object = MibTableColumn
x25SapControl = _X25SapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 120),
    _X25SapControl_Type()
)
x25SapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x25SapControl.setStatus("mandatory")


class _X25SapLinkState_Type(Integer32):
    """Custom type x25SapLinkState based on Integer32"""
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
        *(("connecting", 1),
          ("dataTransfer", 2),
          ("down", 5),
          ("restartExternal", 4),
          ("restartInternal", 3))
    )


_X25SapLinkState_Type.__name__ = "Integer32"
_X25SapLinkState_Object = MibTableColumn
x25SapLinkState = _X25SapLinkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 125),
    _X25SapLinkState_Type()
)
x25SapLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapLinkState.setStatus("mandatory")


class _X25SapFlowControlState_Type(Integer32):
    """Custom type x25SapFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flowNormal", 1),
          ("flowStopped", 2),
          ("noFlow", 3))
    )


_X25SapFlowControlState_Type.__name__ = "Integer32"
_X25SapFlowControlState_Object = MibTableColumn
x25SapFlowControlState = _X25SapFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 21, 1, 126),
    _X25SapFlowControlState_Type()
)
x25SapFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapFlowControlState.setStatus("mandatory")
_X25SapStatsTable_Object = MibTable
x25SapStatsTable = _X25SapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22)
)
if mibBuilder.loadTexts:
    x25SapStatsTable.setStatus("mandatory")
_X25SapStatsEntry_Object = MibTableRow
x25SapStatsEntry = _X25SapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1)
)
x25SapStatsEntry.setIndexNames(
    (0, "CXX25-MIB", "x25SapStatsSapNumber"),
    (0, "CXX25-MIB", "x25SapStatsSapCes"),
)
if mibBuilder.loadTexts:
    x25SapStatsEntry.setStatus("mandatory")
_X25SapStatsSapNumber_Type = SapIndex
_X25SapStatsSapNumber_Object = MibTableColumn
x25SapStatsSapNumber = _X25SapStatsSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 1),
    _X25SapStatsSapNumber_Type()
)
x25SapStatsSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsSapNumber.setStatus("mandatory")
_X25SapStatsSapCes_Type = Ces
_X25SapStatsSapCes_Object = MibTableColumn
x25SapStatsSapCes = _X25SapStatsSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 2),
    _X25SapStatsSapCes_Type()
)
x25SapStatsSapCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsSapCes.setStatus("mandatory")
_X25SapStatsTxDataPkts_Type = Counter32
_X25SapStatsTxDataPkts_Object = MibTableColumn
x25SapStatsTxDataPkts = _X25SapStatsTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 3),
    _X25SapStatsTxDataPkts_Type()
)
x25SapStatsTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxDataPkts.setStatus("mandatory")
_X25SapStatsRxDataPkts_Type = Counter32
_X25SapStatsRxDataPkts_Object = MibTableColumn
x25SapStatsRxDataPkts = _X25SapStatsRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 4),
    _X25SapStatsRxDataPkts_Type()
)
x25SapStatsRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxDataPkts.setStatus("mandatory")
_X25SapStatsTxDataChars_Type = Counter32
_X25SapStatsTxDataChars_Object = MibTableColumn
x25SapStatsTxDataChars = _X25SapStatsTxDataChars_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 5),
    _X25SapStatsTxDataChars_Type()
)
x25SapStatsTxDataChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxDataChars.setStatus("mandatory")
_X25SapStatsRxDataChars_Type = Counter32
_X25SapStatsRxDataChars_Object = MibTableColumn
x25SapStatsRxDataChars = _X25SapStatsRxDataChars_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 6),
    _X25SapStatsRxDataChars_Type()
)
x25SapStatsRxDataChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxDataChars.setStatus("mandatory")
_X25SapStatsTxQDataPkts_Type = Counter32
_X25SapStatsTxQDataPkts_Object = MibTableColumn
x25SapStatsTxQDataPkts = _X25SapStatsTxQDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 7),
    _X25SapStatsTxQDataPkts_Type()
)
x25SapStatsTxQDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxQDataPkts.setStatus("mandatory")
_X25SapStatsRxQDataPkts_Type = Counter32
_X25SapStatsRxQDataPkts_Object = MibTableColumn
x25SapStatsRxQDataPkts = _X25SapStatsRxQDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 8),
    _X25SapStatsRxQDataPkts_Type()
)
x25SapStatsRxQDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxQDataPkts.setStatus("mandatory")
_X25SapStatsTxQDataChars_Type = Counter32
_X25SapStatsTxQDataChars_Object = MibTableColumn
x25SapStatsTxQDataChars = _X25SapStatsTxQDataChars_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 9),
    _X25SapStatsTxQDataChars_Type()
)
x25SapStatsTxQDataChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxQDataChars.setStatus("mandatory")
_X25SapStatsRxQDataChars_Type = Counter32
_X25SapStatsRxQDataChars_Object = MibTableColumn
x25SapStatsRxQDataChars = _X25SapStatsRxQDataChars_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 10),
    _X25SapStatsRxQDataChars_Type()
)
x25SapStatsRxQDataChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxQDataChars.setStatus("mandatory")
_X25SapStatsTxCallPkts_Type = Counter32
_X25SapStatsTxCallPkts_Object = MibTableColumn
x25SapStatsTxCallPkts = _X25SapStatsTxCallPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 11),
    _X25SapStatsTxCallPkts_Type()
)
x25SapStatsTxCallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxCallPkts.setStatus("mandatory")
_X25SapStatsRxCallPkts_Type = Counter32
_X25SapStatsRxCallPkts_Object = MibTableColumn
x25SapStatsRxCallPkts = _X25SapStatsRxCallPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 12),
    _X25SapStatsRxCallPkts_Type()
)
x25SapStatsRxCallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxCallPkts.setStatus("mandatory")
_X25SapStatsTxClrPkts_Type = Counter32
_X25SapStatsTxClrPkts_Object = MibTableColumn
x25SapStatsTxClrPkts = _X25SapStatsTxClrPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 13),
    _X25SapStatsTxClrPkts_Type()
)
x25SapStatsTxClrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxClrPkts.setStatus("mandatory")
_X25SapStatsRxClrPkts_Type = Counter32
_X25SapStatsRxClrPkts_Object = MibTableColumn
x25SapStatsRxClrPkts = _X25SapStatsRxClrPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 14),
    _X25SapStatsRxClrPkts_Type()
)
x25SapStatsRxClrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxClrPkts.setStatus("mandatory")
_X25SapStatsTxRRPkts_Type = Counter32
_X25SapStatsTxRRPkts_Object = MibTableColumn
x25SapStatsTxRRPkts = _X25SapStatsTxRRPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 15),
    _X25SapStatsTxRRPkts_Type()
)
x25SapStatsTxRRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxRRPkts.setStatus("mandatory")
_X25SapStatsRxRRPkts_Type = Counter32
_X25SapStatsRxRRPkts_Object = MibTableColumn
x25SapStatsRxRRPkts = _X25SapStatsRxRRPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 16),
    _X25SapStatsRxRRPkts_Type()
)
x25SapStatsRxRRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxRRPkts.setStatus("mandatory")
_X25SapStatsTxRNRPkts_Type = Counter32
_X25SapStatsTxRNRPkts_Object = MibTableColumn
x25SapStatsTxRNRPkts = _X25SapStatsTxRNRPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 17),
    _X25SapStatsTxRNRPkts_Type()
)
x25SapStatsTxRNRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxRNRPkts.setStatus("mandatory")
_X25SapStatsRxRNRPkts_Type = Counter32
_X25SapStatsRxRNRPkts_Object = MibTableColumn
x25SapStatsRxRNRPkts = _X25SapStatsRxRNRPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 18),
    _X25SapStatsRxRNRPkts_Type()
)
x25SapStatsRxRNRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxRNRPkts.setStatus("mandatory")
_X25SapStatsTxResPkts_Type = Counter32
_X25SapStatsTxResPkts_Object = MibTableColumn
x25SapStatsTxResPkts = _X25SapStatsTxResPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 19),
    _X25SapStatsTxResPkts_Type()
)
x25SapStatsTxResPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxResPkts.setStatus("mandatory")
_X25SapStatsRxResPkts_Type = Counter32
_X25SapStatsRxResPkts_Object = MibTableColumn
x25SapStatsRxResPkts = _X25SapStatsRxResPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 20),
    _X25SapStatsRxResPkts_Type()
)
x25SapStatsRxResPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxResPkts.setStatus("mandatory")
_X25SapStatsTxRstPkts_Type = Counter32
_X25SapStatsTxRstPkts_Object = MibTableColumn
x25SapStatsTxRstPkts = _X25SapStatsTxRstPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 21),
    _X25SapStatsTxRstPkts_Type()
)
x25SapStatsTxRstPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxRstPkts.setStatus("mandatory")
_X25SapStatsRxRstPkts_Type = Counter32
_X25SapStatsRxRstPkts_Object = MibTableColumn
x25SapStatsRxRstPkts = _X25SapStatsRxRstPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 22),
    _X25SapStatsRxRstPkts_Type()
)
x25SapStatsRxRstPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxRstPkts.setStatus("mandatory")
_X25SapStatsTxIntPkts_Type = Counter32
_X25SapStatsTxIntPkts_Object = MibTableColumn
x25SapStatsTxIntPkts = _X25SapStatsTxIntPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 23),
    _X25SapStatsTxIntPkts_Type()
)
x25SapStatsTxIntPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxIntPkts.setStatus("mandatory")
_X25SapStatsRxIntPkts_Type = Counter32
_X25SapStatsRxIntPkts_Object = MibTableColumn
x25SapStatsRxIntPkts = _X25SapStatsRxIntPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 24),
    _X25SapStatsRxIntPkts_Type()
)
x25SapStatsRxIntPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxIntPkts.setStatus("mandatory")
_X25SapStatsTxDiagPkts_Type = Counter32
_X25SapStatsTxDiagPkts_Object = MibTableColumn
x25SapStatsTxDiagPkts = _X25SapStatsTxDiagPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 25),
    _X25SapStatsTxDiagPkts_Type()
)
x25SapStatsTxDiagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsTxDiagPkts.setStatus("mandatory")
_X25SapStatsRxDiagPkts_Type = Counter32
_X25SapStatsRxDiagPkts_Object = MibTableColumn
x25SapStatsRxDiagPkts = _X25SapStatsRxDiagPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 26),
    _X25SapStatsRxDiagPkts_Type()
)
x25SapStatsRxDiagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxDiagPkts.setStatus("mandatory")
_X25SapStatsRxInvPkts_Type = Counter32
_X25SapStatsRxInvPkts_Object = MibTableColumn
x25SapStatsRxInvPkts = _X25SapStatsRxInvPkts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 27),
    _X25SapStatsRxInvPkts_Type()
)
x25SapStatsRxInvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsRxInvPkts.setStatus("mandatory")
_X25SapStatsCons_Type = Counter32
_X25SapStatsCons_Object = MibTableColumn
x25SapStatsCons = _X25SapStatsCons_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 28),
    _X25SapStatsCons_Type()
)
x25SapStatsCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsCons.setStatus("mandatory")
_X25SapStatsDiscs_Type = Counter32
_X25SapStatsDiscs_Object = MibTableColumn
x25SapStatsDiscs = _X25SapStatsDiscs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 29),
    _X25SapStatsDiscs_Type()
)
x25SapStatsDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsDiscs.setStatus("mandatory")
_X25SapStatsLastCauseCode_Type = Counter32
_X25SapStatsLastCauseCode_Object = MibTableColumn
x25SapStatsLastCauseCode = _X25SapStatsLastCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 30),
    _X25SapStatsLastCauseCode_Type()
)
x25SapStatsLastCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsLastCauseCode.setStatus("mandatory")
_X25SapStatsLastDiagCode_Type = Counter32
_X25SapStatsLastDiagCode_Object = MibTableColumn
x25SapStatsLastDiagCode = _X25SapStatsLastDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 31),
    _X25SapStatsLastDiagCode_Type()
)
x25SapStatsLastDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsLastDiagCode.setStatus("mandatory")
_X25SapStatsActiveLcns_Type = Counter32
_X25SapStatsActiveLcns_Object = MibTableColumn
x25SapStatsActiveLcns = _X25SapStatsActiveLcns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 22, 1, 32),
    _X25SapStatsActiveLcns_Type()
)
x25SapStatsActiveLcns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SapStatsActiveLcns.setStatus("mandatory")
_X25CugTable_Object = MibTable
x25CugTable = _X25CugTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23)
)
if mibBuilder.loadTexts:
    x25CugTable.setStatus("mandatory")
_X25CugEntry_Object = MibTableRow
x25CugEntry = _X25CugEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1)
)
x25CugEntry.setIndexNames(
    (0, "CXX25-MIB", "x25CugSapNumber"),
    (0, "CXX25-MIB", "x25CugSapCes"),
    (0, "CXX25-MIB", "x25CugIndex"),
)
if mibBuilder.loadTexts:
    x25CugEntry.setStatus("mandatory")
_X25CugSapNumber_Type = SapIndex
_X25CugSapNumber_Object = MibTableColumn
x25CugSapNumber = _X25CugSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 1),
    _X25CugSapNumber_Type()
)
x25CugSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CugSapNumber.setStatus("mandatory")
_X25CugSapCes_Type = Ces
_X25CugSapCes_Object = MibTableColumn
x25CugSapCes = _X25CugSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 2),
    _X25CugSapCes_Type()
)
x25CugSapCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CugSapCes.setStatus("mandatory")
_X25CugIndex_Type = CugIndex
_X25CugIndex_Object = MibTableColumn
x25CugIndex = _X25CugIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 3),
    _X25CugIndex_Type()
)
x25CugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CugIndex.setStatus("mandatory")


class _X25CugRowStatus_Type(Integer32):
    """Custom type x25CugRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25CugRowStatus_Type.__name__ = "Integer32"
_X25CugRowStatus_Object = MibTableColumn
x25CugRowStatus = _X25CugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 4),
    _X25CugRowStatus_Type()
)
x25CugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CugRowStatus.setStatus("mandatory")
_X25CugInterlockCode_Type = CugIC
_X25CugInterlockCode_Object = MibTableColumn
x25CugInterlockCode = _X25CugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 5),
    _X25CugInterlockCode_Type()
)
x25CugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CugInterlockCode.setStatus("mandatory")


class _X25CugSbscrInCallsBarred_Type(Integer32):
    """Custom type x25CugSbscrInCallsBarred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25CugSbscrInCallsBarred_Type.__name__ = "Integer32"
_X25CugSbscrInCallsBarred_Object = MibTableColumn
x25CugSbscrInCallsBarred = _X25CugSbscrInCallsBarred_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 6),
    _X25CugSbscrInCallsBarred_Type()
)
x25CugSbscrInCallsBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CugSbscrInCallsBarred.setStatus("mandatory")


class _X25CugSbscrOutCallsBarred_Type(Integer32):
    """Custom type x25CugSbscrOutCallsBarred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25CugSbscrOutCallsBarred_Type.__name__ = "Integer32"
_X25CugSbscrOutCallsBarred_Object = MibTableColumn
x25CugSbscrOutCallsBarred = _X25CugSbscrOutCallsBarred_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 7),
    _X25CugSbscrOutCallsBarred_Type()
)
x25CugSbscrOutCallsBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CugSbscrOutCallsBarred.setStatus("mandatory")


class _X25CugEntryState_Type(Integer32):
    """Custom type x25CugEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 1),
          ("onLine", 2))
    )


_X25CugEntryState_Type.__name__ = "Integer32"
_X25CugEntryState_Object = MibTableColumn
x25CugEntryState = _X25CugEntryState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 23, 1, 8),
    _X25CugEntryState_Type()
)
x25CugEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CugEntryState.setStatus("mandatory")
_X25RouteTable_Object = MibTable
x25RouteTable = _X25RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24)
)
if mibBuilder.loadTexts:
    x25RouteTable.setStatus("mandatory")
_X25RouteEntry_Object = MibTableRow
x25RouteEntry = _X25RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1)
)
x25RouteEntry.setIndexNames(
    (0, "CXX25-MIB", "x25RoutePartition"),
    (0, "CXX25-MIB", "x25RouteId"),
)
if mibBuilder.loadTexts:
    x25RouteEntry.setStatus("mandatory")
_X25RoutePartition_Type = RoutePartition
_X25RoutePartition_Object = MibTableColumn
x25RoutePartition = _X25RoutePartition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 1),
    _X25RoutePartition_Type()
)
x25RoutePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RoutePartition.setStatus("mandatory")
_X25RouteId_Type = RouteIndex
_X25RouteId_Object = MibTableColumn
x25RouteId = _X25RouteId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 2),
    _X25RouteId_Type()
)
x25RouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RouteId.setStatus("mandatory")


class _X25RouteRowStatus_Type(Integer32):
    """Custom type x25RouteRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25RouteRowStatus_Type.__name__ = "Integer32"
_X25RouteRowStatus_Object = MibTableColumn
x25RouteRowStatus = _X25RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 3),
    _X25RouteRowStatus_Type()
)
x25RouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteRowStatus.setStatus("mandatory")


class _X25RouteType_Type(Integer32):
    """Custom type x25RouteType based on Integer32"""
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
        *(("huntGroup", 4),
          ("logicalLink", 3),
          ("specLowerSap", 2),
          ("specUpperSap", 1))
    )


_X25RouteType_Type.__name__ = "Integer32"
_X25RouteType_Object = MibTableColumn
x25RouteType = _X25RouteType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 4),
    _X25RouteType_Type()
)
x25RouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteType.setStatus("mandatory")
_X25RouteAddress_Type = X25Address
_X25RouteAddress_Object = MibTableColumn
x25RouteAddress = _X25RouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 5),
    _X25RouteAddress_Type()
)
x25RouteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteAddress.setStatus("mandatory")
_X25RouteSLHNumber_Type = SapIndex
_X25RouteSLHNumber_Object = MibTableColumn
x25RouteSLHNumber = _X25RouteSLHNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 6),
    _X25RouteSLHNumber_Type()
)
x25RouteSLHNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteSLHNumber.setStatus("mandatory")


class _X25RouteSapCes_Type(Ces):
    """Custom type x25RouteSapCes based on Ces"""
    defaultValue = 0


_X25RouteSapCes_Object = MibTableColumn
x25RouteSapCes = _X25RouteSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 7),
    _X25RouteSapCes_Type()
)
x25RouteSapCes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25RouteSapCes.setStatus("mandatory")


class _X25RouteEntryState_Type(Integer32):
    """Custom type x25RouteEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 1),
          ("onLine", 2))
    )


_X25RouteEntryState_Type.__name__ = "Integer32"
_X25RouteEntryState_Object = MibTableColumn
x25RouteEntryState = _X25RouteEntryState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 24, 1, 8),
    _X25RouteEntryState_Type()
)
x25RouteEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RouteEntryState.setStatus("mandatory")
_X25HuntGroupTable_Object = MibTable
x25HuntGroupTable = _X25HuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25)
)
if mibBuilder.loadTexts:
    x25HuntGroupTable.setStatus("mandatory")
_X25HuntGroupEntry_Object = MibTableRow
x25HuntGroupEntry = _X25HuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1)
)
x25HuntGroupEntry.setIndexNames(
    (0, "CXX25-MIB", "x25HGId"),
    (0, "CXX25-MIB", "x25HGMemberIndex"),
)
if mibBuilder.loadTexts:
    x25HuntGroupEntry.setStatus("mandatory")
_X25HGId_Type = HGIndex
_X25HGId_Object = MibTableColumn
x25HGId = _X25HGId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1, 1),
    _X25HGId_Type()
)
x25HGId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGId.setStatus("mandatory")
_X25HGMemberIndex_Type = HGIndex
_X25HGMemberIndex_Object = MibTableColumn
x25HGMemberIndex = _X25HGMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1, 2),
    _X25HGMemberIndex_Type()
)
x25HGMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGMemberIndex.setStatus("mandatory")
_X25HGSapNumber_Type = SapIndex
_X25HGSapNumber_Object = MibTableColumn
x25HGSapNumber = _X25HGSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1, 3),
    _X25HGSapNumber_Type()
)
x25HGSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25HGSapNumber.setStatus("mandatory")


class _X25HGSapCes_Type(Ces):
    """Custom type x25HGSapCes based on Ces"""
    defaultValue = 0


_X25HGSapCes_Object = MibTableColumn
x25HGSapCes = _X25HGSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1, 4),
    _X25HGSapCes_Type()
)
x25HGSapCes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25HGSapCes.setStatus("mandatory")


class _X25HGRowStatus_Type(Integer32):
    """Custom type x25HGRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25HGRowStatus_Type.__name__ = "Integer32"
_X25HGRowStatus_Object = MibTableColumn
x25HGRowStatus = _X25HGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 25, 1, 5),
    _X25HGRowStatus_Type()
)
x25HGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25HGRowStatus.setStatus("mandatory")
_X25HuntGroupOperTable_Object = MibTable
x25HuntGroupOperTable = _X25HuntGroupOperTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26)
)
if mibBuilder.loadTexts:
    x25HuntGroupOperTable.setStatus("mandatory")
_X25HuntGroupOperEntry_Object = MibTableRow
x25HuntGroupOperEntry = _X25HuntGroupOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26, 1)
)
x25HuntGroupOperEntry.setIndexNames(
    (0, "CXX25-MIB", "x25HGOperId"),
    (0, "CXX25-MIB", "x25HGOperMemberIndex"),
)
if mibBuilder.loadTexts:
    x25HuntGroupOperEntry.setStatus("mandatory")
_X25HGOperId_Type = HGIndex
_X25HGOperId_Object = MibTableColumn
x25HGOperId = _X25HGOperId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26, 1, 1),
    _X25HGOperId_Type()
)
x25HGOperId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGOperId.setStatus("mandatory")
_X25HGOperMemberIndex_Type = HGIndex
_X25HGOperMemberIndex_Object = MibTableColumn
x25HGOperMemberIndex = _X25HGOperMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26, 1, 2),
    _X25HGOperMemberIndex_Type()
)
x25HGOperMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGOperMemberIndex.setStatus("mandatory")
_X25HGOperSapNumber_Type = SapIndex
_X25HGOperSapNumber_Object = MibTableColumn
x25HGOperSapNumber = _X25HGOperSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26, 1, 3),
    _X25HGOperSapNumber_Type()
)
x25HGOperSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGOperSapNumber.setStatus("mandatory")
_X25HGOperSapCes_Type = Ces
_X25HGOperSapCes_Object = MibTableColumn
x25HGOperSapCes = _X25HGOperSapCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 26, 1, 4),
    _X25HGOperSapCes_Type()
)
x25HGOperSapCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HGOperSapCes.setStatus("mandatory")
_X25PvcTable_Object = MibTable
x25PvcTable = _X25PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27)
)
if mibBuilder.loadTexts:
    x25PvcTable.setStatus("mandatory")
_X25PvcEntry_Object = MibTableRow
x25PvcEntry = _X25PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1)
)
x25PvcEntry.setIndexNames(
    (0, "CXX25-MIB", "x25PvcId"),
)
if mibBuilder.loadTexts:
    x25PvcEntry.setStatus("mandatory")
_X25PvcId_Type = PvcIndex
_X25PvcId_Object = MibTableColumn
x25PvcId = _X25PvcId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 1),
    _X25PvcId_Type()
)
x25PvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PvcId.setStatus("mandatory")


class _X25PvcRowStatus_Type(Integer32):
    """Custom type x25PvcRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_X25PvcRowStatus_Type.__name__ = "Integer32"
_X25PvcRowStatus_Object = MibTableColumn
x25PvcRowStatus = _X25PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 2),
    _X25PvcRowStatus_Type()
)
x25PvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcRowStatus.setStatus("mandatory")
_X25PvcSrcSap_Type = SapIndex
_X25PvcSrcSap_Object = MibTableColumn
x25PvcSrcSap = _X25PvcSrcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 3),
    _X25PvcSrcSap_Type()
)
x25PvcSrcSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcSap.setStatus("mandatory")


class _X25PvcSrcCes_Type(Ces):
    """Custom type x25PvcSrcCes based on Ces"""
    defaultValue = 0


_X25PvcSrcCes_Object = MibTableColumn
x25PvcSrcCes = _X25PvcSrcCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 4),
    _X25PvcSrcCes_Type()
)
x25PvcSrcCes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcCes.setStatus("mandatory")
_X25PvcDstSap_Type = SapIndex
_X25PvcDstSap_Object = MibTableColumn
x25PvcDstSap = _X25PvcDstSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 5),
    _X25PvcDstSap_Type()
)
x25PvcDstSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstSap.setStatus("mandatory")


class _X25PvcDstCes_Type(Ces):
    """Custom type x25PvcDstCes based on Ces"""
    defaultValue = 0


_X25PvcDstCes_Object = MibTableColumn
x25PvcDstCes = _X25PvcDstCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 6),
    _X25PvcDstCes_Type()
)
x25PvcDstCes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstCes.setStatus("mandatory")


class _X25PvcSrcLcn_Type(Integer32):
    """Custom type x25PvcSrcLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_X25PvcSrcLcn_Type.__name__ = "Integer32"
_X25PvcSrcLcn_Object = MibTableColumn
x25PvcSrcLcn = _X25PvcSrcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 7),
    _X25PvcSrcLcn_Type()
)
x25PvcSrcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcLcn.setStatus("mandatory")


class _X25PvcDstLcn_Type(Integer32):
    """Custom type x25PvcDstLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_X25PvcDstLcn_Type.__name__ = "Integer32"
_X25PvcDstLcn_Object = MibTableColumn
x25PvcDstLcn = _X25PvcDstLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 8),
    _X25PvcDstLcn_Type()
)
x25PvcDstLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstLcn.setStatus("mandatory")


class _X25PvcSrcRxPacketSize_Type(PacketSize):
    """Custom type x25PvcSrcRxPacketSize based on PacketSize"""


_X25PvcSrcRxPacketSize_Object = MibTableColumn
x25PvcSrcRxPacketSize = _X25PvcSrcRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 9),
    _X25PvcSrcRxPacketSize_Type()
)
x25PvcSrcRxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcRxPacketSize.setStatus("mandatory")


class _X25PvcSrcTxPacketSize_Type(PacketSize):
    """Custom type x25PvcSrcTxPacketSize based on PacketSize"""


_X25PvcSrcTxPacketSize_Object = MibTableColumn
x25PvcSrcTxPacketSize = _X25PvcSrcTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 10),
    _X25PvcSrcTxPacketSize_Type()
)
x25PvcSrcTxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcTxPacketSize.setStatus("mandatory")


class _X25PvcDstRxPacketSize_Type(PacketSize):
    """Custom type x25PvcDstRxPacketSize based on PacketSize"""


_X25PvcDstRxPacketSize_Object = MibTableColumn
x25PvcDstRxPacketSize = _X25PvcDstRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 11),
    _X25PvcDstRxPacketSize_Type()
)
x25PvcDstRxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstRxPacketSize.setStatus("mandatory")


class _X25PvcDstTxPacketSize_Type(PacketSize):
    """Custom type x25PvcDstTxPacketSize based on PacketSize"""


_X25PvcDstTxPacketSize_Object = MibTableColumn
x25PvcDstTxPacketSize = _X25PvcDstTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 12),
    _X25PvcDstTxPacketSize_Type()
)
x25PvcDstTxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstTxPacketSize.setStatus("mandatory")


class _X25PvcRxWindow_Type(Integer32):
    """Custom type x25PvcRxWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25PvcRxWindow_Type.__name__ = "Integer32"
_X25PvcRxWindow_Object = MibTableColumn
x25PvcRxWindow = _X25PvcRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 13),
    _X25PvcRxWindow_Type()
)
x25PvcRxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcRxWindow.setStatus("mandatory")


class _X25PvcTxWindow_Type(Integer32):
    """Custom type x25PvcTxWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25PvcTxWindow_Type.__name__ = "Integer32"
_X25PvcTxWindow_Object = MibTableColumn
x25PvcTxWindow = _X25PvcTxWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 14),
    _X25PvcTxWindow_Type()
)
x25PvcTxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcTxWindow.setStatus("mandatory")


class _X25PvcRxThruputClass_Type(ThruputClass):
    """Custom type x25PvcRxThruputClass based on ThruputClass"""


_X25PvcRxThruputClass_Object = MibTableColumn
x25PvcRxThruputClass = _X25PvcRxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 15),
    _X25PvcRxThruputClass_Type()
)
x25PvcRxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcRxThruputClass.setStatus("mandatory")


class _X25PvcTxThruputClass_Type(ThruputClass):
    """Custom type x25PvcTxThruputClass based on ThruputClass"""


_X25PvcTxThruputClass_Object = MibTableColumn
x25PvcTxThruputClass = _X25PvcTxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 16),
    _X25PvcTxThruputClass_Type()
)
x25PvcTxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcTxThruputClass.setStatus("mandatory")


class _X25PvcBilling_Type(Integer32):
    """Custom type x25PvcBilling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25PvcBilling_Type.__name__ = "Integer32"
_X25PvcBilling_Object = MibTableColumn
x25PvcBilling = _X25PvcBilling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 17),
    _X25PvcBilling_Type()
)
x25PvcBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcBilling.setStatus("mandatory")
_X25PvcSrcAddress_Type = X25Address
_X25PvcSrcAddress_Object = MibTableColumn
x25PvcSrcAddress = _X25PvcSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 18),
    _X25PvcSrcAddress_Type()
)
x25PvcSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcSrcAddress.setStatus("mandatory")
_X25PvcDstAddress_Type = X25Address
_X25PvcDstAddress_Object = MibTableColumn
x25PvcDstAddress = _X25PvcDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 19),
    _X25PvcDstAddress_Type()
)
x25PvcDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PvcDstAddress.setStatus("mandatory")


class _X25PvcEntryState_Type(Integer32):
    """Custom type x25PvcEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 1),
          ("onLine", 2))
    )


_X25PvcEntryState_Type.__name__ = "Integer32"
_X25PvcEntryState_Object = MibTableColumn
x25PvcEntryState = _X25PvcEntryState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 27, 1, 20),
    _X25PvcEntryState_Type()
)
x25PvcEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PvcEntryState.setStatus("mandatory")
_X25LcnStatusTable_Object = MibTable
x25LcnStatusTable = _X25LcnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28)
)
if mibBuilder.loadTexts:
    x25LcnStatusTable.setStatus("mandatory")
_X25LcnStatusEntry_Object = MibTableRow
x25LcnStatusEntry = _X25LcnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1)
)
x25LcnStatusEntry.setIndexNames(
    (0, "CXX25-MIB", "x25LcnSrcSap"),
    (0, "CXX25-MIB", "x25LcnSrcCes"),
    (0, "CXX25-MIB", "x25LcnSrcLcn"),
)
if mibBuilder.loadTexts:
    x25LcnStatusEntry.setStatus("mandatory")
_X25LcnSrcSap_Type = SapIndex
_X25LcnSrcSap_Object = MibTableColumn
x25LcnSrcSap = _X25LcnSrcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 1),
    _X25LcnSrcSap_Type()
)
x25LcnSrcSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnSrcSap.setStatus("mandatory")
_X25LcnSrcCes_Type = Ces
_X25LcnSrcCes_Object = MibTableColumn
x25LcnSrcCes = _X25LcnSrcCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 2),
    _X25LcnSrcCes_Type()
)
x25LcnSrcCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnSrcCes.setStatus("mandatory")
_X25LcnSrcLcn_Type = Lcn
_X25LcnSrcLcn_Object = MibTableColumn
x25LcnSrcLcn = _X25LcnSrcLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 3),
    _X25LcnSrcLcn_Type()
)
x25LcnSrcLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnSrcLcn.setStatus("mandatory")
_X25LcnDstSap_Type = SapIndex
_X25LcnDstSap_Object = MibTableColumn
x25LcnDstSap = _X25LcnDstSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 4),
    _X25LcnDstSap_Type()
)
x25LcnDstSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnDstSap.setStatus("mandatory")
_X25LcnDstCes_Type = Ces
_X25LcnDstCes_Object = MibTableColumn
x25LcnDstCes = _X25LcnDstCes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 5),
    _X25LcnDstCes_Type()
)
x25LcnDstCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnDstCes.setStatus("mandatory")
_X25LcnDstLcn_Type = Lcn
_X25LcnDstLcn_Object = MibTableColumn
x25LcnDstLcn = _X25LcnDstLcn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 6),
    _X25LcnDstLcn_Type()
)
x25LcnDstLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnDstLcn.setStatus("mandatory")


class _X25LcnDBitCall_Type(Integer32):
    """Custom type x25LcnDBitCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnDBitCall_Type.__name__ = "Integer32"
_X25LcnDBitCall_Object = MibTableColumn
x25LcnDBitCall = _X25LcnDBitCall_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 20),
    _X25LcnDBitCall_Type()
)
x25LcnDBitCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnDBitCall.setStatus("mandatory")


class _X25LcnPvc_Type(Integer32):
    """Custom type x25LcnPvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnPvc_Type.__name__ = "Integer32"
_X25LcnPvc_Object = MibTableColumn
x25LcnPvc = _X25LcnPvc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 21),
    _X25LcnPvc_Type()
)
x25LcnPvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnPvc.setStatus("mandatory")


class _X25LcnModulo_Type(Integer32):
    """Custom type x25LcnModulo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25LcnModulo_Type.__name__ = "Integer32"
_X25LcnModulo_Object = MibTableColumn
x25LcnModulo = _X25LcnModulo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 22),
    _X25LcnModulo_Type()
)
x25LcnModulo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnModulo.setStatus("mandatory")


class _X25LcnState_Type(Integer32):
    """Custom type x25LcnState based on Integer32"""
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
        *(("stateConnecting", 2),
          ("stateDataTransfer", 3),
          ("stateDisconnecting", 4),
          ("stateReady", 1),
          ("stateResettingBoth", 7),
          ("stateResettingCdSide", 6),
          ("stateResettingCgSide", 5))
    )


_X25LcnState_Type.__name__ = "Integer32"
_X25LcnState_Object = MibTableColumn
x25LcnState = _X25LcnState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 23),
    _X25LcnState_Type()
)
x25LcnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnState.setStatus("mandatory")


class _X25LcnTxRnr_Type(Integer32):
    """Custom type x25LcnTxRnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnTxRnr_Type.__name__ = "Integer32"
_X25LcnTxRnr_Object = MibTableColumn
x25LcnTxRnr = _X25LcnTxRnr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 30),
    _X25LcnTxRnr_Type()
)
x25LcnTxRnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnTxRnr.setStatus("mandatory")


class _X25LcnRxRnr_Type(Integer32):
    """Custom type x25LcnRxRnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnRxRnr_Type.__name__ = "Integer32"
_X25LcnRxRnr_Object = MibTableColumn
x25LcnRxRnr = _X25LcnRxRnr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 31),
    _X25LcnRxRnr_Type()
)
x25LcnRxRnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnRxRnr.setStatus("mandatory")


class _X25LcnTxWindowSize_Type(Integer32):
    """Custom type x25LcnTxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LcnTxWindowSize_Type.__name__ = "Integer32"
_X25LcnTxWindowSize_Object = MibTableColumn
x25LcnTxWindowSize = _X25LcnTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 32),
    _X25LcnTxWindowSize_Type()
)
x25LcnTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnTxWindowSize.setStatus("mandatory")


class _X25LcnRxWindowSize_Type(Integer32):
    """Custom type x25LcnRxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25LcnRxWindowSize_Type.__name__ = "Integer32"
_X25LcnRxWindowSize_Object = MibTableColumn
x25LcnRxWindowSize = _X25LcnRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 33),
    _X25LcnRxWindowSize_Type()
)
x25LcnRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnRxWindowSize.setStatus("mandatory")


class _X25LcnTxPacketSize_Type(Integer32):
    """Custom type x25LcnTxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_X25LcnTxPacketSize_Type.__name__ = "Integer32"
_X25LcnTxPacketSize_Object = MibTableColumn
x25LcnTxPacketSize = _X25LcnTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 34),
    _X25LcnTxPacketSize_Type()
)
x25LcnTxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnTxPacketSize.setStatus("mandatory")


class _X25LcnRxPacketSize_Type(Integer32):
    """Custom type x25LcnRxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_X25LcnRxPacketSize_Type.__name__ = "Integer32"
_X25LcnRxPacketSize_Object = MibTableColumn
x25LcnRxPacketSize = _X25LcnRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 35),
    _X25LcnRxPacketSize_Type()
)
x25LcnRxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnRxPacketSize.setStatus("mandatory")


class _X25LcnTxThruputClass_Type(Integer32):
    """Custom type x25LcnTxThruputClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 64000),
    )


_X25LcnTxThruputClass_Type.__name__ = "Integer32"
_X25LcnTxThruputClass_Object = MibTableColumn
x25LcnTxThruputClass = _X25LcnTxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 36),
    _X25LcnTxThruputClass_Type()
)
x25LcnTxThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnTxThruputClass.setStatus("mandatory")


class _X25LcnRxThruputClass_Type(Integer32):
    """Custom type x25LcnRxThruputClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 64000),
    )


_X25LcnRxThruputClass_Type.__name__ = "Integer32"
_X25LcnRxThruputClass_Object = MibTableColumn
x25LcnRxThruputClass = _X25LcnRxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 37),
    _X25LcnRxThruputClass_Type()
)
x25LcnRxThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnRxThruputClass.setStatus("mandatory")
_X25LcnSrcAddress_Type = X25Address
_X25LcnSrcAddress_Object = MibTableColumn
x25LcnSrcAddress = _X25LcnSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 50),
    _X25LcnSrcAddress_Type()
)
x25LcnSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnSrcAddress.setStatus("mandatory")
_X25LcnDstAddress_Type = X25Address
_X25LcnDstAddress_Object = MibTableColumn
x25LcnDstAddress = _X25LcnDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 51),
    _X25LcnDstAddress_Type()
)
x25LcnDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnDstAddress.setStatus("mandatory")
_X25LcnTxQLength_Type = Integer32
_X25LcnTxQLength_Object = MibTableColumn
x25LcnTxQLength = _X25LcnTxQLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 60),
    _X25LcnTxQLength_Type()
)
x25LcnTxQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnTxQLength.setStatus("mandatory")
_X25LcnNextTransmitPs_Type = Integer32
_X25LcnNextTransmitPs_Object = MibTableColumn
x25LcnNextTransmitPs = _X25LcnNextTransmitPs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 61),
    _X25LcnNextTransmitPs_Type()
)
x25LcnNextTransmitPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnNextTransmitPs.setStatus("mandatory")
_X25LcnNextExpectedPs_Type = Integer32
_X25LcnNextExpectedPs_Object = MibTableColumn
x25LcnNextExpectedPs = _X25LcnNextExpectedPs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 62),
    _X25LcnNextExpectedPs_Type()
)
x25LcnNextExpectedPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnNextExpectedPs.setStatus("mandatory")
_X25LcnLastTransmittedPr_Type = Integer32
_X25LcnLastTransmittedPr_Object = MibTableColumn
x25LcnLastTransmittedPr = _X25LcnLastTransmittedPr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 63),
    _X25LcnLastTransmittedPr_Type()
)
x25LcnLastTransmittedPr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnLastTransmittedPr.setStatus("mandatory")
_X25LcnLastReceivedPr_Type = Integer32
_X25LcnLastReceivedPr_Object = MibTableColumn
x25LcnLastReceivedPr = _X25LcnLastReceivedPr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 64),
    _X25LcnLastReceivedPr_Type()
)
x25LcnLastReceivedPr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnLastReceivedPr.setStatus("mandatory")


class _X25LcnFCTimerRunning_Type(Integer32):
    """Custom type x25LcnFCTimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnFCTimerRunning_Type.__name__ = "Integer32"
_X25LcnFCTimerRunning_Object = MibTableColumn
x25LcnFCTimerRunning = _X25LcnFCTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 80),
    _X25LcnFCTimerRunning_Type()
)
x25LcnFCTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnFCTimerRunning.setStatus("mandatory")


class _X25LcnT24TimerRunning_Type(Integer32):
    """Custom type x25LcnT24TimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnT24TimerRunning_Type.__name__ = "Integer32"
_X25LcnT24TimerRunning_Object = MibTableColumn
x25LcnT24TimerRunning = _X25LcnT24TimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 81),
    _X25LcnT24TimerRunning_Type()
)
x25LcnT24TimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnT24TimerRunning.setStatus("mandatory")


class _X25LcnInacTimerRunning_Type(Integer32):
    """Custom type x25LcnInacTimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnInacTimerRunning_Type.__name__ = "Integer32"
_X25LcnInacTimerRunning_Object = MibTableColumn
x25LcnInacTimerRunning = _X25LcnInacTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 82),
    _X25LcnInacTimerRunning_Type()
)
x25LcnInacTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnInacTimerRunning.setStatus("mandatory")


class _X25LcnCalTimerRunning_Type(Integer32):
    """Custom type x25LcnCalTimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnCalTimerRunning_Type.__name__ = "Integer32"
_X25LcnCalTimerRunning_Object = MibTableColumn
x25LcnCalTimerRunning = _X25LcnCalTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 83),
    _X25LcnCalTimerRunning_Type()
)
x25LcnCalTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnCalTimerRunning.setStatus("mandatory")


class _X25LcnClrTimerRunning_Type(Integer32):
    """Custom type x25LcnClrTimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnClrTimerRunning_Type.__name__ = "Integer32"
_X25LcnClrTimerRunning_Object = MibTableColumn
x25LcnClrTimerRunning = _X25LcnClrTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 84),
    _X25LcnClrTimerRunning_Type()
)
x25LcnClrTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnClrTimerRunning.setStatus("mandatory")


class _X25LcnResTimerRunning_Type(Integer32):
    """Custom type x25LcnResTimerRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_X25LcnResTimerRunning_Type.__name__ = "Integer32"
_X25LcnResTimerRunning_Object = MibTableColumn
x25LcnResTimerRunning = _X25LcnResTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 28, 1, 85),
    _X25LcnResTimerRunning_Type()
)
x25LcnResTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LcnResTimerRunning.setStatus("mandatory")


class _X25MibLevel_Type(Integer32):
    """Custom type x25MibLevel based on Integer32"""
    defaultValue = 0


_X25MibLevel_Object = MibScalar
x25MibLevel = _X25MibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 30),
    _X25MibLevel_Type()
)
x25MibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects

x25SapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 0, 1)
)
x25SapAlarm.setObjects(
      *(("CXX25-MIB", "x25SapNumber"),
        ("CXX25-MIB", "x25SapCes"),
        ("CXX25-MIB", "x25SapStatusEvent"))
)
if mibBuilder.loadTexts:
    x25SapAlarm.setStatus(
        ""
    )

x25ConfigErrorIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29, 0, 2)
)
x25ConfigErrorIndication.setObjects(
      *(("CXX25-MIB", "x25SapNumber"),
        ("CXX25-MIB", "x25SapCes"),
        ("CXX25-MIB", "x25ConfigErrorEvent"))
)
if mibBuilder.loadTexts:
    x25ConfigErrorIndication.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXX25-MIB",
    **{"SapType": SapType,
       "PacketSize": PacketSize,
       "Ces": Ces,
       "Lcn": Lcn,
       "CugIndex": CugIndex,
       "CugIC": CugIC,
       "RoutePartition": RoutePartition,
       "RouteIndex": RouteIndex,
       "HGIndex": HGIndex,
       "PvcIndex": PvcIndex,
       "X25Address": X25Address,
       "x25SapAlarm": x25SapAlarm,
       "x25ConfigErrorIndication": x25ConfigErrorIndication,
       "x25LowerPoolThreshold": x25LowerPoolThreshold,
       "x25UpperPoolThreshold": x25UpperPoolThreshold,
       "x25RouteMask": x25RouteMask,
       "x25BillingSegmentSize": x25BillingSegmentSize,
       "x25Billing": x25Billing,
       "x25NetworkType": x25NetworkType,
       "x25HuntGroupRotation": x25HuntGroupRotation,
       "x25Alarms": x25Alarms,
       "x25SapStatusEvent": x25SapStatusEvent,
       "x25ConfigErrorEvent": x25ConfigErrorEvent,
       "x25SoftwareVersions": x25SoftwareVersions,
       "x25LogicalLinkTable": x25LogicalLinkTable,
       "x25LogicalLinkEntry": x25LogicalLinkEntry,
       "x25LLNumber": x25LLNumber,
       "x25LLSapNumber": x25LLSapNumber,
       "x25LLSapCes": x25LLSapCes,
       "x25LLRowStatus": x25LLRowStatus,
       "x25LLRouteAlgorithm": x25LLRouteAlgorithm,
       "x25LLEntryState": x25LLEntryState,
       "x25SapTable": x25SapTable,
       "x25SapEntry": x25SapEntry,
       "x25SapNumber": x25SapNumber,
       "x25SapCes": x25SapCes,
       "x25SapRowStatus": x25SapRowStatus,
       "x25SapType": x25SapType,
       "x25SapAlias": x25SapAlias,
       "x25SapCompanionAlias": x25SapCompanionAlias,
       "x25SapInterfaceType": x25SapInterfaceType,
       "x25SapLinkType": x25SapLinkType,
       "x25SapRoutePartition": x25SapRoutePartition,
       "x25SapRouteDirection": x25SapRouteDirection,
       "x25SapWildCardRouting": x25SapWildCardRouting,
       "x25SapWildCardRoutingMask": x25SapWildCardRoutingMask,
       "x25SapActivation": x25SapActivation,
       "x25SapPvcBillingTimer": x25SapPvcBillingTimer,
       "x25SapModulo": x25SapModulo,
       "x25SapRxPacketSize": x25SapRxPacketSize,
       "x25SapTxPacketSize": x25SapTxPacketSize,
       "x25SapRxWindowSize": x25SapRxWindowSize,
       "x25SapTxWindowSize": x25SapTxWindowSize,
       "x25SapRxThruputClass": x25SapRxThruputClass,
       "x25SapTxThruputClass": x25SapTxThruputClass,
       "x25SapRxWindowThreshold": x25SapRxWindowThreshold,
       "x25SapLcnAllocation": x25SapLcnAllocation,
       "x25SapLpvcLcn": x25SapLpvcLcn,
       "x25SapHpvcLcn": x25SapHpvcLcn,
       "x25SapLicLcn": x25SapLicLcn,
       "x25SapHicLcn": x25SapHicLcn,
       "x25SapLtcLcn": x25SapLtcLcn,
       "x25SapHtcLcn": x25SapHtcLcn,
       "x25SapLocLcn": x25SapLocLcn,
       "x25SapHocLcn": x25SapHocLcn,
       "x25SapConnectTimer": x25SapConnectTimer,
       "x25SapDisconnectTimer": x25SapDisconnectTimer,
       "x25SapRestartTimer": x25SapRestartTimer,
       "x25SapCallTimer": x25SapCallTimer,
       "x25SapResetTimer": x25SapResetTimer,
       "x25SapClearTimer": x25SapClearTimer,
       "x25SapInactivityTimer": x25SapInactivityTimer,
       "x25SapFlowControlTimer": x25SapFlowControlTimer,
       "x25SapWindowStatusTimer": x25SapWindowStatusTimer,
       "x25SapSbscrCalledAddressInsertion": x25SapSbscrCalledAddressInsertion,
       "x25SapSbscrCallingAddressInsertion": x25SapSbscrCallingAddressInsertion,
       "x25SapSbscrPktRetransmission": x25SapSbscrPktRetransmission,
       "x25SapSbscrInAccessBarred": x25SapSbscrInAccessBarred,
       "x25SapSbscrOutAccessBarred": x25SapSbscrOutAccessBarred,
       "x25SapSbscrFlowCntrlParamNegotiation": x25SapSbscrFlowCntrlParamNegotiation,
       "x25SapSbscrThruputClassNegotiation": x25SapSbscrThruputClassNegotiation,
       "x25SapSbscrFastSelect": x25SapSbscrFastSelect,
       "x25SapSbscrFastSelectAcceptance": x25SapSbscrFastSelectAcceptance,
       "x25SapSbscrReverseChargingAcceptance": x25SapSbscrReverseChargingAcceptance,
       "x25SapSbscrLocalChargingPrevention": x25SapSbscrLocalChargingPrevention,
       "x25SapSbscrChargingInformation": x25SapSbscrChargingInformation,
       "x25SapSbscrCallRedirection": x25SapSbscrCallRedirection,
       "x25SapSbscrPermissionToRedirect": x25SapSbscrPermissionToRedirect,
       "x25SapRedirectionAddress": x25SapRedirectionAddress,
       "x25SapSbscrNetworkUserId": x25SapSbscrNetworkUserId,
       "x25SapSbscrCallingAddressValidation": x25SapSbscrCallingAddressValidation,
       "x25SapSourceAddress": x25SapSourceAddress,
       "x25SapSbscrRouteUsingCUDF": x25SapSbscrRouteUsingCUDF,
       "x25SapSbscrRouteUsingSubAddress": x25SapSbscrRouteUsingSubAddress,
       "x25SapSbscrRouteUsingCAE": x25SapSbscrRouteUsingCAE,
       "x25SapRouteAddressLength": x25SapRouteAddressLength,
       "x25SapSbscrTransitDelay": x25SapSbscrTransitDelay,
       "x25SapTransitDelay": x25SapTransitDelay,
       "x25SapSbscrCugIncomingAccess": x25SapSbscrCugIncomingAccess,
       "x25SapSbscrCugOutgoingAccess": x25SapSbscrCugOutgoingAccess,
       "x25SapPreferentialCugIndex": x25SapPreferentialCugIndex,
       "x25SapControl": x25SapControl,
       "x25SapLinkState": x25SapLinkState,
       "x25SapFlowControlState": x25SapFlowControlState,
       "x25SapStatsTable": x25SapStatsTable,
       "x25SapStatsEntry": x25SapStatsEntry,
       "x25SapStatsSapNumber": x25SapStatsSapNumber,
       "x25SapStatsSapCes": x25SapStatsSapCes,
       "x25SapStatsTxDataPkts": x25SapStatsTxDataPkts,
       "x25SapStatsRxDataPkts": x25SapStatsRxDataPkts,
       "x25SapStatsTxDataChars": x25SapStatsTxDataChars,
       "x25SapStatsRxDataChars": x25SapStatsRxDataChars,
       "x25SapStatsTxQDataPkts": x25SapStatsTxQDataPkts,
       "x25SapStatsRxQDataPkts": x25SapStatsRxQDataPkts,
       "x25SapStatsTxQDataChars": x25SapStatsTxQDataChars,
       "x25SapStatsRxQDataChars": x25SapStatsRxQDataChars,
       "x25SapStatsTxCallPkts": x25SapStatsTxCallPkts,
       "x25SapStatsRxCallPkts": x25SapStatsRxCallPkts,
       "x25SapStatsTxClrPkts": x25SapStatsTxClrPkts,
       "x25SapStatsRxClrPkts": x25SapStatsRxClrPkts,
       "x25SapStatsTxRRPkts": x25SapStatsTxRRPkts,
       "x25SapStatsRxRRPkts": x25SapStatsRxRRPkts,
       "x25SapStatsTxRNRPkts": x25SapStatsTxRNRPkts,
       "x25SapStatsRxRNRPkts": x25SapStatsRxRNRPkts,
       "x25SapStatsTxResPkts": x25SapStatsTxResPkts,
       "x25SapStatsRxResPkts": x25SapStatsRxResPkts,
       "x25SapStatsTxRstPkts": x25SapStatsTxRstPkts,
       "x25SapStatsRxRstPkts": x25SapStatsRxRstPkts,
       "x25SapStatsTxIntPkts": x25SapStatsTxIntPkts,
       "x25SapStatsRxIntPkts": x25SapStatsRxIntPkts,
       "x25SapStatsTxDiagPkts": x25SapStatsTxDiagPkts,
       "x25SapStatsRxDiagPkts": x25SapStatsRxDiagPkts,
       "x25SapStatsRxInvPkts": x25SapStatsRxInvPkts,
       "x25SapStatsCons": x25SapStatsCons,
       "x25SapStatsDiscs": x25SapStatsDiscs,
       "x25SapStatsLastCauseCode": x25SapStatsLastCauseCode,
       "x25SapStatsLastDiagCode": x25SapStatsLastDiagCode,
       "x25SapStatsActiveLcns": x25SapStatsActiveLcns,
       "x25CugTable": x25CugTable,
       "x25CugEntry": x25CugEntry,
       "x25CugSapNumber": x25CugSapNumber,
       "x25CugSapCes": x25CugSapCes,
       "x25CugIndex": x25CugIndex,
       "x25CugRowStatus": x25CugRowStatus,
       "x25CugInterlockCode": x25CugInterlockCode,
       "x25CugSbscrInCallsBarred": x25CugSbscrInCallsBarred,
       "x25CugSbscrOutCallsBarred": x25CugSbscrOutCallsBarred,
       "x25CugEntryState": x25CugEntryState,
       "x25RouteTable": x25RouteTable,
       "x25RouteEntry": x25RouteEntry,
       "x25RoutePartition": x25RoutePartition,
       "x25RouteId": x25RouteId,
       "x25RouteRowStatus": x25RouteRowStatus,
       "x25RouteType": x25RouteType,
       "x25RouteAddress": x25RouteAddress,
       "x25RouteSLHNumber": x25RouteSLHNumber,
       "x25RouteSapCes": x25RouteSapCes,
       "x25RouteEntryState": x25RouteEntryState,
       "x25HuntGroupTable": x25HuntGroupTable,
       "x25HuntGroupEntry": x25HuntGroupEntry,
       "x25HGId": x25HGId,
       "x25HGMemberIndex": x25HGMemberIndex,
       "x25HGSapNumber": x25HGSapNumber,
       "x25HGSapCes": x25HGSapCes,
       "x25HGRowStatus": x25HGRowStatus,
       "x25HuntGroupOperTable": x25HuntGroupOperTable,
       "x25HuntGroupOperEntry": x25HuntGroupOperEntry,
       "x25HGOperId": x25HGOperId,
       "x25HGOperMemberIndex": x25HGOperMemberIndex,
       "x25HGOperSapNumber": x25HGOperSapNumber,
       "x25HGOperSapCes": x25HGOperSapCes,
       "x25PvcTable": x25PvcTable,
       "x25PvcEntry": x25PvcEntry,
       "x25PvcId": x25PvcId,
       "x25PvcRowStatus": x25PvcRowStatus,
       "x25PvcSrcSap": x25PvcSrcSap,
       "x25PvcSrcCes": x25PvcSrcCes,
       "x25PvcDstSap": x25PvcDstSap,
       "x25PvcDstCes": x25PvcDstCes,
       "x25PvcSrcLcn": x25PvcSrcLcn,
       "x25PvcDstLcn": x25PvcDstLcn,
       "x25PvcSrcRxPacketSize": x25PvcSrcRxPacketSize,
       "x25PvcSrcTxPacketSize": x25PvcSrcTxPacketSize,
       "x25PvcDstRxPacketSize": x25PvcDstRxPacketSize,
       "x25PvcDstTxPacketSize": x25PvcDstTxPacketSize,
       "x25PvcRxWindow": x25PvcRxWindow,
       "x25PvcTxWindow": x25PvcTxWindow,
       "x25PvcRxThruputClass": x25PvcRxThruputClass,
       "x25PvcTxThruputClass": x25PvcTxThruputClass,
       "x25PvcBilling": x25PvcBilling,
       "x25PvcSrcAddress": x25PvcSrcAddress,
       "x25PvcDstAddress": x25PvcDstAddress,
       "x25PvcEntryState": x25PvcEntryState,
       "x25LcnStatusTable": x25LcnStatusTable,
       "x25LcnStatusEntry": x25LcnStatusEntry,
       "x25LcnSrcSap": x25LcnSrcSap,
       "x25LcnSrcCes": x25LcnSrcCes,
       "x25LcnSrcLcn": x25LcnSrcLcn,
       "x25LcnDstSap": x25LcnDstSap,
       "x25LcnDstCes": x25LcnDstCes,
       "x25LcnDstLcn": x25LcnDstLcn,
       "x25LcnDBitCall": x25LcnDBitCall,
       "x25LcnPvc": x25LcnPvc,
       "x25LcnModulo": x25LcnModulo,
       "x25LcnState": x25LcnState,
       "x25LcnTxRnr": x25LcnTxRnr,
       "x25LcnRxRnr": x25LcnRxRnr,
       "x25LcnTxWindowSize": x25LcnTxWindowSize,
       "x25LcnRxWindowSize": x25LcnRxWindowSize,
       "x25LcnTxPacketSize": x25LcnTxPacketSize,
       "x25LcnRxPacketSize": x25LcnRxPacketSize,
       "x25LcnTxThruputClass": x25LcnTxThruputClass,
       "x25LcnRxThruputClass": x25LcnRxThruputClass,
       "x25LcnSrcAddress": x25LcnSrcAddress,
       "x25LcnDstAddress": x25LcnDstAddress,
       "x25LcnTxQLength": x25LcnTxQLength,
       "x25LcnNextTransmitPs": x25LcnNextTransmitPs,
       "x25LcnNextExpectedPs": x25LcnNextExpectedPs,
       "x25LcnLastTransmittedPr": x25LcnLastTransmittedPr,
       "x25LcnLastReceivedPr": x25LcnLastReceivedPr,
       "x25LcnFCTimerRunning": x25LcnFCTimerRunning,
       "x25LcnT24TimerRunning": x25LcnT24TimerRunning,
       "x25LcnInacTimerRunning": x25LcnInacTimerRunning,
       "x25LcnCalTimerRunning": x25LcnCalTimerRunning,
       "x25LcnClrTimerRunning": x25LcnClrTimerRunning,
       "x25LcnResTimerRunning": x25LcnResTimerRunning,
       "x25MibLevel": x25MibLevel}
)
