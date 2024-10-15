# SNMP MIB module (IBM-AIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-AIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:23 2024
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

ibmAIX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_AixSystem_ObjectIdentity = ObjectIdentity
aixSystem = _AixSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1)
)
_AixAgent_ObjectIdentity = ObjectIdentity
aixAgent = _AixAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1)
)


class _AixAgentAction_Type(Integer32):
    """Custom type aixAgentAction based on Integer32"""
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
        *(("debugOff", 3),
          ("debugOn", 2),
          ("reset", 1),
          ("running", 5),
          ("shutdown", 4))
    )


_AixAgentAction_Type.__name__ = "Integer32"
_AixAgentAction_Object = MibScalar
aixAgentAction = _AixAgentAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 1),
    _AixAgentAction_Type()
)
aixAgentAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixAgentAction.setStatus("current")
_AixAgentCmdString_Type = DisplayString
_AixAgentCmdString_Object = MibScalar
aixAgentCmdString = _AixAgentCmdString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 2),
    _AixAgentCmdString_Type()
)
aixAgentCmdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixAgentCmdString.setStatus("current")


class _AixAgentExeCommand_Type(Integer32):
    """Custom type aixAgentExeCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("trigger", 1))
    )


_AixAgentExeCommand_Type.__name__ = "Integer32"
_AixAgentExeCommand_Object = MibScalar
aixAgentExeCommand = _AixAgentExeCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 3),
    _AixAgentExeCommand_Type()
)
aixAgentExeCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixAgentExeCommand.setStatus("current")


class _AixAgentCmdResult_Type(Integer32):
    """Custom type aixAgentCmdResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixAgentCmdResult_Type.__name__ = "Integer32"
_AixAgentCmdResult_Object = MibScalar
aixAgentCmdResult = _AixAgentCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 4),
    _AixAgentCmdResult_Type()
)
aixAgentCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAgentCmdResult.setStatus("current")


class _AixAgentPollInterval_Type(Integer32):
    """Custom type aixAgentPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 2147483647),
    )


_AixAgentPollInterval_Type.__name__ = "Integer32"
_AixAgentPollInterval_Object = MibScalar
aixAgentPollInterval = _AixAgentPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 5),
    _AixAgentPollInterval_Type()
)
aixAgentPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixAgentPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    aixAgentPollInterval.setUnits("seconds")


class _AixPollEnable_Type(Integer32):
    """Custom type aixPollEnable based on Integer32"""
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


_AixPollEnable_Type.__name__ = "Integer32"
_AixPollEnable_Object = MibScalar
aixPollEnable = _AixPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 6),
    _AixPollEnable_Type()
)
aixPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixPollEnable.setStatus("current")
_AixLastTrapMsg_Type = DisplayString
_AixLastTrapMsg_Object = MibScalar
aixLastTrapMsg = _AixLastTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 7),
    _AixLastTrapMsg_Type()
)
aixLastTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLastTrapMsg.setStatus("current")
_AixAgentCmdOutTable_Object = MibTable
aixAgentCmdOutTable = _AixAgentCmdOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aixAgentCmdOutTable.setStatus("current")
_AixAgentCmdOutTableEntry_Object = MibTableRow
aixAgentCmdOutTableEntry = _AixAgentCmdOutTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 8, 1)
)
aixAgentCmdOutTableEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixAgentCmdOutIndex"),
)
if mibBuilder.loadTexts:
    aixAgentCmdOutTableEntry.setStatus("current")
_AixAgentCmdOutput_Type = DisplayString
_AixAgentCmdOutput_Object = MibTableColumn
aixAgentCmdOutput = _AixAgentCmdOutput_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 8, 1, 1),
    _AixAgentCmdOutput_Type()
)
aixAgentCmdOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAgentCmdOutput.setStatus("current")


class _AixAgentCmdOutIndex_Type(Integer32):
    """Custom type aixAgentCmdOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixAgentCmdOutIndex_Type.__name__ = "Integer32"
_AixAgentCmdOutIndex_Object = MibTableColumn
aixAgentCmdOutIndex = _AixAgentCmdOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 8, 1, 2),
    _AixAgentCmdOutIndex_Type()
)
aixAgentCmdOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAgentCmdOutIndex.setStatus("current")


class _AixFsPollInterval_Type(Integer32):
    """Custom type aixFsPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFsPollInterval_Type.__name__ = "Integer32"
_AixFsPollInterval_Object = MibScalar
aixFsPollInterval = _AixFsPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 9),
    _AixFsPollInterval_Type()
)
aixFsPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixFsPollInterval.setStatus("current")


class _AixCPUPollInterval_Type(Integer32):
    """Custom type aixCPUPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixCPUPollInterval_Type.__name__ = "Integer32"
_AixCPUPollInterval_Object = MibScalar
aixCPUPollInterval = _AixCPUPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 10),
    _AixCPUPollInterval_Type()
)
aixCPUPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixCPUPollInterval.setStatus("current")


class _AixVgPollInterval_Type(Integer32):
    """Custom type aixVgPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgPollInterval_Type.__name__ = "Integer32"
_AixVgPollInterval_Object = MibScalar
aixVgPollInterval = _AixVgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 11),
    _AixVgPollInterval_Type()
)
aixVgPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixVgPollInterval.setStatus("current")


class _AixPagePollInterval_Type(Integer32):
    """Custom type aixPagePollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixPagePollInterval_Type.__name__ = "Integer32"
_AixPagePollInterval_Object = MibScalar
aixPagePollInterval = _AixPagePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 12),
    _AixPagePollInterval_Type()
)
aixPagePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixPagePollInterval.setStatus("current")


class _AixLFPollInterval_Type(Integer32):
    """Custom type aixLFPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixLFPollInterval_Type.__name__ = "Integer32"
_AixLFPollInterval_Object = MibScalar
aixLFPollInterval = _AixLFPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 1, 13),
    _AixLFPollInterval_Type()
)
aixLFPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixLFPollInterval.setStatus("current")
_AixSystemEnvironment_ObjectIdentity = ObjectIdentity
aixSystemEnvironment = _AixSystemEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2)
)


class _AixSeCPUUtilization_Type(Integer32):
    """Custom type aixSeCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixSeCPUUtilization_Type.__name__ = "Integer32"
_AixSeCPUUtilization_Object = MibScalar
aixSeCPUUtilization = _AixSeCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2, 1),
    _AixSeCPUUtilization_Type()
)
aixSeCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeCPUUtilization.setStatus("current")


class _AixSeCPUThreshold_Type(Integer32):
    """Custom type aixSeCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixSeCPUThreshold_Type.__name__ = "Integer32"
_AixSeCPUThreshold_Object = MibScalar
aixSeCPUThreshold = _AixSeCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2, 2),
    _AixSeCPUThreshold_Type()
)
aixSeCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeCPUThreshold.setStatus("current")


class _AixSeSystemRunLevel_Type(Integer32):
    """Custom type aixSeSystemRunLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("level0", 1),
          ("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("level4", 5),
          ("level5", 6),
          ("level6", 7),
          ("level7", 8),
          ("level8", 9),
          ("level9", 10),
          ("levelm", 11))
    )


_AixSeSystemRunLevel_Type.__name__ = "Integer32"
_AixSeSystemRunLevel_Object = MibScalar
aixSeSystemRunLevel = _AixSeSystemRunLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2, 3),
    _AixSeSystemRunLevel_Type()
)
aixSeSystemRunLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeSystemRunLevel.setStatus("current")


class _AixSeSystemState_Type(Integer32):
    """Custom type aixSeSystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 2),
          ("running", 1),
          ("shutdown", 3))
    )


_AixSeSystemState_Type.__name__ = "Integer32"
_AixSeSystemState_Object = MibScalar
aixSeSystemState = _AixSeSystemState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2, 4),
    _AixSeSystemState_Type()
)
aixSeSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeSystemState.setStatus("current")


class _AixSeSystemTrap_Type(Integer32):
    """Custom type aixSeSystemTrap based on Integer32"""
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


_AixSeSystemTrap_Type.__name__ = "Integer32"
_AixSeSystemTrap_Object = MibScalar
aixSeSystemTrap = _AixSeSystemTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 2, 5),
    _AixSeSystemTrap_Type()
)
aixSeSystemTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeSystemTrap.setStatus("current")
_AixAuxSystemEnvironment_ObjectIdentity = ObjectIdentity
aixAuxSystemEnvironment = _AixAuxSystemEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3)
)
_AixSeDateAndTime_Type = DisplayString
_AixSeDateAndTime_Object = MibScalar
aixSeDateAndTime = _AixSeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 1),
    _AixSeDateAndTime_Type()
)
aixSeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeDateAndTime.setStatus("current")


class _AixSeMaxProcPerUser_Type(Integer32):
    """Custom type aixSeMaxProcPerUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixSeMaxProcPerUser_Type.__name__ = "Integer32"
_AixSeMaxProcPerUser_Object = MibScalar
aixSeMaxProcPerUser = _AixSeMaxProcPerUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 2),
    _AixSeMaxProcPerUser_Type()
)
aixSeMaxProcPerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeMaxProcPerUser.setStatus("current")


class _AixSeLicenseNum_Type(Integer32):
    """Custom type aixSeLicenseNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AixSeLicenseNum_Type.__name__ = "Integer32"
_AixSeLicenseNum_Object = MibScalar
aixSeLicenseNum = _AixSeLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 3),
    _AixSeLicenseNum_Type()
)
aixSeLicenseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSeLicenseNum.setStatus("current")


class _AixSeRemainingLicenseNum_Type(Integer32):
    """Custom type aixSeRemainingLicenseNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AixSeRemainingLicenseNum_Type.__name__ = "Integer32"
_AixSeRemainingLicenseNum_Object = MibScalar
aixSeRemainingLicenseNum = _AixSeRemainingLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 4),
    _AixSeRemainingLicenseNum_Type()
)
aixSeRemainingLicenseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeRemainingLicenseNum.setStatus("current")


class _AixSeNumCPUs_Type(Integer32):
    """Custom type aixSeNumCPUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixSeNumCPUs_Type.__name__ = "Integer32"
_AixSeNumCPUs_Object = MibScalar
aixSeNumCPUs = _AixSeNumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 5),
    _AixSeNumCPUs_Type()
)
aixSeNumCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeNumCPUs.setStatus("current")
_AixSeMachineType_Type = DisplayString
_AixSeMachineType_Object = MibScalar
aixSeMachineType = _AixSeMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 6),
    _AixSeMachineType_Type()
)
aixSeMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeMachineType.setStatus("current")
_AixSeSerialNumber_Type = DisplayString
_AixSeSerialNumber_Object = MibScalar
aixSeSerialNumber = _AixSeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 3, 7),
    _AixSeSerialNumber_Type()
)
aixSeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSeSerialNumber.setStatus("current")
_AixTrap_ObjectIdentity = ObjectIdentity
aixTrap = _AixTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4)
)
_AixGeneralTrap_ObjectIdentity = ObjectIdentity
aixGeneralTrap = _AixGeneralTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 6)
)
_AixStorageSystem_ObjectIdentity = ObjectIdentity
aixStorageSystem = _AixStorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2)
)
_AixVolumeGroup_ObjectIdentity = ObjectIdentity
aixVolumeGroup = _AixVolumeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1)
)


class _AixVgThreshold_Type(Integer32):
    """Custom type aixVgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixVgThreshold_Type.__name__ = "Integer32"
_AixVgThreshold_Object = MibScalar
aixVgThreshold = _AixVgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 1),
    _AixVgThreshold_Type()
)
aixVgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixVgThreshold.setStatus("current")
_AixVgTable_Object = MibTable
aixVgTable = _AixVgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aixVgTable.setStatus("current")
_AixVgEntry_Object = MibTableRow
aixVgEntry = _AixVgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1)
)
aixVgEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixVgIndex"),
)
if mibBuilder.loadTexts:
    aixVgEntry.setStatus("current")
_AixVgName_Type = DisplayString
_AixVgName_Object = MibTableColumn
aixVgName = _AixVgName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 1),
    _AixVgName_Type()
)
aixVgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgName.setStatus("current")
_AixVgIdentifier_Type = DisplayString
_AixVgIdentifier_Object = MibTableColumn
aixVgIdentifier = _AixVgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 2),
    _AixVgIdentifier_Type()
)
aixVgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgIdentifier.setStatus("current")


class _AixVgState_Type(Integer32):
    """Custom type aixVgState based on Integer32"""
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
        *(("activeComplete", 1),
          ("activePartial", 2),
          ("inactive", 3),
          ("unknown", 4))
    )


_AixVgState_Type.__name__ = "Integer32"
_AixVgState_Object = MibTableColumn
aixVgState = _AixVgState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 3),
    _AixVgState_Type()
)
aixVgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgState.setStatus("current")


class _AixVgSize_Type(Integer32):
    """Custom type aixVgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgSize_Type.__name__ = "Integer32"
_AixVgSize_Object = MibTableColumn
aixVgSize = _AixVgSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 4),
    _AixVgSize_Type()
)
aixVgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgSize.setStatus("current")
if mibBuilder.loadTexts:
    aixVgSize.setUnits("megabytes")


class _AixVgFree_Type(Integer32):
    """Custom type aixVgFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgFree_Type.__name__ = "Integer32"
_AixVgFree_Object = MibTableColumn
aixVgFree = _AixVgFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 5),
    _AixVgFree_Type()
)
aixVgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgFree.setStatus("current")
if mibBuilder.loadTexts:
    aixVgFree.setUnits("megabytes")


class _AixVgCurNumLVs_Type(Integer32):
    """Custom type aixVgCurNumLVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgCurNumLVs_Type.__name__ = "Integer32"
_AixVgCurNumLVs_Object = MibTableColumn
aixVgCurNumLVs = _AixVgCurNumLVs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 6),
    _AixVgCurNumLVs_Type()
)
aixVgCurNumLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgCurNumLVs.setStatus("current")


class _AixVgOpenLVs_Type(Integer32):
    """Custom type aixVgOpenLVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgOpenLVs_Type.__name__ = "Integer32"
_AixVgOpenLVs_Object = MibTableColumn
aixVgOpenLVs = _AixVgOpenLVs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 7),
    _AixVgOpenLVs_Type()
)
aixVgOpenLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgOpenLVs.setStatus("current")


class _AixVgActivePVs_Type(Integer32):
    """Custom type aixVgActivePVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixVgActivePVs_Type.__name__ = "Integer32"
_AixVgActivePVs_Object = MibTableColumn
aixVgActivePVs = _AixVgActivePVs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 8),
    _AixVgActivePVs_Type()
)
aixVgActivePVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgActivePVs.setStatus("current")


class _AixVgIndex_Type(Integer32):
    """Custom type aixVgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixVgIndex_Type.__name__ = "Integer32"
_AixVgIndex_Object = MibTableColumn
aixVgIndex = _AixVgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 1, 2, 1, 9),
    _AixVgIndex_Type()
)
aixVgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixVgIndex.setStatus("current")
_AixLogicalVolume_ObjectIdentity = ObjectIdentity
aixLogicalVolume = _AixLogicalVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2)
)
_AixLvTable_Object = MibTable
aixLvTable = _AixLvTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aixLvTable.setStatus("current")
_AixLvEntry_Object = MibTableRow
aixLvEntry = _AixLvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1)
)
aixLvEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixLvIndex"),
)
if mibBuilder.loadTexts:
    aixLvEntry.setStatus("current")
_AixLvName_Type = DisplayString
_AixLvName_Object = MibTableColumn
aixLvName = _AixLvName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 1),
    _AixLvName_Type()
)
aixLvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvName.setStatus("current")
_AixLvNameVG_Type = DisplayString
_AixLvNameVG_Object = MibTableColumn
aixLvNameVG = _AixLvNameVG_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 2),
    _AixLvNameVG_Type()
)
aixLvNameVG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvNameVG.setStatus("current")


class _AixLvType_Type(Integer32):
    """Custom type aixLvType based on Integer32"""
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
        *(("boot", 4),
          ("jfs", 1),
          ("jfs2", 5),
          ("jfs2log", 6),
          ("jfslog", 2),
          ("other", 7),
          ("paging", 3))
    )


_AixLvType_Type.__name__ = "Integer32"
_AixLvType_Object = MibTableColumn
aixLvType = _AixLvType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 3),
    _AixLvType_Type()
)
aixLvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixLvType.setStatus("current")
_AixLvMountPoint_Type = DisplayString
_AixLvMountPoint_Object = MibTableColumn
aixLvMountPoint = _AixLvMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 4),
    _AixLvMountPoint_Type()
)
aixLvMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvMountPoint.setStatus("current")


class _AixLvSize_Type(Integer32):
    """Custom type aixLvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixLvSize_Type.__name__ = "Integer32"
_AixLvSize_Object = MibTableColumn
aixLvSize = _AixLvSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 5),
    _AixLvSize_Type()
)
aixLvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvSize.setStatus("current")
if mibBuilder.loadTexts:
    aixLvSize.setUnits("megabytes")


class _AixLvState_Type(Integer32):
    """Custom type aixLvState based on Integer32"""
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
        *(("closeStale", 3),
          ("closeSyncd", 4),
          ("openStale", 1),
          ("openSyncd", 2),
          ("undefined", 5))
    )


_AixLvState_Type.__name__ = "Integer32"
_AixLvState_Object = MibTableColumn
aixLvState = _AixLvState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 6),
    _AixLvState_Type()
)
aixLvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvState.setStatus("current")


class _AixLvIndex_Type(Integer32):
    """Custom type aixLvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixLvIndex_Type.__name__ = "Integer32"
_AixLvIndex_Object = MibTableColumn
aixLvIndex = _AixLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 2, 1, 1, 7),
    _AixLvIndex_Type()
)
aixLvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLvIndex.setStatus("current")
_AixPhysicalVolume_ObjectIdentity = ObjectIdentity
aixPhysicalVolume = _AixPhysicalVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3)
)
_AixPvTable_Object = MibTable
aixPvTable = _AixPvTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1)
)
if mibBuilder.loadTexts:
    aixPvTable.setStatus("current")
_AixPvEntry_Object = MibTableRow
aixPvEntry = _AixPvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1)
)
aixPvEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixPvIndex"),
)
if mibBuilder.loadTexts:
    aixPvEntry.setStatus("current")
_AixPvName_Type = DisplayString
_AixPvName_Object = MibTableColumn
aixPvName = _AixPvName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 1),
    _AixPvName_Type()
)
aixPvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvName.setStatus("current")
_AixPvNameVG_Type = DisplayString
_AixPvNameVG_Object = MibTableColumn
aixPvNameVG = _AixPvNameVG_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 2),
    _AixPvNameVG_Type()
)
aixPvNameVG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvNameVG.setStatus("current")


class _AixPvState_Type(Integer32):
    """Custom type aixPvState based on Integer32"""
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
        *(("active", 1),
          ("missing", 2),
          ("removed", 3),
          ("variedOff", 4))
    )


_AixPvState_Type.__name__ = "Integer32"
_AixPvState_Object = MibTableColumn
aixPvState = _AixPvState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 3),
    _AixPvState_Type()
)
aixPvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvState.setStatus("current")


class _AixPvSize_Type(Integer32):
    """Custom type aixPvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixPvSize_Type.__name__ = "Integer32"
_AixPvSize_Object = MibTableColumn
aixPvSize = _AixPvSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 4),
    _AixPvSize_Type()
)
aixPvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvSize.setStatus("current")
if mibBuilder.loadTexts:
    aixPvSize.setUnits("megabytes")


class _AixPvFree_Type(Integer32):
    """Custom type aixPvFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixPvFree_Type.__name__ = "Integer32"
_AixPvFree_Object = MibTableColumn
aixPvFree = _AixPvFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 5),
    _AixPvFree_Type()
)
aixPvFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvFree.setStatus("current")
if mibBuilder.loadTexts:
    aixPvFree.setUnits("megabytes")


class _AixPvNumLVs_Type(Integer32):
    """Custom type aixPvNumLVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixPvNumLVs_Type.__name__ = "Integer32"
_AixPvNumLVs_Object = MibTableColumn
aixPvNumLVs = _AixPvNumLVs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 6),
    _AixPvNumLVs_Type()
)
aixPvNumLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvNumLVs.setStatus("current")


class _AixPvIndex_Type(Integer32):
    """Custom type aixPvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixPvIndex_Type.__name__ = "Integer32"
_AixPvIndex_Object = MibTableColumn
aixPvIndex = _AixPvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 3, 1, 1, 7),
    _AixPvIndex_Type()
)
aixPvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPvIndex.setStatus("current")
_AixPagingSpace_ObjectIdentity = ObjectIdentity
aixPagingSpace = _AixPagingSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4)
)


class _AixPageThreshold_Type(Integer32):
    """Custom type aixPageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixPageThreshold_Type.__name__ = "Integer32"
_AixPageThreshold_Object = MibScalar
aixPageThreshold = _AixPageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 1),
    _AixPageThreshold_Type()
)
aixPageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixPageThreshold.setStatus("current")
_AixPageTable_Object = MibTable
aixPageTable = _AixPageTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2)
)
if mibBuilder.loadTexts:
    aixPageTable.setStatus("current")
_AixPageEntry_Object = MibTableRow
aixPageEntry = _AixPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1)
)
aixPageEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixPageIndex"),
)
if mibBuilder.loadTexts:
    aixPageEntry.setStatus("current")
_AixPageName_Type = DisplayString
_AixPageName_Object = MibTableColumn
aixPageName = _AixPageName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 1),
    _AixPageName_Type()
)
aixPageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageName.setStatus("current")
_AixPageNameVG_Type = DisplayString
_AixPageNameVG_Object = MibTableColumn
aixPageNameVG = _AixPageNameVG_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 2),
    _AixPageNameVG_Type()
)
aixPageNameVG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageNameVG.setStatus("current")
_AixPageNamePV_Type = DisplayString
_AixPageNamePV_Object = MibTableColumn
aixPageNamePV = _AixPageNamePV_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 3),
    _AixPageNamePV_Type()
)
aixPageNamePV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageNamePV.setStatus("current")


class _AixPageSize_Type(Integer32):
    """Custom type aixPageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixPageSize_Type.__name__ = "Integer32"
_AixPageSize_Object = MibTableColumn
aixPageSize = _AixPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 4),
    _AixPageSize_Type()
)
aixPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageSize.setStatus("current")
if mibBuilder.loadTexts:
    aixPageSize.setUnits("megabytes")


class _AixPagePercentUsed_Type(Integer32):
    """Custom type aixPagePercentUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixPagePercentUsed_Type.__name__ = "Integer32"
_AixPagePercentUsed_Object = MibTableColumn
aixPagePercentUsed = _AixPagePercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 5),
    _AixPagePercentUsed_Type()
)
aixPagePercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPagePercentUsed.setStatus("current")


class _AixPageStatus_Type(Integer32):
    """Custom type aixPageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_AixPageStatus_Type.__name__ = "Integer32"
_AixPageStatus_Object = MibTableColumn
aixPageStatus = _AixPageStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 6),
    _AixPageStatus_Type()
)
aixPageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageStatus.setStatus("current")


class _AixPageType_Type(Integer32):
    """Custom type aixPageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lv", 1),
          ("nfs", 2),
          ("other", 3))
    )


_AixPageType_Type.__name__ = "Integer32"
_AixPageType_Object = MibTableColumn
aixPageType = _AixPageType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 7),
    _AixPageType_Type()
)
aixPageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageType.setStatus("current")


class _AixPageIndex_Type(Integer32):
    """Custom type aixPageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixPageIndex_Type.__name__ = "Integer32"
_AixPageIndex_Object = MibTableColumn
aixPageIndex = _AixPageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 2, 4, 2, 1, 8),
    _AixPageIndex_Type()
)
aixPageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPageIndex.setStatus("current")
_AixPrintSystem_ObjectIdentity = ObjectIdentity
aixPrintSystem = _AixPrintSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3)
)
_AixPrtQueue_ObjectIdentity = ObjectIdentity
aixPrtQueue = _AixPrtQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1)
)
_AixPrtQueTable_Object = MibTable
aixPrtQueTable = _AixPrtQueTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aixPrtQueTable.setStatus("current")
_AixPrtQueEntry_Object = MibTableRow
aixPrtQueEntry = _AixPrtQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1)
)
aixPrtQueEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixPrtQueIndex"),
)
if mibBuilder.loadTexts:
    aixPrtQueEntry.setStatus("current")
_AixPrtQueName_Type = DisplayString
_AixPrtQueName_Object = MibTableColumn
aixPrtQueName = _AixPrtQueName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 1),
    _AixPrtQueName_Type()
)
aixPrtQueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueName.setStatus("current")
_AixPrtQueDevice_Type = DisplayString
_AixPrtQueDevice_Object = MibTableColumn
aixPrtQueDevice = _AixPrtQueDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 2),
    _AixPrtQueDevice_Type()
)
aixPrtQueDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueDevice.setStatus("current")


class _AixPrtQueStatus_Type(Integer32):
    """Custom type aixPrtQueStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("busy", 10),
          ("connect", 9),
          ("gethost", 8),
          ("init", 6),
          ("off", 4),
          ("oprwait", 5),
          ("ready", 1),
          ("running", 2),
          ("sending", 7),
          ("waiting", 3))
    )


_AixPrtQueStatus_Type.__name__ = "Integer32"
_AixPrtQueStatus_Object = MibTableColumn
aixPrtQueStatus = _AixPrtQueStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 3),
    _AixPrtQueStatus_Type()
)
aixPrtQueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueStatus.setStatus("current")


class _AixPrtQueAction_Type(Integer32):
    """Custom type aixPrtQueAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("start", 2),
          ("stop", 3))
    )


_AixPrtQueAction_Type.__name__ = "Integer32"
_AixPrtQueAction_Object = MibTableColumn
aixPrtQueAction = _AixPrtQueAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 4),
    _AixPrtQueAction_Type()
)
aixPrtQueAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixPrtQueAction.setStatus("current")
_AixPrtQueDescipline_Type = DisplayString
_AixPrtQueDescipline_Object = MibTableColumn
aixPrtQueDescipline = _AixPrtQueDescipline_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 5),
    _AixPrtQueDescipline_Type()
)
aixPrtQueDescipline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueDescipline.setStatus("current")
_AixPrtQueAcctFile_Type = DisplayString
_AixPrtQueAcctFile_Object = MibTableColumn
aixPrtQueAcctFile = _AixPrtQueAcctFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 6),
    _AixPrtQueAcctFile_Type()
)
aixPrtQueAcctFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueAcctFile.setStatus("current")
_AixPrtQueHost_Type = DisplayString
_AixPrtQueHost_Object = MibTableColumn
aixPrtQueHost = _AixPrtQueHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 7),
    _AixPrtQueHost_Type()
)
aixPrtQueHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueHost.setStatus("current")
_AixPrtQueRQ_Type = DisplayString
_AixPrtQueRQ_Object = MibTableColumn
aixPrtQueRQ = _AixPrtQueRQ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 8),
    _AixPrtQueRQ_Type()
)
aixPrtQueRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueRQ.setStatus("current")


class _AixPrtQueJobNum_Type(Integer32):
    """Custom type aixPrtQueJobNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixPrtQueJobNum_Type.__name__ = "Integer32"
_AixPrtQueJobNum_Object = MibTableColumn
aixPrtQueJobNum = _AixPrtQueJobNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 9),
    _AixPrtQueJobNum_Type()
)
aixPrtQueJobNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueJobNum.setStatus("current")


class _AixPrtQueIndex_Type(Integer32):
    """Custom type aixPrtQueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixPrtQueIndex_Type.__name__ = "Integer32"
_AixPrtQueIndex_Object = MibTableColumn
aixPrtQueIndex = _AixPrtQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 3, 1, 1, 1, 10),
    _AixPrtQueIndex_Type()
)
aixPrtQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrtQueIndex.setStatus("current")
_AixUser_ObjectIdentity = ObjectIdentity
aixUser = _AixUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4)
)
_AixUsers_ObjectIdentity = ObjectIdentity
aixUsers = _AixUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1)
)
_AixUsrTable_Object = MibTable
aixUsrTable = _AixUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aixUsrTable.setStatus("current")
_AixUsrEntry_Object = MibTableRow
aixUsrEntry = _AixUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1)
)
aixUsrEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixUsrIndex"),
)
if mibBuilder.loadTexts:
    aixUsrEntry.setStatus("current")
_AixUsrName_Type = DisplayString
_AixUsrName_Object = MibTableColumn
aixUsrName = _AixUsrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 1),
    _AixUsrName_Type()
)
aixUsrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixUsrName.setStatus("current")
_AixUsrID_Type = Integer32
_AixUsrID_Object = MibTableColumn
aixUsrID = _AixUsrID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 2),
    _AixUsrID_Type()
)
aixUsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrID.setStatus("current")
_AixUsrHome_Type = DisplayString
_AixUsrHome_Object = MibTableColumn
aixUsrHome = _AixUsrHome_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 3),
    _AixUsrHome_Type()
)
aixUsrHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrHome.setStatus("current")
_AixUsrShell_Type = DisplayString
_AixUsrShell_Object = MibTableColumn
aixUsrShell = _AixUsrShell_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 4),
    _AixUsrShell_Type()
)
aixUsrShell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrShell.setStatus("current")


class _AixUsrLocalLogin_Type(Integer32):
    """Custom type aixUsrLocalLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AixUsrLocalLogin_Type.__name__ = "Integer32"
_AixUsrLocalLogin_Object = MibTableColumn
aixUsrLocalLogin = _AixUsrLocalLogin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 5),
    _AixUsrLocalLogin_Type()
)
aixUsrLocalLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrLocalLogin.setStatus("current")


class _AixUsrRemoteLogin_Type(Integer32):
    """Custom type aixUsrRemoteLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AixUsrRemoteLogin_Type.__name__ = "Integer32"
_AixUsrRemoteLogin_Object = MibTableColumn
aixUsrRemoteLogin = _AixUsrRemoteLogin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 6),
    _AixUsrRemoteLogin_Type()
)
aixUsrRemoteLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrRemoteLogin.setStatus("current")


class _AixUsrPasswdMaxAge_Type(Integer32):
    """Custom type aixUsrPasswdMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AixUsrPasswdMaxAge_Type.__name__ = "Integer32"
_AixUsrPasswdMaxAge_Object = MibTableColumn
aixUsrPasswdMaxAge = _AixUsrPasswdMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 7),
    _AixUsrPasswdMaxAge_Type()
)
aixUsrPasswdMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrPasswdMaxAge.setStatus("current")


class _AixUsrStatus_Type(Integer32):
    """Custom type aixUsrStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("error", 5),
          ("locked", 2),
          ("unlocked", 1))
    )


_AixUsrStatus_Type.__name__ = "Integer32"
_AixUsrStatus_Object = MibTableColumn
aixUsrStatus = _AixUsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 8),
    _AixUsrStatus_Type()
)
aixUsrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrStatus.setStatus("current")
_AixUsrGroups_Type = DisplayString
_AixUsrGroups_Object = MibTableColumn
aixUsrGroups = _AixUsrGroups_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 9),
    _AixUsrGroups_Type()
)
aixUsrGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixUsrGroups.setStatus("current")
_AixUsrAllowableAttempts_Type = Integer32
_AixUsrAllowableAttempts_Object = MibTableColumn
aixUsrAllowableAttempts = _AixUsrAllowableAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 10),
    _AixUsrAllowableAttempts_Type()
)
aixUsrAllowableAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrAllowableAttempts.setStatus("current")


class _AixUsrResetLoginCount_Type(Integer32):
    """Custom type aixUsrResetLoginCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AixUsrResetLoginCount_Type.__name__ = "Integer32"
_AixUsrResetLoginCount_Object = MibTableColumn
aixUsrResetLoginCount = _AixUsrResetLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 11),
    _AixUsrResetLoginCount_Type()
)
aixUsrResetLoginCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrResetLoginCount.setStatus("current")
_AixUsrPrimaryGroup_Type = DisplayString
_AixUsrPrimaryGroup_Object = MibTableColumn
aixUsrPrimaryGroup = _AixUsrPrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 12),
    _AixUsrPrimaryGroup_Type()
)
aixUsrPrimaryGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixUsrPrimaryGroup.setStatus("current")


class _AixUsrIndex_Type(Integer32):
    """Custom type aixUsrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixUsrIndex_Type.__name__ = "Integer32"
_AixUsrIndex_Object = MibTableColumn
aixUsrIndex = _AixUsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 1, 1, 1, 13),
    _AixUsrIndex_Type()
)
aixUsrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixUsrIndex.setStatus("current")
_AixGroups_ObjectIdentity = ObjectIdentity
aixGroups = _AixGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2)
)
_AixGrpTable_Object = MibTable
aixGrpTable = _AixGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1)
)
if mibBuilder.loadTexts:
    aixGrpTable.setStatus("current")
_AixGrpEntry_Object = MibTableRow
aixGrpEntry = _AixGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1)
)
aixGrpEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixGrpIndex"),
)
if mibBuilder.loadTexts:
    aixGrpEntry.setStatus("current")


class _AixGrpIndex_Type(Integer32):
    """Custom type aixGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixGrpIndex_Type.__name__ = "Integer32"
_AixGrpIndex_Object = MibTableColumn
aixGrpIndex = _AixGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 1),
    _AixGrpIndex_Type()
)
aixGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpIndex.setStatus("current")
_AixGrpName_Type = DisplayString
_AixGrpName_Object = MibTableColumn
aixGrpName = _AixGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 2),
    _AixGrpName_Type()
)
aixGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpName.setStatus("current")


class _AixGrpID_Type(Integer32):
    """Custom type aixGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AixGrpID_Type.__name__ = "Integer32"
_AixGrpID_Object = MibTableColumn
aixGrpID = _AixGrpID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 3),
    _AixGrpID_Type()
)
aixGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpID.setStatus("current")


class _AixGrpAdminGroup_Type(Integer32):
    """Custom type aixGrpAdminGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AixGrpAdminGroup_Type.__name__ = "Integer32"
_AixGrpAdminGroup_Object = MibTableColumn
aixGrpAdminGroup = _AixGrpAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 4),
    _AixGrpAdminGroup_Type()
)
aixGrpAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpAdminGroup.setStatus("current")
_AixGrpUsrList_Type = DisplayString
_AixGrpUsrList_Object = MibTableColumn
aixGrpUsrList = _AixGrpUsrList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 5),
    _AixGrpUsrList_Type()
)
aixGrpUsrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpUsrList.setStatus("current")
_AixGrpAdmList_Type = DisplayString
_AixGrpAdmList_Object = MibTableColumn
aixGrpAdmList = _AixGrpAdmList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 4, 2, 1, 1, 6),
    _AixGrpAdmList_Type()
)
aixGrpAdmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixGrpAdmList.setStatus("current")
_AixService_ObjectIdentity = ObjectIdentity
aixService = _AixService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5)
)
_AixSrvSubsystem_ObjectIdentity = ObjectIdentity
aixSrvSubsystem = _AixSrvSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1)
)


class _AixSubSystemNum_Type(Integer32):
    """Custom type aixSubSystemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixSubSystemNum_Type.__name__ = "Integer32"
_AixSubSystemNum_Object = MibScalar
aixSubSystemNum = _AixSubSystemNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 1),
    _AixSubSystemNum_Type()
)
aixSubSystemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSystemNum.setStatus("current")
_AixSubSysTable_Object = MibTable
aixSubSysTable = _AixSubSysTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2)
)
if mibBuilder.loadTexts:
    aixSubSysTable.setStatus("current")
_AixSubSysEntry_Object = MibTableRow
aixSubSysEntry = _AixSubSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1)
)
aixSubSysEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixSubSysIndex"),
)
if mibBuilder.loadTexts:
    aixSubSysEntry.setStatus("current")
_AixSubSysName_Type = DisplayString
_AixSubSysName_Object = MibTableColumn
aixSubSysName = _AixSubSysName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1, 1),
    _AixSubSysName_Type()
)
aixSubSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSysName.setStatus("current")
_AixSubSysGroup_Type = DisplayString
_AixSubSysGroup_Object = MibTableColumn
aixSubSysGroup = _AixSubSysGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1, 2),
    _AixSubSysGroup_Type()
)
aixSubSysGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSysGroup.setStatus("current")


class _AixSubSysPID_Type(Integer32):
    """Custom type aixSubSysPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixSubSysPID_Type.__name__ = "Integer32"
_AixSubSysPID_Object = MibTableColumn
aixSubSysPID = _AixSubSysPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1, 3),
    _AixSubSysPID_Type()
)
aixSubSysPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSysPID.setStatus("current")


class _AixSubSysStatus_Type(Integer32):
    """Custom type aixSubSysStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inoperative", 2))
    )


_AixSubSysStatus_Type.__name__ = "Integer32"
_AixSubSysStatus_Object = MibTableColumn
aixSubSysStatus = _AixSubSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1, 4),
    _AixSubSysStatus_Type()
)
aixSubSysStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixSubSysStatus.setStatus("current")


class _AixSubSysIndex_Type(Integer32):
    """Custom type aixSubSysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixSubSysIndex_Type.__name__ = "Integer32"
_AixSubSysIndex_Object = MibTableColumn
aixSubSysIndex = _AixSubSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 1, 2, 1, 5),
    _AixSubSysIndex_Type()
)
aixSubSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSysIndex.setStatus("current")
_AixSrvSubserver_ObjectIdentity = ObjectIdentity
aixSrvSubserver = _AixSrvSubserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2)
)


class _AixSubSrvNum_Type(Integer32):
    """Custom type aixSubSrvNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixSubSrvNum_Type.__name__ = "Integer32"
_AixSubSrvNum_Object = MibScalar
aixSubSrvNum = _AixSubSrvNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 1),
    _AixSubSrvNum_Type()
)
aixSubSrvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvNum.setStatus("current")
_AixSubSrvTable_Object = MibTable
aixSubSrvTable = _AixSubSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2)
)
if mibBuilder.loadTexts:
    aixSubSrvTable.setStatus("current")
_AixSubSrvEntry_Object = MibTableRow
aixSubSrvEntry = _AixSubSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1)
)
aixSubSrvEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixSubSrvIndex"),
)
if mibBuilder.loadTexts:
    aixSubSrvEntry.setStatus("current")
_AixSubSrvName_Type = DisplayString
_AixSubSrvName_Object = MibTableColumn
aixSubSrvName = _AixSubSrvName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 1),
    _AixSubSrvName_Type()
)
aixSubSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvName.setStatus("current")
_AixSubSrvDescr_Type = DisplayString
_AixSubSrvDescr_Object = MibTableColumn
aixSubSrvDescr = _AixSubSrvDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 2),
    _AixSubSrvDescr_Type()
)
aixSubSrvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvDescr.setStatus("current")
_AixSubSrvCommand_Type = DisplayString
_AixSubSrvCommand_Object = MibTableColumn
aixSubSrvCommand = _AixSubSrvCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 3),
    _AixSubSrvCommand_Type()
)
aixSubSrvCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvCommand.setStatus("current")


class _AixSubSrvStatus_Type(Integer32):
    """Custom type aixSubSrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inoperative", 2))
    )


_AixSubSrvStatus_Type.__name__ = "Integer32"
_AixSubSrvStatus_Object = MibTableColumn
aixSubSrvStatus = _AixSubSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 4),
    _AixSubSrvStatus_Type()
)
aixSubSrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvStatus.setStatus("current")
_AixSubSrvSubsys_Type = DisplayString
_AixSubSrvSubsys_Object = MibTableColumn
aixSubSrvSubsys = _AixSubSrvSubsys_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 5),
    _AixSubSrvSubsys_Type()
)
aixSubSrvSubsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvSubsys.setStatus("current")


class _AixSubSrvIndex_Type(Integer32):
    """Custom type aixSubSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixSubSrvIndex_Type.__name__ = "Integer32"
_AixSubSrvIndex_Object = MibTableColumn
aixSubSrvIndex = _AixSubSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 5, 2, 2, 1, 6),
    _AixSubSrvIndex_Type()
)
aixSubSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixSubSrvIndex.setStatus("current")
_AixFileSystem_ObjectIdentity = ObjectIdentity
aixFileSystem = _AixFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6)
)


class _AixFsThreshold_Type(Integer32):
    """Custom type aixFsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AixFsThreshold_Type.__name__ = "Integer32"
_AixFsThreshold_Object = MibScalar
aixFsThreshold = _AixFsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 1),
    _AixFsThreshold_Type()
)
aixFsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixFsThreshold.setStatus("current")
_AixFsTable_Object = MibTable
aixFsTable = _AixFsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2)
)
if mibBuilder.loadTexts:
    aixFsTable.setStatus("current")
_AixFsTableEntry_Object = MibTableRow
aixFsTableEntry = _AixFsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1)
)
aixFsTableEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixFsIndex"),
)
if mibBuilder.loadTexts:
    aixFsTableEntry.setStatus("current")


class _AixFsIndex_Type(Integer32):
    """Custom type aixFsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixFsIndex_Type.__name__ = "Integer32"
_AixFsIndex_Object = MibTableColumn
aixFsIndex = _AixFsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 1),
    _AixFsIndex_Type()
)
aixFsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsIndex.setStatus("current")
_AixFsName_Type = DisplayString
_AixFsName_Object = MibTableColumn
aixFsName = _AixFsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 2),
    _AixFsName_Type()
)
aixFsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsName.setStatus("current")
_AixFsMountPoint_Type = DisplayString
_AixFsMountPoint_Object = MibTableColumn
aixFsMountPoint = _AixFsMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 3),
    _AixFsMountPoint_Type()
)
aixFsMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsMountPoint.setStatus("current")


class _AixFsType_Type(Integer32):
    """Custom type aixFsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("afs", 7),
          ("autofs", 6),
          ("cachefs", 5),
          ("cdrfs", 3),
          ("dfs", 8),
          ("jfs", 1),
          ("jfs2", 2),
          ("nfs", 9),
          ("nfs3", 10),
          ("other", 11),
          ("procfs", 4))
    )


_AixFsType_Type.__name__ = "Integer32"
_AixFsType_Object = MibTableColumn
aixFsType = _AixFsType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 4),
    _AixFsType_Type()
)
aixFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsType.setStatus("current")


class _AixFsSize_Type(Integer32):
    """Custom type aixFsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFsSize_Type.__name__ = "Integer32"
_AixFsSize_Object = MibTableColumn
aixFsSize = _AixFsSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 5),
    _AixFsSize_Type()
)
aixFsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixFsSize.setStatus("current")
if mibBuilder.loadTexts:
    aixFsSize.setUnits("megabytes")


class _AixFsFree_Type(Integer32):
    """Custom type aixFsFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFsFree_Type.__name__ = "Integer32"
_AixFsFree_Object = MibTableColumn
aixFsFree = _AixFsFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 6),
    _AixFsFree_Type()
)
aixFsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsFree.setStatus("current")
if mibBuilder.loadTexts:
    aixFsFree.setUnits("megabytes")


class _AixFsNumINodes_Type(Integer32):
    """Custom type aixFsNumINodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFsNumINodes_Type.__name__ = "Integer32"
_AixFsNumINodes_Object = MibTableColumn
aixFsNumINodes = _AixFsNumINodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 7),
    _AixFsNumINodes_Type()
)
aixFsNumINodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsNumINodes.setStatus("current")


class _AixFsUsedInodes_Type(Integer32):
    """Custom type aixFsUsedInodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFsUsedInodes_Type.__name__ = "Integer32"
_AixFsUsedInodes_Object = MibTableColumn
aixFsUsedInodes = _AixFsUsedInodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 8),
    _AixFsUsedInodes_Type()
)
aixFsUsedInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsUsedInodes.setStatus("current")


class _AixFsStatus_Type(Integer32):
    """Custom type aixFsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mounted", 1),
          ("unmounted", 2))
    )


_AixFsStatus_Type.__name__ = "Integer32"
_AixFsStatus_Object = MibTableColumn
aixFsStatus = _AixFsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 9),
    _AixFsStatus_Type()
)
aixFsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsStatus.setStatus("current")


class _AixFsExecution_Type(Integer32):
    """Custom type aixFsExecution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mount", 2),
          ("other", 1),
          ("unmount", 3))
    )


_AixFsExecution_Type.__name__ = "Integer32"
_AixFsExecution_Object = MibTableColumn
aixFsExecution = _AixFsExecution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 10),
    _AixFsExecution_Type()
)
aixFsExecution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixFsExecution.setStatus("current")
_AixFsResultMsg_Type = DisplayString
_AixFsResultMsg_Object = MibTableColumn
aixFsResultMsg = _AixFsResultMsg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 6, 2, 1, 11),
    _AixFsResultMsg_Type()
)
aixFsResultMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixFsResultMsg.setStatus("current")
_AixProcess_ObjectIdentity = ObjectIdentity
aixProcess = _AixProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7)
)


class _AixProcNum_Type(Integer32):
    """Custom type aixProcNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcNum_Type.__name__ = "Integer32"
_AixProcNum_Object = MibScalar
aixProcNum = _AixProcNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 1),
    _AixProcNum_Type()
)
aixProcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcNum.setStatus("current")
_AixProcTable_Object = MibTable
aixProcTable = _AixProcTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2)
)
if mibBuilder.loadTexts:
    aixProcTable.setStatus("current")
_AixProcEntry_Object = MibTableRow
aixProcEntry = _AixProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1)
)
aixProcEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixProcPID"),
)
if mibBuilder.loadTexts:
    aixProcEntry.setStatus("current")


class _AixProcPID_Type(Integer32):
    """Custom type aixProcPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcPID_Type.__name__ = "Integer32"
_AixProcPID_Object = MibTableColumn
aixProcPID = _AixProcPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 1),
    _AixProcPID_Type()
)
aixProcPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcPID.setStatus("current")


class _AixProcUID_Type(Integer32):
    """Custom type aixProcUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcUID_Type.__name__ = "Integer32"
_AixProcUID_Object = MibTableColumn
aixProcUID = _AixProcUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 2),
    _AixProcUID_Type()
)
aixProcUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcUID.setStatus("current")


class _AixProcPPID_Type(Integer32):
    """Custom type aixProcPPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcPPID_Type.__name__ = "Integer32"
_AixProcPPID_Object = MibTableColumn
aixProcPPID = _AixProcPPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 3),
    _AixProcPPID_Type()
)
aixProcPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcPPID.setStatus("current")


class _AixProcGroup_Type(Integer32):
    """Custom type aixProcGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcGroup_Type.__name__ = "Integer32"
_AixProcGroup_Object = MibTableColumn
aixProcGroup = _AixProcGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 4),
    _AixProcGroup_Type()
)
aixProcGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcGroup.setStatus("current")


class _AixProcPriority_Type(Integer32):
    """Custom type aixProcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcPriority_Type.__name__ = "Integer32"
_AixProcPriority_Object = MibTableColumn
aixProcPriority = _AixProcPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 5),
    _AixProcPriority_Type()
)
aixProcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcPriority.setStatus("current")
_AixProcCMD_Type = DisplayString
_AixProcCMD_Object = MibTableColumn
aixProcCMD = _AixProcCMD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 6),
    _AixProcCMD_Type()
)
aixProcCMD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcCMD.setStatus("current")


class _AixProcCPU_Type(Integer32):
    """Custom type aixProcCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixProcCPU_Type.__name__ = "Integer32"
_AixProcCPU_Object = MibTableColumn
aixProcCPU = _AixProcCPU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 7),
    _AixProcCPU_Type()
)
aixProcCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcCPU.setStatus("current")
_AixProcStart_Type = TimeTicks
_AixProcStart_Object = MibTableColumn
aixProcStart = _AixProcStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 8),
    _AixProcStart_Type()
)
aixProcStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcStart.setStatus("current")


class _AixProcStatus_Type(Integer32):
    """Custom type aixProcStatus based on Integer32"""
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
        *(("activePS", 2),
          ("canceledPS", 5),
          ("idlePS", 4),
          ("nonexistentPS", 1),
          ("other", 7),
          ("stoppedPS", 6),
          ("swappedPS", 3))
    )


_AixProcStatus_Type.__name__ = "Integer32"
_AixProcStatus_Object = MibTableColumn
aixProcStatus = _AixProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 9),
    _AixProcStatus_Type()
)
aixProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcStatus.setStatus("current")
_AixProcTTY_Type = DisplayString
_AixProcTTY_Object = MibTableColumn
aixProcTTY = _AixProcTTY_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 7, 2, 1, 10),
    _AixProcTTY_Type()
)
aixProcTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcTTY.setStatus("current")
_AixLogin_ObjectIdentity = ObjectIdentity
aixLogin = _AixLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8)
)


class _AixFailedLoginTimePeriod_Type(Integer32):
    """Custom type aixFailedLoginTimePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixFailedLoginTimePeriod_Type.__name__ = "Integer32"
_AixFailedLoginTimePeriod_Object = MibScalar
aixFailedLoginTimePeriod = _AixFailedLoginTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 1),
    _AixFailedLoginTimePeriod_Type()
)
aixFailedLoginTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixFailedLoginTimePeriod.setStatus("current")
if mibBuilder.loadTexts:
    aixFailedLoginTimePeriod.setUnits("minutes")


class _AixLoginFailedThreshold_Type(Integer32):
    """Custom type aixLoginFailedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixLoginFailedThreshold_Type.__name__ = "Integer32"
_AixLoginFailedThreshold_Object = MibScalar
aixLoginFailedThreshold = _AixLoginFailedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 2),
    _AixLoginFailedThreshold_Type()
)
aixLoginFailedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aixLoginFailedThreshold.setStatus("current")
_AixLoginUserTable_Object = MibTable
aixLoginUserTable = _AixLoginUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3)
)
if mibBuilder.loadTexts:
    aixLoginUserTable.setStatus("current")
_AixLoginUserEntry_Object = MibTableRow
aixLoginUserEntry = _AixLoginUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1)
)
aixLoginUserEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixLoginUserIndex"),
)
if mibBuilder.loadTexts:
    aixLoginUserEntry.setStatus("current")
_AixLoginUserName_Type = DisplayString
_AixLoginUserName_Object = MibTableColumn
aixLoginUserName = _AixLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1, 1),
    _AixLoginUserName_Type()
)
aixLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLoginUserName.setStatus("current")
_AixLoginUserTTY_Type = DisplayString
_AixLoginUserTTY_Object = MibTableColumn
aixLoginUserTTY = _AixLoginUserTTY_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1, 2),
    _AixLoginUserTTY_Type()
)
aixLoginUserTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLoginUserTTY.setStatus("current")
_AixLoginUserHost_Type = DisplayString
_AixLoginUserHost_Object = MibTableColumn
aixLoginUserHost = _AixLoginUserHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1, 3),
    _AixLoginUserHost_Type()
)
aixLoginUserHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLoginUserHost.setStatus("current")
_AixLoginUserDateAndTime_Type = DisplayString
_AixLoginUserDateAndTime_Object = MibTableColumn
aixLoginUserDateAndTime = _AixLoginUserDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1, 4),
    _AixLoginUserDateAndTime_Type()
)
aixLoginUserDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLoginUserDateAndTime.setStatus("current")


class _AixLoginUserIndex_Type(Integer32):
    """Custom type aixLoginUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixLoginUserIndex_Type.__name__ = "Integer32"
_AixLoginUserIndex_Object = MibTableColumn
aixLoginUserIndex = _AixLoginUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 8, 3, 1, 5),
    _AixLoginUserIndex_Type()
)
aixLoginUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixLoginUserIndex.setStatus("current")
_AixDevice_ObjectIdentity = ObjectIdentity
aixDevice = _AixDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9)
)
_AixPrinter_ObjectIdentity = ObjectIdentity
aixPrinter = _AixPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1)
)
_AixPrinterTable_Object = MibTable
aixPrinterTable = _AixPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1)
)
if mibBuilder.loadTexts:
    aixPrinterTable.setStatus("current")
_AixPrinterEntry_Object = MibTableRow
aixPrinterEntry = _AixPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1)
)
aixPrinterEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixPrinterIndex"),
)
if mibBuilder.loadTexts:
    aixPrinterEntry.setStatus("current")
_AixPrinterName_Type = DisplayString
_AixPrinterName_Object = MibTableColumn
aixPrinterName = _AixPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 1),
    _AixPrinterName_Type()
)
aixPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterName.setStatus("current")


class _AixPrinterIndex_Type(Integer32):
    """Custom type aixPrinterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixPrinterIndex_Type.__name__ = "Integer32"
_AixPrinterIndex_Object = MibTableColumn
aixPrinterIndex = _AixPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 2),
    _AixPrinterIndex_Type()
)
aixPrinterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterIndex.setStatus("current")
_AixPrinterType_Type = DisplayString
_AixPrinterType_Object = MibTableColumn
aixPrinterType = _AixPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 3),
    _AixPrinterType_Type()
)
aixPrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterType.setStatus("current")
_AixPrinterInterface_Type = DisplayString
_AixPrinterInterface_Object = MibTableColumn
aixPrinterInterface = _AixPrinterInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 4),
    _AixPrinterInterface_Type()
)
aixPrinterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterInterface.setStatus("current")


class _AixPrinterStatus_Type(Integer32):
    """Custom type aixPrinterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixPrinterStatus_Type.__name__ = "Integer32"
_AixPrinterStatus_Object = MibTableColumn
aixPrinterStatus = _AixPrinterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 5),
    _AixPrinterStatus_Type()
)
aixPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterStatus.setStatus("current")
_AixPrinterDescr_Type = DisplayString
_AixPrinterDescr_Object = MibTableColumn
aixPrinterDescr = _AixPrinterDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 6),
    _AixPrinterDescr_Type()
)
aixPrinterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterDescr.setStatus("current")
_AixPrinterLocation_Type = DisplayString
_AixPrinterLocation_Object = MibTableColumn
aixPrinterLocation = _AixPrinterLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 7),
    _AixPrinterLocation_Type()
)
aixPrinterLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterLocation.setStatus("current")
_AixPrinterPortNumber_Type = DisplayString
_AixPrinterPortNumber_Object = MibTableColumn
aixPrinterPortNumber = _AixPrinterPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 1, 1, 1, 8),
    _AixPrinterPortNumber_Type()
)
aixPrinterPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixPrinterPortNumber.setStatus("current")
_AixTape_ObjectIdentity = ObjectIdentity
aixTape = _AixTape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2)
)
_AixTapeDrvTable_Object = MibTable
aixTapeDrvTable = _AixTapeDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1)
)
if mibBuilder.loadTexts:
    aixTapeDrvTable.setStatus("current")
_AixTapeDrvEntry_Object = MibTableRow
aixTapeDrvEntry = _AixTapeDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1)
)
aixTapeDrvEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixTapeDrvIndex"),
)
if mibBuilder.loadTexts:
    aixTapeDrvEntry.setStatus("current")
_AixTapeDrvName_Type = DisplayString
_AixTapeDrvName_Object = MibTableColumn
aixTapeDrvName = _AixTapeDrvName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 1),
    _AixTapeDrvName_Type()
)
aixTapeDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvName.setStatus("current")


class _AixTapeDrvIndex_Type(Integer32):
    """Custom type aixTapeDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixTapeDrvIndex_Type.__name__ = "Integer32"
_AixTapeDrvIndex_Object = MibTableColumn
aixTapeDrvIndex = _AixTapeDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 2),
    _AixTapeDrvIndex_Type()
)
aixTapeDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvIndex.setStatus("current")
_AixTapeDrvType_Type = DisplayString
_AixTapeDrvType_Object = MibTableColumn
aixTapeDrvType = _AixTapeDrvType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 3),
    _AixTapeDrvType_Type()
)
aixTapeDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvType.setStatus("current")
_AixTapeDrvInterface_Type = DisplayString
_AixTapeDrvInterface_Object = MibTableColumn
aixTapeDrvInterface = _AixTapeDrvInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 4),
    _AixTapeDrvInterface_Type()
)
aixTapeDrvInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvInterface.setStatus("current")


class _AixTapeDrvStatus_Type(Integer32):
    """Custom type aixTapeDrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixTapeDrvStatus_Type.__name__ = "Integer32"
_AixTapeDrvStatus_Object = MibTableColumn
aixTapeDrvStatus = _AixTapeDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 5),
    _AixTapeDrvStatus_Type()
)
aixTapeDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvStatus.setStatus("current")
_AixTapeDrvDescr_Type = DisplayString
_AixTapeDrvDescr_Object = MibTableColumn
aixTapeDrvDescr = _AixTapeDrvDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 6),
    _AixTapeDrvDescr_Type()
)
aixTapeDrvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvDescr.setStatus("current")
_AixTapeDrvLocation_Type = DisplayString
_AixTapeDrvLocation_Object = MibTableColumn
aixTapeDrvLocation = _AixTapeDrvLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 7),
    _AixTapeDrvLocation_Type()
)
aixTapeDrvLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvLocation.setStatus("current")


class _AixTapeDrvBlkSize_Type(Integer32):
    """Custom type aixTapeDrvBlkSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixTapeDrvBlkSize_Type.__name__ = "Integer32"
_AixTapeDrvBlkSize_Object = MibTableColumn
aixTapeDrvBlkSize = _AixTapeDrvBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 8),
    _AixTapeDrvBlkSize_Type()
)
aixTapeDrvBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvBlkSize.setStatus("current")
_AixTapeDrvManufacturerName_Type = DisplayString
_AixTapeDrvManufacturerName_Object = MibTableColumn
aixTapeDrvManufacturerName = _AixTapeDrvManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 9),
    _AixTapeDrvManufacturerName_Type()
)
aixTapeDrvManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvManufacturerName.setStatus("current")
_AixTapeDrvModelName_Type = DisplayString
_AixTapeDrvModelName_Object = MibTableColumn
aixTapeDrvModelName = _AixTapeDrvModelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 10),
    _AixTapeDrvModelName_Type()
)
aixTapeDrvModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvModelName.setStatus("current")
_AixTapeDrvSN_Type = DisplayString
_AixTapeDrvSN_Object = MibTableColumn
aixTapeDrvSN = _AixTapeDrvSN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 11),
    _AixTapeDrvSN_Type()
)
aixTapeDrvSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvSN.setStatus("current")
_AixTapeDrvPN_Type = DisplayString
_AixTapeDrvPN_Object = MibTableColumn
aixTapeDrvPN = _AixTapeDrvPN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 12),
    _AixTapeDrvPN_Type()
)
aixTapeDrvPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvPN.setStatus("current")
_AixTapeDrvFRU_Type = DisplayString
_AixTapeDrvFRU_Object = MibTableColumn
aixTapeDrvFRU = _AixTapeDrvFRU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 13),
    _AixTapeDrvFRU_Type()
)
aixTapeDrvFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvFRU.setStatus("current")
_AixTapeDrvEC_Type = DisplayString
_AixTapeDrvEC_Object = MibTableColumn
aixTapeDrvEC = _AixTapeDrvEC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 2, 1, 1, 14),
    _AixTapeDrvEC_Type()
)
aixTapeDrvEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixTapeDrvEC.setStatus("current")
_AixHardDisk_ObjectIdentity = ObjectIdentity
aixHardDisk = _AixHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3)
)
_AixHdTable_Object = MibTable
aixHdTable = _AixHdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1)
)
if mibBuilder.loadTexts:
    aixHdTable.setStatus("current")
_AixHdEntry_Object = MibTableRow
aixHdEntry = _AixHdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1)
)
aixHdEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixHdIndex"),
)
if mibBuilder.loadTexts:
    aixHdEntry.setStatus("current")
_AixHdName_Type = DisplayString
_AixHdName_Object = MibTableColumn
aixHdName = _AixHdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 1),
    _AixHdName_Type()
)
aixHdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdName.setStatus("current")


class _AixHdIndex_Type(Integer32):
    """Custom type aixHdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixHdIndex_Type.__name__ = "Integer32"
_AixHdIndex_Object = MibTableColumn
aixHdIndex = _AixHdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 2),
    _AixHdIndex_Type()
)
aixHdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdIndex.setStatus("current")
_AixHdType_Type = DisplayString
_AixHdType_Object = MibTableColumn
aixHdType = _AixHdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 3),
    _AixHdType_Type()
)
aixHdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdType.setStatus("current")


class _AixHdSize_Type(Integer32):
    """Custom type aixHdSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixHdSize_Type.__name__ = "Integer32"
_AixHdSize_Object = MibTableColumn
aixHdSize = _AixHdSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 4),
    _AixHdSize_Type()
)
aixHdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdSize.setStatus("current")
if mibBuilder.loadTexts:
    aixHdSize.setUnits("megabytes")
_AixHdInterface_Type = DisplayString
_AixHdInterface_Object = MibTableColumn
aixHdInterface = _AixHdInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 5),
    _AixHdInterface_Type()
)
aixHdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdInterface.setStatus("current")


class _AixHdStatus_Type(Integer32):
    """Custom type aixHdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixHdStatus_Type.__name__ = "Integer32"
_AixHdStatus_Object = MibTableColumn
aixHdStatus = _AixHdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 6),
    _AixHdStatus_Type()
)
aixHdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdStatus.setStatus("current")
_AixHdLocation_Type = DisplayString
_AixHdLocation_Object = MibTableColumn
aixHdLocation = _AixHdLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 7),
    _AixHdLocation_Type()
)
aixHdLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdLocation.setStatus("current")
_AixHdIdentifier_Type = DisplayString
_AixHdIdentifier_Object = MibTableColumn
aixHdIdentifier = _AixHdIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 8),
    _AixHdIdentifier_Type()
)
aixHdIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdIdentifier.setStatus("current")
_AixHdDescr_Type = DisplayString
_AixHdDescr_Object = MibTableColumn
aixHdDescr = _AixHdDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 9),
    _AixHdDescr_Type()
)
aixHdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdDescr.setStatus("current")
_AixHdManufacturerName_Type = DisplayString
_AixHdManufacturerName_Object = MibTableColumn
aixHdManufacturerName = _AixHdManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 10),
    _AixHdManufacturerName_Type()
)
aixHdManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdManufacturerName.setStatus("current")
_AixHdModelName_Type = DisplayString
_AixHdModelName_Object = MibTableColumn
aixHdModelName = _AixHdModelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 11),
    _AixHdModelName_Type()
)
aixHdModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdModelName.setStatus("current")
_AixHdSN_Type = DisplayString
_AixHdSN_Object = MibTableColumn
aixHdSN = _AixHdSN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 12),
    _AixHdSN_Type()
)
aixHdSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdSN.setStatus("current")
_AixHdPN_Type = DisplayString
_AixHdPN_Object = MibTableColumn
aixHdPN = _AixHdPN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 13),
    _AixHdPN_Type()
)
aixHdPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdPN.setStatus("current")
_AixHdFRU_Type = DisplayString
_AixHdFRU_Object = MibTableColumn
aixHdFRU = _AixHdFRU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 14),
    _AixHdFRU_Type()
)
aixHdFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdFRU.setStatus("current")
_AixHdEC_Type = DisplayString
_AixHdEC_Object = MibTableColumn
aixHdEC = _AixHdEC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 3, 1, 1, 15),
    _AixHdEC_Type()
)
aixHdEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixHdEC.setStatus("current")
_AixMemory_ObjectIdentity = ObjectIdentity
aixMemory = _AixMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4)
)
_AixMemTable_Object = MibTable
aixMemTable = _AixMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1)
)
if mibBuilder.loadTexts:
    aixMemTable.setStatus("current")
_AixMemEntry_Object = MibTableRow
aixMemEntry = _AixMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1)
)
aixMemEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixMemIndex"),
)
if mibBuilder.loadTexts:
    aixMemEntry.setStatus("current")
_AixMemName_Type = DisplayString
_AixMemName_Object = MibTableColumn
aixMemName = _AixMemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1, 1),
    _AixMemName_Type()
)
aixMemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixMemName.setStatus("current")


class _AixMemIndex_Type(Integer32):
    """Custom type aixMemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixMemIndex_Type.__name__ = "Integer32"
_AixMemIndex_Object = MibTableColumn
aixMemIndex = _AixMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1, 2),
    _AixMemIndex_Type()
)
aixMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixMemIndex.setStatus("current")
_AixMemLocation_Type = DisplayString
_AixMemLocation_Object = MibTableColumn
aixMemLocation = _AixMemLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1, 3),
    _AixMemLocation_Type()
)
aixMemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixMemLocation.setStatus("current")


class _AixMemSize_Type(Integer32):
    """Custom type aixMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixMemSize_Type.__name__ = "Integer32"
_AixMemSize_Object = MibTableColumn
aixMemSize = _AixMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1, 4),
    _AixMemSize_Type()
)
aixMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixMemSize.setStatus("current")
if mibBuilder.loadTexts:
    aixMemSize.setUnits("megabytes")
_AixMemDescr_Type = DisplayString
_AixMemDescr_Object = MibTableColumn
aixMemDescr = _AixMemDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 4, 1, 1, 5),
    _AixMemDescr_Type()
)
aixMemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixMemDescr.setStatus("current")
_AixCDROM_ObjectIdentity = ObjectIdentity
aixCDROM = _AixCDROM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5)
)
_AixCdromTable_Object = MibTable
aixCdromTable = _AixCdromTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1)
)
if mibBuilder.loadTexts:
    aixCdromTable.setStatus("current")
_AixCdromEntry_Object = MibTableRow
aixCdromEntry = _AixCdromEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1)
)
aixCdromEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixCdromIndex"),
)
if mibBuilder.loadTexts:
    aixCdromEntry.setStatus("current")
_AixCdromName_Type = DisplayString
_AixCdromName_Object = MibTableColumn
aixCdromName = _AixCdromName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 1),
    _AixCdromName_Type()
)
aixCdromName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromName.setStatus("current")


class _AixCdromIndex_Type(Integer32):
    """Custom type aixCdromIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixCdromIndex_Type.__name__ = "Integer32"
_AixCdromIndex_Object = MibTableColumn
aixCdromIndex = _AixCdromIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 2),
    _AixCdromIndex_Type()
)
aixCdromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromIndex.setStatus("current")
_AixCdromType_Type = DisplayString
_AixCdromType_Object = MibTableColumn
aixCdromType = _AixCdromType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 3),
    _AixCdromType_Type()
)
aixCdromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromType.setStatus("current")
_AixCdromInterface_Type = DisplayString
_AixCdromInterface_Object = MibTableColumn
aixCdromInterface = _AixCdromInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 4),
    _AixCdromInterface_Type()
)
aixCdromInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromInterface.setStatus("current")
_AixCdromDescr_Type = DisplayString
_AixCdromDescr_Object = MibTableColumn
aixCdromDescr = _AixCdromDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 5),
    _AixCdromDescr_Type()
)
aixCdromDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromDescr.setStatus("current")


class _AixCdromStatus_Type(Integer32):
    """Custom type aixCdromStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixCdromStatus_Type.__name__ = "Integer32"
_AixCdromStatus_Object = MibTableColumn
aixCdromStatus = _AixCdromStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 6),
    _AixCdromStatus_Type()
)
aixCdromStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromStatus.setStatus("current")
_AixCdromLocation_Type = DisplayString
_AixCdromLocation_Object = MibTableColumn
aixCdromLocation = _AixCdromLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 7),
    _AixCdromLocation_Type()
)
aixCdromLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromLocation.setStatus("current")
_AixCdromManufacturerName_Type = DisplayString
_AixCdromManufacturerName_Object = MibTableColumn
aixCdromManufacturerName = _AixCdromManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 8),
    _AixCdromManufacturerName_Type()
)
aixCdromManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromManufacturerName.setStatus("current")
_AixCdromModelName_Type = DisplayString
_AixCdromModelName_Object = MibTableColumn
aixCdromModelName = _AixCdromModelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 9),
    _AixCdromModelName_Type()
)
aixCdromModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromModelName.setStatus("current")
_AixCdromPN_Type = DisplayString
_AixCdromPN_Object = MibTableColumn
aixCdromPN = _AixCdromPN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 10),
    _AixCdromPN_Type()
)
aixCdromPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromPN.setStatus("current")
_AixCdromFRU_Type = DisplayString
_AixCdromFRU_Object = MibTableColumn
aixCdromFRU = _AixCdromFRU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 11),
    _AixCdromFRU_Type()
)
aixCdromFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromFRU.setStatus("current")
_AixCdromEC_Type = DisplayString
_AixCdromEC_Object = MibTableColumn
aixCdromEC = _AixCdromEC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 5, 1, 1, 12),
    _AixCdromEC_Type()
)
aixCdromEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixCdromEC.setStatus("current")
_AixScsi_ObjectIdentity = ObjectIdentity
aixScsi = _AixScsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6)
)
_AixScsiTable_Object = MibTable
aixScsiTable = _AixScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1)
)
if mibBuilder.loadTexts:
    aixScsiTable.setStatus("current")
_AixScsiEntry_Object = MibTableRow
aixScsiEntry = _AixScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1)
)
aixScsiEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixScsiIndex"),
)
if mibBuilder.loadTexts:
    aixScsiEntry.setStatus("current")
_AixScsiName_Type = DisplayString
_AixScsiName_Object = MibTableColumn
aixScsiName = _AixScsiName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 1),
    _AixScsiName_Type()
)
aixScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiName.setStatus("current")


class _AixScsiIndex_Type(Integer32):
    """Custom type aixScsiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixScsiIndex_Type.__name__ = "Integer32"
_AixScsiIndex_Object = MibTableColumn
aixScsiIndex = _AixScsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 2),
    _AixScsiIndex_Type()
)
aixScsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiIndex.setStatus("current")
_AixScsiDescr_Type = DisplayString
_AixScsiDescr_Object = MibTableColumn
aixScsiDescr = _AixScsiDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 3),
    _AixScsiDescr_Type()
)
aixScsiDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiDescr.setStatus("current")


class _AixScsiStatus_Type(Integer32):
    """Custom type aixScsiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixScsiStatus_Type.__name__ = "Integer32"
_AixScsiStatus_Object = MibTableColumn
aixScsiStatus = _AixScsiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 4),
    _AixScsiStatus_Type()
)
aixScsiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiStatus.setStatus("current")
_AixScsiLocation_Type = DisplayString
_AixScsiLocation_Object = MibTableColumn
aixScsiLocation = _AixScsiLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 5),
    _AixScsiLocation_Type()
)
aixScsiLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiLocation.setStatus("current")


class _AixScsiAdapterID_Type(Integer32):
    """Custom type aixScsiAdapterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AixScsiAdapterID_Type.__name__ = "Integer32"
_AixScsiAdapterID_Object = MibTableColumn
aixScsiAdapterID = _AixScsiAdapterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 6, 1, 1, 6),
    _AixScsiAdapterID_Type()
)
aixScsiAdapterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixScsiAdapterID.setStatus("current")
_AixProcessor_ObjectIdentity = ObjectIdentity
aixProcessor = _AixProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7)
)
_AixProcessorTable_Object = MibTable
aixProcessorTable = _AixProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1)
)
if mibBuilder.loadTexts:
    aixProcessorTable.setStatus("current")
_AixProcessorEntry_Object = MibTableRow
aixProcessorEntry = _AixProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1)
)
aixProcessorEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixProcessorIndex"),
)
if mibBuilder.loadTexts:
    aixProcessorEntry.setStatus("current")
_AixProcessorName_Type = DisplayString
_AixProcessorName_Object = MibTableColumn
aixProcessorName = _AixProcessorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1, 1),
    _AixProcessorName_Type()
)
aixProcessorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcessorName.setStatus("current")


class _AixProcessorIndex_Type(Integer32):
    """Custom type aixProcessorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixProcessorIndex_Type.__name__ = "Integer32"
_AixProcessorIndex_Object = MibTableColumn
aixProcessorIndex = _AixProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1, 2),
    _AixProcessorIndex_Type()
)
aixProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcessorIndex.setStatus("current")
_AixProcessorType_Type = DisplayString
_AixProcessorType_Object = MibTableColumn
aixProcessorType = _AixProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1, 3),
    _AixProcessorType_Type()
)
aixProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcessorType.setStatus("current")
_AixProcessorDescr_Type = DisplayString
_AixProcessorDescr_Object = MibTableColumn
aixProcessorDescr = _AixProcessorDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1, 4),
    _AixProcessorDescr_Type()
)
aixProcessorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcessorDescr.setStatus("current")


class _AixProcessorSpeed_Type(Integer32):
    """Custom type aixProcessorSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixProcessorSpeed_Type.__name__ = "Integer32"
_AixProcessorSpeed_Object = MibTableColumn
aixProcessorSpeed = _AixProcessorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 7, 1, 1, 5),
    _AixProcessorSpeed_Type()
)
aixProcessorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixProcessorSpeed.setStatus("current")
_AixNetwork_ObjectIdentity = ObjectIdentity
aixNetwork = _AixNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8)
)
_AixNetworkTable_Object = MibTable
aixNetworkTable = _AixNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1)
)
if mibBuilder.loadTexts:
    aixNetworkTable.setStatus("current")
_AixNetworkEntry_Object = MibTableRow
aixNetworkEntry = _AixNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1)
)
aixNetworkEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixNetworkIndex"),
)
if mibBuilder.loadTexts:
    aixNetworkEntry.setStatus("current")
_AixNetworkName_Type = DisplayString
_AixNetworkName_Object = MibTableColumn
aixNetworkName = _AixNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 1),
    _AixNetworkName_Type()
)
aixNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkName.setStatus("current")


class _AixNetworkIndex_Type(Integer32):
    """Custom type aixNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixNetworkIndex_Type.__name__ = "Integer32"
_AixNetworkIndex_Object = MibTableColumn
aixNetworkIndex = _AixNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 2),
    _AixNetworkIndex_Type()
)
aixNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkIndex.setStatus("current")
_AixNetworkType_Type = DisplayString
_AixNetworkType_Object = MibTableColumn
aixNetworkType = _AixNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 3),
    _AixNetworkType_Type()
)
aixNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkType.setStatus("current")
_AixNetworkInterface_Type = DisplayString
_AixNetworkInterface_Object = MibTableColumn
aixNetworkInterface = _AixNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 4),
    _AixNetworkInterface_Type()
)
aixNetworkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkInterface.setStatus("current")


class _AixNetworkStatus_Type(Integer32):
    """Custom type aixNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixNetworkStatus_Type.__name__ = "Integer32"
_AixNetworkStatus_Object = MibTableColumn
aixNetworkStatus = _AixNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 5),
    _AixNetworkStatus_Type()
)
aixNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkStatus.setStatus("current")
_AixNetworkLocation_Type = DisplayString
_AixNetworkLocation_Object = MibTableColumn
aixNetworkLocation = _AixNetworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 6),
    _AixNetworkLocation_Type()
)
aixNetworkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkLocation.setStatus("current")
_AixNetworkDescr_Type = DisplayString
_AixNetworkDescr_Object = MibTableColumn
aixNetworkDescr = _AixNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 8, 1, 1, 7),
    _AixNetworkDescr_Type()
)
aixNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixNetworkDescr.setStatus("current")
_AixAdapter_ObjectIdentity = ObjectIdentity
aixAdapter = _AixAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9)
)
_AixAdapterTable_Object = MibTable
aixAdapterTable = _AixAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1)
)
if mibBuilder.loadTexts:
    aixAdapterTable.setStatus("current")
_AixAdapterEntry_Object = MibTableRow
aixAdapterEntry = _AixAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1)
)
aixAdapterEntry.setIndexNames(
    (0, "IBM-AIX-MIB", "aixAdapterIndex"),
)
if mibBuilder.loadTexts:
    aixAdapterEntry.setStatus("current")
_AixAdapterName_Type = DisplayString
_AixAdapterName_Object = MibTableColumn
aixAdapterName = _AixAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 1),
    _AixAdapterName_Type()
)
aixAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterName.setStatus("current")


class _AixAdapterIndex_Type(Integer32):
    """Custom type aixAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AixAdapterIndex_Type.__name__ = "Integer32"
_AixAdapterIndex_Object = MibTableColumn
aixAdapterIndex = _AixAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 2),
    _AixAdapterIndex_Type()
)
aixAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterIndex.setStatus("current")
_AixAdapterType_Type = DisplayString
_AixAdapterType_Object = MibTableColumn
aixAdapterType = _AixAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 3),
    _AixAdapterType_Type()
)
aixAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterType.setStatus("current")
_AixAdapterInterface_Type = DisplayString
_AixAdapterInterface_Object = MibTableColumn
aixAdapterInterface = _AixAdapterInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 4),
    _AixAdapterInterface_Type()
)
aixAdapterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterInterface.setStatus("current")


class _AixAdapterStatus_Type(Integer32):
    """Custom type aixAdapterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("defined", 2))
    )


_AixAdapterStatus_Type.__name__ = "Integer32"
_AixAdapterStatus_Object = MibTableColumn
aixAdapterStatus = _AixAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 5),
    _AixAdapterStatus_Type()
)
aixAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterStatus.setStatus("current")
_AixAdapterLocation_Type = DisplayString
_AixAdapterLocation_Object = MibTableColumn
aixAdapterLocation = _AixAdapterLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 6),
    _AixAdapterLocation_Type()
)
aixAdapterLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterLocation.setStatus("current")
_AixAdapterDescr_Type = DisplayString
_AixAdapterDescr_Object = MibTableColumn
aixAdapterDescr = _AixAdapterDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 9, 9, 1, 1, 7),
    _AixAdapterDescr_Type()
)
aixAdapterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aixAdapterDescr.setStatus("current")
_AixConformance_ObjectIdentity = ObjectIdentity
aixConformance = _AixConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10)
)
_AixCfmGroup_ObjectIdentity = ObjectIdentity
aixCfmGroup = _AixCfmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1)
)
_AixCompliances_ObjectIdentity = ObjectIdentity
aixCompliances = _AixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 2)
)

# Managed Objects groups

aixAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 1)
)
aixAgentGroup.setObjects(
      *(("IBM-AIX-MIB", "aixAgentAction"),
        ("IBM-AIX-MIB", "aixAgentCmdString"),
        ("IBM-AIX-MIB", "aixAgentExeCommand"),
        ("IBM-AIX-MIB", "aixAgentCmdResult"),
        ("IBM-AIX-MIB", "aixAgentCmdOutput"),
        ("IBM-AIX-MIB", "aixAgentCmdOutIndex"),
        ("IBM-AIX-MIB", "aixAgentPollInterval"),
        ("IBM-AIX-MIB", "aixPollEnable"),
        ("IBM-AIX-MIB", "aixLastTrapMsg"),
        ("IBM-AIX-MIB", "aixFsPollInterval"),
        ("IBM-AIX-MIB", "aixVgPollInterval"),
        ("IBM-AIX-MIB", "aixCPUPollInterval"),
        ("IBM-AIX-MIB", "aixLFPollInterval"),
        ("IBM-AIX-MIB", "aixPagePollInterval"))
)
if mibBuilder.loadTexts:
    aixAgentGroup.setStatus("current")

aixSeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 2)
)
aixSeGroup.setObjects(
      *(("IBM-AIX-MIB", "aixSeCPUUtilization"),
        ("IBM-AIX-MIB", "aixSeCPUThreshold"),
        ("IBM-AIX-MIB", "aixSeSystemRunLevel"),
        ("IBM-AIX-MIB", "aixSeSystemState"),
        ("IBM-AIX-MIB", "aixSeSystemTrap"))
)
if mibBuilder.loadTexts:
    aixSeGroup.setStatus("current")

aixVGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 4)
)
aixVGGroup.setObjects(
      *(("IBM-AIX-MIB", "aixVgName"),
        ("IBM-AIX-MIB", "aixVgIdentifier"),
        ("IBM-AIX-MIB", "aixVgState"),
        ("IBM-AIX-MIB", "aixVgSize"),
        ("IBM-AIX-MIB", "aixVgFree"),
        ("IBM-AIX-MIB", "aixVgCurNumLVs"),
        ("IBM-AIX-MIB", "aixVgOpenLVs"),
        ("IBM-AIX-MIB", "aixVgActivePVs"),
        ("IBM-AIX-MIB", "aixVgThreshold"),
        ("IBM-AIX-MIB", "aixVgIndex"))
)
if mibBuilder.loadTexts:
    aixVGGroup.setStatus("current")

aixLVGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 5)
)
aixLVGroup.setObjects(
      *(("IBM-AIX-MIB", "aixLvName"),
        ("IBM-AIX-MIB", "aixLvNameVG"),
        ("IBM-AIX-MIB", "aixLvType"),
        ("IBM-AIX-MIB", "aixLvMountPoint"),
        ("IBM-AIX-MIB", "aixLvSize"),
        ("IBM-AIX-MIB", "aixLvState"),
        ("IBM-AIX-MIB", "aixLvIndex"))
)
if mibBuilder.loadTexts:
    aixLVGroup.setStatus("current")

aixPVGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 6)
)
aixPVGroup.setObjects(
      *(("IBM-AIX-MIB", "aixPvName"),
        ("IBM-AIX-MIB", "aixPvNameVG"),
        ("IBM-AIX-MIB", "aixPvState"),
        ("IBM-AIX-MIB", "aixPvSize"),
        ("IBM-AIX-MIB", "aixPvFree"),
        ("IBM-AIX-MIB", "aixPvNumLVs"),
        ("IBM-AIX-MIB", "aixPvIndex"))
)
if mibBuilder.loadTexts:
    aixPVGroup.setStatus("current")

aixPagingSpaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 7)
)
aixPagingSpaceGroup.setObjects(
      *(("IBM-AIX-MIB", "aixPageName"),
        ("IBM-AIX-MIB", "aixPageNameVG"),
        ("IBM-AIX-MIB", "aixPageNamePV"),
        ("IBM-AIX-MIB", "aixPageSize"),
        ("IBM-AIX-MIB", "aixPagePercentUsed"),
        ("IBM-AIX-MIB", "aixPageStatus"),
        ("IBM-AIX-MIB", "aixPageType"),
        ("IBM-AIX-MIB", "aixPageThreshold"),
        ("IBM-AIX-MIB", "aixPageIndex"))
)
if mibBuilder.loadTexts:
    aixPagingSpaceGroup.setStatus("current")

aixFsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 8)
)
aixFsGroup.setObjects(
      *(("IBM-AIX-MIB", "aixFsIndex"),
        ("IBM-AIX-MIB", "aixFsName"),
        ("IBM-AIX-MIB", "aixFsMountPoint"),
        ("IBM-AIX-MIB", "aixFsType"),
        ("IBM-AIX-MIB", "aixFsSize"),
        ("IBM-AIX-MIB", "aixFsFree"),
        ("IBM-AIX-MIB", "aixFsNumINodes"),
        ("IBM-AIX-MIB", "aixFsUsedInodes"),
        ("IBM-AIX-MIB", "aixFsThreshold"),
        ("IBM-AIX-MIB", "aixFsStatus"),
        ("IBM-AIX-MIB", "aixFsExecution"),
        ("IBM-AIX-MIB", "aixFsResultMsg"))
)
if mibBuilder.loadTexts:
    aixFsGroup.setStatus("current")

aixProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 9)
)
aixProcessGroup.setObjects(
      *(("IBM-AIX-MIB", "aixProcPID"),
        ("IBM-AIX-MIB", "aixProcUID"),
        ("IBM-AIX-MIB", "aixProcPPID"),
        ("IBM-AIX-MIB", "aixProcGroup"),
        ("IBM-AIX-MIB", "aixProcPriority"),
        ("IBM-AIX-MIB", "aixProcCPU"),
        ("IBM-AIX-MIB", "aixProcStart"),
        ("IBM-AIX-MIB", "aixProcStatus"),
        ("IBM-AIX-MIB", "aixProcTTY"),
        ("IBM-AIX-MIB", "aixProcCMD"),
        ("IBM-AIX-MIB", "aixProcNum"))
)
if mibBuilder.loadTexts:
    aixProcessGroup.setStatus("current")

aixLoginUsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 10)
)
aixLoginUsrGroup.setObjects(
      *(("IBM-AIX-MIB", "aixLoginUserName"),
        ("IBM-AIX-MIB", "aixLoginUserTTY"),
        ("IBM-AIX-MIB", "aixLoginUserHost"),
        ("IBM-AIX-MIB", "aixLoginUserDateAndTime"),
        ("IBM-AIX-MIB", "aixLoginUserIndex"),
        ("IBM-AIX-MIB", "aixLoginFailedThreshold"),
        ("IBM-AIX-MIB", "aixFailedLoginTimePeriod"))
)
if mibBuilder.loadTexts:
    aixLoginUsrGroup.setStatus("current")

aixPrtQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 11)
)
aixPrtQueueGroup.setObjects(
      *(("IBM-AIX-MIB", "aixPrtQueName"),
        ("IBM-AIX-MIB", "aixPrtQueDevice"),
        ("IBM-AIX-MIB", "aixPrtQueStatus"),
        ("IBM-AIX-MIB", "aixPrtQueAction"),
        ("IBM-AIX-MIB", "aixPrtQueIndex"),
        ("IBM-AIX-MIB", "aixPrtQueAcctFile"),
        ("IBM-AIX-MIB", "aixPrtQueRQ"),
        ("IBM-AIX-MIB", "aixPrtQueDescipline"),
        ("IBM-AIX-MIB", "aixPrtQueHost"),
        ("IBM-AIX-MIB", "aixPrtQueJobNum"))
)
if mibBuilder.loadTexts:
    aixPrtQueueGroup.setStatus("current")

aixUsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 12)
)
aixUsrGroup.setObjects(
      *(("IBM-AIX-MIB", "aixUsrName"),
        ("IBM-AIX-MIB", "aixUsrID"),
        ("IBM-AIX-MIB", "aixUsrHome"),
        ("IBM-AIX-MIB", "aixUsrShell"),
        ("IBM-AIX-MIB", "aixUsrLocalLogin"),
        ("IBM-AIX-MIB", "aixUsrRemoteLogin"),
        ("IBM-AIX-MIB", "aixUsrPasswdMaxAge"),
        ("IBM-AIX-MIB", "aixUsrStatus"),
        ("IBM-AIX-MIB", "aixUsrGroups"),
        ("IBM-AIX-MIB", "aixUsrAllowableAttempts"),
        ("IBM-AIX-MIB", "aixUsrResetLoginCount"),
        ("IBM-AIX-MIB", "aixUsrPrimaryGroup"),
        ("IBM-AIX-MIB", "aixUsrIndex"))
)
if mibBuilder.loadTexts:
    aixUsrGroup.setStatus("current")

aixGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 13)
)
aixGrpGroup.setObjects(
      *(("IBM-AIX-MIB", "aixGrpName"),
        ("IBM-AIX-MIB", "aixGrpID"),
        ("IBM-AIX-MIB", "aixGrpAdminGroup"),
        ("IBM-AIX-MIB", "aixGrpIndex"),
        ("IBM-AIX-MIB", "aixGrpUsrList"),
        ("IBM-AIX-MIB", "aixGrpAdmList"))
)
if mibBuilder.loadTexts:
    aixGrpGroup.setStatus("current")

aixSubSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 14)
)
aixSubSystemGroup.setObjects(
      *(("IBM-AIX-MIB", "aixSubSysName"),
        ("IBM-AIX-MIB", "aixSubSysGroup"),
        ("IBM-AIX-MIB", "aixSubSysPID"),
        ("IBM-AIX-MIB", "aixSubSysIndex"),
        ("IBM-AIX-MIB", "aixSubSysStatus"),
        ("IBM-AIX-MIB", "aixSubSystemNum"))
)
if mibBuilder.loadTexts:
    aixSubSystemGroup.setStatus("current")

aixSubServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 15)
)
aixSubServerGroup.setObjects(
      *(("IBM-AIX-MIB", "aixSubSrvName"),
        ("IBM-AIX-MIB", "aixSubSrvDescr"),
        ("IBM-AIX-MIB", "aixSubSrvCommand"),
        ("IBM-AIX-MIB", "aixSubSrvStatus"),
        ("IBM-AIX-MIB", "aixSubSrvNum"),
        ("IBM-AIX-MIB", "aixSubSrvIndex"),
        ("IBM-AIX-MIB", "aixSubSrvSubsys"))
)
if mibBuilder.loadTexts:
    aixSubServerGroup.setStatus("current")

aixSeAuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 16)
)
aixSeAuxGroup.setObjects(
      *(("IBM-AIX-MIB", "aixSeDateAndTime"),
        ("IBM-AIX-MIB", "aixSeMaxProcPerUser"),
        ("IBM-AIX-MIB", "aixSeLicenseNum"),
        ("IBM-AIX-MIB", "aixSeRemainingLicenseNum"),
        ("IBM-AIX-MIB", "aixSeNumCPUs"),
        ("IBM-AIX-MIB", "aixSeMachineType"),
        ("IBM-AIX-MIB", "aixSeSerialNumber"))
)
if mibBuilder.loadTexts:
    aixSeAuxGroup.setStatus("current")

aixPrinterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 17)
)
aixPrinterGroup.setObjects(
      *(("IBM-AIX-MIB", "aixPrinterName"),
        ("IBM-AIX-MIB", "aixPrinterType"),
        ("IBM-AIX-MIB", "aixPrinterInterface"),
        ("IBM-AIX-MIB", "aixPrinterStatus"),
        ("IBM-AIX-MIB", "aixPrinterDescr"),
        ("IBM-AIX-MIB", "aixPrinterLocation"),
        ("IBM-AIX-MIB", "aixPrinterPortNumber"),
        ("IBM-AIX-MIB", "aixPrinterIndex"))
)
if mibBuilder.loadTexts:
    aixPrinterGroup.setStatus("current")

aixTapeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 18)
)
aixTapeGroup.setObjects(
      *(("IBM-AIX-MIB", "aixTapeDrvName"),
        ("IBM-AIX-MIB", "aixTapeDrvType"),
        ("IBM-AIX-MIB", "aixTapeDrvInterface"),
        ("IBM-AIX-MIB", "aixTapeDrvStatus"),
        ("IBM-AIX-MIB", "aixTapeDrvLocation"),
        ("IBM-AIX-MIB", "aixTapeDrvBlkSize"),
        ("IBM-AIX-MIB", "aixTapeDrvDescr"),
        ("IBM-AIX-MIB", "aixTapeDrvIndex"),
        ("IBM-AIX-MIB", "aixTapeDrvManufacturerName"),
        ("IBM-AIX-MIB", "aixTapeDrvModelName"),
        ("IBM-AIX-MIB", "aixTapeDrvSN"),
        ("IBM-AIX-MIB", "aixTapeDrvFRU"),
        ("IBM-AIX-MIB", "aixTapeDrvPN"),
        ("IBM-AIX-MIB", "aixTapeDrvEC"))
)
if mibBuilder.loadTexts:
    aixTapeGroup.setStatus("current")

aixHardDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 19)
)
aixHardDiskGroup.setObjects(
      *(("IBM-AIX-MIB", "aixHdName"),
        ("IBM-AIX-MIB", "aixHdType"),
        ("IBM-AIX-MIB", "aixHdSize"),
        ("IBM-AIX-MIB", "aixHdInterface"),
        ("IBM-AIX-MIB", "aixHdStatus"),
        ("IBM-AIX-MIB", "aixHdLocation"),
        ("IBM-AIX-MIB", "aixHdIdentifier"),
        ("IBM-AIX-MIB", "aixHdDescr"),
        ("IBM-AIX-MIB", "aixHdIndex"),
        ("IBM-AIX-MIB", "aixHdManufacturerName"),
        ("IBM-AIX-MIB", "aixHdModelName"),
        ("IBM-AIX-MIB", "aixHdSN"),
        ("IBM-AIX-MIB", "aixHdFRU"),
        ("IBM-AIX-MIB", "aixHdPN"),
        ("IBM-AIX-MIB", "aixHdEC"))
)
if mibBuilder.loadTexts:
    aixHardDiskGroup.setStatus("current")

aixMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 20)
)
aixMemoryGroup.setObjects(
      *(("IBM-AIX-MIB", "aixMemName"),
        ("IBM-AIX-MIB", "aixMemLocation"),
        ("IBM-AIX-MIB", "aixMemSize"),
        ("IBM-AIX-MIB", "aixMemDescr"),
        ("IBM-AIX-MIB", "aixMemIndex"))
)
if mibBuilder.loadTexts:
    aixMemoryGroup.setStatus("current")

aixCDROMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 21)
)
aixCDROMGroup.setObjects(
      *(("IBM-AIX-MIB", "aixCdromName"),
        ("IBM-AIX-MIB", "aixCdromType"),
        ("IBM-AIX-MIB", "aixCdromInterface"),
        ("IBM-AIX-MIB", "aixCdromDescr"),
        ("IBM-AIX-MIB", "aixCdromStatus"),
        ("IBM-AIX-MIB", "aixCdromLocation"),
        ("IBM-AIX-MIB", "aixCdromIndex"),
        ("IBM-AIX-MIB", "aixCdromManufacturerName"),
        ("IBM-AIX-MIB", "aixCdromModelName"),
        ("IBM-AIX-MIB", "aixCdromFRU"),
        ("IBM-AIX-MIB", "aixCdromPN"),
        ("IBM-AIX-MIB", "aixCdromEC"))
)
if mibBuilder.loadTexts:
    aixCDROMGroup.setStatus("current")

aixScsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 22)
)
aixScsiGroup.setObjects(
      *(("IBM-AIX-MIB", "aixScsiName"),
        ("IBM-AIX-MIB", "aixScsiDescr"),
        ("IBM-AIX-MIB", "aixScsiStatus"),
        ("IBM-AIX-MIB", "aixScsiLocation"),
        ("IBM-AIX-MIB", "aixScsiAdapterID"),
        ("IBM-AIX-MIB", "aixScsiIndex"))
)
if mibBuilder.loadTexts:
    aixScsiGroup.setStatus("current")

aixProcessorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 23)
)
aixProcessorGroup.setObjects(
      *(("IBM-AIX-MIB", "aixProcessorName"),
        ("IBM-AIX-MIB", "aixProcessorDescr"),
        ("IBM-AIX-MIB", "aixProcessorSpeed"),
        ("IBM-AIX-MIB", "aixProcessorType"),
        ("IBM-AIX-MIB", "aixProcessorIndex"))
)
if mibBuilder.loadTexts:
    aixProcessorGroup.setStatus("current")

aixNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 24)
)
aixNetworkGroup.setObjects(
      *(("IBM-AIX-MIB", "aixNetworkName"),
        ("IBM-AIX-MIB", "aixNetworkDescr"),
        ("IBM-AIX-MIB", "aixNetworkStatus"),
        ("IBM-AIX-MIB", "aixNetworkLocation"),
        ("IBM-AIX-MIB", "aixNetworkType"),
        ("IBM-AIX-MIB", "aixNetworkIndex"),
        ("IBM-AIX-MIB", "aixNetworkInterface"))
)
if mibBuilder.loadTexts:
    aixNetworkGroup.setStatus("current")

aixAdapterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 25)
)
aixAdapterGroup.setObjects(
      *(("IBM-AIX-MIB", "aixAdapterName"),
        ("IBM-AIX-MIB", "aixAdapterDescr"),
        ("IBM-AIX-MIB", "aixAdapterStatus"),
        ("IBM-AIX-MIB", "aixAdapterLocation"),
        ("IBM-AIX-MIB", "aixAdapterType"),
        ("IBM-AIX-MIB", "aixAdapterIndex"),
        ("IBM-AIX-MIB", "aixAdapterInterface"))
)
if mibBuilder.loadTexts:
    aixAdapterGroup.setStatus("current")


# Notification objects

aixFileSystemMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 1)
)
aixFileSystemMounted.setObjects(
    ("IBM-AIX-MIB", "aixFsName")
)
if mibBuilder.loadTexts:
    aixFileSystemMounted.setStatus(
        "current"
    )

aixFileSystemFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 2)
)
aixFileSystemFull.setObjects(
      *(("IBM-AIX-MIB", "aixFsName"),
        ("IBM-AIX-MIB", "aixFsSize"),
        ("IBM-AIX-MIB", "aixFsFree"),
        ("IBM-AIX-MIB", "aixFsThreshold"))
)
if mibBuilder.loadTexts:
    aixFileSystemFull.setStatus(
        "current"
    )

aixVolumeGroupFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 3)
)
aixVolumeGroupFull.setObjects(
      *(("IBM-AIX-MIB", "aixVgName"),
        ("IBM-AIX-MIB", "aixVgSize"),
        ("IBM-AIX-MIB", "aixVgFree"),
        ("IBM-AIX-MIB", "aixVgThreshold"))
)
if mibBuilder.loadTexts:
    aixVolumeGroupFull.setStatus(
        "current"
    )

aixPageFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 4)
)
aixPageFull.setObjects(
      *(("IBM-AIX-MIB", "aixPageName"),
        ("IBM-AIX-MIB", "aixPagePercentUsed"),
        ("IBM-AIX-MIB", "aixPageThreshold"))
)
if mibBuilder.loadTexts:
    aixPageFull.setStatus(
        "current"
    )

aixUserLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 5)
)
aixUserLoginFailed.setObjects(
    ("IBM-AIX-MIB", "aixFailedLoginTimePeriod")
)
if mibBuilder.loadTexts:
    aixUserLoginFailed.setStatus(
        "current"
    )

aixUtilizationCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 4, 6)
)
aixUtilizationCPU.setObjects(
      *(("IBM-AIX-MIB", "aixSeCPUUtilization"),
        ("IBM-AIX-MIB", "aixSeCPUThreshold"))
)
if mibBuilder.loadTexts:
    aixUtilizationCPU.setStatus(
        "current"
    )

aixSnmptrapHolder = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 1, 6, 1)
)
if mibBuilder.loadTexts:
    aixSnmptrapHolder.setStatus(
        "current"
    )


# Notifications groups

criticalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 1, 3)
)
criticalNotificationGroup.setObjects(
      *(("IBM-AIX-MIB", "aixFileSystemMounted"),
        ("IBM-AIX-MIB", "aixFileSystemFull"),
        ("IBM-AIX-MIB", "aixVolumeGroupFull"),
        ("IBM-AIX-MIB", "aixPageFull"),
        ("IBM-AIX-MIB", "aixUserLoginFailed"),
        ("IBM-AIX-MIB", "aixUtilizationCPU"),
        ("IBM-AIX-MIB", "aixSnmptrapHolder"))
)
if mibBuilder.loadTexts:
    criticalNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 191, 10, 2, 1)
)
if mibBuilder.loadTexts:
    aixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-AIX-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibmAIX": ibmAIX,
       "aixSystem": aixSystem,
       "aixAgent": aixAgent,
       "aixAgentAction": aixAgentAction,
       "aixAgentCmdString": aixAgentCmdString,
       "aixAgentExeCommand": aixAgentExeCommand,
       "aixAgentCmdResult": aixAgentCmdResult,
       "aixAgentPollInterval": aixAgentPollInterval,
       "aixPollEnable": aixPollEnable,
       "aixLastTrapMsg": aixLastTrapMsg,
       "aixAgentCmdOutTable": aixAgentCmdOutTable,
       "aixAgentCmdOutTableEntry": aixAgentCmdOutTableEntry,
       "aixAgentCmdOutput": aixAgentCmdOutput,
       "aixAgentCmdOutIndex": aixAgentCmdOutIndex,
       "aixFsPollInterval": aixFsPollInterval,
       "aixCPUPollInterval": aixCPUPollInterval,
       "aixVgPollInterval": aixVgPollInterval,
       "aixPagePollInterval": aixPagePollInterval,
       "aixLFPollInterval": aixLFPollInterval,
       "aixSystemEnvironment": aixSystemEnvironment,
       "aixSeCPUUtilization": aixSeCPUUtilization,
       "aixSeCPUThreshold": aixSeCPUThreshold,
       "aixSeSystemRunLevel": aixSeSystemRunLevel,
       "aixSeSystemState": aixSeSystemState,
       "aixSeSystemTrap": aixSeSystemTrap,
       "aixAuxSystemEnvironment": aixAuxSystemEnvironment,
       "aixSeDateAndTime": aixSeDateAndTime,
       "aixSeMaxProcPerUser": aixSeMaxProcPerUser,
       "aixSeLicenseNum": aixSeLicenseNum,
       "aixSeRemainingLicenseNum": aixSeRemainingLicenseNum,
       "aixSeNumCPUs": aixSeNumCPUs,
       "aixSeMachineType": aixSeMachineType,
       "aixSeSerialNumber": aixSeSerialNumber,
       "aixTrap": aixTrap,
       "aixFileSystemMounted": aixFileSystemMounted,
       "aixFileSystemFull": aixFileSystemFull,
       "aixVolumeGroupFull": aixVolumeGroupFull,
       "aixPageFull": aixPageFull,
       "aixUserLoginFailed": aixUserLoginFailed,
       "aixUtilizationCPU": aixUtilizationCPU,
       "aixGeneralTrap": aixGeneralTrap,
       "aixSnmptrapHolder": aixSnmptrapHolder,
       "aixStorageSystem": aixStorageSystem,
       "aixVolumeGroup": aixVolumeGroup,
       "aixVgThreshold": aixVgThreshold,
       "aixVgTable": aixVgTable,
       "aixVgEntry": aixVgEntry,
       "aixVgName": aixVgName,
       "aixVgIdentifier": aixVgIdentifier,
       "aixVgState": aixVgState,
       "aixVgSize": aixVgSize,
       "aixVgFree": aixVgFree,
       "aixVgCurNumLVs": aixVgCurNumLVs,
       "aixVgOpenLVs": aixVgOpenLVs,
       "aixVgActivePVs": aixVgActivePVs,
       "aixVgIndex": aixVgIndex,
       "aixLogicalVolume": aixLogicalVolume,
       "aixLvTable": aixLvTable,
       "aixLvEntry": aixLvEntry,
       "aixLvName": aixLvName,
       "aixLvNameVG": aixLvNameVG,
       "aixLvType": aixLvType,
       "aixLvMountPoint": aixLvMountPoint,
       "aixLvSize": aixLvSize,
       "aixLvState": aixLvState,
       "aixLvIndex": aixLvIndex,
       "aixPhysicalVolume": aixPhysicalVolume,
       "aixPvTable": aixPvTable,
       "aixPvEntry": aixPvEntry,
       "aixPvName": aixPvName,
       "aixPvNameVG": aixPvNameVG,
       "aixPvState": aixPvState,
       "aixPvSize": aixPvSize,
       "aixPvFree": aixPvFree,
       "aixPvNumLVs": aixPvNumLVs,
       "aixPvIndex": aixPvIndex,
       "aixPagingSpace": aixPagingSpace,
       "aixPageThreshold": aixPageThreshold,
       "aixPageTable": aixPageTable,
       "aixPageEntry": aixPageEntry,
       "aixPageName": aixPageName,
       "aixPageNameVG": aixPageNameVG,
       "aixPageNamePV": aixPageNamePV,
       "aixPageSize": aixPageSize,
       "aixPagePercentUsed": aixPagePercentUsed,
       "aixPageStatus": aixPageStatus,
       "aixPageType": aixPageType,
       "aixPageIndex": aixPageIndex,
       "aixPrintSystem": aixPrintSystem,
       "aixPrtQueue": aixPrtQueue,
       "aixPrtQueTable": aixPrtQueTable,
       "aixPrtQueEntry": aixPrtQueEntry,
       "aixPrtQueName": aixPrtQueName,
       "aixPrtQueDevice": aixPrtQueDevice,
       "aixPrtQueStatus": aixPrtQueStatus,
       "aixPrtQueAction": aixPrtQueAction,
       "aixPrtQueDescipline": aixPrtQueDescipline,
       "aixPrtQueAcctFile": aixPrtQueAcctFile,
       "aixPrtQueHost": aixPrtQueHost,
       "aixPrtQueRQ": aixPrtQueRQ,
       "aixPrtQueJobNum": aixPrtQueJobNum,
       "aixPrtQueIndex": aixPrtQueIndex,
       "aixUser": aixUser,
       "aixUsers": aixUsers,
       "aixUsrTable": aixUsrTable,
       "aixUsrEntry": aixUsrEntry,
       "aixUsrName": aixUsrName,
       "aixUsrID": aixUsrID,
       "aixUsrHome": aixUsrHome,
       "aixUsrShell": aixUsrShell,
       "aixUsrLocalLogin": aixUsrLocalLogin,
       "aixUsrRemoteLogin": aixUsrRemoteLogin,
       "aixUsrPasswdMaxAge": aixUsrPasswdMaxAge,
       "aixUsrStatus": aixUsrStatus,
       "aixUsrGroups": aixUsrGroups,
       "aixUsrAllowableAttempts": aixUsrAllowableAttempts,
       "aixUsrResetLoginCount": aixUsrResetLoginCount,
       "aixUsrPrimaryGroup": aixUsrPrimaryGroup,
       "aixUsrIndex": aixUsrIndex,
       "aixGroups": aixGroups,
       "aixGrpTable": aixGrpTable,
       "aixGrpEntry": aixGrpEntry,
       "aixGrpIndex": aixGrpIndex,
       "aixGrpName": aixGrpName,
       "aixGrpID": aixGrpID,
       "aixGrpAdminGroup": aixGrpAdminGroup,
       "aixGrpUsrList": aixGrpUsrList,
       "aixGrpAdmList": aixGrpAdmList,
       "aixService": aixService,
       "aixSrvSubsystem": aixSrvSubsystem,
       "aixSubSystemNum": aixSubSystemNum,
       "aixSubSysTable": aixSubSysTable,
       "aixSubSysEntry": aixSubSysEntry,
       "aixSubSysName": aixSubSysName,
       "aixSubSysGroup": aixSubSysGroup,
       "aixSubSysPID": aixSubSysPID,
       "aixSubSysStatus": aixSubSysStatus,
       "aixSubSysIndex": aixSubSysIndex,
       "aixSrvSubserver": aixSrvSubserver,
       "aixSubSrvNum": aixSubSrvNum,
       "aixSubSrvTable": aixSubSrvTable,
       "aixSubSrvEntry": aixSubSrvEntry,
       "aixSubSrvName": aixSubSrvName,
       "aixSubSrvDescr": aixSubSrvDescr,
       "aixSubSrvCommand": aixSubSrvCommand,
       "aixSubSrvStatus": aixSubSrvStatus,
       "aixSubSrvSubsys": aixSubSrvSubsys,
       "aixSubSrvIndex": aixSubSrvIndex,
       "aixFileSystem": aixFileSystem,
       "aixFsThreshold": aixFsThreshold,
       "aixFsTable": aixFsTable,
       "aixFsTableEntry": aixFsTableEntry,
       "aixFsIndex": aixFsIndex,
       "aixFsName": aixFsName,
       "aixFsMountPoint": aixFsMountPoint,
       "aixFsType": aixFsType,
       "aixFsSize": aixFsSize,
       "aixFsFree": aixFsFree,
       "aixFsNumINodes": aixFsNumINodes,
       "aixFsUsedInodes": aixFsUsedInodes,
       "aixFsStatus": aixFsStatus,
       "aixFsExecution": aixFsExecution,
       "aixFsResultMsg": aixFsResultMsg,
       "aixProcess": aixProcess,
       "aixProcNum": aixProcNum,
       "aixProcTable": aixProcTable,
       "aixProcEntry": aixProcEntry,
       "aixProcPID": aixProcPID,
       "aixProcUID": aixProcUID,
       "aixProcPPID": aixProcPPID,
       "aixProcGroup": aixProcGroup,
       "aixProcPriority": aixProcPriority,
       "aixProcCMD": aixProcCMD,
       "aixProcCPU": aixProcCPU,
       "aixProcStart": aixProcStart,
       "aixProcStatus": aixProcStatus,
       "aixProcTTY": aixProcTTY,
       "aixLogin": aixLogin,
       "aixFailedLoginTimePeriod": aixFailedLoginTimePeriod,
       "aixLoginFailedThreshold": aixLoginFailedThreshold,
       "aixLoginUserTable": aixLoginUserTable,
       "aixLoginUserEntry": aixLoginUserEntry,
       "aixLoginUserName": aixLoginUserName,
       "aixLoginUserTTY": aixLoginUserTTY,
       "aixLoginUserHost": aixLoginUserHost,
       "aixLoginUserDateAndTime": aixLoginUserDateAndTime,
       "aixLoginUserIndex": aixLoginUserIndex,
       "aixDevice": aixDevice,
       "aixPrinter": aixPrinter,
       "aixPrinterTable": aixPrinterTable,
       "aixPrinterEntry": aixPrinterEntry,
       "aixPrinterName": aixPrinterName,
       "aixPrinterIndex": aixPrinterIndex,
       "aixPrinterType": aixPrinterType,
       "aixPrinterInterface": aixPrinterInterface,
       "aixPrinterStatus": aixPrinterStatus,
       "aixPrinterDescr": aixPrinterDescr,
       "aixPrinterLocation": aixPrinterLocation,
       "aixPrinterPortNumber": aixPrinterPortNumber,
       "aixTape": aixTape,
       "aixTapeDrvTable": aixTapeDrvTable,
       "aixTapeDrvEntry": aixTapeDrvEntry,
       "aixTapeDrvName": aixTapeDrvName,
       "aixTapeDrvIndex": aixTapeDrvIndex,
       "aixTapeDrvType": aixTapeDrvType,
       "aixTapeDrvInterface": aixTapeDrvInterface,
       "aixTapeDrvStatus": aixTapeDrvStatus,
       "aixTapeDrvDescr": aixTapeDrvDescr,
       "aixTapeDrvLocation": aixTapeDrvLocation,
       "aixTapeDrvBlkSize": aixTapeDrvBlkSize,
       "aixTapeDrvManufacturerName": aixTapeDrvManufacturerName,
       "aixTapeDrvModelName": aixTapeDrvModelName,
       "aixTapeDrvSN": aixTapeDrvSN,
       "aixTapeDrvPN": aixTapeDrvPN,
       "aixTapeDrvFRU": aixTapeDrvFRU,
       "aixTapeDrvEC": aixTapeDrvEC,
       "aixHardDisk": aixHardDisk,
       "aixHdTable": aixHdTable,
       "aixHdEntry": aixHdEntry,
       "aixHdName": aixHdName,
       "aixHdIndex": aixHdIndex,
       "aixHdType": aixHdType,
       "aixHdSize": aixHdSize,
       "aixHdInterface": aixHdInterface,
       "aixHdStatus": aixHdStatus,
       "aixHdLocation": aixHdLocation,
       "aixHdIdentifier": aixHdIdentifier,
       "aixHdDescr": aixHdDescr,
       "aixHdManufacturerName": aixHdManufacturerName,
       "aixHdModelName": aixHdModelName,
       "aixHdSN": aixHdSN,
       "aixHdPN": aixHdPN,
       "aixHdFRU": aixHdFRU,
       "aixHdEC": aixHdEC,
       "aixMemory": aixMemory,
       "aixMemTable": aixMemTable,
       "aixMemEntry": aixMemEntry,
       "aixMemName": aixMemName,
       "aixMemIndex": aixMemIndex,
       "aixMemLocation": aixMemLocation,
       "aixMemSize": aixMemSize,
       "aixMemDescr": aixMemDescr,
       "aixCDROM": aixCDROM,
       "aixCdromTable": aixCdromTable,
       "aixCdromEntry": aixCdromEntry,
       "aixCdromName": aixCdromName,
       "aixCdromIndex": aixCdromIndex,
       "aixCdromType": aixCdromType,
       "aixCdromInterface": aixCdromInterface,
       "aixCdromDescr": aixCdromDescr,
       "aixCdromStatus": aixCdromStatus,
       "aixCdromLocation": aixCdromLocation,
       "aixCdromManufacturerName": aixCdromManufacturerName,
       "aixCdromModelName": aixCdromModelName,
       "aixCdromPN": aixCdromPN,
       "aixCdromFRU": aixCdromFRU,
       "aixCdromEC": aixCdromEC,
       "aixScsi": aixScsi,
       "aixScsiTable": aixScsiTable,
       "aixScsiEntry": aixScsiEntry,
       "aixScsiName": aixScsiName,
       "aixScsiIndex": aixScsiIndex,
       "aixScsiDescr": aixScsiDescr,
       "aixScsiStatus": aixScsiStatus,
       "aixScsiLocation": aixScsiLocation,
       "aixScsiAdapterID": aixScsiAdapterID,
       "aixProcessor": aixProcessor,
       "aixProcessorTable": aixProcessorTable,
       "aixProcessorEntry": aixProcessorEntry,
       "aixProcessorName": aixProcessorName,
       "aixProcessorIndex": aixProcessorIndex,
       "aixProcessorType": aixProcessorType,
       "aixProcessorDescr": aixProcessorDescr,
       "aixProcessorSpeed": aixProcessorSpeed,
       "aixNetwork": aixNetwork,
       "aixNetworkTable": aixNetworkTable,
       "aixNetworkEntry": aixNetworkEntry,
       "aixNetworkName": aixNetworkName,
       "aixNetworkIndex": aixNetworkIndex,
       "aixNetworkType": aixNetworkType,
       "aixNetworkInterface": aixNetworkInterface,
       "aixNetworkStatus": aixNetworkStatus,
       "aixNetworkLocation": aixNetworkLocation,
       "aixNetworkDescr": aixNetworkDescr,
       "aixAdapter": aixAdapter,
       "aixAdapterTable": aixAdapterTable,
       "aixAdapterEntry": aixAdapterEntry,
       "aixAdapterName": aixAdapterName,
       "aixAdapterIndex": aixAdapterIndex,
       "aixAdapterType": aixAdapterType,
       "aixAdapterInterface": aixAdapterInterface,
       "aixAdapterStatus": aixAdapterStatus,
       "aixAdapterLocation": aixAdapterLocation,
       "aixAdapterDescr": aixAdapterDescr,
       "aixConformance": aixConformance,
       "aixCfmGroup": aixCfmGroup,
       "aixAgentGroup": aixAgentGroup,
       "aixSeGroup": aixSeGroup,
       "criticalNotificationGroup": criticalNotificationGroup,
       "aixVGGroup": aixVGGroup,
       "aixLVGroup": aixLVGroup,
       "aixPVGroup": aixPVGroup,
       "aixPagingSpaceGroup": aixPagingSpaceGroup,
       "aixFsGroup": aixFsGroup,
       "aixProcessGroup": aixProcessGroup,
       "aixLoginUsrGroup": aixLoginUsrGroup,
       "aixPrtQueueGroup": aixPrtQueueGroup,
       "aixUsrGroup": aixUsrGroup,
       "aixGrpGroup": aixGrpGroup,
       "aixSubSystemGroup": aixSubSystemGroup,
       "aixSubServerGroup": aixSubServerGroup,
       "aixSeAuxGroup": aixSeAuxGroup,
       "aixPrinterGroup": aixPrinterGroup,
       "aixTapeGroup": aixTapeGroup,
       "aixHardDiskGroup": aixHardDiskGroup,
       "aixMemoryGroup": aixMemoryGroup,
       "aixCDROMGroup": aixCDROMGroup,
       "aixScsiGroup": aixScsiGroup,
       "aixProcessorGroup": aixProcessorGroup,
       "aixNetworkGroup": aixNetworkGroup,
       "aixAdapterGroup": aixAdapterGroup,
       "aixCompliances": aixCompliances,
       "aixCompliance": aixCompliance}
)
