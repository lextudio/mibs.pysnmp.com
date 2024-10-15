# SNMP MIB module (Juniper-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:43 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniLogSeverity,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniLogSeverity")

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


# MODULE-IDENTITY

juniLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28)
)
juniLogMIB.setRevisions(
        ("2002-09-16 21:44",
         "2001-03-16 19:02",
         "2000-03-27 05:00",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniLogCatName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class JuniLogVerbosity(Integer32, TextualConvention):
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



class JuniLogSyslogFacility(Integer32, TextualConvention):
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

_JuniLogTrapPrefix_ObjectIdentity = ObjectIdentity
juniLogTrapPrefix = _JuniLogTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0)
)
_JuniLogObjects_ObjectIdentity = ObjectIdentity
juniLogObjects = _JuniLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1)
)
_JuniLogDestinations_ObjectIdentity = ObjectIdentity
juniLogDestinations = _JuniLogDestinations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1)
)
_JuniLogDestSyslog_ObjectIdentity = ObjectIdentity
juniLogDestSyslog = _JuniLogDestSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1)
)
_JuniLogDestSyslogSeverity_Type = JuniLogSeverity
_JuniLogDestSyslogSeverity_Object = MibScalar
juniLogDestSyslogSeverity = _JuniLogDestSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 1),
    _JuniLogDestSyslogSeverity_Type()
)
juniLogDestSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogDestSyslogSeverity.setStatus("obsolete")
_JuniLogDestSyslogAddress_Type = IpAddress
_JuniLogDestSyslogAddress_Object = MibScalar
juniLogDestSyslogAddress = _JuniLogDestSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 2),
    _JuniLogDestSyslogAddress_Type()
)
juniLogDestSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogDestSyslogAddress.setStatus("obsolete")
_JuniLogSyslogTable_Object = MibTable
juniLogSyslogTable = _JuniLogSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniLogSyslogTable.setStatus("current")
_JuniLogSyslogEntry_Object = MibTableRow
juniLogSyslogEntry = _JuniLogSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1)
)
juniLogSyslogEntry.setIndexNames(
    (0, "Juniper-LOG-MIB", "juniLogSyslogIpAddress"),
)
if mibBuilder.loadTexts:
    juniLogSyslogEntry.setStatus("current")
_JuniLogSyslogIpAddress_Type = IpAddress
_JuniLogSyslogIpAddress_Object = MibTableColumn
juniLogSyslogIpAddress = _JuniLogSyslogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 1),
    _JuniLogSyslogIpAddress_Type()
)
juniLogSyslogIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniLogSyslogIpAddress.setStatus("current")
_JuniLogSyslogRowStatus_Type = RowStatus
_JuniLogSyslogRowStatus_Object = MibTableColumn
juniLogSyslogRowStatus = _JuniLogSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 2),
    _JuniLogSyslogRowStatus_Type()
)
juniLogSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogSyslogRowStatus.setStatus("current")


class _JuniLogSyslogSeverity_Type(JuniLogSeverity):
    """Custom type juniLogSyslogSeverity based on JuniLogSeverity"""


_JuniLogSyslogSeverity_Object = MibTableColumn
juniLogSyslogSeverity = _JuniLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 3),
    _JuniLogSyslogSeverity_Type()
)
juniLogSyslogSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogSyslogSeverity.setStatus("current")


class _JuniLogSyslogFacility_Type(JuniLogSyslogFacility):
    """Custom type juniLogSyslogFacility based on JuniLogSyslogFacility"""


_JuniLogSyslogFacility_Object = MibTableColumn
juniLogSyslogFacility = _JuniLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 4),
    _JuniLogSyslogFacility_Type()
)
juniLogSyslogFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogSyslogFacility.setStatus("current")
_JuniLogDestConsole_ObjectIdentity = ObjectIdentity
juniLogDestConsole = _JuniLogDestConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2)
)
_JuniLogDestConsoleSeverity_Type = JuniLogSeverity
_JuniLogDestConsoleSeverity_Object = MibScalar
juniLogDestConsoleSeverity = _JuniLogDestConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2, 1),
    _JuniLogDestConsoleSeverity_Type()
)
juniLogDestConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogDestConsoleSeverity.setStatus("current")
_JuniLogDestNvFile_ObjectIdentity = ObjectIdentity
juniLogDestNvFile = _JuniLogDestNvFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3)
)
_JuniLogDestNvFileSeverity_Type = JuniLogSeverity
_JuniLogDestNvFileSeverity_Object = MibScalar
juniLogDestNvFileSeverity = _JuniLogDestNvFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3, 1),
    _JuniLogDestNvFileSeverity_Type()
)
juniLogDestNvFileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogDestNvFileSeverity.setStatus("current")
_JuniLogCategories_ObjectIdentity = ObjectIdentity
juniLogCategories = _JuniLogCategories_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2)
)
_JuniLogCatScalars_ObjectIdentity = ObjectIdentity
juniLogCatScalars = _JuniLogCatScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 1)
)
_JuniLogCatTable_Object = MibTable
juniLogCatTable = _JuniLogCatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniLogCatTable.setStatus("current")
_JuniLogCatEntry_Object = MibTableRow
juniLogCatEntry = _JuniLogCatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1)
)
juniLogCatEntry.setIndexNames(
    (0, "Juniper-LOG-MIB", "juniLogCatIndex"),
)
if mibBuilder.loadTexts:
    juniLogCatEntry.setStatus("current")


class _JuniLogCatIndex_Type(Integer32):
    """Custom type juniLogCatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniLogCatIndex_Type.__name__ = "Integer32"
_JuniLogCatIndex_Object = MibTableColumn
juniLogCatIndex = _JuniLogCatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 1),
    _JuniLogCatIndex_Type()
)
juniLogCatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniLogCatIndex.setStatus("current")
_JuniLogCatName_Type = JuniLogCatName
_JuniLogCatName_Object = MibTableColumn
juniLogCatName = _JuniLogCatName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 2),
    _JuniLogCatName_Type()
)
juniLogCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatName.setStatus("current")
_JuniLogCatDescr_Type = DisplayString
_JuniLogCatDescr_Object = MibTableColumn
juniLogCatDescr = _JuniLogCatDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 3),
    _JuniLogCatDescr_Type()
)
juniLogCatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatDescr.setStatus("current")
_JuniLogCatEngineering_Type = TruthValue
_JuniLogCatEngineering_Object = MibTableColumn
juniLogCatEngineering = _JuniLogCatEngineering_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 4),
    _JuniLogCatEngineering_Type()
)
juniLogCatEngineering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatEngineering.setStatus("current")
_JuniLogCatDiscards_Type = Counter32
_JuniLogCatDiscards_Object = MibTableColumn
juniLogCatDiscards = _JuniLogCatDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 5),
    _JuniLogCatDiscards_Type()
)
juniLogCatDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatDiscards.setStatus("current")
_JuniLogCatSeverity_Type = JuniLogSeverity
_JuniLogCatSeverity_Object = MibTableColumn
juniLogCatSeverity = _JuniLogCatSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 6),
    _JuniLogCatSeverity_Type()
)
juniLogCatSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogCatSeverity.setStatus("current")
_JuniLogCatVerbosity_Type = JuniLogVerbosity
_JuniLogCatVerbosity_Object = MibTableColumn
juniLogCatVerbosity = _JuniLogCatVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 7),
    _JuniLogCatVerbosity_Type()
)
juniLogCatVerbosity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogCatVerbosity.setStatus("current")
_JuniLogCatNameTable_Object = MibTable
juniLogCatNameTable = _JuniLogCatNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniLogCatNameTable.setStatus("current")
_JuniLogCatNameEntry_Object = MibTableRow
juniLogCatNameEntry = _JuniLogCatNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1)
)
juniLogCatNameEntry.setIndexNames(
    (1, "Juniper-LOG-MIB", "juniLogCatNameName"),
)
if mibBuilder.loadTexts:
    juniLogCatNameEntry.setStatus("current")
_JuniLogCatNameName_Type = JuniLogCatName
_JuniLogCatNameName_Object = MibTableColumn
juniLogCatNameName = _JuniLogCatNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 1),
    _JuniLogCatNameName_Type()
)
juniLogCatNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatNameName.setStatus("current")


class _JuniLogCatNameIndex_Type(Integer32):
    """Custom type juniLogCatNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniLogCatNameIndex_Type.__name__ = "Integer32"
_JuniLogCatNameIndex_Object = MibTableColumn
juniLogCatNameIndex = _JuniLogCatNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 2),
    _JuniLogCatNameIndex_Type()
)
juniLogCatNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogCatNameIndex.setStatus("current")
_JuniLogMessages_ObjectIdentity = ObjectIdentity
juniLogMessages = _JuniLogMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3)
)
_JuniLogMsgScalars_ObjectIdentity = ObjectIdentity
juniLogMsgScalars = _JuniLogMsgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1)
)
_JuniLogMsgCapacity_Type = Integer32
_JuniLogMsgCapacity_Object = MibScalar
juniLogMsgCapacity = _JuniLogMsgCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 1),
    _JuniLogMsgCapacity_Type()
)
juniLogMsgCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgCapacity.setStatus("current")
if mibBuilder.loadTexts:
    juniLogMsgCapacity.setUnits("messages")
_JuniLogMsgLastSeqNumber_Type = Counter32
_JuniLogMsgLastSeqNumber_Object = MibScalar
juniLogMsgLastSeqNumber = _JuniLogMsgLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 2),
    _JuniLogMsgLastSeqNumber_Type()
)
juniLogMsgLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgLastSeqNumber.setStatus("current")
_JuniLogMsgTable_Object = MibTable
juniLogMsgTable = _JuniLogMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniLogMsgTable.setStatus("current")
_JuniLogMsgEntry_Object = MibTableRow
juniLogMsgEntry = _JuniLogMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1)
)
juniLogMsgEntry.setIndexNames(
    (0, "Juniper-LOG-MIB", "juniLogMsgSysUpTimeStamp"),
    (0, "Juniper-LOG-MIB", "juniLogMsgSequenceNumber"),
)
if mibBuilder.loadTexts:
    juniLogMsgEntry.setStatus("current")
_JuniLogMsgSysUpTimeStamp_Type = TimeStamp
_JuniLogMsgSysUpTimeStamp_Object = MibTableColumn
juniLogMsgSysUpTimeStamp = _JuniLogMsgSysUpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 1),
    _JuniLogMsgSysUpTimeStamp_Type()
)
juniLogMsgSysUpTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniLogMsgSysUpTimeStamp.setStatus("current")
_JuniLogMsgSequenceNumber_Type = Unsigned32
_JuniLogMsgSequenceNumber_Object = MibTableColumn
juniLogMsgSequenceNumber = _JuniLogMsgSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 2),
    _JuniLogMsgSequenceNumber_Type()
)
juniLogMsgSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniLogMsgSequenceNumber.setStatus("current")
_JuniLogMsgCatName_Type = JuniLogCatName
_JuniLogMsgCatName_Object = MibTableColumn
juniLogMsgCatName = _JuniLogMsgCatName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 3),
    _JuniLogMsgCatName_Type()
)
juniLogMsgCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgCatName.setStatus("current")
_JuniLogMsgCatIndex_Type = Integer32
_JuniLogMsgCatIndex_Object = MibTableColumn
juniLogMsgCatIndex = _JuniLogMsgCatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 4),
    _JuniLogMsgCatIndex_Type()
)
juniLogMsgCatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgCatIndex.setStatus("current")
_JuniLogMsgSeverity_Type = JuniLogSeverity
_JuniLogMsgSeverity_Object = MibTableColumn
juniLogMsgSeverity = _JuniLogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 5),
    _JuniLogMsgSeverity_Type()
)
juniLogMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgSeverity.setStatus("current")
_JuniLogMsgText_Type = DisplayString
_JuniLogMsgText_Object = MibTableColumn
juniLogMsgText = _JuniLogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 6),
    _JuniLogMsgText_Type()
)
juniLogMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgText.setStatus("current")
_JuniLogMsgDateAndTimeStamp_Type = DateAndTime
_JuniLogMsgDateAndTimeStamp_Object = MibTableColumn
juniLogMsgDateAndTimeStamp = _JuniLogMsgDateAndTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 7),
    _JuniLogMsgDateAndTimeStamp_Type()
)
juniLogMsgDateAndTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLogMsgDateAndTimeStamp.setStatus("current")
_JuniLogTrapControl_ObjectIdentity = ObjectIdentity
juniLogTrapControl = _JuniLogTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2)
)


class _JuniLogMsgThreshold_Type(Integer32):
    """Custom type juniLogMsgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniLogMsgThreshold_Type.__name__ = "Integer32"
_JuniLogMsgThreshold_Object = MibScalar
juniLogMsgThreshold = _JuniLogMsgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2, 1),
    _JuniLogMsgThreshold_Type()
)
juniLogMsgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLogMsgThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniLogMsgThreshold.setUnits("percent")
_JuniLogMIBConformance_ObjectIdentity = ObjectIdentity
juniLogMIBConformance = _JuniLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4)
)
_JuniLogMIBCompliances_ObjectIdentity = ObjectIdentity
juniLogMIBCompliances = _JuniLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1)
)
_JuniLogMIBGroups_ObjectIdentity = ObjectIdentity
juniLogMIBGroups = _JuniLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2)
)

# Managed Objects groups

juniLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 1)
)
juniLogGroup.setObjects(
      *(("Juniper-LOG-MIB", "juniLogDestSyslogSeverity"),
        ("Juniper-LOG-MIB", "juniLogDestSyslogAddress"),
        ("Juniper-LOG-MIB", "juniLogDestConsoleSeverity"),
        ("Juniper-LOG-MIB", "juniLogDestNvFileSeverity"),
        ("Juniper-LOG-MIB", "juniLogCatName"),
        ("Juniper-LOG-MIB", "juniLogCatDescr"),
        ("Juniper-LOG-MIB", "juniLogCatEngineering"),
        ("Juniper-LOG-MIB", "juniLogCatDiscards"),
        ("Juniper-LOG-MIB", "juniLogCatSeverity"),
        ("Juniper-LOG-MIB", "juniLogCatVerbosity"),
        ("Juniper-LOG-MIB", "juniLogCatNameName"),
        ("Juniper-LOG-MIB", "juniLogCatNameIndex"),
        ("Juniper-LOG-MIB", "juniLogMsgCapacity"),
        ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"),
        ("Juniper-LOG-MIB", "juniLogMsgCatName"),
        ("Juniper-LOG-MIB", "juniLogMsgCatIndex"),
        ("Juniper-LOG-MIB", "juniLogMsgSeverity"),
        ("Juniper-LOG-MIB", "juniLogMsgText"),
        ("Juniper-LOG-MIB", "juniLogMsgDateAndTimeStamp"),
        ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    juniLogGroup.setStatus("obsolete")

juniLogGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 2)
)
juniLogGroup2.setObjects(
      *(("Juniper-LOG-MIB", "juniLogSyslogRowStatus"),
        ("Juniper-LOG-MIB", "juniLogSyslogSeverity"),
        ("Juniper-LOG-MIB", "juniLogSyslogFacility"),
        ("Juniper-LOG-MIB", "juniLogDestConsoleSeverity"),
        ("Juniper-LOG-MIB", "juniLogDestNvFileSeverity"),
        ("Juniper-LOG-MIB", "juniLogCatName"),
        ("Juniper-LOG-MIB", "juniLogCatDescr"),
        ("Juniper-LOG-MIB", "juniLogCatEngineering"),
        ("Juniper-LOG-MIB", "juniLogCatDiscards"),
        ("Juniper-LOG-MIB", "juniLogCatSeverity"),
        ("Juniper-LOG-MIB", "juniLogCatVerbosity"),
        ("Juniper-LOG-MIB", "juniLogCatNameName"),
        ("Juniper-LOG-MIB", "juniLogCatNameIndex"),
        ("Juniper-LOG-MIB", "juniLogMsgCapacity"),
        ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"),
        ("Juniper-LOG-MIB", "juniLogMsgCatName"),
        ("Juniper-LOG-MIB", "juniLogMsgCatIndex"),
        ("Juniper-LOG-MIB", "juniLogMsgSeverity"),
        ("Juniper-LOG-MIB", "juniLogMsgText"),
        ("Juniper-LOG-MIB", "juniLogMsgDateAndTimeStamp"),
        ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    juniLogGroup2.setStatus("current")


# Notification objects

juniLogMsgThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0, 1)
)
juniLogMsgThresholdTrap.setObjects(
      *(("Juniper-LOG-MIB", "juniLogMsgCapacity"),
        ("Juniper-LOG-MIB", "juniLogMsgLastSeqNumber"),
        ("Juniper-LOG-MIB", "juniLogMsgThreshold"))
)
if mibBuilder.loadTexts:
    juniLogMsgThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

juniLogTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 3)
)
juniLogTrapGroup.setObjects(
    ("Juniper-LOG-MIB", "juniLogMsgThresholdTrap")
)
if mibBuilder.loadTexts:
    juniLogTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniLogCompliance.setStatus(
        "obsolete"
    )

juniLogCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniLogCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-LOG-MIB",
    **{"JuniLogCatName": JuniLogCatName,
       "JuniLogVerbosity": JuniLogVerbosity,
       "JuniLogSyslogFacility": JuniLogSyslogFacility,
       "juniLogMIB": juniLogMIB,
       "juniLogTrapPrefix": juniLogTrapPrefix,
       "juniLogMsgThresholdTrap": juniLogMsgThresholdTrap,
       "juniLogObjects": juniLogObjects,
       "juniLogDestinations": juniLogDestinations,
       "juniLogDestSyslog": juniLogDestSyslog,
       "juniLogDestSyslogSeverity": juniLogDestSyslogSeverity,
       "juniLogDestSyslogAddress": juniLogDestSyslogAddress,
       "juniLogSyslogTable": juniLogSyslogTable,
       "juniLogSyslogEntry": juniLogSyslogEntry,
       "juniLogSyslogIpAddress": juniLogSyslogIpAddress,
       "juniLogSyslogRowStatus": juniLogSyslogRowStatus,
       "juniLogSyslogSeverity": juniLogSyslogSeverity,
       "juniLogSyslogFacility": juniLogSyslogFacility,
       "juniLogDestConsole": juniLogDestConsole,
       "juniLogDestConsoleSeverity": juniLogDestConsoleSeverity,
       "juniLogDestNvFile": juniLogDestNvFile,
       "juniLogDestNvFileSeverity": juniLogDestNvFileSeverity,
       "juniLogCategories": juniLogCategories,
       "juniLogCatScalars": juniLogCatScalars,
       "juniLogCatTable": juniLogCatTable,
       "juniLogCatEntry": juniLogCatEntry,
       "juniLogCatIndex": juniLogCatIndex,
       "juniLogCatName": juniLogCatName,
       "juniLogCatDescr": juniLogCatDescr,
       "juniLogCatEngineering": juniLogCatEngineering,
       "juniLogCatDiscards": juniLogCatDiscards,
       "juniLogCatSeverity": juniLogCatSeverity,
       "juniLogCatVerbosity": juniLogCatVerbosity,
       "juniLogCatNameTable": juniLogCatNameTable,
       "juniLogCatNameEntry": juniLogCatNameEntry,
       "juniLogCatNameName": juniLogCatNameName,
       "juniLogCatNameIndex": juniLogCatNameIndex,
       "juniLogMessages": juniLogMessages,
       "juniLogMsgScalars": juniLogMsgScalars,
       "juniLogMsgCapacity": juniLogMsgCapacity,
       "juniLogMsgLastSeqNumber": juniLogMsgLastSeqNumber,
       "juniLogMsgTable": juniLogMsgTable,
       "juniLogMsgEntry": juniLogMsgEntry,
       "juniLogMsgSysUpTimeStamp": juniLogMsgSysUpTimeStamp,
       "juniLogMsgSequenceNumber": juniLogMsgSequenceNumber,
       "juniLogMsgCatName": juniLogMsgCatName,
       "juniLogMsgCatIndex": juniLogMsgCatIndex,
       "juniLogMsgSeverity": juniLogMsgSeverity,
       "juniLogMsgText": juniLogMsgText,
       "juniLogMsgDateAndTimeStamp": juniLogMsgDateAndTimeStamp,
       "juniLogTrapControl": juniLogTrapControl,
       "juniLogMsgThreshold": juniLogMsgThreshold,
       "juniLogMIBConformance": juniLogMIBConformance,
       "juniLogMIBCompliances": juniLogMIBCompliances,
       "juniLogCompliance": juniLogCompliance,
       "juniLogCompliance2": juniLogCompliance2,
       "juniLogMIBGroups": juniLogMIBGroups,
       "juniLogGroup": juniLogGroup,
       "juniLogGroup2": juniLogGroup2,
       "juniLogTrapGroup": juniLogTrapGroup}
)
