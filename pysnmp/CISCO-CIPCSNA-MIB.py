# SNMP MIB module (CISCO-CIPCSNA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIPCSNA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:26 2024
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

(cipCardDtrBrdIndex,
 cipCardEntryIndex,
 cipCardSubChannelIndex) = mibBuilder.importSymbols(
    "CISCO-CHANNEL-MIB",
    "cipCardDtrBrdIndex",
    "cipCardEntryIndex",
    "cipCardSubChannelIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(llcPortVirtualIndex,
 llcSapNumber) = mibBuilder.importSymbols(
    "CISCO-SNA-LLC-MIB",
    "llcPortVirtualIndex",
    "llcSapNumber")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCipCsnaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33)
)
ciscoCipCsnaMIB.setRevisions(
        ("1998-01-06 00:00",
         "1995-08-21 00:00",
         "1995-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelPath(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class ChannelDevice(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



# MIB Managed Objects in the order of their OIDs

_CipCsnaObjects_ObjectIdentity = ObjectIdentity
cipCsnaObjects = _CipCsnaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1)
)
_CipCsnaChannel_ObjectIdentity = ObjectIdentity
cipCsnaChannel = _CipCsnaChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1)
)
_CipCardCsnaAdminTable_Object = MibTable
cipCardCsnaAdminTable = _CipCardCsnaAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipCardCsnaAdminTable.setStatus("current")
_CipCardCsnaAdminEntry_Object = MibTableRow
cipCardCsnaAdminEntry = _CipCardCsnaAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1)
)
cipCardCsnaAdminEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardCsnaAdminEntry.setStatus("current")
_CipCardCsnaAdminPath_Type = ChannelPath
_CipCardCsnaAdminPath_Object = MibTableColumn
cipCardCsnaAdminPath = _CipCardCsnaAdminPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 1),
    _CipCardCsnaAdminPath_Type()
)
cipCardCsnaAdminPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminPath.setStatus("current")
_CipCardCsnaAdminDevice_Type = ChannelDevice
_CipCardCsnaAdminDevice_Object = MibTableColumn
cipCardCsnaAdminDevice = _CipCardCsnaAdminDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 2),
    _CipCardCsnaAdminDevice_Type()
)
cipCardCsnaAdminDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminDevice.setStatus("current")


class _CipCardCsnaAdminBlockDelayTime_Type(Integer32):
    """Custom type cipCardCsnaAdminBlockDelayTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardCsnaAdminBlockDelayTime_Type.__name__ = "Integer32"
_CipCardCsnaAdminBlockDelayTime_Object = MibTableColumn
cipCardCsnaAdminBlockDelayTime = _CipCardCsnaAdminBlockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 3),
    _CipCardCsnaAdminBlockDelayTime_Type()
)
cipCardCsnaAdminBlockDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminBlockDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaAdminBlockDelayTime.setUnits("milliseconds")


class _CipCardCsnaAdminBlockDelayLength_Type(Integer32):
    """Custom type cipCardCsnaAdminBlockDelayLength based on Integer32"""
    defaultValue = 20470

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipCardCsnaAdminBlockDelayLength_Type.__name__ = "Integer32"
_CipCardCsnaAdminBlockDelayLength_Object = MibTableColumn
cipCardCsnaAdminBlockDelayLength = _CipCardCsnaAdminBlockDelayLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 4),
    _CipCardCsnaAdminBlockDelayLength_Type()
)
cipCardCsnaAdminBlockDelayLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminBlockDelayLength.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaAdminBlockDelayLength.setUnits("octets")


class _CipCardCsnaAdminMaxBlockLength_Type(Integer32):
    """Custom type cipCardCsnaAdminMaxBlockLength based on Integer32"""
    defaultValue = 20470

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65535),
    )


_CipCardCsnaAdminMaxBlockLength_Type.__name__ = "Integer32"
_CipCardCsnaAdminMaxBlockLength_Object = MibTableColumn
cipCardCsnaAdminMaxBlockLength = _CipCardCsnaAdminMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 5),
    _CipCardCsnaAdminMaxBlockLength_Type()
)
cipCardCsnaAdminMaxBlockLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminMaxBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaAdminMaxBlockLength.setUnits("octets")
_CipCardCsnaAdminRowStatus_Type = RowStatus
_CipCardCsnaAdminRowStatus_Object = MibTableColumn
cipCardCsnaAdminRowStatus = _CipCardCsnaAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 6),
    _CipCardCsnaAdminRowStatus_Type()
)
cipCardCsnaAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardCsnaAdminRowStatus.setStatus("current")
_CipCardCsnaOperTable_Object = MibTable
cipCardCsnaOperTable = _CipCardCsnaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cipCardCsnaOperTable.setStatus("current")
_CipCardCsnaOperEntry_Object = MibTableRow
cipCardCsnaOperEntry = _CipCardCsnaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1)
)
cipCardCsnaOperEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardCsnaOperEntry.setStatus("current")


class _CipCardCsnaOperState_Type(Integer32):
    """Custom type cipCardCsnaOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 2),
          ("pendingClose", 5),
          ("pendingOpen", 1),
          ("pendingSetup", 3),
          ("setupComplete", 4))
    )


_CipCardCsnaOperState_Type.__name__ = "Integer32"
_CipCardCsnaOperState_Object = MibTableColumn
cipCardCsnaOperState = _CipCardCsnaOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 1),
    _CipCardCsnaOperState_Type()
)
cipCardCsnaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaOperState.setStatus("current")


class _CipCardCsnaOperSlowDownState_Type(Integer32):
    """Custom type cipCardCsnaOperSlowDownState based on Integer32"""
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
        *(("normal", 0),
          ("slowDownReceived", 2),
          ("slowDownSent", 1),
          ("slowDownSentAndReceived", 3))
    )


_CipCardCsnaOperSlowDownState_Type.__name__ = "Integer32"
_CipCardCsnaOperSlowDownState_Object = MibTableColumn
cipCardCsnaOperSlowDownState = _CipCardCsnaOperSlowDownState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 2),
    _CipCardCsnaOperSlowDownState_Type()
)
cipCardCsnaOperSlowDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaOperSlowDownState.setStatus("current")


class _CipCardCsnaOperBlockDelayTime_Type(Integer32):
    """Custom type cipCardCsnaOperBlockDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardCsnaOperBlockDelayTime_Type.__name__ = "Integer32"
_CipCardCsnaOperBlockDelayTime_Object = MibTableColumn
cipCardCsnaOperBlockDelayTime = _CipCardCsnaOperBlockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 3),
    _CipCardCsnaOperBlockDelayTime_Type()
)
cipCardCsnaOperBlockDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaOperBlockDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaOperBlockDelayTime.setUnits("milliseconds")


class _CipCardCsnaOperBlockDelayLength_Type(Integer32):
    """Custom type cipCardCsnaOperBlockDelayLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipCardCsnaOperBlockDelayLength_Type.__name__ = "Integer32"
_CipCardCsnaOperBlockDelayLength_Object = MibTableColumn
cipCardCsnaOperBlockDelayLength = _CipCardCsnaOperBlockDelayLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 4),
    _CipCardCsnaOperBlockDelayLength_Type()
)
cipCardCsnaOperBlockDelayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaOperBlockDelayLength.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaOperBlockDelayLength.setUnits("octets")


class _CipCardCsnaOperMaxBlockLength_Type(Integer32):
    """Custom type cipCardCsnaOperMaxBlockLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65535),
    )


_CipCardCsnaOperMaxBlockLength_Type.__name__ = "Integer32"
_CipCardCsnaOperMaxBlockLength_Object = MibTableColumn
cipCardCsnaOperMaxBlockLength = _CipCardCsnaOperMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 5),
    _CipCardCsnaOperMaxBlockLength_Type()
)
cipCardCsnaOperMaxBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaOperMaxBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaOperMaxBlockLength.setUnits("octets")
_CipCardCsnaStatsTable_Object = MibTable
cipCardCsnaStatsTable = _CipCardCsnaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cipCardCsnaStatsTable.setStatus("current")
_CipCardCsnaStatsEntry_Object = MibTableRow
cipCardCsnaStatsEntry = _CipCardCsnaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1)
)
cipCardCsnaStatsEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardCsnaStatsEntry.setStatus("current")
_CipCardCsnaStatsBlocksTxd_Type = Counter32
_CipCardCsnaStatsBlocksTxd_Object = MibTableColumn
cipCardCsnaStatsBlocksTxd = _CipCardCsnaStatsBlocksTxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 1),
    _CipCardCsnaStatsBlocksTxd_Type()
)
cipCardCsnaStatsBlocksTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBlocksTxd.setStatus("current")
_CipCardCsnaStatsBlocksRxd_Type = Counter32
_CipCardCsnaStatsBlocksRxd_Object = MibTableColumn
cipCardCsnaStatsBlocksRxd = _CipCardCsnaStatsBlocksRxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 2),
    _CipCardCsnaStatsBlocksRxd_Type()
)
cipCardCsnaStatsBlocksRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBlocksRxd.setStatus("current")
_CipCardCsnaStatsBytesTxd_Type = Counter32
_CipCardCsnaStatsBytesTxd_Object = MibTableColumn
cipCardCsnaStatsBytesTxd = _CipCardCsnaStatsBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 3),
    _CipCardCsnaStatsBytesTxd_Type()
)
cipCardCsnaStatsBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesTxd.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesTxd.setUnits("octets")
_CipCardCsnaStatsHCBytesTxd_Type = Counter64
_CipCardCsnaStatsHCBytesTxd_Object = MibTableColumn
cipCardCsnaStatsHCBytesTxd = _CipCardCsnaStatsHCBytesTxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 4),
    _CipCardCsnaStatsHCBytesTxd_Type()
)
cipCardCsnaStatsHCBytesTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesTxd.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesTxd.setUnits("octets")
_CipCardCsnaStatsBytesRxd_Type = Counter32
_CipCardCsnaStatsBytesRxd_Object = MibTableColumn
cipCardCsnaStatsBytesRxd = _CipCardCsnaStatsBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 5),
    _CipCardCsnaStatsBytesRxd_Type()
)
cipCardCsnaStatsBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesRxd.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesRxd.setUnits("octets")
_CipCardCsnaStatsHCBytesRxd_Type = Counter64
_CipCardCsnaStatsHCBytesRxd_Object = MibTableColumn
cipCardCsnaStatsHCBytesRxd = _CipCardCsnaStatsHCBytesRxd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 6),
    _CipCardCsnaStatsHCBytesRxd_Type()
)
cipCardCsnaStatsHCBytesRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesRxd.setStatus("current")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesRxd.setUnits("octets")
_CipCardCsnaStatsBlocksTxByBlockDelayTime_Type = Counter32
_CipCardCsnaStatsBlocksTxByBlockDelayTime_Object = MibTableColumn
cipCardCsnaStatsBlocksTxByBlockDelayTime = _CipCardCsnaStatsBlocksTxByBlockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 7),
    _CipCardCsnaStatsBlocksTxByBlockDelayTime_Type()
)
cipCardCsnaStatsBlocksTxByBlockDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBlocksTxByBlockDelayTime.setStatus("current")
_CipCardCsnaStatsBytesTxByBlockDelayTime_Type = Counter32
_CipCardCsnaStatsBytesTxByBlockDelayTime_Object = MibTableColumn
cipCardCsnaStatsBytesTxByBlockDelayTime = _CipCardCsnaStatsBytesTxByBlockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 8),
    _CipCardCsnaStatsBytesTxByBlockDelayTime_Type()
)
cipCardCsnaStatsBytesTxByBlockDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesTxByBlockDelayTime.setStatus("current")
_CipCardCsnaStatsHCBytesTxByBlockDelayTime_Type = Counter64
_CipCardCsnaStatsHCBytesTxByBlockDelayTime_Object = MibTableColumn
cipCardCsnaStatsHCBytesTxByBlockDelayTime = _CipCardCsnaStatsHCBytesTxByBlockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 9),
    _CipCardCsnaStatsHCBytesTxByBlockDelayTime_Type()
)
cipCardCsnaStatsHCBytesTxByBlockDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesTxByBlockDelayTime.setStatus("current")
_CipCardCsnaStatsBlocksTxByBlockDelayLength_Type = Counter32
_CipCardCsnaStatsBlocksTxByBlockDelayLength_Object = MibTableColumn
cipCardCsnaStatsBlocksTxByBlockDelayLength = _CipCardCsnaStatsBlocksTxByBlockDelayLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 10),
    _CipCardCsnaStatsBlocksTxByBlockDelayLength_Type()
)
cipCardCsnaStatsBlocksTxByBlockDelayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBlocksTxByBlockDelayLength.setStatus("current")
_CipCardCsnaStatsBytesTxByBlockDelayLength_Type = Counter32
_CipCardCsnaStatsBytesTxByBlockDelayLength_Object = MibTableColumn
cipCardCsnaStatsBytesTxByBlockDelayLength = _CipCardCsnaStatsBytesTxByBlockDelayLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 11),
    _CipCardCsnaStatsBytesTxByBlockDelayLength_Type()
)
cipCardCsnaStatsBytesTxByBlockDelayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesTxByBlockDelayLength.setStatus("current")
_CipCardCsnaStatsHCBytesTxByBlockDelayLength_Type = Counter64
_CipCardCsnaStatsHCBytesTxByBlockDelayLength_Object = MibTableColumn
cipCardCsnaStatsHCBytesTxByBlockDelayLength = _CipCardCsnaStatsHCBytesTxByBlockDelayLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 12),
    _CipCardCsnaStatsHCBytesTxByBlockDelayLength_Type()
)
cipCardCsnaStatsHCBytesTxByBlockDelayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesTxByBlockDelayLength.setStatus("current")
_CipCardCsnaStatsBlocksTxByMaxBlockLength_Type = Counter32
_CipCardCsnaStatsBlocksTxByMaxBlockLength_Object = MibTableColumn
cipCardCsnaStatsBlocksTxByMaxBlockLength = _CipCardCsnaStatsBlocksTxByMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 13),
    _CipCardCsnaStatsBlocksTxByMaxBlockLength_Type()
)
cipCardCsnaStatsBlocksTxByMaxBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBlocksTxByMaxBlockLength.setStatus("current")
_CipCardCsnaStatsBytesTxByMaxBlockLength_Type = Counter32
_CipCardCsnaStatsBytesTxByMaxBlockLength_Object = MibTableColumn
cipCardCsnaStatsBytesTxByMaxBlockLength = _CipCardCsnaStatsBytesTxByMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 14),
    _CipCardCsnaStatsBytesTxByMaxBlockLength_Type()
)
cipCardCsnaStatsBytesTxByMaxBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsBytesTxByMaxBlockLength.setStatus("current")
_CipCardCsnaStatsHCBytesTxByMaxBlockLength_Type = Counter64
_CipCardCsnaStatsHCBytesTxByMaxBlockLength_Object = MibTableColumn
cipCardCsnaStatsHCBytesTxByMaxBlockLength = _CipCardCsnaStatsHCBytesTxByMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 15),
    _CipCardCsnaStatsHCBytesTxByMaxBlockLength_Type()
)
cipCardCsnaStatsHCBytesTxByMaxBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsHCBytesTxByMaxBlockLength.setStatus("current")
_CipCardCsnaStatsSlowDownsReceived_Type = Counter32
_CipCardCsnaStatsSlowDownsReceived_Object = MibTableColumn
cipCardCsnaStatsSlowDownsReceived = _CipCardCsnaStatsSlowDownsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 16),
    _CipCardCsnaStatsSlowDownsReceived_Type()
)
cipCardCsnaStatsSlowDownsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsSlowDownsReceived.setStatus("current")
_CipCardCsnaStatsSlowDownsSent_Type = Counter32
_CipCardCsnaStatsSlowDownsSent_Object = MibTableColumn
cipCardCsnaStatsSlowDownsSent = _CipCardCsnaStatsSlowDownsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 17),
    _CipCardCsnaStatsSlowDownsSent_Type()
)
cipCardCsnaStatsSlowDownsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaStatsSlowDownsSent.setStatus("current")
_CipSession_ObjectIdentity = ObjectIdentity
cipSession = _CipSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2)
)
_CipCardSessionsAdminTable_Object = MibTable
cipCardSessionsAdminTable = _CipCardSessionsAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipCardSessionsAdminTable.setStatus("current")
_CipCardSessionsAdminEntry_Object = MibTableRow
cipCardSessionsAdminEntry = _CipCardSessionsAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 1, 1)
)
cipCardSessionsAdminEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
)
if mibBuilder.loadTexts:
    cipCardSessionsAdminEntry.setStatus("current")


class _CipCardAdminMaxLlc2Sessions_Type(Integer32):
    """Custom type cipCardAdminMaxLlc2Sessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CipCardAdminMaxLlc2Sessions_Type.__name__ = "Integer32"
_CipCardAdminMaxLlc2Sessions_Object = MibTableColumn
cipCardAdminMaxLlc2Sessions = _CipCardAdminMaxLlc2Sessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 1, 1, 1),
    _CipCardAdminMaxLlc2Sessions_Type()
)
cipCardAdminMaxLlc2Sessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardAdminMaxLlc2Sessions.setStatus("current")
_CipCardSessionsOperTable_Object = MibTable
cipCardSessionsOperTable = _CipCardSessionsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipCardSessionsOperTable.setStatus("current")
_CipCardSessionsOperEntry_Object = MibTableRow
cipCardSessionsOperEntry = _CipCardSessionsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 2, 1)
)
cipCardSessionsOperEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
)
if mibBuilder.loadTexts:
    cipCardSessionsOperEntry.setStatus("current")


class _CipCardOperMaxLlc2Sessions_Type(Integer32):
    """Custom type cipCardOperMaxLlc2Sessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CipCardOperMaxLlc2Sessions_Type.__name__ = "Integer32"
_CipCardOperMaxLlc2Sessions_Object = MibTableColumn
cipCardOperMaxLlc2Sessions = _CipCardOperMaxLlc2Sessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 2, 1, 1),
    _CipCardOperMaxLlc2Sessions_Type()
)
cipCardOperMaxLlc2Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardOperMaxLlc2Sessions.setStatus("current")
_CipCardSessionsStatsTable_Object = MibTable
cipCardSessionsStatsTable = _CipCardSessionsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cipCardSessionsStatsTable.setStatus("current")
_CipCardSessionsStatsEntry_Object = MibTableRow
cipCardSessionsStatsEntry = _CipCardSessionsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1)
)
cipCardSessionsStatsEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
)
if mibBuilder.loadTexts:
    cipCardSessionsStatsEntry.setStatus("current")
_CipCardStatsHiWaterLlc2Sessions_Type = Gauge32
_CipCardStatsHiWaterLlc2Sessions_Object = MibTableColumn
cipCardStatsHiWaterLlc2Sessions = _CipCardStatsHiWaterLlc2Sessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1, 1),
    _CipCardStatsHiWaterLlc2Sessions_Type()
)
cipCardStatsHiWaterLlc2Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardStatsHiWaterLlc2Sessions.setStatus("current")
_CipCardStatsLlc2SessionAllocationErrs_Type = Counter32
_CipCardStatsLlc2SessionAllocationErrs_Object = MibTableColumn
cipCardStatsLlc2SessionAllocationErrs = _CipCardStatsLlc2SessionAllocationErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1, 2),
    _CipCardStatsLlc2SessionAllocationErrs_Type()
)
cipCardStatsLlc2SessionAllocationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardStatsLlc2SessionAllocationErrs.setStatus("current")
_CipCsnaConnection_ObjectIdentity = ObjectIdentity
cipCsnaConnection = _CipCsnaConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3)
)
_CipCardCsnaConnTable_Object = MibTable
cipCardCsnaConnTable = _CipCardCsnaConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cipCardCsnaConnTable.setStatus("current")
_CipCardCsnaConnEntry_Object = MibTableRow
cipCardCsnaConnEntry = _CipCardCsnaConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1)
)
cipCardCsnaConnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    cipCardCsnaConnEntry.setStatus("current")
_CipCardCsnaConnActiveSessions_Type = Gauge32
_CipCardCsnaConnActiveSessions_Object = MibTableColumn
cipCardCsnaConnActiveSessions = _CipCardCsnaConnActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 1),
    _CipCardCsnaConnActiveSessions_Type()
)
cipCardCsnaConnActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaConnActiveSessions.setStatus("current")
_CipCardCsnaSlot_Type = Integer32
_CipCardCsnaSlot_Object = MibTableColumn
cipCardCsnaSlot = _CipCardCsnaSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 2),
    _CipCardCsnaSlot_Type()
)
cipCardCsnaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaSlot.setStatus("current")
_CipCardCsnaPort_Type = Integer32
_CipCardCsnaPort_Object = MibTableColumn
cipCardCsnaPort = _CipCardCsnaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 3),
    _CipCardCsnaPort_Type()
)
cipCardCsnaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaPort.setStatus("current")
_CipCardCsnaConnPath_Type = ChannelPath
_CipCardCsnaConnPath_Object = MibTableColumn
cipCardCsnaConnPath = _CipCardCsnaConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 4),
    _CipCardCsnaConnPath_Type()
)
cipCardCsnaConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaConnPath.setStatus("current")
_CipCardCsnaConnDevice_Type = ChannelDevice
_CipCardCsnaConnDevice_Object = MibTableColumn
cipCardCsnaConnDevice = _CipCardCsnaConnDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 5),
    _CipCardCsnaConnDevice_Type()
)
cipCardCsnaConnDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardCsnaConnDevice.setStatus("current")
_CipCsnaNotificationPrefix_ObjectIdentity = ObjectIdentity
cipCsnaNotificationPrefix = _CipCsnaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 2)
)
_CipCsnaNotifications_ObjectIdentity = ObjectIdentity
cipCsnaNotifications = _CipCsnaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0)
)
_CiscoCipCsnaMibConformance_ObjectIdentity = ObjectIdentity
ciscoCipCsnaMibConformance = _CiscoCipCsnaMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3)
)
_CiscoCipCsnaMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCipCsnaMibCompliances = _CiscoCipCsnaMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 1)
)
_CiscoCipCsnaMibGroups_ObjectIdentity = ObjectIdentity
ciscoCipCsnaMibGroups = _CiscoCipCsnaMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2)
)

# Managed Objects groups

ciscoCsnaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 1)
)
ciscoCsnaGroup.setObjects(
      *(("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminPath"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminDevice"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminBlockDelayTime"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminBlockDelayLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminMaxBlockLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaAdminRowStatus"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaOperState"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaOperSlowDownState"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaOperBlockDelayTime"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaOperBlockDelayLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaOperMaxBlockLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBlocksTxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBlocksRxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBytesTxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsHCBytesTxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBytesRxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsHCBytesRxd"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBlocksTxByBlockDelayTime"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBytesTxByBlockDelayTime"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsHCBytesTxByBlockDelayTime"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBlocksTxByBlockDelayLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBytesTxByBlockDelayLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsHCBytesTxByBlockDelayLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBlocksTxByMaxBlockLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsBytesTxByMaxBlockLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsHCBytesTxByMaxBlockLength"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsSlowDownsSent"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaStatsSlowDownsReceived"))
)
if mibBuilder.loadTexts:
    ciscoCsnaGroup.setStatus("current")

ciscoMaxSessionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 2)
)
ciscoMaxSessionsGroup.setObjects(
      *(("CISCO-CIPCSNA-MIB", "cipCardAdminMaxLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardOperMaxLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardStatsHiWaterLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardStatsLlc2SessionAllocationErrs"))
)
if mibBuilder.loadTexts:
    ciscoMaxSessionsGroup.setStatus("current")

ciscoCsnaConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 3)
)
ciscoCsnaConnGroup.setObjects(
      *(("CISCO-CIPCSNA-MIB", "cipCardCsnaConnActiveSessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaSlot"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaPort"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaConnPath"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaConnDevice"))
)
if mibBuilder.loadTexts:
    ciscoCsnaConnGroup.setStatus("current")


# Notification objects

cipCsnaOpenDuplicateSapFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0, 1)
)
cipCsnaOpenDuplicateSapFailure.setObjects(
      *(("CISCO-CIPCSNA-MIB", "cipCardCsnaSlot"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaPort"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaConnPath"),
        ("CISCO-CIPCSNA-MIB", "cipCardCsnaConnDevice"))
)
if mibBuilder.loadTexts:
    cipCsnaOpenDuplicateSapFailure.setStatus(
        "current"
    )

cipCsnaLlc2ConnectionLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0, 2)
)
cipCsnaLlc2ConnectionLimitExceeded.setObjects(
      *(("CISCO-CIPCSNA-MIB", "cipCardAdminMaxLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardOperMaxLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardStatsHiWaterLlc2Sessions"),
        ("CISCO-CIPCSNA-MIB", "cipCardStatsLlc2SessionAllocationErrs"))
)
if mibBuilder.loadTexts:
    cipCsnaLlc2ConnectionLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCipCsnaMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCipCsnaMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIPCSNA-MIB",
    **{"ChannelPath": ChannelPath,
       "ChannelDevice": ChannelDevice,
       "ciscoCipCsnaMIB": ciscoCipCsnaMIB,
       "cipCsnaObjects": cipCsnaObjects,
       "cipCsnaChannel": cipCsnaChannel,
       "cipCardCsnaAdminTable": cipCardCsnaAdminTable,
       "cipCardCsnaAdminEntry": cipCardCsnaAdminEntry,
       "cipCardCsnaAdminPath": cipCardCsnaAdminPath,
       "cipCardCsnaAdminDevice": cipCardCsnaAdminDevice,
       "cipCardCsnaAdminBlockDelayTime": cipCardCsnaAdminBlockDelayTime,
       "cipCardCsnaAdminBlockDelayLength": cipCardCsnaAdminBlockDelayLength,
       "cipCardCsnaAdminMaxBlockLength": cipCardCsnaAdminMaxBlockLength,
       "cipCardCsnaAdminRowStatus": cipCardCsnaAdminRowStatus,
       "cipCardCsnaOperTable": cipCardCsnaOperTable,
       "cipCardCsnaOperEntry": cipCardCsnaOperEntry,
       "cipCardCsnaOperState": cipCardCsnaOperState,
       "cipCardCsnaOperSlowDownState": cipCardCsnaOperSlowDownState,
       "cipCardCsnaOperBlockDelayTime": cipCardCsnaOperBlockDelayTime,
       "cipCardCsnaOperBlockDelayLength": cipCardCsnaOperBlockDelayLength,
       "cipCardCsnaOperMaxBlockLength": cipCardCsnaOperMaxBlockLength,
       "cipCardCsnaStatsTable": cipCardCsnaStatsTable,
       "cipCardCsnaStatsEntry": cipCardCsnaStatsEntry,
       "cipCardCsnaStatsBlocksTxd": cipCardCsnaStatsBlocksTxd,
       "cipCardCsnaStatsBlocksRxd": cipCardCsnaStatsBlocksRxd,
       "cipCardCsnaStatsBytesTxd": cipCardCsnaStatsBytesTxd,
       "cipCardCsnaStatsHCBytesTxd": cipCardCsnaStatsHCBytesTxd,
       "cipCardCsnaStatsBytesRxd": cipCardCsnaStatsBytesRxd,
       "cipCardCsnaStatsHCBytesRxd": cipCardCsnaStatsHCBytesRxd,
       "cipCardCsnaStatsBlocksTxByBlockDelayTime": cipCardCsnaStatsBlocksTxByBlockDelayTime,
       "cipCardCsnaStatsBytesTxByBlockDelayTime": cipCardCsnaStatsBytesTxByBlockDelayTime,
       "cipCardCsnaStatsHCBytesTxByBlockDelayTime": cipCardCsnaStatsHCBytesTxByBlockDelayTime,
       "cipCardCsnaStatsBlocksTxByBlockDelayLength": cipCardCsnaStatsBlocksTxByBlockDelayLength,
       "cipCardCsnaStatsBytesTxByBlockDelayLength": cipCardCsnaStatsBytesTxByBlockDelayLength,
       "cipCardCsnaStatsHCBytesTxByBlockDelayLength": cipCardCsnaStatsHCBytesTxByBlockDelayLength,
       "cipCardCsnaStatsBlocksTxByMaxBlockLength": cipCardCsnaStatsBlocksTxByMaxBlockLength,
       "cipCardCsnaStatsBytesTxByMaxBlockLength": cipCardCsnaStatsBytesTxByMaxBlockLength,
       "cipCardCsnaStatsHCBytesTxByMaxBlockLength": cipCardCsnaStatsHCBytesTxByMaxBlockLength,
       "cipCardCsnaStatsSlowDownsReceived": cipCardCsnaStatsSlowDownsReceived,
       "cipCardCsnaStatsSlowDownsSent": cipCardCsnaStatsSlowDownsSent,
       "cipSession": cipSession,
       "cipCardSessionsAdminTable": cipCardSessionsAdminTable,
       "cipCardSessionsAdminEntry": cipCardSessionsAdminEntry,
       "cipCardAdminMaxLlc2Sessions": cipCardAdminMaxLlc2Sessions,
       "cipCardSessionsOperTable": cipCardSessionsOperTable,
       "cipCardSessionsOperEntry": cipCardSessionsOperEntry,
       "cipCardOperMaxLlc2Sessions": cipCardOperMaxLlc2Sessions,
       "cipCardSessionsStatsTable": cipCardSessionsStatsTable,
       "cipCardSessionsStatsEntry": cipCardSessionsStatsEntry,
       "cipCardStatsHiWaterLlc2Sessions": cipCardStatsHiWaterLlc2Sessions,
       "cipCardStatsLlc2SessionAllocationErrs": cipCardStatsLlc2SessionAllocationErrs,
       "cipCsnaConnection": cipCsnaConnection,
       "cipCardCsnaConnTable": cipCardCsnaConnTable,
       "cipCardCsnaConnEntry": cipCardCsnaConnEntry,
       "cipCardCsnaConnActiveSessions": cipCardCsnaConnActiveSessions,
       "cipCardCsnaSlot": cipCardCsnaSlot,
       "cipCardCsnaPort": cipCardCsnaPort,
       "cipCardCsnaConnPath": cipCardCsnaConnPath,
       "cipCardCsnaConnDevice": cipCardCsnaConnDevice,
       "cipCsnaNotificationPrefix": cipCsnaNotificationPrefix,
       "cipCsnaNotifications": cipCsnaNotifications,
       "cipCsnaOpenDuplicateSapFailure": cipCsnaOpenDuplicateSapFailure,
       "cipCsnaLlc2ConnectionLimitExceeded": cipCsnaLlc2ConnectionLimitExceeded,
       "ciscoCipCsnaMibConformance": ciscoCipCsnaMibConformance,
       "ciscoCipCsnaMibCompliances": ciscoCipCsnaMibCompliances,
       "ciscoCipCsnaMibCompliance": ciscoCipCsnaMibCompliance,
       "ciscoCipCsnaMibGroups": ciscoCipCsnaMibGroups,
       "ciscoCsnaGroup": ciscoCsnaGroup,
       "ciscoMaxSessionsGroup": ciscoMaxSessionsGroup,
       "ciscoCsnaConnGroup": ciscoCsnaConnGroup}
)
