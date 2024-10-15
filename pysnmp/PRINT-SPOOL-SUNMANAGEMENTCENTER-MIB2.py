# SNMP MIB module (PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:41 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

printSpool = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37)
)
printSpool.setRevisions(
        ("1999-09-20 15:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_PrsLpschedState_Type = DisplayString
_PrsLpschedState_Object = MibScalar
prsLpschedState = _PrsLpschedState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 1, 1),
    _PrsLpschedState_Type()
)
prsLpschedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsLpschedState.setStatus("current")
_PrsDeviceTable_Object = MibTable
prsDeviceTable = _PrsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1)
)
if mibBuilder.loadTexts:
    prsDeviceTable.setStatus("current")
_PrsDeviceEntry_Object = MibTableRow
prsDeviceEntry = _PrsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1)
)
prsDeviceEntry.setIndexNames(
    (0, "PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevName"),
)
if mibBuilder.loadTexts:
    prsDeviceEntry.setStatus("current")
_PrsDevRowstatus_Type = RowStatus
_PrsDevRowstatus_Object = MibTableColumn
prsDevRowstatus = _PrsDevRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 1),
    _PrsDevRowstatus_Type()
)
prsDevRowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prsDevRowstatus.setStatus("current")
_PrsDevName_Type = DisplayString
_PrsDevName_Object = MibTableColumn
prsDevName = _PrsDevName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 2),
    _PrsDevName_Type()
)
prsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsDevName.setStatus("current")
_PrsDevDesc_Type = DisplayString
_PrsDevDesc_Object = MibTableColumn
prsDevDesc = _PrsDevDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 3),
    _PrsDevDesc_Type()
)
prsDevDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prsDevDesc.setStatus("current")
_PrsDevMachine_Type = DisplayString
_PrsDevMachine_Object = MibTableColumn
prsDevMachine = _PrsDevMachine_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 4),
    _PrsDevMachine_Type()
)
prsDevMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsDevMachine.setStatus("current")
_PrsDevDevice_Type = DisplayString
_PrsDevDevice_Object = MibTableColumn
prsDevDevice = _PrsDevDevice_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 5),
    _PrsDevDevice_Type()
)
prsDevDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsDevDevice.setStatus("current")
_PrsDevState_Type = DisplayString
_PrsDevState_Object = MibTableColumn
prsDevState = _PrsDevState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 1, 1, 6),
    _PrsDevState_Type()
)
prsDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsDevState.setStatus("current")
_PrsQueueTable_Object = MibTable
prsQueueTable = _PrsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2)
)
if mibBuilder.loadTexts:
    prsQueueTable.setStatus("current")
_PrsQueueEntry_Object = MibTableRow
prsQueueEntry = _PrsQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1)
)
prsQueueEntry.setIndexNames(
    (0, "PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueName"),
)
if mibBuilder.loadTexts:
    prsQueueEntry.setStatus("current")
_PrsQueueName_Type = DisplayString
_PrsQueueName_Object = MibTableColumn
prsQueueName = _PrsQueueName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1, 1),
    _PrsQueueName_Type()
)
prsQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsQueueName.setStatus("current")
_PrsQueueState_Type = DisplayString
_PrsQueueState_Object = MibTableColumn
prsQueueState = _PrsQueueState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1, 2),
    _PrsQueueState_Type()
)
prsQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsQueueState.setStatus("current")


class _PrsQueueJobs_Type(Integer32):
    """Custom type prsQueueJobs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PrsQueueJobs_Type.__name__ = "Integer32"
_PrsQueueJobs_Object = MibTableColumn
prsQueueJobs = _PrsQueueJobs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1, 3),
    _PrsQueueJobs_Type()
)
prsQueueJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsQueueJobs.setStatus("current")
_PrsQueueCurrent_Type = DisplayString
_PrsQueueCurrent_Object = MibTableColumn
prsQueueCurrent = _PrsQueueCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1, 4),
    _PrsQueueCurrent_Type()
)
prsQueueCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsQueueCurrent.setStatus("current")


class _PrsQueueSize_Type(Integer32):
    """Custom type prsQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PrsQueueSize_Type.__name__ = "Integer32"
_PrsQueueSize_Object = MibTableColumn
prsQueueSize = _PrsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2, 2, 1, 5),
    _PrsQueueSize_Type()
)
prsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prsQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    prsQueueSize.setUnits("Bytes")

# Managed Objects groups

prsLpschedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 1)
)
prsLpschedGroup.setObjects(
    ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsLpschedState")
)
if mibBuilder.loadTexts:
    prsLpschedGroup.setStatus("current")

prsLpstatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37, 2)
)
prsLpstatGroup.setObjects(
      *(("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevRowstatus"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevName"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevDesc"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevMachine"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevDevice"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsDevState"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueName"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueState"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueJobs"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueCurrent"),
        ("PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2", "prsQueueSize"))
)
if mibBuilder.loadTexts:
    prsLpstatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRINT-SPOOL-SUNMANAGEMENTCENTER-MIB2",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "printSpool": printSpool,
       "prsLpschedGroup": prsLpschedGroup,
       "prsLpschedState": prsLpschedState,
       "prsLpstatGroup": prsLpstatGroup,
       "prsDeviceTable": prsDeviceTable,
       "prsDeviceEntry": prsDeviceEntry,
       "prsDevRowstatus": prsDevRowstatus,
       "prsDevName": prsDevName,
       "prsDevDesc": prsDevDesc,
       "prsDevMachine": prsDevMachine,
       "prsDevDevice": prsDevDevice,
       "prsDevState": prsDevState,
       "prsQueueTable": prsQueueTable,
       "prsQueueEntry": prsQueueEntry,
       "prsQueueName": prsQueueName,
       "prsQueueState": prsQueueState,
       "prsQueueJobs": prsQueueJobs,
       "prsQueueCurrent": prsQueueCurrent,
       "prsQueueSize": prsQueueSize}
)
