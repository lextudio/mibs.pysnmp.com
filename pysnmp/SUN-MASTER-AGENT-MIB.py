# SNMP MIB module (SUN-MASTER-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-MASTER-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:34 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_SunMasterAgent_ObjectIdentity = ObjectIdentity
sunMasterAgent = _SunMasterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 15)
)
_SunMasterAgentStatusFile_Type = DisplayString
_SunMasterAgentStatusFile_Object = MibScalar
sunMasterAgentStatusFile = _SunMasterAgentStatusFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 1),
    _SunMasterAgentStatusFile_Type()
)
sunMasterAgentStatusFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentStatusFile.setStatus("mandatory")
_SunMasterAgentResourceConfigFile_Type = DisplayString
_SunMasterAgentResourceConfigFile_Object = MibScalar
sunMasterAgentResourceConfigFile = _SunMasterAgentResourceConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 2),
    _SunMasterAgentResourceConfigFile_Type()
)
sunMasterAgentResourceConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentResourceConfigFile.setStatus("mandatory")
_SunMasterAgentConfigurationDir_Type = DisplayString
_SunMasterAgentConfigurationDir_Object = MibScalar
sunMasterAgentConfigurationDir = _SunMasterAgentConfigurationDir_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 3),
    _SunMasterAgentConfigurationDir_Type()
)
sunMasterAgentConfigurationDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentConfigurationDir.setStatus("mandatory")
_SunMasterAgentTrapPort_Type = Integer32
_SunMasterAgentTrapPort_Object = MibScalar
sunMasterAgentTrapPort = _SunMasterAgentTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 4),
    _SunMasterAgentTrapPort_Type()
)
sunMasterAgentTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentTrapPort.setStatus("mandatory")
_SunCheckSubAgentName_Type = DisplayString
_SunCheckSubAgentName_Object = MibScalar
sunCheckSubAgentName = _SunCheckSubAgentName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 5),
    _SunCheckSubAgentName_Type()
)
sunCheckSubAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunCheckSubAgentName.setStatus("mandatory")
_SunMasterAgentPollInterval_Type = Integer32
_SunMasterAgentPollInterval_Object = MibScalar
sunMasterAgentPollInterval = _SunMasterAgentPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 6),
    _SunMasterAgentPollInterval_Type()
)
sunMasterAgentPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentPollInterval.setStatus("mandatory")
_SunMasterAgentMaxAgentTimeOut_Type = Integer32
_SunMasterAgentMaxAgentTimeOut_Object = MibScalar
sunMasterAgentMaxAgentTimeOut = _SunMasterAgentMaxAgentTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 7),
    _SunMasterAgentMaxAgentTimeOut_Type()
)
sunMasterAgentMaxAgentTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMasterAgentMaxAgentTimeOut.setStatus("mandatory")
_SunSubAgentTable_Object = MibTable
sunSubAgentTable = _SunSubAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8)
)
if mibBuilder.loadTexts:
    sunSubAgentTable.setStatus("mandatory")
_SunSubAgentEntry_Object = MibTableRow
sunSubAgentEntry = _SunSubAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1)
)
sunSubAgentEntry.setIndexNames(
    (0, "SUN-MASTER-AGENT-MIB", "sunSubAgentID"),
)
if mibBuilder.loadTexts:
    sunSubAgentEntry.setStatus("mandatory")
_SunSubAgentID_Type = Integer32
_SunSubAgentID_Object = MibTableColumn
sunSubAgentID = _SunSubAgentID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 1),
    _SunSubAgentID_Type()
)
sunSubAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubAgentID.setStatus("mandatory")


class _SunSubAgentStatus_Type(Integer32):
    """Custom type sunSubAgentStatus based on Integer32"""
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
        *(("active", 3),
          ("destroy", 5),
          ("inactive", 4),
          ("init", 1),
          ("load", 2))
    )


_SunSubAgentStatus_Type.__name__ = "Integer32"
_SunSubAgentStatus_Object = MibTableColumn
sunSubAgentStatus = _SunSubAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 2),
    _SunSubAgentStatus_Type()
)
sunSubAgentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentStatus.setStatus("mandatory")
_SunSubAgentTimeout_Type = Integer32
_SunSubAgentTimeout_Object = MibTableColumn
sunSubAgentTimeout = _SunSubAgentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 3),
    _SunSubAgentTimeout_Type()
)
sunSubAgentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentTimeout.setStatus("mandatory")


class _SunSubAgentPortNumber_Type(Integer32):
    """Custom type sunSubAgentPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SunSubAgentPortNumber_Type.__name__ = "Integer32"
_SunSubAgentPortNumber_Object = MibTableColumn
sunSubAgentPortNumber = _SunSubAgentPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 4),
    _SunSubAgentPortNumber_Type()
)
sunSubAgentPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentPortNumber.setStatus("mandatory")
_SunSubAgentRegistrationFile_Type = DisplayString
_SunSubAgentRegistrationFile_Object = MibTableColumn
sunSubAgentRegistrationFile = _SunSubAgentRegistrationFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 5),
    _SunSubAgentRegistrationFile_Type()
)
sunSubAgentRegistrationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentRegistrationFile.setStatus("mandatory")
_SunSubAgentAccessControlFile_Type = DisplayString
_SunSubAgentAccessControlFile_Object = MibTableColumn
sunSubAgentAccessControlFile = _SunSubAgentAccessControlFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 6),
    _SunSubAgentAccessControlFile_Type()
)
sunSubAgentAccessControlFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentAccessControlFile.setStatus("mandatory")
_SunSubAgentExecutable_Type = DisplayString
_SunSubAgentExecutable_Object = MibTableColumn
sunSubAgentExecutable = _SunSubAgentExecutable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 7),
    _SunSubAgentExecutable_Type()
)
sunSubAgentExecutable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentExecutable.setStatus("mandatory")
_SunSubAgentVersionNum_Type = DisplayString
_SunSubAgentVersionNum_Object = MibTableColumn
sunSubAgentVersionNum = _SunSubAgentVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 8),
    _SunSubAgentVersionNum_Type()
)
sunSubAgentVersionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentVersionNum.setStatus("mandatory")
_SunSubAgentProcessID_Type = Integer32
_SunSubAgentProcessID_Object = MibTableColumn
sunSubAgentProcessID = _SunSubAgentProcessID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 9),
    _SunSubAgentProcessID_Type()
)
sunSubAgentProcessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentProcessID.setStatus("mandatory")
_SunSubAgentName_Type = DisplayString
_SunSubAgentName_Object = MibTableColumn
sunSubAgentName = _SunSubAgentName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 10),
    _SunSubAgentName_Type()
)
sunSubAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentName.setStatus("mandatory")
_SunSubAgentSystemUpTime_Type = TimeTicks
_SunSubAgentSystemUpTime_Object = MibTableColumn
sunSubAgentSystemUpTime = _SunSubAgentSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 11),
    _SunSubAgentSystemUpTime_Type()
)
sunSubAgentSystemUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentSystemUpTime.setStatus("mandatory")
_SunSubAgentWatchDogTime_Type = Integer32
_SunSubAgentWatchDogTime_Object = MibTableColumn
sunSubAgentWatchDogTime = _SunSubAgentWatchDogTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 12),
    _SunSubAgentWatchDogTime_Type()
)
sunSubAgentWatchDogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentWatchDogTime.setStatus("mandatory")


class _SunSubAgentTableIndex_Type(Integer32):
    """Custom type sunSubAgentTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SunSubAgentTableIndex_Type.__name__ = "Integer32"
_SunSubAgentTableIndex_Object = MibScalar
sunSubAgentTableIndex = _SunSubAgentTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 9),
    _SunSubAgentTableIndex_Type()
)
sunSubAgentTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubAgentTableIndex.setStatus("mandatory")
_SunSubTreeConfigurationTable_Object = MibTable
sunSubTreeConfigurationTable = _SunSubTreeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10)
)
if mibBuilder.loadTexts:
    sunSubTreeConfigurationTable.setStatus("mandatory")
_SunSubTreeConfigurationEntry_Object = MibTableRow
sunSubTreeConfigurationEntry = _SunSubTreeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1)
)
sunSubTreeConfigurationEntry.setIndexNames(
    (0, "SUN-MASTER-AGENT-MIB", "sunSubTreeAgentID"),
    (0, "SUN-MASTER-AGENT-MIB", "sunSubTreeIndex"),
)
if mibBuilder.loadTexts:
    sunSubTreeConfigurationEntry.setStatus("mandatory")
_SunSubTreeIndex_Type = Integer32
_SunSubTreeIndex_Object = MibTableColumn
sunSubTreeIndex = _SunSubTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 1),
    _SunSubTreeIndex_Type()
)
sunSubTreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeIndex.setStatus("mandatory")
_SunSubTreeAgentID_Type = Integer32
_SunSubTreeAgentID_Object = MibTableColumn
sunSubTreeAgentID = _SunSubTreeAgentID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 2),
    _SunSubTreeAgentID_Type()
)
sunSubTreeAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeAgentID.setStatus("mandatory")
_SunSubTreeOID_Type = ObjectIdentifier
_SunSubTreeOID_Object = MibTableColumn
sunSubTreeOID = _SunSubTreeOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 3),
    _SunSubTreeOID_Type()
)
sunSubTreeOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeOID.setStatus("mandatory")
_SunSubTreeStartColumn_Type = Integer32
_SunSubTreeStartColumn_Object = MibTableColumn
sunSubTreeStartColumn = _SunSubTreeStartColumn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 4),
    _SunSubTreeStartColumn_Type()
)
sunSubTreeStartColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeStartColumn.setStatus("mandatory")
_SunSubTreeEndColumn_Type = Integer32
_SunSubTreeEndColumn_Object = MibTableColumn
sunSubTreeEndColumn = _SunSubTreeEndColumn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 5),
    _SunSubTreeEndColumn_Type()
)
sunSubTreeEndColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeEndColumn.setStatus("mandatory")
_SunSubTreeStartRow_Type = Integer32
_SunSubTreeStartRow_Object = MibTableColumn
sunSubTreeStartRow = _SunSubTreeStartRow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 6),
    _SunSubTreeStartRow_Type()
)
sunSubTreeStartRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeStartRow.setStatus("mandatory")
_SunSubTreeEndRow_Type = Integer32
_SunSubTreeEndRow_Object = MibTableColumn
sunSubTreeEndRow = _SunSubTreeEndRow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 7),
    _SunSubTreeEndRow_Type()
)
sunSubTreeEndRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeEndRow.setStatus("mandatory")


class _SunSubTreeStatus_Type(Integer32):
    """Custom type sunSubTreeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SunSubTreeStatus_Type.__name__ = "Integer32"
_SunSubTreeStatus_Object = MibTableColumn
sunSubTreeStatus = _SunSubTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 8),
    _SunSubTreeStatus_Type()
)
sunSubTreeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeStatus.setStatus("mandatory")


class _SunSubTreeConfigurationTableIndex_Type(Integer32):
    """Custom type sunSubTreeConfigurationTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SunSubTreeConfigurationTableIndex_Type.__name__ = "Integer32"
_SunSubTreeConfigurationTableIndex_Object = MibScalar
sunSubTreeConfigurationTableIndex = _SunSubTreeConfigurationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 11),
    _SunSubTreeConfigurationTableIndex_Type()
)
sunSubTreeConfigurationTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeConfigurationTableIndex.setStatus("mandatory")
_SunSubTreeDispatchTable_Object = MibTable
sunSubTreeDispatchTable = _SunSubTreeDispatchTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12)
)
if mibBuilder.loadTexts:
    sunSubTreeDispatchTable.setStatus("mandatory")
_SunSubTreeDispatchEntry_Object = MibTableRow
sunSubTreeDispatchEntry = _SunSubTreeDispatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1)
)
sunSubTreeDispatchEntry.setIndexNames(
    (0, "SUN-MASTER-AGENT-MIB", "sunSubTreeDispatchAgentID"),
    (0, "SUN-MASTER-AGENT-MIB", "sunSubTreeDispatchIndex"),
)
if mibBuilder.loadTexts:
    sunSubTreeDispatchEntry.setStatus("mandatory")
_SunSubTreeDispatchIndex_Type = Integer32
_SunSubTreeDispatchIndex_Object = MibTableColumn
sunSubTreeDispatchIndex = _SunSubTreeDispatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 1),
    _SunSubTreeDispatchIndex_Type()
)
sunSubTreeDispatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeDispatchIndex.setStatus("mandatory")
_SunSubTreeDispatchAgentID_Type = Integer32
_SunSubTreeDispatchAgentID_Object = MibTableColumn
sunSubTreeDispatchAgentID = _SunSubTreeDispatchAgentID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 2),
    _SunSubTreeDispatchAgentID_Type()
)
sunSubTreeDispatchAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeDispatchAgentID.setStatus("mandatory")
_SunSubTreeDispatchOID_Type = ObjectIdentifier
_SunSubTreeDispatchOID_Object = MibTableColumn
sunSubTreeDispatchOID = _SunSubTreeDispatchOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 3),
    _SunSubTreeDispatchOID_Type()
)
sunSubTreeDispatchOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeDispatchOID.setStatus("mandatory")


class _SunSubTreeDispatchStatus_Type(Integer32):
    """Custom type sunSubTreeDispatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SunSubTreeDispatchStatus_Type.__name__ = "Integer32"
_SunSubTreeDispatchStatus_Object = MibTableColumn
sunSubTreeDispatchStatus = _SunSubTreeDispatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 4),
    _SunSubTreeDispatchStatus_Type()
)
sunSubTreeDispatchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunSubTreeDispatchStatus.setStatus("mandatory")


class _SunSubTreeDispatchTableIndex_Type(Integer32):
    """Custom type sunSubTreeDispatchTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SunSubTreeDispatchTableIndex_Type.__name__ = "Integer32"
_SunSubTreeDispatchTableIndex_Object = MibScalar
sunSubTreeDispatchTableIndex = _SunSubTreeDispatchTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 15, 13),
    _SunSubTreeDispatchTableIndex_Type()
)
sunSubTreeDispatchTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunSubTreeDispatchTableIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-MASTER-AGENT-MIB",
    **{"sun": sun,
       "products": products,
       "sunMasterAgent": sunMasterAgent,
       "sunMasterAgentStatusFile": sunMasterAgentStatusFile,
       "sunMasterAgentResourceConfigFile": sunMasterAgentResourceConfigFile,
       "sunMasterAgentConfigurationDir": sunMasterAgentConfigurationDir,
       "sunMasterAgentTrapPort": sunMasterAgentTrapPort,
       "sunCheckSubAgentName": sunCheckSubAgentName,
       "sunMasterAgentPollInterval": sunMasterAgentPollInterval,
       "sunMasterAgentMaxAgentTimeOut": sunMasterAgentMaxAgentTimeOut,
       "sunSubAgentTable": sunSubAgentTable,
       "sunSubAgentEntry": sunSubAgentEntry,
       "sunSubAgentID": sunSubAgentID,
       "sunSubAgentStatus": sunSubAgentStatus,
       "sunSubAgentTimeout": sunSubAgentTimeout,
       "sunSubAgentPortNumber": sunSubAgentPortNumber,
       "sunSubAgentRegistrationFile": sunSubAgentRegistrationFile,
       "sunSubAgentAccessControlFile": sunSubAgentAccessControlFile,
       "sunSubAgentExecutable": sunSubAgentExecutable,
       "sunSubAgentVersionNum": sunSubAgentVersionNum,
       "sunSubAgentProcessID": sunSubAgentProcessID,
       "sunSubAgentName": sunSubAgentName,
       "sunSubAgentSystemUpTime": sunSubAgentSystemUpTime,
       "sunSubAgentWatchDogTime": sunSubAgentWatchDogTime,
       "sunSubAgentTableIndex": sunSubAgentTableIndex,
       "sunSubTreeConfigurationTable": sunSubTreeConfigurationTable,
       "sunSubTreeConfigurationEntry": sunSubTreeConfigurationEntry,
       "sunSubTreeIndex": sunSubTreeIndex,
       "sunSubTreeAgentID": sunSubTreeAgentID,
       "sunSubTreeOID": sunSubTreeOID,
       "sunSubTreeStartColumn": sunSubTreeStartColumn,
       "sunSubTreeEndColumn": sunSubTreeEndColumn,
       "sunSubTreeStartRow": sunSubTreeStartRow,
       "sunSubTreeEndRow": sunSubTreeEndRow,
       "sunSubTreeStatus": sunSubTreeStatus,
       "sunSubTreeConfigurationTableIndex": sunSubTreeConfigurationTableIndex,
       "sunSubTreeDispatchTable": sunSubTreeDispatchTable,
       "sunSubTreeDispatchEntry": sunSubTreeDispatchEntry,
       "sunSubTreeDispatchIndex": sunSubTreeDispatchIndex,
       "sunSubTreeDispatchAgentID": sunSubTreeDispatchAgentID,
       "sunSubTreeDispatchOID": sunSubTreeDispatchOID,
       "sunSubTreeDispatchStatus": sunSubTreeDispatchStatus,
       "sunSubTreeDispatchTableIndex": sunSubTreeDispatchTableIndex}
)
