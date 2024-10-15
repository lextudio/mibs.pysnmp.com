# SNMP MIB module (ALCATEL-IND1-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:44 2024
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

(routingIND1Pim,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Pim")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(pimInterfaceEntry,) = mibBuilder.importSymbols(
    "PIM-STD-MIB",
    "pimInterfaceEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1PIMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1)
)
alcatelIND1PIMMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaPimNotifications_ObjectIdentity = ObjectIdentity
alaPimNotifications = _AlaPimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 0)
)
_AlcatelIND1PIMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBObjects = _AlcatelIND1PIMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1)
)
_AlaPimsmGlobalConfig_ObjectIdentity = ObjectIdentity
alaPimsmGlobalConfig = _AlaPimsmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1)
)


class _AlaPimsmAdminStatus_Type(Integer32):
    """Custom type alaPimsmAdminStatus based on Integer32"""
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


_AlaPimsmAdminStatus_Type.__name__ = "Integer32"
_AlaPimsmAdminStatus_Object = MibScalar
alaPimsmAdminStatus = _AlaPimsmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 1),
    _AlaPimsmAdminStatus_Type()
)
alaPimsmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminStatus.setStatus("current")


class _AlaPimsmMaxRPs_Type(Integer32):
    """Custom type alaPimsmMaxRPs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaPimsmMaxRPs_Type.__name__ = "Integer32"
_AlaPimsmMaxRPs_Object = MibScalar
alaPimsmMaxRPs = _AlaPimsmMaxRPs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 2),
    _AlaPimsmMaxRPs_Type()
)
alaPimsmMaxRPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmMaxRPs.setStatus("current")


class _AlaPimsmProbeTime_Type(Integer32):
    """Custom type alaPimsmProbeTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmProbeTime_Type.__name__ = "Integer32"
_AlaPimsmProbeTime_Object = MibScalar
alaPimsmProbeTime = _AlaPimsmProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 3),
    _AlaPimsmProbeTime_Type()
)
alaPimsmProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmProbeTime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimsmProbeTime.setUnits("seconds")


class _AlaPimsmOldRegisterMessageSupport_Type(Integer32):
    """Custom type alaPimsmOldRegisterMessageSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("header", 1))
    )


_AlaPimsmOldRegisterMessageSupport_Type.__name__ = "Integer32"
_AlaPimsmOldRegisterMessageSupport_Object = MibScalar
alaPimsmOldRegisterMessageSupport = _AlaPimsmOldRegisterMessageSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 4),
    _AlaPimsmOldRegisterMessageSupport_Type()
)
alaPimsmOldRegisterMessageSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmOldRegisterMessageSupport.setStatus("current")


class _AlaPimsmAdminSPTConfig_Type(Integer32):
    """Custom type alaPimsmAdminSPTConfig based on Integer32"""
    defaultValue = 1

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


_AlaPimsmAdminSPTConfig_Type.__name__ = "Integer32"
_AlaPimsmAdminSPTConfig_Object = MibScalar
alaPimsmAdminSPTConfig = _AlaPimsmAdminSPTConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 5),
    _AlaPimsmAdminSPTConfig_Type()
)
alaPimsmAdminSPTConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminSPTConfig.setStatus("current")


class _AlaPimsmRPThreshold_Type(Integer32):
    """Custom type alaPimsmRPThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimsmRPThreshold_Type.__name__ = "Integer32"
_AlaPimsmRPThreshold_Object = MibScalar
alaPimsmRPThreshold = _AlaPimsmRPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 6),
    _AlaPimsmRPThreshold_Type()
)
alaPimsmRPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmRPThreshold.setStatus("current")


class _AlaPimsmV6AdminStatus_Type(Integer32):
    """Custom type alaPimsmV6AdminStatus based on Integer32"""
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


_AlaPimsmV6AdminStatus_Type.__name__ = "Integer32"
_AlaPimsmV6AdminStatus_Object = MibScalar
alaPimsmV6AdminStatus = _AlaPimsmV6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 7),
    _AlaPimsmV6AdminStatus_Type()
)
alaPimsmV6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6AdminStatus.setStatus("current")


class _AlaPimsmV6SPTConfig_Type(Integer32):
    """Custom type alaPimsmV6SPTConfig based on Integer32"""
    defaultValue = 1

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


_AlaPimsmV6SPTConfig_Type.__name__ = "Integer32"
_AlaPimsmV6SPTConfig_Object = MibScalar
alaPimsmV6SPTConfig = _AlaPimsmV6SPTConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 8),
    _AlaPimsmV6SPTConfig_Type()
)
alaPimsmV6SPTConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6SPTConfig.setStatus("current")


class _AlaPimsmV6RPSwitchover_Type(Integer32):
    """Custom type alaPimsmV6RPSwitchover based on Integer32"""
    defaultValue = 1

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


_AlaPimsmV6RPSwitchover_Type.__name__ = "Integer32"
_AlaPimsmV6RPSwitchover_Object = MibScalar
alaPimsmV6RPSwitchover = _AlaPimsmV6RPSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 9),
    _AlaPimsmV6RPSwitchover_Type()
)
alaPimsmV6RPSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6RPSwitchover.setStatus("current")


class _AlaPimsmBidirStatus_Type(Integer32):
    """Custom type alaPimsmBidirStatus based on Integer32"""
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


_AlaPimsmBidirStatus_Type.__name__ = "Integer32"
_AlaPimsmBidirStatus_Object = MibScalar
alaPimsmBidirStatus = _AlaPimsmBidirStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 10),
    _AlaPimsmBidirStatus_Type()
)
alaPimsmBidirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmBidirStatus.setStatus("current")


class _AlaPimsmBidirPeriodicInterval_Type(Integer32):
    """Custom type alaPimsmBidirPeriodicInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AlaPimsmBidirPeriodicInterval_Type.__name__ = "Integer32"
_AlaPimsmBidirPeriodicInterval_Object = MibScalar
alaPimsmBidirPeriodicInterval = _AlaPimsmBidirPeriodicInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 11),
    _AlaPimsmBidirPeriodicInterval_Type()
)
alaPimsmBidirPeriodicInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmBidirPeriodicInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimsmBidirPeriodicInterval.setUnits("seconds")


class _AlaPimsmBidirDFAbort_Type(Integer32):
    """Custom type alaPimsmBidirDFAbort based on Integer32"""
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


_AlaPimsmBidirDFAbort_Type.__name__ = "Integer32"
_AlaPimsmBidirDFAbort_Object = MibScalar
alaPimsmBidirDFAbort = _AlaPimsmBidirDFAbort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 12),
    _AlaPimsmBidirDFAbort_Type()
)
alaPimsmBidirDFAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmBidirDFAbort.setStatus("current")


class _AlaPimsmNonBidirHelloPeriod_Type(Unsigned32):
    """Custom type alaPimsmNonBidirHelloPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AlaPimsmNonBidirHelloPeriod_Type.__name__ = "Unsigned32"
_AlaPimsmNonBidirHelloPeriod_Object = MibScalar
alaPimsmNonBidirHelloPeriod = _AlaPimsmNonBidirHelloPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 13),
    _AlaPimsmNonBidirHelloPeriod_Type()
)
alaPimsmNonBidirHelloPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmNonBidirHelloPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimsmNonBidirHelloPeriod.setUnits("seconds")
_AlaPimsmNonBidirHelloMsgsRcvd_Type = Counter32
_AlaPimsmNonBidirHelloMsgsRcvd_Object = MibScalar
alaPimsmNonBidirHelloMsgsRcvd = _AlaPimsmNonBidirHelloMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 14),
    _AlaPimsmNonBidirHelloMsgsRcvd_Type()
)
alaPimsmNonBidirHelloMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmNonBidirHelloMsgsRcvd.setStatus("current")
_AlaPimsmNonBidirHelloAddressType_Type = InetAddressType
_AlaPimsmNonBidirHelloAddressType_Object = MibScalar
alaPimsmNonBidirHelloAddressType = _AlaPimsmNonBidirHelloAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 15),
    _AlaPimsmNonBidirHelloAddressType_Type()
)
alaPimsmNonBidirHelloAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmNonBidirHelloAddressType.setStatus("current")


class _AlaPimsmNonBidirHelloOrigin_Type(InetAddress):
    """Custom type alaPimsmNonBidirHelloOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimsmNonBidirHelloOrigin_Type.__name__ = "InetAddress"
_AlaPimsmNonBidirHelloOrigin_Object = MibScalar
alaPimsmNonBidirHelloOrigin = _AlaPimsmNonBidirHelloOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 16),
    _AlaPimsmNonBidirHelloOrigin_Type()
)
alaPimsmNonBidirHelloOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmNonBidirHelloOrigin.setStatus("current")


class _AlaPimsmV6BidirStatus_Type(Integer32):
    """Custom type alaPimsmV6BidirStatus based on Integer32"""
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


_AlaPimsmV6BidirStatus_Type.__name__ = "Integer32"
_AlaPimsmV6BidirStatus_Object = MibScalar
alaPimsmV6BidirStatus = _AlaPimsmV6BidirStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 1, 17),
    _AlaPimsmV6BidirStatus_Type()
)
alaPimsmV6BidirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmV6BidirStatus.setStatus("current")
_AlaPimdmGlobalConfig_ObjectIdentity = ObjectIdentity
alaPimdmGlobalConfig = _AlaPimdmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2)
)


class _AlaPimdmAdminStatus_Type(Integer32):
    """Custom type alaPimdmAdminStatus based on Integer32"""
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


_AlaPimdmAdminStatus_Type.__name__ = "Integer32"
_AlaPimdmAdminStatus_Object = MibScalar
alaPimdmAdminStatus = _AlaPimdmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 1),
    _AlaPimdmAdminStatus_Type()
)
alaPimdmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmAdminStatus.setStatus("current")


class _AlaPimdmStateRefreshTimeToLive_Type(Integer32):
    """Custom type alaPimdmStateRefreshTimeToLive based on Integer32"""
    defaultValue = 16


_AlaPimdmStateRefreshTimeToLive_Object = MibScalar
alaPimdmStateRefreshTimeToLive = _AlaPimdmStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 2),
    _AlaPimdmStateRefreshTimeToLive_Type()
)
alaPimdmStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmStateRefreshTimeToLive.setStatus("current")


class _AlaPimdmStateRefreshLimitInterval_Type(TimeTicks):
    """Custom type alaPimdmStateRefreshLimitInterval based on TimeTicks"""
    defaultValue = 0


_AlaPimdmStateRefreshLimitInterval_Object = MibScalar
alaPimdmStateRefreshLimitInterval = _AlaPimdmStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 3),
    _AlaPimdmStateRefreshLimitInterval_Type()
)
alaPimdmStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmStateRefreshLimitInterval.setStatus("current")


class _AlaPimdmV6AdminStatus_Type(Integer32):
    """Custom type alaPimdmV6AdminStatus based on Integer32"""
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


_AlaPimdmV6AdminStatus_Type.__name__ = "Integer32"
_AlaPimdmV6AdminStatus_Object = MibScalar
alaPimdmV6AdminStatus = _AlaPimdmV6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 4),
    _AlaPimdmV6AdminStatus_Type()
)
alaPimdmV6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmV6AdminStatus.setStatus("current")
_AlaPimdmDenseGroupTable_Object = MibTable
alaPimdmDenseGroupTable = _AlaPimdmDenseGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    alaPimdmDenseGroupTable.setStatus("current")
_AlaPimdmDenseGroupEntry_Object = MibTableRow
alaPimdmDenseGroupEntry = _AlaPimdmDenseGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1)
)
alaPimdmDenseGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupAddressType"),
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupGrpAddress"),
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupGrpPrefixLength"),
)
if mibBuilder.loadTexts:
    alaPimdmDenseGroupEntry.setStatus("current")
_AlaPimdmDenseGroupAddressType_Type = InetAddressType
_AlaPimdmDenseGroupAddressType_Object = MibTableColumn
alaPimdmDenseGroupAddressType = _AlaPimdmDenseGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 1),
    _AlaPimdmDenseGroupAddressType_Type()
)
alaPimdmDenseGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupAddressType.setStatus("current")


class _AlaPimdmDenseGroupGrpAddress_Type(InetAddress):
    """Custom type alaPimdmDenseGroupGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimdmDenseGroupGrpAddress_Type.__name__ = "InetAddress"
_AlaPimdmDenseGroupGrpAddress_Object = MibTableColumn
alaPimdmDenseGroupGrpAddress = _AlaPimdmDenseGroupGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 2),
    _AlaPimdmDenseGroupGrpAddress_Type()
)
alaPimdmDenseGroupGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupGrpAddress.setStatus("current")


class _AlaPimdmDenseGroupGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaPimdmDenseGroupGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaPimdmDenseGroupGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaPimdmDenseGroupGrpPrefixLength_Object = MibTableColumn
alaPimdmDenseGroupGrpPrefixLength = _AlaPimdmDenseGroupGrpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 3),
    _AlaPimdmDenseGroupGrpPrefixLength_Type()
)
alaPimdmDenseGroupGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupGrpPrefixLength.setStatus("current")


class _AlaPimdmDenseGroupOverrideDynamic_Type(TruthValue):
    """Custom type alaPimdmDenseGroupOverrideDynamic based on TruthValue"""


_AlaPimdmDenseGroupOverrideDynamic_Object = MibTableColumn
alaPimdmDenseGroupOverrideDynamic = _AlaPimdmDenseGroupOverrideDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 4),
    _AlaPimdmDenseGroupOverrideDynamic_Type()
)
alaPimdmDenseGroupOverrideDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupOverrideDynamic.setStatus("current")


class _AlaPimdmDenseGroupPrecedence_Type(Unsigned32):
    """Custom type alaPimdmDenseGroupPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimdmDenseGroupPrecedence_Type.__name__ = "Unsigned32"
_AlaPimdmDenseGroupPrecedence_Object = MibTableColumn
alaPimdmDenseGroupPrecedence = _AlaPimdmDenseGroupPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 5),
    _AlaPimdmDenseGroupPrecedence_Type()
)
alaPimdmDenseGroupPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupPrecedence.setStatus("current")
_AlaPimdmDenseGroupRowStatus_Type = RowStatus
_AlaPimdmDenseGroupRowStatus_Object = MibTableColumn
alaPimdmDenseGroupRowStatus = _AlaPimdmDenseGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 2, 5, 1, 6),
    _AlaPimdmDenseGroupRowStatus_Type()
)
alaPimdmDenseGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimdmDenseGroupRowStatus.setStatus("current")
_AlaPimGlobalConfig_ObjectIdentity = ObjectIdentity
alaPimGlobalConfig = _AlaPimGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3)
)


class _AlaPimBfdStatus_Type(Integer32):
    """Custom type alaPimBfdStatus based on Integer32"""
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


_AlaPimBfdStatus_Type.__name__ = "Integer32"
_AlaPimBfdStatus_Object = MibScalar
alaPimBfdStatus = _AlaPimBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 1),
    _AlaPimBfdStatus_Type()
)
alaPimBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBfdStatus.setStatus("current")


class _AlaPimBfdAllInterfaceStatus_Type(Integer32):
    """Custom type alaPimBfdAllInterfaceStatus based on Integer32"""
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


_AlaPimBfdAllInterfaceStatus_Type.__name__ = "Integer32"
_AlaPimBfdAllInterfaceStatus_Object = MibScalar
alaPimBfdAllInterfaceStatus = _AlaPimBfdAllInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 2),
    _AlaPimBfdAllInterfaceStatus_Type()
)
alaPimBfdAllInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBfdAllInterfaceStatus.setStatus("current")


class _AlaPimMoFRRStatus_Type(Integer32):
    """Custom type alaPimMoFRRStatus based on Integer32"""
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


_AlaPimMoFRRStatus_Type.__name__ = "Integer32"
_AlaPimMoFRRStatus_Object = MibScalar
alaPimMoFRRStatus = _AlaPimMoFRRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 3),
    _AlaPimMoFRRStatus_Type()
)
alaPimMoFRRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimMoFRRStatus.setStatus("current")


class _AlaPimMoFRRAllRouteStatus_Type(Integer32):
    """Custom type alaPimMoFRRAllRouteStatus based on Integer32"""
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


_AlaPimMoFRRAllRouteStatus_Type.__name__ = "Integer32"
_AlaPimMoFRRAllRouteStatus_Object = MibScalar
alaPimMoFRRAllRouteStatus = _AlaPimMoFRRAllRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 4),
    _AlaPimMoFRRAllRouteStatus_Type()
)
alaPimMoFRRAllRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimMoFRRAllRouteStatus.setStatus("current")
_AlaPimInterfaceAugTable_Object = MibTable
alaPimInterfaceAugTable = _AlaPimInterfaceAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    alaPimInterfaceAugTable.setStatus("current")
_AlaPimInterfaceAugEntry_Object = MibTableRow
alaPimInterfaceAugEntry = _AlaPimInterfaceAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    alaPimInterfaceAugEntry.setStatus("current")


class _AlaPimInterfaceBfdStatus_Type(Integer32):
    """Custom type alaPimInterfaceBfdStatus based on Integer32"""
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


_AlaPimInterfaceBfdStatus_Type.__name__ = "Integer32"
_AlaPimInterfaceBfdStatus_Object = MibTableColumn
alaPimInterfaceBfdStatus = _AlaPimInterfaceBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 5, 1, 1),
    _AlaPimInterfaceBfdStatus_Type()
)
alaPimInterfaceBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceBfdStatus.setStatus("current")


class _AlaPimMbrAllSourcesStatus_Type(Integer32):
    """Custom type alaPimMbrAllSourcesStatus based on Integer32"""
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


_AlaPimMbrAllSourcesStatus_Type.__name__ = "Integer32"
_AlaPimMbrAllSourcesStatus_Object = MibScalar
alaPimMbrAllSourcesStatus = _AlaPimMbrAllSourcesStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 6),
    _AlaPimMbrAllSourcesStatus_Type()
)
alaPimMbrAllSourcesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimMbrAllSourcesStatus.setStatus("current")


class _AlaPimMbrOperStatus_Type(Integer32):
    """Custom type alaPimMbrOperStatus based on Integer32"""
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


_AlaPimMbrOperStatus_Type.__name__ = "Integer32"
_AlaPimMbrOperStatus_Object = MibScalar
alaPimMbrOperStatus = _AlaPimMbrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 1, 3, 7),
    _AlaPimMbrOperStatus_Type()
)
alaPimMbrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimMbrOperStatus.setStatus("current")
_AlcatelIND1PIMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBConformance = _AlcatelIND1PIMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2)
)
_AlcatelIND1PIMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBCompliances = _AlcatelIND1PIMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1)
)
_AlcatelIND1PIMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBGroups = _AlcatelIND1PIMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2)
)
pimInterfaceEntry.registerAugmentions(
    ("ALCATEL-IND1-PIM-MIB",
     "alaPimInterfaceAugEntry")
)
alaPimInterfaceAugEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())

# Managed Objects groups

alaPimsmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 1)
)
alaPimsmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmMaxRPs"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmProbeTime"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmOldRegisterMessageSupport"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminSPTConfig"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmRPThreshold"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6AdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6SPTConfig"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6RPSwitchover"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirPeriodicInterval"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmBidirDFAbort"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloPeriod"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloMsgsRcvd"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6BidirStatus"))
)
if mibBuilder.loadTexts:
    alaPimsmConfigMIBGroup.setStatus("current")

alaPimdmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 2)
)
alaPimdmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimdmAdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshTimeToLive"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshLimitInterval"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmV6AdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupOverrideDynamic"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupPrecedence"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmDenseGroupRowStatus"))
)
if mibBuilder.loadTexts:
    alaPimdmConfigMIBGroup.setStatus("current")

alaPimConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 3)
)
alaPimConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimBfdStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimBfdAllInterfaceStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimMoFRRStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimMoFRRAllRouteStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimInterfaceBfdStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimMbrAllSourcesStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimMbrOperStatus"))
)
if mibBuilder.loadTexts:
    alaPimConfigMIBGroup.setStatus("current")

alaPimOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 4)
)
alaPimOptionalGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloAddressType"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloOrigin"))
)
if mibBuilder.loadTexts:
    alaPimOptionalGroup.setStatus("current")


# Notification objects

alaPimNonBidirHello = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 0, 1)
)
alaPimNonBidirHello.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloAddressType"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmNonBidirHelloOrigin"))
)
if mibBuilder.loadTexts:
    alaPimNonBidirHello.setStatus(
        "current"
    )


# Notifications groups

alaPimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 2, 5)
)
alaPimNotificationGroup.setObjects(
    ("ALCATEL-IND1-PIM-MIB", "alaPimNonBidirHello")
)
if mibBuilder.loadTexts:
    alaPimNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaPimsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaPimsmCompliance.setStatus(
        "current"
    )

alaPimdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alaPimdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PIM-MIB",
    **{"alcatelIND1PIMMIB": alcatelIND1PIMMIB,
       "alaPimNotifications": alaPimNotifications,
       "alaPimNonBidirHello": alaPimNonBidirHello,
       "alcatelIND1PIMMIBObjects": alcatelIND1PIMMIBObjects,
       "alaPimsmGlobalConfig": alaPimsmGlobalConfig,
       "alaPimsmAdminStatus": alaPimsmAdminStatus,
       "alaPimsmMaxRPs": alaPimsmMaxRPs,
       "alaPimsmProbeTime": alaPimsmProbeTime,
       "alaPimsmOldRegisterMessageSupport": alaPimsmOldRegisterMessageSupport,
       "alaPimsmAdminSPTConfig": alaPimsmAdminSPTConfig,
       "alaPimsmRPThreshold": alaPimsmRPThreshold,
       "alaPimsmV6AdminStatus": alaPimsmV6AdminStatus,
       "alaPimsmV6SPTConfig": alaPimsmV6SPTConfig,
       "alaPimsmV6RPSwitchover": alaPimsmV6RPSwitchover,
       "alaPimsmBidirStatus": alaPimsmBidirStatus,
       "alaPimsmBidirPeriodicInterval": alaPimsmBidirPeriodicInterval,
       "alaPimsmBidirDFAbort": alaPimsmBidirDFAbort,
       "alaPimsmNonBidirHelloPeriod": alaPimsmNonBidirHelloPeriod,
       "alaPimsmNonBidirHelloMsgsRcvd": alaPimsmNonBidirHelloMsgsRcvd,
       "alaPimsmNonBidirHelloAddressType": alaPimsmNonBidirHelloAddressType,
       "alaPimsmNonBidirHelloOrigin": alaPimsmNonBidirHelloOrigin,
       "alaPimsmV6BidirStatus": alaPimsmV6BidirStatus,
       "alaPimdmGlobalConfig": alaPimdmGlobalConfig,
       "alaPimdmAdminStatus": alaPimdmAdminStatus,
       "alaPimdmStateRefreshTimeToLive": alaPimdmStateRefreshTimeToLive,
       "alaPimdmStateRefreshLimitInterval": alaPimdmStateRefreshLimitInterval,
       "alaPimdmV6AdminStatus": alaPimdmV6AdminStatus,
       "alaPimdmDenseGroupTable": alaPimdmDenseGroupTable,
       "alaPimdmDenseGroupEntry": alaPimdmDenseGroupEntry,
       "alaPimdmDenseGroupAddressType": alaPimdmDenseGroupAddressType,
       "alaPimdmDenseGroupGrpAddress": alaPimdmDenseGroupGrpAddress,
       "alaPimdmDenseGroupGrpPrefixLength": alaPimdmDenseGroupGrpPrefixLength,
       "alaPimdmDenseGroupOverrideDynamic": alaPimdmDenseGroupOverrideDynamic,
       "alaPimdmDenseGroupPrecedence": alaPimdmDenseGroupPrecedence,
       "alaPimdmDenseGroupRowStatus": alaPimdmDenseGroupRowStatus,
       "alaPimGlobalConfig": alaPimGlobalConfig,
       "alaPimBfdStatus": alaPimBfdStatus,
       "alaPimBfdAllInterfaceStatus": alaPimBfdAllInterfaceStatus,
       "alaPimMoFRRStatus": alaPimMoFRRStatus,
       "alaPimMoFRRAllRouteStatus": alaPimMoFRRAllRouteStatus,
       "alaPimInterfaceAugTable": alaPimInterfaceAugTable,
       "alaPimInterfaceAugEntry": alaPimInterfaceAugEntry,
       "alaPimInterfaceBfdStatus": alaPimInterfaceBfdStatus,
       "alaPimMbrAllSourcesStatus": alaPimMbrAllSourcesStatus,
       "alaPimMbrOperStatus": alaPimMbrOperStatus,
       "alcatelIND1PIMMIBConformance": alcatelIND1PIMMIBConformance,
       "alcatelIND1PIMMIBCompliances": alcatelIND1PIMMIBCompliances,
       "alaPimsmCompliance": alaPimsmCompliance,
       "alaPimdmCompliance": alaPimdmCompliance,
       "alcatelIND1PIMMIBGroups": alcatelIND1PIMMIBGroups,
       "alaPimsmConfigMIBGroup": alaPimsmConfigMIBGroup,
       "alaPimdmConfigMIBGroup": alaPimdmConfigMIBGroup,
       "alaPimConfigMIBGroup": alaPimConfigMIBGroup,
       "alaPimOptionalGroup": alaPimOptionalGroup,
       "alaPimNotificationGroup": alaPimNotificationGroup}
)
