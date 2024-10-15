# SNMP MIB module (APEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:21 2024
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

(giproducts,) = mibBuilder.importSymbols(
    "BCS-IDENT-MIB",
    "giproducts")

(trapAdditionalInfoInteger1,
 trapAdditionalInfoInteger2,
 trapAdditionalInfoInteger3,
 trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapChangedValueIpAddress,
 trapChangedValueOID,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapSequenceId,
 trapText) = mibBuilder.importSymbols(
    "BCS-TRAPS-MIB",
    "trapAdditionalInfoInteger1",
    "trapAdditionalInfoInteger2",
    "trapAdditionalInfoInteger3",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapChangedValueIpAddress",
    "trapChangedValueOID",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapSequenceId",
    "trapText")

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

apex = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31)
)
apex.setRevisions(
        ("2011-02-15 00:00",
         "2010-08-17 00:00",
         "2010-06-30 00:00",
         "2010-03-05 00:00",
         "2010-01-19 00:00",
         "2009-10-16 00:00",
         "2009-09-14 00:00",
         "2009-06-09 00:00",
         "2009-04-20 00:00",
         "2009-04-08 00:00",
         "2009-04-14 00:00",
         "2009-03-23 00:00",
         "2009-03-10 00:00",
         "2008-07-24 00:00",
         "2008-07-08 00:00",
         "2008-02-18 14:00")
)


# Types definitions



class EnableDisableTYPE(Integer32):
    """Custom type EnableDisableTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class ActiveTYPE(Integer32):
    """Custom type ActiveTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1),
          ("notApplicable", 0))
    )





class ApplyDataToDeviceTYPE(Integer32):
    """Custom type ApplyDataToDeviceTYPE based on Integer32"""
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
        *(("apply", 2),
          ("applyNotInProgress", 1),
          ("applyNotInProgressInvalidData", 4),
          ("applyNotInProgressValidData", 3))
    )





class ResetStatisticsTYPE(Integer32):
    """Custom type ResetStatisticsTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("resetNotInProgress", 1))
    )





class ClearAlarmTYPE(Integer32):
    """Custom type ClearAlarmTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarm", 2),
          ("clearAlarmNotInProgress", 1))
    )





class RateComparisonTYPE(Integer32):
    """Custom type RateComparisonTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataRate", 1),
          ("transportStreamRate", 2))
    )





class InputTsStateTYPE(Integer32):
    """Custom type InputTsStateTYPE based on Integer32"""
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
        *(("closed", 0),
          ("openedBackup", 2),
          ("openedInUse", 1),
          ("openedTransToBackup", 3),
          ("openedTransToInUse", 4))
    )





class EthernetInterfaceTYPE(Integer32):
    """Custom type EthernetInterfaceTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet1", 1),
          ("enet2", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApexTraps_ObjectIdentity = ObjectIdentity
apexTraps = _ApexTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0)
)
_ApexSys_ObjectIdentity = ObjectIdentity
apexSys = _ApexSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1)
)
_ApexSysConfig_ObjectIdentity = ObjectIdentity
apexSysConfig = _ApexSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1)
)
_ApexSysConfigGeneral_ObjectIdentity = ObjectIdentity
apexSysConfigGeneral = _ApexSysConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 1)
)


class _ApexSaveConfig_Type(Integer32):
    """Custom type apexSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saveNotInProgress", 1),
          ("savingConfigToFlash", 3),
          ("startSaveToFlash", 2))
    )


_ApexSaveConfig_Type.__name__ = "Integer32"
_ApexSaveConfig_Object = MibScalar
apexSaveConfig = _ApexSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 1, 1),
    _ApexSaveConfig_Type()
)
apexSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSaveConfig.setStatus("current")


class _ApexProductName_Type(DisplayString):
    """Custom type apexProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexProductName_Type.__name__ = "DisplayString"
_ApexProductName_Object = MibScalar
apexProductName = _ApexProductName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 1, 2),
    _ApexProductName_Type()
)
apexProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexProductName.setStatus("current")


class _ApexBootMethod_Type(Integer32):
    """Custom type apexBootMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootpOnly", 3),
          ("noDhcpOrBootp", 1))
    )


_ApexBootMethod_Type.__name__ = "Integer32"
_ApexBootMethod_Object = MibScalar
apexBootMethod = _ApexBootMethod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 1, 3),
    _ApexBootMethod_Type()
)
apexBootMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexBootMethod.setStatus("current")
_ApexAutoRebootEnable_Type = EnableDisableTYPE
_ApexAutoRebootEnable_Object = MibScalar
apexAutoRebootEnable = _ApexAutoRebootEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 1, 4),
    _ApexAutoRebootEnable_Type()
)
apexAutoRebootEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexAutoRebootEnable.setStatus("current")
_ApexSysConfigMcEmmInsertion_ObjectIdentity = ObjectIdentity
apexSysConfigMcEmmInsertion = _ApexSysConfigMcEmmInsertion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2)
)


class _ApexMcEmmInsertionMode_Type(Integer32):
    """Custom type apexMcEmmInsertionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullInBand", 2),
          ("outOfBand", 1))
    )


_ApexMcEmmInsertionMode_Type.__name__ = "Integer32"
_ApexMcEmmInsertionMode_Object = MibScalar
apexMcEmmInsertionMode = _ApexMcEmmInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 1),
    _ApexMcEmmInsertionMode_Type()
)
apexMcEmmInsertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionMode.setStatus("current")
_ApexMcEmmInsertionPid1Enable_Type = EnableDisableTYPE
_ApexMcEmmInsertionPid1Enable_Object = MibScalar
apexMcEmmInsertionPid1Enable = _ApexMcEmmInsertionPid1Enable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 2),
    _ApexMcEmmInsertionPid1Enable_Type()
)
apexMcEmmInsertionPid1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionPid1Enable.setStatus("current")


class _ApexMcEmmInsertionPid1_Type(Unsigned32):
    """Custom type apexMcEmmInsertionPid1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7168, 8190),
    )


_ApexMcEmmInsertionPid1_Type.__name__ = "Unsigned32"
_ApexMcEmmInsertionPid1_Object = MibScalar
apexMcEmmInsertionPid1 = _ApexMcEmmInsertionPid1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 3),
    _ApexMcEmmInsertionPid1_Type()
)
apexMcEmmInsertionPid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionPid1.setStatus("current")
_ApexMcEmmInsertionPid2Enable_Type = EnableDisableTYPE
_ApexMcEmmInsertionPid2Enable_Object = MibScalar
apexMcEmmInsertionPid2Enable = _ApexMcEmmInsertionPid2Enable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 4),
    _ApexMcEmmInsertionPid2Enable_Type()
)
apexMcEmmInsertionPid2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionPid2Enable.setStatus("current")


class _ApexMcEmmInsertionPid2_Type(Unsigned32):
    """Custom type apexMcEmmInsertionPid2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7168, 8190),
    )


_ApexMcEmmInsertionPid2_Type.__name__ = "Unsigned32"
_ApexMcEmmInsertionPid2_Object = MibScalar
apexMcEmmInsertionPid2 = _ApexMcEmmInsertionPid2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 5),
    _ApexMcEmmInsertionPid2_Type()
)
apexMcEmmInsertionPid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionPid2.setStatus("current")
_ApexMcEmmInsertionApplyChange_Type = ApplyDataToDeviceTYPE
_ApexMcEmmInsertionApplyChange_Object = MibScalar
apexMcEmmInsertionApplyChange = _ApexMcEmmInsertionApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 1, 2, 6),
    _ApexMcEmmInsertionApplyChange_Type()
)
apexMcEmmInsertionApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexMcEmmInsertionApplyChange.setStatus("current")
_ApexSysStatus_ObjectIdentity = ObjectIdentity
apexSysStatus = _ApexSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2)
)
_ApexSysStatusGeneral_ObjectIdentity = ObjectIdentity
apexSysStatusGeneral = _ApexSysStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 1)
)


class _ApexBootReason_Type(Integer32):
    """Custom type apexBootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwFault", 2),
          ("operatorReboot", 1),
          ("powerCycle", 0),
          ("wdFault", 3))
    )


_ApexBootReason_Type.__name__ = "Integer32"
_ApexBootReason_Object = MibScalar
apexBootReason = _ApexBootReason_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 1, 1),
    _ApexBootReason_Type()
)
apexBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexBootReason.setStatus("current")
_ApexMaxServiceMappings_Type = Integer32
_ApexMaxServiceMappings_Object = MibScalar
apexMaxServiceMappings = _ApexMaxServiceMappings_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 1, 2),
    _ApexMaxServiceMappings_Type()
)
apexMaxServiceMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMaxServiceMappings.setStatus("current")
_ApexSysStatusVersions_ObjectIdentity = ObjectIdentity
apexSysStatusVersions = _ApexSysStatusVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2)
)


class _ApexHostProcessorBootCodeVersion_Type(DisplayString):
    """Custom type apexHostProcessorBootCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexHostProcessorBootCodeVersion_Type.__name__ = "DisplayString"
_ApexHostProcessorBootCodeVersion_Object = MibScalar
apexHostProcessorBootCodeVersion = _ApexHostProcessorBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 1),
    _ApexHostProcessorBootCodeVersion_Type()
)
apexHostProcessorBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHostProcessorBootCodeVersion.setStatus("current")


class _ApexMuxFpgaVersion_Type(DisplayString):
    """Custom type apexMuxFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexMuxFpgaVersion_Type.__name__ = "DisplayString"
_ApexMuxFpgaVersion_Object = MibScalar
apexMuxFpgaVersion = _ApexMuxFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 2),
    _ApexMuxFpgaVersion_Type()
)
apexMuxFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMuxFpgaVersion.setStatus("current")


class _ApexMuxFpgaEncryption_Type(Integer32):
    """Custom type apexMuxFpgaEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("csa", 2),
          ("des", 1),
          ("noEncryption", 0))
    )


_ApexMuxFpgaEncryption_Type.__name__ = "Integer32"
_ApexMuxFpgaEncryption_Object = MibScalar
apexMuxFpgaEncryption = _ApexMuxFpgaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 3),
    _ApexMuxFpgaEncryption_Type()
)
apexMuxFpgaEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMuxFpgaEncryption.setStatus("current")


class _ApexMainBoardVersion_Type(DisplayString):
    """Custom type apexMainBoardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexMainBoardVersion_Type.__name__ = "DisplayString"
_ApexMainBoardVersion_Object = MibScalar
apexMainBoardVersion = _ApexMainBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 4),
    _ApexMainBoardVersion_Type()
)
apexMainBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardVersion.setStatus("current")


class _ApexHostApplicationDate_Type(DisplayString):
    """Custom type apexHostApplicationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexHostApplicationDate_Type.__name__ = "DisplayString"
_ApexHostApplicationDate_Object = MibScalar
apexHostApplicationDate = _ApexHostApplicationDate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 5),
    _ApexHostApplicationDate_Type()
)
apexHostApplicationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHostApplicationDate.setStatus("current")


class _ApexProductType_Type(Integer32):
    """Custom type apexProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apex1000", 1),
          ("invalid", 0))
    )


_ApexProductType_Type.__name__ = "Integer32"
_ApexProductType_Object = MibScalar
apexProductType = _ApexProductType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 6),
    _ApexProductType_Type()
)
apexProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexProductType.setStatus("current")
_ApexMainBoardType_Type = Integer32
_ApexMainBoardType_Object = MibScalar
apexMainBoardType = _ApexMainBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 7),
    _ApexMainBoardType_Type()
)
apexMainBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardType.setStatus("current")


class _ApexGlueFpgaVersion_Type(DisplayString):
    """Custom type apexGlueFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexGlueFpgaVersion_Type.__name__ = "DisplayString"
_ApexGlueFpgaVersion_Object = MibScalar
apexGlueFpgaVersion = _ApexGlueFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 8),
    _ApexGlueFpgaVersion_Type()
)
apexGlueFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGlueFpgaVersion.setStatus("current")


class _ApexGlueCpldVersion_Type(DisplayString):
    """Custom type apexGlueCpldVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexGlueCpldVersion_Type.__name__ = "DisplayString"
_ApexGlueCpldVersion_Object = MibScalar
apexGlueCpldVersion = _ApexGlueCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 9),
    _ApexGlueCpldVersion_Type()
)
apexGlueCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGlueCpldVersion.setStatus("current")


class _ApexDtiFpgaVersion_Type(DisplayString):
    """Custom type apexDtiFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexDtiFpgaVersion_Type.__name__ = "DisplayString"
_ApexDtiFpgaVersion_Object = MibScalar
apexDtiFpgaVersion = _ApexDtiFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 10),
    _ApexDtiFpgaVersion_Type()
)
apexDtiFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDtiFpgaVersion.setStatus("current")


class _ApexMpc2FpgaVersion_Type(DisplayString):
    """Custom type apexMpc2FpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexMpc2FpgaVersion_Type.__name__ = "DisplayString"
_ApexMpc2FpgaVersion_Object = MibScalar
apexMpc2FpgaVersion = _ApexMpc2FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 11),
    _ApexMpc2FpgaVersion_Type()
)
apexMpc2FpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMpc2FpgaVersion.setStatus("current")


class _ApexDpmVersion_Type(DisplayString):
    """Custom type apexDpmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexDpmVersion_Type.__name__ = "DisplayString"
_ApexDpmVersion_Object = MibScalar
apexDpmVersion = _ApexDpmVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 1, 2, 2, 12),
    _ApexDpmVersion_Type()
)
apexDpmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDpmVersion.setStatus("current")
_ApexTime_ObjectIdentity = ObjectIdentity
apexTime = _ApexTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2)
)
_ApexTimeConfig_ObjectIdentity = ObjectIdentity
apexTimeConfig = _ApexTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1)
)
_ApexTimeConfigGeneral_ObjectIdentity = ObjectIdentity
apexTimeConfigGeneral = _ApexTimeConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1)
)


class _ApexTimeSource_Type(Integer32):
    """Custom type apexTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("sntp", 1))
    )


_ApexTimeSource_Type.__name__ = "Integer32"
_ApexTimeSource_Object = MibScalar
apexTimeSource = _ApexTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1, 1),
    _ApexTimeSource_Type()
)
apexTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexTimeSource.setStatus("current")


class _ApexSntpUtcOffset_Type(Integer32):
    """Custom type apexSntpUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApexSntpUtcOffset_Type.__name__ = "Integer32"
_ApexSntpUtcOffset_Object = MibScalar
apexSntpUtcOffset = _ApexSntpUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1, 2),
    _ApexSntpUtcOffset_Type()
)
apexSntpUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSntpUtcOffset.setStatus("current")


class _ApexSntpServerSpecified_Type(Integer32):
    """Custom type apexSntpServerSpecified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("specified", 2))
    )


_ApexSntpServerSpecified_Type.__name__ = "Integer32"
_ApexSntpServerSpecified_Object = MibScalar
apexSntpServerSpecified = _ApexSntpServerSpecified_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1, 3),
    _ApexSntpServerSpecified_Type()
)
apexSntpServerSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSntpServerSpecified.setStatus("current")
_ApexSntpServerIpAddr_Type = IpAddress
_ApexSntpServerIpAddr_Object = MibScalar
apexSntpServerIpAddr = _ApexSntpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1, 4),
    _ApexSntpServerIpAddr_Type()
)
apexSntpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSntpServerIpAddr.setStatus("current")
_ApexUserSuppliedTime_Type = Unsigned32
_ApexUserSuppliedTime_Object = MibScalar
apexUserSuppliedTime = _ApexUserSuppliedTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 1, 1, 5),
    _ApexUserSuppliedTime_Type()
)
apexUserSuppliedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUserSuppliedTime.setStatus("current")
_ApexTimeStatus_ObjectIdentity = ObjectIdentity
apexTimeStatus = _ApexTimeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 2)
)
_ApexTimeStatusGeneral_ObjectIdentity = ObjectIdentity
apexTimeStatusGeneral = _ApexTimeStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 2, 1)
)
_ApexSystemTime_Type = Integer32
_ApexSystemTime_Object = MibScalar
apexSystemTime = _ApexSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 2, 1, 1),
    _ApexSystemTime_Type()
)
apexSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexSystemTime.setStatus("current")
_ApexOperationalTime_Type = Integer32
_ApexOperationalTime_Object = MibScalar
apexOperationalTime = _ApexOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 2, 2, 1, 8),
    _ApexOperationalTime_Type()
)
apexOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOperationalTime.setStatus("current")
_ApexTemperature_ObjectIdentity = ObjectIdentity
apexTemperature = _ApexTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3)
)
_ApexTemperatureConfig_ObjectIdentity = ObjectIdentity
apexTemperatureConfig = _ApexTemperatureConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 1)
)
_ApexTemperatureConfigGeneral_ObjectIdentity = ObjectIdentity
apexTemperatureConfigGeneral = _ApexTemperatureConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 1, 1)
)
_ApexTemperatureStatus_ObjectIdentity = ObjectIdentity
apexTemperatureStatus = _ApexTemperatureStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2)
)
_ApexTemperatureStatusGeneral_ObjectIdentity = ObjectIdentity
apexTemperatureStatusGeneral = _ApexTemperatureStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 1)
)
_ApexMainBoardTemperature_ObjectIdentity = ObjectIdentity
apexMainBoardTemperature = _ApexMainBoardTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 2)
)
_ApexMainBoardTempFrontIntake_Type = Integer32
_ApexMainBoardTempFrontIntake_Object = MibScalar
apexMainBoardTempFrontIntake = _ApexMainBoardTempFrontIntake_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 2, 1),
    _ApexMainBoardTempFrontIntake_Type()
)
apexMainBoardTempFrontIntake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempFrontIntake.setStatus("current")
_ApexMainBoardTempMuxFpga_Type = Integer32
_ApexMainBoardTempMuxFpga_Object = MibScalar
apexMainBoardTempMuxFpga = _ApexMainBoardTempMuxFpga_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 2, 2),
    _ApexMainBoardTempMuxFpga_Type()
)
apexMainBoardTempMuxFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempMuxFpga.setStatus("current")
_ApexMainBoardTempAcpModule_Type = Integer32
_ApexMainBoardTempAcpModule_Object = MibScalar
apexMainBoardTempAcpModule = _ApexMainBoardTempAcpModule_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 2, 3),
    _ApexMainBoardTempAcpModule_Type()
)
apexMainBoardTempAcpModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempAcpModule.setStatus("current")
_ApexMainBoardTempHostProcessor_Type = Integer32
_ApexMainBoardTempHostProcessor_Object = MibScalar
apexMainBoardTempHostProcessor = _ApexMainBoardTempHostProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 2, 4),
    _ApexMainBoardTempHostProcessor_Type()
)
apexMainBoardTempHostProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempHostProcessor.setStatus("current")
_ApexMainBoardTemperatureFault_ObjectIdentity = ObjectIdentity
apexMainBoardTemperatureFault = _ApexMainBoardTemperatureFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 3)
)


class _ApexMainBoardTempFrontIntakeFault_Type(Integer32):
    """Custom type apexMainBoardTempFrontIntakeFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexMainBoardTempFrontIntakeFault_Type.__name__ = "Integer32"
_ApexMainBoardTempFrontIntakeFault_Object = MibScalar
apexMainBoardTempFrontIntakeFault = _ApexMainBoardTempFrontIntakeFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 3, 1),
    _ApexMainBoardTempFrontIntakeFault_Type()
)
apexMainBoardTempFrontIntakeFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempFrontIntakeFault.setStatus("current")


class _ApexMainBoardTempMuxFpgaFault_Type(Integer32):
    """Custom type apexMainBoardTempMuxFpgaFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexMainBoardTempMuxFpgaFault_Type.__name__ = "Integer32"
_ApexMainBoardTempMuxFpgaFault_Object = MibScalar
apexMainBoardTempMuxFpgaFault = _ApexMainBoardTempMuxFpgaFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 3, 2),
    _ApexMainBoardTempMuxFpgaFault_Type()
)
apexMainBoardTempMuxFpgaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempMuxFpgaFault.setStatus("current")


class _ApexMainBoardTempAcpModuleFault_Type(Integer32):
    """Custom type apexMainBoardTempAcpModuleFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexMainBoardTempAcpModuleFault_Type.__name__ = "Integer32"
_ApexMainBoardTempAcpModuleFault_Object = MibScalar
apexMainBoardTempAcpModuleFault = _ApexMainBoardTempAcpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 3, 3),
    _ApexMainBoardTempAcpModuleFault_Type()
)
apexMainBoardTempAcpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempAcpModuleFault.setStatus("current")


class _ApexMainBoardTempHostProcessorFault_Type(Integer32):
    """Custom type apexMainBoardTempHostProcessorFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexMainBoardTempHostProcessorFault_Type.__name__ = "Integer32"
_ApexMainBoardTempHostProcessorFault_Object = MibScalar
apexMainBoardTempHostProcessorFault = _ApexMainBoardTempHostProcessorFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 3, 2, 3, 4),
    _ApexMainBoardTempHostProcessorFault_Type()
)
apexMainBoardTempHostProcessorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMainBoardTempHostProcessorFault.setStatus("current")
_ApexPowerSupply_ObjectIdentity = ObjectIdentity
apexPowerSupply = _ApexPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4)
)
_ApexPsConfig_ObjectIdentity = ObjectIdentity
apexPsConfig = _ApexPsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 1)
)
_ApexPsConfigGeneral_ObjectIdentity = ObjectIdentity
apexPsConfigGeneral = _ApexPsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 1, 1)
)
_ApexPsStatus_ObjectIdentity = ObjectIdentity
apexPsStatus = _ApexPsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2)
)
_ApexPsStatusGeneral_ObjectIdentity = ObjectIdentity
apexPsStatusGeneral = _ApexPsStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 1)
)
_ApexPsStatusTable_Object = MibTable
apexPsStatusTable = _ApexPsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2)
)
if mibBuilder.loadTexts:
    apexPsStatusTable.setStatus("current")
_ApexPsStatusEntry_Object = MibTableRow
apexPsStatusEntry = _ApexPsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1)
)
apexPsStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsStatusPsNum"),
)
if mibBuilder.loadTexts:
    apexPsStatusEntry.setStatus("current")


class _ApexPsStatusPsNum_Type(Integer32):
    """Custom type apexPsStatusPsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexPsStatusPsNum_Type.__name__ = "Integer32"
_ApexPsStatusPsNum_Object = MibTableColumn
apexPsStatusPsNum = _ApexPsStatusPsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 1),
    _ApexPsStatusPsNum_Type()
)
apexPsStatusPsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsStatusPsNum.setStatus("current")


class _ApexPsStatusInstalled_Type(Integer32):
    """Custom type apexPsStatusInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fanModuleInstalled", 4),
          ("installedAcInput", 2),
          ("installedDcInput", 3),
          ("notApplicable", 0),
          ("notInstalled", 1),
          ("unsupported", 5))
    )


_ApexPsStatusInstalled_Type.__name__ = "Integer32"
_ApexPsStatusInstalled_Object = MibTableColumn
apexPsStatusInstalled = _ApexPsStatusInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 2),
    _ApexPsStatusInstalled_Type()
)
apexPsStatusInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusInstalled.setStatus("current")
_ApexPsStatusOutputVoltage_Type = Integer32
_ApexPsStatusOutputVoltage_Object = MibTableColumn
apexPsStatusOutputVoltage = _ApexPsStatusOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 3),
    _ApexPsStatusOutputVoltage_Type()
)
apexPsStatusOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusOutputVoltage.setStatus("current")
_ApexPsStatusOutputCurrent_Type = Integer32
_ApexPsStatusOutputCurrent_Object = MibTableColumn
apexPsStatusOutputCurrent = _ApexPsStatusOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 4),
    _ApexPsStatusOutputCurrent_Type()
)
apexPsStatusOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusOutputCurrent.setStatus("current")
_ApexPsStatusFanSpeed_Type = Unsigned32
_ApexPsStatusFanSpeed_Object = MibTableColumn
apexPsStatusFanSpeed = _ApexPsStatusFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 5),
    _ApexPsStatusFanSpeed_Type()
)
apexPsStatusFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusFanSpeed.setStatus("current")


class _ApexPsStatusFanStatus_Type(Integer32):
    """Custom type apexPsStatusFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexPsStatusFanStatus_Type.__name__ = "Integer32"
_ApexPsStatusFanStatus_Object = MibTableColumn
apexPsStatusFanStatus = _ApexPsStatusFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 6),
    _ApexPsStatusFanStatus_Type()
)
apexPsStatusFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusFanStatus.setStatus("current")


class _ApexPsStatusTemperatureStatus_Type(Integer32):
    """Custom type apexPsStatusTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexPsStatusTemperatureStatus_Type.__name__ = "Integer32"
_ApexPsStatusTemperatureStatus_Object = MibTableColumn
apexPsStatusTemperatureStatus = _ApexPsStatusTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 7),
    _ApexPsStatusTemperatureStatus_Type()
)
apexPsStatusTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusTemperatureStatus.setStatus("current")


class _ApexPsStatusInputPowerStatus_Type(Integer32):
    """Custom type apexPsStatusInputPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexPsStatusInputPowerStatus_Type.__name__ = "Integer32"
_ApexPsStatusInputPowerStatus_Object = MibTableColumn
apexPsStatusInputPowerStatus = _ApexPsStatusInputPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 8),
    _ApexPsStatusInputPowerStatus_Type()
)
apexPsStatusInputPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusInputPowerStatus.setStatus("current")


class _ApexPsStatusOutputPowerStatus_Type(Integer32):
    """Custom type apexPsStatusOutputPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexPsStatusOutputPowerStatus_Type.__name__ = "Integer32"
_ApexPsStatusOutputPowerStatus_Object = MibTableColumn
apexPsStatusOutputPowerStatus = _ApexPsStatusOutputPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 9),
    _ApexPsStatusOutputPowerStatus_Type()
)
apexPsStatusOutputPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusOutputPowerStatus.setStatus("current")


class _ApexPsStatusErrorStatus_Type(Integer32):
    """Custom type apexPsStatusErrorStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 8),
          ("fanFault", 5),
          ("inputPower", 4),
          ("ok", 1),
          ("outputPower", 7),
          ("overTemp", 6),
          ("psNotInstalled", 2),
          ("psUnsupported", 3))
    )


_ApexPsStatusErrorStatus_Type.__name__ = "Integer32"
_ApexPsStatusErrorStatus_Object = MibTableColumn
apexPsStatusErrorStatus = _ApexPsStatusErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 10),
    _ApexPsStatusErrorStatus_Type()
)
apexPsStatusErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusErrorStatus.setStatus("current")


class _ApexPsStatusFaultCondition_Type(Integer32):
    """Custom type apexPsStatusFaultCondition based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexPsStatusFaultCondition_Type.__name__ = "Integer32"
_ApexPsStatusFaultCondition_Object = MibTableColumn
apexPsStatusFaultCondition = _ApexPsStatusFaultCondition_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 11),
    _ApexPsStatusFaultCondition_Type()
)
apexPsStatusFaultCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusFaultCondition.setStatus("current")
_ApexPsStatusDiagnosticData1_Type = Integer32
_ApexPsStatusDiagnosticData1_Object = MibTableColumn
apexPsStatusDiagnosticData1 = _ApexPsStatusDiagnosticData1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 12),
    _ApexPsStatusDiagnosticData1_Type()
)
apexPsStatusDiagnosticData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusDiagnosticData1.setStatus("current")
_ApexPsStatusDiagnosticData2_Type = Integer32
_ApexPsStatusDiagnosticData2_Object = MibTableColumn
apexPsStatusDiagnosticData2 = _ApexPsStatusDiagnosticData2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 13),
    _ApexPsStatusDiagnosticData2_Type()
)
apexPsStatusDiagnosticData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusDiagnosticData2.setStatus("current")


class _ApexPsStatusCommError_Type(Integer32):
    """Custom type apexPsStatusCommError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexPsStatusCommError_Type.__name__ = "Integer32"
_ApexPsStatusCommError_Object = MibTableColumn
apexPsStatusCommError = _ApexPsStatusCommError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 2, 1, 14),
    _ApexPsStatusCommError_Type()
)
apexPsStatusCommError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusCommError.setStatus("current")
_ApexPsStatusVersionsTable_Object = MibTable
apexPsStatusVersionsTable = _ApexPsStatusVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 3)
)
if mibBuilder.loadTexts:
    apexPsStatusVersionsTable.setStatus("current")
_ApexPsStatusVersionsEntry_Object = MibTableRow
apexPsStatusVersionsEntry = _ApexPsStatusVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 3, 1)
)
apexPsStatusVersionsEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsStatusVersionsPsNum"),
)
if mibBuilder.loadTexts:
    apexPsStatusVersionsEntry.setStatus("current")


class _ApexPsStatusVersionsPsNum_Type(Integer32):
    """Custom type apexPsStatusVersionsPsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexPsStatusVersionsPsNum_Type.__name__ = "Integer32"
_ApexPsStatusVersionsPsNum_Object = MibTableColumn
apexPsStatusVersionsPsNum = _ApexPsStatusVersionsPsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 3, 1, 1),
    _ApexPsStatusVersionsPsNum_Type()
)
apexPsStatusVersionsPsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsStatusVersionsPsNum.setStatus("current")


class _ApexPsStatusVersionsModel_Type(DisplayString):
    """Custom type apexPsStatusVersionsModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ApexPsStatusVersionsModel_Type.__name__ = "DisplayString"
_ApexPsStatusVersionsModel_Object = MibTableColumn
apexPsStatusVersionsModel = _ApexPsStatusVersionsModel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 3, 1, 2),
    _ApexPsStatusVersionsModel_Type()
)
apexPsStatusVersionsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusVersionsModel.setStatus("current")


class _ApexPsStatusVersionsSerialNumber_Type(DisplayString):
    """Custom type apexPsStatusVersionsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexPsStatusVersionsSerialNumber_Type.__name__ = "DisplayString"
_ApexPsStatusVersionsSerialNumber_Object = MibTableColumn
apexPsStatusVersionsSerialNumber = _ApexPsStatusVersionsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 4, 2, 3, 1, 3),
    _ApexPsStatusVersionsSerialNumber_Type()
)
apexPsStatusVersionsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsStatusVersionsSerialNumber.setStatus("current")
_ApexAsi_ObjectIdentity = ObjectIdentity
apexAsi = _ApexAsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5)
)
_ApexAsiConfig_ObjectIdentity = ObjectIdentity
apexAsiConfig = _ApexAsiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5, 1)
)
_ApexAsiMonitorPortConfig_ObjectIdentity = ObjectIdentity
apexAsiMonitorPortConfig = _ApexAsiMonitorPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5, 1, 2)
)


class _ApexAsiMonitorPortOutputTsNum_Type(Integer32):
    """Custom type apexAsiMonitorPortOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexAsiMonitorPortOutputTsNum_Type.__name__ = "Integer32"
_ApexAsiMonitorPortOutputTsNum_Object = MibScalar
apexAsiMonitorPortOutputTsNum = _ApexAsiMonitorPortOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5, 1, 2, 1),
    _ApexAsiMonitorPortOutputTsNum_Type()
)
apexAsiMonitorPortOutputTsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexAsiMonitorPortOutputTsNum.setStatus("current")


class _ApexAsiMonitorPortEncryption_Type(Integer32):
    """Custom type apexAsiMonitorPortEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("postEncryption", 2),
          ("preEncryption", 1))
    )


_ApexAsiMonitorPortEncryption_Type.__name__ = "Integer32"
_ApexAsiMonitorPortEncryption_Object = MibScalar
apexAsiMonitorPortEncryption = _ApexAsiMonitorPortEncryption_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5, 1, 2, 2),
    _ApexAsiMonitorPortEncryption_Type()
)
apexAsiMonitorPortEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexAsiMonitorPortEncryption.setStatus("current")
_ApexFastEnet_ObjectIdentity = ObjectIdentity
apexFastEnet = _ApexFastEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6)
)
_ApexFastEnetConfig_ObjectIdentity = ObjectIdentity
apexFastEnetConfig = _ApexFastEnetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1)
)
_ApexFastEnetConfigGeneral_ObjectIdentity = ObjectIdentity
apexFastEnetConfigGeneral = _ApexFastEnetConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1)
)
_ApexFastEnetDefaultGateway_Type = IpAddress
_ApexFastEnetDefaultGateway_Object = MibScalar
apexFastEnetDefaultGateway = _ApexFastEnetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 1),
    _ApexFastEnetDefaultGateway_Type()
)
apexFastEnetDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetDefaultGateway.setStatus("current")
_ApexFastEnetInsertRateTable_Object = MibTable
apexFastEnetInsertRateTable = _ApexFastEnetInsertRateTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apexFastEnetInsertRateTable.setStatus("current")
_ApexFastEnetInsertRateEntry_Object = MibTableRow
apexFastEnetInsertRateEntry = _ApexFastEnetInsertRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 2, 1)
)
apexFastEnetInsertRateEntry.setIndexNames(
    (0, "APEX-MIB", "apexFastEnetInsertRateOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexFastEnetInsertRateEntry.setStatus("current")


class _ApexFastEnetInsertRateOutputTsNum_Type(Integer32):
    """Custom type apexFastEnetInsertRateOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexFastEnetInsertRateOutputTsNum_Type.__name__ = "Integer32"
_ApexFastEnetInsertRateOutputTsNum_Object = MibTableColumn
apexFastEnetInsertRateOutputTsNum = _ApexFastEnetInsertRateOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 2, 1, 1),
    _ApexFastEnetInsertRateOutputTsNum_Type()
)
apexFastEnetInsertRateOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexFastEnetInsertRateOutputTsNum.setStatus("current")
_ApexFastEnetInsertRate_Type = Integer32
_ApexFastEnetInsertRate_Object = MibTableColumn
apexFastEnetInsertRate = _ApexFastEnetInsertRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 2, 1, 2),
    _ApexFastEnetInsertRate_Type()
)
apexFastEnetInsertRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetInsertRate.setStatus("current")
_ApexFastEnetRoutingApplyChange_Type = ApplyDataToDeviceTYPE
_ApexFastEnetRoutingApplyChange_Object = MibScalar
apexFastEnetRoutingApplyChange = _ApexFastEnetRoutingApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 1, 3),
    _ApexFastEnetRoutingApplyChange_Type()
)
apexFastEnetRoutingApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetRoutingApplyChange.setStatus("current")
_ApexFastEnetRoutingTable_Object = MibTable
apexFastEnetRoutingTable = _ApexFastEnetRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2)
)
if mibBuilder.loadTexts:
    apexFastEnetRoutingTable.setStatus("current")
_ApexFastEnetRoutingEntry_Object = MibTableRow
apexFastEnetRoutingEntry = _ApexFastEnetRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2, 1)
)
apexFastEnetRoutingEntry.setIndexNames(
    (0, "APEX-MIB", "apexFastEnetRoutingIndex"),
)
if mibBuilder.loadTexts:
    apexFastEnetRoutingEntry.setStatus("current")


class _ApexFastEnetRoutingIndex_Type(Integer32):
    """Custom type apexFastEnetRoutingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApexFastEnetRoutingIndex_Type.__name__ = "Integer32"
_ApexFastEnetRoutingIndex_Object = MibTableColumn
apexFastEnetRoutingIndex = _ApexFastEnetRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2, 1, 1),
    _ApexFastEnetRoutingIndex_Type()
)
apexFastEnetRoutingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexFastEnetRoutingIndex.setStatus("current")
_ApexFastEnetRoutingDestinIp_Type = IpAddress
_ApexFastEnetRoutingDestinIp_Object = MibTableColumn
apexFastEnetRoutingDestinIp = _ApexFastEnetRoutingDestinIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2, 1, 2),
    _ApexFastEnetRoutingDestinIp_Type()
)
apexFastEnetRoutingDestinIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetRoutingDestinIp.setStatus("current")
_ApexFastEnetRoutingGatewayIp_Type = IpAddress
_ApexFastEnetRoutingGatewayIp_Object = MibTableColumn
apexFastEnetRoutingGatewayIp = _ApexFastEnetRoutingGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2, 1, 3),
    _ApexFastEnetRoutingGatewayIp_Type()
)
apexFastEnetRoutingGatewayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetRoutingGatewayIp.setStatus("current")
_ApexFastEnetRoutingSubnetMask_Type = IpAddress
_ApexFastEnetRoutingSubnetMask_Object = MibTableColumn
apexFastEnetRoutingSubnetMask = _ApexFastEnetRoutingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 1, 2, 1, 4),
    _ApexFastEnetRoutingSubnetMask_Type()
)
apexFastEnetRoutingSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexFastEnetRoutingSubnetMask.setStatus("current")
_ApexFastEnetStatus_ObjectIdentity = ObjectIdentity
apexFastEnetStatus = _ApexFastEnetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2)
)
_ApexFastEnetStatusGeneral_ObjectIdentity = ObjectIdentity
apexFastEnetStatusGeneral = _ApexFastEnetStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 1)
)
_ApexFastEnetMaxInputUdpPorts_Type = Integer32
_ApexFastEnetMaxInputUdpPorts_Object = MibScalar
apexFastEnetMaxInputUdpPorts = _ApexFastEnetMaxInputUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 1, 1),
    _ApexFastEnetMaxInputUdpPorts_Type()
)
apexFastEnetMaxInputUdpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetMaxInputUdpPorts.setStatus("current")
_ApexFastEnetStatusPacketsTable_Object = MibTable
apexFastEnetStatusPacketsTable = _ApexFastEnetStatusPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2)
)
if mibBuilder.loadTexts:
    apexFastEnetStatusPacketsTable.setStatus("current")
_ApexFastEnetStatusPacketsEntry_Object = MibTableRow
apexFastEnetStatusPacketsEntry = _ApexFastEnetStatusPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1)
)
apexFastEnetStatusPacketsEntry.setIndexNames(
    (0, "APEX-MIB", "apexFastEnetPacketsPortNum"),
)
if mibBuilder.loadTexts:
    apexFastEnetStatusPacketsEntry.setStatus("current")


class _ApexFastEnetPacketsPortNum_Type(Integer32):
    """Custom type apexFastEnetPacketsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexFastEnetPacketsPortNum_Type.__name__ = "Integer32"
_ApexFastEnetPacketsPortNum_Object = MibTableColumn
apexFastEnetPacketsPortNum = _ApexFastEnetPacketsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1, 1),
    _ApexFastEnetPacketsPortNum_Type()
)
apexFastEnetPacketsPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexFastEnetPacketsPortNum.setStatus("current")
_ApexFastEnetPacketsNumPkts_Type = Unsigned32
_ApexFastEnetPacketsNumPkts_Object = MibTableColumn
apexFastEnetPacketsNumPkts = _ApexFastEnetPacketsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1, 2),
    _ApexFastEnetPacketsNumPkts_Type()
)
apexFastEnetPacketsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetPacketsNumPkts.setStatus("current")
_ApexFastEnetPacketsTotPkts_Type = Unsigned32
_ApexFastEnetPacketsTotPkts_Object = MibTableColumn
apexFastEnetPacketsTotPkts = _ApexFastEnetPacketsTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1, 3),
    _ApexFastEnetPacketsTotPkts_Type()
)
apexFastEnetPacketsTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetPacketsTotPkts.setStatus("current")
_ApexFastEnetPacketsNumDiscarded_Type = Unsigned32
_ApexFastEnetPacketsNumDiscarded_Object = MibTableColumn
apexFastEnetPacketsNumDiscarded = _ApexFastEnetPacketsNumDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1, 4),
    _ApexFastEnetPacketsNumDiscarded_Type()
)
apexFastEnetPacketsNumDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetPacketsNumDiscarded.setStatus("current")
_ApexFastEnetPacketsTotDiscarded_Type = Unsigned32
_ApexFastEnetPacketsTotDiscarded_Object = MibTableColumn
apexFastEnetPacketsTotDiscarded = _ApexFastEnetPacketsTotDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 2, 1, 5),
    _ApexFastEnetPacketsTotDiscarded_Type()
)
apexFastEnetPacketsTotDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetPacketsTotDiscarded.setStatus("current")
_ApexFastEnetInsertPacketsTable_Object = MibTable
apexFastEnetInsertPacketsTable = _ApexFastEnetInsertPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3)
)
if mibBuilder.loadTexts:
    apexFastEnetInsertPacketsTable.setStatus("current")
_ApexFastEnetInsertPacketsEntry_Object = MibTableRow
apexFastEnetInsertPacketsEntry = _ApexFastEnetInsertPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1)
)
apexFastEnetInsertPacketsEntry.setIndexNames(
    (0, "APEX-MIB", "apexFastEnetInsPacketsOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexFastEnetInsertPacketsEntry.setStatus("current")


class _ApexFastEnetInsPacketsOutputTsNum_Type(Integer32):
    """Custom type apexFastEnetInsPacketsOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexFastEnetInsPacketsOutputTsNum_Type.__name__ = "Integer32"
_ApexFastEnetInsPacketsOutputTsNum_Object = MibTableColumn
apexFastEnetInsPacketsOutputTsNum = _ApexFastEnetInsPacketsOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1, 1),
    _ApexFastEnetInsPacketsOutputTsNum_Type()
)
apexFastEnetInsPacketsOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexFastEnetInsPacketsOutputTsNum.setStatus("current")
_ApexFastEnetInsPacketsNumPkts_Type = Unsigned32
_ApexFastEnetInsPacketsNumPkts_Object = MibTableColumn
apexFastEnetInsPacketsNumPkts = _ApexFastEnetInsPacketsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1, 2),
    _ApexFastEnetInsPacketsNumPkts_Type()
)
apexFastEnetInsPacketsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetInsPacketsNumPkts.setStatus("current")
_ApexFastEnetInsPacketsTotPkts_Type = Unsigned32
_ApexFastEnetInsPacketsTotPkts_Object = MibTableColumn
apexFastEnetInsPacketsTotPkts = _ApexFastEnetInsPacketsTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1, 3),
    _ApexFastEnetInsPacketsTotPkts_Type()
)
apexFastEnetInsPacketsTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetInsPacketsTotPkts.setStatus("current")
_ApexFastEnetInsPacketsNumDiscarded_Type = Unsigned32
_ApexFastEnetInsPacketsNumDiscarded_Object = MibTableColumn
apexFastEnetInsPacketsNumDiscarded = _ApexFastEnetInsPacketsNumDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1, 4),
    _ApexFastEnetInsPacketsNumDiscarded_Type()
)
apexFastEnetInsPacketsNumDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetInsPacketsNumDiscarded.setStatus("current")
_ApexFastEnetInsPacketsTotDiscarded_Type = Unsigned32
_ApexFastEnetInsPacketsTotDiscarded_Object = MibTableColumn
apexFastEnetInsPacketsTotDiscarded = _ApexFastEnetInsPacketsTotDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 2, 3, 1, 5),
    _ApexFastEnetInsPacketsTotDiscarded_Type()
)
apexFastEnetInsPacketsTotDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFastEnetInsPacketsTotDiscarded.setStatus("current")
_ApexOamp_ObjectIdentity = ObjectIdentity
apexOamp = _ApexOamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3)
)
_ApexOampConfig_ObjectIdentity = ObjectIdentity
apexOampConfig = _ApexOampConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 1)
)
_ApexOampConfigGeneral_ObjectIdentity = ObjectIdentity
apexOampConfigGeneral = _ApexOampConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 1, 1)
)
_ApexOampIpAddr_Type = IpAddress
_ApexOampIpAddr_Object = MibScalar
apexOampIpAddr = _ApexOampIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 1, 1, 1),
    _ApexOampIpAddr_Type()
)
apexOampIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOampIpAddr.setStatus("current")
_ApexOampSubnetMask_Type = IpAddress
_ApexOampSubnetMask_Object = MibScalar
apexOampSubnetMask = _ApexOampSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 1, 1, 2),
    _ApexOampSubnetMask_Type()
)
apexOampSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOampSubnetMask.setStatus("current")
_ApexOampAutoNegotiate_Type = EnableDisableTYPE
_ApexOampAutoNegotiate_Object = MibScalar
apexOampAutoNegotiate = _ApexOampAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 1, 1, 3),
    _ApexOampAutoNegotiate_Type()
)
apexOampAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOampAutoNegotiate.setStatus("current")
_ApexOampStatus_ObjectIdentity = ObjectIdentity
apexOampStatus = _ApexOampStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2)
)
_ApexOampStatusGeneral_ObjectIdentity = ObjectIdentity
apexOampStatusGeneral = _ApexOampStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1)
)


class _ApexOampMacAddr_Type(DisplayString):
    """Custom type apexOampMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ApexOampMacAddr_Type.__name__ = "DisplayString"
_ApexOampMacAddr_Object = MibScalar
apexOampMacAddr = _ApexOampMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1, 1),
    _ApexOampMacAddr_Type()
)
apexOampMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOampMacAddr.setStatus("current")


class _ApexOampSpeed_Type(Integer32):
    """Custom type apexOampSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceSpeed100Mbps", 2),
          ("interfaceSpeed10Mbps", 1),
          ("notApplicable", 0))
    )


_ApexOampSpeed_Type.__name__ = "Integer32"
_ApexOampSpeed_Object = MibScalar
apexOampSpeed = _ApexOampSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1, 2),
    _ApexOampSpeed_Type()
)
apexOampSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOampSpeed.setStatus("current")


class _ApexOampDuplexMode_Type(Integer32):
    """Custom type apexOampDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("notApplicable", 0))
    )


_ApexOampDuplexMode_Type.__name__ = "Integer32"
_ApexOampDuplexMode_Object = MibScalar
apexOampDuplexMode = _ApexOampDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1, 3),
    _ApexOampDuplexMode_Type()
)
apexOampDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOampDuplexMode.setStatus("current")
_ApexOampInputTsAssignedCount_Type = Integer32
_ApexOampInputTsAssignedCount_Object = MibScalar
apexOampInputTsAssignedCount = _ApexOampInputTsAssignedCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1, 4),
    _ApexOampInputTsAssignedCount_Type()
)
apexOampInputTsAssignedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOampInputTsAssignedCount.setStatus("current")
_ApexOampLinkActive_Type = ActiveTYPE
_ApexOampLinkActive_Object = MibScalar
apexOampLinkActive = _ApexOampLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 3, 2, 1, 5),
    _ApexOampLinkActive_Type()
)
apexOampLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOampLinkActive.setStatus("current")
_ApexDataIp_ObjectIdentity = ObjectIdentity
apexDataIp = _ApexDataIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4)
)
_ApexDataIpConfig_ObjectIdentity = ObjectIdentity
apexDataIpConfig = _ApexDataIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 1)
)
_ApexDataIpConfigGeneral_ObjectIdentity = ObjectIdentity
apexDataIpConfigGeneral = _ApexDataIpConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 1, 1)
)
_ApexDataIpAddr_Type = IpAddress
_ApexDataIpAddr_Object = MibScalar
apexDataIpAddr = _ApexDataIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 1, 1, 1),
    _ApexDataIpAddr_Type()
)
apexDataIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDataIpAddr.setStatus("current")
_ApexDataIpSubnetMask_Type = IpAddress
_ApexDataIpSubnetMask_Object = MibScalar
apexDataIpSubnetMask = _ApexDataIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 1, 1, 2),
    _ApexDataIpSubnetMask_Type()
)
apexDataIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDataIpSubnetMask.setStatus("current")
_ApexDataIpAutoNegotiate_Type = EnableDisableTYPE
_ApexDataIpAutoNegotiate_Object = MibScalar
apexDataIpAutoNegotiate = _ApexDataIpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 1, 1, 3),
    _ApexDataIpAutoNegotiate_Type()
)
apexDataIpAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDataIpAutoNegotiate.setStatus("current")
_ApexDataIpStatus_ObjectIdentity = ObjectIdentity
apexDataIpStatus = _ApexDataIpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2)
)
_ApexDataIpStatusGeneral_ObjectIdentity = ObjectIdentity
apexDataIpStatusGeneral = _ApexDataIpStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1)
)


class _ApexDataIpMacAddr_Type(DisplayString):
    """Custom type apexDataIpMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ApexDataIpMacAddr_Type.__name__ = "DisplayString"
_ApexDataIpMacAddr_Object = MibScalar
apexDataIpMacAddr = _ApexDataIpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 1),
    _ApexDataIpMacAddr_Type()
)
apexDataIpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpMacAddr.setStatus("current")


class _ApexDataIpSpeed_Type(Integer32):
    """Custom type apexDataIpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceSpeed100Mbps", 2),
          ("interfaceSpeed10Mbps", 1),
          ("notApplicable", 0))
    )


_ApexDataIpSpeed_Type.__name__ = "Integer32"
_ApexDataIpSpeed_Object = MibScalar
apexDataIpSpeed = _ApexDataIpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 2),
    _ApexDataIpSpeed_Type()
)
apexDataIpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpSpeed.setStatus("current")


class _ApexDataIpDuplexMode_Type(Integer32):
    """Custom type apexDataIpDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("notApplicable", 0))
    )


_ApexDataIpDuplexMode_Type.__name__ = "Integer32"
_ApexDataIpDuplexMode_Object = MibScalar
apexDataIpDuplexMode = _ApexDataIpDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 3),
    _ApexDataIpDuplexMode_Type()
)
apexDataIpDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpDuplexMode.setStatus("current")
_ApexDataIpInputTsAssignedCount_Type = Integer32
_ApexDataIpInputTsAssignedCount_Object = MibScalar
apexDataIpInputTsAssignedCount = _ApexDataIpInputTsAssignedCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 4),
    _ApexDataIpInputTsAssignedCount_Type()
)
apexDataIpInputTsAssignedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpInputTsAssignedCount.setStatus("current")
_ApexDataIpAddrInUse_Type = IpAddress
_ApexDataIpAddrInUse_Object = MibScalar
apexDataIpAddrInUse = _ApexDataIpAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 5),
    _ApexDataIpAddrInUse_Type()
)
apexDataIpAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpAddrInUse.setStatus("current")
_ApexDataIpSubnetMaskInUse_Type = IpAddress
_ApexDataIpSubnetMaskInUse_Object = MibScalar
apexDataIpSubnetMaskInUse = _ApexDataIpSubnetMaskInUse_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 6),
    _ApexDataIpSubnetMaskInUse_Type()
)
apexDataIpSubnetMaskInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpSubnetMaskInUse.setStatus("current")


class _ApexDataIpInUseReason_Type(Integer32):
    """Custom type apexDataIpInUseReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directRemConnection", 2),
          ("notApplicable", 0),
          ("userConfig", 1))
    )


_ApexDataIpInUseReason_Type.__name__ = "Integer32"
_ApexDataIpInUseReason_Object = MibScalar
apexDataIpInUseReason = _ApexDataIpInUseReason_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 7),
    _ApexDataIpInUseReason_Type()
)
apexDataIpInUseReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpInUseReason.setStatus("current")
_ApexDataIpLinkActive_Type = ActiveTYPE
_ApexDataIpLinkActive_Object = MibScalar
apexDataIpLinkActive = _ApexDataIpLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 6, 4, 2, 1, 8),
    _ApexDataIpLinkActive_Type()
)
apexDataIpLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDataIpLinkActive.setStatus("current")
_ApexGbe_ObjectIdentity = ObjectIdentity
apexGbe = _ApexGbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7)
)
_ApexGbeConfig_ObjectIdentity = ObjectIdentity
apexGbeConfig = _ApexGbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1)
)
_ApexGbeConfigGeneral_ObjectIdentity = ObjectIdentity
apexGbeConfigGeneral = _ApexGbeConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1)
)
_ApexGbeDefaultGateway1_Type = IpAddress
_ApexGbeDefaultGateway1_Object = MibScalar
apexGbeDefaultGateway1 = _ApexGbeDefaultGateway1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 1),
    _ApexGbeDefaultGateway1_Type()
)
apexGbeDefaultGateway1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeDefaultGateway1.setStatus("current")
_ApexGbeDefaultGateway2_Type = IpAddress
_ApexGbeDefaultGateway2_Object = MibScalar
apexGbeDefaultGateway2 = _ApexGbeDefaultGateway2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 2),
    _ApexGbeDefaultGateway2_Type()
)
apexGbeDefaultGateway2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeDefaultGateway2.setStatus("current")


class _ApexGbeJitterAbsorption_Type(Integer32):
    """Custom type apexGbeJitterAbsorption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ApexGbeJitterAbsorption_Type.__name__ = "Integer32"
_ApexGbeJitterAbsorption_Object = MibScalar
apexGbeJitterAbsorption = _ApexGbeJitterAbsorption_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 3),
    _ApexGbeJitterAbsorption_Type()
)
apexGbeJitterAbsorption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeJitterAbsorption.setStatus("obsolete")


class _ApexGbeGarpPeriodicity_Type(Integer32):
    """Custom type apexGbeGarpPeriodicity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 300),
    )


_ApexGbeGarpPeriodicity_Type.__name__ = "Integer32"
_ApexGbeGarpPeriodicity_Object = MibScalar
apexGbeGarpPeriodicity = _ApexGbeGarpPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 4),
    _ApexGbeGarpPeriodicity_Type()
)
apexGbeGarpPeriodicity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeGarpPeriodicity.setStatus("current")
_ApexGbeConfigTableApplyChange_Type = ApplyDataToDeviceTYPE
_ApexGbeConfigTableApplyChange_Object = MibScalar
apexGbeConfigTableApplyChange = _ApexGbeConfigTableApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 5),
    _ApexGbeConfigTableApplyChange_Type()
)
apexGbeConfigTableApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigTableApplyChange.setStatus("current")


class _ApexGbeNominalBufferLevel_Type(Integer32):
    """Custom type apexGbeNominalBufferLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 475),
    )


_ApexGbeNominalBufferLevel_Type.__name__ = "Integer32"
_ApexGbeNominalBufferLevel_Object = MibScalar
apexGbeNominalBufferLevel = _ApexGbeNominalBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 6),
    _ApexGbeNominalBufferLevel_Type()
)
apexGbeNominalBufferLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeNominalBufferLevel.setStatus("current")


class _ApexGbeInputDataTsSmoothingPeriod_Type(Integer32):
    """Custom type apexGbeInputDataTsSmoothingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 650),
    )


_ApexGbeInputDataTsSmoothingPeriod_Type.__name__ = "Integer32"
_ApexGbeInputDataTsSmoothingPeriod_Object = MibScalar
apexGbeInputDataTsSmoothingPeriod = _ApexGbeInputDataTsSmoothingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 7),
    _ApexGbeInputDataTsSmoothingPeriod_Type()
)
apexGbeInputDataTsSmoothingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeInputDataTsSmoothingPeriod.setStatus("current")


class _ApexGbeInputDataTsBufferDepth_Type(Integer32):
    """Custom type apexGbeInputDataTsBufferDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 650),
    )


_ApexGbeInputDataTsBufferDepth_Type.__name__ = "Integer32"
_ApexGbeInputDataTsBufferDepth_Object = MibScalar
apexGbeInputDataTsBufferDepth = _ApexGbeInputDataTsBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 8),
    _ApexGbeInputDataTsBufferDepth_Type()
)
apexGbeInputDataTsBufferDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeInputDataTsBufferDepth.setStatus("current")


class _ApexGbeConfigInputDataTsApplyText_Type(DisplayString):
    """Custom type apexGbeConfigInputDataTsApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexGbeConfigInputDataTsApplyText_Type.__name__ = "DisplayString"
_ApexGbeConfigInputDataTsApplyText_Object = MibScalar
apexGbeConfigInputDataTsApplyText = _ApexGbeConfigInputDataTsApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 9),
    _ApexGbeConfigInputDataTsApplyText_Type()
)
apexGbeConfigInputDataTsApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsApplyText.setStatus("current")


class _ApexGbeConfInputUnicastTimeout_Type(Integer32):
    """Custom type apexGbeConfInputUnicastTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 6000),
    )


_ApexGbeConfInputUnicastTimeout_Type.__name__ = "Integer32"
_ApexGbeConfInputUnicastTimeout_Object = MibScalar
apexGbeConfInputUnicastTimeout = _ApexGbeConfInputUnicastTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 10),
    _ApexGbeConfInputUnicastTimeout_Type()
)
apexGbeConfInputUnicastTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInputUnicastTimeout.setStatus("current")


class _ApexGbeConfInputMulticastTimeout_Type(Integer32):
    """Custom type apexGbeConfInputMulticastTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 6000),
    )


_ApexGbeConfInputMulticastTimeout_Type.__name__ = "Integer32"
_ApexGbeConfInputMulticastTimeout_Object = MibScalar
apexGbeConfInputMulticastTimeout = _ApexGbeConfInputMulticastTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 11),
    _ApexGbeConfInputMulticastTimeout_Type()
)
apexGbeConfInputMulticastTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInputMulticastTimeout.setStatus("current")
_ApexGbeConfLossOfInputTsType_Type = RateComparisonTYPE
_ApexGbeConfLossOfInputTsType_Object = MibScalar
apexGbeConfLossOfInputTsType = _ApexGbeConfLossOfInputTsType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 1, 12),
    _ApexGbeConfLossOfInputTsType_Type()
)
apexGbeConfLossOfInputTsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfLossOfInputTsType.setStatus("current")
_ApexGbeConfigTable_Object = MibTable
apexGbeConfigTable = _ApexGbeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2)
)
if mibBuilder.loadTexts:
    apexGbeConfigTable.setStatus("current")
_ApexGbeConfigEntry_Object = MibTableRow
apexGbeConfigEntry = _ApexGbeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1)
)
apexGbeConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfigInterfaceNum"),
)
if mibBuilder.loadTexts:
    apexGbeConfigEntry.setStatus("current")


class _ApexGbeConfigInterfaceNum_Type(Integer32):
    """Custom type apexGbeConfigInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeConfigInterfaceNum_Type.__name__ = "Integer32"
_ApexGbeConfigInterfaceNum_Object = MibTableColumn
apexGbeConfigInterfaceNum = _ApexGbeConfigInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1, 1),
    _ApexGbeConfigInterfaceNum_Type()
)
apexGbeConfigInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfigInterfaceNum.setStatus("current")
_ApexGbeConfigEnable_Type = EnableDisableTYPE
_ApexGbeConfigEnable_Object = MibTableColumn
apexGbeConfigEnable = _ApexGbeConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1, 2),
    _ApexGbeConfigEnable_Type()
)
apexGbeConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigEnable.setStatus("current")
_ApexGbeConfigIpAddr_Type = IpAddress
_ApexGbeConfigIpAddr_Object = MibTableColumn
apexGbeConfigIpAddr = _ApexGbeConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1, 3),
    _ApexGbeConfigIpAddr_Type()
)
apexGbeConfigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigIpAddr.setStatus("current")
_ApexGbeConfigIpSubnetMask_Type = IpAddress
_ApexGbeConfigIpSubnetMask_Object = MibTableColumn
apexGbeConfigIpSubnetMask = _ApexGbeConfigIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1, 4),
    _ApexGbeConfigIpSubnetMask_Type()
)
apexGbeConfigIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigIpSubnetMask.setStatus("current")
_ApexGbeConfigAutoNegotiate_Type = EnableDisableTYPE
_ApexGbeConfigAutoNegotiate_Object = MibTableColumn
apexGbeConfigAutoNegotiate = _ApexGbeConfigAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 2, 1, 5),
    _ApexGbeConfigAutoNegotiate_Type()
)
apexGbeConfigAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigAutoNegotiate.setStatus("current")
_ApexGbeConfigFrameBufferTable_Object = MibTable
apexGbeConfigFrameBufferTable = _ApexGbeConfigFrameBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 3)
)
if mibBuilder.loadTexts:
    apexGbeConfigFrameBufferTable.setStatus("current")
_ApexGbeConfigFrameBufferEntry_Object = MibTableRow
apexGbeConfigFrameBufferEntry = _ApexGbeConfigFrameBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 3, 1)
)
apexGbeConfigFrameBufferEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfigFrameBufferProcessorNum"),
)
if mibBuilder.loadTexts:
    apexGbeConfigFrameBufferEntry.setStatus("current")


class _ApexGbeConfigFrameBufferProcessorNum_Type(Integer32):
    """Custom type apexGbeConfigFrameBufferProcessorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeConfigFrameBufferProcessorNum_Type.__name__ = "Integer32"
_ApexGbeConfigFrameBufferProcessorNum_Object = MibTableColumn
apexGbeConfigFrameBufferProcessorNum = _ApexGbeConfigFrameBufferProcessorNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 3, 1, 1),
    _ApexGbeConfigFrameBufferProcessorNum_Type()
)
apexGbeConfigFrameBufferProcessorNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfigFrameBufferProcessorNum.setStatus("current")


class _ApexGbeConfigFrameBufferMaxInDataRate_Type(Unsigned32):
    """Custom type apexGbeConfigFrameBufferMaxInDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 2000000000),
    )


_ApexGbeConfigFrameBufferMaxInDataRate_Type.__name__ = "Unsigned32"
_ApexGbeConfigFrameBufferMaxInDataRate_Object = MibTableColumn
apexGbeConfigFrameBufferMaxInDataRate = _ApexGbeConfigFrameBufferMaxInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 3, 1, 2),
    _ApexGbeConfigFrameBufferMaxInDataRate_Type()
)
apexGbeConfigFrameBufferMaxInDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigFrameBufferMaxInDataRate.setStatus("current")


class _ApexGbeConfigFrameBufferAlarmThreshold_Type(Integer32):
    """Custom type apexGbeConfigFrameBufferAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApexGbeConfigFrameBufferAlarmThreshold_Type.__name__ = "Integer32"
_ApexGbeConfigFrameBufferAlarmThreshold_Object = MibTableColumn
apexGbeConfigFrameBufferAlarmThreshold = _ApexGbeConfigFrameBufferAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 3, 1, 3),
    _ApexGbeConfigFrameBufferAlarmThreshold_Type()
)
apexGbeConfigFrameBufferAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigFrameBufferAlarmThreshold.setStatus("current")
_ApexGbeConfigInputRedundancy_ObjectIdentity = ObjectIdentity
apexGbeConfigInputRedundancy = _ApexGbeConfigInputRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4)
)
_ApexGbeConfigInputRedundancyGeneral_ObjectIdentity = ObjectIdentity
apexGbeConfigInputRedundancyGeneral = _ApexGbeConfigInputRedundancyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1)
)


class _ApexGbeConfInRedundMonitorPeriod_Type(Integer32):
    """Custom type apexGbeConfInRedundMonitorPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ApexGbeConfInRedundMonitorPeriod_Type.__name__ = "Integer32"
_ApexGbeConfInRedundMonitorPeriod_Object = MibScalar
apexGbeConfInRedundMonitorPeriod = _ApexGbeConfInRedundMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 1),
    _ApexGbeConfInRedundMonitorPeriod_Type()
)
apexGbeConfInRedundMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundMonitorPeriod.setStatus("current")


class _ApexGbeConfInRedundSwitchTime_Type(Integer32):
    """Custom type apexGbeConfInRedundSwitchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApexGbeConfInRedundSwitchTime_Type.__name__ = "Integer32"
_ApexGbeConfInRedundSwitchTime_Object = MibScalar
apexGbeConfInRedundSwitchTime = _ApexGbeConfInRedundSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 2),
    _ApexGbeConfInRedundSwitchTime_Type()
)
apexGbeConfInRedundSwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundSwitchTime.setStatus("current")
_ApexGbeConfInRedundAutoSwitchBack_Type = EnableDisableTYPE
_ApexGbeConfInRedundAutoSwitchBack_Object = MibScalar
apexGbeConfInRedundAutoSwitchBack = _ApexGbeConfInRedundAutoSwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 3),
    _ApexGbeConfInRedundAutoSwitchBack_Type()
)
apexGbeConfInRedundAutoSwitchBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundAutoSwitchBack.setStatus("current")


class _ApexGbeConfInRedundForceToSecondary_Type(Integer32):
    """Custom type apexGbeConfInRedundForceToSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceSwitch", 2),
          ("switchNotInProgress", 1))
    )


_ApexGbeConfInRedundForceToSecondary_Type.__name__ = "Integer32"
_ApexGbeConfInRedundForceToSecondary_Object = MibScalar
apexGbeConfInRedundForceToSecondary = _ApexGbeConfInRedundForceToSecondary_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 4),
    _ApexGbeConfInRedundForceToSecondary_Type()
)
apexGbeConfInRedundForceToSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundForceToSecondary.setStatus("current")


class _ApexGbeConfInRedundForceToPrimary_Type(Integer32):
    """Custom type apexGbeConfInRedundForceToPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceSwitch", 2),
          ("switchNotInProgress", 1))
    )


_ApexGbeConfInRedundForceToPrimary_Type.__name__ = "Integer32"
_ApexGbeConfInRedundForceToPrimary_Object = MibScalar
apexGbeConfInRedundForceToPrimary = _ApexGbeConfInRedundForceToPrimary_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 5),
    _ApexGbeConfInRedundForceToPrimary_Type()
)
apexGbeConfInRedundForceToPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundForceToPrimary.setStatus("current")


class _ApexGbeConfInRedundManualRouteRedundType_Type(Integer32):
    """Custom type apexGbeConfInRedundManualRouteRedundType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hotHot", 2),
          ("hotWarm", 1))
    )


_ApexGbeConfInRedundManualRouteRedundType_Type.__name__ = "Integer32"
_ApexGbeConfInRedundManualRouteRedundType_Object = MibScalar
apexGbeConfInRedundManualRouteRedundType = _ApexGbeConfInRedundManualRouteRedundType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 4, 1, 6),
    _ApexGbeConfInRedundManualRouteRedundType_Type()
)
apexGbeConfInRedundManualRouteRedundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfInRedundManualRouteRedundType.setStatus("current")
_ApexGbeConfigInputDataTsTable_Object = MibTable
apexGbeConfigInputDataTsTable = _ApexGbeConfigInputDataTsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5)
)
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsTable.setStatus("current")
_ApexGbeConfigInputDataTsEntry_Object = MibTableRow
apexGbeConfigInputDataTsEntry = _ApexGbeConfigInputDataTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1)
)
apexGbeConfigInputDataTsEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfigInputDataTsIndex"),
)
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsEntry.setStatus("current")


class _ApexGbeConfigInputDataTsIndex_Type(Integer32):
    """Custom type apexGbeConfigInputDataTsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexGbeConfigInputDataTsIndex_Type.__name__ = "Integer32"
_ApexGbeConfigInputDataTsIndex_Object = MibTableColumn
apexGbeConfigInputDataTsIndex = _ApexGbeConfigInputDataTsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 1),
    _ApexGbeConfigInputDataTsIndex_Type()
)
apexGbeConfigInputDataTsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsIndex.setStatus("current")
_ApexGbeConfigInputDataTsEnable_Type = EnableDisableTYPE
_ApexGbeConfigInputDataTsEnable_Object = MibTableColumn
apexGbeConfigInputDataTsEnable = _ApexGbeConfigInputDataTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 2),
    _ApexGbeConfigInputDataTsEnable_Type()
)
apexGbeConfigInputDataTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsEnable.setStatus("current")


class _ApexGbeConfigInputDataTsInterface_Type(Integer32):
    """Custom type apexGbeConfigInputDataTsInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexGbeConfigInputDataTsInterface_Type.__name__ = "Integer32"
_ApexGbeConfigInputDataTsInterface_Object = MibTableColumn
apexGbeConfigInputDataTsInterface = _ApexGbeConfigInputDataTsInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 3),
    _ApexGbeConfigInputDataTsInterface_Type()
)
apexGbeConfigInputDataTsInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsInterface.setStatus("current")


class _ApexGbeConfigInputDataTsUdp_Type(Integer32):
    """Custom type apexGbeConfigInputDataTsUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexGbeConfigInputDataTsUdp_Type.__name__ = "Integer32"
_ApexGbeConfigInputDataTsUdp_Object = MibTableColumn
apexGbeConfigInputDataTsUdp = _ApexGbeConfigInputDataTsUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 4),
    _ApexGbeConfigInputDataTsUdp_Type()
)
apexGbeConfigInputDataTsUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsUdp.setStatus("current")
_ApexGbeConfigInputDataTsMulticastIp_Type = IpAddress
_ApexGbeConfigInputDataTsMulticastIp_Object = MibTableColumn
apexGbeConfigInputDataTsMulticastIp = _ApexGbeConfigInputDataTsMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 5),
    _ApexGbeConfigInputDataTsMulticastIp_Type()
)
apexGbeConfigInputDataTsMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsMulticastIp.setStatus("current")
_ApexGbeConfigInputDataTsSourceIp_Type = IpAddress
_ApexGbeConfigInputDataTsSourceIp_Object = MibTableColumn
apexGbeConfigInputDataTsSourceIp = _ApexGbeConfigInputDataTsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 5, 1, 6),
    _ApexGbeConfigInputDataTsSourceIp_Type()
)
apexGbeConfigInputDataTsSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsSourceIp.setStatus("current")
_ApexGbeConfigInputDataTsApplyTable_Object = MibTable
apexGbeConfigInputDataTsApplyTable = _ApexGbeConfigInputDataTsApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 6)
)
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsApplyTable.setStatus("current")
_ApexGbeConfigInputDataTsApplyEntry_Object = MibTableRow
apexGbeConfigInputDataTsApplyEntry = _ApexGbeConfigInputDataTsApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 6, 1)
)
apexGbeConfigInputDataTsApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfigInputDataTsApplyIndex"),
)
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsApplyEntry.setStatus("current")


class _ApexGbeConfigInputDataTsApplyIndex_Type(Integer32):
    """Custom type apexGbeConfigInputDataTsApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexGbeConfigInputDataTsApplyIndex_Type.__name__ = "Integer32"
_ApexGbeConfigInputDataTsApplyIndex_Object = MibTableColumn
apexGbeConfigInputDataTsApplyIndex = _ApexGbeConfigInputDataTsApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 6, 1, 1),
    _ApexGbeConfigInputDataTsApplyIndex_Type()
)
apexGbeConfigInputDataTsApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsApplyIndex.setStatus("current")
_ApexGbeConfigInputDataTsApplyChange_Type = ApplyDataToDeviceTYPE
_ApexGbeConfigInputDataTsApplyChange_Object = MibTableColumn
apexGbeConfigInputDataTsApplyChange = _ApexGbeConfigInputDataTsApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 6, 1, 2),
    _ApexGbeConfigInputDataTsApplyChange_Type()
)
apexGbeConfigInputDataTsApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfigInputDataTsApplyChange.setStatus("current")
_ApexGbeConfigInterfaceRedundancy_ObjectIdentity = ObjectIdentity
apexGbeConfigInterfaceRedundancy = _ApexGbeConfigInterfaceRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7)
)
_ApexGbeConfigInterfaceRedundancyGeneral_ObjectIdentity = ObjectIdentity
apexGbeConfigInterfaceRedundancyGeneral = _ApexGbeConfigInterfaceRedundancyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 1)
)
_ApexGbeConfIfRedundAutoSwitchBackEnable_Type = EnableDisableTYPE
_ApexGbeConfIfRedundAutoSwitchBackEnable_Object = MibScalar
apexGbeConfIfRedundAutoSwitchBackEnable = _ApexGbeConfIfRedundAutoSwitchBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 1, 1),
    _ApexGbeConfIfRedundAutoSwitchBackEnable_Type()
)
apexGbeConfIfRedundAutoSwitchBackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundAutoSwitchBackEnable.setStatus("current")


class _ApexGbeConfIfRedundAutoSwitchBackPeriod_Type(Integer32):
    """Custom type apexGbeConfIfRedundAutoSwitchBackPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ApexGbeConfIfRedundAutoSwitchBackPeriod_Type.__name__ = "Integer32"
_ApexGbeConfIfRedundAutoSwitchBackPeriod_Object = MibScalar
apexGbeConfIfRedundAutoSwitchBackPeriod = _ApexGbeConfIfRedundAutoSwitchBackPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 1, 2),
    _ApexGbeConfIfRedundAutoSwitchBackPeriod_Type()
)
apexGbeConfIfRedundAutoSwitchBackPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundAutoSwitchBackPeriod.setStatus("current")
_ApexGbeConfigInterfaceRedundancyTable_Object = MibTable
apexGbeConfigInterfaceRedundancyTable = _ApexGbeConfigInterfaceRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    apexGbeConfigInterfaceRedundancyTable.setStatus("current")
_ApexGbeConfigInterfaceRedundancyEntry_Object = MibTableRow
apexGbeConfigInterfaceRedundancyEntry = _ApexGbeConfigInterfaceRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2, 1)
)
apexGbeConfigInterfaceRedundancyEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfIfRedundIndex"),
)
if mibBuilder.loadTexts:
    apexGbeConfigInterfaceRedundancyEntry.setStatus("current")


class _ApexGbeConfIfRedundIndex_Type(Integer32):
    """Custom type apexGbeConfIfRedundIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeConfIfRedundIndex_Type.__name__ = "Integer32"
_ApexGbeConfIfRedundIndex_Object = MibTableColumn
apexGbeConfIfRedundIndex = _ApexGbeConfIfRedundIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2, 1, 1),
    _ApexGbeConfIfRedundIndex_Type()
)
apexGbeConfIfRedundIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundIndex.setStatus("current")
_ApexGbeConfIfRedundEnable_Type = EnableDisableTYPE
_ApexGbeConfIfRedundEnable_Object = MibTableColumn
apexGbeConfIfRedundEnable = _ApexGbeConfIfRedundEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2, 1, 2),
    _ApexGbeConfIfRedundEnable_Type()
)
apexGbeConfIfRedundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundEnable.setStatus("current")


class _ApexGbeConfIfRedundForceFailover_Type(Integer32):
    """Custom type apexGbeConfIfRedundForceFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 2),
          ("failoverNotInProgress", 1))
    )


_ApexGbeConfIfRedundForceFailover_Type.__name__ = "Integer32"
_ApexGbeConfIfRedundForceFailover_Object = MibTableColumn
apexGbeConfIfRedundForceFailover = _ApexGbeConfIfRedundForceFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2, 1, 3),
    _ApexGbeConfIfRedundForceFailover_Type()
)
apexGbeConfIfRedundForceFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundForceFailover.setStatus("current")
_ApexGbeConfIfRedundSuspendFailover_Type = EnableDisableTYPE
_ApexGbeConfIfRedundSuspendFailover_Object = MibTableColumn
apexGbeConfIfRedundSuspendFailover = _ApexGbeConfIfRedundSuspendFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 2, 1, 4),
    _ApexGbeConfIfRedundSuspendFailover_Type()
)
apexGbeConfIfRedundSuspendFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundSuspendFailover.setStatus("current")
_ApexGbeConfigInterfaceRedundancyApplyTable_Object = MibTable
apexGbeConfigInterfaceRedundancyApplyTable = _ApexGbeConfigInterfaceRedundancyApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 3)
)
if mibBuilder.loadTexts:
    apexGbeConfigInterfaceRedundancyApplyTable.setStatus("current")
_ApexGbeConfigInterfaceRedundancyApplyEntry_Object = MibTableRow
apexGbeConfigInterfaceRedundancyApplyEntry = _ApexGbeConfigInterfaceRedundancyApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 3, 1)
)
apexGbeConfigInterfaceRedundancyApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeConfIfRedundApplyIndex"),
)
if mibBuilder.loadTexts:
    apexGbeConfigInterfaceRedundancyApplyEntry.setStatus("current")


class _ApexGbeConfIfRedundApplyIndex_Type(Integer32):
    """Custom type apexGbeConfIfRedundApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeConfIfRedundApplyIndex_Type.__name__ = "Integer32"
_ApexGbeConfIfRedundApplyIndex_Object = MibTableColumn
apexGbeConfIfRedundApplyIndex = _ApexGbeConfIfRedundApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 3, 1, 1),
    _ApexGbeConfIfRedundApplyIndex_Type()
)
apexGbeConfIfRedundApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundApplyIndex.setStatus("current")
_ApexGbeConfIfRedundApplyChange_Type = ApplyDataToDeviceTYPE
_ApexGbeConfIfRedundApplyChange_Object = MibTableColumn
apexGbeConfIfRedundApplyChange = _ApexGbeConfIfRedundApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 1, 7, 3, 1, 2),
    _ApexGbeConfIfRedundApplyChange_Type()
)
apexGbeConfIfRedundApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeConfIfRedundApplyChange.setStatus("current")
_ApexGbeStatus_ObjectIdentity = ObjectIdentity
apexGbeStatus = _ApexGbeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2)
)
_ApexGbeStatusGeneral_ObjectIdentity = ObjectIdentity
apexGbeStatusGeneral = _ApexGbeStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 1)
)


class _ApexGbeBootCodeVersion_Type(DisplayString):
    """Custom type apexGbeBootCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexGbeBootCodeVersion_Type.__name__ = "DisplayString"
_ApexGbeBootCodeVersion_Object = MibScalar
apexGbeBootCodeVersion = _ApexGbeBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 1, 1),
    _ApexGbeBootCodeVersion_Type()
)
apexGbeBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeBootCodeVersion.setStatus("current")


class _ApexGbeApplicationCodeVersion_Type(DisplayString):
    """Custom type apexGbeApplicationCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexGbeApplicationCodeVersion_Type.__name__ = "DisplayString"
_ApexGbeApplicationCodeVersion_Object = MibScalar
apexGbeApplicationCodeVersion = _ApexGbeApplicationCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 1, 2),
    _ApexGbeApplicationCodeVersion_Type()
)
apexGbeApplicationCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeApplicationCodeVersion.setStatus("current")
_ApexGbeMaxInputTs_Type = Integer32
_ApexGbeMaxInputTs_Object = MibScalar
apexGbeMaxInputTs = _ApexGbeMaxInputTs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 1, 3),
    _ApexGbeMaxInputTs_Type()
)
apexGbeMaxInputTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeMaxInputTs.setStatus("current")
_ApexGbeRoutedPacketUpdateInterval_Type = Integer32
_ApexGbeRoutedPacketUpdateInterval_Object = MibScalar
apexGbeRoutedPacketUpdateInterval = _ApexGbeRoutedPacketUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 1, 4),
    _ApexGbeRoutedPacketUpdateInterval_Type()
)
apexGbeRoutedPacketUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRoutedPacketUpdateInterval.setStatus("current")
_ApexGbeStatusTable_Object = MibTable
apexGbeStatusTable = _ApexGbeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2)
)
if mibBuilder.loadTexts:
    apexGbeStatusTable.setStatus("current")
_ApexGbeStatusEntry_Object = MibTableRow
apexGbeStatusEntry = _ApexGbeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1)
)
apexGbeStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeStatusGbeInterfaceNum"),
)
if mibBuilder.loadTexts:
    apexGbeStatusEntry.setStatus("current")


class _ApexGbeStatusGbeInterfaceNum_Type(Integer32):
    """Custom type apexGbeStatusGbeInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeStatusGbeInterfaceNum_Type.__name__ = "Integer32"
_ApexGbeStatusGbeInterfaceNum_Object = MibTableColumn
apexGbeStatusGbeInterfaceNum = _ApexGbeStatusGbeInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1, 1),
    _ApexGbeStatusGbeInterfaceNum_Type()
)
apexGbeStatusGbeInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeStatusGbeInterfaceNum.setStatus("current")


class _ApexGbeStatusMacAddr_Type(DisplayString):
    """Custom type apexGbeStatusMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ApexGbeStatusMacAddr_Type.__name__ = "DisplayString"
_ApexGbeStatusMacAddr_Object = MibTableColumn
apexGbeStatusMacAddr = _ApexGbeStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1, 2),
    _ApexGbeStatusMacAddr_Type()
)
apexGbeStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusMacAddr.setStatus("current")
_ApexGbeStatusLinkActive_Type = ActiveTYPE
_ApexGbeStatusLinkActive_Object = MibTableColumn
apexGbeStatusLinkActive = _ApexGbeStatusLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1, 3),
    _ApexGbeStatusLinkActive_Type()
)
apexGbeStatusLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusLinkActive.setStatus("current")


class _ApexGbeStatusIgmpVersion_Type(Integer32):
    """Custom type apexGbeStatusIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpV1", 1),
          ("igmpV2", 2),
          ("igmpV3", 3),
          ("notApplicable", 0))
    )


_ApexGbeStatusIgmpVersion_Type.__name__ = "Integer32"
_ApexGbeStatusIgmpVersion_Object = MibTableColumn
apexGbeStatusIgmpVersion = _ApexGbeStatusIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1, 4),
    _ApexGbeStatusIgmpVersion_Type()
)
apexGbeStatusIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusIgmpVersion.setStatus("current")


class _ApexGbeStatusLossOfPhysicalInput_Type(Integer32):
    """Custom type apexGbeStatusLossOfPhysicalInput based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexGbeStatusLossOfPhysicalInput_Type.__name__ = "Integer32"
_ApexGbeStatusLossOfPhysicalInput_Object = MibTableColumn
apexGbeStatusLossOfPhysicalInput = _ApexGbeStatusLossOfPhysicalInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 2, 1, 5),
    _ApexGbeStatusLossOfPhysicalInput_Type()
)
apexGbeStatusLossOfPhysicalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusLossOfPhysicalInput.setStatus("current")
_ApexGbeInputTsAssignedTable_Object = MibTable
apexGbeInputTsAssignedTable = _ApexGbeInputTsAssignedTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 3)
)
if mibBuilder.loadTexts:
    apexGbeInputTsAssignedTable.setStatus("current")
_ApexGbeInputTsAssignedEntry_Object = MibTableRow
apexGbeInputTsAssignedEntry = _ApexGbeInputTsAssignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 3, 1)
)
apexGbeInputTsAssignedEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeInputTsAssignedGbeInterfaceNum"),
)
if mibBuilder.loadTexts:
    apexGbeInputTsAssignedEntry.setStatus("current")


class _ApexGbeInputTsAssignedGbeInterfaceNum_Type(Integer32):
    """Custom type apexGbeInputTsAssignedGbeInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeInputTsAssignedGbeInterfaceNum_Type.__name__ = "Integer32"
_ApexGbeInputTsAssignedGbeInterfaceNum_Object = MibTableColumn
apexGbeInputTsAssignedGbeInterfaceNum = _ApexGbeInputTsAssignedGbeInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 3, 1, 1),
    _ApexGbeInputTsAssignedGbeInterfaceNum_Type()
)
apexGbeInputTsAssignedGbeInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeInputTsAssignedGbeInterfaceNum.setStatus("current")
_ApexGbeInputTsAssignedCount_Type = Counter32
_ApexGbeInputTsAssignedCount_Object = MibTableColumn
apexGbeInputTsAssignedCount = _ApexGbeInputTsAssignedCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 3, 1, 2),
    _ApexGbeInputTsAssignedCount_Type()
)
apexGbeInputTsAssignedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsAssignedCount.setStatus("current")
_ApexGbeOpenInputUdpPortTable_Object = MibTable
apexGbeOpenInputUdpPortTable = _ApexGbeOpenInputUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 4)
)
if mibBuilder.loadTexts:
    apexGbeOpenInputUdpPortTable.setStatus("current")
_ApexGbeOpenInputUdpPortEntry_Object = MibTableRow
apexGbeOpenInputUdpPortEntry = _ApexGbeOpenInputUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 4, 1)
)
apexGbeOpenInputUdpPortEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeOpenInputUdpPortGbeInterfaceNum"),
)
if mibBuilder.loadTexts:
    apexGbeOpenInputUdpPortEntry.setStatus("current")


class _ApexGbeOpenInputUdpPortGbeInterfaceNum_Type(Integer32):
    """Custom type apexGbeOpenInputUdpPortGbeInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeOpenInputUdpPortGbeInterfaceNum_Type.__name__ = "Integer32"
_ApexGbeOpenInputUdpPortGbeInterfaceNum_Object = MibTableColumn
apexGbeOpenInputUdpPortGbeInterfaceNum = _ApexGbeOpenInputUdpPortGbeInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 4, 1, 1),
    _ApexGbeOpenInputUdpPortGbeInterfaceNum_Type()
)
apexGbeOpenInputUdpPortGbeInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeOpenInputUdpPortGbeInterfaceNum.setStatus("current")
_ApexGbeOpenInputUdpPortCount_Type = Counter32
_ApexGbeOpenInputUdpPortCount_Object = MibTableColumn
apexGbeOpenInputUdpPortCount = _ApexGbeOpenInputUdpPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 4, 1, 2),
    _ApexGbeOpenInputUdpPortCount_Type()
)
apexGbeOpenInputUdpPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeOpenInputUdpPortCount.setStatus("current")
_ApexGbeStatusRoutedPacketTable_Object = MibTable
apexGbeStatusRoutedPacketTable = _ApexGbeStatusRoutedPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 5)
)
if mibBuilder.loadTexts:
    apexGbeStatusRoutedPacketTable.setStatus("current")
_ApexGbeStatusRoutedPacketEntry_Object = MibTableRow
apexGbeStatusRoutedPacketEntry = _ApexGbeStatusRoutedPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 5, 1)
)
apexGbeStatusRoutedPacketEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeStatusRoutedPacketOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexGbeStatusRoutedPacketEntry.setStatus("current")


class _ApexGbeStatusRoutedPacketOutputTsNum_Type(Integer32):
    """Custom type apexGbeStatusRoutedPacketOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexGbeStatusRoutedPacketOutputTsNum_Type.__name__ = "Integer32"
_ApexGbeStatusRoutedPacketOutputTsNum_Object = MibTableColumn
apexGbeStatusRoutedPacketOutputTsNum = _ApexGbeStatusRoutedPacketOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 5, 1, 1),
    _ApexGbeStatusRoutedPacketOutputTsNum_Type()
)
apexGbeStatusRoutedPacketOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeStatusRoutedPacketOutputTsNum.setStatus("current")
_ApexGbeStatusTotRoutedPackets_Type = Counter32
_ApexGbeStatusTotRoutedPackets_Object = MibTableColumn
apexGbeStatusTotRoutedPackets = _ApexGbeStatusTotRoutedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 5, 1, 2),
    _ApexGbeStatusTotRoutedPackets_Type()
)
apexGbeStatusTotRoutedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusTotRoutedPackets.setStatus("current")
_ApexGbeStatusNumRoutedPackets_Type = Counter32
_ApexGbeStatusNumRoutedPackets_Object = MibTableColumn
apexGbeStatusNumRoutedPackets = _ApexGbeStatusNumRoutedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 5, 1, 3),
    _ApexGbeStatusNumRoutedPackets_Type()
)
apexGbeStatusNumRoutedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusNumRoutedPackets.setStatus("current")
_ApexGbeStatusFrameCounter_ObjectIdentity = ObjectIdentity
apexGbeStatusFrameCounter = _ApexGbeStatusFrameCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6)
)
_ApexGbeStatusFrameCounterGeneral_ObjectIdentity = ObjectIdentity
apexGbeStatusFrameCounterGeneral = _ApexGbeStatusFrameCounterGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 1)
)
_ApexGbeStatusFrameCounterTableResetAll_Type = ResetStatisticsTYPE
_ApexGbeStatusFrameCounterTableResetAll_Object = MibScalar
apexGbeStatusFrameCounterTableResetAll = _ApexGbeStatusFrameCounterTableResetAll_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 1, 1),
    _ApexGbeStatusFrameCounterTableResetAll_Type()
)
apexGbeStatusFrameCounterTableResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeStatusFrameCounterTableResetAll.setStatus("current")
_ApexGbeFrameCounterUpdateInterval_Type = Integer32
_ApexGbeFrameCounterUpdateInterval_Object = MibScalar
apexGbeFrameCounterUpdateInterval = _ApexGbeFrameCounterUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 1, 2),
    _ApexGbeFrameCounterUpdateInterval_Type()
)
apexGbeFrameCounterUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameCounterUpdateInterval.setStatus("current")
_ApexGbeStatusFrameCounterTable_Object = MibTable
apexGbeStatusFrameCounterTable = _ApexGbeStatusFrameCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2)
)
if mibBuilder.loadTexts:
    apexGbeStatusFrameCounterTable.setStatus("current")
_ApexGbeStatusFrameCounterEntry_Object = MibTableRow
apexGbeStatusFrameCounterEntry = _ApexGbeStatusFrameCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1)
)
apexGbeStatusFrameCounterEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeFrameCounterGbeInterfaceNum"),
)
if mibBuilder.loadTexts:
    apexGbeStatusFrameCounterEntry.setStatus("current")


class _ApexGbeFrameCounterGbeInterfaceNum_Type(Integer32):
    """Custom type apexGbeFrameCounterGbeInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeFrameCounterGbeInterfaceNum_Type.__name__ = "Integer32"
_ApexGbeFrameCounterGbeInterfaceNum_Object = MibTableColumn
apexGbeFrameCounterGbeInterfaceNum = _ApexGbeFrameCounterGbeInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 1),
    _ApexGbeFrameCounterGbeInterfaceNum_Type()
)
apexGbeFrameCounterGbeInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeFrameCounterGbeInterfaceNum.setStatus("current")
_ApexGbeFrameCounterReset_Type = ResetStatisticsTYPE
_ApexGbeFrameCounterReset_Object = MibTableColumn
apexGbeFrameCounterReset = _ApexGbeFrameCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 2),
    _ApexGbeFrameCounterReset_Type()
)
apexGbeFrameCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeFrameCounterReset.setStatus("current")
_ApexGbeTotalRxSinglecastFrames_Type = Counter32
_ApexGbeTotalRxSinglecastFrames_Object = MibTableColumn
apexGbeTotalRxSinglecastFrames = _ApexGbeTotalRxSinglecastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 3),
    _ApexGbeTotalRxSinglecastFrames_Type()
)
apexGbeTotalRxSinglecastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxSinglecastFrames.setStatus("current")
_ApexGbeTotalRxMulticastFrames_Type = Counter32
_ApexGbeTotalRxMulticastFrames_Object = MibTableColumn
apexGbeTotalRxMulticastFrames = _ApexGbeTotalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 4),
    _ApexGbeTotalRxMulticastFrames_Type()
)
apexGbeTotalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxMulticastFrames.setStatus("current")
_ApexGbeTotalRxBroadcastFrames_Type = Counter32
_ApexGbeTotalRxBroadcastFrames_Object = MibTableColumn
apexGbeTotalRxBroadcastFrames = _ApexGbeTotalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 5),
    _ApexGbeTotalRxBroadcastFrames_Type()
)
apexGbeTotalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxBroadcastFrames.setStatus("current")
_ApexGbeTotalRxErrorFrames_Type = Counter32
_ApexGbeTotalRxErrorFrames_Object = MibTableColumn
apexGbeTotalRxErrorFrames = _ApexGbeTotalRxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 6),
    _ApexGbeTotalRxErrorFrames_Type()
)
apexGbeTotalRxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxErrorFrames.setStatus("current")
_ApexGbeTotalRxFrames_Type = Counter32
_ApexGbeTotalRxFrames_Object = MibTableColumn
apexGbeTotalRxFrames = _ApexGbeTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 7),
    _ApexGbeTotalRxFrames_Type()
)
apexGbeTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxFrames.setStatus("current")
_ApexGbeRxSinglecastFrames_Type = Counter32
_ApexGbeRxSinglecastFrames_Object = MibTableColumn
apexGbeRxSinglecastFrames = _ApexGbeRxSinglecastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 8),
    _ApexGbeRxSinglecastFrames_Type()
)
apexGbeRxSinglecastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxSinglecastFrames.setStatus("current")
_ApexGbeRxMulticastFrames_Type = Counter32
_ApexGbeRxMulticastFrames_Object = MibTableColumn
apexGbeRxMulticastFrames = _ApexGbeRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 9),
    _ApexGbeRxMulticastFrames_Type()
)
apexGbeRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxMulticastFrames.setStatus("current")
_ApexGbeRxBroadcastFrames_Type = Counter32
_ApexGbeRxBroadcastFrames_Object = MibTableColumn
apexGbeRxBroadcastFrames = _ApexGbeRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 10),
    _ApexGbeRxBroadcastFrames_Type()
)
apexGbeRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxBroadcastFrames.setStatus("current")
_ApexGbeRxErrorFrames_Type = Counter32
_ApexGbeRxErrorFrames_Object = MibTableColumn
apexGbeRxErrorFrames = _ApexGbeRxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 11),
    _ApexGbeRxErrorFrames_Type()
)
apexGbeRxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxErrorFrames.setStatus("current")
_ApexGbeRxFrames_Type = Counter32
_ApexGbeRxFrames_Object = MibTableColumn
apexGbeRxFrames = _ApexGbeRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 12),
    _ApexGbeRxFrames_Type()
)
apexGbeRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxFrames.setStatus("current")
_ApexGbeTotalTxGoodFrames_Type = Counter32
_ApexGbeTotalTxGoodFrames_Object = MibTableColumn
apexGbeTotalTxGoodFrames = _ApexGbeTotalTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 13),
    _ApexGbeTotalTxGoodFrames_Type()
)
apexGbeTotalTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalTxGoodFrames.setStatus("current")
_ApexGbeTotalTxErrorFrames_Type = Counter32
_ApexGbeTotalTxErrorFrames_Object = MibTableColumn
apexGbeTotalTxErrorFrames = _ApexGbeTotalTxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 14),
    _ApexGbeTotalTxErrorFrames_Type()
)
apexGbeTotalTxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalTxErrorFrames.setStatus("current")
_ApexGbeTxGoodFrames_Type = Counter32
_ApexGbeTxGoodFrames_Object = MibTableColumn
apexGbeTxGoodFrames = _ApexGbeTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 15),
    _ApexGbeTxGoodFrames_Type()
)
apexGbeTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTxGoodFrames.setStatus("current")
_ApexGbeTxErrorFrames_Type = Counter32
_ApexGbeTxErrorFrames_Object = MibTableColumn
apexGbeTxErrorFrames = _ApexGbeTxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 16),
    _ApexGbeTxErrorFrames_Type()
)
apexGbeTxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTxErrorFrames.setStatus("current")
_ApexGbeRxDocsisFrames_Type = Counter32
_ApexGbeRxDocsisFrames_Object = MibTableColumn
apexGbeRxDocsisFrames = _ApexGbeRxDocsisFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 17),
    _ApexGbeRxDocsisFrames_Type()
)
apexGbeRxDocsisFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxDocsisFrames.setStatus("current")
_ApexGbeTotalRxDocsisFrames_Type = Counter32
_ApexGbeTotalRxDocsisFrames_Object = MibTableColumn
apexGbeTotalRxDocsisFrames = _ApexGbeTotalRxDocsisFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 18),
    _ApexGbeTotalRxDocsisFrames_Type()
)
apexGbeTotalRxDocsisFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalRxDocsisFrames.setStatus("current")
_ApexGbeRxMpegDocsisFrames_Type = Counter32
_ApexGbeRxMpegDocsisFrames_Object = MibTableColumn
apexGbeRxMpegDocsisFrames = _ApexGbeRxMpegDocsisFrames_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 19),
    _ApexGbeRxMpegDocsisFrames_Type()
)
apexGbeRxMpegDocsisFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeRxMpegDocsisFrames.setStatus("current")
_ApexGbeIpFragmentedPkts_Type = Counter32
_ApexGbeIpFragmentedPkts_Object = MibTableColumn
apexGbeIpFragmentedPkts = _ApexGbeIpFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 20),
    _ApexGbeIpFragmentedPkts_Type()
)
apexGbeIpFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeIpFragmentedPkts.setStatus("current")
_ApexGbeTotalIpFragmentedPkts_Type = Counter32
_ApexGbeTotalIpFragmentedPkts_Object = MibTableColumn
apexGbeTotalIpFragmentedPkts = _ApexGbeTotalIpFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 6, 2, 1, 21),
    _ApexGbeTotalIpFragmentedPkts_Type()
)
apexGbeTotalIpFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeTotalIpFragmentedPkts.setStatus("current")
_ApexGbeFrameBufferStats_ObjectIdentity = ObjectIdentity
apexGbeFrameBufferStats = _ApexGbeFrameBufferStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7)
)
_ApexGbeFrameBufferStatsGeneral_ObjectIdentity = ObjectIdentity
apexGbeFrameBufferStatsGeneral = _ApexGbeFrameBufferStatsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 1)
)
_ApexGbeFrameBufferStatsTable_Object = MibTable
apexGbeFrameBufferStatsTable = _ApexGbeFrameBufferStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2)
)
if mibBuilder.loadTexts:
    apexGbeFrameBufferStatsTable.setStatus("current")
_ApexGbeFrameBufferStatsEntry_Object = MibTableRow
apexGbeFrameBufferStatsEntry = _ApexGbeFrameBufferStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1)
)
apexGbeFrameBufferStatsEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeFrameBufferProcessorNum"),
)
if mibBuilder.loadTexts:
    apexGbeFrameBufferStatsEntry.setStatus("current")


class _ApexGbeFrameBufferProcessorNum_Type(Integer32):
    """Custom type apexGbeFrameBufferProcessorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeFrameBufferProcessorNum_Type.__name__ = "Integer32"
_ApexGbeFrameBufferProcessorNum_Object = MibTableColumn
apexGbeFrameBufferProcessorNum = _ApexGbeFrameBufferProcessorNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 1),
    _ApexGbeFrameBufferProcessorNum_Type()
)
apexGbeFrameBufferProcessorNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeFrameBufferProcessorNum.setStatus("current")
_ApexGbeFrameBufferResetLevelLimit_Type = Integer32
_ApexGbeFrameBufferResetLevelLimit_Object = MibTableColumn
apexGbeFrameBufferResetLevelLimit = _ApexGbeFrameBufferResetLevelLimit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 2),
    _ApexGbeFrameBufferResetLevelLimit_Type()
)
apexGbeFrameBufferResetLevelLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferResetLevelLimit.setStatus("current")
_ApexGbeFrameBufferCurrMsLevel_Type = Integer32
_ApexGbeFrameBufferCurrMsLevel_Object = MibTableColumn
apexGbeFrameBufferCurrMsLevel = _ApexGbeFrameBufferCurrMsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 3),
    _ApexGbeFrameBufferCurrMsLevel_Type()
)
apexGbeFrameBufferCurrMsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferCurrMsLevel.setStatus("current")
_ApexGbeFrameBufferCurrPercentFull_Type = Integer32
_ApexGbeFrameBufferCurrPercentFull_Object = MibTableColumn
apexGbeFrameBufferCurrPercentFull = _ApexGbeFrameBufferCurrPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 4),
    _ApexGbeFrameBufferCurrPercentFull_Type()
)
apexGbeFrameBufferCurrPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferCurrPercentFull.setStatus("current")
_ApexGbeFrameBufferUnderflowLevel_Type = Integer32
_ApexGbeFrameBufferUnderflowLevel_Object = MibTableColumn
apexGbeFrameBufferUnderflowLevel = _ApexGbeFrameBufferUnderflowLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 5),
    _ApexGbeFrameBufferUnderflowLevel_Type()
)
apexGbeFrameBufferUnderflowLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferUnderflowLevel.setStatus("current")
_ApexGbeFrameBufferOverflowLevel_Type = Integer32
_ApexGbeFrameBufferOverflowLevel_Object = MibTableColumn
apexGbeFrameBufferOverflowLevel = _ApexGbeFrameBufferOverflowLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 6),
    _ApexGbeFrameBufferOverflowLevel_Type()
)
apexGbeFrameBufferOverflowLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferOverflowLevel.setStatus("current")


class _ApexGbeFrameBufferAlarmStatus_Type(Integer32):
    """Custom type apexGbeFrameBufferAlarmStatus based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexGbeFrameBufferAlarmStatus_Type.__name__ = "Integer32"
_ApexGbeFrameBufferAlarmStatus_Object = MibTableColumn
apexGbeFrameBufferAlarmStatus = _ApexGbeFrameBufferAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 2, 1, 7),
    _ApexGbeFrameBufferAlarmStatus_Type()
)
apexGbeFrameBufferAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferAlarmStatus.setStatus("current")
_ApexGbeFrameBufferHourlyTable_Object = MibTable
apexGbeFrameBufferHourlyTable = _ApexGbeFrameBufferHourlyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3)
)
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyTable.setStatus("current")
_ApexGbeFrameBufferHourlyEntry_Object = MibTableRow
apexGbeFrameBufferHourlyEntry = _ApexGbeFrameBufferHourlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1)
)
apexGbeFrameBufferHourlyEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeFrameBufferHourlyProcessorNum"),
    (0, "APEX-MIB", "apexGbeFrameBufferHourlyIndex"),
)
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyEntry.setStatus("current")


class _ApexGbeFrameBufferHourlyProcessorNum_Type(Integer32):
    """Custom type apexGbeFrameBufferHourlyProcessorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeFrameBufferHourlyProcessorNum_Type.__name__ = "Integer32"
_ApexGbeFrameBufferHourlyProcessorNum_Object = MibTableColumn
apexGbeFrameBufferHourlyProcessorNum = _ApexGbeFrameBufferHourlyProcessorNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 1),
    _ApexGbeFrameBufferHourlyProcessorNum_Type()
)
apexGbeFrameBufferHourlyProcessorNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyProcessorNum.setStatus("current")


class _ApexGbeFrameBufferHourlyIndex_Type(Integer32):
    """Custom type apexGbeFrameBufferHourlyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ApexGbeFrameBufferHourlyIndex_Type.__name__ = "Integer32"
_ApexGbeFrameBufferHourlyIndex_Object = MibTableColumn
apexGbeFrameBufferHourlyIndex = _ApexGbeFrameBufferHourlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 2),
    _ApexGbeFrameBufferHourlyIndex_Type()
)
apexGbeFrameBufferHourlyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyIndex.setStatus("current")


class _ApexGbeFrameBufferHourlyInInterface_Type(Integer32):
    """Custom type apexGbeFrameBufferHourlyInInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexGbeFrameBufferHourlyInInterface_Type.__name__ = "Integer32"
_ApexGbeFrameBufferHourlyInInterface_Object = MibTableColumn
apexGbeFrameBufferHourlyInInterface = _ApexGbeFrameBufferHourlyInInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 3),
    _ApexGbeFrameBufferHourlyInInterface_Type()
)
apexGbeFrameBufferHourlyInInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyInInterface.setStatus("current")


class _ApexGbeFrameBufferHourlyInUdp_Type(Integer32):
    """Custom type apexGbeFrameBufferHourlyInUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexGbeFrameBufferHourlyInUdp_Type.__name__ = "Integer32"
_ApexGbeFrameBufferHourlyInUdp_Object = MibTableColumn
apexGbeFrameBufferHourlyInUdp = _ApexGbeFrameBufferHourlyInUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 4),
    _ApexGbeFrameBufferHourlyInUdp_Type()
)
apexGbeFrameBufferHourlyInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyInUdp.setStatus("current")
_ApexGbeFrameBufferHourlyInMulticastIp_Type = IpAddress
_ApexGbeFrameBufferHourlyInMulticastIp_Object = MibTableColumn
apexGbeFrameBufferHourlyInMulticastIp = _ApexGbeFrameBufferHourlyInMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 5),
    _ApexGbeFrameBufferHourlyInMulticastIp_Type()
)
apexGbeFrameBufferHourlyInMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyInMulticastIp.setStatus("current")
_ApexGbeFrameBufferHourlyInSourceIp_Type = IpAddress
_ApexGbeFrameBufferHourlyInSourceIp_Object = MibTableColumn
apexGbeFrameBufferHourlyInSourceIp = _ApexGbeFrameBufferHourlyInSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 6),
    _ApexGbeFrameBufferHourlyInSourceIp_Type()
)
apexGbeFrameBufferHourlyInSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyInSourceIp.setStatus("current")
_ApexGbeFrameBufferHourlyMaxMsLevel_Type = Integer32
_ApexGbeFrameBufferHourlyMaxMsLevel_Object = MibTableColumn
apexGbeFrameBufferHourlyMaxMsLevel = _ApexGbeFrameBufferHourlyMaxMsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 7),
    _ApexGbeFrameBufferHourlyMaxMsLevel_Type()
)
apexGbeFrameBufferHourlyMaxMsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyMaxMsLevel.setStatus("current")
_ApexGbeFrameBufferHourlyMaxPercentFull_Type = Integer32
_ApexGbeFrameBufferHourlyMaxPercentFull_Object = MibTableColumn
apexGbeFrameBufferHourlyMaxPercentFull = _ApexGbeFrameBufferHourlyMaxPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 8),
    _ApexGbeFrameBufferHourlyMaxPercentFull_Type()
)
apexGbeFrameBufferHourlyMaxPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyMaxPercentFull.setStatus("current")
_ApexGbeFrameBufferHourlyGpsTime_Type = Integer32
_ApexGbeFrameBufferHourlyGpsTime_Object = MibTableColumn
apexGbeFrameBufferHourlyGpsTime = _ApexGbeFrameBufferHourlyGpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 9),
    _ApexGbeFrameBufferHourlyGpsTime_Type()
)
apexGbeFrameBufferHourlyGpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyGpsTime.setStatus("current")
_ApexGbeFrameBufferHourlyOverflows_Type = Integer32
_ApexGbeFrameBufferHourlyOverflows_Object = MibTableColumn
apexGbeFrameBufferHourlyOverflows = _ApexGbeFrameBufferHourlyOverflows_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 10),
    _ApexGbeFrameBufferHourlyOverflows_Type()
)
apexGbeFrameBufferHourlyOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyOverflows.setStatus("current")
_ApexGbeFrameBufferHourlyResets_Type = Integer32
_ApexGbeFrameBufferHourlyResets_Object = MibTableColumn
apexGbeFrameBufferHourlyResets = _ApexGbeFrameBufferHourlyResets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 7, 3, 1, 11),
    _ApexGbeFrameBufferHourlyResets_Type()
)
apexGbeFrameBufferHourlyResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeFrameBufferHourlyResets.setStatus("current")
_ApexGbeStatusInputTransportStream_ObjectIdentity = ObjectIdentity
apexGbeStatusInputTransportStream = _ApexGbeStatusInputTransportStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8)
)
_ApexGbeStatusInputTsGeneral_ObjectIdentity = ObjectIdentity
apexGbeStatusInputTsGeneral = _ApexGbeStatusInputTsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 1)
)
_ApexGbeStatusInputTsUpdateInterval_Type = Integer32
_ApexGbeStatusInputTsUpdateInterval_Object = MibScalar
apexGbeStatusInputTsUpdateInterval = _ApexGbeStatusInputTsUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 1, 1),
    _ApexGbeStatusInputTsUpdateInterval_Type()
)
apexGbeStatusInputTsUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusInputTsUpdateInterval.setStatus("current")
_ApexGbeStatusInputTsTable_Object = MibTable
apexGbeStatusInputTsTable = _ApexGbeStatusInputTsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2)
)
if mibBuilder.loadTexts:
    apexGbeStatusInputTsTable.setStatus("current")
_ApexGbeStatusInputTsEntry_Object = MibTableRow
apexGbeStatusInputTsEntry = _ApexGbeStatusInputTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1)
)
apexGbeStatusInputTsEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeStatInTsInputTsNum"),
)
if mibBuilder.loadTexts:
    apexGbeStatusInputTsEntry.setStatus("current")


class _ApexGbeStatInTsInputTsNum_Type(Integer32):
    """Custom type apexGbeStatInTsInputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexGbeStatInTsInputTsNum_Type.__name__ = "Integer32"
_ApexGbeStatInTsInputTsNum_Object = MibTableColumn
apexGbeStatInTsInputTsNum = _ApexGbeStatInTsInputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 1),
    _ApexGbeStatInTsInputTsNum_Type()
)
apexGbeStatInTsInputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeStatInTsInputTsNum.setStatus("current")


class _ApexGbeStatInTsSamplingPeriod_Type(Integer32):
    """Custom type apexGbeStatInTsSamplingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ApexGbeStatInTsSamplingPeriod_Type.__name__ = "Integer32"
_ApexGbeStatInTsSamplingPeriod_Object = MibTableColumn
apexGbeStatInTsSamplingPeriod = _ApexGbeStatInTsSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 2),
    _ApexGbeStatInTsSamplingPeriod_Type()
)
apexGbeStatInTsSamplingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSamplingPeriod.setStatus("current")
_ApexGbeStatInTsPriCurDataCount_Type = Counter32
_ApexGbeStatInTsPriCurDataCount_Object = MibTableColumn
apexGbeStatInTsPriCurDataCount = _ApexGbeStatInTsPriCurDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 3),
    _ApexGbeStatInTsPriCurDataCount_Type()
)
apexGbeStatInTsPriCurDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriCurDataCount.setStatus("current")
_ApexGbeStatInTsPriAvgDataCount_Type = Counter32
_ApexGbeStatInTsPriAvgDataCount_Object = MibTableColumn
apexGbeStatInTsPriAvgDataCount = _ApexGbeStatInTsPriAvgDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 4),
    _ApexGbeStatInTsPriAvgDataCount_Type()
)
apexGbeStatInTsPriAvgDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriAvgDataCount.setStatus("current")
_ApexGbeStatInTsPriMinDataCount_Type = Counter32
_ApexGbeStatInTsPriMinDataCount_Object = MibTableColumn
apexGbeStatInTsPriMinDataCount = _ApexGbeStatInTsPriMinDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 5),
    _ApexGbeStatInTsPriMinDataCount_Type()
)
apexGbeStatInTsPriMinDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriMinDataCount.setStatus("current")
_ApexGbeStatInTsPriPeakDataCount_Type = Counter32
_ApexGbeStatInTsPriPeakDataCount_Object = MibTableColumn
apexGbeStatInTsPriPeakDataCount = _ApexGbeStatInTsPriPeakDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 6),
    _ApexGbeStatInTsPriPeakDataCount_Type()
)
apexGbeStatInTsPriPeakDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriPeakDataCount.setStatus("current")
_ApexGbeStatInTsPriCurStreamCount_Type = Counter32
_ApexGbeStatInTsPriCurStreamCount_Object = MibTableColumn
apexGbeStatInTsPriCurStreamCount = _ApexGbeStatInTsPriCurStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 7),
    _ApexGbeStatInTsPriCurStreamCount_Type()
)
apexGbeStatInTsPriCurStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriCurStreamCount.setStatus("current")
_ApexGbeStatInTsPriAvgStreamCount_Type = Counter32
_ApexGbeStatInTsPriAvgStreamCount_Object = MibTableColumn
apexGbeStatInTsPriAvgStreamCount = _ApexGbeStatInTsPriAvgStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 8),
    _ApexGbeStatInTsPriAvgStreamCount_Type()
)
apexGbeStatInTsPriAvgStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriAvgStreamCount.setStatus("current")
_ApexGbeStatInTsPriMinStreamCount_Type = Counter32
_ApexGbeStatInTsPriMinStreamCount_Object = MibTableColumn
apexGbeStatInTsPriMinStreamCount = _ApexGbeStatInTsPriMinStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 9),
    _ApexGbeStatInTsPriMinStreamCount_Type()
)
apexGbeStatInTsPriMinStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriMinStreamCount.setStatus("current")
_ApexGbeStatInTsPriPeakStreamCount_Type = Counter32
_ApexGbeStatInTsPriPeakStreamCount_Object = MibTableColumn
apexGbeStatInTsPriPeakStreamCount = _ApexGbeStatInTsPriPeakStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 10),
    _ApexGbeStatInTsPriPeakStreamCount_Type()
)
apexGbeStatInTsPriPeakStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriPeakStreamCount.setStatus("current")
_ApexGbeStatInTsSecCurDataCount_Type = Counter32
_ApexGbeStatInTsSecCurDataCount_Object = MibTableColumn
apexGbeStatInTsSecCurDataCount = _ApexGbeStatInTsSecCurDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 11),
    _ApexGbeStatInTsSecCurDataCount_Type()
)
apexGbeStatInTsSecCurDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecCurDataCount.setStatus("current")
_ApexGbeStatInTsSecAvgDataCount_Type = Counter32
_ApexGbeStatInTsSecAvgDataCount_Object = MibTableColumn
apexGbeStatInTsSecAvgDataCount = _ApexGbeStatInTsSecAvgDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 12),
    _ApexGbeStatInTsSecAvgDataCount_Type()
)
apexGbeStatInTsSecAvgDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecAvgDataCount.setStatus("current")
_ApexGbeStatInTsSecMinDataCount_Type = Counter32
_ApexGbeStatInTsSecMinDataCount_Object = MibTableColumn
apexGbeStatInTsSecMinDataCount = _ApexGbeStatInTsSecMinDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 13),
    _ApexGbeStatInTsSecMinDataCount_Type()
)
apexGbeStatInTsSecMinDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecMinDataCount.setStatus("current")
_ApexGbeStatInTsSecPeakDataCount_Type = Counter32
_ApexGbeStatInTsSecPeakDataCount_Object = MibTableColumn
apexGbeStatInTsSecPeakDataCount = _ApexGbeStatInTsSecPeakDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 14),
    _ApexGbeStatInTsSecPeakDataCount_Type()
)
apexGbeStatInTsSecPeakDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecPeakDataCount.setStatus("current")
_ApexGbeStatInTsSecCurStreamCount_Type = Counter32
_ApexGbeStatInTsSecCurStreamCount_Object = MibTableColumn
apexGbeStatInTsSecCurStreamCount = _ApexGbeStatInTsSecCurStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 15),
    _ApexGbeStatInTsSecCurStreamCount_Type()
)
apexGbeStatInTsSecCurStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecCurStreamCount.setStatus("current")
_ApexGbeStatInTsSecAvgStreamCount_Type = Counter32
_ApexGbeStatInTsSecAvgStreamCount_Object = MibTableColumn
apexGbeStatInTsSecAvgStreamCount = _ApexGbeStatInTsSecAvgStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 16),
    _ApexGbeStatInTsSecAvgStreamCount_Type()
)
apexGbeStatInTsSecAvgStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecAvgStreamCount.setStatus("current")
_ApexGbeStatInTsSecMinStreamCount_Type = Counter32
_ApexGbeStatInTsSecMinStreamCount_Object = MibTableColumn
apexGbeStatInTsSecMinStreamCount = _ApexGbeStatInTsSecMinStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 17),
    _ApexGbeStatInTsSecMinStreamCount_Type()
)
apexGbeStatInTsSecMinStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecMinStreamCount.setStatus("current")
_ApexGbeStatInTsSecPeakStreamCount_Type = Counter32
_ApexGbeStatInTsSecPeakStreamCount_Object = MibTableColumn
apexGbeStatInTsSecPeakStreamCount = _ApexGbeStatInTsSecPeakStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 2, 1, 18),
    _ApexGbeStatInTsSecPeakStreamCount_Type()
)
apexGbeStatInTsSecPeakStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecPeakStreamCount.setStatus("current")
_ApexGbeStatusInputTsErrorTable_Object = MibTable
apexGbeStatusInputTsErrorTable = _ApexGbeStatusInputTsErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3)
)
if mibBuilder.loadTexts:
    apexGbeStatusInputTsErrorTable.setStatus("current")
_ApexGbeStatusInputTsErrorEntry_Object = MibTableRow
apexGbeStatusInputTsErrorEntry = _ApexGbeStatusInputTsErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1)
)
apexGbeStatusInputTsErrorEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeStatInTsErrorInputTsNum"),
)
if mibBuilder.loadTexts:
    apexGbeStatusInputTsErrorEntry.setStatus("current")


class _ApexGbeStatInTsErrorInputTsNum_Type(Integer32):
    """Custom type apexGbeStatInTsErrorInputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexGbeStatInTsErrorInputTsNum_Type.__name__ = "Integer32"
_ApexGbeStatInTsErrorInputTsNum_Object = MibTableColumn
apexGbeStatInTsErrorInputTsNum = _ApexGbeStatInTsErrorInputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 1),
    _ApexGbeStatInTsErrorInputTsNum_Type()
)
apexGbeStatInTsErrorInputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeStatInTsErrorInputTsNum.setStatus("current")


class _ApexGbeStatInTsPriErrorSummary_Type(Integer32):
    """Custom type apexGbeStatInTsPriErrorSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsPriErrorSummary_Type.__name__ = "Integer32"
_ApexGbeStatInTsPriErrorSummary_Object = MibTableColumn
apexGbeStatInTsPriErrorSummary = _ApexGbeStatInTsPriErrorSummary_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 2),
    _ApexGbeStatInTsPriErrorSummary_Type()
)
apexGbeStatInTsPriErrorSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriErrorSummary.setStatus("current")


class _ApexGbeStatInTsPriLowBitRateError_Type(Integer32):
    """Custom type apexGbeStatInTsPriLowBitRateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsPriLowBitRateError_Type.__name__ = "Integer32"
_ApexGbeStatInTsPriLowBitRateError_Object = MibTableColumn
apexGbeStatInTsPriLowBitRateError = _ApexGbeStatInTsPriLowBitRateError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 3),
    _ApexGbeStatInTsPriLowBitRateError_Type()
)
apexGbeStatInTsPriLowBitRateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriLowBitRateError.setStatus("current")


class _ApexGbeStatInTsPriHighBitRateError_Type(Integer32):
    """Custom type apexGbeStatInTsPriHighBitRateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsPriHighBitRateError_Type.__name__ = "Integer32"
_ApexGbeStatInTsPriHighBitRateError_Object = MibTableColumn
apexGbeStatInTsPriHighBitRateError = _ApexGbeStatInTsPriHighBitRateError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 4),
    _ApexGbeStatInTsPriHighBitRateError_Type()
)
apexGbeStatInTsPriHighBitRateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriHighBitRateError.setStatus("current")


class _ApexGbeStatInTsMptsRedundPriError_Type(Integer32):
    """Custom type apexGbeStatInTsMptsRedundPriError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsMptsRedundPriError_Type.__name__ = "Integer32"
_ApexGbeStatInTsMptsRedundPriError_Object = MibTableColumn
apexGbeStatInTsMptsRedundPriError = _ApexGbeStatInTsMptsRedundPriError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 5),
    _ApexGbeStatInTsMptsRedundPriError_Type()
)
apexGbeStatInTsMptsRedundPriError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsMptsRedundPriError.setStatus("current")


class _ApexGbeStatInTsMptsRedundFailError_Type(Integer32):
    """Custom type apexGbeStatInTsMptsRedundFailError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsMptsRedundFailError_Type.__name__ = "Integer32"
_ApexGbeStatInTsMptsRedundFailError_Object = MibTableColumn
apexGbeStatInTsMptsRedundFailError = _ApexGbeStatInTsMptsRedundFailError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 6),
    _ApexGbeStatInTsMptsRedundFailError_Type()
)
apexGbeStatInTsMptsRedundFailError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsMptsRedundFailError.setStatus("current")


class _ApexGbeStatInTsSecErrorSummary_Type(Integer32):
    """Custom type apexGbeStatInTsSecErrorSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsSecErrorSummary_Type.__name__ = "Integer32"
_ApexGbeStatInTsSecErrorSummary_Object = MibTableColumn
apexGbeStatInTsSecErrorSummary = _ApexGbeStatInTsSecErrorSummary_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 7),
    _ApexGbeStatInTsSecErrorSummary_Type()
)
apexGbeStatInTsSecErrorSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecErrorSummary.setStatus("current")


class _ApexGbeStatInTsSecLowBitRateError_Type(Integer32):
    """Custom type apexGbeStatInTsSecLowBitRateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsSecLowBitRateError_Type.__name__ = "Integer32"
_ApexGbeStatInTsSecLowBitRateError_Object = MibTableColumn
apexGbeStatInTsSecLowBitRateError = _ApexGbeStatInTsSecLowBitRateError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 8),
    _ApexGbeStatInTsSecLowBitRateError_Type()
)
apexGbeStatInTsSecLowBitRateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecLowBitRateError.setStatus("current")


class _ApexGbeStatInTsSecHighBitRateError_Type(Integer32):
    """Custom type apexGbeStatInTsSecHighBitRateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsSecHighBitRateError_Type.__name__ = "Integer32"
_ApexGbeStatInTsSecHighBitRateError_Object = MibTableColumn
apexGbeStatInTsSecHighBitRateError = _ApexGbeStatInTsSecHighBitRateError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 9),
    _ApexGbeStatInTsSecHighBitRateError_Type()
)
apexGbeStatInTsSecHighBitRateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecHighBitRateError.setStatus("current")


class _ApexGbeStatInTsPriLossInputError_Type(Integer32):
    """Custom type apexGbeStatInTsPriLossInputError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsPriLossInputError_Type.__name__ = "Integer32"
_ApexGbeStatInTsPriLossInputError_Object = MibTableColumn
apexGbeStatInTsPriLossInputError = _ApexGbeStatInTsPriLossInputError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 10),
    _ApexGbeStatInTsPriLossInputError_Type()
)
apexGbeStatInTsPriLossInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsPriLossInputError.setStatus("current")


class _ApexGbeStatInTsSecLossInputError_Type(Integer32):
    """Custom type apexGbeStatInTsSecLossInputError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexGbeStatInTsSecLossInputError_Type.__name__ = "Integer32"
_ApexGbeStatInTsSecLossInputError_Object = MibTableColumn
apexGbeStatInTsSecLossInputError = _ApexGbeStatInTsSecLossInputError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 8, 3, 1, 11),
    _ApexGbeStatInTsSecLossInputError_Type()
)
apexGbeStatInTsSecLossInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatInTsSecLossInputError.setStatus("current")
_ApexGbeStatusInterfaceRedund_ObjectIdentity = ObjectIdentity
apexGbeStatusInterfaceRedund = _ApexGbeStatusInterfaceRedund_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9)
)
_ApexGbeStatusInterfaceRedundTable_Object = MibTable
apexGbeStatusInterfaceRedundTable = _ApexGbeStatusInterfaceRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1)
)
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundTable.setStatus("current")
_ApexGbeStatusInterfaceRedundEntry_Object = MibTableRow
apexGbeStatusInterfaceRedundEntry = _ApexGbeStatusInterfaceRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1, 1)
)
apexGbeStatusInterfaceRedundEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeStatusInterfaceRedundIndex"),
)
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundEntry.setStatus("current")


class _ApexGbeStatusInterfaceRedundIndex_Type(Integer32):
    """Custom type apexGbeStatusInterfaceRedundIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexGbeStatusInterfaceRedundIndex_Type.__name__ = "Integer32"
_ApexGbeStatusInterfaceRedundIndex_Object = MibTableColumn
apexGbeStatusInterfaceRedundIndex = _ApexGbeStatusInterfaceRedundIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1, 1, 1),
    _ApexGbeStatusInterfaceRedundIndex_Type()
)
apexGbeStatusInterfaceRedundIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundIndex.setStatus("current")


class _ApexGbeStatusInterfaceRedundActiveIf_Type(Integer32):
    """Custom type apexGbeStatusInterfaceRedundActiveIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexGbeStatusInterfaceRedundActiveIf_Type.__name__ = "Integer32"
_ApexGbeStatusInterfaceRedundActiveIf_Object = MibTableColumn
apexGbeStatusInterfaceRedundActiveIf = _ApexGbeStatusInterfaceRedundActiveIf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1, 1, 2),
    _ApexGbeStatusInterfaceRedundActiveIf_Type()
)
apexGbeStatusInterfaceRedundActiveIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundActiveIf.setStatus("current")


class _ApexGbeStatusInterfaceRedundInvalidApplyText_Type(DisplayString):
    """Custom type apexGbeStatusInterfaceRedundInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexGbeStatusInterfaceRedundInvalidApplyText_Type.__name__ = "DisplayString"
_ApexGbeStatusInterfaceRedundInvalidApplyText_Object = MibTableColumn
apexGbeStatusInterfaceRedundInvalidApplyText = _ApexGbeStatusInterfaceRedundInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1, 1, 3),
    _ApexGbeStatusInterfaceRedundInvalidApplyText_Type()
)
apexGbeStatusInterfaceRedundInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundInvalidApplyText.setStatus("current")


class _ApexGbeStatusInterfaceRedundFaultCondition_Type(Integer32):
    """Custom type apexGbeStatusInterfaceRedundFaultCondition based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexGbeStatusInterfaceRedundFaultCondition_Type.__name__ = "Integer32"
_ApexGbeStatusInterfaceRedundFaultCondition_Object = MibTableColumn
apexGbeStatusInterfaceRedundFaultCondition = _ApexGbeStatusInterfaceRedundFaultCondition_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 2, 9, 1, 1, 4),
    _ApexGbeStatusInterfaceRedundFaultCondition_Type()
)
apexGbeStatusInterfaceRedundFaultCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeStatusInterfaceRedundFaultCondition.setStatus("current")
_ApexGbeSfp_ObjectIdentity = ObjectIdentity
apexGbeSfp = _ApexGbeSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3)
)
_ApexGbeSfpConfig_ObjectIdentity = ObjectIdentity
apexGbeSfpConfig = _ApexGbeSfpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 1)
)
_ApexGbeSfpConfigGeneral_ObjectIdentity = ObjectIdentity
apexGbeSfpConfigGeneral = _ApexGbeSfpConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 1, 1)
)


class _ApexGbeSfpUpdateStatus_Type(Integer32):
    """Custom type apexGbeSfpUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("update", 2),
          ("updateNotInProgress", 1))
    )


_ApexGbeSfpUpdateStatus_Type.__name__ = "Integer32"
_ApexGbeSfpUpdateStatus_Object = MibScalar
apexGbeSfpUpdateStatus = _ApexGbeSfpUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 1, 1, 1),
    _ApexGbeSfpUpdateStatus_Type()
)
apexGbeSfpUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexGbeSfpUpdateStatus.setStatus("current")
_ApexGbeSfpStatus_ObjectIdentity = ObjectIdentity
apexGbeSfpStatus = _ApexGbeSfpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2)
)
_ApexGbeSfpStatusGeneral_ObjectIdentity = ObjectIdentity
apexGbeSfpStatusGeneral = _ApexGbeSfpStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 1)
)
_ApexGbeSfpStatusTable_Object = MibTable
apexGbeSfpStatusTable = _ApexGbeSfpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    apexGbeSfpStatusTable.setStatus("current")
_ApexGbeSfpStatusEntry_Object = MibTableRow
apexGbeSfpStatusEntry = _ApexGbeSfpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 2, 1)
)
apexGbeSfpStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeSfpStatusGbeIfNum"),
)
if mibBuilder.loadTexts:
    apexGbeSfpStatusEntry.setStatus("current")


class _ApexGbeSfpStatusGbeIfNum_Type(Integer32):
    """Custom type apexGbeSfpStatusGbeIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexGbeSfpStatusGbeIfNum_Type.__name__ = "Integer32"
_ApexGbeSfpStatusGbeIfNum_Object = MibTableColumn
apexGbeSfpStatusGbeIfNum = _ApexGbeSfpStatusGbeIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 2, 1, 1),
    _ApexGbeSfpStatusGbeIfNum_Type()
)
apexGbeSfpStatusGbeIfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeSfpStatusGbeIfNum.setStatus("current")
_ApexGbeSfpStatusVendorId_Type = DisplayString
_ApexGbeSfpStatusVendorId_Object = MibTableColumn
apexGbeSfpStatusVendorId = _ApexGbeSfpStatusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 2, 1, 2),
    _ApexGbeSfpStatusVendorId_Type()
)
apexGbeSfpStatusVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeSfpStatusVendorId.setStatus("current")


class _ApexGbeSfpStatusDiagInfo_Type(DisplayString):
    """Custom type apexGbeSfpStatusDiagInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexGbeSfpStatusDiagInfo_Type.__name__ = "DisplayString"
_ApexGbeSfpStatusDiagInfo_Object = MibTableColumn
apexGbeSfpStatusDiagInfo = _ApexGbeSfpStatusDiagInfo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 7, 3, 2, 2, 1, 3),
    _ApexGbeSfpStatusDiagInfo_Type()
)
apexGbeSfpStatusDiagInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeSfpStatusDiagInfo.setStatus("current")
_ApexQam_ObjectIdentity = ObjectIdentity
apexQam = _ApexQam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8)
)
_ApexQamConfig_ObjectIdentity = ObjectIdentity
apexQamConfig = _ApexQamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1)
)
_ApexQamConfigGeneral_ObjectIdentity = ObjectIdentity
apexQamConfigGeneral = _ApexQamConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 1)
)


class _ApexQamConfigTransmissionMode_Type(Integer32):
    """Custom type apexQamConfigTransmissionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA-DVB", 2),
          ("annexB-ATSC-DCII", 1),
          ("annexC-Asia-Pacific", 3))
    )


_ApexQamConfigTransmissionMode_Type.__name__ = "Integer32"
_ApexQamConfigTransmissionMode_Object = MibScalar
apexQamConfigTransmissionMode = _ApexQamConfigTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 1, 1),
    _ApexQamConfigTransmissionMode_Type()
)
apexQamConfigTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamConfigTransmissionMode.setStatus("current")
_ApexQamModuleUpgrade_ObjectIdentity = ObjectIdentity
apexQamModuleUpgrade = _ApexQamModuleUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 2)
)


class _ApexQamModuleUpgradeSlot_Type(Integer32):
    """Custom type apexQamModuleUpgradeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ApexQamModuleUpgradeSlot_Type.__name__ = "Integer32"
_ApexQamModuleUpgradeSlot_Object = MibScalar
apexQamModuleUpgradeSlot = _ApexQamModuleUpgradeSlot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 2, 1),
    _ApexQamModuleUpgradeSlot_Type()
)
apexQamModuleUpgradeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamModuleUpgradeSlot.setStatus("current")


class _ApexQamModuleUpgradeCode_Type(DisplayString):
    """Custom type apexQamModuleUpgradeCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_ApexQamModuleUpgradeCode_Type.__name__ = "DisplayString"
_ApexQamModuleUpgradeCode_Object = MibScalar
apexQamModuleUpgradeCode = _ApexQamModuleUpgradeCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 2, 2),
    _ApexQamModuleUpgradeCode_Type()
)
apexQamModuleUpgradeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamModuleUpgradeCode.setStatus("current")
_ApexQamModuleUpgradeApplyChange_Type = ApplyDataToDeviceTYPE
_ApexQamModuleUpgradeApplyChange_Object = MibScalar
apexQamModuleUpgradeApplyChange = _ApexQamModuleUpgradeApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 2, 3),
    _ApexQamModuleUpgradeApplyChange_Type()
)
apexQamModuleUpgradeApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamModuleUpgradeApplyChange.setStatus("current")
_ApexQamConfigApplyTable_Object = MibTable
apexQamConfigApplyTable = _ApexQamConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 3)
)
if mibBuilder.loadTexts:
    apexQamConfigApplyTable.setStatus("current")
_ApexQamConfigApplyEntry_Object = MibTableRow
apexQamConfigApplyEntry = _ApexQamConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 3, 1)
)
apexQamConfigApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamConfigApplyRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamConfigApplyEntry.setStatus("current")


class _ApexQamConfigApplyRfPortNum_Type(Integer32):
    """Custom type apexQamConfigApplyRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexQamConfigApplyRfPortNum_Type.__name__ = "Integer32"
_ApexQamConfigApplyRfPortNum_Object = MibTableColumn
apexQamConfigApplyRfPortNum = _ApexQamConfigApplyRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 3, 1, 1),
    _ApexQamConfigApplyRfPortNum_Type()
)
apexQamConfigApplyRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamConfigApplyRfPortNum.setStatus("current")
_ApexQamConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexQamConfigApplyChange_Object = MibTableColumn
apexQamConfigApplyChange = _ApexQamConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 3, 1, 2),
    _ApexQamConfigApplyChange_Type()
)
apexQamConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamConfigApplyChange.setStatus("current")
_ApexQamRfConfigTable_Object = MibTable
apexQamRfConfigTable = _ApexQamRfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4)
)
if mibBuilder.loadTexts:
    apexQamRfConfigTable.setStatus("current")
_ApexQamRfConfigEntry_Object = MibTableRow
apexQamRfConfigEntry = _ApexQamRfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1)
)
apexQamRfConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamRfConfigRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamRfConfigEntry.setStatus("current")


class _ApexQamRfConfigRfPortNum_Type(Integer32):
    """Custom type apexQamRfConfigRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexQamRfConfigRfPortNum_Type.__name__ = "Integer32"
_ApexQamRfConfigRfPortNum_Object = MibTableColumn
apexQamRfConfigRfPortNum = _ApexQamRfConfigRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 1),
    _ApexQamRfConfigRfPortNum_Type()
)
apexQamRfConfigRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamRfConfigRfPortNum.setStatus("current")


class _ApexQamRfConfigNumChannelsEnabled_Type(Integer32):
    """Custom type apexQamRfConfigNumChannelsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ApexQamRfConfigNumChannelsEnabled_Type.__name__ = "Integer32"
_ApexQamRfConfigNumChannelsEnabled_Object = MibTableColumn
apexQamRfConfigNumChannelsEnabled = _ApexQamRfConfigNumChannelsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 2),
    _ApexQamRfConfigNumChannelsEnabled_Type()
)
apexQamRfConfigNumChannelsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigNumChannelsEnabled.setStatus("current")


class _ApexQamRfConfigModulationMode_Type(Integer32):
    """Custom type apexQamRfConfigModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qam256", 2),
          ("qam64", 1))
    )


_ApexQamRfConfigModulationMode_Type.__name__ = "Integer32"
_ApexQamRfConfigModulationMode_Object = MibTableColumn
apexQamRfConfigModulationMode = _ApexQamRfConfigModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 3),
    _ApexQamRfConfigModulationMode_Type()
)
apexQamRfConfigModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigModulationMode.setStatus("current")


class _ApexQamRfConfigSymbolRate_Type(Integer32):
    """Custom type apexQamRfConfigSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800000, 6980000),
    )


_ApexQamRfConfigSymbolRate_Type.__name__ = "Integer32"
_ApexQamRfConfigSymbolRate_Object = MibTableColumn
apexQamRfConfigSymbolRate = _ApexQamRfConfigSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 4),
    _ApexQamRfConfigSymbolRate_Type()
)
apexQamRfConfigSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigSymbolRate.setStatus("current")


class _ApexQamRfConfigSpectrumInvert_Type(Integer32):
    """Custom type apexQamRfConfigSpectrumInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert", 2),
          ("normal", 1))
    )


_ApexQamRfConfigSpectrumInvert_Type.__name__ = "Integer32"
_ApexQamRfConfigSpectrumInvert_Object = MibTableColumn
apexQamRfConfigSpectrumInvert = _ApexQamRfConfigSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 5),
    _ApexQamRfConfigSpectrumInvert_Type()
)
apexQamRfConfigSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigSpectrumInvert.setStatus("current")


class _ApexQamRfConfigTuningMode_Type(Integer32):
    """Custom type apexQamRfConfigTuningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel", 2),
          ("frequency", 1))
    )


_ApexQamRfConfigTuningMode_Type.__name__ = "Integer32"
_ApexQamRfConfigTuningMode_Object = MibTableColumn
apexQamRfConfigTuningMode = _ApexQamRfConfigTuningMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 6),
    _ApexQamRfConfigTuningMode_Type()
)
apexQamRfConfigTuningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigTuningMode.setStatus("current")


class _ApexQamRfConfigEiaFrequencyPlan_Type(Integer32):
    """Custom type apexQamRfConfigEiaFrequencyPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hrc", 2),
          ("irc", 3),
          ("std", 1))
    )


_ApexQamRfConfigEiaFrequencyPlan_Type.__name__ = "Integer32"
_ApexQamRfConfigEiaFrequencyPlan_Object = MibTableColumn
apexQamRfConfigEiaFrequencyPlan = _ApexQamRfConfigEiaFrequencyPlan_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 7),
    _ApexQamRfConfigEiaFrequencyPlan_Type()
)
apexQamRfConfigEiaFrequencyPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigEiaFrequencyPlan.setStatus("current")


class _ApexQamRfConfigEiaChanNumChannelA_Type(Integer32):
    """Custom type apexQamRfConfigEiaChanNumChannelA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 158),
    )


_ApexQamRfConfigEiaChanNumChannelA_Type.__name__ = "Integer32"
_ApexQamRfConfigEiaChanNumChannelA_Object = MibTableColumn
apexQamRfConfigEiaChanNumChannelA = _ApexQamRfConfigEiaChanNumChannelA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 8),
    _ApexQamRfConfigEiaChanNumChannelA_Type()
)
apexQamRfConfigEiaChanNumChannelA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigEiaChanNumChannelA.setStatus("current")


class _ApexQamRfConfigRfCenterFreqChannelA_Type(Integer32):
    """Custom type apexQamRfConfigRfCenterFreqChannelA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 999000000),
    )


_ApexQamRfConfigRfCenterFreqChannelA_Type.__name__ = "Integer32"
_ApexQamRfConfigRfCenterFreqChannelA_Object = MibTableColumn
apexQamRfConfigRfCenterFreqChannelA = _ApexQamRfConfigRfCenterFreqChannelA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 9),
    _ApexQamRfConfigRfCenterFreqChannelA_Type()
)
apexQamRfConfigRfCenterFreqChannelA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigRfCenterFreqChannelA.setStatus("current")


class _ApexQamRfConfigRfChanSpacing_Type(Integer32):
    """Custom type apexQamRfConfigRfChanSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 8000000),
    )


_ApexQamRfConfigRfChanSpacing_Type.__name__ = "Integer32"
_ApexQamRfConfigRfChanSpacing_Object = MibTableColumn
apexQamRfConfigRfChanSpacing = _ApexQamRfConfigRfChanSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 10),
    _ApexQamRfConfigRfChanSpacing_Type()
)
apexQamRfConfigRfChanSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigRfChanSpacing.setStatus("current")


class _ApexQamRfConfigRfLevelAttenuation_Type(Integer32):
    """Custom type apexQamRfConfigRfLevelAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 800),
    )


_ApexQamRfConfigRfLevelAttenuation_Type.__name__ = "Integer32"
_ApexQamRfConfigRfLevelAttenuation_Object = MibTableColumn
apexQamRfConfigRfLevelAttenuation = _ApexQamRfConfigRfLevelAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 11),
    _ApexQamRfConfigRfLevelAttenuation_Type()
)
apexQamRfConfigRfLevelAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigRfLevelAttenuation.setStatus("current")


class _ApexQamRfConfigRfLevelLowThreshold_Type(Integer32):
    """Custom type apexQamRfConfigRfLevelLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexQamRfConfigRfLevelLowThreshold_Type.__name__ = "Integer32"
_ApexQamRfConfigRfLevelLowThreshold_Object = MibTableColumn
apexQamRfConfigRfLevelLowThreshold = _ApexQamRfConfigRfLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 12),
    _ApexQamRfConfigRfLevelLowThreshold_Type()
)
apexQamRfConfigRfLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigRfLevelLowThreshold.setStatus("current")


class _ApexQamRfConfigRfLevelHighThreshold_Type(Integer32):
    """Custom type apexQamRfConfigRfLevelHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexQamRfConfigRfLevelHighThreshold_Type.__name__ = "Integer32"
_ApexQamRfConfigRfLevelHighThreshold_Object = MibTableColumn
apexQamRfConfigRfLevelHighThreshold = _ApexQamRfConfigRfLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 13),
    _ApexQamRfConfigRfLevelHighThreshold_Type()
)
apexQamRfConfigRfLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigRfLevelHighThreshold.setStatus("current")


class _ApexQamRfConfigMute_Type(Integer32):
    """Custom type apexQamRfConfigMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mute", 2),
          ("unmute", 1))
    )


_ApexQamRfConfigMute_Type.__name__ = "Integer32"
_ApexQamRfConfigMute_Object = MibTableColumn
apexQamRfConfigMute = _ApexQamRfConfigMute_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 14),
    _ApexQamRfConfigMute_Type()
)
apexQamRfConfigMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigMute.setStatus("current")


class _ApexQamRfConfigInterleaverDepth1_Type(Integer32):
    """Custom type apexQamRfConfigInterleaverDepth1 based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("i12-j17", 13),
          ("i128-j1", 5),
          ("i128-j2", 6),
          ("i128-j3", 7),
          ("i128-j4", 8),
          ("i128-j5", 9),
          ("i128-j6", 10),
          ("i128-j7", 11),
          ("i128-j8", 12),
          ("i16-j8", 3),
          ("i32-j4", 2),
          ("i64-j2", 1),
          ("i8-j16", 4))
    )


_ApexQamRfConfigInterleaverDepth1_Type.__name__ = "Integer32"
_ApexQamRfConfigInterleaverDepth1_Object = MibTableColumn
apexQamRfConfigInterleaverDepth1 = _ApexQamRfConfigInterleaverDepth1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 15),
    _ApexQamRfConfigInterleaverDepth1_Type()
)
apexQamRfConfigInterleaverDepth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigInterleaverDepth1.setStatus("current")


class _ApexQamRfConfigInterleaverDepth2_Type(Integer32):
    """Custom type apexQamRfConfigInterleaverDepth2 based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("i12-j17", 13),
          ("i128-j1", 5),
          ("i128-j2", 6),
          ("i128-j3", 7),
          ("i128-j4", 8),
          ("i128-j5", 9),
          ("i128-j6", 10),
          ("i128-j7", 11),
          ("i128-j8", 12),
          ("i16-j8", 3),
          ("i32-j4", 2),
          ("i64-j2", 1),
          ("i8-j16", 4))
    )


_ApexQamRfConfigInterleaverDepth2_Type.__name__ = "Integer32"
_ApexQamRfConfigInterleaverDepth2_Object = MibTableColumn
apexQamRfConfigInterleaverDepth2 = _ApexQamRfConfigInterleaverDepth2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 4, 1, 16),
    _ApexQamRfConfigInterleaverDepth2_Type()
)
apexQamRfConfigInterleaverDepth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfConfigInterleaverDepth2.setStatus("current")
_ApexQamChannelConfigTable_Object = MibTable
apexQamChannelConfigTable = _ApexQamChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 5)
)
if mibBuilder.loadTexts:
    apexQamChannelConfigTable.setStatus("current")
_ApexQamChannelConfigEntry_Object = MibTableRow
apexQamChannelConfigEntry = _ApexQamChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 5, 1)
)
apexQamChannelConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamChanConfigChannelNum"),
)
if mibBuilder.loadTexts:
    apexQamChannelConfigEntry.setStatus("current")


class _ApexQamChanConfigChannelNum_Type(Integer32):
    """Custom type apexQamChanConfigChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexQamChanConfigChannelNum_Type.__name__ = "Integer32"
_ApexQamChanConfigChannelNum_Object = MibTableColumn
apexQamChanConfigChannelNum = _ApexQamChanConfigChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 5, 1, 1),
    _ApexQamChanConfigChannelNum_Type()
)
apexQamChanConfigChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamChanConfigChannelNum.setStatus("current")


class _ApexQamChanConfigInterleaverSelect_Type(Integer32):
    """Custom type apexQamChanConfigInterleaverSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interleaverDepth1", 1),
          ("interleaverDepth2", 2))
    )


_ApexQamChanConfigInterleaverSelect_Type.__name__ = "Integer32"
_ApexQamChanConfigInterleaverSelect_Object = MibTableColumn
apexQamChanConfigInterleaverSelect = _ApexQamChanConfigInterleaverSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 5, 1, 2),
    _ApexQamChanConfigInterleaverSelect_Type()
)
apexQamChanConfigInterleaverSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamChanConfigInterleaverSelect.setStatus("current")


class _ApexQamChanConfigTestMode_Type(Integer32):
    """Custom type apexQamChanConfigTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              6,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cwtest", 2),
          ("mpegNull", 6),
          ("off", 0),
          ("prbs23", 5),
          ("prbs23m", 3),
          ("prbs60", 10),
          ("prbs63", 11),
          ("prbs65", 12),
          ("prbs68", 13),
          ("prbs71", 14),
          ("prbs73", 15),
          ("prbs79", 16),
          ("prbs81", 17),
          ("suppress", 9))
    )


_ApexQamChanConfigTestMode_Type.__name__ = "Integer32"
_ApexQamChanConfigTestMode_Object = MibTableColumn
apexQamChanConfigTestMode = _ApexQamChanConfigTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 5, 1, 3),
    _ApexQamChanConfigTestMode_Type()
)
apexQamChanConfigTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamChanConfigTestMode.setStatus("current")
_ApexQamRfRedundancyConfig_ObjectIdentity = ObjectIdentity
apexQamRfRedundancyConfig = _ApexQamRfRedundancyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6)
)
_ApexQamRfRedundancyConfigGeneral_ObjectIdentity = ObjectIdentity
apexQamRfRedundancyConfigGeneral = _ApexQamRfRedundancyConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1)
)
_ApexQamRfRedundConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexQamRfRedundConfigApplyChange_Object = MibScalar
apexQamRfRedundConfigApplyChange = _ApexQamRfRedundConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 1),
    _ApexQamRfRedundConfigApplyChange_Type()
)
apexQamRfRedundConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigApplyChange.setStatus("current")
_ApexQamRfRedundConfigEnable_Type = EnableDisableTYPE
_ApexQamRfRedundConfigEnable_Object = MibScalar
apexQamRfRedundConfigEnable = _ApexQamRfRedundConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 2),
    _ApexQamRfRedundConfigEnable_Type()
)
apexQamRfRedundConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigEnable.setStatus("current")


class _ApexQamRfRedundConfigRemConnection_Type(Integer32):
    """Custom type apexQamRfRedundConfigRemConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("common", 2),
          ("direct", 1),
          ("none", 0))
    )


_ApexQamRfRedundConfigRemConnection_Type.__name__ = "Integer32"
_ApexQamRfRedundConfigRemConnection_Object = MibScalar
apexQamRfRedundConfigRemConnection = _ApexQamRfRedundConfigRemConnection_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 3),
    _ApexQamRfRedundConfigRemConnection_Type()
)
apexQamRfRedundConfigRemConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigRemConnection.setStatus("current")


class _ApexQamRfRedundConfigApexId_Type(Integer32):
    """Custom type apexQamRfRedundConfigApexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApexQamRfRedundConfigApexId_Type.__name__ = "Integer32"
_ApexQamRfRedundConfigApexId_Object = MibScalar
apexQamRfRedundConfigApexId = _ApexQamRfRedundConfigApexId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 4),
    _ApexQamRfRedundConfigApexId_Type()
)
apexQamRfRedundConfigApexId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigApexId.setStatus("current")
_ApexQamRfRedundConfigRemCommonIpAddr_Type = IpAddress
_ApexQamRfRedundConfigRemCommonIpAddr_Object = MibScalar
apexQamRfRedundConfigRemCommonIpAddr = _ApexQamRfRedundConfigRemCommonIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 5),
    _ApexQamRfRedundConfigRemCommonIpAddr_Type()
)
apexQamRfRedundConfigRemCommonIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigRemCommonIpAddr.setStatus("current")
_ApexQamRfRedundConfigAutoSwitchBack_Type = EnableDisableTYPE
_ApexQamRfRedundConfigAutoSwitchBack_Object = MibScalar
apexQamRfRedundConfigAutoSwitchBack = _ApexQamRfRedundConfigAutoSwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 6),
    _ApexQamRfRedundConfigAutoSwitchBack_Type()
)
apexQamRfRedundConfigAutoSwitchBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigAutoSwitchBack.setStatus("current")
_ApexQamRfRedundConfigSuspendFailover_Type = EnableDisableTYPE
_ApexQamRfRedundConfigSuspendFailover_Object = MibScalar
apexQamRfRedundConfigSuspendFailover = _ApexQamRfRedundConfigSuspendFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 7),
    _ApexQamRfRedundConfigSuspendFailover_Type()
)
apexQamRfRedundConfigSuspendFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigSuspendFailover.setStatus("current")


class _ApexQamRfRedundConfigForceSwitch_Type(Integer32):
    """Custom type apexQamRfRedundConfigForceSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("forceFrom1", 1),
          ("forceFrom2", 2),
          ("forceFrom3", 3),
          ("forceFrom4", 4),
          ("forceFrom5", 5),
          ("forceFromBackup", 6),
          ("switchNotInProgress", 0))
    )


_ApexQamRfRedundConfigForceSwitch_Type.__name__ = "Integer32"
_ApexQamRfRedundConfigForceSwitch_Object = MibScalar
apexQamRfRedundConfigForceSwitch = _ApexQamRfRedundConfigForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 8),
    _ApexQamRfRedundConfigForceSwitch_Type()
)
apexQamRfRedundConfigForceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigForceSwitch.setStatus("current")


class _ApexQamRfRedundConfigRemDirectIpOctet1_Type(Integer32):
    """Custom type apexQamRfRedundConfigRemDirectIpOctet1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_ApexQamRfRedundConfigRemDirectIpOctet1_Type.__name__ = "Integer32"
_ApexQamRfRedundConfigRemDirectIpOctet1_Object = MibScalar
apexQamRfRedundConfigRemDirectIpOctet1 = _ApexQamRfRedundConfigRemDirectIpOctet1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 6, 1, 9),
    _ApexQamRfRedundConfigRemDirectIpOctet1_Type()
)
apexQamRfRedundConfigRemDirectIpOctet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamRfRedundConfigRemDirectIpOctet1.setStatus("current")
_ApexQamChannelConfigApplyTable_Object = MibTable
apexQamChannelConfigApplyTable = _ApexQamChannelConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 7)
)
if mibBuilder.loadTexts:
    apexQamChannelConfigApplyTable.setStatus("current")
_ApexQamChannelConfigApplyEntry_Object = MibTableRow
apexQamChannelConfigApplyEntry = _ApexQamChannelConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 7, 1)
)
apexQamChannelConfigApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamChannelConfigApplyChannelNum"),
)
if mibBuilder.loadTexts:
    apexQamChannelConfigApplyEntry.setStatus("current")


class _ApexQamChannelConfigApplyChannelNum_Type(Integer32):
    """Custom type apexQamChannelConfigApplyChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexQamChannelConfigApplyChannelNum_Type.__name__ = "Integer32"
_ApexQamChannelConfigApplyChannelNum_Object = MibTableColumn
apexQamChannelConfigApplyChannelNum = _ApexQamChannelConfigApplyChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 7, 1, 1),
    _ApexQamChannelConfigApplyChannelNum_Type()
)
apexQamChannelConfigApplyChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamChannelConfigApplyChannelNum.setStatus("current")
_ApexQamChannelConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexQamChannelConfigApplyChange_Object = MibTableColumn
apexQamChannelConfigApplyChange = _ApexQamChannelConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 1, 7, 1, 2),
    _ApexQamChannelConfigApplyChange_Type()
)
apexQamChannelConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQamChannelConfigApplyChange.setStatus("current")
_ApexQamStatus_ObjectIdentity = ObjectIdentity
apexQamStatus = _ApexQamStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2)
)
_ApexQamStatusGeneral_ObjectIdentity = ObjectIdentity
apexQamStatusGeneral = _ApexQamStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 1)
)


class _ApexQamStatusTransmissionMode_Type(Integer32):
    """Custom type apexQamStatusTransmissionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA-DVB", 2),
          ("annexB-ATSC-DCII", 1),
          ("annexC-Asia-Pacific", 3))
    )


_ApexQamStatusTransmissionMode_Type.__name__ = "Integer32"
_ApexQamStatusTransmissionMode_Object = MibScalar
apexQamStatusTransmissionMode = _ApexQamStatusTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 1, 1),
    _ApexQamStatusTransmissionMode_Type()
)
apexQamStatusTransmissionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamStatusTransmissionMode.setStatus("current")
_ApexQamModuleInstalledCount_Type = Integer32
_ApexQamModuleInstalledCount_Object = MibScalar
apexQamModuleInstalledCount = _ApexQamModuleInstalledCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 1, 2),
    _ApexQamModuleInstalledCount_Type()
)
apexQamModuleInstalledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleInstalledCount.setStatus("current")
_ApexFanModuleInstalledCount_Type = Integer32
_ApexFanModuleInstalledCount_Object = MibScalar
apexFanModuleInstalledCount = _ApexFanModuleInstalledCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 1, 3),
    _ApexFanModuleInstalledCount_Type()
)
apexFanModuleInstalledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexFanModuleInstalledCount.setStatus("current")
_ApexQamChannelsActiveCount_Type = Integer32
_ApexQamChannelsActiveCount_Object = MibScalar
apexQamChannelsActiveCount = _ApexQamChannelsActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 1, 4),
    _ApexQamChannelsActiveCount_Type()
)
apexQamChannelsActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelsActiveCount.setStatus("current")
_ApexQamModuleStatusTable_Object = MibTable
apexQamModuleStatusTable = _ApexQamModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2)
)
if mibBuilder.loadTexts:
    apexQamModuleStatusTable.setStatus("current")
_ApexQamModuleStatusEntry_Object = MibTableRow
apexQamModuleStatusEntry = _ApexQamModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1)
)
apexQamModuleStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamModuleStatQamModuleNum"),
)
if mibBuilder.loadTexts:
    apexQamModuleStatusEntry.setStatus("current")


class _ApexQamModuleStatQamModuleNum_Type(Integer32):
    """Custom type apexQamModuleStatQamModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ApexQamModuleStatQamModuleNum_Type.__name__ = "Integer32"
_ApexQamModuleStatQamModuleNum_Object = MibTableColumn
apexQamModuleStatQamModuleNum = _ApexQamModuleStatQamModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 1),
    _ApexQamModuleStatQamModuleNum_Type()
)
apexQamModuleStatQamModuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamModuleStatQamModuleNum.setStatus("current")


class _ApexQamModuleStatInstalled_Type(Integer32):
    """Custom type apexQamModuleStatInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fanModule", 4),
          ("notApplicable", 0),
          ("notInstalled", 1),
          ("qam2x4Channel", 2),
          ("qam2x8Channel", 3),
          ("qam4x4Channel", 8),
          ("qamDiscovery", 7),
          ("removed", 6),
          ("unsupported", 5))
    )


_ApexQamModuleStatInstalled_Type.__name__ = "Integer32"
_ApexQamModuleStatInstalled_Object = MibTableColumn
apexQamModuleStatInstalled = _ApexQamModuleStatInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 2),
    _ApexQamModuleStatInstalled_Type()
)
apexQamModuleStatInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatInstalled.setStatus("current")
_ApexQamModuleStatFanSpeed_Type = Unsigned32
_ApexQamModuleStatFanSpeed_Object = MibTableColumn
apexQamModuleStatFanSpeed = _ApexQamModuleStatFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 3),
    _ApexQamModuleStatFanSpeed_Type()
)
apexQamModuleStatFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatFanSpeed.setStatus("current")


class _ApexQamModuleStatFanFault_Type(Integer32):
    """Custom type apexQamModuleStatFanFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamModuleStatFanFault_Type.__name__ = "Integer32"
_ApexQamModuleStatFanFault_Object = MibTableColumn
apexQamModuleStatFanFault = _ApexQamModuleStatFanFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 4),
    _ApexQamModuleStatFanFault_Type()
)
apexQamModuleStatFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatFanFault.setStatus("current")
_ApexQamModuleStatTemperature_Type = Integer32
_ApexQamModuleStatTemperature_Object = MibTableColumn
apexQamModuleStatTemperature = _ApexQamModuleStatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 5),
    _ApexQamModuleStatTemperature_Type()
)
apexQamModuleStatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatTemperature.setStatus("current")


class _ApexQamModuleStatTemperatureFault_Type(Integer32):
    """Custom type apexQamModuleStatTemperatureFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexQamModuleStatTemperatureFault_Type.__name__ = "Integer32"
_ApexQamModuleStatTemperatureFault_Object = MibTableColumn
apexQamModuleStatTemperatureFault = _ApexQamModuleStatTemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 6),
    _ApexQamModuleStatTemperatureFault_Type()
)
apexQamModuleStatTemperatureFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatTemperatureFault.setStatus("current")


class _ApexQamModuleStatError_Type(Integer32):
    """Custom type apexQamModuleStatError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("codeDownload", 11),
          ("codeDownloadError", 12),
          ("codeVersions", 10),
          ("commLost", 9),
          ("dc3-3VoltError", 8),
          ("dc5VoltError", 7),
          ("notApplicable", 0),
          ("notInstalled", 4),
          ("offline", 6),
          ("ok", 1),
          ("powerFault", 5),
          ("removed", 2),
          ("unsupported", 3))
    )


_ApexQamModuleStatError_Type.__name__ = "Integer32"
_ApexQamModuleStatError_Object = MibTableColumn
apexQamModuleStatError = _ApexQamModuleStatError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 7),
    _ApexQamModuleStatError_Type()
)
apexQamModuleStatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatError.setStatus("current")


class _ApexQamModuleStatFaultCondition_Type(Integer32):
    """Custom type apexQamModuleStatFaultCondition based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexQamModuleStatFaultCondition_Type.__name__ = "Integer32"
_ApexQamModuleStatFaultCondition_Object = MibTableColumn
apexQamModuleStatFaultCondition = _ApexQamModuleStatFaultCondition_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 8),
    _ApexQamModuleStatFaultCondition_Type()
)
apexQamModuleStatFaultCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatFaultCondition.setStatus("current")


class _ApexQamModuleStatFaultSumm_Type(Integer32):
    """Custom type apexQamModuleStatFaultSumm based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexQamModuleStatFaultSumm_Type.__name__ = "Integer32"
_ApexQamModuleStatFaultSumm_Object = MibTableColumn
apexQamModuleStatFaultSumm = _ApexQamModuleStatFaultSumm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 9),
    _ApexQamModuleStatFaultSumm_Type()
)
apexQamModuleStatFaultSumm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatFaultSumm.setStatus("current")


class _ApexQamModuleStatPowerFault_Type(Integer32):
    """Custom type apexQamModuleStatPowerFault based on Integer32"""
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
        *(("lowVoltageMainboard", 2),
          ("lowVoltageQamModule", 3),
          ("notApplicable", 0),
          ("ok", 1),
          ("overCurrent", 4))
    )


_ApexQamModuleStatPowerFault_Type.__name__ = "Integer32"
_ApexQamModuleStatPowerFault_Object = MibTableColumn
apexQamModuleStatPowerFault = _ApexQamModuleStatPowerFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 10),
    _ApexQamModuleStatPowerFault_Type()
)
apexQamModuleStatPowerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatPowerFault.setStatus("current")
_ApexQamModuleStatBoardTemperature_Type = Integer32
_ApexQamModuleStatBoardTemperature_Object = MibTableColumn
apexQamModuleStatBoardTemperature = _ApexQamModuleStatBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 11),
    _ApexQamModuleStatBoardTemperature_Type()
)
apexQamModuleStatBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatBoardTemperature.setStatus("current")


class _ApexQamModuleStatBoardTemperatureFault_Type(Integer32):
    """Custom type apexQamModuleStatBoardTemperatureFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexQamModuleStatBoardTemperatureFault_Type.__name__ = "Integer32"
_ApexQamModuleStatBoardTemperatureFault_Object = MibTableColumn
apexQamModuleStatBoardTemperatureFault = _ApexQamModuleStatBoardTemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 12),
    _ApexQamModuleStatBoardTemperatureFault_Type()
)
apexQamModuleStatBoardTemperatureFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatBoardTemperatureFault.setStatus("current")


class _ApexQamModuleStat5VdcSupply_Type(Integer32):
    """Custom type apexQamModuleStat5VdcSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApexQamModuleStat5VdcSupply_Type.__name__ = "Integer32"
_ApexQamModuleStat5VdcSupply_Object = MibTableColumn
apexQamModuleStat5VdcSupply = _ApexQamModuleStat5VdcSupply_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 13),
    _ApexQamModuleStat5VdcSupply_Type()
)
apexQamModuleStat5VdcSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStat5VdcSupply.setStatus("current")


class _ApexQamModuleStat5VdcFault_Type(Integer32):
    """Custom type apexQamModuleStat5VdcFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamModuleStat5VdcFault_Type.__name__ = "Integer32"
_ApexQamModuleStat5VdcFault_Object = MibTableColumn
apexQamModuleStat5VdcFault = _ApexQamModuleStat5VdcFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 14),
    _ApexQamModuleStat5VdcFault_Type()
)
apexQamModuleStat5VdcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStat5VdcFault.setStatus("current")


class _ApexQamModuleStat3dot3VdcSupply_Type(Integer32):
    """Custom type apexQamModuleStat3dot3VdcSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApexQamModuleStat3dot3VdcSupply_Type.__name__ = "Integer32"
_ApexQamModuleStat3dot3VdcSupply_Object = MibTableColumn
apexQamModuleStat3dot3VdcSupply = _ApexQamModuleStat3dot3VdcSupply_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 15),
    _ApexQamModuleStat3dot3VdcSupply_Type()
)
apexQamModuleStat3dot3VdcSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStat3dot3VdcSupply.setStatus("current")


class _ApexQamModuleStat3dot3VdcFault_Type(Integer32):
    """Custom type apexQamModuleStat3dot3VdcFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamModuleStat3dot3VdcFault_Type.__name__ = "Integer32"
_ApexQamModuleStat3dot3VdcFault_Object = MibTableColumn
apexQamModuleStat3dot3VdcFault = _ApexQamModuleStat3dot3VdcFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 16),
    _ApexQamModuleStat3dot3VdcFault_Type()
)
apexQamModuleStat3dot3VdcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStat3dot3VdcFault.setStatus("current")


class _ApexQamModuleStatCommError_Type(Integer32):
    """Custom type apexQamModuleStatCommError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 2),
          ("inComm", 1),
          ("notApplicable", 0))
    )


_ApexQamModuleStatCommError_Type.__name__ = "Integer32"
_ApexQamModuleStatCommError_Object = MibTableColumn
apexQamModuleStatCommError = _ApexQamModuleStatCommError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 17),
    _ApexQamModuleStatCommError_Type()
)
apexQamModuleStatCommError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatCommError.setStatus("current")


class _ApexQamModuleStatCodeInitError_Type(Integer32):
    """Custom type apexQamModuleStatCodeInitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamModuleStatCodeInitError_Type.__name__ = "Integer32"
_ApexQamModuleStatCodeInitError_Object = MibTableColumn
apexQamModuleStatCodeInitError = _ApexQamModuleStatCodeInitError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 2, 1, 18),
    _ApexQamModuleStatCodeInitError_Type()
)
apexQamModuleStatCodeInitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleStatCodeInitError.setStatus("current")
_ApexQamModuleSerialNumTable_Object = MibTable
apexQamModuleSerialNumTable = _ApexQamModuleSerialNumTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 3)
)
if mibBuilder.loadTexts:
    apexQamModuleSerialNumTable.setStatus("current")
_ApexQamModuleSerialNumEntry_Object = MibTableRow
apexQamModuleSerialNumEntry = _ApexQamModuleSerialNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 3, 1)
)
apexQamModuleSerialNumEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamModuleSerialNumQamModuleNum"),
)
if mibBuilder.loadTexts:
    apexQamModuleSerialNumEntry.setStatus("current")


class _ApexQamModuleSerialNumQamModuleNum_Type(Integer32):
    """Custom type apexQamModuleSerialNumQamModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ApexQamModuleSerialNumQamModuleNum_Type.__name__ = "Integer32"
_ApexQamModuleSerialNumQamModuleNum_Object = MibTableColumn
apexQamModuleSerialNumQamModuleNum = _ApexQamModuleSerialNumQamModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 3, 1, 1),
    _ApexQamModuleSerialNumQamModuleNum_Type()
)
apexQamModuleSerialNumQamModuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamModuleSerialNumQamModuleNum.setStatus("current")


class _ApexQamModuleSerialNumber_Type(DisplayString):
    """Custom type apexQamModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ApexQamModuleSerialNumber_Type.__name__ = "DisplayString"
_ApexQamModuleSerialNumber_Object = MibTableColumn
apexQamModuleSerialNumber = _ApexQamModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 3, 1, 2),
    _ApexQamModuleSerialNumber_Type()
)
apexQamModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamModuleSerialNumber.setStatus("current")
_ApexQamQrmRevisionTable_Object = MibTable
apexQamQrmRevisionTable = _ApexQamQrmRevisionTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4)
)
if mibBuilder.loadTexts:
    apexQamQrmRevisionTable.setStatus("current")
_ApexQamQrmRevisionEntry_Object = MibTableRow
apexQamQrmRevisionEntry = _ApexQamQrmRevisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1)
)
apexQamQrmRevisionEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamQrmRevRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamQrmRevisionEntry.setStatus("current")


class _ApexQamQrmRevRfPortNum_Type(Integer32):
    """Custom type apexQamQrmRevRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexQamQrmRevRfPortNum_Type.__name__ = "Integer32"
_ApexQamQrmRevRfPortNum_Object = MibTableColumn
apexQamQrmRevRfPortNum = _ApexQamQrmRevRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 1),
    _ApexQamQrmRevRfPortNum_Type()
)
apexQamQrmRevRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamQrmRevRfPortNum.setStatus("current")


class _ApexQamQrmRevBoardId_Type(DisplayString):
    """Custom type apexQamQrmRevBoardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevBoardId_Type.__name__ = "DisplayString"
_ApexQamQrmRevBoardId_Object = MibTableColumn
apexQamQrmRevBoardId = _ApexQamQrmRevBoardId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 2),
    _ApexQamQrmRevBoardId_Type()
)
apexQamQrmRevBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevBoardId.setStatus("current")


class _ApexQamQrmRevAppFw_Type(DisplayString):
    """Custom type apexQamQrmRevAppFw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevAppFw_Type.__name__ = "DisplayString"
_ApexQamQrmRevAppFw_Object = MibTableColumn
apexQamQrmRevAppFw = _ApexQamQrmRevAppFw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 3),
    _ApexQamQrmRevAppFw_Type()
)
apexQamQrmRevAppFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevAppFw.setStatus("current")


class _ApexQamQrmRevBootLoaderFw_Type(DisplayString):
    """Custom type apexQamQrmRevBootLoaderFw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevBootLoaderFw_Type.__name__ = "DisplayString"
_ApexQamQrmRevBootLoaderFw_Object = MibTableColumn
apexQamQrmRevBootLoaderFw = _ApexQamQrmRevBootLoaderFw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 4),
    _ApexQamQrmRevBootLoaderFw_Type()
)
apexQamQrmRevBootLoaderFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevBootLoaderFw.setStatus("current")


class _ApexQamQrmRevFpga_Type(DisplayString):
    """Custom type apexQamQrmRevFpga based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevFpga_Type.__name__ = "DisplayString"
_ApexQamQrmRevFpga_Object = MibTableColumn
apexQamQrmRevFpga = _ApexQamQrmRevFpga_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 5),
    _ApexQamQrmRevFpga_Type()
)
apexQamQrmRevFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevFpga.setStatus("current")


class _ApexQamQrmRevHw_Type(DisplayString):
    """Custom type apexQamQrmRevHw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevHw_Type.__name__ = "DisplayString"
_ApexQamQrmRevHw_Object = MibTableColumn
apexQamQrmRevHw = _ApexQamQrmRevHw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 6),
    _ApexQamQrmRevHw_Type()
)
apexQamQrmRevHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevHw.setStatus("current")


class _ApexQamQrmRevSerialNumber_Type(DisplayString):
    """Custom type apexQamQrmRevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ApexQamQrmRevSerialNumber_Type.__name__ = "DisplayString"
_ApexQamQrmRevSerialNumber_Object = MibTableColumn
apexQamQrmRevSerialNumber = _ApexQamQrmRevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 7),
    _ApexQamQrmRevSerialNumber_Type()
)
apexQamQrmRevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevSerialNumber.setStatus("current")


class _ApexQamQrmRevFpga2_Type(DisplayString):
    """Custom type apexQamQrmRevFpga2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQamQrmRevFpga2_Type.__name__ = "DisplayString"
_ApexQamQrmRevFpga2_Object = MibTableColumn
apexQamQrmRevFpga2 = _ApexQamQrmRevFpga2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 4, 1, 8),
    _ApexQamQrmRevFpga2_Type()
)
apexQamQrmRevFpga2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevFpga2.setStatus("current")
_ApexQamRfPortStatusTable_Object = MibTable
apexQamRfPortStatusTable = _ApexQamRfPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5)
)
if mibBuilder.loadTexts:
    apexQamRfPortStatusTable.setStatus("current")
_ApexQamRfPortStatusEntry_Object = MibTableRow
apexQamRfPortStatusEntry = _ApexQamRfPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1)
)
apexQamRfPortStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamRfPortStatRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamRfPortStatusEntry.setStatus("current")


class _ApexQamRfPortStatRfPortNum_Type(Integer32):
    """Custom type apexQamRfPortStatRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexQamRfPortStatRfPortNum_Type.__name__ = "Integer32"
_ApexQamRfPortStatRfPortNum_Object = MibTableColumn
apexQamRfPortStatRfPortNum = _ApexQamRfPortStatRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 1),
    _ApexQamRfPortStatRfPortNum_Type()
)
apexQamRfPortStatRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamRfPortStatRfPortNum.setStatus("current")
_ApexQamRfPortStatInfoRate_Type = Unsigned32
_ApexQamRfPortStatInfoRate_Object = MibTableColumn
apexQamRfPortStatInfoRate = _ApexQamRfPortStatInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 2),
    _ApexQamRfPortStatInfoRate_Type()
)
apexQamRfPortStatInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatInfoRate.setStatus("current")


class _ApexQamRfPortStatNumChannelsActive_Type(Integer32):
    """Custom type apexQamRfPortStatNumChannelsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ApexQamRfPortStatNumChannelsActive_Type.__name__ = "Integer32"
_ApexQamRfPortStatNumChannelsActive_Object = MibTableColumn
apexQamRfPortStatNumChannelsActive = _ApexQamRfPortStatNumChannelsActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 3),
    _ApexQamRfPortStatNumChannelsActive_Type()
)
apexQamRfPortStatNumChannelsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatNumChannelsActive.setStatus("current")


class _ApexQamRfPortStatOutputLevel_Type(Integer32):
    """Custom type apexQamRfPortStatOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_ApexQamRfPortStatOutputLevel_Type.__name__ = "Integer32"
_ApexQamRfPortStatOutputLevel_Object = MibTableColumn
apexQamRfPortStatOutputLevel = _ApexQamRfPortStatOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 4),
    _ApexQamRfPortStatOutputLevel_Type()
)
apexQamRfPortStatOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatOutputLevel.setStatus("current")


class _ApexQamRfPortStatOutputLevelFault_Type(Integer32):
    """Custom type apexQamRfPortStatOutputLevelFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamRfPortStatOutputLevelFault_Type.__name__ = "Integer32"
_ApexQamRfPortStatOutputLevelFault_Object = MibTableColumn
apexQamRfPortStatOutputLevelFault = _ApexQamRfPortStatOutputLevelFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 5),
    _ApexQamRfPortStatOutputLevelFault_Type()
)
apexQamRfPortStatOutputLevelFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatOutputLevelFault.setStatus("current")
_ApexQamRfPortStatTemperature_Type = Integer32
_ApexQamRfPortStatTemperature_Object = MibTableColumn
apexQamRfPortStatTemperature = _ApexQamRfPortStatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 6),
    _ApexQamRfPortStatTemperature_Type()
)
apexQamRfPortStatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatTemperature.setStatus("current")


class _ApexQamRfPortStatTemperatureFault_Type(Integer32):
    """Custom type apexQamRfPortStatTemperatureFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ok", 1),
          ("overTemp", 2))
    )


_ApexQamRfPortStatTemperatureFault_Type.__name__ = "Integer32"
_ApexQamRfPortStatTemperatureFault_Object = MibTableColumn
apexQamRfPortStatTemperatureFault = _ApexQamRfPortStatTemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 7),
    _ApexQamRfPortStatTemperatureFault_Type()
)
apexQamRfPortStatTemperatureFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatTemperatureFault.setStatus("current")


class _ApexQamRfPortStat5VdcSupply_Type(Integer32):
    """Custom type apexQamRfPortStat5VdcSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApexQamRfPortStat5VdcSupply_Type.__name__ = "Integer32"
_ApexQamRfPortStat5VdcSupply_Object = MibTableColumn
apexQamRfPortStat5VdcSupply = _ApexQamRfPortStat5VdcSupply_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 8),
    _ApexQamRfPortStat5VdcSupply_Type()
)
apexQamRfPortStat5VdcSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStat5VdcSupply.setStatus("current")


class _ApexQamRfPortStat5VdcFault_Type(Integer32):
    """Custom type apexQamRfPortStat5VdcFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamRfPortStat5VdcFault_Type.__name__ = "Integer32"
_ApexQamRfPortStat5VdcFault_Object = MibTableColumn
apexQamRfPortStat5VdcFault = _ApexQamRfPortStat5VdcFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 9),
    _ApexQamRfPortStat5VdcFault_Type()
)
apexQamRfPortStat5VdcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStat5VdcFault.setStatus("current")


class _ApexQamRfPortStat3dot3VdcSupply_Type(Integer32):
    """Custom type apexQamRfPortStat3dot3VdcSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApexQamRfPortStat3dot3VdcSupply_Type.__name__ = "Integer32"
_ApexQamRfPortStat3dot3VdcSupply_Object = MibTableColumn
apexQamRfPortStat3dot3VdcSupply = _ApexQamRfPortStat3dot3VdcSupply_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 10),
    _ApexQamRfPortStat3dot3VdcSupply_Type()
)
apexQamRfPortStat3dot3VdcSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStat3dot3VdcSupply.setStatus("current")


class _ApexQamRfPortStat3dot3VdcFault_Type(Integer32):
    """Custom type apexQamRfPortStat3dot3VdcFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamRfPortStat3dot3VdcFault_Type.__name__ = "Integer32"
_ApexQamRfPortStat3dot3VdcFault_Object = MibTableColumn
apexQamRfPortStat3dot3VdcFault = _ApexQamRfPortStat3dot3VdcFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 11),
    _ApexQamRfPortStat3dot3VdcFault_Type()
)
apexQamRfPortStat3dot3VdcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStat3dot3VdcFault.setStatus("current")


class _ApexQamRfPortStatFreqPllLock_Type(Integer32):
    """Custom type apexQamRfPortStatFreqPllLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("notApplicable", 0),
          ("notLocked", 2))
    )


_ApexQamRfPortStatFreqPllLock_Type.__name__ = "Integer32"
_ApexQamRfPortStatFreqPllLock_Object = MibTableColumn
apexQamRfPortStatFreqPllLock = _ApexQamRfPortStatFreqPllLock_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 12),
    _ApexQamRfPortStatFreqPllLock_Type()
)
apexQamRfPortStatFreqPllLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatFreqPllLock.setStatus("current")


class _ApexQamRfPortStatRefClockPresent_Type(Integer32):
    """Custom type apexQamRfPortStatRefClockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notPresent", 2),
          ("present", 1))
    )


_ApexQamRfPortStatRefClockPresent_Type.__name__ = "Integer32"
_ApexQamRfPortStatRefClockPresent_Object = MibTableColumn
apexQamRfPortStatRefClockPresent = _ApexQamRfPortStatRefClockPresent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 13),
    _ApexQamRfPortStatRefClockPresent_Type()
)
apexQamRfPortStatRefClockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatRefClockPresent.setStatus("current")


class _ApexQamRfPortStatRefClockLock_Type(Integer32):
    """Custom type apexQamRfPortStatRefClockLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("notApplicable", 0),
          ("notLocked", 2))
    )


_ApexQamRfPortStatRefClockLock_Type.__name__ = "Integer32"
_ApexQamRfPortStatRefClockLock_Object = MibTableColumn
apexQamRfPortStatRefClockLock = _ApexQamRfPortStatRefClockLock_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 14),
    _ApexQamRfPortStatRefClockLock_Type()
)
apexQamRfPortStatRefClockLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatRefClockLock.setStatus("current")


class _ApexQamRfPortStatDataClockPresent_Type(Integer32):
    """Custom type apexQamRfPortStatDataClockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notPresent", 2),
          ("present", 1))
    )


_ApexQamRfPortStatDataClockPresent_Type.__name__ = "Integer32"
_ApexQamRfPortStatDataClockPresent_Object = MibTableColumn
apexQamRfPortStatDataClockPresent = _ApexQamRfPortStatDataClockPresent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 15),
    _ApexQamRfPortStatDataClockPresent_Type()
)
apexQamRfPortStatDataClockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatDataClockPresent.setStatus("current")


class _ApexQamRfPortStatDataSyncFault_Type(Integer32):
    """Custom type apexQamRfPortStatDataSyncFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("notApplicable", 0),
          ("syncLost", 2))
    )


_ApexQamRfPortStatDataSyncFault_Type.__name__ = "Integer32"
_ApexQamRfPortStatDataSyncFault_Object = MibTableColumn
apexQamRfPortStatDataSyncFault = _ApexQamRfPortStatDataSyncFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 16),
    _ApexQamRfPortStatDataSyncFault_Type()
)
apexQamRfPortStatDataSyncFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatDataSyncFault.setStatus("current")


class _ApexQamRfPortStatCommError_Type(Integer32):
    """Custom type apexQamRfPortStatCommError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 2),
          ("inComm", 1),
          ("notApplicable", 0))
    )


_ApexQamRfPortStatCommError_Type.__name__ = "Integer32"
_ApexQamRfPortStatCommError_Object = MibTableColumn
apexQamRfPortStatCommError = _ApexQamRfPortStatCommError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 17),
    _ApexQamRfPortStatCommError_Type()
)
apexQamRfPortStatCommError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatCommError.setStatus("current")


class _ApexQamRfPortStatError_Type(Integer32):
    """Custom type apexQamRfPortStatError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("codeDownload", 14),
          ("codeDownloadError", 15),
          ("codeVersions", 13),
          ("commLost", 10),
          ("configFailed", 12),
          ("dataClkNotPresent", 8),
          ("dataSyncLost", 9),
          ("dc3-3VoltError", 4),
          ("dc5VoltError", 3),
          ("extClkNotLocked", 7),
          ("extClkNotPresent", 6),
          ("freqPllNotLocked", 5),
          ("notApplicable", 0),
          ("ok", 1),
          ("outputRfLevel", 2),
          ("unsupportedQrm", 11))
    )


_ApexQamRfPortStatError_Type.__name__ = "Integer32"
_ApexQamRfPortStatError_Object = MibTableColumn
apexQamRfPortStatError = _ApexQamRfPortStatError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 18),
    _ApexQamRfPortStatError_Type()
)
apexQamRfPortStatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatError.setStatus("current")


class _ApexQamRfPortStatFaultCondition_Type(Integer32):
    """Custom type apexQamRfPortStatFaultCondition based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexQamRfPortStatFaultCondition_Type.__name__ = "Integer32"
_ApexQamRfPortStatFaultCondition_Object = MibTableColumn
apexQamRfPortStatFaultCondition = _ApexQamRfPortStatFaultCondition_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 19),
    _ApexQamRfPortStatFaultCondition_Type()
)
apexQamRfPortStatFaultCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatFaultCondition.setStatus("current")


class _ApexQamRfPortStatChanFaultSumm_Type(Integer32):
    """Custom type apexQamRfPortStatChanFaultSumm based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexQamRfPortStatChanFaultSumm_Type.__name__ = "Integer32"
_ApexQamRfPortStatChanFaultSumm_Object = MibTableColumn
apexQamRfPortStatChanFaultSumm = _ApexQamRfPortStatChanFaultSumm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 20),
    _ApexQamRfPortStatChanFaultSumm_Type()
)
apexQamRfPortStatChanFaultSumm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatChanFaultSumm.setStatus("current")


class _ApexQamRfPortStatCodeInitError_Type(Integer32):
    """Custom type apexQamRfPortStatCodeInitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("calDataError", 3),
          ("fpgaInitError", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamRfPortStatCodeInitError_Type.__name__ = "Integer32"
_ApexQamRfPortStatCodeInitError_Object = MibTableColumn
apexQamRfPortStatCodeInitError = _ApexQamRfPortStatCodeInitError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 5, 1, 21),
    _ApexQamRfPortStatCodeInitError_Type()
)
apexQamRfPortStatCodeInitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortStatCodeInitError.setStatus("current")
_ApexQamChannelStatusTable_Object = MibTable
apexQamChannelStatusTable = _ApexQamChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6)
)
if mibBuilder.loadTexts:
    apexQamChannelStatusTable.setStatus("current")
_ApexQamChannelStatusEntry_Object = MibTableRow
apexQamChannelStatusEntry = _ApexQamChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1)
)
apexQamChannelStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamChanStatChannelNum"),
)
if mibBuilder.loadTexts:
    apexQamChannelStatusEntry.setStatus("current")


class _ApexQamChanStatChannelNum_Type(Integer32):
    """Custom type apexQamChanStatChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexQamChanStatChannelNum_Type.__name__ = "Integer32"
_ApexQamChanStatChannelNum_Object = MibTableColumn
apexQamChanStatChannelNum = _ApexQamChanStatChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 1),
    _ApexQamChanStatChannelNum_Type()
)
apexQamChanStatChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamChanStatChannelNum.setStatus("current")
_ApexQamChanStatActive_Type = ActiveTYPE
_ApexQamChanStatActive_Object = MibTableColumn
apexQamChanStatActive = _ApexQamChanStatActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 2),
    _ApexQamChanStatActive_Type()
)
apexQamChanStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatActive.setStatus("current")
_ApexQamChanStatRfFreq_Type = Integer32
_ApexQamChanStatRfFreq_Object = MibTableColumn
apexQamChanStatRfFreq = _ApexQamChanStatRfFreq_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 3),
    _ApexQamChanStatRfFreq_Type()
)
apexQamChanStatRfFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatRfFreq.setStatus("current")
_ApexQamChanStatEiaChanNum_Type = Integer32
_ApexQamChanStatEiaChanNum_Object = MibTableColumn
apexQamChanStatEiaChanNum = _ApexQamChanStatEiaChanNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 4),
    _ApexQamChanStatEiaChanNum_Type()
)
apexQamChanStatEiaChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatEiaChanNum.setStatus("current")


class _ApexQamChanStatDataPresent_Type(Integer32):
    """Custom type apexQamChanStatDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2),
          ("notApplicable", 0))
    )


_ApexQamChanStatDataPresent_Type.__name__ = "Integer32"
_ApexQamChanStatDataPresent_Object = MibTableColumn
apexQamChanStatDataPresent = _ApexQamChanStatDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 5),
    _ApexQamChanStatDataPresent_Type()
)
apexQamChanStatDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatDataPresent.setStatus("current")


class _ApexQamChanStatError_Type(Integer32):
    """Custom type apexQamChanStatError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noData", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexQamChanStatError_Type.__name__ = "Integer32"
_ApexQamChanStatError_Object = MibTableColumn
apexQamChanStatError = _ApexQamChanStatError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 6),
    _ApexQamChanStatError_Type()
)
apexQamChanStatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatError.setStatus("current")


class _ApexQamChanStatFaultCondition_Type(Integer32):
    """Custom type apexQamChanStatFaultCondition based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexQamChanStatFaultCondition_Type.__name__ = "Integer32"
_ApexQamChanStatFaultCondition_Object = MibTableColumn
apexQamChanStatFaultCondition = _ApexQamChanStatFaultCondition_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 6, 1, 7),
    _ApexQamChanStatFaultCondition_Type()
)
apexQamChanStatFaultCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChanStatFaultCondition.setStatus("current")
_ApexQamRfRedundancyStatus_ObjectIdentity = ObjectIdentity
apexQamRfRedundancyStatus = _ApexQamRfRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7)
)
_ApexQamRfRedundancyStatusGeneral_ObjectIdentity = ObjectIdentity
apexQamRfRedundancyStatusGeneral = _ApexQamRfRedundancyStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1)
)


class _ApexQamRfRedundStatusBackupPort_Type(Integer32):
    """Custom type apexQamRfRedundStatusBackupPort based on Integer32"""
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
        *(("active", 2),
          ("disabled", 0),
          ("failed", 3),
          ("removed", 4),
          ("standby", 1))
    )


_ApexQamRfRedundStatusBackupPort_Type.__name__ = "Integer32"
_ApexQamRfRedundStatusBackupPort_Object = MibScalar
apexQamRfRedundStatusBackupPort = _ApexQamRfRedundStatusBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 1),
    _ApexQamRfRedundStatusBackupPort_Type()
)
apexQamRfRedundStatusBackupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusBackupPort.setStatus("current")
_ApexQamRfRedundStatusFailedPort_Type = Integer32
_ApexQamRfRedundStatusFailedPort_Object = MibScalar
apexQamRfRedundStatusFailedPort = _ApexQamRfRedundStatusFailedPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 2),
    _ApexQamRfRedundStatusFailedPort_Type()
)
apexQamRfRedundStatusFailedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusFailedPort.setStatus("current")


class _ApexQamRfRedundStatusMismatch_Type(Integer32):
    """Custom type apexQamRfRedundStatusMismatch based on Integer32"""
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
        *(("any4x4", 4),
          ("backup2x4", 2),
          ("noMismatch", 1),
          ("notApplicable", 0),
          ("primary2x4", 3))
    )


_ApexQamRfRedundStatusMismatch_Type.__name__ = "Integer32"
_ApexQamRfRedundStatusMismatch_Object = MibScalar
apexQamRfRedundStatusMismatch = _ApexQamRfRedundStatusMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 3),
    _ApexQamRfRedundStatusMismatch_Type()
)
apexQamRfRedundStatusMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusMismatch.setStatus("current")
_ApexQamRfRedundStatusUdpPort_Type = Integer32
_ApexQamRfRedundStatusUdpPort_Object = MibScalar
apexQamRfRedundStatusUdpPort = _ApexQamRfRedundStatusUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 4),
    _ApexQamRfRedundStatusUdpPort_Type()
)
apexQamRfRedundStatusUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusUdpPort.setStatus("current")


class _ApexQamRfRedundStatusRemConnection_Type(Integer32):
    """Custom type apexQamRfRedundStatusRemConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connectionLost", 3),
          ("notApplicable", 0),
          ("notConnected", 1))
    )


_ApexQamRfRedundStatusRemConnection_Type.__name__ = "Integer32"
_ApexQamRfRedundStatusRemConnection_Object = MibScalar
apexQamRfRedundStatusRemConnection = _ApexQamRfRedundStatusRemConnection_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 5),
    _ApexQamRfRedundStatusRemConnection_Type()
)
apexQamRfRedundStatusRemConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusRemConnection.setStatus("current")
_ApexQamRfRedundStatusRemError_Type = Integer32
_ApexQamRfRedundStatusRemError_Object = MibScalar
apexQamRfRedundStatusRemError = _ApexQamRfRedundStatusRemError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 6),
    _ApexQamRfRedundStatusRemError_Type()
)
apexQamRfRedundStatusRemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusRemError.setStatus("current")
_ApexQamRfRedundStatusRemSwitch_Type = Integer32
_ApexQamRfRedundStatusRemSwitch_Object = MibScalar
apexQamRfRedundStatusRemSwitch = _ApexQamRfRedundStatusRemSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 7),
    _ApexQamRfRedundStatusRemSwitch_Type()
)
apexQamRfRedundStatusRemSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusRemSwitch.setStatus("current")


class _ApexQamRfRedundStatusInvalidApplyText_Type(DisplayString):
    """Custom type apexQamRfRedundStatusInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexQamRfRedundStatusInvalidApplyText_Type.__name__ = "DisplayString"
_ApexQamRfRedundStatusInvalidApplyText_Object = MibScalar
apexQamRfRedundStatusInvalidApplyText = _ApexQamRfRedundStatusInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 7, 1, 8),
    _ApexQamRfRedundStatusInvalidApplyText_Type()
)
apexQamRfRedundStatusInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfRedundStatusInvalidApplyText.setStatus("current")
_ApexQamRfPortMuteStatusTable_Object = MibTable
apexQamRfPortMuteStatusTable = _ApexQamRfPortMuteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 8)
)
if mibBuilder.loadTexts:
    apexQamRfPortMuteStatusTable.setStatus("current")
_ApexQamRfPortMuteStatusEntry_Object = MibTableRow
apexQamRfPortMuteStatusEntry = _ApexQamRfPortMuteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 8, 1)
)
apexQamRfPortMuteStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamRfPortMuteStatusRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamRfPortMuteStatusEntry.setStatus("current")


class _ApexQamRfPortMuteStatusRfPortNum_Type(Integer32):
    """Custom type apexQamRfPortMuteStatusRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexQamRfPortMuteStatusRfPortNum_Type.__name__ = "Integer32"
_ApexQamRfPortMuteStatusRfPortNum_Object = MibTableColumn
apexQamRfPortMuteStatusRfPortNum = _ApexQamRfPortMuteStatusRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 8, 1, 1),
    _ApexQamRfPortMuteStatusRfPortNum_Type()
)
apexQamRfPortMuteStatusRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamRfPortMuteStatusRfPortNum.setStatus("current")


class _ApexQamRfPortMuteStatus_Type(Integer32):
    """Custom type apexQamRfPortMuteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("muted", 2),
          ("unmuted", 1))
    )


_ApexQamRfPortMuteStatus_Type.__name__ = "Integer32"
_ApexQamRfPortMuteStatus_Object = MibTableColumn
apexQamRfPortMuteStatus = _ApexQamRfPortMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 8, 1, 2),
    _ApexQamRfPortMuteStatus_Type()
)
apexQamRfPortMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortMuteStatus.setStatus("current")
_ApexQamQrmRevisionStatusTable_Object = MibTable
apexQamQrmRevisionStatusTable = _ApexQamQrmRevisionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9)
)
if mibBuilder.loadTexts:
    apexQamQrmRevisionStatusTable.setStatus("current")
_ApexQamQrmRevisionStatusEntry_Object = MibTableRow
apexQamQrmRevisionStatusEntry = _ApexQamQrmRevisionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1)
)
apexQamQrmRevisionStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamQrmRevStatQrmNum"),
)
if mibBuilder.loadTexts:
    apexQamQrmRevisionStatusEntry.setStatus("current")


class _ApexQamQrmRevStatQrmNum_Type(Integer32):
    """Custom type apexQamQrmRevStatQrmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexQamQrmRevStatQrmNum_Type.__name__ = "Integer32"
_ApexQamQrmRevStatQrmNum_Object = MibTableColumn
apexQamQrmRevStatQrmNum = _ApexQamQrmRevStatQrmNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 1),
    _ApexQamQrmRevStatQrmNum_Type()
)
apexQamQrmRevStatQrmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamQrmRevStatQrmNum.setStatus("current")


class _ApexQamQrmRevStatBoardId_Type(Integer32):
    """Custom type apexQamQrmRevStatBoardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notSupported", 1),
          ("supported", 2))
    )


_ApexQamQrmRevStatBoardId_Type.__name__ = "Integer32"
_ApexQamQrmRevStatBoardId_Object = MibTableColumn
apexQamQrmRevStatBoardId = _ApexQamQrmRevStatBoardId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 2),
    _ApexQamQrmRevStatBoardId_Type()
)
apexQamQrmRevStatBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatBoardId.setStatus("current")


class _ApexQamQrmRevStatAppFw_Type(Integer32):
    """Custom type apexQamQrmRevStatAppFw based on Integer32"""
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
        *(("aboveRelease", 4),
          ("atRelease", 3),
          ("belowRelease", 2),
          ("notApplicable", 0),
          ("notSupported", 1))
    )


_ApexQamQrmRevStatAppFw_Type.__name__ = "Integer32"
_ApexQamQrmRevStatAppFw_Object = MibTableColumn
apexQamQrmRevStatAppFw = _ApexQamQrmRevStatAppFw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 3),
    _ApexQamQrmRevStatAppFw_Type()
)
apexQamQrmRevStatAppFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatAppFw.setStatus("current")


class _ApexQamQrmRevStatBootLoaderFw_Type(Integer32):
    """Custom type apexQamQrmRevStatBootLoaderFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notSupported", 1),
          ("supported", 2))
    )


_ApexQamQrmRevStatBootLoaderFw_Type.__name__ = "Integer32"
_ApexQamQrmRevStatBootLoaderFw_Object = MibTableColumn
apexQamQrmRevStatBootLoaderFw = _ApexQamQrmRevStatBootLoaderFw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 4),
    _ApexQamQrmRevStatBootLoaderFw_Type()
)
apexQamQrmRevStatBootLoaderFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatBootLoaderFw.setStatus("current")


class _ApexQamQrmRevStatFpga_Type(Integer32):
    """Custom type apexQamQrmRevStatFpga based on Integer32"""
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
        *(("aboveRelease", 4),
          ("atRelease", 3),
          ("belowRelease", 2),
          ("notApplicable", 0),
          ("notSupported", 1))
    )


_ApexQamQrmRevStatFpga_Type.__name__ = "Integer32"
_ApexQamQrmRevStatFpga_Object = MibTableColumn
apexQamQrmRevStatFpga = _ApexQamQrmRevStatFpga_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 5),
    _ApexQamQrmRevStatFpga_Type()
)
apexQamQrmRevStatFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatFpga.setStatus("current")


class _ApexQamQrmRevStatHw_Type(Integer32):
    """Custom type apexQamQrmRevStatHw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notSupported", 1),
          ("supported", 2))
    )


_ApexQamQrmRevStatHw_Type.__name__ = "Integer32"
_ApexQamQrmRevStatHw_Object = MibTableColumn
apexQamQrmRevStatHw = _ApexQamQrmRevStatHw_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 6),
    _ApexQamQrmRevStatHw_Type()
)
apexQamQrmRevStatHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatHw.setStatus("current")


class _ApexQamQrmRevStatQrmSupported_Type(Integer32):
    """Custom type apexQamQrmRevStatQrmSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notSupported", 1),
          ("supported", 2))
    )


_ApexQamQrmRevStatQrmSupported_Type.__name__ = "Integer32"
_ApexQamQrmRevStatQrmSupported_Object = MibTableColumn
apexQamQrmRevStatQrmSupported = _ApexQamQrmRevStatQrmSupported_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 7),
    _ApexQamQrmRevStatQrmSupported_Type()
)
apexQamQrmRevStatQrmSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatQrmSupported.setStatus("current")


class _ApexQamQrmRevStatFpga2_Type(Integer32):
    """Custom type apexQamQrmRevStatFpga2 based on Integer32"""
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
        *(("aboveRelease", 4),
          ("atRelease", 3),
          ("belowRelease", 2),
          ("notApplicable", 0),
          ("notSupported", 1))
    )


_ApexQamQrmRevStatFpga2_Type.__name__ = "Integer32"
_ApexQamQrmRevStatFpga2_Object = MibTableColumn
apexQamQrmRevStatFpga2 = _ApexQamQrmRevStatFpga2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 9, 1, 8),
    _ApexQamQrmRevStatFpga2_Type()
)
apexQamQrmRevStatFpga2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamQrmRevStatFpga2.setStatus("current")
_ApexQamRfPortChannelInfoTable_Object = MibTable
apexQamRfPortChannelInfoTable = _ApexQamRfPortChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 10)
)
if mibBuilder.loadTexts:
    apexQamRfPortChannelInfoTable.setStatus("current")
_ApexQamRfPortChannelInfoEntry_Object = MibTableRow
apexQamRfPortChannelInfoEntry = _ApexQamRfPortChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 10, 1)
)
apexQamRfPortChannelInfoEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamRfPortChannelInfoRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQamRfPortChannelInfoEntry.setStatus("current")


class _ApexQamRfPortChannelInfoRfPortNum_Type(Integer32):
    """Custom type apexQamRfPortChannelInfoRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexQamRfPortChannelInfoRfPortNum_Type.__name__ = "Integer32"
_ApexQamRfPortChannelInfoRfPortNum_Object = MibTableColumn
apexQamRfPortChannelInfoRfPortNum = _ApexQamRfPortChannelInfoRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 10, 1, 1),
    _ApexQamRfPortChannelInfoRfPortNum_Type()
)
apexQamRfPortChannelInfoRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamRfPortChannelInfoRfPortNum.setStatus("current")


class _ApexQamRfPortChannelInfoChanA_Type(Integer32):
    """Custom type apexQamRfPortChannelInfoChanA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(29, 29),
        ValueRangeConstraint(33, 33),
        ValueRangeConstraint(37, 37),
        ValueRangeConstraint(41, 41),
        ValueRangeConstraint(45, 45),
    )


_ApexQamRfPortChannelInfoChanA_Type.__name__ = "Integer32"
_ApexQamRfPortChannelInfoChanA_Object = MibTableColumn
apexQamRfPortChannelInfoChanA = _ApexQamRfPortChannelInfoChanA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 10, 1, 2),
    _ApexQamRfPortChannelInfoChanA_Type()
)
apexQamRfPortChannelInfoChanA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortChannelInfoChanA.setStatus("current")


class _ApexQamRfPortChannelInfoChanCount_Type(Integer32):
    """Custom type apexQamRfPortChannelInfoChanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_ApexQamRfPortChannelInfoChanCount_Type.__name__ = "Integer32"
_ApexQamRfPortChannelInfoChanCount_Object = MibTableColumn
apexQamRfPortChannelInfoChanCount = _ApexQamRfPortChannelInfoChanCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 10, 1, 3),
    _ApexQamRfPortChannelInfoChanCount_Type()
)
apexQamRfPortChannelInfoChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamRfPortChannelInfoChanCount.setStatus("current")
_ApexQamChannelIdTable_Object = MibTable
apexQamChannelIdTable = _ApexQamChannelIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11)
)
if mibBuilder.loadTexts:
    apexQamChannelIdTable.setStatus("current")
_ApexQamChannelIdEntry_Object = MibTableRow
apexQamChannelIdEntry = _ApexQamChannelIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1)
)
apexQamChannelIdEntry.setIndexNames(
    (0, "APEX-MIB", "apexQamChannelIdChannelNum"),
)
if mibBuilder.loadTexts:
    apexQamChannelIdEntry.setStatus("current")


class _ApexQamChannelIdChannelNum_Type(Integer32):
    """Custom type apexQamChannelIdChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexQamChannelIdChannelNum_Type.__name__ = "Integer32"
_ApexQamChannelIdChannelNum_Object = MibTableColumn
apexQamChannelIdChannelNum = _ApexQamChannelIdChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 1),
    _ApexQamChannelIdChannelNum_Type()
)
apexQamChannelIdChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQamChannelIdChannelNum.setStatus("current")


class _ApexQamChannelIdSlotNum_Type(Integer32):
    """Custom type apexQamChannelIdSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ApexQamChannelIdSlotNum_Type.__name__ = "Integer32"
_ApexQamChannelIdSlotNum_Object = MibTableColumn
apexQamChannelIdSlotNum = _ApexQamChannelIdSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 2),
    _ApexQamChannelIdSlotNum_Type()
)
apexQamChannelIdSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelIdSlotNum.setStatus("current")


class _ApexQamChannelIdRfPortNum_Type(Integer32):
    """Custom type apexQamChannelIdRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ApexQamChannelIdRfPortNum_Type.__name__ = "Integer32"
_ApexQamChannelIdRfPortNum_Object = MibTableColumn
apexQamChannelIdRfPortNum = _ApexQamChannelIdRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 3),
    _ApexQamChannelIdRfPortNum_Type()
)
apexQamChannelIdRfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelIdRfPortNum.setStatus("current")


class _ApexQamChannelIdModuleRfPortNum_Type(Integer32):
    """Custom type apexQamChannelIdModuleRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexQamChannelIdModuleRfPortNum_Type.__name__ = "Integer32"
_ApexQamChannelIdModuleRfPortNum_Object = MibTableColumn
apexQamChannelIdModuleRfPortNum = _ApexQamChannelIdModuleRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 4),
    _ApexQamChannelIdModuleRfPortNum_Type()
)
apexQamChannelIdModuleRfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelIdModuleRfPortNum.setStatus("current")


class _ApexQamChannelIdChannelLetter_Type(DisplayString):
    """Custom type apexQamChannelIdChannelLetter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_ApexQamChannelIdChannelLetter_Type.__name__ = "DisplayString"
_ApexQamChannelIdChannelLetter_Object = MibTableColumn
apexQamChannelIdChannelLetter = _ApexQamChannelIdChannelLetter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 5),
    _ApexQamChannelIdChannelLetter_Type()
)
apexQamChannelIdChannelLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelIdChannelLetter.setStatus("current")


class _ApexQamChannelIdChannelDescription_Type(DisplayString):
    """Custom type apexQamChannelIdChannelDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ApexQamChannelIdChannelDescription_Type.__name__ = "DisplayString"
_ApexQamChannelIdChannelDescription_Object = MibTableColumn
apexQamChannelIdChannelDescription = _ApexQamChannelIdChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 2, 11, 1, 6),
    _ApexQamChannelIdChannelDescription_Type()
)
apexQamChannelIdChannelDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQamChannelIdChannelDescription.setStatus("current")
_ApexQrmDownload_ObjectIdentity = ObjectIdentity
apexQrmDownload = _ApexQrmDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3)
)
_ApexQrmDownloadConfig_ObjectIdentity = ObjectIdentity
apexQrmDownloadConfig = _ApexQrmDownloadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1)
)
_ApexQrmDownloadConfigGeneral_ObjectIdentity = ObjectIdentity
apexQrmDownloadConfigGeneral = _ApexQrmDownloadConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1, 1)
)
_ApexQrmDownloadConfigTable_Object = MibTable
apexQrmDownloadConfigTable = _ApexQrmDownloadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1, 2)
)
if mibBuilder.loadTexts:
    apexQrmDownloadConfigTable.setStatus("current")
_ApexQrmDownloadConfigEntry_Object = MibTableRow
apexQrmDownloadConfigEntry = _ApexQrmDownloadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1, 2, 1)
)
apexQrmDownloadConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexQrmDownloadConfigQrmNum"),
)
if mibBuilder.loadTexts:
    apexQrmDownloadConfigEntry.setStatus("current")


class _ApexQrmDownloadConfigQrmNum_Type(Integer32):
    """Custom type apexQrmDownloadConfigQrmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexQrmDownloadConfigQrmNum_Type.__name__ = "Integer32"
_ApexQrmDownloadConfigQrmNum_Object = MibTableColumn
apexQrmDownloadConfigQrmNum = _ApexQrmDownloadConfigQrmNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1, 2, 1, 1),
    _ApexQrmDownloadConfigQrmNum_Type()
)
apexQrmDownloadConfigQrmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQrmDownloadConfigQrmNum.setStatus("current")


class _ApexQrmDownloadConfigRequest_Type(Integer32):
    """Custom type apexQrmDownloadConfigRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("requestDownload", 1),
          ("requestNotInProgress", 0))
    )


_ApexQrmDownloadConfigRequest_Type.__name__ = "Integer32"
_ApexQrmDownloadConfigRequest_Object = MibTableColumn
apexQrmDownloadConfigRequest = _ApexQrmDownloadConfigRequest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 1, 2, 1, 2),
    _ApexQrmDownloadConfigRequest_Type()
)
apexQrmDownloadConfigRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexQrmDownloadConfigRequest.setStatus("current")
_ApexQrmDownloadStatus_ObjectIdentity = ObjectIdentity
apexQrmDownloadStatus = _ApexQrmDownloadStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2)
)
_ApexQrmDownloadStatusGeneral_ObjectIdentity = ObjectIdentity
apexQrmDownloadStatusGeneral = _ApexQrmDownloadStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 1)
)
_ApexQrmDownloadStatusTable_Object = MibTable
apexQrmDownloadStatusTable = _ApexQrmDownloadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2)
)
if mibBuilder.loadTexts:
    apexQrmDownloadStatusTable.setStatus("current")
_ApexQrmDownloadStatusEntry_Object = MibTableRow
apexQrmDownloadStatusEntry = _ApexQrmDownloadStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1)
)
apexQrmDownloadStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexQrmDownloadStatusRfPortNum"),
)
if mibBuilder.loadTexts:
    apexQrmDownloadStatusEntry.setStatus("current")


class _ApexQrmDownloadStatusRfPortNum_Type(Integer32):
    """Custom type apexQrmDownloadStatusRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexQrmDownloadStatusRfPortNum_Type.__name__ = "Integer32"
_ApexQrmDownloadStatusRfPortNum_Object = MibTableColumn
apexQrmDownloadStatusRfPortNum = _ApexQrmDownloadStatusRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 1),
    _ApexQrmDownloadStatusRfPortNum_Type()
)
apexQrmDownloadStatusRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQrmDownloadStatusRfPortNum.setStatus("current")
_ApexQrmDownloadStatusDescription_Type = DisplayString
_ApexQrmDownloadStatusDescription_Object = MibTableColumn
apexQrmDownloadStatusDescription = _ApexQrmDownloadStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 2),
    _ApexQrmDownloadStatusDescription_Type()
)
apexQrmDownloadStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmDownloadStatusDescription.setStatus("current")


class _ApexQrmDownloadProgress_Type(Integer32):
    """Custom type apexQrmDownloadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_ApexQrmDownloadProgress_Type.__name__ = "Integer32"
_ApexQrmDownloadProgress_Object = MibTableColumn
apexQrmDownloadProgress = _ApexQrmDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 3),
    _ApexQrmDownloadProgress_Type()
)
apexQrmDownloadProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmDownloadProgress.setStatus("current")


class _ApexQrmDownloadSupported_Type(Integer32):
    """Custom type apexQrmDownloadSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notSupported", 1),
          ("supported", 2))
    )


_ApexQrmDownloadSupported_Type.__name__ = "Integer32"
_ApexQrmDownloadSupported_Object = MibTableColumn
apexQrmDownloadSupported = _ApexQrmDownloadSupported_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 4),
    _ApexQrmDownloadSupported_Type()
)
apexQrmDownloadSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmDownloadSupported.setStatus("current")


class _ApexQrmDownloadRequired_Type(Integer32):
    """Custom type apexQrmDownloadRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notRequired", 1),
          ("required", 2))
    )


_ApexQrmDownloadRequired_Type.__name__ = "Integer32"
_ApexQrmDownloadRequired_Object = MibTableColumn
apexQrmDownloadRequired = _ApexQrmDownloadRequired_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 5),
    _ApexQrmDownloadRequired_Type()
)
apexQrmDownloadRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmDownloadRequired.setStatus("current")


class _ApexQrmDownloadFileSet_Type(Integer32):
    """Custom type apexQrmDownloadFileSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fileSet1", 1),
          ("fileSet2", 2),
          ("fileSet3", 3),
          ("notApplicable", 0))
    )


_ApexQrmDownloadFileSet_Type.__name__ = "Integer32"
_ApexQrmDownloadFileSet_Object = MibTableColumn
apexQrmDownloadFileSet = _ApexQrmDownloadFileSet_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 2, 1, 6),
    _ApexQrmDownloadFileSet_Type()
)
apexQrmDownloadFileSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmDownloadFileSet.setStatus("current")
_ApexQrmFileRevisionTable_Object = MibTable
apexQrmFileRevisionTable = _ApexQrmFileRevisionTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3)
)
if mibBuilder.loadTexts:
    apexQrmFileRevisionTable.setStatus("current")
_ApexQrmFileRevisionEntry_Object = MibTableRow
apexQrmFileRevisionEntry = _ApexQrmFileRevisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1)
)
apexQrmFileRevisionEntry.setIndexNames(
    (0, "APEX-MIB", "apexQrmFileRevFileSetNum"),
)
if mibBuilder.loadTexts:
    apexQrmFileRevisionEntry.setStatus("current")


class _ApexQrmFileRevFileSetNum_Type(Integer32):
    """Custom type apexQrmFileRevFileSetNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ApexQrmFileRevFileSetNum_Type.__name__ = "Integer32"
_ApexQrmFileRevFileSetNum_Object = MibTableColumn
apexQrmFileRevFileSetNum = _ApexQrmFileRevFileSetNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 1),
    _ApexQrmFileRevFileSetNum_Type()
)
apexQrmFileRevFileSetNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexQrmFileRevFileSetNum.setStatus("current")


class _ApexQrmFileRevFirmware_Type(DisplayString):
    """Custom type apexQrmFileRevFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQrmFileRevFirmware_Type.__name__ = "DisplayString"
_ApexQrmFileRevFirmware_Object = MibTableColumn
apexQrmFileRevFirmware = _ApexQrmFileRevFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 2),
    _ApexQrmFileRevFirmware_Type()
)
apexQrmFileRevFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmFileRevFirmware.setStatus("current")


class _ApexQrmFileRevCalibration_Type(DisplayString):
    """Custom type apexQrmFileRevCalibration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQrmFileRevCalibration_Type.__name__ = "DisplayString"
_ApexQrmFileRevCalibration_Object = MibTableColumn
apexQrmFileRevCalibration = _ApexQrmFileRevCalibration_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 3),
    _ApexQrmFileRevCalibration_Type()
)
apexQrmFileRevCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmFileRevCalibration.setStatus("current")


class _ApexQrmFileRevFpga_Type(DisplayString):
    """Custom type apexQrmFileRevFpga based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQrmFileRevFpga_Type.__name__ = "DisplayString"
_ApexQrmFileRevFpga_Object = MibTableColumn
apexQrmFileRevFpga = _ApexQrmFileRevFpga_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 4),
    _ApexQrmFileRevFpga_Type()
)
apexQrmFileRevFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmFileRevFpga.setStatus("current")


class _ApexQrmFileRevFpga2_Type(DisplayString):
    """Custom type apexQrmFileRevFpga2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ApexQrmFileRevFpga2_Type.__name__ = "DisplayString"
_ApexQrmFileRevFpga2_Object = MibTableColumn
apexQrmFileRevFpga2 = _ApexQrmFileRevFpga2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 5),
    _ApexQrmFileRevFpga2_Type()
)
apexQrmFileRevFpga2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmFileRevFpga2.setStatus("current")


class _ApexQrmFileRevDateTime_Type(DisplayString):
    """Custom type apexQrmFileRevDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApexQrmFileRevDateTime_Type.__name__ = "DisplayString"
_ApexQrmFileRevDateTime_Object = MibTableColumn
apexQrmFileRevDateTime = _ApexQrmFileRevDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 8, 3, 2, 3, 1, 6),
    _ApexQrmFileRevDateTime_Type()
)
apexQrmFileRevDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexQrmFileRevDateTime.setStatus("current")
_ApexSessionControl_ObjectIdentity = ObjectIdentity
apexSessionControl = _ApexSessionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9)
)
_ApexSessionControlConfig_ObjectIdentity = ObjectIdentity
apexSessionControlConfig = _ApexSessionControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1)
)
_ApexSessionControlConfigGeneral_ObjectIdentity = ObjectIdentity
apexSessionControlConfigGeneral = _ApexSessionControlConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1)
)


class _ApexSesContConfProtocol_Type(Integer32):
    """Custom type apexSesContConfProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mha-ermi", 3),
          ("none", 0),
          ("rpc", 1),
          ("rtsp", 2))
    )


_ApexSesContConfProtocol_Type.__name__ = "Integer32"
_ApexSesContConfProtocol_Object = MibScalar
apexSesContConfProtocol = _ApexSesContConfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 1),
    _ApexSesContConfProtocol_Type()
)
apexSesContConfProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfProtocol.setStatus("current")
_ApexSesContConfTableApplyChange_Type = ApplyDataToDeviceTYPE
_ApexSesContConfTableApplyChange_Object = MibScalar
apexSesContConfTableApplyChange = _ApexSesContConfTableApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 2),
    _ApexSesContConfTableApplyChange_Type()
)
apexSesContConfTableApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfTableApplyChange.setStatus("current")
_ApexSesContConfRateCompareType_Type = RateComparisonTYPE
_ApexSesContConfRateCompareType_Object = MibScalar
apexSesContConfRateCompareType = _ApexSesContConfRateCompareType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 3),
    _ApexSesContConfRateCompareType_Type()
)
apexSesContConfRateCompareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfRateCompareType.setStatus("current")


class _ApexSesContConfRedundThreshold_Type(Integer32):
    """Custom type apexSesContConfRedundThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexSesContConfRedundThreshold_Type.__name__ = "Integer32"
_ApexSesContConfRedundThreshold_Object = MibScalar
apexSesContConfRedundThreshold = _ApexSesContConfRedundThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 4),
    _ApexSesContConfRedundThreshold_Type()
)
apexSesContConfRedundThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfRedundThreshold.setStatus("obsolete")
_ApexSesContConfInputPreEncryptCheck_Type = EnableDisableTYPE
_ApexSesContConfInputPreEncryptCheck_Object = MibScalar
apexSesContConfInputPreEncryptCheck = _ApexSesContConfInputPreEncryptCheck_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 5),
    _ApexSesContConfInputPreEncryptCheck_Type()
)
apexSesContConfInputPreEncryptCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfInputPreEncryptCheck.setStatus("current")


class _ApexSesContConfRedundType_Type(Integer32):
    """Custom type apexSesContConfRedundType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hotHot", 2),
          ("hotWarm", 1))
    )


_ApexSesContConfRedundType_Type.__name__ = "Integer32"
_ApexSesContConfRedundType_Object = MibScalar
apexSesContConfRedundType = _ApexSesContConfRedundType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 6),
    _ApexSesContConfRedundType_Type()
)
apexSesContConfRedundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfRedundType.setStatus("current")
_ApexSesContConfFollowDtcp_Type = EnableDisableTYPE
_ApexSesContConfFollowDtcp_Object = MibScalar
apexSesContConfFollowDtcp = _ApexSesContConfFollowDtcp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 1, 7),
    _ApexSesContConfFollowDtcp_Type()
)
apexSesContConfFollowDtcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfFollowDtcp.setStatus("current")
_ApexSesContConfTable_Object = MibTable
apexSesContConfTable = _ApexSesContConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 2)
)
if mibBuilder.loadTexts:
    apexSesContConfTable.setStatus("current")
_ApexSesContConfEntry_Object = MibTableRow
apexSesContConfEntry = _ApexSesContConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 2, 1)
)
apexSesContConfEntry.setIndexNames(
    (0, "APEX-MIB", "apexSesContConfOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexSesContConfEntry.setStatus("current")


class _ApexSesContConfOutputTsNum_Type(Integer32):
    """Custom type apexSesContConfOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexSesContConfOutputTsNum_Type.__name__ = "Integer32"
_ApexSesContConfOutputTsNum_Object = MibTableColumn
apexSesContConfOutputTsNum = _ApexSesContConfOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 2, 1, 1),
    _ApexSesContConfOutputTsNum_Type()
)
apexSesContConfOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexSesContConfOutputTsNum.setStatus("current")


class _ApexSesContConfGbePrimaryInterface_Type(Integer32):
    """Custom type apexSesContConfGbePrimaryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexSesContConfGbePrimaryInterface_Type.__name__ = "Integer32"
_ApexSesContConfGbePrimaryInterface_Object = MibTableColumn
apexSesContConfGbePrimaryInterface = _ApexSesContConfGbePrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 2, 1, 2),
    _ApexSesContConfGbePrimaryInterface_Type()
)
apexSesContConfGbePrimaryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfGbePrimaryInterface.setStatus("current")


class _ApexSesContConfGbeSecondaryInterface_Type(Integer32):
    """Custom type apexSesContConfGbeSecondaryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexSesContConfGbeSecondaryInterface_Type.__name__ = "Integer32"
_ApexSesContConfGbeSecondaryInterface_Object = MibTableColumn
apexSesContConfGbeSecondaryInterface = _ApexSesContConfGbeSecondaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 1, 2, 1, 3),
    _ApexSesContConfGbeSecondaryInterface_Type()
)
apexSesContConfGbeSecondaryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSesContConfGbeSecondaryInterface.setStatus("current")
_ApexSessionControlStatus_ObjectIdentity = ObjectIdentity
apexSessionControlStatus = _ApexSessionControlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 2)
)
_ApexSessionControlStatusGeneral_ObjectIdentity = ObjectIdentity
apexSessionControlStatusGeneral = _ApexSessionControlStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 2, 1)
)


class _ApexSesContStatProtocol_Type(Integer32):
    """Custom type apexSesContStatProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mha-ermi", 3),
          ("none", 0),
          ("rpc", 1),
          ("rtsp", 2))
    )


_ApexSesContStatProtocol_Type.__name__ = "Integer32"
_ApexSesContStatProtocol_Object = MibScalar
apexSesContStatProtocol = _ApexSesContStatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 2, 1, 1),
    _ApexSesContStatProtocol_Type()
)
apexSesContStatProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexSesContStatProtocol.setStatus("current")
_ApexRpc_ObjectIdentity = ObjectIdentity
apexRpc = _ApexRpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3)
)
_ApexRpcConfig_ObjectIdentity = ObjectIdentity
apexRpcConfig = _ApexRpcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1)
)
_ApexRpcConfigGeneral_ObjectIdentity = ObjectIdentity
apexRpcConfigGeneral = _ApexRpcConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1)
)


class _ApexRpcDataCarouselProgram_Type(Integer32):
    """Custom type apexRpcDataCarouselProgram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRpcDataCarouselProgram_Type.__name__ = "Integer32"
_ApexRpcDataCarouselProgram_Object = MibScalar
apexRpcDataCarouselProgram = _ApexRpcDataCarouselProgram_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 1),
    _ApexRpcDataCarouselProgram_Type()
)
apexRpcDataCarouselProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcDataCarouselProgram.setStatus("current")
_ApexRpcReportAllSessions_Type = EnableDisableTYPE
_ApexRpcReportAllSessions_Object = MibScalar
apexRpcReportAllSessions = _ApexRpcReportAllSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 2),
    _ApexRpcReportAllSessions_Type()
)
apexRpcReportAllSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcReportAllSessions.setStatus("current")


class _ApexRpcDeviceName_Type(DisplayString):
    """Custom type apexRpcDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexRpcDeviceName_Type.__name__ = "DisplayString"
_ApexRpcDeviceName_Object = MibScalar
apexRpcDeviceName = _ApexRpcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 3),
    _ApexRpcDeviceName_Type()
)
apexRpcDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcDeviceName.setStatus("current")


class _ApexRpcDeviceType_Type(DisplayString):
    """Custom type apexRpcDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexRpcDeviceType_Type.__name__ = "DisplayString"
_ApexRpcDeviceType_Object = MibScalar
apexRpcDeviceType = _ApexRpcDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 4),
    _ApexRpcDeviceType_Type()
)
apexRpcDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcDeviceType.setStatus("current")
_ApexRpcControlInterface_Type = EthernetInterfaceTYPE
_ApexRpcControlInterface_Object = MibScalar
apexRpcControlInterface = _ApexRpcControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 5),
    _ApexRpcControlInterface_Type()
)
apexRpcControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcControlInterface.setStatus("current")


class _ApexRpcNumShellSessions_Type(Integer32):
    """Custom type apexRpcNumShellSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApexRpcNumShellSessions_Type.__name__ = "Integer32"
_ApexRpcNumShellSessions_Object = MibScalar
apexRpcNumShellSessions = _ApexRpcNumShellSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 6),
    _ApexRpcNumShellSessions_Type()
)
apexRpcNumShellSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcNumShellSessions.setStatus("current")
_ApexRpcAvgBandwidthEnable_Type = EnableDisableTYPE
_ApexRpcAvgBandwidthEnable_Object = MibScalar
apexRpcAvgBandwidthEnable = _ApexRpcAvgBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 7),
    _ApexRpcAvgBandwidthEnable_Type()
)
apexRpcAvgBandwidthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcAvgBandwidthEnable.setStatus("current")
_ApexRpcApplyChange_Type = ApplyDataToDeviceTYPE
_ApexRpcApplyChange_Object = MibScalar
apexRpcApplyChange = _ApexRpcApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 1, 8),
    _ApexRpcApplyChange_Type()
)
apexRpcApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcApplyChange.setStatus("current")
_ApexRpcRfPortTable_Object = MibTable
apexRpcRfPortTable = _ApexRpcRfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 2)
)
if mibBuilder.loadTexts:
    apexRpcRfPortTable.setStatus("current")
_ApexRpcRfPortEntry_Object = MibTableRow
apexRpcRfPortEntry = _ApexRpcRfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 2, 1)
)
apexRpcRfPortEntry.setIndexNames(
    (0, "APEX-MIB", "apexRpcRfPortNum"),
)
if mibBuilder.loadTexts:
    apexRpcRfPortEntry.setStatus("current")


class _ApexRpcRfPortNum_Type(Integer32):
    """Custom type apexRpcRfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexRpcRfPortNum_Type.__name__ = "Integer32"
_ApexRpcRfPortNum_Object = MibTableColumn
apexRpcRfPortNum = _ApexRpcRfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 2, 1, 1),
    _ApexRpcRfPortNum_Type()
)
apexRpcRfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRpcRfPortNum.setStatus("current")


class _ApexRpcRfPortName_Type(DisplayString):
    """Custom type apexRpcRfPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexRpcRfPortName_Type.__name__ = "DisplayString"
_ApexRpcRfPortName_Object = MibTableColumn
apexRpcRfPortName = _ApexRpcRfPortName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 2, 1, 2),
    _ApexRpcRfPortName_Type()
)
apexRpcRfPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcRfPortName.setStatus("current")


class _ApexRpcRfPortServiceGroup_Type(Unsigned32):
    """Custom type apexRpcRfPortServiceGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApexRpcRfPortServiceGroup_Type.__name__ = "Unsigned32"
_ApexRpcRfPortServiceGroup_Object = MibTableColumn
apexRpcRfPortServiceGroup = _ApexRpcRfPortServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 2, 1, 3),
    _ApexRpcRfPortServiceGroup_Type()
)
apexRpcRfPortServiceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcRfPortServiceGroup.setStatus("current")
_ApexRpcRfChannelTable_Object = MibTable
apexRpcRfChannelTable = _ApexRpcRfChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 3)
)
if mibBuilder.loadTexts:
    apexRpcRfChannelTable.setStatus("current")
_ApexRpcRfChannelEntry_Object = MibTableRow
apexRpcRfChannelEntry = _ApexRpcRfChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 3, 1)
)
apexRpcRfChannelEntry.setIndexNames(
    (0, "APEX-MIB", "apexRpcRfChannelNum"),
)
if mibBuilder.loadTexts:
    apexRpcRfChannelEntry.setStatus("current")


class _ApexRpcRfChannelNum_Type(Integer32):
    """Custom type apexRpcRfChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRpcRfChannelNum_Type.__name__ = "Integer32"
_ApexRpcRfChannelNum_Object = MibTableColumn
apexRpcRfChannelNum = _ApexRpcRfChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 3, 1, 1),
    _ApexRpcRfChannelNum_Type()
)
apexRpcRfChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRpcRfChannelNum.setStatus("current")


class _ApexRpcRfChannelName_Type(DisplayString):
    """Custom type apexRpcRfChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexRpcRfChannelName_Type.__name__ = "DisplayString"
_ApexRpcRfChannelName_Object = MibTableColumn
apexRpcRfChannelName = _ApexRpcRfChannelName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 1, 3, 1, 2),
    _ApexRpcRfChannelName_Type()
)
apexRpcRfChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRpcRfChannelName.setStatus("current")
_ApexRpcStatus_ObjectIdentity = ObjectIdentity
apexRpcStatus = _ApexRpcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2)
)
_ApexRpcStatusGeneral_ObjectIdentity = ObjectIdentity
apexRpcStatusGeneral = _ApexRpcStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 1)
)
_ApexRpcSessionStatTable_Object = MibTable
apexRpcSessionStatTable = _ApexRpcSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    apexRpcSessionStatTable.setStatus("current")
_ApexRpcSessionStatEntry_Object = MibTableRow
apexRpcSessionStatEntry = _ApexRpcSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1)
)
apexRpcSessionStatEntry.setIndexNames(
    (0, "APEX-MIB", "apexRpcSessionStatIndex"),
)
if mibBuilder.loadTexts:
    apexRpcSessionStatEntry.setStatus("current")


class _ApexRpcSessionStatIndex_Type(Integer32):
    """Custom type apexRpcSessionStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexRpcSessionStatIndex_Type.__name__ = "Integer32"
_ApexRpcSessionStatIndex_Object = MibTableColumn
apexRpcSessionStatIndex = _ApexRpcSessionStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 1),
    _ApexRpcSessionStatIndex_Type()
)
apexRpcSessionStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRpcSessionStatIndex.setStatus("current")
_ApexRpcSessionStatInputTsIndex_Type = Integer32
_ApexRpcSessionStatInputTsIndex_Object = MibTableColumn
apexRpcSessionStatInputTsIndex = _ApexRpcSessionStatInputTsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 2),
    _ApexRpcSessionStatInputTsIndex_Type()
)
apexRpcSessionStatInputTsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatInputTsIndex.setStatus("current")
_ApexRpcSessionStatInputProgramNum_Type = Integer32
_ApexRpcSessionStatInputProgramNum_Object = MibTableColumn
apexRpcSessionStatInputProgramNum = _ApexRpcSessionStatInputProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 3),
    _ApexRpcSessionStatInputProgramNum_Type()
)
apexRpcSessionStatInputProgramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatInputProgramNum.setStatus("current")
_ApexRpcSessionStatSourceIpAddr3_Type = IpAddress
_ApexRpcSessionStatSourceIpAddr3_Object = MibTableColumn
apexRpcSessionStatSourceIpAddr3 = _ApexRpcSessionStatSourceIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 4),
    _ApexRpcSessionStatSourceIpAddr3_Type()
)
apexRpcSessionStatSourceIpAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatSourceIpAddr3.setStatus("current")
_ApexRpcSessionStatOutputQamChannel_Type = Integer32
_ApexRpcSessionStatOutputQamChannel_Object = MibTableColumn
apexRpcSessionStatOutputQamChannel = _ApexRpcSessionStatOutputQamChannel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 5),
    _ApexRpcSessionStatOutputQamChannel_Type()
)
apexRpcSessionStatOutputQamChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatOutputQamChannel.setStatus("current")
_ApexRpcSessionStatOutputProgramNum_Type = Integer32
_ApexRpcSessionStatOutputProgramNum_Object = MibTableColumn
apexRpcSessionStatOutputProgramNum = _ApexRpcSessionStatOutputProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 6),
    _ApexRpcSessionStatOutputProgramNum_Type()
)
apexRpcSessionStatOutputProgramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatOutputProgramNum.setStatus("current")
_ApexRpcSessionStatProgramBandwidth_Type = Integer32
_ApexRpcSessionStatProgramBandwidth_Object = MibTableColumn
apexRpcSessionStatProgramBandwidth = _ApexRpcSessionStatProgramBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 7),
    _ApexRpcSessionStatProgramBandwidth_Type()
)
apexRpcSessionStatProgramBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatProgramBandwidth.setStatus("current")


class _ApexRpcSessionStatSessionType_Type(Integer32):
    """Custom type apexRpcSessionStatSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSession", 0),
          ("sdv", 1),
          ("vodOrBroadcast", 2))
    )


_ApexRpcSessionStatSessionType_Type.__name__ = "Integer32"
_ApexRpcSessionStatSessionType_Object = MibTableColumn
apexRpcSessionStatSessionType = _ApexRpcSessionStatSessionType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 8),
    _ApexRpcSessionStatSessionType_Type()
)
apexRpcSessionStatSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatSessionType.setStatus("current")
_ApexRpcSessionStatSessionIdWord1_Type = Unsigned32
_ApexRpcSessionStatSessionIdWord1_Object = MibTableColumn
apexRpcSessionStatSessionIdWord1 = _ApexRpcSessionStatSessionIdWord1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 9),
    _ApexRpcSessionStatSessionIdWord1_Type()
)
apexRpcSessionStatSessionIdWord1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatSessionIdWord1.setStatus("current")
_ApexRpcSessionStatSessionIdWord2_Type = Unsigned32
_ApexRpcSessionStatSessionIdWord2_Object = MibTableColumn
apexRpcSessionStatSessionIdWord2 = _ApexRpcSessionStatSessionIdWord2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 10),
    _ApexRpcSessionStatSessionIdWord2_Type()
)
apexRpcSessionStatSessionIdWord2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatSessionIdWord2.setStatus("current")
_ApexRpcSessionStatSessionIdWord3_Type = Unsigned32
_ApexRpcSessionStatSessionIdWord3_Object = MibTableColumn
apexRpcSessionStatSessionIdWord3 = _ApexRpcSessionStatSessionIdWord3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 11),
    _ApexRpcSessionStatSessionIdWord3_Type()
)
apexRpcSessionStatSessionIdWord3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatSessionIdWord3.setStatus("current")
_ApexRpcSessionStatManagerIpAddr_Type = IpAddress
_ApexRpcSessionStatManagerIpAddr_Object = MibTableColumn
apexRpcSessionStatManagerIpAddr = _ApexRpcSessionStatManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 2, 1, 12),
    _ApexRpcSessionStatManagerIpAddr_Type()
)
apexRpcSessionStatManagerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcSessionStatManagerIpAddr.setStatus("current")
_ApexRpcQamStatTable_Object = MibTable
apexRpcQamStatTable = _ApexRpcQamStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    apexRpcQamStatTable.setStatus("current")
_ApexRpcQamStatEntry_Object = MibTableRow
apexRpcQamStatEntry = _ApexRpcQamStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3, 1)
)
apexRpcQamStatEntry.setIndexNames(
    (0, "APEX-MIB", "apexRpcQamStatQamChannelNum"),
)
if mibBuilder.loadTexts:
    apexRpcQamStatEntry.setStatus("current")


class _ApexRpcQamStatQamChannelNum_Type(Integer32):
    """Custom type apexRpcQamStatQamChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRpcQamStatQamChannelNum_Type.__name__ = "Integer32"
_ApexRpcQamStatQamChannelNum_Object = MibTableColumn
apexRpcQamStatQamChannelNum = _ApexRpcQamStatQamChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3, 1, 1),
    _ApexRpcQamStatQamChannelNum_Type()
)
apexRpcQamStatQamChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRpcQamStatQamChannelNum.setStatus("current")
_ApexRpcQamStatNumSdvSessions_Type = Integer32
_ApexRpcQamStatNumSdvSessions_Object = MibTableColumn
apexRpcQamStatNumSdvSessions = _ApexRpcQamStatNumSdvSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3, 1, 2),
    _ApexRpcQamStatNumSdvSessions_Type()
)
apexRpcQamStatNumSdvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcQamStatNumSdvSessions.setStatus("current")
_ApexRpcQamStatNumVodBcSessions_Type = Integer32
_ApexRpcQamStatNumVodBcSessions_Object = MibTableColumn
apexRpcQamStatNumVodBcSessions = _ApexRpcQamStatNumVodBcSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3, 1, 3),
    _ApexRpcQamStatNumVodBcSessions_Type()
)
apexRpcQamStatNumVodBcSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcQamStatNumVodBcSessions.setStatus("current")
_ApexRpcQamStatSdvGroupBandwidth_Type = Unsigned32
_ApexRpcQamStatSdvGroupBandwidth_Object = MibTableColumn
apexRpcQamStatSdvGroupBandwidth = _ApexRpcQamStatSdvGroupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 3, 2, 3, 1, 4),
    _ApexRpcQamStatSdvGroupBandwidth_Type()
)
apexRpcQamStatSdvGroupBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRpcQamStatSdvGroupBandwidth.setStatus("current")
_ApexRtsp_ObjectIdentity = ObjectIdentity
apexRtsp = _ApexRtsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4)
)
_ApexRtspConfig_ObjectIdentity = ObjectIdentity
apexRtspConfig = _ApexRtspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1)
)
_ApexRtspConfigGeneral_ObjectIdentity = ObjectIdentity
apexRtspConfigGeneral = _ApexRtspConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 1)
)


class _ApexRtspReportGbeInterfaces_Type(Integer32):
    """Custom type apexRtspReportGbeInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pairedPortAssignment", 3),
          ("reportGbe1and2", 1),
          ("reportGbe3and4", 2))
    )


_ApexRtspReportGbeInterfaces_Type.__name__ = "Integer32"
_ApexRtspReportGbeInterfaces_Object = MibScalar
apexRtspReportGbeInterfaces = _ApexRtspReportGbeInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 1, 1),
    _ApexRtspReportGbeInterfaces_Type()
)
apexRtspReportGbeInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspReportGbeInterfaces.setStatus("current")
_ApexRtspConfControllerApplyTable_Object = MibTable
apexRtspConfControllerApplyTable = _ApexRtspConfControllerApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 2)
)
if mibBuilder.loadTexts:
    apexRtspConfControllerApplyTable.setStatus("current")
_ApexRtspConfControllerApplyEntry_Object = MibTableRow
apexRtspConfControllerApplyEntry = _ApexRtspConfControllerApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 2, 1)
)
apexRtspConfControllerApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfControllerApplyNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfControllerApplyEntry.setStatus("current")


class _ApexRtspConfControllerApplyNum_Type(Integer32):
    """Custom type apexRtspConfControllerApplyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspConfControllerApplyNum_Type.__name__ = "Integer32"
_ApexRtspConfControllerApplyNum_Object = MibTableColumn
apexRtspConfControllerApplyNum = _ApexRtspConfControllerApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 2, 1, 1),
    _ApexRtspConfControllerApplyNum_Type()
)
apexRtspConfControllerApplyNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfControllerApplyNum.setStatus("current")
_ApexRtspConfControllerApplyChange_Type = ApplyDataToDeviceTYPE
_ApexRtspConfControllerApplyChange_Object = MibTableColumn
apexRtspConfControllerApplyChange = _ApexRtspConfControllerApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 2, 1, 2),
    _ApexRtspConfControllerApplyChange_Type()
)
apexRtspConfControllerApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControllerApplyChange.setStatus("current")
_ApexRtspConfControllerTable_Object = MibTable
apexRtspConfControllerTable = _ApexRtspConfControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3)
)
if mibBuilder.loadTexts:
    apexRtspConfControllerTable.setStatus("current")
_ApexRtspConfControllerEntry_Object = MibTableRow
apexRtspConfControllerEntry = _ApexRtspConfControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1)
)
apexRtspConfControllerEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfControllerNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfControllerEntry.setStatus("current")


class _ApexRtspConfControllerNum_Type(Integer32):
    """Custom type apexRtspConfControllerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspConfControllerNum_Type.__name__ = "Integer32"
_ApexRtspConfControllerNum_Object = MibTableColumn
apexRtspConfControllerNum = _ApexRtspConfControllerNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1, 1),
    _ApexRtspConfControllerNum_Type()
)
apexRtspConfControllerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfControllerNum.setStatus("current")
_ApexRtspConfControllerIp_Type = IpAddress
_ApexRtspConfControllerIp_Object = MibTableColumn
apexRtspConfControllerIp = _ApexRtspConfControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1, 2),
    _ApexRtspConfControllerIp_Type()
)
apexRtspConfControllerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControllerIp.setStatus("current")


class _ApexRtspConfControllerPort_Type(Integer32):
    """Custom type apexRtspConfControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApexRtspConfControllerPort_Type.__name__ = "Integer32"
_ApexRtspConfControllerPort_Object = MibTableColumn
apexRtspConfControllerPort = _ApexRtspConfControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1, 3),
    _ApexRtspConfControllerPort_Type()
)
apexRtspConfControllerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControllerPort.setStatus("current")


class _ApexRtspConfControllerHoldTime_Type(Integer32):
    """Custom type apexRtspConfControllerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(9, 300),
    )


_ApexRtspConfControllerHoldTime_Type.__name__ = "Integer32"
_ApexRtspConfControllerHoldTime_Object = MibTableColumn
apexRtspConfControllerHoldTime = _ApexRtspConfControllerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1, 4),
    _ApexRtspConfControllerHoldTime_Type()
)
apexRtspConfControllerHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControllerHoldTime.setStatus("current")


class _ApexRtspConfControllerBandwidthDelta_Type(Integer32):
    """Custom type apexRtspConfControllerBandwidthDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 100000),
    )


_ApexRtspConfControllerBandwidthDelta_Type.__name__ = "Integer32"
_ApexRtspConfControllerBandwidthDelta_Object = MibTableColumn
apexRtspConfControllerBandwidthDelta = _ApexRtspConfControllerBandwidthDelta_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 3, 1, 5),
    _ApexRtspConfControllerBandwidthDelta_Type()
)
apexRtspConfControllerBandwidthDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControllerBandwidthDelta.setStatus("current")
_ApexRtspConfControlNamesTable_Object = MibTable
apexRtspConfControlNamesTable = _ApexRtspConfControlNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 4)
)
if mibBuilder.loadTexts:
    apexRtspConfControlNamesTable.setStatus("current")
_ApexRtspConfControlNamesEntry_Object = MibTableRow
apexRtspConfControlNamesEntry = _ApexRtspConfControlNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 4, 1)
)
apexRtspConfControlNamesEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfControlNamesNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfControlNamesEntry.setStatus("current")


class _ApexRtspConfControlNamesNum_Type(Integer32):
    """Custom type apexRtspConfControlNamesNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspConfControlNamesNum_Type.__name__ = "Integer32"
_ApexRtspConfControlNamesNum_Object = MibTableColumn
apexRtspConfControlNamesNum = _ApexRtspConfControlNamesNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 4, 1, 1),
    _ApexRtspConfControlNamesNum_Type()
)
apexRtspConfControlNamesNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfControlNamesNum.setStatus("current")


class _ApexRtspConfControlNamesStreamingZone_Type(DisplayString):
    """Custom type apexRtspConfControlNamesStreamingZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApexRtspConfControlNamesStreamingZone_Type.__name__ = "DisplayString"
_ApexRtspConfControlNamesStreamingZone_Object = MibTableColumn
apexRtspConfControlNamesStreamingZone = _ApexRtspConfControlNamesStreamingZone_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 4, 1, 2),
    _ApexRtspConfControlNamesStreamingZone_Type()
)
apexRtspConfControlNamesStreamingZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControlNamesStreamingZone.setStatus("current")


class _ApexRtspConfControlNamesDeviceName_Type(DisplayString):
    """Custom type apexRtspConfControlNamesDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApexRtspConfControlNamesDeviceName_Type.__name__ = "DisplayString"
_ApexRtspConfControlNamesDeviceName_Object = MibTableColumn
apexRtspConfControlNamesDeviceName = _ApexRtspConfControlNamesDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 4, 1, 3),
    _ApexRtspConfControlNamesDeviceName_Type()
)
apexRtspConfControlNamesDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfControlNamesDeviceName.setStatus("current")
_ApexRtspConfQamChannelApplyTable_Object = MibTable
apexRtspConfQamChannelApplyTable = _ApexRtspConfQamChannelApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 5)
)
if mibBuilder.loadTexts:
    apexRtspConfQamChannelApplyTable.setStatus("current")
_ApexRtspConfQamChannelApplyEntry_Object = MibTableRow
apexRtspConfQamChannelApplyEntry = _ApexRtspConfQamChannelApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 5, 1)
)
apexRtspConfQamChannelApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfQamChannelApplyNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfQamChannelApplyEntry.setStatus("current")


class _ApexRtspConfQamChannelApplyNum_Type(Integer32):
    """Custom type apexRtspConfQamChannelApplyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRtspConfQamChannelApplyNum_Type.__name__ = "Integer32"
_ApexRtspConfQamChannelApplyNum_Object = MibTableColumn
apexRtspConfQamChannelApplyNum = _ApexRtspConfQamChannelApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 5, 1, 1),
    _ApexRtspConfQamChannelApplyNum_Type()
)
apexRtspConfQamChannelApplyNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfQamChannelApplyNum.setStatus("current")
_ApexRtspConfQamChannelApplyChange_Type = ApplyDataToDeviceTYPE
_ApexRtspConfQamChannelApplyChange_Object = MibTableColumn
apexRtspConfQamChannelApplyChange = _ApexRtspConfQamChannelApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 5, 1, 2),
    _ApexRtspConfQamChannelApplyChange_Type()
)
apexRtspConfQamChannelApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfQamChannelApplyChange.setStatus("current")
_ApexRtspConfQamChannelTable_Object = MibTable
apexRtspConfQamChannelTable = _ApexRtspConfQamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 6)
)
if mibBuilder.loadTexts:
    apexRtspConfQamChannelTable.setStatus("current")
_ApexRtspConfQamChannelEntry_Object = MibTableRow
apexRtspConfQamChannelEntry = _ApexRtspConfQamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 6, 1)
)
apexRtspConfQamChannelEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfQamChannelNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfQamChannelEntry.setStatus("current")


class _ApexRtspConfQamChannelNum_Type(Integer32):
    """Custom type apexRtspConfQamChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRtspConfQamChannelNum_Type.__name__ = "Integer32"
_ApexRtspConfQamChannelNum_Object = MibTableColumn
apexRtspConfQamChannelNum = _ApexRtspConfQamChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 6, 1, 1),
    _ApexRtspConfQamChannelNum_Type()
)
apexRtspConfQamChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfQamChannelNum.setStatus("current")


class _ApexRtspConfQamChannelGroupName_Type(DisplayString):
    """Custom type apexRtspConfQamChannelGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApexRtspConfQamChannelGroupName_Type.__name__ = "DisplayString"
_ApexRtspConfQamChannelGroupName_Object = MibTableColumn
apexRtspConfQamChannelGroupName = _ApexRtspConfQamChannelGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 6, 1, 2),
    _ApexRtspConfQamChannelGroupName_Type()
)
apexRtspConfQamChannelGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfQamChannelGroupName.setStatus("current")
_ApexRtspConfGbeEdgeGroupTable_Object = MibTable
apexRtspConfGbeEdgeGroupTable = _ApexRtspConfGbeEdgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 7)
)
if mibBuilder.loadTexts:
    apexRtspConfGbeEdgeGroupTable.setStatus("current")
_ApexRtspConfGbeEdgeGroupEntry_Object = MibTableRow
apexRtspConfGbeEdgeGroupEntry = _ApexRtspConfGbeEdgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 7, 1)
)
apexRtspConfGbeEdgeGroupEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfGbeEdgeGroupNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfGbeEdgeGroupEntry.setStatus("current")


class _ApexRtspConfGbeEdgeGroupNum_Type(Integer32):
    """Custom type apexRtspConfGbeEdgeGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspConfGbeEdgeGroupNum_Type.__name__ = "Integer32"
_ApexRtspConfGbeEdgeGroupNum_Object = MibTableColumn
apexRtspConfGbeEdgeGroupNum = _ApexRtspConfGbeEdgeGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 7, 1, 1),
    _ApexRtspConfGbeEdgeGroupNum_Type()
)
apexRtspConfGbeEdgeGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfGbeEdgeGroupNum.setStatus("current")


class _ApexRtspConfGbeEdgeGroupName_Type(DisplayString):
    """Custom type apexRtspConfGbeEdgeGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApexRtspConfGbeEdgeGroupName_Type.__name__ = "DisplayString"
_ApexRtspConfGbeEdgeGroupName_Object = MibTableColumn
apexRtspConfGbeEdgeGroupName = _ApexRtspConfGbeEdgeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 7, 1, 2),
    _ApexRtspConfGbeEdgeGroupName_Type()
)
apexRtspConfGbeEdgeGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfGbeEdgeGroupName.setStatus("current")
_ApexRtspConfMhaTable_Object = MibTable
apexRtspConfMhaTable = _ApexRtspConfMhaTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 8)
)
if mibBuilder.loadTexts:
    apexRtspConfMhaTable.setStatus("current")
_ApexRtspConfMhaEntry_Object = MibTableRow
apexRtspConfMhaEntry = _ApexRtspConfMhaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 8, 1)
)
apexRtspConfMhaEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspConfMhaNum"),
)
if mibBuilder.loadTexts:
    apexRtspConfMhaEntry.setStatus("current")


class _ApexRtspConfMhaNum_Type(Integer32):
    """Custom type apexRtspConfMhaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspConfMhaNum_Type.__name__ = "Integer32"
_ApexRtspConfMhaNum_Object = MibTableColumn
apexRtspConfMhaNum = _ApexRtspConfMhaNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 8, 1, 1),
    _ApexRtspConfMhaNum_Type()
)
apexRtspConfMhaNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspConfMhaNum.setStatus("current")


class _ApexRtspConfMhaAddressDomain_Type(Integer32):
    """Custom type apexRtspConfMhaAddressDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexRtspConfMhaAddressDomain_Type.__name__ = "Integer32"
_ApexRtspConfMhaAddressDomain_Object = MibTableColumn
apexRtspConfMhaAddressDomain = _ApexRtspConfMhaAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 8, 1, 2),
    _ApexRtspConfMhaAddressDomain_Type()
)
apexRtspConfMhaAddressDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaAddressDomain.setStatus("current")


class _ApexRtspConfMhaPort_Type(Integer32):
    """Custom type apexRtspConfMhaPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApexRtspConfMhaPort_Type.__name__ = "Integer32"
_ApexRtspConfMhaPort_Object = MibTableColumn
apexRtspConfMhaPort = _ApexRtspConfMhaPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 8, 1, 3),
    _ApexRtspConfMhaPort_Type()
)
apexRtspConfMhaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaPort.setStatus("current")
_ApexRtspConfMhaGeneral_ObjectIdentity = ObjectIdentity
apexRtspConfMhaGeneral = _ApexRtspConfMhaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 9)
)
_ApexRtspConfMhaUdpMapEnable_Type = EnableDisableTYPE
_ApexRtspConfMhaUdpMapEnable_Object = MibScalar
apexRtspConfMhaUdpMapEnable = _ApexRtspConfMhaUdpMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 9, 1),
    _ApexRtspConfMhaUdpMapEnable_Type()
)
apexRtspConfMhaUdpMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaUdpMapEnable.setStatus("current")
_ApexRtspConfMhaSbe_ObjectIdentity = ObjectIdentity
apexRtspConfMhaSbe = _ApexRtspConfMhaSbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10)
)


class _ApexRtspConfMhaSbeEncryptionMode_Type(Integer32):
    """Custom type apexRtspConfMhaSbeEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpk", 3),
          ("full", 1),
          ("fwk", 2))
    )


_ApexRtspConfMhaSbeEncryptionMode_Type.__name__ = "Integer32"
_ApexRtspConfMhaSbeEncryptionMode_Object = MibScalar
apexRtspConfMhaSbeEncryptionMode = _ApexRtspConfMhaSbeEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10, 1),
    _ApexRtspConfMhaSbeEncryptionMode_Type()
)
apexRtspConfMhaSbeEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaSbeEncryptionMode.setStatus("current")


class _ApexRtspConfMhaSbeCciLevel_Type(Integer32):
    """Custom type apexRtspConfMhaSbeCciLevel based on Integer32"""
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
        *(("copyFreely", 2),
          ("copyNever", 4),
          ("copyOnce", 3),
          ("noMoreCopies", 5),
          ("notDefined", 1))
    )


_ApexRtspConfMhaSbeCciLevel_Type.__name__ = "Integer32"
_ApexRtspConfMhaSbeCciLevel_Object = MibScalar
apexRtspConfMhaSbeCciLevel = _ApexRtspConfMhaSbeCciLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10, 2),
    _ApexRtspConfMhaSbeCciLevel_Type()
)
apexRtspConfMhaSbeCciLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaSbeCciLevel.setStatus("current")


class _ApexRtspConfMhaSbeApsLevel_Type(Integer32):
    """Custom type apexRtspConfMhaSbeApsLevel based on Integer32"""
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
        *(("notDefined", 1),
          ("off", 2),
          ("splitBurst2Line", 4),
          ("splitBurst4Line", 5),
          ("splitBurstOff", 3))
    )


_ApexRtspConfMhaSbeApsLevel_Type.__name__ = "Integer32"
_ApexRtspConfMhaSbeApsLevel_Object = MibScalar
apexRtspConfMhaSbeApsLevel = _ApexRtspConfMhaSbeApsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10, 3),
    _ApexRtspConfMhaSbeApsLevel_Type()
)
apexRtspConfMhaSbeApsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaSbeApsLevel.setStatus("current")


class _ApexRtspConfMhaSbeCitSetting_Type(Integer32):
    """Custom type apexRtspConfMhaSbeCitSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApexRtspConfMhaSbeCitSetting_Type.__name__ = "Integer32"
_ApexRtspConfMhaSbeCitSetting_Object = MibScalar
apexRtspConfMhaSbeCitSetting = _ApexRtspConfMhaSbeCitSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10, 4),
    _ApexRtspConfMhaSbeCitSetting_Type()
)
apexRtspConfMhaSbeCitSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaSbeCitSetting.setStatus("current")
_ApexRtspConfMhaSbeApplyChange_Type = ApplyDataToDeviceTYPE
_ApexRtspConfMhaSbeApplyChange_Object = MibScalar
apexRtspConfMhaSbeApplyChange = _ApexRtspConfMhaSbeApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 1, 10, 5),
    _ApexRtspConfMhaSbeApplyChange_Type()
)
apexRtspConfMhaSbeApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRtspConfMhaSbeApplyChange.setStatus("current")
_ApexRtspStatus_ObjectIdentity = ObjectIdentity
apexRtspStatus = _ApexRtspStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2)
)
_ApexRtspStatusGeneral_ObjectIdentity = ObjectIdentity
apexRtspStatusGeneral = _ApexRtspStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 1)
)
_ApexRtspSessionStatTable_Object = MibTable
apexRtspSessionStatTable = _ApexRtspSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2)
)
if mibBuilder.loadTexts:
    apexRtspSessionStatTable.setStatus("current")
_ApexRtspSessionStatEntry_Object = MibTableRow
apexRtspSessionStatEntry = _ApexRtspSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1)
)
apexRtspSessionStatEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspSessionStatIndex"),
)
if mibBuilder.loadTexts:
    apexRtspSessionStatEntry.setStatus("current")


class _ApexRtspSessionStatIndex_Type(Integer32):
    """Custom type apexRtspSessionStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexRtspSessionStatIndex_Type.__name__ = "Integer32"
_ApexRtspSessionStatIndex_Object = MibTableColumn
apexRtspSessionStatIndex = _ApexRtspSessionStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 1),
    _ApexRtspSessionStatIndex_Type()
)
apexRtspSessionStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspSessionStatIndex.setStatus("current")
_ApexRtspSessionStatInputTsIndex_Type = Integer32
_ApexRtspSessionStatInputTsIndex_Object = MibTableColumn
apexRtspSessionStatInputTsIndex = _ApexRtspSessionStatInputTsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 2),
    _ApexRtspSessionStatInputTsIndex_Type()
)
apexRtspSessionStatInputTsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatInputTsIndex.setStatus("current")
_ApexRtspSessionStatInputProgramNum_Type = Integer32
_ApexRtspSessionStatInputProgramNum_Object = MibTableColumn
apexRtspSessionStatInputProgramNum = _ApexRtspSessionStatInputProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 3),
    _ApexRtspSessionStatInputProgramNum_Type()
)
apexRtspSessionStatInputProgramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatInputProgramNum.setStatus("current")
_ApexRtspSessionStatOutputQamChannel_Type = Integer32
_ApexRtspSessionStatOutputQamChannel_Object = MibTableColumn
apexRtspSessionStatOutputQamChannel = _ApexRtspSessionStatOutputQamChannel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 4),
    _ApexRtspSessionStatOutputQamChannel_Type()
)
apexRtspSessionStatOutputQamChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatOutputQamChannel.setStatus("current")
_ApexRtspSessionStatOutputProgramNum_Type = Integer32
_ApexRtspSessionStatOutputProgramNum_Object = MibTableColumn
apexRtspSessionStatOutputProgramNum = _ApexRtspSessionStatOutputProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 5),
    _ApexRtspSessionStatOutputProgramNum_Type()
)
apexRtspSessionStatOutputProgramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatOutputProgramNum.setStatus("current")
_ApexRtspSessionStatProgramBandwidth_Type = Integer32
_ApexRtspSessionStatProgramBandwidth_Object = MibTableColumn
apexRtspSessionStatProgramBandwidth = _ApexRtspSessionStatProgramBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 6),
    _ApexRtspSessionStatProgramBandwidth_Type()
)
apexRtspSessionStatProgramBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatProgramBandwidth.setStatus("current")
_ApexRtspSessionStatManagerIpAddr_Type = IpAddress
_ApexRtspSessionStatManagerIpAddr_Object = MibTableColumn
apexRtspSessionStatManagerIpAddr = _ApexRtspSessionStatManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 2, 1, 7),
    _ApexRtspSessionStatManagerIpAddr_Type()
)
apexRtspSessionStatManagerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionStatManagerIpAddr.setStatus("current")
_ApexRtspSessionIdTable_Object = MibTable
apexRtspSessionIdTable = _ApexRtspSessionIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 3)
)
if mibBuilder.loadTexts:
    apexRtspSessionIdTable.setStatus("current")
_ApexRtspSessionIdEntry_Object = MibTableRow
apexRtspSessionIdEntry = _ApexRtspSessionIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 3, 1)
)
apexRtspSessionIdEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspSessionIdIndex"),
)
if mibBuilder.loadTexts:
    apexRtspSessionIdEntry.setStatus("current")


class _ApexRtspSessionIdIndex_Type(Integer32):
    """Custom type apexRtspSessionIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexRtspSessionIdIndex_Type.__name__ = "Integer32"
_ApexRtspSessionIdIndex_Object = MibTableColumn
apexRtspSessionIdIndex = _ApexRtspSessionIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 3, 1, 1),
    _ApexRtspSessionIdIndex_Type()
)
apexRtspSessionIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspSessionIdIndex.setStatus("current")


class _ApexRtspSessionId_Type(DisplayString):
    """Custom type apexRtspSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexRtspSessionId_Type.__name__ = "DisplayString"
_ApexRtspSessionId_Object = MibTableColumn
apexRtspSessionId = _ApexRtspSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 3, 1, 2),
    _ApexRtspSessionId_Type()
)
apexRtspSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspSessionId.setStatus("current")
_ApexRtspQamStatTable_Object = MibTable
apexRtspQamStatTable = _ApexRtspQamStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 4)
)
if mibBuilder.loadTexts:
    apexRtspQamStatTable.setStatus("current")
_ApexRtspQamStatEntry_Object = MibTableRow
apexRtspQamStatEntry = _ApexRtspQamStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 4, 1)
)
apexRtspQamStatEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspQamStatQamChannelNum"),
)
if mibBuilder.loadTexts:
    apexRtspQamStatEntry.setStatus("current")


class _ApexRtspQamStatQamChannelNum_Type(Integer32):
    """Custom type apexRtspQamStatQamChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRtspQamStatQamChannelNum_Type.__name__ = "Integer32"
_ApexRtspQamStatQamChannelNum_Object = MibTableColumn
apexRtspQamStatQamChannelNum = _ApexRtspQamStatQamChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 4, 1, 1),
    _ApexRtspQamStatQamChannelNum_Type()
)
apexRtspQamStatQamChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspQamStatQamChannelNum.setStatus("current")
_ApexRtspQamStatNumSessions_Type = Integer32
_ApexRtspQamStatNumSessions_Object = MibTableColumn
apexRtspQamStatNumSessions = _ApexRtspQamStatNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 4, 1, 2),
    _ApexRtspQamStatNumSessions_Type()
)
apexRtspQamStatNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspQamStatNumSessions.setStatus("current")
_ApexRtspQamStatAllocatedBandwidth_Type = Unsigned32
_ApexRtspQamStatAllocatedBandwidth_Object = MibTableColumn
apexRtspQamStatAllocatedBandwidth = _ApexRtspQamStatAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 4, 1, 3),
    _ApexRtspQamStatAllocatedBandwidth_Type()
)
apexRtspQamStatAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspQamStatAllocatedBandwidth.setStatus("current")
_ApexRtspStatControllerTable_Object = MibTable
apexRtspStatControllerTable = _ApexRtspStatControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5)
)
if mibBuilder.loadTexts:
    apexRtspStatControllerTable.setStatus("current")
_ApexRtspStatControllerEntry_Object = MibTableRow
apexRtspStatControllerEntry = _ApexRtspStatControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5, 1)
)
apexRtspStatControllerEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspStatControllerNum"),
)
if mibBuilder.loadTexts:
    apexRtspStatControllerEntry.setStatus("current")


class _ApexRtspStatControllerNum_Type(Integer32):
    """Custom type apexRtspStatControllerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexRtspStatControllerNum_Type.__name__ = "Integer32"
_ApexRtspStatControllerNum_Object = MibTableColumn
apexRtspStatControllerNum = _ApexRtspStatControllerNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5, 1, 1),
    _ApexRtspStatControllerNum_Type()
)
apexRtspStatControllerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspStatControllerNum.setStatus("current")


class _ApexRtspStatControllerDiscovery_Type(Integer32):
    """Custom type apexRtspStatControllerDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("discovered", 2),
          ("discoveredAnotB", 4),
          ("discoveredBnotA", 5),
          ("discoveredConnectionLost", 3),
          ("notApplicable", 0),
          ("notDiscovered", 1))
    )


_ApexRtspStatControllerDiscovery_Type.__name__ = "Integer32"
_ApexRtspStatControllerDiscovery_Object = MibTableColumn
apexRtspStatControllerDiscovery = _ApexRtspStatControllerDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5, 1, 2),
    _ApexRtspStatControllerDiscovery_Type()
)
apexRtspStatControllerDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspStatControllerDiscovery.setStatus("current")


class _ApexRtspStatControllerConnection_Type(Integer32):
    """Custom type apexRtspStatControllerConnection based on Integer32"""
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
        *(("connected", 2),
          ("connectedPort2048", 4),
          ("connectedPort554", 3),
          ("notApplicable", 0),
          ("notConnected", 1))
    )


_ApexRtspStatControllerConnection_Type.__name__ = "Integer32"
_ApexRtspStatControllerConnection_Object = MibTableColumn
apexRtspStatControllerConnection = _ApexRtspStatControllerConnection_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5, 1, 3),
    _ApexRtspStatControllerConnection_Type()
)
apexRtspStatControllerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspStatControllerConnection.setStatus("current")


class _ApexRtspStatControllerCommFault_Type(Integer32):
    """Custom type apexRtspStatControllerCommFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexRtspStatControllerCommFault_Type.__name__ = "Integer32"
_ApexRtspStatControllerCommFault_Object = MibTableColumn
apexRtspStatControllerCommFault = _ApexRtspStatControllerCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 5, 1, 4),
    _ApexRtspStatControllerCommFault_Type()
)
apexRtspStatControllerCommFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspStatControllerCommFault.setStatus("current")
_ApexRtspStatQamChannelTable_Object = MibTable
apexRtspStatQamChannelTable = _ApexRtspStatQamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 6)
)
if mibBuilder.loadTexts:
    apexRtspStatQamChannelTable.setStatus("current")
_ApexRtspStatQamChannelEntry_Object = MibTableRow
apexRtspStatQamChannelEntry = _ApexRtspStatQamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 6, 1)
)
apexRtspStatQamChannelEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspStatQamChannelNum"),
)
if mibBuilder.loadTexts:
    apexRtspStatQamChannelEntry.setStatus("current")


class _ApexRtspStatQamChannelNum_Type(Integer32):
    """Custom type apexRtspStatQamChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRtspStatQamChannelNum_Type.__name__ = "Integer32"
_ApexRtspStatQamChannelNum_Object = MibTableColumn
apexRtspStatQamChannelNum = _ApexRtspStatQamChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 6, 1, 1),
    _ApexRtspStatQamChannelNum_Type()
)
apexRtspStatQamChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspStatQamChannelNum.setStatus("current")


class _ApexRtspStatQamChannelName_Type(DisplayString):
    """Custom type apexRtspStatQamChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApexRtspStatQamChannelName_Type.__name__ = "DisplayString"
_ApexRtspStatQamChannelName_Object = MibTableColumn
apexRtspStatQamChannelName = _ApexRtspStatQamChannelName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 6, 1, 2),
    _ApexRtspStatQamChannelName_Type()
)
apexRtspStatQamChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspStatQamChannelName.setStatus("current")
_ApexRtspStatQamMptsModeTable_Object = MibTable
apexRtspStatQamMptsModeTable = _ApexRtspStatQamMptsModeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 7)
)
if mibBuilder.loadTexts:
    apexRtspStatQamMptsModeTable.setStatus("current")
_ApexRtspStatQamMptsModeEntry_Object = MibTableRow
apexRtspStatQamMptsModeEntry = _ApexRtspStatQamMptsModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 7, 1)
)
apexRtspStatQamMptsModeEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspStatQamMptsModeQamChannelNum"),
)
if mibBuilder.loadTexts:
    apexRtspStatQamMptsModeEntry.setStatus("current")


class _ApexRtspStatQamMptsModeQamChannelNum_Type(Integer32):
    """Custom type apexRtspStatQamMptsModeQamChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRtspStatQamMptsModeQamChannelNum_Type.__name__ = "Integer32"
_ApexRtspStatQamMptsModeQamChannelNum_Object = MibTableColumn
apexRtspStatQamMptsModeQamChannelNum = _ApexRtspStatQamMptsModeQamChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 7, 1, 1),
    _ApexRtspStatQamMptsModeQamChannelNum_Type()
)
apexRtspStatQamMptsModeQamChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspStatQamMptsModeQamChannelNum.setStatus("current")


class _ApexRtspStatQamMptsModeQamChannelMode_Type(Integer32):
    """Custom type apexRtspStatQamMptsModeQamChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiplexing", 2),
          ("notApplicable", 0),
          ("passthrough", 1))
    )


_ApexRtspStatQamMptsModeQamChannelMode_Type.__name__ = "Integer32"
_ApexRtspStatQamMptsModeQamChannelMode_Object = MibTableColumn
apexRtspStatQamMptsModeQamChannelMode = _ApexRtspStatQamMptsModeQamChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 9, 4, 2, 7, 1, 2),
    _ApexRtspStatQamMptsModeQamChannelMode_Type()
)
apexRtspStatQamMptsModeQamChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspStatQamMptsModeQamChannelMode.setStatus("current")
_ApexManualRouting_ObjectIdentity = ObjectIdentity
apexManualRouting = _ApexManualRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10)
)
_ApexManualRoutingConfig_ObjectIdentity = ObjectIdentity
apexManualRoutingConfig = _ApexManualRoutingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1)
)
_ApexManualRoutingConfigGeneral_ObjectIdentity = ObjectIdentity
apexManualRoutingConfigGeneral = _ApexManualRoutingConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 1)
)
_ApexManualRouteRmdClear_Type = ApplyDataToDeviceTYPE
_ApexManualRouteRmdClear_Object = MibScalar
apexManualRouteRmdClear = _ApexManualRouteRmdClear_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 1, 1),
    _ApexManualRouteRmdClear_Type()
)
apexManualRouteRmdClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteRmdClear.setStatus("current")
_ApexManualRouteApplyTable_Object = MibTable
apexManualRouteApplyTable = _ApexManualRouteApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 2)
)
if mibBuilder.loadTexts:
    apexManualRouteApplyTable.setStatus("current")
_ApexManualRouteApplyEntry_Object = MibTableRow
apexManualRouteApplyEntry = _ApexManualRouteApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 2, 1)
)
apexManualRouteApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexManualRouteApplyIndex"),
)
if mibBuilder.loadTexts:
    apexManualRouteApplyEntry.setStatus("current")


class _ApexManualRouteApplyIndex_Type(Integer32):
    """Custom type apexManualRouteApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManualRouteApplyIndex_Type.__name__ = "Integer32"
_ApexManualRouteApplyIndex_Object = MibTableColumn
apexManualRouteApplyIndex = _ApexManualRouteApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 2, 1, 1),
    _ApexManualRouteApplyIndex_Type()
)
apexManualRouteApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManualRouteApplyIndex.setStatus("current")
_ApexManualRouteApplyChange_Type = ApplyDataToDeviceTYPE
_ApexManualRouteApplyChange_Object = MibTableColumn
apexManualRouteApplyChange = _ApexManualRouteApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 2, 1, 2),
    _ApexManualRouteApplyChange_Type()
)
apexManualRouteApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteApplyChange.setStatus("current")
_ApexManualRouteTable_Object = MibTable
apexManualRouteTable = _ApexManualRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3)
)
if mibBuilder.loadTexts:
    apexManualRouteTable.setStatus("current")
_ApexManualRouteEntry_Object = MibTableRow
apexManualRouteEntry = _ApexManualRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1)
)
apexManualRouteEntry.setIndexNames(
    (0, "APEX-MIB", "apexManualRouteIndex"),
)
if mibBuilder.loadTexts:
    apexManualRouteEntry.setStatus("current")


class _ApexManualRouteIndex_Type(Integer32):
    """Custom type apexManualRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManualRouteIndex_Type.__name__ = "Integer32"
_ApexManualRouteIndex_Object = MibTableColumn
apexManualRouteIndex = _ApexManualRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 1),
    _ApexManualRouteIndex_Type()
)
apexManualRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManualRouteIndex.setStatus("current")
_ApexManualRouteEnable_Type = EnableDisableTYPE
_ApexManualRouteEnable_Object = MibTableColumn
apexManualRouteEnable = _ApexManualRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 2),
    _ApexManualRouteEnable_Type()
)
apexManualRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteEnable.setStatus("current")


class _ApexManualRouteInputType_Type(Integer32):
    """Custom type apexManualRouteInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1))
    )


_ApexManualRouteInputType_Type.__name__ = "Integer32"
_ApexManualRouteInputType_Object = MibTableColumn
apexManualRouteInputType = _ApexManualRouteInputType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 3),
    _ApexManualRouteInputType_Type()
)
apexManualRouteInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputType.setStatus("current")


class _ApexManualRouteInputInterface_Type(Integer32):
    """Custom type apexManualRouteInputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexManualRouteInputInterface_Type.__name__ = "Integer32"
_ApexManualRouteInputInterface_Object = MibTableColumn
apexManualRouteInputInterface = _ApexManualRouteInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 4),
    _ApexManualRouteInputInterface_Type()
)
apexManualRouteInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputInterface.setStatus("current")


class _ApexManualRouteInputUdp_Type(Integer32):
    """Custom type apexManualRouteInputUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManualRouteInputUdp_Type.__name__ = "Integer32"
_ApexManualRouteInputUdp_Object = MibTableColumn
apexManualRouteInputUdp = _ApexManualRouteInputUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 5),
    _ApexManualRouteInputUdp_Type()
)
apexManualRouteInputUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputUdp.setStatus("current")
_ApexManualRouteInputMulticastIp_Type = IpAddress
_ApexManualRouteInputMulticastIp_Object = MibTableColumn
apexManualRouteInputMulticastIp = _ApexManualRouteInputMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 6),
    _ApexManualRouteInputMulticastIp_Type()
)
apexManualRouteInputMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputMulticastIp.setStatus("current")
_ApexManualRouteInputSourceIp_Type = IpAddress
_ApexManualRouteInputSourceIp_Object = MibTableColumn
apexManualRouteInputSourceIp = _ApexManualRouteInputSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 7),
    _ApexManualRouteInputSourceIp_Type()
)
apexManualRouteInputSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputSourceIp.setStatus("current")


class _ApexManualRouteInputProgNum_Type(Integer32):
    """Custom type apexManualRouteInputProgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManualRouteInputProgNum_Type.__name__ = "Integer32"
_ApexManualRouteInputProgNum_Object = MibTableColumn
apexManualRouteInputProgNum = _ApexManualRouteInputProgNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 8),
    _ApexManualRouteInputProgNum_Type()
)
apexManualRouteInputProgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputProgNum.setStatus("current")
_ApexManualRouteInputPreEncryptCheck_Type = EnableDisableTYPE
_ApexManualRouteInputPreEncryptCheck_Object = MibTableColumn
apexManualRouteInputPreEncryptCheck = _ApexManualRouteInputPreEncryptCheck_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 9),
    _ApexManualRouteInputPreEncryptCheck_Type()
)
apexManualRouteInputPreEncryptCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteInputPreEncryptCheck.setStatus("current")


class _ApexManualRouteOutputTsNum_Type(Integer32):
    """Custom type apexManualRouteOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexManualRouteOutputTsNum_Type.__name__ = "Integer32"
_ApexManualRouteOutputTsNum_Object = MibTableColumn
apexManualRouteOutputTsNum = _ApexManualRouteOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 10),
    _ApexManualRouteOutputTsNum_Type()
)
apexManualRouteOutputTsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteOutputTsNum.setStatus("current")


class _ApexManualRouteOutputProgNum_Type(Integer32):
    """Custom type apexManualRouteOutputProgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManualRouteOutputProgNum_Type.__name__ = "Integer32"
_ApexManualRouteOutputProgNum_Object = MibTableColumn
apexManualRouteOutputProgNum = _ApexManualRouteOutputProgNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 11),
    _ApexManualRouteOutputProgNum_Type()
)
apexManualRouteOutputProgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteOutputProgNum.setStatus("current")


class _ApexManualRouteOutputEncryptMode_Type(Integer32):
    """Custom type apexManualRouteOutputEncryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ApexManualRouteOutputEncryptMode_Type.__name__ = "Integer32"
_ApexManualRouteOutputEncryptMode_Object = MibTableColumn
apexManualRouteOutputEncryptMode = _ApexManualRouteOutputEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 12),
    _ApexManualRouteOutputEncryptMode_Type()
)
apexManualRouteOutputEncryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteOutputEncryptMode.setStatus("current")


class _ApexManualRouteOutputCopyProtectSource_Type(Integer32):
    """Custom type apexManualRouteOutputCopyProtectSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuredSource", 2),
          ("followInputDtcp", 1))
    )


_ApexManualRouteOutputCopyProtectSource_Type.__name__ = "Integer32"
_ApexManualRouteOutputCopyProtectSource_Object = MibTableColumn
apexManualRouteOutputCopyProtectSource = _ApexManualRouteOutputCopyProtectSource_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 13),
    _ApexManualRouteOutputCopyProtectSource_Type()
)
apexManualRouteOutputCopyProtectSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteOutputCopyProtectSource.setStatus("current")


class _ApexManualRouteSourceId_Type(Integer32):
    """Custom type apexManualRouteSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManualRouteSourceId_Type.__name__ = "Integer32"
_ApexManualRouteSourceId_Object = MibTableColumn
apexManualRouteSourceId = _ApexManualRouteSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 14),
    _ApexManualRouteSourceId_Type()
)
apexManualRouteSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteSourceId.setStatus("current")


class _ApexManualRouteProviderId_Type(Integer32):
    """Custom type apexManualRouteProviderId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManualRouteProviderId_Type.__name__ = "Integer32"
_ApexManualRouteProviderId_Object = MibTableColumn
apexManualRouteProviderId = _ApexManualRouteProviderId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 3, 1, 15),
    _ApexManualRouteProviderId_Type()
)
apexManualRouteProviderId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManualRouteProviderId.setStatus("current")
_ApexManRtePassThroughApplyTable_Object = MibTable
apexManRtePassThroughApplyTable = _ApexManRtePassThroughApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 4)
)
if mibBuilder.loadTexts:
    apexManRtePassThroughApplyTable.setStatus("current")
_ApexManRtePassThroughApplyEntry_Object = MibTableRow
apexManRtePassThroughApplyEntry = _ApexManRtePassThroughApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 4, 1)
)
apexManRtePassThroughApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRtePassThroughApplyOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexManRtePassThroughApplyEntry.setStatus("current")


class _ApexManRtePassThroughApplyOutputTsNum_Type(Integer32):
    """Custom type apexManRtePassThroughApplyOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexManRtePassThroughApplyOutputTsNum_Type.__name__ = "Integer32"
_ApexManRtePassThroughApplyOutputTsNum_Object = MibTableColumn
apexManRtePassThroughApplyOutputTsNum = _ApexManRtePassThroughApplyOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 4, 1, 1),
    _ApexManRtePassThroughApplyOutputTsNum_Type()
)
apexManRtePassThroughApplyOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRtePassThroughApplyOutputTsNum.setStatus("current")
_ApexManRtePassThroughApplyChange_Type = ApplyDataToDeviceTYPE
_ApexManRtePassThroughApplyChange_Object = MibTableColumn
apexManRtePassThroughApplyChange = _ApexManRtePassThroughApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 4, 1, 2),
    _ApexManRtePassThroughApplyChange_Type()
)
apexManRtePassThroughApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughApplyChange.setStatus("current")
_ApexManRtePassThroughTable_Object = MibTable
apexManRtePassThroughTable = _ApexManRtePassThroughTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5)
)
if mibBuilder.loadTexts:
    apexManRtePassThroughTable.setStatus("current")
_ApexManRtePassThroughEntry_Object = MibTableRow
apexManRtePassThroughEntry = _ApexManRtePassThroughEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1)
)
apexManRtePassThroughEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRtePassThroughOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexManRtePassThroughEntry.setStatus("current")


class _ApexManRtePassThroughOutputTsNum_Type(Integer32):
    """Custom type apexManRtePassThroughOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexManRtePassThroughOutputTsNum_Type.__name__ = "Integer32"
_ApexManRtePassThroughOutputTsNum_Object = MibTableColumn
apexManRtePassThroughOutputTsNum = _ApexManRtePassThroughOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 1),
    _ApexManRtePassThroughOutputTsNum_Type()
)
apexManRtePassThroughOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRtePassThroughOutputTsNum.setStatus("current")
_ApexManRtePassThroughEnable_Type = EnableDisableTYPE
_ApexManRtePassThroughEnable_Object = MibTableColumn
apexManRtePassThroughEnable = _ApexManRtePassThroughEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 2),
    _ApexManRtePassThroughEnable_Type()
)
apexManRtePassThroughEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughEnable.setStatus("current")


class _ApexManRtePassThroughInputType_Type(Integer32):
    """Custom type apexManRtePassThroughInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1))
    )


_ApexManRtePassThroughInputType_Type.__name__ = "Integer32"
_ApexManRtePassThroughInputType_Object = MibTableColumn
apexManRtePassThroughInputType = _ApexManRtePassThroughInputType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 3),
    _ApexManRtePassThroughInputType_Type()
)
apexManRtePassThroughInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughInputType.setStatus("current")


class _ApexManRtePassThroughInputInterface_Type(Integer32):
    """Custom type apexManRtePassThroughInputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexManRtePassThroughInputInterface_Type.__name__ = "Integer32"
_ApexManRtePassThroughInputInterface_Object = MibTableColumn
apexManRtePassThroughInputInterface = _ApexManRtePassThroughInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 4),
    _ApexManRtePassThroughInputInterface_Type()
)
apexManRtePassThroughInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughInputInterface.setStatus("current")


class _ApexManRtePassThroughInputUdp_Type(Integer32):
    """Custom type apexManRtePassThroughInputUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManRtePassThroughInputUdp_Type.__name__ = "Integer32"
_ApexManRtePassThroughInputUdp_Object = MibTableColumn
apexManRtePassThroughInputUdp = _ApexManRtePassThroughInputUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 5),
    _ApexManRtePassThroughInputUdp_Type()
)
apexManRtePassThroughInputUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughInputUdp.setStatus("current")
_ApexManRtePassThroughInputMulticastIp_Type = IpAddress
_ApexManRtePassThroughInputMulticastIp_Object = MibTableColumn
apexManRtePassThroughInputMulticastIp = _ApexManRtePassThroughInputMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 6),
    _ApexManRtePassThroughInputMulticastIp_Type()
)
apexManRtePassThroughInputMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughInputMulticastIp.setStatus("current")
_ApexManRtePassThroughInputSourceIp_Type = IpAddress
_ApexManRtePassThroughInputSourceIp_Object = MibTableColumn
apexManRtePassThroughInputSourceIp = _ApexManRtePassThroughInputSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 5, 1, 7),
    _ApexManRtePassThroughInputSourceIp_Type()
)
apexManRtePassThroughInputSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRtePassThroughInputSourceIp.setStatus("current")
_ApexManualRouteGbeInputRedundConfig_ObjectIdentity = ObjectIdentity
apexManualRouteGbeInputRedundConfig = _ApexManualRouteGbeInputRedundConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6)
)
_ApexManRteGbeInRedConfigGeneral_ObjectIdentity = ObjectIdentity
apexManRteGbeInRedConfigGeneral = _ApexManRteGbeInRedConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 1)
)
_ApexManRteGbeInRedApplyTable_Object = MibTable
apexManRteGbeInRedApplyTable = _ApexManRteGbeInRedApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedApplyTable.setStatus("current")
_ApexManRteGbeInRedApplyEntry_Object = MibTableRow
apexManRteGbeInRedApplyEntry = _ApexManRteGbeInRedApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 2, 1)
)
apexManRteGbeInRedApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRteGbeInRedApplyIndex"),
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedApplyEntry.setStatus("current")


class _ApexManRteGbeInRedApplyIndex_Type(Integer32):
    """Custom type apexManRteGbeInRedApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManRteGbeInRedApplyIndex_Type.__name__ = "Integer32"
_ApexManRteGbeInRedApplyIndex_Object = MibTableColumn
apexManRteGbeInRedApplyIndex = _ApexManRteGbeInRedApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 2, 1, 1),
    _ApexManRteGbeInRedApplyIndex_Type()
)
apexManRteGbeInRedApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRteGbeInRedApplyIndex.setStatus("current")
_ApexManRteGbeInRedApplyChange_Type = ApplyDataToDeviceTYPE
_ApexManRteGbeInRedApplyChange_Object = MibTableColumn
apexManRteGbeInRedApplyChange = _ApexManRteGbeInRedApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 2, 1, 2),
    _ApexManRteGbeInRedApplyChange_Type()
)
apexManRteGbeInRedApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedApplyChange.setStatus("current")
_ApexManRteGbeInRedTable_Object = MibTable
apexManRteGbeInRedTable = _ApexManRteGbeInRedTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3)
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedTable.setStatus("current")
_ApexManRteGbeInRedEntry_Object = MibTableRow
apexManRteGbeInRedEntry = _ApexManRteGbeInRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1)
)
apexManRteGbeInRedEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRteGbeInRedIndex"),
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedEntry.setStatus("current")


class _ApexManRteGbeInRedIndex_Type(Integer32):
    """Custom type apexManRteGbeInRedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManRteGbeInRedIndex_Type.__name__ = "Integer32"
_ApexManRteGbeInRedIndex_Object = MibTableColumn
apexManRteGbeInRedIndex = _ApexManRteGbeInRedIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 1),
    _ApexManRteGbeInRedIndex_Type()
)
apexManRteGbeInRedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRteGbeInRedIndex.setStatus("current")


class _ApexManRteGbeInRedPriInterface_Type(Integer32):
    """Custom type apexManRteGbeInRedPriInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexManRteGbeInRedPriInterface_Type.__name__ = "Integer32"
_ApexManRteGbeInRedPriInterface_Object = MibTableColumn
apexManRteGbeInRedPriInterface = _ApexManRteGbeInRedPriInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 2),
    _ApexManRteGbeInRedPriInterface_Type()
)
apexManRteGbeInRedPriInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriInterface.setStatus("current")


class _ApexManRteGbeInRedPriUdp_Type(Integer32):
    """Custom type apexManRteGbeInRedPriUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManRteGbeInRedPriUdp_Type.__name__ = "Integer32"
_ApexManRteGbeInRedPriUdp_Object = MibTableColumn
apexManRteGbeInRedPriUdp = _ApexManRteGbeInRedPriUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 3),
    _ApexManRteGbeInRedPriUdp_Type()
)
apexManRteGbeInRedPriUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriUdp.setStatus("current")
_ApexManRteGbeInRedPriMulticastIp_Type = IpAddress
_ApexManRteGbeInRedPriMulticastIp_Object = MibTableColumn
apexManRteGbeInRedPriMulticastIp = _ApexManRteGbeInRedPriMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 4),
    _ApexManRteGbeInRedPriMulticastIp_Type()
)
apexManRteGbeInRedPriMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriMulticastIp.setStatus("current")
_ApexManRteGbeInRedPriSourceIp_Type = IpAddress
_ApexManRteGbeInRedPriSourceIp_Object = MibTableColumn
apexManRteGbeInRedPriSourceIp = _ApexManRteGbeInRedPriSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 5),
    _ApexManRteGbeInRedPriSourceIp_Type()
)
apexManRteGbeInRedPriSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriSourceIp.setStatus("current")
_ApexManRteGbeInRedPriLowAlarmBitRate_Type = Integer32
_ApexManRteGbeInRedPriLowAlarmBitRate_Object = MibTableColumn
apexManRteGbeInRedPriLowAlarmBitRate = _ApexManRteGbeInRedPriLowAlarmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 6),
    _ApexManRteGbeInRedPriLowAlarmBitRate_Type()
)
apexManRteGbeInRedPriLowAlarmBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriLowAlarmBitRate.setStatus("current")
_ApexManRteGbeInRedPriHighAlarmBitRate_Type = Integer32
_ApexManRteGbeInRedPriHighAlarmBitRate_Object = MibTableColumn
apexManRteGbeInRedPriHighAlarmBitRate = _ApexManRteGbeInRedPriHighAlarmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 7),
    _ApexManRteGbeInRedPriHighAlarmBitRate_Type()
)
apexManRteGbeInRedPriHighAlarmBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedPriHighAlarmBitRate.setStatus("current")
_ApexManRteGbeInRedRateCompareType_Type = RateComparisonTYPE
_ApexManRteGbeInRedRateCompareType_Object = MibTableColumn
apexManRteGbeInRedRateCompareType = _ApexManRteGbeInRedRateCompareType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 8),
    _ApexManRteGbeInRedRateCompareType_Type()
)
apexManRteGbeInRedRateCompareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedRateCompareType.setStatus("current")
_ApexManRteGbeInRedEnable_Type = EnableDisableTYPE
_ApexManRteGbeInRedEnable_Object = MibTableColumn
apexManRteGbeInRedEnable = _ApexManRteGbeInRedEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 9),
    _ApexManRteGbeInRedEnable_Type()
)
apexManRteGbeInRedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedEnable.setStatus("current")


class _ApexManRteGbeInRedThreshold_Type(Integer32):
    """Custom type apexManRteGbeInRedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexManRteGbeInRedThreshold_Type.__name__ = "Integer32"
_ApexManRteGbeInRedThreshold_Object = MibTableColumn
apexManRteGbeInRedThreshold = _ApexManRteGbeInRedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 10),
    _ApexManRteGbeInRedThreshold_Type()
)
apexManRteGbeInRedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedThreshold.setStatus("current")


class _ApexManRteGbeInRedSuspend_Type(Integer32):
    """Custom type apexManRteGbeInRedSuspend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSuspended", 1),
          ("suspended", 2))
    )


_ApexManRteGbeInRedSuspend_Type.__name__ = "Integer32"
_ApexManRteGbeInRedSuspend_Object = MibTableColumn
apexManRteGbeInRedSuspend = _ApexManRteGbeInRedSuspend_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 11),
    _ApexManRteGbeInRedSuspend_Type()
)
apexManRteGbeInRedSuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSuspend.setStatus("current")


class _ApexManRteGbeInRedSecInterface_Type(Integer32):
    """Custom type apexManRteGbeInRedSecInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexManRteGbeInRedSecInterface_Type.__name__ = "Integer32"
_ApexManRteGbeInRedSecInterface_Object = MibTableColumn
apexManRteGbeInRedSecInterface = _ApexManRteGbeInRedSecInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 12),
    _ApexManRteGbeInRedSecInterface_Type()
)
apexManRteGbeInRedSecInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecInterface.setStatus("current")


class _ApexManRteGbeInRedSecUdp_Type(Integer32):
    """Custom type apexManRteGbeInRedSecUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexManRteGbeInRedSecUdp_Type.__name__ = "Integer32"
_ApexManRteGbeInRedSecUdp_Object = MibTableColumn
apexManRteGbeInRedSecUdp = _ApexManRteGbeInRedSecUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 13),
    _ApexManRteGbeInRedSecUdp_Type()
)
apexManRteGbeInRedSecUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecUdp.setStatus("current")
_ApexManRteGbeInRedSecMulticastIp_Type = IpAddress
_ApexManRteGbeInRedSecMulticastIp_Object = MibTableColumn
apexManRteGbeInRedSecMulticastIp = _ApexManRteGbeInRedSecMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 14),
    _ApexManRteGbeInRedSecMulticastIp_Type()
)
apexManRteGbeInRedSecMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecMulticastIp.setStatus("current")
_ApexManRteGbeInRedSecSourceIp_Type = IpAddress
_ApexManRteGbeInRedSecSourceIp_Object = MibTableColumn
apexManRteGbeInRedSecSourceIp = _ApexManRteGbeInRedSecSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 15),
    _ApexManRteGbeInRedSecSourceIp_Type()
)
apexManRteGbeInRedSecSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecSourceIp.setStatus("current")
_ApexManRteGbeInRedSecLowAlarmBitRate_Type = Integer32
_ApexManRteGbeInRedSecLowAlarmBitRate_Object = MibTableColumn
apexManRteGbeInRedSecLowAlarmBitRate = _ApexManRteGbeInRedSecLowAlarmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 16),
    _ApexManRteGbeInRedSecLowAlarmBitRate_Type()
)
apexManRteGbeInRedSecLowAlarmBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecLowAlarmBitRate.setStatus("current")
_ApexManRteGbeInRedSecHighAlarmBitRate_Type = Integer32
_ApexManRteGbeInRedSecHighAlarmBitRate_Object = MibTableColumn
apexManRteGbeInRedSecHighAlarmBitRate = _ApexManRteGbeInRedSecHighAlarmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 17),
    _ApexManRteGbeInRedSecHighAlarmBitRate_Type()
)
apexManRteGbeInRedSecHighAlarmBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecHighAlarmBitRate.setStatus("current")


class _ApexManRteGbeInRedSecRedundMcJoin_Type(Integer32):
    """Custom type apexManRteGbeInRedSecRedundMcJoin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joinOnOpen", 2),
          ("noJoinOnOpen", 1))
    )


_ApexManRteGbeInRedSecRedundMcJoin_Type.__name__ = "Integer32"
_ApexManRteGbeInRedSecRedundMcJoin_Object = MibTableColumn
apexManRteGbeInRedSecRedundMcJoin = _ApexManRteGbeInRedSecRedundMcJoin_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 3, 1, 18),
    _ApexManRteGbeInRedSecRedundMcJoin_Type()
)
apexManRteGbeInRedSecRedundMcJoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedSecRedundMcJoin.setStatus("current")
_ApexManRteGbeInRedForceSwitchTable_Object = MibTable
apexManRteGbeInRedForceSwitchTable = _ApexManRteGbeInRedForceSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 4)
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedForceSwitchTable.setStatus("current")
_ApexManRteGbeInRedForceSwitchEntry_Object = MibTableRow
apexManRteGbeInRedForceSwitchEntry = _ApexManRteGbeInRedForceSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 4, 1)
)
apexManRteGbeInRedForceSwitchEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRteGbeInRedForceSwitchIndex"),
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedForceSwitchEntry.setStatus("current")


class _ApexManRteGbeInRedForceSwitchIndex_Type(Integer32):
    """Custom type apexManRteGbeInRedForceSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManRteGbeInRedForceSwitchIndex_Type.__name__ = "Integer32"
_ApexManRteGbeInRedForceSwitchIndex_Object = MibTableColumn
apexManRteGbeInRedForceSwitchIndex = _ApexManRteGbeInRedForceSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 4, 1, 1),
    _ApexManRteGbeInRedForceSwitchIndex_Type()
)
apexManRteGbeInRedForceSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRteGbeInRedForceSwitchIndex.setStatus("current")


class _ApexManRteGbeInRedForceSwitch_Type(Integer32):
    """Custom type apexManRteGbeInRedForceSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceSwitch", 2),
          ("switchNotInProgress", 1))
    )


_ApexManRteGbeInRedForceSwitch_Type.__name__ = "Integer32"
_ApexManRteGbeInRedForceSwitch_Object = MibTableColumn
apexManRteGbeInRedForceSwitch = _ApexManRteGbeInRedForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 1, 6, 4, 1, 2),
    _ApexManRteGbeInRedForceSwitch_Type()
)
apexManRteGbeInRedForceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexManRteGbeInRedForceSwitch.setStatus("current")
_ApexManualRoutingStatus_ObjectIdentity = ObjectIdentity
apexManualRoutingStatus = _ApexManualRoutingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2)
)
_ApexManualRoutingStatusGeneral_ObjectIdentity = ObjectIdentity
apexManualRoutingStatusGeneral = _ApexManualRoutingStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 1)
)


class _ApexManualRouteInvalidApplyText_Type(DisplayString):
    """Custom type apexManualRouteInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexManualRouteInvalidApplyText_Type.__name__ = "DisplayString"
_ApexManualRouteInvalidApplyText_Object = MibScalar
apexManualRouteInvalidApplyText = _ApexManualRouteInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 1, 1),
    _ApexManualRouteInvalidApplyText_Type()
)
apexManualRouteInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexManualRouteInvalidApplyText.setStatus("current")


class _ApexManRtePassThroughInvalidApplyText_Type(DisplayString):
    """Custom type apexManRtePassThroughInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexManRtePassThroughInvalidApplyText_Type.__name__ = "DisplayString"
_ApexManRtePassThroughInvalidApplyText_Object = MibScalar
apexManRtePassThroughInvalidApplyText = _ApexManRtePassThroughInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 1, 2),
    _ApexManRtePassThroughInvalidApplyText_Type()
)
apexManRtePassThroughInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexManRtePassThroughInvalidApplyText.setStatus("current")


class _ApexManRteGbeInRedInvalidApplyText_Type(DisplayString):
    """Custom type apexManRteGbeInRedInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexManRteGbeInRedInvalidApplyText_Type.__name__ = "DisplayString"
_ApexManRteGbeInRedInvalidApplyText_Object = MibScalar
apexManRteGbeInRedInvalidApplyText = _ApexManRteGbeInRedInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 1, 3),
    _ApexManRteGbeInRedInvalidApplyText_Type()
)
apexManRteGbeInRedInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexManRteGbeInRedInvalidApplyText.setStatus("current")
_ApexManualRouteGbeInputRedundStatus_ObjectIdentity = ObjectIdentity
apexManualRouteGbeInputRedundStatus = _ApexManualRouteGbeInputRedundStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2)
)
_ApexManRteGbeInRedStatusGeneral_ObjectIdentity = ObjectIdentity
apexManRteGbeInRedStatusGeneral = _ApexManRteGbeInRedStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2, 1)
)
_ApexManRteGbeInRedStatusMapTable_Object = MibTable
apexManRteGbeInRedStatusMapTable = _ApexManRteGbeInRedStatusMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedStatusMapTable.setStatus("current")
_ApexManRteGbeInRedStatusMapEntry_Object = MibTableRow
apexManRteGbeInRedStatusMapEntry = _ApexManRteGbeInRedStatusMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2, 2, 1)
)
apexManRteGbeInRedStatusMapEntry.setIndexNames(
    (0, "APEX-MIB", "apexManRteGbeInRedStatusMapIndex"),
)
if mibBuilder.loadTexts:
    apexManRteGbeInRedStatusMapEntry.setStatus("current")


class _ApexManRteGbeInRedStatusMapIndex_Type(Integer32):
    """Custom type apexManRteGbeInRedStatusMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexManRteGbeInRedStatusMapIndex_Type.__name__ = "Integer32"
_ApexManRteGbeInRedStatusMapIndex_Object = MibTableColumn
apexManRteGbeInRedStatusMapIndex = _ApexManRteGbeInRedStatusMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2, 2, 1, 1),
    _ApexManRteGbeInRedStatusMapIndex_Type()
)
apexManRteGbeInRedStatusMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexManRteGbeInRedStatusMapIndex.setStatus("current")


class _ApexManRteGbeInRedStatusMapInputTsStatRow_Type(Integer32):
    """Custom type apexManRteGbeInRedStatusMapInputTsStatRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 784),
    )


_ApexManRteGbeInRedStatusMapInputTsStatRow_Type.__name__ = "Integer32"
_ApexManRteGbeInRedStatusMapInputTsStatRow_Object = MibTableColumn
apexManRteGbeInRedStatusMapInputTsStatRow = _ApexManRteGbeInRedStatusMapInputTsStatRow_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 10, 2, 2, 2, 1, 2),
    _ApexManRteGbeInRedStatusMapInputTsStatRow_Type()
)
apexManRteGbeInRedStatusMapInputTsStatRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexManRteGbeInRedStatusMapInputTsStatRow.setStatus("current")
_ApexAncillaryPidMapping_ObjectIdentity = ObjectIdentity
apexAncillaryPidMapping = _ApexAncillaryPidMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11)
)
_ApexPidMapConfig_ObjectIdentity = ObjectIdentity
apexPidMapConfig = _ApexPidMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1)
)
_ApexPidMapTable_Object = MibTable
apexPidMapTable = _ApexPidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1)
)
if mibBuilder.loadTexts:
    apexPidMapTable.setStatus("current")
_ApexPidMapEntry_Object = MibTableRow
apexPidMapEntry = _ApexPidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1)
)
apexPidMapEntry.setIndexNames(
    (0, "APEX-MIB", "apexPidMapIndex"),
)
if mibBuilder.loadTexts:
    apexPidMapEntry.setStatus("current")


class _ApexPidMapIndex_Type(Integer32):
    """Custom type apexPidMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_ApexPidMapIndex_Type.__name__ = "Integer32"
_ApexPidMapIndex_Object = MibTableColumn
apexPidMapIndex = _ApexPidMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 1),
    _ApexPidMapIndex_Type()
)
apexPidMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPidMapIndex.setStatus("current")
_ApexPidMapEnable_Type = EnableDisableTYPE
_ApexPidMapEnable_Object = MibTableColumn
apexPidMapEnable = _ApexPidMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 2),
    _ApexPidMapEnable_Type()
)
apexPidMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapEnable.setStatus("current")


class _ApexPidMapInputType_Type(Integer32):
    """Custom type apexPidMapInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1))
    )


_ApexPidMapInputType_Type.__name__ = "Integer32"
_ApexPidMapInputType_Object = MibTableColumn
apexPidMapInputType = _ApexPidMapInputType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 3),
    _ApexPidMapInputType_Type()
)
apexPidMapInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputType.setStatus("current")


class _ApexPidMapInputInterface_Type(Integer32):
    """Custom type apexPidMapInputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexPidMapInputInterface_Type.__name__ = "Integer32"
_ApexPidMapInputInterface_Object = MibTableColumn
apexPidMapInputInterface = _ApexPidMapInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 4),
    _ApexPidMapInputInterface_Type()
)
apexPidMapInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputInterface.setStatus("current")


class _ApexPidMapInputUdp_Type(Integer32):
    """Custom type apexPidMapInputUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexPidMapInputUdp_Type.__name__ = "Integer32"
_ApexPidMapInputUdp_Object = MibTableColumn
apexPidMapInputUdp = _ApexPidMapInputUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 5),
    _ApexPidMapInputUdp_Type()
)
apexPidMapInputUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputUdp.setStatus("current")
_ApexPidMapInputMulticastIp_Type = IpAddress
_ApexPidMapInputMulticastIp_Object = MibTableColumn
apexPidMapInputMulticastIp = _ApexPidMapInputMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 6),
    _ApexPidMapInputMulticastIp_Type()
)
apexPidMapInputMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputMulticastIp.setStatus("current")
_ApexPidMapInputSourceIp_Type = IpAddress
_ApexPidMapInputSourceIp_Object = MibTableColumn
apexPidMapInputSourceIp = _ApexPidMapInputSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 7),
    _ApexPidMapInputSourceIp_Type()
)
apexPidMapInputSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputSourceIp.setStatus("current")


class _ApexPidMapInputPid_Type(Integer32):
    """Custom type apexPidMapInputPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ApexPidMapInputPid_Type.__name__ = "Integer32"
_ApexPidMapInputPid_Object = MibTableColumn
apexPidMapInputPid = _ApexPidMapInputPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 8),
    _ApexPidMapInputPid_Type()
)
apexPidMapInputPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapInputPid.setStatus("current")


class _ApexPidMapOutputTsNum_Type(Integer32):
    """Custom type apexPidMapOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexPidMapOutputTsNum_Type.__name__ = "Integer32"
_ApexPidMapOutputTsNum_Object = MibTableColumn
apexPidMapOutputTsNum = _ApexPidMapOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 9),
    _ApexPidMapOutputTsNum_Type()
)
apexPidMapOutputTsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapOutputTsNum.setStatus("current")


class _ApexPidMapOutputPid_Type(Integer32):
    """Custom type apexPidMapOutputPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ApexPidMapOutputPid_Type.__name__ = "Integer32"
_ApexPidMapOutputPid_Object = MibTableColumn
apexPidMapOutputPid = _ApexPidMapOutputPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 1, 1, 10),
    _ApexPidMapOutputPid_Type()
)
apexPidMapOutputPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapOutputPid.setStatus("current")
_ApexPidMapApplyTable_Object = MibTable
apexPidMapApplyTable = _ApexPidMapApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 2)
)
if mibBuilder.loadTexts:
    apexPidMapApplyTable.setStatus("current")
_ApexPidMapApplyEntry_Object = MibTableRow
apexPidMapApplyEntry = _ApexPidMapApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 2, 1)
)
apexPidMapApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexPidMapApplyIndex"),
)
if mibBuilder.loadTexts:
    apexPidMapApplyEntry.setStatus("current")


class _ApexPidMapApplyIndex_Type(Integer32):
    """Custom type apexPidMapApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_ApexPidMapApplyIndex_Type.__name__ = "Integer32"
_ApexPidMapApplyIndex_Object = MibTableColumn
apexPidMapApplyIndex = _ApexPidMapApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 2, 1, 1),
    _ApexPidMapApplyIndex_Type()
)
apexPidMapApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPidMapApplyIndex.setStatus("current")
_ApexPidMapApplyChange_Type = ApplyDataToDeviceTYPE
_ApexPidMapApplyChange_Object = MibTableColumn
apexPidMapApplyChange = _ApexPidMapApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 1, 2, 1, 2),
    _ApexPidMapApplyChange_Type()
)
apexPidMapApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPidMapApplyChange.setStatus("current")
_ApexPidMapStatus_ObjectIdentity = ObjectIdentity
apexPidMapStatus = _ApexPidMapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 2)
)
_ApexPidMapStatusGeneral_ObjectIdentity = ObjectIdentity
apexPidMapStatusGeneral = _ApexPidMapStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 2, 1)
)
_ApexPidMapMaxPidMappings_Type = Integer32
_ApexPidMapMaxPidMappings_Object = MibScalar
apexPidMapMaxPidMappings = _ApexPidMapMaxPidMappings_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 2, 1, 1),
    _ApexPidMapMaxPidMappings_Type()
)
apexPidMapMaxPidMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPidMapMaxPidMappings.setStatus("current")


class _ApexPidMapInvalidApplyText_Type(DisplayString):
    """Custom type apexPidMapInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexPidMapInvalidApplyText_Type.__name__ = "DisplayString"
_ApexPidMapInvalidApplyText_Object = MibScalar
apexPidMapInvalidApplyText = _ApexPidMapInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 11, 2, 1, 3),
    _ApexPidMapInvalidApplyText_Type()
)
apexPidMapInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPidMapInvalidApplyText.setStatus("current")
_ApexInsertion_ObjectIdentity = ObjectIdentity
apexInsertion = _ApexInsertion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12)
)
_ApexInsertionConfig_ObjectIdentity = ObjectIdentity
apexInsertionConfig = _ApexInsertionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 1)
)
_ApexInsertionConfigGeneral_ObjectIdentity = ObjectIdentity
apexInsertionConfigGeneral = _ApexInsertionConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 1, 1)
)


class _ApexInsertionMode_Type(Integer32):
    """Custom type apexInsertionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("efficient", 1),
          ("singleSection", 2))
    )


_ApexInsertionMode_Type.__name__ = "Integer32"
_ApexInsertionMode_Object = MibScalar
apexInsertionMode = _ApexInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 1, 1, 1),
    _ApexInsertionMode_Type()
)
apexInsertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexInsertionMode.setStatus("current")
_ApexInsertionStatus_ObjectIdentity = ObjectIdentity
apexInsertionStatus = _ApexInsertionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2)
)
_ApexInsertionStatusGeneral_ObjectIdentity = ObjectIdentity
apexInsertionStatusGeneral = _ApexInsertionStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 1)
)
_ApexInsertPacketStatisticsTable_Object = MibTable
apexInsertPacketStatisticsTable = _ApexInsertPacketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 2)
)
if mibBuilder.loadTexts:
    apexInsertPacketStatisticsTable.setStatus("current")
_ApexInsertPacketStatisticsEntry_Object = MibTableRow
apexInsertPacketStatisticsEntry = _ApexInsertPacketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 2, 1)
)
apexInsertPacketStatisticsEntry.setIndexNames(
    (0, "APEX-MIB", "apexInsertPacketStatOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexInsertPacketStatisticsEntry.setStatus("current")


class _ApexInsertPacketStatOutputTsNum_Type(Integer32):
    """Custom type apexInsertPacketStatOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexInsertPacketStatOutputTsNum_Type.__name__ = "Integer32"
_ApexInsertPacketStatOutputTsNum_Object = MibTableColumn
apexInsertPacketStatOutputTsNum = _ApexInsertPacketStatOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 2, 1, 1),
    _ApexInsertPacketStatOutputTsNum_Type()
)
apexInsertPacketStatOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexInsertPacketStatOutputTsNum.setStatus("current")
_ApexInsertPacketStatTotPkts_Type = Integer32
_ApexInsertPacketStatTotPkts_Object = MibTableColumn
apexInsertPacketStatTotPkts = _ApexInsertPacketStatTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 2, 1, 2),
    _ApexInsertPacketStatTotPkts_Type()
)
apexInsertPacketStatTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInsertPacketStatTotPkts.setStatus("current")
_ApexInsertPacketStatNumPkts_Type = Integer32
_ApexInsertPacketStatNumPkts_Object = MibTableColumn
apexInsertPacketStatNumPkts = _ApexInsertPacketStatNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 12, 2, 2, 1, 3),
    _ApexInsertPacketStatNumPkts_Type()
)
apexInsertPacketStatNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInsertPacketStatNumPkts.setStatus("current")
_ApexInputTransport_ObjectIdentity = ObjectIdentity
apexInputTransport = _ApexInputTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13)
)
_ApexInputTsConfig_ObjectIdentity = ObjectIdentity
apexInputTsConfig = _ApexInputTsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 1)
)
_ApexInputTsConfigGeneral_ObjectIdentity = ObjectIdentity
apexInputTsConfigGeneral = _ApexInputTsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 1, 1)
)
_ApexInputTsStatus_ObjectIdentity = ObjectIdentity
apexInputTsStatus = _ApexInputTsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2)
)
_ApexInputTsStatusGeneral_ObjectIdentity = ObjectIdentity
apexInputTsStatusGeneral = _ApexInputTsStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 1)
)
_ApexInputTsStatTable_Object = MibTable
apexInputTsStatTable = _ApexInputTsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2)
)
if mibBuilder.loadTexts:
    apexInputTsStatTable.setStatus("current")
_ApexInputTsStatEntry_Object = MibTableRow
apexInputTsStatEntry = _ApexInputTsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1)
)
apexInputTsStatEntry.setIndexNames(
    (0, "APEX-MIB", "apexInputTsStatIndex"),
)
if mibBuilder.loadTexts:
    apexInputTsStatEntry.setStatus("current")


class _ApexInputTsStatIndex_Type(Integer32):
    """Custom type apexInputTsStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 784),
    )


_ApexInputTsStatIndex_Type.__name__ = "Integer32"
_ApexInputTsStatIndex_Object = MibTableColumn
apexInputTsStatIndex = _ApexInputTsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 1),
    _ApexInputTsStatIndex_Type()
)
apexInputTsStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexInputTsStatIndex.setStatus("current")


class _ApexInputTsStatStreamInUse_Type(Integer32):
    """Custom type apexInputTsStatStreamInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_ApexInputTsStatStreamInUse_Type.__name__ = "Integer32"
_ApexInputTsStatStreamInUse_Object = MibTableColumn
apexInputTsStatStreamInUse = _ApexInputTsStatStreamInUse_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 2),
    _ApexInputTsStatStreamInUse_Type()
)
apexInputTsStatStreamInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatStreamInUse.setStatus("current")


class _ApexInputTsStatInputType_Type(Integer32):
    """Custom type apexInputTsStatInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1),
          ("notApplicable", 0))
    )


_ApexInputTsStatInputType_Type.__name__ = "Integer32"
_ApexInputTsStatInputType_Object = MibTableColumn
apexInputTsStatInputType = _ApexInputTsStatInputType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 3),
    _ApexInputTsStatInputType_Type()
)
apexInputTsStatInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatInputType.setStatus("current")


class _ApexInputTsStatRoutingType_Type(Integer32):
    """Custom type apexInputTsStatRoutingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("notApplicable", 0),
          ("session", 1),
          ("udpMapping", 3))
    )


_ApexInputTsStatRoutingType_Type.__name__ = "Integer32"
_ApexInputTsStatRoutingType_Object = MibTableColumn
apexInputTsStatRoutingType = _ApexInputTsStatRoutingType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 4),
    _ApexInputTsStatRoutingType_Type()
)
apexInputTsStatRoutingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatRoutingType.setStatus("current")
_ApexInputTsStatPriState_Type = InputTsStateTYPE
_ApexInputTsStatPriState_Object = MibTableColumn
apexInputTsStatPriState = _ApexInputTsStatPriState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 5),
    _ApexInputTsStatPriState_Type()
)
apexInputTsStatPriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatPriState.setStatus("current")
_ApexInputTsStatPriInputInterface_Type = Integer32
_ApexInputTsStatPriInputInterface_Object = MibTableColumn
apexInputTsStatPriInputInterface = _ApexInputTsStatPriInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 6),
    _ApexInputTsStatPriInputInterface_Type()
)
apexInputTsStatPriInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatPriInputInterface.setStatus("current")
_ApexInputTsStatPriInputUdp_Type = Integer32
_ApexInputTsStatPriInputUdp_Object = MibTableColumn
apexInputTsStatPriInputUdp = _ApexInputTsStatPriInputUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 7),
    _ApexInputTsStatPriInputUdp_Type()
)
apexInputTsStatPriInputUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatPriInputUdp.setStatus("current")
_ApexInputTsStatPriInputMulticastIp_Type = IpAddress
_ApexInputTsStatPriInputMulticastIp_Object = MibTableColumn
apexInputTsStatPriInputMulticastIp = _ApexInputTsStatPriInputMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 8),
    _ApexInputTsStatPriInputMulticastIp_Type()
)
apexInputTsStatPriInputMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatPriInputMulticastIp.setStatus("current")
_ApexInputTsStatPriInputSourceIp_Type = IpAddress
_ApexInputTsStatPriInputSourceIp_Object = MibTableColumn
apexInputTsStatPriInputSourceIp = _ApexInputTsStatPriInputSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 9),
    _ApexInputTsStatPriInputSourceIp_Type()
)
apexInputTsStatPriInputSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatPriInputSourceIp.setStatus("current")
_ApexInputTsStatSecState_Type = InputTsStateTYPE
_ApexInputTsStatSecState_Object = MibTableColumn
apexInputTsStatSecState = _ApexInputTsStatSecState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 10),
    _ApexInputTsStatSecState_Type()
)
apexInputTsStatSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatSecState.setStatus("current")
_ApexInputTsStatSecInputInterface_Type = Integer32
_ApexInputTsStatSecInputInterface_Object = MibTableColumn
apexInputTsStatSecInputInterface = _ApexInputTsStatSecInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 11),
    _ApexInputTsStatSecInputInterface_Type()
)
apexInputTsStatSecInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatSecInputInterface.setStatus("current")
_ApexInputTsStatSecInputUdp_Type = Integer32
_ApexInputTsStatSecInputUdp_Object = MibTableColumn
apexInputTsStatSecInputUdp = _ApexInputTsStatSecInputUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 12),
    _ApexInputTsStatSecInputUdp_Type()
)
apexInputTsStatSecInputUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatSecInputUdp.setStatus("current")
_ApexInputTsStatSecInputMulticastIp_Type = IpAddress
_ApexInputTsStatSecInputMulticastIp_Object = MibTableColumn
apexInputTsStatSecInputMulticastIp = _ApexInputTsStatSecInputMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 13),
    _ApexInputTsStatSecInputMulticastIp_Type()
)
apexInputTsStatSecInputMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatSecInputMulticastIp.setStatus("current")
_ApexInputTsStatSecInputSourceIp_Type = IpAddress
_ApexInputTsStatSecInputSourceIp_Object = MibTableColumn
apexInputTsStatSecInputSourceIp = _ApexInputTsStatSecInputSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 14),
    _ApexInputTsStatSecInputSourceIp_Type()
)
apexInputTsStatSecInputSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatSecInputSourceIp.setStatus("current")
_ApexInputTsStatRateCompareType_Type = RateComparisonTYPE
_ApexInputTsStatRateCompareType_Object = MibTableColumn
apexInputTsStatRateCompareType = _ApexInputTsStatRateCompareType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 13, 2, 2, 1, 15),
    _ApexInputTsStatRateCompareType_Type()
)
apexInputTsStatRateCompareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInputTsStatRateCompareType.setStatus("current")
_ApexOutputTransport_ObjectIdentity = ObjectIdentity
apexOutputTransport = _ApexOutputTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14)
)
_ApexOutputTsConfig_ObjectIdentity = ObjectIdentity
apexOutputTsConfig = _ApexOutputTsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1)
)
_ApexOutputTsConfigGeneral_ObjectIdentity = ObjectIdentity
apexOutputTsConfigGeneral = _ApexOutputTsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 1)
)
_ApexOutputTsUtilizationMonitoring_ObjectIdentity = ObjectIdentity
apexOutputTsUtilizationMonitoring = _ApexOutputTsUtilizationMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4)
)
_ApexOutputTsUtilizationMonitorGeneral_ObjectIdentity = ObjectIdentity
apexOutputTsUtilizationMonitorGeneral = _ApexOutputTsUtilizationMonitorGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 1)
)


class _ApexOutputTsUtilMonAlarmThreshold_Type(Integer32):
    """Custom type apexOutputTsUtilMonAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexOutputTsUtilMonAlarmThreshold_Type.__name__ = "Integer32"
_ApexOutputTsUtilMonAlarmThreshold_Object = MibScalar
apexOutputTsUtilMonAlarmThreshold = _ApexOutputTsUtilMonAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 1, 1),
    _ApexOutputTsUtilMonAlarmThreshold_Type()
)
apexOutputTsUtilMonAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsUtilMonAlarmThreshold.setStatus("current")


class _ApexOutputTsUtilMonSetAlarmDelay_Type(Integer32):
    """Custom type apexOutputTsUtilMonSetAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ApexOutputTsUtilMonSetAlarmDelay_Type.__name__ = "Integer32"
_ApexOutputTsUtilMonSetAlarmDelay_Object = MibScalar
apexOutputTsUtilMonSetAlarmDelay = _ApexOutputTsUtilMonSetAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 1, 2),
    _ApexOutputTsUtilMonSetAlarmDelay_Type()
)
apexOutputTsUtilMonSetAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsUtilMonSetAlarmDelay.setStatus("current")


class _ApexOutputTsUtilMonClearAlarmDelay_Type(Integer32):
    """Custom type apexOutputTsUtilMonClearAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ApexOutputTsUtilMonClearAlarmDelay_Type.__name__ = "Integer32"
_ApexOutputTsUtilMonClearAlarmDelay_Object = MibScalar
apexOutputTsUtilMonClearAlarmDelay = _ApexOutputTsUtilMonClearAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 1, 3),
    _ApexOutputTsUtilMonClearAlarmDelay_Type()
)
apexOutputTsUtilMonClearAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsUtilMonClearAlarmDelay.setStatus("current")
_ApexOutputTsUtilizationMonitorTable_Object = MibTable
apexOutputTsUtilizationMonitorTable = _ApexOutputTsUtilizationMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 2)
)
if mibBuilder.loadTexts:
    apexOutputTsUtilizationMonitorTable.setStatus("current")
_ApexOutputTsUtilizationMonitorEntry_Object = MibTableRow
apexOutputTsUtilizationMonitorEntry = _ApexOutputTsUtilizationMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 2, 1)
)
apexOutputTsUtilizationMonitorEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsUtilMonOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexOutputTsUtilizationMonitorEntry.setStatus("current")


class _ApexOutputTsUtilMonOutputTsNum_Type(Integer32):
    """Custom type apexOutputTsUtilMonOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexOutputTsUtilMonOutputTsNum_Type.__name__ = "Integer32"
_ApexOutputTsUtilMonOutputTsNum_Object = MibTableColumn
apexOutputTsUtilMonOutputTsNum = _ApexOutputTsUtilMonOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 2, 1, 1),
    _ApexOutputTsUtilMonOutputTsNum_Type()
)
apexOutputTsUtilMonOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsUtilMonOutputTsNum.setStatus("current")
_ApexOutputTsUtilMonResetTotDropPacket_Type = ResetStatisticsTYPE
_ApexOutputTsUtilMonResetTotDropPacket_Object = MibTableColumn
apexOutputTsUtilMonResetTotDropPacket = _ApexOutputTsUtilMonResetTotDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 4, 2, 1, 2),
    _ApexOutputTsUtilMonResetTotDropPacket_Type()
)
apexOutputTsUtilMonResetTotDropPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsUtilMonResetTotDropPacket.setStatus("current")
_ApexOutputTsConfApplyTable_Object = MibTable
apexOutputTsConfApplyTable = _ApexOutputTsConfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 5)
)
if mibBuilder.loadTexts:
    apexOutputTsConfApplyTable.setStatus("current")
_ApexOutputTsConfApplyEntry_Object = MibTableRow
apexOutputTsConfApplyEntry = _ApexOutputTsConfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 5, 1)
)
apexOutputTsConfApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsConfApplyIndex"),
)
if mibBuilder.loadTexts:
    apexOutputTsConfApplyEntry.setStatus("current")


class _ApexOutputTsConfApplyIndex_Type(Integer32):
    """Custom type apexOutputTsConfApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexOutputTsConfApplyIndex_Type.__name__ = "Integer32"
_ApexOutputTsConfApplyIndex_Object = MibTableColumn
apexOutputTsConfApplyIndex = _ApexOutputTsConfApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 5, 1, 1),
    _ApexOutputTsConfApplyIndex_Type()
)
apexOutputTsConfApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsConfApplyIndex.setStatus("current")
_ApexOutputTsConfApplyChange_Type = ApplyDataToDeviceTYPE
_ApexOutputTsConfApplyChange_Object = MibTableColumn
apexOutputTsConfApplyChange = _ApexOutputTsConfApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 5, 1, 2),
    _ApexOutputTsConfApplyChange_Type()
)
apexOutputTsConfApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfApplyChange.setStatus("current")
_ApexOutputTsConfigTable_Object = MibTable
apexOutputTsConfigTable = _ApexOutputTsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6)
)
if mibBuilder.loadTexts:
    apexOutputTsConfigTable.setStatus("current")
_ApexOutputTsConfigEntry_Object = MibTableRow
apexOutputTsConfigEntry = _ApexOutputTsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1)
)
apexOutputTsConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsConfOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexOutputTsConfigEntry.setStatus("current")


class _ApexOutputTsConfOutputTsNum_Type(Integer32):
    """Custom type apexOutputTsConfOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexOutputTsConfOutputTsNum_Type.__name__ = "Integer32"
_ApexOutputTsConfOutputTsNum_Object = MibTableColumn
apexOutputTsConfOutputTsNum = _ApexOutputTsConfOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 1),
    _ApexOutputTsConfOutputTsNum_Type()
)
apexOutputTsConfOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsConfOutputTsNum.setStatus("current")


class _ApexOutputTsConfPidRemappingMode_Type(Integer32):
    """Custom type apexOutputTsConfPidRemappingMode based on Integer32"""
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
        *(("disabled", 1),
          ("remapProgramBased", 3),
          ("remapProgramBased2", 4),
          ("remapWithoutReuse", 2),
          ("unrestricted", 5))
    )


_ApexOutputTsConfPidRemappingMode_Type.__name__ = "Integer32"
_ApexOutputTsConfPidRemappingMode_Object = MibTableColumn
apexOutputTsConfPidRemappingMode = _ApexOutputTsConfPidRemappingMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 2),
    _ApexOutputTsConfPidRemappingMode_Type()
)
apexOutputTsConfPidRemappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfPidRemappingMode.setStatus("current")


class _ApexOutputTsConfOperatingMode_Type(Integer32):
    """Custom type apexOutputTsConfOperatingMode based on Integer32"""
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
        *(("depi", 4),
          ("manualRouting", 2),
          ("notInUse", 0),
          ("sessionControl", 1),
          ("udpMapping", 3))
    )


_ApexOutputTsConfOperatingMode_Type.__name__ = "Integer32"
_ApexOutputTsConfOperatingMode_Object = MibTableColumn
apexOutputTsConfOperatingMode = _ApexOutputTsConfOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 3),
    _ApexOutputTsConfOperatingMode_Type()
)
apexOutputTsConfOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfOperatingMode.setStatus("current")


class _ApexOutputTsConfOutPatTsId_Type(Integer32):
    """Custom type apexOutputTsConfOutPatTsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexOutputTsConfOutPatTsId_Type.__name__ = "Integer32"
_ApexOutputTsConfOutPatTsId_Object = MibTableColumn
apexOutputTsConfOutPatTsId = _ApexOutputTsConfOutPatTsId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 4),
    _ApexOutputTsConfOutPatTsId_Type()
)
apexOutputTsConfOutPatTsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfOutPatTsId.setStatus("current")
_ApexOutputTsConfPsipEnable_Type = EnableDisableTYPE
_ApexOutputTsConfPsipEnable_Object = MibTableColumn
apexOutputTsConfPsipEnable = _ApexOutputTsConfPsipEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 5),
    _ApexOutputTsConfPsipEnable_Type()
)
apexOutputTsConfPsipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfPsipEnable.setStatus("current")


class _ApexOutputTsConfEncryptionType_Type(Integer32):
    """Custom type apexOutputTsConfEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcastEncryption", 2),
          ("cte", 1),
          ("noEncryption", 0))
    )


_ApexOutputTsConfEncryptionType_Type.__name__ = "Integer32"
_ApexOutputTsConfEncryptionType_Object = MibTableColumn
apexOutputTsConfEncryptionType = _ApexOutputTsConfEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 6),
    _ApexOutputTsConfEncryptionType_Type()
)
apexOutputTsConfEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfEncryptionType.setStatus("current")


class _ApexOutputTsConfSimulcryptMode_Type(Integer32):
    """Custom type apexOutputTsConfSimulcryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalEIS", 1),
          ("internalEIS", 2),
          ("none", 0))
    )


_ApexOutputTsConfSimulcryptMode_Type.__name__ = "Integer32"
_ApexOutputTsConfSimulcryptMode_Object = MibTableColumn
apexOutputTsConfSimulcryptMode = _ApexOutputTsConfSimulcryptMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 7),
    _ApexOutputTsConfSimulcryptMode_Type()
)
apexOutputTsConfSimulcryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfSimulcryptMode.setStatus("current")
_ApexOutputTsConfPcrLess_Type = EnableDisableTYPE
_ApexOutputTsConfPcrLess_Object = MibTableColumn
apexOutputTsConfPcrLess = _ApexOutputTsConfPcrLess_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 1, 6, 1, 8),
    _ApexOutputTsConfPcrLess_Type()
)
apexOutputTsConfPcrLess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexOutputTsConfPcrLess.setStatus("current")
_ApexOutputTsStatus_ObjectIdentity = ObjectIdentity
apexOutputTsStatus = _ApexOutputTsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2)
)
_ApexOutputTsStatusGeneral_ObjectIdentity = ObjectIdentity
apexOutputTsStatusGeneral = _ApexOutputTsStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 1)
)


class _ApexOutputTsStatusInvalidApplyText_Type(DisplayString):
    """Custom type apexOutputTsStatusInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexOutputTsStatusInvalidApplyText_Type.__name__ = "DisplayString"
_ApexOutputTsStatusInvalidApplyText_Object = MibScalar
apexOutputTsStatusInvalidApplyText = _ApexOutputTsStatusInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 1, 1),
    _ApexOutputTsStatusInvalidApplyText_Type()
)
apexOutputTsStatusInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusInvalidApplyText.setStatus("current")
_ApexOutputTsUtilization_ObjectIdentity = ObjectIdentity
apexOutputTsUtilization = _ApexOutputTsUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2)
)
_ApexOutputTsUtilizationGeneral_ObjectIdentity = ObjectIdentity
apexOutputTsUtilizationGeneral = _ApexOutputTsUtilizationGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 1)
)
_ApexOutputTsUtilizationSamplePeriod_Type = Integer32
_ApexOutputTsUtilizationSamplePeriod_Object = MibScalar
apexOutputTsUtilizationSamplePeriod = _ApexOutputTsUtilizationSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 1, 1),
    _ApexOutputTsUtilizationSamplePeriod_Type()
)
apexOutputTsUtilizationSamplePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizationSamplePeriod.setStatus("current")
_ApexOutputTsUtilizationTable_Object = MibTable
apexOutputTsUtilizationTable = _ApexOutputTsUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2)
)
if mibBuilder.loadTexts:
    apexOutputTsUtilizationTable.setStatus("current")
_ApexOutputTsUtilizationEntry_Object = MibTableRow
apexOutputTsUtilizationEntry = _ApexOutputTsUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1)
)
apexOutputTsUtilizationEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsUtilizOutpuTsNum"),
)
if mibBuilder.loadTexts:
    apexOutputTsUtilizationEntry.setStatus("current")


class _ApexOutputTsUtilizOutpuTsNum_Type(Integer32):
    """Custom type apexOutputTsUtilizOutpuTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexOutputTsUtilizOutpuTsNum_Type.__name__ = "Integer32"
_ApexOutputTsUtilizOutpuTsNum_Object = MibTableColumn
apexOutputTsUtilizOutpuTsNum = _ApexOutputTsUtilizOutpuTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 1),
    _ApexOutputTsUtilizOutpuTsNum_Type()
)
apexOutputTsUtilizOutpuTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsUtilizOutpuTsNum.setStatus("current")


class _ApexOutputTsUtilizDataFlag_Type(Integer32):
    """Custom type apexOutputTsUtilizDataFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("samplingComplete", 1),
          ("samplingIncomplete", 2))
    )


_ApexOutputTsUtilizDataFlag_Type.__name__ = "Integer32"
_ApexOutputTsUtilizDataFlag_Object = MibTableColumn
apexOutputTsUtilizDataFlag = _ApexOutputTsUtilizDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 2),
    _ApexOutputTsUtilizDataFlag_Type()
)
apexOutputTsUtilizDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizDataFlag.setStatus("current")
_ApexOutputTsUtilizNumSamples_Type = Unsigned32
_ApexOutputTsUtilizNumSamples_Object = MibTableColumn
apexOutputTsUtilizNumSamples = _ApexOutputTsUtilizNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 3),
    _ApexOutputTsUtilizNumSamples_Type()
)
apexOutputTsUtilizNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizNumSamples.setStatus("current")


class _ApexOutputTsUtilizThreshold_Type(Integer32):
    """Custom type apexOutputTsUtilizThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmThresholdReached", 2),
          ("noError", 1),
          ("notApplicable", 0))
    )


_ApexOutputTsUtilizThreshold_Type.__name__ = "Integer32"
_ApexOutputTsUtilizThreshold_Object = MibTableColumn
apexOutputTsUtilizThreshold = _ApexOutputTsUtilizThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 4),
    _ApexOutputTsUtilizThreshold_Type()
)
apexOutputTsUtilizThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizThreshold.setStatus("current")
_ApexOutputTsUtilizTime_Type = Unsigned32
_ApexOutputTsUtilizTime_Object = MibTableColumn
apexOutputTsUtilizTime = _ApexOutputTsUtilizTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 5),
    _ApexOutputTsUtilizTime_Type()
)
apexOutputTsUtilizTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizTime.setStatus("current")


class _ApexOutputTsUtilizCurPercent_Type(Integer32):
    """Custom type apexOutputTsUtilizCurPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexOutputTsUtilizCurPercent_Type.__name__ = "Integer32"
_ApexOutputTsUtilizCurPercent_Object = MibTableColumn
apexOutputTsUtilizCurPercent = _ApexOutputTsUtilizCurPercent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 6),
    _ApexOutputTsUtilizCurPercent_Type()
)
apexOutputTsUtilizCurPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizCurPercent.setStatus("current")


class _ApexOutputTsUtilizAvgPercent_Type(Integer32):
    """Custom type apexOutputTsUtilizAvgPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexOutputTsUtilizAvgPercent_Type.__name__ = "Integer32"
_ApexOutputTsUtilizAvgPercent_Object = MibTableColumn
apexOutputTsUtilizAvgPercent = _ApexOutputTsUtilizAvgPercent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 7),
    _ApexOutputTsUtilizAvgPercent_Type()
)
apexOutputTsUtilizAvgPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizAvgPercent.setStatus("current")


class _ApexOutputTsUtilizMinPercent_Type(Integer32):
    """Custom type apexOutputTsUtilizMinPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexOutputTsUtilizMinPercent_Type.__name__ = "Integer32"
_ApexOutputTsUtilizMinPercent_Object = MibTableColumn
apexOutputTsUtilizMinPercent = _ApexOutputTsUtilizMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 8),
    _ApexOutputTsUtilizMinPercent_Type()
)
apexOutputTsUtilizMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizMinPercent.setStatus("current")


class _ApexOutputTsUtilizPeakPercent_Type(Integer32):
    """Custom type apexOutputTsUtilizPeakPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApexOutputTsUtilizPeakPercent_Type.__name__ = "Integer32"
_ApexOutputTsUtilizPeakPercent_Object = MibTableColumn
apexOutputTsUtilizPeakPercent = _ApexOutputTsUtilizPeakPercent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 9),
    _ApexOutputTsUtilizPeakPercent_Type()
)
apexOutputTsUtilizPeakPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizPeakPercent.setStatus("current")
_ApexOutputTsUtilizCurRate_Type = Unsigned32
_ApexOutputTsUtilizCurRate_Object = MibTableColumn
apexOutputTsUtilizCurRate = _ApexOutputTsUtilizCurRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 10),
    _ApexOutputTsUtilizCurRate_Type()
)
apexOutputTsUtilizCurRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizCurRate.setStatus("current")
_ApexOutputTsUtilizAvgRate_Type = Unsigned32
_ApexOutputTsUtilizAvgRate_Object = MibTableColumn
apexOutputTsUtilizAvgRate = _ApexOutputTsUtilizAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 11),
    _ApexOutputTsUtilizAvgRate_Type()
)
apexOutputTsUtilizAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizAvgRate.setStatus("current")
_ApexOutputTsUtilizMinRate_Type = Unsigned32
_ApexOutputTsUtilizMinRate_Object = MibTableColumn
apexOutputTsUtilizMinRate = _ApexOutputTsUtilizMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 12),
    _ApexOutputTsUtilizMinRate_Type()
)
apexOutputTsUtilizMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizMinRate.setStatus("current")
_ApexOutputTsUtilizPeakRate_Type = Unsigned32
_ApexOutputTsUtilizPeakRate_Object = MibTableColumn
apexOutputTsUtilizPeakRate = _ApexOutputTsUtilizPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 13),
    _ApexOutputTsUtilizPeakRate_Type()
)
apexOutputTsUtilizPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizPeakRate.setStatus("current")


class _ApexOutputTsUtilizOverflow_Type(Integer32):
    """Custom type apexOutputTsUtilizOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("notApplicable", 0),
          ("overflow", 2))
    )


_ApexOutputTsUtilizOverflow_Type.__name__ = "Integer32"
_ApexOutputTsUtilizOverflow_Object = MibTableColumn
apexOutputTsUtilizOverflow = _ApexOutputTsUtilizOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 14),
    _ApexOutputTsUtilizOverflow_Type()
)
apexOutputTsUtilizOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizOverflow.setStatus("current")
_ApexOutputTsUtilizCurDropPackets_Type = Unsigned32
_ApexOutputTsUtilizCurDropPackets_Object = MibTableColumn
apexOutputTsUtilizCurDropPackets = _ApexOutputTsUtilizCurDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 15),
    _ApexOutputTsUtilizCurDropPackets_Type()
)
apexOutputTsUtilizCurDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizCurDropPackets.setStatus("current")
_ApexOutputTsUtilizPeakDropPackets_Type = Unsigned32
_ApexOutputTsUtilizPeakDropPackets_Object = MibTableColumn
apexOutputTsUtilizPeakDropPackets = _ApexOutputTsUtilizPeakDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 16),
    _ApexOutputTsUtilizPeakDropPackets_Type()
)
apexOutputTsUtilizPeakDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizPeakDropPackets.setStatus("current")
_ApexOutputTsUtilizRollingDropPackets_Type = Unsigned32
_ApexOutputTsUtilizRollingDropPackets_Object = MibTableColumn
apexOutputTsUtilizRollingDropPackets = _ApexOutputTsUtilizRollingDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 17),
    _ApexOutputTsUtilizRollingDropPackets_Type()
)
apexOutputTsUtilizRollingDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizRollingDropPackets.setStatus("current")
_ApexOutputTsUtilizTotalDropPackets_Type = Unsigned32
_ApexOutputTsUtilizTotalDropPackets_Object = MibTableColumn
apexOutputTsUtilizTotalDropPackets = _ApexOutputTsUtilizTotalDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 18),
    _ApexOutputTsUtilizTotalDropPackets_Type()
)
apexOutputTsUtilizTotalDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizTotalDropPackets.setStatus("current")


class _ApexOutputTsUtilizThresholdAlarm_Type(Integer32):
    """Custom type apexOutputTsUtilizThresholdAlarm based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexOutputTsUtilizThresholdAlarm_Type.__name__ = "Integer32"
_ApexOutputTsUtilizThresholdAlarm_Object = MibTableColumn
apexOutputTsUtilizThresholdAlarm = _ApexOutputTsUtilizThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 19),
    _ApexOutputTsUtilizThresholdAlarm_Type()
)
apexOutputTsUtilizThresholdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizThresholdAlarm.setStatus("current")


class _ApexOutputTsUtilizOverflowAlarm_Type(Integer32):
    """Custom type apexOutputTsUtilizOverflowAlarm based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexOutputTsUtilizOverflowAlarm_Type.__name__ = "Integer32"
_ApexOutputTsUtilizOverflowAlarm_Object = MibTableColumn
apexOutputTsUtilizOverflowAlarm = _ApexOutputTsUtilizOverflowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 2, 2, 1, 20),
    _ApexOutputTsUtilizOverflowAlarm_Type()
)
apexOutputTsUtilizOverflowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsUtilizOverflowAlarm.setStatus("current")
_ApexOutputTsStatusTable_Object = MibTable
apexOutputTsStatusTable = _ApexOutputTsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5)
)
if mibBuilder.loadTexts:
    apexOutputTsStatusTable.setStatus("current")
_ApexOutputTsStatusEntry_Object = MibTableRow
apexOutputTsStatusEntry = _ApexOutputTsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1)
)
apexOutputTsStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsStatusOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexOutputTsStatusEntry.setStatus("current")


class _ApexOutputTsStatusOutputTsNum_Type(Integer32):
    """Custom type apexOutputTsStatusOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexOutputTsStatusOutputTsNum_Type.__name__ = "Integer32"
_ApexOutputTsStatusOutputTsNum_Object = MibTableColumn
apexOutputTsStatusOutputTsNum = _ApexOutputTsStatusOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 1),
    _ApexOutputTsStatusOutputTsNum_Type()
)
apexOutputTsStatusOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsStatusOutputTsNum.setStatus("current")
_ApexOutputTsStatusProgramsPerTs_Type = Integer32
_ApexOutputTsStatusProgramsPerTs_Object = MibTableColumn
apexOutputTsStatusProgramsPerTs = _ApexOutputTsStatusProgramsPerTs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 2),
    _ApexOutputTsStatusProgramsPerTs_Type()
)
apexOutputTsStatusProgramsPerTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusProgramsPerTs.setStatus("current")
_ApexOutputTsStatusServicesMapped_Type = Integer32
_ApexOutputTsStatusServicesMapped_Object = MibTableColumn
apexOutputTsStatusServicesMapped = _ApexOutputTsStatusServicesMapped_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 3),
    _ApexOutputTsStatusServicesMapped_Type()
)
apexOutputTsStatusServicesMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusServicesMapped.setStatus("current")
_ApexOutputTsStatusAncillaryPidsMapped_Type = Integer32
_ApexOutputTsStatusAncillaryPidsMapped_Object = MibTableColumn
apexOutputTsStatusAncillaryPidsMapped = _ApexOutputTsStatusAncillaryPidsMapped_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 4),
    _ApexOutputTsStatusAncillaryPidsMapped_Type()
)
apexOutputTsStatusAncillaryPidsMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusAncillaryPidsMapped.setStatus("current")
_ApexOutputTsStatusInputStreamsMapped_Type = Integer32
_ApexOutputTsStatusInputStreamsMapped_Object = MibTableColumn
apexOutputTsStatusInputStreamsMapped = _ApexOutputTsStatusInputStreamsMapped_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 5),
    _ApexOutputTsStatusInputStreamsMapped_Type()
)
apexOutputTsStatusInputStreamsMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusInputStreamsMapped.setStatus("current")


class _ApexOutputTsStatusFault_Type(Integer32):
    """Custom type apexOutputTsStatusFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexOutputTsStatusFault_Type.__name__ = "Integer32"
_ApexOutputTsStatusFault_Object = MibTableColumn
apexOutputTsStatusFault = _ApexOutputTsStatusFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 6),
    _ApexOutputTsStatusFault_Type()
)
apexOutputTsStatusFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusFault.setStatus("current")
_ApexOutputTsStatusServicesInError_Type = Integer32
_ApexOutputTsStatusServicesInError_Object = MibTableColumn
apexOutputTsStatusServicesInError = _ApexOutputTsStatusServicesInError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 7),
    _ApexOutputTsStatusServicesInError_Type()
)
apexOutputTsStatusServicesInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusServicesInError.setStatus("current")
_ApexOutputTsStatusDepiSessionsMapped_Type = Integer32
_ApexOutputTsStatusDepiSessionsMapped_Object = MibTableColumn
apexOutputTsStatusDepiSessionsMapped = _ApexOutputTsStatusDepiSessionsMapped_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 8),
    _ApexOutputTsStatusDepiSessionsMapped_Type()
)
apexOutputTsStatusDepiSessionsMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusDepiSessionsMapped.setStatus("current")
_ApexOutputTsStatusMessageGenerationNum_Type = Integer32
_ApexOutputTsStatusMessageGenerationNum_Object = MibTableColumn
apexOutputTsStatusMessageGenerationNum = _ApexOutputTsStatusMessageGenerationNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 9),
    _ApexOutputTsStatusMessageGenerationNum_Type()
)
apexOutputTsStatusMessageGenerationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusMessageGenerationNum.setStatus("current")
_ApexOutputTsStatusScgsProvisioned_Type = Integer32
_ApexOutputTsStatusScgsProvisioned_Object = MibTableColumn
apexOutputTsStatusScgsProvisioned = _ApexOutputTsStatusScgsProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 10),
    _ApexOutputTsStatusScgsProvisioned_Type()
)
apexOutputTsStatusScgsProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusScgsProvisioned.setStatus("current")
_ApexOutputTsStatusServicesMuxed_Type = Integer32
_ApexOutputTsStatusServicesMuxed_Object = MibTableColumn
apexOutputTsStatusServicesMuxed = _ApexOutputTsStatusServicesMuxed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 14, 2, 5, 1, 11),
    _ApexOutputTsStatusServicesMuxed_Type()
)
apexOutputTsStatusServicesMuxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsStatusServicesMuxed.setStatus("current")
_ApexPsi_ObjectIdentity = ObjectIdentity
apexPsi = _ApexPsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15)
)
_ApexPsiConfig_ObjectIdentity = ObjectIdentity
apexPsiConfig = _ApexPsiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1)
)
_ApexPsiConfigGeneral_ObjectIdentity = ObjectIdentity
apexPsiConfigGeneral = _ApexPsiConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1)
)
_ApexPsiDetectionEnabled_Type = EnableDisableTYPE
_ApexPsiDetectionEnabled_Object = MibScalar
apexPsiDetectionEnabled = _ApexPsiDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 1),
    _ApexPsiDetectionEnabled_Type()
)
apexPsiDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsiDetectionEnabled.setStatus("current")


class _ApexPsiDetectionTimeout_Type(Integer32):
    """Custom type apexPsiDetectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21600),
    )


_ApexPsiDetectionTimeout_Type.__name__ = "Integer32"
_ApexPsiDetectionTimeout_Object = MibScalar
apexPsiDetectionTimeout = _ApexPsiDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 2),
    _ApexPsiDetectionTimeout_Type()
)
apexPsiDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsiDetectionTimeout.setStatus("current")


class _ApexPsiRangeStart_Type(Integer32):
    """Custom type apexPsiRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApexPsiRangeStart_Type.__name__ = "Integer32"
_ApexPsiRangeStart_Object = MibScalar
apexPsiRangeStart = _ApexPsiRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 3),
    _ApexPsiRangeStart_Type()
)
apexPsiRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsiRangeStart.setStatus("current")


class _ApexPsiRangeStop_Type(Integer32):
    """Custom type apexPsiRangeStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApexPsiRangeStop_Type.__name__ = "Integer32"
_ApexPsiRangeStop_Object = MibScalar
apexPsiRangeStop = _ApexPsiRangeStop_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 4),
    _ApexPsiRangeStop_Type()
)
apexPsiRangeStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsiRangeStop.setStatus("current")


class _ApexPatVersionIncrement_Type(Integer32):
    """Custom type apexPatVersionIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApexPatVersionIncrement_Type.__name__ = "Integer32"
_ApexPatVersionIncrement_Object = MibScalar
apexPatVersionIncrement = _ApexPatVersionIncrement_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 5),
    _ApexPatVersionIncrement_Type()
)
apexPatVersionIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPatVersionIncrement.setStatus("current")


class _ApexPmtVersionIncrement_Type(Integer32):
    """Custom type apexPmtVersionIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApexPmtVersionIncrement_Type.__name__ = "Integer32"
_ApexPmtVersionIncrement_Object = MibScalar
apexPmtVersionIncrement = _ApexPmtVersionIncrement_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 6),
    _ApexPmtVersionIncrement_Type()
)
apexPmtVersionIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPmtVersionIncrement.setStatus("current")


class _ApexEcmEmmFirstPid_Type(Integer32):
    """Custom type apexEcmEmmFirstPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8191),
    )


_ApexEcmEmmFirstPid_Type.__name__ = "Integer32"
_ApexEcmEmmFirstPid_Object = MibScalar
apexEcmEmmFirstPid = _ApexEcmEmmFirstPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 7),
    _ApexEcmEmmFirstPid_Type()
)
apexEcmEmmFirstPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEcmEmmFirstPid.setStatus("current")
_ApexEcmEmmNumberPids_Type = Integer32
_ApexEcmEmmNumberPids_Object = MibScalar
apexEcmEmmNumberPids = _ApexEcmEmmNumberPids_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 8),
    _ApexEcmEmmNumberPids_Type()
)
apexEcmEmmNumberPids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEcmEmmNumberPids.setStatus("current")


class _ApexProgramBasedPmtOffset_Type(Integer32):
    """Custom type apexProgramBasedPmtOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_ApexProgramBasedPmtOffset_Type.__name__ = "Integer32"
_ApexProgramBasedPmtOffset_Object = MibScalar
apexProgramBasedPmtOffset = _ApexProgramBasedPmtOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 1, 1, 9),
    _ApexProgramBasedPmtOffset_Type()
)
apexProgramBasedPmtOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexProgramBasedPmtOffset.setStatus("current")
_ApexPsiStatus_ObjectIdentity = ObjectIdentity
apexPsiStatus = _ApexPsiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2)
)
_ApexPsiStatusGeneral_ObjectIdentity = ObjectIdentity
apexPsiStatusGeneral = _ApexPsiStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 1)
)
_ApexPsiStatusTable_Object = MibTable
apexPsiStatusTable = _ApexPsiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2)
)
if mibBuilder.loadTexts:
    apexPsiStatusTable.setStatus("current")
_ApexPsiStatusEntry_Object = MibTableRow
apexPsiStatusEntry = _ApexPsiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1)
)
apexPsiStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsiStatusTableType"),
    (0, "APEX-MIB", "apexPsiStatusIndex"),
    (0, "APEX-MIB", "apexPsiStatusPid"),
    (0, "APEX-MIB", "apexPsiStatusMessageType"),
    (0, "APEX-MIB", "apexPsiStatusProgramNumber"),
    (0, "APEX-MIB", "apexPsiStatusSegment"),
    (0, "APEX-MIB", "apexPsiStatusPart"),
)
if mibBuilder.loadTexts:
    apexPsiStatusEntry.setStatus("current")


class _ApexPsiStatusTableType_Type(Integer32):
    """Custom type apexPsiStatusTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputPsiTable", 1),
          ("outputPsiTable", 2))
    )


_ApexPsiStatusTableType_Type.__name__ = "Integer32"
_ApexPsiStatusTableType_Object = MibTableColumn
apexPsiStatusTableType = _ApexPsiStatusTableType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 1),
    _ApexPsiStatusTableType_Type()
)
apexPsiStatusTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusTableType.setStatus("current")


class _ApexPsiStatusIndex_Type(Integer32):
    """Custom type apexPsiStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 784),
    )


_ApexPsiStatusIndex_Type.__name__ = "Integer32"
_ApexPsiStatusIndex_Object = MibTableColumn
apexPsiStatusIndex = _ApexPsiStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 2),
    _ApexPsiStatusIndex_Type()
)
apexPsiStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusIndex.setStatus("current")


class _ApexPsiStatusPid_Type(Integer32):
    """Custom type apexPsiStatusPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ApexPsiStatusPid_Type.__name__ = "Integer32"
_ApexPsiStatusPid_Object = MibTableColumn
apexPsiStatusPid = _ApexPsiStatusPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 3),
    _ApexPsiStatusPid_Type()
)
apexPsiStatusPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusPid.setStatus("current")


class _ApexPsiStatusMessageType_Type(Integer32):
    """Custom type apexPsiStatusMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexPsiStatusMessageType_Type.__name__ = "Integer32"
_ApexPsiStatusMessageType_Object = MibTableColumn
apexPsiStatusMessageType = _ApexPsiStatusMessageType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 4),
    _ApexPsiStatusMessageType_Type()
)
apexPsiStatusMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusMessageType.setStatus("current")


class _ApexPsiStatusProgramNumber_Type(Integer32):
    """Custom type apexPsiStatusProgramNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexPsiStatusProgramNumber_Type.__name__ = "Integer32"
_ApexPsiStatusProgramNumber_Object = MibTableColumn
apexPsiStatusProgramNumber = _ApexPsiStatusProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 5),
    _ApexPsiStatusProgramNumber_Type()
)
apexPsiStatusProgramNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusProgramNumber.setStatus("current")


class _ApexPsiStatusSegment_Type(Integer32):
    """Custom type apexPsiStatusSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApexPsiStatusSegment_Type.__name__ = "Integer32"
_ApexPsiStatusSegment_Object = MibTableColumn
apexPsiStatusSegment = _ApexPsiStatusSegment_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 6),
    _ApexPsiStatusSegment_Type()
)
apexPsiStatusSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusSegment.setStatus("current")


class _ApexPsiStatusPart_Type(Integer32):
    """Custom type apexPsiStatusPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApexPsiStatusPart_Type.__name__ = "Integer32"
_ApexPsiStatusPart_Object = MibTableColumn
apexPsiStatusPart = _ApexPsiStatusPart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 7),
    _ApexPsiStatusPart_Type()
)
apexPsiStatusPart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsiStatusPart.setStatus("current")
_ApexPsiStatusBody_Type = DisplayString
_ApexPsiStatusBody_Object = MibTableColumn
apexPsiStatusBody = _ApexPsiStatusBody_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 8),
    _ApexPsiStatusBody_Type()
)
apexPsiStatusBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsiStatusBody.setStatus("current")
_ApexPsiStatusGpsTime_Type = Integer32
_ApexPsiStatusGpsTime_Object = MibTableColumn
apexPsiStatusGpsTime = _ApexPsiStatusGpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 15, 2, 2, 1, 9),
    _ApexPsiStatusGpsTime_Type()
)
apexPsiStatusGpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsiStatusGpsTime.setStatus("current")
_ApexOutputProgram_ObjectIdentity = ObjectIdentity
apexOutputProgram = _ApexOutputProgram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16)
)
_ApexOutputProgramConfig_ObjectIdentity = ObjectIdentity
apexOutputProgramConfig = _ApexOutputProgramConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 1)
)
_ApexOutputProgramConfigGeneral_ObjectIdentity = ObjectIdentity
apexOutputProgramConfigGeneral = _ApexOutputProgramConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 1, 1)
)
_ApexOutputProgramStatus_ObjectIdentity = ObjectIdentity
apexOutputProgramStatus = _ApexOutputProgramStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2)
)
_ApexOutputProgramStatusGeneral_ObjectIdentity = ObjectIdentity
apexOutputProgramStatusGeneral = _ApexOutputProgramStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 1)
)
_ApexOutputProgramTable_Object = MibTable
apexOutputProgramTable = _ApexOutputProgramTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2)
)
if mibBuilder.loadTexts:
    apexOutputProgramTable.setStatus("current")
_ApexOutputProgramEntry_Object = MibTableRow
apexOutputProgramEntry = _ApexOutputProgramEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1)
)
apexOutputProgramEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputProgramIndex"),
)
if mibBuilder.loadTexts:
    apexOutputProgramEntry.setStatus("current")


class _ApexOutputProgramIndex_Type(Integer32):
    """Custom type apexOutputProgramIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexOutputProgramIndex_Type.__name__ = "Integer32"
_ApexOutputProgramIndex_Object = MibTableColumn
apexOutputProgramIndex = _ApexOutputProgramIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 1),
    _ApexOutputProgramIndex_Type()
)
apexOutputProgramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputProgramIndex.setStatus("current")
_ApexOutputProgramInputTsIndex_Type = Integer32
_ApexOutputProgramInputTsIndex_Object = MibTableColumn
apexOutputProgramInputTsIndex = _ApexOutputProgramInputTsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 2),
    _ApexOutputProgramInputTsIndex_Type()
)
apexOutputProgramInputTsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramInputTsIndex.setStatus("current")
_ApexOutputProgramInputProgNum_Type = Integer32
_ApexOutputProgramInputProgNum_Object = MibTableColumn
apexOutputProgramInputProgNum = _ApexOutputProgramInputProgNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 3),
    _ApexOutputProgramInputProgNum_Type()
)
apexOutputProgramInputProgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramInputProgNum.setStatus("current")
_ApexOutputProgramOutputProgNum_Type = Integer32
_ApexOutputProgramOutputProgNum_Object = MibTableColumn
apexOutputProgramOutputProgNum = _ApexOutputProgramOutputProgNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 4),
    _ApexOutputProgramOutputProgNum_Type()
)
apexOutputProgramOutputProgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramOutputProgNum.setStatus("current")


class _ApexOutputProgramRoutingStatus_Type(DisplayString):
    """Custom type apexOutputProgramRoutingStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexOutputProgramRoutingStatus_Type.__name__ = "DisplayString"
_ApexOutputProgramRoutingStatus_Object = MibTableColumn
apexOutputProgramRoutingStatus = _ApexOutputProgramRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 5),
    _ApexOutputProgramRoutingStatus_Type()
)
apexOutputProgramRoutingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramRoutingStatus.setStatus("current")


class _ApexOutputProgramInputPreEncrypted_Type(Integer32):
    """Custom type apexOutputProgramInputPreEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("notApplicable", 0),
          ("preEncrypted", 2))
    )


_ApexOutputProgramInputPreEncrypted_Type.__name__ = "Integer32"
_ApexOutputProgramInputPreEncrypted_Object = MibTableColumn
apexOutputProgramInputPreEncrypted = _ApexOutputProgramInputPreEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 6),
    _ApexOutputProgramInputPreEncrypted_Type()
)
apexOutputProgramInputPreEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramInputPreEncrypted.setStatus("current")


class _ApexOutputProgramOutputTsNum_Type(Integer32):
    """Custom type apexOutputProgramOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexOutputProgramOutputTsNum_Type.__name__ = "Integer32"
_ApexOutputProgramOutputTsNum_Object = MibTableColumn
apexOutputProgramOutputTsNum = _ApexOutputProgramOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 7),
    _ApexOutputProgramOutputTsNum_Type()
)
apexOutputProgramOutputTsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramOutputTsNum.setStatus("current")


class _ApexOutputProgramError_Type(Integer32):
    """Custom type apexOutputProgramError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexOutputProgramError_Type.__name__ = "Integer32"
_ApexOutputProgramError_Object = MibTableColumn
apexOutputProgramError = _ApexOutputProgramError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 8),
    _ApexOutputProgramError_Type()
)
apexOutputProgramError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramError.setStatus("current")


class _ApexOutputProgramEncryptionMode_Type(Integer32):
    """Custom type apexOutputProgramEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clear", 4),
          ("fpk", 3),
          ("full", 1),
          ("fwk", 2),
          ("none", 0),
          ("preEncrypted", 6),
          ("unencrypted", 5),
          ("unencryptedWithCci", 7))
    )


_ApexOutputProgramEncryptionMode_Type.__name__ = "Integer32"
_ApexOutputProgramEncryptionMode_Object = MibTableColumn
apexOutputProgramEncryptionMode = _ApexOutputProgramEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 9),
    _ApexOutputProgramEncryptionMode_Type()
)
apexOutputProgramEncryptionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramEncryptionMode.setStatus("current")


class _ApexOutputProgramEncryptionStatus_Type(DisplayString):
    """Custom type apexOutputProgramEncryptionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexOutputProgramEncryptionStatus_Type.__name__ = "DisplayString"
_ApexOutputProgramEncryptionStatus_Object = MibTableColumn
apexOutputProgramEncryptionStatus = _ApexOutputProgramEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 10),
    _ApexOutputProgramEncryptionStatus_Type()
)
apexOutputProgramEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramEncryptionStatus.setStatus("current")
_ApexOutputProgramEcmServiceId_Type = Integer32
_ApexOutputProgramEcmServiceId_Object = MibTableColumn
apexOutputProgramEcmServiceId = _ApexOutputProgramEcmServiceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 11),
    _ApexOutputProgramEcmServiceId_Type()
)
apexOutputProgramEcmServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramEcmServiceId.setStatus("current")


class _ApexOutputProgramCciLevel_Type(Integer32):
    """Custom type apexOutputProgramCciLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyFreely", 2),
          ("copyNever", 4),
          ("copyOnce", 3),
          ("noMoreCopies", 5),
          ("notApplicable", 0),
          ("notDefined", 1))
    )


_ApexOutputProgramCciLevel_Type.__name__ = "Integer32"
_ApexOutputProgramCciLevel_Object = MibTableColumn
apexOutputProgramCciLevel = _ApexOutputProgramCciLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 12),
    _ApexOutputProgramCciLevel_Type()
)
apexOutputProgramCciLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramCciLevel.setStatus("current")


class _ApexOutputProgramApsLevel_Type(Integer32):
    """Custom type apexOutputProgramApsLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notDefined", 1),
          ("off", 2),
          ("splitBurst2Line", 4),
          ("splitBurst4Line", 5),
          ("splitBurstOff", 3))
    )


_ApexOutputProgramApsLevel_Type.__name__ = "Integer32"
_ApexOutputProgramApsLevel_Object = MibTableColumn
apexOutputProgramApsLevel = _ApexOutputProgramApsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 13),
    _ApexOutputProgramApsLevel_Type()
)
apexOutputProgramApsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramApsLevel.setStatus("current")


class _ApexOutputProgramCitSetting_Type(Integer32):
    """Custom type apexOutputProgramCitSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("notApplicable", 0))
    )


_ApexOutputProgramCitSetting_Type.__name__ = "Integer32"
_ApexOutputProgramCitSetting_Object = MibTableColumn
apexOutputProgramCitSetting = _ApexOutputProgramCitSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 14),
    _ApexOutputProgramCitSetting_Type()
)
apexOutputProgramCitSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramCitSetting.setStatus("current")
_ApexOutputProgramNumberTiers_Type = Integer32
_ApexOutputProgramNumberTiers_Object = MibTableColumn
apexOutputProgramNumberTiers = _ApexOutputProgramNumberTiers_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 15),
    _ApexOutputProgramNumberTiers_Type()
)
apexOutputProgramNumberTiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramNumberTiers.setStatus("current")
_ApexOutputProgramTierData_Type = DisplayString
_ApexOutputProgramTierData_Object = MibTableColumn
apexOutputProgramTierData = _ApexOutputProgramTierData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 16),
    _ApexOutputProgramTierData_Type()
)
apexOutputProgramTierData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramTierData.setStatus("current")


class _ApexOutputProgramSourceId_Type(Integer32):
    """Custom type apexOutputProgramSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexOutputProgramSourceId_Type.__name__ = "Integer32"
_ApexOutputProgramSourceId_Object = MibTableColumn
apexOutputProgramSourceId = _ApexOutputProgramSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 17),
    _ApexOutputProgramSourceId_Type()
)
apexOutputProgramSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramSourceId.setStatus("current")


class _ApexOutputProgramProviderId_Type(Integer32):
    """Custom type apexOutputProgramProviderId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexOutputProgramProviderId_Type.__name__ = "Integer32"
_ApexOutputProgramProviderId_Object = MibTableColumn
apexOutputProgramProviderId = _ApexOutputProgramProviderId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 18),
    _ApexOutputProgramProviderId_Type()
)
apexOutputProgramProviderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramProviderId.setStatus("current")


class _ApexOutputProgramProgramType_Type(Integer32):
    """Custom type apexOutputProgramProgramType based on Integer32"""
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
        *(("programEcmProvided", 3),
          ("programInfoAndEcmProvided", 4),
          ("programInfoProvided", 2),
          ("programsDerived", 1))
    )


_ApexOutputProgramProgramType_Type.__name__ = "Integer32"
_ApexOutputProgramProgramType_Object = MibTableColumn
apexOutputProgramProgramType = _ApexOutputProgramProgramType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 19),
    _ApexOutputProgramProgramType_Type()
)
apexOutputProgramProgramType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramProgramType.setStatus("current")


class _ApexOutputProgramDtaEncryptionMode_Type(Integer32):
    """Custom type apexOutputProgramDtaEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtaWithCcm", 1),
          ("dtaWithoutCcm", 2),
          ("notApplicable", 0))
    )


_ApexOutputProgramDtaEncryptionMode_Type.__name__ = "Integer32"
_ApexOutputProgramDtaEncryptionMode_Object = MibTableColumn
apexOutputProgramDtaEncryptionMode = _ApexOutputProgramDtaEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 16, 2, 2, 1, 20),
    _ApexOutputProgramDtaEncryptionMode_Type()
)
apexOutputProgramDtaEncryptionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputProgramDtaEncryptionMode.setStatus("current")
_ApexAcp_ObjectIdentity = ObjectIdentity
apexAcp = _ApexAcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17)
)
_ApexAcpConfig_ObjectIdentity = ObjectIdentity
apexAcpConfig = _ApexAcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 1)
)
_ApexAcpConfigGeneral_ObjectIdentity = ObjectIdentity
apexAcpConfigGeneral = _ApexAcpConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 1, 1)
)
_ApexAcpStatus_ObjectIdentity = ObjectIdentity
apexAcpStatus = _ApexAcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2)
)
_ApexAcpStatusGeneral_ObjectIdentity = ObjectIdentity
apexAcpStatusGeneral = _ApexAcpStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 1)
)
_ApexAcpStatusTable_Object = MibTable
apexAcpStatusTable = _ApexAcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2)
)
if mibBuilder.loadTexts:
    apexAcpStatusTable.setStatus("current")
_ApexAcpStatusEntry_Object = MibTableRow
apexAcpStatusEntry = _ApexAcpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1)
)
apexAcpStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexAcpStatusIndex"),
)
if mibBuilder.loadTexts:
    apexAcpStatusEntry.setStatus("current")


class _ApexAcpStatusIndex_Type(Integer32):
    """Custom type apexAcpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexAcpStatusIndex_Type.__name__ = "Integer32"
_ApexAcpStatusIndex_Object = MibTableColumn
apexAcpStatusIndex = _ApexAcpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 1),
    _ApexAcpStatusIndex_Type()
)
apexAcpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexAcpStatusIndex.setStatus("current")


class _ApexAcpUnitAddress_Type(DisplayString):
    """Custom type apexAcpUnitAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ApexAcpUnitAddress_Type.__name__ = "DisplayString"
_ApexAcpUnitAddress_Object = MibTableColumn
apexAcpUnitAddress = _ApexAcpUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 2),
    _ApexAcpUnitAddress_Type()
)
apexAcpUnitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAcpUnitAddress.setStatus("current")
_ApexAcpHealthByte_Type = Integer32
_ApexAcpHealthByte_Object = MibTableColumn
apexAcpHealthByte = _ApexAcpHealthByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 3),
    _ApexAcpHealthByte_Type()
)
apexAcpHealthByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAcpHealthByte.setStatus("current")
_ApexAcpEvenCsn_Type = Integer32
_ApexAcpEvenCsn_Object = MibTableColumn
apexAcpEvenCsn = _ApexAcpEvenCsn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 4),
    _ApexAcpEvenCsn_Type()
)
apexAcpEvenCsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAcpEvenCsn.setStatus("current")
_ApexAcpOddCsn_Type = Integer32
_ApexAcpOddCsn_Object = MibTableColumn
apexAcpOddCsn = _ApexAcpOddCsn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 5),
    _ApexAcpOddCsn_Type()
)
apexAcpOddCsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAcpOddCsn.setStatus("current")
_ApexAcpUnitAttribute_Type = Integer32
_ApexAcpUnitAttribute_Object = MibTableColumn
apexAcpUnitAttribute = _ApexAcpUnitAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 17, 2, 2, 1, 6),
    _ApexAcpUnitAttribute_Type()
)
apexAcpUnitAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAcpUnitAttribute.setStatus("current")
_ApexUdpPortMapping_ObjectIdentity = ObjectIdentity
apexUdpPortMapping = _ApexUdpPortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18)
)
_ApexUdpMapConfig_ObjectIdentity = ObjectIdentity
apexUdpMapConfig = _ApexUdpMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1)
)
_ApexUdpMapConfigGeneral_ObjectIdentity = ObjectIdentity
apexUdpMapConfigGeneral = _ApexUdpMapConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 1)
)
_ApexUdpMapPreEncryptCheck_Type = EnableDisableTYPE
_ApexUdpMapPreEncryptCheck_Object = MibScalar
apexUdpMapPreEncryptCheck = _ApexUdpMapPreEncryptCheck_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 1, 1),
    _ApexUdpMapPreEncryptCheck_Type()
)
apexUdpMapPreEncryptCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapPreEncryptCheck.setStatus("current")


class _ApexUdpMapModeBits_Type(Integer32):
    """Custom type apexUdpMapModeBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ApexUdpMapModeBits_Type.__name__ = "Integer32"
_ApexUdpMapModeBits_Object = MibScalar
apexUdpMapModeBits = _ApexUdpMapModeBits_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 1, 2),
    _ApexUdpMapModeBits_Type()
)
apexUdpMapModeBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapModeBits.setStatus("current")


class _ApexUdpMapTsOffset_Type(Integer32):
    """Custom type apexUdpMapTsOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ApexUdpMapTsOffset_Type.__name__ = "Integer32"
_ApexUdpMapTsOffset_Object = MibScalar
apexUdpMapTsOffset = _ApexUdpMapTsOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 1, 3),
    _ApexUdpMapTsOffset_Type()
)
apexUdpMapTsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapTsOffset.setStatus("current")
_ApexUdpMapFollowDtcp_Type = EnableDisableTYPE
_ApexUdpMapFollowDtcp_Object = MibScalar
apexUdpMapFollowDtcp = _ApexUdpMapFollowDtcp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 1, 4),
    _ApexUdpMapFollowDtcp_Type()
)
apexUdpMapFollowDtcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapFollowDtcp.setStatus("current")
_ApexUdpMapApplyTable_Object = MibTable
apexUdpMapApplyTable = _ApexUdpMapApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 2)
)
if mibBuilder.loadTexts:
    apexUdpMapApplyTable.setStatus("current")
_ApexUdpMapApplyEntry_Object = MibTableRow
apexUdpMapApplyEntry = _ApexUdpMapApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 2, 1)
)
apexUdpMapApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexUdpMapApplyOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexUdpMapApplyEntry.setStatus("current")


class _ApexUdpMapApplyOutputTsNum_Type(Integer32):
    """Custom type apexUdpMapApplyOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexUdpMapApplyOutputTsNum_Type.__name__ = "Integer32"
_ApexUdpMapApplyOutputTsNum_Object = MibTableColumn
apexUdpMapApplyOutputTsNum = _ApexUdpMapApplyOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 2, 1, 1),
    _ApexUdpMapApplyOutputTsNum_Type()
)
apexUdpMapApplyOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexUdpMapApplyOutputTsNum.setStatus("current")
_ApexUdpMapApplyChange_Type = ApplyDataToDeviceTYPE
_ApexUdpMapApplyChange_Object = MibTableColumn
apexUdpMapApplyChange = _ApexUdpMapApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 2, 1, 2),
    _ApexUdpMapApplyChange_Type()
)
apexUdpMapApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapApplyChange.setStatus("current")
_ApexUdpMapTable_Object = MibTable
apexUdpMapTable = _ApexUdpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3)
)
if mibBuilder.loadTexts:
    apexUdpMapTable.setStatus("current")
_ApexUdpMapEntry_Object = MibTableRow
apexUdpMapEntry = _ApexUdpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3, 1)
)
apexUdpMapEntry.setIndexNames(
    (0, "APEX-MIB", "apexUdpMapOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexUdpMapEntry.setStatus("current")


class _ApexUdpMapOutputTsNum_Type(Integer32):
    """Custom type apexUdpMapOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexUdpMapOutputTsNum_Type.__name__ = "Integer32"
_ApexUdpMapOutputTsNum_Object = MibTableColumn
apexUdpMapOutputTsNum = _ApexUdpMapOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3, 1, 1),
    _ApexUdpMapOutputTsNum_Type()
)
apexUdpMapOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexUdpMapOutputTsNum.setStatus("current")


class _ApexUdpMapInputInterface_Type(Integer32):
    """Custom type apexUdpMapInputInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApexUdpMapInputInterface_Type.__name__ = "Integer32"
_ApexUdpMapInputInterface_Object = MibTableColumn
apexUdpMapInputInterface = _ApexUdpMapInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3, 1, 2),
    _ApexUdpMapInputInterface_Type()
)
apexUdpMapInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapInputInterface.setStatus("current")


class _ApexUdpMapStartProgNum_Type(Integer32):
    """Custom type apexUdpMapStartProgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApexUdpMapStartProgNum_Type.__name__ = "Integer32"
_ApexUdpMapStartProgNum_Object = MibTableColumn
apexUdpMapStartProgNum = _ApexUdpMapStartProgNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3, 1, 3),
    _ApexUdpMapStartProgNum_Type()
)
apexUdpMapStartProgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapStartProgNum.setStatus("current")


class _ApexUdpMapNumberProgs_Type(Integer32):
    """Custom type apexUdpMapNumberProgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ApexUdpMapNumberProgs_Type.__name__ = "Integer32"
_ApexUdpMapNumberProgs_Object = MibTableColumn
apexUdpMapNumberProgs = _ApexUdpMapNumberProgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 3, 1, 4),
    _ApexUdpMapNumberProgs_Type()
)
apexUdpMapNumberProgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapNumberProgs.setStatus("current")
_ApexUdpMapMulticastTable_Object = MibTable
apexUdpMapMulticastTable = _ApexUdpMapMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4)
)
if mibBuilder.loadTexts:
    apexUdpMapMulticastTable.setStatus("current")
_ApexUdpMapMulticastEntry_Object = MibTableRow
apexUdpMapMulticastEntry = _ApexUdpMapMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1)
)
apexUdpMapMulticastEntry.setIndexNames(
    (0, "APEX-MIB", "apexUdpMapMulticastIndex"),
)
if mibBuilder.loadTexts:
    apexUdpMapMulticastEntry.setStatus("current")


class _ApexUdpMapMulticastIndex_Type(Integer32):
    """Custom type apexUdpMapMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ApexUdpMapMulticastIndex_Type.__name__ = "Integer32"
_ApexUdpMapMulticastIndex_Object = MibTableColumn
apexUdpMapMulticastIndex = _ApexUdpMapMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 1),
    _ApexUdpMapMulticastIndex_Type()
)
apexUdpMapMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexUdpMapMulticastIndex.setStatus("current")
_ApexUdpMapMulticastEnable_Type = EnableDisableTYPE
_ApexUdpMapMulticastEnable_Object = MibTableColumn
apexUdpMapMulticastEnable = _ApexUdpMapMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 2),
    _ApexUdpMapMulticastEnable_Type()
)
apexUdpMapMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastEnable.setStatus("current")


class _ApexUdpMapMulticastInterface_Type(Integer32):
    """Custom type apexUdpMapMulticastInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexUdpMapMulticastInterface_Type.__name__ = "Integer32"
_ApexUdpMapMulticastInterface_Object = MibTableColumn
apexUdpMapMulticastInterface = _ApexUdpMapMulticastInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 3),
    _ApexUdpMapMulticastInterface_Type()
)
apexUdpMapMulticastInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastInterface.setStatus("current")


class _ApexUdpMapMulticastUdp_Type(Integer32):
    """Custom type apexUdpMapMulticastUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexUdpMapMulticastUdp_Type.__name__ = "Integer32"
_ApexUdpMapMulticastUdp_Object = MibTableColumn
apexUdpMapMulticastUdp = _ApexUdpMapMulticastUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 4),
    _ApexUdpMapMulticastUdp_Type()
)
apexUdpMapMulticastUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastUdp.setStatus("current")
_ApexUdpMapMulticastMcastIp_Type = IpAddress
_ApexUdpMapMulticastMcastIp_Object = MibTableColumn
apexUdpMapMulticastMcastIp = _ApexUdpMapMulticastMcastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 5),
    _ApexUdpMapMulticastMcastIp_Type()
)
apexUdpMapMulticastMcastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastMcastIp.setStatus("current")
_ApexUdpMapMulticastSourceIp_Type = IpAddress
_ApexUdpMapMulticastSourceIp_Object = MibTableColumn
apexUdpMapMulticastSourceIp = _ApexUdpMapMulticastSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 4, 1, 6),
    _ApexUdpMapMulticastSourceIp_Type()
)
apexUdpMapMulticastSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastSourceIp.setStatus("current")
_ApexUdpMapMulticastApplyTable_Object = MibTable
apexUdpMapMulticastApplyTable = _ApexUdpMapMulticastApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 5)
)
if mibBuilder.loadTexts:
    apexUdpMapMulticastApplyTable.setStatus("current")
_ApexUdpMapMulticastApplyEntry_Object = MibTableRow
apexUdpMapMulticastApplyEntry = _ApexUdpMapMulticastApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 5, 1)
)
apexUdpMapMulticastApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexUdpMapMulticastApplyIndex"),
)
if mibBuilder.loadTexts:
    apexUdpMapMulticastApplyEntry.setStatus("current")


class _ApexUdpMapMulticastApplyIndex_Type(Integer32):
    """Custom type apexUdpMapMulticastApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ApexUdpMapMulticastApplyIndex_Type.__name__ = "Integer32"
_ApexUdpMapMulticastApplyIndex_Object = MibTableColumn
apexUdpMapMulticastApplyIndex = _ApexUdpMapMulticastApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 5, 1, 1),
    _ApexUdpMapMulticastApplyIndex_Type()
)
apexUdpMapMulticastApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexUdpMapMulticastApplyIndex.setStatus("current")
_ApexUdpMapMulticastApplyChange_Type = ApplyDataToDeviceTYPE
_ApexUdpMapMulticastApplyChange_Object = MibTableColumn
apexUdpMapMulticastApplyChange = _ApexUdpMapMulticastApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 1, 5, 1, 2),
    _ApexUdpMapMulticastApplyChange_Type()
)
apexUdpMapMulticastApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexUdpMapMulticastApplyChange.setStatus("current")
_ApexUdpMapStatus_ObjectIdentity = ObjectIdentity
apexUdpMapStatus = _ApexUdpMapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2)
)
_ApexUdpMapStatusGeneral_ObjectIdentity = ObjectIdentity
apexUdpMapStatusGeneral = _ApexUdpMapStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 1)
)


class _ApexUdpMapMulticastInvalidApplyText_Type(DisplayString):
    """Custom type apexUdpMapMulticastInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexUdpMapMulticastInvalidApplyText_Type.__name__ = "DisplayString"
_ApexUdpMapMulticastInvalidApplyText_Object = MibScalar
apexUdpMapMulticastInvalidApplyText = _ApexUdpMapMulticastInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 1, 1),
    _ApexUdpMapMulticastInvalidApplyText_Type()
)
apexUdpMapMulticastInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexUdpMapMulticastInvalidApplyText.setStatus("current")
_ApexUdpMapStatusTable_Object = MibTable
apexUdpMapStatusTable = _ApexUdpMapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 2)
)
if mibBuilder.loadTexts:
    apexUdpMapStatusTable.setStatus("current")
_ApexUdpMapStatusEntry_Object = MibTableRow
apexUdpMapStatusEntry = _ApexUdpMapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 2, 1)
)
apexUdpMapStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexUdpMapStatusOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexUdpMapStatusEntry.setStatus("current")


class _ApexUdpMapStatusOutputTsNum_Type(Integer32):
    """Custom type apexUdpMapStatusOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexUdpMapStatusOutputTsNum_Type.__name__ = "Integer32"
_ApexUdpMapStatusOutputTsNum_Object = MibTableColumn
apexUdpMapStatusOutputTsNum = _ApexUdpMapStatusOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 2, 1, 1),
    _ApexUdpMapStatusOutputTsNum_Type()
)
apexUdpMapStatusOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexUdpMapStatusOutputTsNum.setStatus("current")


class _ApexUdpMapInvalidApplyText_Type(DisplayString):
    """Custom type apexUdpMapInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexUdpMapInvalidApplyText_Type.__name__ = "DisplayString"
_ApexUdpMapInvalidApplyText_Object = MibTableColumn
apexUdpMapInvalidApplyText = _ApexUdpMapInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 18, 2, 2, 1, 2),
    _ApexUdpMapInvalidApplyText_Type()
)
apexUdpMapInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexUdpMapInvalidApplyText.setStatus("current")
_ApexRds_ObjectIdentity = ObjectIdentity
apexRds = _ApexRds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19)
)
_ApexRdsConfig_ObjectIdentity = ObjectIdentity
apexRdsConfig = _ApexRdsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1)
)
_ApexRdsConfigGeneral_ObjectIdentity = ObjectIdentity
apexRdsConfigGeneral = _ApexRdsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1)
)
_ApexRdsIpAddr_Type = IpAddress
_ApexRdsIpAddr_Object = MibScalar
apexRdsIpAddr = _ApexRdsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 1),
    _ApexRdsIpAddr_Type()
)
apexRdsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsIpAddr.setStatus("current")


class _ApexRdsTcpPort_Type(Integer32):
    """Custom type apexRdsTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRdsTcpPort_Type.__name__ = "Integer32"
_ApexRdsTcpPort_Object = MibScalar
apexRdsTcpPort = _ApexRdsTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 2),
    _ApexRdsTcpPort_Type()
)
apexRdsTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsTcpPort.setStatus("current")


class _ApexRdsProgramEpochDuration_Type(Integer32):
    """Custom type apexRdsProgramEpochDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1440),
    )


_ApexRdsProgramEpochDuration_Type.__name__ = "Integer32"
_ApexRdsProgramEpochDuration_Object = MibScalar
apexRdsProgramEpochDuration = _ApexRdsProgramEpochDuration_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 3),
    _ApexRdsProgramEpochDuration_Type()
)
apexRdsProgramEpochDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsProgramEpochDuration.setStatus("current")


class _ApexRdsCetPollInterval_Type(Integer32):
    """Custom type apexRdsCetPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_ApexRdsCetPollInterval_Type.__name__ = "Integer32"
_ApexRdsCetPollInterval_Object = MibScalar
apexRdsCetPollInterval = _ApexRdsCetPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 4),
    _ApexRdsCetPollInterval_Type()
)
apexRdsCetPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsCetPollInterval.setStatus("current")


class _ApexRdsCetRefresh_Type(Integer32):
    """Custom type apexRdsCetRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("refresh", 2),
          ("refreshNotInProgress", 1))
    )


_ApexRdsCetRefresh_Type.__name__ = "Integer32"
_ApexRdsCetRefresh_Object = MibScalar
apexRdsCetRefresh = _ApexRdsCetRefresh_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 5),
    _ApexRdsCetRefresh_Type()
)
apexRdsCetRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsCetRefresh.setStatus("current")


class _ApexRdsRmdPollInterval_Type(Integer32):
    """Custom type apexRdsRmdPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_ApexRdsRmdPollInterval_Type.__name__ = "Integer32"
_ApexRdsRmdPollInterval_Object = MibScalar
apexRdsRmdPollInterval = _ApexRdsRmdPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 6),
    _ApexRdsRmdPollInterval_Type()
)
apexRdsRmdPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsRmdPollInterval.setStatus("current")


class _ApexRdsRmdRefresh_Type(Integer32):
    """Custom type apexRdsRmdRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("refresh", 2),
          ("refreshNotInProgress", 1))
    )


_ApexRdsRmdRefresh_Type.__name__ = "Integer32"
_ApexRdsRmdRefresh_Object = MibScalar
apexRdsRmdRefresh = _ApexRdsRmdRefresh_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 7),
    _ApexRdsRmdRefresh_Type()
)
apexRdsRmdRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsRmdRefresh.setStatus("current")


class _ApexRdsPollRandomization_Type(Integer32):
    """Custom type apexRdsPollRandomization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ApexRdsPollRandomization_Type.__name__ = "Integer32"
_ApexRdsPollRandomization_Object = MibScalar
apexRdsPollRandomization = _ApexRdsPollRandomization_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 8),
    _ApexRdsPollRandomization_Type()
)
apexRdsPollRandomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsPollRandomization.setStatus("current")


class _ApexRdsSetDefault_Type(Integer32):
    """Custom type apexRdsSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSettingToDefault", 1),
          ("setToDefault", 2))
    )


_ApexRdsSetDefault_Type.__name__ = "Integer32"
_ApexRdsSetDefault_Object = MibScalar
apexRdsSetDefault = _ApexRdsSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 9),
    _ApexRdsSetDefault_Type()
)
apexRdsSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsSetDefault.setStatus("current")
_ApexRdsErrorCountReset_Type = ResetStatisticsTYPE
_ApexRdsErrorCountReset_Object = MibScalar
apexRdsErrorCountReset = _ApexRdsErrorCountReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 10),
    _ApexRdsErrorCountReset_Type()
)
apexRdsErrorCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsErrorCountReset.setStatus("current")
_ApexRdsConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexRdsConfigApplyChange_Object = MibScalar
apexRdsConfigApplyChange = _ApexRdsConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 11),
    _ApexRdsConfigApplyChange_Type()
)
apexRdsConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsConfigApplyChange.setStatus("current")
_ApexRdsConfigRds2Enable_Type = EnableDisableTYPE
_ApexRdsConfigRds2Enable_Object = MibScalar
apexRdsConfigRds2Enable = _ApexRdsConfigRds2Enable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 12),
    _ApexRdsConfigRds2Enable_Type()
)
apexRdsConfigRds2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsConfigRds2Enable.setStatus("current")


class _ApexRdsConfigServerUrl_Type(DisplayString):
    """Custom type apexRdsConfigServerUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ApexRdsConfigServerUrl_Type.__name__ = "DisplayString"
_ApexRdsConfigServerUrl_Object = MibScalar
apexRdsConfigServerUrl = _ApexRdsConfigServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 13),
    _ApexRdsConfigServerUrl_Type()
)
apexRdsConfigServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsConfigServerUrl.setStatus("current")


class _ApexRdsInitialEcmRetryInterval_Type(Integer32):
    """Custom type apexRdsInitialEcmRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ApexRdsInitialEcmRetryInterval_Type.__name__ = "Integer32"
_ApexRdsInitialEcmRetryInterval_Object = MibScalar
apexRdsInitialEcmRetryInterval = _ApexRdsInitialEcmRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 1, 1, 14),
    _ApexRdsInitialEcmRetryInterval_Type()
)
apexRdsInitialEcmRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexRdsInitialEcmRetryInterval.setStatus("current")
_ApexRdsStatus_ObjectIdentity = ObjectIdentity
apexRdsStatus = _ApexRdsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2)
)
_ApexRdsStatusGeneral_ObjectIdentity = ObjectIdentity
apexRdsStatusGeneral = _ApexRdsStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1)
)


class _ApexRdsConnectionStatus_Type(Integer32):
    """Custom type apexRdsConnectionStatus based on Integer32"""
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
        *(("csnAquisitionFailed", 7),
          ("csnAquisitionSuccessful", 3),
          ("emmAquisitionFailed", 8),
          ("emmAquisitionSuccessful", 4),
          ("notConnectedInHoldoff", 1),
          ("notConnectedNoRdsIpAddress", 2),
          ("rmdAquisitionFailed", 10),
          ("rmdAquisitionSuccessful", 6),
          ("serviceListAquisitionFailed", 9),
          ("serviceListAquisitionSuccessful", 5))
    )


_ApexRdsConnectionStatus_Type.__name__ = "Integer32"
_ApexRdsConnectionStatus_Object = MibScalar
apexRdsConnectionStatus = _ApexRdsConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 1),
    _ApexRdsConnectionStatus_Type()
)
apexRdsConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsConnectionStatus.setStatus("current")


class _ApexRdsCurrentCsn_Type(Integer32):
    """Custom type apexRdsCurrentCsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexRdsCurrentCsn_Type.__name__ = "Integer32"
_ApexRdsCurrentCsn_Object = MibScalar
apexRdsCurrentCsn = _ApexRdsCurrentCsn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 2),
    _ApexRdsCurrentCsn_Type()
)
apexRdsCurrentCsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsCurrentCsn.setStatus("current")
_ApexRdsCetNextPollTime_Type = Integer32
_ApexRdsCetNextPollTime_Object = MibScalar
apexRdsCetNextPollTime = _ApexRdsCetNextPollTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 3),
    _ApexRdsCetNextPollTime_Type()
)
apexRdsCetNextPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsCetNextPollTime.setStatus("current")
_ApexRdsRmdNextPollTime_Type = Integer32
_ApexRdsRmdNextPollTime_Object = MibScalar
apexRdsRmdNextPollTime = _ApexRdsRmdNextPollTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 4),
    _ApexRdsRmdNextPollTime_Type()
)
apexRdsRmdNextPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsRmdNextPollTime.setStatus("current")
_ApexRdsEmmStatusTableSize_Type = Integer32
_ApexRdsEmmStatusTableSize_Object = MibScalar
apexRdsEmmStatusTableSize = _ApexRdsEmmStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 5),
    _ApexRdsEmmStatusTableSize_Type()
)
apexRdsEmmStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusTableSize.setStatus("current")
_ApexRdsProgramMessagesReceived_Type = Counter32
_ApexRdsProgramMessagesReceived_Object = MibScalar
apexRdsProgramMessagesReceived = _ApexRdsProgramMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 6),
    _ApexRdsProgramMessagesReceived_Type()
)
apexRdsProgramMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsProgramMessagesReceived.setStatus("current")
_ApexRdsProgramMessagesFailed_Type = Counter32
_ApexRdsProgramMessagesFailed_Object = MibScalar
apexRdsProgramMessagesFailed = _ApexRdsProgramMessagesFailed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 7),
    _ApexRdsProgramMessagesFailed_Type()
)
apexRdsProgramMessagesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsProgramMessagesFailed.setStatus("current")
_ApexRdsCommErrorCount_Type = Counter32
_ApexRdsCommErrorCount_Object = MibScalar
apexRdsCommErrorCount = _ApexRdsCommErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 8),
    _ApexRdsCommErrorCount_Type()
)
apexRdsCommErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsCommErrorCount.setStatus("current")


class _ApexRdsCommStatus_Type(Integer32):
    """Custom type apexRdsCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("notApplicable", 0),
          ("ok", 1))
    )


_ApexRdsCommStatus_Type.__name__ = "Integer32"
_ApexRdsCommStatus_Object = MibScalar
apexRdsCommStatus = _ApexRdsCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 9),
    _ApexRdsCommStatus_Type()
)
apexRdsCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsCommStatus.setStatus("current")
_ApexRdsFlashWriteCount_Type = Counter32
_ApexRdsFlashWriteCount_Object = MibScalar
apexRdsFlashWriteCount = _ApexRdsFlashWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 10),
    _ApexRdsFlashWriteCount_Type()
)
apexRdsFlashWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsFlashWriteCount.setStatus("current")
_ApexRdsMcast16_Type = Unsigned32
_ApexRdsMcast16_Object = MibScalar
apexRdsMcast16 = _ApexRdsMcast16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 11),
    _ApexRdsMcast16_Type()
)
apexRdsMcast16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsMcast16.setStatus("current")
_ApexRdsStatusServerIp_Type = IpAddress
_ApexRdsStatusServerIp_Object = MibScalar
apexRdsStatusServerIp = _ApexRdsStatusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 12),
    _ApexRdsStatusServerIp_Type()
)
apexRdsStatusServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsStatusServerIp.setStatus("current")


class _ApexRdsStatusServerPort_Type(Integer32):
    """Custom type apexRdsStatusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRdsStatusServerPort_Type.__name__ = "Integer32"
_ApexRdsStatusServerPort_Object = MibScalar
apexRdsStatusServerPort = _ApexRdsStatusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 13),
    _ApexRdsStatusServerPort_Type()
)
apexRdsStatusServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsStatusServerPort.setStatus("current")


class _ApexRdsStatusServerRootDirPath_Type(DisplayString):
    """Custom type apexRdsStatusServerRootDirPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ApexRdsStatusServerRootDirPath_Type.__name__ = "DisplayString"
_ApexRdsStatusServerRootDirPath_Object = MibScalar
apexRdsStatusServerRootDirPath = _ApexRdsStatusServerRootDirPath_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 14),
    _ApexRdsStatusServerRootDirPath_Type()
)
apexRdsStatusServerRootDirPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsStatusServerRootDirPath.setStatus("current")


class _ApexRdsStatusValidation_Type(Integer32):
    """Custom type apexRdsStatusValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("emptyRootPath", 3),
          ("invalidIpClass", 5),
          ("invalidTcpPort", 4),
          ("missingIpOrPath", 2),
          ("notApplicable", 0),
          ("urlValid", 1))
    )


_ApexRdsStatusValidation_Type.__name__ = "Integer32"
_ApexRdsStatusValidation_Object = MibScalar
apexRdsStatusValidation = _ApexRdsStatusValidation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 1, 15),
    _ApexRdsStatusValidation_Type()
)
apexRdsStatusValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsStatusValidation.setStatus("current")
_ApexRdsEmmStatusTable_Object = MibTable
apexRdsEmmStatusTable = _ApexRdsEmmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2)
)
if mibBuilder.loadTexts:
    apexRdsEmmStatusTable.setStatus("current")
_ApexRdsEmmStatusEntry_Object = MibTableRow
apexRdsEmmStatusEntry = _ApexRdsEmmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1)
)
apexRdsEmmStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexRdsEmmStatusIndex"),
)
if mibBuilder.loadTexts:
    apexRdsEmmStatusEntry.setStatus("current")
_ApexRdsEmmStatusIndex_Type = Integer32
_ApexRdsEmmStatusIndex_Object = MibTableColumn
apexRdsEmmStatusIndex = _ApexRdsEmmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 1),
    _ApexRdsEmmStatusIndex_Type()
)
apexRdsEmmStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRdsEmmStatusIndex.setStatus("current")


class _ApexRdsEmmStatusCsn_Type(Integer32):
    """Custom type apexRdsEmmStatusCsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexRdsEmmStatusCsn_Type.__name__ = "Integer32"
_ApexRdsEmmStatusCsn_Object = MibTableColumn
apexRdsEmmStatusCsn = _ApexRdsEmmStatusCsn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 2),
    _ApexRdsEmmStatusCsn_Type()
)
apexRdsEmmStatusCsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusCsn.setStatus("current")


class _ApexRdsEmmStatusState_Type(Integer32):
    """Custom type apexRdsEmmStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("startOfNewEpoch", 3),
          ("transitionComplete", 1),
          ("transitionStart", 2))
    )


_ApexRdsEmmStatusState_Type.__name__ = "Integer32"
_ApexRdsEmmStatusState_Object = MibTableColumn
apexRdsEmmStatusState = _ApexRdsEmmStatusState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 3),
    _ApexRdsEmmStatusState_Type()
)
apexRdsEmmStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusState.setStatus("current")
_ApexRdsEmmStatusGpsTime_Type = Integer32
_ApexRdsEmmStatusGpsTime_Object = MibTableColumn
apexRdsEmmStatusGpsTime = _ApexRdsEmmStatusGpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 4),
    _ApexRdsEmmStatusGpsTime_Type()
)
apexRdsEmmStatusGpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusGpsTime.setStatus("current")
_ApexRdsEmmStatusServerError_Type = Unsigned32
_ApexRdsEmmStatusServerError_Object = MibTableColumn
apexRdsEmmStatusServerError = _ApexRdsEmmStatusServerError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 5),
    _ApexRdsEmmStatusServerError_Type()
)
apexRdsEmmStatusServerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusServerError.setStatus("current")


class _ApexRdsEmmStatusUnitAddress_Type(DisplayString):
    """Custom type apexRdsEmmStatusUnitAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ApexRdsEmmStatusUnitAddress_Type.__name__ = "DisplayString"
_ApexRdsEmmStatusUnitAddress_Object = MibTableColumn
apexRdsEmmStatusUnitAddress = _ApexRdsEmmStatusUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 2, 1, 6),
    _ApexRdsEmmStatusUnitAddress_Type()
)
apexRdsEmmStatusUnitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEmmStatusUnitAddress.setStatus("current")
_ApexRdsSourceLookupTable_Object = MibTable
apexRdsSourceLookupTable = _ApexRdsSourceLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3)
)
if mibBuilder.loadTexts:
    apexRdsSourceLookupTable.setStatus("current")
_ApexRdsSourceLookupEntry_Object = MibTableRow
apexRdsSourceLookupEntry = _ApexRdsSourceLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3, 1)
)
apexRdsSourceLookupEntry.setIndexNames(
    (0, "APEX-MIB", "apexRdsSourceLookupIndex"),
)
if mibBuilder.loadTexts:
    apexRdsSourceLookupEntry.setStatus("current")
_ApexRdsSourceLookupIndex_Type = Integer32
_ApexRdsSourceLookupIndex_Object = MibTableColumn
apexRdsSourceLookupIndex = _ApexRdsSourceLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3, 1, 1),
    _ApexRdsSourceLookupIndex_Type()
)
apexRdsSourceLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRdsSourceLookupIndex.setStatus("current")
_ApexRdsSourceLookupDescription_Type = DisplayString
_ApexRdsSourceLookupDescription_Object = MibTableColumn
apexRdsSourceLookupDescription = _ApexRdsSourceLookupDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3, 1, 2),
    _ApexRdsSourceLookupDescription_Type()
)
apexRdsSourceLookupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsSourceLookupDescription.setStatus("current")
_ApexRdsSourceLookupSourceId_Type = Integer32
_ApexRdsSourceLookupSourceId_Object = MibTableColumn
apexRdsSourceLookupSourceId = _ApexRdsSourceLookupSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3, 1, 3),
    _ApexRdsSourceLookupSourceId_Type()
)
apexRdsSourceLookupSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsSourceLookupSourceId.setStatus("current")
_ApexRdsSourceLookupProviderId_Type = Integer32
_ApexRdsSourceLookupProviderId_Object = MibTableColumn
apexRdsSourceLookupProviderId = _ApexRdsSourceLookupProviderId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 3, 1, 4),
    _ApexRdsSourceLookupProviderId_Type()
)
apexRdsSourceLookupProviderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsSourceLookupProviderId.setStatus("current")
_ApexRdsEventTable_Object = MibTable
apexRdsEventTable = _ApexRdsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4)
)
if mibBuilder.loadTexts:
    apexRdsEventTable.setStatus("current")
_ApexRdsEventEntry_Object = MibTableRow
apexRdsEventEntry = _ApexRdsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1)
)
apexRdsEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexRdsEventProgramIndex"),
    (0, "APEX-MIB", "apexRdsEventEventIndex"),
)
if mibBuilder.loadTexts:
    apexRdsEventEntry.setStatus("current")


class _ApexRdsEventProgramIndex_Type(Integer32):
    """Custom type apexRdsEventProgramIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexRdsEventProgramIndex_Type.__name__ = "Integer32"
_ApexRdsEventProgramIndex_Object = MibTableColumn
apexRdsEventProgramIndex = _ApexRdsEventProgramIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 1),
    _ApexRdsEventProgramIndex_Type()
)
apexRdsEventProgramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRdsEventProgramIndex.setStatus("current")


class _ApexRdsEventEventIndex_Type(Integer32):
    """Custom type apexRdsEventEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexRdsEventEventIndex_Type.__name__ = "Integer32"
_ApexRdsEventEventIndex_Object = MibTableColumn
apexRdsEventEventIndex = _ApexRdsEventEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 2),
    _ApexRdsEventEventIndex_Type()
)
apexRdsEventEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRdsEventEventIndex.setStatus("current")


class _ApexRdsEventEpochNumber_Type(Integer32):
    """Custom type apexRdsEventEpochNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexRdsEventEpochNumber_Type.__name__ = "Integer32"
_ApexRdsEventEpochNumber_Object = MibTableColumn
apexRdsEventEpochNumber = _ApexRdsEventEpochNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 3),
    _ApexRdsEventEpochNumber_Type()
)
apexRdsEventEpochNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventEpochNumber.setStatus("current")
_ApexRdsEventEpochStart_Type = Integer32
_ApexRdsEventEpochStart_Object = MibTableColumn
apexRdsEventEpochStart = _ApexRdsEventEpochStart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 4),
    _ApexRdsEventEpochStart_Type()
)
apexRdsEventEpochStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventEpochStart.setStatus("current")
_ApexRdsEventEpochEnd_Type = Integer32
_ApexRdsEventEpochEnd_Object = MibTableColumn
apexRdsEventEpochEnd = _ApexRdsEventEpochEnd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 5),
    _ApexRdsEventEpochEnd_Type()
)
apexRdsEventEpochEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventEpochEnd.setStatus("current")


class _ApexRdsEventInterstitialDuration_Type(Integer32):
    """Custom type apexRdsEventInterstitialDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRdsEventInterstitialDuration_Type.__name__ = "Integer32"
_ApexRdsEventInterstitialDuration_Object = MibTableColumn
apexRdsEventInterstitialDuration = _ApexRdsEventInterstitialDuration_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 6),
    _ApexRdsEventInterstitialDuration_Type()
)
apexRdsEventInterstitialDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventInterstitialDuration.setStatus("current")


class _ApexRdsEventPreviewDuration_Type(Integer32):
    """Custom type apexRdsEventPreviewDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRdsEventPreviewDuration_Type.__name__ = "Integer32"
_ApexRdsEventPreviewDuration_Object = MibTableColumn
apexRdsEventPreviewDuration = _ApexRdsEventPreviewDuration_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 7),
    _ApexRdsEventPreviewDuration_Type()
)
apexRdsEventPreviewDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventPreviewDuration.setStatus("current")


class _ApexRdsEventPurchaseDuration_Type(Integer32):
    """Custom type apexRdsEventPurchaseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexRdsEventPurchaseDuration_Type.__name__ = "Integer32"
_ApexRdsEventPurchaseDuration_Object = MibTableColumn
apexRdsEventPurchaseDuration = _ApexRdsEventPurchaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 8),
    _ApexRdsEventPurchaseDuration_Type()
)
apexRdsEventPurchaseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventPurchaseDuration.setStatus("current")
_ApexRdsEventNumberTiers_Type = Integer32
_ApexRdsEventNumberTiers_Object = MibTableColumn
apexRdsEventNumberTiers = _ApexRdsEventNumberTiers_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 9),
    _ApexRdsEventNumberTiers_Type()
)
apexRdsEventNumberTiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventNumberTiers.setStatus("current")
_ApexRdsEventTierData_Type = DisplayString
_ApexRdsEventTierData_Object = MibTableColumn
apexRdsEventTierData = _ApexRdsEventTierData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 10),
    _ApexRdsEventTierData_Type()
)
apexRdsEventTierData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventTierData.setStatus("current")
_ApexRdsEventProgramCost_Type = Integer32
_ApexRdsEventProgramCost_Object = MibTableColumn
apexRdsEventProgramCost = _ApexRdsEventProgramCost_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 11),
    _ApexRdsEventProgramCost_Type()
)
apexRdsEventProgramCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventProgramCost.setStatus("current")
_ApexRdsEventRatingRegion_Type = Integer32
_ApexRdsEventRatingRegion_Object = MibTableColumn
apexRdsEventRatingRegion = _ApexRdsEventRatingRegion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 12),
    _ApexRdsEventRatingRegion_Type()
)
apexRdsEventRatingRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventRatingRegion.setStatus("current")
_ApexRdsEventRatingData_Type = DisplayString
_ApexRdsEventRatingData_Object = MibTableColumn
apexRdsEventRatingData = _ApexRdsEventRatingData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 13),
    _ApexRdsEventRatingData_Type()
)
apexRdsEventRatingData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventRatingData.setStatus("current")


class _ApexRdsEventRatingText_Type(DisplayString):
    """Custom type apexRdsEventRatingText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexRdsEventRatingText_Type.__name__ = "DisplayString"
_ApexRdsEventRatingText_Object = MibTableColumn
apexRdsEventRatingText = _ApexRdsEventRatingText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 14),
    _ApexRdsEventRatingText_Type()
)
apexRdsEventRatingText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventRatingText.setStatus("current")
_ApexRdsEventControlByte_Type = DisplayString
_ApexRdsEventControlByte_Object = MibTableColumn
apexRdsEventControlByte = _ApexRdsEventControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 15),
    _ApexRdsEventControlByte_Type()
)
apexRdsEventControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventControlByte.setStatus("current")


class _ApexRdsEventPrkmWkemAvailable_Type(Integer32):
    """Custom type apexRdsEventPrkmWkemAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_ApexRdsEventPrkmWkemAvailable_Type.__name__ = "Integer32"
_ApexRdsEventPrkmWkemAvailable_Object = MibTableColumn
apexRdsEventPrkmWkemAvailable = _ApexRdsEventPrkmWkemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 16),
    _ApexRdsEventPrkmWkemAvailable_Type()
)
apexRdsEventPrkmWkemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventPrkmWkemAvailable.setStatus("current")


class _ApexRdsEventCcmAvailable_Type(Integer32):
    """Custom type apexRdsEventCcmAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_ApexRdsEventCcmAvailable_Type.__name__ = "Integer32"
_ApexRdsEventCcmAvailable_Object = MibTableColumn
apexRdsEventCcmAvailable = _ApexRdsEventCcmAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 19, 2, 4, 1, 17),
    _ApexRdsEventCcmAvailable_Type()
)
apexRdsEventCcmAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRdsEventCcmAvailable.setStatus("current")
_ApexEncryption_ObjectIdentity = ObjectIdentity
apexEncryption = _ApexEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20)
)
_ApexEncryptionConfig_ObjectIdentity = ObjectIdentity
apexEncryptionConfig = _ApexEncryptionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1)
)
_ApexEncryptionConfigGeneral_ObjectIdentity = ObjectIdentity
apexEncryptionConfigGeneral = _ApexEncryptionConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 1)
)


class _ApexEncryptionConfAlgorithm_Type(Integer32):
    """Custom type apexEncryptionConfAlgorithm based on Integer32"""
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
        *(("des-dcii", 1),
          ("des-scte-52", 2),
          ("dvb-csa", 3),
          ("dvb-csa-simulcrypt", 4))
    )


_ApexEncryptionConfAlgorithm_Type.__name__ = "Integer32"
_ApexEncryptionConfAlgorithm_Object = MibScalar
apexEncryptionConfAlgorithm = _ApexEncryptionConfAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 1, 1),
    _ApexEncryptionConfAlgorithm_Type()
)
apexEncryptionConfAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEncryptionConfAlgorithm.setStatus("current")


class _ApexSimulcryptExternalEisSetting_Type(Integer32):
    """Custom type apexSimulcryptExternalEisSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("encrypt", 1))
    )


_ApexSimulcryptExternalEisSetting_Type.__name__ = "Integer32"
_ApexSimulcryptExternalEisSetting_Object = MibScalar
apexSimulcryptExternalEisSetting = _ApexSimulcryptExternalEisSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 1, 2),
    _ApexSimulcryptExternalEisSetting_Type()
)
apexSimulcryptExternalEisSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSimulcryptExternalEisSetting.setStatus("current")
_ApexSimulcryptEmEnable_Type = EnableDisableTYPE
_ApexSimulcryptEmEnable_Object = MibScalar
apexSimulcryptEmEnable = _ApexSimulcryptEmEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 1, 3),
    _ApexSimulcryptEmEnable_Type()
)
apexSimulcryptEmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSimulcryptEmEnable.setStatus("current")
_ApexCteConfig_ObjectIdentity = ObjectIdentity
apexCteConfig = _ApexCteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2)
)


class _ApexCteEncryptionMode_Type(Integer32):
    """Custom type apexCteEncryptionMode based on Integer32"""
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
        *(("clear", 4),
          ("fpk", 3),
          ("full", 1),
          ("fwk", 2))
    )


_ApexCteEncryptionMode_Type.__name__ = "Integer32"
_ApexCteEncryptionMode_Object = MibScalar
apexCteEncryptionMode = _ApexCteEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 1),
    _ApexCteEncryptionMode_Type()
)
apexCteEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteEncryptionMode.setStatus("current")


class _ApexCteCciLevel_Type(Integer32):
    """Custom type apexCteCciLevel based on Integer32"""
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
        *(("copyFreely", 2),
          ("copyNever", 4),
          ("copyOnce", 3),
          ("noMoreCopies", 5),
          ("notDefined", 1))
    )


_ApexCteCciLevel_Type.__name__ = "Integer32"
_ApexCteCciLevel_Object = MibScalar
apexCteCciLevel = _ApexCteCciLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 2),
    _ApexCteCciLevel_Type()
)
apexCteCciLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteCciLevel.setStatus("current")


class _ApexCteApsLevel_Type(Integer32):
    """Custom type apexCteApsLevel based on Integer32"""
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
        *(("notDefined", 1),
          ("off", 2),
          ("splitBurst2Line", 4),
          ("splitBurst4Line", 5),
          ("splitBurstOff", 3))
    )


_ApexCteApsLevel_Type.__name__ = "Integer32"
_ApexCteApsLevel_Object = MibScalar
apexCteApsLevel = _ApexCteApsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 3),
    _ApexCteApsLevel_Type()
)
apexCteApsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteApsLevel.setStatus("current")
_ApexCteCitEnable_Type = EnableDisableTYPE
_ApexCteCitEnable_Object = MibScalar
apexCteCitEnable = _ApexCteCitEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 4),
    _ApexCteCitEnable_Type()
)
apexCteCitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteCitEnable.setStatus("current")


class _ApexCteCommonTier_Type(Integer32):
    """Custom type apexCteCommonTier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ApexCteCommonTier_Type.__name__ = "Integer32"
_ApexCteCommonTier_Object = MibScalar
apexCteCommonTier = _ApexCteCommonTier_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 5),
    _ApexCteCommonTier_Type()
)
apexCteCommonTier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteCommonTier.setStatus("current")
_ApexCteApplyChange_Type = ApplyDataToDeviceTYPE
_ApexCteApplyChange_Object = MibScalar
apexCteApplyChange = _ApexCteApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 1, 2, 6),
    _ApexCteApplyChange_Type()
)
apexCteApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexCteApplyChange.setStatus("current")
_ApexEncryptionStatus_ObjectIdentity = ObjectIdentity
apexEncryptionStatus = _ApexEncryptionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2)
)
_ApexEncryptionStatusGeneral_ObjectIdentity = ObjectIdentity
apexEncryptionStatusGeneral = _ApexEncryptionStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1)
)


class _ApexEncryptionStatAlgorithm_Type(Integer32):
    """Custom type apexEncryptionStatAlgorithm based on Integer32"""
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
        *(("des-dcii", 1),
          ("des-scte-52", 2),
          ("dvb-csa", 3),
          ("dvb-csa-simulcrypt", 4))
    )


_ApexEncryptionStatAlgorithm_Type.__name__ = "Integer32"
_ApexEncryptionStatAlgorithm_Object = MibScalar
apexEncryptionStatAlgorithm = _ApexEncryptionStatAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 1),
    _ApexEncryptionStatAlgorithm_Type()
)
apexEncryptionStatAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionStatAlgorithm.setStatus("current")
_ApexEncryptionCwgStatus_ObjectIdentity = ObjectIdentity
apexEncryptionCwgStatus = _ApexEncryptionCwgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2)
)
_ApexEncryptionCwgPerSecond_Type = Integer32
_ApexEncryptionCwgPerSecond_Object = MibScalar
apexEncryptionCwgPerSecond = _ApexEncryptionCwgPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 1),
    _ApexEncryptionCwgPerSecond_Type()
)
apexEncryptionCwgPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionCwgPerSecond.setStatus("current")
_ApexEncryptionMux1CollisionCount_Type = Integer32
_ApexEncryptionMux1CollisionCount_Object = MibScalar
apexEncryptionMux1CollisionCount = _ApexEncryptionMux1CollisionCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 2),
    _ApexEncryptionMux1CollisionCount_Type()
)
apexEncryptionMux1CollisionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionMux1CollisionCount.setStatus("current")
_ApexEncryptionMux2CollisionCount_Type = Integer32
_ApexEncryptionMux2CollisionCount_Object = MibScalar
apexEncryptionMux2CollisionCount = _ApexEncryptionMux2CollisionCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 3),
    _ApexEncryptionMux2CollisionCount_Type()
)
apexEncryptionMux2CollisionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionMux2CollisionCount.setStatus("current")
_ApexEncryptionMux1RolloverCount_Type = Integer32
_ApexEncryptionMux1RolloverCount_Object = MibScalar
apexEncryptionMux1RolloverCount = _ApexEncryptionMux1RolloverCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 4),
    _ApexEncryptionMux1RolloverCount_Type()
)
apexEncryptionMux1RolloverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionMux1RolloverCount.setStatus("current")
_ApexEncryptionMux2RolloverCount_Type = Integer32
_ApexEncryptionMux2RolloverCount_Object = MibScalar
apexEncryptionMux2RolloverCount = _ApexEncryptionMux2RolloverCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 5),
    _ApexEncryptionMux2RolloverCount_Type()
)
apexEncryptionMux2RolloverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionMux2RolloverCount.setStatus("current")
_ApexEncryptionEmmRequestsSent_Type = Integer32
_ApexEncryptionEmmRequestsSent_Object = MibScalar
apexEncryptionEmmRequestsSent = _ApexEncryptionEmmRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 6),
    _ApexEncryptionEmmRequestsSent_Type()
)
apexEncryptionEmmRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmRequestsSent.setStatus("current")
_ApexEncryptionEmmGoodRepliesRecvd_Type = Integer32
_ApexEncryptionEmmGoodRepliesRecvd_Object = MibScalar
apexEncryptionEmmGoodRepliesRecvd = _ApexEncryptionEmmGoodRepliesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 7),
    _ApexEncryptionEmmGoodRepliesRecvd_Type()
)
apexEncryptionEmmGoodRepliesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmGoodRepliesRecvd.setStatus("current")
_ApexEncryptionEmmBadRepliesRecvd_Type = Integer32
_ApexEncryptionEmmBadRepliesRecvd_Object = MibScalar
apexEncryptionEmmBadRepliesRecvd = _ApexEncryptionEmmBadRepliesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 8),
    _ApexEncryptionEmmBadRepliesRecvd_Type()
)
apexEncryptionEmmBadRepliesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmBadRepliesRecvd.setStatus("current")
_ApexEncryptionEmmGoodDeliveryTimeMs_Type = Integer32
_ApexEncryptionEmmGoodDeliveryTimeMs_Object = MibScalar
apexEncryptionEmmGoodDeliveryTimeMs = _ApexEncryptionEmmGoodDeliveryTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 9),
    _ApexEncryptionEmmGoodDeliveryTimeMs_Type()
)
apexEncryptionEmmGoodDeliveryTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmGoodDeliveryTimeMs.setStatus("current")
_ApexEncryptionEmmMaxDeliveryTimeMs_Type = Integer32
_ApexEncryptionEmmMaxDeliveryTimeMs_Object = MibScalar
apexEncryptionEmmMaxDeliveryTimeMs = _ApexEncryptionEmmMaxDeliveryTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 10),
    _ApexEncryptionEmmMaxDeliveryTimeMs_Type()
)
apexEncryptionEmmMaxDeliveryTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmMaxDeliveryTimeMs.setStatus("current")
_ApexEncryptionEmmMinDeliveryTimeMs_Type = Integer32
_ApexEncryptionEmmMinDeliveryTimeMs_Object = MibScalar
apexEncryptionEmmMinDeliveryTimeMs = _ApexEncryptionEmmMinDeliveryTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 11),
    _ApexEncryptionEmmMinDeliveryTimeMs_Type()
)
apexEncryptionEmmMinDeliveryTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionEmmMinDeliveryTimeMs.setStatus("current")
_ApexEncryptionMcDiagTable_Object = MibTable
apexEncryptionMcDiagTable = _ApexEncryptionMcDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    apexEncryptionMcDiagTable.setStatus("current")
_ApexEncryptionMcDiagEntry_Object = MibTableRow
apexEncryptionMcDiagEntry = _ApexEncryptionMcDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 12, 1)
)
apexEncryptionMcDiagEntry.setIndexNames(
    (0, "APEX-MIB", "apexEncryptionMcDiagDeviceIndex"),
)
if mibBuilder.loadTexts:
    apexEncryptionMcDiagEntry.setStatus("current")


class _ApexEncryptionMcDiagDeviceIndex_Type(Integer32):
    """Custom type apexEncryptionMcDiagDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApexEncryptionMcDiagDeviceIndex_Type.__name__ = "Integer32"
_ApexEncryptionMcDiagDeviceIndex_Object = MibTableColumn
apexEncryptionMcDiagDeviceIndex = _ApexEncryptionMcDiagDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 12, 1, 1),
    _ApexEncryptionMcDiagDeviceIndex_Type()
)
apexEncryptionMcDiagDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexEncryptionMcDiagDeviceIndex.setStatus("current")
_ApexEncryptionCwCountsPerSecond_Type = Unsigned32
_ApexEncryptionCwCountsPerSecond_Object = MibTableColumn
apexEncryptionCwCountsPerSecond = _ApexEncryptionCwCountsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 20, 2, 1, 2, 12, 1, 2),
    _ApexEncryptionCwCountsPerSecond_Type()
)
apexEncryptionCwCountsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEncryptionCwCountsPerSecond.setStatus("current")
_ApexEas_ObjectIdentity = ObjectIdentity
apexEas = _ApexEas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21)
)
_ApexEasConfig_ObjectIdentity = ObjectIdentity
apexEasConfig = _ApexEasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1)
)
_ApexEasConfigGeneral_ObjectIdentity = ObjectIdentity
apexEasConfigGeneral = _ApexEasConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1)
)
_ApexEasApplyChange_Type = ApplyDataToDeviceTYPE
_ApexEasApplyChange_Object = MibScalar
apexEasApplyChange = _ApexEasApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 1),
    _ApexEasApplyChange_Type()
)
apexEasApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasApplyChange.setStatus("obsolete")


class _ApexEasPhysInType_Type(Integer32):
    """Custom type apexEasPhysInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1),
          ("notApplicable", 0))
    )


_ApexEasPhysInType_Type.__name__ = "Integer32"
_ApexEasPhysInType_Object = MibScalar
apexEasPhysInType = _ApexEasPhysInType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 2),
    _ApexEasPhysInType_Type()
)
apexEasPhysInType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasPhysInType.setStatus("obsolete")
_ApexEasPhysInPort_Type = Integer32
_ApexEasPhysInPort_Object = MibScalar
apexEasPhysInPort = _ApexEasPhysInPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 3),
    _ApexEasPhysInPort_Type()
)
apexEasPhysInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasPhysInPort.setStatus("obsolete")


class _ApexEasRcvUdpPort_Type(Integer32):
    """Custom type apexEasRcvUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexEasRcvUdpPort_Type.__name__ = "Integer32"
_ApexEasRcvUdpPort_Object = MibScalar
apexEasRcvUdpPort = _ApexEasRcvUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 4),
    _ApexEasRcvUdpPort_Type()
)
apexEasRcvUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasRcvUdpPort.setStatus("obsolete")
_ApexEasMulticastIpAddress_Type = IpAddress
_ApexEasMulticastIpAddress_Object = MibScalar
apexEasMulticastIpAddress = _ApexEasMulticastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 5),
    _ApexEasMulticastIpAddress_Type()
)
apexEasMulticastIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasMulticastIpAddress.setStatus("obsolete")
_ApexEasSourceIpAddress_Type = IpAddress
_ApexEasSourceIpAddress_Object = MibScalar
apexEasSourceIpAddress = _ApexEasSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 1, 6),
    _ApexEasSourceIpAddress_Type()
)
apexEasSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasSourceIpAddress.setStatus("obsolete")
_ApexEasOutputTable_Object = MibTable
apexEasOutputTable = _ApexEasOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 2)
)
if mibBuilder.loadTexts:
    apexEasOutputTable.setStatus("current")
_ApexEasOutputEntry_Object = MibTableRow
apexEasOutputEntry = _ApexEasOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 2, 1)
)
apexEasOutputEntry.setIndexNames(
    (0, "APEX-MIB", "apexEasOutputStreamNum"),
)
if mibBuilder.loadTexts:
    apexEasOutputEntry.setStatus("current")


class _ApexEasOutputStreamNum_Type(Integer32):
    """Custom type apexEasOutputStreamNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexEasOutputStreamNum_Type.__name__ = "Integer32"
_ApexEasOutputStreamNum_Object = MibTableColumn
apexEasOutputStreamNum = _ApexEasOutputStreamNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 2, 1, 1),
    _ApexEasOutputStreamNum_Type()
)
apexEasOutputStreamNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexEasOutputStreamNum.setStatus("current")
_ApexEasOutputEnable_Type = EnableDisableTYPE
_ApexEasOutputEnable_Object = MibTableColumn
apexEasOutputEnable = _ApexEasOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 2, 1, 2),
    _ApexEasOutputEnable_Type()
)
apexEasOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasOutputEnable.setStatus("current")
_ApexEasServerApplyTable_Object = MibTable
apexEasServerApplyTable = _ApexEasServerApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 3)
)
if mibBuilder.loadTexts:
    apexEasServerApplyTable.setStatus("current")
_ApexEasServerApplyEntry_Object = MibTableRow
apexEasServerApplyEntry = _ApexEasServerApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 3, 1)
)
apexEasServerApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexEasServerApplyNum"),
)
if mibBuilder.loadTexts:
    apexEasServerApplyEntry.setStatus("current")


class _ApexEasServerApplyNum_Type(Integer32):
    """Custom type apexEasServerApplyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexEasServerApplyNum_Type.__name__ = "Integer32"
_ApexEasServerApplyNum_Object = MibTableColumn
apexEasServerApplyNum = _ApexEasServerApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 3, 1, 1),
    _ApexEasServerApplyNum_Type()
)
apexEasServerApplyNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexEasServerApplyNum.setStatus("current")
_ApexEasServerApplyChange_Type = ApplyDataToDeviceTYPE
_ApexEasServerApplyChange_Object = MibTableColumn
apexEasServerApplyChange = _ApexEasServerApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 3, 1, 2),
    _ApexEasServerApplyChange_Type()
)
apexEasServerApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerApplyChange.setStatus("current")
_ApexEasServerTable_Object = MibTable
apexEasServerTable = _ApexEasServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4)
)
if mibBuilder.loadTexts:
    apexEasServerTable.setStatus("current")
_ApexEasServerEntry_Object = MibTableRow
apexEasServerEntry = _ApexEasServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1)
)
apexEasServerEntry.setIndexNames(
    (0, "APEX-MIB", "apexEasServerNum"),
)
if mibBuilder.loadTexts:
    apexEasServerEntry.setStatus("current")


class _ApexEasServerNum_Type(Integer32):
    """Custom type apexEasServerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexEasServerNum_Type.__name__ = "Integer32"
_ApexEasServerNum_Object = MibTableColumn
apexEasServerNum = _ApexEasServerNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 1),
    _ApexEasServerNum_Type()
)
apexEasServerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexEasServerNum.setStatus("current")


class _ApexEasServerPhysInType_Type(Integer32):
    """Custom type apexEasServerPhysInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1),
          ("notApplicable", 0))
    )


_ApexEasServerPhysInType_Type.__name__ = "Integer32"
_ApexEasServerPhysInType_Object = MibTableColumn
apexEasServerPhysInType = _ApexEasServerPhysInType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 2),
    _ApexEasServerPhysInType_Type()
)
apexEasServerPhysInType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerPhysInType.setStatus("current")
_ApexEasServerPhysInPort_Type = Integer32
_ApexEasServerPhysInPort_Object = MibTableColumn
apexEasServerPhysInPort = _ApexEasServerPhysInPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 3),
    _ApexEasServerPhysInPort_Type()
)
apexEasServerPhysInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerPhysInPort.setStatus("current")


class _ApexEasServerRcvUdpPort_Type(Integer32):
    """Custom type apexEasServerRcvUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexEasServerRcvUdpPort_Type.__name__ = "Integer32"
_ApexEasServerRcvUdpPort_Object = MibTableColumn
apexEasServerRcvUdpPort = _ApexEasServerRcvUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 4),
    _ApexEasServerRcvUdpPort_Type()
)
apexEasServerRcvUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerRcvUdpPort.setStatus("current")
_ApexEasServerMulticastIpAddress_Type = IpAddress
_ApexEasServerMulticastIpAddress_Object = MibTableColumn
apexEasServerMulticastIpAddress = _ApexEasServerMulticastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 5),
    _ApexEasServerMulticastIpAddress_Type()
)
apexEasServerMulticastIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerMulticastIpAddress.setStatus("current")
_ApexEasServerSourceIpAddress_Type = IpAddress
_ApexEasServerSourceIpAddress_Object = MibTableColumn
apexEasServerSourceIpAddress = _ApexEasServerSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 1, 4, 1, 6),
    _ApexEasServerSourceIpAddress_Type()
)
apexEasServerSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEasServerSourceIpAddress.setStatus("current")
_ApexEasStatus_ObjectIdentity = ObjectIdentity
apexEasStatus = _ApexEasStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 2)
)
_ApexEasStatusGeneral_ObjectIdentity = ObjectIdentity
apexEasStatusGeneral = _ApexEasStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 2, 1)
)
_ApexEasNumRcvMsgs_Type = Unsigned32
_ApexEasNumRcvMsgs_Object = MibScalar
apexEasNumRcvMsgs = _ApexEasNumRcvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 2, 1, 1),
    _ApexEasNumRcvMsgs_Type()
)
apexEasNumRcvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEasNumRcvMsgs.setStatus("current")
_ApexEasNumInvalRcvMsgs_Type = Unsigned32
_ApexEasNumInvalRcvMsgs_Object = MibScalar
apexEasNumInvalRcvMsgs = _ApexEasNumInvalRcvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 21, 2, 1, 2),
    _ApexEasNumInvalRcvMsgs_Type()
)
apexEasNumInvalRcvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEasNumInvalRcvMsgs.setStatus("current")
_ApexChassisRedundancy_ObjectIdentity = ObjectIdentity
apexChassisRedundancy = _ApexChassisRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22)
)
_ApexChassisRedundancyConfig_ObjectIdentity = ObjectIdentity
apexChassisRedundancyConfig = _ApexChassisRedundancyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1)
)
_ApexChassisRedundancyConfigGeneral_ObjectIdentity = ObjectIdentity
apexChassisRedundancyConfigGeneral = _ApexChassisRedundancyConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1)
)
_ApexChassisRedundancyConfigEnable_Type = EnableDisableTYPE
_ApexChassisRedundancyConfigEnable_Object = MibScalar
apexChassisRedundancyConfigEnable = _ApexChassisRedundancyConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 1),
    _ApexChassisRedundancyConfigEnable_Type()
)
apexChassisRedundancyConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyConfigEnable.setStatus("current")


class _ApexChassisRedundancyMode_Type(Integer32):
    """Custom type apexChassisRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ApexChassisRedundancyMode_Type.__name__ = "Integer32"
_ApexChassisRedundancyMode_Object = MibScalar
apexChassisRedundancyMode = _ApexChassisRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 2),
    _ApexChassisRedundancyMode_Type()
)
apexChassisRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyMode.setStatus("current")


class _ApexChassisRedundancyMulticastRedundancyMode_Type(Integer32):
    """Custom type apexChassisRedundancyMulticastRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hot", 1),
          ("warm", 2))
    )


_ApexChassisRedundancyMulticastRedundancyMode_Type.__name__ = "Integer32"
_ApexChassisRedundancyMulticastRedundancyMode_Object = MibScalar
apexChassisRedundancyMulticastRedundancyMode = _ApexChassisRedundancyMulticastRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 3),
    _ApexChassisRedundancyMulticastRedundancyMode_Type()
)
apexChassisRedundancyMulticastRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyMulticastRedundancyMode.setStatus("current")


class _ApexChassisRedundancyUdpPort_Type(Integer32):
    """Custom type apexChassisRedundancyUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApexChassisRedundancyUdpPort_Type.__name__ = "Integer32"
_ApexChassisRedundancyUdpPort_Object = MibScalar
apexChassisRedundancyUdpPort = _ApexChassisRedundancyUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 4),
    _ApexChassisRedundancyUdpPort_Type()
)
apexChassisRedundancyUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyUdpPort.setStatus("current")
_ApexChassisRedundancyRedundantApexIp_Type = IpAddress
_ApexChassisRedundancyRedundantApexIp_Object = MibScalar
apexChassisRedundancyRedundantApexIp = _ApexChassisRedundancyRedundantApexIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 5),
    _ApexChassisRedundancyRedundantApexIp_Type()
)
apexChassisRedundancyRedundantApexIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyRedundantApexIp.setStatus("current")
_ApexChassisRedundancySuspend_Type = EnableDisableTYPE
_ApexChassisRedundancySuspend_Object = MibScalar
apexChassisRedundancySuspend = _ApexChassisRedundancySuspend_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 6),
    _ApexChassisRedundancySuspend_Type()
)
apexChassisRedundancySuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancySuspend.setStatus("current")


class _ApexChassisRedundancyForceFailOver_Type(Integer32):
    """Custom type apexChassisRedundancyForceFailOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 2),
          ("failoverNotInProgress", 1))
    )


_ApexChassisRedundancyForceFailOver_Type.__name__ = "Integer32"
_ApexChassisRedundancyForceFailOver_Object = MibScalar
apexChassisRedundancyForceFailOver = _ApexChassisRedundancyForceFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 7),
    _ApexChassisRedundancyForceFailOver_Type()
)
apexChassisRedundancyForceFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyForceFailOver.setStatus("current")
_ApexChassisRedundancyFailOverGigE12LinkLoss_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverGigE12LinkLoss_Object = MibScalar
apexChassisRedundancyFailOverGigE12LinkLoss = _ApexChassisRedundancyFailOverGigE12LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 8),
    _ApexChassisRedundancyFailOverGigE12LinkLoss_Type()
)
apexChassisRedundancyFailOverGigE12LinkLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverGigE12LinkLoss.setStatus("current")
_ApexChassisRedundancyFailOverGigE34LinkLoss_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverGigE34LinkLoss_Object = MibScalar
apexChassisRedundancyFailOverGigE34LinkLoss = _ApexChassisRedundancyFailOverGigE34LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 9),
    _ApexChassisRedundancyFailOverGigE34LinkLoss_Type()
)
apexChassisRedundancyFailOverGigE34LinkLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverGigE34LinkLoss.setStatus("current")
_ApexChassisRedundancyFailOverEnet1LinkLoss_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverEnet1LinkLoss_Object = MibScalar
apexChassisRedundancyFailOverEnet1LinkLoss = _ApexChassisRedundancyFailOverEnet1LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 10),
    _ApexChassisRedundancyFailOverEnet1LinkLoss_Type()
)
apexChassisRedundancyFailOverEnet1LinkLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverEnet1LinkLoss.setStatus("current")
_ApexChassisRedundancyFailOverEnet2LinkLoss_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverEnet2LinkLoss_Object = MibScalar
apexChassisRedundancyFailOverEnet2LinkLoss = _ApexChassisRedundancyFailOverEnet2LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 11),
    _ApexChassisRedundancyFailOverEnet2LinkLoss_Type()
)
apexChassisRedundancyFailOverEnet2LinkLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverEnet2LinkLoss.setStatus("current")
_ApexChassisRedundancyFailOverTemperatureFault_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverTemperatureFault_Object = MibScalar
apexChassisRedundancyFailOverTemperatureFault = _ApexChassisRedundancyFailOverTemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 12),
    _ApexChassisRedundancyFailOverTemperatureFault_Type()
)
apexChassisRedundancyFailOverTemperatureFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverTemperatureFault.setStatus("current")
_ApexChassisRedundancyFailOverQamModuleFault_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverQamModuleFault_Object = MibScalar
apexChassisRedundancyFailOverQamModuleFault = _ApexChassisRedundancyFailOverQamModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 13),
    _ApexChassisRedundancyFailOverQamModuleFault_Type()
)
apexChassisRedundancyFailOverQamModuleFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverQamModuleFault.setStatus("current")
_ApexChassisRedundancyFailOverQamRfPortFault_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverQamRfPortFault_Object = MibScalar
apexChassisRedundancyFailOverQamRfPortFault = _ApexChassisRedundancyFailOverQamRfPortFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 14),
    _ApexChassisRedundancyFailOverQamRfPortFault_Type()
)
apexChassisRedundancyFailOverQamRfPortFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverQamRfPortFault.setStatus("current")
_ApexChassisRedundancyFailOverQamChannelFault_Type = EnableDisableTYPE
_ApexChassisRedundancyFailOverQamChannelFault_Object = MibScalar
apexChassisRedundancyFailOverQamChannelFault = _ApexChassisRedundancyFailOverQamChannelFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 15),
    _ApexChassisRedundancyFailOverQamChannelFault_Type()
)
apexChassisRedundancyFailOverQamChannelFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyFailOverQamChannelFault.setStatus("current")
_ApexChassisRedundancyConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexChassisRedundancyConfigApplyChange_Object = MibScalar
apexChassisRedundancyConfigApplyChange = _ApexChassisRedundancyConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 16),
    _ApexChassisRedundancyConfigApplyChange_Type()
)
apexChassisRedundancyConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyConfigApplyChange.setStatus("current")
_ApexChassisRedundancyPrimaryStandbyOverride_Type = EnableDisableTYPE
_ApexChassisRedundancyPrimaryStandbyOverride_Object = MibScalar
apexChassisRedundancyPrimaryStandbyOverride = _ApexChassisRedundancyPrimaryStandbyOverride_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 17),
    _ApexChassisRedundancyPrimaryStandbyOverride_Type()
)
apexChassisRedundancyPrimaryStandbyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyPrimaryStandbyOverride.setStatus("current")
_ApexChassisRedundancyRedundantApexSecIp_Type = IpAddress
_ApexChassisRedundancyRedundantApexSecIp_Object = MibScalar
apexChassisRedundancyRedundantApexSecIp = _ApexChassisRedundancyRedundantApexSecIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 18),
    _ApexChassisRedundancyRedundantApexSecIp_Type()
)
apexChassisRedundancyRedundantApexSecIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyRedundantApexSecIp.setStatus("current")
_ApexChassisRedundancyRedundantHBEnable_Type = EnableDisableTYPE
_ApexChassisRedundancyRedundantHBEnable_Object = MibScalar
apexChassisRedundancyRedundantHBEnable = _ApexChassisRedundancyRedundantHBEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 1, 1, 19),
    _ApexChassisRedundancyRedundantHBEnable_Type()
)
apexChassisRedundancyRedundantHBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexChassisRedundancyRedundantHBEnable.setStatus("current")
_ApexChassisRedundancyStatus_ObjectIdentity = ObjectIdentity
apexChassisRedundancyStatus = _ApexChassisRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2)
)
_ApexChassisRedundancyStatusGeneral_ObjectIdentity = ObjectIdentity
apexChassisRedundancyStatusGeneral = _ApexChassisRedundancyStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1)
)


class _ApexChassisRedundancyPrimaryApexStatus_Type(Integer32):
    """Custom type apexChassisRedundancyPrimaryApexStatus based on Integer32"""
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
        *(("active", 1),
          ("fault", 3),
          ("standby", 2),
          ("suspend", 4),
          ("unknown", 0))
    )


_ApexChassisRedundancyPrimaryApexStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyPrimaryApexStatus_Object = MibScalar
apexChassisRedundancyPrimaryApexStatus = _ApexChassisRedundancyPrimaryApexStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 1),
    _ApexChassisRedundancyPrimaryApexStatus_Type()
)
apexChassisRedundancyPrimaryApexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyPrimaryApexStatus.setStatus("current")


class _ApexChassisRedundancySecondaryApexStatus_Type(Integer32):
    """Custom type apexChassisRedundancySecondaryApexStatus based on Integer32"""
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
        *(("active", 1),
          ("fault", 3),
          ("standby", 2),
          ("suspend", 4),
          ("unknown", 0))
    )


_ApexChassisRedundancySecondaryApexStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancySecondaryApexStatus_Object = MibScalar
apexChassisRedundancySecondaryApexStatus = _ApexChassisRedundancySecondaryApexStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 2),
    _ApexChassisRedundancySecondaryApexStatus_Type()
)
apexChassisRedundancySecondaryApexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancySecondaryApexStatus.setStatus("current")


class _ApexChassisRedundancyState_Type(Integer32):
    """Custom type apexChassisRedundancyState based on Integer32"""
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
        *(("available", 1),
          ("protected", 2),
          ("synchronizing", 4),
          ("unavailable", 3),
          ("unknown", 0))
    )


_ApexChassisRedundancyState_Type.__name__ = "Integer32"
_ApexChassisRedundancyState_Object = MibScalar
apexChassisRedundancyState = _ApexChassisRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 3),
    _ApexChassisRedundancyState_Type()
)
apexChassisRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyState.setStatus("current")


class _ApexChassisRedundancyCommunicationStatus_Type(Integer32):
    """Custom type apexChassisRedundancyCommunicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 0))
    )


_ApexChassisRedundancyCommunicationStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyCommunicationStatus_Object = MibScalar
apexChassisRedundancyCommunicationStatus = _ApexChassisRedundancyCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 4),
    _ApexChassisRedundancyCommunicationStatus_Type()
)
apexChassisRedundancyCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyCommunicationStatus.setStatus("current")


class _ApexChassisRedundancyConfigurationStatus_Type(Integer32):
    """Custom type apexChassisRedundancyConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outofsync", 2),
          ("synchronized", 1),
          ("unknown", 0))
    )


_ApexChassisRedundancyConfigurationStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyConfigurationStatus_Object = MibScalar
apexChassisRedundancyConfigurationStatus = _ApexChassisRedundancyConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 5),
    _ApexChassisRedundancyConfigurationStatus_Type()
)
apexChassisRedundancyConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyConfigurationStatus.setStatus("current")


class _ApexChassisRedundancyStatusInvalidApplyText_Type(DisplayString):
    """Custom type apexChassisRedundancyStatusInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexChassisRedundancyStatusInvalidApplyText_Type.__name__ = "DisplayString"
_ApexChassisRedundancyStatusInvalidApplyText_Object = MibScalar
apexChassisRedundancyStatusInvalidApplyText = _ApexChassisRedundancyStatusInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 6),
    _ApexChassisRedundancyStatusInvalidApplyText_Type()
)
apexChassisRedundancyStatusInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyStatusInvalidApplyText.setStatus("current")


class _ApexChassisRedundancyGeneralConfigSyncStatusText_Type(DisplayString):
    """Custom type apexChassisRedundancyGeneralConfigSyncStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexChassisRedundancyGeneralConfigSyncStatusText_Type.__name__ = "DisplayString"
_ApexChassisRedundancyGeneralConfigSyncStatusText_Object = MibScalar
apexChassisRedundancyGeneralConfigSyncStatusText = _ApexChassisRedundancyGeneralConfigSyncStatusText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 7),
    _ApexChassisRedundancyGeneralConfigSyncStatusText_Type()
)
apexChassisRedundancyGeneralConfigSyncStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyGeneralConfigSyncStatusText.setStatus("current")


class _ApexChassisRedundancyGigEMismatchStatus_Type(Integer32):
    """Custom type apexChassisRedundancyGigEMismatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("mismatch", 2),
          ("unknown", 0))
    )


_ApexChassisRedundancyGigEMismatchStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyGigEMismatchStatus_Object = MibScalar
apexChassisRedundancyGigEMismatchStatus = _ApexChassisRedundancyGigEMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 8),
    _ApexChassisRedundancyGigEMismatchStatus_Type()
)
apexChassisRedundancyGigEMismatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyGigEMismatchStatus.setStatus("current")


class _ApexChassisRedundancyQamMismatchStatus_Type(Integer32):
    """Custom type apexChassisRedundancyQamMismatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("mismatch", 2),
          ("unknown", 0))
    )


_ApexChassisRedundancyQamMismatchStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyQamMismatchStatus_Object = MibScalar
apexChassisRedundancyQamMismatchStatus = _ApexChassisRedundancyQamMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 9),
    _ApexChassisRedundancyQamMismatchStatus_Type()
)
apexChassisRedundancyQamMismatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyQamMismatchStatus.setStatus("current")


class _ApexChassisRedundancyFirmwareMismatchStatus_Type(Integer32):
    """Custom type apexChassisRedundancyFirmwareMismatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("mismatch", 2),
          ("unknown", 0))
    )


_ApexChassisRedundancyFirmwareMismatchStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyFirmwareMismatchStatus_Object = MibScalar
apexChassisRedundancyFirmwareMismatchStatus = _ApexChassisRedundancyFirmwareMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 10),
    _ApexChassisRedundancyFirmwareMismatchStatus_Type()
)
apexChassisRedundancyFirmwareMismatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyFirmwareMismatchStatus.setStatus("current")


class _ApexChassisRedundancyGigE12LinkStatus_Type(Integer32):
    """Custom type apexChassisRedundancyGigE12LinkStatus based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexChassisRedundancyGigE12LinkStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyGigE12LinkStatus_Object = MibScalar
apexChassisRedundancyGigE12LinkStatus = _ApexChassisRedundancyGigE12LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 11),
    _ApexChassisRedundancyGigE12LinkStatus_Type()
)
apexChassisRedundancyGigE12LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyGigE12LinkStatus.setStatus("current")


class _ApexChassisRedundancyGigE34LinkStatus_Type(Integer32):
    """Custom type apexChassisRedundancyGigE34LinkStatus based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexChassisRedundancyGigE34LinkStatus_Type.__name__ = "Integer32"
_ApexChassisRedundancyGigE34LinkStatus_Object = MibScalar
apexChassisRedundancyGigE34LinkStatus = _ApexChassisRedundancyGigE34LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 12),
    _ApexChassisRedundancyGigE34LinkStatus_Type()
)
apexChassisRedundancyGigE34LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyGigE34LinkStatus.setStatus("current")
_ApexChassisRedundancyCurrHBIntfIPStatus_Type = IpAddress
_ApexChassisRedundancyCurrHBIntfIPStatus_Object = MibScalar
apexChassisRedundancyCurrHBIntfIPStatus = _ApexChassisRedundancyCurrHBIntfIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 22, 2, 1, 13),
    _ApexChassisRedundancyCurrHBIntfIPStatus_Type()
)
apexChassisRedundancyCurrHBIntfIPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyCurrHBIntfIPStatus.setStatus("current")
_ApexDta_ObjectIdentity = ObjectIdentity
apexDta = _ApexDta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23)
)
_ApexDtaConfig_ObjectIdentity = ObjectIdentity
apexDtaConfig = _ApexDtaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1)
)
_ApexDtaGeneralConfig_ObjectIdentity = ObjectIdentity
apexDtaGeneralConfig = _ApexDtaGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1)
)


class _ApexDtaGeneralConfigCatSourceType_Type(Integer32):
    """Custom type apexDtaGeneralConfigCatSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ApexDtaGeneralConfigCatSourceType_Type.__name__ = "Integer32"
_ApexDtaGeneralConfigCatSourceType_Object = MibScalar
apexDtaGeneralConfigCatSourceType = _ApexDtaGeneralConfigCatSourceType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 1),
    _ApexDtaGeneralConfigCatSourceType_Type()
)
apexDtaGeneralConfigCatSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigCatSourceType.setStatus("current")
_ApexDtaGeneralConfigCatEmmPidMulticastIP_Type = IpAddress
_ApexDtaGeneralConfigCatEmmPidMulticastIP_Object = MibScalar
apexDtaGeneralConfigCatEmmPidMulticastIP = _ApexDtaGeneralConfigCatEmmPidMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 2),
    _ApexDtaGeneralConfigCatEmmPidMulticastIP_Type()
)
apexDtaGeneralConfigCatEmmPidMulticastIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigCatEmmPidMulticastIP.setStatus("current")
_ApexDtaGeneralConfigCatEmmPidSourceIP_Type = IpAddress
_ApexDtaGeneralConfigCatEmmPidSourceIP_Object = MibScalar
apexDtaGeneralConfigCatEmmPidSourceIP = _ApexDtaGeneralConfigCatEmmPidSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 3),
    _ApexDtaGeneralConfigCatEmmPidSourceIP_Type()
)
apexDtaGeneralConfigCatEmmPidSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigCatEmmPidSourceIP.setStatus("current")


class _ApexDtaGeneralConfigCatEmmPidUdpPort_Type(Integer32):
    """Custom type apexDtaGeneralConfigCatEmmPidUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApexDtaGeneralConfigCatEmmPidUdpPort_Type.__name__ = "Integer32"
_ApexDtaGeneralConfigCatEmmPidUdpPort_Object = MibScalar
apexDtaGeneralConfigCatEmmPidUdpPort = _ApexDtaGeneralConfigCatEmmPidUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 4),
    _ApexDtaGeneralConfigCatEmmPidUdpPort_Type()
)
apexDtaGeneralConfigCatEmmPidUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigCatEmmPidUdpPort.setStatus("current")
_ApexDtaGeneralConfigCatEmmPidInterface_Type = EthernetInterfaceTYPE
_ApexDtaGeneralConfigCatEmmPidInterface_Object = MibScalar
apexDtaGeneralConfigCatEmmPidInterface = _ApexDtaGeneralConfigCatEmmPidInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 5),
    _ApexDtaGeneralConfigCatEmmPidInterface_Type()
)
apexDtaGeneralConfigCatEmmPidInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigCatEmmPidInterface.setStatus("current")


class _ApexDtaGeneralConfigEmmPidNum_Type(Integer32):
    """Custom type apexDtaGeneralConfigEmmPidNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7168, 8190),
    )


_ApexDtaGeneralConfigEmmPidNum_Type.__name__ = "Integer32"
_ApexDtaGeneralConfigEmmPidNum_Object = MibScalar
apexDtaGeneralConfigEmmPidNum = _ApexDtaGeneralConfigEmmPidNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 6),
    _ApexDtaGeneralConfigEmmPidNum_Type()
)
apexDtaGeneralConfigEmmPidNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigEmmPidNum.setStatus("current")
_ApexDtaGeneralConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexDtaGeneralConfigApplyChange_Object = MibScalar
apexDtaGeneralConfigApplyChange = _ApexDtaGeneralConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 7),
    _ApexDtaGeneralConfigApplyChange_Type()
)
apexDtaGeneralConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigApplyChange.setStatus("current")
_ApexDtaGeneralConfigInvalidApplyText_Type = DisplayString
_ApexDtaGeneralConfigInvalidApplyText_Object = MibScalar
apexDtaGeneralConfigInvalidApplyText = _ApexDtaGeneralConfigInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 1, 8),
    _ApexDtaGeneralConfigInvalidApplyText_Type()
)
apexDtaGeneralConfigInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDtaGeneralConfigInvalidApplyText.setStatus("current")
_ApexDtaConfigApplyTable_Object = MibTable
apexDtaConfigApplyTable = _ApexDtaConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 2)
)
if mibBuilder.loadTexts:
    apexDtaConfigApplyTable.setStatus("current")
_ApexDtaConfigApplyEntry_Object = MibTableRow
apexDtaConfigApplyEntry = _ApexDtaConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 2, 1)
)
apexDtaConfigApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexDtaConfigApplyIndex"),
)
if mibBuilder.loadTexts:
    apexDtaConfigApplyEntry.setStatus("current")


class _ApexDtaConfigApplyIndex_Type(Integer32):
    """Custom type apexDtaConfigApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexDtaConfigApplyIndex_Type.__name__ = "Integer32"
_ApexDtaConfigApplyIndex_Object = MibTableColumn
apexDtaConfigApplyIndex = _ApexDtaConfigApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 2, 1, 1),
    _ApexDtaConfigApplyIndex_Type()
)
apexDtaConfigApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDtaConfigApplyIndex.setStatus("current")
_ApexDtaConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexDtaConfigApplyChange_Object = MibTableColumn
apexDtaConfigApplyChange = _ApexDtaConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 2, 1, 2),
    _ApexDtaConfigApplyChange_Type()
)
apexDtaConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaConfigApplyChange.setStatus("current")
_ApexDtaRfPortConfigTable_Object = MibTable
apexDtaRfPortConfigTable = _ApexDtaRfPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3)
)
if mibBuilder.loadTexts:
    apexDtaRfPortConfigTable.setStatus("current")
_ApexDtaRfPortConfigEntry_Object = MibTableRow
apexDtaRfPortConfigEntry = _ApexDtaRfPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1)
)
apexDtaRfPortConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexDtaRfPortConfigIndex"),
)
if mibBuilder.loadTexts:
    apexDtaRfPortConfigEntry.setStatus("current")


class _ApexDtaRfPortConfigIndex_Type(Integer32):
    """Custom type apexDtaRfPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexDtaRfPortConfigIndex_Type.__name__ = "Integer32"
_ApexDtaRfPortConfigIndex_Object = MibTableColumn
apexDtaRfPortConfigIndex = _ApexDtaRfPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 1),
    _ApexDtaRfPortConfigIndex_Type()
)
apexDtaRfPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigIndex.setStatus("current")
_ApexDtaRfPortConfigNetPidMulticastIP_Type = IpAddress
_ApexDtaRfPortConfigNetPidMulticastIP_Object = MibTableColumn
apexDtaRfPortConfigNetPidMulticastIP = _ApexDtaRfPortConfigNetPidMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 2),
    _ApexDtaRfPortConfigNetPidMulticastIP_Type()
)
apexDtaRfPortConfigNetPidMulticastIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigNetPidMulticastIP.setStatus("current")
_ApexDtaRfPortConfigNetPidSourceIP_Type = IpAddress
_ApexDtaRfPortConfigNetPidSourceIP_Object = MibTableColumn
apexDtaRfPortConfigNetPidSourceIP = _ApexDtaRfPortConfigNetPidSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 3),
    _ApexDtaRfPortConfigNetPidSourceIP_Type()
)
apexDtaRfPortConfigNetPidSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigNetPidSourceIP.setStatus("current")


class _ApexDtaRfPortConfigNetPidUdpPort_Type(Integer32):
    """Custom type apexDtaRfPortConfigNetPidUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApexDtaRfPortConfigNetPidUdpPort_Type.__name__ = "Integer32"
_ApexDtaRfPortConfigNetPidUdpPort_Object = MibTableColumn
apexDtaRfPortConfigNetPidUdpPort = _ApexDtaRfPortConfigNetPidUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 4),
    _ApexDtaRfPortConfigNetPidUdpPort_Type()
)
apexDtaRfPortConfigNetPidUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigNetPidUdpPort.setStatus("current")
_ApexDtaRfPortConfigNetPidInterface_Type = EthernetInterfaceTYPE
_ApexDtaRfPortConfigNetPidInterface_Object = MibTableColumn
apexDtaRfPortConfigNetPidInterface = _ApexDtaRfPortConfigNetPidInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 5),
    _ApexDtaRfPortConfigNetPidInterface_Type()
)
apexDtaRfPortConfigNetPidInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigNetPidInterface.setStatus("current")


class _ApexDtaRfPortConfigNetPidNum_Type(Integer32):
    """Custom type apexDtaRfPortConfigNetPidNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7168, 8190),
    )


_ApexDtaRfPortConfigNetPidNum_Type.__name__ = "Integer32"
_ApexDtaRfPortConfigNetPidNum_Object = MibTableColumn
apexDtaRfPortConfigNetPidNum = _ApexDtaRfPortConfigNetPidNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 3, 1, 6),
    _ApexDtaRfPortConfigNetPidNum_Type()
)
apexDtaRfPortConfigNetPidNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaRfPortConfigNetPidNum.setStatus("current")
_ApexDtaOtsConfigTable_Object = MibTable
apexDtaOtsConfigTable = _ApexDtaOtsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 4)
)
if mibBuilder.loadTexts:
    apexDtaOtsConfigTable.setStatus("current")
_ApexDtaOtsConfigEntry_Object = MibTableRow
apexDtaOtsConfigEntry = _ApexDtaOtsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 4, 1)
)
apexDtaOtsConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexDtaOtsConfigIndex"),
)
if mibBuilder.loadTexts:
    apexDtaOtsConfigEntry.setStatus("current")


class _ApexDtaOtsConfigIndex_Type(Integer32):
    """Custom type apexDtaOtsConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexDtaOtsConfigIndex_Type.__name__ = "Integer32"
_ApexDtaOtsConfigIndex_Object = MibTableColumn
apexDtaOtsConfigIndex = _ApexDtaOtsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 4, 1, 1),
    _ApexDtaOtsConfigIndex_Type()
)
apexDtaOtsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDtaOtsConfigIndex.setStatus("current")
_ApexDtaOtsConfigEnable_Type = EnableDisableTYPE
_ApexDtaOtsConfigEnable_Object = MibTableColumn
apexDtaOtsConfigEnable = _ApexDtaOtsConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 23, 1, 4, 1, 2),
    _ApexDtaOtsConfigEnable_Type()
)
apexDtaOtsConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDtaOtsConfigEnable.setStatus("current")
_ApexDepi_ObjectIdentity = ObjectIdentity
apexDepi = _ApexDepi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24)
)
_ApexDepiConfig_ObjectIdentity = ObjectIdentity
apexDepiConfig = _ApexDepiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 1)
)
_ApexDepiConfigGeneral_ObjectIdentity = ObjectIdentity
apexDepiConfigGeneral = _ApexDepiConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 1, 1)
)


class _ApexDepiConfigHostname_Type(DisplayString):
    """Custom type apexDepiConfigHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApexDepiConfigHostname_Type.__name__ = "DisplayString"
_ApexDepiConfigHostname_Object = MibScalar
apexDepiConfigHostname = _ApexDepiConfigHostname_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 1, 1, 1),
    _ApexDepiConfigHostname_Type()
)
apexDepiConfigHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiConfigHostname.setStatus("current")
_ApexDepiStatus_ObjectIdentity = ObjectIdentity
apexDepiStatus = _ApexDepiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2)
)
_ApexDepiStatusGeneral_ObjectIdentity = ObjectIdentity
apexDepiStatusGeneral = _ApexDepiStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1)
)
_ApexDepiStatusGeneralDtiPort1LinkActive_Type = ActiveTYPE
_ApexDepiStatusGeneralDtiPort1LinkActive_Object = MibScalar
apexDepiStatusGeneralDtiPort1LinkActive = _ApexDepiStatusGeneralDtiPort1LinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 1),
    _ApexDepiStatusGeneralDtiPort1LinkActive_Type()
)
apexDepiStatusGeneralDtiPort1LinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiPort1LinkActive.setStatus("current")
_ApexDepiStatusGeneralDtiPort2LinkActive_Type = ActiveTYPE
_ApexDepiStatusGeneralDtiPort2LinkActive_Object = MibScalar
apexDepiStatusGeneralDtiPort2LinkActive = _ApexDepiStatusGeneralDtiPort2LinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 2),
    _ApexDepiStatusGeneralDtiPort2LinkActive_Type()
)
apexDepiStatusGeneralDtiPort2LinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiPort2LinkActive.setStatus("current")


class _ApexDepiStatusGeneralDtiClientStatusMode_Type(Integer32):
    """Custom type apexDepiStatusGeneralDtiClientStatusMode based on Integer32"""
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
        *(("bridging", 5),
          ("fast", 3),
          ("free-run", 2),
          ("holdover", 6),
          ("normal", 4),
          ("warmup", 1))
    )


_ApexDepiStatusGeneralDtiClientStatusMode_Type.__name__ = "Integer32"
_ApexDepiStatusGeneralDtiClientStatusMode_Object = MibScalar
apexDepiStatusGeneralDtiClientStatusMode = _ApexDepiStatusGeneralDtiClientStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 3),
    _ApexDepiStatusGeneralDtiClientStatusMode_Type()
)
apexDepiStatusGeneralDtiClientStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiClientStatusMode.setStatus("current")
_ApexDepiStatusGeneralDtiClientPhaseError_Type = Integer32
_ApexDepiStatusGeneralDtiClientPhaseError_Object = MibScalar
apexDepiStatusGeneralDtiClientPhaseError = _ApexDepiStatusGeneralDtiClientPhaseError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 4),
    _ApexDepiStatusGeneralDtiClientPhaseError_Type()
)
apexDepiStatusGeneralDtiClientPhaseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiClientPhaseError.setStatus("current")
_ApexDepiStatusGeneralDtiCurrentTimestamp_Type = Unsigned32
_ApexDepiStatusGeneralDtiCurrentTimestamp_Object = MibScalar
apexDepiStatusGeneralDtiCurrentTimestamp = _ApexDepiStatusGeneralDtiCurrentTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 5),
    _ApexDepiStatusGeneralDtiCurrentTimestamp_Type()
)
apexDepiStatusGeneralDtiCurrentTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiCurrentTimestamp.setStatus("current")
_ApexDepiStatusGeneralDtiPort1CableAdvanceValue_Type = Integer32
_ApexDepiStatusGeneralDtiPort1CableAdvanceValue_Object = MibScalar
apexDepiStatusGeneralDtiPort1CableAdvanceValue = _ApexDepiStatusGeneralDtiPort1CableAdvanceValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 6),
    _ApexDepiStatusGeneralDtiPort1CableAdvanceValue_Type()
)
apexDepiStatusGeneralDtiPort1CableAdvanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiPort1CableAdvanceValue.setStatus("current")
_ApexDepiStatusGeneralDtiPort2CableAdvanceValue_Type = Integer32
_ApexDepiStatusGeneralDtiPort2CableAdvanceValue_Object = MibScalar
apexDepiStatusGeneralDtiPort2CableAdvanceValue = _ApexDepiStatusGeneralDtiPort2CableAdvanceValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 2, 1, 7),
    _ApexDepiStatusGeneralDtiPort2CableAdvanceValue_Type()
)
apexDepiStatusGeneralDtiPort2CableAdvanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiStatusGeneralDtiPort2CableAdvanceValue.setStatus("current")
_ApexDepiControl_ObjectIdentity = ObjectIdentity
apexDepiControl = _ApexDepiControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3)
)
_ApexDepiControlConfig_ObjectIdentity = ObjectIdentity
apexDepiControlConfig = _ApexDepiControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1)
)
_ApexDepiControlConfigGeneral_ObjectIdentity = ObjectIdentity
apexDepiControlConfigGeneral = _ApexDepiControlConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 1)
)


class _ApexDepiControlConfigGeneralKeepaliveTimeout_Type(Integer32):
    """Custom type apexDepiControlConfigGeneralKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ApexDepiControlConfigGeneralKeepaliveTimeout_Type.__name__ = "Integer32"
_ApexDepiControlConfigGeneralKeepaliveTimeout_Object = MibScalar
apexDepiControlConfigGeneralKeepaliveTimeout = _ApexDepiControlConfigGeneralKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 1, 1),
    _ApexDepiControlConfigGeneralKeepaliveTimeout_Type()
)
apexDepiControlConfigGeneralKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigGeneralKeepaliveTimeout.setStatus("current")
_ApexDepiControlConfigApplyTable_Object = MibTable
apexDepiControlConfigApplyTable = _ApexDepiControlConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    apexDepiControlConfigApplyTable.setStatus("current")
_ApexDepiControlConfigApplyEntry_Object = MibTableRow
apexDepiControlConfigApplyEntry = _ApexDepiControlConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 2, 1)
)
apexDepiControlConfigApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiControlConfigApplyIndex"),
)
if mibBuilder.loadTexts:
    apexDepiControlConfigApplyEntry.setStatus("current")


class _ApexDepiControlConfigApplyIndex_Type(Integer32):
    """Custom type apexDepiControlConfigApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApexDepiControlConfigApplyIndex_Type.__name__ = "Integer32"
_ApexDepiControlConfigApplyIndex_Object = MibTableColumn
apexDepiControlConfigApplyIndex = _ApexDepiControlConfigApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 2, 1, 1),
    _ApexDepiControlConfigApplyIndex_Type()
)
apexDepiControlConfigApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiControlConfigApplyIndex.setStatus("current")
_ApexDepiControlConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexDepiControlConfigApplyChange_Object = MibTableColumn
apexDepiControlConfigApplyChange = _ApexDepiControlConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 2, 1, 2),
    _ApexDepiControlConfigApplyChange_Type()
)
apexDepiControlConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigApplyChange.setStatus("current")
_ApexDepiControlConfigTable_Object = MibTable
apexDepiControlConfigTable = _ApexDepiControlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3)
)
if mibBuilder.loadTexts:
    apexDepiControlConfigTable.setStatus("current")
_ApexDepiControlConfigEntry_Object = MibTableRow
apexDepiControlConfigEntry = _ApexDepiControlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1)
)
apexDepiControlConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiControlConfigIndex"),
)
if mibBuilder.loadTexts:
    apexDepiControlConfigEntry.setStatus("current")


class _ApexDepiControlConfigIndex_Type(Integer32):
    """Custom type apexDepiControlConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApexDepiControlConfigIndex_Type.__name__ = "Integer32"
_ApexDepiControlConfigIndex_Object = MibTableColumn
apexDepiControlConfigIndex = _ApexDepiControlConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 1),
    _ApexDepiControlConfigIndex_Type()
)
apexDepiControlConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiControlConfigIndex.setStatus("current")
_ApexDepiControlConfigEnable_Type = EnableDisableTYPE
_ApexDepiControlConfigEnable_Object = MibTableColumn
apexDepiControlConfigEnable = _ApexDepiControlConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 2),
    _ApexDepiControlConfigEnable_Type()
)
apexDepiControlConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigEnable.setStatus("current")


class _ApexDepiControlConfigInterfaceNumber_Type(Integer32):
    """Custom type apexDepiControlConfigInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ApexDepiControlConfigInterfaceNumber_Type.__name__ = "Integer32"
_ApexDepiControlConfigInterfaceNumber_Object = MibTableColumn
apexDepiControlConfigInterfaceNumber = _ApexDepiControlConfigInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 3),
    _ApexDepiControlConfigInterfaceNumber_Type()
)
apexDepiControlConfigInterfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigInterfaceNumber.setStatus("current")
_ApexDepiControlConfigSrcIpAddr_Type = IpAddress
_ApexDepiControlConfigSrcIpAddr_Object = MibTableColumn
apexDepiControlConfigSrcIpAddr = _ApexDepiControlConfigSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 4),
    _ApexDepiControlConfigSrcIpAddr_Type()
)
apexDepiControlConfigSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigSrcIpAddr.setStatus("current")


class _ApexDepiControlConfigOverUdp_Type(Integer32):
    """Custom type apexDepiControlConfigOverUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("over-IP", 1),
          ("over-UDP", 2))
    )


_ApexDepiControlConfigOverUdp_Type.__name__ = "Integer32"
_ApexDepiControlConfigOverUdp_Object = MibTableColumn
apexDepiControlConfigOverUdp = _ApexDepiControlConfigOverUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 5),
    _ApexDepiControlConfigOverUdp_Type()
)
apexDepiControlConfigOverUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigOverUdp.setStatus("current")


class _ApexDepiControlConfigType_Type(Integer32):
    """Custom type apexDepiControlConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ApexDepiControlConfigType_Type.__name__ = "Integer32"
_ApexDepiControlConfigType_Object = MibTableColumn
apexDepiControlConfigType = _ApexDepiControlConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 1, 3, 1, 6),
    _ApexDepiControlConfigType_Type()
)
apexDepiControlConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiControlConfigType.setStatus("current")
_ApexDepiControlStatus_ObjectIdentity = ObjectIdentity
apexDepiControlStatus = _ApexDepiControlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2)
)
_ApexDepiControlStatusGeneral_ObjectIdentity = ObjectIdentity
apexDepiControlStatusGeneral = _ApexDepiControlStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1)
)
_ApexDepiControlStatusGeneralTotalConnections_Type = Integer32
_ApexDepiControlStatusGeneralTotalConnections_Object = MibScalar
apexDepiControlStatusGeneralTotalConnections = _ApexDepiControlStatusGeneralTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 1),
    _ApexDepiControlStatusGeneralTotalConnections_Type()
)
apexDepiControlStatusGeneralTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralTotalConnections.setStatus("current")


class _ApexDepiControlStatusGeneralCurrentConnections_Type(Integer32):
    """Custom type apexDepiControlStatusGeneralCurrentConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApexDepiControlStatusGeneralCurrentConnections_Type.__name__ = "Integer32"
_ApexDepiControlStatusGeneralCurrentConnections_Object = MibScalar
apexDepiControlStatusGeneralCurrentConnections = _ApexDepiControlStatusGeneralCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 2),
    _ApexDepiControlStatusGeneralCurrentConnections_Type()
)
apexDepiControlStatusGeneralCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralCurrentConnections.setStatus("current")
_ApexDepiControlStatusGeneralRejectedConnections_Type = Integer32
_ApexDepiControlStatusGeneralRejectedConnections_Object = MibScalar
apexDepiControlStatusGeneralRejectedConnections = _ApexDepiControlStatusGeneralRejectedConnections_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 3),
    _ApexDepiControlStatusGeneralRejectedConnections_Type()
)
apexDepiControlStatusGeneralRejectedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralRejectedConnections.setStatus("current")
_ApexDepiControlStatusGeneralUnknownConnectionMessages_Type = Integer32
_ApexDepiControlStatusGeneralUnknownConnectionMessages_Object = MibScalar
apexDepiControlStatusGeneralUnknownConnectionMessages = _ApexDepiControlStatusGeneralUnknownConnectionMessages_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 4),
    _ApexDepiControlStatusGeneralUnknownConnectionMessages_Type()
)
apexDepiControlStatusGeneralUnknownConnectionMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralUnknownConnectionMessages.setStatus("current")
_ApexDepiControlStatusGeneralUnknownSessionMessages_Type = Integer32
_ApexDepiControlStatusGeneralUnknownSessionMessages_Object = MibScalar
apexDepiControlStatusGeneralUnknownSessionMessages = _ApexDepiControlStatusGeneralUnknownSessionMessages_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 5),
    _ApexDepiControlStatusGeneralUnknownSessionMessages_Type()
)
apexDepiControlStatusGeneralUnknownSessionMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralUnknownSessionMessages.setStatus("current")


class _ApexDepiControlStatusGeneralInvalidApplyText_Type(DisplayString):
    """Custom type apexDepiControlStatusGeneralInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexDepiControlStatusGeneralInvalidApplyText_Type.__name__ = "DisplayString"
_ApexDepiControlStatusGeneralInvalidApplyText_Object = MibScalar
apexDepiControlStatusGeneralInvalidApplyText = _ApexDepiControlStatusGeneralInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 1, 6),
    _ApexDepiControlStatusGeneralInvalidApplyText_Type()
)
apexDepiControlStatusGeneralInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusGeneralInvalidApplyText.setStatus("current")
_ApexDepiControlStatusTable_Object = MibTable
apexDepiControlStatusTable = _ApexDepiControlStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2)
)
if mibBuilder.loadTexts:
    apexDepiControlStatusTable.setStatus("current")
_ApexDepiControlStatusEntry_Object = MibTableRow
apexDepiControlStatusEntry = _ApexDepiControlStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1)
)
apexDepiControlStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiControlStatusIndex"),
)
if mibBuilder.loadTexts:
    apexDepiControlStatusEntry.setStatus("current")


class _ApexDepiControlStatusIndex_Type(Integer32):
    """Custom type apexDepiControlStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApexDepiControlStatusIndex_Type.__name__ = "Integer32"
_ApexDepiControlStatusIndex_Object = MibTableColumn
apexDepiControlStatusIndex = _ApexDepiControlStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 1),
    _ApexDepiControlStatusIndex_Type()
)
apexDepiControlStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiControlStatusIndex.setStatus("current")
_ApexDepiControlStatusLocalUdp_Type = Integer32
_ApexDepiControlStatusLocalUdp_Object = MibTableColumn
apexDepiControlStatusLocalUdp = _ApexDepiControlStatusLocalUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 2),
    _ApexDepiControlStatusLocalUdp_Type()
)
apexDepiControlStatusLocalUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusLocalUdp.setStatus("current")
_ApexDepiControlStatusRemoteUdp_Type = Integer32
_ApexDepiControlStatusRemoteUdp_Object = MibTableColumn
apexDepiControlStatusRemoteUdp = _ApexDepiControlStatusRemoteUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 3),
    _ApexDepiControlStatusRemoteUdp_Type()
)
apexDepiControlStatusRemoteUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusRemoteUdp.setStatus("current")


class _ApexDepiControlStatusConnectionStatus_Type(Integer32):
    """Custom type apexDepiControlStatusConnectionStatus based on Integer32"""
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
        *(("established", 4),
          ("failed", 2),
          ("terminated", 1),
          ("waiting", 3))
    )


_ApexDepiControlStatusConnectionStatus_Type.__name__ = "Integer32"
_ApexDepiControlStatusConnectionStatus_Object = MibTableColumn
apexDepiControlStatusConnectionStatus = _ApexDepiControlStatusConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 4),
    _ApexDepiControlStatusConnectionStatus_Type()
)
apexDepiControlStatusConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusConnectionStatus.setStatus("current")
_ApexDepiControlStatusUnknownCtl_Type = Unsigned32
_ApexDepiControlStatusUnknownCtl_Object = MibTableColumn
apexDepiControlStatusUnknownCtl = _ApexDepiControlStatusUnknownCtl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 5),
    _ApexDepiControlStatusUnknownCtl_Type()
)
apexDepiControlStatusUnknownCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusUnknownCtl.setStatus("current")
_ApexDepiControlStatusMalformedCtl_Type = Unsigned32
_ApexDepiControlStatusMalformedCtl_Object = MibTableColumn
apexDepiControlStatusMalformedCtl = _ApexDepiControlStatusMalformedCtl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 6),
    _ApexDepiControlStatusMalformedCtl_Type()
)
apexDepiControlStatusMalformedCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusMalformedCtl.setStatus("current")
_ApexDepiControlStatusUnknownAvp_Type = Unsigned32
_ApexDepiControlStatusUnknownAvp_Object = MibTableColumn
apexDepiControlStatusUnknownAvp = _ApexDepiControlStatusUnknownAvp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 7),
    _ApexDepiControlStatusUnknownAvp_Type()
)
apexDepiControlStatusUnknownAvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusUnknownAvp.setStatus("current")
_ApexDepiControlStatusMalformedAvp_Type = Unsigned32
_ApexDepiControlStatusMalformedAvp_Object = MibTableColumn
apexDepiControlStatusMalformedAvp = _ApexDepiControlStatusMalformedAvp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 8),
    _ApexDepiControlStatusMalformedAvp_Type()
)
apexDepiControlStatusMalformedAvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusMalformedAvp.setStatus("current")
_ApexDepiControlStatusInvalidVendorId_Type = Unsigned32
_ApexDepiControlStatusInvalidVendorId_Object = MibTableColumn
apexDepiControlStatusInvalidVendorId = _ApexDepiControlStatusInvalidVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 9),
    _ApexDepiControlStatusInvalidVendorId_Type()
)
apexDepiControlStatusInvalidVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusInvalidVendorId.setStatus("current")
_ApexDepiControlStatusHbitSet_Type = Unsigned32
_ApexDepiControlStatusHbitSet_Object = MibTableColumn
apexDepiControlStatusHbitSet = _ApexDepiControlStatusHbitSet_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 10),
    _ApexDepiControlStatusHbitSet_Type()
)
apexDepiControlStatusHbitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusHbitSet.setStatus("current")
_ApexDepiControlStatusTotalSessions_Type = Unsigned32
_ApexDepiControlStatusTotalSessions_Object = MibTableColumn
apexDepiControlStatusTotalSessions = _ApexDepiControlStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 11),
    _ApexDepiControlStatusTotalSessions_Type()
)
apexDepiControlStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusTotalSessions.setStatus("current")
_ApexDepiControlStatusCurrentSessions_Type = Unsigned32
_ApexDepiControlStatusCurrentSessions_Object = MibTableColumn
apexDepiControlStatusCurrentSessions = _ApexDepiControlStatusCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 12),
    _ApexDepiControlStatusCurrentSessions_Type()
)
apexDepiControlStatusCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusCurrentSessions.setStatus("current")
_ApexDepiControlStatusRejectedSessions_Type = Unsigned32
_ApexDepiControlStatusRejectedSessions_Object = MibTableColumn
apexDepiControlStatusRejectedSessions = _ApexDepiControlStatusRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 3, 2, 2, 1, 13),
    _ApexDepiControlStatusRejectedSessions_Type()
)
apexDepiControlStatusRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiControlStatusRejectedSessions.setStatus("current")
_ApexDepiSession_ObjectIdentity = ObjectIdentity
apexDepiSession = _ApexDepiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4)
)
_ApexDepiSessionConfig_ObjectIdentity = ObjectIdentity
apexDepiSessionConfig = _ApexDepiSessionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1)
)
_ApexDepiSessionConfigApplyTable_Object = MibTable
apexDepiSessionConfigApplyTable = _ApexDepiSessionConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 1)
)
if mibBuilder.loadTexts:
    apexDepiSessionConfigApplyTable.setStatus("current")
_ApexDepiSessionConfigApplyEntry_Object = MibTableRow
apexDepiSessionConfigApplyEntry = _ApexDepiSessionConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 1, 1)
)
apexDepiSessionConfigApplyEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiSessionConfigApplyOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexDepiSessionConfigApplyEntry.setStatus("current")


class _ApexDepiSessionConfigApplyOutputTsNum_Type(Integer32):
    """Custom type apexDepiSessionConfigApplyOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexDepiSessionConfigApplyOutputTsNum_Type.__name__ = "Integer32"
_ApexDepiSessionConfigApplyOutputTsNum_Object = MibTableColumn
apexDepiSessionConfigApplyOutputTsNum = _ApexDepiSessionConfigApplyOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 1, 1, 1),
    _ApexDepiSessionConfigApplyOutputTsNum_Type()
)
apexDepiSessionConfigApplyOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiSessionConfigApplyOutputTsNum.setStatus("current")
_ApexDepiSessionConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexDepiSessionConfigApplyChange_Object = MibTableColumn
apexDepiSessionConfigApplyChange = _ApexDepiSessionConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 1, 1, 2),
    _ApexDepiSessionConfigApplyChange_Type()
)
apexDepiSessionConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigApplyChange.setStatus("current")
_ApexDepiSessionConfigTable_Object = MibTable
apexDepiSessionConfigTable = _ApexDepiSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2)
)
if mibBuilder.loadTexts:
    apexDepiSessionConfigTable.setStatus("current")
_ApexDepiSessionConfigEntry_Object = MibTableRow
apexDepiSessionConfigEntry = _ApexDepiSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1)
)
apexDepiSessionConfigEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiSessionConfigOutputTsNum"),
)
if mibBuilder.loadTexts:
    apexDepiSessionConfigEntry.setStatus("current")


class _ApexDepiSessionConfigOutputTsNum_Type(Integer32):
    """Custom type apexDepiSessionConfigOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexDepiSessionConfigOutputTsNum_Type.__name__ = "Integer32"
_ApexDepiSessionConfigOutputTsNum_Object = MibTableColumn
apexDepiSessionConfigOutputTsNum = _ApexDepiSessionConfigOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 1),
    _ApexDepiSessionConfigOutputTsNum_Type()
)
apexDepiSessionConfigOutputTsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiSessionConfigOutputTsNum.setStatus("current")
_ApexDepiSessionConfigEnable_Type = EnableDisableTYPE
_ApexDepiSessionConfigEnable_Object = MibTableColumn
apexDepiSessionConfigEnable = _ApexDepiSessionConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 2),
    _ApexDepiSessionConfigEnable_Type()
)
apexDepiSessionConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigEnable.setStatus("current")


class _ApexDepiSessionConfigControlId_Type(Integer32):
    """Custom type apexDepiSessionConfigControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ApexDepiSessionConfigControlId_Type.__name__ = "Integer32"
_ApexDepiSessionConfigControlId_Object = MibTableColumn
apexDepiSessionConfigControlId = _ApexDepiSessionConfigControlId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 3),
    _ApexDepiSessionConfigControlId_Type()
)
apexDepiSessionConfigControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigControlId.setStatus("current")


class _ApexDepiSessionConfigDocsisTsid_Type(Integer32):
    """Custom type apexDepiSessionConfigDocsisTsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexDepiSessionConfigDocsisTsid_Type.__name__ = "Integer32"
_ApexDepiSessionConfigDocsisTsid_Object = MibTableColumn
apexDepiSessionConfigDocsisTsid = _ApexDepiSessionConfigDocsisTsid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 4),
    _ApexDepiSessionConfigDocsisTsid_Type()
)
apexDepiSessionConfigDocsisTsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigDocsisTsid.setStatus("current")


class _ApexDepiSessionConfigUdpPort_Type(Integer32):
    """Custom type apexDepiSessionConfigUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApexDepiSessionConfigUdpPort_Type.__name__ = "Integer32"
_ApexDepiSessionConfigUdpPort_Object = MibTableColumn
apexDepiSessionConfigUdpPort = _ApexDepiSessionConfigUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 5),
    _ApexDepiSessionConfigUdpPort_Type()
)
apexDepiSessionConfigUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigUdpPort.setStatus("current")
_ApexDepiSessionConfigSyncCorrection_Type = EnableDisableTYPE
_ApexDepiSessionConfigSyncCorrection_Object = MibTableColumn
apexDepiSessionConfigSyncCorrection = _ApexDepiSessionConfigSyncCorrection_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 1, 2, 1, 6),
    _ApexDepiSessionConfigSyncCorrection_Type()
)
apexDepiSessionConfigSyncCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexDepiSessionConfigSyncCorrection.setStatus("current")
_ApexDepiSessionStatus_ObjectIdentity = ObjectIdentity
apexDepiSessionStatus = _ApexDepiSessionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2)
)
_ApexDepiSessionStatusGeneral_ObjectIdentity = ObjectIdentity
apexDepiSessionStatusGeneral = _ApexDepiSessionStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 1)
)


class _ApexDepiSessionStatusGeneralInvalidApplyText_Type(DisplayString):
    """Custom type apexDepiSessionStatusGeneralInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApexDepiSessionStatusGeneralInvalidApplyText_Type.__name__ = "DisplayString"
_ApexDepiSessionStatusGeneralInvalidApplyText_Object = MibScalar
apexDepiSessionStatusGeneralInvalidApplyText = _ApexDepiSessionStatusGeneralInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 1, 1),
    _ApexDepiSessionStatusGeneralInvalidApplyText_Type()
)
apexDepiSessionStatusGeneralInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusGeneralInvalidApplyText.setStatus("current")
_ApexDepiSessionStatusTable_Object = MibTable
apexDepiSessionStatusTable = _ApexDepiSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2)
)
if mibBuilder.loadTexts:
    apexDepiSessionStatusTable.setStatus("current")
_ApexDepiSessionStatusEntry_Object = MibTableRow
apexDepiSessionStatusEntry = _ApexDepiSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1)
)
apexDepiSessionStatusEntry.setIndexNames(
    (0, "APEX-MIB", "apexDepiSessionStatusIndex"),
)
if mibBuilder.loadTexts:
    apexDepiSessionStatusEntry.setStatus("current")


class _ApexDepiSessionStatusIndex_Type(Integer32):
    """Custom type apexDepiSessionStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexDepiSessionStatusIndex_Type.__name__ = "Integer32"
_ApexDepiSessionStatusIndex_Object = MibTableColumn
apexDepiSessionStatusIndex = _ApexDepiSessionStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 1),
    _ApexDepiSessionStatusIndex_Type()
)
apexDepiSessionStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexDepiSessionStatusIndex.setStatus("current")
_ApexDepiSessionStatusControlId_Type = Integer32
_ApexDepiSessionStatusControlId_Object = MibTableColumn
apexDepiSessionStatusControlId = _ApexDepiSessionStatusControlId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 2),
    _ApexDepiSessionStatusControlId_Type()
)
apexDepiSessionStatusControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusControlId.setStatus("current")
_ApexDepiSessionStatusOutputQAMChannel_Type = Integer32
_ApexDepiSessionStatusOutputQAMChannel_Object = MibTableColumn
apexDepiSessionStatusOutputQAMChannel = _ApexDepiSessionStatusOutputQAMChannel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 3),
    _ApexDepiSessionStatusOutputQAMChannel_Type()
)
apexDepiSessionStatusOutputQAMChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusOutputQAMChannel.setStatus("current")
_ApexDepiSessionStatusLocalUdp_Type = Integer32
_ApexDepiSessionStatusLocalUdp_Object = MibTableColumn
apexDepiSessionStatusLocalUdp = _ApexDepiSessionStatusLocalUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 4),
    _ApexDepiSessionStatusLocalUdp_Type()
)
apexDepiSessionStatusLocalUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusLocalUdp.setStatus("current")
_ApexDepiSessionStatusRemoteUdp_Type = Integer32
_ApexDepiSessionStatusRemoteUdp_Object = MibTableColumn
apexDepiSessionStatusRemoteUdp = _ApexDepiSessionStatusRemoteUdp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 5),
    _ApexDepiSessionStatusRemoteUdp_Type()
)
apexDepiSessionStatusRemoteUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusRemoteUdp.setStatus("current")


class _ApexDepiSessionStatusStatus_Type(Integer32):
    """Custom type apexDepiSessionStatusStatus based on Integer32"""
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
        *(("established", 4),
          ("failed", 2),
          ("terminated", 1),
          ("waiting", 3))
    )


_ApexDepiSessionStatusStatus_Type.__name__ = "Integer32"
_ApexDepiSessionStatusStatus_Object = MibTableColumn
apexDepiSessionStatusStatus = _ApexDepiSessionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 6),
    _ApexDepiSessionStatusStatus_Type()
)
apexDepiSessionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusStatus.setStatus("current")
_ApexDepiSessionStatusPerHopBehavior_Type = Integer32
_ApexDepiSessionStatusPerHopBehavior_Object = MibTableColumn
apexDepiSessionStatusPerHopBehavior = _ApexDepiSessionStatusPerHopBehavior_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 7),
    _ApexDepiSessionStatusPerHopBehavior_Type()
)
apexDepiSessionStatusPerHopBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusPerHopBehavior.setStatus("current")
_ApexDepiSessionStatusUnknownCtl_Type = Unsigned32
_ApexDepiSessionStatusUnknownCtl_Object = MibTableColumn
apexDepiSessionStatusUnknownCtl = _ApexDepiSessionStatusUnknownCtl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 8),
    _ApexDepiSessionStatusUnknownCtl_Type()
)
apexDepiSessionStatusUnknownCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusUnknownCtl.setStatus("current")
_ApexDepiSessionStatusMalformedCtl_Type = Unsigned32
_ApexDepiSessionStatusMalformedCtl_Object = MibTableColumn
apexDepiSessionStatusMalformedCtl = _ApexDepiSessionStatusMalformedCtl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 9),
    _ApexDepiSessionStatusMalformedCtl_Type()
)
apexDepiSessionStatusMalformedCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusMalformedCtl.setStatus("current")
_ApexDepiSessionStatusUnknownAvp_Type = Unsigned32
_ApexDepiSessionStatusUnknownAvp_Object = MibTableColumn
apexDepiSessionStatusUnknownAvp = _ApexDepiSessionStatusUnknownAvp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 10),
    _ApexDepiSessionStatusUnknownAvp_Type()
)
apexDepiSessionStatusUnknownAvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusUnknownAvp.setStatus("current")
_ApexDepiSessionStatusMalformedAvp_Type = Unsigned32
_ApexDepiSessionStatusMalformedAvp_Object = MibTableColumn
apexDepiSessionStatusMalformedAvp = _ApexDepiSessionStatusMalformedAvp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 11),
    _ApexDepiSessionStatusMalformedAvp_Type()
)
apexDepiSessionStatusMalformedAvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusMalformedAvp.setStatus("current")
_ApexDepiSessionStatusInvalidVendorId_Type = Unsigned32
_ApexDepiSessionStatusInvalidVendorId_Object = MibTableColumn
apexDepiSessionStatusInvalidVendorId = _ApexDepiSessionStatusInvalidVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 12),
    _ApexDepiSessionStatusInvalidVendorId_Type()
)
apexDepiSessionStatusInvalidVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusInvalidVendorId.setStatus("current")
_ApexDepiSessionStatusHbitSet_Type = Unsigned32
_ApexDepiSessionStatusHbitSet_Object = MibTableColumn
apexDepiSessionStatusHbitSet = _ApexDepiSessionStatusHbitSet_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 13),
    _ApexDepiSessionStatusHbitSet_Type()
)
apexDepiSessionStatusHbitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusHbitSet.setStatus("current")
_ApexDepiSessionStatusInSLIMsgs_Type = Unsigned32
_ApexDepiSessionStatusInSLIMsgs_Object = MibTableColumn
apexDepiSessionStatusInSLIMsgs = _ApexDepiSessionStatusInSLIMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 14),
    _ApexDepiSessionStatusInSLIMsgs_Type()
)
apexDepiSessionStatusInSLIMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusInSLIMsgs.setStatus("current")
_ApexDepiSessionStatusOutSLIMsgs_Type = Unsigned32
_ApexDepiSessionStatusOutSLIMsgs_Object = MibTableColumn
apexDepiSessionStatusOutSLIMsgs = _ApexDepiSessionStatusOutSLIMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 15),
    _ApexDepiSessionStatusOutSLIMsgs_Type()
)
apexDepiSessionStatusOutSLIMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusOutSLIMsgs.setStatus("current")
_ApexDepiSessionStatusIngressDlmMsgs_Type = Unsigned32
_ApexDepiSessionStatusIngressDlmMsgs_Object = MibTableColumn
apexDepiSessionStatusIngressDlmMsgs = _ApexDepiSessionStatusIngressDlmMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 16),
    _ApexDepiSessionStatusIngressDlmMsgs_Type()
)
apexDepiSessionStatusIngressDlmMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusIngressDlmMsgs.setStatus("current")
_ApexDepiSessionStatusEgressDlmMsgs_Type = Unsigned32
_ApexDepiSessionStatusEgressDlmMsgs_Object = MibTableColumn
apexDepiSessionStatusEgressDlmMsgs = _ApexDepiSessionStatusEgressDlmMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 17),
    _ApexDepiSessionStatusEgressDlmMsgs_Type()
)
apexDepiSessionStatusEgressDlmMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusEgressDlmMsgs.setStatus("current")
_ApexDepiSessionStatusLatencyStart_Type = Unsigned32
_ApexDepiSessionStatusLatencyStart_Object = MibTableColumn
apexDepiSessionStatusLatencyStart = _ApexDepiSessionStatusLatencyStart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 18),
    _ApexDepiSessionStatusLatencyStart_Type()
)
apexDepiSessionStatusLatencyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusLatencyStart.setStatus("current")
_ApexDepiSessionStatusLatencyEnd_Type = Unsigned32
_ApexDepiSessionStatusLatencyEnd_Object = MibTableColumn
apexDepiSessionStatusLatencyEnd = _ApexDepiSessionStatusLatencyEnd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 19),
    _ApexDepiSessionStatusLatencyEnd_Type()
)
apexDepiSessionStatusLatencyEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusLatencyEnd.setStatus("current")
_ApexDepiSessionStatusInDataPackets_Type = Unsigned32
_ApexDepiSessionStatusInDataPackets_Object = MibTableColumn
apexDepiSessionStatusInDataPackets = _ApexDepiSessionStatusInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 20),
    _ApexDepiSessionStatusInDataPackets_Type()
)
apexDepiSessionStatusInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusInDataPackets.setStatus("current")
_ApexDepiSessionStatusInSequenceDiscards_Type = Unsigned32
_ApexDepiSessionStatusInSequenceDiscards_Object = MibTableColumn
apexDepiSessionStatusInSequenceDiscards = _ApexDepiSessionStatusInSequenceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 21),
    _ApexDepiSessionStatusInSequenceDiscards_Type()
)
apexDepiSessionStatusInSequenceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusInSequenceDiscards.setStatus("current")
_ApexDepiSessionStatusInDataPacketDiscards_Type = Unsigned32
_ApexDepiSessionStatusInDataPacketDiscards_Object = MibTableColumn
apexDepiSessionStatusInDataPacketDiscards = _ApexDepiSessionStatusInDataPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 22),
    _ApexDepiSessionStatusInDataPacketDiscards_Type()
)
apexDepiSessionStatusInDataPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusInDataPacketDiscards.setStatus("current")
_ApexDepiSessionStatusSessionID_Type = Unsigned32
_ApexDepiSessionStatusSessionID_Object = MibTableColumn
apexDepiSessionStatusSessionID = _ApexDepiSessionStatusSessionID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 24, 4, 2, 2, 1, 23),
    _ApexDepiSessionStatusSessionID_Type()
)
apexDepiSessionStatusSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexDepiSessionStatusSessionID.setStatus("current")
_ApexPsip_ObjectIdentity = ObjectIdentity
apexPsip = _ApexPsip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25)
)
_ApexPsipConfig_ObjectIdentity = ObjectIdentity
apexPsipConfig = _ApexPsipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1)
)
_ApexPsipConfigGeneral_ObjectIdentity = ObjectIdentity
apexPsipConfigGeneral = _ApexPsipConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1)
)
_ApexPsipConfigApplyChange_Type = ApplyDataToDeviceTYPE
_ApexPsipConfigApplyChange_Object = MibScalar
apexPsipConfigApplyChange = _ApexPsipConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 1),
    _ApexPsipConfigApplyChange_Type()
)
apexPsipConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigApplyChange.setStatus("current")


class _ApexPsipConfigMgtMsgInsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigMgtMsgInsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1000),
    )


_ApexPsipConfigMgtMsgInsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigMgtMsgInsertionPeriod_Object = MibScalar
apexPsipConfigMgtMsgInsertionPeriod = _ApexPsipConfigMgtMsgInsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 2),
    _ApexPsipConfigMgtMsgInsertionPeriod_Type()
)
apexPsipConfigMgtMsgInsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigMgtMsgInsertionPeriod.setStatus("current")


class _ApexPsipConfigSttMsgInsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigSttMsgInsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_ApexPsipConfigSttMsgInsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigSttMsgInsertionPeriod_Object = MibScalar
apexPsipConfigSttMsgInsertionPeriod = _ApexPsipConfigSttMsgInsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 3),
    _ApexPsipConfigSttMsgInsertionPeriod_Type()
)
apexPsipConfigSttMsgInsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigSttMsgInsertionPeriod.setStatus("current")


class _ApexPsipConfigCvctMsgInsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigCvctMsgInsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 1000),
    )


_ApexPsipConfigCvctMsgInsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigCvctMsgInsertionPeriod_Object = MibScalar
apexPsipConfigCvctMsgInsertionPeriod = _ApexPsipConfigCvctMsgInsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 4),
    _ApexPsipConfigCvctMsgInsertionPeriod_Type()
)
apexPsipConfigCvctMsgInsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigCvctMsgInsertionPeriod.setStatus("current")


class _ApexPsipConfigRrtMsgInsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigRrtMsgInsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 60000),
    )


_ApexPsipConfigRrtMsgInsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigRrtMsgInsertionPeriod_Object = MibScalar
apexPsipConfigRrtMsgInsertionPeriod = _ApexPsipConfigRrtMsgInsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 5),
    _ApexPsipConfigRrtMsgInsertionPeriod_Type()
)
apexPsipConfigRrtMsgInsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigRrtMsgInsertionPeriod.setStatus("current")


class _ApexPsipConfigEit0InsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigEit0InsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_ApexPsipConfigEit0InsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigEit0InsertionPeriod_Object = MibScalar
apexPsipConfigEit0InsertionPeriod = _ApexPsipConfigEit0InsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 6),
    _ApexPsipConfigEit0InsertionPeriod_Type()
)
apexPsipConfigEit0InsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigEit0InsertionPeriod.setStatus("current")


class _ApexPsipConfigEit1InsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigEit1InsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_ApexPsipConfigEit1InsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigEit1InsertionPeriod_Object = MibScalar
apexPsipConfigEit1InsertionPeriod = _ApexPsipConfigEit1InsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 7),
    _ApexPsipConfigEit1InsertionPeriod_Type()
)
apexPsipConfigEit1InsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigEit1InsertionPeriod.setStatus("current")


class _ApexPsipConfigEit2InsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigEit2InsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_ApexPsipConfigEit2InsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigEit2InsertionPeriod_Object = MibScalar
apexPsipConfigEit2InsertionPeriod = _ApexPsipConfigEit2InsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 8),
    _ApexPsipConfigEit2InsertionPeriod_Type()
)
apexPsipConfigEit2InsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigEit2InsertionPeriod.setStatus("current")


class _ApexPsipConfigEit3InsertionPeriod_Type(Unsigned32):
    """Custom type apexPsipConfigEit3InsertionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_ApexPsipConfigEit3InsertionPeriod_Type.__name__ = "Unsigned32"
_ApexPsipConfigEit3InsertionPeriod_Object = MibScalar
apexPsipConfigEit3InsertionPeriod = _ApexPsipConfigEit3InsertionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 1, 9),
    _ApexPsipConfigEit3InsertionPeriod_Type()
)
apexPsipConfigEit3InsertionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigEit3InsertionPeriod.setStatus("current")
_ApexPsipConfigTime_ObjectIdentity = ObjectIdentity
apexPsipConfigTime = _ApexPsipConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2)
)
_ApexPsipConfigTimeApplyChange_Type = ApplyDataToDeviceTYPE
_ApexPsipConfigTimeApplyChange_Object = MibScalar
apexPsipConfigTimeApplyChange = _ApexPsipConfigTimeApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 1),
    _ApexPsipConfigTimeApplyChange_Type()
)
apexPsipConfigTimeApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeApplyChange.setStatus("current")


class _ApexPsipConfigTimeDsMonthIn_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsMonthIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexPsipConfigTimeDsMonthIn_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsMonthIn_Object = MibScalar
apexPsipConfigTimeDsMonthIn = _ApexPsipConfigTimeDsMonthIn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 2),
    _ApexPsipConfigTimeDsMonthIn_Type()
)
apexPsipConfigTimeDsMonthIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsMonthIn.setStatus("current")


class _ApexPsipConfigTimeDsDayIn_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsDayIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApexPsipConfigTimeDsDayIn_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsDayIn_Object = MibScalar
apexPsipConfigTimeDsDayIn = _ApexPsipConfigTimeDsDayIn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 3),
    _ApexPsipConfigTimeDsDayIn_Type()
)
apexPsipConfigTimeDsDayIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsDayIn.setStatus("current")


class _ApexPsipConfigTimeDsHourIn_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsHourIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_ApexPsipConfigTimeDsHourIn_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsHourIn_Object = MibScalar
apexPsipConfigTimeDsHourIn = _ApexPsipConfigTimeDsHourIn_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 4),
    _ApexPsipConfigTimeDsHourIn_Type()
)
apexPsipConfigTimeDsHourIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsHourIn.setStatus("current")


class _ApexPsipConfigTimeDsMonthOut_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsMonthOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApexPsipConfigTimeDsMonthOut_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsMonthOut_Object = MibScalar
apexPsipConfigTimeDsMonthOut = _ApexPsipConfigTimeDsMonthOut_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 5),
    _ApexPsipConfigTimeDsMonthOut_Type()
)
apexPsipConfigTimeDsMonthOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsMonthOut.setStatus("current")


class _ApexPsipConfigTimeDsDayOut_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsDayOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApexPsipConfigTimeDsDayOut_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsDayOut_Object = MibScalar
apexPsipConfigTimeDsDayOut = _ApexPsipConfigTimeDsDayOut_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 6),
    _ApexPsipConfigTimeDsDayOut_Type()
)
apexPsipConfigTimeDsDayOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsDayOut.setStatus("current")


class _ApexPsipConfigTimeDsHourOut_Type(Unsigned32):
    """Custom type apexPsipConfigTimeDsHourOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_ApexPsipConfigTimeDsHourOut_Type.__name__ = "Unsigned32"
_ApexPsipConfigTimeDsHourOut_Object = MibScalar
apexPsipConfigTimeDsHourOut = _ApexPsipConfigTimeDsHourOut_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 1, 2, 7),
    _ApexPsipConfigTimeDsHourOut_Type()
)
apexPsipConfigTimeDsHourOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexPsipConfigTimeDsHourOut.setStatus("current")
_ApexPsipStatus_ObjectIdentity = ObjectIdentity
apexPsipStatus = _ApexPsipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2)
)
_ApexPsipStatusGeneral_ObjectIdentity = ObjectIdentity
apexPsipStatusGeneral = _ApexPsipStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 1)
)
_ApexPsipStatusInputTable_Object = MibTable
apexPsipStatusInputTable = _ApexPsipStatusInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2)
)
if mibBuilder.loadTexts:
    apexPsipStatusInputTable.setStatus("current")
_ApexPsipStatusInputEntry_Object = MibTableRow
apexPsipStatusInputEntry = _ApexPsipStatusInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1)
)
apexPsipStatusInputEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsipStatusInputIndex"),
    (0, "APEX-MIB", "apexPsipStatusInputPid"),
    (0, "APEX-MIB", "apexPsipStatusInputMessageType"),
    (0, "APEX-MIB", "apexPsipStatusInputSourceId"),
    (0, "APEX-MIB", "apexPsipStatusInputSegment"),
    (0, "APEX-MIB", "apexPsipStatusInputPart"),
)
if mibBuilder.loadTexts:
    apexPsipStatusInputEntry.setStatus("current")


class _ApexPsipStatusInputIndex_Type(Integer32):
    """Custom type apexPsipStatusInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 784),
    )


_ApexPsipStatusInputIndex_Type.__name__ = "Integer32"
_ApexPsipStatusInputIndex_Object = MibTableColumn
apexPsipStatusInputIndex = _ApexPsipStatusInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 1),
    _ApexPsipStatusInputIndex_Type()
)
apexPsipStatusInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputIndex.setStatus("current")


class _ApexPsipStatusInputPid_Type(Integer32):
    """Custom type apexPsipStatusInputPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ApexPsipStatusInputPid_Type.__name__ = "Integer32"
_ApexPsipStatusInputPid_Object = MibTableColumn
apexPsipStatusInputPid = _ApexPsipStatusInputPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 2),
    _ApexPsipStatusInputPid_Type()
)
apexPsipStatusInputPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputPid.setStatus("current")


class _ApexPsipStatusInputMessageType_Type(Integer32):
    """Custom type apexPsipStatusInputMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexPsipStatusInputMessageType_Type.__name__ = "Integer32"
_ApexPsipStatusInputMessageType_Object = MibTableColumn
apexPsipStatusInputMessageType = _ApexPsipStatusInputMessageType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 3),
    _ApexPsipStatusInputMessageType_Type()
)
apexPsipStatusInputMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputMessageType.setStatus("current")


class _ApexPsipStatusInputSourceId_Type(Integer32):
    """Custom type apexPsipStatusInputSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexPsipStatusInputSourceId_Type.__name__ = "Integer32"
_ApexPsipStatusInputSourceId_Object = MibTableColumn
apexPsipStatusInputSourceId = _ApexPsipStatusInputSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 4),
    _ApexPsipStatusInputSourceId_Type()
)
apexPsipStatusInputSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputSourceId.setStatus("current")


class _ApexPsipStatusInputSegment_Type(Integer32):
    """Custom type apexPsipStatusInputSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApexPsipStatusInputSegment_Type.__name__ = "Integer32"
_ApexPsipStatusInputSegment_Object = MibTableColumn
apexPsipStatusInputSegment = _ApexPsipStatusInputSegment_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 5),
    _ApexPsipStatusInputSegment_Type()
)
apexPsipStatusInputSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputSegment.setStatus("current")


class _ApexPsipStatusInputPart_Type(Integer32):
    """Custom type apexPsipStatusInputPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApexPsipStatusInputPart_Type.__name__ = "Integer32"
_ApexPsipStatusInputPart_Object = MibTableColumn
apexPsipStatusInputPart = _ApexPsipStatusInputPart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 6),
    _ApexPsipStatusInputPart_Type()
)
apexPsipStatusInputPart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusInputPart.setStatus("current")
_ApexPsipStatusInputBody_Type = DisplayString
_ApexPsipStatusInputBody_Object = MibTableColumn
apexPsipStatusInputBody = _ApexPsipStatusInputBody_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 7),
    _ApexPsipStatusInputBody_Type()
)
apexPsipStatusInputBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusInputBody.setStatus("current")
_ApexPsipStatusInputGpsTime_Type = Integer32
_ApexPsipStatusInputGpsTime_Object = MibTableColumn
apexPsipStatusInputGpsTime = _ApexPsipStatusInputGpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 8),
    _ApexPsipStatusInputGpsTime_Type()
)
apexPsipStatusInputGpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusInputGpsTime.setStatus("current")
_ApexPsipStatusInputInfo_Type = DisplayString
_ApexPsipStatusInputInfo_Object = MibTableColumn
apexPsipStatusInputInfo = _ApexPsipStatusInputInfo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 2, 1, 9),
    _ApexPsipStatusInputInfo_Type()
)
apexPsipStatusInputInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusInputInfo.setStatus("current")
_ApexPsipStatusOutputTable_Object = MibTable
apexPsipStatusOutputTable = _ApexPsipStatusOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3)
)
if mibBuilder.loadTexts:
    apexPsipStatusOutputTable.setStatus("current")
_ApexPsipStatusOutputEntry_Object = MibTableRow
apexPsipStatusOutputEntry = _ApexPsipStatusOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1)
)
apexPsipStatusOutputEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsipStatusOutputIndex"),
    (0, "APEX-MIB", "apexPsipStatusOutputPid"),
    (0, "APEX-MIB", "apexPsipStatusOutputMessageType"),
    (0, "APEX-MIB", "apexPsipStatusOutputSourceId"),
    (0, "APEX-MIB", "apexPsipStatusOutputSegment"),
    (0, "APEX-MIB", "apexPsipStatusOutputPart"),
)
if mibBuilder.loadTexts:
    apexPsipStatusOutputEntry.setStatus("current")


class _ApexPsipStatusOutputIndex_Type(Integer32):
    """Custom type apexPsipStatusOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexPsipStatusOutputIndex_Type.__name__ = "Integer32"
_ApexPsipStatusOutputIndex_Object = MibTableColumn
apexPsipStatusOutputIndex = _ApexPsipStatusOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 1),
    _ApexPsipStatusOutputIndex_Type()
)
apexPsipStatusOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputIndex.setStatus("current")


class _ApexPsipStatusOutputPid_Type(Integer32):
    """Custom type apexPsipStatusOutputPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ApexPsipStatusOutputPid_Type.__name__ = "Integer32"
_ApexPsipStatusOutputPid_Object = MibTableColumn
apexPsipStatusOutputPid = _ApexPsipStatusOutputPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 2),
    _ApexPsipStatusOutputPid_Type()
)
apexPsipStatusOutputPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputPid.setStatus("current")


class _ApexPsipStatusOutputMessageType_Type(Integer32):
    """Custom type apexPsipStatusOutputMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApexPsipStatusOutputMessageType_Type.__name__ = "Integer32"
_ApexPsipStatusOutputMessageType_Object = MibTableColumn
apexPsipStatusOutputMessageType = _ApexPsipStatusOutputMessageType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 3),
    _ApexPsipStatusOutputMessageType_Type()
)
apexPsipStatusOutputMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputMessageType.setStatus("current")


class _ApexPsipStatusOutputSourceId_Type(Integer32):
    """Custom type apexPsipStatusOutputSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApexPsipStatusOutputSourceId_Type.__name__ = "Integer32"
_ApexPsipStatusOutputSourceId_Object = MibTableColumn
apexPsipStatusOutputSourceId = _ApexPsipStatusOutputSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 4),
    _ApexPsipStatusOutputSourceId_Type()
)
apexPsipStatusOutputSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputSourceId.setStatus("current")


class _ApexPsipStatusOutputSegment_Type(Integer32):
    """Custom type apexPsipStatusOutputSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApexPsipStatusOutputSegment_Type.__name__ = "Integer32"
_ApexPsipStatusOutputSegment_Object = MibTableColumn
apexPsipStatusOutputSegment = _ApexPsipStatusOutputSegment_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 5),
    _ApexPsipStatusOutputSegment_Type()
)
apexPsipStatusOutputSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputSegment.setStatus("current")


class _ApexPsipStatusOutputPart_Type(Integer32):
    """Custom type apexPsipStatusOutputPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApexPsipStatusOutputPart_Type.__name__ = "Integer32"
_ApexPsipStatusOutputPart_Object = MibTableColumn
apexPsipStatusOutputPart = _ApexPsipStatusOutputPart_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 6),
    _ApexPsipStatusOutputPart_Type()
)
apexPsipStatusOutputPart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusOutputPart.setStatus("current")
_ApexPsipStatusOutputBody_Type = DisplayString
_ApexPsipStatusOutputBody_Object = MibTableColumn
apexPsipStatusOutputBody = _ApexPsipStatusOutputBody_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 7),
    _ApexPsipStatusOutputBody_Type()
)
apexPsipStatusOutputBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusOutputBody.setStatus("current")
_ApexPsipStatusOutputGpsTime_Type = Integer32
_ApexPsipStatusOutputGpsTime_Object = MibTableColumn
apexPsipStatusOutputGpsTime = _ApexPsipStatusOutputGpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 3, 1, 8),
    _ApexPsipStatusOutputGpsTime_Type()
)
apexPsipStatusOutputGpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusOutputGpsTime.setStatus("current")
_ApexPsipStatusServiceTable_Object = MibTable
apexPsipStatusServiceTable = _ApexPsipStatusServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4)
)
if mibBuilder.loadTexts:
    apexPsipStatusServiceTable.setStatus("current")
_ApexPsipStatusServiceEntry_Object = MibTableRow
apexPsipStatusServiceEntry = _ApexPsipStatusServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1)
)
apexPsipStatusServiceEntry.setIndexNames(
    (0, "APEX-MIB", "apexPsipStatusServiceIndex"),
)
if mibBuilder.loadTexts:
    apexPsipStatusServiceEntry.setStatus("current")


class _ApexPsipStatusServiceIndex_Type(Integer32):
    """Custom type apexPsipStatusServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_ApexPsipStatusServiceIndex_Type.__name__ = "Integer32"
_ApexPsipStatusServiceIndex_Object = MibTableColumn
apexPsipStatusServiceIndex = _ApexPsipStatusServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1, 1),
    _ApexPsipStatusServiceIndex_Type()
)
apexPsipStatusServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexPsipStatusServiceIndex.setStatus("current")
_ApexPsipStatusServiceNum_Type = Integer32
_ApexPsipStatusServiceNum_Object = MibTableColumn
apexPsipStatusServiceNum = _ApexPsipStatusServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1, 2),
    _ApexPsipStatusServiceNum_Type()
)
apexPsipStatusServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusServiceNum.setStatus("current")


class _ApexPsipStatusServiceOutputTs_Type(Integer32):
    """Custom type apexPsipStatusServiceOutputTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ApexPsipStatusServiceOutputTs_Type.__name__ = "Integer32"
_ApexPsipStatusServiceOutputTs_Object = MibTableColumn
apexPsipStatusServiceOutputTs = _ApexPsipStatusServiceOutputTs_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1, 3),
    _ApexPsipStatusServiceOutputTs_Type()
)
apexPsipStatusServiceOutputTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusServiceOutputTs.setStatus("current")


class _ApexPsipStatusServiceState_Type(DisplayString):
    """Custom type apexPsipStatusServiceState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApexPsipStatusServiceState_Type.__name__ = "DisplayString"
_ApexPsipStatusServiceState_Object = MibTableColumn
apexPsipStatusServiceState = _ApexPsipStatusServiceState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1, 4),
    _ApexPsipStatusServiceState_Type()
)
apexPsipStatusServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusServiceState.setStatus("current")


class _ApexPsipStatusServiceSourceId_Type(Integer32):
    """Custom type apexPsipStatusServiceSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApexPsipStatusServiceSourceId_Type.__name__ = "Integer32"
_ApexPsipStatusServiceSourceId_Object = MibTableColumn
apexPsipStatusServiceSourceId = _ApexPsipStatusServiceSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 25, 2, 4, 1, 5),
    _ApexPsipStatusServiceSourceId_Type()
)
apexPsipStatusServiceSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexPsipStatusServiceSourceId.setStatus("current")
_ApexPreencryption_ObjectIdentity = ObjectIdentity
apexPreencryption = _ApexPreencryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 26)
)
_ApexPreencryptionConfig_ObjectIdentity = ObjectIdentity
apexPreencryptionConfig = _ApexPreencryptionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 26, 1)
)
_ApexPreencryptionConfigGeneral_ObjectIdentity = ObjectIdentity
apexPreencryptionConfigGeneral = _ApexPreencryptionConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 26, 1, 1)
)
_ApexSupportPreencryptedSimulcrypt_Type = EnableDisableTYPE
_ApexSupportPreencryptedSimulcrypt_Object = MibScalar
apexSupportPreencryptedSimulcrypt = _ApexSupportPreencryptedSimulcrypt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 26, 1, 1, 1),
    _ApexSupportPreencryptedSimulcrypt_Type()
)
apexSupportPreencryptedSimulcrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexSupportPreencryptedSimulcrypt.setStatus("current")
_ApexAlarms_ObjectIdentity = ObjectIdentity
apexAlarms = _ApexAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100)
)


class _ApexAlarmHardwareFault_Type(Integer32):
    """Custom type apexAlarmHardwareFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmHardwareFault_Type.__name__ = "Integer32"
_ApexAlarmHardwareFault_Object = MibScalar
apexAlarmHardwareFault = _ApexAlarmHardwareFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8000),
    _ApexAlarmHardwareFault_Type()
)
apexAlarmHardwareFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmHardwareFault.setStatus("current")


class _ApexAlarmInvalidInitData_Type(Integer32):
    """Custom type apexAlarmInvalidInitData based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmInvalidInitData_Type.__name__ = "Integer32"
_ApexAlarmInvalidInitData_Object = MibScalar
apexAlarmInvalidInitData = _ApexAlarmInvalidInitData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8001),
    _ApexAlarmInvalidInitData_Type()
)
apexAlarmInvalidInitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmInvalidInitData.setStatus("current")


class _ApexAlarmTemperatureFault_Type(Integer32):
    """Custom type apexAlarmTemperatureFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmTemperatureFault_Type.__name__ = "Integer32"
_ApexAlarmTemperatureFault_Object = MibScalar
apexAlarmTemperatureFault = _ApexAlarmTemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8002),
    _ApexAlarmTemperatureFault_Type()
)
apexAlarmTemperatureFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmTemperatureFault.setStatus("current")


class _ApexAlarmFanFault_Type(Integer32):
    """Custom type apexAlarmFanFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmFanFault_Type.__name__ = "Integer32"
_ApexAlarmFanFault_Object = MibScalar
apexAlarmFanFault = _ApexAlarmFanFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8003),
    _ApexAlarmFanFault_Type()
)
apexAlarmFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmFanFault.setStatus("current")


class _ApexAlarmPowerFault_Type(Integer32):
    """Custom type apexAlarmPowerFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmPowerFault_Type.__name__ = "Integer32"
_ApexAlarmPowerFault_Object = MibScalar
apexAlarmPowerFault = _ApexAlarmPowerFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8004),
    _ApexAlarmPowerFault_Type()
)
apexAlarmPowerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmPowerFault.setStatus("current")


class _ApexAlarmGbeLossOfPhysicalInput_Type(Integer32):
    """Custom type apexAlarmGbeLossOfPhysicalInput based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeLossOfPhysicalInput_Type.__name__ = "Integer32"
_ApexAlarmGbeLossOfPhysicalInput_Object = MibScalar
apexAlarmGbeLossOfPhysicalInput = _ApexAlarmGbeLossOfPhysicalInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8020),
    _ApexAlarmGbeLossOfPhysicalInput_Type()
)
apexAlarmGbeLossOfPhysicalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeLossOfPhysicalInput.setStatus("current")


class _ApexAlarmGbeBufferFullness_Type(Integer32):
    """Custom type apexAlarmGbeBufferFullness based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeBufferFullness_Type.__name__ = "Integer32"
_ApexAlarmGbeBufferFullness_Object = MibScalar
apexAlarmGbeBufferFullness = _ApexAlarmGbeBufferFullness_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8021),
    _ApexAlarmGbeBufferFullness_Type()
)
apexAlarmGbeBufferFullness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeBufferFullness.setStatus("current")


class _ApexAlarmGbeInputStreamLowBitRate_Type(Integer32):
    """Custom type apexAlarmGbeInputStreamLowBitRate based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeInputStreamLowBitRate_Type.__name__ = "Integer32"
_ApexAlarmGbeInputStreamLowBitRate_Object = MibScalar
apexAlarmGbeInputStreamLowBitRate = _ApexAlarmGbeInputStreamLowBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8022),
    _ApexAlarmGbeInputStreamLowBitRate_Type()
)
apexAlarmGbeInputStreamLowBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeInputStreamLowBitRate.setStatus("current")


class _ApexAlarmGbeInputStreamHighBitRate_Type(Integer32):
    """Custom type apexAlarmGbeInputStreamHighBitRate based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeInputStreamHighBitRate_Type.__name__ = "Integer32"
_ApexAlarmGbeInputStreamHighBitRate_Object = MibScalar
apexAlarmGbeInputStreamHighBitRate = _ApexAlarmGbeInputStreamHighBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8023),
    _ApexAlarmGbeInputStreamHighBitRate_Type()
)
apexAlarmGbeInputStreamHighBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeInputStreamHighBitRate.setStatus("current")


class _ApexAlarmGbeMptsRedundPrimaryThreshold_Type(Integer32):
    """Custom type apexAlarmGbeMptsRedundPrimaryThreshold based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeMptsRedundPrimaryThreshold_Type.__name__ = "Integer32"
_ApexAlarmGbeMptsRedundPrimaryThreshold_Object = MibScalar
apexAlarmGbeMptsRedundPrimaryThreshold = _ApexAlarmGbeMptsRedundPrimaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8024),
    _ApexAlarmGbeMptsRedundPrimaryThreshold_Type()
)
apexAlarmGbeMptsRedundPrimaryThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeMptsRedundPrimaryThreshold.setStatus("current")


class _ApexAlarmGbeMptsRedundFailOver_Type(Integer32):
    """Custom type apexAlarmGbeMptsRedundFailOver based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeMptsRedundFailOver_Type.__name__ = "Integer32"
_ApexAlarmGbeMptsRedundFailOver_Object = MibScalar
apexAlarmGbeMptsRedundFailOver = _ApexAlarmGbeMptsRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8025),
    _ApexAlarmGbeMptsRedundFailOver_Type()
)
apexAlarmGbeMptsRedundFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeMptsRedundFailOver.setStatus("current")


class _ApexAlarmServiceInError_Type(Integer32):
    """Custom type apexAlarmServiceInError based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmServiceInError_Type.__name__ = "Integer32"
_ApexAlarmServiceInError_Object = MibScalar
apexAlarmServiceInError = _ApexAlarmServiceInError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8026),
    _ApexAlarmServiceInError_Type()
)
apexAlarmServiceInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmServiceInError.setStatus("current")


class _ApexAlarmGbeLossOfInputStream_Type(Integer32):
    """Custom type apexAlarmGbeLossOfInputStream based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeLossOfInputStream_Type.__name__ = "Integer32"
_ApexAlarmGbeLossOfInputStream_Object = MibScalar
apexAlarmGbeLossOfInputStream = _ApexAlarmGbeLossOfInputStream_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8027),
    _ApexAlarmGbeLossOfInputStream_Type()
)
apexAlarmGbeLossOfInputStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeLossOfInputStream.setStatus("current")


class _ApexAlarmGigeToHostCommFault_Type(Integer32):
    """Custom type apexAlarmGigeToHostCommFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGigeToHostCommFault_Type.__name__ = "Integer32"
_ApexAlarmGigeToHostCommFault_Object = MibScalar
apexAlarmGigeToHostCommFault = _ApexAlarmGigeToHostCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8028),
    _ApexAlarmGigeToHostCommFault_Type()
)
apexAlarmGigeToHostCommFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGigeToHostCommFault.setStatus("current")


class _ApexAlarmGbeInterfaceRedundFailOver_Type(Integer32):
    """Custom type apexAlarmGbeInterfaceRedundFailOver based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmGbeInterfaceRedundFailOver_Type.__name__ = "Integer32"
_ApexAlarmGbeInterfaceRedundFailOver_Object = MibScalar
apexAlarmGbeInterfaceRedundFailOver = _ApexAlarmGbeInterfaceRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8029),
    _ApexAlarmGbeInterfaceRedundFailOver_Type()
)
apexAlarmGbeInterfaceRedundFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmGbeInterfaceRedundFailOver.setStatus("current")


class _ApexAlarmOutputUtilizationFault_Type(Integer32):
    """Custom type apexAlarmOutputUtilizationFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmOutputUtilizationFault_Type.__name__ = "Integer32"
_ApexAlarmOutputUtilizationFault_Object = MibScalar
apexAlarmOutputUtilizationFault = _ApexAlarmOutputUtilizationFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8040),
    _ApexAlarmOutputUtilizationFault_Type()
)
apexAlarmOutputUtilizationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmOutputUtilizationFault.setStatus("current")


class _ApexAlarmOutputOverflow_Type(Integer32):
    """Custom type apexAlarmOutputOverflow based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmOutputOverflow_Type.__name__ = "Integer32"
_ApexAlarmOutputOverflow_Object = MibScalar
apexAlarmOutputOverflow = _ApexAlarmOutputOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8041),
    _ApexAlarmOutputOverflow_Type()
)
apexAlarmOutputOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmOutputOverflow.setStatus("current")


class _ApexAlarmQamModuleFault_Type(Integer32):
    """Custom type apexAlarmQamModuleFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmQamModuleFault_Type.__name__ = "Integer32"
_ApexAlarmQamModuleFault_Object = MibScalar
apexAlarmQamModuleFault = _ApexAlarmQamModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8042),
    _ApexAlarmQamModuleFault_Type()
)
apexAlarmQamModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmQamModuleFault.setStatus("current")


class _ApexAlarmQamRfPortFault_Type(Integer32):
    """Custom type apexAlarmQamRfPortFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmQamRfPortFault_Type.__name__ = "Integer32"
_ApexAlarmQamRfPortFault_Object = MibScalar
apexAlarmQamRfPortFault = _ApexAlarmQamRfPortFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8043),
    _ApexAlarmQamRfPortFault_Type()
)
apexAlarmQamRfPortFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmQamRfPortFault.setStatus("current")


class _ApexAlarmQamChannelFault_Type(Integer32):
    """Custom type apexAlarmQamChannelFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmQamChannelFault_Type.__name__ = "Integer32"
_ApexAlarmQamChannelFault_Object = MibScalar
apexAlarmQamChannelFault = _ApexAlarmQamChannelFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8044),
    _ApexAlarmQamChannelFault_Type()
)
apexAlarmQamChannelFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmQamChannelFault.setStatus("current")


class _ApexAlarmQamRfRedundFailOver_Type(Integer32):
    """Custom type apexAlarmQamRfRedundFailOver based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmQamRfRedundFailOver_Type.__name__ = "Integer32"
_ApexAlarmQamRfRedundFailOver_Object = MibScalar
apexAlarmQamRfRedundFailOver = _ApexAlarmQamRfRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8045),
    _ApexAlarmQamRfRedundFailOver_Type()
)
apexAlarmQamRfRedundFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmQamRfRedundFailOver.setStatus("current")


class _ApexAlarmQamRfRedundMismatch_Type(Integer32):
    """Custom type apexAlarmQamRfRedundMismatch based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmQamRfRedundMismatch_Type.__name__ = "Integer32"
_ApexAlarmQamRfRedundMismatch_Object = MibScalar
apexAlarmQamRfRedundMismatch = _ApexAlarmQamRfRedundMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8046),
    _ApexAlarmQamRfRedundMismatch_Type()
)
apexAlarmQamRfRedundMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmQamRfRedundMismatch.setStatus("current")


class _ApexAlarmRtspControllerCommFault_Type(Integer32):
    """Custom type apexAlarmRtspControllerCommFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmRtspControllerCommFault_Type.__name__ = "Integer32"
_ApexAlarmRtspControllerCommFault_Object = MibScalar
apexAlarmRtspControllerCommFault = _ApexAlarmRtspControllerCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8050),
    _ApexAlarmRtspControllerCommFault_Type()
)
apexAlarmRtspControllerCommFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmRtspControllerCommFault.setStatus("current")


class _ApexAlarmRdsCommFault_Type(Integer32):
    """Custom type apexAlarmRdsCommFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmRdsCommFault_Type.__name__ = "Integer32"
_ApexAlarmRdsCommFault_Object = MibScalar
apexAlarmRdsCommFault = _ApexAlarmRdsCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8060),
    _ApexAlarmRdsCommFault_Type()
)
apexAlarmRdsCommFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmRdsCommFault.setStatus("current")


class _ApexAlarmRemCommFault_Type(Integer32):
    """Custom type apexAlarmRemCommFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmRemCommFault_Type.__name__ = "Integer32"
_ApexAlarmRemCommFault_Object = MibScalar
apexAlarmRemCommFault = _ApexAlarmRemCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8070),
    _ApexAlarmRemCommFault_Type()
)
apexAlarmRemCommFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmRemCommFault.setStatus("current")


class _ApexAlarmRemFault_Type(Integer32):
    """Custom type apexAlarmRemFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmRemFault_Type.__name__ = "Integer32"
_ApexAlarmRemFault_Object = MibScalar
apexAlarmRemFault = _ApexAlarmRemFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8071),
    _ApexAlarmRemFault_Type()
)
apexAlarmRemFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmRemFault.setStatus("current")


class _ApexAlarmDepiControlConnectionFault_Type(Integer32):
    """Custom type apexAlarmDepiControlConnectionFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmDepiControlConnectionFault_Type.__name__ = "Integer32"
_ApexAlarmDepiControlConnectionFault_Object = MibScalar
apexAlarmDepiControlConnectionFault = _ApexAlarmDepiControlConnectionFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8080),
    _ApexAlarmDepiControlConnectionFault_Type()
)
apexAlarmDepiControlConnectionFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmDepiControlConnectionFault.setStatus("current")


class _ApexAlarmDepiSessionSetupFault_Type(Integer32):
    """Custom type apexAlarmDepiSessionSetupFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmDepiSessionSetupFault_Type.__name__ = "Integer32"
_ApexAlarmDepiSessionSetupFault_Object = MibScalar
apexAlarmDepiSessionSetupFault = _ApexAlarmDepiSessionSetupFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8081),
    _ApexAlarmDepiSessionSetupFault_Type()
)
apexAlarmDepiSessionSetupFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmDepiSessionSetupFault.setStatus("current")


class _ApexAlarmDtiSyncLossFault_Type(Integer32):
    """Custom type apexAlarmDtiSyncLossFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmDtiSyncLossFault_Type.__name__ = "Integer32"
_ApexAlarmDtiSyncLossFault_Object = MibScalar
apexAlarmDtiSyncLossFault = _ApexAlarmDtiSyncLossFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8082),
    _ApexAlarmDtiSyncLossFault_Type()
)
apexAlarmDtiSyncLossFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmDtiSyncLossFault.setStatus("current")


class _ApexAlarmChassisRedundancyPrimaryFailover_Type(Integer32):
    """Custom type apexAlarmChassisRedundancyPrimaryFailover based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmChassisRedundancyPrimaryFailover_Type.__name__ = "Integer32"
_ApexAlarmChassisRedundancyPrimaryFailover_Object = MibScalar
apexAlarmChassisRedundancyPrimaryFailover = _ApexAlarmChassisRedundancyPrimaryFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8090),
    _ApexAlarmChassisRedundancyPrimaryFailover_Type()
)
apexAlarmChassisRedundancyPrimaryFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmChassisRedundancyPrimaryFailover.setStatus("current")


class _ApexAlarmChassisRedundancySecondaryFailover_Type(Integer32):
    """Custom type apexAlarmChassisRedundancySecondaryFailover based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmChassisRedundancySecondaryFailover_Type.__name__ = "Integer32"
_ApexAlarmChassisRedundancySecondaryFailover_Object = MibScalar
apexAlarmChassisRedundancySecondaryFailover = _ApexAlarmChassisRedundancySecondaryFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8091),
    _ApexAlarmChassisRedundancySecondaryFailover_Type()
)
apexAlarmChassisRedundancySecondaryFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmChassisRedundancySecondaryFailover.setStatus("current")


class _ApexAlarmChassisRedundancyAvailabilityFault_Type(Integer32):
    """Custom type apexAlarmChassisRedundancyAvailabilityFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmChassisRedundancyAvailabilityFault_Type.__name__ = "Integer32"
_ApexAlarmChassisRedundancyAvailabilityFault_Object = MibScalar
apexAlarmChassisRedundancyAvailabilityFault = _ApexAlarmChassisRedundancyAvailabilityFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8092),
    _ApexAlarmChassisRedundancyAvailabilityFault_Type()
)
apexAlarmChassisRedundancyAvailabilityFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmChassisRedundancyAvailabilityFault.setStatus("current")


class _ApexAlarmChassisRedundancyLinkFault_Type(Integer32):
    """Custom type apexAlarmChassisRedundancyLinkFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmChassisRedundancyLinkFault_Type.__name__ = "Integer32"
_ApexAlarmChassisRedundancyLinkFault_Object = MibScalar
apexAlarmChassisRedundancyLinkFault = _ApexAlarmChassisRedundancyLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8093),
    _ApexAlarmChassisRedundancyLinkFault_Type()
)
apexAlarmChassisRedundancyLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmChassisRedundancyLinkFault.setStatus("current")


class _ApexAlarmChassisRedundancyConfigurationFault_Type(Integer32):
    """Custom type apexAlarmChassisRedundancyConfigurationFault based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexAlarmChassisRedundancyConfigurationFault_Type.__name__ = "Integer32"
_ApexAlarmChassisRedundancyConfigurationFault_Object = MibScalar
apexAlarmChassisRedundancyConfigurationFault = _ApexAlarmChassisRedundancyConfigurationFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 100, 8094),
    _ApexAlarmChassisRedundancyConfigurationFault_Type()
)
apexAlarmChassisRedundancyConfigurationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexAlarmChassisRedundancyConfigurationFault.setStatus("current")
_ApexEvents_ObjectIdentity = ObjectIdentity
apexEvents = _ApexEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101)
)
_ApexEventEmUserLoginFailed_Type = Unsigned32
_ApexEventEmUserLoginFailed_Object = MibScalar
apexEventEmUserLoginFailed = _ApexEventEmUserLoginFailed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8100),
    _ApexEventEmUserLoginFailed_Type()
)
apexEventEmUserLoginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventEmUserLoginFailed.setStatus("current")
_ApexEventQamModuleUpgraded_Type = Unsigned32
_ApexEventQamModuleUpgraded_Object = MibScalar
apexEventQamModuleUpgraded = _ApexEventQamModuleUpgraded_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8101),
    _ApexEventQamModuleUpgraded_Type()
)
apexEventQamModuleUpgraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventQamModuleUpgraded.setStatus("current")
_ApexEventChassisRedunPrimaryForceFailover_Type = Unsigned32
_ApexEventChassisRedunPrimaryForceFailover_Object = MibScalar
apexEventChassisRedunPrimaryForceFailover = _ApexEventChassisRedunPrimaryForceFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8110),
    _ApexEventChassisRedunPrimaryForceFailover_Type()
)
apexEventChassisRedunPrimaryForceFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventChassisRedunPrimaryForceFailover.setStatus("obsolete")
_ApexEventChassisRedunSecondaryForceFailover_Type = Unsigned32
_ApexEventChassisRedunSecondaryForceFailover_Object = MibScalar
apexEventChassisRedunSecondaryForceFailover = _ApexEventChassisRedunSecondaryForceFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8111),
    _ApexEventChassisRedunSecondaryForceFailover_Type()
)
apexEventChassisRedunSecondaryForceFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventChassisRedunSecondaryForceFailover.setStatus("obsolete")
_ApexEventChassisRedunFirmwareVersionMismatch_Type = Unsigned32
_ApexEventChassisRedunFirmwareVersionMismatch_Object = MibScalar
apexEventChassisRedunFirmwareVersionMismatch = _ApexEventChassisRedunFirmwareVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8112),
    _ApexEventChassisRedunFirmwareVersionMismatch_Type()
)
apexEventChassisRedunFirmwareVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventChassisRedunFirmwareVersionMismatch.setStatus("current")
_ApexEventChassisRedunQAMVersionMismatch_Type = Unsigned32
_ApexEventChassisRedunQAMVersionMismatch_Object = MibScalar
apexEventChassisRedunQAMVersionMismatch = _ApexEventChassisRedunQAMVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 101, 8113),
    _ApexEventChassisRedunQAMVersionMismatch_Type()
)
apexEventChassisRedunQAMVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexEventChassisRedunQAMVersionMismatch.setStatus("current")
_ApexConfigAlarms_ObjectIdentity = ObjectIdentity
apexConfigAlarms = _ApexConfigAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102)
)
_ApexConfAlarmEnable_ObjectIdentity = ObjectIdentity
apexConfAlarmEnable = _ApexConfAlarmEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1)
)
_ApexEnableInvalidInitData_Type = EnableDisableTYPE
_ApexEnableInvalidInitData_Object = MibScalar
apexEnableInvalidInitData = _ApexEnableInvalidInitData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8001),
    _ApexEnableInvalidInitData_Type()
)
apexEnableInvalidInitData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableInvalidInitData.setStatus("current")
_ApexEnableGbeLossOfPhysicalInput_Type = EnableDisableTYPE
_ApexEnableGbeLossOfPhysicalInput_Object = MibScalar
apexEnableGbeLossOfPhysicalInput = _ApexEnableGbeLossOfPhysicalInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8020),
    _ApexEnableGbeLossOfPhysicalInput_Type()
)
apexEnableGbeLossOfPhysicalInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeLossOfPhysicalInput.setStatus("current")
_ApexEnableGbeBufferFullness_Type = EnableDisableTYPE
_ApexEnableGbeBufferFullness_Object = MibScalar
apexEnableGbeBufferFullness = _ApexEnableGbeBufferFullness_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8021),
    _ApexEnableGbeBufferFullness_Type()
)
apexEnableGbeBufferFullness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeBufferFullness.setStatus("current")
_ApexEnableGbeInputStreamLowBitRate_Type = EnableDisableTYPE
_ApexEnableGbeInputStreamLowBitRate_Object = MibScalar
apexEnableGbeInputStreamLowBitRate = _ApexEnableGbeInputStreamLowBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8022),
    _ApexEnableGbeInputStreamLowBitRate_Type()
)
apexEnableGbeInputStreamLowBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeInputStreamLowBitRate.setStatus("current")
_ApexEnableGbeInputStreamHighBitRate_Type = EnableDisableTYPE
_ApexEnableGbeInputStreamHighBitRate_Object = MibScalar
apexEnableGbeInputStreamHighBitRate = _ApexEnableGbeInputStreamHighBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8023),
    _ApexEnableGbeInputStreamHighBitRate_Type()
)
apexEnableGbeInputStreamHighBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeInputStreamHighBitRate.setStatus("current")
_ApexEnableGbeMptsRedundPrimaryThreshold_Type = EnableDisableTYPE
_ApexEnableGbeMptsRedundPrimaryThreshold_Object = MibScalar
apexEnableGbeMptsRedundPrimaryThreshold = _ApexEnableGbeMptsRedundPrimaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8024),
    _ApexEnableGbeMptsRedundPrimaryThreshold_Type()
)
apexEnableGbeMptsRedundPrimaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeMptsRedundPrimaryThreshold.setStatus("current")
_ApexEnableGbeMptsRedundFailOver_Type = EnableDisableTYPE
_ApexEnableGbeMptsRedundFailOver_Object = MibScalar
apexEnableGbeMptsRedundFailOver = _ApexEnableGbeMptsRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8025),
    _ApexEnableGbeMptsRedundFailOver_Type()
)
apexEnableGbeMptsRedundFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeMptsRedundFailOver.setStatus("current")
_ApexEnableServiceInError_Type = EnableDisableTYPE
_ApexEnableServiceInError_Object = MibScalar
apexEnableServiceInError = _ApexEnableServiceInError_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8026),
    _ApexEnableServiceInError_Type()
)
apexEnableServiceInError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableServiceInError.setStatus("current")
_ApexEnableGbeLossOfInputTsFault_Type = EnableDisableTYPE
_ApexEnableGbeLossOfInputTsFault_Object = MibScalar
apexEnableGbeLossOfInputTsFault = _ApexEnableGbeLossOfInputTsFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8027),
    _ApexEnableGbeLossOfInputTsFault_Type()
)
apexEnableGbeLossOfInputTsFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeLossOfInputTsFault.setStatus("current")
_ApexEnableGbeInterfaceRedundFailOver_Type = EnableDisableTYPE
_ApexEnableGbeInterfaceRedundFailOver_Object = MibScalar
apexEnableGbeInterfaceRedundFailOver = _ApexEnableGbeInterfaceRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8029),
    _ApexEnableGbeInterfaceRedundFailOver_Type()
)
apexEnableGbeInterfaceRedundFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableGbeInterfaceRedundFailOver.setStatus("current")
_ApexEnableOutputUtilizationFault_Type = EnableDisableTYPE
_ApexEnableOutputUtilizationFault_Object = MibScalar
apexEnableOutputUtilizationFault = _ApexEnableOutputUtilizationFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8040),
    _ApexEnableOutputUtilizationFault_Type()
)
apexEnableOutputUtilizationFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableOutputUtilizationFault.setStatus("current")
_ApexEnableOutputOverflow_Type = EnableDisableTYPE
_ApexEnableOutputOverflow_Object = MibScalar
apexEnableOutputOverflow = _ApexEnableOutputOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8041),
    _ApexEnableOutputOverflow_Type()
)
apexEnableOutputOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableOutputOverflow.setStatus("current")
_ApexEnableQamModuleFault_Type = EnableDisableTYPE
_ApexEnableQamModuleFault_Object = MibScalar
apexEnableQamModuleFault = _ApexEnableQamModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8042),
    _ApexEnableQamModuleFault_Type()
)
apexEnableQamModuleFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableQamModuleFault.setStatus("current")
_ApexEnableQamRfPortFault_Type = EnableDisableTYPE
_ApexEnableQamRfPortFault_Object = MibScalar
apexEnableQamRfPortFault = _ApexEnableQamRfPortFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8043),
    _ApexEnableQamRfPortFault_Type()
)
apexEnableQamRfPortFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableQamRfPortFault.setStatus("current")
_ApexEnableQamChannelFault_Type = EnableDisableTYPE
_ApexEnableQamChannelFault_Object = MibScalar
apexEnableQamChannelFault = _ApexEnableQamChannelFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8044),
    _ApexEnableQamChannelFault_Type()
)
apexEnableQamChannelFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableQamChannelFault.setStatus("current")
_ApexEnableQamRfRedundFailOver_Type = EnableDisableTYPE
_ApexEnableQamRfRedundFailOver_Object = MibScalar
apexEnableQamRfRedundFailOver = _ApexEnableQamRfRedundFailOver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8045),
    _ApexEnableQamRfRedundFailOver_Type()
)
apexEnableQamRfRedundFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableQamRfRedundFailOver.setStatus("current")
_ApexEnableQamRfRedundMismatch_Type = EnableDisableTYPE
_ApexEnableQamRfRedundMismatch_Object = MibScalar
apexEnableQamRfRedundMismatch = _ApexEnableQamRfRedundMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8046),
    _ApexEnableQamRfRedundMismatch_Type()
)
apexEnableQamRfRedundMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableQamRfRedundMismatch.setStatus("current")
_ApexEnableRtspControllerCommFault_Type = EnableDisableTYPE
_ApexEnableRtspControllerCommFault_Object = MibScalar
apexEnableRtspControllerCommFault = _ApexEnableRtspControllerCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8050),
    _ApexEnableRtspControllerCommFault_Type()
)
apexEnableRtspControllerCommFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableRtspControllerCommFault.setStatus("current")
_ApexEnableRdsCommAlarmFault_Type = EnableDisableTYPE
_ApexEnableRdsCommAlarmFault_Object = MibScalar
apexEnableRdsCommAlarmFault = _ApexEnableRdsCommAlarmFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8060),
    _ApexEnableRdsCommAlarmFault_Type()
)
apexEnableRdsCommAlarmFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableRdsCommAlarmFault.setStatus("current")
_ApexEnableRemCommFault_Type = EnableDisableTYPE
_ApexEnableRemCommFault_Object = MibScalar
apexEnableRemCommFault = _ApexEnableRemCommFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8070),
    _ApexEnableRemCommFault_Type()
)
apexEnableRemCommFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableRemCommFault.setStatus("current")
_ApexEnableRemFault_Type = EnableDisableTYPE
_ApexEnableRemFault_Object = MibScalar
apexEnableRemFault = _ApexEnableRemFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8071),
    _ApexEnableRemFault_Type()
)
apexEnableRemFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableRemFault.setStatus("current")
_ApexEnableDepiControlConnectionFault_Type = EnableDisableTYPE
_ApexEnableDepiControlConnectionFault_Object = MibScalar
apexEnableDepiControlConnectionFault = _ApexEnableDepiControlConnectionFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8080),
    _ApexEnableDepiControlConnectionFault_Type()
)
apexEnableDepiControlConnectionFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableDepiControlConnectionFault.setStatus("current")
_ApexEnableDepiSessionSetupFault_Type = EnableDisableTYPE
_ApexEnableDepiSessionSetupFault_Object = MibScalar
apexEnableDepiSessionSetupFault = _ApexEnableDepiSessionSetupFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8081),
    _ApexEnableDepiSessionSetupFault_Type()
)
apexEnableDepiSessionSetupFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableDepiSessionSetupFault.setStatus("current")
_ApexEnableDtiSyncLossFault_Type = EnableDisableTYPE
_ApexEnableDtiSyncLossFault_Object = MibScalar
apexEnableDtiSyncLossFault = _ApexEnableDtiSyncLossFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8082),
    _ApexEnableDtiSyncLossFault_Type()
)
apexEnableDtiSyncLossFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableDtiSyncLossFault.setStatus("current")
_ApexEnableChassisRedundancyPrimaryFailover_Type = EnableDisableTYPE
_ApexEnableChassisRedundancyPrimaryFailover_Object = MibScalar
apexEnableChassisRedundancyPrimaryFailover = _ApexEnableChassisRedundancyPrimaryFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8090),
    _ApexEnableChassisRedundancyPrimaryFailover_Type()
)
apexEnableChassisRedundancyPrimaryFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableChassisRedundancyPrimaryFailover.setStatus("current")
_ApexEnableChassisRedundancySecondaryFailover_Type = EnableDisableTYPE
_ApexEnableChassisRedundancySecondaryFailover_Object = MibScalar
apexEnableChassisRedundancySecondaryFailover = _ApexEnableChassisRedundancySecondaryFailover_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8091),
    _ApexEnableChassisRedundancySecondaryFailover_Type()
)
apexEnableChassisRedundancySecondaryFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableChassisRedundancySecondaryFailover.setStatus("current")
_ApexEnableChassisRedundancyAvailabilityFault_Type = EnableDisableTYPE
_ApexEnableChassisRedundancyAvailabilityFault_Object = MibScalar
apexEnableChassisRedundancyAvailabilityFault = _ApexEnableChassisRedundancyAvailabilityFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8092),
    _ApexEnableChassisRedundancyAvailabilityFault_Type()
)
apexEnableChassisRedundancyAvailabilityFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableChassisRedundancyAvailabilityFault.setStatus("current")
_ApexEnableChassisRedundancyLinkFault_Type = EnableDisableTYPE
_ApexEnableChassisRedundancyLinkFault_Object = MibScalar
apexEnableChassisRedundancyLinkFault = _ApexEnableChassisRedundancyLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8093),
    _ApexEnableChassisRedundancyLinkFault_Type()
)
apexEnableChassisRedundancyLinkFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableChassisRedundancyLinkFault.setStatus("current")
_ApexEnableChassisRedundancyConfigurationFault_Type = EnableDisableTYPE
_ApexEnableChassisRedundancyConfigurationFault_Object = MibScalar
apexEnableChassisRedundancyConfigurationFault = _ApexEnableChassisRedundancyConfigurationFault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 1, 8094),
    _ApexEnableChassisRedundancyConfigurationFault_Type()
)
apexEnableChassisRedundancyConfigurationFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexEnableChassisRedundancyConfigurationFault.setStatus("current")
_ApexConfAlarmClear_ObjectIdentity = ObjectIdentity
apexConfAlarmClear = _ApexConfAlarmClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 2)
)
_ApexClearInvalidInitData_Type = ClearAlarmTYPE
_ApexClearInvalidInitData_Object = MibScalar
apexClearInvalidInitData = _ApexClearInvalidInitData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 102, 2, 8001),
    _ApexClearInvalidInitData_Type()
)
apexClearInvalidInitData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apexClearInvalidInitData.setStatus("current")
_ApexLogs_ObjectIdentity = ObjectIdentity
apexLogs = _ApexLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200)
)
_ApexHwEventTable_Object = MibTable
apexHwEventTable = _ApexHwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1)
)
if mibBuilder.loadTexts:
    apexHwEventTable.setStatus("current")
_ApexHwEventEntry_Object = MibTableRow
apexHwEventEntry = _ApexHwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1)
)
apexHwEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexHwEventIndex"),
)
if mibBuilder.loadTexts:
    apexHwEventEntry.setStatus("current")


class _ApexHwEventIndex_Type(Integer32):
    """Custom type apexHwEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexHwEventIndex_Type.__name__ = "Integer32"
_ApexHwEventIndex_Object = MibTableColumn
apexHwEventIndex = _ApexHwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 1),
    _ApexHwEventIndex_Type()
)
apexHwEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexHwEventIndex.setStatus("current")
_ApexHwEventTimeLogged_Type = Integer32
_ApexHwEventTimeLogged_Object = MibTableColumn
apexHwEventTimeLogged = _ApexHwEventTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 2),
    _ApexHwEventTimeLogged_Type()
)
apexHwEventTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHwEventTimeLogged.setStatus("current")
_ApexHwEventAlarmCode_Type = Integer32
_ApexHwEventAlarmCode_Object = MibTableColumn
apexHwEventAlarmCode = _ApexHwEventAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 3),
    _ApexHwEventAlarmCode_Type()
)
apexHwEventAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHwEventAlarmCode.setStatus("current")


class _ApexHwEventAlarmSeverity_Type(Integer32):
    """Custom type apexHwEventAlarmSeverity based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexHwEventAlarmSeverity_Type.__name__ = "Integer32"
_ApexHwEventAlarmSeverity_Object = MibTableColumn
apexHwEventAlarmSeverity = _ApexHwEventAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 4),
    _ApexHwEventAlarmSeverity_Type()
)
apexHwEventAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHwEventAlarmSeverity.setStatus("current")
_ApexHwEventData_Type = Integer32
_ApexHwEventData_Object = MibTableColumn
apexHwEventData = _ApexHwEventData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 5),
    _ApexHwEventData_Type()
)
apexHwEventData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHwEventData.setStatus("current")
_ApexHwEventDescription_Type = DisplayString
_ApexHwEventDescription_Object = MibTableColumn
apexHwEventDescription = _ApexHwEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 1, 1, 6),
    _ApexHwEventDescription_Type()
)
apexHwEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexHwEventDescription.setStatus("current")
_ApexInvalidInitDataTable_Object = MibTable
apexInvalidInitDataTable = _ApexInvalidInitDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 2)
)
if mibBuilder.loadTexts:
    apexInvalidInitDataTable.setStatus("current")
_ApexInvalidInitDataEntry_Object = MibTableRow
apexInvalidInitDataEntry = _ApexInvalidInitDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 2, 1)
)
apexInvalidInitDataEntry.setIndexNames(
    (0, "APEX-MIB", "apexInvalidInitDataIndex"),
)
if mibBuilder.loadTexts:
    apexInvalidInitDataEntry.setStatus("current")


class _ApexInvalidInitDataIndex_Type(Integer32):
    """Custom type apexInvalidInitDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexInvalidInitDataIndex_Type.__name__ = "Integer32"
_ApexInvalidInitDataIndex_Object = MibTableColumn
apexInvalidInitDataIndex = _ApexInvalidInitDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 2, 1, 1),
    _ApexInvalidInitDataIndex_Type()
)
apexInvalidInitDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexInvalidInitDataIndex.setStatus("current")
_ApexInvalidInitDataTimeLogged_Type = Integer32
_ApexInvalidInitDataTimeLogged_Object = MibTableColumn
apexInvalidInitDataTimeLogged = _ApexInvalidInitDataTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 2, 1, 2),
    _ApexInvalidInitDataTimeLogged_Type()
)
apexInvalidInitDataTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInvalidInitDataTimeLogged.setStatus("current")
_ApexInvalidInitDataDescription_Type = DisplayString
_ApexInvalidInitDataDescription_Object = MibTableColumn
apexInvalidInitDataDescription = _ApexInvalidInitDataDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 2, 1, 3),
    _ApexInvalidInitDataDescription_Type()
)
apexInvalidInitDataDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexInvalidInitDataDescription.setStatus("current")
_ApexOutputTsEventTable_Object = MibTable
apexOutputTsEventTable = _ApexOutputTsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3)
)
if mibBuilder.loadTexts:
    apexOutputTsEventTable.setStatus("current")
_ApexOutputTsEventEntry_Object = MibTableRow
apexOutputTsEventEntry = _ApexOutputTsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1)
)
apexOutputTsEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexOutputTsEventIndex"),
)
if mibBuilder.loadTexts:
    apexOutputTsEventEntry.setStatus("current")


class _ApexOutputTsEventIndex_Type(Integer32):
    """Custom type apexOutputTsEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexOutputTsEventIndex_Type.__name__ = "Integer32"
_ApexOutputTsEventIndex_Object = MibTableColumn
apexOutputTsEventIndex = _ApexOutputTsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 1),
    _ApexOutputTsEventIndex_Type()
)
apexOutputTsEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexOutputTsEventIndex.setStatus("current")
_ApexOutputTsEventTimeLogged_Type = Integer32
_ApexOutputTsEventTimeLogged_Object = MibTableColumn
apexOutputTsEventTimeLogged = _ApexOutputTsEventTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 2),
    _ApexOutputTsEventTimeLogged_Type()
)
apexOutputTsEventTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventTimeLogged.setStatus("current")
_ApexOutputTsEventAlarmCode_Type = Integer32
_ApexOutputTsEventAlarmCode_Object = MibTableColumn
apexOutputTsEventAlarmCode = _ApexOutputTsEventAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 3),
    _ApexOutputTsEventAlarmCode_Type()
)
apexOutputTsEventAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventAlarmCode.setStatus("current")


class _ApexOutputTsEventAlarmSeverity_Type(Integer32):
    """Custom type apexOutputTsEventAlarmSeverity based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexOutputTsEventAlarmSeverity_Type.__name__ = "Integer32"
_ApexOutputTsEventAlarmSeverity_Object = MibTableColumn
apexOutputTsEventAlarmSeverity = _ApexOutputTsEventAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 4),
    _ApexOutputTsEventAlarmSeverity_Type()
)
apexOutputTsEventAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventAlarmSeverity.setStatus("current")


class _ApexOutputTsEventOutputTsNum_Type(Integer32):
    """Custom type apexOutputTsEventOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexOutputTsEventOutputTsNum_Type.__name__ = "Integer32"
_ApexOutputTsEventOutputTsNum_Object = MibTableColumn
apexOutputTsEventOutputTsNum = _ApexOutputTsEventOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 5),
    _ApexOutputTsEventOutputTsNum_Type()
)
apexOutputTsEventOutputTsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventOutputTsNum.setStatus("current")
_ApexOutputTsEventCurRate_Type = Integer32
_ApexOutputTsEventCurRate_Object = MibTableColumn
apexOutputTsEventCurRate = _ApexOutputTsEventCurRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 6),
    _ApexOutputTsEventCurRate_Type()
)
apexOutputTsEventCurRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventCurRate.setStatus("current")
_ApexOutputTsEventAvgRate_Type = Integer32
_ApexOutputTsEventAvgRate_Object = MibTableColumn
apexOutputTsEventAvgRate = _ApexOutputTsEventAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 7),
    _ApexOutputTsEventAvgRate_Type()
)
apexOutputTsEventAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventAvgRate.setStatus("current")
_ApexOutputTsEventMinRate_Type = Integer32
_ApexOutputTsEventMinRate_Object = MibTableColumn
apexOutputTsEventMinRate = _ApexOutputTsEventMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 8),
    _ApexOutputTsEventMinRate_Type()
)
apexOutputTsEventMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventMinRate.setStatus("current")
_ApexOutputTsEventPeakRate_Type = Integer32
_ApexOutputTsEventPeakRate_Object = MibTableColumn
apexOutputTsEventPeakRate = _ApexOutputTsEventPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 9),
    _ApexOutputTsEventPeakRate_Type()
)
apexOutputTsEventPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventPeakRate.setStatus("current")
_ApexOutputTsEventCurDropPackets_Type = Integer32
_ApexOutputTsEventCurDropPackets_Object = MibTableColumn
apexOutputTsEventCurDropPackets = _ApexOutputTsEventCurDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 10),
    _ApexOutputTsEventCurDropPackets_Type()
)
apexOutputTsEventCurDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventCurDropPackets.setStatus("current")
_ApexOutputTsEventPeakDropPackets_Type = Integer32
_ApexOutputTsEventPeakDropPackets_Object = MibTableColumn
apexOutputTsEventPeakDropPackets = _ApexOutputTsEventPeakDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 11),
    _ApexOutputTsEventPeakDropPackets_Type()
)
apexOutputTsEventPeakDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventPeakDropPackets.setStatus("current")
_ApexOutputTsEventRollingDropPackets_Type = Integer32
_ApexOutputTsEventRollingDropPackets_Object = MibTableColumn
apexOutputTsEventRollingDropPackets = _ApexOutputTsEventRollingDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 12),
    _ApexOutputTsEventRollingDropPackets_Type()
)
apexOutputTsEventRollingDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventRollingDropPackets.setStatus("current")
_ApexOutputTsEventTotalDropPackets_Type = Integer32
_ApexOutputTsEventTotalDropPackets_Object = MibTableColumn
apexOutputTsEventTotalDropPackets = _ApexOutputTsEventTotalDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 13),
    _ApexOutputTsEventTotalDropPackets_Type()
)
apexOutputTsEventTotalDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventTotalDropPackets.setStatus("current")
_ApexOutputTsEventDescription_Type = DisplayString
_ApexOutputTsEventDescription_Object = MibTableColumn
apexOutputTsEventDescription = _ApexOutputTsEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 3, 1, 14),
    _ApexOutputTsEventDescription_Type()
)
apexOutputTsEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexOutputTsEventDescription.setStatus("current")
_ApexGbeInputTsEventTable_Object = MibTable
apexGbeInputTsEventTable = _ApexGbeInputTsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4)
)
if mibBuilder.loadTexts:
    apexGbeInputTsEventTable.setStatus("current")
_ApexGbeInputTsEventEntry_Object = MibTableRow
apexGbeInputTsEventEntry = _ApexGbeInputTsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1)
)
apexGbeInputTsEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexGbeInputTsEventIndex"),
)
if mibBuilder.loadTexts:
    apexGbeInputTsEventEntry.setStatus("current")


class _ApexGbeInputTsEventIndex_Type(Integer32):
    """Custom type apexGbeInputTsEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexGbeInputTsEventIndex_Type.__name__ = "Integer32"
_ApexGbeInputTsEventIndex_Object = MibTableColumn
apexGbeInputTsEventIndex = _ApexGbeInputTsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 1),
    _ApexGbeInputTsEventIndex_Type()
)
apexGbeInputTsEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexGbeInputTsEventIndex.setStatus("current")
_ApexGbeInputTsEventTimeLogged_Type = Integer32
_ApexGbeInputTsEventTimeLogged_Object = MibTableColumn
apexGbeInputTsEventTimeLogged = _ApexGbeInputTsEventTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 2),
    _ApexGbeInputTsEventTimeLogged_Type()
)
apexGbeInputTsEventTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventTimeLogged.setStatus("current")
_ApexGbeInputTsEventAlarmCode_Type = Integer32
_ApexGbeInputTsEventAlarmCode_Object = MibTableColumn
apexGbeInputTsEventAlarmCode = _ApexGbeInputTsEventAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 3),
    _ApexGbeInputTsEventAlarmCode_Type()
)
apexGbeInputTsEventAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventAlarmCode.setStatus("current")


class _ApexGbeInputTsEventAlarmSeverity_Type(Integer32):
    """Custom type apexGbeInputTsEventAlarmSeverity based on Integer32"""
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
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("warning", 3))
    )


_ApexGbeInputTsEventAlarmSeverity_Type.__name__ = "Integer32"
_ApexGbeInputTsEventAlarmSeverity_Object = MibTableColumn
apexGbeInputTsEventAlarmSeverity = _ApexGbeInputTsEventAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 4),
    _ApexGbeInputTsEventAlarmSeverity_Type()
)
apexGbeInputTsEventAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventAlarmSeverity.setStatus("current")


class _ApexGbeInputTsEventRedundantConfig_Type(Integer32):
    """Custom type apexGbeInputTsEventRedundantConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_ApexGbeInputTsEventRedundantConfig_Type.__name__ = "Integer32"
_ApexGbeInputTsEventRedundantConfig_Object = MibTableColumn
apexGbeInputTsEventRedundantConfig = _ApexGbeInputTsEventRedundantConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 5),
    _ApexGbeInputTsEventRedundantConfig_Type()
)
apexGbeInputTsEventRedundantConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventRedundantConfig.setStatus("current")
_ApexGbeInputTsEventGbeInterface_Type = Integer32
_ApexGbeInputTsEventGbeInterface_Object = MibTableColumn
apexGbeInputTsEventGbeInterface = _ApexGbeInputTsEventGbeInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 6),
    _ApexGbeInputTsEventGbeInterface_Type()
)
apexGbeInputTsEventGbeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventGbeInterface.setStatus("current")
_ApexGbeInputTsEventUdpPort_Type = Integer32
_ApexGbeInputTsEventUdpPort_Object = MibTableColumn
apexGbeInputTsEventUdpPort = _ApexGbeInputTsEventUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 7),
    _ApexGbeInputTsEventUdpPort_Type()
)
apexGbeInputTsEventUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventUdpPort.setStatus("current")
_ApexGbeInputTsEventMulticastIp_Type = IpAddress
_ApexGbeInputTsEventMulticastIp_Object = MibTableColumn
apexGbeInputTsEventMulticastIp = _ApexGbeInputTsEventMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 8),
    _ApexGbeInputTsEventMulticastIp_Type()
)
apexGbeInputTsEventMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventMulticastIp.setStatus("current")
_ApexGbeInputTsEventSourceIp_Type = IpAddress
_ApexGbeInputTsEventSourceIp_Object = MibTableColumn
apexGbeInputTsEventSourceIp = _ApexGbeInputTsEventSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 9),
    _ApexGbeInputTsEventSourceIp_Type()
)
apexGbeInputTsEventSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventSourceIp.setStatus("current")
_ApexGbeInputTsEventInputTsState_Type = InputTsStateTYPE
_ApexGbeInputTsEventInputTsState_Object = MibTableColumn
apexGbeInputTsEventInputTsState = _ApexGbeInputTsEventInputTsState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 10),
    _ApexGbeInputTsEventInputTsState_Type()
)
apexGbeInputTsEventInputTsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventInputTsState.setStatus("current")
_ApexGbeInputTsEventRateCompareType_Type = RateComparisonTYPE
_ApexGbeInputTsEventRateCompareType_Object = MibTableColumn
apexGbeInputTsEventRateCompareType = _ApexGbeInputTsEventRateCompareType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 11),
    _ApexGbeInputTsEventRateCompareType_Type()
)
apexGbeInputTsEventRateCompareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventRateCompareType.setStatus("current")
_ApexGbeInputTsEventSamplingPeriod_Type = Integer32
_ApexGbeInputTsEventSamplingPeriod_Object = MibTableColumn
apexGbeInputTsEventSamplingPeriod = _ApexGbeInputTsEventSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 12),
    _ApexGbeInputTsEventSamplingPeriod_Type()
)
apexGbeInputTsEventSamplingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventSamplingPeriod.setStatus("current")
_ApexGbeInputTsEventPriCurStreamCount_Type = Counter32
_ApexGbeInputTsEventPriCurStreamCount_Object = MibTableColumn
apexGbeInputTsEventPriCurStreamCount = _ApexGbeInputTsEventPriCurStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 13),
    _ApexGbeInputTsEventPriCurStreamCount_Type()
)
apexGbeInputTsEventPriCurStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventPriCurStreamCount.setStatus("current")
_ApexGbeInputTsEventPriCurDataCount_Type = Counter32
_ApexGbeInputTsEventPriCurDataCount_Object = MibTableColumn
apexGbeInputTsEventPriCurDataCount = _ApexGbeInputTsEventPriCurDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 14),
    _ApexGbeInputTsEventPriCurDataCount_Type()
)
apexGbeInputTsEventPriCurDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventPriCurDataCount.setStatus("current")
_ApexGbeInputTsEventSecCurStreamCount_Type = Counter32
_ApexGbeInputTsEventSecCurStreamCount_Object = MibTableColumn
apexGbeInputTsEventSecCurStreamCount = _ApexGbeInputTsEventSecCurStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 15),
    _ApexGbeInputTsEventSecCurStreamCount_Type()
)
apexGbeInputTsEventSecCurStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventSecCurStreamCount.setStatus("current")
_ApexGbeInputTsEventSecCurDataCount_Type = Counter32
_ApexGbeInputTsEventSecCurDataCount_Object = MibTableColumn
apexGbeInputTsEventSecCurDataCount = _ApexGbeInputTsEventSecCurDataCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 16),
    _ApexGbeInputTsEventSecCurDataCount_Type()
)
apexGbeInputTsEventSecCurDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventSecCurDataCount.setStatus("current")
_ApexGbeInputTsEventDescription_Type = DisplayString
_ApexGbeInputTsEventDescription_Object = MibTableColumn
apexGbeInputTsEventDescription = _ApexGbeInputTsEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 4, 1, 17),
    _ApexGbeInputTsEventDescription_Type()
)
apexGbeInputTsEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexGbeInputTsEventDescription.setStatus("current")
_ApexRtspEventTable_Object = MibTable
apexRtspEventTable = _ApexRtspEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5)
)
if mibBuilder.loadTexts:
    apexRtspEventTable.setStatus("current")
_ApexRtspEventEntry_Object = MibTableRow
apexRtspEventEntry = _ApexRtspEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1)
)
apexRtspEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexRtspEventIndex"),
)
if mibBuilder.loadTexts:
    apexRtspEventEntry.setStatus("current")


class _ApexRtspEventIndex_Type(Integer32):
    """Custom type apexRtspEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexRtspEventIndex_Type.__name__ = "Integer32"
_ApexRtspEventIndex_Object = MibTableColumn
apexRtspEventIndex = _ApexRtspEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 1),
    _ApexRtspEventIndex_Type()
)
apexRtspEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexRtspEventIndex.setStatus("current")
_ApexRtspEventTimeLogged_Type = Integer32
_ApexRtspEventTimeLogged_Object = MibTableColumn
apexRtspEventTimeLogged = _ApexRtspEventTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 2),
    _ApexRtspEventTimeLogged_Type()
)
apexRtspEventTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspEventTimeLogged.setStatus("current")
_ApexRtspEventControllerIp_Type = IpAddress
_ApexRtspEventControllerIp_Object = MibTableColumn
apexRtspEventControllerIp = _ApexRtspEventControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 3),
    _ApexRtspEventControllerIp_Type()
)
apexRtspEventControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspEventControllerIp.setStatus("current")
_ApexRtspEventSessionCount_Type = Integer32
_ApexRtspEventSessionCount_Object = MibTableColumn
apexRtspEventSessionCount = _ApexRtspEventSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 4),
    _ApexRtspEventSessionCount_Type()
)
apexRtspEventSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspEventSessionCount.setStatus("current")
_ApexRtspEventSourceDescription_Type = DisplayString
_ApexRtspEventSourceDescription_Object = MibTableColumn
apexRtspEventSourceDescription = _ApexRtspEventSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 5),
    _ApexRtspEventSourceDescription_Type()
)
apexRtspEventSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspEventSourceDescription.setStatus("current")
_ApexRtspEventDescription_Type = DisplayString
_ApexRtspEventDescription_Object = MibTableColumn
apexRtspEventDescription = _ApexRtspEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 5, 1, 6),
    _ApexRtspEventDescription_Type()
)
apexRtspEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexRtspEventDescription.setStatus("current")
_ApexMappingErrorTable_Object = MibTable
apexMappingErrorTable = _ApexMappingErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6)
)
if mibBuilder.loadTexts:
    apexMappingErrorTable.setStatus("current")
_ApexMappingErrorEntry_Object = MibTableRow
apexMappingErrorEntry = _ApexMappingErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1)
)
apexMappingErrorEntry.setIndexNames(
    (0, "APEX-MIB", "apexMappingErrorIndex"),
)
if mibBuilder.loadTexts:
    apexMappingErrorEntry.setStatus("current")


class _ApexMappingErrorIndex_Type(Integer32):
    """Custom type apexMappingErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexMappingErrorIndex_Type.__name__ = "Integer32"
_ApexMappingErrorIndex_Object = MibTableColumn
apexMappingErrorIndex = _ApexMappingErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 1),
    _ApexMappingErrorIndex_Type()
)
apexMappingErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexMappingErrorIndex.setStatus("current")
_ApexMappingErrorTimeLogged_Type = Integer32
_ApexMappingErrorTimeLogged_Object = MibTableColumn
apexMappingErrorTimeLogged = _ApexMappingErrorTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 2),
    _ApexMappingErrorTimeLogged_Type()
)
apexMappingErrorTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorTimeLogged.setStatus("current")
_ApexMappingErrorCode_Type = Integer32
_ApexMappingErrorCode_Object = MibTableColumn
apexMappingErrorCode = _ApexMappingErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 3),
    _ApexMappingErrorCode_Type()
)
apexMappingErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorCode.setStatus("current")


class _ApexMappingErrorMappingType_Type(Integer32):
    """Custom type apexMappingErrorMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ancillaryPid", 2),
          ("depiControl", 4),
          ("depiSession", 5),
          ("notApplicable", 0),
          ("program", 1),
          ("streamPassthru", 3))
    )


_ApexMappingErrorMappingType_Type.__name__ = "Integer32"
_ApexMappingErrorMappingType_Object = MibTableColumn
apexMappingErrorMappingType = _ApexMappingErrorMappingType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 4),
    _ApexMappingErrorMappingType_Type()
)
apexMappingErrorMappingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorMappingType.setStatus("current")


class _ApexMappingErrorInputType_Type(Integer32):
    """Custom type apexMappingErrorInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEnet", 2),
          ("gbe", 1),
          ("notApplicable", 0))
    )


_ApexMappingErrorInputType_Type.__name__ = "Integer32"
_ApexMappingErrorInputType_Object = MibTableColumn
apexMappingErrorInputType = _ApexMappingErrorInputType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 5),
    _ApexMappingErrorInputType_Type()
)
apexMappingErrorInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorInputType.setStatus("current")
_ApexMappingErrorInputInterface_Type = Integer32
_ApexMappingErrorInputInterface_Object = MibTableColumn
apexMappingErrorInputInterface = _ApexMappingErrorInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 6),
    _ApexMappingErrorInputInterface_Type()
)
apexMappingErrorInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorInputInterface.setStatus("current")
_ApexMappingErrorUdpPort_Type = Integer32
_ApexMappingErrorUdpPort_Object = MibTableColumn
apexMappingErrorUdpPort = _ApexMappingErrorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 7),
    _ApexMappingErrorUdpPort_Type()
)
apexMappingErrorUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorUdpPort.setStatus("current")
_ApexMappingErrorMulticastIp_Type = IpAddress
_ApexMappingErrorMulticastIp_Object = MibTableColumn
apexMappingErrorMulticastIp = _ApexMappingErrorMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 8),
    _ApexMappingErrorMulticastIp_Type()
)
apexMappingErrorMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorMulticastIp.setStatus("current")
_ApexMappingErrorSourceIp_Type = IpAddress
_ApexMappingErrorSourceIp_Object = MibTableColumn
apexMappingErrorSourceIp = _ApexMappingErrorSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 9),
    _ApexMappingErrorSourceIp_Type()
)
apexMappingErrorSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorSourceIp.setStatus("current")
_ApexMappingErrorInputProgramPid_Type = Integer32
_ApexMappingErrorInputProgramPid_Object = MibTableColumn
apexMappingErrorInputProgramPid = _ApexMappingErrorInputProgramPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 10),
    _ApexMappingErrorInputProgramPid_Type()
)
apexMappingErrorInputProgramPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorInputProgramPid.setStatus("current")
_ApexMappingErrorOutputProgramPid_Type = Integer32
_ApexMappingErrorOutputProgramPid_Object = MibTableColumn
apexMappingErrorOutputProgramPid = _ApexMappingErrorOutputProgramPid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 11),
    _ApexMappingErrorOutputProgramPid_Type()
)
apexMappingErrorOutputProgramPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorOutputProgramPid.setStatus("current")


class _ApexMappingErrorOutputOpMode_Type(Integer32):
    """Custom type apexMappingErrorOutputOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualRouting", 2),
          ("notInUse", 0),
          ("sessionControl", 1))
    )


_ApexMappingErrorOutputOpMode_Type.__name__ = "Integer32"
_ApexMappingErrorOutputOpMode_Object = MibTableColumn
apexMappingErrorOutputOpMode = _ApexMappingErrorOutputOpMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 12),
    _ApexMappingErrorOutputOpMode_Type()
)
apexMappingErrorOutputOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorOutputOpMode.setStatus("current")


class _ApexMappingErrorOutputTsNum_Type(Integer32):
    """Custom type apexMappingErrorOutputTsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ApexMappingErrorOutputTsNum_Type.__name__ = "Integer32"
_ApexMappingErrorOutputTsNum_Object = MibTableColumn
apexMappingErrorOutputTsNum = _ApexMappingErrorOutputTsNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 13),
    _ApexMappingErrorOutputTsNum_Type()
)
apexMappingErrorOutputTsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorOutputTsNum.setStatus("current")
_ApexMappingErrorSecInputInterface_Type = Integer32
_ApexMappingErrorSecInputInterface_Object = MibTableColumn
apexMappingErrorSecInputInterface = _ApexMappingErrorSecInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 14),
    _ApexMappingErrorSecInputInterface_Type()
)
apexMappingErrorSecInputInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorSecInputInterface.setStatus("current")
_ApexMappingErrorSecUdpPort_Type = Integer32
_ApexMappingErrorSecUdpPort_Object = MibTableColumn
apexMappingErrorSecUdpPort = _ApexMappingErrorSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 15),
    _ApexMappingErrorSecUdpPort_Type()
)
apexMappingErrorSecUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorSecUdpPort.setStatus("current")
_ApexMappingErrorSecMulticastIp_Type = IpAddress
_ApexMappingErrorSecMulticastIp_Object = MibTableColumn
apexMappingErrorSecMulticastIp = _ApexMappingErrorSecMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 16),
    _ApexMappingErrorSecMulticastIp_Type()
)
apexMappingErrorSecMulticastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorSecMulticastIp.setStatus("current")
_ApexMappingErrorSecSourceIp_Type = IpAddress
_ApexMappingErrorSecSourceIp_Object = MibTableColumn
apexMappingErrorSecSourceIp = _ApexMappingErrorSecSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 6, 1, 17),
    _ApexMappingErrorSecSourceIp_Type()
)
apexMappingErrorSecSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexMappingErrorSecSourceIp.setStatus("current")
_ApexChassisRedundancyEventTable_Object = MibTable
apexChassisRedundancyEventTable = _ApexChassisRedundancyEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 7)
)
if mibBuilder.loadTexts:
    apexChassisRedundancyEventTable.setStatus("current")
_ApexChassisRedundancyEventEntry_Object = MibTableRow
apexChassisRedundancyEventEntry = _ApexChassisRedundancyEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 7, 1)
)
apexChassisRedundancyEventEntry.setIndexNames(
    (0, "APEX-MIB", "apexChassisRedundancyEventIndex"),
)
if mibBuilder.loadTexts:
    apexChassisRedundancyEventEntry.setStatus("current")


class _ApexChassisRedundancyEventIndex_Type(Integer32):
    """Custom type apexChassisRedundancyEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApexChassisRedundancyEventIndex_Type.__name__ = "Integer32"
_ApexChassisRedundancyEventIndex_Object = MibTableColumn
apexChassisRedundancyEventIndex = _ApexChassisRedundancyEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 7, 1, 1),
    _ApexChassisRedundancyEventIndex_Type()
)
apexChassisRedundancyEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apexChassisRedundancyEventIndex.setStatus("current")
_ApexChassisRedundancyEventTimeLogged_Type = Integer32
_ApexChassisRedundancyEventTimeLogged_Object = MibTableColumn
apexChassisRedundancyEventTimeLogged = _ApexChassisRedundancyEventTimeLogged_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 7, 1, 2),
    _ApexChassisRedundancyEventTimeLogged_Type()
)
apexChassisRedundancyEventTimeLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyEventTimeLogged.setStatus("current")
_ApexChassisRedundancyEventDescription_Type = DisplayString
_ApexChassisRedundancyEventDescription_Object = MibTableColumn
apexChassisRedundancyEventDescription = _ApexChassisRedundancyEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 200, 7, 1, 3),
    _ApexChassisRedundancyEventDescription_Type()
)
apexChassisRedundancyEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apexChassisRedundancyEventDescription.setStatus("current")
_ApexDebug_ObjectIdentity = ObjectIdentity
apexDebug = _ApexDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 5000)
)

# Managed Objects groups


# Notification objects

trapConfigurationChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 3)
)
trapConfigurationChangeInteger.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"))
)
if mibBuilder.loadTexts:
    trapConfigurationChangeInteger.setStatus(
        "current"
    )

trapConfigurationChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 4)
)
trapConfigurationChangeDisplayString.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueDisplayString"))
)
if mibBuilder.loadTexts:
    trapConfigurationChangeDisplayString.setStatus(
        "current"
    )

trapConfigurationChangeOID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 5)
)
trapConfigurationChangeOID.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueOID"))
)
if mibBuilder.loadTexts:
    trapConfigurationChangeOID.setStatus(
        "current"
    )

trapConfigurationChangeIpAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 6)
)
trapConfigurationChangeIpAddress.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueIpAddress"))
)
if mibBuilder.loadTexts:
    trapConfigurationChangeIpAddress.setStatus(
        "current"
    )

trapConditionNotInList = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 20)
)
trapConditionNotInList.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapConditionNotInList.setStatus(
        "current"
    )

trapConditionAlreadyInList = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 21)
)
trapConditionAlreadyInList.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapConditionAlreadyInList.setStatus(
        "current"
    )

trapConditionListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 22)
)
trapConditionListFull.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapConditionListFull.setStatus(
        "current"
    )

trapInvalidCaseInSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 23)
)
trapInvalidCaseInSwitch.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapInvalidCaseInSwitch.setStatus(
        "current"
    )

trapCannotCreateSemaphore = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 24)
)
trapCannotCreateSemaphore.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapCannotCreateSemaphore.setStatus(
        "current"
    )

trapCannotOpenSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 25)
)
trapCannotOpenSocket.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapCannotOpenSocket.setStatus(
        "current"
    )

trapUnknownMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 26)
)
trapUnknownMessageReceived.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapUnknownMessageReceived.setStatus(
        "current"
    )

trapInvalidMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 27)
)
trapInvalidMessageReceived.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapInvalidMessageReceived.setStatus(
        "current"
    )

trapHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8000)
)
trapHardwareFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapHardwareFault.setStatus(
        "current"
    )

trapInvalidInitData = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8001)
)
trapInvalidInitData.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapInvalidInitData.setStatus(
        "current"
    )

trapTemperatureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8002)
)
trapTemperatureFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapTemperatureFault.setStatus(
        "current"
    )

trapFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8003)
)
trapFanFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapFanFault.setStatus(
        "current"
    )

trapPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8004)
)
trapPowerFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapPowerFault.setStatus(
        "current"
    )

trapGbeLossOfPhysicalInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8020)
)
trapGbeLossOfPhysicalInput.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeLossOfPhysicalInput.setStatus(
        "current"
    )

trapGbeBufferFullness = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8021)
)
trapGbeBufferFullness.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeBufferFullness.setStatus(
        "current"
    )

trapGbeInputStreamLowBitRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8022)
)
trapGbeInputStreamLowBitRate.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeInputStreamLowBitRate.setStatus(
        "current"
    )

trapGbeInputStreamHighBitRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8023)
)
trapGbeInputStreamHighBitRate.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeInputStreamHighBitRate.setStatus(
        "current"
    )

trapGbeMptsRedundPrimaryThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8024)
)
trapGbeMptsRedundPrimaryThreshold.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeMptsRedundPrimaryThreshold.setStatus(
        "current"
    )

trapGbeMptsRedundFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8025)
)
trapGbeMptsRedundFailOver.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeMptsRedundFailOver.setStatus(
        "current"
    )

trapServiceInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8026)
)
trapServiceInError.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapServiceInError.setStatus(
        "current"
    )

trapGbeLossOfInputStream = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8027)
)
trapGbeLossOfInputStream.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeLossOfInputStream.setStatus(
        "current"
    )

trapGigeToHostCommFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8028)
)
trapGigeToHostCommFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGigeToHostCommFault.setStatus(
        "current"
    )

trapGbeInterfaceRedundFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8029)
)
trapGbeInterfaceRedundFailOver.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapGbeInterfaceRedundFailOver.setStatus(
        "current"
    )

trapOutputUtilizationFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8040)
)
trapOutputUtilizationFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapOutputUtilizationFault.setStatus(
        "current"
    )

trapOutputOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8041)
)
trapOutputOverflow.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapOutputOverflow.setStatus(
        "current"
    )

trapQamModuleFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8042)
)
trapQamModuleFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamModuleFault.setStatus(
        "current"
    )

trapQamRfPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8043)
)
trapQamRfPortFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamRfPortFault.setStatus(
        "current"
    )

trapQamChannelFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8044)
)
trapQamChannelFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamChannelFault.setStatus(
        "current"
    )

trapQamRfRedundFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8045)
)
trapQamRfRedundFailOver.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamRfRedundFailOver.setStatus(
        "current"
    )

trapQamRfRedundMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8046)
)
trapQamRfRedundMismatch.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamRfRedundMismatch.setStatus(
        "current"
    )

trapRtspControllerCommFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8050)
)
trapRtspControllerCommFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapRtspControllerCommFault.setStatus(
        "current"
    )

trapRdsCommFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8060)
)
trapRdsCommFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapRdsCommFault.setStatus(
        "current"
    )

trapRemCommFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8070)
)
trapRemCommFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapRemCommFault.setStatus(
        "current"
    )

trapRemFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8071)
)
trapRemFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapRemFault.setStatus(
        "current"
    )

trapDepiControlConnectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8080)
)
trapDepiControlConnectionFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapDepiControlConnectionFault.setStatus(
        "current"
    )

trapDepiSessionSetupFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8081)
)
trapDepiSessionSetupFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapDepiSessionSetupFault.setStatus(
        "current"
    )

trapDtiSyncLossFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8082)
)
trapDtiSyncLossFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapDtiSyncLossFault.setStatus(
        "current"
    )

trapChassisRedundancyPrimaryFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8090)
)
trapChassisRedundancyPrimaryFailover.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyPrimaryFailover.setStatus(
        "current"
    )

trapChassisRedundancySecondaryFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8091)
)
trapChassisRedundancySecondaryFailover.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancySecondaryFailover.setStatus(
        "current"
    )

trapChassisRedundancyAvailabilityFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8092)
)
trapChassisRedundancyAvailabilityFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyAvailabilityFault.setStatus(
        "current"
    )

trapChassisRedundancyLinkFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8093)
)
trapChassisRedundancyLinkFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyLinkFault.setStatus(
        "current"
    )

trapChassisRedundancyConfigurationFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8094)
)
trapChassisRedundancyConfigurationFault.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyConfigurationFault.setStatus(
        "current"
    )

trapEmUserLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8100)
)
trapEmUserLoginFailed.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapEmUserLoginFailed.setStatus(
        "current"
    )

trapQamModuleUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8101)
)
trapQamModuleUpgraded.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapQamModuleUpgraded.setStatus(
        "current"
    )

trapChassisRedundancyPrimaryForceFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8110)
)
trapChassisRedundancyPrimaryForceFailover.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyPrimaryForceFailover.setStatus(
        "current"
    )

trapChassisRedundancySecondaryForceFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8111)
)
trapChassisRedundancySecondaryForceFailover.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancySecondaryForceFailover.setStatus(
        "current"
    )

trapChassisRedundancyFirmwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8112)
)
trapChassisRedundancyFirmwareVersionMismatch.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyFirmwareVersionMismatch.setStatus(
        "current"
    )

trapChassisRedundancyQAMVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31, 0, 8113)
)
trapChassisRedundancyQAMVersionMismatch.setObjects(
      *(("BCS-TRAPS-MIB", "trapIdentifier"),
        ("BCS-TRAPS-MIB", "trapSequenceId"),
        ("BCS-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("BCS-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("BCS-TRAPS-MIB", "trapPerceivedSeverity"),
        ("BCS-TRAPS-MIB", "trapNetworkElemOperState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("BCS-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("BCS-TRAPS-MIB", "trapText"),
        ("BCS-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"),
        ("BCS-TRAPS-MIB", "trapChangedObjectId"),
        ("BCS-TRAPS-MIB", "trapChangedValueInteger"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger1"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger2"),
        ("BCS-TRAPS-MIB", "trapAdditionalInfoInteger3"))
)
if mibBuilder.loadTexts:
    trapChassisRedundancyQAMVersionMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APEX-MIB",
    **{"EnableDisableTYPE": EnableDisableTYPE,
       "ActiveTYPE": ActiveTYPE,
       "ApplyDataToDeviceTYPE": ApplyDataToDeviceTYPE,
       "ResetStatisticsTYPE": ResetStatisticsTYPE,
       "ClearAlarmTYPE": ClearAlarmTYPE,
       "RateComparisonTYPE": RateComparisonTYPE,
       "InputTsStateTYPE": InputTsStateTYPE,
       "EthernetInterfaceTYPE": EthernetInterfaceTYPE,
       "apex": apex,
       "apexTraps": apexTraps,
       "trapConfigurationChangeInteger": trapConfigurationChangeInteger,
       "trapConfigurationChangeDisplayString": trapConfigurationChangeDisplayString,
       "trapConfigurationChangeOID": trapConfigurationChangeOID,
       "trapConfigurationChangeIpAddress": trapConfigurationChangeIpAddress,
       "trapConditionNotInList": trapConditionNotInList,
       "trapConditionAlreadyInList": trapConditionAlreadyInList,
       "trapConditionListFull": trapConditionListFull,
       "trapInvalidCaseInSwitch": trapInvalidCaseInSwitch,
       "trapCannotCreateSemaphore": trapCannotCreateSemaphore,
       "trapCannotOpenSocket": trapCannotOpenSocket,
       "trapUnknownMessageReceived": trapUnknownMessageReceived,
       "trapInvalidMessageReceived": trapInvalidMessageReceived,
       "trapHardwareFault": trapHardwareFault,
       "trapInvalidInitData": trapInvalidInitData,
       "trapTemperatureFault": trapTemperatureFault,
       "trapFanFault": trapFanFault,
       "trapPowerFault": trapPowerFault,
       "trapGbeLossOfPhysicalInput": trapGbeLossOfPhysicalInput,
       "trapGbeBufferFullness": trapGbeBufferFullness,
       "trapGbeInputStreamLowBitRate": trapGbeInputStreamLowBitRate,
       "trapGbeInputStreamHighBitRate": trapGbeInputStreamHighBitRate,
       "trapGbeMptsRedundPrimaryThreshold": trapGbeMptsRedundPrimaryThreshold,
       "trapGbeMptsRedundFailOver": trapGbeMptsRedundFailOver,
       "trapServiceInError": trapServiceInError,
       "trapGbeLossOfInputStream": trapGbeLossOfInputStream,
       "trapGigeToHostCommFault": trapGigeToHostCommFault,
       "trapGbeInterfaceRedundFailOver": trapGbeInterfaceRedundFailOver,
       "trapOutputUtilizationFault": trapOutputUtilizationFault,
       "trapOutputOverflow": trapOutputOverflow,
       "trapQamModuleFault": trapQamModuleFault,
       "trapQamRfPortFault": trapQamRfPortFault,
       "trapQamChannelFault": trapQamChannelFault,
       "trapQamRfRedundFailOver": trapQamRfRedundFailOver,
       "trapQamRfRedundMismatch": trapQamRfRedundMismatch,
       "trapRtspControllerCommFault": trapRtspControllerCommFault,
       "trapRdsCommFault": trapRdsCommFault,
       "trapRemCommFault": trapRemCommFault,
       "trapRemFault": trapRemFault,
       "trapDepiControlConnectionFault": trapDepiControlConnectionFault,
       "trapDepiSessionSetupFault": trapDepiSessionSetupFault,
       "trapDtiSyncLossFault": trapDtiSyncLossFault,
       "trapChassisRedundancyPrimaryFailover": trapChassisRedundancyPrimaryFailover,
       "trapChassisRedundancySecondaryFailover": trapChassisRedundancySecondaryFailover,
       "trapChassisRedundancyAvailabilityFault": trapChassisRedundancyAvailabilityFault,
       "trapChassisRedundancyLinkFault": trapChassisRedundancyLinkFault,
       "trapChassisRedundancyConfigurationFault": trapChassisRedundancyConfigurationFault,
       "trapEmUserLoginFailed": trapEmUserLoginFailed,
       "trapQamModuleUpgraded": trapQamModuleUpgraded,
       "trapChassisRedundancyPrimaryForceFailover": trapChassisRedundancyPrimaryForceFailover,
       "trapChassisRedundancySecondaryForceFailover": trapChassisRedundancySecondaryForceFailover,
       "trapChassisRedundancyFirmwareVersionMismatch": trapChassisRedundancyFirmwareVersionMismatch,
       "trapChassisRedundancyQAMVersionMismatch": trapChassisRedundancyQAMVersionMismatch,
       "apexSys": apexSys,
       "apexSysConfig": apexSysConfig,
       "apexSysConfigGeneral": apexSysConfigGeneral,
       "apexSaveConfig": apexSaveConfig,
       "apexProductName": apexProductName,
       "apexBootMethod": apexBootMethod,
       "apexAutoRebootEnable": apexAutoRebootEnable,
       "apexSysConfigMcEmmInsertion": apexSysConfigMcEmmInsertion,
       "apexMcEmmInsertionMode": apexMcEmmInsertionMode,
       "apexMcEmmInsertionPid1Enable": apexMcEmmInsertionPid1Enable,
       "apexMcEmmInsertionPid1": apexMcEmmInsertionPid1,
       "apexMcEmmInsertionPid2Enable": apexMcEmmInsertionPid2Enable,
       "apexMcEmmInsertionPid2": apexMcEmmInsertionPid2,
       "apexMcEmmInsertionApplyChange": apexMcEmmInsertionApplyChange,
       "apexSysStatus": apexSysStatus,
       "apexSysStatusGeneral": apexSysStatusGeneral,
       "apexBootReason": apexBootReason,
       "apexMaxServiceMappings": apexMaxServiceMappings,
       "apexSysStatusVersions": apexSysStatusVersions,
       "apexHostProcessorBootCodeVersion": apexHostProcessorBootCodeVersion,
       "apexMuxFpgaVersion": apexMuxFpgaVersion,
       "apexMuxFpgaEncryption": apexMuxFpgaEncryption,
       "apexMainBoardVersion": apexMainBoardVersion,
       "apexHostApplicationDate": apexHostApplicationDate,
       "apexProductType": apexProductType,
       "apexMainBoardType": apexMainBoardType,
       "apexGlueFpgaVersion": apexGlueFpgaVersion,
       "apexGlueCpldVersion": apexGlueCpldVersion,
       "apexDtiFpgaVersion": apexDtiFpgaVersion,
       "apexMpc2FpgaVersion": apexMpc2FpgaVersion,
       "apexDpmVersion": apexDpmVersion,
       "apexTime": apexTime,
       "apexTimeConfig": apexTimeConfig,
       "apexTimeConfigGeneral": apexTimeConfigGeneral,
       "apexTimeSource": apexTimeSource,
       "apexSntpUtcOffset": apexSntpUtcOffset,
       "apexSntpServerSpecified": apexSntpServerSpecified,
       "apexSntpServerIpAddr": apexSntpServerIpAddr,
       "apexUserSuppliedTime": apexUserSuppliedTime,
       "apexTimeStatus": apexTimeStatus,
       "apexTimeStatusGeneral": apexTimeStatusGeneral,
       "apexSystemTime": apexSystemTime,
       "apexOperationalTime": apexOperationalTime,
       "apexTemperature": apexTemperature,
       "apexTemperatureConfig": apexTemperatureConfig,
       "apexTemperatureConfigGeneral": apexTemperatureConfigGeneral,
       "apexTemperatureStatus": apexTemperatureStatus,
       "apexTemperatureStatusGeneral": apexTemperatureStatusGeneral,
       "apexMainBoardTemperature": apexMainBoardTemperature,
       "apexMainBoardTempFrontIntake": apexMainBoardTempFrontIntake,
       "apexMainBoardTempMuxFpga": apexMainBoardTempMuxFpga,
       "apexMainBoardTempAcpModule": apexMainBoardTempAcpModule,
       "apexMainBoardTempHostProcessor": apexMainBoardTempHostProcessor,
       "apexMainBoardTemperatureFault": apexMainBoardTemperatureFault,
       "apexMainBoardTempFrontIntakeFault": apexMainBoardTempFrontIntakeFault,
       "apexMainBoardTempMuxFpgaFault": apexMainBoardTempMuxFpgaFault,
       "apexMainBoardTempAcpModuleFault": apexMainBoardTempAcpModuleFault,
       "apexMainBoardTempHostProcessorFault": apexMainBoardTempHostProcessorFault,
       "apexPowerSupply": apexPowerSupply,
       "apexPsConfig": apexPsConfig,
       "apexPsConfigGeneral": apexPsConfigGeneral,
       "apexPsStatus": apexPsStatus,
       "apexPsStatusGeneral": apexPsStatusGeneral,
       "apexPsStatusTable": apexPsStatusTable,
       "apexPsStatusEntry": apexPsStatusEntry,
       "apexPsStatusPsNum": apexPsStatusPsNum,
       "apexPsStatusInstalled": apexPsStatusInstalled,
       "apexPsStatusOutputVoltage": apexPsStatusOutputVoltage,
       "apexPsStatusOutputCurrent": apexPsStatusOutputCurrent,
       "apexPsStatusFanSpeed": apexPsStatusFanSpeed,
       "apexPsStatusFanStatus": apexPsStatusFanStatus,
       "apexPsStatusTemperatureStatus": apexPsStatusTemperatureStatus,
       "apexPsStatusInputPowerStatus": apexPsStatusInputPowerStatus,
       "apexPsStatusOutputPowerStatus": apexPsStatusOutputPowerStatus,
       "apexPsStatusErrorStatus": apexPsStatusErrorStatus,
       "apexPsStatusFaultCondition": apexPsStatusFaultCondition,
       "apexPsStatusDiagnosticData1": apexPsStatusDiagnosticData1,
       "apexPsStatusDiagnosticData2": apexPsStatusDiagnosticData2,
       "apexPsStatusCommError": apexPsStatusCommError,
       "apexPsStatusVersionsTable": apexPsStatusVersionsTable,
       "apexPsStatusVersionsEntry": apexPsStatusVersionsEntry,
       "apexPsStatusVersionsPsNum": apexPsStatusVersionsPsNum,
       "apexPsStatusVersionsModel": apexPsStatusVersionsModel,
       "apexPsStatusVersionsSerialNumber": apexPsStatusVersionsSerialNumber,
       "apexAsi": apexAsi,
       "apexAsiConfig": apexAsiConfig,
       "apexAsiMonitorPortConfig": apexAsiMonitorPortConfig,
       "apexAsiMonitorPortOutputTsNum": apexAsiMonitorPortOutputTsNum,
       "apexAsiMonitorPortEncryption": apexAsiMonitorPortEncryption,
       "apexFastEnet": apexFastEnet,
       "apexFastEnetConfig": apexFastEnetConfig,
       "apexFastEnetConfigGeneral": apexFastEnetConfigGeneral,
       "apexFastEnetDefaultGateway": apexFastEnetDefaultGateway,
       "apexFastEnetInsertRateTable": apexFastEnetInsertRateTable,
       "apexFastEnetInsertRateEntry": apexFastEnetInsertRateEntry,
       "apexFastEnetInsertRateOutputTsNum": apexFastEnetInsertRateOutputTsNum,
       "apexFastEnetInsertRate": apexFastEnetInsertRate,
       "apexFastEnetRoutingApplyChange": apexFastEnetRoutingApplyChange,
       "apexFastEnetRoutingTable": apexFastEnetRoutingTable,
       "apexFastEnetRoutingEntry": apexFastEnetRoutingEntry,
       "apexFastEnetRoutingIndex": apexFastEnetRoutingIndex,
       "apexFastEnetRoutingDestinIp": apexFastEnetRoutingDestinIp,
       "apexFastEnetRoutingGatewayIp": apexFastEnetRoutingGatewayIp,
       "apexFastEnetRoutingSubnetMask": apexFastEnetRoutingSubnetMask,
       "apexFastEnetStatus": apexFastEnetStatus,
       "apexFastEnetStatusGeneral": apexFastEnetStatusGeneral,
       "apexFastEnetMaxInputUdpPorts": apexFastEnetMaxInputUdpPorts,
       "apexFastEnetStatusPacketsTable": apexFastEnetStatusPacketsTable,
       "apexFastEnetStatusPacketsEntry": apexFastEnetStatusPacketsEntry,
       "apexFastEnetPacketsPortNum": apexFastEnetPacketsPortNum,
       "apexFastEnetPacketsNumPkts": apexFastEnetPacketsNumPkts,
       "apexFastEnetPacketsTotPkts": apexFastEnetPacketsTotPkts,
       "apexFastEnetPacketsNumDiscarded": apexFastEnetPacketsNumDiscarded,
       "apexFastEnetPacketsTotDiscarded": apexFastEnetPacketsTotDiscarded,
       "apexFastEnetInsertPacketsTable": apexFastEnetInsertPacketsTable,
       "apexFastEnetInsertPacketsEntry": apexFastEnetInsertPacketsEntry,
       "apexFastEnetInsPacketsOutputTsNum": apexFastEnetInsPacketsOutputTsNum,
       "apexFastEnetInsPacketsNumPkts": apexFastEnetInsPacketsNumPkts,
       "apexFastEnetInsPacketsTotPkts": apexFastEnetInsPacketsTotPkts,
       "apexFastEnetInsPacketsNumDiscarded": apexFastEnetInsPacketsNumDiscarded,
       "apexFastEnetInsPacketsTotDiscarded": apexFastEnetInsPacketsTotDiscarded,
       "apexOamp": apexOamp,
       "apexOampConfig": apexOampConfig,
       "apexOampConfigGeneral": apexOampConfigGeneral,
       "apexOampIpAddr": apexOampIpAddr,
       "apexOampSubnetMask": apexOampSubnetMask,
       "apexOampAutoNegotiate": apexOampAutoNegotiate,
       "apexOampStatus": apexOampStatus,
       "apexOampStatusGeneral": apexOampStatusGeneral,
       "apexOampMacAddr": apexOampMacAddr,
       "apexOampSpeed": apexOampSpeed,
       "apexOampDuplexMode": apexOampDuplexMode,
       "apexOampInputTsAssignedCount": apexOampInputTsAssignedCount,
       "apexOampLinkActive": apexOampLinkActive,
       "apexDataIp": apexDataIp,
       "apexDataIpConfig": apexDataIpConfig,
       "apexDataIpConfigGeneral": apexDataIpConfigGeneral,
       "apexDataIpAddr": apexDataIpAddr,
       "apexDataIpSubnetMask": apexDataIpSubnetMask,
       "apexDataIpAutoNegotiate": apexDataIpAutoNegotiate,
       "apexDataIpStatus": apexDataIpStatus,
       "apexDataIpStatusGeneral": apexDataIpStatusGeneral,
       "apexDataIpMacAddr": apexDataIpMacAddr,
       "apexDataIpSpeed": apexDataIpSpeed,
       "apexDataIpDuplexMode": apexDataIpDuplexMode,
       "apexDataIpInputTsAssignedCount": apexDataIpInputTsAssignedCount,
       "apexDataIpAddrInUse": apexDataIpAddrInUse,
       "apexDataIpSubnetMaskInUse": apexDataIpSubnetMaskInUse,
       "apexDataIpInUseReason": apexDataIpInUseReason,
       "apexDataIpLinkActive": apexDataIpLinkActive,
       "apexGbe": apexGbe,
       "apexGbeConfig": apexGbeConfig,
       "apexGbeConfigGeneral": apexGbeConfigGeneral,
       "apexGbeDefaultGateway1": apexGbeDefaultGateway1,
       "apexGbeDefaultGateway2": apexGbeDefaultGateway2,
       "apexGbeJitterAbsorption": apexGbeJitterAbsorption,
       "apexGbeGarpPeriodicity": apexGbeGarpPeriodicity,
       "apexGbeConfigTableApplyChange": apexGbeConfigTableApplyChange,
       "apexGbeNominalBufferLevel": apexGbeNominalBufferLevel,
       "apexGbeInputDataTsSmoothingPeriod": apexGbeInputDataTsSmoothingPeriod,
       "apexGbeInputDataTsBufferDepth": apexGbeInputDataTsBufferDepth,
       "apexGbeConfigInputDataTsApplyText": apexGbeConfigInputDataTsApplyText,
       "apexGbeConfInputUnicastTimeout": apexGbeConfInputUnicastTimeout,
       "apexGbeConfInputMulticastTimeout": apexGbeConfInputMulticastTimeout,
       "apexGbeConfLossOfInputTsType": apexGbeConfLossOfInputTsType,
       "apexGbeConfigTable": apexGbeConfigTable,
       "apexGbeConfigEntry": apexGbeConfigEntry,
       "apexGbeConfigInterfaceNum": apexGbeConfigInterfaceNum,
       "apexGbeConfigEnable": apexGbeConfigEnable,
       "apexGbeConfigIpAddr": apexGbeConfigIpAddr,
       "apexGbeConfigIpSubnetMask": apexGbeConfigIpSubnetMask,
       "apexGbeConfigAutoNegotiate": apexGbeConfigAutoNegotiate,
       "apexGbeConfigFrameBufferTable": apexGbeConfigFrameBufferTable,
       "apexGbeConfigFrameBufferEntry": apexGbeConfigFrameBufferEntry,
       "apexGbeConfigFrameBufferProcessorNum": apexGbeConfigFrameBufferProcessorNum,
       "apexGbeConfigFrameBufferMaxInDataRate": apexGbeConfigFrameBufferMaxInDataRate,
       "apexGbeConfigFrameBufferAlarmThreshold": apexGbeConfigFrameBufferAlarmThreshold,
       "apexGbeConfigInputRedundancy": apexGbeConfigInputRedundancy,
       "apexGbeConfigInputRedundancyGeneral": apexGbeConfigInputRedundancyGeneral,
       "apexGbeConfInRedundMonitorPeriod": apexGbeConfInRedundMonitorPeriod,
       "apexGbeConfInRedundSwitchTime": apexGbeConfInRedundSwitchTime,
       "apexGbeConfInRedundAutoSwitchBack": apexGbeConfInRedundAutoSwitchBack,
       "apexGbeConfInRedundForceToSecondary": apexGbeConfInRedundForceToSecondary,
       "apexGbeConfInRedundForceToPrimary": apexGbeConfInRedundForceToPrimary,
       "apexGbeConfInRedundManualRouteRedundType": apexGbeConfInRedundManualRouteRedundType,
       "apexGbeConfigInputDataTsTable": apexGbeConfigInputDataTsTable,
       "apexGbeConfigInputDataTsEntry": apexGbeConfigInputDataTsEntry,
       "apexGbeConfigInputDataTsIndex": apexGbeConfigInputDataTsIndex,
       "apexGbeConfigInputDataTsEnable": apexGbeConfigInputDataTsEnable,
       "apexGbeConfigInputDataTsInterface": apexGbeConfigInputDataTsInterface,
       "apexGbeConfigInputDataTsUdp": apexGbeConfigInputDataTsUdp,
       "apexGbeConfigInputDataTsMulticastIp": apexGbeConfigInputDataTsMulticastIp,
       "apexGbeConfigInputDataTsSourceIp": apexGbeConfigInputDataTsSourceIp,
       "apexGbeConfigInputDataTsApplyTable": apexGbeConfigInputDataTsApplyTable,
       "apexGbeConfigInputDataTsApplyEntry": apexGbeConfigInputDataTsApplyEntry,
       "apexGbeConfigInputDataTsApplyIndex": apexGbeConfigInputDataTsApplyIndex,
       "apexGbeConfigInputDataTsApplyChange": apexGbeConfigInputDataTsApplyChange,
       "apexGbeConfigInterfaceRedundancy": apexGbeConfigInterfaceRedundancy,
       "apexGbeConfigInterfaceRedundancyGeneral": apexGbeConfigInterfaceRedundancyGeneral,
       "apexGbeConfIfRedundAutoSwitchBackEnable": apexGbeConfIfRedundAutoSwitchBackEnable,
       "apexGbeConfIfRedundAutoSwitchBackPeriod": apexGbeConfIfRedundAutoSwitchBackPeriod,
       "apexGbeConfigInterfaceRedundancyTable": apexGbeConfigInterfaceRedundancyTable,
       "apexGbeConfigInterfaceRedundancyEntry": apexGbeConfigInterfaceRedundancyEntry,
       "apexGbeConfIfRedundIndex": apexGbeConfIfRedundIndex,
       "apexGbeConfIfRedundEnable": apexGbeConfIfRedundEnable,
       "apexGbeConfIfRedundForceFailover": apexGbeConfIfRedundForceFailover,
       "apexGbeConfIfRedundSuspendFailover": apexGbeConfIfRedundSuspendFailover,
       "apexGbeConfigInterfaceRedundancyApplyTable": apexGbeConfigInterfaceRedundancyApplyTable,
       "apexGbeConfigInterfaceRedundancyApplyEntry": apexGbeConfigInterfaceRedundancyApplyEntry,
       "apexGbeConfIfRedundApplyIndex": apexGbeConfIfRedundApplyIndex,
       "apexGbeConfIfRedundApplyChange": apexGbeConfIfRedundApplyChange,
       "apexGbeStatus": apexGbeStatus,
       "apexGbeStatusGeneral": apexGbeStatusGeneral,
       "apexGbeBootCodeVersion": apexGbeBootCodeVersion,
       "apexGbeApplicationCodeVersion": apexGbeApplicationCodeVersion,
       "apexGbeMaxInputTs": apexGbeMaxInputTs,
       "apexGbeRoutedPacketUpdateInterval": apexGbeRoutedPacketUpdateInterval,
       "apexGbeStatusTable": apexGbeStatusTable,
       "apexGbeStatusEntry": apexGbeStatusEntry,
       "apexGbeStatusGbeInterfaceNum": apexGbeStatusGbeInterfaceNum,
       "apexGbeStatusMacAddr": apexGbeStatusMacAddr,
       "apexGbeStatusLinkActive": apexGbeStatusLinkActive,
       "apexGbeStatusIgmpVersion": apexGbeStatusIgmpVersion,
       "apexGbeStatusLossOfPhysicalInput": apexGbeStatusLossOfPhysicalInput,
       "apexGbeInputTsAssignedTable": apexGbeInputTsAssignedTable,
       "apexGbeInputTsAssignedEntry": apexGbeInputTsAssignedEntry,
       "apexGbeInputTsAssignedGbeInterfaceNum": apexGbeInputTsAssignedGbeInterfaceNum,
       "apexGbeInputTsAssignedCount": apexGbeInputTsAssignedCount,
       "apexGbeOpenInputUdpPortTable": apexGbeOpenInputUdpPortTable,
       "apexGbeOpenInputUdpPortEntry": apexGbeOpenInputUdpPortEntry,
       "apexGbeOpenInputUdpPortGbeInterfaceNum": apexGbeOpenInputUdpPortGbeInterfaceNum,
       "apexGbeOpenInputUdpPortCount": apexGbeOpenInputUdpPortCount,
       "apexGbeStatusRoutedPacketTable": apexGbeStatusRoutedPacketTable,
       "apexGbeStatusRoutedPacketEntry": apexGbeStatusRoutedPacketEntry,
       "apexGbeStatusRoutedPacketOutputTsNum": apexGbeStatusRoutedPacketOutputTsNum,
       "apexGbeStatusTotRoutedPackets": apexGbeStatusTotRoutedPackets,
       "apexGbeStatusNumRoutedPackets": apexGbeStatusNumRoutedPackets,
       "apexGbeStatusFrameCounter": apexGbeStatusFrameCounter,
       "apexGbeStatusFrameCounterGeneral": apexGbeStatusFrameCounterGeneral,
       "apexGbeStatusFrameCounterTableResetAll": apexGbeStatusFrameCounterTableResetAll,
       "apexGbeFrameCounterUpdateInterval": apexGbeFrameCounterUpdateInterval,
       "apexGbeStatusFrameCounterTable": apexGbeStatusFrameCounterTable,
       "apexGbeStatusFrameCounterEntry": apexGbeStatusFrameCounterEntry,
       "apexGbeFrameCounterGbeInterfaceNum": apexGbeFrameCounterGbeInterfaceNum,
       "apexGbeFrameCounterReset": apexGbeFrameCounterReset,
       "apexGbeTotalRxSinglecastFrames": apexGbeTotalRxSinglecastFrames,
       "apexGbeTotalRxMulticastFrames": apexGbeTotalRxMulticastFrames,
       "apexGbeTotalRxBroadcastFrames": apexGbeTotalRxBroadcastFrames,
       "apexGbeTotalRxErrorFrames": apexGbeTotalRxErrorFrames,
       "apexGbeTotalRxFrames": apexGbeTotalRxFrames,
       "apexGbeRxSinglecastFrames": apexGbeRxSinglecastFrames,
       "apexGbeRxMulticastFrames": apexGbeRxMulticastFrames,
       "apexGbeRxBroadcastFrames": apexGbeRxBroadcastFrames,
       "apexGbeRxErrorFrames": apexGbeRxErrorFrames,
       "apexGbeRxFrames": apexGbeRxFrames,
       "apexGbeTotalTxGoodFrames": apexGbeTotalTxGoodFrames,
       "apexGbeTotalTxErrorFrames": apexGbeTotalTxErrorFrames,
       "apexGbeTxGoodFrames": apexGbeTxGoodFrames,
       "apexGbeTxErrorFrames": apexGbeTxErrorFrames,
       "apexGbeRxDocsisFrames": apexGbeRxDocsisFrames,
       "apexGbeTotalRxDocsisFrames": apexGbeTotalRxDocsisFrames,
       "apexGbeRxMpegDocsisFrames": apexGbeRxMpegDocsisFrames,
       "apexGbeIpFragmentedPkts": apexGbeIpFragmentedPkts,
       "apexGbeTotalIpFragmentedPkts": apexGbeTotalIpFragmentedPkts,
       "apexGbeFrameBufferStats": apexGbeFrameBufferStats,
       "apexGbeFrameBufferStatsGeneral": apexGbeFrameBufferStatsGeneral,
       "apexGbeFrameBufferStatsTable": apexGbeFrameBufferStatsTable,
       "apexGbeFrameBufferStatsEntry": apexGbeFrameBufferStatsEntry,
       "apexGbeFrameBufferProcessorNum": apexGbeFrameBufferProcessorNum,
       "apexGbeFrameBufferResetLevelLimit": apexGbeFrameBufferResetLevelLimit,
       "apexGbeFrameBufferCurrMsLevel": apexGbeFrameBufferCurrMsLevel,
       "apexGbeFrameBufferCurrPercentFull": apexGbeFrameBufferCurrPercentFull,
       "apexGbeFrameBufferUnderflowLevel": apexGbeFrameBufferUnderflowLevel,
       "apexGbeFrameBufferOverflowLevel": apexGbeFrameBufferOverflowLevel,
       "apexGbeFrameBufferAlarmStatus": apexGbeFrameBufferAlarmStatus,
       "apexGbeFrameBufferHourlyTable": apexGbeFrameBufferHourlyTable,
       "apexGbeFrameBufferHourlyEntry": apexGbeFrameBufferHourlyEntry,
       "apexGbeFrameBufferHourlyProcessorNum": apexGbeFrameBufferHourlyProcessorNum,
       "apexGbeFrameBufferHourlyIndex": apexGbeFrameBufferHourlyIndex,
       "apexGbeFrameBufferHourlyInInterface": apexGbeFrameBufferHourlyInInterface,
       "apexGbeFrameBufferHourlyInUdp": apexGbeFrameBufferHourlyInUdp,
       "apexGbeFrameBufferHourlyInMulticastIp": apexGbeFrameBufferHourlyInMulticastIp,
       "apexGbeFrameBufferHourlyInSourceIp": apexGbeFrameBufferHourlyInSourceIp,
       "apexGbeFrameBufferHourlyMaxMsLevel": apexGbeFrameBufferHourlyMaxMsLevel,
       "apexGbeFrameBufferHourlyMaxPercentFull": apexGbeFrameBufferHourlyMaxPercentFull,
       "apexGbeFrameBufferHourlyGpsTime": apexGbeFrameBufferHourlyGpsTime,
       "apexGbeFrameBufferHourlyOverflows": apexGbeFrameBufferHourlyOverflows,
       "apexGbeFrameBufferHourlyResets": apexGbeFrameBufferHourlyResets,
       "apexGbeStatusInputTransportStream": apexGbeStatusInputTransportStream,
       "apexGbeStatusInputTsGeneral": apexGbeStatusInputTsGeneral,
       "apexGbeStatusInputTsUpdateInterval": apexGbeStatusInputTsUpdateInterval,
       "apexGbeStatusInputTsTable": apexGbeStatusInputTsTable,
       "apexGbeStatusInputTsEntry": apexGbeStatusInputTsEntry,
       "apexGbeStatInTsInputTsNum": apexGbeStatInTsInputTsNum,
       "apexGbeStatInTsSamplingPeriod": apexGbeStatInTsSamplingPeriod,
       "apexGbeStatInTsPriCurDataCount": apexGbeStatInTsPriCurDataCount,
       "apexGbeStatInTsPriAvgDataCount": apexGbeStatInTsPriAvgDataCount,
       "apexGbeStatInTsPriMinDataCount": apexGbeStatInTsPriMinDataCount,
       "apexGbeStatInTsPriPeakDataCount": apexGbeStatInTsPriPeakDataCount,
       "apexGbeStatInTsPriCurStreamCount": apexGbeStatInTsPriCurStreamCount,
       "apexGbeStatInTsPriAvgStreamCount": apexGbeStatInTsPriAvgStreamCount,
       "apexGbeStatInTsPriMinStreamCount": apexGbeStatInTsPriMinStreamCount,
       "apexGbeStatInTsPriPeakStreamCount": apexGbeStatInTsPriPeakStreamCount,
       "apexGbeStatInTsSecCurDataCount": apexGbeStatInTsSecCurDataCount,
       "apexGbeStatInTsSecAvgDataCount": apexGbeStatInTsSecAvgDataCount,
       "apexGbeStatInTsSecMinDataCount": apexGbeStatInTsSecMinDataCount,
       "apexGbeStatInTsSecPeakDataCount": apexGbeStatInTsSecPeakDataCount,
       "apexGbeStatInTsSecCurStreamCount": apexGbeStatInTsSecCurStreamCount,
       "apexGbeStatInTsSecAvgStreamCount": apexGbeStatInTsSecAvgStreamCount,
       "apexGbeStatInTsSecMinStreamCount": apexGbeStatInTsSecMinStreamCount,
       "apexGbeStatInTsSecPeakStreamCount": apexGbeStatInTsSecPeakStreamCount,
       "apexGbeStatusInputTsErrorTable": apexGbeStatusInputTsErrorTable,
       "apexGbeStatusInputTsErrorEntry": apexGbeStatusInputTsErrorEntry,
       "apexGbeStatInTsErrorInputTsNum": apexGbeStatInTsErrorInputTsNum,
       "apexGbeStatInTsPriErrorSummary": apexGbeStatInTsPriErrorSummary,
       "apexGbeStatInTsPriLowBitRateError": apexGbeStatInTsPriLowBitRateError,
       "apexGbeStatInTsPriHighBitRateError": apexGbeStatInTsPriHighBitRateError,
       "apexGbeStatInTsMptsRedundPriError": apexGbeStatInTsMptsRedundPriError,
       "apexGbeStatInTsMptsRedundFailError": apexGbeStatInTsMptsRedundFailError,
       "apexGbeStatInTsSecErrorSummary": apexGbeStatInTsSecErrorSummary,
       "apexGbeStatInTsSecLowBitRateError": apexGbeStatInTsSecLowBitRateError,
       "apexGbeStatInTsSecHighBitRateError": apexGbeStatInTsSecHighBitRateError,
       "apexGbeStatInTsPriLossInputError": apexGbeStatInTsPriLossInputError,
       "apexGbeStatInTsSecLossInputError": apexGbeStatInTsSecLossInputError,
       "apexGbeStatusInterfaceRedund": apexGbeStatusInterfaceRedund,
       "apexGbeStatusInterfaceRedundTable": apexGbeStatusInterfaceRedundTable,
       "apexGbeStatusInterfaceRedundEntry": apexGbeStatusInterfaceRedundEntry,
       "apexGbeStatusInterfaceRedundIndex": apexGbeStatusInterfaceRedundIndex,
       "apexGbeStatusInterfaceRedundActiveIf": apexGbeStatusInterfaceRedundActiveIf,
       "apexGbeStatusInterfaceRedundInvalidApplyText": apexGbeStatusInterfaceRedundInvalidApplyText,
       "apexGbeStatusInterfaceRedundFaultCondition": apexGbeStatusInterfaceRedundFaultCondition,
       "apexGbeSfp": apexGbeSfp,
       "apexGbeSfpConfig": apexGbeSfpConfig,
       "apexGbeSfpConfigGeneral": apexGbeSfpConfigGeneral,
       "apexGbeSfpUpdateStatus": apexGbeSfpUpdateStatus,
       "apexGbeSfpStatus": apexGbeSfpStatus,
       "apexGbeSfpStatusGeneral": apexGbeSfpStatusGeneral,
       "apexGbeSfpStatusTable": apexGbeSfpStatusTable,
       "apexGbeSfpStatusEntry": apexGbeSfpStatusEntry,
       "apexGbeSfpStatusGbeIfNum": apexGbeSfpStatusGbeIfNum,
       "apexGbeSfpStatusVendorId": apexGbeSfpStatusVendorId,
       "apexGbeSfpStatusDiagInfo": apexGbeSfpStatusDiagInfo,
       "apexQam": apexQam,
       "apexQamConfig": apexQamConfig,
       "apexQamConfigGeneral": apexQamConfigGeneral,
       "apexQamConfigTransmissionMode": apexQamConfigTransmissionMode,
       "apexQamModuleUpgrade": apexQamModuleUpgrade,
       "apexQamModuleUpgradeSlot": apexQamModuleUpgradeSlot,
       "apexQamModuleUpgradeCode": apexQamModuleUpgradeCode,
       "apexQamModuleUpgradeApplyChange": apexQamModuleUpgradeApplyChange,
       "apexQamConfigApplyTable": apexQamConfigApplyTable,
       "apexQamConfigApplyEntry": apexQamConfigApplyEntry,
       "apexQamConfigApplyRfPortNum": apexQamConfigApplyRfPortNum,
       "apexQamConfigApplyChange": apexQamConfigApplyChange,
       "apexQamRfConfigTable": apexQamRfConfigTable,
       "apexQamRfConfigEntry": apexQamRfConfigEntry,
       "apexQamRfConfigRfPortNum": apexQamRfConfigRfPortNum,
       "apexQamRfConfigNumChannelsEnabled": apexQamRfConfigNumChannelsEnabled,
       "apexQamRfConfigModulationMode": apexQamRfConfigModulationMode,
       "apexQamRfConfigSymbolRate": apexQamRfConfigSymbolRate,
       "apexQamRfConfigSpectrumInvert": apexQamRfConfigSpectrumInvert,
       "apexQamRfConfigTuningMode": apexQamRfConfigTuningMode,
       "apexQamRfConfigEiaFrequencyPlan": apexQamRfConfigEiaFrequencyPlan,
       "apexQamRfConfigEiaChanNumChannelA": apexQamRfConfigEiaChanNumChannelA,
       "apexQamRfConfigRfCenterFreqChannelA": apexQamRfConfigRfCenterFreqChannelA,
       "apexQamRfConfigRfChanSpacing": apexQamRfConfigRfChanSpacing,
       "apexQamRfConfigRfLevelAttenuation": apexQamRfConfigRfLevelAttenuation,
       "apexQamRfConfigRfLevelLowThreshold": apexQamRfConfigRfLevelLowThreshold,
       "apexQamRfConfigRfLevelHighThreshold": apexQamRfConfigRfLevelHighThreshold,
       "apexQamRfConfigMute": apexQamRfConfigMute,
       "apexQamRfConfigInterleaverDepth1": apexQamRfConfigInterleaverDepth1,
       "apexQamRfConfigInterleaverDepth2": apexQamRfConfigInterleaverDepth2,
       "apexQamChannelConfigTable": apexQamChannelConfigTable,
       "apexQamChannelConfigEntry": apexQamChannelConfigEntry,
       "apexQamChanConfigChannelNum": apexQamChanConfigChannelNum,
       "apexQamChanConfigInterleaverSelect": apexQamChanConfigInterleaverSelect,
       "apexQamChanConfigTestMode": apexQamChanConfigTestMode,
       "apexQamRfRedundancyConfig": apexQamRfRedundancyConfig,
       "apexQamRfRedundancyConfigGeneral": apexQamRfRedundancyConfigGeneral,
       "apexQamRfRedundConfigApplyChange": apexQamRfRedundConfigApplyChange,
       "apexQamRfRedundConfigEnable": apexQamRfRedundConfigEnable,
       "apexQamRfRedundConfigRemConnection": apexQamRfRedundConfigRemConnection,
       "apexQamRfRedundConfigApexId": apexQamRfRedundConfigApexId,
       "apexQamRfRedundConfigRemCommonIpAddr": apexQamRfRedundConfigRemCommonIpAddr,
       "apexQamRfRedundConfigAutoSwitchBack": apexQamRfRedundConfigAutoSwitchBack,
       "apexQamRfRedundConfigSuspendFailover": apexQamRfRedundConfigSuspendFailover,
       "apexQamRfRedundConfigForceSwitch": apexQamRfRedundConfigForceSwitch,
       "apexQamRfRedundConfigRemDirectIpOctet1": apexQamRfRedundConfigRemDirectIpOctet1,
       "apexQamChannelConfigApplyTable": apexQamChannelConfigApplyTable,
       "apexQamChannelConfigApplyEntry": apexQamChannelConfigApplyEntry,
       "apexQamChannelConfigApplyChannelNum": apexQamChannelConfigApplyChannelNum,
       "apexQamChannelConfigApplyChange": apexQamChannelConfigApplyChange,
       "apexQamStatus": apexQamStatus,
       "apexQamStatusGeneral": apexQamStatusGeneral,
       "apexQamStatusTransmissionMode": apexQamStatusTransmissionMode,
       "apexQamModuleInstalledCount": apexQamModuleInstalledCount,
       "apexFanModuleInstalledCount": apexFanModuleInstalledCount,
       "apexQamChannelsActiveCount": apexQamChannelsActiveCount,
       "apexQamModuleStatusTable": apexQamModuleStatusTable,
       "apexQamModuleStatusEntry": apexQamModuleStatusEntry,
       "apexQamModuleStatQamModuleNum": apexQamModuleStatQamModuleNum,
       "apexQamModuleStatInstalled": apexQamModuleStatInstalled,
       "apexQamModuleStatFanSpeed": apexQamModuleStatFanSpeed,
       "apexQamModuleStatFanFault": apexQamModuleStatFanFault,
       "apexQamModuleStatTemperature": apexQamModuleStatTemperature,
       "apexQamModuleStatTemperatureFault": apexQamModuleStatTemperatureFault,
       "apexQamModuleStatError": apexQamModuleStatError,
       "apexQamModuleStatFaultCondition": apexQamModuleStatFaultCondition,
       "apexQamModuleStatFaultSumm": apexQamModuleStatFaultSumm,
       "apexQamModuleStatPowerFault": apexQamModuleStatPowerFault,
       "apexQamModuleStatBoardTemperature": apexQamModuleStatBoardTemperature,
       "apexQamModuleStatBoardTemperatureFault": apexQamModuleStatBoardTemperatureFault,
       "apexQamModuleStat5VdcSupply": apexQamModuleStat5VdcSupply,
       "apexQamModuleStat5VdcFault": apexQamModuleStat5VdcFault,
       "apexQamModuleStat3dot3VdcSupply": apexQamModuleStat3dot3VdcSupply,
       "apexQamModuleStat3dot3VdcFault": apexQamModuleStat3dot3VdcFault,
       "apexQamModuleStatCommError": apexQamModuleStatCommError,
       "apexQamModuleStatCodeInitError": apexQamModuleStatCodeInitError,
       "apexQamModuleSerialNumTable": apexQamModuleSerialNumTable,
       "apexQamModuleSerialNumEntry": apexQamModuleSerialNumEntry,
       "apexQamModuleSerialNumQamModuleNum": apexQamModuleSerialNumQamModuleNum,
       "apexQamModuleSerialNumber": apexQamModuleSerialNumber,
       "apexQamQrmRevisionTable": apexQamQrmRevisionTable,
       "apexQamQrmRevisionEntry": apexQamQrmRevisionEntry,
       "apexQamQrmRevRfPortNum": apexQamQrmRevRfPortNum,
       "apexQamQrmRevBoardId": apexQamQrmRevBoardId,
       "apexQamQrmRevAppFw": apexQamQrmRevAppFw,
       "apexQamQrmRevBootLoaderFw": apexQamQrmRevBootLoaderFw,
       "apexQamQrmRevFpga": apexQamQrmRevFpga,
       "apexQamQrmRevHw": apexQamQrmRevHw,
       "apexQamQrmRevSerialNumber": apexQamQrmRevSerialNumber,
       "apexQamQrmRevFpga2": apexQamQrmRevFpga2,
       "apexQamRfPortStatusTable": apexQamRfPortStatusTable,
       "apexQamRfPortStatusEntry": apexQamRfPortStatusEntry,
       "apexQamRfPortStatRfPortNum": apexQamRfPortStatRfPortNum,
       "apexQamRfPortStatInfoRate": apexQamRfPortStatInfoRate,
       "apexQamRfPortStatNumChannelsActive": apexQamRfPortStatNumChannelsActive,
       "apexQamRfPortStatOutputLevel": apexQamRfPortStatOutputLevel,
       "apexQamRfPortStatOutputLevelFault": apexQamRfPortStatOutputLevelFault,
       "apexQamRfPortStatTemperature": apexQamRfPortStatTemperature,
       "apexQamRfPortStatTemperatureFault": apexQamRfPortStatTemperatureFault,
       "apexQamRfPortStat5VdcSupply": apexQamRfPortStat5VdcSupply,
       "apexQamRfPortStat5VdcFault": apexQamRfPortStat5VdcFault,
       "apexQamRfPortStat3dot3VdcSupply": apexQamRfPortStat3dot3VdcSupply,
       "apexQamRfPortStat3dot3VdcFault": apexQamRfPortStat3dot3VdcFault,
       "apexQamRfPortStatFreqPllLock": apexQamRfPortStatFreqPllLock,
       "apexQamRfPortStatRefClockPresent": apexQamRfPortStatRefClockPresent,
       "apexQamRfPortStatRefClockLock": apexQamRfPortStatRefClockLock,
       "apexQamRfPortStatDataClockPresent": apexQamRfPortStatDataClockPresent,
       "apexQamRfPortStatDataSyncFault": apexQamRfPortStatDataSyncFault,
       "apexQamRfPortStatCommError": apexQamRfPortStatCommError,
       "apexQamRfPortStatError": apexQamRfPortStatError,
       "apexQamRfPortStatFaultCondition": apexQamRfPortStatFaultCondition,
       "apexQamRfPortStatChanFaultSumm": apexQamRfPortStatChanFaultSumm,
       "apexQamRfPortStatCodeInitError": apexQamRfPortStatCodeInitError,
       "apexQamChannelStatusTable": apexQamChannelStatusTable,
       "apexQamChannelStatusEntry": apexQamChannelStatusEntry,
       "apexQamChanStatChannelNum": apexQamChanStatChannelNum,
       "apexQamChanStatActive": apexQamChanStatActive,
       "apexQamChanStatRfFreq": apexQamChanStatRfFreq,
       "apexQamChanStatEiaChanNum": apexQamChanStatEiaChanNum,
       "apexQamChanStatDataPresent": apexQamChanStatDataPresent,
       "apexQamChanStatError": apexQamChanStatError,
       "apexQamChanStatFaultCondition": apexQamChanStatFaultCondition,
       "apexQamRfRedundancyStatus": apexQamRfRedundancyStatus,
       "apexQamRfRedundancyStatusGeneral": apexQamRfRedundancyStatusGeneral,
       "apexQamRfRedundStatusBackupPort": apexQamRfRedundStatusBackupPort,
       "apexQamRfRedundStatusFailedPort": apexQamRfRedundStatusFailedPort,
       "apexQamRfRedundStatusMismatch": apexQamRfRedundStatusMismatch,
       "apexQamRfRedundStatusUdpPort": apexQamRfRedundStatusUdpPort,
       "apexQamRfRedundStatusRemConnection": apexQamRfRedundStatusRemConnection,
       "apexQamRfRedundStatusRemError": apexQamRfRedundStatusRemError,
       "apexQamRfRedundStatusRemSwitch": apexQamRfRedundStatusRemSwitch,
       "apexQamRfRedundStatusInvalidApplyText": apexQamRfRedundStatusInvalidApplyText,
       "apexQamRfPortMuteStatusTable": apexQamRfPortMuteStatusTable,
       "apexQamRfPortMuteStatusEntry": apexQamRfPortMuteStatusEntry,
       "apexQamRfPortMuteStatusRfPortNum": apexQamRfPortMuteStatusRfPortNum,
       "apexQamRfPortMuteStatus": apexQamRfPortMuteStatus,
       "apexQamQrmRevisionStatusTable": apexQamQrmRevisionStatusTable,
       "apexQamQrmRevisionStatusEntry": apexQamQrmRevisionStatusEntry,
       "apexQamQrmRevStatQrmNum": apexQamQrmRevStatQrmNum,
       "apexQamQrmRevStatBoardId": apexQamQrmRevStatBoardId,
       "apexQamQrmRevStatAppFw": apexQamQrmRevStatAppFw,
       "apexQamQrmRevStatBootLoaderFw": apexQamQrmRevStatBootLoaderFw,
       "apexQamQrmRevStatFpga": apexQamQrmRevStatFpga,
       "apexQamQrmRevStatHw": apexQamQrmRevStatHw,
       "apexQamQrmRevStatQrmSupported": apexQamQrmRevStatQrmSupported,
       "apexQamQrmRevStatFpga2": apexQamQrmRevStatFpga2,
       "apexQamRfPortChannelInfoTable": apexQamRfPortChannelInfoTable,
       "apexQamRfPortChannelInfoEntry": apexQamRfPortChannelInfoEntry,
       "apexQamRfPortChannelInfoRfPortNum": apexQamRfPortChannelInfoRfPortNum,
       "apexQamRfPortChannelInfoChanA": apexQamRfPortChannelInfoChanA,
       "apexQamRfPortChannelInfoChanCount": apexQamRfPortChannelInfoChanCount,
       "apexQamChannelIdTable": apexQamChannelIdTable,
       "apexQamChannelIdEntry": apexQamChannelIdEntry,
       "apexQamChannelIdChannelNum": apexQamChannelIdChannelNum,
       "apexQamChannelIdSlotNum": apexQamChannelIdSlotNum,
       "apexQamChannelIdRfPortNum": apexQamChannelIdRfPortNum,
       "apexQamChannelIdModuleRfPortNum": apexQamChannelIdModuleRfPortNum,
       "apexQamChannelIdChannelLetter": apexQamChannelIdChannelLetter,
       "apexQamChannelIdChannelDescription": apexQamChannelIdChannelDescription,
       "apexQrmDownload": apexQrmDownload,
       "apexQrmDownloadConfig": apexQrmDownloadConfig,
       "apexQrmDownloadConfigGeneral": apexQrmDownloadConfigGeneral,
       "apexQrmDownloadConfigTable": apexQrmDownloadConfigTable,
       "apexQrmDownloadConfigEntry": apexQrmDownloadConfigEntry,
       "apexQrmDownloadConfigQrmNum": apexQrmDownloadConfigQrmNum,
       "apexQrmDownloadConfigRequest": apexQrmDownloadConfigRequest,
       "apexQrmDownloadStatus": apexQrmDownloadStatus,
       "apexQrmDownloadStatusGeneral": apexQrmDownloadStatusGeneral,
       "apexQrmDownloadStatusTable": apexQrmDownloadStatusTable,
       "apexQrmDownloadStatusEntry": apexQrmDownloadStatusEntry,
       "apexQrmDownloadStatusRfPortNum": apexQrmDownloadStatusRfPortNum,
       "apexQrmDownloadStatusDescription": apexQrmDownloadStatusDescription,
       "apexQrmDownloadProgress": apexQrmDownloadProgress,
       "apexQrmDownloadSupported": apexQrmDownloadSupported,
       "apexQrmDownloadRequired": apexQrmDownloadRequired,
       "apexQrmDownloadFileSet": apexQrmDownloadFileSet,
       "apexQrmFileRevisionTable": apexQrmFileRevisionTable,
       "apexQrmFileRevisionEntry": apexQrmFileRevisionEntry,
       "apexQrmFileRevFileSetNum": apexQrmFileRevFileSetNum,
       "apexQrmFileRevFirmware": apexQrmFileRevFirmware,
       "apexQrmFileRevCalibration": apexQrmFileRevCalibration,
       "apexQrmFileRevFpga": apexQrmFileRevFpga,
       "apexQrmFileRevFpga2": apexQrmFileRevFpga2,
       "apexQrmFileRevDateTime": apexQrmFileRevDateTime,
       "apexSessionControl": apexSessionControl,
       "apexSessionControlConfig": apexSessionControlConfig,
       "apexSessionControlConfigGeneral": apexSessionControlConfigGeneral,
       "apexSesContConfProtocol": apexSesContConfProtocol,
       "apexSesContConfTableApplyChange": apexSesContConfTableApplyChange,
       "apexSesContConfRateCompareType": apexSesContConfRateCompareType,
       "apexSesContConfRedundThreshold": apexSesContConfRedundThreshold,
       "apexSesContConfInputPreEncryptCheck": apexSesContConfInputPreEncryptCheck,
       "apexSesContConfRedundType": apexSesContConfRedundType,
       "apexSesContConfFollowDtcp": apexSesContConfFollowDtcp,
       "apexSesContConfTable": apexSesContConfTable,
       "apexSesContConfEntry": apexSesContConfEntry,
       "apexSesContConfOutputTsNum": apexSesContConfOutputTsNum,
       "apexSesContConfGbePrimaryInterface": apexSesContConfGbePrimaryInterface,
       "apexSesContConfGbeSecondaryInterface": apexSesContConfGbeSecondaryInterface,
       "apexSessionControlStatus": apexSessionControlStatus,
       "apexSessionControlStatusGeneral": apexSessionControlStatusGeneral,
       "apexSesContStatProtocol": apexSesContStatProtocol,
       "apexRpc": apexRpc,
       "apexRpcConfig": apexRpcConfig,
       "apexRpcConfigGeneral": apexRpcConfigGeneral,
       "apexRpcDataCarouselProgram": apexRpcDataCarouselProgram,
       "apexRpcReportAllSessions": apexRpcReportAllSessions,
       "apexRpcDeviceName": apexRpcDeviceName,
       "apexRpcDeviceType": apexRpcDeviceType,
       "apexRpcControlInterface": apexRpcControlInterface,
       "apexRpcNumShellSessions": apexRpcNumShellSessions,
       "apexRpcAvgBandwidthEnable": apexRpcAvgBandwidthEnable,
       "apexRpcApplyChange": apexRpcApplyChange,
       "apexRpcRfPortTable": apexRpcRfPortTable,
       "apexRpcRfPortEntry": apexRpcRfPortEntry,
       "apexRpcRfPortNum": apexRpcRfPortNum,
       "apexRpcRfPortName": apexRpcRfPortName,
       "apexRpcRfPortServiceGroup": apexRpcRfPortServiceGroup,
       "apexRpcRfChannelTable": apexRpcRfChannelTable,
       "apexRpcRfChannelEntry": apexRpcRfChannelEntry,
       "apexRpcRfChannelNum": apexRpcRfChannelNum,
       "apexRpcRfChannelName": apexRpcRfChannelName,
       "apexRpcStatus": apexRpcStatus,
       "apexRpcStatusGeneral": apexRpcStatusGeneral,
       "apexRpcSessionStatTable": apexRpcSessionStatTable,
       "apexRpcSessionStatEntry": apexRpcSessionStatEntry,
       "apexRpcSessionStatIndex": apexRpcSessionStatIndex,
       "apexRpcSessionStatInputTsIndex": apexRpcSessionStatInputTsIndex,
       "apexRpcSessionStatInputProgramNum": apexRpcSessionStatInputProgramNum,
       "apexRpcSessionStatSourceIpAddr3": apexRpcSessionStatSourceIpAddr3,
       "apexRpcSessionStatOutputQamChannel": apexRpcSessionStatOutputQamChannel,
       "apexRpcSessionStatOutputProgramNum": apexRpcSessionStatOutputProgramNum,
       "apexRpcSessionStatProgramBandwidth": apexRpcSessionStatProgramBandwidth,
       "apexRpcSessionStatSessionType": apexRpcSessionStatSessionType,
       "apexRpcSessionStatSessionIdWord1": apexRpcSessionStatSessionIdWord1,
       "apexRpcSessionStatSessionIdWord2": apexRpcSessionStatSessionIdWord2,
       "apexRpcSessionStatSessionIdWord3": apexRpcSessionStatSessionIdWord3,
       "apexRpcSessionStatManagerIpAddr": apexRpcSessionStatManagerIpAddr,
       "apexRpcQamStatTable": apexRpcQamStatTable,
       "apexRpcQamStatEntry": apexRpcQamStatEntry,
       "apexRpcQamStatQamChannelNum": apexRpcQamStatQamChannelNum,
       "apexRpcQamStatNumSdvSessions": apexRpcQamStatNumSdvSessions,
       "apexRpcQamStatNumVodBcSessions": apexRpcQamStatNumVodBcSessions,
       "apexRpcQamStatSdvGroupBandwidth": apexRpcQamStatSdvGroupBandwidth,
       "apexRtsp": apexRtsp,
       "apexRtspConfig": apexRtspConfig,
       "apexRtspConfigGeneral": apexRtspConfigGeneral,
       "apexRtspReportGbeInterfaces": apexRtspReportGbeInterfaces,
       "apexRtspConfControllerApplyTable": apexRtspConfControllerApplyTable,
       "apexRtspConfControllerApplyEntry": apexRtspConfControllerApplyEntry,
       "apexRtspConfControllerApplyNum": apexRtspConfControllerApplyNum,
       "apexRtspConfControllerApplyChange": apexRtspConfControllerApplyChange,
       "apexRtspConfControllerTable": apexRtspConfControllerTable,
       "apexRtspConfControllerEntry": apexRtspConfControllerEntry,
       "apexRtspConfControllerNum": apexRtspConfControllerNum,
       "apexRtspConfControllerIp": apexRtspConfControllerIp,
       "apexRtspConfControllerPort": apexRtspConfControllerPort,
       "apexRtspConfControllerHoldTime": apexRtspConfControllerHoldTime,
       "apexRtspConfControllerBandwidthDelta": apexRtspConfControllerBandwidthDelta,
       "apexRtspConfControlNamesTable": apexRtspConfControlNamesTable,
       "apexRtspConfControlNamesEntry": apexRtspConfControlNamesEntry,
       "apexRtspConfControlNamesNum": apexRtspConfControlNamesNum,
       "apexRtspConfControlNamesStreamingZone": apexRtspConfControlNamesStreamingZone,
       "apexRtspConfControlNamesDeviceName": apexRtspConfControlNamesDeviceName,
       "apexRtspConfQamChannelApplyTable": apexRtspConfQamChannelApplyTable,
       "apexRtspConfQamChannelApplyEntry": apexRtspConfQamChannelApplyEntry,
       "apexRtspConfQamChannelApplyNum": apexRtspConfQamChannelApplyNum,
       "apexRtspConfQamChannelApplyChange": apexRtspConfQamChannelApplyChange,
       "apexRtspConfQamChannelTable": apexRtspConfQamChannelTable,
       "apexRtspConfQamChannelEntry": apexRtspConfQamChannelEntry,
       "apexRtspConfQamChannelNum": apexRtspConfQamChannelNum,
       "apexRtspConfQamChannelGroupName": apexRtspConfQamChannelGroupName,
       "apexRtspConfGbeEdgeGroupTable": apexRtspConfGbeEdgeGroupTable,
       "apexRtspConfGbeEdgeGroupEntry": apexRtspConfGbeEdgeGroupEntry,
       "apexRtspConfGbeEdgeGroupNum": apexRtspConfGbeEdgeGroupNum,
       "apexRtspConfGbeEdgeGroupName": apexRtspConfGbeEdgeGroupName,
       "apexRtspConfMhaTable": apexRtspConfMhaTable,
       "apexRtspConfMhaEntry": apexRtspConfMhaEntry,
       "apexRtspConfMhaNum": apexRtspConfMhaNum,
       "apexRtspConfMhaAddressDomain": apexRtspConfMhaAddressDomain,
       "apexRtspConfMhaPort": apexRtspConfMhaPort,
       "apexRtspConfMhaGeneral": apexRtspConfMhaGeneral,
       "apexRtspConfMhaUdpMapEnable": apexRtspConfMhaUdpMapEnable,
       "apexRtspConfMhaSbe": apexRtspConfMhaSbe,
       "apexRtspConfMhaSbeEncryptionMode": apexRtspConfMhaSbeEncryptionMode,
       "apexRtspConfMhaSbeCciLevel": apexRtspConfMhaSbeCciLevel,
       "apexRtspConfMhaSbeApsLevel": apexRtspConfMhaSbeApsLevel,
       "apexRtspConfMhaSbeCitSetting": apexRtspConfMhaSbeCitSetting,
       "apexRtspConfMhaSbeApplyChange": apexRtspConfMhaSbeApplyChange,
       "apexRtspStatus": apexRtspStatus,
       "apexRtspStatusGeneral": apexRtspStatusGeneral,
       "apexRtspSessionStatTable": apexRtspSessionStatTable,
       "apexRtspSessionStatEntry": apexRtspSessionStatEntry,
       "apexRtspSessionStatIndex": apexRtspSessionStatIndex,
       "apexRtspSessionStatInputTsIndex": apexRtspSessionStatInputTsIndex,
       "apexRtspSessionStatInputProgramNum": apexRtspSessionStatInputProgramNum,
       "apexRtspSessionStatOutputQamChannel": apexRtspSessionStatOutputQamChannel,
       "apexRtspSessionStatOutputProgramNum": apexRtspSessionStatOutputProgramNum,
       "apexRtspSessionStatProgramBandwidth": apexRtspSessionStatProgramBandwidth,
       "apexRtspSessionStatManagerIpAddr": apexRtspSessionStatManagerIpAddr,
       "apexRtspSessionIdTable": apexRtspSessionIdTable,
       "apexRtspSessionIdEntry": apexRtspSessionIdEntry,
       "apexRtspSessionIdIndex": apexRtspSessionIdIndex,
       "apexRtspSessionId": apexRtspSessionId,
       "apexRtspQamStatTable": apexRtspQamStatTable,
       "apexRtspQamStatEntry": apexRtspQamStatEntry,
       "apexRtspQamStatQamChannelNum": apexRtspQamStatQamChannelNum,
       "apexRtspQamStatNumSessions": apexRtspQamStatNumSessions,
       "apexRtspQamStatAllocatedBandwidth": apexRtspQamStatAllocatedBandwidth,
       "apexRtspStatControllerTable": apexRtspStatControllerTable,
       "apexRtspStatControllerEntry": apexRtspStatControllerEntry,
       "apexRtspStatControllerNum": apexRtspStatControllerNum,
       "apexRtspStatControllerDiscovery": apexRtspStatControllerDiscovery,
       "apexRtspStatControllerConnection": apexRtspStatControllerConnection,
       "apexRtspStatControllerCommFault": apexRtspStatControllerCommFault,
       "apexRtspStatQamChannelTable": apexRtspStatQamChannelTable,
       "apexRtspStatQamChannelEntry": apexRtspStatQamChannelEntry,
       "apexRtspStatQamChannelNum": apexRtspStatQamChannelNum,
       "apexRtspStatQamChannelName": apexRtspStatQamChannelName,
       "apexRtspStatQamMptsModeTable": apexRtspStatQamMptsModeTable,
       "apexRtspStatQamMptsModeEntry": apexRtspStatQamMptsModeEntry,
       "apexRtspStatQamMptsModeQamChannelNum": apexRtspStatQamMptsModeQamChannelNum,
       "apexRtspStatQamMptsModeQamChannelMode": apexRtspStatQamMptsModeQamChannelMode,
       "apexManualRouting": apexManualRouting,
       "apexManualRoutingConfig": apexManualRoutingConfig,
       "apexManualRoutingConfigGeneral": apexManualRoutingConfigGeneral,
       "apexManualRouteRmdClear": apexManualRouteRmdClear,
       "apexManualRouteApplyTable": apexManualRouteApplyTable,
       "apexManualRouteApplyEntry": apexManualRouteApplyEntry,
       "apexManualRouteApplyIndex": apexManualRouteApplyIndex,
       "apexManualRouteApplyChange": apexManualRouteApplyChange,
       "apexManualRouteTable": apexManualRouteTable,
       "apexManualRouteEntry": apexManualRouteEntry,
       "apexManualRouteIndex": apexManualRouteIndex,
       "apexManualRouteEnable": apexManualRouteEnable,
       "apexManualRouteInputType": apexManualRouteInputType,
       "apexManualRouteInputInterface": apexManualRouteInputInterface,
       "apexManualRouteInputUdp": apexManualRouteInputUdp,
       "apexManualRouteInputMulticastIp": apexManualRouteInputMulticastIp,
       "apexManualRouteInputSourceIp": apexManualRouteInputSourceIp,
       "apexManualRouteInputProgNum": apexManualRouteInputProgNum,
       "apexManualRouteInputPreEncryptCheck": apexManualRouteInputPreEncryptCheck,
       "apexManualRouteOutputTsNum": apexManualRouteOutputTsNum,
       "apexManualRouteOutputProgNum": apexManualRouteOutputProgNum,
       "apexManualRouteOutputEncryptMode": apexManualRouteOutputEncryptMode,
       "apexManualRouteOutputCopyProtectSource": apexManualRouteOutputCopyProtectSource,
       "apexManualRouteSourceId": apexManualRouteSourceId,
       "apexManualRouteProviderId": apexManualRouteProviderId,
       "apexManRtePassThroughApplyTable": apexManRtePassThroughApplyTable,
       "apexManRtePassThroughApplyEntry": apexManRtePassThroughApplyEntry,
       "apexManRtePassThroughApplyOutputTsNum": apexManRtePassThroughApplyOutputTsNum,
       "apexManRtePassThroughApplyChange": apexManRtePassThroughApplyChange,
       "apexManRtePassThroughTable": apexManRtePassThroughTable,
       "apexManRtePassThroughEntry": apexManRtePassThroughEntry,
       "apexManRtePassThroughOutputTsNum": apexManRtePassThroughOutputTsNum,
       "apexManRtePassThroughEnable": apexManRtePassThroughEnable,
       "apexManRtePassThroughInputType": apexManRtePassThroughInputType,
       "apexManRtePassThroughInputInterface": apexManRtePassThroughInputInterface,
       "apexManRtePassThroughInputUdp": apexManRtePassThroughInputUdp,
       "apexManRtePassThroughInputMulticastIp": apexManRtePassThroughInputMulticastIp,
       "apexManRtePassThroughInputSourceIp": apexManRtePassThroughInputSourceIp,
       "apexManualRouteGbeInputRedundConfig": apexManualRouteGbeInputRedundConfig,
       "apexManRteGbeInRedConfigGeneral": apexManRteGbeInRedConfigGeneral,
       "apexManRteGbeInRedApplyTable": apexManRteGbeInRedApplyTable,
       "apexManRteGbeInRedApplyEntry": apexManRteGbeInRedApplyEntry,
       "apexManRteGbeInRedApplyIndex": apexManRteGbeInRedApplyIndex,
       "apexManRteGbeInRedApplyChange": apexManRteGbeInRedApplyChange,
       "apexManRteGbeInRedTable": apexManRteGbeInRedTable,
       "apexManRteGbeInRedEntry": apexManRteGbeInRedEntry,
       "apexManRteGbeInRedIndex": apexManRteGbeInRedIndex,
       "apexManRteGbeInRedPriInterface": apexManRteGbeInRedPriInterface,
       "apexManRteGbeInRedPriUdp": apexManRteGbeInRedPriUdp,
       "apexManRteGbeInRedPriMulticastIp": apexManRteGbeInRedPriMulticastIp,
       "apexManRteGbeInRedPriSourceIp": apexManRteGbeInRedPriSourceIp,
       "apexManRteGbeInRedPriLowAlarmBitRate": apexManRteGbeInRedPriLowAlarmBitRate,
       "apexManRteGbeInRedPriHighAlarmBitRate": apexManRteGbeInRedPriHighAlarmBitRate,
       "apexManRteGbeInRedRateCompareType": apexManRteGbeInRedRateCompareType,
       "apexManRteGbeInRedEnable": apexManRteGbeInRedEnable,
       "apexManRteGbeInRedThreshold": apexManRteGbeInRedThreshold,
       "apexManRteGbeInRedSuspend": apexManRteGbeInRedSuspend,
       "apexManRteGbeInRedSecInterface": apexManRteGbeInRedSecInterface,
       "apexManRteGbeInRedSecUdp": apexManRteGbeInRedSecUdp,
       "apexManRteGbeInRedSecMulticastIp": apexManRteGbeInRedSecMulticastIp,
       "apexManRteGbeInRedSecSourceIp": apexManRteGbeInRedSecSourceIp,
       "apexManRteGbeInRedSecLowAlarmBitRate": apexManRteGbeInRedSecLowAlarmBitRate,
       "apexManRteGbeInRedSecHighAlarmBitRate": apexManRteGbeInRedSecHighAlarmBitRate,
       "apexManRteGbeInRedSecRedundMcJoin": apexManRteGbeInRedSecRedundMcJoin,
       "apexManRteGbeInRedForceSwitchTable": apexManRteGbeInRedForceSwitchTable,
       "apexManRteGbeInRedForceSwitchEntry": apexManRteGbeInRedForceSwitchEntry,
       "apexManRteGbeInRedForceSwitchIndex": apexManRteGbeInRedForceSwitchIndex,
       "apexManRteGbeInRedForceSwitch": apexManRteGbeInRedForceSwitch,
       "apexManualRoutingStatus": apexManualRoutingStatus,
       "apexManualRoutingStatusGeneral": apexManualRoutingStatusGeneral,
       "apexManualRouteInvalidApplyText": apexManualRouteInvalidApplyText,
       "apexManRtePassThroughInvalidApplyText": apexManRtePassThroughInvalidApplyText,
       "apexManRteGbeInRedInvalidApplyText": apexManRteGbeInRedInvalidApplyText,
       "apexManualRouteGbeInputRedundStatus": apexManualRouteGbeInputRedundStatus,
       "apexManRteGbeInRedStatusGeneral": apexManRteGbeInRedStatusGeneral,
       "apexManRteGbeInRedStatusMapTable": apexManRteGbeInRedStatusMapTable,
       "apexManRteGbeInRedStatusMapEntry": apexManRteGbeInRedStatusMapEntry,
       "apexManRteGbeInRedStatusMapIndex": apexManRteGbeInRedStatusMapIndex,
       "apexManRteGbeInRedStatusMapInputTsStatRow": apexManRteGbeInRedStatusMapInputTsStatRow,
       "apexAncillaryPidMapping": apexAncillaryPidMapping,
       "apexPidMapConfig": apexPidMapConfig,
       "apexPidMapTable": apexPidMapTable,
       "apexPidMapEntry": apexPidMapEntry,
       "apexPidMapIndex": apexPidMapIndex,
       "apexPidMapEnable": apexPidMapEnable,
       "apexPidMapInputType": apexPidMapInputType,
       "apexPidMapInputInterface": apexPidMapInputInterface,
       "apexPidMapInputUdp": apexPidMapInputUdp,
       "apexPidMapInputMulticastIp": apexPidMapInputMulticastIp,
       "apexPidMapInputSourceIp": apexPidMapInputSourceIp,
       "apexPidMapInputPid": apexPidMapInputPid,
       "apexPidMapOutputTsNum": apexPidMapOutputTsNum,
       "apexPidMapOutputPid": apexPidMapOutputPid,
       "apexPidMapApplyTable": apexPidMapApplyTable,
       "apexPidMapApplyEntry": apexPidMapApplyEntry,
       "apexPidMapApplyIndex": apexPidMapApplyIndex,
       "apexPidMapApplyChange": apexPidMapApplyChange,
       "apexPidMapStatus": apexPidMapStatus,
       "apexPidMapStatusGeneral": apexPidMapStatusGeneral,
       "apexPidMapMaxPidMappings": apexPidMapMaxPidMappings,
       "apexPidMapInvalidApplyText": apexPidMapInvalidApplyText,
       "apexInsertion": apexInsertion,
       "apexInsertionConfig": apexInsertionConfig,
       "apexInsertionConfigGeneral": apexInsertionConfigGeneral,
       "apexInsertionMode": apexInsertionMode,
       "apexInsertionStatus": apexInsertionStatus,
       "apexInsertionStatusGeneral": apexInsertionStatusGeneral,
       "apexInsertPacketStatisticsTable": apexInsertPacketStatisticsTable,
       "apexInsertPacketStatisticsEntry": apexInsertPacketStatisticsEntry,
       "apexInsertPacketStatOutputTsNum": apexInsertPacketStatOutputTsNum,
       "apexInsertPacketStatTotPkts": apexInsertPacketStatTotPkts,
       "apexInsertPacketStatNumPkts": apexInsertPacketStatNumPkts,
       "apexInputTransport": apexInputTransport,
       "apexInputTsConfig": apexInputTsConfig,
       "apexInputTsConfigGeneral": apexInputTsConfigGeneral,
       "apexInputTsStatus": apexInputTsStatus,
       "apexInputTsStatusGeneral": apexInputTsStatusGeneral,
       "apexInputTsStatTable": apexInputTsStatTable,
       "apexInputTsStatEntry": apexInputTsStatEntry,
       "apexInputTsStatIndex": apexInputTsStatIndex,
       "apexInputTsStatStreamInUse": apexInputTsStatStreamInUse,
       "apexInputTsStatInputType": apexInputTsStatInputType,
       "apexInputTsStatRoutingType": apexInputTsStatRoutingType,
       "apexInputTsStatPriState": apexInputTsStatPriState,
       "apexInputTsStatPriInputInterface": apexInputTsStatPriInputInterface,
       "apexInputTsStatPriInputUdp": apexInputTsStatPriInputUdp,
       "apexInputTsStatPriInputMulticastIp": apexInputTsStatPriInputMulticastIp,
       "apexInputTsStatPriInputSourceIp": apexInputTsStatPriInputSourceIp,
       "apexInputTsStatSecState": apexInputTsStatSecState,
       "apexInputTsStatSecInputInterface": apexInputTsStatSecInputInterface,
       "apexInputTsStatSecInputUdp": apexInputTsStatSecInputUdp,
       "apexInputTsStatSecInputMulticastIp": apexInputTsStatSecInputMulticastIp,
       "apexInputTsStatSecInputSourceIp": apexInputTsStatSecInputSourceIp,
       "apexInputTsStatRateCompareType": apexInputTsStatRateCompareType,
       "apexOutputTransport": apexOutputTransport,
       "apexOutputTsConfig": apexOutputTsConfig,
       "apexOutputTsConfigGeneral": apexOutputTsConfigGeneral,
       "apexOutputTsUtilizationMonitoring": apexOutputTsUtilizationMonitoring,
       "apexOutputTsUtilizationMonitorGeneral": apexOutputTsUtilizationMonitorGeneral,
       "apexOutputTsUtilMonAlarmThreshold": apexOutputTsUtilMonAlarmThreshold,
       "apexOutputTsUtilMonSetAlarmDelay": apexOutputTsUtilMonSetAlarmDelay,
       "apexOutputTsUtilMonClearAlarmDelay": apexOutputTsUtilMonClearAlarmDelay,
       "apexOutputTsUtilizationMonitorTable": apexOutputTsUtilizationMonitorTable,
       "apexOutputTsUtilizationMonitorEntry": apexOutputTsUtilizationMonitorEntry,
       "apexOutputTsUtilMonOutputTsNum": apexOutputTsUtilMonOutputTsNum,
       "apexOutputTsUtilMonResetTotDropPacket": apexOutputTsUtilMonResetTotDropPacket,
       "apexOutputTsConfApplyTable": apexOutputTsConfApplyTable,
       "apexOutputTsConfApplyEntry": apexOutputTsConfApplyEntry,
       "apexOutputTsConfApplyIndex": apexOutputTsConfApplyIndex,
       "apexOutputTsConfApplyChange": apexOutputTsConfApplyChange,
       "apexOutputTsConfigTable": apexOutputTsConfigTable,
       "apexOutputTsConfigEntry": apexOutputTsConfigEntry,
       "apexOutputTsConfOutputTsNum": apexOutputTsConfOutputTsNum,
       "apexOutputTsConfPidRemappingMode": apexOutputTsConfPidRemappingMode,
       "apexOutputTsConfOperatingMode": apexOutputTsConfOperatingMode,
       "apexOutputTsConfOutPatTsId": apexOutputTsConfOutPatTsId,
       "apexOutputTsConfPsipEnable": apexOutputTsConfPsipEnable,
       "apexOutputTsConfEncryptionType": apexOutputTsConfEncryptionType,
       "apexOutputTsConfSimulcryptMode": apexOutputTsConfSimulcryptMode,
       "apexOutputTsConfPcrLess": apexOutputTsConfPcrLess,
       "apexOutputTsStatus": apexOutputTsStatus,
       "apexOutputTsStatusGeneral": apexOutputTsStatusGeneral,
       "apexOutputTsStatusInvalidApplyText": apexOutputTsStatusInvalidApplyText,
       "apexOutputTsUtilization": apexOutputTsUtilization,
       "apexOutputTsUtilizationGeneral": apexOutputTsUtilizationGeneral,
       "apexOutputTsUtilizationSamplePeriod": apexOutputTsUtilizationSamplePeriod,
       "apexOutputTsUtilizationTable": apexOutputTsUtilizationTable,
       "apexOutputTsUtilizationEntry": apexOutputTsUtilizationEntry,
       "apexOutputTsUtilizOutpuTsNum": apexOutputTsUtilizOutpuTsNum,
       "apexOutputTsUtilizDataFlag": apexOutputTsUtilizDataFlag,
       "apexOutputTsUtilizNumSamples": apexOutputTsUtilizNumSamples,
       "apexOutputTsUtilizThreshold": apexOutputTsUtilizThreshold,
       "apexOutputTsUtilizTime": apexOutputTsUtilizTime,
       "apexOutputTsUtilizCurPercent": apexOutputTsUtilizCurPercent,
       "apexOutputTsUtilizAvgPercent": apexOutputTsUtilizAvgPercent,
       "apexOutputTsUtilizMinPercent": apexOutputTsUtilizMinPercent,
       "apexOutputTsUtilizPeakPercent": apexOutputTsUtilizPeakPercent,
       "apexOutputTsUtilizCurRate": apexOutputTsUtilizCurRate,
       "apexOutputTsUtilizAvgRate": apexOutputTsUtilizAvgRate,
       "apexOutputTsUtilizMinRate": apexOutputTsUtilizMinRate,
       "apexOutputTsUtilizPeakRate": apexOutputTsUtilizPeakRate,
       "apexOutputTsUtilizOverflow": apexOutputTsUtilizOverflow,
       "apexOutputTsUtilizCurDropPackets": apexOutputTsUtilizCurDropPackets,
       "apexOutputTsUtilizPeakDropPackets": apexOutputTsUtilizPeakDropPackets,
       "apexOutputTsUtilizRollingDropPackets": apexOutputTsUtilizRollingDropPackets,
       "apexOutputTsUtilizTotalDropPackets": apexOutputTsUtilizTotalDropPackets,
       "apexOutputTsUtilizThresholdAlarm": apexOutputTsUtilizThresholdAlarm,
       "apexOutputTsUtilizOverflowAlarm": apexOutputTsUtilizOverflowAlarm,
       "apexOutputTsStatusTable": apexOutputTsStatusTable,
       "apexOutputTsStatusEntry": apexOutputTsStatusEntry,
       "apexOutputTsStatusOutputTsNum": apexOutputTsStatusOutputTsNum,
       "apexOutputTsStatusProgramsPerTs": apexOutputTsStatusProgramsPerTs,
       "apexOutputTsStatusServicesMapped": apexOutputTsStatusServicesMapped,
       "apexOutputTsStatusAncillaryPidsMapped": apexOutputTsStatusAncillaryPidsMapped,
       "apexOutputTsStatusInputStreamsMapped": apexOutputTsStatusInputStreamsMapped,
       "apexOutputTsStatusFault": apexOutputTsStatusFault,
       "apexOutputTsStatusServicesInError": apexOutputTsStatusServicesInError,
       "apexOutputTsStatusDepiSessionsMapped": apexOutputTsStatusDepiSessionsMapped,
       "apexOutputTsStatusMessageGenerationNum": apexOutputTsStatusMessageGenerationNum,
       "apexOutputTsStatusScgsProvisioned": apexOutputTsStatusScgsProvisioned,
       "apexOutputTsStatusServicesMuxed": apexOutputTsStatusServicesMuxed,
       "apexPsi": apexPsi,
       "apexPsiConfig": apexPsiConfig,
       "apexPsiConfigGeneral": apexPsiConfigGeneral,
       "apexPsiDetectionEnabled": apexPsiDetectionEnabled,
       "apexPsiDetectionTimeout": apexPsiDetectionTimeout,
       "apexPsiRangeStart": apexPsiRangeStart,
       "apexPsiRangeStop": apexPsiRangeStop,
       "apexPatVersionIncrement": apexPatVersionIncrement,
       "apexPmtVersionIncrement": apexPmtVersionIncrement,
       "apexEcmEmmFirstPid": apexEcmEmmFirstPid,
       "apexEcmEmmNumberPids": apexEcmEmmNumberPids,
       "apexProgramBasedPmtOffset": apexProgramBasedPmtOffset,
       "apexPsiStatus": apexPsiStatus,
       "apexPsiStatusGeneral": apexPsiStatusGeneral,
       "apexPsiStatusTable": apexPsiStatusTable,
       "apexPsiStatusEntry": apexPsiStatusEntry,
       "apexPsiStatusTableType": apexPsiStatusTableType,
       "apexPsiStatusIndex": apexPsiStatusIndex,
       "apexPsiStatusPid": apexPsiStatusPid,
       "apexPsiStatusMessageType": apexPsiStatusMessageType,
       "apexPsiStatusProgramNumber": apexPsiStatusProgramNumber,
       "apexPsiStatusSegment": apexPsiStatusSegment,
       "apexPsiStatusPart": apexPsiStatusPart,
       "apexPsiStatusBody": apexPsiStatusBody,
       "apexPsiStatusGpsTime": apexPsiStatusGpsTime,
       "apexOutputProgram": apexOutputProgram,
       "apexOutputProgramConfig": apexOutputProgramConfig,
       "apexOutputProgramConfigGeneral": apexOutputProgramConfigGeneral,
       "apexOutputProgramStatus": apexOutputProgramStatus,
       "apexOutputProgramStatusGeneral": apexOutputProgramStatusGeneral,
       "apexOutputProgramTable": apexOutputProgramTable,
       "apexOutputProgramEntry": apexOutputProgramEntry,
       "apexOutputProgramIndex": apexOutputProgramIndex,
       "apexOutputProgramInputTsIndex": apexOutputProgramInputTsIndex,
       "apexOutputProgramInputProgNum": apexOutputProgramInputProgNum,
       "apexOutputProgramOutputProgNum": apexOutputProgramOutputProgNum,
       "apexOutputProgramRoutingStatus": apexOutputProgramRoutingStatus,
       "apexOutputProgramInputPreEncrypted": apexOutputProgramInputPreEncrypted,
       "apexOutputProgramOutputTsNum": apexOutputProgramOutputTsNum,
       "apexOutputProgramError": apexOutputProgramError,
       "apexOutputProgramEncryptionMode": apexOutputProgramEncryptionMode,
       "apexOutputProgramEncryptionStatus": apexOutputProgramEncryptionStatus,
       "apexOutputProgramEcmServiceId": apexOutputProgramEcmServiceId,
       "apexOutputProgramCciLevel": apexOutputProgramCciLevel,
       "apexOutputProgramApsLevel": apexOutputProgramApsLevel,
       "apexOutputProgramCitSetting": apexOutputProgramCitSetting,
       "apexOutputProgramNumberTiers": apexOutputProgramNumberTiers,
       "apexOutputProgramTierData": apexOutputProgramTierData,
       "apexOutputProgramSourceId": apexOutputProgramSourceId,
       "apexOutputProgramProviderId": apexOutputProgramProviderId,
       "apexOutputProgramProgramType": apexOutputProgramProgramType,
       "apexOutputProgramDtaEncryptionMode": apexOutputProgramDtaEncryptionMode,
       "apexAcp": apexAcp,
       "apexAcpConfig": apexAcpConfig,
       "apexAcpConfigGeneral": apexAcpConfigGeneral,
       "apexAcpStatus": apexAcpStatus,
       "apexAcpStatusGeneral": apexAcpStatusGeneral,
       "apexAcpStatusTable": apexAcpStatusTable,
       "apexAcpStatusEntry": apexAcpStatusEntry,
       "apexAcpStatusIndex": apexAcpStatusIndex,
       "apexAcpUnitAddress": apexAcpUnitAddress,
       "apexAcpHealthByte": apexAcpHealthByte,
       "apexAcpEvenCsn": apexAcpEvenCsn,
       "apexAcpOddCsn": apexAcpOddCsn,
       "apexAcpUnitAttribute": apexAcpUnitAttribute,
       "apexUdpPortMapping": apexUdpPortMapping,
       "apexUdpMapConfig": apexUdpMapConfig,
       "apexUdpMapConfigGeneral": apexUdpMapConfigGeneral,
       "apexUdpMapPreEncryptCheck": apexUdpMapPreEncryptCheck,
       "apexUdpMapModeBits": apexUdpMapModeBits,
       "apexUdpMapTsOffset": apexUdpMapTsOffset,
       "apexUdpMapFollowDtcp": apexUdpMapFollowDtcp,
       "apexUdpMapApplyTable": apexUdpMapApplyTable,
       "apexUdpMapApplyEntry": apexUdpMapApplyEntry,
       "apexUdpMapApplyOutputTsNum": apexUdpMapApplyOutputTsNum,
       "apexUdpMapApplyChange": apexUdpMapApplyChange,
       "apexUdpMapTable": apexUdpMapTable,
       "apexUdpMapEntry": apexUdpMapEntry,
       "apexUdpMapOutputTsNum": apexUdpMapOutputTsNum,
       "apexUdpMapInputInterface": apexUdpMapInputInterface,
       "apexUdpMapStartProgNum": apexUdpMapStartProgNum,
       "apexUdpMapNumberProgs": apexUdpMapNumberProgs,
       "apexUdpMapMulticastTable": apexUdpMapMulticastTable,
       "apexUdpMapMulticastEntry": apexUdpMapMulticastEntry,
       "apexUdpMapMulticastIndex": apexUdpMapMulticastIndex,
       "apexUdpMapMulticastEnable": apexUdpMapMulticastEnable,
       "apexUdpMapMulticastInterface": apexUdpMapMulticastInterface,
       "apexUdpMapMulticastUdp": apexUdpMapMulticastUdp,
       "apexUdpMapMulticastMcastIp": apexUdpMapMulticastMcastIp,
       "apexUdpMapMulticastSourceIp": apexUdpMapMulticastSourceIp,
       "apexUdpMapMulticastApplyTable": apexUdpMapMulticastApplyTable,
       "apexUdpMapMulticastApplyEntry": apexUdpMapMulticastApplyEntry,
       "apexUdpMapMulticastApplyIndex": apexUdpMapMulticastApplyIndex,
       "apexUdpMapMulticastApplyChange": apexUdpMapMulticastApplyChange,
       "apexUdpMapStatus": apexUdpMapStatus,
       "apexUdpMapStatusGeneral": apexUdpMapStatusGeneral,
       "apexUdpMapMulticastInvalidApplyText": apexUdpMapMulticastInvalidApplyText,
       "apexUdpMapStatusTable": apexUdpMapStatusTable,
       "apexUdpMapStatusEntry": apexUdpMapStatusEntry,
       "apexUdpMapStatusOutputTsNum": apexUdpMapStatusOutputTsNum,
       "apexUdpMapInvalidApplyText": apexUdpMapInvalidApplyText,
       "apexRds": apexRds,
       "apexRdsConfig": apexRdsConfig,
       "apexRdsConfigGeneral": apexRdsConfigGeneral,
       "apexRdsIpAddr": apexRdsIpAddr,
       "apexRdsTcpPort": apexRdsTcpPort,
       "apexRdsProgramEpochDuration": apexRdsProgramEpochDuration,
       "apexRdsCetPollInterval": apexRdsCetPollInterval,
       "apexRdsCetRefresh": apexRdsCetRefresh,
       "apexRdsRmdPollInterval": apexRdsRmdPollInterval,
       "apexRdsRmdRefresh": apexRdsRmdRefresh,
       "apexRdsPollRandomization": apexRdsPollRandomization,
       "apexRdsSetDefault": apexRdsSetDefault,
       "apexRdsErrorCountReset": apexRdsErrorCountReset,
       "apexRdsConfigApplyChange": apexRdsConfigApplyChange,
       "apexRdsConfigRds2Enable": apexRdsConfigRds2Enable,
       "apexRdsConfigServerUrl": apexRdsConfigServerUrl,
       "apexRdsInitialEcmRetryInterval": apexRdsInitialEcmRetryInterval,
       "apexRdsStatus": apexRdsStatus,
       "apexRdsStatusGeneral": apexRdsStatusGeneral,
       "apexRdsConnectionStatus": apexRdsConnectionStatus,
       "apexRdsCurrentCsn": apexRdsCurrentCsn,
       "apexRdsCetNextPollTime": apexRdsCetNextPollTime,
       "apexRdsRmdNextPollTime": apexRdsRmdNextPollTime,
       "apexRdsEmmStatusTableSize": apexRdsEmmStatusTableSize,
       "apexRdsProgramMessagesReceived": apexRdsProgramMessagesReceived,
       "apexRdsProgramMessagesFailed": apexRdsProgramMessagesFailed,
       "apexRdsCommErrorCount": apexRdsCommErrorCount,
       "apexRdsCommStatus": apexRdsCommStatus,
       "apexRdsFlashWriteCount": apexRdsFlashWriteCount,
       "apexRdsMcast16": apexRdsMcast16,
       "apexRdsStatusServerIp": apexRdsStatusServerIp,
       "apexRdsStatusServerPort": apexRdsStatusServerPort,
       "apexRdsStatusServerRootDirPath": apexRdsStatusServerRootDirPath,
       "apexRdsStatusValidation": apexRdsStatusValidation,
       "apexRdsEmmStatusTable": apexRdsEmmStatusTable,
       "apexRdsEmmStatusEntry": apexRdsEmmStatusEntry,
       "apexRdsEmmStatusIndex": apexRdsEmmStatusIndex,
       "apexRdsEmmStatusCsn": apexRdsEmmStatusCsn,
       "apexRdsEmmStatusState": apexRdsEmmStatusState,
       "apexRdsEmmStatusGpsTime": apexRdsEmmStatusGpsTime,
       "apexRdsEmmStatusServerError": apexRdsEmmStatusServerError,
       "apexRdsEmmStatusUnitAddress": apexRdsEmmStatusUnitAddress,
       "apexRdsSourceLookupTable": apexRdsSourceLookupTable,
       "apexRdsSourceLookupEntry": apexRdsSourceLookupEntry,
       "apexRdsSourceLookupIndex": apexRdsSourceLookupIndex,
       "apexRdsSourceLookupDescription": apexRdsSourceLookupDescription,
       "apexRdsSourceLookupSourceId": apexRdsSourceLookupSourceId,
       "apexRdsSourceLookupProviderId": apexRdsSourceLookupProviderId,
       "apexRdsEventTable": apexRdsEventTable,
       "apexRdsEventEntry": apexRdsEventEntry,
       "apexRdsEventProgramIndex": apexRdsEventProgramIndex,
       "apexRdsEventEventIndex": apexRdsEventEventIndex,
       "apexRdsEventEpochNumber": apexRdsEventEpochNumber,
       "apexRdsEventEpochStart": apexRdsEventEpochStart,
       "apexRdsEventEpochEnd": apexRdsEventEpochEnd,
       "apexRdsEventInterstitialDuration": apexRdsEventInterstitialDuration,
       "apexRdsEventPreviewDuration": apexRdsEventPreviewDuration,
       "apexRdsEventPurchaseDuration": apexRdsEventPurchaseDuration,
       "apexRdsEventNumberTiers": apexRdsEventNumberTiers,
       "apexRdsEventTierData": apexRdsEventTierData,
       "apexRdsEventProgramCost": apexRdsEventProgramCost,
       "apexRdsEventRatingRegion": apexRdsEventRatingRegion,
       "apexRdsEventRatingData": apexRdsEventRatingData,
       "apexRdsEventRatingText": apexRdsEventRatingText,
       "apexRdsEventControlByte": apexRdsEventControlByte,
       "apexRdsEventPrkmWkemAvailable": apexRdsEventPrkmWkemAvailable,
       "apexRdsEventCcmAvailable": apexRdsEventCcmAvailable,
       "apexEncryption": apexEncryption,
       "apexEncryptionConfig": apexEncryptionConfig,
       "apexEncryptionConfigGeneral": apexEncryptionConfigGeneral,
       "apexEncryptionConfAlgorithm": apexEncryptionConfAlgorithm,
       "apexSimulcryptExternalEisSetting": apexSimulcryptExternalEisSetting,
       "apexSimulcryptEmEnable": apexSimulcryptEmEnable,
       "apexCteConfig": apexCteConfig,
       "apexCteEncryptionMode": apexCteEncryptionMode,
       "apexCteCciLevel": apexCteCciLevel,
       "apexCteApsLevel": apexCteApsLevel,
       "apexCteCitEnable": apexCteCitEnable,
       "apexCteCommonTier": apexCteCommonTier,
       "apexCteApplyChange": apexCteApplyChange,
       "apexEncryptionStatus": apexEncryptionStatus,
       "apexEncryptionStatusGeneral": apexEncryptionStatusGeneral,
       "apexEncryptionStatAlgorithm": apexEncryptionStatAlgorithm,
       "apexEncryptionCwgStatus": apexEncryptionCwgStatus,
       "apexEncryptionCwgPerSecond": apexEncryptionCwgPerSecond,
       "apexEncryptionMux1CollisionCount": apexEncryptionMux1CollisionCount,
       "apexEncryptionMux2CollisionCount": apexEncryptionMux2CollisionCount,
       "apexEncryptionMux1RolloverCount": apexEncryptionMux1RolloverCount,
       "apexEncryptionMux2RolloverCount": apexEncryptionMux2RolloverCount,
       "apexEncryptionEmmRequestsSent": apexEncryptionEmmRequestsSent,
       "apexEncryptionEmmGoodRepliesRecvd": apexEncryptionEmmGoodRepliesRecvd,
       "apexEncryptionEmmBadRepliesRecvd": apexEncryptionEmmBadRepliesRecvd,
       "apexEncryptionEmmGoodDeliveryTimeMs": apexEncryptionEmmGoodDeliveryTimeMs,
       "apexEncryptionEmmMaxDeliveryTimeMs": apexEncryptionEmmMaxDeliveryTimeMs,
       "apexEncryptionEmmMinDeliveryTimeMs": apexEncryptionEmmMinDeliveryTimeMs,
       "apexEncryptionMcDiagTable": apexEncryptionMcDiagTable,
       "apexEncryptionMcDiagEntry": apexEncryptionMcDiagEntry,
       "apexEncryptionMcDiagDeviceIndex": apexEncryptionMcDiagDeviceIndex,
       "apexEncryptionCwCountsPerSecond": apexEncryptionCwCountsPerSecond,
       "apexEas": apexEas,
       "apexEasConfig": apexEasConfig,
       "apexEasConfigGeneral": apexEasConfigGeneral,
       "apexEasApplyChange": apexEasApplyChange,
       "apexEasPhysInType": apexEasPhysInType,
       "apexEasPhysInPort": apexEasPhysInPort,
       "apexEasRcvUdpPort": apexEasRcvUdpPort,
       "apexEasMulticastIpAddress": apexEasMulticastIpAddress,
       "apexEasSourceIpAddress": apexEasSourceIpAddress,
       "apexEasOutputTable": apexEasOutputTable,
       "apexEasOutputEntry": apexEasOutputEntry,
       "apexEasOutputStreamNum": apexEasOutputStreamNum,
       "apexEasOutputEnable": apexEasOutputEnable,
       "apexEasServerApplyTable": apexEasServerApplyTable,
       "apexEasServerApplyEntry": apexEasServerApplyEntry,
       "apexEasServerApplyNum": apexEasServerApplyNum,
       "apexEasServerApplyChange": apexEasServerApplyChange,
       "apexEasServerTable": apexEasServerTable,
       "apexEasServerEntry": apexEasServerEntry,
       "apexEasServerNum": apexEasServerNum,
       "apexEasServerPhysInType": apexEasServerPhysInType,
       "apexEasServerPhysInPort": apexEasServerPhysInPort,
       "apexEasServerRcvUdpPort": apexEasServerRcvUdpPort,
       "apexEasServerMulticastIpAddress": apexEasServerMulticastIpAddress,
       "apexEasServerSourceIpAddress": apexEasServerSourceIpAddress,
       "apexEasStatus": apexEasStatus,
       "apexEasStatusGeneral": apexEasStatusGeneral,
       "apexEasNumRcvMsgs": apexEasNumRcvMsgs,
       "apexEasNumInvalRcvMsgs": apexEasNumInvalRcvMsgs,
       "apexChassisRedundancy": apexChassisRedundancy,
       "apexChassisRedundancyConfig": apexChassisRedundancyConfig,
       "apexChassisRedundancyConfigGeneral": apexChassisRedundancyConfigGeneral,
       "apexChassisRedundancyConfigEnable": apexChassisRedundancyConfigEnable,
       "apexChassisRedundancyMode": apexChassisRedundancyMode,
       "apexChassisRedundancyMulticastRedundancyMode": apexChassisRedundancyMulticastRedundancyMode,
       "apexChassisRedundancyUdpPort": apexChassisRedundancyUdpPort,
       "apexChassisRedundancyRedundantApexIp": apexChassisRedundancyRedundantApexIp,
       "apexChassisRedundancySuspend": apexChassisRedundancySuspend,
       "apexChassisRedundancyForceFailOver": apexChassisRedundancyForceFailOver,
       "apexChassisRedundancyFailOverGigE12LinkLoss": apexChassisRedundancyFailOverGigE12LinkLoss,
       "apexChassisRedundancyFailOverGigE34LinkLoss": apexChassisRedundancyFailOverGigE34LinkLoss,
       "apexChassisRedundancyFailOverEnet1LinkLoss": apexChassisRedundancyFailOverEnet1LinkLoss,
       "apexChassisRedundancyFailOverEnet2LinkLoss": apexChassisRedundancyFailOverEnet2LinkLoss,
       "apexChassisRedundancyFailOverTemperatureFault": apexChassisRedundancyFailOverTemperatureFault,
       "apexChassisRedundancyFailOverQamModuleFault": apexChassisRedundancyFailOverQamModuleFault,
       "apexChassisRedundancyFailOverQamRfPortFault": apexChassisRedundancyFailOverQamRfPortFault,
       "apexChassisRedundancyFailOverQamChannelFault": apexChassisRedundancyFailOverQamChannelFault,
       "apexChassisRedundancyConfigApplyChange": apexChassisRedundancyConfigApplyChange,
       "apexChassisRedundancyPrimaryStandbyOverride": apexChassisRedundancyPrimaryStandbyOverride,
       "apexChassisRedundancyRedundantApexSecIp": apexChassisRedundancyRedundantApexSecIp,
       "apexChassisRedundancyRedundantHBEnable": apexChassisRedundancyRedundantHBEnable,
       "apexChassisRedundancyStatus": apexChassisRedundancyStatus,
       "apexChassisRedundancyStatusGeneral": apexChassisRedundancyStatusGeneral,
       "apexChassisRedundancyPrimaryApexStatus": apexChassisRedundancyPrimaryApexStatus,
       "apexChassisRedundancySecondaryApexStatus": apexChassisRedundancySecondaryApexStatus,
       "apexChassisRedundancyState": apexChassisRedundancyState,
       "apexChassisRedundancyCommunicationStatus": apexChassisRedundancyCommunicationStatus,
       "apexChassisRedundancyConfigurationStatus": apexChassisRedundancyConfigurationStatus,
       "apexChassisRedundancyStatusInvalidApplyText": apexChassisRedundancyStatusInvalidApplyText,
       "apexChassisRedundancyGeneralConfigSyncStatusText": apexChassisRedundancyGeneralConfigSyncStatusText,
       "apexChassisRedundancyGigEMismatchStatus": apexChassisRedundancyGigEMismatchStatus,
       "apexChassisRedundancyQamMismatchStatus": apexChassisRedundancyQamMismatchStatus,
       "apexChassisRedundancyFirmwareMismatchStatus": apexChassisRedundancyFirmwareMismatchStatus,
       "apexChassisRedundancyGigE12LinkStatus": apexChassisRedundancyGigE12LinkStatus,
       "apexChassisRedundancyGigE34LinkStatus": apexChassisRedundancyGigE34LinkStatus,
       "apexChassisRedundancyCurrHBIntfIPStatus": apexChassisRedundancyCurrHBIntfIPStatus,
       "apexDta": apexDta,
       "apexDtaConfig": apexDtaConfig,
       "apexDtaGeneralConfig": apexDtaGeneralConfig,
       "apexDtaGeneralConfigCatSourceType": apexDtaGeneralConfigCatSourceType,
       "apexDtaGeneralConfigCatEmmPidMulticastIP": apexDtaGeneralConfigCatEmmPidMulticastIP,
       "apexDtaGeneralConfigCatEmmPidSourceIP": apexDtaGeneralConfigCatEmmPidSourceIP,
       "apexDtaGeneralConfigCatEmmPidUdpPort": apexDtaGeneralConfigCatEmmPidUdpPort,
       "apexDtaGeneralConfigCatEmmPidInterface": apexDtaGeneralConfigCatEmmPidInterface,
       "apexDtaGeneralConfigEmmPidNum": apexDtaGeneralConfigEmmPidNum,
       "apexDtaGeneralConfigApplyChange": apexDtaGeneralConfigApplyChange,
       "apexDtaGeneralConfigInvalidApplyText": apexDtaGeneralConfigInvalidApplyText,
       "apexDtaConfigApplyTable": apexDtaConfigApplyTable,
       "apexDtaConfigApplyEntry": apexDtaConfigApplyEntry,
       "apexDtaConfigApplyIndex": apexDtaConfigApplyIndex,
       "apexDtaConfigApplyChange": apexDtaConfigApplyChange,
       "apexDtaRfPortConfigTable": apexDtaRfPortConfigTable,
       "apexDtaRfPortConfigEntry": apexDtaRfPortConfigEntry,
       "apexDtaRfPortConfigIndex": apexDtaRfPortConfigIndex,
       "apexDtaRfPortConfigNetPidMulticastIP": apexDtaRfPortConfigNetPidMulticastIP,
       "apexDtaRfPortConfigNetPidSourceIP": apexDtaRfPortConfigNetPidSourceIP,
       "apexDtaRfPortConfigNetPidUdpPort": apexDtaRfPortConfigNetPidUdpPort,
       "apexDtaRfPortConfigNetPidInterface": apexDtaRfPortConfigNetPidInterface,
       "apexDtaRfPortConfigNetPidNum": apexDtaRfPortConfigNetPidNum,
       "apexDtaOtsConfigTable": apexDtaOtsConfigTable,
       "apexDtaOtsConfigEntry": apexDtaOtsConfigEntry,
       "apexDtaOtsConfigIndex": apexDtaOtsConfigIndex,
       "apexDtaOtsConfigEnable": apexDtaOtsConfigEnable,
       "apexDepi": apexDepi,
       "apexDepiConfig": apexDepiConfig,
       "apexDepiConfigGeneral": apexDepiConfigGeneral,
       "apexDepiConfigHostname": apexDepiConfigHostname,
       "apexDepiStatus": apexDepiStatus,
       "apexDepiStatusGeneral": apexDepiStatusGeneral,
       "apexDepiStatusGeneralDtiPort1LinkActive": apexDepiStatusGeneralDtiPort1LinkActive,
       "apexDepiStatusGeneralDtiPort2LinkActive": apexDepiStatusGeneralDtiPort2LinkActive,
       "apexDepiStatusGeneralDtiClientStatusMode": apexDepiStatusGeneralDtiClientStatusMode,
       "apexDepiStatusGeneralDtiClientPhaseError": apexDepiStatusGeneralDtiClientPhaseError,
       "apexDepiStatusGeneralDtiCurrentTimestamp": apexDepiStatusGeneralDtiCurrentTimestamp,
       "apexDepiStatusGeneralDtiPort1CableAdvanceValue": apexDepiStatusGeneralDtiPort1CableAdvanceValue,
       "apexDepiStatusGeneralDtiPort2CableAdvanceValue": apexDepiStatusGeneralDtiPort2CableAdvanceValue,
       "apexDepiControl": apexDepiControl,
       "apexDepiControlConfig": apexDepiControlConfig,
       "apexDepiControlConfigGeneral": apexDepiControlConfigGeneral,
       "apexDepiControlConfigGeneralKeepaliveTimeout": apexDepiControlConfigGeneralKeepaliveTimeout,
       "apexDepiControlConfigApplyTable": apexDepiControlConfigApplyTable,
       "apexDepiControlConfigApplyEntry": apexDepiControlConfigApplyEntry,
       "apexDepiControlConfigApplyIndex": apexDepiControlConfigApplyIndex,
       "apexDepiControlConfigApplyChange": apexDepiControlConfigApplyChange,
       "apexDepiControlConfigTable": apexDepiControlConfigTable,
       "apexDepiControlConfigEntry": apexDepiControlConfigEntry,
       "apexDepiControlConfigIndex": apexDepiControlConfigIndex,
       "apexDepiControlConfigEnable": apexDepiControlConfigEnable,
       "apexDepiControlConfigInterfaceNumber": apexDepiControlConfigInterfaceNumber,
       "apexDepiControlConfigSrcIpAddr": apexDepiControlConfigSrcIpAddr,
       "apexDepiControlConfigOverUdp": apexDepiControlConfigOverUdp,
       "apexDepiControlConfigType": apexDepiControlConfigType,
       "apexDepiControlStatus": apexDepiControlStatus,
       "apexDepiControlStatusGeneral": apexDepiControlStatusGeneral,
       "apexDepiControlStatusGeneralTotalConnections": apexDepiControlStatusGeneralTotalConnections,
       "apexDepiControlStatusGeneralCurrentConnections": apexDepiControlStatusGeneralCurrentConnections,
       "apexDepiControlStatusGeneralRejectedConnections": apexDepiControlStatusGeneralRejectedConnections,
       "apexDepiControlStatusGeneralUnknownConnectionMessages": apexDepiControlStatusGeneralUnknownConnectionMessages,
       "apexDepiControlStatusGeneralUnknownSessionMessages": apexDepiControlStatusGeneralUnknownSessionMessages,
       "apexDepiControlStatusGeneralInvalidApplyText": apexDepiControlStatusGeneralInvalidApplyText,
       "apexDepiControlStatusTable": apexDepiControlStatusTable,
       "apexDepiControlStatusEntry": apexDepiControlStatusEntry,
       "apexDepiControlStatusIndex": apexDepiControlStatusIndex,
       "apexDepiControlStatusLocalUdp": apexDepiControlStatusLocalUdp,
       "apexDepiControlStatusRemoteUdp": apexDepiControlStatusRemoteUdp,
       "apexDepiControlStatusConnectionStatus": apexDepiControlStatusConnectionStatus,
       "apexDepiControlStatusUnknownCtl": apexDepiControlStatusUnknownCtl,
       "apexDepiControlStatusMalformedCtl": apexDepiControlStatusMalformedCtl,
       "apexDepiControlStatusUnknownAvp": apexDepiControlStatusUnknownAvp,
       "apexDepiControlStatusMalformedAvp": apexDepiControlStatusMalformedAvp,
       "apexDepiControlStatusInvalidVendorId": apexDepiControlStatusInvalidVendorId,
       "apexDepiControlStatusHbitSet": apexDepiControlStatusHbitSet,
       "apexDepiControlStatusTotalSessions": apexDepiControlStatusTotalSessions,
       "apexDepiControlStatusCurrentSessions": apexDepiControlStatusCurrentSessions,
       "apexDepiControlStatusRejectedSessions": apexDepiControlStatusRejectedSessions,
       "apexDepiSession": apexDepiSession,
       "apexDepiSessionConfig": apexDepiSessionConfig,
       "apexDepiSessionConfigApplyTable": apexDepiSessionConfigApplyTable,
       "apexDepiSessionConfigApplyEntry": apexDepiSessionConfigApplyEntry,
       "apexDepiSessionConfigApplyOutputTsNum": apexDepiSessionConfigApplyOutputTsNum,
       "apexDepiSessionConfigApplyChange": apexDepiSessionConfigApplyChange,
       "apexDepiSessionConfigTable": apexDepiSessionConfigTable,
       "apexDepiSessionConfigEntry": apexDepiSessionConfigEntry,
       "apexDepiSessionConfigOutputTsNum": apexDepiSessionConfigOutputTsNum,
       "apexDepiSessionConfigEnable": apexDepiSessionConfigEnable,
       "apexDepiSessionConfigControlId": apexDepiSessionConfigControlId,
       "apexDepiSessionConfigDocsisTsid": apexDepiSessionConfigDocsisTsid,
       "apexDepiSessionConfigUdpPort": apexDepiSessionConfigUdpPort,
       "apexDepiSessionConfigSyncCorrection": apexDepiSessionConfigSyncCorrection,
       "apexDepiSessionStatus": apexDepiSessionStatus,
       "apexDepiSessionStatusGeneral": apexDepiSessionStatusGeneral,
       "apexDepiSessionStatusGeneralInvalidApplyText": apexDepiSessionStatusGeneralInvalidApplyText,
       "apexDepiSessionStatusTable": apexDepiSessionStatusTable,
       "apexDepiSessionStatusEntry": apexDepiSessionStatusEntry,
       "apexDepiSessionStatusIndex": apexDepiSessionStatusIndex,
       "apexDepiSessionStatusControlId": apexDepiSessionStatusControlId,
       "apexDepiSessionStatusOutputQAMChannel": apexDepiSessionStatusOutputQAMChannel,
       "apexDepiSessionStatusLocalUdp": apexDepiSessionStatusLocalUdp,
       "apexDepiSessionStatusRemoteUdp": apexDepiSessionStatusRemoteUdp,
       "apexDepiSessionStatusStatus": apexDepiSessionStatusStatus,
       "apexDepiSessionStatusPerHopBehavior": apexDepiSessionStatusPerHopBehavior,
       "apexDepiSessionStatusUnknownCtl": apexDepiSessionStatusUnknownCtl,
       "apexDepiSessionStatusMalformedCtl": apexDepiSessionStatusMalformedCtl,
       "apexDepiSessionStatusUnknownAvp": apexDepiSessionStatusUnknownAvp,
       "apexDepiSessionStatusMalformedAvp": apexDepiSessionStatusMalformedAvp,
       "apexDepiSessionStatusInvalidVendorId": apexDepiSessionStatusInvalidVendorId,
       "apexDepiSessionStatusHbitSet": apexDepiSessionStatusHbitSet,
       "apexDepiSessionStatusInSLIMsgs": apexDepiSessionStatusInSLIMsgs,
       "apexDepiSessionStatusOutSLIMsgs": apexDepiSessionStatusOutSLIMsgs,
       "apexDepiSessionStatusIngressDlmMsgs": apexDepiSessionStatusIngressDlmMsgs,
       "apexDepiSessionStatusEgressDlmMsgs": apexDepiSessionStatusEgressDlmMsgs,
       "apexDepiSessionStatusLatencyStart": apexDepiSessionStatusLatencyStart,
       "apexDepiSessionStatusLatencyEnd": apexDepiSessionStatusLatencyEnd,
       "apexDepiSessionStatusInDataPackets": apexDepiSessionStatusInDataPackets,
       "apexDepiSessionStatusInSequenceDiscards": apexDepiSessionStatusInSequenceDiscards,
       "apexDepiSessionStatusInDataPacketDiscards": apexDepiSessionStatusInDataPacketDiscards,
       "apexDepiSessionStatusSessionID": apexDepiSessionStatusSessionID,
       "apexPsip": apexPsip,
       "apexPsipConfig": apexPsipConfig,
       "apexPsipConfigGeneral": apexPsipConfigGeneral,
       "apexPsipConfigApplyChange": apexPsipConfigApplyChange,
       "apexPsipConfigMgtMsgInsertionPeriod": apexPsipConfigMgtMsgInsertionPeriod,
       "apexPsipConfigSttMsgInsertionPeriod": apexPsipConfigSttMsgInsertionPeriod,
       "apexPsipConfigCvctMsgInsertionPeriod": apexPsipConfigCvctMsgInsertionPeriod,
       "apexPsipConfigRrtMsgInsertionPeriod": apexPsipConfigRrtMsgInsertionPeriod,
       "apexPsipConfigEit0InsertionPeriod": apexPsipConfigEit0InsertionPeriod,
       "apexPsipConfigEit1InsertionPeriod": apexPsipConfigEit1InsertionPeriod,
       "apexPsipConfigEit2InsertionPeriod": apexPsipConfigEit2InsertionPeriod,
       "apexPsipConfigEit3InsertionPeriod": apexPsipConfigEit3InsertionPeriod,
       "apexPsipConfigTime": apexPsipConfigTime,
       "apexPsipConfigTimeApplyChange": apexPsipConfigTimeApplyChange,
       "apexPsipConfigTimeDsMonthIn": apexPsipConfigTimeDsMonthIn,
       "apexPsipConfigTimeDsDayIn": apexPsipConfigTimeDsDayIn,
       "apexPsipConfigTimeDsHourIn": apexPsipConfigTimeDsHourIn,
       "apexPsipConfigTimeDsMonthOut": apexPsipConfigTimeDsMonthOut,
       "apexPsipConfigTimeDsDayOut": apexPsipConfigTimeDsDayOut,
       "apexPsipConfigTimeDsHourOut": apexPsipConfigTimeDsHourOut,
       "apexPsipStatus": apexPsipStatus,
       "apexPsipStatusGeneral": apexPsipStatusGeneral,
       "apexPsipStatusInputTable": apexPsipStatusInputTable,
       "apexPsipStatusInputEntry": apexPsipStatusInputEntry,
       "apexPsipStatusInputIndex": apexPsipStatusInputIndex,
       "apexPsipStatusInputPid": apexPsipStatusInputPid,
       "apexPsipStatusInputMessageType": apexPsipStatusInputMessageType,
       "apexPsipStatusInputSourceId": apexPsipStatusInputSourceId,
       "apexPsipStatusInputSegment": apexPsipStatusInputSegment,
       "apexPsipStatusInputPart": apexPsipStatusInputPart,
       "apexPsipStatusInputBody": apexPsipStatusInputBody,
       "apexPsipStatusInputGpsTime": apexPsipStatusInputGpsTime,
       "apexPsipStatusInputInfo": apexPsipStatusInputInfo,
       "apexPsipStatusOutputTable": apexPsipStatusOutputTable,
       "apexPsipStatusOutputEntry": apexPsipStatusOutputEntry,
       "apexPsipStatusOutputIndex": apexPsipStatusOutputIndex,
       "apexPsipStatusOutputPid": apexPsipStatusOutputPid,
       "apexPsipStatusOutputMessageType": apexPsipStatusOutputMessageType,
       "apexPsipStatusOutputSourceId": apexPsipStatusOutputSourceId,
       "apexPsipStatusOutputSegment": apexPsipStatusOutputSegment,
       "apexPsipStatusOutputPart": apexPsipStatusOutputPart,
       "apexPsipStatusOutputBody": apexPsipStatusOutputBody,
       "apexPsipStatusOutputGpsTime": apexPsipStatusOutputGpsTime,
       "apexPsipStatusServiceTable": apexPsipStatusServiceTable,
       "apexPsipStatusServiceEntry": apexPsipStatusServiceEntry,
       "apexPsipStatusServiceIndex": apexPsipStatusServiceIndex,
       "apexPsipStatusServiceNum": apexPsipStatusServiceNum,
       "apexPsipStatusServiceOutputTs": apexPsipStatusServiceOutputTs,
       "apexPsipStatusServiceState": apexPsipStatusServiceState,
       "apexPsipStatusServiceSourceId": apexPsipStatusServiceSourceId,
       "apexPreencryption": apexPreencryption,
       "apexPreencryptionConfig": apexPreencryptionConfig,
       "apexPreencryptionConfigGeneral": apexPreencryptionConfigGeneral,
       "apexSupportPreencryptedSimulcrypt": apexSupportPreencryptedSimulcrypt,
       "apexAlarms": apexAlarms,
       "apexAlarmHardwareFault": apexAlarmHardwareFault,
       "apexAlarmInvalidInitData": apexAlarmInvalidInitData,
       "apexAlarmTemperatureFault": apexAlarmTemperatureFault,
       "apexAlarmFanFault": apexAlarmFanFault,
       "apexAlarmPowerFault": apexAlarmPowerFault,
       "apexAlarmGbeLossOfPhysicalInput": apexAlarmGbeLossOfPhysicalInput,
       "apexAlarmGbeBufferFullness": apexAlarmGbeBufferFullness,
       "apexAlarmGbeInputStreamLowBitRate": apexAlarmGbeInputStreamLowBitRate,
       "apexAlarmGbeInputStreamHighBitRate": apexAlarmGbeInputStreamHighBitRate,
       "apexAlarmGbeMptsRedundPrimaryThreshold": apexAlarmGbeMptsRedundPrimaryThreshold,
       "apexAlarmGbeMptsRedundFailOver": apexAlarmGbeMptsRedundFailOver,
       "apexAlarmServiceInError": apexAlarmServiceInError,
       "apexAlarmGbeLossOfInputStream": apexAlarmGbeLossOfInputStream,
       "apexAlarmGigeToHostCommFault": apexAlarmGigeToHostCommFault,
       "apexAlarmGbeInterfaceRedundFailOver": apexAlarmGbeInterfaceRedundFailOver,
       "apexAlarmOutputUtilizationFault": apexAlarmOutputUtilizationFault,
       "apexAlarmOutputOverflow": apexAlarmOutputOverflow,
       "apexAlarmQamModuleFault": apexAlarmQamModuleFault,
       "apexAlarmQamRfPortFault": apexAlarmQamRfPortFault,
       "apexAlarmQamChannelFault": apexAlarmQamChannelFault,
       "apexAlarmQamRfRedundFailOver": apexAlarmQamRfRedundFailOver,
       "apexAlarmQamRfRedundMismatch": apexAlarmQamRfRedundMismatch,
       "apexAlarmRtspControllerCommFault": apexAlarmRtspControllerCommFault,
       "apexAlarmRdsCommFault": apexAlarmRdsCommFault,
       "apexAlarmRemCommFault": apexAlarmRemCommFault,
       "apexAlarmRemFault": apexAlarmRemFault,
       "apexAlarmDepiControlConnectionFault": apexAlarmDepiControlConnectionFault,
       "apexAlarmDepiSessionSetupFault": apexAlarmDepiSessionSetupFault,
       "apexAlarmDtiSyncLossFault": apexAlarmDtiSyncLossFault,
       "apexAlarmChassisRedundancyPrimaryFailover": apexAlarmChassisRedundancyPrimaryFailover,
       "apexAlarmChassisRedundancySecondaryFailover": apexAlarmChassisRedundancySecondaryFailover,
       "apexAlarmChassisRedundancyAvailabilityFault": apexAlarmChassisRedundancyAvailabilityFault,
       "apexAlarmChassisRedundancyLinkFault": apexAlarmChassisRedundancyLinkFault,
       "apexAlarmChassisRedundancyConfigurationFault": apexAlarmChassisRedundancyConfigurationFault,
       "apexEvents": apexEvents,
       "apexEventEmUserLoginFailed": apexEventEmUserLoginFailed,
       "apexEventQamModuleUpgraded": apexEventQamModuleUpgraded,
       "apexEventChassisRedunPrimaryForceFailover": apexEventChassisRedunPrimaryForceFailover,
       "apexEventChassisRedunSecondaryForceFailover": apexEventChassisRedunSecondaryForceFailover,
       "apexEventChassisRedunFirmwareVersionMismatch": apexEventChassisRedunFirmwareVersionMismatch,
       "apexEventChassisRedunQAMVersionMismatch": apexEventChassisRedunQAMVersionMismatch,
       "apexConfigAlarms": apexConfigAlarms,
       "apexConfAlarmEnable": apexConfAlarmEnable,
       "apexEnableInvalidInitData": apexEnableInvalidInitData,
       "apexEnableGbeLossOfPhysicalInput": apexEnableGbeLossOfPhysicalInput,
       "apexEnableGbeBufferFullness": apexEnableGbeBufferFullness,
       "apexEnableGbeInputStreamLowBitRate": apexEnableGbeInputStreamLowBitRate,
       "apexEnableGbeInputStreamHighBitRate": apexEnableGbeInputStreamHighBitRate,
       "apexEnableGbeMptsRedundPrimaryThreshold": apexEnableGbeMptsRedundPrimaryThreshold,
       "apexEnableGbeMptsRedundFailOver": apexEnableGbeMptsRedundFailOver,
       "apexEnableServiceInError": apexEnableServiceInError,
       "apexEnableGbeLossOfInputTsFault": apexEnableGbeLossOfInputTsFault,
       "apexEnableGbeInterfaceRedundFailOver": apexEnableGbeInterfaceRedundFailOver,
       "apexEnableOutputUtilizationFault": apexEnableOutputUtilizationFault,
       "apexEnableOutputOverflow": apexEnableOutputOverflow,
       "apexEnableQamModuleFault": apexEnableQamModuleFault,
       "apexEnableQamRfPortFault": apexEnableQamRfPortFault,
       "apexEnableQamChannelFault": apexEnableQamChannelFault,
       "apexEnableQamRfRedundFailOver": apexEnableQamRfRedundFailOver,
       "apexEnableQamRfRedundMismatch": apexEnableQamRfRedundMismatch,
       "apexEnableRtspControllerCommFault": apexEnableRtspControllerCommFault,
       "apexEnableRdsCommAlarmFault": apexEnableRdsCommAlarmFault,
       "apexEnableRemCommFault": apexEnableRemCommFault,
       "apexEnableRemFault": apexEnableRemFault,
       "apexEnableDepiControlConnectionFault": apexEnableDepiControlConnectionFault,
       "apexEnableDepiSessionSetupFault": apexEnableDepiSessionSetupFault,
       "apexEnableDtiSyncLossFault": apexEnableDtiSyncLossFault,
       "apexEnableChassisRedundancyPrimaryFailover": apexEnableChassisRedundancyPrimaryFailover,
       "apexEnableChassisRedundancySecondaryFailover": apexEnableChassisRedundancySecondaryFailover,
       "apexEnableChassisRedundancyAvailabilityFault": apexEnableChassisRedundancyAvailabilityFault,
       "apexEnableChassisRedundancyLinkFault": apexEnableChassisRedundancyLinkFault,
       "apexEnableChassisRedundancyConfigurationFault": apexEnableChassisRedundancyConfigurationFault,
       "apexConfAlarmClear": apexConfAlarmClear,
       "apexClearInvalidInitData": apexClearInvalidInitData,
       "apexLogs": apexLogs,
       "apexHwEventTable": apexHwEventTable,
       "apexHwEventEntry": apexHwEventEntry,
       "apexHwEventIndex": apexHwEventIndex,
       "apexHwEventTimeLogged": apexHwEventTimeLogged,
       "apexHwEventAlarmCode": apexHwEventAlarmCode,
       "apexHwEventAlarmSeverity": apexHwEventAlarmSeverity,
       "apexHwEventData": apexHwEventData,
       "apexHwEventDescription": apexHwEventDescription,
       "apexInvalidInitDataTable": apexInvalidInitDataTable,
       "apexInvalidInitDataEntry": apexInvalidInitDataEntry,
       "apexInvalidInitDataIndex": apexInvalidInitDataIndex,
       "apexInvalidInitDataTimeLogged": apexInvalidInitDataTimeLogged,
       "apexInvalidInitDataDescription": apexInvalidInitDataDescription,
       "apexOutputTsEventTable": apexOutputTsEventTable,
       "apexOutputTsEventEntry": apexOutputTsEventEntry,
       "apexOutputTsEventIndex": apexOutputTsEventIndex,
       "apexOutputTsEventTimeLogged": apexOutputTsEventTimeLogged,
       "apexOutputTsEventAlarmCode": apexOutputTsEventAlarmCode,
       "apexOutputTsEventAlarmSeverity": apexOutputTsEventAlarmSeverity,
       "apexOutputTsEventOutputTsNum": apexOutputTsEventOutputTsNum,
       "apexOutputTsEventCurRate": apexOutputTsEventCurRate,
       "apexOutputTsEventAvgRate": apexOutputTsEventAvgRate,
       "apexOutputTsEventMinRate": apexOutputTsEventMinRate,
       "apexOutputTsEventPeakRate": apexOutputTsEventPeakRate,
       "apexOutputTsEventCurDropPackets": apexOutputTsEventCurDropPackets,
       "apexOutputTsEventPeakDropPackets": apexOutputTsEventPeakDropPackets,
       "apexOutputTsEventRollingDropPackets": apexOutputTsEventRollingDropPackets,
       "apexOutputTsEventTotalDropPackets": apexOutputTsEventTotalDropPackets,
       "apexOutputTsEventDescription": apexOutputTsEventDescription,
       "apexGbeInputTsEventTable": apexGbeInputTsEventTable,
       "apexGbeInputTsEventEntry": apexGbeInputTsEventEntry,
       "apexGbeInputTsEventIndex": apexGbeInputTsEventIndex,
       "apexGbeInputTsEventTimeLogged": apexGbeInputTsEventTimeLogged,
       "apexGbeInputTsEventAlarmCode": apexGbeInputTsEventAlarmCode,
       "apexGbeInputTsEventAlarmSeverity": apexGbeInputTsEventAlarmSeverity,
       "apexGbeInputTsEventRedundantConfig": apexGbeInputTsEventRedundantConfig,
       "apexGbeInputTsEventGbeInterface": apexGbeInputTsEventGbeInterface,
       "apexGbeInputTsEventUdpPort": apexGbeInputTsEventUdpPort,
       "apexGbeInputTsEventMulticastIp": apexGbeInputTsEventMulticastIp,
       "apexGbeInputTsEventSourceIp": apexGbeInputTsEventSourceIp,
       "apexGbeInputTsEventInputTsState": apexGbeInputTsEventInputTsState,
       "apexGbeInputTsEventRateCompareType": apexGbeInputTsEventRateCompareType,
       "apexGbeInputTsEventSamplingPeriod": apexGbeInputTsEventSamplingPeriod,
       "apexGbeInputTsEventPriCurStreamCount": apexGbeInputTsEventPriCurStreamCount,
       "apexGbeInputTsEventPriCurDataCount": apexGbeInputTsEventPriCurDataCount,
       "apexGbeInputTsEventSecCurStreamCount": apexGbeInputTsEventSecCurStreamCount,
       "apexGbeInputTsEventSecCurDataCount": apexGbeInputTsEventSecCurDataCount,
       "apexGbeInputTsEventDescription": apexGbeInputTsEventDescription,
       "apexRtspEventTable": apexRtspEventTable,
       "apexRtspEventEntry": apexRtspEventEntry,
       "apexRtspEventIndex": apexRtspEventIndex,
       "apexRtspEventTimeLogged": apexRtspEventTimeLogged,
       "apexRtspEventControllerIp": apexRtspEventControllerIp,
       "apexRtspEventSessionCount": apexRtspEventSessionCount,
       "apexRtspEventSourceDescription": apexRtspEventSourceDescription,
       "apexRtspEventDescription": apexRtspEventDescription,
       "apexMappingErrorTable": apexMappingErrorTable,
       "apexMappingErrorEntry": apexMappingErrorEntry,
       "apexMappingErrorIndex": apexMappingErrorIndex,
       "apexMappingErrorTimeLogged": apexMappingErrorTimeLogged,
       "apexMappingErrorCode": apexMappingErrorCode,
       "apexMappingErrorMappingType": apexMappingErrorMappingType,
       "apexMappingErrorInputType": apexMappingErrorInputType,
       "apexMappingErrorInputInterface": apexMappingErrorInputInterface,
       "apexMappingErrorUdpPort": apexMappingErrorUdpPort,
       "apexMappingErrorMulticastIp": apexMappingErrorMulticastIp,
       "apexMappingErrorSourceIp": apexMappingErrorSourceIp,
       "apexMappingErrorInputProgramPid": apexMappingErrorInputProgramPid,
       "apexMappingErrorOutputProgramPid": apexMappingErrorOutputProgramPid,
       "apexMappingErrorOutputOpMode": apexMappingErrorOutputOpMode,
       "apexMappingErrorOutputTsNum": apexMappingErrorOutputTsNum,
       "apexMappingErrorSecInputInterface": apexMappingErrorSecInputInterface,
       "apexMappingErrorSecUdpPort": apexMappingErrorSecUdpPort,
       "apexMappingErrorSecMulticastIp": apexMappingErrorSecMulticastIp,
       "apexMappingErrorSecSourceIp": apexMappingErrorSecSourceIp,
       "apexChassisRedundancyEventTable": apexChassisRedundancyEventTable,
       "apexChassisRedundancyEventEntry": apexChassisRedundancyEventEntry,
       "apexChassisRedundancyEventIndex": apexChassisRedundancyEventIndex,
       "apexChassisRedundancyEventTimeLogged": apexChassisRedundancyEventTimeLogged,
       "apexChassisRedundancyEventDescription": apexChassisRedundancyEventDescription,
       "apexDebug": apexDebug}
)
