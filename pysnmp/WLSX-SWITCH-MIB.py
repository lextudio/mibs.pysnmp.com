# SNMP MIB module (WLSX-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:13 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1)
)
wlsxSwitchMIB.setRevisions(
        ("1908-04-16 02:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxSystemXGroup_ObjectIdentity = ObjectIdentity
wlsxSystemXGroup = _WlsxSystemXGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1)
)


class _WlsxHostname_Type(DisplayString):
    """Custom type wlsxHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlsxHostname_Type.__name__ = "DisplayString"
_WlsxHostname_Object = MibScalar
wlsxHostname = _WlsxHostname_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 1),
    _WlsxHostname_Type()
)
wlsxHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHostname.setStatus("current")


class _WlsxModelName_Type(DisplayString):
    """Custom type wlsxModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlsxModelName_Type.__name__ = "DisplayString"
_WlsxModelName_Object = MibScalar
wlsxModelName = _WlsxModelName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 2),
    _WlsxModelName_Type()
)
wlsxModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxModelName.setStatus("current")
_WlsxSwitchIp_Type = IpAddress
_WlsxSwitchIp_Object = MibScalar
wlsxSwitchIp = _WlsxSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 3),
    _WlsxSwitchIp_Type()
)
wlsxSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchIp.setStatus("current")


class _WlsxSwitchRole_Type(Integer32):
    """Custom type wlsxSwitchRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("master", 1),
          ("standbymaster", 3))
    )


_WlsxSwitchRole_Type.__name__ = "Integer32"
_WlsxSwitchRole_Object = MibScalar
wlsxSwitchRole = _WlsxSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 4),
    _WlsxSwitchRole_Type()
)
wlsxSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchRole.setStatus("current")
_WlsxSwitchMasterIp_Type = IpAddress
_WlsxSwitchMasterIp_Object = MibScalar
wlsxSwitchMasterIp = _WlsxSwitchMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 5),
    _WlsxSwitchMasterIp_Type()
)
wlsxSwitchMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchMasterIp.setStatus("current")
_WlsxSwitchListTable_Object = MibTable
wlsxSwitchListTable = _WlsxSwitchListTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wlsxSwitchListTable.setStatus("current")
_WlsxSwitchListEntry_Object = MibTableRow
wlsxSwitchListEntry = _WlsxSwitchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 6, 1)
)
wlsxSwitchListEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "switchListSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wlsxSwitchListEntry.setStatus("current")
_SwitchListSwitchIPAddress_Type = IpAddress
_SwitchListSwitchIPAddress_Object = MibTableColumn
switchListSwitchIPAddress = _SwitchListSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 6, 1, 1),
    _SwitchListSwitchIPAddress_Type()
)
switchListSwitchIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchListSwitchIPAddress.setStatus("current")


class _SwitchListSwitchRole_Type(Integer32):
    """Custom type switchListSwitchRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("master", 1),
          ("standbymaster", 3))
    )


_SwitchListSwitchRole_Type.__name__ = "Integer32"
_SwitchListSwitchRole_Object = MibTableColumn
switchListSwitchRole = _SwitchListSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 6, 1, 2),
    _SwitchListSwitchRole_Type()
)
switchListSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchListSwitchRole.setStatus("current")
_WlsxSwitchLicenseCount_Type = Integer32
_WlsxSwitchLicenseCount_Object = MibScalar
wlsxSwitchLicenseCount = _WlsxSwitchLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 7),
    _WlsxSwitchLicenseCount_Type()
)
wlsxSwitchLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchLicenseCount.setStatus("current")
_WlsxSwitchLicenseTable_Object = MibTable
wlsxSwitchLicenseTable = _WlsxSwitchLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wlsxSwitchLicenseTable.setStatus("current")
_WlsxLicenseEntry_Object = MibTableRow
wlsxLicenseEntry = _WlsxLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1)
)
wlsxLicenseEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    wlsxLicenseEntry.setStatus("current")
_LicenseIndex_Type = Integer32
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")
_LicenseKey_Type = DisplayString
_LicenseKey_Object = MibTableColumn
licenseKey = _LicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 2),
    _LicenseKey_Type()
)
licenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKey.setStatus("current")
_LicenseInstalled_Type = DisplayString
_LicenseInstalled_Object = MibTableColumn
licenseInstalled = _LicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 3),
    _LicenseInstalled_Type()
)
licenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseInstalled.setStatus("current")
_LicenseExpires_Type = DisplayString
_LicenseExpires_Object = MibTableColumn
licenseExpires = _LicenseExpires_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 4),
    _LicenseExpires_Type()
)
licenseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpires.setStatus("current")
_LicenseFlags_Type = DisplayString
_LicenseFlags_Object = MibTableColumn
licenseFlags = _LicenseFlags_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 5),
    _LicenseFlags_Type()
)
licenseFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFlags.setStatus("current")
_LicenseService_Type = DisplayString
_LicenseService_Object = MibTableColumn
licenseService = _LicenseService_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 8, 1, 6),
    _LicenseService_Type()
)
licenseService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseService.setStatus("current")
_WlsxSysXProcessorTable_Object = MibTable
wlsxSysXProcessorTable = _WlsxSysXProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wlsxSysXProcessorTable.setStatus("current")
_WlsxSysXProcessorEntry_Object = MibTableRow
wlsxSysXProcessorEntry = _WlsxSysXProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 9, 1)
)
wlsxSysXProcessorEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "sysXProcessorID"),
)
if mibBuilder.loadTexts:
    wlsxSysXProcessorEntry.setStatus("current")
_SysXProcessorID_Type = Integer32
_SysXProcessorID_Object = MibTableColumn
sysXProcessorID = _SysXProcessorID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 9, 1, 1),
    _SysXProcessorID_Type()
)
sysXProcessorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysXProcessorID.setStatus("current")


class _SysXProcessorDescr_Type(DisplayString):
    """Custom type sysXProcessorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysXProcessorDescr_Type.__name__ = "DisplayString"
_SysXProcessorDescr_Object = MibTableColumn
sysXProcessorDescr = _SysXProcessorDescr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 9, 1, 2),
    _SysXProcessorDescr_Type()
)
sysXProcessorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXProcessorDescr.setStatus("current")


class _SysXProcessorLoad_Type(Integer32):
    """Custom type sysXProcessorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysXProcessorLoad_Type.__name__ = "Integer32"
_SysXProcessorLoad_Object = MibTableColumn
sysXProcessorLoad = _SysXProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 9, 1, 3),
    _SysXProcessorLoad_Type()
)
sysXProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXProcessorLoad.setStatus("current")
_WlsxSysXStorageTable_Object = MibTable
wlsxSysXStorageTable = _WlsxSysXStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wlsxSysXStorageTable.setStatus("current")
_WlsxSysXStorageEntry_Object = MibTableRow
wlsxSysXStorageEntry = _WlsxSysXStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1)
)
wlsxSysXStorageEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "sysXStorageIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysXStorageEntry.setStatus("current")
_SysXStorageIndex_Type = Integer32
_SysXStorageIndex_Object = MibTableColumn
sysXStorageIndex = _SysXStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1, 1),
    _SysXStorageIndex_Type()
)
sysXStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysXStorageIndex.setStatus("current")


class _SysXStorageType_Type(Integer32):
    """Custom type sysXStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flashMemory", 2),
          ("ram", 1))
    )


_SysXStorageType_Type.__name__ = "Integer32"
_SysXStorageType_Object = MibTableColumn
sysXStorageType = _SysXStorageType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1, 2),
    _SysXStorageType_Type()
)
sysXStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXStorageType.setStatus("current")
_SysXStorageSize_Type = Integer32
_SysXStorageSize_Object = MibTableColumn
sysXStorageSize = _SysXStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1, 3),
    _SysXStorageSize_Type()
)
sysXStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXStorageSize.setStatus("current")
_SysXStorageUsed_Type = Integer32
_SysXStorageUsed_Object = MibTableColumn
sysXStorageUsed = _SysXStorageUsed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1, 4),
    _SysXStorageUsed_Type()
)
sysXStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXStorageUsed.setStatus("current")


class _SysXStorageName_Type(DisplayString):
    """Custom type sysXStorageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysXStorageName_Type.__name__ = "DisplayString"
_SysXStorageName_Object = MibTableColumn
sysXStorageName = _SysXStorageName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 10, 1, 5),
    _SysXStorageName_Type()
)
sysXStorageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXStorageName.setStatus("current")
_WlsxSysXMemoryTable_Object = MibTable
wlsxSysXMemoryTable = _WlsxSysXMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wlsxSysXMemoryTable.setStatus("current")
_WlsxSysXMemoryEntry_Object = MibTableRow
wlsxSysXMemoryEntry = _WlsxSysXMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11, 1)
)
wlsxSysXMemoryEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "sysXMemoryIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysXMemoryEntry.setStatus("current")
_SysXMemoryIndex_Type = Integer32
_SysXMemoryIndex_Object = MibTableColumn
sysXMemoryIndex = _SysXMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11, 1, 1),
    _SysXMemoryIndex_Type()
)
sysXMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysXMemoryIndex.setStatus("current")
_SysXMemorySize_Type = Integer32
_SysXMemorySize_Object = MibTableColumn
sysXMemorySize = _SysXMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11, 1, 2),
    _SysXMemorySize_Type()
)
sysXMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXMemorySize.setStatus("current")
_SysXMemoryUsed_Type = Integer32
_SysXMemoryUsed_Object = MibTableColumn
sysXMemoryUsed = _SysXMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11, 1, 3),
    _SysXMemoryUsed_Type()
)
sysXMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXMemoryUsed.setStatus("current")
_SysXMemoryFree_Type = Integer32
_SysXMemoryFree_Object = MibTableColumn
sysXMemoryFree = _SysXMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 11, 1, 4),
    _SysXMemoryFree_Type()
)
sysXMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysXMemoryFree.setStatus("current")
_WlsxSwitchLicenseSerialNumber_Type = DisplayString
_WlsxSwitchLicenseSerialNumber_Object = MibScalar
wlsxSwitchLicenseSerialNumber = _WlsxSwitchLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 1, 12),
    _WlsxSwitchLicenseSerialNumber_Type()
)
wlsxSwitchLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchLicenseSerialNumber.setStatus("current")
_WlsxUserInfoGroup_ObjectIdentity = ObjectIdentity
wlsxUserInfoGroup = _WlsxUserInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2)
)
_WlsxSwitchUserTable_Object = MibTable
wlsxSwitchUserTable = _WlsxSwitchUserTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxSwitchUserTable.setStatus("current")
_WlsxSwitchUserEntry_Object = MibTableRow
wlsxSwitchUserEntry = _WlsxSwitchUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1)
)
wlsxSwitchUserEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "userIpAddress"),
)
if mibBuilder.loadTexts:
    wlsxSwitchUserEntry.setStatus("current")
_UserIpAddress_Type = IpAddress
_UserIpAddress_Object = MibTableColumn
userIpAddress = _UserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 1),
    _UserIpAddress_Type()
)
userIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIpAddress.setStatus("current")
_UserPhyAddress_Type = MacAddress
_UserPhyAddress_Object = MibTableColumn
userPhyAddress = _UserPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 2),
    _UserPhyAddress_Type()
)
userPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPhyAddress.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 3),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserRole_Type(DisplayString):
    """Custom type userRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UserRole_Type.__name__ = "DisplayString"
_UserRole_Object = MibTableColumn
userRole = _UserRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 4),
    _UserRole_Type()
)
userRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userRole.setStatus("current")
_UserUpTime_Type = TimeTicks
_UserUpTime_Object = MibTableColumn
userUpTime = _UserUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 5),
    _UserUpTime_Type()
)
userUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUpTime.setStatus("current")


class _UserAuthenticationMethod_Type(Integer32):
    """Custom type userAuthenticationMethod based on Integer32"""
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
        *(("dot1x", 4),
          ("mac", 6),
          ("none", 1),
          ("other", 2),
          ("vpn", 5),
          ("web", 3))
    )


_UserAuthenticationMethod_Type.__name__ = "Integer32"
_UserAuthenticationMethod_Object = MibTableColumn
userAuthenticationMethod = _UserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 6),
    _UserAuthenticationMethod_Type()
)
userAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationMethod.setStatus("current")


class _UserLocation_Type(DisplayString):
    """Custom type userLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserLocation_Type.__name__ = "DisplayString"
_UserLocation_Object = MibTableColumn
userLocation = _UserLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 7),
    _UserLocation_Type()
)
userLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLocation.setStatus("current")


class _UserServerName_Type(DisplayString):
    """Custom type userServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserServerName_Type.__name__ = "DisplayString"
_UserServerName_Object = MibTableColumn
userServerName = _UserServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 8),
    _UserServerName_Type()
)
userServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userServerName.setStatus("current")
_UserConnectedVlan_Type = Integer32
_UserConnectedVlan_Object = MibTableColumn
userConnectedVlan = _UserConnectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 9),
    _UserConnectedVlan_Type()
)
userConnectedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConnectedVlan.setStatus("current")
_UserConnectedSlot_Type = Integer32
_UserConnectedSlot_Object = MibTableColumn
userConnectedSlot = _UserConnectedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 10),
    _UserConnectedSlot_Type()
)
userConnectedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConnectedSlot.setStatus("current")
_UserConnectedPort_Type = Integer32
_UserConnectedPort_Object = MibTableColumn
userConnectedPort = _UserConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 11),
    _UserConnectedPort_Type()
)
userConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConnectedPort.setStatus("current")


class _UserBWContractName_Type(DisplayString):
    """Custom type userBWContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserBWContractName_Type.__name__ = "DisplayString"
_UserBWContractName_Object = MibTableColumn
userBWContractName = _UserBWContractName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 12),
    _UserBWContractName_Type()
)
userBWContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userBWContractName.setStatus("current")


class _UserBWContractUsage_Type(Integer32):
    """Custom type userBWContractUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 2),
          ("user", 1))
    )


_UserBWContractUsage_Type.__name__ = "Integer32"
_UserBWContractUsage_Object = MibTableColumn
userBWContractUsage = _UserBWContractUsage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 13),
    _UserBWContractUsage_Type()
)
userBWContractUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userBWContractUsage.setStatus("current")
_UserConnectedModule_Type = Integer32
_UserConnectedModule_Object = MibTableColumn
userConnectedModule = _UserConnectedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 1, 1, 14),
    _UserConnectedModule_Type()
)
userConnectedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConnectedModule.setStatus("current")
_WlsxSwitchStationMgmtTable_Object = MibTable
wlsxSwitchStationMgmtTable = _WlsxSwitchStationMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wlsxSwitchStationMgmtTable.setStatus("current")
_WlsxSwitchStationMgmtEntry_Object = MibTableRow
wlsxSwitchStationMgmtEntry = _WlsxSwitchStationMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1)
)
wlsxSwitchStationMgmtEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "staPhyAddress"),
    (0, "WLSX-SWITCH-MIB", "staAccessPointBSSID"),
)
if mibBuilder.loadTexts:
    wlsxSwitchStationMgmtEntry.setStatus("current")
_StaPhyAddress_Type = MacAddress
_StaPhyAddress_Object = MibTableColumn
staPhyAddress = _StaPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 1),
    _StaPhyAddress_Type()
)
staPhyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPhyAddress.setStatus("current")
_StaAccessPointBSSID_Type = MacAddress
_StaAccessPointBSSID_Object = MibTableColumn
staAccessPointBSSID = _StaAccessPointBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 2),
    _StaAccessPointBSSID_Type()
)
staAccessPointBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staAccessPointBSSID.setStatus("current")


class _StaUserName_Type(DisplayString):
    """Custom type staUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaUserName_Type.__name__ = "DisplayString"
_StaUserName_Object = MibTableColumn
staUserName = _StaUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 3),
    _StaUserName_Type()
)
staUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staUserName.setStatus("current")


class _StaUserRole_Type(DisplayString):
    """Custom type staUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaUserRole_Type.__name__ = "DisplayString"
_StaUserRole_Object = MibTableColumn
staUserRole = _StaUserRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 4),
    _StaUserRole_Type()
)
staUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staUserRole.setStatus("current")
_StaAssociationID_Type = Unsigned32
_StaAssociationID_Object = MibTableColumn
staAssociationID = _StaAssociationID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 5),
    _StaAssociationID_Type()
)
staAssociationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staAssociationID.setStatus("current")


class _StaAccessPointESSID_Type(DisplayString):
    """Custom type staAccessPointESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StaAccessPointESSID_Type.__name__ = "DisplayString"
_StaAccessPointESSID_Object = MibTableColumn
staAccessPointESSID = _StaAccessPointESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 6),
    _StaAccessPointESSID_Type()
)
staAccessPointESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staAccessPointESSID.setStatus("current")
_StaSignalToNoiseRatio_Type = Integer32
_StaSignalToNoiseRatio_Object = MibTableColumn
staSignalToNoiseRatio = _StaSignalToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 7),
    _StaSignalToNoiseRatio_Type()
)
staSignalToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSignalToNoiseRatio.setStatus("current")


class _StaTransmitRate_Type(Integer32):
    """Custom type staTransmitRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 6),
          ("rate12Mbps", 7),
          ("rate18Mbps", 8),
          ("rate1Mbps", 1),
          ("rate24Mbps", 9),
          ("rate2Mbps", 2),
          ("rate36Mbps", 10),
          ("rate48Mbps", 11),
          ("rate54Mbps", 12),
          ("rate5point5Mbps", 3),
          ("rate6Mbps", 4),
          ("rate9Mbps", 5))
    )


_StaTransmitRate_Type.__name__ = "Integer32"
_StaTransmitRate_Object = MibTableColumn
staTransmitRate = _StaTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 8),
    _StaTransmitRate_Type()
)
staTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTransmitRate.setStatus("current")


class _StaReceiveRate_Type(Integer32):
    """Custom type staReceiveRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 6),
          ("rate12Mbps", 7),
          ("rate18Mbps", 8),
          ("rate1Mbps", 1),
          ("rate24Mbps", 9),
          ("rate2Mbps", 2),
          ("rate36Mbps", 10),
          ("rate48Mbps", 11),
          ("rate54Mbps", 12),
          ("rate5point5Mbps", 3),
          ("rate6Mbps", 4),
          ("rate9Mbps", 5))
    )


_StaReceiveRate_Type.__name__ = "Integer32"
_StaReceiveRate_Object = MibTableColumn
staReceiveRate = _StaReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 2, 1, 9),
    _StaReceiveRate_Type()
)
staReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staReceiveRate.setStatus("current")
_WlsxSwitchStationStatsTable_Object = MibTable
wlsxSwitchStationStatsTable = _WlsxSwitchStationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wlsxSwitchStationStatsTable.setStatus("current")
_WlsxSwitchStationStatsEntry_Object = MibTableRow
wlsxSwitchStationStatsEntry = _WlsxSwitchStationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1)
)
wlsxSwitchStationStatsEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "staPhyAddress"),
    (0, "WLSX-SWITCH-MIB", "staAccessPointBSSID"),
)
if mibBuilder.loadTexts:
    wlsxSwitchStationStatsEntry.setStatus("current")
_StaTxPackets_Type = Counter32
_StaTxPackets_Object = MibTableColumn
staTxPackets = _StaTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 1),
    _StaTxPackets_Type()
)
staTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxPackets.setStatus("current")
_StaTxBytes_Type = Counter32
_StaTxBytes_Object = MibTableColumn
staTxBytes = _StaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 2),
    _StaTxBytes_Type()
)
staTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxBytes.setStatus("current")
_StaRxPackets_Type = Counter32
_StaRxPackets_Object = MibTableColumn
staRxPackets = _StaRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 3),
    _StaRxPackets_Type()
)
staRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRxPackets.setStatus("current")
_StaRxBytes_Type = Counter32
_StaRxBytes_Object = MibTableColumn
staRxBytes = _StaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 4),
    _StaRxBytes_Type()
)
staRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRxBytes.setStatus("current")
_StaBwRate_Type = Integer32
_StaBwRate_Object = MibTableColumn
staBwRate = _StaBwRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 5),
    _StaBwRate_Type()
)
staBwRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBwRate.setStatus("current")
_StaFrameRetryRate_Type = Integer32
_StaFrameRetryRate_Object = MibTableColumn
staFrameRetryRate = _StaFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 6),
    _StaFrameRetryRate_Type()
)
staFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staFrameRetryRate.setStatus("current")
_StaFrameLowSpeedRate_Type = Integer32
_StaFrameLowSpeedRate_Object = MibTableColumn
staFrameLowSpeedRate = _StaFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 7),
    _StaFrameLowSpeedRate_Type()
)
staFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staFrameLowSpeedRate.setStatus("current")
_StaFrameNonUnicastRate_Type = Integer32
_StaFrameNonUnicastRate_Object = MibTableColumn
staFrameNonUnicastRate = _StaFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 8),
    _StaFrameNonUnicastRate_Type()
)
staFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staFrameNonUnicastRate.setStatus("current")
_StaFrameFragmentationRate_Type = Integer32
_StaFrameFragmentationRate_Object = MibTableColumn
staFrameFragmentationRate = _StaFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 9),
    _StaFrameFragmentationRate_Type()
)
staFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staFrameFragmentationRate.setStatus("current")
_StaFrameReceiveErrorRate_Type = Integer32
_StaFrameReceiveErrorRate_Object = MibTableColumn
staFrameReceiveErrorRate = _StaFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 2, 3, 1, 10),
    _StaFrameReceiveErrorRate_Type()
)
staFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staFrameReceiveErrorRate.setStatus("current")
_WlsxAccessPointInfoGroup_ObjectIdentity = ObjectIdentity
wlsxAccessPointInfoGroup = _WlsxAccessPointInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3)
)
_WlsxSwitchTotalNumAccessPoints_Type = Unsigned32
_WlsxSwitchTotalNumAccessPoints_Object = MibScalar
wlsxSwitchTotalNumAccessPoints = _WlsxSwitchTotalNumAccessPoints_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 1),
    _WlsxSwitchTotalNumAccessPoints_Type()
)
wlsxSwitchTotalNumAccessPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchTotalNumAccessPoints.setStatus("current")
_WlsxSwitchTotalNumStationsAssociated_Type = Unsigned32
_WlsxSwitchTotalNumStationsAssociated_Object = MibScalar
wlsxSwitchTotalNumStationsAssociated = _WlsxSwitchTotalNumStationsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 2),
    _WlsxSwitchTotalNumStationsAssociated_Type()
)
wlsxSwitchTotalNumStationsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSwitchTotalNumStationsAssociated.setStatus("current")
_WlsxSwitchAccessPointTable_Object = MibTable
wlsxSwitchAccessPointTable = _WlsxSwitchAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wlsxSwitchAccessPointTable.setStatus("current")
_WlsxSwitchAccessPointEntry_Object = MibTableRow
wlsxSwitchAccessPointEntry = _WlsxSwitchAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1)
)
wlsxSwitchAccessPointEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "apBSSID"),
)
if mibBuilder.loadTexts:
    wlsxSwitchAccessPointEntry.setStatus("current")
_ApBSSID_Type = MacAddress
_ApBSSID_Object = MibTableColumn
apBSSID = _ApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 1),
    _ApBSSID_Type()
)
apBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apBSSID.setStatus("current")


class _ApESSID_Type(DisplayString):
    """Custom type apESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApESSID_Type.__name__ = "DisplayString"
_ApESSID_Object = MibTableColumn
apESSID = _ApESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 2),
    _ApESSID_Type()
)
apESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apESSID.setStatus("current")
_ApSlot_Type = Unsigned32
_ApSlot_Object = MibTableColumn
apSlot = _ApSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 3),
    _ApSlot_Type()
)
apSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSlot.setStatus("current")
_ApPort_Type = Unsigned32
_ApPort_Object = MibTableColumn
apPort = _ApPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 4),
    _ApPort_Type()
)
apPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPort.setStatus("current")
_ApIpAddress_Type = IpAddress
_ApIpAddress_Object = MibTableColumn
apIpAddress = _ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 5),
    _ApIpAddress_Type()
)
apIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAddress.setStatus("current")


class _ApPhyType_Type(Integer32):
    """Custom type apPhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_ApPhyType_Type.__name__ = "Integer32"
_ApPhyType_Object = MibTableColumn
apPhyType = _ApPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 6),
    _ApPhyType_Type()
)
apPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPhyType.setStatus("current")


class _ApType_Type(Integer32):
    """Custom type apType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("am", 2),
          ("ap", 1))
    )


_ApType_Type.__name__ = "Integer32"
_ApType_Object = MibTableColumn
apType = _ApType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 7),
    _ApType_Type()
)
apType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apType.setStatus("current")


class _ApCurrentChannel_Type(Integer32):
    """Custom type apCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_ApCurrentChannel_Type.__name__ = "Integer32"
_ApCurrentChannel_Object = MibTableColumn
apCurrentChannel = _ApCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 8),
    _ApCurrentChannel_Type()
)
apCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentChannel.setStatus("current")


class _ApLocation_Type(DisplayString):
    """Custom type apLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApLocation_Type.__name__ = "DisplayString"
_ApLocation_Object = MibTableColumn
apLocation = _ApLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 9),
    _ApLocation_Type()
)
apLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLocation.setStatus("current")
_ApTotalTime_Type = TimeTicks
_ApTotalTime_Object = MibTableColumn
apTotalTime = _ApTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 10),
    _ApTotalTime_Type()
)
apTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalTime.setStatus("current")
_ApInactiveTime_Type = TimeTicks
_ApInactiveTime_Object = MibTableColumn
apInactiveTime = _ApInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 11),
    _ApInactiveTime_Type()
)
apInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInactiveTime.setStatus("current")
_ApLoadBalancing_Type = TruthValue
_ApLoadBalancing_Object = MibTableColumn
apLoadBalancing = _ApLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 12),
    _ApLoadBalancing_Type()
)
apLoadBalancing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLoadBalancing.setStatus("current")
_ApChannelNoise_Type = Integer32
_ApChannelNoise_Object = MibTableColumn
apChannelNoise = _ApChannelNoise_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 13),
    _ApChannelNoise_Type()
)
apChannelNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelNoise.setStatus("current")
_ApSignalToNoiseRatio_Type = Integer32
_ApSignalToNoiseRatio_Object = MibTableColumn
apSignalToNoiseRatio = _ApSignalToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 14),
    _ApSignalToNoiseRatio_Type()
)
apSignalToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSignalToNoiseRatio.setStatus("current")


class _ApTransmitRate_Type(Integer32):
    """Custom type apTransmitRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 6),
          ("rate12Mbps", 7),
          ("rate18Mbps", 8),
          ("rate1Mbps", 1),
          ("rate24Mbps", 9),
          ("rate2Mbps", 2),
          ("rate36Mbps", 10),
          ("rate48Mbps", 11),
          ("rate54Mbps", 12),
          ("rate5point5Mbps", 3),
          ("rate6Mbps", 4),
          ("rate9Mbps", 5))
    )


_ApTransmitRate_Type.__name__ = "Integer32"
_ApTransmitRate_Object = MibTableColumn
apTransmitRate = _ApTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 15),
    _ApTransmitRate_Type()
)
apTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTransmitRate.setStatus("current")


class _ApReceiveRate_Type(Integer32):
    """Custom type apReceiveRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 6),
          ("rate12Mbps", 7),
          ("rate18Mbps", 8),
          ("rate1Mbps", 1),
          ("rate24Mbps", 9),
          ("rate2Mbps", 2),
          ("rate36Mbps", 10),
          ("rate48Mbps", 11),
          ("rate54Mbps", 12),
          ("rate5point5Mbps", 3),
          ("rate6Mbps", 4),
          ("rate9Mbps", 5))
    )


_ApReceiveRate_Type.__name__ = "Integer32"
_ApReceiveRate_Object = MibTableColumn
apReceiveRate = _ApReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 3, 1, 16),
    _ApReceiveRate_Type()
)
apReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReceiveRate.setStatus("current")
_WlsxSwitchGlobalAPTable_Object = MibTable
wlsxSwitchGlobalAPTable = _WlsxSwitchGlobalAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    wlsxSwitchGlobalAPTable.setStatus("deprecated")
_WlsxSwitchGlobalAPEntry_Object = MibTableRow
wlsxSwitchGlobalAPEntry = _WlsxSwitchGlobalAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1)
)
wlsxSwitchGlobalAPEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "globalAPLocation"),
    (0, "WLSX-SWITCH-MIB", "globalAPAddress"),
)
if mibBuilder.loadTexts:
    wlsxSwitchGlobalAPEntry.setStatus("deprecated")


class _GlobalAPLocation_Type(DisplayString):
    """Custom type globalAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GlobalAPLocation_Type.__name__ = "DisplayString"
_GlobalAPLocation_Object = MibTableColumn
globalAPLocation = _GlobalAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 1),
    _GlobalAPLocation_Type()
)
globalAPLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalAPLocation.setStatus("deprecated")
_GlobalAPAddress_Type = IpAddress
_GlobalAPAddress_Object = MibTableColumn
globalAPAddress = _GlobalAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 2),
    _GlobalAPAddress_Type()
)
globalAPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalAPAddress.setStatus("deprecated")
_GlobalAPLocalSwitch_Type = IpAddress
_GlobalAPLocalSwitch_Object = MibTableColumn
globalAPLocalSwitch = _GlobalAPLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 3),
    _GlobalAPLocalSwitch_Type()
)
globalAPLocalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAPLocalSwitch.setStatus("deprecated")
_GlobalAPdot11aPhyAddr_Type = MacAddress
_GlobalAPdot11aPhyAddr_Object = MibTableColumn
globalAPdot11aPhyAddr = _GlobalAPdot11aPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 4),
    _GlobalAPdot11aPhyAddr_Type()
)
globalAPdot11aPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAPdot11aPhyAddr.setStatus("deprecated")
_GlobalAPdot11bPhyAddr_Type = MacAddress
_GlobalAPdot11bPhyAddr_Object = MibTableColumn
globalAPdot11bPhyAddr = _GlobalAPdot11bPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 5),
    _GlobalAPdot11bPhyAddr_Type()
)
globalAPdot11bPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAPdot11bPhyAddr.setStatus("deprecated")


class _GlobalAPState_Type(Integer32):
    """Custom type globalAPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GlobalAPState_Type.__name__ = "Integer32"
_GlobalAPState_Object = MibTableColumn
globalAPState = _GlobalAPState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 6),
    _GlobalAPState_Type()
)
globalAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAPState.setStatus("deprecated")
_GlobalAPdot11gPhyAddr_Type = MacAddress
_GlobalAPdot11gPhyAddr_Object = MibTableColumn
globalAPdot11gPhyAddr = _GlobalAPdot11gPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 4, 1, 7),
    _GlobalAPdot11gPhyAddr_Type()
)
globalAPdot11gPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAPdot11gPhyAddr.setStatus("deprecated")
_WlsxSwitchAccessPointStatsTable_Object = MibTable
wlsxSwitchAccessPointStatsTable = _WlsxSwitchAccessPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    wlsxSwitchAccessPointStatsTable.setStatus("current")
_WlsxSwitchAccessPointStatsEntry_Object = MibTableRow
wlsxSwitchAccessPointStatsEntry = _WlsxSwitchAccessPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1)
)
wlsxSwitchAccessPointStatsEntry.setIndexNames(
    (0, "WLSX-SWITCH-MIB", "apBSSID"),
)
if mibBuilder.loadTexts:
    wlsxSwitchAccessPointStatsEntry.setStatus("current")


class _ApStatsChannel_Type(Integer32):
    """Custom type apStatsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_ApStatsChannel_Type.__name__ = "Integer32"
_ApStatsChannel_Object = MibTableColumn
apStatsChannel = _ApStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 1),
    _ApStatsChannel_Type()
)
apStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStatsChannel.setStatus("current")
_ApChannelBwRate_Type = Integer32
_ApChannelBwRate_Object = MibTableColumn
apChannelBwRate = _ApChannelBwRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 2),
    _ApChannelBwRate_Type()
)
apChannelBwRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelBwRate.setStatus("current")
_ApChannelFrameRetryRate_Type = Integer32
_ApChannelFrameRetryRate_Object = MibTableColumn
apChannelFrameRetryRate = _ApChannelFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 3),
    _ApChannelFrameRetryRate_Type()
)
apChannelFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelFrameRetryRate.setStatus("current")
_ApChannelFrameLowSpeedRate_Type = Integer32
_ApChannelFrameLowSpeedRate_Object = MibTableColumn
apChannelFrameLowSpeedRate = _ApChannelFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 4),
    _ApChannelFrameLowSpeedRate_Type()
)
apChannelFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelFrameLowSpeedRate.setStatus("current")
_ApChannelFrameNonUnicastRate_Type = Integer32
_ApChannelFrameNonUnicastRate_Object = MibTableColumn
apChannelFrameNonUnicastRate = _ApChannelFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 5),
    _ApChannelFrameNonUnicastRate_Type()
)
apChannelFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelFrameNonUnicastRate.setStatus("current")
_ApChannelFrameFragmentationRate_Type = Integer32
_ApChannelFrameFragmentationRate_Object = MibTableColumn
apChannelFrameFragmentationRate = _ApChannelFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 6),
    _ApChannelFrameFragmentationRate_Type()
)
apChannelFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelFrameFragmentationRate.setStatus("current")
_ApChannelFrameReceiveErrorRate_Type = Integer32
_ApChannelFrameReceiveErrorRate_Object = MibTableColumn
apChannelFrameReceiveErrorRate = _ApChannelFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 7),
    _ApChannelFrameReceiveErrorRate_Type()
)
apChannelFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelFrameReceiveErrorRate.setStatus("current")
_ApBSSTxPackets_Type = Counter32
_ApBSSTxPackets_Object = MibTableColumn
apBSSTxPackets = _ApBSSTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 8),
    _ApBSSTxPackets_Type()
)
apBSSTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSTxPackets.setStatus("current")
_ApBSSTxBytes_Type = Counter32
_ApBSSTxBytes_Object = MibTableColumn
apBSSTxBytes = _ApBSSTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 9),
    _ApBSSTxBytes_Type()
)
apBSSTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSTxBytes.setStatus("current")
_ApBSSRxPackets_Type = Counter32
_ApBSSRxPackets_Object = MibTableColumn
apBSSRxPackets = _ApBSSRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 10),
    _ApBSSRxPackets_Type()
)
apBSSRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSRxPackets.setStatus("current")
_ApBSSRxBytes_Type = Counter32
_ApBSSRxBytes_Object = MibTableColumn
apBSSRxBytes = _ApBSSRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 11),
    _ApBSSRxBytes_Type()
)
apBSSRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSRxBytes.setStatus("current")
_ApBSSBwRate_Type = Integer32
_ApBSSBwRate_Object = MibTableColumn
apBSSBwRate = _ApBSSBwRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 12),
    _ApBSSBwRate_Type()
)
apBSSBwRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSBwRate.setStatus("current")
_ApBSSFrameRetryRate_Type = Integer32
_ApBSSFrameRetryRate_Object = MibTableColumn
apBSSFrameRetryRate = _ApBSSFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 13),
    _ApBSSFrameRetryRate_Type()
)
apBSSFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSFrameRetryRate.setStatus("current")
_ApBSSFrameLowSpeedRate_Type = Integer32
_ApBSSFrameLowSpeedRate_Object = MibTableColumn
apBSSFrameLowSpeedRate = _ApBSSFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 14),
    _ApBSSFrameLowSpeedRate_Type()
)
apBSSFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSFrameLowSpeedRate.setStatus("current")
_ApBSSFrameNonUnicastRate_Type = Integer32
_ApBSSFrameNonUnicastRate_Object = MibTableColumn
apBSSFrameNonUnicastRate = _ApBSSFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 15),
    _ApBSSFrameNonUnicastRate_Type()
)
apBSSFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSFrameNonUnicastRate.setStatus("current")
_ApBSSFrameFragmentationRate_Type = Integer32
_ApBSSFrameFragmentationRate_Object = MibTableColumn
apBSSFrameFragmentationRate = _ApBSSFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 16),
    _ApBSSFrameFragmentationRate_Type()
)
apBSSFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSFrameFragmentationRate.setStatus("current")
_ApBSSFrameReceiveErrorRate_Type = Integer32
_ApBSSFrameReceiveErrorRate_Object = MibTableColumn
apBSSFrameReceiveErrorRate = _ApBSSFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 3, 5, 1, 17),
    _ApBSSFrameReceiveErrorRate_Type()
)
apBSSFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSFrameReceiveErrorRate.setStatus("current")
_WlsxSwitchTraps_ObjectIdentity = ObjectIdentity
wlsxSwitchTraps = _WlsxSwitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100)
)
_WlsxSwitchTrapObjectsGroup_ObjectIdentity = ObjectIdentity
wlsxSwitchTrapObjectsGroup = _WlsxSwitchTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100)
)


class _WlsxAuthServerName_Type(DisplayString):
    """Custom type wlsxAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxAuthServerName_Type.__name__ = "DisplayString"
_WlsxAuthServerName_Object = MibScalar
wlsxAuthServerName = _WlsxAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 1),
    _WlsxAuthServerName_Type()
)
wlsxAuthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxAuthServerName.setStatus("current")
_WlsxAuthServerTimeout_Type = Integer32
_WlsxAuthServerTimeout_Object = MibScalar
wlsxAuthServerTimeout = _WlsxAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 2),
    _WlsxAuthServerTimeout_Type()
)
wlsxAuthServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxAuthServerTimeout.setStatus("current")
_WlsxFanNumber_Type = Integer32
_WlsxFanNumber_Object = MibScalar
wlsxFanNumber = _WlsxFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 4),
    _WlsxFanNumber_Type()
)
wlsxFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxFanNumber.setStatus("current")
_WlsxLineCardNumber_Type = Integer32
_WlsxLineCardNumber_Object = MibScalar
wlsxLineCardNumber = _WlsxLineCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 5),
    _WlsxLineCardNumber_Type()
)
wlsxLineCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxLineCardNumber.setStatus("current")


class _WlsxVoltageType_Type(DisplayString):
    """Custom type wlsxVoltageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlsxVoltageType_Type.__name__ = "DisplayString"
_WlsxVoltageType_Object = MibScalar
wlsxVoltageType = _WlsxVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 6),
    _WlsxVoltageType_Type()
)
wlsxVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoltageType.setStatus("current")


class _WlsxVoltageValue_Type(DisplayString):
    """Custom type wlsxVoltageValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_WlsxVoltageValue_Type.__name__ = "DisplayString"
_WlsxVoltageValue_Object = MibScalar
wlsxVoltageValue = _WlsxVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 7),
    _WlsxVoltageValue_Type()
)
wlsxVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoltageValue.setStatus("current")


class _WlsxTemperatureValue_Type(DisplayString):
    """Custom type wlsxTemperatureValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTemperatureValue_Type.__name__ = "DisplayString"
_WlsxTemperatureValue_Object = MibScalar
wlsxTemperatureValue = _WlsxTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 8),
    _WlsxTemperatureValue_Type()
)
wlsxTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTemperatureValue.setStatus("current")


class _WlsxProcessName_Type(DisplayString):
    """Custom type wlsxProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxProcessName_Type.__name__ = "DisplayString"
_WlsxProcessName_Object = MibScalar
wlsxProcessName = _WlsxProcessName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 9),
    _WlsxProcessName_Type()
)
wlsxProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxProcessName.setStatus("current")
_WlsxStationMacAddress_Type = MacAddress
_WlsxStationMacAddress_Object = MibScalar
wlsxStationMacAddress = _WlsxStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 10),
    _WlsxStationMacAddress_Type()
)
wlsxStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStationMacAddress.setStatus("current")


class _WlsxStationBlackListReason_Type(Integer32):
    """Custom type wlsxStationBlackListReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 3),
          ("ipSpoofing", 8),
          ("mitmAttack", 2),
          ("other", 100),
          ("pingFlood", 4),
          ("sessionBlacklist", 7),
          ("sessionFlood", 5),
          ("synFlood", 6),
          ("userDefined", 1))
    )


_WlsxStationBlackListReason_Type.__name__ = "Integer32"
_WlsxStationBlackListReason_Object = MibScalar
wlsxStationBlackListReason = _WlsxStationBlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 11),
    _WlsxStationBlackListReason_Type()
)
wlsxStationBlackListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStationBlackListReason.setStatus("current")
_WlsxSpoofedIpAddress_Type = IpAddress
_WlsxSpoofedIpAddress_Object = MibScalar
wlsxSpoofedIpAddress = _WlsxSpoofedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 12),
    _WlsxSpoofedIpAddress_Type()
)
wlsxSpoofedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSpoofedIpAddress.setStatus("current")
_WlsxSpoofedOldPhyAddress_Type = MacAddress
_WlsxSpoofedOldPhyAddress_Object = MibScalar
wlsxSpoofedOldPhyAddress = _WlsxSpoofedOldPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 13),
    _WlsxSpoofedOldPhyAddress_Type()
)
wlsxSpoofedOldPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSpoofedOldPhyAddress.setStatus("current")
_WlsxSpoofedNewPhyAddress_Type = MacAddress
_WlsxSpoofedNewPhyAddress_Object = MibScalar
wlsxSpoofedNewPhyAddress = _WlsxSpoofedNewPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 14),
    _WlsxSpoofedNewPhyAddress_Type()
)
wlsxSpoofedNewPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSpoofedNewPhyAddress.setStatus("current")


class _WlsxDBName_Type(DisplayString):
    """Custom type wlsxDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxDBName_Type.__name__ = "DisplayString"
_WlsxDBName_Object = MibScalar
wlsxDBName = _WlsxDBName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 15),
    _WlsxDBName_Type()
)
wlsxDBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxDBName.setStatus("current")


class _WlsxDBUserName_Type(DisplayString):
    """Custom type wlsxDBUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxDBUserName_Type.__name__ = "DisplayString"
_WlsxDBUserName_Object = MibScalar
wlsxDBUserName = _WlsxDBUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 16),
    _WlsxDBUserName_Type()
)
wlsxDBUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxDBUserName.setStatus("current")
_WlsxDBIpAddress_Type = IpAddress
_WlsxDBIpAddress_Object = MibScalar
wlsxDBIpAddress = _WlsxDBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 17),
    _WlsxDBIpAddress_Type()
)
wlsxDBIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxDBIpAddress.setStatus("current")


class _WlsxDBType_Type(Integer32):
    """Custom type wlsxDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mssql", 1),
          ("mysql", 2))
    )


_WlsxDBType_Type.__name__ = "Integer32"
_WlsxDBType_Object = MibScalar
wlsxDBType = _WlsxDBType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 18),
    _WlsxDBType_Type()
)
wlsxDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxDBType.setStatus("current")
_WlsxVrID_Type = Integer32
_WlsxVrID_Object = MibScalar
wlsxVrID = _WlsxVrID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 19),
    _WlsxVrID_Type()
)
wlsxVrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVrID.setStatus("current")
_WlsxVrMasterIp_Type = IpAddress
_WlsxVrMasterIp_Object = MibScalar
wlsxVrMasterIp = _WlsxVrMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 20),
    _WlsxVrMasterIp_Type()
)
wlsxVrMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVrMasterIp.setStatus("current")


class _WlsxVrrpOperState_Type(Integer32):
    """Custom type wlsxVrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_WlsxVrrpOperState_Type.__name__ = "Integer32"
_WlsxVrrpOperState_Object = MibScalar
wlsxVrrpOperState = _WlsxVrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 21),
    _WlsxVrrpOperState_Type()
)
wlsxVrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVrrpOperState.setStatus("current")
_WlsxApTxPower_Type = Integer32
_WlsxApTxPower_Object = MibScalar
wlsxApTxPower = _WlsxApTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 22),
    _WlsxApTxPower_Type()
)
wlsxApTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxApTxPower.setStatus("current")


class _WlsxESIServerGrpName_Type(DisplayString):
    """Custom type wlsxESIServerGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxESIServerGrpName_Type.__name__ = "DisplayString"
_WlsxESIServerGrpName_Object = MibScalar
wlsxESIServerGrpName = _WlsxESIServerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 23),
    _WlsxESIServerGrpName_Type()
)
wlsxESIServerGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxESIServerGrpName.setStatus("current")


class _WlsxESIServerName_Type(DisplayString):
    """Custom type wlsxESIServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxESIServerName_Type.__name__ = "DisplayString"
_WlsxESIServerName_Object = MibScalar
wlsxESIServerName = _WlsxESIServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 24),
    _WlsxESIServerName_Type()
)
wlsxESIServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxESIServerName.setStatus("current")
_WlsxESIServerIpaddress_Type = IpAddress
_WlsxESIServerIpaddress_Object = MibScalar
wlsxESIServerIpaddress = _WlsxESIServerIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 25),
    _WlsxESIServerIpaddress_Type()
)
wlsxESIServerIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxESIServerIpaddress.setStatus("current")
_WlsxLicenseDaysRemaining_Type = Integer32
_WlsxLicenseDaysRemaining_Object = MibScalar
wlsxLicenseDaysRemaining = _WlsxLicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 26),
    _WlsxLicenseDaysRemaining_Type()
)
wlsxLicenseDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxLicenseDaysRemaining.setStatus("current")
_WlsxSlotNumber_Type = Integer32
_WlsxSlotNumber_Object = MibScalar
wlsxSlotNumber = _WlsxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 100, 27),
    _WlsxSlotNumber_Type()
)
wlsxSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSlotNumber.setStatus("current")

# Managed Objects groups


# Notification objects

wlsxSwitchIPChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1001)
)
wlsxSwitchIPChanged.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxSwitchIp")
)
if mibBuilder.loadTexts:
    wlsxSwitchIPChanged.setStatus(
        "current"
    )

wlsxSwitchRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1002)
)
wlsxSwitchRoleChange.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxSwitchRole")
)
if mibBuilder.loadTexts:
    wlsxSwitchRoleChange.setStatus(
        "current"
    )

wlsxUserEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1003)
)
wlsxUserEntryCreated.setObjects(
    ("WLSX-SWITCH-MIB", "userPhyAddress")
)
if mibBuilder.loadTexts:
    wlsxUserEntryCreated.setStatus(
        "current"
    )

wlsxUserEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1004)
)
wlsxUserEntryDeleted.setObjects(
    ("WLSX-SWITCH-MIB", "userPhyAddress")
)
if mibBuilder.loadTexts:
    wlsxUserEntryDeleted.setStatus(
        "current"
    )

wlsxUserEntryAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1005)
)
wlsxUserEntryAuthenticated.setObjects(
      *(("WLSX-SWITCH-MIB", "userPhyAddress"),
        ("WLSX-SWITCH-MIB", "userName"),
        ("WLSX-SWITCH-MIB", "userAuthenticationMethod"),
        ("WLSX-SWITCH-MIB", "userRole"))
)
if mibBuilder.loadTexts:
    wlsxUserEntryAuthenticated.setStatus(
        "current"
    )

wlsxUserEntryDeAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1006)
)
wlsxUserEntryDeAuthenticated.setObjects(
    ("WLSX-SWITCH-MIB", "userPhyAddress")
)
if mibBuilder.loadTexts:
    wlsxUserEntryDeAuthenticated.setStatus(
        "current"
    )

wlsxUserAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1007)
)
wlsxUserAuthenticationFailed.setObjects(
    ("WLSX-SWITCH-MIB", "userPhyAddress")
)
if mibBuilder.loadTexts:
    wlsxUserAuthenticationFailed.setStatus(
        "current"
    )

wlsxAuthServerReqTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1008)
)
wlsxAuthServerReqTimedOut.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxAuthServerName")
)
if mibBuilder.loadTexts:
    wlsxAuthServerReqTimedOut.setStatus(
        "current"
    )

wlsxAuthServerTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1009)
)
wlsxAuthServerTimedOut.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxAuthServerName"),
        ("WLSX-SWITCH-MIB", "wlsxAuthServerTimeout"))
)
if mibBuilder.loadTexts:
    wlsxAuthServerTimedOut.setStatus(
        "current"
    )

wlsxAuthServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1010)
)
wlsxAuthServerIsUp.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxAuthServerName")
)
if mibBuilder.loadTexts:
    wlsxAuthServerIsUp.setStatus(
        "current"
    )

wlsxAuthMaxUserEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1011)
)
if mibBuilder.loadTexts:
    wlsxAuthMaxUserEntries.setStatus(
        "current"
    )

wlsxAuthMaxAclEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1012)
)
if mibBuilder.loadTexts:
    wlsxAuthMaxAclEntries.setStatus(
        "current"
    )

wlsxAuthMaxBWContracts = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1013)
)
if mibBuilder.loadTexts:
    wlsxAuthMaxBWContracts.setStatus(
        "current"
    )

wlsxPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1014)
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyFailure.setStatus(
        "current"
    )

wlsxFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1015)
)
wlsxFanFailure.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxFanNumber")
)
if mibBuilder.loadTexts:
    wlsxFanFailure.setStatus(
        "current"
    )

wlsxOutOfRangeVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1016)
)
wlsxOutOfRangeVoltage.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxVoltageType"),
        ("WLSX-SWITCH-MIB", "wlsxVoltageValue"))
)
if mibBuilder.loadTexts:
    wlsxOutOfRangeVoltage.setStatus(
        "current"
    )

wlsxOutOfRangeTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1017)
)
wlsxOutOfRangeTemperature.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxTemperatureValue")
)
if mibBuilder.loadTexts:
    wlsxOutOfRangeTemperature.setStatus(
        "current"
    )

wlsxLCInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1018)
)
wlsxLCInserted.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxLineCardNumber"),
        ("WLSX-SWITCH-MIB", "wlsxSlotNumber"))
)
if mibBuilder.loadTexts:
    wlsxLCInserted.setStatus(
        "current"
    )

wlsxSCInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1019)
)
if mibBuilder.loadTexts:
    wlsxSCInserted.setStatus(
        "current"
    )

wlsxGBICInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1020)
)
if mibBuilder.loadTexts:
    wlsxGBICInserted.setStatus(
        "current"
    )

wlsxProcessDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1021)
)
wlsxProcessDied.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxProcessName")
)
if mibBuilder.loadTexts:
    wlsxProcessDied.setStatus(
        "current"
    )

wlsxProcessExceedsMemoryLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1022)
)
wlsxProcessExceedsMemoryLimits.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxProcessName")
)
if mibBuilder.loadTexts:
    wlsxProcessExceedsMemoryLimits.setStatus(
        "current"
    )

wlsxLowOnFlashSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1023)
)
if mibBuilder.loadTexts:
    wlsxLowOnFlashSpace.setStatus(
        "current"
    )

wlsxLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1024)
)
if mibBuilder.loadTexts:
    wlsxLowMemory.setStatus(
        "current"
    )

wlsxFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1025)
)
if mibBuilder.loadTexts:
    wlsxFanTrayRemoved.setStatus(
        "current"
    )

wlsxFanTrayInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1026)
)
if mibBuilder.loadTexts:
    wlsxFanTrayInserted.setStatus(
        "current"
    )

wlsxLCRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1027)
)
wlsxLCRemoved.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxLineCardNumber"),
        ("WLSX-SWITCH-MIB", "wlsxSlotNumber"))
)
if mibBuilder.loadTexts:
    wlsxLCRemoved.setStatus(
        "current"
    )

wlsxSCRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1028)
)
if mibBuilder.loadTexts:
    wlsxSCRemoved.setStatus(
        "current"
    )

wlsxPowerSupplyMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1029)
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyMissing.setStatus(
        "current"
    )

wlsxAccessPointIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1030)
)
wlsxAccessPointIsUp.setObjects(
      *(("WLSX-SWITCH-MIB", "apLocation"),
        ("WLSX-SWITCH-MIB", "apIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxAccessPointIsUp.setStatus(
        "deprecated"
    )

wlsxAccessPointIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1031)
)
wlsxAccessPointIsDown.setObjects(
      *(("WLSX-SWITCH-MIB", "apLocation"),
        ("WLSX-SWITCH-MIB", "apIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxAccessPointIsDown.setStatus(
        "deprecated"
    )

wlsxCoverageHoleDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1032)
)
wlsxCoverageHoleDetected.setObjects(
      *(("WLSX-SWITCH-MIB", "apLocation"),
        ("WLSX-SWITCH-MIB", "apIpAddress"),
        ("WLSX-SWITCH-MIB", "wlsxStationMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxCoverageHoleDetected.setStatus(
        "current"
    )

wlsxChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1033)
)
wlsxChannelChanged.setObjects(
      *(("WLSX-SWITCH-MIB", "apLocation"),
        ("WLSX-SWITCH-MIB", "apIpAddress"),
        ("WLSX-SWITCH-MIB", "apCurrentChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelChanged.setStatus(
        "deprecated"
    )

wlsxStationAddedToBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1034)
)
wlsxStationAddedToBlackList.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxStationMacAddress"),
        ("WLSX-SWITCH-MIB", "wlsxStationBlackListReason"))
)
if mibBuilder.loadTexts:
    wlsxStationAddedToBlackList.setStatus(
        "current"
    )

wlsxStationRemovedFromBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1035)
)
wlsxStationRemovedFromBlackList.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxStationMacAddress")
)
if mibBuilder.loadTexts:
    wlsxStationRemovedFromBlackList.setStatus(
        "current"
    )

wlsxIpSpoofingDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1036)
)
wlsxIpSpoofingDetected.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxSpoofedIpAddress"),
        ("WLSX-SWITCH-MIB", "wlsxSpoofedOldPhyAddress"),
        ("WLSX-SWITCH-MIB", "wlsxSpoofedNewPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxIpSpoofingDetected.setStatus(
        "current"
    )

wlsxDBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1037)
)
wlsxDBCommunicationFailure.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxDBName"),
        ("WLSX-SWITCH-MIB", "wlsxDBUserName"),
        ("WLSX-SWITCH-MIB", "wlsxDBIpAddress"),
        ("WLSX-SWITCH-MIB", "wlsxDBType"))
)
if mibBuilder.loadTexts:
    wlsxDBCommunicationFailure.setStatus(
        "current"
    )

wlsxVrrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1038)
)
wlsxVrrpStateChange.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxVrID"),
        ("WLSX-SWITCH-MIB", "wlsxVrMasterIp"),
        ("WLSX-SWITCH-MIB", "wlsxVrrpOperState"))
)
if mibBuilder.loadTexts:
    wlsxVrrpStateChange.setStatus(
        "current"
    )

wlsxAPRadioAttributesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1039)
)
wlsxAPRadioAttributesChanged.setObjects(
      *(("WLSX-SWITCH-MIB", "apLocation"),
        ("WLSX-SWITCH-MIB", "apIpAddress"),
        ("WLSX-SWITCH-MIB", "apCurrentChannel"),
        ("WLSX-SWITCH-MIB", "wlsxApTxPower"))
)
if mibBuilder.loadTexts:
    wlsxAPRadioAttributesChanged.setStatus(
        "current"
    )

wlsxESIServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1040)
)
wlsxESIServerUp.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxESIServerGrpName"),
        ("WLSX-SWITCH-MIB", "wlsxESIServerName"),
        ("WLSX-SWITCH-MIB", "wlsxESIServerIpaddress"))
)
if mibBuilder.loadTexts:
    wlsxESIServerUp.setStatus(
        "current"
    )

wlsxESIServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1041)
)
wlsxESIServerDown.setObjects(
      *(("WLSX-SWITCH-MIB", "wlsxESIServerGrpName"),
        ("WLSX-SWITCH-MIB", "wlsxESIServerName"),
        ("WLSX-SWITCH-MIB", "wlsxESIServerIpaddress"))
)
if mibBuilder.loadTexts:
    wlsxESIServerDown.setStatus(
        "current"
    )

wlsxLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 1, 100, 1042)
)
wlsxLicenseExpiry.setObjects(
    ("WLSX-SWITCH-MIB", "wlsxLicenseDaysRemaining")
)
if mibBuilder.loadTexts:
    wlsxLicenseExpiry.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-SWITCH-MIB",
    **{"wlsxSwitchMIB": wlsxSwitchMIB,
       "wlsxSystemXGroup": wlsxSystemXGroup,
       "wlsxHostname": wlsxHostname,
       "wlsxModelName": wlsxModelName,
       "wlsxSwitchIp": wlsxSwitchIp,
       "wlsxSwitchRole": wlsxSwitchRole,
       "wlsxSwitchMasterIp": wlsxSwitchMasterIp,
       "wlsxSwitchListTable": wlsxSwitchListTable,
       "wlsxSwitchListEntry": wlsxSwitchListEntry,
       "switchListSwitchIPAddress": switchListSwitchIPAddress,
       "switchListSwitchRole": switchListSwitchRole,
       "wlsxSwitchLicenseCount": wlsxSwitchLicenseCount,
       "wlsxSwitchLicenseTable": wlsxSwitchLicenseTable,
       "wlsxLicenseEntry": wlsxLicenseEntry,
       "licenseIndex": licenseIndex,
       "licenseKey": licenseKey,
       "licenseInstalled": licenseInstalled,
       "licenseExpires": licenseExpires,
       "licenseFlags": licenseFlags,
       "licenseService": licenseService,
       "wlsxSysXProcessorTable": wlsxSysXProcessorTable,
       "wlsxSysXProcessorEntry": wlsxSysXProcessorEntry,
       "sysXProcessorID": sysXProcessorID,
       "sysXProcessorDescr": sysXProcessorDescr,
       "sysXProcessorLoad": sysXProcessorLoad,
       "wlsxSysXStorageTable": wlsxSysXStorageTable,
       "wlsxSysXStorageEntry": wlsxSysXStorageEntry,
       "sysXStorageIndex": sysXStorageIndex,
       "sysXStorageType": sysXStorageType,
       "sysXStorageSize": sysXStorageSize,
       "sysXStorageUsed": sysXStorageUsed,
       "sysXStorageName": sysXStorageName,
       "wlsxSysXMemoryTable": wlsxSysXMemoryTable,
       "wlsxSysXMemoryEntry": wlsxSysXMemoryEntry,
       "sysXMemoryIndex": sysXMemoryIndex,
       "sysXMemorySize": sysXMemorySize,
       "sysXMemoryUsed": sysXMemoryUsed,
       "sysXMemoryFree": sysXMemoryFree,
       "wlsxSwitchLicenseSerialNumber": wlsxSwitchLicenseSerialNumber,
       "wlsxUserInfoGroup": wlsxUserInfoGroup,
       "wlsxSwitchUserTable": wlsxSwitchUserTable,
       "wlsxSwitchUserEntry": wlsxSwitchUserEntry,
       "userIpAddress": userIpAddress,
       "userPhyAddress": userPhyAddress,
       "userName": userName,
       "userRole": userRole,
       "userUpTime": userUpTime,
       "userAuthenticationMethod": userAuthenticationMethod,
       "userLocation": userLocation,
       "userServerName": userServerName,
       "userConnectedVlan": userConnectedVlan,
       "userConnectedSlot": userConnectedSlot,
       "userConnectedPort": userConnectedPort,
       "userBWContractName": userBWContractName,
       "userBWContractUsage": userBWContractUsage,
       "userConnectedModule": userConnectedModule,
       "wlsxSwitchStationMgmtTable": wlsxSwitchStationMgmtTable,
       "wlsxSwitchStationMgmtEntry": wlsxSwitchStationMgmtEntry,
       "staPhyAddress": staPhyAddress,
       "staAccessPointBSSID": staAccessPointBSSID,
       "staUserName": staUserName,
       "staUserRole": staUserRole,
       "staAssociationID": staAssociationID,
       "staAccessPointESSID": staAccessPointESSID,
       "staSignalToNoiseRatio": staSignalToNoiseRatio,
       "staTransmitRate": staTransmitRate,
       "staReceiveRate": staReceiveRate,
       "wlsxSwitchStationStatsTable": wlsxSwitchStationStatsTable,
       "wlsxSwitchStationStatsEntry": wlsxSwitchStationStatsEntry,
       "staTxPackets": staTxPackets,
       "staTxBytes": staTxBytes,
       "staRxPackets": staRxPackets,
       "staRxBytes": staRxBytes,
       "staBwRate": staBwRate,
       "staFrameRetryRate": staFrameRetryRate,
       "staFrameLowSpeedRate": staFrameLowSpeedRate,
       "staFrameNonUnicastRate": staFrameNonUnicastRate,
       "staFrameFragmentationRate": staFrameFragmentationRate,
       "staFrameReceiveErrorRate": staFrameReceiveErrorRate,
       "wlsxAccessPointInfoGroup": wlsxAccessPointInfoGroup,
       "wlsxSwitchTotalNumAccessPoints": wlsxSwitchTotalNumAccessPoints,
       "wlsxSwitchTotalNumStationsAssociated": wlsxSwitchTotalNumStationsAssociated,
       "wlsxSwitchAccessPointTable": wlsxSwitchAccessPointTable,
       "wlsxSwitchAccessPointEntry": wlsxSwitchAccessPointEntry,
       "apBSSID": apBSSID,
       "apESSID": apESSID,
       "apSlot": apSlot,
       "apPort": apPort,
       "apIpAddress": apIpAddress,
       "apPhyType": apPhyType,
       "apType": apType,
       "apCurrentChannel": apCurrentChannel,
       "apLocation": apLocation,
       "apTotalTime": apTotalTime,
       "apInactiveTime": apInactiveTime,
       "apLoadBalancing": apLoadBalancing,
       "apChannelNoise": apChannelNoise,
       "apSignalToNoiseRatio": apSignalToNoiseRatio,
       "apTransmitRate": apTransmitRate,
       "apReceiveRate": apReceiveRate,
       "wlsxSwitchGlobalAPTable": wlsxSwitchGlobalAPTable,
       "wlsxSwitchGlobalAPEntry": wlsxSwitchGlobalAPEntry,
       "globalAPLocation": globalAPLocation,
       "globalAPAddress": globalAPAddress,
       "globalAPLocalSwitch": globalAPLocalSwitch,
       "globalAPdot11aPhyAddr": globalAPdot11aPhyAddr,
       "globalAPdot11bPhyAddr": globalAPdot11bPhyAddr,
       "globalAPState": globalAPState,
       "globalAPdot11gPhyAddr": globalAPdot11gPhyAddr,
       "wlsxSwitchAccessPointStatsTable": wlsxSwitchAccessPointStatsTable,
       "wlsxSwitchAccessPointStatsEntry": wlsxSwitchAccessPointStatsEntry,
       "apStatsChannel": apStatsChannel,
       "apChannelBwRate": apChannelBwRate,
       "apChannelFrameRetryRate": apChannelFrameRetryRate,
       "apChannelFrameLowSpeedRate": apChannelFrameLowSpeedRate,
       "apChannelFrameNonUnicastRate": apChannelFrameNonUnicastRate,
       "apChannelFrameFragmentationRate": apChannelFrameFragmentationRate,
       "apChannelFrameReceiveErrorRate": apChannelFrameReceiveErrorRate,
       "apBSSTxPackets": apBSSTxPackets,
       "apBSSTxBytes": apBSSTxBytes,
       "apBSSRxPackets": apBSSRxPackets,
       "apBSSRxBytes": apBSSRxBytes,
       "apBSSBwRate": apBSSBwRate,
       "apBSSFrameRetryRate": apBSSFrameRetryRate,
       "apBSSFrameLowSpeedRate": apBSSFrameLowSpeedRate,
       "apBSSFrameNonUnicastRate": apBSSFrameNonUnicastRate,
       "apBSSFrameFragmentationRate": apBSSFrameFragmentationRate,
       "apBSSFrameReceiveErrorRate": apBSSFrameReceiveErrorRate,
       "wlsxSwitchTraps": wlsxSwitchTraps,
       "wlsxSwitchTrapObjectsGroup": wlsxSwitchTrapObjectsGroup,
       "wlsxAuthServerName": wlsxAuthServerName,
       "wlsxAuthServerTimeout": wlsxAuthServerTimeout,
       "wlsxFanNumber": wlsxFanNumber,
       "wlsxLineCardNumber": wlsxLineCardNumber,
       "wlsxVoltageType": wlsxVoltageType,
       "wlsxVoltageValue": wlsxVoltageValue,
       "wlsxTemperatureValue": wlsxTemperatureValue,
       "wlsxProcessName": wlsxProcessName,
       "wlsxStationMacAddress": wlsxStationMacAddress,
       "wlsxStationBlackListReason": wlsxStationBlackListReason,
       "wlsxSpoofedIpAddress": wlsxSpoofedIpAddress,
       "wlsxSpoofedOldPhyAddress": wlsxSpoofedOldPhyAddress,
       "wlsxSpoofedNewPhyAddress": wlsxSpoofedNewPhyAddress,
       "wlsxDBName": wlsxDBName,
       "wlsxDBUserName": wlsxDBUserName,
       "wlsxDBIpAddress": wlsxDBIpAddress,
       "wlsxDBType": wlsxDBType,
       "wlsxVrID": wlsxVrID,
       "wlsxVrMasterIp": wlsxVrMasterIp,
       "wlsxVrrpOperState": wlsxVrrpOperState,
       "wlsxApTxPower": wlsxApTxPower,
       "wlsxESIServerGrpName": wlsxESIServerGrpName,
       "wlsxESIServerName": wlsxESIServerName,
       "wlsxESIServerIpaddress": wlsxESIServerIpaddress,
       "wlsxLicenseDaysRemaining": wlsxLicenseDaysRemaining,
       "wlsxSlotNumber": wlsxSlotNumber,
       "wlsxSwitchIPChanged": wlsxSwitchIPChanged,
       "wlsxSwitchRoleChange": wlsxSwitchRoleChange,
       "wlsxUserEntryCreated": wlsxUserEntryCreated,
       "wlsxUserEntryDeleted": wlsxUserEntryDeleted,
       "wlsxUserEntryAuthenticated": wlsxUserEntryAuthenticated,
       "wlsxUserEntryDeAuthenticated": wlsxUserEntryDeAuthenticated,
       "wlsxUserAuthenticationFailed": wlsxUserAuthenticationFailed,
       "wlsxAuthServerReqTimedOut": wlsxAuthServerReqTimedOut,
       "wlsxAuthServerTimedOut": wlsxAuthServerTimedOut,
       "wlsxAuthServerIsUp": wlsxAuthServerIsUp,
       "wlsxAuthMaxUserEntries": wlsxAuthMaxUserEntries,
       "wlsxAuthMaxAclEntries": wlsxAuthMaxAclEntries,
       "wlsxAuthMaxBWContracts": wlsxAuthMaxBWContracts,
       "wlsxPowerSupplyFailure": wlsxPowerSupplyFailure,
       "wlsxFanFailure": wlsxFanFailure,
       "wlsxOutOfRangeVoltage": wlsxOutOfRangeVoltage,
       "wlsxOutOfRangeTemperature": wlsxOutOfRangeTemperature,
       "wlsxLCInserted": wlsxLCInserted,
       "wlsxSCInserted": wlsxSCInserted,
       "wlsxGBICInserted": wlsxGBICInserted,
       "wlsxProcessDied": wlsxProcessDied,
       "wlsxProcessExceedsMemoryLimits": wlsxProcessExceedsMemoryLimits,
       "wlsxLowOnFlashSpace": wlsxLowOnFlashSpace,
       "wlsxLowMemory": wlsxLowMemory,
       "wlsxFanTrayRemoved": wlsxFanTrayRemoved,
       "wlsxFanTrayInserted": wlsxFanTrayInserted,
       "wlsxLCRemoved": wlsxLCRemoved,
       "wlsxSCRemoved": wlsxSCRemoved,
       "wlsxPowerSupplyMissing": wlsxPowerSupplyMissing,
       "wlsxAccessPointIsUp": wlsxAccessPointIsUp,
       "wlsxAccessPointIsDown": wlsxAccessPointIsDown,
       "wlsxCoverageHoleDetected": wlsxCoverageHoleDetected,
       "wlsxChannelChanged": wlsxChannelChanged,
       "wlsxStationAddedToBlackList": wlsxStationAddedToBlackList,
       "wlsxStationRemovedFromBlackList": wlsxStationRemovedFromBlackList,
       "wlsxIpSpoofingDetected": wlsxIpSpoofingDetected,
       "wlsxDBCommunicationFailure": wlsxDBCommunicationFailure,
       "wlsxVrrpStateChange": wlsxVrrpStateChange,
       "wlsxAPRadioAttributesChanged": wlsxAPRadioAttributesChanged,
       "wlsxESIServerUp": wlsxESIServerUp,
       "wlsxESIServerDown": wlsxESIServerDown,
       "wlsxLicenseExpiry": wlsxLicenseExpiry}
)
