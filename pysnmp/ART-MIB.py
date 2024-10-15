# SNMP MIB module (ART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:41 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(DataSource,
 protocolDirEntry,
 protocolDirLocalIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "DataSource",
    "protocolDirEntry",
    "protocolDirLocalIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

art = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Frontier_ObjectIdentity = ObjectIdentity
frontier = _Frontier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141)
)
_Mibdoc2_ObjectIdentity = ObjectIdentity
mibdoc2 = _Mibdoc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2)
)
_Netscout2_ObjectIdentity = ObjectIdentity
netscout2 = _Netscout2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1)
)
_ProtocolDir2Table_Object = MibTable
protocolDir2Table = _ProtocolDir2Table_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    protocolDir2Table.setStatus("current")
_ProtocolDir2Entry_Object = MibTableRow
protocolDir2Entry = _ProtocolDir2Entry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    protocolDir2Entry.setStatus("current")


class _ProtocolDir2ArtConfig_Type(Integer32):
    """Custom type protocolDir2ArtConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedOff", 2),
          ("supportedOn", 3))
    )


_ProtocolDir2ArtConfig_Type.__name__ = "Integer32"
_ProtocolDir2ArtConfig_Object = MibTableColumn
protocolDir2ArtConfig = _ProtocolDir2ArtConfig_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 1, 1, 1),
    _ProtocolDir2ArtConfig_Type()
)
protocolDir2ArtConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDir2ArtConfig.setStatus("current")
_ArtControlTable_Object = MibTable
artControlTable = _ArtControlTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    artControlTable.setStatus("current")
_ArtControlEntry_Object = MibTableRow
artControlEntry = _ArtControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1)
)
artControlEntry.setIndexNames(
    (0, "ART-MIB", "artControlIndex"),
)
if mibBuilder.loadTexts:
    artControlEntry.setStatus("current")


class _ArtControlIndex_Type(Integer32):
    """Custom type artControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArtControlIndex_Type.__name__ = "Integer32"
_ArtControlIndex_Object = MibTableColumn
artControlIndex = _ArtControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 1),
    _ArtControlIndex_Type()
)
artControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artControlIndex.setStatus("current")
_ArtControlDataSource_Type = DataSource
_ArtControlDataSource_Object = MibTableColumn
artControlDataSource = _ArtControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 2),
    _ArtControlDataSource_Type()
)
artControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlDataSource.setStatus("current")


class _ArtControlTimeRemaining_Type(Integer32):
    """Custom type artControlTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ArtControlTimeRemaining_Type.__name__ = "Integer32"
_ArtControlTimeRemaining_Object = MibTableColumn
artControlTimeRemaining = _ArtControlTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 3),
    _ArtControlTimeRemaining_Type()
)
artControlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    artControlTimeRemaining.setUnits("seconds")


class _ArtControlDuration_Type(Integer32):
    """Custom type artControlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ArtControlDuration_Type.__name__ = "Integer32"
_ArtControlDuration_Object = MibTableColumn
artControlDuration = _ArtControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 4),
    _ArtControlDuration_Type()
)
artControlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artControlDuration.setStatus("current")
if mibBuilder.loadTexts:
    artControlDuration.setUnits("seconds")


class _ArtControlRspTime1_Type(Integer32):
    """Custom type artControlRspTime1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime1_Type.__name__ = "Integer32"
_ArtControlRspTime1_Object = MibTableColumn
artControlRspTime1 = _ArtControlRspTime1_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 5),
    _ArtControlRspTime1_Type()
)
artControlRspTime1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime1.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime1.setUnits("milliseconds")


class _ArtControlRspTime2_Type(Integer32):
    """Custom type artControlRspTime2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime2_Type.__name__ = "Integer32"
_ArtControlRspTime2_Object = MibTableColumn
artControlRspTime2 = _ArtControlRspTime2_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 6),
    _ArtControlRspTime2_Type()
)
artControlRspTime2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime2.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime2.setUnits("milliseconds")


class _ArtControlRspTime3_Type(Integer32):
    """Custom type artControlRspTime3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime3_Type.__name__ = "Integer32"
_ArtControlRspTime3_Object = MibTableColumn
artControlRspTime3 = _ArtControlRspTime3_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 7),
    _ArtControlRspTime3_Type()
)
artControlRspTime3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime3.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime3.setUnits("milliseconds")


class _ArtControlRspTime4_Type(Integer32):
    """Custom type artControlRspTime4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime4_Type.__name__ = "Integer32"
_ArtControlRspTime4_Object = MibTableColumn
artControlRspTime4 = _ArtControlRspTime4_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 8),
    _ArtControlRspTime4_Type()
)
artControlRspTime4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime4.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime4.setUnits("milliseconds")


class _ArtControlRspTime5_Type(Integer32):
    """Custom type artControlRspTime5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime5_Type.__name__ = "Integer32"
_ArtControlRspTime5_Object = MibTableColumn
artControlRspTime5 = _ArtControlRspTime5_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 9),
    _ArtControlRspTime5_Type()
)
artControlRspTime5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime5.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime5.setUnits("milliseconds")


class _ArtControlRspTime6_Type(Integer32):
    """Custom type artControlRspTime6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTime6_Type.__name__ = "Integer32"
_ArtControlRspTime6_Object = MibTableColumn
artControlRspTime6 = _ArtControlRspTime6_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 10),
    _ArtControlRspTime6_Type()
)
artControlRspTime6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTime6.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTime6.setUnits("milliseconds")


class _ArtControlRspTimeout_Type(Integer32):
    """Custom type artControlRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtControlRspTimeout_Type.__name__ = "Integer32"
_ArtControlRspTimeout_Object = MibTableColumn
artControlRspTimeout = _ArtControlRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 11),
    _ArtControlRspTimeout_Type()
)
artControlRspTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRspTimeout.setStatus("current")
if mibBuilder.loadTexts:
    artControlRspTimeout.setUnits("milliseconds")
_ArtControlRptStartTime_Type = TimeStamp
_ArtControlRptStartTime_Object = MibTableColumn
artControlRptStartTime = _ArtControlRptStartTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 12),
    _ArtControlRptStartTime_Type()
)
artControlRptStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artControlRptStartTime.setStatus("current")


class _ArtControlRequestedSize_Type(Integer32):
    """Custom type artControlRequestedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_ArtControlRequestedSize_Type.__name__ = "Integer32"
_ArtControlRequestedSize_Object = MibTableColumn
artControlRequestedSize = _ArtControlRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 13),
    _ArtControlRequestedSize_Type()
)
artControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlRequestedSize.setStatus("current")


class _ArtControlGrantedSize_Type(Integer32):
    """Custom type artControlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArtControlGrantedSize_Type.__name__ = "Integer32"
_ArtControlGrantedSize_Object = MibTableColumn
artControlGrantedSize = _ArtControlGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 14),
    _ArtControlGrantedSize_Type()
)
artControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artControlGrantedSize.setStatus("current")


class _ArtControlGeneratedRpts_Type(Integer32):
    """Custom type artControlGeneratedRpts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArtControlGeneratedRpts_Type.__name__ = "Integer32"
_ArtControlGeneratedRpts_Object = MibTableColumn
artControlGeneratedRpts = _ArtControlGeneratedRpts_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 15),
    _ArtControlGeneratedRpts_Type()
)
artControlGeneratedRpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artControlGeneratedRpts.setStatus("current")
_ArtControlDroppedFrames_Type = Counter32
_ArtControlDroppedFrames_Object = MibTableColumn
artControlDroppedFrames = _ArtControlDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 16),
    _ArtControlDroppedFrames_Type()
)
artControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artControlDroppedFrames.setStatus("current")
_ArtControlOwner_Type = OwnerString
_ArtControlOwner_Object = MibTableColumn
artControlOwner = _ArtControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 17),
    _ArtControlOwner_Type()
)
artControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlOwner.setStatus("current")
_ArtControlStatus_Type = RowStatus
_ArtControlStatus_Object = MibTableColumn
artControlStatus = _ArtControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 2, 1, 18),
    _ArtControlStatus_Type()
)
artControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artControlStatus.setStatus("current")
_ArtTable_Object = MibTable
artTable = _ArtTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    artTable.setStatus("current")
_ArtEntry_Object = MibTableRow
artEntry = _ArtEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1)
)
artEntry.setIndexNames(
    (0, "ART-MIB", "artControlIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "ART-MIB", "artServerAddress"),
    (0, "ART-MIB", "artClientAddress"),
)
if mibBuilder.loadTexts:
    artEntry.setStatus("current")
_ArtServerAddress_Type = OctetString
_ArtServerAddress_Object = MibTableColumn
artServerAddress = _ArtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 1),
    _ArtServerAddress_Type()
)
artServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artServerAddress.setStatus("current")
_ArtClientAddress_Type = OctetString
_ArtClientAddress_Object = MibTableColumn
artClientAddress = _ArtClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 2),
    _ArtClientAddress_Type()
)
artClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artClientAddress.setStatus("current")


class _ArtAvgRspTime_Type(Integer32):
    """Custom type artAvgRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtAvgRspTime_Type.__name__ = "Integer32"
_ArtAvgRspTime_Object = MibTableColumn
artAvgRspTime = _ArtAvgRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 3),
    _ArtAvgRspTime_Type()
)
artAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artAvgRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artAvgRspTime.setUnits("milliseconds")


class _ArtMinRspTime_Type(Integer32):
    """Custom type artMinRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtMinRspTime_Type.__name__ = "Integer32"
_ArtMinRspTime_Object = MibTableColumn
artMinRspTime = _ArtMinRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 4),
    _ArtMinRspTime_Type()
)
artMinRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMinRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artMinRspTime.setUnits("milliseconds")


class _ArtMaxRspTime_Type(Integer32):
    """Custom type artMaxRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtMaxRspTime_Type.__name__ = "Integer32"
_ArtMaxRspTime_Object = MibTableColumn
artMaxRspTime = _ArtMaxRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 5),
    _ArtMaxRspTime_Type()
)
artMaxRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMaxRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artMaxRspTime.setUnits("milliseconds")
_ArtTotalResponses_Type = Counter32
_ArtTotalResponses_Object = MibTableColumn
artTotalResponses = _ArtTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 6),
    _ArtTotalResponses_Type()
)
artTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artTotalResponses.setStatus("current")
_ArtRsps1_Type = Counter32
_ArtRsps1_Object = MibTableColumn
artRsps1 = _ArtRsps1_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 7),
    _ArtRsps1_Type()
)
artRsps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps1.setStatus("current")
_ArtRsps2_Type = Counter32
_ArtRsps2_Object = MibTableColumn
artRsps2 = _ArtRsps2_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 8),
    _ArtRsps2_Type()
)
artRsps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps2.setStatus("current")
_ArtRsps3_Type = Counter32
_ArtRsps3_Object = MibTableColumn
artRsps3 = _ArtRsps3_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 9),
    _ArtRsps3_Type()
)
artRsps3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps3.setStatus("current")
_ArtRsps4_Type = Counter32
_ArtRsps4_Object = MibTableColumn
artRsps4 = _ArtRsps4_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 10),
    _ArtRsps4_Type()
)
artRsps4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps4.setStatus("current")
_ArtRsps5_Type = Counter32
_ArtRsps5_Object = MibTableColumn
artRsps5 = _ArtRsps5_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 11),
    _ArtRsps5_Type()
)
artRsps5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps5.setStatus("current")
_ArtRsps6_Type = Counter32
_ArtRsps6_Object = MibTableColumn
artRsps6 = _ArtRsps6_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 12),
    _ArtRsps6_Type()
)
artRsps6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps6.setStatus("current")
_ArtRsps7_Type = Counter32
_ArtRsps7_Object = MibTableColumn
artRsps7 = _ArtRsps7_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 13),
    _ArtRsps7_Type()
)
artRsps7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRsps7.setStatus("current")
_ArtClientOctets_Type = Counter32
_ArtClientOctets_Object = MibTableColumn
artClientOctets = _ArtClientOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 14),
    _ArtClientOctets_Type()
)
artClientOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artClientOctets.setStatus("current")
_ArtClientOverflowOctets_Type = Counter32
_ArtClientOverflowOctets_Object = MibTableColumn
artClientOverflowOctets = _ArtClientOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 15),
    _ArtClientOverflowOctets_Type()
)
artClientOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artClientOverflowOctets.setStatus("current")
_ArtClientHCOctets_Type = Counter64
_ArtClientHCOctets_Object = MibTableColumn
artClientHCOctets = _ArtClientHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 16),
    _ArtClientHCOctets_Type()
)
artClientHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artClientHCOctets.setStatus("current")
_ArtServerOctets_Type = Counter32
_ArtServerOctets_Object = MibTableColumn
artServerOctets = _ArtServerOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 17),
    _ArtServerOctets_Type()
)
artServerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artServerOctets.setStatus("current")
_ArtServerOverflowOctets_Type = Counter32
_ArtServerOverflowOctets_Object = MibTableColumn
artServerOverflowOctets = _ArtServerOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 18),
    _ArtServerOverflowOctets_Type()
)
artServerOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artServerOverflowOctets.setStatus("current")
_ArtServerHCOctets_Type = Counter64
_ArtServerHCOctets_Object = MibTableColumn
artServerHCOctets = _ArtServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 19),
    _ArtServerHCOctets_Type()
)
artServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artServerHCOctets.setStatus("current")
_ArtRetries_Type = Counter32
_ArtRetries_Object = MibTableColumn
artRetries = _ArtRetries_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 20),
    _ArtRetries_Type()
)
artRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artRetries.setStatus("current")
_ArtTimeouts_Type = Counter32
_ArtTimeouts_Object = MibTableColumn
artTimeouts = _ArtTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 3, 1, 21),
    _ArtTimeouts_Type()
)
artTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artTimeouts.setStatus("current")
_ArtConformance_ObjectIdentity = ObjectIdentity
artConformance = _ArtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 4)
)
_ArtMIBCompliances_ObjectIdentity = ObjectIdentity
artMIBCompliances = _ArtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 4, 1)
)
_ArtMIBGroups_ObjectIdentity = ObjectIdentity
artMIBGroups = _ArtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 4, 2)
)
_ArtSummaryTable_Object = MibTable
artSummaryTable = _ArtSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    artSummaryTable.setStatus("current")
_ArtSummaryEntry_Object = MibTableRow
artSummaryEntry = _ArtSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1)
)
artSummaryEntry.setIndexNames(
    (0, "ART-MIB", "artControlIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "ART-MIB", "artSummaryServerAddress"),
)
if mibBuilder.loadTexts:
    artSummaryEntry.setStatus("current")
_ArtSummaryServerAddress_Type = OctetString
_ArtSummaryServerAddress_Object = MibTableColumn
artSummaryServerAddress = _ArtSummaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 1),
    _ArtSummaryServerAddress_Type()
)
artSummaryServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artSummaryServerAddress.setStatus("current")


class _ArtSummaryClients_Type(Integer32):
    """Custom type artSummaryClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtSummaryClients_Type.__name__ = "Integer32"
_ArtSummaryClients_Object = MibTableColumn
artSummaryClients = _ArtSummaryClients_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 2),
    _ArtSummaryClients_Type()
)
artSummaryClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryClients.setStatus("current")


class _ArtSummaryAvgRspTime_Type(Integer32):
    """Custom type artSummaryAvgRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtSummaryAvgRspTime_Type.__name__ = "Integer32"
_ArtSummaryAvgRspTime_Object = MibTableColumn
artSummaryAvgRspTime = _ArtSummaryAvgRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 3),
    _ArtSummaryAvgRspTime_Type()
)
artSummaryAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryAvgRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artSummaryAvgRspTime.setUnits("milliseconds")


class _ArtSummaryMinRspTime_Type(Integer32):
    """Custom type artSummaryMinRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtSummaryMinRspTime_Type.__name__ = "Integer32"
_ArtSummaryMinRspTime_Object = MibTableColumn
artSummaryMinRspTime = _ArtSummaryMinRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 4),
    _ArtSummaryMinRspTime_Type()
)
artSummaryMinRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryMinRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artSummaryMinRspTime.setUnits("milliseconds")


class _ArtSummaryMaxRspTime_Type(Integer32):
    """Custom type artSummaryMaxRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArtSummaryMaxRspTime_Type.__name__ = "Integer32"
_ArtSummaryMaxRspTime_Object = MibTableColumn
artSummaryMaxRspTime = _ArtSummaryMaxRspTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 5),
    _ArtSummaryMaxRspTime_Type()
)
artSummaryMaxRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryMaxRspTime.setStatus("current")
if mibBuilder.loadTexts:
    artSummaryMaxRspTime.setUnits("milliseconds")
_ArtSummaryTotalResponses_Type = Counter32
_ArtSummaryTotalResponses_Object = MibTableColumn
artSummaryTotalResponses = _ArtSummaryTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 6),
    _ArtSummaryTotalResponses_Type()
)
artSummaryTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryTotalResponses.setStatus("current")
_ArtSummaryRsps1_Type = Counter32
_ArtSummaryRsps1_Object = MibTableColumn
artSummaryRsps1 = _ArtSummaryRsps1_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 7),
    _ArtSummaryRsps1_Type()
)
artSummaryRsps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps1.setStatus("current")
_ArtSummaryRsps2_Type = Counter32
_ArtSummaryRsps2_Object = MibTableColumn
artSummaryRsps2 = _ArtSummaryRsps2_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 8),
    _ArtSummaryRsps2_Type()
)
artSummaryRsps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps2.setStatus("current")
_ArtSummaryRsps3_Type = Counter32
_ArtSummaryRsps3_Object = MibTableColumn
artSummaryRsps3 = _ArtSummaryRsps3_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 9),
    _ArtSummaryRsps3_Type()
)
artSummaryRsps3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps3.setStatus("current")
_ArtSummaryRsps4_Type = Counter32
_ArtSummaryRsps4_Object = MibTableColumn
artSummaryRsps4 = _ArtSummaryRsps4_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 10),
    _ArtSummaryRsps4_Type()
)
artSummaryRsps4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps4.setStatus("current")
_ArtSummaryRsps5_Type = Counter32
_ArtSummaryRsps5_Object = MibTableColumn
artSummaryRsps5 = _ArtSummaryRsps5_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 11),
    _ArtSummaryRsps5_Type()
)
artSummaryRsps5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps5.setStatus("current")
_ArtSummaryRsps6_Type = Counter32
_ArtSummaryRsps6_Object = MibTableColumn
artSummaryRsps6 = _ArtSummaryRsps6_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 12),
    _ArtSummaryRsps6_Type()
)
artSummaryRsps6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps6.setStatus("current")
_ArtSummaryRsps7_Type = Counter32
_ArtSummaryRsps7_Object = MibTableColumn
artSummaryRsps7 = _ArtSummaryRsps7_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 13),
    _ArtSummaryRsps7_Type()
)
artSummaryRsps7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRsps7.setStatus("current")
_ArtSummaryClientOctets_Type = Counter32
_ArtSummaryClientOctets_Object = MibTableColumn
artSummaryClientOctets = _ArtSummaryClientOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 14),
    _ArtSummaryClientOctets_Type()
)
artSummaryClientOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryClientOctets.setStatus("current")
_ArtSummaryClientOverflowOctets_Type = Counter32
_ArtSummaryClientOverflowOctets_Object = MibTableColumn
artSummaryClientOverflowOctets = _ArtSummaryClientOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 15),
    _ArtSummaryClientOverflowOctets_Type()
)
artSummaryClientOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryClientOverflowOctets.setStatus("current")
_ArtSummaryClientHCOctets_Type = Counter64
_ArtSummaryClientHCOctets_Object = MibTableColumn
artSummaryClientHCOctets = _ArtSummaryClientHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 16),
    _ArtSummaryClientHCOctets_Type()
)
artSummaryClientHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryClientHCOctets.setStatus("current")
_ArtSummaryServerOctets_Type = Counter32
_ArtSummaryServerOctets_Object = MibTableColumn
artSummaryServerOctets = _ArtSummaryServerOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 17),
    _ArtSummaryServerOctets_Type()
)
artSummaryServerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryServerOctets.setStatus("current")
_ArtSummaryServerOverflowOctets_Type = Counter32
_ArtSummaryServerOverflowOctets_Object = MibTableColumn
artSummaryServerOverflowOctets = _ArtSummaryServerOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 18),
    _ArtSummaryServerOverflowOctets_Type()
)
artSummaryServerOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryServerOverflowOctets.setStatus("current")
_ArtSummaryServerHCOctets_Type = Counter64
_ArtSummaryServerHCOctets_Object = MibTableColumn
artSummaryServerHCOctets = _ArtSummaryServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 19),
    _ArtSummaryServerHCOctets_Type()
)
artSummaryServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryServerHCOctets.setStatus("current")
_ArtSummaryRetries_Type = Counter32
_ArtSummaryRetries_Object = MibTableColumn
artSummaryRetries = _ArtSummaryRetries_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 20),
    _ArtSummaryRetries_Type()
)
artSummaryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryRetries.setStatus("current")
_ArtSummaryTimeouts_Type = Counter32
_ArtSummaryTimeouts_Object = MibTableColumn
artSummaryTimeouts = _ArtSummaryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 5, 1, 21),
    _ArtSummaryTimeouts_Type()
)
artSummaryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artSummaryTimeouts.setStatus("current")
protocolDirEntry.registerAugmentions(
    ("ART-MIB",
     "protocolDir2Entry")
)
protocolDir2Entry.setIndexNames(*protocolDirEntry.getIndexNames())

# Managed Objects groups

artGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 4, 2, 1)
)
artGroup.setObjects(
      *(("ART-MIB", "protocolDir2ArtConfig"),
        ("ART-MIB", "artControlDataSource"),
        ("ART-MIB", "artControlTimeRemaining"),
        ("ART-MIB", "artControlDuration"),
        ("ART-MIB", "artControlRspTime1"),
        ("ART-MIB", "artControlRspTime2"),
        ("ART-MIB", "artControlRspTime3"),
        ("ART-MIB", "artControlRspTime4"),
        ("ART-MIB", "artControlRspTime5"),
        ("ART-MIB", "artControlRspTime6"),
        ("ART-MIB", "artControlRspTimeout"),
        ("ART-MIB", "artControlRptStartTime"),
        ("ART-MIB", "artControlRequestedSize"),
        ("ART-MIB", "artControlGrantedSize"),
        ("ART-MIB", "artControlGeneratedRpts"),
        ("ART-MIB", "artControlDroppedFrames"),
        ("ART-MIB", "artControlOwner"),
        ("ART-MIB", "artControlStatus"),
        ("ART-MIB", "artAvgRspTime"),
        ("ART-MIB", "artMinRspTime"),
        ("ART-MIB", "artMaxRspTime"),
        ("ART-MIB", "artTotalResponses"),
        ("ART-MIB", "artRsps1"),
        ("ART-MIB", "artRsps2"),
        ("ART-MIB", "artRsps3"),
        ("ART-MIB", "artRsps4"),
        ("ART-MIB", "artRsps5"),
        ("ART-MIB", "artRsps6"),
        ("ART-MIB", "artRsps7"),
        ("ART-MIB", "artClientOctets"),
        ("ART-MIB", "artClientOverflowOctets"),
        ("ART-MIB", "artClientHCOctets"),
        ("ART-MIB", "artServerOctets"),
        ("ART-MIB", "artServerOverflowOctets"),
        ("ART-MIB", "artServerHCOctets"),
        ("ART-MIB", "artRetries"),
        ("ART-MIB", "artTimeouts"),
        ("ART-MIB", "artSummaryClients"),
        ("ART-MIB", "artSummaryAvgRspTime"),
        ("ART-MIB", "artSummaryMinRspTime"),
        ("ART-MIB", "artSummaryMaxRspTime"),
        ("ART-MIB", "artSummaryTotalResponses"),
        ("ART-MIB", "artSummaryRsps1"),
        ("ART-MIB", "artSummaryRsps2"),
        ("ART-MIB", "artSummaryRsps3"),
        ("ART-MIB", "artSummaryRsps4"),
        ("ART-MIB", "artSummaryRsps5"),
        ("ART-MIB", "artSummaryRsps6"),
        ("ART-MIB", "artSummaryRsps7"),
        ("ART-MIB", "artSummaryClientOctets"),
        ("ART-MIB", "artSummaryClientOverflowOctets"),
        ("ART-MIB", "artSummaryClientHCOctets"),
        ("ART-MIB", "artSummaryServerOctets"),
        ("ART-MIB", "artSummaryServerOverflowOctets"),
        ("ART-MIB", "artSummaryServerHCOctets"),
        ("ART-MIB", "artSummaryRetries"),
        ("ART-MIB", "artSummaryTimeouts"))
)
if mibBuilder.loadTexts:
    artGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

artMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    artMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ART-MIB",
    **{"frontier": frontier,
       "mibdoc2": mibdoc2,
       "netscout2": netscout2,
       "art": art,
       "protocolDir2Table": protocolDir2Table,
       "protocolDir2Entry": protocolDir2Entry,
       "protocolDir2ArtConfig": protocolDir2ArtConfig,
       "artControlTable": artControlTable,
       "artControlEntry": artControlEntry,
       "artControlIndex": artControlIndex,
       "artControlDataSource": artControlDataSource,
       "artControlTimeRemaining": artControlTimeRemaining,
       "artControlDuration": artControlDuration,
       "artControlRspTime1": artControlRspTime1,
       "artControlRspTime2": artControlRspTime2,
       "artControlRspTime3": artControlRspTime3,
       "artControlRspTime4": artControlRspTime4,
       "artControlRspTime5": artControlRspTime5,
       "artControlRspTime6": artControlRspTime6,
       "artControlRspTimeout": artControlRspTimeout,
       "artControlRptStartTime": artControlRptStartTime,
       "artControlRequestedSize": artControlRequestedSize,
       "artControlGrantedSize": artControlGrantedSize,
       "artControlGeneratedRpts": artControlGeneratedRpts,
       "artControlDroppedFrames": artControlDroppedFrames,
       "artControlOwner": artControlOwner,
       "artControlStatus": artControlStatus,
       "artTable": artTable,
       "artEntry": artEntry,
       "artServerAddress": artServerAddress,
       "artClientAddress": artClientAddress,
       "artAvgRspTime": artAvgRspTime,
       "artMinRspTime": artMinRspTime,
       "artMaxRspTime": artMaxRspTime,
       "artTotalResponses": artTotalResponses,
       "artRsps1": artRsps1,
       "artRsps2": artRsps2,
       "artRsps3": artRsps3,
       "artRsps4": artRsps4,
       "artRsps5": artRsps5,
       "artRsps6": artRsps6,
       "artRsps7": artRsps7,
       "artClientOctets": artClientOctets,
       "artClientOverflowOctets": artClientOverflowOctets,
       "artClientHCOctets": artClientHCOctets,
       "artServerOctets": artServerOctets,
       "artServerOverflowOctets": artServerOverflowOctets,
       "artServerHCOctets": artServerHCOctets,
       "artRetries": artRetries,
       "artTimeouts": artTimeouts,
       "artConformance": artConformance,
       "artMIBCompliances": artMIBCompliances,
       "artMIBCompliance": artMIBCompliance,
       "artMIBGroups": artMIBGroups,
       "artGroup": artGroup,
       "artSummaryTable": artSummaryTable,
       "artSummaryEntry": artSummaryEntry,
       "artSummaryServerAddress": artSummaryServerAddress,
       "artSummaryClients": artSummaryClients,
       "artSummaryAvgRspTime": artSummaryAvgRspTime,
       "artSummaryMinRspTime": artSummaryMinRspTime,
       "artSummaryMaxRspTime": artSummaryMaxRspTime,
       "artSummaryTotalResponses": artSummaryTotalResponses,
       "artSummaryRsps1": artSummaryRsps1,
       "artSummaryRsps2": artSummaryRsps2,
       "artSummaryRsps3": artSummaryRsps3,
       "artSummaryRsps4": artSummaryRsps4,
       "artSummaryRsps5": artSummaryRsps5,
       "artSummaryRsps6": artSummaryRsps6,
       "artSummaryRsps7": artSummaryRsps7,
       "artSummaryClientOctets": artSummaryClientOctets,
       "artSummaryClientOverflowOctets": artSummaryClientOverflowOctets,
       "artSummaryClientHCOctets": artSummaryClientHCOctets,
       "artSummaryServerOctets": artSummaryServerOctets,
       "artSummaryServerOverflowOctets": artSummaryServerOverflowOctets,
       "artSummaryServerHCOctets": artSummaryServerHCOctets,
       "artSummaryRetries": artSummaryRetries,
       "artSummaryTimeouts": artSummaryTimeouts}
)
