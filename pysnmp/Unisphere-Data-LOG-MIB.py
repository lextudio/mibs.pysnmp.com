# SNMP MIB module (Unisphere-Data-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:06 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdLogSeverity,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdLogSeverity")


# MODULE-IDENTITY

usdLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28)
)
usdLogMIB.setRevisions(
        ("2001-03-16 19:02",
         "2000-03-27 05:00",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdLogCatName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class UsdLogVerbosity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 0),
          ("medium", 1))
    )



class UsdLogSyslogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )



# MIB Managed Objects in the order of their OIDs

_UsdLogTrapPrefix_ObjectIdentity = ObjectIdentity
usdLogTrapPrefix = _UsdLogTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0)
)
_UsdLogObjects_ObjectIdentity = ObjectIdentity
usdLogObjects = _UsdLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1)
)
_UsdLogDestinations_ObjectIdentity = ObjectIdentity
usdLogDestinations = _UsdLogDestinations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1)
)
_UsdLogDestSyslog_ObjectIdentity = ObjectIdentity
usdLogDestSyslog = _UsdLogDestSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1)
)
_UsdLogDestSyslogSeverity_Type = UsdLogSeverity
_UsdLogDestSyslogSeverity_Object = MibScalar
usdLogDestSyslogSeverity = _UsdLogDestSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 1),
    _UsdLogDestSyslogSeverity_Type()
)
usdLogDestSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogDestSyslogSeverity.setStatus("obsolete")
_UsdLogDestSyslogAddress_Type = IpAddress
_UsdLogDestSyslogAddress_Object = MibScalar
usdLogDestSyslogAddress = _UsdLogDestSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 2),
    _UsdLogDestSyslogAddress_Type()
)
usdLogDestSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogDestSyslogAddress.setStatus("obsolete")
_UsdLogSyslogTable_Object = MibTable
usdLogSyslogTable = _UsdLogSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdLogSyslogTable.setStatus("current")
_UsdLogSyslogEntry_Object = MibTableRow
usdLogSyslogEntry = _UsdLogSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1)
)
usdLogSyslogEntry.setIndexNames(
    (0, "Unisphere-Data-LOG-MIB", "usdLogSyslogIpAddress"),
)
if mibBuilder.loadTexts:
    usdLogSyslogEntry.setStatus("current")
_UsdLogSyslogIpAddress_Type = IpAddress
_UsdLogSyslogIpAddress_Object = MibTableColumn
usdLogSyslogIpAddress = _UsdLogSyslogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 1),
    _UsdLogSyslogIpAddress_Type()
)
usdLogSyslogIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdLogSyslogIpAddress.setStatus("current")
_UsdLogSyslogRowStatus_Type = RowStatus
_UsdLogSyslogRowStatus_Object = MibTableColumn
usdLogSyslogRowStatus = _UsdLogSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 2),
    _UsdLogSyslogRowStatus_Type()
)
usdLogSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdLogSyslogRowStatus.setStatus("current")


class _UsdLogSyslogSeverity_Type(UsdLogSeverity):
    """Custom type usdLogSyslogSeverity based on UsdLogSeverity"""


_UsdLogSyslogSeverity_Object = MibTableColumn
usdLogSyslogSeverity = _UsdLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 3),
    _UsdLogSyslogSeverity_Type()
)
usdLogSyslogSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdLogSyslogSeverity.setStatus("current")


class _UsdLogSyslogFacility_Type(UsdLogSyslogFacility):
    """Custom type usdLogSyslogFacility based on UsdLogSyslogFacility"""


_UsdLogSyslogFacility_Object = MibTableColumn
usdLogSyslogFacility = _UsdLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 4),
    _UsdLogSyslogFacility_Type()
)
usdLogSyslogFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdLogSyslogFacility.setStatus("current")
_UsdLogDestConsole_ObjectIdentity = ObjectIdentity
usdLogDestConsole = _UsdLogDestConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2)
)
_UsdLogDestConsoleSeverity_Type = UsdLogSeverity
_UsdLogDestConsoleSeverity_Object = MibScalar
usdLogDestConsoleSeverity = _UsdLogDestConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2, 1),
    _UsdLogDestConsoleSeverity_Type()
)
usdLogDestConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogDestConsoleSeverity.setStatus("current")
_UsdLogDestNvFile_ObjectIdentity = ObjectIdentity
usdLogDestNvFile = _UsdLogDestNvFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3)
)
_UsdLogDestNvFileSeverity_Type = UsdLogSeverity
_UsdLogDestNvFileSeverity_Object = MibScalar
usdLogDestNvFileSeverity = _UsdLogDestNvFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3, 1),
    _UsdLogDestNvFileSeverity_Type()
)
usdLogDestNvFileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogDestNvFileSeverity.setStatus("current")
_UsdLogCategories_ObjectIdentity = ObjectIdentity
usdLogCategories = _UsdLogCategories_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2)
)
_UsdLogCatScalars_ObjectIdentity = ObjectIdentity
usdLogCatScalars = _UsdLogCatScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 1)
)
_UsdLogCatTable_Object = MibTable
usdLogCatTable = _UsdLogCatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdLogCatTable.setStatus("current")
_UsdLogCatEntry_Object = MibTableRow
usdLogCatEntry = _UsdLogCatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1)
)
usdLogCatEntry.setIndexNames(
    (0, "Unisphere-Data-LOG-MIB", "usdLogCatIndex"),
)
if mibBuilder.loadTexts:
    usdLogCatEntry.setStatus("current")


class _UsdLogCatIndex_Type(Integer32):
    """Custom type usdLogCatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdLogCatIndex_Type.__name__ = "Integer32"
_UsdLogCatIndex_Object = MibTableColumn
usdLogCatIndex = _UsdLogCatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 1),
    _UsdLogCatIndex_Type()
)
usdLogCatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdLogCatIndex.setStatus("current")
_UsdLogCatName_Type = UsdLogCatName
_UsdLogCatName_Object = MibTableColumn
usdLogCatName = _UsdLogCatName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 2),
    _UsdLogCatName_Type()
)
usdLogCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatName.setStatus("current")
_UsdLogCatDescr_Type = DisplayString
_UsdLogCatDescr_Object = MibTableColumn
usdLogCatDescr = _UsdLogCatDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 3),
    _UsdLogCatDescr_Type()
)
usdLogCatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatDescr.setStatus("current")
_UsdLogCatEngineering_Type = TruthValue
_UsdLogCatEngineering_Object = MibTableColumn
usdLogCatEngineering = _UsdLogCatEngineering_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 4),
    _UsdLogCatEngineering_Type()
)
usdLogCatEngineering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatEngineering.setStatus("current")
_UsdLogCatDiscards_Type = Counter32
_UsdLogCatDiscards_Object = MibTableColumn
usdLogCatDiscards = _UsdLogCatDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 5),
    _UsdLogCatDiscards_Type()
)
usdLogCatDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatDiscards.setStatus("current")
_UsdLogCatSeverity_Type = UsdLogSeverity
_UsdLogCatSeverity_Object = MibTableColumn
usdLogCatSeverity = _UsdLogCatSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 6),
    _UsdLogCatSeverity_Type()
)
usdLogCatSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogCatSeverity.setStatus("current")
_UsdLogCatVerbosity_Type = UsdLogVerbosity
_UsdLogCatVerbosity_Object = MibTableColumn
usdLogCatVerbosity = _UsdLogCatVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 7),
    _UsdLogCatVerbosity_Type()
)
usdLogCatVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogCatVerbosity.setStatus("current")
_UsdLogCatNameTable_Object = MibTable
usdLogCatNameTable = _UsdLogCatNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3)
)
if mibBuilder.loadTexts:
    usdLogCatNameTable.setStatus("current")
_UsdLogCatNameEntry_Object = MibTableRow
usdLogCatNameEntry = _UsdLogCatNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1)
)
usdLogCatNameEntry.setIndexNames(
    (1, "Unisphere-Data-LOG-MIB", "usdLogCatNameName"),
)
if mibBuilder.loadTexts:
    usdLogCatNameEntry.setStatus("current")
_UsdLogCatNameName_Type = UsdLogCatName
_UsdLogCatNameName_Object = MibTableColumn
usdLogCatNameName = _UsdLogCatNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 1),
    _UsdLogCatNameName_Type()
)
usdLogCatNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatNameName.setStatus("current")


class _UsdLogCatNameIndex_Type(Integer32):
    """Custom type usdLogCatNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdLogCatNameIndex_Type.__name__ = "Integer32"
_UsdLogCatNameIndex_Object = MibTableColumn
usdLogCatNameIndex = _UsdLogCatNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 2),
    _UsdLogCatNameIndex_Type()
)
usdLogCatNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogCatNameIndex.setStatus("current")
_UsdLogMessages_ObjectIdentity = ObjectIdentity
usdLogMessages = _UsdLogMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3)
)
_UsdLogMsgScalars_ObjectIdentity = ObjectIdentity
usdLogMsgScalars = _UsdLogMsgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1)
)
_UsdLogMsgCapacity_Type = Integer32
_UsdLogMsgCapacity_Object = MibScalar
usdLogMsgCapacity = _UsdLogMsgCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 1),
    _UsdLogMsgCapacity_Type()
)
usdLogMsgCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgCapacity.setStatus("current")
if mibBuilder.loadTexts:
    usdLogMsgCapacity.setUnits("messages")
_UsdLogMsgLastSeqNumber_Type = Counter32
_UsdLogMsgLastSeqNumber_Object = MibScalar
usdLogMsgLastSeqNumber = _UsdLogMsgLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 2),
    _UsdLogMsgLastSeqNumber_Type()
)
usdLogMsgLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgLastSeqNumber.setStatus("current")
_UsdLogMsgTable_Object = MibTable
usdLogMsgTable = _UsdLogMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdLogMsgTable.setStatus("current")
_UsdLogMsgEntry_Object = MibTableRow
usdLogMsgEntry = _UsdLogMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1)
)
usdLogMsgEntry.setIndexNames(
    (0, "Unisphere-Data-LOG-MIB", "usdLogMsgSysUpTimeStamp"),
    (0, "Unisphere-Data-LOG-MIB", "usdLogMsgSequenceNumber"),
)
if mibBuilder.loadTexts:
    usdLogMsgEntry.setStatus("current")
_UsdLogMsgSysUpTimeStamp_Type = TimeStamp
_UsdLogMsgSysUpTimeStamp_Object = MibTableColumn
usdLogMsgSysUpTimeStamp = _UsdLogMsgSysUpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 1),
    _UsdLogMsgSysUpTimeStamp_Type()
)
usdLogMsgSysUpTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdLogMsgSysUpTimeStamp.setStatus("current")
_UsdLogMsgSequenceNumber_Type = Unsigned32
_UsdLogMsgSequenceNumber_Object = MibTableColumn
usdLogMsgSequenceNumber = _UsdLogMsgSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 2),
    _UsdLogMsgSequenceNumber_Type()
)
usdLogMsgSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdLogMsgSequenceNumber.setStatus("current")
_UsdLogMsgCatName_Type = UsdLogCatName
_UsdLogMsgCatName_Object = MibTableColumn
usdLogMsgCatName = _UsdLogMsgCatName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 3),
    _UsdLogMsgCatName_Type()
)
usdLogMsgCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgCatName.setStatus("current")
_UsdLogMsgCatIndex_Type = Integer32
_UsdLogMsgCatIndex_Object = MibTableColumn
usdLogMsgCatIndex = _UsdLogMsgCatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 4),
    _UsdLogMsgCatIndex_Type()
)
usdLogMsgCatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgCatIndex.setStatus("current")
_UsdLogMsgSeverity_Type = UsdLogSeverity
_UsdLogMsgSeverity_Object = MibTableColumn
usdLogMsgSeverity = _UsdLogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 5),
    _UsdLogMsgSeverity_Type()
)
usdLogMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgSeverity.setStatus("current")
_UsdLogMsgText_Type = DisplayString
_UsdLogMsgText_Object = MibTableColumn
usdLogMsgText = _UsdLogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 6),
    _UsdLogMsgText_Type()
)
usdLogMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgText.setStatus("current")
_UsdLogMsgDateAndTimeStamp_Type = DateAndTime
_UsdLogMsgDateAndTimeStamp_Object = MibTableColumn
usdLogMsgDateAndTimeStamp = _UsdLogMsgDateAndTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 7),
    _UsdLogMsgDateAndTimeStamp_Type()
)
usdLogMsgDateAndTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdLogMsgDateAndTimeStamp.setStatus("current")
_UsdLogTrapControl_ObjectIdentity = ObjectIdentity
usdLogTrapControl = _UsdLogTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2)
)


class _UsdLogMsgThreshold_Type(Integer32):
    """Custom type usdLogMsgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdLogMsgThreshold_Type.__name__ = "Integer32"
_UsdLogMsgThreshold_Object = MibScalar
usdLogMsgThreshold = _UsdLogMsgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2, 1),
    _UsdLogMsgThreshold_Type()
)
usdLogMsgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdLogMsgThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdLogMsgThreshold.setUnits("percent")
_UsdLogMIBConformance_ObjectIdentity = ObjectIdentity
usdLogMIBConformance = _UsdLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4)
)
_UsdLogMIBCompliances_ObjectIdentity = ObjectIdentity
usdLogMIBCompliances = _UsdLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1)
)
_UsdLogMIBGroups_ObjectIdentity = ObjectIdentity
usdLogMIBGroups = _UsdLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2)
)

# Managed Objects groups

usdLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 1)
)
usdLogGroup.setObjects(
      *(("Unisphere-Data-LOG-MIB", "usdLogDestSyslogSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogDestSyslogAddress"),
        ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatName"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgText"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    usdLogGroup.setStatus("obsolete")

usdLogGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 2)
)
usdLogGroup2.setObjects(
      *(("Unisphere-Data-LOG-MIB", "usdLogSyslogRowStatus"),
        ("Unisphere-Data-LOG-MIB", "usdLogSyslogSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogSyslogFacility"),
        ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatName"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"),
        ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgText"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    usdLogGroup2.setStatus("current")


# Notification objects

usdLogMsgThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0, 1)
)
usdLogMsgThresholdTrap.setObjects(
      *(("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"),
        ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    usdLogMsgThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

usdLogTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 3)
)
usdLogTrapGroup.setObjects(
    ("Unisphere-Data-LOG-MIB", "usdLogMsgThresholdTrap")
)
if mibBuilder.loadTexts:
    usdLogTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdLogCompliance.setStatus(
        "obsolete"
    )

usdLogCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdLogCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-LOG-MIB",
    **{"UsdLogCatName": UsdLogCatName,
       "UsdLogVerbosity": UsdLogVerbosity,
       "UsdLogSyslogFacility": UsdLogSyslogFacility,
       "usdLogMIB": usdLogMIB,
       "usdLogTrapPrefix": usdLogTrapPrefix,
       "usdLogMsgThresholdTrap": usdLogMsgThresholdTrap,
       "usdLogObjects": usdLogObjects,
       "usdLogDestinations": usdLogDestinations,
       "usdLogDestSyslog": usdLogDestSyslog,
       "usdLogDestSyslogSeverity": usdLogDestSyslogSeverity,
       "usdLogDestSyslogAddress": usdLogDestSyslogAddress,
       "usdLogSyslogTable": usdLogSyslogTable,
       "usdLogSyslogEntry": usdLogSyslogEntry,
       "usdLogSyslogIpAddress": usdLogSyslogIpAddress,
       "usdLogSyslogRowStatus": usdLogSyslogRowStatus,
       "usdLogSyslogSeverity": usdLogSyslogSeverity,
       "usdLogSyslogFacility": usdLogSyslogFacility,
       "usdLogDestConsole": usdLogDestConsole,
       "usdLogDestConsoleSeverity": usdLogDestConsoleSeverity,
       "usdLogDestNvFile": usdLogDestNvFile,
       "usdLogDestNvFileSeverity": usdLogDestNvFileSeverity,
       "usdLogCategories": usdLogCategories,
       "usdLogCatScalars": usdLogCatScalars,
       "usdLogCatTable": usdLogCatTable,
       "usdLogCatEntry": usdLogCatEntry,
       "usdLogCatIndex": usdLogCatIndex,
       "usdLogCatName": usdLogCatName,
       "usdLogCatDescr": usdLogCatDescr,
       "usdLogCatEngineering": usdLogCatEngineering,
       "usdLogCatDiscards": usdLogCatDiscards,
       "usdLogCatSeverity": usdLogCatSeverity,
       "usdLogCatVerbosity": usdLogCatVerbosity,
       "usdLogCatNameTable": usdLogCatNameTable,
       "usdLogCatNameEntry": usdLogCatNameEntry,
       "usdLogCatNameName": usdLogCatNameName,
       "usdLogCatNameIndex": usdLogCatNameIndex,
       "usdLogMessages": usdLogMessages,
       "usdLogMsgScalars": usdLogMsgScalars,
       "usdLogMsgCapacity": usdLogMsgCapacity,
       "usdLogMsgLastSeqNumber": usdLogMsgLastSeqNumber,
       "usdLogMsgTable": usdLogMsgTable,
       "usdLogMsgEntry": usdLogMsgEntry,
       "usdLogMsgSysUpTimeStamp": usdLogMsgSysUpTimeStamp,
       "usdLogMsgSequenceNumber": usdLogMsgSequenceNumber,
       "usdLogMsgCatName": usdLogMsgCatName,
       "usdLogMsgCatIndex": usdLogMsgCatIndex,
       "usdLogMsgSeverity": usdLogMsgSeverity,
       "usdLogMsgText": usdLogMsgText,
       "usdLogMsgDateAndTimeStamp": usdLogMsgDateAndTimeStamp,
       "usdLogTrapControl": usdLogTrapControl,
       "usdLogMsgThreshold": usdLogMsgThreshold,
       "usdLogMIBConformance": usdLogMIBConformance,
       "usdLogMIBCompliances": usdLogMIBCompliances,
       "usdLogCompliance": usdLogCompliance,
       "usdLogCompliance2": usdLogCompliance2,
       "usdLogMIBGroups": usdLogMIBGroups,
       "usdLogGroup": usdLogGroup,
       "usdLogGroup2": usdLogGroup2,
       "usdLogTrapGroup": usdLogTrapGroup}
)
