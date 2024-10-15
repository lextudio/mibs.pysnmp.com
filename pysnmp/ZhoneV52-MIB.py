# SNMP MIB module (ZhoneV52-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneV52-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:22 2024
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

(PerfCurrentCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneVoice,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneVoice")

(ZhoneAdminString,
 ZhoneRowStatus,
 ZhoneShelfValue,
 ZhoneShelfValueOrZero,
 ZhoneSlotValue,
 ZhoneSlotValueOrZero) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus",
    "ZhoneShelfValue",
    "ZhoneShelfValueOrZero",
    "ZhoneSlotValue",
    "ZhoneSlotValueOrZero")


# MODULE-IDENTITY

zhoneV52 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2)
)
zhoneV52.setRevisions(
        ("2008-02-05 01:38",
         "2003-12-09 16:36",
         "2003-01-31 14:09",
         "2002-09-10 15:15",
         "2002-04-05 09:30",
         "2001-12-13 14:30",
         "2001-10-24 17:00",
         "2001-09-04 14:30",
         "2001-08-01 11:15",
         "2001-07-23 15:50",
         "2001-03-09 14:30",
         "2001-01-17 13:17",
         "2001-01-09 11:12",
         "2000-12-19 14:33",
         "2000-11-22 13:22",
         "2000-10-04 10:53",
         "2000-08-23 10:58")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_V52InterfaceGroupTable_Object = MibTable
v52InterfaceGroupTable = _V52InterfaceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    v52InterfaceGroupTable.setStatus("current")
_V52InterfaceGroupEntry_Object = MibTableRow
v52InterfaceGroupEntry = _V52InterfaceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1)
)
v52InterfaceGroupEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
)
if mibBuilder.loadTexts:
    v52InterfaceGroupEntry.setStatus("current")
_V52IgNameId_Type = ZhoneAdminString
_V52IgNameId_Object = MibTableColumn
v52IgNameId = _V52IgNameId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 1),
    _V52IgNameId_Type()
)
v52IgNameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52IgNameId.setStatus("current")
_V52IgShelf_Type = ZhoneShelfValue
_V52IgShelf_Object = MibTableColumn
v52IgShelf = _V52IgShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 2),
    _V52IgShelf_Type()
)
v52IgShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgShelf.setStatus("current")
_V52IgSlot_Type = ZhoneSlotValue
_V52IgSlot_Object = MibTableColumn
v52IgSlot = _V52IgSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 3),
    _V52IgSlot_Type()
)
v52IgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgSlot.setStatus("current")
_V52IgPeerShelf_Type = ZhoneShelfValueOrZero
_V52IgPeerShelf_Object = MibTableColumn
v52IgPeerShelf = _V52IgPeerShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 4),
    _V52IgPeerShelf_Type()
)
v52IgPeerShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgPeerShelf.setStatus("current")
_V52IgPeerSlot_Type = ZhoneSlotValueOrZero
_V52IgPeerSlot_Object = MibTableColumn
v52IgPeerSlot = _V52IgPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 5),
    _V52IgPeerSlot_Type()
)
v52IgPeerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgPeerSlot.setStatus("current")


class _V52IgPeerStatus_Type(Integer32):
    """Custom type v52IgPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuredAndAvailable", 2),
          ("configuredAndUnavailable", 3),
          ("noStandbyConfigured", 1))
    )


_V52IgPeerStatus_Type.__name__ = "Integer32"
_V52IgPeerStatus_Object = MibTableColumn
v52IgPeerStatus = _V52IgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 6),
    _V52IgPeerStatus_Type()
)
v52IgPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgPeerStatus.setStatus("current")


class _V52IgLocalInterfaceId_Type(Integer32):
    """Custom type v52IgLocalInterfaceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_V52IgLocalInterfaceId_Type.__name__ = "Integer32"
_V52IgLocalInterfaceId_Object = MibTableColumn
v52IgLocalInterfaceId = _V52IgLocalInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 7),
    _V52IgLocalInterfaceId_Type()
)
v52IgLocalInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLocalInterfaceId.setStatus("current")


class _V52IgRemoteInterfaceId_Type(Integer32):
    """Custom type v52IgRemoteInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_V52IgRemoteInterfaceId_Type.__name__ = "Integer32"
_V52IgRemoteInterfaceId_Object = MibTableColumn
v52IgRemoteInterfaceId = _V52IgRemoteInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 8),
    _V52IgRemoteInterfaceId_Type()
)
v52IgRemoteInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgRemoteInterfaceId.setStatus("current")


class _V52IgLocalProvVariant_Type(Integer32):
    """Custom type v52IgLocalProvVariant based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_V52IgLocalProvVariant_Type.__name__ = "Integer32"
_V52IgLocalProvVariant_Object = MibTableColumn
v52IgLocalProvVariant = _V52IgLocalProvVariant_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 9),
    _V52IgLocalProvVariant_Type()
)
v52IgLocalProvVariant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLocalProvVariant.setStatus("current")


class _V52IgRemoteProvVariant_Type(Integer32):
    """Custom type v52IgRemoteProvVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_V52IgRemoteProvVariant_Type.__name__ = "Integer32"
_V52IgRemoteProvVariant_Object = MibTableColumn
v52IgRemoteProvVariant = _V52IgRemoteProvVariant_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 10),
    _V52IgRemoteProvVariant_Type()
)
v52IgRemoteProvVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgRemoteProvVariant.setStatus("current")


class _V52IgProvVariantRequest_Type(Integer32):
    """Custom type v52IgProvVariantRequest based on Integer32"""
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
        *(("noRequest", 1),
          ("requestFromLe", 3),
          ("switchLeToLocal", 4),
          ("verifyWithLe", 2))
    )


_V52IgProvVariantRequest_Type.__name__ = "Integer32"
_V52IgProvVariantRequest_Object = MibTableColumn
v52IgProvVariantRequest = _V52IgProvVariantRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 11),
    _V52IgProvVariantRequest_Type()
)
v52IgProvVariantRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgProvVariantRequest.setStatus("current")


class _V52IgProvVariantRequestStatus_Type(Integer32):
    """Custom type v52IgProvVariantRequestStatus based on Integer32"""
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
        *(("requestFromLeFailed", 4),
          ("requestFromLeSucceeded", 3),
          ("switchToLocalFailed", 6),
          ("switchToLocalSucceeded", 5),
          ("verifyWithLeFailed", 2),
          ("verifyWithLeSucceeded", 1))
    )


_V52IgProvVariantRequestStatus_Type.__name__ = "Integer32"
_V52IgProvVariantRequestStatus_Object = MibTableColumn
v52IgProvVariantRequestStatus = _V52IgProvVariantRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 12),
    _V52IgProvVariantRequestStatus_Type()
)
v52IgProvVariantRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgProvVariantRequestStatus.setStatus("current")


class _V52IgAdminStatus_Type(Integer32):
    """Custom type v52IgAdminStatus based on Integer32"""
    defaultValue = 2

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
        *(("deferredOutOfService", 3),
          ("inService", 1),
          ("outOfService", 2),
          ("restart", 4))
    )


_V52IgAdminStatus_Type.__name__ = "Integer32"
_V52IgAdminStatus_Object = MibTableColumn
v52IgAdminStatus = _V52IgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 13),
    _V52IgAdminStatus_Type()
)
v52IgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgAdminStatus.setStatus("current")


class _V52IgOperationalStatus_Type(Integer32):
    """Custom type v52IgOperationalStatus based on Integer32"""
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
        *(("degradedService", 4),
          ("inoperable", 2),
          ("inoperableIsInProgress", 5),
          ("inoperableOosInProgress", 6),
          ("operable", 1),
          ("standby", 3))
    )


_V52IgOperationalStatus_Type.__name__ = "Integer32"
_V52IgOperationalStatus_Object = MibTableColumn
v52IgOperationalStatus = _V52IgOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 14),
    _V52IgOperationalStatus_Type()
)
v52IgOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgOperationalStatus.setStatus("current")


class _V52IgOperStatusCause_Type(Integer32):
    """Custom type v52IgOperStatusCause based on Integer32"""
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
        *(("localDisable", 2),
          ("other", 1),
          ("protocolFailure", 4),
          ("remoteOutOfService", 3))
    )


_V52IgOperStatusCause_Type.__name__ = "Integer32"
_V52IgOperStatusCause_Object = MibTableColumn
v52IgOperStatusCause = _V52IgOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 15),
    _V52IgOperStatusCause_Type()
)
v52IgOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgOperStatusCause.setStatus("current")


class _V52IgMaxConfiguredCalls_Type(Gauge32):
    """Custom type v52IgMaxConfiguredCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 480),
    )


_V52IgMaxConfiguredCalls_Type.__name__ = "Gauge32"
_V52IgMaxConfiguredCalls_Object = MibTableColumn
v52IgMaxConfiguredCalls = _V52IgMaxConfiguredCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 16),
    _V52IgMaxConfiguredCalls_Type()
)
v52IgMaxConfiguredCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgMaxConfiguredCalls.setStatus("current")


class _V52IgCurrActiveCalls_Type(Gauge32):
    """Custom type v52IgCurrActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_V52IgCurrActiveCalls_Type.__name__ = "Gauge32"
_V52IgCurrActiveCalls_Object = MibTableColumn
v52IgCurrActiveCalls = _V52IgCurrActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 17),
    _V52IgCurrActiveCalls_Type()
)
v52IgCurrActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgCurrActiveCalls.setStatus("current")


class _V52IgPstnLayer3StartAddress_Type(Integer32):
    """Custom type v52IgPstnLayer3StartAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_V52IgPstnLayer3StartAddress_Type.__name__ = "Integer32"
_V52IgPstnLayer3StartAddress_Object = MibTableColumn
v52IgPstnLayer3StartAddress = _V52IgPstnLayer3StartAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 18),
    _V52IgPstnLayer3StartAddress_Type()
)
v52IgPstnLayer3StartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgPstnLayer3StartAddress.setStatus("current")


class _V52IgIsdnEnvFuncStartAddress_Type(Integer32):
    """Custom type v52IgIsdnEnvFuncStartAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8175),
    )


_V52IgIsdnEnvFuncStartAddress_Type.__name__ = "Integer32"
_V52IgIsdnEnvFuncStartAddress_Object = MibTableColumn
v52IgIsdnEnvFuncStartAddress = _V52IgIsdnEnvFuncStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 19),
    _V52IgIsdnEnvFuncStartAddress_Type()
)
v52IgIsdnEnvFuncStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgIsdnEnvFuncStartAddress.setStatus("current")


class _V52IgStatsTimeElapsed_Type(Integer32):
    """Custom type v52IgStatsTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_V52IgStatsTimeElapsed_Type.__name__ = "Integer32"
_V52IgStatsTimeElapsed_Object = MibTableColumn
v52IgStatsTimeElapsed = _V52IgStatsTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 20),
    _V52IgStatsTimeElapsed_Type()
)
v52IgStatsTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgStatsTimeElapsed.setStatus("current")


class _V52IgStatsValidIntervals_Type(Integer32):
    """Custom type v52IgStatsValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_V52IgStatsValidIntervals_Type.__name__ = "Integer32"
_V52IgStatsValidIntervals_Object = MibTableColumn
v52IgStatsValidIntervals = _V52IgStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 21),
    _V52IgStatsValidIntervals_Type()
)
v52IgStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgStatsValidIntervals.setStatus("current")


class _V52IgStatsInvalidIntervals_Type(Integer32):
    """Custom type v52IgStatsInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_V52IgStatsInvalidIntervals_Type.__name__ = "Integer32"
_V52IgStatsInvalidIntervals_Object = MibTableColumn
v52IgStatsInvalidIntervals = _V52IgStatsInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 22),
    _V52IgStatsInvalidIntervals_Type()
)
v52IgStatsInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgStatsInvalidIntervals.setStatus("current")


class _V52IgPortAlignmentRequest_Type(Integer32):
    """Custom type v52IgPortAlignmentRequest based on Integer32"""
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
        *(("blockAll", 2),
          ("blockIsdn", 3),
          ("blockPstn", 4),
          ("noRequest", 1),
          ("unblockAll", 5),
          ("unblockIsdn", 6),
          ("unblockPstn", 7))
    )


_V52IgPortAlignmentRequest_Type.__name__ = "Integer32"
_V52IgPortAlignmentRequest_Object = MibTableColumn
v52IgPortAlignmentRequest = _V52IgPortAlignmentRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 23),
    _V52IgPortAlignmentRequest_Type()
)
v52IgPortAlignmentRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgPortAlignmentRequest.setStatus("current")


class _V52IgPortAlignmentStatus_Type(Integer32):
    """Custom type v52IgPortAlignmentStatus based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("blockAllFailed", 2),
          ("blockAllSucceeded", 1),
          ("blockIsdnFailed", 4),
          ("blockIsdnSucceded", 3),
          ("blockPstnFailed", 6),
          ("blockPstnSucceded", 5),
          ("unblockAllFailed", 8),
          ("unblockAllSucceeded", 7),
          ("unblockIsdnFailed", 10),
          ("unblockIsdnSucceeded", 9),
          ("unblockPstnFailed", 12),
          ("unblockPstnSucceeded", 11))
    )


_V52IgPortAlignmentStatus_Type.__name__ = "Integer32"
_V52IgPortAlignmentStatus_Object = MibTableColumn
v52IgPortAlignmentStatus = _V52IgPortAlignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 24),
    _V52IgPortAlignmentStatus_Type()
)
v52IgPortAlignmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IgPortAlignmentStatus.setStatus("current")


class _V52IgNationalPstnRegion_Type(Integer32):
    """Custom type v52IgNationalPstnRegion based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 20),
          ("australia", 28),
          ("austria", 6),
          ("belgium", 7),
          ("brazil", 23),
          ("china", 8),
          ("estonia", 29),
          ("etsi", 1),
          ("finland", 5),
          ("france", 9),
          ("germany", 2),
          ("hong-kong", 10),
          ("ireland", 27),
          ("italy", 4),
          ("japan", 11),
          ("korea", 12),
          ("malaysia", 24),
          ("mexico", 19),
          ("netherlands", 13),
          ("new-zealand", 14),
          ("peru", 21),
          ("puerto-rico", 22),
          ("saudi-arabia", 31),
          ("singapore", 15),
          ("south-africa", 30),
          ("spain", 16),
          ("sweden", 17),
          ("switzerland", 18),
          ("taiwan", 25),
          ("uk", 3),
          ("united-arab-emirates", 26))
    )


_V52IgNationalPstnRegion_Type.__name__ = "Integer32"
_V52IgNationalPstnRegion_Object = MibTableColumn
v52IgNationalPstnRegion = _V52IgNationalPstnRegion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 25),
    _V52IgNationalPstnRegion_Type()
)
v52IgNationalPstnRegion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgNationalPstnRegion.setStatus("current")


class _V52IgSwitchVendor_Type(Integer32):
    """Custom type v52IgSwitchVendor based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alcatel", 4),
          ("ericsson", 5),
          ("lucent", 2),
          ("nokia", 6),
          ("nortel", 3),
          ("samsung", 8),
          ("siemens", 7))
    )


_V52IgSwitchVendor_Type.__name__ = "Integer32"
_V52IgSwitchVendor_Object = MibTableColumn
v52IgSwitchVendor = _V52IgSwitchVendor_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 26),
    _V52IgSwitchVendor_Type()
)
v52IgSwitchVendor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgSwitchVendor.setStatus("current")


class _V52IgProtocolSpecification_Type(Integer32):
    """Custom type v52IgProtocolSpecification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edition1", 1),
          ("edition2", 2))
    )


_V52IgProtocolSpecification_Type.__name__ = "Integer32"
_V52IgProtocolSpecification_Object = MibTableColumn
v52IgProtocolSpecification = _V52IgProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 27),
    _V52IgProtocolSpecification_Type()
)
v52IgProtocolSpecification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgProtocolSpecification.setStatus("current")
_V52IgRowStatus_Type = ZhoneRowStatus
_V52IgRowStatus_Object = MibTableColumn
v52IgRowStatus = _V52IgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 1, 1, 28),
    _V52IgRowStatus_Type()
)
v52IgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgRowStatus.setStatus("current")
_V52InterfaceGroupLapvTable_Object = MibTable
v52InterfaceGroupLapvTable = _V52InterfaceGroupLapvTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    v52InterfaceGroupLapvTable.setStatus("current")
_V52InterfaceGroupLapvEntry_Object = MibTableRow
v52InterfaceGroupLapvEntry = _V52InterfaceGroupLapvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    v52InterfaceGroupLapvEntry.setStatus("current")


class _V52IgLapvMaxOutstandingFrames_Type(Integer32):
    """Custom type v52IgLapvMaxOutstandingFrames based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_V52IgLapvMaxOutstandingFrames_Type.__name__ = "Integer32"
_V52IgLapvMaxOutstandingFrames_Object = MibTableColumn
v52IgLapvMaxOutstandingFrames = _V52IgLapvMaxOutstandingFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1, 1),
    _V52IgLapvMaxOutstandingFrames_Type()
)
v52IgLapvMaxOutstandingFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLapvMaxOutstandingFrames.setStatus("current")
if mibBuilder.loadTexts:
    v52IgLapvMaxOutstandingFrames.setUnits("frames")


class _V52IgLapvN200_Type(Integer32):
    """Custom type v52IgLapvN200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_V52IgLapvN200_Type.__name__ = "Integer32"
_V52IgLapvN200_Object = MibTableColumn
v52IgLapvN200 = _V52IgLapvN200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1, 2),
    _V52IgLapvN200_Type()
)
v52IgLapvN200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLapvN200.setStatus("current")


class _V52IgLapvN201_Type(Integer32):
    """Custom type v52IgLapvN201 based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 260),
    )


_V52IgLapvN201_Type.__name__ = "Integer32"
_V52IgLapvN201_Object = MibTableColumn
v52IgLapvN201 = _V52IgLapvN201_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1, 3),
    _V52IgLapvN201_Type()
)
v52IgLapvN201.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLapvN201.setStatus("current")


class _V52IgLapvT200_Type(Integer32):
    """Custom type v52IgLapvT200 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(350, 350),
        ValueRangeConstraint(400, 400),
        ValueRangeConstraint(450, 450),
        ValueRangeConstraint(500, 500),
        ValueRangeConstraint(550, 550),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(650, 650),
        ValueRangeConstraint(700, 700),
        ValueRangeConstraint(750, 750),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(850, 850),
        ValueRangeConstraint(900, 900),
        ValueRangeConstraint(950, 950),
        ValueRangeConstraint(1000, 1000),
    )


_V52IgLapvT200_Type.__name__ = "Integer32"
_V52IgLapvT200_Object = MibTableColumn
v52IgLapvT200 = _V52IgLapvT200_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1, 4),
    _V52IgLapvT200_Type()
)
v52IgLapvT200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLapvT200.setStatus("current")
if mibBuilder.loadTexts:
    v52IgLapvT200.setUnits("milliseconds")


class _V52IgLapvT203_Type(Integer32):
    """Custom type v52IgLapvT203 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(170, 170),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(190, 190),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(230, 230),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(260, 260),
        ValueRangeConstraint(270, 270),
        ValueRangeConstraint(280, 280),
        ValueRangeConstraint(290, 290),
        ValueRangeConstraint(300, 300),
    )


_V52IgLapvT203_Type.__name__ = "Integer32"
_V52IgLapvT203_Object = MibTableColumn
v52IgLapvT203 = _V52IgLapvT203_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 2, 1, 5),
    _V52IgLapvT203_Type()
)
v52IgLapvT203.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLapvT203.setStatus("current")
if mibBuilder.loadTexts:
    v52IgLapvT203.setUnits("seconds")
_V52LinkTable_Object = MibTable
v52LinkTable = _V52LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    v52LinkTable.setStatus("current")
_V52LinkEntry_Object = MibTableRow
v52LinkEntry = _V52LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1)
)
v52LinkEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52LinkDsnLgId"),
    (0, "ZhoneV52-MIB", "v52LinkDs1ChannelNumber"),
)
if mibBuilder.loadTexts:
    v52LinkEntry.setStatus("current")


class _V52LinkDsnLgId_Type(Integer32):
    """Custom type v52LinkDsnLgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_V52LinkDsnLgId_Type.__name__ = "Integer32"
_V52LinkDsnLgId_Object = MibTableColumn
v52LinkDsnLgId = _V52LinkDsnLgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 1),
    _V52LinkDsnLgId_Type()
)
v52LinkDsnLgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52LinkDsnLgId.setStatus("current")


class _V52LinkDs1ChannelNumber_Type(Integer32):
    """Custom type v52LinkDs1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_V52LinkDs1ChannelNumber_Type.__name__ = "Integer32"
_V52LinkDs1ChannelNumber_Object = MibTableColumn
v52LinkDs1ChannelNumber = _V52LinkDs1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 2),
    _V52LinkDs1ChannelNumber_Type()
)
v52LinkDs1ChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52LinkDs1ChannelNumber.setStatus("current")


class _V52LinkId_Type(Integer32):
    """Custom type v52LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_V52LinkId_Type.__name__ = "Integer32"
_V52LinkId_Object = MibTableColumn
v52LinkId = _V52LinkId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 3),
    _V52LinkId_Type()
)
v52LinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52LinkId.setStatus("current")


class _V52LinkCheckId_Type(Integer32):
    """Custom type v52LinkCheckId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("notActivated", 2))
    )


_V52LinkCheckId_Type.__name__ = "Integer32"
_V52LinkCheckId_Object = MibTableColumn
v52LinkCheckId = _V52LinkCheckId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 4),
    _V52LinkCheckId_Type()
)
v52LinkCheckId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52LinkCheckId.setStatus("current")


class _V52LinkCheckIdStatus_Type(Integer32):
    """Custom type v52LinkCheckIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("rejected", 3),
          ("succeeded", 1))
    )


_V52LinkCheckIdStatus_Type.__name__ = "Integer32"
_V52LinkCheckIdStatus_Object = MibTableColumn
v52LinkCheckIdStatus = _V52LinkCheckIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 5),
    _V52LinkCheckIdStatus_Type()
)
v52LinkCheckIdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52LinkCheckIdStatus.setStatus("current")


class _V52LinkAdminStatus_Type(Integer32):
    """Custom type v52LinkAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_V52LinkAdminStatus_Type.__name__ = "Integer32"
_V52LinkAdminStatus_Object = MibTableColumn
v52LinkAdminStatus = _V52LinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 6),
    _V52LinkAdminStatus_Type()
)
v52LinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52LinkAdminStatus.setStatus("obsolete")


class _V52LinkBlock_Type(Integer32):
    """Custom type v52LinkBlock based on Integer32"""
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
        *(("deferredBlocked", 1),
          ("forceBlocked", 3),
          ("nonDeferredBlocked", 2),
          ("unblocked", 4))
    )


_V52LinkBlock_Type.__name__ = "Integer32"
_V52LinkBlock_Object = MibTableColumn
v52LinkBlock = _V52LinkBlock_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 7),
    _V52LinkBlock_Type()
)
v52LinkBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52LinkBlock.setStatus("current")


class _V52LinkBlockStatus_Type(Integer32):
    """Custom type v52LinkBlockStatus based on Integer32"""
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
        *(("both", 4),
          ("local", 2),
          ("remote", 3),
          ("unblocked", 1))
    )


_V52LinkBlockStatus_Type.__name__ = "Integer32"
_V52LinkBlockStatus_Object = MibTableColumn
v52LinkBlockStatus = _V52LinkBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 8),
    _V52LinkBlockStatus_Type()
)
v52LinkBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52LinkBlockStatus.setStatus("current")
_V52LinkRowStatus_Type = ZhoneRowStatus
_V52LinkRowStatus_Object = MibTableColumn
v52LinkRowStatus = _V52LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 3, 1, 9),
    _V52LinkRowStatus_Type()
)
v52LinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52LinkRowStatus.setStatus("current")
_V52CChannelTable_Object = MibTable
v52CChannelTable = _V52CChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4)
)
if mibBuilder.loadTexts:
    v52CChannelTable.setStatus("current")
_V52CChannelEntry_Object = MibTableRow
v52CChannelEntry = _V52CChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1)
)
v52CChannelEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52LinkDsnLgId"),
    (0, "ZhoneV52-MIB", "v52LinkDs1ChannelNumber"),
    (0, "ZhoneV52-MIB", "v52CChannelTimeSlotIndex"),
)
if mibBuilder.loadTexts:
    v52CChannelEntry.setStatus("current")


class _V52CChannelTimeSlotIndex_Type(Integer32):
    """Custom type v52CChannelTimeSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(31, 31),
    )


_V52CChannelTimeSlotIndex_Type.__name__ = "Integer32"
_V52CChannelTimeSlotIndex_Object = MibTableColumn
v52CChannelTimeSlotIndex = _V52CChannelTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 1),
    _V52CChannelTimeSlotIndex_Type()
)
v52CChannelTimeSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52CChannelTimeSlotIndex.setStatus("current")


class _V52CChannelLogicalChannelId_Type(Integer32):
    """Custom type v52CChannelLogicalChannelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_V52CChannelLogicalChannelId_Type.__name__ = "Integer32"
_V52CChannelLogicalChannelId_Object = MibTableColumn
v52CChannelLogicalChannelId = _V52CChannelLogicalChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 2),
    _V52CChannelLogicalChannelId_Type()
)
v52CChannelLogicalChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CChannelLogicalChannelId.setStatus("current")


class _V52CChannelProtGp_Type(Integer32):
    """Custom type v52CChannelProtGp based on Integer32"""
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
        *(("group1", 2),
          ("mToNGroup2", 4),
          ("none", 1),
          ("oneToOneGroup2", 3))
    )


_V52CChannelProtGp_Type.__name__ = "Integer32"
_V52CChannelProtGp_Object = MibTableColumn
v52CChannelProtGp = _V52CChannelProtGp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 3),
    _V52CChannelProtGp_Type()
)
v52CChannelProtGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CChannelProtGp.setStatus("current")


class _V52CChannelRole_Type(Integer32):
    """Custom type v52CChannelRole based on Integer32"""
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
        *(("active", 1),
          ("standby", 2),
          ("switchToStandby", 3))
    )


_V52CChannelRole_Type.__name__ = "Integer32"
_V52CChannelRole_Object = MibTableColumn
v52CChannelRole = _V52CChannelRole_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 4),
    _V52CChannelRole_Type()
)
v52CChannelRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CChannelRole.setStatus("current")


class _V52CChannelStatus_Type(Integer32):
    """Custom type v52CChannelStatus based on Integer32"""
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
          ("failed", 3),
          ("standby", 2))
    )


_V52CChannelStatus_Type.__name__ = "Integer32"
_V52CChannelStatus_Object = MibTableColumn
v52CChannelStatus = _V52CChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 5),
    _V52CChannelStatus_Type()
)
v52CChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52CChannelStatus.setStatus("current")


class _V52CChannelCurrentLogicalChannelId_Type(Integer32):
    """Custom type v52CChannelCurrentLogicalChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_V52CChannelCurrentLogicalChannelId_Type.__name__ = "Integer32"
_V52CChannelCurrentLogicalChannelId_Object = MibTableColumn
v52CChannelCurrentLogicalChannelId = _V52CChannelCurrentLogicalChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 6),
    _V52CChannelCurrentLogicalChannelId_Type()
)
v52CChannelCurrentLogicalChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52CChannelCurrentLogicalChannelId.setStatus("current")
_V52CChannelRowStatus_Type = ZhoneRowStatus
_V52CChannelRowStatus_Object = MibTableColumn
v52CChannelRowStatus = _V52CChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 7),
    _V52CChannelRowStatus_Type()
)
v52CChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CChannelRowStatus.setStatus("current")


class _V52CChannelStatusCause_Type(Integer32):
    """Custom type v52CChannelStatusCause based on Integer32"""
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
        *(("other", 1),
          ("switchOverAborted", 5),
          ("switchOverError", 3),
          ("switchOverRejected", 2),
          ("switchOverRejectedProvisioningError", 6),
          ("switchOverResetSequence", 7),
          ("switchOverResetSequenceNumberError", 4))
    )


_V52CChannelStatusCause_Type.__name__ = "Integer32"
_V52CChannelStatusCause_Object = MibTableColumn
v52CChannelStatusCause = _V52CChannelStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 4, 1, 8),
    _V52CChannelStatusCause_Type()
)
v52CChannelStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52CChannelStatusCause.setStatus("current")
_V52CPathTable_Object = MibTable
v52CPathTable = _V52CPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5)
)
if mibBuilder.loadTexts:
    v52CPathTable.setStatus("current")
_V52CPathEntry_Object = MibTableRow
v52CPathEntry = _V52CPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1)
)
v52CPathEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52CPathId"),
)
if mibBuilder.loadTexts:
    v52CPathEntry.setStatus("current")


class _V52CPathId_Type(Integer32):
    """Custom type v52CPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_V52CPathId_Type.__name__ = "Integer32"
_V52CPathId_Object = MibTableColumn
v52CPathId = _V52CPathId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 1),
    _V52CPathId_Type()
)
v52CPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52CPathId.setStatus("current")


class _V52CPathType_Type(Integer32):
    """Custom type v52CPathType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bcc", 4),
          ("ctrl", 3),
          ("isdnDs", 6),
          ("isdnF", 7),
          ("isdnP", 8),
          ("lctl", 5),
          ("pstn", 2),
          ("unknown", 1))
    )


_V52CPathType_Type.__name__ = "Integer32"
_V52CPathType_Object = MibTableColumn
v52CPathType = _V52CPathType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 2),
    _V52CPathType_Type()
)
v52CPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CPathType.setStatus("current")


class _V52CPathLogicalChannelId_Type(Integer32):
    """Custom type v52CPathLogicalChannelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_V52CPathLogicalChannelId_Type.__name__ = "Integer32"
_V52CPathLogicalChannelId_Object = MibTableColumn
v52CPathLogicalChannelId = _V52CPathLogicalChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 3),
    _V52CPathLogicalChannelId_Type()
)
v52CPathLogicalChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CPathLogicalChannelId.setStatus("current")
_V52CPathRowStatus_Type = ZhoneRowStatus
_V52CPathRowStatus_Object = MibTableColumn
v52CPathRowStatus = _V52CPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 4),
    _V52CPathRowStatus_Type()
)
v52CPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52CPathRowStatus.setStatus("current")


class _V52CPathOperStatus_Type(Integer32):
    """Custom type v52CPathOperStatus based on Integer32"""
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


_V52CPathOperStatus_Type.__name__ = "Integer32"
_V52CPathOperStatus_Object = MibTableColumn
v52CPathOperStatus = _V52CPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 5),
    _V52CPathOperStatus_Type()
)
v52CPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52CPathOperStatus.setStatus("current")


class _V52CPathOperStatusCause_Type(Integer32):
    """Custom type v52CPathOperStatusCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establishConfirmationReceived", 1),
          ("establishIndicationReceived", 2),
          ("releaseIndicationReceived", 3))
    )


_V52CPathOperStatusCause_Type.__name__ = "Integer32"
_V52CPathOperStatusCause_Object = MibTableColumn
v52CPathOperStatusCause = _V52CPathOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 5, 1, 6),
    _V52CPathOperStatusCause_Type()
)
v52CPathOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52CPathOperStatusCause.setStatus("current")
_V52UserPortTable_Object = MibTable
v52UserPortTable = _V52UserPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6)
)
if mibBuilder.loadTexts:
    v52UserPortTable.setStatus("current")
_V52UserPortEntry_Object = MibTableRow
v52UserPortEntry = _V52UserPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1)
)
v52UserPortEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52UserPortAddress"),
    (0, "ZhoneV52-MIB", "v52UserPortType"),
)
if mibBuilder.loadTexts:
    v52UserPortEntry.setStatus("current")


class _V52UserPortAddress_Type(Integer32):
    """Custom type v52UserPortAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_V52UserPortAddress_Type.__name__ = "Integer32"
_V52UserPortAddress_Object = MibTableColumn
v52UserPortAddress = _V52UserPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 1),
    _V52UserPortAddress_Type()
)
v52UserPortAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52UserPortAddress.setStatus("current")


class _V52UserPortType_Type(Integer32):
    """Custom type v52UserPortType based on Integer32"""
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
        *(("isdnBa", 3),
          ("isdnPra", 4),
          ("pstn", 2),
          ("unknown", 1))
    )


_V52UserPortType_Type.__name__ = "Integer32"
_V52UserPortType_Object = MibTableColumn
v52UserPortType = _V52UserPortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 2),
    _V52UserPortType_Type()
)
v52UserPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52UserPortType.setStatus("current")


class _V52UserPortAdminStatus_Type(Integer32):
    """Custom type v52UserPortAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_V52UserPortAdminStatus_Type.__name__ = "Integer32"
_V52UserPortAdminStatus_Object = MibTableColumn
v52UserPortAdminStatus = _V52UserPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 3),
    _V52UserPortAdminStatus_Type()
)
v52UserPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortAdminStatus.setStatus("current")


class _V52UserPortBlock_Type(Integer32):
    """Custom type v52UserPortBlock based on Integer32"""
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
        *(("blocked", 1),
          ("blockedNotSuitableForGroupUnblocking", 4),
          ("shuttingDown", 2),
          ("unblocked", 3))
    )


_V52UserPortBlock_Type.__name__ = "Integer32"
_V52UserPortBlock_Object = MibTableColumn
v52UserPortBlock = _V52UserPortBlock_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 4),
    _V52UserPortBlock_Type()
)
v52UserPortBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortBlock.setStatus("current")


class _V52UserPortBlockStatus_Type(Integer32):
    """Custom type v52UserPortBlockStatus based on Integer32"""
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
        *(("bothBlocked", 4),
          ("localBlocked", 2),
          ("remoteBlocked", 3),
          ("unblocked", 1))
    )


_V52UserPortBlockStatus_Type.__name__ = "Integer32"
_V52UserPortBlockStatus_Object = MibTableColumn
v52UserPortBlockStatus = _V52UserPortBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 5),
    _V52UserPortBlockStatus_Type()
)
v52UserPortBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52UserPortBlockStatus.setStatus("current")


class _V52UserPortRegOrLeaseUser_Type(Integer32):
    """Custom type v52UserPortRegOrLeaseUser based on Integer32"""
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
        *(("permanentLease", 2),
          ("regular", 1),
          ("semiPermanentLease", 3))
    )


_V52UserPortRegOrLeaseUser_Type.__name__ = "Integer32"
_V52UserPortRegOrLeaseUser_Object = MibTableColumn
v52UserPortRegOrLeaseUser = _V52UserPortRegOrLeaseUser_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 6),
    _V52UserPortRegOrLeaseUser_Type()
)
v52UserPortRegOrLeaseUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortRegOrLeaseUser.setStatus("current")


class _V52UserPortIsdnDsCPathId_Type(Integer32):
    """Custom type v52UserPortIsdnDsCPathId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_V52UserPortIsdnDsCPathId_Type.__name__ = "Integer32"
_V52UserPortIsdnDsCPathId_Object = MibTableColumn
v52UserPortIsdnDsCPathId = _V52UserPortIsdnDsCPathId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 7),
    _V52UserPortIsdnDsCPathId_Type()
)
v52UserPortIsdnDsCPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortIsdnDsCPathId.setStatus("current")


class _V52UserPortIsdnPCPathId_Type(Integer32):
    """Custom type v52UserPortIsdnPCPathId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_V52UserPortIsdnPCPathId_Type.__name__ = "Integer32"
_V52UserPortIsdnPCPathId_Object = MibTableColumn
v52UserPortIsdnPCPathId = _V52UserPortIsdnPCPathId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 8),
    _V52UserPortIsdnPCPathId_Type()
)
v52UserPortIsdnPCPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortIsdnPCPathId.setStatus("current")


class _V52UserPortIsdnFCPathId_Type(Integer32):
    """Custom type v52UserPortIsdnFCPathId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_V52UserPortIsdnFCPathId_Type.__name__ = "Integer32"
_V52UserPortIsdnFCPathId_Object = MibTableColumn
v52UserPortIsdnFCPathId = _V52UserPortIsdnFCPathId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 9),
    _V52UserPortIsdnFCPathId_Type()
)
v52UserPortIsdnFCPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortIsdnFCPathId.setStatus("current")
_V52UserPortRowStatus_Type = ZhoneRowStatus
_V52UserPortRowStatus_Object = MibTableColumn
v52UserPortRowStatus = _V52UserPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 10),
    _V52UserPortRowStatus_Type()
)
v52UserPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52UserPortRowStatus.setStatus("current")


class _V52UserPortOperStatus_Type(Integer32):
    """Custom type v52UserPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("manualOos", 2),
          ("oos", 3))
    )


_V52UserPortOperStatus_Type.__name__ = "Integer32"
_V52UserPortOperStatus_Object = MibTableColumn
v52UserPortOperStatus = _V52UserPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 6, 1, 11),
    _V52UserPortOperStatus_Type()
)
v52UserPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52UserPortOperStatus.setStatus("current")
_V52StatsCurrentTable_Object = MibTable
v52StatsCurrentTable = _V52StatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7)
)
if mibBuilder.loadTexts:
    v52StatsCurrentTable.setStatus("current")
_V52StatsCurrentEntry_Object = MibTableRow
v52StatsCurrentEntry = _V52StatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    v52StatsCurrentEntry.setStatus("current")
_V52IfCurrentPstnOutboundCalls_Type = PerfCurrentCount
_V52IfCurrentPstnOutboundCalls_Object = MibTableColumn
v52IfCurrentPstnOutboundCalls = _V52IfCurrentPstnOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 1),
    _V52IfCurrentPstnOutboundCalls_Type()
)
v52IfCurrentPstnOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentPstnOutboundCalls.setStatus("current")
_V52IfCurrentPstnInboundCalls_Type = PerfCurrentCount
_V52IfCurrentPstnInboundCalls_Object = MibTableColumn
v52IfCurrentPstnInboundCalls = _V52IfCurrentPstnInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 2),
    _V52IfCurrentPstnInboundCalls_Type()
)
v52IfCurrentPstnInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentPstnInboundCalls.setStatus("current")
_V52IfCurrentCallsBlocked_Type = PerfCurrentCount
_V52IfCurrentCallsBlocked_Object = MibTableColumn
v52IfCurrentCallsBlocked = _V52IfCurrentCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 3),
    _V52IfCurrentCallsBlocked_Type()
)
v52IfCurrentCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentCallsBlocked.setStatus("current")
_V52IfCurrentV52ProtocolErrors_Type = PerfCurrentCount
_V52IfCurrentV52ProtocolErrors_Object = MibTableColumn
v52IfCurrentV52ProtocolErrors = _V52IfCurrentV52ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 4),
    _V52IfCurrentV52ProtocolErrors_Type()
)
v52IfCurrentV52ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentV52ProtocolErrors.setStatus("current")
_V52IfCurrentLapdSent_Type = PerfCurrentCount
_V52IfCurrentLapdSent_Object = MibTableColumn
v52IfCurrentLapdSent = _V52IfCurrentLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 5),
    _V52IfCurrentLapdSent_Type()
)
v52IfCurrentLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentLapdSent.setStatus("current")
_V52IfCurrentLapdRcvd_Type = PerfCurrentCount
_V52IfCurrentLapdRcvd_Object = MibTableColumn
v52IfCurrentLapdRcvd = _V52IfCurrentLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 6),
    _V52IfCurrentLapdRcvd_Type()
)
v52IfCurrentLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentLapdRcvd.setStatus("current")
_V52IfCurrentLapdRcvdErrs_Type = PerfCurrentCount
_V52IfCurrentLapdRcvdErrs_Object = MibTableColumn
v52IfCurrentLapdRcvdErrs = _V52IfCurrentLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 7),
    _V52IfCurrentLapdRcvdErrs_Type()
)
v52IfCurrentLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentLapdRcvdErrs.setStatus("current")
_V52IfCurrentIsdnCalls_Type = PerfCurrentCount
_V52IfCurrentIsdnCalls_Object = MibTableColumn
v52IfCurrentIsdnCalls = _V52IfCurrentIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 7, 1, 8),
    _V52IfCurrentIsdnCalls_Type()
)
v52IfCurrentIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfCurrentIsdnCalls.setStatus("current")
_V52StatsIntervalTable_Object = MibTable
v52StatsIntervalTable = _V52StatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8)
)
if mibBuilder.loadTexts:
    v52StatsIntervalTable.setStatus("current")
_V52StatsIntervalEntry_Object = MibTableRow
v52StatsIntervalEntry = _V52StatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1)
)
v52StatsIntervalEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52IfIntervalNumber"),
)
if mibBuilder.loadTexts:
    v52StatsIntervalEntry.setStatus("current")


class _V52IfIntervalNumber_Type(Integer32):
    """Custom type v52IfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_V52IfIntervalNumber_Type.__name__ = "Integer32"
_V52IfIntervalNumber_Object = MibTableColumn
v52IfIntervalNumber = _V52IfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 1),
    _V52IfIntervalNumber_Type()
)
v52IfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52IfIntervalNumber.setStatus("current")
_V52IfIntervalPstnOutboundCalls_Type = PerfCurrentCount
_V52IfIntervalPstnOutboundCalls_Object = MibTableColumn
v52IfIntervalPstnOutboundCalls = _V52IfIntervalPstnOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 2),
    _V52IfIntervalPstnOutboundCalls_Type()
)
v52IfIntervalPstnOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalPstnOutboundCalls.setStatus("current")
_V52IfIntervalPstnInboundCalls_Type = PerfCurrentCount
_V52IfIntervalPstnInboundCalls_Object = MibTableColumn
v52IfIntervalPstnInboundCalls = _V52IfIntervalPstnInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 3),
    _V52IfIntervalPstnInboundCalls_Type()
)
v52IfIntervalPstnInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalPstnInboundCalls.setStatus("current")
_V52IfIntervalCallsBlocked_Type = PerfCurrentCount
_V52IfIntervalCallsBlocked_Object = MibTableColumn
v52IfIntervalCallsBlocked = _V52IfIntervalCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 4),
    _V52IfIntervalCallsBlocked_Type()
)
v52IfIntervalCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalCallsBlocked.setStatus("current")
_V52IfIntervalV52ProtocolErrors_Type = PerfCurrentCount
_V52IfIntervalV52ProtocolErrors_Object = MibTableColumn
v52IfIntervalV52ProtocolErrors = _V52IfIntervalV52ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 5),
    _V52IfIntervalV52ProtocolErrors_Type()
)
v52IfIntervalV52ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalV52ProtocolErrors.setStatus("current")
_V52IfIntervalLapdSent_Type = PerfCurrentCount
_V52IfIntervalLapdSent_Object = MibTableColumn
v52IfIntervalLapdSent = _V52IfIntervalLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 6),
    _V52IfIntervalLapdSent_Type()
)
v52IfIntervalLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalLapdSent.setStatus("current")
_V52IfIntervalLapdRcvd_Type = PerfCurrentCount
_V52IfIntervalLapdRcvd_Object = MibTableColumn
v52IfIntervalLapdRcvd = _V52IfIntervalLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 7),
    _V52IfIntervalLapdRcvd_Type()
)
v52IfIntervalLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalLapdRcvd.setStatus("current")
_V52IfIntervalLapdRcvdErrs_Type = PerfCurrentCount
_V52IfIntervalLapdRcvdErrs_Object = MibTableColumn
v52IfIntervalLapdRcvdErrs = _V52IfIntervalLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 8),
    _V52IfIntervalLapdRcvdErrs_Type()
)
v52IfIntervalLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalLapdRcvdErrs.setStatus("current")
_V52IfIntervalIsdnCalls_Type = PerfCurrentCount
_V52IfIntervalIsdnCalls_Object = MibTableColumn
v52IfIntervalIsdnCalls = _V52IfIntervalIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 8, 1, 9),
    _V52IfIntervalIsdnCalls_Type()
)
v52IfIntervalIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfIntervalIsdnCalls.setStatus("current")
_V52StatsTotalTable_Object = MibTable
v52StatsTotalTable = _V52StatsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9)
)
if mibBuilder.loadTexts:
    v52StatsTotalTable.setStatus("current")
_V52StatsTotalEntry_Object = MibTableRow
v52StatsTotalEntry = _V52StatsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    v52StatsTotalEntry.setStatus("current")
_V52IfTotalPstnOutboundCalls_Type = PerfCurrentCount
_V52IfTotalPstnOutboundCalls_Object = MibTableColumn
v52IfTotalPstnOutboundCalls = _V52IfTotalPstnOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 1),
    _V52IfTotalPstnOutboundCalls_Type()
)
v52IfTotalPstnOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalPstnOutboundCalls.setStatus("current")
_V52IfTotalPstnInboundCalls_Type = PerfCurrentCount
_V52IfTotalPstnInboundCalls_Object = MibTableColumn
v52IfTotalPstnInboundCalls = _V52IfTotalPstnInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 2),
    _V52IfTotalPstnInboundCalls_Type()
)
v52IfTotalPstnInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalPstnInboundCalls.setStatus("current")
_V52IfTotalCallsBlocked_Type = PerfCurrentCount
_V52IfTotalCallsBlocked_Object = MibTableColumn
v52IfTotalCallsBlocked = _V52IfTotalCallsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 3),
    _V52IfTotalCallsBlocked_Type()
)
v52IfTotalCallsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalCallsBlocked.setStatus("current")
_V52IfTotalV52ProtocolErrors_Type = PerfCurrentCount
_V52IfTotalV52ProtocolErrors_Object = MibTableColumn
v52IfTotalV52ProtocolErrors = _V52IfTotalV52ProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 4),
    _V52IfTotalV52ProtocolErrors_Type()
)
v52IfTotalV52ProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalV52ProtocolErrors.setStatus("current")
_V52ifTotalLapdSent_Type = PerfCurrentCount
_V52ifTotalLapdSent_Object = MibTableColumn
v52ifTotalLapdSent = _V52ifTotalLapdSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 5),
    _V52ifTotalLapdSent_Type()
)
v52ifTotalLapdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52ifTotalLapdSent.setStatus("current")
_V52IfTotalLapdRcvd_Type = PerfCurrentCount
_V52IfTotalLapdRcvd_Object = MibTableColumn
v52IfTotalLapdRcvd = _V52IfTotalLapdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 6),
    _V52IfTotalLapdRcvd_Type()
)
v52IfTotalLapdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalLapdRcvd.setStatus("current")
_V52IfTotalLapdRcvdErrs_Type = PerfCurrentCount
_V52IfTotalLapdRcvdErrs_Object = MibTableColumn
v52IfTotalLapdRcvdErrs = _V52IfTotalLapdRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 7),
    _V52IfTotalLapdRcvdErrs_Type()
)
v52IfTotalLapdRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalLapdRcvdErrs.setStatus("current")
_V52IfTotalIsdnCalls_Type = PerfCurrentCount
_V52IfTotalIsdnCalls_Object = MibTableColumn
v52IfTotalIsdnCalls = _V52IfTotalIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 9, 1, 8),
    _V52IfTotalIsdnCalls_Type()
)
v52IfTotalIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52IfTotalIsdnCalls.setStatus("current")
_V52Traps_ObjectIdentity = ObjectIdentity
v52Traps = _V52Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    v52Traps.setStatus("current")
_V52TrapsPrefix_ObjectIdentity = ObjectIdentity
v52TrapsPrefix = _V52TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0)
)
if mibBuilder.loadTexts:
    v52TrapsPrefix.setStatus("current")
_V52IgExtensionTable_Object = MibTable
v52IgExtensionTable = _V52IgExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11)
)
if mibBuilder.loadTexts:
    v52IgExtensionTable.setStatus("current")
_V52IgExtensionEntry_Object = MibTableRow
v52IgExtensionEntry = _V52IgExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    v52IgExtensionEntry.setStatus("current")


class _V52IgStartupCheckLinkId_Type(TruthValue):
    """Custom type v52IgStartupCheckLinkId based on TruthValue"""


_V52IgStartupCheckLinkId_Object = MibTableColumn
v52IgStartupCheckLinkId = _V52IgStartupCheckLinkId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11, 1, 1),
    _V52IgStartupCheckLinkId_Type()
)
v52IgStartupCheckLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgStartupCheckLinkId.setStatus("current")


class _V52IgStartupUnblockUserPorts_Type(TruthValue):
    """Custom type v52IgStartupUnblockUserPorts based on TruthValue"""


_V52IgStartupUnblockUserPorts_Object = MibTableColumn
v52IgStartupUnblockUserPorts = _V52IgStartupUnblockUserPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11, 1, 2),
    _V52IgStartupUnblockUserPorts_Type()
)
v52IgStartupUnblockUserPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgStartupUnblockUserPorts.setStatus("current")


class _V52IgLinkOutOfServiceTimer_Type(Integer32):
    """Custom type v52IgLinkOutOfServiceTimer based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_V52IgLinkOutOfServiceTimer_Type.__name__ = "Integer32"
_V52IgLinkOutOfServiceTimer_Object = MibTableColumn
v52IgLinkOutOfServiceTimer = _V52IgLinkOutOfServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11, 1, 3),
    _V52IgLinkOutOfServiceTimer_Type()
)
v52IgLinkOutOfServiceTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLinkOutOfServiceTimer.setStatus("current")
if mibBuilder.loadTexts:
    v52IgLinkOutOfServiceTimer.setUnits("milliseconds.")


class _V52IgLinkInServiceTimer_Type(Integer32):
    """Custom type v52IgLinkInServiceTimer based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_V52IgLinkInServiceTimer_Type.__name__ = "Integer32"
_V52IgLinkInServiceTimer_Object = MibTableColumn
v52IgLinkInServiceTimer = _V52IgLinkInServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 11, 1, 4),
    _V52IgLinkInServiceTimer_Type()
)
v52IgLinkInServiceTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v52IgLinkInServiceTimer.setStatus("current")
if mibBuilder.loadTexts:
    v52IgLinkInServiceTimer.setUnits("milliseconds")
_V52ProtectionCPathTable_Object = MibTable
v52ProtectionCPathTable = _V52ProtectionCPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 12)
)
if mibBuilder.loadTexts:
    v52ProtectionCPathTable.setStatus("current")
_V52ProtectionCPathEntry_Object = MibTableRow
v52ProtectionCPathEntry = _V52ProtectionCPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 12, 1)
)
v52ProtectionCPathEntry.setIndexNames(
    (0, "ZhoneV52-MIB", "v52IgNameId"),
    (0, "ZhoneV52-MIB", "v52ProtectionCPathId"),
)
if mibBuilder.loadTexts:
    v52ProtectionCPathEntry.setStatus("current")


class _V52ProtectionCPathId_Type(Integer32):
    """Custom type v52ProtectionCPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_V52ProtectionCPathId_Type.__name__ = "Integer32"
_V52ProtectionCPathId_Object = MibTableColumn
v52ProtectionCPathId = _V52ProtectionCPathId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 12, 1, 1),
    _V52ProtectionCPathId_Type()
)
v52ProtectionCPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v52ProtectionCPathId.setStatus("current")


class _V52ProtectionCPathOperStatus_Type(Integer32):
    """Custom type v52ProtectionCPathOperStatus based on Integer32"""
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


_V52ProtectionCPathOperStatus_Type.__name__ = "Integer32"
_V52ProtectionCPathOperStatus_Object = MibTableColumn
v52ProtectionCPathOperStatus = _V52ProtectionCPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 12, 1, 2),
    _V52ProtectionCPathOperStatus_Type()
)
v52ProtectionCPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52ProtectionCPathOperStatus.setStatus("current")


class _V52ProtectionCPathOperStatusCause_Type(Integer32):
    """Custom type v52ProtectionCPathOperStatusCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establishConfirmationReceived", 1),
          ("establishIndicationReceived", 2),
          ("releaseIndicationReceived", 3))
    )


_V52ProtectionCPathOperStatusCause_Type.__name__ = "Integer32"
_V52ProtectionCPathOperStatusCause_Object = MibTableColumn
v52ProtectionCPathOperStatusCause = _V52ProtectionCPathOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 12, 1, 3),
    _V52ProtectionCPathOperStatusCause_Type()
)
v52ProtectionCPathOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v52ProtectionCPathOperStatusCause.setStatus("current")
v52InterfaceGroupEntry.registerAugmentions(
    ("ZhoneV52-MIB",
     "v52InterfaceGroupLapvEntry")
)
v52InterfaceGroupLapvEntry.setIndexNames(*v52InterfaceGroupEntry.getIndexNames())
v52InterfaceGroupEntry.registerAugmentions(
    ("ZhoneV52-MIB",
     "v52StatsCurrentEntry")
)
v52StatsCurrentEntry.setIndexNames(*v52InterfaceGroupEntry.getIndexNames())
v52InterfaceGroupEntry.registerAugmentions(
    ("ZhoneV52-MIB",
     "v52StatsTotalEntry")
)
v52StatsTotalEntry.setIndexNames(*v52InterfaceGroupEntry.getIndexNames())
v52InterfaceGroupEntry.registerAugmentions(
    ("ZhoneV52-MIB",
     "v52IgExtensionEntry")
)
v52IgExtensionEntry.setIndexNames(*v52InterfaceGroupEntry.getIndexNames())

# Managed Objects groups


# Notification objects

v52IgProvVariantRequestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 1)
)
v52IgProvVariantRequestNotification.setObjects(
      *(("ZhoneV52-MIB", "v52IgLocalInterfaceId"),
        ("ZhoneV52-MIB", "v52IgRemoteInterfaceId"),
        ("ZhoneV52-MIB", "v52IgLocalProvVariant"),
        ("ZhoneV52-MIB", "v52IgRemoteProvVariant"),
        ("ZhoneV52-MIB", "v52IgProvVariantRequest"),
        ("ZhoneV52-MIB", "v52IgProvVariantRequestStatus"))
)
if mibBuilder.loadTexts:
    v52IgProvVariantRequestNotification.setStatus(
        "current"
    )

v52IgPortAlignmentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 2)
)
v52IgPortAlignmentNotification.setObjects(
      *(("ZhoneV52-MIB", "v52IgPortAlignmentRequest"),
        ("ZhoneV52-MIB", "v52IgPortAlignmentStatus"))
)
if mibBuilder.loadTexts:
    v52IgPortAlignmentNotification.setStatus(
        "current"
    )

v52LinkCheckIdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 3)
)
v52LinkCheckIdNotification.setObjects(
      *(("ZhoneV52-MIB", "v52LinkCheckId"),
        ("ZhoneV52-MIB", "v52LinkCheckIdStatus"))
)
if mibBuilder.loadTexts:
    v52LinkCheckIdNotification.setStatus(
        "current"
    )

v52LinkBlockNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 4)
)
v52LinkBlockNotification.setObjects(
      *(("ZhoneV52-MIB", "v52LinkBlock"),
        ("ZhoneV52-MIB", "v52LinkBlockStatus"))
)
if mibBuilder.loadTexts:
    v52LinkBlockNotification.setStatus(
        "current"
    )

v52IgOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 5)
)
v52IgOperStatusChange.setObjects(
      *(("ZhoneV52-MIB", "v52IgAdminStatus"),
        ("ZhoneV52-MIB", "v52IgOperationalStatus"),
        ("ZhoneV52-MIB", "v52IgOperStatusCause"))
)
if mibBuilder.loadTexts:
    v52IgOperStatusChange.setStatus(
        "current"
    )

v52CChannelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 6)
)
v52CChannelStatusChange.setObjects(
      *(("ZhoneV52-MIB", "v52CChannelRole"),
        ("ZhoneV52-MIB", "v52CChannelStatus"),
        ("ZhoneV52-MIB", "v52CChannelStatusCause"))
)
if mibBuilder.loadTexts:
    v52CChannelStatusChange.setStatus(
        "current"
    )

v52CPathOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 7)
)
v52CPathOperStatusChange.setObjects(
      *(("ZhoneV52-MIB", "v52CPathOperStatus"),
        ("ZhoneV52-MIB", "v52CPathOperStatusCause"))
)
if mibBuilder.loadTexts:
    v52CPathOperStatusChange.setStatus(
        "current"
    )

v52ProtectionCPathOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 2, 10, 0, 8)
)
v52ProtectionCPathOperStatusChange.setObjects(
      *(("ZhoneV52-MIB", "v52ProtectionCPathOperStatus"),
        ("ZhoneV52-MIB", "v52ProtectionCPathOperStatusCause"))
)
if mibBuilder.loadTexts:
    v52ProtectionCPathOperStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneV52-MIB",
    **{"zhoneV52": zhoneV52,
       "v52InterfaceGroupTable": v52InterfaceGroupTable,
       "v52InterfaceGroupEntry": v52InterfaceGroupEntry,
       "v52IgNameId": v52IgNameId,
       "v52IgShelf": v52IgShelf,
       "v52IgSlot": v52IgSlot,
       "v52IgPeerShelf": v52IgPeerShelf,
       "v52IgPeerSlot": v52IgPeerSlot,
       "v52IgPeerStatus": v52IgPeerStatus,
       "v52IgLocalInterfaceId": v52IgLocalInterfaceId,
       "v52IgRemoteInterfaceId": v52IgRemoteInterfaceId,
       "v52IgLocalProvVariant": v52IgLocalProvVariant,
       "v52IgRemoteProvVariant": v52IgRemoteProvVariant,
       "v52IgProvVariantRequest": v52IgProvVariantRequest,
       "v52IgProvVariantRequestStatus": v52IgProvVariantRequestStatus,
       "v52IgAdminStatus": v52IgAdminStatus,
       "v52IgOperationalStatus": v52IgOperationalStatus,
       "v52IgOperStatusCause": v52IgOperStatusCause,
       "v52IgMaxConfiguredCalls": v52IgMaxConfiguredCalls,
       "v52IgCurrActiveCalls": v52IgCurrActiveCalls,
       "v52IgPstnLayer3StartAddress": v52IgPstnLayer3StartAddress,
       "v52IgIsdnEnvFuncStartAddress": v52IgIsdnEnvFuncStartAddress,
       "v52IgStatsTimeElapsed": v52IgStatsTimeElapsed,
       "v52IgStatsValidIntervals": v52IgStatsValidIntervals,
       "v52IgStatsInvalidIntervals": v52IgStatsInvalidIntervals,
       "v52IgPortAlignmentRequest": v52IgPortAlignmentRequest,
       "v52IgPortAlignmentStatus": v52IgPortAlignmentStatus,
       "v52IgNationalPstnRegion": v52IgNationalPstnRegion,
       "v52IgSwitchVendor": v52IgSwitchVendor,
       "v52IgProtocolSpecification": v52IgProtocolSpecification,
       "v52IgRowStatus": v52IgRowStatus,
       "v52InterfaceGroupLapvTable": v52InterfaceGroupLapvTable,
       "v52InterfaceGroupLapvEntry": v52InterfaceGroupLapvEntry,
       "v52IgLapvMaxOutstandingFrames": v52IgLapvMaxOutstandingFrames,
       "v52IgLapvN200": v52IgLapvN200,
       "v52IgLapvN201": v52IgLapvN201,
       "v52IgLapvT200": v52IgLapvT200,
       "v52IgLapvT203": v52IgLapvT203,
       "v52LinkTable": v52LinkTable,
       "v52LinkEntry": v52LinkEntry,
       "v52LinkDsnLgId": v52LinkDsnLgId,
       "v52LinkDs1ChannelNumber": v52LinkDs1ChannelNumber,
       "v52LinkId": v52LinkId,
       "v52LinkCheckId": v52LinkCheckId,
       "v52LinkCheckIdStatus": v52LinkCheckIdStatus,
       "v52LinkAdminStatus": v52LinkAdminStatus,
       "v52LinkBlock": v52LinkBlock,
       "v52LinkBlockStatus": v52LinkBlockStatus,
       "v52LinkRowStatus": v52LinkRowStatus,
       "v52CChannelTable": v52CChannelTable,
       "v52CChannelEntry": v52CChannelEntry,
       "v52CChannelTimeSlotIndex": v52CChannelTimeSlotIndex,
       "v52CChannelLogicalChannelId": v52CChannelLogicalChannelId,
       "v52CChannelProtGp": v52CChannelProtGp,
       "v52CChannelRole": v52CChannelRole,
       "v52CChannelStatus": v52CChannelStatus,
       "v52CChannelCurrentLogicalChannelId": v52CChannelCurrentLogicalChannelId,
       "v52CChannelRowStatus": v52CChannelRowStatus,
       "v52CChannelStatusCause": v52CChannelStatusCause,
       "v52CPathTable": v52CPathTable,
       "v52CPathEntry": v52CPathEntry,
       "v52CPathId": v52CPathId,
       "v52CPathType": v52CPathType,
       "v52CPathLogicalChannelId": v52CPathLogicalChannelId,
       "v52CPathRowStatus": v52CPathRowStatus,
       "v52CPathOperStatus": v52CPathOperStatus,
       "v52CPathOperStatusCause": v52CPathOperStatusCause,
       "v52UserPortTable": v52UserPortTable,
       "v52UserPortEntry": v52UserPortEntry,
       "v52UserPortAddress": v52UserPortAddress,
       "v52UserPortType": v52UserPortType,
       "v52UserPortAdminStatus": v52UserPortAdminStatus,
       "v52UserPortBlock": v52UserPortBlock,
       "v52UserPortBlockStatus": v52UserPortBlockStatus,
       "v52UserPortRegOrLeaseUser": v52UserPortRegOrLeaseUser,
       "v52UserPortIsdnDsCPathId": v52UserPortIsdnDsCPathId,
       "v52UserPortIsdnPCPathId": v52UserPortIsdnPCPathId,
       "v52UserPortIsdnFCPathId": v52UserPortIsdnFCPathId,
       "v52UserPortRowStatus": v52UserPortRowStatus,
       "v52UserPortOperStatus": v52UserPortOperStatus,
       "v52StatsCurrentTable": v52StatsCurrentTable,
       "v52StatsCurrentEntry": v52StatsCurrentEntry,
       "v52IfCurrentPstnOutboundCalls": v52IfCurrentPstnOutboundCalls,
       "v52IfCurrentPstnInboundCalls": v52IfCurrentPstnInboundCalls,
       "v52IfCurrentCallsBlocked": v52IfCurrentCallsBlocked,
       "v52IfCurrentV52ProtocolErrors": v52IfCurrentV52ProtocolErrors,
       "v52IfCurrentLapdSent": v52IfCurrentLapdSent,
       "v52IfCurrentLapdRcvd": v52IfCurrentLapdRcvd,
       "v52IfCurrentLapdRcvdErrs": v52IfCurrentLapdRcvdErrs,
       "v52IfCurrentIsdnCalls": v52IfCurrentIsdnCalls,
       "v52StatsIntervalTable": v52StatsIntervalTable,
       "v52StatsIntervalEntry": v52StatsIntervalEntry,
       "v52IfIntervalNumber": v52IfIntervalNumber,
       "v52IfIntervalPstnOutboundCalls": v52IfIntervalPstnOutboundCalls,
       "v52IfIntervalPstnInboundCalls": v52IfIntervalPstnInboundCalls,
       "v52IfIntervalCallsBlocked": v52IfIntervalCallsBlocked,
       "v52IfIntervalV52ProtocolErrors": v52IfIntervalV52ProtocolErrors,
       "v52IfIntervalLapdSent": v52IfIntervalLapdSent,
       "v52IfIntervalLapdRcvd": v52IfIntervalLapdRcvd,
       "v52IfIntervalLapdRcvdErrs": v52IfIntervalLapdRcvdErrs,
       "v52IfIntervalIsdnCalls": v52IfIntervalIsdnCalls,
       "v52StatsTotalTable": v52StatsTotalTable,
       "v52StatsTotalEntry": v52StatsTotalEntry,
       "v52IfTotalPstnOutboundCalls": v52IfTotalPstnOutboundCalls,
       "v52IfTotalPstnInboundCalls": v52IfTotalPstnInboundCalls,
       "v52IfTotalCallsBlocked": v52IfTotalCallsBlocked,
       "v52IfTotalV52ProtocolErrors": v52IfTotalV52ProtocolErrors,
       "v52ifTotalLapdSent": v52ifTotalLapdSent,
       "v52IfTotalLapdRcvd": v52IfTotalLapdRcvd,
       "v52IfTotalLapdRcvdErrs": v52IfTotalLapdRcvdErrs,
       "v52IfTotalIsdnCalls": v52IfTotalIsdnCalls,
       "v52Traps": v52Traps,
       "v52TrapsPrefix": v52TrapsPrefix,
       "v52IgProvVariantRequestNotification": v52IgProvVariantRequestNotification,
       "v52IgPortAlignmentNotification": v52IgPortAlignmentNotification,
       "v52LinkCheckIdNotification": v52LinkCheckIdNotification,
       "v52LinkBlockNotification": v52LinkBlockNotification,
       "v52IgOperStatusChange": v52IgOperStatusChange,
       "v52CChannelStatusChange": v52CChannelStatusChange,
       "v52CPathOperStatusChange": v52CPathOperStatusChange,
       "v52ProtectionCPathOperStatusChange": v52ProtectionCPathOperStatusChange,
       "v52IgExtensionTable": v52IgExtensionTable,
       "v52IgExtensionEntry": v52IgExtensionEntry,
       "v52IgStartupCheckLinkId": v52IgStartupCheckLinkId,
       "v52IgStartupUnblockUserPorts": v52IgStartupUnblockUserPorts,
       "v52IgLinkOutOfServiceTimer": v52IgLinkOutOfServiceTimer,
       "v52IgLinkInServiceTimer": v52IgLinkInServiceTimer,
       "v52ProtectionCPathTable": v52ProtectionCPathTable,
       "v52ProtectionCPathEntry": v52ProtectionCPathEntry,
       "v52ProtectionCPathId": v52ProtectionCPathId,
       "v52ProtectionCPathOperStatus": v52ProtectionCPathOperStatus,
       "v52ProtectionCPathOperStatusCause": v52ProtectionCPathOperStatusCause}
)
