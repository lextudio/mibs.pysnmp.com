# SNMP MIB module (NSCDXGLIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCDXGLIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:30 2024
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

(nscDx,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscDx")

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
 enterprises,
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
    "enterprises",
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

_NscDxGreenline_ObjectIdentity = ObjectIdentity
nscDxGreenline = _NscDxGreenline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4)
)
_NscDxGlChannelTable_Object = MibTable
nscDxGlChannelTable = _NscDxGlChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    nscDxGlChannelTable.setStatus("mandatory")
_NscDxGlChannelEntry_Object = MibTableRow
nscDxGlChannelEntry = _NscDxGlChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1)
)
nscDxGlChannelEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlChanEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxGlChannelEntry.setStatus("mandatory")


class _NscDxGlChanEntKeyId_Type(Integer32):
    """Custom type nscDxGlChanEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlChanEntKeyId_Type.__name__ = "Integer32"
_NscDxGlChanEntKeyId_Object = MibTableColumn
nscDxGlChanEntKeyId = _NscDxGlChanEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 1),
    _NscDxGlChanEntKeyId_Type()
)
nscDxGlChanEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntKeyId.setStatus("mandatory")


class _NscDxGlChanEntType_Type(Integer32):
    """Custom type nscDxGlChanEntType based on Integer32"""
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
        *(("bus-tag-hci", 1),
          ("bus-tag-rci", 2),
          ("escon-hci", 3),
          ("escon-rci", 4))
    )


_NscDxGlChanEntType_Type.__name__ = "Integer32"
_NscDxGlChanEntType_Object = MibTableColumn
nscDxGlChanEntType = _NscDxGlChanEntType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 2),
    _NscDxGlChanEntType_Type()
)
nscDxGlChanEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntType.setStatus("mandatory")


class _NscDxGlChanEntActivityState_Type(Integer32):
    """Custom type nscDxGlChanEntActivityState based on Integer32"""
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
        *(("active", 2),
          ("idle", 1),
          ("ipl", 6),
          ("stacked", 3),
          ("suppressible", 4),
          ("unsuppressible", 5),
          ("wait-for-resources", 7))
    )


_NscDxGlChanEntActivityState_Type.__name__ = "Integer32"
_NscDxGlChanEntActivityState_Object = MibTableColumn
nscDxGlChanEntActivityState = _NscDxGlChanEntActivityState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 3),
    _NscDxGlChanEntActivityState_Type()
)
nscDxGlChanEntActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntActivityState.setStatus("mandatory")


class _NscDxGlChanEntResetState_Type(Integer32):
    """Custom type nscDxGlChanEntResetState based on Integer32"""
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
        *(("ifdisc", 4),
          ("none", 1),
          ("selective-reset", 3),
          ("system-reset", 2))
    )


_NscDxGlChanEntResetState_Type.__name__ = "Integer32"
_NscDxGlChanEntResetState_Object = MibTableColumn
nscDxGlChanEntResetState = _NscDxGlChanEntResetState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 4),
    _NscDxGlChanEntResetState_Type()
)
nscDxGlChanEntResetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntResetState.setStatus("mandatory")


class _NscDxGlChanEntIplState_Type(Integer32):
    """Custom type nscDxGlChanEntIplState based on Integer32"""
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
        *(("active", 2),
          ("idle", 1),
          ("ipl", 6),
          ("stacked", 3),
          ("suppressible", 4),
          ("unsuppressible", 5),
          ("wait-for-resources", 7))
    )


_NscDxGlChanEntIplState_Type.__name__ = "Integer32"
_NscDxGlChanEntIplState_Object = MibTableColumn
nscDxGlChanEntIplState = _NscDxGlChanEntIplState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 5),
    _NscDxGlChanEntIplState_Type()
)
nscDxGlChanEntIplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntIplState.setStatus("mandatory")


class _NscDxGlChanEntIpState_Type(Integer32):
    """Custom type nscDxGlChanEntIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NscDxGlChanEntIpState_Type.__name__ = "Integer32"
_NscDxGlChanEntIpState_Object = MibTableColumn
nscDxGlChanEntIpState = _NscDxGlChanEntIpState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 6),
    _NscDxGlChanEntIpState_Type()
)
nscDxGlChanEntIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntIpState.setStatus("mandatory")


class _NscDxGlChanEntOnlineOfflineState_Type(Integer32):
    """Custom type nscDxGlChanEntOnlineOfflineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NscDxGlChanEntOnlineOfflineState_Type.__name__ = "Integer32"
_NscDxGlChanEntOnlineOfflineState_Object = MibTableColumn
nscDxGlChanEntOnlineOfflineState = _NscDxGlChanEntOnlineOfflineState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 7),
    _NscDxGlChanEntOnlineOfflineState_Type()
)
nscDxGlChanEntOnlineOfflineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntOnlineOfflineState.setStatus("mandatory")


class _NscDxGlChanEntPolling_Type(Integer32):
    """Custom type nscDxGlChanEntPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NscDxGlChanEntPolling_Type.__name__ = "Integer32"
_NscDxGlChanEntPolling_Object = MibTableColumn
nscDxGlChanEntPolling = _NscDxGlChanEntPolling_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 8),
    _NscDxGlChanEntPolling_Type()
)
nscDxGlChanEntPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlChanEntPolling.setStatus("mandatory")


class _NscDxGlChanEntActiveSubchannel_Type(Integer32):
    """Custom type nscDxGlChanEntActiveSubchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlChanEntActiveSubchannel_Type.__name__ = "Integer32"
_NscDxGlChanEntActiveSubchannel_Object = MibTableColumn
nscDxGlChanEntActiveSubchannel = _NscDxGlChanEntActiveSubchannel_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 9),
    _NscDxGlChanEntActiveSubchannel_Type()
)
nscDxGlChanEntActiveSubchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntActiveSubchannel.setStatus("mandatory")


class _NscDxGlChanEntMemoryResourcesLimited_Type(Integer32):
    """Custom type nscDxGlChanEntMemoryResourcesLimited based on Integer32"""
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


_NscDxGlChanEntMemoryResourcesLimited_Type.__name__ = "Integer32"
_NscDxGlChanEntMemoryResourcesLimited_Object = MibTableColumn
nscDxGlChanEntMemoryResourcesLimited = _NscDxGlChanEntMemoryResourcesLimited_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 10),
    _NscDxGlChanEntMemoryResourcesLimited_Type()
)
nscDxGlChanEntMemoryResourcesLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntMemoryResourcesLimited.setStatus("mandatory")
_NscDxGlChanEntTagOverruns_Type = Counter32
_NscDxGlChanEntTagOverruns_Object = MibTableColumn
nscDxGlChanEntTagOverruns = _NscDxGlChanEntTagOverruns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 11),
    _NscDxGlChanEntTagOverruns_Type()
)
nscDxGlChanEntTagOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntTagOverruns.setStatus("mandatory")
_NscDxGlChanEntDcOverruns_Type = Counter32
_NscDxGlChanEntDcOverruns_Object = MibTableColumn
nscDxGlChanEntDcOverruns = _NscDxGlChanEntDcOverruns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 12),
    _NscDxGlChanEntDcOverruns_Type()
)
nscDxGlChanEntDcOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntDcOverruns.setStatus("mandatory")
_NscDxGlChanEntDsOverruns_Type = Counter32
_NscDxGlChanEntDsOverruns_Object = MibTableColumn
nscDxGlChanEntDsOverruns = _NscDxGlChanEntDsOverruns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 13),
    _NscDxGlChanEntDsOverruns_Type()
)
nscDxGlChanEntDsOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntDsOverruns.setStatus("mandatory")
_NscDxGlChanEntDmaParityErrors_Type = Counter32
_NscDxGlChanEntDmaParityErrors_Object = MibTableColumn
nscDxGlChanEntDmaParityErrors = _NscDxGlChanEntDmaParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 14),
    _NscDxGlChanEntDmaParityErrors_Type()
)
nscDxGlChanEntDmaParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntDmaParityErrors.setStatus("mandatory")
_NscDxGlChanEntCrcErrors_Type = Counter32
_NscDxGlChanEntCrcErrors_Object = MibTableColumn
nscDxGlChanEntCrcErrors = _NscDxGlChanEntCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 15),
    _NscDxGlChanEntCrcErrors_Type()
)
nscDxGlChanEntCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntCrcErrors.setStatus("mandatory")
_NscDxGlChanEntResetsDuringDma_Type = Counter32
_NscDxGlChanEntResetsDuringDma_Object = MibTableColumn
nscDxGlChanEntResetsDuringDma = _NscDxGlChanEntResetsDuringDma_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 16),
    _NscDxGlChanEntResetsDuringDma_Type()
)
nscDxGlChanEntResetsDuringDma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntResetsDuringDma.setStatus("mandatory")
_NscDxGlChanEntCmdParityErrors_Type = Counter32
_NscDxGlChanEntCmdParityErrors_Object = MibTableColumn
nscDxGlChanEntCmdParityErrors = _NscDxGlChanEntCmdParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 17),
    _NscDxGlChanEntCmdParityErrors_Type()
)
nscDxGlChanEntCmdParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntCmdParityErrors.setStatus("mandatory")
_NscDxGlChanEntUnsupportedStatuses_Type = Counter32
_NscDxGlChanEntUnsupportedStatuses_Object = MibTableColumn
nscDxGlChanEntUnsupportedStatuses = _NscDxGlChanEntUnsupportedStatuses_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 18),
    _NscDxGlChanEntUnsupportedStatuses_Type()
)
nscDxGlChanEntUnsupportedStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntUnsupportedStatuses.setStatus("mandatory")
_NscDxGlChanEntMiscompareParityErrors_Type = Counter32
_NscDxGlChanEntMiscompareParityErrors_Object = MibTableColumn
nscDxGlChanEntMiscompareParityErrors = _NscDxGlChanEntMiscompareParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 19),
    _NscDxGlChanEntMiscompareParityErrors_Type()
)
nscDxGlChanEntMiscompareParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntMiscompareParityErrors.setStatus("mandatory")
_NscDxGlChanEntSelectionTimeouts_Type = Counter32
_NscDxGlChanEntSelectionTimeouts_Object = MibTableColumn
nscDxGlChanEntSelectionTimeouts = _NscDxGlChanEntSelectionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 20),
    _NscDxGlChanEntSelectionTimeouts_Type()
)
nscDxGlChanEntSelectionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntSelectionTimeouts.setStatus("mandatory")
_NscDxGlChanEntStatusAcceptDiscIns_Type = Counter32
_NscDxGlChanEntStatusAcceptDiscIns_Object = MibTableColumn
nscDxGlChanEntStatusAcceptDiscIns = _NscDxGlChanEntStatusAcceptDiscIns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 21),
    _NscDxGlChanEntStatusAcceptDiscIns_Type()
)
nscDxGlChanEntStatusAcceptDiscIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntStatusAcceptDiscIns.setStatus("mandatory")
_NscDxGlChanEntStatusAcceptTimeouts_Type = Counter32
_NscDxGlChanEntStatusAcceptTimeouts_Object = MibTableColumn
nscDxGlChanEntStatusAcceptTimeouts = _NscDxGlChanEntStatusAcceptTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 22),
    _NscDxGlChanEntStatusAcceptTimeouts_Type()
)
nscDxGlChanEntStatusAcceptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntStatusAcceptTimeouts.setStatus("mandatory")
_NscDxGlChanEntStatusWaitDiscIns_Type = Counter32
_NscDxGlChanEntStatusWaitDiscIns_Object = MibTableColumn
nscDxGlChanEntStatusWaitDiscIns = _NscDxGlChanEntStatusWaitDiscIns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 23),
    _NscDxGlChanEntStatusWaitDiscIns_Type()
)
nscDxGlChanEntStatusWaitDiscIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntStatusWaitDiscIns.setStatus("mandatory")
_NscDxGlChanEntStatusWaitTimeouts_Type = Counter32
_NscDxGlChanEntStatusWaitTimeouts_Object = MibTableColumn
nscDxGlChanEntStatusWaitTimeouts = _NscDxGlChanEntStatusWaitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 24),
    _NscDxGlChanEntStatusWaitTimeouts_Type()
)
nscDxGlChanEntStatusWaitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntStatusWaitTimeouts.setStatus("mandatory")
_NscDxGlChanEntOpInActiveTimeouts_Type = Counter32
_NscDxGlChanEntOpInActiveTimeouts_Object = MibTableColumn
nscDxGlChanEntOpInActiveTimeouts = _NscDxGlChanEntOpInActiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 25),
    _NscDxGlChanEntOpInActiveTimeouts_Type()
)
nscDxGlChanEntOpInActiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntOpInActiveTimeouts.setStatus("mandatory")
_NscDxGlChanEntNumCus_Type = Integer32
_NscDxGlChanEntNumCus_Object = MibTableColumn
nscDxGlChanEntNumCus = _NscDxGlChanEntNumCus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 26),
    _NscDxGlChanEntNumCus_Type()
)
nscDxGlChanEntNumCus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntNumCus.setStatus("mandatory")


class _NscDxGlChanEntChannelStatus_Type(Integer32):
    """Custom type nscDxGlChanEntChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notconnected", 2))
    )


_NscDxGlChanEntChannelStatus_Type.__name__ = "Integer32"
_NscDxGlChanEntChannelStatus_Object = MibTableColumn
nscDxGlChanEntChannelStatus = _NscDxGlChanEntChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 1, 1, 27),
    _NscDxGlChanEntChannelStatus_Type()
)
nscDxGlChanEntChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlChanEntChannelStatus.setStatus("mandatory")
_NscDxGlProfiles_ObjectIdentity = ObjectIdentity
nscDxGlProfiles = _NscDxGlProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2)
)
_NscDxGlProfControlUnitTable_Object = MibTable
nscDxGlProfControlUnitTable = _NscDxGlProfControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nscDxGlProfControlUnitTable.setStatus("mandatory")
_NscDxGlProfControlUnitEntry_Object = MibTableRow
nscDxGlProfControlUnitEntry = _NscDxGlProfControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1)
)
nscDxGlProfControlUnitEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlCuEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlCuEntCuNum"),
)
if mibBuilder.loadTexts:
    nscDxGlProfControlUnitEntry.setStatus("mandatory")


class _NscDxGlProfCuEntKeyId_Type(Integer32):
    """Custom type nscDxGlProfCuEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlProfCuEntKeyId_Type.__name__ = "Integer32"
_NscDxGlProfCuEntKeyId_Object = MibTableColumn
nscDxGlProfCuEntKeyId = _NscDxGlProfCuEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 1),
    _NscDxGlProfCuEntKeyId_Type()
)
nscDxGlProfCuEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntKeyId.setStatus("mandatory")


class _NscDxGlProfCuEntCuNum_Type(Integer32):
    """Custom type nscDxGlProfCuEntCuNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlProfCuEntCuNum_Type.__name__ = "Integer32"
_NscDxGlProfCuEntCuNum_Object = MibTableColumn
nscDxGlProfCuEntCuNum = _NscDxGlProfCuEntCuNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 2),
    _NscDxGlProfCuEntCuNum_Type()
)
nscDxGlProfCuEntCuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntCuNum.setStatus("mandatory")
_NscDxGlProfCuEntNumDevices_Type = Integer32
_NscDxGlProfCuEntNumDevices_Object = MibTableColumn
nscDxGlProfCuEntNumDevices = _NscDxGlProfCuEntNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 3),
    _NscDxGlProfCuEntNumDevices_Type()
)
nscDxGlProfCuEntNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntNumDevices.setStatus("mandatory")


class _NscDxGlProfCuEntOnlineOfflineState_Type(Integer32):
    """Custom type nscDxGlProfCuEntOnlineOfflineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_NscDxGlProfCuEntOnlineOfflineState_Type.__name__ = "Integer32"
_NscDxGlProfCuEntOnlineOfflineState_Object = MibTableColumn
nscDxGlProfCuEntOnlineOfflineState = _NscDxGlProfCuEntOnlineOfflineState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 4),
    _NscDxGlProfCuEntOnlineOfflineState_Type()
)
nscDxGlProfCuEntOnlineOfflineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntOnlineOfflineState.setStatus("mandatory")


class _NscDxGlProfCuEntDeviceType_Type(DisplayString):
    """Custom type nscDxGlProfCuEntDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NscDxGlProfCuEntDeviceType_Type.__name__ = "DisplayString"
_NscDxGlProfCuEntDeviceType_Object = MibTableColumn
nscDxGlProfCuEntDeviceType = _NscDxGlProfCuEntDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 5),
    _NscDxGlProfCuEntDeviceType_Type()
)
nscDxGlProfCuEntDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntDeviceType.setStatus("mandatory")


class _NscDxGlProfCuEntHostStartingDevAddr_Type(Integer32):
    """Custom type nscDxGlProfCuEntHostStartingDevAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfCuEntHostStartingDevAddr_Type.__name__ = "Integer32"
_NscDxGlProfCuEntHostStartingDevAddr_Object = MibTableColumn
nscDxGlProfCuEntHostStartingDevAddr = _NscDxGlProfCuEntHostStartingDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 6),
    _NscDxGlProfCuEntHostStartingDevAddr_Type()
)
nscDxGlProfCuEntHostStartingDevAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntHostStartingDevAddr.setStatus("mandatory")


class _NscDxGlProfCuEntHostEndingDevAddr_Type(Integer32):
    """Custom type nscDxGlProfCuEntHostEndingDevAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfCuEntHostEndingDevAddr_Type.__name__ = "Integer32"
_NscDxGlProfCuEntHostEndingDevAddr_Object = MibTableColumn
nscDxGlProfCuEntHostEndingDevAddr = _NscDxGlProfCuEntHostEndingDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 7),
    _NscDxGlProfCuEntHostEndingDevAddr_Type()
)
nscDxGlProfCuEntHostEndingDevAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntHostEndingDevAddr.setStatus("mandatory")


class _NscDxGlProfCuEntHostChannelSpeed_Type(Integer32):
    """Custom type nscDxGlProfCuEntHostChannelSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dci", 1),
          ("ds3", 2),
          ("ds4", 3))
    )


_NscDxGlProfCuEntHostChannelSpeed_Type.__name__ = "Integer32"
_NscDxGlProfCuEntHostChannelSpeed_Object = MibTableColumn
nscDxGlProfCuEntHostChannelSpeed = _NscDxGlProfCuEntHostChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 8),
    _NscDxGlProfCuEntHostChannelSpeed_Type()
)
nscDxGlProfCuEntHostChannelSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntHostChannelSpeed.setStatus("mandatory")


class _NscDxGlProfCuEntHostBufferRequirements_Type(Integer32):
    """Custom type nscDxGlProfCuEntHostBufferRequirements based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfCuEntHostBufferRequirements_Type.__name__ = "Integer32"
_NscDxGlProfCuEntHostBufferRequirements_Object = MibTableColumn
nscDxGlProfCuEntHostBufferRequirements = _NscDxGlProfCuEntHostBufferRequirements_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 9),
    _NscDxGlProfCuEntHostBufferRequirements_Type()
)
nscDxGlProfCuEntHostBufferRequirements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntHostBufferRequirements.setStatus("mandatory")
_NscDxGlProfCuEntRmtIpAddr_Type = IpAddress
_NscDxGlProfCuEntRmtIpAddr_Object = MibTableColumn
nscDxGlProfCuEntRmtIpAddr = _NscDxGlProfCuEntRmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 10),
    _NscDxGlProfCuEntRmtIpAddr_Type()
)
nscDxGlProfCuEntRmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntRmtIpAddr.setStatus("mandatory")


class _NscDxGlProfCuEntRmtStartingDevAddr_Type(Integer32):
    """Custom type nscDxGlProfCuEntRmtStartingDevAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfCuEntRmtStartingDevAddr_Type.__name__ = "Integer32"
_NscDxGlProfCuEntRmtStartingDevAddr_Object = MibTableColumn
nscDxGlProfCuEntRmtStartingDevAddr = _NscDxGlProfCuEntRmtStartingDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 11),
    _NscDxGlProfCuEntRmtStartingDevAddr_Type()
)
nscDxGlProfCuEntRmtStartingDevAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntRmtStartingDevAddr.setStatus("mandatory")


class _NscDxGlProfCuEntRmtBufferHold_Type(Integer32):
    """Custom type nscDxGlProfCuEntRmtBufferHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("tbl-def", 1))
    )


_NscDxGlProfCuEntRmtBufferHold_Type.__name__ = "Integer32"
_NscDxGlProfCuEntRmtBufferHold_Object = MibTableColumn
nscDxGlProfCuEntRmtBufferHold = _NscDxGlProfCuEntRmtBufferHold_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 12),
    _NscDxGlProfCuEntRmtBufferHold_Type()
)
nscDxGlProfCuEntRmtBufferHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntRmtBufferHold.setStatus("mandatory")


class _NscDxGlProfCuEntRmtChannelSpeed_Type(Integer32):
    """Custom type nscDxGlProfCuEntRmtChannelSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dci", 1),
          ("ds3", 2),
          ("ds4", 3))
    )


_NscDxGlProfCuEntRmtChannelSpeed_Type.__name__ = "Integer32"
_NscDxGlProfCuEntRmtChannelSpeed_Object = MibTableColumn
nscDxGlProfCuEntRmtChannelSpeed = _NscDxGlProfCuEntRmtChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 13),
    _NscDxGlProfCuEntRmtChannelSpeed_Type()
)
nscDxGlProfCuEntRmtChannelSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntRmtChannelSpeed.setStatus("mandatory")


class _NscDxGlProfCuEntRmtBufferRequirements_Type(Integer32):
    """Custom type nscDxGlProfCuEntRmtBufferRequirements based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfCuEntRmtBufferRequirements_Type.__name__ = "Integer32"
_NscDxGlProfCuEntRmtBufferRequirements_Object = MibTableColumn
nscDxGlProfCuEntRmtBufferRequirements = _NscDxGlProfCuEntRmtBufferRequirements_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 14),
    _NscDxGlProfCuEntRmtBufferRequirements_Type()
)
nscDxGlProfCuEntRmtBufferRequirements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntRmtBufferRequirements.setStatus("mandatory")


class _NscDxGlProfCuEntUnsolStatusOption_Type(Integer32):
    """Custom type nscDxGlProfCuEntUnsolStatusOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("q-non-uc", 1),
          ("q-uc", 3))
    )


_NscDxGlProfCuEntUnsolStatusOption_Type.__name__ = "Integer32"
_NscDxGlProfCuEntUnsolStatusOption_Object = MibTableColumn
nscDxGlProfCuEntUnsolStatusOption = _NscDxGlProfCuEntUnsolStatusOption_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 15),
    _NscDxGlProfCuEntUnsolStatusOption_Type()
)
nscDxGlProfCuEntUnsolStatusOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntUnsolStatusOption.setStatus("mandatory")
_NscDxGlProfCuEntDevDriverOptions_Type = Integer32
_NscDxGlProfCuEntDevDriverOptions_Object = MibTableColumn
nscDxGlProfCuEntDevDriverOptions = _NscDxGlProfCuEntDevDriverOptions_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 16),
    _NscDxGlProfCuEntDevDriverOptions_Type()
)
nscDxGlProfCuEntDevDriverOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntDevDriverOptions.setStatus("mandatory")


class _NscDxGlProfCuEntHostBufferHold_Type(Integer32):
    """Custom type nscDxGlProfCuEntHostBufferHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("tbl-def", 1))
    )


_NscDxGlProfCuEntHostBufferHold_Type.__name__ = "Integer32"
_NscDxGlProfCuEntHostBufferHold_Object = MibTableColumn
nscDxGlProfCuEntHostBufferHold = _NscDxGlProfCuEntHostBufferHold_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 17),
    _NscDxGlProfCuEntHostBufferHold_Type()
)
nscDxGlProfCuEntHostBufferHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntHostBufferHold.setStatus("mandatory")
_NscDxGlProfCuEntWindowSize_Type = Integer32
_NscDxGlProfCuEntWindowSize_Object = MibTableColumn
nscDxGlProfCuEntWindowSize = _NscDxGlProfCuEntWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 1, 1, 18),
    _NscDxGlProfCuEntWindowSize_Type()
)
nscDxGlProfCuEntWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfCuEntWindowSize.setStatus("mandatory")
_NscDxGlProfDeviceTable_Object = MibTable
nscDxGlProfDeviceTable = _NscDxGlProfDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    nscDxGlProfDeviceTable.setStatus("mandatory")
_NscDxGlProfDeviceEntry_Object = MibTableRow
nscDxGlProfDeviceEntry = _NscDxGlProfDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 2, 1)
)
nscDxGlProfDeviceEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlDevEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlProfDevEntDevice"),
)
if mibBuilder.loadTexts:
    nscDxGlProfDeviceEntry.setStatus("mandatory")


class _NscDxGlProfDevEntKeyId_Type(Integer32):
    """Custom type nscDxGlProfDevEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlProfDevEntKeyId_Type.__name__ = "Integer32"
_NscDxGlProfDevEntKeyId_Object = MibTableColumn
nscDxGlProfDevEntKeyId = _NscDxGlProfDevEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 2, 1, 1),
    _NscDxGlProfDevEntKeyId_Type()
)
nscDxGlProfDevEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlProfDevEntKeyId.setStatus("mandatory")


class _NscDxGlProfDevEntDevice_Type(Integer32):
    """Custom type nscDxGlProfDevEntDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlProfDevEntDevice_Type.__name__ = "Integer32"
_NscDxGlProfDevEntDevice_Object = MibTableColumn
nscDxGlProfDevEntDevice = _NscDxGlProfDevEntDevice_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 2, 1, 2),
    _NscDxGlProfDevEntDevice_Type()
)
nscDxGlProfDevEntDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlProfDevEntDevice.setStatus("mandatory")


class _NscDxGlProfDevEntOnOff_Type(Integer32):
    """Custom type nscDxGlProfDevEntOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_NscDxGlProfDevEntOnOff_Type.__name__ = "Integer32"
_NscDxGlProfDevEntOnOff_Object = MibTableColumn
nscDxGlProfDevEntOnOff = _NscDxGlProfDevEntOnOff_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 2, 2, 1, 3),
    _NscDxGlProfDevEntOnOff_Type()
)
nscDxGlProfDevEntOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxGlProfDevEntOnOff.setStatus("mandatory")
_NscDxGlDevStatusTable_Object = MibTable
nscDxGlDevStatusTable = _NscDxGlDevStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    nscDxGlDevStatusTable.setStatus("mandatory")
_NscDxGlDevStatusEntry_Object = MibTableRow
nscDxGlDevStatusEntry = _NscDxGlDevStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1)
)
nscDxGlDevStatusEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlDevStatusEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlDevStatusEntDeviceNum"),
)
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntry.setStatus("mandatory")


class _NscDxGlDevStatusEntKeyId_Type(Integer32):
    """Custom type nscDxGlDevStatusEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlDevStatusEntKeyId_Type.__name__ = "Integer32"
_NscDxGlDevStatusEntKeyId_Object = MibTableColumn
nscDxGlDevStatusEntKeyId = _NscDxGlDevStatusEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 1),
    _NscDxGlDevStatusEntKeyId_Type()
)
nscDxGlDevStatusEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntKeyId.setStatus("mandatory")


class _NscDxGlDevStatusEntDeviceNum_Type(Integer32):
    """Custom type nscDxGlDevStatusEntDeviceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlDevStatusEntDeviceNum_Type.__name__ = "Integer32"
_NscDxGlDevStatusEntDeviceNum_Object = MibTableColumn
nscDxGlDevStatusEntDeviceNum = _NscDxGlDevStatusEntDeviceNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 2),
    _NscDxGlDevStatusEntDeviceNum_Type()
)
nscDxGlDevStatusEntDeviceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntDeviceNum.setStatus("mandatory")
_NscDxGlDevStatusEntHostDevAddr_Type = Integer32
_NscDxGlDevStatusEntHostDevAddr_Object = MibTableColumn
nscDxGlDevStatusEntHostDevAddr = _NscDxGlDevStatusEntHostDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 3),
    _NscDxGlDevStatusEntHostDevAddr_Type()
)
nscDxGlDevStatusEntHostDevAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntHostDevAddr.setStatus("mandatory")
_NscDxGlDevStatusEntRmtDevAddr_Type = Integer32
_NscDxGlDevStatusEntRmtDevAddr_Object = MibTableColumn
nscDxGlDevStatusEntRmtDevAddr = _NscDxGlDevStatusEntRmtDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 4),
    _NscDxGlDevStatusEntRmtDevAddr_Type()
)
nscDxGlDevStatusEntRmtDevAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntRmtDevAddr.setStatus("mandatory")


class _NscDxGlDevStatusEntOnOffState_Type(Integer32):
    """Custom type nscDxGlDevStatusEntOnOffState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marked-off", 3),
          ("off", 1),
          ("on", 2))
    )


_NscDxGlDevStatusEntOnOffState_Type.__name__ = "Integer32"
_NscDxGlDevStatusEntOnOffState_Object = MibTableColumn
nscDxGlDevStatusEntOnOffState = _NscDxGlDevStatusEntOnOffState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 5),
    _NscDxGlDevStatusEntOnOffState_Type()
)
nscDxGlDevStatusEntOnOffState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntOnOffState.setStatus("mandatory")


class _NscDxGlDevStatusEntReservedState_Type(Integer32):
    """Custom type nscDxGlDevStatusEntReservedState based on Integer32"""
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
        *(("primed", 3),
          ("re-reserved", 4),
          ("reserved", 2),
          ("unreserved", 1))
    )


_NscDxGlDevStatusEntReservedState_Type.__name__ = "Integer32"
_NscDxGlDevStatusEntReservedState_Object = MibTableColumn
nscDxGlDevStatusEntReservedState = _NscDxGlDevStatusEntReservedState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 3, 1, 6),
    _NscDxGlDevStatusEntReservedState_Type()
)
nscDxGlDevStatusEntReservedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlDevStatusEntReservedState.setStatus("mandatory")
_NscDxGlSesStatsTable_Object = MibTable
nscDxGlSesStatsTable = _NscDxGlSesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    nscDxGlSesStatsTable.setStatus("mandatory")
_NscDxGlSesStatsEntry_Object = MibTableRow
nscDxGlSesStatsEntry = _NscDxGlSesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1)
)
nscDxGlSesStatsEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlSesStatsEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntry.setStatus("mandatory")


class _NscDxGlSesStatsEntKeyId_Type(Integer32):
    """Custom type nscDxGlSesStatsEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlSesStatsEntKeyId_Type.__name__ = "Integer32"
_NscDxGlSesStatsEntKeyId_Object = MibTableColumn
nscDxGlSesStatsEntKeyId = _NscDxGlSesStatsEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 1),
    _NscDxGlSesStatsEntKeyId_Type()
)
nscDxGlSesStatsEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntKeyId.setStatus("mandatory")
_NscDxGlSesStatsEntInControlReqs_Type = Counter32
_NscDxGlSesStatsEntInControlReqs_Object = MibTableColumn
nscDxGlSesStatsEntInControlReqs = _NscDxGlSesStatsEntInControlReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 2),
    _NscDxGlSesStatsEntInControlReqs_Type()
)
nscDxGlSesStatsEntInControlReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInControlReqs.setStatus("mandatory")
_NscDxGlSesStatsEntInControlResps_Type = Counter32
_NscDxGlSesStatsEntInControlResps_Object = MibTableColumn
nscDxGlSesStatsEntInControlResps = _NscDxGlSesStatsEntInControlResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 3),
    _NscDxGlSesStatsEntInControlResps_Type()
)
nscDxGlSesStatsEntInControlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInControlResps.setStatus("mandatory")
_NscDxGlSesStatsEntInDevAvailResps_Type = Counter32
_NscDxGlSesStatsEntInDevAvailResps_Object = MibTableColumn
nscDxGlSesStatsEntInDevAvailResps = _NscDxGlSesStatsEntInDevAvailResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 4),
    _NscDxGlSesStatsEntInDevAvailResps_Type()
)
nscDxGlSesStatsEntInDevAvailResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInDevAvailResps.setStatus("mandatory")
_NscDxGlSesStatsEntInDevStatResps_Type = Counter32
_NscDxGlSesStatsEntInDevStatResps_Object = MibTableColumn
nscDxGlSesStatsEntInDevStatResps = _NscDxGlSesStatsEntInDevStatResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 5),
    _NscDxGlSesStatsEntInDevStatResps_Type()
)
nscDxGlSesStatsEntInDevStatResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInDevStatResps.setStatus("mandatory")
_NscDxGlSesStatsEntInInitReqs_Type = Counter32
_NscDxGlSesStatsEntInInitReqs_Object = MibTableColumn
nscDxGlSesStatsEntInInitReqs = _NscDxGlSesStatsEntInInitReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 6),
    _NscDxGlSesStatsEntInInitReqs_Type()
)
nscDxGlSesStatsEntInInitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInInitReqs.setStatus("mandatory")
_NscDxGlSesStatsEntInInitResps_Type = Counter32
_NscDxGlSesStatsEntInInitResps_Object = MibTableColumn
nscDxGlSesStatsEntInInitResps = _NscDxGlSesStatsEntInInitResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 7),
    _NscDxGlSesStatsEntInInitResps_Type()
)
nscDxGlSesStatsEntInInitResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInInitResps.setStatus("mandatory")
_NscDxGlSesStatsEntInReserveReqs_Type = Counter32
_NscDxGlSesStatsEntInReserveReqs_Object = MibTableColumn
nscDxGlSesStatsEntInReserveReqs = _NscDxGlSesStatsEntInReserveReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 8),
    _NscDxGlSesStatsEntInReserveReqs_Type()
)
nscDxGlSesStatsEntInReserveReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInReserveReqs.setStatus("mandatory")
_NscDxGlSesStatsEntInReserveResps_Type = Counter32
_NscDxGlSesStatsEntInReserveResps_Object = MibTableColumn
nscDxGlSesStatsEntInReserveResps = _NscDxGlSesStatsEntInReserveResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 9),
    _NscDxGlSesStatsEntInReserveResps_Type()
)
nscDxGlSesStatsEntInReserveResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInReserveResps.setStatus("mandatory")
_NscDxGlSesStatsEntInSenseReqs_Type = Counter32
_NscDxGlSesStatsEntInSenseReqs_Object = MibTableColumn
nscDxGlSesStatsEntInSenseReqs = _NscDxGlSesStatsEntInSenseReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 10),
    _NscDxGlSesStatsEntInSenseReqs_Type()
)
nscDxGlSesStatsEntInSenseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInSenseReqs.setStatus("mandatory")
_NscDxGlSesStatsEntInSenseResps_Type = Counter32
_NscDxGlSesStatsEntInSenseResps_Object = MibTableColumn
nscDxGlSesStatsEntInSenseResps = _NscDxGlSesStatsEntInSenseResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 11),
    _NscDxGlSesStatsEntInSenseResps_Type()
)
nscDxGlSesStatsEntInSenseResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInSenseResps.setStatus("mandatory")
_NscDxGlSesStatsEntInUnreserveReqs_Type = Counter32
_NscDxGlSesStatsEntInUnreserveReqs_Object = MibTableColumn
nscDxGlSesStatsEntInUnreserveReqs = _NscDxGlSesStatsEntInUnreserveReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 12),
    _NscDxGlSesStatsEntInUnreserveReqs_Type()
)
nscDxGlSesStatsEntInUnreserveReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInUnreserveReqs.setStatus("mandatory")
_NscDxGlSesStatsEntInInvalids_Type = Counter32
_NscDxGlSesStatsEntInInvalids_Object = MibTableColumn
nscDxGlSesStatsEntInInvalids = _NscDxGlSesStatsEntInInvalids_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 13),
    _NscDxGlSesStatsEntInInvalids_Type()
)
nscDxGlSesStatsEntInInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntInInvalids.setStatus("mandatory")
_NscDxGlSesStatsEntOutControlReqs_Type = Counter32
_NscDxGlSesStatsEntOutControlReqs_Object = MibTableColumn
nscDxGlSesStatsEntOutControlReqs = _NscDxGlSesStatsEntOutControlReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 14),
    _NscDxGlSesStatsEntOutControlReqs_Type()
)
nscDxGlSesStatsEntOutControlReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutControlReqs.setStatus("mandatory")
_NscDxGlSesStatsEntOutControlResps_Type = Counter32
_NscDxGlSesStatsEntOutControlResps_Object = MibTableColumn
nscDxGlSesStatsEntOutControlResps = _NscDxGlSesStatsEntOutControlResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 15),
    _NscDxGlSesStatsEntOutControlResps_Type()
)
nscDxGlSesStatsEntOutControlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutControlResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutDevAvailResps_Type = Counter32
_NscDxGlSesStatsEntOutDevAvailResps_Object = MibTableColumn
nscDxGlSesStatsEntOutDevAvailResps = _NscDxGlSesStatsEntOutDevAvailResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 16),
    _NscDxGlSesStatsEntOutDevAvailResps_Type()
)
nscDxGlSesStatsEntOutDevAvailResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutDevAvailResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutDevStatResps_Type = Counter32
_NscDxGlSesStatsEntOutDevStatResps_Object = MibTableColumn
nscDxGlSesStatsEntOutDevStatResps = _NscDxGlSesStatsEntOutDevStatResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 17),
    _NscDxGlSesStatsEntOutDevStatResps_Type()
)
nscDxGlSesStatsEntOutDevStatResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutDevStatResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutInitReqs_Type = Counter32
_NscDxGlSesStatsEntOutInitReqs_Object = MibTableColumn
nscDxGlSesStatsEntOutInitReqs = _NscDxGlSesStatsEntOutInitReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 18),
    _NscDxGlSesStatsEntOutInitReqs_Type()
)
nscDxGlSesStatsEntOutInitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutInitReqs.setStatus("mandatory")
_NscDxGlSesStatsEntOutInitResps_Type = Counter32
_NscDxGlSesStatsEntOutInitResps_Object = MibTableColumn
nscDxGlSesStatsEntOutInitResps = _NscDxGlSesStatsEntOutInitResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 19),
    _NscDxGlSesStatsEntOutInitResps_Type()
)
nscDxGlSesStatsEntOutInitResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutInitResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutReserveReqs_Type = Counter32
_NscDxGlSesStatsEntOutReserveReqs_Object = MibTableColumn
nscDxGlSesStatsEntOutReserveReqs = _NscDxGlSesStatsEntOutReserveReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 20),
    _NscDxGlSesStatsEntOutReserveReqs_Type()
)
nscDxGlSesStatsEntOutReserveReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutReserveReqs.setStatus("mandatory")
_NscDxGlSesStatsEntOutReserveResps_Type = Counter32
_NscDxGlSesStatsEntOutReserveResps_Object = MibTableColumn
nscDxGlSesStatsEntOutReserveResps = _NscDxGlSesStatsEntOutReserveResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 21),
    _NscDxGlSesStatsEntOutReserveResps_Type()
)
nscDxGlSesStatsEntOutReserveResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutReserveResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutSenseReqs_Type = Counter32
_NscDxGlSesStatsEntOutSenseReqs_Object = MibTableColumn
nscDxGlSesStatsEntOutSenseReqs = _NscDxGlSesStatsEntOutSenseReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 22),
    _NscDxGlSesStatsEntOutSenseReqs_Type()
)
nscDxGlSesStatsEntOutSenseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutSenseReqs.setStatus("mandatory")
_NscDxGlSesStatsEntOutSenseResps_Type = Counter32
_NscDxGlSesStatsEntOutSenseResps_Object = MibTableColumn
nscDxGlSesStatsEntOutSenseResps = _NscDxGlSesStatsEntOutSenseResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 23),
    _NscDxGlSesStatsEntOutSenseResps_Type()
)
nscDxGlSesStatsEntOutSenseResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutSenseResps.setStatus("mandatory")
_NscDxGlSesStatsEntOutUnreserveReqs_Type = Counter32
_NscDxGlSesStatsEntOutUnreserveReqs_Object = MibTableColumn
nscDxGlSesStatsEntOutUnreserveReqs = _NscDxGlSesStatsEntOutUnreserveReqs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 24),
    _NscDxGlSesStatsEntOutUnreserveReqs_Type()
)
nscDxGlSesStatsEntOutUnreserveReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutUnreserveReqs.setStatus("mandatory")
_NscDxGlSesStatsEntOutInvalids_Type = Counter32
_NscDxGlSesStatsEntOutInvalids_Object = MibTableColumn
nscDxGlSesStatsEntOutInvalids = _NscDxGlSesStatsEntOutInvalids_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 25),
    _NscDxGlSesStatsEntOutInvalids_Type()
)
nscDxGlSesStatsEntOutInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntOutInvalids.setStatus("mandatory")


class _NscDxGlSesStatsEntHciState_Type(Integer32):
    """Custom type nscDxGlSesStatsEntHciState based on Integer32"""
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
        *(("active", 4),
          ("closed", 1),
          ("hci-wait", 3),
          ("initial-poll", 2))
    )


_NscDxGlSesStatsEntHciState_Type.__name__ = "Integer32"
_NscDxGlSesStatsEntHciState_Object = MibTableColumn
nscDxGlSesStatsEntHciState = _NscDxGlSesStatsEntHciState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 26),
    _NscDxGlSesStatsEntHciState_Type()
)
nscDxGlSesStatsEntHciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntHciState.setStatus("mandatory")


class _NscDxGlSesStatsEntRciState_Type(Integer32):
    """Custom type nscDxGlSesStatsEntRciState based on Integer32"""
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
        *(("active", 4),
          ("closed", 1),
          ("hci-wait", 3),
          ("initial-poll", 2))
    )


_NscDxGlSesStatsEntRciState_Type.__name__ = "Integer32"
_NscDxGlSesStatsEntRciState_Object = MibTableColumn
nscDxGlSesStatsEntRciState = _NscDxGlSesStatsEntRciState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 27),
    _NscDxGlSesStatsEntRciState_Type()
)
nscDxGlSesStatsEntRciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntRciState.setStatus("mandatory")
_NscDxGlSesStatsEntHciMaxSessions_Type = Integer32
_NscDxGlSesStatsEntHciMaxSessions_Object = MibTableColumn
nscDxGlSesStatsEntHciMaxSessions = _NscDxGlSesStatsEntHciMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 28),
    _NscDxGlSesStatsEntHciMaxSessions_Type()
)
nscDxGlSesStatsEntHciMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntHciMaxSessions.setStatus("mandatory")
_NscDxGlSesStatsEntRciMaxSessions_Type = Integer32
_NscDxGlSesStatsEntRciMaxSessions_Object = MibTableColumn
nscDxGlSesStatsEntRciMaxSessions = _NscDxGlSesStatsEntRciMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 29),
    _NscDxGlSesStatsEntRciMaxSessions_Type()
)
nscDxGlSesStatsEntRciMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntRciMaxSessions.setStatus("mandatory")


class _NscDxGlSesStatsEntRciPollStatus_Type(Integer32):
    """Custom type nscDxGlSesStatsEntRciPollStatus based on Integer32"""
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


_NscDxGlSesStatsEntRciPollStatus_Type.__name__ = "Integer32"
_NscDxGlSesStatsEntRciPollStatus_Object = MibTableColumn
nscDxGlSesStatsEntRciPollStatus = _NscDxGlSesStatsEntRciPollStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 30),
    _NscDxGlSesStatsEntRciPollStatus_Type()
)
nscDxGlSesStatsEntRciPollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntRciPollStatus.setStatus("mandatory")
_NscDxGlSesStatsEntRciPollRequests_Type = Counter32
_NscDxGlSesStatsEntRciPollRequests_Object = MibTableColumn
nscDxGlSesStatsEntRciPollRequests = _NscDxGlSesStatsEntRciPollRequests_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 31),
    _NscDxGlSesStatsEntRciPollRequests_Type()
)
nscDxGlSesStatsEntRciPollRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntRciPollRequests.setStatus("mandatory")
_NscDxGlSesStatsEntRciPollDevice_Type = Integer32
_NscDxGlSesStatsEntRciPollDevice_Object = MibTableColumn
nscDxGlSesStatsEntRciPollDevice = _NscDxGlSesStatsEntRciPollDevice_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 4, 1, 32),
    _NscDxGlSesStatsEntRciPollDevice_Type()
)
nscDxGlSesStatsEntRciPollDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesStatsEntRciPollDevice.setStatus("mandatory")
_NscDxGlSesHciConnTable_Object = MibTable
nscDxGlSesHciConnTable = _NscDxGlSesHciConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    nscDxGlSesHciConnTable.setStatus("mandatory")
_NscDxGlSesHciConnEntry_Object = MibTableRow
nscDxGlSesHciConnEntry = _NscDxGlSesHciConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1)
)
nscDxGlSesHciConnEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlSesHciConnEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlSesHciConnEntSesNum"),
)
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntry.setStatus("mandatory")


class _NscDxGlSesHciConnEntKeyId_Type(Integer32):
    """Custom type nscDxGlSesHciConnEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlSesHciConnEntKeyId_Type.__name__ = "Integer32"
_NscDxGlSesHciConnEntKeyId_Object = MibTableColumn
nscDxGlSesHciConnEntKeyId = _NscDxGlSesHciConnEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 1),
    _NscDxGlSesHciConnEntKeyId_Type()
)
nscDxGlSesHciConnEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntKeyId.setStatus("mandatory")
_NscDxGlSesHciConnEntSesNum_Type = Integer32
_NscDxGlSesHciConnEntSesNum_Object = MibTableColumn
nscDxGlSesHciConnEntSesNum = _NscDxGlSesHciConnEntSesNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 2),
    _NscDxGlSesHciConnEntSesNum_Type()
)
nscDxGlSesHciConnEntSesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntSesNum.setStatus("mandatory")
_NscDxGlSesHciConnEntIpAddress_Type = IpAddress
_NscDxGlSesHciConnEntIpAddress_Object = MibTableColumn
nscDxGlSesHciConnEntIpAddress = _NscDxGlSesHciConnEntIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 3),
    _NscDxGlSesHciConnEntIpAddress_Type()
)
nscDxGlSesHciConnEntIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntIpAddress.setStatus("mandatory")


class _NscDxGlSesHciConnEntStatus_Type(Integer32):
    """Custom type nscDxGlSesHciConnEntStatus based on Integer32"""
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
        *(("closed", 1),
          ("closing", 5),
          ("init1", 2),
          ("init2", 3),
          ("open", 4))
    )


_NscDxGlSesHciConnEntStatus_Type.__name__ = "Integer32"
_NscDxGlSesHciConnEntStatus_Object = MibTableColumn
nscDxGlSesHciConnEntStatus = _NscDxGlSesHciConnEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 4),
    _NscDxGlSesHciConnEntStatus_Type()
)
nscDxGlSesHciConnEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntStatus.setStatus("mandatory")


class _NscDxGlSesHciConnEntSendState_Type(Integer32):
    """Custom type nscDxGlSesHciConnEntSendState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("data", 8),
          ("flush", 9),
          ("header", 7),
          ("idle", 6),
          ("trailer", 10))
    )


_NscDxGlSesHciConnEntSendState_Type.__name__ = "Integer32"
_NscDxGlSesHciConnEntSendState_Object = MibTableColumn
nscDxGlSesHciConnEntSendState = _NscDxGlSesHciConnEntSendState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 5),
    _NscDxGlSesHciConnEntSendState_Type()
)
nscDxGlSesHciConnEntSendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntSendState.setStatus("mandatory")


class _NscDxGlSesHciConnEntRecvState_Type(Integer32):
    """Custom type nscDxGlSesHciConnEntRecvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("data", 8),
          ("flush", 9),
          ("header", 7),
          ("idle", 6),
          ("trailer", 10))
    )


_NscDxGlSesHciConnEntRecvState_Type.__name__ = "Integer32"
_NscDxGlSesHciConnEntRecvState_Object = MibTableColumn
nscDxGlSesHciConnEntRecvState = _NscDxGlSesHciConnEntRecvState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 6),
    _NscDxGlSesHciConnEntRecvState_Type()
)
nscDxGlSesHciConnEntRecvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntRecvState.setStatus("mandatory")
_NscDxGlSesHciConnEntAddr_Type = Integer32
_NscDxGlSesHciConnEntAddr_Object = MibTableColumn
nscDxGlSesHciConnEntAddr = _NscDxGlSesHciConnEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 7),
    _NscDxGlSesHciConnEntAddr_Type()
)
nscDxGlSesHciConnEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntAddr.setStatus("mandatory")
_NscDxGlSesHciConnEntFlags_Type = Integer32
_NscDxGlSesHciConnEntFlags_Object = MibTableColumn
nscDxGlSesHciConnEntFlags = _NscDxGlSesHciConnEntFlags_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 8),
    _NscDxGlSesHciConnEntFlags_Type()
)
nscDxGlSesHciConnEntFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntFlags.setStatus("mandatory")
_NscDxGlSesHciConnEntReconn_Type = Integer32
_NscDxGlSesHciConnEntReconn_Object = MibTableColumn
nscDxGlSesHciConnEntReconn = _NscDxGlSesHciConnEntReconn_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 5, 1, 9),
    _NscDxGlSesHciConnEntReconn_Type()
)
nscDxGlSesHciConnEntReconn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesHciConnEntReconn.setStatus("mandatory")
_NscDxGlSesRciConnTable_Object = MibTable
nscDxGlSesRciConnTable = _NscDxGlSesRciConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    nscDxGlSesRciConnTable.setStatus("mandatory")
_NscDxGlSesRciConnEntry_Object = MibTableRow
nscDxGlSesRciConnEntry = _NscDxGlSesRciConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1)
)
nscDxGlSesRciConnEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlSesRciConnEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlSesRciConnEntSesNum"),
)
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntry.setStatus("mandatory")


class _NscDxGlSesRciConnEntKeyId_Type(Integer32):
    """Custom type nscDxGlSesRciConnEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlSesRciConnEntKeyId_Type.__name__ = "Integer32"
_NscDxGlSesRciConnEntKeyId_Object = MibTableColumn
nscDxGlSesRciConnEntKeyId = _NscDxGlSesRciConnEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 1),
    _NscDxGlSesRciConnEntKeyId_Type()
)
nscDxGlSesRciConnEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntKeyId.setStatus("mandatory")
_NscDxGlSesRciConnEntSesNum_Type = Integer32
_NscDxGlSesRciConnEntSesNum_Object = MibTableColumn
nscDxGlSesRciConnEntSesNum = _NscDxGlSesRciConnEntSesNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 2),
    _NscDxGlSesRciConnEntSesNum_Type()
)
nscDxGlSesRciConnEntSesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntSesNum.setStatus("mandatory")
_NscDxGlSesRciConnEntIpAddress_Type = IpAddress
_NscDxGlSesRciConnEntIpAddress_Object = MibTableColumn
nscDxGlSesRciConnEntIpAddress = _NscDxGlSesRciConnEntIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 3),
    _NscDxGlSesRciConnEntIpAddress_Type()
)
nscDxGlSesRciConnEntIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntIpAddress.setStatus("mandatory")


class _NscDxGlSesRciConnEntStatus_Type(Integer32):
    """Custom type nscDxGlSesRciConnEntStatus based on Integer32"""
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
        *(("closed", 1),
          ("closing", 5),
          ("init1", 2),
          ("init2", 3),
          ("open", 4))
    )


_NscDxGlSesRciConnEntStatus_Type.__name__ = "Integer32"
_NscDxGlSesRciConnEntStatus_Object = MibTableColumn
nscDxGlSesRciConnEntStatus = _NscDxGlSesRciConnEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 4),
    _NscDxGlSesRciConnEntStatus_Type()
)
nscDxGlSesRciConnEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntStatus.setStatus("mandatory")


class _NscDxGlSesRciConnEntSendState_Type(Integer32):
    """Custom type nscDxGlSesRciConnEntSendState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("data", 8),
          ("flush", 9),
          ("header", 7),
          ("idle", 6),
          ("trailer", 10))
    )


_NscDxGlSesRciConnEntSendState_Type.__name__ = "Integer32"
_NscDxGlSesRciConnEntSendState_Object = MibTableColumn
nscDxGlSesRciConnEntSendState = _NscDxGlSesRciConnEntSendState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 5),
    _NscDxGlSesRciConnEntSendState_Type()
)
nscDxGlSesRciConnEntSendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntSendState.setStatus("mandatory")


class _NscDxGlSesRciConnEntRecvState_Type(Integer32):
    """Custom type nscDxGlSesRciConnEntRecvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("data", 8),
          ("flush", 9),
          ("header", 7),
          ("idle", 6),
          ("trailer", 10))
    )


_NscDxGlSesRciConnEntRecvState_Type.__name__ = "Integer32"
_NscDxGlSesRciConnEntRecvState_Object = MibTableColumn
nscDxGlSesRciConnEntRecvState = _NscDxGlSesRciConnEntRecvState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 6),
    _NscDxGlSesRciConnEntRecvState_Type()
)
nscDxGlSesRciConnEntRecvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntRecvState.setStatus("mandatory")
_NscDxGlSesRciConnEntAddr_Type = Integer32
_NscDxGlSesRciConnEntAddr_Object = MibTableColumn
nscDxGlSesRciConnEntAddr = _NscDxGlSesRciConnEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 7),
    _NscDxGlSesRciConnEntAddr_Type()
)
nscDxGlSesRciConnEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntAddr.setStatus("mandatory")
_NscDxGlSesRciConnEntFlags_Type = Integer32
_NscDxGlSesRciConnEntFlags_Object = MibTableColumn
nscDxGlSesRciConnEntFlags = _NscDxGlSesRciConnEntFlags_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 6, 1, 8),
    _NscDxGlSesRciConnEntFlags_Type()
)
nscDxGlSesRciConnEntFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesRciConnEntFlags.setStatus("mandatory")
_NscDxGlSesDevTable_Object = MibTable
nscDxGlSesDevTable = _NscDxGlSesDevTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7)
)
if mibBuilder.loadTexts:
    nscDxGlSesDevTable.setStatus("mandatory")
_NscDxGlSesDevEntry_Object = MibTableRow
nscDxGlSesDevEntry = _NscDxGlSesDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1)
)
nscDxGlSesDevEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlSesDevEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlSesDevEntDevice"),
)
if mibBuilder.loadTexts:
    nscDxGlSesDevEntry.setStatus("mandatory")


class _NscDxGlSesDevEntKeyId_Type(Integer32):
    """Custom type nscDxGlSesDevEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlSesDevEntKeyId_Type.__name__ = "Integer32"
_NscDxGlSesDevEntKeyId_Object = MibTableColumn
nscDxGlSesDevEntKeyId = _NscDxGlSesDevEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 1),
    _NscDxGlSesDevEntKeyId_Type()
)
nscDxGlSesDevEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntKeyId.setStatus("mandatory")


class _NscDxGlSesDevEntDevice_Type(Integer32):
    """Custom type nscDxGlSesDevEntDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NscDxGlSesDevEntDevice_Type.__name__ = "Integer32"
_NscDxGlSesDevEntDevice_Object = MibTableColumn
nscDxGlSesDevEntDevice = _NscDxGlSesDevEntDevice_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 2),
    _NscDxGlSesDevEntDevice_Type()
)
nscDxGlSesDevEntDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntDevice.setStatus("mandatory")
_NscDxGlSesDevEntReserve_Type = Integer32
_NscDxGlSesDevEntReserve_Object = MibTableColumn
nscDxGlSesDevEntReserve = _NscDxGlSesDevEntReserve_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 3),
    _NscDxGlSesDevEntReserve_Type()
)
nscDxGlSesDevEntReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntReserve.setStatus("mandatory")
_NscDxGlSesDevEntPrimed_Type = Integer32
_NscDxGlSesDevEntPrimed_Object = MibTableColumn
nscDxGlSesDevEntPrimed = _NscDxGlSesDevEntPrimed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 4),
    _NscDxGlSesDevEntPrimed_Type()
)
nscDxGlSesDevEntPrimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntPrimed.setStatus("mandatory")
_NscDxGlSesDevEntStat_Type = Integer32
_NscDxGlSesDevEntStat_Object = MibTableColumn
nscDxGlSesDevEntStat = _NscDxGlSesDevEntStat_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 5),
    _NscDxGlSesDevEntStat_Type()
)
nscDxGlSesDevEntStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntStat.setStatus("mandatory")


class _NscDxGlSesDevEntSenseData_Type(OctetString):
    """Custom type nscDxGlSesDevEntSenseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_NscDxGlSesDevEntSenseData_Type.__name__ = "OctetString"
_NscDxGlSesDevEntSenseData_Object = MibTableColumn
nscDxGlSesDevEntSenseData = _NscDxGlSesDevEntSenseData_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 7, 1, 6),
    _NscDxGlSesDevEntSenseData_Type()
)
nscDxGlSesDevEntSenseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlSesDevEntSenseData.setStatus("mandatory")
_NscDxGlXportStatsTable_Object = MibTable
nscDxGlXportStatsTable = _NscDxGlXportStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8)
)
if mibBuilder.loadTexts:
    nscDxGlXportStatsTable.setStatus("mandatory")
_NscDxGlXportStatsEntry_Object = MibTableRow
nscDxGlXportStatsEntry = _NscDxGlXportStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1)
)
nscDxGlXportStatsEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlXportStatsEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntry.setStatus("mandatory")


class _NscDxGlXportStatsEntKeyId_Type(Integer32):
    """Custom type nscDxGlXportStatsEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlXportStatsEntKeyId_Type.__name__ = "Integer32"
_NscDxGlXportStatsEntKeyId_Object = MibTableColumn
nscDxGlXportStatsEntKeyId = _NscDxGlXportStatsEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 1),
    _NscDxGlXportStatsEntKeyId_Type()
)
nscDxGlXportStatsEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntKeyId.setStatus("mandatory")
_NscDxGlXportStatsEntInAcks_Type = Counter32
_NscDxGlXportStatsEntInAcks_Object = MibTableColumn
nscDxGlXportStatsEntInAcks = _NscDxGlXportStatsEntInAcks_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 2),
    _NscDxGlXportStatsEntInAcks_Type()
)
nscDxGlXportStatsEntInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInAcks.setStatus("mandatory")
_NscDxGlXportStatsEntInConnects_Type = Counter32
_NscDxGlXportStatsEntInConnects_Object = MibTableColumn
nscDxGlXportStatsEntInConnects = _NscDxGlXportStatsEntInConnects_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 3),
    _NscDxGlXportStatsEntInConnects_Type()
)
nscDxGlXportStatsEntInConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInConnects.setStatus("mandatory")
_NscDxGlXportStatsEntInDataDups_Type = Counter32
_NscDxGlXportStatsEntInDataDups_Object = MibTableColumn
nscDxGlXportStatsEntInDataDups = _NscDxGlXportStatsEntInDataDups_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 4),
    _NscDxGlXportStatsEntInDataDups_Type()
)
nscDxGlXportStatsEntInDataDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInDataDups.setStatus("mandatory")
_NscDxGlXportStatsEntInDataInOrders_Type = Counter32
_NscDxGlXportStatsEntInDataInOrders_Object = MibTableColumn
nscDxGlXportStatsEntInDataInOrders = _NscDxGlXportStatsEntInDataInOrders_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 5),
    _NscDxGlXportStatsEntInDataInOrders_Type()
)
nscDxGlXportStatsEntInDataInOrders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInDataInOrders.setStatus("mandatory")
_NscDxGlXportStatsEntInDataInvalids_Type = Counter32
_NscDxGlXportStatsEntInDataInvalids_Object = MibTableColumn
nscDxGlXportStatsEntInDataInvalids = _NscDxGlXportStatsEntInDataInvalids_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 6),
    _NscDxGlXportStatsEntInDataInvalids_Type()
)
nscDxGlXportStatsEntInDataInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInDataInvalids.setStatus("mandatory")
_NscDxGlXportStatsEntInDataInWindows_Type = Counter32
_NscDxGlXportStatsEntInDataInWindows_Object = MibTableColumn
nscDxGlXportStatsEntInDataInWindows = _NscDxGlXportStatsEntInDataInWindows_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 7),
    _NscDxGlXportStatsEntInDataInWindows_Type()
)
nscDxGlXportStatsEntInDataInWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInDataInWindows.setStatus("mandatory")
_NscDxGlXportStatsEntInDiscs_Type = Counter32
_NscDxGlXportStatsEntInDiscs_Object = MibTableColumn
nscDxGlXportStatsEntInDiscs = _NscDxGlXportStatsEntInDiscs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 8),
    _NscDxGlXportStatsEntInDiscs_Type()
)
nscDxGlXportStatsEntInDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInDiscs.setStatus("mandatory")
_NscDxGlXportStatsEntInNacks_Type = Counter32
_NscDxGlXportStatsEntInNacks_Object = MibTableColumn
nscDxGlXportStatsEntInNacks = _NscDxGlXportStatsEntInNacks_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 9),
    _NscDxGlXportStatsEntInNacks_Type()
)
nscDxGlXportStatsEntInNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInNacks.setStatus("mandatory")
_NscDxGlXportStatsEntInProbes_Type = Counter32
_NscDxGlXportStatsEntInProbes_Object = MibTableColumn
nscDxGlXportStatsEntInProbes = _NscDxGlXportStatsEntInProbes_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 10),
    _NscDxGlXportStatsEntInProbes_Type()
)
nscDxGlXportStatsEntInProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInProbes.setStatus("mandatory")
_NscDxGlXportStatsEntInProbeResps_Type = Counter32
_NscDxGlXportStatsEntInProbeResps_Object = MibTableColumn
nscDxGlXportStatsEntInProbeResps = _NscDxGlXportStatsEntInProbeResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 11),
    _NscDxGlXportStatsEntInProbeResps_Type()
)
nscDxGlXportStatsEntInProbeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInProbeResps.setStatus("mandatory")
_NscDxGlXportStatsEntBadPckts_Type = Counter32
_NscDxGlXportStatsEntBadPckts_Object = MibTableColumn
nscDxGlXportStatsEntBadPckts = _NscDxGlXportStatsEntBadPckts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 12),
    _NscDxGlXportStatsEntBadPckts_Type()
)
nscDxGlXportStatsEntBadPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntBadPckts.setStatus("mandatory")
_NscDxGlXportStatsEntBadXcbs_Type = Counter32
_NscDxGlXportStatsEntBadXcbs_Object = MibTableColumn
nscDxGlXportStatsEntBadXcbs = _NscDxGlXportStatsEntBadXcbs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 13),
    _NscDxGlXportStatsEntBadXcbs_Type()
)
nscDxGlXportStatsEntBadXcbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntBadXcbs.setStatus("mandatory")
_NscDxGlXportStatsEntOutAcks_Type = Counter32
_NscDxGlXportStatsEntOutAcks_Object = MibTableColumn
nscDxGlXportStatsEntOutAcks = _NscDxGlXportStatsEntOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 14),
    _NscDxGlXportStatsEntOutAcks_Type()
)
nscDxGlXportStatsEntOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutAcks.setStatus("mandatory")
_NscDxGlXportStatsEntOutConnects_Type = Counter32
_NscDxGlXportStatsEntOutConnects_Object = MibTableColumn
nscDxGlXportStatsEntOutConnects = _NscDxGlXportStatsEntOutConnects_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 15),
    _NscDxGlXportStatsEntOutConnects_Type()
)
nscDxGlXportStatsEntOutConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutConnects.setStatus("mandatory")
_NscDxGlXportStatsEntOutDatas_Type = Counter32
_NscDxGlXportStatsEntOutDatas_Object = MibTableColumn
nscDxGlXportStatsEntOutDatas = _NscDxGlXportStatsEntOutDatas_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 16),
    _NscDxGlXportStatsEntOutDatas_Type()
)
nscDxGlXportStatsEntOutDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutDatas.setStatus("mandatory")
_NscDxGlXportStatsEntOutDiscs_Type = Counter32
_NscDxGlXportStatsEntOutDiscs_Object = MibTableColumn
nscDxGlXportStatsEntOutDiscs = _NscDxGlXportStatsEntOutDiscs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 17),
    _NscDxGlXportStatsEntOutDiscs_Type()
)
nscDxGlXportStatsEntOutDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutDiscs.setStatus("mandatory")
_NscDxGlXportStatsEntOutNacks_Type = Counter32
_NscDxGlXportStatsEntOutNacks_Object = MibTableColumn
nscDxGlXportStatsEntOutNacks = _NscDxGlXportStatsEntOutNacks_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 18),
    _NscDxGlXportStatsEntOutNacks_Type()
)
nscDxGlXportStatsEntOutNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutNacks.setStatus("mandatory")
_NscDxGlXportStatsEntOutProbes_Type = Counter32
_NscDxGlXportStatsEntOutProbes_Object = MibTableColumn
nscDxGlXportStatsEntOutProbes = _NscDxGlXportStatsEntOutProbes_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 19),
    _NscDxGlXportStatsEntOutProbes_Type()
)
nscDxGlXportStatsEntOutProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutProbes.setStatus("mandatory")
_NscDxGlXportStatsEntOutProbeResps_Type = Counter32
_NscDxGlXportStatsEntOutProbeResps_Object = MibTableColumn
nscDxGlXportStatsEntOutProbeResps = _NscDxGlXportStatsEntOutProbeResps_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 20),
    _NscDxGlXportStatsEntOutProbeResps_Type()
)
nscDxGlXportStatsEntOutProbeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutProbeResps.setStatus("mandatory")
_NscDxGlXportStatsEntReconns_Type = Counter32
_NscDxGlXportStatsEntReconns_Object = MibTableColumn
nscDxGlXportStatsEntReconns = _NscDxGlXportStatsEntReconns_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 21),
    _NscDxGlXportStatsEntReconns_Type()
)
nscDxGlXportStatsEntReconns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntReconns.setStatus("mandatory")
_NscDxGlXportStatsEntRetransmits_Type = Counter32
_NscDxGlXportStatsEntRetransmits_Object = MibTableColumn
nscDxGlXportStatsEntRetransmits = _NscDxGlXportStatsEntRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 22),
    _NscDxGlXportStatsEntRetransmits_Type()
)
nscDxGlXportStatsEntRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntRetransmits.setStatus("mandatory")
_NscDxGlXportStatsEntBadChecksums_Type = Counter32
_NscDxGlXportStatsEntBadChecksums_Object = MibTableColumn
nscDxGlXportStatsEntBadChecksums = _NscDxGlXportStatsEntBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 23),
    _NscDxGlXportStatsEntBadChecksums_Type()
)
nscDxGlXportStatsEntBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntBadChecksums.setStatus("mandatory")
_NscDxGlXportStatsEntBadVersions_Type = Counter32
_NscDxGlXportStatsEntBadVersions_Object = MibTableColumn
nscDxGlXportStatsEntBadVersions = _NscDxGlXportStatsEntBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 24),
    _NscDxGlXportStatsEntBadVersions_Type()
)
nscDxGlXportStatsEntBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntBadVersions.setStatus("mandatory")
_NscDxGlXportStatsEntConnTimeouts_Type = Counter32
_NscDxGlXportStatsEntConnTimeouts_Object = MibTableColumn
nscDxGlXportStatsEntConnTimeouts = _NscDxGlXportStatsEntConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 25),
    _NscDxGlXportStatsEntConnTimeouts_Type()
)
nscDxGlXportStatsEntConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntConnTimeouts.setStatus("mandatory")
_NscDxGlXportStatsEntInitXcbExists_Type = Counter32
_NscDxGlXportStatsEntInitXcbExists_Object = MibTableColumn
nscDxGlXportStatsEntInitXcbExists = _NscDxGlXportStatsEntInitXcbExists_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 26),
    _NscDxGlXportStatsEntInitXcbExists_Type()
)
nscDxGlXportStatsEntInitXcbExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntInitXcbExists.setStatus("mandatory")
_NscDxGlXportStatsEntNoHdrSpaces_Type = Counter32
_NscDxGlXportStatsEntNoHdrSpaces_Object = MibTableColumn
nscDxGlXportStatsEntNoHdrSpaces = _NscDxGlXportStatsEntNoHdrSpaces_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 27),
    _NscDxGlXportStatsEntNoHdrSpaces_Type()
)
nscDxGlXportStatsEntNoHdrSpaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntNoHdrSpaces.setStatus("mandatory")
_NscDxGlXportStatsEntNoMemorys_Type = Counter32
_NscDxGlXportStatsEntNoMemorys_Object = MibTableColumn
nscDxGlXportStatsEntNoMemorys = _NscDxGlXportStatsEntNoMemorys_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 28),
    _NscDxGlXportStatsEntNoMemorys_Type()
)
nscDxGlXportStatsEntNoMemorys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntNoMemorys.setStatus("mandatory")
_NscDxGlXportStatsEntNoPes_Type = Counter32
_NscDxGlXportStatsEntNoPes_Object = MibTableColumn
nscDxGlXportStatsEntNoPes = _NscDxGlXportStatsEntNoPes_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 29),
    _NscDxGlXportStatsEntNoPes_Type()
)
nscDxGlXportStatsEntNoPes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntNoPes.setStatus("mandatory")
_NscDxGlXportStatsEntOutOfSeqDatas_Type = Counter32
_NscDxGlXportStatsEntOutOfSeqDatas_Object = MibTableColumn
nscDxGlXportStatsEntOutOfSeqDatas = _NscDxGlXportStatsEntOutOfSeqDatas_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 30),
    _NscDxGlXportStatsEntOutOfSeqDatas_Type()
)
nscDxGlXportStatsEntOutOfSeqDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntOutOfSeqDatas.setStatus("mandatory")
_NscDxGlXportStatsEntShortPackets_Type = Counter32
_NscDxGlXportStatsEntShortPackets_Object = MibTableColumn
nscDxGlXportStatsEntShortPackets = _NscDxGlXportStatsEntShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 8, 1, 31),
    _NscDxGlXportStatsEntShortPackets_Type()
)
nscDxGlXportStatsEntShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportStatsEntShortPackets.setStatus("mandatory")
_NscDxGlXportConnTable_Object = MibTable
nscDxGlXportConnTable = _NscDxGlXportConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9)
)
if mibBuilder.loadTexts:
    nscDxGlXportConnTable.setStatus("mandatory")
_NscDxGlXportConnEntry_Object = MibTableRow
nscDxGlXportConnEntry = _NscDxGlXportConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1)
)
nscDxGlXportConnEntry.setIndexNames(
    (0, "NSCDXGLIP-MIB", "nscDxGlXportConnEntKeyId"),
    (0, "NSCDXGLIP-MIB", "nscDxGlXportConnEntNum"),
)
if mibBuilder.loadTexts:
    nscDxGlXportConnEntry.setStatus("mandatory")


class _NscDxGlXportConnEntKeyId_Type(Integer32):
    """Custom type nscDxGlXportConnEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxGlXportConnEntKeyId_Type.__name__ = "Integer32"
_NscDxGlXportConnEntKeyId_Object = MibTableColumn
nscDxGlXportConnEntKeyId = _NscDxGlXportConnEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 1),
    _NscDxGlXportConnEntKeyId_Type()
)
nscDxGlXportConnEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntKeyId.setStatus("mandatory")
_NscDxGlXportConnEntNum_Type = Integer32
_NscDxGlXportConnEntNum_Object = MibTableColumn
nscDxGlXportConnEntNum = _NscDxGlXportConnEntNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 2),
    _NscDxGlXportConnEntNum_Type()
)
nscDxGlXportConnEntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntNum.setStatus("mandatory")
_NscDxGlXportConnEntLocalAddress_Type = IpAddress
_NscDxGlXportConnEntLocalAddress_Object = MibTableColumn
nscDxGlXportConnEntLocalAddress = _NscDxGlXportConnEntLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 3),
    _NscDxGlXportConnEntLocalAddress_Type()
)
nscDxGlXportConnEntLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntLocalAddress.setStatus("mandatory")
_NscDxGlXportConnEntLocalPort_Type = Integer32
_NscDxGlXportConnEntLocalPort_Object = MibTableColumn
nscDxGlXportConnEntLocalPort = _NscDxGlXportConnEntLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 4),
    _NscDxGlXportConnEntLocalPort_Type()
)
nscDxGlXportConnEntLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntLocalPort.setStatus("mandatory")
_NscDxGlXportConnEntRemoteAddress_Type = IpAddress
_NscDxGlXportConnEntRemoteAddress_Object = MibTableColumn
nscDxGlXportConnEntRemoteAddress = _NscDxGlXportConnEntRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 5),
    _NscDxGlXportConnEntRemoteAddress_Type()
)
nscDxGlXportConnEntRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntRemoteAddress.setStatus("mandatory")
_NscDxGlXportConnEntRemotePort_Type = Integer32
_NscDxGlXportConnEntRemotePort_Object = MibTableColumn
nscDxGlXportConnEntRemotePort = _NscDxGlXportConnEntRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 6),
    _NscDxGlXportConnEntRemotePort_Type()
)
nscDxGlXportConnEntRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntRemotePort.setStatus("mandatory")
_NscDxGlXportConnEntXopt_Type = Integer32
_NscDxGlXportConnEntXopt_Object = MibTableColumn
nscDxGlXportConnEntXopt = _NscDxGlXportConnEntXopt_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 7),
    _NscDxGlXportConnEntXopt_Type()
)
nscDxGlXportConnEntXopt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntXopt.setStatus("mandatory")
_NscDxGlXportConnEntWindowSize_Type = Integer32
_NscDxGlXportConnEntWindowSize_Object = MibTableColumn
nscDxGlXportConnEntWindowSize = _NscDxGlXportConnEntWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 8),
    _NscDxGlXportConnEntWindowSize_Type()
)
nscDxGlXportConnEntWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntWindowSize.setStatus("mandatory")
_NscDxGlXportConnEntRoundTripTime_Type = Integer32
_NscDxGlXportConnEntRoundTripTime_Object = MibScalar
nscDxGlXportConnEntRoundTripTime = _NscDxGlXportConnEntRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 9),
    _NscDxGlXportConnEntRoundTripTime_Type()
)
nscDxGlXportConnEntRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntRoundTripTime.setStatus("mandatory")
_NscDxGlXportConnEntSeqNumber_Type = Integer32
_NscDxGlXportConnEntSeqNumber_Object = MibTableColumn
nscDxGlXportConnEntSeqNumber = _NscDxGlXportConnEntSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 10),
    _NscDxGlXportConnEntSeqNumber_Type()
)
nscDxGlXportConnEntSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntSeqNumber.setStatus("mandatory")
_NscDxGlXportConnEntXcbFlags_Type = Integer32
_NscDxGlXportConnEntXcbFlags_Object = MibTableColumn
nscDxGlXportConnEntXcbFlags = _NscDxGlXportConnEntXcbFlags_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 4, 9, 1, 11),
    _NscDxGlXportConnEntXcbFlags_Type()
)
nscDxGlXportConnEntXcbFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxGlXportConnEntXcbFlags.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCDXGLIP-MIB",
    **{"nscDxGreenline": nscDxGreenline,
       "nscDxGlChannelTable": nscDxGlChannelTable,
       "nscDxGlChannelEntry": nscDxGlChannelEntry,
       "nscDxGlChanEntKeyId": nscDxGlChanEntKeyId,
       "nscDxGlChanEntType": nscDxGlChanEntType,
       "nscDxGlChanEntActivityState": nscDxGlChanEntActivityState,
       "nscDxGlChanEntResetState": nscDxGlChanEntResetState,
       "nscDxGlChanEntIplState": nscDxGlChanEntIplState,
       "nscDxGlChanEntIpState": nscDxGlChanEntIpState,
       "nscDxGlChanEntOnlineOfflineState": nscDxGlChanEntOnlineOfflineState,
       "nscDxGlChanEntPolling": nscDxGlChanEntPolling,
       "nscDxGlChanEntActiveSubchannel": nscDxGlChanEntActiveSubchannel,
       "nscDxGlChanEntMemoryResourcesLimited": nscDxGlChanEntMemoryResourcesLimited,
       "nscDxGlChanEntTagOverruns": nscDxGlChanEntTagOverruns,
       "nscDxGlChanEntDcOverruns": nscDxGlChanEntDcOverruns,
       "nscDxGlChanEntDsOverruns": nscDxGlChanEntDsOverruns,
       "nscDxGlChanEntDmaParityErrors": nscDxGlChanEntDmaParityErrors,
       "nscDxGlChanEntCrcErrors": nscDxGlChanEntCrcErrors,
       "nscDxGlChanEntResetsDuringDma": nscDxGlChanEntResetsDuringDma,
       "nscDxGlChanEntCmdParityErrors": nscDxGlChanEntCmdParityErrors,
       "nscDxGlChanEntUnsupportedStatuses": nscDxGlChanEntUnsupportedStatuses,
       "nscDxGlChanEntMiscompareParityErrors": nscDxGlChanEntMiscompareParityErrors,
       "nscDxGlChanEntSelectionTimeouts": nscDxGlChanEntSelectionTimeouts,
       "nscDxGlChanEntStatusAcceptDiscIns": nscDxGlChanEntStatusAcceptDiscIns,
       "nscDxGlChanEntStatusAcceptTimeouts": nscDxGlChanEntStatusAcceptTimeouts,
       "nscDxGlChanEntStatusWaitDiscIns": nscDxGlChanEntStatusWaitDiscIns,
       "nscDxGlChanEntStatusWaitTimeouts": nscDxGlChanEntStatusWaitTimeouts,
       "nscDxGlChanEntOpInActiveTimeouts": nscDxGlChanEntOpInActiveTimeouts,
       "nscDxGlChanEntNumCus": nscDxGlChanEntNumCus,
       "nscDxGlChanEntChannelStatus": nscDxGlChanEntChannelStatus,
       "nscDxGlProfiles": nscDxGlProfiles,
       "nscDxGlProfControlUnitTable": nscDxGlProfControlUnitTable,
       "nscDxGlProfControlUnitEntry": nscDxGlProfControlUnitEntry,
       "nscDxGlProfCuEntKeyId": nscDxGlProfCuEntKeyId,
       "nscDxGlProfCuEntCuNum": nscDxGlProfCuEntCuNum,
       "nscDxGlProfCuEntNumDevices": nscDxGlProfCuEntNumDevices,
       "nscDxGlProfCuEntOnlineOfflineState": nscDxGlProfCuEntOnlineOfflineState,
       "nscDxGlProfCuEntDeviceType": nscDxGlProfCuEntDeviceType,
       "nscDxGlProfCuEntHostStartingDevAddr": nscDxGlProfCuEntHostStartingDevAddr,
       "nscDxGlProfCuEntHostEndingDevAddr": nscDxGlProfCuEntHostEndingDevAddr,
       "nscDxGlProfCuEntHostChannelSpeed": nscDxGlProfCuEntHostChannelSpeed,
       "nscDxGlProfCuEntHostBufferRequirements": nscDxGlProfCuEntHostBufferRequirements,
       "nscDxGlProfCuEntRmtIpAddr": nscDxGlProfCuEntRmtIpAddr,
       "nscDxGlProfCuEntRmtStartingDevAddr": nscDxGlProfCuEntRmtStartingDevAddr,
       "nscDxGlProfCuEntRmtBufferHold": nscDxGlProfCuEntRmtBufferHold,
       "nscDxGlProfCuEntRmtChannelSpeed": nscDxGlProfCuEntRmtChannelSpeed,
       "nscDxGlProfCuEntRmtBufferRequirements": nscDxGlProfCuEntRmtBufferRequirements,
       "nscDxGlProfCuEntUnsolStatusOption": nscDxGlProfCuEntUnsolStatusOption,
       "nscDxGlProfCuEntDevDriverOptions": nscDxGlProfCuEntDevDriverOptions,
       "nscDxGlProfCuEntHostBufferHold": nscDxGlProfCuEntHostBufferHold,
       "nscDxGlProfCuEntWindowSize": nscDxGlProfCuEntWindowSize,
       "nscDxGlProfDeviceTable": nscDxGlProfDeviceTable,
       "nscDxGlProfDeviceEntry": nscDxGlProfDeviceEntry,
       "nscDxGlProfDevEntKeyId": nscDxGlProfDevEntKeyId,
       "nscDxGlProfDevEntDevice": nscDxGlProfDevEntDevice,
       "nscDxGlProfDevEntOnOff": nscDxGlProfDevEntOnOff,
       "nscDxGlDevStatusTable": nscDxGlDevStatusTable,
       "nscDxGlDevStatusEntry": nscDxGlDevStatusEntry,
       "nscDxGlDevStatusEntKeyId": nscDxGlDevStatusEntKeyId,
       "nscDxGlDevStatusEntDeviceNum": nscDxGlDevStatusEntDeviceNum,
       "nscDxGlDevStatusEntHostDevAddr": nscDxGlDevStatusEntHostDevAddr,
       "nscDxGlDevStatusEntRmtDevAddr": nscDxGlDevStatusEntRmtDevAddr,
       "nscDxGlDevStatusEntOnOffState": nscDxGlDevStatusEntOnOffState,
       "nscDxGlDevStatusEntReservedState": nscDxGlDevStatusEntReservedState,
       "nscDxGlSesStatsTable": nscDxGlSesStatsTable,
       "nscDxGlSesStatsEntry": nscDxGlSesStatsEntry,
       "nscDxGlSesStatsEntKeyId": nscDxGlSesStatsEntKeyId,
       "nscDxGlSesStatsEntInControlReqs": nscDxGlSesStatsEntInControlReqs,
       "nscDxGlSesStatsEntInControlResps": nscDxGlSesStatsEntInControlResps,
       "nscDxGlSesStatsEntInDevAvailResps": nscDxGlSesStatsEntInDevAvailResps,
       "nscDxGlSesStatsEntInDevStatResps": nscDxGlSesStatsEntInDevStatResps,
       "nscDxGlSesStatsEntInInitReqs": nscDxGlSesStatsEntInInitReqs,
       "nscDxGlSesStatsEntInInitResps": nscDxGlSesStatsEntInInitResps,
       "nscDxGlSesStatsEntInReserveReqs": nscDxGlSesStatsEntInReserveReqs,
       "nscDxGlSesStatsEntInReserveResps": nscDxGlSesStatsEntInReserveResps,
       "nscDxGlSesStatsEntInSenseReqs": nscDxGlSesStatsEntInSenseReqs,
       "nscDxGlSesStatsEntInSenseResps": nscDxGlSesStatsEntInSenseResps,
       "nscDxGlSesStatsEntInUnreserveReqs": nscDxGlSesStatsEntInUnreserveReqs,
       "nscDxGlSesStatsEntInInvalids": nscDxGlSesStatsEntInInvalids,
       "nscDxGlSesStatsEntOutControlReqs": nscDxGlSesStatsEntOutControlReqs,
       "nscDxGlSesStatsEntOutControlResps": nscDxGlSesStatsEntOutControlResps,
       "nscDxGlSesStatsEntOutDevAvailResps": nscDxGlSesStatsEntOutDevAvailResps,
       "nscDxGlSesStatsEntOutDevStatResps": nscDxGlSesStatsEntOutDevStatResps,
       "nscDxGlSesStatsEntOutInitReqs": nscDxGlSesStatsEntOutInitReqs,
       "nscDxGlSesStatsEntOutInitResps": nscDxGlSesStatsEntOutInitResps,
       "nscDxGlSesStatsEntOutReserveReqs": nscDxGlSesStatsEntOutReserveReqs,
       "nscDxGlSesStatsEntOutReserveResps": nscDxGlSesStatsEntOutReserveResps,
       "nscDxGlSesStatsEntOutSenseReqs": nscDxGlSesStatsEntOutSenseReqs,
       "nscDxGlSesStatsEntOutSenseResps": nscDxGlSesStatsEntOutSenseResps,
       "nscDxGlSesStatsEntOutUnreserveReqs": nscDxGlSesStatsEntOutUnreserveReqs,
       "nscDxGlSesStatsEntOutInvalids": nscDxGlSesStatsEntOutInvalids,
       "nscDxGlSesStatsEntHciState": nscDxGlSesStatsEntHciState,
       "nscDxGlSesStatsEntRciState": nscDxGlSesStatsEntRciState,
       "nscDxGlSesStatsEntHciMaxSessions": nscDxGlSesStatsEntHciMaxSessions,
       "nscDxGlSesStatsEntRciMaxSessions": nscDxGlSesStatsEntRciMaxSessions,
       "nscDxGlSesStatsEntRciPollStatus": nscDxGlSesStatsEntRciPollStatus,
       "nscDxGlSesStatsEntRciPollRequests": nscDxGlSesStatsEntRciPollRequests,
       "nscDxGlSesStatsEntRciPollDevice": nscDxGlSesStatsEntRciPollDevice,
       "nscDxGlSesHciConnTable": nscDxGlSesHciConnTable,
       "nscDxGlSesHciConnEntry": nscDxGlSesHciConnEntry,
       "nscDxGlSesHciConnEntKeyId": nscDxGlSesHciConnEntKeyId,
       "nscDxGlSesHciConnEntSesNum": nscDxGlSesHciConnEntSesNum,
       "nscDxGlSesHciConnEntIpAddress": nscDxGlSesHciConnEntIpAddress,
       "nscDxGlSesHciConnEntStatus": nscDxGlSesHciConnEntStatus,
       "nscDxGlSesHciConnEntSendState": nscDxGlSesHciConnEntSendState,
       "nscDxGlSesHciConnEntRecvState": nscDxGlSesHciConnEntRecvState,
       "nscDxGlSesHciConnEntAddr": nscDxGlSesHciConnEntAddr,
       "nscDxGlSesHciConnEntFlags": nscDxGlSesHciConnEntFlags,
       "nscDxGlSesHciConnEntReconn": nscDxGlSesHciConnEntReconn,
       "nscDxGlSesRciConnTable": nscDxGlSesRciConnTable,
       "nscDxGlSesRciConnEntry": nscDxGlSesRciConnEntry,
       "nscDxGlSesRciConnEntKeyId": nscDxGlSesRciConnEntKeyId,
       "nscDxGlSesRciConnEntSesNum": nscDxGlSesRciConnEntSesNum,
       "nscDxGlSesRciConnEntIpAddress": nscDxGlSesRciConnEntIpAddress,
       "nscDxGlSesRciConnEntStatus": nscDxGlSesRciConnEntStatus,
       "nscDxGlSesRciConnEntSendState": nscDxGlSesRciConnEntSendState,
       "nscDxGlSesRciConnEntRecvState": nscDxGlSesRciConnEntRecvState,
       "nscDxGlSesRciConnEntAddr": nscDxGlSesRciConnEntAddr,
       "nscDxGlSesRciConnEntFlags": nscDxGlSesRciConnEntFlags,
       "nscDxGlSesDevTable": nscDxGlSesDevTable,
       "nscDxGlSesDevEntry": nscDxGlSesDevEntry,
       "nscDxGlSesDevEntKeyId": nscDxGlSesDevEntKeyId,
       "nscDxGlSesDevEntDevice": nscDxGlSesDevEntDevice,
       "nscDxGlSesDevEntReserve": nscDxGlSesDevEntReserve,
       "nscDxGlSesDevEntPrimed": nscDxGlSesDevEntPrimed,
       "nscDxGlSesDevEntStat": nscDxGlSesDevEntStat,
       "nscDxGlSesDevEntSenseData": nscDxGlSesDevEntSenseData,
       "nscDxGlXportStatsTable": nscDxGlXportStatsTable,
       "nscDxGlXportStatsEntry": nscDxGlXportStatsEntry,
       "nscDxGlXportStatsEntKeyId": nscDxGlXportStatsEntKeyId,
       "nscDxGlXportStatsEntInAcks": nscDxGlXportStatsEntInAcks,
       "nscDxGlXportStatsEntInConnects": nscDxGlXportStatsEntInConnects,
       "nscDxGlXportStatsEntInDataDups": nscDxGlXportStatsEntInDataDups,
       "nscDxGlXportStatsEntInDataInOrders": nscDxGlXportStatsEntInDataInOrders,
       "nscDxGlXportStatsEntInDataInvalids": nscDxGlXportStatsEntInDataInvalids,
       "nscDxGlXportStatsEntInDataInWindows": nscDxGlXportStatsEntInDataInWindows,
       "nscDxGlXportStatsEntInDiscs": nscDxGlXportStatsEntInDiscs,
       "nscDxGlXportStatsEntInNacks": nscDxGlXportStatsEntInNacks,
       "nscDxGlXportStatsEntInProbes": nscDxGlXportStatsEntInProbes,
       "nscDxGlXportStatsEntInProbeResps": nscDxGlXportStatsEntInProbeResps,
       "nscDxGlXportStatsEntBadPckts": nscDxGlXportStatsEntBadPckts,
       "nscDxGlXportStatsEntBadXcbs": nscDxGlXportStatsEntBadXcbs,
       "nscDxGlXportStatsEntOutAcks": nscDxGlXportStatsEntOutAcks,
       "nscDxGlXportStatsEntOutConnects": nscDxGlXportStatsEntOutConnects,
       "nscDxGlXportStatsEntOutDatas": nscDxGlXportStatsEntOutDatas,
       "nscDxGlXportStatsEntOutDiscs": nscDxGlXportStatsEntOutDiscs,
       "nscDxGlXportStatsEntOutNacks": nscDxGlXportStatsEntOutNacks,
       "nscDxGlXportStatsEntOutProbes": nscDxGlXportStatsEntOutProbes,
       "nscDxGlXportStatsEntOutProbeResps": nscDxGlXportStatsEntOutProbeResps,
       "nscDxGlXportStatsEntReconns": nscDxGlXportStatsEntReconns,
       "nscDxGlXportStatsEntRetransmits": nscDxGlXportStatsEntRetransmits,
       "nscDxGlXportStatsEntBadChecksums": nscDxGlXportStatsEntBadChecksums,
       "nscDxGlXportStatsEntBadVersions": nscDxGlXportStatsEntBadVersions,
       "nscDxGlXportStatsEntConnTimeouts": nscDxGlXportStatsEntConnTimeouts,
       "nscDxGlXportStatsEntInitXcbExists": nscDxGlXportStatsEntInitXcbExists,
       "nscDxGlXportStatsEntNoHdrSpaces": nscDxGlXportStatsEntNoHdrSpaces,
       "nscDxGlXportStatsEntNoMemorys": nscDxGlXportStatsEntNoMemorys,
       "nscDxGlXportStatsEntNoPes": nscDxGlXportStatsEntNoPes,
       "nscDxGlXportStatsEntOutOfSeqDatas": nscDxGlXportStatsEntOutOfSeqDatas,
       "nscDxGlXportStatsEntShortPackets": nscDxGlXportStatsEntShortPackets,
       "nscDxGlXportConnTable": nscDxGlXportConnTable,
       "nscDxGlXportConnEntry": nscDxGlXportConnEntry,
       "nscDxGlXportConnEntKeyId": nscDxGlXportConnEntKeyId,
       "nscDxGlXportConnEntNum": nscDxGlXportConnEntNum,
       "nscDxGlXportConnEntLocalAddress": nscDxGlXportConnEntLocalAddress,
       "nscDxGlXportConnEntLocalPort": nscDxGlXportConnEntLocalPort,
       "nscDxGlXportConnEntRemoteAddress": nscDxGlXportConnEntRemoteAddress,
       "nscDxGlXportConnEntRemotePort": nscDxGlXportConnEntRemotePort,
       "nscDxGlXportConnEntXopt": nscDxGlXportConnEntXopt,
       "nscDxGlXportConnEntWindowSize": nscDxGlXportConnEntWindowSize,
       "nscDxGlXportConnEntRoundTripTime": nscDxGlXportConnEntRoundTripTime,
       "nscDxGlXportConnEntSeqNumber": nscDxGlXportConnEntSeqNumber,
       "nscDxGlXportConnEntXcbFlags": nscDxGlXportConnEntXcbFlags}
)
