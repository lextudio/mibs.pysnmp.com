# SNMP MIB module (Wellfleet-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:24 2024
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

(wfIgmpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIgmpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIgmpBase_ObjectIdentity = ObjectIdentity
wfIgmpBase = _WfIgmpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1)
)


class _WfIgmpBaseCreate_Type(Integer32):
    """Custom type wfIgmpBaseCreate based on Integer32"""
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


_WfIgmpBaseCreate_Type.__name__ = "Integer32"
_WfIgmpBaseCreate_Object = MibScalar
wfIgmpBaseCreate = _WfIgmpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 1),
    _WfIgmpBaseCreate_Type()
)
wfIgmpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseCreate.setStatus("mandatory")


class _WfIgmpBaseEnable_Type(Integer32):
    """Custom type wfIgmpBaseEnable based on Integer32"""
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


_WfIgmpBaseEnable_Type.__name__ = "Integer32"
_WfIgmpBaseEnable_Object = MibScalar
wfIgmpBaseEnable = _WfIgmpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 2),
    _WfIgmpBaseEnable_Type()
)
wfIgmpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseEnable.setStatus("mandatory")


class _WfIgmpBaseState_Type(Integer32):
    """Custom type wfIgmpBaseState based on Integer32"""
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
          ("notpres", 4),
          ("up", 1))
    )


_WfIgmpBaseState_Type.__name__ = "Integer32"
_WfIgmpBaseState_Object = MibScalar
wfIgmpBaseState = _WfIgmpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 3),
    _WfIgmpBaseState_Type()
)
wfIgmpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpBaseState.setStatus("mandatory")


class _WfIgmpBaseEstimatedGroups_Type(Integer32):
    """Custom type wfIgmpBaseEstimatedGroups based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WfIgmpBaseEstimatedGroups_Type.__name__ = "Integer32"
_WfIgmpBaseEstimatedGroups_Object = MibScalar
wfIgmpBaseEstimatedGroups = _WfIgmpBaseEstimatedGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 4),
    _WfIgmpBaseEstimatedGroups_Type()
)
wfIgmpBaseEstimatedGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseEstimatedGroups.setStatus("mandatory")


class _WfIgmpBaseVersionThreshold_Type(Integer32):
    """Custom type wfIgmpBaseVersionThreshold based on Integer32"""
    defaultValue = 540

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfIgmpBaseVersionThreshold_Type.__name__ = "Integer32"
_WfIgmpBaseVersionThreshold_Object = MibScalar
wfIgmpBaseVersionThreshold = _WfIgmpBaseVersionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 5),
    _WfIgmpBaseVersionThreshold_Type()
)
wfIgmpBaseVersionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseVersionThreshold.setStatus("mandatory")
_WfIgmpBaseDebug_Type = Integer32
_WfIgmpBaseDebug_Object = MibScalar
wfIgmpBaseDebug = _WfIgmpBaseDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 6),
    _WfIgmpBaseDebug_Type()
)
wfIgmpBaseDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseDebug.setStatus("mandatory")


class _WfIgmpBaseJoinAckEnable_Type(Integer32):
    """Custom type wfIgmpBaseJoinAckEnable based on Integer32"""
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


_WfIgmpBaseJoinAckEnable_Type.__name__ = "Integer32"
_WfIgmpBaseJoinAckEnable_Object = MibScalar
wfIgmpBaseJoinAckEnable = _WfIgmpBaseJoinAckEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 7),
    _WfIgmpBaseJoinAckEnable_Type()
)
wfIgmpBaseJoinAckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseJoinAckEnable.setStatus("mandatory")


class _WfIgmpBaseFwdCacheLimit_Type(Integer32):
    """Custom type wfIgmpBaseFwdCacheLimit based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_WfIgmpBaseFwdCacheLimit_Type.__name__ = "Integer32"
_WfIgmpBaseFwdCacheLimit_Object = MibScalar
wfIgmpBaseFwdCacheLimit = _WfIgmpBaseFwdCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 8),
    _WfIgmpBaseFwdCacheLimit_Type()
)
wfIgmpBaseFwdCacheLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseFwdCacheLimit.setStatus("mandatory")


class _WfIgmpBaseIgnoreNonLocalReport_Type(Integer32):
    """Custom type wfIgmpBaseIgnoreNonLocalReport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("ignore", 1))
    )


_WfIgmpBaseIgnoreNonLocalReport_Type.__name__ = "Integer32"
_WfIgmpBaseIgnoreNonLocalReport_Object = MibScalar
wfIgmpBaseIgnoreNonLocalReport = _WfIgmpBaseIgnoreNonLocalReport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 9),
    _WfIgmpBaseIgnoreNonLocalReport_Type()
)
wfIgmpBaseIgnoreNonLocalReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseIgnoreNonLocalReport.setStatus("mandatory")


class _WfIgmpBaseRelayEnable_Type(Integer32):
    """Custom type wfIgmpBaseRelayEnable based on Integer32"""
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


_WfIgmpBaseRelayEnable_Type.__name__ = "Integer32"
_WfIgmpBaseRelayEnable_Object = MibScalar
wfIgmpBaseRelayEnable = _WfIgmpBaseRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 10),
    _WfIgmpBaseRelayEnable_Type()
)
wfIgmpBaseRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseRelayEnable.setStatus("mandatory")


class _WfIgmpBaseRelayTimeoutValue_Type(Integer32):
    """Custom type wfIgmpBaseRelayTimeoutValue based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIgmpBaseRelayTimeoutValue_Type.__name__ = "Integer32"
_WfIgmpBaseRelayTimeoutValue_Object = MibScalar
wfIgmpBaseRelayTimeoutValue = _WfIgmpBaseRelayTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 11),
    _WfIgmpBaseRelayTimeoutValue_Type()
)
wfIgmpBaseRelayTimeoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseRelayTimeoutValue.setStatus("mandatory")


class _WfIgmpBaseRelayFwdOptions_Type(Integer32):
    """Custom type wfIgmpBaseRelayFwdOptions based on Integer32"""
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
        *(("backup", 2),
          ("both", 3),
          ("primary", 1))
    )


_WfIgmpBaseRelayFwdOptions_Type.__name__ = "Integer32"
_WfIgmpBaseRelayFwdOptions_Object = MibScalar
wfIgmpBaseRelayFwdOptions = _WfIgmpBaseRelayFwdOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 12),
    _WfIgmpBaseRelayFwdOptions_Type()
)
wfIgmpBaseRelayFwdOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBaseRelayFwdOptions.setStatus("mandatory")
_WfIgmpBaseGroupCount_Type = Counter32
_WfIgmpBaseGroupCount_Object = MibScalar
wfIgmpBaseGroupCount = _WfIgmpBaseGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 13),
    _WfIgmpBaseGroupCount_Type()
)
wfIgmpBaseGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpBaseGroupCount.setStatus("mandatory")


class _WfIgmpBasePerStreamRedundEnable_Type(Integer32):
    """Custom type wfIgmpBasePerStreamRedundEnable based on Integer32"""
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


_WfIgmpBasePerStreamRedundEnable_Type.__name__ = "Integer32"
_WfIgmpBasePerStreamRedundEnable_Object = MibScalar
wfIgmpBasePerStreamRedundEnable = _WfIgmpBasePerStreamRedundEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 14),
    _WfIgmpBasePerStreamRedundEnable_Type()
)
wfIgmpBasePerStreamRedundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBasePerStreamRedundEnable.setStatus("mandatory")
_WfIgmpIfTable_Object = MibTable
wfIgmpIfTable = _WfIgmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2)
)
if mibBuilder.loadTexts:
    wfIgmpIfTable.setStatus("mandatory")
_WfIgmpIfEntry_Object = MibTableRow
wfIgmpIfEntry = _WfIgmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1)
)
wfIgmpIfEntry.setIndexNames(
    (0, "Wellfleet-IGMP-MIB", "wfIgmpIfCctno"),
)
if mibBuilder.loadTexts:
    wfIgmpIfEntry.setStatus("mandatory")


class _WfIgmpIfCreate_Type(Integer32):
    """Custom type wfIgmpIfCreate based on Integer32"""
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


_WfIgmpIfCreate_Type.__name__ = "Integer32"
_WfIgmpIfCreate_Object = MibTableColumn
wfIgmpIfCreate = _WfIgmpIfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 1),
    _WfIgmpIfCreate_Type()
)
wfIgmpIfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfCreate.setStatus("mandatory")


class _WfIgmpIfEnable_Type(Integer32):
    """Custom type wfIgmpIfEnable based on Integer32"""
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


_WfIgmpIfEnable_Type.__name__ = "Integer32"
_WfIgmpIfEnable_Object = MibTableColumn
wfIgmpIfEnable = _WfIgmpIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 2),
    _WfIgmpIfEnable_Type()
)
wfIgmpIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfEnable.setStatus("mandatory")


class _WfIgmpIfState_Type(Integer32):
    """Custom type wfIgmpIfState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfIgmpIfState_Type.__name__ = "Integer32"
_WfIgmpIfState_Object = MibTableColumn
wfIgmpIfState = _WfIgmpIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 3),
    _WfIgmpIfState_Type()
)
wfIgmpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfState.setStatus("mandatory")
_WfIgmpDesignatedRouter_Type = IpAddress
_WfIgmpDesignatedRouter_Object = MibTableColumn
wfIgmpDesignatedRouter = _WfIgmpDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 4),
    _WfIgmpDesignatedRouter_Type()
)
wfIgmpDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpDesignatedRouter.setStatus("mandatory")


class _WfIgmpIfQueryRate_Type(Integer32):
    """Custom type wfIgmpIfQueryRate based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_WfIgmpIfQueryRate_Type.__name__ = "Integer32"
_WfIgmpIfQueryRate_Object = MibTableColumn
wfIgmpIfQueryRate = _WfIgmpIfQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 5),
    _WfIgmpIfQueryRate_Type()
)
wfIgmpIfQueryRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfQueryRate.setStatus("mandatory")


class _WfIgmpIfMembershipTimeout_Type(Integer32):
    """Custom type wfIgmpIfMembershipTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 8192),
    )


_WfIgmpIfMembershipTimeout_Type.__name__ = "Integer32"
_WfIgmpIfMembershipTimeout_Object = MibTableColumn
wfIgmpIfMembershipTimeout = _WfIgmpIfMembershipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 6),
    _WfIgmpIfMembershipTimeout_Type()
)
wfIgmpIfMembershipTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfMembershipTimeout.setStatus("mandatory")


class _WfIgmpIfDRTimeout_Type(Integer32):
    """Custom type wfIgmpIfDRTimeout based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 8192),
    )


_WfIgmpIfDRTimeout_Type.__name__ = "Integer32"
_WfIgmpIfDRTimeout_Object = MibTableColumn
wfIgmpIfDRTimeout = _WfIgmpIfDRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 7),
    _WfIgmpIfDRTimeout_Type()
)
wfIgmpIfDRTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfDRTimeout.setStatus("mandatory")
_WfIgmpIfLocalIpAddress_Type = IpAddress
_WfIgmpIfLocalIpAddress_Object = MibTableColumn
wfIgmpIfLocalIpAddress = _WfIgmpIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 8),
    _WfIgmpIfLocalIpAddress_Type()
)
wfIgmpIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfLocalIpAddress.setStatus("mandatory")
_WfIgmpIfCctno_Type = Integer32
_WfIgmpIfCctno_Object = MibTableColumn
wfIgmpIfCctno = _WfIgmpIfCctno_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 9),
    _WfIgmpIfCctno_Type()
)
wfIgmpIfCctno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfCctno.setStatus("mandatory")
_WfIgmpIfInDatagrams_Type = Counter32
_WfIgmpIfInDatagrams_Object = MibTableColumn
wfIgmpIfInDatagrams = _WfIgmpIfInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 10),
    _WfIgmpIfInDatagrams_Type()
)
wfIgmpIfInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfInDatagrams.setStatus("mandatory")
_WfIgmpIfOutQueries_Type = Counter32
_WfIgmpIfOutQueries_Object = MibTableColumn
wfIgmpIfOutQueries = _WfIgmpIfOutQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 11),
    _WfIgmpIfOutQueries_Type()
)
wfIgmpIfOutQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfOutQueries.setStatus("mandatory")
_WfIgmpIfInQueries_Type = Counter32
_WfIgmpIfInQueries_Object = MibTableColumn
wfIgmpIfInQueries = _WfIgmpIfInQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 12),
    _WfIgmpIfInQueries_Type()
)
wfIgmpIfInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfInQueries.setStatus("mandatory")
_WfIgmpIfDiscards_Type = Counter32
_WfIgmpIfDiscards_Object = MibTableColumn
wfIgmpIfDiscards = _WfIgmpIfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 13),
    _WfIgmpIfDiscards_Type()
)
wfIgmpIfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfDiscards.setStatus("mandatory")
_WfIgmpIfNetVersion_Type = Integer32
_WfIgmpIfNetVersion_Object = MibTableColumn
wfIgmpIfNetVersion = _WfIgmpIfNetVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 14),
    _WfIgmpIfNetVersion_Type()
)
wfIgmpIfNetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfNetVersion.setStatus("mandatory")


class _WfIgmpIfMaxHostResponse_Type(Integer32):
    """Custom type wfIgmpIfMaxHostResponse based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfIgmpIfMaxHostResponse_Type.__name__ = "Integer32"
_WfIgmpIfMaxHostResponse_Object = MibTableColumn
wfIgmpIfMaxHostResponse = _WfIgmpIfMaxHostResponse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 15),
    _WfIgmpIfMaxHostResponse_Type()
)
wfIgmpIfMaxHostResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfMaxHostResponse.setStatus("mandatory")


class _WfIgmpIfRoutingProtocol_Type(Integer32):
    """Custom type wfIgmpIfRoutingProtocol based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cbt", 5),
          ("dvmrp", 2),
          ("igmp", 1),
          ("internal", 6),
          ("mospf", 4),
          ("pim", 3),
          ("relay", 7))
    )


_WfIgmpIfRoutingProtocol_Type.__name__ = "Integer32"
_WfIgmpIfRoutingProtocol_Object = MibTableColumn
wfIgmpIfRoutingProtocol = _WfIgmpIfRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 16),
    _WfIgmpIfRoutingProtocol_Type()
)
wfIgmpIfRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfRoutingProtocol.setStatus("mandatory")
_WfIgmpIfDroppedDataPkt_Type = Counter32
_WfIgmpIfDroppedDataPkt_Object = MibTableColumn
wfIgmpIfDroppedDataPkt = _WfIgmpIfDroppedDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 17),
    _WfIgmpIfDroppedDataPkt_Type()
)
wfIgmpIfDroppedDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfDroppedDataPkt.setStatus("mandatory")


class _WfIgmpIfMtraceEntryLifetime_Type(Integer32):
    """Custom type wfIgmpIfMtraceEntryLifetime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 8192),
    )


_WfIgmpIfMtraceEntryLifetime_Type.__name__ = "Integer32"
_WfIgmpIfMtraceEntryLifetime_Object = MibTableColumn
wfIgmpIfMtraceEntryLifetime = _WfIgmpIfMtraceEntryLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 18),
    _WfIgmpIfMtraceEntryLifetime_Type()
)
wfIgmpIfMtraceEntryLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfMtraceEntryLifetime.setStatus("mandatory")
_WfIgmpIfInMtraceReqs_Type = Counter32
_WfIgmpIfInMtraceReqs_Object = MibTableColumn
wfIgmpIfInMtraceReqs = _WfIgmpIfInMtraceReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 19),
    _WfIgmpIfInMtraceReqs_Type()
)
wfIgmpIfInMtraceReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfInMtraceReqs.setStatus("mandatory")
_WfIgmpIfOutMtraceReqs_Type = Counter32
_WfIgmpIfOutMtraceReqs_Object = MibTableColumn
wfIgmpIfOutMtraceReqs = _WfIgmpIfOutMtraceReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 20),
    _WfIgmpIfOutMtraceReqs_Type()
)
wfIgmpIfOutMtraceReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfOutMtraceReqs.setStatus("mandatory")
_WfIgmpIfInMtraceResps_Type = Counter32
_WfIgmpIfInMtraceResps_Object = MibTableColumn
wfIgmpIfInMtraceResps = _WfIgmpIfInMtraceResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 21),
    _WfIgmpIfInMtraceResps_Type()
)
wfIgmpIfInMtraceResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfInMtraceResps.setStatus("mandatory")
_WfIgmpIfOutMtraceResps_Type = Counter32
_WfIgmpIfOutMtraceResps_Object = MibTableColumn
wfIgmpIfOutMtraceResps = _WfIgmpIfOutMtraceResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 22),
    _WfIgmpIfOutMtraceResps_Type()
)
wfIgmpIfOutMtraceResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfOutMtraceResps.setStatus("mandatory")


class _WfIgmpIfRelayType_Type(Integer32):
    """Custom type wfIgmpIfRelayType based on Integer32"""
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
        *(("backup", 2),
          ("downstream", 3),
          ("primary", 1))
    )


_WfIgmpIfRelayType_Type.__name__ = "Integer32"
_WfIgmpIfRelayType_Object = MibTableColumn
wfIgmpIfRelayType = _WfIgmpIfRelayType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 23),
    _WfIgmpIfRelayType_Type()
)
wfIgmpIfRelayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfRelayType.setStatus("mandatory")


class _WfIgmpIfUnsolicitedReportInterval_Type(Integer32):
    """Custom type wfIgmpIfUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIgmpIfUnsolicitedReportInterval_Type.__name__ = "Integer32"
_WfIgmpIfUnsolicitedReportInterval_Object = MibTableColumn
wfIgmpIfUnsolicitedReportInterval = _WfIgmpIfUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 24),
    _WfIgmpIfUnsolicitedReportInterval_Type()
)
wfIgmpIfUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfUnsolicitedReportInterval.setStatus("mandatory")


class _WfIgmpIfSuppressQuery_Type(Integer32):
    """Custom type wfIgmpIfSuppressQuery based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfIgmpIfSuppressQuery_Type.__name__ = "Integer32"
_WfIgmpIfSuppressQuery_Object = MibTableColumn
wfIgmpIfSuppressQuery = _WfIgmpIfSuppressQuery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 25),
    _WfIgmpIfSuppressQuery_Type()
)
wfIgmpIfSuppressQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfSuppressQuery.setStatus("mandatory")
_WfIgmpIfGroupCount_Type = Counter32
_WfIgmpIfGroupCount_Object = MibTableColumn
wfIgmpIfGroupCount = _WfIgmpIfGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 26),
    _WfIgmpIfGroupCount_Type()
)
wfIgmpIfGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfGroupCount.setStatus("mandatory")


class _WfIgmpIfVRRPTriggerState_Type(Integer32):
    """Custom type wfIgmpIfVRRPTriggerState based on Integer32"""
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


_WfIgmpIfVRRPTriggerState_Type.__name__ = "Integer32"
_WfIgmpIfVRRPTriggerState_Object = MibTableColumn
wfIgmpIfVRRPTriggerState = _WfIgmpIfVRRPTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 27),
    _WfIgmpIfVRRPTriggerState_Type()
)
wfIgmpIfVRRPTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIfVRRPTriggerState.setStatus("mandatory")


class _WfIgmpIfStaticFwdCacheLifeTime_Type(Integer32):
    """Custom type wfIgmpIfStaticFwdCacheLifeTime based on Integer32"""
    defaultValue = 216

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 7200),
    )


_WfIgmpIfStaticFwdCacheLifeTime_Type.__name__ = "Integer32"
_WfIgmpIfStaticFwdCacheLifeTime_Object = MibTableColumn
wfIgmpIfStaticFwdCacheLifeTime = _WfIgmpIfStaticFwdCacheLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 28),
    _WfIgmpIfStaticFwdCacheLifeTime_Type()
)
wfIgmpIfStaticFwdCacheLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpIfStaticFwdCacheLifeTime.setStatus("mandatory")
_WfIgmpGroupTable_Object = MibTable
wfIgmpGroupTable = _WfIgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3)
)
if mibBuilder.loadTexts:
    wfIgmpGroupTable.setStatus("mandatory")
_WfIgmpGroupEntry_Object = MibTableRow
wfIgmpGroupEntry = _WfIgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1)
)
wfIgmpGroupEntry.setIndexNames(
    (0, "Wellfleet-IGMP-MIB", "wfIgmpCct"),
    (0, "Wellfleet-IGMP-MIB", "wfIgmpIpifAddress"),
    (0, "Wellfleet-IGMP-MIB", "wfIgmpGroupAddress"),
)
if mibBuilder.loadTexts:
    wfIgmpGroupEntry.setStatus("mandatory")
_WfIgmpGroupAddress_Type = IpAddress
_WfIgmpGroupAddress_Object = MibTableColumn
wfIgmpGroupAddress = _WfIgmpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 1),
    _WfIgmpGroupAddress_Type()
)
wfIgmpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpGroupAddress.setStatus("mandatory")
_WfIgmpCct_Type = Integer32
_WfIgmpCct_Object = MibTableColumn
wfIgmpCct = _WfIgmpCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 2),
    _WfIgmpCct_Type()
)
wfIgmpCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpCct.setStatus("mandatory")
_WfIgmpIpifAddress_Type = IpAddress
_WfIgmpIpifAddress_Object = MibTableColumn
wfIgmpIpifAddress = _WfIgmpIpifAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 3),
    _WfIgmpIpifAddress_Type()
)
wfIgmpIpifAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpIpifAddress.setStatus("mandatory")
_WfIgmpTimeLeft_Type = Integer32
_WfIgmpTimeLeft_Object = MibTableColumn
wfIgmpTimeLeft = _WfIgmpTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 4),
    _WfIgmpTimeLeft_Type()
)
wfIgmpTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpTimeLeft.setStatus("mandatory")
_WfIgmpStaticGroupTable_Object = MibTable
wfIgmpStaticGroupTable = _WfIgmpStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4)
)
if mibBuilder.loadTexts:
    wfIgmpStaticGroupTable.setStatus("mandatory")
_WfIgmpStaticGroupEntry_Object = MibTableRow
wfIgmpStaticGroupEntry = _WfIgmpStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1)
)
wfIgmpStaticGroupEntry.setIndexNames(
    (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupCct"),
    (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupAddress"),
    (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupPrefix"),
)
if mibBuilder.loadTexts:
    wfIgmpStaticGroupEntry.setStatus("mandatory")


class _WfIgmpStaticGroupCreate_Type(Integer32):
    """Custom type wfIgmpStaticGroupCreate based on Integer32"""
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


_WfIgmpStaticGroupCreate_Type.__name__ = "Integer32"
_WfIgmpStaticGroupCreate_Object = MibTableColumn
wfIgmpStaticGroupCreate = _WfIgmpStaticGroupCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 1),
    _WfIgmpStaticGroupCreate_Type()
)
wfIgmpStaticGroupCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpStaticGroupCreate.setStatus("mandatory")
_WfIgmpStaticGroupCct_Type = Integer32
_WfIgmpStaticGroupCct_Object = MibTableColumn
wfIgmpStaticGroupCct = _WfIgmpStaticGroupCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 2),
    _WfIgmpStaticGroupCct_Type()
)
wfIgmpStaticGroupCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpStaticGroupCct.setStatus("mandatory")
_WfIgmpStaticGroupAddress_Type = IpAddress
_WfIgmpStaticGroupAddress_Object = MibTableColumn
wfIgmpStaticGroupAddress = _WfIgmpStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 3),
    _WfIgmpStaticGroupAddress_Type()
)
wfIgmpStaticGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpStaticGroupAddress.setStatus("mandatory")
_WfIgmpStaticGroupPrefix_Type = Integer32
_WfIgmpStaticGroupPrefix_Object = MibTableColumn
wfIgmpStaticGroupPrefix = _WfIgmpStaticGroupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 4),
    _WfIgmpStaticGroupPrefix_Type()
)
wfIgmpStaticGroupPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpStaticGroupPrefix.setStatus("mandatory")
_WfIgmpBoundaryTable_Object = MibTable
wfIgmpBoundaryTable = _WfIgmpBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5)
)
if mibBuilder.loadTexts:
    wfIgmpBoundaryTable.setStatus("mandatory")
_WfIgmpBoundaryEntry_Object = MibTableRow
wfIgmpBoundaryEntry = _WfIgmpBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1)
)
wfIgmpBoundaryEntry.setIndexNames(
    (0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupAddress"),
    (0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupPrefix"),
)
if mibBuilder.loadTexts:
    wfIgmpBoundaryEntry.setStatus("mandatory")


class _WfIgmpBoundaryCreate_Type(Integer32):
    """Custom type wfIgmpBoundaryCreate based on Integer32"""
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


_WfIgmpBoundaryCreate_Type.__name__ = "Integer32"
_WfIgmpBoundaryCreate_Object = MibTableColumn
wfIgmpBoundaryCreate = _WfIgmpBoundaryCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 1),
    _WfIgmpBoundaryCreate_Type()
)
wfIgmpBoundaryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBoundaryCreate.setStatus("mandatory")


class _WfIgmpBoundaryEnable_Type(Integer32):
    """Custom type wfIgmpBoundaryEnable based on Integer32"""
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


_WfIgmpBoundaryEnable_Type.__name__ = "Integer32"
_WfIgmpBoundaryEnable_Object = MibTableColumn
wfIgmpBoundaryEnable = _WfIgmpBoundaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 2),
    _WfIgmpBoundaryEnable_Type()
)
wfIgmpBoundaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBoundaryEnable.setStatus("mandatory")
_WfIgmpBoundaryGroupAddress_Type = IpAddress
_WfIgmpBoundaryGroupAddress_Object = MibTableColumn
wfIgmpBoundaryGroupAddress = _WfIgmpBoundaryGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 3),
    _WfIgmpBoundaryGroupAddress_Type()
)
wfIgmpBoundaryGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpBoundaryGroupAddress.setStatus("mandatory")
_WfIgmpBoundaryGroupPrefix_Type = Integer32
_WfIgmpBoundaryGroupPrefix_Object = MibTableColumn
wfIgmpBoundaryGroupPrefix = _WfIgmpBoundaryGroupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 4),
    _WfIgmpBoundaryGroupPrefix_Type()
)
wfIgmpBoundaryGroupPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIgmpBoundaryGroupPrefix.setStatus("mandatory")
_WfIgmpBoundaryCctList_Type = OctetString
_WfIgmpBoundaryCctList_Object = MibTableColumn
wfIgmpBoundaryCctList = _WfIgmpBoundaryCctList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 5),
    _WfIgmpBoundaryCctList_Type()
)
wfIgmpBoundaryCctList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBoundaryCctList.setStatus("mandatory")
_WfIgmpBoundaryTunnelList_Type = OctetString
_WfIgmpBoundaryTunnelList_Object = MibTableColumn
wfIgmpBoundaryTunnelList = _WfIgmpBoundaryTunnelList_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 6),
    _WfIgmpBoundaryTunnelList_Type()
)
wfIgmpBoundaryTunnelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpBoundaryTunnelList.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IGMP-MIB",
    **{"wfIgmpBase": wfIgmpBase,
       "wfIgmpBaseCreate": wfIgmpBaseCreate,
       "wfIgmpBaseEnable": wfIgmpBaseEnable,
       "wfIgmpBaseState": wfIgmpBaseState,
       "wfIgmpBaseEstimatedGroups": wfIgmpBaseEstimatedGroups,
       "wfIgmpBaseVersionThreshold": wfIgmpBaseVersionThreshold,
       "wfIgmpBaseDebug": wfIgmpBaseDebug,
       "wfIgmpBaseJoinAckEnable": wfIgmpBaseJoinAckEnable,
       "wfIgmpBaseFwdCacheLimit": wfIgmpBaseFwdCacheLimit,
       "wfIgmpBaseIgnoreNonLocalReport": wfIgmpBaseIgnoreNonLocalReport,
       "wfIgmpBaseRelayEnable": wfIgmpBaseRelayEnable,
       "wfIgmpBaseRelayTimeoutValue": wfIgmpBaseRelayTimeoutValue,
       "wfIgmpBaseRelayFwdOptions": wfIgmpBaseRelayFwdOptions,
       "wfIgmpBaseGroupCount": wfIgmpBaseGroupCount,
       "wfIgmpBasePerStreamRedundEnable": wfIgmpBasePerStreamRedundEnable,
       "wfIgmpIfTable": wfIgmpIfTable,
       "wfIgmpIfEntry": wfIgmpIfEntry,
       "wfIgmpIfCreate": wfIgmpIfCreate,
       "wfIgmpIfEnable": wfIgmpIfEnable,
       "wfIgmpIfState": wfIgmpIfState,
       "wfIgmpDesignatedRouter": wfIgmpDesignatedRouter,
       "wfIgmpIfQueryRate": wfIgmpIfQueryRate,
       "wfIgmpIfMembershipTimeout": wfIgmpIfMembershipTimeout,
       "wfIgmpIfDRTimeout": wfIgmpIfDRTimeout,
       "wfIgmpIfLocalIpAddress": wfIgmpIfLocalIpAddress,
       "wfIgmpIfCctno": wfIgmpIfCctno,
       "wfIgmpIfInDatagrams": wfIgmpIfInDatagrams,
       "wfIgmpIfOutQueries": wfIgmpIfOutQueries,
       "wfIgmpIfInQueries": wfIgmpIfInQueries,
       "wfIgmpIfDiscards": wfIgmpIfDiscards,
       "wfIgmpIfNetVersion": wfIgmpIfNetVersion,
       "wfIgmpIfMaxHostResponse": wfIgmpIfMaxHostResponse,
       "wfIgmpIfRoutingProtocol": wfIgmpIfRoutingProtocol,
       "wfIgmpIfDroppedDataPkt": wfIgmpIfDroppedDataPkt,
       "wfIgmpIfMtraceEntryLifetime": wfIgmpIfMtraceEntryLifetime,
       "wfIgmpIfInMtraceReqs": wfIgmpIfInMtraceReqs,
       "wfIgmpIfOutMtraceReqs": wfIgmpIfOutMtraceReqs,
       "wfIgmpIfInMtraceResps": wfIgmpIfInMtraceResps,
       "wfIgmpIfOutMtraceResps": wfIgmpIfOutMtraceResps,
       "wfIgmpIfRelayType": wfIgmpIfRelayType,
       "wfIgmpIfUnsolicitedReportInterval": wfIgmpIfUnsolicitedReportInterval,
       "wfIgmpIfSuppressQuery": wfIgmpIfSuppressQuery,
       "wfIgmpIfGroupCount": wfIgmpIfGroupCount,
       "wfIgmpIfVRRPTriggerState": wfIgmpIfVRRPTriggerState,
       "wfIgmpIfStaticFwdCacheLifeTime": wfIgmpIfStaticFwdCacheLifeTime,
       "wfIgmpGroupTable": wfIgmpGroupTable,
       "wfIgmpGroupEntry": wfIgmpGroupEntry,
       "wfIgmpGroupAddress": wfIgmpGroupAddress,
       "wfIgmpCct": wfIgmpCct,
       "wfIgmpIpifAddress": wfIgmpIpifAddress,
       "wfIgmpTimeLeft": wfIgmpTimeLeft,
       "wfIgmpStaticGroupTable": wfIgmpStaticGroupTable,
       "wfIgmpStaticGroupEntry": wfIgmpStaticGroupEntry,
       "wfIgmpStaticGroupCreate": wfIgmpStaticGroupCreate,
       "wfIgmpStaticGroupCct": wfIgmpStaticGroupCct,
       "wfIgmpStaticGroupAddress": wfIgmpStaticGroupAddress,
       "wfIgmpStaticGroupPrefix": wfIgmpStaticGroupPrefix,
       "wfIgmpBoundaryTable": wfIgmpBoundaryTable,
       "wfIgmpBoundaryEntry": wfIgmpBoundaryEntry,
       "wfIgmpBoundaryCreate": wfIgmpBoundaryCreate,
       "wfIgmpBoundaryEnable": wfIgmpBoundaryEnable,
       "wfIgmpBoundaryGroupAddress": wfIgmpBoundaryGroupAddress,
       "wfIgmpBoundaryGroupPrefix": wfIgmpBoundaryGroupPrefix,
       "wfIgmpBoundaryCctList": wfIgmpBoundaryCctList,
       "wfIgmpBoundaryTunnelList": wfIgmpBoundaryTunnelList}
)
