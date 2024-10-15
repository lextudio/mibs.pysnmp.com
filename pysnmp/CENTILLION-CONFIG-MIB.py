# SNMP MIB module (CENTILLION-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:01 2024
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

(BitField,
 EnableIndicator,
 MacAddress,
 StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "BitField",
    "EnableIndicator",
    "MacAddress",
    "StatusIndicator",
    "sysConfig")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysTableConfig_ObjectIdentity = ObjectIdentity
sysTableConfig = _SysTableConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 1)
)
_SysImgInfo_ObjectIdentity = ObjectIdentity
sysImgInfo = _SysImgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2)
)
_SysImgGbl_ObjectIdentity = ObjectIdentity
sysImgGbl = _SysImgGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 1)
)


class _SysImgGblInvokeSrc_Type(Integer32):
    """Custom type sysImgGblInvokeSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("other", 1))
    )


_SysImgGblInvokeSrc_Type.__name__ = "Integer32"
_SysImgGblInvokeSrc_Object = MibScalar
sysImgGblInvokeSrc = _SysImgGblInvokeSrc_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 1, 1),
    _SysImgGblInvokeSrc_Type()
)
sysImgGblInvokeSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysImgGblInvokeSrc.setStatus("mandatory")


class _SysImgGblLoadDst_Type(Integer32):
    """Custom type sysImgGblLoadDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("location1", 2),
          ("location2", 3),
          ("other", 1))
    )


_SysImgGblLoadDst_Type.__name__ = "Integer32"
_SysImgGblLoadDst_Object = MibScalar
sysImgGblLoadDst = _SysImgGblLoadDst_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 1, 2),
    _SysImgGblLoadDst_Type()
)
sysImgGblLoadDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysImgGblLoadDst.setStatus("mandatory")
_SysImgTable_Object = MibTable
sysImgTable = _SysImgTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sysImgTable.setStatus("mandatory")
_SysImgEntry_Object = MibTableRow
sysImgEntry = _SysImgEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 2, 1)
)
sysImgEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "sysImgIndx"),
)
if mibBuilder.loadTexts:
    sysImgEntry.setStatus("mandatory")


class _SysImgIndx_Type(Integer32):
    """Custom type sysImgIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysImgIndx_Type.__name__ = "Integer32"
_SysImgIndx_Object = MibTableColumn
sysImgIndx = _SysImgIndx_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 2, 1, 1),
    _SysImgIndx_Type()
)
sysImgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImgIndx.setStatus("mandatory")


class _SysImgVer_Type(DisplayString):
    """Custom type sysImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SysImgVer_Type.__name__ = "DisplayString"
_SysImgVer_Object = MibTableColumn
sysImgVer = _SysImgVer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 2, 1, 2),
    _SysImgVer_Type()
)
sysImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImgVer.setStatus("mandatory")


class _SysImgStatus_Type(Integer32):
    """Custom type sysImgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 2),
          ("other", 1))
    )


_SysImgStatus_Type.__name__ = "Integer32"
_SysImgStatus_Object = MibTableColumn
sysImgStatus = _SysImgStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 2, 2, 1, 3),
    _SysImgStatus_Type()
)
sysImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImgStatus.setStatus("mandatory")
_SysMcpRedundInfo_ObjectIdentity = ObjectIdentity
sysMcpRedundInfo = _SysMcpRedundInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3)
)
_SysMcpRedundGbl_ObjectIdentity = ObjectIdentity
sysMcpRedundGbl = _SysMcpRedundGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 1)
)


class _SysMcpRedundNxtGblState_Type(Integer32):
    """Custom type sysMcpRedundNxtGblState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SysMcpRedundNxtGblState_Type.__name__ = "Integer32"
_SysMcpRedundNxtGblState_Object = MibScalar
sysMcpRedundNxtGblState = _SysMcpRedundNxtGblState_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 1, 1),
    _SysMcpRedundNxtGblState_Type()
)
sysMcpRedundNxtGblState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMcpRedundNxtGblState.setStatus("mandatory")
_SysMcpRedundTable_Object = MibTable
sysMcpRedundTable = _SysMcpRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    sysMcpRedundTable.setStatus("mandatory")
_SysMcpRedundEntry_Object = MibTableRow
sysMcpRedundEntry = _SysMcpRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1)
)
sysMcpRedundEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "sysMcpRedundIndx"),
)
if mibBuilder.loadTexts:
    sysMcpRedundEntry.setStatus("mandatory")


class _SysMcpRedundIndx_Type(Integer32):
    """Custom type sysMcpRedundIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysMcpRedundIndx_Type.__name__ = "Integer32"
_SysMcpRedundIndx_Object = MibTableColumn
sysMcpRedundIndx = _SysMcpRedundIndx_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1, 1),
    _SysMcpRedundIndx_Type()
)
sysMcpRedundIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMcpRedundIndx.setStatus("mandatory")


class _SysMcpRedundPriority_Type(Integer32):
    """Custom type sysMcpRedundPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysMcpRedundPriority_Type.__name__ = "Integer32"
_SysMcpRedundPriority_Object = MibTableColumn
sysMcpRedundPriority = _SysMcpRedundPriority_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1, 2),
    _SysMcpRedundPriority_Type()
)
sysMcpRedundPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMcpRedundPriority.setStatus("mandatory")


class _SysMcpRedundType_Type(Integer32):
    """Custom type sysMcpRedundType based on Integer32"""
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
        *(("other", 1),
          ("primary", 3),
          ("regular", 2),
          ("secondary", 4),
          ("switching", 5))
    )


_SysMcpRedundType_Type.__name__ = "Integer32"
_SysMcpRedundType_Object = MibTableColumn
sysMcpRedundType = _SysMcpRedundType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1, 3),
    _SysMcpRedundType_Type()
)
sysMcpRedundType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMcpRedundType.setStatus("mandatory")


class _SysMcpRedundOperState_Type(Integer32):
    """Custom type sysMcpRedundOperState based on Integer32"""
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
          ("other", 1))
    )


_SysMcpRedundOperState_Type.__name__ = "Integer32"
_SysMcpRedundOperState_Object = MibTableColumn
sysMcpRedundOperState = _SysMcpRedundOperState_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1, 4),
    _SysMcpRedundOperState_Type()
)
sysMcpRedundOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMcpRedundOperState.setStatus("mandatory")


class _SysMcpRedundCfgStatus_Type(Integer32):
    """Custom type sysMcpRedundCfgStatus based on Integer32"""
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
        *(("default-disable", 5),
          ("default-enable", 4),
          ("other", 1),
          ("user-disable", 3),
          ("user-enable", 2))
    )


_SysMcpRedundCfgStatus_Type.__name__ = "Integer32"
_SysMcpRedundCfgStatus_Object = MibTableColumn
sysMcpRedundCfgStatus = _SysMcpRedundCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 3, 2, 1, 5),
    _SysMcpRedundCfgStatus_Type()
)
sysMcpRedundCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMcpRedundCfgStatus.setStatus("mandatory")
_RifTable_Object = MibTable
rifTable = _RifTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rifTable.setStatus("mandatory")
_RifEntry_Object = MibTableRow
rifEntry = _RifEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1)
)
rifEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "rifPath"),
)
if mibBuilder.loadTexts:
    rifEntry.setStatus("mandatory")


class _RifPath_Type(OctetString):
    """Custom type rifPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 28),
    )


_RifPath_Type.__name__ = "OctetString"
_RifPath_Object = MibTableColumn
rifPath = _RifPath_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 1),
    _RifPath_Type()
)
rifPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifPath.setStatus("mandatory")
_RifIndex_Type = Integer32
_RifIndex_Object = MibTableColumn
rifIndex = _RifIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 2),
    _RifIndex_Type()
)
rifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifIndex.setStatus("mandatory")
_RifInUse_Type = BitField
_RifInUse_Object = MibTableColumn
rifInUse = _RifInUse_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 3),
    _RifInUse_Type()
)
rifInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rifInUse.setStatus("mandatory")
_RifCount_Type = Integer32
_RifCount_Object = MibTableColumn
rifCount = _RifCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 4),
    _RifCount_Type()
)
rifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifCount.setStatus("mandatory")
_RifLength_Type = Integer32
_RifLength_Object = MibTableColumn
rifLength = _RifLength_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 5),
    _RifLength_Type()
)
rifLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifLength.setStatus("mandatory")
_RifNext_Type = Integer32
_RifNext_Object = MibTableColumn
rifNext = _RifNext_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 6),
    _RifNext_Type()
)
rifNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifNext.setStatus("mandatory")
_RifPrevious_Type = Integer32
_RifPrevious_Object = MibTableColumn
rifPrevious = _RifPrevious_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 5, 1, 7),
    _RifPrevious_Type()
)
rifPrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rifPrevious.setStatus("mandatory")


class _SystemMaxPacketInfoSize_Type(Integer32):
    """Custom type systemMaxPacketInfoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(516, 17800),
    )


_SystemMaxPacketInfoSize_Type.__name__ = "Integer32"
_SystemMaxPacketInfoSize_Object = MibScalar
systemMaxPacketInfoSize = _SystemMaxPacketInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 6),
    _SystemMaxPacketInfoSize_Type()
)
systemMaxPacketInfoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemMaxPacketInfoSize.setStatus("mandatory")


class _SystemConfigMode_Type(Integer32):
    """Custom type systemConfigMode based on Integer32"""
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
        *(("noVirtualRingBridging", 5),
          ("other", 1),
          ("source-route-bridging", 3),
          ("transparent-bridging", 4),
          ("transparentSwitchingNoSTP", 2))
    )


_SystemConfigMode_Type.__name__ = "Integer32"
_SystemConfigMode_Object = MibScalar
systemConfigMode = _SystemConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 7),
    _SystemConfigMode_Type()
)
systemConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigMode.setStatus("mandatory")
_MaxPerfMode_Type = EnableIndicator
_MaxPerfMode_Object = MibScalar
maxPerfMode = _MaxPerfMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 8),
    _MaxPerfMode_Type()
)
maxPerfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPerfMode.setStatus("mandatory")
_ConfigSave_Type = BitField
_ConfigSave_Object = MibScalar
configSave = _ConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 10),
    _ConfigSave_Type()
)
configSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSave.setStatus("mandatory")
_LocalAdminMacAddress_Type = MacAddress
_LocalAdminMacAddress_Object = MibScalar
localAdminMacAddress = _LocalAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 12),
    _LocalAdminMacAddress_Type()
)
localAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localAdminMacAddress.setStatus("mandatory")
_ConfigLogin_Type = OctetString
_ConfigLogin_Object = MibScalar
configLogin = _ConfigLogin_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 13),
    _ConfigLogin_Type()
)
configLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLogin.setStatus("mandatory")
_SysNetProtocol_ObjectIdentity = ObjectIdentity
sysNetProtocol = _SysNetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14)
)
_SysIpProtocol_ObjectIdentity = ObjectIdentity
sysIpProtocol = _SysIpProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1)
)
_SysAddr_Type = IpAddress
_SysAddr_Object = MibScalar
sysAddr = _SysAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 1),
    _SysAddr_Type()
)
sysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAddr.setStatus("deprecated")
_SysNetMask_Type = IpAddress
_SysNetMask_Object = MibScalar
sysNetMask = _SysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 2),
    _SysNetMask_Type()
)
sysNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetMask.setStatus("deprecated")
_SysBcastAddr_Type = IpAddress
_SysBcastAddr_Object = MibScalar
sysBcastAddr = _SysBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 3),
    _SysBcastAddr_Type()
)
sysBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBcastAddr.setStatus("deprecated")
_DefaultGatewayAddr_Type = IpAddress
_DefaultGatewayAddr_Object = MibScalar
defaultGatewayAddr = _DefaultGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 4),
    _DefaultGatewayAddr_Type()
)
defaultGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGatewayAddr.setStatus("deprecated")
_ConfigServerAddr_Type = IpAddress
_ConfigServerAddr_Object = MibScalar
configServerAddr = _ConfigServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 5),
    _ConfigServerAddr_Type()
)
configServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configServerAddr.setStatus("mandatory")


class _IpConfigProtocol_Type(Integer32):
    """Custom type ipConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("flash", 1))
    )


_IpConfigProtocol_Type.__name__ = "Integer32"
_IpConfigProtocol_Object = MibScalar
ipConfigProtocol = _IpConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 6),
    _IpConfigProtocol_Type()
)
ipConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigProtocol.setStatus("deprecated")
_IpHostNumber_Type = Integer32
_IpHostNumber_Object = MibScalar
ipHostNumber = _IpHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 7),
    _IpHostNumber_Type()
)
ipHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipHostNumber.setStatus("mandatory")
_IpHostTable_Object = MibTable
ipHostTable = _IpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8)
)
if mibBuilder.loadTexts:
    ipHostTable.setStatus("mandatory")
_IpHostEntry_Object = MibTableRow
ipHostEntry = _IpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1)
)
ipHostEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "ipHostIndex"),
)
if mibBuilder.loadTexts:
    ipHostEntry.setStatus("mandatory")
_IpHostIndex_Type = Integer32
_IpHostIndex_Object = MibTableColumn
ipHostIndex = _IpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 1),
    _IpHostIndex_Type()
)
ipHostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostIndex.setStatus("mandatory")
_IpHostAddress_Type = IpAddress
_IpHostAddress_Object = MibTableColumn
ipHostAddress = _IpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 2),
    _IpHostAddress_Type()
)
ipHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostAddress.setStatus("mandatory")
_IpHostNetMask_Type = IpAddress
_IpHostNetMask_Object = MibTableColumn
ipHostNetMask = _IpHostNetMask_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 3),
    _IpHostNetMask_Type()
)
ipHostNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostNetMask.setStatus("mandatory")
_IpHostBcastAddr_Type = IpAddress
_IpHostBcastAddr_Object = MibTableColumn
ipHostBcastAddr = _IpHostBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 4),
    _IpHostBcastAddr_Type()
)
ipHostBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostBcastAddr.setStatus("mandatory")
_IpHostDefaultGatewayAddr_Type = IpAddress
_IpHostDefaultGatewayAddr_Object = MibTableColumn
ipHostDefaultGatewayAddr = _IpHostDefaultGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 5),
    _IpHostDefaultGatewayAddr_Type()
)
ipHostDefaultGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostDefaultGatewayAddr.setStatus("mandatory")


class _IpHostConfigProtocol_Type(Integer32):
    """Custom type ipHostConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("flash", 1))
    )


_IpHostConfigProtocol_Type.__name__ = "Integer32"
_IpHostConfigProtocol_Object = MibTableColumn
ipHostConfigProtocol = _IpHostConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 6),
    _IpHostConfigProtocol_Type()
)
ipHostConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostConfigProtocol.setStatus("mandatory")


class _IpHostEnable_Type(Integer32):
    """Custom type ipHostEnable based on Integer32"""
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


_IpHostEnable_Type.__name__ = "Integer32"
_IpHostEnable_Object = MibTableColumn
ipHostEnable = _IpHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 7),
    _IpHostEnable_Type()
)
ipHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostEnable.setStatus("mandatory")


class _IpHostType_Type(Integer32):
    """Custom type ipHostType based on Integer32"""
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


_IpHostType_Type.__name__ = "Integer32"
_IpHostType_Object = MibTableColumn
ipHostType = _IpHostType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 14, 1, 8, 1, 8),
    _IpHostType_Type()
)
ipHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipHostType.setStatus("mandatory")


class _ConfigProtocol_Type(Integer32):
    """Custom type configProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("tftpNoSave", 2),
          ("tftpSave", 3))
    )


_ConfigProtocol_Type.__name__ = "Integer32"
_ConfigProtocol_Object = MibScalar
configProtocol = _ConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 15),
    _ConfigProtocol_Type()
)
configProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configProtocol.setStatus("mandatory")


class _ConfigFilename_Type(DisplayString):
    """Custom type configFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigFilename_Type.__name__ = "DisplayString"
_ConfigFilename_Object = MibScalar
configFilename = _ConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 16),
    _ConfigFilename_Type()
)
configFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFilename.setStatus("mandatory")


class _ConfigSource_Type(Integer32):
    """Custom type configSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flashConfig", 1),
          ("remoteConfig", 2))
    )


_ConfigSource_Type.__name__ = "Integer32"
_ConfigSource_Object = MibScalar
configSource = _ConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 17),
    _ConfigSource_Type()
)
configSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSource.setStatus("mandatory")
_SysTFTPGroup_ObjectIdentity = ObjectIdentity
sysTFTPGroup = _SysTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18)
)


class _SysTFTPStart_Type(Integer32):
    """Custom type sysTFTPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftpGet", 2),
          ("tftpNoTransfer", 1),
          ("tftpPut", 3))
    )


_SysTFTPStart_Type.__name__ = "Integer32"
_SysTFTPStart_Object = MibScalar
sysTFTPStart = _SysTFTPStart_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18, 1),
    _SysTFTPStart_Type()
)
sysTFTPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTFTPStart.setStatus("mandatory")
_SysTFTPIpAddress_Type = IpAddress
_SysTFTPIpAddress_Object = MibScalar
sysTFTPIpAddress = _SysTFTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18, 2),
    _SysTFTPIpAddress_Type()
)
sysTFTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTFTPIpAddress.setStatus("mandatory")


class _SysTFTPFileName_Type(DisplayString):
    """Custom type sysTFTPFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTFTPFileName_Type.__name__ = "DisplayString"
_SysTFTPFileName_Object = MibScalar
sysTFTPFileName = _SysTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18, 3),
    _SysTFTPFileName_Type()
)
sysTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTFTPFileName.setStatus("mandatory")


class _SysTFTPFileType_Type(Integer32):
    """Custom type sysTFTPFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 1),
          ("imageCode", 2))
    )


_SysTFTPFileType_Type.__name__ = "Integer32"
_SysTFTPFileType_Object = MibScalar
sysTFTPFileType = _SysTFTPFileType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18, 4),
    _SysTFTPFileType_Type()
)
sysTFTPFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTFTPFileType.setStatus("mandatory")


class _SysTFTPResult_Type(Integer32):
    """Custom type sysTFTPResult based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("accessError", 6),
          ("clear", 1),
          ("configChecksumError", 16),
          ("configMismatch", 15),
          ("diskFull", 7),
          ("fileExists", 10),
          ("fileNotFound", 5),
          ("flashError", 14),
          ("illegalTFTPOperation", 8),
          ("invalidTFTPTransactionID", 9),
          ("noResources", 12),
          ("noResponse", 13),
          ("noSuchUser", 11),
          ("okay", 3),
          ("otherTFTPError", 4),
          ("xferInProgress", 2))
    )


_SysTFTPResult_Type.__name__ = "Integer32"
_SysTFTPResult_Object = MibScalar
sysTFTPResult = _SysTFTPResult_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 18, 5),
    _SysTFTPResult_Type()
)
sysTFTPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTFTPResult.setStatus("mandatory")
_SysSNMPGroup_ObjectIdentity = ObjectIdentity
sysSNMPGroup = _SysSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19)
)


class _SysSNMPGetCommunity_Type(DisplayString):
    """Custom type sysSNMPGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysSNMPGetCommunity_Type.__name__ = "DisplayString"
_SysSNMPGetCommunity_Object = MibScalar
sysSNMPGetCommunity = _SysSNMPGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 1),
    _SysSNMPGetCommunity_Type()
)
sysSNMPGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNMPGetCommunity.setStatus("mandatory")


class _SysSNMPSetCommunity_Type(DisplayString):
    """Custom type sysSNMPSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysSNMPSetCommunity_Type.__name__ = "DisplayString"
_SysSNMPSetCommunity_Object = MibScalar
sysSNMPSetCommunity = _SysSNMPSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 2),
    _SysSNMPSetCommunity_Type()
)
sysSNMPSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNMPSetCommunity.setStatus("mandatory")
_SysSNMPEnableTraps_Type = EnableIndicator
_SysSNMPEnableTraps_Object = MibScalar
sysSNMPEnableTraps = _SysSNMPEnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 3),
    _SysSNMPEnableTraps_Type()
)
sysSNMPEnableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNMPEnableTraps.setStatus("mandatory")
_SysSNMPTrapIPReceiverTable_Object = MibTable
sysSNMPTrapIPReceiverTable = _SysSNMPTrapIPReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 4)
)
if mibBuilder.loadTexts:
    sysSNMPTrapIPReceiverTable.setStatus("mandatory")
_SysSNMPTrapIPReceiverEntry_Object = MibTableRow
sysSNMPTrapIPReceiverEntry = _SysSNMPTrapIPReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 4, 1)
)
sysSNMPTrapIPReceiverEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "trapIPRcvrAddress"),
)
if mibBuilder.loadTexts:
    sysSNMPTrapIPReceiverEntry.setStatus("mandatory")
_TrapIPRcvrAddress_Type = IpAddress
_TrapIPRcvrAddress_Object = MibTableColumn
trapIPRcvrAddress = _TrapIPRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 4, 1, 1),
    _TrapIPRcvrAddress_Type()
)
trapIPRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPRcvrAddress.setStatus("mandatory")
_TrapIPRcvrStatus_Type = StatusIndicator
_TrapIPRcvrStatus_Object = MibTableColumn
trapIPRcvrStatus = _TrapIPRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 4, 1, 2),
    _TrapIPRcvrStatus_Type()
)
trapIPRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPRcvrStatus.setStatus("mandatory")


class _TrapIPRcvrCommunity_Type(DisplayString):
    """Custom type trapIPRcvrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TrapIPRcvrCommunity_Type.__name__ = "DisplayString"
_TrapIPRcvrCommunity_Object = MibTableColumn
trapIPRcvrCommunity = _TrapIPRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 19, 4, 1, 3),
    _TrapIPRcvrCommunity_Type()
)
trapIPRcvrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPRcvrCommunity.setStatus("mandatory")


class _SysMgmtRingNumber_Type(Integer32):
    """Custom type sysMgmtRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SysMgmtRingNumber_Type.__name__ = "Integer32"
_SysMgmtRingNumber_Object = MibScalar
sysMgmtRingNumber = _SysMgmtRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 20),
    _SysMgmtRingNumber_Type()
)
sysMgmtRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtRingNumber.setStatus("mandatory")
_NetbiosGroup_ObjectIdentity = ObjectIdentity
netbiosGroup = _NetbiosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21)
)
_NetbiosNameTableAgingTimer_Type = Integer32
_NetbiosNameTableAgingTimer_Object = MibScalar
netbiosNameTableAgingTimer = _NetbiosNameTableAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 1),
    _NetbiosNameTableAgingTimer_Type()
)
netbiosNameTableAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosNameTableAgingTimer.setStatus("mandatory")


class _NetbiosNameQueryInterval_Type(Integer32):
    """Custom type netbiosNameQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetbiosNameQueryInterval_Type.__name__ = "Integer32"
_NetbiosNameQueryInterval_Object = MibScalar
netbiosNameQueryInterval = _NetbiosNameQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 2),
    _NetbiosNameQueryInterval_Type()
)
netbiosNameQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosNameQueryInterval.setStatus("mandatory")
_NetbiosNameTableFlush_Type = BitField
_NetbiosNameTableFlush_Object = MibScalar
netbiosNameTableFlush = _NetbiosNameTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 3),
    _NetbiosNameTableFlush_Type()
)
netbiosNameTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosNameTableFlush.setStatus("mandatory")
_NetbiosNameTableEntry_Object = MibTable
netbiosNameTableEntry = _NetbiosNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    netbiosNameTableEntry.setStatus("deprecated")
_NetbiosNameEntry_Object = MibTableRow
netbiosNameEntry = _NetbiosNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1)
)
netbiosNameEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "netbiosNameName"),
)
if mibBuilder.loadTexts:
    netbiosNameEntry.setStatus("deprecated")


class _NetbiosNameName_Type(DisplayString):
    """Custom type netbiosNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_NetbiosNameName_Type.__name__ = "DisplayString"
_NetbiosNameName_Object = MibTableColumn
netbiosNameName = _NetbiosNameName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 1),
    _NetbiosNameName_Type()
)
netbiosNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameName.setStatus("deprecated")
_NetbiosNameStatus_Type = StatusIndicator
_NetbiosNameStatus_Object = MibTableColumn
netbiosNameStatus = _NetbiosNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 2),
    _NetbiosNameStatus_Type()
)
netbiosNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameStatus.setStatus("deprecated")


class _NetbiosNameStationAddress_Type(PhysAddress):
    """Custom type netbiosNameStationAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NetbiosNameStationAddress_Type.__name__ = "PhysAddress"
_NetbiosNameStationAddress_Object = MibTableColumn
netbiosNameStationAddress = _NetbiosNameStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 3),
    _NetbiosNameStationAddress_Type()
)
netbiosNameStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameStationAddress.setStatus("deprecated")
_NetbiosNameVirtualRingNumber_Type = Integer32
_NetbiosNameVirtualRingNumber_Object = MibTableColumn
netbiosNameVirtualRingNumber = _NetbiosNameVirtualRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 4),
    _NetbiosNameVirtualRingNumber_Type()
)
netbiosNameVirtualRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameVirtualRingNumber.setStatus("deprecated")
_NetbiosNameCardNumber_Type = Integer32
_NetbiosNameCardNumber_Object = MibTableColumn
netbiosNameCardNumber = _NetbiosNameCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 5),
    _NetbiosNameCardNumber_Type()
)
netbiosNameCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameCardNumber.setStatus("deprecated")
_NetbiosNamePortNumber_Type = Integer32
_NetbiosNamePortNumber_Object = MibTableColumn
netbiosNamePortNumber = _NetbiosNamePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 6),
    _NetbiosNamePortNumber_Type()
)
netbiosNamePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNamePortNumber.setStatus("deprecated")


class _NetbiosNamePortType_Type(Integer32):
    """Custom type netbiosNamePortType based on Integer32"""
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
        *(("atm", 5),
          ("ethernet", 4),
          ("fddi", 3),
          ("other", 1),
          ("token-ring", 2))
    )


_NetbiosNamePortType_Type.__name__ = "Integer32"
_NetbiosNamePortType_Object = MibTableColumn
netbiosNamePortType = _NetbiosNamePortType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 7),
    _NetbiosNamePortType_Type()
)
netbiosNamePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNamePortType.setStatus("deprecated")
_NetbiosNameAge_Type = TimeTicks
_NetbiosNameAge_Object = MibTableColumn
netbiosNameAge = _NetbiosNameAge_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 8),
    _NetbiosNameAge_Type()
)
netbiosNameAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameAge.setStatus("deprecated")
_NetbiosNameProxies_Type = Counter32
_NetbiosNameProxies_Object = MibTableColumn
netbiosNameProxies = _NetbiosNameProxies_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 9),
    _NetbiosNameProxies_Type()
)
netbiosNameProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameProxies.setStatus("deprecated")
_NetbiosNameSuppressedQueries_Type = Counter32
_NetbiosNameSuppressedQueries_Object = MibTableColumn
netbiosNameSuppressedQueries = _NetbiosNameSuppressedQueries_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 4, 1, 10),
    _NetbiosNameSuppressedQueries_Type()
)
netbiosNameSuppressedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosNameSuppressedQueries.setStatus("deprecated")
_CnnetbiosNameTableEntry_Object = MibTable
cnnetbiosNameTableEntry = _CnnetbiosNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5)
)
if mibBuilder.loadTexts:
    cnnetbiosNameTableEntry.setStatus("mandatory")
_CnnetbiosNameEntry_Object = MibTableRow
cnnetbiosNameEntry = _CnnetbiosNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1)
)
cnnetbiosNameEntry.setIndexNames(
    (0, "CENTILLION-CONFIG-MIB", "cnnetbiosNameVlanId"),
    (0, "CENTILLION-CONFIG-MIB", "cnnetbiosNameName"),
)
if mibBuilder.loadTexts:
    cnnetbiosNameEntry.setStatus("mandatory")


class _CnnetbiosNameName_Type(DisplayString):
    """Custom type cnnetbiosNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_CnnetbiosNameName_Type.__name__ = "DisplayString"
_CnnetbiosNameName_Object = MibTableColumn
cnnetbiosNameName = _CnnetbiosNameName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 1),
    _CnnetbiosNameName_Type()
)
cnnetbiosNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameName.setStatus("mandatory")
_CnnetbiosNameStatus_Type = StatusIndicator
_CnnetbiosNameStatus_Object = MibTableColumn
cnnetbiosNameStatus = _CnnetbiosNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 2),
    _CnnetbiosNameStatus_Type()
)
cnnetbiosNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameStatus.setStatus("mandatory")


class _CnnetbiosNameStationAddress_Type(PhysAddress):
    """Custom type cnnetbiosNameStationAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CnnetbiosNameStationAddress_Type.__name__ = "PhysAddress"
_CnnetbiosNameStationAddress_Object = MibTableColumn
cnnetbiosNameStationAddress = _CnnetbiosNameStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 3),
    _CnnetbiosNameStationAddress_Type()
)
cnnetbiosNameStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameStationAddress.setStatus("mandatory")
_CnnetbiosNameVirtualRingNumber_Type = Integer32
_CnnetbiosNameVirtualRingNumber_Object = MibTableColumn
cnnetbiosNameVirtualRingNumber = _CnnetbiosNameVirtualRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 4),
    _CnnetbiosNameVirtualRingNumber_Type()
)
cnnetbiosNameVirtualRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameVirtualRingNumber.setStatus("mandatory")
_CnnetbiosNameCardNumber_Type = Integer32
_CnnetbiosNameCardNumber_Object = MibTableColumn
cnnetbiosNameCardNumber = _CnnetbiosNameCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 5),
    _CnnetbiosNameCardNumber_Type()
)
cnnetbiosNameCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameCardNumber.setStatus("mandatory")
_CnnetbiosNamePortNumber_Type = Integer32
_CnnetbiosNamePortNumber_Object = MibTableColumn
cnnetbiosNamePortNumber = _CnnetbiosNamePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 6),
    _CnnetbiosNamePortNumber_Type()
)
cnnetbiosNamePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNamePortNumber.setStatus("mandatory")
_CnnetbiosNameVlanId_Type = VlanId
_CnnetbiosNameVlanId_Object = MibTableColumn
cnnetbiosNameVlanId = _CnnetbiosNameVlanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 7),
    _CnnetbiosNameVlanId_Type()
)
cnnetbiosNameVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameVlanId.setStatus("mandatory")


class _CnnetbiosNamePortType_Type(Integer32):
    """Custom type cnnetbiosNamePortType based on Integer32"""
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
        *(("atm", 5),
          ("ethernet", 4),
          ("fddi", 3),
          ("other", 1),
          ("token-ring", 2))
    )


_CnnetbiosNamePortType_Type.__name__ = "Integer32"
_CnnetbiosNamePortType_Object = MibTableColumn
cnnetbiosNamePortType = _CnnetbiosNamePortType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 8),
    _CnnetbiosNamePortType_Type()
)
cnnetbiosNamePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNamePortType.setStatus("mandatory")
_CnnetbiosNameAge_Type = TimeTicks
_CnnetbiosNameAge_Object = MibTableColumn
cnnetbiosNameAge = _CnnetbiosNameAge_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 9),
    _CnnetbiosNameAge_Type()
)
cnnetbiosNameAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameAge.setStatus("mandatory")
_CnnetbiosNameProxies_Type = Counter32
_CnnetbiosNameProxies_Object = MibTableColumn
cnnetbiosNameProxies = _CnnetbiosNameProxies_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 10),
    _CnnetbiosNameProxies_Type()
)
cnnetbiosNameProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameProxies.setStatus("mandatory")
_CnnetbiosNameSuppressedQueries_Type = Counter32
_CnnetbiosNameSuppressedQueries_Object = MibTableColumn
cnnetbiosNameSuppressedQueries = _CnnetbiosNameSuppressedQueries_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 21, 5, 1, 11),
    _CnnetbiosNameSuppressedQueries_Type()
)
cnnetbiosNameSuppressedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnetbiosNameSuppressedQueries.setStatus("mandatory")
_LnmGroup_ObjectIdentity = ObjectIdentity
lnmGroup = _LnmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 25)
)


class _LnmOperStatus_Type(Integer32):
    """Custom type lnmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 3),
          ("up", 1))
    )


_LnmOperStatus_Type.__name__ = "Integer32"
_LnmOperStatus_Object = MibScalar
lnmOperStatus = _LnmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 25, 1),
    _LnmOperStatus_Type()
)
lnmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnmOperStatus.setStatus("mandatory")


class _LnmAdminStatus_Type(Integer32):
    """Custom type lnmAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LnmAdminStatus_Type.__name__ = "Integer32"
_LnmAdminStatus_Object = MibScalar
lnmAdminStatus = _LnmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 25, 2),
    _LnmAdminStatus_Type()
)
lnmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnmAdminStatus.setStatus("mandatory")


class _LnmBridgeGroupDisplayMode_Type(Integer32):
    """Custom type lnmBridgeGroupDisplayMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("separate", 2))
    )


_LnmBridgeGroupDisplayMode_Type.__name__ = "Integer32"
_LnmBridgeGroupDisplayMode_Object = MibScalar
lnmBridgeGroupDisplayMode = _LnmBridgeGroupDisplayMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 25, 3),
    _LnmBridgeGroupDisplayMode_Type()
)
lnmBridgeGroupDisplayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnmBridgeGroupDisplayMode.setStatus("mandatory")
_LnmLinkPassword_Type = EnableIndicator
_LnmLinkPassword_Object = MibScalar
lnmLinkPassword = _LnmLinkPassword_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 25, 4),
    _LnmLinkPassword_Type()
)
lnmLinkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnmLinkPassword.setStatus("mandatory")


class _SonmpTrConfig_Type(Integer32):
    """Custom type sonmpTrConfig based on Integer32"""
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


_SonmpTrConfig_Type.__name__ = "Integer32"
_SonmpTrConfig_Object = MibScalar
sonmpTrConfig = _SonmpTrConfig_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 28),
    _SonmpTrConfig_Type()
)
sonmpTrConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonmpTrConfig.setStatus("mandatory")


class _SystemConfigIpOption_Type(Integer32):
    """Custom type systemConfigIpOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eraseIP", 2),
          ("other", 1),
          ("preservedIP", 3))
    )


_SystemConfigIpOption_Type.__name__ = "Integer32"
_SystemConfigIpOption_Object = MibScalar
systemConfigIpOption = _SystemConfigIpOption_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 29),
    _SystemConfigIpOption_Type()
)
systemConfigIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigIpOption.setStatus("mandatory")


class _SonmpTrSpeed_Type(Integer32):
    """Custom type sonmpTrSpeed based on Integer32"""
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
          ("topFast", 2),
          ("topSlow", 3))
    )


_SonmpTrSpeed_Type.__name__ = "Integer32"
_SonmpTrSpeed_Object = MibScalar
sonmpTrSpeed = _SonmpTrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 30),
    _SonmpTrSpeed_Type()
)
sonmpTrSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonmpTrSpeed.setStatus("mandatory")
_SrUnknownFrameFlood_Type = EnableIndicator
_SrUnknownFrameFlood_Object = MibScalar
srUnknownFrameFlood = _SrUnknownFrameFlood_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 32),
    _SrUnknownFrameFlood_Type()
)
srUnknownFrameFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srUnknownFrameFlood.setStatus("mandatory")
_SrbIeeeBpduEnable_Type = EnableIndicator
_SrbIeeeBpduEnable_Object = MibScalar
srbIeeeBpduEnable = _SrbIeeeBpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 33),
    _SrbIeeeBpduEnable_Type()
)
srbIeeeBpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srbIeeeBpduEnable.setStatus("mandatory")
_TbRifProxyEnable_Type = EnableIndicator
_TbRifProxyEnable_Object = MibScalar
tbRifProxyEnable = _TbRifProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 34),
    _TbRifProxyEnable_Type()
)
tbRifProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbRifProxyEnable.setStatus("mandatory")


class _CpuClkRate_Type(Integer32):
    """Custom type cpuClkRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mhz66", 1),
          ("mhz85", 2))
    )


_CpuClkRate_Type.__name__ = "Integer32"
_CpuClkRate_Object = MibScalar
cpuClkRate = _CpuClkRate_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 35),
    _CpuClkRate_Type()
)
cpuClkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuClkRate.setStatus("mandatory")
_MaxRids_Type = Integer32
_MaxRids_Object = MibScalar
maxRids = _MaxRids_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 36),
    _MaxRids_Type()
)
maxRids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRids.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-CONFIG-MIB",
    **{"VlanId": VlanId,
       "sysTableConfig": sysTableConfig,
       "sysImgInfo": sysImgInfo,
       "sysImgGbl": sysImgGbl,
       "sysImgGblInvokeSrc": sysImgGblInvokeSrc,
       "sysImgGblLoadDst": sysImgGblLoadDst,
       "sysImgTable": sysImgTable,
       "sysImgEntry": sysImgEntry,
       "sysImgIndx": sysImgIndx,
       "sysImgVer": sysImgVer,
       "sysImgStatus": sysImgStatus,
       "sysMcpRedundInfo": sysMcpRedundInfo,
       "sysMcpRedundGbl": sysMcpRedundGbl,
       "sysMcpRedundNxtGblState": sysMcpRedundNxtGblState,
       "sysMcpRedundTable": sysMcpRedundTable,
       "sysMcpRedundEntry": sysMcpRedundEntry,
       "sysMcpRedundIndx": sysMcpRedundIndx,
       "sysMcpRedundPriority": sysMcpRedundPriority,
       "sysMcpRedundType": sysMcpRedundType,
       "sysMcpRedundOperState": sysMcpRedundOperState,
       "sysMcpRedundCfgStatus": sysMcpRedundCfgStatus,
       "rifTable": rifTable,
       "rifEntry": rifEntry,
       "rifPath": rifPath,
       "rifIndex": rifIndex,
       "rifInUse": rifInUse,
       "rifCount": rifCount,
       "rifLength": rifLength,
       "rifNext": rifNext,
       "rifPrevious": rifPrevious,
       "systemMaxPacketInfoSize": systemMaxPacketInfoSize,
       "systemConfigMode": systemConfigMode,
       "maxPerfMode": maxPerfMode,
       "configSave": configSave,
       "localAdminMacAddress": localAdminMacAddress,
       "configLogin": configLogin,
       "sysNetProtocol": sysNetProtocol,
       "sysIpProtocol": sysIpProtocol,
       "sysAddr": sysAddr,
       "sysNetMask": sysNetMask,
       "sysBcastAddr": sysBcastAddr,
       "defaultGatewayAddr": defaultGatewayAddr,
       "configServerAddr": configServerAddr,
       "ipConfigProtocol": ipConfigProtocol,
       "ipHostNumber": ipHostNumber,
       "ipHostTable": ipHostTable,
       "ipHostEntry": ipHostEntry,
       "ipHostIndex": ipHostIndex,
       "ipHostAddress": ipHostAddress,
       "ipHostNetMask": ipHostNetMask,
       "ipHostBcastAddr": ipHostBcastAddr,
       "ipHostDefaultGatewayAddr": ipHostDefaultGatewayAddr,
       "ipHostConfigProtocol": ipHostConfigProtocol,
       "ipHostEnable": ipHostEnable,
       "ipHostType": ipHostType,
       "configProtocol": configProtocol,
       "configFilename": configFilename,
       "configSource": configSource,
       "sysTFTPGroup": sysTFTPGroup,
       "sysTFTPStart": sysTFTPStart,
       "sysTFTPIpAddress": sysTFTPIpAddress,
       "sysTFTPFileName": sysTFTPFileName,
       "sysTFTPFileType": sysTFTPFileType,
       "sysTFTPResult": sysTFTPResult,
       "sysSNMPGroup": sysSNMPGroup,
       "sysSNMPGetCommunity": sysSNMPGetCommunity,
       "sysSNMPSetCommunity": sysSNMPSetCommunity,
       "sysSNMPEnableTraps": sysSNMPEnableTraps,
       "sysSNMPTrapIPReceiverTable": sysSNMPTrapIPReceiverTable,
       "sysSNMPTrapIPReceiverEntry": sysSNMPTrapIPReceiverEntry,
       "trapIPRcvrAddress": trapIPRcvrAddress,
       "trapIPRcvrStatus": trapIPRcvrStatus,
       "trapIPRcvrCommunity": trapIPRcvrCommunity,
       "sysMgmtRingNumber": sysMgmtRingNumber,
       "netbiosGroup": netbiosGroup,
       "netbiosNameTableAgingTimer": netbiosNameTableAgingTimer,
       "netbiosNameQueryInterval": netbiosNameQueryInterval,
       "netbiosNameTableFlush": netbiosNameTableFlush,
       "netbiosNameTableEntry": netbiosNameTableEntry,
       "netbiosNameEntry": netbiosNameEntry,
       "netbiosNameName": netbiosNameName,
       "netbiosNameStatus": netbiosNameStatus,
       "netbiosNameStationAddress": netbiosNameStationAddress,
       "netbiosNameVirtualRingNumber": netbiosNameVirtualRingNumber,
       "netbiosNameCardNumber": netbiosNameCardNumber,
       "netbiosNamePortNumber": netbiosNamePortNumber,
       "netbiosNamePortType": netbiosNamePortType,
       "netbiosNameAge": netbiosNameAge,
       "netbiosNameProxies": netbiosNameProxies,
       "netbiosNameSuppressedQueries": netbiosNameSuppressedQueries,
       "cnnetbiosNameTableEntry": cnnetbiosNameTableEntry,
       "cnnetbiosNameEntry": cnnetbiosNameEntry,
       "cnnetbiosNameName": cnnetbiosNameName,
       "cnnetbiosNameStatus": cnnetbiosNameStatus,
       "cnnetbiosNameStationAddress": cnnetbiosNameStationAddress,
       "cnnetbiosNameVirtualRingNumber": cnnetbiosNameVirtualRingNumber,
       "cnnetbiosNameCardNumber": cnnetbiosNameCardNumber,
       "cnnetbiosNamePortNumber": cnnetbiosNamePortNumber,
       "cnnetbiosNameVlanId": cnnetbiosNameVlanId,
       "cnnetbiosNamePortType": cnnetbiosNamePortType,
       "cnnetbiosNameAge": cnnetbiosNameAge,
       "cnnetbiosNameProxies": cnnetbiosNameProxies,
       "cnnetbiosNameSuppressedQueries": cnnetbiosNameSuppressedQueries,
       "lnmGroup": lnmGroup,
       "lnmOperStatus": lnmOperStatus,
       "lnmAdminStatus": lnmAdminStatus,
       "lnmBridgeGroupDisplayMode": lnmBridgeGroupDisplayMode,
       "lnmLinkPassword": lnmLinkPassword,
       "sonmpTrConfig": sonmpTrConfig,
       "systemConfigIpOption": systemConfigIpOption,
       "sonmpTrSpeed": sonmpTrSpeed,
       "srUnknownFrameFlood": srUnknownFrameFlood,
       "srbIeeeBpduEnable": srbIeeeBpduEnable,
       "tbRifProxyEnable": tbRifProxyEnable,
       "cpuClkRate": cpuClkRate,
       "maxRids": maxRids}
)
