# SNMP MIB module (LC-ADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LC-ADMIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:32 2024
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

(lancastMibModulesA,) = mibBuilder.importSymbols(
    "LANCAST-MIB",
    "lancastMibModulesA")

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

admin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1)
)
admin.setRevisions(
        ("1999-03-03 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdminS_ObjectIdentity = ObjectIdentity
adminS = _AdminS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1)
)
_CurNumSysFiles_Type = Integer32
_CurNumSysFiles_Object = MibScalar
curNumSysFiles = _CurNumSysFiles_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 1),
    _CurNumSysFiles_Type()
)
curNumSysFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curNumSysFiles.setStatus("current")


class _PrimaryBootImage_Type(DisplayString):
    """Custom type primaryBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryBootImage_Type.__name__ = "DisplayString"
_PrimaryBootImage_Object = MibScalar
primaryBootImage = _PrimaryBootImage_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 2),
    _PrimaryBootImage_Type()
)
primaryBootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryBootImage.setStatus("current")


class _PrimaryBootImageVersion_Type(DisplayString):
    """Custom type primaryBootImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryBootImageVersion_Type.__name__ = "DisplayString"
_PrimaryBootImageVersion_Object = MibScalar
primaryBootImageVersion = _PrimaryBootImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 3),
    _PrimaryBootImageVersion_Type()
)
primaryBootImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryBootImageVersion.setStatus("current")


class _PrimaryCoreImage_Type(DisplayString):
    """Custom type primaryCoreImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryCoreImage_Type.__name__ = "DisplayString"
_PrimaryCoreImage_Object = MibScalar
primaryCoreImage = _PrimaryCoreImage_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 4),
    _PrimaryCoreImage_Type()
)
primaryCoreImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryCoreImage.setStatus("current")


class _PrimaryCoreImageVersion_Type(DisplayString):
    """Custom type primaryCoreImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryCoreImageVersion_Type.__name__ = "DisplayString"
_PrimaryCoreImageVersion_Object = MibScalar
primaryCoreImageVersion = _PrimaryCoreImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 5),
    _PrimaryCoreImageVersion_Type()
)
primaryCoreImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryCoreImageVersion.setStatus("current")


class _PrimaryAppImage_Type(DisplayString):
    """Custom type primaryAppImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryAppImage_Type.__name__ = "DisplayString"
_PrimaryAppImage_Object = MibScalar
primaryAppImage = _PrimaryAppImage_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 6),
    _PrimaryAppImage_Type()
)
primaryAppImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryAppImage.setStatus("current")


class _PrimaryAppImageVersion_Type(DisplayString):
    """Custom type primaryAppImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PrimaryAppImageVersion_Type.__name__ = "DisplayString"
_PrimaryAppImageVersion_Object = MibScalar
primaryAppImageVersion = _PrimaryAppImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 7),
    _PrimaryAppImageVersion_Type()
)
primaryAppImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryAppImageVersion.setStatus("current")


class _CurDateTime_Type(DisplayString):
    """Custom type curDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CurDateTime_Type.__name__ = "DisplayString"
_CurDateTime_Object = MibScalar
curDateTime = _CurDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 8),
    _CurDateTime_Type()
)
curDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curDateTime.setStatus("current")


class _FileTransferCapability_Type(Integer32):
    """Custom type fileTransferCapability based on Integer32"""
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
        *(("both", 4),
          ("downLoadOnly", 3),
          ("none", 1),
          ("upLoadOnly", 2))
    )


_FileTransferCapability_Type.__name__ = "Integer32"
_FileTransferCapability_Object = MibScalar
fileTransferCapability = _FileTransferCapability_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 9),
    _FileTransferCapability_Type()
)
fileTransferCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferCapability.setStatus("current")


class _EntityMibSupport_Type(Integer32):
    """Custom type entityMibSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localsubsetSNMPV1", 1),
          ("standardMibSNMPV2", 2))
    )


_EntityMibSupport_Type.__name__ = "Integer32"
_EntityMibSupport_Object = MibScalar
entityMibSupport = _EntityMibSupport_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 10),
    _EntityMibSupport_Type()
)
entityMibSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityMibSupport.setStatus("current")


class _Manufacturer_Type(DisplayString):
    """Custom type manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Manufacturer_Type.__name__ = "DisplayString"
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 11),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")


class _CommunityStringRO_Type(DisplayString):
    """Custom type communityStringRO based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CommunityStringRO_Type.__name__ = "DisplayString"
_CommunityStringRO_Object = MibScalar
communityStringRO = _CommunityStringRO_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 12),
    _CommunityStringRO_Type()
)
communityStringRO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStringRO.setStatus("current")


class _CommunityStringRW_Type(DisplayString):
    """Custom type communityStringRW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CommunityStringRW_Type.__name__ = "DisplayString"
_CommunityStringRW_Object = MibScalar
communityStringRW = _CommunityStringRW_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 13),
    _CommunityStringRW_Type()
)
communityStringRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStringRW.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
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
        *(("biLingualV1V2", 5),
          ("bilingualV1V2c", 6),
          ("other", 1),
          ("v1", 2),
          ("v2", 3),
          ("v3", 4))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 14),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_DefaultGatewayAddress_Type = IpAddress
_DefaultGatewayAddress_Object = MibScalar
defaultGatewayAddress = _DefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 15),
    _DefaultGatewayAddress_Type()
)
defaultGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGatewayAddress.setStatus("current")


class _LastSystemResetReason_Type(Integer32):
    """Custom type lastSystemResetReason based on Integer32"""
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
        *(("cold-start", 1),
          ("download-reset", 3),
          ("nms-sw-reset", 2),
          ("watch-dog-timeout", 4))
    )


_LastSystemResetReason_Type.__name__ = "Integer32"
_LastSystemResetReason_Object = MibScalar
lastSystemResetReason = _LastSystemResetReason_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 16),
    _LastSystemResetReason_Type()
)
lastSystemResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSystemResetReason.setStatus("current")


class _LastSystemResetTime_Type(DisplayString):
    """Custom type lastSystemResetTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LastSystemResetTime_Type.__name__ = "DisplayString"
_LastSystemResetTime_Object = MibScalar
lastSystemResetTime = _LastSystemResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 17),
    _LastSystemResetTime_Type()
)
lastSystemResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSystemResetTime.setStatus("current")
_AdminT_ObjectIdentity = ObjectIdentity
adminT = _AdminT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2)
)
_AccessControlTable_Object = MibTable
accessControlTable = _AccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    accessControlTable.setStatus("current")
_AccessControlTableEntry_Object = MibTableRow
accessControlTableEntry = _AccessControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1)
)
accessControlTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "accessControlIndex"),
)
if mibBuilder.loadTexts:
    accessControlTableEntry.setStatus("current")
_AccessControlIndex_Type = Integer32
_AccessControlIndex_Object = MibTableColumn
accessControlIndex = _AccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1, 1),
    _AccessControlIndex_Type()
)
accessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlIndex.setStatus("current")
_AccessControlAddress_Type = IpAddress
_AccessControlAddress_Object = MibTableColumn
accessControlAddress = _AccessControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1, 2),
    _AccessControlAddress_Type()
)
accessControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddress.setStatus("current")
_SysFileTable_Object = MibTable
sysFileTable = _SysFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sysFileTable.setStatus("current")
_SysFileTableEntry_Object = MibTableRow
sysFileTableEntry = _SysFileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1)
)
sysFileTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "sysFileTableIndex"),
)
if mibBuilder.loadTexts:
    sysFileTableEntry.setStatus("current")
_SysFileTableIndex_Type = Integer32
_SysFileTableIndex_Object = MibTableColumn
sysFileTableIndex = _SysFileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 1),
    _SysFileTableIndex_Type()
)
sysFileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFileTableIndex.setStatus("current")


class _SysFileName_Type(DisplayString):
    """Custom type sysFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysFileName_Type.__name__ = "DisplayString"
_SysFileName_Object = MibTableColumn
sysFileName = _SysFileName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 2),
    _SysFileName_Type()
)
sysFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFileName.setStatus("current")
_SysFileSize_Type = Integer32
_SysFileSize_Object = MibTableColumn
sysFileSize = _SysFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 3),
    _SysFileSize_Type()
)
sysFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFileSize.setStatus("current")


class _SysFileAttribute_Type(Integer32):
    """Custom type sysFileAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("executable", 3),
          ("read", 1),
          ("write", 2))
    )


_SysFileAttribute_Type.__name__ = "Integer32"
_SysFileAttribute_Object = MibTableColumn
sysFileAttribute = _SysFileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 4),
    _SysFileAttribute_Type()
)
sysFileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFileAttribute.setStatus("current")


class _SysFileDateTime_Type(DisplayString):
    """Custom type sysFileDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SysFileDateTime_Type.__name__ = "DisplayString"
_SysFileDateTime_Object = MibTableColumn
sysFileDateTime = _SysFileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 5),
    _SysFileDateTime_Type()
)
sysFileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFileDateTime.setStatus("current")
_XferFileTable_Object = MibTable
xferFileTable = _XferFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    xferFileTable.setStatus("current")
_XferFileTableEntry_Object = MibTableRow
xferFileTableEntry = _XferFileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1)
)
xferFileTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "xferFileTableIndex"),
)
if mibBuilder.loadTexts:
    xferFileTableEntry.setStatus("current")
_XferFileTableIndex_Type = Integer32
_XferFileTableIndex_Object = MibTableColumn
xferFileTableIndex = _XferFileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 1),
    _XferFileTableIndex_Type()
)
xferFileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferFileTableIndex.setStatus("current")


class _XferFileName_Type(DisplayString):
    """Custom type xferFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_XferFileName_Type.__name__ = "DisplayString"
_XferFileName_Object = MibTableColumn
xferFileName = _XferFileName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 2),
    _XferFileName_Type()
)
xferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferFileName.setStatus("current")
_XferFileAddress_Type = IpAddress
_XferFileAddress_Object = MibTableColumn
xferFileAddress = _XferFileAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 3),
    _XferFileAddress_Type()
)
xferFileAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferFileAddress.setStatus("current")


class _XferFileDirection_Type(Integer32):
    """Custom type xferFileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("upload", 1))
    )


_XferFileDirection_Type.__name__ = "Integer32"
_XferFileDirection_Object = MibTableColumn
xferFileDirection = _XferFileDirection_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 4),
    _XferFileDirection_Type()
)
xferFileDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferFileDirection.setStatus("current")


class _XferFileActivation_Type(Integer32):
    """Custom type xferFileActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("transfer", 1))
    )


_XferFileActivation_Type.__name__ = "Integer32"
_XferFileActivation_Object = MibTableColumn
xferFileActivation = _XferFileActivation_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 5),
    _XferFileActivation_Type()
)
xferFileActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferFileActivation.setStatus("current")


class _XferFileStatus_Type(Integer32):
    """Custom type xferFileStatus based on Integer32"""
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
        *(("failure", 5),
          ("inProgress", 3),
          ("other", 1),
          ("success", 4),
          ("waitingToXfer", 2))
    )


_XferFileStatus_Type.__name__ = "Integer32"
_XferFileStatus_Object = MibTableColumn
xferFileStatus = _XferFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 6),
    _XferFileStatus_Type()
)
xferFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferFileStatus.setStatus("current")
_XferFileFailureCode_Type = Integer32
_XferFileFailureCode_Object = MibTableColumn
xferFileFailureCode = _XferFileFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 7),
    _XferFileFailureCode_Type()
)
xferFileFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferFileFailureCode.setStatus("current")


class _XferFileProtocol_Type(Integer32):
    """Custom type xferFileProtocol based on Integer32"""
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
          ("other", 1),
          ("tftp", 3))
    )


_XferFileProtocol_Type.__name__ = "Integer32"
_XferFileProtocol_Object = MibTableColumn
xferFileProtocol = _XferFileProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 8),
    _XferFileProtocol_Type()
)
xferFileProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferFileProtocol.setStatus("current")
_TrapManagerTable_Object = MibTable
trapManagerTable = _TrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    trapManagerTable.setStatus("current")
_TrapManagerTableEntry_Object = MibTableRow
trapManagerTableEntry = _TrapManagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1)
)
trapManagerTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "trapManagerIndex"),
)
if mibBuilder.loadTexts:
    trapManagerTableEntry.setStatus("current")
_TrapManagerIndex_Type = Integer32
_TrapManagerIndex_Object = MibTableColumn
trapManagerIndex = _TrapManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 1),
    _TrapManagerIndex_Type()
)
trapManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapManagerIndex.setStatus("current")
_TrapManagerIpAddress_Type = IpAddress
_TrapManagerIpAddress_Object = MibTableColumn
trapManagerIpAddress = _TrapManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 2),
    _TrapManagerIpAddress_Type()
)
trapManagerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerIpAddress.setStatus("current")


class _TrapManagerUdpPort_Type(Integer32):
    """Custom type trapManagerUdpPort based on Integer32"""
    defaultValue = 162


_TrapManagerUdpPort_Object = MibTableColumn
trapManagerUdpPort = _TrapManagerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 3),
    _TrapManagerUdpPort_Type()
)
trapManagerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerUdpPort.setStatus("current")


class _TrapManagerName_Type(DisplayString):
    """Custom type trapManagerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapManagerName_Type.__name__ = "DisplayString"
_TrapManagerName_Object = MibTableColumn
trapManagerName = _TrapManagerName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 4),
    _TrapManagerName_Type()
)
trapManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerName.setStatus("current")


class _TrapManagerControlStatus_Type(Integer32):
    """Custom type trapManagerControlStatus based on Integer32"""
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


_TrapManagerControlStatus_Type.__name__ = "Integer32"
_TrapManagerControlStatus_Object = MibTableColumn
trapManagerControlStatus = _TrapManagerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 5),
    _TrapManagerControlStatus_Type()
)
trapManagerControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerControlStatus.setStatus("current")


class _TrapManagerSnmpVersion_Type(Integer32):
    """Custom type trapManagerSnmpVersion based on Integer32"""
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
        *(("biLingualV1V2", 5),
          ("bilingualV1V2c", 6),
          ("other", 1),
          ("v1", 2),
          ("v2", 3),
          ("v3", 4))
    )


_TrapManagerSnmpVersion_Type.__name__ = "Integer32"
_TrapManagerSnmpVersion_Object = MibTableColumn
trapManagerSnmpVersion = _TrapManagerSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 6),
    _TrapManagerSnmpVersion_Type()
)
trapManagerSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerSnmpVersion.setStatus("current")
_TrapControlTable_Object = MibTable
trapControlTable = _TrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    trapControlTable.setStatus("current")
_TrapControlTableEntry_Object = MibTableRow
trapControlTableEntry = _TrapControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1)
)
trapControlTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "trapControlTableIndex"),
)
if mibBuilder.loadTexts:
    trapControlTableEntry.setStatus("current")
_TrapControlTableIndex_Type = Integer32
_TrapControlTableIndex_Object = MibTableColumn
trapControlTableIndex = _TrapControlTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 1),
    _TrapControlTableIndex_Type()
)
trapControlTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapControlTableIndex.setStatus("current")


class _TrapControlName_Type(DisplayString):
    """Custom type trapControlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapControlName_Type.__name__ = "DisplayString"
_TrapControlName_Object = MibTableColumn
trapControlName = _TrapControlName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 2),
    _TrapControlName_Type()
)
trapControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapControlName.setStatus("current")
_TrapControlV1TrapNumber_Type = Integer32
_TrapControlV1TrapNumber_Object = MibTableColumn
trapControlV1TrapNumber = _TrapControlV1TrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 3),
    _TrapControlV1TrapNumber_Type()
)
trapControlV1TrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapControlV1TrapNumber.setStatus("current")


class _TrapControlStatus_Type(Integer32):
    """Custom type trapControlStatus based on Integer32"""
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


_TrapControlStatus_Type.__name__ = "Integer32"
_TrapControlStatus_Object = MibTableColumn
trapControlStatus = _TrapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 4),
    _TrapControlStatus_Type()
)
trapControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapControlStatus.setStatus("current")
_TrapControlV2TrapOid_Type = ObjectIdentifier
_TrapControlV2TrapOid_Object = MibTableColumn
trapControlV2TrapOid = _TrapControlV2TrapOid_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 5),
    _TrapControlV2TrapOid_Type()
)
trapControlV2TrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapControlV2TrapOid.setStatus("current")
_InterfaceAddressTable_Object = MibTable
interfaceAddressTable = _InterfaceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    interfaceAddressTable.setStatus("current")
_InterfaceAddressTableEntry_Object = MibTableRow
interfaceAddressTableEntry = _InterfaceAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1)
)
interfaceAddressTableEntry.setIndexNames(
    (0, "LC-ADMIN-MIB", "interfaceIfNum"),
)
if mibBuilder.loadTexts:
    interfaceAddressTableEntry.setStatus("current")
_InterfaceIfNum_Type = Integer32
_InterfaceIfNum_Object = MibTableColumn
interfaceIfNum = _InterfaceIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 1),
    _InterfaceIfNum_Type()
)
interfaceIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfNum.setStatus("current")
_InterfaceIpAddress_Type = IpAddress
_InterfaceIpAddress_Object = MibTableColumn
interfaceIpAddress = _InterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 2),
    _InterfaceIpAddress_Type()
)
interfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpAddress.setStatus("current")
_InterfaceSubnetMask_Type = IpAddress
_InterfaceSubnetMask_Object = MibTableColumn
interfaceSubnetMask = _InterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 3),
    _InterfaceSubnetMask_Type()
)
interfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceSubnetMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LC-ADMIN-MIB",
    **{"admin": admin,
       "adminS": adminS,
       "curNumSysFiles": curNumSysFiles,
       "primaryBootImage": primaryBootImage,
       "primaryBootImageVersion": primaryBootImageVersion,
       "primaryCoreImage": primaryCoreImage,
       "primaryCoreImageVersion": primaryCoreImageVersion,
       "primaryAppImage": primaryAppImage,
       "primaryAppImageVersion": primaryAppImageVersion,
       "curDateTime": curDateTime,
       "fileTransferCapability": fileTransferCapability,
       "entityMibSupport": entityMibSupport,
       "manufacturer": manufacturer,
       "communityStringRO": communityStringRO,
       "communityStringRW": communityStringRW,
       "snmpVersion": snmpVersion,
       "defaultGatewayAddress": defaultGatewayAddress,
       "lastSystemResetReason": lastSystemResetReason,
       "lastSystemResetTime": lastSystemResetTime,
       "adminT": adminT,
       "accessControlTable": accessControlTable,
       "accessControlTableEntry": accessControlTableEntry,
       "accessControlIndex": accessControlIndex,
       "accessControlAddress": accessControlAddress,
       "sysFileTable": sysFileTable,
       "sysFileTableEntry": sysFileTableEntry,
       "sysFileTableIndex": sysFileTableIndex,
       "sysFileName": sysFileName,
       "sysFileSize": sysFileSize,
       "sysFileAttribute": sysFileAttribute,
       "sysFileDateTime": sysFileDateTime,
       "xferFileTable": xferFileTable,
       "xferFileTableEntry": xferFileTableEntry,
       "xferFileTableIndex": xferFileTableIndex,
       "xferFileName": xferFileName,
       "xferFileAddress": xferFileAddress,
       "xferFileDirection": xferFileDirection,
       "xferFileActivation": xferFileActivation,
       "xferFileStatus": xferFileStatus,
       "xferFileFailureCode": xferFileFailureCode,
       "xferFileProtocol": xferFileProtocol,
       "trapManagerTable": trapManagerTable,
       "trapManagerTableEntry": trapManagerTableEntry,
       "trapManagerIndex": trapManagerIndex,
       "trapManagerIpAddress": trapManagerIpAddress,
       "trapManagerUdpPort": trapManagerUdpPort,
       "trapManagerName": trapManagerName,
       "trapManagerControlStatus": trapManagerControlStatus,
       "trapManagerSnmpVersion": trapManagerSnmpVersion,
       "trapControlTable": trapControlTable,
       "trapControlTableEntry": trapControlTableEntry,
       "trapControlTableIndex": trapControlTableIndex,
       "trapControlName": trapControlName,
       "trapControlV1TrapNumber": trapControlV1TrapNumber,
       "trapControlStatus": trapControlStatus,
       "trapControlV2TrapOid": trapControlV2TrapOid,
       "interfaceAddressTable": interfaceAddressTable,
       "interfaceAddressTableEntry": interfaceAddressTableEntry,
       "interfaceIfNum": interfaceIfNum,
       "interfaceIpAddress": interfaceIpAddress,
       "interfaceSubnetMask": interfaceSubnetMask}
)
