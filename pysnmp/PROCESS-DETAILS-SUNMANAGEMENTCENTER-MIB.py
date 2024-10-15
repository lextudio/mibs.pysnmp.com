# SNMP MIB module (PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:47 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

processDetails = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13)
)
processDetails.setRevisions(
        ("1999-07-20 15:05",)
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
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    processTable.setStatus("current")
_ProcessTableEntry_Object = MibTableRow
processTableEntry = _ProcessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1)
)
processTableEntry.setIndexNames(
    (0, "PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB", "psProcessID"),
)
if mibBuilder.loadTexts:
    processTableEntry.setStatus("current")


class _PsProcessID_Type(Integer32):
    """Custom type psProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsProcessID_Type.__name__ = "Integer32"
_PsProcessID_Object = MibTableColumn
psProcessID = _PsProcessID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 1),
    _PsProcessID_Type()
)
psProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessID.setStatus("current")
_PsParentProcessID_Type = Integer32
_PsParentProcessID_Object = MibTableColumn
psParentProcessID = _PsParentProcessID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 2),
    _PsParentProcessID_Type()
)
psParentProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psParentProcessID.setStatus("current")
_PsUserID_Type = Integer32
_PsUserID_Object = MibTableColumn
psUserID = _PsUserID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 3),
    _PsUserID_Type()
)
psUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psUserID.setStatus("current")
_PsUserName_Type = DisplayString
_PsUserName_Object = MibTableColumn
psUserName = _PsUserName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 4),
    _PsUserName_Type()
)
psUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psUserName.setStatus("current")
_PsEUserID_Type = Integer32
_PsEUserID_Object = MibTableColumn
psEUserID = _PsEUserID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 5),
    _PsEUserID_Type()
)
psEUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEUserID.setStatus("current")
_PsGroupID_Type = Integer32
_PsGroupID_Object = MibTableColumn
psGroupID = _PsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 6),
    _PsGroupID_Type()
)
psGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psGroupID.setStatus("current")
_PsEGroupID_Type = Integer32
_PsEGroupID_Object = MibTableColumn
psEGroupID = _PsEGroupID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 7),
    _PsEGroupID_Type()
)
psEGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEGroupID.setStatus("current")
_PsSessionID_Type = Integer32
_PsSessionID_Object = MibTableColumn
psSessionID = _PsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 8),
    _PsSessionID_Type()
)
psSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSessionID.setStatus("current")
_PsProcessGroupID_Type = Integer32
_PsProcessGroupID_Object = MibTableColumn
psProcessGroupID = _PsProcessGroupID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 9),
    _PsProcessGroupID_Type()
)
psProcessGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessGroupID.setStatus("current")
_PsControlTTY_Type = DisplayString
_PsControlTTY_Object = MibTableColumn
psControlTTY = _PsControlTTY_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 10),
    _PsControlTTY_Type()
)
psControlTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psControlTTY.setStatus("current")
_PsStartTime_Type = DisplayString
_PsStartTime_Object = MibTableColumn
psStartTime = _PsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 11),
    _PsStartTime_Type()
)
psStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStartTime.setStatus("current")
_PsExecutionTime_Type = DisplayString
_PsExecutionTime_Object = MibTableColumn
psExecutionTime = _PsExecutionTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 12),
    _PsExecutionTime_Type()
)
psExecutionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psExecutionTime.setStatus("current")
_PsState_Type = DisplayString
_PsState_Object = MibTableColumn
psState = _PsState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 13),
    _PsState_Type()
)
psState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psState.setStatus("current")
_PsWaitChannel_Type = DisplayString
_PsWaitChannel_Object = MibTableColumn
psWaitChannel = _PsWaitChannel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 14),
    _PsWaitChannel_Type()
)
psWaitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psWaitChannel.setStatus("current")
_PsSchedulingClass_Type = DisplayString
_PsSchedulingClass_Object = MibTableColumn
psSchedulingClass = _PsSchedulingClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 15),
    _PsSchedulingClass_Type()
)
psSchedulingClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSchedulingClass.setStatus("current")
_PsAddress_Type = DisplayString
_PsAddress_Object = MibTableColumn
psAddress = _PsAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 16),
    _PsAddress_Type()
)
psAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAddress.setStatus("current")
_PsSize_Type = Integer32
_PsSize_Object = MibTableColumn
psSize = _PsSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 17),
    _PsSize_Type()
)
psSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSize.setStatus("current")
_PsPriority_Type = Integer32
_PsPriority_Object = MibTableColumn
psPriority = _PsPriority_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 18),
    _PsPriority_Type()
)
psPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPriority.setStatus("current")
_PsNice_Type = Integer32
_PsNice_Object = MibTableColumn
psNice = _PsNice_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 19),
    _PsNice_Type()
)
psNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNice.setStatus("current")
_PsPercentCPUTime_Type = DisplayString
_PsPercentCPUTime_Object = MibTableColumn
psPercentCPUTime = _PsPercentCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 20),
    _PsPercentCPUTime_Type()
)
psPercentCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPercentCPUTime.setStatus("current")
_PsPercentMemory_Type = DisplayString
_PsPercentMemory_Object = MibTableColumn
psPercentMemory = _PsPercentMemory_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 21),
    _PsPercentMemory_Type()
)
psPercentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPercentMemory.setStatus("current")
_PsCommand_Type = DisplayString
_PsCommand_Object = MibTableColumn
psCommand = _PsCommand_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 22),
    _PsCommand_Type()
)
psCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psCommand.setStatus("current")
_PsCommandLine_Type = DisplayString
_PsCommandLine_Object = MibTableColumn
psCommandLine = _PsCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 23),
    _PsCommandLine_Type()
)
psCommandLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psCommandLine.setStatus("current")
_PsZoneID_Type = DisplayString
_PsZoneID_Object = MibTableColumn
psZoneID = _PsZoneID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 24),
    _PsZoneID_Type()
)
psZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psZoneID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "processDetails": processDetails,
       "processTable": processTable,
       "processTableEntry": processTableEntry,
       "psProcessID": psProcessID,
       "psParentProcessID": psParentProcessID,
       "psUserID": psUserID,
       "psUserName": psUserName,
       "psEUserID": psEUserID,
       "psGroupID": psGroupID,
       "psEGroupID": psEGroupID,
       "psSessionID": psSessionID,
       "psProcessGroupID": psProcessGroupID,
       "psControlTTY": psControlTTY,
       "psStartTime": psStartTime,
       "psExecutionTime": psExecutionTime,
       "psState": psState,
       "psWaitChannel": psWaitChannel,
       "psSchedulingClass": psSchedulingClass,
       "psAddress": psAddress,
       "psSize": psSize,
       "psPriority": psPriority,
       "psNice": psNice,
       "psPercentCPUTime": psPercentCPUTime,
       "psPercentMemory": psPercentMemory,
       "psCommand": psCommand,
       "psCommandLine": psCommandLine,
       "psZoneID": psZoneID}
)
