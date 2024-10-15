# SNMP MIB module (PAIRGAIN-SDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-SDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:24 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainSDSL,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainSDSL")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pgsdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1)
)


# Types definitions



class Byte(Integer32):
    """Custom type Byte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Short(Integer32):
    """Custom type Short based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class SdslLineProfileType(Integer32):
    """Custom type SdslLineProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class PgSdslTimeStamp(OctetString):
    """Custom type PgSdslTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class PgSdslAlarmSeverityMode(Integer32):
    """Custom type PgSdslAlarmSeverityMode based on Integer32"""
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
          ("enable", 2),
          ("notAvailable", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdslMibObjects_ObjectIdentity = ObjectIdentity
sdslMibObjects = _SdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1)
)
_Sdsl15mPerformanceTable_Object = MibTable
sdsl15mPerformanceTable = _Sdsl15mPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sdsl15mPerformanceTable.setStatus("current")
_Sdsl15mPerformanceEntry_Object = MibTableRow
sdsl15mPerformanceEntry = _Sdsl15mPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1)
)
sdsl15mPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PAIRGAIN-SDSL-MIB", "sdsl15mHistoryId"),
)
if mibBuilder.loadTexts:
    sdsl15mPerformanceEntry.setStatus("current")
_Sdsl15mHistoryId_Type = Short
_Sdsl15mHistoryId_Object = MibTableColumn
sdsl15mHistoryId = _Sdsl15mHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1, 1),
    _Sdsl15mHistoryId_Type()
)
sdsl15mHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl15mHistoryId.setStatus("current")
_Sdsl15mESNet_Type = Short
_Sdsl15mESNet_Object = MibTableColumn
sdsl15mESNet = _Sdsl15mESNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1, 2),
    _Sdsl15mESNet_Type()
)
sdsl15mESNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl15mESNet.setStatus("current")
_Sdsl15mUASNet_Type = Short
_Sdsl15mUASNet_Object = MibTableColumn
sdsl15mUASNet = _Sdsl15mUASNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1, 3),
    _Sdsl15mUASNet_Type()
)
sdsl15mUASNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl15mUASNet.setStatus("current")
_Sdsl15mESCust_Type = Short
_Sdsl15mESCust_Object = MibTableColumn
sdsl15mESCust = _Sdsl15mESCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1, 4),
    _Sdsl15mESCust_Type()
)
sdsl15mESCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl15mESCust.setStatus("current")
_Sdsl15mUASCust_Type = Short
_Sdsl15mUASCust_Object = MibTableColumn
sdsl15mUASCust = _Sdsl15mUASCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 1, 1, 5),
    _Sdsl15mUASCust_Type()
)
sdsl15mUASCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl15mUASCust.setStatus("current")
_Sdsl24hPerformanceTable_Object = MibTable
sdsl24hPerformanceTable = _Sdsl24hPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sdsl24hPerformanceTable.setStatus("current")
_Sdsl24hPerformanceEntry_Object = MibTableRow
sdsl24hPerformanceEntry = _Sdsl24hPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1)
)
sdsl24hPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PAIRGAIN-SDSL-MIB", "sdsl24hHistoryId"),
)
if mibBuilder.loadTexts:
    sdsl24hPerformanceEntry.setStatus("current")
_Sdsl24hHistoryId_Type = Short
_Sdsl24hHistoryId_Object = MibTableColumn
sdsl24hHistoryId = _Sdsl24hHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1, 1),
    _Sdsl24hHistoryId_Type()
)
sdsl24hHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl24hHistoryId.setStatus("current")
_Sdsl24hESNet_Type = Short
_Sdsl24hESNet_Object = MibTableColumn
sdsl24hESNet = _Sdsl24hESNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1, 2),
    _Sdsl24hESNet_Type()
)
sdsl24hESNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl24hESNet.setStatus("current")
_Sdsl24hUASNet_Type = Short
_Sdsl24hUASNet_Object = MibTableColumn
sdsl24hUASNet = _Sdsl24hUASNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1, 3),
    _Sdsl24hUASNet_Type()
)
sdsl24hUASNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl24hUASNet.setStatus("current")
_Sdsl24hESCust_Type = Short
_Sdsl24hESCust_Object = MibTableColumn
sdsl24hESCust = _Sdsl24hESCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1, 4),
    _Sdsl24hESCust_Type()
)
sdsl24hESCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl24hESCust.setStatus("current")
_Sdsl24hUASCust_Type = Short
_Sdsl24hUASCust_Object = MibTableColumn
sdsl24hUASCust = _Sdsl24hUASCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 2, 1, 5),
    _Sdsl24hUASCust_Type()
)
sdsl24hUASCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsl24hUASCust.setStatus("current")
_SdslCurr24hPerformanceTable_Object = MibTable
sdslCurr24hPerformanceTable = _SdslCurr24hPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sdslCurr24hPerformanceTable.setStatus("current")
_SdslCurr24hPerformanceEntry_Object = MibTableRow
sdslCurr24hPerformanceEntry = _SdslCurr24hPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3, 1)
)
sdslCurr24hPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdslCurr24hPerformanceEntry.setStatus("current")
_SdslCurr24hESNet_Type = Short
_SdslCurr24hESNet_Object = MibTableColumn
sdslCurr24hESNet = _SdslCurr24hESNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3, 1, 1),
    _SdslCurr24hESNet_Type()
)
sdslCurr24hESNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslCurr24hESNet.setStatus("current")
_SdslCurr24hUASNet_Type = Short
_SdslCurr24hUASNet_Object = MibTableColumn
sdslCurr24hUASNet = _SdslCurr24hUASNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3, 1, 2),
    _SdslCurr24hUASNet_Type()
)
sdslCurr24hUASNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslCurr24hUASNet.setStatus("current")
_SdslCurr24hESCust_Type = Short
_SdslCurr24hESCust_Object = MibTableColumn
sdslCurr24hESCust = _SdslCurr24hESCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3, 1, 3),
    _SdslCurr24hESCust_Type()
)
sdslCurr24hESCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslCurr24hESCust.setStatus("current")
_SdslCurr24hUASCust_Type = Short
_SdslCurr24hUASCust_Object = MibTableColumn
sdslCurr24hUASCust = _SdslCurr24hUASCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 3, 1, 4),
    _SdslCurr24hUASCust_Type()
)
sdslCurr24hUASCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslCurr24hUASCust.setStatus("current")
_SdslStatisticsTable_Object = MibTable
sdslStatisticsTable = _SdslStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sdslStatisticsTable.setStatus("current")
_SdslStatisticsEntry_Object = MibTableRow
sdslStatisticsEntry = _SdslStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1)
)
sdslStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdslStatisticsEntry.setStatus("current")
_SdslTipRingReversal_Type = Byte
_SdslTipRingReversal_Object = MibTableColumn
sdslTipRingReversal = _SdslTipRingReversal_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 1),
    _SdslTipRingReversal_Type()
)
sdslTipRingReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslTipRingReversal.setStatus("current")
_SdslUpState_Type = Byte
_SdslUpState_Object = MibTableColumn
sdslUpState = _SdslUpState_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 2),
    _SdslUpState_Type()
)
sdslUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUpState.setStatus("current")
_SdslMarginNet_Type = Byte
_SdslMarginNet_Object = MibTableColumn
sdslMarginNet = _SdslMarginNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 3),
    _SdslMarginNet_Type()
)
sdslMarginNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginNet.setStatus("current")
_SdslMarginHighNet_Type = Byte
_SdslMarginHighNet_Object = MibTableColumn
sdslMarginHighNet = _SdslMarginHighNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 4),
    _SdslMarginHighNet_Type()
)
sdslMarginHighNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginHighNet.setStatus("current")
_SdslMarginLowNet_Type = Byte
_SdslMarginLowNet_Object = MibTableColumn
sdslMarginLowNet = _SdslMarginLowNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 5),
    _SdslMarginLowNet_Type()
)
sdslMarginLowNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginLowNet.setStatus("current")
_SdslPulseAttenuationNet_Type = Byte
_SdslPulseAttenuationNet_Object = MibTableColumn
sdslPulseAttenuationNet = _SdslPulseAttenuationNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 6),
    _SdslPulseAttenuationNet_Type()
)
sdslPulseAttenuationNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslPulseAttenuationNet.setStatus("current")
_SdslMarginCust_Type = Byte
_SdslMarginCust_Object = MibTableColumn
sdslMarginCust = _SdslMarginCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 7),
    _SdslMarginCust_Type()
)
sdslMarginCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginCust.setStatus("current")
_SdslMarginHighCust_Type = Byte
_SdslMarginHighCust_Object = MibTableColumn
sdslMarginHighCust = _SdslMarginHighCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 8),
    _SdslMarginHighCust_Type()
)
sdslMarginHighCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginHighCust.setStatus("current")
_SdslMarginLowCust_Type = Byte
_SdslMarginLowCust_Object = MibTableColumn
sdslMarginLowCust = _SdslMarginLowCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 9),
    _SdslMarginLowCust_Type()
)
sdslMarginLowCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginLowCust.setStatus("current")
_SdslPulseAttenuationCust_Type = Byte
_SdslPulseAttenuationCust_Object = MibTableColumn
sdslPulseAttenuationCust = _SdslPulseAttenuationCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 4, 1, 10),
    _SdslPulseAttenuationCust_Type()
)
sdslPulseAttenuationCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslPulseAttenuationCust.setStatus("current")
_SdslLineTable_Object = MibTable
sdslLineTable = _SdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sdslLineTable.setStatus("current")
_SdslLineEntry_Object = MibTableRow
sdslLineEntry = _SdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 5, 1)
)
sdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdslLineEntry.setStatus("current")
_SdslLineConfProfile_Type = SdslLineProfileType
_SdslLineConfProfile_Object = MibTableColumn
sdslLineConfProfile = _SdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 5, 1, 1),
    _SdslLineConfProfile_Type()
)
sdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineConfProfile.setStatus("current")
_SdslLineAlarmConfProfile_Type = SdslLineProfileType
_SdslLineAlarmConfProfile_Object = MibTableColumn
sdslLineAlarmConfProfile = _SdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 5, 1, 2),
    _SdslLineAlarmConfProfile_Type()
)
sdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfile.setStatus("current")
_SdslAlarmTable_Object = MibTable
sdslAlarmTable = _SdslAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sdslAlarmTable.setStatus("current")
_SdslAlarmEntry_Object = MibTableRow
sdslAlarmEntry = _SdslAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1)
)
sdslAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdslAlarmEntry.setStatus("current")
_SdslMarginAlarmNet_Type = Byte
_SdslMarginAlarmNet_Object = MibTableColumn
sdslMarginAlarmNet = _SdslMarginAlarmNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 1),
    _SdslMarginAlarmNet_Type()
)
sdslMarginAlarmNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginAlarmNet.setStatus("current")
_SdslESAlarmNet_Type = Byte
_SdslESAlarmNet_Object = MibTableColumn
sdslESAlarmNet = _SdslESAlarmNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 2),
    _SdslESAlarmNet_Type()
)
sdslESAlarmNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslESAlarmNet.setStatus("current")
_SdslUASAlarmNet_Type = Byte
_SdslUASAlarmNet_Object = MibTableColumn
sdslUASAlarmNet = _SdslUASAlarmNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 3),
    _SdslUASAlarmNet_Type()
)
sdslUASAlarmNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUASAlarmNet.setStatus("current")
_SdslMarginAlarmCust_Type = Byte
_SdslMarginAlarmCust_Object = MibTableColumn
sdslMarginAlarmCust = _SdslMarginAlarmCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 4),
    _SdslMarginAlarmCust_Type()
)
sdslMarginAlarmCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginAlarmCust.setStatus("current")
_SdslESAlarmCust_Type = Byte
_SdslESAlarmCust_Object = MibTableColumn
sdslESAlarmCust = _SdslESAlarmCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 5),
    _SdslESAlarmCust_Type()
)
sdslESAlarmCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslESAlarmCust.setStatus("current")
_SdslUASAlarmCust_Type = Byte
_SdslUASAlarmCust_Object = MibTableColumn
sdslUASAlarmCust = _SdslUASAlarmCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 6),
    _SdslUASAlarmCust_Type()
)
sdslUASAlarmCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUASAlarmCust.setStatus("current")
_SdslLOSWAlarm_Type = Byte
_SdslLOSWAlarm_Object = MibTableColumn
sdslLOSWAlarm = _SdslLOSWAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 6, 1, 7),
    _SdslLOSWAlarm_Type()
)
sdslLOSWAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLOSWAlarm.setStatus("current")
_SdslAlarmHistoryTable_Object = MibTable
sdslAlarmHistoryTable = _SdslAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sdslAlarmHistoryTable.setStatus("current")
_SdslAlarmHistoryEntry_Object = MibTableRow
sdslAlarmHistoryEntry = _SdslAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1)
)
sdslAlarmHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdslAlarmHistoryEntry.setStatus("current")
_SdslMarginAlarmFirst_Type = PgSdslTimeStamp
_SdslMarginAlarmFirst_Object = MibTableColumn
sdslMarginAlarmFirst = _SdslMarginAlarmFirst_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 1),
    _SdslMarginAlarmFirst_Type()
)
sdslMarginAlarmFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginAlarmFirst.setStatus("current")
_SdslMarginAlarmLast_Type = PgSdslTimeStamp
_SdslMarginAlarmLast_Object = MibTableColumn
sdslMarginAlarmLast = _SdslMarginAlarmLast_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 2),
    _SdslMarginAlarmLast_Type()
)
sdslMarginAlarmLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginAlarmLast.setStatus("current")
_SdslMarginAlarmCount_Type = Short
_SdslMarginAlarmCount_Object = MibTableColumn
sdslMarginAlarmCount = _SdslMarginAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 3),
    _SdslMarginAlarmCount_Type()
)
sdslMarginAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslMarginAlarmCount.setStatus("current")
_SdslESAlarmFirst_Type = PgSdslTimeStamp
_SdslESAlarmFirst_Object = MibTableColumn
sdslESAlarmFirst = _SdslESAlarmFirst_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 4),
    _SdslESAlarmFirst_Type()
)
sdslESAlarmFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslESAlarmFirst.setStatus("current")
_SdslESAlarmLast_Type = PgSdslTimeStamp
_SdslESAlarmLast_Object = MibTableColumn
sdslESAlarmLast = _SdslESAlarmLast_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 5),
    _SdslESAlarmLast_Type()
)
sdslESAlarmLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslESAlarmLast.setStatus("current")
_SdslESAlarmCount_Type = Short
_SdslESAlarmCount_Object = MibTableColumn
sdslESAlarmCount = _SdslESAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 6),
    _SdslESAlarmCount_Type()
)
sdslESAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslESAlarmCount.setStatus("current")
_SdslUASAlarmFirst_Type = PgSdslTimeStamp
_SdslUASAlarmFirst_Object = MibTableColumn
sdslUASAlarmFirst = _SdslUASAlarmFirst_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 7),
    _SdslUASAlarmFirst_Type()
)
sdslUASAlarmFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUASAlarmFirst.setStatus("current")
_SdslUASAlarmLast_Type = PgSdslTimeStamp
_SdslUASAlarmLast_Object = MibTableColumn
sdslUASAlarmLast = _SdslUASAlarmLast_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 8),
    _SdslUASAlarmLast_Type()
)
sdslUASAlarmLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUASAlarmLast.setStatus("current")
_SdslUASAlarmCount_Type = Short
_SdslUASAlarmCount_Object = MibTableColumn
sdslUASAlarmCount = _SdslUASAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 9),
    _SdslUASAlarmCount_Type()
)
sdslUASAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslUASAlarmCount.setStatus("current")
_SdslLOSWAlarmFirst_Type = PgSdslTimeStamp
_SdslLOSWAlarmFirst_Object = MibTableColumn
sdslLOSWAlarmFirst = _SdslLOSWAlarmFirst_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 10),
    _SdslLOSWAlarmFirst_Type()
)
sdslLOSWAlarmFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLOSWAlarmFirst.setStatus("current")
_SdslLOSWAlarmLast_Type = PgSdslTimeStamp
_SdslLOSWAlarmLast_Object = MibTableColumn
sdslLOSWAlarmLast = _SdslLOSWAlarmLast_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 11),
    _SdslLOSWAlarmLast_Type()
)
sdslLOSWAlarmLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLOSWAlarmLast.setStatus("current")
_SdslLOSWAlarmCount_Type = Short
_SdslLOSWAlarmCount_Object = MibTableColumn
sdslLOSWAlarmCount = _SdslLOSWAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 7, 1, 12),
    _SdslLOSWAlarmCount_Type()
)
sdslLOSWAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLOSWAlarmCount.setStatus("current")


class _SdslLineConfProfileIndexNext_Type(Integer32):
    """Custom type sdslLineConfProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdslLineConfProfileIndexNext_Type.__name__ = "Integer32"
_SdslLineConfProfileIndexNext_Object = MibScalar
sdslLineConfProfileIndexNext = _SdslLineConfProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 8),
    _SdslLineConfProfileIndexNext_Type()
)
sdslLineConfProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineConfProfileIndexNext.setStatus("current")
_SdslLineConfProfileTable_Object = MibTable
sdslLineConfProfileTable = _SdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sdslLineConfProfileTable.setStatus("current")
_SdslLineConfProfileEntry_Object = MibTableRow
sdslLineConfProfileEntry = _SdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1)
)
sdslLineConfProfileEntry.setIndexNames(
    (0, "PAIRGAIN-SDSL-MIB", "sdslLineConfProfileIndex"),
)
if mibBuilder.loadTexts:
    sdslLineConfProfileEntry.setStatus("current")
_SdslLineConfProfileIndex_Type = SdslLineProfileType
_SdslLineConfProfileIndex_Object = MibTableColumn
sdslLineConfProfileIndex = _SdslLineConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1, 1),
    _SdslLineConfProfileIndex_Type()
)
sdslLineConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdslLineConfProfileIndex.setStatus("current")


class _SdslRateMode_Type(Integer32):
    """Custom type sdslRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_SdslRateMode_Type.__name__ = "Integer32"
_SdslRateMode_Object = MibTableColumn
sdslRateMode = _SdslRateMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1, 2),
    _SdslRateMode_Type()
)
sdslRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslRateMode.setStatus("current")
_SdslRemFeatures_Type = Short
_SdslRemFeatures_Object = MibTableColumn
sdslRemFeatures = _SdslRemFeatures_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1, 3),
    _SdslRemFeatures_Type()
)
sdslRemFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslRemFeatures.setStatus("current")


class _SdslRate_Type(Integer32):
    """Custom type sdslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_SdslRate_Type.__name__ = "Integer32"
_SdslRate_Object = MibTableColumn
sdslRate = _SdslRate_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1, 4),
    _SdslRate_Type()
)
sdslRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslRate.setStatus("current")
if mibBuilder.loadTexts:
    sdslRate.setUnits("kbps")
_SdslLineConfProfileRowStatus_Type = RowStatus
_SdslLineConfProfileRowStatus_Object = MibTableColumn
sdslLineConfProfileRowStatus = _SdslLineConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 9, 1, 5),
    _SdslLineConfProfileRowStatus_Type()
)
sdslLineConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdslLineConfProfileRowStatus.setStatus("current")


class _SdslLineAlarmConfProfileIndexNext_Type(Integer32):
    """Custom type sdslLineAlarmConfProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdslLineAlarmConfProfileIndexNext_Type.__name__ = "Integer32"
_SdslLineAlarmConfProfileIndexNext_Object = MibScalar
sdslLineAlarmConfProfileIndexNext = _SdslLineAlarmConfProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 10),
    _SdslLineAlarmConfProfileIndexNext_Type()
)
sdslLineAlarmConfProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfileIndexNext.setStatus("current")
_SdslLineAlarmConfProfileTable_Object = MibTable
sdslLineAlarmConfProfileTable = _SdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11)
)
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfileTable.setStatus("current")
_SdslLineAlarmConfProfileEntry_Object = MibTableRow
sdslLineAlarmConfProfileEntry = _SdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1)
)
sdslLineAlarmConfProfileEntry.setIndexNames(
    (0, "PAIRGAIN-SDSL-MIB", "sdslLineAlarmConfProfileIndex"),
)
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfileEntry.setStatus("current")
_SdslLineAlarmConfProfileIndex_Type = SdslLineProfileType
_SdslLineAlarmConfProfileIndex_Object = MibTableColumn
sdslLineAlarmConfProfileIndex = _SdslLineAlarmConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 1),
    _SdslLineAlarmConfProfileIndex_Type()
)
sdslLineAlarmConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfileIndex.setStatus("current")
_SdslLOSWAlarmSetting_Type = PgSdslAlarmSeverityMode
_SdslLOSWAlarmSetting_Object = MibTableColumn
sdslLOSWAlarmSetting = _SdslLOSWAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 2),
    _SdslLOSWAlarmSetting_Type()
)
sdslLOSWAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLOSWAlarmSetting.setStatus("current")
_SdslMarginThreshold_Type = Byte
_SdslMarginThreshold_Object = MibTableColumn
sdslMarginThreshold = _SdslMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 3),
    _SdslMarginThreshold_Type()
)
sdslMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslMarginThreshold.setStatus("current")
_SdslMarginAlarmSetting_Type = PgSdslAlarmSeverityMode
_SdslMarginAlarmSetting_Object = MibTableColumn
sdslMarginAlarmSetting = _SdslMarginAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 4),
    _SdslMarginAlarmSetting_Type()
)
sdslMarginAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslMarginAlarmSetting.setStatus("current")
_SdslESThreshold_Type = Byte
_SdslESThreshold_Object = MibTableColumn
sdslESThreshold = _SdslESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 5),
    _SdslESThreshold_Type()
)
sdslESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslESThreshold.setStatus("current")
_SdslESAlarmSetting_Type = PgSdslAlarmSeverityMode
_SdslESAlarmSetting_Object = MibTableColumn
sdslESAlarmSetting = _SdslESAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 6),
    _SdslESAlarmSetting_Type()
)
sdslESAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslESAlarmSetting.setStatus("current")
_SdslUASThreshold_Type = Byte
_SdslUASThreshold_Object = MibTableColumn
sdslUASThreshold = _SdslUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 7),
    _SdslUASThreshold_Type()
)
sdslUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslUASThreshold.setStatus("current")
_SdslUASAlarmSetting_Type = PgSdslAlarmSeverityMode
_SdslUASAlarmSetting_Object = MibTableColumn
sdslUASAlarmSetting = _SdslUASAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 8),
    _SdslUASAlarmSetting_Type()
)
sdslUASAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslUASAlarmSetting.setStatus("current")
_SdslLineAlarmConfProfileRowStatus_Type = RowStatus
_SdslLineAlarmConfProfileRowStatus_Object = MibTableColumn
sdslLineAlarmConfProfileRowStatus = _SdslLineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 11, 1, 9),
    _SdslLineAlarmConfProfileRowStatus_Type()
)
sdslLineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdslLineAlarmConfProfileRowStatus.setStatus("current")
_PgSdslModGenTable_Object = MibTable
pgSdslModGenTable = _PgSdslModGenTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pgSdslModGenTable.setStatus("current")
_PgSdslModGenEntry_Object = MibTableRow
pgSdslModGenEntry = _PgSdslModGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1)
)
pgSdslModGenEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslModGenEntry.setStatus("current")
_PgSdslModGenVersionNum_Type = Byte
_PgSdslModGenVersionNum_Object = MibTableColumn
pgSdslModGenVersionNum = _PgSdslModGenVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 1),
    _PgSdslModGenVersionNum_Type()
)
pgSdslModGenVersionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenVersionNum.setStatus("current")
_PgSdslModGenListNum_Type = Byte
_PgSdslModGenListNum_Object = MibTableColumn
pgSdslModGenListNum = _PgSdslModGenListNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 2),
    _PgSdslModGenListNum_Type()
)
pgSdslModGenListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenListNum.setStatus("current")
_PgSdslModGenVendNum_Type = Byte
_PgSdslModGenVendNum_Object = MibTableColumn
pgSdslModGenVendNum = _PgSdslModGenVendNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 3),
    _PgSdslModGenVendNum_Type()
)
pgSdslModGenVendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenVendNum.setStatus("current")
_PgSdslModGenFeatures_Type = Integer32
_PgSdslModGenFeatures_Object = MibTableColumn
pgSdslModGenFeatures = _PgSdslModGenFeatures_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 4),
    _PgSdslModGenFeatures_Type()
)
pgSdslModGenFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenFeatures.setStatus("current")
_PgSdslModGenSerialNum_Type = Short
_PgSdslModGenSerialNum_Object = MibTableColumn
pgSdslModGenSerialNum = _PgSdslModGenSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 5),
    _PgSdslModGenSerialNum_Type()
)
pgSdslModGenSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenSerialNum.setStatus("current")
_PgSdslModGenMfgDate_Type = Short
_PgSdslModGenMfgDate_Object = MibTableColumn
pgSdslModGenMfgDate = _PgSdslModGenMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 12, 1, 6),
    _PgSdslModGenMfgDate_Type()
)
pgSdslModGenMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModGenMfgDate.setStatus("current")
_PgSdslModStatTable_Object = MibTable
pgSdslModStatTable = _PgSdslModStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13)
)
if mibBuilder.loadTexts:
    pgSdslModStatTable.setStatus("current")
_PgSdslModStatEntry_Object = MibTableRow
pgSdslModStatEntry = _PgSdslModStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1)
)
pgSdslModStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslModStatEntry.setStatus("current")


class _PgSdslModEthOperStatus_Type(Integer32):
    """Custom type pgSdslModEthOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_PgSdslModEthOperStatus_Type.__name__ = "Integer32"
_PgSdslModEthOperStatus_Object = MibTableColumn
pgSdslModEthOperStatus = _PgSdslModEthOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 1),
    _PgSdslModEthOperStatus_Type()
)
pgSdslModEthOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthOperStatus.setStatus("current")
_PgSdslModEthInOctets_Type = Counter32
_PgSdslModEthInOctets_Object = MibTableColumn
pgSdslModEthInOctets = _PgSdslModEthInOctets_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 2),
    _PgSdslModEthInOctets_Type()
)
pgSdslModEthInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthInOctets.setStatus("current")
_PgSdslModEthInUcastPkts_Type = Counter32
_PgSdslModEthInUcastPkts_Object = MibTableColumn
pgSdslModEthInUcastPkts = _PgSdslModEthInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 3),
    _PgSdslModEthInUcastPkts_Type()
)
pgSdslModEthInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthInUcastPkts.setStatus("current")
_PgSdslModEthInNUcastPkts_Type = Counter32
_PgSdslModEthInNUcastPkts_Object = MibTableColumn
pgSdslModEthInNUcastPkts = _PgSdslModEthInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 4),
    _PgSdslModEthInNUcastPkts_Type()
)
pgSdslModEthInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthInNUcastPkts.setStatus("current")
_PgSdslModEthInDiscards_Type = Counter32
_PgSdslModEthInDiscards_Object = MibTableColumn
pgSdslModEthInDiscards = _PgSdslModEthInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 5),
    _PgSdslModEthInDiscards_Type()
)
pgSdslModEthInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthInDiscards.setStatus("current")
_PgSdslModEthInErrors_Type = Counter32
_PgSdslModEthInErrors_Object = MibTableColumn
pgSdslModEthInErrors = _PgSdslModEthInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 6),
    _PgSdslModEthInErrors_Type()
)
pgSdslModEthInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthInErrors.setStatus("current")
_PgSdslModEthOutOctets_Type = Counter32
_PgSdslModEthOutOctets_Object = MibTableColumn
pgSdslModEthOutOctets = _PgSdslModEthOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 7),
    _PgSdslModEthOutOctets_Type()
)
pgSdslModEthOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthOutOctets.setStatus("current")
_PgSdslModEthOutUcastPkts_Type = Counter32
_PgSdslModEthOutUcastPkts_Object = MibTableColumn
pgSdslModEthOutUcastPkts = _PgSdslModEthOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 8),
    _PgSdslModEthOutUcastPkts_Type()
)
pgSdslModEthOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthOutUcastPkts.setStatus("current")
_PgSdslModEthOutNUcastPkts_Type = Counter32
_PgSdslModEthOutNUcastPkts_Object = MibTableColumn
pgSdslModEthOutNUcastPkts = _PgSdslModEthOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 9),
    _PgSdslModEthOutNUcastPkts_Type()
)
pgSdslModEthOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthOutNUcastPkts.setStatus("current")
_PgSdslModEthOutErrors_Type = Counter32
_PgSdslModEthOutErrors_Object = MibTableColumn
pgSdslModEthOutErrors = _PgSdslModEthOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 10),
    _PgSdslModEthOutErrors_Type()
)
pgSdslModEthOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModEthOutErrors.setStatus("current")
_PgSdslModDslInOctets_Type = Counter32
_PgSdslModDslInOctets_Object = MibTableColumn
pgSdslModDslInOctets = _PgSdslModDslInOctets_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 11),
    _PgSdslModDslInOctets_Type()
)
pgSdslModDslInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslInOctets.setStatus("current")
_PgSdslModDslInUcastPkts_Type = Counter32
_PgSdslModDslInUcastPkts_Object = MibTableColumn
pgSdslModDslInUcastPkts = _PgSdslModDslInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 12),
    _PgSdslModDslInUcastPkts_Type()
)
pgSdslModDslInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslInUcastPkts.setStatus("current")
_PgSdslModDslInNUcastPkts_Type = Counter32
_PgSdslModDslInNUcastPkts_Object = MibTableColumn
pgSdslModDslInNUcastPkts = _PgSdslModDslInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 13),
    _PgSdslModDslInNUcastPkts_Type()
)
pgSdslModDslInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslInNUcastPkts.setStatus("current")
_PgSdslModDslInDiscards_Type = Counter32
_PgSdslModDslInDiscards_Object = MibTableColumn
pgSdslModDslInDiscards = _PgSdslModDslInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 14),
    _PgSdslModDslInDiscards_Type()
)
pgSdslModDslInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslInDiscards.setStatus("current")
_PgSdslModDslInErrors_Type = Counter32
_PgSdslModDslInErrors_Object = MibTableColumn
pgSdslModDslInErrors = _PgSdslModDslInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 15),
    _PgSdslModDslInErrors_Type()
)
pgSdslModDslInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslInErrors.setStatus("current")
_PgSdslModDslOutOctets_Type = Counter32
_PgSdslModDslOutOctets_Object = MibTableColumn
pgSdslModDslOutOctets = _PgSdslModDslOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 16),
    _PgSdslModDslOutOctets_Type()
)
pgSdslModDslOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslOutOctets.setStatus("current")
_PgSdslModDslOutUcastPkts_Type = Counter32
_PgSdslModDslOutUcastPkts_Object = MibTableColumn
pgSdslModDslOutUcastPkts = _PgSdslModDslOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 17),
    _PgSdslModDslOutUcastPkts_Type()
)
pgSdslModDslOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslOutUcastPkts.setStatus("current")
_PgSdslModDslOutNUcastPkts_Type = Counter32
_PgSdslModDslOutNUcastPkts_Object = MibTableColumn
pgSdslModDslOutNUcastPkts = _PgSdslModDslOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 18),
    _PgSdslModDslOutNUcastPkts_Type()
)
pgSdslModDslOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslOutNUcastPkts.setStatus("current")
_PgSdslModDslOutErrors_Type = Counter32
_PgSdslModDslOutErrors_Object = MibTableColumn
pgSdslModDslOutErrors = _PgSdslModDslOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 13, 1, 1, 13, 1, 19),
    _PgSdslModDslOutErrors_Type()
)
pgSdslModDslOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslModDslOutErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-SDSL-MIB",
    **{"Byte": Byte,
       "Short": Short,
       "SdslLineProfileType": SdslLineProfileType,
       "PgSdslTimeStamp": PgSdslTimeStamp,
       "PgSdslAlarmSeverityMode": PgSdslAlarmSeverityMode,
       "pgsdslMIB": pgsdslMIB,
       "sdslMibObjects": sdslMibObjects,
       "sdsl15mPerformanceTable": sdsl15mPerformanceTable,
       "sdsl15mPerformanceEntry": sdsl15mPerformanceEntry,
       "sdsl15mHistoryId": sdsl15mHistoryId,
       "sdsl15mESNet": sdsl15mESNet,
       "sdsl15mUASNet": sdsl15mUASNet,
       "sdsl15mESCust": sdsl15mESCust,
       "sdsl15mUASCust": sdsl15mUASCust,
       "sdsl24hPerformanceTable": sdsl24hPerformanceTable,
       "sdsl24hPerformanceEntry": sdsl24hPerformanceEntry,
       "sdsl24hHistoryId": sdsl24hHistoryId,
       "sdsl24hESNet": sdsl24hESNet,
       "sdsl24hUASNet": sdsl24hUASNet,
       "sdsl24hESCust": sdsl24hESCust,
       "sdsl24hUASCust": sdsl24hUASCust,
       "sdslCurr24hPerformanceTable": sdslCurr24hPerformanceTable,
       "sdslCurr24hPerformanceEntry": sdslCurr24hPerformanceEntry,
       "sdslCurr24hESNet": sdslCurr24hESNet,
       "sdslCurr24hUASNet": sdslCurr24hUASNet,
       "sdslCurr24hESCust": sdslCurr24hESCust,
       "sdslCurr24hUASCust": sdslCurr24hUASCust,
       "sdslStatisticsTable": sdslStatisticsTable,
       "sdslStatisticsEntry": sdslStatisticsEntry,
       "sdslTipRingReversal": sdslTipRingReversal,
       "sdslUpState": sdslUpState,
       "sdslMarginNet": sdslMarginNet,
       "sdslMarginHighNet": sdslMarginHighNet,
       "sdslMarginLowNet": sdslMarginLowNet,
       "sdslPulseAttenuationNet": sdslPulseAttenuationNet,
       "sdslMarginCust": sdslMarginCust,
       "sdslMarginHighCust": sdslMarginHighCust,
       "sdslMarginLowCust": sdslMarginLowCust,
       "sdslPulseAttenuationCust": sdslPulseAttenuationCust,
       "sdslLineTable": sdslLineTable,
       "sdslLineEntry": sdslLineEntry,
       "sdslLineConfProfile": sdslLineConfProfile,
       "sdslLineAlarmConfProfile": sdslLineAlarmConfProfile,
       "sdslAlarmTable": sdslAlarmTable,
       "sdslAlarmEntry": sdslAlarmEntry,
       "sdslMarginAlarmNet": sdslMarginAlarmNet,
       "sdslESAlarmNet": sdslESAlarmNet,
       "sdslUASAlarmNet": sdslUASAlarmNet,
       "sdslMarginAlarmCust": sdslMarginAlarmCust,
       "sdslESAlarmCust": sdslESAlarmCust,
       "sdslUASAlarmCust": sdslUASAlarmCust,
       "sdslLOSWAlarm": sdslLOSWAlarm,
       "sdslAlarmHistoryTable": sdslAlarmHistoryTable,
       "sdslAlarmHistoryEntry": sdslAlarmHistoryEntry,
       "sdslMarginAlarmFirst": sdslMarginAlarmFirst,
       "sdslMarginAlarmLast": sdslMarginAlarmLast,
       "sdslMarginAlarmCount": sdslMarginAlarmCount,
       "sdslESAlarmFirst": sdslESAlarmFirst,
       "sdslESAlarmLast": sdslESAlarmLast,
       "sdslESAlarmCount": sdslESAlarmCount,
       "sdslUASAlarmFirst": sdslUASAlarmFirst,
       "sdslUASAlarmLast": sdslUASAlarmLast,
       "sdslUASAlarmCount": sdslUASAlarmCount,
       "sdslLOSWAlarmFirst": sdslLOSWAlarmFirst,
       "sdslLOSWAlarmLast": sdslLOSWAlarmLast,
       "sdslLOSWAlarmCount": sdslLOSWAlarmCount,
       "sdslLineConfProfileIndexNext": sdslLineConfProfileIndexNext,
       "sdslLineConfProfileTable": sdslLineConfProfileTable,
       "sdslLineConfProfileEntry": sdslLineConfProfileEntry,
       "sdslLineConfProfileIndex": sdslLineConfProfileIndex,
       "sdslRateMode": sdslRateMode,
       "sdslRemFeatures": sdslRemFeatures,
       "sdslRate": sdslRate,
       "sdslLineConfProfileRowStatus": sdslLineConfProfileRowStatus,
       "sdslLineAlarmConfProfileIndexNext": sdslLineAlarmConfProfileIndexNext,
       "sdslLineAlarmConfProfileTable": sdslLineAlarmConfProfileTable,
       "sdslLineAlarmConfProfileEntry": sdslLineAlarmConfProfileEntry,
       "sdslLineAlarmConfProfileIndex": sdslLineAlarmConfProfileIndex,
       "sdslLOSWAlarmSetting": sdslLOSWAlarmSetting,
       "sdslMarginThreshold": sdslMarginThreshold,
       "sdslMarginAlarmSetting": sdslMarginAlarmSetting,
       "sdslESThreshold": sdslESThreshold,
       "sdslESAlarmSetting": sdslESAlarmSetting,
       "sdslUASThreshold": sdslUASThreshold,
       "sdslUASAlarmSetting": sdslUASAlarmSetting,
       "sdslLineAlarmConfProfileRowStatus": sdslLineAlarmConfProfileRowStatus,
       "pgSdslModGenTable": pgSdslModGenTable,
       "pgSdslModGenEntry": pgSdslModGenEntry,
       "pgSdslModGenVersionNum": pgSdslModGenVersionNum,
       "pgSdslModGenListNum": pgSdslModGenListNum,
       "pgSdslModGenVendNum": pgSdslModGenVendNum,
       "pgSdslModGenFeatures": pgSdslModGenFeatures,
       "pgSdslModGenSerialNum": pgSdslModGenSerialNum,
       "pgSdslModGenMfgDate": pgSdslModGenMfgDate,
       "pgSdslModStatTable": pgSdslModStatTable,
       "pgSdslModStatEntry": pgSdslModStatEntry,
       "pgSdslModEthOperStatus": pgSdslModEthOperStatus,
       "pgSdslModEthInOctets": pgSdslModEthInOctets,
       "pgSdslModEthInUcastPkts": pgSdslModEthInUcastPkts,
       "pgSdslModEthInNUcastPkts": pgSdslModEthInNUcastPkts,
       "pgSdslModEthInDiscards": pgSdslModEthInDiscards,
       "pgSdslModEthInErrors": pgSdslModEthInErrors,
       "pgSdslModEthOutOctets": pgSdslModEthOutOctets,
       "pgSdslModEthOutUcastPkts": pgSdslModEthOutUcastPkts,
       "pgSdslModEthOutNUcastPkts": pgSdslModEthOutNUcastPkts,
       "pgSdslModEthOutErrors": pgSdslModEthOutErrors,
       "pgSdslModDslInOctets": pgSdslModDslInOctets,
       "pgSdslModDslInUcastPkts": pgSdslModDslInUcastPkts,
       "pgSdslModDslInNUcastPkts": pgSdslModDslInNUcastPkts,
       "pgSdslModDslInDiscards": pgSdslModDslInDiscards,
       "pgSdslModDslInErrors": pgSdslModDslInErrors,
       "pgSdslModDslOutOctets": pgSdslModDslOutOctets,
       "pgSdslModDslOutUcastPkts": pgSdslModDslOutUcastPkts,
       "pgSdslModDslOutNUcastPkts": pgSdslModDslOutNUcastPkts,
       "pgSdslModDslOutErrors": pgSdslModDslOutErrors}
)
