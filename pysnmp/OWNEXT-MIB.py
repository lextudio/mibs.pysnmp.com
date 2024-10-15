# SNMP MIB module (OWNEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OWNEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:51 2024
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

(ownExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "ownExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apOwnExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApOwnTable_Object = MibTable
apOwnTable = _ApOwnTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2)
)
if mibBuilder.loadTexts:
    apOwnTable.setStatus("current")
_ApOwnEntry_Object = MibTableRow
apOwnEntry = _ApOwnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1)
)
apOwnEntry.setIndexNames(
    (0, "OWNEXT-MIB", "apOwnName"),
)
if mibBuilder.loadTexts:
    apOwnEntry.setStatus("current")


class _ApOwnName_Type(DisplayString):
    """Custom type apOwnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApOwnName_Type.__name__ = "DisplayString"
_ApOwnName_Object = MibTableColumn
apOwnName = _ApOwnName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 1),
    _ApOwnName_Type()
)
apOwnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnName.setStatus("current")
_ApOwnIndex_Type = Integer32
_ApOwnIndex_Object = MibTableColumn
apOwnIndex = _ApOwnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 2),
    _ApOwnIndex_Type()
)
apOwnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnIndex.setStatus("current")


class _ApOwnMaxFlowPipeBwdth_Type(Integer32):
    """Custom type apOwnMaxFlowPipeBwdth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnMaxFlowPipeBwdth_Type.__name__ = "Integer32"
_ApOwnMaxFlowPipeBwdth_Object = MibTableColumn
apOwnMaxFlowPipeBwdth = _ApOwnMaxFlowPipeBwdth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 3),
    _ApOwnMaxFlowPipeBwdth_Type()
)
apOwnMaxFlowPipeBwdth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnMaxFlowPipeBwdth.setStatus("current")


class _ApOwnFlowPipeBurstTolerance_Type(Integer32):
    """Custom type apOwnFlowPipeBurstTolerance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApOwnFlowPipeBurstTolerance_Type.__name__ = "Integer32"
_ApOwnFlowPipeBurstTolerance_Object = MibTableColumn
apOwnFlowPipeBurstTolerance = _ApOwnFlowPipeBurstTolerance_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 4),
    _ApOwnFlowPipeBurstTolerance_Type()
)
apOwnFlowPipeBurstTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnFlowPipeBurstTolerance.setStatus("current")


class _ApOwnMaxPrioritizedFlows_Type(Integer32):
    """Custom type apOwnMaxPrioritizedFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnMaxPrioritizedFlows_Type.__name__ = "Integer32"
_ApOwnMaxPrioritizedFlows_Object = MibTableColumn
apOwnMaxPrioritizedFlows = _ApOwnMaxPrioritizedFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 5),
    _ApOwnMaxPrioritizedFlows_Type()
)
apOwnMaxPrioritizedFlows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnMaxPrioritizedFlows.setStatus("current")


class _ApOwnBillingInfo_Type(DisplayString):
    """Custom type apOwnBillingInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApOwnBillingInfo_Type.__name__ = "DisplayString"
_ApOwnBillingInfo_Object = MibTableColumn
apOwnBillingInfo = _ApOwnBillingInfo_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 6),
    _ApOwnBillingInfo_Type()
)
apOwnBillingInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnBillingInfo.setStatus("current")


class _ApOwnAddress_Type(DisplayString):
    """Custom type apOwnAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApOwnAddress_Type.__name__ = "DisplayString"
_ApOwnAddress_Object = MibTableColumn
apOwnAddress = _ApOwnAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 7),
    _ApOwnAddress_Type()
)
apOwnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnAddress.setStatus("current")


class _ApOwnEmailAddress_Type(DisplayString):
    """Custom type apOwnEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApOwnEmailAddress_Type.__name__ = "DisplayString"
_ApOwnEmailAddress_Object = MibTableColumn
apOwnEmailAddress = _ApOwnEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 8),
    _ApOwnEmailAddress_Type()
)
apOwnEmailAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnEmailAddress.setStatus("current")


class _ApOwnFlowPipeBwdthAlloc_Type(Integer32):
    """Custom type apOwnFlowPipeBwdthAlloc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnFlowPipeBwdthAlloc_Type.__name__ = "Integer32"
_ApOwnFlowPipeBwdthAlloc_Object = MibTableColumn
apOwnFlowPipeBwdthAlloc = _ApOwnFlowPipeBwdthAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 9),
    _ApOwnFlowPipeBwdthAlloc_Type()
)
apOwnFlowPipeBwdthAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnFlowPipeBwdthAlloc.setStatus("current")


class _ApOwnFlowPipeActiveFlows_Type(Integer32):
    """Custom type apOwnFlowPipeActiveFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnFlowPipeActiveFlows_Type.__name__ = "Integer32"
_ApOwnFlowPipeActiveFlows_Object = MibTableColumn
apOwnFlowPipeActiveFlows = _ApOwnFlowPipeActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 10),
    _ApOwnFlowPipeActiveFlows_Type()
)
apOwnFlowPipeActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnFlowPipeActiveFlows.setStatus("current")


class _ApOwnFlowPipeTotalFlows_Type(Integer32):
    """Custom type apOwnFlowPipeTotalFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnFlowPipeTotalFlows_Type.__name__ = "Integer32"
_ApOwnFlowPipeTotalFlows_Object = MibTableColumn
apOwnFlowPipeTotalFlows = _ApOwnFlowPipeTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 11),
    _ApOwnFlowPipeTotalFlows_Type()
)
apOwnFlowPipeTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnFlowPipeTotalFlows.setStatus("current")


class _ApOwnFlowPipeTotalMisses_Type(Integer32):
    """Custom type apOwnFlowPipeTotalMisses based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnFlowPipeTotalMisses_Type.__name__ = "Integer32"
_ApOwnFlowPipeTotalMisses_Object = MibTableColumn
apOwnFlowPipeTotalMisses = _ApOwnFlowPipeTotalMisses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 12),
    _ApOwnFlowPipeTotalMisses_Type()
)
apOwnFlowPipeTotalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnFlowPipeTotalMisses.setStatus("current")


class _ApOwnQosBwdthAlloc_Type(Integer32):
    """Custom type apOwnQosBwdthAlloc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnQosBwdthAlloc_Type.__name__ = "Integer32"
_ApOwnQosBwdthAlloc_Object = MibTableColumn
apOwnQosBwdthAlloc = _ApOwnQosBwdthAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 13),
    _ApOwnQosBwdthAlloc_Type()
)
apOwnQosBwdthAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnQosBwdthAlloc.setStatus("current")


class _ApOwnBEBwdthAlloc_Type(Integer32):
    """Custom type apOwnBEBwdthAlloc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApOwnBEBwdthAlloc_Type.__name__ = "Integer32"
_ApOwnBEBwdthAlloc_Object = MibTableColumn
apOwnBEBwdthAlloc = _ApOwnBEBwdthAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 14),
    _ApOwnBEBwdthAlloc_Type()
)
apOwnBEBwdthAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnBEBwdthAlloc.setStatus("current")


class _ApOwnHits_Type(Integer32):
    """Custom type apOwnHits based on Integer32"""
    defaultValue = 0


_ApOwnHits_Object = MibTableColumn
apOwnHits = _ApOwnHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 15),
    _ApOwnHits_Type()
)
apOwnHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnHits.setStatus("current")


class _ApOwnRedirects_Type(Integer32):
    """Custom type apOwnRedirects based on Integer32"""
    defaultValue = 0


_ApOwnRedirects_Object = MibTableColumn
apOwnRedirects = _ApOwnRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 16),
    _ApOwnRedirects_Type()
)
apOwnRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnRedirects.setStatus("current")


class _ApOwnDrops_Type(Integer32):
    """Custom type apOwnDrops based on Integer32"""
    defaultValue = 0


_ApOwnDrops_Object = MibTableColumn
apOwnDrops = _ApOwnDrops_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 17),
    _ApOwnDrops_Type()
)
apOwnDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnDrops.setStatus("current")


class _ApOwnRejNoServices_Type(Integer32):
    """Custom type apOwnRejNoServices based on Integer32"""
    defaultValue = 0


_ApOwnRejNoServices_Object = MibTableColumn
apOwnRejNoServices = _ApOwnRejNoServices_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 18),
    _ApOwnRejNoServices_Type()
)
apOwnRejNoServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnRejNoServices.setStatus("current")


class _ApOwnRejServOverload_Type(Integer32):
    """Custom type apOwnRejServOverload based on Integer32"""
    defaultValue = 0


_ApOwnRejServOverload_Object = MibTableColumn
apOwnRejServOverload = _ApOwnRejServOverload_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 19),
    _ApOwnRejServOverload_Type()
)
apOwnRejServOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnRejServOverload.setStatus("current")


class _ApOwnSpoofs_Type(Integer32):
    """Custom type apOwnSpoofs based on Integer32"""
    defaultValue = 0


_ApOwnSpoofs_Object = MibTableColumn
apOwnSpoofs = _ApOwnSpoofs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 20),
    _ApOwnSpoofs_Type()
)
apOwnSpoofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnSpoofs.setStatus("current")


class _ApOwnNats_Type(Integer32):
    """Custom type apOwnNats based on Integer32"""
    defaultValue = 0


_ApOwnNats_Object = MibTableColumn
apOwnNats = _ApOwnNats_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 21),
    _ApOwnNats_Type()
)
apOwnNats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnNats.setStatus("current")


class _ApOwnByteCount_Type(Integer32):
    """Custom type apOwnByteCount based on Integer32"""
    defaultValue = 0


_ApOwnByteCount_Object = MibTableColumn
apOwnByteCount = _ApOwnByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 22),
    _ApOwnByteCount_Type()
)
apOwnByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnByteCount.setStatus("current")


class _ApOwnFrameCount_Type(Integer32):
    """Custom type apOwnFrameCount based on Integer32"""
    defaultValue = 0


_ApOwnFrameCount_Object = MibTableColumn
apOwnFrameCount = _ApOwnFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 23),
    _ApOwnFrameCount_Type()
)
apOwnFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOwnFrameCount.setStatus("current")


class _ApOwnDNSPolicy_Type(Integer32):
    """Custom type apOwnDNSPolicy based on Integer32"""
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
        *(("accept", 1),
          ("both", 3),
          ("none", 0),
          ("push", 2))
    )


_ApOwnDNSPolicy_Type.__name__ = "Integer32"
_ApOwnDNSPolicy_Object = MibTableColumn
apOwnDNSPolicy = _ApOwnDNSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 24),
    _ApOwnDNSPolicy_Type()
)
apOwnDNSPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnDNSPolicy.setStatus("current")
_ApOwnStatus_Type = RowStatus
_ApOwnStatus_Object = MibTableColumn
apOwnStatus = _ApOwnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 25),
    _ApOwnStatus_Type()
)
apOwnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnStatus.setStatus("current")


class _ApOwnCaseSensitive_Type(Integer32):
    """Custom type apOwnCaseSensitive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insensitive", 0),
          ("sensitive", 1))
    )


_ApOwnCaseSensitive_Type.__name__ = "Integer32"
_ApOwnCaseSensitive_Object = MibTableColumn
apOwnCaseSensitive = _ApOwnCaseSensitive_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 26),
    _ApOwnCaseSensitive_Type()
)
apOwnCaseSensitive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnCaseSensitive.setStatus("current")


class _ApOwnDNSBalance_Type(Integer32):
    """Custom type apOwnDNSBalance based on Integer32"""
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
        *(("leastloaded", 3),
          ("preferlocal", 1),
          ("roundrobin", 2))
    )


_ApOwnDNSBalance_Type.__name__ = "Integer32"
_ApOwnDNSBalance_Object = MibTableColumn
apOwnDNSBalance = _ApOwnDNSBalance_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 25, 2, 1, 27),
    _ApOwnDNSBalance_Type()
)
apOwnDNSBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apOwnDNSBalance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OWNEXT-MIB",
    **{"apOwnExtMib": apOwnExtMib,
       "apOwnTable": apOwnTable,
       "apOwnEntry": apOwnEntry,
       "apOwnName": apOwnName,
       "apOwnIndex": apOwnIndex,
       "apOwnMaxFlowPipeBwdth": apOwnMaxFlowPipeBwdth,
       "apOwnFlowPipeBurstTolerance": apOwnFlowPipeBurstTolerance,
       "apOwnMaxPrioritizedFlows": apOwnMaxPrioritizedFlows,
       "apOwnBillingInfo": apOwnBillingInfo,
       "apOwnAddress": apOwnAddress,
       "apOwnEmailAddress": apOwnEmailAddress,
       "apOwnFlowPipeBwdthAlloc": apOwnFlowPipeBwdthAlloc,
       "apOwnFlowPipeActiveFlows": apOwnFlowPipeActiveFlows,
       "apOwnFlowPipeTotalFlows": apOwnFlowPipeTotalFlows,
       "apOwnFlowPipeTotalMisses": apOwnFlowPipeTotalMisses,
       "apOwnQosBwdthAlloc": apOwnQosBwdthAlloc,
       "apOwnBEBwdthAlloc": apOwnBEBwdthAlloc,
       "apOwnHits": apOwnHits,
       "apOwnRedirects": apOwnRedirects,
       "apOwnDrops": apOwnDrops,
       "apOwnRejNoServices": apOwnRejNoServices,
       "apOwnRejServOverload": apOwnRejServOverload,
       "apOwnSpoofs": apOwnSpoofs,
       "apOwnNats": apOwnNats,
       "apOwnByteCount": apOwnByteCount,
       "apOwnFrameCount": apOwnFrameCount,
       "apOwnDNSPolicy": apOwnDNSPolicy,
       "apOwnStatus": apOwnStatus,
       "apOwnCaseSensitive": apOwnCaseSensitive,
       "apOwnDNSBalance": apOwnDNSBalance}
)
