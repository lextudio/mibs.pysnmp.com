# SNMP MIB module (DFRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:21 2024
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
_Dfrap_ObjectIdentity = ObjectIdentity
dfrap = _Dfrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6)
)
_DfrapSystem_ObjectIdentity = ObjectIdentity
dfrapSystem = _DfrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 1)
)
_DfrapSysTable_ObjectIdentity = ObjectIdentity
dfrapSysTable = _DfrapSysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1)
)


class _DfrapSysType_Type(DisplayString):
    """Custom type dfrapSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DfrapSysType_Type.__name__ = "DisplayString"
_DfrapSysType_Object = MibScalar
dfrapSysType = _DfrapSysType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 1),
    _DfrapSysType_Type()
)
dfrapSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysType.setStatus("mandatory")


class _DfrapSysSoftRev_Type(DisplayString):
    """Custom type dfrapSysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysSoftRev_Type.__name__ = "DisplayString"
_DfrapSysSoftRev_Object = MibScalar
dfrapSysSoftRev = _DfrapSysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 2),
    _DfrapSysSoftRev_Type()
)
dfrapSysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysSoftRev.setStatus("mandatory")


class _DfrapSysHardRev_Type(DisplayString):
    """Custom type dfrapSysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysHardRev_Type.__name__ = "DisplayString"
_DfrapSysHardRev_Object = MibScalar
dfrapSysHardRev = _DfrapSysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 3),
    _DfrapSysHardRev_Type()
)
dfrapSysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysHardRev.setStatus("mandatory")


class _DfrapSysNumT1Installed_Type(Integer32):
    """Custom type dfrapSysNumT1Installed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DfrapSysNumT1Installed_Type.__name__ = "Integer32"
_DfrapSysNumT1Installed_Object = MibScalar
dfrapSysNumT1Installed = _DfrapSysNumT1Installed_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 4),
    _DfrapSysNumT1Installed_Type()
)
dfrapSysNumT1Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumT1Installed.setStatus("mandatory")


class _DfrapSysNumDteInstalled_Type(Integer32):
    """Custom type dfrapSysNumDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DfrapSysNumDteInstalled_Type.__name__ = "Integer32"
_DfrapSysNumDteInstalled_Object = MibScalar
dfrapSysNumDteInstalled = _DfrapSysNumDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 5),
    _DfrapSysNumDteInstalled_Type()
)
dfrapSysNumDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumDteInstalled.setStatus("mandatory")


class _DfrapSysNumMaintInstalled_Type(Integer32):
    """Custom type dfrapSysNumMaintInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DfrapSysNumMaintInstalled_Type.__name__ = "Integer32"
_DfrapSysNumMaintInstalled_Object = MibScalar
dfrapSysNumMaintInstalled = _DfrapSysNumMaintInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 6),
    _DfrapSysNumMaintInstalled_Type()
)
dfrapSysNumMaintInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumMaintInstalled.setStatus("mandatory")


class _DfrapSysName_Type(DisplayString):
    """Custom type dfrapSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapSysName_Type.__name__ = "DisplayString"
_DfrapSysName_Object = MibScalar
dfrapSysName = _DfrapSysName_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 7),
    _DfrapSysName_Type()
)
dfrapSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapSysName.setStatus("mandatory")


class _DfrapSysSerialNo_Type(DisplayString):
    """Custom type dfrapSysSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DfrapSysSerialNo_Type.__name__ = "DisplayString"
_DfrapSysSerialNo_Object = MibScalar
dfrapSysSerialNo = _DfrapSysSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 8),
    _DfrapSysSerialNo_Type()
)
dfrapSysSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysSerialNo.setStatus("mandatory")


class _DfrapSysResetNode_Type(Integer32):
    """Custom type dfrapSysResetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            321
        )
    )
    namedValues = NamedValues(
        ("reset-node", 321)
    )


_DfrapSysResetNode_Type.__name__ = "Integer32"
_DfrapSysResetNode_Object = MibScalar
dfrapSysResetNode = _DfrapSysResetNode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 9),
    _DfrapSysResetNode_Type()
)
dfrapSysResetNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapSysResetNode.setStatus("mandatory")
_DfrapSysAmtMemoryInstalled_Type = Integer32
_DfrapSysAmtMemoryInstalled_Object = MibScalar
dfrapSysAmtMemoryInstalled = _DfrapSysAmtMemoryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 10),
    _DfrapSysAmtMemoryInstalled_Type()
)
dfrapSysAmtMemoryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysAmtMemoryInstalled.setStatus("mandatory")


class _DfrapSysNumDdsInstalled_Type(Integer32):
    """Custom type dfrapSysNumDdsInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DfrapSysNumDdsInstalled_Type.__name__ = "Integer32"
_DfrapSysNumDdsInstalled_Object = MibScalar
dfrapSysNumDdsInstalled = _DfrapSysNumDdsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 11),
    _DfrapSysNumDdsInstalled_Type()
)
dfrapSysNumDdsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumDdsInstalled.setStatus("mandatory")


class _DfrapSysLocation_Type(DisplayString):
    """Custom type dfrapSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapSysLocation_Type.__name__ = "DisplayString"
_DfrapSysLocation_Object = MibScalar
dfrapSysLocation = _DfrapSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 12),
    _DfrapSysLocation_Type()
)
dfrapSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapSysLocation.setStatus("mandatory")


class _DfrapSysContact_Type(DisplayString):
    """Custom type dfrapSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapSysContact_Type.__name__ = "DisplayString"
_DfrapSysContact_Object = MibScalar
dfrapSysContact = _DfrapSysContact_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 13),
    _DfrapSysContact_Type()
)
dfrapSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapSysContact.setStatus("mandatory")


class _DfrapSysPrompt_Type(DisplayString):
    """Custom type dfrapSysPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapSysPrompt_Type.__name__ = "DisplayString"
_DfrapSysPrompt_Object = MibScalar
dfrapSysPrompt = _DfrapSysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 15),
    _DfrapSysPrompt_Type()
)
dfrapSysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapSysPrompt.setStatus("mandatory")


class _DfrapSysBootRev_Type(DisplayString):
    """Custom type dfrapSysBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysBootRev_Type.__name__ = "DisplayString"
_DfrapSysBootRev_Object = MibScalar
dfrapSysBootRev = _DfrapSysBootRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 1, 16),
    _DfrapSysBootRev_Type()
)
dfrapSysBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysBootRev.setStatus("mandatory")
_DfrapSysFeatureTable_ObjectIdentity = ObjectIdentity
dfrapSysFeatureTable = _DfrapSysFeatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2)
)


class _DfrapSysSLIPSupported_Type(DisplayString):
    """Custom type dfrapSysSLIPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysSLIPSupported_Type.__name__ = "DisplayString"
_DfrapSysSLIPSupported_Object = MibScalar
dfrapSysSLIPSupported = _DfrapSysSLIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 1),
    _DfrapSysSLIPSupported_Type()
)
dfrapSysSLIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysSLIPSupported.setStatus("mandatory")


class _DfrapSysPPPSupported_Type(DisplayString):
    """Custom type dfrapSysPPPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysPPPSupported_Type.__name__ = "DisplayString"
_DfrapSysPPPSupported_Object = MibScalar
dfrapSysPPPSupported = _DfrapSysPPPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 2),
    _DfrapSysPPPSupported_Type()
)
dfrapSysPPPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysPPPSupported.setStatus("mandatory")


class _DfrapSysRDOSupported_Type(DisplayString):
    """Custom type dfrapSysRDOSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysRDOSupported_Type.__name__ = "DisplayString"
_DfrapSysRDOSupported_Object = MibScalar
dfrapSysRDOSupported = _DfrapSysRDOSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 3),
    _DfrapSysRDOSupported_Type()
)
dfrapSysRDOSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysRDOSupported.setStatus("mandatory")


class _DfrapSysETHSupported_Type(DisplayString):
    """Custom type dfrapSysETHSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysETHSupported_Type.__name__ = "DisplayString"
_DfrapSysETHSupported_Object = MibScalar
dfrapSysETHSupported = _DfrapSysETHSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 4),
    _DfrapSysETHSupported_Type()
)
dfrapSysETHSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysETHSupported.setStatus("mandatory")


class _DfrapSysTKRSupported_Type(DisplayString):
    """Custom type dfrapSysTKRSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysTKRSupported_Type.__name__ = "DisplayString"
_DfrapSysTKRSupported_Object = MibScalar
dfrapSysTKRSupported = _DfrapSysTKRSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 5),
    _DfrapSysTKRSupported_Type()
)
dfrapSysTKRSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysTKRSupported.setStatus("mandatory")


class _DfrapSysExtTimSupported_Type(DisplayString):
    """Custom type dfrapSysExtTimSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysExtTimSupported_Type.__name__ = "DisplayString"
_DfrapSysExtTimSupported_Object = MibScalar
dfrapSysExtTimSupported = _DfrapSysExtTimSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 6),
    _DfrapSysExtTimSupported_Type()
)
dfrapSysExtTimSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysExtTimSupported.setStatus("mandatory")


class _DfrapSysBRISupported_Type(DisplayString):
    """Custom type dfrapSysBRISupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysBRISupported_Type.__name__ = "DisplayString"
_DfrapSysBRISupported_Object = MibScalar
dfrapSysBRISupported = _DfrapSysBRISupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 7),
    _DfrapSysBRISupported_Type()
)
dfrapSysBRISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysBRISupported.setStatus("mandatory")


class _DfrapSysSelDTESupported_Type(DisplayString):
    """Custom type dfrapSysSelDTESupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysSelDTESupported_Type.__name__ = "DisplayString"
_DfrapSysSelDTESupported_Object = MibScalar
dfrapSysSelDTESupported = _DfrapSysSelDTESupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 8),
    _DfrapSysSelDTESupported_Type()
)
dfrapSysSelDTESupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysSelDTESupported.setStatus("mandatory")


class _DfrapSysMLSupported_Type(DisplayString):
    """Custom type dfrapSysMLSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DfrapSysMLSupported_Type.__name__ = "DisplayString"
_DfrapSysMLSupported_Object = MibScalar
dfrapSysMLSupported = _DfrapSysMLSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 9),
    _DfrapSysMLSupported_Type()
)
dfrapSysMLSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysMLSupported.setStatus("mandatory")
_DfrapSysNumDlcisSupported_Type = Integer32
_DfrapSysNumDlcisSupported_Object = MibScalar
dfrapSysNumDlcisSupported = _DfrapSysNumDlcisSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 10),
    _DfrapSysNumDlcisSupported_Type()
)
dfrapSysNumDlcisSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumDlcisSupported.setStatus("mandatory")
_DfrapSysLTFNumDlcis_Type = Integer32
_DfrapSysLTFNumDlcis_Object = MibScalar
dfrapSysLTFNumDlcis = _DfrapSysLTFNumDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 11),
    _DfrapSysLTFNumDlcis_Type()
)
dfrapSysLTFNumDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysLTFNumDlcis.setStatus("mandatory")
_DfrapSysLTFNumProtocols_Type = Integer32
_DfrapSysLTFNumProtocols_Object = MibScalar
dfrapSysLTFNumProtocols = _DfrapSysLTFNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 12),
    _DfrapSysLTFNumProtocols_Type()
)
dfrapSysLTFNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysLTFNumProtocols.setStatus("mandatory")
_DfrapSysNumUserProtocols_Type = Integer32
_DfrapSysNumUserProtocols_Object = MibScalar
dfrapSysNumUserProtocols = _DfrapSysNumUserProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 13),
    _DfrapSysNumUserProtocols_Type()
)
dfrapSysNumUserProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumUserProtocols.setStatus("mandatory")
_DfrapSysNumSnmpMgrs_Type = Integer32
_DfrapSysNumSnmpMgrs_Object = MibScalar
dfrapSysNumSnmpMgrs = _DfrapSysNumSnmpMgrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 14),
    _DfrapSysNumSnmpMgrs_Type()
)
dfrapSysNumSnmpMgrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumSnmpMgrs.setStatus("mandatory")
_DfrapSysNumDlciNames_Type = Integer32
_DfrapSysNumDlciNames_Object = MibScalar
dfrapSysNumDlciNames = _DfrapSysNumDlciNames_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 1, 2, 15),
    _DfrapSysNumDlciNames_Type()
)
dfrapSysNumDlciNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapSysNumDlciNames.setStatus("mandatory")
_DfrapConfiguration_ObjectIdentity = ObjectIdentity
dfrapConfiguration = _DfrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2)
)
_DfrapCfgMgmtTable_ObjectIdentity = ObjectIdentity
dfrapCfgMgmtTable = _DfrapCfgMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1)
)
_DfrapCfgIpTable_ObjectIdentity = ObjectIdentity
dfrapCfgIpTable = _DfrapCfgIpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1)
)
_DfrapCfgIpMyIP_Type = IpAddress
_DfrapCfgIpMyIP_Object = MibScalar
dfrapCfgIpMyIP = _DfrapCfgIpMyIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 1),
    _DfrapCfgIpMyIP_Type()
)
dfrapCfgIpMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpMyIP.setStatus("mandatory")
_DfrapCfgIpPeerIP_Type = IpAddress
_DfrapCfgIpPeerIP_Object = MibScalar
dfrapCfgIpPeerIP = _DfrapCfgIpPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 2),
    _DfrapCfgIpPeerIP_Type()
)
dfrapCfgIpPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpPeerIP.setStatus("mandatory")
_DfrapCfgIpMask_Type = IpAddress
_DfrapCfgIpMask_Object = MibScalar
dfrapCfgIpMask = _DfrapCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 3),
    _DfrapCfgIpMask_Type()
)
dfrapCfgIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpMask.setStatus("mandatory")


class _DfrapCfgIpMaxMTU_Type(Integer32):
    """Custom type dfrapCfgIpMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_DfrapCfgIpMaxMTU_Type.__name__ = "Integer32"
_DfrapCfgIpMaxMTU_Object = MibScalar
dfrapCfgIpMaxMTU = _DfrapCfgIpMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 4),
    _DfrapCfgIpMaxMTU_Type()
)
dfrapCfgIpMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpMaxMTU.setStatus("mandatory")


class _DfrapCfgIpChannel_Type(Integer32):
    """Custom type dfrapCfgIpChannel based on Integer32"""
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


_DfrapCfgIpChannel_Type.__name__ = "Integer32"
_DfrapCfgIpChannel_Object = MibScalar
dfrapCfgIpChannel = _DfrapCfgIpChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 5),
    _DfrapCfgIpChannel_Type()
)
dfrapCfgIpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgIpChannel.setStatus("mandatory")


class _DfrapCfgIpTelnetEnable_Type(Integer32):
    """Custom type dfrapCfgIpTelnetEnable based on Integer32"""
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


_DfrapCfgIpTelnetEnable_Type.__name__ = "Integer32"
_DfrapCfgIpTelnetEnable_Object = MibScalar
dfrapCfgIpTelnetEnable = _DfrapCfgIpTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 6),
    _DfrapCfgIpTelnetEnable_Type()
)
dfrapCfgIpTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpTelnetEnable.setStatus("mandatory")


class _DfrapCfgIpTelnetAutoLogOut_Type(Integer32):
    """Custom type dfrapCfgIpTelnetAutoLogOut based on Integer32"""
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


_DfrapCfgIpTelnetAutoLogOut_Type.__name__ = "Integer32"
_DfrapCfgIpTelnetAutoLogOut_Object = MibScalar
dfrapCfgIpTelnetAutoLogOut = _DfrapCfgIpTelnetAutoLogOut_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 1, 7),
    _DfrapCfgIpTelnetAutoLogOut_Type()
)
dfrapCfgIpTelnetAutoLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgIpTelnetAutoLogOut.setStatus("mandatory")
_DfrapCfgTftpTable_ObjectIdentity = ObjectIdentity
dfrapCfgTftpTable = _DfrapCfgTftpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2)
)


class _DfrapCfgTftpInitiate_Type(DisplayString):
    """Custom type dfrapCfgTftpInitiate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgTftpInitiate_Type.__name__ = "DisplayString"
_DfrapCfgTftpInitiate_Object = MibScalar
dfrapCfgTftpInitiate = _DfrapCfgTftpInitiate_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 1),
    _DfrapCfgTftpInitiate_Type()
)
dfrapCfgTftpInitiate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgTftpInitiate.setStatus("mandatory")
_DfrapCfgTftpIpAddress_Type = IpAddress
_DfrapCfgTftpIpAddress_Object = MibScalar
dfrapCfgTftpIpAddress = _DfrapCfgTftpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 2),
    _DfrapCfgTftpIpAddress_Type()
)
dfrapCfgTftpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpIpAddress.setStatus("mandatory")


class _DfrapCfgTftpFilename_Type(DisplayString):
    """Custom type dfrapCfgTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DfrapCfgTftpFilename_Type.__name__ = "DisplayString"
_DfrapCfgTftpFilename_Object = MibScalar
dfrapCfgTftpFilename = _DfrapCfgTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 3),
    _DfrapCfgTftpFilename_Type()
)
dfrapCfgTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpFilename.setStatus("mandatory")


class _DfrapCfgTftpInterface_Type(Integer32):
    """Custom type dfrapCfgTftpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dds-interface", 2),
          ("dte-interface", 1),
          ("slip-interface", 3))
    )


_DfrapCfgTftpInterface_Type.__name__ = "Integer32"
_DfrapCfgTftpInterface_Object = MibScalar
dfrapCfgTftpInterface = _DfrapCfgTftpInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 4),
    _DfrapCfgTftpInterface_Type()
)
dfrapCfgTftpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpInterface.setStatus("mandatory")


class _DfrapCfgTftpDlci_Type(Integer32):
    """Custom type dfrapCfgTftpDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63487),
    )


_DfrapCfgTftpDlci_Type.__name__ = "Integer32"
_DfrapCfgTftpDlci_Object = MibScalar
dfrapCfgTftpDlci = _DfrapCfgTftpDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 5),
    _DfrapCfgTftpDlci_Type()
)
dfrapCfgTftpDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpDlci.setStatus("mandatory")


class _DfrapCfgTftpStatus_Type(Integer32):
    """Custom type dfrapCfgTftpStatus based on Integer32"""
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


_DfrapCfgTftpStatus_Type.__name__ = "Integer32"
_DfrapCfgTftpStatus_Object = MibScalar
dfrapCfgTftpStatus = _DfrapCfgTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 6),
    _DfrapCfgTftpStatus_Type()
)
dfrapCfgTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpStatus.setStatus("mandatory")
_DfrapCfgTftpNumBytes_Type = Counter32
_DfrapCfgTftpNumBytes_Object = MibScalar
dfrapCfgTftpNumBytes = _DfrapCfgTftpNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 2, 7),
    _DfrapCfgTftpNumBytes_Type()
)
dfrapCfgTftpNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgTftpNumBytes.setStatus("mandatory")
_DfrapCfgSnmpTable_ObjectIdentity = ObjectIdentity
dfrapCfgSnmpTable = _DfrapCfgSnmpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3)
)


class _DfrapCfgSnmpFrTrap_Type(Integer32):
    """Custom type dfrapCfgSnmpFrTrap based on Integer32"""
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


_DfrapCfgSnmpFrTrap_Type.__name__ = "Integer32"
_DfrapCfgSnmpFrTrap_Object = MibScalar
dfrapCfgSnmpFrTrap = _DfrapCfgSnmpFrTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 1),
    _DfrapCfgSnmpFrTrap_Type()
)
dfrapCfgSnmpFrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpFrTrap.setStatus("mandatory")
_DfrapCfgSnmpMgrTable_Object = MibTable
dfrapCfgSnmpMgrTable = _DfrapCfgSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrTable.setStatus("mandatory")
_DfrapCfgSnmpMgrEntry_Object = MibTableRow
dfrapCfgSnmpMgrEntry = _DfrapCfgSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2, 1)
)
dfrapCfgSnmpMgrEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgSnmpMgrIndex"),
)
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrEntry.setStatus("mandatory")
_DfrapCfgSnmpMgrIndex_Type = Integer32
_DfrapCfgSnmpMgrIndex_Object = MibTableColumn
dfrapCfgSnmpMgrIndex = _DfrapCfgSnmpMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2, 1, 1),
    _DfrapCfgSnmpMgrIndex_Type()
)
dfrapCfgSnmpMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrIndex.setStatus("mandatory")
_DfrapCfgSnmpMgrIP_Type = IpAddress
_DfrapCfgSnmpMgrIP_Object = MibTableColumn
dfrapCfgSnmpMgrIP = _DfrapCfgSnmpMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2, 1, 2),
    _DfrapCfgSnmpMgrIP_Type()
)
dfrapCfgSnmpMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrIP.setStatus("mandatory")


class _DfrapCfgSnmpMgrInterface_Type(Integer32):
    """Custom type dfrapCfgSnmpMgrInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dds-interface", 2),
          ("dte-interface", 1),
          ("slip-interface", 3))
    )


_DfrapCfgSnmpMgrInterface_Type.__name__ = "Integer32"
_DfrapCfgSnmpMgrInterface_Object = MibTableColumn
dfrapCfgSnmpMgrInterface = _DfrapCfgSnmpMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2, 1, 3),
    _DfrapCfgSnmpMgrInterface_Type()
)
dfrapCfgSnmpMgrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrInterface.setStatus("mandatory")
_DfrapCfgSnmpMgrDlci_Type = Integer32
_DfrapCfgSnmpMgrDlci_Object = MibTableColumn
dfrapCfgSnmpMgrDlci = _DfrapCfgSnmpMgrDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 2, 1, 4),
    _DfrapCfgSnmpMgrDlci_Type()
)
dfrapCfgSnmpMgrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrDlci.setStatus("mandatory")


class _DfrapCfgSnmpTrapMuting_Type(Integer32):
    """Custom type dfrapCfgSnmpTrapMuting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_DfrapCfgSnmpTrapMuting_Type.__name__ = "Integer32"
_DfrapCfgSnmpTrapMuting_Object = MibScalar
dfrapCfgSnmpTrapMuting = _DfrapCfgSnmpTrapMuting_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 3),
    _DfrapCfgSnmpTrapMuting_Type()
)
dfrapCfgSnmpTrapMuting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpTrapMuting.setStatus("mandatory")


class _DfrapCfgSnmpUtilTrapEnable_Type(Integer32):
    """Custom type dfrapCfgSnmpUtilTrapEnable based on Integer32"""
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


_DfrapCfgSnmpUtilTrapEnable_Type.__name__ = "Integer32"
_DfrapCfgSnmpUtilTrapEnable_Object = MibScalar
dfrapCfgSnmpUtilTrapEnable = _DfrapCfgSnmpUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 6),
    _DfrapCfgSnmpUtilTrapEnable_Type()
)
dfrapCfgSnmpUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSnmpUtilTrapEnable.setStatus("mandatory")
_DfrapCfgSnmpMgrClearN_Type = Integer32
_DfrapCfgSnmpMgrClearN_Object = MibScalar
dfrapCfgSnmpMgrClearN = _DfrapCfgSnmpMgrClearN_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 3, 7),
    _DfrapCfgSnmpMgrClearN_Type()
)
dfrapCfgSnmpMgrClearN.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgSnmpMgrClearN.setStatus("mandatory")
_DfrapCfgCommTable_ObjectIdentity = ObjectIdentity
dfrapCfgCommTable = _DfrapCfgCommTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4)
)


class _DfrapCfgCommMode_Type(Integer32):
    """Custom type dfrapCfgCommMode based on Integer32"""
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


_DfrapCfgCommMode_Type.__name__ = "Integer32"
_DfrapCfgCommMode_Object = MibScalar
dfrapCfgCommMode = _DfrapCfgCommMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 1),
    _DfrapCfgCommMode_Type()
)
dfrapCfgCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommMode.setStatus("mandatory")


class _DfrapCfgCommBaud_Type(Integer32):
    """Custom type dfrapCfgCommBaud based on Integer32"""
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


_DfrapCfgCommBaud_Type.__name__ = "Integer32"
_DfrapCfgCommBaud_Object = MibScalar
dfrapCfgCommBaud = _DfrapCfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 2),
    _DfrapCfgCommBaud_Type()
)
dfrapCfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommBaud.setStatus("mandatory")


class _DfrapCfgCommDataBits_Type(Integer32):
    """Custom type dfrapCfgCommDataBits based on Integer32"""
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


_DfrapCfgCommDataBits_Type.__name__ = "Integer32"
_DfrapCfgCommDataBits_Object = MibScalar
dfrapCfgCommDataBits = _DfrapCfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 3),
    _DfrapCfgCommDataBits_Type()
)
dfrapCfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommDataBits.setStatus("mandatory")


class _DfrapCfgCommStopBits_Type(Integer32):
    """Custom type dfrapCfgCommStopBits based on Integer32"""
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


_DfrapCfgCommStopBits_Type.__name__ = "Integer32"
_DfrapCfgCommStopBits_Object = MibScalar
dfrapCfgCommStopBits = _DfrapCfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 4),
    _DfrapCfgCommStopBits_Type()
)
dfrapCfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommStopBits.setStatus("mandatory")


class _DfrapCfgCommParity_Type(Integer32):
    """Custom type dfrapCfgCommParity based on Integer32"""
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


_DfrapCfgCommParity_Type.__name__ = "Integer32"
_DfrapCfgCommParity_Object = MibScalar
dfrapCfgCommParity = _DfrapCfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 5),
    _DfrapCfgCommParity_Type()
)
dfrapCfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommParity.setStatus("mandatory")


class _DfrapCfgCommFlowCtrl_Type(Integer32):
    """Custom type dfrapCfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("no-flow-control", 1)
    )


_DfrapCfgCommFlowCtrl_Type.__name__ = "Integer32"
_DfrapCfgCommFlowCtrl_Object = MibScalar
dfrapCfgCommFlowCtrl = _DfrapCfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 4, 6),
    _DfrapCfgCommFlowCtrl_Type()
)
dfrapCfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCommFlowCtrl.setStatus("mandatory")
_DfrapCfgFrDLCITable_ObjectIdentity = ObjectIdentity
dfrapCfgFrDLCITable = _DfrapCfgFrDLCITable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 5)
)


class _DfrapCfgFrDLCIMode_Type(Integer32):
    """Custom type dfrapCfgFrDLCIMode based on Integer32"""
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
          ("fixed-dce", 6),
          ("inactive", 1),
          ("local", 2),
          ("piggyback", 5),
          ("remote", 3))
    )


_DfrapCfgFrDLCIMode_Type.__name__ = "Integer32"
_DfrapCfgFrDLCIMode_Object = MibScalar
dfrapCfgFrDLCIMode = _DfrapCfgFrDLCIMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 5, 1),
    _DfrapCfgFrDLCIMode_Type()
)
dfrapCfgFrDLCIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrDLCIMode.setStatus("mandatory")


class _DfrapCfgFrDLCIValue_Type(Integer32):
    """Custom type dfrapCfgFrDLCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 63487),
    )


_DfrapCfgFrDLCIValue_Type.__name__ = "Integer32"
_DfrapCfgFrDLCIValue_Object = MibScalar
dfrapCfgFrDLCIValue = _DfrapCfgFrDLCIValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 5, 2),
    _DfrapCfgFrDLCIValue_Type()
)
dfrapCfgFrDLCIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrDLCIValue.setStatus("mandatory")


class _DfrapCfgFrDLCIEncap_Type(Integer32):
    """Custom type dfrapCfgFrDLCIEncap based on Integer32"""
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


_DfrapCfgFrDLCIEncap_Type.__name__ = "Integer32"
_DfrapCfgFrDLCIEncap_Object = MibScalar
dfrapCfgFrDLCIEncap = _DfrapCfgFrDLCIEncap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 5, 3),
    _DfrapCfgFrDLCIEncap_Type()
)
dfrapCfgFrDLCIEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrDLCIEncap.setStatus("mandatory")


class _DfrapCfgFrDLCIMgmtDE_Type(Integer32):
    """Custom type dfrapCfgFrDLCIMgmtDE based on Integer32"""
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


_DfrapCfgFrDLCIMgmtDE_Type.__name__ = "Integer32"
_DfrapCfgFrDLCIMgmtDE_Object = MibScalar
dfrapCfgFrDLCIMgmtDE = _DfrapCfgFrDLCIMgmtDE_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 1, 5, 4),
    _DfrapCfgFrDLCIMgmtDE_Type()
)
dfrapCfgFrDLCIMgmtDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrDLCIMgmtDE.setStatus("mandatory")
_DfrapCfgAppTable_ObjectIdentity = ObjectIdentity
dfrapCfgAppTable = _DfrapCfgAppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2)
)


class _DfrapCfgAppClockSource_Type(Integer32):
    """Custom type dfrapCfgAppClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte", 3),
          ("internal", 1),
          ("network", 2))
    )


_DfrapCfgAppClockSource_Type.__name__ = "Integer32"
_DfrapCfgAppClockSource_Object = MibScalar
dfrapCfgAppClockSource = _DfrapCfgAppClockSource_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 1),
    _DfrapCfgAppClockSource_Type()
)
dfrapCfgAppClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppClockSource.setStatus("mandatory")


class _DfrapCfgAppCircuitId_Type(DisplayString):
    """Custom type dfrapCfgAppCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DfrapCfgAppCircuitId_Type.__name__ = "DisplayString"
_DfrapCfgAppCircuitId_Object = MibScalar
dfrapCfgAppCircuitId = _DfrapCfgAppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 2),
    _DfrapCfgAppCircuitId_Type()
)
dfrapCfgAppCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppCircuitId.setStatus("mandatory")


class _DfrapCfgAppType_Type(Integer32):
    """Custom type dfrapCfgAppType based on Integer32"""
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


_DfrapCfgAppType_Type.__name__ = "Integer32"
_DfrapCfgAppType_Object = MibScalar
dfrapCfgAppType = _DfrapCfgAppType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 3),
    _DfrapCfgAppType_Type()
)
dfrapCfgAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppType.setStatus("mandatory")


class _DfrapCfgAppFormat_Type(Integer32):
    """Custom type dfrapCfgAppFormat based on Integer32"""
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


_DfrapCfgAppFormat_Type.__name__ = "Integer32"
_DfrapCfgAppFormat_Object = MibScalar
dfrapCfgAppFormat = _DfrapCfgAppFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 4),
    _DfrapCfgAppFormat_Type()
)
dfrapCfgAppFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppFormat.setStatus("mandatory")


class _DfrapCfgAppLpbkTimeout_Type(Integer32):
    """Custom type dfrapCfgAppLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_DfrapCfgAppLpbkTimeout_Type.__name__ = "Integer32"
_DfrapCfgAppLpbkTimeout_Object = MibScalar
dfrapCfgAppLpbkTimeout = _DfrapCfgAppLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 5),
    _DfrapCfgAppLpbkTimeout_Type()
)
dfrapCfgAppLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppLpbkTimeout.setStatus("mandatory")


class _DfrapCfgAppPerfBuffLimit_Type(Integer32):
    """Custom type dfrapCfgAppPerfBuffLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_DfrapCfgAppPerfBuffLimit_Type.__name__ = "Integer32"
_DfrapCfgAppPerfBuffLimit_Object = MibScalar
dfrapCfgAppPerfBuffLimit = _DfrapCfgAppPerfBuffLimit_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 2, 10),
    _DfrapCfgAppPerfBuffLimit_Type()
)
dfrapCfgAppPerfBuffLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgAppPerfBuffLimit.setStatus("mandatory")
_DfrapCfgDdsTable_ObjectIdentity = ObjectIdentity
dfrapCfgDdsTable = _DfrapCfgDdsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 3)
)


class _DfrapCfgDdsLoopRate_Type(Integer32):
    """Custom type dfrapCfgDdsLoopRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifty-six", 1),
          ("sixty-four", 2))
    )


_DfrapCfgDdsLoopRate_Type.__name__ = "Integer32"
_DfrapCfgDdsLoopRate_Object = MibScalar
dfrapCfgDdsLoopRate = _DfrapCfgDdsLoopRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 3, 1),
    _DfrapCfgDdsLoopRate_Type()
)
dfrapCfgDdsLoopRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDdsLoopRate.setStatus("mandatory")


class _DfrapCfgDdsBPVThresholding_Type(Integer32):
    """Custom type dfrapCfgDdsBPVThresholding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-thresholding", 2),
          ("thresholding-at-10E-4", 1))
    )


_DfrapCfgDdsBPVThresholding_Type.__name__ = "Integer32"
_DfrapCfgDdsBPVThresholding_Object = MibScalar
dfrapCfgDdsBPVThresholding = _DfrapCfgDdsBPVThresholding_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 3, 2),
    _DfrapCfgDdsBPVThresholding_Type()
)
dfrapCfgDdsBPVThresholding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDdsBPVThresholding.setStatus("mandatory")
_DfrapCfgDteTable_ObjectIdentity = ObjectIdentity
dfrapCfgDteTable = _DfrapCfgDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4)
)


class _DfrapCfgDteIntfType_Type(Integer32):
    """Custom type dfrapCfgDteIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intf-rs449", 4),
          ("intf-v35", 3))
    )


_DfrapCfgDteIntfType_Type.__name__ = "Integer32"
_DfrapCfgDteIntfType_Object = MibScalar
dfrapCfgDteIntfType = _DfrapCfgDteIntfType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 1),
    _DfrapCfgDteIntfType_Type()
)
dfrapCfgDteIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgDteIntfType.setStatus("mandatory")


class _DfrapCfgDteClockMode_Type(Integer32):
    """Custom type dfrapCfgDteClockMode based on Integer32"""
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


_DfrapCfgDteClockMode_Type.__name__ = "Integer32"
_DfrapCfgDteClockMode_Object = MibScalar
dfrapCfgDteClockMode = _DfrapCfgDteClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 3),
    _DfrapCfgDteClockMode_Type()
)
dfrapCfgDteClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteClockMode.setStatus("mandatory")


class _DfrapCfgDteTiming_Type(Integer32):
    """Custom type dfrapCfgDteTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop-1", 1),
          ("loop-2", 2))
    )


_DfrapCfgDteTiming_Type.__name__ = "Integer32"
_DfrapCfgDteTiming_Object = MibScalar
dfrapCfgDteTiming = _DfrapCfgDteTiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 4),
    _DfrapCfgDteTiming_Type()
)
dfrapCfgDteTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteTiming.setStatus("mandatory")


class _DfrapCfgDteRts_Type(Integer32):
    """Custom type dfrapCfgDteRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external-from-dte", 2),
          ("internal-held-active", 1))
    )


_DfrapCfgDteRts_Type.__name__ = "Integer32"
_DfrapCfgDteRts_Object = MibScalar
dfrapCfgDteRts = _DfrapCfgDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 15),
    _DfrapCfgDteRts_Type()
)
dfrapCfgDteRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteRts.setStatus("mandatory")


class _DfrapCfgDteDtr_Type(Integer32):
    """Custom type dfrapCfgDteDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external-from-dte", 2),
          ("internal-held-active", 1))
    )


_DfrapCfgDteDtr_Type.__name__ = "Integer32"
_DfrapCfgDteDtr_Object = MibScalar
dfrapCfgDteDtr = _DfrapCfgDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 16),
    _DfrapCfgDteDtr_Type()
)
dfrapCfgDteDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteDtr.setStatus("mandatory")


class _DfrapCfgDteDcdOutput_Type(Integer32):
    """Custom type dfrapCfgDteDcdOutput based on Integer32"""
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
        *(("follow-carrier", 3),
          ("follow-carrier-rts", 6),
          ("follow-lmi-carr-rts", 8),
          ("follow-rts", 5),
          ("follow-sync-rts", 7),
          ("follow-test", 4),
          ("signal-off", 1),
          ("signal-on", 2))
    )


_DfrapCfgDteDcdOutput_Type.__name__ = "Integer32"
_DfrapCfgDteDcdOutput_Object = MibScalar
dfrapCfgDteDcdOutput = _DfrapCfgDteDcdOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 18),
    _DfrapCfgDteDcdOutput_Type()
)
dfrapCfgDteDcdOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteDcdOutput.setStatus("mandatory")


class _DfrapCfgDteDsrOutput_Type(Integer32):
    """Custom type dfrapCfgDteDsrOutput based on Integer32"""
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
        *(("follow-carrier", 3),
          ("follow-carrier-rts", 6),
          ("follow-lmi-carr-rts", 8),
          ("follow-rts", 5),
          ("follow-sync-rts", 7),
          ("follow-test", 4),
          ("signal-off", 1),
          ("signal-on", 2))
    )


_DfrapCfgDteDsrOutput_Type.__name__ = "Integer32"
_DfrapCfgDteDsrOutput_Object = MibScalar
dfrapCfgDteDsrOutput = _DfrapCfgDteDsrOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 19),
    _DfrapCfgDteDsrOutput_Type()
)
dfrapCfgDteDsrOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteDsrOutput.setStatus("mandatory")


class _DfrapCfgDteCtsOutput_Type(Integer32):
    """Custom type dfrapCfgDteCtsOutput based on Integer32"""
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
        *(("follow-carrier", 3),
          ("follow-carrier-rts", 6),
          ("follow-lmi-carr-rts", 8),
          ("follow-rts", 5),
          ("follow-sync-rts", 7),
          ("follow-test", 4),
          ("signal-off", 1),
          ("signal-on", 2))
    )


_DfrapCfgDteCtsOutput_Type.__name__ = "Integer32"
_DfrapCfgDteCtsOutput_Object = MibScalar
dfrapCfgDteCtsOutput = _DfrapCfgDteCtsOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 4, 20),
    _DfrapCfgDteCtsOutput_Type()
)
dfrapCfgDteCtsOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgDteCtsOutput.setStatus("mandatory")
_DfrapCfgFrTable_ObjectIdentity = ObjectIdentity
dfrapCfgFrTable = _DfrapCfgFrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5)
)


class _DfrapCfgFrAddrLen_Type(Integer32):
    """Custom type dfrapCfgFrAddrLen based on Integer32"""
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


_DfrapCfgFrAddrLen_Type.__name__ = "Integer32"
_DfrapCfgFrAddrLen_Object = MibScalar
dfrapCfgFrAddrLen = _DfrapCfgFrAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 1),
    _DfrapCfgFrAddrLen_Type()
)
dfrapCfgFrAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrAddrLen.setStatus("mandatory")


class _DfrapCfgFrCrcMode_Type(Integer32):
    """Custom type dfrapCfgFrCrcMode based on Integer32"""
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


_DfrapCfgFrCrcMode_Type.__name__ = "Integer32"
_DfrapCfgFrCrcMode_Object = MibScalar
dfrapCfgFrCrcMode = _DfrapCfgFrCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 2),
    _DfrapCfgFrCrcMode_Type()
)
dfrapCfgFrCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrCrcMode.setStatus("mandatory")


class _DfrapCfgFrLmiType_Type(Integer32):
    """Custom type dfrapCfgFrLmiType based on Integer32"""
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


_DfrapCfgFrLmiType_Type.__name__ = "Integer32"
_DfrapCfgFrLmiType_Object = MibScalar
dfrapCfgFrLmiType = _DfrapCfgFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 3),
    _DfrapCfgFrLmiType_Type()
)
dfrapCfgFrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrLmiType.setStatus("mandatory")


class _DfrapCfgFrLmiInactivityTimeout_Type(Integer32):
    """Custom type dfrapCfgFrLmiInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DfrapCfgFrLmiInactivityTimeout_Type.__name__ = "Integer32"
_DfrapCfgFrLmiInactivityTimeout_Object = MibScalar
dfrapCfgFrLmiInactivityTimeout = _DfrapCfgFrLmiInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 4),
    _DfrapCfgFrLmiInactivityTimeout_Type()
)
dfrapCfgFrLmiInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrLmiInactivityTimeout.setStatus("mandatory")


class _DfrapCfgFrLmiKeepaliveTimeout_Type(Integer32):
    """Custom type dfrapCfgFrLmiKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_DfrapCfgFrLmiKeepaliveTimeout_Type.__name__ = "Integer32"
_DfrapCfgFrLmiKeepaliveTimeout_Object = MibScalar
dfrapCfgFrLmiKeepaliveTimeout = _DfrapCfgFrLmiKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 5),
    _DfrapCfgFrLmiKeepaliveTimeout_Type()
)
dfrapCfgFrLmiKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrLmiKeepaliveTimeout.setStatus("mandatory")


class _DfrapCfgFrAddrResMode_Type(Integer32):
    """Custom type dfrapCfgFrAddrResMode based on Integer32"""
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


_DfrapCfgFrAddrResMode_Type.__name__ = "Integer32"
_DfrapCfgFrAddrResMode_Object = MibScalar
dfrapCfgFrAddrResMode = _DfrapCfgFrAddrResMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 6),
    _DfrapCfgFrAddrResMode_Type()
)
dfrapCfgFrAddrResMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrAddrResMode.setStatus("mandatory")


class _DfrapCfgFrAddrResInarpTimer_Type(Integer32):
    """Custom type dfrapCfgFrAddrResInarpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DfrapCfgFrAddrResInarpTimer_Type.__name__ = "Integer32"
_DfrapCfgFrAddrResInarpTimer_Object = MibScalar
dfrapCfgFrAddrResInarpTimer = _DfrapCfgFrAddrResInarpTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 7),
    _DfrapCfgFrAddrResInarpTimer_Type()
)
dfrapCfgFrAddrResInarpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrAddrResInarpTimer.setStatus("mandatory")


class _DfrapCfgFrLmiFullStatus_Type(Integer32):
    """Custom type dfrapCfgFrLmiFullStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DfrapCfgFrLmiFullStatus_Type.__name__ = "Integer32"
_DfrapCfgFrLmiFullStatus_Object = MibScalar
dfrapCfgFrLmiFullStatus = _DfrapCfgFrLmiFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 8),
    _DfrapCfgFrLmiFullStatus_Type()
)
dfrapCfgFrLmiFullStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrLmiFullStatus.setStatus("mandatory")


class _DfrapCfgFrAddrResDlcis_Type(Integer32):
    """Custom type dfrapCfgFrAddrResDlcis based on Integer32"""
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
        *(("ddsmulti", 3),
          ("dtemulti", 4),
          ("multiple", 2),
          ("single", 1))
    )


_DfrapCfgFrAddrResDlcis_Type.__name__ = "Integer32"
_DfrapCfgFrAddrResDlcis_Object = MibScalar
dfrapCfgFrAddrResDlcis = _DfrapCfgFrAddrResDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 5, 9),
    _DfrapCfgFrAddrResDlcis_Type()
)
dfrapCfgFrAddrResDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrAddrResDlcis.setStatus("mandatory")
_DfrapCfgVnipTable_ObjectIdentity = ObjectIdentity
dfrapCfgVnipTable = _DfrapCfgVnipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6)
)


class _DfrapCfgVnipMode_Type(Integer32):
    """Custom type dfrapCfgVnipMode based on Integer32"""
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
          ("dds", 3),
          ("dte", 2),
          ("inactive", 1))
    )


_DfrapCfgVnipMode_Type.__name__ = "Integer32"
_DfrapCfgVnipMode_Object = MibScalar
dfrapCfgVnipMode = _DfrapCfgVnipMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 1),
    _DfrapCfgVnipMode_Type()
)
dfrapCfgVnipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgVnipMode.setStatus("mandatory")


class _DfrapCfgVnipInitTimer_Type(Integer32):
    """Custom type dfrapCfgVnipInitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DfrapCfgVnipInitTimer_Type.__name__ = "Integer32"
_DfrapCfgVnipInitTimer_Object = MibScalar
dfrapCfgVnipInitTimer = _DfrapCfgVnipInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 2),
    _DfrapCfgVnipInitTimer_Type()
)
dfrapCfgVnipInitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgVnipInitTimer.setStatus("mandatory")


class _DfrapCfgVnipKeepAliveTimer_Type(Integer32):
    """Custom type dfrapCfgVnipKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DfrapCfgVnipKeepAliveTimer_Type.__name__ = "Integer32"
_DfrapCfgVnipKeepAliveTimer_Object = MibScalar
dfrapCfgVnipKeepAliveTimer = _DfrapCfgVnipKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 3),
    _DfrapCfgVnipKeepAliveTimer_Type()
)
dfrapCfgVnipKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgVnipKeepAliveTimer.setStatus("mandatory")


class _DfrapCfgVnipInactivityTimer_Type(Integer32):
    """Custom type dfrapCfgVnipInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DfrapCfgVnipInactivityTimer_Type.__name__ = "Integer32"
_DfrapCfgVnipInactivityTimer_Object = MibScalar
dfrapCfgVnipInactivityTimer = _DfrapCfgVnipInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 4),
    _DfrapCfgVnipInactivityTimer_Type()
)
dfrapCfgVnipInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgVnipInactivityTimer.setStatus("mandatory")


class _DfrapCfgVnipTransitDelayFrequency_Type(Integer32):
    """Custom type dfrapCfgVnipTransitDelayFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_DfrapCfgVnipTransitDelayFrequency_Type.__name__ = "Integer32"
_DfrapCfgVnipTransitDelayFrequency_Object = MibScalar
dfrapCfgVnipTransitDelayFrequency = _DfrapCfgVnipTransitDelayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 5),
    _DfrapCfgVnipTransitDelayFrequency_Type()
)
dfrapCfgVnipTransitDelayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgVnipTransitDelayFrequency.setStatus("mandatory")
_DfrapCfgTransitDelayTable_Object = MibTable
dfrapCfgTransitDelayTable = _DfrapCfgTransitDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20)
)
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayTable.setStatus("mandatory")
_DfrapCfgTransitDelayEntry_Object = MibTableRow
dfrapCfgTransitDelayEntry = _DfrapCfgTransitDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1)
)
dfrapCfgTransitDelayEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgTransitDelayInterface"),
    (0, "DFRAP-MIB", "dfrapCfgTransitDelayDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayEntry.setStatus("mandatory")


class _DfrapCfgTransitDelayInterface_Type(Integer32):
    """Custom type dfrapCfgTransitDelayInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dds-interface", 2),
          ("dte-interface", 1))
    )


_DfrapCfgTransitDelayInterface_Type.__name__ = "Integer32"
_DfrapCfgTransitDelayInterface_Object = MibTableColumn
dfrapCfgTransitDelayInterface = _DfrapCfgTransitDelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1, 1),
    _DfrapCfgTransitDelayInterface_Type()
)
dfrapCfgTransitDelayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayInterface.setStatus("mandatory")
_DfrapCfgTransitDelayDlciValue_Type = Integer32
_DfrapCfgTransitDelayDlciValue_Object = MibTableColumn
dfrapCfgTransitDelayDlciValue = _DfrapCfgTransitDelayDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1, 2),
    _DfrapCfgTransitDelayDlciValue_Type()
)
dfrapCfgTransitDelayDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayDlciValue.setStatus("mandatory")


class _DfrapCfgTransitDelayNumHops_Type(Integer32):
    """Custom type dfrapCfgTransitDelayNumHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DfrapCfgTransitDelayNumHops_Type.__name__ = "Integer32"
_DfrapCfgTransitDelayNumHops_Object = MibTableColumn
dfrapCfgTransitDelayNumHops = _DfrapCfgTransitDelayNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1, 4),
    _DfrapCfgTransitDelayNumHops_Type()
)
dfrapCfgTransitDelayNumHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayNumHops.setStatus("mandatory")


class _DfrapCfgTransitDelayRcvSummaryCancel_Type(Integer32):
    """Custom type dfrapCfgTransitDelayRcvSummaryCancel based on Integer32"""
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


_DfrapCfgTransitDelayRcvSummaryCancel_Type.__name__ = "Integer32"
_DfrapCfgTransitDelayRcvSummaryCancel_Object = MibTableColumn
dfrapCfgTransitDelayRcvSummaryCancel = _DfrapCfgTransitDelayRcvSummaryCancel_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1, 5),
    _DfrapCfgTransitDelayRcvSummaryCancel_Type()
)
dfrapCfgTransitDelayRcvSummaryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayRcvSummaryCancel.setStatus("mandatory")


class _DfrapCfgTransitDelayThreshold_Type(Integer32):
    """Custom type dfrapCfgTransitDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_DfrapCfgTransitDelayThreshold_Type.__name__ = "Integer32"
_DfrapCfgTransitDelayThreshold_Object = MibTableColumn
dfrapCfgTransitDelayThreshold = _DfrapCfgTransitDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 20, 1, 6),
    _DfrapCfgTransitDelayThreshold_Type()
)
dfrapCfgTransitDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayThreshold.setStatus("mandatory")
_DfrapCfgTDDeleteTable_Object = MibTable
dfrapCfgTDDeleteTable = _DfrapCfgTDDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 21)
)
if mibBuilder.loadTexts:
    dfrapCfgTDDeleteTable.setStatus("mandatory")
_DfrapCfgTDDeleteEntry_Object = MibTableRow
dfrapCfgTDDeleteEntry = _DfrapCfgTDDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 21, 1)
)
dfrapCfgTDDeleteEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgTDDeleteInterface"),
)
if mibBuilder.loadTexts:
    dfrapCfgTDDeleteEntry.setStatus("mandatory")


class _DfrapCfgTDDeleteInterface_Type(Integer32):
    """Custom type dfrapCfgTDDeleteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dds-interface", 2),
          ("dte-interface", 1))
    )


_DfrapCfgTDDeleteInterface_Type.__name__ = "Integer32"
_DfrapCfgTDDeleteInterface_Object = MibTableColumn
dfrapCfgTDDeleteInterface = _DfrapCfgTDDeleteInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 21, 1, 1),
    _DfrapCfgTDDeleteInterface_Type()
)
dfrapCfgTDDeleteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfrapCfgTDDeleteInterface.setStatus("mandatory")
_DfrapCfgTDDeleteDlciValue_Type = Integer32
_DfrapCfgTDDeleteDlciValue_Object = MibTableColumn
dfrapCfgTDDeleteDlciValue = _DfrapCfgTDDeleteDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 21, 1, 2),
    _DfrapCfgTDDeleteDlciValue_Type()
)
dfrapCfgTDDeleteDlciValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgTDDeleteDlciValue.setStatus("mandatory")


class _DfrapCfgTransitDelayTableClear_Type(Integer32):
    """Custom type dfrapCfgTransitDelayTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_DfrapCfgTransitDelayTableClear_Type.__name__ = "Integer32"
_DfrapCfgTransitDelayTableClear_Object = MibScalar
dfrapCfgTransitDelayTableClear = _DfrapCfgTransitDelayTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 6, 22),
    _DfrapCfgTransitDelayTableClear_Type()
)
dfrapCfgTransitDelayTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgTransitDelayTableClear.setStatus("mandatory")
_DfrapCfgFrPerf_ObjectIdentity = ObjectIdentity
dfrapCfgFrPerf = _DfrapCfgFrPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7)
)
_DfrapCfgFrPerfDlciNamesTable_Object = MibTable
dfrapCfgFrPerfDlciNamesTable = _DfrapCfgFrPerfDlciNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesTable.setStatus("mandatory")
_DfrapCfgFrPerfDlciNamesEntry_Object = MibTableRow
dfrapCfgFrPerfDlciNamesEntry = _DfrapCfgFrPerfDlciNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1)
)
dfrapCfgFrPerfDlciNamesEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgFrPerfDlciNamesDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesEntry.setStatus("mandatory")
_DfrapCfgFrPerfDlciNamesDlciValue_Type = Integer32
_DfrapCfgFrPerfDlciNamesDlciValue_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesDlciValue = _DfrapCfgFrPerfDlciNamesDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 1),
    _DfrapCfgFrPerfDlciNamesDlciValue_Type()
)
dfrapCfgFrPerfDlciNamesDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesDlciValue.setStatus("mandatory")


class _DfrapCfgFrPerfDlciNamesDlciName_Type(DisplayString):
    """Custom type dfrapCfgFrPerfDlciNamesDlciName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapCfgFrPerfDlciNamesDlciName_Type.__name__ = "DisplayString"
_DfrapCfgFrPerfDlciNamesDlciName_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesDlciName = _DfrapCfgFrPerfDlciNamesDlciName_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 2),
    _DfrapCfgFrPerfDlciNamesDlciName_Type()
)
dfrapCfgFrPerfDlciNamesDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesDlciName.setStatus("mandatory")
_DfrapCfgFrPerfDlciNamesCirValue_Type = Integer32
_DfrapCfgFrPerfDlciNamesCirValue_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesCirValue = _DfrapCfgFrPerfDlciNamesCirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 3),
    _DfrapCfgFrPerfDlciNamesCirValue_Type()
)
dfrapCfgFrPerfDlciNamesCirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesCirValue.setStatus("mandatory")


class _DfrapCfgFrPerfDlciNamesCirType_Type(Integer32):
    """Custom type dfrapCfgFrPerfDlciNamesCirType based on Integer32"""
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


_DfrapCfgFrPerfDlciNamesCirType_Type.__name__ = "Integer32"
_DfrapCfgFrPerfDlciNamesCirType_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesCirType = _DfrapCfgFrPerfDlciNamesCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 4),
    _DfrapCfgFrPerfDlciNamesCirType_Type()
)
dfrapCfgFrPerfDlciNamesCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesCirType.setStatus("mandatory")


class _DfrapCfgFrPerfDlciNamesUtilThreshold_Type(Integer32):
    """Custom type dfrapCfgFrPerfDlciNamesUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DfrapCfgFrPerfDlciNamesUtilThreshold_Type.__name__ = "Integer32"
_DfrapCfgFrPerfDlciNamesUtilThreshold_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesUtilThreshold = _DfrapCfgFrPerfDlciNamesUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 5),
    _DfrapCfgFrPerfDlciNamesUtilThreshold_Type()
)
dfrapCfgFrPerfDlciNamesUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesUtilThreshold.setStatus("mandatory")
_DfrapCfgFrPerfDlciNamesEirValue_Type = Integer32
_DfrapCfgFrPerfDlciNamesEirValue_Object = MibTableColumn
dfrapCfgFrPerfDlciNamesEirValue = _DfrapCfgFrPerfDlciNamesEirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 1, 1, 6),
    _DfrapCfgFrPerfDlciNamesEirValue_Type()
)
dfrapCfgFrPerfDlciNamesEirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesEirValue.setStatus("mandatory")
_DfrapCfgFrPerfDlciNamesDelete_Type = Integer32
_DfrapCfgFrPerfDlciNamesDelete_Object = MibScalar
dfrapCfgFrPerfDlciNamesDelete = _DfrapCfgFrPerfDlciNamesDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 2),
    _DfrapCfgFrPerfDlciNamesDelete_Type()
)
dfrapCfgFrPerfDlciNamesDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesDelete.setStatus("mandatory")
_DfrapCfgFrPerfTimers_ObjectIdentity = ObjectIdentity
dfrapCfgFrPerfTimers = _DfrapCfgFrPerfTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 3)
)


class _DfrapCfgFrPerfTimersSTInterval_Type(Integer32):
    """Custom type dfrapCfgFrPerfTimersSTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_DfrapCfgFrPerfTimersSTInterval_Type.__name__ = "Integer32"
_DfrapCfgFrPerfTimersSTInterval_Object = MibScalar
dfrapCfgFrPerfTimersSTInterval = _DfrapCfgFrPerfTimersSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 3, 1),
    _DfrapCfgFrPerfTimersSTInterval_Type()
)
dfrapCfgFrPerfTimersSTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfTimersSTInterval.setStatus("mandatory")


class _DfrapCfgFrPerfTimersLTInterval_Type(Integer32):
    """Custom type dfrapCfgFrPerfTimersLTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_DfrapCfgFrPerfTimersLTInterval_Type.__name__ = "Integer32"
_DfrapCfgFrPerfTimersLTInterval_Object = MibScalar
dfrapCfgFrPerfTimersLTInterval = _DfrapCfgFrPerfTimersLTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 3, 2),
    _DfrapCfgFrPerfTimersLTInterval_Type()
)
dfrapCfgFrPerfTimersLTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfTimersLTInterval.setStatus("mandatory")
_DfrapCfgFrPerfUserProtocolsTable_Object = MibTable
dfrapCfgFrPerfUserProtocolsTable = _DfrapCfgFrPerfUserProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 4)
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUserProtocolsTable.setStatus("mandatory")
_DfrapCfgFrPerfUserProtocolsEntry_Object = MibTableRow
dfrapCfgFrPerfUserProtocolsEntry = _DfrapCfgFrPerfUserProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 4, 1)
)
dfrapCfgFrPerfUserProtocolsEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgFrPerfUserProtocolsIndex"),
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUserProtocolsEntry.setStatus("mandatory")
_DfrapCfgFrPerfUserProtocolsIndex_Type = Integer32
_DfrapCfgFrPerfUserProtocolsIndex_Object = MibTableColumn
dfrapCfgFrPerfUserProtocolsIndex = _DfrapCfgFrPerfUserProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 4, 1, 1),
    _DfrapCfgFrPerfUserProtocolsIndex_Type()
)
dfrapCfgFrPerfUserProtocolsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUserProtocolsIndex.setStatus("mandatory")
_DfrapCfgFrPerfUserProtocolsPortNum_Type = Integer32
_DfrapCfgFrPerfUserProtocolsPortNum_Object = MibTableColumn
dfrapCfgFrPerfUserProtocolsPortNum = _DfrapCfgFrPerfUserProtocolsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 4, 1, 2),
    _DfrapCfgFrPerfUserProtocolsPortNum_Type()
)
dfrapCfgFrPerfUserProtocolsPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUserProtocolsPortNum.setStatus("mandatory")
_DfrapCfgFrPerfLTDlciFilterTable_Object = MibTable
dfrapCfgFrPerfLTDlciFilterTable = _DfrapCfgFrPerfLTDlciFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 5)
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTDlciFilterTable.setStatus("mandatory")
_DfrapCfgFrPerfLTDlciFilterEntry_Object = MibTableRow
dfrapCfgFrPerfLTDlciFilterEntry = _DfrapCfgFrPerfLTDlciFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 5, 1)
)
dfrapCfgFrPerfLTDlciFilterEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgFrPerfLTDlciFilterIndex"),
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTDlciFilterEntry.setStatus("mandatory")
_DfrapCfgFrPerfLTDlciFilterIndex_Type = Integer32
_DfrapCfgFrPerfLTDlciFilterIndex_Object = MibTableColumn
dfrapCfgFrPerfLTDlciFilterIndex = _DfrapCfgFrPerfLTDlciFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 5, 1, 1),
    _DfrapCfgFrPerfLTDlciFilterIndex_Type()
)
dfrapCfgFrPerfLTDlciFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTDlciFilterIndex.setStatus("mandatory")
_DfrapCfgFrPerfLTDlciFilterDlciNum_Type = Integer32
_DfrapCfgFrPerfLTDlciFilterDlciNum_Object = MibTableColumn
dfrapCfgFrPerfLTDlciFilterDlciNum = _DfrapCfgFrPerfLTDlciFilterDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 5, 1, 2),
    _DfrapCfgFrPerfLTDlciFilterDlciNum_Type()
)
dfrapCfgFrPerfLTDlciFilterDlciNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTDlciFilterDlciNum.setStatus("mandatory")
_DfrapCfgFrPerfLTProtocolFilterTable_Object = MibTable
dfrapCfgFrPerfLTProtocolFilterTable = _DfrapCfgFrPerfLTProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 6)
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTProtocolFilterTable.setStatus("mandatory")
_DfrapCfgFrPerfLTProtocolFilterEntry_Object = MibTableRow
dfrapCfgFrPerfLTProtocolFilterEntry = _DfrapCfgFrPerfLTProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 6, 1)
)
dfrapCfgFrPerfLTProtocolFilterEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapCfgFrPerfLTProtocolFilterIndex"),
)
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTProtocolFilterEntry.setStatus("mandatory")
_DfrapCfgFrPerfLTProtocolFilterIndex_Type = Integer32
_DfrapCfgFrPerfLTProtocolFilterIndex_Object = MibTableColumn
dfrapCfgFrPerfLTProtocolFilterIndex = _DfrapCfgFrPerfLTProtocolFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 6, 1, 1),
    _DfrapCfgFrPerfLTProtocolFilterIndex_Type()
)
dfrapCfgFrPerfLTProtocolFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTProtocolFilterIndex.setStatus("mandatory")


class _DfrapCfgFrPerfLTProtocolFilterProtocol_Type(Integer32):
    """Custom type dfrapCfgFrPerfLTProtocolFilterProtocol based on Integer32"""
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
          ("ftp-udp-ip-rx-bc", 24),
          ("ftp-udp-ip-tx-bc", 23),
          ("gp-mem-query-icmp-ip-rx-bc", 68),
          ("gp-mem-query-icmp-ip-tx-bc", 67),
          ("gp-mem-reduct-icmp-ip-rx-bc", 72),
          ("gp-mem-reduct-icmp-ip-tx-bc", 71),
          ("gp-mem-report-icmp-ip-rx-bc", 70),
          ("gp-mem-report-icmp-ip-tx-bc", 69),
          ("http-tcp-ip-rx-bc", 14),
          ("http-tcp-ip-tx-bc", 13),
          ("http-udp-ip-rx-bc", 32),
          ("http-udp-ip-tx-bc", 31),
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
          ("smtp-udp-ip-rx-bc", 28),
          ("smtp-udp-ip-tx-bc", 27),
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
          ("snmp-tcp-ip-rx-bc", 18),
          ("snmp-tcp-ip-tx-bc", 17),
          ("snmp-udp-ip-rx-bc", 36),
          ("snmp-udp-ip-tx-bc", 35),
          ("snmptrap-tcp-ip-rx-bc", 20),
          ("snmptrap-tcp-ip-tx-bc", 19),
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
          ("telnet-udp-ip-rx-bc", 26),
          ("telnet-udp-ip-tx-bc", 25),
          ("tftp-tcp-ip-rx-bc", 12),
          ("tftp-tcp-ip-tx-bc", 11),
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


_DfrapCfgFrPerfLTProtocolFilterProtocol_Type.__name__ = "Integer32"
_DfrapCfgFrPerfLTProtocolFilterProtocol_Object = MibTableColumn
dfrapCfgFrPerfLTProtocolFilterProtocol = _DfrapCfgFrPerfLTProtocolFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 6, 1, 2),
    _DfrapCfgFrPerfLTProtocolFilterProtocol_Type()
)
dfrapCfgFrPerfLTProtocolFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTProtocolFilterProtocol.setStatus("mandatory")


class _DfrapCfgFrPerfDlciDefaultUtilThreshold_Type(Integer32):
    """Custom type dfrapCfgFrPerfDlciDefaultUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DfrapCfgFrPerfDlciDefaultUtilThreshold_Type.__name__ = "Integer32"
_DfrapCfgFrPerfDlciDefaultUtilThreshold_Object = MibScalar
dfrapCfgFrPerfDlciDefaultUtilThreshold = _DfrapCfgFrPerfDlciDefaultUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 7),
    _DfrapCfgFrPerfDlciDefaultUtilThreshold_Type()
)
dfrapCfgFrPerfDlciDefaultUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciDefaultUtilThreshold.setStatus("mandatory")


class _DfrapCfgFrPerfDlciUtilDuration_Type(Integer32):
    """Custom type dfrapCfgFrPerfDlciUtilDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DfrapCfgFrPerfDlciUtilDuration_Type.__name__ = "Integer32"
_DfrapCfgFrPerfDlciUtilDuration_Object = MibScalar
dfrapCfgFrPerfDlciUtilDuration = _DfrapCfgFrPerfDlciUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 8),
    _DfrapCfgFrPerfDlciUtilDuration_Type()
)
dfrapCfgFrPerfDlciUtilDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciUtilDuration.setStatus("mandatory")


class _DfrapCfgFrPerfDlciNamesTableClear_Type(Integer32):
    """Custom type dfrapCfgFrPerfDlciNamesTableClear based on Integer32"""
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


_DfrapCfgFrPerfDlciNamesTableClear_Type.__name__ = "Integer32"
_DfrapCfgFrPerfDlciNamesTableClear_Object = MibScalar
dfrapCfgFrPerfDlciNamesTableClear = _DfrapCfgFrPerfDlciNamesTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 9),
    _DfrapCfgFrPerfDlciNamesTableClear_Type()
)
dfrapCfgFrPerfDlciNamesTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfDlciNamesTableClear.setStatus("mandatory")


class _DfrapCfgFrPerfUserProtocolsTableClear_Type(Integer32):
    """Custom type dfrapCfgFrPerfUserProtocolsTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_DfrapCfgFrPerfUserProtocolsTableClear_Type.__name__ = "Integer32"
_DfrapCfgFrPerfUserProtocolsTableClear_Object = MibScalar
dfrapCfgFrPerfUserProtocolsTableClear = _DfrapCfgFrPerfUserProtocolsTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 10),
    _DfrapCfgFrPerfUserProtocolsTableClear_Type()
)
dfrapCfgFrPerfUserProtocolsTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUserProtocolsTableClear.setStatus("mandatory")


class _DfrapCfgFrPerfLTDlciFilterTableClear_Type(Integer32):
    """Custom type dfrapCfgFrPerfLTDlciFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_DfrapCfgFrPerfLTDlciFilterTableClear_Type.__name__ = "Integer32"
_DfrapCfgFrPerfLTDlciFilterTableClear_Object = MibScalar
dfrapCfgFrPerfLTDlciFilterTableClear = _DfrapCfgFrPerfLTDlciFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 11),
    _DfrapCfgFrPerfLTDlciFilterTableClear_Type()
)
dfrapCfgFrPerfLTDlciFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTDlciFilterTableClear.setStatus("mandatory")


class _DfrapCfgFrPerfLTProtocolFilterTableClear_Type(Integer32):
    """Custom type dfrapCfgFrPerfLTProtocolFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_DfrapCfgFrPerfLTProtocolFilterTableClear_Type.__name__ = "Integer32"
_DfrapCfgFrPerfLTProtocolFilterTableClear_Object = MibScalar
dfrapCfgFrPerfLTProtocolFilterTableClear = _DfrapCfgFrPerfLTProtocolFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 12),
    _DfrapCfgFrPerfLTProtocolFilterTableClear_Type()
)
dfrapCfgFrPerfLTProtocolFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfLTProtocolFilterTableClear.setStatus("mandatory")


class _DfrapCfgFrPerfUnprovDlcisDelete_Type(Integer32):
    """Custom type dfrapCfgFrPerfUnprovDlcisDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete-unprov", 1)
    )


_DfrapCfgFrPerfUnprovDlcisDelete_Type.__name__ = "Integer32"
_DfrapCfgFrPerfUnprovDlcisDelete_Object = MibScalar
dfrapCfgFrPerfUnprovDlcisDelete = _DfrapCfgFrPerfUnprovDlcisDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 7, 13),
    _DfrapCfgFrPerfUnprovDlcisDelete_Type()
)
dfrapCfgFrPerfUnprovDlcisDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgFrPerfUnprovDlcisDelete.setStatus("mandatory")
_DfrapCfgSecurityTable_ObjectIdentity = ObjectIdentity
dfrapCfgSecurityTable = _DfrapCfgSecurityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8)
)


class _DfrapCfgTelnetCliLcdPassword_Type(DisplayString):
    """Custom type dfrapCfgTelnetCliLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgTelnetCliLcdPassword_Type.__name__ = "DisplayString"
_DfrapCfgTelnetCliLcdPassword_Object = MibScalar
dfrapCfgTelnetCliLcdPassword = _DfrapCfgTelnetCliLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 1),
    _DfrapCfgTelnetCliLcdPassword_Type()
)
dfrapCfgTelnetCliLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTelnetCliLcdPassword.setStatus("mandatory")


class _DfrapCfgTftpPassword_Type(DisplayString):
    """Custom type dfrapCfgTftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgTftpPassword_Type.__name__ = "DisplayString"
_DfrapCfgTftpPassword_Object = MibScalar
dfrapCfgTftpPassword = _DfrapCfgTftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 2),
    _DfrapCfgTftpPassword_Type()
)
dfrapCfgTftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgTftpPassword.setStatus("mandatory")


class _DfrapCfgCliPassword_Type(DisplayString):
    """Custom type dfrapCfgCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgCliPassword_Type.__name__ = "DisplayString"
_DfrapCfgCliPassword_Object = MibScalar
dfrapCfgCliPassword = _DfrapCfgCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 3),
    _DfrapCfgCliPassword_Type()
)
dfrapCfgCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgCliPassword.setStatus("mandatory")


class _DfrapCfgLcdPassword_Type(DisplayString):
    """Custom type dfrapCfgLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgLcdPassword_Type.__name__ = "DisplayString"
_DfrapCfgLcdPassword_Object = MibScalar
dfrapCfgLcdPassword = _DfrapCfgLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 4),
    _DfrapCfgLcdPassword_Type()
)
dfrapCfgLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgLcdPassword.setStatus("mandatory")


class _DfrapCfgGetCommunityString_Type(DisplayString):
    """Custom type dfrapCfgGetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapCfgGetCommunityString_Type.__name__ = "DisplayString"
_DfrapCfgGetCommunityString_Object = MibScalar
dfrapCfgGetCommunityString = _DfrapCfgGetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 5),
    _DfrapCfgGetCommunityString_Type()
)
dfrapCfgGetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgGetCommunityString.setStatus("mandatory")


class _DfrapCfgSetCommunityString_Type(DisplayString):
    """Custom type dfrapCfgSetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfrapCfgSetCommunityString_Type.__name__ = "DisplayString"
_DfrapCfgSetCommunityString_Object = MibScalar
dfrapCfgSetCommunityString = _DfrapCfgSetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 8, 6),
    _DfrapCfgSetCommunityString_Type()
)
dfrapCfgSetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgSetCommunityString.setStatus("mandatory")


class _DfrapCfgLock_Type(Integer32):
    """Custom type dfrapCfgLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_DfrapCfgLock_Type.__name__ = "Integer32"
_DfrapCfgLock_Object = MibScalar
dfrapCfgLock = _DfrapCfgLock_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 12),
    _DfrapCfgLock_Type()
)
dfrapCfgLock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgLock.setStatus("mandatory")
_DfrapCfgLockID_Type = IpAddress
_DfrapCfgLockID_Object = MibScalar
dfrapCfgLockID = _DfrapCfgLockID_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 13),
    _DfrapCfgLockID_Type()
)
dfrapCfgLockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgLockID.setStatus("mandatory")


class _DfrapCfgID_Type(DisplayString):
    """Custom type dfrapCfgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfrapCfgID_Type.__name__ = "DisplayString"
_DfrapCfgID_Object = MibScalar
dfrapCfgID = _DfrapCfgID_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 14),
    _DfrapCfgID_Type()
)
dfrapCfgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapCfgID.setStatus("mandatory")


class _DfrapCfgStatus_Type(Integer32):
    """Custom type dfrapCfgStatus based on Integer32"""
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


_DfrapCfgStatus_Type.__name__ = "Integer32"
_DfrapCfgStatus_Object = MibScalar
dfrapCfgStatus = _DfrapCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 15),
    _DfrapCfgStatus_Type()
)
dfrapCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgStatus.setStatus("mandatory")


class _DfrapCfgUnlock_Type(Integer32):
    """Custom type dfrapCfgUnlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("un-lock", 1)
    )


_DfrapCfgUnlock_Type.__name__ = "Integer32"
_DfrapCfgUnlock_Object = MibScalar
dfrapCfgUnlock = _DfrapCfgUnlock_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 16),
    _DfrapCfgUnlock_Type()
)
dfrapCfgUnlock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgUnlock.setStatus("mandatory")


class _DfrapCfgUpdate_Type(Integer32):
    """Custom type dfrapCfgUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_DfrapCfgUpdate_Type.__name__ = "Integer32"
_DfrapCfgUpdate_Object = MibScalar
dfrapCfgUpdate = _DfrapCfgUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 2, 17),
    _DfrapCfgUpdate_Type()
)
dfrapCfgUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapCfgUpdate.setStatus("mandatory")
_DfrapDiagnostics_ObjectIdentity = ObjectIdentity
dfrapDiagnostics = _DfrapDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 3)
)
_DfrapDiagUnitTable_ObjectIdentity = ObjectIdentity
dfrapDiagUnitTable = _DfrapDiagUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 1)
)


class _DfrapDiagUnitLocLoop_Type(Integer32):
    """Custom type dfrapDiagUnitLocLoop based on Integer32"""
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


_DfrapDiagUnitLocLoop_Type.__name__ = "Integer32"
_DfrapDiagUnitLocLoop_Object = MibScalar
dfrapDiagUnitLocLoop = _DfrapDiagUnitLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 1, 1),
    _DfrapDiagUnitLocLoop_Type()
)
dfrapDiagUnitLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagUnitLocLoop.setStatus("mandatory")


class _DfrapDiagUnitReset_Type(Integer32):
    """Custom type dfrapDiagUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-unit", 1)
    )


_DfrapDiagUnitReset_Type.__name__ = "Integer32"
_DfrapDiagUnitReset_Object = MibScalar
dfrapDiagUnitReset = _DfrapDiagUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 1, 2),
    _DfrapDiagUnitReset_Type()
)
dfrapDiagUnitReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapDiagUnitReset.setStatus("mandatory")
_DfrapDiagUnitTimeRemaining_Type = TimeTicks
_DfrapDiagUnitTimeRemaining_Object = MibScalar
dfrapDiagUnitTimeRemaining = _DfrapDiagUnitTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 1, 3),
    _DfrapDiagUnitTimeRemaining_Type()
)
dfrapDiagUnitTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagUnitTimeRemaining.setStatus("mandatory")
_DfrapDiagDdsTable_ObjectIdentity = ObjectIdentity
dfrapDiagDdsTable = _DfrapDiagDdsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 2)
)


class _DfrapDiagDdsLclLpbk_Type(Integer32):
    """Custom type dfrapDiagDdsLclLpbk based on Integer32"""
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


_DfrapDiagDdsLclLpbk_Type.__name__ = "Integer32"
_DfrapDiagDdsLclLpbk_Object = MibScalar
dfrapDiagDdsLclLpbk = _DfrapDiagDdsLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 2, 2),
    _DfrapDiagDdsLclLpbk_Type()
)
dfrapDiagDdsLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagDdsLclLpbk.setStatus("mandatory")


class _DfrapDiagDdsRmtLpbk_Type(Integer32):
    """Custom type dfrapDiagDdsRmtLpbk based on Integer32"""
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
        *(("latching-loopback", 4),
          ("no-loop-from-remote", 1),
          ("non-latching-loop", 3),
          ("simplex-current-loop", 2))
    )


_DfrapDiagDdsRmtLpbk_Type.__name__ = "Integer32"
_DfrapDiagDdsRmtLpbk_Object = MibScalar
dfrapDiagDdsRmtLpbk = _DfrapDiagDdsRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 2, 3),
    _DfrapDiagDdsRmtLpbk_Type()
)
dfrapDiagDdsRmtLpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagDdsRmtLpbk.setStatus("mandatory")
_DfrapDiagDdsTimeRemaining_Type = TimeTicks
_DfrapDiagDdsTimeRemaining_Object = MibScalar
dfrapDiagDdsTimeRemaining = _DfrapDiagDdsTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 2, 4),
    _DfrapDiagDdsTimeRemaining_Type()
)
dfrapDiagDdsTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagDdsTimeRemaining.setStatus("mandatory")
_DfrapDiagDteTable_ObjectIdentity = ObjectIdentity
dfrapDiagDteTable = _DfrapDiagDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 3)
)


class _DfrapDiagDteLclLpbk_Type(Integer32):
    """Custom type dfrapDiagDteLclLpbk based on Integer32"""
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


_DfrapDiagDteLclLpbk_Type.__name__ = "Integer32"
_DfrapDiagDteLclLpbk_Object = MibScalar
dfrapDiagDteLclLpbk = _DfrapDiagDteLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 3, 3),
    _DfrapDiagDteLclLpbk_Type()
)
dfrapDiagDteLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagDteLclLpbk.setStatus("mandatory")


class _DfrapDiagDteV54Lpbk_Type(Integer32):
    """Custom type dfrapDiagDteV54Lpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v54-not-received", 2),
          ("v54-received", 1))
    )


_DfrapDiagDteV54Lpbk_Type.__name__ = "Integer32"
_DfrapDiagDteV54Lpbk_Object = MibScalar
dfrapDiagDteV54Lpbk = _DfrapDiagDteV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 3, 4),
    _DfrapDiagDteV54Lpbk_Type()
)
dfrapDiagDteV54Lpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagDteV54Lpbk.setStatus("mandatory")


class _DfrapDiagDteRmtV54Lpbk_Type(Integer32):
    """Custom type dfrapDiagDteRmtV54Lpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("transmit-code-disable", 4),
          ("transmit-code-enable", 3))
    )


_DfrapDiagDteRmtV54Lpbk_Type.__name__ = "Integer32"
_DfrapDiagDteRmtV54Lpbk_Object = MibScalar
dfrapDiagDteRmtV54Lpbk = _DfrapDiagDteRmtV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 3, 5),
    _DfrapDiagDteRmtV54Lpbk_Type()
)
dfrapDiagDteRmtV54Lpbk.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapDiagDteRmtV54Lpbk.setStatus("mandatory")
_DfrapDiagDteTimeRemaining_Type = TimeTicks
_DfrapDiagDteTimeRemaining_Object = MibScalar
dfrapDiagDteTimeRemaining = _DfrapDiagDteTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 3, 13),
    _DfrapDiagDteTimeRemaining_Type()
)
dfrapDiagDteTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagDteTimeRemaining.setStatus("mandatory")
_DfrapDiagBertTable_ObjectIdentity = ObjectIdentity
dfrapDiagBertTable = _DfrapDiagBertTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5)
)


class _DfrapDiagBertState_Type(Integer32):
    """Custom type dfrapDiagBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear-error", 5),
          ("inject-error", 4),
          ("start-test", 1),
          ("stop-test", 3))
    )


_DfrapDiagBertState_Type.__name__ = "Integer32"
_DfrapDiagBertState_Object = MibScalar
dfrapDiagBertState = _DfrapDiagBertState_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 1),
    _DfrapDiagBertState_Type()
)
dfrapDiagBertState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapDiagBertState.setStatus("mandatory")


class _DfrapDiagBertStatus_Type(Integer32):
    """Custom type dfrapDiagBertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bert-in-sync", 3),
          ("bert-off", 1),
          ("bert-out-of-sync", 2))
    )


_DfrapDiagBertStatus_Type.__name__ = "Integer32"
_DfrapDiagBertStatus_Object = MibScalar
dfrapDiagBertStatus = _DfrapDiagBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 2),
    _DfrapDiagBertStatus_Type()
)
dfrapDiagBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagBertStatus.setStatus("mandatory")
_DfrapDiagBertErrors_Type = Counter32
_DfrapDiagBertErrors_Object = MibScalar
dfrapDiagBertErrors = _DfrapDiagBertErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 3),
    _DfrapDiagBertErrors_Type()
)
dfrapDiagBertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagBertErrors.setStatus("mandatory")
_DfrapDiagBertErrSec_Type = Counter32
_DfrapDiagBertErrSec_Object = MibScalar
dfrapDiagBertErrSec = _DfrapDiagBertErrSec_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 4),
    _DfrapDiagBertErrSec_Type()
)
dfrapDiagBertErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagBertErrSec.setStatus("mandatory")
_DfrapDiagBertTimeElaps_Type = TimeTicks
_DfrapDiagBertTimeElaps_Object = MibScalar
dfrapDiagBertTimeElaps = _DfrapDiagBertTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 5),
    _DfrapDiagBertTimeElaps_Type()
)
dfrapDiagBertTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagBertTimeElaps.setStatus("mandatory")
_DfrapDiagBertResyncs_Type = Counter32
_DfrapDiagBertResyncs_Object = MibScalar
dfrapDiagBertResyncs = _DfrapDiagBertResyncs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 6),
    _DfrapDiagBertResyncs_Type()
)
dfrapDiagBertResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagBertResyncs.setStatus("mandatory")


class _DfrapDiagBertPattern_Type(Integer32):
    """Custom type dfrapDiagBertPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("five11-pattern", 1),
          ("qrss", 2))
    )


_DfrapDiagBertPattern_Type.__name__ = "Integer32"
_DfrapDiagBertPattern_Object = MibScalar
dfrapDiagBertPattern = _DfrapDiagBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 5, 7),
    _DfrapDiagBertPattern_Type()
)
dfrapDiagBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagBertPattern.setStatus("mandatory")
_DfrapDiagVnipTable_Object = MibTable
dfrapDiagVnipTable = _DfrapDiagVnipTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6)
)
if mibBuilder.loadTexts:
    dfrapDiagVnipTable.setStatus("mandatory")
_DfrapDiagVnipEntry_Object = MibTableRow
dfrapDiagVnipEntry = _DfrapDiagVnipEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1)
)
dfrapDiagVnipEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapDiagVnipInterface"),
    (0, "DFRAP-MIB", "dfrapDiagVnipIndex"),
)
if mibBuilder.loadTexts:
    dfrapDiagVnipEntry.setStatus("mandatory")


class _DfrapDiagVnipInterface_Type(Integer32):
    """Custom type dfrapDiagVnipInterface based on Integer32"""
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


_DfrapDiagVnipInterface_Type.__name__ = "Integer32"
_DfrapDiagVnipInterface_Object = MibTableColumn
dfrapDiagVnipInterface = _DfrapDiagVnipInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 1),
    _DfrapDiagVnipInterface_Type()
)
dfrapDiagVnipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVnipInterface.setStatus("mandatory")
_DfrapDiagVnipIndex_Type = Integer32
_DfrapDiagVnipIndex_Object = MibTableColumn
dfrapDiagVnipIndex = _DfrapDiagVnipIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 2),
    _DfrapDiagVnipIndex_Type()
)
dfrapDiagVnipIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVnipIndex.setStatus("mandatory")
_DfrapDiagVnipDlci_Type = Integer32
_DfrapDiagVnipDlci_Object = MibTableColumn
dfrapDiagVnipDlci = _DfrapDiagVnipDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 3),
    _DfrapDiagVnipDlci_Type()
)
dfrapDiagVnipDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagVnipDlci.setStatus("mandatory")
_DfrapDiagVnipIpAddr_Type = IpAddress
_DfrapDiagVnipIpAddr_Object = MibTableColumn
dfrapDiagVnipIpAddr = _DfrapDiagVnipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 4),
    _DfrapDiagVnipIpAddr_Type()
)
dfrapDiagVnipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDiagVnipIpAddr.setStatus("mandatory")


class _DfrapDiagVLOOP_Type(Integer32):
    """Custom type dfrapDiagVLOOP based on Integer32"""
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


_DfrapDiagVLOOP_Type.__name__ = "Integer32"
_DfrapDiagVLOOP_Object = MibTableColumn
dfrapDiagVLOOP = _DfrapDiagVLOOP_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 5),
    _DfrapDiagVLOOP_Type()
)
dfrapDiagVLOOP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapDiagVLOOP.setStatus("mandatory")


class _DfrapDiagVBERT_Type(Integer32):
    """Custom type dfrapDiagVBERT based on Integer32"""
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


_DfrapDiagVBERT_Type.__name__ = "Integer32"
_DfrapDiagVBERT_Object = MibTableColumn
dfrapDiagVBERT = _DfrapDiagVBERT_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 6),
    _DfrapDiagVBERT_Type()
)
dfrapDiagVBERT.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapDiagVBERT.setStatus("mandatory")


class _DfrapDiagVBERTRate_Type(Integer32):
    """Custom type dfrapDiagVBERTRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 64000),
    )


_DfrapDiagVBERTRate_Type.__name__ = "Integer32"
_DfrapDiagVBERTRate_Object = MibTableColumn
dfrapDiagVBERTRate = _DfrapDiagVBERTRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 7),
    _DfrapDiagVBERTRate_Type()
)
dfrapDiagVBERTRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVBERTRate.setStatus("mandatory")


class _DfrapDiagVBERTSize_Type(Integer32):
    """Custom type dfrapDiagVBERTSize based on Integer32"""
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
        *(("five-hundred-twelve-byte", 512),
          ("one-twenty-eight-byte", 128),
          ("sixty-four-byte", 64),
          ("thousand-twenty-four-byte", 1024),
          ("two-fifty-six-byte", 256),
          ("two-thous-forty-eight-byte", 2048))
    )


_DfrapDiagVBERTSize_Type.__name__ = "Integer32"
_DfrapDiagVBERTSize_Object = MibTableColumn
dfrapDiagVBERTSize = _DfrapDiagVBERTSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 8),
    _DfrapDiagVBERTSize_Type()
)
dfrapDiagVBERTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVBERTSize.setStatus("mandatory")


class _DfrapDiagVBERTPktPercent_Type(Integer32):
    """Custom type dfrapDiagVBERTPktPercent based on Integer32"""
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
        *(("fifty-percent", 3),
          ("oneHundred-percent", 5),
          ("seventyFive-percent", 4),
          ("twentyFive-percent", 2),
          ("zero-percent", 1))
    )


_DfrapDiagVBERTPktPercent_Type.__name__ = "Integer32"
_DfrapDiagVBERTPktPercent_Object = MibTableColumn
dfrapDiagVBERTPktPercent = _DfrapDiagVBERTPktPercent_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 9),
    _DfrapDiagVBERTPktPercent_Type()
)
dfrapDiagVBERTPktPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVBERTPktPercent.setStatus("mandatory")


class _DfrapDiagVBERTTestPeriod_Type(Integer32):
    """Custom type dfrapDiagVBERTTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_DfrapDiagVBERTTestPeriod_Type.__name__ = "Integer32"
_DfrapDiagVBERTTestPeriod_Object = MibTableColumn
dfrapDiagVBERTTestPeriod = _DfrapDiagVBERTTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 3, 6, 1, 10),
    _DfrapDiagVBERTTestPeriod_Type()
)
dfrapDiagVBERTTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfrapDiagVBERTTestPeriod.setStatus("mandatory")
_DfrapStatus_ObjectIdentity = ObjectIdentity
dfrapStatus = _DfrapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 4)
)
_DfrapVnipTopologyTable_Object = MibTable
dfrapVnipTopologyTable = _DfrapVnipTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dfrapVnipTopologyTable.setStatus("mandatory")
_DfrapVnipTopologyEntry_Object = MibTableRow
dfrapVnipTopologyEntry = _DfrapVnipTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1)
)
dfrapVnipTopologyEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapVnipTopologyInterface"),
    (0, "DFRAP-MIB", "dfrapVnipTopologyIndex"),
)
if mibBuilder.loadTexts:
    dfrapVnipTopologyEntry.setStatus("mandatory")


class _DfrapVnipTopologyInterface_Type(Integer32):
    """Custom type dfrapVnipTopologyInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dds-interface", 2),
          ("dte-interface", 1))
    )


_DfrapVnipTopologyInterface_Type.__name__ = "Integer32"
_DfrapVnipTopologyInterface_Object = MibTableColumn
dfrapVnipTopologyInterface = _DfrapVnipTopologyInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 1),
    _DfrapVnipTopologyInterface_Type()
)
dfrapVnipTopologyInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyInterface.setStatus("mandatory")
_DfrapVnipTopologyIndex_Type = Integer32
_DfrapVnipTopologyIndex_Object = MibTableColumn
dfrapVnipTopologyIndex = _DfrapVnipTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 2),
    _DfrapVnipTopologyIndex_Type()
)
dfrapVnipTopologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyIndex.setStatus("mandatory")
_DfrapVnipTopologyDlci_Type = Integer32
_DfrapVnipTopologyDlci_Object = MibTableColumn
dfrapVnipTopologyDlci = _DfrapVnipTopologyDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 3),
    _DfrapVnipTopologyDlci_Type()
)
dfrapVnipTopologyDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyDlci.setStatus("mandatory")
_DfrapVnipTopologyIpAddr_Type = IpAddress
_DfrapVnipTopologyIpAddr_Object = MibTableColumn
dfrapVnipTopologyIpAddr = _DfrapVnipTopologyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 4),
    _DfrapVnipTopologyIpAddr_Type()
)
dfrapVnipTopologyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyIpAddr.setStatus("mandatory")
_DfrapVnipTopologyNumHops_Type = Integer32
_DfrapVnipTopologyNumHops_Object = MibTableColumn
dfrapVnipTopologyNumHops = _DfrapVnipTopologyNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 5),
    _DfrapVnipTopologyNumHops_Type()
)
dfrapVnipTopologyNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyNumHops.setStatus("mandatory")
_DfrapVnipTopologyLocalDlci_Type = Integer32
_DfrapVnipTopologyLocalDlci_Object = MibTableColumn
dfrapVnipTopologyLocalDlci = _DfrapVnipTopologyLocalDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 6),
    _DfrapVnipTopologyLocalDlci_Type()
)
dfrapVnipTopologyLocalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopologyLocalDlci.setStatus("mandatory")
_DfrapVnipTopoTDNumSamples_Type = Counter32
_DfrapVnipTopoTDNumSamples_Object = MibTableColumn
dfrapVnipTopoTDNumSamples = _DfrapVnipTopoTDNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 10),
    _DfrapVnipTopoTDNumSamples_Type()
)
dfrapVnipTopoTDNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoTDNumSamples.setStatus("mandatory")
_DfrapVnipTopoTDAvgDelay_Type = Counter32
_DfrapVnipTopoTDAvgDelay_Object = MibTableColumn
dfrapVnipTopoTDAvgDelay = _DfrapVnipTopoTDAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 11),
    _DfrapVnipTopoTDAvgDelay_Type()
)
dfrapVnipTopoTDAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoTDAvgDelay.setStatus("mandatory")
_DfrapVnipTopoTDMaxDelay_Type = Counter32
_DfrapVnipTopoTDMaxDelay_Object = MibTableColumn
dfrapVnipTopoTDMaxDelay = _DfrapVnipTopoTDMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 12),
    _DfrapVnipTopoTDMaxDelay_Type()
)
dfrapVnipTopoTDMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoTDMaxDelay.setStatus("mandatory")
_DfrapVnipTopoTDMinDelay_Type = Counter32
_DfrapVnipTopoTDMinDelay_Object = MibTableColumn
dfrapVnipTopoTDMinDelay = _DfrapVnipTopoTDMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 13),
    _DfrapVnipTopoTDMinDelay_Type()
)
dfrapVnipTopoTDMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoTDMinDelay.setStatus("mandatory")
_DfrapVnipTopoTDLastDelay_Type = Counter32
_DfrapVnipTopoTDLastDelay_Object = MibTableColumn
dfrapVnipTopoTDLastDelay = _DfrapVnipTopoTDLastDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 14),
    _DfrapVnipTopoTDLastDelay_Type()
)
dfrapVnipTopoTDLastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoTDLastDelay.setStatus("mandatory")


class _DfrapVnipTopoVLOOPStatus_Type(Integer32):
    """Custom type dfrapVnipTopoVLOOPStatus based on Integer32"""
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


_DfrapVnipTopoVLOOPStatus_Type.__name__ = "Integer32"
_DfrapVnipTopoVLOOPStatus_Object = MibTableColumn
dfrapVnipTopoVLOOPStatus = _DfrapVnipTopoVLOOPStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 15),
    _DfrapVnipTopoVLOOPStatus_Type()
)
dfrapVnipTopoVLOOPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVLOOPStatus.setStatus("mandatory")


class _DfrapVnipTopoVBERTStatus_Type(Integer32):
    """Custom type dfrapVnipTopoVBERTStatus based on Integer32"""
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


_DfrapVnipTopoVBERTStatus_Type.__name__ = "Integer32"
_DfrapVnipTopoVBERTStatus_Object = MibTableColumn
dfrapVnipTopoVBERTStatus = _DfrapVnipTopoVBERTStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 16),
    _DfrapVnipTopoVBERTStatus_Type()
)
dfrapVnipTopoVBERTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBERTStatus.setStatus("mandatory")
_DfrapVnipTopoVBertTxDESetFrames_Type = Counter32
_DfrapVnipTopoVBertTxDESetFrames_Object = MibTableColumn
dfrapVnipTopoVBertTxDESetFrames = _DfrapVnipTopoVBertTxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 17),
    _DfrapVnipTopoVBertTxDESetFrames_Type()
)
dfrapVnipTopoVBertTxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertTxDESetFrames.setStatus("mandatory")
_DfrapVnipTopoVBertRxDESetFrames_Type = Counter32
_DfrapVnipTopoVBertRxDESetFrames_Object = MibTableColumn
dfrapVnipTopoVBertRxDESetFrames = _DfrapVnipTopoVBertRxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 18),
    _DfrapVnipTopoVBertRxDESetFrames_Type()
)
dfrapVnipTopoVBertRxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertRxDESetFrames.setStatus("mandatory")
_DfrapVnipTopoVBertTxDEClrFrames_Type = Counter32
_DfrapVnipTopoVBertTxDEClrFrames_Object = MibTableColumn
dfrapVnipTopoVBertTxDEClrFrames = _DfrapVnipTopoVBertTxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 19),
    _DfrapVnipTopoVBertTxDEClrFrames_Type()
)
dfrapVnipTopoVBertTxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertTxDEClrFrames.setStatus("mandatory")
_DfrapVnipTopoVBertRxDEClrFrames_Type = Counter32
_DfrapVnipTopoVBertRxDEClrFrames_Object = MibTableColumn
dfrapVnipTopoVBertRxDEClrFrames = _DfrapVnipTopoVBertRxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 20),
    _DfrapVnipTopoVBertRxDEClrFrames_Type()
)
dfrapVnipTopoVBertRxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertRxDEClrFrames.setStatus("mandatory")
_DfrapVnipTopoVBertTransitDelayMax_Type = Counter32
_DfrapVnipTopoVBertTransitDelayMax_Object = MibTableColumn
dfrapVnipTopoVBertTransitDelayMax = _DfrapVnipTopoVBertTransitDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 21),
    _DfrapVnipTopoVBertTransitDelayMax_Type()
)
dfrapVnipTopoVBertTransitDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertTransitDelayMax.setStatus("mandatory")
_DfrapVnipTopoVBertTransitDelayAvg_Type = Counter32
_DfrapVnipTopoVBertTransitDelayAvg_Object = MibTableColumn
dfrapVnipTopoVBertTransitDelayAvg = _DfrapVnipTopoVBertTransitDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 22),
    _DfrapVnipTopoVBertTransitDelayAvg_Type()
)
dfrapVnipTopoVBertTransitDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertTransitDelayAvg.setStatus("mandatory")
_DfrapVnipTopoVBertTimeElapse_Type = TimeTicks
_DfrapVnipTopoVBertTimeElapse_Object = MibTableColumn
dfrapVnipTopoVBertTimeElapse = _DfrapVnipTopoVBertTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 23),
    _DfrapVnipTopoVBertTimeElapse_Type()
)
dfrapVnipTopoVBertTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertTimeElapse.setStatus("mandatory")
_DfrapVnipTopoVBertPerUtilCIR_Type = Integer32
_DfrapVnipTopoVBertPerUtilCIR_Object = MibTableColumn
dfrapVnipTopoVBertPerUtilCIR = _DfrapVnipTopoVBertPerUtilCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 24),
    _DfrapVnipTopoVBertPerUtilCIR_Type()
)
dfrapVnipTopoVBertPerUtilCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertPerUtilCIR.setStatus("mandatory")
_DfrapVnipTopoVBertPerUtilEIR_Type = Integer32
_DfrapVnipTopoVBertPerUtilEIR_Object = MibTableColumn
dfrapVnipTopoVBertPerUtilEIR = _DfrapVnipTopoVBertPerUtilEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 2, 1, 25),
    _DfrapVnipTopoVBertPerUtilEIR_Type()
)
dfrapVnipTopoVBertPerUtilEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapVnipTopoVBertPerUtilEIR.setStatus("mandatory")
_DfrapStatusMgmtTable_ObjectIdentity = ObjectIdentity
dfrapStatusMgmtTable = _DfrapStatusMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3)
)


class _DfrapStatusMgmtChannel_Type(Integer32):
    """Custom type dfrapStatusMgmtChannel based on Integer32"""
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


_DfrapStatusMgmtChannel_Type.__name__ = "Integer32"
_DfrapStatusMgmtChannel_Object = MibScalar
dfrapStatusMgmtChannel = _DfrapStatusMgmtChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3, 1),
    _DfrapStatusMgmtChannel_Type()
)
dfrapStatusMgmtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusMgmtChannel.setStatus("mandatory")


class _DfrapStatusMgmtInterface_Type(Integer32):
    """Custom type dfrapStatusMgmtInterface based on Integer32"""
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
          ("local-dte", 2),
          ("remote-wan", 3))
    )


_DfrapStatusMgmtInterface_Type.__name__ = "Integer32"
_DfrapStatusMgmtInterface_Object = MibScalar
dfrapStatusMgmtInterface = _DfrapStatusMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3, 2),
    _DfrapStatusMgmtInterface_Type()
)
dfrapStatusMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusMgmtInterface.setStatus("mandatory")


class _DfrapStatusMgmtInterfaceStatus_Type(Integer32):
    """Custom type dfrapStatusMgmtInterfaceStatus based on Integer32"""
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


_DfrapStatusMgmtInterfaceStatus_Type.__name__ = "Integer32"
_DfrapStatusMgmtInterfaceStatus_Object = MibScalar
dfrapStatusMgmtInterfaceStatus = _DfrapStatusMgmtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3, 3),
    _DfrapStatusMgmtInterfaceStatus_Type()
)
dfrapStatusMgmtInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusMgmtInterfaceStatus.setStatus("mandatory")
_DfrapStatusMgmtDefaultDLCINo_Type = Integer32
_DfrapStatusMgmtDefaultDLCINo_Object = MibScalar
dfrapStatusMgmtDefaultDLCINo = _DfrapStatusMgmtDefaultDLCINo_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3, 4),
    _DfrapStatusMgmtDefaultDLCINo_Type()
)
dfrapStatusMgmtDefaultDLCINo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusMgmtDefaultDLCINo.setStatus("mandatory")


class _DfrapStatusMgmtDefaultDLCIStatus_Type(Integer32):
    """Custom type dfrapStatusMgmtDefaultDLCIStatus based on Integer32"""
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


_DfrapStatusMgmtDefaultDLCIStatus_Type.__name__ = "Integer32"
_DfrapStatusMgmtDefaultDLCIStatus_Object = MibScalar
dfrapStatusMgmtDefaultDLCIStatus = _DfrapStatusMgmtDefaultDLCIStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 3, 5),
    _DfrapStatusMgmtDefaultDLCIStatus_Type()
)
dfrapStatusMgmtDefaultDLCIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusMgmtDefaultDLCIStatus.setStatus("mandatory")
_DfrapStatusLedTable_ObjectIdentity = ObjectIdentity
dfrapStatusLedTable = _DfrapStatusLedTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4)
)


class _DfrapStatusDteModeLED_Type(Integer32):
    """Custom type dfrapStatusDteModeLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-normal", 2),
          ("offLED-DTE-inactive", 1),
          ("yellowLED-test-mode", 3))
    )


_DfrapStatusDteModeLED_Type.__name__ = "Integer32"
_DfrapStatusDteModeLED_Object = MibScalar
dfrapStatusDteModeLED = _DfrapStatusDteModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 1),
    _DfrapStatusDteModeLED_Type()
)
dfrapStatusDteModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteModeLED.setStatus("mandatory")


class _DfrapStatusDteStatusLED_Type(Integer32):
    """Custom type dfrapStatusDteStatusLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("greenLED-active", 2)
    )


_DfrapStatusDteStatusLED_Type.__name__ = "Integer32"
_DfrapStatusDteStatusLED_Object = MibScalar
dfrapStatusDteStatusLED = _DfrapStatusDteStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 2),
    _DfrapStatusDteStatusLED_Type()
)
dfrapStatusDteStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteStatusLED.setStatus("mandatory")


class _DfrapStatusDteTxLED_Type(Integer32):
    """Custom type dfrapStatusDteTxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-tx-data-transmitting", 2),
          ("offLED-inactive", 1))
    )


_DfrapStatusDteTxLED_Type.__name__ = "Integer32"
_DfrapStatusDteTxLED_Object = MibScalar
dfrapStatusDteTxLED = _DfrapStatusDteTxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 3),
    _DfrapStatusDteTxLED_Type()
)
dfrapStatusDteTxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteTxLED.setStatus("mandatory")


class _DfrapStatusDteRxLED_Type(Integer32):
    """Custom type dfrapStatusDteRxLED based on Integer32"""
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


_DfrapStatusDteRxLED_Type.__name__ = "Integer32"
_DfrapStatusDteRxLED_Object = MibScalar
dfrapStatusDteRxLED = _DfrapStatusDteRxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 4),
    _DfrapStatusDteRxLED_Type()
)
dfrapStatusDteRxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteRxLED.setStatus("mandatory")


class _DfrapStatusDdsModeLED_Type(Integer32):
    """Custom type dfrapStatusDdsModeLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-normal", 2),
          ("yellowLED-test-mode", 3))
    )


_DfrapStatusDdsModeLED_Type.__name__ = "Integer32"
_DfrapStatusDdsModeLED_Object = MibScalar
dfrapStatusDdsModeLED = _DfrapStatusDdsModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 5),
    _DfrapStatusDdsModeLED_Type()
)
dfrapStatusDdsModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDdsModeLED.setStatus("mandatory")


class _DfrapStatusDdsStatusLED_Type(Integer32):
    """Custom type dfrapStatusDdsStatusLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-normal", 2),
          ("offLED-DDS-no-signal", 1),
          ("yellowLED-remote-alarm", 3))
    )


_DfrapStatusDdsStatusLED_Type.__name__ = "Integer32"
_DfrapStatusDdsStatusLED_Object = MibScalar
dfrapStatusDdsStatusLED = _DfrapStatusDdsStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 6),
    _DfrapStatusDdsStatusLED_Type()
)
dfrapStatusDdsStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDdsStatusLED.setStatus("mandatory")


class _DfrapStatusAllLEDs_Type(DisplayString):
    """Custom type dfrapStatusAllLEDs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DfrapStatusAllLEDs_Type.__name__ = "DisplayString"
_DfrapStatusAllLEDs_Object = MibScalar
dfrapStatusAllLEDs = _DfrapStatusAllLEDs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 4, 7),
    _DfrapStatusAllLEDs_Type()
)
dfrapStatusAllLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusAllLEDs.setStatus("mandatory")


class _DfrapVnipTransitDelayClear_Type(Integer32):
    """Custom type dfrapVnipTransitDelayClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-transit-delay", 1)
    )


_DfrapVnipTransitDelayClear_Type.__name__ = "Integer32"
_DfrapVnipTransitDelayClear_Object = MibScalar
dfrapVnipTransitDelayClear = _DfrapVnipTransitDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 5),
    _DfrapVnipTransitDelayClear_Type()
)
dfrapVnipTransitDelayClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapVnipTransitDelayClear.setStatus("mandatory")


class _DfrapLmiSourcing_Type(Integer32):
    """Custom type dfrapLmiSourcing based on Integer32"""
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
        *(("disabled", 7),
          ("initializing", 1),
          ("passthrough", 2),
          ("status-enqs-to-dds", 4),
          ("status-enqs-to-dte", 3),
          ("status-rspns-both", 8),
          ("status-rspns-to-dds", 6),
          ("status-rspns-to-dte", 5))
    )


_DfrapLmiSourcing_Type.__name__ = "Integer32"
_DfrapLmiSourcing_Object = MibScalar
dfrapLmiSourcing = _DfrapLmiSourcing_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 6),
    _DfrapLmiSourcing_Type()
)
dfrapLmiSourcing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapLmiSourcing.setStatus("mandatory")
_DfrapStatusDteTable_ObjectIdentity = ObjectIdentity
dfrapStatusDteTable = _DfrapStatusDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7)
)


class _DfrapStatusDteMode_Type(Integer32):
    """Custom type dfrapStatusDteMode based on Integer32"""
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


_DfrapStatusDteMode_Type.__name__ = "Integer32"
_DfrapStatusDteMode_Object = MibScalar
dfrapStatusDteMode = _DfrapStatusDteMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 1),
    _DfrapStatusDteMode_Type()
)
dfrapStatusDteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteMode.setStatus("mandatory")


class _DfrapStatusDteRts_Type(Integer32):
    """Custom type dfrapStatusDteRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DfrapStatusDteRts_Type.__name__ = "Integer32"
_DfrapStatusDteRts_Object = MibScalar
dfrapStatusDteRts = _DfrapStatusDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 2),
    _DfrapStatusDteRts_Type()
)
dfrapStatusDteRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteRts.setStatus("mandatory")


class _DfrapStatusDteDtr_Type(Integer32):
    """Custom type dfrapStatusDteDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DfrapStatusDteDtr_Type.__name__ = "Integer32"
_DfrapStatusDteDtr_Object = MibScalar
dfrapStatusDteDtr = _DfrapStatusDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 3),
    _DfrapStatusDteDtr_Type()
)
dfrapStatusDteDtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteDtr.setStatus("mandatory")


class _DfrapStatusDteDcd_Type(Integer32):
    """Custom type dfrapStatusDteDcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DfrapStatusDteDcd_Type.__name__ = "Integer32"
_DfrapStatusDteDcd_Object = MibScalar
dfrapStatusDteDcd = _DfrapStatusDteDcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 4),
    _DfrapStatusDteDcd_Type()
)
dfrapStatusDteDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteDcd.setStatus("mandatory")


class _DfrapStatusDteDsr_Type(Integer32):
    """Custom type dfrapStatusDteDsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DfrapStatusDteDsr_Type.__name__ = "Integer32"
_DfrapStatusDteDsr_Object = MibScalar
dfrapStatusDteDsr = _DfrapStatusDteDsr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 5),
    _DfrapStatusDteDsr_Type()
)
dfrapStatusDteDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteDsr.setStatus("mandatory")


class _DfrapStatusDteCts_Type(Integer32):
    """Custom type dfrapStatusDteCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DfrapStatusDteCts_Type.__name__ = "Integer32"
_DfrapStatusDteCts_Object = MibScalar
dfrapStatusDteCts = _DfrapStatusDteCts_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 7, 6),
    _DfrapStatusDteCts_Type()
)
dfrapStatusDteCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDteCts.setStatus("mandatory")
_DfrapStatusDdsTable_ObjectIdentity = ObjectIdentity
dfrapStatusDdsTable = _DfrapStatusDdsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 8)
)


class _DfrapStatusDdsLineStatus_Type(Integer32):
    """Custom type dfrapStatusDdsLineStatus based on Integer32"""
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
        *(("bpv-threshold-failure", 4),
          ("in-sync", 1),
          ("loss-of-signal", 5),
          ("out-of-frame", 3),
          ("out-of-service", 2),
          ("simplex-current-loopback", 6))
    )


_DfrapStatusDdsLineStatus_Type.__name__ = "Integer32"
_DfrapStatusDdsLineStatus_Object = MibScalar
dfrapStatusDdsLineStatus = _DfrapStatusDdsLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 8, 1),
    _DfrapStatusDdsLineStatus_Type()
)
dfrapStatusDdsLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDdsLineStatus.setStatus("mandatory")


class _DfrapStatusDdsLoopLength_Type(Integer32):
    """Custom type dfrapStatusDdsLoopLength based on Integer32"""
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
        *(("loss-0db", 9),
          ("loss-1-7db", 8),
          ("loss-15-20db", 6),
          ("loss-21-26db", 5),
          ("loss-27-32db", 4),
          ("loss-33-38db", 3),
          ("loss-39-44db", 2),
          ("loss-40-50db", 1),
          ("loss-8-14db", 7))
    )


_DfrapStatusDdsLoopLength_Type.__name__ = "Integer32"
_DfrapStatusDdsLoopLength_Object = MibScalar
dfrapStatusDdsLoopLength = _DfrapStatusDdsLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 8, 2),
    _DfrapStatusDdsLoopLength_Type()
)
dfrapStatusDdsLoopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusDdsLoopLength.setStatus("mandatory")


class _DfrapVBertClear_Type(Integer32):
    """Custom type dfrapVBertClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-vbert", 1)
    )


_DfrapVBertClear_Type.__name__ = "Integer32"
_DfrapVBertClear_Object = MibScalar
dfrapVBertClear = _DfrapVBertClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 11),
    _DfrapVBertClear_Type()
)
dfrapVBertClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapVBertClear.setStatus("mandatory")


class _DfrapStatusLmiAutosense_Type(Integer32):
    """Custom type dfrapStatusLmiAutosense based on Integer32"""
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


_DfrapStatusLmiAutosense_Type.__name__ = "Integer32"
_DfrapStatusLmiAutosense_Object = MibScalar
dfrapStatusLmiAutosense = _DfrapStatusLmiAutosense_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 4, 12),
    _DfrapStatusLmiAutosense_Type()
)
dfrapStatusLmiAutosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapStatusLmiAutosense.setStatus("mandatory")
_DfrapPerformance_ObjectIdentity = ObjectIdentity
dfrapPerformance = _DfrapPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5)
)
_DfrapPerfMgmtIp_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIp = _DfrapPerfMgmtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2)
)
_DfrapPerfMgmtIpIFStatsTable_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIpIFStatsTable = _DfrapPerfMgmtIpIFStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 1)
)
_DfrapPerfMgmtIpIFInOctets_Type = Counter32
_DfrapPerfMgmtIpIFInOctets_Object = MibScalar
dfrapPerfMgmtIpIFInOctets = _DfrapPerfMgmtIpIFInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 1, 1),
    _DfrapPerfMgmtIpIFInOctets_Type()
)
dfrapPerfMgmtIpIFInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIFInOctets.setStatus("mandatory")
_DfrapPerfMgmtIpIFInErrors_Type = Counter32
_DfrapPerfMgmtIpIFInErrors_Object = MibScalar
dfrapPerfMgmtIpIFInErrors = _DfrapPerfMgmtIpIFInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 1, 2),
    _DfrapPerfMgmtIpIFInErrors_Type()
)
dfrapPerfMgmtIpIFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIFInErrors.setStatus("mandatory")
_DfrapPerfMgmtIpIFOutOctets_Type = Counter32
_DfrapPerfMgmtIpIFOutOctets_Object = MibScalar
dfrapPerfMgmtIpIFOutOctets = _DfrapPerfMgmtIpIFOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 1, 3),
    _DfrapPerfMgmtIpIFOutOctets_Type()
)
dfrapPerfMgmtIpIFOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIFOutOctets.setStatus("mandatory")


class _DfrapPerfMgmtIpIFOperStatus_Type(Integer32):
    """Custom type dfrapPerfMgmtIpIFOperStatus based on Integer32"""
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


_DfrapPerfMgmtIpIFOperStatus_Type.__name__ = "Integer32"
_DfrapPerfMgmtIpIFOperStatus_Object = MibScalar
dfrapPerfMgmtIpIFOperStatus = _DfrapPerfMgmtIpIFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 1, 4),
    _DfrapPerfMgmtIpIFOperStatus_Type()
)
dfrapPerfMgmtIpIFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIFOperStatus.setStatus("mandatory")
_DfrapPerfMgmtIpIPStatsTable_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIpIPStatsTable = _DfrapPerfMgmtIpIPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2)
)
_DfrapPerfMgmtIpIPInRcv_Type = Counter32
_DfrapPerfMgmtIpIPInRcv_Object = MibScalar
dfrapPerfMgmtIpIPInRcv = _DfrapPerfMgmtIpIPInRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 1),
    _DfrapPerfMgmtIpIPInRcv_Type()
)
dfrapPerfMgmtIpIPInRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInRcv.setStatus("mandatory")
_DfrapPerfMgmtIpIPInHdrErr_Type = Counter32
_DfrapPerfMgmtIpIPInHdrErr_Object = MibScalar
dfrapPerfMgmtIpIPInHdrErr = _DfrapPerfMgmtIpIPInHdrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 2),
    _DfrapPerfMgmtIpIPInHdrErr_Type()
)
dfrapPerfMgmtIpIPInHdrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInHdrErr.setStatus("mandatory")
_DfrapPerfMgmtIpIPInAddrErr_Type = Counter32
_DfrapPerfMgmtIpIPInAddrErr_Object = MibScalar
dfrapPerfMgmtIpIPInAddrErr = _DfrapPerfMgmtIpIPInAddrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 3),
    _DfrapPerfMgmtIpIPInAddrErr_Type()
)
dfrapPerfMgmtIpIPInAddrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInAddrErr.setStatus("mandatory")
_DfrapPerfMgmtIpIPInProtUnk_Type = Counter32
_DfrapPerfMgmtIpIPInProtUnk_Object = MibScalar
dfrapPerfMgmtIpIPInProtUnk = _DfrapPerfMgmtIpIPInProtUnk_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 4),
    _DfrapPerfMgmtIpIPInProtUnk_Type()
)
dfrapPerfMgmtIpIPInProtUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInProtUnk.setStatus("mandatory")
_DfrapPerfMgmtIpIPInDscrd_Type = Counter32
_DfrapPerfMgmtIpIPInDscrd_Object = MibScalar
dfrapPerfMgmtIpIPInDscrd = _DfrapPerfMgmtIpIPInDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 5),
    _DfrapPerfMgmtIpIPInDscrd_Type()
)
dfrapPerfMgmtIpIPInDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInDscrd.setStatus("mandatory")
_DfrapPerfMgmtIpIPInDlvrs_Type = Counter32
_DfrapPerfMgmtIpIPInDlvrs_Object = MibScalar
dfrapPerfMgmtIpIPInDlvrs = _DfrapPerfMgmtIpIPInDlvrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 6),
    _DfrapPerfMgmtIpIPInDlvrs_Type()
)
dfrapPerfMgmtIpIPInDlvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPInDlvrs.setStatus("mandatory")
_DfrapPerfMgmtIpIPOutRqst_Type = Counter32
_DfrapPerfMgmtIpIPOutRqst_Object = MibScalar
dfrapPerfMgmtIpIPOutRqst = _DfrapPerfMgmtIpIPOutRqst_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 7),
    _DfrapPerfMgmtIpIPOutRqst_Type()
)
dfrapPerfMgmtIpIPOutRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPOutRqst.setStatus("mandatory")
_DfrapPerfMgmtIpIPOutDscrd_Type = Counter32
_DfrapPerfMgmtIpIPOutDscrd_Object = MibScalar
dfrapPerfMgmtIpIPOutDscrd = _DfrapPerfMgmtIpIPOutDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 8),
    _DfrapPerfMgmtIpIPOutDscrd_Type()
)
dfrapPerfMgmtIpIPOutDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPOutDscrd.setStatus("mandatory")
_DfrapPerfMgmtIpIPOutNoRt_Type = Counter32
_DfrapPerfMgmtIpIPOutNoRt_Object = MibScalar
dfrapPerfMgmtIpIPOutNoRt = _DfrapPerfMgmtIpIPOutNoRt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 2, 9),
    _DfrapPerfMgmtIpIPOutNoRt_Type()
)
dfrapPerfMgmtIpIPOutNoRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpIPOutNoRt.setStatus("mandatory")
_DfrapPerfMgmtIpICMPStatsTable_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIpICMPStatsTable = _DfrapPerfMgmtIpICMPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3)
)
_DfrapPerfMgmtIpICMPInMsgs_Type = Counter32
_DfrapPerfMgmtIpICMPInMsgs_Object = MibScalar
dfrapPerfMgmtIpICMPInMsgs = _DfrapPerfMgmtIpICMPInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 1),
    _DfrapPerfMgmtIpICMPInMsgs_Type()
)
dfrapPerfMgmtIpICMPInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInMsgs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInErrors_Type = Counter32
_DfrapPerfMgmtIpICMPInErrors_Object = MibScalar
dfrapPerfMgmtIpICMPInErrors = _DfrapPerfMgmtIpICMPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 2),
    _DfrapPerfMgmtIpICMPInErrors_Type()
)
dfrapPerfMgmtIpICMPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInErrors.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInDestUnreachs_Type = Counter32
_DfrapPerfMgmtIpICMPInDestUnreachs_Object = MibScalar
dfrapPerfMgmtIpICMPInDestUnreachs = _DfrapPerfMgmtIpICMPInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 3),
    _DfrapPerfMgmtIpICMPInDestUnreachs_Type()
)
dfrapPerfMgmtIpICMPInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInDestUnreachs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInTimeExcds_Type = Counter32
_DfrapPerfMgmtIpICMPInTimeExcds_Object = MibScalar
dfrapPerfMgmtIpICMPInTimeExcds = _DfrapPerfMgmtIpICMPInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 4),
    _DfrapPerfMgmtIpICMPInTimeExcds_Type()
)
dfrapPerfMgmtIpICMPInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInTimeExcds.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInParmProbs_Type = Counter32
_DfrapPerfMgmtIpICMPInParmProbs_Object = MibScalar
dfrapPerfMgmtIpICMPInParmProbs = _DfrapPerfMgmtIpICMPInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 5),
    _DfrapPerfMgmtIpICMPInParmProbs_Type()
)
dfrapPerfMgmtIpICMPInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInParmProbs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInRedirects_Type = Counter32
_DfrapPerfMgmtIpICMPInRedirects_Object = MibScalar
dfrapPerfMgmtIpICMPInRedirects = _DfrapPerfMgmtIpICMPInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 6),
    _DfrapPerfMgmtIpICMPInRedirects_Type()
)
dfrapPerfMgmtIpICMPInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInRedirects.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInEchos_Type = Counter32
_DfrapPerfMgmtIpICMPInEchos_Object = MibScalar
dfrapPerfMgmtIpICMPInEchos = _DfrapPerfMgmtIpICMPInEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 7),
    _DfrapPerfMgmtIpICMPInEchos_Type()
)
dfrapPerfMgmtIpICMPInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInEchos.setStatus("mandatory")
_DfrapPerfMgmtIpICMPInEchoReps_Type = Counter32
_DfrapPerfMgmtIpICMPInEchoReps_Object = MibScalar
dfrapPerfMgmtIpICMPInEchoReps = _DfrapPerfMgmtIpICMPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 8),
    _DfrapPerfMgmtIpICMPInEchoReps_Type()
)
dfrapPerfMgmtIpICMPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPInEchoReps.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutMsgs_Type = Counter32
_DfrapPerfMgmtIpICMPOutMsgs_Object = MibScalar
dfrapPerfMgmtIpICMPOutMsgs = _DfrapPerfMgmtIpICMPOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 9),
    _DfrapPerfMgmtIpICMPOutMsgs_Type()
)
dfrapPerfMgmtIpICMPOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutMsgs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutErrors_Type = Counter32
_DfrapPerfMgmtIpICMPOutErrors_Object = MibScalar
dfrapPerfMgmtIpICMPOutErrors = _DfrapPerfMgmtIpICMPOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 10),
    _DfrapPerfMgmtIpICMPOutErrors_Type()
)
dfrapPerfMgmtIpICMPOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutErrors.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutDestUnreachs_Type = Counter32
_DfrapPerfMgmtIpICMPOutDestUnreachs_Object = MibScalar
dfrapPerfMgmtIpICMPOutDestUnreachs = _DfrapPerfMgmtIpICMPOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 11),
    _DfrapPerfMgmtIpICMPOutDestUnreachs_Type()
)
dfrapPerfMgmtIpICMPOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutDestUnreachs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutParmProbs_Type = Counter32
_DfrapPerfMgmtIpICMPOutParmProbs_Object = MibScalar
dfrapPerfMgmtIpICMPOutParmProbs = _DfrapPerfMgmtIpICMPOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 12),
    _DfrapPerfMgmtIpICMPOutParmProbs_Type()
)
dfrapPerfMgmtIpICMPOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutParmProbs.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutRedirects_Type = Counter32
_DfrapPerfMgmtIpICMPOutRedirects_Object = MibScalar
dfrapPerfMgmtIpICMPOutRedirects = _DfrapPerfMgmtIpICMPOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 13),
    _DfrapPerfMgmtIpICMPOutRedirects_Type()
)
dfrapPerfMgmtIpICMPOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutRedirects.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutEchos_Type = Counter32
_DfrapPerfMgmtIpICMPOutEchos_Object = MibScalar
dfrapPerfMgmtIpICMPOutEchos = _DfrapPerfMgmtIpICMPOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 14),
    _DfrapPerfMgmtIpICMPOutEchos_Type()
)
dfrapPerfMgmtIpICMPOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutEchos.setStatus("mandatory")
_DfrapPerfMgmtIpICMPOutEchoReps_Type = Counter32
_DfrapPerfMgmtIpICMPOutEchoReps_Object = MibScalar
dfrapPerfMgmtIpICMPOutEchoReps = _DfrapPerfMgmtIpICMPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 3, 15),
    _DfrapPerfMgmtIpICMPOutEchoReps_Type()
)
dfrapPerfMgmtIpICMPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpICMPOutEchoReps.setStatus("mandatory")
_DfrapPerfMgmtIpUDPStatsTable_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIpUDPStatsTable = _DfrapPerfMgmtIpUDPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 4)
)
_DfrapPerfMgmtIpUDPInDatagrams_Type = Counter32
_DfrapPerfMgmtIpUDPInDatagrams_Object = MibScalar
dfrapPerfMgmtIpUDPInDatagrams = _DfrapPerfMgmtIpUDPInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 4, 1),
    _DfrapPerfMgmtIpUDPInDatagrams_Type()
)
dfrapPerfMgmtIpUDPInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpUDPInDatagrams.setStatus("mandatory")
_DfrapPerfMgmtIpUDPOutDatagrams_Type = Counter32
_DfrapPerfMgmtIpUDPOutDatagrams_Object = MibScalar
dfrapPerfMgmtIpUDPOutDatagrams = _DfrapPerfMgmtIpUDPOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 4, 2),
    _DfrapPerfMgmtIpUDPOutDatagrams_Type()
)
dfrapPerfMgmtIpUDPOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpUDPOutDatagrams.setStatus("mandatory")
_DfrapPerfMgmtIpUDPNoPorts_Type = Counter32
_DfrapPerfMgmtIpUDPNoPorts_Object = MibScalar
dfrapPerfMgmtIpUDPNoPorts = _DfrapPerfMgmtIpUDPNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 4, 3),
    _DfrapPerfMgmtIpUDPNoPorts_Type()
)
dfrapPerfMgmtIpUDPNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpUDPNoPorts.setStatus("mandatory")
_DfrapPerfMgmtIpTCPStatsTable_ObjectIdentity = ObjectIdentity
dfrapPerfMgmtIpTCPStatsTable = _DfrapPerfMgmtIpTCPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5)
)
_DfrapPerfMgmtIpTCPActiveOpens_Type = Counter32
_DfrapPerfMgmtIpTCPActiveOpens_Object = MibScalar
dfrapPerfMgmtIpTCPActiveOpens = _DfrapPerfMgmtIpTCPActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 1),
    _DfrapPerfMgmtIpTCPActiveOpens_Type()
)
dfrapPerfMgmtIpTCPActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPActiveOpens.setStatus("mandatory")
_DfrapPerfMgmtIpTCPPassiveOpens_Type = Counter32
_DfrapPerfMgmtIpTCPPassiveOpens_Object = MibScalar
dfrapPerfMgmtIpTCPPassiveOpens = _DfrapPerfMgmtIpTCPPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 2),
    _DfrapPerfMgmtIpTCPPassiveOpens_Type()
)
dfrapPerfMgmtIpTCPPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPPassiveOpens.setStatus("mandatory")
_DfrapPerfMgmtIpTCPAttemptFails_Type = Counter32
_DfrapPerfMgmtIpTCPAttemptFails_Object = MibScalar
dfrapPerfMgmtIpTCPAttemptFails = _DfrapPerfMgmtIpTCPAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 3),
    _DfrapPerfMgmtIpTCPAttemptFails_Type()
)
dfrapPerfMgmtIpTCPAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPAttemptFails.setStatus("mandatory")
_DfrapPerfMgmtIpTCPCurrEstab_Type = Gauge32
_DfrapPerfMgmtIpTCPCurrEstab_Object = MibScalar
dfrapPerfMgmtIpTCPCurrEstab = _DfrapPerfMgmtIpTCPCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 4),
    _DfrapPerfMgmtIpTCPCurrEstab_Type()
)
dfrapPerfMgmtIpTCPCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPCurrEstab.setStatus("mandatory")
_DfrapPerfMgmtIpTCPInSegs_Type = Counter32
_DfrapPerfMgmtIpTCPInSegs_Object = MibScalar
dfrapPerfMgmtIpTCPInSegs = _DfrapPerfMgmtIpTCPInSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 5),
    _DfrapPerfMgmtIpTCPInSegs_Type()
)
dfrapPerfMgmtIpTCPInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPInSegs.setStatus("mandatory")
_DfrapPerfMgmtIpTCPOutSegs_Type = Counter32
_DfrapPerfMgmtIpTCPOutSegs_Object = MibScalar
dfrapPerfMgmtIpTCPOutSegs = _DfrapPerfMgmtIpTCPOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 2, 5, 6),
    _DfrapPerfMgmtIpTCPOutSegs_Type()
)
dfrapPerfMgmtIpTCPOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfMgmtIpTCPOutSegs.setStatus("mandatory")
_DfrapPerfThruput_ObjectIdentity = ObjectIdentity
dfrapPerfThruput = _DfrapPerfThruput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3)
)
_DfrapPerfThruputPerIntfTable_Object = MibTable
dfrapPerfThruputPerIntfTable = _DfrapPerfThruputPerIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1)
)
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfTable.setStatus("mandatory")
_DfrapPerfThruputPerIntfEntry_Object = MibTableRow
dfrapPerfThruputPerIntfEntry = _DfrapPerfThruputPerIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1)
)
dfrapPerfThruputPerIntfEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfThruputPerIntfIndex"),
)
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfEntry.setStatus("mandatory")


class _DfrapPerfThruputPerIntfIndex_Type(Integer32):
    """Custom type dfrapPerfThruputPerIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dds", 2),
          ("dte", 1))
    )


_DfrapPerfThruputPerIntfIndex_Type.__name__ = "Integer32"
_DfrapPerfThruputPerIntfIndex_Object = MibTableColumn
dfrapPerfThruputPerIntfIndex = _DfrapPerfThruputPerIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 1),
    _DfrapPerfThruputPerIntfIndex_Type()
)
dfrapPerfThruputPerIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfIndex.setStatus("mandatory")
_DfrapPerfThruputPerIntfRxByteCnt_Type = Counter32
_DfrapPerfThruputPerIntfRxByteCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfRxByteCnt = _DfrapPerfThruputPerIntfRxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 2),
    _DfrapPerfThruputPerIntfRxByteCnt_Type()
)
dfrapPerfThruputPerIntfRxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfRxByteCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfTxByteCnt_Type = Counter32
_DfrapPerfThruputPerIntfTxByteCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfTxByteCnt = _DfrapPerfThruputPerIntfTxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 3),
    _DfrapPerfThruputPerIntfTxByteCnt_Type()
)
dfrapPerfThruputPerIntfTxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfTxByteCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfRxFrameCnt_Type = Counter32
_DfrapPerfThruputPerIntfRxFrameCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfRxFrameCnt = _DfrapPerfThruputPerIntfRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 4),
    _DfrapPerfThruputPerIntfRxFrameCnt_Type()
)
dfrapPerfThruputPerIntfRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfRxFrameCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfTxFrameCnt_Type = Counter32
_DfrapPerfThruputPerIntfTxFrameCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfTxFrameCnt = _DfrapPerfThruputPerIntfTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 5),
    _DfrapPerfThruputPerIntfTxFrameCnt_Type()
)
dfrapPerfThruputPerIntfTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfTxFrameCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfRxCrcErrCnt_Type = Counter32
_DfrapPerfThruputPerIntfRxCrcErrCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfRxCrcErrCnt = _DfrapPerfThruputPerIntfRxCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 6),
    _DfrapPerfThruputPerIntfRxCrcErrCnt_Type()
)
dfrapPerfThruputPerIntfRxCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfRxCrcErrCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfRxAbortCnt_Type = Counter32
_DfrapPerfThruputPerIntfRxAbortCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfRxAbortCnt = _DfrapPerfThruputPerIntfRxAbortCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 7),
    _DfrapPerfThruputPerIntfRxAbortCnt_Type()
)
dfrapPerfThruputPerIntfRxAbortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfRxAbortCnt.setStatus("mandatory")
_DfrapPerfThruputPerIntfRxBpvCnt_Type = Counter32
_DfrapPerfThruputPerIntfRxBpvCnt_Object = MibTableColumn
dfrapPerfThruputPerIntfRxBpvCnt = _DfrapPerfThruputPerIntfRxBpvCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 1, 1, 8),
    _DfrapPerfThruputPerIntfRxBpvCnt_Type()
)
dfrapPerfThruputPerIntfRxBpvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerIntfRxBpvCnt.setStatus("mandatory")
_DfrapPerfThruputPerDlciTable_Object = MibTable
dfrapPerfThruputPerDlciTable = _DfrapPerfThruputPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTable.setStatus("mandatory")
_DfrapPerfThruputPerDlciEntry_Object = MibTableRow
dfrapPerfThruputPerDlciEntry = _DfrapPerfThruputPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1)
)
dfrapPerfThruputPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfThruputPerDlciIndex"),
    (0, "DFRAP-MIB", "dfrapPerfThruputPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciEntry.setStatus("mandatory")
_DfrapPerfThruputPerDlciIndex_Type = Index
_DfrapPerfThruputPerDlciIndex_Object = MibTableColumn
dfrapPerfThruputPerDlciIndex = _DfrapPerfThruputPerDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 1),
    _DfrapPerfThruputPerDlciIndex_Type()
)
dfrapPerfThruputPerDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciIndex.setStatus("mandatory")
_DfrapPerfThruputPerDlciValue_Type = Integer32
_DfrapPerfThruputPerDlciValue_Object = MibTableColumn
dfrapPerfThruputPerDlciValue = _DfrapPerfThruputPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 2),
    _DfrapPerfThruputPerDlciValue_Type()
)
dfrapPerfThruputPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciValue.setStatus("mandatory")
_DfrapPerfThruputPerDlciCreateTime_Type = Integer32
_DfrapPerfThruputPerDlciCreateTime_Object = MibTableColumn
dfrapPerfThruputPerDlciCreateTime = _DfrapPerfThruputPerDlciCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 3),
    _DfrapPerfThruputPerDlciCreateTime_Type()
)
dfrapPerfThruputPerDlciCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciCreateTime.setStatus("mandatory")
_DfrapPerfThruputPerDlciChangeTime_Type = Integer32
_DfrapPerfThruputPerDlciChangeTime_Object = MibTableColumn
dfrapPerfThruputPerDlciChangeTime = _DfrapPerfThruputPerDlciChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 4),
    _DfrapPerfThruputPerDlciChangeTime_Type()
)
dfrapPerfThruputPerDlciChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciChangeTime.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxByte_Type = Counter32
_DfrapPerfThruputPerDlciRxByte_Object = MibTableColumn
dfrapPerfThruputPerDlciRxByte = _DfrapPerfThruputPerDlciRxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 5),
    _DfrapPerfThruputPerDlciRxByte_Type()
)
dfrapPerfThruputPerDlciRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxByte.setStatus("mandatory")
_DfrapPerfThruputPerDlciTxByte_Type = Counter32
_DfrapPerfThruputPerDlciTxByte_Object = MibTableColumn
dfrapPerfThruputPerDlciTxByte = _DfrapPerfThruputPerDlciTxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 6),
    _DfrapPerfThruputPerDlciTxByte_Type()
)
dfrapPerfThruputPerDlciTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTxByte.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxFrame_Type = Counter32
_DfrapPerfThruputPerDlciRxFrame_Object = MibTableColumn
dfrapPerfThruputPerDlciRxFrame = _DfrapPerfThruputPerDlciRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 7),
    _DfrapPerfThruputPerDlciRxFrame_Type()
)
dfrapPerfThruputPerDlciRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxFrame.setStatus("mandatory")
_DfrapPerfThruputPerDlciTxFrame_Type = Counter32
_DfrapPerfThruputPerDlciTxFrame_Object = MibTableColumn
dfrapPerfThruputPerDlciTxFrame = _DfrapPerfThruputPerDlciTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 8),
    _DfrapPerfThruputPerDlciTxFrame_Type()
)
dfrapPerfThruputPerDlciTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTxFrame.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxFecn_Type = Counter32
_DfrapPerfThruputPerDlciRxFecn_Object = MibTableColumn
dfrapPerfThruputPerDlciRxFecn = _DfrapPerfThruputPerDlciRxFecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 9),
    _DfrapPerfThruputPerDlciRxFecn_Type()
)
dfrapPerfThruputPerDlciRxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxFecn.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxBecn_Type = Counter32
_DfrapPerfThruputPerDlciRxBecn_Object = MibTableColumn
dfrapPerfThruputPerDlciRxBecn = _DfrapPerfThruputPerDlciRxBecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 10),
    _DfrapPerfThruputPerDlciRxBecn_Type()
)
dfrapPerfThruputPerDlciRxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxBecn.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxDe_Type = Counter32
_DfrapPerfThruputPerDlciRxDe_Object = MibTableColumn
dfrapPerfThruputPerDlciRxDe = _DfrapPerfThruputPerDlciRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 11),
    _DfrapPerfThruputPerDlciRxDe_Type()
)
dfrapPerfThruputPerDlciRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxDe.setStatus("mandatory")
_DfrapPerfThruputPerDlciTxDe_Type = Counter32
_DfrapPerfThruputPerDlciTxDe_Object = MibTableColumn
dfrapPerfThruputPerDlciTxDe = _DfrapPerfThruputPerDlciTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 12),
    _DfrapPerfThruputPerDlciTxDe_Type()
)
dfrapPerfThruputPerDlciTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTxDe.setStatus("mandatory")
_DfrapPerfThruputPerDlciRxThruput_Type = Integer32
_DfrapPerfThruputPerDlciRxThruput_Object = MibTableColumn
dfrapPerfThruputPerDlciRxThruput = _DfrapPerfThruputPerDlciRxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 13),
    _DfrapPerfThruputPerDlciRxThruput_Type()
)
dfrapPerfThruputPerDlciRxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxThruput.setStatus("mandatory")
_DfrapPerfThruputPerDlciTxThruput_Type = Integer32
_DfrapPerfThruputPerDlciTxThruput_Object = MibTableColumn
dfrapPerfThruputPerDlciTxThruput = _DfrapPerfThruputPerDlciTxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 14),
    _DfrapPerfThruputPerDlciTxThruput_Type()
)
dfrapPerfThruputPerDlciTxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTxThruput.setStatus("mandatory")
_DfrapPerfThruputPerDlciCIR_Type = Integer32
_DfrapPerfThruputPerDlciCIR_Object = MibTableColumn
dfrapPerfThruputPerDlciCIR = _DfrapPerfThruputPerDlciCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 15),
    _DfrapPerfThruputPerDlciCIR_Type()
)
dfrapPerfThruputPerDlciCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciCIR.setStatus("mandatory")
_DfrapPerfThruputPerDlciUptime_Type = Integer32
_DfrapPerfThruputPerDlciUptime_Object = MibTableColumn
dfrapPerfThruputPerDlciUptime = _DfrapPerfThruputPerDlciUptime_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 16),
    _DfrapPerfThruputPerDlciUptime_Type()
)
dfrapPerfThruputPerDlciUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciUptime.setStatus("mandatory")
_DfrapPerfThruputPerDlciDowntime_Type = Integer32
_DfrapPerfThruputPerDlciDowntime_Object = MibTableColumn
dfrapPerfThruputPerDlciDowntime = _DfrapPerfThruputPerDlciDowntime_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 17),
    _DfrapPerfThruputPerDlciDowntime_Type()
)
dfrapPerfThruputPerDlciDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciDowntime.setStatus("mandatory")


class _DfrapPerfThruputPerDlciCirType_Type(Integer32):
    """Custom type dfrapPerfThruputPerDlciCirType based on Integer32"""
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


_DfrapPerfThruputPerDlciCirType_Type.__name__ = "Integer32"
_DfrapPerfThruputPerDlciCirType_Object = MibTableColumn
dfrapPerfThruputPerDlciCirType = _DfrapPerfThruputPerDlciCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 18),
    _DfrapPerfThruputPerDlciCirType_Type()
)
dfrapPerfThruputPerDlciCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciCirType.setStatus("mandatory")


class _DfrapPerfThruputPerDlciPvcState_Type(Integer32):
    """Custom type dfrapPerfThruputPerDlciPvcState based on Integer32"""
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


_DfrapPerfThruputPerDlciPvcState_Type.__name__ = "Integer32"
_DfrapPerfThruputPerDlciPvcState_Object = MibTableColumn
dfrapPerfThruputPerDlciPvcState = _DfrapPerfThruputPerDlciPvcState_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 19),
    _DfrapPerfThruputPerDlciPvcState_Type()
)
dfrapPerfThruputPerDlciPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciPvcState.setStatus("mandatory")
_DfrapPerfThruputPerDlciOutageCount_Type = Counter32
_DfrapPerfThruputPerDlciOutageCount_Object = MibTableColumn
dfrapPerfThruputPerDlciOutageCount = _DfrapPerfThruputPerDlciOutageCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 20),
    _DfrapPerfThruputPerDlciOutageCount_Type()
)
dfrapPerfThruputPerDlciOutageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciOutageCount.setStatus("mandatory")
_DfrapPerfThruputPerDlciAvailability_Type = Integer32
_DfrapPerfThruputPerDlciAvailability_Object = MibTableColumn
dfrapPerfThruputPerDlciAvailability = _DfrapPerfThruputPerDlciAvailability_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 21),
    _DfrapPerfThruputPerDlciAvailability_Type()
)
dfrapPerfThruputPerDlciAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciAvailability.setStatus("mandatory")
_DfrapPerfThruputPerDlciMTBSO_Type = Integer32
_DfrapPerfThruputPerDlciMTBSO_Object = MibTableColumn
dfrapPerfThruputPerDlciMTBSO = _DfrapPerfThruputPerDlciMTBSO_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 22),
    _DfrapPerfThruputPerDlciMTBSO_Type()
)
dfrapPerfThruputPerDlciMTBSO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciMTBSO.setStatus("mandatory")
_DfrapPerfThruputPerDlciMTTSR_Type = Integer32
_DfrapPerfThruputPerDlciMTTSR_Object = MibTableColumn
dfrapPerfThruputPerDlciMTTSR = _DfrapPerfThruputPerDlciMTTSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 23),
    _DfrapPerfThruputPerDlciMTTSR_Type()
)
dfrapPerfThruputPerDlciMTTSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciMTTSR.setStatus("mandatory")


class _DfrapPerfThruputPerDlciEncapType_Type(Integer32):
    """Custom type dfrapPerfThruputPerDlciEncapType based on Integer32"""
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


_DfrapPerfThruputPerDlciEncapType_Type.__name__ = "Integer32"
_DfrapPerfThruputPerDlciEncapType_Object = MibTableColumn
dfrapPerfThruputPerDlciEncapType = _DfrapPerfThruputPerDlciEncapType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 24),
    _DfrapPerfThruputPerDlciEncapType_Type()
)
dfrapPerfThruputPerDlciEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciEncapType.setStatus("mandatory")


class _DfrapPerfThruputPerDlciRxUtilizationStatus_Type(Integer32):
    """Custom type dfrapPerfThruputPerDlciRxUtilizationStatus based on Integer32"""
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


_DfrapPerfThruputPerDlciRxUtilizationStatus_Type.__name__ = "Integer32"
_DfrapPerfThruputPerDlciRxUtilizationStatus_Object = MibTableColumn
dfrapPerfThruputPerDlciRxUtilizationStatus = _DfrapPerfThruputPerDlciRxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 25),
    _DfrapPerfThruputPerDlciRxUtilizationStatus_Type()
)
dfrapPerfThruputPerDlciRxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciRxUtilizationStatus.setStatus("mandatory")


class _DfrapPerfThruputPerDlciTxUtilizationStatus_Type(Integer32):
    """Custom type dfrapPerfThruputPerDlciTxUtilizationStatus based on Integer32"""
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


_DfrapPerfThruputPerDlciTxUtilizationStatus_Type.__name__ = "Integer32"
_DfrapPerfThruputPerDlciTxUtilizationStatus_Object = MibTableColumn
dfrapPerfThruputPerDlciTxUtilizationStatus = _DfrapPerfThruputPerDlciTxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 26),
    _DfrapPerfThruputPerDlciTxUtilizationStatus_Type()
)
dfrapPerfThruputPerDlciTxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciTxUtilizationStatus.setStatus("mandatory")
_DfrapPerfThruputPerDlciEIR_Type = Integer32
_DfrapPerfThruputPerDlciEIR_Object = MibTableColumn
dfrapPerfThruputPerDlciEIR = _DfrapPerfThruputPerDlciEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 2, 1, 27),
    _DfrapPerfThruputPerDlciEIR_Type()
)
dfrapPerfThruputPerDlciEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputPerDlciEIR.setStatus("mandatory")
_DfrapPerfThruputCommands_ObjectIdentity = ObjectIdentity
dfrapPerfThruputCommands = _DfrapPerfThruputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3)
)


class _DfrapPerfThruputCmdClearDteStats_Type(Integer32):
    """Custom type dfrapPerfThruputCmdClearDteStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfThruputCmdClearDteStats_Type.__name__ = "Integer32"
_DfrapPerfThruputCmdClearDteStats_Object = MibScalar
dfrapPerfThruputCmdClearDteStats = _DfrapPerfThruputCmdClearDteStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 1),
    _DfrapPerfThruputCmdClearDteStats_Type()
)
dfrapPerfThruputCmdClearDteStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdClearDteStats.setStatus("mandatory")


class _DfrapPerfThruputCmdClearDdsStats_Type(Integer32):
    """Custom type dfrapPerfThruputCmdClearDdsStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfThruputCmdClearDdsStats_Type.__name__ = "Integer32"
_DfrapPerfThruputCmdClearDdsStats_Object = MibScalar
dfrapPerfThruputCmdClearDdsStats = _DfrapPerfThruputCmdClearDdsStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 2),
    _DfrapPerfThruputCmdClearDdsStats_Type()
)
dfrapPerfThruputCmdClearDdsStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdClearDdsStats.setStatus("mandatory")


class _DfrapPerfThruputCmdClearAllIntfStats_Type(Integer32):
    """Custom type dfrapPerfThruputCmdClearAllIntfStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfThruputCmdClearAllIntfStats_Type.__name__ = "Integer32"
_DfrapPerfThruputCmdClearAllIntfStats_Object = MibScalar
dfrapPerfThruputCmdClearAllIntfStats = _DfrapPerfThruputCmdClearAllIntfStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 3),
    _DfrapPerfThruputCmdClearAllIntfStats_Type()
)
dfrapPerfThruputCmdClearAllIntfStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdClearAllIntfStats.setStatus("mandatory")


class _DfrapPerfThruputCmdClearDlciStats_Type(Integer32):
    """Custom type dfrapPerfThruputCmdClearDlciStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfThruputCmdClearDlciStats_Type.__name__ = "Integer32"
_DfrapPerfThruputCmdClearDlciStats_Object = MibScalar
dfrapPerfThruputCmdClearDlciStats = _DfrapPerfThruputCmdClearDlciStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 4),
    _DfrapPerfThruputCmdClearDlciStats_Type()
)
dfrapPerfThruputCmdClearDlciStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdClearDlciStats.setStatus("mandatory")


class _DfrapPerfThruputCmdClearAllStats_Type(Integer32):
    """Custom type dfrapPerfThruputCmdClearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfThruputCmdClearAllStats_Type.__name__ = "Integer32"
_DfrapPerfThruputCmdClearAllStats_Object = MibScalar
dfrapPerfThruputCmdClearAllStats = _DfrapPerfThruputCmdClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 5),
    _DfrapPerfThruputCmdClearAllStats_Type()
)
dfrapPerfThruputCmdClearAllStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdClearAllStats.setStatus("mandatory")
_DfrapPerfThruputCmdRemoveStsDlci_Type = Integer32
_DfrapPerfThruputCmdRemoveStsDlci_Object = MibScalar
dfrapPerfThruputCmdRemoveStsDlci = _DfrapPerfThruputCmdRemoveStsDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 6),
    _DfrapPerfThruputCmdRemoveStsDlci_Type()
)
dfrapPerfThruputCmdRemoveStsDlci.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdRemoveStsDlci.setStatus("mandatory")
_DfrapPerfThruputCmdReplaceDlciTable_Object = MibTable
dfrapPerfThruputCmdReplaceDlciTable = _DfrapPerfThruputCmdReplaceDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 7)
)
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdReplaceDlciTable.setStatus("mandatory")
_DfrapPerfThruputCmdReplaceDlciEntry_Object = MibTableRow
dfrapPerfThruputCmdReplaceDlciEntry = _DfrapPerfThruputCmdReplaceDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 7, 1)
)
dfrapPerfThruputCmdReplaceDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfThruputCmdReplaceDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdReplaceDlciEntry.setStatus("mandatory")
_DfrapPerfThruputCmdReplaceDlciValue_Type = Integer32
_DfrapPerfThruputCmdReplaceDlciValue_Object = MibTableColumn
dfrapPerfThruputCmdReplaceDlciValue = _DfrapPerfThruputCmdReplaceDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 7, 1, 1),
    _DfrapPerfThruputCmdReplaceDlciValue_Type()
)
dfrapPerfThruputCmdReplaceDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdReplaceDlciValue.setStatus("mandatory")
_DfrapPerfThruputCmdReplaceDlciNewValue_Type = Integer32
_DfrapPerfThruputCmdReplaceDlciNewValue_Object = MibTableColumn
dfrapPerfThruputCmdReplaceDlciNewValue = _DfrapPerfThruputCmdReplaceDlciNewValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 7, 1, 2),
    _DfrapPerfThruputCmdReplaceDlciNewValue_Type()
)
dfrapPerfThruputCmdReplaceDlciNewValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdReplaceDlciNewValue.setStatus("mandatory")
_DfrapPerfThruputCmdAvailabilityStsDlciReset_Type = Integer32
_DfrapPerfThruputCmdAvailabilityStsDlciReset_Object = MibScalar
dfrapPerfThruputCmdAvailabilityStsDlciReset = _DfrapPerfThruputCmdAvailabilityStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 8),
    _DfrapPerfThruputCmdAvailabilityStsDlciReset_Type()
)
dfrapPerfThruputCmdAvailabilityStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdAvailabilityStsDlciReset.setStatus("mandatory")
_DfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type = Integer32
_DfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object = MibScalar
dfrapPerfThruputCmdAvailabilityStsDlciResetAll = _DfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 9),
    _DfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type()
)
dfrapPerfThruputCmdAvailabilityStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdAvailabilityStsDlciResetAll.setStatus("mandatory")
_DfrapPerfThruputCmdCountsStsDlciReset_Type = Integer32
_DfrapPerfThruputCmdCountsStsDlciReset_Object = MibScalar
dfrapPerfThruputCmdCountsStsDlciReset = _DfrapPerfThruputCmdCountsStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 10),
    _DfrapPerfThruputCmdCountsStsDlciReset_Type()
)
dfrapPerfThruputCmdCountsStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdCountsStsDlciReset.setStatus("mandatory")
_DfrapPerfThruputCmdCountsStsDlciResetAll_Type = Integer32
_DfrapPerfThruputCmdCountsStsDlciResetAll_Object = MibScalar
dfrapPerfThruputCmdCountsStsDlciResetAll = _DfrapPerfThruputCmdCountsStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 11),
    _DfrapPerfThruputCmdCountsStsDlciResetAll_Type()
)
dfrapPerfThruputCmdCountsStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdCountsStsDlciResetAll.setStatus("mandatory")
_DfrapPerfThruputCmdAllStsDlciReset_Type = Integer32
_DfrapPerfThruputCmdAllStsDlciReset_Object = MibScalar
dfrapPerfThruputCmdAllStsDlciReset = _DfrapPerfThruputCmdAllStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 12),
    _DfrapPerfThruputCmdAllStsDlciReset_Type()
)
dfrapPerfThruputCmdAllStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdAllStsDlciReset.setStatus("mandatory")
_DfrapPerfThruputCmdAllStsDlciResetAll_Type = Integer32
_DfrapPerfThruputCmdAllStsDlciResetAll_Object = MibScalar
dfrapPerfThruputCmdAllStsDlciResetAll = _DfrapPerfThruputCmdAllStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 3, 3, 13),
    _DfrapPerfThruputCmdAllStsDlciResetAll_Type()
)
dfrapPerfThruputCmdAllStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfThruputCmdAllStsDlciResetAll.setStatus("mandatory")
_DfrapPerfNetworkShortTerm_ObjectIdentity = ObjectIdentity
dfrapPerfNetworkShortTerm = _DfrapPerfNetworkShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4)
)
_DfrapPerfNetwProtoPerDlciTable_Object = MibTable
dfrapPerfNetwProtoPerDlciTable = _DfrapPerfNetwProtoPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1)
)
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTable.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciEntry_Object = MibTableRow
dfrapPerfNetwProtoPerDlciEntry = _DfrapPerfNetwProtoPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1)
)
dfrapPerfNetwProtoPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfNetwProtoPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfNetwProtoPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciEntry.setStatus("mandatory")


class _DfrapPerfNetwProtoPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfNetwProtoPerDlciInterval based on Integer32"""
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


_DfrapPerfNetwProtoPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfNetwProtoPerDlciInterval_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciInterval = _DfrapPerfNetwProtoPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 1),
    _DfrapPerfNetwProtoPerDlciInterval_Type()
)
dfrapPerfNetwProtoPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciInterval.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciValue_Type = Integer32
_DfrapPerfNetwProtoPerDlciValue_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciValue = _DfrapPerfNetwProtoPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 2),
    _DfrapPerfNetwProtoPerDlciValue_Type()
)
dfrapPerfNetwProtoPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciValue.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxTotal_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxTotal_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxTotal = _DfrapPerfNetwProtoPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 3),
    _DfrapPerfNetwProtoPerDlciRxTotal_Type()
)
dfrapPerfNetwProtoPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxTotal_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxTotal_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxTotal = _DfrapPerfNetwProtoPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 4),
    _DfrapPerfNetwProtoPerDlciTxTotal_Type()
)
dfrapPerfNetwProtoPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxIp_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxIp_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxIp = _DfrapPerfNetwProtoPerDlciRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 5),
    _DfrapPerfNetwProtoPerDlciRxIp_Type()
)
dfrapPerfNetwProtoPerDlciRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxIp.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxIp_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxIp_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxIp = _DfrapPerfNetwProtoPerDlciTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 6),
    _DfrapPerfNetwProtoPerDlciTxIp_Type()
)
dfrapPerfNetwProtoPerDlciTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxIp.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxIpx_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxIpx_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxIpx = _DfrapPerfNetwProtoPerDlciRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 7),
    _DfrapPerfNetwProtoPerDlciRxIpx_Type()
)
dfrapPerfNetwProtoPerDlciRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxIpx.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxIpx_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxIpx_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxIpx = _DfrapPerfNetwProtoPerDlciTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 8),
    _DfrapPerfNetwProtoPerDlciTxIpx_Type()
)
dfrapPerfNetwProtoPerDlciTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxIpx.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxSna_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxSna_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxSna = _DfrapPerfNetwProtoPerDlciRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 9),
    _DfrapPerfNetwProtoPerDlciRxSna_Type()
)
dfrapPerfNetwProtoPerDlciRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxSna.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxSna_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxSna_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxSna = _DfrapPerfNetwProtoPerDlciTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 10),
    _DfrapPerfNetwProtoPerDlciTxSna_Type()
)
dfrapPerfNetwProtoPerDlciTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxSna.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxArp_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxArp_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxArp = _DfrapPerfNetwProtoPerDlciRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 11),
    _DfrapPerfNetwProtoPerDlciRxArp_Type()
)
dfrapPerfNetwProtoPerDlciRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxArp.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxArp_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxArp_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxArp = _DfrapPerfNetwProtoPerDlciTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 12),
    _DfrapPerfNetwProtoPerDlciTxArp_Type()
)
dfrapPerfNetwProtoPerDlciTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxArp.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxCisco_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxCisco_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxCisco = _DfrapPerfNetwProtoPerDlciRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 13),
    _DfrapPerfNetwProtoPerDlciRxCisco_Type()
)
dfrapPerfNetwProtoPerDlciRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxCisco.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxCisco_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxCisco_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxCisco = _DfrapPerfNetwProtoPerDlciTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 14),
    _DfrapPerfNetwProtoPerDlciTxCisco_Type()
)
dfrapPerfNetwProtoPerDlciTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxCisco.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxOther_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxOther_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxOther = _DfrapPerfNetwProtoPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 15),
    _DfrapPerfNetwProtoPerDlciRxOther_Type()
)
dfrapPerfNetwProtoPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxOther.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxOther_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxOther_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxOther = _DfrapPerfNetwProtoPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 16),
    _DfrapPerfNetwProtoPerDlciTxOther_Type()
)
dfrapPerfNetwProtoPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxOther.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxVnip_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxVnip_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxVnip = _DfrapPerfNetwProtoPerDlciRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 17),
    _DfrapPerfNetwProtoPerDlciRxVnip_Type()
)
dfrapPerfNetwProtoPerDlciRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxVnip.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxVnip_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxVnip_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxVnip = _DfrapPerfNetwProtoPerDlciTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 18),
    _DfrapPerfNetwProtoPerDlciTxVnip_Type()
)
dfrapPerfNetwProtoPerDlciTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxVnip.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciRxAnnexG_Type = Counter32
_DfrapPerfNetwProtoPerDlciRxAnnexG_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciRxAnnexG = _DfrapPerfNetwProtoPerDlciRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 19),
    _DfrapPerfNetwProtoPerDlciRxAnnexG_Type()
)
dfrapPerfNetwProtoPerDlciRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciRxAnnexG.setStatus("mandatory")
_DfrapPerfNetwProtoPerDlciTxAnnexG_Type = Counter32
_DfrapPerfNetwProtoPerDlciTxAnnexG_Object = MibTableColumn
dfrapPerfNetwProtoPerDlciTxAnnexG = _DfrapPerfNetwProtoPerDlciTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 1, 1, 20),
    _DfrapPerfNetwProtoPerDlciTxAnnexG_Type()
)
dfrapPerfNetwProtoPerDlciTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoPerDlciTxAnnexG.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTable_Object = MibTable
dfrapPerfNetwProtoTotalTable = _DfrapPerfNetwProtoTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2)
)
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTable.setStatus("mandatory")
_DfrapPerfNetwProtoTotalEntry_Object = MibTableRow
dfrapPerfNetwProtoTotalEntry = _DfrapPerfNetwProtoTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1)
)
dfrapPerfNetwProtoTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfNetwProtoTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalEntry.setStatus("mandatory")


class _DfrapPerfNetwProtoTotalInterval_Type(Integer32):
    """Custom type dfrapPerfNetwProtoTotalInterval based on Integer32"""
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


_DfrapPerfNetwProtoTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfNetwProtoTotalInterval_Object = MibTableColumn
dfrapPerfNetwProtoTotalInterval = _DfrapPerfNetwProtoTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 1),
    _DfrapPerfNetwProtoTotalInterval_Type()
)
dfrapPerfNetwProtoTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalInterval.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxTotal_Type = Counter32
_DfrapPerfNetwProtoTotalRxTotal_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxTotal = _DfrapPerfNetwProtoTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 3),
    _DfrapPerfNetwProtoTotalRxTotal_Type()
)
dfrapPerfNetwProtoTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxTotal.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxTotal_Type = Counter32
_DfrapPerfNetwProtoTotalTxTotal_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxTotal = _DfrapPerfNetwProtoTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 4),
    _DfrapPerfNetwProtoTotalTxTotal_Type()
)
dfrapPerfNetwProtoTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxTotal.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxIp_Type = Counter32
_DfrapPerfNetwProtoTotalRxIp_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxIp = _DfrapPerfNetwProtoTotalRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 5),
    _DfrapPerfNetwProtoTotalRxIp_Type()
)
dfrapPerfNetwProtoTotalRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxIp.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxIp_Type = Counter32
_DfrapPerfNetwProtoTotalTxIp_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxIp = _DfrapPerfNetwProtoTotalTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 6),
    _DfrapPerfNetwProtoTotalTxIp_Type()
)
dfrapPerfNetwProtoTotalTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxIp.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxIpx_Type = Counter32
_DfrapPerfNetwProtoTotalRxIpx_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxIpx = _DfrapPerfNetwProtoTotalRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 7),
    _DfrapPerfNetwProtoTotalRxIpx_Type()
)
dfrapPerfNetwProtoTotalRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxIpx.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxIpx_Type = Counter32
_DfrapPerfNetwProtoTotalTxIpx_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxIpx = _DfrapPerfNetwProtoTotalTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 8),
    _DfrapPerfNetwProtoTotalTxIpx_Type()
)
dfrapPerfNetwProtoTotalTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxIpx.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxSna_Type = Counter32
_DfrapPerfNetwProtoTotalRxSna_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxSna = _DfrapPerfNetwProtoTotalRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 9),
    _DfrapPerfNetwProtoTotalRxSna_Type()
)
dfrapPerfNetwProtoTotalRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxSna.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxSna_Type = Counter32
_DfrapPerfNetwProtoTotalTxSna_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxSna = _DfrapPerfNetwProtoTotalTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 10),
    _DfrapPerfNetwProtoTotalTxSna_Type()
)
dfrapPerfNetwProtoTotalTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxSna.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxArp_Type = Counter32
_DfrapPerfNetwProtoTotalRxArp_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxArp = _DfrapPerfNetwProtoTotalRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 11),
    _DfrapPerfNetwProtoTotalRxArp_Type()
)
dfrapPerfNetwProtoTotalRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxArp.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxArp_Type = Counter32
_DfrapPerfNetwProtoTotalTxArp_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxArp = _DfrapPerfNetwProtoTotalTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 12),
    _DfrapPerfNetwProtoTotalTxArp_Type()
)
dfrapPerfNetwProtoTotalTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxArp.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxCisco_Type = Counter32
_DfrapPerfNetwProtoTotalRxCisco_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxCisco = _DfrapPerfNetwProtoTotalRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 13),
    _DfrapPerfNetwProtoTotalRxCisco_Type()
)
dfrapPerfNetwProtoTotalRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxCisco.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxCisco_Type = Counter32
_DfrapPerfNetwProtoTotalTxCisco_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxCisco = _DfrapPerfNetwProtoTotalTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 14),
    _DfrapPerfNetwProtoTotalTxCisco_Type()
)
dfrapPerfNetwProtoTotalTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxCisco.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxOther_Type = Counter32
_DfrapPerfNetwProtoTotalRxOther_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxOther = _DfrapPerfNetwProtoTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 15),
    _DfrapPerfNetwProtoTotalRxOther_Type()
)
dfrapPerfNetwProtoTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxOther.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxOther_Type = Counter32
_DfrapPerfNetwProtoTotalTxOther_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxOther = _DfrapPerfNetwProtoTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 16),
    _DfrapPerfNetwProtoTotalTxOther_Type()
)
dfrapPerfNetwProtoTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxOther.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxVnip_Type = Counter32
_DfrapPerfNetwProtoTotalRxVnip_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxVnip = _DfrapPerfNetwProtoTotalRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 17),
    _DfrapPerfNetwProtoTotalRxVnip_Type()
)
dfrapPerfNetwProtoTotalRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxVnip.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxVnip_Type = Counter32
_DfrapPerfNetwProtoTotalTxVnip_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxVnip = _DfrapPerfNetwProtoTotalTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 18),
    _DfrapPerfNetwProtoTotalTxVnip_Type()
)
dfrapPerfNetwProtoTotalTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxVnip.setStatus("mandatory")
_DfrapPerfNetwProtoTotalRxAnnexG_Type = Counter32
_DfrapPerfNetwProtoTotalRxAnnexG_Object = MibTableColumn
dfrapPerfNetwProtoTotalRxAnnexG = _DfrapPerfNetwProtoTotalRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 19),
    _DfrapPerfNetwProtoTotalRxAnnexG_Type()
)
dfrapPerfNetwProtoTotalRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalRxAnnexG.setStatus("mandatory")
_DfrapPerfNetwProtoTotalTxAnnexG_Type = Counter32
_DfrapPerfNetwProtoTotalTxAnnexG_Object = MibTableColumn
dfrapPerfNetwProtoTotalTxAnnexG = _DfrapPerfNetwProtoTotalTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 2, 1, 20),
    _DfrapPerfNetwProtoTotalTxAnnexG_Type()
)
dfrapPerfNetwProtoTotalTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwProtoTotalTxAnnexG.setStatus("mandatory")
_DfrapPerfIpPerDlciTable_Object = MibTable
dfrapPerfIpPerDlciTable = _DfrapPerfIpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3)
)
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTable.setStatus("mandatory")
_DfrapPerfIpPerDlciEntry_Object = MibTableRow
dfrapPerfIpPerDlciEntry = _DfrapPerfIpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1)
)
dfrapPerfIpPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIpPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfIpPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciEntry.setStatus("mandatory")


class _DfrapPerfIpPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfIpPerDlciInterval based on Integer32"""
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


_DfrapPerfIpPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfIpPerDlciInterval_Object = MibTableColumn
dfrapPerfIpPerDlciInterval = _DfrapPerfIpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 1),
    _DfrapPerfIpPerDlciInterval_Type()
)
dfrapPerfIpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciInterval.setStatus("mandatory")
_DfrapPerfIpPerDlciValue_Type = Integer32
_DfrapPerfIpPerDlciValue_Object = MibTableColumn
dfrapPerfIpPerDlciValue = _DfrapPerfIpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 2),
    _DfrapPerfIpPerDlciValue_Type()
)
dfrapPerfIpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciValue.setStatus("mandatory")
_DfrapPerfIpPerDlciRxTotal_Type = Counter32
_DfrapPerfIpPerDlciRxTotal_Object = MibTableColumn
dfrapPerfIpPerDlciRxTotal = _DfrapPerfIpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 3),
    _DfrapPerfIpPerDlciRxTotal_Type()
)
dfrapPerfIpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfIpPerDlciTxTotal_Type = Counter32
_DfrapPerfIpPerDlciTxTotal_Object = MibTableColumn
dfrapPerfIpPerDlciTxTotal = _DfrapPerfIpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 4),
    _DfrapPerfIpPerDlciTxTotal_Type()
)
dfrapPerfIpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfIpPerDlciRxTcp_Type = Counter32
_DfrapPerfIpPerDlciRxTcp_Object = MibTableColumn
dfrapPerfIpPerDlciRxTcp = _DfrapPerfIpPerDlciRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 5),
    _DfrapPerfIpPerDlciRxTcp_Type()
)
dfrapPerfIpPerDlciRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxTcp.setStatus("mandatory")
_DfrapPerfIpPerDlciTxTcp_Type = Counter32
_DfrapPerfIpPerDlciTxTcp_Object = MibTableColumn
dfrapPerfIpPerDlciTxTcp = _DfrapPerfIpPerDlciTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 6),
    _DfrapPerfIpPerDlciTxTcp_Type()
)
dfrapPerfIpPerDlciTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxTcp.setStatus("mandatory")
_DfrapPerfIpPerDlciRxUdp_Type = Counter32
_DfrapPerfIpPerDlciRxUdp_Object = MibTableColumn
dfrapPerfIpPerDlciRxUdp = _DfrapPerfIpPerDlciRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 7),
    _DfrapPerfIpPerDlciRxUdp_Type()
)
dfrapPerfIpPerDlciRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxUdp.setStatus("mandatory")
_DfrapPerfIpPerDlciTxUdp_Type = Counter32
_DfrapPerfIpPerDlciTxUdp_Object = MibTableColumn
dfrapPerfIpPerDlciTxUdp = _DfrapPerfIpPerDlciTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 8),
    _DfrapPerfIpPerDlciTxUdp_Type()
)
dfrapPerfIpPerDlciTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxUdp.setStatus("mandatory")
_DfrapPerfIpPerDlciRxIcmp_Type = Counter32
_DfrapPerfIpPerDlciRxIcmp_Object = MibTableColumn
dfrapPerfIpPerDlciRxIcmp = _DfrapPerfIpPerDlciRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 9),
    _DfrapPerfIpPerDlciRxIcmp_Type()
)
dfrapPerfIpPerDlciRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxIcmp.setStatus("mandatory")
_DfrapPerfIpPerDlciTxIcmp_Type = Counter32
_DfrapPerfIpPerDlciTxIcmp_Object = MibTableColumn
dfrapPerfIpPerDlciTxIcmp = _DfrapPerfIpPerDlciTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 10),
    _DfrapPerfIpPerDlciTxIcmp_Type()
)
dfrapPerfIpPerDlciTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxIcmp.setStatus("mandatory")
_DfrapPerfIpPerDlciRxOther_Type = Counter32
_DfrapPerfIpPerDlciRxOther_Object = MibTableColumn
dfrapPerfIpPerDlciRxOther = _DfrapPerfIpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 11),
    _DfrapPerfIpPerDlciRxOther_Type()
)
dfrapPerfIpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxOther.setStatus("mandatory")
_DfrapPerfIpPerDlciTxOther_Type = Counter32
_DfrapPerfIpPerDlciTxOther_Object = MibTableColumn
dfrapPerfIpPerDlciTxOther = _DfrapPerfIpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 12),
    _DfrapPerfIpPerDlciTxOther_Type()
)
dfrapPerfIpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxOther.setStatus("mandatory")
_DfrapPerfIpPerDlciRxIgrp_Type = Counter32
_DfrapPerfIpPerDlciRxIgrp_Object = MibTableColumn
dfrapPerfIpPerDlciRxIgrp = _DfrapPerfIpPerDlciRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 13),
    _DfrapPerfIpPerDlciRxIgrp_Type()
)
dfrapPerfIpPerDlciRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciRxIgrp.setStatus("mandatory")
_DfrapPerfIpPerDlciTxIgrp_Type = Counter32
_DfrapPerfIpPerDlciTxIgrp_Object = MibTableColumn
dfrapPerfIpPerDlciTxIgrp = _DfrapPerfIpPerDlciTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 3, 1, 14),
    _DfrapPerfIpPerDlciTxIgrp_Type()
)
dfrapPerfIpPerDlciTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpPerDlciTxIgrp.setStatus("mandatory")
_DfrapPerfIpTotalTable_Object = MibTable
dfrapPerfIpTotalTable = _DfrapPerfIpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4)
)
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTable.setStatus("mandatory")
_DfrapPerfIpTotalEntry_Object = MibTableRow
dfrapPerfIpTotalEntry = _DfrapPerfIpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1)
)
dfrapPerfIpTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIpTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfIpTotalEntry.setStatus("mandatory")


class _DfrapPerfIpTotalInterval_Type(Integer32):
    """Custom type dfrapPerfIpTotalInterval based on Integer32"""
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


_DfrapPerfIpTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfIpTotalInterval_Object = MibTableColumn
dfrapPerfIpTotalInterval = _DfrapPerfIpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 1),
    _DfrapPerfIpTotalInterval_Type()
)
dfrapPerfIpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalInterval.setStatus("mandatory")
_DfrapPerfIpTotalRxTotal_Type = Counter32
_DfrapPerfIpTotalRxTotal_Object = MibTableColumn
dfrapPerfIpTotalRxTotal = _DfrapPerfIpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 3),
    _DfrapPerfIpTotalRxTotal_Type()
)
dfrapPerfIpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxTotal.setStatus("mandatory")
_DfrapPerfIpTotalTxTotal_Type = Counter32
_DfrapPerfIpTotalTxTotal_Object = MibTableColumn
dfrapPerfIpTotalTxTotal = _DfrapPerfIpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 4),
    _DfrapPerfIpTotalTxTotal_Type()
)
dfrapPerfIpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxTotal.setStatus("mandatory")
_DfrapPerfIpTotalRxTcp_Type = Counter32
_DfrapPerfIpTotalRxTcp_Object = MibTableColumn
dfrapPerfIpTotalRxTcp = _DfrapPerfIpTotalRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 5),
    _DfrapPerfIpTotalRxTcp_Type()
)
dfrapPerfIpTotalRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxTcp.setStatus("mandatory")
_DfrapPerfIpTotalTxTcp_Type = Counter32
_DfrapPerfIpTotalTxTcp_Object = MibTableColumn
dfrapPerfIpTotalTxTcp = _DfrapPerfIpTotalTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 6),
    _DfrapPerfIpTotalTxTcp_Type()
)
dfrapPerfIpTotalTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxTcp.setStatus("mandatory")
_DfrapPerfIpTotalRxUdp_Type = Counter32
_DfrapPerfIpTotalRxUdp_Object = MibTableColumn
dfrapPerfIpTotalRxUdp = _DfrapPerfIpTotalRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 7),
    _DfrapPerfIpTotalRxUdp_Type()
)
dfrapPerfIpTotalRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxUdp.setStatus("mandatory")
_DfrapPerfIpTotalTxUdp_Type = Counter32
_DfrapPerfIpTotalTxUdp_Object = MibTableColumn
dfrapPerfIpTotalTxUdp = _DfrapPerfIpTotalTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 8),
    _DfrapPerfIpTotalTxUdp_Type()
)
dfrapPerfIpTotalTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxUdp.setStatus("mandatory")
_DfrapPerfIpTotalRxIcmp_Type = Counter32
_DfrapPerfIpTotalRxIcmp_Object = MibTableColumn
dfrapPerfIpTotalRxIcmp = _DfrapPerfIpTotalRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 9),
    _DfrapPerfIpTotalRxIcmp_Type()
)
dfrapPerfIpTotalRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxIcmp.setStatus("mandatory")
_DfrapPerfIpTotalTxIcmp_Type = Counter32
_DfrapPerfIpTotalTxIcmp_Object = MibTableColumn
dfrapPerfIpTotalTxIcmp = _DfrapPerfIpTotalTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 10),
    _DfrapPerfIpTotalTxIcmp_Type()
)
dfrapPerfIpTotalTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxIcmp.setStatus("mandatory")
_DfrapPerfIpTotalRxOther_Type = Counter32
_DfrapPerfIpTotalRxOther_Object = MibTableColumn
dfrapPerfIpTotalRxOther = _DfrapPerfIpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 11),
    _DfrapPerfIpTotalRxOther_Type()
)
dfrapPerfIpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxOther.setStatus("mandatory")
_DfrapPerfIpTotalTxOther_Type = Counter32
_DfrapPerfIpTotalTxOther_Object = MibTableColumn
dfrapPerfIpTotalTxOther = _DfrapPerfIpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 12),
    _DfrapPerfIpTotalTxOther_Type()
)
dfrapPerfIpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxOther.setStatus("mandatory")
_DfrapPerfIpTotalRxIgrp_Type = Counter32
_DfrapPerfIpTotalRxIgrp_Object = MibTableColumn
dfrapPerfIpTotalRxIgrp = _DfrapPerfIpTotalRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 13),
    _DfrapPerfIpTotalRxIgrp_Type()
)
dfrapPerfIpTotalRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalRxIgrp.setStatus("mandatory")
_DfrapPerfIpTotalTxIgrp_Type = Counter32
_DfrapPerfIpTotalTxIgrp_Object = MibTableColumn
dfrapPerfIpTotalTxIgrp = _DfrapPerfIpTotalTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 4, 1, 14),
    _DfrapPerfIpTotalTxIgrp_Type()
)
dfrapPerfIpTotalTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpTotalTxIgrp.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTable_Object = MibTable
dfrapPerfIcmpPerDlciTable = _DfrapPerfIcmpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5)
)
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTable.setStatus("mandatory")
_DfrapPerfIcmpPerDlciEntry_Object = MibTableRow
dfrapPerfIcmpPerDlciEntry = _DfrapPerfIcmpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1)
)
dfrapPerfIcmpPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIcmpPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfIcmpPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciEntry.setStatus("mandatory")


class _DfrapPerfIcmpPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfIcmpPerDlciInterval based on Integer32"""
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


_DfrapPerfIcmpPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfIcmpPerDlciInterval_Object = MibTableColumn
dfrapPerfIcmpPerDlciInterval = _DfrapPerfIcmpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 1),
    _DfrapPerfIcmpPerDlciInterval_Type()
)
dfrapPerfIcmpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciInterval.setStatus("mandatory")
_DfrapPerfIcmpPerDlciValue_Type = Integer32
_DfrapPerfIcmpPerDlciValue_Object = MibTableColumn
dfrapPerfIcmpPerDlciValue = _DfrapPerfIcmpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 2),
    _DfrapPerfIcmpPerDlciValue_Type()
)
dfrapPerfIcmpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciValue.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxTotal_Type = Counter32
_DfrapPerfIcmpPerDlciRxTotal_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxTotal = _DfrapPerfIcmpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 3),
    _DfrapPerfIcmpPerDlciRxTotal_Type()
)
dfrapPerfIcmpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxTotal_Type = Counter32
_DfrapPerfIcmpPerDlciTxTotal_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxTotal = _DfrapPerfIcmpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 4),
    _DfrapPerfIcmpPerDlciTxTotal_Type()
)
dfrapPerfIcmpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxEchoRep_Type = Counter32
_DfrapPerfIcmpPerDlciRxEchoRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxEchoRep = _DfrapPerfIcmpPerDlciRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 5),
    _DfrapPerfIcmpPerDlciRxEchoRep_Type()
)
dfrapPerfIcmpPerDlciRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxEchoRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxEchoRep_Type = Counter32
_DfrapPerfIcmpPerDlciTxEchoRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxEchoRep = _DfrapPerfIcmpPerDlciTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 6),
    _DfrapPerfIcmpPerDlciTxEchoRep_Type()
)
dfrapPerfIcmpPerDlciTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxEchoRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxDestUnr_Type = Counter32
_DfrapPerfIcmpPerDlciRxDestUnr_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxDestUnr = _DfrapPerfIcmpPerDlciRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 7),
    _DfrapPerfIcmpPerDlciRxDestUnr_Type()
)
dfrapPerfIcmpPerDlciRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxDestUnr.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxDestUnr_Type = Counter32
_DfrapPerfIcmpPerDlciTxDestUnr_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxDestUnr = _DfrapPerfIcmpPerDlciTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 8),
    _DfrapPerfIcmpPerDlciTxDestUnr_Type()
)
dfrapPerfIcmpPerDlciTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxDestUnr.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxSrcQuench_Type = Counter32
_DfrapPerfIcmpPerDlciRxSrcQuench_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxSrcQuench = _DfrapPerfIcmpPerDlciRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 9),
    _DfrapPerfIcmpPerDlciRxSrcQuench_Type()
)
dfrapPerfIcmpPerDlciRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxSrcQuench.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxSrcQuench_Type = Counter32
_DfrapPerfIcmpPerDlciTxSrcQuench_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxSrcQuench = _DfrapPerfIcmpPerDlciTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 10),
    _DfrapPerfIcmpPerDlciTxSrcQuench_Type()
)
dfrapPerfIcmpPerDlciTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxSrcQuench.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxRedirect_Type = Counter32
_DfrapPerfIcmpPerDlciRxRedirect_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxRedirect = _DfrapPerfIcmpPerDlciRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 11),
    _DfrapPerfIcmpPerDlciRxRedirect_Type()
)
dfrapPerfIcmpPerDlciRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxRedirect.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxRedirect_Type = Counter32
_DfrapPerfIcmpPerDlciTxRedirect_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxRedirect = _DfrapPerfIcmpPerDlciTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 12),
    _DfrapPerfIcmpPerDlciTxRedirect_Type()
)
dfrapPerfIcmpPerDlciTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxRedirect.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxEchoReq_Type = Counter32
_DfrapPerfIcmpPerDlciRxEchoReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxEchoReq = _DfrapPerfIcmpPerDlciRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 13),
    _DfrapPerfIcmpPerDlciRxEchoReq_Type()
)
dfrapPerfIcmpPerDlciRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxEchoReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxEchoReq_Type = Counter32
_DfrapPerfIcmpPerDlciTxEchoReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxEchoReq = _DfrapPerfIcmpPerDlciTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 14),
    _DfrapPerfIcmpPerDlciTxEchoReq_Type()
)
dfrapPerfIcmpPerDlciTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxEchoReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxTimeExcd_Type = Counter32
_DfrapPerfIcmpPerDlciRxTimeExcd_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxTimeExcd = _DfrapPerfIcmpPerDlciRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 15),
    _DfrapPerfIcmpPerDlciRxTimeExcd_Type()
)
dfrapPerfIcmpPerDlciRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxTimeExcd.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxTimeExcd_Type = Counter32
_DfrapPerfIcmpPerDlciTxTimeExcd_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxTimeExcd = _DfrapPerfIcmpPerDlciTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 16),
    _DfrapPerfIcmpPerDlciTxTimeExcd_Type()
)
dfrapPerfIcmpPerDlciTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxTimeExcd.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxParamProb_Type = Counter32
_DfrapPerfIcmpPerDlciRxParamProb_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxParamProb = _DfrapPerfIcmpPerDlciRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 17),
    _DfrapPerfIcmpPerDlciRxParamProb_Type()
)
dfrapPerfIcmpPerDlciRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxParamProb.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxParamProb_Type = Counter32
_DfrapPerfIcmpPerDlciTxParamProb_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxParamProb = _DfrapPerfIcmpPerDlciTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 18),
    _DfrapPerfIcmpPerDlciTxParamProb_Type()
)
dfrapPerfIcmpPerDlciTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxParamProb.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxTimestpReq_Type = Counter32
_DfrapPerfIcmpPerDlciRxTimestpReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxTimestpReq = _DfrapPerfIcmpPerDlciRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 19),
    _DfrapPerfIcmpPerDlciRxTimestpReq_Type()
)
dfrapPerfIcmpPerDlciRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxTimestpReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxTimestpReq_Type = Counter32
_DfrapPerfIcmpPerDlciTxTimestpReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxTimestpReq = _DfrapPerfIcmpPerDlciTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 20),
    _DfrapPerfIcmpPerDlciTxTimestpReq_Type()
)
dfrapPerfIcmpPerDlciTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxTimestpReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxTimestpRep_Type = Counter32
_DfrapPerfIcmpPerDlciRxTimestpRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxTimestpRep = _DfrapPerfIcmpPerDlciRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 21),
    _DfrapPerfIcmpPerDlciRxTimestpRep_Type()
)
dfrapPerfIcmpPerDlciRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxTimestpRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxTimestpRep_Type = Counter32
_DfrapPerfIcmpPerDlciTxTimestpRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxTimestpRep = _DfrapPerfIcmpPerDlciTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 22),
    _DfrapPerfIcmpPerDlciTxTimestpRep_Type()
)
dfrapPerfIcmpPerDlciTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxTimestpRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxAddrMaskReq_Type = Counter32
_DfrapPerfIcmpPerDlciRxAddrMaskReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxAddrMaskReq = _DfrapPerfIcmpPerDlciRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 23),
    _DfrapPerfIcmpPerDlciRxAddrMaskReq_Type()
)
dfrapPerfIcmpPerDlciRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxAddrMaskReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxAddrMaskReq_Type = Counter32
_DfrapPerfIcmpPerDlciTxAddrMaskReq_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxAddrMaskReq = _DfrapPerfIcmpPerDlciTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 24),
    _DfrapPerfIcmpPerDlciTxAddrMaskReq_Type()
)
dfrapPerfIcmpPerDlciTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxAddrMaskReq.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxAddrMaskRep_Type = Counter32
_DfrapPerfIcmpPerDlciRxAddrMaskRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxAddrMaskRep = _DfrapPerfIcmpPerDlciRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 25),
    _DfrapPerfIcmpPerDlciRxAddrMaskRep_Type()
)
dfrapPerfIcmpPerDlciRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxAddrMaskRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxAddrMaskRep_Type = Counter32
_DfrapPerfIcmpPerDlciTxAddrMaskRep_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxAddrMaskRep = _DfrapPerfIcmpPerDlciTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 26),
    _DfrapPerfIcmpPerDlciTxAddrMaskRep_Type()
)
dfrapPerfIcmpPerDlciTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxAddrMaskRep.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxPktTooBig_Type = Counter32
_DfrapPerfIcmpPerDlciRxPktTooBig_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxPktTooBig = _DfrapPerfIcmpPerDlciRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 27),
    _DfrapPerfIcmpPerDlciRxPktTooBig_Type()
)
dfrapPerfIcmpPerDlciRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxPktTooBig.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxPktTooBig_Type = Counter32
_DfrapPerfIcmpPerDlciTxPktTooBig_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxPktTooBig = _DfrapPerfIcmpPerDlciTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 28),
    _DfrapPerfIcmpPerDlciTxPktTooBig_Type()
)
dfrapPerfIcmpPerDlciTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxPktTooBig.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxGmQuery_Type = Counter32
_DfrapPerfIcmpPerDlciRxGmQuery_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxGmQuery = _DfrapPerfIcmpPerDlciRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 29),
    _DfrapPerfIcmpPerDlciRxGmQuery_Type()
)
dfrapPerfIcmpPerDlciRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxGmQuery.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxGmQuery_Type = Counter32
_DfrapPerfIcmpPerDlciTxGmQuery_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxGmQuery = _DfrapPerfIcmpPerDlciTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 30),
    _DfrapPerfIcmpPerDlciTxGmQuery_Type()
)
dfrapPerfIcmpPerDlciTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxGmQuery.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxGmReport_Type = Counter32
_DfrapPerfIcmpPerDlciRxGmReport_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxGmReport = _DfrapPerfIcmpPerDlciRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 31),
    _DfrapPerfIcmpPerDlciRxGmReport_Type()
)
dfrapPerfIcmpPerDlciRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxGmReport.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxGmReport_Type = Counter32
_DfrapPerfIcmpPerDlciTxGmReport_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxGmReport = _DfrapPerfIcmpPerDlciTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 32),
    _DfrapPerfIcmpPerDlciTxGmReport_Type()
)
dfrapPerfIcmpPerDlciTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxGmReport.setStatus("mandatory")
_DfrapPerfIcmpPerDlciRxGmReduct_Type = Counter32
_DfrapPerfIcmpPerDlciRxGmReduct_Object = MibTableColumn
dfrapPerfIcmpPerDlciRxGmReduct = _DfrapPerfIcmpPerDlciRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 33),
    _DfrapPerfIcmpPerDlciRxGmReduct_Type()
)
dfrapPerfIcmpPerDlciRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciRxGmReduct.setStatus("mandatory")
_DfrapPerfIcmpPerDlciTxGmReduct_Type = Counter32
_DfrapPerfIcmpPerDlciTxGmReduct_Object = MibTableColumn
dfrapPerfIcmpPerDlciTxGmReduct = _DfrapPerfIcmpPerDlciTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 5, 1, 34),
    _DfrapPerfIcmpPerDlciTxGmReduct_Type()
)
dfrapPerfIcmpPerDlciTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpPerDlciTxGmReduct.setStatus("mandatory")
_DfrapPerfIcmpTotalTable_Object = MibTable
dfrapPerfIcmpTotalTable = _DfrapPerfIcmpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6)
)
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTable.setStatus("mandatory")
_DfrapPerfIcmpTotalEntry_Object = MibTableRow
dfrapPerfIcmpTotalEntry = _DfrapPerfIcmpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1)
)
dfrapPerfIcmpTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIcmpTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalEntry.setStatus("mandatory")


class _DfrapPerfIcmpTotalInterval_Type(Integer32):
    """Custom type dfrapPerfIcmpTotalInterval based on Integer32"""
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


_DfrapPerfIcmpTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfIcmpTotalInterval_Object = MibTableColumn
dfrapPerfIcmpTotalInterval = _DfrapPerfIcmpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 1),
    _DfrapPerfIcmpTotalInterval_Type()
)
dfrapPerfIcmpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalInterval.setStatus("mandatory")
_DfrapPerfIcmpTotalRxTotal_Type = Counter32
_DfrapPerfIcmpTotalRxTotal_Object = MibTableColumn
dfrapPerfIcmpTotalRxTotal = _DfrapPerfIcmpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 3),
    _DfrapPerfIcmpTotalRxTotal_Type()
)
dfrapPerfIcmpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxTotal.setStatus("mandatory")
_DfrapPerfIcmpTotalTxTotal_Type = Counter32
_DfrapPerfIcmpTotalTxTotal_Object = MibTableColumn
dfrapPerfIcmpTotalTxTotal = _DfrapPerfIcmpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 4),
    _DfrapPerfIcmpTotalTxTotal_Type()
)
dfrapPerfIcmpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxTotal.setStatus("mandatory")
_DfrapPerfIcmpTotalRxEchoRep_Type = Counter32
_DfrapPerfIcmpTotalRxEchoRep_Object = MibTableColumn
dfrapPerfIcmpTotalRxEchoRep = _DfrapPerfIcmpTotalRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 5),
    _DfrapPerfIcmpTotalRxEchoRep_Type()
)
dfrapPerfIcmpTotalRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxEchoRep.setStatus("mandatory")
_DfrapPerfIcmpTotalTxEchoRep_Type = Counter32
_DfrapPerfIcmpTotalTxEchoRep_Object = MibTableColumn
dfrapPerfIcmpTotalTxEchoRep = _DfrapPerfIcmpTotalTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 6),
    _DfrapPerfIcmpTotalTxEchoRep_Type()
)
dfrapPerfIcmpTotalTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxEchoRep.setStatus("mandatory")
_DfrapPerfIcmpTotalRxDestUnr_Type = Counter32
_DfrapPerfIcmpTotalRxDestUnr_Object = MibTableColumn
dfrapPerfIcmpTotalRxDestUnr = _DfrapPerfIcmpTotalRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 7),
    _DfrapPerfIcmpTotalRxDestUnr_Type()
)
dfrapPerfIcmpTotalRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxDestUnr.setStatus("mandatory")
_DfrapPerfIcmpTotalTxDestUnr_Type = Counter32
_DfrapPerfIcmpTotalTxDestUnr_Object = MibTableColumn
dfrapPerfIcmpTotalTxDestUnr = _DfrapPerfIcmpTotalTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 8),
    _DfrapPerfIcmpTotalTxDestUnr_Type()
)
dfrapPerfIcmpTotalTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxDestUnr.setStatus("mandatory")
_DfrapPerfIcmpTotalRxSrcQuench_Type = Counter32
_DfrapPerfIcmpTotalRxSrcQuench_Object = MibTableColumn
dfrapPerfIcmpTotalRxSrcQuench = _DfrapPerfIcmpTotalRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 9),
    _DfrapPerfIcmpTotalRxSrcQuench_Type()
)
dfrapPerfIcmpTotalRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxSrcQuench.setStatus("mandatory")
_DfrapPerfIcmpTotalTxSrcQuench_Type = Counter32
_DfrapPerfIcmpTotalTxSrcQuench_Object = MibTableColumn
dfrapPerfIcmpTotalTxSrcQuench = _DfrapPerfIcmpTotalTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 10),
    _DfrapPerfIcmpTotalTxSrcQuench_Type()
)
dfrapPerfIcmpTotalTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxSrcQuench.setStatus("mandatory")
_DfrapPerfIcmpTotalRxRedirect_Type = Counter32
_DfrapPerfIcmpTotalRxRedirect_Object = MibTableColumn
dfrapPerfIcmpTotalRxRedirect = _DfrapPerfIcmpTotalRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 11),
    _DfrapPerfIcmpTotalRxRedirect_Type()
)
dfrapPerfIcmpTotalRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxRedirect.setStatus("mandatory")
_DfrapPerfIcmpTotalTxRedirect_Type = Counter32
_DfrapPerfIcmpTotalTxRedirect_Object = MibTableColumn
dfrapPerfIcmpTotalTxRedirect = _DfrapPerfIcmpTotalTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 12),
    _DfrapPerfIcmpTotalTxRedirect_Type()
)
dfrapPerfIcmpTotalTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxRedirect.setStatus("mandatory")
_DfrapPerfIcmpTotalRxEchoReq_Type = Counter32
_DfrapPerfIcmpTotalRxEchoReq_Object = MibTableColumn
dfrapPerfIcmpTotalRxEchoReq = _DfrapPerfIcmpTotalRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 13),
    _DfrapPerfIcmpTotalRxEchoReq_Type()
)
dfrapPerfIcmpTotalRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxEchoReq.setStatus("mandatory")
_DfrapPerfIcmpTotalTxEchoReq_Type = Counter32
_DfrapPerfIcmpTotalTxEchoReq_Object = MibTableColumn
dfrapPerfIcmpTotalTxEchoReq = _DfrapPerfIcmpTotalTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 14),
    _DfrapPerfIcmpTotalTxEchoReq_Type()
)
dfrapPerfIcmpTotalTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxEchoReq.setStatus("mandatory")
_DfrapPerfIcmpTotalRxTimeExcd_Type = Counter32
_DfrapPerfIcmpTotalRxTimeExcd_Object = MibTableColumn
dfrapPerfIcmpTotalRxTimeExcd = _DfrapPerfIcmpTotalRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 15),
    _DfrapPerfIcmpTotalRxTimeExcd_Type()
)
dfrapPerfIcmpTotalRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxTimeExcd.setStatus("mandatory")
_DfrapPerfIcmpTotalTxTimeExcd_Type = Counter32
_DfrapPerfIcmpTotalTxTimeExcd_Object = MibTableColumn
dfrapPerfIcmpTotalTxTimeExcd = _DfrapPerfIcmpTotalTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 16),
    _DfrapPerfIcmpTotalTxTimeExcd_Type()
)
dfrapPerfIcmpTotalTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxTimeExcd.setStatus("mandatory")
_DfrapPerfIcmpTotalRxParamProb_Type = Counter32
_DfrapPerfIcmpTotalRxParamProb_Object = MibTableColumn
dfrapPerfIcmpTotalRxParamProb = _DfrapPerfIcmpTotalRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 17),
    _DfrapPerfIcmpTotalRxParamProb_Type()
)
dfrapPerfIcmpTotalRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxParamProb.setStatus("mandatory")
_DfrapPerfIcmpTotalTxParamProb_Type = Counter32
_DfrapPerfIcmpTotalTxParamProb_Object = MibTableColumn
dfrapPerfIcmpTotalTxParamProb = _DfrapPerfIcmpTotalTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 18),
    _DfrapPerfIcmpTotalTxParamProb_Type()
)
dfrapPerfIcmpTotalTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxParamProb.setStatus("mandatory")
_DfrapPerfIcmpTotalRxTimestpReq_Type = Counter32
_DfrapPerfIcmpTotalRxTimestpReq_Object = MibTableColumn
dfrapPerfIcmpTotalRxTimestpReq = _DfrapPerfIcmpTotalRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 19),
    _DfrapPerfIcmpTotalRxTimestpReq_Type()
)
dfrapPerfIcmpTotalRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxTimestpReq.setStatus("mandatory")
_DfrapPerfIcmpTotalTxTimestpReq_Type = Counter32
_DfrapPerfIcmpTotalTxTimestpReq_Object = MibTableColumn
dfrapPerfIcmpTotalTxTimestpReq = _DfrapPerfIcmpTotalTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 20),
    _DfrapPerfIcmpTotalTxTimestpReq_Type()
)
dfrapPerfIcmpTotalTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxTimestpReq.setStatus("mandatory")
_DfrapPerfIcmpTotalRxTimestpRep_Type = Counter32
_DfrapPerfIcmpTotalRxTimestpRep_Object = MibTableColumn
dfrapPerfIcmpTotalRxTimestpRep = _DfrapPerfIcmpTotalRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 21),
    _DfrapPerfIcmpTotalRxTimestpRep_Type()
)
dfrapPerfIcmpTotalRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxTimestpRep.setStatus("mandatory")
_DfrapPerfIcmpTotalTxTimestpRep_Type = Counter32
_DfrapPerfIcmpTotalTxTimestpRep_Object = MibTableColumn
dfrapPerfIcmpTotalTxTimestpRep = _DfrapPerfIcmpTotalTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 22),
    _DfrapPerfIcmpTotalTxTimestpRep_Type()
)
dfrapPerfIcmpTotalTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxTimestpRep.setStatus("mandatory")
_DfrapPerfIcmpTotalRxAddrMaskReq_Type = Counter32
_DfrapPerfIcmpTotalRxAddrMaskReq_Object = MibTableColumn
dfrapPerfIcmpTotalRxAddrMaskReq = _DfrapPerfIcmpTotalRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 23),
    _DfrapPerfIcmpTotalRxAddrMaskReq_Type()
)
dfrapPerfIcmpTotalRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxAddrMaskReq.setStatus("mandatory")
_DfrapPerfIcmpTotalTxAddrMaskReq_Type = Counter32
_DfrapPerfIcmpTotalTxAddrMaskReq_Object = MibTableColumn
dfrapPerfIcmpTotalTxAddrMaskReq = _DfrapPerfIcmpTotalTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 24),
    _DfrapPerfIcmpTotalTxAddrMaskReq_Type()
)
dfrapPerfIcmpTotalTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxAddrMaskReq.setStatus("mandatory")
_DfrapPerfIcmpTotalRxAddrMaskRep_Type = Counter32
_DfrapPerfIcmpTotalRxAddrMaskRep_Object = MibTableColumn
dfrapPerfIcmpTotalRxAddrMaskRep = _DfrapPerfIcmpTotalRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 25),
    _DfrapPerfIcmpTotalRxAddrMaskRep_Type()
)
dfrapPerfIcmpTotalRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxAddrMaskRep.setStatus("mandatory")
_DfrapPerfIcmpTotalTxAddrMaskRep_Type = Counter32
_DfrapPerfIcmpTotalTxAddrMaskRep_Object = MibTableColumn
dfrapPerfIcmpTotalTxAddrMaskRep = _DfrapPerfIcmpTotalTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 26),
    _DfrapPerfIcmpTotalTxAddrMaskRep_Type()
)
dfrapPerfIcmpTotalTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxAddrMaskRep.setStatus("mandatory")
_DfrapPerfIcmpTotalRxPktTooBig_Type = Counter32
_DfrapPerfIcmpTotalRxPktTooBig_Object = MibTableColumn
dfrapPerfIcmpTotalRxPktTooBig = _DfrapPerfIcmpTotalRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 27),
    _DfrapPerfIcmpTotalRxPktTooBig_Type()
)
dfrapPerfIcmpTotalRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxPktTooBig.setStatus("mandatory")
_DfrapPerfIcmpTotalTxPktTooBig_Type = Counter32
_DfrapPerfIcmpTotalTxPktTooBig_Object = MibTableColumn
dfrapPerfIcmpTotalTxPktTooBig = _DfrapPerfIcmpTotalTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 28),
    _DfrapPerfIcmpTotalTxPktTooBig_Type()
)
dfrapPerfIcmpTotalTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxPktTooBig.setStatus("mandatory")
_DfrapPerfIcmpTotalRxGmQuery_Type = Counter32
_DfrapPerfIcmpTotalRxGmQuery_Object = MibTableColumn
dfrapPerfIcmpTotalRxGmQuery = _DfrapPerfIcmpTotalRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 29),
    _DfrapPerfIcmpTotalRxGmQuery_Type()
)
dfrapPerfIcmpTotalRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxGmQuery.setStatus("mandatory")
_DfrapPerfIcmpTotalTxGmQuery_Type = Counter32
_DfrapPerfIcmpTotalTxGmQuery_Object = MibTableColumn
dfrapPerfIcmpTotalTxGmQuery = _DfrapPerfIcmpTotalTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 30),
    _DfrapPerfIcmpTotalTxGmQuery_Type()
)
dfrapPerfIcmpTotalTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxGmQuery.setStatus("mandatory")
_DfrapPerfIcmpTotalRxGmReport_Type = Counter32
_DfrapPerfIcmpTotalRxGmReport_Object = MibTableColumn
dfrapPerfIcmpTotalRxGmReport = _DfrapPerfIcmpTotalRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 31),
    _DfrapPerfIcmpTotalRxGmReport_Type()
)
dfrapPerfIcmpTotalRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxGmReport.setStatus("mandatory")
_DfrapPerfIcmpTotalTxGmReport_Type = Counter32
_DfrapPerfIcmpTotalTxGmReport_Object = MibTableColumn
dfrapPerfIcmpTotalTxGmReport = _DfrapPerfIcmpTotalTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 32),
    _DfrapPerfIcmpTotalTxGmReport_Type()
)
dfrapPerfIcmpTotalTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxGmReport.setStatus("mandatory")
_DfrapPerfIcmpTotalRxGmReduct_Type = Counter32
_DfrapPerfIcmpTotalRxGmReduct_Object = MibTableColumn
dfrapPerfIcmpTotalRxGmReduct = _DfrapPerfIcmpTotalRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 33),
    _DfrapPerfIcmpTotalRxGmReduct_Type()
)
dfrapPerfIcmpTotalRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalRxGmReduct.setStatus("mandatory")
_DfrapPerfIcmpTotalTxGmReduct_Type = Counter32
_DfrapPerfIcmpTotalTxGmReduct_Object = MibTableColumn
dfrapPerfIcmpTotalTxGmReduct = _DfrapPerfIcmpTotalTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 6, 1, 34),
    _DfrapPerfIcmpTotalTxGmReduct_Type()
)
dfrapPerfIcmpTotalTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIcmpTotalTxGmReduct.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTable_Object = MibTable
dfrapPerfApplicationPerDlciTable = _DfrapPerfApplicationPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7)
)
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTable.setStatus("mandatory")
_DfrapPerfApplicationPerDlciEntry_Object = MibTableRow
dfrapPerfApplicationPerDlciEntry = _DfrapPerfApplicationPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1)
)
dfrapPerfApplicationPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfApplicationPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfApplicationPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciEntry.setStatus("mandatory")


class _DfrapPerfApplicationPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfApplicationPerDlciInterval based on Integer32"""
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


_DfrapPerfApplicationPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfApplicationPerDlciInterval_Object = MibTableColumn
dfrapPerfApplicationPerDlciInterval = _DfrapPerfApplicationPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 1),
    _DfrapPerfApplicationPerDlciInterval_Type()
)
dfrapPerfApplicationPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciInterval.setStatus("mandatory")
_DfrapPerfApplicationPerDlciValue_Type = Integer32
_DfrapPerfApplicationPerDlciValue_Object = MibTableColumn
dfrapPerfApplicationPerDlciValue = _DfrapPerfApplicationPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 2),
    _DfrapPerfApplicationPerDlciValue_Type()
)
dfrapPerfApplicationPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciValue.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxSnmp_Type = Counter32
_DfrapPerfApplicationPerDlciRxSnmp_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxSnmp = _DfrapPerfApplicationPerDlciRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 3),
    _DfrapPerfApplicationPerDlciRxSnmp_Type()
)
dfrapPerfApplicationPerDlciRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxSnmp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxSnmp_Type = Counter32
_DfrapPerfApplicationPerDlciTxSnmp_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxSnmp = _DfrapPerfApplicationPerDlciTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 4),
    _DfrapPerfApplicationPerDlciTxSnmp_Type()
)
dfrapPerfApplicationPerDlciTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxSnmp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxSnmpTrap_Type = Counter32
_DfrapPerfApplicationPerDlciRxSnmpTrap_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxSnmpTrap = _DfrapPerfApplicationPerDlciRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 5),
    _DfrapPerfApplicationPerDlciRxSnmpTrap_Type()
)
dfrapPerfApplicationPerDlciRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxSnmpTrap.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxSnmpTrap_Type = Counter32
_DfrapPerfApplicationPerDlciTxSnmpTrap_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxSnmpTrap = _DfrapPerfApplicationPerDlciTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 6),
    _DfrapPerfApplicationPerDlciTxSnmpTrap_Type()
)
dfrapPerfApplicationPerDlciTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxSnmpTrap.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxHttp_Type = Counter32
_DfrapPerfApplicationPerDlciRxHttp_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxHttp = _DfrapPerfApplicationPerDlciRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 7),
    _DfrapPerfApplicationPerDlciRxHttp_Type()
)
dfrapPerfApplicationPerDlciRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxHttp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxHttp_Type = Counter32
_DfrapPerfApplicationPerDlciTxHttp_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxHttp = _DfrapPerfApplicationPerDlciTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 8),
    _DfrapPerfApplicationPerDlciTxHttp_Type()
)
dfrapPerfApplicationPerDlciTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxHttp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxTelnet_Type = Counter32
_DfrapPerfApplicationPerDlciRxTelnet_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxTelnet = _DfrapPerfApplicationPerDlciRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 9),
    _DfrapPerfApplicationPerDlciRxTelnet_Type()
)
dfrapPerfApplicationPerDlciRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxTelnet.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxTelnet_Type = Counter32
_DfrapPerfApplicationPerDlciTxTelnet_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxTelnet = _DfrapPerfApplicationPerDlciTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 10),
    _DfrapPerfApplicationPerDlciTxTelnet_Type()
)
dfrapPerfApplicationPerDlciTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxTelnet.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxSmtp_Type = Counter32
_DfrapPerfApplicationPerDlciRxSmtp_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxSmtp = _DfrapPerfApplicationPerDlciRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 11),
    _DfrapPerfApplicationPerDlciRxSmtp_Type()
)
dfrapPerfApplicationPerDlciRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxSmtp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxSmtp_Type = Counter32
_DfrapPerfApplicationPerDlciTxSmtp_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxSmtp = _DfrapPerfApplicationPerDlciTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 12),
    _DfrapPerfApplicationPerDlciTxSmtp_Type()
)
dfrapPerfApplicationPerDlciTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxSmtp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxFtp_Type = Counter32
_DfrapPerfApplicationPerDlciRxFtp_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxFtp = _DfrapPerfApplicationPerDlciRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 13),
    _DfrapPerfApplicationPerDlciRxFtp_Type()
)
dfrapPerfApplicationPerDlciRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxFtp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxFtp_Type = Counter32
_DfrapPerfApplicationPerDlciTxFtp_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxFtp = _DfrapPerfApplicationPerDlciTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 14),
    _DfrapPerfApplicationPerDlciTxFtp_Type()
)
dfrapPerfApplicationPerDlciTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxFtp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxTftp_Type = Counter32
_DfrapPerfApplicationPerDlciRxTftp_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxTftp = _DfrapPerfApplicationPerDlciRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 15),
    _DfrapPerfApplicationPerDlciRxTftp_Type()
)
dfrapPerfApplicationPerDlciRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxTftp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxTftp_Type = Counter32
_DfrapPerfApplicationPerDlciTxTftp_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxTftp = _DfrapPerfApplicationPerDlciTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 16),
    _DfrapPerfApplicationPerDlciTxTftp_Type()
)
dfrapPerfApplicationPerDlciTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxTftp.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxCustom1_Type = Counter32
_DfrapPerfApplicationPerDlciRxCustom1_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxCustom1 = _DfrapPerfApplicationPerDlciRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 17),
    _DfrapPerfApplicationPerDlciRxCustom1_Type()
)
dfrapPerfApplicationPerDlciRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxCustom1.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxCustom1_Type = Counter32
_DfrapPerfApplicationPerDlciTxCustom1_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxCustom1 = _DfrapPerfApplicationPerDlciTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 18),
    _DfrapPerfApplicationPerDlciTxCustom1_Type()
)
dfrapPerfApplicationPerDlciTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxCustom1.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxCustom2_Type = Counter32
_DfrapPerfApplicationPerDlciRxCustom2_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxCustom2 = _DfrapPerfApplicationPerDlciRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 19),
    _DfrapPerfApplicationPerDlciRxCustom2_Type()
)
dfrapPerfApplicationPerDlciRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxCustom2.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxCustom2_Type = Counter32
_DfrapPerfApplicationPerDlciTxCustom2_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxCustom2 = _DfrapPerfApplicationPerDlciTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 20),
    _DfrapPerfApplicationPerDlciTxCustom2_Type()
)
dfrapPerfApplicationPerDlciTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxCustom2.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxCustom3_Type = Counter32
_DfrapPerfApplicationPerDlciRxCustom3_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxCustom3 = _DfrapPerfApplicationPerDlciRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 21),
    _DfrapPerfApplicationPerDlciRxCustom3_Type()
)
dfrapPerfApplicationPerDlciRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxCustom3.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxCustom3_Type = Counter32
_DfrapPerfApplicationPerDlciTxCustom3_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxCustom3 = _DfrapPerfApplicationPerDlciTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 22),
    _DfrapPerfApplicationPerDlciTxCustom3_Type()
)
dfrapPerfApplicationPerDlciTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxCustom3.setStatus("mandatory")
_DfrapPerfApplicationPerDlciRxCustom4_Type = Counter32
_DfrapPerfApplicationPerDlciRxCustom4_Object = MibTableColumn
dfrapPerfApplicationPerDlciRxCustom4 = _DfrapPerfApplicationPerDlciRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 23),
    _DfrapPerfApplicationPerDlciRxCustom4_Type()
)
dfrapPerfApplicationPerDlciRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciRxCustom4.setStatus("mandatory")
_DfrapPerfApplicationPerDlciTxCustom4_Type = Counter32
_DfrapPerfApplicationPerDlciTxCustom4_Object = MibTableColumn
dfrapPerfApplicationPerDlciTxCustom4 = _DfrapPerfApplicationPerDlciTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 7, 1, 24),
    _DfrapPerfApplicationPerDlciTxCustom4_Type()
)
dfrapPerfApplicationPerDlciTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationPerDlciTxCustom4.setStatus("mandatory")
_DfrapPerfApplicationTotalTable_Object = MibTable
dfrapPerfApplicationTotalTable = _DfrapPerfApplicationTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8)
)
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTable.setStatus("mandatory")
_DfrapPerfApplicationTotalEntry_Object = MibTableRow
dfrapPerfApplicationTotalEntry = _DfrapPerfApplicationTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1)
)
dfrapPerfApplicationTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfApplicationTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalEntry.setStatus("mandatory")


class _DfrapPerfApplicationTotalInterval_Type(Integer32):
    """Custom type dfrapPerfApplicationTotalInterval based on Integer32"""
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


_DfrapPerfApplicationTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfApplicationTotalInterval_Object = MibTableColumn
dfrapPerfApplicationTotalInterval = _DfrapPerfApplicationTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 1),
    _DfrapPerfApplicationTotalInterval_Type()
)
dfrapPerfApplicationTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalInterval.setStatus("mandatory")
_DfrapPerfApplicationTotalRxSnmp_Type = Counter32
_DfrapPerfApplicationTotalRxSnmp_Object = MibTableColumn
dfrapPerfApplicationTotalRxSnmp = _DfrapPerfApplicationTotalRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 3),
    _DfrapPerfApplicationTotalRxSnmp_Type()
)
dfrapPerfApplicationTotalRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxSnmp.setStatus("mandatory")
_DfrapPerfApplicationTotalTxSnmp_Type = Counter32
_DfrapPerfApplicationTotalTxSnmp_Object = MibTableColumn
dfrapPerfApplicationTotalTxSnmp = _DfrapPerfApplicationTotalTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 4),
    _DfrapPerfApplicationTotalTxSnmp_Type()
)
dfrapPerfApplicationTotalTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxSnmp.setStatus("mandatory")
_DfrapPerfApplicationTotalRxSnmpTrap_Type = Counter32
_DfrapPerfApplicationTotalRxSnmpTrap_Object = MibTableColumn
dfrapPerfApplicationTotalRxSnmpTrap = _DfrapPerfApplicationTotalRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 5),
    _DfrapPerfApplicationTotalRxSnmpTrap_Type()
)
dfrapPerfApplicationTotalRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxSnmpTrap.setStatus("mandatory")
_DfrapPerfApplicationTotalTxSnmpTrap_Type = Counter32
_DfrapPerfApplicationTotalTxSnmpTrap_Object = MibTableColumn
dfrapPerfApplicationTotalTxSnmpTrap = _DfrapPerfApplicationTotalTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 6),
    _DfrapPerfApplicationTotalTxSnmpTrap_Type()
)
dfrapPerfApplicationTotalTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxSnmpTrap.setStatus("mandatory")
_DfrapPerfApplicationTotalRxHttp_Type = Counter32
_DfrapPerfApplicationTotalRxHttp_Object = MibTableColumn
dfrapPerfApplicationTotalRxHttp = _DfrapPerfApplicationTotalRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 7),
    _DfrapPerfApplicationTotalRxHttp_Type()
)
dfrapPerfApplicationTotalRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxHttp.setStatus("mandatory")
_DfrapPerfApplicationTotalTxHttp_Type = Counter32
_DfrapPerfApplicationTotalTxHttp_Object = MibTableColumn
dfrapPerfApplicationTotalTxHttp = _DfrapPerfApplicationTotalTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 8),
    _DfrapPerfApplicationTotalTxHttp_Type()
)
dfrapPerfApplicationTotalTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxHttp.setStatus("mandatory")
_DfrapPerfApplicationTotalRxTelnet_Type = Counter32
_DfrapPerfApplicationTotalRxTelnet_Object = MibTableColumn
dfrapPerfApplicationTotalRxTelnet = _DfrapPerfApplicationTotalRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 9),
    _DfrapPerfApplicationTotalRxTelnet_Type()
)
dfrapPerfApplicationTotalRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxTelnet.setStatus("mandatory")
_DfrapPerfApplicationTotalTxTelnet_Type = Counter32
_DfrapPerfApplicationTotalTxTelnet_Object = MibTableColumn
dfrapPerfApplicationTotalTxTelnet = _DfrapPerfApplicationTotalTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 10),
    _DfrapPerfApplicationTotalTxTelnet_Type()
)
dfrapPerfApplicationTotalTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxTelnet.setStatus("mandatory")
_DfrapPerfApplicationTotalRxSmtp_Type = Counter32
_DfrapPerfApplicationTotalRxSmtp_Object = MibTableColumn
dfrapPerfApplicationTotalRxSmtp = _DfrapPerfApplicationTotalRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 11),
    _DfrapPerfApplicationTotalRxSmtp_Type()
)
dfrapPerfApplicationTotalRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxSmtp.setStatus("mandatory")
_DfrapPerfApplicationTotalTxSmtp_Type = Counter32
_DfrapPerfApplicationTotalTxSmtp_Object = MibTableColumn
dfrapPerfApplicationTotalTxSmtp = _DfrapPerfApplicationTotalTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 12),
    _DfrapPerfApplicationTotalTxSmtp_Type()
)
dfrapPerfApplicationTotalTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxSmtp.setStatus("mandatory")
_DfrapPerfApplicationTotalRxFtp_Type = Counter32
_DfrapPerfApplicationTotalRxFtp_Object = MibTableColumn
dfrapPerfApplicationTotalRxFtp = _DfrapPerfApplicationTotalRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 13),
    _DfrapPerfApplicationTotalRxFtp_Type()
)
dfrapPerfApplicationTotalRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxFtp.setStatus("mandatory")
_DfrapPerfApplicationTotalTxFtp_Type = Counter32
_DfrapPerfApplicationTotalTxFtp_Object = MibTableColumn
dfrapPerfApplicationTotalTxFtp = _DfrapPerfApplicationTotalTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 14),
    _DfrapPerfApplicationTotalTxFtp_Type()
)
dfrapPerfApplicationTotalTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxFtp.setStatus("mandatory")
_DfrapPerfApplicationTotalRxTftp_Type = Counter32
_DfrapPerfApplicationTotalRxTftp_Object = MibTableColumn
dfrapPerfApplicationTotalRxTftp = _DfrapPerfApplicationTotalRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 15),
    _DfrapPerfApplicationTotalRxTftp_Type()
)
dfrapPerfApplicationTotalRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxTftp.setStatus("mandatory")
_DfrapPerfApplicationTotalTxTftp_Type = Counter32
_DfrapPerfApplicationTotalTxTftp_Object = MibTableColumn
dfrapPerfApplicationTotalTxTftp = _DfrapPerfApplicationTotalTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 16),
    _DfrapPerfApplicationTotalTxTftp_Type()
)
dfrapPerfApplicationTotalTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxTftp.setStatus("mandatory")
_DfrapPerfApplicationTotalRxCustom1_Type = Counter32
_DfrapPerfApplicationTotalRxCustom1_Object = MibTableColumn
dfrapPerfApplicationTotalRxCustom1 = _DfrapPerfApplicationTotalRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 17),
    _DfrapPerfApplicationTotalRxCustom1_Type()
)
dfrapPerfApplicationTotalRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxCustom1.setStatus("mandatory")
_DfrapPerfApplicationTotalTxCustom1_Type = Counter32
_DfrapPerfApplicationTotalTxCustom1_Object = MibTableColumn
dfrapPerfApplicationTotalTxCustom1 = _DfrapPerfApplicationTotalTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 18),
    _DfrapPerfApplicationTotalTxCustom1_Type()
)
dfrapPerfApplicationTotalTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxCustom1.setStatus("mandatory")
_DfrapPerfApplicationTotalRxCustom2_Type = Counter32
_DfrapPerfApplicationTotalRxCustom2_Object = MibTableColumn
dfrapPerfApplicationTotalRxCustom2 = _DfrapPerfApplicationTotalRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 19),
    _DfrapPerfApplicationTotalRxCustom2_Type()
)
dfrapPerfApplicationTotalRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxCustom2.setStatus("mandatory")
_DfrapPerfApplicationTotalTxCustom2_Type = Counter32
_DfrapPerfApplicationTotalTxCustom2_Object = MibTableColumn
dfrapPerfApplicationTotalTxCustom2 = _DfrapPerfApplicationTotalTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 20),
    _DfrapPerfApplicationTotalTxCustom2_Type()
)
dfrapPerfApplicationTotalTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxCustom2.setStatus("mandatory")
_DfrapPerfApplicationTotalRxCustom3_Type = Counter32
_DfrapPerfApplicationTotalRxCustom3_Object = MibTableColumn
dfrapPerfApplicationTotalRxCustom3 = _DfrapPerfApplicationTotalRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 21),
    _DfrapPerfApplicationTotalRxCustom3_Type()
)
dfrapPerfApplicationTotalRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxCustom3.setStatus("mandatory")
_DfrapPerfApplicationTotalTxCustom3_Type = Counter32
_DfrapPerfApplicationTotalTxCustom3_Object = MibTableColumn
dfrapPerfApplicationTotalTxCustom3 = _DfrapPerfApplicationTotalTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 22),
    _DfrapPerfApplicationTotalTxCustom3_Type()
)
dfrapPerfApplicationTotalTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxCustom3.setStatus("mandatory")
_DfrapPerfApplicationTotalRxCustom4_Type = Counter32
_DfrapPerfApplicationTotalRxCustom4_Object = MibTableColumn
dfrapPerfApplicationTotalRxCustom4 = _DfrapPerfApplicationTotalRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 23),
    _DfrapPerfApplicationTotalRxCustom4_Type()
)
dfrapPerfApplicationTotalRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalRxCustom4.setStatus("mandatory")
_DfrapPerfApplicationTotalTxCustom4_Type = Counter32
_DfrapPerfApplicationTotalTxCustom4_Object = MibTableColumn
dfrapPerfApplicationTotalTxCustom4 = _DfrapPerfApplicationTotalTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 8, 1, 24),
    _DfrapPerfApplicationTotalTxCustom4_Type()
)
dfrapPerfApplicationTotalTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfApplicationTotalTxCustom4.setStatus("mandatory")
_DfrapPerfRoutingPerDlciTable_Object = MibTable
dfrapPerfRoutingPerDlciTable = _DfrapPerfRoutingPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9)
)
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciTable.setStatus("mandatory")
_DfrapPerfRoutingPerDlciEntry_Object = MibTableRow
dfrapPerfRoutingPerDlciEntry = _DfrapPerfRoutingPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1)
)
dfrapPerfRoutingPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfRoutingPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfRoutingPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciEntry.setStatus("mandatory")


class _DfrapPerfRoutingPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfRoutingPerDlciInterval based on Integer32"""
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


_DfrapPerfRoutingPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfRoutingPerDlciInterval_Object = MibTableColumn
dfrapPerfRoutingPerDlciInterval = _DfrapPerfRoutingPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 1),
    _DfrapPerfRoutingPerDlciInterval_Type()
)
dfrapPerfRoutingPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciInterval.setStatus("mandatory")
_DfrapPerfRoutingPerDlciValue_Type = Integer32
_DfrapPerfRoutingPerDlciValue_Object = MibTableColumn
dfrapPerfRoutingPerDlciValue = _DfrapPerfRoutingPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 2),
    _DfrapPerfRoutingPerDlciValue_Type()
)
dfrapPerfRoutingPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciValue.setStatus("mandatory")
_DfrapPerfRoutingPerDlciRxOspf_Type = Counter32
_DfrapPerfRoutingPerDlciRxOspf_Object = MibTableColumn
dfrapPerfRoutingPerDlciRxOspf = _DfrapPerfRoutingPerDlciRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 3),
    _DfrapPerfRoutingPerDlciRxOspf_Type()
)
dfrapPerfRoutingPerDlciRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciRxOspf.setStatus("mandatory")
_DfrapPerfRoutingPerDlciTxOspf_Type = Counter32
_DfrapPerfRoutingPerDlciTxOspf_Object = MibTableColumn
dfrapPerfRoutingPerDlciTxOspf = _DfrapPerfRoutingPerDlciTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 4),
    _DfrapPerfRoutingPerDlciTxOspf_Type()
)
dfrapPerfRoutingPerDlciTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciTxOspf.setStatus("mandatory")
_DfrapPerfRoutingPerDlciRxRip_Type = Counter32
_DfrapPerfRoutingPerDlciRxRip_Object = MibTableColumn
dfrapPerfRoutingPerDlciRxRip = _DfrapPerfRoutingPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 5),
    _DfrapPerfRoutingPerDlciRxRip_Type()
)
dfrapPerfRoutingPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciRxRip.setStatus("mandatory")
_DfrapPerfRoutingPerDlciTxRip_Type = Counter32
_DfrapPerfRoutingPerDlciTxRip_Object = MibTableColumn
dfrapPerfRoutingPerDlciTxRip = _DfrapPerfRoutingPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 6),
    _DfrapPerfRoutingPerDlciTxRip_Type()
)
dfrapPerfRoutingPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciTxRip.setStatus("mandatory")
_DfrapPerfRoutingPerDlciRxNetbios_Type = Counter32
_DfrapPerfRoutingPerDlciRxNetbios_Object = MibTableColumn
dfrapPerfRoutingPerDlciRxNetbios = _DfrapPerfRoutingPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 7),
    _DfrapPerfRoutingPerDlciRxNetbios_Type()
)
dfrapPerfRoutingPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciRxNetbios.setStatus("mandatory")
_DfrapPerfRoutingPerDlciTxNetbios_Type = Counter32
_DfrapPerfRoutingPerDlciTxNetbios_Object = MibTableColumn
dfrapPerfRoutingPerDlciTxNetbios = _DfrapPerfRoutingPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 9, 1, 8),
    _DfrapPerfRoutingPerDlciTxNetbios_Type()
)
dfrapPerfRoutingPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingPerDlciTxNetbios.setStatus("mandatory")
_DfrapPerfRoutingTotalTable_Object = MibTable
dfrapPerfRoutingTotalTable = _DfrapPerfRoutingTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10)
)
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalTable.setStatus("mandatory")
_DfrapPerfRoutingTotalEntry_Object = MibTableRow
dfrapPerfRoutingTotalEntry = _DfrapPerfRoutingTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1)
)
dfrapPerfRoutingTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfRoutingTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalEntry.setStatus("mandatory")


class _DfrapPerfRoutingTotalInterval_Type(Integer32):
    """Custom type dfrapPerfRoutingTotalInterval based on Integer32"""
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


_DfrapPerfRoutingTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfRoutingTotalInterval_Object = MibTableColumn
dfrapPerfRoutingTotalInterval = _DfrapPerfRoutingTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 1),
    _DfrapPerfRoutingTotalInterval_Type()
)
dfrapPerfRoutingTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalInterval.setStatus("mandatory")
_DfrapPerfRoutingTotalRxOspf_Type = Counter32
_DfrapPerfRoutingTotalRxOspf_Object = MibTableColumn
dfrapPerfRoutingTotalRxOspf = _DfrapPerfRoutingTotalRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 3),
    _DfrapPerfRoutingTotalRxOspf_Type()
)
dfrapPerfRoutingTotalRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalRxOspf.setStatus("mandatory")
_DfrapPerfRoutingTotalTxOspf_Type = Counter32
_DfrapPerfRoutingTotalTxOspf_Object = MibTableColumn
dfrapPerfRoutingTotalTxOspf = _DfrapPerfRoutingTotalTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 4),
    _DfrapPerfRoutingTotalTxOspf_Type()
)
dfrapPerfRoutingTotalTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalTxOspf.setStatus("mandatory")
_DfrapPerfRoutingTotalRxRip_Type = Counter32
_DfrapPerfRoutingTotalRxRip_Object = MibTableColumn
dfrapPerfRoutingTotalRxRip = _DfrapPerfRoutingTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 5),
    _DfrapPerfRoutingTotalRxRip_Type()
)
dfrapPerfRoutingTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalRxRip.setStatus("mandatory")
_DfrapPerfRoutingTotalTxRip_Type = Counter32
_DfrapPerfRoutingTotalTxRip_Object = MibTableColumn
dfrapPerfRoutingTotalTxRip = _DfrapPerfRoutingTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 6),
    _DfrapPerfRoutingTotalTxRip_Type()
)
dfrapPerfRoutingTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalTxRip.setStatus("mandatory")
_DfrapPerfRoutingTotalRxNetbios_Type = Counter32
_DfrapPerfRoutingTotalRxNetbios_Object = MibTableColumn
dfrapPerfRoutingTotalRxNetbios = _DfrapPerfRoutingTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 7),
    _DfrapPerfRoutingTotalRxNetbios_Type()
)
dfrapPerfRoutingTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalRxNetbios.setStatus("mandatory")
_DfrapPerfRoutingTotalTxNetbios_Type = Counter32
_DfrapPerfRoutingTotalTxNetbios_Object = MibTableColumn
dfrapPerfRoutingTotalTxNetbios = _DfrapPerfRoutingTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 10, 1, 8),
    _DfrapPerfRoutingTotalTxNetbios_Type()
)
dfrapPerfRoutingTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfRoutingTotalTxNetbios.setStatus("mandatory")
_DfrapPerfIpxPerDlciTable_Object = MibTable
dfrapPerfIpxPerDlciTable = _DfrapPerfIpxPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11)
)
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTable.setStatus("mandatory")
_DfrapPerfIpxPerDlciEntry_Object = MibTableRow
dfrapPerfIpxPerDlciEntry = _DfrapPerfIpxPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1)
)
dfrapPerfIpxPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIpxPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfIpxPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciEntry.setStatus("mandatory")


class _DfrapPerfIpxPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfIpxPerDlciInterval based on Integer32"""
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


_DfrapPerfIpxPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfIpxPerDlciInterval_Object = MibTableColumn
dfrapPerfIpxPerDlciInterval = _DfrapPerfIpxPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 1),
    _DfrapPerfIpxPerDlciInterval_Type()
)
dfrapPerfIpxPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciInterval.setStatus("mandatory")
_DfrapPerfIpxPerDlciValue_Type = Integer32
_DfrapPerfIpxPerDlciValue_Object = MibTableColumn
dfrapPerfIpxPerDlciValue = _DfrapPerfIpxPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 2),
    _DfrapPerfIpxPerDlciValue_Type()
)
dfrapPerfIpxPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciValue.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxTotal_Type = Counter32
_DfrapPerfIpxPerDlciRxTotal_Object = MibTableColumn
dfrapPerfIpxPerDlciRxTotal = _DfrapPerfIpxPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 3),
    _DfrapPerfIpxPerDlciRxTotal_Type()
)
dfrapPerfIpxPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxTotal_Type = Counter32
_DfrapPerfIpxPerDlciTxTotal_Object = MibTableColumn
dfrapPerfIpxPerDlciTxTotal = _DfrapPerfIpxPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 4),
    _DfrapPerfIpxPerDlciTxTotal_Type()
)
dfrapPerfIpxPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxSpx_Type = Counter32
_DfrapPerfIpxPerDlciRxSpx_Object = MibTableColumn
dfrapPerfIpxPerDlciRxSpx = _DfrapPerfIpxPerDlciRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 5),
    _DfrapPerfIpxPerDlciRxSpx_Type()
)
dfrapPerfIpxPerDlciRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxSpx.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxSpx_Type = Counter32
_DfrapPerfIpxPerDlciTxSpx_Object = MibTableColumn
dfrapPerfIpxPerDlciTxSpx = _DfrapPerfIpxPerDlciTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 6),
    _DfrapPerfIpxPerDlciTxSpx_Type()
)
dfrapPerfIpxPerDlciTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxSpx.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxNcp_Type = Counter32
_DfrapPerfIpxPerDlciRxNcp_Object = MibTableColumn
dfrapPerfIpxPerDlciRxNcp = _DfrapPerfIpxPerDlciRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 7),
    _DfrapPerfIpxPerDlciRxNcp_Type()
)
dfrapPerfIpxPerDlciRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxNcp.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxNcp_Type = Counter32
_DfrapPerfIpxPerDlciTxNcp_Object = MibTableColumn
dfrapPerfIpxPerDlciTxNcp = _DfrapPerfIpxPerDlciTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 8),
    _DfrapPerfIpxPerDlciTxNcp_Type()
)
dfrapPerfIpxPerDlciTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxNcp.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxSap_Type = Counter32
_DfrapPerfIpxPerDlciRxSap_Object = MibTableColumn
dfrapPerfIpxPerDlciRxSap = _DfrapPerfIpxPerDlciRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 9),
    _DfrapPerfIpxPerDlciRxSap_Type()
)
dfrapPerfIpxPerDlciRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxSap.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxSap_Type = Counter32
_DfrapPerfIpxPerDlciTxSap_Object = MibTableColumn
dfrapPerfIpxPerDlciTxSap = _DfrapPerfIpxPerDlciTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 10),
    _DfrapPerfIpxPerDlciTxSap_Type()
)
dfrapPerfIpxPerDlciTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxSap.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxRip_Type = Counter32
_DfrapPerfIpxPerDlciRxRip_Object = MibTableColumn
dfrapPerfIpxPerDlciRxRip = _DfrapPerfIpxPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 11),
    _DfrapPerfIpxPerDlciRxRip_Type()
)
dfrapPerfIpxPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxRip.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxRip_Type = Counter32
_DfrapPerfIpxPerDlciTxRip_Object = MibTableColumn
dfrapPerfIpxPerDlciTxRip = _DfrapPerfIpxPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 12),
    _DfrapPerfIpxPerDlciTxRip_Type()
)
dfrapPerfIpxPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxRip.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxNetbios_Type = Counter32
_DfrapPerfIpxPerDlciRxNetbios_Object = MibTableColumn
dfrapPerfIpxPerDlciRxNetbios = _DfrapPerfIpxPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 13),
    _DfrapPerfIpxPerDlciRxNetbios_Type()
)
dfrapPerfIpxPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxNetbios.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxNetbios_Type = Counter32
_DfrapPerfIpxPerDlciTxNetbios_Object = MibTableColumn
dfrapPerfIpxPerDlciTxNetbios = _DfrapPerfIpxPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 14),
    _DfrapPerfIpxPerDlciTxNetbios_Type()
)
dfrapPerfIpxPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxNetbios.setStatus("mandatory")
_DfrapPerfIpxPerDlciRxOther_Type = Counter32
_DfrapPerfIpxPerDlciRxOther_Object = MibTableColumn
dfrapPerfIpxPerDlciRxOther = _DfrapPerfIpxPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 15),
    _DfrapPerfIpxPerDlciRxOther_Type()
)
dfrapPerfIpxPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciRxOther.setStatus("mandatory")
_DfrapPerfIpxPerDlciTxOther_Type = Counter32
_DfrapPerfIpxPerDlciTxOther_Object = MibTableColumn
dfrapPerfIpxPerDlciTxOther = _DfrapPerfIpxPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 11, 1, 16),
    _DfrapPerfIpxPerDlciTxOther_Type()
)
dfrapPerfIpxPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxPerDlciTxOther.setStatus("mandatory")
_DfrapPerfIpxTotalTable_Object = MibTable
dfrapPerfIpxTotalTable = _DfrapPerfIpxTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12)
)
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTable.setStatus("mandatory")
_DfrapPerfIpxTotalEntry_Object = MibTableRow
dfrapPerfIpxTotalEntry = _DfrapPerfIpxTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1)
)
dfrapPerfIpxTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfIpxTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalEntry.setStatus("mandatory")


class _DfrapPerfIpxTotalInterval_Type(Integer32):
    """Custom type dfrapPerfIpxTotalInterval based on Integer32"""
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


_DfrapPerfIpxTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfIpxTotalInterval_Object = MibTableColumn
dfrapPerfIpxTotalInterval = _DfrapPerfIpxTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 1),
    _DfrapPerfIpxTotalInterval_Type()
)
dfrapPerfIpxTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalInterval.setStatus("mandatory")
_DfrapPerfIpxTotalRxTotal_Type = Counter32
_DfrapPerfIpxTotalRxTotal_Object = MibTableColumn
dfrapPerfIpxTotalRxTotal = _DfrapPerfIpxTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 3),
    _DfrapPerfIpxTotalRxTotal_Type()
)
dfrapPerfIpxTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxTotal.setStatus("mandatory")
_DfrapPerfIpxTotalTxTotal_Type = Counter32
_DfrapPerfIpxTotalTxTotal_Object = MibTableColumn
dfrapPerfIpxTotalTxTotal = _DfrapPerfIpxTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 4),
    _DfrapPerfIpxTotalTxTotal_Type()
)
dfrapPerfIpxTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxTotal.setStatus("mandatory")
_DfrapPerfIpxTotalRxSpx_Type = Counter32
_DfrapPerfIpxTotalRxSpx_Object = MibTableColumn
dfrapPerfIpxTotalRxSpx = _DfrapPerfIpxTotalRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 5),
    _DfrapPerfIpxTotalRxSpx_Type()
)
dfrapPerfIpxTotalRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxSpx.setStatus("mandatory")
_DfrapPerfIpxTotalTxSpx_Type = Counter32
_DfrapPerfIpxTotalTxSpx_Object = MibTableColumn
dfrapPerfIpxTotalTxSpx = _DfrapPerfIpxTotalTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 6),
    _DfrapPerfIpxTotalTxSpx_Type()
)
dfrapPerfIpxTotalTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxSpx.setStatus("mandatory")
_DfrapPerfIpxTotalRxNcp_Type = Counter32
_DfrapPerfIpxTotalRxNcp_Object = MibTableColumn
dfrapPerfIpxTotalRxNcp = _DfrapPerfIpxTotalRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 7),
    _DfrapPerfIpxTotalRxNcp_Type()
)
dfrapPerfIpxTotalRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxNcp.setStatus("mandatory")
_DfrapPerfIpxTotalTxNcp_Type = Counter32
_DfrapPerfIpxTotalTxNcp_Object = MibTableColumn
dfrapPerfIpxTotalTxNcp = _DfrapPerfIpxTotalTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 8),
    _DfrapPerfIpxTotalTxNcp_Type()
)
dfrapPerfIpxTotalTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxNcp.setStatus("mandatory")
_DfrapPerfIpxTotalRxSap_Type = Counter32
_DfrapPerfIpxTotalRxSap_Object = MibTableColumn
dfrapPerfIpxTotalRxSap = _DfrapPerfIpxTotalRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 9),
    _DfrapPerfIpxTotalRxSap_Type()
)
dfrapPerfIpxTotalRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxSap.setStatus("mandatory")
_DfrapPerfIpxTotalTxSap_Type = Counter32
_DfrapPerfIpxTotalTxSap_Object = MibTableColumn
dfrapPerfIpxTotalTxSap = _DfrapPerfIpxTotalTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 10),
    _DfrapPerfIpxTotalTxSap_Type()
)
dfrapPerfIpxTotalTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxSap.setStatus("mandatory")
_DfrapPerfIpxTotalRxRip_Type = Counter32
_DfrapPerfIpxTotalRxRip_Object = MibTableColumn
dfrapPerfIpxTotalRxRip = _DfrapPerfIpxTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 11),
    _DfrapPerfIpxTotalRxRip_Type()
)
dfrapPerfIpxTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxRip.setStatus("mandatory")
_DfrapPerfIpxTotalTxRip_Type = Counter32
_DfrapPerfIpxTotalTxRip_Object = MibTableColumn
dfrapPerfIpxTotalTxRip = _DfrapPerfIpxTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 12),
    _DfrapPerfIpxTotalTxRip_Type()
)
dfrapPerfIpxTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxRip.setStatus("mandatory")
_DfrapPerfIpxTotalRxNetbios_Type = Counter32
_DfrapPerfIpxTotalRxNetbios_Object = MibTableColumn
dfrapPerfIpxTotalRxNetbios = _DfrapPerfIpxTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 13),
    _DfrapPerfIpxTotalRxNetbios_Type()
)
dfrapPerfIpxTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxNetbios.setStatus("mandatory")
_DfrapPerfIpxTotalTxNetbios_Type = Counter32
_DfrapPerfIpxTotalTxNetbios_Object = MibTableColumn
dfrapPerfIpxTotalTxNetbios = _DfrapPerfIpxTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 14),
    _DfrapPerfIpxTotalTxNetbios_Type()
)
dfrapPerfIpxTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxNetbios.setStatus("mandatory")
_DfrapPerfIpxTotalRxOther_Type = Counter32
_DfrapPerfIpxTotalRxOther_Object = MibTableColumn
dfrapPerfIpxTotalRxOther = _DfrapPerfIpxTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 15),
    _DfrapPerfIpxTotalRxOther_Type()
)
dfrapPerfIpxTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalRxOther.setStatus("mandatory")
_DfrapPerfIpxTotalTxOther_Type = Counter32
_DfrapPerfIpxTotalTxOther_Object = MibTableColumn
dfrapPerfIpxTotalTxOther = _DfrapPerfIpxTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 12, 1, 16),
    _DfrapPerfIpxTotalTxOther_Type()
)
dfrapPerfIpxTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfIpxTotalTxOther.setStatus("mandatory")
_DfrapPerfSnaPerDlciTable_Object = MibTable
dfrapPerfSnaPerDlciTable = _DfrapPerfSnaPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13)
)
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTable.setStatus("mandatory")
_DfrapPerfSnaPerDlciEntry_Object = MibTableRow
dfrapPerfSnaPerDlciEntry = _DfrapPerfSnaPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1)
)
dfrapPerfSnaPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfSnaPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfSnaPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciEntry.setStatus("mandatory")


class _DfrapPerfSnaPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfSnaPerDlciInterval based on Integer32"""
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


_DfrapPerfSnaPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfSnaPerDlciInterval_Object = MibTableColumn
dfrapPerfSnaPerDlciInterval = _DfrapPerfSnaPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 1),
    _DfrapPerfSnaPerDlciInterval_Type()
)
dfrapPerfSnaPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciInterval.setStatus("mandatory")
_DfrapPerfSnaPerDlciValue_Type = Integer32
_DfrapPerfSnaPerDlciValue_Object = MibTableColumn
dfrapPerfSnaPerDlciValue = _DfrapPerfSnaPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 2),
    _DfrapPerfSnaPerDlciValue_Type()
)
dfrapPerfSnaPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciValue.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxTotal_Type = Counter32
_DfrapPerfSnaPerDlciRxTotal_Object = MibTableColumn
dfrapPerfSnaPerDlciRxTotal = _DfrapPerfSnaPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 3),
    _DfrapPerfSnaPerDlciRxTotal_Type()
)
dfrapPerfSnaPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxTotal_Type = Counter32
_DfrapPerfSnaPerDlciTxTotal_Object = MibTableColumn
dfrapPerfSnaPerDlciTxTotal = _DfrapPerfSnaPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 4),
    _DfrapPerfSnaPerDlciTxTotal_Type()
)
dfrapPerfSnaPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxSubarea_Type = Counter32
_DfrapPerfSnaPerDlciRxSubarea_Object = MibTableColumn
dfrapPerfSnaPerDlciRxSubarea = _DfrapPerfSnaPerDlciRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 5),
    _DfrapPerfSnaPerDlciRxSubarea_Type()
)
dfrapPerfSnaPerDlciRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxSubarea.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxSubarea_Type = Counter32
_DfrapPerfSnaPerDlciTxSubarea_Object = MibTableColumn
dfrapPerfSnaPerDlciTxSubarea = _DfrapPerfSnaPerDlciTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 6),
    _DfrapPerfSnaPerDlciTxSubarea_Type()
)
dfrapPerfSnaPerDlciTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxSubarea.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxPeriph_Type = Counter32
_DfrapPerfSnaPerDlciRxPeriph_Object = MibTableColumn
dfrapPerfSnaPerDlciRxPeriph = _DfrapPerfSnaPerDlciRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 7),
    _DfrapPerfSnaPerDlciRxPeriph_Type()
)
dfrapPerfSnaPerDlciRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxPeriph.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxPeriph_Type = Counter32
_DfrapPerfSnaPerDlciTxPeriph_Object = MibTableColumn
dfrapPerfSnaPerDlciTxPeriph = _DfrapPerfSnaPerDlciTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 8),
    _DfrapPerfSnaPerDlciTxPeriph_Type()
)
dfrapPerfSnaPerDlciTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxPeriph.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxAppn_Type = Counter32
_DfrapPerfSnaPerDlciRxAppn_Object = MibTableColumn
dfrapPerfSnaPerDlciRxAppn = _DfrapPerfSnaPerDlciRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 9),
    _DfrapPerfSnaPerDlciRxAppn_Type()
)
dfrapPerfSnaPerDlciRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxAppn.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxAppn_Type = Counter32
_DfrapPerfSnaPerDlciTxAppn_Object = MibTableColumn
dfrapPerfSnaPerDlciTxAppn = _DfrapPerfSnaPerDlciTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 10),
    _DfrapPerfSnaPerDlciTxAppn_Type()
)
dfrapPerfSnaPerDlciTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxAppn.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxNetbios_Type = Counter32
_DfrapPerfSnaPerDlciRxNetbios_Object = MibTableColumn
dfrapPerfSnaPerDlciRxNetbios = _DfrapPerfSnaPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 11),
    _DfrapPerfSnaPerDlciRxNetbios_Type()
)
dfrapPerfSnaPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxNetbios.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxNetbios_Type = Counter32
_DfrapPerfSnaPerDlciTxNetbios_Object = MibTableColumn
dfrapPerfSnaPerDlciTxNetbios = _DfrapPerfSnaPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 12),
    _DfrapPerfSnaPerDlciTxNetbios_Type()
)
dfrapPerfSnaPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxNetbios.setStatus("mandatory")
_DfrapPerfSnaPerDlciRxOther_Type = Counter32
_DfrapPerfSnaPerDlciRxOther_Object = MibTableColumn
dfrapPerfSnaPerDlciRxOther = _DfrapPerfSnaPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 13),
    _DfrapPerfSnaPerDlciRxOther_Type()
)
dfrapPerfSnaPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciRxOther.setStatus("mandatory")
_DfrapPerfSnaPerDlciTxOther_Type = Counter32
_DfrapPerfSnaPerDlciTxOther_Object = MibTableColumn
dfrapPerfSnaPerDlciTxOther = _DfrapPerfSnaPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 13, 1, 14),
    _DfrapPerfSnaPerDlciTxOther_Type()
)
dfrapPerfSnaPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaPerDlciTxOther.setStatus("mandatory")
_DfrapPerfSnaTotalTable_Object = MibTable
dfrapPerfSnaTotalTable = _DfrapPerfSnaTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14)
)
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTable.setStatus("mandatory")
_DfrapPerfSnaTotalEntry_Object = MibTableRow
dfrapPerfSnaTotalEntry = _DfrapPerfSnaTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1)
)
dfrapPerfSnaTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfSnaTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalEntry.setStatus("mandatory")


class _DfrapPerfSnaTotalInterval_Type(Integer32):
    """Custom type dfrapPerfSnaTotalInterval based on Integer32"""
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


_DfrapPerfSnaTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfSnaTotalInterval_Object = MibTableColumn
dfrapPerfSnaTotalInterval = _DfrapPerfSnaTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 1),
    _DfrapPerfSnaTotalInterval_Type()
)
dfrapPerfSnaTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalInterval.setStatus("mandatory")
_DfrapPerfSnaTotalRxTotal_Type = Counter32
_DfrapPerfSnaTotalRxTotal_Object = MibTableColumn
dfrapPerfSnaTotalRxTotal = _DfrapPerfSnaTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 3),
    _DfrapPerfSnaTotalRxTotal_Type()
)
dfrapPerfSnaTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxTotal.setStatus("mandatory")
_DfrapPerfSnaTotalTxTotal_Type = Counter32
_DfrapPerfSnaTotalTxTotal_Object = MibTableColumn
dfrapPerfSnaTotalTxTotal = _DfrapPerfSnaTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 4),
    _DfrapPerfSnaTotalTxTotal_Type()
)
dfrapPerfSnaTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxTotal.setStatus("mandatory")
_DfrapPerfSnaTotalRxSubarea_Type = Counter32
_DfrapPerfSnaTotalRxSubarea_Object = MibTableColumn
dfrapPerfSnaTotalRxSubarea = _DfrapPerfSnaTotalRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 5),
    _DfrapPerfSnaTotalRxSubarea_Type()
)
dfrapPerfSnaTotalRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxSubarea.setStatus("mandatory")
_DfrapPerfSnaTotalTxSubarea_Type = Counter32
_DfrapPerfSnaTotalTxSubarea_Object = MibTableColumn
dfrapPerfSnaTotalTxSubarea = _DfrapPerfSnaTotalTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 6),
    _DfrapPerfSnaTotalTxSubarea_Type()
)
dfrapPerfSnaTotalTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxSubarea.setStatus("mandatory")
_DfrapPerfSnaTotalRxPeriph_Type = Counter32
_DfrapPerfSnaTotalRxPeriph_Object = MibTableColumn
dfrapPerfSnaTotalRxPeriph = _DfrapPerfSnaTotalRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 7),
    _DfrapPerfSnaTotalRxPeriph_Type()
)
dfrapPerfSnaTotalRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxPeriph.setStatus("mandatory")
_DfrapPerfSnaTotalTxPeriph_Type = Counter32
_DfrapPerfSnaTotalTxPeriph_Object = MibTableColumn
dfrapPerfSnaTotalTxPeriph = _DfrapPerfSnaTotalTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 8),
    _DfrapPerfSnaTotalTxPeriph_Type()
)
dfrapPerfSnaTotalTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxPeriph.setStatus("mandatory")
_DfrapPerfSnaTotalRxAppn_Type = Counter32
_DfrapPerfSnaTotalRxAppn_Object = MibTableColumn
dfrapPerfSnaTotalRxAppn = _DfrapPerfSnaTotalRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 9),
    _DfrapPerfSnaTotalRxAppn_Type()
)
dfrapPerfSnaTotalRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxAppn.setStatus("mandatory")
_DfrapPerfSnaTotalTxAppn_Type = Counter32
_DfrapPerfSnaTotalTxAppn_Object = MibTableColumn
dfrapPerfSnaTotalTxAppn = _DfrapPerfSnaTotalTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 10),
    _DfrapPerfSnaTotalTxAppn_Type()
)
dfrapPerfSnaTotalTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxAppn.setStatus("mandatory")
_DfrapPerfSnaTotalRxNetbios_Type = Counter32
_DfrapPerfSnaTotalRxNetbios_Object = MibTableColumn
dfrapPerfSnaTotalRxNetbios = _DfrapPerfSnaTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 11),
    _DfrapPerfSnaTotalRxNetbios_Type()
)
dfrapPerfSnaTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxNetbios.setStatus("mandatory")
_DfrapPerfSnaTotalTxNetbios_Type = Counter32
_DfrapPerfSnaTotalTxNetbios_Object = MibTableColumn
dfrapPerfSnaTotalTxNetbios = _DfrapPerfSnaTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 12),
    _DfrapPerfSnaTotalTxNetbios_Type()
)
dfrapPerfSnaTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxNetbios.setStatus("mandatory")
_DfrapPerfSnaTotalRxOther_Type = Counter32
_DfrapPerfSnaTotalRxOther_Object = MibTableColumn
dfrapPerfSnaTotalRxOther = _DfrapPerfSnaTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 13),
    _DfrapPerfSnaTotalRxOther_Type()
)
dfrapPerfSnaTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalRxOther.setStatus("mandatory")
_DfrapPerfSnaTotalTxOther_Type = Counter32
_DfrapPerfSnaTotalTxOther_Object = MibTableColumn
dfrapPerfSnaTotalTxOther = _DfrapPerfSnaTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 14, 1, 14),
    _DfrapPerfSnaTotalTxOther_Type()
)
dfrapPerfSnaTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfSnaTotalTxOther.setStatus("mandatory")
_DfrapPerfArpPerDlciTable_Object = MibTable
dfrapPerfArpPerDlciTable = _DfrapPerfArpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15)
)
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTable.setStatus("mandatory")
_DfrapPerfArpPerDlciEntry_Object = MibTableRow
dfrapPerfArpPerDlciEntry = _DfrapPerfArpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1)
)
dfrapPerfArpPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfArpPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfArpPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciEntry.setStatus("mandatory")


class _DfrapPerfArpPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfArpPerDlciInterval based on Integer32"""
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


_DfrapPerfArpPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfArpPerDlciInterval_Object = MibTableColumn
dfrapPerfArpPerDlciInterval = _DfrapPerfArpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 1),
    _DfrapPerfArpPerDlciInterval_Type()
)
dfrapPerfArpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciInterval.setStatus("mandatory")
_DfrapPerfArpPerDlciValue_Type = Integer32
_DfrapPerfArpPerDlciValue_Object = MibTableColumn
dfrapPerfArpPerDlciValue = _DfrapPerfArpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 2),
    _DfrapPerfArpPerDlciValue_Type()
)
dfrapPerfArpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciValue.setStatus("mandatory")
_DfrapPerfArpPerDlciRxTotal_Type = Counter32
_DfrapPerfArpPerDlciRxTotal_Object = MibTableColumn
dfrapPerfArpPerDlciRxTotal = _DfrapPerfArpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 3),
    _DfrapPerfArpPerDlciRxTotal_Type()
)
dfrapPerfArpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxTotal.setStatus("mandatory")
_DfrapPerfArpPerDlciTxTotal_Type = Counter32
_DfrapPerfArpPerDlciTxTotal_Object = MibTableColumn
dfrapPerfArpPerDlciTxTotal = _DfrapPerfArpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 4),
    _DfrapPerfArpPerDlciTxTotal_Type()
)
dfrapPerfArpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxTotal.setStatus("mandatory")
_DfrapPerfArpPerDlciRxArpReq_Type = Counter32
_DfrapPerfArpPerDlciRxArpReq_Object = MibTableColumn
dfrapPerfArpPerDlciRxArpReq = _DfrapPerfArpPerDlciRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 5),
    _DfrapPerfArpPerDlciRxArpReq_Type()
)
dfrapPerfArpPerDlciRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxArpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciTxArpReq_Type = Counter32
_DfrapPerfArpPerDlciTxArpReq_Object = MibTableColumn
dfrapPerfArpPerDlciTxArpReq = _DfrapPerfArpPerDlciTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 6),
    _DfrapPerfArpPerDlciTxArpReq_Type()
)
dfrapPerfArpPerDlciTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxArpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciRxArpRep_Type = Counter32
_DfrapPerfArpPerDlciRxArpRep_Object = MibTableColumn
dfrapPerfArpPerDlciRxArpRep = _DfrapPerfArpPerDlciRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 7),
    _DfrapPerfArpPerDlciRxArpRep_Type()
)
dfrapPerfArpPerDlciRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxArpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciTxArpRep_Type = Counter32
_DfrapPerfArpPerDlciTxArpRep_Object = MibTableColumn
dfrapPerfArpPerDlciTxArpRep = _DfrapPerfArpPerDlciTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 8),
    _DfrapPerfArpPerDlciTxArpRep_Type()
)
dfrapPerfArpPerDlciTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxArpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciRxRarpReq_Type = Counter32
_DfrapPerfArpPerDlciRxRarpReq_Object = MibTableColumn
dfrapPerfArpPerDlciRxRarpReq = _DfrapPerfArpPerDlciRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 9),
    _DfrapPerfArpPerDlciRxRarpReq_Type()
)
dfrapPerfArpPerDlciRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxRarpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciTxRarpReq_Type = Counter32
_DfrapPerfArpPerDlciTxRarpReq_Object = MibTableColumn
dfrapPerfArpPerDlciTxRarpReq = _DfrapPerfArpPerDlciTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 10),
    _DfrapPerfArpPerDlciTxRarpReq_Type()
)
dfrapPerfArpPerDlciTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxRarpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciRxRarpRep_Type = Counter32
_DfrapPerfArpPerDlciRxRarpRep_Object = MibTableColumn
dfrapPerfArpPerDlciRxRarpRep = _DfrapPerfArpPerDlciRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 11),
    _DfrapPerfArpPerDlciRxRarpRep_Type()
)
dfrapPerfArpPerDlciRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxRarpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciTxRarpRep_Type = Counter32
_DfrapPerfArpPerDlciTxRarpRep_Object = MibTableColumn
dfrapPerfArpPerDlciTxRarpRep = _DfrapPerfArpPerDlciTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 12),
    _DfrapPerfArpPerDlciTxRarpRep_Type()
)
dfrapPerfArpPerDlciTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxRarpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciRxInarpReq_Type = Counter32
_DfrapPerfArpPerDlciRxInarpReq_Object = MibTableColumn
dfrapPerfArpPerDlciRxInarpReq = _DfrapPerfArpPerDlciRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 13),
    _DfrapPerfArpPerDlciRxInarpReq_Type()
)
dfrapPerfArpPerDlciRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxInarpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciTxInarpReq_Type = Counter32
_DfrapPerfArpPerDlciTxInarpReq_Object = MibTableColumn
dfrapPerfArpPerDlciTxInarpReq = _DfrapPerfArpPerDlciTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 14),
    _DfrapPerfArpPerDlciTxInarpReq_Type()
)
dfrapPerfArpPerDlciTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxInarpReq.setStatus("mandatory")
_DfrapPerfArpPerDlciRxInarpRep_Type = Counter32
_DfrapPerfArpPerDlciRxInarpRep_Object = MibTableColumn
dfrapPerfArpPerDlciRxInarpRep = _DfrapPerfArpPerDlciRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 15),
    _DfrapPerfArpPerDlciRxInarpRep_Type()
)
dfrapPerfArpPerDlciRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxInarpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciTxInarpRep_Type = Counter32
_DfrapPerfArpPerDlciTxInarpRep_Object = MibTableColumn
dfrapPerfArpPerDlciTxInarpRep = _DfrapPerfArpPerDlciTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 16),
    _DfrapPerfArpPerDlciTxInarpRep_Type()
)
dfrapPerfArpPerDlciTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxInarpRep.setStatus("mandatory")
_DfrapPerfArpPerDlciRxOther_Type = Counter32
_DfrapPerfArpPerDlciRxOther_Object = MibTableColumn
dfrapPerfArpPerDlciRxOther = _DfrapPerfArpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 17),
    _DfrapPerfArpPerDlciRxOther_Type()
)
dfrapPerfArpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciRxOther.setStatus("mandatory")
_DfrapPerfArpPerDlciTxOther_Type = Counter32
_DfrapPerfArpPerDlciTxOther_Object = MibTableColumn
dfrapPerfArpPerDlciTxOther = _DfrapPerfArpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 15, 1, 18),
    _DfrapPerfArpPerDlciTxOther_Type()
)
dfrapPerfArpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpPerDlciTxOther.setStatus("mandatory")
_DfrapPerfArpTotalTable_Object = MibTable
dfrapPerfArpTotalTable = _DfrapPerfArpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16)
)
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTable.setStatus("mandatory")
_DfrapPerfArpTotalEntry_Object = MibTableRow
dfrapPerfArpTotalEntry = _DfrapPerfArpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1)
)
dfrapPerfArpTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfArpTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfArpTotalEntry.setStatus("mandatory")


class _DfrapPerfArpTotalInterval_Type(Integer32):
    """Custom type dfrapPerfArpTotalInterval based on Integer32"""
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


_DfrapPerfArpTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfArpTotalInterval_Object = MibTableColumn
dfrapPerfArpTotalInterval = _DfrapPerfArpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 1),
    _DfrapPerfArpTotalInterval_Type()
)
dfrapPerfArpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalInterval.setStatus("mandatory")
_DfrapPerfArpTotalRxTotal_Type = Counter32
_DfrapPerfArpTotalRxTotal_Object = MibTableColumn
dfrapPerfArpTotalRxTotal = _DfrapPerfArpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 3),
    _DfrapPerfArpTotalRxTotal_Type()
)
dfrapPerfArpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxTotal.setStatus("mandatory")
_DfrapPerfArpTotalTxTotal_Type = Counter32
_DfrapPerfArpTotalTxTotal_Object = MibTableColumn
dfrapPerfArpTotalTxTotal = _DfrapPerfArpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 4),
    _DfrapPerfArpTotalTxTotal_Type()
)
dfrapPerfArpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxTotal.setStatus("mandatory")
_DfrapPerfArpTotalRxArpReq_Type = Counter32
_DfrapPerfArpTotalRxArpReq_Object = MibTableColumn
dfrapPerfArpTotalRxArpReq = _DfrapPerfArpTotalRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 5),
    _DfrapPerfArpTotalRxArpReq_Type()
)
dfrapPerfArpTotalRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxArpReq.setStatus("mandatory")
_DfrapPerfArpTotalTxArpReq_Type = Counter32
_DfrapPerfArpTotalTxArpReq_Object = MibTableColumn
dfrapPerfArpTotalTxArpReq = _DfrapPerfArpTotalTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 6),
    _DfrapPerfArpTotalTxArpReq_Type()
)
dfrapPerfArpTotalTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxArpReq.setStatus("mandatory")
_DfrapPerfArpTotalRxArpRep_Type = Counter32
_DfrapPerfArpTotalRxArpRep_Object = MibTableColumn
dfrapPerfArpTotalRxArpRep = _DfrapPerfArpTotalRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 7),
    _DfrapPerfArpTotalRxArpRep_Type()
)
dfrapPerfArpTotalRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxArpRep.setStatus("mandatory")
_DfrapPerfArpTotalTxArpRep_Type = Counter32
_DfrapPerfArpTotalTxArpRep_Object = MibTableColumn
dfrapPerfArpTotalTxArpRep = _DfrapPerfArpTotalTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 8),
    _DfrapPerfArpTotalTxArpRep_Type()
)
dfrapPerfArpTotalTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxArpRep.setStatus("mandatory")
_DfrapPerfArpTotalRxRarpReq_Type = Counter32
_DfrapPerfArpTotalRxRarpReq_Object = MibTableColumn
dfrapPerfArpTotalRxRarpReq = _DfrapPerfArpTotalRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 9),
    _DfrapPerfArpTotalRxRarpReq_Type()
)
dfrapPerfArpTotalRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxRarpReq.setStatus("mandatory")
_DfrapPerfArpTotalTxRarpReq_Type = Counter32
_DfrapPerfArpTotalTxRarpReq_Object = MibTableColumn
dfrapPerfArpTotalTxRarpReq = _DfrapPerfArpTotalTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 10),
    _DfrapPerfArpTotalTxRarpReq_Type()
)
dfrapPerfArpTotalTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxRarpReq.setStatus("mandatory")
_DfrapPerfArpTotalRxRarpRep_Type = Counter32
_DfrapPerfArpTotalRxRarpRep_Object = MibTableColumn
dfrapPerfArpTotalRxRarpRep = _DfrapPerfArpTotalRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 11),
    _DfrapPerfArpTotalRxRarpRep_Type()
)
dfrapPerfArpTotalRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxRarpRep.setStatus("mandatory")
_DfrapPerfArpTotalTxRarpRep_Type = Counter32
_DfrapPerfArpTotalTxRarpRep_Object = MibTableColumn
dfrapPerfArpTotalTxRarpRep = _DfrapPerfArpTotalTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 12),
    _DfrapPerfArpTotalTxRarpRep_Type()
)
dfrapPerfArpTotalTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxRarpRep.setStatus("mandatory")
_DfrapPerfArpTotalRxInarpReq_Type = Counter32
_DfrapPerfArpTotalRxInarpReq_Object = MibTableColumn
dfrapPerfArpTotalRxInarpReq = _DfrapPerfArpTotalRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 13),
    _DfrapPerfArpTotalRxInarpReq_Type()
)
dfrapPerfArpTotalRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxInarpReq.setStatus("mandatory")
_DfrapPerfArpTotalTxInarpReq_Type = Counter32
_DfrapPerfArpTotalTxInarpReq_Object = MibTableColumn
dfrapPerfArpTotalTxInarpReq = _DfrapPerfArpTotalTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 14),
    _DfrapPerfArpTotalTxInarpReq_Type()
)
dfrapPerfArpTotalTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxInarpReq.setStatus("mandatory")
_DfrapPerfArpTotalRxInarpRep_Type = Counter32
_DfrapPerfArpTotalRxInarpRep_Object = MibTableColumn
dfrapPerfArpTotalRxInarpRep = _DfrapPerfArpTotalRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 15),
    _DfrapPerfArpTotalRxInarpRep_Type()
)
dfrapPerfArpTotalRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxInarpRep.setStatus("mandatory")
_DfrapPerfArpTotalTxInarpRep_Type = Counter32
_DfrapPerfArpTotalTxInarpRep_Object = MibTableColumn
dfrapPerfArpTotalTxInarpRep = _DfrapPerfArpTotalTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 16),
    _DfrapPerfArpTotalTxInarpRep_Type()
)
dfrapPerfArpTotalTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxInarpRep.setStatus("mandatory")
_DfrapPerfArpTotalRxOther_Type = Counter32
_DfrapPerfArpTotalRxOther_Object = MibTableColumn
dfrapPerfArpTotalRxOther = _DfrapPerfArpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 17),
    _DfrapPerfArpTotalRxOther_Type()
)
dfrapPerfArpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalRxOther.setStatus("mandatory")
_DfrapPerfArpTotalTxOther_Type = Counter32
_DfrapPerfArpTotalTxOther_Object = MibTableColumn
dfrapPerfArpTotalTxOther = _DfrapPerfArpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 16, 1, 18),
    _DfrapPerfArpTotalTxOther_Type()
)
dfrapPerfArpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfArpTotalTxOther.setStatus("mandatory")
_DfrapPerfLmiPerDlciTable_Object = MibTable
dfrapPerfLmiPerDlciTable = _DfrapPerfLmiPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17)
)
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTable.setStatus("mandatory")
_DfrapPerfLmiPerDlciEntry_Object = MibTableRow
dfrapPerfLmiPerDlciEntry = _DfrapPerfLmiPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1)
)
dfrapPerfLmiPerDlciEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfLmiPerDlciInterval"),
    (0, "DFRAP-MIB", "dfrapPerfLmiPerDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciEntry.setStatus("mandatory")


class _DfrapPerfLmiPerDlciInterval_Type(Integer32):
    """Custom type dfrapPerfLmiPerDlciInterval based on Integer32"""
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


_DfrapPerfLmiPerDlciInterval_Type.__name__ = "Integer32"
_DfrapPerfLmiPerDlciInterval_Object = MibTableColumn
dfrapPerfLmiPerDlciInterval = _DfrapPerfLmiPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 1),
    _DfrapPerfLmiPerDlciInterval_Type()
)
dfrapPerfLmiPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciInterval.setStatus("mandatory")
_DfrapPerfLmiPerDlciValue_Type = Integer32
_DfrapPerfLmiPerDlciValue_Object = MibTableColumn
dfrapPerfLmiPerDlciValue = _DfrapPerfLmiPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 2),
    _DfrapPerfLmiPerDlciValue_Type()
)
dfrapPerfLmiPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciValue.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxTotalByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxTotalByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxTotalByteCnt = _DfrapPerfLmiPerDlciRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 3),
    _DfrapPerfLmiPerDlciRxTotalByteCnt_Type()
)
dfrapPerfLmiPerDlciRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxTotalByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxTotalByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxTotalByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxTotalByteCnt = _DfrapPerfLmiPerDlciTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 4),
    _DfrapPerfLmiPerDlciTxTotalByteCnt_Type()
)
dfrapPerfLmiPerDlciTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxTotalByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxLivoEnqByteCnt = _DfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 5),
    _DfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type()
)
dfrapPerfLmiPerDlciRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxLivoEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxLivoEnqByteCnt = _DfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 6),
    _DfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type()
)
dfrapPerfLmiPerDlciTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxLivoEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxLivoStatByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxLivoStatByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxLivoStatByteCnt = _DfrapPerfLmiPerDlciRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 7),
    _DfrapPerfLmiPerDlciRxLivoStatByteCnt_Type()
)
dfrapPerfLmiPerDlciRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxLivoStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxLivoStatByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxLivoStatByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxLivoStatByteCnt = _DfrapPerfLmiPerDlciTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 8),
    _DfrapPerfLmiPerDlciTxLivoStatByteCnt_Type()
)
dfrapPerfLmiPerDlciTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxLivoStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxFullEnqByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxFullEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxFullEnqByteCnt = _DfrapPerfLmiPerDlciRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 9),
    _DfrapPerfLmiPerDlciRxFullEnqByteCnt_Type()
)
dfrapPerfLmiPerDlciRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxFullEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxFullEnqByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxFullEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxFullEnqByteCnt = _DfrapPerfLmiPerDlciTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 10),
    _DfrapPerfLmiPerDlciTxFullEnqByteCnt_Type()
)
dfrapPerfLmiPerDlciTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxFullEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxFullStatByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxFullStatByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxFullStatByteCnt = _DfrapPerfLmiPerDlciRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 11),
    _DfrapPerfLmiPerDlciRxFullStatByteCnt_Type()
)
dfrapPerfLmiPerDlciRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxFullStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxFullStatByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxFullStatByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxFullStatByteCnt = _DfrapPerfLmiPerDlciTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 12),
    _DfrapPerfLmiPerDlciTxFullStatByteCnt_Type()
)
dfrapPerfLmiPerDlciTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxFullStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciRxOtherByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciRxOtherByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciRxOtherByteCnt = _DfrapPerfLmiPerDlciRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 13),
    _DfrapPerfLmiPerDlciRxOtherByteCnt_Type()
)
dfrapPerfLmiPerDlciRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciRxOtherByteCnt.setStatus("mandatory")
_DfrapPerfLmiPerDlciTxOtherByteCnt_Type = Counter32
_DfrapPerfLmiPerDlciTxOtherByteCnt_Object = MibTableColumn
dfrapPerfLmiPerDlciTxOtherByteCnt = _DfrapPerfLmiPerDlciTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 17, 1, 14),
    _DfrapPerfLmiPerDlciTxOtherByteCnt_Type()
)
dfrapPerfLmiPerDlciTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiPerDlciTxOtherByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTable_Object = MibTable
dfrapPerfLmiTotalTable = _DfrapPerfLmiTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18)
)
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTable.setStatus("mandatory")
_DfrapPerfLmiTotalEntry_Object = MibTableRow
dfrapPerfLmiTotalEntry = _DfrapPerfLmiTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1)
)
dfrapPerfLmiTotalEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfLmiTotalInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalEntry.setStatus("mandatory")


class _DfrapPerfLmiTotalInterval_Type(Integer32):
    """Custom type dfrapPerfLmiTotalInterval based on Integer32"""
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


_DfrapPerfLmiTotalInterval_Type.__name__ = "Integer32"
_DfrapPerfLmiTotalInterval_Object = MibTableColumn
dfrapPerfLmiTotalInterval = _DfrapPerfLmiTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 1),
    _DfrapPerfLmiTotalInterval_Type()
)
dfrapPerfLmiTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalInterval.setStatus("mandatory")
_DfrapPerfLmiTotalDlciValue_Type = Integer32
_DfrapPerfLmiTotalDlciValue_Object = MibTableColumn
dfrapPerfLmiTotalDlciValue = _DfrapPerfLmiTotalDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 2),
    _DfrapPerfLmiTotalDlciValue_Type()
)
dfrapPerfLmiTotalDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalDlciValue.setStatus("mandatory")
_DfrapPerfLmiTotalRxTotalByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxTotalByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxTotalByteCnt = _DfrapPerfLmiTotalRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 3),
    _DfrapPerfLmiTotalRxTotalByteCnt_Type()
)
dfrapPerfLmiTotalRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxTotalByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxTotalByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxTotalByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxTotalByteCnt = _DfrapPerfLmiTotalTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 4),
    _DfrapPerfLmiTotalTxTotalByteCnt_Type()
)
dfrapPerfLmiTotalTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxTotalByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalRxLivoEnqByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxLivoEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxLivoEnqByteCnt = _DfrapPerfLmiTotalRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 5),
    _DfrapPerfLmiTotalRxLivoEnqByteCnt_Type()
)
dfrapPerfLmiTotalRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxLivoEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxLivoEnqByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxLivoEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxLivoEnqByteCnt = _DfrapPerfLmiTotalTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 6),
    _DfrapPerfLmiTotalTxLivoEnqByteCnt_Type()
)
dfrapPerfLmiTotalTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxLivoEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalRxLivoStatByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxLivoStatByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxLivoStatByteCnt = _DfrapPerfLmiTotalRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 7),
    _DfrapPerfLmiTotalRxLivoStatByteCnt_Type()
)
dfrapPerfLmiTotalRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxLivoStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxLivoStatByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxLivoStatByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxLivoStatByteCnt = _DfrapPerfLmiTotalTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 8),
    _DfrapPerfLmiTotalTxLivoStatByteCnt_Type()
)
dfrapPerfLmiTotalTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxLivoStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalRxFullEnqByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxFullEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxFullEnqByteCnt = _DfrapPerfLmiTotalRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 9),
    _DfrapPerfLmiTotalRxFullEnqByteCnt_Type()
)
dfrapPerfLmiTotalRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxFullEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxFullEnqByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxFullEnqByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxFullEnqByteCnt = _DfrapPerfLmiTotalTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 10),
    _DfrapPerfLmiTotalTxFullEnqByteCnt_Type()
)
dfrapPerfLmiTotalTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxFullEnqByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalRxFullStatByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxFullStatByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxFullStatByteCnt = _DfrapPerfLmiTotalRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 11),
    _DfrapPerfLmiTotalRxFullStatByteCnt_Type()
)
dfrapPerfLmiTotalRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxFullStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxFullStatByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxFullStatByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxFullStatByteCnt = _DfrapPerfLmiTotalTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 12),
    _DfrapPerfLmiTotalTxFullStatByteCnt_Type()
)
dfrapPerfLmiTotalTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxFullStatByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalRxOtherByteCnt_Type = Counter32
_DfrapPerfLmiTotalRxOtherByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalRxOtherByteCnt = _DfrapPerfLmiTotalRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 13),
    _DfrapPerfLmiTotalRxOtherByteCnt_Type()
)
dfrapPerfLmiTotalRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalRxOtherByteCnt.setStatus("mandatory")
_DfrapPerfLmiTotalTxOtherByteCnt_Type = Counter32
_DfrapPerfLmiTotalTxOtherByteCnt_Object = MibTableColumn
dfrapPerfLmiTotalTxOtherByteCnt = _DfrapPerfLmiTotalTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 4, 18, 1, 14),
    _DfrapPerfLmiTotalTxOtherByteCnt_Type()
)
dfrapPerfLmiTotalTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfLmiTotalTxOtherByteCnt.setStatus("mandatory")
_DfrapPerfNetworkLongTerm_ObjectIdentity = ObjectIdentity
dfrapPerfNetworkLongTerm = _DfrapPerfNetworkLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5)
)
_DfrapPerfNetwLongTermTable_Object = MibTable
dfrapPerfNetwLongTermTable = _DfrapPerfNetwLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1)
)
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermTable.setStatus("mandatory")
_DfrapPerfNetwLongTermEntry_Object = MibTableRow
dfrapPerfNetwLongTermEntry = _DfrapPerfNetwLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1, 1)
)
dfrapPerfNetwLongTermEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfNetwLongTermDlci"),
    (0, "DFRAP-MIB", "dfrapPerfNetwLongTermProtocol"),
    (0, "DFRAP-MIB", "dfrapPerfNetwLongTermInterval"),
)
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermEntry.setStatus("mandatory")
_DfrapPerfNetwLongTermDlci_Type = Integer32
_DfrapPerfNetwLongTermDlci_Object = MibTableColumn
dfrapPerfNetwLongTermDlci = _DfrapPerfNetwLongTermDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1, 1, 1),
    _DfrapPerfNetwLongTermDlci_Type()
)
dfrapPerfNetwLongTermDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermDlci.setStatus("mandatory")


class _DfrapPerfNetwLongTermProtocol_Type(Integer32):
    """Custom type dfrapPerfNetwLongTermProtocol based on Integer32"""
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


_DfrapPerfNetwLongTermProtocol_Type.__name__ = "Integer32"
_DfrapPerfNetwLongTermProtocol_Object = MibTableColumn
dfrapPerfNetwLongTermProtocol = _DfrapPerfNetwLongTermProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1, 1, 2),
    _DfrapPerfNetwLongTermProtocol_Type()
)
dfrapPerfNetwLongTermProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermProtocol.setStatus("mandatory")
_DfrapPerfNetwLongTermInterval_Type = Integer32
_DfrapPerfNetwLongTermInterval_Object = MibTableColumn
dfrapPerfNetwLongTermInterval = _DfrapPerfNetwLongTermInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1, 1, 3),
    _DfrapPerfNetwLongTermInterval_Type()
)
dfrapPerfNetwLongTermInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermInterval.setStatus("mandatory")
_DfrapPerfNetwLongTermValue_Type = Counter32
_DfrapPerfNetwLongTermValue_Object = MibTableColumn
dfrapPerfNetwLongTermValue = _DfrapPerfNetwLongTermValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 1, 1, 4),
    _DfrapPerfNetwLongTermValue_Type()
)
dfrapPerfNetwLongTermValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermValue.setStatus("mandatory")
_DfrapPerfNetwLongTermAltTable_Object = MibTable
dfrapPerfNetwLongTermAltTable = _DfrapPerfNetwLongTermAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 2)
)
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermAltTable.setStatus("mandatory")
_DfrapPerfNetwLongTermAltEntry_Object = MibTableRow
dfrapPerfNetwLongTermAltEntry = _DfrapPerfNetwLongTermAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 2, 1)
)
dfrapPerfNetwLongTermAltEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfNetwLongTermAltDlci"),
    (0, "DFRAP-MIB", "dfrapPerfNetwLongTermAltProtocol"),
)
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermAltEntry.setStatus("mandatory")
_DfrapPerfNetwLongTermAltDlci_Type = Integer32
_DfrapPerfNetwLongTermAltDlci_Object = MibTableColumn
dfrapPerfNetwLongTermAltDlci = _DfrapPerfNetwLongTermAltDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 2, 1, 1),
    _DfrapPerfNetwLongTermAltDlci_Type()
)
dfrapPerfNetwLongTermAltDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermAltDlci.setStatus("mandatory")


class _DfrapPerfNetwLongTermAltProtocol_Type(Integer32):
    """Custom type dfrapPerfNetwLongTermAltProtocol based on Integer32"""
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


_DfrapPerfNetwLongTermAltProtocol_Type.__name__ = "Integer32"
_DfrapPerfNetwLongTermAltProtocol_Object = MibTableColumn
dfrapPerfNetwLongTermAltProtocol = _DfrapPerfNetwLongTermAltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 2, 1, 2),
    _DfrapPerfNetwLongTermAltProtocol_Type()
)
dfrapPerfNetwLongTermAltProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermAltProtocol.setStatus("mandatory")
_DfrapPerfNetwLongTermAltArray_Type = OctetString
_DfrapPerfNetwLongTermAltArray_Object = MibTableColumn
dfrapPerfNetwLongTermAltArray = _DfrapPerfNetwLongTermAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 2, 1, 3),
    _DfrapPerfNetwLongTermAltArray_Type()
)
dfrapPerfNetwLongTermAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfNetwLongTermAltArray.setStatus("mandatory")
_DfrapPerfNetworkLongTermCommands_ObjectIdentity = ObjectIdentity
dfrapPerfNetworkLongTermCommands = _DfrapPerfNetworkLongTermCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 3)
)


class _DfrapPerfNetworkLongTermCmdClear_Type(Integer32):
    """Custom type dfrapPerfNetworkLongTermCmdClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_DfrapPerfNetworkLongTermCmdClear_Type.__name__ = "Integer32"
_DfrapPerfNetworkLongTermCmdClear_Object = MibScalar
dfrapPerfNetworkLongTermCmdClear = _DfrapPerfNetworkLongTermCmdClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 5, 3, 1),
    _DfrapPerfNetworkLongTermCmdClear_Type()
)
dfrapPerfNetworkLongTermCmdClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapPerfNetworkLongTermCmdClear.setStatus("mandatory")
_DfrapPerfCirPercentUtilization_ObjectIdentity = ObjectIdentity
dfrapPerfCirPercentUtilization = _DfrapPerfCirPercentUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6)
)
_DfrapPerfCirPercentUtilizationTable_Object = MibTable
dfrapPerfCirPercentUtilizationTable = _DfrapPerfCirPercentUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1)
)
if mibBuilder.loadTexts:
    dfrapPerfCirPercentUtilizationTable.setStatus("mandatory")
_DfrapPerfCirPercentUtilizationEntry_Object = MibTableRow
dfrapPerfCirPercentUtilizationEntry = _DfrapPerfCirPercentUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1)
)
dfrapPerfCirPercentUtilizationEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfCirPercentUtilizationInterval"),
    (0, "DFRAP-MIB", "dfrapPerfCirPercentUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfCirPercentUtilizationEntry.setStatus("mandatory")


class _DfrapPerfCirPercentUtilizationInterval_Type(Integer32):
    """Custom type dfrapPerfCirPercentUtilizationInterval based on Integer32"""
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


_DfrapPerfCirPercentUtilizationInterval_Type.__name__ = "Integer32"
_DfrapPerfCirPercentUtilizationInterval_Object = MibTableColumn
dfrapPerfCirPercentUtilizationInterval = _DfrapPerfCirPercentUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 1),
    _DfrapPerfCirPercentUtilizationInterval_Type()
)
dfrapPerfCirPercentUtilizationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirPercentUtilizationInterval.setStatus("mandatory")
_DfrapPerfCirPercentUtilizationDlciValue_Type = Integer32
_DfrapPerfCirPercentUtilizationDlciValue_Object = MibTableColumn
dfrapPerfCirPercentUtilizationDlciValue = _DfrapPerfCirPercentUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 2),
    _DfrapPerfCirPercentUtilizationDlciValue_Type()
)
dfrapPerfCirPercentUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirPercentUtilizationDlciValue.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange1_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange1_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange1 = _DfrapPerfCirRxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 21),
    _DfrapPerfCirRxPercentUtilizationRange1_Type()
)
dfrapPerfCirRxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange1.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange2_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange2_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange2 = _DfrapPerfCirRxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 22),
    _DfrapPerfCirRxPercentUtilizationRange2_Type()
)
dfrapPerfCirRxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange2.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange3_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange3_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange3 = _DfrapPerfCirRxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 23),
    _DfrapPerfCirRxPercentUtilizationRange3_Type()
)
dfrapPerfCirRxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange3.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange4_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange4_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange4 = _DfrapPerfCirRxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 24),
    _DfrapPerfCirRxPercentUtilizationRange4_Type()
)
dfrapPerfCirRxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange4.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange5_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange5_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange5 = _DfrapPerfCirRxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 25),
    _DfrapPerfCirRxPercentUtilizationRange5_Type()
)
dfrapPerfCirRxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange5.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange6_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange6_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange6 = _DfrapPerfCirRxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 26),
    _DfrapPerfCirRxPercentUtilizationRange6_Type()
)
dfrapPerfCirRxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange6.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange7_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange7_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange7 = _DfrapPerfCirRxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 27),
    _DfrapPerfCirRxPercentUtilizationRange7_Type()
)
dfrapPerfCirRxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange7.setStatus("mandatory")
_DfrapPerfCirRxPercentUtilizationRange8_Type = Integer32
_DfrapPerfCirRxPercentUtilizationRange8_Object = MibTableColumn
dfrapPerfCirRxPercentUtilizationRange8 = _DfrapPerfCirRxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 28),
    _DfrapPerfCirRxPercentUtilizationRange8_Type()
)
dfrapPerfCirRxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirRxPercentUtilizationRange8.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange1_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange1_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange1 = _DfrapPerfCirTxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 41),
    _DfrapPerfCirTxPercentUtilizationRange1_Type()
)
dfrapPerfCirTxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange1.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange2_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange2_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange2 = _DfrapPerfCirTxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 42),
    _DfrapPerfCirTxPercentUtilizationRange2_Type()
)
dfrapPerfCirTxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange2.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange3_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange3_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange3 = _DfrapPerfCirTxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 43),
    _DfrapPerfCirTxPercentUtilizationRange3_Type()
)
dfrapPerfCirTxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange3.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange4_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange4_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange4 = _DfrapPerfCirTxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 44),
    _DfrapPerfCirTxPercentUtilizationRange4_Type()
)
dfrapPerfCirTxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange4.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange5_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange5_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange5 = _DfrapPerfCirTxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 45),
    _DfrapPerfCirTxPercentUtilizationRange5_Type()
)
dfrapPerfCirTxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange5.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange6_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange6_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange6 = _DfrapPerfCirTxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 46),
    _DfrapPerfCirTxPercentUtilizationRange6_Type()
)
dfrapPerfCirTxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange6.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange7_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange7_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange7 = _DfrapPerfCirTxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 47),
    _DfrapPerfCirTxPercentUtilizationRange7_Type()
)
dfrapPerfCirTxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange7.setStatus("mandatory")
_DfrapPerfCirTxPercentUtilizationRange8_Type = Integer32
_DfrapPerfCirTxPercentUtilizationRange8_Object = MibTableColumn
dfrapPerfCirTxPercentUtilizationRange8 = _DfrapPerfCirTxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 1, 1, 48),
    _DfrapPerfCirTxPercentUtilizationRange8_Type()
)
dfrapPerfCirTxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCirTxPercentUtilizationRange8.setStatus("mandatory")
_DfrapPerfCurrentPerDlciUtilizationTable_Object = MibTable
dfrapPerfCurrentPerDlciUtilizationTable = _DfrapPerfCurrentPerDlciUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2)
)
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciUtilizationTable.setStatus("mandatory")
_DfrapPerfCurrentPerDlciUtilizationEntry_Object = MibTableRow
dfrapPerfCurrentPerDlciUtilizationEntry = _DfrapPerfCurrentPerDlciUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2, 1)
)
dfrapPerfCurrentPerDlciUtilizationEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapPerfCurrentPerDlciUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciUtilizationEntry.setStatus("mandatory")
_DfrapPerfCurrentPerDlciUtilizationDlciValue_Type = Integer32
_DfrapPerfCurrentPerDlciUtilizationDlciValue_Object = MibTableColumn
dfrapPerfCurrentPerDlciUtilizationDlciValue = _DfrapPerfCurrentPerDlciUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2, 1, 1),
    _DfrapPerfCurrentPerDlciUtilizationDlciValue_Type()
)
dfrapPerfCurrentPerDlciUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciUtilizationDlciValue.setStatus("mandatory")
_DfrapPerfCurrentPerDlciRxUtilization_Type = Integer32
_DfrapPerfCurrentPerDlciRxUtilization_Object = MibTableColumn
dfrapPerfCurrentPerDlciRxUtilization = _DfrapPerfCurrentPerDlciRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2, 1, 2),
    _DfrapPerfCurrentPerDlciRxUtilization_Type()
)
dfrapPerfCurrentPerDlciRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciRxUtilization.setStatus("mandatory")
_DfrapPerfCurrentPerDlciTxUtilization_Type = Integer32
_DfrapPerfCurrentPerDlciTxUtilization_Object = MibTableColumn
dfrapPerfCurrentPerDlciTxUtilization = _DfrapPerfCurrentPerDlciTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2, 1, 3),
    _DfrapPerfCurrentPerDlciTxUtilization_Type()
)
dfrapPerfCurrentPerDlciTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciTxUtilization.setStatus("mandatory")
_DfrapPerfCurrentPerDlciAggregateUtilization_Type = Integer32
_DfrapPerfCurrentPerDlciAggregateUtilization_Object = MibTableColumn
dfrapPerfCurrentPerDlciAggregateUtilization = _DfrapPerfCurrentPerDlciAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 2, 1, 4),
    _DfrapPerfCurrentPerDlciAggregateUtilization_Type()
)
dfrapPerfCurrentPerDlciAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentPerDlciAggregateUtilization.setStatus("mandatory")
_DfrapPerfCurrentUnitUtilization_ObjectIdentity = ObjectIdentity
dfrapPerfCurrentUnitUtilization = _DfrapPerfCurrentUnitUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 3)
)
_DfrapPerfCurrentDteUtilization_Type = Integer32
_DfrapPerfCurrentDteUtilization_Object = MibScalar
dfrapPerfCurrentDteUtilization = _DfrapPerfCurrentDteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 3, 2),
    _DfrapPerfCurrentDteUtilization_Type()
)
dfrapPerfCurrentDteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentDteUtilization.setStatus("mandatory")
_DfrapPerfCurrentWanUtilization_Type = Integer32
_DfrapPerfCurrentWanUtilization_Object = MibScalar
dfrapPerfCurrentWanUtilization = _DfrapPerfCurrentWanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 3, 3),
    _DfrapPerfCurrentWanUtilization_Type()
)
dfrapPerfCurrentWanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentWanUtilization.setStatus("mandatory")
_DfrapPerfCurrentAggregateUtilization_Type = Integer32
_DfrapPerfCurrentAggregateUtilization_Object = MibScalar
dfrapPerfCurrentAggregateUtilization = _DfrapPerfCurrentAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 5, 6, 3, 4),
    _DfrapPerfCurrentAggregateUtilization_Type()
)
dfrapPerfCurrentAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPerfCurrentAggregateUtilization.setStatus("mandatory")


class _DfrapAlarmType_Type(Integer32):
    """Custom type dfrapAlarmType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
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
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
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
          ("bert-test-pattern-completed", 45),
          ("bert-test-pattern-failure", 46),
          ("bert-test-pattern-initiated", 44),
          ("bpv-threshold-acceptable", 70),
          ("bpv-threshold-exceeded", 69),
          ("config-install-success", 142),
          ("config-local-update", 2),
          ("connect-failure", 66),
          ("connected", 65),
          ("disconnected", 68),
          ("dlci-active", 47),
          ("dlci-inactive", 48),
          ("dlci-td-threshold", 49),
          ("dte-signal-dtr-off", 58),
          ("dte-signal-dtr-on", 57),
          ("dte-signal-rts-off", 56),
          ("dte-signal-rts-on", 55),
          ("incoming-call", 67),
          ("line-failure", 63),
          ("line-in-service", 64),
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
          ("local-network-loopback-disabled", 27),
          ("local-network-loopback-enabled", 26),
          ("local-network-loopback-failure", 28),
          ("local-unit-loopback-disabled", 15),
          ("local-unit-loopback-enabled", 14),
          ("local-unit-loopback-failure", 16),
          ("pvc-rx-utilization-cleared", 140),
          ("pvc-rx-utilization-exceeded", 138),
          ("pvc-tx-utilization-cleared", 141),
          ("pvc-tx-utilization-exceeded", 139),
          ("remote-network-non-latching-loopback-disabled", 74),
          ("remote-network-non-latching-loopback-enabled", 73),
          ("remote-network-simplex-loopback-disabled", 72),
          ("remote-network-simplex-loopback-enabled", 71),
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
          ("v54-loop-down-completed", 30),
          ("v54-loop-up-initiated", 29),
          ("v54-loopback-disabled-by-remote", 32),
          ("v54-loopback-enabled-by-remote", 31),
          ("v54-loopback-failure", 33),
          ("vbert-request-failed", 97),
          ("vbert-started", 95),
          ("vbert-stopped", 96),
          ("vloop-down-via-remote", 93),
          ("vloop-failed", 94),
          ("vloop-loop-down", 91),
          ("vloop-loop-up", 90),
          ("vloop-up-via-remote", 92))
    )


_DfrapAlarmType_Type.__name__ = "Integer32"
_DfrapAlarmType_Object = MibScalar
dfrapAlarmType = _DfrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 6),
    _DfrapAlarmType_Type()
)
dfrapAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapAlarmType.setStatus("mandatory")
_DfrapDLCINum_Type = Integer32
_DfrapDLCINum_Object = MibScalar
dfrapDLCINum = _DfrapDLCINum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 7),
    _DfrapDLCINum_Type()
)
dfrapDLCINum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapDLCINum.setStatus("mandatory")


class _DfrapInterface_Type(Integer32):
    """Custom type dfrapInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dds", 2),
          ("dte", 1))
    )


_DfrapInterface_Type.__name__ = "Integer32"
_DfrapInterface_Object = MibScalar
dfrapInterface = _DfrapInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 8),
    _DfrapInterface_Type()
)
dfrapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapInterface.setStatus("mandatory")
_DfrapIpAddress_Type = IpAddress
_DfrapIpAddress_Object = MibScalar
dfrapIpAddress = _DfrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 9),
    _DfrapIpAddress_Type()
)
dfrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapIpAddress.setStatus("mandatory")
_DfrapEventTrapLog_ObjectIdentity = ObjectIdentity
dfrapEventTrapLog = _DfrapEventTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 6, 10)
)
_DfrapEventTrapLogTable_Object = MibTable
dfrapEventTrapLogTable = _DfrapEventTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1)
)
if mibBuilder.loadTexts:
    dfrapEventTrapLogTable.setStatus("mandatory")
_DfrapEventTrapLogEntry_Object = MibTableRow
dfrapEventTrapLogEntry = _DfrapEventTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1)
)
dfrapEventTrapLogEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapEventTrapLogSeqNum"),
)
if mibBuilder.loadTexts:
    dfrapEventTrapLogEntry.setStatus("mandatory")
_DfrapEventTrapLogSeqNum_Type = Integer32
_DfrapEventTrapLogSeqNum_Object = MibTableColumn
dfrapEventTrapLogSeqNum = _DfrapEventTrapLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 1),
    _DfrapEventTrapLogSeqNum_Type()
)
dfrapEventTrapLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogSeqNum.setStatus("mandatory")
_DfrapEventTrapLogGenericEvent_Type = Integer32
_DfrapEventTrapLogGenericEvent_Object = MibTableColumn
dfrapEventTrapLogGenericEvent = _DfrapEventTrapLogGenericEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 2),
    _DfrapEventTrapLogGenericEvent_Type()
)
dfrapEventTrapLogGenericEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogGenericEvent.setStatus("mandatory")
_DfrapEventTrapLogSpecificEvent_Type = Integer32
_DfrapEventTrapLogSpecificEvent_Object = MibTableColumn
dfrapEventTrapLogSpecificEvent = _DfrapEventTrapLogSpecificEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 3),
    _DfrapEventTrapLogSpecificEvent_Type()
)
dfrapEventTrapLogSpecificEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogSpecificEvent.setStatus("mandatory")
_DfrapEventTrapLogTimeStamp_Type = TimeTicks
_DfrapEventTrapLogTimeStamp_Object = MibTableColumn
dfrapEventTrapLogTimeStamp = _DfrapEventTrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 4),
    _DfrapEventTrapLogTimeStamp_Type()
)
dfrapEventTrapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogTimeStamp.setStatus("mandatory")
_DfrapEventTrapLogVarBind1_Type = Integer32
_DfrapEventTrapLogVarBind1_Object = MibTableColumn
dfrapEventTrapLogVarBind1 = _DfrapEventTrapLogVarBind1_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 5),
    _DfrapEventTrapLogVarBind1_Type()
)
dfrapEventTrapLogVarBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogVarBind1.setStatus("mandatory")
_DfrapEventTrapLogVarBind2_Type = Integer32
_DfrapEventTrapLogVarBind2_Object = MibTableColumn
dfrapEventTrapLogVarBind2 = _DfrapEventTrapLogVarBind2_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 6),
    _DfrapEventTrapLogVarBind2_Type()
)
dfrapEventTrapLogVarBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogVarBind2.setStatus("mandatory")
_DfrapEventTrapLogVarBind3_Type = Integer32
_DfrapEventTrapLogVarBind3_Object = MibTableColumn
dfrapEventTrapLogVarBind3 = _DfrapEventTrapLogVarBind3_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 1, 1, 7),
    _DfrapEventTrapLogVarBind3_Type()
)
dfrapEventTrapLogVarBind3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventTrapLogVarBind3.setStatus("mandatory")
_DfrapEventLogAltTable_Object = MibTable
dfrapEventLogAltTable = _DfrapEventLogAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 2)
)
if mibBuilder.loadTexts:
    dfrapEventLogAltTable.setStatus("mandatory")
_DfrapEventLogAltEntry_Object = MibTableRow
dfrapEventLogAltEntry = _DfrapEventLogAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 2, 1)
)
dfrapEventLogAltEntry.setIndexNames(
    (0, "DFRAP-MIB", "dfrapEventLogAltSeqNum"),
)
if mibBuilder.loadTexts:
    dfrapEventLogAltEntry.setStatus("mandatory")
_DfrapEventLogAltSeqNum_Type = Integer32
_DfrapEventLogAltSeqNum_Object = MibTableColumn
dfrapEventLogAltSeqNum = _DfrapEventLogAltSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 2, 1, 1),
    _DfrapEventLogAltSeqNum_Type()
)
dfrapEventLogAltSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventLogAltSeqNum.setStatus("mandatory")
_DfrapEventLogAltArray_Type = OctetString
_DfrapEventLogAltArray_Object = MibTableColumn
dfrapEventLogAltArray = _DfrapEventLogAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 2, 1, 2),
    _DfrapEventLogAltArray_Type()
)
dfrapEventLogAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventLogAltArray.setStatus("mandatory")
_DfrapEventLogCurrentSeqNum_Type = Integer32
_DfrapEventLogCurrentSeqNum_Object = MibScalar
dfrapEventLogCurrentSeqNum = _DfrapEventLogCurrentSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 3),
    _DfrapEventLogCurrentSeqNum_Type()
)
dfrapEventLogCurrentSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapEventLogCurrentSeqNum.setStatus("mandatory")


class _DfrapEventLogFreeze_Type(Integer32):
    """Custom type dfrapEventLogFreeze based on Integer32"""
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


_DfrapEventLogFreeze_Type.__name__ = "Integer32"
_DfrapEventLogFreeze_Object = MibScalar
dfrapEventLogFreeze = _DfrapEventLogFreeze_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 4),
    _DfrapEventLogFreeze_Type()
)
dfrapEventLogFreeze.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapEventLogFreeze.setStatus("mandatory")


class _DfrapEventLogClear_Type(Integer32):
    """Custom type dfrapEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_DfrapEventLogClear_Type.__name__ = "Integer32"
_DfrapEventLogClear_Object = MibScalar
dfrapEventLogClear = _DfrapEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 10, 5),
    _DfrapEventLogClear_Type()
)
dfrapEventLogClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dfrapEventLogClear.setStatus("mandatory")
_DfrapPercentUtilization_Type = Integer32
_DfrapPercentUtilization_Object = MibScalar
dfrapPercentUtilization = _DfrapPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 11),
    _DfrapPercentUtilization_Type()
)
dfrapPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapPercentUtilization.setStatus("mandatory")
_DfrapUtilizationThreshold_Type = Integer32
_DfrapUtilizationThreshold_Object = MibScalar
dfrapUtilizationThreshold = _DfrapUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 12),
    _DfrapUtilizationThreshold_Type()
)
dfrapUtilizationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapUtilizationThreshold.setStatus("mandatory")
_DfrapCfgLockIpAddress_Type = Integer32
_DfrapCfgLockIpAddress_Object = MibScalar
dfrapCfgLockIpAddress = _DfrapCfgLockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 6, 13),
    _DfrapCfgLockIpAddress_Type()
)
dfrapCfgLockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfrapCfgLockIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dfrapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 0)
)
dfrapTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTrap.setStatus(
        ""
    )

dfrapBadConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 1)
)
dfrapBadConfigTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBadConfigTrap.setStatus(
        ""
    )

dfrapLocalConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 2)
)
dfrapLocalConfigTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalConfigTrap.setStatus(
        ""
    )

dfrapLocalUnitLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 14)
)
dfrapLocalUnitLoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalUnitLoopbackEnabledTrap.setStatus(
        ""
    )

dfrapLocalUnitLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 15)
)
dfrapLocalUnitLoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalUnitLoopbackDisabledTrap.setStatus(
        ""
    )

dfrapLocalUnitLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 16)
)
dfrapLocalUnitLoopbackFailedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalUnitLoopbackFailedTrap.setStatus(
        ""
    )

dfrapLocalDteLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 17)
)
dfrapLocalDteLoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalDteLoopbackEnabledTrap.setStatus(
        ""
    )

dfrapLocalDteLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 18)
)
dfrapLocalDteLoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalDteLoopbackDisabledTrap.setStatus(
        ""
    )

dfrapLocalDteLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 19)
)
dfrapLocalDteLoopbackFailedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalDteLoopbackFailedTrap.setStatus(
        ""
    )

dfrapLocalNetLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 26)
)
dfrapLocalNetLoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalNetLoopbackEnabledTrap.setStatus(
        ""
    )

dfrapLocalNetLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 27)
)
dfrapLocalNetLoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalNetLoopbackDisabledTrap.setStatus(
        ""
    )

dfrapLocalNetLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 28)
)
dfrapLocalNetLoopbackFailedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLocalNetLoopbackFailedTrap.setStatus(
        ""
    )

dfrapV54LoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 29)
)
dfrapV54LoopUpInitiatedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapV54LoopUpInitiatedTrap.setStatus(
        ""
    )

dfrapV54LoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 30)
)
dfrapV54LoopDownCompletedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapV54LoopDownCompletedTrap.setStatus(
        ""
    )

dfrapV54LoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 31)
)
dfrapV54LoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapV54LoopbackEnabledTrap.setStatus(
        ""
    )

dfrapV54LoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 32)
)
dfrapV54LoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapV54LoopbackDisabledTrap.setStatus(
        ""
    )

dfrapV54LoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 33)
)
dfrapV54LoopbackFailedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapV54LoopbackFailedTrap.setStatus(
        ""
    )

dfrapBertInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 44)
)
dfrapBertInitiatedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBertInitiatedTrap.setStatus(
        ""
    )

dfrapBertCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 45)
)
dfrapBertCompletedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBertCompletedTrap.setStatus(
        ""
    )

dfrapBertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 46)
)
dfrapBertFailedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBertFailedTrap.setStatus(
        ""
    )

dfrapDLCIActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 47)
)
dfrapDLCIActiveTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"))
)
if mibBuilder.loadTexts:
    dfrapDLCIActiveTrap.setStatus(
        ""
    )

dfrapDLCIInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 48)
)
dfrapDLCIInactiveTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"))
)
if mibBuilder.loadTexts:
    dfrapDLCIInactiveTrap.setStatus(
        ""
    )

dfrapDLCITDThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 49)
)
dfrapDLCITDThresholdTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapIpAddress"))
)
if mibBuilder.loadTexts:
    dfrapDLCITDThresholdTrap.setStatus(
        ""
    )

dfrapLmiSourcingChangePassthruTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 50)
)
dfrapLmiSourcingChangePassthruTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSourcingChangePassthruTrap.setStatus(
        ""
    )

dfrapLmiSourcingChangeUserDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 51)
)
dfrapLmiSourcingChangeUserDteTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSourcingChangeUserDteTrap.setStatus(
        ""
    )

dfrapLmiSourcingChangeNetDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 52)
)
dfrapLmiSourcingChangeNetDteTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSourcingChangeNetDteTrap.setStatus(
        ""
    )

dfrapLmiSourcingChangeUserDdsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 53)
)
dfrapLmiSourcingChangeUserDdsTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSourcingChangeUserDdsTrap.setStatus(
        ""
    )

dfrapLmiSourcingChangeNetDdsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 54)
)
dfrapLmiSourcingChangeNetDdsTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSourcingChangeNetDdsTrap.setStatus(
        ""
    )

dfrapDteSignalRtsOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 55)
)
dfrapDteSignalRtsOnTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapDteSignalRtsOnTrap.setStatus(
        ""
    )

dfrapDteSignalRtsOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 56)
)
dfrapDteSignalRtsOffTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapDteSignalRtsOffTrap.setStatus(
        ""
    )

dfrapDteSignalDtrOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 57)
)
dfrapDteSignalDtrOnTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapDteSignalDtrOnTrap.setStatus(
        ""
    )

dfrapDteSignalDtrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 58)
)
dfrapDteSignalDtrOffTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapDteSignalDtrOffTrap.setStatus(
        ""
    )

dfrapNonIncrLmiSeqNumDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 59)
)
dfrapNonIncrLmiSeqNumDteTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapNonIncrLmiSeqNumDteTrap.setStatus(
        ""
    )

dfrapNonIncrLmiSeqNumDdsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 60)
)
dfrapNonIncrLmiSeqNumDdsTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapNonIncrLmiSeqNumDdsTrap.setStatus(
        ""
    )

dfrapLmiSeqNumMismatchDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 61)
)
dfrapLmiSeqNumMismatchDteTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSeqNumMismatchDteTrap.setStatus(
        ""
    )

dfrapLmiSeqNumMismatchDdsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 62)
)
dfrapLmiSeqNumMismatchDdsTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLmiSeqNumMismatchDdsTrap.setStatus(
        ""
    )

dfrapLineFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 63)
)
dfrapLineFailureTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLineFailureTrap.setStatus(
        ""
    )

dfrapLineInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 64)
)
dfrapLineInServiceTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapLineInServiceTrap.setStatus(
        ""
    )

dfrapBPVThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 69)
)
dfrapBPVThresholdExceededTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBPVThresholdExceededTrap.setStatus(
        ""
    )

dfrapBPVThresholdAcceptableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 70)
)
dfrapBPVThresholdAcceptableTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapBPVThresholdAcceptableTrap.setStatus(
        ""
    )

dfrapSimplexCurrentLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 71)
)
dfrapSimplexCurrentLoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapSimplexCurrentLoopbackEnabledTrap.setStatus(
        ""
    )

dfrapSimplexCurrentLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 72)
)
dfrapSimplexCurrentLoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapSimplexCurrentLoopbackDisabledTrap.setStatus(
        ""
    )

dfrapNonLatchingLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 73)
)
dfrapNonLatchingLoopbackEnabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapNonLatchingLoopbackEnabledTrap.setStatus(
        ""
    )

dfrapNonLatchingLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 74)
)
dfrapNonLatchingLoopbackDisabledTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapNonLatchingLoopbackDisabledTrap.setStatus(
        ""
    )

dfrapTrapMutingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 75)
)
dfrapTrapMutingActive.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTrapMutingActive.setStatus(
        ""
    )

dfrapTrapMutingInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 76)
)
dfrapTrapMutingInactive.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTrapMutingInactive.setStatus(
        ""
    )

dfrapVloopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 90)
)
dfrapVloopUp.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVloopUp.setStatus(
        ""
    )

dfrapVloopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 91)
)
dfrapVloopDown.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVloopDown.setStatus(
        ""
    )

dfrapVloopUpViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 92)
)
dfrapVloopUpViaRemote.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVloopUpViaRemote.setStatus(
        ""
    )

dfrapVloopDownViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 93)
)
dfrapVloopDownViaRemote.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVloopDownViaRemote.setStatus(
        ""
    )

dfrapVloopRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 94)
)
dfrapVloopRequestFailed.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVloopRequestFailed.setStatus(
        ""
    )

dfrapVbertStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 95)
)
dfrapVbertStarted.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVbertStarted.setStatus(
        ""
    )

dfrapVbertStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 96)
)
dfrapVbertStopped.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVbertStopped.setStatus(
        ""
    )

dfrapVbertRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 97)
)
dfrapVbertRequestFailed.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapInterface"))
)
if mibBuilder.loadTexts:
    dfrapVbertRequestFailed.setStatus(
        ""
    )

dfrapPvcRxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 138)
)
dfrapPvcRxUtilizationExceededTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapPercentUtilization"),
        ("DFRAP-MIB", "dfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    dfrapPvcRxUtilizationExceededTrap.setStatus(
        ""
    )

dfrapPvcTxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 139)
)
dfrapPvcTxUtilizationExceededTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapPercentUtilization"),
        ("DFRAP-MIB", "dfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    dfrapPvcTxUtilizationExceededTrap.setStatus(
        ""
    )

dfrapPvcRxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 140)
)
dfrapPvcRxUtilizationClearedTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapPercentUtilization"),
        ("DFRAP-MIB", "dfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    dfrapPvcRxUtilizationClearedTrap.setStatus(
        ""
    )

dfrapPvcTxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 141)
)
dfrapPvcTxUtilizationClearedTrap.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapDLCINum"),
        ("DFRAP-MIB", "dfrapPercentUtilization"),
        ("DFRAP-MIB", "dfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    dfrapPvcTxUtilizationClearedTrap.setStatus(
        ""
    )

dfrapConfigInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 142)
)
dfrapConfigInstallSuccess.setObjects(
      *(("DFRAP-MIB", "dfrapAlarmType"),
        ("DFRAP-MIB", "dfrapCfgLockIpAddress"))
)
if mibBuilder.loadTexts:
    dfrapConfigInstallSuccess.setStatus(
        ""
    )

dfrapTftpRequestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 257)
)
dfrapTftpRequestedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpRequestedTrap.setStatus(
        ""
    )

dfrapTftpTransferringTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 258)
)
dfrapTftpTransferringTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpTransferringTrap.setStatus(
        ""
    )

dfrapTftpProgrammingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 259)
)
dfrapTftpProgrammingTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpProgrammingTrap.setStatus(
        ""
    )

dfrapTftpAbortedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 260)
)
dfrapTftpAbortedTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpAbortedTrap.setStatus(
        ""
    )

dfrapTftpSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 261)
)
dfrapTftpSuccessTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpSuccessTrap.setStatus(
        ""
    )

dfrapTftpHostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 262)
)
dfrapTftpHostUnreachableTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpHostUnreachableTrap.setStatus(
        ""
    )

dfrapTftpNoFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 263)
)
dfrapTftpNoFileTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpNoFileTrap.setStatus(
        ""
    )

dfrapTftpInvalidFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 264)
)
dfrapTftpInvalidFileTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpInvalidFileTrap.setStatus(
        ""
    )

dfrapTftpCorruptFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 6, 0, 265)
)
dfrapTftpCorruptFileTrap.setObjects(
    ("DFRAP-MIB", "dfrapAlarmType")
)
if mibBuilder.loadTexts:
    dfrapTftpCorruptFileTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFRAP-MIB",
    **{"Index": Index,
       "private": private,
       "enterprises": enterprises,
       "sync": sync,
       "dfrap": dfrap,
       "dfrapTrap": dfrapTrap,
       "dfrapBadConfigTrap": dfrapBadConfigTrap,
       "dfrapLocalConfigTrap": dfrapLocalConfigTrap,
       "dfrapLocalUnitLoopbackEnabledTrap": dfrapLocalUnitLoopbackEnabledTrap,
       "dfrapLocalUnitLoopbackDisabledTrap": dfrapLocalUnitLoopbackDisabledTrap,
       "dfrapLocalUnitLoopbackFailedTrap": dfrapLocalUnitLoopbackFailedTrap,
       "dfrapLocalDteLoopbackEnabledTrap": dfrapLocalDteLoopbackEnabledTrap,
       "dfrapLocalDteLoopbackDisabledTrap": dfrapLocalDteLoopbackDisabledTrap,
       "dfrapLocalDteLoopbackFailedTrap": dfrapLocalDteLoopbackFailedTrap,
       "dfrapLocalNetLoopbackEnabledTrap": dfrapLocalNetLoopbackEnabledTrap,
       "dfrapLocalNetLoopbackDisabledTrap": dfrapLocalNetLoopbackDisabledTrap,
       "dfrapLocalNetLoopbackFailedTrap": dfrapLocalNetLoopbackFailedTrap,
       "dfrapV54LoopUpInitiatedTrap": dfrapV54LoopUpInitiatedTrap,
       "dfrapV54LoopDownCompletedTrap": dfrapV54LoopDownCompletedTrap,
       "dfrapV54LoopbackEnabledTrap": dfrapV54LoopbackEnabledTrap,
       "dfrapV54LoopbackDisabledTrap": dfrapV54LoopbackDisabledTrap,
       "dfrapV54LoopbackFailedTrap": dfrapV54LoopbackFailedTrap,
       "dfrapBertInitiatedTrap": dfrapBertInitiatedTrap,
       "dfrapBertCompletedTrap": dfrapBertCompletedTrap,
       "dfrapBertFailedTrap": dfrapBertFailedTrap,
       "dfrapDLCIActiveTrap": dfrapDLCIActiveTrap,
       "dfrapDLCIInactiveTrap": dfrapDLCIInactiveTrap,
       "dfrapDLCITDThresholdTrap": dfrapDLCITDThresholdTrap,
       "dfrapLmiSourcingChangePassthruTrap": dfrapLmiSourcingChangePassthruTrap,
       "dfrapLmiSourcingChangeUserDteTrap": dfrapLmiSourcingChangeUserDteTrap,
       "dfrapLmiSourcingChangeNetDteTrap": dfrapLmiSourcingChangeNetDteTrap,
       "dfrapLmiSourcingChangeUserDdsTrap": dfrapLmiSourcingChangeUserDdsTrap,
       "dfrapLmiSourcingChangeNetDdsTrap": dfrapLmiSourcingChangeNetDdsTrap,
       "dfrapDteSignalRtsOnTrap": dfrapDteSignalRtsOnTrap,
       "dfrapDteSignalRtsOffTrap": dfrapDteSignalRtsOffTrap,
       "dfrapDteSignalDtrOnTrap": dfrapDteSignalDtrOnTrap,
       "dfrapDteSignalDtrOffTrap": dfrapDteSignalDtrOffTrap,
       "dfrapNonIncrLmiSeqNumDteTrap": dfrapNonIncrLmiSeqNumDteTrap,
       "dfrapNonIncrLmiSeqNumDdsTrap": dfrapNonIncrLmiSeqNumDdsTrap,
       "dfrapLmiSeqNumMismatchDteTrap": dfrapLmiSeqNumMismatchDteTrap,
       "dfrapLmiSeqNumMismatchDdsTrap": dfrapLmiSeqNumMismatchDdsTrap,
       "dfrapLineFailureTrap": dfrapLineFailureTrap,
       "dfrapLineInServiceTrap": dfrapLineInServiceTrap,
       "dfrapBPVThresholdExceededTrap": dfrapBPVThresholdExceededTrap,
       "dfrapBPVThresholdAcceptableTrap": dfrapBPVThresholdAcceptableTrap,
       "dfrapSimplexCurrentLoopbackEnabledTrap": dfrapSimplexCurrentLoopbackEnabledTrap,
       "dfrapSimplexCurrentLoopbackDisabledTrap": dfrapSimplexCurrentLoopbackDisabledTrap,
       "dfrapNonLatchingLoopbackEnabledTrap": dfrapNonLatchingLoopbackEnabledTrap,
       "dfrapNonLatchingLoopbackDisabledTrap": dfrapNonLatchingLoopbackDisabledTrap,
       "dfrapTrapMutingActive": dfrapTrapMutingActive,
       "dfrapTrapMutingInactive": dfrapTrapMutingInactive,
       "dfrapVloopUp": dfrapVloopUp,
       "dfrapVloopDown": dfrapVloopDown,
       "dfrapVloopUpViaRemote": dfrapVloopUpViaRemote,
       "dfrapVloopDownViaRemote": dfrapVloopDownViaRemote,
       "dfrapVloopRequestFailed": dfrapVloopRequestFailed,
       "dfrapVbertStarted": dfrapVbertStarted,
       "dfrapVbertStopped": dfrapVbertStopped,
       "dfrapVbertRequestFailed": dfrapVbertRequestFailed,
       "dfrapPvcRxUtilizationExceededTrap": dfrapPvcRxUtilizationExceededTrap,
       "dfrapPvcTxUtilizationExceededTrap": dfrapPvcTxUtilizationExceededTrap,
       "dfrapPvcRxUtilizationClearedTrap": dfrapPvcRxUtilizationClearedTrap,
       "dfrapPvcTxUtilizationClearedTrap": dfrapPvcTxUtilizationClearedTrap,
       "dfrapConfigInstallSuccess": dfrapConfigInstallSuccess,
       "dfrapTftpRequestedTrap": dfrapTftpRequestedTrap,
       "dfrapTftpTransferringTrap": dfrapTftpTransferringTrap,
       "dfrapTftpProgrammingTrap": dfrapTftpProgrammingTrap,
       "dfrapTftpAbortedTrap": dfrapTftpAbortedTrap,
       "dfrapTftpSuccessTrap": dfrapTftpSuccessTrap,
       "dfrapTftpHostUnreachableTrap": dfrapTftpHostUnreachableTrap,
       "dfrapTftpNoFileTrap": dfrapTftpNoFileTrap,
       "dfrapTftpInvalidFileTrap": dfrapTftpInvalidFileTrap,
       "dfrapTftpCorruptFileTrap": dfrapTftpCorruptFileTrap,
       "dfrapSystem": dfrapSystem,
       "dfrapSysTable": dfrapSysTable,
       "dfrapSysType": dfrapSysType,
       "dfrapSysSoftRev": dfrapSysSoftRev,
       "dfrapSysHardRev": dfrapSysHardRev,
       "dfrapSysNumT1Installed": dfrapSysNumT1Installed,
       "dfrapSysNumDteInstalled": dfrapSysNumDteInstalled,
       "dfrapSysNumMaintInstalled": dfrapSysNumMaintInstalled,
       "dfrapSysName": dfrapSysName,
       "dfrapSysSerialNo": dfrapSysSerialNo,
       "dfrapSysResetNode": dfrapSysResetNode,
       "dfrapSysAmtMemoryInstalled": dfrapSysAmtMemoryInstalled,
       "dfrapSysNumDdsInstalled": dfrapSysNumDdsInstalled,
       "dfrapSysLocation": dfrapSysLocation,
       "dfrapSysContact": dfrapSysContact,
       "dfrapSysPrompt": dfrapSysPrompt,
       "dfrapSysBootRev": dfrapSysBootRev,
       "dfrapSysFeatureTable": dfrapSysFeatureTable,
       "dfrapSysSLIPSupported": dfrapSysSLIPSupported,
       "dfrapSysPPPSupported": dfrapSysPPPSupported,
       "dfrapSysRDOSupported": dfrapSysRDOSupported,
       "dfrapSysETHSupported": dfrapSysETHSupported,
       "dfrapSysTKRSupported": dfrapSysTKRSupported,
       "dfrapSysExtTimSupported": dfrapSysExtTimSupported,
       "dfrapSysBRISupported": dfrapSysBRISupported,
       "dfrapSysSelDTESupported": dfrapSysSelDTESupported,
       "dfrapSysMLSupported": dfrapSysMLSupported,
       "dfrapSysNumDlcisSupported": dfrapSysNumDlcisSupported,
       "dfrapSysLTFNumDlcis": dfrapSysLTFNumDlcis,
       "dfrapSysLTFNumProtocols": dfrapSysLTFNumProtocols,
       "dfrapSysNumUserProtocols": dfrapSysNumUserProtocols,
       "dfrapSysNumSnmpMgrs": dfrapSysNumSnmpMgrs,
       "dfrapSysNumDlciNames": dfrapSysNumDlciNames,
       "dfrapConfiguration": dfrapConfiguration,
       "dfrapCfgMgmtTable": dfrapCfgMgmtTable,
       "dfrapCfgIpTable": dfrapCfgIpTable,
       "dfrapCfgIpMyIP": dfrapCfgIpMyIP,
       "dfrapCfgIpPeerIP": dfrapCfgIpPeerIP,
       "dfrapCfgIpMask": dfrapCfgIpMask,
       "dfrapCfgIpMaxMTU": dfrapCfgIpMaxMTU,
       "dfrapCfgIpChannel": dfrapCfgIpChannel,
       "dfrapCfgIpTelnetEnable": dfrapCfgIpTelnetEnable,
       "dfrapCfgIpTelnetAutoLogOut": dfrapCfgIpTelnetAutoLogOut,
       "dfrapCfgTftpTable": dfrapCfgTftpTable,
       "dfrapCfgTftpInitiate": dfrapCfgTftpInitiate,
       "dfrapCfgTftpIpAddress": dfrapCfgTftpIpAddress,
       "dfrapCfgTftpFilename": dfrapCfgTftpFilename,
       "dfrapCfgTftpInterface": dfrapCfgTftpInterface,
       "dfrapCfgTftpDlci": dfrapCfgTftpDlci,
       "dfrapCfgTftpStatus": dfrapCfgTftpStatus,
       "dfrapCfgTftpNumBytes": dfrapCfgTftpNumBytes,
       "dfrapCfgSnmpTable": dfrapCfgSnmpTable,
       "dfrapCfgSnmpFrTrap": dfrapCfgSnmpFrTrap,
       "dfrapCfgSnmpMgrTable": dfrapCfgSnmpMgrTable,
       "dfrapCfgSnmpMgrEntry": dfrapCfgSnmpMgrEntry,
       "dfrapCfgSnmpMgrIndex": dfrapCfgSnmpMgrIndex,
       "dfrapCfgSnmpMgrIP": dfrapCfgSnmpMgrIP,
       "dfrapCfgSnmpMgrInterface": dfrapCfgSnmpMgrInterface,
       "dfrapCfgSnmpMgrDlci": dfrapCfgSnmpMgrDlci,
       "dfrapCfgSnmpTrapMuting": dfrapCfgSnmpTrapMuting,
       "dfrapCfgSnmpUtilTrapEnable": dfrapCfgSnmpUtilTrapEnable,
       "dfrapCfgSnmpMgrClearN": dfrapCfgSnmpMgrClearN,
       "dfrapCfgCommTable": dfrapCfgCommTable,
       "dfrapCfgCommMode": dfrapCfgCommMode,
       "dfrapCfgCommBaud": dfrapCfgCommBaud,
       "dfrapCfgCommDataBits": dfrapCfgCommDataBits,
       "dfrapCfgCommStopBits": dfrapCfgCommStopBits,
       "dfrapCfgCommParity": dfrapCfgCommParity,
       "dfrapCfgCommFlowCtrl": dfrapCfgCommFlowCtrl,
       "dfrapCfgFrDLCITable": dfrapCfgFrDLCITable,
       "dfrapCfgFrDLCIMode": dfrapCfgFrDLCIMode,
       "dfrapCfgFrDLCIValue": dfrapCfgFrDLCIValue,
       "dfrapCfgFrDLCIEncap": dfrapCfgFrDLCIEncap,
       "dfrapCfgFrDLCIMgmtDE": dfrapCfgFrDLCIMgmtDE,
       "dfrapCfgAppTable": dfrapCfgAppTable,
       "dfrapCfgAppClockSource": dfrapCfgAppClockSource,
       "dfrapCfgAppCircuitId": dfrapCfgAppCircuitId,
       "dfrapCfgAppType": dfrapCfgAppType,
       "dfrapCfgAppFormat": dfrapCfgAppFormat,
       "dfrapCfgAppLpbkTimeout": dfrapCfgAppLpbkTimeout,
       "dfrapCfgAppPerfBuffLimit": dfrapCfgAppPerfBuffLimit,
       "dfrapCfgDdsTable": dfrapCfgDdsTable,
       "dfrapCfgDdsLoopRate": dfrapCfgDdsLoopRate,
       "dfrapCfgDdsBPVThresholding": dfrapCfgDdsBPVThresholding,
       "dfrapCfgDteTable": dfrapCfgDteTable,
       "dfrapCfgDteIntfType": dfrapCfgDteIntfType,
       "dfrapCfgDteClockMode": dfrapCfgDteClockMode,
       "dfrapCfgDteTiming": dfrapCfgDteTiming,
       "dfrapCfgDteRts": dfrapCfgDteRts,
       "dfrapCfgDteDtr": dfrapCfgDteDtr,
       "dfrapCfgDteDcdOutput": dfrapCfgDteDcdOutput,
       "dfrapCfgDteDsrOutput": dfrapCfgDteDsrOutput,
       "dfrapCfgDteCtsOutput": dfrapCfgDteCtsOutput,
       "dfrapCfgFrTable": dfrapCfgFrTable,
       "dfrapCfgFrAddrLen": dfrapCfgFrAddrLen,
       "dfrapCfgFrCrcMode": dfrapCfgFrCrcMode,
       "dfrapCfgFrLmiType": dfrapCfgFrLmiType,
       "dfrapCfgFrLmiInactivityTimeout": dfrapCfgFrLmiInactivityTimeout,
       "dfrapCfgFrLmiKeepaliveTimeout": dfrapCfgFrLmiKeepaliveTimeout,
       "dfrapCfgFrAddrResMode": dfrapCfgFrAddrResMode,
       "dfrapCfgFrAddrResInarpTimer": dfrapCfgFrAddrResInarpTimer,
       "dfrapCfgFrLmiFullStatus": dfrapCfgFrLmiFullStatus,
       "dfrapCfgFrAddrResDlcis": dfrapCfgFrAddrResDlcis,
       "dfrapCfgVnipTable": dfrapCfgVnipTable,
       "dfrapCfgVnipMode": dfrapCfgVnipMode,
       "dfrapCfgVnipInitTimer": dfrapCfgVnipInitTimer,
       "dfrapCfgVnipKeepAliveTimer": dfrapCfgVnipKeepAliveTimer,
       "dfrapCfgVnipInactivityTimer": dfrapCfgVnipInactivityTimer,
       "dfrapCfgVnipTransitDelayFrequency": dfrapCfgVnipTransitDelayFrequency,
       "dfrapCfgTransitDelayTable": dfrapCfgTransitDelayTable,
       "dfrapCfgTransitDelayEntry": dfrapCfgTransitDelayEntry,
       "dfrapCfgTransitDelayInterface": dfrapCfgTransitDelayInterface,
       "dfrapCfgTransitDelayDlciValue": dfrapCfgTransitDelayDlciValue,
       "dfrapCfgTransitDelayNumHops": dfrapCfgTransitDelayNumHops,
       "dfrapCfgTransitDelayRcvSummaryCancel": dfrapCfgTransitDelayRcvSummaryCancel,
       "dfrapCfgTransitDelayThreshold": dfrapCfgTransitDelayThreshold,
       "dfrapCfgTDDeleteTable": dfrapCfgTDDeleteTable,
       "dfrapCfgTDDeleteEntry": dfrapCfgTDDeleteEntry,
       "dfrapCfgTDDeleteInterface": dfrapCfgTDDeleteInterface,
       "dfrapCfgTDDeleteDlciValue": dfrapCfgTDDeleteDlciValue,
       "dfrapCfgTransitDelayTableClear": dfrapCfgTransitDelayTableClear,
       "dfrapCfgFrPerf": dfrapCfgFrPerf,
       "dfrapCfgFrPerfDlciNamesTable": dfrapCfgFrPerfDlciNamesTable,
       "dfrapCfgFrPerfDlciNamesEntry": dfrapCfgFrPerfDlciNamesEntry,
       "dfrapCfgFrPerfDlciNamesDlciValue": dfrapCfgFrPerfDlciNamesDlciValue,
       "dfrapCfgFrPerfDlciNamesDlciName": dfrapCfgFrPerfDlciNamesDlciName,
       "dfrapCfgFrPerfDlciNamesCirValue": dfrapCfgFrPerfDlciNamesCirValue,
       "dfrapCfgFrPerfDlciNamesCirType": dfrapCfgFrPerfDlciNamesCirType,
       "dfrapCfgFrPerfDlciNamesUtilThreshold": dfrapCfgFrPerfDlciNamesUtilThreshold,
       "dfrapCfgFrPerfDlciNamesEirValue": dfrapCfgFrPerfDlciNamesEirValue,
       "dfrapCfgFrPerfDlciNamesDelete": dfrapCfgFrPerfDlciNamesDelete,
       "dfrapCfgFrPerfTimers": dfrapCfgFrPerfTimers,
       "dfrapCfgFrPerfTimersSTInterval": dfrapCfgFrPerfTimersSTInterval,
       "dfrapCfgFrPerfTimersLTInterval": dfrapCfgFrPerfTimersLTInterval,
       "dfrapCfgFrPerfUserProtocolsTable": dfrapCfgFrPerfUserProtocolsTable,
       "dfrapCfgFrPerfUserProtocolsEntry": dfrapCfgFrPerfUserProtocolsEntry,
       "dfrapCfgFrPerfUserProtocolsIndex": dfrapCfgFrPerfUserProtocolsIndex,
       "dfrapCfgFrPerfUserProtocolsPortNum": dfrapCfgFrPerfUserProtocolsPortNum,
       "dfrapCfgFrPerfLTDlciFilterTable": dfrapCfgFrPerfLTDlciFilterTable,
       "dfrapCfgFrPerfLTDlciFilterEntry": dfrapCfgFrPerfLTDlciFilterEntry,
       "dfrapCfgFrPerfLTDlciFilterIndex": dfrapCfgFrPerfLTDlciFilterIndex,
       "dfrapCfgFrPerfLTDlciFilterDlciNum": dfrapCfgFrPerfLTDlciFilterDlciNum,
       "dfrapCfgFrPerfLTProtocolFilterTable": dfrapCfgFrPerfLTProtocolFilterTable,
       "dfrapCfgFrPerfLTProtocolFilterEntry": dfrapCfgFrPerfLTProtocolFilterEntry,
       "dfrapCfgFrPerfLTProtocolFilterIndex": dfrapCfgFrPerfLTProtocolFilterIndex,
       "dfrapCfgFrPerfLTProtocolFilterProtocol": dfrapCfgFrPerfLTProtocolFilterProtocol,
       "dfrapCfgFrPerfDlciDefaultUtilThreshold": dfrapCfgFrPerfDlciDefaultUtilThreshold,
       "dfrapCfgFrPerfDlciUtilDuration": dfrapCfgFrPerfDlciUtilDuration,
       "dfrapCfgFrPerfDlciNamesTableClear": dfrapCfgFrPerfDlciNamesTableClear,
       "dfrapCfgFrPerfUserProtocolsTableClear": dfrapCfgFrPerfUserProtocolsTableClear,
       "dfrapCfgFrPerfLTDlciFilterTableClear": dfrapCfgFrPerfLTDlciFilterTableClear,
       "dfrapCfgFrPerfLTProtocolFilterTableClear": dfrapCfgFrPerfLTProtocolFilterTableClear,
       "dfrapCfgFrPerfUnprovDlcisDelete": dfrapCfgFrPerfUnprovDlcisDelete,
       "dfrapCfgSecurityTable": dfrapCfgSecurityTable,
       "dfrapCfgTelnetCliLcdPassword": dfrapCfgTelnetCliLcdPassword,
       "dfrapCfgTftpPassword": dfrapCfgTftpPassword,
       "dfrapCfgCliPassword": dfrapCfgCliPassword,
       "dfrapCfgLcdPassword": dfrapCfgLcdPassword,
       "dfrapCfgGetCommunityString": dfrapCfgGetCommunityString,
       "dfrapCfgSetCommunityString": dfrapCfgSetCommunityString,
       "dfrapCfgLock": dfrapCfgLock,
       "dfrapCfgLockID": dfrapCfgLockID,
       "dfrapCfgID": dfrapCfgID,
       "dfrapCfgStatus": dfrapCfgStatus,
       "dfrapCfgUnlock": dfrapCfgUnlock,
       "dfrapCfgUpdate": dfrapCfgUpdate,
       "dfrapDiagnostics": dfrapDiagnostics,
       "dfrapDiagUnitTable": dfrapDiagUnitTable,
       "dfrapDiagUnitLocLoop": dfrapDiagUnitLocLoop,
       "dfrapDiagUnitReset": dfrapDiagUnitReset,
       "dfrapDiagUnitTimeRemaining": dfrapDiagUnitTimeRemaining,
       "dfrapDiagDdsTable": dfrapDiagDdsTable,
       "dfrapDiagDdsLclLpbk": dfrapDiagDdsLclLpbk,
       "dfrapDiagDdsRmtLpbk": dfrapDiagDdsRmtLpbk,
       "dfrapDiagDdsTimeRemaining": dfrapDiagDdsTimeRemaining,
       "dfrapDiagDteTable": dfrapDiagDteTable,
       "dfrapDiagDteLclLpbk": dfrapDiagDteLclLpbk,
       "dfrapDiagDteV54Lpbk": dfrapDiagDteV54Lpbk,
       "dfrapDiagDteRmtV54Lpbk": dfrapDiagDteRmtV54Lpbk,
       "dfrapDiagDteTimeRemaining": dfrapDiagDteTimeRemaining,
       "dfrapDiagBertTable": dfrapDiagBertTable,
       "dfrapDiagBertState": dfrapDiagBertState,
       "dfrapDiagBertStatus": dfrapDiagBertStatus,
       "dfrapDiagBertErrors": dfrapDiagBertErrors,
       "dfrapDiagBertErrSec": dfrapDiagBertErrSec,
       "dfrapDiagBertTimeElaps": dfrapDiagBertTimeElaps,
       "dfrapDiagBertResyncs": dfrapDiagBertResyncs,
       "dfrapDiagBertPattern": dfrapDiagBertPattern,
       "dfrapDiagVnipTable": dfrapDiagVnipTable,
       "dfrapDiagVnipEntry": dfrapDiagVnipEntry,
       "dfrapDiagVnipInterface": dfrapDiagVnipInterface,
       "dfrapDiagVnipIndex": dfrapDiagVnipIndex,
       "dfrapDiagVnipDlci": dfrapDiagVnipDlci,
       "dfrapDiagVnipIpAddr": dfrapDiagVnipIpAddr,
       "dfrapDiagVLOOP": dfrapDiagVLOOP,
       "dfrapDiagVBERT": dfrapDiagVBERT,
       "dfrapDiagVBERTRate": dfrapDiagVBERTRate,
       "dfrapDiagVBERTSize": dfrapDiagVBERTSize,
       "dfrapDiagVBERTPktPercent": dfrapDiagVBERTPktPercent,
       "dfrapDiagVBERTTestPeriod": dfrapDiagVBERTTestPeriod,
       "dfrapStatus": dfrapStatus,
       "dfrapVnipTopologyTable": dfrapVnipTopologyTable,
       "dfrapVnipTopologyEntry": dfrapVnipTopologyEntry,
       "dfrapVnipTopologyInterface": dfrapVnipTopologyInterface,
       "dfrapVnipTopologyIndex": dfrapVnipTopologyIndex,
       "dfrapVnipTopologyDlci": dfrapVnipTopologyDlci,
       "dfrapVnipTopologyIpAddr": dfrapVnipTopologyIpAddr,
       "dfrapVnipTopologyNumHops": dfrapVnipTopologyNumHops,
       "dfrapVnipTopologyLocalDlci": dfrapVnipTopologyLocalDlci,
       "dfrapVnipTopoTDNumSamples": dfrapVnipTopoTDNumSamples,
       "dfrapVnipTopoTDAvgDelay": dfrapVnipTopoTDAvgDelay,
       "dfrapVnipTopoTDMaxDelay": dfrapVnipTopoTDMaxDelay,
       "dfrapVnipTopoTDMinDelay": dfrapVnipTopoTDMinDelay,
       "dfrapVnipTopoTDLastDelay": dfrapVnipTopoTDLastDelay,
       "dfrapVnipTopoVLOOPStatus": dfrapVnipTopoVLOOPStatus,
       "dfrapVnipTopoVBERTStatus": dfrapVnipTopoVBERTStatus,
       "dfrapVnipTopoVBertTxDESetFrames": dfrapVnipTopoVBertTxDESetFrames,
       "dfrapVnipTopoVBertRxDESetFrames": dfrapVnipTopoVBertRxDESetFrames,
       "dfrapVnipTopoVBertTxDEClrFrames": dfrapVnipTopoVBertTxDEClrFrames,
       "dfrapVnipTopoVBertRxDEClrFrames": dfrapVnipTopoVBertRxDEClrFrames,
       "dfrapVnipTopoVBertTransitDelayMax": dfrapVnipTopoVBertTransitDelayMax,
       "dfrapVnipTopoVBertTransitDelayAvg": dfrapVnipTopoVBertTransitDelayAvg,
       "dfrapVnipTopoVBertTimeElapse": dfrapVnipTopoVBertTimeElapse,
       "dfrapVnipTopoVBertPerUtilCIR": dfrapVnipTopoVBertPerUtilCIR,
       "dfrapVnipTopoVBertPerUtilEIR": dfrapVnipTopoVBertPerUtilEIR,
       "dfrapStatusMgmtTable": dfrapStatusMgmtTable,
       "dfrapStatusMgmtChannel": dfrapStatusMgmtChannel,
       "dfrapStatusMgmtInterface": dfrapStatusMgmtInterface,
       "dfrapStatusMgmtInterfaceStatus": dfrapStatusMgmtInterfaceStatus,
       "dfrapStatusMgmtDefaultDLCINo": dfrapStatusMgmtDefaultDLCINo,
       "dfrapStatusMgmtDefaultDLCIStatus": dfrapStatusMgmtDefaultDLCIStatus,
       "dfrapStatusLedTable": dfrapStatusLedTable,
       "dfrapStatusDteModeLED": dfrapStatusDteModeLED,
       "dfrapStatusDteStatusLED": dfrapStatusDteStatusLED,
       "dfrapStatusDteTxLED": dfrapStatusDteTxLED,
       "dfrapStatusDteRxLED": dfrapStatusDteRxLED,
       "dfrapStatusDdsModeLED": dfrapStatusDdsModeLED,
       "dfrapStatusDdsStatusLED": dfrapStatusDdsStatusLED,
       "dfrapStatusAllLEDs": dfrapStatusAllLEDs,
       "dfrapVnipTransitDelayClear": dfrapVnipTransitDelayClear,
       "dfrapLmiSourcing": dfrapLmiSourcing,
       "dfrapStatusDteTable": dfrapStatusDteTable,
       "dfrapStatusDteMode": dfrapStatusDteMode,
       "dfrapStatusDteRts": dfrapStatusDteRts,
       "dfrapStatusDteDtr": dfrapStatusDteDtr,
       "dfrapStatusDteDcd": dfrapStatusDteDcd,
       "dfrapStatusDteDsr": dfrapStatusDteDsr,
       "dfrapStatusDteCts": dfrapStatusDteCts,
       "dfrapStatusDdsTable": dfrapStatusDdsTable,
       "dfrapStatusDdsLineStatus": dfrapStatusDdsLineStatus,
       "dfrapStatusDdsLoopLength": dfrapStatusDdsLoopLength,
       "dfrapVBertClear": dfrapVBertClear,
       "dfrapStatusLmiAutosense": dfrapStatusLmiAutosense,
       "dfrapPerformance": dfrapPerformance,
       "dfrapPerfMgmtIp": dfrapPerfMgmtIp,
       "dfrapPerfMgmtIpIFStatsTable": dfrapPerfMgmtIpIFStatsTable,
       "dfrapPerfMgmtIpIFInOctets": dfrapPerfMgmtIpIFInOctets,
       "dfrapPerfMgmtIpIFInErrors": dfrapPerfMgmtIpIFInErrors,
       "dfrapPerfMgmtIpIFOutOctets": dfrapPerfMgmtIpIFOutOctets,
       "dfrapPerfMgmtIpIFOperStatus": dfrapPerfMgmtIpIFOperStatus,
       "dfrapPerfMgmtIpIPStatsTable": dfrapPerfMgmtIpIPStatsTable,
       "dfrapPerfMgmtIpIPInRcv": dfrapPerfMgmtIpIPInRcv,
       "dfrapPerfMgmtIpIPInHdrErr": dfrapPerfMgmtIpIPInHdrErr,
       "dfrapPerfMgmtIpIPInAddrErr": dfrapPerfMgmtIpIPInAddrErr,
       "dfrapPerfMgmtIpIPInProtUnk": dfrapPerfMgmtIpIPInProtUnk,
       "dfrapPerfMgmtIpIPInDscrd": dfrapPerfMgmtIpIPInDscrd,
       "dfrapPerfMgmtIpIPInDlvrs": dfrapPerfMgmtIpIPInDlvrs,
       "dfrapPerfMgmtIpIPOutRqst": dfrapPerfMgmtIpIPOutRqst,
       "dfrapPerfMgmtIpIPOutDscrd": dfrapPerfMgmtIpIPOutDscrd,
       "dfrapPerfMgmtIpIPOutNoRt": dfrapPerfMgmtIpIPOutNoRt,
       "dfrapPerfMgmtIpICMPStatsTable": dfrapPerfMgmtIpICMPStatsTable,
       "dfrapPerfMgmtIpICMPInMsgs": dfrapPerfMgmtIpICMPInMsgs,
       "dfrapPerfMgmtIpICMPInErrors": dfrapPerfMgmtIpICMPInErrors,
       "dfrapPerfMgmtIpICMPInDestUnreachs": dfrapPerfMgmtIpICMPInDestUnreachs,
       "dfrapPerfMgmtIpICMPInTimeExcds": dfrapPerfMgmtIpICMPInTimeExcds,
       "dfrapPerfMgmtIpICMPInParmProbs": dfrapPerfMgmtIpICMPInParmProbs,
       "dfrapPerfMgmtIpICMPInRedirects": dfrapPerfMgmtIpICMPInRedirects,
       "dfrapPerfMgmtIpICMPInEchos": dfrapPerfMgmtIpICMPInEchos,
       "dfrapPerfMgmtIpICMPInEchoReps": dfrapPerfMgmtIpICMPInEchoReps,
       "dfrapPerfMgmtIpICMPOutMsgs": dfrapPerfMgmtIpICMPOutMsgs,
       "dfrapPerfMgmtIpICMPOutErrors": dfrapPerfMgmtIpICMPOutErrors,
       "dfrapPerfMgmtIpICMPOutDestUnreachs": dfrapPerfMgmtIpICMPOutDestUnreachs,
       "dfrapPerfMgmtIpICMPOutParmProbs": dfrapPerfMgmtIpICMPOutParmProbs,
       "dfrapPerfMgmtIpICMPOutRedirects": dfrapPerfMgmtIpICMPOutRedirects,
       "dfrapPerfMgmtIpICMPOutEchos": dfrapPerfMgmtIpICMPOutEchos,
       "dfrapPerfMgmtIpICMPOutEchoReps": dfrapPerfMgmtIpICMPOutEchoReps,
       "dfrapPerfMgmtIpUDPStatsTable": dfrapPerfMgmtIpUDPStatsTable,
       "dfrapPerfMgmtIpUDPInDatagrams": dfrapPerfMgmtIpUDPInDatagrams,
       "dfrapPerfMgmtIpUDPOutDatagrams": dfrapPerfMgmtIpUDPOutDatagrams,
       "dfrapPerfMgmtIpUDPNoPorts": dfrapPerfMgmtIpUDPNoPorts,
       "dfrapPerfMgmtIpTCPStatsTable": dfrapPerfMgmtIpTCPStatsTable,
       "dfrapPerfMgmtIpTCPActiveOpens": dfrapPerfMgmtIpTCPActiveOpens,
       "dfrapPerfMgmtIpTCPPassiveOpens": dfrapPerfMgmtIpTCPPassiveOpens,
       "dfrapPerfMgmtIpTCPAttemptFails": dfrapPerfMgmtIpTCPAttemptFails,
       "dfrapPerfMgmtIpTCPCurrEstab": dfrapPerfMgmtIpTCPCurrEstab,
       "dfrapPerfMgmtIpTCPInSegs": dfrapPerfMgmtIpTCPInSegs,
       "dfrapPerfMgmtIpTCPOutSegs": dfrapPerfMgmtIpTCPOutSegs,
       "dfrapPerfThruput": dfrapPerfThruput,
       "dfrapPerfThruputPerIntfTable": dfrapPerfThruputPerIntfTable,
       "dfrapPerfThruputPerIntfEntry": dfrapPerfThruputPerIntfEntry,
       "dfrapPerfThruputPerIntfIndex": dfrapPerfThruputPerIntfIndex,
       "dfrapPerfThruputPerIntfRxByteCnt": dfrapPerfThruputPerIntfRxByteCnt,
       "dfrapPerfThruputPerIntfTxByteCnt": dfrapPerfThruputPerIntfTxByteCnt,
       "dfrapPerfThruputPerIntfRxFrameCnt": dfrapPerfThruputPerIntfRxFrameCnt,
       "dfrapPerfThruputPerIntfTxFrameCnt": dfrapPerfThruputPerIntfTxFrameCnt,
       "dfrapPerfThruputPerIntfRxCrcErrCnt": dfrapPerfThruputPerIntfRxCrcErrCnt,
       "dfrapPerfThruputPerIntfRxAbortCnt": dfrapPerfThruputPerIntfRxAbortCnt,
       "dfrapPerfThruputPerIntfRxBpvCnt": dfrapPerfThruputPerIntfRxBpvCnt,
       "dfrapPerfThruputPerDlciTable": dfrapPerfThruputPerDlciTable,
       "dfrapPerfThruputPerDlciEntry": dfrapPerfThruputPerDlciEntry,
       "dfrapPerfThruputPerDlciIndex": dfrapPerfThruputPerDlciIndex,
       "dfrapPerfThruputPerDlciValue": dfrapPerfThruputPerDlciValue,
       "dfrapPerfThruputPerDlciCreateTime": dfrapPerfThruputPerDlciCreateTime,
       "dfrapPerfThruputPerDlciChangeTime": dfrapPerfThruputPerDlciChangeTime,
       "dfrapPerfThruputPerDlciRxByte": dfrapPerfThruputPerDlciRxByte,
       "dfrapPerfThruputPerDlciTxByte": dfrapPerfThruputPerDlciTxByte,
       "dfrapPerfThruputPerDlciRxFrame": dfrapPerfThruputPerDlciRxFrame,
       "dfrapPerfThruputPerDlciTxFrame": dfrapPerfThruputPerDlciTxFrame,
       "dfrapPerfThruputPerDlciRxFecn": dfrapPerfThruputPerDlciRxFecn,
       "dfrapPerfThruputPerDlciRxBecn": dfrapPerfThruputPerDlciRxBecn,
       "dfrapPerfThruputPerDlciRxDe": dfrapPerfThruputPerDlciRxDe,
       "dfrapPerfThruputPerDlciTxDe": dfrapPerfThruputPerDlciTxDe,
       "dfrapPerfThruputPerDlciRxThruput": dfrapPerfThruputPerDlciRxThruput,
       "dfrapPerfThruputPerDlciTxThruput": dfrapPerfThruputPerDlciTxThruput,
       "dfrapPerfThruputPerDlciCIR": dfrapPerfThruputPerDlciCIR,
       "dfrapPerfThruputPerDlciUptime": dfrapPerfThruputPerDlciUptime,
       "dfrapPerfThruputPerDlciDowntime": dfrapPerfThruputPerDlciDowntime,
       "dfrapPerfThruputPerDlciCirType": dfrapPerfThruputPerDlciCirType,
       "dfrapPerfThruputPerDlciPvcState": dfrapPerfThruputPerDlciPvcState,
       "dfrapPerfThruputPerDlciOutageCount": dfrapPerfThruputPerDlciOutageCount,
       "dfrapPerfThruputPerDlciAvailability": dfrapPerfThruputPerDlciAvailability,
       "dfrapPerfThruputPerDlciMTBSO": dfrapPerfThruputPerDlciMTBSO,
       "dfrapPerfThruputPerDlciMTTSR": dfrapPerfThruputPerDlciMTTSR,
       "dfrapPerfThruputPerDlciEncapType": dfrapPerfThruputPerDlciEncapType,
       "dfrapPerfThruputPerDlciRxUtilizationStatus": dfrapPerfThruputPerDlciRxUtilizationStatus,
       "dfrapPerfThruputPerDlciTxUtilizationStatus": dfrapPerfThruputPerDlciTxUtilizationStatus,
       "dfrapPerfThruputPerDlciEIR": dfrapPerfThruputPerDlciEIR,
       "dfrapPerfThruputCommands": dfrapPerfThruputCommands,
       "dfrapPerfThruputCmdClearDteStats": dfrapPerfThruputCmdClearDteStats,
       "dfrapPerfThruputCmdClearDdsStats": dfrapPerfThruputCmdClearDdsStats,
       "dfrapPerfThruputCmdClearAllIntfStats": dfrapPerfThruputCmdClearAllIntfStats,
       "dfrapPerfThruputCmdClearDlciStats": dfrapPerfThruputCmdClearDlciStats,
       "dfrapPerfThruputCmdClearAllStats": dfrapPerfThruputCmdClearAllStats,
       "dfrapPerfThruputCmdRemoveStsDlci": dfrapPerfThruputCmdRemoveStsDlci,
       "dfrapPerfThruputCmdReplaceDlciTable": dfrapPerfThruputCmdReplaceDlciTable,
       "dfrapPerfThruputCmdReplaceDlciEntry": dfrapPerfThruputCmdReplaceDlciEntry,
       "dfrapPerfThruputCmdReplaceDlciValue": dfrapPerfThruputCmdReplaceDlciValue,
       "dfrapPerfThruputCmdReplaceDlciNewValue": dfrapPerfThruputCmdReplaceDlciNewValue,
       "dfrapPerfThruputCmdAvailabilityStsDlciReset": dfrapPerfThruputCmdAvailabilityStsDlciReset,
       "dfrapPerfThruputCmdAvailabilityStsDlciResetAll": dfrapPerfThruputCmdAvailabilityStsDlciResetAll,
       "dfrapPerfThruputCmdCountsStsDlciReset": dfrapPerfThruputCmdCountsStsDlciReset,
       "dfrapPerfThruputCmdCountsStsDlciResetAll": dfrapPerfThruputCmdCountsStsDlciResetAll,
       "dfrapPerfThruputCmdAllStsDlciReset": dfrapPerfThruputCmdAllStsDlciReset,
       "dfrapPerfThruputCmdAllStsDlciResetAll": dfrapPerfThruputCmdAllStsDlciResetAll,
       "dfrapPerfNetworkShortTerm": dfrapPerfNetworkShortTerm,
       "dfrapPerfNetwProtoPerDlciTable": dfrapPerfNetwProtoPerDlciTable,
       "dfrapPerfNetwProtoPerDlciEntry": dfrapPerfNetwProtoPerDlciEntry,
       "dfrapPerfNetwProtoPerDlciInterval": dfrapPerfNetwProtoPerDlciInterval,
       "dfrapPerfNetwProtoPerDlciValue": dfrapPerfNetwProtoPerDlciValue,
       "dfrapPerfNetwProtoPerDlciRxTotal": dfrapPerfNetwProtoPerDlciRxTotal,
       "dfrapPerfNetwProtoPerDlciTxTotal": dfrapPerfNetwProtoPerDlciTxTotal,
       "dfrapPerfNetwProtoPerDlciRxIp": dfrapPerfNetwProtoPerDlciRxIp,
       "dfrapPerfNetwProtoPerDlciTxIp": dfrapPerfNetwProtoPerDlciTxIp,
       "dfrapPerfNetwProtoPerDlciRxIpx": dfrapPerfNetwProtoPerDlciRxIpx,
       "dfrapPerfNetwProtoPerDlciTxIpx": dfrapPerfNetwProtoPerDlciTxIpx,
       "dfrapPerfNetwProtoPerDlciRxSna": dfrapPerfNetwProtoPerDlciRxSna,
       "dfrapPerfNetwProtoPerDlciTxSna": dfrapPerfNetwProtoPerDlciTxSna,
       "dfrapPerfNetwProtoPerDlciRxArp": dfrapPerfNetwProtoPerDlciRxArp,
       "dfrapPerfNetwProtoPerDlciTxArp": dfrapPerfNetwProtoPerDlciTxArp,
       "dfrapPerfNetwProtoPerDlciRxCisco": dfrapPerfNetwProtoPerDlciRxCisco,
       "dfrapPerfNetwProtoPerDlciTxCisco": dfrapPerfNetwProtoPerDlciTxCisco,
       "dfrapPerfNetwProtoPerDlciRxOther": dfrapPerfNetwProtoPerDlciRxOther,
       "dfrapPerfNetwProtoPerDlciTxOther": dfrapPerfNetwProtoPerDlciTxOther,
       "dfrapPerfNetwProtoPerDlciRxVnip": dfrapPerfNetwProtoPerDlciRxVnip,
       "dfrapPerfNetwProtoPerDlciTxVnip": dfrapPerfNetwProtoPerDlciTxVnip,
       "dfrapPerfNetwProtoPerDlciRxAnnexG": dfrapPerfNetwProtoPerDlciRxAnnexG,
       "dfrapPerfNetwProtoPerDlciTxAnnexG": dfrapPerfNetwProtoPerDlciTxAnnexG,
       "dfrapPerfNetwProtoTotalTable": dfrapPerfNetwProtoTotalTable,
       "dfrapPerfNetwProtoTotalEntry": dfrapPerfNetwProtoTotalEntry,
       "dfrapPerfNetwProtoTotalInterval": dfrapPerfNetwProtoTotalInterval,
       "dfrapPerfNetwProtoTotalRxTotal": dfrapPerfNetwProtoTotalRxTotal,
       "dfrapPerfNetwProtoTotalTxTotal": dfrapPerfNetwProtoTotalTxTotal,
       "dfrapPerfNetwProtoTotalRxIp": dfrapPerfNetwProtoTotalRxIp,
       "dfrapPerfNetwProtoTotalTxIp": dfrapPerfNetwProtoTotalTxIp,
       "dfrapPerfNetwProtoTotalRxIpx": dfrapPerfNetwProtoTotalRxIpx,
       "dfrapPerfNetwProtoTotalTxIpx": dfrapPerfNetwProtoTotalTxIpx,
       "dfrapPerfNetwProtoTotalRxSna": dfrapPerfNetwProtoTotalRxSna,
       "dfrapPerfNetwProtoTotalTxSna": dfrapPerfNetwProtoTotalTxSna,
       "dfrapPerfNetwProtoTotalRxArp": dfrapPerfNetwProtoTotalRxArp,
       "dfrapPerfNetwProtoTotalTxArp": dfrapPerfNetwProtoTotalTxArp,
       "dfrapPerfNetwProtoTotalRxCisco": dfrapPerfNetwProtoTotalRxCisco,
       "dfrapPerfNetwProtoTotalTxCisco": dfrapPerfNetwProtoTotalTxCisco,
       "dfrapPerfNetwProtoTotalRxOther": dfrapPerfNetwProtoTotalRxOther,
       "dfrapPerfNetwProtoTotalTxOther": dfrapPerfNetwProtoTotalTxOther,
       "dfrapPerfNetwProtoTotalRxVnip": dfrapPerfNetwProtoTotalRxVnip,
       "dfrapPerfNetwProtoTotalTxVnip": dfrapPerfNetwProtoTotalTxVnip,
       "dfrapPerfNetwProtoTotalRxAnnexG": dfrapPerfNetwProtoTotalRxAnnexG,
       "dfrapPerfNetwProtoTotalTxAnnexG": dfrapPerfNetwProtoTotalTxAnnexG,
       "dfrapPerfIpPerDlciTable": dfrapPerfIpPerDlciTable,
       "dfrapPerfIpPerDlciEntry": dfrapPerfIpPerDlciEntry,
       "dfrapPerfIpPerDlciInterval": dfrapPerfIpPerDlciInterval,
       "dfrapPerfIpPerDlciValue": dfrapPerfIpPerDlciValue,
       "dfrapPerfIpPerDlciRxTotal": dfrapPerfIpPerDlciRxTotal,
       "dfrapPerfIpPerDlciTxTotal": dfrapPerfIpPerDlciTxTotal,
       "dfrapPerfIpPerDlciRxTcp": dfrapPerfIpPerDlciRxTcp,
       "dfrapPerfIpPerDlciTxTcp": dfrapPerfIpPerDlciTxTcp,
       "dfrapPerfIpPerDlciRxUdp": dfrapPerfIpPerDlciRxUdp,
       "dfrapPerfIpPerDlciTxUdp": dfrapPerfIpPerDlciTxUdp,
       "dfrapPerfIpPerDlciRxIcmp": dfrapPerfIpPerDlciRxIcmp,
       "dfrapPerfIpPerDlciTxIcmp": dfrapPerfIpPerDlciTxIcmp,
       "dfrapPerfIpPerDlciRxOther": dfrapPerfIpPerDlciRxOther,
       "dfrapPerfIpPerDlciTxOther": dfrapPerfIpPerDlciTxOther,
       "dfrapPerfIpPerDlciRxIgrp": dfrapPerfIpPerDlciRxIgrp,
       "dfrapPerfIpPerDlciTxIgrp": dfrapPerfIpPerDlciTxIgrp,
       "dfrapPerfIpTotalTable": dfrapPerfIpTotalTable,
       "dfrapPerfIpTotalEntry": dfrapPerfIpTotalEntry,
       "dfrapPerfIpTotalInterval": dfrapPerfIpTotalInterval,
       "dfrapPerfIpTotalRxTotal": dfrapPerfIpTotalRxTotal,
       "dfrapPerfIpTotalTxTotal": dfrapPerfIpTotalTxTotal,
       "dfrapPerfIpTotalRxTcp": dfrapPerfIpTotalRxTcp,
       "dfrapPerfIpTotalTxTcp": dfrapPerfIpTotalTxTcp,
       "dfrapPerfIpTotalRxUdp": dfrapPerfIpTotalRxUdp,
       "dfrapPerfIpTotalTxUdp": dfrapPerfIpTotalTxUdp,
       "dfrapPerfIpTotalRxIcmp": dfrapPerfIpTotalRxIcmp,
       "dfrapPerfIpTotalTxIcmp": dfrapPerfIpTotalTxIcmp,
       "dfrapPerfIpTotalRxOther": dfrapPerfIpTotalRxOther,
       "dfrapPerfIpTotalTxOther": dfrapPerfIpTotalTxOther,
       "dfrapPerfIpTotalRxIgrp": dfrapPerfIpTotalRxIgrp,
       "dfrapPerfIpTotalTxIgrp": dfrapPerfIpTotalTxIgrp,
       "dfrapPerfIcmpPerDlciTable": dfrapPerfIcmpPerDlciTable,
       "dfrapPerfIcmpPerDlciEntry": dfrapPerfIcmpPerDlciEntry,
       "dfrapPerfIcmpPerDlciInterval": dfrapPerfIcmpPerDlciInterval,
       "dfrapPerfIcmpPerDlciValue": dfrapPerfIcmpPerDlciValue,
       "dfrapPerfIcmpPerDlciRxTotal": dfrapPerfIcmpPerDlciRxTotal,
       "dfrapPerfIcmpPerDlciTxTotal": dfrapPerfIcmpPerDlciTxTotal,
       "dfrapPerfIcmpPerDlciRxEchoRep": dfrapPerfIcmpPerDlciRxEchoRep,
       "dfrapPerfIcmpPerDlciTxEchoRep": dfrapPerfIcmpPerDlciTxEchoRep,
       "dfrapPerfIcmpPerDlciRxDestUnr": dfrapPerfIcmpPerDlciRxDestUnr,
       "dfrapPerfIcmpPerDlciTxDestUnr": dfrapPerfIcmpPerDlciTxDestUnr,
       "dfrapPerfIcmpPerDlciRxSrcQuench": dfrapPerfIcmpPerDlciRxSrcQuench,
       "dfrapPerfIcmpPerDlciTxSrcQuench": dfrapPerfIcmpPerDlciTxSrcQuench,
       "dfrapPerfIcmpPerDlciRxRedirect": dfrapPerfIcmpPerDlciRxRedirect,
       "dfrapPerfIcmpPerDlciTxRedirect": dfrapPerfIcmpPerDlciTxRedirect,
       "dfrapPerfIcmpPerDlciRxEchoReq": dfrapPerfIcmpPerDlciRxEchoReq,
       "dfrapPerfIcmpPerDlciTxEchoReq": dfrapPerfIcmpPerDlciTxEchoReq,
       "dfrapPerfIcmpPerDlciRxTimeExcd": dfrapPerfIcmpPerDlciRxTimeExcd,
       "dfrapPerfIcmpPerDlciTxTimeExcd": dfrapPerfIcmpPerDlciTxTimeExcd,
       "dfrapPerfIcmpPerDlciRxParamProb": dfrapPerfIcmpPerDlciRxParamProb,
       "dfrapPerfIcmpPerDlciTxParamProb": dfrapPerfIcmpPerDlciTxParamProb,
       "dfrapPerfIcmpPerDlciRxTimestpReq": dfrapPerfIcmpPerDlciRxTimestpReq,
       "dfrapPerfIcmpPerDlciTxTimestpReq": dfrapPerfIcmpPerDlciTxTimestpReq,
       "dfrapPerfIcmpPerDlciRxTimestpRep": dfrapPerfIcmpPerDlciRxTimestpRep,
       "dfrapPerfIcmpPerDlciTxTimestpRep": dfrapPerfIcmpPerDlciTxTimestpRep,
       "dfrapPerfIcmpPerDlciRxAddrMaskReq": dfrapPerfIcmpPerDlciRxAddrMaskReq,
       "dfrapPerfIcmpPerDlciTxAddrMaskReq": dfrapPerfIcmpPerDlciTxAddrMaskReq,
       "dfrapPerfIcmpPerDlciRxAddrMaskRep": dfrapPerfIcmpPerDlciRxAddrMaskRep,
       "dfrapPerfIcmpPerDlciTxAddrMaskRep": dfrapPerfIcmpPerDlciTxAddrMaskRep,
       "dfrapPerfIcmpPerDlciRxPktTooBig": dfrapPerfIcmpPerDlciRxPktTooBig,
       "dfrapPerfIcmpPerDlciTxPktTooBig": dfrapPerfIcmpPerDlciTxPktTooBig,
       "dfrapPerfIcmpPerDlciRxGmQuery": dfrapPerfIcmpPerDlciRxGmQuery,
       "dfrapPerfIcmpPerDlciTxGmQuery": dfrapPerfIcmpPerDlciTxGmQuery,
       "dfrapPerfIcmpPerDlciRxGmReport": dfrapPerfIcmpPerDlciRxGmReport,
       "dfrapPerfIcmpPerDlciTxGmReport": dfrapPerfIcmpPerDlciTxGmReport,
       "dfrapPerfIcmpPerDlciRxGmReduct": dfrapPerfIcmpPerDlciRxGmReduct,
       "dfrapPerfIcmpPerDlciTxGmReduct": dfrapPerfIcmpPerDlciTxGmReduct,
       "dfrapPerfIcmpTotalTable": dfrapPerfIcmpTotalTable,
       "dfrapPerfIcmpTotalEntry": dfrapPerfIcmpTotalEntry,
       "dfrapPerfIcmpTotalInterval": dfrapPerfIcmpTotalInterval,
       "dfrapPerfIcmpTotalRxTotal": dfrapPerfIcmpTotalRxTotal,
       "dfrapPerfIcmpTotalTxTotal": dfrapPerfIcmpTotalTxTotal,
       "dfrapPerfIcmpTotalRxEchoRep": dfrapPerfIcmpTotalRxEchoRep,
       "dfrapPerfIcmpTotalTxEchoRep": dfrapPerfIcmpTotalTxEchoRep,
       "dfrapPerfIcmpTotalRxDestUnr": dfrapPerfIcmpTotalRxDestUnr,
       "dfrapPerfIcmpTotalTxDestUnr": dfrapPerfIcmpTotalTxDestUnr,
       "dfrapPerfIcmpTotalRxSrcQuench": dfrapPerfIcmpTotalRxSrcQuench,
       "dfrapPerfIcmpTotalTxSrcQuench": dfrapPerfIcmpTotalTxSrcQuench,
       "dfrapPerfIcmpTotalRxRedirect": dfrapPerfIcmpTotalRxRedirect,
       "dfrapPerfIcmpTotalTxRedirect": dfrapPerfIcmpTotalTxRedirect,
       "dfrapPerfIcmpTotalRxEchoReq": dfrapPerfIcmpTotalRxEchoReq,
       "dfrapPerfIcmpTotalTxEchoReq": dfrapPerfIcmpTotalTxEchoReq,
       "dfrapPerfIcmpTotalRxTimeExcd": dfrapPerfIcmpTotalRxTimeExcd,
       "dfrapPerfIcmpTotalTxTimeExcd": dfrapPerfIcmpTotalTxTimeExcd,
       "dfrapPerfIcmpTotalRxParamProb": dfrapPerfIcmpTotalRxParamProb,
       "dfrapPerfIcmpTotalTxParamProb": dfrapPerfIcmpTotalTxParamProb,
       "dfrapPerfIcmpTotalRxTimestpReq": dfrapPerfIcmpTotalRxTimestpReq,
       "dfrapPerfIcmpTotalTxTimestpReq": dfrapPerfIcmpTotalTxTimestpReq,
       "dfrapPerfIcmpTotalRxTimestpRep": dfrapPerfIcmpTotalRxTimestpRep,
       "dfrapPerfIcmpTotalTxTimestpRep": dfrapPerfIcmpTotalTxTimestpRep,
       "dfrapPerfIcmpTotalRxAddrMaskReq": dfrapPerfIcmpTotalRxAddrMaskReq,
       "dfrapPerfIcmpTotalTxAddrMaskReq": dfrapPerfIcmpTotalTxAddrMaskReq,
       "dfrapPerfIcmpTotalRxAddrMaskRep": dfrapPerfIcmpTotalRxAddrMaskRep,
       "dfrapPerfIcmpTotalTxAddrMaskRep": dfrapPerfIcmpTotalTxAddrMaskRep,
       "dfrapPerfIcmpTotalRxPktTooBig": dfrapPerfIcmpTotalRxPktTooBig,
       "dfrapPerfIcmpTotalTxPktTooBig": dfrapPerfIcmpTotalTxPktTooBig,
       "dfrapPerfIcmpTotalRxGmQuery": dfrapPerfIcmpTotalRxGmQuery,
       "dfrapPerfIcmpTotalTxGmQuery": dfrapPerfIcmpTotalTxGmQuery,
       "dfrapPerfIcmpTotalRxGmReport": dfrapPerfIcmpTotalRxGmReport,
       "dfrapPerfIcmpTotalTxGmReport": dfrapPerfIcmpTotalTxGmReport,
       "dfrapPerfIcmpTotalRxGmReduct": dfrapPerfIcmpTotalRxGmReduct,
       "dfrapPerfIcmpTotalTxGmReduct": dfrapPerfIcmpTotalTxGmReduct,
       "dfrapPerfApplicationPerDlciTable": dfrapPerfApplicationPerDlciTable,
       "dfrapPerfApplicationPerDlciEntry": dfrapPerfApplicationPerDlciEntry,
       "dfrapPerfApplicationPerDlciInterval": dfrapPerfApplicationPerDlciInterval,
       "dfrapPerfApplicationPerDlciValue": dfrapPerfApplicationPerDlciValue,
       "dfrapPerfApplicationPerDlciRxSnmp": dfrapPerfApplicationPerDlciRxSnmp,
       "dfrapPerfApplicationPerDlciTxSnmp": dfrapPerfApplicationPerDlciTxSnmp,
       "dfrapPerfApplicationPerDlciRxSnmpTrap": dfrapPerfApplicationPerDlciRxSnmpTrap,
       "dfrapPerfApplicationPerDlciTxSnmpTrap": dfrapPerfApplicationPerDlciTxSnmpTrap,
       "dfrapPerfApplicationPerDlciRxHttp": dfrapPerfApplicationPerDlciRxHttp,
       "dfrapPerfApplicationPerDlciTxHttp": dfrapPerfApplicationPerDlciTxHttp,
       "dfrapPerfApplicationPerDlciRxTelnet": dfrapPerfApplicationPerDlciRxTelnet,
       "dfrapPerfApplicationPerDlciTxTelnet": dfrapPerfApplicationPerDlciTxTelnet,
       "dfrapPerfApplicationPerDlciRxSmtp": dfrapPerfApplicationPerDlciRxSmtp,
       "dfrapPerfApplicationPerDlciTxSmtp": dfrapPerfApplicationPerDlciTxSmtp,
       "dfrapPerfApplicationPerDlciRxFtp": dfrapPerfApplicationPerDlciRxFtp,
       "dfrapPerfApplicationPerDlciTxFtp": dfrapPerfApplicationPerDlciTxFtp,
       "dfrapPerfApplicationPerDlciRxTftp": dfrapPerfApplicationPerDlciRxTftp,
       "dfrapPerfApplicationPerDlciTxTftp": dfrapPerfApplicationPerDlciTxTftp,
       "dfrapPerfApplicationPerDlciRxCustom1": dfrapPerfApplicationPerDlciRxCustom1,
       "dfrapPerfApplicationPerDlciTxCustom1": dfrapPerfApplicationPerDlciTxCustom1,
       "dfrapPerfApplicationPerDlciRxCustom2": dfrapPerfApplicationPerDlciRxCustom2,
       "dfrapPerfApplicationPerDlciTxCustom2": dfrapPerfApplicationPerDlciTxCustom2,
       "dfrapPerfApplicationPerDlciRxCustom3": dfrapPerfApplicationPerDlciRxCustom3,
       "dfrapPerfApplicationPerDlciTxCustom3": dfrapPerfApplicationPerDlciTxCustom3,
       "dfrapPerfApplicationPerDlciRxCustom4": dfrapPerfApplicationPerDlciRxCustom4,
       "dfrapPerfApplicationPerDlciTxCustom4": dfrapPerfApplicationPerDlciTxCustom4,
       "dfrapPerfApplicationTotalTable": dfrapPerfApplicationTotalTable,
       "dfrapPerfApplicationTotalEntry": dfrapPerfApplicationTotalEntry,
       "dfrapPerfApplicationTotalInterval": dfrapPerfApplicationTotalInterval,
       "dfrapPerfApplicationTotalRxSnmp": dfrapPerfApplicationTotalRxSnmp,
       "dfrapPerfApplicationTotalTxSnmp": dfrapPerfApplicationTotalTxSnmp,
       "dfrapPerfApplicationTotalRxSnmpTrap": dfrapPerfApplicationTotalRxSnmpTrap,
       "dfrapPerfApplicationTotalTxSnmpTrap": dfrapPerfApplicationTotalTxSnmpTrap,
       "dfrapPerfApplicationTotalRxHttp": dfrapPerfApplicationTotalRxHttp,
       "dfrapPerfApplicationTotalTxHttp": dfrapPerfApplicationTotalTxHttp,
       "dfrapPerfApplicationTotalRxTelnet": dfrapPerfApplicationTotalRxTelnet,
       "dfrapPerfApplicationTotalTxTelnet": dfrapPerfApplicationTotalTxTelnet,
       "dfrapPerfApplicationTotalRxSmtp": dfrapPerfApplicationTotalRxSmtp,
       "dfrapPerfApplicationTotalTxSmtp": dfrapPerfApplicationTotalTxSmtp,
       "dfrapPerfApplicationTotalRxFtp": dfrapPerfApplicationTotalRxFtp,
       "dfrapPerfApplicationTotalTxFtp": dfrapPerfApplicationTotalTxFtp,
       "dfrapPerfApplicationTotalRxTftp": dfrapPerfApplicationTotalRxTftp,
       "dfrapPerfApplicationTotalTxTftp": dfrapPerfApplicationTotalTxTftp,
       "dfrapPerfApplicationTotalRxCustom1": dfrapPerfApplicationTotalRxCustom1,
       "dfrapPerfApplicationTotalTxCustom1": dfrapPerfApplicationTotalTxCustom1,
       "dfrapPerfApplicationTotalRxCustom2": dfrapPerfApplicationTotalRxCustom2,
       "dfrapPerfApplicationTotalTxCustom2": dfrapPerfApplicationTotalTxCustom2,
       "dfrapPerfApplicationTotalRxCustom3": dfrapPerfApplicationTotalRxCustom3,
       "dfrapPerfApplicationTotalTxCustom3": dfrapPerfApplicationTotalTxCustom3,
       "dfrapPerfApplicationTotalRxCustom4": dfrapPerfApplicationTotalRxCustom4,
       "dfrapPerfApplicationTotalTxCustom4": dfrapPerfApplicationTotalTxCustom4,
       "dfrapPerfRoutingPerDlciTable": dfrapPerfRoutingPerDlciTable,
       "dfrapPerfRoutingPerDlciEntry": dfrapPerfRoutingPerDlciEntry,
       "dfrapPerfRoutingPerDlciInterval": dfrapPerfRoutingPerDlciInterval,
       "dfrapPerfRoutingPerDlciValue": dfrapPerfRoutingPerDlciValue,
       "dfrapPerfRoutingPerDlciRxOspf": dfrapPerfRoutingPerDlciRxOspf,
       "dfrapPerfRoutingPerDlciTxOspf": dfrapPerfRoutingPerDlciTxOspf,
       "dfrapPerfRoutingPerDlciRxRip": dfrapPerfRoutingPerDlciRxRip,
       "dfrapPerfRoutingPerDlciTxRip": dfrapPerfRoutingPerDlciTxRip,
       "dfrapPerfRoutingPerDlciRxNetbios": dfrapPerfRoutingPerDlciRxNetbios,
       "dfrapPerfRoutingPerDlciTxNetbios": dfrapPerfRoutingPerDlciTxNetbios,
       "dfrapPerfRoutingTotalTable": dfrapPerfRoutingTotalTable,
       "dfrapPerfRoutingTotalEntry": dfrapPerfRoutingTotalEntry,
       "dfrapPerfRoutingTotalInterval": dfrapPerfRoutingTotalInterval,
       "dfrapPerfRoutingTotalRxOspf": dfrapPerfRoutingTotalRxOspf,
       "dfrapPerfRoutingTotalTxOspf": dfrapPerfRoutingTotalTxOspf,
       "dfrapPerfRoutingTotalRxRip": dfrapPerfRoutingTotalRxRip,
       "dfrapPerfRoutingTotalTxRip": dfrapPerfRoutingTotalTxRip,
       "dfrapPerfRoutingTotalRxNetbios": dfrapPerfRoutingTotalRxNetbios,
       "dfrapPerfRoutingTotalTxNetbios": dfrapPerfRoutingTotalTxNetbios,
       "dfrapPerfIpxPerDlciTable": dfrapPerfIpxPerDlciTable,
       "dfrapPerfIpxPerDlciEntry": dfrapPerfIpxPerDlciEntry,
       "dfrapPerfIpxPerDlciInterval": dfrapPerfIpxPerDlciInterval,
       "dfrapPerfIpxPerDlciValue": dfrapPerfIpxPerDlciValue,
       "dfrapPerfIpxPerDlciRxTotal": dfrapPerfIpxPerDlciRxTotal,
       "dfrapPerfIpxPerDlciTxTotal": dfrapPerfIpxPerDlciTxTotal,
       "dfrapPerfIpxPerDlciRxSpx": dfrapPerfIpxPerDlciRxSpx,
       "dfrapPerfIpxPerDlciTxSpx": dfrapPerfIpxPerDlciTxSpx,
       "dfrapPerfIpxPerDlciRxNcp": dfrapPerfIpxPerDlciRxNcp,
       "dfrapPerfIpxPerDlciTxNcp": dfrapPerfIpxPerDlciTxNcp,
       "dfrapPerfIpxPerDlciRxSap": dfrapPerfIpxPerDlciRxSap,
       "dfrapPerfIpxPerDlciTxSap": dfrapPerfIpxPerDlciTxSap,
       "dfrapPerfIpxPerDlciRxRip": dfrapPerfIpxPerDlciRxRip,
       "dfrapPerfIpxPerDlciTxRip": dfrapPerfIpxPerDlciTxRip,
       "dfrapPerfIpxPerDlciRxNetbios": dfrapPerfIpxPerDlciRxNetbios,
       "dfrapPerfIpxPerDlciTxNetbios": dfrapPerfIpxPerDlciTxNetbios,
       "dfrapPerfIpxPerDlciRxOther": dfrapPerfIpxPerDlciRxOther,
       "dfrapPerfIpxPerDlciTxOther": dfrapPerfIpxPerDlciTxOther,
       "dfrapPerfIpxTotalTable": dfrapPerfIpxTotalTable,
       "dfrapPerfIpxTotalEntry": dfrapPerfIpxTotalEntry,
       "dfrapPerfIpxTotalInterval": dfrapPerfIpxTotalInterval,
       "dfrapPerfIpxTotalRxTotal": dfrapPerfIpxTotalRxTotal,
       "dfrapPerfIpxTotalTxTotal": dfrapPerfIpxTotalTxTotal,
       "dfrapPerfIpxTotalRxSpx": dfrapPerfIpxTotalRxSpx,
       "dfrapPerfIpxTotalTxSpx": dfrapPerfIpxTotalTxSpx,
       "dfrapPerfIpxTotalRxNcp": dfrapPerfIpxTotalRxNcp,
       "dfrapPerfIpxTotalTxNcp": dfrapPerfIpxTotalTxNcp,
       "dfrapPerfIpxTotalRxSap": dfrapPerfIpxTotalRxSap,
       "dfrapPerfIpxTotalTxSap": dfrapPerfIpxTotalTxSap,
       "dfrapPerfIpxTotalRxRip": dfrapPerfIpxTotalRxRip,
       "dfrapPerfIpxTotalTxRip": dfrapPerfIpxTotalTxRip,
       "dfrapPerfIpxTotalRxNetbios": dfrapPerfIpxTotalRxNetbios,
       "dfrapPerfIpxTotalTxNetbios": dfrapPerfIpxTotalTxNetbios,
       "dfrapPerfIpxTotalRxOther": dfrapPerfIpxTotalRxOther,
       "dfrapPerfIpxTotalTxOther": dfrapPerfIpxTotalTxOther,
       "dfrapPerfSnaPerDlciTable": dfrapPerfSnaPerDlciTable,
       "dfrapPerfSnaPerDlciEntry": dfrapPerfSnaPerDlciEntry,
       "dfrapPerfSnaPerDlciInterval": dfrapPerfSnaPerDlciInterval,
       "dfrapPerfSnaPerDlciValue": dfrapPerfSnaPerDlciValue,
       "dfrapPerfSnaPerDlciRxTotal": dfrapPerfSnaPerDlciRxTotal,
       "dfrapPerfSnaPerDlciTxTotal": dfrapPerfSnaPerDlciTxTotal,
       "dfrapPerfSnaPerDlciRxSubarea": dfrapPerfSnaPerDlciRxSubarea,
       "dfrapPerfSnaPerDlciTxSubarea": dfrapPerfSnaPerDlciTxSubarea,
       "dfrapPerfSnaPerDlciRxPeriph": dfrapPerfSnaPerDlciRxPeriph,
       "dfrapPerfSnaPerDlciTxPeriph": dfrapPerfSnaPerDlciTxPeriph,
       "dfrapPerfSnaPerDlciRxAppn": dfrapPerfSnaPerDlciRxAppn,
       "dfrapPerfSnaPerDlciTxAppn": dfrapPerfSnaPerDlciTxAppn,
       "dfrapPerfSnaPerDlciRxNetbios": dfrapPerfSnaPerDlciRxNetbios,
       "dfrapPerfSnaPerDlciTxNetbios": dfrapPerfSnaPerDlciTxNetbios,
       "dfrapPerfSnaPerDlciRxOther": dfrapPerfSnaPerDlciRxOther,
       "dfrapPerfSnaPerDlciTxOther": dfrapPerfSnaPerDlciTxOther,
       "dfrapPerfSnaTotalTable": dfrapPerfSnaTotalTable,
       "dfrapPerfSnaTotalEntry": dfrapPerfSnaTotalEntry,
       "dfrapPerfSnaTotalInterval": dfrapPerfSnaTotalInterval,
       "dfrapPerfSnaTotalRxTotal": dfrapPerfSnaTotalRxTotal,
       "dfrapPerfSnaTotalTxTotal": dfrapPerfSnaTotalTxTotal,
       "dfrapPerfSnaTotalRxSubarea": dfrapPerfSnaTotalRxSubarea,
       "dfrapPerfSnaTotalTxSubarea": dfrapPerfSnaTotalTxSubarea,
       "dfrapPerfSnaTotalRxPeriph": dfrapPerfSnaTotalRxPeriph,
       "dfrapPerfSnaTotalTxPeriph": dfrapPerfSnaTotalTxPeriph,
       "dfrapPerfSnaTotalRxAppn": dfrapPerfSnaTotalRxAppn,
       "dfrapPerfSnaTotalTxAppn": dfrapPerfSnaTotalTxAppn,
       "dfrapPerfSnaTotalRxNetbios": dfrapPerfSnaTotalRxNetbios,
       "dfrapPerfSnaTotalTxNetbios": dfrapPerfSnaTotalTxNetbios,
       "dfrapPerfSnaTotalRxOther": dfrapPerfSnaTotalRxOther,
       "dfrapPerfSnaTotalTxOther": dfrapPerfSnaTotalTxOther,
       "dfrapPerfArpPerDlciTable": dfrapPerfArpPerDlciTable,
       "dfrapPerfArpPerDlciEntry": dfrapPerfArpPerDlciEntry,
       "dfrapPerfArpPerDlciInterval": dfrapPerfArpPerDlciInterval,
       "dfrapPerfArpPerDlciValue": dfrapPerfArpPerDlciValue,
       "dfrapPerfArpPerDlciRxTotal": dfrapPerfArpPerDlciRxTotal,
       "dfrapPerfArpPerDlciTxTotal": dfrapPerfArpPerDlciTxTotal,
       "dfrapPerfArpPerDlciRxArpReq": dfrapPerfArpPerDlciRxArpReq,
       "dfrapPerfArpPerDlciTxArpReq": dfrapPerfArpPerDlciTxArpReq,
       "dfrapPerfArpPerDlciRxArpRep": dfrapPerfArpPerDlciRxArpRep,
       "dfrapPerfArpPerDlciTxArpRep": dfrapPerfArpPerDlciTxArpRep,
       "dfrapPerfArpPerDlciRxRarpReq": dfrapPerfArpPerDlciRxRarpReq,
       "dfrapPerfArpPerDlciTxRarpReq": dfrapPerfArpPerDlciTxRarpReq,
       "dfrapPerfArpPerDlciRxRarpRep": dfrapPerfArpPerDlciRxRarpRep,
       "dfrapPerfArpPerDlciTxRarpRep": dfrapPerfArpPerDlciTxRarpRep,
       "dfrapPerfArpPerDlciRxInarpReq": dfrapPerfArpPerDlciRxInarpReq,
       "dfrapPerfArpPerDlciTxInarpReq": dfrapPerfArpPerDlciTxInarpReq,
       "dfrapPerfArpPerDlciRxInarpRep": dfrapPerfArpPerDlciRxInarpRep,
       "dfrapPerfArpPerDlciTxInarpRep": dfrapPerfArpPerDlciTxInarpRep,
       "dfrapPerfArpPerDlciRxOther": dfrapPerfArpPerDlciRxOther,
       "dfrapPerfArpPerDlciTxOther": dfrapPerfArpPerDlciTxOther,
       "dfrapPerfArpTotalTable": dfrapPerfArpTotalTable,
       "dfrapPerfArpTotalEntry": dfrapPerfArpTotalEntry,
       "dfrapPerfArpTotalInterval": dfrapPerfArpTotalInterval,
       "dfrapPerfArpTotalRxTotal": dfrapPerfArpTotalRxTotal,
       "dfrapPerfArpTotalTxTotal": dfrapPerfArpTotalTxTotal,
       "dfrapPerfArpTotalRxArpReq": dfrapPerfArpTotalRxArpReq,
       "dfrapPerfArpTotalTxArpReq": dfrapPerfArpTotalTxArpReq,
       "dfrapPerfArpTotalRxArpRep": dfrapPerfArpTotalRxArpRep,
       "dfrapPerfArpTotalTxArpRep": dfrapPerfArpTotalTxArpRep,
       "dfrapPerfArpTotalRxRarpReq": dfrapPerfArpTotalRxRarpReq,
       "dfrapPerfArpTotalTxRarpReq": dfrapPerfArpTotalTxRarpReq,
       "dfrapPerfArpTotalRxRarpRep": dfrapPerfArpTotalRxRarpRep,
       "dfrapPerfArpTotalTxRarpRep": dfrapPerfArpTotalTxRarpRep,
       "dfrapPerfArpTotalRxInarpReq": dfrapPerfArpTotalRxInarpReq,
       "dfrapPerfArpTotalTxInarpReq": dfrapPerfArpTotalTxInarpReq,
       "dfrapPerfArpTotalRxInarpRep": dfrapPerfArpTotalRxInarpRep,
       "dfrapPerfArpTotalTxInarpRep": dfrapPerfArpTotalTxInarpRep,
       "dfrapPerfArpTotalRxOther": dfrapPerfArpTotalRxOther,
       "dfrapPerfArpTotalTxOther": dfrapPerfArpTotalTxOther,
       "dfrapPerfLmiPerDlciTable": dfrapPerfLmiPerDlciTable,
       "dfrapPerfLmiPerDlciEntry": dfrapPerfLmiPerDlciEntry,
       "dfrapPerfLmiPerDlciInterval": dfrapPerfLmiPerDlciInterval,
       "dfrapPerfLmiPerDlciValue": dfrapPerfLmiPerDlciValue,
       "dfrapPerfLmiPerDlciRxTotalByteCnt": dfrapPerfLmiPerDlciRxTotalByteCnt,
       "dfrapPerfLmiPerDlciTxTotalByteCnt": dfrapPerfLmiPerDlciTxTotalByteCnt,
       "dfrapPerfLmiPerDlciRxLivoEnqByteCnt": dfrapPerfLmiPerDlciRxLivoEnqByteCnt,
       "dfrapPerfLmiPerDlciTxLivoEnqByteCnt": dfrapPerfLmiPerDlciTxLivoEnqByteCnt,
       "dfrapPerfLmiPerDlciRxLivoStatByteCnt": dfrapPerfLmiPerDlciRxLivoStatByteCnt,
       "dfrapPerfLmiPerDlciTxLivoStatByteCnt": dfrapPerfLmiPerDlciTxLivoStatByteCnt,
       "dfrapPerfLmiPerDlciRxFullEnqByteCnt": dfrapPerfLmiPerDlciRxFullEnqByteCnt,
       "dfrapPerfLmiPerDlciTxFullEnqByteCnt": dfrapPerfLmiPerDlciTxFullEnqByteCnt,
       "dfrapPerfLmiPerDlciRxFullStatByteCnt": dfrapPerfLmiPerDlciRxFullStatByteCnt,
       "dfrapPerfLmiPerDlciTxFullStatByteCnt": dfrapPerfLmiPerDlciTxFullStatByteCnt,
       "dfrapPerfLmiPerDlciRxOtherByteCnt": dfrapPerfLmiPerDlciRxOtherByteCnt,
       "dfrapPerfLmiPerDlciTxOtherByteCnt": dfrapPerfLmiPerDlciTxOtherByteCnt,
       "dfrapPerfLmiTotalTable": dfrapPerfLmiTotalTable,
       "dfrapPerfLmiTotalEntry": dfrapPerfLmiTotalEntry,
       "dfrapPerfLmiTotalInterval": dfrapPerfLmiTotalInterval,
       "dfrapPerfLmiTotalDlciValue": dfrapPerfLmiTotalDlciValue,
       "dfrapPerfLmiTotalRxTotalByteCnt": dfrapPerfLmiTotalRxTotalByteCnt,
       "dfrapPerfLmiTotalTxTotalByteCnt": dfrapPerfLmiTotalTxTotalByteCnt,
       "dfrapPerfLmiTotalRxLivoEnqByteCnt": dfrapPerfLmiTotalRxLivoEnqByteCnt,
       "dfrapPerfLmiTotalTxLivoEnqByteCnt": dfrapPerfLmiTotalTxLivoEnqByteCnt,
       "dfrapPerfLmiTotalRxLivoStatByteCnt": dfrapPerfLmiTotalRxLivoStatByteCnt,
       "dfrapPerfLmiTotalTxLivoStatByteCnt": dfrapPerfLmiTotalTxLivoStatByteCnt,
       "dfrapPerfLmiTotalRxFullEnqByteCnt": dfrapPerfLmiTotalRxFullEnqByteCnt,
       "dfrapPerfLmiTotalTxFullEnqByteCnt": dfrapPerfLmiTotalTxFullEnqByteCnt,
       "dfrapPerfLmiTotalRxFullStatByteCnt": dfrapPerfLmiTotalRxFullStatByteCnt,
       "dfrapPerfLmiTotalTxFullStatByteCnt": dfrapPerfLmiTotalTxFullStatByteCnt,
       "dfrapPerfLmiTotalRxOtherByteCnt": dfrapPerfLmiTotalRxOtherByteCnt,
       "dfrapPerfLmiTotalTxOtherByteCnt": dfrapPerfLmiTotalTxOtherByteCnt,
       "dfrapPerfNetworkLongTerm": dfrapPerfNetworkLongTerm,
       "dfrapPerfNetwLongTermTable": dfrapPerfNetwLongTermTable,
       "dfrapPerfNetwLongTermEntry": dfrapPerfNetwLongTermEntry,
       "dfrapPerfNetwLongTermDlci": dfrapPerfNetwLongTermDlci,
       "dfrapPerfNetwLongTermProtocol": dfrapPerfNetwLongTermProtocol,
       "dfrapPerfNetwLongTermInterval": dfrapPerfNetwLongTermInterval,
       "dfrapPerfNetwLongTermValue": dfrapPerfNetwLongTermValue,
       "dfrapPerfNetwLongTermAltTable": dfrapPerfNetwLongTermAltTable,
       "dfrapPerfNetwLongTermAltEntry": dfrapPerfNetwLongTermAltEntry,
       "dfrapPerfNetwLongTermAltDlci": dfrapPerfNetwLongTermAltDlci,
       "dfrapPerfNetwLongTermAltProtocol": dfrapPerfNetwLongTermAltProtocol,
       "dfrapPerfNetwLongTermAltArray": dfrapPerfNetwLongTermAltArray,
       "dfrapPerfNetworkLongTermCommands": dfrapPerfNetworkLongTermCommands,
       "dfrapPerfNetworkLongTermCmdClear": dfrapPerfNetworkLongTermCmdClear,
       "dfrapPerfCirPercentUtilization": dfrapPerfCirPercentUtilization,
       "dfrapPerfCirPercentUtilizationTable": dfrapPerfCirPercentUtilizationTable,
       "dfrapPerfCirPercentUtilizationEntry": dfrapPerfCirPercentUtilizationEntry,
       "dfrapPerfCirPercentUtilizationInterval": dfrapPerfCirPercentUtilizationInterval,
       "dfrapPerfCirPercentUtilizationDlciValue": dfrapPerfCirPercentUtilizationDlciValue,
       "dfrapPerfCirRxPercentUtilizationRange1": dfrapPerfCirRxPercentUtilizationRange1,
       "dfrapPerfCirRxPercentUtilizationRange2": dfrapPerfCirRxPercentUtilizationRange2,
       "dfrapPerfCirRxPercentUtilizationRange3": dfrapPerfCirRxPercentUtilizationRange3,
       "dfrapPerfCirRxPercentUtilizationRange4": dfrapPerfCirRxPercentUtilizationRange4,
       "dfrapPerfCirRxPercentUtilizationRange5": dfrapPerfCirRxPercentUtilizationRange5,
       "dfrapPerfCirRxPercentUtilizationRange6": dfrapPerfCirRxPercentUtilizationRange6,
       "dfrapPerfCirRxPercentUtilizationRange7": dfrapPerfCirRxPercentUtilizationRange7,
       "dfrapPerfCirRxPercentUtilizationRange8": dfrapPerfCirRxPercentUtilizationRange8,
       "dfrapPerfCirTxPercentUtilizationRange1": dfrapPerfCirTxPercentUtilizationRange1,
       "dfrapPerfCirTxPercentUtilizationRange2": dfrapPerfCirTxPercentUtilizationRange2,
       "dfrapPerfCirTxPercentUtilizationRange3": dfrapPerfCirTxPercentUtilizationRange3,
       "dfrapPerfCirTxPercentUtilizationRange4": dfrapPerfCirTxPercentUtilizationRange4,
       "dfrapPerfCirTxPercentUtilizationRange5": dfrapPerfCirTxPercentUtilizationRange5,
       "dfrapPerfCirTxPercentUtilizationRange6": dfrapPerfCirTxPercentUtilizationRange6,
       "dfrapPerfCirTxPercentUtilizationRange7": dfrapPerfCirTxPercentUtilizationRange7,
       "dfrapPerfCirTxPercentUtilizationRange8": dfrapPerfCirTxPercentUtilizationRange8,
       "dfrapPerfCurrentPerDlciUtilizationTable": dfrapPerfCurrentPerDlciUtilizationTable,
       "dfrapPerfCurrentPerDlciUtilizationEntry": dfrapPerfCurrentPerDlciUtilizationEntry,
       "dfrapPerfCurrentPerDlciUtilizationDlciValue": dfrapPerfCurrentPerDlciUtilizationDlciValue,
       "dfrapPerfCurrentPerDlciRxUtilization": dfrapPerfCurrentPerDlciRxUtilization,
       "dfrapPerfCurrentPerDlciTxUtilization": dfrapPerfCurrentPerDlciTxUtilization,
       "dfrapPerfCurrentPerDlciAggregateUtilization": dfrapPerfCurrentPerDlciAggregateUtilization,
       "dfrapPerfCurrentUnitUtilization": dfrapPerfCurrentUnitUtilization,
       "dfrapPerfCurrentDteUtilization": dfrapPerfCurrentDteUtilization,
       "dfrapPerfCurrentWanUtilization": dfrapPerfCurrentWanUtilization,
       "dfrapPerfCurrentAggregateUtilization": dfrapPerfCurrentAggregateUtilization,
       "dfrapAlarmType": dfrapAlarmType,
       "dfrapDLCINum": dfrapDLCINum,
       "dfrapInterface": dfrapInterface,
       "dfrapIpAddress": dfrapIpAddress,
       "dfrapEventTrapLog": dfrapEventTrapLog,
       "dfrapEventTrapLogTable": dfrapEventTrapLogTable,
       "dfrapEventTrapLogEntry": dfrapEventTrapLogEntry,
       "dfrapEventTrapLogSeqNum": dfrapEventTrapLogSeqNum,
       "dfrapEventTrapLogGenericEvent": dfrapEventTrapLogGenericEvent,
       "dfrapEventTrapLogSpecificEvent": dfrapEventTrapLogSpecificEvent,
       "dfrapEventTrapLogTimeStamp": dfrapEventTrapLogTimeStamp,
       "dfrapEventTrapLogVarBind1": dfrapEventTrapLogVarBind1,
       "dfrapEventTrapLogVarBind2": dfrapEventTrapLogVarBind2,
       "dfrapEventTrapLogVarBind3": dfrapEventTrapLogVarBind3,
       "dfrapEventLogAltTable": dfrapEventLogAltTable,
       "dfrapEventLogAltEntry": dfrapEventLogAltEntry,
       "dfrapEventLogAltSeqNum": dfrapEventLogAltSeqNum,
       "dfrapEventLogAltArray": dfrapEventLogAltArray,
       "dfrapEventLogCurrentSeqNum": dfrapEventLogCurrentSeqNum,
       "dfrapEventLogFreeze": dfrapEventLogFreeze,
       "dfrapEventLogClear": dfrapEventLogClear,
       "dfrapPercentUtilization": dfrapPercentUtilization,
       "dfrapUtilizationThreshold": dfrapUtilizationThreshold,
       "dfrapCfgLockIpAddress": dfrapCfgLockIpAddress}
)
