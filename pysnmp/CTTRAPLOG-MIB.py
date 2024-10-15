# SNMP MIB module (CTTRAPLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTTRAPLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:58 2024
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

(ctTrapLog,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTrapLog")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TotalNumberOfEntries_Type = Integer32
_TotalNumberOfEntries_Object = MibScalar
totalNumberOfEntries = _TotalNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 1),
    _TotalNumberOfEntries_Type()
)
totalNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfEntries.setStatus("mandatory")
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2)
)
if mibBuilder.loadTexts:
    configTable.setStatus("mandatory")
_ConfigTableEntry_Object = MibTableRow
configTableEntry = _ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1)
)
configTableEntry.setIndexNames(
    (0, "CTTRAPLOG-MIB", "slotInChassis"),
)
if mibBuilder.loadTexts:
    configTableEntry.setStatus("mandatory")
_SlotInChassis_Type = Integer32
_SlotInChassis_Object = MibTableColumn
slotInChassis = _SlotInChassis_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 1),
    _SlotInChassis_Type()
)
slotInChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInChassis.setStatus("mandatory")
_NumEntriesLoggeds_Type = Counter32
_NumEntriesLoggeds_Object = MibTableColumn
numEntriesLoggeds = _NumEntriesLoggeds_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 2),
    _NumEntriesLoggeds_Type()
)
numEntriesLoggeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEntriesLoggeds.setStatus("mandatory")
_NumEntriesRequested_Type = Integer32
_NumEntriesRequested_Object = MibTableColumn
numEntriesRequested = _NumEntriesRequested_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 3),
    _NumEntriesRequested_Type()
)
numEntriesRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numEntriesRequested.setStatus("mandatory")
_NumEntriesAllocated_Type = Integer32
_NumEntriesAllocated_Object = MibTableColumn
numEntriesAllocated = _NumEntriesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 4),
    _NumEntriesAllocated_Type()
)
numEntriesAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEntriesAllocated.setStatus("mandatory")
_LastLoggedEntryLogId_Type = Integer32
_LastLoggedEntryLogId_Object = MibTableColumn
lastLoggedEntryLogId = _LastLoggedEntryLogId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 5),
    _LastLoggedEntryLogId_Type()
)
lastLoggedEntryLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastLoggedEntryLogId.setStatus("mandatory")


class _LogCommand_Type(Integer32):
    """Custom type logCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearLog", 1)
    )


_LogCommand_Type.__name__ = "Integer32"
_LogCommand_Object = MibTableColumn
logCommand = _LogCommand_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 6),
    _LogCommand_Type()
)
logCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logCommand.setStatus("mandatory")
_Wrap_Type = Integer32
_Wrap_Object = MibTableColumn
wrap = _Wrap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 7),
    _Wrap_Type()
)
wrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrap.setStatus("mandatory")
_TrapLogTable_Object = MibTable
trapLogTable = _TrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3)
)
if mibBuilder.loadTexts:
    trapLogTable.setStatus("mandatory")
_TrapLogEntry_Object = MibTableRow
trapLogEntry = _TrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1)
)
trapLogEntry.setIndexNames(
    (0, "CTTRAPLOG-MIB", "slotChassis"),
    (0, "CTTRAPLOG-MIB", "logId"),
)
if mibBuilder.loadTexts:
    trapLogEntry.setStatus("mandatory")
_LogId_Type = Integer32
_LogId_Object = MibTableColumn
logId = _LogId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 1),
    _LogId_Type()
)
logId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logId.setStatus("mandatory")
_NvmpId_Type = Integer32
_NvmpId_Object = MibTableColumn
nvmpId = _NvmpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 2),
    _NvmpId_Type()
)
nvmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmpId.setStatus("mandatory")
_TrapLogAcknowledged_Type = Integer32
_TrapLogAcknowledged_Object = MibTableColumn
trapLogAcknowledged = _TrapLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 3),
    _TrapLogAcknowledged_Type()
)
trapLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogAcknowledged.setStatus("mandatory")


class _TrapLogVarBind_Type(OctetString):
    """Custom type trapLogVarBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_TrapLogVarBind_Type.__name__ = "OctetString"
_TrapLogVarBind_Object = MibTableColumn
trapLogVarBind = _TrapLogVarBind_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 4),
    _TrapLogVarBind_Type()
)
trapLogVarBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogVarBind.setStatus("mandatory")


class _TrapLogDescription_Type(DisplayString):
    """Custom type trapLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrapLogDescription_Type.__name__ = "DisplayString"
_TrapLogDescription_Object = MibTableColumn
trapLogDescription = _TrapLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 5),
    _TrapLogDescription_Type()
)
trapLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogDescription.setStatus("mandatory")
_TimeLogged_Type = TimeTicks
_TimeLogged_Object = MibTableColumn
timeLogged = _TimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 6),
    _TimeLogged_Type()
)
timeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeLogged.setStatus("mandatory")


class _FilterId_Type(Integer32):
    """Custom type filterId based on Integer32"""
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
        *(("existing", 5),
          ("fatal", 4),
          ("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_FilterId_Type.__name__ = "Integer32"
_FilterId_Object = MibTableColumn
filterId = _FilterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 7),
    _FilterId_Type()
)
filterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterId.setStatus("mandatory")
_SlotChassis_Type = Integer32
_SlotChassis_Object = MibTableColumn
slotChassis = _SlotChassis_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 8),
    _SlotChassis_Type()
)
slotChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotChassis.setStatus("mandatory")
_TrapOID_Type = ObjectIdentifier
_TrapOID_Object = MibTableColumn
trapOID = _TrapOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 9),
    _TrapOID_Type()
)
trapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOID.setStatus("mandatory")
_Z80Time_Type = TimeTicks
_Z80Time_Object = MibTableColumn
z80Time = _Z80Time_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 10),
    _Z80Time_Type()
)
z80Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z80Time.setStatus("mandatory")
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1)
)
filterEntry.setIndexNames(
    (0, "CTTRAPLOG-MIB", "filterSlotInChassis"),
    (0, "CTTRAPLOG-MIB", "filterFilterId"),
    (0, "CTTRAPLOG-MIB", "filterLogId"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterLogId_Type = Integer32
_FilterLogId_Object = MibTableColumn
filterLogId = _FilterLogId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 1),
    _FilterLogId_Type()
)
filterLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterLogId.setStatus("mandatory")
_FilterNvmpId_Type = Integer32
_FilterNvmpId_Object = MibTableColumn
filterNvmpId = _FilterNvmpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 2),
    _FilterNvmpId_Type()
)
filterNvmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterNvmpId.setStatus("mandatory")
_FilterTrapLogAcknowledged_Type = Integer32
_FilterTrapLogAcknowledged_Object = MibTableColumn
filterTrapLogAcknowledged = _FilterTrapLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 3),
    _FilterTrapLogAcknowledged_Type()
)
filterTrapLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTrapLogAcknowledged.setStatus("mandatory")


class _FilterTrapLogVarBind_Type(OctetString):
    """Custom type filterTrapLogVarBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_FilterTrapLogVarBind_Type.__name__ = "OctetString"
_FilterTrapLogVarBind_Object = MibTableColumn
filterTrapLogVarBind = _FilterTrapLogVarBind_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 4),
    _FilterTrapLogVarBind_Type()
)
filterTrapLogVarBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTrapLogVarBind.setStatus("mandatory")


class _FilterTrapLogDescription_Type(DisplayString):
    """Custom type filterTrapLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FilterTrapLogDescription_Type.__name__ = "DisplayString"
_FilterTrapLogDescription_Object = MibTableColumn
filterTrapLogDescription = _FilterTrapLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 5),
    _FilterTrapLogDescription_Type()
)
filterTrapLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTrapLogDescription.setStatus("mandatory")
_FilterTimeLogged_Type = TimeTicks
_FilterTimeLogged_Object = MibTableColumn
filterTimeLogged = _FilterTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 6),
    _FilterTimeLogged_Type()
)
filterTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTimeLogged.setStatus("mandatory")


class _FilterFilterId_Type(Integer32):
    """Custom type filterFilterId based on Integer32"""
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
        *(("existing", 5),
          ("fatal", 4),
          ("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_FilterFilterId_Type.__name__ = "Integer32"
_FilterFilterId_Object = MibTableColumn
filterFilterId = _FilterFilterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 7),
    _FilterFilterId_Type()
)
filterFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterFilterId.setStatus("mandatory")
_FilterSlotInChassis_Type = Integer32
_FilterSlotInChassis_Object = MibTableColumn
filterSlotInChassis = _FilterSlotInChassis_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 8),
    _FilterSlotInChassis_Type()
)
filterSlotInChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterSlotInChassis.setStatus("mandatory")
_FilterTrapOID_Type = ObjectIdentifier
_FilterTrapOID_Object = MibTableColumn
filterTrapOID = _FilterTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 9),
    _FilterTrapOID_Type()
)
filterTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTrapOID.setStatus("mandatory")
_FilterZ80Time_Type = TimeTicks
_FilterZ80Time_Object = MibTableColumn
filterZ80Time = _FilterZ80Time_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 10),
    _FilterZ80Time_Type()
)
filterZ80Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterZ80Time.setStatus("mandatory")


class _TrapLoggerAgent_Type(Integer32):
    """Custom type trapLoggerAgent based on Integer32"""
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
        *(("disabled", 1),
          ("elected", 4),
          ("enabled", 2),
          ("standby", 3))
    )


_TrapLoggerAgent_Type.__name__ = "Integer32"
_TrapLoggerAgent_Object = MibScalar
trapLoggerAgent = _TrapLoggerAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 5),
    _TrapLoggerAgent_Type()
)
trapLoggerAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLoggerAgent.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTTRAPLOG-MIB",
    **{"totalNumberOfEntries": totalNumberOfEntries,
       "configTable": configTable,
       "configTableEntry": configTableEntry,
       "slotInChassis": slotInChassis,
       "numEntriesLoggeds": numEntriesLoggeds,
       "numEntriesRequested": numEntriesRequested,
       "numEntriesAllocated": numEntriesAllocated,
       "lastLoggedEntryLogId": lastLoggedEntryLogId,
       "logCommand": logCommand,
       "wrap": wrap,
       "trapLogTable": trapLogTable,
       "trapLogEntry": trapLogEntry,
       "logId": logId,
       "nvmpId": nvmpId,
       "trapLogAcknowledged": trapLogAcknowledged,
       "trapLogVarBind": trapLogVarBind,
       "trapLogDescription": trapLogDescription,
       "timeLogged": timeLogged,
       "filterId": filterId,
       "slotChassis": slotChassis,
       "trapOID": trapOID,
       "z80Time": z80Time,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterLogId": filterLogId,
       "filterNvmpId": filterNvmpId,
       "filterTrapLogAcknowledged": filterTrapLogAcknowledged,
       "filterTrapLogVarBind": filterTrapLogVarBind,
       "filterTrapLogDescription": filterTrapLogDescription,
       "filterTimeLogged": filterTimeLogged,
       "filterFilterId": filterFilterId,
       "filterSlotInChassis": filterSlotInChassis,
       "filterTrapOID": filterTrapOID,
       "filterZ80Time": filterZ80Time,
       "trapLoggerAgent": trapLoggerAgent}
)
