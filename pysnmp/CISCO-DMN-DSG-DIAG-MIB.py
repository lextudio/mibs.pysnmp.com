# SNMP MIB module (CISCO-DMN-DSG-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGDiag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18)
)
ciscoDSGDiag.setRevisions(
        ("2012-03-20 08:00",
         "2010-10-13 08:00",
         "2010-08-03 10:00",
         "2010-04-12 09:00",
         "2010-02-12 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PowerOn_ObjectIdentity = ObjectIdentity
powerOn = _PowerOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1)
)


class _PowerOnCreationDate_Type(DisplayString):
    """Custom type powerOnCreationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PowerOnCreationDate_Type.__name__ = "DisplayString"
_PowerOnCreationDate_Object = MibScalar
powerOnCreationDate = _PowerOnCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 1),
    _PowerOnCreationDate_Type()
)
powerOnCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnCreationDate.setStatus("current")


class _PowerOnDate_Type(DisplayString):
    """Custom type powerOnDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PowerOnDate_Type.__name__ = "DisplayString"
_PowerOnDate_Object = MibScalar
powerOnDate = _PowerOnDate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 2),
    _PowerOnDate_Type()
)
powerOnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnDate.setStatus("current")


class _PowerOnTotalHours_Type(DisplayString):
    """Custom type powerOnTotalHours based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnTotalHours_Type.__name__ = "DisplayString"
_PowerOnTotalHours_Object = MibScalar
powerOnTotalHours = _PowerOnTotalHours_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 3),
    _PowerOnTotalHours_Type()
)
powerOnTotalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnTotalHours.setStatus("current")


class _PowerOnHrsSinceLastPowerOff_Type(DisplayString):
    """Custom type powerOnHrsSinceLastPowerOff based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnHrsSinceLastPowerOff_Type.__name__ = "DisplayString"
_PowerOnHrsSinceLastPowerOff_Object = MibScalar
powerOnHrsSinceLastPowerOff = _PowerOnHrsSinceLastPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 4),
    _PowerOnHrsSinceLastPowerOff_Type()
)
powerOnHrsSinceLastPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnHrsSinceLastPowerOff.setStatus("current")


class _PowerOnTotResetCount_Type(DisplayString):
    """Custom type powerOnTotResetCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnTotResetCount_Type.__name__ = "DisplayString"
_PowerOnTotResetCount_Object = MibScalar
powerOnTotResetCount = _PowerOnTotResetCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 5),
    _PowerOnTotResetCount_Type()
)
powerOnTotResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnTotResetCount.setStatus("current")


class _PowerOnClrableResetCount_Type(DisplayString):
    """Custom type powerOnClrableResetCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnClrableResetCount_Type.__name__ = "DisplayString"
_PowerOnClrableResetCount_Object = MibScalar
powerOnClrableResetCount = _PowerOnClrableResetCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 6),
    _PowerOnClrableResetCount_Type()
)
powerOnClrableResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnClrableResetCount.setStatus("current")


class _PowerOnReasonLastReset_Type(DisplayString):
    """Custom type powerOnReasonLastReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PowerOnReasonLastReset_Type.__name__ = "DisplayString"
_PowerOnReasonLastReset_Object = MibScalar
powerOnReasonLastReset = _PowerOnReasonLastReset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 7),
    _PowerOnReasonLastReset_Type()
)
powerOnReasonLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnReasonLastReset.setStatus("current")


class _PowerOnClearResetCounter_Type(Integer32):
    """Custom type powerOnClearResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_PowerOnClearResetCounter_Type.__name__ = "Integer32"
_PowerOnClearResetCounter_Object = MibScalar
powerOnClearResetCounter = _PowerOnClearResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 8),
    _PowerOnClearResetCounter_Type()
)
powerOnClearResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerOnClearResetCounter.setStatus("current")


class _PowerOnFactoryResetCount_Type(DisplayString):
    """Custom type powerOnFactoryResetCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnFactoryResetCount_Type.__name__ = "DisplayString"
_PowerOnFactoryResetCount_Object = MibScalar
powerOnFactoryResetCount = _PowerOnFactoryResetCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 9),
    _PowerOnFactoryResetCount_Type()
)
powerOnFactoryResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnFactoryResetCount.setStatus("current")


class _PowerOnCurrentDateTime_Type(DisplayString):
    """Custom type powerOnCurrentDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerOnCurrentDateTime_Type.__name__ = "DisplayString"
_PowerOnCurrentDateTime_Object = MibScalar
powerOnCurrentDateTime = _PowerOnCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 1, 10),
    _PowerOnCurrentDateTime_Type()
)
powerOnCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnCurrentDateTime.setStatus("current")
_DiagTable_ObjectIdentity = ObjectIdentity
diagTable = _DiagTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2)
)
_DiagHealthMonitorTable_Object = MibTable
diagHealthMonitorTable = _DiagHealthMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 1)
)
if mibBuilder.loadTexts:
    diagHealthMonitorTable.setStatus("current")
_DiagHealthMonitorEntry_Object = MibTableRow
diagHealthMonitorEntry = _DiagHealthMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 1, 1)
)
diagHealthMonitorEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DIAG-MIB", "diagHealthMonitorIndex"),
)
if mibBuilder.loadTexts:
    diagHealthMonitorEntry.setStatus("current")


class _DiagHealthMonitorIndex_Type(Integer32):
    """Custom type diagHealthMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DiagHealthMonitorIndex_Type.__name__ = "Integer32"
_DiagHealthMonitorIndex_Object = MibTableColumn
diagHealthMonitorIndex = _DiagHealthMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 1, 1, 1),
    _DiagHealthMonitorIndex_Type()
)
diagHealthMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diagHealthMonitorIndex.setStatus("current")


class _DiagHealthMonitorName_Type(DisplayString):
    """Custom type diagHealthMonitorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DiagHealthMonitorName_Type.__name__ = "DisplayString"
_DiagHealthMonitorName_Object = MibTableColumn
diagHealthMonitorName = _DiagHealthMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 1, 1, 2),
    _DiagHealthMonitorName_Type()
)
diagHealthMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagHealthMonitorName.setStatus("current")


class _DiagHealthMonitorValue_Type(DisplayString):
    """Custom type diagHealthMonitorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DiagHealthMonitorValue_Type.__name__ = "DisplayString"
_DiagHealthMonitorValue_Object = MibTableColumn
diagHealthMonitorValue = _DiagHealthMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 1, 1, 3),
    _DiagHealthMonitorValue_Type()
)
diagHealthMonitorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagHealthMonitorValue.setStatus("current")
_DiagFanRPMTable_Object = MibTable
diagFanRPMTable = _DiagFanRPMTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 2)
)
if mibBuilder.loadTexts:
    diagFanRPMTable.setStatus("current")
_DiagFanRPMEntry_Object = MibTableRow
diagFanRPMEntry = _DiagFanRPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 2, 1)
)
diagFanRPMEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DIAG-MIB", "diagFanRPMIndex"),
)
if mibBuilder.loadTexts:
    diagFanRPMEntry.setStatus("current")


class _DiagFanRPMIndex_Type(Integer32):
    """Custom type diagFanRPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiagFanRPMIndex_Type.__name__ = "Integer32"
_DiagFanRPMIndex_Object = MibTableColumn
diagFanRPMIndex = _DiagFanRPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 2, 1, 1),
    _DiagFanRPMIndex_Type()
)
diagFanRPMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diagFanRPMIndex.setStatus("current")


class _DiagFanRPMName_Type(DisplayString):
    """Custom type diagFanRPMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DiagFanRPMName_Type.__name__ = "DisplayString"
_DiagFanRPMName_Object = MibTableColumn
diagFanRPMName = _DiagFanRPMName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 2, 1, 2),
    _DiagFanRPMName_Type()
)
diagFanRPMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagFanRPMName.setStatus("current")


class _DiagFanRPMValue_Type(DisplayString):
    """Custom type diagFanRPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DiagFanRPMValue_Type.__name__ = "DisplayString"
_DiagFanRPMValue_Object = MibTableColumn
diagFanRPMValue = _DiagFanRPMValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 2, 1, 3),
    _DiagFanRPMValue_Type()
)
diagFanRPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagFanRPMValue.setStatus("current")
_DiagECCReadingsTable_Object = MibTable
diagECCReadingsTable = _DiagECCReadingsTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3)
)
if mibBuilder.loadTexts:
    diagECCReadingsTable.setStatus("current")
_DiagECCReadingsEntry_Object = MibTableRow
diagECCReadingsEntry = _DiagECCReadingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1)
)
diagECCReadingsEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DIAG-MIB", "diagECCReadingsIndex"),
)
if mibBuilder.loadTexts:
    diagECCReadingsEntry.setStatus("current")


class _DiagECCReadingsIndex_Type(Integer32):
    """Custom type diagECCReadingsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DiagECCReadingsIndex_Type.__name__ = "Integer32"
_DiagECCReadingsIndex_Object = MibTableColumn
diagECCReadingsIndex = _DiagECCReadingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1, 1),
    _DiagECCReadingsIndex_Type()
)
diagECCReadingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagECCReadingsIndex.setStatus("current")


class _DiagECCReadingsLocat_Type(DisplayString):
    """Custom type diagECCReadingsLocat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiagECCReadingsLocat_Type.__name__ = "DisplayString"
_DiagECCReadingsLocat_Object = MibTableColumn
diagECCReadingsLocat = _DiagECCReadingsLocat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1, 2),
    _DiagECCReadingsLocat_Type()
)
diagECCReadingsLocat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagECCReadingsLocat.setStatus("current")


class _DiagECCReadingsType_Type(DisplayString):
    """Custom type diagECCReadingsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiagECCReadingsType_Type.__name__ = "DisplayString"
_DiagECCReadingsType_Object = MibTableColumn
diagECCReadingsType = _DiagECCReadingsType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1, 3),
    _DiagECCReadingsType_Type()
)
diagECCReadingsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagECCReadingsType.setStatus("current")


class _DiagECCReadingsVal_Type(DisplayString):
    """Custom type diagECCReadingsVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiagECCReadingsVal_Type.__name__ = "DisplayString"
_DiagECCReadingsVal_Object = MibTableColumn
diagECCReadingsVal = _DiagECCReadingsVal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1, 4),
    _DiagECCReadingsVal_Type()
)
diagECCReadingsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagECCReadingsVal.setStatus("current")


class _DiagECCReadingsApplicability_Type(DisplayString):
    """Custom type diagECCReadingsApplicability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiagECCReadingsApplicability_Type.__name__ = "DisplayString"
_DiagECCReadingsApplicability_Object = MibTableColumn
diagECCReadingsApplicability = _DiagECCReadingsApplicability_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 3, 1, 5),
    _DiagECCReadingsApplicability_Type()
)
diagECCReadingsApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagECCReadingsApplicability.setStatus("current")
_DiagCtrlHistoryTable_Object = MibTable
diagCtrlHistoryTable = _DiagCtrlHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 4)
)
if mibBuilder.loadTexts:
    diagCtrlHistoryTable.setStatus("current")
_DiagCtrlHistoryEntry_Object = MibTableRow
diagCtrlHistoryEntry = _DiagCtrlHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 4, 1)
)
diagCtrlHistoryEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DIAG-MIB", "diagCtrlHistoryIndex"),
)
if mibBuilder.loadTexts:
    diagCtrlHistoryEntry.setStatus("current")
_DiagCtrlHistoryIndex_Type = Counter32
_DiagCtrlHistoryIndex_Object = MibTableColumn
diagCtrlHistoryIndex = _DiagCtrlHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 4, 1, 1),
    _DiagCtrlHistoryIndex_Type()
)
diagCtrlHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagCtrlHistoryIndex.setStatus("current")


class _DiagCtrlHistoryHistory_Type(DisplayString):
    """Custom type diagCtrlHistoryHistory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiagCtrlHistoryHistory_Type.__name__ = "DisplayString"
_DiagCtrlHistoryHistory_Object = MibTableColumn
diagCtrlHistoryHistory = _DiagCtrlHistoryHistory_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 4, 1, 2),
    _DiagCtrlHistoryHistory_Type()
)
diagCtrlHistoryHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagCtrlHistoryHistory.setStatus("current")


class _DiagCtrlHistoryDateTime_Type(DisplayString):
    """Custom type diagCtrlHistoryDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DiagCtrlHistoryDateTime_Type.__name__ = "DisplayString"
_DiagCtrlHistoryDateTime_Object = MibTableColumn
diagCtrlHistoryDateTime = _DiagCtrlHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 18, 2, 4, 1, 3),
    _DiagCtrlHistoryDateTime_Type()
)
diagCtrlHistoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagCtrlHistoryDateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DIAG-MIB",
    **{"ciscoDSGDiag": ciscoDSGDiag,
       "powerOn": powerOn,
       "powerOnCreationDate": powerOnCreationDate,
       "powerOnDate": powerOnDate,
       "powerOnTotalHours": powerOnTotalHours,
       "powerOnHrsSinceLastPowerOff": powerOnHrsSinceLastPowerOff,
       "powerOnTotResetCount": powerOnTotResetCount,
       "powerOnClrableResetCount": powerOnClrableResetCount,
       "powerOnReasonLastReset": powerOnReasonLastReset,
       "powerOnClearResetCounter": powerOnClearResetCounter,
       "powerOnFactoryResetCount": powerOnFactoryResetCount,
       "powerOnCurrentDateTime": powerOnCurrentDateTime,
       "diagTable": diagTable,
       "diagHealthMonitorTable": diagHealthMonitorTable,
       "diagHealthMonitorEntry": diagHealthMonitorEntry,
       "diagHealthMonitorIndex": diagHealthMonitorIndex,
       "diagHealthMonitorName": diagHealthMonitorName,
       "diagHealthMonitorValue": diagHealthMonitorValue,
       "diagFanRPMTable": diagFanRPMTable,
       "diagFanRPMEntry": diagFanRPMEntry,
       "diagFanRPMIndex": diagFanRPMIndex,
       "diagFanRPMName": diagFanRPMName,
       "diagFanRPMValue": diagFanRPMValue,
       "diagECCReadingsTable": diagECCReadingsTable,
       "diagECCReadingsEntry": diagECCReadingsEntry,
       "diagECCReadingsIndex": diagECCReadingsIndex,
       "diagECCReadingsLocat": diagECCReadingsLocat,
       "diagECCReadingsType": diagECCReadingsType,
       "diagECCReadingsVal": diagECCReadingsVal,
       "diagECCReadingsApplicability": diagECCReadingsApplicability,
       "diagCtrlHistoryTable": diagCtrlHistoryTable,
       "diagCtrlHistoryEntry": diagCtrlHistoryEntry,
       "diagCtrlHistoryIndex": diagCtrlHistoryIndex,
       "diagCtrlHistoryHistory": diagCtrlHistoryHistory,
       "diagCtrlHistoryDateTime": diagCtrlHistoryDateTime}
)
