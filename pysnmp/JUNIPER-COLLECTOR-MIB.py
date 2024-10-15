# SNMP MIB module (JUNIPER-COLLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-COLLECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:54 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxCollectorNotifications,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxCollectorNotifications",
    "jnxMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxCollectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28)
)
jnxCollectorMIB.setRevisions(
        ("2003-11-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxCollPicStateDef(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxCollGlobalStats_ObjectIdentity = ObjectIdentity
jnxCollGlobalStats = _JnxCollGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 1)
)
if mibBuilder.loadTexts:
    jnxCollGlobalStats.setStatus("current")
_JnxCollGlobalCreatedFiles_Type = Counter64
_JnxCollGlobalCreatedFiles_Object = MibScalar
jnxCollGlobalCreatedFiles = _JnxCollGlobalCreatedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 1, 1),
    _JnxCollGlobalCreatedFiles_Type()
)
jnxCollGlobalCreatedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollGlobalCreatedFiles.setStatus("current")
_JnxCollGlobalOpenFiles_Type = Counter64
_JnxCollGlobalOpenFiles_Object = MibScalar
jnxCollGlobalOpenFiles = _JnxCollGlobalOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 1, 2),
    _JnxCollGlobalOpenFiles_Type()
)
jnxCollGlobalOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollGlobalOpenFiles.setStatus("current")
_JnxCollPicIfTable_Object = MibTable
jnxCollPicIfTable = _JnxCollPicIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2)
)
if mibBuilder.loadTexts:
    jnxCollPicIfTable.setStatus("current")
_JnxCollPicIfEntry_Object = MibTableRow
jnxCollPicIfEntry = _JnxCollPicIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1)
)
jnxCollPicIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxCollPicIfEntry.setStatus("current")
_JnxCollPicIfCreatedFiles_Type = Counter64
_JnxCollPicIfCreatedFiles_Object = MibTableColumn
jnxCollPicIfCreatedFiles = _JnxCollPicIfCreatedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 1),
    _JnxCollPicIfCreatedFiles_Type()
)
jnxCollPicIfCreatedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfCreatedFiles.setStatus("current")
_JnxCollPicIfCreatedFileRate_Type = Gauge32
_JnxCollPicIfCreatedFileRate_Object = MibTableColumn
jnxCollPicIfCreatedFileRate = _JnxCollPicIfCreatedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 2),
    _JnxCollPicIfCreatedFileRate_Type()
)
jnxCollPicIfCreatedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfCreatedFileRate.setStatus("current")
_JnxCollPicIfPeakCreatedFileRate_Type = Gauge32
_JnxCollPicIfPeakCreatedFileRate_Object = MibTableColumn
jnxCollPicIfPeakCreatedFileRate = _JnxCollPicIfPeakCreatedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 3),
    _JnxCollPicIfPeakCreatedFileRate_Type()
)
jnxCollPicIfPeakCreatedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakCreatedFileRate.setStatus("current")
_JnxCollPicIfExportedFiles_Type = Counter64
_JnxCollPicIfExportedFiles_Object = MibTableColumn
jnxCollPicIfExportedFiles = _JnxCollPicIfExportedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 4),
    _JnxCollPicIfExportedFiles_Type()
)
jnxCollPicIfExportedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfExportedFiles.setStatus("current")
_JnxCollPicIfExportedFileRate_Type = Gauge32
_JnxCollPicIfExportedFileRate_Object = MibTableColumn
jnxCollPicIfExportedFileRate = _JnxCollPicIfExportedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 5),
    _JnxCollPicIfExportedFileRate_Type()
)
jnxCollPicIfExportedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfExportedFileRate.setStatus("current")
_JnxCollPicIfPeakExportedFileRate_Type = Gauge32
_JnxCollPicIfPeakExportedFileRate_Object = MibTableColumn
jnxCollPicIfPeakExportedFileRate = _JnxCollPicIfPeakExportedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 6),
    _JnxCollPicIfPeakExportedFileRate_Type()
)
jnxCollPicIfPeakExportedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakExportedFileRate.setStatus("current")
_JnxCollPicIfDestroyedFiles_Type = Counter64
_JnxCollPicIfDestroyedFiles_Object = MibTableColumn
jnxCollPicIfDestroyedFiles = _JnxCollPicIfDestroyedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 7),
    _JnxCollPicIfDestroyedFiles_Type()
)
jnxCollPicIfDestroyedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfDestroyedFiles.setStatus("current")
_JnxCollPicIfDestroyedFileRate_Type = Gauge32
_JnxCollPicIfDestroyedFileRate_Object = MibTableColumn
jnxCollPicIfDestroyedFileRate = _JnxCollPicIfDestroyedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 8),
    _JnxCollPicIfDestroyedFileRate_Type()
)
jnxCollPicIfDestroyedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfDestroyedFileRate.setStatus("current")
_JnxCollPicIfPeakDestroyedFileRate_Type = Gauge32
_JnxCollPicIfPeakDestroyedFileRate_Object = MibTableColumn
jnxCollPicIfPeakDestroyedFileRate = _JnxCollPicIfPeakDestroyedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 9),
    _JnxCollPicIfPeakDestroyedFileRate_Type()
)
jnxCollPicIfPeakDestroyedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakDestroyedFileRate.setStatus("current")
_JnxCollPicIfProcRecords_Type = Counter64
_JnxCollPicIfProcRecords_Object = MibTableColumn
jnxCollPicIfProcRecords = _JnxCollPicIfProcRecords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 10),
    _JnxCollPicIfProcRecords_Type()
)
jnxCollPicIfProcRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfProcRecords.setStatus("current")
_JnxCollPicIfProcRecordsRate_Type = Gauge32
_JnxCollPicIfProcRecordsRate_Object = MibTableColumn
jnxCollPicIfProcRecordsRate = _JnxCollPicIfProcRecordsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 11),
    _JnxCollPicIfProcRecordsRate_Type()
)
jnxCollPicIfProcRecordsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfProcRecordsRate.setStatus("current")
_JnxCollPicIfPeakProcRecordsRate_Type = Gauge32
_JnxCollPicIfPeakProcRecordsRate_Object = MibTableColumn
jnxCollPicIfPeakProcRecordsRate = _JnxCollPicIfPeakProcRecordsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 12),
    _JnxCollPicIfPeakProcRecordsRate_Type()
)
jnxCollPicIfPeakProcRecordsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakProcRecordsRate.setStatus("current")
_JnxCollPicIfMemoryUsed_Type = CounterBasedGauge64
_JnxCollPicIfMemoryUsed_Object = MibTableColumn
jnxCollPicIfMemoryUsed = _JnxCollPicIfMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 13),
    _JnxCollPicIfMemoryUsed_Type()
)
jnxCollPicIfMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfMemoryUsed.setStatus("current")
_JnxCollPicIfMemoryFree_Type = CounterBasedGauge64
_JnxCollPicIfMemoryFree_Object = MibTableColumn
jnxCollPicIfMemoryFree = _JnxCollPicIfMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 14),
    _JnxCollPicIfMemoryFree_Type()
)
jnxCollPicIfMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfMemoryFree.setStatus("current")
_JnxCollPicIfFtpBytes_Type = Counter64
_JnxCollPicIfFtpBytes_Object = MibTableColumn
jnxCollPicIfFtpBytes = _JnxCollPicIfFtpBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 15),
    _JnxCollPicIfFtpBytes_Type()
)
jnxCollPicIfFtpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfFtpBytes.setStatus("current")
_JnxCollPicIfFtpByteRate_Type = Gauge32
_JnxCollPicIfFtpByteRate_Object = MibTableColumn
jnxCollPicIfFtpByteRate = _JnxCollPicIfFtpByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 16),
    _JnxCollPicIfFtpByteRate_Type()
)
jnxCollPicIfFtpByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfFtpByteRate.setStatus("current")
_JnxCollPicIfPeakFtpByteRate_Type = Gauge32
_JnxCollPicIfPeakFtpByteRate_Object = MibTableColumn
jnxCollPicIfPeakFtpByteRate = _JnxCollPicIfPeakFtpByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 17),
    _JnxCollPicIfPeakFtpByteRate_Type()
)
jnxCollPicIfPeakFtpByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakFtpByteRate.setStatus("current")
_JnxCollPicIfFtpFiles_Type = Counter64
_JnxCollPicIfFtpFiles_Object = MibTableColumn
jnxCollPicIfFtpFiles = _JnxCollPicIfFtpFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 18),
    _JnxCollPicIfFtpFiles_Type()
)
jnxCollPicIfFtpFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfFtpFiles.setStatus("current")
_JnxCollPicIfFtpFileRate_Type = Gauge32
_JnxCollPicIfFtpFileRate_Object = MibTableColumn
jnxCollPicIfFtpFileRate = _JnxCollPicIfFtpFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 19),
    _JnxCollPicIfFtpFileRate_Type()
)
jnxCollPicIfFtpFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfFtpFileRate.setStatus("current")
_JnxCollPicIfPeakFtpFileRate_Type = Gauge32
_JnxCollPicIfPeakFtpFileRate_Object = MibTableColumn
jnxCollPicIfPeakFtpFileRate = _JnxCollPicIfPeakFtpFileRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 20),
    _JnxCollPicIfPeakFtpFileRate_Type()
)
jnxCollPicIfPeakFtpFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfPeakFtpFileRate.setStatus("current")
_JnxCollPicIfFtpFailures_Type = CounterBasedGauge64
_JnxCollPicIfFtpFailures_Object = MibTableColumn
jnxCollPicIfFtpFailures = _JnxCollPicIfFtpFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 21),
    _JnxCollPicIfFtpFailures_Type()
)
jnxCollPicIfFtpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfFtpFailures.setStatus("current")
_JnxCollPicIfCurrentState_Type = JnxCollPicStateDef
_JnxCollPicIfCurrentState_Object = MibTableColumn
jnxCollPicIfCurrentState = _JnxCollPicIfCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 22),
    _JnxCollPicIfCurrentState_Type()
)
jnxCollPicIfCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfCurrentState.setStatus("current")
_JnxCollPicIfLastStateChange_Type = JnxCollPicStateDef
_JnxCollPicIfLastStateChange_Object = MibTableColumn
jnxCollPicIfLastStateChange = _JnxCollPicIfLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 23),
    _JnxCollPicIfLastStateChange_Type()
)
jnxCollPicIfLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfLastStateChange.setStatus("current")
_JnxCollPicIfStateChangeTime_Type = TimeTicks
_JnxCollPicIfStateChangeTime_Object = MibTableColumn
jnxCollPicIfStateChangeTime = _JnxCollPicIfStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 24),
    _JnxCollPicIfStateChangeTime_Type()
)
jnxCollPicIfStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfStateChangeTime.setStatus("current")
_JnxCollPicIfStateChangeDate_Type = DateAndTime
_JnxCollPicIfStateChangeDate_Object = MibTableColumn
jnxCollPicIfStateChangeDate = _JnxCollPicIfStateChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 25),
    _JnxCollPicIfStateChangeDate_Type()
)
jnxCollPicIfStateChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfStateChangeDate.setStatus("current")


class _JnxCollPicIfStateChangeType_Type(Integer32):
    """Custom type jnxCollPicIfStateChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 3),
          ("none", 1),
          ("set", 2))
    )


_JnxCollPicIfStateChangeType_Type.__name__ = "Integer32"
_JnxCollPicIfStateChangeType_Object = MibTableColumn
jnxCollPicIfStateChangeType = _JnxCollPicIfStateChangeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 26),
    _JnxCollPicIfStateChangeType_Type()
)
jnxCollPicIfStateChangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollPicIfStateChangeType.setStatus("current")
_JnxCollFileTable_Object = MibTable
jnxCollFileTable = _JnxCollFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3)
)
if mibBuilder.loadTexts:
    jnxCollFileTable.setStatus("current")
_JnxCollFileEntry_Object = MibTableRow
jnxCollFileEntry = _JnxCollFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1)
)
jnxCollFileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-COLLECTOR-MIB", "jnxCollFileName"),
)
if mibBuilder.loadTexts:
    jnxCollFileEntry.setStatus("current")


class _JnxCollFileName_Type(DisplayString):
    """Custom type jnxCollFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 115),
    )


_JnxCollFileName_Type.__name__ = "DisplayString"
_JnxCollFileName_Object = MibTableColumn
jnxCollFileName = _JnxCollFileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 1),
    _JnxCollFileName_Type()
)
jnxCollFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCollFileName.setStatus("current")
_JnxCollFileFname_Type = DisplayString
_JnxCollFileFname_Object = MibTableColumn
jnxCollFileFname = _JnxCollFileFname_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 2),
    _JnxCollFileFname_Type()
)
jnxCollFileFname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileFname.setStatus("current")
_JnxCollFileRecords_Type = CounterBasedGauge64
_JnxCollFileRecords_Object = MibTableColumn
jnxCollFileRecords = _JnxCollFileRecords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 3),
    _JnxCollFileRecords_Type()
)
jnxCollFileRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileRecords.setStatus("current")
_JnxCollFileRecordRate_Type = Gauge32
_JnxCollFileRecordRate_Object = MibTableColumn
jnxCollFileRecordRate = _JnxCollFileRecordRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 4),
    _JnxCollFileRecordRate_Type()
)
jnxCollFileRecordRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileRecordRate.setStatus("current")
_JnxCollFilePeakRecordRate_Type = Gauge32
_JnxCollFilePeakRecordRate_Object = MibTableColumn
jnxCollFilePeakRecordRate = _JnxCollFilePeakRecordRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 5),
    _JnxCollFilePeakRecordRate_Type()
)
jnxCollFilePeakRecordRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFilePeakRecordRate.setStatus("current")
_JnxCollFileUncompBytes_Type = CounterBasedGauge64
_JnxCollFileUncompBytes_Object = MibTableColumn
jnxCollFileUncompBytes = _JnxCollFileUncompBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 6),
    _JnxCollFileUncompBytes_Type()
)
jnxCollFileUncompBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileUncompBytes.setStatus("current")
_JnxCollFileUncompByteRate_Type = Gauge32
_JnxCollFileUncompByteRate_Object = MibTableColumn
jnxCollFileUncompByteRate = _JnxCollFileUncompByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 7),
    _JnxCollFileUncompByteRate_Type()
)
jnxCollFileUncompByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileUncompByteRate.setStatus("current")
_JnxCollFilePeakUncompByteRate_Type = Gauge32
_JnxCollFilePeakUncompByteRate_Object = MibTableColumn
jnxCollFilePeakUncompByteRate = _JnxCollFilePeakUncompByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 8),
    _JnxCollFilePeakUncompByteRate_Type()
)
jnxCollFilePeakUncompByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFilePeakUncompByteRate.setStatus("current")
_JnxCollFileCompBytes_Type = CounterBasedGauge64
_JnxCollFileCompBytes_Object = MibTableColumn
jnxCollFileCompBytes = _JnxCollFileCompBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 9),
    _JnxCollFileCompBytes_Type()
)
jnxCollFileCompBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileCompBytes.setStatus("current")
_JnxCollFileCompByteRate_Type = Gauge32
_JnxCollFileCompByteRate_Object = MibTableColumn
jnxCollFileCompByteRate = _JnxCollFileCompByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 10),
    _JnxCollFileCompByteRate_Type()
)
jnxCollFileCompByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileCompByteRate.setStatus("current")
_JnxCollFilePeakCompByteRate_Type = Gauge32
_JnxCollFilePeakCompByteRate_Object = MibTableColumn
jnxCollFilePeakCompByteRate = _JnxCollFilePeakCompByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 11),
    _JnxCollFilePeakCompByteRate_Type()
)
jnxCollFilePeakCompByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFilePeakCompByteRate.setStatus("current")
_JnxCollFileBlocks_Type = Gauge32
_JnxCollFileBlocks_Object = MibTableColumn
jnxCollFileBlocks = _JnxCollFileBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 12),
    _JnxCollFileBlocks_Type()
)
jnxCollFileBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileBlocks.setStatus("current")
_JnxCollFileCompBlocks_Type = Gauge32
_JnxCollFileCompBlocks_Object = MibTableColumn
jnxCollFileCompBlocks = _JnxCollFileCompBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 14),
    _JnxCollFileCompBlocks_Type()
)
jnxCollFileCompBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileCompBlocks.setStatus("current")
_JnxCollFileTransferAttempts_Type = Gauge32
_JnxCollFileTransferAttempts_Object = MibTableColumn
jnxCollFileTransferAttempts = _JnxCollFileTransferAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 15),
    _JnxCollFileTransferAttempts_Type()
)
jnxCollFileTransferAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileTransferAttempts.setStatus("current")


class _JnxCollFileState_Type(Integer32):
    """Custom type jnxCollFileState based on Integer32"""
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
        *(("active", 2),
          ("export1", 4),
          ("export2", 5),
          ("unknown", 1),
          ("wait", 3))
    )


_JnxCollFileState_Type.__name__ = "Integer32"
_JnxCollFileState_Object = MibTableColumn
jnxCollFileState = _JnxCollFileState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 16),
    _JnxCollFileState_Type()
)
jnxCollFileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCollFileState.setStatus("current")
_JnxCollNotifyVars_ObjectIdentity = ObjectIdentity
jnxCollNotifyVars = _JnxCollNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4)
)
if mibBuilder.loadTexts:
    jnxCollNotifyVars.setStatus("current")
_JnxCollNotifyUrl_Type = DisplayString
_JnxCollNotifyUrl_Object = MibScalar
jnxCollNotifyUrl = _JnxCollNotifyUrl_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 1),
    _JnxCollNotifyUrl_Type()
)
jnxCollNotifyUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyUrl.setStatus("current")
_JnxCollNotifyInetType_Type = InetAddressType
_JnxCollNotifyInetType_Object = MibScalar
jnxCollNotifyInetType = _JnxCollNotifyInetType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 2),
    _JnxCollNotifyInetType_Type()
)
jnxCollNotifyInetType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyInetType.setStatus("current")
_JnxCollNotifyInetAddress_Type = InetAddress
_JnxCollNotifyInetAddress_Object = MibScalar
jnxCollNotifyInetAddress = _JnxCollNotifyInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 3),
    _JnxCollNotifyInetAddress_Type()
)
jnxCollNotifyInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyInetAddress.setStatus("current")
_JnxCollNotifyError_Type = DisplayString
_JnxCollNotifyError_Object = MibScalar
jnxCollNotifyError = _JnxCollNotifyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 4),
    _JnxCollNotifyError_Type()
)
jnxCollNotifyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyError.setStatus("current")
_JnxCollNotifyFile_Type = DisplayString
_JnxCollNotifyFile_Object = MibScalar
jnxCollNotifyFile = _JnxCollNotifyFile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 5),
    _JnxCollNotifyFile_Type()
)
jnxCollNotifyFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFile.setStatus("current")
_JnxCollNotifyFtpResultCode_Type = Integer32
_JnxCollNotifyFtpResultCode_Object = MibScalar
jnxCollNotifyFtpResultCode = _JnxCollNotifyFtpResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 6),
    _JnxCollNotifyFtpResultCode_Type()
)
jnxCollNotifyFtpResultCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFtpResultCode.setStatus("current")
_JnxCollNotifyFtpErrorText_Type = DisplayString
_JnxCollNotifyFtpErrorText_Object = MibScalar
jnxCollNotifyFtpErrorText = _JnxCollNotifyFtpErrorText_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 7),
    _JnxCollNotifyFtpErrorText_Type()
)
jnxCollNotifyFtpErrorText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFtpErrorText.setStatus("current")
_JnxCollNotifyMemUtil_Type = Gauge32
_JnxCollNotifyMemUtil_Object = MibScalar
jnxCollNotifyMemUtil = _JnxCollNotifyMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 8),
    _JnxCollNotifyMemUtil_Type()
)
jnxCollNotifyMemUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyMemUtil.setStatus("current")
_JnxCollNotifyMemFree_Type = Gauge32
_JnxCollNotifyMemFree_Object = MibScalar
jnxCollNotifyMemFree = _JnxCollNotifyMemFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 9),
    _JnxCollNotifyMemFree_Type()
)
jnxCollNotifyMemFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyMemFree.setStatus("current")
_JnxCollNotifyMemThresh_Type = Gauge32
_JnxCollNotifyMemThresh_Object = MibScalar
jnxCollNotifyMemThresh = _JnxCollNotifyMemThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 10),
    _JnxCollNotifyMemThresh_Type()
)
jnxCollNotifyMemThresh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyMemThresh.setStatus("current")
_JnxCollNotifyNewRecordRate_Type = Gauge32
_JnxCollNotifyNewRecordRate_Object = MibScalar
jnxCollNotifyNewRecordRate = _JnxCollNotifyNewRecordRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 11),
    _JnxCollNotifyNewRecordRate_Type()
)
jnxCollNotifyNewRecordRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyNewRecordRate.setStatus("current")


class _JnxCollNotifyOverloadType_Type(Integer32):
    """Custom type jnxCollNotifyOverloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardOverload", 2),
          ("softOverload", 1))
    )


_JnxCollNotifyOverloadType_Type.__name__ = "Integer32"
_JnxCollNotifyOverloadType_Object = MibScalar
jnxCollNotifyOverloadType = _JnxCollNotifyOverloadType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 12),
    _JnxCollNotifyOverloadType_Type()
)
jnxCollNotifyOverloadType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyOverloadType.setStatus("current")
_JnxCollNotifyDate_Type = DateAndTime
_JnxCollNotifyDate_Object = MibScalar
jnxCollNotifyDate = _JnxCollNotifyDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 13),
    _JnxCollNotifyDate_Type()
)
jnxCollNotifyDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyDate.setStatus("current")
_JnxCollNotifyFromFtpServerInetType_Type = InetAddressType
_JnxCollNotifyFromFtpServerInetType_Object = MibScalar
jnxCollNotifyFromFtpServerInetType = _JnxCollNotifyFromFtpServerInetType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 14),
    _JnxCollNotifyFromFtpServerInetType_Type()
)
jnxCollNotifyFromFtpServerInetType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFromFtpServerInetType.setStatus("current")
_JnxCollNotifyFromFtpServerInetAddress_Type = InetAddress
_JnxCollNotifyFromFtpServerInetAddress_Object = MibScalar
jnxCollNotifyFromFtpServerInetAddress = _JnxCollNotifyFromFtpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 15),
    _JnxCollNotifyFromFtpServerInetAddress_Type()
)
jnxCollNotifyFromFtpServerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFromFtpServerInetAddress.setStatus("current")


class _JnxCollNotifyFromFtpServerType_Type(Integer32):
    """Custom type jnxCollNotifyFromFtpServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_JnxCollNotifyFromFtpServerType_Type.__name__ = "Integer32"
_JnxCollNotifyFromFtpServerType_Object = MibScalar
jnxCollNotifyFromFtpServerType = _JnxCollNotifyFromFtpServerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 16),
    _JnxCollNotifyFromFtpServerType_Type()
)
jnxCollNotifyFromFtpServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyFromFtpServerType.setStatus("current")
_JnxCollNotifyToFtpServerInetType_Type = InetAddressType
_JnxCollNotifyToFtpServerInetType_Object = MibScalar
jnxCollNotifyToFtpServerInetType = _JnxCollNotifyToFtpServerInetType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 17),
    _JnxCollNotifyToFtpServerInetType_Type()
)
jnxCollNotifyToFtpServerInetType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyToFtpServerInetType.setStatus("current")
_JnxCollNotifyToFtpServerInetAddress_Type = InetAddress
_JnxCollNotifyToFtpServerInetAddress_Object = MibScalar
jnxCollNotifyToFtpServerInetAddress = _JnxCollNotifyToFtpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 18),
    _JnxCollNotifyToFtpServerInetAddress_Type()
)
jnxCollNotifyToFtpServerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyToFtpServerInetAddress.setStatus("current")


class _JnxCollNotifyToFtpServerType_Type(Integer32):
    """Custom type jnxCollNotifyToFtpServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_JnxCollNotifyToFtpServerType_Type.__name__ = "Integer32"
_JnxCollNotifyToFtpServerType_Object = MibScalar
jnxCollNotifyToFtpServerType = _JnxCollNotifyToFtpServerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 19),
    _JnxCollNotifyToFtpServerType_Type()
)
jnxCollNotifyToFtpServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyToFtpServerType.setStatus("current")


class _JnxCollNotifyInitiatedBy_Type(Integer32):
    """Custom type jnxCollNotifyInitiatedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("cli", 1))
    )


_JnxCollNotifyInitiatedBy_Type.__name__ = "Integer32"
_JnxCollNotifyInitiatedBy_Object = MibScalar
jnxCollNotifyInitiatedBy = _JnxCollNotifyInitiatedBy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 20),
    _JnxCollNotifyInitiatedBy_Type()
)
jnxCollNotifyInitiatedBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCollNotifyInitiatedBy.setStatus("current")
_JnxCollNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxCollNotificationPrefix = _JnxCollNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0)
)
if mibBuilder.loadTexts:
    jnxCollNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxCollUnavailableDest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 1)
)
jnxCollUnavailableDest.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"))
)
if mibBuilder.loadTexts:
    jnxCollUnavailableDest.setStatus(
        "current"
    )

jnxCollUnavailableDestCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 2)
)
jnxCollUnavailableDestCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"))
)
if mibBuilder.loadTexts:
    jnxCollUnavailableDestCleared.setStatus(
        "current"
    )

jnxCollUnsuccessfulTransfer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 3)
)
jnxCollUnsuccessfulTransfer.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFile"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyError"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFtpResultCode"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFtpErrorText"))
)
if mibBuilder.loadTexts:
    jnxCollUnsuccessfulTransfer.setStatus(
        "current"
    )

jnxCollFlowOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 4)
)
jnxCollFlowOverload.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyOverloadType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyNewRecordRate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfCreatedFiles"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfDestroyedFiles"))
)
if mibBuilder.loadTexts:
    jnxCollFlowOverload.setStatus(
        "current"
    )

jnxCollFlowOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 5)
)
jnxCollFlowOverloadCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyOverloadType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyNewRecordRate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfCreatedFiles"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfDestroyedFiles"))
)
if mibBuilder.loadTexts:
    jnxCollFlowOverloadCleared.setStatus(
        "current"
    )

jnxCollMemoryUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 6)
)
jnxCollMemoryUnavailable.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemThresh"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemUtil"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemFree"))
)
if mibBuilder.loadTexts:
    jnxCollMemoryUnavailable.setStatus(
        "current"
    )

jnxCollMemoryAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 7)
)
jnxCollMemoryAvailable.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemThresh"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemUtil"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemFree"))
)
if mibBuilder.loadTexts:
    jnxCollMemoryAvailable.setStatus(
        "current"
    )

jnxCollFtpSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 8)
)
jnxCollFtpSwitchover.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerInetType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerInetAddress"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerInetType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerInetAddress"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerType"),
        ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInitiatedBy"))
)
if mibBuilder.loadTexts:
    jnxCollFtpSwitchover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-COLLECTOR-MIB",
    **{"JnxCollPicStateDef": JnxCollPicStateDef,
       "jnxCollectorMIB": jnxCollectorMIB,
       "jnxCollGlobalStats": jnxCollGlobalStats,
       "jnxCollGlobalCreatedFiles": jnxCollGlobalCreatedFiles,
       "jnxCollGlobalOpenFiles": jnxCollGlobalOpenFiles,
       "jnxCollPicIfTable": jnxCollPicIfTable,
       "jnxCollPicIfEntry": jnxCollPicIfEntry,
       "jnxCollPicIfCreatedFiles": jnxCollPicIfCreatedFiles,
       "jnxCollPicIfCreatedFileRate": jnxCollPicIfCreatedFileRate,
       "jnxCollPicIfPeakCreatedFileRate": jnxCollPicIfPeakCreatedFileRate,
       "jnxCollPicIfExportedFiles": jnxCollPicIfExportedFiles,
       "jnxCollPicIfExportedFileRate": jnxCollPicIfExportedFileRate,
       "jnxCollPicIfPeakExportedFileRate": jnxCollPicIfPeakExportedFileRate,
       "jnxCollPicIfDestroyedFiles": jnxCollPicIfDestroyedFiles,
       "jnxCollPicIfDestroyedFileRate": jnxCollPicIfDestroyedFileRate,
       "jnxCollPicIfPeakDestroyedFileRate": jnxCollPicIfPeakDestroyedFileRate,
       "jnxCollPicIfProcRecords": jnxCollPicIfProcRecords,
       "jnxCollPicIfProcRecordsRate": jnxCollPicIfProcRecordsRate,
       "jnxCollPicIfPeakProcRecordsRate": jnxCollPicIfPeakProcRecordsRate,
       "jnxCollPicIfMemoryUsed": jnxCollPicIfMemoryUsed,
       "jnxCollPicIfMemoryFree": jnxCollPicIfMemoryFree,
       "jnxCollPicIfFtpBytes": jnxCollPicIfFtpBytes,
       "jnxCollPicIfFtpByteRate": jnxCollPicIfFtpByteRate,
       "jnxCollPicIfPeakFtpByteRate": jnxCollPicIfPeakFtpByteRate,
       "jnxCollPicIfFtpFiles": jnxCollPicIfFtpFiles,
       "jnxCollPicIfFtpFileRate": jnxCollPicIfFtpFileRate,
       "jnxCollPicIfPeakFtpFileRate": jnxCollPicIfPeakFtpFileRate,
       "jnxCollPicIfFtpFailures": jnxCollPicIfFtpFailures,
       "jnxCollPicIfCurrentState": jnxCollPicIfCurrentState,
       "jnxCollPicIfLastStateChange": jnxCollPicIfLastStateChange,
       "jnxCollPicIfStateChangeTime": jnxCollPicIfStateChangeTime,
       "jnxCollPicIfStateChangeDate": jnxCollPicIfStateChangeDate,
       "jnxCollPicIfStateChangeType": jnxCollPicIfStateChangeType,
       "jnxCollFileTable": jnxCollFileTable,
       "jnxCollFileEntry": jnxCollFileEntry,
       "jnxCollFileName": jnxCollFileName,
       "jnxCollFileFname": jnxCollFileFname,
       "jnxCollFileRecords": jnxCollFileRecords,
       "jnxCollFileRecordRate": jnxCollFileRecordRate,
       "jnxCollFilePeakRecordRate": jnxCollFilePeakRecordRate,
       "jnxCollFileUncompBytes": jnxCollFileUncompBytes,
       "jnxCollFileUncompByteRate": jnxCollFileUncompByteRate,
       "jnxCollFilePeakUncompByteRate": jnxCollFilePeakUncompByteRate,
       "jnxCollFileCompBytes": jnxCollFileCompBytes,
       "jnxCollFileCompByteRate": jnxCollFileCompByteRate,
       "jnxCollFilePeakCompByteRate": jnxCollFilePeakCompByteRate,
       "jnxCollFileBlocks": jnxCollFileBlocks,
       "jnxCollFileCompBlocks": jnxCollFileCompBlocks,
       "jnxCollFileTransferAttempts": jnxCollFileTransferAttempts,
       "jnxCollFileState": jnxCollFileState,
       "jnxCollNotifyVars": jnxCollNotifyVars,
       "jnxCollNotifyUrl": jnxCollNotifyUrl,
       "jnxCollNotifyInetType": jnxCollNotifyInetType,
       "jnxCollNotifyInetAddress": jnxCollNotifyInetAddress,
       "jnxCollNotifyError": jnxCollNotifyError,
       "jnxCollNotifyFile": jnxCollNotifyFile,
       "jnxCollNotifyFtpResultCode": jnxCollNotifyFtpResultCode,
       "jnxCollNotifyFtpErrorText": jnxCollNotifyFtpErrorText,
       "jnxCollNotifyMemUtil": jnxCollNotifyMemUtil,
       "jnxCollNotifyMemFree": jnxCollNotifyMemFree,
       "jnxCollNotifyMemThresh": jnxCollNotifyMemThresh,
       "jnxCollNotifyNewRecordRate": jnxCollNotifyNewRecordRate,
       "jnxCollNotifyOverloadType": jnxCollNotifyOverloadType,
       "jnxCollNotifyDate": jnxCollNotifyDate,
       "jnxCollNotifyFromFtpServerInetType": jnxCollNotifyFromFtpServerInetType,
       "jnxCollNotifyFromFtpServerInetAddress": jnxCollNotifyFromFtpServerInetAddress,
       "jnxCollNotifyFromFtpServerType": jnxCollNotifyFromFtpServerType,
       "jnxCollNotifyToFtpServerInetType": jnxCollNotifyToFtpServerInetType,
       "jnxCollNotifyToFtpServerInetAddress": jnxCollNotifyToFtpServerInetAddress,
       "jnxCollNotifyToFtpServerType": jnxCollNotifyToFtpServerType,
       "jnxCollNotifyInitiatedBy": jnxCollNotifyInitiatedBy,
       "jnxCollNotificationPrefix": jnxCollNotificationPrefix,
       "jnxCollUnavailableDest": jnxCollUnavailableDest,
       "jnxCollUnavailableDestCleared": jnxCollUnavailableDestCleared,
       "jnxCollUnsuccessfulTransfer": jnxCollUnsuccessfulTransfer,
       "jnxCollFlowOverload": jnxCollFlowOverload,
       "jnxCollFlowOverloadCleared": jnxCollFlowOverloadCleared,
       "jnxCollMemoryUnavailable": jnxCollMemoryUnavailable,
       "jnxCollMemoryAvailable": jnxCollMemoryAvailable,
       "jnxCollFtpSwitchover": jnxCollFtpSwitchover}
)
