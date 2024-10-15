# SNMP MIB module (CISCO-DMN-DSG-REMINDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-REMINDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:31 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGReminder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30)
)
ciscoDSGReminder.setRevisions(
        ("2010-08-30 11:00",
         "2010-06-17 06:00",
         "2010-04-12 06:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ReminderTable_ObjectIdentity = ObjectIdentity
reminderTable = _ReminderTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2)
)
_ReminderTimerTable_Object = MibTable
reminderTimerTable = _ReminderTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1)
)
if mibBuilder.loadTexts:
    reminderTimerTable.setStatus("current")
_ReminderTimerEntry_Object = MibTableRow
reminderTimerEntry = _ReminderTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1)
)
reminderTimerEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-REMINDER-MIB", "reminderTimerID"),
)
if mibBuilder.loadTexts:
    reminderTimerEntry.setStatus("current")


class _ReminderTimerID_Type(Integer32):
    """Custom type reminderTimerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ReminderTimerID_Type.__name__ = "Integer32"
_ReminderTimerID_Object = MibTableColumn
reminderTimerID = _ReminderTimerID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 1),
    _ReminderTimerID_Type()
)
reminderTimerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reminderTimerID.setStatus("current")


class _ReminderTimerChType_Type(Integer32):
    """Custom type reminderTimerChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("radio", 2),
          ("tv", 1))
    )


_ReminderTimerChType_Type.__name__ = "Integer32"
_ReminderTimerChType_Object = MibTableColumn
reminderTimerChType = _ReminderTimerChType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 2),
    _ReminderTimerChType_Type()
)
reminderTimerChType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerChType.setStatus("current")


class _ReminderTimerChNum_Type(Integer32):
    """Custom type reminderTimerChNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReminderTimerChNum_Type.__name__ = "Integer32"
_ReminderTimerChNum_Object = MibTableColumn
reminderTimerChNum = _ReminderTimerChNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 3),
    _ReminderTimerChNum_Type()
)
reminderTimerChNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerChNum.setStatus("current")


class _ReminderTimerChName_Type(DisplayString):
    """Custom type reminderTimerChName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReminderTimerChName_Type.__name__ = "DisplayString"
_ReminderTimerChName_Object = MibTableColumn
reminderTimerChName = _ReminderTimerChName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 4),
    _ReminderTimerChName_Type()
)
reminderTimerChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerChName.setStatus("current")


class _ReminderTimerEvtName_Type(DisplayString):
    """Custom type reminderTimerEvtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReminderTimerEvtName_Type.__name__ = "DisplayString"
_ReminderTimerEvtName_Object = MibTableColumn
reminderTimerEvtName = _ReminderTimerEvtName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 5),
    _ReminderTimerEvtName_Type()
)
reminderTimerEvtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerEvtName.setStatus("current")


class _ReminderTimerDay_Type(Integer32):
    """Custom type reminderTimerDay based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_ReminderTimerDay_Type.__name__ = "Integer32"
_ReminderTimerDay_Object = MibTableColumn
reminderTimerDay = _ReminderTimerDay_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 6),
    _ReminderTimerDay_Type()
)
reminderTimerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerDay.setStatus("current")


class _ReminderTimerStartTime_Type(DisplayString):
    """Custom type reminderTimerStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReminderTimerStartTime_Type.__name__ = "DisplayString"
_ReminderTimerStartTime_Object = MibTableColumn
reminderTimerStartTime = _ReminderTimerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 7),
    _ReminderTimerStartTime_Type()
)
reminderTimerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerStartTime.setStatus("current")


class _ReminderTimerEndTime_Type(DisplayString):
    """Custom type reminderTimerEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReminderTimerEndTime_Type.__name__ = "DisplayString"
_ReminderTimerEndTime_Object = MibTableColumn
reminderTimerEndTime = _ReminderTimerEndTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 8),
    _ReminderTimerEndTime_Type()
)
reminderTimerEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerEndTime.setStatus("current")


class _ReminderTimerEvtParentalRating_Type(Integer32):
    """Custom type reminderTimerEvtParentalRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ReminderTimerEvtParentalRating_Type.__name__ = "Integer32"
_ReminderTimerEvtParentalRating_Object = MibTableColumn
reminderTimerEvtParentalRating = _ReminderTimerEvtParentalRating_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 9),
    _ReminderTimerEvtParentalRating_Type()
)
reminderTimerEvtParentalRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerEvtParentalRating.setStatus("current")


class _ReminderTimerFrequency_Type(Integer32):
    """Custom type reminderTimerFrequency based on Integer32"""
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
        *(("daily", 2),
          ("once", 1),
          ("weekDays", 4),
          ("weekly", 3))
    )


_ReminderTimerFrequency_Type.__name__ = "Integer32"
_ReminderTimerFrequency_Object = MibTableColumn
reminderTimerFrequency = _ReminderTimerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 10),
    _ReminderTimerFrequency_Type()
)
reminderTimerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerFrequency.setStatus("current")
_ReminderTimerRowStatus_Type = RowStatus
_ReminderTimerRowStatus_Object = MibTableColumn
reminderTimerRowStatus = _ReminderTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 11),
    _ReminderTimerRowStatus_Type()
)
reminderTimerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reminderTimerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-REMINDER-MIB",
    **{"ciscoDSGReminder": ciscoDSGReminder,
       "reminderTable": reminderTable,
       "reminderTimerTable": reminderTimerTable,
       "reminderTimerEntry": reminderTimerEntry,
       "reminderTimerID": reminderTimerID,
       "reminderTimerChType": reminderTimerChType,
       "reminderTimerChNum": reminderTimerChNum,
       "reminderTimerChName": reminderTimerChName,
       "reminderTimerEvtName": reminderTimerEvtName,
       "reminderTimerDay": reminderTimerDay,
       "reminderTimerStartTime": reminderTimerStartTime,
       "reminderTimerEndTime": reminderTimerEndTime,
       "reminderTimerEvtParentalRating": reminderTimerEvtParentalRating,
       "reminderTimerFrequency": reminderTimerFrequency,
       "reminderTimerRowStatus": reminderTimerRowStatus}
)
