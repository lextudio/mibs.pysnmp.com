# SNMP MIB module (DES3225G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES3225G-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:27 2024
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
    "NotificationType",
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_Des3225gProd_ObjectIdentity = ObjectIdentity
dlink_Des3225gProd = _Dlink_Des3225gProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 24)
)
_SwProperty_ObjectIdentity = ObjectIdentity
swProperty = _SwProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1)
)
_SwModule_ObjectIdentity = ObjectIdentity
swModule = _SwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 1)
)
_Dlink_mgmt_ObjectIdentity = ObjectIdentity
dlink_mgmt = _Dlink_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11)
)
_Des3225gSeries_ObjectIdentity = ObjectIdentity
des3225gSeries = _Des3225gSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24)
)
_SwDevPackage_ObjectIdentity = ObjectIdentity
swDevPackage = _SwDevPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1)
)
_SwDevInfo_ObjectIdentity = ObjectIdentity
swDevInfo = _SwDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1)
)
_SwDevInfoSystemUpTime_Type = TimeTicks
_SwDevInfoSystemUpTime_Object = MibScalar
swDevInfoSystemUpTime = _SwDevInfoSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 1),
    _SwDevInfoSystemUpTime_Type()
)
swDevInfoSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSystemUpTime.setStatus("mandatory")
_SwDevInfoMaxNumOfModule_Type = Integer32
_SwDevInfoMaxNumOfModule_Object = MibScalar
swDevInfoMaxNumOfModule = _SwDevInfoMaxNumOfModule_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 2),
    _SwDevInfoMaxNumOfModule_Type()
)
swDevInfoMaxNumOfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoMaxNumOfModule.setStatus("mandatory")
_SwDevInfoTotalNumOfModule_Type = Integer32
_SwDevInfoTotalNumOfModule_Object = MibScalar
swDevInfoTotalNumOfModule = _SwDevInfoTotalNumOfModule_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 3),
    _SwDevInfoTotalNumOfModule_Type()
)
swDevInfoTotalNumOfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoTotalNumOfModule.setStatus("mandatory")
_SwDevInfoTotalNumOfPort_Type = Integer32
_SwDevInfoTotalNumOfPort_Object = MibScalar
swDevInfoTotalNumOfPort = _SwDevInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 4),
    _SwDevInfoTotalNumOfPort_Type()
)
swDevInfoTotalNumOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoTotalNumOfPort.setStatus("mandatory")
_SwDevInfoNumOfPortInUse_Type = Integer32
_SwDevInfoNumOfPortInUse_Object = MibScalar
swDevInfoNumOfPortInUse = _SwDevInfoNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 5),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("mandatory")


class _SwDevInfoConsoleInUse_Type(Integer32):
    """Custom type swDevInfoConsoleInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-in-use", 3),
          ("other", 1))
    )


_SwDevInfoConsoleInUse_Type.__name__ = "Integer32"
_SwDevInfoConsoleInUse_Object = MibScalar
swDevInfoConsoleInUse = _SwDevInfoConsoleInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 6),
    _SwDevInfoConsoleInUse_Type()
)
swDevInfoConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoConsoleInUse.setStatus("mandatory")


class _SwDevInfoSystemLedStatus_Type(OctetString):
    """Custom type swDevInfoSystemLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwDevInfoSystemLedStatus_Type.__name__ = "OctetString"
_SwDevInfoSystemLedStatus_Object = MibScalar
swDevInfoSystemLedStatus = _SwDevInfoSystemLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 7),
    _SwDevInfoSystemLedStatus_Type()
)
swDevInfoSystemLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSystemLedStatus.setStatus("mandatory")


class _SwDevInfoSaveCfg_Type(Integer32):
    """Custom type swDevInfoSaveCfg based on Integer32"""
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
        *(("changed-not-save", 4),
          ("completed", 3),
          ("failed", 5),
          ("other", 1),
          ("proceeding", 2))
    )


_SwDevInfoSaveCfg_Type.__name__ = "Integer32"
_SwDevInfoSaveCfg_Object = MibScalar
swDevInfoSaveCfg = _SwDevInfoSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 8),
    _SwDevInfoSaveCfg_Type()
)
swDevInfoSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSaveCfg.setStatus("mandatory")
_SwDevCtrl_ObjectIdentity = ObjectIdentity
swDevCtrl = _SwDevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2)
)


class _SwDevCtrlStpState_Type(Integer32):
    """Custom type swDevCtrlStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevCtrlStpState_Type.__name__ = "Integer32"
_SwDevCtrlStpState_Object = MibScalar
swDevCtrlStpState = _SwDevCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 1),
    _SwDevCtrlStpState_Type()
)
swDevCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlStpState.setStatus("mandatory")


class _SwDevIGMPCaptureState_Type(Integer32):
    """Custom type swDevIGMPCaptureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevIGMPCaptureState_Type.__name__ = "Integer32"
_SwDevIGMPCaptureState_Object = MibScalar
swDevIGMPCaptureState = _SwDevIGMPCaptureState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 2),
    _SwDevIGMPCaptureState_Type()
)
swDevIGMPCaptureState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevIGMPCaptureState.setStatus("mandatory")


class _SwDevCtrlPartitionModeState_Type(Integer32):
    """Custom type swDevCtrlPartitionModeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevCtrlPartitionModeState_Type.__name__ = "Integer32"
_SwDevCtrlPartitionModeState_Object = MibScalar
swDevCtrlPartitionModeState = _SwDevCtrlPartitionModeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 3),
    _SwDevCtrlPartitionModeState_Type()
)
swDevCtrlPartitionModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlPartitionModeState.setStatus("mandatory")


class _SwDevCtrlTableLockState_Type(Integer32):
    """Custom type swDevCtrlTableLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevCtrlTableLockState_Type.__name__ = "Integer32"
_SwDevCtrlTableLockState_Object = MibScalar
swDevCtrlTableLockState = _SwDevCtrlTableLockState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 4),
    _SwDevCtrlTableLockState_Type()
)
swDevCtrlTableLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlTableLockState.setStatus("mandatory")
_SwDevCtrlSaveCfg_Type = Integer32
_SwDevCtrlSaveCfg_Object = MibScalar
swDevCtrlSaveCfg = _SwDevCtrlSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 5),
    _SwDevCtrlSaveCfg_Type()
)
swDevCtrlSaveCfg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swDevCtrlSaveCfg.setStatus("mandatory")


class _SwDevCtrlHOLState_Type(Integer32):
    """Custom type swDevCtrlHOLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevCtrlHOLState_Type.__name__ = "Integer32"
_SwDevCtrlHOLState_Object = MibScalar
swDevCtrlHOLState = _SwDevCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 6),
    _SwDevCtrlHOLState_Type()
)
swDevCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlHOLState.setStatus("mandatory")


class _SwDevCtrlAddrLookupModesAndHitRate_Type(Integer32):
    """Custom type swDevCtrlAddrLookupModesAndHitRate based on Integer32"""
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
        *(("level0", 1),
          ("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("level4", 5),
          ("level5", 6),
          ("level6", 7),
          ("level7", 8))
    )


_SwDevCtrlAddrLookupModesAndHitRate_Type.__name__ = "Integer32"
_SwDevCtrlAddrLookupModesAndHitRate_Object = MibScalar
swDevCtrlAddrLookupModesAndHitRate = _SwDevCtrlAddrLookupModesAndHitRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 7),
    _SwDevCtrlAddrLookupModesAndHitRate_Type()
)
swDevCtrlAddrLookupModesAndHitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlAddrLookupModesAndHitRate.setStatus("mandatory")


class _SwDevCtrlUploadImageFileName_Type(DisplayString):
    """Custom type swDevCtrlUploadImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwDevCtrlUploadImageFileName_Type.__name__ = "DisplayString"
_SwDevCtrlUploadImageFileName_Object = MibScalar
swDevCtrlUploadImageFileName = _SwDevCtrlUploadImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 8),
    _SwDevCtrlUploadImageFileName_Type()
)
swDevCtrlUploadImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlUploadImageFileName.setStatus("mandatory")
_SwDevCtrlUploadImage_Type = Integer32
_SwDevCtrlUploadImage_Object = MibScalar
swDevCtrlUploadImage = _SwDevCtrlUploadImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 9),
    _SwDevCtrlUploadImage_Type()
)
swDevCtrlUploadImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swDevCtrlUploadImage.setStatus("mandatory")
_SwDevAlarm_ObjectIdentity = ObjectIdentity
swDevAlarm = _SwDevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3)
)


class _SwDevAlarmPartition_Type(Integer32):
    """Custom type swDevAlarmPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevAlarmPartition_Type.__name__ = "Integer32"
_SwDevAlarmPartition_Object = MibScalar
swDevAlarmPartition = _SwDevAlarmPartition_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 1),
    _SwDevAlarmPartition_Type()
)
swDevAlarmPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevAlarmPartition.setStatus("mandatory")


class _SwDevAlarmNewRoot_Type(Integer32):
    """Custom type swDevAlarmNewRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevAlarmNewRoot_Type.__name__ = "Integer32"
_SwDevAlarmNewRoot_Object = MibScalar
swDevAlarmNewRoot = _SwDevAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 2),
    _SwDevAlarmNewRoot_Type()
)
swDevAlarmNewRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevAlarmNewRoot.setStatus("mandatory")


class _SwDevAlarmTopologyChange_Type(Integer32):
    """Custom type swDevAlarmTopologyChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevAlarmTopologyChange_Type.__name__ = "Integer32"
_SwDevAlarmTopologyChange_Object = MibScalar
swDevAlarmTopologyChange = _SwDevAlarmTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 3),
    _SwDevAlarmTopologyChange_Type()
)
swDevAlarmTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevAlarmTopologyChange.setStatus("mandatory")


class _SwDevAlarmLinkChange_Type(Integer32):
    """Custom type swDevAlarmLinkChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDevAlarmLinkChange_Type.__name__ = "Integer32"
_SwDevAlarmLinkChange_Object = MibScalar
swDevAlarmLinkChange = _SwDevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 4),
    _SwDevAlarmLinkChange_Type()
)
swDevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevAlarmLinkChange.setStatus("mandatory")
_SwModulePackage_ObjectIdentity = ObjectIdentity
swModulePackage = _SwModulePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2)
)
_SwModuleInfoTable_Object = MibTable
swModuleInfoTable = _SwModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1)
)
if mibBuilder.loadTexts:
    swModuleInfoTable.setStatus("mandatory")
_SwModuleInfoEntry_Object = MibTableRow
swModuleInfoEntry = _SwModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1)
)
swModuleInfoEntry.setIndexNames(
    (0, "DES3225G-MIB", "swModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    swModuleInfoEntry.setStatus("mandatory")
_SwModuleInfoIndex_Type = Integer32
_SwModuleInfoIndex_Object = MibTableColumn
swModuleInfoIndex = _SwModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 1),
    _SwModuleInfoIndex_Type()
)
swModuleInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoIndex.setStatus("mandatory")
_SwModuleInfoDesc_Type = DisplayString
_SwModuleInfoDesc_Object = MibTableColumn
swModuleInfoDesc = _SwModuleInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 2),
    _SwModuleInfoDesc_Type()
)
swModuleInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoDesc.setStatus("mandatory")


class _SwModuleInfoType_Type(Integer32):
    """Custom type swModuleInfoType based on Integer32"""
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
        *(("baseModule-UTP", 2),
          ("optionModule-1000Base-LX", 7),
          ("optionModule-1000Base-SX", 6),
          ("optionModule-1PortFiber-SC", 5),
          ("optionModule-2PortFiber-MTRJ", 3),
          ("optionModule-2PortTX-UTP", 4),
          ("other", 1))
    )


_SwModuleInfoType_Type.__name__ = "Integer32"
_SwModuleInfoType_Object = MibTableColumn
swModuleInfoType = _SwModuleInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 3),
    _SwModuleInfoType_Type()
)
swModuleInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoType.setStatus("mandatory")
_SwModuleInfoTotalNumOfPort_Type = Integer32
_SwModuleInfoTotalNumOfPort_Object = MibTableColumn
swModuleInfoTotalNumOfPort = _SwModuleInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 4),
    _SwModuleInfoTotalNumOfPort_Type()
)
swModuleInfoTotalNumOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoTotalNumOfPort.setStatus("mandatory")
_SwModuleInfoNumOfPortInUse_Type = Integer32
_SwModuleInfoNumOfPortInUse_Object = MibTableColumn
swModuleInfoNumOfPortInUse = _SwModuleInfoNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 5),
    _SwModuleInfoNumOfPortInUse_Type()
)
swModuleInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoNumOfPortInUse.setStatus("mandatory")


class _SwModuleInfoPortLedStatus_Type(OctetString):
    """Custom type swModuleInfoPortLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwModuleInfoPortLedStatus_Type.__name__ = "OctetString"
_SwModuleInfoPortLedStatus_Object = MibTableColumn
swModuleInfoPortLedStatus = _SwModuleInfoPortLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 6),
    _SwModuleInfoPortLedStatus_Type()
)
swModuleInfoPortLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleInfoPortLedStatus.setStatus("mandatory")
_SwPortPackage_ObjectIdentity = ObjectIdentity
swPortPackage = _SwPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3)
)
_SwPortInfoTable_Object = MibTable
swPortInfoTable = _SwPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1)
)
if mibBuilder.loadTexts:
    swPortInfoTable.setStatus("mandatory")
_SwPortInfoEntry_Object = MibTableRow
swPortInfoEntry = _SwPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1)
)
swPortInfoEntry.setIndexNames(
    (0, "DES3225G-MIB", "swPortInfoModuleIndex"),
    (0, "DES3225G-MIB", "swPortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swPortInfoEntry.setStatus("mandatory")
_SwPortInfoModuleIndex_Type = Integer32
_SwPortInfoModuleIndex_Object = MibTableColumn
swPortInfoModuleIndex = _SwPortInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 1),
    _SwPortInfoModuleIndex_Type()
)
swPortInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoModuleIndex.setStatus("mandatory")
_SwPortInfoPortIndex_Type = Integer32
_SwPortInfoPortIndex_Object = MibTableColumn
swPortInfoPortIndex = _SwPortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 2),
    _SwPortInfoPortIndex_Type()
)
swPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoPortIndex.setStatus("mandatory")


class _SwPortInfoType_Type(Integer32):
    """Custom type swPortInfoType based on Integer32"""
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
        *(("other", 1),
          ("portType-AUI", 3),
          ("portType-BNC", 6),
          ("portType-Fiber-MTRJ", 4),
          ("portType-Fiber-SC", 5),
          ("portType-UTP", 2))
    )


_SwPortInfoType_Type.__name__ = "Integer32"
_SwPortInfoType_Object = MibTableColumn
swPortInfoType = _SwPortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 3),
    _SwPortInfoType_Type()
)
swPortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoType.setStatus("mandatory")


class _SwPortInfoLinkStatus_Type(Integer32):
    """Custom type swPortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwPortInfoLinkStatus_Type.__name__ = "Integer32"
_SwPortInfoLinkStatus_Object = MibTableColumn
swPortInfoLinkStatus = _SwPortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 4),
    _SwPortInfoLinkStatus_Type()
)
swPortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoLinkStatus.setStatus("mandatory")


class _SwPortInfoNwayStatus_Type(Integer32):
    """Custom type swPortInfoNwayStatus based on Integer32"""
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
        *(("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("full-1Gigabps", 7),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2),
          ("half-1Gigabps", 6),
          ("other", 1))
    )


_SwPortInfoNwayStatus_Type.__name__ = "Integer32"
_SwPortInfoNwayStatus_Object = MibTableColumn
swPortInfoNwayStatus = _SwPortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 5),
    _SwPortInfoNwayStatus_Type()
)
swPortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoNwayStatus.setStatus("mandatory")


class _SwPortInfoFlowCtrlStatus_Type(Integer32):
    """Custom type swPortInfoFlowCtrlStatus based on Integer32"""
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
        *(("backpressure-disabled", 4),
          ("backpressure-enabled", 5),
          ("flowctrl-disabled", 2),
          ("flowctrl-enabled", 3),
          ("other", 1))
    )


_SwPortInfoFlowCtrlStatus_Type.__name__ = "Integer32"
_SwPortInfoFlowCtrlStatus_Object = MibTableColumn
swPortInfoFlowCtrlStatus = _SwPortInfoFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 6),
    _SwPortInfoFlowCtrlStatus_Type()
)
swPortInfoFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoFlowCtrlStatus.setStatus("mandatory")
_SwPortCtrlTable_Object = MibTable
swPortCtrlTable = _SwPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2)
)
if mibBuilder.loadTexts:
    swPortCtrlTable.setStatus("mandatory")
_SwPortCtrlEntry_Object = MibTableRow
swPortCtrlEntry = _SwPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1)
)
swPortCtrlEntry.setIndexNames(
    (0, "DES3225G-MIB", "swPortCtrlModuleIndex"),
    (0, "DES3225G-MIB", "swPortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swPortCtrlEntry.setStatus("mandatory")
_SwPortCtrlModuleIndex_Type = Integer32
_SwPortCtrlModuleIndex_Object = MibTableColumn
swPortCtrlModuleIndex = _SwPortCtrlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 1),
    _SwPortCtrlModuleIndex_Type()
)
swPortCtrlModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCtrlModuleIndex.setStatus("mandatory")
_SwPortCtrlPortIndex_Type = Integer32
_SwPortCtrlPortIndex_Object = MibTableColumn
swPortCtrlPortIndex = _SwPortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 2),
    _SwPortCtrlPortIndex_Type()
)
swPortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCtrlPortIndex.setStatus("mandatory")


class _SwPortCtrlAdminState_Type(Integer32):
    """Custom type swPortCtrlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlAdminState_Type.__name__ = "Integer32"
_SwPortCtrlAdminState_Object = MibTableColumn
swPortCtrlAdminState = _SwPortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 3),
    _SwPortCtrlAdminState_Type()
)
swPortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlAdminState.setStatus("mandatory")


class _SwPortCtrlLinkStatusAlarmState_Type(Integer32):
    """Custom type swPortCtrlLinkStatusAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlLinkStatusAlarmState_Type.__name__ = "Integer32"
_SwPortCtrlLinkStatusAlarmState_Object = MibTableColumn
swPortCtrlLinkStatusAlarmState = _SwPortCtrlLinkStatusAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 4),
    _SwPortCtrlLinkStatusAlarmState_Type()
)
swPortCtrlLinkStatusAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlLinkStatusAlarmState.setStatus("mandatory")


class _SwPortCtrlNwayState_Type(Integer32):
    """Custom type swPortCtrlNwayState based on Integer32"""
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
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwPortCtrlNwayState_Type.__name__ = "Integer32"
_SwPortCtrlNwayState_Object = MibTableColumn
swPortCtrlNwayState = _SwPortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 5),
    _SwPortCtrlNwayState_Type()
)
swPortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlNwayState.setStatus("mandatory")


class _SwPortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swPortCtrlFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwPortCtrlFlowCtrlState_Object = MibTableColumn
swPortCtrlFlowCtrlState = _SwPortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 6),
    _SwPortCtrlFlowCtrlState_Type()
)
swPortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlFlowCtrlState.setStatus("mandatory")


class _SwPortCtrlBackPressState_Type(Integer32):
    """Custom type swPortCtrlBackPressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlBackPressState_Type.__name__ = "Integer32"
_SwPortCtrlBackPressState_Object = MibTableColumn
swPortCtrlBackPressState = _SwPortCtrlBackPressState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 7),
    _SwPortCtrlBackPressState_Type()
)
swPortCtrlBackPressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlBackPressState.setStatus("mandatory")


class _SwPortCtrlLockState_Type(Integer32):
    """Custom type swPortCtrlLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwPortCtrlLockState_Type.__name__ = "Integer32"
_SwPortCtrlLockState_Object = MibTableColumn
swPortCtrlLockState = _SwPortCtrlLockState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 8),
    _SwPortCtrlLockState_Type()
)
swPortCtrlLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlLockState.setStatus("mandatory")


class _SwPortCtrlPriority_Type(Integer32):
    """Custom type swPortCtrlPriority based on Integer32"""
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
        *(("default", 2),
          ("force-high-priority", 4),
          ("force-low-priority", 3),
          ("other", 1))
    )


_SwPortCtrlPriority_Type.__name__ = "Integer32"
_SwPortCtrlPriority_Object = MibTableColumn
swPortCtrlPriority = _SwPortCtrlPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 9),
    _SwPortCtrlPriority_Type()
)
swPortCtrlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlPriority.setStatus("mandatory")


class _SwPortCtrlStpState_Type(Integer32):
    """Custom type swPortCtrlStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlStpState_Type.__name__ = "Integer32"
_SwPortCtrlStpState_Object = MibTableColumn
swPortCtrlStpState = _SwPortCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 10),
    _SwPortCtrlStpState_Type()
)
swPortCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlStpState.setStatus("mandatory")


class _SwPortCtrlHOLState_Type(Integer32):
    """Custom type swPortCtrlHOLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortCtrlHOLState_Type.__name__ = "Integer32"
_SwPortCtrlHOLState_Object = MibTableColumn
swPortCtrlHOLState = _SwPortCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 11),
    _SwPortCtrlHOLState_Type()
)
swPortCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlHOLState.setStatus("mandatory")


class _SwPortCtrlBroadcastRisingThr_Type(Integer32):
    """Custom type swPortCtrlBroadcastRisingThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1488000),
    )


_SwPortCtrlBroadcastRisingThr_Type.__name__ = "Integer32"
_SwPortCtrlBroadcastRisingThr_Object = MibTableColumn
swPortCtrlBroadcastRisingThr = _SwPortCtrlBroadcastRisingThr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 12),
    _SwPortCtrlBroadcastRisingThr_Type()
)
swPortCtrlBroadcastRisingThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlBroadcastRisingThr.setStatus("mandatory")


class _SwPortCtrlBroadcastFallingThr_Type(Integer32):
    """Custom type swPortCtrlBroadcastFallingThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1488000),
    )


_SwPortCtrlBroadcastFallingThr_Type.__name__ = "Integer32"
_SwPortCtrlBroadcastFallingThr_Object = MibTableColumn
swPortCtrlBroadcastFallingThr = _SwPortCtrlBroadcastFallingThr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 13),
    _SwPortCtrlBroadcastFallingThr_Type()
)
swPortCtrlBroadcastFallingThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlBroadcastFallingThr.setStatus("mandatory")


class _SwPortCtrlBroadcastRisingAct_Type(Integer32):
    """Custom type swPortCtrlBroadcastRisingAct based on Integer32"""
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
        *(("blocking", 3),
          ("blocking-trap", 4),
          ("do-nothing", 2),
          ("other", 1))
    )


_SwPortCtrlBroadcastRisingAct_Type.__name__ = "Integer32"
_SwPortCtrlBroadcastRisingAct_Object = MibTableColumn
swPortCtrlBroadcastRisingAct = _SwPortCtrlBroadcastRisingAct_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 14),
    _SwPortCtrlBroadcastRisingAct_Type()
)
swPortCtrlBroadcastRisingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlBroadcastRisingAct.setStatus("mandatory")


class _SwPortCtrlBroadcastFallingAct_Type(Integer32):
    """Custom type swPortCtrlBroadcastFallingAct based on Integer32"""
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
        *(("do-nothing", 2),
          ("forwarding", 3),
          ("forwarding-trap", 4),
          ("other", 1))
    )


_SwPortCtrlBroadcastFallingAct_Type.__name__ = "Integer32"
_SwPortCtrlBroadcastFallingAct_Object = MibTableColumn
swPortCtrlBroadcastFallingAct = _SwPortCtrlBroadcastFallingAct_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 15),
    _SwPortCtrlBroadcastFallingAct_Type()
)
swPortCtrlBroadcastFallingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlBroadcastFallingAct.setStatus("mandatory")
_SwPortCtrlCleanAllStatisticCounter_Type = Integer32
_SwPortCtrlCleanAllStatisticCounter_Object = MibTableColumn
swPortCtrlCleanAllStatisticCounter = _SwPortCtrlCleanAllStatisticCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 16),
    _SwPortCtrlCleanAllStatisticCounter_Type()
)
swPortCtrlCleanAllStatisticCounter.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swPortCtrlCleanAllStatisticCounter.setStatus("mandatory")
_SwPortStTable_Object = MibTable
swPortStTable = _SwPortStTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3)
)
if mibBuilder.loadTexts:
    swPortStTable.setStatus("mandatory")
_SwPortStEntry_Object = MibTableRow
swPortStEntry = _SwPortStEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1)
)
swPortStEntry.setIndexNames(
    (0, "DES3225G-MIB", "swPortStModuleIndex"),
    (0, "DES3225G-MIB", "swPortStPortIndex"),
)
if mibBuilder.loadTexts:
    swPortStEntry.setStatus("mandatory")
_SwPortStModuleIndex_Type = Integer32
_SwPortStModuleIndex_Object = MibTableColumn
swPortStModuleIndex = _SwPortStModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 1),
    _SwPortStModuleIndex_Type()
)
swPortStModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStModuleIndex.setStatus("mandatory")
_SwPortStPortIndex_Type = Integer32
_SwPortStPortIndex_Object = MibTableColumn
swPortStPortIndex = _SwPortStPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 2),
    _SwPortStPortIndex_Type()
)
swPortStPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStPortIndex.setStatus("mandatory")
_SwPortStByteRx_Type = Counter32
_SwPortStByteRx_Object = MibTableColumn
swPortStByteRx = _SwPortStByteRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 3),
    _SwPortStByteRx_Type()
)
swPortStByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStByteRx.setStatus("mandatory")
_SwPortStByteTx_Type = Counter32
_SwPortStByteTx_Object = MibTableColumn
swPortStByteTx = _SwPortStByteTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 4),
    _SwPortStByteTx_Type()
)
swPortStByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStByteTx.setStatus("mandatory")
_SwPortStFrameRx_Type = Counter32
_SwPortStFrameRx_Object = MibTableColumn
swPortStFrameRx = _SwPortStFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 5),
    _SwPortStFrameRx_Type()
)
swPortStFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrameRx.setStatus("mandatory")
_SwPortStFrameTx_Type = Counter32
_SwPortStFrameTx_Object = MibTableColumn
swPortStFrameTx = _SwPortStFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 6),
    _SwPortStFrameTx_Type()
)
swPortStFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrameTx.setStatus("mandatory")
_SwPortStTotalBytesRx_Type = Counter32
_SwPortStTotalBytesRx_Object = MibTableColumn
swPortStTotalBytesRx = _SwPortStTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 7),
    _SwPortStTotalBytesRx_Type()
)
swPortStTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStTotalBytesRx.setStatus("mandatory")
_SwPortStTotalFramesRx_Type = Counter32
_SwPortStTotalFramesRx_Object = MibTableColumn
swPortStTotalFramesRx = _SwPortStTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 8),
    _SwPortStTotalFramesRx_Type()
)
swPortStTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStTotalFramesRx.setStatus("mandatory")
_SwPortStBroadcastFramesRx_Type = Counter32
_SwPortStBroadcastFramesRx_Object = MibTableColumn
swPortStBroadcastFramesRx = _SwPortStBroadcastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 9),
    _SwPortStBroadcastFramesRx_Type()
)
swPortStBroadcastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStBroadcastFramesRx.setStatus("mandatory")
_SwPortStMulticastFramesRx_Type = Counter32
_SwPortStMulticastFramesRx_Object = MibTableColumn
swPortStMulticastFramesRx = _SwPortStMulticastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 10),
    _SwPortStMulticastFramesRx_Type()
)
swPortStMulticastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStMulticastFramesRx.setStatus("mandatory")
_SwPortStCRCError_Type = Counter32
_SwPortStCRCError_Object = MibTableColumn
swPortStCRCError = _SwPortStCRCError_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 11),
    _SwPortStCRCError_Type()
)
swPortStCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStCRCError.setStatus("mandatory")
_SwPortStOversizeFrames_Type = Counter32
_SwPortStOversizeFrames_Object = MibTableColumn
swPortStOversizeFrames = _SwPortStOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 12),
    _SwPortStOversizeFrames_Type()
)
swPortStOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStOversizeFrames.setStatus("mandatory")
_SwPortStFragments_Type = Counter32
_SwPortStFragments_Object = MibTableColumn
swPortStFragments = _SwPortStFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 13),
    _SwPortStFragments_Type()
)
swPortStFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFragments.setStatus("mandatory")
_SwPortStJabber_Type = Counter32
_SwPortStJabber_Object = MibTableColumn
swPortStJabber = _SwPortStJabber_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 14),
    _SwPortStJabber_Type()
)
swPortStJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStJabber.setStatus("mandatory")
_SwPortStCollision_Type = Counter32
_SwPortStCollision_Object = MibTableColumn
swPortStCollision = _SwPortStCollision_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 15),
    _SwPortStCollision_Type()
)
swPortStCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStCollision.setStatus("mandatory")
_SwPortStLateCollision_Type = Counter32
_SwPortStLateCollision_Object = MibTableColumn
swPortStLateCollision = _SwPortStLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 16),
    _SwPortStLateCollision_Type()
)
swPortStLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStLateCollision.setStatus("mandatory")
_SwPortStFrames_64_bytes_Type = Counter32
_SwPortStFrames_64_bytes_Object = MibScalar
swPortStFrames_64_bytes = _SwPortStFrames_64_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 17),
    _SwPortStFrames_64_bytes_Type()
)
swPortStFrames_64_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_64_bytes.setStatus("mandatory")
_SwPortStFrames_65_127_bytes_Type = Counter32
_SwPortStFrames_65_127_bytes_Object = MibScalar
swPortStFrames_65_127_bytes = _SwPortStFrames_65_127_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 18),
    _SwPortStFrames_65_127_bytes_Type()
)
swPortStFrames_65_127_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_65_127_bytes.setStatus("mandatory")
_SwPortStFrames_128_255_bytes_Type = Counter32
_SwPortStFrames_128_255_bytes_Object = MibScalar
swPortStFrames_128_255_bytes = _SwPortStFrames_128_255_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 19),
    _SwPortStFrames_128_255_bytes_Type()
)
swPortStFrames_128_255_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_128_255_bytes.setStatus("mandatory")
_SwPortStFrames_256_511_bytes_Type = Counter32
_SwPortStFrames_256_511_bytes_Object = MibScalar
swPortStFrames_256_511_bytes = _SwPortStFrames_256_511_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 20),
    _SwPortStFrames_256_511_bytes_Type()
)
swPortStFrames_256_511_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_256_511_bytes.setStatus("mandatory")
_SwPortStFrames_512_1023_bytes_Type = Counter32
_SwPortStFrames_512_1023_bytes_Object = MibScalar
swPortStFrames_512_1023_bytes = _SwPortStFrames_512_1023_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 21),
    _SwPortStFrames_512_1023_bytes_Type()
)
swPortStFrames_512_1023_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_512_1023_bytes.setStatus("mandatory")
_SwPortStFrames_1024_1536_bytes_Type = Counter32
_SwPortStFrames_1024_1536_bytes_Object = MibScalar
swPortStFrames_1024_1536_bytes = _SwPortStFrames_1024_1536_bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 22),
    _SwPortStFrames_1024_1536_bytes_Type()
)
swPortStFrames_1024_1536_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFrames_1024_1536_bytes.setStatus("mandatory")
_SwPortStFramesDroppedFrames_Type = Counter32
_SwPortStFramesDroppedFrames_Object = MibTableColumn
swPortStFramesDroppedFrames = _SwPortStFramesDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 23),
    _SwPortStFramesDroppedFrames_Type()
)
swPortStFramesDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStFramesDroppedFrames.setStatus("mandatory")
_SwPortStMulticastFramesTx_Type = Counter32
_SwPortStMulticastFramesTx_Object = MibTableColumn
swPortStMulticastFramesTx = _SwPortStMulticastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 24),
    _SwPortStMulticastFramesTx_Type()
)
swPortStMulticastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStMulticastFramesTx.setStatus("mandatory")
_SwPortStBroadcastFramesTx_Type = Counter32
_SwPortStBroadcastFramesTx_Object = MibTableColumn
swPortStBroadcastFramesTx = _SwPortStBroadcastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 25),
    _SwPortStBroadcastFramesTx_Type()
)
swPortStBroadcastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStBroadcastFramesTx.setStatus("mandatory")
_SwPortStUndersizeFrames_Type = Counter32
_SwPortStUndersizeFrames_Object = MibTableColumn
swPortStUndersizeFrames = _SwPortStUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 26),
    _SwPortStUndersizeFrames_Type()
)
swPortStUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStUndersizeFrames.setStatus("mandatory")
_SwFdbPackage_ObjectIdentity = ObjectIdentity
swFdbPackage = _SwFdbPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4)
)
_SwFdbStaticTable_Object = MibTable
swFdbStaticTable = _SwFdbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1)
)
if mibBuilder.loadTexts:
    swFdbStaticTable.setStatus("mandatory")
_SwFdbStaticEntry_Object = MibTableRow
swFdbStaticEntry = _SwFdbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1)
)
swFdbStaticEntry.setIndexNames(
    (0, "DES3225G-MIB", "swFdbStaticVid"),
    (0, "DES3225G-MIB", "swFdbStaticAddressIndex"),
)
if mibBuilder.loadTexts:
    swFdbStaticEntry.setStatus("mandatory")
_SwFdbStaticVid_Type = Integer32
_SwFdbStaticVid_Object = MibTableColumn
swFdbStaticVid = _SwFdbStaticVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 1),
    _SwFdbStaticVid_Type()
)
swFdbStaticVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticVid.setStatus("mandatory")
_SwFdbStaticAddressIndex_Type = MacAddress
_SwFdbStaticAddressIndex_Object = MibTableColumn
swFdbStaticAddressIndex = _SwFdbStaticAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 2),
    _SwFdbStaticAddressIndex_Type()
)
swFdbStaticAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticAddressIndex.setStatus("mandatory")


class _SwFdbStaticPortMap_Type(OctetString):
    """Custom type swFdbStaticPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SwFdbStaticPortMap_Type.__name__ = "OctetString"
_SwFdbStaticPortMap_Object = MibTableColumn
swFdbStaticPortMap = _SwFdbStaticPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 3),
    _SwFdbStaticPortMap_Type()
)
swFdbStaticPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticPortMap.setStatus("mandatory")


class _SwFdbStaticState_Type(Integer32):
    """Custom type swFdbStaticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwFdbStaticState_Type.__name__ = "Integer32"
_SwFdbStaticState_Object = MibTableColumn
swFdbStaticState = _SwFdbStaticState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 4),
    _SwFdbStaticState_Type()
)
swFdbStaticState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticState.setStatus("mandatory")


class _SwFdbStaticStatus_Type(Integer32):
    """Custom type swFdbStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_SwFdbStaticStatus_Type.__name__ = "Integer32"
_SwFdbStaticStatus_Object = MibTableColumn
swFdbStaticStatus = _SwFdbStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 5),
    _SwFdbStaticStatus_Type()
)
swFdbStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticStatus.setStatus("mandatory")
_SwFdbFilterTable_Object = MibTable
swFdbFilterTable = _SwFdbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2)
)
if mibBuilder.loadTexts:
    swFdbFilterTable.setStatus("mandatory")
_SwFdbFilterEntry_Object = MibTableRow
swFdbFilterEntry = _SwFdbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1)
)
swFdbFilterEntry.setIndexNames(
    (0, "DES3225G-MIB", "swFdbFilterVid"),
    (0, "DES3225G-MIB", "swFdbFilterAddressIndex"),
)
if mibBuilder.loadTexts:
    swFdbFilterEntry.setStatus("mandatory")
_SwFdbFilterVid_Type = Integer32
_SwFdbFilterVid_Object = MibTableColumn
swFdbFilterVid = _SwFdbFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 1),
    _SwFdbFilterVid_Type()
)
swFdbFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterVid.setStatus("mandatory")
_SwFdbFilterAddressIndex_Type = MacAddress
_SwFdbFilterAddressIndex_Object = MibTableColumn
swFdbFilterAddressIndex = _SwFdbFilterAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 2),
    _SwFdbFilterAddressIndex_Type()
)
swFdbFilterAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterAddressIndex.setStatus("mandatory")


class _SwFdbFilterState_Type(Integer32):
    """Custom type swFdbFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dst-src-addr", 2),
          ("invalid", 3),
          ("other", 1))
    )


_SwFdbFilterState_Type.__name__ = "Integer32"
_SwFdbFilterState_Object = MibTableColumn
swFdbFilterState = _SwFdbFilterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 3),
    _SwFdbFilterState_Type()
)
swFdbFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbFilterState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

portPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 0, 1)
)
portPartition.setObjects(
      *(("DES3225G-MIB", "swPortInfoModuleIndex"),
        ("DES3225G-MIB", "swPortInfoPortIndex"))
)
if mibBuilder.loadTexts:
    portPartition.setStatus(
        ""
    )

linkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 0, 2)
)
linkChangeEvent.setObjects(
      *(("DES3225G-MIB", "swPortInfoModuleIndex"),
        ("DES3225G-MIB", "swPortInfoPortIndex"))
)
if mibBuilder.loadTexts:
    linkChangeEvent.setStatus(
        ""
    )

broadcastRisingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 0, 3)
)
broadcastRisingStorm.setObjects(
      *(("DES3225G-MIB", "swPortInfoModuleIndex"),
        ("DES3225G-MIB", "swPortInfoPortIndex"))
)
if mibBuilder.loadTexts:
    broadcastRisingStorm.setStatus(
        ""
    )

broadcastFallingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 0, 4)
)
broadcastFallingStorm.setObjects(
      *(("DES3225G-MIB", "swPortInfoModuleIndex"),
        ("DES3225G-MIB", "swPortInfoPortIndex"))
)
if mibBuilder.loadTexts:
    broadcastFallingStorm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3225G-MIB",
    **{"MacAddress": MacAddress,
       "dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-Des3225gProd": dlink_Des3225gProd,
       "swProperty": swProperty,
       "portPartition": portPartition,
       "linkChangeEvent": linkChangeEvent,
       "broadcastRisingStorm": broadcastRisingStorm,
       "broadcastFallingStorm": broadcastFallingStorm,
       "swModule": swModule,
       "dlink-mgmt": dlink_mgmt,
       "des3225gSeries": des3225gSeries,
       "swDevPackage": swDevPackage,
       "swDevInfo": swDevInfo,
       "swDevInfoSystemUpTime": swDevInfoSystemUpTime,
       "swDevInfoMaxNumOfModule": swDevInfoMaxNumOfModule,
       "swDevInfoTotalNumOfModule": swDevInfoTotalNumOfModule,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortInUse": swDevInfoNumOfPortInUse,
       "swDevInfoConsoleInUse": swDevInfoConsoleInUse,
       "swDevInfoSystemLedStatus": swDevInfoSystemLedStatus,
       "swDevInfoSaveCfg": swDevInfoSaveCfg,
       "swDevCtrl": swDevCtrl,
       "swDevCtrlStpState": swDevCtrlStpState,
       "swDevIGMPCaptureState": swDevIGMPCaptureState,
       "swDevCtrlPartitionModeState": swDevCtrlPartitionModeState,
       "swDevCtrlTableLockState": swDevCtrlTableLockState,
       "swDevCtrlSaveCfg": swDevCtrlSaveCfg,
       "swDevCtrlHOLState": swDevCtrlHOLState,
       "swDevCtrlAddrLookupModesAndHitRate": swDevCtrlAddrLookupModesAndHitRate,
       "swDevCtrlUploadImageFileName": swDevCtrlUploadImageFileName,
       "swDevCtrlUploadImage": swDevCtrlUploadImage,
       "swDevAlarm": swDevAlarm,
       "swDevAlarmPartition": swDevAlarmPartition,
       "swDevAlarmNewRoot": swDevAlarmNewRoot,
       "swDevAlarmTopologyChange": swDevAlarmTopologyChange,
       "swDevAlarmLinkChange": swDevAlarmLinkChange,
       "swModulePackage": swModulePackage,
       "swModuleInfoTable": swModuleInfoTable,
       "swModuleInfoEntry": swModuleInfoEntry,
       "swModuleInfoIndex": swModuleInfoIndex,
       "swModuleInfoDesc": swModuleInfoDesc,
       "swModuleInfoType": swModuleInfoType,
       "swModuleInfoTotalNumOfPort": swModuleInfoTotalNumOfPort,
       "swModuleInfoNumOfPortInUse": swModuleInfoNumOfPortInUse,
       "swModuleInfoPortLedStatus": swModuleInfoPortLedStatus,
       "swPortPackage": swPortPackage,
       "swPortInfoTable": swPortInfoTable,
       "swPortInfoEntry": swPortInfoEntry,
       "swPortInfoModuleIndex": swPortInfoModuleIndex,
       "swPortInfoPortIndex": swPortInfoPortIndex,
       "swPortInfoType": swPortInfoType,
       "swPortInfoLinkStatus": swPortInfoLinkStatus,
       "swPortInfoNwayStatus": swPortInfoNwayStatus,
       "swPortInfoFlowCtrlStatus": swPortInfoFlowCtrlStatus,
       "swPortCtrlTable": swPortCtrlTable,
       "swPortCtrlEntry": swPortCtrlEntry,
       "swPortCtrlModuleIndex": swPortCtrlModuleIndex,
       "swPortCtrlPortIndex": swPortCtrlPortIndex,
       "swPortCtrlAdminState": swPortCtrlAdminState,
       "swPortCtrlLinkStatusAlarmState": swPortCtrlLinkStatusAlarmState,
       "swPortCtrlNwayState": swPortCtrlNwayState,
       "swPortCtrlFlowCtrlState": swPortCtrlFlowCtrlState,
       "swPortCtrlBackPressState": swPortCtrlBackPressState,
       "swPortCtrlLockState": swPortCtrlLockState,
       "swPortCtrlPriority": swPortCtrlPriority,
       "swPortCtrlStpState": swPortCtrlStpState,
       "swPortCtrlHOLState": swPortCtrlHOLState,
       "swPortCtrlBroadcastRisingThr": swPortCtrlBroadcastRisingThr,
       "swPortCtrlBroadcastFallingThr": swPortCtrlBroadcastFallingThr,
       "swPortCtrlBroadcastRisingAct": swPortCtrlBroadcastRisingAct,
       "swPortCtrlBroadcastFallingAct": swPortCtrlBroadcastFallingAct,
       "swPortCtrlCleanAllStatisticCounter": swPortCtrlCleanAllStatisticCounter,
       "swPortStTable": swPortStTable,
       "swPortStEntry": swPortStEntry,
       "swPortStModuleIndex": swPortStModuleIndex,
       "swPortStPortIndex": swPortStPortIndex,
       "swPortStByteRx": swPortStByteRx,
       "swPortStByteTx": swPortStByteTx,
       "swPortStFrameRx": swPortStFrameRx,
       "swPortStFrameTx": swPortStFrameTx,
       "swPortStTotalBytesRx": swPortStTotalBytesRx,
       "swPortStTotalFramesRx": swPortStTotalFramesRx,
       "swPortStBroadcastFramesRx": swPortStBroadcastFramesRx,
       "swPortStMulticastFramesRx": swPortStMulticastFramesRx,
       "swPortStCRCError": swPortStCRCError,
       "swPortStOversizeFrames": swPortStOversizeFrames,
       "swPortStFragments": swPortStFragments,
       "swPortStJabber": swPortStJabber,
       "swPortStCollision": swPortStCollision,
       "swPortStLateCollision": swPortStLateCollision,
       "swPortStFrames-64-bytes": swPortStFrames_64_bytes,
       "swPortStFrames-65-127-bytes": swPortStFrames_65_127_bytes,
       "swPortStFrames-128-255-bytes": swPortStFrames_128_255_bytes,
       "swPortStFrames-256-511-bytes": swPortStFrames_256_511_bytes,
       "swPortStFrames-512-1023-bytes": swPortStFrames_512_1023_bytes,
       "swPortStFrames-1024-1536-bytes": swPortStFrames_1024_1536_bytes,
       "swPortStFramesDroppedFrames": swPortStFramesDroppedFrames,
       "swPortStMulticastFramesTx": swPortStMulticastFramesTx,
       "swPortStBroadcastFramesTx": swPortStBroadcastFramesTx,
       "swPortStUndersizeFrames": swPortStUndersizeFrames,
       "swFdbPackage": swFdbPackage,
       "swFdbStaticTable": swFdbStaticTable,
       "swFdbStaticEntry": swFdbStaticEntry,
       "swFdbStaticVid": swFdbStaticVid,
       "swFdbStaticAddressIndex": swFdbStaticAddressIndex,
       "swFdbStaticPortMap": swFdbStaticPortMap,
       "swFdbStaticState": swFdbStaticState,
       "swFdbStaticStatus": swFdbStaticStatus,
       "swFdbFilterTable": swFdbFilterTable,
       "swFdbFilterEntry": swFdbFilterEntry,
       "swFdbFilterVid": swFdbFilterVid,
       "swFdbFilterAddressIndex": swFdbFilterAddressIndex,
       "swFdbFilterState": swFdbFilterState}
)
