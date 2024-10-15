# SNMP MIB module (Wellfleet-NHRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NHRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:46 2024
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

(wfNhrpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfNhrpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNhrpNetTable_Object = MibTable
wfNhrpNetTable = _WfNhrpNetTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1)
)
if mibBuilder.loadTexts:
    wfNhrpNetTable.setStatus("mandatory")
_WfNhrpNetEntry_Object = MibTableRow
wfNhrpNetEntry = _WfNhrpNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1)
)
wfNhrpNetEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpLayer2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpLayer3Type"),
)
if mibBuilder.loadTexts:
    wfNhrpNetEntry.setStatus("mandatory")


class _WfNhrpDelete_Type(Integer32):
    """Custom type wfNhrpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNhrpDelete_Type.__name__ = "Integer32"
_WfNhrpDelete_Object = MibTableColumn
wfNhrpDelete = _WfNhrpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 1),
    _WfNhrpDelete_Type()
)
wfNhrpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDelete.setStatus("mandatory")


class _WfNhrpLayer2Type_Type(Integer32):
    """Custom type wfNhrpLayer2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpLayer2Type_Type.__name__ = "Integer32"
_WfNhrpLayer2Type_Object = MibTableColumn
wfNhrpLayer2Type = _WfNhrpLayer2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 2),
    _WfNhrpLayer2Type_Type()
)
wfNhrpLayer2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpLayer2Type.setStatus("mandatory")


class _WfNhrpLayer3Type_Type(Integer32):
    """Custom type wfNhrpLayer3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpLayer3Type_Type.__name__ = "Integer32"
_WfNhrpLayer3Type_Object = MibTableColumn
wfNhrpLayer3Type = _WfNhrpLayer3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 3),
    _WfNhrpLayer3Type_Type()
)
wfNhrpLayer3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpLayer3Type.setStatus("mandatory")


class _WfNhrpNHReqPath_Type(Integer32):
    """Custom type wfNhrpNHReqPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defNHS", 2),
          ("routed", 1))
    )


_WfNhrpNHReqPath_Type.__name__ = "Integer32"
_WfNhrpNHReqPath_Object = MibTableColumn
wfNhrpNHReqPath = _WfNhrpNHReqPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 4),
    _WfNhrpNHReqPath_Type()
)
wfNhrpNHReqPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHReqPath.setStatus("mandatory")


class _WfNhrpClientDisable_Type(Integer32):
    """Custom type wfNhrpClientDisable based on Integer32"""
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


_WfNhrpClientDisable_Type.__name__ = "Integer32"
_WfNhrpClientDisable_Object = MibTableColumn
wfNhrpClientDisable = _WfNhrpClientDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 5),
    _WfNhrpClientDisable_Type()
)
wfNhrpClientDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientDisable.setStatus("mandatory")


class _WfNhrpClientRegInterval_Type(Integer32):
    """Custom type wfNhrpClientRegInterval based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_WfNhrpClientRegInterval_Type.__name__ = "Integer32"
_WfNhrpClientRegInterval_Object = MibTableColumn
wfNhrpClientRegInterval = _WfNhrpClientRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 6),
    _WfNhrpClientRegInterval_Type()
)
wfNhrpClientRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientRegInterval.setStatus("mandatory")


class _WfNhrpClientHoldTime_Type(Integer32):
    """Custom type wfNhrpClientHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_WfNhrpClientHoldTime_Type.__name__ = "Integer32"
_WfNhrpClientHoldTime_Object = MibTableColumn
wfNhrpClientHoldTime = _WfNhrpClientHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 7),
    _WfNhrpClientHoldTime_Type()
)
wfNhrpClientHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientHoldTime.setStatus("mandatory")


class _WfNhrpClientReqTimeout_Type(Integer32):
    """Custom type wfNhrpClientReqTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfNhrpClientReqTimeout_Type.__name__ = "Integer32"
_WfNhrpClientReqTimeout_Object = MibTableColumn
wfNhrpClientReqTimeout = _WfNhrpClientReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 8),
    _WfNhrpClientReqTimeout_Type()
)
wfNhrpClientReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientReqTimeout.setStatus("mandatory")


class _WfNhrpClientReqRetry_Type(Integer32):
    """Custom type wfNhrpClientReqRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfNhrpClientReqRetry_Type.__name__ = "Integer32"
_WfNhrpClientReqRetry_Object = MibTableColumn
wfNhrpClientReqRetry = _WfNhrpClientReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 9),
    _WfNhrpClientReqRetry_Type()
)
wfNhrpClientReqRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientReqRetry.setStatus("mandatory")


class _WfNhrpClientMaxPendRequests_Type(Integer32):
    """Custom type wfNhrpClientMaxPendRequests based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfNhrpClientMaxPendRequests_Type.__name__ = "Integer32"
_WfNhrpClientMaxPendRequests_Object = MibTableColumn
wfNhrpClientMaxPendRequests = _WfNhrpClientMaxPendRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 10),
    _WfNhrpClientMaxPendRequests_Type()
)
wfNhrpClientMaxPendRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpClientMaxPendRequests.setStatus("mandatory")


class _WfNhrpServerDisable_Type(Integer32):
    """Custom type wfNhrpServerDisable based on Integer32"""
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


_WfNhrpServerDisable_Type.__name__ = "Integer32"
_WfNhrpServerDisable_Object = MibTableColumn
wfNhrpServerDisable = _WfNhrpServerDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 11),
    _WfNhrpServerDisable_Type()
)
wfNhrpServerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerDisable.setStatus("mandatory")


class _WfNhrpServerFwdDisable_Type(Integer32):
    """Custom type wfNhrpServerFwdDisable based on Integer32"""
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


_WfNhrpServerFwdDisable_Type.__name__ = "Integer32"
_WfNhrpServerFwdDisable_Object = MibTableColumn
wfNhrpServerFwdDisable = _WfNhrpServerFwdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 12),
    _WfNhrpServerFwdDisable_Type()
)
wfNhrpServerFwdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerFwdDisable.setStatus("mandatory")


class _WfNhrpServerMaxNhEntries_Type(Integer32):
    """Custom type wfNhrpServerMaxNhEntries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfNhrpServerMaxNhEntries_Type.__name__ = "Integer32"
_WfNhrpServerMaxNhEntries_Object = MibTableColumn
wfNhrpServerMaxNhEntries = _WfNhrpServerMaxNhEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 13),
    _WfNhrpServerMaxNhEntries_Type()
)
wfNhrpServerMaxNhEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerMaxNhEntries.setStatus("mandatory")


class _WfNhrpServerMaxPendRequests_Type(Integer32):
    """Custom type wfNhrpServerMaxPendRequests based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfNhrpServerMaxPendRequests_Type.__name__ = "Integer32"
_WfNhrpServerMaxPendRequests_Object = MibTableColumn
wfNhrpServerMaxPendRequests = _WfNhrpServerMaxPendRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 14),
    _WfNhrpServerMaxPendRequests_Type()
)
wfNhrpServerMaxPendRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerMaxPendRequests.setStatus("mandatory")


class _WfNhrpServerUseBgp_Type(Integer32):
    """Custom type wfNhrpServerUseBgp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notuse", 2),
          ("use", 1))
    )


_WfNhrpServerUseBgp_Type.__name__ = "Integer32"
_WfNhrpServerUseBgp_Object = MibTableColumn
wfNhrpServerUseBgp = _WfNhrpServerUseBgp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 15),
    _WfNhrpServerUseBgp_Type()
)
wfNhrpServerUseBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerUseBgp.setStatus("mandatory")


class _WfNhrpServerUseDns_Type(Integer32):
    """Custom type wfNhrpServerUseDns based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notuse", 2),
          ("use", 1))
    )


_WfNhrpServerUseDns_Type.__name__ = "Integer32"
_WfNhrpServerUseDns_Object = MibTableColumn
wfNhrpServerUseDns = _WfNhrpServerUseDns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 16),
    _WfNhrpServerUseDns_Type()
)
wfNhrpServerUseDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerUseDns.setStatus("mandatory")


class _WfNhrpServerDnsProxyPort_Type(Integer32):
    """Custom type wfNhrpServerDnsProxyPort based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32550),
    )


_WfNhrpServerDnsProxyPort_Type.__name__ = "Integer32"
_WfNhrpServerDnsProxyPort_Object = MibTableColumn
wfNhrpServerDnsProxyPort = _WfNhrpServerDnsProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 17),
    _WfNhrpServerDnsProxyPort_Type()
)
wfNhrpServerDnsProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerDnsProxyPort.setStatus("mandatory")


class _WfNhrpServerOverrideNbmaAddr_Type(Integer32):
    """Custom type wfNhrpServerOverrideNbmaAddr based on Integer32"""
    defaultValue = 2

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


_WfNhrpServerOverrideNbmaAddr_Type.__name__ = "Integer32"
_WfNhrpServerOverrideNbmaAddr_Object = MibTableColumn
wfNhrpServerOverrideNbmaAddr = _WfNhrpServerOverrideNbmaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 18),
    _WfNhrpServerOverrideNbmaAddr_Type()
)
wfNhrpServerOverrideNbmaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerOverrideNbmaAddr.setStatus("mandatory")


class _WfNhrpBogusNbmaAddr_Type(DisplayString):
    """Custom type wfNhrpBogusNbmaAddr based on DisplayString"""
    defaultValue = OctetString("NOADDRESS")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WfNhrpBogusNbmaAddr_Type.__name__ = "DisplayString"
_WfNhrpBogusNbmaAddr_Object = MibTableColumn
wfNhrpBogusNbmaAddr = _WfNhrpBogusNbmaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 19),
    _WfNhrpBogusNbmaAddr_Type()
)
wfNhrpBogusNbmaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpBogusNbmaAddr.setStatus("mandatory")


class _WfNhrpNhCacheSize_Type(Integer32):
    """Custom type wfNhrpNhCacheSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_WfNhrpNhCacheSize_Type.__name__ = "Integer32"
_WfNhrpNhCacheSize_Object = MibTableColumn
wfNhrpNhCacheSize = _WfNhrpNhCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 20),
    _WfNhrpNhCacheSize_Type()
)
wfNhrpNhCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNhCacheSize.setStatus("mandatory")


class _WfNhrpQosCacheSize_Type(Integer32):
    """Custom type wfNhrpQosCacheSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_WfNhrpQosCacheSize_Type.__name__ = "Integer32"
_WfNhrpQosCacheSize_Object = MibTableColumn
wfNhrpQosCacheSize = _WfNhrpQosCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 21),
    _WfNhrpQosCacheSize_Type()
)
wfNhrpQosCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpQosCacheSize.setStatus("mandatory")


class _WfNhrpAddrXlateCacheSize_Type(Integer32):
    """Custom type wfNhrpAddrXlateCacheSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_WfNhrpAddrXlateCacheSize_Type.__name__ = "Integer32"
_WfNhrpAddrXlateCacheSize_Object = MibTableColumn
wfNhrpAddrXlateCacheSize = _WfNhrpAddrXlateCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 22),
    _WfNhrpAddrXlateCacheSize_Type()
)
wfNhrpAddrXlateCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpAddrXlateCacheSize.setStatus("mandatory")


class _WfNhrpServerLoadBalance_Type(Integer32):
    """Custom type wfNhrpServerLoadBalance based on Integer32"""
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


_WfNhrpServerLoadBalance_Type.__name__ = "Integer32"
_WfNhrpServerLoadBalance_Object = MibTableColumn
wfNhrpServerLoadBalance = _WfNhrpServerLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 23),
    _WfNhrpServerLoadBalance_Type()
)
wfNhrpServerLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerLoadBalance.setStatus("mandatory")


class _WfNhrpServerNegativeCaching_Type(Integer32):
    """Custom type wfNhrpServerNegativeCaching based on Integer32"""
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


_WfNhrpServerNegativeCaching_Type.__name__ = "Integer32"
_WfNhrpServerNegativeCaching_Object = MibTableColumn
wfNhrpServerNegativeCaching = _WfNhrpServerNegativeCaching_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 24),
    _WfNhrpServerNegativeCaching_Type()
)
wfNhrpServerNegativeCaching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerNegativeCaching.setStatus("mandatory")


class _WfNhrpServerNegativeTTL_Type(Integer32):
    """Custom type wfNhrpServerNegativeTTL based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfNhrpServerNegativeTTL_Type.__name__ = "Integer32"
_WfNhrpServerNegativeTTL_Object = MibTableColumn
wfNhrpServerNegativeTTL = _WfNhrpServerNegativeTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 25),
    _WfNhrpServerNegativeTTL_Type()
)
wfNhrpServerNegativeTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpServerNegativeTTL.setStatus("mandatory")


class _WfNhrpDebugLevel_Type(Integer32):
    """Custom type wfNhrpDebugLevel based on Integer32"""
    defaultValue = 0


_WfNhrpDebugLevel_Object = MibTableColumn
wfNhrpDebugLevel = _WfNhrpDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 26),
    _WfNhrpDebugLevel_Type()
)
wfNhrpDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDebugLevel.setStatus("mandatory")


class _WfNhrpStatReset_Type(Integer32):
    """Custom type wfNhrpStatReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("reset", 2))
    )


_WfNhrpStatReset_Type.__name__ = "Integer32"
_WfNhrpStatReset_Object = MibTableColumn
wfNhrpStatReset = _WfNhrpStatReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 27),
    _WfNhrpStatReset_Type()
)
wfNhrpStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpStatReset.setStatus("mandatory")


class _WfNhrpNhCacheSequence_Type(Integer32):
    """Custom type wfNhrpNhCacheSequence based on Integer32"""
    defaultValue = 0


_WfNhrpNhCacheSequence_Object = MibTableColumn
wfNhrpNhCacheSequence = _WfNhrpNhCacheSequence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 28),
    _WfNhrpNhCacheSequence_Type()
)
wfNhrpNhCacheSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNhCacheSequence.setStatus("mandatory")


class _WfNhrpNhCacheNumEntries_Type(Integer32):
    """Custom type wfNhrpNhCacheNumEntries based on Integer32"""
    defaultValue = 0


_WfNhrpNhCacheNumEntries_Object = MibTableColumn
wfNhrpNhCacheNumEntries = _WfNhrpNhCacheNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 29),
    _WfNhrpNhCacheNumEntries_Type()
)
wfNhrpNhCacheNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNhCacheNumEntries.setStatus("mandatory")


class _WfNhrpQosCacheNumEntries_Type(Integer32):
    """Custom type wfNhrpQosCacheNumEntries based on Integer32"""
    defaultValue = 0


_WfNhrpQosCacheNumEntries_Object = MibTableColumn
wfNhrpQosCacheNumEntries = _WfNhrpQosCacheNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 30),
    _WfNhrpQosCacheNumEntries_Type()
)
wfNhrpQosCacheNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpQosCacheNumEntries.setStatus("mandatory")


class _WfNhrpAddrXlateCacheNumEntries_Type(Integer32):
    """Custom type wfNhrpAddrXlateCacheNumEntries based on Integer32"""
    defaultValue = 0


_WfNhrpAddrXlateCacheNumEntries_Object = MibTableColumn
wfNhrpAddrXlateCacheNumEntries = _WfNhrpAddrXlateCacheNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 1, 1, 31),
    _WfNhrpAddrXlateCacheNumEntries_Type()
)
wfNhrpAddrXlateCacheNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpAddrXlateCacheNumEntries.setStatus("mandatory")
_WfNhrpIfTable_Object = MibTable
wfNhrpIfTable = _WfNhrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2)
)
if mibBuilder.loadTexts:
    wfNhrpIfTable.setStatus("mandatory")
_WfNhrpIfEntry_Object = MibTableRow
wfNhrpIfEntry = _WfNhrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1)
)
wfNhrpIfEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpIfLayer2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpIfLayer3Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpIfCct"),
)
if mibBuilder.loadTexts:
    wfNhrpIfEntry.setStatus("mandatory")


class _WfNhrpIfDelete_Type(Integer32):
    """Custom type wfNhrpIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNhrpIfDelete_Type.__name__ = "Integer32"
_WfNhrpIfDelete_Object = MibTableColumn
wfNhrpIfDelete = _WfNhrpIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 1),
    _WfNhrpIfDelete_Type()
)
wfNhrpIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpIfDelete.setStatus("mandatory")


class _WfNhrpIfDisable_Type(Integer32):
    """Custom type wfNhrpIfDisable based on Integer32"""
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


_WfNhrpIfDisable_Type.__name__ = "Integer32"
_WfNhrpIfDisable_Object = MibTableColumn
wfNhrpIfDisable = _WfNhrpIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 2),
    _WfNhrpIfDisable_Type()
)
wfNhrpIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpIfDisable.setStatus("mandatory")


class _WfNhrpIfVCType_Type(Integer32):
    """Custom type wfNhrpIfVCType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_WfNhrpIfVCType_Type.__name__ = "Integer32"
_WfNhrpIfVCType_Object = MibTableColumn
wfNhrpIfVCType = _WfNhrpIfVCType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 3),
    _WfNhrpIfVCType_Type()
)
wfNhrpIfVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpIfVCType.setStatus("mandatory")


class _WfNhrpIfCct_Type(Integer32):
    """Custom type wfNhrpIfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfNhrpIfCct_Type.__name__ = "Integer32"
_WfNhrpIfCct_Object = MibTableColumn
wfNhrpIfCct = _WfNhrpIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 4),
    _WfNhrpIfCct_Type()
)
wfNhrpIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpIfCct.setStatus("mandatory")


class _WfNhrpIfLayer2Type_Type(Integer32):
    """Custom type wfNhrpIfLayer2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpIfLayer2Type_Type.__name__ = "Integer32"
_WfNhrpIfLayer2Type_Object = MibTableColumn
wfNhrpIfLayer2Type = _WfNhrpIfLayer2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 5),
    _WfNhrpIfLayer2Type_Type()
)
wfNhrpIfLayer2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpIfLayer2Type.setStatus("mandatory")


class _WfNhrpIfLayer3Type_Type(Integer32):
    """Custom type wfNhrpIfLayer3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpIfLayer3Type_Type.__name__ = "Integer32"
_WfNhrpIfLayer3Type_Object = MibTableColumn
wfNhrpIfLayer3Type = _WfNhrpIfLayer3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 6),
    _WfNhrpIfLayer3Type_Type()
)
wfNhrpIfLayer3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpIfLayer3Type.setStatus("mandatory")
_WfNhrpIfPktsXmt_Type = Counter32
_WfNhrpIfPktsXmt_Object = MibTableColumn
wfNhrpIfPktsXmt = _WfNhrpIfPktsXmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 2, 1, 7),
    _WfNhrpIfPktsXmt_Type()
)
wfNhrpIfPktsXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpIfPktsXmt.setStatus("mandatory")
_WfNhrpDefNhsTable_Object = MibTable
wfNhrpDefNhsTable = _WfNhrpDefNhsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3)
)
if mibBuilder.loadTexts:
    wfNhrpDefNhsTable.setStatus("mandatory")
_WfNhrpDefNhsEntry_Object = MibTableRow
wfNhrpDefNhsEntry = _WfNhrpDefNhsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1)
)
wfNhrpDefNhsEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpDefNhsLayer2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpDefNhsLayer3Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpDefNhsIndex"),
)
if mibBuilder.loadTexts:
    wfNhrpDefNhsEntry.setStatus("mandatory")


class _WfNhrpDefNhsDelete_Type(Integer32):
    """Custom type wfNhrpDefNhsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNhrpDefNhsDelete_Type.__name__ = "Integer32"
_WfNhrpDefNhsDelete_Object = MibTableColumn
wfNhrpDefNhsDelete = _WfNhrpDefNhsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 1),
    _WfNhrpDefNhsDelete_Type()
)
wfNhrpDefNhsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsDelete.setStatus("mandatory")


class _WfNhrpDefNhsDisable_Type(Integer32):
    """Custom type wfNhrpDefNhsDisable based on Integer32"""
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


_WfNhrpDefNhsDisable_Type.__name__ = "Integer32"
_WfNhrpDefNhsDisable_Object = MibTableColumn
wfNhrpDefNhsDisable = _WfNhrpDefNhsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 2),
    _WfNhrpDefNhsDisable_Type()
)
wfNhrpDefNhsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsDisable.setStatus("mandatory")


class _WfNhrpDefNhsCct_Type(Integer32):
    """Custom type wfNhrpDefNhsCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfNhrpDefNhsCct_Type.__name__ = "Integer32"
_WfNhrpDefNhsCct_Object = MibTableColumn
wfNhrpDefNhsCct = _WfNhrpDefNhsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 3),
    _WfNhrpDefNhsCct_Type()
)
wfNhrpDefNhsCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsCct.setStatus("mandatory")
_WfNhrpDefNhsVcid1_Type = Integer32
_WfNhrpDefNhsVcid1_Object = MibTableColumn
wfNhrpDefNhsVcid1 = _WfNhrpDefNhsVcid1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 4),
    _WfNhrpDefNhsVcid1_Type()
)
wfNhrpDefNhsVcid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsVcid1.setStatus("mandatory")
_WfNhrpDefNhsVcid2_Type = Integer32
_WfNhrpDefNhsVcid2_Object = MibTableColumn
wfNhrpDefNhsVcid2 = _WfNhrpDefNhsVcid2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 5),
    _WfNhrpDefNhsVcid2_Type()
)
wfNhrpDefNhsVcid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsVcid2.setStatus("mandatory")
_WfNhrpDefNhsProtoAddr_Type = IpAddress
_WfNhrpDefNhsProtoAddr_Object = MibTableColumn
wfNhrpDefNhsProtoAddr = _WfNhrpDefNhsProtoAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 6),
    _WfNhrpDefNhsProtoAddr_Type()
)
wfNhrpDefNhsProtoAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsProtoAddr.setStatus("mandatory")
_WfNhrpDefNhsServingNetworkAddr_Type = IpAddress
_WfNhrpDefNhsServingNetworkAddr_Object = MibTableColumn
wfNhrpDefNhsServingNetworkAddr = _WfNhrpDefNhsServingNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 7),
    _WfNhrpDefNhsServingNetworkAddr_Type()
)
wfNhrpDefNhsServingNetworkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsServingNetworkAddr.setStatus("mandatory")
_WfNhrpDefNhsServingNetworkMask_Type = IpAddress
_WfNhrpDefNhsServingNetworkMask_Object = MibTableColumn
wfNhrpDefNhsServingNetworkMask = _WfNhrpDefNhsServingNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 8),
    _WfNhrpDefNhsServingNetworkMask_Type()
)
wfNhrpDefNhsServingNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsServingNetworkMask.setStatus("mandatory")
_WfNhrpDefNhsNbmaAddr_Type = OctetString
_WfNhrpDefNhsNbmaAddr_Object = MibTableColumn
wfNhrpDefNhsNbmaAddr = _WfNhrpDefNhsNbmaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 9),
    _WfNhrpDefNhsNbmaAddr_Type()
)
wfNhrpDefNhsNbmaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpDefNhsNbmaAddr.setStatus("mandatory")


class _WfNhrpDefNhsStatus_Type(Integer32):
    """Custom type wfNhrpDefNhsStatus based on Integer32"""
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


_WfNhrpDefNhsStatus_Type.__name__ = "Integer32"
_WfNhrpDefNhsStatus_Object = MibTableColumn
wfNhrpDefNhsStatus = _WfNhrpDefNhsStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 10),
    _WfNhrpDefNhsStatus_Type()
)
wfNhrpDefNhsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpDefNhsStatus.setStatus("mandatory")


class _WfNhrpDefNhsLayer2Type_Type(Integer32):
    """Custom type wfNhrpDefNhsLayer2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpDefNhsLayer2Type_Type.__name__ = "Integer32"
_WfNhrpDefNhsLayer2Type_Object = MibTableColumn
wfNhrpDefNhsLayer2Type = _WfNhrpDefNhsLayer2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 11),
    _WfNhrpDefNhsLayer2Type_Type()
)
wfNhrpDefNhsLayer2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpDefNhsLayer2Type.setStatus("mandatory")


class _WfNhrpDefNhsLayer3Type_Type(Integer32):
    """Custom type wfNhrpDefNhsLayer3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpDefNhsLayer3Type_Type.__name__ = "Integer32"
_WfNhrpDefNhsLayer3Type_Object = MibTableColumn
wfNhrpDefNhsLayer3Type = _WfNhrpDefNhsLayer3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 12),
    _WfNhrpDefNhsLayer3Type_Type()
)
wfNhrpDefNhsLayer3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpDefNhsLayer3Type.setStatus("mandatory")


class _WfNhrpDefNhsIndex_Type(Integer32):
    """Custom type wfNhrpDefNhsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfNhrpDefNhsIndex_Type.__name__ = "Integer32"
_WfNhrpDefNhsIndex_Object = MibTableColumn
wfNhrpDefNhsIndex = _WfNhrpDefNhsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 3, 1, 13),
    _WfNhrpDefNhsIndex_Type()
)
wfNhrpDefNhsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpDefNhsIndex.setStatus("mandatory")
_WfNhrpNHCacheTable_Object = MibTable
wfNhrpNHCacheTable = _WfNhrpNHCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4)
)
if mibBuilder.loadTexts:
    wfNhrpNHCacheTable.setStatus("mandatory")
_WfNhrpNHCacheEntry_Object = MibTableRow
wfNhrpNHCacheEntry = _WfNhrpNHCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1)
)
wfNhrpNHCacheEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCacheSlot"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCacheLayer2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCacheLayer3Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCacheDestAddr"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCacheDestAddrPrefixLen"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpNHCachePrefOrder"),
)
if mibBuilder.loadTexts:
    wfNhrpNHCacheEntry.setStatus("mandatory")
_WfNhrpNHCacheSlot_Type = Integer32
_WfNhrpNHCacheSlot_Object = MibTableColumn
wfNhrpNHCacheSlot = _WfNhrpNHCacheSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 1),
    _WfNhrpNHCacheSlot_Type()
)
wfNhrpNHCacheSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCacheSlot.setStatus("mandatory")


class _WfNhrpNHCacheLayer2Type_Type(Integer32):
    """Custom type wfNhrpNHCacheLayer2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpNHCacheLayer2Type_Type.__name__ = "Integer32"
_WfNhrpNHCacheLayer2Type_Object = MibTableColumn
wfNhrpNHCacheLayer2Type = _WfNhrpNHCacheLayer2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 2),
    _WfNhrpNHCacheLayer2Type_Type()
)
wfNhrpNHCacheLayer2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCacheLayer2Type.setStatus("mandatory")


class _WfNhrpNHCacheLayer3Type_Type(Integer32):
    """Custom type wfNhrpNHCacheLayer3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpNHCacheLayer3Type_Type.__name__ = "Integer32"
_WfNhrpNHCacheLayer3Type_Object = MibTableColumn
wfNhrpNHCacheLayer3Type = _WfNhrpNHCacheLayer3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 3),
    _WfNhrpNHCacheLayer3Type_Type()
)
wfNhrpNHCacheLayer3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCacheLayer3Type.setStatus("mandatory")
_WfNhrpNHCacheDestAddr_Type = IpAddress
_WfNhrpNHCacheDestAddr_Object = MibTableColumn
wfNhrpNHCacheDestAddr = _WfNhrpNHCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 4),
    _WfNhrpNHCacheDestAddr_Type()
)
wfNhrpNHCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCacheDestAddr.setStatus("mandatory")


class _WfNhrpNHCacheDestAddrPrefixLen_Type(Integer32):
    """Custom type wfNhrpNHCacheDestAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfNhrpNHCacheDestAddrPrefixLen_Type.__name__ = "Integer32"
_WfNhrpNHCacheDestAddrPrefixLen_Object = MibTableColumn
wfNhrpNHCacheDestAddrPrefixLen = _WfNhrpNHCacheDestAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 5),
    _WfNhrpNHCacheDestAddrPrefixLen_Type()
)
wfNhrpNHCacheDestAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCacheDestAddrPrefixLen.setStatus("mandatory")
_WfNhrpNHCachePrefOrder_Type = Integer32
_WfNhrpNHCachePrefOrder_Object = MibTableColumn
wfNhrpNHCachePrefOrder = _WfNhrpNHCachePrefOrder_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 6),
    _WfNhrpNHCachePrefOrder_Type()
)
wfNhrpNHCachePrefOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpNHCachePrefOrder.setStatus("mandatory")
_WfNhrpNHCacheNhProtAddr_Type = IpAddress
_WfNhrpNHCacheNhProtAddr_Object = MibTableColumn
wfNhrpNHCacheNhProtAddr = _WfNhrpNHCacheNhProtAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 7),
    _WfNhrpNHCacheNhProtAddr_Type()
)
wfNhrpNHCacheNhProtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheNhProtAddr.setStatus("mandatory")


class _WfNhrpNHCacheNhNbmaAddr_Type(DisplayString):
    """Custom type wfNhrpNHCacheNhNbmaAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WfNhrpNHCacheNhNbmaAddr_Type.__name__ = "DisplayString"
_WfNhrpNHCacheNhNbmaAddr_Object = MibTableColumn
wfNhrpNHCacheNhNbmaAddr = _WfNhrpNHCacheNhNbmaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 8),
    _WfNhrpNHCacheNhNbmaAddr_Type()
)
wfNhrpNHCacheNhNbmaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheNhNbmaAddr.setStatus("mandatory")


class _WfNhrpNHCacheHoldTime_Type(Integer32):
    """Custom type wfNhrpNHCacheHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              30,
              200)
        )
    )
    namedValues = NamedValues(
        *(("default", 30),
          ("maximum", 200),
          ("minimum", 10))
    )


_WfNhrpNHCacheHoldTime_Type.__name__ = "Integer32"
_WfNhrpNHCacheHoldTime_Object = MibTableColumn
wfNhrpNHCacheHoldTime = _WfNhrpNHCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 9),
    _WfNhrpNHCacheHoldTime_Type()
)
wfNhrpNHCacheHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheHoldTime.setStatus("mandatory")
_WfNhrpNHCacheFlags_Type = Integer32
_WfNhrpNHCacheFlags_Object = MibTableColumn
wfNhrpNHCacheFlags = _WfNhrpNHCacheFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 10),
    _WfNhrpNHCacheFlags_Type()
)
wfNhrpNHCacheFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheFlags.setStatus("mandatory")
_WfNhrpNHCachePrefValue_Type = Integer32
_WfNhrpNHCachePrefValue_Object = MibTableColumn
wfNhrpNHCachePrefValue = _WfNhrpNHCachePrefValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 11),
    _WfNhrpNHCachePrefValue_Type()
)
wfNhrpNHCachePrefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCachePrefValue.setStatus("mandatory")
_WfNhrpNHCacheMtu_Type = Integer32
_WfNhrpNHCacheMtu_Object = MibTableColumn
wfNhrpNHCacheMtu = _WfNhrpNHCacheMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 12),
    _WfNhrpNHCacheMtu_Type()
)
wfNhrpNHCacheMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheMtu.setStatus("mandatory")


class _WfNhrpNHCacheDelete_Type(Integer32):
    """Custom type wfNhrpNHCacheDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNhrpNHCacheDelete_Type.__name__ = "Integer32"
_WfNhrpNHCacheDelete_Object = MibTableColumn
wfNhrpNHCacheDelete = _WfNhrpNHCacheDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 4, 1, 13),
    _WfNhrpNHCacheDelete_Type()
)
wfNhrpNHCacheDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpNHCacheDelete.setStatus("mandatory")
_WfNhrpTest_ObjectIdentity = ObjectIdentity
wfNhrpTest = _WfNhrpTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5)
)


class _WfNhrpTestDelete_Type(Integer32):
    """Custom type wfNhrpTestDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNhrpTestDelete_Type.__name__ = "Integer32"
_WfNhrpTestDelete_Object = MibScalar
wfNhrpTestDelete = _WfNhrpTestDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 1),
    _WfNhrpTestDelete_Type()
)
wfNhrpTestDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestDelete.setStatus("mandatory")


class _WfNhrpTestLayer2Type_Type(Integer32):
    """Custom type wfNhrpTestLayer2Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpTestLayer2Type_Type.__name__ = "Integer32"
_WfNhrpTestLayer2Type_Object = MibScalar
wfNhrpTestLayer2Type = _WfNhrpTestLayer2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 2),
    _WfNhrpTestLayer2Type_Type()
)
wfNhrpTestLayer2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestLayer2Type.setStatus("mandatory")


class _WfNhrpTestLayer3Type_Type(Integer32):
    """Custom type wfNhrpTestLayer3Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpTestLayer3Type_Type.__name__ = "Integer32"
_WfNhrpTestLayer3Type_Object = MibScalar
wfNhrpTestLayer3Type = _WfNhrpTestLayer3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 3),
    _WfNhrpTestLayer3Type_Type()
)
wfNhrpTestLayer3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestLayer3Type.setStatus("mandatory")


class _WfNhrpTestSlot_Type(Integer32):
    """Custom type wfNhrpTestSlot based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("maximum", 16),
          ("minimum", 1))
    )


_WfNhrpTestSlot_Type.__name__ = "Integer32"
_WfNhrpTestSlot_Object = MibScalar
wfNhrpTestSlot = _WfNhrpTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 4),
    _WfNhrpTestSlot_Type()
)
wfNhrpTestSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestSlot.setStatus("mandatory")


class _WfNhrpTestNHRPeriod_Type(Integer32):
    """Custom type wfNhrpTestNHRPeriod based on Integer32"""
    defaultValue = 5000


_WfNhrpTestNHRPeriod_Object = MibScalar
wfNhrpTestNHRPeriod = _WfNhrpTestNHRPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 5),
    _WfNhrpTestNHRPeriod_Type()
)
wfNhrpTestNHRPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestNHRPeriod.setStatus("mandatory")
_WfNhrpTestNHRDestAddr_Type = IpAddress
_WfNhrpTestNHRDestAddr_Object = MibScalar
wfNhrpTestNHRDestAddr = _WfNhrpTestNHRDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 6),
    _WfNhrpTestNHRDestAddr_Type()
)
wfNhrpTestNHRDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestNHRDestAddr.setStatus("mandatory")
_WfNhrpTestNHRDestPrefix_Type = Integer32
_WfNhrpTestNHRDestPrefix_Object = MibScalar
wfNhrpTestNHRDestPrefix = _WfNhrpTestNHRDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 7),
    _WfNhrpTestNHRDestPrefix_Type()
)
wfNhrpTestNHRDestPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestNHRDestPrefix.setStatus("mandatory")


class _WfNhrpTestNHRReqOpt_Type(Integer32):
    """Custom type wfNhrpTestNHRReqOpt based on Integer32"""
    defaultValue = 0


_WfNhrpTestNHRReqOpt_Object = MibScalar
wfNhrpTestNHRReqOpt = _WfNhrpTestNHRReqOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 8),
    _WfNhrpTestNHRReqOpt_Type()
)
wfNhrpTestNHRReqOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestNHRReqOpt.setStatus("mandatory")


class _WfNhrpTestNHRReqQOS_Type(DisplayString):
    """Custom type wfNhrpTestNHRReqQOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_WfNhrpTestNHRReqQOS_Type.__name__ = "DisplayString"
_WfNhrpTestNHRReqQOS_Object = MibScalar
wfNhrpTestNHRReqQOS = _WfNhrpTestNHRReqQOS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 9),
    _WfNhrpTestNHRReqQOS_Type()
)
wfNhrpTestNHRReqQOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestNHRReqQOS.setStatus("mandatory")


class _WfNhrpTestLogDisable_Type(Integer32):
    """Custom type wfNhrpTestLogDisable based on Integer32"""
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


_WfNhrpTestLogDisable_Type.__name__ = "Integer32"
_WfNhrpTestLogDisable_Object = MibScalar
wfNhrpTestLogDisable = _WfNhrpTestLogDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 10),
    _WfNhrpTestLogDisable_Type()
)
wfNhrpTestLogDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestLogDisable.setStatus("mandatory")


class _WfNhrpTestRegCmd_Type(Integer32):
    """Custom type wfNhrpTestRegCmd based on Integer32"""
    defaultValue = 1

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
        *(("ignore", 1),
          ("mpsAddMps", 9),
          ("mpsDelMps", 10),
          ("mpsPurgeReq", 7),
          ("mpsPurgeRply", 8),
          ("mpsResReq", 5),
          ("mpsResRply", 6),
          ("nhreq", 4),
          ("purge", 3),
          ("register", 2))
    )


_WfNhrpTestRegCmd_Type.__name__ = "Integer32"
_WfNhrpTestRegCmd_Object = MibScalar
wfNhrpTestRegCmd = _WfNhrpTestRegCmd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 11),
    _WfNhrpTestRegCmd_Type()
)
wfNhrpTestRegCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegCmd.setStatus("mandatory")
_WfNhrpTestRegNhsAddr_Type = IpAddress
_WfNhrpTestRegNhsAddr_Object = MibScalar
wfNhrpTestRegNhsAddr = _WfNhrpTestRegNhsAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 12),
    _WfNhrpTestRegNhsAddr_Type()
)
wfNhrpTestRegNhsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegNhsAddr.setStatus("mandatory")


class _WfNhrpTestRegReqOpt_Type(Integer32):
    """Custom type wfNhrpTestRegReqOpt based on Integer32"""
    defaultValue = 0


_WfNhrpTestRegReqOpt_Object = MibScalar
wfNhrpTestRegReqOpt = _WfNhrpTestRegReqOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 13),
    _WfNhrpTestRegReqOpt_Type()
)
wfNhrpTestRegReqOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegReqOpt.setStatus("mandatory")


class _WfNhrpTestRegClientHoldTime_Type(Integer32):
    """Custom type wfNhrpTestRegClientHoldTime based on Integer32"""
    defaultValue = 0


_WfNhrpTestRegClientHoldTime_Object = MibScalar
wfNhrpTestRegClientHoldTime = _WfNhrpTestRegClientHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 14),
    _WfNhrpTestRegClientHoldTime_Type()
)
wfNhrpTestRegClientHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientHoldTime.setStatus("mandatory")


class _WfNhrpTestRegClientPrefVal_Type(Integer32):
    """Custom type wfNhrpTestRegClientPrefVal based on Integer32"""
    defaultValue = 0


_WfNhrpTestRegClientPrefVal_Object = MibScalar
wfNhrpTestRegClientPrefVal = _WfNhrpTestRegClientPrefVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 15),
    _WfNhrpTestRegClientPrefVal_Type()
)
wfNhrpTestRegClientPrefVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientPrefVal.setStatus("mandatory")


class _WfNhrpTestRegClientMtu_Type(Integer32):
    """Custom type wfNhrpTestRegClientMtu based on Integer32"""
    defaultValue = 0


_WfNhrpTestRegClientMtu_Object = MibScalar
wfNhrpTestRegClientMtu = _WfNhrpTestRegClientMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 16),
    _WfNhrpTestRegClientMtu_Type()
)
wfNhrpTestRegClientMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientMtu.setStatus("mandatory")
_WfNhrpTestRegClientPrefix_Type = Integer32
_WfNhrpTestRegClientPrefix_Object = MibScalar
wfNhrpTestRegClientPrefix = _WfNhrpTestRegClientPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 17),
    _WfNhrpTestRegClientPrefix_Type()
)
wfNhrpTestRegClientPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientPrefix.setStatus("mandatory")
_WfNhrpTestRegClientProto_Type = IpAddress
_WfNhrpTestRegClientProto_Object = MibScalar
wfNhrpTestRegClientProto = _WfNhrpTestRegClientProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 18),
    _WfNhrpTestRegClientProto_Type()
)
wfNhrpTestRegClientProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientProto.setStatus("mandatory")


class _WfNhrpTestRegClientNbma_Type(DisplayString):
    """Custom type wfNhrpTestRegClientNbma based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WfNhrpTestRegClientNbma_Type.__name__ = "DisplayString"
_WfNhrpTestRegClientNbma_Object = MibScalar
wfNhrpTestRegClientNbma = _WfNhrpTestRegClientNbma_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 19),
    _WfNhrpTestRegClientNbma_Type()
)
wfNhrpTestRegClientNbma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestRegClientNbma.setStatus("mandatory")
_WfNhrpTestMpsGH_Type = Integer32
_WfNhrpTestMpsGH_Object = MibScalar
wfNhrpTestMpsGH = _WfNhrpTestMpsGH_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 20),
    _WfNhrpTestMpsGH_Type()
)
wfNhrpTestMpsGH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestMpsGH.setStatus("mandatory")
_WfNhrpTestMpsCct_Type = Integer32
_WfNhrpTestMpsCct_Object = MibScalar
wfNhrpTestMpsCct = _WfNhrpTestMpsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 5, 21),
    _WfNhrpTestMpsCct_Type()
)
wfNhrpTestMpsCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNhrpTestMpsCct.setStatus("mandatory")
_WfNhrpClientStatTable_Object = MibTable
wfNhrpClientStatTable = _WfNhrpClientStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6)
)
if mibBuilder.loadTexts:
    wfNhrpClientStatTable.setStatus("mandatory")
_WfNhrpClientStatEntry_Object = MibTableRow
wfNhrpClientStatEntry = _WfNhrpClientStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1)
)
wfNhrpClientStatEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpClientStatL2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpClientStatL3Type"),
)
if mibBuilder.loadTexts:
    wfNhrpClientStatEntry.setStatus("mandatory")


class _WfNhrpClientStatL2Type_Type(Integer32):
    """Custom type wfNhrpClientStatL2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpClientStatL2Type_Type.__name__ = "Integer32"
_WfNhrpClientStatL2Type_Object = MibTableColumn
wfNhrpClientStatL2Type = _WfNhrpClientStatL2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 1),
    _WfNhrpClientStatL2Type_Type()
)
wfNhrpClientStatL2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatL2Type.setStatus("mandatory")


class _WfNhrpClientStatL3Type_Type(Integer32):
    """Custom type wfNhrpClientStatL3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpClientStatL3Type_Type.__name__ = "Integer32"
_WfNhrpClientStatL3Type_Object = MibTableColumn
wfNhrpClientStatL3Type = _WfNhrpClientStatL3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 2),
    _WfNhrpClientStatL3Type_Type()
)
wfNhrpClientStatL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatL3Type.setStatus("mandatory")
_WfNhrpClientStatTxResolveReq_Type = Counter32
_WfNhrpClientStatTxResolveReq_Object = MibTableColumn
wfNhrpClientStatTxResolveReq = _WfNhrpClientStatTxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 3),
    _WfNhrpClientStatTxResolveReq_Type()
)
wfNhrpClientStatTxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatTxResolveReq.setStatus("mandatory")
_WfNhrpClientStatRxResolveReplyAck_Type = Counter32
_WfNhrpClientStatRxResolveReplyAck_Object = MibTableColumn
wfNhrpClientStatRxResolveReplyAck = _WfNhrpClientStatRxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 4),
    _WfNhrpClientStatRxResolveReplyAck_Type()
)
wfNhrpClientStatRxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxResolveReplyAck.setStatus("mandatory")
_WfNhrpClientStatRxResolveReplyNak_Type = Counter32
_WfNhrpClientStatRxResolveReplyNak_Object = MibTableColumn
wfNhrpClientStatRxResolveReplyNak = _WfNhrpClientStatRxResolveReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 5),
    _WfNhrpClientStatRxResolveReplyNak_Type()
)
wfNhrpClientStatRxResolveReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxResolveReplyNak.setStatus("mandatory")
_WfNhrpClientStatTxRegisterReq_Type = Counter32
_WfNhrpClientStatTxRegisterReq_Object = MibTableColumn
wfNhrpClientStatTxRegisterReq = _WfNhrpClientStatTxRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 6),
    _WfNhrpClientStatTxRegisterReq_Type()
)
wfNhrpClientStatTxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatTxRegisterReq.setStatus("mandatory")
_WfNhrpClientStatRxRegisterReplyAck_Type = Counter32
_WfNhrpClientStatRxRegisterReplyAck_Object = MibTableColumn
wfNhrpClientStatRxRegisterReplyAck = _WfNhrpClientStatRxRegisterReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 7),
    _WfNhrpClientStatRxRegisterReplyAck_Type()
)
wfNhrpClientStatRxRegisterReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxRegisterReplyAck.setStatus("mandatory")
_WfNhrpClientStatRxRegisterReplyNak_Type = Counter32
_WfNhrpClientStatRxRegisterReplyNak_Object = MibTableColumn
wfNhrpClientStatRxRegisterReplyNak = _WfNhrpClientStatRxRegisterReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 8),
    _WfNhrpClientStatRxRegisterReplyNak_Type()
)
wfNhrpClientStatRxRegisterReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxRegisterReplyNak.setStatus("mandatory")
_WfNhrpClientStatTxPurgeReq_Type = Counter32
_WfNhrpClientStatTxPurgeReq_Object = MibTableColumn
wfNhrpClientStatTxPurgeReq = _WfNhrpClientStatTxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 9),
    _WfNhrpClientStatTxPurgeReq_Type()
)
wfNhrpClientStatTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatTxPurgeReq.setStatus("mandatory")
_WfNhrpClientStatRxPurgeReplyAck_Type = Counter32
_WfNhrpClientStatRxPurgeReplyAck_Object = MibTableColumn
wfNhrpClientStatRxPurgeReplyAck = _WfNhrpClientStatRxPurgeReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 10),
    _WfNhrpClientStatRxPurgeReplyAck_Type()
)
wfNhrpClientStatRxPurgeReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxPurgeReplyAck.setStatus("mandatory")
_WfNhrpClientStatRxPurgeReplyNak_Type = Counter32
_WfNhrpClientStatRxPurgeReplyNak_Object = MibTableColumn
wfNhrpClientStatRxPurgeReplyNak = _WfNhrpClientStatRxPurgeReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 11),
    _WfNhrpClientStatRxPurgeReplyNak_Type()
)
wfNhrpClientStatRxPurgeReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxPurgeReplyNak.setStatus("mandatory")
_WfNhrpClientStatUnsolicitPurgeReq_Type = Counter32
_WfNhrpClientStatUnsolicitPurgeReq_Object = MibTableColumn
wfNhrpClientStatUnsolicitPurgeReq = _WfNhrpClientStatUnsolicitPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 12),
    _WfNhrpClientStatUnsolicitPurgeReq_Type()
)
wfNhrpClientStatUnsolicitPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatUnsolicitPurgeReq.setStatus("mandatory")
_WfNhrpClientStatTxError_Type = Counter32
_WfNhrpClientStatTxError_Object = MibTableColumn
wfNhrpClientStatTxError = _WfNhrpClientStatTxError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 13),
    _WfNhrpClientStatTxError_Type()
)
wfNhrpClientStatTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatTxError.setStatus("mandatory")
_WfNhrpClientStatRxError_Type = Counter32
_WfNhrpClientStatRxError_Object = MibTableColumn
wfNhrpClientStatRxError = _WfNhrpClientStatRxError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 14),
    _WfNhrpClientStatRxError_Type()
)
wfNhrpClientStatRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRxError.setStatus("mandatory")
_WfNhrpClientStatLocalError_Type = Counter32
_WfNhrpClientStatLocalError_Object = MibTableColumn
wfNhrpClientStatLocalError = _WfNhrpClientStatLocalError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 15),
    _WfNhrpClientStatLocalError_Type()
)
wfNhrpClientStatLocalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatLocalError.setStatus("mandatory")
_WfNhrpClientStatRetryReq_Type = Counter32
_WfNhrpClientStatRetryReq_Object = MibTableColumn
wfNhrpClientStatRetryReq = _WfNhrpClientStatRetryReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 6, 1, 16),
    _WfNhrpClientStatRetryReq_Type()
)
wfNhrpClientStatRetryReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpClientStatRetryReq.setStatus("mandatory")
_WfNhrpServerStatTable_Object = MibTable
wfNhrpServerStatTable = _WfNhrpServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7)
)
if mibBuilder.loadTexts:
    wfNhrpServerStatTable.setStatus("mandatory")
_WfNhrpServerStatEntry_Object = MibTableRow
wfNhrpServerStatEntry = _WfNhrpServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1)
)
wfNhrpServerStatEntry.setIndexNames(
    (0, "Wellfleet-NHRP-MIB", "wfNhrpServerStatL2Type"),
    (0, "Wellfleet-NHRP-MIB", "wfNhrpServerStatL3Type"),
)
if mibBuilder.loadTexts:
    wfNhrpServerStatEntry.setStatus("mandatory")


class _WfNhrpServerStatL2Type_Type(Integer32):
    """Custom type wfNhrpServerStatL2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_WfNhrpServerStatL2Type_Type.__name__ = "Integer32"
_WfNhrpServerStatL2Type_Object = MibTableColumn
wfNhrpServerStatL2Type = _WfNhrpServerStatL2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 1),
    _WfNhrpServerStatL2Type_Type()
)
wfNhrpServerStatL2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatL2Type.setStatus("mandatory")


class _WfNhrpServerStatL3Type_Type(Integer32):
    """Custom type wfNhrpServerStatL3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_WfNhrpServerStatL3Type_Type.__name__ = "Integer32"
_WfNhrpServerStatL3Type_Object = MibTableColumn
wfNhrpServerStatL3Type = _WfNhrpServerStatL3Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 2),
    _WfNhrpServerStatL3Type_Type()
)
wfNhrpServerStatL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatL3Type.setStatus("mandatory")
_WfNhrpServerStatRxResolveReq_Type = Counter32
_WfNhrpServerStatRxResolveReq_Object = MibTableColumn
wfNhrpServerStatRxResolveReq = _WfNhrpServerStatRxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 3),
    _WfNhrpServerStatRxResolveReq_Type()
)
wfNhrpServerStatRxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatRxResolveReq.setStatus("mandatory")
_WfNhrpServerStatTxResolveReplyAck_Type = Counter32
_WfNhrpServerStatTxResolveReplyAck_Object = MibTableColumn
wfNhrpServerStatTxResolveReplyAck = _WfNhrpServerStatTxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 4),
    _WfNhrpServerStatTxResolveReplyAck_Type()
)
wfNhrpServerStatTxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxResolveReplyAck.setStatus("mandatory")
_WfNhrpServerStatTxResolveReplyNak_Type = Counter32
_WfNhrpServerStatTxResolveReplyNak_Object = MibTableColumn
wfNhrpServerStatTxResolveReplyNak = _WfNhrpServerStatTxResolveReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 5),
    _WfNhrpServerStatTxResolveReplyNak_Type()
)
wfNhrpServerStatTxResolveReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxResolveReplyNak.setStatus("mandatory")
_WfNhrpServerStatRxRegisterReq_Type = Counter32
_WfNhrpServerStatRxRegisterReq_Object = MibTableColumn
wfNhrpServerStatRxRegisterReq = _WfNhrpServerStatRxRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 6),
    _WfNhrpServerStatRxRegisterReq_Type()
)
wfNhrpServerStatRxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatRxRegisterReq.setStatus("mandatory")
_WfNhrpServerStatTxRegisterReplyAck_Type = Counter32
_WfNhrpServerStatTxRegisterReplyAck_Object = MibTableColumn
wfNhrpServerStatTxRegisterReplyAck = _WfNhrpServerStatTxRegisterReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 7),
    _WfNhrpServerStatTxRegisterReplyAck_Type()
)
wfNhrpServerStatTxRegisterReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxRegisterReplyAck.setStatus("mandatory")
_WfNhrpServerStatTxRegisterReplyNak_Type = Counter32
_WfNhrpServerStatTxRegisterReplyNak_Object = MibTableColumn
wfNhrpServerStatTxRegisterReplyNak = _WfNhrpServerStatTxRegisterReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 8),
    _WfNhrpServerStatTxRegisterReplyNak_Type()
)
wfNhrpServerStatTxRegisterReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxRegisterReplyNak.setStatus("mandatory")
_WfNhrpServerStatRxPurgeReq_Type = Counter32
_WfNhrpServerStatRxPurgeReq_Object = MibTableColumn
wfNhrpServerStatRxPurgeReq = _WfNhrpServerStatRxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 9),
    _WfNhrpServerStatRxPurgeReq_Type()
)
wfNhrpServerStatRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatRxPurgeReq.setStatus("mandatory")
_WfNhrpServerStatTxPurgeReplyAck_Type = Counter32
_WfNhrpServerStatTxPurgeReplyAck_Object = MibTableColumn
wfNhrpServerStatTxPurgeReplyAck = _WfNhrpServerStatTxPurgeReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 10),
    _WfNhrpServerStatTxPurgeReplyAck_Type()
)
wfNhrpServerStatTxPurgeReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxPurgeReplyAck.setStatus("mandatory")
_WfNhrpServerStatTxPurgeReplyNak_Type = Counter32
_WfNhrpServerStatTxPurgeReplyNak_Object = MibTableColumn
wfNhrpServerStatTxPurgeReplyNak = _WfNhrpServerStatTxPurgeReplyNak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 11),
    _WfNhrpServerStatTxPurgeReplyNak_Type()
)
wfNhrpServerStatTxPurgeReplyNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxPurgeReplyNak.setStatus("mandatory")
_WfNhrpServerStatRxError_Type = Counter32
_WfNhrpServerStatRxError_Object = MibTableColumn
wfNhrpServerStatRxError = _WfNhrpServerStatRxError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 12),
    _WfNhrpServerStatRxError_Type()
)
wfNhrpServerStatRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatRxError.setStatus("mandatory")
_WfNhrpServerStatTxError_Type = Counter32
_WfNhrpServerStatTxError_Object = MibTableColumn
wfNhrpServerStatTxError = _WfNhrpServerStatTxError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 13),
    _WfNhrpServerStatTxError_Type()
)
wfNhrpServerStatTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatTxError.setStatus("mandatory")
_WfNhrpServerStatFwdResolveReq_Type = Counter32
_WfNhrpServerStatFwdResolveReq_Object = MibTableColumn
wfNhrpServerStatFwdResolveReq = _WfNhrpServerStatFwdResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 14),
    _WfNhrpServerStatFwdResolveReq_Type()
)
wfNhrpServerStatFwdResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdResolveReq.setStatus("mandatory")
_WfNhrpServerStatFwdResolveReply_Type = Counter32
_WfNhrpServerStatFwdResolveReply_Object = MibTableColumn
wfNhrpServerStatFwdResolveReply = _WfNhrpServerStatFwdResolveReply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 15),
    _WfNhrpServerStatFwdResolveReply_Type()
)
wfNhrpServerStatFwdResolveReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdResolveReply.setStatus("mandatory")
_WfNhrpServerStatFwdRegisterReq_Type = Counter32
_WfNhrpServerStatFwdRegisterReq_Object = MibTableColumn
wfNhrpServerStatFwdRegisterReq = _WfNhrpServerStatFwdRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 16),
    _WfNhrpServerStatFwdRegisterReq_Type()
)
wfNhrpServerStatFwdRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdRegisterReq.setStatus("mandatory")
_WfNhrpServerStatFwdRegisterReply_Type = Counter32
_WfNhrpServerStatFwdRegisterReply_Object = MibTableColumn
wfNhrpServerStatFwdRegisterReply = _WfNhrpServerStatFwdRegisterReply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 17),
    _WfNhrpServerStatFwdRegisterReply_Type()
)
wfNhrpServerStatFwdRegisterReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdRegisterReply.setStatus("mandatory")
_WfNhrpServerStatFwdPurgeReq_Type = Counter32
_WfNhrpServerStatFwdPurgeReq_Object = MibTableColumn
wfNhrpServerStatFwdPurgeReq = _WfNhrpServerStatFwdPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 18),
    _WfNhrpServerStatFwdPurgeReq_Type()
)
wfNhrpServerStatFwdPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdPurgeReq.setStatus("mandatory")
_WfNhrpServerStatFwdPurgeReply_Type = Counter32
_WfNhrpServerStatFwdPurgeReply_Object = MibTableColumn
wfNhrpServerStatFwdPurgeReply = _WfNhrpServerStatFwdPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 19),
    _WfNhrpServerStatFwdPurgeReply_Type()
)
wfNhrpServerStatFwdPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdPurgeReply.setStatus("mandatory")
_WfNhrpServerStatFwdError_Type = Counter32
_WfNhrpServerStatFwdError_Object = MibTableColumn
wfNhrpServerStatFwdError = _WfNhrpServerStatFwdError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 20),
    _WfNhrpServerStatFwdError_Type()
)
wfNhrpServerStatFwdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatFwdError.setStatus("mandatory")
_WfNhrpServerStatDropPkts_Type = Counter32
_WfNhrpServerStatDropPkts_Object = MibTableColumn
wfNhrpServerStatDropPkts = _WfNhrpServerStatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23, 7, 1, 21),
    _WfNhrpServerStatDropPkts_Type()
)
wfNhrpServerStatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNhrpServerStatDropPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NHRP-MIB",
    **{"wfNhrpNetTable": wfNhrpNetTable,
       "wfNhrpNetEntry": wfNhrpNetEntry,
       "wfNhrpDelete": wfNhrpDelete,
       "wfNhrpLayer2Type": wfNhrpLayer2Type,
       "wfNhrpLayer3Type": wfNhrpLayer3Type,
       "wfNhrpNHReqPath": wfNhrpNHReqPath,
       "wfNhrpClientDisable": wfNhrpClientDisable,
       "wfNhrpClientRegInterval": wfNhrpClientRegInterval,
       "wfNhrpClientHoldTime": wfNhrpClientHoldTime,
       "wfNhrpClientReqTimeout": wfNhrpClientReqTimeout,
       "wfNhrpClientReqRetry": wfNhrpClientReqRetry,
       "wfNhrpClientMaxPendRequests": wfNhrpClientMaxPendRequests,
       "wfNhrpServerDisable": wfNhrpServerDisable,
       "wfNhrpServerFwdDisable": wfNhrpServerFwdDisable,
       "wfNhrpServerMaxNhEntries": wfNhrpServerMaxNhEntries,
       "wfNhrpServerMaxPendRequests": wfNhrpServerMaxPendRequests,
       "wfNhrpServerUseBgp": wfNhrpServerUseBgp,
       "wfNhrpServerUseDns": wfNhrpServerUseDns,
       "wfNhrpServerDnsProxyPort": wfNhrpServerDnsProxyPort,
       "wfNhrpServerOverrideNbmaAddr": wfNhrpServerOverrideNbmaAddr,
       "wfNhrpBogusNbmaAddr": wfNhrpBogusNbmaAddr,
       "wfNhrpNhCacheSize": wfNhrpNhCacheSize,
       "wfNhrpQosCacheSize": wfNhrpQosCacheSize,
       "wfNhrpAddrXlateCacheSize": wfNhrpAddrXlateCacheSize,
       "wfNhrpServerLoadBalance": wfNhrpServerLoadBalance,
       "wfNhrpServerNegativeCaching": wfNhrpServerNegativeCaching,
       "wfNhrpServerNegativeTTL": wfNhrpServerNegativeTTL,
       "wfNhrpDebugLevel": wfNhrpDebugLevel,
       "wfNhrpStatReset": wfNhrpStatReset,
       "wfNhrpNhCacheSequence": wfNhrpNhCacheSequence,
       "wfNhrpNhCacheNumEntries": wfNhrpNhCacheNumEntries,
       "wfNhrpQosCacheNumEntries": wfNhrpQosCacheNumEntries,
       "wfNhrpAddrXlateCacheNumEntries": wfNhrpAddrXlateCacheNumEntries,
       "wfNhrpIfTable": wfNhrpIfTable,
       "wfNhrpIfEntry": wfNhrpIfEntry,
       "wfNhrpIfDelete": wfNhrpIfDelete,
       "wfNhrpIfDisable": wfNhrpIfDisable,
       "wfNhrpIfVCType": wfNhrpIfVCType,
       "wfNhrpIfCct": wfNhrpIfCct,
       "wfNhrpIfLayer2Type": wfNhrpIfLayer2Type,
       "wfNhrpIfLayer3Type": wfNhrpIfLayer3Type,
       "wfNhrpIfPktsXmt": wfNhrpIfPktsXmt,
       "wfNhrpDefNhsTable": wfNhrpDefNhsTable,
       "wfNhrpDefNhsEntry": wfNhrpDefNhsEntry,
       "wfNhrpDefNhsDelete": wfNhrpDefNhsDelete,
       "wfNhrpDefNhsDisable": wfNhrpDefNhsDisable,
       "wfNhrpDefNhsCct": wfNhrpDefNhsCct,
       "wfNhrpDefNhsVcid1": wfNhrpDefNhsVcid1,
       "wfNhrpDefNhsVcid2": wfNhrpDefNhsVcid2,
       "wfNhrpDefNhsProtoAddr": wfNhrpDefNhsProtoAddr,
       "wfNhrpDefNhsServingNetworkAddr": wfNhrpDefNhsServingNetworkAddr,
       "wfNhrpDefNhsServingNetworkMask": wfNhrpDefNhsServingNetworkMask,
       "wfNhrpDefNhsNbmaAddr": wfNhrpDefNhsNbmaAddr,
       "wfNhrpDefNhsStatus": wfNhrpDefNhsStatus,
       "wfNhrpDefNhsLayer2Type": wfNhrpDefNhsLayer2Type,
       "wfNhrpDefNhsLayer3Type": wfNhrpDefNhsLayer3Type,
       "wfNhrpDefNhsIndex": wfNhrpDefNhsIndex,
       "wfNhrpNHCacheTable": wfNhrpNHCacheTable,
       "wfNhrpNHCacheEntry": wfNhrpNHCacheEntry,
       "wfNhrpNHCacheSlot": wfNhrpNHCacheSlot,
       "wfNhrpNHCacheLayer2Type": wfNhrpNHCacheLayer2Type,
       "wfNhrpNHCacheLayer3Type": wfNhrpNHCacheLayer3Type,
       "wfNhrpNHCacheDestAddr": wfNhrpNHCacheDestAddr,
       "wfNhrpNHCacheDestAddrPrefixLen": wfNhrpNHCacheDestAddrPrefixLen,
       "wfNhrpNHCachePrefOrder": wfNhrpNHCachePrefOrder,
       "wfNhrpNHCacheNhProtAddr": wfNhrpNHCacheNhProtAddr,
       "wfNhrpNHCacheNhNbmaAddr": wfNhrpNHCacheNhNbmaAddr,
       "wfNhrpNHCacheHoldTime": wfNhrpNHCacheHoldTime,
       "wfNhrpNHCacheFlags": wfNhrpNHCacheFlags,
       "wfNhrpNHCachePrefValue": wfNhrpNHCachePrefValue,
       "wfNhrpNHCacheMtu": wfNhrpNHCacheMtu,
       "wfNhrpNHCacheDelete": wfNhrpNHCacheDelete,
       "wfNhrpTest": wfNhrpTest,
       "wfNhrpTestDelete": wfNhrpTestDelete,
       "wfNhrpTestLayer2Type": wfNhrpTestLayer2Type,
       "wfNhrpTestLayer3Type": wfNhrpTestLayer3Type,
       "wfNhrpTestSlot": wfNhrpTestSlot,
       "wfNhrpTestNHRPeriod": wfNhrpTestNHRPeriod,
       "wfNhrpTestNHRDestAddr": wfNhrpTestNHRDestAddr,
       "wfNhrpTestNHRDestPrefix": wfNhrpTestNHRDestPrefix,
       "wfNhrpTestNHRReqOpt": wfNhrpTestNHRReqOpt,
       "wfNhrpTestNHRReqQOS": wfNhrpTestNHRReqQOS,
       "wfNhrpTestLogDisable": wfNhrpTestLogDisable,
       "wfNhrpTestRegCmd": wfNhrpTestRegCmd,
       "wfNhrpTestRegNhsAddr": wfNhrpTestRegNhsAddr,
       "wfNhrpTestRegReqOpt": wfNhrpTestRegReqOpt,
       "wfNhrpTestRegClientHoldTime": wfNhrpTestRegClientHoldTime,
       "wfNhrpTestRegClientPrefVal": wfNhrpTestRegClientPrefVal,
       "wfNhrpTestRegClientMtu": wfNhrpTestRegClientMtu,
       "wfNhrpTestRegClientPrefix": wfNhrpTestRegClientPrefix,
       "wfNhrpTestRegClientProto": wfNhrpTestRegClientProto,
       "wfNhrpTestRegClientNbma": wfNhrpTestRegClientNbma,
       "wfNhrpTestMpsGH": wfNhrpTestMpsGH,
       "wfNhrpTestMpsCct": wfNhrpTestMpsCct,
       "wfNhrpClientStatTable": wfNhrpClientStatTable,
       "wfNhrpClientStatEntry": wfNhrpClientStatEntry,
       "wfNhrpClientStatL2Type": wfNhrpClientStatL2Type,
       "wfNhrpClientStatL3Type": wfNhrpClientStatL3Type,
       "wfNhrpClientStatTxResolveReq": wfNhrpClientStatTxResolveReq,
       "wfNhrpClientStatRxResolveReplyAck": wfNhrpClientStatRxResolveReplyAck,
       "wfNhrpClientStatRxResolveReplyNak": wfNhrpClientStatRxResolveReplyNak,
       "wfNhrpClientStatTxRegisterReq": wfNhrpClientStatTxRegisterReq,
       "wfNhrpClientStatRxRegisterReplyAck": wfNhrpClientStatRxRegisterReplyAck,
       "wfNhrpClientStatRxRegisterReplyNak": wfNhrpClientStatRxRegisterReplyNak,
       "wfNhrpClientStatTxPurgeReq": wfNhrpClientStatTxPurgeReq,
       "wfNhrpClientStatRxPurgeReplyAck": wfNhrpClientStatRxPurgeReplyAck,
       "wfNhrpClientStatRxPurgeReplyNak": wfNhrpClientStatRxPurgeReplyNak,
       "wfNhrpClientStatUnsolicitPurgeReq": wfNhrpClientStatUnsolicitPurgeReq,
       "wfNhrpClientStatTxError": wfNhrpClientStatTxError,
       "wfNhrpClientStatRxError": wfNhrpClientStatRxError,
       "wfNhrpClientStatLocalError": wfNhrpClientStatLocalError,
       "wfNhrpClientStatRetryReq": wfNhrpClientStatRetryReq,
       "wfNhrpServerStatTable": wfNhrpServerStatTable,
       "wfNhrpServerStatEntry": wfNhrpServerStatEntry,
       "wfNhrpServerStatL2Type": wfNhrpServerStatL2Type,
       "wfNhrpServerStatL3Type": wfNhrpServerStatL3Type,
       "wfNhrpServerStatRxResolveReq": wfNhrpServerStatRxResolveReq,
       "wfNhrpServerStatTxResolveReplyAck": wfNhrpServerStatTxResolveReplyAck,
       "wfNhrpServerStatTxResolveReplyNak": wfNhrpServerStatTxResolveReplyNak,
       "wfNhrpServerStatRxRegisterReq": wfNhrpServerStatRxRegisterReq,
       "wfNhrpServerStatTxRegisterReplyAck": wfNhrpServerStatTxRegisterReplyAck,
       "wfNhrpServerStatTxRegisterReplyNak": wfNhrpServerStatTxRegisterReplyNak,
       "wfNhrpServerStatRxPurgeReq": wfNhrpServerStatRxPurgeReq,
       "wfNhrpServerStatTxPurgeReplyAck": wfNhrpServerStatTxPurgeReplyAck,
       "wfNhrpServerStatTxPurgeReplyNak": wfNhrpServerStatTxPurgeReplyNak,
       "wfNhrpServerStatRxError": wfNhrpServerStatRxError,
       "wfNhrpServerStatTxError": wfNhrpServerStatTxError,
       "wfNhrpServerStatFwdResolveReq": wfNhrpServerStatFwdResolveReq,
       "wfNhrpServerStatFwdResolveReply": wfNhrpServerStatFwdResolveReply,
       "wfNhrpServerStatFwdRegisterReq": wfNhrpServerStatFwdRegisterReq,
       "wfNhrpServerStatFwdRegisterReply": wfNhrpServerStatFwdRegisterReply,
       "wfNhrpServerStatFwdPurgeReq": wfNhrpServerStatFwdPurgeReq,
       "wfNhrpServerStatFwdPurgeReply": wfNhrpServerStatFwdPurgeReply,
       "wfNhrpServerStatFwdError": wfNhrpServerStatFwdError,
       "wfNhrpServerStatDropPkts": wfNhrpServerStatDropPkts}
)
