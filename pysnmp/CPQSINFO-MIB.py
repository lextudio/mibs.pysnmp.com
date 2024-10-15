# SNMP MIB module (CPQSINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:24 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

_CpqSystemInfo_ObjectIdentity = ObjectIdentity
cpqSystemInfo = _CpqSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2)
)
_CpqSiMibRev_ObjectIdentity = ObjectIdentity
cpqSiMibRev = _CpqSiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 1)
)


class _CpqSiMibRevMajor_Type(Integer32):
    """Custom type cpqSiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSiMibRevMajor_Type.__name__ = "Integer32"
_CpqSiMibRevMajor_Object = MibScalar
cpqSiMibRevMajor = _CpqSiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 1, 1),
    _CpqSiMibRevMajor_Type()
)
cpqSiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMibRevMajor.setStatus("mandatory")


class _CpqSiMibRevMinor_Type(Integer32):
    """Custom type cpqSiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMibRevMinor_Type.__name__ = "Integer32"
_CpqSiMibRevMinor_Object = MibScalar
cpqSiMibRevMinor = _CpqSiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 1, 2),
    _CpqSiMibRevMinor_Type()
)
cpqSiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMibRevMinor.setStatus("mandatory")


class _CpqSiMibCondition_Type(Integer32):
    """Custom type cpqSiMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMibCondition_Type.__name__ = "Integer32"
_CpqSiMibCondition_Object = MibScalar
cpqSiMibCondition = _CpqSiMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 1, 3),
    _CpqSiMibCondition_Type()
)
cpqSiMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMibCondition.setStatus("mandatory")
_CpqSiComponent_ObjectIdentity = ObjectIdentity
cpqSiComponent = _CpqSiComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2)
)
_CpqSiInterface_ObjectIdentity = ObjectIdentity
cpqSiInterface = _CpqSiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1)
)
_CpqSiOsCommon_ObjectIdentity = ObjectIdentity
cpqSiOsCommon = _CpqSiOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4)
)


class _CpqSiOsCommonPollFreq_Type(Integer32):
    """Custom type cpqSiOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqSiOsCommonPollFreq_Object = MibScalar
cpqSiOsCommonPollFreq = _CpqSiOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 1),
    _CpqSiOsCommonPollFreq_Type()
)
cpqSiOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiOsCommonPollFreq.setStatus("mandatory")
_CpqSiOsCommonModuleTable_Object = MibTable
cpqSiOsCommonModuleTable = _CpqSiOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleTable.setStatus("deprecated")
_CpqSiOsCommonModuleEntry_Object = MibTableRow
cpqSiOsCommonModuleEntry = _CpqSiOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1)
)
cpqSiOsCommonModuleEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleEntry.setStatus("deprecated")


class _CpqSiOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqSiOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqSiOsCommonModuleIndex_Object = MibTableColumn
cpqSiOsCommonModuleIndex = _CpqSiOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1, 1),
    _CpqSiOsCommonModuleIndex_Type()
)
cpqSiOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleIndex.setStatus("deprecated")


class _CpqSiOsCommonModuleName_Type(DisplayString):
    """Custom type cpqSiOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqSiOsCommonModuleName_Object = MibTableColumn
cpqSiOsCommonModuleName = _CpqSiOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1, 2),
    _CpqSiOsCommonModuleName_Type()
)
cpqSiOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleName.setStatus("deprecated")


class _CpqSiOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqSiOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSiOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqSiOsCommonModuleVersion_Object = MibTableColumn
cpqSiOsCommonModuleVersion = _CpqSiOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1, 3),
    _CpqSiOsCommonModuleVersion_Type()
)
cpqSiOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleVersion.setStatus("deprecated")


class _CpqSiOsCommonModuleDate_Type(OctetString):
    """Custom type cpqSiOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqSiOsCommonModuleDate_Object = MibTableColumn
cpqSiOsCommonModuleDate = _CpqSiOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1, 4),
    _CpqSiOsCommonModuleDate_Type()
)
cpqSiOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOsCommonModuleDate.setStatus("deprecated")


class _CpqSiOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqSiOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqSiOsCommonModulePurpose_Object = MibTableColumn
cpqSiOsCommonModulePurpose = _CpqSiOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 1, 4, 2, 1, 5),
    _CpqSiOsCommonModulePurpose_Type()
)
cpqSiOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOsCommonModulePurpose.setStatus("deprecated")
_CpqSiAsset_ObjectIdentity = ObjectIdentity
cpqSiAsset = _CpqSiAsset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2)
)


class _CpqSiSysSerialNum_Type(DisplayString):
    """Custom type cpqSiSysSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysSerialNum_Type.__name__ = "DisplayString"
_CpqSiSysSerialNum_Object = MibScalar
cpqSiSysSerialNum = _CpqSiSysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 1),
    _CpqSiSysSerialNum_Type()
)
cpqSiSysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysSerialNum.setStatus("mandatory")


class _CpqSiFormFactor_Type(Integer32):
    """Custom type cpqSiFormFactor based on Integer32"""
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
        *(("desktop", 4),
          ("laptop", 3),
          ("mini-tower", 6),
          ("portable", 2),
          ("rack-mount", 7),
          ("tower", 5),
          ("unknown", 1))
    )


_CpqSiFormFactor_Type.__name__ = "Integer32"
_CpqSiFormFactor_Object = MibScalar
cpqSiFormFactor = _CpqSiFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 2),
    _CpqSiFormFactor_Type()
)
cpqSiFormFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiFormFactor.setStatus("mandatory")


class _CpqSiAssetTag_Type(DisplayString):
    """Custom type cpqSiAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiAssetTag_Type.__name__ = "DisplayString"
_CpqSiAssetTag_Object = MibScalar
cpqSiAssetTag = _CpqSiAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 3),
    _CpqSiAssetTag_Type()
)
cpqSiAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiAssetTag.setStatus("mandatory")


class _CpqSiOwnershipTag_Type(DisplayString):
    """Custom type cpqSiOwnershipTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CpqSiOwnershipTag_Type.__name__ = "DisplayString"
_CpqSiOwnershipTag_Object = MibScalar
cpqSiOwnershipTag = _CpqSiOwnershipTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 4),
    _CpqSiOwnershipTag_Type()
)
cpqSiOwnershipTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiOwnershipTag.setStatus("mandatory")


class _CpqSiSysServiceNum_Type(DisplayString):
    """Custom type cpqSiSysServiceNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysServiceNum_Type.__name__ = "DisplayString"
_CpqSiSysServiceNum_Object = MibScalar
cpqSiSysServiceNum = _CpqSiSysServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 5),
    _CpqSiSysServiceNum_Type()
)
cpqSiSysServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysServiceNum.setStatus("mandatory")


class _CpqSiSysProductId_Type(DisplayString):
    """Custom type cpqSiSysProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysProductId_Type.__name__ = "DisplayString"
_CpqSiSysProductId_Object = MibScalar
cpqSiSysProductId = _CpqSiSysProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 6),
    _CpqSiSysProductId_Type()
)
cpqSiSysProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysProductId.setStatus("mandatory")
_CpqSiAssetTagMaxLength_Type = Integer32
_CpqSiAssetTagMaxLength_Object = MibScalar
cpqSiAssetTagMaxLength = _CpqSiAssetTagMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 7),
    _CpqSiAssetTagMaxLength_Type()
)
cpqSiAssetTagMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiAssetTagMaxLength.setStatus("optional")
_CpqSiVirtualSystemTable_Object = MibTable
cpqSiVirtualSystemTable = _CpqSiVirtualSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    cpqSiVirtualSystemTable.setStatus("optional")
_CpqSiVirtualSystemEntry_Object = MibTableRow
cpqSiVirtualSystemEntry = _CpqSiVirtualSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 8, 1)
)
cpqSiVirtualSystemEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiVirtualSystemIndex"),
)
if mibBuilder.loadTexts:
    cpqSiVirtualSystemEntry.setStatus("optional")


class _CpqSiVirtualSystemIndex_Type(Integer32):
    """Custom type cpqSiVirtualSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiVirtualSystemIndex_Type.__name__ = "Integer32"
_CpqSiVirtualSystemIndex_Object = MibTableColumn
cpqSiVirtualSystemIndex = _CpqSiVirtualSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 8, 1, 1),
    _CpqSiVirtualSystemIndex_Type()
)
cpqSiVirtualSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVirtualSystemIndex.setStatus("optional")
_CpqSiVirtualSystemSerialNumber_Type = DisplayString
_CpqSiVirtualSystemSerialNumber_Object = MibTableColumn
cpqSiVirtualSystemSerialNumber = _CpqSiVirtualSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 8, 1, 2),
    _CpqSiVirtualSystemSerialNumber_Type()
)
cpqSiVirtualSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVirtualSystemSerialNumber.setStatus("optional")
_CpqSiVirtualSystemUUID_Type = DisplayString
_CpqSiVirtualSystemUUID_Object = MibTableColumn
cpqSiVirtualSystemUUID = _CpqSiVirtualSystemUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 2, 8, 1, 3),
    _CpqSiVirtualSystemUUID_Type()
)
cpqSiVirtualSystemUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVirtualSystemUUID.setStatus("optional")
_CpqSiSecurity_ObjectIdentity = ObjectIdentity
cpqSiSecurity = _CpqSiSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3)
)


class _CpqSiPowerOnPassword_Type(Integer32):
    """Custom type cpqSiPowerOnPassword based on Integer32"""
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


_CpqSiPowerOnPassword_Type.__name__ = "Integer32"
_CpqSiPowerOnPassword_Object = MibScalar
cpqSiPowerOnPassword = _CpqSiPowerOnPassword_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 1),
    _CpqSiPowerOnPassword_Type()
)
cpqSiPowerOnPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPowerOnPassword.setStatus("mandatory")


class _CpqSiNetServerMode_Type(Integer32):
    """Custom type cpqSiNetServerMode based on Integer32"""
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


_CpqSiNetServerMode_Type.__name__ = "Integer32"
_CpqSiNetServerMode_Object = MibScalar
cpqSiNetServerMode = _CpqSiNetServerMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 2),
    _CpqSiNetServerMode_Type()
)
cpqSiNetServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiNetServerMode.setStatus("mandatory")


class _CpqSiQuickLockPassword_Type(Integer32):
    """Custom type cpqSiQuickLockPassword based on Integer32"""
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


_CpqSiQuickLockPassword_Type.__name__ = "Integer32"
_CpqSiQuickLockPassword_Object = MibScalar
cpqSiQuickLockPassword = _CpqSiQuickLockPassword_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 3),
    _CpqSiQuickLockPassword_Type()
)
cpqSiQuickLockPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiQuickLockPassword.setStatus("mandatory")


class _CpqSiQuickBlank_Type(Integer32):
    """Custom type cpqSiQuickBlank based on Integer32"""
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


_CpqSiQuickBlank_Type.__name__ = "Integer32"
_CpqSiQuickBlank_Object = MibScalar
cpqSiQuickBlank = _CpqSiQuickBlank_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 4),
    _CpqSiQuickBlank_Type()
)
cpqSiQuickBlank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiQuickBlank.setStatus("mandatory")


class _CpqSiDisketteBootControl_Type(Integer32):
    """Custom type cpqSiDisketteBootControl based on Integer32"""
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


_CpqSiDisketteBootControl_Type.__name__ = "Integer32"
_CpqSiDisketteBootControl_Object = MibScalar
cpqSiDisketteBootControl = _CpqSiDisketteBootControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 5),
    _CpqSiDisketteBootControl_Type()
)
cpqSiDisketteBootControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiDisketteBootControl.setStatus("mandatory")


class _CpqSiSerialPortAControl_Type(Integer32):
    """Custom type cpqSiSerialPortAControl based on Integer32"""
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


_CpqSiSerialPortAControl_Type.__name__ = "Integer32"
_CpqSiSerialPortAControl_Object = MibScalar
cpqSiSerialPortAControl = _CpqSiSerialPortAControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 6),
    _CpqSiSerialPortAControl_Type()
)
cpqSiSerialPortAControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSerialPortAControl.setStatus("mandatory")


class _CpqSiSerialPortBControl_Type(Integer32):
    """Custom type cpqSiSerialPortBControl based on Integer32"""
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


_CpqSiSerialPortBControl_Type.__name__ = "Integer32"
_CpqSiSerialPortBControl_Object = MibScalar
cpqSiSerialPortBControl = _CpqSiSerialPortBControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 7),
    _CpqSiSerialPortBControl_Type()
)
cpqSiSerialPortBControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSerialPortBControl.setStatus("mandatory")


class _CpqSiParallelPortControl_Type(Integer32):
    """Custom type cpqSiParallelPortControl based on Integer32"""
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


_CpqSiParallelPortControl_Type.__name__ = "Integer32"
_CpqSiParallelPortControl_Object = MibScalar
cpqSiParallelPortControl = _CpqSiParallelPortControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 8),
    _CpqSiParallelPortControl_Type()
)
cpqSiParallelPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiParallelPortControl.setStatus("mandatory")


class _CpqSiFloppyDiskControl_Type(Integer32):
    """Custom type cpqSiFloppyDiskControl based on Integer32"""
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


_CpqSiFloppyDiskControl_Type.__name__ = "Integer32"
_CpqSiFloppyDiskControl_Object = MibScalar
cpqSiFloppyDiskControl = _CpqSiFloppyDiskControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 9),
    _CpqSiFloppyDiskControl_Type()
)
cpqSiFloppyDiskControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFloppyDiskControl.setStatus("mandatory")


class _CpqSiFixedDiskControl_Type(Integer32):
    """Custom type cpqSiFixedDiskControl based on Integer32"""
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


_CpqSiFixedDiskControl_Type.__name__ = "Integer32"
_CpqSiFixedDiskControl_Object = MibScalar
cpqSiFixedDiskControl = _CpqSiFixedDiskControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 10),
    _CpqSiFixedDiskControl_Type()
)
cpqSiFixedDiskControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFixedDiskControl.setStatus("mandatory")


class _CpqSiHoodRemovedTime_Type(DisplayString):
    """Custom type cpqSiHoodRemovedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiHoodRemovedTime_Type.__name__ = "DisplayString"
_CpqSiHoodRemovedTime_Object = MibScalar
cpqSiHoodRemovedTime = _CpqSiHoodRemovedTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 11),
    _CpqSiHoodRemovedTime_Type()
)
cpqSiHoodRemovedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHoodRemovedTime.setStatus("mandatory")


class _CpqSiHoodSensorConfiguration_Type(Integer32):
    """Custom type cpqSiHoodSensorConfiguration based on Integer32"""
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
        *(("adminPasswordProtected", 4),
          ("disabled", 2),
          ("notifyUser", 3),
          ("other", 1))
    )


_CpqSiHoodSensorConfiguration_Type.__name__ = "Integer32"
_CpqSiHoodSensorConfiguration_Object = MibScalar
cpqSiHoodSensorConfiguration = _CpqSiHoodSensorConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 12),
    _CpqSiHoodSensorConfiguration_Type()
)
cpqSiHoodSensorConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHoodSensorConfiguration.setStatus("mandatory")


class _CpqSiSmartCoverLockStatus_Type(Integer32):
    """Custom type cpqSiSmartCoverLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("other", 1),
          ("unlocked", 2))
    )


_CpqSiSmartCoverLockStatus_Type.__name__ = "Integer32"
_CpqSiSmartCoverLockStatus_Object = MibScalar
cpqSiSmartCoverLockStatus = _CpqSiSmartCoverLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 13),
    _CpqSiSmartCoverLockStatus_Type()
)
cpqSiSmartCoverLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSmartCoverLockStatus.setStatus("mandatory")


class _CpqSiUSBPortControl_Type(Integer32):
    """Custom type cpqSiUSBPortControl based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("externalportdisabled", 5),
          ("legacydisabled", 4),
          ("other", 1))
    )


_CpqSiUSBPortControl_Type.__name__ = "Integer32"
_CpqSiUSBPortControl_Object = MibScalar
cpqSiUSBPortControl = _CpqSiUSBPortControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 3, 14),
    _CpqSiUSBPortControl_Type()
)
cpqSiUSBPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiUSBPortControl.setStatus("mandatory")
_CpqSiSystemBoard_ObjectIdentity = ObjectIdentity
cpqSiSystemBoard = _CpqSiSystemBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4)
)


class _CpqSiProductId_Type(Integer32):
    """Custom type cpqSiProductId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSiProductId_Type.__name__ = "Integer32"
_CpqSiProductId_Object = MibScalar
cpqSiProductId = _CpqSiProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 1),
    _CpqSiProductId_Type()
)
cpqSiProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProductId.setStatus("mandatory")


class _CpqSiProductName_Type(DisplayString):
    """Custom type cpqSiProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiProductName_Type.__name__ = "DisplayString"
_CpqSiProductName_Object = MibScalar
cpqSiProductName = _CpqSiProductName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 2),
    _CpqSiProductName_Type()
)
cpqSiProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProductName.setStatus("mandatory")


class _CpqSiAuxiliaryInput_Type(Integer32):
    """Custom type cpqSiAuxiliaryInput based on Integer32"""
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


_CpqSiAuxiliaryInput_Type.__name__ = "Integer32"
_CpqSiAuxiliaryInput_Object = MibScalar
cpqSiAuxiliaryInput = _CpqSiAuxiliaryInput_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 4),
    _CpqSiAuxiliaryInput_Type()
)
cpqSiAuxiliaryInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiAuxiliaryInput.setStatus("mandatory")
_CpqSiMemModuleTable_Object = MibTable
cpqSiMemModuleTable = _CpqSiMemModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    cpqSiMemModuleTable.setStatus("mandatory")
_CpqSiMemModuleEntry_Object = MibTableRow
cpqSiMemModuleEntry = _CpqSiMemModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1)
)
cpqSiMemModuleEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiMemBoardIndex"),
    (0, "CPQSINFO-MIB", "cpqSiMemModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqSiMemModuleEntry.setStatus("mandatory")


class _CpqSiMemBoardIndex_Type(Integer32):
    """Custom type cpqSiMemBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiMemBoardIndex_Type.__name__ = "Integer32"
_CpqSiMemBoardIndex_Object = MibTableColumn
cpqSiMemBoardIndex = _CpqSiMemBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 1),
    _CpqSiMemBoardIndex_Type()
)
cpqSiMemBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemBoardIndex.setStatus("mandatory")


class _CpqSiMemModuleIndex_Type(Integer32):
    """Custom type cpqSiMemModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMemModuleIndex_Type.__name__ = "Integer32"
_CpqSiMemModuleIndex_Object = MibTableColumn
cpqSiMemModuleIndex = _CpqSiMemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 2),
    _CpqSiMemModuleIndex_Type()
)
cpqSiMemModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleIndex.setStatus("mandatory")


class _CpqSiMemModuleSize_Type(Integer32):
    """Custom type cpqSiMemModuleSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSiMemModuleSize_Type.__name__ = "Integer32"
_CpqSiMemModuleSize_Object = MibTableColumn
cpqSiMemModuleSize = _CpqSiMemModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 3),
    _CpqSiMemModuleSize_Type()
)
cpqSiMemModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleSize.setStatus("mandatory")


class _CpqSiMemModuleType_Type(Integer32):
    """Custom type cpqSiMemModuleType based on Integer32"""
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
        *(("board", 2),
          ("compaq-specific", 7),
          ("cpqDoubleWidthModule", 4),
          ("cpqSingleWidthModule", 3),
          ("dimm", 8),
          ("fb-dimm", 12),
          ("other", 1),
          ("pcmcia", 6),
          ("rimm", 10),
          ("simm", 5),
          ("smallOutlineDimm", 9),
          ("srimm", 11))
    )


_CpqSiMemModuleType_Type.__name__ = "Integer32"
_CpqSiMemModuleType_Object = MibTableColumn
cpqSiMemModuleType = _CpqSiMemModuleType_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 4),
    _CpqSiMemModuleType_Type()
)
cpqSiMemModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleType.setStatus("mandatory")


class _CpqSiMemModuleSpeed_Type(Integer32):
    """Custom type cpqSiMemModuleSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMemModuleSpeed_Type.__name__ = "Integer32"
_CpqSiMemModuleSpeed_Object = MibTableColumn
cpqSiMemModuleSpeed = _CpqSiMemModuleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 5),
    _CpqSiMemModuleSpeed_Type()
)
cpqSiMemModuleSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleSpeed.setStatus("deprecated")


class _CpqSiMemModuleTechnology_Type(Integer32):
    """Custom type cpqSiMemModuleTechnology based on Integer32"""
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
        *(("burstEdoPageMode", 4),
          ("edoPageMode", 3),
          ("fastPageMode", 2),
          ("other", 1),
          ("rdram", 6),
          ("synchronous", 5))
    )


_CpqSiMemModuleTechnology_Type.__name__ = "Integer32"
_CpqSiMemModuleTechnology_Object = MibTableColumn
cpqSiMemModuleTechnology = _CpqSiMemModuleTechnology_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 6),
    _CpqSiMemModuleTechnology_Type()
)
cpqSiMemModuleTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleTechnology.setStatus("mandatory")


class _CpqSiMemModuleManufacturer_Type(DisplayString):
    """Custom type cpqSiMemModuleManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModuleManufacturer_Type.__name__ = "DisplayString"
_CpqSiMemModuleManufacturer_Object = MibTableColumn
cpqSiMemModuleManufacturer = _CpqSiMemModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 7),
    _CpqSiMemModuleManufacturer_Type()
)
cpqSiMemModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleManufacturer.setStatus("mandatory")


class _CpqSiMemModulePartNo_Type(DisplayString):
    """Custom type cpqSiMemModulePartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModulePartNo_Type.__name__ = "DisplayString"
_CpqSiMemModulePartNo_Object = MibTableColumn
cpqSiMemModulePartNo = _CpqSiMemModulePartNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 8),
    _CpqSiMemModulePartNo_Type()
)
cpqSiMemModulePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModulePartNo.setStatus("mandatory")


class _CpqSiMemModuleDate_Type(OctetString):
    """Custom type cpqSiMemModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiMemModuleDate_Type.__name__ = "OctetString"
_CpqSiMemModuleDate_Object = MibTableColumn
cpqSiMemModuleDate = _CpqSiMemModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 9),
    _CpqSiMemModuleDate_Type()
)
cpqSiMemModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleDate.setStatus("mandatory")


class _CpqSiMemModuleSerialNo_Type(DisplayString):
    """Custom type cpqSiMemModuleSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModuleSerialNo_Type.__name__ = "DisplayString"
_CpqSiMemModuleSerialNo_Object = MibTableColumn
cpqSiMemModuleSerialNo = _CpqSiMemModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 10),
    _CpqSiMemModuleSerialNo_Type()
)
cpqSiMemModuleSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiMemModuleSerialNo.setStatus("mandatory")


class _CpqSiMemModuleECCStatus_Type(Integer32):
    """Custom type cpqSiMemModuleECCStatus based on Integer32"""
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
        *(("degraded", 3),
          ("degradedModuleIndexUnknown", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMemModuleECCStatus_Type.__name__ = "Integer32"
_CpqSiMemModuleECCStatus_Object = MibTableColumn
cpqSiMemModuleECCStatus = _CpqSiMemModuleECCStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 11),
    _CpqSiMemModuleECCStatus_Type()
)
cpqSiMemModuleECCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleECCStatus.setStatus("mandatory")


class _CpqSiMemModuleHwLocation_Type(DisplayString):
    """Custom type cpqSiMemModuleHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModuleHwLocation_Type.__name__ = "DisplayString"
_CpqSiMemModuleHwLocation_Object = MibTableColumn
cpqSiMemModuleHwLocation = _CpqSiMemModuleHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 12),
    _CpqSiMemModuleHwLocation_Type()
)
cpqSiMemModuleHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleHwLocation.setStatus("optional")


class _CpqSiMemModuleFrequency_Type(Integer32):
    """Custom type cpqSiMemModuleFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMemModuleFrequency_Type.__name__ = "Integer32"
_CpqSiMemModuleFrequency_Object = MibTableColumn
cpqSiMemModuleFrequency = _CpqSiMemModuleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 13),
    _CpqSiMemModuleFrequency_Type()
)
cpqSiMemModuleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleFrequency.setStatus("mandatory")


class _CpqSiMemModuleCellTablePtr_Type(Integer32):
    """Custom type cpqSiMemModuleCellTablePtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CpqSiMemModuleCellTablePtr_Type.__name__ = "Integer32"
_CpqSiMemModuleCellTablePtr_Object = MibTableColumn
cpqSiMemModuleCellTablePtr = _CpqSiMemModuleCellTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 14),
    _CpqSiMemModuleCellTablePtr_Type()
)
cpqSiMemModuleCellTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleCellTablePtr.setStatus("optional")


class _CpqSiMemModuleCellStatus_Type(Integer32):
    """Custom type cpqSiMemModuleCellStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deconfigured", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMemModuleCellStatus_Type.__name__ = "Integer32"
_CpqSiMemModuleCellStatus_Object = MibTableColumn
cpqSiMemModuleCellStatus = _CpqSiMemModuleCellStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 15),
    _CpqSiMemModuleCellStatus_Type()
)
cpqSiMemModuleCellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleCellStatus.setStatus("optional")


class _CpqSiMemModulePartNoMfgr_Type(DisplayString):
    """Custom type cpqSiMemModulePartNoMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModulePartNoMfgr_Type.__name__ = "DisplayString"
_CpqSiMemModulePartNoMfgr_Object = MibTableColumn
cpqSiMemModulePartNoMfgr = _CpqSiMemModulePartNoMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 16),
    _CpqSiMemModulePartNoMfgr_Type()
)
cpqSiMemModulePartNoMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModulePartNoMfgr.setStatus("optional")


class _CpqSiMemModuleSerialNoMfgr_Type(DisplayString):
    """Custom type cpqSiMemModuleSerialNoMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMemModuleSerialNoMfgr_Type.__name__ = "DisplayString"
_CpqSiMemModuleSerialNoMfgr_Object = MibTableColumn
cpqSiMemModuleSerialNoMfgr = _CpqSiMemModuleSerialNoMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 5, 1, 17),
    _CpqSiMemModuleSerialNoMfgr_Type()
)
cpqSiMemModuleSerialNoMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemModuleSerialNoMfgr.setStatus("optional")


class _CpqSiSystemId_Type(Integer32):
    """Custom type cpqSiSystemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSystemId_Type.__name__ = "Integer32"
_CpqSiSystemId_Object = MibScalar
cpqSiSystemId = _CpqSiSystemId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 6),
    _CpqSiSystemId_Type()
)
cpqSiSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSystemId.setStatus("mandatory")


class _CpqSiSystemCpuId_Type(Integer32):
    """Custom type cpqSiSystemCpuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSystemCpuId_Type.__name__ = "Integer32"
_CpqSiSystemCpuId_Object = MibScalar
cpqSiSystemCpuId = _CpqSiSystemCpuId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 7),
    _CpqSiSystemCpuId_Type()
)
cpqSiSystemCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSystemCpuId.setStatus("mandatory")


class _CpqSiFlashRomSupport_Type(Integer32):
    """Custom type cpqSiFlashRomSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("other", 1),
          ("supported", 3))
    )


_CpqSiFlashRomSupport_Type.__name__ = "Integer32"
_CpqSiFlashRomSupport_Object = MibScalar
cpqSiFlashRomSupport = _CpqSiFlashRomSupport_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 8),
    _CpqSiFlashRomSupport_Type()
)
cpqSiFlashRomSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFlashRomSupport.setStatus("mandatory")


class _CpqSiQuickTestRomDate_Type(OctetString):
    """Custom type cpqSiQuickTestRomDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiQuickTestRomDate_Type.__name__ = "OctetString"
_CpqSiQuickTestRomDate_Object = MibScalar
cpqSiQuickTestRomDate = _CpqSiQuickTestRomDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 9),
    _CpqSiQuickTestRomDate_Type()
)
cpqSiQuickTestRomDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiQuickTestRomDate.setStatus("mandatory")


class _CpqSiReboot_Type(Integer32):
    """Custom type cpqSiReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2693,
              8115,
              9037)
        )
    )
    namedValues = NamedValues(
        *(("autoShutdown", 9037),
          ("available", 2),
          ("defaultOnlyAvailable", 3),
          ("notAvailable", 1),
          ("rebootToCpqUtils", 2693),
          ("rebootToDefault", 8115))
    )


_CpqSiReboot_Type.__name__ = "Integer32"
_CpqSiReboot_Object = MibScalar
cpqSiReboot = _CpqSiReboot_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 10),
    _CpqSiReboot_Type()
)
cpqSiReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiReboot.setStatus("deprecated")
_CpqSiProcMicroPatchTable_Object = MibTable
cpqSiProcMicroPatchTable = _CpqSiProcMicroPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchTable.setStatus("mandatory")
_CpqSiProcMicroPatchEntry_Object = MibTableRow
cpqSiProcMicroPatchEntry = _CpqSiProcMicroPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11, 1)
)
cpqSiProcMicroPatchEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiProcMicroPatchIndex"),
)
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchEntry.setStatus("mandatory")


class _CpqSiProcMicroPatchIndex_Type(Integer32):
    """Custom type cpqSiProcMicroPatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpqSiProcMicroPatchIndex_Type.__name__ = "Integer32"
_CpqSiProcMicroPatchIndex_Object = MibTableColumn
cpqSiProcMicroPatchIndex = _CpqSiProcMicroPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11, 1, 1),
    _CpqSiProcMicroPatchIndex_Type()
)
cpqSiProcMicroPatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchIndex.setStatus("mandatory")
_CpqSiProcMicroPatchId_Type = Integer32
_CpqSiProcMicroPatchId_Object = MibTableColumn
cpqSiProcMicroPatchId = _CpqSiProcMicroPatchId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11, 1, 2),
    _CpqSiProcMicroPatchId_Type()
)
cpqSiProcMicroPatchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchId.setStatus("mandatory")


class _CpqSiProcMicroPatchDate_Type(OctetString):
    """Custom type cpqSiProcMicroPatchDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiProcMicroPatchDate_Type.__name__ = "OctetString"
_CpqSiProcMicroPatchDate_Object = MibTableColumn
cpqSiProcMicroPatchDate = _CpqSiProcMicroPatchDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11, 1, 3),
    _CpqSiProcMicroPatchDate_Type()
)
cpqSiProcMicroPatchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchDate.setStatus("mandatory")


class _CpqSiProcMicroPatchFamily_Type(OctetString):
    """Custom type cpqSiProcMicroPatchFamily based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CpqSiProcMicroPatchFamily_Type.__name__ = "OctetString"
_CpqSiProcMicroPatchFamily_Object = MibTableColumn
cpqSiProcMicroPatchFamily = _CpqSiProcMicroPatchFamily_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 11, 1, 4),
    _CpqSiProcMicroPatchFamily_Type()
)
cpqSiProcMicroPatchFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiProcMicroPatchFamily.setStatus("mandatory")


class _CpqSiPowerMgmtStatus_Type(Integer32):
    """Custom type cpqSiPowerMgmtStatus based on Integer32"""
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


_CpqSiPowerMgmtStatus_Type.__name__ = "Integer32"
_CpqSiPowerMgmtStatus_Object = MibScalar
cpqSiPowerMgmtStatus = _CpqSiPowerMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 12),
    _CpqSiPowerMgmtStatus_Type()
)
cpqSiPowerMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPowerMgmtStatus.setStatus("mandatory")
_CpqSiRebootFlags_Type = Integer32
_CpqSiRebootFlags_Object = MibScalar
cpqSiRebootFlags = _CpqSiRebootFlags_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 13),
    _CpqSiRebootFlags_Type()
)
cpqSiRebootFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiRebootFlags.setStatus("mandatory")


class _CpqSiMemErrorIndex_Type(Integer32):
    """Custom type cpqSiMemErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMemErrorIndex_Type.__name__ = "Integer32"
_CpqSiMemErrorIndex_Object = MibScalar
cpqSiMemErrorIndex = _CpqSiMemErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 14),
    _CpqSiMemErrorIndex_Type()
)
cpqSiMemErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemErrorIndex.setStatus("mandatory")


class _CpqSiMemECCCondition_Type(Integer32):
    """Custom type cpqSiMemECCCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMemECCCondition_Type.__name__ = "Integer32"
_CpqSiMemECCCondition_Object = MibScalar
cpqSiMemECCCondition = _CpqSiMemECCCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 15),
    _CpqSiMemECCCondition_Type()
)
cpqSiMemECCCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemECCCondition.setStatus("mandatory")


class _CpqSiMemConfigChangeData_Type(DisplayString):
    """Custom type cpqSiMemConfigChangeData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 383),
    )


_CpqSiMemConfigChangeData_Type.__name__ = "DisplayString"
_CpqSiMemConfigChangeData_Object = MibScalar
cpqSiMemConfigChangeData = _CpqSiMemConfigChangeData_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 16),
    _CpqSiMemConfigChangeData_Type()
)
cpqSiMemConfigChangeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMemConfigChangeData.setStatus("mandatory")


class _CpqSiServerSystemId_Type(DisplayString):
    """Custom type cpqSiServerSystemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSiServerSystemId_Type.__name__ = "DisplayString"
_CpqSiServerSystemId_Object = MibScalar
cpqSiServerSystemId = _CpqSiServerSystemId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 17),
    _CpqSiServerSystemId_Type()
)
cpqSiServerSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiServerSystemId.setStatus("mandatory")


class _CpqSiPowerScheme_Type(Integer32):
    """Custom type cpqSiPowerScheme based on Integer32"""
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
        *(("balanced", 4),
          ("high-performance", 5),
          ("other", 2),
          ("power-saver", 3),
          ("unsupported", 1),
          ("user-defined", 6))
    )


_CpqSiPowerScheme_Type.__name__ = "Integer32"
_CpqSiPowerScheme_Object = MibScalar
cpqSiPowerScheme = _CpqSiPowerScheme_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 18),
    _CpqSiPowerScheme_Type()
)
cpqSiPowerScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPowerScheme.setStatus("optional")


class _CpqSiPowerSchemeName_Type(DisplayString):
    """Custom type cpqSiPowerSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiPowerSchemeName_Type.__name__ = "DisplayString"
_CpqSiPowerSchemeName_Object = MibScalar
cpqSiPowerSchemeName = _CpqSiPowerSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 19),
    _CpqSiPowerSchemeName_Type()
)
cpqSiPowerSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPowerSchemeName.setStatus("optional")


class _CpqSiCurrentPerformanceStatePointer_Type(Integer32):
    """Custom type cpqSiCurrentPerformanceStatePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiCurrentPerformanceStatePointer_Type.__name__ = "Integer32"
_CpqSiCurrentPerformanceStatePointer_Object = MibScalar
cpqSiCurrentPerformanceStatePointer = _CpqSiCurrentPerformanceStatePointer_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 20),
    _CpqSiCurrentPerformanceStatePointer_Type()
)
cpqSiCurrentPerformanceStatePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiCurrentPerformanceStatePointer.setStatus("optional")


class _CpqSiMinPerformanceState_Type(Integer32):
    """Custom type cpqSiMinPerformanceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMinPerformanceState_Type.__name__ = "Integer32"
_CpqSiMinPerformanceState_Object = MibScalar
cpqSiMinPerformanceState = _CpqSiMinPerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 21),
    _CpqSiMinPerformanceState_Type()
)
cpqSiMinPerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMinPerformanceState.setStatus("optional")


class _CpqSiMaxPerformanceState_Type(Integer32):
    """Custom type cpqSiMaxPerformanceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMaxPerformanceState_Type.__name__ = "Integer32"
_CpqSiMaxPerformanceState_Object = MibScalar
cpqSiMaxPerformanceState = _CpqSiMaxPerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 22),
    _CpqSiMaxPerformanceState_Type()
)
cpqSiMaxPerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMaxPerformanceState.setStatus("optional")
_CpqSiPerfStateTable_Object = MibTable
cpqSiPerfStateTable = _CpqSiPerfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23)
)
if mibBuilder.loadTexts:
    cpqSiPerfStateTable.setStatus("optional")
_CpqSiPerfStateEntry_Object = MibTableRow
cpqSiPerfStateEntry = _CpqSiPerfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23, 1)
)
cpqSiPerfStateEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiPerfStateIndex"),
)
if mibBuilder.loadTexts:
    cpqSiPerfStateEntry.setStatus("optional")


class _CpqSiPerfStateIndex_Type(Integer32):
    """Custom type cpqSiPerfStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiPerfStateIndex_Type.__name__ = "Integer32"
_CpqSiPerfStateIndex_Object = MibTableColumn
cpqSiPerfStateIndex = _CpqSiPerfStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23, 1, 1),
    _CpqSiPerfStateIndex_Type()
)
cpqSiPerfStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPerfStateIndex.setStatus("optional")


class _CpqSiPerfState_Type(Integer32):
    """Custom type cpqSiPerfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiPerfState_Type.__name__ = "Integer32"
_CpqSiPerfState_Object = MibTableColumn
cpqSiPerfState = _CpqSiPerfState_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23, 1, 2),
    _CpqSiPerfState_Type()
)
cpqSiPerfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPerfState.setStatus("optional")


class _CpqSiPerfStateCpuFrequency_Type(Integer32):
    """Custom type cpqSiPerfStateCpuFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSiPerfStateCpuFrequency_Type.__name__ = "Integer32"
_CpqSiPerfStateCpuFrequency_Object = MibTableColumn
cpqSiPerfStateCpuFrequency = _CpqSiPerfStateCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23, 1, 3),
    _CpqSiPerfStateCpuFrequency_Type()
)
cpqSiPerfStateCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPerfStateCpuFrequency.setStatus("optional")


class _CpqSiPerfStateCpuPower_Type(Integer32):
    """Custom type cpqSiPerfStateCpuPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSiPerfStateCpuPower_Type.__name__ = "Integer32"
_CpqSiPerfStateCpuPower_Object = MibTableColumn
cpqSiPerfStateCpuPower = _CpqSiPerfStateCpuPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 23, 1, 4),
    _CpqSiPerfStateCpuPower_Type()
)
cpqSiPerfStateCpuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPerfStateCpuPower.setStatus("optional")


class _CpqSiTPMmodule_Type(Integer32):
    """Custom type cpqSiTPMmodule based on Integer32"""
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
        *(("absent", 2),
          ("other", 1),
          ("presentDisabled", 4),
          ("presentEnabled", 3))
    )


_CpqSiTPMmodule_Type.__name__ = "Integer32"
_CpqSiTPMmodule_Object = MibScalar
cpqSiTPMmodule = _CpqSiTPMmodule_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 4, 24),
    _CpqSiTPMmodule_Type()
)
cpqSiTPMmodule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiTPMmodule.setStatus("optional")
_CpqSiBoardRev_ObjectIdentity = ObjectIdentity
cpqSiBoardRev = _CpqSiBoardRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5)
)


class _CpqSiCurRevDate_Type(DisplayString):
    """Custom type cpqSiCurRevDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpqSiCurRevDate_Type.__name__ = "DisplayString"
_CpqSiCurRevDate_Object = MibScalar
cpqSiCurRevDate = _CpqSiCurRevDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 1),
    _CpqSiCurRevDate_Type()
)
cpqSiCurRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiCurRevDate.setStatus("mandatory")


class _CpqSiPrevRevDate_Type(DisplayString):
    """Custom type cpqSiPrevRevDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpqSiPrevRevDate_Type.__name__ = "DisplayString"
_CpqSiPrevRevDate_Object = MibScalar
cpqSiPrevRevDate = _CpqSiPrevRevDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 2),
    _CpqSiPrevRevDate_Type()
)
cpqSiPrevRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiPrevRevDate.setStatus("mandatory")
_CpqSiBoardRevTable_Object = MibTable
cpqSiBoardRevTable = _CpqSiBoardRevTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cpqSiBoardRevTable.setStatus("mandatory")
_CpqSiBoardRevEntry_Object = MibTableRow
cpqSiBoardRevEntry = _CpqSiBoardRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1)
)
cpqSiBoardRevEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiBoardRevSlotIndex"),
    (0, "CPQSINFO-MIB", "cpqSiBoardRevIndex"),
)
if mibBuilder.loadTexts:
    cpqSiBoardRevEntry.setStatus("mandatory")


class _CpqSiBoardRevSlotIndex_Type(Integer32):
    """Custom type cpqSiBoardRevSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiBoardRevSlotIndex_Type.__name__ = "Integer32"
_CpqSiBoardRevSlotIndex_Object = MibTableColumn
cpqSiBoardRevSlotIndex = _CpqSiBoardRevSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 1),
    _CpqSiBoardRevSlotIndex_Type()
)
cpqSiBoardRevSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevSlotIndex.setStatus("mandatory")


class _CpqSiBoardRevIndex_Type(Integer32):
    """Custom type cpqSiBoardRevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiBoardRevIndex_Type.__name__ = "Integer32"
_CpqSiBoardRevIndex_Object = MibTableColumn
cpqSiBoardRevIndex = _CpqSiBoardRevIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 2),
    _CpqSiBoardRevIndex_Type()
)
cpqSiBoardRevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevIndex.setStatus("mandatory")


class _CpqSiBoardRevId_Type(DisplayString):
    """Custom type cpqSiBoardRevId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqSiBoardRevId_Type.__name__ = "DisplayString"
_CpqSiBoardRevId_Object = MibTableColumn
cpqSiBoardRevId = _CpqSiBoardRevId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 3),
    _CpqSiBoardRevId_Type()
)
cpqSiBoardRevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevId.setStatus("mandatory")


class _CpqSiBoardRevCur_Type(DisplayString):
    """Custom type cpqSiBoardRevCur based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSiBoardRevCur_Type.__name__ = "DisplayString"
_CpqSiBoardRevCur_Object = MibTableColumn
cpqSiBoardRevCur = _CpqSiBoardRevCur_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 4),
    _CpqSiBoardRevCur_Type()
)
cpqSiBoardRevCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevCur.setStatus("mandatory")


class _CpqSiBoardRevPrev_Type(DisplayString):
    """Custom type cpqSiBoardRevPrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSiBoardRevPrev_Type.__name__ = "DisplayString"
_CpqSiBoardRevPrev_Object = MibTableColumn
cpqSiBoardRevPrev = _CpqSiBoardRevPrev_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 5),
    _CpqSiBoardRevPrev_Type()
)
cpqSiBoardRevPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevPrev.setStatus("mandatory")


class _CpqSiBoardRevHwLocation_Type(DisplayString):
    """Custom type cpqSiBoardRevHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiBoardRevHwLocation_Type.__name__ = "DisplayString"
_CpqSiBoardRevHwLocation_Object = MibTableColumn
cpqSiBoardRevHwLocation = _CpqSiBoardRevHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 3, 1, 6),
    _CpqSiBoardRevHwLocation_Type()
)
cpqSiBoardRevHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiBoardRevHwLocation.setStatus("optional")
_CpqSiFirmwareRevTable_Object = MibTable
cpqSiFirmwareRevTable = _CpqSiFirmwareRevTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    cpqSiFirmwareRevTable.setStatus("mandatory")
_CpqSiFirmwareRevEntry_Object = MibTableRow
cpqSiFirmwareRevEntry = _CpqSiFirmwareRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1)
)
cpqSiFirmwareRevEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiFirmwareRevIndex"),
)
if mibBuilder.loadTexts:
    cpqSiFirmwareRevEntry.setStatus("mandatory")
_CpqSiFirmwareRevIndex_Type = Integer32
_CpqSiFirmwareRevIndex_Object = MibTableColumn
cpqSiFirmwareRevIndex = _CpqSiFirmwareRevIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 1),
    _CpqSiFirmwareRevIndex_Type()
)
cpqSiFirmwareRevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareRevIndex.setStatus("mandatory")
_CpqSiFirmwareRevDesc_Type = DisplayString
_CpqSiFirmwareRevDesc_Object = MibTableColumn
cpqSiFirmwareRevDesc = _CpqSiFirmwareRevDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 2),
    _CpqSiFirmwareRevDesc_Type()
)
cpqSiFirmwareRevDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareRevDesc.setStatus("mandatory")
_CpqSiFirmwareRevString_Type = DisplayString
_CpqSiFirmwareRevString_Object = MibTableColumn
cpqSiFirmwareRevString = _CpqSiFirmwareRevString_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 3),
    _CpqSiFirmwareRevString_Type()
)
cpqSiFirmwareRevString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareRevString.setStatus("mandatory")
_CpqSiFirmwareRevCellTablePtr_Type = Integer32
_CpqSiFirmwareRevCellTablePtr_Object = MibTableColumn
cpqSiFirmwareRevCellTablePtr = _CpqSiFirmwareRevCellTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 4),
    _CpqSiFirmwareRevCellTablePtr_Type()
)
cpqSiFirmwareRevCellTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareRevCellTablePtr.setStatus("deprecated")


class _CpqSiFirmwareLocation_Type(DisplayString):
    """Custom type cpqSiFirmwareLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiFirmwareLocation_Type.__name__ = "DisplayString"
_CpqSiFirmwareLocation_Object = MibTableColumn
cpqSiFirmwareLocation = _CpqSiFirmwareLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 5),
    _CpqSiFirmwareLocation_Type()
)
cpqSiFirmwareLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareLocation.setStatus("optional")


class _CpqSiFirmwareStatus_Type(Integer32):
    """Custom type cpqSiFirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_CpqSiFirmwareStatus_Type.__name__ = "Integer32"
_CpqSiFirmwareStatus_Object = MibTableColumn
cpqSiFirmwareStatus = _CpqSiFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 4, 1, 6),
    _CpqSiFirmwareStatus_Type()
)
cpqSiFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareStatus.setStatus("optional")
_CpqSiFirmwareCfgTable_Object = MibTable
cpqSiFirmwareCfgTable = _CpqSiFirmwareCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 5)
)
if mibBuilder.loadTexts:
    cpqSiFirmwareCfgTable.setStatus("mandatory")
_CpqSiFirmwareCfgEntry_Object = MibTableRow
cpqSiFirmwareCfgEntry = _CpqSiFirmwareCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 5, 1)
)
cpqSiFirmwareCfgEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiFirmwareCfgName"),
)
if mibBuilder.loadTexts:
    cpqSiFirmwareCfgEntry.setStatus("mandatory")
_CpqSiFirmwareCfgName_Type = DisplayString
_CpqSiFirmwareCfgName_Object = MibTableColumn
cpqSiFirmwareCfgName = _CpqSiFirmwareCfgName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 5, 1, 1),
    _CpqSiFirmwareCfgName_Type()
)
cpqSiFirmwareCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareCfgName.setStatus("mandatory")
_CpqSiFirmwareCfgValue_Type = DisplayString
_CpqSiFirmwareCfgValue_Object = MibTableColumn
cpqSiFirmwareCfgValue = _CpqSiFirmwareCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 5, 5, 1, 2),
    _CpqSiFirmwareCfgValue_Type()
)
cpqSiFirmwareCfgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFirmwareCfgValue.setStatus("mandatory")
_CpqSiRackServer_ObjectIdentity = ObjectIdentity
cpqSiRackServer = _CpqSiRackServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 6)
)


class _CpqSiRackServerShutdownRole_Type(Integer32):
    """Custom type cpqSiRackServerShutdownRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("other", 1),
          ("slave", 3))
    )


_CpqSiRackServerShutdownRole_Type.__name__ = "Integer32"
_CpqSiRackServerShutdownRole_Object = MibScalar
cpqSiRackServerShutdownRole = _CpqSiRackServerShutdownRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 6, 1),
    _CpqSiRackServerShutdownRole_Type()
)
cpqSiRackServerShutdownRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiRackServerShutdownRole.setStatus("mandatory")


class _CpqSiRackServerMasterName_Type(DisplayString):
    """Custom type cpqSiRackServerMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CpqSiRackServerMasterName_Type.__name__ = "DisplayString"
_CpqSiRackServerMasterName_Object = MibScalar
cpqSiRackServerMasterName = _CpqSiRackServerMasterName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 6, 2),
    _CpqSiRackServerMasterName_Type()
)
cpqSiRackServerMasterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiRackServerMasterName.setStatus("mandatory")
_CpqSiVideo_ObjectIdentity = ObjectIdentity
cpqSiVideo = _CpqSiVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7)
)


class _CpqSiVideoEdidRaw_Type(OctetString):
    """Custom type cpqSiVideoEdidRaw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CpqSiVideoEdidRaw_Type.__name__ = "OctetString"
_CpqSiVideoEdidRaw_Object = MibScalar
cpqSiVideoEdidRaw = _CpqSiVideoEdidRaw_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 1),
    _CpqSiVideoEdidRaw_Type()
)
cpqSiVideoEdidRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoEdidRaw.setStatus("deprecated")


class _CpqSiVideoDesc_Type(DisplayString):
    """Custom type cpqSiVideoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiVideoDesc_Type.__name__ = "DisplayString"
_CpqSiVideoDesc_Object = MibScalar
cpqSiVideoDesc = _CpqSiVideoDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 2),
    _CpqSiVideoDesc_Type()
)
cpqSiVideoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoDesc.setStatus("deprecated")


class _CpqSiVideoSerialNumber_Type(DisplayString):
    """Custom type cpqSiVideoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqSiVideoSerialNumber_Type.__name__ = "DisplayString"
_CpqSiVideoSerialNumber_Object = MibScalar
cpqSiVideoSerialNumber = _CpqSiVideoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 3),
    _CpqSiVideoSerialNumber_Type()
)
cpqSiVideoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoSerialNumber.setStatus("deprecated")


class _CpqSiVideoManufactureDate_Type(OctetString):
    """Custom type cpqSiVideoManufactureDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiVideoManufactureDate_Type.__name__ = "OctetString"
_CpqSiVideoManufactureDate_Object = MibScalar
cpqSiVideoManufactureDate = _CpqSiVideoManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 4),
    _CpqSiVideoManufactureDate_Type()
)
cpqSiVideoManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoManufactureDate.setStatus("deprecated")


class _CpqSiVideoHeight_Type(Integer32):
    """Custom type cpqSiVideoHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiVideoHeight_Type.__name__ = "Integer32"
_CpqSiVideoHeight_Object = MibScalar
cpqSiVideoHeight = _CpqSiVideoHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 5),
    _CpqSiVideoHeight_Type()
)
cpqSiVideoHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoHeight.setStatus("deprecated")


class _CpqSiVideoWidth_Type(Integer32):
    """Custom type cpqSiVideoWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiVideoWidth_Type.__name__ = "Integer32"
_CpqSiVideoWidth_Object = MibScalar
cpqSiVideoWidth = _CpqSiVideoWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 6),
    _CpqSiVideoWidth_Type()
)
cpqSiVideoWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoWidth.setStatus("deprecated")


class _CpqSiVideoMaxHorPixel_Type(Integer32):
    """Custom type cpqSiVideoMaxHorPixel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiVideoMaxHorPixel_Type.__name__ = "Integer32"
_CpqSiVideoMaxHorPixel_Object = MibScalar
cpqSiVideoMaxHorPixel = _CpqSiVideoMaxHorPixel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 7),
    _CpqSiVideoMaxHorPixel_Type()
)
cpqSiVideoMaxHorPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoMaxHorPixel.setStatus("deprecated")


class _CpqSiVideoMaxVertPixel_Type(Integer32):
    """Custom type cpqSiVideoMaxVertPixel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiVideoMaxVertPixel_Type.__name__ = "Integer32"
_CpqSiVideoMaxVertPixel_Object = MibScalar
cpqSiVideoMaxVertPixel = _CpqSiVideoMaxVertPixel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 8),
    _CpqSiVideoMaxVertPixel_Type()
)
cpqSiVideoMaxVertPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoMaxVertPixel.setStatus("deprecated")


class _CpqSiVideoMaxRefreshRate_Type(Integer32):
    """Custom type cpqSiVideoMaxRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiVideoMaxRefreshRate_Type.__name__ = "Integer32"
_CpqSiVideoMaxRefreshRate_Object = MibScalar
cpqSiVideoMaxRefreshRate = _CpqSiVideoMaxRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 7, 9),
    _CpqSiVideoMaxRefreshRate_Type()
)
cpqSiVideoMaxRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiVideoMaxRefreshRate.setStatus("deprecated")
_CpqSiMonitor_ObjectIdentity = ObjectIdentity
cpqSiMonitor = _CpqSiMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8)
)


class _CpqSiMonitorOverallCondition_Type(Integer32):
    """Custom type cpqSiMonitorOverallCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMonitorOverallCondition_Type.__name__ = "Integer32"
_CpqSiMonitorOverallCondition_Object = MibScalar
cpqSiMonitorOverallCondition = _CpqSiMonitorOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 1),
    _CpqSiMonitorOverallCondition_Type()
)
cpqSiMonitorOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorOverallCondition.setStatus("mandatory")
_CpqSiMonitorTable_Object = MibTable
cpqSiMonitorTable = _CpqSiMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    cpqSiMonitorTable.setStatus("mandatory")
_CpqSiMonitorEntry_Object = MibTableRow
cpqSiMonitorEntry = _CpqSiMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1)
)
cpqSiMonitorEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiMonitorIndex"),
)
if mibBuilder.loadTexts:
    cpqSiMonitorEntry.setStatus("mandatory")


class _CpqSiMonitorIndex_Type(Integer32):
    """Custom type cpqSiMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CpqSiMonitorIndex_Type.__name__ = "Integer32"
_CpqSiMonitorIndex_Object = MibTableColumn
cpqSiMonitorIndex = _CpqSiMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 1),
    _CpqSiMonitorIndex_Type()
)
cpqSiMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorIndex.setStatus("mandatory")


class _CpqSiMonitorEdidRaw_Type(OctetString):
    """Custom type cpqSiMonitorEdidRaw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CpqSiMonitorEdidRaw_Type.__name__ = "OctetString"
_CpqSiMonitorEdidRaw_Object = MibTableColumn
cpqSiMonitorEdidRaw = _CpqSiMonitorEdidRaw_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 2),
    _CpqSiMonitorEdidRaw_Type()
)
cpqSiMonitorEdidRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorEdidRaw.setStatus("mandatory")


class _CpqSiMonitorDesc_Type(DisplayString):
    """Custom type cpqSiMonitorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMonitorDesc_Type.__name__ = "DisplayString"
_CpqSiMonitorDesc_Object = MibTableColumn
cpqSiMonitorDesc = _CpqSiMonitorDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 3),
    _CpqSiMonitorDesc_Type()
)
cpqSiMonitorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorDesc.setStatus("mandatory")


class _CpqSiMonitorSerialNumber_Type(DisplayString):
    """Custom type cpqSiMonitorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqSiMonitorSerialNumber_Type.__name__ = "DisplayString"
_CpqSiMonitorSerialNumber_Object = MibTableColumn
cpqSiMonitorSerialNumber = _CpqSiMonitorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 4),
    _CpqSiMonitorSerialNumber_Type()
)
cpqSiMonitorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorSerialNumber.setStatus("mandatory")


class _CpqSiMonitorManufactureDate_Type(OctetString):
    """Custom type cpqSiMonitorManufactureDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiMonitorManufactureDate_Type.__name__ = "OctetString"
_CpqSiMonitorManufactureDate_Object = MibTableColumn
cpqSiMonitorManufactureDate = _CpqSiMonitorManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 5),
    _CpqSiMonitorManufactureDate_Type()
)
cpqSiMonitorManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorManufactureDate.setStatus("mandatory")


class _CpqSiMonitorHeight_Type(Integer32):
    """Custom type cpqSiMonitorHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiMonitorHeight_Type.__name__ = "Integer32"
_CpqSiMonitorHeight_Object = MibTableColumn
cpqSiMonitorHeight = _CpqSiMonitorHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 6),
    _CpqSiMonitorHeight_Type()
)
cpqSiMonitorHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorHeight.setStatus("mandatory")


class _CpqSiMonitorWidth_Type(Integer32):
    """Custom type cpqSiMonitorWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiMonitorWidth_Type.__name__ = "Integer32"
_CpqSiMonitorWidth_Object = MibTableColumn
cpqSiMonitorWidth = _CpqSiMonitorWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 7),
    _CpqSiMonitorWidth_Type()
)
cpqSiMonitorWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorWidth.setStatus("mandatory")


class _CpqSiMonitorMaxHorPixel_Type(Integer32):
    """Custom type cpqSiMonitorMaxHorPixel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMonitorMaxHorPixel_Type.__name__ = "Integer32"
_CpqSiMonitorMaxHorPixel_Object = MibTableColumn
cpqSiMonitorMaxHorPixel = _CpqSiMonitorMaxHorPixel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 8),
    _CpqSiMonitorMaxHorPixel_Type()
)
cpqSiMonitorMaxHorPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorMaxHorPixel.setStatus("mandatory")


class _CpqSiMonitorMaxVertPixel_Type(Integer32):
    """Custom type cpqSiMonitorMaxVertPixel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMonitorMaxVertPixel_Type.__name__ = "Integer32"
_CpqSiMonitorMaxVertPixel_Object = MibTableColumn
cpqSiMonitorMaxVertPixel = _CpqSiMonitorMaxVertPixel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 9),
    _CpqSiMonitorMaxVertPixel_Type()
)
cpqSiMonitorMaxVertPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorMaxVertPixel.setStatus("mandatory")


class _CpqSiMonitorMaxRefreshRate_Type(Integer32):
    """Custom type cpqSiMonitorMaxRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiMonitorMaxRefreshRate_Type.__name__ = "Integer32"
_CpqSiMonitorMaxRefreshRate_Object = MibTableColumn
cpqSiMonitorMaxRefreshRate = _CpqSiMonitorMaxRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 10),
    _CpqSiMonitorMaxRefreshRate_Type()
)
cpqSiMonitorMaxRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorMaxRefreshRate.setStatus("mandatory")


class _CpqSiMonitorManufacturer_Type(DisplayString):
    """Custom type cpqSiMonitorManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiMonitorManufacturer_Type.__name__ = "DisplayString"
_CpqSiMonitorManufacturer_Object = MibTableColumn
cpqSiMonitorManufacturer = _CpqSiMonitorManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 11),
    _CpqSiMonitorManufacturer_Type()
)
cpqSiMonitorManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorManufacturer.setStatus("mandatory")


class _CpqSiMonitorThermalCondition_Type(Integer32):
    """Custom type cpqSiMonitorThermalCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMonitorThermalCondition_Type.__name__ = "Integer32"
_CpqSiMonitorThermalCondition_Object = MibTableColumn
cpqSiMonitorThermalCondition = _CpqSiMonitorThermalCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 12),
    _CpqSiMonitorThermalCondition_Type()
)
cpqSiMonitorThermalCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorThermalCondition.setStatus("mandatory")


class _CpqSiMonitorOperationalCondition_Type(Integer32):
    """Custom type cpqSiMonitorOperationalCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiMonitorOperationalCondition_Type.__name__ = "Integer32"
_CpqSiMonitorOperationalCondition_Object = MibTableColumn
cpqSiMonitorOperationalCondition = _CpqSiMonitorOperationalCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 13),
    _CpqSiMonitorOperationalCondition_Type()
)
cpqSiMonitorOperationalCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorOperationalCondition.setStatus("mandatory")


class _CpqSiMonitorStatus_Type(Integer32):
    """Custom type cpqSiMonitorStatus based on Integer32"""
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
        *(("ok", 3),
          ("operationalFailure", 5),
          ("other", 1),
          ("thermalDegraded", 4),
          ("unknown", 2))
    )


_CpqSiMonitorStatus_Type.__name__ = "Integer32"
_CpqSiMonitorStatus_Object = MibTableColumn
cpqSiMonitorStatus = _CpqSiMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 8, 2, 1, 14),
    _CpqSiMonitorStatus_Type()
)
cpqSiMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMonitorStatus.setStatus("mandatory")
_CpqSiHotPlugSlot_ObjectIdentity = ObjectIdentity
cpqSiHotPlugSlot = _CpqSiHotPlugSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9)
)


class _CpqSiHotPlugSlotSupported_Type(Integer32):
    """Custom type cpqSiHotPlugSlotSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("other", 1),
          ("supported", 3))
    )


_CpqSiHotPlugSlotSupported_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotSupported_Object = MibScalar
cpqSiHotPlugSlotSupported = _CpqSiHotPlugSlotSupported_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 1),
    _CpqSiHotPlugSlotSupported_Type()
)
cpqSiHotPlugSlotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotSupported.setStatus("mandatory")


class _CpqSiHotPlugSlotCondition_Type(Integer32):
    """Custom type cpqSiHotPlugSlotCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiHotPlugSlotCondition_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotCondition_Object = MibScalar
cpqSiHotPlugSlotCondition = _CpqSiHotPlugSlotCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 2),
    _CpqSiHotPlugSlotCondition_Type()
)
cpqSiHotPlugSlotCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotCondition.setStatus("mandatory")
_CpqSiHotPlugSlotChangeCount_Type = Integer32
_CpqSiHotPlugSlotChangeCount_Object = MibScalar
cpqSiHotPlugSlotChangeCount = _CpqSiHotPlugSlotChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 3),
    _CpqSiHotPlugSlotChangeCount_Type()
)
cpqSiHotPlugSlotChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotChangeCount.setStatus("mandatory")
_CpqSiHotPlugSlotTable_Object = MibTable
cpqSiHotPlugSlotTable = _CpqSiHotPlugSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4)
)
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotTable.setStatus("mandatory")
_CpqSiHotPlugSlotEntry_Object = MibTableRow
cpqSiHotPlugSlotEntry = _CpqSiHotPlugSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1)
)
cpqSiHotPlugSlotEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiHotPlugSlotChassis"),
    (0, "CPQSINFO-MIB", "cpqSiHotPlugSlotIndex"),
)
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotEntry.setStatus("mandatory")


class _CpqSiHotPlugSlotChassis_Type(Integer32):
    """Custom type cpqSiHotPlugSlotChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiHotPlugSlotChassis_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotChassis_Object = MibTableColumn
cpqSiHotPlugSlotChassis = _CpqSiHotPlugSlotChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 1),
    _CpqSiHotPlugSlotChassis_Type()
)
cpqSiHotPlugSlotChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotChassis.setStatus("mandatory")


class _CpqSiHotPlugSlotIndex_Type(Integer32):
    """Custom type cpqSiHotPlugSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiHotPlugSlotIndex_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotIndex_Object = MibTableColumn
cpqSiHotPlugSlotIndex = _CpqSiHotPlugSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 2),
    _CpqSiHotPlugSlotIndex_Type()
)
cpqSiHotPlugSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotIndex.setStatus("mandatory")


class _CpqSiHotPlugSlotBoardPresent_Type(Integer32):
    """Custom type cpqSiHotPlugSlotBoardPresent based on Integer32"""
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
        *(("absent", 3),
          ("other", 1),
          ("present", 2),
          ("presentButSuspended", 4))
    )


_CpqSiHotPlugSlotBoardPresent_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotBoardPresent_Object = MibTableColumn
cpqSiHotPlugSlotBoardPresent = _CpqSiHotPlugSlotBoardPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 3),
    _CpqSiHotPlugSlotBoardPresent_Type()
)
cpqSiHotPlugSlotBoardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotBoardPresent.setStatus("mandatory")


class _CpqSiHotPlugSlotPowerState_Type(Integer32):
    """Custom type cpqSiHotPlugSlotPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("powerOff", 3),
          ("powerOn", 2))
    )


_CpqSiHotPlugSlotPowerState_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotPowerState_Object = MibTableColumn
cpqSiHotPlugSlotPowerState = _CpqSiHotPlugSlotPowerState_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 4),
    _CpqSiHotPlugSlotPowerState_Type()
)
cpqSiHotPlugSlotPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotPowerState.setStatus("mandatory")


class _CpqSiHotPlugSlotBoardCondition_Type(Integer32):
    """Custom type cpqSiHotPlugSlotBoardCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiHotPlugSlotBoardCondition_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotBoardCondition_Object = MibTableColumn
cpqSiHotPlugSlotBoardCondition = _CpqSiHotPlugSlotBoardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 5),
    _CpqSiHotPlugSlotBoardCondition_Type()
)
cpqSiHotPlugSlotBoardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotBoardCondition.setStatus("mandatory")


class _CpqSiHotPlugSlotErrorStatus_Type(Integer32):
    """Custom type cpqSiHotPlugSlotErrorStatus based on Integer32"""
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
        *(("cannotConfig", 5),
          ("functionalFailure", 9),
          ("generalError", 2),
          ("noError", 1),
          ("powerFault", 6),
          ("unexpectedPowerLoss", 7),
          ("wrongBoard", 4),
          ("wrongRevision", 3),
          ("wrongSpeed", 8))
    )


_CpqSiHotPlugSlotErrorStatus_Type.__name__ = "Integer32"
_CpqSiHotPlugSlotErrorStatus_Object = MibTableColumn
cpqSiHotPlugSlotErrorStatus = _CpqSiHotPlugSlotErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 6),
    _CpqSiHotPlugSlotErrorStatus_Type()
)
cpqSiHotPlugSlotErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotErrorStatus.setStatus("mandatory")


class _CpqSiHotPlugSlotHwLocation_Type(DisplayString):
    """Custom type cpqSiHotPlugSlotHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiHotPlugSlotHwLocation_Type.__name__ = "DisplayString"
_CpqSiHotPlugSlotHwLocation_Object = MibTableColumn
cpqSiHotPlugSlotHwLocation = _CpqSiHotPlugSlotHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 9, 4, 1, 7),
    _CpqSiHotPlugSlotHwLocation_Type()
)
cpqSiHotPlugSlotHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotHwLocation.setStatus("optional")
_CpqSiSystemBattery_ObjectIdentity = ObjectIdentity
cpqSiSystemBattery = _CpqSiSystemBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10)
)


class _CpqSiSystemBatteryOverallCondition_Type(Integer32):
    """Custom type cpqSiSystemBatteryOverallCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiSystemBatteryOverallCondition_Type.__name__ = "Integer32"
_CpqSiSystemBatteryOverallCondition_Object = MibScalar
cpqSiSystemBatteryOverallCondition = _CpqSiSystemBatteryOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 1),
    _CpqSiSystemBatteryOverallCondition_Type()
)
cpqSiSystemBatteryOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSystemBatteryOverallCondition.setStatus("mandatory")
_CpqSiSysBatteryTable_Object = MibTable
cpqSiSysBatteryTable = _CpqSiSysBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    cpqSiSysBatteryTable.setStatus("mandatory")
_CpqSiSysBatteryEntry_Object = MibTableRow
cpqSiSysBatteryEntry = _CpqSiSysBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1)
)
cpqSiSysBatteryEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiSysBatteryIndex"),
)
if mibBuilder.loadTexts:
    cpqSiSysBatteryEntry.setStatus("mandatory")


class _CpqSiSysBatteryIndex_Type(Integer32):
    """Custom type cpqSiSysBatteryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSysBatteryIndex_Type.__name__ = "Integer32"
_CpqSiSysBatteryIndex_Object = MibTableColumn
cpqSiSysBatteryIndex = _CpqSiSysBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 1),
    _CpqSiSysBatteryIndex_Type()
)
cpqSiSysBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryIndex.setStatus("mandatory")


class _CpqSiSysBatteryModel_Type(DisplayString):
    """Custom type cpqSiSysBatteryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatteryModel_Type.__name__ = "DisplayString"
_CpqSiSysBatteryModel_Object = MibTableColumn
cpqSiSysBatteryModel = _CpqSiSysBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 2),
    _CpqSiSysBatteryModel_Type()
)
cpqSiSysBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryModel.setStatus("mandatory")


class _CpqSiSysBatterySerialNum_Type(DisplayString):
    """Custom type cpqSiSysBatterySerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatterySerialNum_Type.__name__ = "DisplayString"
_CpqSiSysBatterySerialNum_Object = MibTableColumn
cpqSiSysBatterySerialNum = _CpqSiSysBatterySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 3),
    _CpqSiSysBatterySerialNum_Type()
)
cpqSiSysBatterySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatterySerialNum.setStatus("mandatory")


class _CpqSiSysBatteryAssetTag_Type(DisplayString):
    """Custom type cpqSiSysBatteryAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatteryAssetTag_Type.__name__ = "DisplayString"
_CpqSiSysBatteryAssetTag_Object = MibTableColumn
cpqSiSysBatteryAssetTag = _CpqSiSysBatteryAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 4),
    _CpqSiSysBatteryAssetTag_Type()
)
cpqSiSysBatteryAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryAssetTag.setStatus("mandatory")


class _CpqSiSysBatteryManufacturer_Type(DisplayString):
    """Custom type cpqSiSysBatteryManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatteryManufacturer_Type.__name__ = "DisplayString"
_CpqSiSysBatteryManufacturer_Object = MibTableColumn
cpqSiSysBatteryManufacturer = _CpqSiSysBatteryManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 5),
    _CpqSiSysBatteryManufacturer_Type()
)
cpqSiSysBatteryManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryManufacturer.setStatus("mandatory")


class _CpqSiSysBatteryDate_Type(OctetString):
    """Custom type cpqSiSysBatteryDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSiSysBatteryDate_Type.__name__ = "OctetString"
_CpqSiSysBatteryDate_Object = MibTableColumn
cpqSiSysBatteryDate = _CpqSiSysBatteryDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 6),
    _CpqSiSysBatteryDate_Type()
)
cpqSiSysBatteryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryDate.setStatus("mandatory")


class _CpqSiSysBatterySmartVersion_Type(DisplayString):
    """Custom type cpqSiSysBatterySmartVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatterySmartVersion_Type.__name__ = "DisplayString"
_CpqSiSysBatterySmartVersion_Object = MibTableColumn
cpqSiSysBatterySmartVersion = _CpqSiSysBatterySmartVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 7),
    _CpqSiSysBatterySmartVersion_Type()
)
cpqSiSysBatterySmartVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatterySmartVersion.setStatus("mandatory")


class _CpqSiSysBatteryCondition_Type(Integer32):
    """Custom type cpqSiSysBatteryCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiSysBatteryCondition_Type.__name__ = "Integer32"
_CpqSiSysBatteryCondition_Object = MibTableColumn
cpqSiSysBatteryCondition = _CpqSiSysBatteryCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 8),
    _CpqSiSysBatteryCondition_Type()
)
cpqSiSysBatteryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryCondition.setStatus("mandatory")


class _CpqSiSysBatteryStatus_Type(Integer32):
    """Custom type cpqSiSysBatteryStatus based on Integer32"""
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
        *(("batteryFailure", 5),
          ("capacityDegraded", 3),
          ("chargeFault", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiSysBatteryStatus_Type.__name__ = "Integer32"
_CpqSiSysBatteryStatus_Object = MibTableColumn
cpqSiSysBatteryStatus = _CpqSiSysBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 9),
    _CpqSiSysBatteryStatus_Type()
)
cpqSiSysBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryStatus.setStatus("mandatory")


class _CpqSiSysBatteryChemistry_Type(Integer32):
    """Custom type cpqSiSysBatteryChemistry based on Integer32"""
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
        *(("lead-Acid", 3),
          ("lithium-Ion", 6),
          ("lithium-Polymer", 8),
          ("nickel-Cadmium", 4),
          ("nickel-Metal-Hydride", 5),
          ("other", 1),
          ("unknown", 2),
          ("zinc-Air", 7))
    )


_CpqSiSysBatteryChemistry_Type.__name__ = "Integer32"
_CpqSiSysBatteryChemistry_Object = MibTableColumn
cpqSiSysBatteryChemistry = _CpqSiSysBatteryChemistry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 10),
    _CpqSiSysBatteryChemistry_Type()
)
cpqSiSysBatteryChemistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryChemistry.setStatus("mandatory")


class _CpqSiSysBatteryRemainingCap_Type(Integer32):
    """Custom type cpqSiSysBatteryRemainingCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSysBatteryRemainingCap_Type.__name__ = "Integer32"
_CpqSiSysBatteryRemainingCap_Object = MibTableColumn
cpqSiSysBatteryRemainingCap = _CpqSiSysBatteryRemainingCap_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 11),
    _CpqSiSysBatteryRemainingCap_Type()
)
cpqSiSysBatteryRemainingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryRemainingCap.setStatus("mandatory")


class _CpqSiSysBatteryFirmwareRevision_Type(Integer32):
    """Custom type cpqSiSysBatteryFirmwareRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiSysBatteryFirmwareRevision_Type.__name__ = "Integer32"
_CpqSiSysBatteryFirmwareRevision_Object = MibTableColumn
cpqSiSysBatteryFirmwareRevision = _CpqSiSysBatteryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 12),
    _CpqSiSysBatteryFirmwareRevision_Type()
)
cpqSiSysBatteryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryFirmwareRevision.setStatus("mandatory")


class _CpqSiSysBatteryHardwareRevision_Type(Integer32):
    """Custom type cpqSiSysBatteryHardwareRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSiSysBatteryHardwareRevision_Type.__name__ = "Integer32"
_CpqSiSysBatteryHardwareRevision_Object = MibTableColumn
cpqSiSysBatteryHardwareRevision = _CpqSiSysBatteryHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 13),
    _CpqSiSysBatteryHardwareRevision_Type()
)
cpqSiSysBatteryHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryHardwareRevision.setStatus("mandatory")


class _CpqSiSysBatteryFullCap_Type(Integer32):
    """Custom type cpqSiSysBatteryFullCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSysBatteryFullCap_Type.__name__ = "Integer32"
_CpqSiSysBatteryFullCap_Object = MibTableColumn
cpqSiSysBatteryFullCap = _CpqSiSysBatteryFullCap_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 14),
    _CpqSiSysBatteryFullCap_Type()
)
cpqSiSysBatteryFullCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryFullCap.setStatus("mandatory")


class _CpqSiSysBatteryDesignCap_Type(Integer32):
    """Custom type cpqSiSysBatteryDesignCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSiSysBatteryDesignCap_Type.__name__ = "Integer32"
_CpqSiSysBatteryDesignCap_Object = MibTableColumn
cpqSiSysBatteryDesignCap = _CpqSiSysBatteryDesignCap_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 15),
    _CpqSiSysBatteryDesignCap_Type()
)
cpqSiSysBatteryDesignCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryDesignCap.setStatus("mandatory")


class _CpqSiSysBatteryHwLocation_Type(DisplayString):
    """Custom type cpqSiSysBatteryHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiSysBatteryHwLocation_Type.__name__ = "DisplayString"
_CpqSiSysBatteryHwLocation_Object = MibTableColumn
cpqSiSysBatteryHwLocation = _CpqSiSysBatteryHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 10, 2, 1, 16),
    _CpqSiSysBatteryHwLocation_Type()
)
cpqSiSysBatteryHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiSysBatteryHwLocation.setStatus("optional")
_CpqSiDockingStation_ObjectIdentity = ObjectIdentity
cpqSiDockingStation = _CpqSiDockingStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 11)
)


class _CpqSiDockingStationStatus_Type(Integer32):
    """Custom type cpqSiDockingStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("docked", 2),
          ("notSupported", 1),
          ("undocked", 3))
    )


_CpqSiDockingStationStatus_Type.__name__ = "Integer32"
_CpqSiDockingStationStatus_Object = MibScalar
cpqSiDockingStationStatus = _CpqSiDockingStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 11, 1),
    _CpqSiDockingStationStatus_Type()
)
cpqSiDockingStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiDockingStationStatus.setStatus("mandatory")


class _CpqSiDockingStationSerialNum_Type(DisplayString):
    """Custom type cpqSiDockingStationSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiDockingStationSerialNum_Type.__name__ = "DisplayString"
_CpqSiDockingStationSerialNum_Object = MibScalar
cpqSiDockingStationSerialNum = _CpqSiDockingStationSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 11, 2),
    _CpqSiDockingStationSerialNum_Type()
)
cpqSiDockingStationSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiDockingStationSerialNum.setStatus("mandatory")


class _CpqSiDockingStationModel_Type(DisplayString):
    """Custom type cpqSiDockingStationModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiDockingStationModel_Type.__name__ = "DisplayString"
_CpqSiDockingStationModel_Object = MibScalar
cpqSiDockingStationModel = _CpqSiDockingStationModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 11, 3),
    _CpqSiDockingStationModel_Type()
)
cpqSiDockingStationModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiDockingStationModel.setStatus("mandatory")


class _CpqSiDockingStationAssetTag_Type(DisplayString):
    """Custom type cpqSiDockingStationAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiDockingStationAssetTag_Type.__name__ = "DisplayString"
_CpqSiDockingStationAssetTag_Object = MibScalar
cpqSiDockingStationAssetTag = _CpqSiDockingStationAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 11, 4),
    _CpqSiDockingStationAssetTag_Type()
)
cpqSiDockingStationAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiDockingStationAssetTag.setStatus("mandatory")
_CpqSiFru_ObjectIdentity = ObjectIdentity
cpqSiFru = _CpqSiFru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12)
)
_CpqSiFruTable_Object = MibTable
cpqSiFruTable = _CpqSiFruTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    cpqSiFruTable.setStatus("mandatory")
_CpqSiFruEntry_Object = MibTableRow
cpqSiFruEntry = _CpqSiFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1)
)
cpqSiFruEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiFruIndex"),
)
if mibBuilder.loadTexts:
    cpqSiFruEntry.setStatus("mandatory")
_CpqSiFruIndex_Type = Integer32
_CpqSiFruIndex_Object = MibTableColumn
cpqSiFruIndex = _CpqSiFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 1),
    _CpqSiFruIndex_Type()
)
cpqSiFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruIndex.setStatus("mandatory")


class _CpqSiFruType_Type(Integer32):
    """Custom type cpqSiFruType based on Integer32"""
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
        *(("chassis", 10),
          ("fan", 11),
          ("ioCard", 12),
          ("memoryCard", 5),
          ("memoryModule", 6),
          ("motherBoard", 3),
          ("other", 2),
          ("peripheralDevice", 7),
          ("powerSupply", 9),
          ("processor", 4),
          ("systemBusBridge", 8),
          ("unknown", 1))
    )


_CpqSiFruType_Type.__name__ = "Integer32"
_CpqSiFruType_Object = MibTableColumn
cpqSiFruType = _CpqSiFruType_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 2),
    _CpqSiFruType_Type()
)
cpqSiFruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruType.setStatus("mandatory")
_CpqSiFruDescr_Type = DisplayString
_CpqSiFruDescr_Object = MibTableColumn
cpqSiFruDescr = _CpqSiFruDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 3),
    _CpqSiFruDescr_Type()
)
cpqSiFruDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiFruDescr.setStatus("mandatory")
_CpqSiFruVendor_Type = DisplayString
_CpqSiFruVendor_Object = MibTableColumn
cpqSiFruVendor = _CpqSiFruVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 4),
    _CpqSiFruVendor_Type()
)
cpqSiFruVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruVendor.setStatus("mandatory")
_CpqSiFruPartNumber_Type = DisplayString
_CpqSiFruPartNumber_Object = MibTableColumn
cpqSiFruPartNumber = _CpqSiFruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 5),
    _CpqSiFruPartNumber_Type()
)
cpqSiFruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruPartNumber.setStatus("mandatory")
_CpqSiFruRevision_Type = DisplayString
_CpqSiFruRevision_Object = MibTableColumn
cpqSiFruRevision = _CpqSiFruRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 6),
    _CpqSiFruRevision_Type()
)
cpqSiFruRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruRevision.setStatus("mandatory")
_CpqSiFruFirmwareRevision_Type = DisplayString
_CpqSiFruFirmwareRevision_Object = MibTableColumn
cpqSiFruFirmwareRevision = _CpqSiFruFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 7),
    _CpqSiFruFirmwareRevision_Type()
)
cpqSiFruFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruFirmwareRevision.setStatus("mandatory")
_CpqSiFruSerialNumber_Type = DisplayString
_CpqSiFruSerialNumber_Object = MibTableColumn
cpqSiFruSerialNumber = _CpqSiFruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 8),
    _CpqSiFruSerialNumber_Type()
)
cpqSiFruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruSerialNumber.setStatus("mandatory")
_CpqSiFruAssetNo_Type = DisplayString
_CpqSiFruAssetNo_Object = MibTableColumn
cpqSiFruAssetNo = _CpqSiFruAssetNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 9),
    _CpqSiFruAssetNo_Type()
)
cpqSiFruAssetNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSiFruAssetNo.setStatus("mandatory")


class _CpqSiFruClass_Type(Integer32):
    """Custom type cpqSiFruClass based on Integer32"""
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
        *(("currentBoardInSlot", 3),
          ("other", 2),
          ("parentBoard", 5),
          ("priorBoardInSlot", 4),
          ("priorParentBoard", 6),
          ("priorParentSystem", 7),
          ("unknown", 1))
    )


_CpqSiFruClass_Type.__name__ = "Integer32"
_CpqSiFruClass_Object = MibTableColumn
cpqSiFruClass = _CpqSiFruClass_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 10),
    _CpqSiFruClass_Type()
)
cpqSiFruClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruClass.setStatus("mandatory")
_CpqSiFruSlotNumber_Type = DisplayString
_CpqSiFruSlotNumber_Object = MibTableColumn
cpqSiFruSlotNumber = _CpqSiFruSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 11),
    _CpqSiFruSlotNumber_Type()
)
cpqSiFruSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruSlotNumber.setStatus("mandatory")
_CpqSiFruSubAssemblyNumber_Type = Integer32
_CpqSiFruSubAssemblyNumber_Object = MibTableColumn
cpqSiFruSubAssemblyNumber = _CpqSiFruSubAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 12),
    _CpqSiFruSubAssemblyNumber_Type()
)
cpqSiFruSubAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruSubAssemblyNumber.setStatus("mandatory")
_CpqSiFruAssemblyNumber_Type = Integer32
_CpqSiFruAssemblyNumber_Object = MibTableColumn
cpqSiFruAssemblyNumber = _CpqSiFruAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 13),
    _CpqSiFruAssemblyNumber_Type()
)
cpqSiFruAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruAssemblyNumber.setStatus("mandatory")
_CpqSiFruChassisNumber_Type = Integer32
_CpqSiFruChassisNumber_Object = MibTableColumn
cpqSiFruChassisNumber = _CpqSiFruChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 14),
    _CpqSiFruChassisNumber_Type()
)
cpqSiFruChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruChassisNumber.setStatus("mandatory")
_CpqSiFruPositionNumber_Type = Integer32
_CpqSiFruPositionNumber_Object = MibTableColumn
cpqSiFruPositionNumber = _CpqSiFruPositionNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 15),
    _CpqSiFruPositionNumber_Type()
)
cpqSiFruPositionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruPositionNumber.setStatus("mandatory")
_CpqSiFruCabinetIDNumber_Type = Integer32
_CpqSiFruCabinetIDNumber_Object = MibTableColumn
cpqSiFruCabinetIDNumber = _CpqSiFruCabinetIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 16),
    _CpqSiFruCabinetIDNumber_Type()
)
cpqSiFruCabinetIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruCabinetIDNumber.setStatus("mandatory")
_CpqSiFruSiteLocation_Type = Integer32
_CpqSiFruSiteLocation_Object = MibTableColumn
cpqSiFruSiteLocation = _CpqSiFruSiteLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 17),
    _CpqSiFruSiteLocation_Type()
)
cpqSiFruSiteLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruSiteLocation.setStatus("mandatory")


class _CpqSiFruDiagStatus_Type(Integer32):
    """Custom type cpqSiFruDiagStatus based on Integer32"""
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
        *(("degraded", 3),
          ("disabled", 5),
          ("failed", 4),
          ("ok", 2),
          ("unknown", 1))
    )


_CpqSiFruDiagStatus_Type.__name__ = "Integer32"
_CpqSiFruDiagStatus_Object = MibTableColumn
cpqSiFruDiagStatus = _CpqSiFruDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 18),
    _CpqSiFruDiagStatus_Type()
)
cpqSiFruDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruDiagStatus.setStatus("mandatory")
_CpqSiFruExtendedDiagStatus_Type = Integer32
_CpqSiFruExtendedDiagStatus_Object = MibTableColumn
cpqSiFruExtendedDiagStatus = _CpqSiFruExtendedDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 19),
    _CpqSiFruExtendedDiagStatus_Type()
)
cpqSiFruExtendedDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruExtendedDiagStatus.setStatus("mandatory")
_CpqSiFruCellTablePtr_Type = Integer32
_CpqSiFruCellTablePtr_Object = MibTableColumn
cpqSiFruCellTablePtr = _CpqSiFruCellTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 20),
    _CpqSiFruCellTablePtr_Type()
)
cpqSiFruCellTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruCellTablePtr.setStatus("optional")
_CpqSiFruIOCTablePtr_Type = Integer32
_CpqSiFruIOCTablePtr_Object = MibTableColumn
cpqSiFruIOCTablePtr = _CpqSiFruIOCTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 21),
    _CpqSiFruIOCTablePtr_Type()
)
cpqSiFruIOCTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruIOCTablePtr.setStatus("optional")


class _CpqSiFruFileId_Type(DisplayString):
    """Custom type cpqSiFruFileId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiFruFileId_Type.__name__ = "DisplayString"
_CpqSiFruFileId_Object = MibTableColumn
cpqSiFruFileId = _CpqSiFruFileId_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 22),
    _CpqSiFruFileId_Type()
)
cpqSiFruFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruFileId.setStatus("optional")


class _CpqSiFruScanRev_Type(DisplayString):
    """Custom type cpqSiFruScanRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSiFruScanRev_Type.__name__ = "DisplayString"
_CpqSiFruScanRev_Object = MibTableColumn
cpqSiFruScanRev = _CpqSiFruScanRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 12, 1, 1, 23),
    _CpqSiFruScanRev_Type()
)
cpqSiFruScanRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiFruScanRev.setStatus("optional")
_CpqSiRackEnclosure_ObjectIdentity = ObjectIdentity
cpqSiRackEnclosure = _CpqSiRackEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13)
)
_CpqSiRackEnclosureMgrTable_Object = MibTable
cpqSiRackEnclosureMgrTable = _CpqSiRackEnclosureMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrTable.setStatus("mandatory")
_CpqSiRackEnclosureMgrEntry_Object = MibTableRow
cpqSiRackEnclosureMgrEntry = _CpqSiRackEnclosureMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1)
)
cpqSiRackEnclosureMgrEntry.setIndexNames(
    (0, "CPQSINFO-MIB", "cpqSiRackEnclosureMgrIndex"),
)
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrEntry.setStatus("mandatory")
_CpqSiRackEnclosureMgrIndex_Type = Integer32
_CpqSiRackEnclosureMgrIndex_Object = MibTableColumn
cpqSiRackEnclosureMgrIndex = _CpqSiRackEnclosureMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 1),
    _CpqSiRackEnclosureMgrIndex_Type()
)
cpqSiRackEnclosureMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrIndex.setStatus("mandatory")


class _CpqSiRackEnclosureMgrType_Type(Integer32):
    """Custom type cpqSiRackEnclosureMgrType based on Integer32"""
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
        *(("enclosureManagement", 3),
          ("noEnclosureManagement", 2),
          ("onboardAdminManagement", 4),
          ("other", 1))
    )


_CpqSiRackEnclosureMgrType_Type.__name__ = "Integer32"
_CpqSiRackEnclosureMgrType_Object = MibTableColumn
cpqSiRackEnclosureMgrType = _CpqSiRackEnclosureMgrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 2),
    _CpqSiRackEnclosureMgrType_Type()
)
cpqSiRackEnclosureMgrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrType.setStatus("mandatory")
_CpqSiRackEnclosureMgrIpAddr_Type = DisplayString
_CpqSiRackEnclosureMgrIpAddr_Object = MibTableColumn
cpqSiRackEnclosureMgrIpAddr = _CpqSiRackEnclosureMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 3),
    _CpqSiRackEnclosureMgrIpAddr_Type()
)
cpqSiRackEnclosureMgrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrIpAddr.setStatus("mandatory")
_CpqSiRackEnclosureMgrWebLink_Type = DisplayString
_CpqSiRackEnclosureMgrWebLink_Object = MibTableColumn
cpqSiRackEnclosureMgrWebLink = _CpqSiRackEnclosureMgrWebLink_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 4),
    _CpqSiRackEnclosureMgrWebLink_Type()
)
cpqSiRackEnclosureMgrWebLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrWebLink.setStatus("mandatory")


class _CpqSiRackEnclosureMgrCondition_Type(Integer32):
    """Custom type cpqSiRackEnclosureMgrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSiRackEnclosureMgrCondition_Type.__name__ = "Integer32"
_CpqSiRackEnclosureMgrCondition_Object = MibTableColumn
cpqSiRackEnclosureMgrCondition = _CpqSiRackEnclosureMgrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 5),
    _CpqSiRackEnclosureMgrCondition_Type()
)
cpqSiRackEnclosureMgrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrCondition.setStatus("mandatory")
_CpqSiRackEnclosureMgrSerialNumber_Type = DisplayString
_CpqSiRackEnclosureMgrSerialNumber_Object = MibTableColumn
cpqSiRackEnclosureMgrSerialNumber = _CpqSiRackEnclosureMgrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 6),
    _CpqSiRackEnclosureMgrSerialNumber_Type()
)
cpqSiRackEnclosureMgrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrSerialNumber.setStatus("mandatory")
_CpqSiRackEnclosureMgrModel_Type = DisplayString
_CpqSiRackEnclosureMgrModel_Object = MibTableColumn
cpqSiRackEnclosureMgrModel = _CpqSiRackEnclosureMgrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 7),
    _CpqSiRackEnclosureMgrModel_Type()
)
cpqSiRackEnclosureMgrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrModel.setStatus("optional")
_CpqSiRackEnclosureMgrName_Type = DisplayString
_CpqSiRackEnclosureMgrName_Object = MibTableColumn
cpqSiRackEnclosureMgrName = _CpqSiRackEnclosureMgrName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 8),
    _CpqSiRackEnclosureMgrName_Type()
)
cpqSiRackEnclosureMgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrName.setStatus("optional")
_CpqSiRackEnclosureMgrFwRev_Type = DisplayString
_CpqSiRackEnclosureMgrFwRev_Object = MibTableColumn
cpqSiRackEnclosureMgrFwRev = _CpqSiRackEnclosureMgrFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 9),
    _CpqSiRackEnclosureMgrFwRev_Type()
)
cpqSiRackEnclosureMgrFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrFwRev.setStatus("optional")
_CpqSiRackEnclosureMgrProductID_Type = DisplayString
_CpqSiRackEnclosureMgrProductID_Object = MibTableColumn
cpqSiRackEnclosureMgrProductID = _CpqSiRackEnclosureMgrProductID_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 10),
    _CpqSiRackEnclosureMgrProductID_Type()
)
cpqSiRackEnclosureMgrProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrProductID.setStatus("optional")
_CpqSiRackEnclosureMgrUUID_Type = DisplayString
_CpqSiRackEnclosureMgrUUID_Object = MibTableColumn
cpqSiRackEnclosureMgrUUID = _CpqSiRackEnclosureMgrUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 13, 1, 1, 11),
    _CpqSiRackEnclosureMgrUUID_Type()
)
cpqSiRackEnclosureMgrUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackEnclosureMgrUUID.setStatus("optional")
_CpqSiServerBlade_ObjectIdentity = ObjectIdentity
cpqSiServerBlade = _CpqSiServerBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 14)
)
_CpqSiServerBladeEnclosureBayNumber_Type = Integer32
_CpqSiServerBladeEnclosureBayNumber_Object = MibScalar
cpqSiServerBladeEnclosureBayNumber = _CpqSiServerBladeEnclosureBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 14, 1),
    _CpqSiServerBladeEnclosureBayNumber_Type()
)
cpqSiServerBladeEnclosureBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiServerBladeEnclosureBayNumber.setStatus("optional")


class _CpqSiServerBladeHeight_Type(Integer32):
    """Custom type cpqSiServerBladeHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullHeightBlade", 3),
          ("halfHeightBlade", 2),
          ("unknown", 1))
    )


_CpqSiServerBladeHeight_Type.__name__ = "Integer32"
_CpqSiServerBladeHeight_Object = MibScalar
cpqSiServerBladeHeight = _CpqSiServerBladeHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 14, 2),
    _CpqSiServerBladeHeight_Type()
)
cpqSiServerBladeHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiServerBladeHeight.setStatus("optional")


class _CpqSiServerBladeWidth_Type(Integer32):
    """Custom type cpqSiServerBladeWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doubleWide", 3),
          ("singleWide", 2),
          ("unknown", 1))
    )


_CpqSiServerBladeWidth_Type.__name__ = "Integer32"
_CpqSiServerBladeWidth_Object = MibScalar
cpqSiServerBladeWidth = _CpqSiServerBladeWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 14, 3),
    _CpqSiServerBladeWidth_Type()
)
cpqSiServerBladeWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiServerBladeWidth.setStatus("optional")
_CpqSiRack_ObjectIdentity = ObjectIdentity
cpqSiRack = _CpqSiRack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 15)
)
_CpqSiRackName_Type = DisplayString
_CpqSiRackName_Object = MibScalar
cpqSiRackName = _CpqSiRackName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 15, 1),
    _CpqSiRackName_Type()
)
cpqSiRackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackName.setStatus("optional")
_CpqSiRackUUID_Type = DisplayString
_CpqSiRackUUID_Object = MibScalar
cpqSiRackUUID = _CpqSiRackUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 15, 2),
    _CpqSiRackUUID_Type()
)
cpqSiRackUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiRackUUID.setStatus("optional")
_CpqSiMP_ObjectIdentity = ObjectIdentity
cpqSiMP = _CpqSiMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 16)
)
_CpqSiMPHostName_Type = DisplayString
_CpqSiMPHostName_Object = MibScalar
cpqSiMPHostName = _CpqSiMPHostName_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 16, 1),
    _CpqSiMPHostName_Type()
)
cpqSiMPHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMPHostName.setStatus("optional")


class _CpqSiMPHealthStatus_Type(Integer32):
    """Custom type cpqSiMPHealthStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("unknown", 1))
    )


_CpqSiMPHealthStatus_Type.__name__ = "Integer32"
_CpqSiMPHealthStatus_Object = MibScalar
cpqSiMPHealthStatus = _CpqSiMPHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 2, 2, 16, 2),
    _CpqSiMPHealthStatus_Type()
)
cpqSiMPHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSiMPHealthStatus.setStatus("optional")

# Managed Objects groups


# Notification objects

cpqSiHoodRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2001)
)
cpqSiHoodRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSiHoodRemoved.setStatus(
        ""
    )

cpqSiMonitorConditionOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2002)
)
cpqSiMonitorConditionOK.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMonitorIndex"))
)
if mibBuilder.loadTexts:
    cpqSiMonitorConditionOK.setStatus(
        ""
    )

cpqSiMonitorConditionDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2003)
)
cpqSiMonitorConditionDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMonitorIndex"))
)
if mibBuilder.loadTexts:
    cpqSiMonitorConditionDegraded.setStatus(
        ""
    )

cpqSiMonitorConditionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2004)
)
cpqSiMonitorConditionFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMonitorIndex"))
)
if mibBuilder.loadTexts:
    cpqSiMonitorConditionFailed.setStatus(
        ""
    )

cpqSiCorrMemErrStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2005)
)
cpqSiCorrMemErrStatusDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMemErrorIndex"))
)
if mibBuilder.loadTexts:
    cpqSiCorrMemErrStatusDegraded.setStatus(
        ""
    )

cpqSiCorrMemErrStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2006)
)
cpqSiCorrMemErrStatusOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMemErrorIndex"))
)
if mibBuilder.loadTexts:
    cpqSiCorrMemErrStatusOk.setStatus(
        ""
    )

cpqSiMemConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2007)
)
cpqSiMemConfigChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiMemConfigChangeData"))
)
if mibBuilder.loadTexts:
    cpqSiMemConfigChange.setStatus(
        ""
    )

cpqSiHotPlugSlotBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2008)
)
cpqSiHotPlugSlotBoardRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotChassis"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotBoardRemoved.setStatus(
        ""
    )

cpqSiHotPlugSlotBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2009)
)
cpqSiHotPlugSlotBoardInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotChassis"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotBoardInserted.setStatus(
        ""
    )

cpqSiHotPlugSlotPowerUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2010)
)
cpqSiHotPlugSlotPowerUpFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotChassis"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotIndex"),
        ("CPQSINFO-MIB", "cpqSiHotPlugSlotErrorStatus"))
)
if mibBuilder.loadTexts:
    cpqSiHotPlugSlotPowerUpFailed.setStatus(
        ""
    )

cpqSiSysBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2011)
)
cpqSiSysBatteryFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiSysBatteryIndex"),
        ("CPQSINFO-MIB", "cpqSiSysBatterySerialNum"))
)
if mibBuilder.loadTexts:
    cpqSiSysBatteryFailure.setStatus(
        ""
    )

cpqSiSysBatteryChargingDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2012)
)
cpqSiSysBatteryChargingDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiSysBatteryIndex"),
        ("CPQSINFO-MIB", "cpqSiSysBatterySerialNum"))
)
if mibBuilder.loadTexts:
    cpqSiSysBatteryChargingDegraded.setStatus(
        ""
    )

cpqSiSysBatteryCalibrationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 2013)
)
cpqSiSysBatteryCalibrationError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiSysBatteryIndex"),
        ("CPQSINFO-MIB", "cpqSiSysBatterySerialNum"))
)
if mibBuilder.loadTexts:
    cpqSiSysBatteryCalibrationError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSINFO-MIB",
    **{"cpqSiHoodRemoved": cpqSiHoodRemoved,
       "cpqSiMonitorConditionOK": cpqSiMonitorConditionOK,
       "cpqSiMonitorConditionDegraded": cpqSiMonitorConditionDegraded,
       "cpqSiMonitorConditionFailed": cpqSiMonitorConditionFailed,
       "cpqSiCorrMemErrStatusDegraded": cpqSiCorrMemErrStatusDegraded,
       "cpqSiCorrMemErrStatusOk": cpqSiCorrMemErrStatusOk,
       "cpqSiMemConfigChange": cpqSiMemConfigChange,
       "cpqSiHotPlugSlotBoardRemoved": cpqSiHotPlugSlotBoardRemoved,
       "cpqSiHotPlugSlotBoardInserted": cpqSiHotPlugSlotBoardInserted,
       "cpqSiHotPlugSlotPowerUpFailed": cpqSiHotPlugSlotPowerUpFailed,
       "cpqSiSysBatteryFailure": cpqSiSysBatteryFailure,
       "cpqSiSysBatteryChargingDegraded": cpqSiSysBatteryChargingDegraded,
       "cpqSiSysBatteryCalibrationError": cpqSiSysBatteryCalibrationError,
       "cpqSystemInfo": cpqSystemInfo,
       "cpqSiMibRev": cpqSiMibRev,
       "cpqSiMibRevMajor": cpqSiMibRevMajor,
       "cpqSiMibRevMinor": cpqSiMibRevMinor,
       "cpqSiMibCondition": cpqSiMibCondition,
       "cpqSiComponent": cpqSiComponent,
       "cpqSiInterface": cpqSiInterface,
       "cpqSiOsCommon": cpqSiOsCommon,
       "cpqSiOsCommonPollFreq": cpqSiOsCommonPollFreq,
       "cpqSiOsCommonModuleTable": cpqSiOsCommonModuleTable,
       "cpqSiOsCommonModuleEntry": cpqSiOsCommonModuleEntry,
       "cpqSiOsCommonModuleIndex": cpqSiOsCommonModuleIndex,
       "cpqSiOsCommonModuleName": cpqSiOsCommonModuleName,
       "cpqSiOsCommonModuleVersion": cpqSiOsCommonModuleVersion,
       "cpqSiOsCommonModuleDate": cpqSiOsCommonModuleDate,
       "cpqSiOsCommonModulePurpose": cpqSiOsCommonModulePurpose,
       "cpqSiAsset": cpqSiAsset,
       "cpqSiSysSerialNum": cpqSiSysSerialNum,
       "cpqSiFormFactor": cpqSiFormFactor,
       "cpqSiAssetTag": cpqSiAssetTag,
       "cpqSiOwnershipTag": cpqSiOwnershipTag,
       "cpqSiSysServiceNum": cpqSiSysServiceNum,
       "cpqSiSysProductId": cpqSiSysProductId,
       "cpqSiAssetTagMaxLength": cpqSiAssetTagMaxLength,
       "cpqSiVirtualSystemTable": cpqSiVirtualSystemTable,
       "cpqSiVirtualSystemEntry": cpqSiVirtualSystemEntry,
       "cpqSiVirtualSystemIndex": cpqSiVirtualSystemIndex,
       "cpqSiVirtualSystemSerialNumber": cpqSiVirtualSystemSerialNumber,
       "cpqSiVirtualSystemUUID": cpqSiVirtualSystemUUID,
       "cpqSiSecurity": cpqSiSecurity,
       "cpqSiPowerOnPassword": cpqSiPowerOnPassword,
       "cpqSiNetServerMode": cpqSiNetServerMode,
       "cpqSiQuickLockPassword": cpqSiQuickLockPassword,
       "cpqSiQuickBlank": cpqSiQuickBlank,
       "cpqSiDisketteBootControl": cpqSiDisketteBootControl,
       "cpqSiSerialPortAControl": cpqSiSerialPortAControl,
       "cpqSiSerialPortBControl": cpqSiSerialPortBControl,
       "cpqSiParallelPortControl": cpqSiParallelPortControl,
       "cpqSiFloppyDiskControl": cpqSiFloppyDiskControl,
       "cpqSiFixedDiskControl": cpqSiFixedDiskControl,
       "cpqSiHoodRemovedTime": cpqSiHoodRemovedTime,
       "cpqSiHoodSensorConfiguration": cpqSiHoodSensorConfiguration,
       "cpqSiSmartCoverLockStatus": cpqSiSmartCoverLockStatus,
       "cpqSiUSBPortControl": cpqSiUSBPortControl,
       "cpqSiSystemBoard": cpqSiSystemBoard,
       "cpqSiProductId": cpqSiProductId,
       "cpqSiProductName": cpqSiProductName,
       "cpqSiAuxiliaryInput": cpqSiAuxiliaryInput,
       "cpqSiMemModuleTable": cpqSiMemModuleTable,
       "cpqSiMemModuleEntry": cpqSiMemModuleEntry,
       "cpqSiMemBoardIndex": cpqSiMemBoardIndex,
       "cpqSiMemModuleIndex": cpqSiMemModuleIndex,
       "cpqSiMemModuleSize": cpqSiMemModuleSize,
       "cpqSiMemModuleType": cpqSiMemModuleType,
       "cpqSiMemModuleSpeed": cpqSiMemModuleSpeed,
       "cpqSiMemModuleTechnology": cpqSiMemModuleTechnology,
       "cpqSiMemModuleManufacturer": cpqSiMemModuleManufacturer,
       "cpqSiMemModulePartNo": cpqSiMemModulePartNo,
       "cpqSiMemModuleDate": cpqSiMemModuleDate,
       "cpqSiMemModuleSerialNo": cpqSiMemModuleSerialNo,
       "cpqSiMemModuleECCStatus": cpqSiMemModuleECCStatus,
       "cpqSiMemModuleHwLocation": cpqSiMemModuleHwLocation,
       "cpqSiMemModuleFrequency": cpqSiMemModuleFrequency,
       "cpqSiMemModuleCellTablePtr": cpqSiMemModuleCellTablePtr,
       "cpqSiMemModuleCellStatus": cpqSiMemModuleCellStatus,
       "cpqSiMemModulePartNoMfgr": cpqSiMemModulePartNoMfgr,
       "cpqSiMemModuleSerialNoMfgr": cpqSiMemModuleSerialNoMfgr,
       "cpqSiSystemId": cpqSiSystemId,
       "cpqSiSystemCpuId": cpqSiSystemCpuId,
       "cpqSiFlashRomSupport": cpqSiFlashRomSupport,
       "cpqSiQuickTestRomDate": cpqSiQuickTestRomDate,
       "cpqSiReboot": cpqSiReboot,
       "cpqSiProcMicroPatchTable": cpqSiProcMicroPatchTable,
       "cpqSiProcMicroPatchEntry": cpqSiProcMicroPatchEntry,
       "cpqSiProcMicroPatchIndex": cpqSiProcMicroPatchIndex,
       "cpqSiProcMicroPatchId": cpqSiProcMicroPatchId,
       "cpqSiProcMicroPatchDate": cpqSiProcMicroPatchDate,
       "cpqSiProcMicroPatchFamily": cpqSiProcMicroPatchFamily,
       "cpqSiPowerMgmtStatus": cpqSiPowerMgmtStatus,
       "cpqSiRebootFlags": cpqSiRebootFlags,
       "cpqSiMemErrorIndex": cpqSiMemErrorIndex,
       "cpqSiMemECCCondition": cpqSiMemECCCondition,
       "cpqSiMemConfigChangeData": cpqSiMemConfigChangeData,
       "cpqSiServerSystemId": cpqSiServerSystemId,
       "cpqSiPowerScheme": cpqSiPowerScheme,
       "cpqSiPowerSchemeName": cpqSiPowerSchemeName,
       "cpqSiCurrentPerformanceStatePointer": cpqSiCurrentPerformanceStatePointer,
       "cpqSiMinPerformanceState": cpqSiMinPerformanceState,
       "cpqSiMaxPerformanceState": cpqSiMaxPerformanceState,
       "cpqSiPerfStateTable": cpqSiPerfStateTable,
       "cpqSiPerfStateEntry": cpqSiPerfStateEntry,
       "cpqSiPerfStateIndex": cpqSiPerfStateIndex,
       "cpqSiPerfState": cpqSiPerfState,
       "cpqSiPerfStateCpuFrequency": cpqSiPerfStateCpuFrequency,
       "cpqSiPerfStateCpuPower": cpqSiPerfStateCpuPower,
       "cpqSiTPMmodule": cpqSiTPMmodule,
       "cpqSiBoardRev": cpqSiBoardRev,
       "cpqSiCurRevDate": cpqSiCurRevDate,
       "cpqSiPrevRevDate": cpqSiPrevRevDate,
       "cpqSiBoardRevTable": cpqSiBoardRevTable,
       "cpqSiBoardRevEntry": cpqSiBoardRevEntry,
       "cpqSiBoardRevSlotIndex": cpqSiBoardRevSlotIndex,
       "cpqSiBoardRevIndex": cpqSiBoardRevIndex,
       "cpqSiBoardRevId": cpqSiBoardRevId,
       "cpqSiBoardRevCur": cpqSiBoardRevCur,
       "cpqSiBoardRevPrev": cpqSiBoardRevPrev,
       "cpqSiBoardRevHwLocation": cpqSiBoardRevHwLocation,
       "cpqSiFirmwareRevTable": cpqSiFirmwareRevTable,
       "cpqSiFirmwareRevEntry": cpqSiFirmwareRevEntry,
       "cpqSiFirmwareRevIndex": cpqSiFirmwareRevIndex,
       "cpqSiFirmwareRevDesc": cpqSiFirmwareRevDesc,
       "cpqSiFirmwareRevString": cpqSiFirmwareRevString,
       "cpqSiFirmwareRevCellTablePtr": cpqSiFirmwareRevCellTablePtr,
       "cpqSiFirmwareLocation": cpqSiFirmwareLocation,
       "cpqSiFirmwareStatus": cpqSiFirmwareStatus,
       "cpqSiFirmwareCfgTable": cpqSiFirmwareCfgTable,
       "cpqSiFirmwareCfgEntry": cpqSiFirmwareCfgEntry,
       "cpqSiFirmwareCfgName": cpqSiFirmwareCfgName,
       "cpqSiFirmwareCfgValue": cpqSiFirmwareCfgValue,
       "cpqSiRackServer": cpqSiRackServer,
       "cpqSiRackServerShutdownRole": cpqSiRackServerShutdownRole,
       "cpqSiRackServerMasterName": cpqSiRackServerMasterName,
       "cpqSiVideo": cpqSiVideo,
       "cpqSiVideoEdidRaw": cpqSiVideoEdidRaw,
       "cpqSiVideoDesc": cpqSiVideoDesc,
       "cpqSiVideoSerialNumber": cpqSiVideoSerialNumber,
       "cpqSiVideoManufactureDate": cpqSiVideoManufactureDate,
       "cpqSiVideoHeight": cpqSiVideoHeight,
       "cpqSiVideoWidth": cpqSiVideoWidth,
       "cpqSiVideoMaxHorPixel": cpqSiVideoMaxHorPixel,
       "cpqSiVideoMaxVertPixel": cpqSiVideoMaxVertPixel,
       "cpqSiVideoMaxRefreshRate": cpqSiVideoMaxRefreshRate,
       "cpqSiMonitor": cpqSiMonitor,
       "cpqSiMonitorOverallCondition": cpqSiMonitorOverallCondition,
       "cpqSiMonitorTable": cpqSiMonitorTable,
       "cpqSiMonitorEntry": cpqSiMonitorEntry,
       "cpqSiMonitorIndex": cpqSiMonitorIndex,
       "cpqSiMonitorEdidRaw": cpqSiMonitorEdidRaw,
       "cpqSiMonitorDesc": cpqSiMonitorDesc,
       "cpqSiMonitorSerialNumber": cpqSiMonitorSerialNumber,
       "cpqSiMonitorManufactureDate": cpqSiMonitorManufactureDate,
       "cpqSiMonitorHeight": cpqSiMonitorHeight,
       "cpqSiMonitorWidth": cpqSiMonitorWidth,
       "cpqSiMonitorMaxHorPixel": cpqSiMonitorMaxHorPixel,
       "cpqSiMonitorMaxVertPixel": cpqSiMonitorMaxVertPixel,
       "cpqSiMonitorMaxRefreshRate": cpqSiMonitorMaxRefreshRate,
       "cpqSiMonitorManufacturer": cpqSiMonitorManufacturer,
       "cpqSiMonitorThermalCondition": cpqSiMonitorThermalCondition,
       "cpqSiMonitorOperationalCondition": cpqSiMonitorOperationalCondition,
       "cpqSiMonitorStatus": cpqSiMonitorStatus,
       "cpqSiHotPlugSlot": cpqSiHotPlugSlot,
       "cpqSiHotPlugSlotSupported": cpqSiHotPlugSlotSupported,
       "cpqSiHotPlugSlotCondition": cpqSiHotPlugSlotCondition,
       "cpqSiHotPlugSlotChangeCount": cpqSiHotPlugSlotChangeCount,
       "cpqSiHotPlugSlotTable": cpqSiHotPlugSlotTable,
       "cpqSiHotPlugSlotEntry": cpqSiHotPlugSlotEntry,
       "cpqSiHotPlugSlotChassis": cpqSiHotPlugSlotChassis,
       "cpqSiHotPlugSlotIndex": cpqSiHotPlugSlotIndex,
       "cpqSiHotPlugSlotBoardPresent": cpqSiHotPlugSlotBoardPresent,
       "cpqSiHotPlugSlotPowerState": cpqSiHotPlugSlotPowerState,
       "cpqSiHotPlugSlotBoardCondition": cpqSiHotPlugSlotBoardCondition,
       "cpqSiHotPlugSlotErrorStatus": cpqSiHotPlugSlotErrorStatus,
       "cpqSiHotPlugSlotHwLocation": cpqSiHotPlugSlotHwLocation,
       "cpqSiSystemBattery": cpqSiSystemBattery,
       "cpqSiSystemBatteryOverallCondition": cpqSiSystemBatteryOverallCondition,
       "cpqSiSysBatteryTable": cpqSiSysBatteryTable,
       "cpqSiSysBatteryEntry": cpqSiSysBatteryEntry,
       "cpqSiSysBatteryIndex": cpqSiSysBatteryIndex,
       "cpqSiSysBatteryModel": cpqSiSysBatteryModel,
       "cpqSiSysBatterySerialNum": cpqSiSysBatterySerialNum,
       "cpqSiSysBatteryAssetTag": cpqSiSysBatteryAssetTag,
       "cpqSiSysBatteryManufacturer": cpqSiSysBatteryManufacturer,
       "cpqSiSysBatteryDate": cpqSiSysBatteryDate,
       "cpqSiSysBatterySmartVersion": cpqSiSysBatterySmartVersion,
       "cpqSiSysBatteryCondition": cpqSiSysBatteryCondition,
       "cpqSiSysBatteryStatus": cpqSiSysBatteryStatus,
       "cpqSiSysBatteryChemistry": cpqSiSysBatteryChemistry,
       "cpqSiSysBatteryRemainingCap": cpqSiSysBatteryRemainingCap,
       "cpqSiSysBatteryFirmwareRevision": cpqSiSysBatteryFirmwareRevision,
       "cpqSiSysBatteryHardwareRevision": cpqSiSysBatteryHardwareRevision,
       "cpqSiSysBatteryFullCap": cpqSiSysBatteryFullCap,
       "cpqSiSysBatteryDesignCap": cpqSiSysBatteryDesignCap,
       "cpqSiSysBatteryHwLocation": cpqSiSysBatteryHwLocation,
       "cpqSiDockingStation": cpqSiDockingStation,
       "cpqSiDockingStationStatus": cpqSiDockingStationStatus,
       "cpqSiDockingStationSerialNum": cpqSiDockingStationSerialNum,
       "cpqSiDockingStationModel": cpqSiDockingStationModel,
       "cpqSiDockingStationAssetTag": cpqSiDockingStationAssetTag,
       "cpqSiFru": cpqSiFru,
       "cpqSiFruTable": cpqSiFruTable,
       "cpqSiFruEntry": cpqSiFruEntry,
       "cpqSiFruIndex": cpqSiFruIndex,
       "cpqSiFruType": cpqSiFruType,
       "cpqSiFruDescr": cpqSiFruDescr,
       "cpqSiFruVendor": cpqSiFruVendor,
       "cpqSiFruPartNumber": cpqSiFruPartNumber,
       "cpqSiFruRevision": cpqSiFruRevision,
       "cpqSiFruFirmwareRevision": cpqSiFruFirmwareRevision,
       "cpqSiFruSerialNumber": cpqSiFruSerialNumber,
       "cpqSiFruAssetNo": cpqSiFruAssetNo,
       "cpqSiFruClass": cpqSiFruClass,
       "cpqSiFruSlotNumber": cpqSiFruSlotNumber,
       "cpqSiFruSubAssemblyNumber": cpqSiFruSubAssemblyNumber,
       "cpqSiFruAssemblyNumber": cpqSiFruAssemblyNumber,
       "cpqSiFruChassisNumber": cpqSiFruChassisNumber,
       "cpqSiFruPositionNumber": cpqSiFruPositionNumber,
       "cpqSiFruCabinetIDNumber": cpqSiFruCabinetIDNumber,
       "cpqSiFruSiteLocation": cpqSiFruSiteLocation,
       "cpqSiFruDiagStatus": cpqSiFruDiagStatus,
       "cpqSiFruExtendedDiagStatus": cpqSiFruExtendedDiagStatus,
       "cpqSiFruCellTablePtr": cpqSiFruCellTablePtr,
       "cpqSiFruIOCTablePtr": cpqSiFruIOCTablePtr,
       "cpqSiFruFileId": cpqSiFruFileId,
       "cpqSiFruScanRev": cpqSiFruScanRev,
       "cpqSiRackEnclosure": cpqSiRackEnclosure,
       "cpqSiRackEnclosureMgrTable": cpqSiRackEnclosureMgrTable,
       "cpqSiRackEnclosureMgrEntry": cpqSiRackEnclosureMgrEntry,
       "cpqSiRackEnclosureMgrIndex": cpqSiRackEnclosureMgrIndex,
       "cpqSiRackEnclosureMgrType": cpqSiRackEnclosureMgrType,
       "cpqSiRackEnclosureMgrIpAddr": cpqSiRackEnclosureMgrIpAddr,
       "cpqSiRackEnclosureMgrWebLink": cpqSiRackEnclosureMgrWebLink,
       "cpqSiRackEnclosureMgrCondition": cpqSiRackEnclosureMgrCondition,
       "cpqSiRackEnclosureMgrSerialNumber": cpqSiRackEnclosureMgrSerialNumber,
       "cpqSiRackEnclosureMgrModel": cpqSiRackEnclosureMgrModel,
       "cpqSiRackEnclosureMgrName": cpqSiRackEnclosureMgrName,
       "cpqSiRackEnclosureMgrFwRev": cpqSiRackEnclosureMgrFwRev,
       "cpqSiRackEnclosureMgrProductID": cpqSiRackEnclosureMgrProductID,
       "cpqSiRackEnclosureMgrUUID": cpqSiRackEnclosureMgrUUID,
       "cpqSiServerBlade": cpqSiServerBlade,
       "cpqSiServerBladeEnclosureBayNumber": cpqSiServerBladeEnclosureBayNumber,
       "cpqSiServerBladeHeight": cpqSiServerBladeHeight,
       "cpqSiServerBladeWidth": cpqSiServerBladeWidth,
       "cpqSiRack": cpqSiRack,
       "cpqSiRackName": cpqSiRackName,
       "cpqSiRackUUID": cpqSiRackUUID,
       "cpqSiMP": cpqSiMP,
       "cpqSiMPHostName": cpqSiMPHostName,
       "cpqSiMPHealthStatus": cpqSiMPHealthStatus}
)
