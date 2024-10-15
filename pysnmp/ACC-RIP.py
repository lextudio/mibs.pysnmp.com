# SNMP MIB module (ACC-RIP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-RIP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:53 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccRip_ObjectIdentity = ObjectIdentity
accRip = _AccRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16)
)


class _AccRipAdminStatus_Type(Integer32):
    """Custom type accRipAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccRipAdminStatus_Type.__name__ = "Integer32"
_AccRipAdminStatus_Object = MibScalar
accRipAdminStatus = _AccRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 1),
    _AccRipAdminStatus_Type()
)
accRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipAdminStatus.setStatus("mandatory")
_AccRipUpdateTimer_Type = TimeTicks
_AccRipUpdateTimer_Object = MibScalar
accRipUpdateTimer = _AccRipUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 2),
    _AccRipUpdateTimer_Type()
)
accRipUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipUpdateTimer.setStatus("obsolete")


class _AccRipGateway_Type(Integer32):
    """Custom type accRipGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extended", 3),
          ("off", 2),
          ("on", 1))
    )


_AccRipGateway_Type.__name__ = "Integer32"
_AccRipGateway_Object = MibScalar
accRipGateway = _AccRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 3),
    _AccRipGateway_Type()
)
accRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipGateway.setStatus("obsolete")
_AccRipNeighborList_ObjectIdentity = ObjectIdentity
accRipNeighborList = _AccRipNeighborList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5)
)
_AccRipNeighbor_Type = IpAddress
_AccRipNeighbor_Object = MibScalar
accRipNeighbor = _AccRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5, 1),
    _AccRipNeighbor_Type()
)
accRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipNeighbor.setStatus("obsolete")
_AccRipNeighborIfindex_Type = Integer32
_AccRipNeighborIfindex_Object = MibScalar
accRipNeighborIfindex = _AccRipNeighborIfindex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5, 2),
    _AccRipNeighborIfindex_Type()
)
accRipNeighborIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipNeighborIfindex.setStatus("obsolete")
_AccRipInCmdCnts_Type = Counter32
_AccRipInCmdCnts_Object = MibScalar
accRipInCmdCnts = _AccRipInCmdCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 6),
    _AccRipInCmdCnts_Type()
)
accRipInCmdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInCmdCnts.setStatus("obsolete")
_AccRipInRspCnts_Type = Counter32
_AccRipInRspCnts_Object = MibScalar
accRipInRspCnts = _AccRipInRspCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 7),
    _AccRipInRspCnts_Type()
)
accRipInRspCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInRspCnts.setStatus("obsolete")
_AccRipInErrors_Type = Counter32
_AccRipInErrors_Object = MibScalar
accRipInErrors = _AccRipInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 8),
    _AccRipInErrors_Type()
)
accRipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInErrors.setStatus("obsolete")
_AccRipOutCmdCnts_Type = Counter32
_AccRipOutCmdCnts_Object = MibScalar
accRipOutCmdCnts = _AccRipOutCmdCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 9),
    _AccRipOutCmdCnts_Type()
)
accRipOutCmdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipOutCmdCnts.setStatus("obsolete")
_AccRipOutRspCounts_Type = Counter32
_AccRipOutRspCounts_Object = MibScalar
accRipOutRspCounts = _AccRipOutRspCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 10),
    _AccRipOutRspCounts_Type()
)
accRipOutRspCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipOutRspCounts.setStatus("obsolete")
_AccRipGeneral_ObjectIdentity = ObjectIdentity
accRipGeneral = _AccRipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 11)
)


class _AccRipMessageLevel_Type(Integer32):
    """Custom type accRipMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccRipMessageLevel_Type.__name__ = "Integer32"
_AccRipMessageLevel_Object = MibScalar
accRipMessageLevel = _AccRipMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 11, 1),
    _AccRipMessageLevel_Type()
)
accRipMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipMessageLevel.setStatus("mandatory")


class _AccRipDefaultVersion_Type(Integer32):
    """Custom type accRipDefaultVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_AccRipDefaultVersion_Type.__name__ = "Integer32"
_AccRipDefaultVersion_Object = MibScalar
accRipDefaultVersion = _AccRipDefaultVersion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 11, 2),
    _AccRipDefaultVersion_Type()
)
accRipDefaultVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipDefaultVersion.setStatus("mandatory")
_AccRip2IfConfExtTable_Object = MibTable
accRip2IfConfExtTable = _AccRip2IfConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12)
)
if mibBuilder.loadTexts:
    accRip2IfConfExtTable.setStatus("mandatory")
_AccRip2IfConfExtEntry_Object = MibTableRow
accRip2IfConfExtEntry = _AccRip2IfConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1)
)
accRip2IfConfExtEntry.setIndexNames(
    (0, "ACC-RIP", "accRip2IfConfExtAddress"),
)
if mibBuilder.loadTexts:
    accRip2IfConfExtEntry.setStatus("mandatory")
_AccRip2IfConfExtAddress_Type = IpAddress
_AccRip2IfConfExtAddress_Object = MibTableColumn
accRip2IfConfExtAddress = _AccRip2IfConfExtAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 1),
    _AccRip2IfConfExtAddress_Type()
)
accRip2IfConfExtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRip2IfConfExtAddress.setStatus("mandatory")


class _AccRip2IfConfExtProfile_Type(Integer32):
    """Custom type accRip2IfConfExtProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AccRip2IfConfExtProfile_Type.__name__ = "Integer32"
_AccRip2IfConfExtProfile_Object = MibTableColumn
accRip2IfConfExtProfile = _AccRip2IfConfExtProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 2),
    _AccRip2IfConfExtProfile_Type()
)
accRip2IfConfExtProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtProfile.setStatus("mandatory")


class _AccRip2IfConfExtDefaultOnly_Type(Integer32):
    """Custom type accRip2IfConfExtDefaultOnly based on Integer32"""
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


_AccRip2IfConfExtDefaultOnly_Type.__name__ = "Integer32"
_AccRip2IfConfExtDefaultOnly_Object = MibTableColumn
accRip2IfConfExtDefaultOnly = _AccRip2IfConfExtDefaultOnly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 3),
    _AccRip2IfConfExtDefaultOnly_Type()
)
accRip2IfConfExtDefaultOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtDefaultOnly.setStatus("mandatory")


class _AccRip2IfConfExtDefaultMetric_Type(Integer32):
    """Custom type accRip2IfConfExtDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AccRip2IfConfExtDefaultMetric_Type.__name__ = "Integer32"
_AccRip2IfConfExtDefaultMetric_Object = MibTableColumn
accRip2IfConfExtDefaultMetric = _AccRip2IfConfExtDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 4),
    _AccRip2IfConfExtDefaultMetric_Type()
)
accRip2IfConfExtDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtDefaultMetric.setStatus("mandatory")


class _AccRip2IfConfExtMessageLevel_Type(Integer32):
    """Custom type accRip2IfConfExtMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccRip2IfConfExtMessageLevel_Type.__name__ = "Integer32"
_AccRip2IfConfExtMessageLevel_Object = MibTableColumn
accRip2IfConfExtMessageLevel = _AccRip2IfConfExtMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 5),
    _AccRip2IfConfExtMessageLevel_Type()
)
accRip2IfConfExtMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtMessageLevel.setStatus("mandatory")


class _AccRip2IfConfExtAdminStat_Type(Integer32):
    """Custom type accRip2IfConfExtAdminStat based on Integer32"""
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


_AccRip2IfConfExtAdminStat_Type.__name__ = "Integer32"
_AccRip2IfConfExtAdminStat_Object = MibTableColumn
accRip2IfConfExtAdminStat = _AccRip2IfConfExtAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 6),
    _AccRip2IfConfExtAdminStat_Type()
)
accRip2IfConfExtAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtAdminStat.setStatus("mandatory")


class _AccRip2IfConfExtTxOnly_Type(Integer32):
    """Custom type accRip2IfConfExtTxOnly based on Integer32"""
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


_AccRip2IfConfExtTxOnly_Type.__name__ = "Integer32"
_AccRip2IfConfExtTxOnly_Object = MibTableColumn
accRip2IfConfExtTxOnly = _AccRip2IfConfExtTxOnly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 12, 1, 7),
    _AccRip2IfConfExtTxOnly_Type()
)
accRip2IfConfExtTxOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRip2IfConfExtTxOnly.setStatus("mandatory")
_AccRipProfileTable_Object = MibTable
accRipProfileTable = _AccRipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13)
)
if mibBuilder.loadTexts:
    accRipProfileTable.setStatus("mandatory")
_AccRipProfileEntry_Object = MibTableRow
accRipProfileEntry = _AccRipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1)
)
accRipProfileEntry.setIndexNames(
    (0, "ACC-RIP", "accRipProfileId"),
)
if mibBuilder.loadTexts:
    accRipProfileEntry.setStatus("mandatory")


class _AccRipProfileId_Type(Integer32):
    """Custom type accRipProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AccRipProfileId_Type.__name__ = "Integer32"
_AccRipProfileId_Object = MibTableColumn
accRipProfileId = _AccRipProfileId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 1),
    _AccRipProfileId_Type()
)
accRipProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipProfileId.setStatus("mandatory")


class _AccRipProfileUpdateInterval_Type(Integer32):
    """Custom type accRipProfileUpdateInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AccRipProfileUpdateInterval_Type.__name__ = "Integer32"
_AccRipProfileUpdateInterval_Object = MibTableColumn
accRipProfileUpdateInterval = _AccRipProfileUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 2),
    _AccRipProfileUpdateInterval_Type()
)
accRipProfileUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileUpdateInterval.setStatus("mandatory")


class _AccRipProfilePacketGap_Type(Integer32):
    """Custom type accRipProfilePacketGap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccRipProfilePacketGap_Type.__name__ = "Integer32"
_AccRipProfilePacketGap_Object = MibTableColumn
accRipProfilePacketGap = _AccRipProfilePacketGap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 3),
    _AccRipProfilePacketGap_Type()
)
accRipProfilePacketGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfilePacketGap.setStatus("mandatory")


class _AccRipProfileMaxPkts_Type(Integer32):
    """Custom type accRipProfileMaxPkts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccRipProfileMaxPkts_Type.__name__ = "Integer32"
_AccRipProfileMaxPkts_Object = MibTableColumn
accRipProfileMaxPkts = _AccRipProfileMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 4),
    _AccRipProfileMaxPkts_Type()
)
accRipProfileMaxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileMaxPkts.setStatus("mandatory")


class _AccRipProfileRetxTO_Type(Integer32):
    """Custom type accRipProfileRetxTO based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AccRipProfileRetxTO_Type.__name__ = "Integer32"
_AccRipProfileRetxTO_Object = MibTableColumn
accRipProfileRetxTO = _AccRipProfileRetxTO_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 5),
    _AccRipProfileRetxTO_Type()
)
accRipProfileRetxTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileRetxTO.setStatus("mandatory")


class _AccRipProfileShortPollRetries_Type(Integer32):
    """Custom type accRipProfileShortPollRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AccRipProfileShortPollRetries_Type.__name__ = "Integer32"
_AccRipProfileShortPollRetries_Object = MibTableColumn
accRipProfileShortPollRetries = _AccRipProfileShortPollRetries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 6),
    _AccRipProfileShortPollRetries_Type()
)
accRipProfileShortPollRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileShortPollRetries.setStatus("mandatory")


class _AccRipProfileBackground_Type(Integer32):
    """Custom type accRipProfileBackground based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AccRipProfileBackground_Type.__name__ = "Integer32"
_AccRipProfileBackground_Object = MibTableColumn
accRipProfileBackground = _AccRipProfileBackground_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 7),
    _AccRipProfileBackground_Type()
)
accRipProfileBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileBackground.setStatus("mandatory")
_AccRipProfileStatus_Type = RowStatus
_AccRipProfileStatus_Object = MibTableColumn
accRipProfileStatus = _AccRipProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 13, 1, 8),
    _AccRipProfileStatus_Type()
)
accRipProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipProfileStatus.setStatus("mandatory")
_AccRipNbrTable_Object = MibTable
accRipNbrTable = _AccRipNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16)
)
if mibBuilder.loadTexts:
    accRipNbrTable.setStatus("mandatory")
_AccRipNbrEntry_Object = MibTableRow
accRipNbrEntry = _AccRipNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16, 1)
)
accRipNbrEntry.setIndexNames(
    (0, "ACC-RIP", "accRipNbrIpAddr"),
)
if mibBuilder.loadTexts:
    accRipNbrEntry.setStatus("mandatory")
_AccRipNbrIpAddr_Type = IpAddress
_AccRipNbrIpAddr_Object = MibTableColumn
accRipNbrIpAddr = _AccRipNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16, 1, 1),
    _AccRipNbrIpAddr_Type()
)
accRipNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipNbrIpAddr.setStatus("mandatory")


class _AccRipNbrTriggered_Type(Integer32):
    """Custom type accRipNbrTriggered based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 4),
          ("yes", 1))
    )


_AccRipNbrTriggered_Type.__name__ = "Integer32"
_AccRipNbrTriggered_Object = MibTableColumn
accRipNbrTriggered = _AccRipNbrTriggered_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16, 1, 2),
    _AccRipNbrTriggered_Type()
)
accRipNbrTriggered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipNbrTriggered.setStatus("mandatory")
_AccRipNbrType_Type = Integer32
_AccRipNbrType_Object = MibTableColumn
accRipNbrType = _AccRipNbrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16, 1, 3),
    _AccRipNbrType_Type()
)
accRipNbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipNbrType.setStatus("mandatory")
_AccRipNbrStatus_Type = RowStatus
_AccRipNbrStatus_Object = MibTableColumn
accRipNbrStatus = _AccRipNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 16, 1, 4),
    _AccRipNbrStatus_Type()
)
accRipNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipNbrStatus.setStatus("mandatory")
_AccDemandRipTable_Object = MibTable
accDemandRipTable = _AccDemandRipTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17)
)
if mibBuilder.loadTexts:
    accDemandRipTable.setStatus("mandatory")
_AccDemandRipEntry_Object = MibTableRow
accDemandRipEntry = _AccDemandRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1)
)
accDemandRipEntry.setIndexNames(
    (0, "ACC-RIP", "accDemandRipNeighbor"),
)
if mibBuilder.loadTexts:
    accDemandRipEntry.setStatus("mandatory")
_AccDemandRipNeighbor_Type = IpAddress
_AccDemandRipNeighbor_Object = MibTableColumn
accDemandRipNeighbor = _AccDemandRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 1),
    _AccDemandRipNeighbor_Type()
)
accDemandRipNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipNeighbor.setStatus("mandatory")
_AccDemandRipRetxTimeouts_Type = Gauge32
_AccDemandRipRetxTimeouts_Object = MibTableColumn
accDemandRipRetxTimeouts = _AccDemandRipRetxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 2),
    _AccDemandRipRetxTimeouts_Type()
)
accDemandRipRetxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipRetxTimeouts.setStatus("mandatory")
_AccDemandRipShortPollRetries_Type = Gauge32
_AccDemandRipShortPollRetries_Object = MibTableColumn
accDemandRipShortPollRetries = _AccDemandRipShortPollRetries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 3),
    _AccDemandRipShortPollRetries_Type()
)
accDemandRipShortPollRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipShortPollRetries.setStatus("mandatory")
_AccDemandRipBackGroundRetries_Type = Gauge32
_AccDemandRipBackGroundRetries_Object = MibTableColumn
accDemandRipBackGroundRetries = _AccDemandRipBackGroundRetries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 4),
    _AccDemandRipBackGroundRetries_Type()
)
accDemandRipBackGroundRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipBackGroundRetries.setStatus("mandatory")
_AccDemandRipTransitions_Type = Counter32
_AccDemandRipTransitions_Object = MibTableColumn
accDemandRipTransitions = _AccDemandRipTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 5),
    _AccDemandRipTransitions_Type()
)
accDemandRipTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipTransitions.setStatus("mandatory")
_AccDemandRipSeqNumber_Type = Integer32
_AccDemandRipSeqNumber_Object = MibTableColumn
accDemandRipSeqNumber = _AccDemandRipSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 6),
    _AccDemandRipSeqNumber_Type()
)
accDemandRipSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipSeqNumber.setStatus("mandatory")


class _AccDemandRipStatus_Type(Integer32):
    """Custom type accDemandRipStatus based on Integer32"""
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
        *(("attempt", 4),
          ("down", 2),
          ("exchange", 5),
          ("flushed", 6),
          ("notResponding", 3),
          ("up", 1))
    )


_AccDemandRipStatus_Type.__name__ = "Integer32"
_AccDemandRipStatus_Object = MibTableColumn
accDemandRipStatus = _AccDemandRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 17, 1, 7),
    _AccDemandRipStatus_Type()
)
accDemandRipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDemandRipStatus.setStatus("mandatory")
_AccRipExportTable_Object = MibTable
accRipExportTable = _AccRipExportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18)
)
if mibBuilder.loadTexts:
    accRipExportTable.setStatus("mandatory")
_AccRipExportEntry_Object = MibTableRow
accRipExportEntry = _AccRipExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1)
)
accRipExportEntry.setIndexNames(
    (0, "ACC-RIP", "accRipExportProtocol"),
    (0, "ACC-RIP", "accRipExportProtoSpecific"),
    (0, "ACC-RIP", "accRipExportNetwork"),
    (0, "ACC-RIP", "accRipExportMask"),
    (0, "ACC-RIP", "accRipExportDestIf"),
)
if mibBuilder.loadTexts:
    accRipExportEntry.setStatus("mandatory")


class _AccRipExportProtocol_Type(Integer32):
    """Custom type accRipExportProtocol based on Integer32"""
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
        *(("any", 1),
          ("ebgp", 7),
          ("eospf", 5),
          ("ibgp", 8),
          ("iospf", 4),
          ("local", 2),
          ("rip", 6),
          ("static", 3))
    )


_AccRipExportProtocol_Type.__name__ = "Integer32"
_AccRipExportProtocol_Object = MibTableColumn
accRipExportProtocol = _AccRipExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 1),
    _AccRipExportProtocol_Type()
)
accRipExportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipExportProtocol.setStatus("mandatory")
_AccRipExportProtoSpecific_Type = Integer32
_AccRipExportProtoSpecific_Object = MibTableColumn
accRipExportProtoSpecific = _AccRipExportProtoSpecific_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 2),
    _AccRipExportProtoSpecific_Type()
)
accRipExportProtoSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipExportProtoSpecific.setStatus("mandatory")
_AccRipExportNetwork_Type = IpAddress
_AccRipExportNetwork_Object = MibTableColumn
accRipExportNetwork = _AccRipExportNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 3),
    _AccRipExportNetwork_Type()
)
accRipExportNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipExportNetwork.setStatus("mandatory")
_AccRipExportMask_Type = IpAddress
_AccRipExportMask_Object = MibTableColumn
accRipExportMask = _AccRipExportMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 4),
    _AccRipExportMask_Type()
)
accRipExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipExportMask.setStatus("mandatory")
_AccRipExportDestIf_Type = IpAddress
_AccRipExportDestIf_Object = MibTableColumn
accRipExportDestIf = _AccRipExportDestIf_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 5),
    _AccRipExportDestIf_Type()
)
accRipExportDestIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipExportDestIf.setStatus("mandatory")


class _AccRipExportAction_Type(Integer32):
    """Custom type accRipExportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("export", 1))
    )


_AccRipExportAction_Type.__name__ = "Integer32"
_AccRipExportAction_Object = MibTableColumn
accRipExportAction = _AccRipExportAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 6),
    _AccRipExportAction_Type()
)
accRipExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipExportAction.setStatus("mandatory")


class _AccRipExportMetric_Type(Integer32):
    """Custom type accRipExportMetric based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_AccRipExportMetric_Type.__name__ = "Integer32"
_AccRipExportMetric_Object = MibTableColumn
accRipExportMetric = _AccRipExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 7),
    _AccRipExportMetric_Type()
)
accRipExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipExportMetric.setStatus("mandatory")
_AccRipExportStatus_Type = RowStatus
_AccRipExportStatus_Object = MibTableColumn
accRipExportStatus = _AccRipExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 18, 1, 8),
    _AccRipExportStatus_Type()
)
accRipExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipExportStatus.setStatus("mandatory")
_AccRipImportTable_Object = MibTable
accRipImportTable = _AccRipImportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19)
)
if mibBuilder.loadTexts:
    accRipImportTable.setStatus("mandatory")
_AccRipImportEntry_Object = MibTableRow
accRipImportEntry = _AccRipImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1)
)
accRipImportEntry.setIndexNames(
    (0, "ACC-RIP", "accRipImportInterface"),
    (0, "ACC-RIP", "accRipImportPeerAddress"),
    (0, "ACC-RIP", "accRipImportNetwork"),
    (0, "ACC-RIP", "accRipImportMask"),
)
if mibBuilder.loadTexts:
    accRipImportEntry.setStatus("mandatory")
_AccRipImportInterface_Type = IpAddress
_AccRipImportInterface_Object = MibTableColumn
accRipImportInterface = _AccRipImportInterface_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 1),
    _AccRipImportInterface_Type()
)
accRipImportInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipImportInterface.setStatus("mandatory")
_AccRipImportPeerAddress_Type = IpAddress
_AccRipImportPeerAddress_Object = MibTableColumn
accRipImportPeerAddress = _AccRipImportPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 2),
    _AccRipImportPeerAddress_Type()
)
accRipImportPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipImportPeerAddress.setStatus("mandatory")
_AccRipImportNetwork_Type = IpAddress
_AccRipImportNetwork_Object = MibTableColumn
accRipImportNetwork = _AccRipImportNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 3),
    _AccRipImportNetwork_Type()
)
accRipImportNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipImportNetwork.setStatus("mandatory")
_AccRipImportMask_Type = IpAddress
_AccRipImportMask_Object = MibTableColumn
accRipImportMask = _AccRipImportMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 4),
    _AccRipImportMask_Type()
)
accRipImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipImportMask.setStatus("mandatory")


class _AccRipImportAction_Type(Integer32):
    """Custom type accRipImportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("import", 1))
    )


_AccRipImportAction_Type.__name__ = "Integer32"
_AccRipImportAction_Object = MibTableColumn
accRipImportAction = _AccRipImportAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 5),
    _AccRipImportAction_Type()
)
accRipImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipImportAction.setStatus("mandatory")


class _AccRipImportMetric_Type(Integer32):
    """Custom type accRipImportMetric based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccRipImportMetric_Type.__name__ = "Integer32"
_AccRipImportMetric_Object = MibTableColumn
accRipImportMetric = _AccRipImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 6),
    _AccRipImportMetric_Type()
)
accRipImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipImportMetric.setStatus("mandatory")


class _AccRipImportPref_Type(Integer32):
    """Custom type accRipImportPref based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccRipImportPref_Type.__name__ = "Integer32"
_AccRipImportPref_Object = MibTableColumn
accRipImportPref = _AccRipImportPref_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 7),
    _AccRipImportPref_Type()
)
accRipImportPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipImportPref.setStatus("mandatory")
_AccRipImportStatus_Type = RowStatus
_AccRipImportStatus_Object = MibTableColumn
accRipImportStatus = _AccRipImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 19, 1, 8),
    _AccRipImportStatus_Type()
)
accRipImportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipImportStatus.setStatus("mandatory")
_AccRipTraps_ObjectIdentity = ObjectIdentity
accRipTraps = _AccRipTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20)
)
_AccRipTrapMsg_Type = DisplayString
_AccRipTrapMsg_Object = MibScalar
accRipTrapMsg = _AccRipTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 1),
    _AccRipTrapMsg_Type()
)
accRipTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accRipFiltPolAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 1)
)
accRipFiltPolAllocTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipImportInterface"),
        ("ACC-RIP", "accRipImportPeerAddress"),
        ("ACC-RIP", "accRipImportNetwork"),
        ("ACC-RIP", "accRipImportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipFiltPolAllocTrap.setStatus(
        ""
    )

accRipFiltPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 2)
)
accRipFiltPolTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipImportInterface"),
        ("ACC-RIP", "accRipImportPeerAddress"),
        ("ACC-RIP", "accRipImportNetwork"),
        ("ACC-RIP", "accRipImportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipFiltPolTrap.setStatus(
        ""
    )

accRipImpPolAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 3)
)
accRipImpPolAllocTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipExportMask"),
        ("ACC-RIP", "accRipExportNetwork"),
        ("ACC-RIP", "accRipExportProtocol"),
        ("ACC-RIP", "accRipExportProtoSpecific"),
        ("ACC-RIP", "accRipExportDestIf"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipImpPolAllocTrap.setStatus(
        ""
    )

accRipImpPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 4)
)
accRipImpPolTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipExportMask"),
        ("ACC-RIP", "accRipExportNetwork"),
        ("ACC-RIP", "accRipExportProtocol"),
        ("ACC-RIP", "accRipExportProtoSpecific"),
        ("ACC-RIP", "accRipExportDestIf"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipImpPolTrap.setStatus(
        ""
    )

accRipNbrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 5)
)
accRipNbrTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNbrTrap.setStatus(
        ""
    )

accRipNbrIncompatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 6)
)
accRipNbrIncompatTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNbrIncompatTrap.setStatus(
        ""
    )

accRipDefProfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 7)
)
accRipDefProfTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipProfileId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipDefProfTrap.setStatus(
        ""
    )

accRipProfUsedByIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 8)
)
accRipProfUsedByIntfTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipProfileId"),
        ("IF-MIB", "ifIndex"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipProfUsedByIntfTrap.setStatus(
        ""
    )

accRipMustBeDisbldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 9)
)
accRipMustBeDisbldTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipAdminStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipMustBeDisbldTrap.setStatus(
        ""
    )

accRipUpdateIntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 10)
)
accRipUpdateIntTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipProfileId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipUpdateIntTrap.setStatus(
        ""
    )

accRipInitNbrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 11)
)
accRipInitNbrTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipInitNbrTrap.setStatus(
        ""
    )

accRipNbrAvlInsrtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 12)
)
accRipNbrAvlInsrtTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNbrAvlInsrtTrap.setStatus(
        ""
    )

accRipRtNotifIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 13)
)
accRipRtNotifIdTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipRtNotifIdTrap.setStatus(
        ""
    )

accRipNbrNxtHopMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 14)
)
accRipNbrNxtHopMemTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNbrNxtHopMemTrap.setStatus(
        ""
    )

accRipNoIntfMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 15)
)
accRipNoIntfMemTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipDefaultVersion"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNoIntfMemTrap.setStatus(
        ""
    )

accRipAddNbrRtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 16)
)
accRipAddNbrRtTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipAddNbrRtTrap.setStatus(
        ""
    )

accRipMaxIntfGrpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 17)
)
accRipMaxIntfGrpTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipMaxIntfGrpTrap.setStatus(
        ""
    )

accRipMemReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 18)
)
accRipMemReqTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipMemReqTrap.setStatus(
        ""
    )

accRipUpdateEvntHndlrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 19)
)
accRipUpdateEvntHndlrTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipProfileId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipUpdateEvntHndlrTrap.setStatus(
        ""
    )

accRipIntfLnkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 20)
)
accRipIntfLnkUpTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipIntfLnkUpTrap.setStatus(
        ""
    )

accRipEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 21)
)
accRipEnableTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipDefaultVersion"),
        ("ACC-RIP", "accRip2IfConfExtAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipEnableTrap.setStatus(
        ""
    )

accRipInitFiltPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 22)
)
accRipInitFiltPolTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipInitFiltPolTrap.setStatus(
        ""
    )

accRipInitImpPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 23)
)
accRipInitImpPolTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipInitImpPolTrap.setStatus(
        ""
    )

accRipNoNotifIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 24)
)
accRipNoNotifIdTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipNoNotifIdTrap.setStatus(
        ""
    )

accRipMaxReTxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 20, 0, 25)
)
accRipMaxReTxTrap.setObjects(
      *(("ACC-RIP", "accRipTrapMsg"),
        ("ACC-RIP", "accRipNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRipMaxReTxTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-RIP",
    **{"accRip": accRip,
       "accRipAdminStatus": accRipAdminStatus,
       "accRipUpdateTimer": accRipUpdateTimer,
       "accRipGateway": accRipGateway,
       "accRipNeighborList": accRipNeighborList,
       "accRipNeighbor": accRipNeighbor,
       "accRipNeighborIfindex": accRipNeighborIfindex,
       "accRipInCmdCnts": accRipInCmdCnts,
       "accRipInRspCnts": accRipInRspCnts,
       "accRipInErrors": accRipInErrors,
       "accRipOutCmdCnts": accRipOutCmdCnts,
       "accRipOutRspCounts": accRipOutRspCounts,
       "accRipGeneral": accRipGeneral,
       "accRipMessageLevel": accRipMessageLevel,
       "accRipDefaultVersion": accRipDefaultVersion,
       "accRip2IfConfExtTable": accRip2IfConfExtTable,
       "accRip2IfConfExtEntry": accRip2IfConfExtEntry,
       "accRip2IfConfExtAddress": accRip2IfConfExtAddress,
       "accRip2IfConfExtProfile": accRip2IfConfExtProfile,
       "accRip2IfConfExtDefaultOnly": accRip2IfConfExtDefaultOnly,
       "accRip2IfConfExtDefaultMetric": accRip2IfConfExtDefaultMetric,
       "accRip2IfConfExtMessageLevel": accRip2IfConfExtMessageLevel,
       "accRip2IfConfExtAdminStat": accRip2IfConfExtAdminStat,
       "accRip2IfConfExtTxOnly": accRip2IfConfExtTxOnly,
       "accRipProfileTable": accRipProfileTable,
       "accRipProfileEntry": accRipProfileEntry,
       "accRipProfileId": accRipProfileId,
       "accRipProfileUpdateInterval": accRipProfileUpdateInterval,
       "accRipProfilePacketGap": accRipProfilePacketGap,
       "accRipProfileMaxPkts": accRipProfileMaxPkts,
       "accRipProfileRetxTO": accRipProfileRetxTO,
       "accRipProfileShortPollRetries": accRipProfileShortPollRetries,
       "accRipProfileBackground": accRipProfileBackground,
       "accRipProfileStatus": accRipProfileStatus,
       "accRipNbrTable": accRipNbrTable,
       "accRipNbrEntry": accRipNbrEntry,
       "accRipNbrIpAddr": accRipNbrIpAddr,
       "accRipNbrTriggered": accRipNbrTriggered,
       "accRipNbrType": accRipNbrType,
       "accRipNbrStatus": accRipNbrStatus,
       "accDemandRipTable": accDemandRipTable,
       "accDemandRipEntry": accDemandRipEntry,
       "accDemandRipNeighbor": accDemandRipNeighbor,
       "accDemandRipRetxTimeouts": accDemandRipRetxTimeouts,
       "accDemandRipShortPollRetries": accDemandRipShortPollRetries,
       "accDemandRipBackGroundRetries": accDemandRipBackGroundRetries,
       "accDemandRipTransitions": accDemandRipTransitions,
       "accDemandRipSeqNumber": accDemandRipSeqNumber,
       "accDemandRipStatus": accDemandRipStatus,
       "accRipExportTable": accRipExportTable,
       "accRipExportEntry": accRipExportEntry,
       "accRipExportProtocol": accRipExportProtocol,
       "accRipExportProtoSpecific": accRipExportProtoSpecific,
       "accRipExportNetwork": accRipExportNetwork,
       "accRipExportMask": accRipExportMask,
       "accRipExportDestIf": accRipExportDestIf,
       "accRipExportAction": accRipExportAction,
       "accRipExportMetric": accRipExportMetric,
       "accRipExportStatus": accRipExportStatus,
       "accRipImportTable": accRipImportTable,
       "accRipImportEntry": accRipImportEntry,
       "accRipImportInterface": accRipImportInterface,
       "accRipImportPeerAddress": accRipImportPeerAddress,
       "accRipImportNetwork": accRipImportNetwork,
       "accRipImportMask": accRipImportMask,
       "accRipImportAction": accRipImportAction,
       "accRipImportMetric": accRipImportMetric,
       "accRipImportPref": accRipImportPref,
       "accRipImportStatus": accRipImportStatus,
       "accRipTraps": accRipTraps,
       "accRipFiltPolAllocTrap": accRipFiltPolAllocTrap,
       "accRipFiltPolTrap": accRipFiltPolTrap,
       "accRipImpPolAllocTrap": accRipImpPolAllocTrap,
       "accRipImpPolTrap": accRipImpPolTrap,
       "accRipNbrTrap": accRipNbrTrap,
       "accRipNbrIncompatTrap": accRipNbrIncompatTrap,
       "accRipDefProfTrap": accRipDefProfTrap,
       "accRipProfUsedByIntfTrap": accRipProfUsedByIntfTrap,
       "accRipMustBeDisbldTrap": accRipMustBeDisbldTrap,
       "accRipUpdateIntTrap": accRipUpdateIntTrap,
       "accRipInitNbrTrap": accRipInitNbrTrap,
       "accRipNbrAvlInsrtTrap": accRipNbrAvlInsrtTrap,
       "accRipRtNotifIdTrap": accRipRtNotifIdTrap,
       "accRipNbrNxtHopMemTrap": accRipNbrNxtHopMemTrap,
       "accRipNoIntfMemTrap": accRipNoIntfMemTrap,
       "accRipAddNbrRtTrap": accRipAddNbrRtTrap,
       "accRipMaxIntfGrpTrap": accRipMaxIntfGrpTrap,
       "accRipMemReqTrap": accRipMemReqTrap,
       "accRipUpdateEvntHndlrTrap": accRipUpdateEvntHndlrTrap,
       "accRipIntfLnkUpTrap": accRipIntfLnkUpTrap,
       "accRipEnableTrap": accRipEnableTrap,
       "accRipInitFiltPolTrap": accRipInitFiltPolTrap,
       "accRipInitImpPolTrap": accRipInitImpPolTrap,
       "accRipNoNotifIdTrap": accRipNoNotifIdTrap,
       "accRipMaxReTxTrap": accRipMaxReTxTrap,
       "accRipTrapMsg": accRipTrapMsg}
)
