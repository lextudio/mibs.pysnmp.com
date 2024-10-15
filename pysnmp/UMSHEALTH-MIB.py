# SNMP MIB module (UMSHEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMSHEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:32 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Boolean,
 Datetime,
 Real32,
 Real64,
 Sint16,
 Sint32,
 Sint64,
 Sint8,
 String,
 Uint16,
 Uint32,
 Uint64,
 Uint8,
 ibmpsg,
 ibmpsgEvent,
 ibmpsgHealth,
 umservices,
 win32,
 win32Event) = mibBuilder.importSymbols(
    "UMS-MIB",
    "Boolean",
    "Datetime",
    "Real32",
    "Real64",
    "Sint16",
    "Sint32",
    "Sint64",
    "Sint8",
    "String",
    "Uint16",
    "Uint32",
    "Uint64",
    "Uint8",
    "ibmpsg",
    "ibmpsgEvent",
    "ibmpsgHealth",
    "umservices",
    "win32",
    "win32Event")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IBMPSGUMSComponentHealthTable_Object = MibTable
iBMPSGUMSComponentHealthTable = _IBMPSGUMSComponentHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3)
)
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthTable.setStatus("mandatory")
_IBMPSGUMSComponentHealthEntry_Object = MibTableRow
iBMPSGUMSComponentHealthEntry = _IBMPSGUMSComponentHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1)
)
iBMPSGUMSComponentHealthEntry.setIndexNames(
    (0, "UMSHEALTH-MIB", "iBMPSGUMSComponentHealthKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthEntry.setStatus("mandatory")
_IBMPSGUMSComponentHealthKeyIndex_Type = String
_IBMPSGUMSComponentHealthKeyIndex_Object = MibTableColumn
iBMPSGUMSComponentHealthKeyIndex = _IBMPSGUMSComponentHealthKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 1),
    _IBMPSGUMSComponentHealthKeyIndex_Type()
)
iBMPSGUMSComponentHealthKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthKeyIndex.setStatus("mandatory")
_IBMPSGUMSComponentHealthCurrentState_Type = Uint16
_IBMPSGUMSComponentHealthCurrentState_Object = MibTableColumn
iBMPSGUMSComponentHealthCurrentState = _IBMPSGUMSComponentHealthCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 2),
    _IBMPSGUMSComponentHealthCurrentState_Type()
)
iBMPSGUMSComponentHealthCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthCurrentState.setStatus("mandatory")
_IBMPSGUMSComponentHealthLastState_Type = Uint16
_IBMPSGUMSComponentHealthLastState_Object = MibTableColumn
iBMPSGUMSComponentHealthLastState = _IBMPSGUMSComponentHealthLastState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 3),
    _IBMPSGUMSComponentHealthLastState_Type()
)
iBMPSGUMSComponentHealthLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthLastState.setStatus("mandatory")
_IBMPSGUMSComponentHealthDateTime_Type = Datetime
_IBMPSGUMSComponentHealthDateTime_Object = MibTableColumn
iBMPSGUMSComponentHealthDateTime = _IBMPSGUMSComponentHealthDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 4),
    _IBMPSGUMSComponentHealthDateTime_Type()
)
iBMPSGUMSComponentHealthDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthDateTime.setStatus("mandatory")
_IBMPSGUMSComponentHealthLastUpdate_Type = Datetime
_IBMPSGUMSComponentHealthLastUpdate_Object = MibTableColumn
iBMPSGUMSComponentHealthLastUpdate = _IBMPSGUMSComponentHealthLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 5),
    _IBMPSGUMSComponentHealthLastUpdate_Type()
)
iBMPSGUMSComponentHealthLastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthLastUpdate.setStatus("mandatory")
_IBMPSGUMSComponentHealthDescription_Type = String
_IBMPSGUMSComponentHealthDescription_Object = MibTableColumn
iBMPSGUMSComponentHealthDescription = _IBMPSGUMSComponentHealthDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 6),
    _IBMPSGUMSComponentHealthDescription_Type()
)
iBMPSGUMSComponentHealthDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthDescription.setStatus("mandatory")
_IBMPSGUMSComponentHealthEventCategory_Type = String
_IBMPSGUMSComponentHealthEventCategory_Object = MibTableColumn
iBMPSGUMSComponentHealthEventCategory = _IBMPSGUMSComponentHealthEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 7),
    _IBMPSGUMSComponentHealthEventCategory_Type()
)
iBMPSGUMSComponentHealthEventCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthEventCategory.setStatus("mandatory")
_IBMPSGUMSComponentHealthResolution_Type = String
_IBMPSGUMSComponentHealthResolution_Object = MibTableColumn
iBMPSGUMSComponentHealthResolution = _IBMPSGUMSComponentHealthResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 8),
    _IBMPSGUMSComponentHealthResolution_Type()
)
iBMPSGUMSComponentHealthResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthResolution.setStatus("mandatory")
_IBMPSGUMSComponentHealthSourceObjectPath_Type = String
_IBMPSGUMSComponentHealthSourceObjectPath_Object = MibTableColumn
iBMPSGUMSComponentHealthSourceObjectPath = _IBMPSGUMSComponentHealthSourceObjectPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 9),
    _IBMPSGUMSComponentHealthSourceObjectPath_Type()
)
iBMPSGUMSComponentHealthSourceObjectPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthSourceObjectPath.setStatus("mandatory")
_IBMPSGUMSComponentHealthTargetObjectPath_Type = String
_IBMPSGUMSComponentHealthTargetObjectPath_Object = MibTableColumn
iBMPSGUMSComponentHealthTargetObjectPath = _IBMPSGUMSComponentHealthTargetObjectPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 10),
    _IBMPSGUMSComponentHealthTargetObjectPath_Type()
)
iBMPSGUMSComponentHealthTargetObjectPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthTargetObjectPath.setStatus("mandatory")
_IBMPSGUMSComponentHealthStatus_Type = String
_IBMPSGUMSComponentHealthStatus_Object = MibTableColumn
iBMPSGUMSComponentHealthStatus = _IBMPSGUMSComponentHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30, 3, 1, 11),
    _IBMPSGUMSComponentHealthStatus_Type()
)
iBMPSGUMSComponentHealthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGUMSComponentHealthStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMSHEALTH-MIB",
    **{"iBMPSGUMSComponentHealthTable": iBMPSGUMSComponentHealthTable,
       "iBMPSGUMSComponentHealthEntry": iBMPSGUMSComponentHealthEntry,
       "iBMPSGUMSComponentHealthKeyIndex": iBMPSGUMSComponentHealthKeyIndex,
       "iBMPSGUMSComponentHealthCurrentState": iBMPSGUMSComponentHealthCurrentState,
       "iBMPSGUMSComponentHealthLastState": iBMPSGUMSComponentHealthLastState,
       "iBMPSGUMSComponentHealthDateTime": iBMPSGUMSComponentHealthDateTime,
       "iBMPSGUMSComponentHealthLastUpdate": iBMPSGUMSComponentHealthLastUpdate,
       "iBMPSGUMSComponentHealthDescription": iBMPSGUMSComponentHealthDescription,
       "iBMPSGUMSComponentHealthEventCategory": iBMPSGUMSComponentHealthEventCategory,
       "iBMPSGUMSComponentHealthResolution": iBMPSGUMSComponentHealthResolution,
       "iBMPSGUMSComponentHealthSourceObjectPath": iBMPSGUMSComponentHealthSourceObjectPath,
       "iBMPSGUMSComponentHealthTargetObjectPath": iBMPSGUMSComponentHealthTargetObjectPath,
       "iBMPSGUMSComponentHealthStatus": iBMPSGUMSComponentHealthStatus}
)
