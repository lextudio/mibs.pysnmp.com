# SNMP MIB module (MRV-IN-REACH-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:47 2024
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

(AddressType,
 ChassisType,
 DateTime,
 HardwareType,
 TypedAddress,
 mrvInReachProductDivision) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "AddressType",
    "ChassisType",
    "DateTime",
    "HardwareType",
    "TypedAddress",
    "mrvInReachProductDivision")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XSystem_ObjectIdentity = ObjectIdentity
xSystem = _XSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 1)
)


class _SysIdent_Type(DisplayString):
    """Custom type sysIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SysIdent_Type.__name__ = "DisplayString"
_SysIdent_Object = MibScalar
sysIdent = _SysIdent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 1),
    _SysIdent_Type()
)
sysIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdent.setStatus("mandatory")


class _SysDefineMode_Type(Integer32):
    """Custom type sysDefineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operAndPerm", 2),
          ("permOnly", 1))
    )


_SysDefineMode_Type.__name__ = "Integer32"
_SysDefineMode_Object = MibScalar
sysDefineMode = _SysDefineMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 2),
    _SysDefineMode_Type()
)
sysDefineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefineMode.setStatus("mandatory")
_SysDateTime_Type = DateTime
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 3),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("mandatory")


class _SysTimeZone_Type(OctetString):
    """Custom type sysTimeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysTimeZone_Type.__name__ = "OctetString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 4),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("mandatory")


class _SysLoadSoftware_Type(DisplayString):
    """Custom type sysLoadSoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysLoadSoftware_Type.__name__ = "DisplayString"
_SysLoadSoftware_Object = MibScalar
sysLoadSoftware = _SysLoadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 5),
    _SysLoadSoftware_Type()
)
sysLoadSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoadSoftware.setStatus("mandatory")


class _SysDump_Type(Integer32):
    """Custom type sysDump based on Integer32"""
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


_SysDump_Type.__name__ = "Integer32"
_SysDump_Object = MibScalar
sysDump = _SysDump_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 6),
    _SysDump_Type()
)
sysDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDump.setStatus("mandatory")


class _SysMaintenancePassword_Type(OctetString):
    """Custom type sysMaintenancePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysMaintenancePassword_Type.__name__ = "OctetString"
_SysMaintenancePassword_Object = MibScalar
sysMaintenancePassword = _SysMaintenancePassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 7),
    _SysMaintenancePassword_Type()
)
sysMaintenancePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaintenancePassword.setStatus("mandatory")


class _SysLocalName_Type(DisplayString):
    """Custom type sysLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SysLocalName_Type.__name__ = "DisplayString"
_SysLocalName_Object = MibScalar
sysLocalName = _SysLocalName_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 8),
    _SysLocalName_Type()
)
sysLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalName.setStatus("mandatory")


class _SysSoftwareVersionType_Type(Integer32):
    """Custom type sysSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("production", 3),
          ("special", 4))
    )


_SysSoftwareVersionType_Type.__name__ = "Integer32"
_SysSoftwareVersionType_Object = MibScalar
sysSoftwareVersionType = _SysSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 9),
    _SysSoftwareVersionType_Type()
)
sysSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersionType.setStatus("mandatory")


class _SysSoftwareVersion_Type(OctetString):
    """Custom type sysSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SysSoftwareVersion_Type.__name__ = "OctetString"
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 10),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("mandatory")
_SysRomVersion_Type = Integer32
_SysRomVersion_Object = MibScalar
sysRomVersion = _SysRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 11),
    _SysRomVersion_Type()
)
sysRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRomVersion.setStatus("mandatory")
_SysHardwareType_Type = HardwareType
_SysHardwareType_Object = MibScalar
sysHardwareType = _SysHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 12),
    _SysHardwareType_Type()
)
sysHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareType.setStatus("mandatory")
_SysHardwareVersion_Type = Integer32
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 13),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("mandatory")
_SysChassisType_Type = ChassisType
_SysChassisType_Object = MibScalar
sysChassisType = _SysChassisType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 14),
    _SysChassisType_Type()
)
sysChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisType.setStatus("mandatory")
_SysChassisVersion_Type = Integer32
_SysChassisVersion_Object = MibScalar
sysChassisVersion = _SysChassisVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 15),
    _SysChassisVersion_Type()
)
sysChassisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisVersion.setStatus("mandatory")


class _SysCrash_Type(Integer32):
    """Custom type sysCrash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysCrash_Type.__name__ = "Integer32"
_SysCrash_Object = MibScalar
sysCrash = _SysCrash_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 16),
    _SysCrash_Type()
)
sysCrash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCrash.setStatus("mandatory")


class _SysInitialize_Type(Integer32):
    """Custom type sysInitialize based on Integer32"""
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
        *(("cancel", 4),
          ("conditionalExecute", 2),
          ("ready", 1),
          ("unconditionalExecute", 3))
    )


_SysInitialize_Type.__name__ = "Integer32"
_SysInitialize_Object = MibScalar
sysInitialize = _SysInitialize_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 17),
    _SysInitialize_Type()
)
sysInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitialize.setStatus("mandatory")


class _SysInitializeDelay_Type(Integer32):
    """Custom type sysInitializeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SysInitializeDelay_Type.__name__ = "Integer32"
_SysInitializeDelay_Object = MibScalar
sysInitializeDelay = _SysInitializeDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 18),
    _SysInitializeDelay_Type()
)
sysInitializeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitializeDelay.setStatus("mandatory")


class _SysZeroAll_Type(Integer32):
    """Custom type sysZeroAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysZeroAll_Type.__name__ = "Integer32"
_SysZeroAll_Object = MibScalar
sysZeroAll = _SysZeroAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 19),
    _SysZeroAll_Type()
)
sysZeroAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysZeroAll.setStatus("mandatory")


class _SysZeroBase_Type(Integer32):
    """Custom type sysZeroBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysZeroBase_Type.__name__ = "Integer32"
_SysZeroBase_Object = MibScalar
sysZeroBase = _SysZeroBase_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 20),
    _SysZeroBase_Type()
)
sysZeroBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysZeroBase.setStatus("mandatory")
_SysZeroBaseTime_Type = TimeTicks
_SysZeroBaseTime_Object = MibScalar
sysZeroBaseTime = _SysZeroBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 21),
    _SysZeroBaseTime_Type()
)
sysZeroBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysZeroBaseTime.setStatus("mandatory")


class _SysLoaderName_Type(DisplayString):
    """Custom type sysLoaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysLoaderName_Type.__name__ = "DisplayString"
_SysLoaderName_Object = MibScalar
sysLoaderName = _SysLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 22),
    _SysLoaderName_Type()
)
sysLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderName.setStatus("mandatory")
_SysLoaderAddressType_Type = AddressType
_SysLoaderAddressType_Object = MibScalar
sysLoaderAddressType = _SysLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 23),
    _SysLoaderAddressType_Type()
)
sysLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderAddressType.setStatus("mandatory")
_SysLoaderAddress_Type = OctetString
_SysLoaderAddress_Object = MibScalar
sysLoaderAddress = _SysLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 24),
    _SysLoaderAddress_Type()
)
sysLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderAddress.setStatus("mandatory")
_SysDumperAddressType_Type = AddressType
_SysDumperAddressType_Object = MibScalar
sysDumperAddressType = _SysDumperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 25),
    _SysDumperAddressType_Type()
)
sysDumperAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDumperAddressType.setStatus("mandatory")
_SysDumperAddress_Type = OctetString
_SysDumperAddress_Object = MibScalar
sysDumperAddress = _SysDumperAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 26),
    _SysDumperAddress_Type()
)
sysDumperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDumperAddress.setStatus("mandatory")
_SysResourceLacks_Type = Counter32
_SysResourceLacks_Object = MibScalar
sysResourceLacks = _SysResourceLacks_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 27),
    _SysResourceLacks_Type()
)
sysResourceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceLacks.setStatus("mandatory")


class _SysChassisState_Type(Integer32):
    """Custom type sysChassisState based on Integer32"""
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
        *(("fault", 3),
          ("loop", 4),
          ("noFault", 2),
          ("notApplicable", 1))
    )


_SysChassisState_Type.__name__ = "Integer32"
_SysChassisState_Object = MibScalar
sysChassisState = _SysChassisState_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 28),
    _SysChassisState_Type()
)
sysChassisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisState.setStatus("mandatory")
_SysChassisFaultTransitions_Type = Counter32
_SysChassisFaultTransitions_Object = MibScalar
sysChassisFaultTransitions = _SysChassisFaultTransitions_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 29),
    _SysChassisFaultTransitions_Type()
)
sysChassisFaultTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisFaultTransitions.setStatus("mandatory")
_SysResourceNumber_Type = Integer32
_SysResourceNumber_Object = MibScalar
sysResourceNumber = _SysResourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 30),
    _SysResourceNumber_Type()
)
sysResourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceNumber.setStatus("mandatory")
_SysFeatureNumber_Type = Integer32
_SysFeatureNumber_Object = MibScalar
sysFeatureNumber = _SysFeatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 31),
    _SysFeatureNumber_Type()
)
sysFeatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureNumber.setStatus("mandatory")
_ResTable_Object = MibTable
resTable = _ResTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32)
)
if mibBuilder.loadTexts:
    resTable.setStatus("mandatory")
_ResEntry_Object = MibTableRow
resEntry = _ResEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1)
)
resEntry.setIndexNames(
    (0, "MRV-IN-REACH-SYSTEM-MIB", "resType"),
)
if mibBuilder.loadTexts:
    resEntry.setStatus("mandatory")


class _ResType_Type(Integer32):
    """Custom type resType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("appleFilterTable", 19),
          ("appleRouteCache", 18),
          ("bridgeFilterTable", 25),
          ("bridgeInactiveFilters", 29),
          ("bridgeLearnedFilters", 28),
          ("bridgeProtocolFilters", 30),
          ("bridgeSourceFilters", 27),
          ("bridgeStaticFilters", 26),
          ("circuits", 38),
          ("cpuPercent", 1),
          ("freeMemory", 8),
          ("globalMemoryPercent", 9),
          ("interfaces", 37),
          ("ipFilterCache", 11),
          ("ipFilterTable", 15),
          ("ipFragmentTable", 33),
          ("ipIgmpTable", 39),
          ("ipMulticastTable", 40),
          ("ipPolicyTable", 14),
          ("ipRouteCache", 12),
          ("ipRouteTable", 41),
          ("ipcMessage", 6),
          ("ipxRipFilterTable", 42),
          ("ipxRipTable", 22),
          ("ipxRouteCache", 13),
          ("ipxSapFilterTable", 43),
          ("ipxSapTable", 23),
          ("latAnnouncementCompressionTable", 31),
          ("memoryPercent", 2),
          ("packetBuffer", 5),
          ("packetCompressionTable", 32),
          ("packetHeaders", 36),
          ("phivDecnetFilterTable", 17),
          ("phivDecnetPolicyTable", 16),
          ("phivDecnetRouteCache", 10),
          ("process", 3),
          ("repeaterGlobalSecurityTable", 35),
          ("repeaterPortAccessTable", 20),
          ("repeaterPortNameTable", 21),
          ("repeaterPortSecurityTable", 24),
          ("repeaterRedundancyTable", 34),
          ("textPool", 7),
          ("timer", 4))
    )


_ResType_Type.__name__ = "Integer32"
_ResType_Object = MibTableColumn
resType = _ResType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 1),
    _ResType_Type()
)
resType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resType.setStatus("mandatory")
_ResCurrent_Type = Gauge32
_ResCurrent_Object = MibTableColumn
resCurrent = _ResCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 2),
    _ResCurrent_Type()
)
resCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resCurrent.setStatus("mandatory")
_ResWorst_Type = Gauge32
_ResWorst_Object = MibTableColumn
resWorst = _ResWorst_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 3),
    _ResWorst_Type()
)
resWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resWorst.setStatus("mandatory")
_ResAdminMaximum_Type = Integer32
_ResAdminMaximum_Object = MibTableColumn
resAdminMaximum = _ResAdminMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 4),
    _ResAdminMaximum_Type()
)
resAdminMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resAdminMaximum.setStatus("mandatory")
_ResLacks_Type = Counter32
_ResLacks_Object = MibTableColumn
resLacks = _ResLacks_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 5),
    _ResLacks_Type()
)
resLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resLacks.setStatus("mandatory")
_ResLackTime_Type = DateTime
_ResLackTime_Object = MibTableColumn
resLackTime = _ResLackTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 6),
    _ResLackTime_Type()
)
resLackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resLackTime.setStatus("mandatory")
_ResOperMaximum_Type = Integer32
_ResOperMaximum_Object = MibTableColumn
resOperMaximum = _ResOperMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 7),
    _ResOperMaximum_Type()
)
resOperMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resOperMaximum.setStatus("mandatory")
_FeatTable_Object = MibTable
featTable = _FeatTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33)
)
if mibBuilder.loadTexts:
    featTable.setStatus("mandatory")
_FeatEntry_Object = MibTableRow
featEntry = _FeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1)
)
featEntry.setIndexNames(
    (0, "MRV-IN-REACH-SYSTEM-MIB", "featType"),
)
if mibBuilder.loadTexts:
    featEntry.setStatus("mandatory")


class _FeatType_Type(Integer32):
    """Custom type featType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("allPorts", 15),
          ("apd", 30),
          ("arap", 25),
          ("changeEthernetAddress", 20),
          ("enviromentalManager", 36),
          ("eventLog", 8),
          ("expanded800", 21),
          ("fingerDaemon", 26),
          ("frameRelay", 18),
          ("help", 1),
          ("internetSecurity", 9),
          ("ipFiltering", 33),
          ("ipMulticastSpecial", 19),
          ("ipxFiltering", 32),
          ("ipxRouting", 31),
          ("kerberos", 12),
          ("kerberos5", 34),
          ("lat", 7),
          ("lpDaemon", 22),
          ("menu", 5),
          ("multisessions", 6),
          ("ppp", 23),
          ("radius", 35),
          ("rlogin", 14),
          ("routeDaemon", 27),
          ("rwhoDaemon", 28),
          ("scriptServer", 11),
          ("securID", 29),
          ("slip", 10),
          ("snmp", 2),
          ("ssh", 38),
          ("telnet", 13),
          ("terminalServer", 37),
          ("tl1", 39),
          ("tn3270", 4),
          ("unixCommands", 24),
          ("x25", 17),
          ("xprinter", 16),
          ("xremote", 3))
    )


_FeatType_Type.__name__ = "Integer32"
_FeatType_Object = MibTableColumn
featType = _FeatType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1, 1),
    _FeatType_Type()
)
featType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featType.setStatus("mandatory")


class _FeatStatus_Type(Integer32):
    """Custom type featStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("locked", 3))
    )


_FeatStatus_Type.__name__ = "Integer32"
_FeatStatus_Object = MibTableColumn
featStatus = _FeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1, 2),
    _FeatStatus_Type()
)
featStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featStatus.setStatus("mandatory")


class _FeatKey_Type(DisplayString):
    """Custom type featKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FeatKey_Type.__name__ = "DisplayString"
_FeatKey_Object = MibTableColumn
featKey = _FeatKey_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1, 3),
    _FeatKey_Type()
)
featKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featKey.setStatus("mandatory")
_XBootControl_ObjectIdentity = ObjectIdentity
xBootControl = _XBootControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 1, 34)
)


class _BootControlLoadInternetFile_Type(DisplayString):
    """Custom type bootControlLoadInternetFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootControlLoadInternetFile_Type.__name__ = "DisplayString"
_BootControlLoadInternetFile_Object = MibScalar
bootControlLoadInternetFile = _BootControlLoadInternetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 1),
    _BootControlLoadInternetFile_Type()
)
bootControlLoadInternetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetFile.setStatus("deprecated")
_BootControlLoadInternetServer_Type = IpAddress
_BootControlLoadInternetServer_Object = MibScalar
bootControlLoadInternetServer = _BootControlLoadInternetServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 2),
    _BootControlLoadInternetServer_Type()
)
bootControlLoadInternetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetServer.setStatus("deprecated")
_BootControlLoadInternetGateway_Type = IpAddress
_BootControlLoadInternetGateway_Object = MibScalar
bootControlLoadInternetGateway = _BootControlLoadInternetGateway_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 3),
    _BootControlLoadInternetGateway_Type()
)
bootControlLoadInternetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetGateway.setStatus("deprecated")


class _BootControlLoadBootpTftp_Type(Integer32):
    """Custom type bootControlLoadBootpTftp based on Integer32"""
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


_BootControlLoadBootpTftp_Type.__name__ = "Integer32"
_BootControlLoadBootpTftp_Object = MibScalar
bootControlLoadBootpTftp = _BootControlLoadBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 4),
    _BootControlLoadBootpTftp_Type()
)
bootControlLoadBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadBootpTftp.setStatus("deprecated")


class _BootControlLoadTftpDirect_Type(Integer32):
    """Custom type bootControlLoadTftpDirect based on Integer32"""
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


_BootControlLoadTftpDirect_Type.__name__ = "Integer32"
_BootControlLoadTftpDirect_Object = MibScalar
bootControlLoadTftpDirect = _BootControlLoadTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 5),
    _BootControlLoadTftpDirect_Type()
)
bootControlLoadTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadTftpDirect.setStatus("deprecated")


class _BootControlLoadLocal_Type(Integer32):
    """Custom type bootControlLoadLocal based on Integer32"""
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


_BootControlLoadLocal_Type.__name__ = "Integer32"
_BootControlLoadLocal_Object = MibScalar
bootControlLoadLocal = _BootControlLoadLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 6),
    _BootControlLoadLocal_Type()
)
bootControlLoadLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadLocal.setStatus("deprecated")


class _BootControlLoadMop_Type(Integer32):
    """Custom type bootControlLoadMop based on Integer32"""
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


_BootControlLoadMop_Type.__name__ = "Integer32"
_BootControlLoadMop_Object = MibScalar
bootControlLoadMop = _BootControlLoadMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 7),
    _BootControlLoadMop_Type()
)
bootControlLoadMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadMop.setStatus("deprecated")


class _BootControlLoadProprietary_Type(Integer32):
    """Custom type bootControlLoadProprietary based on Integer32"""
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


_BootControlLoadProprietary_Type.__name__ = "Integer32"
_BootControlLoadProprietary_Object = MibScalar
bootControlLoadProprietary = _BootControlLoadProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 8),
    _BootControlLoadProprietary_Type()
)
bootControlLoadProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadProprietary.setStatus("deprecated")


class _BootControlLoadRarpTftp_Type(Integer32):
    """Custom type bootControlLoadRarpTftp based on Integer32"""
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


_BootControlLoadRarpTftp_Type.__name__ = "Integer32"
_BootControlLoadRarpTftp_Object = MibScalar
bootControlLoadRarpTftp = _BootControlLoadRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 9),
    _BootControlLoadRarpTftp_Type()
)
bootControlLoadRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadRarpTftp.setStatus("deprecated")


class _BootControlDumpBootpTftp_Type(Integer32):
    """Custom type bootControlDumpBootpTftp based on Integer32"""
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


_BootControlDumpBootpTftp_Type.__name__ = "Integer32"
_BootControlDumpBootpTftp_Object = MibScalar
bootControlDumpBootpTftp = _BootControlDumpBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 10),
    _BootControlDumpBootpTftp_Type()
)
bootControlDumpBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpBootpTftp.setStatus("deprecated")


class _BootControlDumpLocal_Type(Integer32):
    """Custom type bootControlDumpLocal based on Integer32"""
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


_BootControlDumpLocal_Type.__name__ = "Integer32"
_BootControlDumpLocal_Object = MibScalar
bootControlDumpLocal = _BootControlDumpLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 11),
    _BootControlDumpLocal_Type()
)
bootControlDumpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpLocal.setStatus("deprecated")


class _BootControlDumpMop_Type(Integer32):
    """Custom type bootControlDumpMop based on Integer32"""
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


_BootControlDumpMop_Type.__name__ = "Integer32"
_BootControlDumpMop_Object = MibScalar
bootControlDumpMop = _BootControlDumpMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 12),
    _BootControlDumpMop_Type()
)
bootControlDumpMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpMop.setStatus("deprecated")


class _BootControlDumpProprietary_Type(Integer32):
    """Custom type bootControlDumpProprietary based on Integer32"""
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


_BootControlDumpProprietary_Type.__name__ = "Integer32"
_BootControlDumpProprietary_Object = MibScalar
bootControlDumpProprietary = _BootControlDumpProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 13),
    _BootControlDumpProprietary_Type()
)
bootControlDumpProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpProprietary.setStatus("deprecated")


class _BootControlDumpRarpTftp_Type(Integer32):
    """Custom type bootControlDumpRarpTftp based on Integer32"""
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


_BootControlDumpRarpTftp_Type.__name__ = "Integer32"
_BootControlDumpRarpTftp_Object = MibScalar
bootControlDumpRarpTftp = _BootControlDumpRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 14),
    _BootControlDumpRarpTftp_Type()
)
bootControlDumpRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpRarpTftp.setStatus("deprecated")


class _BootControlParamBootpTftp_Type(Integer32):
    """Custom type bootControlParamBootpTftp based on Integer32"""
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


_BootControlParamBootpTftp_Type.__name__ = "Integer32"
_BootControlParamBootpTftp_Object = MibScalar
bootControlParamBootpTftp = _BootControlParamBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 15),
    _BootControlParamBootpTftp_Type()
)
bootControlParamBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamBootpTftp.setStatus("deprecated")


class _BootControlParamLocal_Type(Integer32):
    """Custom type bootControlParamLocal based on Integer32"""
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


_BootControlParamLocal_Type.__name__ = "Integer32"
_BootControlParamLocal_Object = MibScalar
bootControlParamLocal = _BootControlParamLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 16),
    _BootControlParamLocal_Type()
)
bootControlParamLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamLocal.setStatus("deprecated")


class _BootControlParamMop_Type(Integer32):
    """Custom type bootControlParamMop based on Integer32"""
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


_BootControlParamMop_Type.__name__ = "Integer32"
_BootControlParamMop_Object = MibScalar
bootControlParamMop = _BootControlParamMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 17),
    _BootControlParamMop_Type()
)
bootControlParamMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamMop.setStatus("deprecated")


class _BootControlParamProprietary_Type(Integer32):
    """Custom type bootControlParamProprietary based on Integer32"""
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


_BootControlParamProprietary_Type.__name__ = "Integer32"
_BootControlParamProprietary_Object = MibScalar
bootControlParamProprietary = _BootControlParamProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 18),
    _BootControlParamProprietary_Type()
)
bootControlParamProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamProprietary.setStatus("deprecated")


class _BootControlParamRarpTftp_Type(Integer32):
    """Custom type bootControlParamRarpTftp based on Integer32"""
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


_BootControlParamRarpTftp_Type.__name__ = "Integer32"
_BootControlParamRarpTftp_Object = MibScalar
bootControlParamRarpTftp = _BootControlParamRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 19),
    _BootControlParamRarpTftp_Type()
)
bootControlParamRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamRarpTftp.setStatus("deprecated")
_SysInstalledMemory_Type = Gauge32
_SysInstalledMemory_Object = MibScalar
sysInstalledMemory = _SysInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 35),
    _SysInstalledMemory_Type()
)
sysInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInstalledMemory.setStatus("mandatory")


class _SysTemperatureLevel_Type(Integer32):
    """Custom type sysTemperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("normal", 2),
          ("unknown", 1))
    )


_SysTemperatureLevel_Type.__name__ = "Integer32"
_SysTemperatureLevel_Object = MibScalar
sysTemperatureLevel = _SysTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 36),
    _SysTemperatureLevel_Type()
)
sysTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTemperatureLevel.setStatus("mandatory")
_BootRecordTable_Object = MibTable
bootRecordTable = _BootRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37)
)
if mibBuilder.loadTexts:
    bootRecordTable.setStatus("mandatory")
_BootRecordEntry_Object = MibTableRow
bootRecordEntry = _BootRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1)
)
bootRecordEntry.setIndexNames(
    (0, "MRV-IN-REACH-SYSTEM-MIB", "bootRecordIndex"),
)
if mibBuilder.loadTexts:
    bootRecordEntry.setStatus("mandatory")
_BootRecordIndex_Type = Integer32
_BootRecordIndex_Object = MibTableColumn
bootRecordIndex = _BootRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 1),
    _BootRecordIndex_Type()
)
bootRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootRecordIndex.setStatus("mandatory")


class _BootRecordLoadInternetFile_Type(DisplayString):
    """Custom type bootRecordLoadInternetFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootRecordLoadInternetFile_Type.__name__ = "DisplayString"
_BootRecordLoadInternetFile_Object = MibTableColumn
bootRecordLoadInternetFile = _BootRecordLoadInternetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 2),
    _BootRecordLoadInternetFile_Type()
)
bootRecordLoadInternetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadInternetFile.setStatus("mandatory")
_BootRecordLoadInternetServer_Type = IpAddress
_BootRecordLoadInternetServer_Object = MibTableColumn
bootRecordLoadInternetServer = _BootRecordLoadInternetServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 3),
    _BootRecordLoadInternetServer_Type()
)
bootRecordLoadInternetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadInternetServer.setStatus("mandatory")
_BootRecordLoadInternetGateway_Type = IpAddress
_BootRecordLoadInternetGateway_Object = MibTableColumn
bootRecordLoadInternetGateway = _BootRecordLoadInternetGateway_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 4),
    _BootRecordLoadInternetGateway_Type()
)
bootRecordLoadInternetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadInternetGateway.setStatus("mandatory")


class _BootRecordLoadBootpTftp_Type(Integer32):
    """Custom type bootRecordLoadBootpTftp based on Integer32"""
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


_BootRecordLoadBootpTftp_Type.__name__ = "Integer32"
_BootRecordLoadBootpTftp_Object = MibTableColumn
bootRecordLoadBootpTftp = _BootRecordLoadBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 5),
    _BootRecordLoadBootpTftp_Type()
)
bootRecordLoadBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadBootpTftp.setStatus("mandatory")


class _BootRecordLoadTftpDirect_Type(Integer32):
    """Custom type bootRecordLoadTftpDirect based on Integer32"""
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


_BootRecordLoadTftpDirect_Type.__name__ = "Integer32"
_BootRecordLoadTftpDirect_Object = MibTableColumn
bootRecordLoadTftpDirect = _BootRecordLoadTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 6),
    _BootRecordLoadTftpDirect_Type()
)
bootRecordLoadTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadTftpDirect.setStatus("mandatory")


class _BootRecordLoadLocal_Type(Integer32):
    """Custom type bootRecordLoadLocal based on Integer32"""
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


_BootRecordLoadLocal_Type.__name__ = "Integer32"
_BootRecordLoadLocal_Object = MibTableColumn
bootRecordLoadLocal = _BootRecordLoadLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 7),
    _BootRecordLoadLocal_Type()
)
bootRecordLoadLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadLocal.setStatus("mandatory")


class _BootRecordLoadMop_Type(Integer32):
    """Custom type bootRecordLoadMop based on Integer32"""
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


_BootRecordLoadMop_Type.__name__ = "Integer32"
_BootRecordLoadMop_Object = MibTableColumn
bootRecordLoadMop = _BootRecordLoadMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 8),
    _BootRecordLoadMop_Type()
)
bootRecordLoadMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadMop.setStatus("mandatory")


class _BootRecordLoadProprietary_Type(Integer32):
    """Custom type bootRecordLoadProprietary based on Integer32"""
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


_BootRecordLoadProprietary_Type.__name__ = "Integer32"
_BootRecordLoadProprietary_Object = MibTableColumn
bootRecordLoadProprietary = _BootRecordLoadProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 9),
    _BootRecordLoadProprietary_Type()
)
bootRecordLoadProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadProprietary.setStatus("mandatory")


class _BootRecordLoadRarpTftp_Type(Integer32):
    """Custom type bootRecordLoadRarpTftp based on Integer32"""
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


_BootRecordLoadRarpTftp_Type.__name__ = "Integer32"
_BootRecordLoadRarpTftp_Object = MibTableColumn
bootRecordLoadRarpTftp = _BootRecordLoadRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 10),
    _BootRecordLoadRarpTftp_Type()
)
bootRecordLoadRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordLoadRarpTftp.setStatus("mandatory")


class _BootRecordDumpBootpTftp_Type(Integer32):
    """Custom type bootRecordDumpBootpTftp based on Integer32"""
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


_BootRecordDumpBootpTftp_Type.__name__ = "Integer32"
_BootRecordDumpBootpTftp_Object = MibTableColumn
bootRecordDumpBootpTftp = _BootRecordDumpBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 11),
    _BootRecordDumpBootpTftp_Type()
)
bootRecordDumpBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordDumpBootpTftp.setStatus("mandatory")


class _BootRecordDumpLocal_Type(Integer32):
    """Custom type bootRecordDumpLocal based on Integer32"""
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


_BootRecordDumpLocal_Type.__name__ = "Integer32"
_BootRecordDumpLocal_Object = MibTableColumn
bootRecordDumpLocal = _BootRecordDumpLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 12),
    _BootRecordDumpLocal_Type()
)
bootRecordDumpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordDumpLocal.setStatus("mandatory")


class _BootRecordDumpMop_Type(Integer32):
    """Custom type bootRecordDumpMop based on Integer32"""
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


_BootRecordDumpMop_Type.__name__ = "Integer32"
_BootRecordDumpMop_Object = MibTableColumn
bootRecordDumpMop = _BootRecordDumpMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 13),
    _BootRecordDumpMop_Type()
)
bootRecordDumpMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordDumpMop.setStatus("mandatory")


class _BootRecordDumpProprietary_Type(Integer32):
    """Custom type bootRecordDumpProprietary based on Integer32"""
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


_BootRecordDumpProprietary_Type.__name__ = "Integer32"
_BootRecordDumpProprietary_Object = MibTableColumn
bootRecordDumpProprietary = _BootRecordDumpProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 14),
    _BootRecordDumpProprietary_Type()
)
bootRecordDumpProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordDumpProprietary.setStatus("mandatory")


class _BootRecordDumpRarpTftp_Type(Integer32):
    """Custom type bootRecordDumpRarpTftp based on Integer32"""
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


_BootRecordDumpRarpTftp_Type.__name__ = "Integer32"
_BootRecordDumpRarpTftp_Object = MibTableColumn
bootRecordDumpRarpTftp = _BootRecordDumpRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 15),
    _BootRecordDumpRarpTftp_Type()
)
bootRecordDumpRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordDumpRarpTftp.setStatus("mandatory")


class _BootRecordParamBootpTftp_Type(Integer32):
    """Custom type bootRecordParamBootpTftp based on Integer32"""
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


_BootRecordParamBootpTftp_Type.__name__ = "Integer32"
_BootRecordParamBootpTftp_Object = MibTableColumn
bootRecordParamBootpTftp = _BootRecordParamBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 16),
    _BootRecordParamBootpTftp_Type()
)
bootRecordParamBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamBootpTftp.setStatus("mandatory")


class _BootRecordParamLocal_Type(Integer32):
    """Custom type bootRecordParamLocal based on Integer32"""
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


_BootRecordParamLocal_Type.__name__ = "Integer32"
_BootRecordParamLocal_Object = MibTableColumn
bootRecordParamLocal = _BootRecordParamLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 17),
    _BootRecordParamLocal_Type()
)
bootRecordParamLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamLocal.setStatus("mandatory")


class _BootRecordParamMop_Type(Integer32):
    """Custom type bootRecordParamMop based on Integer32"""
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


_BootRecordParamMop_Type.__name__ = "Integer32"
_BootRecordParamMop_Object = MibTableColumn
bootRecordParamMop = _BootRecordParamMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 18),
    _BootRecordParamMop_Type()
)
bootRecordParamMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamMop.setStatus("mandatory")


class _BootRecordParamProprietary_Type(Integer32):
    """Custom type bootRecordParamProprietary based on Integer32"""
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


_BootRecordParamProprietary_Type.__name__ = "Integer32"
_BootRecordParamProprietary_Object = MibTableColumn
bootRecordParamProprietary = _BootRecordParamProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 19),
    _BootRecordParamProprietary_Type()
)
bootRecordParamProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamProprietary.setStatus("mandatory")


class _BootRecordParamRarpTftp_Type(Integer32):
    """Custom type bootRecordParamRarpTftp based on Integer32"""
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


_BootRecordParamRarpTftp_Type.__name__ = "Integer32"
_BootRecordParamRarpTftp_Object = MibTableColumn
bootRecordParamRarpTftp = _BootRecordParamRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 20),
    _BootRecordParamRarpTftp_Type()
)
bootRecordParamRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamRarpTftp.setStatus("mandatory")


class _BootRecordStatus_Type(Integer32):
    """Custom type bootRecordStatus based on Integer32"""
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


_BootRecordStatus_Type.__name__ = "Integer32"
_BootRecordStatus_Object = MibTableColumn
bootRecordStatus = _BootRecordStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 21),
    _BootRecordStatus_Type()
)
bootRecordStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordStatus.setStatus("mandatory")


class _BootRecordMopFile_Type(DisplayString):
    """Custom type bootRecordMopFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BootRecordMopFile_Type.__name__ = "DisplayString"
_BootRecordMopFile_Object = MibTableColumn
bootRecordMopFile = _BootRecordMopFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 22),
    _BootRecordMopFile_Type()
)
bootRecordMopFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordMopFile.setStatus("mandatory")
_BootRecordInternetAddress_Type = IpAddress
_BootRecordInternetAddress_Object = MibTableColumn
bootRecordInternetAddress = _BootRecordInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 23),
    _BootRecordInternetAddress_Type()
)
bootRecordInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordInternetAddress.setStatus("mandatory")


class _BootRecordParamTftpDirect_Type(Integer32):
    """Custom type bootRecordParamTftpDirect based on Integer32"""
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


_BootRecordParamTftpDirect_Type.__name__ = "Integer32"
_BootRecordParamTftpDirect_Object = MibTableColumn
bootRecordParamTftpDirect = _BootRecordParamTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 24),
    _BootRecordParamTftpDirect_Type()
)
bootRecordParamTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordParamTftpDirect.setStatus("mandatory")


class _BootRecordInternetDelimiter_Type(DisplayString):
    """Custom type bootRecordInternetDelimiter based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_BootRecordInternetDelimiter_Type.__name__ = "DisplayString"
_BootRecordInternetDelimiter_Object = MibTableColumn
bootRecordInternetDelimiter = _BootRecordInternetDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 37, 1, 25),
    _BootRecordInternetDelimiter_Type()
)
bootRecordInternetDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootRecordInternetDelimiter.setStatus("mandatory")


class _SysLastAgentError_Type(Integer32):
    """Custom type sysLastAgentError based on Integer32"""
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
        *(("badClient", 10),
          ("badCommunity", 7),
          ("badType", 9),
          ("badValue", 4),
          ("badVersion", 8),
          ("genErr", 6),
          ("noError", 1),
          ("noSuchName", 3),
          ("readOnly", 5),
          ("tooBig", 2))
    )


_SysLastAgentError_Type.__name__ = "Integer32"
_SysLastAgentError_Object = MibScalar
sysLastAgentError = _SysLastAgentError_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 38),
    _SysLastAgentError_Type()
)
sysLastAgentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastAgentError.setStatus("mandatory")


class _SysRcpMulticast_Type(Integer32):
    """Custom type sysRcpMulticast based on Integer32"""
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


_SysRcpMulticast_Type.__name__ = "Integer32"
_SysRcpMulticast_Object = MibScalar
sysRcpMulticast = _SysRcpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 40),
    _SysRcpMulticast_Type()
)
sysRcpMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRcpMulticast.setStatus("mandatory")
_SysTimeServerAddress_Type = TypedAddress
_SysTimeServerAddress_Object = MibScalar
sysTimeServerAddress = _SysTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 41),
    _SysTimeServerAddress_Type()
)
sysTimeServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeServerAddress.setStatus("mandatory")
_SysTimeServerConfiguredAddress_Type = TypedAddress
_SysTimeServerConfiguredAddress_Object = MibScalar
sysTimeServerConfiguredAddress = _SysTimeServerConfiguredAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 46),
    _SysTimeServerConfiguredAddress_Type()
)
sysTimeServerConfiguredAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerConfiguredAddress.setStatus("mandatory")


class _SysTimeServerConfiguredStatus_Type(Integer32):
    """Custom type sysTimeServerConfiguredStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("required", 3))
    )


_SysTimeServerConfiguredStatus_Type.__name__ = "Integer32"
_SysTimeServerConfiguredStatus_Object = MibScalar
sysTimeServerConfiguredStatus = _SysTimeServerConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 47),
    _SysTimeServerConfiguredStatus_Type()
)
sysTimeServerConfiguredStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeServerConfiguredStatus.setStatus("mandatory")


class _SysBootRecordOverrideDefinedAddress_Type(Integer32):
    """Custom type sysBootRecordOverrideDefinedAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysBootRecordOverrideDefinedAddress_Type.__name__ = "Integer32"
_SysBootRecordOverrideDefinedAddress_Object = MibScalar
sysBootRecordOverrideDefinedAddress = _SysBootRecordOverrideDefinedAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 48),
    _SysBootRecordOverrideDefinedAddress_Type()
)
sysBootRecordOverrideDefinedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootRecordOverrideDefinedAddress.setStatus("mandatory")


class _SysBootRecordMessageEnable_Type(Integer32):
    """Custom type sysBootRecordMessageEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysBootRecordMessageEnable_Type.__name__ = "Integer32"
_SysBootRecordMessageEnable_Object = MibScalar
sysBootRecordMessageEnable = _SysBootRecordMessageEnable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 49),
    _SysBootRecordMessageEnable_Type()
)
sysBootRecordMessageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootRecordMessageEnable.setStatus("mandatory")


class _SysBootRecordParamDefaults_Type(Integer32):
    """Custom type sysBootRecordParamDefaults based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysBootRecordParamDefaults_Type.__name__ = "Integer32"
_SysBootRecordParamDefaults_Object = MibScalar
sysBootRecordParamDefaults = _SysBootRecordParamDefaults_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 50),
    _SysBootRecordParamDefaults_Type()
)
sysBootRecordParamDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootRecordParamDefaults.setStatus("mandatory")


class _SysLoginAuthFailureTrapType_Type(Integer32):
    """Custom type sysLoginAuthFailureTrapType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("chap", 4),
          ("kerberos", 5),
          ("limitedPrivilegedPassword", 9),
          ("loginPassword", 2),
          ("none", 1),
          ("pap", 3),
          ("privilegedPassword", 8),
          ("radius", 7),
          ("securId", 6))
    )


_SysLoginAuthFailureTrapType_Type.__name__ = "Integer32"
_SysLoginAuthFailureTrapType_Object = MibScalar
sysLoginAuthFailureTrapType = _SysLoginAuthFailureTrapType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 78),
    _SysLoginAuthFailureTrapType_Type()
)
sysLoginAuthFailureTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoginAuthFailureTrapType.setStatus("mandatory")


class _SysLoginAuthTrapIdentity_Type(DisplayString):
    """Custom type sysLoginAuthTrapIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysLoginAuthTrapIdentity_Type.__name__ = "DisplayString"
_SysLoginAuthTrapIdentity_Object = MibScalar
sysLoginAuthTrapIdentity = _SysLoginAuthTrapIdentity_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 81),
    _SysLoginAuthTrapIdentity_Type()
)
sysLoginAuthTrapIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoginAuthTrapIdentity.setStatus("mandatory")


class _SysLocalScriptServer_Type(Integer32):
    """Custom type sysLocalScriptServer based on Integer32"""
    defaultValue = 2

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


_SysLocalScriptServer_Type.__name__ = "Integer32"
_SysLocalScriptServer_Object = MibScalar
sysLocalScriptServer = _SysLocalScriptServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 82),
    _SysLocalScriptServer_Type()
)
sysLocalScriptServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalScriptServer.setStatus("mandatory")


class _SysInReachManagementSecurityStatus_Type(Integer32):
    """Custom type sysInReachManagementSecurityStatus based on Integer32"""
    defaultValue = 1

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


_SysInReachManagementSecurityStatus_Type.__name__ = "Integer32"
_SysInReachManagementSecurityStatus_Object = MibScalar
sysInReachManagementSecurityStatus = _SysInReachManagementSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 83),
    _SysInReachManagementSecurityStatus_Type()
)
sysInReachManagementSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInReachManagementSecurityStatus.setStatus("mandatory")
_SysProductName_Type = DisplayString
_SysProductName_Object = MibScalar
sysProductName = _SysProductName_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 84),
    _SysProductName_Type()
)
sysProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductName.setStatus("mandatory")


class _SysModemPresent_Type(Integer32):
    """Custom type sysModemPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem", 2),
          ("noModem", 1))
    )


_SysModemPresent_Type.__name__ = "Integer32"
_SysModemPresent_Object = MibScalar
sysModemPresent = _SysModemPresent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 85),
    _SysModemPresent_Type()
)
sysModemPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModemPresent.setStatus("mandatory")


class _SysCauseAction_Type(Integer32):
    """Custom type sysCauseAction based on Integer32"""
    defaultValue = 1

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


_SysCauseAction_Type.__name__ = "Integer32"
_SysCauseAction_Object = MibScalar
sysCauseAction = _SysCauseAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 86),
    _SysCauseAction_Type()
)
sysCauseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCauseAction.setStatus("mandatory")


class _SysWebServerConfigAdminStatus_Type(Integer32):
    """Custom type sysWebServerConfigAdminStatus based on Integer32"""
    defaultValue = 2

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


_SysWebServerConfigAdminStatus_Type.__name__ = "Integer32"
_SysWebServerConfigAdminStatus_Object = MibScalar
sysWebServerConfigAdminStatus = _SysWebServerConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 87),
    _SysWebServerConfigAdminStatus_Type()
)
sysWebServerConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysWebServerConfigAdminStatus.setStatus("mandatory")


class _SysTl1SourceIdentifier_Type(DisplayString):
    """Custom type sysTl1SourceIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysTl1SourceIdentifier_Type.__name__ = "DisplayString"
_SysTl1SourceIdentifier_Object = MibScalar
sysTl1SourceIdentifier = _SysTl1SourceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 88),
    _SysTl1SourceIdentifier_Type()
)
sysTl1SourceIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTl1SourceIdentifier.setStatus("mandatory")


class _SysInitializeDelayParameter_Type(Integer32):
    """Custom type sysInitializeDelayParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysInitializeDelayParameter_Type.__name__ = "Integer32"
_SysInitializeDelayParameter_Object = MibScalar
sysInitializeDelayParameter = _SysInitializeDelayParameter_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 89),
    _SysInitializeDelayParameter_Type()
)
sysInitializeDelayParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitializeDelayParameter.setStatus("mandatory")


class _SysTimeProtocol_Type(Integer32):
    """Custom type sysTimeProtocol based on Integer32"""
    defaultValue = 1

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


_SysTimeProtocol_Type.__name__ = "Integer32"
_SysTimeProtocol_Object = MibScalar
sysTimeProtocol = _SysTimeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 90),
    _SysTimeProtocol_Type()
)
sysTimeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeProtocol.setStatus("mandatory")


class _SysTimeBroadcast_Type(Integer32):
    """Custom type sysTimeBroadcast based on Integer32"""
    defaultValue = 2

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


_SysTimeBroadcast_Type.__name__ = "Integer32"
_SysTimeBroadcast_Object = MibScalar
sysTimeBroadcast = _SysTimeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 91),
    _SysTimeBroadcast_Type()
)
sysTimeBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeBroadcast.setStatus("mandatory")

# Managed Objects groups


# Notification objects

resourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 9)
)
resourceFailure.setObjects(
      *(("MRV-IN-REACH-SYSTEM-MIB", "resType"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    resourceFailure.setStatus(
        ""
    )

sysLoginAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 28)
)
sysLoginAuthenticationFailure.setObjects(
      *(("MRV-IN-REACH-SYSTEM-MIB", "sysLoginAuthFailureTrapType"),
        ("MRV-IN-REACH-SYSTEM-MIB", "sysLoginAuthTrapIdentity"))
)
if mibBuilder.loadTexts:
    sysLoginAuthenticationFailure.setStatus(
        ""
    )

resourceLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 1, 0, 1)
)
resourceLack.setObjects(
    ("MRV-IN-REACH-SYSTEM-MIB", "resType")
)
if mibBuilder.loadTexts:
    resourceLack.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-SYSTEM-MIB",
    **{"resourceFailure": resourceFailure,
       "sysLoginAuthenticationFailure": sysLoginAuthenticationFailure,
       "xSystem": xSystem,
       "resourceLack": resourceLack,
       "sysIdent": sysIdent,
       "sysDefineMode": sysDefineMode,
       "sysDateTime": sysDateTime,
       "sysTimeZone": sysTimeZone,
       "sysLoadSoftware": sysLoadSoftware,
       "sysDump": sysDump,
       "sysMaintenancePassword": sysMaintenancePassword,
       "sysLocalName": sysLocalName,
       "sysSoftwareVersionType": sysSoftwareVersionType,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysRomVersion": sysRomVersion,
       "sysHardwareType": sysHardwareType,
       "sysHardwareVersion": sysHardwareVersion,
       "sysChassisType": sysChassisType,
       "sysChassisVersion": sysChassisVersion,
       "sysCrash": sysCrash,
       "sysInitialize": sysInitialize,
       "sysInitializeDelay": sysInitializeDelay,
       "sysZeroAll": sysZeroAll,
       "sysZeroBase": sysZeroBase,
       "sysZeroBaseTime": sysZeroBaseTime,
       "sysLoaderName": sysLoaderName,
       "sysLoaderAddressType": sysLoaderAddressType,
       "sysLoaderAddress": sysLoaderAddress,
       "sysDumperAddressType": sysDumperAddressType,
       "sysDumperAddress": sysDumperAddress,
       "sysResourceLacks": sysResourceLacks,
       "sysChassisState": sysChassisState,
       "sysChassisFaultTransitions": sysChassisFaultTransitions,
       "sysResourceNumber": sysResourceNumber,
       "sysFeatureNumber": sysFeatureNumber,
       "resTable": resTable,
       "resEntry": resEntry,
       "resType": resType,
       "resCurrent": resCurrent,
       "resWorst": resWorst,
       "resAdminMaximum": resAdminMaximum,
       "resLacks": resLacks,
       "resLackTime": resLackTime,
       "resOperMaximum": resOperMaximum,
       "featTable": featTable,
       "featEntry": featEntry,
       "featType": featType,
       "featStatus": featStatus,
       "featKey": featKey,
       "xBootControl": xBootControl,
       "bootControlLoadInternetFile": bootControlLoadInternetFile,
       "bootControlLoadInternetServer": bootControlLoadInternetServer,
       "bootControlLoadInternetGateway": bootControlLoadInternetGateway,
       "bootControlLoadBootpTftp": bootControlLoadBootpTftp,
       "bootControlLoadTftpDirect": bootControlLoadTftpDirect,
       "bootControlLoadLocal": bootControlLoadLocal,
       "bootControlLoadMop": bootControlLoadMop,
       "bootControlLoadProprietary": bootControlLoadProprietary,
       "bootControlLoadRarpTftp": bootControlLoadRarpTftp,
       "bootControlDumpBootpTftp": bootControlDumpBootpTftp,
       "bootControlDumpLocal": bootControlDumpLocal,
       "bootControlDumpMop": bootControlDumpMop,
       "bootControlDumpProprietary": bootControlDumpProprietary,
       "bootControlDumpRarpTftp": bootControlDumpRarpTftp,
       "bootControlParamBootpTftp": bootControlParamBootpTftp,
       "bootControlParamLocal": bootControlParamLocal,
       "bootControlParamMop": bootControlParamMop,
       "bootControlParamProprietary": bootControlParamProprietary,
       "bootControlParamRarpTftp": bootControlParamRarpTftp,
       "sysInstalledMemory": sysInstalledMemory,
       "sysTemperatureLevel": sysTemperatureLevel,
       "bootRecordTable": bootRecordTable,
       "bootRecordEntry": bootRecordEntry,
       "bootRecordIndex": bootRecordIndex,
       "bootRecordLoadInternetFile": bootRecordLoadInternetFile,
       "bootRecordLoadInternetServer": bootRecordLoadInternetServer,
       "bootRecordLoadInternetGateway": bootRecordLoadInternetGateway,
       "bootRecordLoadBootpTftp": bootRecordLoadBootpTftp,
       "bootRecordLoadTftpDirect": bootRecordLoadTftpDirect,
       "bootRecordLoadLocal": bootRecordLoadLocal,
       "bootRecordLoadMop": bootRecordLoadMop,
       "bootRecordLoadProprietary": bootRecordLoadProprietary,
       "bootRecordLoadRarpTftp": bootRecordLoadRarpTftp,
       "bootRecordDumpBootpTftp": bootRecordDumpBootpTftp,
       "bootRecordDumpLocal": bootRecordDumpLocal,
       "bootRecordDumpMop": bootRecordDumpMop,
       "bootRecordDumpProprietary": bootRecordDumpProprietary,
       "bootRecordDumpRarpTftp": bootRecordDumpRarpTftp,
       "bootRecordParamBootpTftp": bootRecordParamBootpTftp,
       "bootRecordParamLocal": bootRecordParamLocal,
       "bootRecordParamMop": bootRecordParamMop,
       "bootRecordParamProprietary": bootRecordParamProprietary,
       "bootRecordParamRarpTftp": bootRecordParamRarpTftp,
       "bootRecordStatus": bootRecordStatus,
       "bootRecordMopFile": bootRecordMopFile,
       "bootRecordInternetAddress": bootRecordInternetAddress,
       "bootRecordParamTftpDirect": bootRecordParamTftpDirect,
       "bootRecordInternetDelimiter": bootRecordInternetDelimiter,
       "sysLastAgentError": sysLastAgentError,
       "sysRcpMulticast": sysRcpMulticast,
       "sysTimeServerAddress": sysTimeServerAddress,
       "sysTimeServerConfiguredAddress": sysTimeServerConfiguredAddress,
       "sysTimeServerConfiguredStatus": sysTimeServerConfiguredStatus,
       "sysBootRecordOverrideDefinedAddress": sysBootRecordOverrideDefinedAddress,
       "sysBootRecordMessageEnable": sysBootRecordMessageEnable,
       "sysBootRecordParamDefaults": sysBootRecordParamDefaults,
       "sysLoginAuthFailureTrapType": sysLoginAuthFailureTrapType,
       "sysLoginAuthTrapIdentity": sysLoginAuthTrapIdentity,
       "sysLocalScriptServer": sysLocalScriptServer,
       "sysInReachManagementSecurityStatus": sysInReachManagementSecurityStatus,
       "sysProductName": sysProductName,
       "sysModemPresent": sysModemPresent,
       "sysCauseAction": sysCauseAction,
       "sysWebServerConfigAdminStatus": sysWebServerConfigAdminStatus,
       "sysTl1SourceIdentifier": sysTl1SourceIdentifier,
       "sysInitializeDelayParameter": sysInitializeDelayParameter,
       "sysTimeProtocol": sysTimeProtocol,
       "sysTimeBroadcast": sysTimeBroadcast}
)
