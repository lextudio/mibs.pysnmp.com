# SNMP MIB module (SFRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SFRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:25 2024
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
 internet,
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
    "internet",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Index(Integer32):
    """Custom type Index based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Sync_ObjectIdentity = ObjectIdentity
sync = _Sync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485)
)
_Sfrap_ObjectIdentity = ObjectIdentity
sfrap = _Sfrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7)
)
_SfrapSystem_ObjectIdentity = ObjectIdentity
sfrapSystem = _SfrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 1)
)
_SfrapSysTable_ObjectIdentity = ObjectIdentity
sfrapSysTable = _SfrapSysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1)
)


class _SfrapSysType_Type(DisplayString):
    """Custom type sfrapSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SfrapSysType_Type.__name__ = "DisplayString"
_SfrapSysType_Object = MibScalar
sfrapSysType = _SfrapSysType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 1),
    _SfrapSysType_Type()
)
sfrapSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysType.setStatus("mandatory")


class _SfrapSysSoftRev_Type(DisplayString):
    """Custom type sfrapSysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysSoftRev_Type.__name__ = "DisplayString"
_SfrapSysSoftRev_Object = MibScalar
sfrapSysSoftRev = _SfrapSysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 2),
    _SfrapSysSoftRev_Type()
)
sfrapSysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysSoftRev.setStatus("mandatory")


class _SfrapSysHardRev_Type(DisplayString):
    """Custom type sfrapSysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysHardRev_Type.__name__ = "DisplayString"
_SfrapSysHardRev_Object = MibScalar
sfrapSysHardRev = _SfrapSysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 3),
    _SfrapSysHardRev_Type()
)
sfrapSysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysHardRev.setStatus("mandatory")


class _SfrapSysNumToDteInstalled_Type(Integer32):
    """Custom type sfrapSysNumToDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfrapSysNumToDteInstalled_Type.__name__ = "Integer32"
_SfrapSysNumToDteInstalled_Object = MibScalar
sfrapSysNumToDteInstalled = _SfrapSysNumToDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 5),
    _SfrapSysNumToDteInstalled_Type()
)
sfrapSysNumToDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumToDteInstalled.setStatus("mandatory")


class _SfrapSysNumMaintInstalled_Type(Integer32):
    """Custom type sfrapSysNumMaintInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SfrapSysNumMaintInstalled_Type.__name__ = "Integer32"
_SfrapSysNumMaintInstalled_Object = MibScalar
sfrapSysNumMaintInstalled = _SfrapSysNumMaintInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 6),
    _SfrapSysNumMaintInstalled_Type()
)
sfrapSysNumMaintInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumMaintInstalled.setStatus("mandatory")


class _SfrapSysName_Type(DisplayString):
    """Custom type sfrapSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfrapSysName_Type.__name__ = "DisplayString"
_SfrapSysName_Object = MibScalar
sfrapSysName = _SfrapSysName_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 7),
    _SfrapSysName_Type()
)
sfrapSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapSysName.setStatus("mandatory")


class _SfrapSysSerialNo_Type(DisplayString):
    """Custom type sfrapSysSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysSerialNo_Type.__name__ = "DisplayString"
_SfrapSysSerialNo_Object = MibScalar
sfrapSysSerialNo = _SfrapSysSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 8),
    _SfrapSysSerialNo_Type()
)
sfrapSysSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysSerialNo.setStatus("mandatory")


class _SfrapSysResetNode_Type(Integer32):
    """Custom type sfrapSysResetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            321
        )
    )
    namedValues = NamedValues(
        ("reset-node", 321)
    )


_SfrapSysResetNode_Type.__name__ = "Integer32"
_SfrapSysResetNode_Object = MibScalar
sfrapSysResetNode = _SfrapSysResetNode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 9),
    _SfrapSysResetNode_Type()
)
sfrapSysResetNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapSysResetNode.setStatus("mandatory")
_SfrapSysAmtMemoryInstalled_Type = Integer32
_SfrapSysAmtMemoryInstalled_Object = MibScalar
sfrapSysAmtMemoryInstalled = _SfrapSysAmtMemoryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 10),
    _SfrapSysAmtMemoryInstalled_Type()
)
sfrapSysAmtMemoryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysAmtMemoryInstalled.setStatus("mandatory")


class _SfrapSysLocation_Type(DisplayString):
    """Custom type sfrapSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfrapSysLocation_Type.__name__ = "DisplayString"
_SfrapSysLocation_Object = MibScalar
sfrapSysLocation = _SfrapSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 12),
    _SfrapSysLocation_Type()
)
sfrapSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapSysLocation.setStatus("mandatory")


class _SfrapSysContact_Type(DisplayString):
    """Custom type sfrapSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfrapSysContact_Type.__name__ = "DisplayString"
_SfrapSysContact_Object = MibScalar
sfrapSysContact = _SfrapSysContact_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 13),
    _SfrapSysContact_Type()
)
sfrapSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapSysContact.setStatus("mandatory")


class _SfrapSysNumToDceInstalled_Type(Integer32):
    """Custom type sfrapSysNumToDceInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfrapSysNumToDceInstalled_Type.__name__ = "Integer32"
_SfrapSysNumToDceInstalled_Object = MibScalar
sfrapSysNumToDceInstalled = _SfrapSysNumToDceInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 14),
    _SfrapSysNumToDceInstalled_Type()
)
sfrapSysNumToDceInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumToDceInstalled.setStatus("mandatory")


class _SfrapSysPrompt_Type(DisplayString):
    """Custom type sfrapSysPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapSysPrompt_Type.__name__ = "DisplayString"
_SfrapSysPrompt_Object = MibScalar
sfrapSysPrompt = _SfrapSysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 15),
    _SfrapSysPrompt_Type()
)
sfrapSysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapSysPrompt.setStatus("mandatory")


class _SfrapSysBootRev_Type(DisplayString):
    """Custom type sfrapSysBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysBootRev_Type.__name__ = "DisplayString"
_SfrapSysBootRev_Object = MibScalar
sfrapSysBootRev = _SfrapSysBootRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 1, 16),
    _SfrapSysBootRev_Type()
)
sfrapSysBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysBootRev.setStatus("mandatory")
_SfrapSysFeatureTable_ObjectIdentity = ObjectIdentity
sfrapSysFeatureTable = _SfrapSysFeatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2)
)


class _SfrapSysSLIPSupported_Type(DisplayString):
    """Custom type sfrapSysSLIPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysSLIPSupported_Type.__name__ = "DisplayString"
_SfrapSysSLIPSupported_Object = MibScalar
sfrapSysSLIPSupported = _SfrapSysSLIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 1),
    _SfrapSysSLIPSupported_Type()
)
sfrapSysSLIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysSLIPSupported.setStatus("mandatory")


class _SfrapSysPPPSupported_Type(DisplayString):
    """Custom type sfrapSysPPPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysPPPSupported_Type.__name__ = "DisplayString"
_SfrapSysPPPSupported_Object = MibScalar
sfrapSysPPPSupported = _SfrapSysPPPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 2),
    _SfrapSysPPPSupported_Type()
)
sfrapSysPPPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysPPPSupported.setStatus("mandatory")


class _SfrapSysRDOSupported_Type(DisplayString):
    """Custom type sfrapSysRDOSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysRDOSupported_Type.__name__ = "DisplayString"
_SfrapSysRDOSupported_Object = MibScalar
sfrapSysRDOSupported = _SfrapSysRDOSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 3),
    _SfrapSysRDOSupported_Type()
)
sfrapSysRDOSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysRDOSupported.setStatus("mandatory")


class _SfrapSysETHSupported_Type(DisplayString):
    """Custom type sfrapSysETHSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysETHSupported_Type.__name__ = "DisplayString"
_SfrapSysETHSupported_Object = MibScalar
sfrapSysETHSupported = _SfrapSysETHSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 4),
    _SfrapSysETHSupported_Type()
)
sfrapSysETHSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysETHSupported.setStatus("mandatory")


class _SfrapSysTKRSupported_Type(DisplayString):
    """Custom type sfrapSysTKRSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysTKRSupported_Type.__name__ = "DisplayString"
_SfrapSysTKRSupported_Object = MibScalar
sfrapSysTKRSupported = _SfrapSysTKRSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 5),
    _SfrapSysTKRSupported_Type()
)
sfrapSysTKRSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysTKRSupported.setStatus("mandatory")


class _SfrapSysExtTimSupported_Type(DisplayString):
    """Custom type sfrapSysExtTimSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysExtTimSupported_Type.__name__ = "DisplayString"
_SfrapSysExtTimSupported_Object = MibScalar
sfrapSysExtTimSupported = _SfrapSysExtTimSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 6),
    _SfrapSysExtTimSupported_Type()
)
sfrapSysExtTimSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysExtTimSupported.setStatus("mandatory")


class _SfrapSysBRISupported_Type(DisplayString):
    """Custom type sfrapSysBRISupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysBRISupported_Type.__name__ = "DisplayString"
_SfrapSysBRISupported_Object = MibScalar
sfrapSysBRISupported = _SfrapSysBRISupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 7),
    _SfrapSysBRISupported_Type()
)
sfrapSysBRISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysBRISupported.setStatus("mandatory")


class _SfrapSysSelDTESupported_Type(DisplayString):
    """Custom type sfrapSysSelDTESupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysSelDTESupported_Type.__name__ = "DisplayString"
_SfrapSysSelDTESupported_Object = MibScalar
sfrapSysSelDTESupported = _SfrapSysSelDTESupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 8),
    _SfrapSysSelDTESupported_Type()
)
sfrapSysSelDTESupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysSelDTESupported.setStatus("mandatory")


class _SfrapSysMLSupported_Type(DisplayString):
    """Custom type sfrapSysMLSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysMLSupported_Type.__name__ = "DisplayString"
_SfrapSysMLSupported_Object = MibScalar
sfrapSysMLSupported = _SfrapSysMLSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 9),
    _SfrapSysMLSupported_Type()
)
sfrapSysMLSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysMLSupported.setStatus("mandatory")
_SfrapSysNumDlcisSupported_Type = Integer32
_SfrapSysNumDlcisSupported_Object = MibScalar
sfrapSysNumDlcisSupported = _SfrapSysNumDlcisSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 10),
    _SfrapSysNumDlcisSupported_Type()
)
sfrapSysNumDlcisSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumDlcisSupported.setStatus("mandatory")
_SfrapSysLTFNumDlcis_Type = Integer32
_SfrapSysLTFNumDlcis_Object = MibScalar
sfrapSysLTFNumDlcis = _SfrapSysLTFNumDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 11),
    _SfrapSysLTFNumDlcis_Type()
)
sfrapSysLTFNumDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysLTFNumDlcis.setStatus("mandatory")
_SfrapSysLTFNumProtocols_Type = Integer32
_SfrapSysLTFNumProtocols_Object = MibScalar
sfrapSysLTFNumProtocols = _SfrapSysLTFNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 12),
    _SfrapSysLTFNumProtocols_Type()
)
sfrapSysLTFNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysLTFNumProtocols.setStatus("mandatory")
_SfrapSysNumUserProtocols_Type = Integer32
_SfrapSysNumUserProtocols_Object = MibScalar
sfrapSysNumUserProtocols = _SfrapSysNumUserProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 13),
    _SfrapSysNumUserProtocols_Type()
)
sfrapSysNumUserProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumUserProtocols.setStatus("mandatory")
_SfrapSysNumSnmpMgrs_Type = Integer32
_SfrapSysNumSnmpMgrs_Object = MibScalar
sfrapSysNumSnmpMgrs = _SfrapSysNumSnmpMgrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 14),
    _SfrapSysNumSnmpMgrs_Type()
)
sfrapSysNumSnmpMgrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumSnmpMgrs.setStatus("mandatory")
_SfrapSysNumDlciNames_Type = Integer32
_SfrapSysNumDlciNames_Object = MibScalar
sfrapSysNumDlciNames = _SfrapSysNumDlciNames_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 15),
    _SfrapSysNumDlciNames_Type()
)
sfrapSysNumDlciNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysNumDlciNames.setStatus("mandatory")


class _SfrapSysHighSpeedSupported_Type(DisplayString):
    """Custom type sfrapSysHighSpeedSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapSysHighSpeedSupported_Type.__name__ = "DisplayString"
_SfrapSysHighSpeedSupported_Object = MibScalar
sfrapSysHighSpeedSupported = _SfrapSysHighSpeedSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 1, 2, 16),
    _SfrapSysHighSpeedSupported_Type()
)
sfrapSysHighSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapSysHighSpeedSupported.setStatus("mandatory")
_SfrapConfiguration_ObjectIdentity = ObjectIdentity
sfrapConfiguration = _SfrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2)
)
_SfrapCfgMgmtTable_ObjectIdentity = ObjectIdentity
sfrapCfgMgmtTable = _SfrapCfgMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1)
)
_SfrapCfgIpTable_ObjectIdentity = ObjectIdentity
sfrapCfgIpTable = _SfrapCfgIpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1)
)
_SfrapCfgIpMyIP_Type = IpAddress
_SfrapCfgIpMyIP_Object = MibScalar
sfrapCfgIpMyIP = _SfrapCfgIpMyIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 1),
    _SfrapCfgIpMyIP_Type()
)
sfrapCfgIpMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpMyIP.setStatus("mandatory")
_SfrapCfgIpPeerIP_Type = IpAddress
_SfrapCfgIpPeerIP_Object = MibScalar
sfrapCfgIpPeerIP = _SfrapCfgIpPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 2),
    _SfrapCfgIpPeerIP_Type()
)
sfrapCfgIpPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpPeerIP.setStatus("mandatory")
_SfrapCfgIpMask_Type = IpAddress
_SfrapCfgIpMask_Object = MibScalar
sfrapCfgIpMask = _SfrapCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 3),
    _SfrapCfgIpMask_Type()
)
sfrapCfgIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpMask.setStatus("mandatory")


class _SfrapCfgIpMaxMTU_Type(Integer32):
    """Custom type sfrapCfgIpMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SfrapCfgIpMaxMTU_Type.__name__ = "Integer32"
_SfrapCfgIpMaxMTU_Object = MibScalar
sfrapCfgIpMaxMTU = _SfrapCfgIpMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 4),
    _SfrapCfgIpMaxMTU_Type()
)
sfrapCfgIpMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpMaxMTU.setStatus("mandatory")


class _SfrapCfgIpChannel_Type(Integer32):
    """Custom type sfrapCfgIpChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-band-dlci", 3),
          ("none", 1),
          ("slip-port", 2))
    )


_SfrapCfgIpChannel_Type.__name__ = "Integer32"
_SfrapCfgIpChannel_Object = MibScalar
sfrapCfgIpChannel = _SfrapCfgIpChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 5),
    _SfrapCfgIpChannel_Type()
)
sfrapCfgIpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgIpChannel.setStatus("mandatory")


class _SfrapCfgIpTelnetEnable_Type(Integer32):
    """Custom type sfrapCfgIpTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-telnet", 2),
          ("enable-telnet", 1))
    )


_SfrapCfgIpTelnetEnable_Type.__name__ = "Integer32"
_SfrapCfgIpTelnetEnable_Object = MibScalar
sfrapCfgIpTelnetEnable = _SfrapCfgIpTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 6),
    _SfrapCfgIpTelnetEnable_Type()
)
sfrapCfgIpTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpTelnetEnable.setStatus("mandatory")


class _SfrapCfgIpTelnetAutoLogOut_Type(Integer32):
    """Custom type sfrapCfgIpTelnetAutoLogOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              10,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("autologout-at-10-minutes", 10),
          ("autologout-at-15-minutes", 1),
          ("autologout-at-3-minutes", 3),
          ("autologout-at-30-minutes", 30),
          ("autologout-at-5-minutes", 5),
          ("autologout-at-60-minutes", 60),
          ("disable-autologout", 2))
    )


_SfrapCfgIpTelnetAutoLogOut_Type.__name__ = "Integer32"
_SfrapCfgIpTelnetAutoLogOut_Object = MibScalar
sfrapCfgIpTelnetAutoLogOut = _SfrapCfgIpTelnetAutoLogOut_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 1, 7),
    _SfrapCfgIpTelnetAutoLogOut_Type()
)
sfrapCfgIpTelnetAutoLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgIpTelnetAutoLogOut.setStatus("mandatory")
_SfrapCfgTftpTable_ObjectIdentity = ObjectIdentity
sfrapCfgTftpTable = _SfrapCfgTftpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2)
)


class _SfrapCfgTftpInitiate_Type(DisplayString):
    """Custom type sfrapCfgTftpInitiate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapCfgTftpInitiate_Type.__name__ = "DisplayString"
_SfrapCfgTftpInitiate_Object = MibScalar
sfrapCfgTftpInitiate = _SfrapCfgTftpInitiate_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 1),
    _SfrapCfgTftpInitiate_Type()
)
sfrapCfgTftpInitiate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgTftpInitiate.setStatus("mandatory")
_SfrapCfgTftpIpAddress_Type = IpAddress
_SfrapCfgTftpIpAddress_Object = MibScalar
sfrapCfgTftpIpAddress = _SfrapCfgTftpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 2),
    _SfrapCfgTftpIpAddress_Type()
)
sfrapCfgTftpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpIpAddress.setStatus("mandatory")


class _SfrapCfgTftpFilename_Type(DisplayString):
    """Custom type sfrapCfgTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SfrapCfgTftpFilename_Type.__name__ = "DisplayString"
_SfrapCfgTftpFilename_Object = MibScalar
sfrapCfgTftpFilename = _SfrapCfgTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 3),
    _SfrapCfgTftpFilename_Type()
)
sfrapCfgTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpFilename.setStatus("mandatory")


class _SfrapCfgTftpInterface_Type(Integer32):
    """Custom type sfrapCfgTftpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slip-interface", 3),
          ("to-dce-interface", 2),
          ("to-dte-interface", 1))
    )


_SfrapCfgTftpInterface_Type.__name__ = "Integer32"
_SfrapCfgTftpInterface_Object = MibScalar
sfrapCfgTftpInterface = _SfrapCfgTftpInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 4),
    _SfrapCfgTftpInterface_Type()
)
sfrapCfgTftpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpInterface.setStatus("mandatory")


class _SfrapCfgTftpDlci_Type(Integer32):
    """Custom type sfrapCfgTftpDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63487),
    )


_SfrapCfgTftpDlci_Type.__name__ = "Integer32"
_SfrapCfgTftpDlci_Object = MibScalar
sfrapCfgTftpDlci = _SfrapCfgTftpDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 5),
    _SfrapCfgTftpDlci_Type()
)
sfrapCfgTftpDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpDlci.setStatus("mandatory")


class _SfrapCfgTftpStatus_Type(Integer32):
    """Custom type sfrapCfgTftpStatus based on Integer32"""
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
        *(("corrupt-file", 9),
          ("file-not-found", 7),
          ("host-no-reply", 6),
          ("inactive", 1),
          ("invalid-file", 8),
          ("programming", 4),
          ("requested", 2),
          ("successful", 10),
          ("transfer-aborted", 5),
          ("transferring", 3))
    )


_SfrapCfgTftpStatus_Type.__name__ = "Integer32"
_SfrapCfgTftpStatus_Object = MibScalar
sfrapCfgTftpStatus = _SfrapCfgTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 6),
    _SfrapCfgTftpStatus_Type()
)
sfrapCfgTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpStatus.setStatus("mandatory")
_SfrapCfgTftpNumBytes_Type = Counter32
_SfrapCfgTftpNumBytes_Object = MibScalar
sfrapCfgTftpNumBytes = _SfrapCfgTftpNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 2, 7),
    _SfrapCfgTftpNumBytes_Type()
)
sfrapCfgTftpNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgTftpNumBytes.setStatus("mandatory")
_SfrapCfgSnmpTable_ObjectIdentity = ObjectIdentity
sfrapCfgSnmpTable = _SfrapCfgSnmpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3)
)


class _SfrapCfgSnmpFrTrap_Type(Integer32):
    """Custom type sfrapCfgSnmpFrTrap based on Integer32"""
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


_SfrapCfgSnmpFrTrap_Type.__name__ = "Integer32"
_SfrapCfgSnmpFrTrap_Object = MibScalar
sfrapCfgSnmpFrTrap = _SfrapCfgSnmpFrTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 1),
    _SfrapCfgSnmpFrTrap_Type()
)
sfrapCfgSnmpFrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpFrTrap.setStatus("mandatory")
_SfrapCfgSnmpMgrTable_Object = MibTable
sfrapCfgSnmpMgrTable = _SfrapCfgSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrTable.setStatus("mandatory")
_SfrapCfgSnmpMgrEntry_Object = MibTableRow
sfrapCfgSnmpMgrEntry = _SfrapCfgSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2, 1)
)
sfrapCfgSnmpMgrEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgSnmpMgrIndex"),
)
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrEntry.setStatus("mandatory")
_SfrapCfgSnmpMgrIndex_Type = Integer32
_SfrapCfgSnmpMgrIndex_Object = MibTableColumn
sfrapCfgSnmpMgrIndex = _SfrapCfgSnmpMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2, 1, 1),
    _SfrapCfgSnmpMgrIndex_Type()
)
sfrapCfgSnmpMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrIndex.setStatus("mandatory")
_SfrapCfgSnmpMgrIP_Type = IpAddress
_SfrapCfgSnmpMgrIP_Object = MibTableColumn
sfrapCfgSnmpMgrIP = _SfrapCfgSnmpMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2, 1, 2),
    _SfrapCfgSnmpMgrIP_Type()
)
sfrapCfgSnmpMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrIP.setStatus("mandatory")


class _SfrapCfgSnmpMgrInterface_Type(Integer32):
    """Custom type sfrapCfgSnmpMgrInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slip-interface", 3),
          ("to-dce-interface", 2),
          ("to-dte-interface", 1))
    )


_SfrapCfgSnmpMgrInterface_Type.__name__ = "Integer32"
_SfrapCfgSnmpMgrInterface_Object = MibTableColumn
sfrapCfgSnmpMgrInterface = _SfrapCfgSnmpMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2, 1, 3),
    _SfrapCfgSnmpMgrInterface_Type()
)
sfrapCfgSnmpMgrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrInterface.setStatus("mandatory")
_SfrapCfgSnmpMgrDlci_Type = Integer32
_SfrapCfgSnmpMgrDlci_Object = MibTableColumn
sfrapCfgSnmpMgrDlci = _SfrapCfgSnmpMgrDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 2, 1, 4),
    _SfrapCfgSnmpMgrDlci_Type()
)
sfrapCfgSnmpMgrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrDlci.setStatus("mandatory")


class _SfrapCfgSnmpTrapMuting_Type(Integer32):
    """Custom type sfrapCfgSnmpTrapMuting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_SfrapCfgSnmpTrapMuting_Type.__name__ = "Integer32"
_SfrapCfgSnmpTrapMuting_Object = MibScalar
sfrapCfgSnmpTrapMuting = _SfrapCfgSnmpTrapMuting_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 3),
    _SfrapCfgSnmpTrapMuting_Type()
)
sfrapCfgSnmpTrapMuting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpTrapMuting.setStatus("mandatory")


class _SfrapCfgSnmpUtilTrapEnable_Type(Integer32):
    """Custom type sfrapCfgSnmpUtilTrapEnable based on Integer32"""
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


_SfrapCfgSnmpUtilTrapEnable_Type.__name__ = "Integer32"
_SfrapCfgSnmpUtilTrapEnable_Object = MibScalar
sfrapCfgSnmpUtilTrapEnable = _SfrapCfgSnmpUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 6),
    _SfrapCfgSnmpUtilTrapEnable_Type()
)
sfrapCfgSnmpUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSnmpUtilTrapEnable.setStatus("mandatory")
_SfrapCfgSnmpMgrClearN_Type = Integer32
_SfrapCfgSnmpMgrClearN_Object = MibScalar
sfrapCfgSnmpMgrClearN = _SfrapCfgSnmpMgrClearN_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 3, 7),
    _SfrapCfgSnmpMgrClearN_Type()
)
sfrapCfgSnmpMgrClearN.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgSnmpMgrClearN.setStatus("mandatory")
_SfrapCfgCommTable_ObjectIdentity = ObjectIdentity
sfrapCfgCommTable = _SfrapCfgCommTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4)
)


class _SfrapCfgCommMode_Type(Integer32):
    """Custom type sfrapCfgCommMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slip", 2),
          ("vt100", 1))
    )


_SfrapCfgCommMode_Type.__name__ = "Integer32"
_SfrapCfgCommMode_Object = MibScalar
sfrapCfgCommMode = _SfrapCfgCommMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 1),
    _SfrapCfgCommMode_Type()
)
sfrapCfgCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommMode.setStatus("mandatory")


class _SfrapCfgCommBaud_Type(Integer32):
    """Custom type sfrapCfgCommBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("baud-19200", 5),
          ("baud-2400", 2),
          ("baud-38400", 6),
          ("baud-9600", 4))
    )


_SfrapCfgCommBaud_Type.__name__ = "Integer32"
_SfrapCfgCommBaud_Object = MibScalar
sfrapCfgCommBaud = _SfrapCfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 2),
    _SfrapCfgCommBaud_Type()
)
sfrapCfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommBaud.setStatus("mandatory")


class _SfrapCfgCommDataBits_Type(Integer32):
    """Custom type sfrapCfgCommDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_SfrapCfgCommDataBits_Type.__name__ = "Integer32"
_SfrapCfgCommDataBits_Object = MibScalar
sfrapCfgCommDataBits = _SfrapCfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 3),
    _SfrapCfgCommDataBits_Type()
)
sfrapCfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommDataBits.setStatus("mandatory")


class _SfrapCfgCommStopBits_Type(Integer32):
    """Custom type sfrapCfgCommStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-1-5", 2),
          ("stopbits-2", 3))
    )


_SfrapCfgCommStopBits_Type.__name__ = "Integer32"
_SfrapCfgCommStopBits_Object = MibScalar
sfrapCfgCommStopBits = _SfrapCfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 4),
    _SfrapCfgCommStopBits_Type()
)
sfrapCfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommStopBits.setStatus("mandatory")


class _SfrapCfgCommParity_Type(Integer32):
    """Custom type sfrapCfgCommParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even-parity", 3),
          ("no-parity", 1),
          ("odd-parity", 2))
    )


_SfrapCfgCommParity_Type.__name__ = "Integer32"
_SfrapCfgCommParity_Object = MibScalar
sfrapCfgCommParity = _SfrapCfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 5),
    _SfrapCfgCommParity_Type()
)
sfrapCfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommParity.setStatus("mandatory")


class _SfrapCfgCommFlowCtrl_Type(Integer32):
    """Custom type sfrapCfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("no-flow-control", 1)
    )


_SfrapCfgCommFlowCtrl_Type.__name__ = "Integer32"
_SfrapCfgCommFlowCtrl_Object = MibScalar
sfrapCfgCommFlowCtrl = _SfrapCfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 4, 6),
    _SfrapCfgCommFlowCtrl_Type()
)
sfrapCfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCommFlowCtrl.setStatus("mandatory")
_SfrapCfgFrDLCITable_ObjectIdentity = ObjectIdentity
sfrapCfgFrDLCITable = _SfrapCfgFrDLCITable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 5)
)


class _SfrapCfgFrDLCIMode_Type(Integer32):
    """Custom type sfrapCfgFrDLCIMode based on Integer32"""
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
        *(("bidirectional", 4),
          ("fixedDCE", 6),
          ("inactive", 1),
          ("local-to-dte", 2),
          ("piggyback", 5),
          ("remote-to-dce", 3))
    )


_SfrapCfgFrDLCIMode_Type.__name__ = "Integer32"
_SfrapCfgFrDLCIMode_Object = MibScalar
sfrapCfgFrDLCIMode = _SfrapCfgFrDLCIMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 5, 1),
    _SfrapCfgFrDLCIMode_Type()
)
sfrapCfgFrDLCIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrDLCIMode.setStatus("mandatory")


class _SfrapCfgFrDLCIValue_Type(Integer32):
    """Custom type sfrapCfgFrDLCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 63487),
    )


_SfrapCfgFrDLCIValue_Type.__name__ = "Integer32"
_SfrapCfgFrDLCIValue_Object = MibScalar
sfrapCfgFrDLCIValue = _SfrapCfgFrDLCIValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 5, 2),
    _SfrapCfgFrDLCIValue_Type()
)
sfrapCfgFrDLCIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrDLCIValue.setStatus("mandatory")


class _SfrapCfgFrDLCIEncap_Type(Integer32):
    """Custom type sfrapCfgFrDLCIEncap based on Integer32"""
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
        *(("auto", 3),
          ("cisco", 4),
          ("rfc1490", 1),
          ("rfc1490snap", 2))
    )


_SfrapCfgFrDLCIEncap_Type.__name__ = "Integer32"
_SfrapCfgFrDLCIEncap_Object = MibScalar
sfrapCfgFrDLCIEncap = _SfrapCfgFrDLCIEncap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 5, 3),
    _SfrapCfgFrDLCIEncap_Type()
)
sfrapCfgFrDLCIEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrDLCIEncap.setStatus("mandatory")


class _SfrapCfgFrDLCIMgmtDE_Type(Integer32):
    """Custom type sfrapCfgFrDLCIMgmtDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-DE-bit-0", 1),
          ("yes-DE-bit-1", 2))
    )


_SfrapCfgFrDLCIMgmtDE_Type.__name__ = "Integer32"
_SfrapCfgFrDLCIMgmtDE_Object = MibScalar
sfrapCfgFrDLCIMgmtDE = _SfrapCfgFrDLCIMgmtDE_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 1, 5, 4),
    _SfrapCfgFrDLCIMgmtDE_Type()
)
sfrapCfgFrDLCIMgmtDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrDLCIMgmtDE.setStatus("mandatory")
_SfrapCfgAppTable_ObjectIdentity = ObjectIdentity
sfrapCfgAppTable = _SfrapCfgAppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2)
)


class _SfrapCfgAppCircuitId_Type(DisplayString):
    """Custom type sfrapCfgAppCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SfrapCfgAppCircuitId_Type.__name__ = "DisplayString"
_SfrapCfgAppCircuitId_Object = MibScalar
sfrapCfgAppCircuitId = _SfrapCfgAppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 2),
    _SfrapCfgAppCircuitId_Type()
)
sfrapCfgAppCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppCircuitId.setStatus("mandatory")


class _SfrapCfgAppType_Type(Integer32):
    """Custom type sfrapCfgAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("frame-relay", 2))
    )


_SfrapCfgAppType_Type.__name__ = "Integer32"
_SfrapCfgAppType_Object = MibScalar
sfrapCfgAppType = _SfrapCfgAppType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 3),
    _SfrapCfgAppType_Type()
)
sfrapCfgAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppType.setStatus("mandatory")


class _SfrapCfgAppFormat_Type(Integer32):
    """Custom type sfrapCfgAppFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbo", 1),
          ("hdlc", 2))
    )


_SfrapCfgAppFormat_Type.__name__ = "Integer32"
_SfrapCfgAppFormat_Object = MibScalar
sfrapCfgAppFormat = _SfrapCfgAppFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 4),
    _SfrapCfgAppFormat_Type()
)
sfrapCfgAppFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppFormat.setStatus("mandatory")


class _SfrapCfgAppLpbkTimeout_Type(Integer32):
    """Custom type sfrapCfgAppLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SfrapCfgAppLpbkTimeout_Type.__name__ = "Integer32"
_SfrapCfgAppLpbkTimeout_Object = MibScalar
sfrapCfgAppLpbkTimeout = _SfrapCfgAppLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 5),
    _SfrapCfgAppLpbkTimeout_Type()
)
sfrapCfgAppLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppLpbkTimeout.setStatus("mandatory")


class _SfrapCfgAppTxClkmode_Type(Integer32):
    """Custom type sfrapCfgAppTxClkmode based on Integer32"""
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
        *(("invert-TO-DCE", 2),
          ("invert-TO-DTE", 3),
          ("invert-timing", 4),
          ("normal-timing", 1))
    )


_SfrapCfgAppTxClkmode_Type.__name__ = "Integer32"
_SfrapCfgAppTxClkmode_Object = MibScalar
sfrapCfgAppTxClkmode = _SfrapCfgAppTxClkmode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 6),
    _SfrapCfgAppTxClkmode_Type()
)
sfrapCfgAppTxClkmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppTxClkmode.setStatus("mandatory")


class _SfrapCfgAppTxtiming_Type(Integer32):
    """Custom type sfrapCfgAppTxtiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loop-1", 1),
          ("loop-2", 2),
          ("source-tt", 3))
    )


_SfrapCfgAppTxtiming_Type.__name__ = "Integer32"
_SfrapCfgAppTxtiming_Object = MibScalar
sfrapCfgAppTxtiming = _SfrapCfgAppTxtiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 7),
    _SfrapCfgAppTxtiming_Type()
)
sfrapCfgAppTxtiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppTxtiming.setStatus("mandatory")


class _SfrapCfgAppOperationMode_Type(Integer32):
    """Custom type sfrapCfgAppOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 2),
          ("tap", 1))
    )


_SfrapCfgAppOperationMode_Type.__name__ = "Integer32"
_SfrapCfgAppOperationMode_Object = MibScalar
sfrapCfgAppOperationMode = _SfrapCfgAppOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 8),
    _SfrapCfgAppOperationMode_Type()
)
sfrapCfgAppOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppOperationMode.setStatus("mandatory")


class _SfrapCfgAppCutthruTimeout_Type(Integer32):
    """Custom type sfrapCfgAppCutthruTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SfrapCfgAppCutthruTimeout_Type.__name__ = "Integer32"
_SfrapCfgAppCutthruTimeout_Object = MibScalar
sfrapCfgAppCutthruTimeout = _SfrapCfgAppCutthruTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 9),
    _SfrapCfgAppCutthruTimeout_Type()
)
sfrapCfgAppCutthruTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppCutthruTimeout.setStatus("mandatory")


class _SfrapCfgAppPerfBuffLimit_Type(Integer32):
    """Custom type sfrapCfgAppPerfBuffLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_SfrapCfgAppPerfBuffLimit_Type.__name__ = "Integer32"
_SfrapCfgAppPerfBuffLimit_Object = MibScalar
sfrapCfgAppPerfBuffLimit = _SfrapCfgAppPerfBuffLimit_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 2, 10),
    _SfrapCfgAppPerfBuffLimit_Type()
)
sfrapCfgAppPerfBuffLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgAppPerfBuffLimit.setStatus("mandatory")
_SfrapCfgDteTable_Object = MibTable
sfrapCfgDteTable = _SfrapCfgDteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4)
)
if mibBuilder.loadTexts:
    sfrapCfgDteTable.setStatus("mandatory")
_SfrapCfgDteEntry_Object = MibTableRow
sfrapCfgDteEntry = _SfrapCfgDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1)
)
sfrapCfgDteEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgDteIndex"),
)
if mibBuilder.loadTexts:
    sfrapCfgDteEntry.setStatus("mandatory")


class _SfrapCfgDteIntfType_Type(Integer32):
    """Custom type sfrapCfgDteIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("intf-rs449", 4),
          ("intf-v35", 3),
          ("intf-x21", 5))
    )


_SfrapCfgDteIntfType_Type.__name__ = "Integer32"
_SfrapCfgDteIntfType_Object = MibTableColumn
sfrapCfgDteIntfType = _SfrapCfgDteIntfType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1, 1),
    _SfrapCfgDteIntfType_Type()
)
sfrapCfgDteIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgDteIntfType.setStatus("mandatory")


class _SfrapCfgDteTxClockMode_Type(Integer32):
    """Custom type sfrapCfgDteTxClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clock-invert", 2),
          ("clock-normal", 1))
    )


_SfrapCfgDteTxClockMode_Type.__name__ = "Integer32"
_SfrapCfgDteTxClockMode_Object = MibTableColumn
sfrapCfgDteTxClockMode = _SfrapCfgDteTxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1, 3),
    _SfrapCfgDteTxClockMode_Type()
)
sfrapCfgDteTxClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgDteTxClockMode.setStatus("mandatory")


class _SfrapCfgDteRxClockMode_Type(Integer32):
    """Custom type sfrapCfgDteRxClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clock-auto", 3),
          ("clock-invert", 2),
          ("clock-normal", 1))
    )


_SfrapCfgDteRxClockMode_Type.__name__ = "Integer32"
_SfrapCfgDteRxClockMode_Object = MibTableColumn
sfrapCfgDteRxClockMode = _SfrapCfgDteRxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1, 21),
    _SfrapCfgDteRxClockMode_Type()
)
sfrapCfgDteRxClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgDteRxClockMode.setStatus("mandatory")


class _SfrapCfgDteRtsC_Type(Integer32):
    """Custom type sfrapCfgDteRtsC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal-assumed-active", 1),
          ("signal-monitored", 2))
    )


_SfrapCfgDteRtsC_Type.__name__ = "Integer32"
_SfrapCfgDteRtsC_Object = MibTableColumn
sfrapCfgDteRtsC = _SfrapCfgDteRtsC_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1, 22),
    _SfrapCfgDteRtsC_Type()
)
sfrapCfgDteRtsC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgDteRtsC.setStatus("mandatory")


class _SfrapCfgDteIndex_Type(Integer32):
    """Custom type sfrapCfgDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce", 2),
          ("to-dte", 1))
    )


_SfrapCfgDteIndex_Type.__name__ = "Integer32"
_SfrapCfgDteIndex_Object = MibTableColumn
sfrapCfgDteIndex = _SfrapCfgDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 4, 1, 99),
    _SfrapCfgDteIndex_Type()
)
sfrapCfgDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgDteIndex.setStatus("mandatory")
_SfrapCfgFrTable_ObjectIdentity = ObjectIdentity
sfrapCfgFrTable = _SfrapCfgFrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5)
)


class _SfrapCfgFrAddrLen_Type(Integer32):
    """Custom type sfrapCfgFrAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourbytes", 3),
          ("threebytes", 2),
          ("twobytes", 1))
    )


_SfrapCfgFrAddrLen_Type.__name__ = "Integer32"
_SfrapCfgFrAddrLen_Object = MibScalar
sfrapCfgFrAddrLen = _SfrapCfgFrAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 1),
    _SfrapCfgFrAddrLen_Type()
)
sfrapCfgFrAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrAddrLen.setStatus("mandatory")


class _SfrapCfgFrCrcMode_Type(Integer32):
    """Custom type sfrapCfgFrCrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("passthru", 2))
    )


_SfrapCfgFrCrcMode_Type.__name__ = "Integer32"
_SfrapCfgFrCrcMode_Object = MibScalar
sfrapCfgFrCrcMode = _SfrapCfgFrCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 2),
    _SfrapCfgFrCrcMode_Type()
)
sfrapCfgFrCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrCrcMode.setStatus("mandatory")


class _SfrapCfgFrLmiType_Type(Integer32):
    """Custom type sfrapCfgFrLmiType based on Integer32"""
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
        *(("annexa", 2),
          ("annexd", 1),
          ("autosense", 4),
          ("type1", 3))
    )


_SfrapCfgFrLmiType_Type.__name__ = "Integer32"
_SfrapCfgFrLmiType_Object = MibScalar
sfrapCfgFrLmiType = _SfrapCfgFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 3),
    _SfrapCfgFrLmiType_Type()
)
sfrapCfgFrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrLmiType.setStatus("mandatory")


class _SfrapCfgFrLmiInactivityTimeout_Type(Integer32):
    """Custom type sfrapCfgFrLmiInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SfrapCfgFrLmiInactivityTimeout_Type.__name__ = "Integer32"
_SfrapCfgFrLmiInactivityTimeout_Object = MibScalar
sfrapCfgFrLmiInactivityTimeout = _SfrapCfgFrLmiInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 4),
    _SfrapCfgFrLmiInactivityTimeout_Type()
)
sfrapCfgFrLmiInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrLmiInactivityTimeout.setStatus("mandatory")


class _SfrapCfgFrLmiKeepaliveTimeout_Type(Integer32):
    """Custom type sfrapCfgFrLmiKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_SfrapCfgFrLmiKeepaliveTimeout_Type.__name__ = "Integer32"
_SfrapCfgFrLmiKeepaliveTimeout_Object = MibScalar
sfrapCfgFrLmiKeepaliveTimeout = _SfrapCfgFrLmiKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 5),
    _SfrapCfgFrLmiKeepaliveTimeout_Type()
)
sfrapCfgFrLmiKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrLmiKeepaliveTimeout.setStatus("mandatory")


class _SfrapCfgFrAddrResMode_Type(Integer32):
    """Custom type sfrapCfgFrAddrResMode based on Integer32"""
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
        *(("arp", 2),
          ("both", 4),
          ("inactive", 1),
          ("inarp", 3))
    )


_SfrapCfgFrAddrResMode_Type.__name__ = "Integer32"
_SfrapCfgFrAddrResMode_Object = MibScalar
sfrapCfgFrAddrResMode = _SfrapCfgFrAddrResMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 6),
    _SfrapCfgFrAddrResMode_Type()
)
sfrapCfgFrAddrResMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrAddrResMode.setStatus("mandatory")


class _SfrapCfgFrAddrResInarpTimer_Type(Integer32):
    """Custom type sfrapCfgFrAddrResInarpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SfrapCfgFrAddrResInarpTimer_Type.__name__ = "Integer32"
_SfrapCfgFrAddrResInarpTimer_Object = MibScalar
sfrapCfgFrAddrResInarpTimer = _SfrapCfgFrAddrResInarpTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 7),
    _SfrapCfgFrAddrResInarpTimer_Type()
)
sfrapCfgFrAddrResInarpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrAddrResInarpTimer.setStatus("mandatory")


class _SfrapCfgFrLmiFullStatus_Type(Integer32):
    """Custom type sfrapCfgFrLmiFullStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SfrapCfgFrLmiFullStatus_Type.__name__ = "Integer32"
_SfrapCfgFrLmiFullStatus_Object = MibScalar
sfrapCfgFrLmiFullStatus = _SfrapCfgFrLmiFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 8),
    _SfrapCfgFrLmiFullStatus_Type()
)
sfrapCfgFrLmiFullStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrLmiFullStatus.setStatus("mandatory")


class _SfrapCfgFrAddrResDlcis_Type(Integer32):
    """Custom type sfrapCfgFrAddrResDlcis based on Integer32"""
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
        *(("multiple", 2),
          ("single", 1),
          ("todcemulti", 3),
          ("todtemulti", 4))
    )


_SfrapCfgFrAddrResDlcis_Type.__name__ = "Integer32"
_SfrapCfgFrAddrResDlcis_Object = MibScalar
sfrapCfgFrAddrResDlcis = _SfrapCfgFrAddrResDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 5, 9),
    _SfrapCfgFrAddrResDlcis_Type()
)
sfrapCfgFrAddrResDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrAddrResDlcis.setStatus("mandatory")
_SfrapCfgVnipTable_ObjectIdentity = ObjectIdentity
sfrapCfgVnipTable = _SfrapCfgVnipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6)
)


class _SfrapCfgVnipMode_Type(Integer32):
    """Custom type sfrapCfgVnipMode based on Integer32"""
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
          ("inactive", 1),
          ("to-dce", 3),
          ("to-dte", 2))
    )


_SfrapCfgVnipMode_Type.__name__ = "Integer32"
_SfrapCfgVnipMode_Object = MibScalar
sfrapCfgVnipMode = _SfrapCfgVnipMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 1),
    _SfrapCfgVnipMode_Type()
)
sfrapCfgVnipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgVnipMode.setStatus("mandatory")


class _SfrapCfgVnipInitTimer_Type(Integer32):
    """Custom type sfrapCfgVnipInitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SfrapCfgVnipInitTimer_Type.__name__ = "Integer32"
_SfrapCfgVnipInitTimer_Object = MibScalar
sfrapCfgVnipInitTimer = _SfrapCfgVnipInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 2),
    _SfrapCfgVnipInitTimer_Type()
)
sfrapCfgVnipInitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgVnipInitTimer.setStatus("mandatory")


class _SfrapCfgVnipTxTimer_Type(Integer32):
    """Custom type sfrapCfgVnipTxTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SfrapCfgVnipTxTimer_Type.__name__ = "Integer32"
_SfrapCfgVnipTxTimer_Object = MibScalar
sfrapCfgVnipTxTimer = _SfrapCfgVnipTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 3),
    _SfrapCfgVnipTxTimer_Type()
)
sfrapCfgVnipTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgVnipTxTimer.setStatus("mandatory")


class _SfrapCfgVnipRxTimer_Type(Integer32):
    """Custom type sfrapCfgVnipRxTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SfrapCfgVnipRxTimer_Type.__name__ = "Integer32"
_SfrapCfgVnipRxTimer_Object = MibScalar
sfrapCfgVnipRxTimer = _SfrapCfgVnipRxTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 4),
    _SfrapCfgVnipRxTimer_Type()
)
sfrapCfgVnipRxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgVnipRxTimer.setStatus("mandatory")


class _SfrapCfgVnipTransitDelayFrequency_Type(Integer32):
    """Custom type sfrapCfgVnipTransitDelayFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_SfrapCfgVnipTransitDelayFrequency_Type.__name__ = "Integer32"
_SfrapCfgVnipTransitDelayFrequency_Object = MibScalar
sfrapCfgVnipTransitDelayFrequency = _SfrapCfgVnipTransitDelayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 5),
    _SfrapCfgVnipTransitDelayFrequency_Type()
)
sfrapCfgVnipTransitDelayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgVnipTransitDelayFrequency.setStatus("mandatory")
_SfrapCfgTransitDelayTable_Object = MibTable
sfrapCfgTransitDelayTable = _SfrapCfgTransitDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20)
)
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayTable.setStatus("mandatory")
_SfrapCfgTransitDelayEntry_Object = MibTableRow
sfrapCfgTransitDelayEntry = _SfrapCfgTransitDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1)
)
sfrapCfgTransitDelayEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgTransitDelayInterface"),
    (0, "SFRAP-MIB", "sfrapCfgTransitDelayDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayEntry.setStatus("mandatory")


class _SfrapCfgTransitDelayInterface_Type(Integer32):
    """Custom type sfrapCfgTransitDelayInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce-interface", 2),
          ("to-dte-interface", 1))
    )


_SfrapCfgTransitDelayInterface_Type.__name__ = "Integer32"
_SfrapCfgTransitDelayInterface_Object = MibTableColumn
sfrapCfgTransitDelayInterface = _SfrapCfgTransitDelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1, 1),
    _SfrapCfgTransitDelayInterface_Type()
)
sfrapCfgTransitDelayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayInterface.setStatus("mandatory")
_SfrapCfgTransitDelayDlciValue_Type = Integer32
_SfrapCfgTransitDelayDlciValue_Object = MibTableColumn
sfrapCfgTransitDelayDlciValue = _SfrapCfgTransitDelayDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1, 2),
    _SfrapCfgTransitDelayDlciValue_Type()
)
sfrapCfgTransitDelayDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayDlciValue.setStatus("mandatory")


class _SfrapCfgTransitDelayNumHops_Type(Integer32):
    """Custom type sfrapCfgTransitDelayNumHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SfrapCfgTransitDelayNumHops_Type.__name__ = "Integer32"
_SfrapCfgTransitDelayNumHops_Object = MibTableColumn
sfrapCfgTransitDelayNumHops = _SfrapCfgTransitDelayNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1, 4),
    _SfrapCfgTransitDelayNumHops_Type()
)
sfrapCfgTransitDelayNumHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayNumHops.setStatus("mandatory")


class _SfrapCfgTransitDelayRcvSummaryCancel_Type(Integer32):
    """Custom type sfrapCfgTransitDelayRcvSummaryCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-rsc", 2),
          ("enable-rsc", 1))
    )


_SfrapCfgTransitDelayRcvSummaryCancel_Type.__name__ = "Integer32"
_SfrapCfgTransitDelayRcvSummaryCancel_Object = MibTableColumn
sfrapCfgTransitDelayRcvSummaryCancel = _SfrapCfgTransitDelayRcvSummaryCancel_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1, 5),
    _SfrapCfgTransitDelayRcvSummaryCancel_Type()
)
sfrapCfgTransitDelayRcvSummaryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayRcvSummaryCancel.setStatus("mandatory")


class _SfrapCfgTransitDelayThreshold_Type(Integer32):
    """Custom type sfrapCfgTransitDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_SfrapCfgTransitDelayThreshold_Type.__name__ = "Integer32"
_SfrapCfgTransitDelayThreshold_Object = MibTableColumn
sfrapCfgTransitDelayThreshold = _SfrapCfgTransitDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 20, 1, 6),
    _SfrapCfgTransitDelayThreshold_Type()
)
sfrapCfgTransitDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayThreshold.setStatus("mandatory")
_SfrapCfgTDDeleteTable_Object = MibTable
sfrapCfgTDDeleteTable = _SfrapCfgTDDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 21)
)
if mibBuilder.loadTexts:
    sfrapCfgTDDeleteTable.setStatus("mandatory")
_SfrapCfgTDDeleteEntry_Object = MibTableRow
sfrapCfgTDDeleteEntry = _SfrapCfgTDDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 21, 1)
)
sfrapCfgTDDeleteEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgTDDeleteInterface"),
)
if mibBuilder.loadTexts:
    sfrapCfgTDDeleteEntry.setStatus("mandatory")


class _SfrapCfgTDDeleteInterface_Type(Integer32):
    """Custom type sfrapCfgTDDeleteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce-interface", 2),
          ("to-dte-interface", 1))
    )


_SfrapCfgTDDeleteInterface_Type.__name__ = "Integer32"
_SfrapCfgTDDeleteInterface_Object = MibTableColumn
sfrapCfgTDDeleteInterface = _SfrapCfgTDDeleteInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 21, 1, 1),
    _SfrapCfgTDDeleteInterface_Type()
)
sfrapCfgTDDeleteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfrapCfgTDDeleteInterface.setStatus("mandatory")
_SfrapCfgTDDeleteDlciValue_Type = Integer32
_SfrapCfgTDDeleteDlciValue_Object = MibTableColumn
sfrapCfgTDDeleteDlciValue = _SfrapCfgTDDeleteDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 21, 1, 2),
    _SfrapCfgTDDeleteDlciValue_Type()
)
sfrapCfgTDDeleteDlciValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgTDDeleteDlciValue.setStatus("mandatory")


class _SfrapCfgTransitDelayTableClear_Type(Integer32):
    """Custom type sfrapCfgTransitDelayTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_SfrapCfgTransitDelayTableClear_Type.__name__ = "Integer32"
_SfrapCfgTransitDelayTableClear_Object = MibScalar
sfrapCfgTransitDelayTableClear = _SfrapCfgTransitDelayTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 6, 22),
    _SfrapCfgTransitDelayTableClear_Type()
)
sfrapCfgTransitDelayTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgTransitDelayTableClear.setStatus("mandatory")
_SfrapCfgFrPerf_ObjectIdentity = ObjectIdentity
sfrapCfgFrPerf = _SfrapCfgFrPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7)
)
_SfrapCfgFrPerfDlciNamesTable_Object = MibTable
sfrapCfgFrPerfDlciNamesTable = _SfrapCfgFrPerfDlciNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesTable.setStatus("mandatory")
_SfrapCfgFrPerfDlciNamesEntry_Object = MibTableRow
sfrapCfgFrPerfDlciNamesEntry = _SfrapCfgFrPerfDlciNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1)
)
sfrapCfgFrPerfDlciNamesEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgFrPerfDlciNamesDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesEntry.setStatus("mandatory")
_SfrapCfgFrPerfDlciNamesDlciValue_Type = Integer32
_SfrapCfgFrPerfDlciNamesDlciValue_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesDlciValue = _SfrapCfgFrPerfDlciNamesDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 1),
    _SfrapCfgFrPerfDlciNamesDlciValue_Type()
)
sfrapCfgFrPerfDlciNamesDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesDlciValue.setStatus("mandatory")


class _SfrapCfgFrPerfDlciNamesDlciName_Type(DisplayString):
    """Custom type sfrapCfgFrPerfDlciNamesDlciName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SfrapCfgFrPerfDlciNamesDlciName_Type.__name__ = "DisplayString"
_SfrapCfgFrPerfDlciNamesDlciName_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesDlciName = _SfrapCfgFrPerfDlciNamesDlciName_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 2),
    _SfrapCfgFrPerfDlciNamesDlciName_Type()
)
sfrapCfgFrPerfDlciNamesDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesDlciName.setStatus("mandatory")
_SfrapCfgFrPerfDlciNamesCirValue_Type = Integer32
_SfrapCfgFrPerfDlciNamesCirValue_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesCirValue = _SfrapCfgFrPerfDlciNamesCirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 3),
    _SfrapCfgFrPerfDlciNamesCirValue_Type()
)
sfrapCfgFrPerfDlciNamesCirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesCirValue.setStatus("mandatory")


class _SfrapCfgFrPerfDlciNamesCirType_Type(Integer32):
    """Custom type sfrapCfgFrPerfDlciNamesCirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cir-acquired-from-lmi", 1),
          ("cir-configured-by-user", 2),
          ("cir-is-datarate", 3))
    )


_SfrapCfgFrPerfDlciNamesCirType_Type.__name__ = "Integer32"
_SfrapCfgFrPerfDlciNamesCirType_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesCirType = _SfrapCfgFrPerfDlciNamesCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 4),
    _SfrapCfgFrPerfDlciNamesCirType_Type()
)
sfrapCfgFrPerfDlciNamesCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesCirType.setStatus("mandatory")


class _SfrapCfgFrPerfDlciNamesUtilThreshold_Type(Integer32):
    """Custom type sfrapCfgFrPerfDlciNamesUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfrapCfgFrPerfDlciNamesUtilThreshold_Type.__name__ = "Integer32"
_SfrapCfgFrPerfDlciNamesUtilThreshold_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesUtilThreshold = _SfrapCfgFrPerfDlciNamesUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 5),
    _SfrapCfgFrPerfDlciNamesUtilThreshold_Type()
)
sfrapCfgFrPerfDlciNamesUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesUtilThreshold.setStatus("mandatory")
_SfrapCfgFrPerfDlciNamesEirValue_Type = Integer32
_SfrapCfgFrPerfDlciNamesEirValue_Object = MibTableColumn
sfrapCfgFrPerfDlciNamesEirValue = _SfrapCfgFrPerfDlciNamesEirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 1, 1, 6),
    _SfrapCfgFrPerfDlciNamesEirValue_Type()
)
sfrapCfgFrPerfDlciNamesEirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesEirValue.setStatus("mandatory")
_SfrapCfgFrPerfDlciNamesDelete_Type = Integer32
_SfrapCfgFrPerfDlciNamesDelete_Object = MibScalar
sfrapCfgFrPerfDlciNamesDelete = _SfrapCfgFrPerfDlciNamesDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 2),
    _SfrapCfgFrPerfDlciNamesDelete_Type()
)
sfrapCfgFrPerfDlciNamesDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesDelete.setStatus("mandatory")
_SfrapCfgFrPerfTimers_ObjectIdentity = ObjectIdentity
sfrapCfgFrPerfTimers = _SfrapCfgFrPerfTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 3)
)


class _SfrapCfgFrPerfTimersSTInterval_Type(Integer32):
    """Custom type sfrapCfgFrPerfTimersSTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_SfrapCfgFrPerfTimersSTInterval_Type.__name__ = "Integer32"
_SfrapCfgFrPerfTimersSTInterval_Object = MibScalar
sfrapCfgFrPerfTimersSTInterval = _SfrapCfgFrPerfTimersSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 3, 1),
    _SfrapCfgFrPerfTimersSTInterval_Type()
)
sfrapCfgFrPerfTimersSTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfTimersSTInterval.setStatus("mandatory")


class _SfrapCfgFrPerfTimersLTInterval_Type(Integer32):
    """Custom type sfrapCfgFrPerfTimersLTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_SfrapCfgFrPerfTimersLTInterval_Type.__name__ = "Integer32"
_SfrapCfgFrPerfTimersLTInterval_Object = MibScalar
sfrapCfgFrPerfTimersLTInterval = _SfrapCfgFrPerfTimersLTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 3, 2),
    _SfrapCfgFrPerfTimersLTInterval_Type()
)
sfrapCfgFrPerfTimersLTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfTimersLTInterval.setStatus("mandatory")
_SfrapCfgFrPerfUserProtocolsTable_Object = MibTable
sfrapCfgFrPerfUserProtocolsTable = _SfrapCfgFrPerfUserProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 4)
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUserProtocolsTable.setStatus("mandatory")
_SfrapCfgFrPerfUserProtocolsEntry_Object = MibTableRow
sfrapCfgFrPerfUserProtocolsEntry = _SfrapCfgFrPerfUserProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 4, 1)
)
sfrapCfgFrPerfUserProtocolsEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgFrPerfUserProtocolsIndex"),
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUserProtocolsEntry.setStatus("mandatory")
_SfrapCfgFrPerfUserProtocolsIndex_Type = Integer32
_SfrapCfgFrPerfUserProtocolsIndex_Object = MibTableColumn
sfrapCfgFrPerfUserProtocolsIndex = _SfrapCfgFrPerfUserProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 4, 1, 1),
    _SfrapCfgFrPerfUserProtocolsIndex_Type()
)
sfrapCfgFrPerfUserProtocolsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUserProtocolsIndex.setStatus("mandatory")
_SfrapCfgFrPerfUserProtocolsPortNum_Type = Integer32
_SfrapCfgFrPerfUserProtocolsPortNum_Object = MibTableColumn
sfrapCfgFrPerfUserProtocolsPortNum = _SfrapCfgFrPerfUserProtocolsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 4, 1, 2),
    _SfrapCfgFrPerfUserProtocolsPortNum_Type()
)
sfrapCfgFrPerfUserProtocolsPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUserProtocolsPortNum.setStatus("mandatory")
_SfrapCfgFrPerfLTDlciFilterTable_Object = MibTable
sfrapCfgFrPerfLTDlciFilterTable = _SfrapCfgFrPerfLTDlciFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 5)
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTDlciFilterTable.setStatus("mandatory")
_SfrapCfgFrPerfLTDlciFilterEntry_Object = MibTableRow
sfrapCfgFrPerfLTDlciFilterEntry = _SfrapCfgFrPerfLTDlciFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 5, 1)
)
sfrapCfgFrPerfLTDlciFilterEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgFrPerfLTDlciFilterIndex"),
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTDlciFilterEntry.setStatus("mandatory")
_SfrapCfgFrPerfLTDlciFilterIndex_Type = Integer32
_SfrapCfgFrPerfLTDlciFilterIndex_Object = MibTableColumn
sfrapCfgFrPerfLTDlciFilterIndex = _SfrapCfgFrPerfLTDlciFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 5, 1, 1),
    _SfrapCfgFrPerfLTDlciFilterIndex_Type()
)
sfrapCfgFrPerfLTDlciFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTDlciFilterIndex.setStatus("mandatory")
_SfrapCfgFrPerfLTDlciFilterDlciNum_Type = Integer32
_SfrapCfgFrPerfLTDlciFilterDlciNum_Object = MibTableColumn
sfrapCfgFrPerfLTDlciFilterDlciNum = _SfrapCfgFrPerfLTDlciFilterDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 5, 1, 2),
    _SfrapCfgFrPerfLTDlciFilterDlciNum_Type()
)
sfrapCfgFrPerfLTDlciFilterDlciNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTDlciFilterDlciNum.setStatus("mandatory")
_SfrapCfgFrPerfLTProtocolFilterTable_Object = MibTable
sfrapCfgFrPerfLTProtocolFilterTable = _SfrapCfgFrPerfLTProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 6)
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTProtocolFilterTable.setStatus("mandatory")
_SfrapCfgFrPerfLTProtocolFilterEntry_Object = MibTableRow
sfrapCfgFrPerfLTProtocolFilterEntry = _SfrapCfgFrPerfLTProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 6, 1)
)
sfrapCfgFrPerfLTProtocolFilterEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapCfgFrPerfLTProtocolFilterIndex"),
)
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTProtocolFilterEntry.setStatus("mandatory")
_SfrapCfgFrPerfLTProtocolFilterIndex_Type = Integer32
_SfrapCfgFrPerfLTProtocolFilterIndex_Object = MibTableColumn
sfrapCfgFrPerfLTProtocolFilterIndex = _SfrapCfgFrPerfLTProtocolFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 6, 1, 1),
    _SfrapCfgFrPerfLTProtocolFilterIndex_Type()
)
sfrapCfgFrPerfLTProtocolFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTProtocolFilterIndex.setStatus("mandatory")


class _SfrapCfgFrPerfLTProtocolFilterProtocol_Type(Integer32):
    """Custom type sfrapCfgFrPerfLTProtocolFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
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
              13,
              14,
              15,
              16,
              21,
              22,
              29,
              30,
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172)
        )
    )
    namedValues = NamedValues(
        *(("addr-mask-rep-icmp-ip-rx-bc", 64),
          ("addr-mask-rep-icmp-ip-tx-bc", 63),
          ("addr-mask-req-icmp-ip-rx-bc", 62),
          ("addr-mask-req-icmp-ip-tx-bc", 61),
          ("annex-g-rx-bc", 172),
          ("annex-g-tx-bc", 171),
          ("arp-rep-rx-bc", 96),
          ("arp-rep-tx-bc", 95),
          ("arp-req-rx-bc", 94),
          ("arp-req-tx-bc", 93),
          ("arp-rx-bc", 92),
          ("arp-tx-bc", 91),
          ("cir-percent-range1-rx-bc", 138),
          ("cir-percent-range1-tx-bc", 137),
          ("cir-percent-range2-rx-bc", 140),
          ("cir-percent-range2-tx-bc", 139),
          ("cir-percent-range3-rx-bc", 142),
          ("cir-percent-range3-tx-bc", 141),
          ("cir-percent-range4-rx-bc", 144),
          ("cir-percent-range4-tx-bc", 143),
          ("cir-percent-range5-rx-bc", 146),
          ("cir-percent-range5-tx-bc", 145),
          ("cir-percent-range6-rx-bc", 148),
          ("cir-percent-range6-tx-bc", 147),
          ("cir-percent-range7-rx-bc", 150),
          ("cir-percent-range7-tx-bc", 149),
          ("cir-percent-range8-rx-bc", 152),
          ("cir-percent-range8-tx-bc", 151),
          ("cisco-rx-bc", 116),
          ("cisco-tx-bc", 115),
          ("delete-entry", -1),
          ("dest-unr-icmp-ip-rx-bc", 46),
          ("dest-unr-icmp-ip-tx-bc", 45),
          ("echorep-icmp-ip-rx-bc", 44),
          ("echorep-icmp-ip-tx-bc", 43),
          ("echoreq-icmp-ip-rx-bc", 52),
          ("echoreq-icmp-ip-tx-bc", 51),
          ("ftp-tcp-ip-rx-bc", 6),
          ("ftp-tcp-ip-tx-bc", 5),
          ("gp-mem-query-icmp-ip-rx-bc", 68),
          ("gp-mem-query-icmp-ip-tx-bc", 67),
          ("gp-mem-reduct-icmp-ip-rx-bc", 72),
          ("gp-mem-reduct-icmp-ip-tx-bc", 71),
          ("gp-mem-report-icmp-ip-rx-bc", 70),
          ("gp-mem-report-icmp-ip-tx-bc", 69),
          ("http-tcp-ip-rx-bc", 14),
          ("http-tcp-ip-tx-bc", 13),
          ("icmp-ip-rx-bc", 42),
          ("icmp-ip-tx-bc", 41),
          ("igrp-rx-bc", 168),
          ("igrp-tx-bc", 167),
          ("inarp-rep-rx-bc", 104),
          ("inarp-rep-tx-bc", 103),
          ("inarp-req-rx-bc", 102),
          ("inarp-req-tx-bc", 101),
          ("ip-rx-bc", 2),
          ("ip-tx-bc", 1),
          ("ipx-rx-bc", 78),
          ("ipx-tx-bc", 77),
          ("lmi-full-enq-rx-bc", 160),
          ("lmi-full-enq-tx-bc", 159),
          ("lmi-full-stat-rx-bc", 162),
          ("lmi-full-stat-tx-bc", 161),
          ("lmi-livo-enq-rx-bc", 156),
          ("lmi-livo-enq-tx-bc", 155),
          ("lmi-livo-stat-rx-bc", 158),
          ("lmi-livo-stat-tx-bc", 157),
          ("lmi-other-rx-bc", 164),
          ("lmi-other-tx-bc", 163),
          ("lmi-rx-bc", 154),
          ("lmi-tx-bc", 153),
          ("ncp-ipx-rx-bc", 82),
          ("ncp-ipx-tx-bc", 81),
          ("netbios-dgm-udp-ip-rx-bc", 34),
          ("netbios-dgm-udp-ip-tx-bc", 33),
          ("netbios-ipx-rx-bc", 88),
          ("netbios-ipx-tx-bc", 87),
          ("netbios-ssn-tcp-ip-rx-bc", 16),
          ("netbios-ssn-tcp-ip-tx-bc", 15),
          ("ospf-ip-rx-bc", 74),
          ("ospf-ip-tx-bc", 73),
          ("other-ip-rx-bc", 76),
          ("other-ip-tx-bc", 75),
          ("other-ipx-rx-bc", 90),
          ("other-ipx-tx-bc", 89),
          ("other-rx-bc", 118),
          ("other-tx-bc", 117),
          ("param-prob-icmp-ip-rx-bc", 56),
          ("param-prob-icmp-ip-tx-bc", 55),
          ("pkt-too-big-icmp-ip-rx-bc", 66),
          ("pkt-too-big-icmp-ip-tx-bc", 65),
          ("rarp-rep-rx-bc", 100),
          ("rarp-rep-tx-bc", 99),
          ("rarp-req-rx-bc", 98),
          ("rarp-req-tx-bc", 97),
          ("redirect-icmp-ip-rx-bc", 50),
          ("redirect-icmp-ip-tx-bc", 49),
          ("rip-ipx-rx-bc", 86),
          ("rip-ipx-tx-bc", 85),
          ("rip-udp-ip-rx-bc", 40),
          ("rip-udp-ip-tx-bc", 39),
          ("sap-ipx-rx-bc", 84),
          ("sap-ipx-tx-bc", 83),
          ("smtp-tcp-ip-rx-bc", 10),
          ("smtp-tcp-ip-tx-bc", 9),
          ("sna-appn-rx-bc", 112),
          ("sna-appn-tx-bc", 111),
          ("sna-netbios-rx-bc", 114),
          ("sna-netbios-tx-bc", 113),
          ("sna-periph-rx-bc", 110),
          ("sna-periph-tx-bc", 109),
          ("sna-rx-bc", 106),
          ("sna-subarea-rx-bc", 108),
          ("sna-subarea-tx-bc", 107),
          ("sna-tx-bc", 105),
          ("snmp-udp-ip-rx-bc", 36),
          ("snmp-udp-ip-tx-bc", 35),
          ("snmptrap-udp-ip-rx-bc", 38),
          ("snmptrap-udp-ip-tx-bc", 37),
          ("spx-ipx-rx-bc", 80),
          ("spx-ipx-tx-bc", 79),
          ("src-quench-icmp-ip-rx-bc", 48),
          ("src-quench-icmp-ip-tx-bc", 47),
          ("tcp-ip-rx-bc", 4),
          ("tcp-ip-tx-bc", 3),
          ("telnet-tcp-ip-rx-bc", 8),
          ("telnet-tcp-ip-tx-bc", 7),
          ("tftp-udp-ip-rx-bc", 30),
          ("tftp-udp-ip-tx-bc", 29),
          ("thru-becn-rx-c", 134),
          ("thru-becn-tx-c", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-c", 136),
          ("thru-de-tx-c", 135),
          ("thru-fecn-rx-c", 132),
          ("thru-fecn-tx-c", 131),
          ("thru-frame-rx-c", 130),
          ("thru-frame-tx-c", 129),
          ("time-excd-icmp-ip-rx-bc", 54),
          ("time-excd-icmp-ip-tx-bc", 53),
          ("timestamp-rep-icmp-ip-rx-bc", 60),
          ("timestamp-rep-icmp-ip-tx-bc", 59),
          ("timestamp-req-icmp-ip-rx-bc", 58),
          ("timestamp-req-icmp-ip-tx-bc", 57),
          ("total-downtime", 166),
          ("total-uptime", 165),
          ("udp-ip-rx-bc", 22),
          ("udp-ip-tx-bc", 21),
          ("user-defined-1-rx-bc", 120),
          ("user-defined-1-tx-bc", 119),
          ("user-defined-2-rx-bc", 122),
          ("user-defined-2-tx-bc", 121),
          ("user-defined-3-rx-bc", 124),
          ("user-defined-3-tx-bc", 123),
          ("user-defined-4-rx-bc", 126),
          ("user-defined-4-tx-bc", 125),
          ("vnip-rx-bc", 170),
          ("vnip-tx-bc", 169))
    )


_SfrapCfgFrPerfLTProtocolFilterProtocol_Type.__name__ = "Integer32"
_SfrapCfgFrPerfLTProtocolFilterProtocol_Object = MibTableColumn
sfrapCfgFrPerfLTProtocolFilterProtocol = _SfrapCfgFrPerfLTProtocolFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 6, 1, 2),
    _SfrapCfgFrPerfLTProtocolFilterProtocol_Type()
)
sfrapCfgFrPerfLTProtocolFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTProtocolFilterProtocol.setStatus("mandatory")


class _SfrapCfgFrPerfDlciDefaultUtilThreshold_Type(Integer32):
    """Custom type sfrapCfgFrPerfDlciDefaultUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfrapCfgFrPerfDlciDefaultUtilThreshold_Type.__name__ = "Integer32"
_SfrapCfgFrPerfDlciDefaultUtilThreshold_Object = MibScalar
sfrapCfgFrPerfDlciDefaultUtilThreshold = _SfrapCfgFrPerfDlciDefaultUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 7),
    _SfrapCfgFrPerfDlciDefaultUtilThreshold_Type()
)
sfrapCfgFrPerfDlciDefaultUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciDefaultUtilThreshold.setStatus("mandatory")


class _SfrapCfgFrPerfDlciUtilDuration_Type(Integer32):
    """Custom type sfrapCfgFrPerfDlciUtilDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfrapCfgFrPerfDlciUtilDuration_Type.__name__ = "Integer32"
_SfrapCfgFrPerfDlciUtilDuration_Object = MibScalar
sfrapCfgFrPerfDlciUtilDuration = _SfrapCfgFrPerfDlciUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 8),
    _SfrapCfgFrPerfDlciUtilDuration_Type()
)
sfrapCfgFrPerfDlciUtilDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciUtilDuration.setStatus("mandatory")


class _SfrapCfgFrPerfDlciNamesTableClear_Type(Integer32):
    """Custom type sfrapCfgFrPerfDlciNamesTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-table", 1),
          ("clear-table-keep-stats", 2))
    )


_SfrapCfgFrPerfDlciNamesTableClear_Type.__name__ = "Integer32"
_SfrapCfgFrPerfDlciNamesTableClear_Object = MibScalar
sfrapCfgFrPerfDlciNamesTableClear = _SfrapCfgFrPerfDlciNamesTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 9),
    _SfrapCfgFrPerfDlciNamesTableClear_Type()
)
sfrapCfgFrPerfDlciNamesTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfDlciNamesTableClear.setStatus("mandatory")


class _SfrapCfgFrPerfUserProtocolsTableClear_Type(Integer32):
    """Custom type sfrapCfgFrPerfUserProtocolsTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_SfrapCfgFrPerfUserProtocolsTableClear_Type.__name__ = "Integer32"
_SfrapCfgFrPerfUserProtocolsTableClear_Object = MibScalar
sfrapCfgFrPerfUserProtocolsTableClear = _SfrapCfgFrPerfUserProtocolsTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 10),
    _SfrapCfgFrPerfUserProtocolsTableClear_Type()
)
sfrapCfgFrPerfUserProtocolsTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUserProtocolsTableClear.setStatus("mandatory")


class _SfrapCfgFrPerfLTDlciFilterTableClear_Type(Integer32):
    """Custom type sfrapCfgFrPerfLTDlciFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_SfrapCfgFrPerfLTDlciFilterTableClear_Type.__name__ = "Integer32"
_SfrapCfgFrPerfLTDlciFilterTableClear_Object = MibScalar
sfrapCfgFrPerfLTDlciFilterTableClear = _SfrapCfgFrPerfLTDlciFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 11),
    _SfrapCfgFrPerfLTDlciFilterTableClear_Type()
)
sfrapCfgFrPerfLTDlciFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTDlciFilterTableClear.setStatus("mandatory")


class _SfrapCfgFrPerfLTProtocolFilterTableClear_Type(Integer32):
    """Custom type sfrapCfgFrPerfLTProtocolFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_SfrapCfgFrPerfLTProtocolFilterTableClear_Type.__name__ = "Integer32"
_SfrapCfgFrPerfLTProtocolFilterTableClear_Object = MibScalar
sfrapCfgFrPerfLTProtocolFilterTableClear = _SfrapCfgFrPerfLTProtocolFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 12),
    _SfrapCfgFrPerfLTProtocolFilterTableClear_Type()
)
sfrapCfgFrPerfLTProtocolFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfLTProtocolFilterTableClear.setStatus("mandatory")


class _SfrapCfgFrPerfUnprovDlcisDelete_Type(Integer32):
    """Custom type sfrapCfgFrPerfUnprovDlcisDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete-unprov", 1)
    )


_SfrapCfgFrPerfUnprovDlcisDelete_Type.__name__ = "Integer32"
_SfrapCfgFrPerfUnprovDlcisDelete_Object = MibScalar
sfrapCfgFrPerfUnprovDlcisDelete = _SfrapCfgFrPerfUnprovDlcisDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 7, 13),
    _SfrapCfgFrPerfUnprovDlcisDelete_Type()
)
sfrapCfgFrPerfUnprovDlcisDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgFrPerfUnprovDlcisDelete.setStatus("mandatory")
_SfrapCfgSecurityTable_ObjectIdentity = ObjectIdentity
sfrapCfgSecurityTable = _SfrapCfgSecurityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8)
)


class _SfrapCfgTelnetCliPassword_Type(DisplayString):
    """Custom type sfrapCfgTelnetCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapCfgTelnetCliPassword_Type.__name__ = "DisplayString"
_SfrapCfgTelnetCliPassword_Object = MibScalar
sfrapCfgTelnetCliPassword = _SfrapCfgTelnetCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8, 1),
    _SfrapCfgTelnetCliPassword_Type()
)
sfrapCfgTelnetCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTelnetCliPassword.setStatus("mandatory")


class _SfrapCfgTftpPassword_Type(DisplayString):
    """Custom type sfrapCfgTftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapCfgTftpPassword_Type.__name__ = "DisplayString"
_SfrapCfgTftpPassword_Object = MibScalar
sfrapCfgTftpPassword = _SfrapCfgTftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8, 2),
    _SfrapCfgTftpPassword_Type()
)
sfrapCfgTftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgTftpPassword.setStatus("mandatory")


class _SfrapCfgCliPassword_Type(DisplayString):
    """Custom type sfrapCfgCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapCfgCliPassword_Type.__name__ = "DisplayString"
_SfrapCfgCliPassword_Object = MibScalar
sfrapCfgCliPassword = _SfrapCfgCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8, 3),
    _SfrapCfgCliPassword_Type()
)
sfrapCfgCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgCliPassword.setStatus("mandatory")


class _SfrapCfgGetCommunityString_Type(DisplayString):
    """Custom type sfrapCfgGetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SfrapCfgGetCommunityString_Type.__name__ = "DisplayString"
_SfrapCfgGetCommunityString_Object = MibScalar
sfrapCfgGetCommunityString = _SfrapCfgGetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8, 5),
    _SfrapCfgGetCommunityString_Type()
)
sfrapCfgGetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgGetCommunityString.setStatus("mandatory")


class _SfrapCfgSetCommunityString_Type(DisplayString):
    """Custom type sfrapCfgSetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SfrapCfgSetCommunityString_Type.__name__ = "DisplayString"
_SfrapCfgSetCommunityString_Object = MibScalar
sfrapCfgSetCommunityString = _SfrapCfgSetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 8, 6),
    _SfrapCfgSetCommunityString_Type()
)
sfrapCfgSetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgSetCommunityString.setStatus("mandatory")


class _SfrapCfgLock_Type(Integer32):
    """Custom type sfrapCfgLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfrapCfgLock_Type.__name__ = "Integer32"
_SfrapCfgLock_Object = MibScalar
sfrapCfgLock = _SfrapCfgLock_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 12),
    _SfrapCfgLock_Type()
)
sfrapCfgLock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgLock.setStatus("mandatory")
_SfrapCfgLockID_Type = IpAddress
_SfrapCfgLockID_Object = MibScalar
sfrapCfgLockID = _SfrapCfgLockID_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 13),
    _SfrapCfgLockID_Type()
)
sfrapCfgLockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgLockID.setStatus("mandatory")


class _SfrapCfgID_Type(DisplayString):
    """Custom type sfrapCfgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfrapCfgID_Type.__name__ = "DisplayString"
_SfrapCfgID_Object = MibScalar
sfrapCfgID = _SfrapCfgID_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 14),
    _SfrapCfgID_Type()
)
sfrapCfgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapCfgID.setStatus("mandatory")


class _SfrapCfgStatus_Type(Integer32):
    """Custom type sfrapCfgStatus based on Integer32"""
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
        *(("aborted-by-user", 7),
          ("bandwidth-allocation-error", 4),
          ("datarate-density-conflict", 3),
          ("general-error", 5),
          ("in-progress", 1),
          ("success", 2),
          ("timeout", 6))
    )


_SfrapCfgStatus_Type.__name__ = "Integer32"
_SfrapCfgStatus_Object = MibScalar
sfrapCfgStatus = _SfrapCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 15),
    _SfrapCfgStatus_Type()
)
sfrapCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgStatus.setStatus("mandatory")


class _SfrapCfgUnlock_Type(Integer32):
    """Custom type sfrapCfgUnlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("un-lock", 1)
    )


_SfrapCfgUnlock_Type.__name__ = "Integer32"
_SfrapCfgUnlock_Object = MibScalar
sfrapCfgUnlock = _SfrapCfgUnlock_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 16),
    _SfrapCfgUnlock_Type()
)
sfrapCfgUnlock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgUnlock.setStatus("mandatory")


class _SfrapCfgUpdate_Type(Integer32):
    """Custom type sfrapCfgUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_SfrapCfgUpdate_Type.__name__ = "Integer32"
_SfrapCfgUpdate_Object = MibScalar
sfrapCfgUpdate = _SfrapCfgUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 2, 17),
    _SfrapCfgUpdate_Type()
)
sfrapCfgUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapCfgUpdate.setStatus("mandatory")
_SfrapDiagnostics_ObjectIdentity = ObjectIdentity
sfrapDiagnostics = _SfrapDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 3)
)
_SfrapDiagUnitTable_ObjectIdentity = ObjectIdentity
sfrapDiagUnitTable = _SfrapDiagUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1)
)


class _SfrapDiagUnitLocLoop_Type(Integer32):
    """Custom type sfrapDiagUnitLocLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-loopback-mode", 2),
          ("enable-loopback-mode", 1))
    )


_SfrapDiagUnitLocLoop_Type.__name__ = "Integer32"
_SfrapDiagUnitLocLoop_Object = MibScalar
sfrapDiagUnitLocLoop = _SfrapDiagUnitLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1, 1),
    _SfrapDiagUnitLocLoop_Type()
)
sfrapDiagUnitLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagUnitLocLoop.setStatus("mandatory")


class _SfrapDiagUnitReset_Type(Integer32):
    """Custom type sfrapDiagUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-unit", 1)
    )


_SfrapDiagUnitReset_Type.__name__ = "Integer32"
_SfrapDiagUnitReset_Object = MibScalar
sfrapDiagUnitReset = _SfrapDiagUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1, 2),
    _SfrapDiagUnitReset_Type()
)
sfrapDiagUnitReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapDiagUnitReset.setStatus("mandatory")
_SfrapDiagUnitTimeRemaining_Type = TimeTicks
_SfrapDiagUnitTimeRemaining_Object = MibScalar
sfrapDiagUnitTimeRemaining = _SfrapDiagUnitTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1, 3),
    _SfrapDiagUnitTimeRemaining_Type()
)
sfrapDiagUnitTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagUnitTimeRemaining.setStatus("mandatory")


class _SfrapDiagUnitCutThru_Type(Integer32):
    """Custom type sfrapDiagUnitCutThru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-cutthru-mode", 2),
          ("enable-cutthru-mode", 1))
    )


_SfrapDiagUnitCutThru_Type.__name__ = "Integer32"
_SfrapDiagUnitCutThru_Object = MibScalar
sfrapDiagUnitCutThru = _SfrapDiagUnitCutThru_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1, 4),
    _SfrapDiagUnitCutThru_Type()
)
sfrapDiagUnitCutThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagUnitCutThru.setStatus("mandatory")
_SfrapDiagUnitCutThruTimeRemaining_Type = TimeTicks
_SfrapDiagUnitCutThruTimeRemaining_Object = MibScalar
sfrapDiagUnitCutThruTimeRemaining = _SfrapDiagUnitCutThruTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 1, 5),
    _SfrapDiagUnitCutThruTimeRemaining_Type()
)
sfrapDiagUnitCutThruTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagUnitCutThruTimeRemaining.setStatus("mandatory")
_SfrapDiagDteTable_Object = MibTable
sfrapDiagDteTable = _SfrapDiagDteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 3)
)
if mibBuilder.loadTexts:
    sfrapDiagDteTable.setStatus("mandatory")
_SfrapDiagDteEntry_Object = MibTableRow
sfrapDiagDteEntry = _SfrapDiagDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 3, 1)
)
sfrapDiagDteEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapDiagDteIndex"),
)
if mibBuilder.loadTexts:
    sfrapDiagDteEntry.setStatus("mandatory")


class _SfrapDiagDteLclLpbk_Type(Integer32):
    """Custom type sfrapDiagDteLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-loopback-mode", 2),
          ("enable-loopback-mode", 1))
    )


_SfrapDiagDteLclLpbk_Type.__name__ = "Integer32"
_SfrapDiagDteLclLpbk_Object = MibTableColumn
sfrapDiagDteLclLpbk = _SfrapDiagDteLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 3, 1, 3),
    _SfrapDiagDteLclLpbk_Type()
)
sfrapDiagDteLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagDteLclLpbk.setStatus("mandatory")
_SfrapDiagDteTimeRemaining_Type = TimeTicks
_SfrapDiagDteTimeRemaining_Object = MibTableColumn
sfrapDiagDteTimeRemaining = _SfrapDiagDteTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 3, 1, 13),
    _SfrapDiagDteTimeRemaining_Type()
)
sfrapDiagDteTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagDteTimeRemaining.setStatus("mandatory")


class _SfrapDiagDteIndex_Type(Integer32):
    """Custom type sfrapDiagDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce", 2),
          ("to-dte", 1))
    )


_SfrapDiagDteIndex_Type.__name__ = "Integer32"
_SfrapDiagDteIndex_Object = MibTableColumn
sfrapDiagDteIndex = _SfrapDiagDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 3, 1, 99),
    _SfrapDiagDteIndex_Type()
)
sfrapDiagDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagDteIndex.setStatus("mandatory")
_SfrapDiagVnipTable_Object = MibTable
sfrapDiagVnipTable = _SfrapDiagVnipTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6)
)
if mibBuilder.loadTexts:
    sfrapDiagVnipTable.setStatus("mandatory")
_SfrapDiagVnipEntry_Object = MibTableRow
sfrapDiagVnipEntry = _SfrapDiagVnipEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1)
)
sfrapDiagVnipEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapDiagVnipInterface"),
    (0, "SFRAP-MIB", "sfrapDiagVnipIndex"),
)
if mibBuilder.loadTexts:
    sfrapDiagVnipEntry.setStatus("mandatory")


class _SfrapDiagVnipInterface_Type(Integer32):
    """Custom type sfrapDiagVnipInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dte-interface", 1),
          ("t1-interface", 2))
    )


_SfrapDiagVnipInterface_Type.__name__ = "Integer32"
_SfrapDiagVnipInterface_Object = MibTableColumn
sfrapDiagVnipInterface = _SfrapDiagVnipInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 1),
    _SfrapDiagVnipInterface_Type()
)
sfrapDiagVnipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVnipInterface.setStatus("mandatory")
_SfrapDiagVnipIndex_Type = Integer32
_SfrapDiagVnipIndex_Object = MibTableColumn
sfrapDiagVnipIndex = _SfrapDiagVnipIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 2),
    _SfrapDiagVnipIndex_Type()
)
sfrapDiagVnipIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVnipIndex.setStatus("mandatory")
_SfrapDiagVnipDlci_Type = Integer32
_SfrapDiagVnipDlci_Object = MibTableColumn
sfrapDiagVnipDlci = _SfrapDiagVnipDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 3),
    _SfrapDiagVnipDlci_Type()
)
sfrapDiagVnipDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagVnipDlci.setStatus("mandatory")
_SfrapDiagVnipIpAddr_Type = IpAddress
_SfrapDiagVnipIpAddr_Object = MibTableColumn
sfrapDiagVnipIpAddr = _SfrapDiagVnipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 4),
    _SfrapDiagVnipIpAddr_Type()
)
sfrapDiagVnipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDiagVnipIpAddr.setStatus("mandatory")


class _SfrapDiagVLOOP_Type(Integer32):
    """Custom type sfrapDiagVLOOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-test", 1),
          ("stop-test", 2))
    )


_SfrapDiagVLOOP_Type.__name__ = "Integer32"
_SfrapDiagVLOOP_Object = MibTableColumn
sfrapDiagVLOOP = _SfrapDiagVLOOP_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 5),
    _SfrapDiagVLOOP_Type()
)
sfrapDiagVLOOP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapDiagVLOOP.setStatus("mandatory")


class _SfrapDiagVBERT_Type(Integer32):
    """Custom type sfrapDiagVBERT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_SfrapDiagVBERT_Type.__name__ = "Integer32"
_SfrapDiagVBERT_Object = MibTableColumn
sfrapDiagVBERT = _SfrapDiagVBERT_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 6),
    _SfrapDiagVBERT_Type()
)
sfrapDiagVBERT.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapDiagVBERT.setStatus("mandatory")


class _SfrapDiagVBERTRate_Type(Integer32):
    """Custom type sfrapDiagVBERTRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2048000),
    )


_SfrapDiagVBERTRate_Type.__name__ = "Integer32"
_SfrapDiagVBERTRate_Object = MibTableColumn
sfrapDiagVBERTRate = _SfrapDiagVBERTRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 7),
    _SfrapDiagVBERTRate_Type()
)
sfrapDiagVBERTRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVBERTRate.setStatus("mandatory")


class _SfrapDiagVBERTSize_Type(Integer32):
    """Custom type sfrapDiagVBERTSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("pkt-size-1024", 1024),
          ("pkt-size-128", 128),
          ("pkt-size-2048", 2048),
          ("pkt-size-256", 256),
          ("pkt-size-512", 512),
          ("pkt-size-64", 64))
    )


_SfrapDiagVBERTSize_Type.__name__ = "Integer32"
_SfrapDiagVBERTSize_Object = MibTableColumn
sfrapDiagVBERTSize = _SfrapDiagVBERTSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 8),
    _SfrapDiagVBERTSize_Type()
)
sfrapDiagVBERTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVBERTSize.setStatus("mandatory")


class _SfrapDiagVBERTPktPercent_Type(Integer32):
    """Custom type sfrapDiagVBERTPktPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fifty-percent", 50),
          ("oneHundred-percent", 100),
          ("seventyFive-percent", 75),
          ("twentyFive-percent", 25),
          ("zero-percent", 0))
    )


_SfrapDiagVBERTPktPercent_Type.__name__ = "Integer32"
_SfrapDiagVBERTPktPercent_Object = MibTableColumn
sfrapDiagVBERTPktPercent = _SfrapDiagVBERTPktPercent_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 9),
    _SfrapDiagVBERTPktPercent_Type()
)
sfrapDiagVBERTPktPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVBERTPktPercent.setStatus("mandatory")


class _SfrapDiagVBERTTestPeriod_Type(Integer32):
    """Custom type sfrapDiagVBERTTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_SfrapDiagVBERTTestPeriod_Type.__name__ = "Integer32"
_SfrapDiagVBERTTestPeriod_Object = MibTableColumn
sfrapDiagVBERTTestPeriod = _SfrapDiagVBERTTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 6, 1, 10),
    _SfrapDiagVBERTTestPeriod_Type()
)
sfrapDiagVBERTTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagVBERTTestPeriod.setStatus("mandatory")


class _SfrapDiagTxClockDetect_Type(Integer32):
    """Custom type sfrapDiagTxClockDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate-clock-detect", 1),
          ("terminate-clock-detect", 2))
    )


_SfrapDiagTxClockDetect_Type.__name__ = "Integer32"
_SfrapDiagTxClockDetect_Object = MibScalar
sfrapDiagTxClockDetect = _SfrapDiagTxClockDetect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 3, 7),
    _SfrapDiagTxClockDetect_Type()
)
sfrapDiagTxClockDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfrapDiagTxClockDetect.setStatus("mandatory")
_SfrapStatus_ObjectIdentity = ObjectIdentity
sfrapStatus = _SfrapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 4)
)
_SfrapVnipTopologyTable_Object = MibTable
sfrapVnipTopologyTable = _SfrapVnipTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2)
)
if mibBuilder.loadTexts:
    sfrapVnipTopologyTable.setStatus("mandatory")
_SfrapVnipTopologyEntry_Object = MibTableRow
sfrapVnipTopologyEntry = _SfrapVnipTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1)
)
sfrapVnipTopologyEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapVnipTopologyInterface"),
    (0, "SFRAP-MIB", "sfrapVnipTopologyIndex"),
)
if mibBuilder.loadTexts:
    sfrapVnipTopologyEntry.setStatus("mandatory")


class _SfrapVnipTopologyInterface_Type(Integer32):
    """Custom type sfrapVnipTopologyInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data1-interface", 1),
          ("data2-interface", 2))
    )


_SfrapVnipTopologyInterface_Type.__name__ = "Integer32"
_SfrapVnipTopologyInterface_Object = MibTableColumn
sfrapVnipTopologyInterface = _SfrapVnipTopologyInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 1),
    _SfrapVnipTopologyInterface_Type()
)
sfrapVnipTopologyInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyInterface.setStatus("mandatory")
_SfrapVnipTopologyIndex_Type = Integer32
_SfrapVnipTopologyIndex_Object = MibTableColumn
sfrapVnipTopologyIndex = _SfrapVnipTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 2),
    _SfrapVnipTopologyIndex_Type()
)
sfrapVnipTopologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyIndex.setStatus("mandatory")
_SfrapVnipTopologyDlci_Type = Integer32
_SfrapVnipTopologyDlci_Object = MibTableColumn
sfrapVnipTopologyDlci = _SfrapVnipTopologyDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 3),
    _SfrapVnipTopologyDlci_Type()
)
sfrapVnipTopologyDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyDlci.setStatus("mandatory")
_SfrapVnipTopologyIpAddr_Type = IpAddress
_SfrapVnipTopologyIpAddr_Object = MibTableColumn
sfrapVnipTopologyIpAddr = _SfrapVnipTopologyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 4),
    _SfrapVnipTopologyIpAddr_Type()
)
sfrapVnipTopologyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyIpAddr.setStatus("mandatory")
_SfrapVnipTopologyNumHops_Type = Integer32
_SfrapVnipTopologyNumHops_Object = MibTableColumn
sfrapVnipTopologyNumHops = _SfrapVnipTopologyNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 5),
    _SfrapVnipTopologyNumHops_Type()
)
sfrapVnipTopologyNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyNumHops.setStatus("mandatory")
_SfrapVnipTopologyLocalDlci_Type = Integer32
_SfrapVnipTopologyLocalDlci_Object = MibTableColumn
sfrapVnipTopologyLocalDlci = _SfrapVnipTopologyLocalDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 6),
    _SfrapVnipTopologyLocalDlci_Type()
)
sfrapVnipTopologyLocalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopologyLocalDlci.setStatus("mandatory")
_SfrapVnipTopoTDNumSamples_Type = Counter32
_SfrapVnipTopoTDNumSamples_Object = MibTableColumn
sfrapVnipTopoTDNumSamples = _SfrapVnipTopoTDNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 10),
    _SfrapVnipTopoTDNumSamples_Type()
)
sfrapVnipTopoTDNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoTDNumSamples.setStatus("mandatory")
_SfrapVnipTopoTDAvgDelay_Type = Counter32
_SfrapVnipTopoTDAvgDelay_Object = MibTableColumn
sfrapVnipTopoTDAvgDelay = _SfrapVnipTopoTDAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 11),
    _SfrapVnipTopoTDAvgDelay_Type()
)
sfrapVnipTopoTDAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoTDAvgDelay.setStatus("mandatory")
_SfrapVnipTopoTDMaxDelay_Type = Counter32
_SfrapVnipTopoTDMaxDelay_Object = MibTableColumn
sfrapVnipTopoTDMaxDelay = _SfrapVnipTopoTDMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 12),
    _SfrapVnipTopoTDMaxDelay_Type()
)
sfrapVnipTopoTDMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoTDMaxDelay.setStatus("mandatory")
_SfrapVnipTopoTDMinDelay_Type = Counter32
_SfrapVnipTopoTDMinDelay_Object = MibTableColumn
sfrapVnipTopoTDMinDelay = _SfrapVnipTopoTDMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 13),
    _SfrapVnipTopoTDMinDelay_Type()
)
sfrapVnipTopoTDMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoTDMinDelay.setStatus("mandatory")
_SfrapVnipTopoTDLastDelay_Type = Counter32
_SfrapVnipTopoTDLastDelay_Object = MibTableColumn
sfrapVnipTopoTDLastDelay = _SfrapVnipTopoTDLastDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 14),
    _SfrapVnipTopoTDLastDelay_Type()
)
sfrapVnipTopoTDLastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoTDLastDelay.setStatus("mandatory")


class _SfrapVnipTopoVLOOPStatus_Type(Integer32):
    """Custom type sfrapVnipTopoVLOOPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback-disable", 2),
          ("loopback-enable", 1))
    )


_SfrapVnipTopoVLOOPStatus_Type.__name__ = "Integer32"
_SfrapVnipTopoVLOOPStatus_Object = MibTableColumn
sfrapVnipTopoVLOOPStatus = _SfrapVnipTopoVLOOPStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 15),
    _SfrapVnipTopoVLOOPStatus_Type()
)
sfrapVnipTopoVLOOPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVLOOPStatus.setStatus("mandatory")


class _SfrapVnipTopoVBERTStatus_Type(Integer32):
    """Custom type sfrapVnipTopoVBERTStatus based on Integer32"""
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
        *(("in-test", 5),
          ("off", 1),
          ("test-completed", 4),
          ("test-failed", 3),
          ("testing", 2))
    )


_SfrapVnipTopoVBERTStatus_Type.__name__ = "Integer32"
_SfrapVnipTopoVBERTStatus_Object = MibTableColumn
sfrapVnipTopoVBERTStatus = _SfrapVnipTopoVBERTStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 16),
    _SfrapVnipTopoVBERTStatus_Type()
)
sfrapVnipTopoVBERTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBERTStatus.setStatus("mandatory")
_SfrapVnipTopoVBertTxDESetFrames_Type = Counter32
_SfrapVnipTopoVBertTxDESetFrames_Object = MibTableColumn
sfrapVnipTopoVBertTxDESetFrames = _SfrapVnipTopoVBertTxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 17),
    _SfrapVnipTopoVBertTxDESetFrames_Type()
)
sfrapVnipTopoVBertTxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertTxDESetFrames.setStatus("mandatory")
_SfrapVnipTopoVBertRxDESetFrames_Type = Counter32
_SfrapVnipTopoVBertRxDESetFrames_Object = MibTableColumn
sfrapVnipTopoVBertRxDESetFrames = _SfrapVnipTopoVBertRxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 18),
    _SfrapVnipTopoVBertRxDESetFrames_Type()
)
sfrapVnipTopoVBertRxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertRxDESetFrames.setStatus("mandatory")
_SfrapVnipTopoVBertTxDEClrFrames_Type = Counter32
_SfrapVnipTopoVBertTxDEClrFrames_Object = MibTableColumn
sfrapVnipTopoVBertTxDEClrFrames = _SfrapVnipTopoVBertTxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 19),
    _SfrapVnipTopoVBertTxDEClrFrames_Type()
)
sfrapVnipTopoVBertTxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertTxDEClrFrames.setStatus("mandatory")
_SfrapVnipTopoVBertRxDEClrFrames_Type = Counter32
_SfrapVnipTopoVBertRxDEClrFrames_Object = MibTableColumn
sfrapVnipTopoVBertRxDEClrFrames = _SfrapVnipTopoVBertRxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 20),
    _SfrapVnipTopoVBertRxDEClrFrames_Type()
)
sfrapVnipTopoVBertRxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertRxDEClrFrames.setStatus("mandatory")
_SfrapVnipTopoVBertTransitDelayMax_Type = Counter32
_SfrapVnipTopoVBertTransitDelayMax_Object = MibTableColumn
sfrapVnipTopoVBertTransitDelayMax = _SfrapVnipTopoVBertTransitDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 21),
    _SfrapVnipTopoVBertTransitDelayMax_Type()
)
sfrapVnipTopoVBertTransitDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertTransitDelayMax.setStatus("mandatory")
_SfrapVnipTopoVBertTransitDelayAvg_Type = Counter32
_SfrapVnipTopoVBertTransitDelayAvg_Object = MibTableColumn
sfrapVnipTopoVBertTransitDelayAvg = _SfrapVnipTopoVBertTransitDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 22),
    _SfrapVnipTopoVBertTransitDelayAvg_Type()
)
sfrapVnipTopoVBertTransitDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertTransitDelayAvg.setStatus("mandatory")
_SfrapVnipTopoVBertTimeElapse_Type = TimeTicks
_SfrapVnipTopoVBertTimeElapse_Object = MibTableColumn
sfrapVnipTopoVBertTimeElapse = _SfrapVnipTopoVBertTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 23),
    _SfrapVnipTopoVBertTimeElapse_Type()
)
sfrapVnipTopoVBertTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertTimeElapse.setStatus("mandatory")
_SfrapVnipTopoVBertPerUtilCIR_Type = Integer32
_SfrapVnipTopoVBertPerUtilCIR_Object = MibTableColumn
sfrapVnipTopoVBertPerUtilCIR = _SfrapVnipTopoVBertPerUtilCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 24),
    _SfrapVnipTopoVBertPerUtilCIR_Type()
)
sfrapVnipTopoVBertPerUtilCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertPerUtilCIR.setStatus("mandatory")
_SfrapVnipTopoVBertPerUtilEIR_Type = Integer32
_SfrapVnipTopoVBertPerUtilEIR_Object = MibTableColumn
sfrapVnipTopoVBertPerUtilEIR = _SfrapVnipTopoVBertPerUtilEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 2, 1, 25),
    _SfrapVnipTopoVBertPerUtilEIR_Type()
)
sfrapVnipTopoVBertPerUtilEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapVnipTopoVBertPerUtilEIR.setStatus("mandatory")
_SfrapStatusMgmtTable_ObjectIdentity = ObjectIdentity
sfrapStatusMgmtTable = _SfrapStatusMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3)
)


class _SfrapStatusMgmtChannel_Type(Integer32):
    """Custom type sfrapStatusMgmtChannel based on Integer32"""
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
        *(("none", 1),
          ("piggyback-dlci", 4),
          ("private-dlci", 3),
          ("slip", 2))
    )


_SfrapStatusMgmtChannel_Type.__name__ = "Integer32"
_SfrapStatusMgmtChannel_Object = MibScalar
sfrapStatusMgmtChannel = _SfrapStatusMgmtChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3, 1),
    _SfrapStatusMgmtChannel_Type()
)
sfrapStatusMgmtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusMgmtChannel.setStatus("mandatory")


class _SfrapStatusMgmtInterface_Type(Integer32):
    """Custom type sfrapStatusMgmtInterface based on Integer32"""
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
        *(("comm", 1),
          ("local-and-remote", 4),
          ("local-to-dte", 2),
          ("remote-to-dce", 3))
    )


_SfrapStatusMgmtInterface_Type.__name__ = "Integer32"
_SfrapStatusMgmtInterface_Object = MibScalar
sfrapStatusMgmtInterface = _SfrapStatusMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3, 2),
    _SfrapStatusMgmtInterface_Type()
)
sfrapStatusMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusMgmtInterface.setStatus("mandatory")


class _SfrapStatusMgmtInterfaceStatus_Type(Integer32):
    """Custom type sfrapStatusMgmtInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("alarm", 3),
          ("inactive", 2))
    )


_SfrapStatusMgmtInterfaceStatus_Type.__name__ = "Integer32"
_SfrapStatusMgmtInterfaceStatus_Object = MibScalar
sfrapStatusMgmtInterfaceStatus = _SfrapStatusMgmtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3, 3),
    _SfrapStatusMgmtInterfaceStatus_Type()
)
sfrapStatusMgmtInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusMgmtInterfaceStatus.setStatus("mandatory")
_SfrapStatusMgmtDefaultDLCINo_Type = Integer32
_SfrapStatusMgmtDefaultDLCINo_Object = MibScalar
sfrapStatusMgmtDefaultDLCINo = _SfrapStatusMgmtDefaultDLCINo_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3, 4),
    _SfrapStatusMgmtDefaultDLCINo_Type()
)
sfrapStatusMgmtDefaultDLCINo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusMgmtDefaultDLCINo.setStatus("mandatory")


class _SfrapStatusMgmtDefaultDLCIStatus_Type(Integer32):
    """Custom type sfrapStatusMgmtDefaultDLCIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dlci-active", 2),
          ("dlci-inactive", 3),
          ("na", 1))
    )


_SfrapStatusMgmtDefaultDLCIStatus_Type.__name__ = "Integer32"
_SfrapStatusMgmtDefaultDLCIStatus_Object = MibScalar
sfrapStatusMgmtDefaultDLCIStatus = _SfrapStatusMgmtDefaultDLCIStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 3, 5),
    _SfrapStatusMgmtDefaultDLCIStatus_Type()
)
sfrapStatusMgmtDefaultDLCIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusMgmtDefaultDLCIStatus.setStatus("mandatory")
_SfrapStatusLedTable_ObjectIdentity = ObjectIdentity
sfrapStatusLedTable = _SfrapStatusLedTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4)
)


class _SfrapStatusLedOpStatusLED_Type(Integer32):
    """Custom type sfrapStatusLedOpStatusLED based on Integer32"""
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
        *(("blinkgreenLED-low-speed-mode", 2),
          ("blinkredLED-cut-through-mode", 5),
          ("greenLED-high-speed-mode", 1),
          ("redLED-alarm-mode", 4),
          ("yellowLED-test-mode", 3))
    )


_SfrapStatusLedOpStatusLED_Type.__name__ = "Integer32"
_SfrapStatusLedOpStatusLED_Object = MibScalar
sfrapStatusLedOpStatusLED = _SfrapStatusLedOpStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 1),
    _SfrapStatusLedOpStatusLED_Type()
)
sfrapStatusLedOpStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedOpStatusLED.setStatus("mandatory")


class _SfrapStatusLedToDTETxLED_Type(Integer32):
    """Custom type sfrapStatusLedToDTETxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-tx-data-receiving", 2),
          ("offLED-inactive", 1))
    )


_SfrapStatusLedToDTETxLED_Type.__name__ = "Integer32"
_SfrapStatusLedToDTETxLED_Object = MibScalar
sfrapStatusLedToDTETxLED = _SfrapStatusLedToDTETxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 2),
    _SfrapStatusLedToDTETxLED_Type()
)
sfrapStatusLedToDTETxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedToDTETxLED.setStatus("mandatory")


class _SfrapStatusLedToDTERxLED_Type(Integer32):
    """Custom type sfrapStatusLedToDTERxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-rx-data-receiving", 2),
          ("offLED-inactive", 1))
    )


_SfrapStatusLedToDTERxLED_Type.__name__ = "Integer32"
_SfrapStatusLedToDTERxLED_Object = MibScalar
sfrapStatusLedToDTERxLED = _SfrapStatusLedToDTERxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 3),
    _SfrapStatusLedToDTERxLED_Type()
)
sfrapStatusLedToDTERxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedToDTERxLED.setStatus("mandatory")


class _SfrapStatusLedRtsLED_Type(Integer32):
    """Custom type sfrapStatusLedRtsLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-rts-active", 1),
          ("offLED-rts-inactive", 2))
    )


_SfrapStatusLedRtsLED_Type.__name__ = "Integer32"
_SfrapStatusLedRtsLED_Object = MibScalar
sfrapStatusLedRtsLED = _SfrapStatusLedRtsLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 4),
    _SfrapStatusLedRtsLED_Type()
)
sfrapStatusLedRtsLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedRtsLED.setStatus("mandatory")


class _SfrapStatusLedCtsLED_Type(Integer32):
    """Custom type sfrapStatusLedCtsLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-cts-active", 1),
          ("offLED-cts-inactive", 2))
    )


_SfrapStatusLedCtsLED_Type.__name__ = "Integer32"
_SfrapStatusLedCtsLED_Object = MibScalar
sfrapStatusLedCtsLED = _SfrapStatusLedCtsLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 5),
    _SfrapStatusLedCtsLED_Type()
)
sfrapStatusLedCtsLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedCtsLED.setStatus("mandatory")


class _SfrapStatusLedDsrLED_Type(Integer32):
    """Custom type sfrapStatusLedDsrLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-dsr-active", 1),
          ("offLED-dsr-inactive", 2))
    )


_SfrapStatusLedDsrLED_Type.__name__ = "Integer32"
_SfrapStatusLedDsrLED_Object = MibScalar
sfrapStatusLedDsrLED = _SfrapStatusLedDsrLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 7),
    _SfrapStatusLedDsrLED_Type()
)
sfrapStatusLedDsrLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedDsrLED.setStatus("mandatory")


class _SfrapStatusLedDcdLED_Type(Integer32):
    """Custom type sfrapStatusLedDcdLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-dcd-active", 1),
          ("offLED-dcd-inactive", 2))
    )


_SfrapStatusLedDcdLED_Type.__name__ = "Integer32"
_SfrapStatusLedDcdLED_Object = MibScalar
sfrapStatusLedDcdLED = _SfrapStatusLedDcdLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 8),
    _SfrapStatusLedDcdLED_Type()
)
sfrapStatusLedDcdLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedDcdLED.setStatus("mandatory")


class _SfrapStatusLedToDCETxLED_Type(Integer32):
    """Custom type sfrapStatusLedToDCETxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-tx-data-receiving", 2),
          ("offLED-inactive", 1))
    )


_SfrapStatusLedToDCETxLED_Type.__name__ = "Integer32"
_SfrapStatusLedToDCETxLED_Object = MibScalar
sfrapStatusLedToDCETxLED = _SfrapStatusLedToDCETxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 9),
    _SfrapStatusLedToDCETxLED_Type()
)
sfrapStatusLedToDCETxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedToDCETxLED.setStatus("mandatory")


class _SfrapStatusLedToDCERxLED_Type(Integer32):
    """Custom type sfrapStatusLedToDCERxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-rx-data-receiving", 2),
          ("offLED-inactive", 1))
    )


_SfrapStatusLedToDCERxLED_Type.__name__ = "Integer32"
_SfrapStatusLedToDCERxLED_Object = MibScalar
sfrapStatusLedToDCERxLED = _SfrapStatusLedToDCERxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 10),
    _SfrapStatusLedToDCERxLED_Type()
)
sfrapStatusLedToDCERxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedToDCERxLED.setStatus("mandatory")


class _SfrapStatusAllLEDs_Type(DisplayString):
    """Custom type sfrapStatusAllLEDs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SfrapStatusAllLEDs_Type.__name__ = "DisplayString"
_SfrapStatusAllLEDs_Object = MibScalar
sfrapStatusAllLEDs = _SfrapStatusAllLEDs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 14),
    _SfrapStatusAllLEDs_Type()
)
sfrapStatusAllLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusAllLEDs.setStatus("mandatory")


class _SfrapStatusLedLmiErrLED_Type(Integer32):
    """Custom type sfrapStatusLedLmiErrLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blinkyellowLED-lmi-source-state", 3),
          ("offLED-lmi-active-state", 1),
          ("yellowLED-lmi-error-state", 2))
    )


_SfrapStatusLedLmiErrLED_Type.__name__ = "Integer32"
_SfrapStatusLedLmiErrLED_Object = MibScalar
sfrapStatusLedLmiErrLED = _SfrapStatusLedLmiErrLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 15),
    _SfrapStatusLedLmiErrLED_Type()
)
sfrapStatusLedLmiErrLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedLmiErrLED.setStatus("mandatory")


class _SfrapStatusLedFrmActLED_Type(Integer32):
    """Custom type sfrapStatusLedFrmActLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-frm-active", 1),
          ("offLED-frm-inactive", 2))
    )


_SfrapStatusLedFrmActLED_Type.__name__ = "Integer32"
_SfrapStatusLedFrmActLED_Object = MibScalar
sfrapStatusLedFrmActLED = _SfrapStatusLedFrmActLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 16),
    _SfrapStatusLedFrmActLED_Type()
)
sfrapStatusLedFrmActLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedFrmActLED.setStatus("mandatory")


class _SfrapStatusLedCtrlLED_Type(Integer32):
    """Custom type sfrapStatusLedCtrlLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLED-ctrl-inactive", 2),
          ("yellowLED-ctrl-active", 1))
    )


_SfrapStatusLedCtrlLED_Type.__name__ = "Integer32"
_SfrapStatusLedCtrlLED_Object = MibScalar
sfrapStatusLedCtrlLED = _SfrapStatusLedCtrlLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 17),
    _SfrapStatusLedCtrlLED_Type()
)
sfrapStatusLedCtrlLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedCtrlLED.setStatus("mandatory")


class _SfrapStatusLedIndLED_Type(Integer32):
    """Custom type sfrapStatusLedIndLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offLED-ind-inactive", 2),
          ("yellowLED-ind-active", 1))
    )


_SfrapStatusLedIndLED_Type.__name__ = "Integer32"
_SfrapStatusLedIndLED_Object = MibScalar
sfrapStatusLedIndLED = _SfrapStatusLedIndLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 4, 18),
    _SfrapStatusLedIndLED_Type()
)
sfrapStatusLedIndLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLedIndLED.setStatus("mandatory")


class _SfrapVnipTransitDelayClear_Type(Integer32):
    """Custom type sfrapVnipTransitDelayClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-transit-delay", 1)
    )


_SfrapVnipTransitDelayClear_Type.__name__ = "Integer32"
_SfrapVnipTransitDelayClear_Object = MibScalar
sfrapVnipTransitDelayClear = _SfrapVnipTransitDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 5),
    _SfrapVnipTransitDelayClear_Type()
)
sfrapVnipTransitDelayClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapVnipTransitDelayClear.setStatus("mandatory")


class _SfrapLmiSourcing_Type(Integer32):
    """Custom type sfrapLmiSourcing based on Integer32"""
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
        *(("both-ports", 8),
          ("disabled", 7),
          ("initializing", 1),
          ("ntwk-to-dce", 6),
          ("ntwk-to-dte", 5),
          ("passthrough", 2),
          ("user-to-dce", 4),
          ("user-to-dte", 3))
    )


_SfrapLmiSourcing_Type.__name__ = "Integer32"
_SfrapLmiSourcing_Object = MibScalar
sfrapLmiSourcing = _SfrapLmiSourcing_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 6),
    _SfrapLmiSourcing_Type()
)
sfrapLmiSourcing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapLmiSourcing.setStatus("mandatory")
_SfrapStatusDteTable_Object = MibTable
sfrapStatusDteTable = _SfrapStatusDteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7)
)
if mibBuilder.loadTexts:
    sfrapStatusDteTable.setStatus("mandatory")
_SfrapStatusDteEntry_Object = MibTableRow
sfrapStatusDteEntry = _SfrapStatusDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1)
)
sfrapStatusDteEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapStatusDteIndex"),
)
if mibBuilder.loadTexts:
    sfrapStatusDteEntry.setStatus("mandatory")


class _SfrapStatusDteMode_Type(Integer32):
    """Custom type sfrapStatusDteMode based on Integer32"""
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
          ("no-connections", 1),
          ("test", 3))
    )


_SfrapStatusDteMode_Type.__name__ = "Integer32"
_SfrapStatusDteMode_Object = MibTableColumn
sfrapStatusDteMode = _SfrapStatusDteMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 1),
    _SfrapStatusDteMode_Type()
)
sfrapStatusDteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteMode.setStatus("mandatory")


class _SfrapStatusDteRts_Type(Integer32):
    """Custom type sfrapStatusDteRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteRts_Type.__name__ = "Integer32"
_SfrapStatusDteRts_Object = MibTableColumn
sfrapStatusDteRts = _SfrapStatusDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 2),
    _SfrapStatusDteRts_Type()
)
sfrapStatusDteRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteRts.setStatus("mandatory")


class _SfrapStatusDteDtr_Type(Integer32):
    """Custom type sfrapStatusDteDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteDtr_Type.__name__ = "Integer32"
_SfrapStatusDteDtr_Object = MibTableColumn
sfrapStatusDteDtr = _SfrapStatusDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 3),
    _SfrapStatusDteDtr_Type()
)
sfrapStatusDteDtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteDtr.setStatus("mandatory")


class _SfrapStatusDteDcd_Type(Integer32):
    """Custom type sfrapStatusDteDcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteDcd_Type.__name__ = "Integer32"
_SfrapStatusDteDcd_Object = MibTableColumn
sfrapStatusDteDcd = _SfrapStatusDteDcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 4),
    _SfrapStatusDteDcd_Type()
)
sfrapStatusDteDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteDcd.setStatus("mandatory")


class _SfrapStatusDteDsr_Type(Integer32):
    """Custom type sfrapStatusDteDsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteDsr_Type.__name__ = "Integer32"
_SfrapStatusDteDsr_Object = MibTableColumn
sfrapStatusDteDsr = _SfrapStatusDteDsr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 5),
    _SfrapStatusDteDsr_Type()
)
sfrapStatusDteDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteDsr.setStatus("mandatory")


class _SfrapStatusDteCts_Type(Integer32):
    """Custom type sfrapStatusDteCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteCts_Type.__name__ = "Integer32"
_SfrapStatusDteCts_Object = MibTableColumn
sfrapStatusDteCts = _SfrapStatusDteCts_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 6),
    _SfrapStatusDteCts_Type()
)
sfrapStatusDteCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteCts.setStatus("mandatory")


class _SfrapStatusDteSendtiming_Type(Integer32):
    """Custom type sfrapStatusDteSendtiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("not-present", 2),
          ("present", 1))
    )


_SfrapStatusDteSendtiming_Type.__name__ = "Integer32"
_SfrapStatusDteSendtiming_Object = MibTableColumn
sfrapStatusDteSendtiming = _SfrapStatusDteSendtiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 7),
    _SfrapStatusDteSendtiming_Type()
)
sfrapStatusDteSendtiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteSendtiming.setStatus("mandatory")


class _SfrapStatusDteRxtiming_Type(Integer32):
    """Custom type sfrapStatusDteRxtiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("not-present", 2),
          ("present", 1))
    )


_SfrapStatusDteRxtiming_Type.__name__ = "Integer32"
_SfrapStatusDteRxtiming_Object = MibTableColumn
sfrapStatusDteRxtiming = _SfrapStatusDteRxtiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 8),
    _SfrapStatusDteRxtiming_Type()
)
sfrapStatusDteRxtiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteRxtiming.setStatus("mandatory")


class _SfrapStatusDteTermtiming_Type(Integer32):
    """Custom type sfrapStatusDteTermtiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("not-present", 2),
          ("present", 1))
    )


_SfrapStatusDteTermtiming_Type.__name__ = "Integer32"
_SfrapStatusDteTermtiming_Object = MibTableColumn
sfrapStatusDteTermtiming = _SfrapStatusDteTermtiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 9),
    _SfrapStatusDteTermtiming_Type()
)
sfrapStatusDteTermtiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteTermtiming.setStatus("mandatory")


class _SfrapStatusDteCtrl_Type(Integer32):
    """Custom type sfrapStatusDteCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteCtrl_Type.__name__ = "Integer32"
_SfrapStatusDteCtrl_Object = MibTableColumn
sfrapStatusDteCtrl = _SfrapStatusDteCtrl_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 10),
    _SfrapStatusDteCtrl_Type()
)
sfrapStatusDteCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteCtrl.setStatus("mandatory")


class _SfrapStatusDteInd_Type(Integer32):
    """Custom type sfrapStatusDteInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_SfrapStatusDteInd_Type.__name__ = "Integer32"
_SfrapStatusDteInd_Object = MibTableColumn
sfrapStatusDteInd = _SfrapStatusDteInd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 11),
    _SfrapStatusDteInd_Type()
)
sfrapStatusDteInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteInd.setStatus("mandatory")


class _SfrapStatusDteIndex_Type(Integer32):
    """Custom type sfrapStatusDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce", 2),
          ("to-dte", 1))
    )


_SfrapStatusDteIndex_Type.__name__ = "Integer32"
_SfrapStatusDteIndex_Object = MibTableColumn
sfrapStatusDteIndex = _SfrapStatusDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 7, 1, 99),
    _SfrapStatusDteIndex_Type()
)
sfrapStatusDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDteIndex.setStatus("mandatory")


class _SfrapStatusClockRate_Type(Integer32):
    """Custom type sfrapStatusClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_SfrapStatusClockRate_Type.__name__ = "Integer32"
_SfrapStatusClockRate_Object = MibScalar
sfrapStatusClockRate = _SfrapStatusClockRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 8),
    _SfrapStatusClockRate_Type()
)
sfrapStatusClockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusClockRate.setStatus("mandatory")


class _SfrapStatusToDteRxClockMode_Type(Integer32):
    """Custom type sfrapStatusToDteRxClockMode based on Integer32"""
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
        *(("clock-auto-invert", 4),
          ("clock-auto-normal", 3),
          ("clock-invert", 2),
          ("clock-normal", 1))
    )


_SfrapStatusToDteRxClockMode_Type.__name__ = "Integer32"
_SfrapStatusToDteRxClockMode_Object = MibScalar
sfrapStatusToDteRxClockMode = _SfrapStatusToDteRxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 9),
    _SfrapStatusToDteRxClockMode_Type()
)
sfrapStatusToDteRxClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusToDteRxClockMode.setStatus("mandatory")
_SfrapStatusDipswitchTable_ObjectIdentity = ObjectIdentity
sfrapStatusDipswitchTable = _SfrapStatusDipswitchTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10)
)


class _SfrapStatusDipswitchCutthru_Type(Integer32):
    """Custom type sfrapStatusDipswitchCutthru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchCutthru_Type.__name__ = "Integer32"
_SfrapStatusDipswitchCutthru_Object = MibScalar
sfrapStatusDipswitchCutthru = _SfrapStatusDipswitchCutthru_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 1),
    _SfrapStatusDipswitchCutthru_Type()
)
sfrapStatusDipswitchCutthru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchCutthru.setStatus("mandatory")


class _SfrapStatusDipswitchToDteLpbk_Type(Integer32):
    """Custom type sfrapStatusDipswitchToDteLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchToDteLpbk_Type.__name__ = "Integer32"
_SfrapStatusDipswitchToDteLpbk_Object = MibScalar
sfrapStatusDipswitchToDteLpbk = _SfrapStatusDipswitchToDteLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 2),
    _SfrapStatusDipswitchToDteLpbk_Type()
)
sfrapStatusDipswitchToDteLpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchToDteLpbk.setStatus("mandatory")


class _SfrapStatusDipswitchToDceLpbk_Type(Integer32):
    """Custom type sfrapStatusDipswitchToDceLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchToDceLpbk_Type.__name__ = "Integer32"
_SfrapStatusDipswitchToDceLpbk_Object = MibScalar
sfrapStatusDipswitchToDceLpbk = _SfrapStatusDipswitchToDceLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 3),
    _SfrapStatusDipswitchToDceLpbk_Type()
)
sfrapStatusDipswitchToDceLpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchToDceLpbk.setStatus("mandatory")


class _SfrapStatusDipswitchUnused_Type(Integer32):
    """Custom type sfrapStatusDipswitchUnused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchUnused_Type.__name__ = "Integer32"
_SfrapStatusDipswitchUnused_Object = MibScalar
sfrapStatusDipswitchUnused = _SfrapStatusDipswitchUnused_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 4),
    _SfrapStatusDipswitchUnused_Type()
)
sfrapStatusDipswitchUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchUnused.setStatus("mandatory")


class _SfrapStatusDipswitchIntfMode1_Type(Integer32):
    """Custom type sfrapStatusDipswitchIntfMode1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchIntfMode1_Type.__name__ = "Integer32"
_SfrapStatusDipswitchIntfMode1_Object = MibScalar
sfrapStatusDipswitchIntfMode1 = _SfrapStatusDipswitchIntfMode1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 5),
    _SfrapStatusDipswitchIntfMode1_Type()
)
sfrapStatusDipswitchIntfMode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchIntfMode1.setStatus("mandatory")


class _SfrapStatusDipswitchIntfMode2_Type(Integer32):
    """Custom type sfrapStatusDipswitchIntfMode2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("switch-down", 2),
          ("switch-up", 1))
    )


_SfrapStatusDipswitchIntfMode2_Type.__name__ = "Integer32"
_SfrapStatusDipswitchIntfMode2_Object = MibScalar
sfrapStatusDipswitchIntfMode2 = _SfrapStatusDipswitchIntfMode2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 10, 6),
    _SfrapStatusDipswitchIntfMode2_Type()
)
sfrapStatusDipswitchIntfMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusDipswitchIntfMode2.setStatus("mandatory")


class _SfrapVBertClear_Type(Integer32):
    """Custom type sfrapVBertClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-vbert", 1)
    )


_SfrapVBertClear_Type.__name__ = "Integer32"
_SfrapVBertClear_Object = MibScalar
sfrapVBertClear = _SfrapVBertClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 11),
    _SfrapVBertClear_Type()
)
sfrapVBertClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapVBertClear.setStatus("mandatory")


class _SfrapStatusLmiAutosense_Type(Integer32):
    """Custom type sfrapStatusLmiAutosense based on Integer32"""
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
          ("learned-annex-a", 4),
          ("learned-annex-d", 3),
          ("learned-type1", 5),
          ("searching", 2))
    )


_SfrapStatusLmiAutosense_Type.__name__ = "Integer32"
_SfrapStatusLmiAutosense_Object = MibScalar
sfrapStatusLmiAutosense = _SfrapStatusLmiAutosense_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 12),
    _SfrapStatusLmiAutosense_Type()
)
sfrapStatusLmiAutosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusLmiAutosense.setStatus("mandatory")


class _SfrapStatusTxClockDetect_Type(Integer32):
    """Custom type sfrapStatusTxClockDetect based on Integer32"""
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
        *(("failed-cut-thru", 4),
          ("failed-inband", 10),
          ("failed-inband-norm", 7),
          ("inactive", 1),
          ("initiate", 2),
          ("success-inband-invert", 9),
          ("success-inband-norm", 6),
          ("terminate", 11),
          ("trying-cut-thru", 3),
          ("trying-inband-invert", 8),
          ("trying-inband-norm", 5))
    )


_SfrapStatusTxClockDetect_Type.__name__ = "Integer32"
_SfrapStatusTxClockDetect_Object = MibScalar
sfrapStatusTxClockDetect = _SfrapStatusTxClockDetect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 4, 13),
    _SfrapStatusTxClockDetect_Type()
)
sfrapStatusTxClockDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapStatusTxClockDetect.setStatus("mandatory")
_SfrapPerformance_ObjectIdentity = ObjectIdentity
sfrapPerformance = _SfrapPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5)
)
_SfrapPerfMgmtIp_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIp = _SfrapPerfMgmtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2)
)
_SfrapPerfMgmtIpIFStatsTable_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIpIFStatsTable = _SfrapPerfMgmtIpIFStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 1)
)
_SfrapPerfMgmtIpIFInOctets_Type = Counter32
_SfrapPerfMgmtIpIFInOctets_Object = MibScalar
sfrapPerfMgmtIpIFInOctets = _SfrapPerfMgmtIpIFInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 1, 1),
    _SfrapPerfMgmtIpIFInOctets_Type()
)
sfrapPerfMgmtIpIFInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIFInOctets.setStatus("mandatory")
_SfrapPerfMgmtIpIFInErrors_Type = Counter32
_SfrapPerfMgmtIpIFInErrors_Object = MibScalar
sfrapPerfMgmtIpIFInErrors = _SfrapPerfMgmtIpIFInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 1, 2),
    _SfrapPerfMgmtIpIFInErrors_Type()
)
sfrapPerfMgmtIpIFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIFInErrors.setStatus("mandatory")
_SfrapPerfMgmtIpIFOutOctets_Type = Counter32
_SfrapPerfMgmtIpIFOutOctets_Object = MibScalar
sfrapPerfMgmtIpIFOutOctets = _SfrapPerfMgmtIpIFOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 1, 3),
    _SfrapPerfMgmtIpIFOutOctets_Type()
)
sfrapPerfMgmtIpIFOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIFOutOctets.setStatus("mandatory")


class _SfrapPerfMgmtIpIFOperStatus_Type(Integer32):
    """Custom type sfrapPerfMgmtIpIFOperStatus based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_SfrapPerfMgmtIpIFOperStatus_Type.__name__ = "Integer32"
_SfrapPerfMgmtIpIFOperStatus_Object = MibScalar
sfrapPerfMgmtIpIFOperStatus = _SfrapPerfMgmtIpIFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 1, 4),
    _SfrapPerfMgmtIpIFOperStatus_Type()
)
sfrapPerfMgmtIpIFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIFOperStatus.setStatus("mandatory")
_SfrapPerfMgmtIpIPStatsTable_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIpIPStatsTable = _SfrapPerfMgmtIpIPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2)
)
_SfrapPerfMgmtIpIPInRcv_Type = Counter32
_SfrapPerfMgmtIpIPInRcv_Object = MibScalar
sfrapPerfMgmtIpIPInRcv = _SfrapPerfMgmtIpIPInRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 1),
    _SfrapPerfMgmtIpIPInRcv_Type()
)
sfrapPerfMgmtIpIPInRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInRcv.setStatus("mandatory")
_SfrapPerfMgmtIpIPInHdrErr_Type = Counter32
_SfrapPerfMgmtIpIPInHdrErr_Object = MibScalar
sfrapPerfMgmtIpIPInHdrErr = _SfrapPerfMgmtIpIPInHdrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 2),
    _SfrapPerfMgmtIpIPInHdrErr_Type()
)
sfrapPerfMgmtIpIPInHdrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInHdrErr.setStatus("mandatory")
_SfrapPerfMgmtIpIPInAddrErr_Type = Counter32
_SfrapPerfMgmtIpIPInAddrErr_Object = MibScalar
sfrapPerfMgmtIpIPInAddrErr = _SfrapPerfMgmtIpIPInAddrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 3),
    _SfrapPerfMgmtIpIPInAddrErr_Type()
)
sfrapPerfMgmtIpIPInAddrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInAddrErr.setStatus("mandatory")
_SfrapPerfMgmtIpIPInProtUnk_Type = Counter32
_SfrapPerfMgmtIpIPInProtUnk_Object = MibScalar
sfrapPerfMgmtIpIPInProtUnk = _SfrapPerfMgmtIpIPInProtUnk_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 4),
    _SfrapPerfMgmtIpIPInProtUnk_Type()
)
sfrapPerfMgmtIpIPInProtUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInProtUnk.setStatus("mandatory")
_SfrapPerfMgmtIpIPInDscrd_Type = Counter32
_SfrapPerfMgmtIpIPInDscrd_Object = MibScalar
sfrapPerfMgmtIpIPInDscrd = _SfrapPerfMgmtIpIPInDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 5),
    _SfrapPerfMgmtIpIPInDscrd_Type()
)
sfrapPerfMgmtIpIPInDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInDscrd.setStatus("mandatory")
_SfrapPerfMgmtIpIPInDlvrs_Type = Counter32
_SfrapPerfMgmtIpIPInDlvrs_Object = MibScalar
sfrapPerfMgmtIpIPInDlvrs = _SfrapPerfMgmtIpIPInDlvrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 6),
    _SfrapPerfMgmtIpIPInDlvrs_Type()
)
sfrapPerfMgmtIpIPInDlvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPInDlvrs.setStatus("mandatory")
_SfrapPerfMgmtIpIPOutRqst_Type = Counter32
_SfrapPerfMgmtIpIPOutRqst_Object = MibScalar
sfrapPerfMgmtIpIPOutRqst = _SfrapPerfMgmtIpIPOutRqst_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 7),
    _SfrapPerfMgmtIpIPOutRqst_Type()
)
sfrapPerfMgmtIpIPOutRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPOutRqst.setStatus("mandatory")
_SfrapPerfMgmtIpIPOutDscrd_Type = Counter32
_SfrapPerfMgmtIpIPOutDscrd_Object = MibScalar
sfrapPerfMgmtIpIPOutDscrd = _SfrapPerfMgmtIpIPOutDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 8),
    _SfrapPerfMgmtIpIPOutDscrd_Type()
)
sfrapPerfMgmtIpIPOutDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPOutDscrd.setStatus("mandatory")
_SfrapPerfMgmtIpIPOutNoRt_Type = Counter32
_SfrapPerfMgmtIpIPOutNoRt_Object = MibScalar
sfrapPerfMgmtIpIPOutNoRt = _SfrapPerfMgmtIpIPOutNoRt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 2, 9),
    _SfrapPerfMgmtIpIPOutNoRt_Type()
)
sfrapPerfMgmtIpIPOutNoRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpIPOutNoRt.setStatus("mandatory")
_SfrapPerfMgmtIpICMPStatsTable_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIpICMPStatsTable = _SfrapPerfMgmtIpICMPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3)
)
_SfrapPerfMgmtIpICMPInMsgs_Type = Counter32
_SfrapPerfMgmtIpICMPInMsgs_Object = MibScalar
sfrapPerfMgmtIpICMPInMsgs = _SfrapPerfMgmtIpICMPInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 1),
    _SfrapPerfMgmtIpICMPInMsgs_Type()
)
sfrapPerfMgmtIpICMPInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInMsgs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInErrors_Type = Counter32
_SfrapPerfMgmtIpICMPInErrors_Object = MibScalar
sfrapPerfMgmtIpICMPInErrors = _SfrapPerfMgmtIpICMPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 2),
    _SfrapPerfMgmtIpICMPInErrors_Type()
)
sfrapPerfMgmtIpICMPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInErrors.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInDestUnreachs_Type = Counter32
_SfrapPerfMgmtIpICMPInDestUnreachs_Object = MibScalar
sfrapPerfMgmtIpICMPInDestUnreachs = _SfrapPerfMgmtIpICMPInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 3),
    _SfrapPerfMgmtIpICMPInDestUnreachs_Type()
)
sfrapPerfMgmtIpICMPInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInDestUnreachs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInTimeExcds_Type = Counter32
_SfrapPerfMgmtIpICMPInTimeExcds_Object = MibScalar
sfrapPerfMgmtIpICMPInTimeExcds = _SfrapPerfMgmtIpICMPInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 4),
    _SfrapPerfMgmtIpICMPInTimeExcds_Type()
)
sfrapPerfMgmtIpICMPInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInTimeExcds.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInParmProbs_Type = Counter32
_SfrapPerfMgmtIpICMPInParmProbs_Object = MibScalar
sfrapPerfMgmtIpICMPInParmProbs = _SfrapPerfMgmtIpICMPInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 5),
    _SfrapPerfMgmtIpICMPInParmProbs_Type()
)
sfrapPerfMgmtIpICMPInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInParmProbs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInRedirects_Type = Counter32
_SfrapPerfMgmtIpICMPInRedirects_Object = MibScalar
sfrapPerfMgmtIpICMPInRedirects = _SfrapPerfMgmtIpICMPInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 6),
    _SfrapPerfMgmtIpICMPInRedirects_Type()
)
sfrapPerfMgmtIpICMPInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInRedirects.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInEchos_Type = Counter32
_SfrapPerfMgmtIpICMPInEchos_Object = MibScalar
sfrapPerfMgmtIpICMPInEchos = _SfrapPerfMgmtIpICMPInEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 7),
    _SfrapPerfMgmtIpICMPInEchos_Type()
)
sfrapPerfMgmtIpICMPInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInEchos.setStatus("mandatory")
_SfrapPerfMgmtIpICMPInEchoReps_Type = Counter32
_SfrapPerfMgmtIpICMPInEchoReps_Object = MibScalar
sfrapPerfMgmtIpICMPInEchoReps = _SfrapPerfMgmtIpICMPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 8),
    _SfrapPerfMgmtIpICMPInEchoReps_Type()
)
sfrapPerfMgmtIpICMPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPInEchoReps.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutMsgs_Type = Counter32
_SfrapPerfMgmtIpICMPOutMsgs_Object = MibScalar
sfrapPerfMgmtIpICMPOutMsgs = _SfrapPerfMgmtIpICMPOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 9),
    _SfrapPerfMgmtIpICMPOutMsgs_Type()
)
sfrapPerfMgmtIpICMPOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutMsgs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutErrors_Type = Counter32
_SfrapPerfMgmtIpICMPOutErrors_Object = MibScalar
sfrapPerfMgmtIpICMPOutErrors = _SfrapPerfMgmtIpICMPOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 10),
    _SfrapPerfMgmtIpICMPOutErrors_Type()
)
sfrapPerfMgmtIpICMPOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutErrors.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutDestUnreachs_Type = Counter32
_SfrapPerfMgmtIpICMPOutDestUnreachs_Object = MibScalar
sfrapPerfMgmtIpICMPOutDestUnreachs = _SfrapPerfMgmtIpICMPOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 11),
    _SfrapPerfMgmtIpICMPOutDestUnreachs_Type()
)
sfrapPerfMgmtIpICMPOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutDestUnreachs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutParmProbs_Type = Counter32
_SfrapPerfMgmtIpICMPOutParmProbs_Object = MibScalar
sfrapPerfMgmtIpICMPOutParmProbs = _SfrapPerfMgmtIpICMPOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 12),
    _SfrapPerfMgmtIpICMPOutParmProbs_Type()
)
sfrapPerfMgmtIpICMPOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutParmProbs.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutRedirects_Type = Counter32
_SfrapPerfMgmtIpICMPOutRedirects_Object = MibScalar
sfrapPerfMgmtIpICMPOutRedirects = _SfrapPerfMgmtIpICMPOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 13),
    _SfrapPerfMgmtIpICMPOutRedirects_Type()
)
sfrapPerfMgmtIpICMPOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutRedirects.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutEchos_Type = Counter32
_SfrapPerfMgmtIpICMPOutEchos_Object = MibScalar
sfrapPerfMgmtIpICMPOutEchos = _SfrapPerfMgmtIpICMPOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 14),
    _SfrapPerfMgmtIpICMPOutEchos_Type()
)
sfrapPerfMgmtIpICMPOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutEchos.setStatus("mandatory")
_SfrapPerfMgmtIpICMPOutEchoReps_Type = Counter32
_SfrapPerfMgmtIpICMPOutEchoReps_Object = MibScalar
sfrapPerfMgmtIpICMPOutEchoReps = _SfrapPerfMgmtIpICMPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 3, 15),
    _SfrapPerfMgmtIpICMPOutEchoReps_Type()
)
sfrapPerfMgmtIpICMPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpICMPOutEchoReps.setStatus("mandatory")
_SfrapPerfMgmtIpUDPStatsTable_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIpUDPStatsTable = _SfrapPerfMgmtIpUDPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 4)
)
_SfrapPerfMgmtIpUDPInDatagrams_Type = Counter32
_SfrapPerfMgmtIpUDPInDatagrams_Object = MibScalar
sfrapPerfMgmtIpUDPInDatagrams = _SfrapPerfMgmtIpUDPInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 4, 1),
    _SfrapPerfMgmtIpUDPInDatagrams_Type()
)
sfrapPerfMgmtIpUDPInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpUDPInDatagrams.setStatus("mandatory")
_SfrapPerfMgmtIpUDPOutDatagrams_Type = Counter32
_SfrapPerfMgmtIpUDPOutDatagrams_Object = MibScalar
sfrapPerfMgmtIpUDPOutDatagrams = _SfrapPerfMgmtIpUDPOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 4, 2),
    _SfrapPerfMgmtIpUDPOutDatagrams_Type()
)
sfrapPerfMgmtIpUDPOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpUDPOutDatagrams.setStatus("mandatory")
_SfrapPerfMgmtIpUDPNoPorts_Type = Counter32
_SfrapPerfMgmtIpUDPNoPorts_Object = MibScalar
sfrapPerfMgmtIpUDPNoPorts = _SfrapPerfMgmtIpUDPNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 4, 3),
    _SfrapPerfMgmtIpUDPNoPorts_Type()
)
sfrapPerfMgmtIpUDPNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpUDPNoPorts.setStatus("mandatory")
_SfrapPerfMgmtIpTCPStatsTable_ObjectIdentity = ObjectIdentity
sfrapPerfMgmtIpTCPStatsTable = _SfrapPerfMgmtIpTCPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5)
)
_SfrapPerfMgmtIpTCPActiveOpens_Type = Counter32
_SfrapPerfMgmtIpTCPActiveOpens_Object = MibScalar
sfrapPerfMgmtIpTCPActiveOpens = _SfrapPerfMgmtIpTCPActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 1),
    _SfrapPerfMgmtIpTCPActiveOpens_Type()
)
sfrapPerfMgmtIpTCPActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPActiveOpens.setStatus("mandatory")
_SfrapPerfMgmtIpTCPPassiveOpens_Type = Counter32
_SfrapPerfMgmtIpTCPPassiveOpens_Object = MibScalar
sfrapPerfMgmtIpTCPPassiveOpens = _SfrapPerfMgmtIpTCPPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 2),
    _SfrapPerfMgmtIpTCPPassiveOpens_Type()
)
sfrapPerfMgmtIpTCPPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPPassiveOpens.setStatus("mandatory")
_SfrapPerfMgmtIpTCPAttemptFails_Type = Counter32
_SfrapPerfMgmtIpTCPAttemptFails_Object = MibScalar
sfrapPerfMgmtIpTCPAttemptFails = _SfrapPerfMgmtIpTCPAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 3),
    _SfrapPerfMgmtIpTCPAttemptFails_Type()
)
sfrapPerfMgmtIpTCPAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPAttemptFails.setStatus("mandatory")
_SfrapPerfMgmtIpTCPCurrEstab_Type = Gauge32
_SfrapPerfMgmtIpTCPCurrEstab_Object = MibScalar
sfrapPerfMgmtIpTCPCurrEstab = _SfrapPerfMgmtIpTCPCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 4),
    _SfrapPerfMgmtIpTCPCurrEstab_Type()
)
sfrapPerfMgmtIpTCPCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPCurrEstab.setStatus("mandatory")
_SfrapPerfMgmtIpTCPInSegs_Type = Counter32
_SfrapPerfMgmtIpTCPInSegs_Object = MibScalar
sfrapPerfMgmtIpTCPInSegs = _SfrapPerfMgmtIpTCPInSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 5),
    _SfrapPerfMgmtIpTCPInSegs_Type()
)
sfrapPerfMgmtIpTCPInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPInSegs.setStatus("mandatory")
_SfrapPerfMgmtIpTCPOutSegs_Type = Counter32
_SfrapPerfMgmtIpTCPOutSegs_Object = MibScalar
sfrapPerfMgmtIpTCPOutSegs = _SfrapPerfMgmtIpTCPOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 2, 5, 6),
    _SfrapPerfMgmtIpTCPOutSegs_Type()
)
sfrapPerfMgmtIpTCPOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfMgmtIpTCPOutSegs.setStatus("mandatory")
_SfrapPerfThruput_ObjectIdentity = ObjectIdentity
sfrapPerfThruput = _SfrapPerfThruput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3)
)
_SfrapPerfThruputPerIntfTable_Object = MibTable
sfrapPerfThruputPerIntfTable = _SfrapPerfThruputPerIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfTable.setStatus("mandatory")
_SfrapPerfThruputPerIntfEntry_Object = MibTableRow
sfrapPerfThruputPerIntfEntry = _SfrapPerfThruputPerIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1)
)
sfrapPerfThruputPerIntfEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfThruputPerIntfIndex"),
)
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfEntry.setStatus("mandatory")


class _SfrapPerfThruputPerIntfIndex_Type(Integer32):
    """Custom type sfrapPerfThruputPerIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce", 2),
          ("to-dte", 1))
    )


_SfrapPerfThruputPerIntfIndex_Type.__name__ = "Integer32"
_SfrapPerfThruputPerIntfIndex_Object = MibTableColumn
sfrapPerfThruputPerIntfIndex = _SfrapPerfThruputPerIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 1),
    _SfrapPerfThruputPerIntfIndex_Type()
)
sfrapPerfThruputPerIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfIndex.setStatus("mandatory")
_SfrapPerfThruputPerIntfRxByteCnt_Type = Counter32
_SfrapPerfThruputPerIntfRxByteCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfRxByteCnt = _SfrapPerfThruputPerIntfRxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 2),
    _SfrapPerfThruputPerIntfRxByteCnt_Type()
)
sfrapPerfThruputPerIntfRxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfRxByteCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfTxByteCnt_Type = Counter32
_SfrapPerfThruputPerIntfTxByteCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfTxByteCnt = _SfrapPerfThruputPerIntfTxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 3),
    _SfrapPerfThruputPerIntfTxByteCnt_Type()
)
sfrapPerfThruputPerIntfTxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfTxByteCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfRxFrameCnt_Type = Counter32
_SfrapPerfThruputPerIntfRxFrameCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfRxFrameCnt = _SfrapPerfThruputPerIntfRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 4),
    _SfrapPerfThruputPerIntfRxFrameCnt_Type()
)
sfrapPerfThruputPerIntfRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfRxFrameCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfTxFrameCnt_Type = Counter32
_SfrapPerfThruputPerIntfTxFrameCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfTxFrameCnt = _SfrapPerfThruputPerIntfTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 5),
    _SfrapPerfThruputPerIntfTxFrameCnt_Type()
)
sfrapPerfThruputPerIntfTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfTxFrameCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfRxCrcErrCnt_Type = Counter32
_SfrapPerfThruputPerIntfRxCrcErrCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfRxCrcErrCnt = _SfrapPerfThruputPerIntfRxCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 6),
    _SfrapPerfThruputPerIntfRxCrcErrCnt_Type()
)
sfrapPerfThruputPerIntfRxCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfRxCrcErrCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfRxAbortCnt_Type = Counter32
_SfrapPerfThruputPerIntfRxAbortCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfRxAbortCnt = _SfrapPerfThruputPerIntfRxAbortCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 7),
    _SfrapPerfThruputPerIntfRxAbortCnt_Type()
)
sfrapPerfThruputPerIntfRxAbortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfRxAbortCnt.setStatus("mandatory")
_SfrapPerfThruputPerIntfRxBpvCnt_Type = Counter32
_SfrapPerfThruputPerIntfRxBpvCnt_Object = MibTableColumn
sfrapPerfThruputPerIntfRxBpvCnt = _SfrapPerfThruputPerIntfRxBpvCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 1, 1, 8),
    _SfrapPerfThruputPerIntfRxBpvCnt_Type()
)
sfrapPerfThruputPerIntfRxBpvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerIntfRxBpvCnt.setStatus("mandatory")
_SfrapPerfThruputPerDlciTable_Object = MibTable
sfrapPerfThruputPerDlciTable = _SfrapPerfThruputPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2)
)
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTable.setStatus("mandatory")
_SfrapPerfThruputPerDlciEntry_Object = MibTableRow
sfrapPerfThruputPerDlciEntry = _SfrapPerfThruputPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1)
)
sfrapPerfThruputPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfThruputPerDlciIndex"),
    (0, "SFRAP-MIB", "sfrapPerfThruputPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciEntry.setStatus("mandatory")
_SfrapPerfThruputPerDlciIndex_Type = Index
_SfrapPerfThruputPerDlciIndex_Object = MibTableColumn
sfrapPerfThruputPerDlciIndex = _SfrapPerfThruputPerDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 1),
    _SfrapPerfThruputPerDlciIndex_Type()
)
sfrapPerfThruputPerDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciIndex.setStatus("mandatory")
_SfrapPerfThruputPerDlciValue_Type = Integer32
_SfrapPerfThruputPerDlciValue_Object = MibTableColumn
sfrapPerfThruputPerDlciValue = _SfrapPerfThruputPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 2),
    _SfrapPerfThruputPerDlciValue_Type()
)
sfrapPerfThruputPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciValue.setStatus("mandatory")
_SfrapPerfThruputPerDlciCreateTime_Type = Integer32
_SfrapPerfThruputPerDlciCreateTime_Object = MibTableColumn
sfrapPerfThruputPerDlciCreateTime = _SfrapPerfThruputPerDlciCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 3),
    _SfrapPerfThruputPerDlciCreateTime_Type()
)
sfrapPerfThruputPerDlciCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciCreateTime.setStatus("mandatory")
_SfrapPerfThruputPerDlciChangeTime_Type = Integer32
_SfrapPerfThruputPerDlciChangeTime_Object = MibTableColumn
sfrapPerfThruputPerDlciChangeTime = _SfrapPerfThruputPerDlciChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 4),
    _SfrapPerfThruputPerDlciChangeTime_Type()
)
sfrapPerfThruputPerDlciChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciChangeTime.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxByte_Type = Counter32
_SfrapPerfThruputPerDlciRxByte_Object = MibTableColumn
sfrapPerfThruputPerDlciRxByte = _SfrapPerfThruputPerDlciRxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 5),
    _SfrapPerfThruputPerDlciRxByte_Type()
)
sfrapPerfThruputPerDlciRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxByte.setStatus("mandatory")
_SfrapPerfThruputPerDlciTxByte_Type = Counter32
_SfrapPerfThruputPerDlciTxByte_Object = MibTableColumn
sfrapPerfThruputPerDlciTxByte = _SfrapPerfThruputPerDlciTxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 6),
    _SfrapPerfThruputPerDlciTxByte_Type()
)
sfrapPerfThruputPerDlciTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTxByte.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxFrame_Type = Counter32
_SfrapPerfThruputPerDlciRxFrame_Object = MibTableColumn
sfrapPerfThruputPerDlciRxFrame = _SfrapPerfThruputPerDlciRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 7),
    _SfrapPerfThruputPerDlciRxFrame_Type()
)
sfrapPerfThruputPerDlciRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxFrame.setStatus("mandatory")
_SfrapPerfThruputPerDlciTxFrame_Type = Counter32
_SfrapPerfThruputPerDlciTxFrame_Object = MibTableColumn
sfrapPerfThruputPerDlciTxFrame = _SfrapPerfThruputPerDlciTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 8),
    _SfrapPerfThruputPerDlciTxFrame_Type()
)
sfrapPerfThruputPerDlciTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTxFrame.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxFecn_Type = Counter32
_SfrapPerfThruputPerDlciRxFecn_Object = MibTableColumn
sfrapPerfThruputPerDlciRxFecn = _SfrapPerfThruputPerDlciRxFecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 9),
    _SfrapPerfThruputPerDlciRxFecn_Type()
)
sfrapPerfThruputPerDlciRxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxFecn.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxBecn_Type = Counter32
_SfrapPerfThruputPerDlciRxBecn_Object = MibTableColumn
sfrapPerfThruputPerDlciRxBecn = _SfrapPerfThruputPerDlciRxBecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 10),
    _SfrapPerfThruputPerDlciRxBecn_Type()
)
sfrapPerfThruputPerDlciRxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxBecn.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxDe_Type = Counter32
_SfrapPerfThruputPerDlciRxDe_Object = MibTableColumn
sfrapPerfThruputPerDlciRxDe = _SfrapPerfThruputPerDlciRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 11),
    _SfrapPerfThruputPerDlciRxDe_Type()
)
sfrapPerfThruputPerDlciRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxDe.setStatus("mandatory")
_SfrapPerfThruputPerDlciTxDe_Type = Counter32
_SfrapPerfThruputPerDlciTxDe_Object = MibTableColumn
sfrapPerfThruputPerDlciTxDe = _SfrapPerfThruputPerDlciTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 12),
    _SfrapPerfThruputPerDlciTxDe_Type()
)
sfrapPerfThruputPerDlciTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTxDe.setStatus("mandatory")
_SfrapPerfThruputPerDlciRxThruput_Type = Integer32
_SfrapPerfThruputPerDlciRxThruput_Object = MibTableColumn
sfrapPerfThruputPerDlciRxThruput = _SfrapPerfThruputPerDlciRxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 13),
    _SfrapPerfThruputPerDlciRxThruput_Type()
)
sfrapPerfThruputPerDlciRxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxThruput.setStatus("mandatory")
_SfrapPerfThruputPerDlciTxThruput_Type = Integer32
_SfrapPerfThruputPerDlciTxThruput_Object = MibTableColumn
sfrapPerfThruputPerDlciTxThruput = _SfrapPerfThruputPerDlciTxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 14),
    _SfrapPerfThruputPerDlciTxThruput_Type()
)
sfrapPerfThruputPerDlciTxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTxThruput.setStatus("mandatory")
_SfrapPerfThruputPerDlciCIR_Type = Integer32
_SfrapPerfThruputPerDlciCIR_Object = MibTableColumn
sfrapPerfThruputPerDlciCIR = _SfrapPerfThruputPerDlciCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 15),
    _SfrapPerfThruputPerDlciCIR_Type()
)
sfrapPerfThruputPerDlciCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciCIR.setStatus("mandatory")
_SfrapPerfThruputPerDlciUptime_Type = Integer32
_SfrapPerfThruputPerDlciUptime_Object = MibTableColumn
sfrapPerfThruputPerDlciUptime = _SfrapPerfThruputPerDlciUptime_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 16),
    _SfrapPerfThruputPerDlciUptime_Type()
)
sfrapPerfThruputPerDlciUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciUptime.setStatus("mandatory")
_SfrapPerfThruputPerDlciDowntime_Type = Integer32
_SfrapPerfThruputPerDlciDowntime_Object = MibTableColumn
sfrapPerfThruputPerDlciDowntime = _SfrapPerfThruputPerDlciDowntime_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 17),
    _SfrapPerfThruputPerDlciDowntime_Type()
)
sfrapPerfThruputPerDlciDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciDowntime.setStatus("mandatory")


class _SfrapPerfThruputPerDlciCirType_Type(Integer32):
    """Custom type sfrapPerfThruputPerDlciCirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cir-acquired-from-lmi", 1),
          ("cir-configured-by-user", 2),
          ("cir-is-dte-datarate", 3))
    )


_SfrapPerfThruputPerDlciCirType_Type.__name__ = "Integer32"
_SfrapPerfThruputPerDlciCirType_Object = MibTableColumn
sfrapPerfThruputPerDlciCirType = _SfrapPerfThruputPerDlciCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 18),
    _SfrapPerfThruputPerDlciCirType_Type()
)
sfrapPerfThruputPerDlciCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciCirType.setStatus("mandatory")


class _SfrapPerfThruputPerDlciPvcState_Type(Integer32):
    """Custom type sfrapPerfThruputPerDlciPvcState based on Integer32"""
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
        *(("pvc-active", 1),
          ("pvc-inactive", 2),
          ("pvc-lmi-timeout", 5),
          ("pvc-not-in-lmi", 4),
          ("pvc-undetermined", 6),
          ("pvc-unprovisioned", 3))
    )


_SfrapPerfThruputPerDlciPvcState_Type.__name__ = "Integer32"
_SfrapPerfThruputPerDlciPvcState_Object = MibTableColumn
sfrapPerfThruputPerDlciPvcState = _SfrapPerfThruputPerDlciPvcState_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 19),
    _SfrapPerfThruputPerDlciPvcState_Type()
)
sfrapPerfThruputPerDlciPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciPvcState.setStatus("mandatory")
_SfrapPerfThruputPerDlciOutageCount_Type = Counter32
_SfrapPerfThruputPerDlciOutageCount_Object = MibTableColumn
sfrapPerfThruputPerDlciOutageCount = _SfrapPerfThruputPerDlciOutageCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 20),
    _SfrapPerfThruputPerDlciOutageCount_Type()
)
sfrapPerfThruputPerDlciOutageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciOutageCount.setStatus("mandatory")
_SfrapPerfThruputPerDlciAvailability_Type = Integer32
_SfrapPerfThruputPerDlciAvailability_Object = MibTableColumn
sfrapPerfThruputPerDlciAvailability = _SfrapPerfThruputPerDlciAvailability_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 21),
    _SfrapPerfThruputPerDlciAvailability_Type()
)
sfrapPerfThruputPerDlciAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciAvailability.setStatus("mandatory")
_SfrapPerfThruputPerDlciMTBSO_Type = Integer32
_SfrapPerfThruputPerDlciMTBSO_Object = MibTableColumn
sfrapPerfThruputPerDlciMTBSO = _SfrapPerfThruputPerDlciMTBSO_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 22),
    _SfrapPerfThruputPerDlciMTBSO_Type()
)
sfrapPerfThruputPerDlciMTBSO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciMTBSO.setStatus("mandatory")
_SfrapPerfThruputPerDlciMTTSR_Type = Integer32
_SfrapPerfThruputPerDlciMTTSR_Object = MibTableColumn
sfrapPerfThruputPerDlciMTTSR = _SfrapPerfThruputPerDlciMTTSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 23),
    _SfrapPerfThruputPerDlciMTTSR_Type()
)
sfrapPerfThruputPerDlciMTTSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciMTTSR.setStatus("mandatory")


class _SfrapPerfThruputPerDlciEncapType_Type(Integer32):
    """Custom type sfrapPerfThruputPerDlciEncapType based on Integer32"""
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
        *(("encap-1490", 2),
          ("encap-annex-g", 4),
          ("encap-cisco", 3),
          ("encap-na", 1),
          ("encap-other", 5))
    )


_SfrapPerfThruputPerDlciEncapType_Type.__name__ = "Integer32"
_SfrapPerfThruputPerDlciEncapType_Object = MibTableColumn
sfrapPerfThruputPerDlciEncapType = _SfrapPerfThruputPerDlciEncapType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 24),
    _SfrapPerfThruputPerDlciEncapType_Type()
)
sfrapPerfThruputPerDlciEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciEncapType.setStatus("mandatory")


class _SfrapPerfThruputPerDlciRxUtilizationStatus_Type(Integer32):
    """Custom type sfrapPerfThruputPerDlciRxUtilizationStatus based on Integer32"""
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
        *(("alarm", 3),
          ("alarm-under-threshold", 4),
          ("clear", 1),
          ("over-threshold", 2))
    )


_SfrapPerfThruputPerDlciRxUtilizationStatus_Type.__name__ = "Integer32"
_SfrapPerfThruputPerDlciRxUtilizationStatus_Object = MibTableColumn
sfrapPerfThruputPerDlciRxUtilizationStatus = _SfrapPerfThruputPerDlciRxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 25),
    _SfrapPerfThruputPerDlciRxUtilizationStatus_Type()
)
sfrapPerfThruputPerDlciRxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciRxUtilizationStatus.setStatus("mandatory")


class _SfrapPerfThruputPerDlciTxUtilizationStatus_Type(Integer32):
    """Custom type sfrapPerfThruputPerDlciTxUtilizationStatus based on Integer32"""
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
        *(("alarm", 3),
          ("alarm-under-threshold", 4),
          ("clear", 1),
          ("over-threshold", 2))
    )


_SfrapPerfThruputPerDlciTxUtilizationStatus_Type.__name__ = "Integer32"
_SfrapPerfThruputPerDlciTxUtilizationStatus_Object = MibTableColumn
sfrapPerfThruputPerDlciTxUtilizationStatus = _SfrapPerfThruputPerDlciTxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 26),
    _SfrapPerfThruputPerDlciTxUtilizationStatus_Type()
)
sfrapPerfThruputPerDlciTxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciTxUtilizationStatus.setStatus("mandatory")
_SfrapPerfThruputPerDlciEIR_Type = Integer32
_SfrapPerfThruputPerDlciEIR_Object = MibTableColumn
sfrapPerfThruputPerDlciEIR = _SfrapPerfThruputPerDlciEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 2, 1, 27),
    _SfrapPerfThruputPerDlciEIR_Type()
)
sfrapPerfThruputPerDlciEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputPerDlciEIR.setStatus("mandatory")
_SfrapPerfThruputCommands_ObjectIdentity = ObjectIdentity
sfrapPerfThruputCommands = _SfrapPerfThruputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3)
)


class _SfrapPerfThruputCmdClearToDteStats_Type(Integer32):
    """Custom type sfrapPerfThruputCmdClearToDteStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfThruputCmdClearToDteStats_Type.__name__ = "Integer32"
_SfrapPerfThruputCmdClearToDteStats_Object = MibScalar
sfrapPerfThruputCmdClearToDteStats = _SfrapPerfThruputCmdClearToDteStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 1),
    _SfrapPerfThruputCmdClearToDteStats_Type()
)
sfrapPerfThruputCmdClearToDteStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdClearToDteStats.setStatus("mandatory")


class _SfrapPerfThruputCmdClearToDceStats_Type(Integer32):
    """Custom type sfrapPerfThruputCmdClearToDceStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfThruputCmdClearToDceStats_Type.__name__ = "Integer32"
_SfrapPerfThruputCmdClearToDceStats_Object = MibScalar
sfrapPerfThruputCmdClearToDceStats = _SfrapPerfThruputCmdClearToDceStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 2),
    _SfrapPerfThruputCmdClearToDceStats_Type()
)
sfrapPerfThruputCmdClearToDceStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdClearToDceStats.setStatus("mandatory")


class _SfrapPerfThruputCmdClearAllIntfStats_Type(Integer32):
    """Custom type sfrapPerfThruputCmdClearAllIntfStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfThruputCmdClearAllIntfStats_Type.__name__ = "Integer32"
_SfrapPerfThruputCmdClearAllIntfStats_Object = MibScalar
sfrapPerfThruputCmdClearAllIntfStats = _SfrapPerfThruputCmdClearAllIntfStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 3),
    _SfrapPerfThruputCmdClearAllIntfStats_Type()
)
sfrapPerfThruputCmdClearAllIntfStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdClearAllIntfStats.setStatus("mandatory")


class _SfrapPerfThruputCmdClearDlciStats_Type(Integer32):
    """Custom type sfrapPerfThruputCmdClearDlciStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfThruputCmdClearDlciStats_Type.__name__ = "Integer32"
_SfrapPerfThruputCmdClearDlciStats_Object = MibScalar
sfrapPerfThruputCmdClearDlciStats = _SfrapPerfThruputCmdClearDlciStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 4),
    _SfrapPerfThruputCmdClearDlciStats_Type()
)
sfrapPerfThruputCmdClearDlciStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdClearDlciStats.setStatus("mandatory")


class _SfrapPerfThruputCmdClearAllStats_Type(Integer32):
    """Custom type sfrapPerfThruputCmdClearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfThruputCmdClearAllStats_Type.__name__ = "Integer32"
_SfrapPerfThruputCmdClearAllStats_Object = MibScalar
sfrapPerfThruputCmdClearAllStats = _SfrapPerfThruputCmdClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 5),
    _SfrapPerfThruputCmdClearAllStats_Type()
)
sfrapPerfThruputCmdClearAllStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdClearAllStats.setStatus("mandatory")
_SfrapPerfThruputCmdRemoveStsDlci_Type = Integer32
_SfrapPerfThruputCmdRemoveStsDlci_Object = MibScalar
sfrapPerfThruputCmdRemoveStsDlci = _SfrapPerfThruputCmdRemoveStsDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 6),
    _SfrapPerfThruputCmdRemoveStsDlci_Type()
)
sfrapPerfThruputCmdRemoveStsDlci.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdRemoveStsDlci.setStatus("mandatory")
_SfrapPerfThruputCmdReplaceDlciTable_Object = MibTable
sfrapPerfThruputCmdReplaceDlciTable = _SfrapPerfThruputCmdReplaceDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 7)
)
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdReplaceDlciTable.setStatus("mandatory")
_SfrapPerfThruputCmdReplaceDlciEntry_Object = MibTableRow
sfrapPerfThruputCmdReplaceDlciEntry = _SfrapPerfThruputCmdReplaceDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 7, 1)
)
sfrapPerfThruputCmdReplaceDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfThruputCmdReplaceDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdReplaceDlciEntry.setStatus("mandatory")
_SfrapPerfThruputCmdReplaceDlciValue_Type = Integer32
_SfrapPerfThruputCmdReplaceDlciValue_Object = MibTableColumn
sfrapPerfThruputCmdReplaceDlciValue = _SfrapPerfThruputCmdReplaceDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 7, 1, 1),
    _SfrapPerfThruputCmdReplaceDlciValue_Type()
)
sfrapPerfThruputCmdReplaceDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdReplaceDlciValue.setStatus("mandatory")
_SfrapPerfThruputCmdReplaceDlciNewValue_Type = Integer32
_SfrapPerfThruputCmdReplaceDlciNewValue_Object = MibTableColumn
sfrapPerfThruputCmdReplaceDlciNewValue = _SfrapPerfThruputCmdReplaceDlciNewValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 7, 1, 2),
    _SfrapPerfThruputCmdReplaceDlciNewValue_Type()
)
sfrapPerfThruputCmdReplaceDlciNewValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdReplaceDlciNewValue.setStatus("mandatory")
_SfrapPerfThruputCmdAvailabilityStsDlciReset_Type = Integer32
_SfrapPerfThruputCmdAvailabilityStsDlciReset_Object = MibScalar
sfrapPerfThruputCmdAvailabilityStsDlciReset = _SfrapPerfThruputCmdAvailabilityStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 8),
    _SfrapPerfThruputCmdAvailabilityStsDlciReset_Type()
)
sfrapPerfThruputCmdAvailabilityStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdAvailabilityStsDlciReset.setStatus("mandatory")
_SfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type = Integer32
_SfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object = MibScalar
sfrapPerfThruputCmdAvailabilityStsDlciResetAll = _SfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 9),
    _SfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type()
)
sfrapPerfThruputCmdAvailabilityStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdAvailabilityStsDlciResetAll.setStatus("mandatory")
_SfrapPerfThruputCmdCountsStsDlciReset_Type = Integer32
_SfrapPerfThruputCmdCountsStsDlciReset_Object = MibScalar
sfrapPerfThruputCmdCountsStsDlciReset = _SfrapPerfThruputCmdCountsStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 10),
    _SfrapPerfThruputCmdCountsStsDlciReset_Type()
)
sfrapPerfThruputCmdCountsStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdCountsStsDlciReset.setStatus("mandatory")
_SfrapPerfThruputCmdCountsStsDlciResetAll_Type = Integer32
_SfrapPerfThruputCmdCountsStsDlciResetAll_Object = MibScalar
sfrapPerfThruputCmdCountsStsDlciResetAll = _SfrapPerfThruputCmdCountsStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 11),
    _SfrapPerfThruputCmdCountsStsDlciResetAll_Type()
)
sfrapPerfThruputCmdCountsStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdCountsStsDlciResetAll.setStatus("mandatory")
_SfrapPerfThruputCmdAllStsDlciReset_Type = Integer32
_SfrapPerfThruputCmdAllStsDlciReset_Object = MibScalar
sfrapPerfThruputCmdAllStsDlciReset = _SfrapPerfThruputCmdAllStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 12),
    _SfrapPerfThruputCmdAllStsDlciReset_Type()
)
sfrapPerfThruputCmdAllStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdAllStsDlciReset.setStatus("mandatory")
_SfrapPerfThruputCmdAllStsDlciResetAll_Type = Integer32
_SfrapPerfThruputCmdAllStsDlciResetAll_Object = MibScalar
sfrapPerfThruputCmdAllStsDlciResetAll = _SfrapPerfThruputCmdAllStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 3, 3, 13),
    _SfrapPerfThruputCmdAllStsDlciResetAll_Type()
)
sfrapPerfThruputCmdAllStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfThruputCmdAllStsDlciResetAll.setStatus("mandatory")
_SfrapPerfNetworkShortTerm_ObjectIdentity = ObjectIdentity
sfrapPerfNetworkShortTerm = _SfrapPerfNetworkShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4)
)
_SfrapPerfNetwProtoPerDlciTable_Object = MibTable
sfrapPerfNetwProtoPerDlciTable = _SfrapPerfNetwProtoPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1)
)
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTable.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciEntry_Object = MibTableRow
sfrapPerfNetwProtoPerDlciEntry = _SfrapPerfNetwProtoPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1)
)
sfrapPerfNetwProtoPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfNetwProtoPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfNetwProtoPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciEntry.setStatus("mandatory")


class _SfrapPerfNetwProtoPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfNetwProtoPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfNetwProtoPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfNetwProtoPerDlciInterval_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciInterval = _SfrapPerfNetwProtoPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 1),
    _SfrapPerfNetwProtoPerDlciInterval_Type()
)
sfrapPerfNetwProtoPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciInterval.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciValue_Type = Integer32
_SfrapPerfNetwProtoPerDlciValue_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciValue = _SfrapPerfNetwProtoPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 2),
    _SfrapPerfNetwProtoPerDlciValue_Type()
)
sfrapPerfNetwProtoPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciValue.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxTotal_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxTotal_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxTotal = _SfrapPerfNetwProtoPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 3),
    _SfrapPerfNetwProtoPerDlciRxTotal_Type()
)
sfrapPerfNetwProtoPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxTotal_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxTotal_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxTotal = _SfrapPerfNetwProtoPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 4),
    _SfrapPerfNetwProtoPerDlciTxTotal_Type()
)
sfrapPerfNetwProtoPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxIp_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxIp_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxIp = _SfrapPerfNetwProtoPerDlciRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 5),
    _SfrapPerfNetwProtoPerDlciRxIp_Type()
)
sfrapPerfNetwProtoPerDlciRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxIp.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxIp_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxIp_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxIp = _SfrapPerfNetwProtoPerDlciTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 6),
    _SfrapPerfNetwProtoPerDlciTxIp_Type()
)
sfrapPerfNetwProtoPerDlciTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxIp.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxIpx_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxIpx_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxIpx = _SfrapPerfNetwProtoPerDlciRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 7),
    _SfrapPerfNetwProtoPerDlciRxIpx_Type()
)
sfrapPerfNetwProtoPerDlciRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxIpx.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxIpx_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxIpx_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxIpx = _SfrapPerfNetwProtoPerDlciTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 8),
    _SfrapPerfNetwProtoPerDlciTxIpx_Type()
)
sfrapPerfNetwProtoPerDlciTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxIpx.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxSna_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxSna_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxSna = _SfrapPerfNetwProtoPerDlciRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 9),
    _SfrapPerfNetwProtoPerDlciRxSna_Type()
)
sfrapPerfNetwProtoPerDlciRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxSna.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxSna_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxSna_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxSna = _SfrapPerfNetwProtoPerDlciTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 10),
    _SfrapPerfNetwProtoPerDlciTxSna_Type()
)
sfrapPerfNetwProtoPerDlciTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxSna.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxArp_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxArp_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxArp = _SfrapPerfNetwProtoPerDlciRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 11),
    _SfrapPerfNetwProtoPerDlciRxArp_Type()
)
sfrapPerfNetwProtoPerDlciRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxArp.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxArp_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxArp_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxArp = _SfrapPerfNetwProtoPerDlciTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 12),
    _SfrapPerfNetwProtoPerDlciTxArp_Type()
)
sfrapPerfNetwProtoPerDlciTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxArp.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxCisco_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxCisco_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxCisco = _SfrapPerfNetwProtoPerDlciRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 13),
    _SfrapPerfNetwProtoPerDlciRxCisco_Type()
)
sfrapPerfNetwProtoPerDlciRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxCisco.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxCisco_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxCisco_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxCisco = _SfrapPerfNetwProtoPerDlciTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 14),
    _SfrapPerfNetwProtoPerDlciTxCisco_Type()
)
sfrapPerfNetwProtoPerDlciTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxCisco.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxOther_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxOther_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxOther = _SfrapPerfNetwProtoPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 15),
    _SfrapPerfNetwProtoPerDlciRxOther_Type()
)
sfrapPerfNetwProtoPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxOther.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxOther_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxOther_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxOther = _SfrapPerfNetwProtoPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 16),
    _SfrapPerfNetwProtoPerDlciTxOther_Type()
)
sfrapPerfNetwProtoPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxOther.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxVnip_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxVnip_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxVnip = _SfrapPerfNetwProtoPerDlciRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 17),
    _SfrapPerfNetwProtoPerDlciRxVnip_Type()
)
sfrapPerfNetwProtoPerDlciRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxVnip.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxVnip_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxVnip_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxVnip = _SfrapPerfNetwProtoPerDlciTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 18),
    _SfrapPerfNetwProtoPerDlciTxVnip_Type()
)
sfrapPerfNetwProtoPerDlciTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxVnip.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciRxAnnexG_Type = Counter32
_SfrapPerfNetwProtoPerDlciRxAnnexG_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciRxAnnexG = _SfrapPerfNetwProtoPerDlciRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 19),
    _SfrapPerfNetwProtoPerDlciRxAnnexG_Type()
)
sfrapPerfNetwProtoPerDlciRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciRxAnnexG.setStatus("mandatory")
_SfrapPerfNetwProtoPerDlciTxAnnexG_Type = Counter32
_SfrapPerfNetwProtoPerDlciTxAnnexG_Object = MibTableColumn
sfrapPerfNetwProtoPerDlciTxAnnexG = _SfrapPerfNetwProtoPerDlciTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 1, 1, 20),
    _SfrapPerfNetwProtoPerDlciTxAnnexG_Type()
)
sfrapPerfNetwProtoPerDlciTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoPerDlciTxAnnexG.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTable_Object = MibTable
sfrapPerfNetwProtoTotalTable = _SfrapPerfNetwProtoTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2)
)
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTable.setStatus("mandatory")
_SfrapPerfNetwProtoTotalEntry_Object = MibTableRow
sfrapPerfNetwProtoTotalEntry = _SfrapPerfNetwProtoTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1)
)
sfrapPerfNetwProtoTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfNetwProtoTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalEntry.setStatus("mandatory")


class _SfrapPerfNetwProtoTotalInterval_Type(Integer32):
    """Custom type sfrapPerfNetwProtoTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfNetwProtoTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfNetwProtoTotalInterval_Object = MibTableColumn
sfrapPerfNetwProtoTotalInterval = _SfrapPerfNetwProtoTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 1),
    _SfrapPerfNetwProtoTotalInterval_Type()
)
sfrapPerfNetwProtoTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalInterval.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxTotal_Type = Counter32
_SfrapPerfNetwProtoTotalRxTotal_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxTotal = _SfrapPerfNetwProtoTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 3),
    _SfrapPerfNetwProtoTotalRxTotal_Type()
)
sfrapPerfNetwProtoTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxTotal.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxTotal_Type = Counter32
_SfrapPerfNetwProtoTotalTxTotal_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxTotal = _SfrapPerfNetwProtoTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 4),
    _SfrapPerfNetwProtoTotalTxTotal_Type()
)
sfrapPerfNetwProtoTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxTotal.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxIp_Type = Counter32
_SfrapPerfNetwProtoTotalRxIp_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxIp = _SfrapPerfNetwProtoTotalRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 5),
    _SfrapPerfNetwProtoTotalRxIp_Type()
)
sfrapPerfNetwProtoTotalRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxIp.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxIp_Type = Counter32
_SfrapPerfNetwProtoTotalTxIp_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxIp = _SfrapPerfNetwProtoTotalTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 6),
    _SfrapPerfNetwProtoTotalTxIp_Type()
)
sfrapPerfNetwProtoTotalTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxIp.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxIpx_Type = Counter32
_SfrapPerfNetwProtoTotalRxIpx_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxIpx = _SfrapPerfNetwProtoTotalRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 7),
    _SfrapPerfNetwProtoTotalRxIpx_Type()
)
sfrapPerfNetwProtoTotalRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxIpx.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxIpx_Type = Counter32
_SfrapPerfNetwProtoTotalTxIpx_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxIpx = _SfrapPerfNetwProtoTotalTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 8),
    _SfrapPerfNetwProtoTotalTxIpx_Type()
)
sfrapPerfNetwProtoTotalTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxIpx.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxSna_Type = Counter32
_SfrapPerfNetwProtoTotalRxSna_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxSna = _SfrapPerfNetwProtoTotalRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 9),
    _SfrapPerfNetwProtoTotalRxSna_Type()
)
sfrapPerfNetwProtoTotalRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxSna.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxSna_Type = Counter32
_SfrapPerfNetwProtoTotalTxSna_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxSna = _SfrapPerfNetwProtoTotalTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 10),
    _SfrapPerfNetwProtoTotalTxSna_Type()
)
sfrapPerfNetwProtoTotalTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxSna.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxArp_Type = Counter32
_SfrapPerfNetwProtoTotalRxArp_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxArp = _SfrapPerfNetwProtoTotalRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 11),
    _SfrapPerfNetwProtoTotalRxArp_Type()
)
sfrapPerfNetwProtoTotalRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxArp.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxArp_Type = Counter32
_SfrapPerfNetwProtoTotalTxArp_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxArp = _SfrapPerfNetwProtoTotalTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 12),
    _SfrapPerfNetwProtoTotalTxArp_Type()
)
sfrapPerfNetwProtoTotalTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxArp.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxCisco_Type = Counter32
_SfrapPerfNetwProtoTotalRxCisco_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxCisco = _SfrapPerfNetwProtoTotalRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 13),
    _SfrapPerfNetwProtoTotalRxCisco_Type()
)
sfrapPerfNetwProtoTotalRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxCisco.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxCisco_Type = Counter32
_SfrapPerfNetwProtoTotalTxCisco_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxCisco = _SfrapPerfNetwProtoTotalTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 14),
    _SfrapPerfNetwProtoTotalTxCisco_Type()
)
sfrapPerfNetwProtoTotalTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxCisco.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxOther_Type = Counter32
_SfrapPerfNetwProtoTotalRxOther_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxOther = _SfrapPerfNetwProtoTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 15),
    _SfrapPerfNetwProtoTotalRxOther_Type()
)
sfrapPerfNetwProtoTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxOther.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxOther_Type = Counter32
_SfrapPerfNetwProtoTotalTxOther_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxOther = _SfrapPerfNetwProtoTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 16),
    _SfrapPerfNetwProtoTotalTxOther_Type()
)
sfrapPerfNetwProtoTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxOther.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxVnip_Type = Counter32
_SfrapPerfNetwProtoTotalRxVnip_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxVnip = _SfrapPerfNetwProtoTotalRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 17),
    _SfrapPerfNetwProtoTotalRxVnip_Type()
)
sfrapPerfNetwProtoTotalRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxVnip.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxVnip_Type = Counter32
_SfrapPerfNetwProtoTotalTxVnip_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxVnip = _SfrapPerfNetwProtoTotalTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 18),
    _SfrapPerfNetwProtoTotalTxVnip_Type()
)
sfrapPerfNetwProtoTotalTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxVnip.setStatus("mandatory")
_SfrapPerfNetwProtoTotalRxAnnexG_Type = Counter32
_SfrapPerfNetwProtoTotalRxAnnexG_Object = MibTableColumn
sfrapPerfNetwProtoTotalRxAnnexG = _SfrapPerfNetwProtoTotalRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 19),
    _SfrapPerfNetwProtoTotalRxAnnexG_Type()
)
sfrapPerfNetwProtoTotalRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalRxAnnexG.setStatus("mandatory")
_SfrapPerfNetwProtoTotalTxAnnexG_Type = Counter32
_SfrapPerfNetwProtoTotalTxAnnexG_Object = MibTableColumn
sfrapPerfNetwProtoTotalTxAnnexG = _SfrapPerfNetwProtoTotalTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 2, 1, 20),
    _SfrapPerfNetwProtoTotalTxAnnexG_Type()
)
sfrapPerfNetwProtoTotalTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwProtoTotalTxAnnexG.setStatus("mandatory")
_SfrapPerfIpPerDlciTable_Object = MibTable
sfrapPerfIpPerDlciTable = _SfrapPerfIpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3)
)
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTable.setStatus("mandatory")
_SfrapPerfIpPerDlciEntry_Object = MibTableRow
sfrapPerfIpPerDlciEntry = _SfrapPerfIpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1)
)
sfrapPerfIpPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIpPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfIpPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciEntry.setStatus("mandatory")


class _SfrapPerfIpPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfIpPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIpPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfIpPerDlciInterval_Object = MibTableColumn
sfrapPerfIpPerDlciInterval = _SfrapPerfIpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 1),
    _SfrapPerfIpPerDlciInterval_Type()
)
sfrapPerfIpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciInterval.setStatus("mandatory")
_SfrapPerfIpPerDlciValue_Type = Integer32
_SfrapPerfIpPerDlciValue_Object = MibTableColumn
sfrapPerfIpPerDlciValue = _SfrapPerfIpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 2),
    _SfrapPerfIpPerDlciValue_Type()
)
sfrapPerfIpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciValue.setStatus("mandatory")
_SfrapPerfIpPerDlciRxTotal_Type = Counter32
_SfrapPerfIpPerDlciRxTotal_Object = MibTableColumn
sfrapPerfIpPerDlciRxTotal = _SfrapPerfIpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 3),
    _SfrapPerfIpPerDlciRxTotal_Type()
)
sfrapPerfIpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfIpPerDlciTxTotal_Type = Counter32
_SfrapPerfIpPerDlciTxTotal_Object = MibTableColumn
sfrapPerfIpPerDlciTxTotal = _SfrapPerfIpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 4),
    _SfrapPerfIpPerDlciTxTotal_Type()
)
sfrapPerfIpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfIpPerDlciRxTcp_Type = Counter32
_SfrapPerfIpPerDlciRxTcp_Object = MibTableColumn
sfrapPerfIpPerDlciRxTcp = _SfrapPerfIpPerDlciRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 5),
    _SfrapPerfIpPerDlciRxTcp_Type()
)
sfrapPerfIpPerDlciRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxTcp.setStatus("mandatory")
_SfrapPerfIpPerDlciTxTcp_Type = Counter32
_SfrapPerfIpPerDlciTxTcp_Object = MibTableColumn
sfrapPerfIpPerDlciTxTcp = _SfrapPerfIpPerDlciTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 6),
    _SfrapPerfIpPerDlciTxTcp_Type()
)
sfrapPerfIpPerDlciTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxTcp.setStatus("mandatory")
_SfrapPerfIpPerDlciRxUdp_Type = Counter32
_SfrapPerfIpPerDlciRxUdp_Object = MibTableColumn
sfrapPerfIpPerDlciRxUdp = _SfrapPerfIpPerDlciRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 7),
    _SfrapPerfIpPerDlciRxUdp_Type()
)
sfrapPerfIpPerDlciRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxUdp.setStatus("mandatory")
_SfrapPerfIpPerDlciTxUdp_Type = Counter32
_SfrapPerfIpPerDlciTxUdp_Object = MibTableColumn
sfrapPerfIpPerDlciTxUdp = _SfrapPerfIpPerDlciTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 8),
    _SfrapPerfIpPerDlciTxUdp_Type()
)
sfrapPerfIpPerDlciTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxUdp.setStatus("mandatory")
_SfrapPerfIpPerDlciRxIcmp_Type = Counter32
_SfrapPerfIpPerDlciRxIcmp_Object = MibTableColumn
sfrapPerfIpPerDlciRxIcmp = _SfrapPerfIpPerDlciRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 9),
    _SfrapPerfIpPerDlciRxIcmp_Type()
)
sfrapPerfIpPerDlciRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxIcmp.setStatus("mandatory")
_SfrapPerfIpPerDlciTxIcmp_Type = Counter32
_SfrapPerfIpPerDlciTxIcmp_Object = MibTableColumn
sfrapPerfIpPerDlciTxIcmp = _SfrapPerfIpPerDlciTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 10),
    _SfrapPerfIpPerDlciTxIcmp_Type()
)
sfrapPerfIpPerDlciTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxIcmp.setStatus("mandatory")
_SfrapPerfIpPerDlciRxOther_Type = Counter32
_SfrapPerfIpPerDlciRxOther_Object = MibTableColumn
sfrapPerfIpPerDlciRxOther = _SfrapPerfIpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 11),
    _SfrapPerfIpPerDlciRxOther_Type()
)
sfrapPerfIpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxOther.setStatus("mandatory")
_SfrapPerfIpPerDlciTxOther_Type = Counter32
_SfrapPerfIpPerDlciTxOther_Object = MibTableColumn
sfrapPerfIpPerDlciTxOther = _SfrapPerfIpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 12),
    _SfrapPerfIpPerDlciTxOther_Type()
)
sfrapPerfIpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxOther.setStatus("mandatory")
_SfrapPerfIpPerDlciRxIgrp_Type = Counter32
_SfrapPerfIpPerDlciRxIgrp_Object = MibTableColumn
sfrapPerfIpPerDlciRxIgrp = _SfrapPerfIpPerDlciRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 13),
    _SfrapPerfIpPerDlciRxIgrp_Type()
)
sfrapPerfIpPerDlciRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciRxIgrp.setStatus("mandatory")
_SfrapPerfIpPerDlciTxIgrp_Type = Counter32
_SfrapPerfIpPerDlciTxIgrp_Object = MibTableColumn
sfrapPerfIpPerDlciTxIgrp = _SfrapPerfIpPerDlciTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 3, 1, 14),
    _SfrapPerfIpPerDlciTxIgrp_Type()
)
sfrapPerfIpPerDlciTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpPerDlciTxIgrp.setStatus("mandatory")
_SfrapPerfIpTotalTable_Object = MibTable
sfrapPerfIpTotalTable = _SfrapPerfIpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4)
)
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTable.setStatus("mandatory")
_SfrapPerfIpTotalEntry_Object = MibTableRow
sfrapPerfIpTotalEntry = _SfrapPerfIpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1)
)
sfrapPerfIpTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIpTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfIpTotalEntry.setStatus("mandatory")


class _SfrapPerfIpTotalInterval_Type(Integer32):
    """Custom type sfrapPerfIpTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIpTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfIpTotalInterval_Object = MibTableColumn
sfrapPerfIpTotalInterval = _SfrapPerfIpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 1),
    _SfrapPerfIpTotalInterval_Type()
)
sfrapPerfIpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalInterval.setStatus("mandatory")
_SfrapPerfIpTotalRxTotal_Type = Counter32
_SfrapPerfIpTotalRxTotal_Object = MibTableColumn
sfrapPerfIpTotalRxTotal = _SfrapPerfIpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 3),
    _SfrapPerfIpTotalRxTotal_Type()
)
sfrapPerfIpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxTotal.setStatus("mandatory")
_SfrapPerfIpTotalTxTotal_Type = Counter32
_SfrapPerfIpTotalTxTotal_Object = MibTableColumn
sfrapPerfIpTotalTxTotal = _SfrapPerfIpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 4),
    _SfrapPerfIpTotalTxTotal_Type()
)
sfrapPerfIpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxTotal.setStatus("mandatory")
_SfrapPerfIpTotalRxTcp_Type = Counter32
_SfrapPerfIpTotalRxTcp_Object = MibTableColumn
sfrapPerfIpTotalRxTcp = _SfrapPerfIpTotalRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 5),
    _SfrapPerfIpTotalRxTcp_Type()
)
sfrapPerfIpTotalRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxTcp.setStatus("mandatory")
_SfrapPerfIpTotalTxTcp_Type = Counter32
_SfrapPerfIpTotalTxTcp_Object = MibTableColumn
sfrapPerfIpTotalTxTcp = _SfrapPerfIpTotalTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 6),
    _SfrapPerfIpTotalTxTcp_Type()
)
sfrapPerfIpTotalTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxTcp.setStatus("mandatory")
_SfrapPerfIpTotalRxUdp_Type = Counter32
_SfrapPerfIpTotalRxUdp_Object = MibTableColumn
sfrapPerfIpTotalRxUdp = _SfrapPerfIpTotalRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 7),
    _SfrapPerfIpTotalRxUdp_Type()
)
sfrapPerfIpTotalRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxUdp.setStatus("mandatory")
_SfrapPerfIpTotalTxUdp_Type = Counter32
_SfrapPerfIpTotalTxUdp_Object = MibTableColumn
sfrapPerfIpTotalTxUdp = _SfrapPerfIpTotalTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 8),
    _SfrapPerfIpTotalTxUdp_Type()
)
sfrapPerfIpTotalTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxUdp.setStatus("mandatory")
_SfrapPerfIpTotalRxIcmp_Type = Counter32
_SfrapPerfIpTotalRxIcmp_Object = MibTableColumn
sfrapPerfIpTotalRxIcmp = _SfrapPerfIpTotalRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 9),
    _SfrapPerfIpTotalRxIcmp_Type()
)
sfrapPerfIpTotalRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxIcmp.setStatus("mandatory")
_SfrapPerfIpTotalTxIcmp_Type = Counter32
_SfrapPerfIpTotalTxIcmp_Object = MibTableColumn
sfrapPerfIpTotalTxIcmp = _SfrapPerfIpTotalTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 10),
    _SfrapPerfIpTotalTxIcmp_Type()
)
sfrapPerfIpTotalTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxIcmp.setStatus("mandatory")
_SfrapPerfIpTotalRxOther_Type = Counter32
_SfrapPerfIpTotalRxOther_Object = MibTableColumn
sfrapPerfIpTotalRxOther = _SfrapPerfIpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 11),
    _SfrapPerfIpTotalRxOther_Type()
)
sfrapPerfIpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxOther.setStatus("mandatory")
_SfrapPerfIpTotalTxOther_Type = Counter32
_SfrapPerfIpTotalTxOther_Object = MibTableColumn
sfrapPerfIpTotalTxOther = _SfrapPerfIpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 12),
    _SfrapPerfIpTotalTxOther_Type()
)
sfrapPerfIpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxOther.setStatus("mandatory")
_SfrapPerfIpTotalRxIgrp_Type = Counter32
_SfrapPerfIpTotalRxIgrp_Object = MibTableColumn
sfrapPerfIpTotalRxIgrp = _SfrapPerfIpTotalRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 13),
    _SfrapPerfIpTotalRxIgrp_Type()
)
sfrapPerfIpTotalRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalRxIgrp.setStatus("mandatory")
_SfrapPerfIpTotalTxIgrp_Type = Counter32
_SfrapPerfIpTotalTxIgrp_Object = MibTableColumn
sfrapPerfIpTotalTxIgrp = _SfrapPerfIpTotalTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 4, 1, 14),
    _SfrapPerfIpTotalTxIgrp_Type()
)
sfrapPerfIpTotalTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpTotalTxIgrp.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTable_Object = MibTable
sfrapPerfIcmpPerDlciTable = _SfrapPerfIcmpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5)
)
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTable.setStatus("mandatory")
_SfrapPerfIcmpPerDlciEntry_Object = MibTableRow
sfrapPerfIcmpPerDlciEntry = _SfrapPerfIcmpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1)
)
sfrapPerfIcmpPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIcmpPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfIcmpPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciEntry.setStatus("mandatory")


class _SfrapPerfIcmpPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfIcmpPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIcmpPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfIcmpPerDlciInterval_Object = MibTableColumn
sfrapPerfIcmpPerDlciInterval = _SfrapPerfIcmpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 1),
    _SfrapPerfIcmpPerDlciInterval_Type()
)
sfrapPerfIcmpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciInterval.setStatus("mandatory")
_SfrapPerfIcmpPerDlciValue_Type = Integer32
_SfrapPerfIcmpPerDlciValue_Object = MibTableColumn
sfrapPerfIcmpPerDlciValue = _SfrapPerfIcmpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 2),
    _SfrapPerfIcmpPerDlciValue_Type()
)
sfrapPerfIcmpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciValue.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxTotal_Type = Counter32
_SfrapPerfIcmpPerDlciRxTotal_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxTotal = _SfrapPerfIcmpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 3),
    _SfrapPerfIcmpPerDlciRxTotal_Type()
)
sfrapPerfIcmpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxTotal_Type = Counter32
_SfrapPerfIcmpPerDlciTxTotal_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxTotal = _SfrapPerfIcmpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 4),
    _SfrapPerfIcmpPerDlciTxTotal_Type()
)
sfrapPerfIcmpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxEchoRep_Type = Counter32
_SfrapPerfIcmpPerDlciRxEchoRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxEchoRep = _SfrapPerfIcmpPerDlciRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 5),
    _SfrapPerfIcmpPerDlciRxEchoRep_Type()
)
sfrapPerfIcmpPerDlciRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxEchoRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxEchoRep_Type = Counter32
_SfrapPerfIcmpPerDlciTxEchoRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxEchoRep = _SfrapPerfIcmpPerDlciTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 6),
    _SfrapPerfIcmpPerDlciTxEchoRep_Type()
)
sfrapPerfIcmpPerDlciTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxEchoRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxDestUnr_Type = Counter32
_SfrapPerfIcmpPerDlciRxDestUnr_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxDestUnr = _SfrapPerfIcmpPerDlciRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 7),
    _SfrapPerfIcmpPerDlciRxDestUnr_Type()
)
sfrapPerfIcmpPerDlciRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxDestUnr.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxDestUnr_Type = Counter32
_SfrapPerfIcmpPerDlciTxDestUnr_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxDestUnr = _SfrapPerfIcmpPerDlciTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 8),
    _SfrapPerfIcmpPerDlciTxDestUnr_Type()
)
sfrapPerfIcmpPerDlciTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxDestUnr.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxSrcQuench_Type = Counter32
_SfrapPerfIcmpPerDlciRxSrcQuench_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxSrcQuench = _SfrapPerfIcmpPerDlciRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 9),
    _SfrapPerfIcmpPerDlciRxSrcQuench_Type()
)
sfrapPerfIcmpPerDlciRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxSrcQuench.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxSrcQuench_Type = Counter32
_SfrapPerfIcmpPerDlciTxSrcQuench_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxSrcQuench = _SfrapPerfIcmpPerDlciTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 10),
    _SfrapPerfIcmpPerDlciTxSrcQuench_Type()
)
sfrapPerfIcmpPerDlciTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxSrcQuench.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxRedirect_Type = Counter32
_SfrapPerfIcmpPerDlciRxRedirect_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxRedirect = _SfrapPerfIcmpPerDlciRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 11),
    _SfrapPerfIcmpPerDlciRxRedirect_Type()
)
sfrapPerfIcmpPerDlciRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxRedirect.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxRedirect_Type = Counter32
_SfrapPerfIcmpPerDlciTxRedirect_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxRedirect = _SfrapPerfIcmpPerDlciTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 12),
    _SfrapPerfIcmpPerDlciTxRedirect_Type()
)
sfrapPerfIcmpPerDlciTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxRedirect.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxEchoReq_Type = Counter32
_SfrapPerfIcmpPerDlciRxEchoReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxEchoReq = _SfrapPerfIcmpPerDlciRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 13),
    _SfrapPerfIcmpPerDlciRxEchoReq_Type()
)
sfrapPerfIcmpPerDlciRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxEchoReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxEchoReq_Type = Counter32
_SfrapPerfIcmpPerDlciTxEchoReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxEchoReq = _SfrapPerfIcmpPerDlciTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 14),
    _SfrapPerfIcmpPerDlciTxEchoReq_Type()
)
sfrapPerfIcmpPerDlciTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxEchoReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxTimeExcd_Type = Counter32
_SfrapPerfIcmpPerDlciRxTimeExcd_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxTimeExcd = _SfrapPerfIcmpPerDlciRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 15),
    _SfrapPerfIcmpPerDlciRxTimeExcd_Type()
)
sfrapPerfIcmpPerDlciRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxTimeExcd.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxTimeExcd_Type = Counter32
_SfrapPerfIcmpPerDlciTxTimeExcd_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxTimeExcd = _SfrapPerfIcmpPerDlciTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 16),
    _SfrapPerfIcmpPerDlciTxTimeExcd_Type()
)
sfrapPerfIcmpPerDlciTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxTimeExcd.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxParamProb_Type = Counter32
_SfrapPerfIcmpPerDlciRxParamProb_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxParamProb = _SfrapPerfIcmpPerDlciRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 17),
    _SfrapPerfIcmpPerDlciRxParamProb_Type()
)
sfrapPerfIcmpPerDlciRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxParamProb.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxParamProb_Type = Counter32
_SfrapPerfIcmpPerDlciTxParamProb_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxParamProb = _SfrapPerfIcmpPerDlciTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 18),
    _SfrapPerfIcmpPerDlciTxParamProb_Type()
)
sfrapPerfIcmpPerDlciTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxParamProb.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxTimestpReq_Type = Counter32
_SfrapPerfIcmpPerDlciRxTimestpReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxTimestpReq = _SfrapPerfIcmpPerDlciRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 19),
    _SfrapPerfIcmpPerDlciRxTimestpReq_Type()
)
sfrapPerfIcmpPerDlciRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxTimestpReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxTimestpReq_Type = Counter32
_SfrapPerfIcmpPerDlciTxTimestpReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxTimestpReq = _SfrapPerfIcmpPerDlciTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 20),
    _SfrapPerfIcmpPerDlciTxTimestpReq_Type()
)
sfrapPerfIcmpPerDlciTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxTimestpReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxTimestpRep_Type = Counter32
_SfrapPerfIcmpPerDlciRxTimestpRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxTimestpRep = _SfrapPerfIcmpPerDlciRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 21),
    _SfrapPerfIcmpPerDlciRxTimestpRep_Type()
)
sfrapPerfIcmpPerDlciRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxTimestpRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxTimestpRep_Type = Counter32
_SfrapPerfIcmpPerDlciTxTimestpRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxTimestpRep = _SfrapPerfIcmpPerDlciTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 22),
    _SfrapPerfIcmpPerDlciTxTimestpRep_Type()
)
sfrapPerfIcmpPerDlciTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxTimestpRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxAddrMaskReq_Type = Counter32
_SfrapPerfIcmpPerDlciRxAddrMaskReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxAddrMaskReq = _SfrapPerfIcmpPerDlciRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 23),
    _SfrapPerfIcmpPerDlciRxAddrMaskReq_Type()
)
sfrapPerfIcmpPerDlciRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxAddrMaskReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxAddrMaskReq_Type = Counter32
_SfrapPerfIcmpPerDlciTxAddrMaskReq_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxAddrMaskReq = _SfrapPerfIcmpPerDlciTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 24),
    _SfrapPerfIcmpPerDlciTxAddrMaskReq_Type()
)
sfrapPerfIcmpPerDlciTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxAddrMaskReq.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxAddrMaskRep_Type = Counter32
_SfrapPerfIcmpPerDlciRxAddrMaskRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxAddrMaskRep = _SfrapPerfIcmpPerDlciRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 25),
    _SfrapPerfIcmpPerDlciRxAddrMaskRep_Type()
)
sfrapPerfIcmpPerDlciRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxAddrMaskRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxAddrMaskRep_Type = Counter32
_SfrapPerfIcmpPerDlciTxAddrMaskRep_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxAddrMaskRep = _SfrapPerfIcmpPerDlciTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 26),
    _SfrapPerfIcmpPerDlciTxAddrMaskRep_Type()
)
sfrapPerfIcmpPerDlciTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxAddrMaskRep.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxPktTooBig_Type = Counter32
_SfrapPerfIcmpPerDlciRxPktTooBig_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxPktTooBig = _SfrapPerfIcmpPerDlciRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 27),
    _SfrapPerfIcmpPerDlciRxPktTooBig_Type()
)
sfrapPerfIcmpPerDlciRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxPktTooBig.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxPktTooBig_Type = Counter32
_SfrapPerfIcmpPerDlciTxPktTooBig_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxPktTooBig = _SfrapPerfIcmpPerDlciTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 28),
    _SfrapPerfIcmpPerDlciTxPktTooBig_Type()
)
sfrapPerfIcmpPerDlciTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxPktTooBig.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxGmQuery_Type = Counter32
_SfrapPerfIcmpPerDlciRxGmQuery_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxGmQuery = _SfrapPerfIcmpPerDlciRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 29),
    _SfrapPerfIcmpPerDlciRxGmQuery_Type()
)
sfrapPerfIcmpPerDlciRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxGmQuery.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxGmQuery_Type = Counter32
_SfrapPerfIcmpPerDlciTxGmQuery_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxGmQuery = _SfrapPerfIcmpPerDlciTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 30),
    _SfrapPerfIcmpPerDlciTxGmQuery_Type()
)
sfrapPerfIcmpPerDlciTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxGmQuery.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxGmReport_Type = Counter32
_SfrapPerfIcmpPerDlciRxGmReport_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxGmReport = _SfrapPerfIcmpPerDlciRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 31),
    _SfrapPerfIcmpPerDlciRxGmReport_Type()
)
sfrapPerfIcmpPerDlciRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxGmReport.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxGmReport_Type = Counter32
_SfrapPerfIcmpPerDlciTxGmReport_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxGmReport = _SfrapPerfIcmpPerDlciTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 32),
    _SfrapPerfIcmpPerDlciTxGmReport_Type()
)
sfrapPerfIcmpPerDlciTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxGmReport.setStatus("mandatory")
_SfrapPerfIcmpPerDlciRxGmReduct_Type = Counter32
_SfrapPerfIcmpPerDlciRxGmReduct_Object = MibTableColumn
sfrapPerfIcmpPerDlciRxGmReduct = _SfrapPerfIcmpPerDlciRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 33),
    _SfrapPerfIcmpPerDlciRxGmReduct_Type()
)
sfrapPerfIcmpPerDlciRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciRxGmReduct.setStatus("mandatory")
_SfrapPerfIcmpPerDlciTxGmReduct_Type = Counter32
_SfrapPerfIcmpPerDlciTxGmReduct_Object = MibTableColumn
sfrapPerfIcmpPerDlciTxGmReduct = _SfrapPerfIcmpPerDlciTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 5, 1, 34),
    _SfrapPerfIcmpPerDlciTxGmReduct_Type()
)
sfrapPerfIcmpPerDlciTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpPerDlciTxGmReduct.setStatus("mandatory")
_SfrapPerfIcmpTotalTable_Object = MibTable
sfrapPerfIcmpTotalTable = _SfrapPerfIcmpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6)
)
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTable.setStatus("mandatory")
_SfrapPerfIcmpTotalEntry_Object = MibTableRow
sfrapPerfIcmpTotalEntry = _SfrapPerfIcmpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1)
)
sfrapPerfIcmpTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIcmpTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalEntry.setStatus("mandatory")


class _SfrapPerfIcmpTotalInterval_Type(Integer32):
    """Custom type sfrapPerfIcmpTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIcmpTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfIcmpTotalInterval_Object = MibTableColumn
sfrapPerfIcmpTotalInterval = _SfrapPerfIcmpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 1),
    _SfrapPerfIcmpTotalInterval_Type()
)
sfrapPerfIcmpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalInterval.setStatus("mandatory")
_SfrapPerfIcmpTotalRxTotal_Type = Counter32
_SfrapPerfIcmpTotalRxTotal_Object = MibTableColumn
sfrapPerfIcmpTotalRxTotal = _SfrapPerfIcmpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 3),
    _SfrapPerfIcmpTotalRxTotal_Type()
)
sfrapPerfIcmpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxTotal.setStatus("mandatory")
_SfrapPerfIcmpTotalTxTotal_Type = Counter32
_SfrapPerfIcmpTotalTxTotal_Object = MibTableColumn
sfrapPerfIcmpTotalTxTotal = _SfrapPerfIcmpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 4),
    _SfrapPerfIcmpTotalTxTotal_Type()
)
sfrapPerfIcmpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxTotal.setStatus("mandatory")
_SfrapPerfIcmpTotalRxEchoRep_Type = Counter32
_SfrapPerfIcmpTotalRxEchoRep_Object = MibTableColumn
sfrapPerfIcmpTotalRxEchoRep = _SfrapPerfIcmpTotalRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 5),
    _SfrapPerfIcmpTotalRxEchoRep_Type()
)
sfrapPerfIcmpTotalRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxEchoRep.setStatus("mandatory")
_SfrapPerfIcmpTotalTxEchoRep_Type = Counter32
_SfrapPerfIcmpTotalTxEchoRep_Object = MibTableColumn
sfrapPerfIcmpTotalTxEchoRep = _SfrapPerfIcmpTotalTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 6),
    _SfrapPerfIcmpTotalTxEchoRep_Type()
)
sfrapPerfIcmpTotalTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxEchoRep.setStatus("mandatory")
_SfrapPerfIcmpTotalRxDestUnr_Type = Counter32
_SfrapPerfIcmpTotalRxDestUnr_Object = MibTableColumn
sfrapPerfIcmpTotalRxDestUnr = _SfrapPerfIcmpTotalRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 7),
    _SfrapPerfIcmpTotalRxDestUnr_Type()
)
sfrapPerfIcmpTotalRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxDestUnr.setStatus("mandatory")
_SfrapPerfIcmpTotalTxDestUnr_Type = Counter32
_SfrapPerfIcmpTotalTxDestUnr_Object = MibTableColumn
sfrapPerfIcmpTotalTxDestUnr = _SfrapPerfIcmpTotalTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 8),
    _SfrapPerfIcmpTotalTxDestUnr_Type()
)
sfrapPerfIcmpTotalTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxDestUnr.setStatus("mandatory")
_SfrapPerfIcmpTotalRxSrcQuench_Type = Counter32
_SfrapPerfIcmpTotalRxSrcQuench_Object = MibTableColumn
sfrapPerfIcmpTotalRxSrcQuench = _SfrapPerfIcmpTotalRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 9),
    _SfrapPerfIcmpTotalRxSrcQuench_Type()
)
sfrapPerfIcmpTotalRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxSrcQuench.setStatus("mandatory")
_SfrapPerfIcmpTotalTxSrcQuench_Type = Counter32
_SfrapPerfIcmpTotalTxSrcQuench_Object = MibTableColumn
sfrapPerfIcmpTotalTxSrcQuench = _SfrapPerfIcmpTotalTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 10),
    _SfrapPerfIcmpTotalTxSrcQuench_Type()
)
sfrapPerfIcmpTotalTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxSrcQuench.setStatus("mandatory")
_SfrapPerfIcmpTotalRxRedirect_Type = Counter32
_SfrapPerfIcmpTotalRxRedirect_Object = MibTableColumn
sfrapPerfIcmpTotalRxRedirect = _SfrapPerfIcmpTotalRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 11),
    _SfrapPerfIcmpTotalRxRedirect_Type()
)
sfrapPerfIcmpTotalRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxRedirect.setStatus("mandatory")
_SfrapPerfIcmpTotalTxRedirect_Type = Counter32
_SfrapPerfIcmpTotalTxRedirect_Object = MibTableColumn
sfrapPerfIcmpTotalTxRedirect = _SfrapPerfIcmpTotalTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 12),
    _SfrapPerfIcmpTotalTxRedirect_Type()
)
sfrapPerfIcmpTotalTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxRedirect.setStatus("mandatory")
_SfrapPerfIcmpTotalRxEchoReq_Type = Counter32
_SfrapPerfIcmpTotalRxEchoReq_Object = MibTableColumn
sfrapPerfIcmpTotalRxEchoReq = _SfrapPerfIcmpTotalRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 13),
    _SfrapPerfIcmpTotalRxEchoReq_Type()
)
sfrapPerfIcmpTotalRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxEchoReq.setStatus("mandatory")
_SfrapPerfIcmpTotalTxEchoReq_Type = Counter32
_SfrapPerfIcmpTotalTxEchoReq_Object = MibTableColumn
sfrapPerfIcmpTotalTxEchoReq = _SfrapPerfIcmpTotalTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 14),
    _SfrapPerfIcmpTotalTxEchoReq_Type()
)
sfrapPerfIcmpTotalTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxEchoReq.setStatus("mandatory")
_SfrapPerfIcmpTotalRxTimeExcd_Type = Counter32
_SfrapPerfIcmpTotalRxTimeExcd_Object = MibTableColumn
sfrapPerfIcmpTotalRxTimeExcd = _SfrapPerfIcmpTotalRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 15),
    _SfrapPerfIcmpTotalRxTimeExcd_Type()
)
sfrapPerfIcmpTotalRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxTimeExcd.setStatus("mandatory")
_SfrapPerfIcmpTotalTxTimeExcd_Type = Counter32
_SfrapPerfIcmpTotalTxTimeExcd_Object = MibTableColumn
sfrapPerfIcmpTotalTxTimeExcd = _SfrapPerfIcmpTotalTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 16),
    _SfrapPerfIcmpTotalTxTimeExcd_Type()
)
sfrapPerfIcmpTotalTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxTimeExcd.setStatus("mandatory")
_SfrapPerfIcmpTotalRxParamProb_Type = Counter32
_SfrapPerfIcmpTotalRxParamProb_Object = MibTableColumn
sfrapPerfIcmpTotalRxParamProb = _SfrapPerfIcmpTotalRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 17),
    _SfrapPerfIcmpTotalRxParamProb_Type()
)
sfrapPerfIcmpTotalRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxParamProb.setStatus("mandatory")
_SfrapPerfIcmpTotalTxParamProb_Type = Counter32
_SfrapPerfIcmpTotalTxParamProb_Object = MibTableColumn
sfrapPerfIcmpTotalTxParamProb = _SfrapPerfIcmpTotalTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 18),
    _SfrapPerfIcmpTotalTxParamProb_Type()
)
sfrapPerfIcmpTotalTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxParamProb.setStatus("mandatory")
_SfrapPerfIcmpTotalRxTimestpReq_Type = Counter32
_SfrapPerfIcmpTotalRxTimestpReq_Object = MibTableColumn
sfrapPerfIcmpTotalRxTimestpReq = _SfrapPerfIcmpTotalRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 19),
    _SfrapPerfIcmpTotalRxTimestpReq_Type()
)
sfrapPerfIcmpTotalRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxTimestpReq.setStatus("mandatory")
_SfrapPerfIcmpTotalTxTimestpReq_Type = Counter32
_SfrapPerfIcmpTotalTxTimestpReq_Object = MibTableColumn
sfrapPerfIcmpTotalTxTimestpReq = _SfrapPerfIcmpTotalTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 20),
    _SfrapPerfIcmpTotalTxTimestpReq_Type()
)
sfrapPerfIcmpTotalTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxTimestpReq.setStatus("mandatory")
_SfrapPerfIcmpTotalRxTimestpRep_Type = Counter32
_SfrapPerfIcmpTotalRxTimestpRep_Object = MibTableColumn
sfrapPerfIcmpTotalRxTimestpRep = _SfrapPerfIcmpTotalRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 21),
    _SfrapPerfIcmpTotalRxTimestpRep_Type()
)
sfrapPerfIcmpTotalRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxTimestpRep.setStatus("mandatory")
_SfrapPerfIcmpTotalTxTimestpRep_Type = Counter32
_SfrapPerfIcmpTotalTxTimestpRep_Object = MibTableColumn
sfrapPerfIcmpTotalTxTimestpRep = _SfrapPerfIcmpTotalTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 22),
    _SfrapPerfIcmpTotalTxTimestpRep_Type()
)
sfrapPerfIcmpTotalTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxTimestpRep.setStatus("mandatory")
_SfrapPerfIcmpTotalRxAddrMaskReq_Type = Counter32
_SfrapPerfIcmpTotalRxAddrMaskReq_Object = MibTableColumn
sfrapPerfIcmpTotalRxAddrMaskReq = _SfrapPerfIcmpTotalRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 23),
    _SfrapPerfIcmpTotalRxAddrMaskReq_Type()
)
sfrapPerfIcmpTotalRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxAddrMaskReq.setStatus("mandatory")
_SfrapPerfIcmpTotalTxAddrMaskReq_Type = Counter32
_SfrapPerfIcmpTotalTxAddrMaskReq_Object = MibTableColumn
sfrapPerfIcmpTotalTxAddrMaskReq = _SfrapPerfIcmpTotalTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 24),
    _SfrapPerfIcmpTotalTxAddrMaskReq_Type()
)
sfrapPerfIcmpTotalTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxAddrMaskReq.setStatus("mandatory")
_SfrapPerfIcmpTotalRxAddrMaskRep_Type = Counter32
_SfrapPerfIcmpTotalRxAddrMaskRep_Object = MibTableColumn
sfrapPerfIcmpTotalRxAddrMaskRep = _SfrapPerfIcmpTotalRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 25),
    _SfrapPerfIcmpTotalRxAddrMaskRep_Type()
)
sfrapPerfIcmpTotalRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxAddrMaskRep.setStatus("mandatory")
_SfrapPerfIcmpTotalTxAddrMaskRep_Type = Counter32
_SfrapPerfIcmpTotalTxAddrMaskRep_Object = MibTableColumn
sfrapPerfIcmpTotalTxAddrMaskRep = _SfrapPerfIcmpTotalTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 26),
    _SfrapPerfIcmpTotalTxAddrMaskRep_Type()
)
sfrapPerfIcmpTotalTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxAddrMaskRep.setStatus("mandatory")
_SfrapPerfIcmpTotalRxPktTooBig_Type = Counter32
_SfrapPerfIcmpTotalRxPktTooBig_Object = MibTableColumn
sfrapPerfIcmpTotalRxPktTooBig = _SfrapPerfIcmpTotalRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 27),
    _SfrapPerfIcmpTotalRxPktTooBig_Type()
)
sfrapPerfIcmpTotalRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxPktTooBig.setStatus("mandatory")
_SfrapPerfIcmpTotalTxPktTooBig_Type = Counter32
_SfrapPerfIcmpTotalTxPktTooBig_Object = MibTableColumn
sfrapPerfIcmpTotalTxPktTooBig = _SfrapPerfIcmpTotalTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 28),
    _SfrapPerfIcmpTotalTxPktTooBig_Type()
)
sfrapPerfIcmpTotalTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxPktTooBig.setStatus("mandatory")
_SfrapPerfIcmpTotalRxGmQuery_Type = Counter32
_SfrapPerfIcmpTotalRxGmQuery_Object = MibTableColumn
sfrapPerfIcmpTotalRxGmQuery = _SfrapPerfIcmpTotalRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 29),
    _SfrapPerfIcmpTotalRxGmQuery_Type()
)
sfrapPerfIcmpTotalRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxGmQuery.setStatus("mandatory")
_SfrapPerfIcmpTotalTxGmQuery_Type = Counter32
_SfrapPerfIcmpTotalTxGmQuery_Object = MibTableColumn
sfrapPerfIcmpTotalTxGmQuery = _SfrapPerfIcmpTotalTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 30),
    _SfrapPerfIcmpTotalTxGmQuery_Type()
)
sfrapPerfIcmpTotalTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxGmQuery.setStatus("mandatory")
_SfrapPerfIcmpTotalRxGmReport_Type = Counter32
_SfrapPerfIcmpTotalRxGmReport_Object = MibTableColumn
sfrapPerfIcmpTotalRxGmReport = _SfrapPerfIcmpTotalRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 31),
    _SfrapPerfIcmpTotalRxGmReport_Type()
)
sfrapPerfIcmpTotalRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxGmReport.setStatus("mandatory")
_SfrapPerfIcmpTotalTxGmReport_Type = Counter32
_SfrapPerfIcmpTotalTxGmReport_Object = MibTableColumn
sfrapPerfIcmpTotalTxGmReport = _SfrapPerfIcmpTotalTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 32),
    _SfrapPerfIcmpTotalTxGmReport_Type()
)
sfrapPerfIcmpTotalTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxGmReport.setStatus("mandatory")
_SfrapPerfIcmpTotalRxGmReduct_Type = Counter32
_SfrapPerfIcmpTotalRxGmReduct_Object = MibTableColumn
sfrapPerfIcmpTotalRxGmReduct = _SfrapPerfIcmpTotalRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 33),
    _SfrapPerfIcmpTotalRxGmReduct_Type()
)
sfrapPerfIcmpTotalRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalRxGmReduct.setStatus("mandatory")
_SfrapPerfIcmpTotalTxGmReduct_Type = Counter32
_SfrapPerfIcmpTotalTxGmReduct_Object = MibTableColumn
sfrapPerfIcmpTotalTxGmReduct = _SfrapPerfIcmpTotalTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 6, 1, 34),
    _SfrapPerfIcmpTotalTxGmReduct_Type()
)
sfrapPerfIcmpTotalTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIcmpTotalTxGmReduct.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTable_Object = MibTable
sfrapPerfApplicationPerDlciTable = _SfrapPerfApplicationPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7)
)
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTable.setStatus("mandatory")
_SfrapPerfApplicationPerDlciEntry_Object = MibTableRow
sfrapPerfApplicationPerDlciEntry = _SfrapPerfApplicationPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1)
)
sfrapPerfApplicationPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfApplicationPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfApplicationPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciEntry.setStatus("mandatory")


class _SfrapPerfApplicationPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfApplicationPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfApplicationPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfApplicationPerDlciInterval_Object = MibTableColumn
sfrapPerfApplicationPerDlciInterval = _SfrapPerfApplicationPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 1),
    _SfrapPerfApplicationPerDlciInterval_Type()
)
sfrapPerfApplicationPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciInterval.setStatus("mandatory")
_SfrapPerfApplicationPerDlciValue_Type = Integer32
_SfrapPerfApplicationPerDlciValue_Object = MibTableColumn
sfrapPerfApplicationPerDlciValue = _SfrapPerfApplicationPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 2),
    _SfrapPerfApplicationPerDlciValue_Type()
)
sfrapPerfApplicationPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciValue.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxSnmp_Type = Counter32
_SfrapPerfApplicationPerDlciRxSnmp_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxSnmp = _SfrapPerfApplicationPerDlciRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 3),
    _SfrapPerfApplicationPerDlciRxSnmp_Type()
)
sfrapPerfApplicationPerDlciRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxSnmp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxSnmp_Type = Counter32
_SfrapPerfApplicationPerDlciTxSnmp_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxSnmp = _SfrapPerfApplicationPerDlciTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 4),
    _SfrapPerfApplicationPerDlciTxSnmp_Type()
)
sfrapPerfApplicationPerDlciTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxSnmp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxSnmpTrap_Type = Counter32
_SfrapPerfApplicationPerDlciRxSnmpTrap_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxSnmpTrap = _SfrapPerfApplicationPerDlciRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 5),
    _SfrapPerfApplicationPerDlciRxSnmpTrap_Type()
)
sfrapPerfApplicationPerDlciRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxSnmpTrap.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxSnmpTrap_Type = Counter32
_SfrapPerfApplicationPerDlciTxSnmpTrap_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxSnmpTrap = _SfrapPerfApplicationPerDlciTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 6),
    _SfrapPerfApplicationPerDlciTxSnmpTrap_Type()
)
sfrapPerfApplicationPerDlciTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxSnmpTrap.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxHttp_Type = Counter32
_SfrapPerfApplicationPerDlciRxHttp_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxHttp = _SfrapPerfApplicationPerDlciRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 7),
    _SfrapPerfApplicationPerDlciRxHttp_Type()
)
sfrapPerfApplicationPerDlciRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxHttp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxHttp_Type = Counter32
_SfrapPerfApplicationPerDlciTxHttp_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxHttp = _SfrapPerfApplicationPerDlciTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 8),
    _SfrapPerfApplicationPerDlciTxHttp_Type()
)
sfrapPerfApplicationPerDlciTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxHttp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxTelnet_Type = Counter32
_SfrapPerfApplicationPerDlciRxTelnet_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxTelnet = _SfrapPerfApplicationPerDlciRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 9),
    _SfrapPerfApplicationPerDlciRxTelnet_Type()
)
sfrapPerfApplicationPerDlciRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxTelnet.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxTelnet_Type = Counter32
_SfrapPerfApplicationPerDlciTxTelnet_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxTelnet = _SfrapPerfApplicationPerDlciTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 10),
    _SfrapPerfApplicationPerDlciTxTelnet_Type()
)
sfrapPerfApplicationPerDlciTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxTelnet.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxSmtp_Type = Counter32
_SfrapPerfApplicationPerDlciRxSmtp_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxSmtp = _SfrapPerfApplicationPerDlciRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 11),
    _SfrapPerfApplicationPerDlciRxSmtp_Type()
)
sfrapPerfApplicationPerDlciRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxSmtp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxSmtp_Type = Counter32
_SfrapPerfApplicationPerDlciTxSmtp_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxSmtp = _SfrapPerfApplicationPerDlciTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 12),
    _SfrapPerfApplicationPerDlciTxSmtp_Type()
)
sfrapPerfApplicationPerDlciTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxSmtp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxFtp_Type = Counter32
_SfrapPerfApplicationPerDlciRxFtp_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxFtp = _SfrapPerfApplicationPerDlciRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 13),
    _SfrapPerfApplicationPerDlciRxFtp_Type()
)
sfrapPerfApplicationPerDlciRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxFtp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxFtp_Type = Counter32
_SfrapPerfApplicationPerDlciTxFtp_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxFtp = _SfrapPerfApplicationPerDlciTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 14),
    _SfrapPerfApplicationPerDlciTxFtp_Type()
)
sfrapPerfApplicationPerDlciTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxFtp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxTftp_Type = Counter32
_SfrapPerfApplicationPerDlciRxTftp_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxTftp = _SfrapPerfApplicationPerDlciRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 15),
    _SfrapPerfApplicationPerDlciRxTftp_Type()
)
sfrapPerfApplicationPerDlciRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxTftp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxTftp_Type = Counter32
_SfrapPerfApplicationPerDlciTxTftp_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxTftp = _SfrapPerfApplicationPerDlciTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 16),
    _SfrapPerfApplicationPerDlciTxTftp_Type()
)
sfrapPerfApplicationPerDlciTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxTftp.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxCustom1_Type = Counter32
_SfrapPerfApplicationPerDlciRxCustom1_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxCustom1 = _SfrapPerfApplicationPerDlciRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 17),
    _SfrapPerfApplicationPerDlciRxCustom1_Type()
)
sfrapPerfApplicationPerDlciRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxCustom1.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxCustom1_Type = Counter32
_SfrapPerfApplicationPerDlciTxCustom1_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxCustom1 = _SfrapPerfApplicationPerDlciTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 18),
    _SfrapPerfApplicationPerDlciTxCustom1_Type()
)
sfrapPerfApplicationPerDlciTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxCustom1.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxCustom2_Type = Counter32
_SfrapPerfApplicationPerDlciRxCustom2_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxCustom2 = _SfrapPerfApplicationPerDlciRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 19),
    _SfrapPerfApplicationPerDlciRxCustom2_Type()
)
sfrapPerfApplicationPerDlciRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxCustom2.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxCustom2_Type = Counter32
_SfrapPerfApplicationPerDlciTxCustom2_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxCustom2 = _SfrapPerfApplicationPerDlciTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 20),
    _SfrapPerfApplicationPerDlciTxCustom2_Type()
)
sfrapPerfApplicationPerDlciTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxCustom2.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxCustom3_Type = Counter32
_SfrapPerfApplicationPerDlciRxCustom3_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxCustom3 = _SfrapPerfApplicationPerDlciRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 21),
    _SfrapPerfApplicationPerDlciRxCustom3_Type()
)
sfrapPerfApplicationPerDlciRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxCustom3.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxCustom3_Type = Counter32
_SfrapPerfApplicationPerDlciTxCustom3_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxCustom3 = _SfrapPerfApplicationPerDlciTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 22),
    _SfrapPerfApplicationPerDlciTxCustom3_Type()
)
sfrapPerfApplicationPerDlciTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxCustom3.setStatus("mandatory")
_SfrapPerfApplicationPerDlciRxCustom4_Type = Counter32
_SfrapPerfApplicationPerDlciRxCustom4_Object = MibTableColumn
sfrapPerfApplicationPerDlciRxCustom4 = _SfrapPerfApplicationPerDlciRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 23),
    _SfrapPerfApplicationPerDlciRxCustom4_Type()
)
sfrapPerfApplicationPerDlciRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciRxCustom4.setStatus("mandatory")
_SfrapPerfApplicationPerDlciTxCustom4_Type = Counter32
_SfrapPerfApplicationPerDlciTxCustom4_Object = MibTableColumn
sfrapPerfApplicationPerDlciTxCustom4 = _SfrapPerfApplicationPerDlciTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 7, 1, 24),
    _SfrapPerfApplicationPerDlciTxCustom4_Type()
)
sfrapPerfApplicationPerDlciTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationPerDlciTxCustom4.setStatus("mandatory")
_SfrapPerfApplicationTotalTable_Object = MibTable
sfrapPerfApplicationTotalTable = _SfrapPerfApplicationTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8)
)
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTable.setStatus("mandatory")
_SfrapPerfApplicationTotalEntry_Object = MibTableRow
sfrapPerfApplicationTotalEntry = _SfrapPerfApplicationTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1)
)
sfrapPerfApplicationTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfApplicationTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalEntry.setStatus("mandatory")


class _SfrapPerfApplicationTotalInterval_Type(Integer32):
    """Custom type sfrapPerfApplicationTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfApplicationTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfApplicationTotalInterval_Object = MibTableColumn
sfrapPerfApplicationTotalInterval = _SfrapPerfApplicationTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 1),
    _SfrapPerfApplicationTotalInterval_Type()
)
sfrapPerfApplicationTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalInterval.setStatus("mandatory")
_SfrapPerfApplicationTotalRxSnmp_Type = Counter32
_SfrapPerfApplicationTotalRxSnmp_Object = MibTableColumn
sfrapPerfApplicationTotalRxSnmp = _SfrapPerfApplicationTotalRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 3),
    _SfrapPerfApplicationTotalRxSnmp_Type()
)
sfrapPerfApplicationTotalRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxSnmp.setStatus("mandatory")
_SfrapPerfApplicationTotalTxSnmp_Type = Counter32
_SfrapPerfApplicationTotalTxSnmp_Object = MibTableColumn
sfrapPerfApplicationTotalTxSnmp = _SfrapPerfApplicationTotalTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 4),
    _SfrapPerfApplicationTotalTxSnmp_Type()
)
sfrapPerfApplicationTotalTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxSnmp.setStatus("mandatory")
_SfrapPerfApplicationTotalRxSnmpTrap_Type = Counter32
_SfrapPerfApplicationTotalRxSnmpTrap_Object = MibTableColumn
sfrapPerfApplicationTotalRxSnmpTrap = _SfrapPerfApplicationTotalRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 5),
    _SfrapPerfApplicationTotalRxSnmpTrap_Type()
)
sfrapPerfApplicationTotalRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxSnmpTrap.setStatus("mandatory")
_SfrapPerfApplicationTotalTxSnmpTrap_Type = Counter32
_SfrapPerfApplicationTotalTxSnmpTrap_Object = MibTableColumn
sfrapPerfApplicationTotalTxSnmpTrap = _SfrapPerfApplicationTotalTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 6),
    _SfrapPerfApplicationTotalTxSnmpTrap_Type()
)
sfrapPerfApplicationTotalTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxSnmpTrap.setStatus("mandatory")
_SfrapPerfApplicationTotalRxHttp_Type = Counter32
_SfrapPerfApplicationTotalRxHttp_Object = MibTableColumn
sfrapPerfApplicationTotalRxHttp = _SfrapPerfApplicationTotalRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 7),
    _SfrapPerfApplicationTotalRxHttp_Type()
)
sfrapPerfApplicationTotalRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxHttp.setStatus("mandatory")
_SfrapPerfApplicationTotalTxHttp_Type = Counter32
_SfrapPerfApplicationTotalTxHttp_Object = MibTableColumn
sfrapPerfApplicationTotalTxHttp = _SfrapPerfApplicationTotalTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 8),
    _SfrapPerfApplicationTotalTxHttp_Type()
)
sfrapPerfApplicationTotalTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxHttp.setStatus("mandatory")
_SfrapPerfApplicationTotalRxTelnet_Type = Counter32
_SfrapPerfApplicationTotalRxTelnet_Object = MibTableColumn
sfrapPerfApplicationTotalRxTelnet = _SfrapPerfApplicationTotalRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 9),
    _SfrapPerfApplicationTotalRxTelnet_Type()
)
sfrapPerfApplicationTotalRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxTelnet.setStatus("mandatory")
_SfrapPerfApplicationTotalTxTelnet_Type = Counter32
_SfrapPerfApplicationTotalTxTelnet_Object = MibTableColumn
sfrapPerfApplicationTotalTxTelnet = _SfrapPerfApplicationTotalTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 10),
    _SfrapPerfApplicationTotalTxTelnet_Type()
)
sfrapPerfApplicationTotalTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxTelnet.setStatus("mandatory")
_SfrapPerfApplicationTotalRxSmtp_Type = Counter32
_SfrapPerfApplicationTotalRxSmtp_Object = MibTableColumn
sfrapPerfApplicationTotalRxSmtp = _SfrapPerfApplicationTotalRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 11),
    _SfrapPerfApplicationTotalRxSmtp_Type()
)
sfrapPerfApplicationTotalRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxSmtp.setStatus("mandatory")
_SfrapPerfApplicationTotalTxSmtp_Type = Counter32
_SfrapPerfApplicationTotalTxSmtp_Object = MibTableColumn
sfrapPerfApplicationTotalTxSmtp = _SfrapPerfApplicationTotalTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 12),
    _SfrapPerfApplicationTotalTxSmtp_Type()
)
sfrapPerfApplicationTotalTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxSmtp.setStatus("mandatory")
_SfrapPerfApplicationTotalRxFtp_Type = Counter32
_SfrapPerfApplicationTotalRxFtp_Object = MibTableColumn
sfrapPerfApplicationTotalRxFtp = _SfrapPerfApplicationTotalRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 13),
    _SfrapPerfApplicationTotalRxFtp_Type()
)
sfrapPerfApplicationTotalRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxFtp.setStatus("mandatory")
_SfrapPerfApplicationTotalTxFtp_Type = Counter32
_SfrapPerfApplicationTotalTxFtp_Object = MibTableColumn
sfrapPerfApplicationTotalTxFtp = _SfrapPerfApplicationTotalTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 14),
    _SfrapPerfApplicationTotalTxFtp_Type()
)
sfrapPerfApplicationTotalTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxFtp.setStatus("mandatory")
_SfrapPerfApplicationTotalRxTftp_Type = Counter32
_SfrapPerfApplicationTotalRxTftp_Object = MibTableColumn
sfrapPerfApplicationTotalRxTftp = _SfrapPerfApplicationTotalRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 15),
    _SfrapPerfApplicationTotalRxTftp_Type()
)
sfrapPerfApplicationTotalRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxTftp.setStatus("mandatory")
_SfrapPerfApplicationTotalTxTftp_Type = Counter32
_SfrapPerfApplicationTotalTxTftp_Object = MibTableColumn
sfrapPerfApplicationTotalTxTftp = _SfrapPerfApplicationTotalTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 16),
    _SfrapPerfApplicationTotalTxTftp_Type()
)
sfrapPerfApplicationTotalTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxTftp.setStatus("mandatory")
_SfrapPerfApplicationTotalRxCustom1_Type = Counter32
_SfrapPerfApplicationTotalRxCustom1_Object = MibTableColumn
sfrapPerfApplicationTotalRxCustom1 = _SfrapPerfApplicationTotalRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 17),
    _SfrapPerfApplicationTotalRxCustom1_Type()
)
sfrapPerfApplicationTotalRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxCustom1.setStatus("mandatory")
_SfrapPerfApplicationTotalTxCustom1_Type = Counter32
_SfrapPerfApplicationTotalTxCustom1_Object = MibTableColumn
sfrapPerfApplicationTotalTxCustom1 = _SfrapPerfApplicationTotalTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 18),
    _SfrapPerfApplicationTotalTxCustom1_Type()
)
sfrapPerfApplicationTotalTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxCustom1.setStatus("mandatory")
_SfrapPerfApplicationTotalRxCustom2_Type = Counter32
_SfrapPerfApplicationTotalRxCustom2_Object = MibTableColumn
sfrapPerfApplicationTotalRxCustom2 = _SfrapPerfApplicationTotalRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 19),
    _SfrapPerfApplicationTotalRxCustom2_Type()
)
sfrapPerfApplicationTotalRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxCustom2.setStatus("mandatory")
_SfrapPerfApplicationTotalTxCustom2_Type = Counter32
_SfrapPerfApplicationTotalTxCustom2_Object = MibTableColumn
sfrapPerfApplicationTotalTxCustom2 = _SfrapPerfApplicationTotalTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 20),
    _SfrapPerfApplicationTotalTxCustom2_Type()
)
sfrapPerfApplicationTotalTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxCustom2.setStatus("mandatory")
_SfrapPerfApplicationTotalRxCustom3_Type = Counter32
_SfrapPerfApplicationTotalRxCustom3_Object = MibTableColumn
sfrapPerfApplicationTotalRxCustom3 = _SfrapPerfApplicationTotalRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 21),
    _SfrapPerfApplicationTotalRxCustom3_Type()
)
sfrapPerfApplicationTotalRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxCustom3.setStatus("mandatory")
_SfrapPerfApplicationTotalTxCustom3_Type = Counter32
_SfrapPerfApplicationTotalTxCustom3_Object = MibTableColumn
sfrapPerfApplicationTotalTxCustom3 = _SfrapPerfApplicationTotalTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 22),
    _SfrapPerfApplicationTotalTxCustom3_Type()
)
sfrapPerfApplicationTotalTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxCustom3.setStatus("mandatory")
_SfrapPerfApplicationTotalRxCustom4_Type = Counter32
_SfrapPerfApplicationTotalRxCustom4_Object = MibTableColumn
sfrapPerfApplicationTotalRxCustom4 = _SfrapPerfApplicationTotalRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 23),
    _SfrapPerfApplicationTotalRxCustom4_Type()
)
sfrapPerfApplicationTotalRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalRxCustom4.setStatus("mandatory")
_SfrapPerfApplicationTotalTxCustom4_Type = Counter32
_SfrapPerfApplicationTotalTxCustom4_Object = MibTableColumn
sfrapPerfApplicationTotalTxCustom4 = _SfrapPerfApplicationTotalTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 8, 1, 24),
    _SfrapPerfApplicationTotalTxCustom4_Type()
)
sfrapPerfApplicationTotalTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfApplicationTotalTxCustom4.setStatus("mandatory")
_SfrapPerfRoutingPerDlciTable_Object = MibTable
sfrapPerfRoutingPerDlciTable = _SfrapPerfRoutingPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9)
)
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciTable.setStatus("mandatory")
_SfrapPerfRoutingPerDlciEntry_Object = MibTableRow
sfrapPerfRoutingPerDlciEntry = _SfrapPerfRoutingPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1)
)
sfrapPerfRoutingPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfRoutingPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfRoutingPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciEntry.setStatus("mandatory")


class _SfrapPerfRoutingPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfRoutingPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfRoutingPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfRoutingPerDlciInterval_Object = MibTableColumn
sfrapPerfRoutingPerDlciInterval = _SfrapPerfRoutingPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 1),
    _SfrapPerfRoutingPerDlciInterval_Type()
)
sfrapPerfRoutingPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciInterval.setStatus("mandatory")
_SfrapPerfRoutingPerDlciValue_Type = Integer32
_SfrapPerfRoutingPerDlciValue_Object = MibTableColumn
sfrapPerfRoutingPerDlciValue = _SfrapPerfRoutingPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 2),
    _SfrapPerfRoutingPerDlciValue_Type()
)
sfrapPerfRoutingPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciValue.setStatus("mandatory")
_SfrapPerfRoutingPerDlciRxOspf_Type = Counter32
_SfrapPerfRoutingPerDlciRxOspf_Object = MibTableColumn
sfrapPerfRoutingPerDlciRxOspf = _SfrapPerfRoutingPerDlciRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 3),
    _SfrapPerfRoutingPerDlciRxOspf_Type()
)
sfrapPerfRoutingPerDlciRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciRxOspf.setStatus("mandatory")
_SfrapPerfRoutingPerDlciTxOspf_Type = Counter32
_SfrapPerfRoutingPerDlciTxOspf_Object = MibTableColumn
sfrapPerfRoutingPerDlciTxOspf = _SfrapPerfRoutingPerDlciTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 4),
    _SfrapPerfRoutingPerDlciTxOspf_Type()
)
sfrapPerfRoutingPerDlciTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciTxOspf.setStatus("mandatory")
_SfrapPerfRoutingPerDlciRxRip_Type = Counter32
_SfrapPerfRoutingPerDlciRxRip_Object = MibTableColumn
sfrapPerfRoutingPerDlciRxRip = _SfrapPerfRoutingPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 5),
    _SfrapPerfRoutingPerDlciRxRip_Type()
)
sfrapPerfRoutingPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciRxRip.setStatus("mandatory")
_SfrapPerfRoutingPerDlciTxRip_Type = Counter32
_SfrapPerfRoutingPerDlciTxRip_Object = MibTableColumn
sfrapPerfRoutingPerDlciTxRip = _SfrapPerfRoutingPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 6),
    _SfrapPerfRoutingPerDlciTxRip_Type()
)
sfrapPerfRoutingPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciTxRip.setStatus("mandatory")
_SfrapPerfRoutingPerDlciRxNetbios_Type = Counter32
_SfrapPerfRoutingPerDlciRxNetbios_Object = MibTableColumn
sfrapPerfRoutingPerDlciRxNetbios = _SfrapPerfRoutingPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 7),
    _SfrapPerfRoutingPerDlciRxNetbios_Type()
)
sfrapPerfRoutingPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciRxNetbios.setStatus("mandatory")
_SfrapPerfRoutingPerDlciTxNetbios_Type = Counter32
_SfrapPerfRoutingPerDlciTxNetbios_Object = MibTableColumn
sfrapPerfRoutingPerDlciTxNetbios = _SfrapPerfRoutingPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 9, 1, 8),
    _SfrapPerfRoutingPerDlciTxNetbios_Type()
)
sfrapPerfRoutingPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingPerDlciTxNetbios.setStatus("mandatory")
_SfrapPerfRoutingTotalTable_Object = MibTable
sfrapPerfRoutingTotalTable = _SfrapPerfRoutingTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10)
)
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalTable.setStatus("mandatory")
_SfrapPerfRoutingTotalEntry_Object = MibTableRow
sfrapPerfRoutingTotalEntry = _SfrapPerfRoutingTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1)
)
sfrapPerfRoutingTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfRoutingTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalEntry.setStatus("mandatory")


class _SfrapPerfRoutingTotalInterval_Type(Integer32):
    """Custom type sfrapPerfRoutingTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfRoutingTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfRoutingTotalInterval_Object = MibTableColumn
sfrapPerfRoutingTotalInterval = _SfrapPerfRoutingTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 1),
    _SfrapPerfRoutingTotalInterval_Type()
)
sfrapPerfRoutingTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalInterval.setStatus("mandatory")
_SfrapPerfRoutingTotalRxOspf_Type = Counter32
_SfrapPerfRoutingTotalRxOspf_Object = MibTableColumn
sfrapPerfRoutingTotalRxOspf = _SfrapPerfRoutingTotalRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 3),
    _SfrapPerfRoutingTotalRxOspf_Type()
)
sfrapPerfRoutingTotalRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalRxOspf.setStatus("mandatory")
_SfrapPerfRoutingTotalTxOspf_Type = Counter32
_SfrapPerfRoutingTotalTxOspf_Object = MibTableColumn
sfrapPerfRoutingTotalTxOspf = _SfrapPerfRoutingTotalTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 4),
    _SfrapPerfRoutingTotalTxOspf_Type()
)
sfrapPerfRoutingTotalTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalTxOspf.setStatus("mandatory")
_SfrapPerfRoutingTotalRxRip_Type = Counter32
_SfrapPerfRoutingTotalRxRip_Object = MibTableColumn
sfrapPerfRoutingTotalRxRip = _SfrapPerfRoutingTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 5),
    _SfrapPerfRoutingTotalRxRip_Type()
)
sfrapPerfRoutingTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalRxRip.setStatus("mandatory")
_SfrapPerfRoutingTotalTxRip_Type = Counter32
_SfrapPerfRoutingTotalTxRip_Object = MibTableColumn
sfrapPerfRoutingTotalTxRip = _SfrapPerfRoutingTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 6),
    _SfrapPerfRoutingTotalTxRip_Type()
)
sfrapPerfRoutingTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalTxRip.setStatus("mandatory")
_SfrapPerfRoutingTotalRxNetbios_Type = Counter32
_SfrapPerfRoutingTotalRxNetbios_Object = MibTableColumn
sfrapPerfRoutingTotalRxNetbios = _SfrapPerfRoutingTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 7),
    _SfrapPerfRoutingTotalRxNetbios_Type()
)
sfrapPerfRoutingTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalRxNetbios.setStatus("mandatory")
_SfrapPerfRoutingTotalTxNetbios_Type = Counter32
_SfrapPerfRoutingTotalTxNetbios_Object = MibTableColumn
sfrapPerfRoutingTotalTxNetbios = _SfrapPerfRoutingTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 10, 1, 8),
    _SfrapPerfRoutingTotalTxNetbios_Type()
)
sfrapPerfRoutingTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfRoutingTotalTxNetbios.setStatus("mandatory")
_SfrapPerfIpxPerDlciTable_Object = MibTable
sfrapPerfIpxPerDlciTable = _SfrapPerfIpxPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11)
)
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTable.setStatus("mandatory")
_SfrapPerfIpxPerDlciEntry_Object = MibTableRow
sfrapPerfIpxPerDlciEntry = _SfrapPerfIpxPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1)
)
sfrapPerfIpxPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIpxPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfIpxPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciEntry.setStatus("mandatory")


class _SfrapPerfIpxPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfIpxPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIpxPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfIpxPerDlciInterval_Object = MibTableColumn
sfrapPerfIpxPerDlciInterval = _SfrapPerfIpxPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 1),
    _SfrapPerfIpxPerDlciInterval_Type()
)
sfrapPerfIpxPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciInterval.setStatus("mandatory")
_SfrapPerfIpxPerDlciValue_Type = Integer32
_SfrapPerfIpxPerDlciValue_Object = MibTableColumn
sfrapPerfIpxPerDlciValue = _SfrapPerfIpxPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 2),
    _SfrapPerfIpxPerDlciValue_Type()
)
sfrapPerfIpxPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciValue.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxTotal_Type = Counter32
_SfrapPerfIpxPerDlciRxTotal_Object = MibTableColumn
sfrapPerfIpxPerDlciRxTotal = _SfrapPerfIpxPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 3),
    _SfrapPerfIpxPerDlciRxTotal_Type()
)
sfrapPerfIpxPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxTotal_Type = Counter32
_SfrapPerfIpxPerDlciTxTotal_Object = MibTableColumn
sfrapPerfIpxPerDlciTxTotal = _SfrapPerfIpxPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 4),
    _SfrapPerfIpxPerDlciTxTotal_Type()
)
sfrapPerfIpxPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxSpx_Type = Counter32
_SfrapPerfIpxPerDlciRxSpx_Object = MibTableColumn
sfrapPerfIpxPerDlciRxSpx = _SfrapPerfIpxPerDlciRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 5),
    _SfrapPerfIpxPerDlciRxSpx_Type()
)
sfrapPerfIpxPerDlciRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxSpx.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxSpx_Type = Counter32
_SfrapPerfIpxPerDlciTxSpx_Object = MibTableColumn
sfrapPerfIpxPerDlciTxSpx = _SfrapPerfIpxPerDlciTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 6),
    _SfrapPerfIpxPerDlciTxSpx_Type()
)
sfrapPerfIpxPerDlciTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxSpx.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxNcp_Type = Counter32
_SfrapPerfIpxPerDlciRxNcp_Object = MibTableColumn
sfrapPerfIpxPerDlciRxNcp = _SfrapPerfIpxPerDlciRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 7),
    _SfrapPerfIpxPerDlciRxNcp_Type()
)
sfrapPerfIpxPerDlciRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxNcp.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxNcp_Type = Counter32
_SfrapPerfIpxPerDlciTxNcp_Object = MibTableColumn
sfrapPerfIpxPerDlciTxNcp = _SfrapPerfIpxPerDlciTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 8),
    _SfrapPerfIpxPerDlciTxNcp_Type()
)
sfrapPerfIpxPerDlciTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxNcp.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxSap_Type = Counter32
_SfrapPerfIpxPerDlciRxSap_Object = MibTableColumn
sfrapPerfIpxPerDlciRxSap = _SfrapPerfIpxPerDlciRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 9),
    _SfrapPerfIpxPerDlciRxSap_Type()
)
sfrapPerfIpxPerDlciRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxSap.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxSap_Type = Counter32
_SfrapPerfIpxPerDlciTxSap_Object = MibTableColumn
sfrapPerfIpxPerDlciTxSap = _SfrapPerfIpxPerDlciTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 10),
    _SfrapPerfIpxPerDlciTxSap_Type()
)
sfrapPerfIpxPerDlciTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxSap.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxRip_Type = Counter32
_SfrapPerfIpxPerDlciRxRip_Object = MibTableColumn
sfrapPerfIpxPerDlciRxRip = _SfrapPerfIpxPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 11),
    _SfrapPerfIpxPerDlciRxRip_Type()
)
sfrapPerfIpxPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxRip.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxRip_Type = Counter32
_SfrapPerfIpxPerDlciTxRip_Object = MibTableColumn
sfrapPerfIpxPerDlciTxRip = _SfrapPerfIpxPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 12),
    _SfrapPerfIpxPerDlciTxRip_Type()
)
sfrapPerfIpxPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxRip.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxNetbios_Type = Counter32
_SfrapPerfIpxPerDlciRxNetbios_Object = MibTableColumn
sfrapPerfIpxPerDlciRxNetbios = _SfrapPerfIpxPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 13),
    _SfrapPerfIpxPerDlciRxNetbios_Type()
)
sfrapPerfIpxPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxNetbios.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxNetbios_Type = Counter32
_SfrapPerfIpxPerDlciTxNetbios_Object = MibTableColumn
sfrapPerfIpxPerDlciTxNetbios = _SfrapPerfIpxPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 14),
    _SfrapPerfIpxPerDlciTxNetbios_Type()
)
sfrapPerfIpxPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxNetbios.setStatus("mandatory")
_SfrapPerfIpxPerDlciRxOther_Type = Counter32
_SfrapPerfIpxPerDlciRxOther_Object = MibTableColumn
sfrapPerfIpxPerDlciRxOther = _SfrapPerfIpxPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 15),
    _SfrapPerfIpxPerDlciRxOther_Type()
)
sfrapPerfIpxPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciRxOther.setStatus("mandatory")
_SfrapPerfIpxPerDlciTxOther_Type = Counter32
_SfrapPerfIpxPerDlciTxOther_Object = MibTableColumn
sfrapPerfIpxPerDlciTxOther = _SfrapPerfIpxPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 11, 1, 16),
    _SfrapPerfIpxPerDlciTxOther_Type()
)
sfrapPerfIpxPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxPerDlciTxOther.setStatus("mandatory")
_SfrapPerfIpxTotalTable_Object = MibTable
sfrapPerfIpxTotalTable = _SfrapPerfIpxTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12)
)
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTable.setStatus("mandatory")
_SfrapPerfIpxTotalEntry_Object = MibTableRow
sfrapPerfIpxTotalEntry = _SfrapPerfIpxTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1)
)
sfrapPerfIpxTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfIpxTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalEntry.setStatus("mandatory")


class _SfrapPerfIpxTotalInterval_Type(Integer32):
    """Custom type sfrapPerfIpxTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfIpxTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfIpxTotalInterval_Object = MibTableColumn
sfrapPerfIpxTotalInterval = _SfrapPerfIpxTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 1),
    _SfrapPerfIpxTotalInterval_Type()
)
sfrapPerfIpxTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalInterval.setStatus("mandatory")
_SfrapPerfIpxTotalRxTotal_Type = Counter32
_SfrapPerfIpxTotalRxTotal_Object = MibTableColumn
sfrapPerfIpxTotalRxTotal = _SfrapPerfIpxTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 3),
    _SfrapPerfIpxTotalRxTotal_Type()
)
sfrapPerfIpxTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxTotal.setStatus("mandatory")
_SfrapPerfIpxTotalTxTotal_Type = Counter32
_SfrapPerfIpxTotalTxTotal_Object = MibTableColumn
sfrapPerfIpxTotalTxTotal = _SfrapPerfIpxTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 4),
    _SfrapPerfIpxTotalTxTotal_Type()
)
sfrapPerfIpxTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxTotal.setStatus("mandatory")
_SfrapPerfIpxTotalRxSpx_Type = Counter32
_SfrapPerfIpxTotalRxSpx_Object = MibTableColumn
sfrapPerfIpxTotalRxSpx = _SfrapPerfIpxTotalRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 5),
    _SfrapPerfIpxTotalRxSpx_Type()
)
sfrapPerfIpxTotalRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxSpx.setStatus("mandatory")
_SfrapPerfIpxTotalTxSpx_Type = Counter32
_SfrapPerfIpxTotalTxSpx_Object = MibTableColumn
sfrapPerfIpxTotalTxSpx = _SfrapPerfIpxTotalTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 6),
    _SfrapPerfIpxTotalTxSpx_Type()
)
sfrapPerfIpxTotalTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxSpx.setStatus("mandatory")
_SfrapPerfIpxTotalRxNcp_Type = Counter32
_SfrapPerfIpxTotalRxNcp_Object = MibTableColumn
sfrapPerfIpxTotalRxNcp = _SfrapPerfIpxTotalRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 7),
    _SfrapPerfIpxTotalRxNcp_Type()
)
sfrapPerfIpxTotalRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxNcp.setStatus("mandatory")
_SfrapPerfIpxTotalTxNcp_Type = Counter32
_SfrapPerfIpxTotalTxNcp_Object = MibTableColumn
sfrapPerfIpxTotalTxNcp = _SfrapPerfIpxTotalTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 8),
    _SfrapPerfIpxTotalTxNcp_Type()
)
sfrapPerfIpxTotalTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxNcp.setStatus("mandatory")
_SfrapPerfIpxTotalRxSap_Type = Counter32
_SfrapPerfIpxTotalRxSap_Object = MibTableColumn
sfrapPerfIpxTotalRxSap = _SfrapPerfIpxTotalRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 9),
    _SfrapPerfIpxTotalRxSap_Type()
)
sfrapPerfIpxTotalRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxSap.setStatus("mandatory")
_SfrapPerfIpxTotalTxSap_Type = Counter32
_SfrapPerfIpxTotalTxSap_Object = MibTableColumn
sfrapPerfIpxTotalTxSap = _SfrapPerfIpxTotalTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 10),
    _SfrapPerfIpxTotalTxSap_Type()
)
sfrapPerfIpxTotalTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxSap.setStatus("mandatory")
_SfrapPerfIpxTotalRxRip_Type = Counter32
_SfrapPerfIpxTotalRxRip_Object = MibTableColumn
sfrapPerfIpxTotalRxRip = _SfrapPerfIpxTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 11),
    _SfrapPerfIpxTotalRxRip_Type()
)
sfrapPerfIpxTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxRip.setStatus("mandatory")
_SfrapPerfIpxTotalTxRip_Type = Counter32
_SfrapPerfIpxTotalTxRip_Object = MibTableColumn
sfrapPerfIpxTotalTxRip = _SfrapPerfIpxTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 12),
    _SfrapPerfIpxTotalTxRip_Type()
)
sfrapPerfIpxTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxRip.setStatus("mandatory")
_SfrapPerfIpxTotalRxNetbios_Type = Counter32
_SfrapPerfIpxTotalRxNetbios_Object = MibTableColumn
sfrapPerfIpxTotalRxNetbios = _SfrapPerfIpxTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 13),
    _SfrapPerfIpxTotalRxNetbios_Type()
)
sfrapPerfIpxTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxNetbios.setStatus("mandatory")
_SfrapPerfIpxTotalTxNetbios_Type = Counter32
_SfrapPerfIpxTotalTxNetbios_Object = MibTableColumn
sfrapPerfIpxTotalTxNetbios = _SfrapPerfIpxTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 14),
    _SfrapPerfIpxTotalTxNetbios_Type()
)
sfrapPerfIpxTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxNetbios.setStatus("mandatory")
_SfrapPerfIpxTotalRxOther_Type = Counter32
_SfrapPerfIpxTotalRxOther_Object = MibTableColumn
sfrapPerfIpxTotalRxOther = _SfrapPerfIpxTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 15),
    _SfrapPerfIpxTotalRxOther_Type()
)
sfrapPerfIpxTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalRxOther.setStatus("mandatory")
_SfrapPerfIpxTotalTxOther_Type = Counter32
_SfrapPerfIpxTotalTxOther_Object = MibTableColumn
sfrapPerfIpxTotalTxOther = _SfrapPerfIpxTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 12, 1, 16),
    _SfrapPerfIpxTotalTxOther_Type()
)
sfrapPerfIpxTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfIpxTotalTxOther.setStatus("mandatory")
_SfrapPerfSnaPerDlciTable_Object = MibTable
sfrapPerfSnaPerDlciTable = _SfrapPerfSnaPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13)
)
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTable.setStatus("mandatory")
_SfrapPerfSnaPerDlciEntry_Object = MibTableRow
sfrapPerfSnaPerDlciEntry = _SfrapPerfSnaPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1)
)
sfrapPerfSnaPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfSnaPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfSnaPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciEntry.setStatus("mandatory")


class _SfrapPerfSnaPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfSnaPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfSnaPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfSnaPerDlciInterval_Object = MibTableColumn
sfrapPerfSnaPerDlciInterval = _SfrapPerfSnaPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 1),
    _SfrapPerfSnaPerDlciInterval_Type()
)
sfrapPerfSnaPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciInterval.setStatus("mandatory")
_SfrapPerfSnaPerDlciValue_Type = Integer32
_SfrapPerfSnaPerDlciValue_Object = MibTableColumn
sfrapPerfSnaPerDlciValue = _SfrapPerfSnaPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 2),
    _SfrapPerfSnaPerDlciValue_Type()
)
sfrapPerfSnaPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciValue.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxTotal_Type = Counter32
_SfrapPerfSnaPerDlciRxTotal_Object = MibTableColumn
sfrapPerfSnaPerDlciRxTotal = _SfrapPerfSnaPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 3),
    _SfrapPerfSnaPerDlciRxTotal_Type()
)
sfrapPerfSnaPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxTotal_Type = Counter32
_SfrapPerfSnaPerDlciTxTotal_Object = MibTableColumn
sfrapPerfSnaPerDlciTxTotal = _SfrapPerfSnaPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 4),
    _SfrapPerfSnaPerDlciTxTotal_Type()
)
sfrapPerfSnaPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxSubarea_Type = Counter32
_SfrapPerfSnaPerDlciRxSubarea_Object = MibTableColumn
sfrapPerfSnaPerDlciRxSubarea = _SfrapPerfSnaPerDlciRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 5),
    _SfrapPerfSnaPerDlciRxSubarea_Type()
)
sfrapPerfSnaPerDlciRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxSubarea.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxSubarea_Type = Counter32
_SfrapPerfSnaPerDlciTxSubarea_Object = MibTableColumn
sfrapPerfSnaPerDlciTxSubarea = _SfrapPerfSnaPerDlciTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 6),
    _SfrapPerfSnaPerDlciTxSubarea_Type()
)
sfrapPerfSnaPerDlciTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxSubarea.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxPeriph_Type = Counter32
_SfrapPerfSnaPerDlciRxPeriph_Object = MibTableColumn
sfrapPerfSnaPerDlciRxPeriph = _SfrapPerfSnaPerDlciRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 7),
    _SfrapPerfSnaPerDlciRxPeriph_Type()
)
sfrapPerfSnaPerDlciRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxPeriph.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxPeriph_Type = Counter32
_SfrapPerfSnaPerDlciTxPeriph_Object = MibTableColumn
sfrapPerfSnaPerDlciTxPeriph = _SfrapPerfSnaPerDlciTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 8),
    _SfrapPerfSnaPerDlciTxPeriph_Type()
)
sfrapPerfSnaPerDlciTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxPeriph.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxAppn_Type = Counter32
_SfrapPerfSnaPerDlciRxAppn_Object = MibTableColumn
sfrapPerfSnaPerDlciRxAppn = _SfrapPerfSnaPerDlciRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 9),
    _SfrapPerfSnaPerDlciRxAppn_Type()
)
sfrapPerfSnaPerDlciRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxAppn.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxAppn_Type = Counter32
_SfrapPerfSnaPerDlciTxAppn_Object = MibTableColumn
sfrapPerfSnaPerDlciTxAppn = _SfrapPerfSnaPerDlciTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 10),
    _SfrapPerfSnaPerDlciTxAppn_Type()
)
sfrapPerfSnaPerDlciTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxAppn.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxNetbios_Type = Counter32
_SfrapPerfSnaPerDlciRxNetbios_Object = MibTableColumn
sfrapPerfSnaPerDlciRxNetbios = _SfrapPerfSnaPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 11),
    _SfrapPerfSnaPerDlciRxNetbios_Type()
)
sfrapPerfSnaPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxNetbios.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxNetbios_Type = Counter32
_SfrapPerfSnaPerDlciTxNetbios_Object = MibTableColumn
sfrapPerfSnaPerDlciTxNetbios = _SfrapPerfSnaPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 12),
    _SfrapPerfSnaPerDlciTxNetbios_Type()
)
sfrapPerfSnaPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxNetbios.setStatus("mandatory")
_SfrapPerfSnaPerDlciRxOther_Type = Counter32
_SfrapPerfSnaPerDlciRxOther_Object = MibTableColumn
sfrapPerfSnaPerDlciRxOther = _SfrapPerfSnaPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 13),
    _SfrapPerfSnaPerDlciRxOther_Type()
)
sfrapPerfSnaPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciRxOther.setStatus("mandatory")
_SfrapPerfSnaPerDlciTxOther_Type = Counter32
_SfrapPerfSnaPerDlciTxOther_Object = MibTableColumn
sfrapPerfSnaPerDlciTxOther = _SfrapPerfSnaPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 13, 1, 14),
    _SfrapPerfSnaPerDlciTxOther_Type()
)
sfrapPerfSnaPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaPerDlciTxOther.setStatus("mandatory")
_SfrapPerfSnaTotalTable_Object = MibTable
sfrapPerfSnaTotalTable = _SfrapPerfSnaTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14)
)
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTable.setStatus("mandatory")
_SfrapPerfSnaTotalEntry_Object = MibTableRow
sfrapPerfSnaTotalEntry = _SfrapPerfSnaTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1)
)
sfrapPerfSnaTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfSnaTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalEntry.setStatus("mandatory")


class _SfrapPerfSnaTotalInterval_Type(Integer32):
    """Custom type sfrapPerfSnaTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfSnaTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfSnaTotalInterval_Object = MibTableColumn
sfrapPerfSnaTotalInterval = _SfrapPerfSnaTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 1),
    _SfrapPerfSnaTotalInterval_Type()
)
sfrapPerfSnaTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalInterval.setStatus("mandatory")
_SfrapPerfSnaTotalRxTotal_Type = Counter32
_SfrapPerfSnaTotalRxTotal_Object = MibTableColumn
sfrapPerfSnaTotalRxTotal = _SfrapPerfSnaTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 3),
    _SfrapPerfSnaTotalRxTotal_Type()
)
sfrapPerfSnaTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxTotal.setStatus("mandatory")
_SfrapPerfSnaTotalTxTotal_Type = Counter32
_SfrapPerfSnaTotalTxTotal_Object = MibTableColumn
sfrapPerfSnaTotalTxTotal = _SfrapPerfSnaTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 4),
    _SfrapPerfSnaTotalTxTotal_Type()
)
sfrapPerfSnaTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxTotal.setStatus("mandatory")
_SfrapPerfSnaTotalRxSubarea_Type = Counter32
_SfrapPerfSnaTotalRxSubarea_Object = MibTableColumn
sfrapPerfSnaTotalRxSubarea = _SfrapPerfSnaTotalRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 5),
    _SfrapPerfSnaTotalRxSubarea_Type()
)
sfrapPerfSnaTotalRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxSubarea.setStatus("mandatory")
_SfrapPerfSnaTotalTxSubarea_Type = Counter32
_SfrapPerfSnaTotalTxSubarea_Object = MibTableColumn
sfrapPerfSnaTotalTxSubarea = _SfrapPerfSnaTotalTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 6),
    _SfrapPerfSnaTotalTxSubarea_Type()
)
sfrapPerfSnaTotalTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxSubarea.setStatus("mandatory")
_SfrapPerfSnaTotalRxPeriph_Type = Counter32
_SfrapPerfSnaTotalRxPeriph_Object = MibTableColumn
sfrapPerfSnaTotalRxPeriph = _SfrapPerfSnaTotalRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 7),
    _SfrapPerfSnaTotalRxPeriph_Type()
)
sfrapPerfSnaTotalRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxPeriph.setStatus("mandatory")
_SfrapPerfSnaTotalTxPeriph_Type = Counter32
_SfrapPerfSnaTotalTxPeriph_Object = MibTableColumn
sfrapPerfSnaTotalTxPeriph = _SfrapPerfSnaTotalTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 8),
    _SfrapPerfSnaTotalTxPeriph_Type()
)
sfrapPerfSnaTotalTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxPeriph.setStatus("mandatory")
_SfrapPerfSnaTotalRxAppn_Type = Counter32
_SfrapPerfSnaTotalRxAppn_Object = MibTableColumn
sfrapPerfSnaTotalRxAppn = _SfrapPerfSnaTotalRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 9),
    _SfrapPerfSnaTotalRxAppn_Type()
)
sfrapPerfSnaTotalRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxAppn.setStatus("mandatory")
_SfrapPerfSnaTotalTxAppn_Type = Counter32
_SfrapPerfSnaTotalTxAppn_Object = MibTableColumn
sfrapPerfSnaTotalTxAppn = _SfrapPerfSnaTotalTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 10),
    _SfrapPerfSnaTotalTxAppn_Type()
)
sfrapPerfSnaTotalTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxAppn.setStatus("mandatory")
_SfrapPerfSnaTotalRxNetbios_Type = Counter32
_SfrapPerfSnaTotalRxNetbios_Object = MibTableColumn
sfrapPerfSnaTotalRxNetbios = _SfrapPerfSnaTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 11),
    _SfrapPerfSnaTotalRxNetbios_Type()
)
sfrapPerfSnaTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxNetbios.setStatus("mandatory")
_SfrapPerfSnaTotalTxNetbios_Type = Counter32
_SfrapPerfSnaTotalTxNetbios_Object = MibTableColumn
sfrapPerfSnaTotalTxNetbios = _SfrapPerfSnaTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 12),
    _SfrapPerfSnaTotalTxNetbios_Type()
)
sfrapPerfSnaTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxNetbios.setStatus("mandatory")
_SfrapPerfSnaTotalRxOther_Type = Counter32
_SfrapPerfSnaTotalRxOther_Object = MibTableColumn
sfrapPerfSnaTotalRxOther = _SfrapPerfSnaTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 13),
    _SfrapPerfSnaTotalRxOther_Type()
)
sfrapPerfSnaTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalRxOther.setStatus("mandatory")
_SfrapPerfSnaTotalTxOther_Type = Counter32
_SfrapPerfSnaTotalTxOther_Object = MibTableColumn
sfrapPerfSnaTotalTxOther = _SfrapPerfSnaTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 14, 1, 14),
    _SfrapPerfSnaTotalTxOther_Type()
)
sfrapPerfSnaTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfSnaTotalTxOther.setStatus("mandatory")
_SfrapPerfArpPerDlciTable_Object = MibTable
sfrapPerfArpPerDlciTable = _SfrapPerfArpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15)
)
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTable.setStatus("mandatory")
_SfrapPerfArpPerDlciEntry_Object = MibTableRow
sfrapPerfArpPerDlciEntry = _SfrapPerfArpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1)
)
sfrapPerfArpPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfArpPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfArpPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciEntry.setStatus("mandatory")


class _SfrapPerfArpPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfArpPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfArpPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfArpPerDlciInterval_Object = MibTableColumn
sfrapPerfArpPerDlciInterval = _SfrapPerfArpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 1),
    _SfrapPerfArpPerDlciInterval_Type()
)
sfrapPerfArpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciInterval.setStatus("mandatory")
_SfrapPerfArpPerDlciValue_Type = Integer32
_SfrapPerfArpPerDlciValue_Object = MibTableColumn
sfrapPerfArpPerDlciValue = _SfrapPerfArpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 2),
    _SfrapPerfArpPerDlciValue_Type()
)
sfrapPerfArpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciValue.setStatus("mandatory")
_SfrapPerfArpPerDlciRxTotal_Type = Counter32
_SfrapPerfArpPerDlciRxTotal_Object = MibTableColumn
sfrapPerfArpPerDlciRxTotal = _SfrapPerfArpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 3),
    _SfrapPerfArpPerDlciRxTotal_Type()
)
sfrapPerfArpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxTotal.setStatus("mandatory")
_SfrapPerfArpPerDlciTxTotal_Type = Counter32
_SfrapPerfArpPerDlciTxTotal_Object = MibTableColumn
sfrapPerfArpPerDlciTxTotal = _SfrapPerfArpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 4),
    _SfrapPerfArpPerDlciTxTotal_Type()
)
sfrapPerfArpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxTotal.setStatus("mandatory")
_SfrapPerfArpPerDlciRxArpReq_Type = Counter32
_SfrapPerfArpPerDlciRxArpReq_Object = MibTableColumn
sfrapPerfArpPerDlciRxArpReq = _SfrapPerfArpPerDlciRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 5),
    _SfrapPerfArpPerDlciRxArpReq_Type()
)
sfrapPerfArpPerDlciRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxArpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciTxArpReq_Type = Counter32
_SfrapPerfArpPerDlciTxArpReq_Object = MibTableColumn
sfrapPerfArpPerDlciTxArpReq = _SfrapPerfArpPerDlciTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 6),
    _SfrapPerfArpPerDlciTxArpReq_Type()
)
sfrapPerfArpPerDlciTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxArpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciRxArpRep_Type = Counter32
_SfrapPerfArpPerDlciRxArpRep_Object = MibTableColumn
sfrapPerfArpPerDlciRxArpRep = _SfrapPerfArpPerDlciRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 7),
    _SfrapPerfArpPerDlciRxArpRep_Type()
)
sfrapPerfArpPerDlciRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxArpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciTxArpRep_Type = Counter32
_SfrapPerfArpPerDlciTxArpRep_Object = MibTableColumn
sfrapPerfArpPerDlciTxArpRep = _SfrapPerfArpPerDlciTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 8),
    _SfrapPerfArpPerDlciTxArpRep_Type()
)
sfrapPerfArpPerDlciTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxArpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciRxRarpReq_Type = Counter32
_SfrapPerfArpPerDlciRxRarpReq_Object = MibTableColumn
sfrapPerfArpPerDlciRxRarpReq = _SfrapPerfArpPerDlciRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 9),
    _SfrapPerfArpPerDlciRxRarpReq_Type()
)
sfrapPerfArpPerDlciRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxRarpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciTxRarpReq_Type = Counter32
_SfrapPerfArpPerDlciTxRarpReq_Object = MibTableColumn
sfrapPerfArpPerDlciTxRarpReq = _SfrapPerfArpPerDlciTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 10),
    _SfrapPerfArpPerDlciTxRarpReq_Type()
)
sfrapPerfArpPerDlciTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxRarpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciRxRarpRep_Type = Counter32
_SfrapPerfArpPerDlciRxRarpRep_Object = MibTableColumn
sfrapPerfArpPerDlciRxRarpRep = _SfrapPerfArpPerDlciRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 11),
    _SfrapPerfArpPerDlciRxRarpRep_Type()
)
sfrapPerfArpPerDlciRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxRarpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciTxRarpRep_Type = Counter32
_SfrapPerfArpPerDlciTxRarpRep_Object = MibTableColumn
sfrapPerfArpPerDlciTxRarpRep = _SfrapPerfArpPerDlciTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 12),
    _SfrapPerfArpPerDlciTxRarpRep_Type()
)
sfrapPerfArpPerDlciTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxRarpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciRxInarpReq_Type = Counter32
_SfrapPerfArpPerDlciRxInarpReq_Object = MibTableColumn
sfrapPerfArpPerDlciRxInarpReq = _SfrapPerfArpPerDlciRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 13),
    _SfrapPerfArpPerDlciRxInarpReq_Type()
)
sfrapPerfArpPerDlciRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxInarpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciTxInarpReq_Type = Counter32
_SfrapPerfArpPerDlciTxInarpReq_Object = MibTableColumn
sfrapPerfArpPerDlciTxInarpReq = _SfrapPerfArpPerDlciTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 14),
    _SfrapPerfArpPerDlciTxInarpReq_Type()
)
sfrapPerfArpPerDlciTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxInarpReq.setStatus("mandatory")
_SfrapPerfArpPerDlciRxInarpRep_Type = Counter32
_SfrapPerfArpPerDlciRxInarpRep_Object = MibTableColumn
sfrapPerfArpPerDlciRxInarpRep = _SfrapPerfArpPerDlciRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 15),
    _SfrapPerfArpPerDlciRxInarpRep_Type()
)
sfrapPerfArpPerDlciRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxInarpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciTxInarpRep_Type = Counter32
_SfrapPerfArpPerDlciTxInarpRep_Object = MibTableColumn
sfrapPerfArpPerDlciTxInarpRep = _SfrapPerfArpPerDlciTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 16),
    _SfrapPerfArpPerDlciTxInarpRep_Type()
)
sfrapPerfArpPerDlciTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxInarpRep.setStatus("mandatory")
_SfrapPerfArpPerDlciRxOther_Type = Counter32
_SfrapPerfArpPerDlciRxOther_Object = MibTableColumn
sfrapPerfArpPerDlciRxOther = _SfrapPerfArpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 17),
    _SfrapPerfArpPerDlciRxOther_Type()
)
sfrapPerfArpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciRxOther.setStatus("mandatory")
_SfrapPerfArpPerDlciTxOther_Type = Counter32
_SfrapPerfArpPerDlciTxOther_Object = MibTableColumn
sfrapPerfArpPerDlciTxOther = _SfrapPerfArpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 15, 1, 18),
    _SfrapPerfArpPerDlciTxOther_Type()
)
sfrapPerfArpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpPerDlciTxOther.setStatus("mandatory")
_SfrapPerfArpTotalTable_Object = MibTable
sfrapPerfArpTotalTable = _SfrapPerfArpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16)
)
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTable.setStatus("mandatory")
_SfrapPerfArpTotalEntry_Object = MibTableRow
sfrapPerfArpTotalEntry = _SfrapPerfArpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1)
)
sfrapPerfArpTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfArpTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfArpTotalEntry.setStatus("mandatory")


class _SfrapPerfArpTotalInterval_Type(Integer32):
    """Custom type sfrapPerfArpTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfArpTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfArpTotalInterval_Object = MibTableColumn
sfrapPerfArpTotalInterval = _SfrapPerfArpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 1),
    _SfrapPerfArpTotalInterval_Type()
)
sfrapPerfArpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalInterval.setStatus("mandatory")
_SfrapPerfArpTotalRxTotal_Type = Counter32
_SfrapPerfArpTotalRxTotal_Object = MibTableColumn
sfrapPerfArpTotalRxTotal = _SfrapPerfArpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 3),
    _SfrapPerfArpTotalRxTotal_Type()
)
sfrapPerfArpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxTotal.setStatus("mandatory")
_SfrapPerfArpTotalTxTotal_Type = Counter32
_SfrapPerfArpTotalTxTotal_Object = MibTableColumn
sfrapPerfArpTotalTxTotal = _SfrapPerfArpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 4),
    _SfrapPerfArpTotalTxTotal_Type()
)
sfrapPerfArpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxTotal.setStatus("mandatory")
_SfrapPerfArpTotalRxArpReq_Type = Counter32
_SfrapPerfArpTotalRxArpReq_Object = MibTableColumn
sfrapPerfArpTotalRxArpReq = _SfrapPerfArpTotalRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 5),
    _SfrapPerfArpTotalRxArpReq_Type()
)
sfrapPerfArpTotalRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxArpReq.setStatus("mandatory")
_SfrapPerfArpTotalTxArpReq_Type = Counter32
_SfrapPerfArpTotalTxArpReq_Object = MibTableColumn
sfrapPerfArpTotalTxArpReq = _SfrapPerfArpTotalTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 6),
    _SfrapPerfArpTotalTxArpReq_Type()
)
sfrapPerfArpTotalTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxArpReq.setStatus("mandatory")
_SfrapPerfArpTotalRxArpRep_Type = Counter32
_SfrapPerfArpTotalRxArpRep_Object = MibTableColumn
sfrapPerfArpTotalRxArpRep = _SfrapPerfArpTotalRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 7),
    _SfrapPerfArpTotalRxArpRep_Type()
)
sfrapPerfArpTotalRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxArpRep.setStatus("mandatory")
_SfrapPerfArpTotalTxArpRep_Type = Counter32
_SfrapPerfArpTotalTxArpRep_Object = MibTableColumn
sfrapPerfArpTotalTxArpRep = _SfrapPerfArpTotalTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 8),
    _SfrapPerfArpTotalTxArpRep_Type()
)
sfrapPerfArpTotalTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxArpRep.setStatus("mandatory")
_SfrapPerfArpTotalRxRarpReq_Type = Counter32
_SfrapPerfArpTotalRxRarpReq_Object = MibTableColumn
sfrapPerfArpTotalRxRarpReq = _SfrapPerfArpTotalRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 9),
    _SfrapPerfArpTotalRxRarpReq_Type()
)
sfrapPerfArpTotalRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxRarpReq.setStatus("mandatory")
_SfrapPerfArpTotalTxRarpReq_Type = Counter32
_SfrapPerfArpTotalTxRarpReq_Object = MibTableColumn
sfrapPerfArpTotalTxRarpReq = _SfrapPerfArpTotalTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 10),
    _SfrapPerfArpTotalTxRarpReq_Type()
)
sfrapPerfArpTotalTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxRarpReq.setStatus("mandatory")
_SfrapPerfArpTotalRxRarpRep_Type = Counter32
_SfrapPerfArpTotalRxRarpRep_Object = MibTableColumn
sfrapPerfArpTotalRxRarpRep = _SfrapPerfArpTotalRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 11),
    _SfrapPerfArpTotalRxRarpRep_Type()
)
sfrapPerfArpTotalRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxRarpRep.setStatus("mandatory")
_SfrapPerfArpTotalTxRarpRep_Type = Counter32
_SfrapPerfArpTotalTxRarpRep_Object = MibTableColumn
sfrapPerfArpTotalTxRarpRep = _SfrapPerfArpTotalTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 12),
    _SfrapPerfArpTotalTxRarpRep_Type()
)
sfrapPerfArpTotalTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxRarpRep.setStatus("mandatory")
_SfrapPerfArpTotalRxInarpReq_Type = Counter32
_SfrapPerfArpTotalRxInarpReq_Object = MibTableColumn
sfrapPerfArpTotalRxInarpReq = _SfrapPerfArpTotalRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 13),
    _SfrapPerfArpTotalRxInarpReq_Type()
)
sfrapPerfArpTotalRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxInarpReq.setStatus("mandatory")
_SfrapPerfArpTotalTxInarpReq_Type = Counter32
_SfrapPerfArpTotalTxInarpReq_Object = MibTableColumn
sfrapPerfArpTotalTxInarpReq = _SfrapPerfArpTotalTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 14),
    _SfrapPerfArpTotalTxInarpReq_Type()
)
sfrapPerfArpTotalTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxInarpReq.setStatus("mandatory")
_SfrapPerfArpTotalRxInarpRep_Type = Counter32
_SfrapPerfArpTotalRxInarpRep_Object = MibTableColumn
sfrapPerfArpTotalRxInarpRep = _SfrapPerfArpTotalRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 15),
    _SfrapPerfArpTotalRxInarpRep_Type()
)
sfrapPerfArpTotalRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxInarpRep.setStatus("mandatory")
_SfrapPerfArpTotalTxInarpRep_Type = Counter32
_SfrapPerfArpTotalTxInarpRep_Object = MibTableColumn
sfrapPerfArpTotalTxInarpRep = _SfrapPerfArpTotalTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 16),
    _SfrapPerfArpTotalTxInarpRep_Type()
)
sfrapPerfArpTotalTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxInarpRep.setStatus("mandatory")
_SfrapPerfArpTotalRxOther_Type = Counter32
_SfrapPerfArpTotalRxOther_Object = MibTableColumn
sfrapPerfArpTotalRxOther = _SfrapPerfArpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 17),
    _SfrapPerfArpTotalRxOther_Type()
)
sfrapPerfArpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalRxOther.setStatus("mandatory")
_SfrapPerfArpTotalTxOther_Type = Counter32
_SfrapPerfArpTotalTxOther_Object = MibTableColumn
sfrapPerfArpTotalTxOther = _SfrapPerfArpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 16, 1, 18),
    _SfrapPerfArpTotalTxOther_Type()
)
sfrapPerfArpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfArpTotalTxOther.setStatus("mandatory")
_SfrapPerfLmiPerDlciTable_Object = MibTable
sfrapPerfLmiPerDlciTable = _SfrapPerfLmiPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17)
)
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTable.setStatus("mandatory")
_SfrapPerfLmiPerDlciEntry_Object = MibTableRow
sfrapPerfLmiPerDlciEntry = _SfrapPerfLmiPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1)
)
sfrapPerfLmiPerDlciEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfLmiPerDlciInterval"),
    (0, "SFRAP-MIB", "sfrapPerfLmiPerDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciEntry.setStatus("mandatory")


class _SfrapPerfLmiPerDlciInterval_Type(Integer32):
    """Custom type sfrapPerfLmiPerDlciInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfLmiPerDlciInterval_Type.__name__ = "Integer32"
_SfrapPerfLmiPerDlciInterval_Object = MibTableColumn
sfrapPerfLmiPerDlciInterval = _SfrapPerfLmiPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 1),
    _SfrapPerfLmiPerDlciInterval_Type()
)
sfrapPerfLmiPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciInterval.setStatus("mandatory")
_SfrapPerfLmiPerDlciValue_Type = Integer32
_SfrapPerfLmiPerDlciValue_Object = MibTableColumn
sfrapPerfLmiPerDlciValue = _SfrapPerfLmiPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 2),
    _SfrapPerfLmiPerDlciValue_Type()
)
sfrapPerfLmiPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciValue.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxTotalByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxTotalByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxTotalByteCnt = _SfrapPerfLmiPerDlciRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 3),
    _SfrapPerfLmiPerDlciRxTotalByteCnt_Type()
)
sfrapPerfLmiPerDlciRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxTotalByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxTotalByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxTotalByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxTotalByteCnt = _SfrapPerfLmiPerDlciTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 4),
    _SfrapPerfLmiPerDlciTxTotalByteCnt_Type()
)
sfrapPerfLmiPerDlciTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxTotalByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxLivoEnqByteCnt = _SfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 5),
    _SfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type()
)
sfrapPerfLmiPerDlciRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxLivoEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxLivoEnqByteCnt = _SfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 6),
    _SfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type()
)
sfrapPerfLmiPerDlciTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxLivoEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxLivoStatByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxLivoStatByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxLivoStatByteCnt = _SfrapPerfLmiPerDlciRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 7),
    _SfrapPerfLmiPerDlciRxLivoStatByteCnt_Type()
)
sfrapPerfLmiPerDlciRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxLivoStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxLivoStatByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxLivoStatByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxLivoStatByteCnt = _SfrapPerfLmiPerDlciTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 8),
    _SfrapPerfLmiPerDlciTxLivoStatByteCnt_Type()
)
sfrapPerfLmiPerDlciTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxLivoStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxFullEnqByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxFullEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxFullEnqByteCnt = _SfrapPerfLmiPerDlciRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 9),
    _SfrapPerfLmiPerDlciRxFullEnqByteCnt_Type()
)
sfrapPerfLmiPerDlciRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxFullEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxFullEnqByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxFullEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxFullEnqByteCnt = _SfrapPerfLmiPerDlciTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 10),
    _SfrapPerfLmiPerDlciTxFullEnqByteCnt_Type()
)
sfrapPerfLmiPerDlciTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxFullEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxFullStatByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxFullStatByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxFullStatByteCnt = _SfrapPerfLmiPerDlciRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 11),
    _SfrapPerfLmiPerDlciRxFullStatByteCnt_Type()
)
sfrapPerfLmiPerDlciRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxFullStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxFullStatByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxFullStatByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxFullStatByteCnt = _SfrapPerfLmiPerDlciTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 12),
    _SfrapPerfLmiPerDlciTxFullStatByteCnt_Type()
)
sfrapPerfLmiPerDlciTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxFullStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciRxOtherByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciRxOtherByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciRxOtherByteCnt = _SfrapPerfLmiPerDlciRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 13),
    _SfrapPerfLmiPerDlciRxOtherByteCnt_Type()
)
sfrapPerfLmiPerDlciRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciRxOtherByteCnt.setStatus("mandatory")
_SfrapPerfLmiPerDlciTxOtherByteCnt_Type = Counter32
_SfrapPerfLmiPerDlciTxOtherByteCnt_Object = MibTableColumn
sfrapPerfLmiPerDlciTxOtherByteCnt = _SfrapPerfLmiPerDlciTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 17, 1, 14),
    _SfrapPerfLmiPerDlciTxOtherByteCnt_Type()
)
sfrapPerfLmiPerDlciTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiPerDlciTxOtherByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTable_Object = MibTable
sfrapPerfLmiTotalTable = _SfrapPerfLmiTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18)
)
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTable.setStatus("mandatory")
_SfrapPerfLmiTotalEntry_Object = MibTableRow
sfrapPerfLmiTotalEntry = _SfrapPerfLmiTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1)
)
sfrapPerfLmiTotalEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfLmiTotalInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalEntry.setStatus("mandatory")


class _SfrapPerfLmiTotalInterval_Type(Integer32):
    """Custom type sfrapPerfLmiTotalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfLmiTotalInterval_Type.__name__ = "Integer32"
_SfrapPerfLmiTotalInterval_Object = MibTableColumn
sfrapPerfLmiTotalInterval = _SfrapPerfLmiTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 1),
    _SfrapPerfLmiTotalInterval_Type()
)
sfrapPerfLmiTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalInterval.setStatus("mandatory")
_SfrapPerfLmiTotalDlciValue_Type = Integer32
_SfrapPerfLmiTotalDlciValue_Object = MibTableColumn
sfrapPerfLmiTotalDlciValue = _SfrapPerfLmiTotalDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 2),
    _SfrapPerfLmiTotalDlciValue_Type()
)
sfrapPerfLmiTotalDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalDlciValue.setStatus("mandatory")
_SfrapPerfLmiTotalRxTotalByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxTotalByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxTotalByteCnt = _SfrapPerfLmiTotalRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 3),
    _SfrapPerfLmiTotalRxTotalByteCnt_Type()
)
sfrapPerfLmiTotalRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxTotalByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxTotalByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxTotalByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxTotalByteCnt = _SfrapPerfLmiTotalTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 4),
    _SfrapPerfLmiTotalTxTotalByteCnt_Type()
)
sfrapPerfLmiTotalTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxTotalByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalRxLivoEnqByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxLivoEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxLivoEnqByteCnt = _SfrapPerfLmiTotalRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 5),
    _SfrapPerfLmiTotalRxLivoEnqByteCnt_Type()
)
sfrapPerfLmiTotalRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxLivoEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxLivoEnqByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxLivoEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxLivoEnqByteCnt = _SfrapPerfLmiTotalTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 6),
    _SfrapPerfLmiTotalTxLivoEnqByteCnt_Type()
)
sfrapPerfLmiTotalTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxLivoEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalRxLivoStatByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxLivoStatByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxLivoStatByteCnt = _SfrapPerfLmiTotalRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 7),
    _SfrapPerfLmiTotalRxLivoStatByteCnt_Type()
)
sfrapPerfLmiTotalRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxLivoStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxLivoStatByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxLivoStatByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxLivoStatByteCnt = _SfrapPerfLmiTotalTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 8),
    _SfrapPerfLmiTotalTxLivoStatByteCnt_Type()
)
sfrapPerfLmiTotalTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxLivoStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalRxFullEnqByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxFullEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxFullEnqByteCnt = _SfrapPerfLmiTotalRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 9),
    _SfrapPerfLmiTotalRxFullEnqByteCnt_Type()
)
sfrapPerfLmiTotalRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxFullEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxFullEnqByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxFullEnqByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxFullEnqByteCnt = _SfrapPerfLmiTotalTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 10),
    _SfrapPerfLmiTotalTxFullEnqByteCnt_Type()
)
sfrapPerfLmiTotalTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxFullEnqByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalRxFullStatByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxFullStatByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxFullStatByteCnt = _SfrapPerfLmiTotalRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 11),
    _SfrapPerfLmiTotalRxFullStatByteCnt_Type()
)
sfrapPerfLmiTotalRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxFullStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxFullStatByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxFullStatByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxFullStatByteCnt = _SfrapPerfLmiTotalTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 12),
    _SfrapPerfLmiTotalTxFullStatByteCnt_Type()
)
sfrapPerfLmiTotalTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxFullStatByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalRxOtherByteCnt_Type = Counter32
_SfrapPerfLmiTotalRxOtherByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalRxOtherByteCnt = _SfrapPerfLmiTotalRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 13),
    _SfrapPerfLmiTotalRxOtherByteCnt_Type()
)
sfrapPerfLmiTotalRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalRxOtherByteCnt.setStatus("mandatory")
_SfrapPerfLmiTotalTxOtherByteCnt_Type = Counter32
_SfrapPerfLmiTotalTxOtherByteCnt_Object = MibTableColumn
sfrapPerfLmiTotalTxOtherByteCnt = _SfrapPerfLmiTotalTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 4, 18, 1, 14),
    _SfrapPerfLmiTotalTxOtherByteCnt_Type()
)
sfrapPerfLmiTotalTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfLmiTotalTxOtherByteCnt.setStatus("mandatory")
_SfrapPerfNetworkLongTerm_ObjectIdentity = ObjectIdentity
sfrapPerfNetworkLongTerm = _SfrapPerfNetworkLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5)
)
_SfrapPerfNetwLongTermTable_Object = MibTable
sfrapPerfNetwLongTermTable = _SfrapPerfNetwLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1)
)
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermTable.setStatus("mandatory")
_SfrapPerfNetwLongTermEntry_Object = MibTableRow
sfrapPerfNetwLongTermEntry = _SfrapPerfNetwLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1, 1)
)
sfrapPerfNetwLongTermEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfNetwLongTermDlci"),
    (0, "SFRAP-MIB", "sfrapPerfNetwLongTermProtocol"),
    (0, "SFRAP-MIB", "sfrapPerfNetwLongTermInterval"),
)
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermEntry.setStatus("mandatory")
_SfrapPerfNetwLongTermDlci_Type = Integer32
_SfrapPerfNetwLongTermDlci_Object = MibTableColumn
sfrapPerfNetwLongTermDlci = _SfrapPerfNetwLongTermDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1, 1, 1),
    _SfrapPerfNetwLongTermDlci_Type()
)
sfrapPerfNetwLongTermDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermDlci.setStatus("mandatory")


class _SfrapPerfNetwLongTermProtocol_Type(Integer32):
    """Custom type sfrapPerfNetwLongTermProtocol based on Integer32"""
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
              13,
              14,
              15,
              16,
              21,
              22,
              29,
              30,
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172)
        )
    )
    namedValues = NamedValues(
        *(("addr-mask-rep-icmp-ip-rx-bc", 64),
          ("addr-mask-rep-icmp-ip-tx-bc", 63),
          ("addr-mask-req-icmp-ip-rx-bc", 62),
          ("addr-mask-req-icmp-ip-tx-bc", 61),
          ("annex-g-rx-bc", 172),
          ("annex-g-tx-bc", 171),
          ("arp-rep-rx-bc", 96),
          ("arp-rep-tx-bc", 95),
          ("arp-req-rx-bc", 94),
          ("arp-req-tx-bc", 93),
          ("arp-rx-bc", 92),
          ("arp-tx-bc", 91),
          ("cir-percent-range1-rx-bc", 138),
          ("cir-percent-range1-tx-bc", 137),
          ("cir-percent-range2-rx-bc", 140),
          ("cir-percent-range2-tx-bc", 139),
          ("cir-percent-range3-rx-bc", 142),
          ("cir-percent-range3-tx-bc", 141),
          ("cir-percent-range4-rx-bc", 144),
          ("cir-percent-range4-tx-bc", 143),
          ("cir-percent-range5-rx-bc", 146),
          ("cir-percent-range5-tx-bc", 145),
          ("cir-percent-range6-rx-bc", 148),
          ("cir-percent-range6-tx-bc", 147),
          ("cir-percent-range7-rx-bc", 150),
          ("cir-percent-range7-tx-bc", 149),
          ("cir-percent-range8-rx-bc", 152),
          ("cir-percent-range8-tx-bc", 151),
          ("cisco-rx-bc", 116),
          ("cisco-tx-bc", 115),
          ("dest-unr-icmp-ip-rx-bc", 46),
          ("dest-unr-icmp-ip-tx-bc", 45),
          ("echorep-icmp-ip-rx-bc", 44),
          ("echorep-icmp-ip-tx-bc", 43),
          ("echoreq-icmp-ip-rx-bc", 52),
          ("echoreq-icmp-ip-tx-bc", 51),
          ("ftp-tcp-ip-rx-bc", 6),
          ("ftp-tcp-ip-tx-bc", 5),
          ("gp-mem-query-icmp-ip-rx-bc", 68),
          ("gp-mem-query-icmp-ip-tx-bc", 67),
          ("gp-mem-reduct-icmp-ip-rx-bc", 72),
          ("gp-mem-reduct-icmp-ip-tx-bc", 71),
          ("gp-mem-report-icmp-ip-rx-bc", 70),
          ("gp-mem-report-icmp-ip-tx-bc", 69),
          ("http-tcp-ip-rx-bc", 14),
          ("http-tcp-ip-tx-bc", 13),
          ("icmp-ip-rx-bc", 42),
          ("icmp-ip-tx-bc", 41),
          ("igrp-rx-bc", 168),
          ("igrp-tx-bc", 167),
          ("inarp-rep-rx-bc", 104),
          ("inarp-rep-tx-bc", 103),
          ("inarp-req-rx-bc", 102),
          ("inarp-req-tx-bc", 101),
          ("ip-rx-bc", 2),
          ("ip-tx-bc", 1),
          ("ipx-rx-bc", 78),
          ("ipx-tx-bc", 77),
          ("lmi-full-enq-rx-bc", 160),
          ("lmi-full-enq-tx-bc", 159),
          ("lmi-full-stat-rx-bc", 162),
          ("lmi-full-stat-tx-bc", 161),
          ("lmi-livo-enq-rx-bc", 156),
          ("lmi-livo-enq-tx-bc", 155),
          ("lmi-livo-stat-rx-bc", 158),
          ("lmi-livo-stat-tx-bc", 157),
          ("lmi-other-rx-bc", 164),
          ("lmi-other-tx-bc", 163),
          ("lmi-rx-bc", 154),
          ("lmi-tx-bc", 153),
          ("ncp-ipx-rx-bc", 82),
          ("ncp-ipx-tx-bc", 81),
          ("netbios-dgm-udp-ip-rx-bc", 34),
          ("netbios-dgm-udp-ip-tx-bc", 33),
          ("netbios-ipx-rx-bc", 88),
          ("netbios-ipx-tx-bc", 87),
          ("netbios-ssn-tcp-ip-rx-bc", 16),
          ("netbios-ssn-tcp-ip-tx-bc", 15),
          ("ospf-ip-rx-bc", 74),
          ("ospf-ip-tx-bc", 73),
          ("other-ip-rx-bc", 76),
          ("other-ip-tx-bc", 75),
          ("other-ipx-rx-bc", 90),
          ("other-ipx-tx-bc", 89),
          ("other-rx-bc", 118),
          ("other-tx-bc", 117),
          ("param-prob-icmp-ip-rx-bc", 56),
          ("param-prob-icmp-ip-tx-bc", 55),
          ("pkt-too-big-icmp-ip-rx-bc", 66),
          ("pkt-too-big-icmp-ip-tx-bc", 65),
          ("rarp-rep-rx-bc", 100),
          ("rarp-rep-tx-bc", 99),
          ("rarp-req-rx-bc", 98),
          ("rarp-req-tx-bc", 97),
          ("redirect-icmp-ip-rx-bc", 50),
          ("redirect-icmp-ip-tx-bc", 49),
          ("rip-ipx-rx-bc", 86),
          ("rip-ipx-tx-bc", 85),
          ("rip-udp-ip-rx-bc", 40),
          ("rip-udp-ip-tx-bc", 39),
          ("sap-ipx-rx-bc", 84),
          ("sap-ipx-tx-bc", 83),
          ("smtp-tcp-ip-rx-bc", 10),
          ("smtp-tcp-ip-tx-bc", 9),
          ("sna-appn-rx-bc", 112),
          ("sna-appn-tx-bc", 111),
          ("sna-netbios-rx-bc", 114),
          ("sna-netbios-tx-bc", 113),
          ("sna-periph-rx-bc", 110),
          ("sna-periph-tx-bc", 109),
          ("sna-rx-bc", 106),
          ("sna-subarea-rx-bc", 108),
          ("sna-subarea-tx-bc", 107),
          ("sna-tx-bc", 105),
          ("snmp-udp-ip-rx-bc", 36),
          ("snmp-udp-ip-tx-bc", 35),
          ("snmptrap-udp-ip-rx-bc", 38),
          ("snmptrap-udp-ip-tx-bc", 37),
          ("spx-ipx-rx-bc", 80),
          ("spx-ipx-tx-bc", 79),
          ("src-quench-icmp-ip-rx-bc", 48),
          ("src-quench-icmp-ip-tx-bc", 47),
          ("tcp-ip-rx-bc", 4),
          ("tcp-ip-tx-bc", 3),
          ("telnet-tcp-ip-rx-bc", 8),
          ("telnet-tcp-ip-tx-bc", 7),
          ("tftp-udp-ip-rx-bc", 30),
          ("tftp-udp-ip-tx-bc", 29),
          ("thru-becn-rx-c", 134),
          ("thru-becn-tx-c", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-c", 136),
          ("thru-de-tx-c", 135),
          ("thru-fecn-rx-c", 132),
          ("thru-fecn-tx-c", 131),
          ("thru-frame-rx-c", 130),
          ("thru-frame-tx-c", 129),
          ("time-excd-icmp-ip-rx-bc", 54),
          ("time-excd-icmp-ip-tx-bc", 53),
          ("timestamp-rep-icmp-ip-rx-bc", 60),
          ("timestamp-rep-icmp-ip-tx-bc", 59),
          ("timestamp-req-icmp-ip-rx-bc", 58),
          ("timestamp-req-icmp-ip-tx-bc", 57),
          ("total-downtime", 166),
          ("total-uptime", 165),
          ("udp-ip-rx-bc", 22),
          ("udp-ip-tx-bc", 21),
          ("user-defined-1-rx-bc", 120),
          ("user-defined-1-tx-bc", 119),
          ("user-defined-2-rx-bc", 122),
          ("user-defined-2-tx-bc", 121),
          ("user-defined-3-rx-bc", 124),
          ("user-defined-3-tx-bc", 123),
          ("user-defined-4-rx-bc", 126),
          ("user-defined-4-tx-bc", 125),
          ("vnip-rx-bc", 170),
          ("vnip-tx-bc", 169))
    )


_SfrapPerfNetwLongTermProtocol_Type.__name__ = "Integer32"
_SfrapPerfNetwLongTermProtocol_Object = MibTableColumn
sfrapPerfNetwLongTermProtocol = _SfrapPerfNetwLongTermProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1, 1, 2),
    _SfrapPerfNetwLongTermProtocol_Type()
)
sfrapPerfNetwLongTermProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermProtocol.setStatus("mandatory")
_SfrapPerfNetwLongTermInterval_Type = Integer32
_SfrapPerfNetwLongTermInterval_Object = MibTableColumn
sfrapPerfNetwLongTermInterval = _SfrapPerfNetwLongTermInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1, 1, 3),
    _SfrapPerfNetwLongTermInterval_Type()
)
sfrapPerfNetwLongTermInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermInterval.setStatus("mandatory")
_SfrapPerfNetwLongTermValue_Type = Counter32
_SfrapPerfNetwLongTermValue_Object = MibTableColumn
sfrapPerfNetwLongTermValue = _SfrapPerfNetwLongTermValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 1, 1, 4),
    _SfrapPerfNetwLongTermValue_Type()
)
sfrapPerfNetwLongTermValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermValue.setStatus("mandatory")
_SfrapPerfNetwLongTermAltTable_Object = MibTable
sfrapPerfNetwLongTermAltTable = _SfrapPerfNetwLongTermAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 2)
)
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermAltTable.setStatus("mandatory")
_SfrapPerfNetwLongTermAltEntry_Object = MibTableRow
sfrapPerfNetwLongTermAltEntry = _SfrapPerfNetwLongTermAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 2, 1)
)
sfrapPerfNetwLongTermAltEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfNetwLongTermAltDlci"),
    (0, "SFRAP-MIB", "sfrapPerfNetwLongTermAltProtocol"),
)
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermAltEntry.setStatus("mandatory")
_SfrapPerfNetwLongTermAltDlci_Type = Integer32
_SfrapPerfNetwLongTermAltDlci_Object = MibTableColumn
sfrapPerfNetwLongTermAltDlci = _SfrapPerfNetwLongTermAltDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 2, 1, 1),
    _SfrapPerfNetwLongTermAltDlci_Type()
)
sfrapPerfNetwLongTermAltDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermAltDlci.setStatus("mandatory")


class _SfrapPerfNetwLongTermAltProtocol_Type(Integer32):
    """Custom type sfrapPerfNetwLongTermAltProtocol based on Integer32"""
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
              13,
              14,
              15,
              16,
              21,
              22,
              29,
              30,
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172)
        )
    )
    namedValues = NamedValues(
        *(("addr-mask-rep-icmp-ip-rx-bc", 64),
          ("addr-mask-rep-icmp-ip-tx-bc", 63),
          ("addr-mask-req-icmp-ip-rx-bc", 62),
          ("addr-mask-req-icmp-ip-tx-bc", 61),
          ("annex-g-rx-bc", 172),
          ("annex-g-tx-bc", 171),
          ("arp-rep-rx-bc", 96),
          ("arp-rep-tx-bc", 95),
          ("arp-req-rx-bc", 94),
          ("arp-req-tx-bc", 93),
          ("arp-rx-bc", 92),
          ("arp-tx-bc", 91),
          ("cir-percent-range1-rx-bc", 138),
          ("cir-percent-range1-tx-bc", 137),
          ("cir-percent-range2-rx-bc", 140),
          ("cir-percent-range2-tx-bc", 139),
          ("cir-percent-range3-rx-bc", 142),
          ("cir-percent-range3-tx-bc", 141),
          ("cir-percent-range4-rx-bc", 144),
          ("cir-percent-range4-tx-bc", 143),
          ("cir-percent-range5-rx-bc", 146),
          ("cir-percent-range5-tx-bc", 145),
          ("cir-percent-range6-rx-bc", 148),
          ("cir-percent-range6-tx-bc", 147),
          ("cir-percent-range7-rx-bc", 150),
          ("cir-percent-range7-tx-bc", 149),
          ("cir-percent-range8-rx-bc", 152),
          ("cir-percent-range8-tx-bc", 151),
          ("cisco-rx-bc", 116),
          ("cisco-tx-bc", 115),
          ("dest-unr-icmp-ip-rx-bc", 46),
          ("dest-unr-icmp-ip-tx-bc", 45),
          ("echorep-icmp-ip-rx-bc", 44),
          ("echorep-icmp-ip-tx-bc", 43),
          ("echoreq-icmp-ip-rx-bc", 52),
          ("echoreq-icmp-ip-tx-bc", 51),
          ("ftp-tcp-ip-rx-bc", 6),
          ("ftp-tcp-ip-tx-bc", 5),
          ("gp-mem-query-icmp-ip-rx-bc", 68),
          ("gp-mem-query-icmp-ip-tx-bc", 67),
          ("gp-mem-reduct-icmp-ip-rx-bc", 72),
          ("gp-mem-reduct-icmp-ip-tx-bc", 71),
          ("gp-mem-report-icmp-ip-rx-bc", 70),
          ("gp-mem-report-icmp-ip-tx-bc", 69),
          ("http-tcp-ip-rx-bc", 14),
          ("http-tcp-ip-tx-bc", 13),
          ("icmp-ip-rx-bc", 42),
          ("icmp-ip-tx-bc", 41),
          ("igrp-rx-bc", 168),
          ("igrp-tx-bc", 167),
          ("inarp-rep-rx-bc", 104),
          ("inarp-rep-tx-bc", 103),
          ("inarp-req-rx-bc", 102),
          ("inarp-req-tx-bc", 101),
          ("ip-rx-bc", 2),
          ("ip-tx-bc", 1),
          ("ipx-rx-bc", 78),
          ("ipx-tx-bc", 77),
          ("lmi-full-enq-rx-bc", 160),
          ("lmi-full-enq-tx-bc", 159),
          ("lmi-full-stat-rx-bc", 162),
          ("lmi-full-stat-tx-bc", 161),
          ("lmi-livo-enq-rx-bc", 156),
          ("lmi-livo-enq-tx-bc", 155),
          ("lmi-livo-stat-rx-bc", 158),
          ("lmi-livo-stat-tx-bc", 157),
          ("lmi-other-rx-bc", 164),
          ("lmi-other-tx-bc", 163),
          ("lmi-rx-bc", 154),
          ("lmi-tx-bc", 153),
          ("ncp-ipx-rx-bc", 82),
          ("ncp-ipx-tx-bc", 81),
          ("netbios-dgm-udp-ip-rx-bc", 34),
          ("netbios-dgm-udp-ip-tx-bc", 33),
          ("netbios-ipx-rx-bc", 88),
          ("netbios-ipx-tx-bc", 87),
          ("netbios-ssn-tcp-ip-rx-bc", 16),
          ("netbios-ssn-tcp-ip-tx-bc", 15),
          ("ospf-ip-rx-bc", 74),
          ("ospf-ip-tx-bc", 73),
          ("other-ip-rx-bc", 76),
          ("other-ip-tx-bc", 75),
          ("other-ipx-rx-bc", 90),
          ("other-ipx-tx-bc", 89),
          ("other-rx-bc", 118),
          ("other-tx-bc", 117),
          ("param-prob-icmp-ip-rx-bc", 56),
          ("param-prob-icmp-ip-tx-bc", 55),
          ("pkt-too-big-icmp-ip-rx-bc", 66),
          ("pkt-too-big-icmp-ip-tx-bc", 65),
          ("rarp-rep-rx-bc", 100),
          ("rarp-rep-tx-bc", 99),
          ("rarp-req-rx-bc", 98),
          ("rarp-req-tx-bc", 97),
          ("redirect-icmp-ip-rx-bc", 50),
          ("redirect-icmp-ip-tx-bc", 49),
          ("rip-ipx-rx-bc", 86),
          ("rip-ipx-tx-bc", 85),
          ("rip-udp-ip-rx-bc", 40),
          ("rip-udp-ip-tx-bc", 39),
          ("sap-ipx-rx-bc", 84),
          ("sap-ipx-tx-bc", 83),
          ("smtp-tcp-ip-rx-bc", 10),
          ("smtp-tcp-ip-tx-bc", 9),
          ("sna-appn-rx-bc", 112),
          ("sna-appn-tx-bc", 111),
          ("sna-netbios-rx-bc", 114),
          ("sna-netbios-tx-bc", 113),
          ("sna-periph-rx-bc", 110),
          ("sna-periph-tx-bc", 109),
          ("sna-rx-bc", 106),
          ("sna-subarea-rx-bc", 108),
          ("sna-subarea-tx-bc", 107),
          ("sna-tx-bc", 105),
          ("snmp-udp-ip-rx-bc", 36),
          ("snmp-udp-ip-tx-bc", 35),
          ("snmptrap-udp-ip-rx-bc", 38),
          ("snmptrap-udp-ip-tx-bc", 37),
          ("spx-ipx-rx-bc", 80),
          ("spx-ipx-tx-bc", 79),
          ("src-quench-icmp-ip-rx-bc", 48),
          ("src-quench-icmp-ip-tx-bc", 47),
          ("tcp-ip-rx-bc", 4),
          ("tcp-ip-tx-bc", 3),
          ("telnet-tcp-ip-rx-bc", 8),
          ("telnet-tcp-ip-tx-bc", 7),
          ("tftp-udp-ip-rx-bc", 30),
          ("tftp-udp-ip-tx-bc", 29),
          ("thru-becn-rx-c", 134),
          ("thru-becn-tx-c", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-c", 136),
          ("thru-de-tx-c", 135),
          ("thru-fecn-rx-c", 132),
          ("thru-fecn-tx-c", 131),
          ("thru-frame-rx-c", 130),
          ("thru-frame-tx-c", 129),
          ("time-excd-icmp-ip-rx-bc", 54),
          ("time-excd-icmp-ip-tx-bc", 53),
          ("timestamp-rep-icmp-ip-rx-bc", 60),
          ("timestamp-rep-icmp-ip-tx-bc", 59),
          ("timestamp-req-icmp-ip-rx-bc", 58),
          ("timestamp-req-icmp-ip-tx-bc", 57),
          ("total-downtime", 166),
          ("total-uptime", 165),
          ("udp-ip-rx-bc", 22),
          ("udp-ip-tx-bc", 21),
          ("user-defined-1-rx-bc", 120),
          ("user-defined-1-tx-bc", 119),
          ("user-defined-2-rx-bc", 122),
          ("user-defined-2-tx-bc", 121),
          ("user-defined-3-rx-bc", 124),
          ("user-defined-3-tx-bc", 123),
          ("user-defined-4-rx-bc", 126),
          ("user-defined-4-tx-bc", 125),
          ("vnip-rx-bc", 170),
          ("vnip-tx-bc", 169))
    )


_SfrapPerfNetwLongTermAltProtocol_Type.__name__ = "Integer32"
_SfrapPerfNetwLongTermAltProtocol_Object = MibTableColumn
sfrapPerfNetwLongTermAltProtocol = _SfrapPerfNetwLongTermAltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 2, 1, 2),
    _SfrapPerfNetwLongTermAltProtocol_Type()
)
sfrapPerfNetwLongTermAltProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermAltProtocol.setStatus("mandatory")
_SfrapPerfNetwLongTermAltArray_Type = OctetString
_SfrapPerfNetwLongTermAltArray_Object = MibTableColumn
sfrapPerfNetwLongTermAltArray = _SfrapPerfNetwLongTermAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 2, 1, 3),
    _SfrapPerfNetwLongTermAltArray_Type()
)
sfrapPerfNetwLongTermAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfNetwLongTermAltArray.setStatus("mandatory")
_SfrapPerfNetworkLongTermCommands_ObjectIdentity = ObjectIdentity
sfrapPerfNetworkLongTermCommands = _SfrapPerfNetworkLongTermCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 3)
)


class _SfrapPerfNetworkLongTermCmdClear_Type(Integer32):
    """Custom type sfrapPerfNetworkLongTermCmdClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_SfrapPerfNetworkLongTermCmdClear_Type.__name__ = "Integer32"
_SfrapPerfNetworkLongTermCmdClear_Object = MibScalar
sfrapPerfNetworkLongTermCmdClear = _SfrapPerfNetworkLongTermCmdClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 5, 3, 1),
    _SfrapPerfNetworkLongTermCmdClear_Type()
)
sfrapPerfNetworkLongTermCmdClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapPerfNetworkLongTermCmdClear.setStatus("mandatory")
_SfrapPerfCirPercentUtilization_ObjectIdentity = ObjectIdentity
sfrapPerfCirPercentUtilization = _SfrapPerfCirPercentUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6)
)
_SfrapPerfCirPercentUtilizationTable_Object = MibTable
sfrapPerfCirPercentUtilizationTable = _SfrapPerfCirPercentUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1)
)
if mibBuilder.loadTexts:
    sfrapPerfCirPercentUtilizationTable.setStatus("mandatory")
_SfrapPerfCirPercentUtilizationEntry_Object = MibTableRow
sfrapPerfCirPercentUtilizationEntry = _SfrapPerfCirPercentUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1)
)
sfrapPerfCirPercentUtilizationEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfCirPercentUtilizationInterval"),
    (0, "SFRAP-MIB", "sfrapPerfCirPercentUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfCirPercentUtilizationEntry.setStatus("mandatory")


class _SfrapPerfCirPercentUtilizationInterval_Type(Integer32):
    """Custom type sfrapPerfCirPercentUtilizationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cumulative-counts", 3),
          ("current-interval", 1),
          ("previous-interval", 2))
    )


_SfrapPerfCirPercentUtilizationInterval_Type.__name__ = "Integer32"
_SfrapPerfCirPercentUtilizationInterval_Object = MibTableColumn
sfrapPerfCirPercentUtilizationInterval = _SfrapPerfCirPercentUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 1),
    _SfrapPerfCirPercentUtilizationInterval_Type()
)
sfrapPerfCirPercentUtilizationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirPercentUtilizationInterval.setStatus("mandatory")
_SfrapPerfCirPercentUtilizationDlciValue_Type = Integer32
_SfrapPerfCirPercentUtilizationDlciValue_Object = MibTableColumn
sfrapPerfCirPercentUtilizationDlciValue = _SfrapPerfCirPercentUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 2),
    _SfrapPerfCirPercentUtilizationDlciValue_Type()
)
sfrapPerfCirPercentUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirPercentUtilizationDlciValue.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange1_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange1_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange1 = _SfrapPerfCirRxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 21),
    _SfrapPerfCirRxPercentUtilizationRange1_Type()
)
sfrapPerfCirRxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange1.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange2_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange2_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange2 = _SfrapPerfCirRxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 22),
    _SfrapPerfCirRxPercentUtilizationRange2_Type()
)
sfrapPerfCirRxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange2.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange3_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange3_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange3 = _SfrapPerfCirRxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 23),
    _SfrapPerfCirRxPercentUtilizationRange3_Type()
)
sfrapPerfCirRxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange3.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange4_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange4_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange4 = _SfrapPerfCirRxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 24),
    _SfrapPerfCirRxPercentUtilizationRange4_Type()
)
sfrapPerfCirRxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange4.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange5_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange5_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange5 = _SfrapPerfCirRxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 25),
    _SfrapPerfCirRxPercentUtilizationRange5_Type()
)
sfrapPerfCirRxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange5.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange6_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange6_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange6 = _SfrapPerfCirRxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 26),
    _SfrapPerfCirRxPercentUtilizationRange6_Type()
)
sfrapPerfCirRxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange6.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange7_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange7_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange7 = _SfrapPerfCirRxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 27),
    _SfrapPerfCirRxPercentUtilizationRange7_Type()
)
sfrapPerfCirRxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange7.setStatus("mandatory")
_SfrapPerfCirRxPercentUtilizationRange8_Type = Integer32
_SfrapPerfCirRxPercentUtilizationRange8_Object = MibTableColumn
sfrapPerfCirRxPercentUtilizationRange8 = _SfrapPerfCirRxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 28),
    _SfrapPerfCirRxPercentUtilizationRange8_Type()
)
sfrapPerfCirRxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirRxPercentUtilizationRange8.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange1_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange1_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange1 = _SfrapPerfCirTxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 41),
    _SfrapPerfCirTxPercentUtilizationRange1_Type()
)
sfrapPerfCirTxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange1.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange2_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange2_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange2 = _SfrapPerfCirTxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 42),
    _SfrapPerfCirTxPercentUtilizationRange2_Type()
)
sfrapPerfCirTxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange2.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange3_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange3_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange3 = _SfrapPerfCirTxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 43),
    _SfrapPerfCirTxPercentUtilizationRange3_Type()
)
sfrapPerfCirTxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange3.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange4_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange4_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange4 = _SfrapPerfCirTxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 44),
    _SfrapPerfCirTxPercentUtilizationRange4_Type()
)
sfrapPerfCirTxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange4.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange5_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange5_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange5 = _SfrapPerfCirTxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 45),
    _SfrapPerfCirTxPercentUtilizationRange5_Type()
)
sfrapPerfCirTxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange5.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange6_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange6_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange6 = _SfrapPerfCirTxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 46),
    _SfrapPerfCirTxPercentUtilizationRange6_Type()
)
sfrapPerfCirTxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange6.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange7_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange7_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange7 = _SfrapPerfCirTxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 47),
    _SfrapPerfCirTxPercentUtilizationRange7_Type()
)
sfrapPerfCirTxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange7.setStatus("mandatory")
_SfrapPerfCirTxPercentUtilizationRange8_Type = Integer32
_SfrapPerfCirTxPercentUtilizationRange8_Object = MibTableColumn
sfrapPerfCirTxPercentUtilizationRange8 = _SfrapPerfCirTxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 1, 1, 48),
    _SfrapPerfCirTxPercentUtilizationRange8_Type()
)
sfrapPerfCirTxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCirTxPercentUtilizationRange8.setStatus("mandatory")
_SfrapPerfCurrentPerDlciUtilizationTable_Object = MibTable
sfrapPerfCurrentPerDlciUtilizationTable = _SfrapPerfCurrentPerDlciUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2)
)
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciUtilizationTable.setStatus("mandatory")
_SfrapPerfCurrentPerDlciUtilizationEntry_Object = MibTableRow
sfrapPerfCurrentPerDlciUtilizationEntry = _SfrapPerfCurrentPerDlciUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2, 1)
)
sfrapPerfCurrentPerDlciUtilizationEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapPerfCurrentPerDlciUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciUtilizationEntry.setStatus("mandatory")
_SfrapPerfCurrentPerDlciUtilizationDlciValue_Type = Integer32
_SfrapPerfCurrentPerDlciUtilizationDlciValue_Object = MibTableColumn
sfrapPerfCurrentPerDlciUtilizationDlciValue = _SfrapPerfCurrentPerDlciUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2, 1, 1),
    _SfrapPerfCurrentPerDlciUtilizationDlciValue_Type()
)
sfrapPerfCurrentPerDlciUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciUtilizationDlciValue.setStatus("mandatory")
_SfrapPerfCurrentPerDlciRxUtilization_Type = Integer32
_SfrapPerfCurrentPerDlciRxUtilization_Object = MibTableColumn
sfrapPerfCurrentPerDlciRxUtilization = _SfrapPerfCurrentPerDlciRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2, 1, 2),
    _SfrapPerfCurrentPerDlciRxUtilization_Type()
)
sfrapPerfCurrentPerDlciRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciRxUtilization.setStatus("mandatory")
_SfrapPerfCurrentPerDlciTxUtilization_Type = Integer32
_SfrapPerfCurrentPerDlciTxUtilization_Object = MibTableColumn
sfrapPerfCurrentPerDlciTxUtilization = _SfrapPerfCurrentPerDlciTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2, 1, 3),
    _SfrapPerfCurrentPerDlciTxUtilization_Type()
)
sfrapPerfCurrentPerDlciTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciTxUtilization.setStatus("mandatory")
_SfrapPerfCurrentPerDlciAggregateUtilization_Type = Integer32
_SfrapPerfCurrentPerDlciAggregateUtilization_Object = MibTableColumn
sfrapPerfCurrentPerDlciAggregateUtilization = _SfrapPerfCurrentPerDlciAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 2, 1, 4),
    _SfrapPerfCurrentPerDlciAggregateUtilization_Type()
)
sfrapPerfCurrentPerDlciAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentPerDlciAggregateUtilization.setStatus("mandatory")
_SfrapPerfCurrentUnitUtilization_ObjectIdentity = ObjectIdentity
sfrapPerfCurrentUnitUtilization = _SfrapPerfCurrentUnitUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 3)
)
_SfrapPerfCurrentDteUtilization_Type = Integer32
_SfrapPerfCurrentDteUtilization_Object = MibScalar
sfrapPerfCurrentDteUtilization = _SfrapPerfCurrentDteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 3, 2),
    _SfrapPerfCurrentDteUtilization_Type()
)
sfrapPerfCurrentDteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentDteUtilization.setStatus("mandatory")
_SfrapPerfCurrentWanUtilization_Type = Integer32
_SfrapPerfCurrentWanUtilization_Object = MibScalar
sfrapPerfCurrentWanUtilization = _SfrapPerfCurrentWanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 3, 3),
    _SfrapPerfCurrentWanUtilization_Type()
)
sfrapPerfCurrentWanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentWanUtilization.setStatus("mandatory")
_SfrapPerfCurrentAggregateUtilization_Type = Integer32
_SfrapPerfCurrentAggregateUtilization_Object = MibScalar
sfrapPerfCurrentAggregateUtilization = _SfrapPerfCurrentAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 6, 3, 4),
    _SfrapPerfCurrentAggregateUtilization_Type()
)
sfrapPerfCurrentAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfCurrentAggregateUtilization.setStatus("mandatory")
_SfrapPerfFRStatsCollectionStatus_ObjectIdentity = ObjectIdentity
sfrapPerfFRStatsCollectionStatus = _SfrapPerfFRStatsCollectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 7)
)


class _SfrapPerfFRStatsCollection_Type(Integer32):
    """Custom type sfrapPerfFRStatsCollection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("collecting-stats", 2),
          ("not-collecting-stats", 1))
    )


_SfrapPerfFRStatsCollection_Type.__name__ = "Integer32"
_SfrapPerfFRStatsCollection_Object = MibScalar
sfrapPerfFRStatsCollection = _SfrapPerfFRStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 5, 7, 1),
    _SfrapPerfFRStatsCollection_Type()
)
sfrapPerfFRStatsCollection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPerfFRStatsCollection.setStatus("mandatory")


class _SfrapAlarmType_Type(Integer32):
    """Custom type sfrapAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              14,
              15,
              16,
              17,
              18,
              19,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              75,
              76,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              100,
              101,
              102,
              103,
              138,
              139,
              140,
              141,
              142,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265)
        )
    )
    namedValues = NamedValues(
        *(("bad-config-in-set", 1),
          ("config-install-success", 142),
          ("config-local-update", 2),
          ("dlci-active", 47),
          ("dlci-inactive", 48),
          ("dlci-td-threshold", 49),
          ("dte-signal-control-off", 101),
          ("dte-signal-control-on", 100),
          ("dte-signal-dtr-off", 58),
          ("dte-signal-dtr-on", 57),
          ("dte-signal-indicate-off", 103),
          ("dte-signal-indicate-on", 102),
          ("dte-signal-rts-off", 56),
          ("dte-signal-rts-on", 55),
          ("lmi-non-incr-seq-num-dte", 59),
          ("lmi-non-incr-seq-num-net", 60),
          ("lmi-seq-num-mismatch-dte", 61),
          ("lmi-seq-num-mismatch-net", 62),
          ("lmi-sourcing-change-net-dte", 52),
          ("lmi-sourcing-change-net-net", 54),
          ("lmi-sourcing-change-passthru", 50),
          ("lmi-sourcing-change-user-dte", 51),
          ("lmi-sourcing-change-user-net", 53),
          ("local-dte-loopback-disabled", 18),
          ("local-dte-loopback-enabled", 17),
          ("local-dte-loopback-failure", 19),
          ("local-dte2-loopback-disabled", 85),
          ("local-dte2-loopback-enabled", 84),
          ("local-dte2-loopback-failure", 86),
          ("local-unit-loopback-disabled", 15),
          ("local-unit-loopback-enabled", 14),
          ("local-unit-loopback-failure", 16),
          ("low-speed-exceeded", 80),
          ("low-speed-resumed", 81),
          ("op-mode-cutthru-disabled", 83),
          ("op-mode-cutthru-enabled", 82),
          ("pvc-rx-utilization-cleared", 140),
          ("pvc-rx-utilization-exceeded", 138),
          ("pvc-tx-utilization-cleared", 141),
          ("pvc-tx-utilization-exceeded", 139),
          ("tftp-aborted", 260),
          ("tftp-corrupt-file", 265),
          ("tftp-host-unreachable", 262),
          ("tftp-invalid-file", 264),
          ("tftp-no-file", 263),
          ("tftp-programming", 259),
          ("tftp-requested", 257),
          ("tftp-success", 261),
          ("tftp-transferring", 258),
          ("trap-muting-active", 75),
          ("trap-muting-inactive", 76),
          ("vbert-request-failed", 97),
          ("vbert-started", 95),
          ("vbert-stopped", 96),
          ("vloop-down-via-remote", 93),
          ("vloop-failed", 94),
          ("vloop-loop-down", 91),
          ("vloop-loop-up", 90),
          ("vloop-up-via-remote", 92))
    )


_SfrapAlarmType_Type.__name__ = "Integer32"
_SfrapAlarmType_Object = MibScalar
sfrapAlarmType = _SfrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 6),
    _SfrapAlarmType_Type()
)
sfrapAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapAlarmType.setStatus("mandatory")
_SfrapDLCINum_Type = Integer32
_SfrapDLCINum_Object = MibScalar
sfrapDLCINum = _SfrapDLCINum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 7),
    _SfrapDLCINum_Type()
)
sfrapDLCINum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapDLCINum.setStatus("mandatory")


class _SfrapInterface_Type(Integer32):
    """Custom type sfrapInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-dce", 2),
          ("to-dte", 1))
    )


_SfrapInterface_Type.__name__ = "Integer32"
_SfrapInterface_Object = MibScalar
sfrapInterface = _SfrapInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 8),
    _SfrapInterface_Type()
)
sfrapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapInterface.setStatus("mandatory")
_SfrapIpAddress_Type = IpAddress
_SfrapIpAddress_Object = MibScalar
sfrapIpAddress = _SfrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 9),
    _SfrapIpAddress_Type()
)
sfrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapIpAddress.setStatus("mandatory")
_SfrapEventTrapLog_ObjectIdentity = ObjectIdentity
sfrapEventTrapLog = _SfrapEventTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 7, 10)
)
_SfrapEventTrapLogTable_Object = MibTable
sfrapEventTrapLogTable = _SfrapEventTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1)
)
if mibBuilder.loadTexts:
    sfrapEventTrapLogTable.setStatus("mandatory")
_SfrapEventTrapLogEntry_Object = MibTableRow
sfrapEventTrapLogEntry = _SfrapEventTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1)
)
sfrapEventTrapLogEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapEventTrapLogSeqNum"),
)
if mibBuilder.loadTexts:
    sfrapEventTrapLogEntry.setStatus("mandatory")
_SfrapEventTrapLogSeqNum_Type = Integer32
_SfrapEventTrapLogSeqNum_Object = MibTableColumn
sfrapEventTrapLogSeqNum = _SfrapEventTrapLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 1),
    _SfrapEventTrapLogSeqNum_Type()
)
sfrapEventTrapLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogSeqNum.setStatus("mandatory")
_SfrapEventTrapLogGenericEvent_Type = Integer32
_SfrapEventTrapLogGenericEvent_Object = MibTableColumn
sfrapEventTrapLogGenericEvent = _SfrapEventTrapLogGenericEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 2),
    _SfrapEventTrapLogGenericEvent_Type()
)
sfrapEventTrapLogGenericEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogGenericEvent.setStatus("mandatory")
_SfrapEventTrapLogSpecificEvent_Type = Integer32
_SfrapEventTrapLogSpecificEvent_Object = MibTableColumn
sfrapEventTrapLogSpecificEvent = _SfrapEventTrapLogSpecificEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 3),
    _SfrapEventTrapLogSpecificEvent_Type()
)
sfrapEventTrapLogSpecificEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogSpecificEvent.setStatus("mandatory")
_SfrapEventTrapLogTimeStamp_Type = TimeTicks
_SfrapEventTrapLogTimeStamp_Object = MibTableColumn
sfrapEventTrapLogTimeStamp = _SfrapEventTrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 4),
    _SfrapEventTrapLogTimeStamp_Type()
)
sfrapEventTrapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogTimeStamp.setStatus("mandatory")
_SfrapEventTrapLogVarBind1_Type = Integer32
_SfrapEventTrapLogVarBind1_Object = MibTableColumn
sfrapEventTrapLogVarBind1 = _SfrapEventTrapLogVarBind1_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 5),
    _SfrapEventTrapLogVarBind1_Type()
)
sfrapEventTrapLogVarBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogVarBind1.setStatus("mandatory")
_SfrapEventTrapLogVarBind2_Type = Integer32
_SfrapEventTrapLogVarBind2_Object = MibTableColumn
sfrapEventTrapLogVarBind2 = _SfrapEventTrapLogVarBind2_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 6),
    _SfrapEventTrapLogVarBind2_Type()
)
sfrapEventTrapLogVarBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogVarBind2.setStatus("mandatory")
_SfrapEventTrapLogVarBind3_Type = Integer32
_SfrapEventTrapLogVarBind3_Object = MibTableColumn
sfrapEventTrapLogVarBind3 = _SfrapEventTrapLogVarBind3_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 1, 1, 7),
    _SfrapEventTrapLogVarBind3_Type()
)
sfrapEventTrapLogVarBind3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventTrapLogVarBind3.setStatus("mandatory")
_SfrapEventLogAltTable_Object = MibTable
sfrapEventLogAltTable = _SfrapEventLogAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 2)
)
if mibBuilder.loadTexts:
    sfrapEventLogAltTable.setStatus("mandatory")
_SfrapEventLogAltEntry_Object = MibTableRow
sfrapEventLogAltEntry = _SfrapEventLogAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 2, 1)
)
sfrapEventLogAltEntry.setIndexNames(
    (0, "SFRAP-MIB", "sfrapEventLogAltSeqNum"),
)
if mibBuilder.loadTexts:
    sfrapEventLogAltEntry.setStatus("mandatory")
_SfrapEventLogAltSeqNum_Type = Integer32
_SfrapEventLogAltSeqNum_Object = MibTableColumn
sfrapEventLogAltSeqNum = _SfrapEventLogAltSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 2, 1, 1),
    _SfrapEventLogAltSeqNum_Type()
)
sfrapEventLogAltSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventLogAltSeqNum.setStatus("mandatory")
_SfrapEventLogAltArray_Type = OctetString
_SfrapEventLogAltArray_Object = MibTableColumn
sfrapEventLogAltArray = _SfrapEventLogAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 2, 1, 2),
    _SfrapEventLogAltArray_Type()
)
sfrapEventLogAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventLogAltArray.setStatus("mandatory")
_SfrapEventLogCurrentSeqNum_Type = Integer32
_SfrapEventLogCurrentSeqNum_Object = MibScalar
sfrapEventLogCurrentSeqNum = _SfrapEventLogCurrentSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 3),
    _SfrapEventLogCurrentSeqNum_Type()
)
sfrapEventLogCurrentSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapEventLogCurrentSeqNum.setStatus("mandatory")


class _SfrapEventLogFreeze_Type(Integer32):
    """Custom type sfrapEventLogFreeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freeze", 1),
          ("un-freeze", 2))
    )


_SfrapEventLogFreeze_Type.__name__ = "Integer32"
_SfrapEventLogFreeze_Object = MibScalar
sfrapEventLogFreeze = _SfrapEventLogFreeze_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 4),
    _SfrapEventLogFreeze_Type()
)
sfrapEventLogFreeze.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapEventLogFreeze.setStatus("mandatory")


class _SfrapEventLogClear_Type(Integer32):
    """Custom type sfrapEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_SfrapEventLogClear_Type.__name__ = "Integer32"
_SfrapEventLogClear_Object = MibScalar
sfrapEventLogClear = _SfrapEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 10, 5),
    _SfrapEventLogClear_Type()
)
sfrapEventLogClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfrapEventLogClear.setStatus("mandatory")
_SfrapPercentUtilization_Type = Integer32
_SfrapPercentUtilization_Object = MibScalar
sfrapPercentUtilization = _SfrapPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 11),
    _SfrapPercentUtilization_Type()
)
sfrapPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapPercentUtilization.setStatus("mandatory")
_SfrapUtilizationThreshold_Type = Integer32
_SfrapUtilizationThreshold_Object = MibScalar
sfrapUtilizationThreshold = _SfrapUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 12),
    _SfrapUtilizationThreshold_Type()
)
sfrapUtilizationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapUtilizationThreshold.setStatus("mandatory")
_SfrapCfgLockIpAddress_Type = Integer32
_SfrapCfgLockIpAddress_Object = MibScalar
sfrapCfgLockIpAddress = _SfrapCfgLockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 7, 13),
    _SfrapCfgLockIpAddress_Type()
)
sfrapCfgLockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfrapCfgLockIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sfrapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 0)
)
sfrapTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTrap.setStatus(
        ""
    )

sfrapBadConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 1)
)
sfrapBadConfigTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapBadConfigTrap.setStatus(
        ""
    )

sfrapLocalConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 2)
)
sfrapLocalConfigTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalConfigTrap.setStatus(
        ""
    )

sfrapLocalUnitLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 14)
)
sfrapLocalUnitLoopbackEnabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalUnitLoopbackEnabledTrap.setStatus(
        ""
    )

sfrapLocalUnitLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 15)
)
sfrapLocalUnitLoopbackDisabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalUnitLoopbackDisabledTrap.setStatus(
        ""
    )

sfrapLocalUnitLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 16)
)
sfrapLocalUnitLoopbackFailedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalUnitLoopbackFailedTrap.setStatus(
        ""
    )

sfrapLocalToDteLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 17)
)
sfrapLocalToDteLoopbackEnabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalToDteLoopbackEnabledTrap.setStatus(
        ""
    )

sfrapLocalToDteLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 18)
)
sfrapLocalToDteLoopbackDisabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalToDteLoopbackDisabledTrap.setStatus(
        ""
    )

sfrapLocalToDteLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 19)
)
sfrapLocalToDteLoopbackFailedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalToDteLoopbackFailedTrap.setStatus(
        ""
    )

sfrapDLCIActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 47)
)
sfrapDLCIActiveTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"))
)
if mibBuilder.loadTexts:
    sfrapDLCIActiveTrap.setStatus(
        ""
    )

sfrapDLCIInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 48)
)
sfrapDLCIInactiveTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"))
)
if mibBuilder.loadTexts:
    sfrapDLCIInactiveTrap.setStatus(
        ""
    )

sfrapDLCITDThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 49)
)
sfrapDLCITDThresholdTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapIpAddress"))
)
if mibBuilder.loadTexts:
    sfrapDLCITDThresholdTrap.setStatus(
        ""
    )

sfrapLmiSourcingChangePassthruTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 50)
)
sfrapLmiSourcingChangePassthruTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSourcingChangePassthruTrap.setStatus(
        ""
    )

sfrapLmiSourcingChangeUserToDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 51)
)
sfrapLmiSourcingChangeUserToDteTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSourcingChangeUserToDteTrap.setStatus(
        ""
    )

sfrapLmiSourcingChangeNetToDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 52)
)
sfrapLmiSourcingChangeNetToDteTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSourcingChangeNetToDteTrap.setStatus(
        ""
    )

sfrapLmiSourcingChangeUserToDceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 53)
)
sfrapLmiSourcingChangeUserToDceTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSourcingChangeUserToDceTrap.setStatus(
        ""
    )

sfrapLmiSourcingChangeNetToDceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 54)
)
sfrapLmiSourcingChangeNetToDceTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSourcingChangeNetToDceTrap.setStatus(
        ""
    )

sfrapDteSignalRtsOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 55)
)
sfrapDteSignalRtsOnTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalRtsOnTrap.setStatus(
        ""
    )

sfrapDteSignalRtsOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 56)
)
sfrapDteSignalRtsOffTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalRtsOffTrap.setStatus(
        ""
    )

sfrapDteSignalDtrOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 57)
)
sfrapDteSignalDtrOnTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalDtrOnTrap.setStatus(
        ""
    )

sfrapDteSignalDtrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 58)
)
sfrapDteSignalDtrOffTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalDtrOffTrap.setStatus(
        ""
    )

sfrapNonIncrLmiSeqNumToDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 59)
)
sfrapNonIncrLmiSeqNumToDteTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapNonIncrLmiSeqNumToDteTrap.setStatus(
        ""
    )

sfrapNonIncrLmiSeqNumToDceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 60)
)
sfrapNonIncrLmiSeqNumToDceTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapNonIncrLmiSeqNumToDceTrap.setStatus(
        ""
    )

sfrapLmiSeqNumMismatchToDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 61)
)
sfrapLmiSeqNumMismatchToDteTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSeqNumMismatchToDteTrap.setStatus(
        ""
    )

sfrapLmiSeqNumMismatchToDceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 62)
)
sfrapLmiSeqNumMismatchToDceTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLmiSeqNumMismatchToDceTrap.setStatus(
        ""
    )

sfrapTrapMutingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 75)
)
sfrapTrapMutingActive.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTrapMutingActive.setStatus(
        ""
    )

sfrapTrapMutingInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 76)
)
sfrapTrapMutingInactive.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTrapMutingInactive.setStatus(
        ""
    )

sfrapLowSpeedExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 80)
)
sfrapLowSpeedExceededTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLowSpeedExceededTrap.setStatus(
        ""
    )

sfrapLowSpeedResumedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 81)
)
sfrapLowSpeedResumedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLowSpeedResumedTrap.setStatus(
        ""
    )

sfrapOpModeCutThruEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 82)
)
sfrapOpModeCutThruEnabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapOpModeCutThruEnabledTrap.setStatus(
        ""
    )

sfrapOpModeCutThruDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 83)
)
sfrapOpModeCutThruDisabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapOpModeCutThruDisabledTrap.setStatus(
        ""
    )

sfrapLocalDte2LoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 84)
)
sfrapLocalDte2LoopbackEnabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalDte2LoopbackEnabledTrap.setStatus(
        ""
    )

sfrapLocalDte2LoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 85)
)
sfrapLocalDte2LoopbackDisabledTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalDte2LoopbackDisabledTrap.setStatus(
        ""
    )

sfrapLocalDte2LoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 86)
)
sfrapLocalDte2LoopbackFailedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapLocalDte2LoopbackFailedTrap.setStatus(
        ""
    )

sfrapVloopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 90)
)
sfrapVloopUp.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVloopUp.setStatus(
        ""
    )

sfrapVloopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 91)
)
sfrapVloopDown.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVloopDown.setStatus(
        ""
    )

sfrapVloopUpViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 92)
)
sfrapVloopUpViaRemote.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVloopUpViaRemote.setStatus(
        ""
    )

sfrapVloopDownViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 93)
)
sfrapVloopDownViaRemote.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVloopDownViaRemote.setStatus(
        ""
    )

sfrapVloopRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 94)
)
sfrapVloopRequestFailed.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVloopRequestFailed.setStatus(
        ""
    )

sfrapVbertStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 95)
)
sfrapVbertStarted.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVbertStarted.setStatus(
        ""
    )

sfrapVbertStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 96)
)
sfrapVbertStopped.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVbertStopped.setStatus(
        ""
    )

sfrapVbertRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 97)
)
sfrapVbertRequestFailed.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapInterface"))
)
if mibBuilder.loadTexts:
    sfrapVbertRequestFailed.setStatus(
        ""
    )

sfrapDteSignalControlOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 100)
)
sfrapDteSignalControlOnTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalControlOnTrap.setStatus(
        ""
    )

sfrapDteSignalControlOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 101)
)
sfrapDteSignalControlOffTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalControlOffTrap.setStatus(
        ""
    )

sfrapDteSignalIndicateOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 102)
)
sfrapDteSignalIndicateOnTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalIndicateOnTrap.setStatus(
        ""
    )

sfrapDteSignalIndicateOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 103)
)
sfrapDteSignalIndicateOffTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapDteSignalIndicateOffTrap.setStatus(
        ""
    )

sfrapPvcRxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 138)
)
sfrapPvcRxUtilizationExceededTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapPercentUtilization"),
        ("SFRAP-MIB", "sfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    sfrapPvcRxUtilizationExceededTrap.setStatus(
        ""
    )

sfrapPvcTxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 139)
)
sfrapPvcTxUtilizationExceededTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapPercentUtilization"),
        ("SFRAP-MIB", "sfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    sfrapPvcTxUtilizationExceededTrap.setStatus(
        ""
    )

sfrapPvcRxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 140)
)
sfrapPvcRxUtilizationClearedTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapPercentUtilization"),
        ("SFRAP-MIB", "sfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    sfrapPvcRxUtilizationClearedTrap.setStatus(
        ""
    )

sfrapPvcTxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 141)
)
sfrapPvcTxUtilizationClearedTrap.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapDLCINum"),
        ("SFRAP-MIB", "sfrapPercentUtilization"),
        ("SFRAP-MIB", "sfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    sfrapPvcTxUtilizationClearedTrap.setStatus(
        ""
    )

sfrapConfigInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 142)
)
sfrapConfigInstallSuccess.setObjects(
      *(("SFRAP-MIB", "sfrapAlarmType"),
        ("SFRAP-MIB", "sfrapCfgLockIpAddress"))
)
if mibBuilder.loadTexts:
    sfrapConfigInstallSuccess.setStatus(
        ""
    )

sfrapTftpRequestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 257)
)
sfrapTftpRequestedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpRequestedTrap.setStatus(
        ""
    )

sfrapTftpTransferringTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 258)
)
sfrapTftpTransferringTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpTransferringTrap.setStatus(
        ""
    )

sfrapTftpProgrammingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 259)
)
sfrapTftpProgrammingTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpProgrammingTrap.setStatus(
        ""
    )

sfrapTftpAbortedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 260)
)
sfrapTftpAbortedTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpAbortedTrap.setStatus(
        ""
    )

sfrapTftpSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 261)
)
sfrapTftpSuccessTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpSuccessTrap.setStatus(
        ""
    )

sfrapTftpHostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 262)
)
sfrapTftpHostUnreachableTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpHostUnreachableTrap.setStatus(
        ""
    )

sfrapTftpNoFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 263)
)
sfrapTftpNoFileTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpNoFileTrap.setStatus(
        ""
    )

sfrapTftpInvalidFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 264)
)
sfrapTftpInvalidFileTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpInvalidFileTrap.setStatus(
        ""
    )

sfrapTftpCorruptFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 7, 0, 265)
)
sfrapTftpCorruptFileTrap.setObjects(
    ("SFRAP-MIB", "sfrapAlarmType")
)
if mibBuilder.loadTexts:
    sfrapTftpCorruptFileTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFRAP-MIB",
    **{"Index": Index,
       "private": private,
       "enterprises": enterprises,
       "sync": sync,
       "sfrap": sfrap,
       "sfrapTrap": sfrapTrap,
       "sfrapBadConfigTrap": sfrapBadConfigTrap,
       "sfrapLocalConfigTrap": sfrapLocalConfigTrap,
       "sfrapLocalUnitLoopbackEnabledTrap": sfrapLocalUnitLoopbackEnabledTrap,
       "sfrapLocalUnitLoopbackDisabledTrap": sfrapLocalUnitLoopbackDisabledTrap,
       "sfrapLocalUnitLoopbackFailedTrap": sfrapLocalUnitLoopbackFailedTrap,
       "sfrapLocalToDteLoopbackEnabledTrap": sfrapLocalToDteLoopbackEnabledTrap,
       "sfrapLocalToDteLoopbackDisabledTrap": sfrapLocalToDteLoopbackDisabledTrap,
       "sfrapLocalToDteLoopbackFailedTrap": sfrapLocalToDteLoopbackFailedTrap,
       "sfrapDLCIActiveTrap": sfrapDLCIActiveTrap,
       "sfrapDLCIInactiveTrap": sfrapDLCIInactiveTrap,
       "sfrapDLCITDThresholdTrap": sfrapDLCITDThresholdTrap,
       "sfrapLmiSourcingChangePassthruTrap": sfrapLmiSourcingChangePassthruTrap,
       "sfrapLmiSourcingChangeUserToDteTrap": sfrapLmiSourcingChangeUserToDteTrap,
       "sfrapLmiSourcingChangeNetToDteTrap": sfrapLmiSourcingChangeNetToDteTrap,
       "sfrapLmiSourcingChangeUserToDceTrap": sfrapLmiSourcingChangeUserToDceTrap,
       "sfrapLmiSourcingChangeNetToDceTrap": sfrapLmiSourcingChangeNetToDceTrap,
       "sfrapDteSignalRtsOnTrap": sfrapDteSignalRtsOnTrap,
       "sfrapDteSignalRtsOffTrap": sfrapDteSignalRtsOffTrap,
       "sfrapDteSignalDtrOnTrap": sfrapDteSignalDtrOnTrap,
       "sfrapDteSignalDtrOffTrap": sfrapDteSignalDtrOffTrap,
       "sfrapNonIncrLmiSeqNumToDteTrap": sfrapNonIncrLmiSeqNumToDteTrap,
       "sfrapNonIncrLmiSeqNumToDceTrap": sfrapNonIncrLmiSeqNumToDceTrap,
       "sfrapLmiSeqNumMismatchToDteTrap": sfrapLmiSeqNumMismatchToDteTrap,
       "sfrapLmiSeqNumMismatchToDceTrap": sfrapLmiSeqNumMismatchToDceTrap,
       "sfrapTrapMutingActive": sfrapTrapMutingActive,
       "sfrapTrapMutingInactive": sfrapTrapMutingInactive,
       "sfrapLowSpeedExceededTrap": sfrapLowSpeedExceededTrap,
       "sfrapLowSpeedResumedTrap": sfrapLowSpeedResumedTrap,
       "sfrapOpModeCutThruEnabledTrap": sfrapOpModeCutThruEnabledTrap,
       "sfrapOpModeCutThruDisabledTrap": sfrapOpModeCutThruDisabledTrap,
       "sfrapLocalDte2LoopbackEnabledTrap": sfrapLocalDte2LoopbackEnabledTrap,
       "sfrapLocalDte2LoopbackDisabledTrap": sfrapLocalDte2LoopbackDisabledTrap,
       "sfrapLocalDte2LoopbackFailedTrap": sfrapLocalDte2LoopbackFailedTrap,
       "sfrapVloopUp": sfrapVloopUp,
       "sfrapVloopDown": sfrapVloopDown,
       "sfrapVloopUpViaRemote": sfrapVloopUpViaRemote,
       "sfrapVloopDownViaRemote": sfrapVloopDownViaRemote,
       "sfrapVloopRequestFailed": sfrapVloopRequestFailed,
       "sfrapVbertStarted": sfrapVbertStarted,
       "sfrapVbertStopped": sfrapVbertStopped,
       "sfrapVbertRequestFailed": sfrapVbertRequestFailed,
       "sfrapDteSignalControlOnTrap": sfrapDteSignalControlOnTrap,
       "sfrapDteSignalControlOffTrap": sfrapDteSignalControlOffTrap,
       "sfrapDteSignalIndicateOnTrap": sfrapDteSignalIndicateOnTrap,
       "sfrapDteSignalIndicateOffTrap": sfrapDteSignalIndicateOffTrap,
       "sfrapPvcRxUtilizationExceededTrap": sfrapPvcRxUtilizationExceededTrap,
       "sfrapPvcTxUtilizationExceededTrap": sfrapPvcTxUtilizationExceededTrap,
       "sfrapPvcRxUtilizationClearedTrap": sfrapPvcRxUtilizationClearedTrap,
       "sfrapPvcTxUtilizationClearedTrap": sfrapPvcTxUtilizationClearedTrap,
       "sfrapConfigInstallSuccess": sfrapConfigInstallSuccess,
       "sfrapTftpRequestedTrap": sfrapTftpRequestedTrap,
       "sfrapTftpTransferringTrap": sfrapTftpTransferringTrap,
       "sfrapTftpProgrammingTrap": sfrapTftpProgrammingTrap,
       "sfrapTftpAbortedTrap": sfrapTftpAbortedTrap,
       "sfrapTftpSuccessTrap": sfrapTftpSuccessTrap,
       "sfrapTftpHostUnreachableTrap": sfrapTftpHostUnreachableTrap,
       "sfrapTftpNoFileTrap": sfrapTftpNoFileTrap,
       "sfrapTftpInvalidFileTrap": sfrapTftpInvalidFileTrap,
       "sfrapTftpCorruptFileTrap": sfrapTftpCorruptFileTrap,
       "sfrapSystem": sfrapSystem,
       "sfrapSysTable": sfrapSysTable,
       "sfrapSysType": sfrapSysType,
       "sfrapSysSoftRev": sfrapSysSoftRev,
       "sfrapSysHardRev": sfrapSysHardRev,
       "sfrapSysNumToDteInstalled": sfrapSysNumToDteInstalled,
       "sfrapSysNumMaintInstalled": sfrapSysNumMaintInstalled,
       "sfrapSysName": sfrapSysName,
       "sfrapSysSerialNo": sfrapSysSerialNo,
       "sfrapSysResetNode": sfrapSysResetNode,
       "sfrapSysAmtMemoryInstalled": sfrapSysAmtMemoryInstalled,
       "sfrapSysLocation": sfrapSysLocation,
       "sfrapSysContact": sfrapSysContact,
       "sfrapSysNumToDceInstalled": sfrapSysNumToDceInstalled,
       "sfrapSysPrompt": sfrapSysPrompt,
       "sfrapSysBootRev": sfrapSysBootRev,
       "sfrapSysFeatureTable": sfrapSysFeatureTable,
       "sfrapSysSLIPSupported": sfrapSysSLIPSupported,
       "sfrapSysPPPSupported": sfrapSysPPPSupported,
       "sfrapSysRDOSupported": sfrapSysRDOSupported,
       "sfrapSysETHSupported": sfrapSysETHSupported,
       "sfrapSysTKRSupported": sfrapSysTKRSupported,
       "sfrapSysExtTimSupported": sfrapSysExtTimSupported,
       "sfrapSysBRISupported": sfrapSysBRISupported,
       "sfrapSysSelDTESupported": sfrapSysSelDTESupported,
       "sfrapSysMLSupported": sfrapSysMLSupported,
       "sfrapSysNumDlcisSupported": sfrapSysNumDlcisSupported,
       "sfrapSysLTFNumDlcis": sfrapSysLTFNumDlcis,
       "sfrapSysLTFNumProtocols": sfrapSysLTFNumProtocols,
       "sfrapSysNumUserProtocols": sfrapSysNumUserProtocols,
       "sfrapSysNumSnmpMgrs": sfrapSysNumSnmpMgrs,
       "sfrapSysNumDlciNames": sfrapSysNumDlciNames,
       "sfrapSysHighSpeedSupported": sfrapSysHighSpeedSupported,
       "sfrapConfiguration": sfrapConfiguration,
       "sfrapCfgMgmtTable": sfrapCfgMgmtTable,
       "sfrapCfgIpTable": sfrapCfgIpTable,
       "sfrapCfgIpMyIP": sfrapCfgIpMyIP,
       "sfrapCfgIpPeerIP": sfrapCfgIpPeerIP,
       "sfrapCfgIpMask": sfrapCfgIpMask,
       "sfrapCfgIpMaxMTU": sfrapCfgIpMaxMTU,
       "sfrapCfgIpChannel": sfrapCfgIpChannel,
       "sfrapCfgIpTelnetEnable": sfrapCfgIpTelnetEnable,
       "sfrapCfgIpTelnetAutoLogOut": sfrapCfgIpTelnetAutoLogOut,
       "sfrapCfgTftpTable": sfrapCfgTftpTable,
       "sfrapCfgTftpInitiate": sfrapCfgTftpInitiate,
       "sfrapCfgTftpIpAddress": sfrapCfgTftpIpAddress,
       "sfrapCfgTftpFilename": sfrapCfgTftpFilename,
       "sfrapCfgTftpInterface": sfrapCfgTftpInterface,
       "sfrapCfgTftpDlci": sfrapCfgTftpDlci,
       "sfrapCfgTftpStatus": sfrapCfgTftpStatus,
       "sfrapCfgTftpNumBytes": sfrapCfgTftpNumBytes,
       "sfrapCfgSnmpTable": sfrapCfgSnmpTable,
       "sfrapCfgSnmpFrTrap": sfrapCfgSnmpFrTrap,
       "sfrapCfgSnmpMgrTable": sfrapCfgSnmpMgrTable,
       "sfrapCfgSnmpMgrEntry": sfrapCfgSnmpMgrEntry,
       "sfrapCfgSnmpMgrIndex": sfrapCfgSnmpMgrIndex,
       "sfrapCfgSnmpMgrIP": sfrapCfgSnmpMgrIP,
       "sfrapCfgSnmpMgrInterface": sfrapCfgSnmpMgrInterface,
       "sfrapCfgSnmpMgrDlci": sfrapCfgSnmpMgrDlci,
       "sfrapCfgSnmpTrapMuting": sfrapCfgSnmpTrapMuting,
       "sfrapCfgSnmpUtilTrapEnable": sfrapCfgSnmpUtilTrapEnable,
       "sfrapCfgSnmpMgrClearN": sfrapCfgSnmpMgrClearN,
       "sfrapCfgCommTable": sfrapCfgCommTable,
       "sfrapCfgCommMode": sfrapCfgCommMode,
       "sfrapCfgCommBaud": sfrapCfgCommBaud,
       "sfrapCfgCommDataBits": sfrapCfgCommDataBits,
       "sfrapCfgCommStopBits": sfrapCfgCommStopBits,
       "sfrapCfgCommParity": sfrapCfgCommParity,
       "sfrapCfgCommFlowCtrl": sfrapCfgCommFlowCtrl,
       "sfrapCfgFrDLCITable": sfrapCfgFrDLCITable,
       "sfrapCfgFrDLCIMode": sfrapCfgFrDLCIMode,
       "sfrapCfgFrDLCIValue": sfrapCfgFrDLCIValue,
       "sfrapCfgFrDLCIEncap": sfrapCfgFrDLCIEncap,
       "sfrapCfgFrDLCIMgmtDE": sfrapCfgFrDLCIMgmtDE,
       "sfrapCfgAppTable": sfrapCfgAppTable,
       "sfrapCfgAppCircuitId": sfrapCfgAppCircuitId,
       "sfrapCfgAppType": sfrapCfgAppType,
       "sfrapCfgAppFormat": sfrapCfgAppFormat,
       "sfrapCfgAppLpbkTimeout": sfrapCfgAppLpbkTimeout,
       "sfrapCfgAppTxClkmode": sfrapCfgAppTxClkmode,
       "sfrapCfgAppTxtiming": sfrapCfgAppTxtiming,
       "sfrapCfgAppOperationMode": sfrapCfgAppOperationMode,
       "sfrapCfgAppCutthruTimeout": sfrapCfgAppCutthruTimeout,
       "sfrapCfgAppPerfBuffLimit": sfrapCfgAppPerfBuffLimit,
       "sfrapCfgDteTable": sfrapCfgDteTable,
       "sfrapCfgDteEntry": sfrapCfgDteEntry,
       "sfrapCfgDteIntfType": sfrapCfgDteIntfType,
       "sfrapCfgDteTxClockMode": sfrapCfgDteTxClockMode,
       "sfrapCfgDteRxClockMode": sfrapCfgDteRxClockMode,
       "sfrapCfgDteRtsC": sfrapCfgDteRtsC,
       "sfrapCfgDteIndex": sfrapCfgDteIndex,
       "sfrapCfgFrTable": sfrapCfgFrTable,
       "sfrapCfgFrAddrLen": sfrapCfgFrAddrLen,
       "sfrapCfgFrCrcMode": sfrapCfgFrCrcMode,
       "sfrapCfgFrLmiType": sfrapCfgFrLmiType,
       "sfrapCfgFrLmiInactivityTimeout": sfrapCfgFrLmiInactivityTimeout,
       "sfrapCfgFrLmiKeepaliveTimeout": sfrapCfgFrLmiKeepaliveTimeout,
       "sfrapCfgFrAddrResMode": sfrapCfgFrAddrResMode,
       "sfrapCfgFrAddrResInarpTimer": sfrapCfgFrAddrResInarpTimer,
       "sfrapCfgFrLmiFullStatus": sfrapCfgFrLmiFullStatus,
       "sfrapCfgFrAddrResDlcis": sfrapCfgFrAddrResDlcis,
       "sfrapCfgVnipTable": sfrapCfgVnipTable,
       "sfrapCfgVnipMode": sfrapCfgVnipMode,
       "sfrapCfgVnipInitTimer": sfrapCfgVnipInitTimer,
       "sfrapCfgVnipTxTimer": sfrapCfgVnipTxTimer,
       "sfrapCfgVnipRxTimer": sfrapCfgVnipRxTimer,
       "sfrapCfgVnipTransitDelayFrequency": sfrapCfgVnipTransitDelayFrequency,
       "sfrapCfgTransitDelayTable": sfrapCfgTransitDelayTable,
       "sfrapCfgTransitDelayEntry": sfrapCfgTransitDelayEntry,
       "sfrapCfgTransitDelayInterface": sfrapCfgTransitDelayInterface,
       "sfrapCfgTransitDelayDlciValue": sfrapCfgTransitDelayDlciValue,
       "sfrapCfgTransitDelayNumHops": sfrapCfgTransitDelayNumHops,
       "sfrapCfgTransitDelayRcvSummaryCancel": sfrapCfgTransitDelayRcvSummaryCancel,
       "sfrapCfgTransitDelayThreshold": sfrapCfgTransitDelayThreshold,
       "sfrapCfgTDDeleteTable": sfrapCfgTDDeleteTable,
       "sfrapCfgTDDeleteEntry": sfrapCfgTDDeleteEntry,
       "sfrapCfgTDDeleteInterface": sfrapCfgTDDeleteInterface,
       "sfrapCfgTDDeleteDlciValue": sfrapCfgTDDeleteDlciValue,
       "sfrapCfgTransitDelayTableClear": sfrapCfgTransitDelayTableClear,
       "sfrapCfgFrPerf": sfrapCfgFrPerf,
       "sfrapCfgFrPerfDlciNamesTable": sfrapCfgFrPerfDlciNamesTable,
       "sfrapCfgFrPerfDlciNamesEntry": sfrapCfgFrPerfDlciNamesEntry,
       "sfrapCfgFrPerfDlciNamesDlciValue": sfrapCfgFrPerfDlciNamesDlciValue,
       "sfrapCfgFrPerfDlciNamesDlciName": sfrapCfgFrPerfDlciNamesDlciName,
       "sfrapCfgFrPerfDlciNamesCirValue": sfrapCfgFrPerfDlciNamesCirValue,
       "sfrapCfgFrPerfDlciNamesCirType": sfrapCfgFrPerfDlciNamesCirType,
       "sfrapCfgFrPerfDlciNamesUtilThreshold": sfrapCfgFrPerfDlciNamesUtilThreshold,
       "sfrapCfgFrPerfDlciNamesEirValue": sfrapCfgFrPerfDlciNamesEirValue,
       "sfrapCfgFrPerfDlciNamesDelete": sfrapCfgFrPerfDlciNamesDelete,
       "sfrapCfgFrPerfTimers": sfrapCfgFrPerfTimers,
       "sfrapCfgFrPerfTimersSTInterval": sfrapCfgFrPerfTimersSTInterval,
       "sfrapCfgFrPerfTimersLTInterval": sfrapCfgFrPerfTimersLTInterval,
       "sfrapCfgFrPerfUserProtocolsTable": sfrapCfgFrPerfUserProtocolsTable,
       "sfrapCfgFrPerfUserProtocolsEntry": sfrapCfgFrPerfUserProtocolsEntry,
       "sfrapCfgFrPerfUserProtocolsIndex": sfrapCfgFrPerfUserProtocolsIndex,
       "sfrapCfgFrPerfUserProtocolsPortNum": sfrapCfgFrPerfUserProtocolsPortNum,
       "sfrapCfgFrPerfLTDlciFilterTable": sfrapCfgFrPerfLTDlciFilterTable,
       "sfrapCfgFrPerfLTDlciFilterEntry": sfrapCfgFrPerfLTDlciFilterEntry,
       "sfrapCfgFrPerfLTDlciFilterIndex": sfrapCfgFrPerfLTDlciFilterIndex,
       "sfrapCfgFrPerfLTDlciFilterDlciNum": sfrapCfgFrPerfLTDlciFilterDlciNum,
       "sfrapCfgFrPerfLTProtocolFilterTable": sfrapCfgFrPerfLTProtocolFilterTable,
       "sfrapCfgFrPerfLTProtocolFilterEntry": sfrapCfgFrPerfLTProtocolFilterEntry,
       "sfrapCfgFrPerfLTProtocolFilterIndex": sfrapCfgFrPerfLTProtocolFilterIndex,
       "sfrapCfgFrPerfLTProtocolFilterProtocol": sfrapCfgFrPerfLTProtocolFilterProtocol,
       "sfrapCfgFrPerfDlciDefaultUtilThreshold": sfrapCfgFrPerfDlciDefaultUtilThreshold,
       "sfrapCfgFrPerfDlciUtilDuration": sfrapCfgFrPerfDlciUtilDuration,
       "sfrapCfgFrPerfDlciNamesTableClear": sfrapCfgFrPerfDlciNamesTableClear,
       "sfrapCfgFrPerfUserProtocolsTableClear": sfrapCfgFrPerfUserProtocolsTableClear,
       "sfrapCfgFrPerfLTDlciFilterTableClear": sfrapCfgFrPerfLTDlciFilterTableClear,
       "sfrapCfgFrPerfLTProtocolFilterTableClear": sfrapCfgFrPerfLTProtocolFilterTableClear,
       "sfrapCfgFrPerfUnprovDlcisDelete": sfrapCfgFrPerfUnprovDlcisDelete,
       "sfrapCfgSecurityTable": sfrapCfgSecurityTable,
       "sfrapCfgTelnetCliPassword": sfrapCfgTelnetCliPassword,
       "sfrapCfgTftpPassword": sfrapCfgTftpPassword,
       "sfrapCfgCliPassword": sfrapCfgCliPassword,
       "sfrapCfgGetCommunityString": sfrapCfgGetCommunityString,
       "sfrapCfgSetCommunityString": sfrapCfgSetCommunityString,
       "sfrapCfgLock": sfrapCfgLock,
       "sfrapCfgLockID": sfrapCfgLockID,
       "sfrapCfgID": sfrapCfgID,
       "sfrapCfgStatus": sfrapCfgStatus,
       "sfrapCfgUnlock": sfrapCfgUnlock,
       "sfrapCfgUpdate": sfrapCfgUpdate,
       "sfrapDiagnostics": sfrapDiagnostics,
       "sfrapDiagUnitTable": sfrapDiagUnitTable,
       "sfrapDiagUnitLocLoop": sfrapDiagUnitLocLoop,
       "sfrapDiagUnitReset": sfrapDiagUnitReset,
       "sfrapDiagUnitTimeRemaining": sfrapDiagUnitTimeRemaining,
       "sfrapDiagUnitCutThru": sfrapDiagUnitCutThru,
       "sfrapDiagUnitCutThruTimeRemaining": sfrapDiagUnitCutThruTimeRemaining,
       "sfrapDiagDteTable": sfrapDiagDteTable,
       "sfrapDiagDteEntry": sfrapDiagDteEntry,
       "sfrapDiagDteLclLpbk": sfrapDiagDteLclLpbk,
       "sfrapDiagDteTimeRemaining": sfrapDiagDteTimeRemaining,
       "sfrapDiagDteIndex": sfrapDiagDteIndex,
       "sfrapDiagVnipTable": sfrapDiagVnipTable,
       "sfrapDiagVnipEntry": sfrapDiagVnipEntry,
       "sfrapDiagVnipInterface": sfrapDiagVnipInterface,
       "sfrapDiagVnipIndex": sfrapDiagVnipIndex,
       "sfrapDiagVnipDlci": sfrapDiagVnipDlci,
       "sfrapDiagVnipIpAddr": sfrapDiagVnipIpAddr,
       "sfrapDiagVLOOP": sfrapDiagVLOOP,
       "sfrapDiagVBERT": sfrapDiagVBERT,
       "sfrapDiagVBERTRate": sfrapDiagVBERTRate,
       "sfrapDiagVBERTSize": sfrapDiagVBERTSize,
       "sfrapDiagVBERTPktPercent": sfrapDiagVBERTPktPercent,
       "sfrapDiagVBERTTestPeriod": sfrapDiagVBERTTestPeriod,
       "sfrapDiagTxClockDetect": sfrapDiagTxClockDetect,
       "sfrapStatus": sfrapStatus,
       "sfrapVnipTopologyTable": sfrapVnipTopologyTable,
       "sfrapVnipTopologyEntry": sfrapVnipTopologyEntry,
       "sfrapVnipTopologyInterface": sfrapVnipTopologyInterface,
       "sfrapVnipTopologyIndex": sfrapVnipTopologyIndex,
       "sfrapVnipTopologyDlci": sfrapVnipTopologyDlci,
       "sfrapVnipTopologyIpAddr": sfrapVnipTopologyIpAddr,
       "sfrapVnipTopologyNumHops": sfrapVnipTopologyNumHops,
       "sfrapVnipTopologyLocalDlci": sfrapVnipTopologyLocalDlci,
       "sfrapVnipTopoTDNumSamples": sfrapVnipTopoTDNumSamples,
       "sfrapVnipTopoTDAvgDelay": sfrapVnipTopoTDAvgDelay,
       "sfrapVnipTopoTDMaxDelay": sfrapVnipTopoTDMaxDelay,
       "sfrapVnipTopoTDMinDelay": sfrapVnipTopoTDMinDelay,
       "sfrapVnipTopoTDLastDelay": sfrapVnipTopoTDLastDelay,
       "sfrapVnipTopoVLOOPStatus": sfrapVnipTopoVLOOPStatus,
       "sfrapVnipTopoVBERTStatus": sfrapVnipTopoVBERTStatus,
       "sfrapVnipTopoVBertTxDESetFrames": sfrapVnipTopoVBertTxDESetFrames,
       "sfrapVnipTopoVBertRxDESetFrames": sfrapVnipTopoVBertRxDESetFrames,
       "sfrapVnipTopoVBertTxDEClrFrames": sfrapVnipTopoVBertTxDEClrFrames,
       "sfrapVnipTopoVBertRxDEClrFrames": sfrapVnipTopoVBertRxDEClrFrames,
       "sfrapVnipTopoVBertTransitDelayMax": sfrapVnipTopoVBertTransitDelayMax,
       "sfrapVnipTopoVBertTransitDelayAvg": sfrapVnipTopoVBertTransitDelayAvg,
       "sfrapVnipTopoVBertTimeElapse": sfrapVnipTopoVBertTimeElapse,
       "sfrapVnipTopoVBertPerUtilCIR": sfrapVnipTopoVBertPerUtilCIR,
       "sfrapVnipTopoVBertPerUtilEIR": sfrapVnipTopoVBertPerUtilEIR,
       "sfrapStatusMgmtTable": sfrapStatusMgmtTable,
       "sfrapStatusMgmtChannel": sfrapStatusMgmtChannel,
       "sfrapStatusMgmtInterface": sfrapStatusMgmtInterface,
       "sfrapStatusMgmtInterfaceStatus": sfrapStatusMgmtInterfaceStatus,
       "sfrapStatusMgmtDefaultDLCINo": sfrapStatusMgmtDefaultDLCINo,
       "sfrapStatusMgmtDefaultDLCIStatus": sfrapStatusMgmtDefaultDLCIStatus,
       "sfrapStatusLedTable": sfrapStatusLedTable,
       "sfrapStatusLedOpStatusLED": sfrapStatusLedOpStatusLED,
       "sfrapStatusLedToDTETxLED": sfrapStatusLedToDTETxLED,
       "sfrapStatusLedToDTERxLED": sfrapStatusLedToDTERxLED,
       "sfrapStatusLedRtsLED": sfrapStatusLedRtsLED,
       "sfrapStatusLedCtsLED": sfrapStatusLedCtsLED,
       "sfrapStatusLedDsrLED": sfrapStatusLedDsrLED,
       "sfrapStatusLedDcdLED": sfrapStatusLedDcdLED,
       "sfrapStatusLedToDCETxLED": sfrapStatusLedToDCETxLED,
       "sfrapStatusLedToDCERxLED": sfrapStatusLedToDCERxLED,
       "sfrapStatusAllLEDs": sfrapStatusAllLEDs,
       "sfrapStatusLedLmiErrLED": sfrapStatusLedLmiErrLED,
       "sfrapStatusLedFrmActLED": sfrapStatusLedFrmActLED,
       "sfrapStatusLedCtrlLED": sfrapStatusLedCtrlLED,
       "sfrapStatusLedIndLED": sfrapStatusLedIndLED,
       "sfrapVnipTransitDelayClear": sfrapVnipTransitDelayClear,
       "sfrapLmiSourcing": sfrapLmiSourcing,
       "sfrapStatusDteTable": sfrapStatusDteTable,
       "sfrapStatusDteEntry": sfrapStatusDteEntry,
       "sfrapStatusDteMode": sfrapStatusDteMode,
       "sfrapStatusDteRts": sfrapStatusDteRts,
       "sfrapStatusDteDtr": sfrapStatusDteDtr,
       "sfrapStatusDteDcd": sfrapStatusDteDcd,
       "sfrapStatusDteDsr": sfrapStatusDteDsr,
       "sfrapStatusDteCts": sfrapStatusDteCts,
       "sfrapStatusDteSendtiming": sfrapStatusDteSendtiming,
       "sfrapStatusDteRxtiming": sfrapStatusDteRxtiming,
       "sfrapStatusDteTermtiming": sfrapStatusDteTermtiming,
       "sfrapStatusDteCtrl": sfrapStatusDteCtrl,
       "sfrapStatusDteInd": sfrapStatusDteInd,
       "sfrapStatusDteIndex": sfrapStatusDteIndex,
       "sfrapStatusClockRate": sfrapStatusClockRate,
       "sfrapStatusToDteRxClockMode": sfrapStatusToDteRxClockMode,
       "sfrapStatusDipswitchTable": sfrapStatusDipswitchTable,
       "sfrapStatusDipswitchCutthru": sfrapStatusDipswitchCutthru,
       "sfrapStatusDipswitchToDteLpbk": sfrapStatusDipswitchToDteLpbk,
       "sfrapStatusDipswitchToDceLpbk": sfrapStatusDipswitchToDceLpbk,
       "sfrapStatusDipswitchUnused": sfrapStatusDipswitchUnused,
       "sfrapStatusDipswitchIntfMode1": sfrapStatusDipswitchIntfMode1,
       "sfrapStatusDipswitchIntfMode2": sfrapStatusDipswitchIntfMode2,
       "sfrapVBertClear": sfrapVBertClear,
       "sfrapStatusLmiAutosense": sfrapStatusLmiAutosense,
       "sfrapStatusTxClockDetect": sfrapStatusTxClockDetect,
       "sfrapPerformance": sfrapPerformance,
       "sfrapPerfMgmtIp": sfrapPerfMgmtIp,
       "sfrapPerfMgmtIpIFStatsTable": sfrapPerfMgmtIpIFStatsTable,
       "sfrapPerfMgmtIpIFInOctets": sfrapPerfMgmtIpIFInOctets,
       "sfrapPerfMgmtIpIFInErrors": sfrapPerfMgmtIpIFInErrors,
       "sfrapPerfMgmtIpIFOutOctets": sfrapPerfMgmtIpIFOutOctets,
       "sfrapPerfMgmtIpIFOperStatus": sfrapPerfMgmtIpIFOperStatus,
       "sfrapPerfMgmtIpIPStatsTable": sfrapPerfMgmtIpIPStatsTable,
       "sfrapPerfMgmtIpIPInRcv": sfrapPerfMgmtIpIPInRcv,
       "sfrapPerfMgmtIpIPInHdrErr": sfrapPerfMgmtIpIPInHdrErr,
       "sfrapPerfMgmtIpIPInAddrErr": sfrapPerfMgmtIpIPInAddrErr,
       "sfrapPerfMgmtIpIPInProtUnk": sfrapPerfMgmtIpIPInProtUnk,
       "sfrapPerfMgmtIpIPInDscrd": sfrapPerfMgmtIpIPInDscrd,
       "sfrapPerfMgmtIpIPInDlvrs": sfrapPerfMgmtIpIPInDlvrs,
       "sfrapPerfMgmtIpIPOutRqst": sfrapPerfMgmtIpIPOutRqst,
       "sfrapPerfMgmtIpIPOutDscrd": sfrapPerfMgmtIpIPOutDscrd,
       "sfrapPerfMgmtIpIPOutNoRt": sfrapPerfMgmtIpIPOutNoRt,
       "sfrapPerfMgmtIpICMPStatsTable": sfrapPerfMgmtIpICMPStatsTable,
       "sfrapPerfMgmtIpICMPInMsgs": sfrapPerfMgmtIpICMPInMsgs,
       "sfrapPerfMgmtIpICMPInErrors": sfrapPerfMgmtIpICMPInErrors,
       "sfrapPerfMgmtIpICMPInDestUnreachs": sfrapPerfMgmtIpICMPInDestUnreachs,
       "sfrapPerfMgmtIpICMPInTimeExcds": sfrapPerfMgmtIpICMPInTimeExcds,
       "sfrapPerfMgmtIpICMPInParmProbs": sfrapPerfMgmtIpICMPInParmProbs,
       "sfrapPerfMgmtIpICMPInRedirects": sfrapPerfMgmtIpICMPInRedirects,
       "sfrapPerfMgmtIpICMPInEchos": sfrapPerfMgmtIpICMPInEchos,
       "sfrapPerfMgmtIpICMPInEchoReps": sfrapPerfMgmtIpICMPInEchoReps,
       "sfrapPerfMgmtIpICMPOutMsgs": sfrapPerfMgmtIpICMPOutMsgs,
       "sfrapPerfMgmtIpICMPOutErrors": sfrapPerfMgmtIpICMPOutErrors,
       "sfrapPerfMgmtIpICMPOutDestUnreachs": sfrapPerfMgmtIpICMPOutDestUnreachs,
       "sfrapPerfMgmtIpICMPOutParmProbs": sfrapPerfMgmtIpICMPOutParmProbs,
       "sfrapPerfMgmtIpICMPOutRedirects": sfrapPerfMgmtIpICMPOutRedirects,
       "sfrapPerfMgmtIpICMPOutEchos": sfrapPerfMgmtIpICMPOutEchos,
       "sfrapPerfMgmtIpICMPOutEchoReps": sfrapPerfMgmtIpICMPOutEchoReps,
       "sfrapPerfMgmtIpUDPStatsTable": sfrapPerfMgmtIpUDPStatsTable,
       "sfrapPerfMgmtIpUDPInDatagrams": sfrapPerfMgmtIpUDPInDatagrams,
       "sfrapPerfMgmtIpUDPOutDatagrams": sfrapPerfMgmtIpUDPOutDatagrams,
       "sfrapPerfMgmtIpUDPNoPorts": sfrapPerfMgmtIpUDPNoPorts,
       "sfrapPerfMgmtIpTCPStatsTable": sfrapPerfMgmtIpTCPStatsTable,
       "sfrapPerfMgmtIpTCPActiveOpens": sfrapPerfMgmtIpTCPActiveOpens,
       "sfrapPerfMgmtIpTCPPassiveOpens": sfrapPerfMgmtIpTCPPassiveOpens,
       "sfrapPerfMgmtIpTCPAttemptFails": sfrapPerfMgmtIpTCPAttemptFails,
       "sfrapPerfMgmtIpTCPCurrEstab": sfrapPerfMgmtIpTCPCurrEstab,
       "sfrapPerfMgmtIpTCPInSegs": sfrapPerfMgmtIpTCPInSegs,
       "sfrapPerfMgmtIpTCPOutSegs": sfrapPerfMgmtIpTCPOutSegs,
       "sfrapPerfThruput": sfrapPerfThruput,
       "sfrapPerfThruputPerIntfTable": sfrapPerfThruputPerIntfTable,
       "sfrapPerfThruputPerIntfEntry": sfrapPerfThruputPerIntfEntry,
       "sfrapPerfThruputPerIntfIndex": sfrapPerfThruputPerIntfIndex,
       "sfrapPerfThruputPerIntfRxByteCnt": sfrapPerfThruputPerIntfRxByteCnt,
       "sfrapPerfThruputPerIntfTxByteCnt": sfrapPerfThruputPerIntfTxByteCnt,
       "sfrapPerfThruputPerIntfRxFrameCnt": sfrapPerfThruputPerIntfRxFrameCnt,
       "sfrapPerfThruputPerIntfTxFrameCnt": sfrapPerfThruputPerIntfTxFrameCnt,
       "sfrapPerfThruputPerIntfRxCrcErrCnt": sfrapPerfThruputPerIntfRxCrcErrCnt,
       "sfrapPerfThruputPerIntfRxAbortCnt": sfrapPerfThruputPerIntfRxAbortCnt,
       "sfrapPerfThruputPerIntfRxBpvCnt": sfrapPerfThruputPerIntfRxBpvCnt,
       "sfrapPerfThruputPerDlciTable": sfrapPerfThruputPerDlciTable,
       "sfrapPerfThruputPerDlciEntry": sfrapPerfThruputPerDlciEntry,
       "sfrapPerfThruputPerDlciIndex": sfrapPerfThruputPerDlciIndex,
       "sfrapPerfThruputPerDlciValue": sfrapPerfThruputPerDlciValue,
       "sfrapPerfThruputPerDlciCreateTime": sfrapPerfThruputPerDlciCreateTime,
       "sfrapPerfThruputPerDlciChangeTime": sfrapPerfThruputPerDlciChangeTime,
       "sfrapPerfThruputPerDlciRxByte": sfrapPerfThruputPerDlciRxByte,
       "sfrapPerfThruputPerDlciTxByte": sfrapPerfThruputPerDlciTxByte,
       "sfrapPerfThruputPerDlciRxFrame": sfrapPerfThruputPerDlciRxFrame,
       "sfrapPerfThruputPerDlciTxFrame": sfrapPerfThruputPerDlciTxFrame,
       "sfrapPerfThruputPerDlciRxFecn": sfrapPerfThruputPerDlciRxFecn,
       "sfrapPerfThruputPerDlciRxBecn": sfrapPerfThruputPerDlciRxBecn,
       "sfrapPerfThruputPerDlciRxDe": sfrapPerfThruputPerDlciRxDe,
       "sfrapPerfThruputPerDlciTxDe": sfrapPerfThruputPerDlciTxDe,
       "sfrapPerfThruputPerDlciRxThruput": sfrapPerfThruputPerDlciRxThruput,
       "sfrapPerfThruputPerDlciTxThruput": sfrapPerfThruputPerDlciTxThruput,
       "sfrapPerfThruputPerDlciCIR": sfrapPerfThruputPerDlciCIR,
       "sfrapPerfThruputPerDlciUptime": sfrapPerfThruputPerDlciUptime,
       "sfrapPerfThruputPerDlciDowntime": sfrapPerfThruputPerDlciDowntime,
       "sfrapPerfThruputPerDlciCirType": sfrapPerfThruputPerDlciCirType,
       "sfrapPerfThruputPerDlciPvcState": sfrapPerfThruputPerDlciPvcState,
       "sfrapPerfThruputPerDlciOutageCount": sfrapPerfThruputPerDlciOutageCount,
       "sfrapPerfThruputPerDlciAvailability": sfrapPerfThruputPerDlciAvailability,
       "sfrapPerfThruputPerDlciMTBSO": sfrapPerfThruputPerDlciMTBSO,
       "sfrapPerfThruputPerDlciMTTSR": sfrapPerfThruputPerDlciMTTSR,
       "sfrapPerfThruputPerDlciEncapType": sfrapPerfThruputPerDlciEncapType,
       "sfrapPerfThruputPerDlciRxUtilizationStatus": sfrapPerfThruputPerDlciRxUtilizationStatus,
       "sfrapPerfThruputPerDlciTxUtilizationStatus": sfrapPerfThruputPerDlciTxUtilizationStatus,
       "sfrapPerfThruputPerDlciEIR": sfrapPerfThruputPerDlciEIR,
       "sfrapPerfThruputCommands": sfrapPerfThruputCommands,
       "sfrapPerfThruputCmdClearToDteStats": sfrapPerfThruputCmdClearToDteStats,
       "sfrapPerfThruputCmdClearToDceStats": sfrapPerfThruputCmdClearToDceStats,
       "sfrapPerfThruputCmdClearAllIntfStats": sfrapPerfThruputCmdClearAllIntfStats,
       "sfrapPerfThruputCmdClearDlciStats": sfrapPerfThruputCmdClearDlciStats,
       "sfrapPerfThruputCmdClearAllStats": sfrapPerfThruputCmdClearAllStats,
       "sfrapPerfThruputCmdRemoveStsDlci": sfrapPerfThruputCmdRemoveStsDlci,
       "sfrapPerfThruputCmdReplaceDlciTable": sfrapPerfThruputCmdReplaceDlciTable,
       "sfrapPerfThruputCmdReplaceDlciEntry": sfrapPerfThruputCmdReplaceDlciEntry,
       "sfrapPerfThruputCmdReplaceDlciValue": sfrapPerfThruputCmdReplaceDlciValue,
       "sfrapPerfThruputCmdReplaceDlciNewValue": sfrapPerfThruputCmdReplaceDlciNewValue,
       "sfrapPerfThruputCmdAvailabilityStsDlciReset": sfrapPerfThruputCmdAvailabilityStsDlciReset,
       "sfrapPerfThruputCmdAvailabilityStsDlciResetAll": sfrapPerfThruputCmdAvailabilityStsDlciResetAll,
       "sfrapPerfThruputCmdCountsStsDlciReset": sfrapPerfThruputCmdCountsStsDlciReset,
       "sfrapPerfThruputCmdCountsStsDlciResetAll": sfrapPerfThruputCmdCountsStsDlciResetAll,
       "sfrapPerfThruputCmdAllStsDlciReset": sfrapPerfThruputCmdAllStsDlciReset,
       "sfrapPerfThruputCmdAllStsDlciResetAll": sfrapPerfThruputCmdAllStsDlciResetAll,
       "sfrapPerfNetworkShortTerm": sfrapPerfNetworkShortTerm,
       "sfrapPerfNetwProtoPerDlciTable": sfrapPerfNetwProtoPerDlciTable,
       "sfrapPerfNetwProtoPerDlciEntry": sfrapPerfNetwProtoPerDlciEntry,
       "sfrapPerfNetwProtoPerDlciInterval": sfrapPerfNetwProtoPerDlciInterval,
       "sfrapPerfNetwProtoPerDlciValue": sfrapPerfNetwProtoPerDlciValue,
       "sfrapPerfNetwProtoPerDlciRxTotal": sfrapPerfNetwProtoPerDlciRxTotal,
       "sfrapPerfNetwProtoPerDlciTxTotal": sfrapPerfNetwProtoPerDlciTxTotal,
       "sfrapPerfNetwProtoPerDlciRxIp": sfrapPerfNetwProtoPerDlciRxIp,
       "sfrapPerfNetwProtoPerDlciTxIp": sfrapPerfNetwProtoPerDlciTxIp,
       "sfrapPerfNetwProtoPerDlciRxIpx": sfrapPerfNetwProtoPerDlciRxIpx,
       "sfrapPerfNetwProtoPerDlciTxIpx": sfrapPerfNetwProtoPerDlciTxIpx,
       "sfrapPerfNetwProtoPerDlciRxSna": sfrapPerfNetwProtoPerDlciRxSna,
       "sfrapPerfNetwProtoPerDlciTxSna": sfrapPerfNetwProtoPerDlciTxSna,
       "sfrapPerfNetwProtoPerDlciRxArp": sfrapPerfNetwProtoPerDlciRxArp,
       "sfrapPerfNetwProtoPerDlciTxArp": sfrapPerfNetwProtoPerDlciTxArp,
       "sfrapPerfNetwProtoPerDlciRxCisco": sfrapPerfNetwProtoPerDlciRxCisco,
       "sfrapPerfNetwProtoPerDlciTxCisco": sfrapPerfNetwProtoPerDlciTxCisco,
       "sfrapPerfNetwProtoPerDlciRxOther": sfrapPerfNetwProtoPerDlciRxOther,
       "sfrapPerfNetwProtoPerDlciTxOther": sfrapPerfNetwProtoPerDlciTxOther,
       "sfrapPerfNetwProtoPerDlciRxVnip": sfrapPerfNetwProtoPerDlciRxVnip,
       "sfrapPerfNetwProtoPerDlciTxVnip": sfrapPerfNetwProtoPerDlciTxVnip,
       "sfrapPerfNetwProtoPerDlciRxAnnexG": sfrapPerfNetwProtoPerDlciRxAnnexG,
       "sfrapPerfNetwProtoPerDlciTxAnnexG": sfrapPerfNetwProtoPerDlciTxAnnexG,
       "sfrapPerfNetwProtoTotalTable": sfrapPerfNetwProtoTotalTable,
       "sfrapPerfNetwProtoTotalEntry": sfrapPerfNetwProtoTotalEntry,
       "sfrapPerfNetwProtoTotalInterval": sfrapPerfNetwProtoTotalInterval,
       "sfrapPerfNetwProtoTotalRxTotal": sfrapPerfNetwProtoTotalRxTotal,
       "sfrapPerfNetwProtoTotalTxTotal": sfrapPerfNetwProtoTotalTxTotal,
       "sfrapPerfNetwProtoTotalRxIp": sfrapPerfNetwProtoTotalRxIp,
       "sfrapPerfNetwProtoTotalTxIp": sfrapPerfNetwProtoTotalTxIp,
       "sfrapPerfNetwProtoTotalRxIpx": sfrapPerfNetwProtoTotalRxIpx,
       "sfrapPerfNetwProtoTotalTxIpx": sfrapPerfNetwProtoTotalTxIpx,
       "sfrapPerfNetwProtoTotalRxSna": sfrapPerfNetwProtoTotalRxSna,
       "sfrapPerfNetwProtoTotalTxSna": sfrapPerfNetwProtoTotalTxSna,
       "sfrapPerfNetwProtoTotalRxArp": sfrapPerfNetwProtoTotalRxArp,
       "sfrapPerfNetwProtoTotalTxArp": sfrapPerfNetwProtoTotalTxArp,
       "sfrapPerfNetwProtoTotalRxCisco": sfrapPerfNetwProtoTotalRxCisco,
       "sfrapPerfNetwProtoTotalTxCisco": sfrapPerfNetwProtoTotalTxCisco,
       "sfrapPerfNetwProtoTotalRxOther": sfrapPerfNetwProtoTotalRxOther,
       "sfrapPerfNetwProtoTotalTxOther": sfrapPerfNetwProtoTotalTxOther,
       "sfrapPerfNetwProtoTotalRxVnip": sfrapPerfNetwProtoTotalRxVnip,
       "sfrapPerfNetwProtoTotalTxVnip": sfrapPerfNetwProtoTotalTxVnip,
       "sfrapPerfNetwProtoTotalRxAnnexG": sfrapPerfNetwProtoTotalRxAnnexG,
       "sfrapPerfNetwProtoTotalTxAnnexG": sfrapPerfNetwProtoTotalTxAnnexG,
       "sfrapPerfIpPerDlciTable": sfrapPerfIpPerDlciTable,
       "sfrapPerfIpPerDlciEntry": sfrapPerfIpPerDlciEntry,
       "sfrapPerfIpPerDlciInterval": sfrapPerfIpPerDlciInterval,
       "sfrapPerfIpPerDlciValue": sfrapPerfIpPerDlciValue,
       "sfrapPerfIpPerDlciRxTotal": sfrapPerfIpPerDlciRxTotal,
       "sfrapPerfIpPerDlciTxTotal": sfrapPerfIpPerDlciTxTotal,
       "sfrapPerfIpPerDlciRxTcp": sfrapPerfIpPerDlciRxTcp,
       "sfrapPerfIpPerDlciTxTcp": sfrapPerfIpPerDlciTxTcp,
       "sfrapPerfIpPerDlciRxUdp": sfrapPerfIpPerDlciRxUdp,
       "sfrapPerfIpPerDlciTxUdp": sfrapPerfIpPerDlciTxUdp,
       "sfrapPerfIpPerDlciRxIcmp": sfrapPerfIpPerDlciRxIcmp,
       "sfrapPerfIpPerDlciTxIcmp": sfrapPerfIpPerDlciTxIcmp,
       "sfrapPerfIpPerDlciRxOther": sfrapPerfIpPerDlciRxOther,
       "sfrapPerfIpPerDlciTxOther": sfrapPerfIpPerDlciTxOther,
       "sfrapPerfIpPerDlciRxIgrp": sfrapPerfIpPerDlciRxIgrp,
       "sfrapPerfIpPerDlciTxIgrp": sfrapPerfIpPerDlciTxIgrp,
       "sfrapPerfIpTotalTable": sfrapPerfIpTotalTable,
       "sfrapPerfIpTotalEntry": sfrapPerfIpTotalEntry,
       "sfrapPerfIpTotalInterval": sfrapPerfIpTotalInterval,
       "sfrapPerfIpTotalRxTotal": sfrapPerfIpTotalRxTotal,
       "sfrapPerfIpTotalTxTotal": sfrapPerfIpTotalTxTotal,
       "sfrapPerfIpTotalRxTcp": sfrapPerfIpTotalRxTcp,
       "sfrapPerfIpTotalTxTcp": sfrapPerfIpTotalTxTcp,
       "sfrapPerfIpTotalRxUdp": sfrapPerfIpTotalRxUdp,
       "sfrapPerfIpTotalTxUdp": sfrapPerfIpTotalTxUdp,
       "sfrapPerfIpTotalRxIcmp": sfrapPerfIpTotalRxIcmp,
       "sfrapPerfIpTotalTxIcmp": sfrapPerfIpTotalTxIcmp,
       "sfrapPerfIpTotalRxOther": sfrapPerfIpTotalRxOther,
       "sfrapPerfIpTotalTxOther": sfrapPerfIpTotalTxOther,
       "sfrapPerfIpTotalRxIgrp": sfrapPerfIpTotalRxIgrp,
       "sfrapPerfIpTotalTxIgrp": sfrapPerfIpTotalTxIgrp,
       "sfrapPerfIcmpPerDlciTable": sfrapPerfIcmpPerDlciTable,
       "sfrapPerfIcmpPerDlciEntry": sfrapPerfIcmpPerDlciEntry,
       "sfrapPerfIcmpPerDlciInterval": sfrapPerfIcmpPerDlciInterval,
       "sfrapPerfIcmpPerDlciValue": sfrapPerfIcmpPerDlciValue,
       "sfrapPerfIcmpPerDlciRxTotal": sfrapPerfIcmpPerDlciRxTotal,
       "sfrapPerfIcmpPerDlciTxTotal": sfrapPerfIcmpPerDlciTxTotal,
       "sfrapPerfIcmpPerDlciRxEchoRep": sfrapPerfIcmpPerDlciRxEchoRep,
       "sfrapPerfIcmpPerDlciTxEchoRep": sfrapPerfIcmpPerDlciTxEchoRep,
       "sfrapPerfIcmpPerDlciRxDestUnr": sfrapPerfIcmpPerDlciRxDestUnr,
       "sfrapPerfIcmpPerDlciTxDestUnr": sfrapPerfIcmpPerDlciTxDestUnr,
       "sfrapPerfIcmpPerDlciRxSrcQuench": sfrapPerfIcmpPerDlciRxSrcQuench,
       "sfrapPerfIcmpPerDlciTxSrcQuench": sfrapPerfIcmpPerDlciTxSrcQuench,
       "sfrapPerfIcmpPerDlciRxRedirect": sfrapPerfIcmpPerDlciRxRedirect,
       "sfrapPerfIcmpPerDlciTxRedirect": sfrapPerfIcmpPerDlciTxRedirect,
       "sfrapPerfIcmpPerDlciRxEchoReq": sfrapPerfIcmpPerDlciRxEchoReq,
       "sfrapPerfIcmpPerDlciTxEchoReq": sfrapPerfIcmpPerDlciTxEchoReq,
       "sfrapPerfIcmpPerDlciRxTimeExcd": sfrapPerfIcmpPerDlciRxTimeExcd,
       "sfrapPerfIcmpPerDlciTxTimeExcd": sfrapPerfIcmpPerDlciTxTimeExcd,
       "sfrapPerfIcmpPerDlciRxParamProb": sfrapPerfIcmpPerDlciRxParamProb,
       "sfrapPerfIcmpPerDlciTxParamProb": sfrapPerfIcmpPerDlciTxParamProb,
       "sfrapPerfIcmpPerDlciRxTimestpReq": sfrapPerfIcmpPerDlciRxTimestpReq,
       "sfrapPerfIcmpPerDlciTxTimestpReq": sfrapPerfIcmpPerDlciTxTimestpReq,
       "sfrapPerfIcmpPerDlciRxTimestpRep": sfrapPerfIcmpPerDlciRxTimestpRep,
       "sfrapPerfIcmpPerDlciTxTimestpRep": sfrapPerfIcmpPerDlciTxTimestpRep,
       "sfrapPerfIcmpPerDlciRxAddrMaskReq": sfrapPerfIcmpPerDlciRxAddrMaskReq,
       "sfrapPerfIcmpPerDlciTxAddrMaskReq": sfrapPerfIcmpPerDlciTxAddrMaskReq,
       "sfrapPerfIcmpPerDlciRxAddrMaskRep": sfrapPerfIcmpPerDlciRxAddrMaskRep,
       "sfrapPerfIcmpPerDlciTxAddrMaskRep": sfrapPerfIcmpPerDlciTxAddrMaskRep,
       "sfrapPerfIcmpPerDlciRxPktTooBig": sfrapPerfIcmpPerDlciRxPktTooBig,
       "sfrapPerfIcmpPerDlciTxPktTooBig": sfrapPerfIcmpPerDlciTxPktTooBig,
       "sfrapPerfIcmpPerDlciRxGmQuery": sfrapPerfIcmpPerDlciRxGmQuery,
       "sfrapPerfIcmpPerDlciTxGmQuery": sfrapPerfIcmpPerDlciTxGmQuery,
       "sfrapPerfIcmpPerDlciRxGmReport": sfrapPerfIcmpPerDlciRxGmReport,
       "sfrapPerfIcmpPerDlciTxGmReport": sfrapPerfIcmpPerDlciTxGmReport,
       "sfrapPerfIcmpPerDlciRxGmReduct": sfrapPerfIcmpPerDlciRxGmReduct,
       "sfrapPerfIcmpPerDlciTxGmReduct": sfrapPerfIcmpPerDlciTxGmReduct,
       "sfrapPerfIcmpTotalTable": sfrapPerfIcmpTotalTable,
       "sfrapPerfIcmpTotalEntry": sfrapPerfIcmpTotalEntry,
       "sfrapPerfIcmpTotalInterval": sfrapPerfIcmpTotalInterval,
       "sfrapPerfIcmpTotalRxTotal": sfrapPerfIcmpTotalRxTotal,
       "sfrapPerfIcmpTotalTxTotal": sfrapPerfIcmpTotalTxTotal,
       "sfrapPerfIcmpTotalRxEchoRep": sfrapPerfIcmpTotalRxEchoRep,
       "sfrapPerfIcmpTotalTxEchoRep": sfrapPerfIcmpTotalTxEchoRep,
       "sfrapPerfIcmpTotalRxDestUnr": sfrapPerfIcmpTotalRxDestUnr,
       "sfrapPerfIcmpTotalTxDestUnr": sfrapPerfIcmpTotalTxDestUnr,
       "sfrapPerfIcmpTotalRxSrcQuench": sfrapPerfIcmpTotalRxSrcQuench,
       "sfrapPerfIcmpTotalTxSrcQuench": sfrapPerfIcmpTotalTxSrcQuench,
       "sfrapPerfIcmpTotalRxRedirect": sfrapPerfIcmpTotalRxRedirect,
       "sfrapPerfIcmpTotalTxRedirect": sfrapPerfIcmpTotalTxRedirect,
       "sfrapPerfIcmpTotalRxEchoReq": sfrapPerfIcmpTotalRxEchoReq,
       "sfrapPerfIcmpTotalTxEchoReq": sfrapPerfIcmpTotalTxEchoReq,
       "sfrapPerfIcmpTotalRxTimeExcd": sfrapPerfIcmpTotalRxTimeExcd,
       "sfrapPerfIcmpTotalTxTimeExcd": sfrapPerfIcmpTotalTxTimeExcd,
       "sfrapPerfIcmpTotalRxParamProb": sfrapPerfIcmpTotalRxParamProb,
       "sfrapPerfIcmpTotalTxParamProb": sfrapPerfIcmpTotalTxParamProb,
       "sfrapPerfIcmpTotalRxTimestpReq": sfrapPerfIcmpTotalRxTimestpReq,
       "sfrapPerfIcmpTotalTxTimestpReq": sfrapPerfIcmpTotalTxTimestpReq,
       "sfrapPerfIcmpTotalRxTimestpRep": sfrapPerfIcmpTotalRxTimestpRep,
       "sfrapPerfIcmpTotalTxTimestpRep": sfrapPerfIcmpTotalTxTimestpRep,
       "sfrapPerfIcmpTotalRxAddrMaskReq": sfrapPerfIcmpTotalRxAddrMaskReq,
       "sfrapPerfIcmpTotalTxAddrMaskReq": sfrapPerfIcmpTotalTxAddrMaskReq,
       "sfrapPerfIcmpTotalRxAddrMaskRep": sfrapPerfIcmpTotalRxAddrMaskRep,
       "sfrapPerfIcmpTotalTxAddrMaskRep": sfrapPerfIcmpTotalTxAddrMaskRep,
       "sfrapPerfIcmpTotalRxPktTooBig": sfrapPerfIcmpTotalRxPktTooBig,
       "sfrapPerfIcmpTotalTxPktTooBig": sfrapPerfIcmpTotalTxPktTooBig,
       "sfrapPerfIcmpTotalRxGmQuery": sfrapPerfIcmpTotalRxGmQuery,
       "sfrapPerfIcmpTotalTxGmQuery": sfrapPerfIcmpTotalTxGmQuery,
       "sfrapPerfIcmpTotalRxGmReport": sfrapPerfIcmpTotalRxGmReport,
       "sfrapPerfIcmpTotalTxGmReport": sfrapPerfIcmpTotalTxGmReport,
       "sfrapPerfIcmpTotalRxGmReduct": sfrapPerfIcmpTotalRxGmReduct,
       "sfrapPerfIcmpTotalTxGmReduct": sfrapPerfIcmpTotalTxGmReduct,
       "sfrapPerfApplicationPerDlciTable": sfrapPerfApplicationPerDlciTable,
       "sfrapPerfApplicationPerDlciEntry": sfrapPerfApplicationPerDlciEntry,
       "sfrapPerfApplicationPerDlciInterval": sfrapPerfApplicationPerDlciInterval,
       "sfrapPerfApplicationPerDlciValue": sfrapPerfApplicationPerDlciValue,
       "sfrapPerfApplicationPerDlciRxSnmp": sfrapPerfApplicationPerDlciRxSnmp,
       "sfrapPerfApplicationPerDlciTxSnmp": sfrapPerfApplicationPerDlciTxSnmp,
       "sfrapPerfApplicationPerDlciRxSnmpTrap": sfrapPerfApplicationPerDlciRxSnmpTrap,
       "sfrapPerfApplicationPerDlciTxSnmpTrap": sfrapPerfApplicationPerDlciTxSnmpTrap,
       "sfrapPerfApplicationPerDlciRxHttp": sfrapPerfApplicationPerDlciRxHttp,
       "sfrapPerfApplicationPerDlciTxHttp": sfrapPerfApplicationPerDlciTxHttp,
       "sfrapPerfApplicationPerDlciRxTelnet": sfrapPerfApplicationPerDlciRxTelnet,
       "sfrapPerfApplicationPerDlciTxTelnet": sfrapPerfApplicationPerDlciTxTelnet,
       "sfrapPerfApplicationPerDlciRxSmtp": sfrapPerfApplicationPerDlciRxSmtp,
       "sfrapPerfApplicationPerDlciTxSmtp": sfrapPerfApplicationPerDlciTxSmtp,
       "sfrapPerfApplicationPerDlciRxFtp": sfrapPerfApplicationPerDlciRxFtp,
       "sfrapPerfApplicationPerDlciTxFtp": sfrapPerfApplicationPerDlciTxFtp,
       "sfrapPerfApplicationPerDlciRxTftp": sfrapPerfApplicationPerDlciRxTftp,
       "sfrapPerfApplicationPerDlciTxTftp": sfrapPerfApplicationPerDlciTxTftp,
       "sfrapPerfApplicationPerDlciRxCustom1": sfrapPerfApplicationPerDlciRxCustom1,
       "sfrapPerfApplicationPerDlciTxCustom1": sfrapPerfApplicationPerDlciTxCustom1,
       "sfrapPerfApplicationPerDlciRxCustom2": sfrapPerfApplicationPerDlciRxCustom2,
       "sfrapPerfApplicationPerDlciTxCustom2": sfrapPerfApplicationPerDlciTxCustom2,
       "sfrapPerfApplicationPerDlciRxCustom3": sfrapPerfApplicationPerDlciRxCustom3,
       "sfrapPerfApplicationPerDlciTxCustom3": sfrapPerfApplicationPerDlciTxCustom3,
       "sfrapPerfApplicationPerDlciRxCustom4": sfrapPerfApplicationPerDlciRxCustom4,
       "sfrapPerfApplicationPerDlciTxCustom4": sfrapPerfApplicationPerDlciTxCustom4,
       "sfrapPerfApplicationTotalTable": sfrapPerfApplicationTotalTable,
       "sfrapPerfApplicationTotalEntry": sfrapPerfApplicationTotalEntry,
       "sfrapPerfApplicationTotalInterval": sfrapPerfApplicationTotalInterval,
       "sfrapPerfApplicationTotalRxSnmp": sfrapPerfApplicationTotalRxSnmp,
       "sfrapPerfApplicationTotalTxSnmp": sfrapPerfApplicationTotalTxSnmp,
       "sfrapPerfApplicationTotalRxSnmpTrap": sfrapPerfApplicationTotalRxSnmpTrap,
       "sfrapPerfApplicationTotalTxSnmpTrap": sfrapPerfApplicationTotalTxSnmpTrap,
       "sfrapPerfApplicationTotalRxHttp": sfrapPerfApplicationTotalRxHttp,
       "sfrapPerfApplicationTotalTxHttp": sfrapPerfApplicationTotalTxHttp,
       "sfrapPerfApplicationTotalRxTelnet": sfrapPerfApplicationTotalRxTelnet,
       "sfrapPerfApplicationTotalTxTelnet": sfrapPerfApplicationTotalTxTelnet,
       "sfrapPerfApplicationTotalRxSmtp": sfrapPerfApplicationTotalRxSmtp,
       "sfrapPerfApplicationTotalTxSmtp": sfrapPerfApplicationTotalTxSmtp,
       "sfrapPerfApplicationTotalRxFtp": sfrapPerfApplicationTotalRxFtp,
       "sfrapPerfApplicationTotalTxFtp": sfrapPerfApplicationTotalTxFtp,
       "sfrapPerfApplicationTotalRxTftp": sfrapPerfApplicationTotalRxTftp,
       "sfrapPerfApplicationTotalTxTftp": sfrapPerfApplicationTotalTxTftp,
       "sfrapPerfApplicationTotalRxCustom1": sfrapPerfApplicationTotalRxCustom1,
       "sfrapPerfApplicationTotalTxCustom1": sfrapPerfApplicationTotalTxCustom1,
       "sfrapPerfApplicationTotalRxCustom2": sfrapPerfApplicationTotalRxCustom2,
       "sfrapPerfApplicationTotalTxCustom2": sfrapPerfApplicationTotalTxCustom2,
       "sfrapPerfApplicationTotalRxCustom3": sfrapPerfApplicationTotalRxCustom3,
       "sfrapPerfApplicationTotalTxCustom3": sfrapPerfApplicationTotalTxCustom3,
       "sfrapPerfApplicationTotalRxCustom4": sfrapPerfApplicationTotalRxCustom4,
       "sfrapPerfApplicationTotalTxCustom4": sfrapPerfApplicationTotalTxCustom4,
       "sfrapPerfRoutingPerDlciTable": sfrapPerfRoutingPerDlciTable,
       "sfrapPerfRoutingPerDlciEntry": sfrapPerfRoutingPerDlciEntry,
       "sfrapPerfRoutingPerDlciInterval": sfrapPerfRoutingPerDlciInterval,
       "sfrapPerfRoutingPerDlciValue": sfrapPerfRoutingPerDlciValue,
       "sfrapPerfRoutingPerDlciRxOspf": sfrapPerfRoutingPerDlciRxOspf,
       "sfrapPerfRoutingPerDlciTxOspf": sfrapPerfRoutingPerDlciTxOspf,
       "sfrapPerfRoutingPerDlciRxRip": sfrapPerfRoutingPerDlciRxRip,
       "sfrapPerfRoutingPerDlciTxRip": sfrapPerfRoutingPerDlciTxRip,
       "sfrapPerfRoutingPerDlciRxNetbios": sfrapPerfRoutingPerDlciRxNetbios,
       "sfrapPerfRoutingPerDlciTxNetbios": sfrapPerfRoutingPerDlciTxNetbios,
       "sfrapPerfRoutingTotalTable": sfrapPerfRoutingTotalTable,
       "sfrapPerfRoutingTotalEntry": sfrapPerfRoutingTotalEntry,
       "sfrapPerfRoutingTotalInterval": sfrapPerfRoutingTotalInterval,
       "sfrapPerfRoutingTotalRxOspf": sfrapPerfRoutingTotalRxOspf,
       "sfrapPerfRoutingTotalTxOspf": sfrapPerfRoutingTotalTxOspf,
       "sfrapPerfRoutingTotalRxRip": sfrapPerfRoutingTotalRxRip,
       "sfrapPerfRoutingTotalTxRip": sfrapPerfRoutingTotalTxRip,
       "sfrapPerfRoutingTotalRxNetbios": sfrapPerfRoutingTotalRxNetbios,
       "sfrapPerfRoutingTotalTxNetbios": sfrapPerfRoutingTotalTxNetbios,
       "sfrapPerfIpxPerDlciTable": sfrapPerfIpxPerDlciTable,
       "sfrapPerfIpxPerDlciEntry": sfrapPerfIpxPerDlciEntry,
       "sfrapPerfIpxPerDlciInterval": sfrapPerfIpxPerDlciInterval,
       "sfrapPerfIpxPerDlciValue": sfrapPerfIpxPerDlciValue,
       "sfrapPerfIpxPerDlciRxTotal": sfrapPerfIpxPerDlciRxTotal,
       "sfrapPerfIpxPerDlciTxTotal": sfrapPerfIpxPerDlciTxTotal,
       "sfrapPerfIpxPerDlciRxSpx": sfrapPerfIpxPerDlciRxSpx,
       "sfrapPerfIpxPerDlciTxSpx": sfrapPerfIpxPerDlciTxSpx,
       "sfrapPerfIpxPerDlciRxNcp": sfrapPerfIpxPerDlciRxNcp,
       "sfrapPerfIpxPerDlciTxNcp": sfrapPerfIpxPerDlciTxNcp,
       "sfrapPerfIpxPerDlciRxSap": sfrapPerfIpxPerDlciRxSap,
       "sfrapPerfIpxPerDlciTxSap": sfrapPerfIpxPerDlciTxSap,
       "sfrapPerfIpxPerDlciRxRip": sfrapPerfIpxPerDlciRxRip,
       "sfrapPerfIpxPerDlciTxRip": sfrapPerfIpxPerDlciTxRip,
       "sfrapPerfIpxPerDlciRxNetbios": sfrapPerfIpxPerDlciRxNetbios,
       "sfrapPerfIpxPerDlciTxNetbios": sfrapPerfIpxPerDlciTxNetbios,
       "sfrapPerfIpxPerDlciRxOther": sfrapPerfIpxPerDlciRxOther,
       "sfrapPerfIpxPerDlciTxOther": sfrapPerfIpxPerDlciTxOther,
       "sfrapPerfIpxTotalTable": sfrapPerfIpxTotalTable,
       "sfrapPerfIpxTotalEntry": sfrapPerfIpxTotalEntry,
       "sfrapPerfIpxTotalInterval": sfrapPerfIpxTotalInterval,
       "sfrapPerfIpxTotalRxTotal": sfrapPerfIpxTotalRxTotal,
       "sfrapPerfIpxTotalTxTotal": sfrapPerfIpxTotalTxTotal,
       "sfrapPerfIpxTotalRxSpx": sfrapPerfIpxTotalRxSpx,
       "sfrapPerfIpxTotalTxSpx": sfrapPerfIpxTotalTxSpx,
       "sfrapPerfIpxTotalRxNcp": sfrapPerfIpxTotalRxNcp,
       "sfrapPerfIpxTotalTxNcp": sfrapPerfIpxTotalTxNcp,
       "sfrapPerfIpxTotalRxSap": sfrapPerfIpxTotalRxSap,
       "sfrapPerfIpxTotalTxSap": sfrapPerfIpxTotalTxSap,
       "sfrapPerfIpxTotalRxRip": sfrapPerfIpxTotalRxRip,
       "sfrapPerfIpxTotalTxRip": sfrapPerfIpxTotalTxRip,
       "sfrapPerfIpxTotalRxNetbios": sfrapPerfIpxTotalRxNetbios,
       "sfrapPerfIpxTotalTxNetbios": sfrapPerfIpxTotalTxNetbios,
       "sfrapPerfIpxTotalRxOther": sfrapPerfIpxTotalRxOther,
       "sfrapPerfIpxTotalTxOther": sfrapPerfIpxTotalTxOther,
       "sfrapPerfSnaPerDlciTable": sfrapPerfSnaPerDlciTable,
       "sfrapPerfSnaPerDlciEntry": sfrapPerfSnaPerDlciEntry,
       "sfrapPerfSnaPerDlciInterval": sfrapPerfSnaPerDlciInterval,
       "sfrapPerfSnaPerDlciValue": sfrapPerfSnaPerDlciValue,
       "sfrapPerfSnaPerDlciRxTotal": sfrapPerfSnaPerDlciRxTotal,
       "sfrapPerfSnaPerDlciTxTotal": sfrapPerfSnaPerDlciTxTotal,
       "sfrapPerfSnaPerDlciRxSubarea": sfrapPerfSnaPerDlciRxSubarea,
       "sfrapPerfSnaPerDlciTxSubarea": sfrapPerfSnaPerDlciTxSubarea,
       "sfrapPerfSnaPerDlciRxPeriph": sfrapPerfSnaPerDlciRxPeriph,
       "sfrapPerfSnaPerDlciTxPeriph": sfrapPerfSnaPerDlciTxPeriph,
       "sfrapPerfSnaPerDlciRxAppn": sfrapPerfSnaPerDlciRxAppn,
       "sfrapPerfSnaPerDlciTxAppn": sfrapPerfSnaPerDlciTxAppn,
       "sfrapPerfSnaPerDlciRxNetbios": sfrapPerfSnaPerDlciRxNetbios,
       "sfrapPerfSnaPerDlciTxNetbios": sfrapPerfSnaPerDlciTxNetbios,
       "sfrapPerfSnaPerDlciRxOther": sfrapPerfSnaPerDlciRxOther,
       "sfrapPerfSnaPerDlciTxOther": sfrapPerfSnaPerDlciTxOther,
       "sfrapPerfSnaTotalTable": sfrapPerfSnaTotalTable,
       "sfrapPerfSnaTotalEntry": sfrapPerfSnaTotalEntry,
       "sfrapPerfSnaTotalInterval": sfrapPerfSnaTotalInterval,
       "sfrapPerfSnaTotalRxTotal": sfrapPerfSnaTotalRxTotal,
       "sfrapPerfSnaTotalTxTotal": sfrapPerfSnaTotalTxTotal,
       "sfrapPerfSnaTotalRxSubarea": sfrapPerfSnaTotalRxSubarea,
       "sfrapPerfSnaTotalTxSubarea": sfrapPerfSnaTotalTxSubarea,
       "sfrapPerfSnaTotalRxPeriph": sfrapPerfSnaTotalRxPeriph,
       "sfrapPerfSnaTotalTxPeriph": sfrapPerfSnaTotalTxPeriph,
       "sfrapPerfSnaTotalRxAppn": sfrapPerfSnaTotalRxAppn,
       "sfrapPerfSnaTotalTxAppn": sfrapPerfSnaTotalTxAppn,
       "sfrapPerfSnaTotalRxNetbios": sfrapPerfSnaTotalRxNetbios,
       "sfrapPerfSnaTotalTxNetbios": sfrapPerfSnaTotalTxNetbios,
       "sfrapPerfSnaTotalRxOther": sfrapPerfSnaTotalRxOther,
       "sfrapPerfSnaTotalTxOther": sfrapPerfSnaTotalTxOther,
       "sfrapPerfArpPerDlciTable": sfrapPerfArpPerDlciTable,
       "sfrapPerfArpPerDlciEntry": sfrapPerfArpPerDlciEntry,
       "sfrapPerfArpPerDlciInterval": sfrapPerfArpPerDlciInterval,
       "sfrapPerfArpPerDlciValue": sfrapPerfArpPerDlciValue,
       "sfrapPerfArpPerDlciRxTotal": sfrapPerfArpPerDlciRxTotal,
       "sfrapPerfArpPerDlciTxTotal": sfrapPerfArpPerDlciTxTotal,
       "sfrapPerfArpPerDlciRxArpReq": sfrapPerfArpPerDlciRxArpReq,
       "sfrapPerfArpPerDlciTxArpReq": sfrapPerfArpPerDlciTxArpReq,
       "sfrapPerfArpPerDlciRxArpRep": sfrapPerfArpPerDlciRxArpRep,
       "sfrapPerfArpPerDlciTxArpRep": sfrapPerfArpPerDlciTxArpRep,
       "sfrapPerfArpPerDlciRxRarpReq": sfrapPerfArpPerDlciRxRarpReq,
       "sfrapPerfArpPerDlciTxRarpReq": sfrapPerfArpPerDlciTxRarpReq,
       "sfrapPerfArpPerDlciRxRarpRep": sfrapPerfArpPerDlciRxRarpRep,
       "sfrapPerfArpPerDlciTxRarpRep": sfrapPerfArpPerDlciTxRarpRep,
       "sfrapPerfArpPerDlciRxInarpReq": sfrapPerfArpPerDlciRxInarpReq,
       "sfrapPerfArpPerDlciTxInarpReq": sfrapPerfArpPerDlciTxInarpReq,
       "sfrapPerfArpPerDlciRxInarpRep": sfrapPerfArpPerDlciRxInarpRep,
       "sfrapPerfArpPerDlciTxInarpRep": sfrapPerfArpPerDlciTxInarpRep,
       "sfrapPerfArpPerDlciRxOther": sfrapPerfArpPerDlciRxOther,
       "sfrapPerfArpPerDlciTxOther": sfrapPerfArpPerDlciTxOther,
       "sfrapPerfArpTotalTable": sfrapPerfArpTotalTable,
       "sfrapPerfArpTotalEntry": sfrapPerfArpTotalEntry,
       "sfrapPerfArpTotalInterval": sfrapPerfArpTotalInterval,
       "sfrapPerfArpTotalRxTotal": sfrapPerfArpTotalRxTotal,
       "sfrapPerfArpTotalTxTotal": sfrapPerfArpTotalTxTotal,
       "sfrapPerfArpTotalRxArpReq": sfrapPerfArpTotalRxArpReq,
       "sfrapPerfArpTotalTxArpReq": sfrapPerfArpTotalTxArpReq,
       "sfrapPerfArpTotalRxArpRep": sfrapPerfArpTotalRxArpRep,
       "sfrapPerfArpTotalTxArpRep": sfrapPerfArpTotalTxArpRep,
       "sfrapPerfArpTotalRxRarpReq": sfrapPerfArpTotalRxRarpReq,
       "sfrapPerfArpTotalTxRarpReq": sfrapPerfArpTotalTxRarpReq,
       "sfrapPerfArpTotalRxRarpRep": sfrapPerfArpTotalRxRarpRep,
       "sfrapPerfArpTotalTxRarpRep": sfrapPerfArpTotalTxRarpRep,
       "sfrapPerfArpTotalRxInarpReq": sfrapPerfArpTotalRxInarpReq,
       "sfrapPerfArpTotalTxInarpReq": sfrapPerfArpTotalTxInarpReq,
       "sfrapPerfArpTotalRxInarpRep": sfrapPerfArpTotalRxInarpRep,
       "sfrapPerfArpTotalTxInarpRep": sfrapPerfArpTotalTxInarpRep,
       "sfrapPerfArpTotalRxOther": sfrapPerfArpTotalRxOther,
       "sfrapPerfArpTotalTxOther": sfrapPerfArpTotalTxOther,
       "sfrapPerfLmiPerDlciTable": sfrapPerfLmiPerDlciTable,
       "sfrapPerfLmiPerDlciEntry": sfrapPerfLmiPerDlciEntry,
       "sfrapPerfLmiPerDlciInterval": sfrapPerfLmiPerDlciInterval,
       "sfrapPerfLmiPerDlciValue": sfrapPerfLmiPerDlciValue,
       "sfrapPerfLmiPerDlciRxTotalByteCnt": sfrapPerfLmiPerDlciRxTotalByteCnt,
       "sfrapPerfLmiPerDlciTxTotalByteCnt": sfrapPerfLmiPerDlciTxTotalByteCnt,
       "sfrapPerfLmiPerDlciRxLivoEnqByteCnt": sfrapPerfLmiPerDlciRxLivoEnqByteCnt,
       "sfrapPerfLmiPerDlciTxLivoEnqByteCnt": sfrapPerfLmiPerDlciTxLivoEnqByteCnt,
       "sfrapPerfLmiPerDlciRxLivoStatByteCnt": sfrapPerfLmiPerDlciRxLivoStatByteCnt,
       "sfrapPerfLmiPerDlciTxLivoStatByteCnt": sfrapPerfLmiPerDlciTxLivoStatByteCnt,
       "sfrapPerfLmiPerDlciRxFullEnqByteCnt": sfrapPerfLmiPerDlciRxFullEnqByteCnt,
       "sfrapPerfLmiPerDlciTxFullEnqByteCnt": sfrapPerfLmiPerDlciTxFullEnqByteCnt,
       "sfrapPerfLmiPerDlciRxFullStatByteCnt": sfrapPerfLmiPerDlciRxFullStatByteCnt,
       "sfrapPerfLmiPerDlciTxFullStatByteCnt": sfrapPerfLmiPerDlciTxFullStatByteCnt,
       "sfrapPerfLmiPerDlciRxOtherByteCnt": sfrapPerfLmiPerDlciRxOtherByteCnt,
       "sfrapPerfLmiPerDlciTxOtherByteCnt": sfrapPerfLmiPerDlciTxOtherByteCnt,
       "sfrapPerfLmiTotalTable": sfrapPerfLmiTotalTable,
       "sfrapPerfLmiTotalEntry": sfrapPerfLmiTotalEntry,
       "sfrapPerfLmiTotalInterval": sfrapPerfLmiTotalInterval,
       "sfrapPerfLmiTotalDlciValue": sfrapPerfLmiTotalDlciValue,
       "sfrapPerfLmiTotalRxTotalByteCnt": sfrapPerfLmiTotalRxTotalByteCnt,
       "sfrapPerfLmiTotalTxTotalByteCnt": sfrapPerfLmiTotalTxTotalByteCnt,
       "sfrapPerfLmiTotalRxLivoEnqByteCnt": sfrapPerfLmiTotalRxLivoEnqByteCnt,
       "sfrapPerfLmiTotalTxLivoEnqByteCnt": sfrapPerfLmiTotalTxLivoEnqByteCnt,
       "sfrapPerfLmiTotalRxLivoStatByteCnt": sfrapPerfLmiTotalRxLivoStatByteCnt,
       "sfrapPerfLmiTotalTxLivoStatByteCnt": sfrapPerfLmiTotalTxLivoStatByteCnt,
       "sfrapPerfLmiTotalRxFullEnqByteCnt": sfrapPerfLmiTotalRxFullEnqByteCnt,
       "sfrapPerfLmiTotalTxFullEnqByteCnt": sfrapPerfLmiTotalTxFullEnqByteCnt,
       "sfrapPerfLmiTotalRxFullStatByteCnt": sfrapPerfLmiTotalRxFullStatByteCnt,
       "sfrapPerfLmiTotalTxFullStatByteCnt": sfrapPerfLmiTotalTxFullStatByteCnt,
       "sfrapPerfLmiTotalRxOtherByteCnt": sfrapPerfLmiTotalRxOtherByteCnt,
       "sfrapPerfLmiTotalTxOtherByteCnt": sfrapPerfLmiTotalTxOtherByteCnt,
       "sfrapPerfNetworkLongTerm": sfrapPerfNetworkLongTerm,
       "sfrapPerfNetwLongTermTable": sfrapPerfNetwLongTermTable,
       "sfrapPerfNetwLongTermEntry": sfrapPerfNetwLongTermEntry,
       "sfrapPerfNetwLongTermDlci": sfrapPerfNetwLongTermDlci,
       "sfrapPerfNetwLongTermProtocol": sfrapPerfNetwLongTermProtocol,
       "sfrapPerfNetwLongTermInterval": sfrapPerfNetwLongTermInterval,
       "sfrapPerfNetwLongTermValue": sfrapPerfNetwLongTermValue,
       "sfrapPerfNetwLongTermAltTable": sfrapPerfNetwLongTermAltTable,
       "sfrapPerfNetwLongTermAltEntry": sfrapPerfNetwLongTermAltEntry,
       "sfrapPerfNetwLongTermAltDlci": sfrapPerfNetwLongTermAltDlci,
       "sfrapPerfNetwLongTermAltProtocol": sfrapPerfNetwLongTermAltProtocol,
       "sfrapPerfNetwLongTermAltArray": sfrapPerfNetwLongTermAltArray,
       "sfrapPerfNetworkLongTermCommands": sfrapPerfNetworkLongTermCommands,
       "sfrapPerfNetworkLongTermCmdClear": sfrapPerfNetworkLongTermCmdClear,
       "sfrapPerfCirPercentUtilization": sfrapPerfCirPercentUtilization,
       "sfrapPerfCirPercentUtilizationTable": sfrapPerfCirPercentUtilizationTable,
       "sfrapPerfCirPercentUtilizationEntry": sfrapPerfCirPercentUtilizationEntry,
       "sfrapPerfCirPercentUtilizationInterval": sfrapPerfCirPercentUtilizationInterval,
       "sfrapPerfCirPercentUtilizationDlciValue": sfrapPerfCirPercentUtilizationDlciValue,
       "sfrapPerfCirRxPercentUtilizationRange1": sfrapPerfCirRxPercentUtilizationRange1,
       "sfrapPerfCirRxPercentUtilizationRange2": sfrapPerfCirRxPercentUtilizationRange2,
       "sfrapPerfCirRxPercentUtilizationRange3": sfrapPerfCirRxPercentUtilizationRange3,
       "sfrapPerfCirRxPercentUtilizationRange4": sfrapPerfCirRxPercentUtilizationRange4,
       "sfrapPerfCirRxPercentUtilizationRange5": sfrapPerfCirRxPercentUtilizationRange5,
       "sfrapPerfCirRxPercentUtilizationRange6": sfrapPerfCirRxPercentUtilizationRange6,
       "sfrapPerfCirRxPercentUtilizationRange7": sfrapPerfCirRxPercentUtilizationRange7,
       "sfrapPerfCirRxPercentUtilizationRange8": sfrapPerfCirRxPercentUtilizationRange8,
       "sfrapPerfCirTxPercentUtilizationRange1": sfrapPerfCirTxPercentUtilizationRange1,
       "sfrapPerfCirTxPercentUtilizationRange2": sfrapPerfCirTxPercentUtilizationRange2,
       "sfrapPerfCirTxPercentUtilizationRange3": sfrapPerfCirTxPercentUtilizationRange3,
       "sfrapPerfCirTxPercentUtilizationRange4": sfrapPerfCirTxPercentUtilizationRange4,
       "sfrapPerfCirTxPercentUtilizationRange5": sfrapPerfCirTxPercentUtilizationRange5,
       "sfrapPerfCirTxPercentUtilizationRange6": sfrapPerfCirTxPercentUtilizationRange6,
       "sfrapPerfCirTxPercentUtilizationRange7": sfrapPerfCirTxPercentUtilizationRange7,
       "sfrapPerfCirTxPercentUtilizationRange8": sfrapPerfCirTxPercentUtilizationRange8,
       "sfrapPerfCurrentPerDlciUtilizationTable": sfrapPerfCurrentPerDlciUtilizationTable,
       "sfrapPerfCurrentPerDlciUtilizationEntry": sfrapPerfCurrentPerDlciUtilizationEntry,
       "sfrapPerfCurrentPerDlciUtilizationDlciValue": sfrapPerfCurrentPerDlciUtilizationDlciValue,
       "sfrapPerfCurrentPerDlciRxUtilization": sfrapPerfCurrentPerDlciRxUtilization,
       "sfrapPerfCurrentPerDlciTxUtilization": sfrapPerfCurrentPerDlciTxUtilization,
       "sfrapPerfCurrentPerDlciAggregateUtilization": sfrapPerfCurrentPerDlciAggregateUtilization,
       "sfrapPerfCurrentUnitUtilization": sfrapPerfCurrentUnitUtilization,
       "sfrapPerfCurrentDteUtilization": sfrapPerfCurrentDteUtilization,
       "sfrapPerfCurrentWanUtilization": sfrapPerfCurrentWanUtilization,
       "sfrapPerfCurrentAggregateUtilization": sfrapPerfCurrentAggregateUtilization,
       "sfrapPerfFRStatsCollectionStatus": sfrapPerfFRStatsCollectionStatus,
       "sfrapPerfFRStatsCollection": sfrapPerfFRStatsCollection,
       "sfrapAlarmType": sfrapAlarmType,
       "sfrapDLCINum": sfrapDLCINum,
       "sfrapInterface": sfrapInterface,
       "sfrapIpAddress": sfrapIpAddress,
       "sfrapEventTrapLog": sfrapEventTrapLog,
       "sfrapEventTrapLogTable": sfrapEventTrapLogTable,
       "sfrapEventTrapLogEntry": sfrapEventTrapLogEntry,
       "sfrapEventTrapLogSeqNum": sfrapEventTrapLogSeqNum,
       "sfrapEventTrapLogGenericEvent": sfrapEventTrapLogGenericEvent,
       "sfrapEventTrapLogSpecificEvent": sfrapEventTrapLogSpecificEvent,
       "sfrapEventTrapLogTimeStamp": sfrapEventTrapLogTimeStamp,
       "sfrapEventTrapLogVarBind1": sfrapEventTrapLogVarBind1,
       "sfrapEventTrapLogVarBind2": sfrapEventTrapLogVarBind2,
       "sfrapEventTrapLogVarBind3": sfrapEventTrapLogVarBind3,
       "sfrapEventLogAltTable": sfrapEventLogAltTable,
       "sfrapEventLogAltEntry": sfrapEventLogAltEntry,
       "sfrapEventLogAltSeqNum": sfrapEventLogAltSeqNum,
       "sfrapEventLogAltArray": sfrapEventLogAltArray,
       "sfrapEventLogCurrentSeqNum": sfrapEventLogCurrentSeqNum,
       "sfrapEventLogFreeze": sfrapEventLogFreeze,
       "sfrapEventLogClear": sfrapEventLogClear,
       "sfrapPercentUtilization": sfrapPercentUtilization,
       "sfrapUtilizationThreshold": sfrapUtilizationThreshold,
       "sfrapCfgLockIpAddress": sfrapCfgLockIpAddress}
)
