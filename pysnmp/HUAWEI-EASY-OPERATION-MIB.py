# SNMP MIB module (HUAWEI-EASY-OPERATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-EASY-OPERATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:38 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwEasyOperationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311)
)
hwEasyOperationMIB.setRevisions(
        ("2014-09-09 00:00",
         "2014-06-04 00:00",
         "2013-12-30 00:00",
         "2013-08-05 00:00",
         "2013-03-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwEasyOperationGlobalObjects_ObjectIdentity = ObjectIdentity
hwEasyOperationGlobalObjects = _HwEasyOperationGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1)
)
_HwEasyOperationCommanderEnable_Type = EnabledStatus
_HwEasyOperationCommanderEnable_Object = MibScalar
hwEasyOperationCommanderEnable = _HwEasyOperationCommanderEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 1),
    _HwEasyOperationCommanderEnable_Type()
)
hwEasyOperationCommanderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationCommanderEnable.setStatus("current")
_HwEasyOperationCommanderIpAddress_Type = InetAddress
_HwEasyOperationCommanderIpAddress_Object = MibScalar
hwEasyOperationCommanderIpAddress = _HwEasyOperationCommanderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 2),
    _HwEasyOperationCommanderIpAddress_Type()
)
hwEasyOperationCommanderIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationCommanderIpAddress.setStatus("current")
_HwEasyOperationCommanderIpAddressType_Type = InetAddressType
_HwEasyOperationCommanderIpAddressType_Object = MibScalar
hwEasyOperationCommanderIpAddressType = _HwEasyOperationCommanderIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 3),
    _HwEasyOperationCommanderIpAddressType_Type()
)
hwEasyOperationCommanderIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationCommanderIpAddressType.setStatus("current")
_HwEasyOperationCommanderUdpPort_Type = Integer32
_HwEasyOperationCommanderUdpPort_Object = MibScalar
hwEasyOperationCommanderUdpPort = _HwEasyOperationCommanderUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 4),
    _HwEasyOperationCommanderUdpPort_Type()
)
hwEasyOperationCommanderUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationCommanderUdpPort.setStatus("current")


class _HwEasyOperationServerType_Type(Integer32):
    """Custom type hwEasyOperationServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_HwEasyOperationServerType_Type.__name__ = "Integer32"
_HwEasyOperationServerType_Object = MibScalar
hwEasyOperationServerType = _HwEasyOperationServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 5),
    _HwEasyOperationServerType_Type()
)
hwEasyOperationServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationServerType.setStatus("current")
_HwEasyOperationServerIpAddress_Type = InetAddress
_HwEasyOperationServerIpAddress_Object = MibScalar
hwEasyOperationServerIpAddress = _HwEasyOperationServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 6),
    _HwEasyOperationServerIpAddress_Type()
)
hwEasyOperationServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationServerIpAddress.setStatus("current")
_HwEasyOperationServerIpAddressType_Type = InetAddressType
_HwEasyOperationServerIpAddressType_Object = MibScalar
hwEasyOperationServerIpAddressType = _HwEasyOperationServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 7),
    _HwEasyOperationServerIpAddressType_Type()
)
hwEasyOperationServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationServerIpAddressType.setStatus("current")
_HwEasyOperationServerPort_Type = Integer32
_HwEasyOperationServerPort_Object = MibScalar
hwEasyOperationServerPort = _HwEasyOperationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 8),
    _HwEasyOperationServerPort_Type()
)
hwEasyOperationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationServerPort.setStatus("current")
_HwEasyOperationAutoClearEnable_Type = EnabledStatus
_HwEasyOperationAutoClearEnable_Object = MibScalar
hwEasyOperationAutoClearEnable = _HwEasyOperationAutoClearEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 9),
    _HwEasyOperationAutoClearEnable_Type()
)
hwEasyOperationAutoClearEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationAutoClearEnable.setStatus("current")


class _HwEasyOperationActivateMode_Type(Integer32):
    """Custom type hwEasyOperationActivateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reload", 2))
    )


_HwEasyOperationActivateMode_Type.__name__ = "Integer32"
_HwEasyOperationActivateMode_Object = MibScalar
hwEasyOperationActivateMode = _HwEasyOperationActivateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 10),
    _HwEasyOperationActivateMode_Type()
)
hwEasyOperationActivateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationActivateMode.setStatus("current")
_HwEasyOperationActivateDelayTime_Type = Integer32
_HwEasyOperationActivateDelayTime_Object = MibScalar
hwEasyOperationActivateDelayTime = _HwEasyOperationActivateDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 11),
    _HwEasyOperationActivateDelayTime_Type()
)
hwEasyOperationActivateDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationActivateDelayTime.setStatus("current")
_HwEasyOperationActivateInTime_Type = DisplayString
_HwEasyOperationActivateInTime_Object = MibScalar
hwEasyOperationActivateInTime = _HwEasyOperationActivateInTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 12),
    _HwEasyOperationActivateInTime_Type()
)
hwEasyOperationActivateInTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationActivateInTime.setStatus("current")


class _HwEasyOperationBackupConfigMode_Type(Integer32):
    """Custom type hwEasyOperationBackupConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplicate", 2),
          ("overwrite", 1))
    )


_HwEasyOperationBackupConfigMode_Type.__name__ = "Integer32"
_HwEasyOperationBackupConfigMode_Object = MibScalar
hwEasyOperationBackupConfigMode = _HwEasyOperationBackupConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 13),
    _HwEasyOperationBackupConfigMode_Type()
)
hwEasyOperationBackupConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationBackupConfigMode.setStatus("current")
_HwEasyOperationBackupConfigInterval_Type = Integer32
_HwEasyOperationBackupConfigInterval_Object = MibScalar
hwEasyOperationBackupConfigInterval = _HwEasyOperationBackupConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 14),
    _HwEasyOperationBackupConfigInterval_Type()
)
hwEasyOperationBackupConfigInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationBackupConfigInterval.setStatus("current")
_HwEasyOperationDefaultSysSoftware_Type = DisplayString
_HwEasyOperationDefaultSysSoftware_Object = MibScalar
hwEasyOperationDefaultSysSoftware = _HwEasyOperationDefaultSysSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 15),
    _HwEasyOperationDefaultSysSoftware_Type()
)
hwEasyOperationDefaultSysSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultSysSoftware.setStatus("current")
_HwEasyOperationDefaultSysSoftwareVer_Type = DisplayString
_HwEasyOperationDefaultSysSoftwareVer_Object = MibScalar
hwEasyOperationDefaultSysSoftwareVer = _HwEasyOperationDefaultSysSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 16),
    _HwEasyOperationDefaultSysSoftwareVer_Type()
)
hwEasyOperationDefaultSysSoftwareVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultSysSoftwareVer.setStatus("current")
_HwEasyOperationDefaultConfig_Type = DisplayString
_HwEasyOperationDefaultConfig_Object = MibScalar
hwEasyOperationDefaultConfig = _HwEasyOperationDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 17),
    _HwEasyOperationDefaultConfig_Type()
)
hwEasyOperationDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultConfig.setStatus("current")
_HwEasyOperationDefaultPatch_Type = DisplayString
_HwEasyOperationDefaultPatch_Object = MibScalar
hwEasyOperationDefaultPatch = _HwEasyOperationDefaultPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 18),
    _HwEasyOperationDefaultPatch_Type()
)
hwEasyOperationDefaultPatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultPatch.setStatus("current")
_HwEasyOperationDefaultWebfile_Type = DisplayString
_HwEasyOperationDefaultWebfile_Object = MibScalar
hwEasyOperationDefaultWebfile = _HwEasyOperationDefaultWebfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 19),
    _HwEasyOperationDefaultWebfile_Type()
)
hwEasyOperationDefaultWebfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultWebfile.setStatus("current")
_HwEasyOperationDefaultLicense_Type = DisplayString
_HwEasyOperationDefaultLicense_Object = MibScalar
hwEasyOperationDefaultLicense = _HwEasyOperationDefaultLicense_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 20),
    _HwEasyOperationDefaultLicense_Type()
)
hwEasyOperationDefaultLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultLicense.setStatus("current")
_HwEasyOperationDefaultCustomfile1_Type = DisplayString
_HwEasyOperationDefaultCustomfile1_Object = MibScalar
hwEasyOperationDefaultCustomfile1 = _HwEasyOperationDefaultCustomfile1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 21),
    _HwEasyOperationDefaultCustomfile1_Type()
)
hwEasyOperationDefaultCustomfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultCustomfile1.setStatus("current")
_HwEasyOperationDefaultCustomfile2_Type = DisplayString
_HwEasyOperationDefaultCustomfile2_Object = MibScalar
hwEasyOperationDefaultCustomfile2 = _HwEasyOperationDefaultCustomfile2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 22),
    _HwEasyOperationDefaultCustomfile2_Type()
)
hwEasyOperationDefaultCustomfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultCustomfile2.setStatus("current")
_HwEasyOperationDefaultCustomfile3_Type = DisplayString
_HwEasyOperationDefaultCustomfile3_Object = MibScalar
hwEasyOperationDefaultCustomfile3 = _HwEasyOperationDefaultCustomfile3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 23),
    _HwEasyOperationDefaultCustomfile3_Type()
)
hwEasyOperationDefaultCustomfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationDefaultCustomfile3.setStatus("current")
_HwEasyOperationClientAutoJoinEnable_Type = EnabledStatus
_HwEasyOperationClientAutoJoinEnable_Object = MibScalar
hwEasyOperationClientAutoJoinEnable = _HwEasyOperationClientAutoJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 24),
    _HwEasyOperationClientAutoJoinEnable_Type()
)
hwEasyOperationClientAutoJoinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationClientAutoJoinEnable.setStatus("current")
_HwEasyOperationTopologyEnable_Type = EnabledStatus
_HwEasyOperationTopologyEnable_Object = MibScalar
hwEasyOperationTopologyEnable = _HwEasyOperationTopologyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 25),
    _HwEasyOperationTopologyEnable_Type()
)
hwEasyOperationTopologyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyEnable.setStatus("current")
_HwEasyOperationClientAgingTime_Type = Integer32
_HwEasyOperationClientAgingTime_Object = MibScalar
hwEasyOperationClientAgingTime = _HwEasyOperationClientAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 1, 26),
    _HwEasyOperationClientAgingTime_Type()
)
hwEasyOperationClientAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationClientAgingTime.setStatus("current")
_HwEasyOperationGroup_ObjectIdentity = ObjectIdentity
hwEasyOperationGroup = _HwEasyOperationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2)
)
_HwEasyOperationTotalGroupNumber_Type = Integer32
_HwEasyOperationTotalGroupNumber_Object = MibScalar
hwEasyOperationTotalGroupNumber = _HwEasyOperationTotalGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 1),
    _HwEasyOperationTotalGroupNumber_Type()
)
hwEasyOperationTotalGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTotalGroupNumber.setStatus("current")
_HwEasyOperationBuildInGroupNumber_Type = Integer32
_HwEasyOperationBuildInGroupNumber_Object = MibScalar
hwEasyOperationBuildInGroupNumber = _HwEasyOperationBuildInGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 2),
    _HwEasyOperationBuildInGroupNumber_Type()
)
hwEasyOperationBuildInGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationBuildInGroupNumber.setStatus("current")
_HwEasyOperationCustomGroupNumber_Type = Integer32
_HwEasyOperationCustomGroupNumber_Object = MibScalar
hwEasyOperationCustomGroupNumber = _HwEasyOperationCustomGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 3),
    _HwEasyOperationCustomGroupNumber_Type()
)
hwEasyOperationCustomGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationCustomGroupNumber.setStatus("current")
_HwEasyOperationGroupTable_Object = MibTable
hwEasyOperationGroupTable = _HwEasyOperationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4)
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupTable.setStatus("current")
_HwEasyOperationGroupEntry_Object = MibTableRow
hwEasyOperationGroupEntry = _HwEasyOperationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1)
)
hwEasyOperationGroupEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupEntry.setStatus("current")


class _HwEasyOperationGroupIndex_Type(Integer32):
    """Custom type hwEasyOperationGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwEasyOperationGroupIndex_Type.__name__ = "Integer32"
_HwEasyOperationGroupIndex_Object = MibTableColumn
hwEasyOperationGroupIndex = _HwEasyOperationGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 1),
    _HwEasyOperationGroupIndex_Type()
)
hwEasyOperationGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationGroupIndex.setStatus("current")


class _HwEasyOperationGroupType_Type(Integer32):
    """Custom type hwEasyOperationGroupType based on Integer32"""
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
        *(("buildIn", 1),
          ("deviceType", 5),
          ("esn", 3),
          ("ipAddress", 6),
          ("macAddress", 2),
          ("model", 4))
    )


_HwEasyOperationGroupType_Type.__name__ = "Integer32"
_HwEasyOperationGroupType_Object = MibTableColumn
hwEasyOperationGroupType = _HwEasyOperationGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 2),
    _HwEasyOperationGroupType_Type()
)
hwEasyOperationGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupType.setStatus("current")
_HwEasyOperationGroupName_Type = DisplayString
_HwEasyOperationGroupName_Object = MibTableColumn
hwEasyOperationGroupName = _HwEasyOperationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 3),
    _HwEasyOperationGroupName_Type()
)
hwEasyOperationGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupName.setStatus("current")
_HwEasyOperationGroupSysSoftware_Type = DisplayString
_HwEasyOperationGroupSysSoftware_Object = MibTableColumn
hwEasyOperationGroupSysSoftware = _HwEasyOperationGroupSysSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 4),
    _HwEasyOperationGroupSysSoftware_Type()
)
hwEasyOperationGroupSysSoftware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupSysSoftware.setStatus("current")
_HwEasyOperationGroupSysSoftwareVer_Type = DisplayString
_HwEasyOperationGroupSysSoftwareVer_Object = MibTableColumn
hwEasyOperationGroupSysSoftwareVer = _HwEasyOperationGroupSysSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 5),
    _HwEasyOperationGroupSysSoftwareVer_Type()
)
hwEasyOperationGroupSysSoftwareVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupSysSoftwareVer.setStatus("current")
_HwEasyOperationGroupConfig_Type = DisplayString
_HwEasyOperationGroupConfig_Object = MibTableColumn
hwEasyOperationGroupConfig = _HwEasyOperationGroupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 6),
    _HwEasyOperationGroupConfig_Type()
)
hwEasyOperationGroupConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupConfig.setStatus("current")
_HwEasyOperationGroupPatch_Type = DisplayString
_HwEasyOperationGroupPatch_Object = MibTableColumn
hwEasyOperationGroupPatch = _HwEasyOperationGroupPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 7),
    _HwEasyOperationGroupPatch_Type()
)
hwEasyOperationGroupPatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupPatch.setStatus("current")
_HwEasyOperationGroupWebfile_Type = DisplayString
_HwEasyOperationGroupWebfile_Object = MibTableColumn
hwEasyOperationGroupWebfile = _HwEasyOperationGroupWebfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 8),
    _HwEasyOperationGroupWebfile_Type()
)
hwEasyOperationGroupWebfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupWebfile.setStatus("current")
_HwEasyOperationGroupLicense_Type = DisplayString
_HwEasyOperationGroupLicense_Object = MibTableColumn
hwEasyOperationGroupLicense = _HwEasyOperationGroupLicense_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 9),
    _HwEasyOperationGroupLicense_Type()
)
hwEasyOperationGroupLicense.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupLicense.setStatus("current")
_HwEasyOperationGroupCustomfile1_Type = DisplayString
_HwEasyOperationGroupCustomfile1_Object = MibTableColumn
hwEasyOperationGroupCustomfile1 = _HwEasyOperationGroupCustomfile1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 10),
    _HwEasyOperationGroupCustomfile1_Type()
)
hwEasyOperationGroupCustomfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupCustomfile1.setStatus("current")
_HwEasyOperationGroupCustomfile2_Type = DisplayString
_HwEasyOperationGroupCustomfile2_Object = MibTableColumn
hwEasyOperationGroupCustomfile2 = _HwEasyOperationGroupCustomfile2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 11),
    _HwEasyOperationGroupCustomfile2_Type()
)
hwEasyOperationGroupCustomfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupCustomfile2.setStatus("current")
_HwEasyOperationGroupCustomfile3_Type = DisplayString
_HwEasyOperationGroupCustomfile3_Object = MibTableColumn
hwEasyOperationGroupCustomfile3 = _HwEasyOperationGroupCustomfile3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 12),
    _HwEasyOperationGroupCustomfile3_Type()
)
hwEasyOperationGroupCustomfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupCustomfile3.setStatus("current")


class _HwEasyOperationGroupActivateMode_Type(Integer32):
    """Custom type hwEasyOperationGroupActivateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reload", 2))
    )


_HwEasyOperationGroupActivateMode_Type.__name__ = "Integer32"
_HwEasyOperationGroupActivateMode_Object = MibTableColumn
hwEasyOperationGroupActivateMode = _HwEasyOperationGroupActivateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 13),
    _HwEasyOperationGroupActivateMode_Type()
)
hwEasyOperationGroupActivateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupActivateMode.setStatus("current")
_HwEasyOperationGroupActivateDelayTime_Type = Integer32
_HwEasyOperationGroupActivateDelayTime_Object = MibTableColumn
hwEasyOperationGroupActivateDelayTime = _HwEasyOperationGroupActivateDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 14),
    _HwEasyOperationGroupActivateDelayTime_Type()
)
hwEasyOperationGroupActivateDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupActivateDelayTime.setStatus("current")
_HwEasyOperationGroupActivateInTime_Type = DisplayString
_HwEasyOperationGroupActivateInTime_Object = MibTableColumn
hwEasyOperationGroupActivateInTime = _HwEasyOperationGroupActivateInTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 15),
    _HwEasyOperationGroupActivateInTime_Type()
)
hwEasyOperationGroupActivateInTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupActivateInTime.setStatus("current")
_HwEasyOperationGroupRowStatus_Type = RowStatus
_HwEasyOperationGroupRowStatus_Object = MibTableColumn
hwEasyOperationGroupRowStatus = _HwEasyOperationGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 4, 1, 50),
    _HwEasyOperationGroupRowStatus_Type()
)
hwEasyOperationGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupRowStatus.setStatus("current")
_HwEasyOperationGroupMatchTable_Object = MibTable
hwEasyOperationGroupMatchTable = _HwEasyOperationGroupMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5)
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchTable.setStatus("current")
_HwEasyOperationGroupMatchEntry_Object = MibTableRow
hwEasyOperationGroupMatchEntry = _HwEasyOperationGroupMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1)
)
hwEasyOperationGroupMatchEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupIndex"),
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchEntry.setStatus("current")


class _HwEasyOperationGroupMatchIndex_Type(Integer32):
    """Custom type hwEasyOperationGroupMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwEasyOperationGroupMatchIndex_Type.__name__ = "Integer32"
_HwEasyOperationGroupMatchIndex_Object = MibTableColumn
hwEasyOperationGroupMatchIndex = _HwEasyOperationGroupMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 1),
    _HwEasyOperationGroupMatchIndex_Type()
)
hwEasyOperationGroupMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchIndex.setStatus("current")
_HwEasyOperationGroupMatchMacAddress_Type = MacAddress
_HwEasyOperationGroupMatchMacAddress_Object = MibTableColumn
hwEasyOperationGroupMatchMacAddress = _HwEasyOperationGroupMatchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 2),
    _HwEasyOperationGroupMatchMacAddress_Type()
)
hwEasyOperationGroupMatchMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchMacAddress.setStatus("current")
_HwEasyOperationGroupMatchMacMask_Type = Integer32
_HwEasyOperationGroupMatchMacMask_Object = MibTableColumn
hwEasyOperationGroupMatchMacMask = _HwEasyOperationGroupMatchMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 3),
    _HwEasyOperationGroupMatchMacMask_Type()
)
hwEasyOperationGroupMatchMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchMacMask.setStatus("current")
_HwEasyOperationGroupMatchEsn_Type = DisplayString
_HwEasyOperationGroupMatchEsn_Object = MibTableColumn
hwEasyOperationGroupMatchEsn = _HwEasyOperationGroupMatchEsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 4),
    _HwEasyOperationGroupMatchEsn_Type()
)
hwEasyOperationGroupMatchEsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchEsn.setStatus("current")
_HwEasyOperationGroupMatchModel_Type = DisplayString
_HwEasyOperationGroupMatchModel_Object = MibTableColumn
hwEasyOperationGroupMatchModel = _HwEasyOperationGroupMatchModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 5),
    _HwEasyOperationGroupMatchModel_Type()
)
hwEasyOperationGroupMatchModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchModel.setStatus("current")
_HwEasyOperationGroupMatchDeviceType_Type = DisplayString
_HwEasyOperationGroupMatchDeviceType_Object = MibTableColumn
hwEasyOperationGroupMatchDeviceType = _HwEasyOperationGroupMatchDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 6),
    _HwEasyOperationGroupMatchDeviceType_Type()
)
hwEasyOperationGroupMatchDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchDeviceType.setStatus("current")
_HwEasyOperationGroupMatchIpAddress_Type = InetAddress
_HwEasyOperationGroupMatchIpAddress_Object = MibTableColumn
hwEasyOperationGroupMatchIpAddress = _HwEasyOperationGroupMatchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 7),
    _HwEasyOperationGroupMatchIpAddress_Type()
)
hwEasyOperationGroupMatchIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchIpAddress.setStatus("current")
_HwEasyOperationGroupMatchIpAddressType_Type = InetAddressType
_HwEasyOperationGroupMatchIpAddressType_Object = MibTableColumn
hwEasyOperationGroupMatchIpAddressType = _HwEasyOperationGroupMatchIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 8),
    _HwEasyOperationGroupMatchIpAddressType_Type()
)
hwEasyOperationGroupMatchIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchIpAddressType.setStatus("current")
_HwEasyOperationGroupMatchIpAddressMask_Type = Integer32
_HwEasyOperationGroupMatchIpAddressMask_Object = MibTableColumn
hwEasyOperationGroupMatchIpAddressMask = _HwEasyOperationGroupMatchIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 9),
    _HwEasyOperationGroupMatchIpAddressMask_Type()
)
hwEasyOperationGroupMatchIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchIpAddressMask.setStatus("current")
_HwEasyOperationGroupMatchRowStatus_Type = RowStatus
_HwEasyOperationGroupMatchRowStatus_Object = MibTableColumn
hwEasyOperationGroupMatchRowStatus = _HwEasyOperationGroupMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 2, 5, 1, 50),
    _HwEasyOperationGroupMatchRowStatus_Type()
)
hwEasyOperationGroupMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchRowStatus.setStatus("current")
_HwEasyOperationClient_ObjectIdentity = ObjectIdentity
hwEasyOperationClient = _HwEasyOperationClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5)
)
_HwEasyOperationClientNumber_Type = Integer32
_HwEasyOperationClientNumber_Object = MibScalar
hwEasyOperationClientNumber = _HwEasyOperationClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 1),
    _HwEasyOperationClientNumber_Type()
)
hwEasyOperationClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientNumber.setStatus("current")
_HwEasyOperationClientInfoTable_Object = MibTable
hwEasyOperationClientInfoTable = _HwEasyOperationClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2)
)
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoTable.setStatus("current")
_HwEasyOperationClientInfoEntry_Object = MibTableRow
hwEasyOperationClientInfoEntry = _HwEasyOperationClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1)
)
hwEasyOperationClientInfoEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoEntry.setStatus("current")


class _HwEasyOperationClientInfoClientIndex_Type(Integer32):
    """Custom type hwEasyOperationClientInfoClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwEasyOperationClientInfoClientIndex_Type.__name__ = "Integer32"
_HwEasyOperationClientInfoClientIndex_Object = MibTableColumn
hwEasyOperationClientInfoClientIndex = _HwEasyOperationClientInfoClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 1),
    _HwEasyOperationClientInfoClientIndex_Type()
)
hwEasyOperationClientInfoClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientIndex.setStatus("current")
_HwEasyOperationClientInfoClientMacAddress_Type = MacAddress
_HwEasyOperationClientInfoClientMacAddress_Object = MibTableColumn
hwEasyOperationClientInfoClientMacAddress = _HwEasyOperationClientInfoClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 2),
    _HwEasyOperationClientInfoClientMacAddress_Type()
)
hwEasyOperationClientInfoClientMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientMacAddress.setStatus("current")
_HwEasyOperationClientInfoClientEsn_Type = DisplayString
_HwEasyOperationClientInfoClientEsn_Object = MibTableColumn
hwEasyOperationClientInfoClientEsn = _HwEasyOperationClientInfoClientEsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 3),
    _HwEasyOperationClientInfoClientEsn_Type()
)
hwEasyOperationClientInfoClientEsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientEsn.setStatus("current")
_HwEasyOperationClientInfoClientHostName_Type = DisplayString
_HwEasyOperationClientInfoClientHostName_Object = MibTableColumn
hwEasyOperationClientInfoClientHostName = _HwEasyOperationClientInfoClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 4),
    _HwEasyOperationClientInfoClientHostName_Type()
)
hwEasyOperationClientInfoClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientHostName.setStatus("current")
_HwEasyOperationClientInfoClientIpAddress_Type = InetAddress
_HwEasyOperationClientInfoClientIpAddress_Object = MibTableColumn
hwEasyOperationClientInfoClientIpAddress = _HwEasyOperationClientInfoClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 5),
    _HwEasyOperationClientInfoClientIpAddress_Type()
)
hwEasyOperationClientInfoClientIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientIpAddress.setStatus("current")
_HwEasyOperationClientInfoClientIpAddressType_Type = InetAddressType
_HwEasyOperationClientInfoClientIpAddressType_Object = MibTableColumn
hwEasyOperationClientInfoClientIpAddressType = _HwEasyOperationClientInfoClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 6),
    _HwEasyOperationClientInfoClientIpAddressType_Type()
)
hwEasyOperationClientInfoClientIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientIpAddressType.setStatus("current")
_HwEasyOperationClientInfoClientModel_Type = DisplayString
_HwEasyOperationClientInfoClientModel_Object = MibTableColumn
hwEasyOperationClientInfoClientModel = _HwEasyOperationClientInfoClientModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 7),
    _HwEasyOperationClientInfoClientModel_Type()
)
hwEasyOperationClientInfoClientModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientModel.setStatus("current")
_HwEasyOperationClientInfoClientDeviceType_Type = DisplayString
_HwEasyOperationClientInfoClientDeviceType_Object = MibTableColumn
hwEasyOperationClientInfoClientDeviceType = _HwEasyOperationClientInfoClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 8),
    _HwEasyOperationClientInfoClientDeviceType_Type()
)
hwEasyOperationClientInfoClientDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDeviceType.setStatus("current")
_HwEasyOperationClientInfoClientSysSoftware_Type = DisplayString
_HwEasyOperationClientInfoClientSysSoftware_Object = MibTableColumn
hwEasyOperationClientInfoClientSysSoftware = _HwEasyOperationClientInfoClientSysSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 9),
    _HwEasyOperationClientInfoClientSysSoftware_Type()
)
hwEasyOperationClientInfoClientSysSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysSoftware.setStatus("current")
_HwEasyOperationClientInfoClientSysSoftwareVer_Type = DisplayString
_HwEasyOperationClientInfoClientSysSoftwareVer_Object = MibTableColumn
hwEasyOperationClientInfoClientSysSoftwareVer = _HwEasyOperationClientInfoClientSysSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 10),
    _HwEasyOperationClientInfoClientSysSoftwareVer_Type()
)
hwEasyOperationClientInfoClientSysSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysSoftwareVer.setStatus("current")
_HwEasyOperationClientInfoClientSysConfig_Type = DisplayString
_HwEasyOperationClientInfoClientSysConfig_Object = MibTableColumn
hwEasyOperationClientInfoClientSysConfig = _HwEasyOperationClientInfoClientSysConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 11),
    _HwEasyOperationClientInfoClientSysConfig_Type()
)
hwEasyOperationClientInfoClientSysConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysConfig.setStatus("current")
_HwEasyOperationClientInfoClientSysPatch_Type = DisplayString
_HwEasyOperationClientInfoClientSysPatch_Object = MibTableColumn
hwEasyOperationClientInfoClientSysPatch = _HwEasyOperationClientInfoClientSysPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 12),
    _HwEasyOperationClientInfoClientSysPatch_Type()
)
hwEasyOperationClientInfoClientSysPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysPatch.setStatus("current")
_HwEasyOperationClientInfoClientSysWebFile_Type = DisplayString
_HwEasyOperationClientInfoClientSysWebFile_Object = MibTableColumn
hwEasyOperationClientInfoClientSysWebFile = _HwEasyOperationClientInfoClientSysWebFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 13),
    _HwEasyOperationClientInfoClientSysWebFile_Type()
)
hwEasyOperationClientInfoClientSysWebFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysWebFile.setStatus("current")
_HwEasyOperationClientInfoClientSysLicense_Type = DisplayString
_HwEasyOperationClientInfoClientSysLicense_Object = MibTableColumn
hwEasyOperationClientInfoClientSysLicense = _HwEasyOperationClientInfoClientSysLicense_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 14),
    _HwEasyOperationClientInfoClientSysLicense_Type()
)
hwEasyOperationClientInfoClientSysLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientSysLicense.setStatus("current")
_HwEasyOperationClientInfoClientDownloadSoftware_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadSoftware_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadSoftware = _HwEasyOperationClientInfoClientDownloadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 15),
    _HwEasyOperationClientInfoClientDownloadSoftware_Type()
)
hwEasyOperationClientInfoClientDownloadSoftware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadSoftware.setStatus("current")
_HwEasyOperationClientInfoClientDownloadSoftwareVer_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadSoftwareVer_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadSoftwareVer = _HwEasyOperationClientInfoClientDownloadSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 16),
    _HwEasyOperationClientInfoClientDownloadSoftwareVer_Type()
)
hwEasyOperationClientInfoClientDownloadSoftwareVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadSoftwareVer.setStatus("current")
_HwEasyOperationClientInfoClientDownloadConfig_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadConfig_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadConfig = _HwEasyOperationClientInfoClientDownloadConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 17),
    _HwEasyOperationClientInfoClientDownloadConfig_Type()
)
hwEasyOperationClientInfoClientDownloadConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadConfig.setStatus("current")
_HwEasyOperationClientInfoClientDownloadPatch_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadPatch_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadPatch = _HwEasyOperationClientInfoClientDownloadPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 18),
    _HwEasyOperationClientInfoClientDownloadPatch_Type()
)
hwEasyOperationClientInfoClientDownloadPatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadPatch.setStatus("current")
_HwEasyOperationClientInfoClientDownloadWebFile_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadWebFile_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadWebFile = _HwEasyOperationClientInfoClientDownloadWebFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 19),
    _HwEasyOperationClientInfoClientDownloadWebFile_Type()
)
hwEasyOperationClientInfoClientDownloadWebFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadWebFile.setStatus("current")
_HwEasyOperationClientInfoClientDownloadLicense_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadLicense_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadLicense = _HwEasyOperationClientInfoClientDownloadLicense_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 20),
    _HwEasyOperationClientInfoClientDownloadLicense_Type()
)
hwEasyOperationClientInfoClientDownloadLicense.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadLicense.setStatus("current")
_HwEasyOperationClientInfoClientDownloadCustomfile1_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadCustomfile1_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadCustomfile1 = _HwEasyOperationClientInfoClientDownloadCustomfile1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 21),
    _HwEasyOperationClientInfoClientDownloadCustomfile1_Type()
)
hwEasyOperationClientInfoClientDownloadCustomfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadCustomfile1.setStatus("current")
_HwEasyOperationClientInfoClientDownloadCustomfile2_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadCustomfile2_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadCustomfile2 = _HwEasyOperationClientInfoClientDownloadCustomfile2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 22),
    _HwEasyOperationClientInfoClientDownloadCustomfile2_Type()
)
hwEasyOperationClientInfoClientDownloadCustomfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadCustomfile2.setStatus("current")
_HwEasyOperationClientInfoClientDownloadCustomfile3_Type = DisplayString
_HwEasyOperationClientInfoClientDownloadCustomfile3_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadCustomfile3 = _HwEasyOperationClientInfoClientDownloadCustomfile3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 23),
    _HwEasyOperationClientInfoClientDownloadCustomfile3_Type()
)
hwEasyOperationClientInfoClientDownloadCustomfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadCustomfile3.setStatus("current")


class _HwEasyOperationClientInfoClientMethod_Type(Integer32):
    """Custom type hwEasyOperationClientInfoClientMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("unknown", 255),
          ("upgrade", 2),
          ("usbDownload", 4),
          ("zeroTouch", 3))
    )


_HwEasyOperationClientInfoClientMethod_Type.__name__ = "Integer32"
_HwEasyOperationClientInfoClientMethod_Object = MibTableColumn
hwEasyOperationClientInfoClientMethod = _HwEasyOperationClientInfoClientMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 24),
    _HwEasyOperationClientInfoClientMethod_Type()
)
hwEasyOperationClientInfoClientMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientMethod.setStatus("current")


class _HwEasyOperationClientInfoClientPhase_Type(Integer32):
    """Custom type hwEasyOperationClientInfoClientPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("activateFile", 5),
          ("downloadFile", 4),
          ("getDownloadInfo", 3),
          ("initial", 1),
          ("normalRunning", 6),
          ("requestIp", 2),
          ("unknown", 255))
    )


_HwEasyOperationClientInfoClientPhase_Type.__name__ = "Integer32"
_HwEasyOperationClientInfoClientPhase_Object = MibTableColumn
hwEasyOperationClientInfoClientPhase = _HwEasyOperationClientInfoClientPhase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 25),
    _HwEasyOperationClientInfoClientPhase_Type()
)
hwEasyOperationClientInfoClientPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientPhase.setStatus("current")


class _HwEasyOperationClientInfoClientOperateState_Type(Integer32):
    """Custom type hwEasyOperationClientInfoClientOperateState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("downloadConfig", 3),
          ("downloadCustomFile1", 7),
          ("downloadCustomFile2", 8),
          ("downloadCustomFile3", 9),
          ("downloadLicense", 6),
          ("downloadPatch", 4),
          ("downloadSoftware", 2),
          ("downloadWebFile", 5),
          ("finished", 1),
          ("unknown", 255))
    )


_HwEasyOperationClientInfoClientOperateState_Type.__name__ = "Integer32"
_HwEasyOperationClientInfoClientOperateState_Object = MibTableColumn
hwEasyOperationClientInfoClientOperateState = _HwEasyOperationClientInfoClientOperateState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 26),
    _HwEasyOperationClientInfoClientOperateState_Type()
)
hwEasyOperationClientInfoClientOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientOperateState.setStatus("current")
_HwEasyOperationClientInfoClientDownloadPercent_Type = Integer32
_HwEasyOperationClientInfoClientDownloadPercent_Object = MibTableColumn
hwEasyOperationClientInfoClientDownloadPercent = _HwEasyOperationClientInfoClientDownloadPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 27),
    _HwEasyOperationClientInfoClientDownloadPercent_Type()
)
hwEasyOperationClientInfoClientDownloadPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientDownloadPercent.setStatus("current")
_HwEasyOperationClientInfoClientErrorReason_Type = Integer32
_HwEasyOperationClientInfoClientErrorReason_Object = MibTableColumn
hwEasyOperationClientInfoClientErrorReason = _HwEasyOperationClientInfoClientErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 28),
    _HwEasyOperationClientInfoClientErrorReason_Type()
)
hwEasyOperationClientInfoClientErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientErrorReason.setStatus("current")
_HwEasyOperationClientInfoClientErrorDescr_Type = DisplayString
_HwEasyOperationClientInfoClientErrorDescr_Object = MibTableColumn
hwEasyOperationClientInfoClientErrorDescr = _HwEasyOperationClientInfoClientErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 29),
    _HwEasyOperationClientInfoClientErrorDescr_Type()
)
hwEasyOperationClientInfoClientErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientErrorDescr.setStatus("current")
_HwEasyOperationClientInfoClientBackupErrorReason_Type = Integer32
_HwEasyOperationClientInfoClientBackupErrorReason_Object = MibTableColumn
hwEasyOperationClientInfoClientBackupErrorReason = _HwEasyOperationClientInfoClientBackupErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 30),
    _HwEasyOperationClientInfoClientBackupErrorReason_Type()
)
hwEasyOperationClientInfoClientBackupErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientBackupErrorReason.setStatus("current")
_HwEasyOperationClientInfoClientBackupErrorDescr_Type = DisplayString
_HwEasyOperationClientInfoClientBackupErrorDescr_Object = MibTableColumn
hwEasyOperationClientInfoClientBackupErrorDescr = _HwEasyOperationClientInfoClientBackupErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 31),
    _HwEasyOperationClientInfoClientBackupErrorDescr_Type()
)
hwEasyOperationClientInfoClientBackupErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientBackupErrorDescr.setStatus("current")


class _HwEasyOperationClientInfoClientRunState_Type(Integer32):
    """Custom type hwEasyOperationClientInfoClientRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 5),
          ("initial", 1),
          ("lost", 4),
          ("normalRunning", 2),
          ("unknown", 255),
          ("upgrading", 3))
    )


_HwEasyOperationClientInfoClientRunState_Type.__name__ = "Integer32"
_HwEasyOperationClientInfoClientRunState_Object = MibTableColumn
hwEasyOperationClientInfoClientRunState = _HwEasyOperationClientInfoClientRunState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 32),
    _HwEasyOperationClientInfoClientRunState_Type()
)
hwEasyOperationClientInfoClientRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientRunState.setStatus("current")
_HwEasyOperationClientInfoClientCpuUsage_Type = Integer32
_HwEasyOperationClientInfoClientCpuUsage_Object = MibTableColumn
hwEasyOperationClientInfoClientCpuUsage = _HwEasyOperationClientInfoClientCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 33),
    _HwEasyOperationClientInfoClientCpuUsage_Type()
)
hwEasyOperationClientInfoClientCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientCpuUsage.setStatus("current")
_HwEasyOperationClientInfoClientMemoryUsage_Type = Integer32
_HwEasyOperationClientInfoClientMemoryUsage_Object = MibTableColumn
hwEasyOperationClientInfoClientMemoryUsage = _HwEasyOperationClientInfoClientMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 34),
    _HwEasyOperationClientInfoClientMemoryUsage_Type()
)
hwEasyOperationClientInfoClientMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientMemoryUsage.setStatus("current")
_HwEasyOperationClientInfoClientRowStatus_Type = RowStatus
_HwEasyOperationClientInfoClientRowStatus_Object = MibTableColumn
hwEasyOperationClientInfoClientRowStatus = _HwEasyOperationClientInfoClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 2, 1, 100),
    _HwEasyOperationClientInfoClientRowStatus_Type()
)
hwEasyOperationClientInfoClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoClientRowStatus.setStatus("current")
_HwEasyOperationClientReplaceTable_Object = MibTable
hwEasyOperationClientReplaceTable = _HwEasyOperationClientReplaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3)
)
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceTable.setStatus("current")
_HwEasyOperationClientReplaceEntry_Object = MibTableRow
hwEasyOperationClientReplaceEntry = _HwEasyOperationClientReplaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1)
)
hwEasyOperationClientReplaceEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceClientIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceEntry.setStatus("current")


class _HwEasyOperationClientReplaceClientIndex_Type(Integer32):
    """Custom type hwEasyOperationClientReplaceClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwEasyOperationClientReplaceClientIndex_Type.__name__ = "Integer32"
_HwEasyOperationClientReplaceClientIndex_Object = MibTableColumn
hwEasyOperationClientReplaceClientIndex = _HwEasyOperationClientReplaceClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 1),
    _HwEasyOperationClientReplaceClientIndex_Type()
)
hwEasyOperationClientReplaceClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceClientIndex.setStatus("current")
_HwEasyOperationClientReplaceNewMacAddress_Type = MacAddress
_HwEasyOperationClientReplaceNewMacAddress_Object = MibTableColumn
hwEasyOperationClientReplaceNewMacAddress = _HwEasyOperationClientReplaceNewMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 2),
    _HwEasyOperationClientReplaceNewMacAddress_Type()
)
hwEasyOperationClientReplaceNewMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceNewMacAddress.setStatus("current")
_HwEasyOperationClientReplaceNewEsn_Type = DisplayString
_HwEasyOperationClientReplaceNewEsn_Object = MibTableColumn
hwEasyOperationClientReplaceNewEsn = _HwEasyOperationClientReplaceNewEsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 3),
    _HwEasyOperationClientReplaceNewEsn_Type()
)
hwEasyOperationClientReplaceNewEsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceNewEsn.setStatus("current")
_HwEasyOperationClientReplaceDownloadSoftware_Type = DisplayString
_HwEasyOperationClientReplaceDownloadSoftware_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadSoftware = _HwEasyOperationClientReplaceDownloadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 4),
    _HwEasyOperationClientReplaceDownloadSoftware_Type()
)
hwEasyOperationClientReplaceDownloadSoftware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadSoftware.setStatus("current")
_HwEasyOperationClientReplaceDownloadSoftwareVer_Type = DisplayString
_HwEasyOperationClientReplaceDownloadSoftwareVer_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadSoftwareVer = _HwEasyOperationClientReplaceDownloadSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 5),
    _HwEasyOperationClientReplaceDownloadSoftwareVer_Type()
)
hwEasyOperationClientReplaceDownloadSoftwareVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadSoftwareVer.setStatus("current")
_HwEasyOperationClientReplaceDownloadPatch_Type = DisplayString
_HwEasyOperationClientReplaceDownloadPatch_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadPatch = _HwEasyOperationClientReplaceDownloadPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 6),
    _HwEasyOperationClientReplaceDownloadPatch_Type()
)
hwEasyOperationClientReplaceDownloadPatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadPatch.setStatus("current")
_HwEasyOperationClientReplaceDownloadWebFile_Type = DisplayString
_HwEasyOperationClientReplaceDownloadWebFile_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadWebFile = _HwEasyOperationClientReplaceDownloadWebFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 7),
    _HwEasyOperationClientReplaceDownloadWebFile_Type()
)
hwEasyOperationClientReplaceDownloadWebFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadWebFile.setStatus("current")
_HwEasyOperationClientReplaceDownloadLicense_Type = DisplayString
_HwEasyOperationClientReplaceDownloadLicense_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadLicense = _HwEasyOperationClientReplaceDownloadLicense_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 8),
    _HwEasyOperationClientReplaceDownloadLicense_Type()
)
hwEasyOperationClientReplaceDownloadLicense.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadLicense.setStatus("current")
_HwEasyOperationClientReplaceDownloadCustomfile1_Type = DisplayString
_HwEasyOperationClientReplaceDownloadCustomfile1_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadCustomfile1 = _HwEasyOperationClientReplaceDownloadCustomfile1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 9),
    _HwEasyOperationClientReplaceDownloadCustomfile1_Type()
)
hwEasyOperationClientReplaceDownloadCustomfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadCustomfile1.setStatus("current")
_HwEasyOperationClientReplaceDownloadCustomfile2_Type = DisplayString
_HwEasyOperationClientReplaceDownloadCustomfile2_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadCustomfile2 = _HwEasyOperationClientReplaceDownloadCustomfile2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 10),
    _HwEasyOperationClientReplaceDownloadCustomfile2_Type()
)
hwEasyOperationClientReplaceDownloadCustomfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadCustomfile2.setStatus("current")
_HwEasyOperationClientReplaceDownloadCustomfile3_Type = DisplayString
_HwEasyOperationClientReplaceDownloadCustomfile3_Object = MibTableColumn
hwEasyOperationClientReplaceDownloadCustomfile3 = _HwEasyOperationClientReplaceDownloadCustomfile3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 11),
    _HwEasyOperationClientReplaceDownloadCustomfile3_Type()
)
hwEasyOperationClientReplaceDownloadCustomfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceDownloadCustomfile3.setStatus("current")
_HwEasyOperationClientReplaceRowStatus_Type = RowStatus
_HwEasyOperationClientReplaceRowStatus_Object = MibTableColumn
hwEasyOperationClientReplaceRowStatus = _HwEasyOperationClientReplaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 5, 3, 1, 50),
    _HwEasyOperationClientReplaceRowStatus_Type()
)
hwEasyOperationClientReplaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceRowStatus.setStatus("current")
_HwEasyOperationNotification_ObjectIdentity = ObjectIdentity
hwEasyOperationNotification = _HwEasyOperationNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6)
)
_HwEasyOperationTrapVar_ObjectIdentity = ObjectIdentity
hwEasyOperationTrapVar = _HwEasyOperationTrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6, 1)
)
_HwEasyOperationTrap_ObjectIdentity = ObjectIdentity
hwEasyOperationTrap = _HwEasyOperationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6, 2)
)
_HwEasyOperationMonitor_ObjectIdentity = ObjectIdentity
hwEasyOperationMonitor = _HwEasyOperationMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7)
)
_HwEasyOperationPowerInfo_ObjectIdentity = ObjectIdentity
hwEasyOperationPowerInfo = _HwEasyOperationPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1)
)
_HwEasyOperationDevicePowerInfoTable_Object = MibTable
hwEasyOperationDevicePowerInfoTable = _HwEasyOperationDevicePowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoTable.setStatus("current")
_HwEasyOperationDevicePowerInfoEntry_Object = MibTableRow
hwEasyOperationDevicePowerInfoEntry = _HwEasyOperationDevicePowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1)
)
hwEasyOperationDevicePowerInfoEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDevicePowerInfoIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoEntry.setStatus("current")
_HwEasyOperationDevicePowerInfoIndex_Type = Integer32
_HwEasyOperationDevicePowerInfoIndex_Object = MibTableColumn
hwEasyOperationDevicePowerInfoIndex = _HwEasyOperationDevicePowerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1, 1),
    _HwEasyOperationDevicePowerInfoIndex_Type()
)
hwEasyOperationDevicePowerInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoIndex.setStatus("current")
_HwEasyOperationDevicePowerInfoCurrentPower_Type = Integer32
_HwEasyOperationDevicePowerInfoCurrentPower_Object = MibTableColumn
hwEasyOperationDevicePowerInfoCurrentPower = _HwEasyOperationDevicePowerInfoCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1, 2),
    _HwEasyOperationDevicePowerInfoCurrentPower_Type()
)
hwEasyOperationDevicePowerInfoCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoCurrentPower.setStatus("current")


class _HwEasyOperationDevicePowerInfoGauge_Type(Integer32):
    """Custom type hwEasyOperationDevicePowerInfoGauge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actual", 1),
          ("rated", 2))
    )


_HwEasyOperationDevicePowerInfoGauge_Type.__name__ = "Integer32"
_HwEasyOperationDevicePowerInfoGauge_Object = MibTableColumn
hwEasyOperationDevicePowerInfoGauge = _HwEasyOperationDevicePowerInfoGauge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1, 3),
    _HwEasyOperationDevicePowerInfoGauge_Type()
)
hwEasyOperationDevicePowerInfoGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoGauge.setStatus("current")
_HwEasyOperationDevicePowerInfoRatedPower_Type = Integer32
_HwEasyOperationDevicePowerInfoRatedPower_Object = MibTableColumn
hwEasyOperationDevicePowerInfoRatedPower = _HwEasyOperationDevicePowerInfoRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1, 4),
    _HwEasyOperationDevicePowerInfoRatedPower_Type()
)
hwEasyOperationDevicePowerInfoRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoRatedPower.setStatus("current")


class _HwEasyOperationDevicePowerInfoPowerManageMode_Type(Integer32):
    """Custom type hwEasyOperationDevicePowerInfoPowerManageMode based on Integer32"""
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
        *(("basic", 3),
          ("deep", 4),
          ("standard", 2),
          ("userDefined", 1))
    )


_HwEasyOperationDevicePowerInfoPowerManageMode_Type.__name__ = "Integer32"
_HwEasyOperationDevicePowerInfoPowerManageMode_Object = MibTableColumn
hwEasyOperationDevicePowerInfoPowerManageMode = _HwEasyOperationDevicePowerInfoPowerManageMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 1, 1, 5),
    _HwEasyOperationDevicePowerInfoPowerManageMode_Type()
)
hwEasyOperationDevicePowerInfoPowerManageMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoPowerManageMode.setStatus("current")
_HwEasyOperationPortPowerInfoTable_Object = MibTable
hwEasyOperationPortPowerInfoTable = _HwEasyOperationPortPowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoTable.setStatus("current")
_HwEasyOperationPortPowerInfoEntry_Object = MibTableRow
hwEasyOperationPortPowerInfoEntry = _HwEasyOperationPortPowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1)
)
hwEasyOperationPortPowerInfoEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationPortPowerInfoDeviceIndex"),
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationPortPowerInfoPortIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoEntry.setStatus("current")
_HwEasyOperationPortPowerInfoDeviceIndex_Type = Integer32
_HwEasyOperationPortPowerInfoDeviceIndex_Object = MibTableColumn
hwEasyOperationPortPowerInfoDeviceIndex = _HwEasyOperationPortPowerInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1, 1),
    _HwEasyOperationPortPowerInfoDeviceIndex_Type()
)
hwEasyOperationPortPowerInfoDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoDeviceIndex.setStatus("current")
_HwEasyOperationPortPowerInfoPortIndex_Type = Integer32
_HwEasyOperationPortPowerInfoPortIndex_Object = MibTableColumn
hwEasyOperationPortPowerInfoPortIndex = _HwEasyOperationPortPowerInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1, 2),
    _HwEasyOperationPortPowerInfoPortIndex_Type()
)
hwEasyOperationPortPowerInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoPortIndex.setStatus("current")
_HwEasyOperationPortPowerInfoPortName_Type = OctetString
_HwEasyOperationPortPowerInfoPortName_Object = MibTableColumn
hwEasyOperationPortPowerInfoPortName = _HwEasyOperationPortPowerInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1, 3),
    _HwEasyOperationPortPowerInfoPortName_Type()
)
hwEasyOperationPortPowerInfoPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoPortName.setStatus("current")
_HwEasyOperationPortPowerInfoCurrentPower_Type = Integer32
_HwEasyOperationPortPowerInfoCurrentPower_Object = MibTableColumn
hwEasyOperationPortPowerInfoCurrentPower = _HwEasyOperationPortPowerInfoCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1, 4),
    _HwEasyOperationPortPowerInfoCurrentPower_Type()
)
hwEasyOperationPortPowerInfoCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoCurrentPower.setStatus("current")


class _HwEasyOperationPortPowerInfoGauge_Type(Integer32):
    """Custom type hwEasyOperationPortPowerInfoGauge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actual", 1),
          ("presumed", 2))
    )


_HwEasyOperationPortPowerInfoGauge_Type.__name__ = "Integer32"
_HwEasyOperationPortPowerInfoGauge_Object = MibTableColumn
hwEasyOperationPortPowerInfoGauge = _HwEasyOperationPortPowerInfoGauge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 2, 1, 5),
    _HwEasyOperationPortPowerInfoGauge_Type()
)
hwEasyOperationPortPowerInfoGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoGauge.setStatus("current")
_HwEasyOperationNetPowerHistoryInfoTable_Object = MibTable
hwEasyOperationNetPowerHistoryInfoTable = _HwEasyOperationNetPowerHistoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 3)
)
if mibBuilder.loadTexts:
    hwEasyOperationNetPowerHistoryInfoTable.setStatus("current")
_HwEasyOperationNetPowerHistoryInfoEntry_Object = MibTableRow
hwEasyOperationNetPowerHistoryInfoEntry = _HwEasyOperationNetPowerHistoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 3, 1)
)
hwEasyOperationNetPowerHistoryInfoEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationNetPowerHistoryInfoIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationNetPowerHistoryInfoEntry.setStatus("current")
_HwEasyOperationNetPowerHistoryInfoIndex_Type = Integer32
_HwEasyOperationNetPowerHistoryInfoIndex_Object = MibTableColumn
hwEasyOperationNetPowerHistoryInfoIndex = _HwEasyOperationNetPowerHistoryInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 3, 1, 1),
    _HwEasyOperationNetPowerHistoryInfoIndex_Type()
)
hwEasyOperationNetPowerHistoryInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationNetPowerHistoryInfoIndex.setStatus("current")
_HwEasyOperationNetPowerHistoryInfoWholePower_Type = Integer32
_HwEasyOperationNetPowerHistoryInfoWholePower_Object = MibTableColumn
hwEasyOperationNetPowerHistoryInfoWholePower = _HwEasyOperationNetPowerHistoryInfoWholePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 1, 3, 1, 2),
    _HwEasyOperationNetPowerHistoryInfoWholePower_Type()
)
hwEasyOperationNetPowerHistoryInfoWholePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationNetPowerHistoryInfoWholePower.setStatus("current")
_HwEasyOperationTopologyTable_Object = MibTable
hwEasyOperationTopologyTable = _HwEasyOperationTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3)
)
if mibBuilder.loadTexts:
    hwEasyOperationTopologyTable.setStatus("current")
_HwEasyOperationTopologyEntry_Object = MibTableRow
hwEasyOperationTopologyEntry = _HwEasyOperationTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1)
)
hwEasyOperationTopologyEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyHopIndex"),
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyDeviceIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationTopologyEntry.setStatus("current")
_HwEasyOperationTopologyHopIndex_Type = Integer32
_HwEasyOperationTopologyHopIndex_Object = MibTableColumn
hwEasyOperationTopologyHopIndex = _HwEasyOperationTopologyHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 1),
    _HwEasyOperationTopologyHopIndex_Type()
)
hwEasyOperationTopologyHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyHopIndex.setStatus("current")
_HwEasyOperationTopologyDeviceIndex_Type = Integer32
_HwEasyOperationTopologyDeviceIndex_Object = MibTableColumn
hwEasyOperationTopologyDeviceIndex = _HwEasyOperationTopologyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 2),
    _HwEasyOperationTopologyDeviceIndex_Type()
)
hwEasyOperationTopologyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyDeviceIndex.setStatus("current")
_HwEasyOperationTopologyLocalMac_Type = MacAddress
_HwEasyOperationTopologyLocalMac_Object = MibTableColumn
hwEasyOperationTopologyLocalMac = _HwEasyOperationTopologyLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 3),
    _HwEasyOperationTopologyLocalMac_Type()
)
hwEasyOperationTopologyLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyLocalMac.setStatus("current")
_HwEasyOperationTopologyFatherMac_Type = MacAddress
_HwEasyOperationTopologyFatherMac_Object = MibTableColumn
hwEasyOperationTopologyFatherMac = _HwEasyOperationTopologyFatherMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 4),
    _HwEasyOperationTopologyFatherMac_Type()
)
hwEasyOperationTopologyFatherMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyFatherMac.setStatus("current")
_HwEasyOperationTopologyLocalPortName_Type = OctetString
_HwEasyOperationTopologyLocalPortName_Object = MibTableColumn
hwEasyOperationTopologyLocalPortName = _HwEasyOperationTopologyLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 5),
    _HwEasyOperationTopologyLocalPortName_Type()
)
hwEasyOperationTopologyLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyLocalPortName.setStatus("current")
_HwEasyOperationTopologyFatherPortName_Type = OctetString
_HwEasyOperationTopologyFatherPortName_Object = MibTableColumn
hwEasyOperationTopologyFatherPortName = _HwEasyOperationTopologyFatherPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 6),
    _HwEasyOperationTopologyFatherPortName_Type()
)
hwEasyOperationTopologyFatherPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyFatherPortName.setStatus("current")
_HwEasyOperationTopologyLocalDeviceId_Type = Integer32
_HwEasyOperationTopologyLocalDeviceId_Object = MibTableColumn
hwEasyOperationTopologyLocalDeviceId = _HwEasyOperationTopologyLocalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 7),
    _HwEasyOperationTopologyLocalDeviceId_Type()
)
hwEasyOperationTopologyLocalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyLocalDeviceId.setStatus("current")
_HwEasyOperationTopologyFatherDeviceId_Type = Integer32
_HwEasyOperationTopologyFatherDeviceId_Object = MibTableColumn
hwEasyOperationTopologyFatherDeviceId = _HwEasyOperationTopologyFatherDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 3, 1, 8),
    _HwEasyOperationTopologyFatherDeviceId_Type()
)
hwEasyOperationTopologyFatherDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationTopologyFatherDeviceId.setStatus("current")
_HwEasyOperationSavedTopologyTable_Object = MibTable
hwEasyOperationSavedTopologyTable = _HwEasyOperationSavedTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4)
)
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyTable.setStatus("current")
_HwEasyOperationSavedTopologyEntry_Object = MibTableRow
hwEasyOperationSavedTopologyEntry = _HwEasyOperationSavedTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1)
)
hwEasyOperationSavedTopologyEntry.setIndexNames(
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyHopIndex"),
    (0, "HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyDeviceIndex"),
)
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyEntry.setStatus("current")
_HwEasyOperationSavedTopologyHopIndex_Type = Integer32
_HwEasyOperationSavedTopologyHopIndex_Object = MibTableColumn
hwEasyOperationSavedTopologyHopIndex = _HwEasyOperationSavedTopologyHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 1),
    _HwEasyOperationSavedTopologyHopIndex_Type()
)
hwEasyOperationSavedTopologyHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyHopIndex.setStatus("current")
_HwEasyOperationSavedTopologyDeviceIndex_Type = Integer32
_HwEasyOperationSavedTopologyDeviceIndex_Object = MibTableColumn
hwEasyOperationSavedTopologyDeviceIndex = _HwEasyOperationSavedTopologyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 2),
    _HwEasyOperationSavedTopologyDeviceIndex_Type()
)
hwEasyOperationSavedTopologyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyDeviceIndex.setStatus("current")
_HwEasyOperationSavedTopologyLocalMac_Type = MacAddress
_HwEasyOperationSavedTopologyLocalMac_Object = MibTableColumn
hwEasyOperationSavedTopologyLocalMac = _HwEasyOperationSavedTopologyLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 3),
    _HwEasyOperationSavedTopologyLocalMac_Type()
)
hwEasyOperationSavedTopologyLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyLocalMac.setStatus("current")
_HwEasyOperationSavedTopologyFatherMac_Type = MacAddress
_HwEasyOperationSavedTopologyFatherMac_Object = MibTableColumn
hwEasyOperationSavedTopologyFatherMac = _HwEasyOperationSavedTopologyFatherMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 4),
    _HwEasyOperationSavedTopologyFatherMac_Type()
)
hwEasyOperationSavedTopologyFatherMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyFatherMac.setStatus("current")
_HwEasyOperationSavedTopologyLocalPortName_Type = OctetString
_HwEasyOperationSavedTopologyLocalPortName_Object = MibTableColumn
hwEasyOperationSavedTopologyLocalPortName = _HwEasyOperationSavedTopologyLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 5),
    _HwEasyOperationSavedTopologyLocalPortName_Type()
)
hwEasyOperationSavedTopologyLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyLocalPortName.setStatus("current")
_HwEasyOperationSavedTopologyFatherPortName_Type = OctetString
_HwEasyOperationSavedTopologyFatherPortName_Object = MibTableColumn
hwEasyOperationSavedTopologyFatherPortName = _HwEasyOperationSavedTopologyFatherPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 7, 4, 1, 6),
    _HwEasyOperationSavedTopologyFatherPortName_Type()
)
hwEasyOperationSavedTopologyFatherPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyFatherPortName.setStatus("current")

# Managed Objects groups

hwEasyOperationGlobalObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 1)
)
hwEasyOperationGlobalObjectsGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationCommanderIpAddressType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationBackupConfigMode"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationActivateInTime"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationActivateDelayTime"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationActivateMode"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationAutoClearEnable"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationServerIpAddressType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationServerIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationServerType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultSysSoftwareVer"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultConfig"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultPatch"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultWebfile"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultLicense"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultCustomfile1"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultCustomfile2"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultCustomfile3"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDefaultSysSoftware"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationBackupConfigInterval"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationCommanderUdpPort"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationServerPort"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientAgingTime"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyEnable"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationCommanderIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationCommanderEnable"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientAutoJoinEnable"))
)
if mibBuilder.loadTexts:
    hwEasyOperationGlobalObjectsGroup.setStatus("current")

hwEasyOperationGroupObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 2)
)
hwEasyOperationGroupObjectsGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTotalGroupNumber"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationBuildInGroupNumber"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationCustomGroupNumber"))
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupObjectsGroup.setStatus("current")

hwEasyOperationGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 3)
)
hwEasyOperationGroupTableGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupSysSoftware"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupSysSoftwareVer"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupConfig"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupPatch"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupWebfile"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupLicense"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupCustomfile1"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupCustomfile2"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupCustomfile3"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupActivateMode"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupActivateDelayTime"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupActivateInTime"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupTableGroup.setStatus("current")

hwEasyOperationGroupMatchTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 4)
)
hwEasyOperationGroupMatchTableGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchMacAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchEsn"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchModel"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchDeviceType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchRowStatus"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchMacMask"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchIpAddressType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationGroupMatchIpAddressMask"))
)
if mibBuilder.loadTexts:
    hwEasyOperationGroupMatchTableGroup.setStatus("current")

hwEasyOperationClientObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 5)
)
hwEasyOperationClientObjectsGroup.setObjects(
    ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientNumber")
)
if mibBuilder.loadTexts:
    hwEasyOperationClientObjectsGroup.setStatus("current")

hwEasyOperationClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 6)
)
hwEasyOperationClientInfoGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMacAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientEsn"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientModel"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDeviceType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysSoftware"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysSoftwareVer"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysConfig"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysPatch"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysWebFile"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientSysLicense"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadSoftware"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadSoftwareVer"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadConfig"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadPatch"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadWebFile"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadLicense"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadCustomfile1"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadCustomfile2"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadCustomfile3"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientErrorDescr"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientRowStatus"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientHostName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientBackupErrorDescr"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientBackupErrorReason"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientErrorReason"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientDownloadPercent"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIpAddressType"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMethod"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientPhase"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientOperateState"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientRunState"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientCpuUsage"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMemoryUsage"))
)
if mibBuilder.loadTexts:
    hwEasyOperationClientInfoGroup.setStatus("current")

hwEasyOperationClientReplaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 7)
)
hwEasyOperationClientReplaceGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceRowStatus"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadCustomfile3"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadCustomfile2"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadCustomfile1"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadLicense"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadWebFile"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadPatch"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadSoftwareVer"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceDownloadSoftware"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceNewEsn"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientReplaceNewMacAddress"))
)
if mibBuilder.loadTexts:
    hwEasyOperationClientReplaceGroup.setStatus("current")

hwEasyOperationDevicePowerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 9)
)
hwEasyOperationDevicePowerInfoGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDevicePowerInfoCurrentPower"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDevicePowerInfoGauge"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDevicePowerInfoRatedPower"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationDevicePowerInfoPowerManageMode"))
)
if mibBuilder.loadTexts:
    hwEasyOperationDevicePowerInfoGroup.setStatus("current")

hwEasyOperationPortPowerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 10)
)
hwEasyOperationPortPowerInfoGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationPortPowerInfoPortName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationPortPowerInfoCurrentPower"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationPortPowerInfoGauge"))
)
if mibBuilder.loadTexts:
    hwEasyOperationPortPowerInfoGroup.setStatus("current")

hwEasyOperationTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 11)
)
hwEasyOperationTopologyGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyLocalMac"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyFatherMac"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyLocalPortName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyFatherPortName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyLocalDeviceId"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationTopologyFatherDeviceId"))
)
if mibBuilder.loadTexts:
    hwEasyOperationTopologyGroup.setStatus("current")

hwEasyOperationSavedTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 12)
)
hwEasyOperationSavedTopologyGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyLocalMac"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyFatherMac"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyLocalPortName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationSavedTopologyFatherPortName"))
)
if mibBuilder.loadTexts:
    hwEasyOperationSavedTopologyGroup.setStatus("current")

hwEasyOperationNetPowerHistoryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 13)
)
hwEasyOperationNetPowerHistoryInfoGroup.setObjects(
    ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationNetPowerHistoryInfoWholePower")
)
if mibBuilder.loadTexts:
    hwEasyOperationNetPowerHistoryInfoGroup.setStatus("current")


# Notification objects

hwEasyOperationClientAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6, 2, 1)
)
hwEasyOperationClientAdded.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientHostName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMacAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientEsn"))
)
if mibBuilder.loadTexts:
    hwEasyOperationClientAdded.setStatus(
        "current"
    )

hwEasyOperationClientLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6, 2, 2)
)
hwEasyOperationClientLost.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientHostName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMacAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientEsn"))
)
if mibBuilder.loadTexts:
    hwEasyOperationClientLost.setStatus(
        "current"
    )

hwEasyOperationClientJoinNotPermit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 6, 2, 3)
)
hwEasyOperationClientJoinNotPermit.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientHostName"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientIpAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientMacAddress"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientInfoClientEsn"))
)
if mibBuilder.loadTexts:
    hwEasyOperationClientJoinNotPermit.setStatus(
        "current"
    )


# Notifications groups

hwEasyOperationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100, 8)
)
hwEasyOperationNotificationGroup.setObjects(
      *(("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientAdded"),
        ("HUAWEI-EASY-OPERATION-MIB", "hwEasyOperationClientLost"))
)
if mibBuilder.loadTexts:
    hwEasyOperationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEasyOperationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 311, 100)
)
if mibBuilder.loadTexts:
    hwEasyOperationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-EASY-OPERATION-MIB",
    **{"hwEasyOperationMIB": hwEasyOperationMIB,
       "hwEasyOperationGlobalObjects": hwEasyOperationGlobalObjects,
       "hwEasyOperationCommanderEnable": hwEasyOperationCommanderEnable,
       "hwEasyOperationCommanderIpAddress": hwEasyOperationCommanderIpAddress,
       "hwEasyOperationCommanderIpAddressType": hwEasyOperationCommanderIpAddressType,
       "hwEasyOperationCommanderUdpPort": hwEasyOperationCommanderUdpPort,
       "hwEasyOperationServerType": hwEasyOperationServerType,
       "hwEasyOperationServerIpAddress": hwEasyOperationServerIpAddress,
       "hwEasyOperationServerIpAddressType": hwEasyOperationServerIpAddressType,
       "hwEasyOperationServerPort": hwEasyOperationServerPort,
       "hwEasyOperationAutoClearEnable": hwEasyOperationAutoClearEnable,
       "hwEasyOperationActivateMode": hwEasyOperationActivateMode,
       "hwEasyOperationActivateDelayTime": hwEasyOperationActivateDelayTime,
       "hwEasyOperationActivateInTime": hwEasyOperationActivateInTime,
       "hwEasyOperationBackupConfigMode": hwEasyOperationBackupConfigMode,
       "hwEasyOperationBackupConfigInterval": hwEasyOperationBackupConfigInterval,
       "hwEasyOperationDefaultSysSoftware": hwEasyOperationDefaultSysSoftware,
       "hwEasyOperationDefaultSysSoftwareVer": hwEasyOperationDefaultSysSoftwareVer,
       "hwEasyOperationDefaultConfig": hwEasyOperationDefaultConfig,
       "hwEasyOperationDefaultPatch": hwEasyOperationDefaultPatch,
       "hwEasyOperationDefaultWebfile": hwEasyOperationDefaultWebfile,
       "hwEasyOperationDefaultLicense": hwEasyOperationDefaultLicense,
       "hwEasyOperationDefaultCustomfile1": hwEasyOperationDefaultCustomfile1,
       "hwEasyOperationDefaultCustomfile2": hwEasyOperationDefaultCustomfile2,
       "hwEasyOperationDefaultCustomfile3": hwEasyOperationDefaultCustomfile3,
       "hwEasyOperationClientAutoJoinEnable": hwEasyOperationClientAutoJoinEnable,
       "hwEasyOperationTopologyEnable": hwEasyOperationTopologyEnable,
       "hwEasyOperationClientAgingTime": hwEasyOperationClientAgingTime,
       "hwEasyOperationGroup": hwEasyOperationGroup,
       "hwEasyOperationTotalGroupNumber": hwEasyOperationTotalGroupNumber,
       "hwEasyOperationBuildInGroupNumber": hwEasyOperationBuildInGroupNumber,
       "hwEasyOperationCustomGroupNumber": hwEasyOperationCustomGroupNumber,
       "hwEasyOperationGroupTable": hwEasyOperationGroupTable,
       "hwEasyOperationGroupEntry": hwEasyOperationGroupEntry,
       "hwEasyOperationGroupIndex": hwEasyOperationGroupIndex,
       "hwEasyOperationGroupType": hwEasyOperationGroupType,
       "hwEasyOperationGroupName": hwEasyOperationGroupName,
       "hwEasyOperationGroupSysSoftware": hwEasyOperationGroupSysSoftware,
       "hwEasyOperationGroupSysSoftwareVer": hwEasyOperationGroupSysSoftwareVer,
       "hwEasyOperationGroupConfig": hwEasyOperationGroupConfig,
       "hwEasyOperationGroupPatch": hwEasyOperationGroupPatch,
       "hwEasyOperationGroupWebfile": hwEasyOperationGroupWebfile,
       "hwEasyOperationGroupLicense": hwEasyOperationGroupLicense,
       "hwEasyOperationGroupCustomfile1": hwEasyOperationGroupCustomfile1,
       "hwEasyOperationGroupCustomfile2": hwEasyOperationGroupCustomfile2,
       "hwEasyOperationGroupCustomfile3": hwEasyOperationGroupCustomfile3,
       "hwEasyOperationGroupActivateMode": hwEasyOperationGroupActivateMode,
       "hwEasyOperationGroupActivateDelayTime": hwEasyOperationGroupActivateDelayTime,
       "hwEasyOperationGroupActivateInTime": hwEasyOperationGroupActivateInTime,
       "hwEasyOperationGroupRowStatus": hwEasyOperationGroupRowStatus,
       "hwEasyOperationGroupMatchTable": hwEasyOperationGroupMatchTable,
       "hwEasyOperationGroupMatchEntry": hwEasyOperationGroupMatchEntry,
       "hwEasyOperationGroupMatchIndex": hwEasyOperationGroupMatchIndex,
       "hwEasyOperationGroupMatchMacAddress": hwEasyOperationGroupMatchMacAddress,
       "hwEasyOperationGroupMatchMacMask": hwEasyOperationGroupMatchMacMask,
       "hwEasyOperationGroupMatchEsn": hwEasyOperationGroupMatchEsn,
       "hwEasyOperationGroupMatchModel": hwEasyOperationGroupMatchModel,
       "hwEasyOperationGroupMatchDeviceType": hwEasyOperationGroupMatchDeviceType,
       "hwEasyOperationGroupMatchIpAddress": hwEasyOperationGroupMatchIpAddress,
       "hwEasyOperationGroupMatchIpAddressType": hwEasyOperationGroupMatchIpAddressType,
       "hwEasyOperationGroupMatchIpAddressMask": hwEasyOperationGroupMatchIpAddressMask,
       "hwEasyOperationGroupMatchRowStatus": hwEasyOperationGroupMatchRowStatus,
       "hwEasyOperationClient": hwEasyOperationClient,
       "hwEasyOperationClientNumber": hwEasyOperationClientNumber,
       "hwEasyOperationClientInfoTable": hwEasyOperationClientInfoTable,
       "hwEasyOperationClientInfoEntry": hwEasyOperationClientInfoEntry,
       "hwEasyOperationClientInfoClientIndex": hwEasyOperationClientInfoClientIndex,
       "hwEasyOperationClientInfoClientMacAddress": hwEasyOperationClientInfoClientMacAddress,
       "hwEasyOperationClientInfoClientEsn": hwEasyOperationClientInfoClientEsn,
       "hwEasyOperationClientInfoClientHostName": hwEasyOperationClientInfoClientHostName,
       "hwEasyOperationClientInfoClientIpAddress": hwEasyOperationClientInfoClientIpAddress,
       "hwEasyOperationClientInfoClientIpAddressType": hwEasyOperationClientInfoClientIpAddressType,
       "hwEasyOperationClientInfoClientModel": hwEasyOperationClientInfoClientModel,
       "hwEasyOperationClientInfoClientDeviceType": hwEasyOperationClientInfoClientDeviceType,
       "hwEasyOperationClientInfoClientSysSoftware": hwEasyOperationClientInfoClientSysSoftware,
       "hwEasyOperationClientInfoClientSysSoftwareVer": hwEasyOperationClientInfoClientSysSoftwareVer,
       "hwEasyOperationClientInfoClientSysConfig": hwEasyOperationClientInfoClientSysConfig,
       "hwEasyOperationClientInfoClientSysPatch": hwEasyOperationClientInfoClientSysPatch,
       "hwEasyOperationClientInfoClientSysWebFile": hwEasyOperationClientInfoClientSysWebFile,
       "hwEasyOperationClientInfoClientSysLicense": hwEasyOperationClientInfoClientSysLicense,
       "hwEasyOperationClientInfoClientDownloadSoftware": hwEasyOperationClientInfoClientDownloadSoftware,
       "hwEasyOperationClientInfoClientDownloadSoftwareVer": hwEasyOperationClientInfoClientDownloadSoftwareVer,
       "hwEasyOperationClientInfoClientDownloadConfig": hwEasyOperationClientInfoClientDownloadConfig,
       "hwEasyOperationClientInfoClientDownloadPatch": hwEasyOperationClientInfoClientDownloadPatch,
       "hwEasyOperationClientInfoClientDownloadWebFile": hwEasyOperationClientInfoClientDownloadWebFile,
       "hwEasyOperationClientInfoClientDownloadLicense": hwEasyOperationClientInfoClientDownloadLicense,
       "hwEasyOperationClientInfoClientDownloadCustomfile1": hwEasyOperationClientInfoClientDownloadCustomfile1,
       "hwEasyOperationClientInfoClientDownloadCustomfile2": hwEasyOperationClientInfoClientDownloadCustomfile2,
       "hwEasyOperationClientInfoClientDownloadCustomfile3": hwEasyOperationClientInfoClientDownloadCustomfile3,
       "hwEasyOperationClientInfoClientMethod": hwEasyOperationClientInfoClientMethod,
       "hwEasyOperationClientInfoClientPhase": hwEasyOperationClientInfoClientPhase,
       "hwEasyOperationClientInfoClientOperateState": hwEasyOperationClientInfoClientOperateState,
       "hwEasyOperationClientInfoClientDownloadPercent": hwEasyOperationClientInfoClientDownloadPercent,
       "hwEasyOperationClientInfoClientErrorReason": hwEasyOperationClientInfoClientErrorReason,
       "hwEasyOperationClientInfoClientErrorDescr": hwEasyOperationClientInfoClientErrorDescr,
       "hwEasyOperationClientInfoClientBackupErrorReason": hwEasyOperationClientInfoClientBackupErrorReason,
       "hwEasyOperationClientInfoClientBackupErrorDescr": hwEasyOperationClientInfoClientBackupErrorDescr,
       "hwEasyOperationClientInfoClientRunState": hwEasyOperationClientInfoClientRunState,
       "hwEasyOperationClientInfoClientCpuUsage": hwEasyOperationClientInfoClientCpuUsage,
       "hwEasyOperationClientInfoClientMemoryUsage": hwEasyOperationClientInfoClientMemoryUsage,
       "hwEasyOperationClientInfoClientRowStatus": hwEasyOperationClientInfoClientRowStatus,
       "hwEasyOperationClientReplaceTable": hwEasyOperationClientReplaceTable,
       "hwEasyOperationClientReplaceEntry": hwEasyOperationClientReplaceEntry,
       "hwEasyOperationClientReplaceClientIndex": hwEasyOperationClientReplaceClientIndex,
       "hwEasyOperationClientReplaceNewMacAddress": hwEasyOperationClientReplaceNewMacAddress,
       "hwEasyOperationClientReplaceNewEsn": hwEasyOperationClientReplaceNewEsn,
       "hwEasyOperationClientReplaceDownloadSoftware": hwEasyOperationClientReplaceDownloadSoftware,
       "hwEasyOperationClientReplaceDownloadSoftwareVer": hwEasyOperationClientReplaceDownloadSoftwareVer,
       "hwEasyOperationClientReplaceDownloadPatch": hwEasyOperationClientReplaceDownloadPatch,
       "hwEasyOperationClientReplaceDownloadWebFile": hwEasyOperationClientReplaceDownloadWebFile,
       "hwEasyOperationClientReplaceDownloadLicense": hwEasyOperationClientReplaceDownloadLicense,
       "hwEasyOperationClientReplaceDownloadCustomfile1": hwEasyOperationClientReplaceDownloadCustomfile1,
       "hwEasyOperationClientReplaceDownloadCustomfile2": hwEasyOperationClientReplaceDownloadCustomfile2,
       "hwEasyOperationClientReplaceDownloadCustomfile3": hwEasyOperationClientReplaceDownloadCustomfile3,
       "hwEasyOperationClientReplaceRowStatus": hwEasyOperationClientReplaceRowStatus,
       "hwEasyOperationNotification": hwEasyOperationNotification,
       "hwEasyOperationTrapVar": hwEasyOperationTrapVar,
       "hwEasyOperationTrap": hwEasyOperationTrap,
       "hwEasyOperationClientAdded": hwEasyOperationClientAdded,
       "hwEasyOperationClientLost": hwEasyOperationClientLost,
       "hwEasyOperationClientJoinNotPermit": hwEasyOperationClientJoinNotPermit,
       "hwEasyOperationMonitor": hwEasyOperationMonitor,
       "hwEasyOperationPowerInfo": hwEasyOperationPowerInfo,
       "hwEasyOperationDevicePowerInfoTable": hwEasyOperationDevicePowerInfoTable,
       "hwEasyOperationDevicePowerInfoEntry": hwEasyOperationDevicePowerInfoEntry,
       "hwEasyOperationDevicePowerInfoIndex": hwEasyOperationDevicePowerInfoIndex,
       "hwEasyOperationDevicePowerInfoCurrentPower": hwEasyOperationDevicePowerInfoCurrentPower,
       "hwEasyOperationDevicePowerInfoGauge": hwEasyOperationDevicePowerInfoGauge,
       "hwEasyOperationDevicePowerInfoRatedPower": hwEasyOperationDevicePowerInfoRatedPower,
       "hwEasyOperationDevicePowerInfoPowerManageMode": hwEasyOperationDevicePowerInfoPowerManageMode,
       "hwEasyOperationPortPowerInfoTable": hwEasyOperationPortPowerInfoTable,
       "hwEasyOperationPortPowerInfoEntry": hwEasyOperationPortPowerInfoEntry,
       "hwEasyOperationPortPowerInfoDeviceIndex": hwEasyOperationPortPowerInfoDeviceIndex,
       "hwEasyOperationPortPowerInfoPortIndex": hwEasyOperationPortPowerInfoPortIndex,
       "hwEasyOperationPortPowerInfoPortName": hwEasyOperationPortPowerInfoPortName,
       "hwEasyOperationPortPowerInfoCurrentPower": hwEasyOperationPortPowerInfoCurrentPower,
       "hwEasyOperationPortPowerInfoGauge": hwEasyOperationPortPowerInfoGauge,
       "hwEasyOperationNetPowerHistoryInfoTable": hwEasyOperationNetPowerHistoryInfoTable,
       "hwEasyOperationNetPowerHistoryInfoEntry": hwEasyOperationNetPowerHistoryInfoEntry,
       "hwEasyOperationNetPowerHistoryInfoIndex": hwEasyOperationNetPowerHistoryInfoIndex,
       "hwEasyOperationNetPowerHistoryInfoWholePower": hwEasyOperationNetPowerHistoryInfoWholePower,
       "hwEasyOperationTopologyTable": hwEasyOperationTopologyTable,
       "hwEasyOperationTopologyEntry": hwEasyOperationTopologyEntry,
       "hwEasyOperationTopologyHopIndex": hwEasyOperationTopologyHopIndex,
       "hwEasyOperationTopologyDeviceIndex": hwEasyOperationTopologyDeviceIndex,
       "hwEasyOperationTopologyLocalMac": hwEasyOperationTopologyLocalMac,
       "hwEasyOperationTopologyFatherMac": hwEasyOperationTopologyFatherMac,
       "hwEasyOperationTopologyLocalPortName": hwEasyOperationTopologyLocalPortName,
       "hwEasyOperationTopologyFatherPortName": hwEasyOperationTopologyFatherPortName,
       "hwEasyOperationTopologyLocalDeviceId": hwEasyOperationTopologyLocalDeviceId,
       "hwEasyOperationTopologyFatherDeviceId": hwEasyOperationTopologyFatherDeviceId,
       "hwEasyOperationSavedTopologyTable": hwEasyOperationSavedTopologyTable,
       "hwEasyOperationSavedTopologyEntry": hwEasyOperationSavedTopologyEntry,
       "hwEasyOperationSavedTopologyHopIndex": hwEasyOperationSavedTopologyHopIndex,
       "hwEasyOperationSavedTopologyDeviceIndex": hwEasyOperationSavedTopologyDeviceIndex,
       "hwEasyOperationSavedTopologyLocalMac": hwEasyOperationSavedTopologyLocalMac,
       "hwEasyOperationSavedTopologyFatherMac": hwEasyOperationSavedTopologyFatherMac,
       "hwEasyOperationSavedTopologyLocalPortName": hwEasyOperationSavedTopologyLocalPortName,
       "hwEasyOperationSavedTopologyFatherPortName": hwEasyOperationSavedTopologyFatherPortName,
       "hwEasyOperationCompliance": hwEasyOperationCompliance,
       "hwEasyOperationGlobalObjectsGroup": hwEasyOperationGlobalObjectsGroup,
       "hwEasyOperationGroupObjectsGroup": hwEasyOperationGroupObjectsGroup,
       "hwEasyOperationGroupTableGroup": hwEasyOperationGroupTableGroup,
       "hwEasyOperationGroupMatchTableGroup": hwEasyOperationGroupMatchTableGroup,
       "hwEasyOperationClientObjectsGroup": hwEasyOperationClientObjectsGroup,
       "hwEasyOperationClientInfoGroup": hwEasyOperationClientInfoGroup,
       "hwEasyOperationClientReplaceGroup": hwEasyOperationClientReplaceGroup,
       "hwEasyOperationNotificationGroup": hwEasyOperationNotificationGroup,
       "hwEasyOperationDevicePowerInfoGroup": hwEasyOperationDevicePowerInfoGroup,
       "hwEasyOperationPortPowerInfoGroup": hwEasyOperationPortPowerInfoGroup,
       "hwEasyOperationTopologyGroup": hwEasyOperationTopologyGroup,
       "hwEasyOperationSavedTopologyGroup": hwEasyOperationSavedTopologyGroup,
       "hwEasyOperationNetPowerHistoryInfoGroup": hwEasyOperationNetPowerHistoryInfoGroup}
)
