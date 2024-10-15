# SNMP MIB module (CPE-MANAGER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPE-MANAGER
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:09 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(cpeMgr,) = mibBuilder.importSymbols(
    "ZHONE-SYSTEM-MIB",
    "cpeMgr")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

cpeMgrModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1)
)
cpeMgrModule.setRevisions(
        ("2011-05-13 09:17",
         "2011-02-08 06:48",
         "2010-10-28 12:06",
         "2010-09-22 07:42",
         "2010-05-18 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpeMgrGlobal_ObjectIdentity = ObjectIdentity
cpeMgrGlobal = _CpeMgrGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    cpeMgrGlobal.setStatus("current")
_CpeMgrGlobalObjects_ObjectIdentity = ObjectIdentity
cpeMgrGlobalObjects = _CpeMgrGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpeMgrGlobalObjects.setStatus("current")


class _CpeMgrLocalVlanId_Type(Unsigned32):
    """Custom type cpeMgrLocalVlanId based on Unsigned32"""
    defaultValue = 7


_CpeMgrLocalVlanId_Object = MibScalar
cpeMgrLocalVlanId = _CpeMgrLocalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 1, 1),
    _CpeMgrLocalVlanId_Type()
)
cpeMgrLocalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeMgrLocalVlanId.setStatus("current")
_CpeMgrLocalSlanId_Type = Unsigned32
_CpeMgrLocalSlanId_Object = MibScalar
cpeMgrLocalSlanId = _CpeMgrLocalSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 1, 2),
    _CpeMgrLocalSlanId_Type()
)
cpeMgrLocalSlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeMgrLocalSlanId.setStatus("current")


class _CpeCfgMgrConcurrentUpdateLimit_Type(Unsigned32):
    """Custom type cpeCfgMgrConcurrentUpdateLimit based on Unsigned32"""
    defaultValue = 5


_CpeCfgMgrConcurrentUpdateLimit_Object = MibScalar
cpeCfgMgrConcurrentUpdateLimit = _CpeCfgMgrConcurrentUpdateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 1, 3),
    _CpeCfgMgrConcurrentUpdateLimit_Type()
)
cpeCfgMgrConcurrentUpdateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrConcurrentUpdateLimit.setStatus("current")
_CpeMgrGlobalConformance_ObjectIdentity = ObjectIdentity
cpeMgrGlobalConformance = _CpeMgrGlobalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpeMgrGlobalConformance.setStatus("current")
_CpeMgrGlobalGroups_ObjectIdentity = ObjectIdentity
cpeMgrGlobalGroups = _CpeMgrGlobalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpeMgrGlobalGroups.setStatus("current")
_CpeMgrGlobalCompliances_ObjectIdentity = ObjectIdentity
cpeMgrGlobalCompliances = _CpeMgrGlobalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpeMgrGlobalCompliances.setStatus("current")
_CpeConfigMgr_ObjectIdentity = ObjectIdentity
cpeConfigMgr = _CpeConfigMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2)
)
if mibBuilder.loadTexts:
    cpeConfigMgr.setStatus("current")
_CpeConfigMgrNotifications_ObjectIdentity = ObjectIdentity
cpeConfigMgrNotifications = _CpeConfigMgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0)
)
if mibBuilder.loadTexts:
    cpeConfigMgrNotifications.setStatus("current")
_CpeConfigMgrObjects_ObjectIdentity = ObjectIdentity
cpeConfigMgrObjects = _CpeConfigMgrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpeConfigMgrObjects.setStatus("current")
_CpeConfigMgrTable_Object = MibTable
cpeConfigMgrTable = _CpeConfigMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpeConfigMgrTable.setStatus("current")
_CpeConfigMgrEntry_Object = MibTableRow
cpeConfigMgrEntry = _CpeConfigMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1)
)
cpeConfigMgrEntry.setIndexNames(
    (0, "CPE-MANAGER", "cpeConfigMgrIndex"),
)
if mibBuilder.loadTexts:
    cpeConfigMgrEntry.setStatus("current")
_CpeConfigMgrRowStatus_Type = ZhoneRowStatus
_CpeConfigMgrRowStatus_Object = MibTableColumn
cpeConfigMgrRowStatus = _CpeConfigMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 1),
    _CpeConfigMgrRowStatus_Type()
)
cpeConfigMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrRowStatus.setStatus("current")


class _CpeConfigMgrIndex_Type(Integer32):
    """Custom type cpeConfigMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpeConfigMgrIndex_Type.__name__ = "Integer32"
_CpeConfigMgrIndex_Object = MibTableColumn
cpeConfigMgrIndex = _CpeConfigMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 2),
    _CpeConfigMgrIndex_Type()
)
cpeConfigMgrIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cpeConfigMgrIndex.setStatus("current")


class _CpeConfigMgrName_Type(OctetString):
    """Custom type cpeConfigMgrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CpeConfigMgrName_Type.__name__ = "OctetString"
_CpeConfigMgrName_Object = MibTableColumn
cpeConfigMgrName = _CpeConfigMgrName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 3),
    _CpeConfigMgrName_Type()
)
cpeConfigMgrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrName.setStatus("current")


class _CpeConfigMgrGroup_Type(Integer32):
    """Custom type cpeConfigMgrGroup based on Integer32"""
    defaultValue = 0


_CpeConfigMgrGroup_Object = MibTableColumn
cpeConfigMgrGroup = _CpeConfigMgrGroup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 4),
    _CpeConfigMgrGroup_Type()
)
cpeConfigMgrGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrGroup.setStatus("current")


class _ManagedCpeType_Type(OctetString):
    """Custom type managedCpeType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ManagedCpeType_Type.__name__ = "OctetString"
_ManagedCpeType_Object = MibTableColumn
managedCpeType = _ManagedCpeType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 5),
    _ManagedCpeType_Type()
)
managedCpeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managedCpeType.setStatus("current")


class _RequiredCpeSoftwareVersion_Type(OctetString):
    """Custom type requiredCpeSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RequiredCpeSoftwareVersion_Type.__name__ = "OctetString"
_RequiredCpeSoftwareVersion_Object = MibTableColumn
requiredCpeSoftwareVersion = _RequiredCpeSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 6),
    _RequiredCpeSoftwareVersion_Type()
)
requiredCpeSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requiredCpeSoftwareVersion.setStatus("current")


class _RequiredCpeSoftwareFilename_Type(OctetString):
    """Custom type requiredCpeSoftwareFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RequiredCpeSoftwareFilename_Type.__name__ = "OctetString"
_RequiredCpeSoftwareFilename_Object = MibTableColumn
requiredCpeSoftwareFilename = _RequiredCpeSoftwareFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 7),
    _RequiredCpeSoftwareFilename_Type()
)
requiredCpeSoftwareFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requiredCpeSoftwareFilename.setStatus("current")


class _RequiredCpeWebUIVersion_Type(OctetString):
    """Custom type requiredCpeWebUIVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RequiredCpeWebUIVersion_Type.__name__ = "OctetString"
_RequiredCpeWebUIVersion_Object = MibTableColumn
requiredCpeWebUIVersion = _RequiredCpeWebUIVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 8),
    _RequiredCpeWebUIVersion_Type()
)
requiredCpeWebUIVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requiredCpeWebUIVersion.setStatus("current")


class _RequiredCpeWebUIFilename_Type(OctetString):
    """Custom type requiredCpeWebUIFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RequiredCpeWebUIFilename_Type.__name__ = "OctetString"
_RequiredCpeWebUIFilename_Object = MibTableColumn
requiredCpeWebUIFilename = _RequiredCpeWebUIFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 9),
    _RequiredCpeWebUIFilename_Type()
)
requiredCpeWebUIFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requiredCpeWebUIFilename.setStatus("current")


class _RequiredCpeGenericConfigFile_Type(OctetString):
    """Custom type requiredCpeGenericConfigFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RequiredCpeGenericConfigFile_Type.__name__ = "OctetString"
_RequiredCpeGenericConfigFile_Object = MibTableColumn
requiredCpeGenericConfigFile = _RequiredCpeGenericConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 10),
    _RequiredCpeGenericConfigFile_Type()
)
requiredCpeGenericConfigFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    requiredCpeGenericConfigFile.setStatus("current")


class _CpeLeaseTimeUpdate_Type(Integer32):
    """Custom type cpeLeaseTimeUpdate based on Integer32"""
    defaultValue = 300


_CpeLeaseTimeUpdate_Object = MibTableColumn
cpeLeaseTimeUpdate = _CpeLeaseTimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 11),
    _CpeLeaseTimeUpdate_Type()
)
cpeLeaseTimeUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeLeaseTimeUpdate.setStatus("current")
if mibBuilder.loadTexts:
    cpeLeaseTimeUpdate.setUnits("Seconds")


class _CpeLeaseTimeOperational_Type(Integer32):
    """Custom type cpeLeaseTimeOperational based on Integer32"""
    defaultValue = 86400


_CpeLeaseTimeOperational_Object = MibTableColumn
cpeLeaseTimeOperational = _CpeLeaseTimeOperational_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 12),
    _CpeLeaseTimeOperational_Type()
)
cpeLeaseTimeOperational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeLeaseTimeOperational.setStatus("current")
if mibBuilder.loadTexts:
    cpeLeaseTimeOperational.setUnits("Seconds")
_CpeConfigMgrDwnldSrvrToUsed_Type = Unsigned32
_CpeConfigMgrDwnldSrvrToUsed_Object = MibTableColumn
cpeConfigMgrDwnldSrvrToUsed = _CpeConfigMgrDwnldSrvrToUsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 13),
    _CpeConfigMgrDwnldSrvrToUsed_Type()
)
cpeConfigMgrDwnldSrvrToUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrDwnldSrvrToUsed.setStatus("current")


class _CpeConfigMgrDownloadBasePath_Type(OctetString):
    """Custom type cpeConfigMgrDownloadBasePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeConfigMgrDownloadBasePath_Type.__name__ = "OctetString"
_CpeConfigMgrDownloadBasePath_Object = MibTableColumn
cpeConfigMgrDownloadBasePath = _CpeConfigMgrDownloadBasePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 14),
    _CpeConfigMgrDownloadBasePath_Type()
)
cpeConfigMgrDownloadBasePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrDownloadBasePath.setStatus("current")


class _CpeConfigMgrDownloadSecureMode_Type(Integer32):
    """Custom type cpeConfigMgrDownloadSecureMode based on Integer32"""
    defaultValue = 3

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
          ("noPreference", 3))
    )


_CpeConfigMgrDownloadSecureMode_Type.__name__ = "Integer32"
_CpeConfigMgrDownloadSecureMode_Object = MibTableColumn
cpeConfigMgrDownloadSecureMode = _CpeConfigMgrDownloadSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 15),
    _CpeConfigMgrDownloadSecureMode_Type()
)
cpeConfigMgrDownloadSecureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrDownloadSecureMode.setStatus("current")


class _CpeConfigMgrTrapsEnabled_Type(TruthValue):
    """Custom type cpeConfigMgrTrapsEnabled based on TruthValue"""


_CpeConfigMgrTrapsEnabled_Object = MibTableColumn
cpeConfigMgrTrapsEnabled = _CpeConfigMgrTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 16),
    _CpeConfigMgrTrapsEnabled_Type()
)
cpeConfigMgrTrapsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrTrapsEnabled.setStatus("current")
_CpeConfigScriptIndex_Type = Unsigned32
_CpeConfigScriptIndex_Object = MibTableColumn
cpeConfigScriptIndex = _CpeConfigScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 17),
    _CpeConfigScriptIndex_Type()
)
cpeConfigScriptIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigScriptIndex.setStatus("current")
_CpeConfigVarsIndex_Type = Unsigned32
_CpeConfigVarsIndex_Object = MibTableColumn
cpeConfigVarsIndex = _CpeConfigVarsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 1, 1, 18),
    _CpeConfigVarsIndex_Type()
)
cpeConfigVarsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigVarsIndex.setStatus("current")
_CpeConfigMgrDownloadServerTable_Object = MibTable
cpeConfigMgrDownloadServerTable = _CpeConfigMgrDownloadServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpeConfigMgrDownloadServerTable.setStatus("current")
_CpeConfigMgrDownloadServerEntry_Object = MibTableRow
cpeConfigMgrDownloadServerEntry = _CpeConfigMgrDownloadServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1)
)
cpeConfigMgrDownloadServerEntry.setIndexNames(
    (0, "CPE-MANAGER", "cpeCfgMgrDwnldSrvrIndex"),
)
if mibBuilder.loadTexts:
    cpeConfigMgrDownloadServerEntry.setStatus("current")
_CpeCfgMgrDwnldSrvrRowStatus_Type = ZhoneRowStatus
_CpeCfgMgrDwnldSrvrRowStatus_Object = MibTableColumn
cpeCfgMgrDwnldSrvrRowStatus = _CpeCfgMgrDwnldSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 1),
    _CpeCfgMgrDwnldSrvrRowStatus_Type()
)
cpeCfgMgrDwnldSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrRowStatus.setStatus("current")
_CpeCfgMgrDwnldSrvrIndex_Type = Unsigned32
_CpeCfgMgrDwnldSrvrIndex_Object = MibTableColumn
cpeCfgMgrDwnldSrvrIndex = _CpeCfgMgrDwnldSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 2),
    _CpeCfgMgrDwnldSrvrIndex_Type()
)
cpeCfgMgrDwnldSrvrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrIndex.setStatus("current")


class _CpeCfgMgrDwnldSrvrIP_Type(IpAddress):
    """Custom type cpeCfgMgrDwnldSrvrIP based on IpAddress"""
    defaultHexValue = "00000000"


_CpeCfgMgrDwnldSrvrIP_Object = MibTableColumn
cpeCfgMgrDwnldSrvrIP = _CpeCfgMgrDwnldSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 3),
    _CpeCfgMgrDwnldSrvrIP_Type()
)
cpeCfgMgrDwnldSrvrIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrIP.setStatus("current")


class _CpeCfgMgrDwnldSrvrUsername_Type(OctetString):
    """Custom type cpeCfgMgrDwnldSrvrUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpeCfgMgrDwnldSrvrUsername_Type.__name__ = "OctetString"
_CpeCfgMgrDwnldSrvrUsername_Object = MibTableColumn
cpeCfgMgrDwnldSrvrUsername = _CpeCfgMgrDwnldSrvrUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 4),
    _CpeCfgMgrDwnldSrvrUsername_Type()
)
cpeCfgMgrDwnldSrvrUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrUsername.setStatus("current")


class _CpeCfgMgrDwnldSrvrPassword_Type(OctetString):
    """Custom type cpeCfgMgrDwnldSrvrPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpeCfgMgrDwnldSrvrPassword_Type.__name__ = "OctetString"
_CpeCfgMgrDwnldSrvrPassword_Object = MibTableColumn
cpeCfgMgrDwnldSrvrPassword = _CpeCfgMgrDwnldSrvrPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 5),
    _CpeCfgMgrDwnldSrvrPassword_Type()
)
cpeCfgMgrDwnldSrvrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrPassword.setStatus("current")
_CpeCfgMgrDwnldSrvrDefault_Type = TruthValue
_CpeCfgMgrDwnldSrvrDefault_Object = MibTableColumn
cpeCfgMgrDwnldSrvrDefault = _CpeCfgMgrDwnldSrvrDefault_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 2, 1, 6),
    _CpeCfgMgrDwnldSrvrDefault_Type()
)
cpeCfgMgrDwnldSrvrDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeCfgMgrDwnldSrvrDefault.setStatus("current")
_CpeConfigMgrMemberTable_Object = MibTable
cpeConfigMgrMemberTable = _CpeConfigMgrMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cpeConfigMgrMemberTable.setStatus("current")
_CpeConfigMgrMemberEntry_Object = MibTableRow
cpeConfigMgrMemberEntry = _CpeConfigMgrMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1)
)
cpeConfigMgrMemberEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpeConfigMgrMemberEntry.setStatus("current")
_CpeConfigMgrMemberRowStatus_Type = ZhoneRowStatus
_CpeConfigMgrMemberRowStatus_Object = MibTableColumn
cpeConfigMgrMemberRowStatus = _CpeConfigMgrMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1, 1),
    _CpeConfigMgrMemberRowStatus_Type()
)
cpeConfigMgrMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrMemberRowStatus.setStatus("current")


class _CpeConfigMgrGroupMembership_Type(Unsigned32):
    """Custom type cpeConfigMgrGroupMembership based on Unsigned32"""
    defaultValue = 0


_CpeConfigMgrGroupMembership_Object = MibTableColumn
cpeConfigMgrGroupMembership = _CpeConfigMgrGroupMembership_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1, 2),
    _CpeConfigMgrGroupMembership_Type()
)
cpeConfigMgrGroupMembership.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrGroupMembership.setStatus("current")


class _CpeSpecificConfigFile_Type(OctetString):
    """Custom type cpeSpecificConfigFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeSpecificConfigFile_Type.__name__ = "OctetString"
_CpeSpecificConfigFile_Object = MibTableColumn
cpeSpecificConfigFile = _CpeSpecificConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1, 3),
    _CpeSpecificConfigFile_Type()
)
cpeSpecificConfigFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeSpecificConfigFile.setStatus("current")


class _CpeSpecificDownloadPath_Type(OctetString):
    """Custom type cpeSpecificDownloadPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpeSpecificDownloadPath_Type.__name__ = "OctetString"
_CpeSpecificDownloadPath_Object = MibTableColumn
cpeSpecificDownloadPath = _CpeSpecificDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1, 4),
    _CpeSpecificDownloadPath_Type()
)
cpeSpecificDownloadPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeSpecificDownloadPath.setStatus("current")


class _CpeConfigMgrMemberTrapsEnabled_Type(TruthValue):
    """Custom type cpeConfigMgrMemberTrapsEnabled based on TruthValue"""


_CpeConfigMgrMemberTrapsEnabled_Object = MibTableColumn
cpeConfigMgrMemberTrapsEnabled = _CpeConfigMgrMemberTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 3, 1, 5),
    _CpeConfigMgrMemberTrapsEnabled_Type()
)
cpeConfigMgrMemberTrapsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpeConfigMgrMemberTrapsEnabled.setStatus("current")
_CpeConfigMgrMemberStatusTable_Object = MibTable
cpeConfigMgrMemberStatusTable = _CpeConfigMgrMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cpeConfigMgrMemberStatusTable.setStatus("current")
_CpeConfigMgrMemberStatusEntry_Object = MibTableRow
cpeConfigMgrMemberStatusEntry = _CpeConfigMgrMemberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1)
)
cpeConfigMgrMemberStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpeConfigMgrMemberStatusEntry.setStatus("current")


class _CpeConfigMgrMemberStatus_Type(Bits):
    """Custom type cpeConfigMgrMemberStatus based on Bits"""
    namedValues = NamedValues(
        *(("configBackupNeeded", 10),
          ("configUpdateNeeded", 9),
          ("cpeTypeMismatch", 4),
          ("downloadStormThrottled", 5),
          ("errorsDetected", 3),
          ("noUpdateRequired", 1),
          ("notCompared", 0),
          ("provisioningActive", 12),
          ("provisioningError", 13),
          ("provisioningPending", 11),
          ("softwareUpgradeNeeded", 7),
          ("updateRetryLimitExceeded", 6),
          ("upgradeInfoSent", 2),
          ("webuiUpgradeNeeded", 8))
    )

_CpeConfigMgrMemberStatus_Type.__name__ = "Bits"
_CpeConfigMgrMemberStatus_Object = MibTableColumn
cpeConfigMgrMemberStatus = _CpeConfigMgrMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 1),
    _CpeConfigMgrMemberStatus_Type()
)
cpeConfigMgrMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeConfigMgrMemberStatus.setStatus("current")


class _CpeConfigMgrUsed_Type(Integer32):
    """Custom type cpeConfigMgrUsed based on Integer32"""
    defaultValue = 0


_CpeConfigMgrUsed_Object = MibTableColumn
cpeConfigMgrUsed = _CpeConfigMgrUsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 2),
    _CpeConfigMgrUsed_Type()
)
cpeConfigMgrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeConfigMgrUsed.setStatus("current")


class _ReportedCpeType_Type(OctetString):
    """Custom type reportedCpeType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ReportedCpeType_Type.__name__ = "OctetString"
_ReportedCpeType_Object = MibTableColumn
reportedCpeType = _ReportedCpeType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 3),
    _ReportedCpeType_Type()
)
reportedCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeType.setStatus("current")


class _ReportedCpeSoftwareVersion_Type(OctetString):
    """Custom type reportedCpeSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ReportedCpeSoftwareVersion_Type.__name__ = "OctetString"
_ReportedCpeSoftwareVersion_Object = MibTableColumn
reportedCpeSoftwareVersion = _ReportedCpeSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 4),
    _ReportedCpeSoftwareVersion_Type()
)
reportedCpeSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeSoftwareVersion.setStatus("current")


class _ReportedCpeWebUIVersion_Type(OctetString):
    """Custom type reportedCpeWebUIVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ReportedCpeWebUIVersion_Type.__name__ = "OctetString"
_ReportedCpeWebUIVersion_Object = MibTableColumn
reportedCpeWebUIVersion = _ReportedCpeWebUIVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 5),
    _ReportedCpeWebUIVersion_Type()
)
reportedCpeWebUIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeWebUIVersion.setStatus("current")


class _ReportedCpeConfigFilename_Type(OctetString):
    """Custom type reportedCpeConfigFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ReportedCpeConfigFilename_Type.__name__ = "OctetString"
_ReportedCpeConfigFilename_Object = MibTableColumn
reportedCpeConfigFilename = _ReportedCpeConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 6),
    _ReportedCpeConfigFilename_Type()
)
reportedCpeConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeConfigFilename.setStatus("current")


class _ReportedCpeSerialNumber_Type(OctetString):
    """Custom type reportedCpeSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ReportedCpeSerialNumber_Type.__name__ = "OctetString"
_ReportedCpeSerialNumber_Object = MibTableColumn
reportedCpeSerialNumber = _ReportedCpeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 7),
    _ReportedCpeSerialNumber_Type()
)
reportedCpeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeSerialNumber.setStatus("current")


class _ReportedCpeRegistrationID_Type(OctetString):
    """Custom type reportedCpeRegistrationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ReportedCpeRegistrationID_Type.__name__ = "OctetString"
_ReportedCpeRegistrationID_Object = MibTableColumn
reportedCpeRegistrationID = _ReportedCpeRegistrationID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 8),
    _ReportedCpeRegistrationID_Type()
)
reportedCpeRegistrationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeRegistrationID.setStatus("current")


class _ReportedCpeFSAN_Type(OctetString):
    """Custom type reportedCpeFSAN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ReportedCpeFSAN_Type.__name__ = "OctetString"
_ReportedCpeFSAN_Object = MibTableColumn
reportedCpeFSAN = _ReportedCpeFSAN_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 9),
    _ReportedCpeFSAN_Type()
)
reportedCpeFSAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeFSAN.setStatus("current")
_ReportedCpeMacAddress_Type = MacAddress
_ReportedCpeMacAddress_Object = MibTableColumn
reportedCpeMacAddress = _ReportedCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 10),
    _ReportedCpeMacAddress_Type()
)
reportedCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeMacAddress.setStatus("current")


class _ReportedDwnldSrvrBasePath_Type(OctetString):
    """Custom type reportedDwnldSrvrBasePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ReportedDwnldSrvrBasePath_Type.__name__ = "OctetString"
_ReportedDwnldSrvrBasePath_Object = MibTableColumn
reportedDwnldSrvrBasePath = _ReportedDwnldSrvrBasePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 11),
    _ReportedDwnldSrvrBasePath_Type()
)
reportedDwnldSrvrBasePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedDwnldSrvrBasePath.setStatus("current")


class _ReportedDwnldSrvrSpecificPath_Type(OctetString):
    """Custom type reportedDwnldSrvrSpecificPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ReportedDwnldSrvrSpecificPath_Type.__name__ = "OctetString"
_ReportedDwnldSrvrSpecificPath_Object = MibTableColumn
reportedDwnldSrvrSpecificPath = _ReportedDwnldSrvrSpecificPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 12),
    _ReportedDwnldSrvrSpecificPath_Type()
)
reportedDwnldSrvrSpecificPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedDwnldSrvrSpecificPath.setStatus("current")


class _ReportedCpeState_Type(Integer32):
    """Custom type reportedCpeState based on Integer32"""
    defaultValue = -1


_ReportedCpeState_Object = MibTableColumn
reportedCpeState = _ReportedCpeState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 1, 4, 1, 13),
    _ReportedCpeState_Type()
)
reportedCpeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportedCpeState.setStatus("current")
_CpeConfigMgrConformance_ObjectIdentity = ObjectIdentity
cpeConfigMgrConformance = _CpeConfigMgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpeConfigMgrConformance.setStatus("current")
_CpeConfigMgrGroups_ObjectIdentity = ObjectIdentity
cpeConfigMgrGroups = _CpeConfigMgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpeConfigMgrGroups.setStatus("current")
_CpeConfigMgrCompliances_ObjectIdentity = ObjectIdentity
cpeConfigMgrCompliances = _CpeConfigMgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpeConfigMgrCompliances.setStatus("current")
_CpeConfigMgrClient_ObjectIdentity = ObjectIdentity
cpeConfigMgrClient = _CpeConfigMgrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3)
)
if mibBuilder.loadTexts:
    cpeConfigMgrClient.setStatus("current")
_CpeCfgMgrClientNotifications_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientNotifications = _CpeCfgMgrClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientNotifications.setStatus("current")
_CpeCfgMgrClientObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientObjects = _CpeCfgMgrClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientObjects.setStatus("current")
_CpeCfgMgrClientIdObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientIdObjects = _CpeCfgMgrClientIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientIdObjects.setStatus("current")


class _CpeCfgMgrClientSerialNumber_Type(OctetString):
    """Custom type cpeCfgMgrClientSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpeCfgMgrClientSerialNumber_Type.__name__ = "OctetString"
_CpeCfgMgrClientSerialNumber_Object = MibScalar
cpeCfgMgrClientSerialNumber = _CpeCfgMgrClientSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1, 1),
    _CpeCfgMgrClientSerialNumber_Type()
)
cpeCfgMgrClientSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientSerialNumber.setStatus("current")


class _CpeCfgMgrClientRegistrationID_Type(OctetString):
    """Custom type cpeCfgMgrClientRegistrationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpeCfgMgrClientRegistrationID_Type.__name__ = "OctetString"
_CpeCfgMgrClientRegistrationID_Object = MibScalar
cpeCfgMgrClientRegistrationID = _CpeCfgMgrClientRegistrationID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1, 2),
    _CpeCfgMgrClientRegistrationID_Type()
)
cpeCfgMgrClientRegistrationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientRegistrationID.setStatus("current")


class _CpeCfgMgrClientFSAN_Type(OctetString):
    """Custom type cpeCfgMgrClientFSAN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpeCfgMgrClientFSAN_Type.__name__ = "OctetString"
_CpeCfgMgrClientFSAN_Object = MibScalar
cpeCfgMgrClientFSAN = _CpeCfgMgrClientFSAN_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1, 3),
    _CpeCfgMgrClientFSAN_Type()
)
cpeCfgMgrClientFSAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientFSAN.setStatus("current")
_CpeCfgMgrClientMacAddress_Type = MacAddress
_CpeCfgMgrClientMacAddress_Object = MibScalar
cpeCfgMgrClientMacAddress = _CpeCfgMgrClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1, 4),
    _CpeCfgMgrClientMacAddress_Type()
)
cpeCfgMgrClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientMacAddress.setStatus("current")


class _CpeCfgMgrClientSysName_Type(OctetString):
    """Custom type cpeCfgMgrClientSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientSysName_Type.__name__ = "OctetString"
_CpeCfgMgrClientSysName_Object = MibScalar
cpeCfgMgrClientSysName = _CpeCfgMgrClientSysName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 1, 5),
    _CpeCfgMgrClientSysName_Type()
)
cpeCfgMgrClientSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientSysName.setStatus("current")
_CpeCfgMgrClientStatusObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientStatusObjects = _CpeCfgMgrClientStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientStatusObjects.setStatus("current")


class _CpeCfgMgrClientState_Type(Integer32):
    """Custom type cpeCfgMgrClientState based on Integer32"""
    defaultValue = 1

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
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("backingUpConfig", 13),
          ("dhcpRenewing", 3),
          ("dhcpRequesting", 2),
          ("dhcpShortLeaseWaiting", 4),
          ("downloadingGenericConfig", 7),
          ("downloadingSoftware", 5),
          ("downloadingSpecificConfig", 8),
          ("downloadingWebUI", 6),
          ("error", 0),
          ("genericOperational", 99),
          ("installingGenericConfig", 11),
          ("installingSoftware", 9),
          ("installingSpecificConfig", 12),
          ("installingWebUI", 10),
          ("operational", 100),
          ("starting", 1))
    )


_CpeCfgMgrClientState_Type.__name__ = "Integer32"
_CpeCfgMgrClientState_Object = MibScalar
cpeCfgMgrClientState = _CpeCfgMgrClientState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 1),
    _CpeCfgMgrClientState_Type()
)
cpeCfgMgrClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientState.setStatus("current")


class _CpeCfgMgrClientErrorDescription_Type(OctetString):
    """Custom type cpeCfgMgrClientErrorDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpeCfgMgrClientErrorDescription_Type.__name__ = "OctetString"
_CpeCfgMgrClientErrorDescription_Object = MibScalar
cpeCfgMgrClientErrorDescription = _CpeCfgMgrClientErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 2),
    _CpeCfgMgrClientErrorDescription_Type()
)
cpeCfgMgrClientErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientErrorDescription.setStatus("current")


class _CpeCfgMgrClientCurrentSwVersion_Type(OctetString):
    """Custom type cpeCfgMgrClientCurrentSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientCurrentSwVersion_Type.__name__ = "OctetString"
_CpeCfgMgrClientCurrentSwVersion_Object = MibScalar
cpeCfgMgrClientCurrentSwVersion = _CpeCfgMgrClientCurrentSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 3),
    _CpeCfgMgrClientCurrentSwVersion_Type()
)
cpeCfgMgrClientCurrentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientCurrentSwVersion.setStatus("current")


class _CpeCfgMgrClientCurrentWebUIVersion_Type(OctetString):
    """Custom type cpeCfgMgrClientCurrentWebUIVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientCurrentWebUIVersion_Type.__name__ = "OctetString"
_CpeCfgMgrClientCurrentWebUIVersion_Object = MibScalar
cpeCfgMgrClientCurrentWebUIVersion = _CpeCfgMgrClientCurrentWebUIVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 4),
    _CpeCfgMgrClientCurrentWebUIVersion_Type()
)
cpeCfgMgrClientCurrentWebUIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientCurrentWebUIVersion.setStatus("current")


class _CpeCfgMgrClientLastInstalledConfigFile_Type(OctetString):
    """Custom type cpeCfgMgrClientLastInstalledConfigFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientLastInstalledConfigFile_Type.__name__ = "OctetString"
_CpeCfgMgrClientLastInstalledConfigFile_Object = MibScalar
cpeCfgMgrClientLastInstalledConfigFile = _CpeCfgMgrClientLastInstalledConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 5),
    _CpeCfgMgrClientLastInstalledConfigFile_Type()
)
cpeCfgMgrClientLastInstalledConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientLastInstalledConfigFile.setStatus("current")


class _CpeCfgMgrClientLastDwnldSrvrBasePath_Type(OctetString):
    """Custom type cpeCfgMgrClientLastDwnldSrvrBasePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientLastDwnldSrvrBasePath_Type.__name__ = "OctetString"
_CpeCfgMgrClientLastDwnldSrvrBasePath_Object = MibScalar
cpeCfgMgrClientLastDwnldSrvrBasePath = _CpeCfgMgrClientLastDwnldSrvrBasePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 6),
    _CpeCfgMgrClientLastDwnldSrvrBasePath_Type()
)
cpeCfgMgrClientLastDwnldSrvrBasePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientLastDwnldSrvrBasePath.setStatus("current")


class _CpeCfgMgrClientLastDwnldSrvrSpecificPath_Type(OctetString):
    """Custom type cpeCfgMgrClientLastDwnldSrvrSpecificPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpeCfgMgrClientLastDwnldSrvrSpecificPath_Type.__name__ = "OctetString"
_CpeCfgMgrClientLastDwnldSrvrSpecificPath_Object = MibScalar
cpeCfgMgrClientLastDwnldSrvrSpecificPath = _CpeCfgMgrClientLastDwnldSrvrSpecificPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 2, 7),
    _CpeCfgMgrClientLastDwnldSrvrSpecificPath_Type()
)
cpeCfgMgrClientLastDwnldSrvrSpecificPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeCfgMgrClientLastDwnldSrvrSpecificPath.setStatus("current")
_CpeCfgMgrClientUpdateObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientUpdateObjects = _CpeCfgMgrClientUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientUpdateObjects.setStatus("current")


class _CpeCfgMgrClientRequiredUpdates_Type(Bits):
    """Custom type cpeCfgMgrClientRequiredUpdates based on Bits"""
    namedValues = NamedValues(
        *(("backup", 3),
          ("config", 2),
          ("software", 0),
          ("webUI", 1))
    )

_CpeCfgMgrClientRequiredUpdates_Type.__name__ = "Bits"
_CpeCfgMgrClientRequiredUpdates_Object = MibScalar
cpeCfgMgrClientRequiredUpdates = _CpeCfgMgrClientRequiredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 1),
    _CpeCfgMgrClientRequiredUpdates_Type()
)
cpeCfgMgrClientRequiredUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientRequiredUpdates.setStatus("current")


class _CpeCfgMgrClientReceivedSwFilename_Type(OctetString):
    """Custom type cpeCfgMgrClientReceivedSwFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientReceivedSwFilename_Type.__name__ = "OctetString"
_CpeCfgMgrClientReceivedSwFilename_Object = MibScalar
cpeCfgMgrClientReceivedSwFilename = _CpeCfgMgrClientReceivedSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 2),
    _CpeCfgMgrClientReceivedSwFilename_Type()
)
cpeCfgMgrClientReceivedSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientReceivedSwFilename.setStatus("current")


class _CpeCfgMgrClientReceivedWebUIFilename_Type(OctetString):
    """Custom type cpeCfgMgrClientReceivedWebUIFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientReceivedWebUIFilename_Type.__name__ = "OctetString"
_CpeCfgMgrClientReceivedWebUIFilename_Object = MibScalar
cpeCfgMgrClientReceivedWebUIFilename = _CpeCfgMgrClientReceivedWebUIFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 3),
    _CpeCfgMgrClientReceivedWebUIFilename_Type()
)
cpeCfgMgrClientReceivedWebUIFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientReceivedWebUIFilename.setStatus("current")


class _CpeCfgMgrClientReceivedGenericCfgFilename_Type(OctetString):
    """Custom type cpeCfgMgrClientReceivedGenericCfgFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientReceivedGenericCfgFilename_Type.__name__ = "OctetString"
_CpeCfgMgrClientReceivedGenericCfgFilename_Object = MibScalar
cpeCfgMgrClientReceivedGenericCfgFilename = _CpeCfgMgrClientReceivedGenericCfgFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 4),
    _CpeCfgMgrClientReceivedGenericCfgFilename_Type()
)
cpeCfgMgrClientReceivedGenericCfgFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientReceivedGenericCfgFilename.setStatus("current")


class _CpeCfgMgrClientReceivedSpecificCfgFilename_Type(OctetString):
    """Custom type cpeCfgMgrClientReceivedSpecificCfgFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientReceivedSpecificCfgFilename_Type.__name__ = "OctetString"
_CpeCfgMgrClientReceivedSpecificCfgFilename_Object = MibScalar
cpeCfgMgrClientReceivedSpecificCfgFilename = _CpeCfgMgrClientReceivedSpecificCfgFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 5),
    _CpeCfgMgrClientReceivedSpecificCfgFilename_Type()
)
cpeCfgMgrClientReceivedSpecificCfgFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientReceivedSpecificCfgFilename.setStatus("current")


class _CpeCfgMgrClientForceUpdate_Type(Integer32):
    """Custom type cpeCfgMgrClientForceUpdate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renewDhcp", 1),
          ("updateConfig", 2))
    )


_CpeCfgMgrClientForceUpdate_Type.__name__ = "Integer32"
_CpeCfgMgrClientForceUpdate_Object = MibScalar
cpeCfgMgrClientForceUpdate = _CpeCfgMgrClientForceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 3, 6),
    _CpeCfgMgrClientForceUpdate_Type()
)
cpeCfgMgrClientForceUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientForceUpdate.setStatus("current")
_CpeCfgMgrClientDownloadServerObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientDownloadServerObjects = _CpeCfgMgrClientDownloadServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientDownloadServerObjects.setStatus("current")
_CpeCfgMgrClientDwnldSrvrIP_Type = IpAddress
_CpeCfgMgrClientDwnldSrvrIP_Object = MibScalar
cpeCfgMgrClientDwnldSrvrIP = _CpeCfgMgrClientDwnldSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 1),
    _CpeCfgMgrClientDwnldSrvrIP_Type()
)
cpeCfgMgrClientDwnldSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSrvrIP.setStatus("current")


class _CpeCfgMgrClientDwnldSrvrUsername_Type(OctetString):
    """Custom type cpeCfgMgrClientDwnldSrvrUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpeCfgMgrClientDwnldSrvrUsername_Type.__name__ = "OctetString"
_CpeCfgMgrClientDwnldSrvrUsername_Object = MibScalar
cpeCfgMgrClientDwnldSrvrUsername = _CpeCfgMgrClientDwnldSrvrUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 2),
    _CpeCfgMgrClientDwnldSrvrUsername_Type()
)
cpeCfgMgrClientDwnldSrvrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSrvrUsername.setStatus("current")


class _CpeCfgMgrClientDwnldSrvrPassword_Type(OctetString):
    """Custom type cpeCfgMgrClientDwnldSrvrPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpeCfgMgrClientDwnldSrvrPassword_Type.__name__ = "OctetString"
_CpeCfgMgrClientDwnldSrvrPassword_Object = MibScalar
cpeCfgMgrClientDwnldSrvrPassword = _CpeCfgMgrClientDwnldSrvrPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 3),
    _CpeCfgMgrClientDwnldSrvrPassword_Type()
)
cpeCfgMgrClientDwnldSrvrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSrvrPassword.setStatus("current")


class _CpeCfgMgrClientDwnldSrvrSecureMode_Type(Integer32):
    """Custom type cpeCfgMgrClientDwnldSrvrSecureMode based on Integer32"""
    defaultValue = 3

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
          ("noPreference", 3))
    )


_CpeCfgMgrClientDwnldSrvrSecureMode_Type.__name__ = "Integer32"
_CpeCfgMgrClientDwnldSrvrSecureMode_Object = MibScalar
cpeCfgMgrClientDwnldSrvrSecureMode = _CpeCfgMgrClientDwnldSrvrSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 4),
    _CpeCfgMgrClientDwnldSrvrSecureMode_Type()
)
cpeCfgMgrClientDwnldSrvrSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSrvrSecureMode.setStatus("current")


class _CpeCfgMgrClientDwnldSrvrBasePath_Type(OctetString):
    """Custom type cpeCfgMgrClientDwnldSrvrBasePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrClientDwnldSrvrBasePath_Type.__name__ = "OctetString"
_CpeCfgMgrClientDwnldSrvrBasePath_Object = MibScalar
cpeCfgMgrClientDwnldSrvrBasePath = _CpeCfgMgrClientDwnldSrvrBasePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 5),
    _CpeCfgMgrClientDwnldSrvrBasePath_Type()
)
cpeCfgMgrClientDwnldSrvrBasePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSrvrBasePath.setStatus("current")


class _CpeCfgMgrClientDwnldSpecificPath_Type(OctetString):
    """Custom type cpeCfgMgrClientDwnldSpecificPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpeCfgMgrClientDwnldSpecificPath_Type.__name__ = "OctetString"
_CpeCfgMgrClientDwnldSpecificPath_Object = MibScalar
cpeCfgMgrClientDwnldSpecificPath = _CpeCfgMgrClientDwnldSpecificPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 4, 6),
    _CpeCfgMgrClientDwnldSpecificPath_Type()
)
cpeCfgMgrClientDwnldSpecificPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrClientDwnldSpecificPath.setStatus("current")
_CpeCfgMgrClientCoObjects_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientCoObjects = _CpeCfgMgrClientCoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientCoObjects.setStatus("current")
_CpeCfgMgrPublicIPAddress_Type = IpAddress
_CpeCfgMgrPublicIPAddress_Object = MibScalar
cpeCfgMgrPublicIPAddress = _CpeCfgMgrPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 1),
    _CpeCfgMgrPublicIPAddress_Type()
)
cpeCfgMgrPublicIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrPublicIPAddress.setStatus("current")


class _CpeCfgMgrBaseProtocolPort_Type(Integer32):
    """Custom type cpeCfgMgrBaseProtocolPort based on Integer32"""
    defaultValue = 0


_CpeCfgMgrBaseProtocolPort_Object = MibScalar
cpeCfgMgrBaseProtocolPort = _CpeCfgMgrBaseProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 2),
    _CpeCfgMgrBaseProtocolPort_Type()
)
cpeCfgMgrBaseProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrBaseProtocolPort.setStatus("current")


class _CpeCfgMgrSlot_Type(Integer32):
    """Custom type cpeCfgMgrSlot based on Integer32"""
    defaultValue = 0


_CpeCfgMgrSlot_Object = MibScalar
cpeCfgMgrSlot = _CpeCfgMgrSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 3),
    _CpeCfgMgrSlot_Type()
)
cpeCfgMgrSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrSlot.setStatus("current")


class _CpeCfgMgrPort_Type(Integer32):
    """Custom type cpeCfgMgrPort based on Integer32"""
    defaultValue = 0


_CpeCfgMgrPort_Object = MibScalar
cpeCfgMgrPort = _CpeCfgMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 4),
    _CpeCfgMgrPort_Type()
)
cpeCfgMgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrPort.setStatus("current")


class _CpeCfgMgrSubport_Type(Integer32):
    """Custom type cpeCfgMgrSubport based on Integer32"""
    defaultValue = 0


_CpeCfgMgrSubport_Object = MibScalar
cpeCfgMgrSubport = _CpeCfgMgrSubport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 5),
    _CpeCfgMgrSubport_Type()
)
cpeCfgMgrSubport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrSubport.setStatus("current")


class _CpeCfgMgrInterfaceName_Type(OctetString):
    """Custom type cpeCfgMgrInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpeCfgMgrInterfaceName_Type.__name__ = "OctetString"
_CpeCfgMgrInterfaceName_Object = MibScalar
cpeCfgMgrInterfaceName = _CpeCfgMgrInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 1, 5, 6),
    _CpeCfgMgrInterfaceName_Type()
)
cpeCfgMgrInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeCfgMgrInterfaceName.setStatus("current")
_CpeCfgMgrClientConformance_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientConformance = _CpeCfgMgrClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientConformance.setStatus("current")
_CpeCfgMgrClientGroups_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientGroups = _CpeCfgMgrClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientGroups.setStatus("current")
_CpeCfgMgrClientCompliances_ObjectIdentity = ObjectIdentity
cpeCfgMgrClientCompliances = _CpeCfgMgrClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientCompliances.setStatus("current")

# Managed Objects groups

cpeMgrGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 2, 1, 1)
)
cpeMgrGlobalGroup.setObjects(
      *(("CPE-MANAGER", "cpeMgrLocalVlanId"),
        ("CPE-MANAGER", "cpeMgrLocalSlanId"),
        ("CPE-MANAGER", "cpeCfgMgrConcurrentUpdateLimit"))
)
if mibBuilder.loadTexts:
    cpeMgrGlobalGroup.setStatus("current")

cpeConfigMgrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 1, 1)
)
cpeConfigMgrObjectGroup.setObjects(
      *(("CPE-MANAGER", "cpeConfigMgrRowStatus"),
        ("CPE-MANAGER", "cpeConfigMgrIndex"),
        ("CPE-MANAGER", "cpeConfigMgrName"),
        ("CPE-MANAGER", "cpeConfigMgrGroup"),
        ("CPE-MANAGER", "managedCpeType"),
        ("CPE-MANAGER", "requiredCpeSoftwareVersion"),
        ("CPE-MANAGER", "requiredCpeSoftwareFilename"),
        ("CPE-MANAGER", "requiredCpeWebUIVersion"),
        ("CPE-MANAGER", "requiredCpeWebUIFilename"),
        ("CPE-MANAGER", "requiredCpeGenericConfigFile"),
        ("CPE-MANAGER", "cpeLeaseTimeUpdate"),
        ("CPE-MANAGER", "cpeLeaseTimeOperational"),
        ("CPE-MANAGER", "cpeConfigMgrDownloadBasePath"),
        ("CPE-MANAGER", "cpeConfigMgrDownloadSecureMode"),
        ("CPE-MANAGER", "cpeConfigVarsIndex"),
        ("CPE-MANAGER", "cpeConfigScriptIndex"),
        ("CPE-MANAGER", "cpeConfigMgrTrapsEnabled"),
        ("CPE-MANAGER", "cpeConfigMgrDwnldSrvrToUsed"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrObjectGroup.setStatus("current")

cpeConfigMgrDownloadServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 1, 2)
)
cpeConfigMgrDownloadServerGroup.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrDwnldSrvrRowStatus"),
        ("CPE-MANAGER", "cpeCfgMgrDwnldSrvrIndex"),
        ("CPE-MANAGER", "cpeCfgMgrDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrDwnldSrvrPassword"),
        ("CPE-MANAGER", "cpeCfgMgrDwnldSrvrDefault"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrDownloadServerGroup.setStatus("current")

cpeConfigMgrMemberObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 1, 3)
)
cpeConfigMgrMemberObjectGroup.setObjects(
      *(("CPE-MANAGER", "cpeConfigMgrMemberRowStatus"),
        ("CPE-MANAGER", "cpeConfigMgrGroupMembership"),
        ("CPE-MANAGER", "cpeSpecificConfigFile"),
        ("CPE-MANAGER", "cpeSpecificDownloadPath"),
        ("CPE-MANAGER", "cpeConfigMgrMemberTrapsEnabled"),
        ("CPE-MANAGER", "cpeConfigMgrMemberStatus"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "reportedCpeType"),
        ("CPE-MANAGER", "reportedCpeSoftwareVersion"),
        ("CPE-MANAGER", "reportedCpeWebUIVersion"),
        ("CPE-MANAGER", "reportedCpeConfigFilename"),
        ("CPE-MANAGER", "reportedCpeSerialNumber"),
        ("CPE-MANAGER", "reportedCpeRegistrationID"),
        ("CPE-MANAGER", "reportedCpeFSAN"),
        ("CPE-MANAGER", "reportedCpeMacAddress"),
        ("CPE-MANAGER", "reportedDwnldSrvrBasePath"),
        ("CPE-MANAGER", "reportedDwnldSrvrSpecificPath"),
        ("CPE-MANAGER", "reportedCpeState"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrMemberObjectGroup.setStatus("current")

cpeCfgMgrClientObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2, 1, 1)
)
cpeCfgMgrClientObjectGroup.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientFSAN"),
        ("CPE-MANAGER", "cpeCfgMgrClientMacAddress"),
        ("CPE-MANAGER", "cpeCfgMgrClientSysName"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSwFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedWebUIFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedGenericCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSpecificCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientForceUpdate"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrPassword"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrPublicIPAddress"),
        ("CPE-MANAGER", "cpeCfgMgrBaseProtocolPort"),
        ("CPE-MANAGER", "cpeCfgMgrSlot"),
        ("CPE-MANAGER", "cpeCfgMgrPort"),
        ("CPE-MANAGER", "cpeCfgMgrSubport"),
        ("CPE-MANAGER", "cpeCfgMgrClientCurrentSwVersion"),
        ("CPE-MANAGER", "cpeCfgMgrClientCurrentWebUIVersion"),
        ("CPE-MANAGER", "cpeCfgMgrClientLastInstalledConfigFile"),
        ("CPE-MANAGER", "cpeCfgMgrClientLastDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientLastDwnldSrvrSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrInterfaceName"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientObjectGroup.setStatus("current")


# Notification objects

cpeConfigMgrClientOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 1)
)
cpeConfigMgrClientOperational.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "reportedCpeSerialNumber"),
        ("CPE-MANAGER", "reportedCpeRegistrationID"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrClientOperational.setStatus(
        "current"
    )

cpeConfigMgrClientDysfunctional = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 2)
)
cpeConfigMgrClientDysfunctional.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "cpeConfigMgrMemberStatus"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrClientDysfunctional.setStatus(
        "current"
    )

cpeConfigMgrMismatchType = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 3)
)
cpeConfigMgrMismatchType.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrGroupMembership"),
        ("CPE-MANAGER", "reportedCpeType"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrMismatchType.setStatus(
        "current"
    )

cpeConfigMgrMismatchSoftwareVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 4)
)
cpeConfigMgrMismatchSoftwareVersion.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "requiredCpeSoftwareVersion"),
        ("CPE-MANAGER", "reportedCpeSoftwareVersion"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrMismatchSoftwareVersion.setStatus(
        "current"
    )

cpeConfigMgrMismatchWebUIVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 5)
)
cpeConfigMgrMismatchWebUIVersion.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "requiredCpeWebUIVersion"),
        ("CPE-MANAGER", "reportedCpeWebUIVersion"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrMismatchWebUIVersion.setStatus(
        "current"
    )

cpeConfigMgrMismatchConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 6)
)
cpeConfigMgrMismatchConfigFile.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "reportedCpeConfigFilename"),
        ("CPE-MANAGER", "reportedDwnldSrvrBasePath"),
        ("CPE-MANAGER", "reportedDwnldSrvrSpecificPath"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrMismatchConfigFile.setStatus(
        "current"
    )

cpeConfigMgrUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 0, 7)
)
cpeConfigMgrUpdateError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPE-MANAGER", "cpeConfigMgrUsed"),
        ("CPE-MANAGER", "cpeConfigMgrMemberStatus"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrUpdateError.setStatus(
        "current"
    )

cpeCfgMgrClientSoftwareDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 1)
)
cpeCfgMgrClientSoftwareDownloadFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSwFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientSoftwareDownloadFailed.setStatus(
        "current"
    )

cpeCfgMgrClientSoftwareInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 2)
)
cpeCfgMgrClientSoftwareInstallFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSwFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientSoftwareInstallFailed.setStatus(
        "current"
    )

cpeCfgMgrClientWebUIDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 3)
)
cpeCfgMgrClientWebUIDownloadFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedWebUIFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientWebUIDownloadFailed.setStatus(
        "current"
    )

cpeCfgMgrClientWebUIInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 4)
)
cpeCfgMgrClientWebUIInstallFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedWebUIFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientWebUIInstallFailed.setStatus(
        "current"
    )

cpeCfgMgrClientConfigDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 5)
)
cpeCfgMgrClientConfigDownloadFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedGenericCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSpecificCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientConfigDownloadFailed.setStatus(
        "current"
    )

cpeCfgMgrClientConfigUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 6)
)
cpeCfgMgrClientConfigUpdateFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedGenericCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSpecificCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientConfigUpdateFailed.setStatus(
        "current"
    )

cpeCfgMgrClientConfigBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 7)
)
cpeCfgMgrClientConfigBackupFailed.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientErrorDescription"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSpecificCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientConfigBackupFailed.setStatus(
        "current"
    )

cpeCfgMgrClientLevelReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 8)
)
cpeCfgMgrClientLevelReady.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientMacAddress"),
        ("CPE-MANAGER", "cpeCfgMgrClientFSAN"),
        ("CPE-MANAGER", "cpeCfgMgrPublicIPAddress"),
        ("CPE-MANAGER", "cpeCfgMgrBaseProtocolPort"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientLevelReady.setStatus(
        "current"
    )

cpeCfgMgrClientConfigBackupDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 0, 9)
)
cpeCfgMgrClientConfigBackupDone.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSerialNumber"),
        ("CPE-MANAGER", "cpeCfgMgrClientRegistrationID"),
        ("CPE-MANAGER", "cpeCfgMgrClientState"),
        ("CPE-MANAGER", "cpeCfgMgrClientRequiredUpdates"),
        ("CPE-MANAGER", "cpeCfgMgrClientReceivedSpecificCfgFilename"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrBasePath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSpecificPath"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrIP"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrUsername"),
        ("CPE-MANAGER", "cpeCfgMgrClientDwnldSrvrSecureMode"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientConfigBackupDone.setStatus(
        "current"
    )


# Notifications groups

cpeConfigMgrNotificationsObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 1, 4)
)
cpeConfigMgrNotificationsObjectGroup.setObjects(
      *(("CPE-MANAGER", "cpeConfigMgrClientOperational"),
        ("CPE-MANAGER", "cpeConfigMgrClientDysfunctional"),
        ("CPE-MANAGER", "cpeConfigMgrMismatchType"),
        ("CPE-MANAGER", "cpeConfigMgrMismatchSoftwareVersion"),
        ("CPE-MANAGER", "cpeConfigMgrMismatchWebUIVersion"),
        ("CPE-MANAGER", "cpeConfigMgrMismatchConfigFile"),
        ("CPE-MANAGER", "cpeConfigMgrUpdateError"))
)
if mibBuilder.loadTexts:
    cpeConfigMgrNotificationsObjectGroup.setStatus(
        "current"
    )

cpeCfgMgrClientNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2, 1, 2)
)
cpeCfgMgrClientNotificationsGroup.setObjects(
      *(("CPE-MANAGER", "cpeCfgMgrClientSoftwareDownloadFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientSoftwareInstallFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientWebUIDownloadFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientWebUIInstallFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientConfigDownloadFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientConfigUpdateFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientConfigBackupFailed"),
        ("CPE-MANAGER", "cpeCfgMgrClientLevelReady"),
        ("CPE-MANAGER", "cpeCfgMgrClientConfigBackupDone"))
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpeMgrGlobalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpeMgrGlobalCompliance.setStatus(
        "current"
    )

cpeConfigMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpeConfigMgrCompliance.setStatus(
        "current"
    )

cpeCfgMgrClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpeCfgMgrClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPE-MANAGER",
    **{"cpeMgrModule": cpeMgrModule,
       "cpeMgrGlobal": cpeMgrGlobal,
       "cpeMgrGlobalObjects": cpeMgrGlobalObjects,
       "cpeMgrLocalVlanId": cpeMgrLocalVlanId,
       "cpeMgrLocalSlanId": cpeMgrLocalSlanId,
       "cpeCfgMgrConcurrentUpdateLimit": cpeCfgMgrConcurrentUpdateLimit,
       "cpeMgrGlobalConformance": cpeMgrGlobalConformance,
       "cpeMgrGlobalGroups": cpeMgrGlobalGroups,
       "cpeMgrGlobalGroup": cpeMgrGlobalGroup,
       "cpeMgrGlobalCompliances": cpeMgrGlobalCompliances,
       "cpeMgrGlobalCompliance": cpeMgrGlobalCompliance,
       "cpeConfigMgr": cpeConfigMgr,
       "cpeConfigMgrNotifications": cpeConfigMgrNotifications,
       "cpeConfigMgrClientOperational": cpeConfigMgrClientOperational,
       "cpeConfigMgrClientDysfunctional": cpeConfigMgrClientDysfunctional,
       "cpeConfigMgrMismatchType": cpeConfigMgrMismatchType,
       "cpeConfigMgrMismatchSoftwareVersion": cpeConfigMgrMismatchSoftwareVersion,
       "cpeConfigMgrMismatchWebUIVersion": cpeConfigMgrMismatchWebUIVersion,
       "cpeConfigMgrMismatchConfigFile": cpeConfigMgrMismatchConfigFile,
       "cpeConfigMgrUpdateError": cpeConfigMgrUpdateError,
       "cpeConfigMgrObjects": cpeConfigMgrObjects,
       "cpeConfigMgrTable": cpeConfigMgrTable,
       "cpeConfigMgrEntry": cpeConfigMgrEntry,
       "cpeConfigMgrRowStatus": cpeConfigMgrRowStatus,
       "cpeConfigMgrIndex": cpeConfigMgrIndex,
       "cpeConfigMgrName": cpeConfigMgrName,
       "cpeConfigMgrGroup": cpeConfigMgrGroup,
       "managedCpeType": managedCpeType,
       "requiredCpeSoftwareVersion": requiredCpeSoftwareVersion,
       "requiredCpeSoftwareFilename": requiredCpeSoftwareFilename,
       "requiredCpeWebUIVersion": requiredCpeWebUIVersion,
       "requiredCpeWebUIFilename": requiredCpeWebUIFilename,
       "requiredCpeGenericConfigFile": requiredCpeGenericConfigFile,
       "cpeLeaseTimeUpdate": cpeLeaseTimeUpdate,
       "cpeLeaseTimeOperational": cpeLeaseTimeOperational,
       "cpeConfigMgrDwnldSrvrToUsed": cpeConfigMgrDwnldSrvrToUsed,
       "cpeConfigMgrDownloadBasePath": cpeConfigMgrDownloadBasePath,
       "cpeConfigMgrDownloadSecureMode": cpeConfigMgrDownloadSecureMode,
       "cpeConfigMgrTrapsEnabled": cpeConfigMgrTrapsEnabled,
       "cpeConfigScriptIndex": cpeConfigScriptIndex,
       "cpeConfigVarsIndex": cpeConfigVarsIndex,
       "cpeConfigMgrDownloadServerTable": cpeConfigMgrDownloadServerTable,
       "cpeConfigMgrDownloadServerEntry": cpeConfigMgrDownloadServerEntry,
       "cpeCfgMgrDwnldSrvrRowStatus": cpeCfgMgrDwnldSrvrRowStatus,
       "cpeCfgMgrDwnldSrvrIndex": cpeCfgMgrDwnldSrvrIndex,
       "cpeCfgMgrDwnldSrvrIP": cpeCfgMgrDwnldSrvrIP,
       "cpeCfgMgrDwnldSrvrUsername": cpeCfgMgrDwnldSrvrUsername,
       "cpeCfgMgrDwnldSrvrPassword": cpeCfgMgrDwnldSrvrPassword,
       "cpeCfgMgrDwnldSrvrDefault": cpeCfgMgrDwnldSrvrDefault,
       "cpeConfigMgrMemberTable": cpeConfigMgrMemberTable,
       "cpeConfigMgrMemberEntry": cpeConfigMgrMemberEntry,
       "cpeConfigMgrMemberRowStatus": cpeConfigMgrMemberRowStatus,
       "cpeConfigMgrGroupMembership": cpeConfigMgrGroupMembership,
       "cpeSpecificConfigFile": cpeSpecificConfigFile,
       "cpeSpecificDownloadPath": cpeSpecificDownloadPath,
       "cpeConfigMgrMemberTrapsEnabled": cpeConfigMgrMemberTrapsEnabled,
       "cpeConfigMgrMemberStatusTable": cpeConfigMgrMemberStatusTable,
       "cpeConfigMgrMemberStatusEntry": cpeConfigMgrMemberStatusEntry,
       "cpeConfigMgrMemberStatus": cpeConfigMgrMemberStatus,
       "cpeConfigMgrUsed": cpeConfigMgrUsed,
       "reportedCpeType": reportedCpeType,
       "reportedCpeSoftwareVersion": reportedCpeSoftwareVersion,
       "reportedCpeWebUIVersion": reportedCpeWebUIVersion,
       "reportedCpeConfigFilename": reportedCpeConfigFilename,
       "reportedCpeSerialNumber": reportedCpeSerialNumber,
       "reportedCpeRegistrationID": reportedCpeRegistrationID,
       "reportedCpeFSAN": reportedCpeFSAN,
       "reportedCpeMacAddress": reportedCpeMacAddress,
       "reportedDwnldSrvrBasePath": reportedDwnldSrvrBasePath,
       "reportedDwnldSrvrSpecificPath": reportedDwnldSrvrSpecificPath,
       "reportedCpeState": reportedCpeState,
       "cpeConfigMgrConformance": cpeConfigMgrConformance,
       "cpeConfigMgrGroups": cpeConfigMgrGroups,
       "cpeConfigMgrObjectGroup": cpeConfigMgrObjectGroup,
       "cpeConfigMgrDownloadServerGroup": cpeConfigMgrDownloadServerGroup,
       "cpeConfigMgrMemberObjectGroup": cpeConfigMgrMemberObjectGroup,
       "cpeConfigMgrNotificationsObjectGroup": cpeConfigMgrNotificationsObjectGroup,
       "cpeConfigMgrCompliances": cpeConfigMgrCompliances,
       "cpeConfigMgrCompliance": cpeConfigMgrCompliance,
       "cpeConfigMgrClient": cpeConfigMgrClient,
       "cpeCfgMgrClientNotifications": cpeCfgMgrClientNotifications,
       "cpeCfgMgrClientSoftwareDownloadFailed": cpeCfgMgrClientSoftwareDownloadFailed,
       "cpeCfgMgrClientSoftwareInstallFailed": cpeCfgMgrClientSoftwareInstallFailed,
       "cpeCfgMgrClientWebUIDownloadFailed": cpeCfgMgrClientWebUIDownloadFailed,
       "cpeCfgMgrClientWebUIInstallFailed": cpeCfgMgrClientWebUIInstallFailed,
       "cpeCfgMgrClientConfigDownloadFailed": cpeCfgMgrClientConfigDownloadFailed,
       "cpeCfgMgrClientConfigUpdateFailed": cpeCfgMgrClientConfigUpdateFailed,
       "cpeCfgMgrClientConfigBackupFailed": cpeCfgMgrClientConfigBackupFailed,
       "cpeCfgMgrClientLevelReady": cpeCfgMgrClientLevelReady,
       "cpeCfgMgrClientConfigBackupDone": cpeCfgMgrClientConfigBackupDone,
       "cpeCfgMgrClientObjects": cpeCfgMgrClientObjects,
       "cpeCfgMgrClientIdObjects": cpeCfgMgrClientIdObjects,
       "cpeCfgMgrClientSerialNumber": cpeCfgMgrClientSerialNumber,
       "cpeCfgMgrClientRegistrationID": cpeCfgMgrClientRegistrationID,
       "cpeCfgMgrClientFSAN": cpeCfgMgrClientFSAN,
       "cpeCfgMgrClientMacAddress": cpeCfgMgrClientMacAddress,
       "cpeCfgMgrClientSysName": cpeCfgMgrClientSysName,
       "cpeCfgMgrClientStatusObjects": cpeCfgMgrClientStatusObjects,
       "cpeCfgMgrClientState": cpeCfgMgrClientState,
       "cpeCfgMgrClientErrorDescription": cpeCfgMgrClientErrorDescription,
       "cpeCfgMgrClientCurrentSwVersion": cpeCfgMgrClientCurrentSwVersion,
       "cpeCfgMgrClientCurrentWebUIVersion": cpeCfgMgrClientCurrentWebUIVersion,
       "cpeCfgMgrClientLastInstalledConfigFile": cpeCfgMgrClientLastInstalledConfigFile,
       "cpeCfgMgrClientLastDwnldSrvrBasePath": cpeCfgMgrClientLastDwnldSrvrBasePath,
       "cpeCfgMgrClientLastDwnldSrvrSpecificPath": cpeCfgMgrClientLastDwnldSrvrSpecificPath,
       "cpeCfgMgrClientUpdateObjects": cpeCfgMgrClientUpdateObjects,
       "cpeCfgMgrClientRequiredUpdates": cpeCfgMgrClientRequiredUpdates,
       "cpeCfgMgrClientReceivedSwFilename": cpeCfgMgrClientReceivedSwFilename,
       "cpeCfgMgrClientReceivedWebUIFilename": cpeCfgMgrClientReceivedWebUIFilename,
       "cpeCfgMgrClientReceivedGenericCfgFilename": cpeCfgMgrClientReceivedGenericCfgFilename,
       "cpeCfgMgrClientReceivedSpecificCfgFilename": cpeCfgMgrClientReceivedSpecificCfgFilename,
       "cpeCfgMgrClientForceUpdate": cpeCfgMgrClientForceUpdate,
       "cpeCfgMgrClientDownloadServerObjects": cpeCfgMgrClientDownloadServerObjects,
       "cpeCfgMgrClientDwnldSrvrIP": cpeCfgMgrClientDwnldSrvrIP,
       "cpeCfgMgrClientDwnldSrvrUsername": cpeCfgMgrClientDwnldSrvrUsername,
       "cpeCfgMgrClientDwnldSrvrPassword": cpeCfgMgrClientDwnldSrvrPassword,
       "cpeCfgMgrClientDwnldSrvrSecureMode": cpeCfgMgrClientDwnldSrvrSecureMode,
       "cpeCfgMgrClientDwnldSrvrBasePath": cpeCfgMgrClientDwnldSrvrBasePath,
       "cpeCfgMgrClientDwnldSpecificPath": cpeCfgMgrClientDwnldSpecificPath,
       "cpeCfgMgrClientCoObjects": cpeCfgMgrClientCoObjects,
       "cpeCfgMgrPublicIPAddress": cpeCfgMgrPublicIPAddress,
       "cpeCfgMgrBaseProtocolPort": cpeCfgMgrBaseProtocolPort,
       "cpeCfgMgrSlot": cpeCfgMgrSlot,
       "cpeCfgMgrPort": cpeCfgMgrPort,
       "cpeCfgMgrSubport": cpeCfgMgrSubport,
       "cpeCfgMgrInterfaceName": cpeCfgMgrInterfaceName,
       "cpeCfgMgrClientConformance": cpeCfgMgrClientConformance,
       "cpeCfgMgrClientGroups": cpeCfgMgrClientGroups,
       "cpeCfgMgrClientObjectGroup": cpeCfgMgrClientObjectGroup,
       "cpeCfgMgrClientNotificationsGroup": cpeCfgMgrClientNotificationsGroup,
       "cpeCfgMgrClientCompliances": cpeCfgMgrClientCompliances,
       "cpeCfgMgrClientCompliance": cpeCfgMgrClientCompliance}
)
