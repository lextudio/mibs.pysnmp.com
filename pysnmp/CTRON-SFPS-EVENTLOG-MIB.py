# SNMP MIB module (CTRON-SFPS-EVENTLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-EVENTLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:23 2024
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

(sfpsEventLogClientConfig,
 sfpsEventLogClientConfigAPI,
 sfpsEventLogGenConfig,
 sfpsEventLogStats,
 sfpsFragStats,
 sfpsTrapAPI,
 sfpsTrapTable) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsEventLogClientConfig",
    "sfpsEventLogClientConfigAPI",
    "sfpsEventLogGenConfig",
    "sfpsEventLogStats",
    "sfpsFragStats",
    "sfpsTrapAPI",
    "sfpsTrapTable")

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


# MODULE-IDENTITY


# Types definitions



class SfpsSwitchInstance(OctetString):
    """Custom type SfpsSwitchInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsEventLogStatsTable_Object = MibTable
sfpsEventLogStatsTable = _SfpsEventLogStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsEventLogStatsTable.setStatus("mandatory")
_SfpsEventLogStatsEntry_Object = MibTableRow
sfpsEventLogStatsEntry = _SfpsEventLogStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1)
)
sfpsEventLogStatsEntry.setIndexNames(
    (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogStatsSwInst"),
    (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogWindowStart"),
)
if mibBuilder.loadTexts:
    sfpsEventLogStatsEntry.setStatus("mandatory")
_SfpsEventLogStatsSwInst_Type = SfpsSwitchInstance
_SfpsEventLogStatsSwInst_Object = MibTableColumn
sfpsEventLogStatsSwInst = _SfpsEventLogStatsSwInst_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 1),
    _SfpsEventLogStatsSwInst_Type()
)
sfpsEventLogStatsSwInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogStatsSwInst.setStatus("mandatory")
_SfpsEventLogWindowStart_Type = Integer32
_SfpsEventLogWindowStart_Object = MibTableColumn
sfpsEventLogWindowStart = _SfpsEventLogWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 2),
    _SfpsEventLogWindowStart_Type()
)
sfpsEventLogWindowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogWindowStart.setStatus("mandatory")
_SfpsEventLogIndex_Type = Integer32
_SfpsEventLogIndex_Object = MibTableColumn
sfpsEventLogIndex = _SfpsEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 3),
    _SfpsEventLogIndex_Type()
)
sfpsEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogIndex.setStatus("mandatory")
_SfpsEventLogClientName_Type = DisplayString
_SfpsEventLogClientName_Object = MibTableColumn
sfpsEventLogClientName = _SfpsEventLogClientName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 4),
    _SfpsEventLogClientName_Type()
)
sfpsEventLogClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogClientName.setStatus("mandatory")
_SfpsEventLogLevel_Type = DisplayString
_SfpsEventLogLevel_Object = MibTableColumn
sfpsEventLogLevel = _SfpsEventLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 5),
    _SfpsEventLogLevel_Type()
)
sfpsEventLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogLevel.setStatus("mandatory")
_SfpsEventLogMessageString_Type = DisplayString
_SfpsEventLogMessageString_Object = MibTableColumn
sfpsEventLogMessageString = _SfpsEventLogMessageString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 6),
    _SfpsEventLogMessageString_Type()
)
sfpsEventLogMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogMessageString.setStatus("mandatory")
_SfpsEventLogTime_Type = TimeTicks
_SfpsEventLogTime_Object = MibTableColumn
sfpsEventLogTime = _SfpsEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 7),
    _SfpsEventLogTime_Type()
)
sfpsEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogTime.setStatus("mandatory")
_SfpsEventLogCallTag_Type = HexInteger
_SfpsEventLogCallTag_Object = MibTableColumn
sfpsEventLogCallTag = _SfpsEventLogCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 8),
    _SfpsEventLogCallTag_Type()
)
sfpsEventLogCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogCallTag.setStatus("mandatory")
_SfpsEventLogInfo1_Type = HexInteger
_SfpsEventLogInfo1_Object = MibTableColumn
sfpsEventLogInfo1 = _SfpsEventLogInfo1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 9),
    _SfpsEventLogInfo1_Type()
)
sfpsEventLogInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogInfo1.setStatus("mandatory")
_SfpsEventLogInfo2_Type = HexInteger
_SfpsEventLogInfo2_Object = MibTableColumn
sfpsEventLogInfo2 = _SfpsEventLogInfo2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 10),
    _SfpsEventLogInfo2_Type()
)
sfpsEventLogInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogInfo2.setStatus("mandatory")
_SfpsEventLogGenConfigTable_Object = MibTable
sfpsEventLogGenConfigTable = _SfpsEventLogGenConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigTable.setStatus("mandatory")
_SfpsEventLogGenConfigEntry_Object = MibTableRow
sfpsEventLogGenConfigEntry = _SfpsEventLogGenConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1)
)
sfpsEventLogGenConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogGenConfigSwInst"),
)
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigEntry.setStatus("mandatory")
_SfpsEventLogGenConfigSwInst_Type = SfpsSwitchInstance
_SfpsEventLogGenConfigSwInst_Object = MibTableColumn
sfpsEventLogGenConfigSwInst = _SfpsEventLogGenConfigSwInst_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 1),
    _SfpsEventLogGenConfigSwInst_Type()
)
sfpsEventLogGenConfigSwInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigSwInst.setStatus("mandatory")


class _SfpsEventLogGenConfigWindowStart_Type(Integer32):
    """Custom type sfpsEventLogGenConfigWindowStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_SfpsEventLogGenConfigWindowStart_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigWindowStart_Object = MibTableColumn
sfpsEventLogGenConfigWindowStart = _SfpsEventLogGenConfigWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 2),
    _SfpsEventLogGenConfigWindowStart_Type()
)
sfpsEventLogGenConfigWindowStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigWindowStart.setStatus("mandatory")


class _SfpsEventLogGenConfigLoggingIndex_Type(Integer32):
    """Custom type sfpsEventLogGenConfigLoggingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_SfpsEventLogGenConfigLoggingIndex_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigLoggingIndex_Object = MibTableColumn
sfpsEventLogGenConfigLoggingIndex = _SfpsEventLogGenConfigLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 3),
    _SfpsEventLogGenConfigLoggingIndex_Type()
)
sfpsEventLogGenConfigLoggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigLoggingIndex.setStatus("mandatory")
_SfpsEventLogGenConfigMessageFilter_Type = DisplayString
_SfpsEventLogGenConfigMessageFilter_Object = MibTableColumn
sfpsEventLogGenConfigMessageFilter = _SfpsEventLogGenConfigMessageFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 4),
    _SfpsEventLogGenConfigMessageFilter_Type()
)
sfpsEventLogGenConfigMessageFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigMessageFilter.setStatus("mandatory")
_SfpsEventLogGenConfigCallTagFilter_Type = HexInteger
_SfpsEventLogGenConfigCallTagFilter_Object = MibTableColumn
sfpsEventLogGenConfigCallTagFilter = _SfpsEventLogGenConfigCallTagFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 5),
    _SfpsEventLogGenConfigCallTagFilter_Type()
)
sfpsEventLogGenConfigCallTagFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigCallTagFilter.setStatus("mandatory")


class _SfpsEventLogGenConfigAdminStatus_Type(Integer32):
    """Custom type sfpsEventLogGenConfigAdminStatus based on Integer32"""
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
        *(("continue", 5),
          ("disable", 2),
          ("enable", 3),
          ("other", 1),
          ("reset", 4))
    )


_SfpsEventLogGenConfigAdminStatus_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigAdminStatus_Object = MibTableColumn
sfpsEventLogGenConfigAdminStatus = _SfpsEventLogGenConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 6),
    _SfpsEventLogGenConfigAdminStatus_Type()
)
sfpsEventLogGenConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigAdminStatus.setStatus("mandatory")


class _SfpsEventLogGenConfigOperStatus_Type(Integer32):
    """Custom type sfpsEventLogGenConfigOperStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_SfpsEventLogGenConfigOperStatus_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigOperStatus_Object = MibTableColumn
sfpsEventLogGenConfigOperStatus = _SfpsEventLogGenConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 7),
    _SfpsEventLogGenConfigOperStatus_Type()
)
sfpsEventLogGenConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigOperStatus.setStatus("mandatory")
_SfpsEventLogGenConfigOperTime_Type = TimeTicks
_SfpsEventLogGenConfigOperTime_Object = MibTableColumn
sfpsEventLogGenConfigOperTime = _SfpsEventLogGenConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 8),
    _SfpsEventLogGenConfigOperTime_Type()
)
sfpsEventLogGenConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigOperTime.setStatus("mandatory")


class _SfpsEventLogGenConfigAutoFreeze_Type(Integer32):
    """Custom type sfpsEventLogGenConfigAutoFreeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogGenConfigAutoFreeze_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigAutoFreeze_Object = MibTableColumn
sfpsEventLogGenConfigAutoFreeze = _SfpsEventLogGenConfigAutoFreeze_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 9),
    _SfpsEventLogGenConfigAutoFreeze_Type()
)
sfpsEventLogGenConfigAutoFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigAutoFreeze.setStatus("mandatory")


class _SfpsEventLogGenConfigDisplayWrapDetect_Type(Integer32):
    """Custom type sfpsEventLogGenConfigDisplayWrapDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogGenConfigDisplayWrapDetect_Type.__name__ = "Integer32"
_SfpsEventLogGenConfigDisplayWrapDetect_Object = MibTableColumn
sfpsEventLogGenConfigDisplayWrapDetect = _SfpsEventLogGenConfigDisplayWrapDetect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 10),
    _SfpsEventLogGenConfigDisplayWrapDetect_Type()
)
sfpsEventLogGenConfigDisplayWrapDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigDisplayWrapDetect.setStatus("mandatory")
_SfpsEventLogGenConfigAdvertiseAddr_Type = IpAddress
_SfpsEventLogGenConfigAdvertiseAddr_Object = MibTableColumn
sfpsEventLogGenConfigAdvertiseAddr = _SfpsEventLogGenConfigAdvertiseAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 11),
    _SfpsEventLogGenConfigAdvertiseAddr_Type()
)
sfpsEventLogGenConfigAdvertiseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogGenConfigAdvertiseAddr.setStatus("mandatory")
_SfpsEventLogClientConfigTable_Object = MibTable
sfpsEventLogClientConfigTable = _SfpsEventLogClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigTable.setStatus("mandatory")
_SfpsEventLogClientConfigEntry_Object = MibTableRow
sfpsEventLogClientConfigEntry = _SfpsEventLogClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1)
)
sfpsEventLogClientConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogClientConfigId"),
)
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigEntry.setStatus("mandatory")
_SfpsEventLogClientConfigId_Type = Integer32
_SfpsEventLogClientConfigId_Object = MibTableColumn
sfpsEventLogClientConfigId = _SfpsEventLogClientConfigId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 1),
    _SfpsEventLogClientConfigId_Type()
)
sfpsEventLogClientConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigId.setStatus("mandatory")
_SfpsEventLogClientConfigName_Type = DisplayString
_SfpsEventLogClientConfigName_Object = MibTableColumn
sfpsEventLogClientConfigName = _SfpsEventLogClientConfigName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 2),
    _SfpsEventLogClientConfigName_Type()
)
sfpsEventLogClientConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigName.setStatus("mandatory")


class _SfpsEventLogClientLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientLogStatus_Object = MibTableColumn
sfpsEventLogClientLogStatus = _SfpsEventLogClientLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 3),
    _SfpsEventLogClientLogStatus_Type()
)
sfpsEventLogClientLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientLogStatus.setStatus("mandatory")


class _SfpsEventLogClientDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientDisplayStatus_Object = MibTableColumn
sfpsEventLogClientDisplayStatus = _SfpsEventLogClientDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 4),
    _SfpsEventLogClientDisplayStatus_Type()
)
sfpsEventLogClientDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientFreezeLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientFreezeLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientFreezeLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientFreezeLogStatus_Object = MibTableColumn
sfpsEventLogClientFreezeLogStatus = _SfpsEventLogClientFreezeLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 5),
    _SfpsEventLogClientFreezeLogStatus_Type()
)
sfpsEventLogClientFreezeLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientFreezeLogStatus.setStatus("mandatory")


class _SfpsEventLogClientFreezeDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientFreezeDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientFreezeDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientFreezeDisplayStatus_Object = MibTableColumn
sfpsEventLogClientFreezeDisplayStatus = _SfpsEventLogClientFreezeDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 6),
    _SfpsEventLogClientFreezeDisplayStatus_Type()
)
sfpsEventLogClientFreezeDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientFreezeDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientErrorLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientErrorLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientErrorLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientErrorLogStatus_Object = MibTableColumn
sfpsEventLogClientErrorLogStatus = _SfpsEventLogClientErrorLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 7),
    _SfpsEventLogClientErrorLogStatus_Type()
)
sfpsEventLogClientErrorLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientErrorLogStatus.setStatus("mandatory")


class _SfpsEventLogClientErrorDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientErrorDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientErrorDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientErrorDisplayStatus_Object = MibTableColumn
sfpsEventLogClientErrorDisplayStatus = _SfpsEventLogClientErrorDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 8),
    _SfpsEventLogClientErrorDisplayStatus_Type()
)
sfpsEventLogClientErrorDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientErrorDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientCriticalLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientCriticalLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientCriticalLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientCriticalLogStatus_Object = MibTableColumn
sfpsEventLogClientCriticalLogStatus = _SfpsEventLogClientCriticalLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 9),
    _SfpsEventLogClientCriticalLogStatus_Type()
)
sfpsEventLogClientCriticalLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientCriticalLogStatus.setStatus("mandatory")


class _SfpsEventLogClientCriticalDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientCriticalDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientCriticalDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientCriticalDisplayStatus_Object = MibTableColumn
sfpsEventLogClientCriticalDisplayStatus = _SfpsEventLogClientCriticalDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 10),
    _SfpsEventLogClientCriticalDisplayStatus_Type()
)
sfpsEventLogClientCriticalDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientCriticalDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientInfoLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientInfoLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientInfoLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientInfoLogStatus_Object = MibTableColumn
sfpsEventLogClientInfoLogStatus = _SfpsEventLogClientInfoLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 11),
    _SfpsEventLogClientInfoLogStatus_Type()
)
sfpsEventLogClientInfoLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientInfoLogStatus.setStatus("mandatory")


class _SfpsEventLogClientInfoDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientInfoDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientInfoDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientInfoDisplayStatus_Object = MibTableColumn
sfpsEventLogClientInfoDisplayStatus = _SfpsEventLogClientInfoDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 12),
    _SfpsEventLogClientInfoDisplayStatus_Type()
)
sfpsEventLogClientInfoDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientInfoDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientDebugLogStatus_Type(Integer32):
    """Custom type sfpsEventLogClientDebugLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientDebugLogStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientDebugLogStatus_Object = MibTableColumn
sfpsEventLogClientDebugLogStatus = _SfpsEventLogClientDebugLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 13),
    _SfpsEventLogClientDebugLogStatus_Type()
)
sfpsEventLogClientDebugLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientDebugLogStatus.setStatus("mandatory")


class _SfpsEventLogClientDebugDisplayStatus_Type(Integer32):
    """Custom type sfpsEventLogClientDebugDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientDebugDisplayStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientDebugDisplayStatus_Object = MibTableColumn
sfpsEventLogClientDebugDisplayStatus = _SfpsEventLogClientDebugDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 14),
    _SfpsEventLogClientDebugDisplayStatus_Type()
)
sfpsEventLogClientDebugDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientDebugDisplayStatus.setStatus("mandatory")


class _SfpsEventLogClientConfigAPIVerb_Type(Integer32):
    """Custom type sfpsEventLogClientConfigAPIVerb based on Integer32"""
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
        *(("allClients", 7),
          ("allLogLevels", 6),
          ("criticalLog", 3),
          ("debugLog", 5),
          ("errorLog", 2),
          ("freezeLog", 1),
          ("infoLog", 4),
          ("masterLog", 8))
    )


_SfpsEventLogClientConfigAPIVerb_Type.__name__ = "Integer32"
_SfpsEventLogClientConfigAPIVerb_Object = MibScalar
sfpsEventLogClientConfigAPIVerb = _SfpsEventLogClientConfigAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 1),
    _SfpsEventLogClientConfigAPIVerb_Type()
)
sfpsEventLogClientConfigAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigAPIVerb.setStatus("mandatory")


class _SfpsEventLogClientConfigAPIAdminStatus_Type(Integer32):
    """Custom type sfpsEventLogClientConfigAPIAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsEventLogClientConfigAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsEventLogClientConfigAPIAdminStatus_Object = MibScalar
sfpsEventLogClientConfigAPIAdminStatus = _SfpsEventLogClientConfigAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 2),
    _SfpsEventLogClientConfigAPIAdminStatus_Type()
)
sfpsEventLogClientConfigAPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigAPIAdminStatus.setStatus("mandatory")
_SfpsEventLogClientConfigAPIClientName_Type = DisplayString
_SfpsEventLogClientConfigAPIClientName_Object = MibScalar
sfpsEventLogClientConfigAPIClientName = _SfpsEventLogClientConfigAPIClientName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 3),
    _SfpsEventLogClientConfigAPIClientName_Type()
)
sfpsEventLogClientConfigAPIClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigAPIClientName.setStatus("mandatory")
_SfpsEventLogClientConfigAPIClientID_Type = Integer32
_SfpsEventLogClientConfigAPIClientID_Object = MibScalar
sfpsEventLogClientConfigAPIClientID = _SfpsEventLogClientConfigAPIClientID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 4),
    _SfpsEventLogClientConfigAPIClientID_Type()
)
sfpsEventLogClientConfigAPIClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigAPIClientID.setStatus("mandatory")


class _SfpsEventLogClientConfigAPILogDisplay_Type(Integer32):
    """Custom type sfpsEventLogClientConfigAPILogDisplay based on Integer32"""
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
        *(("displayOnly", 4),
          ("logAndDisplay", 2),
          ("logOnly", 3),
          ("other", 1))
    )


_SfpsEventLogClientConfigAPILogDisplay_Type.__name__ = "Integer32"
_SfpsEventLogClientConfigAPILogDisplay_Object = MibScalar
sfpsEventLogClientConfigAPILogDisplay = _SfpsEventLogClientConfigAPILogDisplay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 5),
    _SfpsEventLogClientConfigAPILogDisplay_Type()
)
sfpsEventLogClientConfigAPILogDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsEventLogClientConfigAPILogDisplay.setStatus("mandatory")


class _SfpsTrapAPIVerb_Type(Integer32):
    """Custom type sfpsTrapAPIVerb based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("other", 1),
          ("resetAllStats", 5),
          ("resetTrapStats", 4))
    )


_SfpsTrapAPIVerb_Type.__name__ = "Integer32"
_SfpsTrapAPIVerb_Object = MibScalar
sfpsTrapAPIVerb = _SfpsTrapAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 1),
    _SfpsTrapAPIVerb_Type()
)
sfpsTrapAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTrapAPIVerb.setStatus("mandatory")


class _SfpsTrapAPITrapId_Type(Integer32):
    """Custom type sfpsTrapAPITrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1400,
              1401,
              1402,
              1403,
              1404,
              1405,
              1406,
              1407,
              1408,
              1409,
              1410)
        )
    )
    namedValues = NamedValues(
        *(("ageCnt", 1406),
          ("agentIP", 1410),
          ("changeCount", 1407),
          ("dstBlock", 1403),
          ("foundNeighbor", 1408),
          ("lostNeighbor", 1409),
          ("newUser", 1400),
          ("portFromStandby", 1405),
          ("portToStandby", 1404),
          ("srcBlock", 1402),
          ("violation", 1401))
    )


_SfpsTrapAPITrapId_Type.__name__ = "Integer32"
_SfpsTrapAPITrapId_Object = MibScalar
sfpsTrapAPITrapId = _SfpsTrapAPITrapId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 2),
    _SfpsTrapAPITrapId_Type()
)
sfpsTrapAPITrapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTrapAPITrapId.setStatus("mandatory")
_SfpsTrapAPITotalSent_Type = Integer32
_SfpsTrapAPITotalSent_Object = MibScalar
sfpsTrapAPITotalSent = _SfpsTrapAPITotalSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 3),
    _SfpsTrapAPITotalSent_Type()
)
sfpsTrapAPITotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTrapAPITotalSent.setStatus("mandatory")


class _SfpsTrapTableTrapId_Type(Integer32):
    """Custom type sfpsTrapTableTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1400,
              1401,
              1402,
              1403,
              1404,
              1405,
              1406,
              1407,
              1408,
              1409,
              1410,
              1411,
              1412,
              1413,
              1414,
              1415,
              1416,
              1417,
              1418,
              1419,
              1420,
              1421,
              1422)
        )
    )
    namedValues = NamedValues(
        *(("ageCnt", 1406),
          ("agentIP", 1410),
          ("changeCount", 1407),
          ("decVlanUserCount", 1417),
          ("dstBlock", 1403),
          ("foundNeighbor", 1408),
          ("hsrpPrimaryResign", 1421),
          ("hsrpSecondaryUp", 1422),
          ("incVlanUserCount", 1416),
          ("lostNeighbor", 1409),
          ("newUser", 1400),
          ("noCommonSecureVlan", 1415),
          ("noDestVlans", 1412),
          ("noDestVlansEnabled", 1414),
          ("noSrcVlans", 1411),
          ("noSrcVlansEnabled", 1413),
          ("portFromStandby", 1405),
          ("portToStandby", 1404),
          ("srcBlock", 1402),
          ("violation", 1401),
          ("vrrpPrimaryAged", 1419),
          ("vrrpPrimaryResign", 1418),
          ("vrrpSecondaryUp", 1420))
    )


_SfpsTrapTableTrapId_Type.__name__ = "Integer32"
_SfpsTrapTableTrapId_Object = MibScalar
sfpsTrapTableTrapId = _SfpsTrapTableTrapId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 1),
    _SfpsTrapTableTrapId_Type()
)
sfpsTrapTableTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTrapTableTrapId.setStatus("mandatory")


class _SfpsTrapTableAdminStatus_Type(Integer32):
    """Custom type sfpsTrapTableAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsTrapTableAdminStatus_Type.__name__ = "Integer32"
_SfpsTrapTableAdminStatus_Object = MibScalar
sfpsTrapTableAdminStatus = _SfpsTrapTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 2),
    _SfpsTrapTableAdminStatus_Type()
)
sfpsTrapTableAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTrapTableAdminStatus.setStatus("mandatory")
_SfpsTrapTableNumSent_Type = Integer32
_SfpsTrapTableNumSent_Object = MibScalar
sfpsTrapTableNumSent = _SfpsTrapTableNumSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 3),
    _SfpsTrapTableNumSent_Type()
)
sfpsTrapTableNumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTrapTableNumSent.setStatus("mandatory")
_SfpsTrapTableLastSent_Type = TimeTicks
_SfpsTrapTableLastSent_Object = MibScalar
sfpsTrapTableLastSent = _SfpsTrapTableLastSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 4),
    _SfpsTrapTableLastSent_Type()
)
sfpsTrapTableLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTrapTableLastSent.setStatus("mandatory")
_SfpsFragStatsTotalFrags_Type = Integer32
_SfpsFragStatsTotalFrags_Object = MibScalar
sfpsFragStatsTotalFrags = _SfpsFragStatsTotalFrags_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 1),
    _SfpsFragStatsTotalFrags_Type()
)
sfpsFragStatsTotalFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsTotalFrags.setStatus("mandatory")
_SfpsFragStatsNumLookupFail_Type = Integer32
_SfpsFragStatsNumLookupFail_Object = MibScalar
sfpsFragStatsNumLookupFail = _SfpsFragStatsNumLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 2),
    _SfpsFragStatsNumLookupFail_Type()
)
sfpsFragStatsNumLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsNumLookupFail.setStatus("mandatory")
_SfpsFragStatsAvgCompares_Type = OctetString
_SfpsFragStatsAvgCompares_Object = MibScalar
sfpsFragStatsAvgCompares = _SfpsFragStatsAvgCompares_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 3),
    _SfpsFragStatsAvgCompares_Type()
)
sfpsFragStatsAvgCompares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsAvgCompares.setStatus("mandatory")
_SfpsFragStatsNumNodes_Type = Integer32
_SfpsFragStatsNumNodes_Object = MibScalar
sfpsFragStatsNumNodes = _SfpsFragStatsNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 4),
    _SfpsFragStatsNumNodes_Type()
)
sfpsFragStatsNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsNumNodes.setStatus("mandatory")
_SfpsFragStatsNumUsed_Type = Integer32
_SfpsFragStatsNumUsed_Object = MibScalar
sfpsFragStatsNumUsed = _SfpsFragStatsNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 5),
    _SfpsFragStatsNumUsed_Type()
)
sfpsFragStatsNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsNumUsed.setStatus("mandatory")
_SfpsFragStatsMaxNumUsed_Type = Integer32
_SfpsFragStatsMaxNumUsed_Object = MibScalar
sfpsFragStatsMaxNumUsed = _SfpsFragStatsMaxNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 6),
    _SfpsFragStatsMaxNumUsed_Type()
)
sfpsFragStatsMaxNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsMaxNumUsed.setStatus("mandatory")
_SfpsFragStatsNumStolen_Type = Integer32
_SfpsFragStatsNumStolen_Object = MibScalar
sfpsFragStatsNumStolen = _SfpsFragStatsNumStolen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 7),
    _SfpsFragStatsNumStolen_Type()
)
sfpsFragStatsNumStolen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFragStatsNumStolen.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-EVENTLOG-MIB",
    **{"SfpsSwitchInstance": SfpsSwitchInstance,
       "HexInteger": HexInteger,
       "sfpsEventLogStatsTable": sfpsEventLogStatsTable,
       "sfpsEventLogStatsEntry": sfpsEventLogStatsEntry,
       "sfpsEventLogStatsSwInst": sfpsEventLogStatsSwInst,
       "sfpsEventLogWindowStart": sfpsEventLogWindowStart,
       "sfpsEventLogIndex": sfpsEventLogIndex,
       "sfpsEventLogClientName": sfpsEventLogClientName,
       "sfpsEventLogLevel": sfpsEventLogLevel,
       "sfpsEventLogMessageString": sfpsEventLogMessageString,
       "sfpsEventLogTime": sfpsEventLogTime,
       "sfpsEventLogCallTag": sfpsEventLogCallTag,
       "sfpsEventLogInfo1": sfpsEventLogInfo1,
       "sfpsEventLogInfo2": sfpsEventLogInfo2,
       "sfpsEventLogGenConfigTable": sfpsEventLogGenConfigTable,
       "sfpsEventLogGenConfigEntry": sfpsEventLogGenConfigEntry,
       "sfpsEventLogGenConfigSwInst": sfpsEventLogGenConfigSwInst,
       "sfpsEventLogGenConfigWindowStart": sfpsEventLogGenConfigWindowStart,
       "sfpsEventLogGenConfigLoggingIndex": sfpsEventLogGenConfigLoggingIndex,
       "sfpsEventLogGenConfigMessageFilter": sfpsEventLogGenConfigMessageFilter,
       "sfpsEventLogGenConfigCallTagFilter": sfpsEventLogGenConfigCallTagFilter,
       "sfpsEventLogGenConfigAdminStatus": sfpsEventLogGenConfigAdminStatus,
       "sfpsEventLogGenConfigOperStatus": sfpsEventLogGenConfigOperStatus,
       "sfpsEventLogGenConfigOperTime": sfpsEventLogGenConfigOperTime,
       "sfpsEventLogGenConfigAutoFreeze": sfpsEventLogGenConfigAutoFreeze,
       "sfpsEventLogGenConfigDisplayWrapDetect": sfpsEventLogGenConfigDisplayWrapDetect,
       "sfpsEventLogGenConfigAdvertiseAddr": sfpsEventLogGenConfigAdvertiseAddr,
       "sfpsEventLogClientConfigTable": sfpsEventLogClientConfigTable,
       "sfpsEventLogClientConfigEntry": sfpsEventLogClientConfigEntry,
       "sfpsEventLogClientConfigId": sfpsEventLogClientConfigId,
       "sfpsEventLogClientConfigName": sfpsEventLogClientConfigName,
       "sfpsEventLogClientLogStatus": sfpsEventLogClientLogStatus,
       "sfpsEventLogClientDisplayStatus": sfpsEventLogClientDisplayStatus,
       "sfpsEventLogClientFreezeLogStatus": sfpsEventLogClientFreezeLogStatus,
       "sfpsEventLogClientFreezeDisplayStatus": sfpsEventLogClientFreezeDisplayStatus,
       "sfpsEventLogClientErrorLogStatus": sfpsEventLogClientErrorLogStatus,
       "sfpsEventLogClientErrorDisplayStatus": sfpsEventLogClientErrorDisplayStatus,
       "sfpsEventLogClientCriticalLogStatus": sfpsEventLogClientCriticalLogStatus,
       "sfpsEventLogClientCriticalDisplayStatus": sfpsEventLogClientCriticalDisplayStatus,
       "sfpsEventLogClientInfoLogStatus": sfpsEventLogClientInfoLogStatus,
       "sfpsEventLogClientInfoDisplayStatus": sfpsEventLogClientInfoDisplayStatus,
       "sfpsEventLogClientDebugLogStatus": sfpsEventLogClientDebugLogStatus,
       "sfpsEventLogClientDebugDisplayStatus": sfpsEventLogClientDebugDisplayStatus,
       "sfpsEventLogClientConfigAPIVerb": sfpsEventLogClientConfigAPIVerb,
       "sfpsEventLogClientConfigAPIAdminStatus": sfpsEventLogClientConfigAPIAdminStatus,
       "sfpsEventLogClientConfigAPIClientName": sfpsEventLogClientConfigAPIClientName,
       "sfpsEventLogClientConfigAPIClientID": sfpsEventLogClientConfigAPIClientID,
       "sfpsEventLogClientConfigAPILogDisplay": sfpsEventLogClientConfigAPILogDisplay,
       "sfpsTrapAPIVerb": sfpsTrapAPIVerb,
       "sfpsTrapAPITrapId": sfpsTrapAPITrapId,
       "sfpsTrapAPITotalSent": sfpsTrapAPITotalSent,
       "sfpsTrapTableTrapId": sfpsTrapTableTrapId,
       "sfpsTrapTableAdminStatus": sfpsTrapTableAdminStatus,
       "sfpsTrapTableNumSent": sfpsTrapTableNumSent,
       "sfpsTrapTableLastSent": sfpsTrapTableLastSent,
       "sfpsFragStatsTotalFrags": sfpsFragStatsTotalFrags,
       "sfpsFragStatsNumLookupFail": sfpsFragStatsNumLookupFail,
       "sfpsFragStatsAvgCompares": sfpsFragStatsAvgCompares,
       "sfpsFragStatsNumNodes": sfpsFragStatsNumNodes,
       "sfpsFragStatsNumUsed": sfpsFragStatsNumUsed,
       "sfpsFragStatsMaxNumUsed": sfpsFragStatsMaxNumUsed,
       "sfpsFragStatsNumStolen": sfpsFragStatsNumStolen}
)
