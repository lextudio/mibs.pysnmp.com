# SNMP MIB module (ALCATEL-IND1-RIPNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-RIPNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:56 2024
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

(routingIND1Ripng,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ripng")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1RIPNGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1)
)
alcatelIND1RIPNGMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RIPNGMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBObjects = _AlcatelIND1RIPNGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBObjects.setStatus("current")
_AlaProtocolRipng_ObjectIdentity = ObjectIdentity
alaProtocolRipng = _AlaProtocolRipng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1)
)


class _AlaRipngProtoStatus_Type(Integer32):
    """Custom type alaRipngProtoStatus based on Integer32"""
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


_AlaRipngProtoStatus_Type.__name__ = "Integer32"
_AlaRipngProtoStatus_Object = MibScalar
alaRipngProtoStatus = _AlaRipngProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 1),
    _AlaRipngProtoStatus_Type()
)
alaRipngProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngProtoStatus.setStatus("current")


class _AlaRipngUpdateInterval_Type(Integer32):
    """Custom type alaRipngUpdateInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaRipngUpdateInterval_Type.__name__ = "Integer32"
_AlaRipngUpdateInterval_Object = MibScalar
alaRipngUpdateInterval = _AlaRipngUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 2),
    _AlaRipngUpdateInterval_Type()
)
alaRipngUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngUpdateInterval.setUnits("seconds")


class _AlaRipngInvalidTimer_Type(Integer32):
    """Custom type alaRipngInvalidTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_AlaRipngInvalidTimer_Type.__name__ = "Integer32"
_AlaRipngInvalidTimer_Object = MibScalar
alaRipngInvalidTimer = _AlaRipngInvalidTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 3),
    _AlaRipngInvalidTimer_Type()
)
alaRipngInvalidTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInvalidTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngInvalidTimer.setUnits("seconds")


class _AlaRipngHolddownTimer_Type(Integer32):
    """Custom type alaRipngHolddownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipngHolddownTimer_Type.__name__ = "Integer32"
_AlaRipngHolddownTimer_Object = MibScalar
alaRipngHolddownTimer = _AlaRipngHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 4),
    _AlaRipngHolddownTimer_Type()
)
alaRipngHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngHolddownTimer.setStatus("current")


class _AlaRipngGarbageTimer_Type(Integer32):
    """Custom type alaRipngGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_AlaRipngGarbageTimer_Type.__name__ = "Integer32"
_AlaRipngGarbageTimer_Object = MibScalar
alaRipngGarbageTimer = _AlaRipngGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 5),
    _AlaRipngGarbageTimer_Type()
)
alaRipngGarbageTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngGarbageTimer.setStatus("current")


class _AlaRipngRouteCount_Type(Integer32):
    """Custom type alaRipngRouteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipngRouteCount_Type.__name__ = "Integer32"
_AlaRipngRouteCount_Object = MibScalar
alaRipngRouteCount = _AlaRipngRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 6),
    _AlaRipngRouteCount_Type()
)
alaRipngRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteCount.setStatus("current")


class _AlaRipngGlobalRouteTag_Type(Integer32):
    """Custom type alaRipngGlobalRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaRipngGlobalRouteTag_Type.__name__ = "Integer32"
_AlaRipngGlobalRouteTag_Object = MibScalar
alaRipngGlobalRouteTag = _AlaRipngGlobalRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 7),
    _AlaRipngGlobalRouteTag_Type()
)
alaRipngGlobalRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngGlobalRouteTag.setStatus("current")


class _AlaRipngTriggeredSends_Type(Integer32):
    """Custom type alaRipngTriggeredSends based on Integer32"""
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
        *(("all", 1),
          ("off", 3),
          ("onlyupdated", 2))
    )


_AlaRipngTriggeredSends_Type.__name__ = "Integer32"
_AlaRipngTriggeredSends_Object = MibScalar
alaRipngTriggeredSends = _AlaRipngTriggeredSends_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 8),
    _AlaRipngTriggeredSends_Type()
)
alaRipngTriggeredSends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngTriggeredSends.setStatus("current")


class _AlaRipngJitter_Type(Integer32):
    """Custom type alaRipngJitter based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaRipngJitter_Type.__name__ = "Integer32"
_AlaRipngJitter_Object = MibScalar
alaRipngJitter = _AlaRipngJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 9),
    _AlaRipngJitter_Type()
)
alaRipngJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngJitter.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngJitter.setUnits("seconds")


class _AlaRipngPort_Type(Integer32):
    """Custom type alaRipngPort based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaRipngPort_Type.__name__ = "Integer32"
_AlaRipngPort_Object = MibScalar
alaRipngPort = _AlaRipngPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 10),
    _AlaRipngPort_Type()
)
alaRipngPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngPort.setStatus("current")
_AlaRipngInterfaceTable_Object = MibTable
alaRipngInterfaceTable = _AlaRipngInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaRipngInterfaceTable.setStatus("current")
_AlaRipngInterfaceEntry_Object = MibTableRow
alaRipngInterfaceEntry = _AlaRipngInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1)
)
alaRipngInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceIndex"),
)
if mibBuilder.loadTexts:
    alaRipngInterfaceEntry.setStatus("current")


class _AlaRipngInterfaceStatus_Type(RowStatus):
    """Custom type alaRipngInterfaceStatus based on RowStatus"""


_AlaRipngInterfaceStatus_Object = MibTableColumn
alaRipngInterfaceStatus = _AlaRipngInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 1),
    _AlaRipngInterfaceStatus_Type()
)
alaRipngInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceStatus.setStatus("current")
_AlaRipngInterfaceIndex_Type = Integer32
_AlaRipngInterfaceIndex_Object = MibTableColumn
alaRipngInterfaceIndex = _AlaRipngInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 2),
    _AlaRipngInterfaceIndex_Type()
)
alaRipngInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngInterfaceIndex.setStatus("current")


class _AlaRipngInterfaceMetric_Type(Integer32):
    """Custom type alaRipngInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AlaRipngInterfaceMetric_Type.__name__ = "Integer32"
_AlaRipngInterfaceMetric_Object = MibTableColumn
alaRipngInterfaceMetric = _AlaRipngInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 3),
    _AlaRipngInterfaceMetric_Type()
)
alaRipngInterfaceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceMetric.setStatus("current")


class _AlaRipngInterfaceRecvStatus_Type(Integer32):
    """Custom type alaRipngInterfaceRecvStatus based on Integer32"""
    defaultValue = 1

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


_AlaRipngInterfaceRecvStatus_Type.__name__ = "Integer32"
_AlaRipngInterfaceRecvStatus_Object = MibTableColumn
alaRipngInterfaceRecvStatus = _AlaRipngInterfaceRecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 4),
    _AlaRipngInterfaceRecvStatus_Type()
)
alaRipngInterfaceRecvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceRecvStatus.setStatus("current")


class _AlaRipngInterfaceSendStatus_Type(Integer32):
    """Custom type alaRipngInterfaceSendStatus based on Integer32"""
    defaultValue = 1

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


_AlaRipngInterfaceSendStatus_Type.__name__ = "Integer32"
_AlaRipngInterfaceSendStatus_Object = MibTableColumn
alaRipngInterfaceSendStatus = _AlaRipngInterfaceSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 5),
    _AlaRipngInterfaceSendStatus_Type()
)
alaRipngInterfaceSendStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceSendStatus.setStatus("current")


class _AlaRipngInterfaceHorizon_Type(Integer32):
    """Custom type alaRipngInterfaceHorizon based on Integer32"""
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
        *(("none", 1),
          ("onlysplit", 2),
          ("poison", 3))
    )


_AlaRipngInterfaceHorizon_Type.__name__ = "Integer32"
_AlaRipngInterfaceHorizon_Object = MibTableColumn
alaRipngInterfaceHorizon = _AlaRipngInterfaceHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 6),
    _AlaRipngInterfaceHorizon_Type()
)
alaRipngInterfaceHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceHorizon.setStatus("current")
_AlaRipngInterfacePacketsSent_Type = Integer32
_AlaRipngInterfacePacketsSent_Object = MibTableColumn
alaRipngInterfacePacketsSent = _AlaRipngInterfacePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 7),
    _AlaRipngInterfacePacketsSent_Type()
)
alaRipngInterfacePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfacePacketsSent.setStatus("current")
_AlaRipngInterfacePacketsRcvd_Type = Integer32
_AlaRipngInterfacePacketsRcvd_Object = MibTableColumn
alaRipngInterfacePacketsRcvd = _AlaRipngInterfacePacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 8),
    _AlaRipngInterfacePacketsRcvd_Type()
)
alaRipngInterfacePacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfacePacketsRcvd.setStatus("current")
_AlaRipngInterfaceMTU_Type = Counter32
_AlaRipngInterfaceMTU_Object = MibTableColumn
alaRipngInterfaceMTU = _AlaRipngInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 9),
    _AlaRipngInterfaceMTU_Type()
)
alaRipngInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfaceMTU.setStatus("current")
_AlaRipngInterfaceNextUpdate_Type = TimeTicks
_AlaRipngInterfaceNextUpdate_Object = MibTableColumn
alaRipngInterfaceNextUpdate = _AlaRipngInterfaceNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 10),
    _AlaRipngInterfaceNextUpdate_Type()
)
alaRipngInterfaceNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfaceNextUpdate.setStatus("current")


class _AlaRipngInterfaceJitter_Type(Integer32):
    """Custom type alaRipngInterfaceJitter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaRipngInterfaceJitter_Type.__name__ = "Integer32"
_AlaRipngInterfaceJitter_Object = MibTableColumn
alaRipngInterfaceJitter = _AlaRipngInterfaceJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 11),
    _AlaRipngInterfaceJitter_Type()
)
alaRipngInterfaceJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInterfaceJitter.setStatus("deprecated")
_AlaRipngNexthopFilterTable_Object = MibTable
alaRipngNexthopFilterTable = _AlaRipngNexthopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaRipngNexthopFilterTable.setStatus("deprecated")
_AlaRipngNexthopFilterEntry_Object = MibTableRow
alaRipngNexthopFilterEntry = _AlaRipngNexthopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1)
)
alaRipngNexthopFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterAddress"),
)
if mibBuilder.loadTexts:
    alaRipngNexthopFilterEntry.setStatus("deprecated")


class _AlaRipngNexthopFilterStatus_Type(RowStatus):
    """Custom type alaRipngNexthopFilterStatus based on RowStatus"""


_AlaRipngNexthopFilterStatus_Object = MibTableColumn
alaRipngNexthopFilterStatus = _AlaRipngNexthopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1, 1),
    _AlaRipngNexthopFilterStatus_Type()
)
alaRipngNexthopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngNexthopFilterStatus.setStatus("deprecated")
_AlaRipngNexthopFilterAddress_Type = Ipv6Address
_AlaRipngNexthopFilterAddress_Object = MibTableColumn
alaRipngNexthopFilterAddress = _AlaRipngNexthopFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1, 2),
    _AlaRipngNexthopFilterAddress_Type()
)
alaRipngNexthopFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngNexthopFilterAddress.setStatus("deprecated")
_AlaRipngSummarizationTable_Object = MibTable
alaRipngSummarizationTable = _AlaRipngSummarizationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaRipngSummarizationTable.setStatus("deprecated")
_AlaRipngSummarizationEntry_Object = MibTableRow
alaRipngSummarizationEntry = _AlaRipngSummarizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1)
)
alaRipngSummarizationEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefix"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefixLen"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefix"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefixLen"),
)
if mibBuilder.loadTexts:
    alaRipngSummarizationEntry.setStatus("deprecated")


class _AlaRipngSummarizationStatus_Type(RowStatus):
    """Custom type alaRipngSummarizationStatus based on RowStatus"""


_AlaRipngSummarizationStatus_Object = MibTableColumn
alaRipngSummarizationStatus = _AlaRipngSummarizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 1),
    _AlaRipngSummarizationStatus_Type()
)
alaRipngSummarizationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationStatus.setStatus("deprecated")
_AlaRipngSummarizationSourcePrefix_Type = Ipv6AddressPrefix
_AlaRipngSummarizationSourcePrefix_Object = MibTableColumn
alaRipngSummarizationSourcePrefix = _AlaRipngSummarizationSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 2),
    _AlaRipngSummarizationSourcePrefix_Type()
)
alaRipngSummarizationSourcePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationSourcePrefix.setStatus("deprecated")


class _AlaRipngSummarizationSourcePrefixLen_Type(Integer32):
    """Custom type alaRipngSummarizationSourcePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaRipngSummarizationSourcePrefixLen_Type.__name__ = "Integer32"
_AlaRipngSummarizationSourcePrefixLen_Object = MibTableColumn
alaRipngSummarizationSourcePrefixLen = _AlaRipngSummarizationSourcePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 3),
    _AlaRipngSummarizationSourcePrefixLen_Type()
)
alaRipngSummarizationSourcePrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationSourcePrefixLen.setStatus("deprecated")
_AlaRipngSummarizationPrefix_Type = Ipv6AddressPrefix
_AlaRipngSummarizationPrefix_Object = MibTableColumn
alaRipngSummarizationPrefix = _AlaRipngSummarizationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 4),
    _AlaRipngSummarizationPrefix_Type()
)
alaRipngSummarizationPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationPrefix.setStatus("deprecated")


class _AlaRipngSummarizationPrefixLen_Type(Integer32):
    """Custom type alaRipngSummarizationPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaRipngSummarizationPrefixLen_Type.__name__ = "Integer32"
_AlaRipngSummarizationPrefixLen_Object = MibTableColumn
alaRipngSummarizationPrefixLen = _AlaRipngSummarizationPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 5),
    _AlaRipngSummarizationPrefixLen_Type()
)
alaRipngSummarizationPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationPrefixLen.setStatus("deprecated")


class _AlaRipngSummarizationSubnets_Type(Integer32):
    """Custom type alaRipngSummarizationSubnets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donotinclude", 2),
          ("include", 1))
    )


_AlaRipngSummarizationSubnets_Type.__name__ = "Integer32"
_AlaRipngSummarizationSubnets_Object = MibTableColumn
alaRipngSummarizationSubnets = _AlaRipngSummarizationSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 6),
    _AlaRipngSummarizationSubnets_Type()
)
alaRipngSummarizationSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngSummarizationSubnets.setStatus("deprecated")
_AlaRipngRouteFilterTable_Object = MibTable
alaRipngRouteFilterTable = _AlaRipngRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaRipngRouteFilterTable.setStatus("deprecated")
_AlaRipngRouteFilterEntry_Object = MibTableRow
alaRipngRouteFilterEntry = _AlaRipngRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1)
)
alaRipngRouteFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefix"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefixLen"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterDirection"),
)
if mibBuilder.loadTexts:
    alaRipngRouteFilterEntry.setStatus("deprecated")


class _AlaRipngRouteFilterStatus_Type(RowStatus):
    """Custom type alaRipngRouteFilterStatus based on RowStatus"""


_AlaRipngRouteFilterStatus_Object = MibTableColumn
alaRipngRouteFilterStatus = _AlaRipngRouteFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 1),
    _AlaRipngRouteFilterStatus_Type()
)
alaRipngRouteFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngRouteFilterStatus.setStatus("deprecated")
_AlaRipngRouteFilterPrefix_Type = Ipv6AddressPrefix
_AlaRipngRouteFilterPrefix_Object = MibTableColumn
alaRipngRouteFilterPrefix = _AlaRipngRouteFilterPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 2),
    _AlaRipngRouteFilterPrefix_Type()
)
alaRipngRouteFilterPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngRouteFilterPrefix.setStatus("deprecated")


class _AlaRipngRouteFilterPrefixLen_Type(Integer32):
    """Custom type alaRipngRouteFilterPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaRipngRouteFilterPrefixLen_Type.__name__ = "Integer32"
_AlaRipngRouteFilterPrefixLen_Object = MibTableColumn
alaRipngRouteFilterPrefixLen = _AlaRipngRouteFilterPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 3),
    _AlaRipngRouteFilterPrefixLen_Type()
)
alaRipngRouteFilterPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngRouteFilterPrefixLen.setStatus("deprecated")


class _AlaRipngRouteFilterDirection_Type(Integer32):
    """Custom type alaRipngRouteFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_AlaRipngRouteFilterDirection_Type.__name__ = "Integer32"
_AlaRipngRouteFilterDirection_Object = MibTableColumn
alaRipngRouteFilterDirection = _AlaRipngRouteFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 4),
    _AlaRipngRouteFilterDirection_Type()
)
alaRipngRouteFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngRouteFilterDirection.setStatus("deprecated")


class _AlaRipngRouteFilterSubnets_Type(Integer32):
    """Custom type alaRipngRouteFilterSubnets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donotinclude", 2),
          ("include", 1))
    )


_AlaRipngRouteFilterSubnets_Type.__name__ = "Integer32"
_AlaRipngRouteFilterSubnets_Object = MibTableColumn
alaRipngRouteFilterSubnets = _AlaRipngRouteFilterSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 5),
    _AlaRipngRouteFilterSubnets_Type()
)
alaRipngRouteFilterSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngRouteFilterSubnets.setStatus("deprecated")
_AlaRipngPeerTable_Object = MibTable
alaRipngPeerTable = _AlaRipngPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaRipngPeerTable.setStatus("current")
_AlaRipngPeerEntry_Object = MibTableRow
alaRipngPeerEntry = _AlaRipngPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1)
)
alaRipngPeerEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerAddress"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerIndex"),
)
if mibBuilder.loadTexts:
    alaRipngPeerEntry.setStatus("current")
_AlaRipngPeerAddress_Type = Ipv6Address
_AlaRipngPeerAddress_Object = MibTableColumn
alaRipngPeerAddress = _AlaRipngPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 1),
    _AlaRipngPeerAddress_Type()
)
alaRipngPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngPeerAddress.setStatus("current")
_AlaRipngPeerLastUpdate_Type = TimeTicks
_AlaRipngPeerLastUpdate_Object = MibTableColumn
alaRipngPeerLastUpdate = _AlaRipngPeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 2),
    _AlaRipngPeerLastUpdate_Type()
)
alaRipngPeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerLastUpdate.setStatus("current")
_AlaRipngPeerNumUpdates_Type = Counter32
_AlaRipngPeerNumUpdates_Object = MibTableColumn
alaRipngPeerNumUpdates = _AlaRipngPeerNumUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 3),
    _AlaRipngPeerNumUpdates_Type()
)
alaRipngPeerNumUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerNumUpdates.setStatus("current")
_AlaRipngPeerNumRoutes_Type = Counter32
_AlaRipngPeerNumRoutes_Object = MibTableColumn
alaRipngPeerNumRoutes = _AlaRipngPeerNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 4),
    _AlaRipngPeerNumRoutes_Type()
)
alaRipngPeerNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerNumRoutes.setStatus("current")
_AlaRipngPeerBadPackets_Type = Counter32
_AlaRipngPeerBadPackets_Object = MibTableColumn
alaRipngPeerBadPackets = _AlaRipngPeerBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 5),
    _AlaRipngPeerBadPackets_Type()
)
alaRipngPeerBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerBadPackets.setStatus("current")
_AlaRipngPeerBadRoutes_Type = Counter32
_AlaRipngPeerBadRoutes_Object = MibTableColumn
alaRipngPeerBadRoutes = _AlaRipngPeerBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 6),
    _AlaRipngPeerBadRoutes_Type()
)
alaRipngPeerBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerBadRoutes.setStatus("current")
_AlaRipngPeerIndex_Type = Integer32
_AlaRipngPeerIndex_Object = MibTableColumn
alaRipngPeerIndex = _AlaRipngPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 7),
    _AlaRipngPeerIndex_Type()
)
alaRipngPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngPeerIndex.setStatus("current")
_AlaRipngRouteTable_Object = MibTable
alaRipngRouteTable = _AlaRipngRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaRipngRouteTable.setStatus("current")
_AlaRipngRouteEntry_Object = MibTableRow
alaRipngRouteEntry = _AlaRipngRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1)
)
alaRipngRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRoutePrefix"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRoutePrefixLen"),
    (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaRipngRouteEntry.setStatus("current")
_AlaRipngRoutePrefix_Type = Ipv6AddressPrefix
_AlaRipngRoutePrefix_Object = MibTableColumn
alaRipngRoutePrefix = _AlaRipngRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 1),
    _AlaRipngRoutePrefix_Type()
)
alaRipngRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRoutePrefix.setStatus("current")


class _AlaRipngRoutePrefixLen_Type(Integer32):
    """Custom type alaRipngRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaRipngRoutePrefixLen_Type.__name__ = "Integer32"
_AlaRipngRoutePrefixLen_Object = MibTableColumn
alaRipngRoutePrefixLen = _AlaRipngRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 2),
    _AlaRipngRoutePrefixLen_Type()
)
alaRipngRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRoutePrefixLen.setStatus("current")
_AlaRipngRouteNextHop_Type = Ipv6Address
_AlaRipngRouteNextHop_Object = MibTableColumn
alaRipngRouteNextHop = _AlaRipngRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 3),
    _AlaRipngRouteNextHop_Type()
)
alaRipngRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRouteNextHop.setStatus("current")


class _AlaRipngRouteType_Type(Integer32):
    """Custom type alaRipngRouteType based on Integer32"""
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
        *(("local", 1),
          ("redist", 3),
          ("rip", 2),
          ("unknown", 4))
    )


_AlaRipngRouteType_Type.__name__ = "Integer32"
_AlaRipngRouteType_Object = MibTableColumn
alaRipngRouteType = _AlaRipngRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 4),
    _AlaRipngRouteType_Type()
)
alaRipngRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteType.setStatus("current")
_AlaRipngRouteAge_Type = TimeTicks
_AlaRipngRouteAge_Object = MibTableColumn
alaRipngRouteAge = _AlaRipngRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 5),
    _AlaRipngRouteAge_Type()
)
alaRipngRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteAge.setStatus("current")


class _AlaRipngRouteTag_Type(Integer32):
    """Custom type alaRipngRouteTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipngRouteTag_Type.__name__ = "Integer32"
_AlaRipngRouteTag_Object = MibTableColumn
alaRipngRouteTag = _AlaRipngRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 6),
    _AlaRipngRouteTag_Type()
)
alaRipngRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteTag.setStatus("current")


class _AlaRipngRouteMetric_Type(Integer32):
    """Custom type alaRipngRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipngRouteMetric_Type.__name__ = "Integer32"
_AlaRipngRouteMetric_Object = MibTableColumn
alaRipngRouteMetric = _AlaRipngRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 7),
    _AlaRipngRouteMetric_Type()
)
alaRipngRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteMetric.setStatus("current")
_AlaRipngRouteStatus_Type = RowStatus
_AlaRipngRouteStatus_Object = MibTableColumn
alaRipngRouteStatus = _AlaRipngRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 8),
    _AlaRipngRouteStatus_Type()
)
alaRipngRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteStatus.setStatus("current")


class _AlaRipngRouteFlags_Type(Integer32):
    """Custom type alaRipngRouteFlags based on Integer32"""
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
        *(("active", 1),
          ("garbage", 2),
          ("holddown", 3),
          ("unknown", 4))
    )


_AlaRipngRouteFlags_Type.__name__ = "Integer32"
_AlaRipngRouteFlags_Object = MibTableColumn
alaRipngRouteFlags = _AlaRipngRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 9),
    _AlaRipngRouteFlags_Type()
)
alaRipngRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteFlags.setStatus("current")
_AlaRipngRouteIndex_Type = Integer32
_AlaRipngRouteIndex_Object = MibTableColumn
alaRipngRouteIndex = _AlaRipngRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 10),
    _AlaRipngRouteIndex_Type()
)
alaRipngRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteIndex.setStatus("current")
_AlaRipngDebug_ObjectIdentity = ObjectIdentity
alaRipngDebug = _AlaRipngDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2)
)


class _AlaRipngDebugLevel_Type(Integer32):
    """Custom type alaRipngDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaRipngDebugLevel_Type.__name__ = "Integer32"
_AlaRipngDebugLevel_Object = MibScalar
alaRipngDebugLevel = _AlaRipngDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 1),
    _AlaRipngDebugLevel_Type()
)
alaRipngDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugLevel.setStatus("deprecated")


class _AlaRipngDebugError_Type(Integer32):
    """Custom type alaRipngDebugError based on Integer32"""
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


_AlaRipngDebugError_Type.__name__ = "Integer32"
_AlaRipngDebugError_Object = MibScalar
alaRipngDebugError = _AlaRipngDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 2),
    _AlaRipngDebugError_Type()
)
alaRipngDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugError.setStatus("deprecated")


class _AlaRipngDebugWarn_Type(Integer32):
    """Custom type alaRipngDebugWarn based on Integer32"""
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


_AlaRipngDebugWarn_Type.__name__ = "Integer32"
_AlaRipngDebugWarn_Object = MibScalar
alaRipngDebugWarn = _AlaRipngDebugWarn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 3),
    _AlaRipngDebugWarn_Type()
)
alaRipngDebugWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugWarn.setStatus("deprecated")


class _AlaRipngDebugRecv_Type(Integer32):
    """Custom type alaRipngDebugRecv based on Integer32"""
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


_AlaRipngDebugRecv_Type.__name__ = "Integer32"
_AlaRipngDebugRecv_Object = MibScalar
alaRipngDebugRecv = _AlaRipngDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 4),
    _AlaRipngDebugRecv_Type()
)
alaRipngDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugRecv.setStatus("deprecated")


class _AlaRipngDebugSend_Type(Integer32):
    """Custom type alaRipngDebugSend based on Integer32"""
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


_AlaRipngDebugSend_Type.__name__ = "Integer32"
_AlaRipngDebugSend_Object = MibScalar
alaRipngDebugSend = _AlaRipngDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 5),
    _AlaRipngDebugSend_Type()
)
alaRipngDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugSend.setStatus("deprecated")


class _AlaRipngDebugRdb_Type(Integer32):
    """Custom type alaRipngDebugRdb based on Integer32"""
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


_AlaRipngDebugRdb_Type.__name__ = "Integer32"
_AlaRipngDebugRdb_Object = MibScalar
alaRipngDebugRdb = _AlaRipngDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 6),
    _AlaRipngDebugRdb_Type()
)
alaRipngDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugRdb.setStatus("deprecated")


class _AlaRipngDebugAge_Type(Integer32):
    """Custom type alaRipngDebugAge based on Integer32"""
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


_AlaRipngDebugAge_Type.__name__ = "Integer32"
_AlaRipngDebugAge_Object = MibScalar
alaRipngDebugAge = _AlaRipngDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 7),
    _AlaRipngDebugAge_Type()
)
alaRipngDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugAge.setStatus("deprecated")


class _AlaRipngDebugMip_Type(Integer32):
    """Custom type alaRipngDebugMip based on Integer32"""
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


_AlaRipngDebugMip_Type.__name__ = "Integer32"
_AlaRipngDebugMip_Object = MibScalar
alaRipngDebugMip = _AlaRipngDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 8),
    _AlaRipngDebugMip_Type()
)
alaRipngDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugMip.setStatus("deprecated")


class _AlaRipngDebugInfo_Type(Integer32):
    """Custom type alaRipngDebugInfo based on Integer32"""
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


_AlaRipngDebugInfo_Type.__name__ = "Integer32"
_AlaRipngDebugInfo_Object = MibScalar
alaRipngDebugInfo = _AlaRipngDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 9),
    _AlaRipngDebugInfo_Type()
)
alaRipngDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugInfo.setStatus("deprecated")


class _AlaRipngDebugSetup_Type(Integer32):
    """Custom type alaRipngDebugSetup based on Integer32"""
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


_AlaRipngDebugSetup_Type.__name__ = "Integer32"
_AlaRipngDebugSetup_Object = MibScalar
alaRipngDebugSetup = _AlaRipngDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 10),
    _AlaRipngDebugSetup_Type()
)
alaRipngDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugSetup.setStatus("deprecated")


class _AlaRipngDebugTime_Type(Integer32):
    """Custom type alaRipngDebugTime based on Integer32"""
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


_AlaRipngDebugTime_Type.__name__ = "Integer32"
_AlaRipngDebugTime_Object = MibScalar
alaRipngDebugTime = _AlaRipngDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 11),
    _AlaRipngDebugTime_Type()
)
alaRipngDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugTime.setStatus("deprecated")


class _AlaRipngDebugTm_Type(Integer32):
    """Custom type alaRipngDebugTm based on Integer32"""
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


_AlaRipngDebugTm_Type.__name__ = "Integer32"
_AlaRipngDebugTm_Object = MibScalar
alaRipngDebugTm = _AlaRipngDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 12),
    _AlaRipngDebugTm_Type()
)
alaRipngDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugTm.setStatus("deprecated")


class _AlaRipngDebugRouteFilter_Type(Integer32):
    """Custom type alaRipngDebugRouteFilter based on Integer32"""
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


_AlaRipngDebugRouteFilter_Type.__name__ = "Integer32"
_AlaRipngDebugRouteFilter_Object = MibScalar
alaRipngDebugRouteFilter = _AlaRipngDebugRouteFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 13),
    _AlaRipngDebugRouteFilter_Type()
)
alaRipngDebugRouteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugRouteFilter.setStatus("deprecated")


class _AlaRipngDebugNexthopFilter_Type(Integer32):
    """Custom type alaRipngDebugNexthopFilter based on Integer32"""
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


_AlaRipngDebugNexthopFilter_Type.__name__ = "Integer32"
_AlaRipngDebugNexthopFilter_Object = MibScalar
alaRipngDebugNexthopFilter = _AlaRipngDebugNexthopFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 14),
    _AlaRipngDebugNexthopFilter_Type()
)
alaRipngDebugNexthopFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugNexthopFilter.setStatus("deprecated")


class _AlaRipngDebugSummary_Type(Integer32):
    """Custom type alaRipngDebugSummary based on Integer32"""
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


_AlaRipngDebugSummary_Type.__name__ = "Integer32"
_AlaRipngDebugSummary_Object = MibScalar
alaRipngDebugSummary = _AlaRipngDebugSummary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 15),
    _AlaRipngDebugSummary_Type()
)
alaRipngDebugSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugSummary.setStatus("deprecated")


class _AlaRipngDebugAll_Type(Integer32):
    """Custom type alaRipngDebugAll based on Integer32"""
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


_AlaRipngDebugAll_Type.__name__ = "Integer32"
_AlaRipngDebugAll_Object = MibScalar
alaRipngDebugAll = _AlaRipngDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 16),
    _AlaRipngDebugAll_Type()
)
alaRipngDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngDebugAll.setStatus("deprecated")
_AlcatelIND1RIPNGMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBConformance = _AlcatelIND1RIPNGMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBConformance.setStatus("current")
_AlcatelIND1RIPNGMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBGroups = _AlcatelIND1RIPNGMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBGroups.setStatus("current")
_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBCompliances = _AlcatelIND1RIPNGMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBCompliances.setStatus("current")
_AlcatelIND1RIPNGTraps_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGTraps = _AlcatelIND1RIPNGTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3)
)
_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGTrapsRoot = _AlcatelIND1RIPNGTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0)
)

# Managed Objects groups

alaRipngGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 1)
)
alaRipngGlobalGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngProtoStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngUpdateInterval"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInvalidTimer"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngHolddownTimer"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngGarbageTimer"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteCount"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngGlobalRouteTag"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngTriggeredSends"))
)
if mibBuilder.loadTexts:
    alaRipngGlobalGroup.setStatus("current")

alaRipngDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 2)
)
alaRipngDebugGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugLevel"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugError"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugWarn"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugRecv"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugSend"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugRdb"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugAge"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugMip"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugInfo"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugSetup"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugTime"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugTm"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugAll"))
)
if mibBuilder.loadTexts:
    alaRipngDebugGroup.setStatus("current")

alaRipngInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 3)
)
alaRipngInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceMetric"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceRecvStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceSendStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceHorizon"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfacePacketsSent"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfacePacketsRcvd"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceMTU"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceNextUpdate"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceJitter"))
)
if mibBuilder.loadTexts:
    alaRipngInterfaceGroup.setStatus("current")

alaRipngNexthopFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 4)
)
alaRipngNexthopFilterGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterAddress"))
)
if mibBuilder.loadTexts:
    alaRipngNexthopFilterGroup.setStatus("current")

alaRipngSummarizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 5)
)
alaRipngSummarizationGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefix"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefixLen"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefix"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefixLen"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSubnets"))
)
if mibBuilder.loadTexts:
    alaRipngSummarizationGroup.setStatus("current")

alaRipngRouteFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 6)
)
alaRipngRouteFilterGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefix"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefixLen"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterDirection"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterSubnets"))
)
if mibBuilder.loadTexts:
    alaRipngRouteFilterGroup.setStatus("current")

alaRipngPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 7)
)
alaRipngPeerGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerLastUpdate"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerNumUpdates"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerNumRoutes"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerBadPackets"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerBadRoutes"))
)
if mibBuilder.loadTexts:
    alaRipngPeerGroup.setStatus("current")

alaRipngRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 8)
)
alaRipngRouteGroup.setObjects(
      *(("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteType"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteAge"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteTag"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteMetric"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteStatus"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFlags"),
        ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteIndex"))
)
if mibBuilder.loadTexts:
    alaRipngRouteGroup.setStatus("current")


# Notification objects

ripngRouteMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ripngRouteMaxLimitReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1RIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-RIPNG-MIB",
    **{"alcatelIND1RIPNGMIB": alcatelIND1RIPNGMIB,
       "alcatelIND1RIPNGMIBObjects": alcatelIND1RIPNGMIBObjects,
       "alaProtocolRipng": alaProtocolRipng,
       "alaRipngProtoStatus": alaRipngProtoStatus,
       "alaRipngUpdateInterval": alaRipngUpdateInterval,
       "alaRipngInvalidTimer": alaRipngInvalidTimer,
       "alaRipngHolddownTimer": alaRipngHolddownTimer,
       "alaRipngGarbageTimer": alaRipngGarbageTimer,
       "alaRipngRouteCount": alaRipngRouteCount,
       "alaRipngGlobalRouteTag": alaRipngGlobalRouteTag,
       "alaRipngTriggeredSends": alaRipngTriggeredSends,
       "alaRipngJitter": alaRipngJitter,
       "alaRipngPort": alaRipngPort,
       "alaRipngInterfaceTable": alaRipngInterfaceTable,
       "alaRipngInterfaceEntry": alaRipngInterfaceEntry,
       "alaRipngInterfaceStatus": alaRipngInterfaceStatus,
       "alaRipngInterfaceIndex": alaRipngInterfaceIndex,
       "alaRipngInterfaceMetric": alaRipngInterfaceMetric,
       "alaRipngInterfaceRecvStatus": alaRipngInterfaceRecvStatus,
       "alaRipngInterfaceSendStatus": alaRipngInterfaceSendStatus,
       "alaRipngInterfaceHorizon": alaRipngInterfaceHorizon,
       "alaRipngInterfacePacketsSent": alaRipngInterfacePacketsSent,
       "alaRipngInterfacePacketsRcvd": alaRipngInterfacePacketsRcvd,
       "alaRipngInterfaceMTU": alaRipngInterfaceMTU,
       "alaRipngInterfaceNextUpdate": alaRipngInterfaceNextUpdate,
       "alaRipngInterfaceJitter": alaRipngInterfaceJitter,
       "alaRipngNexthopFilterTable": alaRipngNexthopFilterTable,
       "alaRipngNexthopFilterEntry": alaRipngNexthopFilterEntry,
       "alaRipngNexthopFilterStatus": alaRipngNexthopFilterStatus,
       "alaRipngNexthopFilterAddress": alaRipngNexthopFilterAddress,
       "alaRipngSummarizationTable": alaRipngSummarizationTable,
       "alaRipngSummarizationEntry": alaRipngSummarizationEntry,
       "alaRipngSummarizationStatus": alaRipngSummarizationStatus,
       "alaRipngSummarizationSourcePrefix": alaRipngSummarizationSourcePrefix,
       "alaRipngSummarizationSourcePrefixLen": alaRipngSummarizationSourcePrefixLen,
       "alaRipngSummarizationPrefix": alaRipngSummarizationPrefix,
       "alaRipngSummarizationPrefixLen": alaRipngSummarizationPrefixLen,
       "alaRipngSummarizationSubnets": alaRipngSummarizationSubnets,
       "alaRipngRouteFilterTable": alaRipngRouteFilterTable,
       "alaRipngRouteFilterEntry": alaRipngRouteFilterEntry,
       "alaRipngRouteFilterStatus": alaRipngRouteFilterStatus,
       "alaRipngRouteFilterPrefix": alaRipngRouteFilterPrefix,
       "alaRipngRouteFilterPrefixLen": alaRipngRouteFilterPrefixLen,
       "alaRipngRouteFilterDirection": alaRipngRouteFilterDirection,
       "alaRipngRouteFilterSubnets": alaRipngRouteFilterSubnets,
       "alaRipngPeerTable": alaRipngPeerTable,
       "alaRipngPeerEntry": alaRipngPeerEntry,
       "alaRipngPeerAddress": alaRipngPeerAddress,
       "alaRipngPeerLastUpdate": alaRipngPeerLastUpdate,
       "alaRipngPeerNumUpdates": alaRipngPeerNumUpdates,
       "alaRipngPeerNumRoutes": alaRipngPeerNumRoutes,
       "alaRipngPeerBadPackets": alaRipngPeerBadPackets,
       "alaRipngPeerBadRoutes": alaRipngPeerBadRoutes,
       "alaRipngPeerIndex": alaRipngPeerIndex,
       "alaRipngRouteTable": alaRipngRouteTable,
       "alaRipngRouteEntry": alaRipngRouteEntry,
       "alaRipngRoutePrefix": alaRipngRoutePrefix,
       "alaRipngRoutePrefixLen": alaRipngRoutePrefixLen,
       "alaRipngRouteNextHop": alaRipngRouteNextHop,
       "alaRipngRouteType": alaRipngRouteType,
       "alaRipngRouteAge": alaRipngRouteAge,
       "alaRipngRouteTag": alaRipngRouteTag,
       "alaRipngRouteMetric": alaRipngRouteMetric,
       "alaRipngRouteStatus": alaRipngRouteStatus,
       "alaRipngRouteFlags": alaRipngRouteFlags,
       "alaRipngRouteIndex": alaRipngRouteIndex,
       "alaRipngDebug": alaRipngDebug,
       "alaRipngDebugLevel": alaRipngDebugLevel,
       "alaRipngDebugError": alaRipngDebugError,
       "alaRipngDebugWarn": alaRipngDebugWarn,
       "alaRipngDebugRecv": alaRipngDebugRecv,
       "alaRipngDebugSend": alaRipngDebugSend,
       "alaRipngDebugRdb": alaRipngDebugRdb,
       "alaRipngDebugAge": alaRipngDebugAge,
       "alaRipngDebugMip": alaRipngDebugMip,
       "alaRipngDebugInfo": alaRipngDebugInfo,
       "alaRipngDebugSetup": alaRipngDebugSetup,
       "alaRipngDebugTime": alaRipngDebugTime,
       "alaRipngDebugTm": alaRipngDebugTm,
       "alaRipngDebugRouteFilter": alaRipngDebugRouteFilter,
       "alaRipngDebugNexthopFilter": alaRipngDebugNexthopFilter,
       "alaRipngDebugSummary": alaRipngDebugSummary,
       "alaRipngDebugAll": alaRipngDebugAll,
       "alcatelIND1RIPNGMIBConformance": alcatelIND1RIPNGMIBConformance,
       "alcatelIND1RIPNGMIBGroups": alcatelIND1RIPNGMIBGroups,
       "alaRipngGlobalGroup": alaRipngGlobalGroup,
       "alaRipngDebugGroup": alaRipngDebugGroup,
       "alaRipngInterfaceGroup": alaRipngInterfaceGroup,
       "alaRipngNexthopFilterGroup": alaRipngNexthopFilterGroup,
       "alaRipngSummarizationGroup": alaRipngSummarizationGroup,
       "alaRipngRouteFilterGroup": alaRipngRouteFilterGroup,
       "alaRipngPeerGroup": alaRipngPeerGroup,
       "alaRipngRouteGroup": alaRipngRouteGroup,
       "alcatelIND1RIPNGMIBCompliances": alcatelIND1RIPNGMIBCompliances,
       "alcatelIND1RIPMIBCompliance": alcatelIND1RIPMIBCompliance,
       "alcatelIND1RIPNGTraps": alcatelIND1RIPNGTraps,
       "alcatelIND1RIPNGTrapsRoot": alcatelIND1RIPNGTrapsRoot,
       "ripngRouteMaxLimitReached": ripngRouteMaxLimitReached}
)
