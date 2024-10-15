# SNMP MIB module (DSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:41 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(CounterBasedGauge64,
 ZeroBasedCounter64) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64",
    "ZeroBasedCounter64")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(DataSource,
 LastCreateTime,
 TimeFilter,
 ZeroBasedCounter32,
 protocolDirLocalIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "DataSource",
    "LastCreateTime",
    "TimeFilter",
    "ZeroBasedCounter32",
    "protocolDirLocalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dsmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26)
)
dsmonMIB.setRevisions(
        ("2002-05-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DsmonCounterAggGroupIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class DsmonCounterAggProfileIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_DsmonObjects_ObjectIdentity = ObjectIdentity
dsmonObjects = _DsmonObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1)
)
_DsmonAggObjects_ObjectIdentity = ObjectIdentity
dsmonAggObjects = _DsmonAggObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1)
)


class _DsmonMaxAggGroups_Type(Integer32):
    """Custom type dsmonMaxAggGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_DsmonMaxAggGroups_Type.__name__ = "Integer32"
_DsmonMaxAggGroups_Object = MibScalar
dsmonMaxAggGroups = _DsmonMaxAggGroups_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 1),
    _DsmonMaxAggGroups_Type()
)
dsmonMaxAggGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMaxAggGroups.setStatus("current")
_DsmonAggControlLocked_Type = TruthValue
_DsmonAggControlLocked_Object = MibScalar
dsmonAggControlLocked = _DsmonAggControlLocked_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 2),
    _DsmonAggControlLocked_Type()
)
dsmonAggControlLocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsmonAggControlLocked.setStatus("current")
_DsmonAggControlChanges_Type = Counter32
_DsmonAggControlChanges_Object = MibScalar
dsmonAggControlChanges = _DsmonAggControlChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 3),
    _DsmonAggControlChanges_Type()
)
dsmonAggControlChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonAggControlChanges.setStatus("current")
_DsmonAggControlLastChangeTime_Type = TimeStamp
_DsmonAggControlLastChangeTime_Object = MibScalar
dsmonAggControlLastChangeTime = _DsmonAggControlLastChangeTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 4),
    _DsmonAggControlLastChangeTime_Type()
)
dsmonAggControlLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonAggControlLastChangeTime.setStatus("current")
_DsmonAggControlTable_Object = MibTable
dsmonAggControlTable = _DsmonAggControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dsmonAggControlTable.setStatus("current")
_DsmonAggControlEntry_Object = MibTableRow
dsmonAggControlEntry = _DsmonAggControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5, 1)
)
dsmonAggControlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonAggControlIndex"),
)
if mibBuilder.loadTexts:
    dsmonAggControlEntry.setStatus("current")
_DsmonAggControlIndex_Type = DsmonCounterAggProfileIndex
_DsmonAggControlIndex_Object = MibTableColumn
dsmonAggControlIndex = _DsmonAggControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5, 1, 1),
    _DsmonAggControlIndex_Type()
)
dsmonAggControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonAggControlIndex.setStatus("current")


class _DsmonAggControlDescr_Type(SnmpAdminString):
    """Custom type dsmonAggControlDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DsmonAggControlDescr_Type.__name__ = "SnmpAdminString"
_DsmonAggControlDescr_Object = MibTableColumn
dsmonAggControlDescr = _DsmonAggControlDescr_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5, 1, 2),
    _DsmonAggControlDescr_Type()
)
dsmonAggControlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonAggControlDescr.setStatus("current")
_DsmonAggControlOwner_Type = OwnerString
_DsmonAggControlOwner_Object = MibTableColumn
dsmonAggControlOwner = _DsmonAggControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5, 1, 3),
    _DsmonAggControlOwner_Type()
)
dsmonAggControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonAggControlOwner.setStatus("current")
_DsmonAggControlStatus_Type = RowStatus
_DsmonAggControlStatus_Object = MibTableColumn
dsmonAggControlStatus = _DsmonAggControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 5, 1, 4),
    _DsmonAggControlStatus_Type()
)
dsmonAggControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonAggControlStatus.setStatus("current")
_DsmonAggProfileTable_Object = MibTable
dsmonAggProfileTable = _DsmonAggProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dsmonAggProfileTable.setStatus("current")
_DsmonAggProfileEntry_Object = MibTableRow
dsmonAggProfileEntry = _DsmonAggProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 6, 1)
)
dsmonAggProfileEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonAggControlIndex"),
    (0, "DSMON-MIB", "dsmonAggProfileDSCP"),
)
if mibBuilder.loadTexts:
    dsmonAggProfileEntry.setStatus("current")
_DsmonAggProfileDSCP_Type = Dscp
_DsmonAggProfileDSCP_Object = MibTableColumn
dsmonAggProfileDSCP = _DsmonAggProfileDSCP_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 6, 1, 1),
    _DsmonAggProfileDSCP_Type()
)
dsmonAggProfileDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonAggProfileDSCP.setStatus("current")


class _DsmonAggGroupIndex_Type(DsmonCounterAggGroupIndex):
    """Custom type dsmonAggGroupIndex based on DsmonCounterAggGroupIndex"""
    defaultValue = 0


_DsmonAggGroupIndex_Object = MibTableColumn
dsmonAggGroupIndex = _DsmonAggGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 6, 1, 2),
    _DsmonAggGroupIndex_Type()
)
dsmonAggGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsmonAggGroupIndex.setStatus("current")
_DsmonAggGroupTable_Object = MibTable
dsmonAggGroupTable = _DsmonAggGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dsmonAggGroupTable.setStatus("current")
_DsmonAggGroupEntry_Object = MibTableRow
dsmonAggGroupEntry = _DsmonAggGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 7, 1)
)
dsmonAggGroupEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonAggControlIndex"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
)
if mibBuilder.loadTexts:
    dsmonAggGroupEntry.setStatus("current")


class _DsmonAggGroupDescr_Type(SnmpAdminString):
    """Custom type dsmonAggGroupDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DsmonAggGroupDescr_Type.__name__ = "SnmpAdminString"
_DsmonAggGroupDescr_Object = MibTableColumn
dsmonAggGroupDescr = _DsmonAggGroupDescr_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 7, 1, 1),
    _DsmonAggGroupDescr_Type()
)
dsmonAggGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonAggGroupDescr.setStatus("current")
_DsmonAggGroupStatus_Type = RowStatus
_DsmonAggGroupStatus_Object = MibTableColumn
dsmonAggGroupStatus = _DsmonAggGroupStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 1, 7, 1, 2),
    _DsmonAggGroupStatus_Type()
)
dsmonAggGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonAggGroupStatus.setStatus("current")
_DsmonStatsObjects_ObjectIdentity = ObjectIdentity
dsmonStatsObjects = _DsmonStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2)
)
_DsmonStatsControlTable_Object = MibTable
dsmonStatsControlTable = _DsmonStatsControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsmonStatsControlTable.setStatus("current")
_DsmonStatsControlEntry_Object = MibTableRow
dsmonStatsControlEntry = _DsmonStatsControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1)
)
dsmonStatsControlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonStatsControlIndex"),
)
if mibBuilder.loadTexts:
    dsmonStatsControlEntry.setStatus("current")


class _DsmonStatsControlIndex_Type(Integer32):
    """Custom type dsmonStatsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonStatsControlIndex_Type.__name__ = "Integer32"
_DsmonStatsControlIndex_Object = MibTableColumn
dsmonStatsControlIndex = _DsmonStatsControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 1),
    _DsmonStatsControlIndex_Type()
)
dsmonStatsControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonStatsControlIndex.setStatus("current")
_DsmonStatsControlDataSource_Type = DataSource
_DsmonStatsControlDataSource_Object = MibTableColumn
dsmonStatsControlDataSource = _DsmonStatsControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 2),
    _DsmonStatsControlDataSource_Type()
)
dsmonStatsControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonStatsControlDataSource.setStatus("current")
_DsmonStatsControlAggProfile_Type = DsmonCounterAggProfileIndex
_DsmonStatsControlAggProfile_Object = MibTableColumn
dsmonStatsControlAggProfile = _DsmonStatsControlAggProfile_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 3),
    _DsmonStatsControlAggProfile_Type()
)
dsmonStatsControlAggProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonStatsControlAggProfile.setStatus("current")
_DsmonStatsControlDroppedFrames_Type = Counter32
_DsmonStatsControlDroppedFrames_Object = MibTableColumn
dsmonStatsControlDroppedFrames = _DsmonStatsControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 4),
    _DsmonStatsControlDroppedFrames_Type()
)
dsmonStatsControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsControlDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsControlDroppedFrames.setUnits("frames")
_DsmonStatsControlCreateTime_Type = LastCreateTime
_DsmonStatsControlCreateTime_Object = MibTableColumn
dsmonStatsControlCreateTime = _DsmonStatsControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 5),
    _DsmonStatsControlCreateTime_Type()
)
dsmonStatsControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsControlCreateTime.setStatus("current")
_DsmonStatsControlOwner_Type = OwnerString
_DsmonStatsControlOwner_Object = MibTableColumn
dsmonStatsControlOwner = _DsmonStatsControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 6),
    _DsmonStatsControlOwner_Type()
)
dsmonStatsControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonStatsControlOwner.setStatus("current")
_DsmonStatsControlStatus_Type = RowStatus
_DsmonStatsControlStatus_Object = MibTableColumn
dsmonStatsControlStatus = _DsmonStatsControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 1, 1, 7),
    _DsmonStatsControlStatus_Type()
)
dsmonStatsControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonStatsControlStatus.setStatus("current")
_DsmonStatsTable_Object = MibTable
dsmonStatsTable = _DsmonStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dsmonStatsTable.setStatus("current")
_DsmonStatsEntry_Object = MibTableRow
dsmonStatsEntry = _DsmonStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1)
)
dsmonStatsEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonStatsControlIndex"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
)
if mibBuilder.loadTexts:
    dsmonStatsEntry.setStatus("current")
_DsmonStatsInPkts_Type = ZeroBasedCounter32
_DsmonStatsInPkts_Object = MibTableColumn
dsmonStatsInPkts = _DsmonStatsInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 1),
    _DsmonStatsInPkts_Type()
)
dsmonStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsInPkts.setUnits("packets")
_DsmonStatsInOctets_Type = ZeroBasedCounter32
_DsmonStatsInOctets_Object = MibTableColumn
dsmonStatsInOctets = _DsmonStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 2),
    _DsmonStatsInOctets_Type()
)
dsmonStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsInOctets.setUnits("octets")
_DsmonStatsInOvflPkts_Type = ZeroBasedCounter32
_DsmonStatsInOvflPkts_Object = MibTableColumn
dsmonStatsInOvflPkts = _DsmonStatsInOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 3),
    _DsmonStatsInOvflPkts_Type()
)
dsmonStatsInOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInOvflPkts.setStatus("deprecated")
_DsmonStatsInOvflOctets_Type = ZeroBasedCounter32
_DsmonStatsInOvflOctets_Object = MibTableColumn
dsmonStatsInOvflOctets = _DsmonStatsInOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 4),
    _DsmonStatsInOvflOctets_Type()
)
dsmonStatsInOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInOvflOctets.setStatus("deprecated")
_DsmonStatsInHCPkts_Type = ZeroBasedCounter64
_DsmonStatsInHCPkts_Object = MibTableColumn
dsmonStatsInHCPkts = _DsmonStatsInHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 5),
    _DsmonStatsInHCPkts_Type()
)
dsmonStatsInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsInHCPkts.setUnits("packets")
_DsmonStatsInHCOctets_Type = ZeroBasedCounter64
_DsmonStatsInHCOctets_Object = MibTableColumn
dsmonStatsInHCOctets = _DsmonStatsInHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 6),
    _DsmonStatsInHCOctets_Type()
)
dsmonStatsInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsInHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsInHCOctets.setUnits("octets")
_DsmonStatsOutPkts_Type = ZeroBasedCounter32
_DsmonStatsOutPkts_Object = MibTableColumn
dsmonStatsOutPkts = _DsmonStatsOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 7),
    _DsmonStatsOutPkts_Type()
)
dsmonStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsOutPkts.setUnits("packets")
_DsmonStatsOutOctets_Type = ZeroBasedCounter32
_DsmonStatsOutOctets_Object = MibTableColumn
dsmonStatsOutOctets = _DsmonStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 8),
    _DsmonStatsOutOctets_Type()
)
dsmonStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsOutOctets.setUnits("octets")
_DsmonStatsOutOvflPkts_Type = ZeroBasedCounter32
_DsmonStatsOutOvflPkts_Object = MibTableColumn
dsmonStatsOutOvflPkts = _DsmonStatsOutOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 9),
    _DsmonStatsOutOvflPkts_Type()
)
dsmonStatsOutOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutOvflPkts.setStatus("deprecated")
_DsmonStatsOutOvflOctets_Type = ZeroBasedCounter32
_DsmonStatsOutOvflOctets_Object = MibTableColumn
dsmonStatsOutOvflOctets = _DsmonStatsOutOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 10),
    _DsmonStatsOutOvflOctets_Type()
)
dsmonStatsOutOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutOvflOctets.setStatus("deprecated")
_DsmonStatsOutHCPkts_Type = ZeroBasedCounter64
_DsmonStatsOutHCPkts_Object = MibTableColumn
dsmonStatsOutHCPkts = _DsmonStatsOutHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 11),
    _DsmonStatsOutHCPkts_Type()
)
dsmonStatsOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsOutHCPkts.setUnits("packets")
_DsmonStatsOutHCOctets_Type = ZeroBasedCounter64
_DsmonStatsOutHCOctets_Object = MibTableColumn
dsmonStatsOutHCOctets = _DsmonStatsOutHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 2, 2, 1, 12),
    _DsmonStatsOutHCOctets_Type()
)
dsmonStatsOutHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonStatsOutHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonStatsOutHCOctets.setUnits("octets")
_DsmonPdistObjects_ObjectIdentity = ObjectIdentity
dsmonPdistObjects = _DsmonPdistObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3)
)
_DsmonPdistCtlTable_Object = MibTable
dsmonPdistCtlTable = _DsmonPdistCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsmonPdistCtlTable.setStatus("current")
_DsmonPdistCtlEntry_Object = MibTableRow
dsmonPdistCtlEntry = _DsmonPdistCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1)
)
dsmonPdistCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonPdistCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonPdistCtlEntry.setStatus("current")


class _DsmonPdistCtlIndex_Type(Integer32):
    """Custom type dsmonPdistCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonPdistCtlIndex_Type.__name__ = "Integer32"
_DsmonPdistCtlIndex_Object = MibTableColumn
dsmonPdistCtlIndex = _DsmonPdistCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 1),
    _DsmonPdistCtlIndex_Type()
)
dsmonPdistCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonPdistCtlIndex.setStatus("current")
_DsmonPdistCtlDataSource_Type = DataSource
_DsmonPdistCtlDataSource_Object = MibTableColumn
dsmonPdistCtlDataSource = _DsmonPdistCtlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 2),
    _DsmonPdistCtlDataSource_Type()
)
dsmonPdistCtlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistCtlDataSource.setStatus("current")
_DsmonPdistCtlAggProfile_Type = DsmonCounterAggProfileIndex
_DsmonPdistCtlAggProfile_Object = MibTableColumn
dsmonPdistCtlAggProfile = _DsmonPdistCtlAggProfile_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 3),
    _DsmonPdistCtlAggProfile_Type()
)
dsmonPdistCtlAggProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistCtlAggProfile.setStatus("current")


class _DsmonPdistCtlMaxDesiredEntries_Type(Integer32):
    """Custom type dsmonPdistCtlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonPdistCtlMaxDesiredEntries_Type.__name__ = "Integer32"
_DsmonPdistCtlMaxDesiredEntries_Object = MibTableColumn
dsmonPdistCtlMaxDesiredEntries = _DsmonPdistCtlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 4),
    _DsmonPdistCtlMaxDesiredEntries_Type()
)
dsmonPdistCtlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistCtlMaxDesiredEntries.setStatus("current")
_DsmonPdistCtlDroppedFrames_Type = Counter32
_DsmonPdistCtlDroppedFrames_Object = MibTableColumn
dsmonPdistCtlDroppedFrames = _DsmonPdistCtlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 5),
    _DsmonPdistCtlDroppedFrames_Type()
)
dsmonPdistCtlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistCtlDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistCtlDroppedFrames.setUnits("frames")
_DsmonPdistCtlInserts_Type = Counter32
_DsmonPdistCtlInserts_Object = MibTableColumn
dsmonPdistCtlInserts = _DsmonPdistCtlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 6),
    _DsmonPdistCtlInserts_Type()
)
dsmonPdistCtlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistCtlInserts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistCtlInserts.setUnits("table entries")
_DsmonPdistCtlDeletes_Type = Counter32
_DsmonPdistCtlDeletes_Object = MibTableColumn
dsmonPdistCtlDeletes = _DsmonPdistCtlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 7),
    _DsmonPdistCtlDeletes_Type()
)
dsmonPdistCtlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistCtlDeletes.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistCtlDeletes.setUnits("table entries")
_DsmonPdistCtlCreateTime_Type = LastCreateTime
_DsmonPdistCtlCreateTime_Object = MibTableColumn
dsmonPdistCtlCreateTime = _DsmonPdistCtlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 8),
    _DsmonPdistCtlCreateTime_Type()
)
dsmonPdistCtlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistCtlCreateTime.setStatus("current")
_DsmonPdistCtlOwner_Type = OwnerString
_DsmonPdistCtlOwner_Object = MibTableColumn
dsmonPdistCtlOwner = _DsmonPdistCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 9),
    _DsmonPdistCtlOwner_Type()
)
dsmonPdistCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistCtlOwner.setStatus("current")
_DsmonPdistCtlStatus_Type = RowStatus
_DsmonPdistCtlStatus_Object = MibTableColumn
dsmonPdistCtlStatus = _DsmonPdistCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 1, 1, 10),
    _DsmonPdistCtlStatus_Type()
)
dsmonPdistCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistCtlStatus.setStatus("current")
_DsmonPdistStatsTable_Object = MibTable
dsmonPdistStatsTable = _DsmonPdistStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dsmonPdistStatsTable.setStatus("current")
_DsmonPdistStatsEntry_Object = MibTableRow
dsmonPdistStatsEntry = _DsmonPdistStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1)
)
dsmonPdistStatsEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonPdistCtlIndex"),
    (0, "DSMON-MIB", "dsmonPdistTimeMark"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    dsmonPdistStatsEntry.setStatus("current")
_DsmonPdistTimeMark_Type = TimeFilter
_DsmonPdistTimeMark_Object = MibTableColumn
dsmonPdistTimeMark = _DsmonPdistTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 1),
    _DsmonPdistTimeMark_Type()
)
dsmonPdistTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonPdistTimeMark.setStatus("current")
_DsmonPdistStatsPkts_Type = ZeroBasedCounter32
_DsmonPdistStatsPkts_Object = MibTableColumn
dsmonPdistStatsPkts = _DsmonPdistStatsPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 2),
    _DsmonPdistStatsPkts_Type()
)
dsmonPdistStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistStatsPkts.setUnits("packets")
_DsmonPdistStatsOctets_Type = ZeroBasedCounter32
_DsmonPdistStatsOctets_Object = MibTableColumn
dsmonPdistStatsOctets = _DsmonPdistStatsOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 3),
    _DsmonPdistStatsOctets_Type()
)
dsmonPdistStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistStatsOctets.setUnits("octets")
_DsmonPdistStatsOvflPkts_Type = ZeroBasedCounter32
_DsmonPdistStatsOvflPkts_Object = MibTableColumn
dsmonPdistStatsOvflPkts = _DsmonPdistStatsOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 4),
    _DsmonPdistStatsOvflPkts_Type()
)
dsmonPdistStatsOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsOvflPkts.setStatus("deprecated")
_DsmonPdistStatsOvflOctets_Type = ZeroBasedCounter32
_DsmonPdistStatsOvflOctets_Object = MibTableColumn
dsmonPdistStatsOvflOctets = _DsmonPdistStatsOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 5),
    _DsmonPdistStatsOvflOctets_Type()
)
dsmonPdistStatsOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsOvflOctets.setStatus("deprecated")
_DsmonPdistStatsHCPkts_Type = ZeroBasedCounter64
_DsmonPdistStatsHCPkts_Object = MibTableColumn
dsmonPdistStatsHCPkts = _DsmonPdistStatsHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 6),
    _DsmonPdistStatsHCPkts_Type()
)
dsmonPdistStatsHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistStatsHCPkts.setUnits("packets")
_DsmonPdistStatsHCOctets_Type = ZeroBasedCounter64
_DsmonPdistStatsHCOctets_Object = MibTableColumn
dsmonPdistStatsHCOctets = _DsmonPdistStatsHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 7),
    _DsmonPdistStatsHCOctets_Type()
)
dsmonPdistStatsHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistStatsHCOctets.setUnits("octets")
_DsmonPdistStatsCreateTime_Type = LastCreateTime
_DsmonPdistStatsCreateTime_Object = MibTableColumn
dsmonPdistStatsCreateTime = _DsmonPdistStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 2, 1, 8),
    _DsmonPdistStatsCreateTime_Type()
)
dsmonPdistStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistStatsCreateTime.setStatus("current")
_DsmonPdistTopNCtlTable_Object = MibTable
dsmonPdistTopNCtlTable = _DsmonPdistTopNCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlTable.setStatus("current")
_DsmonPdistTopNCtlEntry_Object = MibTableRow
dsmonPdistTopNCtlEntry = _DsmonPdistTopNCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1)
)
dsmonPdistTopNCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonPdistTopNCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlEntry.setStatus("current")


class _DsmonPdistTopNCtlIndex_Type(Integer32):
    """Custom type dsmonPdistTopNCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonPdistTopNCtlIndex_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlIndex_Object = MibTableColumn
dsmonPdistTopNCtlIndex = _DsmonPdistTopNCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 1),
    _DsmonPdistTopNCtlIndex_Type()
)
dsmonPdistTopNCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlIndex.setStatus("current")


class _DsmonPdistTopNCtlPdistIndex_Type(Integer32):
    """Custom type dsmonPdistTopNCtlPdistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonPdistTopNCtlPdistIndex_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlPdistIndex_Object = MibTableColumn
dsmonPdistTopNCtlPdistIndex = _DsmonPdistTopNCtlPdistIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 2),
    _DsmonPdistTopNCtlPdistIndex_Type()
)
dsmonPdistTopNCtlPdistIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlPdistIndex.setStatus("current")


class _DsmonPdistTopNCtlRateBase_Type(Integer32):
    """Custom type dsmonPdistTopNCtlRateBase based on Integer32"""
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
        *(("dsmonPdistTopNHCOctets", 4),
          ("dsmonPdistTopNHCPkts", 3),
          ("dsmonPdistTopNOctets", 2),
          ("dsmonPdistTopNPkts", 1))
    )


_DsmonPdistTopNCtlRateBase_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlRateBase_Object = MibTableColumn
dsmonPdistTopNCtlRateBase = _DsmonPdistTopNCtlRateBase_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 3),
    _DsmonPdistTopNCtlRateBase_Type()
)
dsmonPdistTopNCtlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlRateBase.setStatus("current")


class _DsmonPdistTopNCtlTimeRemaining_Type(Integer32):
    """Custom type dsmonPdistTopNCtlTimeRemaining based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonPdistTopNCtlTimeRemaining_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlTimeRemaining_Object = MibTableColumn
dsmonPdistTopNCtlTimeRemaining = _DsmonPdistTopNCtlTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 4),
    _DsmonPdistTopNCtlTimeRemaining_Type()
)
dsmonPdistTopNCtlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlTimeRemaining.setUnits("seconds")
_DsmonPdistTopNCtlGeneratedReprts_Type = Counter32
_DsmonPdistTopNCtlGeneratedReprts_Object = MibTableColumn
dsmonPdistTopNCtlGeneratedReprts = _DsmonPdistTopNCtlGeneratedReprts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 5),
    _DsmonPdistTopNCtlGeneratedReprts_Type()
)
dsmonPdistTopNCtlGeneratedReprts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlGeneratedReprts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlGeneratedReprts.setUnits("reports")


class _DsmonPdistTopNCtlDuration_Type(Integer32):
    """Custom type dsmonPdistTopNCtlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonPdistTopNCtlDuration_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlDuration_Object = MibTableColumn
dsmonPdistTopNCtlDuration = _DsmonPdistTopNCtlDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 6),
    _DsmonPdistTopNCtlDuration_Type()
)
dsmonPdistTopNCtlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlDuration.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlDuration.setUnits("seconds")


class _DsmonPdistTopNCtlRequestedSize_Type(Integer32):
    """Custom type dsmonPdistTopNCtlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonPdistTopNCtlRequestedSize_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlRequestedSize_Object = MibTableColumn
dsmonPdistTopNCtlRequestedSize = _DsmonPdistTopNCtlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 7),
    _DsmonPdistTopNCtlRequestedSize_Type()
)
dsmonPdistTopNCtlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlRequestedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlRequestedSize.setUnits("table entries")


class _DsmonPdistTopNCtlGrantedSize_Type(Integer32):
    """Custom type dsmonPdistTopNCtlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonPdistTopNCtlGrantedSize_Type.__name__ = "Integer32"
_DsmonPdistTopNCtlGrantedSize_Object = MibTableColumn
dsmonPdistTopNCtlGrantedSize = _DsmonPdistTopNCtlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 8),
    _DsmonPdistTopNCtlGrantedSize_Type()
)
dsmonPdistTopNCtlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlGrantedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlGrantedSize.setUnits("table entries")
_DsmonPdistTopNCtlStartTime_Type = TimeStamp
_DsmonPdistTopNCtlStartTime_Object = MibTableColumn
dsmonPdistTopNCtlStartTime = _DsmonPdistTopNCtlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 9),
    _DsmonPdistTopNCtlStartTime_Type()
)
dsmonPdistTopNCtlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlStartTime.setStatus("current")
_DsmonPdistTopNCtlOwner_Type = OwnerString
_DsmonPdistTopNCtlOwner_Object = MibTableColumn
dsmonPdistTopNCtlOwner = _DsmonPdistTopNCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 10),
    _DsmonPdistTopNCtlOwner_Type()
)
dsmonPdistTopNCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlOwner.setStatus("current")
_DsmonPdistTopNCtlStatus_Type = RowStatus
_DsmonPdistTopNCtlStatus_Object = MibTableColumn
dsmonPdistTopNCtlStatus = _DsmonPdistTopNCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 3, 1, 11),
    _DsmonPdistTopNCtlStatus_Type()
)
dsmonPdistTopNCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonPdistTopNCtlStatus.setStatus("current")
_DsmonPdistTopNTable_Object = MibTable
dsmonPdistTopNTable = _DsmonPdistTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dsmonPdistTopNTable.setStatus("current")
_DsmonPdistTopNEntry_Object = MibTableRow
dsmonPdistTopNEntry = _DsmonPdistTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1)
)
dsmonPdistTopNEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonPdistTopNCtlIndex"),
    (0, "DSMON-MIB", "dsmonPdistTopNIndex"),
)
if mibBuilder.loadTexts:
    dsmonPdistTopNEntry.setStatus("current")


class _DsmonPdistTopNIndex_Type(Integer32):
    """Custom type dsmonPdistTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonPdistTopNIndex_Type.__name__ = "Integer32"
_DsmonPdistTopNIndex_Object = MibTableColumn
dsmonPdistTopNIndex = _DsmonPdistTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 1),
    _DsmonPdistTopNIndex_Type()
)
dsmonPdistTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonPdistTopNIndex.setStatus("current")


class _DsmonPdistTopNPDLocalIndex_Type(Integer32):
    """Custom type dsmonPdistTopNPDLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonPdistTopNPDLocalIndex_Type.__name__ = "Integer32"
_DsmonPdistTopNPDLocalIndex_Object = MibTableColumn
dsmonPdistTopNPDLocalIndex = _DsmonPdistTopNPDLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 2),
    _DsmonPdistTopNPDLocalIndex_Type()
)
dsmonPdistTopNPDLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNPDLocalIndex.setStatus("current")
_DsmonPdistTopNAggGroup_Type = DsmonCounterAggGroupIndex
_DsmonPdistTopNAggGroup_Object = MibTableColumn
dsmonPdistTopNAggGroup = _DsmonPdistTopNAggGroup_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 3),
    _DsmonPdistTopNAggGroup_Type()
)
dsmonPdistTopNAggGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNAggGroup.setStatus("current")
_DsmonPdistTopNRate_Type = Gauge32
_DsmonPdistTopNRate_Object = MibTableColumn
dsmonPdistTopNRate = _DsmonPdistTopNRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 4),
    _DsmonPdistTopNRate_Type()
)
dsmonPdistTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNRate.setStatus("current")
_DsmonPdistTopNRateOvfl_Type = Gauge32
_DsmonPdistTopNRateOvfl_Object = MibTableColumn
dsmonPdistTopNRateOvfl = _DsmonPdistTopNRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 5),
    _DsmonPdistTopNRateOvfl_Type()
)
dsmonPdistTopNRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNRateOvfl.setStatus("deprecated")
_DsmonPdistTopNHCRate_Type = CounterBasedGauge64
_DsmonPdistTopNHCRate_Object = MibTableColumn
dsmonPdistTopNHCRate = _DsmonPdistTopNHCRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 3, 4, 1, 6),
    _DsmonPdistTopNHCRate_Type()
)
dsmonPdistTopNHCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonPdistTopNHCRate.setStatus("current")
_DsmonHostObjects_ObjectIdentity = ObjectIdentity
dsmonHostObjects = _DsmonHostObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4)
)
_DsmonHostCtlTable_Object = MibTable
dsmonHostCtlTable = _DsmonHostCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsmonHostCtlTable.setStatus("current")
_DsmonHostCtlEntry_Object = MibTableRow
dsmonHostCtlEntry = _DsmonHostCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1)
)
dsmonHostCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonHostCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonHostCtlEntry.setStatus("current")


class _DsmonHostCtlIndex_Type(Integer32):
    """Custom type dsmonHostCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonHostCtlIndex_Type.__name__ = "Integer32"
_DsmonHostCtlIndex_Object = MibTableColumn
dsmonHostCtlIndex = _DsmonHostCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 1),
    _DsmonHostCtlIndex_Type()
)
dsmonHostCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonHostCtlIndex.setStatus("current")
_DsmonHostCtlDataSource_Type = DataSource
_DsmonHostCtlDataSource_Object = MibTableColumn
dsmonHostCtlDataSource = _DsmonHostCtlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 2),
    _DsmonHostCtlDataSource_Type()
)
dsmonHostCtlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlDataSource.setStatus("current")
_DsmonHostCtlAggProfile_Type = DsmonCounterAggProfileIndex
_DsmonHostCtlAggProfile_Object = MibTableColumn
dsmonHostCtlAggProfile = _DsmonHostCtlAggProfile_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 3),
    _DsmonHostCtlAggProfile_Type()
)
dsmonHostCtlAggProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlAggProfile.setStatus("current")


class _DsmonHostCtlMaxDesiredEntries_Type(Integer32):
    """Custom type dsmonHostCtlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonHostCtlMaxDesiredEntries_Type.__name__ = "Integer32"
_DsmonHostCtlMaxDesiredEntries_Object = MibTableColumn
dsmonHostCtlMaxDesiredEntries = _DsmonHostCtlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 4),
    _DsmonHostCtlMaxDesiredEntries_Type()
)
dsmonHostCtlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlMaxDesiredEntries.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlMaxDesiredEntries.setUnits("table entries")


class _DsmonHostCtlIPv4PrefixLen_Type(Integer32):
    """Custom type dsmonHostCtlIPv4PrefixLen based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_DsmonHostCtlIPv4PrefixLen_Type.__name__ = "Integer32"
_DsmonHostCtlIPv4PrefixLen_Object = MibTableColumn
dsmonHostCtlIPv4PrefixLen = _DsmonHostCtlIPv4PrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 5),
    _DsmonHostCtlIPv4PrefixLen_Type()
)
dsmonHostCtlIPv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlIPv4PrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlIPv4PrefixLen.setUnits("bits")


class _DsmonHostCtlIPv6PrefixLen_Type(Integer32):
    """Custom type dsmonHostCtlIPv6PrefixLen based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_DsmonHostCtlIPv6PrefixLen_Type.__name__ = "Integer32"
_DsmonHostCtlIPv6PrefixLen_Object = MibTableColumn
dsmonHostCtlIPv6PrefixLen = _DsmonHostCtlIPv6PrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 6),
    _DsmonHostCtlIPv6PrefixLen_Type()
)
dsmonHostCtlIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlIPv6PrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlIPv6PrefixLen.setUnits("bits")
_DsmonHostCtlDroppedFrames_Type = Counter32
_DsmonHostCtlDroppedFrames_Object = MibTableColumn
dsmonHostCtlDroppedFrames = _DsmonHostCtlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 7),
    _DsmonHostCtlDroppedFrames_Type()
)
dsmonHostCtlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostCtlDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlDroppedFrames.setUnits("frames")
_DsmonHostCtlInserts_Type = Counter32
_DsmonHostCtlInserts_Object = MibTableColumn
dsmonHostCtlInserts = _DsmonHostCtlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 8),
    _DsmonHostCtlInserts_Type()
)
dsmonHostCtlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostCtlInserts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlInserts.setUnits("table entries")
_DsmonHostCtlDeletes_Type = Counter32
_DsmonHostCtlDeletes_Object = MibTableColumn
dsmonHostCtlDeletes = _DsmonHostCtlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 9),
    _DsmonHostCtlDeletes_Type()
)
dsmonHostCtlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostCtlDeletes.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostCtlDeletes.setUnits("table entries")
_DsmonHostCtlCreateTime_Type = LastCreateTime
_DsmonHostCtlCreateTime_Object = MibTableColumn
dsmonHostCtlCreateTime = _DsmonHostCtlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 10),
    _DsmonHostCtlCreateTime_Type()
)
dsmonHostCtlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostCtlCreateTime.setStatus("current")
_DsmonHostCtlOwner_Type = OwnerString
_DsmonHostCtlOwner_Object = MibTableColumn
dsmonHostCtlOwner = _DsmonHostCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 11),
    _DsmonHostCtlOwner_Type()
)
dsmonHostCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlOwner.setStatus("current")
_DsmonHostCtlStatus_Type = RowStatus
_DsmonHostCtlStatus_Object = MibTableColumn
dsmonHostCtlStatus = _DsmonHostCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 1, 1, 12),
    _DsmonHostCtlStatus_Type()
)
dsmonHostCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostCtlStatus.setStatus("current")
_DsmonHostTable_Object = MibTable
dsmonHostTable = _DsmonHostTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dsmonHostTable.setStatus("current")
_DsmonHostEntry_Object = MibTableRow
dsmonHostEntry = _DsmonHostEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1)
)
dsmonHostEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonHostCtlIndex"),
    (0, "DSMON-MIB", "dsmonHostTimeMark"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "DSMON-MIB", "dsmonHostAddress"),
)
if mibBuilder.loadTexts:
    dsmonHostEntry.setStatus("current")
_DsmonHostTimeMark_Type = TimeFilter
_DsmonHostTimeMark_Object = MibTableColumn
dsmonHostTimeMark = _DsmonHostTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 1),
    _DsmonHostTimeMark_Type()
)
dsmonHostTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonHostTimeMark.setStatus("current")


class _DsmonHostAddress_Type(OctetString):
    """Custom type dsmonHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 110),
    )


_DsmonHostAddress_Type.__name__ = "OctetString"
_DsmonHostAddress_Object = MibTableColumn
dsmonHostAddress = _DsmonHostAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 2),
    _DsmonHostAddress_Type()
)
dsmonHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonHostAddress.setStatus("current")
_DsmonHostInPkts_Type = ZeroBasedCounter32
_DsmonHostInPkts_Object = MibTableColumn
dsmonHostInPkts = _DsmonHostInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 3),
    _DsmonHostInPkts_Type()
)
dsmonHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostInPkts.setUnits("packets")
_DsmonHostInOctets_Type = ZeroBasedCounter32
_DsmonHostInOctets_Object = MibTableColumn
dsmonHostInOctets = _DsmonHostInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 4),
    _DsmonHostInOctets_Type()
)
dsmonHostInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostInOctets.setUnits("octets")
_DsmonHostInOvflPkts_Type = ZeroBasedCounter32
_DsmonHostInOvflPkts_Object = MibTableColumn
dsmonHostInOvflPkts = _DsmonHostInOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 5),
    _DsmonHostInOvflPkts_Type()
)
dsmonHostInOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInOvflPkts.setStatus("deprecated")
_DsmonHostInOvflOctets_Type = ZeroBasedCounter32
_DsmonHostInOvflOctets_Object = MibTableColumn
dsmonHostInOvflOctets = _DsmonHostInOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 6),
    _DsmonHostInOvflOctets_Type()
)
dsmonHostInOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInOvflOctets.setStatus("deprecated")
_DsmonHostInHCPkts_Type = ZeroBasedCounter64
_DsmonHostInHCPkts_Object = MibTableColumn
dsmonHostInHCPkts = _DsmonHostInHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 7),
    _DsmonHostInHCPkts_Type()
)
dsmonHostInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostInHCPkts.setUnits("packets")
_DsmonHostInHCOctets_Type = ZeroBasedCounter64
_DsmonHostInHCOctets_Object = MibTableColumn
dsmonHostInHCOctets = _DsmonHostInHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 8),
    _DsmonHostInHCOctets_Type()
)
dsmonHostInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostInHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostInHCOctets.setUnits("octets")
_DsmonHostOutPkts_Type = ZeroBasedCounter32
_DsmonHostOutPkts_Object = MibTableColumn
dsmonHostOutPkts = _DsmonHostOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 9),
    _DsmonHostOutPkts_Type()
)
dsmonHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostOutPkts.setUnits("packets")
_DsmonHostOutOctets_Type = ZeroBasedCounter32
_DsmonHostOutOctets_Object = MibTableColumn
dsmonHostOutOctets = _DsmonHostOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 10),
    _DsmonHostOutOctets_Type()
)
dsmonHostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostOutOctets.setUnits("octets")
_DsmonHostOutOvflPkts_Type = ZeroBasedCounter32
_DsmonHostOutOvflPkts_Object = MibTableColumn
dsmonHostOutOvflPkts = _DsmonHostOutOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 11),
    _DsmonHostOutOvflPkts_Type()
)
dsmonHostOutOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutOvflPkts.setStatus("deprecated")
_DsmonHostOutOvflOctets_Type = ZeroBasedCounter32
_DsmonHostOutOvflOctets_Object = MibTableColumn
dsmonHostOutOvflOctets = _DsmonHostOutOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 12),
    _DsmonHostOutOvflOctets_Type()
)
dsmonHostOutOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutOvflOctets.setStatus("deprecated")
_DsmonHostOutHCPkts_Type = ZeroBasedCounter64
_DsmonHostOutHCPkts_Object = MibTableColumn
dsmonHostOutHCPkts = _DsmonHostOutHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 13),
    _DsmonHostOutHCPkts_Type()
)
dsmonHostOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostOutHCPkts.setUnits("packets")
_DsmonHostOutHCOctets_Type = ZeroBasedCounter64
_DsmonHostOutHCOctets_Object = MibTableColumn
dsmonHostOutHCOctets = _DsmonHostOutHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 14),
    _DsmonHostOutHCOctets_Type()
)
dsmonHostOutHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostOutHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostOutHCOctets.setUnits("octets")
_DsmonHostCreateTime_Type = LastCreateTime
_DsmonHostCreateTime_Object = MibTableColumn
dsmonHostCreateTime = _DsmonHostCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 2, 1, 15),
    _DsmonHostCreateTime_Type()
)
dsmonHostCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostCreateTime.setStatus("current")
_DsmonHostTopNCtlTable_Object = MibTable
dsmonHostTopNCtlTable = _DsmonHostTopNCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dsmonHostTopNCtlTable.setStatus("current")
_DsmonHostTopNCtlEntry_Object = MibTableRow
dsmonHostTopNCtlEntry = _DsmonHostTopNCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1)
)
dsmonHostTopNCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonHostTopNCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonHostTopNCtlEntry.setStatus("current")


class _DsmonHostTopNCtlIndex_Type(Integer32):
    """Custom type dsmonHostTopNCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonHostTopNCtlIndex_Type.__name__ = "Integer32"
_DsmonHostTopNCtlIndex_Object = MibTableColumn
dsmonHostTopNCtlIndex = _DsmonHostTopNCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 1),
    _DsmonHostTopNCtlIndex_Type()
)
dsmonHostTopNCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlIndex.setStatus("current")


class _DsmonHostTopNCtlHostIndex_Type(Integer32):
    """Custom type dsmonHostTopNCtlHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonHostTopNCtlHostIndex_Type.__name__ = "Integer32"
_DsmonHostTopNCtlHostIndex_Object = MibTableColumn
dsmonHostTopNCtlHostIndex = _DsmonHostTopNCtlHostIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 2),
    _DsmonHostTopNCtlHostIndex_Type()
)
dsmonHostTopNCtlHostIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlHostIndex.setStatus("current")


class _DsmonHostTopNCtlRateBase_Type(Integer32):
    """Custom type dsmonHostTopNCtlRateBase based on Integer32"""
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
        *(("dsmonHostTopNInHCOctets", 8),
          ("dsmonHostTopNInHCPkts", 7),
          ("dsmonHostTopNInOctets", 2),
          ("dsmonHostTopNInPkts", 1),
          ("dsmonHostTopNOutHCOctets", 10),
          ("dsmonHostTopNOutHCPkts", 9),
          ("dsmonHostTopNOutOctets", 4),
          ("dsmonHostTopNOutPkts", 3),
          ("dsmonHostTopNTotalHCOctets", 12),
          ("dsmonHostTopNTotalHCPkts", 11),
          ("dsmonHostTopNTotalOctets", 6),
          ("dsmonHostTopNTotalPkts", 5))
    )


_DsmonHostTopNCtlRateBase_Type.__name__ = "Integer32"
_DsmonHostTopNCtlRateBase_Object = MibTableColumn
dsmonHostTopNCtlRateBase = _DsmonHostTopNCtlRateBase_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 3),
    _DsmonHostTopNCtlRateBase_Type()
)
dsmonHostTopNCtlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlRateBase.setStatus("current")


class _DsmonHostTopNCtlTimeRemaining_Type(Integer32):
    """Custom type dsmonHostTopNCtlTimeRemaining based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonHostTopNCtlTimeRemaining_Type.__name__ = "Integer32"
_DsmonHostTopNCtlTimeRemaining_Object = MibTableColumn
dsmonHostTopNCtlTimeRemaining = _DsmonHostTopNCtlTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 4),
    _DsmonHostTopNCtlTimeRemaining_Type()
)
dsmonHostTopNCtlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlTimeRemaining.setUnits("seconds")
_DsmonHostTopNCtlGeneratedReports_Type = Counter32
_DsmonHostTopNCtlGeneratedReports_Object = MibTableColumn
dsmonHostTopNCtlGeneratedReports = _DsmonHostTopNCtlGeneratedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 5),
    _DsmonHostTopNCtlGeneratedReports_Type()
)
dsmonHostTopNCtlGeneratedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlGeneratedReports.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlGeneratedReports.setUnits("reports")


class _DsmonHostTopNCtlDuration_Type(Integer32):
    """Custom type dsmonHostTopNCtlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonHostTopNCtlDuration_Type.__name__ = "Integer32"
_DsmonHostTopNCtlDuration_Object = MibTableColumn
dsmonHostTopNCtlDuration = _DsmonHostTopNCtlDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 6),
    _DsmonHostTopNCtlDuration_Type()
)
dsmonHostTopNCtlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlDuration.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlDuration.setUnits("seconds")


class _DsmonHostTopNCtlRequestedSize_Type(Integer32):
    """Custom type dsmonHostTopNCtlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonHostTopNCtlRequestedSize_Type.__name__ = "Integer32"
_DsmonHostTopNCtlRequestedSize_Object = MibTableColumn
dsmonHostTopNCtlRequestedSize = _DsmonHostTopNCtlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 7),
    _DsmonHostTopNCtlRequestedSize_Type()
)
dsmonHostTopNCtlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlRequestedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlRequestedSize.setUnits("table entries")


class _DsmonHostTopNCtlGrantedSize_Type(Integer32):
    """Custom type dsmonHostTopNCtlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonHostTopNCtlGrantedSize_Type.__name__ = "Integer32"
_DsmonHostTopNCtlGrantedSize_Object = MibTableColumn
dsmonHostTopNCtlGrantedSize = _DsmonHostTopNCtlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 8),
    _DsmonHostTopNCtlGrantedSize_Type()
)
dsmonHostTopNCtlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlGrantedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlGrantedSize.setUnits("table entries")
_DsmonHostTopNCtlStartTime_Type = TimeStamp
_DsmonHostTopNCtlStartTime_Object = MibTableColumn
dsmonHostTopNCtlStartTime = _DsmonHostTopNCtlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 9),
    _DsmonHostTopNCtlStartTime_Type()
)
dsmonHostTopNCtlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlStartTime.setStatus("current")
_DsmonHostTopNCtlOwner_Type = OwnerString
_DsmonHostTopNCtlOwner_Object = MibTableColumn
dsmonHostTopNCtlOwner = _DsmonHostTopNCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 10),
    _DsmonHostTopNCtlOwner_Type()
)
dsmonHostTopNCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlOwner.setStatus("current")
_DsmonHostTopNCtlStatus_Type = RowStatus
_DsmonHostTopNCtlStatus_Object = MibTableColumn
dsmonHostTopNCtlStatus = _DsmonHostTopNCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 3, 1, 11),
    _DsmonHostTopNCtlStatus_Type()
)
dsmonHostTopNCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonHostTopNCtlStatus.setStatus("current")
_DsmonHostTopNTable_Object = MibTable
dsmonHostTopNTable = _DsmonHostTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dsmonHostTopNTable.setStatus("current")
_DsmonHostTopNEntry_Object = MibTableRow
dsmonHostTopNEntry = _DsmonHostTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1)
)
dsmonHostTopNEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonHostTopNCtlIndex"),
    (0, "DSMON-MIB", "dsmonHostTopNIndex"),
)
if mibBuilder.loadTexts:
    dsmonHostTopNEntry.setStatus("current")


class _DsmonHostTopNIndex_Type(Integer32):
    """Custom type dsmonHostTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonHostTopNIndex_Type.__name__ = "Integer32"
_DsmonHostTopNIndex_Object = MibTableColumn
dsmonHostTopNIndex = _DsmonHostTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 1),
    _DsmonHostTopNIndex_Type()
)
dsmonHostTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonHostTopNIndex.setStatus("current")


class _DsmonHostTopNPDLocalIndex_Type(Integer32):
    """Custom type dsmonHostTopNPDLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonHostTopNPDLocalIndex_Type.__name__ = "Integer32"
_DsmonHostTopNPDLocalIndex_Object = MibTableColumn
dsmonHostTopNPDLocalIndex = _DsmonHostTopNPDLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 2),
    _DsmonHostTopNPDLocalIndex_Type()
)
dsmonHostTopNPDLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNPDLocalIndex.setStatus("current")
_DsmonHostTopNAddress_Type = OctetString
_DsmonHostTopNAddress_Object = MibTableColumn
dsmonHostTopNAddress = _DsmonHostTopNAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 3),
    _DsmonHostTopNAddress_Type()
)
dsmonHostTopNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNAddress.setStatus("current")
_DsmonHostTopNAggGroup_Type = DsmonCounterAggGroupIndex
_DsmonHostTopNAggGroup_Object = MibTableColumn
dsmonHostTopNAggGroup = _DsmonHostTopNAggGroup_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 4),
    _DsmonHostTopNAggGroup_Type()
)
dsmonHostTopNAggGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNAggGroup.setStatus("current")
_DsmonHostTopNRate_Type = Gauge32
_DsmonHostTopNRate_Object = MibTableColumn
dsmonHostTopNRate = _DsmonHostTopNRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 5),
    _DsmonHostTopNRate_Type()
)
dsmonHostTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNRate.setStatus("current")
_DsmonHostTopNRateOvfl_Type = Gauge32
_DsmonHostTopNRateOvfl_Object = MibTableColumn
dsmonHostTopNRateOvfl = _DsmonHostTopNRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 6),
    _DsmonHostTopNRateOvfl_Type()
)
dsmonHostTopNRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNRateOvfl.setStatus("deprecated")
_DsmonHostTopNHCRate_Type = CounterBasedGauge64
_DsmonHostTopNHCRate_Object = MibTableColumn
dsmonHostTopNHCRate = _DsmonHostTopNHCRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 4, 4, 1, 7),
    _DsmonHostTopNHCRate_Type()
)
dsmonHostTopNHCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonHostTopNHCRate.setStatus("current")
_DsmonCapsObjects_ObjectIdentity = ObjectIdentity
dsmonCapsObjects = _DsmonCapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 5)
)


class _DsmonCapabilities_Type(Bits):
    """Custom type dsmonCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dsmonCaps", 10),
          ("dsmonCounterAggControl", 0),
          ("dsmonHost", 7),
          ("dsmonHostHC", 9),
          ("dsmonHostOvfl", 8),
          ("dsmonMatrix", 11),
          ("dsmonMatrixHC", 13),
          ("dsmonMatrixOvfl", 12),
          ("dsmonPdist", 4),
          ("dsmonPdistHC", 6),
          ("dsmonPdistOvfl", 5),
          ("dsmonStats", 1),
          ("dsmonStatsHC", 3),
          ("dsmonStatsOvfl", 2))
    )

_DsmonCapabilities_Type.__name__ = "Bits"
_DsmonCapabilities_Object = MibScalar
dsmonCapabilities = _DsmonCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 5, 1),
    _DsmonCapabilities_Type()
)
dsmonCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonCapabilities.setStatus("current")
_DsmonMatrixObjects_ObjectIdentity = ObjectIdentity
dsmonMatrixObjects = _DsmonMatrixObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6)
)
_DsmonMatrixCtlTable_Object = MibTable
dsmonMatrixCtlTable = _DsmonMatrixCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dsmonMatrixCtlTable.setStatus("current")
_DsmonMatrixCtlEntry_Object = MibTableRow
dsmonMatrixCtlEntry = _DsmonMatrixCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1)
)
dsmonMatrixCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonMatrixCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonMatrixCtlEntry.setStatus("current")


class _DsmonMatrixCtlIndex_Type(Integer32):
    """Custom type dsmonMatrixCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonMatrixCtlIndex_Type.__name__ = "Integer32"
_DsmonMatrixCtlIndex_Object = MibTableColumn
dsmonMatrixCtlIndex = _DsmonMatrixCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 1),
    _DsmonMatrixCtlIndex_Type()
)
dsmonMatrixCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixCtlIndex.setStatus("current")
_DsmonMatrixCtlDataSource_Type = DataSource
_DsmonMatrixCtlDataSource_Object = MibTableColumn
dsmonMatrixCtlDataSource = _DsmonMatrixCtlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 2),
    _DsmonMatrixCtlDataSource_Type()
)
dsmonMatrixCtlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixCtlDataSource.setStatus("current")
_DsmonMatrixCtlAggProfile_Type = DsmonCounterAggProfileIndex
_DsmonMatrixCtlAggProfile_Object = MibTableColumn
dsmonMatrixCtlAggProfile = _DsmonMatrixCtlAggProfile_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 3),
    _DsmonMatrixCtlAggProfile_Type()
)
dsmonMatrixCtlAggProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixCtlAggProfile.setStatus("current")


class _DsmonMatrixCtlMaxDesiredEntries_Type(Integer32):
    """Custom type dsmonMatrixCtlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixCtlMaxDesiredEntries_Type.__name__ = "Integer32"
_DsmonMatrixCtlMaxDesiredEntries_Object = MibTableColumn
dsmonMatrixCtlMaxDesiredEntries = _DsmonMatrixCtlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 4),
    _DsmonMatrixCtlMaxDesiredEntries_Type()
)
dsmonMatrixCtlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixCtlMaxDesiredEntries.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixCtlMaxDesiredEntries.setUnits("table entries")
_DsmonMatrixCtlDroppedFrames_Type = Counter32
_DsmonMatrixCtlDroppedFrames_Object = MibTableColumn
dsmonMatrixCtlDroppedFrames = _DsmonMatrixCtlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 5),
    _DsmonMatrixCtlDroppedFrames_Type()
)
dsmonMatrixCtlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixCtlDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixCtlDroppedFrames.setUnits("frames")
_DsmonMatrixCtlInserts_Type = Counter32
_DsmonMatrixCtlInserts_Object = MibTableColumn
dsmonMatrixCtlInserts = _DsmonMatrixCtlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 6),
    _DsmonMatrixCtlInserts_Type()
)
dsmonMatrixCtlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixCtlInserts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixCtlInserts.setUnits("table entries")
_DsmonMatrixCtlDeletes_Type = Counter32
_DsmonMatrixCtlDeletes_Object = MibTableColumn
dsmonMatrixCtlDeletes = _DsmonMatrixCtlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 7),
    _DsmonMatrixCtlDeletes_Type()
)
dsmonMatrixCtlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixCtlDeletes.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixCtlDeletes.setUnits("table entries")
_DsmonMatrixCtlCreateTime_Type = LastCreateTime
_DsmonMatrixCtlCreateTime_Object = MibTableColumn
dsmonMatrixCtlCreateTime = _DsmonMatrixCtlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 8),
    _DsmonMatrixCtlCreateTime_Type()
)
dsmonMatrixCtlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixCtlCreateTime.setStatus("current")
_DsmonMatrixCtlOwner_Type = OwnerString
_DsmonMatrixCtlOwner_Object = MibTableColumn
dsmonMatrixCtlOwner = _DsmonMatrixCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 9),
    _DsmonMatrixCtlOwner_Type()
)
dsmonMatrixCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixCtlOwner.setStatus("current")
_DsmonMatrixCtlStatus_Type = RowStatus
_DsmonMatrixCtlStatus_Object = MibTableColumn
dsmonMatrixCtlStatus = _DsmonMatrixCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 1, 1, 10),
    _DsmonMatrixCtlStatus_Type()
)
dsmonMatrixCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixCtlStatus.setStatus("current")
_DsmonMatrixSDTable_Object = MibTable
dsmonMatrixSDTable = _DsmonMatrixSDTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dsmonMatrixSDTable.setStatus("current")
_DsmonMatrixSDEntry_Object = MibTableRow
dsmonMatrixSDEntry = _DsmonMatrixSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1)
)
dsmonMatrixSDEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonMatrixCtlIndex"),
    (0, "DSMON-MIB", "dsmonMatrixTimeMark"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
    (0, "DSMON-MIB", "dsmonMatrixNLIndex"),
    (0, "DSMON-MIB", "dsmonMatrixSourceAddress"),
    (0, "DSMON-MIB", "dsmonMatrixDestAddress"),
    (0, "DSMON-MIB", "dsmonMatrixALIndex"),
)
if mibBuilder.loadTexts:
    dsmonMatrixSDEntry.setStatus("current")
_DsmonMatrixTimeMark_Type = TimeFilter
_DsmonMatrixTimeMark_Object = MibTableColumn
dsmonMatrixTimeMark = _DsmonMatrixTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 1),
    _DsmonMatrixTimeMark_Type()
)
dsmonMatrixTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixTimeMark.setStatus("current")


class _DsmonMatrixNLIndex_Type(Integer32):
    """Custom type dsmonMatrixNLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixNLIndex_Type.__name__ = "Integer32"
_DsmonMatrixNLIndex_Object = MibTableColumn
dsmonMatrixNLIndex = _DsmonMatrixNLIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 2),
    _DsmonMatrixNLIndex_Type()
)
dsmonMatrixNLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixNLIndex.setStatus("current")


class _DsmonMatrixSourceAddress_Type(OctetString):
    """Custom type dsmonMatrixSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_DsmonMatrixSourceAddress_Type.__name__ = "OctetString"
_DsmonMatrixSourceAddress_Object = MibTableColumn
dsmonMatrixSourceAddress = _DsmonMatrixSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 3),
    _DsmonMatrixSourceAddress_Type()
)
dsmonMatrixSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixSourceAddress.setStatus("current")


class _DsmonMatrixDestAddress_Type(OctetString):
    """Custom type dsmonMatrixDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_DsmonMatrixDestAddress_Type.__name__ = "OctetString"
_DsmonMatrixDestAddress_Object = MibTableColumn
dsmonMatrixDestAddress = _DsmonMatrixDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 4),
    _DsmonMatrixDestAddress_Type()
)
dsmonMatrixDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixDestAddress.setStatus("current")


class _DsmonMatrixALIndex_Type(Integer32):
    """Custom type dsmonMatrixALIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixALIndex_Type.__name__ = "Integer32"
_DsmonMatrixALIndex_Object = MibTableColumn
dsmonMatrixALIndex = _DsmonMatrixALIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 5),
    _DsmonMatrixALIndex_Type()
)
dsmonMatrixALIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixALIndex.setStatus("current")
_DsmonMatrixSDPkts_Type = ZeroBasedCounter32
_DsmonMatrixSDPkts_Object = MibTableColumn
dsmonMatrixSDPkts = _DsmonMatrixSDPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 6),
    _DsmonMatrixSDPkts_Type()
)
dsmonMatrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixSDPkts.setUnits("packets")
_DsmonMatrixSDOvflPkts_Type = ZeroBasedCounter32
_DsmonMatrixSDOvflPkts_Object = MibTableColumn
dsmonMatrixSDOvflPkts = _DsmonMatrixSDOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 7),
    _DsmonMatrixSDOvflPkts_Type()
)
dsmonMatrixSDOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDOvflPkts.setStatus("deprecated")
_DsmonMatrixSDHCPkts_Type = ZeroBasedCounter64
_DsmonMatrixSDHCPkts_Object = MibTableColumn
dsmonMatrixSDHCPkts = _DsmonMatrixSDHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 8),
    _DsmonMatrixSDHCPkts_Type()
)
dsmonMatrixSDHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixSDHCPkts.setUnits("packets")
_DsmonMatrixSDOctets_Type = ZeroBasedCounter32
_DsmonMatrixSDOctets_Object = MibTableColumn
dsmonMatrixSDOctets = _DsmonMatrixSDOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 9),
    _DsmonMatrixSDOctets_Type()
)
dsmonMatrixSDOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixSDOctets.setUnits("octets")
_DsmonMatrixSDOvflOctets_Type = ZeroBasedCounter32
_DsmonMatrixSDOvflOctets_Object = MibTableColumn
dsmonMatrixSDOvflOctets = _DsmonMatrixSDOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 10),
    _DsmonMatrixSDOvflOctets_Type()
)
dsmonMatrixSDOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDOvflOctets.setStatus("deprecated")
_DsmonMatrixSDHCOctets_Type = ZeroBasedCounter64
_DsmonMatrixSDHCOctets_Object = MibTableColumn
dsmonMatrixSDHCOctets = _DsmonMatrixSDHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 11),
    _DsmonMatrixSDHCOctets_Type()
)
dsmonMatrixSDHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixSDHCOctets.setUnits("octets")
_DsmonMatrixSDCreateTime_Type = LastCreateTime
_DsmonMatrixSDCreateTime_Object = MibTableColumn
dsmonMatrixSDCreateTime = _DsmonMatrixSDCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 2, 1, 12),
    _DsmonMatrixSDCreateTime_Type()
)
dsmonMatrixSDCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixSDCreateTime.setStatus("current")
_DsmonMatrixDSTable_Object = MibTable
dsmonMatrixDSTable = _DsmonMatrixDSTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dsmonMatrixDSTable.setStatus("current")
_DsmonMatrixDSEntry_Object = MibTableRow
dsmonMatrixDSEntry = _DsmonMatrixDSEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1)
)
dsmonMatrixDSEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonMatrixCtlIndex"),
    (0, "DSMON-MIB", "dsmonMatrixTimeMark"),
    (0, "DSMON-MIB", "dsmonAggGroupIndex"),
    (0, "DSMON-MIB", "dsmonMatrixNLIndex"),
    (0, "DSMON-MIB", "dsmonMatrixDestAddress"),
    (0, "DSMON-MIB", "dsmonMatrixSourceAddress"),
    (0, "DSMON-MIB", "dsmonMatrixALIndex"),
)
if mibBuilder.loadTexts:
    dsmonMatrixDSEntry.setStatus("current")
_DsmonMatrixDSPkts_Type = ZeroBasedCounter32
_DsmonMatrixDSPkts_Object = MibTableColumn
dsmonMatrixDSPkts = _DsmonMatrixDSPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 1),
    _DsmonMatrixDSPkts_Type()
)
dsmonMatrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixDSPkts.setUnits("packets")
_DsmonMatrixDSOvflPkts_Type = ZeroBasedCounter32
_DsmonMatrixDSOvflPkts_Object = MibTableColumn
dsmonMatrixDSOvflPkts = _DsmonMatrixDSOvflPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 2),
    _DsmonMatrixDSOvflPkts_Type()
)
dsmonMatrixDSOvflPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSOvflPkts.setStatus("deprecated")
_DsmonMatrixDSHCPkts_Type = ZeroBasedCounter64
_DsmonMatrixDSHCPkts_Object = MibTableColumn
dsmonMatrixDSHCPkts = _DsmonMatrixDSHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 3),
    _DsmonMatrixDSHCPkts_Type()
)
dsmonMatrixDSHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixDSHCPkts.setUnits("packets")
_DsmonMatrixDSOctets_Type = ZeroBasedCounter32
_DsmonMatrixDSOctets_Object = MibTableColumn
dsmonMatrixDSOctets = _DsmonMatrixDSOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 4),
    _DsmonMatrixDSOctets_Type()
)
dsmonMatrixDSOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixDSOctets.setUnits("octets")
_DsmonMatrixDSOvflOctets_Type = ZeroBasedCounter32
_DsmonMatrixDSOvflOctets_Object = MibTableColumn
dsmonMatrixDSOvflOctets = _DsmonMatrixDSOvflOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 5),
    _DsmonMatrixDSOvflOctets_Type()
)
dsmonMatrixDSOvflOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSOvflOctets.setStatus("deprecated")
_DsmonMatrixDSHCOctets_Type = ZeroBasedCounter64
_DsmonMatrixDSHCOctets_Object = MibTableColumn
dsmonMatrixDSHCOctets = _DsmonMatrixDSHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 6),
    _DsmonMatrixDSHCOctets_Type()
)
dsmonMatrixDSHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixDSHCOctets.setUnits("octets")
_DsmonMatrixDSCreateTime_Type = LastCreateTime
_DsmonMatrixDSCreateTime_Object = MibTableColumn
dsmonMatrixDSCreateTime = _DsmonMatrixDSCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 3, 1, 7),
    _DsmonMatrixDSCreateTime_Type()
)
dsmonMatrixDSCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixDSCreateTime.setStatus("current")
_DsmonMatrixTopNCtlTable_Object = MibTable
dsmonMatrixTopNCtlTable = _DsmonMatrixTopNCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4)
)
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlTable.setStatus("current")
_DsmonMatrixTopNCtlEntry_Object = MibTableRow
dsmonMatrixTopNCtlEntry = _DsmonMatrixTopNCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1)
)
dsmonMatrixTopNCtlEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonMatrixTopNCtlIndex"),
)
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlEntry.setStatus("current")


class _DsmonMatrixTopNCtlIndex_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonMatrixTopNCtlIndex_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlIndex_Object = MibTableColumn
dsmonMatrixTopNCtlIndex = _DsmonMatrixTopNCtlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 1),
    _DsmonMatrixTopNCtlIndex_Type()
)
dsmonMatrixTopNCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlIndex.setStatus("current")


class _DsmonMatrixTopNCtlMatrixIndex_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlMatrixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsmonMatrixTopNCtlMatrixIndex_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlMatrixIndex_Object = MibTableColumn
dsmonMatrixTopNCtlMatrixIndex = _DsmonMatrixTopNCtlMatrixIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 2),
    _DsmonMatrixTopNCtlMatrixIndex_Type()
)
dsmonMatrixTopNCtlMatrixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlMatrixIndex.setStatus("current")


class _DsmonMatrixTopNCtlRateBase_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlRateBase based on Integer32"""
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
        *(("dsmonMatrixTopNHCOctets", 4),
          ("dsmonMatrixTopNHCPkts", 3),
          ("dsmonMatrixTopNOctets", 2),
          ("dsmonMatrixTopNPkts", 1))
    )


_DsmonMatrixTopNCtlRateBase_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlRateBase_Object = MibTableColumn
dsmonMatrixTopNCtlRateBase = _DsmonMatrixTopNCtlRateBase_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 3),
    _DsmonMatrixTopNCtlRateBase_Type()
)
dsmonMatrixTopNCtlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlRateBase.setStatus("current")


class _DsmonMatrixTopNCtlTimeRemaining_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlTimeRemaining based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonMatrixTopNCtlTimeRemaining_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlTimeRemaining_Object = MibTableColumn
dsmonMatrixTopNCtlTimeRemaining = _DsmonMatrixTopNCtlTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 4),
    _DsmonMatrixTopNCtlTimeRemaining_Type()
)
dsmonMatrixTopNCtlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlTimeRemaining.setUnits("seconds")
_DsmonMatrixTopNCtlGeneratedRpts_Type = Counter32
_DsmonMatrixTopNCtlGeneratedRpts_Object = MibTableColumn
dsmonMatrixTopNCtlGeneratedRpts = _DsmonMatrixTopNCtlGeneratedRpts_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 5),
    _DsmonMatrixTopNCtlGeneratedRpts_Type()
)
dsmonMatrixTopNCtlGeneratedRpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlGeneratedRpts.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlGeneratedRpts.setUnits("reports")


class _DsmonMatrixTopNCtlDuration_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonMatrixTopNCtlDuration_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlDuration_Object = MibTableColumn
dsmonMatrixTopNCtlDuration = _DsmonMatrixTopNCtlDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 6),
    _DsmonMatrixTopNCtlDuration_Type()
)
dsmonMatrixTopNCtlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlDuration.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlDuration.setUnits("seconds")


class _DsmonMatrixTopNCtlRequestedSize_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonMatrixTopNCtlRequestedSize_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlRequestedSize_Object = MibTableColumn
dsmonMatrixTopNCtlRequestedSize = _DsmonMatrixTopNCtlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 7),
    _DsmonMatrixTopNCtlRequestedSize_Type()
)
dsmonMatrixTopNCtlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlRequestedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlRequestedSize.setUnits("table entries")


class _DsmonMatrixTopNCtlGrantedSize_Type(Integer32):
    """Custom type dsmonMatrixTopNCtlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsmonMatrixTopNCtlGrantedSize_Type.__name__ = "Integer32"
_DsmonMatrixTopNCtlGrantedSize_Object = MibTableColumn
dsmonMatrixTopNCtlGrantedSize = _DsmonMatrixTopNCtlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 8),
    _DsmonMatrixTopNCtlGrantedSize_Type()
)
dsmonMatrixTopNCtlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlGrantedSize.setStatus("current")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlGrantedSize.setUnits("table entries")
_DsmonMatrixTopNCtlStartTime_Type = TimeStamp
_DsmonMatrixTopNCtlStartTime_Object = MibTableColumn
dsmonMatrixTopNCtlStartTime = _DsmonMatrixTopNCtlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 9),
    _DsmonMatrixTopNCtlStartTime_Type()
)
dsmonMatrixTopNCtlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlStartTime.setStatus("current")
_DsmonMatrixTopNCtlOwner_Type = OwnerString
_DsmonMatrixTopNCtlOwner_Object = MibTableColumn
dsmonMatrixTopNCtlOwner = _DsmonMatrixTopNCtlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 10),
    _DsmonMatrixTopNCtlOwner_Type()
)
dsmonMatrixTopNCtlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlOwner.setStatus("current")
_DsmonMatrixTopNCtlStatus_Type = RowStatus
_DsmonMatrixTopNCtlStatus_Object = MibTableColumn
dsmonMatrixTopNCtlStatus = _DsmonMatrixTopNCtlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 4, 1, 11),
    _DsmonMatrixTopNCtlStatus_Type()
)
dsmonMatrixTopNCtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsmonMatrixTopNCtlStatus.setStatus("current")
_DsmonMatrixTopNTable_Object = MibTable
dsmonMatrixTopNTable = _DsmonMatrixTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5)
)
if mibBuilder.loadTexts:
    dsmonMatrixTopNTable.setStatus("current")
_DsmonMatrixTopNEntry_Object = MibTableRow
dsmonMatrixTopNEntry = _DsmonMatrixTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1)
)
dsmonMatrixTopNEntry.setIndexNames(
    (0, "DSMON-MIB", "dsmonMatrixTopNCtlIndex"),
    (0, "DSMON-MIB", "dsmonMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    dsmonMatrixTopNEntry.setStatus("current")


class _DsmonMatrixTopNIndex_Type(Integer32):
    """Custom type dsmonMatrixTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixTopNIndex_Type.__name__ = "Integer32"
_DsmonMatrixTopNIndex_Object = MibTableColumn
dsmonMatrixTopNIndex = _DsmonMatrixTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 1),
    _DsmonMatrixTopNIndex_Type()
)
dsmonMatrixTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsmonMatrixTopNIndex.setStatus("current")
_DsmonMatrixTopNAggGroup_Type = DsmonCounterAggGroupIndex
_DsmonMatrixTopNAggGroup_Object = MibTableColumn
dsmonMatrixTopNAggGroup = _DsmonMatrixTopNAggGroup_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 2),
    _DsmonMatrixTopNAggGroup_Type()
)
dsmonMatrixTopNAggGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNAggGroup.setStatus("current")


class _DsmonMatrixTopNNLIndex_Type(Integer32):
    """Custom type dsmonMatrixTopNNLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixTopNNLIndex_Type.__name__ = "Integer32"
_DsmonMatrixTopNNLIndex_Object = MibTableColumn
dsmonMatrixTopNNLIndex = _DsmonMatrixTopNNLIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 3),
    _DsmonMatrixTopNNLIndex_Type()
)
dsmonMatrixTopNNLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNNLIndex.setStatus("current")
_DsmonMatrixTopNSourceAddress_Type = OctetString
_DsmonMatrixTopNSourceAddress_Object = MibTableColumn
dsmonMatrixTopNSourceAddress = _DsmonMatrixTopNSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 4),
    _DsmonMatrixTopNSourceAddress_Type()
)
dsmonMatrixTopNSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNSourceAddress.setStatus("current")
_DsmonMatrixTopNDestAddress_Type = OctetString
_DsmonMatrixTopNDestAddress_Object = MibTableColumn
dsmonMatrixTopNDestAddress = _DsmonMatrixTopNDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 5),
    _DsmonMatrixTopNDestAddress_Type()
)
dsmonMatrixTopNDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNDestAddress.setStatus("current")


class _DsmonMatrixTopNALIndex_Type(Integer32):
    """Custom type dsmonMatrixTopNALIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DsmonMatrixTopNALIndex_Type.__name__ = "Integer32"
_DsmonMatrixTopNALIndex_Object = MibTableColumn
dsmonMatrixTopNALIndex = _DsmonMatrixTopNALIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 6),
    _DsmonMatrixTopNALIndex_Type()
)
dsmonMatrixTopNALIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNALIndex.setStatus("current")
_DsmonMatrixTopNPktRate_Type = Gauge32
_DsmonMatrixTopNPktRate_Object = MibTableColumn
dsmonMatrixTopNPktRate = _DsmonMatrixTopNPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 7),
    _DsmonMatrixTopNPktRate_Type()
)
dsmonMatrixTopNPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNPktRate.setStatus("current")
_DsmonMatrixTopNPktRateOvfl_Type = Gauge32
_DsmonMatrixTopNPktRateOvfl_Object = MibTableColumn
dsmonMatrixTopNPktRateOvfl = _DsmonMatrixTopNPktRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 8),
    _DsmonMatrixTopNPktRateOvfl_Type()
)
dsmonMatrixTopNPktRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNPktRateOvfl.setStatus("deprecated")
_DsmonMatrixTopNHCPktRate_Type = CounterBasedGauge64
_DsmonMatrixTopNHCPktRate_Object = MibTableColumn
dsmonMatrixTopNHCPktRate = _DsmonMatrixTopNHCPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 9),
    _DsmonMatrixTopNHCPktRate_Type()
)
dsmonMatrixTopNHCPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNHCPktRate.setStatus("current")
_DsmonMatrixTopNRevPktRate_Type = Gauge32
_DsmonMatrixTopNRevPktRate_Object = MibTableColumn
dsmonMatrixTopNRevPktRate = _DsmonMatrixTopNRevPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 10),
    _DsmonMatrixTopNRevPktRate_Type()
)
dsmonMatrixTopNRevPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNRevPktRate.setStatus("current")
_DsmonMatrixTopNRevPktRateOvfl_Type = Gauge32
_DsmonMatrixTopNRevPktRateOvfl_Object = MibTableColumn
dsmonMatrixTopNRevPktRateOvfl = _DsmonMatrixTopNRevPktRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 11),
    _DsmonMatrixTopNRevPktRateOvfl_Type()
)
dsmonMatrixTopNRevPktRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNRevPktRateOvfl.setStatus("deprecated")
_DsmonMatrixTopNHCRevPktRate_Type = CounterBasedGauge64
_DsmonMatrixTopNHCRevPktRate_Object = MibTableColumn
dsmonMatrixTopNHCRevPktRate = _DsmonMatrixTopNHCRevPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 12),
    _DsmonMatrixTopNHCRevPktRate_Type()
)
dsmonMatrixTopNHCRevPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNHCRevPktRate.setStatus("current")
_DsmonMatrixTopNOctetRate_Type = Gauge32
_DsmonMatrixTopNOctetRate_Object = MibTableColumn
dsmonMatrixTopNOctetRate = _DsmonMatrixTopNOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 13),
    _DsmonMatrixTopNOctetRate_Type()
)
dsmonMatrixTopNOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNOctetRate.setStatus("current")
_DsmonMatrixTopNOctetRateOvfl_Type = Gauge32
_DsmonMatrixTopNOctetRateOvfl_Object = MibTableColumn
dsmonMatrixTopNOctetRateOvfl = _DsmonMatrixTopNOctetRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 14),
    _DsmonMatrixTopNOctetRateOvfl_Type()
)
dsmonMatrixTopNOctetRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNOctetRateOvfl.setStatus("deprecated")
_DsmonMatrixTopNHCOctetRate_Type = CounterBasedGauge64
_DsmonMatrixTopNHCOctetRate_Object = MibTableColumn
dsmonMatrixTopNHCOctetRate = _DsmonMatrixTopNHCOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 15),
    _DsmonMatrixTopNHCOctetRate_Type()
)
dsmonMatrixTopNHCOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNHCOctetRate.setStatus("current")
_DsmonMatrixTopNRevOctetRate_Type = Gauge32
_DsmonMatrixTopNRevOctetRate_Object = MibTableColumn
dsmonMatrixTopNRevOctetRate = _DsmonMatrixTopNRevOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 16),
    _DsmonMatrixTopNRevOctetRate_Type()
)
dsmonMatrixTopNRevOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNRevOctetRate.setStatus("current")
_DsmonMatrixTopNRevOctetRateOvfl_Type = Gauge32
_DsmonMatrixTopNRevOctetRateOvfl_Object = MibTableColumn
dsmonMatrixTopNRevOctetRateOvfl = _DsmonMatrixTopNRevOctetRateOvfl_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 17),
    _DsmonMatrixTopNRevOctetRateOvfl_Type()
)
dsmonMatrixTopNRevOctetRateOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNRevOctetRateOvfl.setStatus("deprecated")
_DsmonMatrixTopNHCRevOctetRate_Type = CounterBasedGauge64
_DsmonMatrixTopNHCRevOctetRate_Object = MibTableColumn
dsmonMatrixTopNHCRevOctetRate = _DsmonMatrixTopNHCRevOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 26, 1, 6, 5, 1, 18),
    _DsmonMatrixTopNHCRevOctetRate_Type()
)
dsmonMatrixTopNHCRevOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsmonMatrixTopNHCRevOctetRate.setStatus("current")
_DsmonNotifications_ObjectIdentity = ObjectIdentity
dsmonNotifications = _DsmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 2)
)
_DsmonConformance_ObjectIdentity = ObjectIdentity
dsmonConformance = _DsmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 3)
)
_DsmonCompliances_ObjectIdentity = ObjectIdentity
dsmonCompliances = _DsmonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 1)
)
_DsmonGroups_ObjectIdentity = ObjectIdentity
dsmonGroups = _DsmonGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2)
)

# Managed Objects groups

dsmonCounterAggControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 1)
)
dsmonCounterAggControlGroup.setObjects(
      *(("DSMON-MIB", "dsmonMaxAggGroups"),
        ("DSMON-MIB", "dsmonAggControlLocked"),
        ("DSMON-MIB", "dsmonAggControlChanges"),
        ("DSMON-MIB", "dsmonAggControlLastChangeTime"),
        ("DSMON-MIB", "dsmonAggControlDescr"),
        ("DSMON-MIB", "dsmonAggControlOwner"),
        ("DSMON-MIB", "dsmonAggControlStatus"),
        ("DSMON-MIB", "dsmonAggGroupIndex"),
        ("DSMON-MIB", "dsmonAggGroupDescr"),
        ("DSMON-MIB", "dsmonAggGroupStatus"))
)
if mibBuilder.loadTexts:
    dsmonCounterAggControlGroup.setStatus("current")

dsmonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 2)
)
dsmonStatsGroup.setObjects(
      *(("DSMON-MIB", "dsmonStatsControlDataSource"),
        ("DSMON-MIB", "dsmonStatsControlAggProfile"),
        ("DSMON-MIB", "dsmonStatsControlDroppedFrames"),
        ("DSMON-MIB", "dsmonStatsControlCreateTime"),
        ("DSMON-MIB", "dsmonStatsControlOwner"),
        ("DSMON-MIB", "dsmonStatsControlStatus"),
        ("DSMON-MIB", "dsmonStatsInPkts"),
        ("DSMON-MIB", "dsmonStatsInOctets"),
        ("DSMON-MIB", "dsmonStatsOutPkts"),
        ("DSMON-MIB", "dsmonStatsOutOctets"))
)
if mibBuilder.loadTexts:
    dsmonStatsGroup.setStatus("current")

dsmonStatsOvflGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 3)
)
dsmonStatsOvflGroup.setObjects(
      *(("DSMON-MIB", "dsmonStatsInOvflPkts"),
        ("DSMON-MIB", "dsmonStatsInOvflOctets"),
        ("DSMON-MIB", "dsmonStatsOutOvflPkts"),
        ("DSMON-MIB", "dsmonStatsOutOvflOctets"))
)
if mibBuilder.loadTexts:
    dsmonStatsOvflGroup.setStatus("deprecated")

dsmonStatsHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 4)
)
dsmonStatsHCGroup.setObjects(
      *(("DSMON-MIB", "dsmonStatsInHCPkts"),
        ("DSMON-MIB", "dsmonStatsInHCOctets"),
        ("DSMON-MIB", "dsmonStatsOutHCPkts"),
        ("DSMON-MIB", "dsmonStatsOutHCOctets"))
)
if mibBuilder.loadTexts:
    dsmonStatsHCGroup.setStatus("current")

dsmonPdistGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 5)
)
dsmonPdistGroup.setObjects(
      *(("DSMON-MIB", "dsmonPdistCtlDataSource"),
        ("DSMON-MIB", "dsmonPdistCtlAggProfile"),
        ("DSMON-MIB", "dsmonPdistCtlMaxDesiredEntries"),
        ("DSMON-MIB", "dsmonPdistCtlDroppedFrames"),
        ("DSMON-MIB", "dsmonPdistCtlInserts"),
        ("DSMON-MIB", "dsmonPdistCtlDeletes"),
        ("DSMON-MIB", "dsmonPdistCtlCreateTime"),
        ("DSMON-MIB", "dsmonPdistCtlOwner"),
        ("DSMON-MIB", "dsmonPdistCtlStatus"),
        ("DSMON-MIB", "dsmonPdistStatsPkts"),
        ("DSMON-MIB", "dsmonPdistStatsOctets"),
        ("DSMON-MIB", "dsmonPdistStatsCreateTime"),
        ("DSMON-MIB", "dsmonPdistTopNCtlPdistIndex"),
        ("DSMON-MIB", "dsmonPdistTopNCtlRateBase"),
        ("DSMON-MIB", "dsmonPdistTopNCtlTimeRemaining"),
        ("DSMON-MIB", "dsmonPdistTopNCtlGeneratedReprts"),
        ("DSMON-MIB", "dsmonPdistTopNCtlDuration"),
        ("DSMON-MIB", "dsmonPdistTopNCtlRequestedSize"),
        ("DSMON-MIB", "dsmonPdistTopNCtlGrantedSize"),
        ("DSMON-MIB", "dsmonPdistTopNCtlStartTime"),
        ("DSMON-MIB", "dsmonPdistTopNCtlOwner"),
        ("DSMON-MIB", "dsmonPdistTopNCtlStatus"),
        ("DSMON-MIB", "dsmonPdistTopNPDLocalIndex"),
        ("DSMON-MIB", "dsmonPdistTopNAggGroup"),
        ("DSMON-MIB", "dsmonPdistTopNRate"))
)
if mibBuilder.loadTexts:
    dsmonPdistGroup.setStatus("current")

dsmonPdistOvflGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 6)
)
dsmonPdistOvflGroup.setObjects(
      *(("DSMON-MIB", "dsmonPdistStatsOvflPkts"),
        ("DSMON-MIB", "dsmonPdistStatsOvflOctets"),
        ("DSMON-MIB", "dsmonPdistTopNRateOvfl"))
)
if mibBuilder.loadTexts:
    dsmonPdistOvflGroup.setStatus("deprecated")

dsmonPdistHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 7)
)
dsmonPdistHCGroup.setObjects(
      *(("DSMON-MIB", "dsmonPdistStatsHCPkts"),
        ("DSMON-MIB", "dsmonPdistStatsHCOctets"),
        ("DSMON-MIB", "dsmonPdistTopNHCRate"))
)
if mibBuilder.loadTexts:
    dsmonPdistHCGroup.setStatus("current")

dsmonHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 8)
)
dsmonHostGroup.setObjects(
      *(("DSMON-MIB", "dsmonHostCtlDataSource"),
        ("DSMON-MIB", "dsmonHostCtlAggProfile"),
        ("DSMON-MIB", "dsmonHostCtlMaxDesiredEntries"),
        ("DSMON-MIB", "dsmonHostCtlIPv4PrefixLen"),
        ("DSMON-MIB", "dsmonHostCtlIPv6PrefixLen"),
        ("DSMON-MIB", "dsmonHostCtlDroppedFrames"),
        ("DSMON-MIB", "dsmonHostCtlInserts"),
        ("DSMON-MIB", "dsmonHostCtlDeletes"),
        ("DSMON-MIB", "dsmonHostCtlCreateTime"),
        ("DSMON-MIB", "dsmonHostCtlOwner"),
        ("DSMON-MIB", "dsmonHostCtlStatus"),
        ("DSMON-MIB", "dsmonHostInPkts"),
        ("DSMON-MIB", "dsmonHostInOctets"),
        ("DSMON-MIB", "dsmonHostOutPkts"),
        ("DSMON-MIB", "dsmonHostOutOctets"),
        ("DSMON-MIB", "dsmonHostCreateTime"),
        ("DSMON-MIB", "dsmonHostTopNCtlHostIndex"),
        ("DSMON-MIB", "dsmonHostTopNCtlRateBase"),
        ("DSMON-MIB", "dsmonHostTopNCtlTimeRemaining"),
        ("DSMON-MIB", "dsmonHostTopNCtlGeneratedReports"),
        ("DSMON-MIB", "dsmonHostTopNCtlDuration"),
        ("DSMON-MIB", "dsmonHostTopNCtlRequestedSize"),
        ("DSMON-MIB", "dsmonHostTopNCtlGrantedSize"),
        ("DSMON-MIB", "dsmonHostTopNCtlStartTime"),
        ("DSMON-MIB", "dsmonHostTopNCtlOwner"),
        ("DSMON-MIB", "dsmonHostTopNCtlStatus"),
        ("DSMON-MIB", "dsmonHostTopNPDLocalIndex"),
        ("DSMON-MIB", "dsmonHostTopNAddress"),
        ("DSMON-MIB", "dsmonHostTopNAggGroup"),
        ("DSMON-MIB", "dsmonHostTopNRate"))
)
if mibBuilder.loadTexts:
    dsmonHostGroup.setStatus("current")

dsmonHostOvflGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 9)
)
dsmonHostOvflGroup.setObjects(
      *(("DSMON-MIB", "dsmonHostInOvflPkts"),
        ("DSMON-MIB", "dsmonHostInOvflOctets"),
        ("DSMON-MIB", "dsmonHostOutOvflPkts"),
        ("DSMON-MIB", "dsmonHostOutOvflOctets"),
        ("DSMON-MIB", "dsmonHostTopNRateOvfl"))
)
if mibBuilder.loadTexts:
    dsmonHostOvflGroup.setStatus("deprecated")

dsmonHostHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 10)
)
dsmonHostHCGroup.setObjects(
      *(("DSMON-MIB", "dsmonHostInHCPkts"),
        ("DSMON-MIB", "dsmonHostInHCOctets"),
        ("DSMON-MIB", "dsmonHostOutHCPkts"),
        ("DSMON-MIB", "dsmonHostOutHCOctets"),
        ("DSMON-MIB", "dsmonHostTopNHCRate"))
)
if mibBuilder.loadTexts:
    dsmonHostHCGroup.setStatus("current")

dsmonCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 11)
)
dsmonCapsGroup.setObjects(
    ("DSMON-MIB", "dsmonCapabilities")
)
if mibBuilder.loadTexts:
    dsmonCapsGroup.setStatus("current")

dsmonMatrixGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 12)
)
dsmonMatrixGroup.setObjects(
      *(("DSMON-MIB", "dsmonMatrixCtlDataSource"),
        ("DSMON-MIB", "dsmonMatrixCtlAggProfile"),
        ("DSMON-MIB", "dsmonMatrixCtlMaxDesiredEntries"),
        ("DSMON-MIB", "dsmonMatrixCtlDroppedFrames"),
        ("DSMON-MIB", "dsmonMatrixCtlInserts"),
        ("DSMON-MIB", "dsmonMatrixCtlDeletes"),
        ("DSMON-MIB", "dsmonMatrixCtlCreateTime"),
        ("DSMON-MIB", "dsmonMatrixCtlOwner"),
        ("DSMON-MIB", "dsmonMatrixCtlStatus"),
        ("DSMON-MIB", "dsmonMatrixSDPkts"),
        ("DSMON-MIB", "dsmonMatrixSDOctets"),
        ("DSMON-MIB", "dsmonMatrixSDCreateTime"),
        ("DSMON-MIB", "dsmonMatrixDSPkts"),
        ("DSMON-MIB", "dsmonMatrixDSOctets"),
        ("DSMON-MIB", "dsmonMatrixDSCreateTime"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlMatrixIndex"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlRateBase"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlTimeRemaining"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlGeneratedRpts"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlDuration"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlRequestedSize"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlGrantedSize"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlStartTime"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlOwner"),
        ("DSMON-MIB", "dsmonMatrixTopNCtlStatus"),
        ("DSMON-MIB", "dsmonMatrixTopNAggGroup"),
        ("DSMON-MIB", "dsmonMatrixTopNNLIndex"),
        ("DSMON-MIB", "dsmonMatrixTopNSourceAddress"),
        ("DSMON-MIB", "dsmonMatrixTopNDestAddress"),
        ("DSMON-MIB", "dsmonMatrixTopNALIndex"),
        ("DSMON-MIB", "dsmonMatrixTopNPktRate"),
        ("DSMON-MIB", "dsmonMatrixTopNRevPktRate"),
        ("DSMON-MIB", "dsmonMatrixTopNOctetRate"),
        ("DSMON-MIB", "dsmonMatrixTopNRevOctetRate"))
)
if mibBuilder.loadTexts:
    dsmonMatrixGroup.setStatus("current")

dsmonMatrixOvflGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 13)
)
dsmonMatrixOvflGroup.setObjects(
      *(("DSMON-MIB", "dsmonMatrixSDOvflPkts"),
        ("DSMON-MIB", "dsmonMatrixSDOvflOctets"),
        ("DSMON-MIB", "dsmonMatrixDSOvflPkts"),
        ("DSMON-MIB", "dsmonMatrixDSOvflOctets"),
        ("DSMON-MIB", "dsmonMatrixTopNPktRateOvfl"),
        ("DSMON-MIB", "dsmonMatrixTopNRevPktRateOvfl"),
        ("DSMON-MIB", "dsmonMatrixTopNOctetRateOvfl"),
        ("DSMON-MIB", "dsmonMatrixTopNRevOctetRateOvfl"))
)
if mibBuilder.loadTexts:
    dsmonMatrixOvflGroup.setStatus("deprecated")

dsmonMatrixHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 2, 14)
)
dsmonMatrixHCGroup.setObjects(
      *(("DSMON-MIB", "dsmonMatrixSDHCPkts"),
        ("DSMON-MIB", "dsmonMatrixSDHCOctets"),
        ("DSMON-MIB", "dsmonMatrixDSHCPkts"),
        ("DSMON-MIB", "dsmonMatrixDSHCOctets"),
        ("DSMON-MIB", "dsmonMatrixTopNHCPktRate"),
        ("DSMON-MIB", "dsmonMatrixTopNHCRevPktRate"),
        ("DSMON-MIB", "dsmonMatrixTopNHCOctetRate"),
        ("DSMON-MIB", "dsmonMatrixTopNHCRevOctetRate"))
)
if mibBuilder.loadTexts:
    dsmonMatrixHCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsmonCompliance.setStatus(
        "current"
    )

dsmonHCCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dsmonHCCompliance.setStatus(
        "current"
    )

dsmonHCNoC64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 26, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dsmonHCNoC64Compliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSMON-MIB",
    **{"DsmonCounterAggGroupIndex": DsmonCounterAggGroupIndex,
       "DsmonCounterAggProfileIndex": DsmonCounterAggProfileIndex,
       "dsmonMIB": dsmonMIB,
       "dsmonObjects": dsmonObjects,
       "dsmonAggObjects": dsmonAggObjects,
       "dsmonMaxAggGroups": dsmonMaxAggGroups,
       "dsmonAggControlLocked": dsmonAggControlLocked,
       "dsmonAggControlChanges": dsmonAggControlChanges,
       "dsmonAggControlLastChangeTime": dsmonAggControlLastChangeTime,
       "dsmonAggControlTable": dsmonAggControlTable,
       "dsmonAggControlEntry": dsmonAggControlEntry,
       "dsmonAggControlIndex": dsmonAggControlIndex,
       "dsmonAggControlDescr": dsmonAggControlDescr,
       "dsmonAggControlOwner": dsmonAggControlOwner,
       "dsmonAggControlStatus": dsmonAggControlStatus,
       "dsmonAggProfileTable": dsmonAggProfileTable,
       "dsmonAggProfileEntry": dsmonAggProfileEntry,
       "dsmonAggProfileDSCP": dsmonAggProfileDSCP,
       "dsmonAggGroupIndex": dsmonAggGroupIndex,
       "dsmonAggGroupTable": dsmonAggGroupTable,
       "dsmonAggGroupEntry": dsmonAggGroupEntry,
       "dsmonAggGroupDescr": dsmonAggGroupDescr,
       "dsmonAggGroupStatus": dsmonAggGroupStatus,
       "dsmonStatsObjects": dsmonStatsObjects,
       "dsmonStatsControlTable": dsmonStatsControlTable,
       "dsmonStatsControlEntry": dsmonStatsControlEntry,
       "dsmonStatsControlIndex": dsmonStatsControlIndex,
       "dsmonStatsControlDataSource": dsmonStatsControlDataSource,
       "dsmonStatsControlAggProfile": dsmonStatsControlAggProfile,
       "dsmonStatsControlDroppedFrames": dsmonStatsControlDroppedFrames,
       "dsmonStatsControlCreateTime": dsmonStatsControlCreateTime,
       "dsmonStatsControlOwner": dsmonStatsControlOwner,
       "dsmonStatsControlStatus": dsmonStatsControlStatus,
       "dsmonStatsTable": dsmonStatsTable,
       "dsmonStatsEntry": dsmonStatsEntry,
       "dsmonStatsInPkts": dsmonStatsInPkts,
       "dsmonStatsInOctets": dsmonStatsInOctets,
       "dsmonStatsInOvflPkts": dsmonStatsInOvflPkts,
       "dsmonStatsInOvflOctets": dsmonStatsInOvflOctets,
       "dsmonStatsInHCPkts": dsmonStatsInHCPkts,
       "dsmonStatsInHCOctets": dsmonStatsInHCOctets,
       "dsmonStatsOutPkts": dsmonStatsOutPkts,
       "dsmonStatsOutOctets": dsmonStatsOutOctets,
       "dsmonStatsOutOvflPkts": dsmonStatsOutOvflPkts,
       "dsmonStatsOutOvflOctets": dsmonStatsOutOvflOctets,
       "dsmonStatsOutHCPkts": dsmonStatsOutHCPkts,
       "dsmonStatsOutHCOctets": dsmonStatsOutHCOctets,
       "dsmonPdistObjects": dsmonPdistObjects,
       "dsmonPdistCtlTable": dsmonPdistCtlTable,
       "dsmonPdistCtlEntry": dsmonPdistCtlEntry,
       "dsmonPdistCtlIndex": dsmonPdistCtlIndex,
       "dsmonPdistCtlDataSource": dsmonPdistCtlDataSource,
       "dsmonPdistCtlAggProfile": dsmonPdistCtlAggProfile,
       "dsmonPdistCtlMaxDesiredEntries": dsmonPdistCtlMaxDesiredEntries,
       "dsmonPdistCtlDroppedFrames": dsmonPdistCtlDroppedFrames,
       "dsmonPdistCtlInserts": dsmonPdistCtlInserts,
       "dsmonPdistCtlDeletes": dsmonPdistCtlDeletes,
       "dsmonPdistCtlCreateTime": dsmonPdistCtlCreateTime,
       "dsmonPdistCtlOwner": dsmonPdistCtlOwner,
       "dsmonPdistCtlStatus": dsmonPdistCtlStatus,
       "dsmonPdistStatsTable": dsmonPdistStatsTable,
       "dsmonPdistStatsEntry": dsmonPdistStatsEntry,
       "dsmonPdistTimeMark": dsmonPdistTimeMark,
       "dsmonPdistStatsPkts": dsmonPdistStatsPkts,
       "dsmonPdistStatsOctets": dsmonPdistStatsOctets,
       "dsmonPdistStatsOvflPkts": dsmonPdistStatsOvflPkts,
       "dsmonPdistStatsOvflOctets": dsmonPdistStatsOvflOctets,
       "dsmonPdistStatsHCPkts": dsmonPdistStatsHCPkts,
       "dsmonPdistStatsHCOctets": dsmonPdistStatsHCOctets,
       "dsmonPdistStatsCreateTime": dsmonPdistStatsCreateTime,
       "dsmonPdistTopNCtlTable": dsmonPdistTopNCtlTable,
       "dsmonPdistTopNCtlEntry": dsmonPdistTopNCtlEntry,
       "dsmonPdistTopNCtlIndex": dsmonPdistTopNCtlIndex,
       "dsmonPdistTopNCtlPdistIndex": dsmonPdistTopNCtlPdistIndex,
       "dsmonPdistTopNCtlRateBase": dsmonPdistTopNCtlRateBase,
       "dsmonPdistTopNCtlTimeRemaining": dsmonPdistTopNCtlTimeRemaining,
       "dsmonPdistTopNCtlGeneratedReprts": dsmonPdistTopNCtlGeneratedReprts,
       "dsmonPdistTopNCtlDuration": dsmonPdistTopNCtlDuration,
       "dsmonPdistTopNCtlRequestedSize": dsmonPdistTopNCtlRequestedSize,
       "dsmonPdistTopNCtlGrantedSize": dsmonPdistTopNCtlGrantedSize,
       "dsmonPdistTopNCtlStartTime": dsmonPdistTopNCtlStartTime,
       "dsmonPdistTopNCtlOwner": dsmonPdistTopNCtlOwner,
       "dsmonPdistTopNCtlStatus": dsmonPdistTopNCtlStatus,
       "dsmonPdistTopNTable": dsmonPdistTopNTable,
       "dsmonPdistTopNEntry": dsmonPdistTopNEntry,
       "dsmonPdistTopNIndex": dsmonPdistTopNIndex,
       "dsmonPdistTopNPDLocalIndex": dsmonPdistTopNPDLocalIndex,
       "dsmonPdistTopNAggGroup": dsmonPdistTopNAggGroup,
       "dsmonPdistTopNRate": dsmonPdistTopNRate,
       "dsmonPdistTopNRateOvfl": dsmonPdistTopNRateOvfl,
       "dsmonPdistTopNHCRate": dsmonPdistTopNHCRate,
       "dsmonHostObjects": dsmonHostObjects,
       "dsmonHostCtlTable": dsmonHostCtlTable,
       "dsmonHostCtlEntry": dsmonHostCtlEntry,
       "dsmonHostCtlIndex": dsmonHostCtlIndex,
       "dsmonHostCtlDataSource": dsmonHostCtlDataSource,
       "dsmonHostCtlAggProfile": dsmonHostCtlAggProfile,
       "dsmonHostCtlMaxDesiredEntries": dsmonHostCtlMaxDesiredEntries,
       "dsmonHostCtlIPv4PrefixLen": dsmonHostCtlIPv4PrefixLen,
       "dsmonHostCtlIPv6PrefixLen": dsmonHostCtlIPv6PrefixLen,
       "dsmonHostCtlDroppedFrames": dsmonHostCtlDroppedFrames,
       "dsmonHostCtlInserts": dsmonHostCtlInserts,
       "dsmonHostCtlDeletes": dsmonHostCtlDeletes,
       "dsmonHostCtlCreateTime": dsmonHostCtlCreateTime,
       "dsmonHostCtlOwner": dsmonHostCtlOwner,
       "dsmonHostCtlStatus": dsmonHostCtlStatus,
       "dsmonHostTable": dsmonHostTable,
       "dsmonHostEntry": dsmonHostEntry,
       "dsmonHostTimeMark": dsmonHostTimeMark,
       "dsmonHostAddress": dsmonHostAddress,
       "dsmonHostInPkts": dsmonHostInPkts,
       "dsmonHostInOctets": dsmonHostInOctets,
       "dsmonHostInOvflPkts": dsmonHostInOvflPkts,
       "dsmonHostInOvflOctets": dsmonHostInOvflOctets,
       "dsmonHostInHCPkts": dsmonHostInHCPkts,
       "dsmonHostInHCOctets": dsmonHostInHCOctets,
       "dsmonHostOutPkts": dsmonHostOutPkts,
       "dsmonHostOutOctets": dsmonHostOutOctets,
       "dsmonHostOutOvflPkts": dsmonHostOutOvflPkts,
       "dsmonHostOutOvflOctets": dsmonHostOutOvflOctets,
       "dsmonHostOutHCPkts": dsmonHostOutHCPkts,
       "dsmonHostOutHCOctets": dsmonHostOutHCOctets,
       "dsmonHostCreateTime": dsmonHostCreateTime,
       "dsmonHostTopNCtlTable": dsmonHostTopNCtlTable,
       "dsmonHostTopNCtlEntry": dsmonHostTopNCtlEntry,
       "dsmonHostTopNCtlIndex": dsmonHostTopNCtlIndex,
       "dsmonHostTopNCtlHostIndex": dsmonHostTopNCtlHostIndex,
       "dsmonHostTopNCtlRateBase": dsmonHostTopNCtlRateBase,
       "dsmonHostTopNCtlTimeRemaining": dsmonHostTopNCtlTimeRemaining,
       "dsmonHostTopNCtlGeneratedReports": dsmonHostTopNCtlGeneratedReports,
       "dsmonHostTopNCtlDuration": dsmonHostTopNCtlDuration,
       "dsmonHostTopNCtlRequestedSize": dsmonHostTopNCtlRequestedSize,
       "dsmonHostTopNCtlGrantedSize": dsmonHostTopNCtlGrantedSize,
       "dsmonHostTopNCtlStartTime": dsmonHostTopNCtlStartTime,
       "dsmonHostTopNCtlOwner": dsmonHostTopNCtlOwner,
       "dsmonHostTopNCtlStatus": dsmonHostTopNCtlStatus,
       "dsmonHostTopNTable": dsmonHostTopNTable,
       "dsmonHostTopNEntry": dsmonHostTopNEntry,
       "dsmonHostTopNIndex": dsmonHostTopNIndex,
       "dsmonHostTopNPDLocalIndex": dsmonHostTopNPDLocalIndex,
       "dsmonHostTopNAddress": dsmonHostTopNAddress,
       "dsmonHostTopNAggGroup": dsmonHostTopNAggGroup,
       "dsmonHostTopNRate": dsmonHostTopNRate,
       "dsmonHostTopNRateOvfl": dsmonHostTopNRateOvfl,
       "dsmonHostTopNHCRate": dsmonHostTopNHCRate,
       "dsmonCapsObjects": dsmonCapsObjects,
       "dsmonCapabilities": dsmonCapabilities,
       "dsmonMatrixObjects": dsmonMatrixObjects,
       "dsmonMatrixCtlTable": dsmonMatrixCtlTable,
       "dsmonMatrixCtlEntry": dsmonMatrixCtlEntry,
       "dsmonMatrixCtlIndex": dsmonMatrixCtlIndex,
       "dsmonMatrixCtlDataSource": dsmonMatrixCtlDataSource,
       "dsmonMatrixCtlAggProfile": dsmonMatrixCtlAggProfile,
       "dsmonMatrixCtlMaxDesiredEntries": dsmonMatrixCtlMaxDesiredEntries,
       "dsmonMatrixCtlDroppedFrames": dsmonMatrixCtlDroppedFrames,
       "dsmonMatrixCtlInserts": dsmonMatrixCtlInserts,
       "dsmonMatrixCtlDeletes": dsmonMatrixCtlDeletes,
       "dsmonMatrixCtlCreateTime": dsmonMatrixCtlCreateTime,
       "dsmonMatrixCtlOwner": dsmonMatrixCtlOwner,
       "dsmonMatrixCtlStatus": dsmonMatrixCtlStatus,
       "dsmonMatrixSDTable": dsmonMatrixSDTable,
       "dsmonMatrixSDEntry": dsmonMatrixSDEntry,
       "dsmonMatrixTimeMark": dsmonMatrixTimeMark,
       "dsmonMatrixNLIndex": dsmonMatrixNLIndex,
       "dsmonMatrixSourceAddress": dsmonMatrixSourceAddress,
       "dsmonMatrixDestAddress": dsmonMatrixDestAddress,
       "dsmonMatrixALIndex": dsmonMatrixALIndex,
       "dsmonMatrixSDPkts": dsmonMatrixSDPkts,
       "dsmonMatrixSDOvflPkts": dsmonMatrixSDOvflPkts,
       "dsmonMatrixSDHCPkts": dsmonMatrixSDHCPkts,
       "dsmonMatrixSDOctets": dsmonMatrixSDOctets,
       "dsmonMatrixSDOvflOctets": dsmonMatrixSDOvflOctets,
       "dsmonMatrixSDHCOctets": dsmonMatrixSDHCOctets,
       "dsmonMatrixSDCreateTime": dsmonMatrixSDCreateTime,
       "dsmonMatrixDSTable": dsmonMatrixDSTable,
       "dsmonMatrixDSEntry": dsmonMatrixDSEntry,
       "dsmonMatrixDSPkts": dsmonMatrixDSPkts,
       "dsmonMatrixDSOvflPkts": dsmonMatrixDSOvflPkts,
       "dsmonMatrixDSHCPkts": dsmonMatrixDSHCPkts,
       "dsmonMatrixDSOctets": dsmonMatrixDSOctets,
       "dsmonMatrixDSOvflOctets": dsmonMatrixDSOvflOctets,
       "dsmonMatrixDSHCOctets": dsmonMatrixDSHCOctets,
       "dsmonMatrixDSCreateTime": dsmonMatrixDSCreateTime,
       "dsmonMatrixTopNCtlTable": dsmonMatrixTopNCtlTable,
       "dsmonMatrixTopNCtlEntry": dsmonMatrixTopNCtlEntry,
       "dsmonMatrixTopNCtlIndex": dsmonMatrixTopNCtlIndex,
       "dsmonMatrixTopNCtlMatrixIndex": dsmonMatrixTopNCtlMatrixIndex,
       "dsmonMatrixTopNCtlRateBase": dsmonMatrixTopNCtlRateBase,
       "dsmonMatrixTopNCtlTimeRemaining": dsmonMatrixTopNCtlTimeRemaining,
       "dsmonMatrixTopNCtlGeneratedRpts": dsmonMatrixTopNCtlGeneratedRpts,
       "dsmonMatrixTopNCtlDuration": dsmonMatrixTopNCtlDuration,
       "dsmonMatrixTopNCtlRequestedSize": dsmonMatrixTopNCtlRequestedSize,
       "dsmonMatrixTopNCtlGrantedSize": dsmonMatrixTopNCtlGrantedSize,
       "dsmonMatrixTopNCtlStartTime": dsmonMatrixTopNCtlStartTime,
       "dsmonMatrixTopNCtlOwner": dsmonMatrixTopNCtlOwner,
       "dsmonMatrixTopNCtlStatus": dsmonMatrixTopNCtlStatus,
       "dsmonMatrixTopNTable": dsmonMatrixTopNTable,
       "dsmonMatrixTopNEntry": dsmonMatrixTopNEntry,
       "dsmonMatrixTopNIndex": dsmonMatrixTopNIndex,
       "dsmonMatrixTopNAggGroup": dsmonMatrixTopNAggGroup,
       "dsmonMatrixTopNNLIndex": dsmonMatrixTopNNLIndex,
       "dsmonMatrixTopNSourceAddress": dsmonMatrixTopNSourceAddress,
       "dsmonMatrixTopNDestAddress": dsmonMatrixTopNDestAddress,
       "dsmonMatrixTopNALIndex": dsmonMatrixTopNALIndex,
       "dsmonMatrixTopNPktRate": dsmonMatrixTopNPktRate,
       "dsmonMatrixTopNPktRateOvfl": dsmonMatrixTopNPktRateOvfl,
       "dsmonMatrixTopNHCPktRate": dsmonMatrixTopNHCPktRate,
       "dsmonMatrixTopNRevPktRate": dsmonMatrixTopNRevPktRate,
       "dsmonMatrixTopNRevPktRateOvfl": dsmonMatrixTopNRevPktRateOvfl,
       "dsmonMatrixTopNHCRevPktRate": dsmonMatrixTopNHCRevPktRate,
       "dsmonMatrixTopNOctetRate": dsmonMatrixTopNOctetRate,
       "dsmonMatrixTopNOctetRateOvfl": dsmonMatrixTopNOctetRateOvfl,
       "dsmonMatrixTopNHCOctetRate": dsmonMatrixTopNHCOctetRate,
       "dsmonMatrixTopNRevOctetRate": dsmonMatrixTopNRevOctetRate,
       "dsmonMatrixTopNRevOctetRateOvfl": dsmonMatrixTopNRevOctetRateOvfl,
       "dsmonMatrixTopNHCRevOctetRate": dsmonMatrixTopNHCRevOctetRate,
       "dsmonNotifications": dsmonNotifications,
       "dsmonConformance": dsmonConformance,
       "dsmonCompliances": dsmonCompliances,
       "dsmonCompliance": dsmonCompliance,
       "dsmonHCCompliance": dsmonHCCompliance,
       "dsmonHCNoC64Compliance": dsmonHCNoC64Compliance,
       "dsmonGroups": dsmonGroups,
       "dsmonCounterAggControlGroup": dsmonCounterAggControlGroup,
       "dsmonStatsGroup": dsmonStatsGroup,
       "dsmonStatsOvflGroup": dsmonStatsOvflGroup,
       "dsmonStatsHCGroup": dsmonStatsHCGroup,
       "dsmonPdistGroup": dsmonPdistGroup,
       "dsmonPdistOvflGroup": dsmonPdistOvflGroup,
       "dsmonPdistHCGroup": dsmonPdistHCGroup,
       "dsmonHostGroup": dsmonHostGroup,
       "dsmonHostOvflGroup": dsmonHostOvflGroup,
       "dsmonHostHCGroup": dsmonHostHCGroup,
       "dsmonCapsGroup": dsmonCapsGroup,
       "dsmonMatrixGroup": dsmonMatrixGroup,
       "dsmonMatrixOvflGroup": dsmonMatrixOvflGroup,
       "dsmonMatrixHCGroup": dsmonMatrixHCGroup}
)
