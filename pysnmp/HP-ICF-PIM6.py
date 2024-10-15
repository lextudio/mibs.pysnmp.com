# SNMP MIB module (HP-ICF-PIM6) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-PIM6
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:58 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(pimRPSetComponent,) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimRPSetComponent")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfPim6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122)
)
hpicfPim6MIB.setRevisions(
        ("2017-10-10 00:00",
         "2017-07-03 00:00",
         "2012-04-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfPim6Objects_ObjectIdentity = ObjectIdentity
hpicfPim6Objects = _HpicfPim6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1)
)
_HpicfPim6Traps_ObjectIdentity = ObjectIdentity
hpicfPim6Traps = _HpicfPim6Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 0)
)
_HpicfPim6_ObjectIdentity = ObjectIdentity
hpicfPim6 = _HpicfPim6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1)
)


class _HpicfPim6AdminStatus_Type(Integer32):
    """Custom type hpicfPim6AdminStatus based on Integer32"""
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


_HpicfPim6AdminStatus_Type.__name__ = "Integer32"
_HpicfPim6AdminStatus_Object = MibScalar
hpicfPim6AdminStatus = _HpicfPim6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 1),
    _HpicfPim6AdminStatus_Type()
)
hpicfPim6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6AdminStatus.setStatus("current")


class _HpicfPim6StateRefreshInterval_Type(Integer32):
    """Custom type hpicfPim6StateRefreshInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_HpicfPim6StateRefreshInterval_Type.__name__ = "Integer32"
_HpicfPim6StateRefreshInterval_Object = MibScalar
hpicfPim6StateRefreshInterval = _HpicfPim6StateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 2),
    _HpicfPim6StateRefreshInterval_Type()
)
hpicfPim6StateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6StateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6StateRefreshInterval.setUnits("seconds")


class _HpicfPim6TrapControl_Type(Bits):
    """Custom type hpicfPim6TrapControl based on Bits"""
    namedValues = NamedValues(
        *(("hardMrtFull", 1),
          ("neighborLoss", 0),
          ("softMrtFull", 2))
    )

_HpicfPim6TrapControl_Type.__name__ = "Bits"
_HpicfPim6TrapControl_Object = MibScalar
hpicfPim6TrapControl = _HpicfPim6TrapControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 3),
    _HpicfPim6TrapControl_Type()
)
hpicfPim6TrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6TrapControl.setStatus("current")
_HpicfPim6IfTable_Object = MibTable
hpicfPim6IfTable = _HpicfPim6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfPim6IfTable.setStatus("current")
_HpicfPim6IfEntry_Object = MibTableRow
hpicfPim6IfEntry = _HpicfPim6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1)
)
hpicfPim6IfEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6IfIndex"),
)
if mibBuilder.loadTexts:
    hpicfPim6IfEntry.setStatus("current")
_HpicfPim6IfIndex_Type = InterfaceIndex
_HpicfPim6IfIndex_Object = MibTableColumn
hpicfPim6IfIndex = _HpicfPim6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 1),
    _HpicfPim6IfIndex_Type()
)
hpicfPim6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IfIndex.setStatus("current")
_HpicfPim6IfAddressType_Type = InetAddressType
_HpicfPim6IfAddressType_Object = MibTableColumn
hpicfPim6IfAddressType = _HpicfPim6IfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 2),
    _HpicfPim6IfAddressType_Type()
)
hpicfPim6IfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfAddressType.setStatus("current")


class _HpicfPim6IfAddress_Type(InetAddress):
    """Custom type hpicfPim6IfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IfAddress_Type.__name__ = "InetAddress"
_HpicfPim6IfAddress_Object = MibTableColumn
hpicfPim6IfAddress = _HpicfPim6IfAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 3),
    _HpicfPim6IfAddress_Type()
)
hpicfPim6IfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfAddress.setStatus("current")


class _HpicfPim6IfMode_Type(Integer32):
    """Custom type hpicfPim6IfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_HpicfPim6IfMode_Type.__name__ = "Integer32"
_HpicfPim6IfMode_Object = MibTableColumn
hpicfPim6IfMode = _HpicfPim6IfMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 4),
    _HpicfPim6IfMode_Type()
)
hpicfPim6IfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfMode.setStatus("current")


class _HpicfPim6IfTrigHelloInterval_Type(Unsigned32):
    """Custom type hpicfPim6IfTrigHelloInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HpicfPim6IfTrigHelloInterval_Type.__name__ = "Unsigned32"
_HpicfPim6IfTrigHelloInterval_Object = MibTableColumn
hpicfPim6IfTrigHelloInterval = _HpicfPim6IfTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 5),
    _HpicfPim6IfTrigHelloInterval_Type()
)
hpicfPim6IfTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfTrigHelloInterval.setUnits("seconds")


class _HpicfPim6IfHelloHoldtime_Type(Unsigned32):
    """Custom type hpicfPim6IfHelloHoldtime based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPim6IfHelloHoldtime_Type.__name__ = "Unsigned32"
_HpicfPim6IfHelloHoldtime_Object = MibTableColumn
hpicfPim6IfHelloHoldtime = _HpicfPim6IfHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 6),
    _HpicfPim6IfHelloHoldtime_Type()
)
hpicfPim6IfHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfHelloHoldtime.setUnits("seconds")


class _HpicfPim6IfLanPruneDelay_Type(TruthValue):
    """Custom type hpicfPim6IfLanPruneDelay based on TruthValue"""


_HpicfPim6IfLanPruneDelay_Object = MibTableColumn
hpicfPim6IfLanPruneDelay = _HpicfPim6IfLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 7),
    _HpicfPim6IfLanPruneDelay_Type()
)
hpicfPim6IfLanPruneDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfLanPruneDelay.setStatus("current")


class _HpicfPim6IfPropagationDelay_Type(Unsigned32):
    """Custom type hpicfPim6IfPropagationDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 2000),
    )


_HpicfPim6IfPropagationDelay_Type.__name__ = "Unsigned32"
_HpicfPim6IfPropagationDelay_Object = MibTableColumn
hpicfPim6IfPropagationDelay = _HpicfPim6IfPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 8),
    _HpicfPim6IfPropagationDelay_Type()
)
hpicfPim6IfPropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfPropagationDelay.setUnits("milliseconds")


class _HpicfPim6IfOverrideInterval_Type(Unsigned32):
    """Custom type hpicfPim6IfOverrideInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 6000),
    )


_HpicfPim6IfOverrideInterval_Type.__name__ = "Unsigned32"
_HpicfPim6IfOverrideInterval_Object = MibTableColumn
hpicfPim6IfOverrideInterval = _HpicfPim6IfOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 9),
    _HpicfPim6IfOverrideInterval_Type()
)
hpicfPim6IfOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfOverrideInterval.setUnits("milliseconds")


class _HpicfPim6IfGenerationID_Type(TruthValue):
    """Custom type hpicfPim6IfGenerationID based on TruthValue"""


_HpicfPim6IfGenerationID_Object = MibTableColumn
hpicfPim6IfGenerationID = _HpicfPim6IfGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 10),
    _HpicfPim6IfGenerationID_Type()
)
hpicfPim6IfGenerationID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfGenerationID.setStatus("current")


class _HpicfPim6IfJoinPruneHoldtime_Type(Unsigned32):
    """Custom type hpicfPim6IfJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPim6IfJoinPruneHoldtime_Type.__name__ = "Unsigned32"
_HpicfPim6IfJoinPruneHoldtime_Object = MibTableColumn
hpicfPim6IfJoinPruneHoldtime = _HpicfPim6IfJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 11),
    _HpicfPim6IfJoinPruneHoldtime_Type()
)
hpicfPim6IfJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfJoinPruneHoldtime.setUnits("seconds")


class _HpicfPim6IfGraftRetryInterval_Type(Unsigned32):
    """Custom type hpicfPim6IfGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfPim6IfGraftRetryInterval_Type.__name__ = "Unsigned32"
_HpicfPim6IfGraftRetryInterval_Object = MibTableColumn
hpicfPim6IfGraftRetryInterval = _HpicfPim6IfGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 12),
    _HpicfPim6IfGraftRetryInterval_Type()
)
hpicfPim6IfGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfGraftRetryInterval.setUnits("seconds")


class _HpicfPim6IfMaxGraftRetries_Type(Integer32):
    """Custom type hpicfPim6IfMaxGraftRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfPim6IfMaxGraftRetries_Type.__name__ = "Integer32"
_HpicfPim6IfMaxGraftRetries_Object = MibTableColumn
hpicfPim6IfMaxGraftRetries = _HpicfPim6IfMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 13),
    _HpicfPim6IfMaxGraftRetries_Type()
)
hpicfPim6IfMaxGraftRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfMaxGraftRetries.setStatus("current")


class _HpicfPim6IfSRTTLThreshold_Type(Unsigned32):
    """Custom type hpicfPim6IfSRTTLThreshold based on Unsigned32"""
    defaultValue = 0


_HpicfPim6IfSRTTLThreshold_Object = MibTableColumn
hpicfPim6IfSRTTLThreshold = _HpicfPim6IfSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 14),
    _HpicfPim6IfSRTTLThreshold_Type()
)
hpicfPim6IfSRTTLThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfSRTTLThreshold.setStatus("current")
_HpicfPim6IfLanDelayEnabled_Type = TruthValue
_HpicfPim6IfLanDelayEnabled_Object = MibTableColumn
hpicfPim6IfLanDelayEnabled = _HpicfPim6IfLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 15),
    _HpicfPim6IfLanDelayEnabled_Type()
)
hpicfPim6IfLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfLanDelayEnabled.setStatus("current")
_HpicfPim6IfSRCapable_Type = TruthValue
_HpicfPim6IfSRCapable_Object = MibTableColumn
hpicfPim6IfSRCapable = _HpicfPim6IfSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 16),
    _HpicfPim6IfSRCapable_Type()
)
hpicfPim6IfSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfSRCapable.setStatus("current")


class _HpicfPim6IfNBRTimeout_Type(Integer32):
    """Custom type hpicfPim6IfNBRTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_HpicfPim6IfNBRTimeout_Type.__name__ = "Integer32"
_HpicfPim6IfNBRTimeout_Object = MibTableColumn
hpicfPim6IfNBRTimeout = _HpicfPim6IfNBRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 17),
    _HpicfPim6IfNBRTimeout_Type()
)
hpicfPim6IfNBRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfNBRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfNBRTimeout.setUnits("seconds")
_HpicfPim6IfNBRCount_Type = Counter32
_HpicfPim6IfNBRCount_Object = MibTableColumn
hpicfPim6IfNBRCount = _HpicfPim6IfNBRCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 18),
    _HpicfPim6IfNBRCount_Type()
)
hpicfPim6IfNBRCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfNBRCount.setStatus("current")
_HpicfPim6IfNegotiatedPropagationDelay_Type = TimeTicks
_HpicfPim6IfNegotiatedPropagationDelay_Object = MibTableColumn
hpicfPim6IfNegotiatedPropagationDelay = _HpicfPim6IfNegotiatedPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 19),
    _HpicfPim6IfNegotiatedPropagationDelay_Type()
)
hpicfPim6IfNegotiatedPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfNegotiatedPropagationDelay.setStatus("current")
_HpicfPim6IfNegotiatedOverrideInterval_Type = TimeTicks
_HpicfPim6IfNegotiatedOverrideInterval_Object = MibTableColumn
hpicfPim6IfNegotiatedOverrideInterval = _HpicfPim6IfNegotiatedOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 20),
    _HpicfPim6IfNegotiatedOverrideInterval_Type()
)
hpicfPim6IfNegotiatedOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfNegotiatedOverrideInterval.setStatus("current")
_HpicfPim6IfAssertHoldInterval_Type = Counter32
_HpicfPim6IfAssertHoldInterval_Object = MibTableColumn
hpicfPim6IfAssertHoldInterval = _HpicfPim6IfAssertHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 21),
    _HpicfPim6IfAssertHoldInterval_Type()
)
hpicfPim6IfAssertHoldInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfAssertHoldInterval.setStatus("current")
_HpicfPim6IfNumRoutersNotUsingLanDelay_Type = Counter32
_HpicfPim6IfNumRoutersNotUsingLanDelay_Object = MibTableColumn
hpicfPim6IfNumRoutersNotUsingLanDelay = _HpicfPim6IfNumRoutersNotUsingLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 22),
    _HpicfPim6IfNumRoutersNotUsingLanDelay_Type()
)
hpicfPim6IfNumRoutersNotUsingLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfNumRoutersNotUsingLanDelay.setStatus("current")


class _HpicfPim6IfHelloInterval_Type(Unsigned32):
    """Custom type hpicfPim6IfHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpicfPim6IfHelloInterval_Type.__name__ = "Unsigned32"
_HpicfPim6IfHelloInterval_Object = MibTableColumn
hpicfPim6IfHelloInterval = _HpicfPim6IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 23),
    _HpicfPim6IfHelloInterval_Type()
)
hpicfPim6IfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IfHelloInterval.setUnits("seconds")
_HpicfPim6IfStatus_Type = RowStatus
_HpicfPim6IfStatus_Object = MibTableColumn
hpicfPim6IfStatus = _HpicfPim6IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 24),
    _HpicfPim6IfStatus_Type()
)
hpicfPim6IfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfStatus.setStatus("current")


class _HpicfPim6IfDRPriority_Type(Unsigned32):
    """Custom type hpicfPim6IfDRPriority based on Unsigned32"""
    defaultValue = 1


_HpicfPim6IfDRPriority_Object = MibTableColumn
hpicfPim6IfDRPriority = _HpicfPim6IfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 25),
    _HpicfPim6IfDRPriority_Type()
)
hpicfPim6IfDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfDRPriority.setStatus("current")
_HpicfPim6IfDRType_Type = InetAddressType
_HpicfPim6IfDRType_Object = MibTableColumn
hpicfPim6IfDRType = _HpicfPim6IfDRType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 26),
    _HpicfPim6IfDRType_Type()
)
hpicfPim6IfDRType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6IfDRType.setStatus("current")


class _HpicfPim6IfDR_Type(InetAddress):
    """Custom type hpicfPim6IfDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IfDR_Type.__name__ = "InetAddress"
_HpicfPim6IfDR_Object = MibTableColumn
hpicfPim6IfDR = _HpicfPim6IfDR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 4, 1, 27),
    _HpicfPim6IfDR_Type()
)
hpicfPim6IfDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IfDR.setStatus("current")


class _HpicfPim6RemoveConfig_Type(TruthValue):
    """Custom type hpicfPim6RemoveConfig based on TruthValue"""


_HpicfPim6RemoveConfig_Object = MibScalar
hpicfPim6RemoveConfig = _HpicfPim6RemoveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 5),
    _HpicfPim6RemoveConfig_Type()
)
hpicfPim6RemoveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6RemoveConfig.setStatus("current")
_HpicfPim6NumStaticRpfEntries_Type = Counter32
_HpicfPim6NumStaticRpfEntries_Object = MibScalar
hpicfPim6NumStaticRpfEntries = _HpicfPim6NumStaticRpfEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 6),
    _HpicfPim6NumStaticRpfEntries_Type()
)
hpicfPim6NumStaticRpfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NumStaticRpfEntries.setStatus("current")
_HpicfPim6Version_Type = Counter32
_HpicfPim6Version_Object = MibScalar
hpicfPim6Version = _HpicfPim6Version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 7),
    _HpicfPim6Version_Type()
)
hpicfPim6Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6Version.setStatus("current")
_HpicfPim6StarGEntries_Type = Counter32
_HpicfPim6StarGEntries_Object = MibScalar
hpicfPim6StarGEntries = _HpicfPim6StarGEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 8),
    _HpicfPim6StarGEntries_Type()
)
hpicfPim6StarGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6StarGEntries.setStatus("current")
_HpicfPim6SGEntries_Type = Counter32
_HpicfPim6SGEntries_Object = MibScalar
hpicfPim6SGEntries = _HpicfPim6SGEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 9),
    _HpicfPim6SGEntries_Type()
)
hpicfPim6SGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6SGEntries.setStatus("current")
_HpicfPim6TotalNeighborCount_Type = Counter32
_HpicfPim6TotalNeighborCount_Object = MibScalar
hpicfPim6TotalNeighborCount = _HpicfPim6TotalNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 10),
    _HpicfPim6TotalNeighborCount_Type()
)
hpicfPim6TotalNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6TotalNeighborCount.setStatus("current")
_HpicfPim6JoinPruneInterval_Type = Integer32
_HpicfPim6JoinPruneInterval_Object = MibScalar
hpicfPim6JoinPruneInterval = _HpicfPim6JoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 11),
    _HpicfPim6JoinPruneInterval_Type()
)
hpicfPim6JoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6JoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6JoinPruneInterval.setUnits("seconds")
_HpicfPim6StaticRPSetTable_Object = MibTable
hpicfPim6StaticRPSetTable = _HpicfPim6StaticRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetTable.setStatus("current")
_HpicfPim6StaticRPSetEntry_Object = MibTableRow
hpicfPim6StaticRPSetEntry = _HpicfPim6StaticRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1)
)
hpicfPim6StaticRPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetGrpAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetGroupAddress"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetGrpMskType"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetGroupMask"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetAddressType"),
    (0, "HP-ICF-PIM6", "hpicfPim6StaticRPSetAddress"),
)
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetEntry.setStatus("current")
_HpicfPim6StaticRPSetGrpAddrType_Type = InetAddressType
_HpicfPim6StaticRPSetGrpAddrType_Object = MibTableColumn
hpicfPim6StaticRPSetGrpAddrType = _HpicfPim6StaticRPSetGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 1),
    _HpicfPim6StaticRPSetGrpAddrType_Type()
)
hpicfPim6StaticRPSetGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetGrpAddrType.setStatus("current")


class _HpicfPim6StaticRPSetGroupAddress_Type(InetAddress):
    """Custom type hpicfPim6StaticRPSetGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6StaticRPSetGroupAddress_Type.__name__ = "InetAddress"
_HpicfPim6StaticRPSetGroupAddress_Object = MibTableColumn
hpicfPim6StaticRPSetGroupAddress = _HpicfPim6StaticRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 2),
    _HpicfPim6StaticRPSetGroupAddress_Type()
)
hpicfPim6StaticRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetGroupAddress.setStatus("current")
_HpicfPim6StaticRPSetGrpMskType_Type = InetAddressType
_HpicfPim6StaticRPSetGrpMskType_Object = MibTableColumn
hpicfPim6StaticRPSetGrpMskType = _HpicfPim6StaticRPSetGrpMskType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 3),
    _HpicfPim6StaticRPSetGrpMskType_Type()
)
hpicfPim6StaticRPSetGrpMskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetGrpMskType.setStatus("current")


class _HpicfPim6StaticRPSetGroupMask_Type(InetAddress):
    """Custom type hpicfPim6StaticRPSetGroupMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6StaticRPSetGroupMask_Type.__name__ = "InetAddress"
_HpicfPim6StaticRPSetGroupMask_Object = MibTableColumn
hpicfPim6StaticRPSetGroupMask = _HpicfPim6StaticRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 4),
    _HpicfPim6StaticRPSetGroupMask_Type()
)
hpicfPim6StaticRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetGroupMask.setStatus("current")
_HpicfPim6StaticRPSetAddressType_Type = InetAddressType
_HpicfPim6StaticRPSetAddressType_Object = MibTableColumn
hpicfPim6StaticRPSetAddressType = _HpicfPim6StaticRPSetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 5),
    _HpicfPim6StaticRPSetAddressType_Type()
)
hpicfPim6StaticRPSetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetAddressType.setStatus("current")


class _HpicfPim6StaticRPSetAddress_Type(InetAddress):
    """Custom type hpicfPim6StaticRPSetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6StaticRPSetAddress_Type.__name__ = "InetAddress"
_HpicfPim6StaticRPSetAddress_Object = MibTableColumn
hpicfPim6StaticRPSetAddress = _HpicfPim6StaticRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 6),
    _HpicfPim6StaticRPSetAddress_Type()
)
hpicfPim6StaticRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetAddress.setStatus("current")


class _HpicfPim6StaticRPSetOverride_Type(TruthValue):
    """Custom type hpicfPim6StaticRPSetOverride based on TruthValue"""


_HpicfPim6StaticRPSetOverride_Object = MibTableColumn
hpicfPim6StaticRPSetOverride = _HpicfPim6StaticRPSetOverride_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 7),
    _HpicfPim6StaticRPSetOverride_Type()
)
hpicfPim6StaticRPSetOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetOverride.setStatus("current")
_HpicfPim6StaticRPSetRowStatus_Type = RowStatus
_HpicfPim6StaticRPSetRowStatus_Object = MibTableColumn
hpicfPim6StaticRPSetRowStatus = _HpicfPim6StaticRPSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 12, 1, 8),
    _HpicfPim6StaticRPSetRowStatus_Type()
)
hpicfPim6StaticRPSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetRowStatus.setStatus("current")
_HpicfPim6CandidateRPTable_Object = MibTable
hpicfPim6CandidateRPTable = _HpicfPim6CandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPTable.setStatus("current")
_HpicfPim6CandidateRPEntry_Object = MibTableRow
hpicfPim6CandidateRPEntry = _HpicfPim6CandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1)
)
hpicfPim6CandidateRPEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6CandidateRPGrpAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6CandidateRPGroupAddress"),
    (0, "HP-ICF-PIM6", "hpicfPim6CandidateRPGrpMskType"),
    (0, "HP-ICF-PIM6", "hpicfPim6CandidateRPGroupMask"),
)
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPEntry.setStatus("current")
_HpicfPim6CandidateRPGrpAddrType_Type = InetAddressType
_HpicfPim6CandidateRPGrpAddrType_Object = MibTableColumn
hpicfPim6CandidateRPGrpAddrType = _HpicfPim6CandidateRPGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 1),
    _HpicfPim6CandidateRPGrpAddrType_Type()
)
hpicfPim6CandidateRPGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPGrpAddrType.setStatus("current")


class _HpicfPim6CandidateRPGroupAddress_Type(InetAddress):
    """Custom type hpicfPim6CandidateRPGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6CandidateRPGroupAddress_Type.__name__ = "InetAddress"
_HpicfPim6CandidateRPGroupAddress_Object = MibTableColumn
hpicfPim6CandidateRPGroupAddress = _HpicfPim6CandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 2),
    _HpicfPim6CandidateRPGroupAddress_Type()
)
hpicfPim6CandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPGroupAddress.setStatus("current")
_HpicfPim6CandidateRPGrpMskType_Type = InetAddressType
_HpicfPim6CandidateRPGrpMskType_Object = MibTableColumn
hpicfPim6CandidateRPGrpMskType = _HpicfPim6CandidateRPGrpMskType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 3),
    _HpicfPim6CandidateRPGrpMskType_Type()
)
hpicfPim6CandidateRPGrpMskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPGrpMskType.setStatus("current")


class _HpicfPim6CandidateRPGroupMask_Type(InetAddress):
    """Custom type hpicfPim6CandidateRPGroupMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6CandidateRPGroupMask_Type.__name__ = "InetAddress"
_HpicfPim6CandidateRPGroupMask_Object = MibTableColumn
hpicfPim6CandidateRPGroupMask = _HpicfPim6CandidateRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 4),
    _HpicfPim6CandidateRPGroupMask_Type()
)
hpicfPim6CandidateRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPGroupMask.setStatus("current")
_HpicfPim6CandidateRPAddressType_Type = InetAddressType
_HpicfPim6CandidateRPAddressType_Object = MibTableColumn
hpicfPim6CandidateRPAddressType = _HpicfPim6CandidateRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 5),
    _HpicfPim6CandidateRPAddressType_Type()
)
hpicfPim6CandidateRPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPAddressType.setStatus("current")


class _HpicfPim6CandidateRPAddress_Type(InetAddress):
    """Custom type hpicfPim6CandidateRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6CandidateRPAddress_Type.__name__ = "InetAddress"
_HpicfPim6CandidateRPAddress_Object = MibTableColumn
hpicfPim6CandidateRPAddress = _HpicfPim6CandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 6),
    _HpicfPim6CandidateRPAddress_Type()
)
hpicfPim6CandidateRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPAddress.setStatus("current")
_HpicfPim6CandidateRPRowStatus_Type = RowStatus
_HpicfPim6CandidateRPRowStatus_Object = MibTableColumn
hpicfPim6CandidateRPRowStatus = _HpicfPim6CandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 13, 1, 7),
    _HpicfPim6CandidateRPRowStatus_Type()
)
hpicfPim6CandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPRowStatus.setStatus("current")
_HpicfPim6ComponentTable_Object = MibTable
hpicfPim6ComponentTable = _HpicfPim6ComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hpicfPim6ComponentTable.setStatus("current")
_HpicfPim6ComponentEntry_Object = MibTableRow
hpicfPim6ComponentEntry = _HpicfPim6ComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1)
)
hpicfPim6ComponentEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6ComponentIndex"),
)
if mibBuilder.loadTexts:
    hpicfPim6ComponentEntry.setStatus("current")


class _HpicfPim6ComponentIndex_Type(Integer32):
    """Custom type hpicfPim6ComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfPim6ComponentIndex_Type.__name__ = "Integer32"
_HpicfPim6ComponentIndex_Object = MibTableColumn
hpicfPim6ComponentIndex = _HpicfPim6ComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 1),
    _HpicfPim6ComponentIndex_Type()
)
hpicfPim6ComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6ComponentIndex.setStatus("current")
_HpicfPim6ComponentBSRAddrType_Type = InetAddressType
_HpicfPim6ComponentBSRAddrType_Object = MibTableColumn
hpicfPim6ComponentBSRAddrType = _HpicfPim6ComponentBSRAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 2),
    _HpicfPim6ComponentBSRAddrType_Type()
)
hpicfPim6ComponentBSRAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRAddrType.setStatus("current")
_HpicfPim6ComponentBSRAddress_Type = InetAddress
_HpicfPim6ComponentBSRAddress_Object = MibTableColumn
hpicfPim6ComponentBSRAddress = _HpicfPim6ComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 3),
    _HpicfPim6ComponentBSRAddress_Type()
)
hpicfPim6ComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRAddress.setStatus("current")
_HpicfPim6ComponentBSRExpiryTime_Type = TimeTicks
_HpicfPim6ComponentBSRExpiryTime_Object = MibTableColumn
hpicfPim6ComponentBSRExpiryTime = _HpicfPim6ComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 4),
    _HpicfPim6ComponentBSRExpiryTime_Type()
)
hpicfPim6ComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRExpiryTime.setStatus("current")


class _HpicfPim6ComponentCRPHoldTime_Type(Integer32):
    """Custom type hpicfPim6ComponentCRPHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPim6ComponentCRPHoldTime_Type.__name__ = "Integer32"
_HpicfPim6ComponentCRPHoldTime_Object = MibTableColumn
hpicfPim6ComponentCRPHoldTime = _HpicfPim6ComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 5),
    _HpicfPim6ComponentCRPHoldTime_Type()
)
hpicfPim6ComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCRPHoldTime.setUnits("seconds")
_HpicfPim6ComponentStatus_Type = RowStatus
_HpicfPim6ComponentStatus_Object = MibTableColumn
hpicfPim6ComponentStatus = _HpicfPim6ComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 6),
    _HpicfPim6ComponentStatus_Type()
)
hpicfPim6ComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentStatus.setStatus("current")


class _HpicfPim6ComponentCBSRAdmStatus_Type(Integer32):
    """Custom type hpicfPim6ComponentCBSRAdmStatus based on Integer32"""
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


_HpicfPim6ComponentCBSRAdmStatus_Type.__name__ = "Integer32"
_HpicfPim6ComponentCBSRAdmStatus_Object = MibTableColumn
hpicfPim6ComponentCBSRAdmStatus = _HpicfPim6ComponentCBSRAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 7),
    _HpicfPim6ComponentCBSRAdmStatus_Type()
)
hpicfPim6ComponentCBSRAdmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRAdmStatus.setStatus("current")
_HpicfPim6ComponentCBSRAddrType_Type = InetAddressType
_HpicfPim6ComponentCBSRAddrType_Object = MibTableColumn
hpicfPim6ComponentCBSRAddrType = _HpicfPim6ComponentCBSRAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 8),
    _HpicfPim6ComponentCBSRAddrType_Type()
)
hpicfPim6ComponentCBSRAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRAddrType.setStatus("current")
_HpicfPim6ComponentCBSRAddress_Type = InetAddress
_HpicfPim6ComponentCBSRAddress_Object = MibTableColumn
hpicfPim6ComponentCBSRAddress = _HpicfPim6ComponentCBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 9),
    _HpicfPim6ComponentCBSRAddress_Type()
)
hpicfPim6ComponentCBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRAddress.setStatus("current")


class _HpicfPim6ComponentCBSRPriority_Type(Integer32):
    """Custom type hpicfPim6ComponentCBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPim6ComponentCBSRPriority_Type.__name__ = "Integer32"
_HpicfPim6ComponentCBSRPriority_Object = MibTableColumn
hpicfPim6ComponentCBSRPriority = _HpicfPim6ComponentCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 10),
    _HpicfPim6ComponentCBSRPriority_Type()
)
hpicfPim6ComponentCBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRPriority.setStatus("current")


class _HpicfPim6ComponentCBSRHashMskLen_Type(Integer32):
    """Custom type hpicfPim6ComponentCBSRHashMskLen based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpicfPim6ComponentCBSRHashMskLen_Type.__name__ = "Integer32"
_HpicfPim6ComponentCBSRHashMskLen_Object = MibTableColumn
hpicfPim6ComponentCBSRHashMskLen = _HpicfPim6ComponentCBSRHashMskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 11),
    _HpicfPim6ComponentCBSRHashMskLen_Type()
)
hpicfPim6ComponentCBSRHashMskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRHashMskLen.setStatus("current")


class _HpicfPim6ComponentCBSRMsgInt_Type(Integer32):
    """Custom type hpicfPim6ComponentCBSRMsgInt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpicfPim6ComponentCBSRMsgInt_Type.__name__ = "Integer32"
_HpicfPim6ComponentCBSRMsgInt_Object = MibTableColumn
hpicfPim6ComponentCBSRMsgInt = _HpicfPim6ComponentCBSRMsgInt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 12),
    _HpicfPim6ComponentCBSRMsgInt_Type()
)
hpicfPim6ComponentCBSRMsgInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRMsgInt.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCBSRMsgInt.setUnits("seconds")


class _HpicfPim6ComponentCRPPriority_Type(Integer32):
    """Custom type hpicfPim6ComponentCRPPriority based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPim6ComponentCRPPriority_Type.__name__ = "Integer32"
_HpicfPim6ComponentCRPPriority_Object = MibTableColumn
hpicfPim6ComponentCRPPriority = _HpicfPim6ComponentCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 13),
    _HpicfPim6ComponentCRPPriority_Type()
)
hpicfPim6ComponentCRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCRPPriority.setStatus("current")
_HpicfPim6ComponentCRPAdvInterval_Type = Unsigned32
_HpicfPim6ComponentCRPAdvInterval_Object = MibTableColumn
hpicfPim6ComponentCRPAdvInterval = _HpicfPim6ComponentCRPAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 14),
    _HpicfPim6ComponentCRPAdvInterval_Type()
)
hpicfPim6ComponentCRPAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCRPAdvInterval.setStatus("current")
_HpicfPim6ComponentBSRPriority_Type = Unsigned32
_HpicfPim6ComponentBSRPriority_Object = MibTableColumn
hpicfPim6ComponentBSRPriority = _HpicfPim6ComponentBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 15),
    _HpicfPim6ComponentBSRPriority_Type()
)
hpicfPim6ComponentBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRPriority.setStatus("current")
_HpicfPim6ComponentBSRHashMskLen_Type = Unsigned32
_HpicfPim6ComponentBSRHashMskLen_Object = MibTableColumn
hpicfPim6ComponentBSRHashMskLen = _HpicfPim6ComponentBSRHashMskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 16),
    _HpicfPim6ComponentBSRHashMskLen_Type()
)
hpicfPim6ComponentBSRHashMskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRHashMskLen.setStatus("current")
_HpicfPim6ComponentBSRUpTime_Type = TimeTicks
_HpicfPim6ComponentBSRUpTime_Object = MibTableColumn
hpicfPim6ComponentBSRUpTime = _HpicfPim6ComponentBSRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 17),
    _HpicfPim6ComponentBSRUpTime_Type()
)
hpicfPim6ComponentBSRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRUpTime.setStatus("current")
_HpicfPim6ComponentBSRNextMessage_Type = TimeTicks
_HpicfPim6ComponentBSRNextMessage_Object = MibTableColumn
hpicfPim6ComponentBSRNextMessage = _HpicfPim6ComponentBSRNextMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 18),
    _HpicfPim6ComponentBSRNextMessage_Type()
)
hpicfPim6ComponentBSRNextMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentBSRNextMessage.setStatus("current")
_HpicfPim6ComponentCRPAdvTimer_Type = TimeTicks
_HpicfPim6ComponentCRPAdvTimer_Object = MibTableColumn
hpicfPim6ComponentCRPAdvTimer = _HpicfPim6ComponentCRPAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 14, 1, 19),
    _HpicfPim6ComponentCRPAdvTimer_Type()
)
hpicfPim6ComponentCRPAdvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6ComponentCRPAdvTimer.setStatus("current")


class _HpicfPim6SPTThreshold_Type(Integer32):
    """Custom type hpicfPim6SPTThreshold based on Integer32"""
    defaultValue = -1


_HpicfPim6SPTThreshold_Object = MibScalar
hpicfPim6SPTThreshold = _HpicfPim6SPTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 15),
    _HpicfPim6SPTThreshold_Type()
)
hpicfPim6SPTThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6SPTThreshold.setStatus("current")
_HpicfPim6NeighborTable_Object = MibTable
hpicfPim6NeighborTable = _HpicfPim6NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hpicfPim6NeighborTable.setStatus("current")
_HpicfPim6NeighborEntry_Object = MibTableRow
hpicfPim6NeighborEntry = _HpicfPim6NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1)
)
hpicfPim6NeighborEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6NeighborIfIndex"),
    (0, "HP-ICF-PIM6", "hpicfPim6NeighborAddressType"),
    (0, "HP-ICF-PIM6", "hpicfPim6NeighborAddress"),
)
if mibBuilder.loadTexts:
    hpicfPim6NeighborEntry.setStatus("current")
_HpicfPim6NeighborIfIndex_Type = InterfaceIndex
_HpicfPim6NeighborIfIndex_Object = MibTableColumn
hpicfPim6NeighborIfIndex = _HpicfPim6NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 1),
    _HpicfPim6NeighborIfIndex_Type()
)
hpicfPim6NeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6NeighborIfIndex.setStatus("current")
_HpicfPim6NeighborAddressType_Type = InetAddressType
_HpicfPim6NeighborAddressType_Object = MibTableColumn
hpicfPim6NeighborAddressType = _HpicfPim6NeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 2),
    _HpicfPim6NeighborAddressType_Type()
)
hpicfPim6NeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6NeighborAddressType.setStatus("current")


class _HpicfPim6NeighborAddress_Type(InetAddress):
    """Custom type hpicfPim6NeighborAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6NeighborAddress_Type.__name__ = "InetAddress"
_HpicfPim6NeighborAddress_Object = MibTableColumn
hpicfPim6NeighborAddress = _HpicfPim6NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 3),
    _HpicfPim6NeighborAddress_Type()
)
hpicfPim6NeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6NeighborAddress.setStatus("current")
_HpicfPim6NeighborGenIDPresent_Type = TruthValue
_HpicfPim6NeighborGenIDPresent_Object = MibTableColumn
hpicfPim6NeighborGenIDPresent = _HpicfPim6NeighborGenIDPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 4),
    _HpicfPim6NeighborGenIDPresent_Type()
)
hpicfPim6NeighborGenIDPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborGenIDPresent.setStatus("current")
_HpicfPim6NeighborGenIDValue_Type = Unsigned32
_HpicfPim6NeighborGenIDValue_Object = MibTableColumn
hpicfPim6NeighborGenIDValue = _HpicfPim6NeighborGenIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 5),
    _HpicfPim6NeighborGenIDValue_Type()
)
hpicfPim6NeighborGenIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborGenIDValue.setStatus("current")
_HpicfPim6NeighborUpTime_Type = TimeTicks
_HpicfPim6NeighborUpTime_Object = MibTableColumn
hpicfPim6NeighborUpTime = _HpicfPim6NeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 6),
    _HpicfPim6NeighborUpTime_Type()
)
hpicfPim6NeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborUpTime.setStatus("current")
_HpicfPim6NeighborExpiryTime_Type = TimeTicks
_HpicfPim6NeighborExpiryTime_Object = MibTableColumn
hpicfPim6NeighborExpiryTime = _HpicfPim6NeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 7),
    _HpicfPim6NeighborExpiryTime_Type()
)
hpicfPim6NeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborExpiryTime.setStatus("current")
_HpicfPim6NeighborDRPrioPresent_Type = TruthValue
_HpicfPim6NeighborDRPrioPresent_Object = MibTableColumn
hpicfPim6NeighborDRPrioPresent = _HpicfPim6NeighborDRPrioPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 8),
    _HpicfPim6NeighborDRPrioPresent_Type()
)
hpicfPim6NeighborDRPrioPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborDRPrioPresent.setStatus("current")
_HpicfPim6NeighborDRPriority_Type = Unsigned32
_HpicfPim6NeighborDRPriority_Object = MibTableColumn
hpicfPim6NeighborDRPriority = _HpicfPim6NeighborDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 9),
    _HpicfPim6NeighborDRPriority_Type()
)
hpicfPim6NeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborDRPriority.setStatus("current")
_HpicfPim6NeighborLanPruneDlyPres_Type = TruthValue
_HpicfPim6NeighborLanPruneDlyPres_Object = MibTableColumn
hpicfPim6NeighborLanPruneDlyPres = _HpicfPim6NeighborLanPruneDlyPres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 16, 1, 10),
    _HpicfPim6NeighborLanPruneDlyPres_Type()
)
hpicfPim6NeighborLanPruneDlyPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6NeighborLanPruneDlyPres.setStatus("current")
_HpicfPim6RPSetTable_Object = MibTable
hpicfPim6RPSetTable = _HpicfPim6RPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hpicfPim6RPSetTable.setStatus("current")
_HpicfPim6RPSetEntry_Object = MibTableRow
hpicfPim6RPSetEntry = _HpicfPim6RPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1)
)
hpicfPim6RPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetGroupAddressType"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetGroupAddress"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetGroupMaskType"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetGroupMask"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetAddressType"),
    (0, "HP-ICF-PIM6", "hpicfPim6RPSetAddress"),
)
if mibBuilder.loadTexts:
    hpicfPim6RPSetEntry.setStatus("current")
_HpicfPim6RPSetGroupAddressType_Type = InetAddressType
_HpicfPim6RPSetGroupAddressType_Object = MibTableColumn
hpicfPim6RPSetGroupAddressType = _HpicfPim6RPSetGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 1),
    _HpicfPim6RPSetGroupAddressType_Type()
)
hpicfPim6RPSetGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetGroupAddressType.setStatus("current")


class _HpicfPim6RPSetGroupAddress_Type(InetAddress):
    """Custom type hpicfPim6RPSetGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6RPSetGroupAddress_Type.__name__ = "InetAddress"
_HpicfPim6RPSetGroupAddress_Object = MibTableColumn
hpicfPim6RPSetGroupAddress = _HpicfPim6RPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 2),
    _HpicfPim6RPSetGroupAddress_Type()
)
hpicfPim6RPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetGroupAddress.setStatus("current")
_HpicfPim6RPSetGroupMaskType_Type = InetAddressType
_HpicfPim6RPSetGroupMaskType_Object = MibTableColumn
hpicfPim6RPSetGroupMaskType = _HpicfPim6RPSetGroupMaskType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 3),
    _HpicfPim6RPSetGroupMaskType_Type()
)
hpicfPim6RPSetGroupMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetGroupMaskType.setStatus("current")


class _HpicfPim6RPSetGroupMask_Type(InetAddress):
    """Custom type hpicfPim6RPSetGroupMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6RPSetGroupMask_Type.__name__ = "InetAddress"
_HpicfPim6RPSetGroupMask_Object = MibTableColumn
hpicfPim6RPSetGroupMask = _HpicfPim6RPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 4),
    _HpicfPim6RPSetGroupMask_Type()
)
hpicfPim6RPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetGroupMask.setStatus("current")
_HpicfPim6RPSetAddressType_Type = InetAddressType
_HpicfPim6RPSetAddressType_Object = MibTableColumn
hpicfPim6RPSetAddressType = _HpicfPim6RPSetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 5),
    _HpicfPim6RPSetAddressType_Type()
)
hpicfPim6RPSetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetAddressType.setStatus("current")


class _HpicfPim6RPSetAddress_Type(InetAddress):
    """Custom type hpicfPim6RPSetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6RPSetAddress_Type.__name__ = "InetAddress"
_HpicfPim6RPSetAddress_Object = MibTableColumn
hpicfPim6RPSetAddress = _HpicfPim6RPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 6),
    _HpicfPim6RPSetAddress_Type()
)
hpicfPim6RPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6RPSetAddress.setStatus("current")


class _HpicfPim6RPSetHoldTime_Type(Integer32):
    """Custom type hpicfPim6RPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPim6RPSetHoldTime_Type.__name__ = "Integer32"
_HpicfPim6RPSetHoldTime_Object = MibTableColumn
hpicfPim6RPSetHoldTime = _HpicfPim6RPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 7),
    _HpicfPim6RPSetHoldTime_Type()
)
hpicfPim6RPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6RPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6RPSetHoldTime.setUnits("seconds")
_HpicfPim6RPSetExpiryTime_Type = TimeTicks
_HpicfPim6RPSetExpiryTime_Object = MibTableColumn
hpicfPim6RPSetExpiryTime = _HpicfPim6RPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 17, 1, 8),
    _HpicfPim6RPSetExpiryTime_Type()
)
hpicfPim6RPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6RPSetExpiryTime.setStatus("current")


class _HpicfPim6IpMcastEnabled_Type(Integer32):
    """Custom type hpicfPim6IpMcastEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfPim6IpMcastEnabled_Type.__name__ = "Integer32"
_HpicfPim6IpMcastEnabled_Object = MibScalar
hpicfPim6IpMcastEnabled = _HpicfPim6IpMcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 18),
    _HpicfPim6IpMcastEnabled_Type()
)
hpicfPim6IpMcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPim6IpMcastEnabled.setStatus("current")
_HpicfPim6IpMcastRouteEntryCount_Type = Counter32
_HpicfPim6IpMcastRouteEntryCount_Object = MibScalar
hpicfPim6IpMcastRouteEntryCount = _HpicfPim6IpMcastRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 19),
    _HpicfPim6IpMcastRouteEntryCount_Type()
)
hpicfPim6IpMcastRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMcastRouteEntryCount.setStatus("current")
_HpicfPim6IpMRouteTable_Object = MibTable
hpicfPim6IpMRouteTable = _HpicfPim6IpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteTable.setStatus("current")
_HpicfPim6IpMRouteEntry_Object = MibTableRow
hpicfPim6IpMRouteEntry = _HpicfPim6IpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1)
)
hpicfPim6IpMRouteEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteGrpAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteGroup"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteGrpPrefixLen"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteSrcAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteSource"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteSrcPrefixLen"),
)
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteEntry.setStatus("current")
_HpicfPim6IpMRouteGrpAddrType_Type = InetAddressType
_HpicfPim6IpMRouteGrpAddrType_Object = MibTableColumn
hpicfPim6IpMRouteGrpAddrType = _HpicfPim6IpMRouteGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 1),
    _HpicfPim6IpMRouteGrpAddrType_Type()
)
hpicfPim6IpMRouteGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteGrpAddrType.setStatus("current")


class _HpicfPim6IpMRouteGroup_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteGroup_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteGroup_Object = MibTableColumn
hpicfPim6IpMRouteGroup = _HpicfPim6IpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 2),
    _HpicfPim6IpMRouteGroup_Type()
)
hpicfPim6IpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteGroup.setStatus("current")
_HpicfPim6IpMRouteGrpPrefixLen_Type = InetAddressPrefixLength
_HpicfPim6IpMRouteGrpPrefixLen_Object = MibTableColumn
hpicfPim6IpMRouteGrpPrefixLen = _HpicfPim6IpMRouteGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 3),
    _HpicfPim6IpMRouteGrpPrefixLen_Type()
)
hpicfPim6IpMRouteGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteGrpPrefixLen.setStatus("current")
_HpicfPim6IpMRouteSrcAddrType_Type = InetAddressType
_HpicfPim6IpMRouteSrcAddrType_Object = MibTableColumn
hpicfPim6IpMRouteSrcAddrType = _HpicfPim6IpMRouteSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 4),
    _HpicfPim6IpMRouteSrcAddrType_Type()
)
hpicfPim6IpMRouteSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteSrcAddrType.setStatus("current")


class _HpicfPim6IpMRouteSource_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteSource_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteSource_Object = MibTableColumn
hpicfPim6IpMRouteSource = _HpicfPim6IpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 5),
    _HpicfPim6IpMRouteSource_Type()
)
hpicfPim6IpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteSource.setStatus("current")
_HpicfPim6IpMRouteSrcPrefixLen_Type = InetAddressPrefixLength
_HpicfPim6IpMRouteSrcPrefixLen_Object = MibTableColumn
hpicfPim6IpMRouteSrcPrefixLen = _HpicfPim6IpMRouteSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 6),
    _HpicfPim6IpMRouteSrcPrefixLen_Type()
)
hpicfPim6IpMRouteSrcPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteSrcPrefixLen.setStatus("current")
_HpicfPim6IpMRouteUpstrNbrType_Type = InetAddressType
_HpicfPim6IpMRouteUpstrNbrType_Object = MibTableColumn
hpicfPim6IpMRouteUpstrNbrType = _HpicfPim6IpMRouteUpstrNbrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 7),
    _HpicfPim6IpMRouteUpstrNbrType_Type()
)
hpicfPim6IpMRouteUpstrNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteUpstrNbrType.setStatus("current")


class _HpicfPim6IpMRouteUpstrNbr_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteUpstrNbr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteUpstrNbr_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteUpstrNbr_Object = MibTableColumn
hpicfPim6IpMRouteUpstrNbr = _HpicfPim6IpMRouteUpstrNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 8),
    _HpicfPim6IpMRouteUpstrNbr_Type()
)
hpicfPim6IpMRouteUpstrNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteUpstrNbr.setStatus("current")
_HpicfPim6IpMRouteInIfIndex_Type = InterfaceIndexOrZero
_HpicfPim6IpMRouteInIfIndex_Object = MibTableColumn
hpicfPim6IpMRouteInIfIndex = _HpicfPim6IpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 9),
    _HpicfPim6IpMRouteInIfIndex_Type()
)
hpicfPim6IpMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteInIfIndex.setStatus("current")
_HpicfPim6IpMRouteTimeStamp_Type = TimeStamp
_HpicfPim6IpMRouteTimeStamp_Object = MibTableColumn
hpicfPim6IpMRouteTimeStamp = _HpicfPim6IpMRouteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 10),
    _HpicfPim6IpMRouteTimeStamp_Type()
)
hpicfPim6IpMRouteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteTimeStamp.setStatus("current")
_HpicfPim6IpMRouteExpiryTime_Type = TimeTicks
_HpicfPim6IpMRouteExpiryTime_Object = MibTableColumn
hpicfPim6IpMRouteExpiryTime = _HpicfPim6IpMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 11),
    _HpicfPim6IpMRouteExpiryTime_Type()
)
hpicfPim6IpMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteExpiryTime.setStatus("current")
_HpicfPim6IpMRouteProtocol_Type = IANAipMRouteProtocol
_HpicfPim6IpMRouteProtocol_Object = MibTableColumn
hpicfPim6IpMRouteProtocol = _HpicfPim6IpMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 12),
    _HpicfPim6IpMRouteProtocol_Type()
)
hpicfPim6IpMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteProtocol.setStatus("current")
_HpicfPim6IpMRouteRtProtocol_Type = IANAipRouteProtocol
_HpicfPim6IpMRouteRtProtocol_Object = MibTableColumn
hpicfPim6IpMRouteRtProtocol = _HpicfPim6IpMRouteRtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 13),
    _HpicfPim6IpMRouteRtProtocol_Type()
)
hpicfPim6IpMRouteRtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteRtProtocol.setStatus("current")
_HpicfPim6IpMRouteRtAddrType_Type = InetAddressType
_HpicfPim6IpMRouteRtAddrType_Object = MibTableColumn
hpicfPim6IpMRouteRtAddrType = _HpicfPim6IpMRouteRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 14),
    _HpicfPim6IpMRouteRtAddrType_Type()
)
hpicfPim6IpMRouteRtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteRtAddrType.setStatus("current")


class _HpicfPim6IpMRouteRtAddress_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteRtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteRtAddress_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteRtAddress_Object = MibTableColumn
hpicfPim6IpMRouteRtAddress = _HpicfPim6IpMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 15),
    _HpicfPim6IpMRouteRtAddress_Type()
)
hpicfPim6IpMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteRtAddress.setStatus("current")
_HpicfPim6IpMRouteRtPrefixLen_Type = InetAddressPrefixLength
_HpicfPim6IpMRouteRtPrefixLen_Object = MibTableColumn
hpicfPim6IpMRouteRtPrefixLen = _HpicfPim6IpMRouteRtPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 16),
    _HpicfPim6IpMRouteRtPrefixLen_Type()
)
hpicfPim6IpMRouteRtPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteRtPrefixLen.setStatus("current")


class _HpicfPim6IpMRouteRtType_Type(Integer32):
    """Custom type hpicfPim6IpMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_HpicfPim6IpMRouteRtType_Type.__name__ = "Integer32"
_HpicfPim6IpMRouteRtType_Object = MibTableColumn
hpicfPim6IpMRouteRtType = _HpicfPim6IpMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 17),
    _HpicfPim6IpMRouteRtType_Type()
)
hpicfPim6IpMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteRtType.setStatus("current")
_HpicfPim6IpMRouteOctets_Type = Counter64
_HpicfPim6IpMRouteOctets_Object = MibTableColumn
hpicfPim6IpMRouteOctets = _HpicfPim6IpMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 18),
    _HpicfPim6IpMRouteOctets_Type()
)
hpicfPim6IpMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteOctets.setStatus("current")
_HpicfPim6IpMRoutePkts_Type = Counter64
_HpicfPim6IpMRoutePkts_Object = MibTableColumn
hpicfPim6IpMRoutePkts = _HpicfPim6IpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 19),
    _HpicfPim6IpMRoutePkts_Type()
)
hpicfPim6IpMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRoutePkts.setStatus("current")
_HpicfPim6IpMRouteTtlDropOct_Type = Counter64
_HpicfPim6IpMRouteTtlDropOct_Object = MibTableColumn
hpicfPim6IpMRouteTtlDropOct = _HpicfPim6IpMRouteTtlDropOct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 20),
    _HpicfPim6IpMRouteTtlDropOct_Type()
)
hpicfPim6IpMRouteTtlDropOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteTtlDropOct.setStatus("current")
_HpicfPim6IpMRouteTtlDropPkts_Type = Counter64
_HpicfPim6IpMRouteTtlDropPkts_Object = MibTableColumn
hpicfPim6IpMRouteTtlDropPkts = _HpicfPim6IpMRouteTtlDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 21),
    _HpicfPim6IpMRouteTtlDropPkts_Type()
)
hpicfPim6IpMRouteTtlDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteTtlDropPkts.setStatus("current")
_HpicfPim6IpMRouteDiffInIfOct_Type = Counter64
_HpicfPim6IpMRouteDiffInIfOct_Object = MibTableColumn
hpicfPim6IpMRouteDiffInIfOct = _HpicfPim6IpMRouteDiffInIfOct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 22),
    _HpicfPim6IpMRouteDiffInIfOct_Type()
)
hpicfPim6IpMRouteDiffInIfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteDiffInIfOct.setStatus("current")
_HpicfPim6IpMRouteDiffInIfPkts_Type = Counter64
_HpicfPim6IpMRouteDiffInIfPkts_Object = MibTableColumn
hpicfPim6IpMRouteDiffInIfPkts = _HpicfPim6IpMRouteDiffInIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 23),
    _HpicfPim6IpMRouteDiffInIfPkts_Type()
)
hpicfPim6IpMRouteDiffInIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteDiffInIfPkts.setStatus("current")
_HpicfPim6IpMRouteBps_Type = Counter64
_HpicfPim6IpMRouteBps_Object = MibTableColumn
hpicfPim6IpMRouteBps = _HpicfPim6IpMRouteBps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 20, 1, 24),
    _HpicfPim6IpMRouteBps_Type()
)
hpicfPim6IpMRouteBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteBps.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteBps.setUnits("bits per second")
_HpicfPim6IpMRouteNHopTable_Object = MibTable
hpicfPim6IpMRouteNHopTable = _HpicfPim6IpMRouteNHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21)
)
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopTable.setStatus("current")
_HpicfPim6IpMRouteNHopEntry_Object = MibTableRow
hpicfPim6IpMRouteNHopEntry = _HpicfPim6IpMRouteNHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1)
)
hpicfPim6IpMRouteNHopEntry.setIndexNames(
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopGrpAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopGroup"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopGrpPLen"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopSrcAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopSource"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopSrcPLen"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopIfIndex"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopAddrType"),
    (0, "HP-ICF-PIM6", "hpicfPim6IpMRouteNHopAddress"),
)
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopEntry.setStatus("current")
_HpicfPim6IpMRouteNHopGrpAddrType_Type = InetAddressType
_HpicfPim6IpMRouteNHopGrpAddrType_Object = MibTableColumn
hpicfPim6IpMRouteNHopGrpAddrType = _HpicfPim6IpMRouteNHopGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 1),
    _HpicfPim6IpMRouteNHopGrpAddrType_Type()
)
hpicfPim6IpMRouteNHopGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopGrpAddrType.setStatus("current")


class _HpicfPim6IpMRouteNHopGroup_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteNHopGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteNHopGroup_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteNHopGroup_Object = MibTableColumn
hpicfPim6IpMRouteNHopGroup = _HpicfPim6IpMRouteNHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 2),
    _HpicfPim6IpMRouteNHopGroup_Type()
)
hpicfPim6IpMRouteNHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopGroup.setStatus("current")
_HpicfPim6IpMRouteNHopGrpPLen_Type = InetAddressPrefixLength
_HpicfPim6IpMRouteNHopGrpPLen_Object = MibTableColumn
hpicfPim6IpMRouteNHopGrpPLen = _HpicfPim6IpMRouteNHopGrpPLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 3),
    _HpicfPim6IpMRouteNHopGrpPLen_Type()
)
hpicfPim6IpMRouteNHopGrpPLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopGrpPLen.setStatus("current")
_HpicfPim6IpMRouteNHopSrcAddrType_Type = InetAddressType
_HpicfPim6IpMRouteNHopSrcAddrType_Object = MibTableColumn
hpicfPim6IpMRouteNHopSrcAddrType = _HpicfPim6IpMRouteNHopSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 4),
    _HpicfPim6IpMRouteNHopSrcAddrType_Type()
)
hpicfPim6IpMRouteNHopSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopSrcAddrType.setStatus("current")


class _HpicfPim6IpMRouteNHopSource_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteNHopSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteNHopSource_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteNHopSource_Object = MibTableColumn
hpicfPim6IpMRouteNHopSource = _HpicfPim6IpMRouteNHopSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 5),
    _HpicfPim6IpMRouteNHopSource_Type()
)
hpicfPim6IpMRouteNHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopSource.setStatus("current")
_HpicfPim6IpMRouteNHopSrcPLen_Type = InetAddressPrefixLength
_HpicfPim6IpMRouteNHopSrcPLen_Object = MibTableColumn
hpicfPim6IpMRouteNHopSrcPLen = _HpicfPim6IpMRouteNHopSrcPLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 6),
    _HpicfPim6IpMRouteNHopSrcPLen_Type()
)
hpicfPim6IpMRouteNHopSrcPLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopSrcPLen.setStatus("current")
_HpicfPim6IpMRouteNHopIfIndex_Type = InterfaceIndex
_HpicfPim6IpMRouteNHopIfIndex_Object = MibTableColumn
hpicfPim6IpMRouteNHopIfIndex = _HpicfPim6IpMRouteNHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 7),
    _HpicfPim6IpMRouteNHopIfIndex_Type()
)
hpicfPim6IpMRouteNHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopIfIndex.setStatus("current")
_HpicfPim6IpMRouteNHopAddrType_Type = InetAddressType
_HpicfPim6IpMRouteNHopAddrType_Object = MibTableColumn
hpicfPim6IpMRouteNHopAddrType = _HpicfPim6IpMRouteNHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 8),
    _HpicfPim6IpMRouteNHopAddrType_Type()
)
hpicfPim6IpMRouteNHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopAddrType.setStatus("current")


class _HpicfPim6IpMRouteNHopAddress_Type(InetAddress):
    """Custom type hpicfPim6IpMRouteNHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfPim6IpMRouteNHopAddress_Type.__name__ = "InetAddress"
_HpicfPim6IpMRouteNHopAddress_Object = MibTableColumn
hpicfPim6IpMRouteNHopAddress = _HpicfPim6IpMRouteNHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 9),
    _HpicfPim6IpMRouteNHopAddress_Type()
)
hpicfPim6IpMRouteNHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopAddress.setStatus("current")


class _HpicfPim6IpMRouteNHopState_Type(Integer32):
    """Custom type hpicfPim6IpMRouteNHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("pruned", 1))
    )


_HpicfPim6IpMRouteNHopState_Type.__name__ = "Integer32"
_HpicfPim6IpMRouteNHopState_Object = MibTableColumn
hpicfPim6IpMRouteNHopState = _HpicfPim6IpMRouteNHopState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 10),
    _HpicfPim6IpMRouteNHopState_Type()
)
hpicfPim6IpMRouteNHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopState.setStatus("current")
_HpicfPim6IpMRouteNHopTStamp_Type = TimeStamp
_HpicfPim6IpMRouteNHopTStamp_Object = MibTableColumn
hpicfPim6IpMRouteNHopTStamp = _HpicfPim6IpMRouteNHopTStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 11),
    _HpicfPim6IpMRouteNHopTStamp_Type()
)
hpicfPim6IpMRouteNHopTStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopTStamp.setStatus("current")
_HpicfPim6IpMRouteNHopExpTime_Type = TimeTicks
_HpicfPim6IpMRouteNHopExpTime_Object = MibTableColumn
hpicfPim6IpMRouteNHopExpTime = _HpicfPim6IpMRouteNHopExpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 12),
    _HpicfPim6IpMRouteNHopExpTime_Type()
)
hpicfPim6IpMRouteNHopExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopExpTime.setStatus("current")


class _HpicfPim6IpMRouteNHopClsMHops_Type(Unsigned32):
    """Custom type hpicfPim6IpMRouteNHopClsMHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HpicfPim6IpMRouteNHopClsMHops_Type.__name__ = "Unsigned32"
_HpicfPim6IpMRouteNHopClsMHops_Object = MibTableColumn
hpicfPim6IpMRouteNHopClsMHops = _HpicfPim6IpMRouteNHopClsMHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 13),
    _HpicfPim6IpMRouteNHopClsMHops_Type()
)
hpicfPim6IpMRouteNHopClsMHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopClsMHops.setStatus("current")
_HpicfPim6IpMRouteNHopProtocol_Type = IANAipMRouteProtocol
_HpicfPim6IpMRouteNHopProtocol_Object = MibTableColumn
hpicfPim6IpMRouteNHopProtocol = _HpicfPim6IpMRouteNHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 14),
    _HpicfPim6IpMRouteNHopProtocol_Type()
)
hpicfPim6IpMRouteNHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopProtocol.setStatus("current")
_HpicfPim6IpMRouteNHopOctets_Type = Counter64
_HpicfPim6IpMRouteNHopOctets_Object = MibTableColumn
hpicfPim6IpMRouteNHopOctets = _HpicfPim6IpMRouteNHopOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 15),
    _HpicfPim6IpMRouteNHopOctets_Type()
)
hpicfPim6IpMRouteNHopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopOctets.setStatus("current")
_HpicfPim6IpMRouteNHopPkts_Type = Counter64
_HpicfPim6IpMRouteNHopPkts_Object = MibTableColumn
hpicfPim6IpMRouteNHopPkts = _HpicfPim6IpMRouteNHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 1, 21, 1, 16),
    _HpicfPim6IpMRouteNHopPkts_Type()
)
hpicfPim6IpMRouteNHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPim6IpMRouteNHopPkts.setStatus("current")
_HpicfPim6Conformance_ObjectIdentity = ObjectIdentity
hpicfPim6Conformance = _HpicfPim6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2)
)
_HpicfPim6Groups_ObjectIdentity = ObjectIdentity
hpicfPim6Groups = _HpicfPim6Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1)
)
_HpicfPim6Compliances_ObjectIdentity = ObjectIdentity
hpicfPim6Compliances = _HpicfPim6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2)
)

# Managed Objects groups

hpicfPim6BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 1)
)
hpicfPim6BaseGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6AdminStatus"),
        ("HP-ICF-PIM6", "hpicfPim6StateRefreshInterval"),
        ("HP-ICF-PIM6", "hpicfPim6TrapControl"),
        ("HP-ICF-PIM6", "hpicfPim6JoinPruneInterval"),
        ("HP-ICF-PIM6", "hpicfPim6RemoveConfig"))
)
if mibBuilder.loadTexts:
    hpicfPim6BaseGroup.setStatus("deprecated")

hpicfPim6DenseIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 2)
)
hpicfPim6DenseIfGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6IfAddressType"),
        ("HP-ICF-PIM6", "hpicfPim6IfAddress"),
        ("HP-ICF-PIM6", "hpicfPim6IfMode"),
        ("HP-ICF-PIM6", "hpicfPim6IfStatus"),
        ("HP-ICF-PIM6", "hpicfPim6IfTrigHelloInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfHelloInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfHelloHoldtime"),
        ("HP-ICF-PIM6", "hpicfPim6IfLanPruneDelay"),
        ("HP-ICF-PIM6", "hpicfPim6IfPropagationDelay"),
        ("HP-ICF-PIM6", "hpicfPim6IfOverrideInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfGenerationID"),
        ("HP-ICF-PIM6", "hpicfPim6IfJoinPruneHoldtime"),
        ("HP-ICF-PIM6", "hpicfPim6IfGraftRetryInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfMaxGraftRetries"),
        ("HP-ICF-PIM6", "hpicfPim6IfSRTTLThreshold"),
        ("HP-ICF-PIM6", "hpicfPim6IfLanDelayEnabled"),
        ("HP-ICF-PIM6", "hpicfPim6IfSRCapable"),
        ("HP-ICF-PIM6", "hpicfPim6IfNBRTimeout"))
)
if mibBuilder.loadTexts:
    hpicfPim6DenseIfGroup.setStatus("current")

hpicfPim6InterfaceExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 3)
)
hpicfPim6InterfaceExtensionsGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6Version"),
        ("HP-ICF-PIM6", "hpicfPim6IfNBRCount"),
        ("HP-ICF-PIM6", "hpicfPim6IfNegotiatedPropagationDelay"),
        ("HP-ICF-PIM6", "hpicfPim6IfNegotiatedOverrideInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfAssertHoldInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfNumRoutersNotUsingLanDelay"))
)
if mibBuilder.loadTexts:
    hpicfPim6InterfaceExtensionsGroup.setStatus("current")

hpicfPim6StaticRpfExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 4)
)
hpicfPim6StaticRpfExtensionsGroup.setObjects(
    ("HP-ICF-PIM6", "hpicfPim6NumStaticRpfEntries")
)
if mibBuilder.loadTexts:
    hpicfPim6StaticRpfExtensionsGroup.setStatus("current")

hpicfPim6GlobalCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 5)
)
hpicfPim6GlobalCounterGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6StarGEntries"),
        ("HP-ICF-PIM6", "hpicfPim6SGEntries"),
        ("HP-ICF-PIM6", "hpicfPim6TotalNeighborCount"))
)
if mibBuilder.loadTexts:
    hpicfPim6GlobalCounterGroup.setStatus("current")

hpicfPim6StaticRPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 7)
)
hpicfPim6StaticRPSetGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6StaticRPSetOverride"),
        ("HP-ICF-PIM6", "hpicfPim6StaticRPSetRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfPim6StaticRPSetGroup.setStatus("current")

hpicfPim6CandidateRPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 8)
)
hpicfPim6CandidateRPGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6CandidateRPAddressType"),
        ("HP-ICF-PIM6", "hpicfPim6CandidateRPAddress"),
        ("HP-ICF-PIM6", "hpicfPim6CandidateRPRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfPim6CandidateRPGroup.setStatus("current")

hpicfPim6ComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 9)
)
hpicfPim6ComponentGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6ComponentBSRAddrType"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRAddress"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRExpiryTime"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCRPHoldTime"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentStatus"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRAdmStatus"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRAddrType"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRAddress"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRPriority"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRHashMskLen"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCBSRMsgInt"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCRPPriority"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCRPAdvInterval"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRPriority"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRHashMskLen"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRUpTime"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentBSRNextMessage"),
        ("HP-ICF-PIM6", "hpicfPim6ComponentCRPAdvTimer"))
)
if mibBuilder.loadTexts:
    hpicfPim6ComponentGroup.setStatus("current")

hpicfPim6CommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 10)
)
hpicfPim6CommonGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6AdminStatus"),
        ("HP-ICF-PIM6", "hpicfPim6StateRefreshInterval"),
        ("HP-ICF-PIM6", "hpicfPim6TrapControl"),
        ("HP-ICF-PIM6", "hpicfPim6JoinPruneInterval"),
        ("HP-ICF-PIM6", "hpicfPim6RemoveConfig"),
        ("HP-ICF-PIM6", "hpicfPim6SPTThreshold"),
        ("HP-ICF-PIM6", "hpicfPim6IpMcastEnabled"),
        ("HP-ICF-PIM6", "hpicfPim6IpMcastRouteEntryCount"))
)
if mibBuilder.loadTexts:
    hpicfPim6CommonGroup.setStatus("current")

hpicfPim6SparseIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 11)
)
hpicfPim6SparseIfGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6IfAddressType"),
        ("HP-ICF-PIM6", "hpicfPim6IfAddress"),
        ("HP-ICF-PIM6", "hpicfPim6IfTrigHelloInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfHelloHoldtime"),
        ("HP-ICF-PIM6", "hpicfPim6IfLanPruneDelay"),
        ("HP-ICF-PIM6", "hpicfPim6IfPropagationDelay"),
        ("HP-ICF-PIM6", "hpicfPim6IfOverrideInterval"),
        ("HP-ICF-PIM6", "hpicfPim6IfGenerationID"),
        ("HP-ICF-PIM6", "hpicfPim6IfJoinPruneHoldtime"),
        ("HP-ICF-PIM6", "hpicfPim6IfLanDelayEnabled"),
        ("HP-ICF-PIM6", "hpicfPim6IfDRPriority"),
        ("HP-ICF-PIM6", "hpicfPim6IfNBRTimeout"),
        ("HP-ICF-PIM6", "hpicfPim6IfDRType"),
        ("HP-ICF-PIM6", "hpicfPim6IfDR"))
)
if mibBuilder.loadTexts:
    hpicfPim6SparseIfGroup.setStatus("current")

hpicfPim6NeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 12)
)
hpicfPim6NeighborGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6NeighborGenIDPresent"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborGenIDValue"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborUpTime"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborExpiryTime"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborDRPrioPresent"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborDRPriority"),
        ("HP-ICF-PIM6", "hpicfPim6NeighborLanPruneDlyPres"))
)
if mibBuilder.loadTexts:
    hpicfPim6NeighborGroup.setStatus("current")

hpicfPim6RPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 13)
)
hpicfPim6RPSetGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6RPSetHoldTime"),
        ("HP-ICF-PIM6", "hpicfPim6RPSetExpiryTime"))
)
if mibBuilder.loadTexts:
    hpicfPim6RPSetGroup.setStatus("current")

hpicfPim6MRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 14)
)
hpicfPim6MRouteGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6IpMRouteUpstrNbrType"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteUpstrNbr"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteInIfIndex"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteTimeStamp"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteExpiryTime"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteProtocol"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteRtProtocol"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteRtAddrType"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteRtAddress"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteRtPrefixLen"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteRtType"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteOctets"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRoutePkts"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteTtlDropOct"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteTtlDropPkts"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteDiffInIfOct"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteDiffInIfPkts"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteBps"))
)
if mibBuilder.loadTexts:
    hpicfPim6MRouteGroup.setStatus("current")

hpicfPim6MRouteNHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 15)
)
hpicfPim6MRouteNHopGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopState"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopTStamp"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopExpTime"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopClsMHops"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopProtocol"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopOctets"),
        ("HP-ICF-PIM6", "hpicfPim6IpMRouteNHopPkts"))
)
if mibBuilder.loadTexts:
    hpicfPim6MRouteNHopGroup.setStatus("current")


# Notification objects

hpicfPim6NeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 0, 1)
)
if mibBuilder.loadTexts:
    hpicfPim6NeighborLoss.setStatus(
        "current"
    )

hpicfPim6HardMRTFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpicfPim6HardMRTFull.setStatus(
        "current"
    )

hpicfPim6SoftMRTFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 1, 0, 3)
)
if mibBuilder.loadTexts:
    hpicfPim6SoftMRTFull.setStatus(
        "current"
    )


# Notifications groups

hpicfPim6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 1, 6)
)
hpicfPim6NotificationGroup.setObjects(
      *(("HP-ICF-PIM6", "hpicfPim6NeighborLoss"),
        ("HP-ICF-PIM6", "hpicfPim6HardMRTFull"),
        ("HP-ICF-PIM6", "hpicfPim6SoftMRTFull"))
)
if mibBuilder.loadTexts:
    hpicfPim6NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfPim6DenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfPim6DenseMIBCompliance.setStatus(
        "deprecated"
    )

hpicfPim6UcastRoutingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfPim6UcastRoutingCompliance.setStatus(
        "current"
    )

hpicfPim6GlobalCountersCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfPim6GlobalCountersCompliance.setStatus(
        "current"
    )

hpicfPim6InterfaceInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfPim6InterfaceInfoCompliance.setStatus(
        "current"
    )

hpicfPim6NotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfPim6NotificationCompliance.setStatus(
        "current"
    )

hpicfPim6SparseModeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfPim6SparseModeMIBCompliance.setStatus(
        "current"
    )

hpicfPim6DenseModeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfPim6DenseModeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-PIM6",
    **{"hpicfPim6MIB": hpicfPim6MIB,
       "hpicfPim6Objects": hpicfPim6Objects,
       "hpicfPim6Traps": hpicfPim6Traps,
       "hpicfPim6NeighborLoss": hpicfPim6NeighborLoss,
       "hpicfPim6HardMRTFull": hpicfPim6HardMRTFull,
       "hpicfPim6SoftMRTFull": hpicfPim6SoftMRTFull,
       "hpicfPim6": hpicfPim6,
       "hpicfPim6AdminStatus": hpicfPim6AdminStatus,
       "hpicfPim6StateRefreshInterval": hpicfPim6StateRefreshInterval,
       "hpicfPim6TrapControl": hpicfPim6TrapControl,
       "hpicfPim6IfTable": hpicfPim6IfTable,
       "hpicfPim6IfEntry": hpicfPim6IfEntry,
       "hpicfPim6IfIndex": hpicfPim6IfIndex,
       "hpicfPim6IfAddressType": hpicfPim6IfAddressType,
       "hpicfPim6IfAddress": hpicfPim6IfAddress,
       "hpicfPim6IfMode": hpicfPim6IfMode,
       "hpicfPim6IfTrigHelloInterval": hpicfPim6IfTrigHelloInterval,
       "hpicfPim6IfHelloHoldtime": hpicfPim6IfHelloHoldtime,
       "hpicfPim6IfLanPruneDelay": hpicfPim6IfLanPruneDelay,
       "hpicfPim6IfPropagationDelay": hpicfPim6IfPropagationDelay,
       "hpicfPim6IfOverrideInterval": hpicfPim6IfOverrideInterval,
       "hpicfPim6IfGenerationID": hpicfPim6IfGenerationID,
       "hpicfPim6IfJoinPruneHoldtime": hpicfPim6IfJoinPruneHoldtime,
       "hpicfPim6IfGraftRetryInterval": hpicfPim6IfGraftRetryInterval,
       "hpicfPim6IfMaxGraftRetries": hpicfPim6IfMaxGraftRetries,
       "hpicfPim6IfSRTTLThreshold": hpicfPim6IfSRTTLThreshold,
       "hpicfPim6IfLanDelayEnabled": hpicfPim6IfLanDelayEnabled,
       "hpicfPim6IfSRCapable": hpicfPim6IfSRCapable,
       "hpicfPim6IfNBRTimeout": hpicfPim6IfNBRTimeout,
       "hpicfPim6IfNBRCount": hpicfPim6IfNBRCount,
       "hpicfPim6IfNegotiatedPropagationDelay": hpicfPim6IfNegotiatedPropagationDelay,
       "hpicfPim6IfNegotiatedOverrideInterval": hpicfPim6IfNegotiatedOverrideInterval,
       "hpicfPim6IfAssertHoldInterval": hpicfPim6IfAssertHoldInterval,
       "hpicfPim6IfNumRoutersNotUsingLanDelay": hpicfPim6IfNumRoutersNotUsingLanDelay,
       "hpicfPim6IfHelloInterval": hpicfPim6IfHelloInterval,
       "hpicfPim6IfStatus": hpicfPim6IfStatus,
       "hpicfPim6IfDRPriority": hpicfPim6IfDRPriority,
       "hpicfPim6IfDRType": hpicfPim6IfDRType,
       "hpicfPim6IfDR": hpicfPim6IfDR,
       "hpicfPim6RemoveConfig": hpicfPim6RemoveConfig,
       "hpicfPim6NumStaticRpfEntries": hpicfPim6NumStaticRpfEntries,
       "hpicfPim6Version": hpicfPim6Version,
       "hpicfPim6StarGEntries": hpicfPim6StarGEntries,
       "hpicfPim6SGEntries": hpicfPim6SGEntries,
       "hpicfPim6TotalNeighborCount": hpicfPim6TotalNeighborCount,
       "hpicfPim6JoinPruneInterval": hpicfPim6JoinPruneInterval,
       "hpicfPim6StaticRPSetTable": hpicfPim6StaticRPSetTable,
       "hpicfPim6StaticRPSetEntry": hpicfPim6StaticRPSetEntry,
       "hpicfPim6StaticRPSetGrpAddrType": hpicfPim6StaticRPSetGrpAddrType,
       "hpicfPim6StaticRPSetGroupAddress": hpicfPim6StaticRPSetGroupAddress,
       "hpicfPim6StaticRPSetGrpMskType": hpicfPim6StaticRPSetGrpMskType,
       "hpicfPim6StaticRPSetGroupMask": hpicfPim6StaticRPSetGroupMask,
       "hpicfPim6StaticRPSetAddressType": hpicfPim6StaticRPSetAddressType,
       "hpicfPim6StaticRPSetAddress": hpicfPim6StaticRPSetAddress,
       "hpicfPim6StaticRPSetOverride": hpicfPim6StaticRPSetOverride,
       "hpicfPim6StaticRPSetRowStatus": hpicfPim6StaticRPSetRowStatus,
       "hpicfPim6CandidateRPTable": hpicfPim6CandidateRPTable,
       "hpicfPim6CandidateRPEntry": hpicfPim6CandidateRPEntry,
       "hpicfPim6CandidateRPGrpAddrType": hpicfPim6CandidateRPGrpAddrType,
       "hpicfPim6CandidateRPGroupAddress": hpicfPim6CandidateRPGroupAddress,
       "hpicfPim6CandidateRPGrpMskType": hpicfPim6CandidateRPGrpMskType,
       "hpicfPim6CandidateRPGroupMask": hpicfPim6CandidateRPGroupMask,
       "hpicfPim6CandidateRPAddressType": hpicfPim6CandidateRPAddressType,
       "hpicfPim6CandidateRPAddress": hpicfPim6CandidateRPAddress,
       "hpicfPim6CandidateRPRowStatus": hpicfPim6CandidateRPRowStatus,
       "hpicfPim6ComponentTable": hpicfPim6ComponentTable,
       "hpicfPim6ComponentEntry": hpicfPim6ComponentEntry,
       "hpicfPim6ComponentIndex": hpicfPim6ComponentIndex,
       "hpicfPim6ComponentBSRAddrType": hpicfPim6ComponentBSRAddrType,
       "hpicfPim6ComponentBSRAddress": hpicfPim6ComponentBSRAddress,
       "hpicfPim6ComponentBSRExpiryTime": hpicfPim6ComponentBSRExpiryTime,
       "hpicfPim6ComponentCRPHoldTime": hpicfPim6ComponentCRPHoldTime,
       "hpicfPim6ComponentStatus": hpicfPim6ComponentStatus,
       "hpicfPim6ComponentCBSRAdmStatus": hpicfPim6ComponentCBSRAdmStatus,
       "hpicfPim6ComponentCBSRAddrType": hpicfPim6ComponentCBSRAddrType,
       "hpicfPim6ComponentCBSRAddress": hpicfPim6ComponentCBSRAddress,
       "hpicfPim6ComponentCBSRPriority": hpicfPim6ComponentCBSRPriority,
       "hpicfPim6ComponentCBSRHashMskLen": hpicfPim6ComponentCBSRHashMskLen,
       "hpicfPim6ComponentCBSRMsgInt": hpicfPim6ComponentCBSRMsgInt,
       "hpicfPim6ComponentCRPPriority": hpicfPim6ComponentCRPPriority,
       "hpicfPim6ComponentCRPAdvInterval": hpicfPim6ComponentCRPAdvInterval,
       "hpicfPim6ComponentBSRPriority": hpicfPim6ComponentBSRPriority,
       "hpicfPim6ComponentBSRHashMskLen": hpicfPim6ComponentBSRHashMskLen,
       "hpicfPim6ComponentBSRUpTime": hpicfPim6ComponentBSRUpTime,
       "hpicfPim6ComponentBSRNextMessage": hpicfPim6ComponentBSRNextMessage,
       "hpicfPim6ComponentCRPAdvTimer": hpicfPim6ComponentCRPAdvTimer,
       "hpicfPim6SPTThreshold": hpicfPim6SPTThreshold,
       "hpicfPim6NeighborTable": hpicfPim6NeighborTable,
       "hpicfPim6NeighborEntry": hpicfPim6NeighborEntry,
       "hpicfPim6NeighborIfIndex": hpicfPim6NeighborIfIndex,
       "hpicfPim6NeighborAddressType": hpicfPim6NeighborAddressType,
       "hpicfPim6NeighborAddress": hpicfPim6NeighborAddress,
       "hpicfPim6NeighborGenIDPresent": hpicfPim6NeighborGenIDPresent,
       "hpicfPim6NeighborGenIDValue": hpicfPim6NeighborGenIDValue,
       "hpicfPim6NeighborUpTime": hpicfPim6NeighborUpTime,
       "hpicfPim6NeighborExpiryTime": hpicfPim6NeighborExpiryTime,
       "hpicfPim6NeighborDRPrioPresent": hpicfPim6NeighborDRPrioPresent,
       "hpicfPim6NeighborDRPriority": hpicfPim6NeighborDRPriority,
       "hpicfPim6NeighborLanPruneDlyPres": hpicfPim6NeighborLanPruneDlyPres,
       "hpicfPim6RPSetTable": hpicfPim6RPSetTable,
       "hpicfPim6RPSetEntry": hpicfPim6RPSetEntry,
       "hpicfPim6RPSetGroupAddressType": hpicfPim6RPSetGroupAddressType,
       "hpicfPim6RPSetGroupAddress": hpicfPim6RPSetGroupAddress,
       "hpicfPim6RPSetGroupMaskType": hpicfPim6RPSetGroupMaskType,
       "hpicfPim6RPSetGroupMask": hpicfPim6RPSetGroupMask,
       "hpicfPim6RPSetAddressType": hpicfPim6RPSetAddressType,
       "hpicfPim6RPSetAddress": hpicfPim6RPSetAddress,
       "hpicfPim6RPSetHoldTime": hpicfPim6RPSetHoldTime,
       "hpicfPim6RPSetExpiryTime": hpicfPim6RPSetExpiryTime,
       "hpicfPim6IpMcastEnabled": hpicfPim6IpMcastEnabled,
       "hpicfPim6IpMcastRouteEntryCount": hpicfPim6IpMcastRouteEntryCount,
       "hpicfPim6IpMRouteTable": hpicfPim6IpMRouteTable,
       "hpicfPim6IpMRouteEntry": hpicfPim6IpMRouteEntry,
       "hpicfPim6IpMRouteGrpAddrType": hpicfPim6IpMRouteGrpAddrType,
       "hpicfPim6IpMRouteGroup": hpicfPim6IpMRouteGroup,
       "hpicfPim6IpMRouteGrpPrefixLen": hpicfPim6IpMRouteGrpPrefixLen,
       "hpicfPim6IpMRouteSrcAddrType": hpicfPim6IpMRouteSrcAddrType,
       "hpicfPim6IpMRouteSource": hpicfPim6IpMRouteSource,
       "hpicfPim6IpMRouteSrcPrefixLen": hpicfPim6IpMRouteSrcPrefixLen,
       "hpicfPim6IpMRouteUpstrNbrType": hpicfPim6IpMRouteUpstrNbrType,
       "hpicfPim6IpMRouteUpstrNbr": hpicfPim6IpMRouteUpstrNbr,
       "hpicfPim6IpMRouteInIfIndex": hpicfPim6IpMRouteInIfIndex,
       "hpicfPim6IpMRouteTimeStamp": hpicfPim6IpMRouteTimeStamp,
       "hpicfPim6IpMRouteExpiryTime": hpicfPim6IpMRouteExpiryTime,
       "hpicfPim6IpMRouteProtocol": hpicfPim6IpMRouteProtocol,
       "hpicfPim6IpMRouteRtProtocol": hpicfPim6IpMRouteRtProtocol,
       "hpicfPim6IpMRouteRtAddrType": hpicfPim6IpMRouteRtAddrType,
       "hpicfPim6IpMRouteRtAddress": hpicfPim6IpMRouteRtAddress,
       "hpicfPim6IpMRouteRtPrefixLen": hpicfPim6IpMRouteRtPrefixLen,
       "hpicfPim6IpMRouteRtType": hpicfPim6IpMRouteRtType,
       "hpicfPim6IpMRouteOctets": hpicfPim6IpMRouteOctets,
       "hpicfPim6IpMRoutePkts": hpicfPim6IpMRoutePkts,
       "hpicfPim6IpMRouteTtlDropOct": hpicfPim6IpMRouteTtlDropOct,
       "hpicfPim6IpMRouteTtlDropPkts": hpicfPim6IpMRouteTtlDropPkts,
       "hpicfPim6IpMRouteDiffInIfOct": hpicfPim6IpMRouteDiffInIfOct,
       "hpicfPim6IpMRouteDiffInIfPkts": hpicfPim6IpMRouteDiffInIfPkts,
       "hpicfPim6IpMRouteBps": hpicfPim6IpMRouteBps,
       "hpicfPim6IpMRouteNHopTable": hpicfPim6IpMRouteNHopTable,
       "hpicfPim6IpMRouteNHopEntry": hpicfPim6IpMRouteNHopEntry,
       "hpicfPim6IpMRouteNHopGrpAddrType": hpicfPim6IpMRouteNHopGrpAddrType,
       "hpicfPim6IpMRouteNHopGroup": hpicfPim6IpMRouteNHopGroup,
       "hpicfPim6IpMRouteNHopGrpPLen": hpicfPim6IpMRouteNHopGrpPLen,
       "hpicfPim6IpMRouteNHopSrcAddrType": hpicfPim6IpMRouteNHopSrcAddrType,
       "hpicfPim6IpMRouteNHopSource": hpicfPim6IpMRouteNHopSource,
       "hpicfPim6IpMRouteNHopSrcPLen": hpicfPim6IpMRouteNHopSrcPLen,
       "hpicfPim6IpMRouteNHopIfIndex": hpicfPim6IpMRouteNHopIfIndex,
       "hpicfPim6IpMRouteNHopAddrType": hpicfPim6IpMRouteNHopAddrType,
       "hpicfPim6IpMRouteNHopAddress": hpicfPim6IpMRouteNHopAddress,
       "hpicfPim6IpMRouteNHopState": hpicfPim6IpMRouteNHopState,
       "hpicfPim6IpMRouteNHopTStamp": hpicfPim6IpMRouteNHopTStamp,
       "hpicfPim6IpMRouteNHopExpTime": hpicfPim6IpMRouteNHopExpTime,
       "hpicfPim6IpMRouteNHopClsMHops": hpicfPim6IpMRouteNHopClsMHops,
       "hpicfPim6IpMRouteNHopProtocol": hpicfPim6IpMRouteNHopProtocol,
       "hpicfPim6IpMRouteNHopOctets": hpicfPim6IpMRouteNHopOctets,
       "hpicfPim6IpMRouteNHopPkts": hpicfPim6IpMRouteNHopPkts,
       "hpicfPim6Conformance": hpicfPim6Conformance,
       "hpicfPim6Groups": hpicfPim6Groups,
       "hpicfPim6BaseGroup": hpicfPim6BaseGroup,
       "hpicfPim6DenseIfGroup": hpicfPim6DenseIfGroup,
       "hpicfPim6InterfaceExtensionsGroup": hpicfPim6InterfaceExtensionsGroup,
       "hpicfPim6StaticRpfExtensionsGroup": hpicfPim6StaticRpfExtensionsGroup,
       "hpicfPim6GlobalCounterGroup": hpicfPim6GlobalCounterGroup,
       "hpicfPim6NotificationGroup": hpicfPim6NotificationGroup,
       "hpicfPim6StaticRPSetGroup": hpicfPim6StaticRPSetGroup,
       "hpicfPim6CandidateRPGroup": hpicfPim6CandidateRPGroup,
       "hpicfPim6ComponentGroup": hpicfPim6ComponentGroup,
       "hpicfPim6CommonGroup": hpicfPim6CommonGroup,
       "hpicfPim6SparseIfGroup": hpicfPim6SparseIfGroup,
       "hpicfPim6NeighborGroup": hpicfPim6NeighborGroup,
       "hpicfPim6RPSetGroup": hpicfPim6RPSetGroup,
       "hpicfPim6MRouteGroup": hpicfPim6MRouteGroup,
       "hpicfPim6MRouteNHopGroup": hpicfPim6MRouteNHopGroup,
       "hpicfPim6Compliances": hpicfPim6Compliances,
       "hpicfPim6DenseMIBCompliance": hpicfPim6DenseMIBCompliance,
       "hpicfPim6UcastRoutingCompliance": hpicfPim6UcastRoutingCompliance,
       "hpicfPim6GlobalCountersCompliance": hpicfPim6GlobalCountersCompliance,
       "hpicfPim6InterfaceInfoCompliance": hpicfPim6InterfaceInfoCompliance,
       "hpicfPim6NotificationCompliance": hpicfPim6NotificationCompliance,
       "hpicfPim6SparseModeMIBCompliance": hpicfPim6SparseModeMIBCompliance,
       "hpicfPim6DenseModeMIBCompliance": hpicfPim6DenseModeMIBCompliance}
)
