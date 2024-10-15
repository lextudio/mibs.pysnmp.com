# SNMP MIB module (JUNIPER-OTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-OTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:58 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxOtnMibRoot,
 jnxOtnNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxOtnMibRoot",
    "jnxOtnNotifications")

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

jnxOtnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1)
)
jnxOtnMib.setRevisions(
        ("2015-06-17 00:00",
         "2008-07-10 00:00",
         "2008-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxOtnAlarmId(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxOtnAlarms_ObjectIdentity = ObjectIdentity
jnxOtnAlarms = _JnxOtnAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1)
)
_JnxOtnAlarmTable_Object = MibTable
jnxOtnAlarmTable = _JnxOtnAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxOtnAlarmTable.setStatus("current")
_JnxOtnAlarmEntry_Object = MibTableRow
jnxOtnAlarmEntry = _JnxOtnAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1)
)
jnxOtnAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnAlarmEntry.setStatus("current")
_JnxOtnCurrentAlarms_Type = JnxOtnAlarmId
_JnxOtnCurrentAlarms_Object = MibTableColumn
jnxOtnCurrentAlarms = _JnxOtnCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 1),
    _JnxOtnCurrentAlarms_Type()
)
jnxOtnCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentAlarms.setStatus("current")
_JnxOtnLastAlarmId_Type = JnxOtnAlarmId
_JnxOtnLastAlarmId_Object = MibTableColumn
jnxOtnLastAlarmId = _JnxOtnLastAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 2),
    _JnxOtnLastAlarmId_Type()
)
jnxOtnLastAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnLastAlarmId.setStatus("current")
_JnxOtnLastAlarmTime_Type = TimeTicks
_JnxOtnLastAlarmTime_Object = MibTableColumn
jnxOtnLastAlarmTime = _JnxOtnLastAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 3),
    _JnxOtnLastAlarmTime_Type()
)
jnxOtnLastAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnLastAlarmTime.setStatus("current")
_JnxOtnLastAlarmDate_Type = DateAndTime
_JnxOtnLastAlarmDate_Object = MibTableColumn
jnxOtnLastAlarmDate = _JnxOtnLastAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 4),
    _JnxOtnLastAlarmDate_Type()
)
jnxOtnLastAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnLastAlarmDate.setStatus("current")


class _JnxOtnLastAlarmEvent_Type(Integer32):
    """Custom type jnxOtnLastAlarmEvent based on Integer32"""
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


_JnxOtnLastAlarmEvent_Type.__name__ = "Integer32"
_JnxOtnLastAlarmEvent_Object = MibTableColumn
jnxOtnLastAlarmEvent = _JnxOtnLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 5),
    _JnxOtnLastAlarmEvent_Type()
)
jnxOtnLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnLastAlarmEvent.setStatus("current")
_JnxOtnPerformanceMonitoring_ObjectIdentity = ObjectIdentity
jnxOtnPerformanceMonitoring = _JnxOtnPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2)
)
_JnxOtnCurrentOdu15minTable_Object = MibTable
jnxOtnCurrentOdu15minTable = _JnxOtnCurrentOdu15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minTable.setStatus("current")
_JnxOtnCurrentOdu15minEntry_Object = MibTableRow
jnxOtnCurrentOdu15minEntry = _JnxOtnCurrentOdu15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1)
)
jnxOtnCurrentOdu15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minEntry.setStatus("current")
_JnxOtnCurrentOdu15minBIP_Type = Unsigned32
_JnxOtnCurrentOdu15minBIP_Object = MibTableColumn
jnxOtnCurrentOdu15minBIP = _JnxOtnCurrentOdu15minBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 1),
    _JnxOtnCurrentOdu15minBIP_Type()
)
jnxOtnCurrentOdu15minBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minBIP.setStatus("current")
_JnxOtnCurrentOdu15minBBE_Type = Unsigned32
_JnxOtnCurrentOdu15minBBE_Object = MibTableColumn
jnxOtnCurrentOdu15minBBE = _JnxOtnCurrentOdu15minBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 2),
    _JnxOtnCurrentOdu15minBBE_Type()
)
jnxOtnCurrentOdu15minBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minBBE.setStatus("current")
_JnxOtnCurrentOdu15minES_Type = Unsigned32
_JnxOtnCurrentOdu15minES_Object = MibTableColumn
jnxOtnCurrentOdu15minES = _JnxOtnCurrentOdu15minES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 3),
    _JnxOtnCurrentOdu15minES_Type()
)
jnxOtnCurrentOdu15minES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minES.setStatus("current")
_JnxOtnCurrentOdu15minSES_Type = Unsigned32
_JnxOtnCurrentOdu15minSES_Object = MibTableColumn
jnxOtnCurrentOdu15minSES = _JnxOtnCurrentOdu15minSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 4),
    _JnxOtnCurrentOdu15minSES_Type()
)
jnxOtnCurrentOdu15minSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minSES.setStatus("current")
_JnxOtnCurrentOdu15minUAS_Type = Unsigned32
_JnxOtnCurrentOdu15minUAS_Object = MibTableColumn
jnxOtnCurrentOdu15minUAS = _JnxOtnCurrentOdu15minUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 5),
    _JnxOtnCurrentOdu15minUAS_Type()
)
jnxOtnCurrentOdu15minUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minUAS.setStatus("current")
_JnxOtnCurrentOdu15minElapsedTime_Type = Unsigned32
_JnxOtnCurrentOdu15minElapsedTime_Object = MibTableColumn
jnxOtnCurrentOdu15minElapsedTime = _JnxOtnCurrentOdu15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 6),
    _JnxOtnCurrentOdu15minElapsedTime_Type()
)
jnxOtnCurrentOdu15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOdu15minElapsedTime.setStatus("current")
_JnxOtnIntervalOdu15minTable_Object = MibTable
jnxOtnIntervalOdu15minTable = _JnxOtnIntervalOdu15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minTable.setStatus("current")
_JnxOtnIntervalOdu15minEntry_Object = MibTableRow
jnxOtnIntervalOdu15minEntry = _JnxOtnIntervalOdu15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1)
)
jnxOtnIntervalOdu15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOdu15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minEntry.setStatus("current")


class _JnxOtnIntervalOdu15minIntervalNumber_Type(Integer32):
    """Custom type jnxOtnIntervalOdu15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOtnIntervalOdu15minIntervalNumber_Type.__name__ = "Integer32"
_JnxOtnIntervalOdu15minIntervalNumber_Object = MibTableColumn
jnxOtnIntervalOdu15minIntervalNumber = _JnxOtnIntervalOdu15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 1),
    _JnxOtnIntervalOdu15minIntervalNumber_Type()
)
jnxOtnIntervalOdu15minIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minIntervalNumber.setStatus("current")
_JnxOtnIntervalOdu15minBIP_Type = Unsigned32
_JnxOtnIntervalOdu15minBIP_Object = MibTableColumn
jnxOtnIntervalOdu15minBIP = _JnxOtnIntervalOdu15minBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 2),
    _JnxOtnIntervalOdu15minBIP_Type()
)
jnxOtnIntervalOdu15minBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minBIP.setStatus("current")
_JnxOtnIntervalOdu15minBBE_Type = Unsigned32
_JnxOtnIntervalOdu15minBBE_Object = MibTableColumn
jnxOtnIntervalOdu15minBBE = _JnxOtnIntervalOdu15minBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 3),
    _JnxOtnIntervalOdu15minBBE_Type()
)
jnxOtnIntervalOdu15minBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minBBE.setStatus("current")
_JnxOtnIntervalOdu15minES_Type = Unsigned32
_JnxOtnIntervalOdu15minES_Object = MibTableColumn
jnxOtnIntervalOdu15minES = _JnxOtnIntervalOdu15minES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 4),
    _JnxOtnIntervalOdu15minES_Type()
)
jnxOtnIntervalOdu15minES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minES.setStatus("current")
_JnxOtnIntervalOdu15minSES_Type = Unsigned32
_JnxOtnIntervalOdu15minSES_Object = MibTableColumn
jnxOtnIntervalOdu15minSES = _JnxOtnIntervalOdu15minSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 5),
    _JnxOtnIntervalOdu15minSES_Type()
)
jnxOtnIntervalOdu15minSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minSES.setStatus("current")
_JnxOtnIntervalOdu15minUAS_Type = Unsigned32
_JnxOtnIntervalOdu15minUAS_Object = MibTableColumn
jnxOtnIntervalOdu15minUAS = _JnxOtnIntervalOdu15minUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 6),
    _JnxOtnIntervalOdu15minUAS_Type()
)
jnxOtnIntervalOdu15minUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minUAS.setStatus("current")
_JnxOtnIntervalOdu15minInvalidData_Type = Unsigned32
_JnxOtnIntervalOdu15minInvalidData_Object = MibTableColumn
jnxOtnIntervalOdu15minInvalidData = _JnxOtnIntervalOdu15minInvalidData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 7),
    _JnxOtnIntervalOdu15minInvalidData_Type()
)
jnxOtnIntervalOdu15minInvalidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOdu15minInvalidData.setStatus("current")
_JnxOtnIntervalODdu15minTimeStamp_Type = DateAndTime
_JnxOtnIntervalODdu15minTimeStamp_Object = MibTableColumn
jnxOtnIntervalODdu15minTimeStamp = _JnxOtnIntervalODdu15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 8),
    _JnxOtnIntervalODdu15minTimeStamp_Type()
)
jnxOtnIntervalODdu15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalODdu15minTimeStamp.setStatus("current")
_JnxOtnTotalOduTable_Object = MibTable
jnxOtnTotalOduTable = _JnxOtnTotalOduTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxOtnTotalOduTable.setStatus("current")
_JnxOtnTotalOduEntry_Object = MibTableRow
jnxOtnTotalOduEntry = _JnxOtnTotalOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1)
)
jnxOtnTotalOduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnTotalOduEntry.setStatus("current")
_JnxOtnTotalOduDayNumber_Type = Integer32
_JnxOtnTotalOduDayNumber_Object = MibTableColumn
jnxOtnTotalOduDayNumber = _JnxOtnTotalOduDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 1),
    _JnxOtnTotalOduDayNumber_Type()
)
jnxOtnTotalOduDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduDayNumber.setStatus("current")
_JnxOtnTotalOduBIP_Type = Unsigned32
_JnxOtnTotalOduBIP_Object = MibTableColumn
jnxOtnTotalOduBIP = _JnxOtnTotalOduBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 2),
    _JnxOtnTotalOduBIP_Type()
)
jnxOtnTotalOduBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduBIP.setStatus("current")
_JnxOtnTotalOduBBE_Type = Unsigned32
_JnxOtnTotalOduBBE_Object = MibTableColumn
jnxOtnTotalOduBBE = _JnxOtnTotalOduBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 3),
    _JnxOtnTotalOduBBE_Type()
)
jnxOtnTotalOduBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduBBE.setStatus("current")
_JnxOtnTotalOduES_Type = Unsigned32
_JnxOtnTotalOduES_Object = MibTableColumn
jnxOtnTotalOduES = _JnxOtnTotalOduES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 4),
    _JnxOtnTotalOduES_Type()
)
jnxOtnTotalOduES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduES.setStatus("current")
_JnxOtnTotalOduSES_Type = Unsigned32
_JnxOtnTotalOduSES_Object = MibTableColumn
jnxOtnTotalOduSES = _JnxOtnTotalOduSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 5),
    _JnxOtnTotalOduSES_Type()
)
jnxOtnTotalOduSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduSES.setStatus("current")
_JnxOtnTotalOduUAS_Type = Unsigned32
_JnxOtnTotalOduUAS_Object = MibTableColumn
jnxOtnTotalOduUAS = _JnxOtnTotalOduUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 6),
    _JnxOtnTotalOduUAS_Type()
)
jnxOtnTotalOduUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOduUAS.setStatus("current")
_JnxOtnCurrentOtu15minTable_Object = MibTable
jnxOtnCurrentOtu15minTable = _JnxOtnCurrentOtu15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minTable.setStatus("current")
_JnxOtnCurrentOtu15minEntry_Object = MibTableRow
jnxOtnCurrentOtu15minEntry = _JnxOtnCurrentOtu15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1)
)
jnxOtnCurrentOtu15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minEntry.setStatus("current")
_JnxOtnCurrentOtu15minBIP_Type = Unsigned32
_JnxOtnCurrentOtu15minBIP_Object = MibTableColumn
jnxOtnCurrentOtu15minBIP = _JnxOtnCurrentOtu15minBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 1),
    _JnxOtnCurrentOtu15minBIP_Type()
)
jnxOtnCurrentOtu15minBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minBIP.setStatus("current")
_JnxOtnCurrentOtu15minBBE_Type = Unsigned32
_JnxOtnCurrentOtu15minBBE_Object = MibTableColumn
jnxOtnCurrentOtu15minBBE = _JnxOtnCurrentOtu15minBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 2),
    _JnxOtnCurrentOtu15minBBE_Type()
)
jnxOtnCurrentOtu15minBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minBBE.setStatus("current")
_JnxOtnCurrentOtu15minES_Type = Unsigned32
_JnxOtnCurrentOtu15minES_Object = MibTableColumn
jnxOtnCurrentOtu15minES = _JnxOtnCurrentOtu15minES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 3),
    _JnxOtnCurrentOtu15minES_Type()
)
jnxOtnCurrentOtu15minES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minES.setStatus("current")
_JnxOtnCurrentOtu15minSES_Type = Unsigned32
_JnxOtnCurrentOtu15minSES_Object = MibTableColumn
jnxOtnCurrentOtu15minSES = _JnxOtnCurrentOtu15minSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 4),
    _JnxOtnCurrentOtu15minSES_Type()
)
jnxOtnCurrentOtu15minSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minSES.setStatus("current")
_JnxOtnCurrentOtu15minUAS_Type = Unsigned32
_JnxOtnCurrentOtu15minUAS_Object = MibTableColumn
jnxOtnCurrentOtu15minUAS = _JnxOtnCurrentOtu15minUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 5),
    _JnxOtnCurrentOtu15minUAS_Type()
)
jnxOtnCurrentOtu15minUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minUAS.setStatus("current")
_JnxOtnCurrentOtu15minElapsedTime_Type = Unsigned32
_JnxOtnCurrentOtu15minElapsedTime_Object = MibTableColumn
jnxOtnCurrentOtu15minElapsedTime = _JnxOtnCurrentOtu15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 6),
    _JnxOtnCurrentOtu15minElapsedTime_Type()
)
jnxOtnCurrentOtu15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtu15minElapsedTime.setStatus("current")
_JnxOtnIntervalOtu15minTable_Object = MibTable
jnxOtnIntervalOtu15minTable = _JnxOtnIntervalOtu15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minTable.setStatus("current")
_JnxOtnIntervalOtu15minEntry_Object = MibTableRow
jnxOtnIntervalOtu15minEntry = _JnxOtnIntervalOtu15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1)
)
jnxOtnIntervalOtu15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOtu15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minEntry.setStatus("current")


class _JnxOtnIntervalOtu15minIntervalNumber_Type(Integer32):
    """Custom type jnxOtnIntervalOtu15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOtnIntervalOtu15minIntervalNumber_Type.__name__ = "Integer32"
_JnxOtnIntervalOtu15minIntervalNumber_Object = MibTableColumn
jnxOtnIntervalOtu15minIntervalNumber = _JnxOtnIntervalOtu15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 1),
    _JnxOtnIntervalOtu15minIntervalNumber_Type()
)
jnxOtnIntervalOtu15minIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minIntervalNumber.setStatus("current")
_JnxOtnIntervalOtu15minBIP_Type = Unsigned32
_JnxOtnIntervalOtu15minBIP_Object = MibTableColumn
jnxOtnIntervalOtu15minBIP = _JnxOtnIntervalOtu15minBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 2),
    _JnxOtnIntervalOtu15minBIP_Type()
)
jnxOtnIntervalOtu15minBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minBIP.setStatus("current")
_JnxOtnIntervalOtu15minBBE_Type = Unsigned32
_JnxOtnIntervalOtu15minBBE_Object = MibTableColumn
jnxOtnIntervalOtu15minBBE = _JnxOtnIntervalOtu15minBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 3),
    _JnxOtnIntervalOtu15minBBE_Type()
)
jnxOtnIntervalOtu15minBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minBBE.setStatus("current")
_JnxOtnIntervalOtu15minES_Type = Unsigned32
_JnxOtnIntervalOtu15minES_Object = MibTableColumn
jnxOtnIntervalOtu15minES = _JnxOtnIntervalOtu15minES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 4),
    _JnxOtnIntervalOtu15minES_Type()
)
jnxOtnIntervalOtu15minES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minES.setStatus("current")
_JnxOtnIntervalOtu15minSES_Type = Unsigned32
_JnxOtnIntervalOtu15minSES_Object = MibTableColumn
jnxOtnIntervalOtu15minSES = _JnxOtnIntervalOtu15minSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 5),
    _JnxOtnIntervalOtu15minSES_Type()
)
jnxOtnIntervalOtu15minSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minSES.setStatus("current")
_JnxOtnIntervalOtu15minUAS_Type = Unsigned32
_JnxOtnIntervalOtu15minUAS_Object = MibTableColumn
jnxOtnIntervalOtu15minUAS = _JnxOtnIntervalOtu15minUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 6),
    _JnxOtnIntervalOtu15minUAS_Type()
)
jnxOtnIntervalOtu15minUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minUAS.setStatus("current")
_JnxOtnIntervalOtu15minInvalidData_Type = Unsigned32
_JnxOtnIntervalOtu15minInvalidData_Object = MibTableColumn
jnxOtnIntervalOtu15minInvalidData = _JnxOtnIntervalOtu15minInvalidData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 7),
    _JnxOtnIntervalOtu15minInvalidData_Type()
)
jnxOtnIntervalOtu15minInvalidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minInvalidData.setStatus("current")
_JnxOtnIntervalOtu15minTimeStamp_Type = DateAndTime
_JnxOtnIntervalOtu15minTimeStamp_Object = MibTableColumn
jnxOtnIntervalOtu15minTimeStamp = _JnxOtnIntervalOtu15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 8),
    _JnxOtnIntervalOtu15minTimeStamp_Type()
)
jnxOtnIntervalOtu15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtu15minTimeStamp.setStatus("current")
_JnxOtnTotalOtuTable_Object = MibTable
jnxOtnTotalOtuTable = _JnxOtnTotalOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6)
)
if mibBuilder.loadTexts:
    jnxOtnTotalOtuTable.setStatus("current")
_JnxOtnTotalOtuEntry_Object = MibTableRow
jnxOtnTotalOtuEntry = _JnxOtnTotalOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1)
)
jnxOtnTotalOtuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnTotalOtuEntry.setStatus("current")
_JnxOtnTotalOtuDayNumber_Type = Integer32
_JnxOtnTotalOtuDayNumber_Object = MibTableColumn
jnxOtnTotalOtuDayNumber = _JnxOtnTotalOtuDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 1),
    _JnxOtnTotalOtuDayNumber_Type()
)
jnxOtnTotalOtuDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuDayNumber.setStatus("current")
_JnxOtnTotalOtuBIP_Type = Unsigned32
_JnxOtnTotalOtuBIP_Object = MibTableColumn
jnxOtnTotalOtuBIP = _JnxOtnTotalOtuBIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 2),
    _JnxOtnTotalOtuBIP_Type()
)
jnxOtnTotalOtuBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuBIP.setStatus("current")
_JnxOtnTotalOtuBBE_Type = Unsigned32
_JnxOtnTotalOtuBBE_Object = MibTableColumn
jnxOtnTotalOtuBBE = _JnxOtnTotalOtuBBE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 3),
    _JnxOtnTotalOtuBBE_Type()
)
jnxOtnTotalOtuBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuBBE.setStatus("current")
_JnxOtnTotalOtuES_Type = Unsigned32
_JnxOtnTotalOtuES_Object = MibTableColumn
jnxOtnTotalOtuES = _JnxOtnTotalOtuES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 4),
    _JnxOtnTotalOtuES_Type()
)
jnxOtnTotalOtuES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuES.setStatus("current")
_JnxOtnTotalOtuSES_Type = Unsigned32
_JnxOtnTotalOtuSES_Object = MibTableColumn
jnxOtnTotalOtuSES = _JnxOtnTotalOtuSES_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 5),
    _JnxOtnTotalOtuSES_Type()
)
jnxOtnTotalOtuSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuSES.setStatus("current")
_JnxOtnTotalOtuUAS_Type = Unsigned32
_JnxOtnTotalOtuUAS_Object = MibTableColumn
jnxOtnTotalOtuUAS = _JnxOtnTotalOtuUAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 6),
    _JnxOtnTotalOtuUAS_Type()
)
jnxOtnTotalOtuUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuUAS.setStatus("current")
_JnxOtnCurrentOtuFec15minTable_Object = MibTable
jnxOtnCurrentOtuFec15minTable = _JnxOtnCurrentOtuFec15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7)
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minTable.setStatus("current")
_JnxOtnCurrentOtuFec15minEntry_Object = MibTableRow
jnxOtnCurrentOtuFec15minEntry = _JnxOtnCurrentOtuFec15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1)
)
jnxOtnCurrentOtuFec15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minEntry.setStatus("current")
_JnxOtnCurrentOtuFec15minCorrectedErrors_Type = Unsigned32
_JnxOtnCurrentOtuFec15minCorrectedErrors_Object = MibTableColumn
jnxOtnCurrentOtuFec15minCorrectedErrors = _JnxOtnCurrentOtuFec15minCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 1),
    _JnxOtnCurrentOtuFec15minCorrectedErrors_Type()
)
jnxOtnCurrentOtuFec15minCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minCorrectedErrors.setStatus("current")
_JnxOtnCurrentOtuFec15minCorrectedErrorRatioX_Type = Unsigned32
_JnxOtnCurrentOtuFec15minCorrectedErrorRatioX_Object = MibTableColumn
jnxOtnCurrentOtuFec15minCorrectedErrorRatioX = _JnxOtnCurrentOtuFec15minCorrectedErrorRatioX_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 2),
    _JnxOtnCurrentOtuFec15minCorrectedErrorRatioX_Type()
)
jnxOtnCurrentOtuFec15minCorrectedErrorRatioX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minCorrectedErrorRatioX.setStatus("current")
_JnxOtnCurrentOtuFec15minCorrectedErrorRatioY_Type = Unsigned32
_JnxOtnCurrentOtuFec15minCorrectedErrorRatioY_Object = MibTableColumn
jnxOtnCurrentOtuFec15minCorrectedErrorRatioY = _JnxOtnCurrentOtuFec15minCorrectedErrorRatioY_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 3),
    _JnxOtnCurrentOtuFec15minCorrectedErrorRatioY_Type()
)
jnxOtnCurrentOtuFec15minCorrectedErrorRatioY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minCorrectedErrorRatioY.setStatus("current")
_JnxOtnCurrentOtuFec15minUncorrectedWords_Type = Unsigned32
_JnxOtnCurrentOtuFec15minUncorrectedWords_Object = MibTableColumn
jnxOtnCurrentOtuFec15minUncorrectedWords = _JnxOtnCurrentOtuFec15minUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 4),
    _JnxOtnCurrentOtuFec15minUncorrectedWords_Type()
)
jnxOtnCurrentOtuFec15minUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minUncorrectedWords.setStatus("current")
_JnxOtnCurrentOtuFec15minElapsedTime_Type = Unsigned32
_JnxOtnCurrentOtuFec15minElapsedTime_Object = MibTableColumn
jnxOtnCurrentOtuFec15minElapsedTime = _JnxOtnCurrentOtuFec15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 5),
    _JnxOtnCurrentOtuFec15minElapsedTime_Type()
)
jnxOtnCurrentOtuFec15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnCurrentOtuFec15minElapsedTime.setStatus("current")
_JnxOtnIntervalOtuFec15minTable_Object = MibTable
jnxOtnIntervalOtuFec15minTable = _JnxOtnIntervalOtuFec15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8)
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minTable.setStatus("current")
_JnxOtnIntervalOtuFec15minEntry_Object = MibTableRow
jnxOtnIntervalOtuFec15minEntry = _JnxOtnIntervalOtuFec15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1)
)
jnxOtnIntervalOtuFec15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOtuFec15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minEntry.setStatus("current")


class _JnxOtnIntervalOtuFec15minIntervalNumber_Type(Integer32):
    """Custom type jnxOtnIntervalOtuFec15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOtnIntervalOtuFec15minIntervalNumber_Type.__name__ = "Integer32"
_JnxOtnIntervalOtuFec15minIntervalNumber_Object = MibTableColumn
jnxOtnIntervalOtuFec15minIntervalNumber = _JnxOtnIntervalOtuFec15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 1),
    _JnxOtnIntervalOtuFec15minIntervalNumber_Type()
)
jnxOtnIntervalOtuFec15minIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minIntervalNumber.setStatus("current")
_JnxOtnIntervalOtuFec15minCorrectedErrors_Type = Unsigned32
_JnxOtnIntervalOtuFec15minCorrectedErrors_Object = MibTableColumn
jnxOtnIntervalOtuFec15minCorrectedErrors = _JnxOtnIntervalOtuFec15minCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 2),
    _JnxOtnIntervalOtuFec15minCorrectedErrors_Type()
)
jnxOtnIntervalOtuFec15minCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minCorrectedErrors.setStatus("current")
_JnxOtnIntervalOtuFec15minCorrectedErrorRatioX_Type = Unsigned32
_JnxOtnIntervalOtuFec15minCorrectedErrorRatioX_Object = MibTableColumn
jnxOtnIntervalOtuFec15minCorrectedErrorRatioX = _JnxOtnIntervalOtuFec15minCorrectedErrorRatioX_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 3),
    _JnxOtnIntervalOtuFec15minCorrectedErrorRatioX_Type()
)
jnxOtnIntervalOtuFec15minCorrectedErrorRatioX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minCorrectedErrorRatioX.setStatus("current")
_JnxOtnIntervalOtuFec15minCorrectedErrorRatioY_Type = Unsigned32
_JnxOtnIntervalOtuFec15minCorrectedErrorRatioY_Object = MibTableColumn
jnxOtnIntervalOtuFec15minCorrectedErrorRatioY = _JnxOtnIntervalOtuFec15minCorrectedErrorRatioY_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 4),
    _JnxOtnIntervalOtuFec15minCorrectedErrorRatioY_Type()
)
jnxOtnIntervalOtuFec15minCorrectedErrorRatioY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minCorrectedErrorRatioY.setStatus("current")
_JnxOtnIntervalOtuFec15minUncorrectedWords_Type = Unsigned32
_JnxOtnIntervalOtuFec15minUncorrectedWords_Object = MibTableColumn
jnxOtnIntervalOtuFec15minUncorrectedWords = _JnxOtnIntervalOtuFec15minUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 5),
    _JnxOtnIntervalOtuFec15minUncorrectedWords_Type()
)
jnxOtnIntervalOtuFec15minUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minUncorrectedWords.setStatus("current")
_JnxOtnIntervalOtuFec15minTimeStamp_Type = DateAndTime
_JnxOtnIntervalOtuFec15minTimeStamp_Object = MibTableColumn
jnxOtnIntervalOtuFec15minTimeStamp = _JnxOtnIntervalOtuFec15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 6),
    _JnxOtnIntervalOtuFec15minTimeStamp_Type()
)
jnxOtnIntervalOtuFec15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnIntervalOtuFec15minTimeStamp.setStatus("current")
_JnxOtnTotalOtuFecTable_Object = MibTable
jnxOtnTotalOtuFecTable = _JnxOtnTotalOtuFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9)
)
if mibBuilder.loadTexts:
    jnxOtnTotalOtuFecTable.setStatus("current")
_JnxOtnTotalOtuFecEntry_Object = MibTableRow
jnxOtnTotalOtuFecEntry = _JnxOtnTotalOtuFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1)
)
jnxOtnTotalOtuFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnTotalOtuFecEntry.setStatus("current")


class _JnxOtnTotalOtuFecDayNumber_Type(Integer32):
    """Custom type jnxOtnTotalOtuFecDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOtnTotalOtuFecDayNumber_Type.__name__ = "Integer32"
_JnxOtnTotalOtuFecDayNumber_Object = MibTableColumn
jnxOtnTotalOtuFecDayNumber = _JnxOtnTotalOtuFecDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 1),
    _JnxOtnTotalOtuFecDayNumber_Type()
)
jnxOtnTotalOtuFecDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuFecDayNumber.setStatus("current")
_JnxOtnTotalOtuFecCorrectedErrors_Type = Unsigned32
_JnxOtnTotalOtuFecCorrectedErrors_Object = MibTableColumn
jnxOtnTotalOtuFecCorrectedErrors = _JnxOtnTotalOtuFecCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 2),
    _JnxOtnTotalOtuFecCorrectedErrors_Type()
)
jnxOtnTotalOtuFecCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuFecCorrectedErrors.setStatus("current")
_JnxOtnTotalOtuFecUncorrectedWords_Type = Unsigned32
_JnxOtnTotalOtuFecUncorrectedWords_Object = MibTableColumn
jnxOtnTotalOtuFecUncorrectedWords = _JnxOtnTotalOtuFecUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 3),
    _JnxOtnTotalOtuFecUncorrectedWords_Type()
)
jnxOtnTotalOtuFecUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOtnTotalOtuFecUncorrectedWords.setStatus("current")
_JnxOtnNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxOtnNotificationPrefix = _JnxOtnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 15, 0)
)

# Managed Objects groups


# Notification objects

jnxOtnAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 15, 0, 1)
)
jnxOtnAlarmSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmId"),
        ("JUNIPER-OTN-MIB", "jnxOtnCurrentAlarms"),
        ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxOtnAlarmSet.setStatus(
        "current"
    )

jnxOtnAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 15, 0, 2)
)
jnxOtnAlarmCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmId"),
        ("JUNIPER-OTN-MIB", "jnxOtnCurrentAlarms"),
        ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxOtnAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-OTN-MIB",
    **{"JnxOtnAlarmId": JnxOtnAlarmId,
       "jnxOtnMib": jnxOtnMib,
       "jnxOtnAlarms": jnxOtnAlarms,
       "jnxOtnAlarmTable": jnxOtnAlarmTable,
       "jnxOtnAlarmEntry": jnxOtnAlarmEntry,
       "jnxOtnCurrentAlarms": jnxOtnCurrentAlarms,
       "jnxOtnLastAlarmId": jnxOtnLastAlarmId,
       "jnxOtnLastAlarmTime": jnxOtnLastAlarmTime,
       "jnxOtnLastAlarmDate": jnxOtnLastAlarmDate,
       "jnxOtnLastAlarmEvent": jnxOtnLastAlarmEvent,
       "jnxOtnPerformanceMonitoring": jnxOtnPerformanceMonitoring,
       "jnxOtnCurrentOdu15minTable": jnxOtnCurrentOdu15minTable,
       "jnxOtnCurrentOdu15minEntry": jnxOtnCurrentOdu15minEntry,
       "jnxOtnCurrentOdu15minBIP": jnxOtnCurrentOdu15minBIP,
       "jnxOtnCurrentOdu15minBBE": jnxOtnCurrentOdu15minBBE,
       "jnxOtnCurrentOdu15minES": jnxOtnCurrentOdu15minES,
       "jnxOtnCurrentOdu15minSES": jnxOtnCurrentOdu15minSES,
       "jnxOtnCurrentOdu15minUAS": jnxOtnCurrentOdu15minUAS,
       "jnxOtnCurrentOdu15minElapsedTime": jnxOtnCurrentOdu15minElapsedTime,
       "jnxOtnIntervalOdu15minTable": jnxOtnIntervalOdu15minTable,
       "jnxOtnIntervalOdu15minEntry": jnxOtnIntervalOdu15minEntry,
       "jnxOtnIntervalOdu15minIntervalNumber": jnxOtnIntervalOdu15minIntervalNumber,
       "jnxOtnIntervalOdu15minBIP": jnxOtnIntervalOdu15minBIP,
       "jnxOtnIntervalOdu15minBBE": jnxOtnIntervalOdu15minBBE,
       "jnxOtnIntervalOdu15minES": jnxOtnIntervalOdu15minES,
       "jnxOtnIntervalOdu15minSES": jnxOtnIntervalOdu15minSES,
       "jnxOtnIntervalOdu15minUAS": jnxOtnIntervalOdu15minUAS,
       "jnxOtnIntervalOdu15minInvalidData": jnxOtnIntervalOdu15minInvalidData,
       "jnxOtnIntervalODdu15minTimeStamp": jnxOtnIntervalODdu15minTimeStamp,
       "jnxOtnTotalOduTable": jnxOtnTotalOduTable,
       "jnxOtnTotalOduEntry": jnxOtnTotalOduEntry,
       "jnxOtnTotalOduDayNumber": jnxOtnTotalOduDayNumber,
       "jnxOtnTotalOduBIP": jnxOtnTotalOduBIP,
       "jnxOtnTotalOduBBE": jnxOtnTotalOduBBE,
       "jnxOtnTotalOduES": jnxOtnTotalOduES,
       "jnxOtnTotalOduSES": jnxOtnTotalOduSES,
       "jnxOtnTotalOduUAS": jnxOtnTotalOduUAS,
       "jnxOtnCurrentOtu15minTable": jnxOtnCurrentOtu15minTable,
       "jnxOtnCurrentOtu15minEntry": jnxOtnCurrentOtu15minEntry,
       "jnxOtnCurrentOtu15minBIP": jnxOtnCurrentOtu15minBIP,
       "jnxOtnCurrentOtu15minBBE": jnxOtnCurrentOtu15minBBE,
       "jnxOtnCurrentOtu15minES": jnxOtnCurrentOtu15minES,
       "jnxOtnCurrentOtu15minSES": jnxOtnCurrentOtu15minSES,
       "jnxOtnCurrentOtu15minUAS": jnxOtnCurrentOtu15minUAS,
       "jnxOtnCurrentOtu15minElapsedTime": jnxOtnCurrentOtu15minElapsedTime,
       "jnxOtnIntervalOtu15minTable": jnxOtnIntervalOtu15minTable,
       "jnxOtnIntervalOtu15minEntry": jnxOtnIntervalOtu15minEntry,
       "jnxOtnIntervalOtu15minIntervalNumber": jnxOtnIntervalOtu15minIntervalNumber,
       "jnxOtnIntervalOtu15minBIP": jnxOtnIntervalOtu15minBIP,
       "jnxOtnIntervalOtu15minBBE": jnxOtnIntervalOtu15minBBE,
       "jnxOtnIntervalOtu15minES": jnxOtnIntervalOtu15minES,
       "jnxOtnIntervalOtu15minSES": jnxOtnIntervalOtu15minSES,
       "jnxOtnIntervalOtu15minUAS": jnxOtnIntervalOtu15minUAS,
       "jnxOtnIntervalOtu15minInvalidData": jnxOtnIntervalOtu15minInvalidData,
       "jnxOtnIntervalOtu15minTimeStamp": jnxOtnIntervalOtu15minTimeStamp,
       "jnxOtnTotalOtuTable": jnxOtnTotalOtuTable,
       "jnxOtnTotalOtuEntry": jnxOtnTotalOtuEntry,
       "jnxOtnTotalOtuDayNumber": jnxOtnTotalOtuDayNumber,
       "jnxOtnTotalOtuBIP": jnxOtnTotalOtuBIP,
       "jnxOtnTotalOtuBBE": jnxOtnTotalOtuBBE,
       "jnxOtnTotalOtuES": jnxOtnTotalOtuES,
       "jnxOtnTotalOtuSES": jnxOtnTotalOtuSES,
       "jnxOtnTotalOtuUAS": jnxOtnTotalOtuUAS,
       "jnxOtnCurrentOtuFec15minTable": jnxOtnCurrentOtuFec15minTable,
       "jnxOtnCurrentOtuFec15minEntry": jnxOtnCurrentOtuFec15minEntry,
       "jnxOtnCurrentOtuFec15minCorrectedErrors": jnxOtnCurrentOtuFec15minCorrectedErrors,
       "jnxOtnCurrentOtuFec15minCorrectedErrorRatioX": jnxOtnCurrentOtuFec15minCorrectedErrorRatioX,
       "jnxOtnCurrentOtuFec15minCorrectedErrorRatioY": jnxOtnCurrentOtuFec15minCorrectedErrorRatioY,
       "jnxOtnCurrentOtuFec15minUncorrectedWords": jnxOtnCurrentOtuFec15minUncorrectedWords,
       "jnxOtnCurrentOtuFec15minElapsedTime": jnxOtnCurrentOtuFec15minElapsedTime,
       "jnxOtnIntervalOtuFec15minTable": jnxOtnIntervalOtuFec15minTable,
       "jnxOtnIntervalOtuFec15minEntry": jnxOtnIntervalOtuFec15minEntry,
       "jnxOtnIntervalOtuFec15minIntervalNumber": jnxOtnIntervalOtuFec15minIntervalNumber,
       "jnxOtnIntervalOtuFec15minCorrectedErrors": jnxOtnIntervalOtuFec15minCorrectedErrors,
       "jnxOtnIntervalOtuFec15minCorrectedErrorRatioX": jnxOtnIntervalOtuFec15minCorrectedErrorRatioX,
       "jnxOtnIntervalOtuFec15minCorrectedErrorRatioY": jnxOtnIntervalOtuFec15minCorrectedErrorRatioY,
       "jnxOtnIntervalOtuFec15minUncorrectedWords": jnxOtnIntervalOtuFec15minUncorrectedWords,
       "jnxOtnIntervalOtuFec15minTimeStamp": jnxOtnIntervalOtuFec15minTimeStamp,
       "jnxOtnTotalOtuFecTable": jnxOtnTotalOtuFecTable,
       "jnxOtnTotalOtuFecEntry": jnxOtnTotalOtuFecEntry,
       "jnxOtnTotalOtuFecDayNumber": jnxOtnTotalOtuFecDayNumber,
       "jnxOtnTotalOtuFecCorrectedErrors": jnxOtnTotalOtuFecCorrectedErrors,
       "jnxOtnTotalOtuFecUncorrectedWords": jnxOtnTotalOtuFecUncorrectedWords,
       "jnxOtnNotificationPrefix": jnxOtnNotificationPrefix,
       "jnxOtnAlarmSet": jnxOtnAlarmSet,
       "jnxOtnAlarmCleared": jnxOtnAlarmCleared}
)
