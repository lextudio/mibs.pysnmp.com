# SNMP MIB module (CISCO-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(MilliSeconds,
 imaGroupEntry,
 imaGroupIndex,
 imaLinkEntry,
 imaLinkIfIndex) = mibBuilder.importSymbols(
    "IMA-MIB",
    "MilliSeconds",
    "imaGroupEntry",
    "imaGroupIndex",
    "imaLinkEntry",
    "imaLinkIfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoImaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 235)
)
ciscoImaMIB.setRevisions(
        ("2003-03-26 00:00",
         "2002-05-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoImaGrpAlarmType(Integer32, TextualConvention):
    status = "current"
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
        *(("cimaAlarmGroupBlockedFe", 6),
          ("cimaAlarmGroupCfgAbort", 2),
          ("cimaAlarmGroupCfgAbortFe", 3),
          ("cimaAlarmGroupInsuffLinks", 4),
          ("cimaAlarmGroupInsuffLinksFe", 5),
          ("cimaAlarmGroupStartupFe", 1),
          ("cimaAlarmGroupTimingSynch", 7))
    )



class CiscoImaLinkAlarmType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cimaAlarmLinkLif", 1),
          ("cimaAlarmLinkLods", 2),
          ("cimaAlarmLinkRfi", 3),
          ("cimaAlarmLinkRxFault", 7),
          ("cimaAlarmLinkRxMisConnect", 5),
          ("cimaAlarmLinkRxUnusableFe", 9),
          ("cimaAlarmLinkTxFault", 6),
          ("cimaAlarmLinkTxMisConnect", 4),
          ("cimaAlarmLinkTxUnusableFe", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoImaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImaMIBObjects = _CiscoImaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1)
)
_CimaGrpAlarmType_Type = CiscoImaGrpAlarmType
_CimaGrpAlarmType_Object = MibScalar
cimaGrpAlarmType = _CimaGrpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 1),
    _CimaGrpAlarmType_Type()
)
cimaGrpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpAlarmType.setStatus("deprecated")
_CimaLinkAlarmType_Type = CiscoImaLinkAlarmType
_CimaLinkAlarmType_Object = MibScalar
cimaLinkAlarmType = _CimaLinkAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 2),
    _CimaLinkAlarmType_Type()
)
cimaLinkAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkAlarmType.setStatus("deprecated")
_CimaGroupTable_Object = MibTable
cimaGroupTable = _CimaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3)
)
if mibBuilder.loadTexts:
    cimaGroupTable.setStatus("current")
_CimaGroupEntry_Object = MibTableRow
cimaGroupEntry = _CimaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cimaGroupEntry.setStatus("current")
_CimaGroupAccumulatedDelay_Type = MilliSeconds
_CimaGroupAccumulatedDelay_Object = MibTableColumn
cimaGroupAccumulatedDelay = _CimaGroupAccumulatedDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 1),
    _CimaGroupAccumulatedDelay_Type()
)
cimaGroupAccumulatedDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGroupAccumulatedDelay.setStatus("current")
if mibBuilder.loadTexts:
    cimaGroupAccumulatedDelay.setUnits("millisecond")


class _CimaGroupClearAccDelay_Type(TruthValue):
    """Custom type cimaGroupClearAccDelay based on TruthValue"""


_CimaGroupClearAccDelay_Object = MibTableColumn
cimaGroupClearAccDelay = _CimaGroupClearAccDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 2),
    _CimaGroupClearAccDelay_Type()
)
cimaGroupClearAccDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGroupClearAccDelay.setStatus("current")


class _CimaStuffAndCellIndication_Type(Bits):
    """Custom type cimaStuffAndCellIndication based on Bits"""
    namedValues = NamedValues(
        *(("lsibit0", 0),
          ("lsibit1", 1),
          ("lsibit2", 2))
    )

_CimaStuffAndCellIndication_Type.__name__ = "Bits"
_CimaStuffAndCellIndication_Object = MibTableColumn
cimaStuffAndCellIndication = _CimaStuffAndCellIndication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 3),
    _CimaStuffAndCellIndication_Type()
)
cimaStuffAndCellIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaStuffAndCellIndication.setStatus("current")


class _CimaGrpIntegrationUpTime_Type(MilliSeconds):
    """Custom type cimaGrpIntegrationUpTime based on MilliSeconds"""
    defaultValue = 10000

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000),
    )


_CimaGrpIntegrationUpTime_Type.__name__ = "MilliSeconds"
_CimaGrpIntegrationUpTime_Object = MibTableColumn
cimaGrpIntegrationUpTime = _CimaGrpIntegrationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 4),
    _CimaGrpIntegrationUpTime_Type()
)
cimaGrpIntegrationUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpIntegrationUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpIntegrationUpTime.setUnits("millisecond")


class _CimaGrpIntegrationDownTime_Type(MilliSeconds):
    """Custom type cimaGrpIntegrationDownTime based on MilliSeconds"""
    defaultValue = 2500

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CimaGrpIntegrationDownTime_Type.__name__ = "MilliSeconds"
_CimaGrpIntegrationDownTime_Object = MibTableColumn
cimaGrpIntegrationDownTime = _CimaGrpIntegrationDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 5),
    _CimaGrpIntegrationDownTime_Type()
)
cimaGrpIntegrationDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpIntegrationDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpIntegrationDownTime.setUnits("millisecond")
_CimaGrpNumTxIcpCells_Type = Counter32
_CimaGrpNumTxIcpCells_Object = MibTableColumn
cimaGrpNumTxIcpCells = _CimaGrpNumTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 6),
    _CimaGrpNumTxIcpCells_Type()
)
cimaGrpNumTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumTxIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumTxIcpCells.setUnits("cells")
_CimaGrpNumRxIcpCells_Type = Counter32
_CimaGrpNumRxIcpCells_Object = MibTableColumn
cimaGrpNumRxIcpCells = _CimaGrpNumRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 7),
    _CimaGrpNumRxIcpCells_Type()
)
cimaGrpNumRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumRxIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumRxIcpCells.setUnits("cells")
_CimaGrpNumRxErrIcpCells_Type = Counter32
_CimaGrpNumRxErrIcpCells_Object = MibTableColumn
cimaGrpNumRxErrIcpCells = _CimaGrpNumRxErrIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 8),
    _CimaGrpNumRxErrIcpCells_Type()
)
cimaGrpNumRxErrIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumRxErrIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumRxErrIcpCells.setUnits("cells")
_CimaGrpNumRxInvalidIcpCells_Type = Counter32
_CimaGrpNumRxInvalidIcpCells_Object = MibTableColumn
cimaGrpNumRxInvalidIcpCells = _CimaGrpNumRxInvalidIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 9),
    _CimaGrpNumRxInvalidIcpCells_Type()
)
cimaGrpNumRxInvalidIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumRxInvalidIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumRxInvalidIcpCells.setUnits("cells")
_CimaGrpNumRxMissingIcpCells_Type = Counter32
_CimaGrpNumRxMissingIcpCells_Object = MibTableColumn
cimaGrpNumRxMissingIcpCells = _CimaGrpNumRxMissingIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 10),
    _CimaGrpNumRxMissingIcpCells_Type()
)
cimaGrpNumRxMissingIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumRxMissingIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumRxMissingIcpCells.setUnits("cells")
_CimaGrpNumTxMissingIcpCells_Type = Counter32
_CimaGrpNumTxMissingIcpCells_Object = MibTableColumn
cimaGrpNumTxMissingIcpCells = _CimaGrpNumTxMissingIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 11),
    _CimaGrpNumTxMissingIcpCells_Type()
)
cimaGrpNumTxMissingIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpNumTxMissingIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpNumTxMissingIcpCells.setUnits("cells")


class _CimaGrpRestarting_Type(TruthValue):
    """Custom type cimaGrpRestarting based on TruthValue"""


_CimaGrpRestarting_Object = MibTableColumn
cimaGrpRestarting = _CimaGrpRestarting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 12),
    _CimaGrpRestarting_Type()
)
cimaGrpRestarting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpRestarting.setStatus("current")


class _CimaGrpNeVersion_Type(Integer32):
    """Custom type cimaGrpNeVersion based on Integer32"""
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
        *(("others", 1),
          ("version10", 2),
          ("version11", 3))
    )


_CimaGrpNeVersion_Type.__name__ = "Integer32"
_CimaGrpNeVersion_Object = MibTableColumn
cimaGrpNeVersion = _CimaGrpNeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 13),
    _CimaGrpNeVersion_Type()
)
cimaGrpNeVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpNeVersion.setStatus("current")
_CimaGrpMaxCellRate_Type = Gauge32
_CimaGrpMaxCellRate_Object = MibTableColumn
cimaGrpMaxCellRate = _CimaGrpMaxCellRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 14),
    _CimaGrpMaxCellRate_Type()
)
cimaGrpMaxCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpMaxCellRate.setStatus("current")
if mibBuilder.loadTexts:
    cimaGrpMaxCellRate.setUnits("cells per second")


class _CimaGrpVerFallbackEnable_Type(TruthValue):
    """Custom type cimaGrpVerFallbackEnable based on TruthValue"""


_CimaGrpVerFallbackEnable_Object = MibTableColumn
cimaGrpVerFallbackEnable = _CimaGrpVerFallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 15),
    _CimaGrpVerFallbackEnable_Type()
)
cimaGrpVerFallbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpVerFallbackEnable.setStatus("current")


class _CimaGrpAutoRestartMode_Type(Integer32):
    """Custom type cimaGrpAutoRestartMode based on Integer32"""
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
        *(("disable", 1),
          ("relearn", 2),
          ("reuse", 3))
    )


_CimaGrpAutoRestartMode_Type.__name__ = "Integer32"
_CimaGrpAutoRestartMode_Object = MibTableColumn
cimaGrpAutoRestartMode = _CimaGrpAutoRestartMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 16),
    _CimaGrpAutoRestartMode_Type()
)
cimaGrpAutoRestartMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpAutoRestartMode.setStatus("current")


class _CimaGrpRxImaIdExpected_Type(Integer32):
    """Custom type cimaGrpRxImaIdExpected based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CimaGrpRxImaIdExpected_Type.__name__ = "Integer32"
_CimaGrpRxImaIdExpected_Object = MibTableColumn
cimaGrpRxImaIdExpected = _CimaGrpRxImaIdExpected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 17),
    _CimaGrpRxImaIdExpected_Type()
)
cimaGrpRxImaIdExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaGrpRxImaIdExpected.setStatus("current")


class _CimaGrpAutoRestartSyncState_Type(Integer32):
    """Custom type cimaGrpAutoRestartSyncState based on Integer32"""
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
        *(("disable", 1),
          ("feSync", 5),
          ("inProgress", 2),
          ("loopbackSync", 3),
          ("tempSync", 4))
    )


_CimaGrpAutoRestartSyncState_Type.__name__ = "Integer32"
_CimaGrpAutoRestartSyncState_Object = MibTableColumn
cimaGrpAutoRestartSyncState = _CimaGrpAutoRestartSyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 3, 1, 18),
    _CimaGrpAutoRestartSyncState_Type()
)
cimaGrpAutoRestartSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaGrpAutoRestartSyncState.setStatus("current")
_CimaLinkMappingTable_Object = MibTable
cimaLinkMappingTable = _CimaLinkMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 4)
)
if mibBuilder.loadTexts:
    cimaLinkMappingTable.setStatus("current")
_CimaLinkMappingEntry_Object = MibTableRow
cimaLinkMappingEntry = _CimaLinkMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 4, 1)
)
cimaLinkMappingEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
    (0, "IMA-MIB", "imaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cimaLinkMappingEntry.setStatus("current")


class _CimaLinkState_Type(Integer32):
    """Custom type cimaLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonactive", 2))
    )


_CimaLinkState_Type.__name__ = "Integer32"
_CimaLinkState_Object = MibTableColumn
cimaLinkState = _CimaLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 4, 1, 1),
    _CimaLinkState_Type()
)
cimaLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkState.setStatus("current")
_CimaLinkTable_Object = MibTable
cimaLinkTable = _CimaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5)
)
if mibBuilder.loadTexts:
    cimaLinkTable.setStatus("current")
_CimaLinkEntry_Object = MibTableRow
cimaLinkEntry = _CimaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cimaLinkEntry.setStatus("current")


class _CimaLinkLifIntUpTime_Type(MilliSeconds):
    """Custom type cimaLinkLifIntUpTime based on MilliSeconds"""
    defaultValue = 2500

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_CimaLinkLifIntUpTime_Type.__name__ = "MilliSeconds"
_CimaLinkLifIntUpTime_Object = MibTableColumn
cimaLinkLifIntUpTime = _CimaLinkLifIntUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 1),
    _CimaLinkLifIntUpTime_Type()
)
cimaLinkLifIntUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaLinkLifIntUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkLifIntUpTime.setUnits("millisecond")


class _CimaLinkLifIntDownTime_Type(MilliSeconds):
    """Custom type cimaLinkLifIntDownTime based on MilliSeconds"""
    defaultValue = 10000

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_CimaLinkLifIntDownTime_Type.__name__ = "MilliSeconds"
_CimaLinkLifIntDownTime_Object = MibTableColumn
cimaLinkLifIntDownTime = _CimaLinkLifIntDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 2),
    _CimaLinkLifIntDownTime_Type()
)
cimaLinkLifIntDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaLinkLifIntDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkLifIntDownTime.setUnits("millisecond")


class _CimaLinkLodsIntUpTime_Type(MilliSeconds):
    """Custom type cimaLinkLodsIntUpTime based on MilliSeconds"""
    defaultValue = 2500

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_CimaLinkLodsIntUpTime_Type.__name__ = "MilliSeconds"
_CimaLinkLodsIntUpTime_Object = MibTableColumn
cimaLinkLodsIntUpTime = _CimaLinkLodsIntUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 3),
    _CimaLinkLodsIntUpTime_Type()
)
cimaLinkLodsIntUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaLinkLodsIntUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkLodsIntUpTime.setUnits("millisecond")


class _CimaLinkLodsIntDownTime_Type(MilliSeconds):
    """Custom type cimaLinkLodsIntDownTime based on MilliSeconds"""
    defaultValue = 10000

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_CimaLinkLodsIntDownTime_Type.__name__ = "MilliSeconds"
_CimaLinkLodsIntDownTime_Object = MibTableColumn
cimaLinkLodsIntDownTime = _CimaLinkLodsIntDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 4),
    _CimaLinkLodsIntDownTime_Type()
)
cimaLinkLodsIntDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cimaLinkLodsIntDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkLodsIntDownTime.setUnits("millisecond")
_CimaLinkNumTxIcpCells_Type = Counter32
_CimaLinkNumTxIcpCells_Object = MibTableColumn
cimaLinkNumTxIcpCells = _CimaLinkNumTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 5),
    _CimaLinkNumTxIcpCells_Type()
)
cimaLinkNumTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumTxIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumTxIcpCells.setUnits("cells")
_CimaLinkNumRxIcpCells_Type = Counter32
_CimaLinkNumRxIcpCells_Object = MibTableColumn
cimaLinkNumRxIcpCells = _CimaLinkNumRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 6),
    _CimaLinkNumRxIcpCells_Type()
)
cimaLinkNumRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumRxIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumRxIcpCells.setUnits("cells")
_CimaLinkNumRxErrIcpCells_Type = Counter32
_CimaLinkNumRxErrIcpCells_Object = MibTableColumn
cimaLinkNumRxErrIcpCells = _CimaLinkNumRxErrIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 7),
    _CimaLinkNumRxErrIcpCells_Type()
)
cimaLinkNumRxErrIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumRxErrIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumRxErrIcpCells.setUnits("cells")
_CimaLinkNumRxInvalidIcpCells_Type = Counter32
_CimaLinkNumRxInvalidIcpCells_Object = MibTableColumn
cimaLinkNumRxInvalidIcpCells = _CimaLinkNumRxInvalidIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 8),
    _CimaLinkNumRxInvalidIcpCells_Type()
)
cimaLinkNumRxInvalidIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumRxInvalidIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumRxInvalidIcpCells.setUnits("cells")
_CimaLinkNumRxMissingIcpCells_Type = Counter32
_CimaLinkNumRxMissingIcpCells_Object = MibTableColumn
cimaLinkNumRxMissingIcpCells = _CimaLinkNumRxMissingIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 9),
    _CimaLinkNumRxMissingIcpCells_Type()
)
cimaLinkNumRxMissingIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumRxMissingIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumRxMissingIcpCells.setUnits("cells")
_CimaLinkNumTxMissingIcpCells_Type = Counter32
_CimaLinkNumTxMissingIcpCells_Object = MibTableColumn
cimaLinkNumTxMissingIcpCells = _CimaLinkNumTxMissingIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 5, 1, 10),
    _CimaLinkNumTxMissingIcpCells_Type()
)
cimaLinkNumTxMissingIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaLinkNumTxMissingIcpCells.setStatus("current")
if mibBuilder.loadTexts:
    cimaLinkNumTxMissingIcpCells.setUnits("cells")
_CimaFeatureTable_Object = MibTable
cimaFeatureTable = _CimaFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6)
)
if mibBuilder.loadTexts:
    cimaFeatureTable.setStatus("current")
_CimaFeatureEntry_Object = MibTableRow
cimaFeatureEntry = _CimaFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1)
)
cimaFeatureEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cimaFeatureEntry.setStatus("current")


class _CimaMaxImaGroupsSupported_Type(Unsigned32):
    """Custom type cimaMaxImaGroupsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CimaMaxImaGroupsSupported_Type.__name__ = "Unsigned32"
_CimaMaxImaGroupsSupported_Object = MibTableColumn
cimaMaxImaGroupsSupported = _CimaMaxImaGroupsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 1),
    _CimaMaxImaGroupsSupported_Type()
)
cimaMaxImaGroupsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaMaxImaGroupsSupported.setStatus("current")


class _CimaConfiguredImaGroups_Type(Gauge32):
    """Custom type cimaConfiguredImaGroups based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CimaConfiguredImaGroups_Type.__name__ = "Gauge32"
_CimaConfiguredImaGroups_Object = MibTableColumn
cimaConfiguredImaGroups = _CimaConfiguredImaGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 2),
    _CimaConfiguredImaGroups_Type()
)
cimaConfiguredImaGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimaConfiguredImaGroups.setStatus("current")


class _CimaMinGrpTxImaId_Type(Unsigned32):
    """Custom type cimaMinGrpTxImaId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CimaMinGrpTxImaId_Type.__name__ = "Unsigned32"
_CimaMinGrpTxImaId_Object = MibTableColumn
cimaMinGrpTxImaId = _CimaMinGrpTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 3),
    _CimaMinGrpTxImaId_Type()
)
cimaMinGrpTxImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimaMinGrpTxImaId.setStatus("current")


class _CimaMaxGrpTxImaId_Type(Unsigned32):
    """Custom type cimaMaxGrpTxImaId based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CimaMaxGrpTxImaId_Type.__name__ = "Unsigned32"
_CimaMaxGrpTxImaId_Object = MibTableColumn
cimaMaxGrpTxImaId = _CimaMaxGrpTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 4),
    _CimaMaxGrpTxImaId_Type()
)
cimaMaxGrpTxImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimaMaxGrpTxImaId.setStatus("current")


class _CimaVerFallbackEnable_Type(TruthValue):
    """Custom type cimaVerFallbackEnable based on TruthValue"""


_CimaVerFallbackEnable_Object = MibTableColumn
cimaVerFallbackEnable = _CimaVerFallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 5),
    _CimaVerFallbackEnable_Type()
)
cimaVerFallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimaVerFallbackEnable.setStatus("current")


class _CimaAutoRestartEnable_Type(TruthValue):
    """Custom type cimaAutoRestartEnable based on TruthValue"""


_CimaAutoRestartEnable_Object = MibTableColumn
cimaAutoRestartEnable = _CimaAutoRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 1, 6, 1, 6),
    _CimaAutoRestartEnable_Type()
)
cimaAutoRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimaAutoRestartEnable.setStatus("current")
_CiscoImaMIBConformance_ObjectIdentity = ObjectIdentity
ciscoImaMIBConformance = _CiscoImaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2)
)
_CiscoImaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoImaMIBCompliances = _CiscoImaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 1)
)
_CiscoImaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoImaMIBGroups = _CiscoImaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2)
)
imaGroupEntry.registerAugmentions(
    ("CISCO-IMA-MIB",
     "cimaGroupEntry")
)
cimaGroupEntry.setIndexNames(*imaGroupEntry.getIndexNames())
imaLinkEntry.registerAugmentions(
    ("CISCO-IMA-MIB",
     "cimaLinkEntry")
)
cimaLinkEntry.setIndexNames(*imaLinkEntry.getIndexNames())

# Managed Objects groups

ciscoImaGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 1)
)
ciscoImaGroupGroup.setObjects(
      *(("CISCO-IMA-MIB", "cimaGroupAccumulatedDelay"),
        ("CISCO-IMA-MIB", "cimaGroupClearAccDelay"),
        ("CISCO-IMA-MIB", "cimaStuffAndCellIndication"),
        ("CISCO-IMA-MIB", "cimaGrpIntegrationUpTime"),
        ("CISCO-IMA-MIB", "cimaGrpIntegrationDownTime"),
        ("CISCO-IMA-MIB", "cimaGrpNumTxIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpNumRxIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpNumRxErrIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpNumRxInvalidIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpNumRxMissingIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpNumTxMissingIcpCells"),
        ("CISCO-IMA-MIB", "cimaGrpRestarting"),
        ("CISCO-IMA-MIB", "cimaGrpNeVersion"),
        ("CISCO-IMA-MIB", "cimaGrpMaxCellRate"))
)
if mibBuilder.loadTexts:
    ciscoImaGroupGroup.setStatus("current")

ciscoImaLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 2)
)
ciscoImaLinkGroup.setObjects(
      *(("CISCO-IMA-MIB", "cimaLinkLifIntUpTime"),
        ("CISCO-IMA-MIB", "cimaLinkLodsIntUpTime"),
        ("CISCO-IMA-MIB", "cimaLinkLifIntDownTime"),
        ("CISCO-IMA-MIB", "cimaLinkLodsIntDownTime"),
        ("CISCO-IMA-MIB", "cimaLinkNumTxIcpCells"),
        ("CISCO-IMA-MIB", "cimaLinkNumRxIcpCells"),
        ("CISCO-IMA-MIB", "cimaLinkNumRxErrIcpCells"),
        ("CISCO-IMA-MIB", "cimaLinkNumRxInvalidIcpCells"),
        ("CISCO-IMA-MIB", "cimaLinkNumRxMissingIcpCells"),
        ("CISCO-IMA-MIB", "cimaLinkNumTxMissingIcpCells"))
)
if mibBuilder.loadTexts:
    ciscoImaLinkGroup.setStatus("current")

ciscoImaLinkMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 3)
)
ciscoImaLinkMappingGroup.setObjects(
    ("CISCO-IMA-MIB", "cimaLinkState")
)
if mibBuilder.loadTexts:
    ciscoImaLinkMappingGroup.setStatus("current")

ciscoImaAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 4)
)
ciscoImaAlarmGroup.setObjects(
      *(("CISCO-IMA-MIB", "cimaGrpAlarmType"),
        ("CISCO-IMA-MIB", "cimaLinkAlarmType"))
)
if mibBuilder.loadTexts:
    ciscoImaAlarmGroup.setStatus("deprecated")

ciscoImaFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 5)
)
ciscoImaFeatureGroup.setObjects(
      *(("CISCO-IMA-MIB", "cimaMaxImaGroupsSupported"),
        ("CISCO-IMA-MIB", "cimaConfiguredImaGroups"),
        ("CISCO-IMA-MIB", "cimaMinGrpTxImaId"),
        ("CISCO-IMA-MIB", "cimaMaxGrpTxImaId"),
        ("CISCO-IMA-MIB", "cimaVerFallbackEnable"),
        ("CISCO-IMA-MIB", "cimaAutoRestartEnable"))
)
if mibBuilder.loadTexts:
    ciscoImaFeatureGroup.setStatus("current")

ciscoImaAutoRestartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 6)
)
ciscoImaAutoRestartGroup.setObjects(
      *(("CISCO-IMA-MIB", "cimaGrpAutoRestartMode"),
        ("CISCO-IMA-MIB", "cimaGrpRxImaIdExpected"),
        ("CISCO-IMA-MIB", "cimaGrpAutoRestartSyncState"))
)
if mibBuilder.loadTexts:
    ciscoImaAutoRestartGroup.setStatus("current")

ciscoImaVerFallbackSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 2, 7)
)
ciscoImaVerFallbackSupportGroup.setObjects(
    ("CISCO-IMA-MIB", "cimaGrpVerFallbackEnable")
)
if mibBuilder.loadTexts:
    ciscoImaVerFallbackSupportGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoImaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImaMIBCompliance.setStatus(
        "deprecated"
    )

ciscoImaMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 235, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoImaMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMA-MIB",
    **{"CiscoImaGrpAlarmType": CiscoImaGrpAlarmType,
       "CiscoImaLinkAlarmType": CiscoImaLinkAlarmType,
       "ciscoImaMIB": ciscoImaMIB,
       "ciscoImaMIBObjects": ciscoImaMIBObjects,
       "cimaGrpAlarmType": cimaGrpAlarmType,
       "cimaLinkAlarmType": cimaLinkAlarmType,
       "cimaGroupTable": cimaGroupTable,
       "cimaGroupEntry": cimaGroupEntry,
       "cimaGroupAccumulatedDelay": cimaGroupAccumulatedDelay,
       "cimaGroupClearAccDelay": cimaGroupClearAccDelay,
       "cimaStuffAndCellIndication": cimaStuffAndCellIndication,
       "cimaGrpIntegrationUpTime": cimaGrpIntegrationUpTime,
       "cimaGrpIntegrationDownTime": cimaGrpIntegrationDownTime,
       "cimaGrpNumTxIcpCells": cimaGrpNumTxIcpCells,
       "cimaGrpNumRxIcpCells": cimaGrpNumRxIcpCells,
       "cimaGrpNumRxErrIcpCells": cimaGrpNumRxErrIcpCells,
       "cimaGrpNumRxInvalidIcpCells": cimaGrpNumRxInvalidIcpCells,
       "cimaGrpNumRxMissingIcpCells": cimaGrpNumRxMissingIcpCells,
       "cimaGrpNumTxMissingIcpCells": cimaGrpNumTxMissingIcpCells,
       "cimaGrpRestarting": cimaGrpRestarting,
       "cimaGrpNeVersion": cimaGrpNeVersion,
       "cimaGrpMaxCellRate": cimaGrpMaxCellRate,
       "cimaGrpVerFallbackEnable": cimaGrpVerFallbackEnable,
       "cimaGrpAutoRestartMode": cimaGrpAutoRestartMode,
       "cimaGrpRxImaIdExpected": cimaGrpRxImaIdExpected,
       "cimaGrpAutoRestartSyncState": cimaGrpAutoRestartSyncState,
       "cimaLinkMappingTable": cimaLinkMappingTable,
       "cimaLinkMappingEntry": cimaLinkMappingEntry,
       "cimaLinkState": cimaLinkState,
       "cimaLinkTable": cimaLinkTable,
       "cimaLinkEntry": cimaLinkEntry,
       "cimaLinkLifIntUpTime": cimaLinkLifIntUpTime,
       "cimaLinkLifIntDownTime": cimaLinkLifIntDownTime,
       "cimaLinkLodsIntUpTime": cimaLinkLodsIntUpTime,
       "cimaLinkLodsIntDownTime": cimaLinkLodsIntDownTime,
       "cimaLinkNumTxIcpCells": cimaLinkNumTxIcpCells,
       "cimaLinkNumRxIcpCells": cimaLinkNumRxIcpCells,
       "cimaLinkNumRxErrIcpCells": cimaLinkNumRxErrIcpCells,
       "cimaLinkNumRxInvalidIcpCells": cimaLinkNumRxInvalidIcpCells,
       "cimaLinkNumRxMissingIcpCells": cimaLinkNumRxMissingIcpCells,
       "cimaLinkNumTxMissingIcpCells": cimaLinkNumTxMissingIcpCells,
       "cimaFeatureTable": cimaFeatureTable,
       "cimaFeatureEntry": cimaFeatureEntry,
       "cimaMaxImaGroupsSupported": cimaMaxImaGroupsSupported,
       "cimaConfiguredImaGroups": cimaConfiguredImaGroups,
       "cimaMinGrpTxImaId": cimaMinGrpTxImaId,
       "cimaMaxGrpTxImaId": cimaMaxGrpTxImaId,
       "cimaVerFallbackEnable": cimaVerFallbackEnable,
       "cimaAutoRestartEnable": cimaAutoRestartEnable,
       "ciscoImaMIBConformance": ciscoImaMIBConformance,
       "ciscoImaMIBCompliances": ciscoImaMIBCompliances,
       "ciscoImaMIBCompliance": ciscoImaMIBCompliance,
       "ciscoImaMIBCompliance1": ciscoImaMIBCompliance1,
       "ciscoImaMIBGroups": ciscoImaMIBGroups,
       "ciscoImaGroupGroup": ciscoImaGroupGroup,
       "ciscoImaLinkGroup": ciscoImaLinkGroup,
       "ciscoImaLinkMappingGroup": ciscoImaLinkMappingGroup,
       "ciscoImaAlarmGroup": ciscoImaAlarmGroup,
       "ciscoImaFeatureGroup": ciscoImaFeatureGroup,
       "ciscoImaAutoRestartGroup": ciscoImaAutoRestartGroup,
       "ciscoImaVerFallbackSupportGroup": ciscoImaVerFallbackSupportGroup}
)
