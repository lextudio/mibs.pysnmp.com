# SNMP MIB module (SMON2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMON2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:37 2024
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

(smon,) = mibBuilder.importSymbols(
    "APPLIC-MIB",
    "smon")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(DataSource,
 LastCreateTime,
 TimeFilter,
 ZeroBasedCounter32,
 hlMatrixControlIndex,
 protocolDirLocalIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "DataSource",
    "LastCreateTime",
    "TimeFilter",
    "ZeroBasedCounter32",
    "hlMatrixControlIndex",
    "protocolDirLocalIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XsSmon_ObjectIdentity = ObjectIdentity
xsSmon = _XsSmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 2)
)


class _XsSmonResourceAllocation_Type(OctetString):
    """Custom type xsSmonResourceAllocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XsSmonResourceAllocation_Type.__name__ = "OctetString"
_XsSmonResourceAllocation_Object = MibScalar
xsSmonResourceAllocation = _XsSmonResourceAllocation_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 1),
    _XsSmonResourceAllocation_Type()
)
xsSmonResourceAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSmonResourceAllocation.setStatus("current")
_XsHostTopN_ObjectIdentity = ObjectIdentity
xsHostTopN = _XsHostTopN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2)
)
_XsHostTopNControlTable_Object = MibTable
xsHostTopNControlTable = _XsHostTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xsHostTopNControlTable.setStatus("current")
_XsHostTopNControlEntry_Object = MibTableRow
xsHostTopNControlEntry = _XsHostTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1)
)
xsHostTopNControlEntry.setIndexNames(
    (0, "SMON2-MIB", "xsHostTopNControlIndex"),
)
if mibBuilder.loadTexts:
    xsHostTopNControlEntry.setStatus("current")


class _XsHostTopNControlIndex_Type(Integer32):
    """Custom type xsHostTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XsHostTopNControlIndex_Type.__name__ = "Integer32"
_XsHostTopNControlIndex_Object = MibTableColumn
xsHostTopNControlIndex = _XsHostTopNControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 1),
    _XsHostTopNControlIndex_Type()
)
xsHostTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsHostTopNControlIndex.setStatus("current")


class _XsHostTopNControlHostIndex_Type(Integer32):
    """Custom type xsHostTopNControlHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XsHostTopNControlHostIndex_Type.__name__ = "Integer32"
_XsHostTopNControlHostIndex_Object = MibTableColumn
xsHostTopNControlHostIndex = _XsHostTopNControlHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 2),
    _XsHostTopNControlHostIndex_Type()
)
xsHostTopNControlHostIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlHostIndex.setStatus("current")


class _XsHostTopNControlRateBase_Type(Integer32):
    """Custom type xsHostTopNControlRateBase based on Integer32"""
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
        *(("xsHostTopNInOctets", 3),
          ("xsHostTopNInPkts", 1),
          ("xsHostTopNOutOctets", 4),
          ("xsHostTopNOutPkts", 2))
    )


_XsHostTopNControlRateBase_Type.__name__ = "Integer32"
_XsHostTopNControlRateBase_Object = MibTableColumn
xsHostTopNControlRateBase = _XsHostTopNControlRateBase_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 3),
    _XsHostTopNControlRateBase_Type()
)
xsHostTopNControlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlRateBase.setStatus("current")


class _XsHostTopNControlTimeRemaining_Type(Integer32):
    """Custom type xsHostTopNControlTimeRemaining based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XsHostTopNControlTimeRemaining_Type.__name__ = "Integer32"
_XsHostTopNControlTimeRemaining_Object = MibTableColumn
xsHostTopNControlTimeRemaining = _XsHostTopNControlTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 4),
    _XsHostTopNControlTimeRemaining_Type()
)
xsHostTopNControlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlTimeRemaining.setStatus("current")
_XsHostTopNControlDuration_Type = Integer32
_XsHostTopNControlDuration_Object = MibTableColumn
xsHostTopNControlDuration = _XsHostTopNControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 5),
    _XsHostTopNControlDuration_Type()
)
xsHostTopNControlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNControlDuration.setStatus("current")


class _XsHostTopNControlRequestedSize_Type(Integer32):
    """Custom type xsHostTopNControlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XsHostTopNControlRequestedSize_Type.__name__ = "Integer32"
_XsHostTopNControlRequestedSize_Object = MibTableColumn
xsHostTopNControlRequestedSize = _XsHostTopNControlRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 6),
    _XsHostTopNControlRequestedSize_Type()
)
xsHostTopNControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlRequestedSize.setStatus("current")


class _XsHostTopNControlGrantedSize_Type(Integer32):
    """Custom type xsHostTopNControlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XsHostTopNControlGrantedSize_Type.__name__ = "Integer32"
_XsHostTopNControlGrantedSize_Object = MibTableColumn
xsHostTopNControlGrantedSize = _XsHostTopNControlGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 7),
    _XsHostTopNControlGrantedSize_Type()
)
xsHostTopNControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNControlGrantedSize.setStatus("current")
_XsHostTopNControlStartTime_Type = TimeStamp
_XsHostTopNControlStartTime_Object = MibTableColumn
xsHostTopNControlStartTime = _XsHostTopNControlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 8),
    _XsHostTopNControlStartTime_Type()
)
xsHostTopNControlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNControlStartTime.setStatus("current")
_XsHostTopNControlOwner_Type = OwnerString
_XsHostTopNControlOwner_Object = MibTableColumn
xsHostTopNControlOwner = _XsHostTopNControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 9),
    _XsHostTopNControlOwner_Type()
)
xsHostTopNControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlOwner.setStatus("current")
_XsHostTopNControlStatus_Type = RowStatus
_XsHostTopNControlStatus_Object = MibTableColumn
xsHostTopNControlStatus = _XsHostTopNControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 1, 1, 10),
    _XsHostTopNControlStatus_Type()
)
xsHostTopNControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsHostTopNControlStatus.setStatus("current")
_XsHostTopNTable_Object = MibTable
xsHostTopNTable = _XsHostTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xsHostTopNTable.setStatus("current")
_XsHostTopNEntry_Object = MibTableRow
xsHostTopNEntry = _XsHostTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2, 1)
)
xsHostTopNEntry.setIndexNames(
    (0, "SMON2-MIB", "xsHostTopNControlIndex"),
    (0, "SMON2-MIB", "xsHostTopNIndex"),
)
if mibBuilder.loadTexts:
    xsHostTopNEntry.setStatus("current")


class _XsHostTopNIndex_Type(Integer32):
    """Custom type xsHostTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XsHostTopNIndex_Type.__name__ = "Integer32"
_XsHostTopNIndex_Object = MibTableColumn
xsHostTopNIndex = _XsHostTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2, 1, 1),
    _XsHostTopNIndex_Type()
)
xsHostTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsHostTopNIndex.setStatus("current")


class _XsHostTopNProtocolDirLocalIndex_Type(Integer32):
    """Custom type xsHostTopNProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XsHostTopNProtocolDirLocalIndex_Type.__name__ = "Integer32"
_XsHostTopNProtocolDirLocalIndex_Object = MibTableColumn
xsHostTopNProtocolDirLocalIndex = _XsHostTopNProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2, 1, 2),
    _XsHostTopNProtocolDirLocalIndex_Type()
)
xsHostTopNProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNProtocolDirLocalIndex.setStatus("current")
_XsHostTopNNlAddress_Type = OctetString
_XsHostTopNNlAddress_Object = MibTableColumn
xsHostTopNNlAddress = _XsHostTopNNlAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2, 1, 3),
    _XsHostTopNNlAddress_Type()
)
xsHostTopNNlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNNlAddress.setStatus("current")
_XsHostTopNRate_Type = Gauge32
_XsHostTopNRate_Object = MibTableColumn
xsHostTopNRate = _XsHostTopNRate_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 2, 2, 1, 4),
    _XsHostTopNRate_Type()
)
xsHostTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsHostTopNRate.setStatus("current")
_XsFilter_ObjectIdentity = ObjectIdentity
xsFilter = _XsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3)
)
_XsHostFilterTable_Object = MibTable
xsHostFilterTable = _XsHostFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xsHostFilterTable.setStatus("current")
_XsHostFilterEntry_Object = MibTableRow
xsHostFilterEntry = _XsHostFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1)
)
xsHostFilterEntry.setIndexNames(
    (0, "SMON2-MIB", "xsHostFilterIpAddress"),
)
if mibBuilder.loadTexts:
    xsHostFilterEntry.setStatus("current")


class _XsHostFilterType_Type(Integer32):
    """Custom type xsHostFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipHost", 1),
          ("ipSubnet", 2),
          ("ipxNet", 3))
    )


_XsHostFilterType_Type.__name__ = "Integer32"
_XsHostFilterType_Object = MibTableColumn
xsHostFilterType = _XsHostFilterType_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 1),
    _XsHostFilterType_Type()
)
xsHostFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterType.setStatus("current")
_XsHostFilterIpAddress_Type = OctetString
_XsHostFilterIpAddress_Object = MibTableColumn
xsHostFilterIpAddress = _XsHostFilterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 2),
    _XsHostFilterIpAddress_Type()
)
xsHostFilterIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterIpAddress.setStatus("current")
_XsHostFilterIpSubnet_Type = OctetString
_XsHostFilterIpSubnet_Object = MibTableColumn
xsHostFilterIpSubnet = _XsHostFilterIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 3),
    _XsHostFilterIpSubnet_Type()
)
xsHostFilterIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterIpSubnet.setStatus("current")
_XsHostFilterIpMask_Type = OctetString
_XsHostFilterIpMask_Object = MibTableColumn
xsHostFilterIpMask = _XsHostFilterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 4),
    _XsHostFilterIpMask_Type()
)
xsHostFilterIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterIpMask.setStatus("current")
_XsHostFilterIpxAddress_Type = OctetString
_XsHostFilterIpxAddress_Object = MibTableColumn
xsHostFilterIpxAddress = _XsHostFilterIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 5),
    _XsHostFilterIpxAddress_Type()
)
xsHostFilterIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterIpxAddress.setStatus("current")


class _XsHostFilterStatus_Type(Integer32):
    """Custom type xsHostFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_XsHostFilterStatus_Type.__name__ = "Integer32"
_XsHostFilterStatus_Object = MibTableColumn
xsHostFilterStatus = _XsHostFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 1, 1, 6),
    _XsHostFilterStatus_Type()
)
xsHostFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterStatus.setStatus("current")


class _XsHostFilterTableClear_Type(Integer32):
    """Custom type xsHostFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("idle", 1))
    )


_XsHostFilterTableClear_Type.__name__ = "Integer32"
_XsHostFilterTableClear_Object = MibScalar
xsHostFilterTableClear = _XsHostFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 3, 2),
    _XsHostFilterTableClear_Type()
)
xsHostFilterTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsHostFilterTableClear.setStatus("current")
_XsSubnet_ObjectIdentity = ObjectIdentity
xsSubnet = _XsSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4)
)
_XsSubnetControlTable_Object = MibTable
xsSubnetControlTable = _XsSubnetControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xsSubnetControlTable.setStatus("current")
_XsSubnetControlEntry_Object = MibTableRow
xsSubnetControlEntry = _XsSubnetControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1)
)
xsSubnetControlEntry.setIndexNames(
    (0, "SMON2-MIB", "xsSubnetControlIndex"),
)
if mibBuilder.loadTexts:
    xsSubnetControlEntry.setStatus("current")


class _XsSubnetControlIndex_Type(Integer32):
    """Custom type xsSubnetControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XsSubnetControlIndex_Type.__name__ = "Integer32"
_XsSubnetControlIndex_Object = MibTableColumn
xsSubnetControlIndex = _XsSubnetControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 1),
    _XsSubnetControlIndex_Type()
)
xsSubnetControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetControlIndex.setStatus("current")
_XsSubnetControlDataSource_Type = DataSource
_XsSubnetControlDataSource_Object = MibTableColumn
xsSubnetControlDataSource = _XsSubnetControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 2),
    _XsSubnetControlDataSource_Type()
)
xsSubnetControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetControlDataSource.setStatus("current")
_XsSubnetControlInserts_Type = Counter32
_XsSubnetControlInserts_Object = MibTableColumn
xsSubnetControlInserts = _XsSubnetControlInserts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 3),
    _XsSubnetControlInserts_Type()
)
xsSubnetControlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetControlInserts.setStatus("current")
_XsSubnetControlDeletes_Type = Counter32
_XsSubnetControlDeletes_Object = MibTableColumn
xsSubnetControlDeletes = _XsSubnetControlDeletes_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 4),
    _XsSubnetControlDeletes_Type()
)
xsSubnetControlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetControlDeletes.setStatus("current")


class _XsSubnetControlMaxDesiredEntries_Type(Integer32):
    """Custom type xsSubnetControlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XsSubnetControlMaxDesiredEntries_Type.__name__ = "Integer32"
_XsSubnetControlMaxDesiredEntries_Object = MibTableColumn
xsSubnetControlMaxDesiredEntries = _XsSubnetControlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 5),
    _XsSubnetControlMaxDesiredEntries_Type()
)
xsSubnetControlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetControlMaxDesiredEntries.setStatus("current")
_XsSubnetControlOwner_Type = OwnerString
_XsSubnetControlOwner_Object = MibTableColumn
xsSubnetControlOwner = _XsSubnetControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 6),
    _XsSubnetControlOwner_Type()
)
xsSubnetControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetControlOwner.setStatus("current")
_XsSubnetControlStatus_Type = RowStatus
_XsSubnetControlStatus_Object = MibTableColumn
xsSubnetControlStatus = _XsSubnetControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 1, 1, 7),
    _XsSubnetControlStatus_Type()
)
xsSubnetControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetControlStatus.setStatus("current")
_XsSubnetTable_Object = MibTable
xsSubnetTable = _XsSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2)
)
if mibBuilder.loadTexts:
    xsSubnetTable.setStatus("current")
_XsSubnetEntry_Object = MibTableRow
xsSubnetEntry = _XsSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1)
)
xsSubnetEntry.setIndexNames(
    (0, "SMON2-MIB", "xsSubnetControlIndex"),
    (0, "SMON2-MIB", "xsSubnetTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "SMON2-MIB", "xsSubnetAddress"),
    (0, "SMON2-MIB", "xsSubnetMask"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    xsSubnetEntry.setStatus("current")
_XsSubnetTimeMark_Type = TimeFilter
_XsSubnetTimeMark_Object = MibTableColumn
xsSubnetTimeMark = _XsSubnetTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 1),
    _XsSubnetTimeMark_Type()
)
xsSubnetTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetTimeMark.setStatus("current")
_XsSubnetAddress_Type = OctetString
_XsSubnetAddress_Object = MibTableColumn
xsSubnetAddress = _XsSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 2),
    _XsSubnetAddress_Type()
)
xsSubnetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetAddress.setStatus("current")
_XsSubnetMask_Type = OctetString
_XsSubnetMask_Object = MibTableColumn
xsSubnetMask = _XsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 3),
    _XsSubnetMask_Type()
)
xsSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMask.setStatus("current")
_XsSubnetInPkts_Type = ZeroBasedCounter32
_XsSubnetInPkts_Object = MibTableColumn
xsSubnetInPkts = _XsSubnetInPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 4),
    _XsSubnetInPkts_Type()
)
xsSubnetInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetInPkts.setStatus("current")
_XsSubnetOutPkts_Type = ZeroBasedCounter32
_XsSubnetOutPkts_Object = MibTableColumn
xsSubnetOutPkts = _XsSubnetOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 5),
    _XsSubnetOutPkts_Type()
)
xsSubnetOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetOutPkts.setStatus("current")
_XsSubnetCreateTime_Type = LastCreateTime
_XsSubnetCreateTime_Object = MibTableColumn
xsSubnetCreateTime = _XsSubnetCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 2, 1, 6),
    _XsSubnetCreateTime_Type()
)
xsSubnetCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetCreateTime.setStatus("current")
_XsSubnetMatrixControlTable_Object = MibTable
xsSubnetMatrixControlTable = _XsSubnetMatrixControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3)
)
if mibBuilder.loadTexts:
    xsSubnetMatrixControlTable.setStatus("current")
_XsSubnetMatrixControlEntry_Object = MibTableRow
xsSubnetMatrixControlEntry = _XsSubnetMatrixControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1)
)
xsSubnetMatrixControlEntry.setIndexNames(
    (0, "SMON2-MIB", "xsSubnetMatrixControlIndex"),
)
if mibBuilder.loadTexts:
    xsSubnetMatrixControlEntry.setStatus("current")


class _XsSubnetMatrixControlIndex_Type(Integer32):
    """Custom type xsSubnetMatrixControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XsSubnetMatrixControlIndex_Type.__name__ = "Integer32"
_XsSubnetMatrixControlIndex_Object = MibTableColumn
xsSubnetMatrixControlIndex = _XsSubnetMatrixControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 1),
    _XsSubnetMatrixControlIndex_Type()
)
xsSubnetMatrixControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlIndex.setStatus("current")
_XsSubnetMatrixControlDataSource_Type = DataSource
_XsSubnetMatrixControlDataSource_Object = MibTableColumn
xsSubnetMatrixControlDataSource = _XsSubnetMatrixControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 2),
    _XsSubnetMatrixControlDataSource_Type()
)
xsSubnetMatrixControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlDataSource.setStatus("current")
_XsSubnetMatrixControlInserts_Type = Counter32
_XsSubnetMatrixControlInserts_Object = MibTableColumn
xsSubnetMatrixControlInserts = _XsSubnetMatrixControlInserts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 4),
    _XsSubnetMatrixControlInserts_Type()
)
xsSubnetMatrixControlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlInserts.setStatus("current")
_XsSubnetMatrixControlDeletes_Type = Counter32
_XsSubnetMatrixControlDeletes_Object = MibTableColumn
xsSubnetMatrixControlDeletes = _XsSubnetMatrixControlDeletes_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 5),
    _XsSubnetMatrixControlDeletes_Type()
)
xsSubnetMatrixControlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlDeletes.setStatus("current")


class _XsSubnetMatrixControlMaxDesiredEntries_Type(Integer32):
    """Custom type xsSubnetMatrixControlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XsSubnetMatrixControlMaxDesiredEntries_Type.__name__ = "Integer32"
_XsSubnetMatrixControlMaxDesiredEntries_Object = MibTableColumn
xsSubnetMatrixControlMaxDesiredEntries = _XsSubnetMatrixControlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 6),
    _XsSubnetMatrixControlMaxDesiredEntries_Type()
)
xsSubnetMatrixControlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlMaxDesiredEntries.setStatus("current")
_XsSubnetMatrixControlOwner_Type = OwnerString
_XsSubnetMatrixControlOwner_Object = MibTableColumn
xsSubnetMatrixControlOwner = _XsSubnetMatrixControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 7),
    _XsSubnetMatrixControlOwner_Type()
)
xsSubnetMatrixControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlOwner.setStatus("current")
_XsSubnetMatrixControlStatus_Type = RowStatus
_XsSubnetMatrixControlStatus_Object = MibTableColumn
xsSubnetMatrixControlStatus = _XsSubnetMatrixControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 3, 1, 8),
    _XsSubnetMatrixControlStatus_Type()
)
xsSubnetMatrixControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xsSubnetMatrixControlStatus.setStatus("current")
_XsSubnetMatrixSDTable_Object = MibTable
xsSubnetMatrixSDTable = _XsSubnetMatrixSDTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4)
)
if mibBuilder.loadTexts:
    xsSubnetMatrixSDTable.setStatus("current")
_XsSubnetMatrixSDEntry_Object = MibTableRow
xsSubnetMatrixSDEntry = _XsSubnetMatrixSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1)
)
xsSubnetMatrixSDEntry.setIndexNames(
    (0, "SMON2-MIB", "xsSubnetMatrixControlIndex"),
    (0, "SMON2-MIB", "xsSubnetMatrixSDTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "SMON2-MIB", "xsSubnetMatrixSDSourceAddress"),
    (0, "SMON2-MIB", "xsSubnetMatrixSDSourceMask"),
    (0, "SMON2-MIB", "xsSubnetMatrixSDDestAddress"),
    (0, "SMON2-MIB", "xsSubnetMatrixSDDestMask"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    xsSubnetMatrixSDEntry.setStatus("current")
_XsSubnetMatrixSDTimeMark_Type = TimeFilter
_XsSubnetMatrixSDTimeMark_Object = MibTableColumn
xsSubnetMatrixSDTimeMark = _XsSubnetMatrixSDTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 1),
    _XsSubnetMatrixSDTimeMark_Type()
)
xsSubnetMatrixSDTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDTimeMark.setStatus("current")
_XsSubnetMatrixSDSourceAddress_Type = OctetString
_XsSubnetMatrixSDSourceAddress_Object = MibTableColumn
xsSubnetMatrixSDSourceAddress = _XsSubnetMatrixSDSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 2),
    _XsSubnetMatrixSDSourceAddress_Type()
)
xsSubnetMatrixSDSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDSourceAddress.setStatus("current")
_XsSubnetMatrixSDSourceMask_Type = OctetString
_XsSubnetMatrixSDSourceMask_Object = MibTableColumn
xsSubnetMatrixSDSourceMask = _XsSubnetMatrixSDSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 3),
    _XsSubnetMatrixSDSourceMask_Type()
)
xsSubnetMatrixSDSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDSourceMask.setStatus("current")
_XsSubnetMatrixSDDestAddress_Type = OctetString
_XsSubnetMatrixSDDestAddress_Object = MibTableColumn
xsSubnetMatrixSDDestAddress = _XsSubnetMatrixSDDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 4),
    _XsSubnetMatrixSDDestAddress_Type()
)
xsSubnetMatrixSDDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDDestAddress.setStatus("current")
_XsSubnetMatrixSDDestMask_Type = OctetString
_XsSubnetMatrixSDDestMask_Object = MibTableColumn
xsSubnetMatrixSDDestMask = _XsSubnetMatrixSDDestMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 5),
    _XsSubnetMatrixSDDestMask_Type()
)
xsSubnetMatrixSDDestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDDestMask.setStatus("current")
_XsSubnetMatrixSDPkts_Type = ZeroBasedCounter32
_XsSubnetMatrixSDPkts_Object = MibTableColumn
xsSubnetMatrixSDPkts = _XsSubnetMatrixSDPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 6),
    _XsSubnetMatrixSDPkts_Type()
)
xsSubnetMatrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDPkts.setStatus("current")
_XsSubnetMatrixSDCreateTime_Type = LastCreateTime
_XsSubnetMatrixSDCreateTime_Object = MibTableColumn
xsSubnetMatrixSDCreateTime = _XsSubnetMatrixSDCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 4, 1, 7),
    _XsSubnetMatrixSDCreateTime_Type()
)
xsSubnetMatrixSDCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixSDCreateTime.setStatus("current")
_XsSubnetMatrixDSTable_Object = MibTable
xsSubnetMatrixDSTable = _XsSubnetMatrixDSTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5)
)
if mibBuilder.loadTexts:
    xsSubnetMatrixDSTable.setStatus("current")
_XsSubnetMatrixDSEntry_Object = MibTableRow
xsSubnetMatrixDSEntry = _XsSubnetMatrixDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1)
)
xsSubnetMatrixDSEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "SMON2-MIB", "xsSubnetMatrixDSTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "SMON2-MIB", "xsSubnetMatrixDSDestAddress"),
    (0, "SMON2-MIB", "xsSubnetMatrixDSDestMask"),
    (0, "SMON2-MIB", "xsSubnetMatrixDSSourceAddress"),
    (0, "SMON2-MIB", "xsSubnetMatrixDSSourceMask"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    xsSubnetMatrixDSEntry.setStatus("current")
_XsSubnetMatrixDSTimeMark_Type = TimeFilter
_XsSubnetMatrixDSTimeMark_Object = MibTableColumn
xsSubnetMatrixDSTimeMark = _XsSubnetMatrixDSTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 1),
    _XsSubnetMatrixDSTimeMark_Type()
)
xsSubnetMatrixDSTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSTimeMark.setStatus("current")
_XsSubnetMatrixDSSourceAddress_Type = OctetString
_XsSubnetMatrixDSSourceAddress_Object = MibTableColumn
xsSubnetMatrixDSSourceAddress = _XsSubnetMatrixDSSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 2),
    _XsSubnetMatrixDSSourceAddress_Type()
)
xsSubnetMatrixDSSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSSourceAddress.setStatus("current")
_XsSubnetMatrixDSSourceMask_Type = OctetString
_XsSubnetMatrixDSSourceMask_Object = MibTableColumn
xsSubnetMatrixDSSourceMask = _XsSubnetMatrixDSSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 3),
    _XsSubnetMatrixDSSourceMask_Type()
)
xsSubnetMatrixDSSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSSourceMask.setStatus("current")
_XsSubnetMatrixDSDestAddress_Type = OctetString
_XsSubnetMatrixDSDestAddress_Object = MibTableColumn
xsSubnetMatrixDSDestAddress = _XsSubnetMatrixDSDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 4),
    _XsSubnetMatrixDSDestAddress_Type()
)
xsSubnetMatrixDSDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSDestAddress.setStatus("current")
_XsSubnetMatrixDSDestMask_Type = OctetString
_XsSubnetMatrixDSDestMask_Object = MibTableColumn
xsSubnetMatrixDSDestMask = _XsSubnetMatrixDSDestMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 5),
    _XsSubnetMatrixDSDestMask_Type()
)
xsSubnetMatrixDSDestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSDestMask.setStatus("current")
_XsSubnetMatrixDSPkts_Type = ZeroBasedCounter32
_XsSubnetMatrixDSPkts_Object = MibTableColumn
xsSubnetMatrixDSPkts = _XsSubnetMatrixDSPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 6),
    _XsSubnetMatrixDSPkts_Type()
)
xsSubnetMatrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSPkts.setStatus("current")
_XsSubnetMatrixDSCreateTime_Type = LastCreateTime
_XsSubnetMatrixDSCreateTime_Object = MibTableColumn
xsSubnetMatrixDSCreateTime = _XsSubnetMatrixDSCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 4, 5, 1, 7),
    _XsSubnetMatrixDSCreateTime_Type()
)
xsSubnetMatrixDSCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetMatrixDSCreateTime.setStatus("current")
_XsNumberOfProtocols_Type = Integer32
_XsNumberOfProtocols_Object = MibScalar
xsNumberOfProtocols = _XsNumberOfProtocols_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 5),
    _XsNumberOfProtocols_Type()
)
xsNumberOfProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsNumberOfProtocols.setStatus("current")
_XsProtocolDistStatsTimeStamp_Type = TimeTicks
_XsProtocolDistStatsTimeStamp_Object = MibScalar
xsProtocolDistStatsTimeStamp = _XsProtocolDistStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 6),
    _XsProtocolDistStatsTimeStamp_Type()
)
xsProtocolDistStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsProtocolDistStatsTimeStamp.setStatus("current")
_XsNlHostTimeStamp_Type = TimeTicks
_XsNlHostTimeStamp_Object = MibScalar
xsNlHostTimeStamp = _XsNlHostTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 7),
    _XsNlHostTimeStamp_Type()
)
xsNlHostTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsNlHostTimeStamp.setStatus("current")
_XsSubnetStatsTimeStamp_Type = TimeTicks
_XsSubnetStatsTimeStamp_Object = MibScalar
xsSubnetStatsTimeStamp = _XsSubnetStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 8),
    _XsSubnetStatsTimeStamp_Type()
)
xsSubnetStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsSubnetStatsTimeStamp.setStatus("current")
_XsActiveApplications_ObjectIdentity = ObjectIdentity
xsActiveApplications = _XsActiveApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9)
)


class _XsActiveApplicationsBitMask_Type(OctetString):
    """Custom type xsActiveApplicationsBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_XsActiveApplicationsBitMask_Type.__name__ = "OctetString"
_XsActiveApplicationsBitMask_Object = MibScalar
xsActiveApplicationsBitMask = _XsActiveApplicationsBitMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9, 1),
    _XsActiveApplicationsBitMask_Type()
)
xsActiveApplicationsBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsActiveApplicationsBitMask.setStatus("current")
_XsActiveApplicationsTable_Object = MibTable
xsActiveApplicationsTable = _XsActiveApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9, 2)
)
if mibBuilder.loadTexts:
    xsActiveApplicationsTable.setStatus("current")
_XsActiveApplicationsEntry_Object = MibTableRow
xsActiveApplicationsEntry = _XsActiveApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9, 2, 1)
)
xsActiveApplicationsEntry.setIndexNames(
    (0, "SMON2-MIB", "xsActiveApplicationsIndex"),
)
if mibBuilder.loadTexts:
    xsActiveApplicationsEntry.setStatus("current")
_XsActiveApplicationsIndex_Type = Integer32
_XsActiveApplicationsIndex_Object = MibTableColumn
xsActiveApplicationsIndex = _XsActiveApplicationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9, 2, 1, 1),
    _XsActiveApplicationsIndex_Type()
)
xsActiveApplicationsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xsActiveApplicationsIndex.setStatus("current")
_XsActiveApplicationsPkts_Type = Counter32
_XsActiveApplicationsPkts_Object = MibTableColumn
xsActiveApplicationsPkts = _XsActiveApplicationsPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 9, 2, 1, 2),
    _XsActiveApplicationsPkts_Type()
)
xsActiveApplicationsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xsActiveApplicationsPkts.setStatus("current")


class _XsSmonStatus_Type(Integer32):
    """Custom type xsSmonStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operate", 1),
          ("paused", 2))
    )


_XsSmonStatus_Type.__name__ = "Integer32"
_XsSmonStatus_Object = MibScalar
xsSmonStatus = _XsSmonStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 2, 10),
    _XsSmonStatus_Type()
)
xsSmonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsSmonStatus.setStatus("current")
_DrSmon_ObjectIdentity = ObjectIdentity
drSmon = _DrSmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 4)
)
_DrSmonConfiguration_ObjectIdentity = ObjectIdentity
drSmonConfiguration = _DrSmonConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1)
)
_DrSmonControlTable_Object = MibTable
drSmonControlTable = _DrSmonControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1)
)
if mibBuilder.loadTexts:
    drSmonControlTable.setStatus("current")
_DrSmonControlEntry_Object = MibTableRow
drSmonControlEntry = _DrSmonControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1)
)
drSmonControlEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonControlModuleID"),
)
if mibBuilder.loadTexts:
    drSmonControlEntry.setStatus("current")


class _DrSmonControlModuleID_Type(Integer32):
    """Custom type drSmonControlModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonControlModuleID_Type.__name__ = "Integer32"
_DrSmonControlModuleID_Object = MibTableColumn
drSmonControlModuleID = _DrSmonControlModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 1),
    _DrSmonControlModuleID_Type()
)
drSmonControlModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonControlModuleID.setStatus("current")


class _DrSmonControlRowAddressAutoLearnMode_Type(Integer32):
    """Custom type drSmonControlRowAddressAutoLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 255))
    )


_DrSmonControlRowAddressAutoLearnMode_Type.__name__ = "Integer32"
_DrSmonControlRowAddressAutoLearnMode_Object = MibTableColumn
drSmonControlRowAddressAutoLearnMode = _DrSmonControlRowAddressAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 2),
    _DrSmonControlRowAddressAutoLearnMode_Type()
)
drSmonControlRowAddressAutoLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drSmonControlRowAddressAutoLearnMode.setStatus("current")
_DrSmonControlRoutedPackets_Type = Counter32
_DrSmonControlRoutedPackets_Object = MibTableColumn
drSmonControlRoutedPackets = _DrSmonControlRoutedPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 3),
    _DrSmonControlRoutedPackets_Type()
)
drSmonControlRoutedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonControlRoutedPackets.setStatus("current")
_DrSmonControlProtocolDistStatsTimeStamp_Type = TimeTicks
_DrSmonControlProtocolDistStatsTimeStamp_Object = MibTableColumn
drSmonControlProtocolDistStatsTimeStamp = _DrSmonControlProtocolDistStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 4),
    _DrSmonControlProtocolDistStatsTimeStamp_Type()
)
drSmonControlProtocolDistStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonControlProtocolDistStatsTimeStamp.setStatus("current")


class _DrSmonControlMatrixRows_Type(Integer32):
    """Custom type drSmonControlMatrixRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DrSmonControlMatrixRows_Type.__name__ = "Integer32"
_DrSmonControlMatrixRows_Object = MibTableColumn
drSmonControlMatrixRows = _DrSmonControlMatrixRows_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 5),
    _DrSmonControlMatrixRows_Type()
)
drSmonControlMatrixRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonControlMatrixRows.setStatus("current")


class _DrSmonControlMatrixCols_Type(Integer32):
    """Custom type drSmonControlMatrixCols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DrSmonControlMatrixCols_Type.__name__ = "Integer32"
_DrSmonControlMatrixCols_Object = MibTableColumn
drSmonControlMatrixCols = _DrSmonControlMatrixCols_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 1, 1, 6),
    _DrSmonControlMatrixCols_Type()
)
drSmonControlMatrixCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonControlMatrixCols.setStatus("current")
_DrSmonEntityPlacementTable_Object = MibTable
drSmonEntityPlacementTable = _DrSmonEntityPlacementTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2)
)
if mibBuilder.loadTexts:
    drSmonEntityPlacementTable.setStatus("current")
_DrSmonEntityPlacementEntry_Object = MibTableRow
drSmonEntityPlacementEntry = _DrSmonEntityPlacementEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1)
)
drSmonEntityPlacementEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonEntityPlacementModuleID"),
    (0, "SMON2-MIB", "drSmonEntityPlacementIndex"),
)
if mibBuilder.loadTexts:
    drSmonEntityPlacementEntry.setStatus("current")


class _DrSmonEntityPlacementModuleID_Type(Integer32):
    """Custom type drSmonEntityPlacementModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonEntityPlacementModuleID_Type.__name__ = "Integer32"
_DrSmonEntityPlacementModuleID_Object = MibTableColumn
drSmonEntityPlacementModuleID = _DrSmonEntityPlacementModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1, 1),
    _DrSmonEntityPlacementModuleID_Type()
)
drSmonEntityPlacementModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonEntityPlacementModuleID.setStatus("current")


class _DrSmonEntityPlacementIndex_Type(Integer32):
    """Custom type drSmonEntityPlacementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DrSmonEntityPlacementIndex_Type.__name__ = "Integer32"
_DrSmonEntityPlacementIndex_Object = MibTableColumn
drSmonEntityPlacementIndex = _DrSmonEntityPlacementIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1, 2),
    _DrSmonEntityPlacementIndex_Type()
)
drSmonEntityPlacementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonEntityPlacementIndex.setStatus("current")
_DrSmonEntityPlacementAddress_Type = IpAddress
_DrSmonEntityPlacementAddress_Object = MibTableColumn
drSmonEntityPlacementAddress = _DrSmonEntityPlacementAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1, 3),
    _DrSmonEntityPlacementAddress_Type()
)
drSmonEntityPlacementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonEntityPlacementAddress.setStatus("current")
_DrSmonEntityPlacementMask_Type = IpAddress
_DrSmonEntityPlacementMask_Object = MibTableColumn
drSmonEntityPlacementMask = _DrSmonEntityPlacementMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1, 4),
    _DrSmonEntityPlacementMask_Type()
)
drSmonEntityPlacementMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonEntityPlacementMask.setStatus("current")


class _DrSmonEntityPlacementType_Type(Integer32):
    """Custom type drSmonEntityPlacementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 2),
          ("empty", 1),
          ("filter", 3))
    )


_DrSmonEntityPlacementType_Type.__name__ = "Integer32"
_DrSmonEntityPlacementType_Object = MibTableColumn
drSmonEntityPlacementType = _DrSmonEntityPlacementType_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 1, 2, 1, 5),
    _DrSmonEntityPlacementType_Type()
)
drSmonEntityPlacementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonEntityPlacementType.setStatus("current")
_DrSmonProtocolDir_ObjectIdentity = ObjectIdentity
drSmonProtocolDir = _DrSmonProtocolDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2)
)
_DrSmonProtocolDirLCTable_Object = MibTable
drSmonProtocolDirLCTable = _DrSmonProtocolDirLCTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 1)
)
if mibBuilder.loadTexts:
    drSmonProtocolDirLCTable.setStatus("current")
_DrSmonProtocolDirLCEntry_Object = MibTableRow
drSmonProtocolDirLCEntry = _DrSmonProtocolDirLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 1, 1)
)
drSmonProtocolDirLCEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonProtocolDirLCModuleID"),
)
if mibBuilder.loadTexts:
    drSmonProtocolDirLCEntry.setStatus("current")


class _DrSmonProtocolDirLCModuleID_Type(Integer32):
    """Custom type drSmonProtocolDirLCModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonProtocolDirLCModuleID_Type.__name__ = "Integer32"
_DrSmonProtocolDirLCModuleID_Object = MibTableColumn
drSmonProtocolDirLCModuleID = _DrSmonProtocolDirLCModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 1, 1, 1),
    _DrSmonProtocolDirLCModuleID_Type()
)
drSmonProtocolDirLCModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonProtocolDirLCModuleID.setStatus("current")
_DrSmonProtocolDirLCLastChange_Type = TimeStamp
_DrSmonProtocolDirLCLastChange_Object = MibTableColumn
drSmonProtocolDirLCLastChange = _DrSmonProtocolDirLCLastChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 1, 1, 2),
    _DrSmonProtocolDirLCLastChange_Type()
)
drSmonProtocolDirLCLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonProtocolDirLCLastChange.setStatus("current")
_DrSmonProtocolDirTable_Object = MibTable
drSmonProtocolDirTable = _DrSmonProtocolDirTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2)
)
if mibBuilder.loadTexts:
    drSmonProtocolDirTable.setStatus("current")
_DrSmonProtocolDirEntry_Object = MibTableRow
drSmonProtocolDirEntry = _DrSmonProtocolDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1)
)
drSmonProtocolDirEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonProtocolDirModuleID"),
    (0, "SMON2-MIB", "drSmonProtocolDirID"),
    (0, "SMON2-MIB", "drSmonProtocolDirParameters"),
)
if mibBuilder.loadTexts:
    drSmonProtocolDirEntry.setStatus("current")


class _DrSmonProtocolDirModuleID_Type(Integer32):
    """Custom type drSmonProtocolDirModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonProtocolDirModuleID_Type.__name__ = "Integer32"
_DrSmonProtocolDirModuleID_Object = MibTableColumn
drSmonProtocolDirModuleID = _DrSmonProtocolDirModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 1),
    _DrSmonProtocolDirModuleID_Type()
)
drSmonProtocolDirModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonProtocolDirModuleID.setStatus("current")
_DrSmonProtocolDirID_Type = OctetString
_DrSmonProtocolDirID_Object = MibTableColumn
drSmonProtocolDirID = _DrSmonProtocolDirID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 2),
    _DrSmonProtocolDirID_Type()
)
drSmonProtocolDirID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonProtocolDirID.setStatus("current")
_DrSmonProtocolDirParameters_Type = OctetString
_DrSmonProtocolDirParameters_Object = MibTableColumn
drSmonProtocolDirParameters = _DrSmonProtocolDirParameters_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 3),
    _DrSmonProtocolDirParameters_Type()
)
drSmonProtocolDirParameters.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonProtocolDirParameters.setStatus("current")


class _DrSmonProtocolDirLocalIndex_Type(Integer32):
    """Custom type drSmonProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DrSmonProtocolDirLocalIndex_Type.__name__ = "Integer32"
_DrSmonProtocolDirLocalIndex_Object = MibTableColumn
drSmonProtocolDirLocalIndex = _DrSmonProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 4),
    _DrSmonProtocolDirLocalIndex_Type()
)
drSmonProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonProtocolDirLocalIndex.setStatus("current")


class _DrSmonProtocolDirDescr_Type(DisplayString):
    """Custom type drSmonProtocolDirDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DrSmonProtocolDirDescr_Type.__name__ = "DisplayString"
_DrSmonProtocolDirDescr_Object = MibTableColumn
drSmonProtocolDirDescr = _DrSmonProtocolDirDescr_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 5),
    _DrSmonProtocolDirDescr_Type()
)
drSmonProtocolDirDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirDescr.setStatus("current")


class _DrSmonProtocolDirType_Type(Bits):
    """Custom type drSmonProtocolDirType based on Bits"""
    namedValues = NamedValues(
        *(("addressRecognitionCapable", 1),
          ("extensible", 0))
    )

_DrSmonProtocolDirType_Type.__name__ = "Bits"
_DrSmonProtocolDirType_Object = MibTableColumn
drSmonProtocolDirType = _DrSmonProtocolDirType_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 6),
    _DrSmonProtocolDirType_Type()
)
drSmonProtocolDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonProtocolDirType.setStatus("current")


class _DrSmonProtocolDirAddressMapConfig_Type(Integer32):
    """Custom type drSmonProtocolDirAddressMapConfig based on Integer32"""
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


_DrSmonProtocolDirAddressMapConfig_Type.__name__ = "Integer32"
_DrSmonProtocolDirAddressMapConfig_Object = MibTableColumn
drSmonProtocolDirAddressMapConfig = _DrSmonProtocolDirAddressMapConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 7),
    _DrSmonProtocolDirAddressMapConfig_Type()
)
drSmonProtocolDirAddressMapConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirAddressMapConfig.setStatus("current")


class _DrSmonProtocolDirHostConfig_Type(Integer32):
    """Custom type drSmonProtocolDirHostConfig based on Integer32"""
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


_DrSmonProtocolDirHostConfig_Type.__name__ = "Integer32"
_DrSmonProtocolDirHostConfig_Object = MibTableColumn
drSmonProtocolDirHostConfig = _DrSmonProtocolDirHostConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 8),
    _DrSmonProtocolDirHostConfig_Type()
)
drSmonProtocolDirHostConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirHostConfig.setStatus("current")


class _DrSmonProtocolDirMatrixConfig_Type(Integer32):
    """Custom type drSmonProtocolDirMatrixConfig based on Integer32"""
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


_DrSmonProtocolDirMatrixConfig_Type.__name__ = "Integer32"
_DrSmonProtocolDirMatrixConfig_Object = MibTableColumn
drSmonProtocolDirMatrixConfig = _DrSmonProtocolDirMatrixConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 9),
    _DrSmonProtocolDirMatrixConfig_Type()
)
drSmonProtocolDirMatrixConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirMatrixConfig.setStatus("current")
_DrSmonProtocolDirOwner_Type = OwnerString
_DrSmonProtocolDirOwner_Object = MibTableColumn
drSmonProtocolDirOwner = _DrSmonProtocolDirOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 10),
    _DrSmonProtocolDirOwner_Type()
)
drSmonProtocolDirOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirOwner.setStatus("current")
_DrSmonProtocolDirStatus_Type = RowStatus
_DrSmonProtocolDirStatus_Object = MibTableColumn
drSmonProtocolDirStatus = _DrSmonProtocolDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 2, 2, 1, 11),
    _DrSmonProtocolDirStatus_Type()
)
drSmonProtocolDirStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonProtocolDirStatus.setStatus("current")
_DrSmonFilter_ObjectIdentity = ObjectIdentity
drSmonFilter = _DrSmonFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3)
)
_DrSmonFilterTable_Object = MibTable
drSmonFilterTable = _DrSmonFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1)
)
if mibBuilder.loadTexts:
    drSmonFilterTable.setStatus("current")
_DrSmonFilterEntry_Object = MibTableRow
drSmonFilterEntry = _DrSmonFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1)
)
drSmonFilterEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonFilterModuleID"),
    (0, "SMON2-MIB", "drSmonFilterIndex"),
)
if mibBuilder.loadTexts:
    drSmonFilterEntry.setStatus("current")


class _DrSmonFilterModuleID_Type(Integer32):
    """Custom type drSmonFilterModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonFilterModuleID_Type.__name__ = "Integer32"
_DrSmonFilterModuleID_Object = MibTableColumn
drSmonFilterModuleID = _DrSmonFilterModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1, 1),
    _DrSmonFilterModuleID_Type()
)
drSmonFilterModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonFilterModuleID.setStatus("current")


class _DrSmonFilterIndex_Type(Integer32):
    """Custom type drSmonFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DrSmonFilterIndex_Type.__name__ = "Integer32"
_DrSmonFilterIndex_Object = MibTableColumn
drSmonFilterIndex = _DrSmonFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1, 2),
    _DrSmonFilterIndex_Type()
)
drSmonFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonFilterIndex.setStatus("current")
_DrSmonFilterAddress_Type = IpAddress
_DrSmonFilterAddress_Object = MibTableColumn
drSmonFilterAddress = _DrSmonFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1, 3),
    _DrSmonFilterAddress_Type()
)
drSmonFilterAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonFilterAddress.setStatus("current")
_DrSmonFilterMask_Type = IpAddress
_DrSmonFilterMask_Object = MibTableColumn
drSmonFilterMask = _DrSmonFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1, 4),
    _DrSmonFilterMask_Type()
)
drSmonFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonFilterMask.setStatus("current")
_DrSmonFilterStatus_Type = RowStatus
_DrSmonFilterStatus_Object = MibTableColumn
drSmonFilterStatus = _DrSmonFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 3, 1, 1, 5),
    _DrSmonFilterStatus_Type()
)
drSmonFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drSmonFilterStatus.setStatus("current")
_DrSmonActiveApplications_ObjectIdentity = ObjectIdentity
drSmonActiveApplications = _DrSmonActiveApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4)
)
_DrSmonActiveApplicationsTable_Object = MibTable
drSmonActiveApplicationsTable = _DrSmonActiveApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1)
)
if mibBuilder.loadTexts:
    drSmonActiveApplicationsTable.setStatus("current")
_DrSmonActiveApplicationsEntry_Object = MibTableRow
drSmonActiveApplicationsEntry = _DrSmonActiveApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1, 1)
)
drSmonActiveApplicationsEntry.setIndexNames(
    (0, "SMON2-MIB", "drSmonActiveApplicationsModuleID"),
    (0, "SMON2-MIB", "drSmonActiveApplicationsType"),
    (0, "SMON2-MIB", "drSmonActiveApplicationsSubType"),
)
if mibBuilder.loadTexts:
    drSmonActiveApplicationsEntry.setStatus("current")


class _DrSmonActiveApplicationsModuleID_Type(Integer32):
    """Custom type drSmonActiveApplicationsModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrSmonActiveApplicationsModuleID_Type.__name__ = "Integer32"
_DrSmonActiveApplicationsModuleID_Object = MibTableColumn
drSmonActiveApplicationsModuleID = _DrSmonActiveApplicationsModuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1, 1, 1),
    _DrSmonActiveApplicationsModuleID_Type()
)
drSmonActiveApplicationsModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonActiveApplicationsModuleID.setStatus("current")


class _DrSmonActiveApplicationsType_Type(Integer32):
    """Custom type drSmonActiveApplicationsType based on Integer32"""
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
        *(("ethertype", 1),
          ("ipProtocol", 2),
          ("tcpProtocol", 4),
          ("udpProtocol", 3))
    )


_DrSmonActiveApplicationsType_Type.__name__ = "Integer32"
_DrSmonActiveApplicationsType_Object = MibTableColumn
drSmonActiveApplicationsType = _DrSmonActiveApplicationsType_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1, 1, 2),
    _DrSmonActiveApplicationsType_Type()
)
drSmonActiveApplicationsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonActiveApplicationsType.setStatus("current")
_DrSmonActiveApplicationsSubType_Type = Integer32
_DrSmonActiveApplicationsSubType_Object = MibTableColumn
drSmonActiveApplicationsSubType = _DrSmonActiveApplicationsSubType_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1, 1, 3),
    _DrSmonActiveApplicationsSubType_Type()
)
drSmonActiveApplicationsSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drSmonActiveApplicationsSubType.setStatus("current")
_DrSmonActiveApplicationsPkts_Type = Counter32
_DrSmonActiveApplicationsPkts_Object = MibTableColumn
drSmonActiveApplicationsPkts = _DrSmonActiveApplicationsPkts_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 4, 4, 1, 1, 4),
    _DrSmonActiveApplicationsPkts_Type()
)
drSmonActiveApplicationsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSmonActiveApplicationsPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMON2-MIB",
    **{"xsSmon": xsSmon,
       "xsSmonResourceAllocation": xsSmonResourceAllocation,
       "xsHostTopN": xsHostTopN,
       "xsHostTopNControlTable": xsHostTopNControlTable,
       "xsHostTopNControlEntry": xsHostTopNControlEntry,
       "xsHostTopNControlIndex": xsHostTopNControlIndex,
       "xsHostTopNControlHostIndex": xsHostTopNControlHostIndex,
       "xsHostTopNControlRateBase": xsHostTopNControlRateBase,
       "xsHostTopNControlTimeRemaining": xsHostTopNControlTimeRemaining,
       "xsHostTopNControlDuration": xsHostTopNControlDuration,
       "xsHostTopNControlRequestedSize": xsHostTopNControlRequestedSize,
       "xsHostTopNControlGrantedSize": xsHostTopNControlGrantedSize,
       "xsHostTopNControlStartTime": xsHostTopNControlStartTime,
       "xsHostTopNControlOwner": xsHostTopNControlOwner,
       "xsHostTopNControlStatus": xsHostTopNControlStatus,
       "xsHostTopNTable": xsHostTopNTable,
       "xsHostTopNEntry": xsHostTopNEntry,
       "xsHostTopNIndex": xsHostTopNIndex,
       "xsHostTopNProtocolDirLocalIndex": xsHostTopNProtocolDirLocalIndex,
       "xsHostTopNNlAddress": xsHostTopNNlAddress,
       "xsHostTopNRate": xsHostTopNRate,
       "xsFilter": xsFilter,
       "xsHostFilterTable": xsHostFilterTable,
       "xsHostFilterEntry": xsHostFilterEntry,
       "xsHostFilterType": xsHostFilterType,
       "xsHostFilterIpAddress": xsHostFilterIpAddress,
       "xsHostFilterIpSubnet": xsHostFilterIpSubnet,
       "xsHostFilterIpMask": xsHostFilterIpMask,
       "xsHostFilterIpxAddress": xsHostFilterIpxAddress,
       "xsHostFilterStatus": xsHostFilterStatus,
       "xsHostFilterTableClear": xsHostFilterTableClear,
       "xsSubnet": xsSubnet,
       "xsSubnetControlTable": xsSubnetControlTable,
       "xsSubnetControlEntry": xsSubnetControlEntry,
       "xsSubnetControlIndex": xsSubnetControlIndex,
       "xsSubnetControlDataSource": xsSubnetControlDataSource,
       "xsSubnetControlInserts": xsSubnetControlInserts,
       "xsSubnetControlDeletes": xsSubnetControlDeletes,
       "xsSubnetControlMaxDesiredEntries": xsSubnetControlMaxDesiredEntries,
       "xsSubnetControlOwner": xsSubnetControlOwner,
       "xsSubnetControlStatus": xsSubnetControlStatus,
       "xsSubnetTable": xsSubnetTable,
       "xsSubnetEntry": xsSubnetEntry,
       "xsSubnetTimeMark": xsSubnetTimeMark,
       "xsSubnetAddress": xsSubnetAddress,
       "xsSubnetMask": xsSubnetMask,
       "xsSubnetInPkts": xsSubnetInPkts,
       "xsSubnetOutPkts": xsSubnetOutPkts,
       "xsSubnetCreateTime": xsSubnetCreateTime,
       "xsSubnetMatrixControlTable": xsSubnetMatrixControlTable,
       "xsSubnetMatrixControlEntry": xsSubnetMatrixControlEntry,
       "xsSubnetMatrixControlIndex": xsSubnetMatrixControlIndex,
       "xsSubnetMatrixControlDataSource": xsSubnetMatrixControlDataSource,
       "xsSubnetMatrixControlInserts": xsSubnetMatrixControlInserts,
       "xsSubnetMatrixControlDeletes": xsSubnetMatrixControlDeletes,
       "xsSubnetMatrixControlMaxDesiredEntries": xsSubnetMatrixControlMaxDesiredEntries,
       "xsSubnetMatrixControlOwner": xsSubnetMatrixControlOwner,
       "xsSubnetMatrixControlStatus": xsSubnetMatrixControlStatus,
       "xsSubnetMatrixSDTable": xsSubnetMatrixSDTable,
       "xsSubnetMatrixSDEntry": xsSubnetMatrixSDEntry,
       "xsSubnetMatrixSDTimeMark": xsSubnetMatrixSDTimeMark,
       "xsSubnetMatrixSDSourceAddress": xsSubnetMatrixSDSourceAddress,
       "xsSubnetMatrixSDSourceMask": xsSubnetMatrixSDSourceMask,
       "xsSubnetMatrixSDDestAddress": xsSubnetMatrixSDDestAddress,
       "xsSubnetMatrixSDDestMask": xsSubnetMatrixSDDestMask,
       "xsSubnetMatrixSDPkts": xsSubnetMatrixSDPkts,
       "xsSubnetMatrixSDCreateTime": xsSubnetMatrixSDCreateTime,
       "xsSubnetMatrixDSTable": xsSubnetMatrixDSTable,
       "xsSubnetMatrixDSEntry": xsSubnetMatrixDSEntry,
       "xsSubnetMatrixDSTimeMark": xsSubnetMatrixDSTimeMark,
       "xsSubnetMatrixDSSourceAddress": xsSubnetMatrixDSSourceAddress,
       "xsSubnetMatrixDSSourceMask": xsSubnetMatrixDSSourceMask,
       "xsSubnetMatrixDSDestAddress": xsSubnetMatrixDSDestAddress,
       "xsSubnetMatrixDSDestMask": xsSubnetMatrixDSDestMask,
       "xsSubnetMatrixDSPkts": xsSubnetMatrixDSPkts,
       "xsSubnetMatrixDSCreateTime": xsSubnetMatrixDSCreateTime,
       "xsNumberOfProtocols": xsNumberOfProtocols,
       "xsProtocolDistStatsTimeStamp": xsProtocolDistStatsTimeStamp,
       "xsNlHostTimeStamp": xsNlHostTimeStamp,
       "xsSubnetStatsTimeStamp": xsSubnetStatsTimeStamp,
       "xsActiveApplications": xsActiveApplications,
       "xsActiveApplicationsBitMask": xsActiveApplicationsBitMask,
       "xsActiveApplicationsTable": xsActiveApplicationsTable,
       "xsActiveApplicationsEntry": xsActiveApplicationsEntry,
       "xsActiveApplicationsIndex": xsActiveApplicationsIndex,
       "xsActiveApplicationsPkts": xsActiveApplicationsPkts,
       "xsSmonStatus": xsSmonStatus,
       "drSmon": drSmon,
       "drSmonConfiguration": drSmonConfiguration,
       "drSmonControlTable": drSmonControlTable,
       "drSmonControlEntry": drSmonControlEntry,
       "drSmonControlModuleID": drSmonControlModuleID,
       "drSmonControlRowAddressAutoLearnMode": drSmonControlRowAddressAutoLearnMode,
       "drSmonControlRoutedPackets": drSmonControlRoutedPackets,
       "drSmonControlProtocolDistStatsTimeStamp": drSmonControlProtocolDistStatsTimeStamp,
       "drSmonControlMatrixRows": drSmonControlMatrixRows,
       "drSmonControlMatrixCols": drSmonControlMatrixCols,
       "drSmonEntityPlacementTable": drSmonEntityPlacementTable,
       "drSmonEntityPlacementEntry": drSmonEntityPlacementEntry,
       "drSmonEntityPlacementModuleID": drSmonEntityPlacementModuleID,
       "drSmonEntityPlacementIndex": drSmonEntityPlacementIndex,
       "drSmonEntityPlacementAddress": drSmonEntityPlacementAddress,
       "drSmonEntityPlacementMask": drSmonEntityPlacementMask,
       "drSmonEntityPlacementType": drSmonEntityPlacementType,
       "drSmonProtocolDir": drSmonProtocolDir,
       "drSmonProtocolDirLCTable": drSmonProtocolDirLCTable,
       "drSmonProtocolDirLCEntry": drSmonProtocolDirLCEntry,
       "drSmonProtocolDirLCModuleID": drSmonProtocolDirLCModuleID,
       "drSmonProtocolDirLCLastChange": drSmonProtocolDirLCLastChange,
       "drSmonProtocolDirTable": drSmonProtocolDirTable,
       "drSmonProtocolDirEntry": drSmonProtocolDirEntry,
       "drSmonProtocolDirModuleID": drSmonProtocolDirModuleID,
       "drSmonProtocolDirID": drSmonProtocolDirID,
       "drSmonProtocolDirParameters": drSmonProtocolDirParameters,
       "drSmonProtocolDirLocalIndex": drSmonProtocolDirLocalIndex,
       "drSmonProtocolDirDescr": drSmonProtocolDirDescr,
       "drSmonProtocolDirType": drSmonProtocolDirType,
       "drSmonProtocolDirAddressMapConfig": drSmonProtocolDirAddressMapConfig,
       "drSmonProtocolDirHostConfig": drSmonProtocolDirHostConfig,
       "drSmonProtocolDirMatrixConfig": drSmonProtocolDirMatrixConfig,
       "drSmonProtocolDirOwner": drSmonProtocolDirOwner,
       "drSmonProtocolDirStatus": drSmonProtocolDirStatus,
       "drSmonFilter": drSmonFilter,
       "drSmonFilterTable": drSmonFilterTable,
       "drSmonFilterEntry": drSmonFilterEntry,
       "drSmonFilterModuleID": drSmonFilterModuleID,
       "drSmonFilterIndex": drSmonFilterIndex,
       "drSmonFilterAddress": drSmonFilterAddress,
       "drSmonFilterMask": drSmonFilterMask,
       "drSmonFilterStatus": drSmonFilterStatus,
       "drSmonActiveApplications": drSmonActiveApplications,
       "drSmonActiveApplicationsTable": drSmonActiveApplicationsTable,
       "drSmonActiveApplicationsEntry": drSmonActiveApplicationsEntry,
       "drSmonActiveApplicationsModuleID": drSmonActiveApplicationsModuleID,
       "drSmonActiveApplicationsType": drSmonActiveApplicationsType,
       "drSmonActiveApplicationsSubType": drSmonActiveApplicationsSubType,
       "drSmonActiveApplicationsPkts": drSmonActiveApplicationsPkts}
)
