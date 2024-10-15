# SNMP MIB module (PATROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PATROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:56 2024
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



class PRowStatus(Integer32):
    """Custom type PRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class OutputMode(Integer32):
    """Custom type OutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("console", 4),
          ("gauge", 2),
          ("graph", 3),
          ("none", 0),
          ("text", 1))
    )





class States(Integer32):
    """Custom type States based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("offline", 3),
          ("ok", 0),
          ("void", 4),
          ("warn", 1))
    )





class PBoolean(Integer32):
    """Custom type PBoolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bmc_ObjectIdentity = ObjectIdentity
bmc = _Bmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031)
)
_PatrolMIB_ObjectIdentity = ObjectIdentity
patrolMIB = _PatrolMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1)
)
_PatrolAgent_ObjectIdentity = ObjectIdentity
patrolAgent = _PatrolAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1)
)
_PatrolObjects_ObjectIdentity = ObjectIdentity
patrolObjects = _PatrolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1)
)


class _ObjectsCwd_Type(DisplayString):
    """Custom type objectsCwd based on DisplayString"""
    defaultValue = OctetString("/")


_ObjectsCwd_Object = MibScalar
objectsCwd = _ObjectsCwd_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 2),
    _ObjectsCwd_Type()
)
objectsCwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    objectsCwd.setStatus("mandatory")
_ObjectsTable_Object = MibTable
objectsTable = _ObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    objectsTable.setStatus("deprecated")
_ObjectsEntry_Object = MibTableRow
objectsEntry = _ObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 3, 1)
)
objectsEntry.setIndexNames(
    (0, "PATROL-MIB", "objectName"),
)
if mibBuilder.loadTexts:
    objectsEntry.setStatus("mandatory")
_ObjectName_Type = DisplayString
_ObjectName_Object = MibTableColumn
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 3, 1, 1),
    _ObjectName_Type()
)
objectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectName.setStatus("mandatory")
_ObjectDescr_Type = DisplayString
_ObjectDescr_Object = MibTableColumn
objectDescr = _ObjectDescr_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 3, 1, 3),
    _ObjectDescr_Type()
)
objectDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectDescr.setStatus("mandatory")
_ObjectRowStatus_Type = PRowStatus
_ObjectRowStatus_Object = MibTableColumn
objectRowStatus = _ObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 3, 1, 4),
    _ObjectRowStatus_Type()
)
objectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    objectRowStatus.setStatus("mandatory")
_VariablesTable_Object = MibTable
variablesTable = _VariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    variablesTable.setStatus("deprecated")
_VariablesEntry_Object = MibTableRow
variablesEntry = _VariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1)
)
variablesEntry.setIndexNames(
    (0, "PATROL-MIB", "variableName"),
)
if mibBuilder.loadTexts:
    variablesEntry.setStatus("mandatory")
_VariableName_Type = DisplayString
_VariableName_Object = MibTableColumn
variableName = _VariableName_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1, 2),
    _VariableName_Type()
)
variableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableName.setStatus("mandatory")
_VariableType_Type = DisplayString
_VariableType_Object = MibTableColumn
variableType = _VariableType_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1, 3),
    _VariableType_Type()
)
variableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variableType.setStatus("mandatory")
_VariableValue_Type = DisplayString
_VariableValue_Object = MibTableColumn
variableValue = _VariableValue_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1, 4),
    _VariableValue_Type()
)
variableValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    variableValue.setStatus("mandatory")
_VariableDesr_Type = DisplayString
_VariableDesr_Object = MibTableColumn
variableDesr = _VariableDesr_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1, 5),
    _VariableDesr_Type()
)
variableDesr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    variableDesr.setStatus("mandatory")
_VariableRowStatus_Type = PRowStatus
_VariableRowStatus_Object = MibTableColumn
variableRowStatus = _VariableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 5, 1, 6),
    _VariableRowStatus_Type()
)
variableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    variableRowStatus.setStatus("mandatory")
_ApplicationsTable_Object = MibTable
applicationsTable = _ApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    applicationsTable.setStatus("deprecated")
_ApplicationsEntry_Object = MibTableRow
applicationsEntry = _ApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1)
)
applicationsEntry.setIndexNames(
    (0, "PATROL-MIB", "applicationOid"),
)
if mibBuilder.loadTexts:
    applicationsEntry.setStatus("mandatory")
_ApplicationName_Type = DisplayString
_ApplicationName_Object = MibTableColumn
applicationName = _ApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 1),
    _ApplicationName_Type()
)
applicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationName.setStatus("mandatory")
_ApplicationState_Type = States
_ApplicationState_Object = MibTableColumn
applicationState = _ApplicationState_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 2),
    _ApplicationState_Type()
)
applicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationState.setStatus("mandatory")
_ApplWorstInst_Type = DisplayString
_ApplWorstInst_Object = MibTableColumn
applWorstInst = _ApplWorstInst_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 3),
    _ApplWorstInst_Type()
)
applWorstInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applWorstInst.setStatus("mandatory")
_ApplMasterVersion_Type = Integer32
_ApplMasterVersion_Object = MibTableColumn
applMasterVersion = _ApplMasterVersion_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 4),
    _ApplMasterVersion_Type()
)
applMasterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applMasterVersion.setStatus("mandatory")
_ApplMinorRevision_Type = Integer32
_ApplMinorRevision_Object = MibTableColumn
applMinorRevision = _ApplMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 5),
    _ApplMinorRevision_Type()
)
applMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applMinorRevision.setStatus("mandatory")
_ApplicationRowStatus_Type = PRowStatus
_ApplicationRowStatus_Object = MibTableColumn
applicationRowStatus = _ApplicationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 6),
    _ApplicationRowStatus_Type()
)
applicationRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationRowStatus.setStatus("mandatory")


class _ApplicationOid_Type(Integer32):
    """Custom type applicationOid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApplicationOid_Type.__name__ = "Integer32"
_ApplicationOid_Object = MibTableColumn
applicationOid = _ApplicationOid_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 6, 1, 7),
    _ApplicationOid_Type()
)
applicationOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationOid.setStatus("mandatory")
_ApplInstTable_Object = MibTable
applInstTable = _ApplInstTable_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    applInstTable.setStatus("deprecated")
_ApplInstEntry_Object = MibTableRow
applInstEntry = _ApplInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1)
)
applInstEntry.setIndexNames(
    (0, "PATROL-MIB", "applicationOid"),
    (0, "PATROL-MIB", "applInstOid"),
)
if mibBuilder.loadTexts:
    applInstEntry.setStatus("mandatory")
_ApplInstName_Type = DisplayString
_ApplInstName_Object = MibTableColumn
applInstName = _ApplInstName_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 1),
    _ApplInstName_Type()
)
applInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstName.setStatus("mandatory")
_ApplInstRuleState_Type = States
_ApplInstRuleState_Object = MibTableColumn
applInstRuleState = _ApplInstRuleState_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 2),
    _ApplInstRuleState_Type()
)
applInstRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstRuleState.setStatus("mandatory")
_ApplInstStatus_Type = States
_ApplInstStatus_Object = MibTableColumn
applInstStatus = _ApplInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 3),
    _ApplInstStatus_Type()
)
applInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstStatus.setStatus("mandatory")
_ApplInstWorstParam_Type = DisplayString
_ApplInstWorstParam_Object = MibTableColumn
applInstWorstParam = _ApplInstWorstParam_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 4),
    _ApplInstWorstParam_Type()
)
applInstWorstParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstWorstParam.setStatus("mandatory")
_ApplInstCreateIcon_Type = PBoolean
_ApplInstCreateIcon_Object = MibTableColumn
applInstCreateIcon = _ApplInstCreateIcon_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 5),
    _ApplInstCreateIcon_Type()
)
applInstCreateIcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstCreateIcon.setStatus("mandatory")
_ApplInstRowStatus_Type = PRowStatus
_ApplInstRowStatus_Object = MibTableColumn
applInstRowStatus = _ApplInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 6),
    _ApplInstRowStatus_Type()
)
applInstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstRowStatus.setStatus("mandatory")


class _ApplInstOid_Type(Integer32):
    """Custom type applInstOid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApplInstOid_Type.__name__ = "Integer32"
_ApplInstOid_Object = MibTableColumn
applInstOid = _ApplInstOid_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 7),
    _ApplInstOid_Type()
)
applInstOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstOid.setStatus("mandatory")


class _ApplInstPInstOid_Type(Integer32):
    """Custom type applInstPInstOid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApplInstPInstOid_Type.__name__ = "Integer32"
_ApplInstPInstOid_Object = MibTableColumn
applInstPInstOid = _ApplInstPInstOid_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 8),
    _ApplInstPInstOid_Type()
)
applInstPInstOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstPInstOid.setStatus("mandatory")


class _ApplInstPApplOid_Type(Integer32):
    """Custom type applInstPApplOid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApplInstPApplOid_Type.__name__ = "Integer32"
_ApplInstPApplOid_Object = MibTableColumn
applInstPApplOid = _ApplInstPApplOid_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 7, 1, 9),
    _ApplInstPApplOid_Type()
)
applInstPApplOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInstPApplOid.setStatus("mandatory")
_ParametersTable_ObjectIdentity = ObjectIdentity
parametersTable = _ParametersTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8)
)
_ParametersEntry_Object = MibTableRow
parametersEntry = _ParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1)
)
parametersEntry.setIndexNames(
    (0, "PATROL-MIB", "applicationOid"),
    (0, "PATROL-MIB", "applInstOid"),
    (0, "PATROL-MIB", "parameterObjId"),
)
if mibBuilder.loadTexts:
    parametersEntry.setStatus("mandatory")
_ParameterName_Type = DisplayString
_ParameterName_Object = MibTableColumn
parameterName = _ParameterName_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 1),
    _ParameterName_Type()
)
parameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterName.setStatus("mandatory")
_ParameterState_Type = States
_ParameterState_Object = MibTableColumn
parameterState = _ParameterState_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 2),
    _ParameterState_Type()
)
parameterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterState.setStatus("mandatory")
_ParameterCurrentTime_Type = TimeTicks
_ParameterCurrentTime_Object = MibTableColumn
parameterCurrentTime = _ParameterCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 3),
    _ParameterCurrentTime_Type()
)
parameterCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterCurrentTime.setStatus("mandatory")
_ParameterCurrentValue_Type = DisplayString
_ParameterCurrentValue_Object = MibTableColumn
parameterCurrentValue = _ParameterCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 4),
    _ParameterCurrentValue_Type()
)
parameterCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterCurrentValue.setStatus("mandatory")
_ParameterPollingInt_Type = Integer32
_ParameterPollingInt_Object = MibTableColumn
parameterPollingInt = _ParameterPollingInt_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 5),
    _ParameterPollingInt_Type()
)
parameterPollingInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterPollingInt.setStatus("mandatory")
_ParameterRetries_Type = Integer32
_ParameterRetries_Object = MibTableColumn
parameterRetries = _ParameterRetries_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 6),
    _ParameterRetries_Type()
)
parameterRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterRetries.setStatus("mandatory")
_ParameterOutputMode_Type = OutputMode
_ParameterOutputMode_Object = MibTableColumn
parameterOutputMode = _ParameterOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 7),
    _ParameterOutputMode_Type()
)
parameterOutputMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterOutputMode.setStatus("mandatory")
_ParameterAutoScale_Type = PBoolean
_ParameterAutoScale_Object = MibTableColumn
parameterAutoScale = _ParameterAutoScale_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 8),
    _ParameterAutoScale_Type()
)
parameterAutoScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterAutoScale.setStatus("mandatory")
_ParameterYaxisMin_Type = Integer32
_ParameterYaxisMin_Object = MibTableColumn
parameterYaxisMin = _ParameterYaxisMin_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 9),
    _ParameterYaxisMin_Type()
)
parameterYaxisMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterYaxisMin.setStatus("mandatory")
_ParameterYaxisMax_Type = Integer32
_ParameterYaxisMax_Object = MibTableColumn
parameterYaxisMax = _ParameterYaxisMax_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 10),
    _ParameterYaxisMax_Type()
)
parameterYaxisMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterYaxisMax.setStatus("mandatory")
_ParameterRowStatus_Type = PRowStatus
_ParameterRowStatus_Object = MibTableColumn
parameterRowStatus = _ParameterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 11),
    _ParameterRowStatus_Type()
)
parameterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameterRowStatus.setStatus("mandatory")


class _ParameterObjId_Type(Integer32):
    """Custom type parameterObjId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ParameterObjId_Type.__name__ = "Integer32"
_ParameterObjId_Object = MibTableColumn
parameterObjId = _ParameterObjId_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 12),
    _ParameterObjId_Type()
)
parameterObjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterObjId.setStatus("mandatory")
_ParameterIntValue_ObjectIdentity = ObjectIdentity
parameterIntValue = _ParameterIntValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 13)
)
_ParameterActiveStat_Type = PBoolean
_ParameterActiveStat_Object = MibTableColumn
parameterActiveStat = _ParameterActiveStat_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 14),
    _ParameterActiveStat_Type()
)
parameterActiveStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameterActiveStat.setStatus("mandatory")
_ParameterRunningStat_Type = PBoolean
_ParameterRunningStat_Object = MibTableColumn
parameterRunningStat = _ParameterRunningStat_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 1, 8, 1, 15),
    _ParameterRunningStat_Type()
)
parameterRunningStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameterRunningStat.setStatus("mandatory")
_PatrolTraps_ObjectIdentity = ObjectIdentity
patrolTraps = _PatrolTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 2)
)
_AgentExecuteCommand_Type = DisplayString
_AgentExecuteCommand_Object = MibScalar
agentExecuteCommand = _AgentExecuteCommand_Object(
    (1, 3, 6, 1, 4, 1, 1031, 1, 1, 3),
    _AgentExecuteCommand_Type()
)
agentExecuteCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecuteCommand.setStatus("mandatory")
_PatrolConsole_ObjectIdentity = ObjectIdentity
patrolConsole = _PatrolConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1031, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PATROL-MIB",
    **{"PRowStatus": PRowStatus,
       "OutputMode": OutputMode,
       "States": States,
       "PBoolean": PBoolean,
       "bmc": bmc,
       "patrolMIB": patrolMIB,
       "patrolAgent": patrolAgent,
       "patrolObjects": patrolObjects,
       "objectsCwd": objectsCwd,
       "objectsTable": objectsTable,
       "objectsEntry": objectsEntry,
       "objectName": objectName,
       "objectDescr": objectDescr,
       "objectRowStatus": objectRowStatus,
       "variablesTable": variablesTable,
       "variablesEntry": variablesEntry,
       "variableName": variableName,
       "variableType": variableType,
       "variableValue": variableValue,
       "variableDesr": variableDesr,
       "variableRowStatus": variableRowStatus,
       "applicationsTable": applicationsTable,
       "applicationsEntry": applicationsEntry,
       "applicationName": applicationName,
       "applicationState": applicationState,
       "applWorstInst": applWorstInst,
       "applMasterVersion": applMasterVersion,
       "applMinorRevision": applMinorRevision,
       "applicationRowStatus": applicationRowStatus,
       "applicationOid": applicationOid,
       "applInstTable": applInstTable,
       "applInstEntry": applInstEntry,
       "applInstName": applInstName,
       "applInstRuleState": applInstRuleState,
       "applInstStatus": applInstStatus,
       "applInstWorstParam": applInstWorstParam,
       "applInstCreateIcon": applInstCreateIcon,
       "applInstRowStatus": applInstRowStatus,
       "applInstOid": applInstOid,
       "applInstPInstOid": applInstPInstOid,
       "applInstPApplOid": applInstPApplOid,
       "parametersTable": parametersTable,
       "parametersEntry": parametersEntry,
       "parameterName": parameterName,
       "parameterState": parameterState,
       "parameterCurrentTime": parameterCurrentTime,
       "parameterCurrentValue": parameterCurrentValue,
       "parameterPollingInt": parameterPollingInt,
       "parameterRetries": parameterRetries,
       "parameterOutputMode": parameterOutputMode,
       "parameterAutoScale": parameterAutoScale,
       "parameterYaxisMin": parameterYaxisMin,
       "parameterYaxisMax": parameterYaxisMax,
       "parameterRowStatus": parameterRowStatus,
       "parameterObjId": parameterObjId,
       "parameterIntValue": parameterIntValue,
       "parameterActiveStat": parameterActiveStat,
       "parameterRunningStat": parameterRunningStat,
       "patrolTraps": patrolTraps,
       "agentExecuteCommand": agentExecuteCommand,
       "patrolConsole": patrolConsole}
)
