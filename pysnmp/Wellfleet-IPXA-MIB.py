# SNMP MIB module (Wellfleet-IPXA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPXA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:31 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIpxGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpxGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpxBasicSysTable_Object = MibTable
wfIpxBasicSysTable = _WfIpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15)
)
if mibBuilder.loadTexts:
    wfIpxBasicSysTable.setStatus("mandatory")
_WfIpxBasicSysEntry_Object = MibTableRow
wfIpxBasicSysEntry = _WfIpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1)
)
wfIpxBasicSysEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    wfIpxBasicSysEntry.setStatus("mandatory")


class _WfIpxBasicSysDelete_Type(Integer32):
    """Custom type wfIpxBasicSysDelete based on Integer32"""
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


_WfIpxBasicSysDelete_Type.__name__ = "Integer32"
_WfIpxBasicSysDelete_Object = MibTableColumn
wfIpxBasicSysDelete = _WfIpxBasicSysDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 1),
    _WfIpxBasicSysDelete_Type()
)
wfIpxBasicSysDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysDelete.setStatus("mandatory")


class _WfIpxBasicSysDisable_Type(Integer32):
    """Custom type wfIpxBasicSysDisable based on Integer32"""
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


_WfIpxBasicSysDisable_Type.__name__ = "Integer32"
_WfIpxBasicSysDisable_Object = MibTableColumn
wfIpxBasicSysDisable = _WfIpxBasicSysDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 2),
    _WfIpxBasicSysDisable_Type()
)
wfIpxBasicSysDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysDisable.setStatus("mandatory")


class _WfIpxBasicSysState_Type(Integer32):
    """Custom type wfIpxBasicSysState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxBasicSysState_Type.__name__ = "Integer32"
_WfIpxBasicSysState_Object = MibTableColumn
wfIpxBasicSysState = _WfIpxBasicSysState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 3),
    _WfIpxBasicSysState_Type()
)
wfIpxBasicSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysState.setStatus("mandatory")
_WfIpxBasicSysInstance_Type = Integer32
_WfIpxBasicSysInstance_Object = MibTableColumn
wfIpxBasicSysInstance = _WfIpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 4),
    _WfIpxBasicSysInstance_Type()
)
wfIpxBasicSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInstance.setStatus("mandatory")
_WfIpxBasicSysPrimaryNetworkNumber_Type = OctetString
_WfIpxBasicSysPrimaryNetworkNumber_Object = MibTableColumn
wfIpxBasicSysPrimaryNetworkNumber = _WfIpxBasicSysPrimaryNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 5),
    _WfIpxBasicSysPrimaryNetworkNumber_Type()
)
wfIpxBasicSysPrimaryNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysPrimaryNetworkNumber.setStatus("mandatory")


class _WfIpxBasicSysMultipleHostAddresses_Type(Integer32):
    """Custom type wfIpxBasicSysMultipleHostAddresses based on Integer32"""
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


_WfIpxBasicSysMultipleHostAddresses_Type.__name__ = "Integer32"
_WfIpxBasicSysMultipleHostAddresses_Object = MibTableColumn
wfIpxBasicSysMultipleHostAddresses = _WfIpxBasicSysMultipleHostAddresses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 6),
    _WfIpxBasicSysMultipleHostAddresses_Type()
)
wfIpxBasicSysMultipleHostAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysMultipleHostAddresses.setStatus("mandatory")
_WfIpxBasicSysCfgHostAddress_Type = OctetString
_WfIpxBasicSysCfgHostAddress_Object = MibTableColumn
wfIpxBasicSysCfgHostAddress = _WfIpxBasicSysCfgHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 7),
    _WfIpxBasicSysCfgHostAddress_Type()
)
wfIpxBasicSysCfgHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysCfgHostAddress.setStatus("mandatory")
_WfIpxBasicSysHostAddress_Type = OctetString
_WfIpxBasicSysHostAddress_Object = MibTableColumn
wfIpxBasicSysHostAddress = _WfIpxBasicSysHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 8),
    _WfIpxBasicSysHostAddress_Type()
)
wfIpxBasicSysHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysHostAddress.setStatus("mandatory")
_WfIpxBasicSysRouterName_Type = DisplayString
_WfIpxBasicSysRouterName_Object = MibTableColumn
wfIpxBasicSysRouterName = _WfIpxBasicSysRouterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 9),
    _WfIpxBasicSysRouterName_Type()
)
wfIpxBasicSysRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBasicSysRouterName.setStatus("mandatory")
_WfIpxBasicSysInReceives_Type = Counter32
_WfIpxBasicSysInReceives_Object = MibTableColumn
wfIpxBasicSysInReceives = _WfIpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 10),
    _WfIpxBasicSysInReceives_Type()
)
wfIpxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInReceives.setStatus("mandatory")
_WfIpxBasicSysInHdrErrors_Type = Counter32
_WfIpxBasicSysInHdrErrors_Object = MibTableColumn
wfIpxBasicSysInHdrErrors = _WfIpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 11),
    _WfIpxBasicSysInHdrErrors_Type()
)
wfIpxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInHdrErrors.setStatus("mandatory")
_WfIpxBasicSysInUnknownSockets_Type = Counter32
_WfIpxBasicSysInUnknownSockets_Object = MibTableColumn
wfIpxBasicSysInUnknownSockets = _WfIpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 12),
    _WfIpxBasicSysInUnknownSockets_Type()
)
wfIpxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInUnknownSockets.setStatus("mandatory")
_WfIpxBasicSysInDiscards_Type = Counter32
_WfIpxBasicSysInDiscards_Object = MibTableColumn
wfIpxBasicSysInDiscards = _WfIpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 13),
    _WfIpxBasicSysInDiscards_Type()
)
wfIpxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInDiscards.setStatus("mandatory")
_WfIpxBasicSysInBadChecksums_Type = Counter32
_WfIpxBasicSysInBadChecksums_Object = MibTableColumn
wfIpxBasicSysInBadChecksums = _WfIpxBasicSysInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 14),
    _WfIpxBasicSysInBadChecksums_Type()
)
wfIpxBasicSysInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInBadChecksums.setStatus("mandatory")
_WfIpxBasicSysInDelivers_Type = Counter32
_WfIpxBasicSysInDelivers_Object = MibTableColumn
wfIpxBasicSysInDelivers = _WfIpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 15),
    _WfIpxBasicSysInDelivers_Type()
)
wfIpxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysInDelivers.setStatus("mandatory")
_WfIpxBasicSysNoRoutes_Type = Counter32
_WfIpxBasicSysNoRoutes_Object = MibTableColumn
wfIpxBasicSysNoRoutes = _WfIpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 16),
    _WfIpxBasicSysNoRoutes_Type()
)
wfIpxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysNoRoutes.setStatus("mandatory")
_WfIpxBasicSysOutRequests_Type = Counter32
_WfIpxBasicSysOutRequests_Object = MibTableColumn
wfIpxBasicSysOutRequests = _WfIpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 17),
    _WfIpxBasicSysOutRequests_Type()
)
wfIpxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysOutRequests.setStatus("mandatory")
_WfIpxBasicSysOutMalformedRequests_Type = Counter32
_WfIpxBasicSysOutMalformedRequests_Object = MibTableColumn
wfIpxBasicSysOutMalformedRequests = _WfIpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 18),
    _WfIpxBasicSysOutMalformedRequests_Type()
)
wfIpxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysOutMalformedRequests.setStatus("mandatory")
_WfIpxBasicSysOutPackets_Type = Counter32
_WfIpxBasicSysOutPackets_Object = MibTableColumn
wfIpxBasicSysOutPackets = _WfIpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 19),
    _WfIpxBasicSysOutPackets_Type()
)
wfIpxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysOutPackets.setStatus("mandatory")
_WfIpxBasicSysOpenEncapsFails_Type = Counter32
_WfIpxBasicSysOpenEncapsFails_Object = MibTableColumn
wfIpxBasicSysOpenEncapsFails = _WfIpxBasicSysOpenEncapsFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 20),
    _WfIpxBasicSysOpenEncapsFails_Type()
)
wfIpxBasicSysOpenEncapsFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysOpenEncapsFails.setStatus("mandatory")
_WfIpxBasicSysOutDiscards_Type = Counter32
_WfIpxBasicSysOutDiscards_Object = MibTableColumn
wfIpxBasicSysOutDiscards = _WfIpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 15, 1, 21),
    _WfIpxBasicSysOutDiscards_Type()
)
wfIpxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBasicSysOutDiscards.setStatus("mandatory")
_WfIpxAdvSysTable_Object = MibTable
wfIpxAdvSysTable = _WfIpxAdvSysTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16)
)
if mibBuilder.loadTexts:
    wfIpxAdvSysTable.setStatus("mandatory")
_WfIpxAdvSysEntry_Object = MibTableRow
wfIpxAdvSysEntry = _WfIpxAdvSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1)
)
wfIpxAdvSysEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxAdvSysInstance"),
)
if mibBuilder.loadTexts:
    wfIpxAdvSysEntry.setStatus("mandatory")


class _WfIpxAdvSysDelete_Type(Integer32):
    """Custom type wfIpxAdvSysDelete based on Integer32"""
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


_WfIpxAdvSysDelete_Type.__name__ = "Integer32"
_WfIpxAdvSysDelete_Object = MibTableColumn
wfIpxAdvSysDelete = _WfIpxAdvSysDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 1),
    _WfIpxAdvSysDelete_Type()
)
wfIpxAdvSysDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysDelete.setStatus("mandatory")
_WfIpxAdvSysInstance_Type = Integer32
_WfIpxAdvSysInstance_Object = MibTableColumn
wfIpxAdvSysInstance = _WfIpxAdvSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 2),
    _WfIpxAdvSysInstance_Type()
)
wfIpxAdvSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysInstance.setStatus("mandatory")


class _WfIpxAdvSysRoutingMethod_Type(Integer32):
    """Custom type wfIpxAdvSysRoutingMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hop", 1),
          ("tick", 2))
    )


_WfIpxAdvSysRoutingMethod_Type.__name__ = "Integer32"
_WfIpxAdvSysRoutingMethod_Object = MibTableColumn
wfIpxAdvSysRoutingMethod = _WfIpxAdvSysRoutingMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 3),
    _WfIpxAdvSysRoutingMethod_Type()
)
wfIpxAdvSysRoutingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysRoutingMethod.setStatus("mandatory")


class _WfIpxAdvSysLogFilter_Type(Integer32):
    """Custom type wfIpxAdvSysLogFilter based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("debuginfo", 3),
          ("debuginfotrace", 19),
          ("debugtrace", 17),
          ("info", 2),
          ("infotrace", 18),
          ("trace", 16))
    )


_WfIpxAdvSysLogFilter_Type.__name__ = "Integer32"
_WfIpxAdvSysLogFilter_Object = MibTableColumn
wfIpxAdvSysLogFilter = _WfIpxAdvSysLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 4),
    _WfIpxAdvSysLogFilter_Type()
)
wfIpxAdvSysLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysLogFilter.setStatus("mandatory")


class _WfIpxAdvSysMaximumPath_Type(Integer32):
    """Custom type wfIpxAdvSysMaximumPath based on Integer32"""
    defaultValue = 1


_WfIpxAdvSysMaximumPath_Object = MibTableColumn
wfIpxAdvSysMaximumPath = _WfIpxAdvSysMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 5),
    _WfIpxAdvSysMaximumPath_Type()
)
wfIpxAdvSysMaximumPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysMaximumPath.setStatus("mandatory")


class _WfIpxAdvSysMaxPathSplits_Type(Integer32):
    """Custom type wfIpxAdvSysMaxPathSplits based on Integer32"""
    defaultValue = 1


_WfIpxAdvSysMaxPathSplits_Object = MibTableColumn
wfIpxAdvSysMaxPathSplits = _WfIpxAdvSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 6),
    _WfIpxAdvSysMaxPathSplits_Type()
)
wfIpxAdvSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysMaxPathSplits.setStatus("mandatory")


class _WfIpxAdvSysMaxHops_Type(Integer32):
    """Custom type wfIpxAdvSysMaxHops based on Integer32"""
    defaultValue = 16


_WfIpxAdvSysMaxHops_Object = MibTableColumn
wfIpxAdvSysMaxHops = _WfIpxAdvSysMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 7),
    _WfIpxAdvSysMaxHops_Type()
)
wfIpxAdvSysMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysMaxHops.setStatus("mandatory")
_WfIpxAdvSysInTooManyHops_Type = Counter32
_WfIpxAdvSysInTooManyHops_Object = MibTableColumn
wfIpxAdvSysInTooManyHops = _WfIpxAdvSysInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 8),
    _WfIpxAdvSysInTooManyHops_Type()
)
wfIpxAdvSysInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysInTooManyHops.setStatus("mandatory")
_WfIpxAdvSysInFiltered_Type = Counter32
_WfIpxAdvSysInFiltered_Object = MibTableColumn
wfIpxAdvSysInFiltered = _WfIpxAdvSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 9),
    _WfIpxAdvSysInFiltered_Type()
)
wfIpxAdvSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysInFiltered.setStatus("mandatory")
_WfIpxAdvSysInCompressDiscards_Type = Counter32
_WfIpxAdvSysInCompressDiscards_Object = MibTableColumn
wfIpxAdvSysInCompressDiscards = _WfIpxAdvSysInCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 10),
    _WfIpxAdvSysInCompressDiscards_Type()
)
wfIpxAdvSysInCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysInCompressDiscards.setStatus("mandatory")
_WfIpxAdvSysNETBIOSPackets_Type = Counter32
_WfIpxAdvSysNETBIOSPackets_Object = MibTableColumn
wfIpxAdvSysNETBIOSPackets = _WfIpxAdvSysNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 11),
    _WfIpxAdvSysNETBIOSPackets_Type()
)
wfIpxAdvSysNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysNETBIOSPackets.setStatus("mandatory")
_WfIpxAdvSysForwPackets_Type = Counter32
_WfIpxAdvSysForwPackets_Object = MibTableColumn
wfIpxAdvSysForwPackets = _WfIpxAdvSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 12),
    _WfIpxAdvSysForwPackets_Type()
)
wfIpxAdvSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysForwPackets.setStatus("mandatory")
_WfIpxAdvSysOutFiltered_Type = Counter32
_WfIpxAdvSysOutFiltered_Object = MibTableColumn
wfIpxAdvSysOutFiltered = _WfIpxAdvSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 13),
    _WfIpxAdvSysOutFiltered_Type()
)
wfIpxAdvSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysOutFiltered.setStatus("mandatory")
_WfIpxAdvSysOutCompressDiscards_Type = Counter32
_WfIpxAdvSysOutCompressDiscards_Object = MibTableColumn
wfIpxAdvSysOutCompressDiscards = _WfIpxAdvSysOutCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 14),
    _WfIpxAdvSysOutCompressDiscards_Type()
)
wfIpxAdvSysOutCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysOutCompressDiscards.setStatus("mandatory")


class _WfIpxAdvSysNovellCertificationConformanceDisable_Type(Integer32):
    """Custom type wfIpxAdvSysNovellCertificationConformanceDisable based on Integer32"""
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


_WfIpxAdvSysNovellCertificationConformanceDisable_Type.__name__ = "Integer32"
_WfIpxAdvSysNovellCertificationConformanceDisable_Object = MibTableColumn
wfIpxAdvSysNovellCertificationConformanceDisable = _WfIpxAdvSysNovellCertificationConformanceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 15),
    _WfIpxAdvSysNovellCertificationConformanceDisable_Type()
)
wfIpxAdvSysNovellCertificationConformanceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysNovellCertificationConformanceDisable.setStatus("mandatory")
_WfIpxAdvSysCircCount_Type = Counter32
_WfIpxAdvSysCircCount_Object = MibTableColumn
wfIpxAdvSysCircCount = _WfIpxAdvSysCircCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 16),
    _WfIpxAdvSysCircCount_Type()
)
wfIpxAdvSysCircCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysCircCount.setStatus("mandatory")
_WfIpxAdvSysCfgDestCount_Type = Integer32
_WfIpxAdvSysCfgDestCount_Object = MibTableColumn
wfIpxAdvSysCfgDestCount = _WfIpxAdvSysCfgDestCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 17),
    _WfIpxAdvSysCfgDestCount_Type()
)
wfIpxAdvSysCfgDestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysCfgDestCount.setStatus("mandatory")
_WfIpxAdvSysDestCount_Type = Counter32
_WfIpxAdvSysDestCount_Object = MibTableColumn
wfIpxAdvSysDestCount = _WfIpxAdvSysDestCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 18),
    _WfIpxAdvSysDestCount_Type()
)
wfIpxAdvSysDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysDestCount.setStatus("mandatory")
_WfIpxAdvSysCfgServCount_Type = Integer32
_WfIpxAdvSysCfgServCount_Object = MibTableColumn
wfIpxAdvSysCfgServCount = _WfIpxAdvSysCfgServCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 19),
    _WfIpxAdvSysCfgServCount_Type()
)
wfIpxAdvSysCfgServCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysCfgServCount.setStatus("mandatory")
_WfIpxAdvSysServCount_Type = Counter32
_WfIpxAdvSysServCount_Object = MibTableColumn
wfIpxAdvSysServCount = _WfIpxAdvSysServCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 20),
    _WfIpxAdvSysServCount_Type()
)
wfIpxAdvSysServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysServCount.setStatus("mandatory")
_WfIpxAdvSysCfgHostCount_Type = Integer32
_WfIpxAdvSysCfgHostCount_Object = MibTableColumn
wfIpxAdvSysCfgHostCount = _WfIpxAdvSysCfgHostCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 21),
    _WfIpxAdvSysCfgHostCount_Type()
)
wfIpxAdvSysCfgHostCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysCfgHostCount.setStatus("mandatory")
_WfIpxAdvSysHostCount_Type = Counter32
_WfIpxAdvSysHostCount_Object = MibTableColumn
wfIpxAdvSysHostCount = _WfIpxAdvSysHostCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 22),
    _WfIpxAdvSysHostCount_Type()
)
wfIpxAdvSysHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAdvSysHostCount.setStatus("mandatory")


class _WfIpxAdvSysAgingFrequency_Type(Integer32):
    """Custom type wfIpxAdvSysAgingFrequency based on Integer32"""
    defaultValue = 10


_WfIpxAdvSysAgingFrequency_Object = MibTableColumn
wfIpxAdvSysAgingFrequency = _WfIpxAdvSysAgingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 23),
    _WfIpxAdvSysAgingFrequency_Type()
)
wfIpxAdvSysAgingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysAgingFrequency.setStatus("mandatory")


class _WfIpxAdvSysAgingPendingFrequency_Type(Integer32):
    """Custom type wfIpxAdvSysAgingPendingFrequency based on Integer32"""
    defaultValue = 100


_WfIpxAdvSysAgingPendingFrequency_Object = MibTableColumn
wfIpxAdvSysAgingPendingFrequency = _WfIpxAdvSysAgingPendingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 24),
    _WfIpxAdvSysAgingPendingFrequency_Type()
)
wfIpxAdvSysAgingPendingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysAgingPendingFrequency.setStatus("mandatory")


class _WfIpxAdvSysDefaultRouteEnable_Type(Integer32):
    """Custom type wfIpxAdvSysDefaultRouteEnable based on Integer32"""
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


_WfIpxAdvSysDefaultRouteEnable_Type.__name__ = "Integer32"
_WfIpxAdvSysDefaultRouteEnable_Object = MibTableColumn
wfIpxAdvSysDefaultRouteEnable = _WfIpxAdvSysDefaultRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 25),
    _WfIpxAdvSysDefaultRouteEnable_Type()
)
wfIpxAdvSysDefaultRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysDefaultRouteEnable.setStatus("mandatory")


class _WfIpxAdvSysSapViaDefaultRouteEnable_Type(Integer32):
    """Custom type wfIpxAdvSysSapViaDefaultRouteEnable based on Integer32"""
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


_WfIpxAdvSysSapViaDefaultRouteEnable_Type.__name__ = "Integer32"
_WfIpxAdvSysSapViaDefaultRouteEnable_Object = MibTableColumn
wfIpxAdvSysSapViaDefaultRouteEnable = _WfIpxAdvSysSapViaDefaultRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 26),
    _WfIpxAdvSysSapViaDefaultRouteEnable_Type()
)
wfIpxAdvSysSapViaDefaultRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysSapViaDefaultRouteEnable.setStatus("mandatory")


class _WfIpxAdvSysCT_Type(Integer32):
    """Custom type wfIpxAdvSysCT based on Integer32"""
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


_WfIpxAdvSysCT_Type.__name__ = "Integer32"
_WfIpxAdvSysCT_Object = MibTableColumn
wfIpxAdvSysCT = _WfIpxAdvSysCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 27),
    _WfIpxAdvSysCT_Type()
)
wfIpxAdvSysCT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysCT.setStatus("mandatory")
_WfIpxAdvSysMibReplySlots_Type = DisplayString
_WfIpxAdvSysMibReplySlots_Object = MibTableColumn
wfIpxAdvSysMibReplySlots = _WfIpxAdvSysMibReplySlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 28),
    _WfIpxAdvSysMibReplySlots_Type()
)
wfIpxAdvSysMibReplySlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysMibReplySlots.setStatus("mandatory")


class _WfIpxAdvSysGNSRespMode_Type(Integer32):
    """Custom type wfIpxAdvSysGNSRespMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alphabetical", 1),
          ("lastlearned", 2))
    )


_WfIpxAdvSysGNSRespMode_Type.__name__ = "Integer32"
_WfIpxAdvSysGNSRespMode_Object = MibTableColumn
wfIpxAdvSysGNSRespMode = _WfIpxAdvSysGNSRespMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 29),
    _WfIpxAdvSysGNSRespMode_Type()
)
wfIpxAdvSysGNSRespMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysGNSRespMode.setStatus("mandatory")


class _WfIpxAdvSysMaxNetTblSize_Type(Integer32):
    """Custom type wfIpxAdvSysMaxNetTblSize based on Integer32"""
    defaultValue = 0


_WfIpxAdvSysMaxNetTblSize_Object = MibTableColumn
wfIpxAdvSysMaxNetTblSize = _WfIpxAdvSysMaxNetTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 30),
    _WfIpxAdvSysMaxNetTblSize_Type()
)
wfIpxAdvSysMaxNetTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysMaxNetTblSize.setStatus("mandatory")


class _WfIpxAdvSysNetTblFillNotify_Type(Integer32):
    """Custom type wfIpxAdvSysNetTblFillNotify based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfIpxAdvSysNetTblFillNotify_Type.__name__ = "Integer32"
_WfIpxAdvSysNetTblFillNotify_Object = MibTableColumn
wfIpxAdvSysNetTblFillNotify = _WfIpxAdvSysNetTblFillNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 31),
    _WfIpxAdvSysNetTblFillNotify_Type()
)
wfIpxAdvSysNetTblFillNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysNetTblFillNotify.setStatus("mandatory")


class _WfIpxAdvSysGlobalTrigUpdate_Type(Integer32):
    """Custom type wfIpxAdvSysGlobalTrigUpdate based on Integer32"""
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


_WfIpxAdvSysGlobalTrigUpdate_Type.__name__ = "Integer32"
_WfIpxAdvSysGlobalTrigUpdate_Object = MibTableColumn
wfIpxAdvSysGlobalTrigUpdate = _WfIpxAdvSysGlobalTrigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 32),
    _WfIpxAdvSysGlobalTrigUpdate_Type()
)
wfIpxAdvSysGlobalTrigUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysGlobalTrigUpdate.setStatus("mandatory")


class _WfIpxAdvSysTrigUpdateDelay_Type(Integer32):
    """Custom type wfIpxAdvSysTrigUpdateDelay based on Integer32"""
    defaultValue = 0


_WfIpxAdvSysTrigUpdateDelay_Object = MibTableColumn
wfIpxAdvSysTrigUpdateDelay = _WfIpxAdvSysTrigUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 33),
    _WfIpxAdvSysTrigUpdateDelay_Type()
)
wfIpxAdvSysTrigUpdateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysTrigUpdateDelay.setStatus("mandatory")


class _WfIpxAdvSysLostRouteDelay_Type(Integer32):
    """Custom type wfIpxAdvSysLostRouteDelay based on Integer32"""
    defaultValue = 5


_WfIpxAdvSysLostRouteDelay_Object = MibTableColumn
wfIpxAdvSysLostRouteDelay = _WfIpxAdvSysLostRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 16, 1, 34),
    _WfIpxAdvSysLostRouteDelay_Type()
)
wfIpxAdvSysLostRouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAdvSysLostRouteDelay.setStatus("mandatory")
_WfIpxCircTable_Object = MibTable
wfIpxCircTable = _WfIpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17)
)
if mibBuilder.loadTexts:
    wfIpxCircTable.setStatus("mandatory")
_WfIpxCircEntry_Object = MibTableRow
wfIpxCircEntry = _WfIpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1)
)
wfIpxCircEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxCircSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxCircIndex"),
)
if mibBuilder.loadTexts:
    wfIpxCircEntry.setStatus("mandatory")


class _WfIpxCircDelete_Type(Integer32):
    """Custom type wfIpxCircDelete based on Integer32"""
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


_WfIpxCircDelete_Type.__name__ = "Integer32"
_WfIpxCircDelete_Object = MibTableColumn
wfIpxCircDelete = _WfIpxCircDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 1),
    _WfIpxCircDelete_Type()
)
wfIpxCircDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircDelete.setStatus("mandatory")


class _WfIpxCircDisable_Type(Integer32):
    """Custom type wfIpxCircDisable based on Integer32"""
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


_WfIpxCircDisable_Type.__name__ = "Integer32"
_WfIpxCircDisable_Object = MibTableColumn
wfIpxCircDisable = _WfIpxCircDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 2),
    _WfIpxCircDisable_Type()
)
wfIpxCircDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircDisable.setStatus("mandatory")


class _WfIpxCircState_Type(Integer32):
    """Custom type wfIpxCircState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxCircState_Type.__name__ = "Integer32"
_WfIpxCircState_Object = MibTableColumn
wfIpxCircState = _WfIpxCircState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 3),
    _WfIpxCircState_Type()
)
wfIpxCircState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircState.setStatus("mandatory")
_WfIpxCircSysInstance_Type = Integer32
_WfIpxCircSysInstance_Object = MibTableColumn
wfIpxCircSysInstance = _WfIpxCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 4),
    _WfIpxCircSysInstance_Type()
)
wfIpxCircSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircSysInstance.setStatus("mandatory")
_WfIpxCircIndex_Type = Integer32
_WfIpxCircIndex_Object = MibTableColumn
wfIpxCircIndex = _WfIpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 5),
    _WfIpxCircIndex_Type()
)
wfIpxCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircIndex.setStatus("mandatory")
_WfIpxCircIfIndex_Type = Integer32
_WfIpxCircIfIndex_Object = MibTableColumn
wfIpxCircIfIndex = _WfIpxCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 6),
    _WfIpxCircIfIndex_Type()
)
wfIpxCircIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircIfIndex.setStatus("mandatory")
_WfIpxCircName_Type = DisplayString
_WfIpxCircName_Object = MibTableColumn
wfIpxCircName = _WfIpxCircName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 7),
    _WfIpxCircName_Type()
)
wfIpxCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircName.setStatus("mandatory")


class _WfIpxCircCfgType_Type(Integer32):
    """Custom type wfIpxCircCfgType based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("dynamic", 32),
          ("nlsp", 128),
          ("other", 1),
          ("pt", 4),
          ("unnumberedrip", 16),
          ("wanrip", 8),
          ("ws", 64))
    )


_WfIpxCircCfgType_Type.__name__ = "Integer32"
_WfIpxCircCfgType_Object = MibTableColumn
wfIpxCircCfgType = _WfIpxCircCfgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 8),
    _WfIpxCircCfgType_Type()
)
wfIpxCircCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgType.setStatus("mandatory")
_WfIpxCircLocalMaxPacketSize_Type = Integer32
_WfIpxCircLocalMaxPacketSize_Object = MibTableColumn
wfIpxCircLocalMaxPacketSize = _WfIpxCircLocalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 9),
    _WfIpxCircLocalMaxPacketSize_Type()
)
wfIpxCircLocalMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircLocalMaxPacketSize.setStatus("mandatory")


class _WfIpxCircCfgCompressState_Type(Integer32):
    """Custom type wfIpxCircCfgCompressState based on Integer32"""
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


_WfIpxCircCfgCompressState_Type.__name__ = "Integer32"
_WfIpxCircCfgCompressState_Object = MibTableColumn
wfIpxCircCfgCompressState = _WfIpxCircCfgCompressState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 10),
    _WfIpxCircCfgCompressState_Type()
)
wfIpxCircCfgCompressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgCompressState.setStatus("mandatory")


class _WfIpxCircCompressState_Type(Integer32):
    """Custom type wfIpxCircCompressState based on Integer32"""
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


_WfIpxCircCompressState_Type.__name__ = "Integer32"
_WfIpxCircCompressState_Object = MibTableColumn
wfIpxCircCompressState = _WfIpxCircCompressState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 11),
    _WfIpxCircCompressState_Type()
)
wfIpxCircCompressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressState.setStatus("mandatory")


class _WfIpxCircCompressSlots_Type(Integer32):
    """Custom type wfIpxCircCompressSlots based on Integer32"""
    defaultValue = 16


_WfIpxCircCompressSlots_Object = MibTableColumn
wfIpxCircCompressSlots = _WfIpxCircCompressSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 12),
    _WfIpxCircCompressSlots_Type()
)
wfIpxCircCompressSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCompressSlots.setStatus("mandatory")
_WfIpxCircCompressedSent_Type = Counter32
_WfIpxCircCompressedSent_Object = MibTableColumn
wfIpxCircCompressedSent = _WfIpxCircCompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 13),
    _WfIpxCircCompressedSent_Type()
)
wfIpxCircCompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedSent.setStatus("mandatory")
_WfIpxCircCompressedInitSent_Type = Counter32
_WfIpxCircCompressedInitSent_Object = MibTableColumn
wfIpxCircCompressedInitSent = _WfIpxCircCompressedInitSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 14),
    _WfIpxCircCompressedInitSent_Type()
)
wfIpxCircCompressedInitSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedInitSent.setStatus("mandatory")
_WfIpxCircCompressedRejectsSent_Type = Counter32
_WfIpxCircCompressedRejectsSent_Object = MibTableColumn
wfIpxCircCompressedRejectsSent = _WfIpxCircCompressedRejectsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 15),
    _WfIpxCircCompressedRejectsSent_Type()
)
wfIpxCircCompressedRejectsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedRejectsSent.setStatus("mandatory")
_WfIpxCircUncompressedSent_Type = Counter32
_WfIpxCircUncompressedSent_Object = MibTableColumn
wfIpxCircUncompressedSent = _WfIpxCircUncompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 16),
    _WfIpxCircUncompressedSent_Type()
)
wfIpxCircUncompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircUncompressedSent.setStatus("mandatory")
_WfIpxCircCompressedReceived_Type = Counter32
_WfIpxCircCompressedReceived_Object = MibTableColumn
wfIpxCircCompressedReceived = _WfIpxCircCompressedReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 17),
    _WfIpxCircCompressedReceived_Type()
)
wfIpxCircCompressedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedReceived.setStatus("mandatory")
_WfIpxCircCompressedInitReceived_Type = Counter32
_WfIpxCircCompressedInitReceived_Object = MibTableColumn
wfIpxCircCompressedInitReceived = _WfIpxCircCompressedInitReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 18),
    _WfIpxCircCompressedInitReceived_Type()
)
wfIpxCircCompressedInitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedInitReceived.setStatus("mandatory")
_WfIpxCircCompressedRejectsReceived_Type = Counter32
_WfIpxCircCompressedRejectsReceived_Object = MibTableColumn
wfIpxCircCompressedRejectsReceived = _WfIpxCircCompressedRejectsReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 19),
    _WfIpxCircCompressedRejectsReceived_Type()
)
wfIpxCircCompressedRejectsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircCompressedRejectsReceived.setStatus("mandatory")
_WfIpxCircUncompressedReceived_Type = Counter32
_WfIpxCircUncompressedReceived_Object = MibTableColumn
wfIpxCircUncompressedReceived = _WfIpxCircUncompressedReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 20),
    _WfIpxCircUncompressedReceived_Type()
)
wfIpxCircUncompressedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircUncompressedReceived.setStatus("mandatory")
_WfIpxCircMediaType_Type = Integer32
_WfIpxCircMediaType_Object = MibTableColumn
wfIpxCircMediaType = _WfIpxCircMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 21),
    _WfIpxCircMediaType_Type()
)
wfIpxCircMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircMediaType.setStatus("mandatory")
_WfIpxCircCfgNetworkNumber_Type = OctetString
_WfIpxCircCfgNetworkNumber_Object = MibTableColumn
wfIpxCircCfgNetworkNumber = _WfIpxCircCfgNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 22),
    _WfIpxCircCfgNetworkNumber_Type()
)
wfIpxCircCfgNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgNetworkNumber.setStatus("mandatory")
_WfIpxCircNetworkNumber_Type = OctetString
_WfIpxCircNetworkNumber_Object = MibTableColumn
wfIpxCircNetworkNumber = _WfIpxCircNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 23),
    _WfIpxCircNetworkNumber_Type()
)
wfIpxCircNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircNetworkNumber.setStatus("mandatory")
_WfIpxCircCommonNetworkNumber_Type = OctetString
_WfIpxCircCommonNetworkNumber_Object = MibTableColumn
wfIpxCircCommonNetworkNumber = _WfIpxCircCommonNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 24),
    _WfIpxCircCommonNetworkNumber_Type()
)
wfIpxCircCommonNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCommonNetworkNumber.setStatus("mandatory")


class _WfIpxCircCfgHostAddress_Type(OctetString):
    """Custom type wfIpxCircCfgHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfIpxCircCfgHostAddress_Type.__name__ = "OctetString"
_WfIpxCircCfgHostAddress_Object = MibTableColumn
wfIpxCircCfgHostAddress = _WfIpxCircCfgHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 25),
    _WfIpxCircCfgHostAddress_Type()
)
wfIpxCircCfgHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgHostAddress.setStatus("mandatory")
_WfIpxCircHostAddress_Type = OctetString
_WfIpxCircHostAddress_Object = MibTableColumn
wfIpxCircHostAddress = _WfIpxCircHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 26),
    _WfIpxCircHostAddress_Type()
)
wfIpxCircHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircHostAddress.setStatus("mandatory")
_WfIpxCircMacAddress_Type = OctetString
_WfIpxCircMacAddress_Object = MibTableColumn
wfIpxCircMacAddress = _WfIpxCircMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 27),
    _WfIpxCircMacAddress_Type()
)
wfIpxCircMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircMacAddress.setStatus("mandatory")
_WfIpxCircCfgBroadcastAddress_Type = OctetString
_WfIpxCircCfgBroadcastAddress_Object = MibTableColumn
wfIpxCircCfgBroadcastAddress = _WfIpxCircCfgBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 28),
    _WfIpxCircCfgBroadcastAddress_Type()
)
wfIpxCircCfgBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgBroadcastAddress.setStatus("mandatory")
_WfIpxCircBroadcastAddress_Type = OctetString
_WfIpxCircBroadcastAddress_Object = MibTableColumn
wfIpxCircBroadcastAddress = _WfIpxCircBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 29),
    _WfIpxCircBroadcastAddress_Type()
)
wfIpxCircBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircBroadcastAddress.setStatus("mandatory")
_WfIpxCircCfgMulticastAddress_Type = OctetString
_WfIpxCircCfgMulticastAddress_Object = MibTableColumn
wfIpxCircCfgMulticastAddress = _WfIpxCircCfgMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 30),
    _WfIpxCircCfgMulticastAddress_Type()
)
wfIpxCircCfgMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgMulticastAddress.setStatus("mandatory")
_WfIpxCircMulticastAddress_Type = OctetString
_WfIpxCircMulticastAddress_Object = MibTableColumn
wfIpxCircMulticastAddress = _WfIpxCircMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 31),
    _WfIpxCircMulticastAddress_Type()
)
wfIpxCircMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircMulticastAddress.setStatus("mandatory")
_WfIpxCircStateChanges_Type = Counter32
_WfIpxCircStateChanges_Object = MibTableColumn
wfIpxCircStateChanges = _WfIpxCircStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 32),
    _WfIpxCircStateChanges_Type()
)
wfIpxCircStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircStateChanges.setStatus("mandatory")
_WfIpxCircInitFails_Type = Counter32
_WfIpxCircInitFails_Object = MibTableColumn
wfIpxCircInitFails = _WfIpxCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 33),
    _WfIpxCircInitFails_Type()
)
wfIpxCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInitFails.setStatus("mandatory")
_WfIpxCircDelay_Type = Integer32
_WfIpxCircDelay_Object = MibTableColumn
wfIpxCircDelay = _WfIpxCircDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 34),
    _WfIpxCircDelay_Type()
)
wfIpxCircDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircDelay.setStatus("mandatory")
_WfIpxCircThroughput_Type = Integer32
_WfIpxCircThroughput_Object = MibTableColumn
wfIpxCircThroughput = _WfIpxCircThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 35),
    _WfIpxCircThroughput_Type()
)
wfIpxCircThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircThroughput.setStatus("mandatory")
_WfIpxCircNeighRouterName_Type = DisplayString
_WfIpxCircNeighRouterName_Object = MibTableColumn
wfIpxCircNeighRouterName = _WfIpxCircNeighRouterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 36),
    _WfIpxCircNeighRouterName_Type()
)
wfIpxCircNeighRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircNeighRouterName.setStatus("mandatory")
_WfIpxCircNeighInternalNetNum_Type = OctetString
_WfIpxCircNeighInternalNetNum_Object = MibTableColumn
wfIpxCircNeighInternalNetNum = _WfIpxCircNeighInternalNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 37),
    _WfIpxCircNeighInternalNetNum_Type()
)
wfIpxCircNeighInternalNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircNeighInternalNetNum.setStatus("mandatory")


class _WfIpxCircCost_Type(Integer32):
    """Custom type wfIpxCircCost based on Integer32"""
    defaultValue = 0


_WfIpxCircCost_Object = MibTableColumn
wfIpxCircCost = _WfIpxCircCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 38),
    _WfIpxCircCost_Type()
)
wfIpxCircCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCost.setStatus("mandatory")


class _WfIpxCircChecksum_Type(Integer32):
    """Custom type wfIpxCircChecksum based on Integer32"""
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


_WfIpxCircChecksum_Type.__name__ = "Integer32"
_WfIpxCircChecksum_Object = MibTableColumn
wfIpxCircChecksum = _WfIpxCircChecksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 39),
    _WfIpxCircChecksum_Type()
)
wfIpxCircChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircChecksum.setStatus("mandatory")


class _WfIpxCircCfgEncaps_Type(Integer32):
    """Custom type wfIpxCircCfgEncaps based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("ppp", 5),
          ("snap", 4))
    )


_WfIpxCircCfgEncaps_Type.__name__ = "Integer32"
_WfIpxCircCfgEncaps_Object = MibTableColumn
wfIpxCircCfgEncaps = _WfIpxCircCfgEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 40),
    _WfIpxCircCfgEncaps_Type()
)
wfIpxCircCfgEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgEncaps.setStatus("mandatory")


class _WfIpxCircEncaps_Type(Integer32):
    """Custom type wfIpxCircEncaps based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("ppp", 5),
          ("snap", 4))
    )


_WfIpxCircEncaps_Type.__name__ = "Integer32"
_WfIpxCircEncaps_Object = MibTableColumn
wfIpxCircEncaps = _WfIpxCircEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 41),
    _WfIpxCircEncaps_Type()
)
wfIpxCircEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircEncaps.setStatus("mandatory")
_WfIpxCircInTooManyHops_Type = Counter32
_WfIpxCircInTooManyHops_Object = MibTableColumn
wfIpxCircInTooManyHops = _WfIpxCircInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 42),
    _WfIpxCircInTooManyHops_Type()
)
wfIpxCircInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInTooManyHops.setStatus("mandatory")
_WfIpxCircInFiltered_Type = Counter32
_WfIpxCircInFiltered_Object = MibTableColumn
wfIpxCircInFiltered = _WfIpxCircInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 43),
    _WfIpxCircInFiltered_Type()
)
wfIpxCircInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInFiltered.setStatus("mandatory")
_WfIpxCircInHdrErrors_Type = Counter32
_WfIpxCircInHdrErrors_Object = MibTableColumn
wfIpxCircInHdrErrors = _WfIpxCircInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 44),
    _WfIpxCircInHdrErrors_Type()
)
wfIpxCircInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInHdrErrors.setStatus("mandatory")
_WfIpxCircInUnknownSockets_Type = Counter32
_WfIpxCircInUnknownSockets_Object = MibTableColumn
wfIpxCircInUnknownSockets = _WfIpxCircInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 45),
    _WfIpxCircInUnknownSockets_Type()
)
wfIpxCircInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInUnknownSockets.setStatus("mandatory")
_WfIpxCircNETBIOSPackets_Type = Counter32
_WfIpxCircNETBIOSPackets_Object = MibTableColumn
wfIpxCircNETBIOSPackets = _WfIpxCircNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 46),
    _WfIpxCircNETBIOSPackets_Type()
)
wfIpxCircNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircNETBIOSPackets.setStatus("mandatory")
_WfIpxCircInBadChecksums_Type = Counter32
_WfIpxCircInBadChecksums_Object = MibTableColumn
wfIpxCircInBadChecksums = _WfIpxCircInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 47),
    _WfIpxCircInBadChecksums_Type()
)
wfIpxCircInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInBadChecksums.setStatus("mandatory")
_WfIpxCircInDelivers_Type = Counter32
_WfIpxCircInDelivers_Object = MibTableColumn
wfIpxCircInDelivers = _WfIpxCircInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 48),
    _WfIpxCircInDelivers_Type()
)
wfIpxCircInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInDelivers.setStatus("mandatory")
_WfIpxCircInDiscards_Type = Counter32
_WfIpxCircInDiscards_Object = MibTableColumn
wfIpxCircInDiscards = _WfIpxCircInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 49),
    _WfIpxCircInDiscards_Type()
)
wfIpxCircInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircInDiscards.setStatus("mandatory")
_WfIpxCircNoRoutes_Type = Counter32
_WfIpxCircNoRoutes_Object = MibTableColumn
wfIpxCircNoRoutes = _WfIpxCircNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 50),
    _WfIpxCircNoRoutes_Type()
)
wfIpxCircNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircNoRoutes.setStatus("mandatory")
_WfIpxCircOutRequests_Type = Counter32
_WfIpxCircOutRequests_Object = MibTableColumn
wfIpxCircOutRequests = _WfIpxCircOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 51),
    _WfIpxCircOutRequests_Type()
)
wfIpxCircOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircOutRequests.setStatus("mandatory")
_WfIpxCircOutMalformedRequests_Type = Counter32
_WfIpxCircOutMalformedRequests_Object = MibTableColumn
wfIpxCircOutMalformedRequests = _WfIpxCircOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 52),
    _WfIpxCircOutMalformedRequests_Type()
)
wfIpxCircOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircOutMalformedRequests.setStatus("mandatory")
_WfIpxCircOutDiscards_Type = Counter32
_WfIpxCircOutDiscards_Object = MibTableColumn
wfIpxCircOutDiscards = _WfIpxCircOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 53),
    _WfIpxCircOutDiscards_Type()
)
wfIpxCircOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircOutDiscards.setStatus("mandatory")
_WfIpxCircOutFiltered_Type = Counter32
_WfIpxCircOutFiltered_Object = MibTableColumn
wfIpxCircOutFiltered = _WfIpxCircOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 54),
    _WfIpxCircOutFiltered_Type()
)
wfIpxCircOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircOutFiltered.setStatus("mandatory")
_WfIpxCircDestCount_Type = Counter32
_WfIpxCircDestCount_Object = MibTableColumn
wfIpxCircDestCount = _WfIpxCircDestCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 55),
    _WfIpxCircDestCount_Type()
)
wfIpxCircDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircDestCount.setStatus("mandatory")
_WfIpxCircServCount_Type = Counter32
_WfIpxCircServCount_Object = MibTableColumn
wfIpxCircServCount = _WfIpxCircServCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 56),
    _WfIpxCircServCount_Type()
)
wfIpxCircServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircServCount.setStatus("mandatory")
_WfIpxCircHostCount_Type = Counter32
_WfIpxCircHostCount_Object = MibTableColumn
wfIpxCircHostCount = _WfIpxCircHostCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 57),
    _WfIpxCircHostCount_Type()
)
wfIpxCircHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircHostCount.setStatus("mandatory")
_WfIpxCircForwardCount_Type = Counter32
_WfIpxCircForwardCount_Object = MibTableColumn
wfIpxCircForwardCount = _WfIpxCircForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 58),
    _WfIpxCircForwardCount_Type()
)
wfIpxCircForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircForwardCount.setStatus("mandatory")


class _WfIpxCircTrEndStation_Type(Integer32):
    """Custom type wfIpxCircTrEndStation based on Integer32"""
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


_WfIpxCircTrEndStation_Type.__name__ = "Integer32"
_WfIpxCircTrEndStation_Object = MibTableColumn
wfIpxCircTrEndStation = _WfIpxCircTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 59),
    _WfIpxCircTrEndStation_Type()
)
wfIpxCircTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircTrEndStation.setStatus("mandatory")


class _WfIpxCircNetbiosAccept_Type(Integer32):
    """Custom type wfIpxCircNetbiosAccept based on Integer32"""
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


_WfIpxCircNetbiosAccept_Type.__name__ = "Integer32"
_WfIpxCircNetbiosAccept_Object = MibTableColumn
wfIpxCircNetbiosAccept = _WfIpxCircNetbiosAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 60),
    _WfIpxCircNetbiosAccept_Type()
)
wfIpxCircNetbiosAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircNetbiosAccept.setStatus("mandatory")


class _WfIpxCircNetbiosDeliver_Type(Integer32):
    """Custom type wfIpxCircNetbiosDeliver based on Integer32"""
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


_WfIpxCircNetbiosDeliver_Type.__name__ = "Integer32"
_WfIpxCircNetbiosDeliver_Object = MibTableColumn
wfIpxCircNetbiosDeliver = _WfIpxCircNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 61),
    _WfIpxCircNetbiosDeliver_Type()
)
wfIpxCircNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircNetbiosDeliver.setStatus("mandatory")
_WfIpxCircSMDSIndividualAddress_Type = OctetString
_WfIpxCircSMDSIndividualAddress_Object = MibTableColumn
wfIpxCircSMDSIndividualAddress = _WfIpxCircSMDSIndividualAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 62),
    _WfIpxCircSMDSIndividualAddress_Type()
)
wfIpxCircSMDSIndividualAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircSMDSIndividualAddress.setStatus("mandatory")


class _WfIpxCircType_Type(Integer32):
    """Custom type wfIpxCircType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("dynamic", 6),
          ("nlsp", 8),
          ("other", 1),
          ("pt", 3),
          ("unnumberedrip", 5),
          ("wanrip", 4),
          ("ws", 7))
    )


_WfIpxCircType_Type.__name__ = "Integer32"
_WfIpxCircType_Object = MibTableColumn
wfIpxCircType = _WfIpxCircType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 63),
    _WfIpxCircType_Type()
)
wfIpxCircType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircType.setStatus("mandatory")


class _WfIpxCircWatchdogSpoof_Type(Integer32):
    """Custom type wfIpxCircWatchdogSpoof based on Integer32"""
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


_WfIpxCircWatchdogSpoof_Type.__name__ = "Integer32"
_WfIpxCircWatchdogSpoof_Object = MibTableColumn
wfIpxCircWatchdogSpoof = _WfIpxCircWatchdogSpoof_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 64),
    _WfIpxCircWatchdogSpoof_Type()
)
wfIpxCircWatchdogSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircWatchdogSpoof.setStatus("mandatory")
_WfIpxCircIPXOutWatchdogSpoofRsps_Type = Counter32
_WfIpxCircIPXOutWatchdogSpoofRsps_Object = MibTableColumn
wfIpxCircIPXOutWatchdogSpoofRsps = _WfIpxCircIPXOutWatchdogSpoofRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 65),
    _WfIpxCircIPXOutWatchdogSpoofRsps_Type()
)
wfIpxCircIPXOutWatchdogSpoofRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircIPXOutWatchdogSpoofRsps.setStatus("mandatory")
_WfIpxCircCfgDelay_Type = Integer32
_WfIpxCircCfgDelay_Object = MibTableColumn
wfIpxCircCfgDelay = _WfIpxCircCfgDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 66),
    _WfIpxCircCfgDelay_Type()
)
wfIpxCircCfgDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgDelay.setStatus("mandatory")
_WfIpxCircCfgThroughput_Type = Integer32
_WfIpxCircCfgThroughput_Object = MibTableColumn
wfIpxCircCfgThroughput = _WfIpxCircCfgThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 67),
    _WfIpxCircCfgThroughput_Type()
)
wfIpxCircCfgThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircCfgThroughput.setStatus("mandatory")
_WfIpxCircSPXOutWatchdogSpoofRsps_Type = Counter32
_WfIpxCircSPXOutWatchdogSpoofRsps_Object = MibTableColumn
wfIpxCircSPXOutWatchdogSpoofRsps = _WfIpxCircSPXOutWatchdogSpoofRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 68),
    _WfIpxCircSPXOutWatchdogSpoofRsps_Type()
)
wfIpxCircSPXOutWatchdogSpoofRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircSPXOutWatchdogSpoofRsps.setStatus("mandatory")


class _WfIpxCircInitStabilizationTimer_Type(Integer32):
    """Custom type wfIpxCircInitStabilizationTimer based on Integer32"""
    defaultValue = 0


_WfIpxCircInitStabilizationTimer_Object = MibTableColumn
wfIpxCircInitStabilizationTimer = _WfIpxCircInitStabilizationTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 69),
    _WfIpxCircInitStabilizationTimer_Type()
)
wfIpxCircInitStabilizationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircInitStabilizationTimer.setStatus("mandatory")


class _WfIpxCircSVCBroadcast_Type(Integer32):
    """Custom type wfIpxCircSVCBroadcast based on Integer32"""
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


_WfIpxCircSVCBroadcast_Type.__name__ = "Integer32"
_WfIpxCircSVCBroadcast_Object = MibTableColumn
wfIpxCircSVCBroadcast = _WfIpxCircSVCBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 70),
    _WfIpxCircSVCBroadcast_Type()
)
wfIpxCircSVCBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxCircSVCBroadcast.setStatus("mandatory")


class _WfIpxCircVRRPTriggerState_Type(Integer32):
    """Custom type wfIpxCircVRRPTriggerState based on Integer32"""
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


_WfIpxCircVRRPTriggerState_Type.__name__ = "Integer32"
_WfIpxCircVRRPTriggerState_Object = MibTableColumn
wfIpxCircVRRPTriggerState = _WfIpxCircVRRPTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 17, 1, 71),
    _WfIpxCircVRRPTriggerState_Type()
)
wfIpxCircVRRPTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxCircVRRPTriggerState.setStatus("mandatory")
_WfIpxDestEntryTable_Object = MibTable
wfIpxDestEntryTable = _WfIpxDestEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18)
)
if mibBuilder.loadTexts:
    wfIpxDestEntryTable.setStatus("mandatory")
_WfIpxDestEntry_Object = MibTableRow
wfIpxDestEntry = _WfIpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1)
)
wfIpxDestEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxDestSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxDestNetNum"),
)
if mibBuilder.loadTexts:
    wfIpxDestEntry.setStatus("mandatory")
_WfIpxDestSysInstance_Type = Integer32
_WfIpxDestSysInstance_Object = MibTableColumn
wfIpxDestSysInstance = _WfIpxDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 1),
    _WfIpxDestSysInstance_Type()
)
wfIpxDestSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestSysInstance.setStatus("mandatory")


class _WfIpxDestNetNum_Type(OctetString):
    """Custom type wfIpxDestNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxDestNetNum_Type.__name__ = "OctetString"
_WfIpxDestNetNum_Object = MibTableColumn
wfIpxDestNetNum = _WfIpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 2),
    _WfIpxDestNetNum_Type()
)
wfIpxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestNetNum.setStatus("mandatory")


class _WfIpxDestProtocol_Type(Integer32):
    """Custom type wfIpxDestProtocol based on Integer32"""
    defaultValue = 1

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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_WfIpxDestProtocol_Type.__name__ = "Integer32"
_WfIpxDestProtocol_Object = MibTableColumn
wfIpxDestProtocol = _WfIpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 3),
    _WfIpxDestProtocol_Type()
)
wfIpxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestProtocol.setStatus("mandatory")
_WfIpxDestTicks_Type = Integer32
_WfIpxDestTicks_Object = MibTableColumn
wfIpxDestTicks = _WfIpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 4),
    _WfIpxDestTicks_Type()
)
wfIpxDestTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestTicks.setStatus("mandatory")
_WfIpxDestHopCount_Type = Integer32
_WfIpxDestHopCount_Object = MibTableColumn
wfIpxDestHopCount = _WfIpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 5),
    _WfIpxDestHopCount_Type()
)
wfIpxDestHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestHopCount.setStatus("mandatory")
_WfIpxDestNextHopCircIndex_Type = Integer32
_WfIpxDestNextHopCircIndex_Object = MibTableColumn
wfIpxDestNextHopCircIndex = _WfIpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 6),
    _WfIpxDestNextHopCircIndex_Type()
)
wfIpxDestNextHopCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestNextHopCircIndex.setStatus("mandatory")
_WfIpxDestNextHopHostAddress_Type = OctetString
_WfIpxDestNextHopHostAddress_Object = MibTableColumn
wfIpxDestNextHopHostAddress = _WfIpxDestNextHopHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 7),
    _WfIpxDestNextHopHostAddress_Type()
)
wfIpxDestNextHopHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestNextHopHostAddress.setStatus("mandatory")
_WfIpxDestNextHopNetNum_Type = OctetString
_WfIpxDestNextHopNetNum_Object = MibTableColumn
wfIpxDestNextHopNetNum = _WfIpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 8),
    _WfIpxDestNextHopNetNum_Type()
)
wfIpxDestNextHopNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestNextHopNetNum.setStatus("mandatory")
_WfIpxDestAge_Type = Integer32
_WfIpxDestAge_Object = MibTableColumn
wfIpxDestAge = _WfIpxDestAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 18, 1, 9),
    _WfIpxDestAge_Type()
)
wfIpxDestAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxDestAge.setStatus("mandatory")
_WfIpxUserStaticRouteEntryTable_Object = MibTable
wfIpxUserStaticRouteEntryTable = _WfIpxUserStaticRouteEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19)
)
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteEntryTable.setStatus("mandatory")
_WfIpxUserStaticRouteEntry_Object = MibTableRow
wfIpxUserStaticRouteEntry = _WfIpxUserStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1)
)
wfIpxUserStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticRouteSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticRouteCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteEntry.setStatus("mandatory")


class _WfIpxUserStaticRouteDelete_Type(Integer32):
    """Custom type wfIpxUserStaticRouteDelete based on Integer32"""
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


_WfIpxUserStaticRouteDelete_Type.__name__ = "Integer32"
_WfIpxUserStaticRouteDelete_Object = MibTableColumn
wfIpxUserStaticRouteDelete = _WfIpxUserStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 1),
    _WfIpxUserStaticRouteDelete_Type()
)
wfIpxUserStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteDelete.setStatus("mandatory")


class _WfIpxUserStaticRouteDisable_Type(Integer32):
    """Custom type wfIpxUserStaticRouteDisable based on Integer32"""
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


_WfIpxUserStaticRouteDisable_Type.__name__ = "Integer32"
_WfIpxUserStaticRouteDisable_Object = MibTableColumn
wfIpxUserStaticRouteDisable = _WfIpxUserStaticRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 2),
    _WfIpxUserStaticRouteDisable_Type()
)
wfIpxUserStaticRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteDisable.setStatus("mandatory")
_WfIpxUserStaticRouteSysInstance_Type = Integer32
_WfIpxUserStaticRouteSysInstance_Object = MibTableColumn
wfIpxUserStaticRouteSysInstance = _WfIpxUserStaticRouteSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 3),
    _WfIpxUserStaticRouteSysInstance_Type()
)
wfIpxUserStaticRouteSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteSysInstance.setStatus("mandatory")
_WfIpxUserStaticRouteCircIndex_Type = Integer32
_WfIpxUserStaticRouteCircIndex_Object = MibTableColumn
wfIpxUserStaticRouteCircIndex = _WfIpxUserStaticRouteCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 4),
    _WfIpxUserStaticRouteCircIndex_Type()
)
wfIpxUserStaticRouteCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteCircIndex.setStatus("mandatory")


class _WfIpxUserStaticRouteNetNum_Type(OctetString):
    """Custom type wfIpxUserStaticRouteNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxUserStaticRouteNetNum_Type.__name__ = "OctetString"
_WfIpxUserStaticRouteNetNum_Object = MibTableColumn
wfIpxUserStaticRouteNetNum = _WfIpxUserStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 5),
    _WfIpxUserStaticRouteNetNum_Type()
)
wfIpxUserStaticRouteNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteNetNum.setStatus("mandatory")
_WfIpxUserStaticRouteTicks_Type = Integer32
_WfIpxUserStaticRouteTicks_Object = MibTableColumn
wfIpxUserStaticRouteTicks = _WfIpxUserStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 6),
    _WfIpxUserStaticRouteTicks_Type()
)
wfIpxUserStaticRouteTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteTicks.setStatus("mandatory")
_WfIpxUserStaticRouteHopCount_Type = Integer32
_WfIpxUserStaticRouteHopCount_Object = MibTableColumn
wfIpxUserStaticRouteHopCount = _WfIpxUserStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 7),
    _WfIpxUserStaticRouteHopCount_Type()
)
wfIpxUserStaticRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteHopCount.setStatus("mandatory")
_WfIpxUserStaticRouteNextHopHostAddress_Type = OctetString
_WfIpxUserStaticRouteNextHopHostAddress_Object = MibTableColumn
wfIpxUserStaticRouteNextHopHostAddress = _WfIpxUserStaticRouteNextHopHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 19, 1, 8),
    _WfIpxUserStaticRouteNextHopHostAddress_Type()
)
wfIpxUserStaticRouteNextHopHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticRouteNextHopHostAddress.setStatus("mandatory")
_WfIpxAutoStaticRouteEntryTable_Object = MibTable
wfIpxAutoStaticRouteEntryTable = _WfIpxAutoStaticRouteEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20)
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteEntryTable.setStatus("mandatory")
_WfIpxAutoStaticRouteEntry_Object = MibTableRow
wfIpxAutoStaticRouteEntry = _WfIpxAutoStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1)
)
wfIpxAutoStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticRouteSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticRouteCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteEntry.setStatus("mandatory")


class _WfIpxAutoStaticRouteDelete_Type(Integer32):
    """Custom type wfIpxAutoStaticRouteDelete based on Integer32"""
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


_WfIpxAutoStaticRouteDelete_Type.__name__ = "Integer32"
_WfIpxAutoStaticRouteDelete_Object = MibTableColumn
wfIpxAutoStaticRouteDelete = _WfIpxAutoStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 1),
    _WfIpxAutoStaticRouteDelete_Type()
)
wfIpxAutoStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteDelete.setStatus("mandatory")


class _WfIpxAutoStaticRouteDisable_Type(Integer32):
    """Custom type wfIpxAutoStaticRouteDisable based on Integer32"""
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


_WfIpxAutoStaticRouteDisable_Type.__name__ = "Integer32"
_WfIpxAutoStaticRouteDisable_Object = MibTableColumn
wfIpxAutoStaticRouteDisable = _WfIpxAutoStaticRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 2),
    _WfIpxAutoStaticRouteDisable_Type()
)
wfIpxAutoStaticRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteDisable.setStatus("mandatory")
_WfIpxAutoStaticRouteSysInstance_Type = Integer32
_WfIpxAutoStaticRouteSysInstance_Object = MibTableColumn
wfIpxAutoStaticRouteSysInstance = _WfIpxAutoStaticRouteSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 3),
    _WfIpxAutoStaticRouteSysInstance_Type()
)
wfIpxAutoStaticRouteSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteSysInstance.setStatus("mandatory")
_WfIpxAutoStaticRouteCircIndex_Type = Integer32
_WfIpxAutoStaticRouteCircIndex_Object = MibTableColumn
wfIpxAutoStaticRouteCircIndex = _WfIpxAutoStaticRouteCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 4),
    _WfIpxAutoStaticRouteCircIndex_Type()
)
wfIpxAutoStaticRouteCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteCircIndex.setStatus("mandatory")


class _WfIpxAutoStaticRouteNetNum_Type(OctetString):
    """Custom type wfIpxAutoStaticRouteNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxAutoStaticRouteNetNum_Type.__name__ = "OctetString"
_WfIpxAutoStaticRouteNetNum_Object = MibTableColumn
wfIpxAutoStaticRouteNetNum = _WfIpxAutoStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 5),
    _WfIpxAutoStaticRouteNetNum_Type()
)
wfIpxAutoStaticRouteNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteNetNum.setStatus("mandatory")
_WfIpxAutoStaticRouteTicks_Type = Integer32
_WfIpxAutoStaticRouteTicks_Object = MibTableColumn
wfIpxAutoStaticRouteTicks = _WfIpxAutoStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 6),
    _WfIpxAutoStaticRouteTicks_Type()
)
wfIpxAutoStaticRouteTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteTicks.setStatus("mandatory")
_WfIpxAutoStaticRouteHopCount_Type = Integer32
_WfIpxAutoStaticRouteHopCount_Object = MibTableColumn
wfIpxAutoStaticRouteHopCount = _WfIpxAutoStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 7),
    _WfIpxAutoStaticRouteHopCount_Type()
)
wfIpxAutoStaticRouteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteHopCount.setStatus("mandatory")
_WfIpxAutoStaticRouteNextHopHostAddress_Type = OctetString
_WfIpxAutoStaticRouteNextHopHostAddress_Object = MibTableColumn
wfIpxAutoStaticRouteNextHopHostAddress = _WfIpxAutoStaticRouteNextHopHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 20, 1, 8),
    _WfIpxAutoStaticRouteNextHopHostAddress_Type()
)
wfIpxAutoStaticRouteNextHopHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticRouteNextHopHostAddress.setStatus("mandatory")
_WfIpxStaticRouteMaskEntryTable_Object = MibTable
wfIpxStaticRouteMaskEntryTable = _WfIpxStaticRouteMaskEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21)
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskEntryTable.setStatus("mandatory")
_WfIpxStaticRouteMaskEntry_Object = MibTableRow
wfIpxStaticRouteMaskEntry = _WfIpxStaticRouteMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1)
)
wfIpxStaticRouteMaskEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticRouteMaskSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticRouteMaskCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticRouteMaskNetwork"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticRouteMaskNetworkMask"),
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskEntry.setStatus("mandatory")


class _WfIpxStaticRouteMaskDelete_Type(Integer32):
    """Custom type wfIpxStaticRouteMaskDelete based on Integer32"""
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


_WfIpxStaticRouteMaskDelete_Type.__name__ = "Integer32"
_WfIpxStaticRouteMaskDelete_Object = MibTableColumn
wfIpxStaticRouteMaskDelete = _WfIpxStaticRouteMaskDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 1),
    _WfIpxStaticRouteMaskDelete_Type()
)
wfIpxStaticRouteMaskDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskDelete.setStatus("mandatory")


class _WfIpxStaticRouteMaskDisable_Type(Integer32):
    """Custom type wfIpxStaticRouteMaskDisable based on Integer32"""
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


_WfIpxStaticRouteMaskDisable_Type.__name__ = "Integer32"
_WfIpxStaticRouteMaskDisable_Object = MibTableColumn
wfIpxStaticRouteMaskDisable = _WfIpxStaticRouteMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 2),
    _WfIpxStaticRouteMaskDisable_Type()
)
wfIpxStaticRouteMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskDisable.setStatus("mandatory")
_WfIpxStaticRouteMaskSysInstance_Type = Integer32
_WfIpxStaticRouteMaskSysInstance_Object = MibTableColumn
wfIpxStaticRouteMaskSysInstance = _WfIpxStaticRouteMaskSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 3),
    _WfIpxStaticRouteMaskSysInstance_Type()
)
wfIpxStaticRouteMaskSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskSysInstance.setStatus("mandatory")
_WfIpxStaticRouteMaskCircIndex_Type = Integer32
_WfIpxStaticRouteMaskCircIndex_Object = MibTableColumn
wfIpxStaticRouteMaskCircIndex = _WfIpxStaticRouteMaskCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 4),
    _WfIpxStaticRouteMaskCircIndex_Type()
)
wfIpxStaticRouteMaskCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskCircIndex.setStatus("mandatory")


class _WfIpxStaticRouteMaskNetwork_Type(OctetString):
    """Custom type wfIpxStaticRouteMaskNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticRouteMaskNetwork_Type.__name__ = "OctetString"
_WfIpxStaticRouteMaskNetwork_Object = MibTableColumn
wfIpxStaticRouteMaskNetwork = _WfIpxStaticRouteMaskNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 5),
    _WfIpxStaticRouteMaskNetwork_Type()
)
wfIpxStaticRouteMaskNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskNetwork.setStatus("mandatory")


class _WfIpxStaticRouteMaskNetworkMask_Type(OctetString):
    """Custom type wfIpxStaticRouteMaskNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticRouteMaskNetworkMask_Type.__name__ = "OctetString"
_WfIpxStaticRouteMaskNetworkMask_Object = MibTableColumn
wfIpxStaticRouteMaskNetworkMask = _WfIpxStaticRouteMaskNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 21, 1, 6),
    _WfIpxStaticRouteMaskNetworkMask_Type()
)
wfIpxStaticRouteMaskNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticRouteMaskNetworkMask.setStatus("mandatory")
_WfIpxServEntryTable_Object = MibTable
wfIpxServEntryTable = _WfIpxServEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22)
)
if mibBuilder.loadTexts:
    wfIpxServEntryTable.setStatus("mandatory")
_WfIpxServEntry_Object = MibTableRow
wfIpxServEntry = _WfIpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1)
)
wfIpxServEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxServSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServType"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServName"),
)
if mibBuilder.loadTexts:
    wfIpxServEntry.setStatus("mandatory")
_WfIpxServSysInstance_Type = Integer32
_WfIpxServSysInstance_Object = MibTableColumn
wfIpxServSysInstance = _WfIpxServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 1),
    _WfIpxServSysInstance_Type()
)
wfIpxServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServSysInstance.setStatus("mandatory")


class _WfIpxServType_Type(OctetString):
    """Custom type wfIpxServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WfIpxServType_Type.__name__ = "OctetString"
_WfIpxServType_Object = MibTableColumn
wfIpxServType = _WfIpxServType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 2),
    _WfIpxServType_Type()
)
wfIpxServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServType.setStatus("mandatory")
_WfIpxServName_Type = DisplayString
_WfIpxServName_Object = MibTableColumn
wfIpxServName = _WfIpxServName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 3),
    _WfIpxServName_Type()
)
wfIpxServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServName.setStatus("mandatory")


class _WfIpxServProtocol_Type(Integer32):
    """Custom type wfIpxServProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_WfIpxServProtocol_Type.__name__ = "Integer32"
_WfIpxServProtocol_Object = MibTableColumn
wfIpxServProtocol = _WfIpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 4),
    _WfIpxServProtocol_Type()
)
wfIpxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServProtocol.setStatus("mandatory")
_WfIpxServNetNum_Type = OctetString
_WfIpxServNetNum_Object = MibTableColumn
wfIpxServNetNum = _WfIpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 5),
    _WfIpxServNetNum_Type()
)
wfIpxServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNetNum.setStatus("mandatory")
_WfIpxServNode_Type = OctetString
_WfIpxServNode_Object = MibTableColumn
wfIpxServNode = _WfIpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 6),
    _WfIpxServNode_Type()
)
wfIpxServNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNode.setStatus("mandatory")
_WfIpxServSocket_Type = OctetString
_WfIpxServSocket_Object = MibTableColumn
wfIpxServSocket = _WfIpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 7),
    _WfIpxServSocket_Type()
)
wfIpxServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServSocket.setStatus("mandatory")
_WfIpxServHopCount_Type = Integer32
_WfIpxServHopCount_Object = MibTableColumn
wfIpxServHopCount = _WfIpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 8),
    _WfIpxServHopCount_Type()
)
wfIpxServHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServHopCount.setStatus("mandatory")
_WfIpxServNextHopCircIndex_Type = Integer32
_WfIpxServNextHopCircIndex_Object = MibTableColumn
wfIpxServNextHopCircIndex = _WfIpxServNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 9),
    _WfIpxServNextHopCircIndex_Type()
)
wfIpxServNextHopCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNextHopCircIndex.setStatus("mandatory")
_WfIpxServNextHopHostAddress_Type = OctetString
_WfIpxServNextHopHostAddress_Object = MibTableColumn
wfIpxServNextHopHostAddress = _WfIpxServNextHopHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 10),
    _WfIpxServNextHopHostAddress_Type()
)
wfIpxServNextHopHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNextHopHostAddress.setStatus("mandatory")
_WfIpxServNextHopNetNum_Type = OctetString
_WfIpxServNextHopNetNum_Object = MibTableColumn
wfIpxServNextHopNetNum = _WfIpxServNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 11),
    _WfIpxServNextHopNetNum_Type()
)
wfIpxServNextHopNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNextHopNetNum.setStatus("mandatory")
_WfIpxServAge_Type = Integer32
_WfIpxServAge_Object = MibTableColumn
wfIpxServAge = _WfIpxServAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 22, 1, 12),
    _WfIpxServAge_Type()
)
wfIpxServAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServAge.setStatus("mandatory")
_WfIpxUserStaticServEntryTable_Object = MibTable
wfIpxUserStaticServEntryTable = _WfIpxUserStaticServEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23)
)
if mibBuilder.loadTexts:
    wfIpxUserStaticServEntryTable.setStatus("mandatory")
_WfIpxUserStaticServEntry_Object = MibTableRow
wfIpxUserStaticServEntry = _WfIpxUserStaticServEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1)
)
wfIpxUserStaticServEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticServSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticServCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticServName"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticServType"),
)
if mibBuilder.loadTexts:
    wfIpxUserStaticServEntry.setStatus("mandatory")


class _WfIpxUserStaticServDelete_Type(Integer32):
    """Custom type wfIpxUserStaticServDelete based on Integer32"""
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


_WfIpxUserStaticServDelete_Type.__name__ = "Integer32"
_WfIpxUserStaticServDelete_Object = MibTableColumn
wfIpxUserStaticServDelete = _WfIpxUserStaticServDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 1),
    _WfIpxUserStaticServDelete_Type()
)
wfIpxUserStaticServDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServDelete.setStatus("mandatory")


class _WfIpxUserStaticServDisable_Type(Integer32):
    """Custom type wfIpxUserStaticServDisable based on Integer32"""
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


_WfIpxUserStaticServDisable_Type.__name__ = "Integer32"
_WfIpxUserStaticServDisable_Object = MibTableColumn
wfIpxUserStaticServDisable = _WfIpxUserStaticServDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 2),
    _WfIpxUserStaticServDisable_Type()
)
wfIpxUserStaticServDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServDisable.setStatus("mandatory")
_WfIpxUserStaticServSysInstance_Type = Integer32
_WfIpxUserStaticServSysInstance_Object = MibTableColumn
wfIpxUserStaticServSysInstance = _WfIpxUserStaticServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 3),
    _WfIpxUserStaticServSysInstance_Type()
)
wfIpxUserStaticServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticServSysInstance.setStatus("mandatory")
_WfIpxUserStaticServCircIndex_Type = Integer32
_WfIpxUserStaticServCircIndex_Object = MibTableColumn
wfIpxUserStaticServCircIndex = _WfIpxUserStaticServCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 4),
    _WfIpxUserStaticServCircIndex_Type()
)
wfIpxUserStaticServCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticServCircIndex.setStatus("mandatory")
_WfIpxUserStaticServName_Type = DisplayString
_WfIpxUserStaticServName_Object = MibTableColumn
wfIpxUserStaticServName = _WfIpxUserStaticServName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 5),
    _WfIpxUserStaticServName_Type()
)
wfIpxUserStaticServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticServName.setStatus("mandatory")


class _WfIpxUserStaticServType_Type(OctetString):
    """Custom type wfIpxUserStaticServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WfIpxUserStaticServType_Type.__name__ = "OctetString"
_WfIpxUserStaticServType_Object = MibTableColumn
wfIpxUserStaticServType = _WfIpxUserStaticServType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 6),
    _WfIpxUserStaticServType_Type()
)
wfIpxUserStaticServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticServType.setStatus("mandatory")
_WfIpxUserStaticServNetNum_Type = OctetString
_WfIpxUserStaticServNetNum_Object = MibTableColumn
wfIpxUserStaticServNetNum = _WfIpxUserStaticServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 7),
    _WfIpxUserStaticServNetNum_Type()
)
wfIpxUserStaticServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServNetNum.setStatus("mandatory")
_WfIpxUserStaticServHostAddress_Type = OctetString
_WfIpxUserStaticServHostAddress_Object = MibTableColumn
wfIpxUserStaticServHostAddress = _WfIpxUserStaticServHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 8),
    _WfIpxUserStaticServHostAddress_Type()
)
wfIpxUserStaticServHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServHostAddress.setStatus("mandatory")
_WfIpxUserStaticServSocket_Type = OctetString
_WfIpxUserStaticServSocket_Object = MibTableColumn
wfIpxUserStaticServSocket = _WfIpxUserStaticServSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 9),
    _WfIpxUserStaticServSocket_Type()
)
wfIpxUserStaticServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServSocket.setStatus("mandatory")


class _WfIpxUserStaticServHopCount_Type(Integer32):
    """Custom type wfIpxUserStaticServHopCount based on Integer32"""
    defaultValue = 1


_WfIpxUserStaticServHopCount_Object = MibTableColumn
wfIpxUserStaticServHopCount = _WfIpxUserStaticServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 23, 1, 10),
    _WfIpxUserStaticServHopCount_Type()
)
wfIpxUserStaticServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticServHopCount.setStatus("mandatory")
_WfIpxAutoStaticServEntryTable_Object = MibTable
wfIpxAutoStaticServEntryTable = _WfIpxAutoStaticServEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24)
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticServEntryTable.setStatus("mandatory")
_WfIpxAutoStaticServEntry_Object = MibTableRow
wfIpxAutoStaticServEntry = _WfIpxAutoStaticServEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1)
)
wfIpxAutoStaticServEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticServSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticServCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticServName"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticServType"),
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticServEntry.setStatus("mandatory")


class _WfIpxAutoStaticServDelete_Type(Integer32):
    """Custom type wfIpxAutoStaticServDelete based on Integer32"""
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


_WfIpxAutoStaticServDelete_Type.__name__ = "Integer32"
_WfIpxAutoStaticServDelete_Object = MibTableColumn
wfIpxAutoStaticServDelete = _WfIpxAutoStaticServDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 1),
    _WfIpxAutoStaticServDelete_Type()
)
wfIpxAutoStaticServDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServDelete.setStatus("mandatory")


class _WfIpxAutoStaticServDisable_Type(Integer32):
    """Custom type wfIpxAutoStaticServDisable based on Integer32"""
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


_WfIpxAutoStaticServDisable_Type.__name__ = "Integer32"
_WfIpxAutoStaticServDisable_Object = MibTableColumn
wfIpxAutoStaticServDisable = _WfIpxAutoStaticServDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 2),
    _WfIpxAutoStaticServDisable_Type()
)
wfIpxAutoStaticServDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServDisable.setStatus("mandatory")
_WfIpxAutoStaticServSysInstance_Type = Integer32
_WfIpxAutoStaticServSysInstance_Object = MibTableColumn
wfIpxAutoStaticServSysInstance = _WfIpxAutoStaticServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 3),
    _WfIpxAutoStaticServSysInstance_Type()
)
wfIpxAutoStaticServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServSysInstance.setStatus("mandatory")
_WfIpxAutoStaticServCircIndex_Type = Integer32
_WfIpxAutoStaticServCircIndex_Object = MibTableColumn
wfIpxAutoStaticServCircIndex = _WfIpxAutoStaticServCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 4),
    _WfIpxAutoStaticServCircIndex_Type()
)
wfIpxAutoStaticServCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServCircIndex.setStatus("mandatory")
_WfIpxAutoStaticServName_Type = DisplayString
_WfIpxAutoStaticServName_Object = MibTableColumn
wfIpxAutoStaticServName = _WfIpxAutoStaticServName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 5),
    _WfIpxAutoStaticServName_Type()
)
wfIpxAutoStaticServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServName.setStatus("mandatory")
_WfIpxAutoStaticServType_Type = OctetString
_WfIpxAutoStaticServType_Object = MibTableColumn
wfIpxAutoStaticServType = _WfIpxAutoStaticServType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 6),
    _WfIpxAutoStaticServType_Type()
)
wfIpxAutoStaticServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServType.setStatus("mandatory")
_WfIpxAutoStaticServNetNum_Type = OctetString
_WfIpxAutoStaticServNetNum_Object = MibTableColumn
wfIpxAutoStaticServNetNum = _WfIpxAutoStaticServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 7),
    _WfIpxAutoStaticServNetNum_Type()
)
wfIpxAutoStaticServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServNetNum.setStatus("mandatory")
_WfIpxAutoStaticServHostAddress_Type = OctetString
_WfIpxAutoStaticServHostAddress_Object = MibTableColumn
wfIpxAutoStaticServHostAddress = _WfIpxAutoStaticServHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 8),
    _WfIpxAutoStaticServHostAddress_Type()
)
wfIpxAutoStaticServHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServHostAddress.setStatus("mandatory")
_WfIpxAutoStaticServSocket_Type = OctetString
_WfIpxAutoStaticServSocket_Object = MibTableColumn
wfIpxAutoStaticServSocket = _WfIpxAutoStaticServSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 9),
    _WfIpxAutoStaticServSocket_Type()
)
wfIpxAutoStaticServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServSocket.setStatus("mandatory")


class _WfIpxAutoStaticServHopCount_Type(Integer32):
    """Custom type wfIpxAutoStaticServHopCount based on Integer32"""
    defaultValue = 1


_WfIpxAutoStaticServHopCount_Object = MibTableColumn
wfIpxAutoStaticServHopCount = _WfIpxAutoStaticServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 24, 1, 10),
    _WfIpxAutoStaticServHopCount_Type()
)
wfIpxAutoStaticServHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticServHopCount.setStatus("mandatory")
_WfIpxStaticServMaskEntryTable_Object = MibTable
wfIpxStaticServMaskEntryTable = _WfIpxStaticServMaskEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25)
)
if mibBuilder.loadTexts:
    wfIpxStaticServMaskEntryTable.setStatus("mandatory")
_WfIpxStaticServMaskEntry_Object = MibTableRow
wfIpxStaticServMaskEntry = _WfIpxStaticServMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1)
)
wfIpxStaticServMaskEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticServMaskSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticServMaskCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticServMaskNetwork"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticServMaskNetworkMask"),
)
if mibBuilder.loadTexts:
    wfIpxStaticServMaskEntry.setStatus("mandatory")


class _WfIpxStaticServMaskDelete_Type(Integer32):
    """Custom type wfIpxStaticServMaskDelete based on Integer32"""
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


_WfIpxStaticServMaskDelete_Type.__name__ = "Integer32"
_WfIpxStaticServMaskDelete_Object = MibTableColumn
wfIpxStaticServMaskDelete = _WfIpxStaticServMaskDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 1),
    _WfIpxStaticServMaskDelete_Type()
)
wfIpxStaticServMaskDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskDelete.setStatus("mandatory")


class _WfIpxStaticServMaskDisable_Type(Integer32):
    """Custom type wfIpxStaticServMaskDisable based on Integer32"""
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


_WfIpxStaticServMaskDisable_Type.__name__ = "Integer32"
_WfIpxStaticServMaskDisable_Object = MibTableColumn
wfIpxStaticServMaskDisable = _WfIpxStaticServMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 2),
    _WfIpxStaticServMaskDisable_Type()
)
wfIpxStaticServMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskDisable.setStatus("mandatory")
_WfIpxStaticServMaskSysInstance_Type = Integer32
_WfIpxStaticServMaskSysInstance_Object = MibTableColumn
wfIpxStaticServMaskSysInstance = _WfIpxStaticServMaskSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 3),
    _WfIpxStaticServMaskSysInstance_Type()
)
wfIpxStaticServMaskSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskSysInstance.setStatus("mandatory")
_WfIpxStaticServMaskCircIndex_Type = Integer32
_WfIpxStaticServMaskCircIndex_Object = MibTableColumn
wfIpxStaticServMaskCircIndex = _WfIpxStaticServMaskCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 4),
    _WfIpxStaticServMaskCircIndex_Type()
)
wfIpxStaticServMaskCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskCircIndex.setStatus("mandatory")


class _WfIpxStaticServMaskNetwork_Type(OctetString):
    """Custom type wfIpxStaticServMaskNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticServMaskNetwork_Type.__name__ = "OctetString"
_WfIpxStaticServMaskNetwork_Object = MibTableColumn
wfIpxStaticServMaskNetwork = _WfIpxStaticServMaskNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 5),
    _WfIpxStaticServMaskNetwork_Type()
)
wfIpxStaticServMaskNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskNetwork.setStatus("mandatory")


class _WfIpxStaticServMaskNetworkMask_Type(OctetString):
    """Custom type wfIpxStaticServMaskNetworkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxStaticServMaskNetworkMask_Type.__name__ = "OctetString"
_WfIpxStaticServMaskNetworkMask_Object = MibTableColumn
wfIpxStaticServMaskNetworkMask = _WfIpxStaticServMaskNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 25, 1, 6),
    _WfIpxStaticServMaskNetworkMask_Type()
)
wfIpxStaticServMaskNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticServMaskNetworkMask.setStatus("mandatory")
_WfIpxStaticHostEntryTable_Object = MibTable
wfIpxStaticHostEntryTable = _WfIpxStaticHostEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26)
)
if mibBuilder.loadTexts:
    wfIpxStaticHostEntryTable.setStatus("mandatory")
_WfIpxStaticHostEntry_Object = MibTableRow
wfIpxStaticHostEntry = _WfIpxStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1)
)
wfIpxStaticHostEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticHostSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticHostCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxStaticHostAddress"),
)
if mibBuilder.loadTexts:
    wfIpxStaticHostEntry.setStatus("mandatory")


class _WfIpxStaticHostDelete_Type(Integer32):
    """Custom type wfIpxStaticHostDelete based on Integer32"""
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


_WfIpxStaticHostDelete_Type.__name__ = "Integer32"
_WfIpxStaticHostDelete_Object = MibTableColumn
wfIpxStaticHostDelete = _WfIpxStaticHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 1),
    _WfIpxStaticHostDelete_Type()
)
wfIpxStaticHostDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostDelete.setStatus("mandatory")


class _WfIpxStaticHostDisable_Type(Integer32):
    """Custom type wfIpxStaticHostDisable based on Integer32"""
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


_WfIpxStaticHostDisable_Type.__name__ = "Integer32"
_WfIpxStaticHostDisable_Object = MibTableColumn
wfIpxStaticHostDisable = _WfIpxStaticHostDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 2),
    _WfIpxStaticHostDisable_Type()
)
wfIpxStaticHostDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostDisable.setStatus("mandatory")
_WfIpxStaticHostSysInstance_Type = Integer32
_WfIpxStaticHostSysInstance_Object = MibTableColumn
wfIpxStaticHostSysInstance = _WfIpxStaticHostSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 3),
    _WfIpxStaticHostSysInstance_Type()
)
wfIpxStaticHostSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticHostSysInstance.setStatus("mandatory")
_WfIpxStaticHostCircIndex_Type = Integer32
_WfIpxStaticHostCircIndex_Object = MibTableColumn
wfIpxStaticHostCircIndex = _WfIpxStaticHostCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 4),
    _WfIpxStaticHostCircIndex_Type()
)
wfIpxStaticHostCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticHostCircIndex.setStatus("mandatory")


class _WfIpxStaticHostAddress_Type(OctetString):
    """Custom type wfIpxStaticHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfIpxStaticHostAddress_Type.__name__ = "OctetString"
_WfIpxStaticHostAddress_Object = MibTableColumn
wfIpxStaticHostAddress = _WfIpxStaticHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 5),
    _WfIpxStaticHostAddress_Type()
)
wfIpxStaticHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxStaticHostAddress.setStatus("mandatory")
_WfIpxStaticHostWanAddress_Type = OctetString
_WfIpxStaticHostWanAddress_Object = MibTableColumn
wfIpxStaticHostWanAddress = _WfIpxStaticHostWanAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 6),
    _WfIpxStaticHostWanAddress_Type()
)
wfIpxStaticHostWanAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostWanAddress.setStatus("mandatory")
_WfIpxStaticHostSubaddress_Type = DisplayString
_WfIpxStaticHostSubaddress_Object = MibTableColumn
wfIpxStaticHostSubaddress = _WfIpxStaticHostSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 7),
    _WfIpxStaticHostSubaddress_Type()
)
wfIpxStaticHostSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostSubaddress.setStatus("mandatory")


class _WfIpxStaticHostTypeOfNumber_Type(Integer32):
    """Custom type wfIpxStaticHostTypeOfNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("unknown", 1))
    )


_WfIpxStaticHostTypeOfNumber_Type.__name__ = "Integer32"
_WfIpxStaticHostTypeOfNumber_Object = MibTableColumn
wfIpxStaticHostTypeOfNumber = _WfIpxStaticHostTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 8),
    _WfIpxStaticHostTypeOfNumber_Type()
)
wfIpxStaticHostTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostTypeOfNumber.setStatus("mandatory")


class _WfIpxStaticHostType_Type(Integer32):
    """Custom type wfIpxStaticHostType based on Integer32"""
    defaultValue = 2

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
        *(("atmsvc", 6),
          ("default", 2),
          ("frdlci", 4),
          ("fre164", 1),
          ("frx121", 3),
          ("gre", 5))
    )


_WfIpxStaticHostType_Type.__name__ = "Integer32"
_WfIpxStaticHostType_Object = MibTableColumn
wfIpxStaticHostType = _WfIpxStaticHostType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 9),
    _WfIpxStaticHostType_Type()
)
wfIpxStaticHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostType.setStatus("mandatory")
_WfIpxStaticHostGreConnName_Type = DisplayString
_WfIpxStaticHostGreConnName_Object = MibTableColumn
wfIpxStaticHostGreConnName = _WfIpxStaticHostGreConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 26, 1, 10),
    _WfIpxStaticHostGreConnName_Type()
)
wfIpxStaticHostGreConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxStaticHostGreConnName.setStatus("mandatory")
_WfIpxUserStaticNETBIOSTable_Object = MibTable
wfIpxUserStaticNETBIOSTable = _WfIpxUserStaticNETBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27)
)
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSTable.setStatus("mandatory")
_WfIpxUserStaticNETBIOSEntry_Object = MibTableRow
wfIpxUserStaticNETBIOSEntry = _WfIpxUserStaticNETBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1)
)
wfIpxUserStaticNETBIOSEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticNETBIOSSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxUserStaticNETBIOSName"),
)
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSEntry.setStatus("mandatory")


class _WfIpxUserStaticNETBIOSDelete_Type(Integer32):
    """Custom type wfIpxUserStaticNETBIOSDelete based on Integer32"""
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


_WfIpxUserStaticNETBIOSDelete_Type.__name__ = "Integer32"
_WfIpxUserStaticNETBIOSDelete_Object = MibTableColumn
wfIpxUserStaticNETBIOSDelete = _WfIpxUserStaticNETBIOSDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1, 1),
    _WfIpxUserStaticNETBIOSDelete_Type()
)
wfIpxUserStaticNETBIOSDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSDelete.setStatus("mandatory")


class _WfIpxUserStaticNETBIOSDisable_Type(Integer32):
    """Custom type wfIpxUserStaticNETBIOSDisable based on Integer32"""
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


_WfIpxUserStaticNETBIOSDisable_Type.__name__ = "Integer32"
_WfIpxUserStaticNETBIOSDisable_Object = MibTableColumn
wfIpxUserStaticNETBIOSDisable = _WfIpxUserStaticNETBIOSDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1, 2),
    _WfIpxUserStaticNETBIOSDisable_Type()
)
wfIpxUserStaticNETBIOSDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSDisable.setStatus("mandatory")
_WfIpxUserStaticNETBIOSSysInstance_Type = Integer32
_WfIpxUserStaticNETBIOSSysInstance_Object = MibTableColumn
wfIpxUserStaticNETBIOSSysInstance = _WfIpxUserStaticNETBIOSSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1, 3),
    _WfIpxUserStaticNETBIOSSysInstance_Type()
)
wfIpxUserStaticNETBIOSSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSSysInstance.setStatus("mandatory")
_WfIpxUserStaticNETBIOSName_Type = DisplayString
_WfIpxUserStaticNETBIOSName_Object = MibTableColumn
wfIpxUserStaticNETBIOSName = _WfIpxUserStaticNETBIOSName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1, 4),
    _WfIpxUserStaticNETBIOSName_Type()
)
wfIpxUserStaticNETBIOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSName.setStatus("mandatory")
_WfIpxUserStaticNETBIOSDestNetwork_Type = OctetString
_WfIpxUserStaticNETBIOSDestNetwork_Object = MibTableColumn
wfIpxUserStaticNETBIOSDestNetwork = _WfIpxUserStaticNETBIOSDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 27, 1, 5),
    _WfIpxUserStaticNETBIOSDestNetwork_Type()
)
wfIpxUserStaticNETBIOSDestNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxUserStaticNETBIOSDestNetwork.setStatus("mandatory")
_WfIpxAutoStaticNETBIOSTable_Object = MibTable
wfIpxAutoStaticNETBIOSTable = _WfIpxAutoStaticNETBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28)
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSTable.setStatus("mandatory")
_WfIpxAutoStaticNETBIOSEntry_Object = MibTableRow
wfIpxAutoStaticNETBIOSEntry = _WfIpxAutoStaticNETBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1)
)
wfIpxAutoStaticNETBIOSEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticNETBIOSSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxAutoStaticNETBIOSDestNetwork"),
)
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSEntry.setStatus("mandatory")


class _WfIpxAutoStaticNETBIOSDelete_Type(Integer32):
    """Custom type wfIpxAutoStaticNETBIOSDelete based on Integer32"""
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


_WfIpxAutoStaticNETBIOSDelete_Type.__name__ = "Integer32"
_WfIpxAutoStaticNETBIOSDelete_Object = MibTableColumn
wfIpxAutoStaticNETBIOSDelete = _WfIpxAutoStaticNETBIOSDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1, 1),
    _WfIpxAutoStaticNETBIOSDelete_Type()
)
wfIpxAutoStaticNETBIOSDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSDelete.setStatus("mandatory")


class _WfIpxAutoStaticNETBIOSDisable_Type(Integer32):
    """Custom type wfIpxAutoStaticNETBIOSDisable based on Integer32"""
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


_WfIpxAutoStaticNETBIOSDisable_Type.__name__ = "Integer32"
_WfIpxAutoStaticNETBIOSDisable_Object = MibTableColumn
wfIpxAutoStaticNETBIOSDisable = _WfIpxAutoStaticNETBIOSDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1, 2),
    _WfIpxAutoStaticNETBIOSDisable_Type()
)
wfIpxAutoStaticNETBIOSDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSDisable.setStatus("mandatory")
_WfIpxAutoStaticNETBIOSSysInstance_Type = Integer32
_WfIpxAutoStaticNETBIOSSysInstance_Object = MibTableColumn
wfIpxAutoStaticNETBIOSSysInstance = _WfIpxAutoStaticNETBIOSSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1, 3),
    _WfIpxAutoStaticNETBIOSSysInstance_Type()
)
wfIpxAutoStaticNETBIOSSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSSysInstance.setStatus("mandatory")


class _WfIpxAutoStaticNETBIOSDestNetwork_Type(OctetString):
    """Custom type wfIpxAutoStaticNETBIOSDestNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxAutoStaticNETBIOSDestNetwork_Type.__name__ = "OctetString"
_WfIpxAutoStaticNETBIOSDestNetwork_Object = MibTableColumn
wfIpxAutoStaticNETBIOSDestNetwork = _WfIpxAutoStaticNETBIOSDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1, 4),
    _WfIpxAutoStaticNETBIOSDestNetwork_Type()
)
wfIpxAutoStaticNETBIOSDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSDestNetwork.setStatus("mandatory")
_WfIpxAutoStaticNETBIOSName_Type = DisplayString
_WfIpxAutoStaticNETBIOSName_Object = MibTableColumn
wfIpxAutoStaticNETBIOSName = _WfIpxAutoStaticNETBIOSName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 28, 1, 5),
    _WfIpxAutoStaticNETBIOSName_Type()
)
wfIpxAutoStaticNETBIOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAutoStaticNETBIOSName.setStatus("mandatory")
_WfIpxRouteFilterTable_Object = MibTable
wfIpxRouteFilterTable = _WfIpxRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29)
)
if mibBuilder.loadTexts:
    wfIpxRouteFilterTable.setStatus("mandatory")
_WfIpxRouteFilterEntry_Object = MibTableRow
wfIpxRouteFilterEntry = _WfIpxRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1)
)
wfIpxRouteFilterEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxRouteFilterSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxRouteFilterCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxRouteFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    wfIpxRouteFilterEntry.setStatus("mandatory")


class _WfIpxRouteFilterDelete_Type(Integer32):
    """Custom type wfIpxRouteFilterDelete based on Integer32"""
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


_WfIpxRouteFilterDelete_Type.__name__ = "Integer32"
_WfIpxRouteFilterDelete_Object = MibTableColumn
wfIpxRouteFilterDelete = _WfIpxRouteFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 1),
    _WfIpxRouteFilterDelete_Type()
)
wfIpxRouteFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterDelete.setStatus("mandatory")


class _WfIpxRouteFilterDisable_Type(Integer32):
    """Custom type wfIpxRouteFilterDisable based on Integer32"""
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


_WfIpxRouteFilterDisable_Type.__name__ = "Integer32"
_WfIpxRouteFilterDisable_Object = MibTableColumn
wfIpxRouteFilterDisable = _WfIpxRouteFilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 2),
    _WfIpxRouteFilterDisable_Type()
)
wfIpxRouteFilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterDisable.setStatus("mandatory")
_WfIpxRouteFilterSysInstance_Type = Integer32
_WfIpxRouteFilterSysInstance_Object = MibTableColumn
wfIpxRouteFilterSysInstance = _WfIpxRouteFilterSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 3),
    _WfIpxRouteFilterSysInstance_Type()
)
wfIpxRouteFilterSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRouteFilterSysInstance.setStatus("mandatory")
_WfIpxRouteFilterCircIndex_Type = Integer32
_WfIpxRouteFilterCircIndex_Object = MibTableColumn
wfIpxRouteFilterCircIndex = _WfIpxRouteFilterCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 4),
    _WfIpxRouteFilterCircIndex_Type()
)
wfIpxRouteFilterCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRouteFilterCircIndex.setStatus("mandatory")
_WfIpxRouteFilterRuleNumber_Type = Integer32
_WfIpxRouteFilterRuleNumber_Object = MibTableColumn
wfIpxRouteFilterRuleNumber = _WfIpxRouteFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 5),
    _WfIpxRouteFilterRuleNumber_Type()
)
wfIpxRouteFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRouteFilterRuleNumber.setStatus("mandatory")
_WfIpxRouteFilterNetwork_Type = OctetString
_WfIpxRouteFilterNetwork_Object = MibTableColumn
wfIpxRouteFilterNetwork = _WfIpxRouteFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 6),
    _WfIpxRouteFilterNetwork_Type()
)
wfIpxRouteFilterNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterNetwork.setStatus("mandatory")
_WfIpxRouteFilterNetworkMask_Type = OctetString
_WfIpxRouteFilterNetworkMask_Object = MibTableColumn
wfIpxRouteFilterNetworkMask = _WfIpxRouteFilterNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 7),
    _WfIpxRouteFilterNetworkMask_Type()
)
wfIpxRouteFilterNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterNetworkMask.setStatus("mandatory")


class _WfIpxRouteFilterMode_Type(Integer32):
    """Custom type wfIpxRouteFilterMode based on Integer32"""
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
        *(("both", 3),
          ("inbound", 2),
          ("outbound", 1))
    )


_WfIpxRouteFilterMode_Type.__name__ = "Integer32"
_WfIpxRouteFilterMode_Object = MibTableColumn
wfIpxRouteFilterMode = _WfIpxRouteFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 8),
    _WfIpxRouteFilterMode_Type()
)
wfIpxRouteFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterMode.setStatus("mandatory")


class _WfIpxRouteFilterAction_Type(Integer32):
    """Custom type wfIpxRouteFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("suppress", 2))
    )


_WfIpxRouteFilterAction_Type.__name__ = "Integer32"
_WfIpxRouteFilterAction_Object = MibTableColumn
wfIpxRouteFilterAction = _WfIpxRouteFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 9),
    _WfIpxRouteFilterAction_Type()
)
wfIpxRouteFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterAction.setStatus("mandatory")


class _WfIpxRouteFilterProtocol_Type(Integer32):
    """Custom type wfIpxRouteFilterProtocol based on Integer32"""
    defaultValue = 1

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
        *(("any", 1),
          ("local", 2),
          ("nlsp", 4),
          ("rip", 3),
          ("static", 5))
    )


_WfIpxRouteFilterProtocol_Type.__name__ = "Integer32"
_WfIpxRouteFilterProtocol_Object = MibTableColumn
wfIpxRouteFilterProtocol = _WfIpxRouteFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 10),
    _WfIpxRouteFilterProtocol_Type()
)
wfIpxRouteFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterProtocol.setStatus("mandatory")
_WfIpxRouteFilterCost_Type = Integer32
_WfIpxRouteFilterCost_Object = MibTableColumn
wfIpxRouteFilterCost = _WfIpxRouteFilterCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 11),
    _WfIpxRouteFilterCost_Type()
)
wfIpxRouteFilterCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterCost.setStatus("mandatory")
_WfIpxRouteFilterCounter_Type = Counter32
_WfIpxRouteFilterCounter_Object = MibTableColumn
wfIpxRouteFilterCounter = _WfIpxRouteFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 12),
    _WfIpxRouteFilterCounter_Type()
)
wfIpxRouteFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRouteFilterCounter.setStatus("mandatory")
_WfIpxRouteFilterPriority_Type = Integer32
_WfIpxRouteFilterPriority_Object = MibTableColumn
wfIpxRouteFilterPriority = _WfIpxRouteFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 29, 1, 13),
    _WfIpxRouteFilterPriority_Type()
)
wfIpxRouteFilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRouteFilterPriority.setStatus("mandatory")
_WfIpxServNetFilterTable_Object = MibTable
wfIpxServNetFilterTable = _WfIpxServNetFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30)
)
if mibBuilder.loadTexts:
    wfIpxServNetFilterTable.setStatus("mandatory")
_WfIpxServNetFilterEntry_Object = MibTableRow
wfIpxServNetFilterEntry = _WfIpxServNetFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1)
)
wfIpxServNetFilterEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNetFilterSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNetFilterCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNetFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    wfIpxServNetFilterEntry.setStatus("mandatory")


class _WfIpxServNetFilterDelete_Type(Integer32):
    """Custom type wfIpxServNetFilterDelete based on Integer32"""
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


_WfIpxServNetFilterDelete_Type.__name__ = "Integer32"
_WfIpxServNetFilterDelete_Object = MibTableColumn
wfIpxServNetFilterDelete = _WfIpxServNetFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 1),
    _WfIpxServNetFilterDelete_Type()
)
wfIpxServNetFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterDelete.setStatus("mandatory")


class _WfIpxServNetFilterDisable_Type(Integer32):
    """Custom type wfIpxServNetFilterDisable based on Integer32"""
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


_WfIpxServNetFilterDisable_Type.__name__ = "Integer32"
_WfIpxServNetFilterDisable_Object = MibTableColumn
wfIpxServNetFilterDisable = _WfIpxServNetFilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 2),
    _WfIpxServNetFilterDisable_Type()
)
wfIpxServNetFilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterDisable.setStatus("mandatory")
_WfIpxServNetFilterSysInstance_Type = Integer32
_WfIpxServNetFilterSysInstance_Object = MibTableColumn
wfIpxServNetFilterSysInstance = _WfIpxServNetFilterSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 3),
    _WfIpxServNetFilterSysInstance_Type()
)
wfIpxServNetFilterSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNetFilterSysInstance.setStatus("mandatory")
_WfIpxServNetFilterCircIndex_Type = Integer32
_WfIpxServNetFilterCircIndex_Object = MibTableColumn
wfIpxServNetFilterCircIndex = _WfIpxServNetFilterCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 4),
    _WfIpxServNetFilterCircIndex_Type()
)
wfIpxServNetFilterCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNetFilterCircIndex.setStatus("mandatory")
_WfIpxServNetFilterRuleNumber_Type = Integer32
_WfIpxServNetFilterRuleNumber_Object = MibTableColumn
wfIpxServNetFilterRuleNumber = _WfIpxServNetFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 5),
    _WfIpxServNetFilterRuleNumber_Type()
)
wfIpxServNetFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNetFilterRuleNumber.setStatus("mandatory")
_WfIpxServNetFilterNetwork_Type = OctetString
_WfIpxServNetFilterNetwork_Object = MibTableColumn
wfIpxServNetFilterNetwork = _WfIpxServNetFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 6),
    _WfIpxServNetFilterNetwork_Type()
)
wfIpxServNetFilterNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterNetwork.setStatus("mandatory")
_WfIpxServNetFilterNetworkMask_Type = OctetString
_WfIpxServNetFilterNetworkMask_Object = MibTableColumn
wfIpxServNetFilterNetworkMask = _WfIpxServNetFilterNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 7),
    _WfIpxServNetFilterNetworkMask_Type()
)
wfIpxServNetFilterNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterNetworkMask.setStatus("mandatory")
_WfIpxServNetFilterType_Type = OctetString
_WfIpxServNetFilterType_Object = MibTableColumn
wfIpxServNetFilterType = _WfIpxServNetFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 8),
    _WfIpxServNetFilterType_Type()
)
wfIpxServNetFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterType.setStatus("mandatory")


class _WfIpxServNetFilterMode_Type(Integer32):
    """Custom type wfIpxServNetFilterMode based on Integer32"""
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
        *(("both", 3),
          ("inbound", 2),
          ("outbound", 1))
    )


_WfIpxServNetFilterMode_Type.__name__ = "Integer32"
_WfIpxServNetFilterMode_Object = MibTableColumn
wfIpxServNetFilterMode = _WfIpxServNetFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 9),
    _WfIpxServNetFilterMode_Type()
)
wfIpxServNetFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterMode.setStatus("mandatory")


class _WfIpxServNetFilterAction_Type(Integer32):
    """Custom type wfIpxServNetFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("suppress", 2))
    )


_WfIpxServNetFilterAction_Type.__name__ = "Integer32"
_WfIpxServNetFilterAction_Object = MibTableColumn
wfIpxServNetFilterAction = _WfIpxServNetFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 10),
    _WfIpxServNetFilterAction_Type()
)
wfIpxServNetFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterAction.setStatus("mandatory")


class _WfIpxServNetFilterProtocol_Type(Integer32):
    """Custom type wfIpxServNetFilterProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("local", 2),
          ("nlsp", 4),
          ("sap", 6),
          ("static", 5))
    )


_WfIpxServNetFilterProtocol_Type.__name__ = "Integer32"
_WfIpxServNetFilterProtocol_Object = MibTableColumn
wfIpxServNetFilterProtocol = _WfIpxServNetFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 11),
    _WfIpxServNetFilterProtocol_Type()
)
wfIpxServNetFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterProtocol.setStatus("mandatory")
_WfIpxServNetFilterCost_Type = Integer32
_WfIpxServNetFilterCost_Object = MibTableColumn
wfIpxServNetFilterCost = _WfIpxServNetFilterCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 12),
    _WfIpxServNetFilterCost_Type()
)
wfIpxServNetFilterCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterCost.setStatus("mandatory")
_WfIpxServNetFilterCounter_Type = Counter32
_WfIpxServNetFilterCounter_Object = MibTableColumn
wfIpxServNetFilterCounter = _WfIpxServNetFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 13),
    _WfIpxServNetFilterCounter_Type()
)
wfIpxServNetFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNetFilterCounter.setStatus("mandatory")
_WfIpxServNetFilterPriority_Type = Integer32
_WfIpxServNetFilterPriority_Object = MibTableColumn
wfIpxServNetFilterPriority = _WfIpxServNetFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 30, 1, 14),
    _WfIpxServNetFilterPriority_Type()
)
wfIpxServNetFilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNetFilterPriority.setStatus("mandatory")
_WfIpxServNameFilterTable_Object = MibTable
wfIpxServNameFilterTable = _WfIpxServNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31)
)
if mibBuilder.loadTexts:
    wfIpxServNameFilterTable.setStatus("mandatory")
_WfIpxServNameFilterEntry_Object = MibTableRow
wfIpxServNameFilterEntry = _WfIpxServNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1)
)
wfIpxServNameFilterEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNameFilterSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNameFilterCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxServNameFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    wfIpxServNameFilterEntry.setStatus("mandatory")


class _WfIpxServNameFilterDelete_Type(Integer32):
    """Custom type wfIpxServNameFilterDelete based on Integer32"""
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


_WfIpxServNameFilterDelete_Type.__name__ = "Integer32"
_WfIpxServNameFilterDelete_Object = MibTableColumn
wfIpxServNameFilterDelete = _WfIpxServNameFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 1),
    _WfIpxServNameFilterDelete_Type()
)
wfIpxServNameFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterDelete.setStatus("mandatory")


class _WfIpxServNameFilterDisable_Type(Integer32):
    """Custom type wfIpxServNameFilterDisable based on Integer32"""
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


_WfIpxServNameFilterDisable_Type.__name__ = "Integer32"
_WfIpxServNameFilterDisable_Object = MibTableColumn
wfIpxServNameFilterDisable = _WfIpxServNameFilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 2),
    _WfIpxServNameFilterDisable_Type()
)
wfIpxServNameFilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterDisable.setStatus("mandatory")
_WfIpxServNameFilterSysInstance_Type = Integer32
_WfIpxServNameFilterSysInstance_Object = MibTableColumn
wfIpxServNameFilterSysInstance = _WfIpxServNameFilterSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 3),
    _WfIpxServNameFilterSysInstance_Type()
)
wfIpxServNameFilterSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNameFilterSysInstance.setStatus("mandatory")
_WfIpxServNameFilterCircIndex_Type = Integer32
_WfIpxServNameFilterCircIndex_Object = MibTableColumn
wfIpxServNameFilterCircIndex = _WfIpxServNameFilterCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 4),
    _WfIpxServNameFilterCircIndex_Type()
)
wfIpxServNameFilterCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNameFilterCircIndex.setStatus("mandatory")
_WfIpxServNameFilterRuleNumber_Type = Integer32
_WfIpxServNameFilterRuleNumber_Object = MibTableColumn
wfIpxServNameFilterRuleNumber = _WfIpxServNameFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 5),
    _WfIpxServNameFilterRuleNumber_Type()
)
wfIpxServNameFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNameFilterRuleNumber.setStatus("mandatory")
_WfIpxServNameFilterName_Type = DisplayString
_WfIpxServNameFilterName_Object = MibTableColumn
wfIpxServNameFilterName = _WfIpxServNameFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 6),
    _WfIpxServNameFilterName_Type()
)
wfIpxServNameFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterName.setStatus("mandatory")
_WfIpxServNameFilterType_Type = OctetString
_WfIpxServNameFilterType_Object = MibTableColumn
wfIpxServNameFilterType = _WfIpxServNameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 7),
    _WfIpxServNameFilterType_Type()
)
wfIpxServNameFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterType.setStatus("mandatory")


class _WfIpxServNameFilterMode_Type(Integer32):
    """Custom type wfIpxServNameFilterMode based on Integer32"""
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
        *(("both", 3),
          ("inbound", 2),
          ("outbound", 1))
    )


_WfIpxServNameFilterMode_Type.__name__ = "Integer32"
_WfIpxServNameFilterMode_Object = MibTableColumn
wfIpxServNameFilterMode = _WfIpxServNameFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 8),
    _WfIpxServNameFilterMode_Type()
)
wfIpxServNameFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterMode.setStatus("mandatory")


class _WfIpxServNameFilterAction_Type(Integer32):
    """Custom type wfIpxServNameFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("suppress", 2))
    )


_WfIpxServNameFilterAction_Type.__name__ = "Integer32"
_WfIpxServNameFilterAction_Object = MibTableColumn
wfIpxServNameFilterAction = _WfIpxServNameFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 9),
    _WfIpxServNameFilterAction_Type()
)
wfIpxServNameFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterAction.setStatus("mandatory")


class _WfIpxServNameFilterProtocol_Type(Integer32):
    """Custom type wfIpxServNameFilterProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("local", 2),
          ("nlsp", 4),
          ("sap", 6),
          ("static", 5))
    )


_WfIpxServNameFilterProtocol_Type.__name__ = "Integer32"
_WfIpxServNameFilterProtocol_Object = MibTableColumn
wfIpxServNameFilterProtocol = _WfIpxServNameFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 10),
    _WfIpxServNameFilterProtocol_Type()
)
wfIpxServNameFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterProtocol.setStatus("mandatory")
_WfIpxServNameFilterCost_Type = Integer32
_WfIpxServNameFilterCost_Object = MibTableColumn
wfIpxServNameFilterCost = _WfIpxServNameFilterCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 11),
    _WfIpxServNameFilterCost_Type()
)
wfIpxServNameFilterCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterCost.setStatus("mandatory")
_WfIpxServNameFilterCounter_Type = Counter32
_WfIpxServNameFilterCounter_Object = MibTableColumn
wfIpxServNameFilterCounter = _WfIpxServNameFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 12),
    _WfIpxServNameFilterCounter_Type()
)
wfIpxServNameFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxServNameFilterCounter.setStatus("mandatory")
_WfIpxServNameFilterPriority_Type = Integer32
_WfIpxServNameFilterPriority_Object = MibTableColumn
wfIpxServNameFilterPriority = _WfIpxServNameFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 31, 1, 13),
    _WfIpxServNameFilterPriority_Type()
)
wfIpxServNameFilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxServNameFilterPriority.setStatus("mandatory")
_WfIpxRipCircTable_Object = MibTable
wfIpxRipCircTable = _WfIpxRipCircTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32)
)
if mibBuilder.loadTexts:
    wfIpxRipCircTable.setStatus("mandatory")
_WfIpxRipCircEntry_Object = MibTableRow
wfIpxRipCircEntry = _WfIpxRipCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1)
)
wfIpxRipCircEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxRipCircSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxRipCircIndex"),
)
if mibBuilder.loadTexts:
    wfIpxRipCircEntry.setStatus("mandatory")


class _WfIpxRipCircDelete_Type(Integer32):
    """Custom type wfIpxRipCircDelete based on Integer32"""
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


_WfIpxRipCircDelete_Type.__name__ = "Integer32"
_WfIpxRipCircDelete_Object = MibTableColumn
wfIpxRipCircDelete = _WfIpxRipCircDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 1),
    _WfIpxRipCircDelete_Type()
)
wfIpxRipCircDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircDelete.setStatus("mandatory")


class _WfIpxRipCircDisable_Type(Integer32):
    """Custom type wfIpxRipCircDisable based on Integer32"""
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


_WfIpxRipCircDisable_Type.__name__ = "Integer32"
_WfIpxRipCircDisable_Object = MibTableColumn
wfIpxRipCircDisable = _WfIpxRipCircDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 2),
    _WfIpxRipCircDisable_Type()
)
wfIpxRipCircDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircDisable.setStatus("mandatory")


class _WfIpxRipCircState_Type(Integer32):
    """Custom type wfIpxRipCircState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxRipCircState_Type.__name__ = "Integer32"
_WfIpxRipCircState_Object = MibTableColumn
wfIpxRipCircState = _WfIpxRipCircState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 3),
    _WfIpxRipCircState_Type()
)
wfIpxRipCircState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircState.setStatus("mandatory")
_WfIpxRipCircSysInstance_Type = Integer32
_WfIpxRipCircSysInstance_Object = MibTableColumn
wfIpxRipCircSysInstance = _WfIpxRipCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 4),
    _WfIpxRipCircSysInstance_Type()
)
wfIpxRipCircSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircSysInstance.setStatus("mandatory")
_WfIpxRipCircIndex_Type = Integer32
_WfIpxRipCircIndex_Object = MibTableColumn
wfIpxRipCircIndex = _WfIpxRipCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 5),
    _WfIpxRipCircIndex_Type()
)
wfIpxRipCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircIndex.setStatus("mandatory")


class _WfIpxRipCircMode_Type(Integer32):
    """Custom type wfIpxRipCircMode based on Integer32"""
    defaultValue = 1

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
        *(("auto", 4),
          ("listen", 2),
          ("standard", 1),
          ("supply", 3))
    )


_WfIpxRipCircMode_Type.__name__ = "Integer32"
_WfIpxRipCircMode_Object = MibTableColumn
wfIpxRipCircMode = _WfIpxRipCircMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 6),
    _WfIpxRipCircMode_Type()
)
wfIpxRipCircMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircMode.setStatus("mandatory")


class _WfIpxRipCircPace_Type(Integer32):
    """Custom type wfIpxRipCircPace based on Integer32"""
    defaultValue = 18


_WfIpxRipCircPace_Object = MibTableColumn
wfIpxRipCircPace = _WfIpxRipCircPace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 7),
    _WfIpxRipCircPace_Type()
)
wfIpxRipCircPace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircPace.setStatus("mandatory")


class _WfIpxRipCircUpdate_Type(Integer32):
    """Custom type wfIpxRipCircUpdate based on Integer32"""
    defaultValue = 60


_WfIpxRipCircUpdate_Object = MibTableColumn
wfIpxRipCircUpdate = _WfIpxRipCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 8),
    _WfIpxRipCircUpdate_Type()
)
wfIpxRipCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircUpdate.setStatus("mandatory")


class _WfIpxRipCircAgeMultiplier_Type(Integer32):
    """Custom type wfIpxRipCircAgeMultiplier based on Integer32"""
    defaultValue = 3


_WfIpxRipCircAgeMultiplier_Object = MibTableColumn
wfIpxRipCircAgeMultiplier = _WfIpxRipCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 9),
    _WfIpxRipCircAgeMultiplier_Type()
)
wfIpxRipCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircAgeMultiplier.setStatus("mandatory")


class _WfIpxRipCircPacketSize_Type(Integer32):
    """Custom type wfIpxRipCircPacketSize based on Integer32"""
    defaultValue = 432


_WfIpxRipCircPacketSize_Object = MibTableColumn
wfIpxRipCircPacketSize = _WfIpxRipCircPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 10),
    _WfIpxRipCircPacketSize_Type()
)
wfIpxRipCircPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircPacketSize.setStatus("mandatory")
_WfIpxRipCircOutPackets_Type = Counter32
_WfIpxRipCircOutPackets_Object = MibTableColumn
wfIpxRipCircOutPackets = _WfIpxRipCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 11),
    _WfIpxRipCircOutPackets_Type()
)
wfIpxRipCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircOutPackets.setStatus("mandatory")
_WfIpxRipCircInPackets_Type = Counter32
_WfIpxRipCircInPackets_Object = MibTableColumn
wfIpxRipCircInPackets = _WfIpxRipCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 12),
    _WfIpxRipCircInPackets_Type()
)
wfIpxRipCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircInPackets.setStatus("mandatory")
_WfIpxRipCircBadPackets_Type = Counter32
_WfIpxRipCircBadPackets_Object = MibTableColumn
wfIpxRipCircBadPackets = _WfIpxRipCircBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 13),
    _WfIpxRipCircBadPackets_Type()
)
wfIpxRipCircBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipCircBadPackets.setStatus("mandatory")


class _WfIpxRipCircUseMulticast_Type(Integer32):
    """Custom type wfIpxRipCircUseMulticast based on Integer32"""
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


_WfIpxRipCircUseMulticast_Type.__name__ = "Integer32"
_WfIpxRipCircUseMulticast_Object = MibTableColumn
wfIpxRipCircUseMulticast = _WfIpxRipCircUseMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 14),
    _WfIpxRipCircUseMulticast_Type()
)
wfIpxRipCircUseMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircUseMulticast.setStatus("mandatory")


class _WfIpxRipCircSplitHorizon_Type(Integer32):
    """Custom type wfIpxRipCircSplitHorizon based on Integer32"""
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


_WfIpxRipCircSplitHorizon_Type.__name__ = "Integer32"
_WfIpxRipCircSplitHorizon_Object = MibTableColumn
wfIpxRipCircSplitHorizon = _WfIpxRipCircSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 15),
    _WfIpxRipCircSplitHorizon_Type()
)
wfIpxRipCircSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircSplitHorizon.setStatus("mandatory")


class _WfIpxRipCircGenAutoStaticRoutes_Type(Integer32):
    """Custom type wfIpxRipCircGenAutoStaticRoutes based on Integer32"""
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


_WfIpxRipCircGenAutoStaticRoutes_Type.__name__ = "Integer32"
_WfIpxRipCircGenAutoStaticRoutes_Object = MibTableColumn
wfIpxRipCircGenAutoStaticRoutes = _WfIpxRipCircGenAutoStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 16),
    _WfIpxRipCircGenAutoStaticRoutes_Type()
)
wfIpxRipCircGenAutoStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircGenAutoStaticRoutes.setStatus("mandatory")


class _WfIpxRipCircImmedUpdate_Type(Integer32):
    """Custom type wfIpxRipCircImmedUpdate based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("useglobal", 3))
    )


_WfIpxRipCircImmedUpdate_Type.__name__ = "Integer32"
_WfIpxRipCircImmedUpdate_Object = MibTableColumn
wfIpxRipCircImmedUpdate = _WfIpxRipCircImmedUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 17),
    _WfIpxRipCircImmedUpdate_Type()
)
wfIpxRipCircImmedUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircImmedUpdate.setStatus("mandatory")


class _WfIpxRipCircDefaultRouteSupply_Type(Integer32):
    """Custom type wfIpxRipCircDefaultRouteSupply based on Integer32"""
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


_WfIpxRipCircDefaultRouteSupply_Type.__name__ = "Integer32"
_WfIpxRipCircDefaultRouteSupply_Object = MibTableColumn
wfIpxRipCircDefaultRouteSupply = _WfIpxRipCircDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 18),
    _WfIpxRipCircDefaultRouteSupply_Type()
)
wfIpxRipCircDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircDefaultRouteSupply.setStatus("mandatory")


class _WfIpxRipCircDefaultRouteListen_Type(Integer32):
    """Custom type wfIpxRipCircDefaultRouteListen based on Integer32"""
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


_WfIpxRipCircDefaultRouteListen_Type.__name__ = "Integer32"
_WfIpxRipCircDefaultRouteListen_Object = MibTableColumn
wfIpxRipCircDefaultRouteListen = _WfIpxRipCircDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 19),
    _WfIpxRipCircDefaultRouteListen_Type()
)
wfIpxRipCircDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircDefaultRouteListen.setStatus("mandatory")


class _WfIpxRipCircLostRouteDisable_Type(Integer32):
    """Custom type wfIpxRipCircLostRouteDisable based on Integer32"""
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


_WfIpxRipCircLostRouteDisable_Type.__name__ = "Integer32"
_WfIpxRipCircLostRouteDisable_Object = MibTableColumn
wfIpxRipCircLostRouteDisable = _WfIpxRipCircLostRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 32, 1, 20),
    _WfIpxRipCircLostRouteDisable_Type()
)
wfIpxRipCircLostRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipCircLostRouteDisable.setStatus("mandatory")
_WfIpxSapCircTable_Object = MibTable
wfIpxSapCircTable = _WfIpxSapCircTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33)
)
if mibBuilder.loadTexts:
    wfIpxSapCircTable.setStatus("mandatory")
_WfIpxSapCircEntry_Object = MibTableRow
wfIpxSapCircEntry = _WfIpxSapCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1)
)
wfIpxSapCircEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxSapCircSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxSapCircIndex"),
)
if mibBuilder.loadTexts:
    wfIpxSapCircEntry.setStatus("mandatory")


class _WfIpxSapCircDelete_Type(Integer32):
    """Custom type wfIpxSapCircDelete based on Integer32"""
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


_WfIpxSapCircDelete_Type.__name__ = "Integer32"
_WfIpxSapCircDelete_Object = MibTableColumn
wfIpxSapCircDelete = _WfIpxSapCircDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 1),
    _WfIpxSapCircDelete_Type()
)
wfIpxSapCircDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircDelete.setStatus("mandatory")


class _WfIpxSapCircDisable_Type(Integer32):
    """Custom type wfIpxSapCircDisable based on Integer32"""
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


_WfIpxSapCircDisable_Type.__name__ = "Integer32"
_WfIpxSapCircDisable_Object = MibTableColumn
wfIpxSapCircDisable = _WfIpxSapCircDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 2),
    _WfIpxSapCircDisable_Type()
)
wfIpxSapCircDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircDisable.setStatus("mandatory")


class _WfIpxSapCircState_Type(Integer32):
    """Custom type wfIpxSapCircState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxSapCircState_Type.__name__ = "Integer32"
_WfIpxSapCircState_Object = MibTableColumn
wfIpxSapCircState = _WfIpxSapCircState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 3),
    _WfIpxSapCircState_Type()
)
wfIpxSapCircState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircState.setStatus("mandatory")
_WfIpxSapCircSysInstance_Type = Integer32
_WfIpxSapCircSysInstance_Object = MibTableColumn
wfIpxSapCircSysInstance = _WfIpxSapCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 4),
    _WfIpxSapCircSysInstance_Type()
)
wfIpxSapCircSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircSysInstance.setStatus("mandatory")
_WfIpxSapCircIndex_Type = Integer32
_WfIpxSapCircIndex_Object = MibTableColumn
wfIpxSapCircIndex = _WfIpxSapCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 5),
    _WfIpxSapCircIndex_Type()
)
wfIpxSapCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircIndex.setStatus("mandatory")


class _WfIpxSapCircMode_Type(Integer32):
    """Custom type wfIpxSapCircMode based on Integer32"""
    defaultValue = 1

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
        *(("auto", 4),
          ("listen", 2),
          ("standard", 1),
          ("supply", 3))
    )


_WfIpxSapCircMode_Type.__name__ = "Integer32"
_WfIpxSapCircMode_Object = MibTableColumn
wfIpxSapCircMode = _WfIpxSapCircMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 6),
    _WfIpxSapCircMode_Type()
)
wfIpxSapCircMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircMode.setStatus("mandatory")


class _WfIpxSapCircPace_Type(Integer32):
    """Custom type wfIpxSapCircPace based on Integer32"""
    defaultValue = 18


_WfIpxSapCircPace_Object = MibTableColumn
wfIpxSapCircPace = _WfIpxSapCircPace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 7),
    _WfIpxSapCircPace_Type()
)
wfIpxSapCircPace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircPace.setStatus("mandatory")


class _WfIpxSapCircUpdate_Type(Integer32):
    """Custom type wfIpxSapCircUpdate based on Integer32"""
    defaultValue = 60


_WfIpxSapCircUpdate_Object = MibTableColumn
wfIpxSapCircUpdate = _WfIpxSapCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 8),
    _WfIpxSapCircUpdate_Type()
)
wfIpxSapCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircUpdate.setStatus("mandatory")


class _WfIpxSapCircAgeMultiplier_Type(Integer32):
    """Custom type wfIpxSapCircAgeMultiplier based on Integer32"""
    defaultValue = 3


_WfIpxSapCircAgeMultiplier_Object = MibTableColumn
wfIpxSapCircAgeMultiplier = _WfIpxSapCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 9),
    _WfIpxSapCircAgeMultiplier_Type()
)
wfIpxSapCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircAgeMultiplier.setStatus("mandatory")


class _WfIpxSapCircPacketSize_Type(Integer32):
    """Custom type wfIpxSapCircPacketSize based on Integer32"""
    defaultValue = 480


_WfIpxSapCircPacketSize_Object = MibTableColumn
wfIpxSapCircPacketSize = _WfIpxSapCircPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 10),
    _WfIpxSapCircPacketSize_Type()
)
wfIpxSapCircPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircPacketSize.setStatus("mandatory")


class _WfIpxSapCircGetNearestServerReply_Type(Integer32):
    """Custom type wfIpxSapCircGetNearestServerReply based on Integer32"""
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


_WfIpxSapCircGetNearestServerReply_Type.__name__ = "Integer32"
_WfIpxSapCircGetNearestServerReply_Object = MibTableColumn
wfIpxSapCircGetNearestServerReply = _WfIpxSapCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 11),
    _WfIpxSapCircGetNearestServerReply_Type()
)
wfIpxSapCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircGetNearestServerReply.setStatus("mandatory")


class _WfIpxSapCircNSQAlphabetical_Type(Integer32):
    """Custom type wfIpxSapCircNSQAlphabetical based on Integer32"""
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


_WfIpxSapCircNSQAlphabetical_Type.__name__ = "Integer32"
_WfIpxSapCircNSQAlphabetical_Object = MibTableColumn
wfIpxSapCircNSQAlphabetical = _WfIpxSapCircNSQAlphabetical_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 12),
    _WfIpxSapCircNSQAlphabetical_Type()
)
wfIpxSapCircNSQAlphabetical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircNSQAlphabetical.setStatus("mandatory")
_WfIpxSapCircOutPackets_Type = Counter32
_WfIpxSapCircOutPackets_Object = MibTableColumn
wfIpxSapCircOutPackets = _WfIpxSapCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 13),
    _WfIpxSapCircOutPackets_Type()
)
wfIpxSapCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircOutPackets.setStatus("mandatory")
_WfIpxSapCircInPackets_Type = Counter32
_WfIpxSapCircInPackets_Object = MibTableColumn
wfIpxSapCircInPackets = _WfIpxSapCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 14),
    _WfIpxSapCircInPackets_Type()
)
wfIpxSapCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircInPackets.setStatus("mandatory")
_WfIpxSapCircBadPackets_Type = Counter32
_WfIpxSapCircBadPackets_Object = MibTableColumn
wfIpxSapCircBadPackets = _WfIpxSapCircBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 15),
    _WfIpxSapCircBadPackets_Type()
)
wfIpxSapCircBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapCircBadPackets.setStatus("mandatory")


class _WfIpxSapCircUseMulticast_Type(Integer32):
    """Custom type wfIpxSapCircUseMulticast based on Integer32"""
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


_WfIpxSapCircUseMulticast_Type.__name__ = "Integer32"
_WfIpxSapCircUseMulticast_Object = MibTableColumn
wfIpxSapCircUseMulticast = _WfIpxSapCircUseMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 16),
    _WfIpxSapCircUseMulticast_Type()
)
wfIpxSapCircUseMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircUseMulticast.setStatus("mandatory")


class _WfIpxSapCircSplitHorizon_Type(Integer32):
    """Custom type wfIpxSapCircSplitHorizon based on Integer32"""
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


_WfIpxSapCircSplitHorizon_Type.__name__ = "Integer32"
_WfIpxSapCircSplitHorizon_Object = MibTableColumn
wfIpxSapCircSplitHorizon = _WfIpxSapCircSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 17),
    _WfIpxSapCircSplitHorizon_Type()
)
wfIpxSapCircSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircSplitHorizon.setStatus("mandatory")


class _WfIpxSapCircGenAutoStaticServices_Type(Integer32):
    """Custom type wfIpxSapCircGenAutoStaticServices based on Integer32"""
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


_WfIpxSapCircGenAutoStaticServices_Type.__name__ = "Integer32"
_WfIpxSapCircGenAutoStaticServices_Object = MibTableColumn
wfIpxSapCircGenAutoStaticServices = _WfIpxSapCircGenAutoStaticServices_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 18),
    _WfIpxSapCircGenAutoStaticServices_Type()
)
wfIpxSapCircGenAutoStaticServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircGenAutoStaticServices.setStatus("mandatory")


class _WfIpxSapCircImmedUpdate_Type(Integer32):
    """Custom type wfIpxSapCircImmedUpdate based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("useglobal", 3))
    )


_WfIpxSapCircImmedUpdate_Type.__name__ = "Integer32"
_WfIpxSapCircImmedUpdate_Object = MibTableColumn
wfIpxSapCircImmedUpdate = _WfIpxSapCircImmedUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 19),
    _WfIpxSapCircImmedUpdate_Type()
)
wfIpxSapCircImmedUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircImmedUpdate.setStatus("mandatory")


class _WfIpxSapCircSaveFullName_Type(Integer32):
    """Custom type wfIpxSapCircSaveFullName based on Integer32"""
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


_WfIpxSapCircSaveFullName_Type.__name__ = "Integer32"
_WfIpxSapCircSaveFullName_Object = MibTableColumn
wfIpxSapCircSaveFullName = _WfIpxSapCircSaveFullName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 33, 1, 20),
    _WfIpxSapCircSaveFullName_Type()
)
wfIpxSapCircSaveFullName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapCircSaveFullName.setStatus("mandatory")
_WfIpxHostEntryTable_Object = MibTable
wfIpxHostEntryTable = _WfIpxHostEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34)
)
if mibBuilder.loadTexts:
    wfIpxHostEntryTable.setStatus("mandatory")
_WfIpxHostEntry_Object = MibTableRow
wfIpxHostEntry = _WfIpxHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1)
)
wfIpxHostEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxHostSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxHostNextHopCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxHostHostAddress"),
)
if mibBuilder.loadTexts:
    wfIpxHostEntry.setStatus("mandatory")
_WfIpxHostSysInstance_Type = Integer32
_WfIpxHostSysInstance_Object = MibTableColumn
wfIpxHostSysInstance = _WfIpxHostSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 1),
    _WfIpxHostSysInstance_Type()
)
wfIpxHostSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostSysInstance.setStatus("mandatory")
_WfIpxHostNextHopCircIndex_Type = Integer32
_WfIpxHostNextHopCircIndex_Object = MibTableColumn
wfIpxHostNextHopCircIndex = _WfIpxHostNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 2),
    _WfIpxHostNextHopCircIndex_Type()
)
wfIpxHostNextHopCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostNextHopCircIndex.setStatus("mandatory")


class _WfIpxHostHostAddress_Type(OctetString):
    """Custom type wfIpxHostHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfIpxHostHostAddress_Type.__name__ = "OctetString"
_WfIpxHostHostAddress_Object = MibTableColumn
wfIpxHostHostAddress = _WfIpxHostHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 3),
    _WfIpxHostHostAddress_Type()
)
wfIpxHostHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostHostAddress.setStatus("mandatory")
_WfIpxHostNetNum_Type = OctetString
_WfIpxHostNetNum_Object = MibTableColumn
wfIpxHostNetNum = _WfIpxHostNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 4),
    _WfIpxHostNetNum_Type()
)
wfIpxHostNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostNetNum.setStatus("mandatory")
_WfIpxHostWanAddress_Type = OctetString
_WfIpxHostWanAddress_Object = MibTableColumn
wfIpxHostWanAddress = _WfIpxHostWanAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 5),
    _WfIpxHostWanAddress_Type()
)
wfIpxHostWanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostWanAddress.setStatus("mandatory")


class _WfIpxHostProtocol_Type(Integer32):
    """Custom type wfIpxHostProtocol based on Integer32"""
    defaultValue = 1

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
        *(("dynamic", 3),
          ("local", 2),
          ("other", 1),
          ("static", 4))
    )


_WfIpxHostProtocol_Type.__name__ = "Integer32"
_WfIpxHostProtocol_Object = MibTableColumn
wfIpxHostProtocol = _WfIpxHostProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 6),
    _WfIpxHostProtocol_Type()
)
wfIpxHostProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostProtocol.setStatus("mandatory")
_WfIpxHostAge_Type = Integer32
_WfIpxHostAge_Object = MibTableColumn
wfIpxHostAge = _WfIpxHostAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 34, 1, 7),
    _WfIpxHostAge_Type()
)
wfIpxHostAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxHostAge.setStatus("mandatory")
_WfIpxForwardEntryTable_Object = MibTable
wfIpxForwardEntryTable = _WfIpxForwardEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35)
)
if mibBuilder.loadTexts:
    wfIpxForwardEntryTable.setStatus("mandatory")
_WfIpxForwardEntry_Object = MibTableRow
wfIpxForwardEntry = _WfIpxForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1)
)
wfIpxForwardEntry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxForwardSysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxForwardCircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxForwardNetNum"),
)
if mibBuilder.loadTexts:
    wfIpxForwardEntry.setStatus("mandatory")
_WfIpxForwardSysInstance_Type = Integer32
_WfIpxForwardSysInstance_Object = MibTableColumn
wfIpxForwardSysInstance = _WfIpxForwardSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 1),
    _WfIpxForwardSysInstance_Type()
)
wfIpxForwardSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardSysInstance.setStatus("mandatory")
_WfIpxForwardCircIndex_Type = Integer32
_WfIpxForwardCircIndex_Object = MibTableColumn
wfIpxForwardCircIndex = _WfIpxForwardCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 2),
    _WfIpxForwardCircIndex_Type()
)
wfIpxForwardCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardCircIndex.setStatus("mandatory")


class _WfIpxForwardNetNum_Type(OctetString):
    """Custom type wfIpxForwardNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfIpxForwardNetNum_Type.__name__ = "OctetString"
_WfIpxForwardNetNum_Object = MibTableColumn
wfIpxForwardNetNum = _WfIpxForwardNetNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 3),
    _WfIpxForwardNetNum_Type()
)
wfIpxForwardNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardNetNum.setStatus("mandatory")


class _WfIpxForwardType_Type(Integer32):
    """Custom type wfIpxForwardType based on Integer32"""
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
        *(("local", 2),
          ("other", 1),
          ("remote", 3))
    )


_WfIpxForwardType_Type.__name__ = "Integer32"
_WfIpxForwardType_Object = MibTableColumn
wfIpxForwardType = _WfIpxForwardType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 4),
    _WfIpxForwardType_Type()
)
wfIpxForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardType.setStatus("mandatory")


class _WfIpxForwardProtocol_Type(Integer32):
    """Custom type wfIpxForwardProtocol based on Integer32"""
    defaultValue = 1

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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_WfIpxForwardProtocol_Type.__name__ = "Integer32"
_WfIpxForwardProtocol_Object = MibTableColumn
wfIpxForwardProtocol = _WfIpxForwardProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 5),
    _WfIpxForwardProtocol_Type()
)
wfIpxForwardProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardProtocol.setStatus("mandatory")
_WfIpxForwardCount_Type = Counter32
_WfIpxForwardCount_Object = MibTableColumn
wfIpxForwardCount = _WfIpxForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 35, 1, 6),
    _WfIpxForwardCount_Type()
)
wfIpxForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxForwardCount.setStatus("mandatory")
_WfIpxTrafficFilter2Table_Object = MibTable
wfIpxTrafficFilter2Table = _WfIpxTrafficFilter2Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36)
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Table.setStatus("mandatory")
_WfIpxTrafficFilter2Entry_Object = MibTableRow
wfIpxTrafficFilter2Entry = _WfIpxTrafficFilter2Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1)
)
wfIpxTrafficFilter2Entry.setIndexNames(
    (0, "Wellfleet-IPXA-MIB", "wfIpxTrafficFilter2SysInstance"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxTrafficFilter2CircIndex"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxTrafficFilter2RuleNumber"),
    (0, "Wellfleet-IPXA-MIB", "wfIpxTrafficFilter2Fragment"),
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Entry.setStatus("mandatory")


class _WfIpxTrafficFilter2Create_Type(Integer32):
    """Custom type wfIpxTrafficFilter2Create based on Integer32"""
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


_WfIpxTrafficFilter2Create_Type.__name__ = "Integer32"
_WfIpxTrafficFilter2Create_Object = MibTableColumn
wfIpxTrafficFilter2Create = _WfIpxTrafficFilter2Create_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 1),
    _WfIpxTrafficFilter2Create_Type()
)
wfIpxTrafficFilter2Create.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Create.setStatus("mandatory")


class _WfIpxTrafficFilter2Enable_Type(Integer32):
    """Custom type wfIpxTrafficFilter2Enable based on Integer32"""
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


_WfIpxTrafficFilter2Enable_Type.__name__ = "Integer32"
_WfIpxTrafficFilter2Enable_Object = MibTableColumn
wfIpxTrafficFilter2Enable = _WfIpxTrafficFilter2Enable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 2),
    _WfIpxTrafficFilter2Enable_Type()
)
wfIpxTrafficFilter2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Enable.setStatus("mandatory")


class _WfIpxTrafficFilter2Status_Type(Integer32):
    """Custom type wfIpxTrafficFilter2Status based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfIpxTrafficFilter2Status_Type.__name__ = "Integer32"
_WfIpxTrafficFilter2Status_Object = MibTableColumn
wfIpxTrafficFilter2Status = _WfIpxTrafficFilter2Status_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 3),
    _WfIpxTrafficFilter2Status_Type()
)
wfIpxTrafficFilter2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Status.setStatus("mandatory")
_WfIpxTrafficFilter2Counter_Type = Counter32
_WfIpxTrafficFilter2Counter_Object = MibTableColumn
wfIpxTrafficFilter2Counter = _WfIpxTrafficFilter2Counter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 4),
    _WfIpxTrafficFilter2Counter_Type()
)
wfIpxTrafficFilter2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Counter.setStatus("mandatory")
_WfIpxTrafficFilter2Definition_Type = Opaque
_WfIpxTrafficFilter2Definition_Object = MibTableColumn
wfIpxTrafficFilter2Definition = _WfIpxTrafficFilter2Definition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 5),
    _WfIpxTrafficFilter2Definition_Type()
)
wfIpxTrafficFilter2Definition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Definition.setStatus("mandatory")
_WfIpxTrafficFilter2Reserved_Type = Integer32
_WfIpxTrafficFilter2Reserved_Object = MibTableColumn
wfIpxTrafficFilter2Reserved = _WfIpxTrafficFilter2Reserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 6),
    _WfIpxTrafficFilter2Reserved_Type()
)
wfIpxTrafficFilter2Reserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Reserved.setStatus("mandatory")
_WfIpxTrafficFilter2SysInstance_Type = Integer32
_WfIpxTrafficFilter2SysInstance_Object = MibTableColumn
wfIpxTrafficFilter2SysInstance = _WfIpxTrafficFilter2SysInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 7),
    _WfIpxTrafficFilter2SysInstance_Type()
)
wfIpxTrafficFilter2SysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2SysInstance.setStatus("mandatory")
_WfIpxTrafficFilter2CircIndex_Type = Integer32
_WfIpxTrafficFilter2CircIndex_Object = MibTableColumn
wfIpxTrafficFilter2CircIndex = _WfIpxTrafficFilter2CircIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 8),
    _WfIpxTrafficFilter2CircIndex_Type()
)
wfIpxTrafficFilter2CircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2CircIndex.setStatus("mandatory")
_WfIpxTrafficFilter2RuleNumber_Type = Integer32
_WfIpxTrafficFilter2RuleNumber_Object = MibTableColumn
wfIpxTrafficFilter2RuleNumber = _WfIpxTrafficFilter2RuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 9),
    _WfIpxTrafficFilter2RuleNumber_Type()
)
wfIpxTrafficFilter2RuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2RuleNumber.setStatus("mandatory")
_WfIpxTrafficFilter2Fragment_Type = Integer32
_WfIpxTrafficFilter2Fragment_Object = MibTableColumn
wfIpxTrafficFilter2Fragment = _WfIpxTrafficFilter2Fragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 10),
    _WfIpxTrafficFilter2Fragment_Type()
)
wfIpxTrafficFilter2Fragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Fragment.setStatus("mandatory")
_WfIpxTrafficFilter2Name_Type = DisplayString
_WfIpxTrafficFilter2Name_Object = MibTableColumn
wfIpxTrafficFilter2Name = _WfIpxTrafficFilter2Name_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 36, 1, 11),
    _WfIpxTrafficFilter2Name_Type()
)
wfIpxTrafficFilter2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilter2Name.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPXA-MIB",
    **{"wfIpxBasicSysTable": wfIpxBasicSysTable,
       "wfIpxBasicSysEntry": wfIpxBasicSysEntry,
       "wfIpxBasicSysDelete": wfIpxBasicSysDelete,
       "wfIpxBasicSysDisable": wfIpxBasicSysDisable,
       "wfIpxBasicSysState": wfIpxBasicSysState,
       "wfIpxBasicSysInstance": wfIpxBasicSysInstance,
       "wfIpxBasicSysPrimaryNetworkNumber": wfIpxBasicSysPrimaryNetworkNumber,
       "wfIpxBasicSysMultipleHostAddresses": wfIpxBasicSysMultipleHostAddresses,
       "wfIpxBasicSysCfgHostAddress": wfIpxBasicSysCfgHostAddress,
       "wfIpxBasicSysHostAddress": wfIpxBasicSysHostAddress,
       "wfIpxBasicSysRouterName": wfIpxBasicSysRouterName,
       "wfIpxBasicSysInReceives": wfIpxBasicSysInReceives,
       "wfIpxBasicSysInHdrErrors": wfIpxBasicSysInHdrErrors,
       "wfIpxBasicSysInUnknownSockets": wfIpxBasicSysInUnknownSockets,
       "wfIpxBasicSysInDiscards": wfIpxBasicSysInDiscards,
       "wfIpxBasicSysInBadChecksums": wfIpxBasicSysInBadChecksums,
       "wfIpxBasicSysInDelivers": wfIpxBasicSysInDelivers,
       "wfIpxBasicSysNoRoutes": wfIpxBasicSysNoRoutes,
       "wfIpxBasicSysOutRequests": wfIpxBasicSysOutRequests,
       "wfIpxBasicSysOutMalformedRequests": wfIpxBasicSysOutMalformedRequests,
       "wfIpxBasicSysOutPackets": wfIpxBasicSysOutPackets,
       "wfIpxBasicSysOpenEncapsFails": wfIpxBasicSysOpenEncapsFails,
       "wfIpxBasicSysOutDiscards": wfIpxBasicSysOutDiscards,
       "wfIpxAdvSysTable": wfIpxAdvSysTable,
       "wfIpxAdvSysEntry": wfIpxAdvSysEntry,
       "wfIpxAdvSysDelete": wfIpxAdvSysDelete,
       "wfIpxAdvSysInstance": wfIpxAdvSysInstance,
       "wfIpxAdvSysRoutingMethod": wfIpxAdvSysRoutingMethod,
       "wfIpxAdvSysLogFilter": wfIpxAdvSysLogFilter,
       "wfIpxAdvSysMaximumPath": wfIpxAdvSysMaximumPath,
       "wfIpxAdvSysMaxPathSplits": wfIpxAdvSysMaxPathSplits,
       "wfIpxAdvSysMaxHops": wfIpxAdvSysMaxHops,
       "wfIpxAdvSysInTooManyHops": wfIpxAdvSysInTooManyHops,
       "wfIpxAdvSysInFiltered": wfIpxAdvSysInFiltered,
       "wfIpxAdvSysInCompressDiscards": wfIpxAdvSysInCompressDiscards,
       "wfIpxAdvSysNETBIOSPackets": wfIpxAdvSysNETBIOSPackets,
       "wfIpxAdvSysForwPackets": wfIpxAdvSysForwPackets,
       "wfIpxAdvSysOutFiltered": wfIpxAdvSysOutFiltered,
       "wfIpxAdvSysOutCompressDiscards": wfIpxAdvSysOutCompressDiscards,
       "wfIpxAdvSysNovellCertificationConformanceDisable": wfIpxAdvSysNovellCertificationConformanceDisable,
       "wfIpxAdvSysCircCount": wfIpxAdvSysCircCount,
       "wfIpxAdvSysCfgDestCount": wfIpxAdvSysCfgDestCount,
       "wfIpxAdvSysDestCount": wfIpxAdvSysDestCount,
       "wfIpxAdvSysCfgServCount": wfIpxAdvSysCfgServCount,
       "wfIpxAdvSysServCount": wfIpxAdvSysServCount,
       "wfIpxAdvSysCfgHostCount": wfIpxAdvSysCfgHostCount,
       "wfIpxAdvSysHostCount": wfIpxAdvSysHostCount,
       "wfIpxAdvSysAgingFrequency": wfIpxAdvSysAgingFrequency,
       "wfIpxAdvSysAgingPendingFrequency": wfIpxAdvSysAgingPendingFrequency,
       "wfIpxAdvSysDefaultRouteEnable": wfIpxAdvSysDefaultRouteEnable,
       "wfIpxAdvSysSapViaDefaultRouteEnable": wfIpxAdvSysSapViaDefaultRouteEnable,
       "wfIpxAdvSysCT": wfIpxAdvSysCT,
       "wfIpxAdvSysMibReplySlots": wfIpxAdvSysMibReplySlots,
       "wfIpxAdvSysGNSRespMode": wfIpxAdvSysGNSRespMode,
       "wfIpxAdvSysMaxNetTblSize": wfIpxAdvSysMaxNetTblSize,
       "wfIpxAdvSysNetTblFillNotify": wfIpxAdvSysNetTblFillNotify,
       "wfIpxAdvSysGlobalTrigUpdate": wfIpxAdvSysGlobalTrigUpdate,
       "wfIpxAdvSysTrigUpdateDelay": wfIpxAdvSysTrigUpdateDelay,
       "wfIpxAdvSysLostRouteDelay": wfIpxAdvSysLostRouteDelay,
       "wfIpxCircTable": wfIpxCircTable,
       "wfIpxCircEntry": wfIpxCircEntry,
       "wfIpxCircDelete": wfIpxCircDelete,
       "wfIpxCircDisable": wfIpxCircDisable,
       "wfIpxCircState": wfIpxCircState,
       "wfIpxCircSysInstance": wfIpxCircSysInstance,
       "wfIpxCircIndex": wfIpxCircIndex,
       "wfIpxCircIfIndex": wfIpxCircIfIndex,
       "wfIpxCircName": wfIpxCircName,
       "wfIpxCircCfgType": wfIpxCircCfgType,
       "wfIpxCircLocalMaxPacketSize": wfIpxCircLocalMaxPacketSize,
       "wfIpxCircCfgCompressState": wfIpxCircCfgCompressState,
       "wfIpxCircCompressState": wfIpxCircCompressState,
       "wfIpxCircCompressSlots": wfIpxCircCompressSlots,
       "wfIpxCircCompressedSent": wfIpxCircCompressedSent,
       "wfIpxCircCompressedInitSent": wfIpxCircCompressedInitSent,
       "wfIpxCircCompressedRejectsSent": wfIpxCircCompressedRejectsSent,
       "wfIpxCircUncompressedSent": wfIpxCircUncompressedSent,
       "wfIpxCircCompressedReceived": wfIpxCircCompressedReceived,
       "wfIpxCircCompressedInitReceived": wfIpxCircCompressedInitReceived,
       "wfIpxCircCompressedRejectsReceived": wfIpxCircCompressedRejectsReceived,
       "wfIpxCircUncompressedReceived": wfIpxCircUncompressedReceived,
       "wfIpxCircMediaType": wfIpxCircMediaType,
       "wfIpxCircCfgNetworkNumber": wfIpxCircCfgNetworkNumber,
       "wfIpxCircNetworkNumber": wfIpxCircNetworkNumber,
       "wfIpxCircCommonNetworkNumber": wfIpxCircCommonNetworkNumber,
       "wfIpxCircCfgHostAddress": wfIpxCircCfgHostAddress,
       "wfIpxCircHostAddress": wfIpxCircHostAddress,
       "wfIpxCircMacAddress": wfIpxCircMacAddress,
       "wfIpxCircCfgBroadcastAddress": wfIpxCircCfgBroadcastAddress,
       "wfIpxCircBroadcastAddress": wfIpxCircBroadcastAddress,
       "wfIpxCircCfgMulticastAddress": wfIpxCircCfgMulticastAddress,
       "wfIpxCircMulticastAddress": wfIpxCircMulticastAddress,
       "wfIpxCircStateChanges": wfIpxCircStateChanges,
       "wfIpxCircInitFails": wfIpxCircInitFails,
       "wfIpxCircDelay": wfIpxCircDelay,
       "wfIpxCircThroughput": wfIpxCircThroughput,
       "wfIpxCircNeighRouterName": wfIpxCircNeighRouterName,
       "wfIpxCircNeighInternalNetNum": wfIpxCircNeighInternalNetNum,
       "wfIpxCircCost": wfIpxCircCost,
       "wfIpxCircChecksum": wfIpxCircChecksum,
       "wfIpxCircCfgEncaps": wfIpxCircCfgEncaps,
       "wfIpxCircEncaps": wfIpxCircEncaps,
       "wfIpxCircInTooManyHops": wfIpxCircInTooManyHops,
       "wfIpxCircInFiltered": wfIpxCircInFiltered,
       "wfIpxCircInHdrErrors": wfIpxCircInHdrErrors,
       "wfIpxCircInUnknownSockets": wfIpxCircInUnknownSockets,
       "wfIpxCircNETBIOSPackets": wfIpxCircNETBIOSPackets,
       "wfIpxCircInBadChecksums": wfIpxCircInBadChecksums,
       "wfIpxCircInDelivers": wfIpxCircInDelivers,
       "wfIpxCircInDiscards": wfIpxCircInDiscards,
       "wfIpxCircNoRoutes": wfIpxCircNoRoutes,
       "wfIpxCircOutRequests": wfIpxCircOutRequests,
       "wfIpxCircOutMalformedRequests": wfIpxCircOutMalformedRequests,
       "wfIpxCircOutDiscards": wfIpxCircOutDiscards,
       "wfIpxCircOutFiltered": wfIpxCircOutFiltered,
       "wfIpxCircDestCount": wfIpxCircDestCount,
       "wfIpxCircServCount": wfIpxCircServCount,
       "wfIpxCircHostCount": wfIpxCircHostCount,
       "wfIpxCircForwardCount": wfIpxCircForwardCount,
       "wfIpxCircTrEndStation": wfIpxCircTrEndStation,
       "wfIpxCircNetbiosAccept": wfIpxCircNetbiosAccept,
       "wfIpxCircNetbiosDeliver": wfIpxCircNetbiosDeliver,
       "wfIpxCircSMDSIndividualAddress": wfIpxCircSMDSIndividualAddress,
       "wfIpxCircType": wfIpxCircType,
       "wfIpxCircWatchdogSpoof": wfIpxCircWatchdogSpoof,
       "wfIpxCircIPXOutWatchdogSpoofRsps": wfIpxCircIPXOutWatchdogSpoofRsps,
       "wfIpxCircCfgDelay": wfIpxCircCfgDelay,
       "wfIpxCircCfgThroughput": wfIpxCircCfgThroughput,
       "wfIpxCircSPXOutWatchdogSpoofRsps": wfIpxCircSPXOutWatchdogSpoofRsps,
       "wfIpxCircInitStabilizationTimer": wfIpxCircInitStabilizationTimer,
       "wfIpxCircSVCBroadcast": wfIpxCircSVCBroadcast,
       "wfIpxCircVRRPTriggerState": wfIpxCircVRRPTriggerState,
       "wfIpxDestEntryTable": wfIpxDestEntryTable,
       "wfIpxDestEntry": wfIpxDestEntry,
       "wfIpxDestSysInstance": wfIpxDestSysInstance,
       "wfIpxDestNetNum": wfIpxDestNetNum,
       "wfIpxDestProtocol": wfIpxDestProtocol,
       "wfIpxDestTicks": wfIpxDestTicks,
       "wfIpxDestHopCount": wfIpxDestHopCount,
       "wfIpxDestNextHopCircIndex": wfIpxDestNextHopCircIndex,
       "wfIpxDestNextHopHostAddress": wfIpxDestNextHopHostAddress,
       "wfIpxDestNextHopNetNum": wfIpxDestNextHopNetNum,
       "wfIpxDestAge": wfIpxDestAge,
       "wfIpxUserStaticRouteEntryTable": wfIpxUserStaticRouteEntryTable,
       "wfIpxUserStaticRouteEntry": wfIpxUserStaticRouteEntry,
       "wfIpxUserStaticRouteDelete": wfIpxUserStaticRouteDelete,
       "wfIpxUserStaticRouteDisable": wfIpxUserStaticRouteDisable,
       "wfIpxUserStaticRouteSysInstance": wfIpxUserStaticRouteSysInstance,
       "wfIpxUserStaticRouteCircIndex": wfIpxUserStaticRouteCircIndex,
       "wfIpxUserStaticRouteNetNum": wfIpxUserStaticRouteNetNum,
       "wfIpxUserStaticRouteTicks": wfIpxUserStaticRouteTicks,
       "wfIpxUserStaticRouteHopCount": wfIpxUserStaticRouteHopCount,
       "wfIpxUserStaticRouteNextHopHostAddress": wfIpxUserStaticRouteNextHopHostAddress,
       "wfIpxAutoStaticRouteEntryTable": wfIpxAutoStaticRouteEntryTable,
       "wfIpxAutoStaticRouteEntry": wfIpxAutoStaticRouteEntry,
       "wfIpxAutoStaticRouteDelete": wfIpxAutoStaticRouteDelete,
       "wfIpxAutoStaticRouteDisable": wfIpxAutoStaticRouteDisable,
       "wfIpxAutoStaticRouteSysInstance": wfIpxAutoStaticRouteSysInstance,
       "wfIpxAutoStaticRouteCircIndex": wfIpxAutoStaticRouteCircIndex,
       "wfIpxAutoStaticRouteNetNum": wfIpxAutoStaticRouteNetNum,
       "wfIpxAutoStaticRouteTicks": wfIpxAutoStaticRouteTicks,
       "wfIpxAutoStaticRouteHopCount": wfIpxAutoStaticRouteHopCount,
       "wfIpxAutoStaticRouteNextHopHostAddress": wfIpxAutoStaticRouteNextHopHostAddress,
       "wfIpxStaticRouteMaskEntryTable": wfIpxStaticRouteMaskEntryTable,
       "wfIpxStaticRouteMaskEntry": wfIpxStaticRouteMaskEntry,
       "wfIpxStaticRouteMaskDelete": wfIpxStaticRouteMaskDelete,
       "wfIpxStaticRouteMaskDisable": wfIpxStaticRouteMaskDisable,
       "wfIpxStaticRouteMaskSysInstance": wfIpxStaticRouteMaskSysInstance,
       "wfIpxStaticRouteMaskCircIndex": wfIpxStaticRouteMaskCircIndex,
       "wfIpxStaticRouteMaskNetwork": wfIpxStaticRouteMaskNetwork,
       "wfIpxStaticRouteMaskNetworkMask": wfIpxStaticRouteMaskNetworkMask,
       "wfIpxServEntryTable": wfIpxServEntryTable,
       "wfIpxServEntry": wfIpxServEntry,
       "wfIpxServSysInstance": wfIpxServSysInstance,
       "wfIpxServType": wfIpxServType,
       "wfIpxServName": wfIpxServName,
       "wfIpxServProtocol": wfIpxServProtocol,
       "wfIpxServNetNum": wfIpxServNetNum,
       "wfIpxServNode": wfIpxServNode,
       "wfIpxServSocket": wfIpxServSocket,
       "wfIpxServHopCount": wfIpxServHopCount,
       "wfIpxServNextHopCircIndex": wfIpxServNextHopCircIndex,
       "wfIpxServNextHopHostAddress": wfIpxServNextHopHostAddress,
       "wfIpxServNextHopNetNum": wfIpxServNextHopNetNum,
       "wfIpxServAge": wfIpxServAge,
       "wfIpxUserStaticServEntryTable": wfIpxUserStaticServEntryTable,
       "wfIpxUserStaticServEntry": wfIpxUserStaticServEntry,
       "wfIpxUserStaticServDelete": wfIpxUserStaticServDelete,
       "wfIpxUserStaticServDisable": wfIpxUserStaticServDisable,
       "wfIpxUserStaticServSysInstance": wfIpxUserStaticServSysInstance,
       "wfIpxUserStaticServCircIndex": wfIpxUserStaticServCircIndex,
       "wfIpxUserStaticServName": wfIpxUserStaticServName,
       "wfIpxUserStaticServType": wfIpxUserStaticServType,
       "wfIpxUserStaticServNetNum": wfIpxUserStaticServNetNum,
       "wfIpxUserStaticServHostAddress": wfIpxUserStaticServHostAddress,
       "wfIpxUserStaticServSocket": wfIpxUserStaticServSocket,
       "wfIpxUserStaticServHopCount": wfIpxUserStaticServHopCount,
       "wfIpxAutoStaticServEntryTable": wfIpxAutoStaticServEntryTable,
       "wfIpxAutoStaticServEntry": wfIpxAutoStaticServEntry,
       "wfIpxAutoStaticServDelete": wfIpxAutoStaticServDelete,
       "wfIpxAutoStaticServDisable": wfIpxAutoStaticServDisable,
       "wfIpxAutoStaticServSysInstance": wfIpxAutoStaticServSysInstance,
       "wfIpxAutoStaticServCircIndex": wfIpxAutoStaticServCircIndex,
       "wfIpxAutoStaticServName": wfIpxAutoStaticServName,
       "wfIpxAutoStaticServType": wfIpxAutoStaticServType,
       "wfIpxAutoStaticServNetNum": wfIpxAutoStaticServNetNum,
       "wfIpxAutoStaticServHostAddress": wfIpxAutoStaticServHostAddress,
       "wfIpxAutoStaticServSocket": wfIpxAutoStaticServSocket,
       "wfIpxAutoStaticServHopCount": wfIpxAutoStaticServHopCount,
       "wfIpxStaticServMaskEntryTable": wfIpxStaticServMaskEntryTable,
       "wfIpxStaticServMaskEntry": wfIpxStaticServMaskEntry,
       "wfIpxStaticServMaskDelete": wfIpxStaticServMaskDelete,
       "wfIpxStaticServMaskDisable": wfIpxStaticServMaskDisable,
       "wfIpxStaticServMaskSysInstance": wfIpxStaticServMaskSysInstance,
       "wfIpxStaticServMaskCircIndex": wfIpxStaticServMaskCircIndex,
       "wfIpxStaticServMaskNetwork": wfIpxStaticServMaskNetwork,
       "wfIpxStaticServMaskNetworkMask": wfIpxStaticServMaskNetworkMask,
       "wfIpxStaticHostEntryTable": wfIpxStaticHostEntryTable,
       "wfIpxStaticHostEntry": wfIpxStaticHostEntry,
       "wfIpxStaticHostDelete": wfIpxStaticHostDelete,
       "wfIpxStaticHostDisable": wfIpxStaticHostDisable,
       "wfIpxStaticHostSysInstance": wfIpxStaticHostSysInstance,
       "wfIpxStaticHostCircIndex": wfIpxStaticHostCircIndex,
       "wfIpxStaticHostAddress": wfIpxStaticHostAddress,
       "wfIpxStaticHostWanAddress": wfIpxStaticHostWanAddress,
       "wfIpxStaticHostSubaddress": wfIpxStaticHostSubaddress,
       "wfIpxStaticHostTypeOfNumber": wfIpxStaticHostTypeOfNumber,
       "wfIpxStaticHostType": wfIpxStaticHostType,
       "wfIpxStaticHostGreConnName": wfIpxStaticHostGreConnName,
       "wfIpxUserStaticNETBIOSTable": wfIpxUserStaticNETBIOSTable,
       "wfIpxUserStaticNETBIOSEntry": wfIpxUserStaticNETBIOSEntry,
       "wfIpxUserStaticNETBIOSDelete": wfIpxUserStaticNETBIOSDelete,
       "wfIpxUserStaticNETBIOSDisable": wfIpxUserStaticNETBIOSDisable,
       "wfIpxUserStaticNETBIOSSysInstance": wfIpxUserStaticNETBIOSSysInstance,
       "wfIpxUserStaticNETBIOSName": wfIpxUserStaticNETBIOSName,
       "wfIpxUserStaticNETBIOSDestNetwork": wfIpxUserStaticNETBIOSDestNetwork,
       "wfIpxAutoStaticNETBIOSTable": wfIpxAutoStaticNETBIOSTable,
       "wfIpxAutoStaticNETBIOSEntry": wfIpxAutoStaticNETBIOSEntry,
       "wfIpxAutoStaticNETBIOSDelete": wfIpxAutoStaticNETBIOSDelete,
       "wfIpxAutoStaticNETBIOSDisable": wfIpxAutoStaticNETBIOSDisable,
       "wfIpxAutoStaticNETBIOSSysInstance": wfIpxAutoStaticNETBIOSSysInstance,
       "wfIpxAutoStaticNETBIOSDestNetwork": wfIpxAutoStaticNETBIOSDestNetwork,
       "wfIpxAutoStaticNETBIOSName": wfIpxAutoStaticNETBIOSName,
       "wfIpxRouteFilterTable": wfIpxRouteFilterTable,
       "wfIpxRouteFilterEntry": wfIpxRouteFilterEntry,
       "wfIpxRouteFilterDelete": wfIpxRouteFilterDelete,
       "wfIpxRouteFilterDisable": wfIpxRouteFilterDisable,
       "wfIpxRouteFilterSysInstance": wfIpxRouteFilterSysInstance,
       "wfIpxRouteFilterCircIndex": wfIpxRouteFilterCircIndex,
       "wfIpxRouteFilterRuleNumber": wfIpxRouteFilterRuleNumber,
       "wfIpxRouteFilterNetwork": wfIpxRouteFilterNetwork,
       "wfIpxRouteFilterNetworkMask": wfIpxRouteFilterNetworkMask,
       "wfIpxRouteFilterMode": wfIpxRouteFilterMode,
       "wfIpxRouteFilterAction": wfIpxRouteFilterAction,
       "wfIpxRouteFilterProtocol": wfIpxRouteFilterProtocol,
       "wfIpxRouteFilterCost": wfIpxRouteFilterCost,
       "wfIpxRouteFilterCounter": wfIpxRouteFilterCounter,
       "wfIpxRouteFilterPriority": wfIpxRouteFilterPriority,
       "wfIpxServNetFilterTable": wfIpxServNetFilterTable,
       "wfIpxServNetFilterEntry": wfIpxServNetFilterEntry,
       "wfIpxServNetFilterDelete": wfIpxServNetFilterDelete,
       "wfIpxServNetFilterDisable": wfIpxServNetFilterDisable,
       "wfIpxServNetFilterSysInstance": wfIpxServNetFilterSysInstance,
       "wfIpxServNetFilterCircIndex": wfIpxServNetFilterCircIndex,
       "wfIpxServNetFilterRuleNumber": wfIpxServNetFilterRuleNumber,
       "wfIpxServNetFilterNetwork": wfIpxServNetFilterNetwork,
       "wfIpxServNetFilterNetworkMask": wfIpxServNetFilterNetworkMask,
       "wfIpxServNetFilterType": wfIpxServNetFilterType,
       "wfIpxServNetFilterMode": wfIpxServNetFilterMode,
       "wfIpxServNetFilterAction": wfIpxServNetFilterAction,
       "wfIpxServNetFilterProtocol": wfIpxServNetFilterProtocol,
       "wfIpxServNetFilterCost": wfIpxServNetFilterCost,
       "wfIpxServNetFilterCounter": wfIpxServNetFilterCounter,
       "wfIpxServNetFilterPriority": wfIpxServNetFilterPriority,
       "wfIpxServNameFilterTable": wfIpxServNameFilterTable,
       "wfIpxServNameFilterEntry": wfIpxServNameFilterEntry,
       "wfIpxServNameFilterDelete": wfIpxServNameFilterDelete,
       "wfIpxServNameFilterDisable": wfIpxServNameFilterDisable,
       "wfIpxServNameFilterSysInstance": wfIpxServNameFilterSysInstance,
       "wfIpxServNameFilterCircIndex": wfIpxServNameFilterCircIndex,
       "wfIpxServNameFilterRuleNumber": wfIpxServNameFilterRuleNumber,
       "wfIpxServNameFilterName": wfIpxServNameFilterName,
       "wfIpxServNameFilterType": wfIpxServNameFilterType,
       "wfIpxServNameFilterMode": wfIpxServNameFilterMode,
       "wfIpxServNameFilterAction": wfIpxServNameFilterAction,
       "wfIpxServNameFilterProtocol": wfIpxServNameFilterProtocol,
       "wfIpxServNameFilterCost": wfIpxServNameFilterCost,
       "wfIpxServNameFilterCounter": wfIpxServNameFilterCounter,
       "wfIpxServNameFilterPriority": wfIpxServNameFilterPriority,
       "wfIpxRipCircTable": wfIpxRipCircTable,
       "wfIpxRipCircEntry": wfIpxRipCircEntry,
       "wfIpxRipCircDelete": wfIpxRipCircDelete,
       "wfIpxRipCircDisable": wfIpxRipCircDisable,
       "wfIpxRipCircState": wfIpxRipCircState,
       "wfIpxRipCircSysInstance": wfIpxRipCircSysInstance,
       "wfIpxRipCircIndex": wfIpxRipCircIndex,
       "wfIpxRipCircMode": wfIpxRipCircMode,
       "wfIpxRipCircPace": wfIpxRipCircPace,
       "wfIpxRipCircUpdate": wfIpxRipCircUpdate,
       "wfIpxRipCircAgeMultiplier": wfIpxRipCircAgeMultiplier,
       "wfIpxRipCircPacketSize": wfIpxRipCircPacketSize,
       "wfIpxRipCircOutPackets": wfIpxRipCircOutPackets,
       "wfIpxRipCircInPackets": wfIpxRipCircInPackets,
       "wfIpxRipCircBadPackets": wfIpxRipCircBadPackets,
       "wfIpxRipCircUseMulticast": wfIpxRipCircUseMulticast,
       "wfIpxRipCircSplitHorizon": wfIpxRipCircSplitHorizon,
       "wfIpxRipCircGenAutoStaticRoutes": wfIpxRipCircGenAutoStaticRoutes,
       "wfIpxRipCircImmedUpdate": wfIpxRipCircImmedUpdate,
       "wfIpxRipCircDefaultRouteSupply": wfIpxRipCircDefaultRouteSupply,
       "wfIpxRipCircDefaultRouteListen": wfIpxRipCircDefaultRouteListen,
       "wfIpxRipCircLostRouteDisable": wfIpxRipCircLostRouteDisable,
       "wfIpxSapCircTable": wfIpxSapCircTable,
       "wfIpxSapCircEntry": wfIpxSapCircEntry,
       "wfIpxSapCircDelete": wfIpxSapCircDelete,
       "wfIpxSapCircDisable": wfIpxSapCircDisable,
       "wfIpxSapCircState": wfIpxSapCircState,
       "wfIpxSapCircSysInstance": wfIpxSapCircSysInstance,
       "wfIpxSapCircIndex": wfIpxSapCircIndex,
       "wfIpxSapCircMode": wfIpxSapCircMode,
       "wfIpxSapCircPace": wfIpxSapCircPace,
       "wfIpxSapCircUpdate": wfIpxSapCircUpdate,
       "wfIpxSapCircAgeMultiplier": wfIpxSapCircAgeMultiplier,
       "wfIpxSapCircPacketSize": wfIpxSapCircPacketSize,
       "wfIpxSapCircGetNearestServerReply": wfIpxSapCircGetNearestServerReply,
       "wfIpxSapCircNSQAlphabetical": wfIpxSapCircNSQAlphabetical,
       "wfIpxSapCircOutPackets": wfIpxSapCircOutPackets,
       "wfIpxSapCircInPackets": wfIpxSapCircInPackets,
       "wfIpxSapCircBadPackets": wfIpxSapCircBadPackets,
       "wfIpxSapCircUseMulticast": wfIpxSapCircUseMulticast,
       "wfIpxSapCircSplitHorizon": wfIpxSapCircSplitHorizon,
       "wfIpxSapCircGenAutoStaticServices": wfIpxSapCircGenAutoStaticServices,
       "wfIpxSapCircImmedUpdate": wfIpxSapCircImmedUpdate,
       "wfIpxSapCircSaveFullName": wfIpxSapCircSaveFullName,
       "wfIpxHostEntryTable": wfIpxHostEntryTable,
       "wfIpxHostEntry": wfIpxHostEntry,
       "wfIpxHostSysInstance": wfIpxHostSysInstance,
       "wfIpxHostNextHopCircIndex": wfIpxHostNextHopCircIndex,
       "wfIpxHostHostAddress": wfIpxHostHostAddress,
       "wfIpxHostNetNum": wfIpxHostNetNum,
       "wfIpxHostWanAddress": wfIpxHostWanAddress,
       "wfIpxHostProtocol": wfIpxHostProtocol,
       "wfIpxHostAge": wfIpxHostAge,
       "wfIpxForwardEntryTable": wfIpxForwardEntryTable,
       "wfIpxForwardEntry": wfIpxForwardEntry,
       "wfIpxForwardSysInstance": wfIpxForwardSysInstance,
       "wfIpxForwardCircIndex": wfIpxForwardCircIndex,
       "wfIpxForwardNetNum": wfIpxForwardNetNum,
       "wfIpxForwardType": wfIpxForwardType,
       "wfIpxForwardProtocol": wfIpxForwardProtocol,
       "wfIpxForwardCount": wfIpxForwardCount,
       "wfIpxTrafficFilter2Table": wfIpxTrafficFilter2Table,
       "wfIpxTrafficFilter2Entry": wfIpxTrafficFilter2Entry,
       "wfIpxTrafficFilter2Create": wfIpxTrafficFilter2Create,
       "wfIpxTrafficFilter2Enable": wfIpxTrafficFilter2Enable,
       "wfIpxTrafficFilter2Status": wfIpxTrafficFilter2Status,
       "wfIpxTrafficFilter2Counter": wfIpxTrafficFilter2Counter,
       "wfIpxTrafficFilter2Definition": wfIpxTrafficFilter2Definition,
       "wfIpxTrafficFilter2Reserved": wfIpxTrafficFilter2Reserved,
       "wfIpxTrafficFilter2SysInstance": wfIpxTrafficFilter2SysInstance,
       "wfIpxTrafficFilter2CircIndex": wfIpxTrafficFilter2CircIndex,
       "wfIpxTrafficFilter2RuleNumber": wfIpxTrafficFilter2RuleNumber,
       "wfIpxTrafficFilter2Fragment": wfIpxTrafficFilter2Fragment,
       "wfIpxTrafficFilter2Name": wfIpxTrafficFilter2Name}
)
