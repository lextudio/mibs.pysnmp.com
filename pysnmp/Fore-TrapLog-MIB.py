# SNMP MIB module (Fore-TrapLog-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-TrapLog-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:50 2024
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

(TrapNumber,
 snmpTrapLog) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "TrapNumber",
    "snmpTrapLog")

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
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

foreTrapLogModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrapLogTable_Object = MibTable
trapLogTable = _TrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2)
)
if mibBuilder.loadTexts:
    trapLogTable.setStatus("current")
_TrapLogEntry_Object = MibTableRow
trapLogEntry = _TrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1)
)
trapLogEntry.setIndexNames(
    (0, "Fore-TrapLog-MIB", "trapLogIndex"),
)
if mibBuilder.loadTexts:
    trapLogEntry.setStatus("current")
_TrapLogIndex_Type = Integer32
_TrapLogIndex_Object = MibTableColumn
trapLogIndex = _TrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 1),
    _TrapLogIndex_Type()
)
trapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogIndex.setStatus("current")
_TrapLogEnterprise_Type = ObjectIdentifier
_TrapLogEnterprise_Object = MibTableColumn
trapLogEnterprise = _TrapLogEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 2),
    _TrapLogEnterprise_Type()
)
trapLogEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogEnterprise.setStatus("current")
_TrapLogGenericId_Type = TrapNumber
_TrapLogGenericId_Object = MibTableColumn
trapLogGenericId = _TrapLogGenericId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 3),
    _TrapLogGenericId_Type()
)
trapLogGenericId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogGenericId.setStatus("current")
_TrapLogId_Type = TrapNumber
_TrapLogId_Object = MibTableColumn
trapLogId = _TrapLogId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 4),
    _TrapLogId_Type()
)
trapLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogId.setStatus("current")
_TrapLogXmits_Type = Counter32
_TrapLogXmits_Object = MibTableColumn
trapLogXmits = _TrapLogXmits_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 5),
    _TrapLogXmits_Type()
)
trapLogXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogXmits.setStatus("current")
_TrapLogLastXmit_Type = TimeStamp
_TrapLogLastXmit_Object = MibTableColumn
trapLogLastXmit = _TrapLogLastXmit_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 6),
    _TrapLogLastXmit_Type()
)
trapLogLastXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogLastXmit.setStatus("current")
_TrapLogEvents_Type = Counter32
_TrapLogEvents_Object = MibTableColumn
trapLogEvents = _TrapLogEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 7),
    _TrapLogEvents_Type()
)
trapLogEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogEvents.setStatus("current")
_TrapLogLastEvent_Type = TimeStamp
_TrapLogLastEvent_Object = MibTableColumn
trapLogLastEvent = _TrapLogLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 2, 1, 8),
    _TrapLogLastEvent_Type()
)
trapLogLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogLastEvent.setStatus("current")
_TrapLogVarTable_Object = MibTable
trapLogVarTable = _TrapLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 3)
)
if mibBuilder.loadTexts:
    trapLogVarTable.setStatus("current")
_TrapLogVarEntry_Object = MibTableRow
trapLogVarEntry = _TrapLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 3, 1)
)
trapLogVarEntry.setIndexNames(
    (0, "Fore-TrapLog-MIB", "trapLogIndex"),
    (0, "Fore-TrapLog-MIB", "trapLogVarIndex"),
)
if mibBuilder.loadTexts:
    trapLogVarEntry.setStatus("current")
_TrapLogVarIndex_Type = Integer32
_TrapLogVarIndex_Object = MibTableColumn
trapLogVarIndex = _TrapLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 3, 1, 1),
    _TrapLogVarIndex_Type()
)
trapLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLogVarIndex.setStatus("current")
_TrapLogVarOID_Type = ObjectIdentifier
_TrapLogVarOID_Object = MibTableColumn
trapLogVarOID = _TrapLogVarOID_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 3, 1, 2),
    _TrapLogVarOID_Type()
)
trapLogVarOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogVarOID.setStatus("current")
_TrapLogVarValue_Type = OctetString
_TrapLogVarValue_Object = MibTableColumn
trapLogVarValue = _TrapLogVarValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 3, 1, 3),
    _TrapLogVarValue_Type()
)
trapLogVarValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogVarValue.setStatus("current")
_TrapThresholdTable_Object = MibTable
trapThresholdTable = _TrapThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4)
)
if mibBuilder.loadTexts:
    trapThresholdTable.setStatus("current")
_TrapThresholdEntry_Object = MibTableRow
trapThresholdEntry = _TrapThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1)
)
trapThresholdEntry.setIndexNames(
    (0, "Fore-TrapLog-MIB", "trapThresholdTrapEnterprise"),
    (0, "Fore-TrapLog-MIB", "trapThresholdGenericTrapId"),
    (0, "Fore-TrapLog-MIB", "trapThresholdTrapId"),
)
if mibBuilder.loadTexts:
    trapThresholdEntry.setStatus("current")
_TrapThresholdTrapEnterprise_Type = ObjectIdentifier
_TrapThresholdTrapEnterprise_Object = MibTableColumn
trapThresholdTrapEnterprise = _TrapThresholdTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1, 1),
    _TrapThresholdTrapEnterprise_Type()
)
trapThresholdTrapEnterprise.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapThresholdTrapEnterprise.setStatus("current")
_TrapThresholdGenericTrapId_Type = TrapNumber
_TrapThresholdGenericTrapId_Object = MibTableColumn
trapThresholdGenericTrapId = _TrapThresholdGenericTrapId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1, 2),
    _TrapThresholdGenericTrapId_Type()
)
trapThresholdGenericTrapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapThresholdGenericTrapId.setStatus("current")
_TrapThresholdTrapId_Type = TrapNumber
_TrapThresholdTrapId_Object = MibTableColumn
trapThresholdTrapId = _TrapThresholdTrapId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1, 3),
    _TrapThresholdTrapId_Type()
)
trapThresholdTrapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapThresholdTrapId.setStatus("current")
_TrapThresholdValue_Type = Integer32
_TrapThresholdValue_Object = MibTableColumn
trapThresholdValue = _TrapThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1, 4),
    _TrapThresholdValue_Type()
)
trapThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThresholdValue.setStatus("current")
_TrapThresholdTimePeriod_Type = TimeInterval
_TrapThresholdTimePeriod_Object = MibTableColumn
trapThresholdTimePeriod = _TrapThresholdTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 1, 5),
    _TrapThresholdTimePeriod_Type()
)
trapThresholdTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThresholdTimePeriod.setStatus("current")


class _TrapThresholdTableReset_Type(Integer32):
    """Custom type trapThresholdTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrapThresholdTableReset_Type.__name__ = "Integer32"
_TrapThresholdTableReset_Object = MibScalar
trapThresholdTableReset = _TrapThresholdTableReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 9, 4, 3),
    _TrapThresholdTableReset_Type()
)
trapThresholdTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThresholdTableReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-TrapLog-MIB",
    **{"foreTrapLogModule": foreTrapLogModule,
       "trapLogTable": trapLogTable,
       "trapLogEntry": trapLogEntry,
       "trapLogIndex": trapLogIndex,
       "trapLogEnterprise": trapLogEnterprise,
       "trapLogGenericId": trapLogGenericId,
       "trapLogId": trapLogId,
       "trapLogXmits": trapLogXmits,
       "trapLogLastXmit": trapLogLastXmit,
       "trapLogEvents": trapLogEvents,
       "trapLogLastEvent": trapLogLastEvent,
       "trapLogVarTable": trapLogVarTable,
       "trapLogVarEntry": trapLogVarEntry,
       "trapLogVarIndex": trapLogVarIndex,
       "trapLogVarOID": trapLogVarOID,
       "trapLogVarValue": trapLogVarValue,
       "trapThresholdTable": trapThresholdTable,
       "trapThresholdEntry": trapThresholdEntry,
       "trapThresholdTrapEnterprise": trapThresholdTrapEnterprise,
       "trapThresholdGenericTrapId": trapThresholdGenericTrapId,
       "trapThresholdTrapId": trapThresholdTrapId,
       "trapThresholdValue": trapThresholdValue,
       "trapThresholdTimePeriod": trapThresholdTimePeriod,
       "trapThresholdTableReset": trapThresholdTableReset}
)
