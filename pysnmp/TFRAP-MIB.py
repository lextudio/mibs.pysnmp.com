# SNMP MIB module (TFRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TFRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:28 2024
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
_Tfrap_ObjectIdentity = ObjectIdentity
tfrap = _Tfrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5)
)
_TfrapSystem_ObjectIdentity = ObjectIdentity
tfrapSystem = _TfrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 1)
)
_TfrapSysTable_ObjectIdentity = ObjectIdentity
tfrapSysTable = _TfrapSysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1)
)


class _TfrapSysType_Type(DisplayString):
    """Custom type tfrapSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TfrapSysType_Type.__name__ = "DisplayString"
_TfrapSysType_Object = MibScalar
tfrapSysType = _TfrapSysType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 1),
    _TfrapSysType_Type()
)
tfrapSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysType.setStatus("mandatory")


class _TfrapSysSoftRev_Type(DisplayString):
    """Custom type tfrapSysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysSoftRev_Type.__name__ = "DisplayString"
_TfrapSysSoftRev_Object = MibScalar
tfrapSysSoftRev = _TfrapSysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 2),
    _TfrapSysSoftRev_Type()
)
tfrapSysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysSoftRev.setStatus("mandatory")


class _TfrapSysHardRev_Type(DisplayString):
    """Custom type tfrapSysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysHardRev_Type.__name__ = "DisplayString"
_TfrapSysHardRev_Object = MibScalar
tfrapSysHardRev = _TfrapSysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 3),
    _TfrapSysHardRev_Type()
)
tfrapSysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysHardRev.setStatus("mandatory")


class _TfrapSysNumT1Installed_Type(Integer32):
    """Custom type tfrapSysNumT1Installed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TfrapSysNumT1Installed_Type.__name__ = "Integer32"
_TfrapSysNumT1Installed_Object = MibScalar
tfrapSysNumT1Installed = _TfrapSysNumT1Installed_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 4),
    _TfrapSysNumT1Installed_Type()
)
tfrapSysNumT1Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumT1Installed.setStatus("mandatory")


class _TfrapSysNumDteInstalled_Type(Integer32):
    """Custom type tfrapSysNumDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TfrapSysNumDteInstalled_Type.__name__ = "Integer32"
_TfrapSysNumDteInstalled_Object = MibScalar
tfrapSysNumDteInstalled = _TfrapSysNumDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 5),
    _TfrapSysNumDteInstalled_Type()
)
tfrapSysNumDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumDteInstalled.setStatus("mandatory")


class _TfrapSysNumMaintInstalled_Type(Integer32):
    """Custom type tfrapSysNumMaintInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TfrapSysNumMaintInstalled_Type.__name__ = "Integer32"
_TfrapSysNumMaintInstalled_Object = MibScalar
tfrapSysNumMaintInstalled = _TfrapSysNumMaintInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 6),
    _TfrapSysNumMaintInstalled_Type()
)
tfrapSysNumMaintInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumMaintInstalled.setStatus("mandatory")


class _TfrapSysName_Type(DisplayString):
    """Custom type tfrapSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TfrapSysName_Type.__name__ = "DisplayString"
_TfrapSysName_Object = MibScalar
tfrapSysName = _TfrapSysName_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 7),
    _TfrapSysName_Type()
)
tfrapSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapSysName.setStatus("mandatory")


class _TfrapSysSerialNo_Type(DisplayString):
    """Custom type tfrapSysSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysSerialNo_Type.__name__ = "DisplayString"
_TfrapSysSerialNo_Object = MibScalar
tfrapSysSerialNo = _TfrapSysSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 8),
    _TfrapSysSerialNo_Type()
)
tfrapSysSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysSerialNo.setStatus("mandatory")


class _TfrapSysResetNode_Type(Integer32):
    """Custom type tfrapSysResetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            321
        )
    )
    namedValues = NamedValues(
        ("reset-node", 321)
    )


_TfrapSysResetNode_Type.__name__ = "Integer32"
_TfrapSysResetNode_Object = MibScalar
tfrapSysResetNode = _TfrapSysResetNode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 9),
    _TfrapSysResetNode_Type()
)
tfrapSysResetNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapSysResetNode.setStatus("mandatory")
_TfrapSysAmtMemoryInstalled_Type = Integer32
_TfrapSysAmtMemoryInstalled_Object = MibScalar
tfrapSysAmtMemoryInstalled = _TfrapSysAmtMemoryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 10),
    _TfrapSysAmtMemoryInstalled_Type()
)
tfrapSysAmtMemoryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysAmtMemoryInstalled.setStatus("mandatory")


class _TfrapSysLocation_Type(DisplayString):
    """Custom type tfrapSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TfrapSysLocation_Type.__name__ = "DisplayString"
_TfrapSysLocation_Object = MibScalar
tfrapSysLocation = _TfrapSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 12),
    _TfrapSysLocation_Type()
)
tfrapSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapSysLocation.setStatus("mandatory")


class _TfrapSysContact_Type(DisplayString):
    """Custom type tfrapSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TfrapSysContact_Type.__name__ = "DisplayString"
_TfrapSysContact_Object = MibScalar
tfrapSysContact = _TfrapSysContact_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 13),
    _TfrapSysContact_Type()
)
tfrapSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapSysContact.setStatus("mandatory")


class _TfrapSysPrompt_Type(DisplayString):
    """Custom type tfrapSysPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapSysPrompt_Type.__name__ = "DisplayString"
_TfrapSysPrompt_Object = MibScalar
tfrapSysPrompt = _TfrapSysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 15),
    _TfrapSysPrompt_Type()
)
tfrapSysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapSysPrompt.setStatus("mandatory")


class _TfrapSysBootRev_Type(DisplayString):
    """Custom type tfrapSysBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysBootRev_Type.__name__ = "DisplayString"
_TfrapSysBootRev_Object = MibScalar
tfrapSysBootRev = _TfrapSysBootRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 1, 16),
    _TfrapSysBootRev_Type()
)
tfrapSysBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysBootRev.setStatus("mandatory")
_TfrapSysFeatureTable_ObjectIdentity = ObjectIdentity
tfrapSysFeatureTable = _TfrapSysFeatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2)
)


class _TfrapSysSLIPSupported_Type(DisplayString):
    """Custom type tfrapSysSLIPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysSLIPSupported_Type.__name__ = "DisplayString"
_TfrapSysSLIPSupported_Object = MibScalar
tfrapSysSLIPSupported = _TfrapSysSLIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 1),
    _TfrapSysSLIPSupported_Type()
)
tfrapSysSLIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysSLIPSupported.setStatus("mandatory")


class _TfrapSysPPPSupported_Type(DisplayString):
    """Custom type tfrapSysPPPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysPPPSupported_Type.__name__ = "DisplayString"
_TfrapSysPPPSupported_Object = MibScalar
tfrapSysPPPSupported = _TfrapSysPPPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 2),
    _TfrapSysPPPSupported_Type()
)
tfrapSysPPPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysPPPSupported.setStatus("mandatory")


class _TfrapSysRDOSupported_Type(DisplayString):
    """Custom type tfrapSysRDOSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysRDOSupported_Type.__name__ = "DisplayString"
_TfrapSysRDOSupported_Object = MibScalar
tfrapSysRDOSupported = _TfrapSysRDOSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 3),
    _TfrapSysRDOSupported_Type()
)
tfrapSysRDOSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysRDOSupported.setStatus("mandatory")


class _TfrapSysETHSupported_Type(DisplayString):
    """Custom type tfrapSysETHSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysETHSupported_Type.__name__ = "DisplayString"
_TfrapSysETHSupported_Object = MibScalar
tfrapSysETHSupported = _TfrapSysETHSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 4),
    _TfrapSysETHSupported_Type()
)
tfrapSysETHSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysETHSupported.setStatus("mandatory")


class _TfrapSysTKRSupported_Type(DisplayString):
    """Custom type tfrapSysTKRSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysTKRSupported_Type.__name__ = "DisplayString"
_TfrapSysTKRSupported_Object = MibScalar
tfrapSysTKRSupported = _TfrapSysTKRSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 5),
    _TfrapSysTKRSupported_Type()
)
tfrapSysTKRSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysTKRSupported.setStatus("mandatory")


class _TfrapSysExtTimSupported_Type(DisplayString):
    """Custom type tfrapSysExtTimSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysExtTimSupported_Type.__name__ = "DisplayString"
_TfrapSysExtTimSupported_Object = MibScalar
tfrapSysExtTimSupported = _TfrapSysExtTimSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 6),
    _TfrapSysExtTimSupported_Type()
)
tfrapSysExtTimSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysExtTimSupported.setStatus("mandatory")


class _TfrapSysBRISupported_Type(DisplayString):
    """Custom type tfrapSysBRISupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysBRISupported_Type.__name__ = "DisplayString"
_TfrapSysBRISupported_Object = MibScalar
tfrapSysBRISupported = _TfrapSysBRISupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 7),
    _TfrapSysBRISupported_Type()
)
tfrapSysBRISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysBRISupported.setStatus("mandatory")


class _TfrapSysSelDTESupported_Type(DisplayString):
    """Custom type tfrapSysSelDTESupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysSelDTESupported_Type.__name__ = "DisplayString"
_TfrapSysSelDTESupported_Object = MibScalar
tfrapSysSelDTESupported = _TfrapSysSelDTESupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 8),
    _TfrapSysSelDTESupported_Type()
)
tfrapSysSelDTESupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysSelDTESupported.setStatus("mandatory")


class _TfrapSysMLSupported_Type(DisplayString):
    """Custom type tfrapSysMLSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TfrapSysMLSupported_Type.__name__ = "DisplayString"
_TfrapSysMLSupported_Object = MibScalar
tfrapSysMLSupported = _TfrapSysMLSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 9),
    _TfrapSysMLSupported_Type()
)
tfrapSysMLSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysMLSupported.setStatus("mandatory")
_TfrapSysNumDlcisSupported_Type = Integer32
_TfrapSysNumDlcisSupported_Object = MibScalar
tfrapSysNumDlcisSupported = _TfrapSysNumDlcisSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 10),
    _TfrapSysNumDlcisSupported_Type()
)
tfrapSysNumDlcisSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumDlcisSupported.setStatus("mandatory")
_TfrapSysLTFNumDlcis_Type = Integer32
_TfrapSysLTFNumDlcis_Object = MibScalar
tfrapSysLTFNumDlcis = _TfrapSysLTFNumDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 11),
    _TfrapSysLTFNumDlcis_Type()
)
tfrapSysLTFNumDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysLTFNumDlcis.setStatus("mandatory")
_TfrapSysLTFNumProtocols_Type = Integer32
_TfrapSysLTFNumProtocols_Object = MibScalar
tfrapSysLTFNumProtocols = _TfrapSysLTFNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 12),
    _TfrapSysLTFNumProtocols_Type()
)
tfrapSysLTFNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysLTFNumProtocols.setStatus("mandatory")
_TfrapSysNumUserProtocols_Type = Integer32
_TfrapSysNumUserProtocols_Object = MibScalar
tfrapSysNumUserProtocols = _TfrapSysNumUserProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 13),
    _TfrapSysNumUserProtocols_Type()
)
tfrapSysNumUserProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumUserProtocols.setStatus("mandatory")
_TfrapSysNumSnmpMgrs_Type = Integer32
_TfrapSysNumSnmpMgrs_Object = MibScalar
tfrapSysNumSnmpMgrs = _TfrapSysNumSnmpMgrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 14),
    _TfrapSysNumSnmpMgrs_Type()
)
tfrapSysNumSnmpMgrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumSnmpMgrs.setStatus("mandatory")
_TfrapSysNumDlciNames_Type = Integer32
_TfrapSysNumDlciNames_Object = MibScalar
tfrapSysNumDlciNames = _TfrapSysNumDlciNames_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 1, 2, 15),
    _TfrapSysNumDlciNames_Type()
)
tfrapSysNumDlciNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapSysNumDlciNames.setStatus("mandatory")
_TfrapConfiguration_ObjectIdentity = ObjectIdentity
tfrapConfiguration = _TfrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2)
)
_TfrapCfgMgmtTable_ObjectIdentity = ObjectIdentity
tfrapCfgMgmtTable = _TfrapCfgMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1)
)
_TfrapCfgIpTable_ObjectIdentity = ObjectIdentity
tfrapCfgIpTable = _TfrapCfgIpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1)
)
_TfrapCfgIpMyIP_Type = IpAddress
_TfrapCfgIpMyIP_Object = MibScalar
tfrapCfgIpMyIP = _TfrapCfgIpMyIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 1),
    _TfrapCfgIpMyIP_Type()
)
tfrapCfgIpMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpMyIP.setStatus("mandatory")
_TfrapCfgIpPeerIP_Type = IpAddress
_TfrapCfgIpPeerIP_Object = MibScalar
tfrapCfgIpPeerIP = _TfrapCfgIpPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 2),
    _TfrapCfgIpPeerIP_Type()
)
tfrapCfgIpPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpPeerIP.setStatus("mandatory")
_TfrapCfgIpMask_Type = IpAddress
_TfrapCfgIpMask_Object = MibScalar
tfrapCfgIpMask = _TfrapCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 3),
    _TfrapCfgIpMask_Type()
)
tfrapCfgIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpMask.setStatus("mandatory")


class _TfrapCfgIpMaxMTU_Type(Integer32):
    """Custom type tfrapCfgIpMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TfrapCfgIpMaxMTU_Type.__name__ = "Integer32"
_TfrapCfgIpMaxMTU_Object = MibScalar
tfrapCfgIpMaxMTU = _TfrapCfgIpMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 4),
    _TfrapCfgIpMaxMTU_Type()
)
tfrapCfgIpMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpMaxMTU.setStatus("mandatory")


class _TfrapCfgIpChannel_Type(Integer32):
    """Custom type tfrapCfgIpChannel based on Integer32"""
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


_TfrapCfgIpChannel_Type.__name__ = "Integer32"
_TfrapCfgIpChannel_Object = MibScalar
tfrapCfgIpChannel = _TfrapCfgIpChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 5),
    _TfrapCfgIpChannel_Type()
)
tfrapCfgIpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgIpChannel.setStatus("mandatory")


class _TfrapCfgIpTelnetEnable_Type(Integer32):
    """Custom type tfrapCfgIpTelnetEnable based on Integer32"""
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


_TfrapCfgIpTelnetEnable_Type.__name__ = "Integer32"
_TfrapCfgIpTelnetEnable_Object = MibScalar
tfrapCfgIpTelnetEnable = _TfrapCfgIpTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 6),
    _TfrapCfgIpTelnetEnable_Type()
)
tfrapCfgIpTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpTelnetEnable.setStatus("mandatory")


class _TfrapCfgIpTelnetAutoLogOut_Type(Integer32):
    """Custom type tfrapCfgIpTelnetAutoLogOut based on Integer32"""
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


_TfrapCfgIpTelnetAutoLogOut_Type.__name__ = "Integer32"
_TfrapCfgIpTelnetAutoLogOut_Object = MibScalar
tfrapCfgIpTelnetAutoLogOut = _TfrapCfgIpTelnetAutoLogOut_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 1, 7),
    _TfrapCfgIpTelnetAutoLogOut_Type()
)
tfrapCfgIpTelnetAutoLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgIpTelnetAutoLogOut.setStatus("mandatory")
_TfrapCfgTftpTable_ObjectIdentity = ObjectIdentity
tfrapCfgTftpTable = _TfrapCfgTftpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2)
)


class _TfrapCfgTftpInitiate_Type(DisplayString):
    """Custom type tfrapCfgTftpInitiate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgTftpInitiate_Type.__name__ = "DisplayString"
_TfrapCfgTftpInitiate_Object = MibScalar
tfrapCfgTftpInitiate = _TfrapCfgTftpInitiate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 1),
    _TfrapCfgTftpInitiate_Type()
)
tfrapCfgTftpInitiate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgTftpInitiate.setStatus("mandatory")
_TfrapCfgTftpIpAddress_Type = IpAddress
_TfrapCfgTftpIpAddress_Object = MibScalar
tfrapCfgTftpIpAddress = _TfrapCfgTftpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 2),
    _TfrapCfgTftpIpAddress_Type()
)
tfrapCfgTftpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpIpAddress.setStatus("mandatory")


class _TfrapCfgTftpFilename_Type(DisplayString):
    """Custom type tfrapCfgTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TfrapCfgTftpFilename_Type.__name__ = "DisplayString"
_TfrapCfgTftpFilename_Object = MibScalar
tfrapCfgTftpFilename = _TfrapCfgTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 3),
    _TfrapCfgTftpFilename_Type()
)
tfrapCfgTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpFilename.setStatus("mandatory")


class _TfrapCfgTftpInterface_Type(Integer32):
    """Custom type tfrapCfgTftpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte-interface", 1),
          ("slip-interface", 3),
          ("t1-interface", 2))
    )


_TfrapCfgTftpInterface_Type.__name__ = "Integer32"
_TfrapCfgTftpInterface_Object = MibScalar
tfrapCfgTftpInterface = _TfrapCfgTftpInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 4),
    _TfrapCfgTftpInterface_Type()
)
tfrapCfgTftpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpInterface.setStatus("mandatory")


class _TfrapCfgTftpDlci_Type(Integer32):
    """Custom type tfrapCfgTftpDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63487),
    )


_TfrapCfgTftpDlci_Type.__name__ = "Integer32"
_TfrapCfgTftpDlci_Object = MibScalar
tfrapCfgTftpDlci = _TfrapCfgTftpDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 5),
    _TfrapCfgTftpDlci_Type()
)
tfrapCfgTftpDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpDlci.setStatus("mandatory")


class _TfrapCfgTftpStatus_Type(Integer32):
    """Custom type tfrapCfgTftpStatus based on Integer32"""
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


_TfrapCfgTftpStatus_Type.__name__ = "Integer32"
_TfrapCfgTftpStatus_Object = MibScalar
tfrapCfgTftpStatus = _TfrapCfgTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 6),
    _TfrapCfgTftpStatus_Type()
)
tfrapCfgTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpStatus.setStatus("mandatory")
_TfrapCfgTftpNumBytes_Type = Counter32
_TfrapCfgTftpNumBytes_Object = MibScalar
tfrapCfgTftpNumBytes = _TfrapCfgTftpNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 2, 7),
    _TfrapCfgTftpNumBytes_Type()
)
tfrapCfgTftpNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgTftpNumBytes.setStatus("mandatory")
_TfrapCfgSnmpTable_ObjectIdentity = ObjectIdentity
tfrapCfgSnmpTable = _TfrapCfgSnmpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3)
)


class _TfrapCfgSnmpFrTrap_Type(Integer32):
    """Custom type tfrapCfgSnmpFrTrap based on Integer32"""
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


_TfrapCfgSnmpFrTrap_Type.__name__ = "Integer32"
_TfrapCfgSnmpFrTrap_Object = MibScalar
tfrapCfgSnmpFrTrap = _TfrapCfgSnmpFrTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 1),
    _TfrapCfgSnmpFrTrap_Type()
)
tfrapCfgSnmpFrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpFrTrap.setStatus("mandatory")
_TfrapCfgSnmpMgrTable_Object = MibTable
tfrapCfgSnmpMgrTable = _TfrapCfgSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrTable.setStatus("mandatory")
_TfrapCfgSnmpMgrEntry_Object = MibTableRow
tfrapCfgSnmpMgrEntry = _TfrapCfgSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2, 1)
)
tfrapCfgSnmpMgrEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgSnmpMgrIndex"),
)
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrEntry.setStatus("mandatory")
_TfrapCfgSnmpMgrIndex_Type = Integer32
_TfrapCfgSnmpMgrIndex_Object = MibTableColumn
tfrapCfgSnmpMgrIndex = _TfrapCfgSnmpMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2, 1, 1),
    _TfrapCfgSnmpMgrIndex_Type()
)
tfrapCfgSnmpMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrIndex.setStatus("mandatory")
_TfrapCfgSnmpMgrIP_Type = IpAddress
_TfrapCfgSnmpMgrIP_Object = MibTableColumn
tfrapCfgSnmpMgrIP = _TfrapCfgSnmpMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2, 1, 2),
    _TfrapCfgSnmpMgrIP_Type()
)
tfrapCfgSnmpMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrIP.setStatus("mandatory")


class _TfrapCfgSnmpMgrInterface_Type(Integer32):
    """Custom type tfrapCfgSnmpMgrInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte-interface", 1),
          ("slip-interface", 3),
          ("t1-interface", 2))
    )


_TfrapCfgSnmpMgrInterface_Type.__name__ = "Integer32"
_TfrapCfgSnmpMgrInterface_Object = MibTableColumn
tfrapCfgSnmpMgrInterface = _TfrapCfgSnmpMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2, 1, 3),
    _TfrapCfgSnmpMgrInterface_Type()
)
tfrapCfgSnmpMgrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrInterface.setStatus("mandatory")
_TfrapCfgSnmpMgrDlci_Type = Integer32
_TfrapCfgSnmpMgrDlci_Object = MibTableColumn
tfrapCfgSnmpMgrDlci = _TfrapCfgSnmpMgrDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 2, 1, 4),
    _TfrapCfgSnmpMgrDlci_Type()
)
tfrapCfgSnmpMgrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrDlci.setStatus("mandatory")


class _TfrapCfgSnmpTrapMuting_Type(Integer32):
    """Custom type tfrapCfgSnmpTrapMuting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_TfrapCfgSnmpTrapMuting_Type.__name__ = "Integer32"
_TfrapCfgSnmpTrapMuting_Object = MibScalar
tfrapCfgSnmpTrapMuting = _TfrapCfgSnmpTrapMuting_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 3),
    _TfrapCfgSnmpTrapMuting_Type()
)
tfrapCfgSnmpTrapMuting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpTrapMuting.setStatus("mandatory")


class _TfrapCfgSnmpUtilTrapEnable_Type(Integer32):
    """Custom type tfrapCfgSnmpUtilTrapEnable based on Integer32"""
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


_TfrapCfgSnmpUtilTrapEnable_Type.__name__ = "Integer32"
_TfrapCfgSnmpUtilTrapEnable_Object = MibScalar
tfrapCfgSnmpUtilTrapEnable = _TfrapCfgSnmpUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 6),
    _TfrapCfgSnmpUtilTrapEnable_Type()
)
tfrapCfgSnmpUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSnmpUtilTrapEnable.setStatus("mandatory")
_TfrapCfgSnmpMgrClearN_Type = Integer32
_TfrapCfgSnmpMgrClearN_Object = MibScalar
tfrapCfgSnmpMgrClearN = _TfrapCfgSnmpMgrClearN_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 3, 7),
    _TfrapCfgSnmpMgrClearN_Type()
)
tfrapCfgSnmpMgrClearN.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgSnmpMgrClearN.setStatus("mandatory")
_TfrapCfgCommTable_ObjectIdentity = ObjectIdentity
tfrapCfgCommTable = _TfrapCfgCommTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4)
)


class _TfrapCfgCommMode_Type(Integer32):
    """Custom type tfrapCfgCommMode based on Integer32"""
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


_TfrapCfgCommMode_Type.__name__ = "Integer32"
_TfrapCfgCommMode_Object = MibScalar
tfrapCfgCommMode = _TfrapCfgCommMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 1),
    _TfrapCfgCommMode_Type()
)
tfrapCfgCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommMode.setStatus("mandatory")


class _TfrapCfgCommBaud_Type(Integer32):
    """Custom type tfrapCfgCommBaud based on Integer32"""
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


_TfrapCfgCommBaud_Type.__name__ = "Integer32"
_TfrapCfgCommBaud_Object = MibScalar
tfrapCfgCommBaud = _TfrapCfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 2),
    _TfrapCfgCommBaud_Type()
)
tfrapCfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommBaud.setStatus("mandatory")


class _TfrapCfgCommDataBits_Type(Integer32):
    """Custom type tfrapCfgCommDataBits based on Integer32"""
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


_TfrapCfgCommDataBits_Type.__name__ = "Integer32"
_TfrapCfgCommDataBits_Object = MibScalar
tfrapCfgCommDataBits = _TfrapCfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 3),
    _TfrapCfgCommDataBits_Type()
)
tfrapCfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommDataBits.setStatus("mandatory")


class _TfrapCfgCommStopBits_Type(Integer32):
    """Custom type tfrapCfgCommStopBits based on Integer32"""
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


_TfrapCfgCommStopBits_Type.__name__ = "Integer32"
_TfrapCfgCommStopBits_Object = MibScalar
tfrapCfgCommStopBits = _TfrapCfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 4),
    _TfrapCfgCommStopBits_Type()
)
tfrapCfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommStopBits.setStatus("mandatory")


class _TfrapCfgCommParity_Type(Integer32):
    """Custom type tfrapCfgCommParity based on Integer32"""
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


_TfrapCfgCommParity_Type.__name__ = "Integer32"
_TfrapCfgCommParity_Object = MibScalar
tfrapCfgCommParity = _TfrapCfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 5),
    _TfrapCfgCommParity_Type()
)
tfrapCfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommParity.setStatus("mandatory")


class _TfrapCfgCommFlowCtrl_Type(Integer32):
    """Custom type tfrapCfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("no-flow-control", 1)
    )


_TfrapCfgCommFlowCtrl_Type.__name__ = "Integer32"
_TfrapCfgCommFlowCtrl_Object = MibScalar
tfrapCfgCommFlowCtrl = _TfrapCfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 4, 6),
    _TfrapCfgCommFlowCtrl_Type()
)
tfrapCfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCommFlowCtrl.setStatus("mandatory")
_TfrapCfgFrDLCITable_ObjectIdentity = ObjectIdentity
tfrapCfgFrDLCITable = _TfrapCfgFrDLCITable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 5)
)


class _TfrapCfgFrDLCIMode_Type(Integer32):
    """Custom type tfrapCfgFrDLCIMode based on Integer32"""
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
          ("local", 2),
          ("piggyback", 5),
          ("remote", 3))
    )


_TfrapCfgFrDLCIMode_Type.__name__ = "Integer32"
_TfrapCfgFrDLCIMode_Object = MibScalar
tfrapCfgFrDLCIMode = _TfrapCfgFrDLCIMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 5, 1),
    _TfrapCfgFrDLCIMode_Type()
)
tfrapCfgFrDLCIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrDLCIMode.setStatus("mandatory")


class _TfrapCfgFrDLCIValue_Type(Integer32):
    """Custom type tfrapCfgFrDLCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 63487),
    )


_TfrapCfgFrDLCIValue_Type.__name__ = "Integer32"
_TfrapCfgFrDLCIValue_Object = MibScalar
tfrapCfgFrDLCIValue = _TfrapCfgFrDLCIValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 5, 2),
    _TfrapCfgFrDLCIValue_Type()
)
tfrapCfgFrDLCIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrDLCIValue.setStatus("mandatory")


class _TfrapCfgFrDLCIEncap_Type(Integer32):
    """Custom type tfrapCfgFrDLCIEncap based on Integer32"""
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


_TfrapCfgFrDLCIEncap_Type.__name__ = "Integer32"
_TfrapCfgFrDLCIEncap_Object = MibScalar
tfrapCfgFrDLCIEncap = _TfrapCfgFrDLCIEncap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 5, 3),
    _TfrapCfgFrDLCIEncap_Type()
)
tfrapCfgFrDLCIEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrDLCIEncap.setStatus("mandatory")


class _TfrapCfgFrDLCIMgmtDE_Type(Integer32):
    """Custom type tfrapCfgFrDLCIMgmtDE based on Integer32"""
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


_TfrapCfgFrDLCIMgmtDE_Type.__name__ = "Integer32"
_TfrapCfgFrDLCIMgmtDE_Object = MibScalar
tfrapCfgFrDLCIMgmtDE = _TfrapCfgFrDLCIMgmtDE_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 1, 5, 4),
    _TfrapCfgFrDLCIMgmtDE_Type()
)
tfrapCfgFrDLCIMgmtDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrDLCIMgmtDE.setStatus("mandatory")
_TfrapCfgAppTable_ObjectIdentity = ObjectIdentity
tfrapCfgAppTable = _TfrapCfgAppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2)
)


class _TfrapCfgAppClockSource_Type(Integer32):
    """Custom type tfrapCfgAppClockSource based on Integer32"""
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


_TfrapCfgAppClockSource_Type.__name__ = "Integer32"
_TfrapCfgAppClockSource_Object = MibScalar
tfrapCfgAppClockSource = _TfrapCfgAppClockSource_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 1),
    _TfrapCfgAppClockSource_Type()
)
tfrapCfgAppClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppClockSource.setStatus("mandatory")


class _TfrapCfgAppCircuitId_Type(DisplayString):
    """Custom type tfrapCfgAppCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TfrapCfgAppCircuitId_Type.__name__ = "DisplayString"
_TfrapCfgAppCircuitId_Object = MibScalar
tfrapCfgAppCircuitId = _TfrapCfgAppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 2),
    _TfrapCfgAppCircuitId_Type()
)
tfrapCfgAppCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppCircuitId.setStatus("mandatory")


class _TfrapCfgAppType_Type(Integer32):
    """Custom type tfrapCfgAppType based on Integer32"""
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


_TfrapCfgAppType_Type.__name__ = "Integer32"
_TfrapCfgAppType_Object = MibScalar
tfrapCfgAppType = _TfrapCfgAppType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 3),
    _TfrapCfgAppType_Type()
)
tfrapCfgAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppType.setStatus("mandatory")


class _TfrapCfgAppFormat_Type(Integer32):
    """Custom type tfrapCfgAppFormat based on Integer32"""
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


_TfrapCfgAppFormat_Type.__name__ = "Integer32"
_TfrapCfgAppFormat_Object = MibScalar
tfrapCfgAppFormat = _TfrapCfgAppFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 4),
    _TfrapCfgAppFormat_Type()
)
tfrapCfgAppFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppFormat.setStatus("mandatory")


class _TfrapCfgAppLpbkTimeout_Type(Integer32):
    """Custom type tfrapCfgAppLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TfrapCfgAppLpbkTimeout_Type.__name__ = "Integer32"
_TfrapCfgAppLpbkTimeout_Object = MibScalar
tfrapCfgAppLpbkTimeout = _TfrapCfgAppLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 5),
    _TfrapCfgAppLpbkTimeout_Type()
)
tfrapCfgAppLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppLpbkTimeout.setStatus("mandatory")


class _TfrapCfgAppPerfBuffLimit_Type(Integer32):
    """Custom type tfrapCfgAppPerfBuffLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_TfrapCfgAppPerfBuffLimit_Type.__name__ = "Integer32"
_TfrapCfgAppPerfBuffLimit_Object = MibScalar
tfrapCfgAppPerfBuffLimit = _TfrapCfgAppPerfBuffLimit_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 2, 10),
    _TfrapCfgAppPerfBuffLimit_Type()
)
tfrapCfgAppPerfBuffLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgAppPerfBuffLimit.setStatus("mandatory")
_TfrapCfgT1Table_ObjectIdentity = ObjectIdentity
tfrapCfgT1Table = _TfrapCfgT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3)
)


class _TfrapCfgT1Framing_Type(Integer32):
    """Custom type tfrapCfgT1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf-54016", 2),
          ("esf-ansi", 3))
    )


_TfrapCfgT1Framing_Type.__name__ = "Integer32"
_TfrapCfgT1Framing_Object = MibScalar
tfrapCfgT1Framing = _TfrapCfgT1Framing_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3, 1),
    _TfrapCfgT1Framing_Type()
)
tfrapCfgT1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgT1Framing.setStatus("mandatory")


class _TfrapCfgT1LineEncoding_Type(Integer32):
    """Custom type tfrapCfgT1LineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_TfrapCfgT1LineEncoding_Type.__name__ = "Integer32"
_TfrapCfgT1LineEncoding_Object = MibScalar
tfrapCfgT1LineEncoding = _TfrapCfgT1LineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3, 2),
    _TfrapCfgT1LineEncoding_Type()
)
tfrapCfgT1LineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgT1LineEncoding.setStatus("mandatory")


class _TfrapCfgT1Density_Type(Integer32):
    """Custom type tfrapCfgT1Density based on Integer32"""
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
        *(("no-density", 1),
          ("one-in-16", 3),
          ("one-in-64", 4),
          ("twelve-half-percent", 2))
    )


_TfrapCfgT1Density_Type.__name__ = "Integer32"
_TfrapCfgT1Density_Object = MibScalar
tfrapCfgT1Density = _TfrapCfgT1Density_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3, 3),
    _TfrapCfgT1Density_Type()
)
tfrapCfgT1Density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgT1Density.setStatus("mandatory")


class _TfrapCfgT1Interface_Type(Integer32):
    """Custom type tfrapCfgT1Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 2),
          ("dsx-1", 1))
    )


_TfrapCfgT1Interface_Type.__name__ = "Integer32"
_TfrapCfgT1Interface_Object = MibScalar
tfrapCfgT1Interface = _TfrapCfgT1Interface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3, 4),
    _TfrapCfgT1Interface_Type()
)
tfrapCfgT1Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgT1Interface.setStatus("mandatory")


class _TfrapCfgT1LboSetting_Type(Integer32):
    """Custom type tfrapCfgT1LboSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n15-db", 3),
          ("n7-5-db", 2),
          ("zero-db", 1))
    )


_TfrapCfgT1LboSetting_Type.__name__ = "Integer32"
_TfrapCfgT1LboSetting_Object = MibScalar
tfrapCfgT1LboSetting = _TfrapCfgT1LboSetting_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 3, 5),
    _TfrapCfgT1LboSetting_Type()
)
tfrapCfgT1LboSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgT1LboSetting.setStatus("mandatory")
_TfrapCfgDteTable_ObjectIdentity = ObjectIdentity
tfrapCfgDteTable = _TfrapCfgDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4)
)


class _TfrapCfgDteIntfType_Type(Integer32):
    """Custom type tfrapCfgDteIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("intf-v35", 3)
    )


_TfrapCfgDteIntfType_Type.__name__ = "Integer32"
_TfrapCfgDteIntfType_Object = MibScalar
tfrapCfgDteIntfType = _TfrapCfgDteIntfType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 1),
    _TfrapCfgDteIntfType_Type()
)
tfrapCfgDteIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteIntfType.setStatus("mandatory")


class _TfrapCfgDteDataMode_Type(Integer32):
    """Custom type tfrapCfgDteDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-invert", 2),
          ("data-normal", 1))
    )


_TfrapCfgDteDataMode_Type.__name__ = "Integer32"
_TfrapCfgDteDataMode_Object = MibScalar
tfrapCfgDteDataMode = _TfrapCfgDteDataMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 2),
    _TfrapCfgDteDataMode_Type()
)
tfrapCfgDteDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteDataMode.setStatus("mandatory")


class _TfrapCfgDteClockMode_Type(Integer32):
    """Custom type tfrapCfgDteClockMode based on Integer32"""
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


_TfrapCfgDteClockMode_Type.__name__ = "Integer32"
_TfrapCfgDteClockMode_Object = MibScalar
tfrapCfgDteClockMode = _TfrapCfgDteClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 3),
    _TfrapCfgDteClockMode_Type()
)
tfrapCfgDteClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteClockMode.setStatus("mandatory")


class _TfrapCfgDteTiming_Type(Integer32):
    """Custom type tfrapCfgDteTiming based on Integer32"""
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


_TfrapCfgDteTiming_Type.__name__ = "Integer32"
_TfrapCfgDteTiming_Object = MibScalar
tfrapCfgDteTiming = _TfrapCfgDteTiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 4),
    _TfrapCfgDteTiming_Type()
)
tfrapCfgDteTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteTiming.setStatus("mandatory")


class _TfrapCfgDteLineRate_Type(Integer32):
    """Custom type tfrapCfgDteLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_TfrapCfgDteLineRate_Type.__name__ = "Integer32"
_TfrapCfgDteLineRate_Object = MibScalar
tfrapCfgDteLineRate = _TfrapCfgDteLineRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 5),
    _TfrapCfgDteLineRate_Type()
)
tfrapCfgDteLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteLineRate.setStatus("mandatory")


class _TfrapCfgDteChannelDensity_Type(Integer32):
    """Custom type tfrapCfgDteChannelDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("bit-7-stuff", 56),
          ("clear-channel", 64))
    )


_TfrapCfgDteChannelDensity_Type.__name__ = "Integer32"
_TfrapCfgDteChannelDensity_Object = MibScalar
tfrapCfgDteChannelDensity = _TfrapCfgDteChannelDensity_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 6),
    _TfrapCfgDteChannelDensity_Type()
)
tfrapCfgDteChannelDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteChannelDensity.setStatus("mandatory")


class _TfrapCfgDteStartDs0_Type(Integer32):
    """Custom type tfrapCfgDteStartDs0 based on Integer32"""
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
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ds0-01", 1),
          ("ds0-02", 2),
          ("ds0-03", 3),
          ("ds0-04", 4),
          ("ds0-05", 5),
          ("ds0-06", 6),
          ("ds0-07", 7),
          ("ds0-08", 8),
          ("ds0-09", 9),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("no-current-connections", 40),
          ("non-continuous-ds0s", 41))
    )


_TfrapCfgDteStartDs0_Type.__name__ = "Integer32"
_TfrapCfgDteStartDs0_Object = MibScalar
tfrapCfgDteStartDs0 = _TfrapCfgDteStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 7),
    _TfrapCfgDteStartDs0_Type()
)
tfrapCfgDteStartDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteStartDs0.setStatus("mandatory")


class _TfrapCfgDteConnStatus_Type(Integer32):
    """Custom type tfrapCfgDteConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connections-valid", 1),
          ("no-current-connections", 4))
    )


_TfrapCfgDteConnStatus_Type.__name__ = "Integer32"
_TfrapCfgDteConnStatus_Object = MibScalar
tfrapCfgDteConnStatus = _TfrapCfgDteConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 8),
    _TfrapCfgDteConnStatus_Type()
)
tfrapCfgDteConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteConnStatus.setStatus("mandatory")


class _TfrapCfgDteConnStartDs0_Type(Integer32):
    """Custom type tfrapCfgDteConnStartDs0 based on Integer32"""
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
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ds0-01", 1),
          ("ds0-02", 2),
          ("ds0-03", 3),
          ("ds0-04", 4),
          ("ds0-05", 5),
          ("ds0-06", 6),
          ("ds0-07", 7),
          ("ds0-08", 8),
          ("ds0-09", 9),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("no-current-connections", 40),
          ("non-continuous-ds0s", 41))
    )


_TfrapCfgDteConnStartDs0_Type.__name__ = "Integer32"
_TfrapCfgDteConnStartDs0_Object = MibScalar
tfrapCfgDteConnStartDs0 = _TfrapCfgDteConnStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 9),
    _TfrapCfgDteConnStartDs0_Type()
)
tfrapCfgDteConnStartDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteConnStartDs0.setStatus("mandatory")


class _TfrapCfgDteConnRate_Type(Integer32):
    """Custom type tfrapCfgDteConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_TfrapCfgDteConnRate_Type.__name__ = "Integer32"
_TfrapCfgDteConnRate_Object = MibScalar
tfrapCfgDteConnRate = _TfrapCfgDteConnRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 10),
    _TfrapCfgDteConnRate_Type()
)
tfrapCfgDteConnRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteConnRate.setStatus("mandatory")


class _TfrapCfgDteConnDensity_Type(Integer32):
    """Custom type tfrapCfgDteConnDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("bit-7-stuff", 56),
          ("clear-channel", 64))
    )


_TfrapCfgDteConnDensity_Type.__name__ = "Integer32"
_TfrapCfgDteConnDensity_Object = MibScalar
tfrapCfgDteConnDensity = _TfrapCfgDteConnDensity_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 11),
    _TfrapCfgDteConnDensity_Type()
)
tfrapCfgDteConnDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteConnDensity.setStatus("mandatory")


class _TfrapCfgDteConnDs0Required_Type(Integer32):
    """Custom type tfrapCfgDteConnDs0Required based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_TfrapCfgDteConnDs0Required_Type.__name__ = "Integer32"
_TfrapCfgDteConnDs0Required_Object = MibScalar
tfrapCfgDteConnDs0Required = _TfrapCfgDteConnDs0Required_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 12),
    _TfrapCfgDteConnDs0Required_Type()
)
tfrapCfgDteConnDs0Required.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteConnDs0Required.setStatus("mandatory")


class _TfrapCfgDteConnAutoStatus_Type(Integer32):
    """Custom type tfrapCfgDteConnAutoStatus based on Integer32"""
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
        *(("configuration-invalid", 2),
          ("configuration-valid", 1),
          ("invalid-cfg-no-update", 4),
          ("valid-config-updated", 3))
    )


_TfrapCfgDteConnAutoStatus_Type.__name__ = "Integer32"
_TfrapCfgDteConnAutoStatus_Object = MibScalar
tfrapCfgDteConnAutoStatus = _TfrapCfgDteConnAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 13),
    _TfrapCfgDteConnAutoStatus_Type()
)
tfrapCfgDteConnAutoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgDteConnAutoStatus.setStatus("mandatory")


class _TfrapCfgDteConnAutoUpdate_Type(Integer32):
    """Custom type tfrapCfgDteConnAutoUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("config-and-connect", 1)
    )


_TfrapCfgDteConnAutoUpdate_Type.__name__ = "Integer32"
_TfrapCfgDteConnAutoUpdate_Object = MibScalar
tfrapCfgDteConnAutoUpdate = _TfrapCfgDteConnAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 14),
    _TfrapCfgDteConnAutoUpdate_Type()
)
tfrapCfgDteConnAutoUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgDteConnAutoUpdate.setStatus("mandatory")


class _TfrapCfgDteRts_Type(Integer32):
    """Custom type tfrapCfgDteRts based on Integer32"""
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


_TfrapCfgDteRts_Type.__name__ = "Integer32"
_TfrapCfgDteRts_Object = MibScalar
tfrapCfgDteRts = _TfrapCfgDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 15),
    _TfrapCfgDteRts_Type()
)
tfrapCfgDteRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteRts.setStatus("mandatory")


class _TfrapCfgDteDtr_Type(Integer32):
    """Custom type tfrapCfgDteDtr based on Integer32"""
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


_TfrapCfgDteDtr_Type.__name__ = "Integer32"
_TfrapCfgDteDtr_Object = MibScalar
tfrapCfgDteDtr = _TfrapCfgDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 16),
    _TfrapCfgDteDtr_Type()
)
tfrapCfgDteDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteDtr.setStatus("mandatory")


class _TfrapCfgDteDcdOutput_Type(Integer32):
    """Custom type tfrapCfgDteDcdOutput based on Integer32"""
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


_TfrapCfgDteDcdOutput_Type.__name__ = "Integer32"
_TfrapCfgDteDcdOutput_Object = MibScalar
tfrapCfgDteDcdOutput = _TfrapCfgDteDcdOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 18),
    _TfrapCfgDteDcdOutput_Type()
)
tfrapCfgDteDcdOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteDcdOutput.setStatus("mandatory")


class _TfrapCfgDteDsrOutput_Type(Integer32):
    """Custom type tfrapCfgDteDsrOutput based on Integer32"""
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


_TfrapCfgDteDsrOutput_Type.__name__ = "Integer32"
_TfrapCfgDteDsrOutput_Object = MibScalar
tfrapCfgDteDsrOutput = _TfrapCfgDteDsrOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 19),
    _TfrapCfgDteDsrOutput_Type()
)
tfrapCfgDteDsrOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteDsrOutput.setStatus("mandatory")


class _TfrapCfgDteCtsOutput_Type(Integer32):
    """Custom type tfrapCfgDteCtsOutput based on Integer32"""
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


_TfrapCfgDteCtsOutput_Type.__name__ = "Integer32"
_TfrapCfgDteCtsOutput_Object = MibScalar
tfrapCfgDteCtsOutput = _TfrapCfgDteCtsOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 4, 20),
    _TfrapCfgDteCtsOutput_Type()
)
tfrapCfgDteCtsOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgDteCtsOutput.setStatus("mandatory")
_TfrapCfgFrTable_ObjectIdentity = ObjectIdentity
tfrapCfgFrTable = _TfrapCfgFrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5)
)


class _TfrapCfgFrAddrLen_Type(Integer32):
    """Custom type tfrapCfgFrAddrLen based on Integer32"""
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


_TfrapCfgFrAddrLen_Type.__name__ = "Integer32"
_TfrapCfgFrAddrLen_Object = MibScalar
tfrapCfgFrAddrLen = _TfrapCfgFrAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 1),
    _TfrapCfgFrAddrLen_Type()
)
tfrapCfgFrAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrAddrLen.setStatus("mandatory")


class _TfrapCfgFrCrcMode_Type(Integer32):
    """Custom type tfrapCfgFrCrcMode based on Integer32"""
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


_TfrapCfgFrCrcMode_Type.__name__ = "Integer32"
_TfrapCfgFrCrcMode_Object = MibScalar
tfrapCfgFrCrcMode = _TfrapCfgFrCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 2),
    _TfrapCfgFrCrcMode_Type()
)
tfrapCfgFrCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrCrcMode.setStatus("mandatory")


class _TfrapCfgFrLmiType_Type(Integer32):
    """Custom type tfrapCfgFrLmiType based on Integer32"""
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


_TfrapCfgFrLmiType_Type.__name__ = "Integer32"
_TfrapCfgFrLmiType_Object = MibScalar
tfrapCfgFrLmiType = _TfrapCfgFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 3),
    _TfrapCfgFrLmiType_Type()
)
tfrapCfgFrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrLmiType.setStatus("mandatory")


class _TfrapCfgFrLmiInactivityTimeout_Type(Integer32):
    """Custom type tfrapCfgFrLmiInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TfrapCfgFrLmiInactivityTimeout_Type.__name__ = "Integer32"
_TfrapCfgFrLmiInactivityTimeout_Object = MibScalar
tfrapCfgFrLmiInactivityTimeout = _TfrapCfgFrLmiInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 4),
    _TfrapCfgFrLmiInactivityTimeout_Type()
)
tfrapCfgFrLmiInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrLmiInactivityTimeout.setStatus("mandatory")


class _TfrapCfgFrLmiKeepaliveTimeout_Type(Integer32):
    """Custom type tfrapCfgFrLmiKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_TfrapCfgFrLmiKeepaliveTimeout_Type.__name__ = "Integer32"
_TfrapCfgFrLmiKeepaliveTimeout_Object = MibScalar
tfrapCfgFrLmiKeepaliveTimeout = _TfrapCfgFrLmiKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 5),
    _TfrapCfgFrLmiKeepaliveTimeout_Type()
)
tfrapCfgFrLmiKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrLmiKeepaliveTimeout.setStatus("mandatory")


class _TfrapCfgFrAddrResMode_Type(Integer32):
    """Custom type tfrapCfgFrAddrResMode based on Integer32"""
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


_TfrapCfgFrAddrResMode_Type.__name__ = "Integer32"
_TfrapCfgFrAddrResMode_Object = MibScalar
tfrapCfgFrAddrResMode = _TfrapCfgFrAddrResMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 6),
    _TfrapCfgFrAddrResMode_Type()
)
tfrapCfgFrAddrResMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrAddrResMode.setStatus("mandatory")


class _TfrapCfgFrAddrResInarpTimer_Type(Integer32):
    """Custom type tfrapCfgFrAddrResInarpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_TfrapCfgFrAddrResInarpTimer_Type.__name__ = "Integer32"
_TfrapCfgFrAddrResInarpTimer_Object = MibScalar
tfrapCfgFrAddrResInarpTimer = _TfrapCfgFrAddrResInarpTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 7),
    _TfrapCfgFrAddrResInarpTimer_Type()
)
tfrapCfgFrAddrResInarpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrAddrResInarpTimer.setStatus("mandatory")


class _TfrapCfgFrLmiFullStatus_Type(Integer32):
    """Custom type tfrapCfgFrLmiFullStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TfrapCfgFrLmiFullStatus_Type.__name__ = "Integer32"
_TfrapCfgFrLmiFullStatus_Object = MibScalar
tfrapCfgFrLmiFullStatus = _TfrapCfgFrLmiFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 8),
    _TfrapCfgFrLmiFullStatus_Type()
)
tfrapCfgFrLmiFullStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrLmiFullStatus.setStatus("mandatory")


class _TfrapCfgFrAddrResDlcis_Type(Integer32):
    """Custom type tfrapCfgFrAddrResDlcis based on Integer32"""
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
        *(("dtemulti", 4),
          ("multiple", 2),
          ("single", 1),
          ("t1multi", 3))
    )


_TfrapCfgFrAddrResDlcis_Type.__name__ = "Integer32"
_TfrapCfgFrAddrResDlcis_Object = MibScalar
tfrapCfgFrAddrResDlcis = _TfrapCfgFrAddrResDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 5, 9),
    _TfrapCfgFrAddrResDlcis_Type()
)
tfrapCfgFrAddrResDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrAddrResDlcis.setStatus("mandatory")
_TfrapCfgVnipTable_ObjectIdentity = ObjectIdentity
tfrapCfgVnipTable = _TfrapCfgVnipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6)
)


class _TfrapCfgVnipMode_Type(Integer32):
    """Custom type tfrapCfgVnipMode based on Integer32"""
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
          ("dte", 2),
          ("inactive", 1),
          ("t1", 3))
    )


_TfrapCfgVnipMode_Type.__name__ = "Integer32"
_TfrapCfgVnipMode_Object = MibScalar
tfrapCfgVnipMode = _TfrapCfgVnipMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 1),
    _TfrapCfgVnipMode_Type()
)
tfrapCfgVnipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgVnipMode.setStatus("mandatory")


class _TfrapCfgVnipInitTimer_Type(Integer32):
    """Custom type tfrapCfgVnipInitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_TfrapCfgVnipInitTimer_Type.__name__ = "Integer32"
_TfrapCfgVnipInitTimer_Object = MibScalar
tfrapCfgVnipInitTimer = _TfrapCfgVnipInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 2),
    _TfrapCfgVnipInitTimer_Type()
)
tfrapCfgVnipInitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgVnipInitTimer.setStatus("mandatory")


class _TfrapCfgVnipKeepAliveTimer_Type(Integer32):
    """Custom type tfrapCfgVnipKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_TfrapCfgVnipKeepAliveTimer_Type.__name__ = "Integer32"
_TfrapCfgVnipKeepAliveTimer_Object = MibScalar
tfrapCfgVnipKeepAliveTimer = _TfrapCfgVnipKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 3),
    _TfrapCfgVnipKeepAliveTimer_Type()
)
tfrapCfgVnipKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgVnipKeepAliveTimer.setStatus("mandatory")


class _TfrapCfgVnipInactivityTimer_Type(Integer32):
    """Custom type tfrapCfgVnipInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_TfrapCfgVnipInactivityTimer_Type.__name__ = "Integer32"
_TfrapCfgVnipInactivityTimer_Object = MibScalar
tfrapCfgVnipInactivityTimer = _TfrapCfgVnipInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 4),
    _TfrapCfgVnipInactivityTimer_Type()
)
tfrapCfgVnipInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgVnipInactivityTimer.setStatus("mandatory")


class _TfrapCfgVnipTransitDelayFrequency_Type(Integer32):
    """Custom type tfrapCfgVnipTransitDelayFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_TfrapCfgVnipTransitDelayFrequency_Type.__name__ = "Integer32"
_TfrapCfgVnipTransitDelayFrequency_Object = MibScalar
tfrapCfgVnipTransitDelayFrequency = _TfrapCfgVnipTransitDelayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 5),
    _TfrapCfgVnipTransitDelayFrequency_Type()
)
tfrapCfgVnipTransitDelayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgVnipTransitDelayFrequency.setStatus("mandatory")
_TfrapCfgTransitDelayTable_Object = MibTable
tfrapCfgTransitDelayTable = _TfrapCfgTransitDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20)
)
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayTable.setStatus("mandatory")
_TfrapCfgTransitDelayEntry_Object = MibTableRow
tfrapCfgTransitDelayEntry = _TfrapCfgTransitDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1)
)
tfrapCfgTransitDelayEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgTransitDelayInterface"),
    (0, "TFRAP-MIB", "tfrapCfgTransitDelayDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayEntry.setStatus("mandatory")


class _TfrapCfgTransitDelayInterface_Type(Integer32):
    """Custom type tfrapCfgTransitDelayInterface based on Integer32"""
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


_TfrapCfgTransitDelayInterface_Type.__name__ = "Integer32"
_TfrapCfgTransitDelayInterface_Object = MibTableColumn
tfrapCfgTransitDelayInterface = _TfrapCfgTransitDelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1, 1),
    _TfrapCfgTransitDelayInterface_Type()
)
tfrapCfgTransitDelayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayInterface.setStatus("mandatory")
_TfrapCfgTransitDelayDlciValue_Type = Integer32
_TfrapCfgTransitDelayDlciValue_Object = MibTableColumn
tfrapCfgTransitDelayDlciValue = _TfrapCfgTransitDelayDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1, 2),
    _TfrapCfgTransitDelayDlciValue_Type()
)
tfrapCfgTransitDelayDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayDlciValue.setStatus("mandatory")


class _TfrapCfgTransitDelayNumHops_Type(Integer32):
    """Custom type tfrapCfgTransitDelayNumHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TfrapCfgTransitDelayNumHops_Type.__name__ = "Integer32"
_TfrapCfgTransitDelayNumHops_Object = MibTableColumn
tfrapCfgTransitDelayNumHops = _TfrapCfgTransitDelayNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1, 4),
    _TfrapCfgTransitDelayNumHops_Type()
)
tfrapCfgTransitDelayNumHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayNumHops.setStatus("mandatory")


class _TfrapCfgTransitDelayRcvSummaryCancel_Type(Integer32):
    """Custom type tfrapCfgTransitDelayRcvSummaryCancel based on Integer32"""
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


_TfrapCfgTransitDelayRcvSummaryCancel_Type.__name__ = "Integer32"
_TfrapCfgTransitDelayRcvSummaryCancel_Object = MibTableColumn
tfrapCfgTransitDelayRcvSummaryCancel = _TfrapCfgTransitDelayRcvSummaryCancel_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1, 5),
    _TfrapCfgTransitDelayRcvSummaryCancel_Type()
)
tfrapCfgTransitDelayRcvSummaryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayRcvSummaryCancel.setStatus("mandatory")


class _TfrapCfgTransitDelayThreshold_Type(Integer32):
    """Custom type tfrapCfgTransitDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_TfrapCfgTransitDelayThreshold_Type.__name__ = "Integer32"
_TfrapCfgTransitDelayThreshold_Object = MibTableColumn
tfrapCfgTransitDelayThreshold = _TfrapCfgTransitDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 20, 1, 6),
    _TfrapCfgTransitDelayThreshold_Type()
)
tfrapCfgTransitDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayThreshold.setStatus("mandatory")
_TfrapCfgTDDeleteTable_Object = MibTable
tfrapCfgTDDeleteTable = _TfrapCfgTDDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 21)
)
if mibBuilder.loadTexts:
    tfrapCfgTDDeleteTable.setStatus("mandatory")
_TfrapCfgTDDeleteEntry_Object = MibTableRow
tfrapCfgTDDeleteEntry = _TfrapCfgTDDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 21, 1)
)
tfrapCfgTDDeleteEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgTDDeleteInterface"),
)
if mibBuilder.loadTexts:
    tfrapCfgTDDeleteEntry.setStatus("mandatory")


class _TfrapCfgTDDeleteInterface_Type(Integer32):
    """Custom type tfrapCfgTDDeleteInterface based on Integer32"""
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


_TfrapCfgTDDeleteInterface_Type.__name__ = "Integer32"
_TfrapCfgTDDeleteInterface_Object = MibTableColumn
tfrapCfgTDDeleteInterface = _TfrapCfgTDDeleteInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 21, 1, 1),
    _TfrapCfgTDDeleteInterface_Type()
)
tfrapCfgTDDeleteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tfrapCfgTDDeleteInterface.setStatus("mandatory")
_TfrapCfgTDDeleteDlciValue_Type = Integer32
_TfrapCfgTDDeleteDlciValue_Object = MibTableColumn
tfrapCfgTDDeleteDlciValue = _TfrapCfgTDDeleteDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 21, 1, 2),
    _TfrapCfgTDDeleteDlciValue_Type()
)
tfrapCfgTDDeleteDlciValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgTDDeleteDlciValue.setStatus("mandatory")


class _TfrapCfgTransitDelayTableClear_Type(Integer32):
    """Custom type tfrapCfgTransitDelayTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_TfrapCfgTransitDelayTableClear_Type.__name__ = "Integer32"
_TfrapCfgTransitDelayTableClear_Object = MibScalar
tfrapCfgTransitDelayTableClear = _TfrapCfgTransitDelayTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 6, 22),
    _TfrapCfgTransitDelayTableClear_Type()
)
tfrapCfgTransitDelayTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgTransitDelayTableClear.setStatus("mandatory")
_TfrapCfgFrPerf_ObjectIdentity = ObjectIdentity
tfrapCfgFrPerf = _TfrapCfgFrPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7)
)
_TfrapCfgFrPerfDlciNamesTable_Object = MibTable
tfrapCfgFrPerfDlciNamesTable = _TfrapCfgFrPerfDlciNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesTable.setStatus("mandatory")
_TfrapCfgFrPerfDlciNamesEntry_Object = MibTableRow
tfrapCfgFrPerfDlciNamesEntry = _TfrapCfgFrPerfDlciNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1)
)
tfrapCfgFrPerfDlciNamesEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgFrPerfDlciNamesDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesEntry.setStatus("mandatory")
_TfrapCfgFrPerfDlciNamesDlciValue_Type = Integer32
_TfrapCfgFrPerfDlciNamesDlciValue_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesDlciValue = _TfrapCfgFrPerfDlciNamesDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 1),
    _TfrapCfgFrPerfDlciNamesDlciValue_Type()
)
tfrapCfgFrPerfDlciNamesDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesDlciValue.setStatus("mandatory")


class _TfrapCfgFrPerfDlciNamesDlciName_Type(DisplayString):
    """Custom type tfrapCfgFrPerfDlciNamesDlciName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TfrapCfgFrPerfDlciNamesDlciName_Type.__name__ = "DisplayString"
_TfrapCfgFrPerfDlciNamesDlciName_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesDlciName = _TfrapCfgFrPerfDlciNamesDlciName_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 2),
    _TfrapCfgFrPerfDlciNamesDlciName_Type()
)
tfrapCfgFrPerfDlciNamesDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesDlciName.setStatus("mandatory")
_TfrapCfgFrPerfDlciNamesCirValue_Type = Integer32
_TfrapCfgFrPerfDlciNamesCirValue_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesCirValue = _TfrapCfgFrPerfDlciNamesCirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 3),
    _TfrapCfgFrPerfDlciNamesCirValue_Type()
)
tfrapCfgFrPerfDlciNamesCirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesCirValue.setStatus("mandatory")


class _TfrapCfgFrPerfDlciNamesCirType_Type(Integer32):
    """Custom type tfrapCfgFrPerfDlciNamesCirType based on Integer32"""
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


_TfrapCfgFrPerfDlciNamesCirType_Type.__name__ = "Integer32"
_TfrapCfgFrPerfDlciNamesCirType_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesCirType = _TfrapCfgFrPerfDlciNamesCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 4),
    _TfrapCfgFrPerfDlciNamesCirType_Type()
)
tfrapCfgFrPerfDlciNamesCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesCirType.setStatus("mandatory")


class _TfrapCfgFrPerfDlciNamesUtilThreshold_Type(Integer32):
    """Custom type tfrapCfgFrPerfDlciNamesUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TfrapCfgFrPerfDlciNamesUtilThreshold_Type.__name__ = "Integer32"
_TfrapCfgFrPerfDlciNamesUtilThreshold_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesUtilThreshold = _TfrapCfgFrPerfDlciNamesUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 5),
    _TfrapCfgFrPerfDlciNamesUtilThreshold_Type()
)
tfrapCfgFrPerfDlciNamesUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesUtilThreshold.setStatus("mandatory")
_TfrapCfgFrPerfDlciNamesEirValue_Type = Integer32
_TfrapCfgFrPerfDlciNamesEirValue_Object = MibTableColumn
tfrapCfgFrPerfDlciNamesEirValue = _TfrapCfgFrPerfDlciNamesEirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 1, 1, 6),
    _TfrapCfgFrPerfDlciNamesEirValue_Type()
)
tfrapCfgFrPerfDlciNamesEirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesEirValue.setStatus("mandatory")
_TfrapCfgFrPerfDlciNamesDelete_Type = Integer32
_TfrapCfgFrPerfDlciNamesDelete_Object = MibScalar
tfrapCfgFrPerfDlciNamesDelete = _TfrapCfgFrPerfDlciNamesDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 2),
    _TfrapCfgFrPerfDlciNamesDelete_Type()
)
tfrapCfgFrPerfDlciNamesDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesDelete.setStatus("mandatory")
_TfrapCfgFrPerfTimers_ObjectIdentity = ObjectIdentity
tfrapCfgFrPerfTimers = _TfrapCfgFrPerfTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 3)
)


class _TfrapCfgFrPerfTimersSTInterval_Type(Integer32):
    """Custom type tfrapCfgFrPerfTimersSTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_TfrapCfgFrPerfTimersSTInterval_Type.__name__ = "Integer32"
_TfrapCfgFrPerfTimersSTInterval_Object = MibScalar
tfrapCfgFrPerfTimersSTInterval = _TfrapCfgFrPerfTimersSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 3, 1),
    _TfrapCfgFrPerfTimersSTInterval_Type()
)
tfrapCfgFrPerfTimersSTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfTimersSTInterval.setStatus("mandatory")


class _TfrapCfgFrPerfTimersLTInterval_Type(Integer32):
    """Custom type tfrapCfgFrPerfTimersLTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_TfrapCfgFrPerfTimersLTInterval_Type.__name__ = "Integer32"
_TfrapCfgFrPerfTimersLTInterval_Object = MibScalar
tfrapCfgFrPerfTimersLTInterval = _TfrapCfgFrPerfTimersLTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 3, 2),
    _TfrapCfgFrPerfTimersLTInterval_Type()
)
tfrapCfgFrPerfTimersLTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfTimersLTInterval.setStatus("mandatory")
_TfrapCfgFrPerfUserProtocolsTable_Object = MibTable
tfrapCfgFrPerfUserProtocolsTable = _TfrapCfgFrPerfUserProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 4)
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUserProtocolsTable.setStatus("mandatory")
_TfrapCfgFrPerfUserProtocolsEntry_Object = MibTableRow
tfrapCfgFrPerfUserProtocolsEntry = _TfrapCfgFrPerfUserProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 4, 1)
)
tfrapCfgFrPerfUserProtocolsEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgFrPerfUserProtocolsIndex"),
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUserProtocolsEntry.setStatus("mandatory")
_TfrapCfgFrPerfUserProtocolsIndex_Type = Integer32
_TfrapCfgFrPerfUserProtocolsIndex_Object = MibTableColumn
tfrapCfgFrPerfUserProtocolsIndex = _TfrapCfgFrPerfUserProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 4, 1, 1),
    _TfrapCfgFrPerfUserProtocolsIndex_Type()
)
tfrapCfgFrPerfUserProtocolsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUserProtocolsIndex.setStatus("mandatory")
_TfrapCfgFrPerfUserProtocolsPortNum_Type = Integer32
_TfrapCfgFrPerfUserProtocolsPortNum_Object = MibTableColumn
tfrapCfgFrPerfUserProtocolsPortNum = _TfrapCfgFrPerfUserProtocolsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 4, 1, 2),
    _TfrapCfgFrPerfUserProtocolsPortNum_Type()
)
tfrapCfgFrPerfUserProtocolsPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUserProtocolsPortNum.setStatus("mandatory")
_TfrapCfgFrPerfLTDlciFilterTable_Object = MibTable
tfrapCfgFrPerfLTDlciFilterTable = _TfrapCfgFrPerfLTDlciFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 5)
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTDlciFilterTable.setStatus("mandatory")
_TfrapCfgFrPerfLTDlciFilterEntry_Object = MibTableRow
tfrapCfgFrPerfLTDlciFilterEntry = _TfrapCfgFrPerfLTDlciFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 5, 1)
)
tfrapCfgFrPerfLTDlciFilterEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgFrPerfLTDlciFilterIndex"),
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTDlciFilterEntry.setStatus("mandatory")
_TfrapCfgFrPerfLTDlciFilterIndex_Type = Integer32
_TfrapCfgFrPerfLTDlciFilterIndex_Object = MibTableColumn
tfrapCfgFrPerfLTDlciFilterIndex = _TfrapCfgFrPerfLTDlciFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 5, 1, 1),
    _TfrapCfgFrPerfLTDlciFilterIndex_Type()
)
tfrapCfgFrPerfLTDlciFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTDlciFilterIndex.setStatus("mandatory")
_TfrapCfgFrPerfLTDlciFilterDlciNum_Type = Integer32
_TfrapCfgFrPerfLTDlciFilterDlciNum_Object = MibTableColumn
tfrapCfgFrPerfLTDlciFilterDlciNum = _TfrapCfgFrPerfLTDlciFilterDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 5, 1, 2),
    _TfrapCfgFrPerfLTDlciFilterDlciNum_Type()
)
tfrapCfgFrPerfLTDlciFilterDlciNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTDlciFilterDlciNum.setStatus("mandatory")
_TfrapCfgFrPerfLTProtocolFilterTable_Object = MibTable
tfrapCfgFrPerfLTProtocolFilterTable = _TfrapCfgFrPerfLTProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 6)
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTProtocolFilterTable.setStatus("mandatory")
_TfrapCfgFrPerfLTProtocolFilterEntry_Object = MibTableRow
tfrapCfgFrPerfLTProtocolFilterEntry = _TfrapCfgFrPerfLTProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 6, 1)
)
tfrapCfgFrPerfLTProtocolFilterEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapCfgFrPerfLTProtocolFilterIndex"),
)
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTProtocolFilterEntry.setStatus("mandatory")
_TfrapCfgFrPerfLTProtocolFilterIndex_Type = Integer32
_TfrapCfgFrPerfLTProtocolFilterIndex_Object = MibTableColumn
tfrapCfgFrPerfLTProtocolFilterIndex = _TfrapCfgFrPerfLTProtocolFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 6, 1, 1),
    _TfrapCfgFrPerfLTProtocolFilterIndex_Type()
)
tfrapCfgFrPerfLTProtocolFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTProtocolFilterIndex.setStatus("mandatory")


class _TfrapCfgFrPerfLTProtocolFilterProtocol_Type(Integer32):
    """Custom type tfrapCfgFrPerfLTProtocolFilterProtocol based on Integer32"""
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
          ("thru-becn-rx-bc", 134),
          ("thru-becn-tx-bc", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-bc", 136),
          ("thru-de-tx-bc", 135),
          ("thru-fecn-rx-bc", 132),
          ("thru-fecn-tx-bc", 131),
          ("thru-frame-rx-bc", 130),
          ("thru-frame-tx-bc", 129),
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


_TfrapCfgFrPerfLTProtocolFilterProtocol_Type.__name__ = "Integer32"
_TfrapCfgFrPerfLTProtocolFilterProtocol_Object = MibTableColumn
tfrapCfgFrPerfLTProtocolFilterProtocol = _TfrapCfgFrPerfLTProtocolFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 6, 1, 2),
    _TfrapCfgFrPerfLTProtocolFilterProtocol_Type()
)
tfrapCfgFrPerfLTProtocolFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTProtocolFilterProtocol.setStatus("mandatory")


class _TfrapCfgFrPerfDlciDefaultUtilThreshold_Type(Integer32):
    """Custom type tfrapCfgFrPerfDlciDefaultUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TfrapCfgFrPerfDlciDefaultUtilThreshold_Type.__name__ = "Integer32"
_TfrapCfgFrPerfDlciDefaultUtilThreshold_Object = MibScalar
tfrapCfgFrPerfDlciDefaultUtilThreshold = _TfrapCfgFrPerfDlciDefaultUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 7),
    _TfrapCfgFrPerfDlciDefaultUtilThreshold_Type()
)
tfrapCfgFrPerfDlciDefaultUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciDefaultUtilThreshold.setStatus("mandatory")


class _TfrapCfgFrPerfDlciUtilDuration_Type(Integer32):
    """Custom type tfrapCfgFrPerfDlciUtilDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TfrapCfgFrPerfDlciUtilDuration_Type.__name__ = "Integer32"
_TfrapCfgFrPerfDlciUtilDuration_Object = MibScalar
tfrapCfgFrPerfDlciUtilDuration = _TfrapCfgFrPerfDlciUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 8),
    _TfrapCfgFrPerfDlciUtilDuration_Type()
)
tfrapCfgFrPerfDlciUtilDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciUtilDuration.setStatus("mandatory")


class _TfrapCfgFrPerfDlciNamesTableClear_Type(Integer32):
    """Custom type tfrapCfgFrPerfDlciNamesTableClear based on Integer32"""
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


_TfrapCfgFrPerfDlciNamesTableClear_Type.__name__ = "Integer32"
_TfrapCfgFrPerfDlciNamesTableClear_Object = MibScalar
tfrapCfgFrPerfDlciNamesTableClear = _TfrapCfgFrPerfDlciNamesTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 9),
    _TfrapCfgFrPerfDlciNamesTableClear_Type()
)
tfrapCfgFrPerfDlciNamesTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfDlciNamesTableClear.setStatus("mandatory")


class _TfrapCfgFrPerfUserProtocolsTableClear_Type(Integer32):
    """Custom type tfrapCfgFrPerfUserProtocolsTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_TfrapCfgFrPerfUserProtocolsTableClear_Type.__name__ = "Integer32"
_TfrapCfgFrPerfUserProtocolsTableClear_Object = MibScalar
tfrapCfgFrPerfUserProtocolsTableClear = _TfrapCfgFrPerfUserProtocolsTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 10),
    _TfrapCfgFrPerfUserProtocolsTableClear_Type()
)
tfrapCfgFrPerfUserProtocolsTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUserProtocolsTableClear.setStatus("mandatory")


class _TfrapCfgFrPerfLTDlciFilterTableClear_Type(Integer32):
    """Custom type tfrapCfgFrPerfLTDlciFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_TfrapCfgFrPerfLTDlciFilterTableClear_Type.__name__ = "Integer32"
_TfrapCfgFrPerfLTDlciFilterTableClear_Object = MibScalar
tfrapCfgFrPerfLTDlciFilterTableClear = _TfrapCfgFrPerfLTDlciFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 11),
    _TfrapCfgFrPerfLTDlciFilterTableClear_Type()
)
tfrapCfgFrPerfLTDlciFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTDlciFilterTableClear.setStatus("mandatory")


class _TfrapCfgFrPerfLTProtocolFilterTableClear_Type(Integer32):
    """Custom type tfrapCfgFrPerfLTProtocolFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_TfrapCfgFrPerfLTProtocolFilterTableClear_Type.__name__ = "Integer32"
_TfrapCfgFrPerfLTProtocolFilterTableClear_Object = MibScalar
tfrapCfgFrPerfLTProtocolFilterTableClear = _TfrapCfgFrPerfLTProtocolFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 12),
    _TfrapCfgFrPerfLTProtocolFilterTableClear_Type()
)
tfrapCfgFrPerfLTProtocolFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfLTProtocolFilterTableClear.setStatus("mandatory")


class _TfrapCfgFrPerfUnprovDlcisDelete_Type(Integer32):
    """Custom type tfrapCfgFrPerfUnprovDlcisDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete-unprov", 1)
    )


_TfrapCfgFrPerfUnprovDlcisDelete_Type.__name__ = "Integer32"
_TfrapCfgFrPerfUnprovDlcisDelete_Object = MibScalar
tfrapCfgFrPerfUnprovDlcisDelete = _TfrapCfgFrPerfUnprovDlcisDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 7, 13),
    _TfrapCfgFrPerfUnprovDlcisDelete_Type()
)
tfrapCfgFrPerfUnprovDlcisDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgFrPerfUnprovDlcisDelete.setStatus("mandatory")
_TfrapCfgSecurityTable_ObjectIdentity = ObjectIdentity
tfrapCfgSecurityTable = _TfrapCfgSecurityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8)
)


class _TfrapCfgTelnetCliLcdPassword_Type(DisplayString):
    """Custom type tfrapCfgTelnetCliLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgTelnetCliLcdPassword_Type.__name__ = "DisplayString"
_TfrapCfgTelnetCliLcdPassword_Object = MibScalar
tfrapCfgTelnetCliLcdPassword = _TfrapCfgTelnetCliLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 1),
    _TfrapCfgTelnetCliLcdPassword_Type()
)
tfrapCfgTelnetCliLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTelnetCliLcdPassword.setStatus("mandatory")


class _TfrapCfgTftpPassword_Type(DisplayString):
    """Custom type tfrapCfgTftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgTftpPassword_Type.__name__ = "DisplayString"
_TfrapCfgTftpPassword_Object = MibScalar
tfrapCfgTftpPassword = _TfrapCfgTftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 2),
    _TfrapCfgTftpPassword_Type()
)
tfrapCfgTftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgTftpPassword.setStatus("mandatory")


class _TfrapCfgCliPassword_Type(DisplayString):
    """Custom type tfrapCfgCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgCliPassword_Type.__name__ = "DisplayString"
_TfrapCfgCliPassword_Object = MibScalar
tfrapCfgCliPassword = _TfrapCfgCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 3),
    _TfrapCfgCliPassword_Type()
)
tfrapCfgCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgCliPassword.setStatus("mandatory")


class _TfrapCfgLcdPassword_Type(DisplayString):
    """Custom type tfrapCfgLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgLcdPassword_Type.__name__ = "DisplayString"
_TfrapCfgLcdPassword_Object = MibScalar
tfrapCfgLcdPassword = _TfrapCfgLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 4),
    _TfrapCfgLcdPassword_Type()
)
tfrapCfgLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgLcdPassword.setStatus("mandatory")


class _TfrapCfgGetCommunityString_Type(DisplayString):
    """Custom type tfrapCfgGetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TfrapCfgGetCommunityString_Type.__name__ = "DisplayString"
_TfrapCfgGetCommunityString_Object = MibScalar
tfrapCfgGetCommunityString = _TfrapCfgGetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 5),
    _TfrapCfgGetCommunityString_Type()
)
tfrapCfgGetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgGetCommunityString.setStatus("mandatory")


class _TfrapCfgSetCommunityString_Type(DisplayString):
    """Custom type tfrapCfgSetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TfrapCfgSetCommunityString_Type.__name__ = "DisplayString"
_TfrapCfgSetCommunityString_Object = MibScalar
tfrapCfgSetCommunityString = _TfrapCfgSetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 6),
    _TfrapCfgSetCommunityString_Type()
)
tfrapCfgSetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgSetCommunityString.setStatus("mandatory")


class _TfrapCfgLcdPswdEnable_Type(Integer32):
    """Custom type tfrapCfgLcdPswdEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-lcd-pswd", 2),
          ("enable-lcd-pswd", 1))
    )


_TfrapCfgLcdPswdEnable_Type.__name__ = "Integer32"
_TfrapCfgLcdPswdEnable_Object = MibScalar
tfrapCfgLcdPswdEnable = _TfrapCfgLcdPswdEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 7),
    _TfrapCfgLcdPswdEnable_Type()
)
tfrapCfgLcdPswdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgLcdPswdEnable.setStatus("mandatory")
_TfrapCfgLcdPswdTimeout_Type = Integer32
_TfrapCfgLcdPswdTimeout_Object = MibScalar
tfrapCfgLcdPswdTimeout = _TfrapCfgLcdPswdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 8, 8),
    _TfrapCfgLcdPswdTimeout_Type()
)
tfrapCfgLcdPswdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgLcdPswdTimeout.setStatus("mandatory")


class _TfrapCfgLock_Type(Integer32):
    """Custom type tfrapCfgLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TfrapCfgLock_Type.__name__ = "Integer32"
_TfrapCfgLock_Object = MibScalar
tfrapCfgLock = _TfrapCfgLock_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 12),
    _TfrapCfgLock_Type()
)
tfrapCfgLock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgLock.setStatus("mandatory")
_TfrapCfgLockID_Type = IpAddress
_TfrapCfgLockID_Object = MibScalar
tfrapCfgLockID = _TfrapCfgLockID_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 13),
    _TfrapCfgLockID_Type()
)
tfrapCfgLockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgLockID.setStatus("mandatory")


class _TfrapCfgID_Type(DisplayString):
    """Custom type tfrapCfgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TfrapCfgID_Type.__name__ = "DisplayString"
_TfrapCfgID_Object = MibScalar
tfrapCfgID = _TfrapCfgID_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 14),
    _TfrapCfgID_Type()
)
tfrapCfgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapCfgID.setStatus("mandatory")


class _TfrapCfgStatus_Type(Integer32):
    """Custom type tfrapCfgStatus based on Integer32"""
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


_TfrapCfgStatus_Type.__name__ = "Integer32"
_TfrapCfgStatus_Object = MibScalar
tfrapCfgStatus = _TfrapCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 15),
    _TfrapCfgStatus_Type()
)
tfrapCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgStatus.setStatus("mandatory")


class _TfrapCfgUnlock_Type(Integer32):
    """Custom type tfrapCfgUnlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("un-lock", 1)
    )


_TfrapCfgUnlock_Type.__name__ = "Integer32"
_TfrapCfgUnlock_Object = MibScalar
tfrapCfgUnlock = _TfrapCfgUnlock_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 16),
    _TfrapCfgUnlock_Type()
)
tfrapCfgUnlock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgUnlock.setStatus("mandatory")


class _TfrapCfgUpdate_Type(Integer32):
    """Custom type tfrapCfgUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_TfrapCfgUpdate_Type.__name__ = "Integer32"
_TfrapCfgUpdate_Object = MibScalar
tfrapCfgUpdate = _TfrapCfgUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 2, 17),
    _TfrapCfgUpdate_Type()
)
tfrapCfgUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapCfgUpdate.setStatus("mandatory")
_TfrapDiagnostics_ObjectIdentity = ObjectIdentity
tfrapDiagnostics = _TfrapDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 3)
)
_TfrapDiagUnitTable_ObjectIdentity = ObjectIdentity
tfrapDiagUnitTable = _TfrapDiagUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 1)
)


class _TfrapDiagUnitLocLoop_Type(Integer32):
    """Custom type tfrapDiagUnitLocLoop based on Integer32"""
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


_TfrapDiagUnitLocLoop_Type.__name__ = "Integer32"
_TfrapDiagUnitLocLoop_Object = MibScalar
tfrapDiagUnitLocLoop = _TfrapDiagUnitLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 1, 1),
    _TfrapDiagUnitLocLoop_Type()
)
tfrapDiagUnitLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagUnitLocLoop.setStatus("mandatory")


class _TfrapDiagUnitReset_Type(Integer32):
    """Custom type tfrapDiagUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-unit", 1)
    )


_TfrapDiagUnitReset_Type.__name__ = "Integer32"
_TfrapDiagUnitReset_Object = MibScalar
tfrapDiagUnitReset = _TfrapDiagUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 1, 2),
    _TfrapDiagUnitReset_Type()
)
tfrapDiagUnitReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagUnitReset.setStatus("mandatory")
_TfrapDiagUnitTimeRemaining_Type = TimeTicks
_TfrapDiagUnitTimeRemaining_Object = MibScalar
tfrapDiagUnitTimeRemaining = _TfrapDiagUnitTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 1, 3),
    _TfrapDiagUnitTimeRemaining_Type()
)
tfrapDiagUnitTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagUnitTimeRemaining.setStatus("mandatory")
_TfrapDiagT1Table_ObjectIdentity = ObjectIdentity
tfrapDiagT1Table = _TfrapDiagT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2)
)


class _TfrapDiagT1LocLineLpbk_Type(Integer32):
    """Custom type tfrapDiagT1LocLineLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line-lpbk-disable", 1),
          ("line-lpbk-enable", 2))
    )


_TfrapDiagT1LocLineLpbk_Type.__name__ = "Integer32"
_TfrapDiagT1LocLineLpbk_Object = MibScalar
tfrapDiagT1LocLineLpbk = _TfrapDiagT1LocLineLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 1),
    _TfrapDiagT1LocLineLpbk_Type()
)
tfrapDiagT1LocLineLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagT1LocLineLpbk.setStatus("mandatory")


class _TfrapDiagT1LocPylLpbk_Type(Integer32):
    """Custom type tfrapDiagT1LocPylLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pyl-lpbk-disable", 1),
          ("pyl-lpbk-enable", 2))
    )


_TfrapDiagT1LocPylLpbk_Type.__name__ = "Integer32"
_TfrapDiagT1LocPylLpbk_Object = MibScalar
tfrapDiagT1LocPylLpbk = _TfrapDiagT1LocPylLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 2),
    _TfrapDiagT1LocPylLpbk_Type()
)
tfrapDiagT1LocPylLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagT1LocPylLpbk.setStatus("mandatory")


class _TfrapDiagT1LocAggrLpbk_Type(Integer32):
    """Custom type tfrapDiagT1LocAggrLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggr-lpbk-disable", 1),
          ("aggr-lpbk-enable", 2))
    )


_TfrapDiagT1LocAggrLpbk_Type.__name__ = "Integer32"
_TfrapDiagT1LocAggrLpbk_Object = MibScalar
tfrapDiagT1LocAggrLpbk = _TfrapDiagT1LocAggrLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 3),
    _TfrapDiagT1LocAggrLpbk_Type()
)
tfrapDiagT1LocAggrLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagT1LocAggrLpbk.setStatus("mandatory")


class _TfrapDiagT1RmtLpbkStatus_Type(Integer32):
    """Custom type tfrapDiagT1RmtLpbkStatus based on Integer32"""
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
        *(("csu-lpbk-from-remote", 2),
          ("csu-lpbk-sent-to-remote", 5),
          ("dsu-lpbk-from-remote", 3),
          ("dsu-lpbk-sent-to-remote", 6),
          ("no-remote-lpbks", 1),
          ("pyl-lpbk-from-remote", 4))
    )


_TfrapDiagT1RmtLpbkStatus_Type.__name__ = "Integer32"
_TfrapDiagT1RmtLpbkStatus_Object = MibScalar
tfrapDiagT1RmtLpbkStatus = _TfrapDiagT1RmtLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 4),
    _TfrapDiagT1RmtLpbkStatus_Type()
)
tfrapDiagT1RmtLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagT1RmtLpbkStatus.setStatus("mandatory")


class _TfrapDiagT1RmtLpbkCmd_Type(Integer32):
    """Custom type tfrapDiagT1RmtLpbkCmd based on Integer32"""
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
        *(("rmt-csu-lpbk-loopdown", 2),
          ("rmt-csu-lpbk-loopup", 1),
          ("rmt-dsu-lpbk-loopdown", 4),
          ("rmt-dsu-lpbk-loopup", 3))
    )


_TfrapDiagT1RmtLpbkCmd_Type.__name__ = "Integer32"
_TfrapDiagT1RmtLpbkCmd_Object = MibScalar
tfrapDiagT1RmtLpbkCmd = _TfrapDiagT1RmtLpbkCmd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 5),
    _TfrapDiagT1RmtLpbkCmd_Type()
)
tfrapDiagT1RmtLpbkCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagT1RmtLpbkCmd.setStatus("mandatory")
_TfrapDiagT1TimeRemaining_Type = TimeTicks
_TfrapDiagT1TimeRemaining_Object = MibScalar
tfrapDiagT1TimeRemaining = _TfrapDiagT1TimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 2, 6),
    _TfrapDiagT1TimeRemaining_Type()
)
tfrapDiagT1TimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagT1TimeRemaining.setStatus("mandatory")
_TfrapDiagDteTable_ObjectIdentity = ObjectIdentity
tfrapDiagDteTable = _TfrapDiagDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3)
)


class _TfrapDiagDteSigRTS_Type(Integer32):
    """Custom type tfrapDiagDteSigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rts-signal-off", 2),
          ("rts-signal-on", 1))
    )


_TfrapDiagDteSigRTS_Type.__name__ = "Integer32"
_TfrapDiagDteSigRTS_Object = MibScalar
tfrapDiagDteSigRTS = _TfrapDiagDteSigRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 1),
    _TfrapDiagDteSigRTS_Type()
)
tfrapDiagDteSigRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteSigRTS.setStatus("mandatory")


class _TfrapDiagDteSigDTR_Type(Integer32):
    """Custom type tfrapDiagDteSigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr-signal-off", 2),
          ("dtr-signal-on", 1))
    )


_TfrapDiagDteSigDTR_Type.__name__ = "Integer32"
_TfrapDiagDteSigDTR_Object = MibScalar
tfrapDiagDteSigDTR = _TfrapDiagDteSigDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 2),
    _TfrapDiagDteSigDTR_Type()
)
tfrapDiagDteSigDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteSigDTR.setStatus("mandatory")


class _TfrapDiagDteLclLpbk_Type(Integer32):
    """Custom type tfrapDiagDteLclLpbk based on Integer32"""
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


_TfrapDiagDteLclLpbk_Type.__name__ = "Integer32"
_TfrapDiagDteLclLpbk_Object = MibScalar
tfrapDiagDteLclLpbk = _TfrapDiagDteLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 3),
    _TfrapDiagDteLclLpbk_Type()
)
tfrapDiagDteLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagDteLclLpbk.setStatus("mandatory")


class _TfrapDiagDteV54Lpbk_Type(Integer32):
    """Custom type tfrapDiagDteV54Lpbk based on Integer32"""
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


_TfrapDiagDteV54Lpbk_Type.__name__ = "Integer32"
_TfrapDiagDteV54Lpbk_Object = MibScalar
tfrapDiagDteV54Lpbk = _TfrapDiagDteV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 4),
    _TfrapDiagDteV54Lpbk_Type()
)
tfrapDiagDteV54Lpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteV54Lpbk.setStatus("mandatory")


class _TfrapDiagDteRmtV54Lpbk_Type(Integer32):
    """Custom type tfrapDiagDteRmtV54Lpbk based on Integer32"""
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


_TfrapDiagDteRmtV54Lpbk_Type.__name__ = "Integer32"
_TfrapDiagDteRmtV54Lpbk_Object = MibScalar
tfrapDiagDteRmtV54Lpbk = _TfrapDiagDteRmtV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 5),
    _TfrapDiagDteRmtV54Lpbk_Type()
)
tfrapDiagDteRmtV54Lpbk.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagDteRmtV54Lpbk.setStatus("mandatory")


class _TfrapDiagDteBerState_Type(Integer32):
    """Custom type tfrapDiagDteBerState based on Integer32"""
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
        *(("clear-error-bert-test", 5),
          ("inject-error-bert-test", 4),
          ("start-bert-test-dte", 2),
          ("start-bert-test-t1", 1),
          ("stop-bert-test", 3))
    )


_TfrapDiagDteBerState_Type.__name__ = "Integer32"
_TfrapDiagDteBerState_Object = MibScalar
tfrapDiagDteBerState = _TfrapDiagDteBerState_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 6),
    _TfrapDiagDteBerState_Type()
)
tfrapDiagDteBerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerState.setStatus("mandatory")


class _TfrapDiagDteBerStatus_Type(Integer32):
    """Custom type tfrapDiagDteBerStatus based on Integer32"""
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


_TfrapDiagDteBerStatus_Type.__name__ = "Integer32"
_TfrapDiagDteBerStatus_Object = MibScalar
tfrapDiagDteBerStatus = _TfrapDiagDteBerStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 7),
    _TfrapDiagDteBerStatus_Type()
)
tfrapDiagDteBerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerStatus.setStatus("mandatory")
_TfrapDiagDteBerErrors_Type = Counter32
_TfrapDiagDteBerErrors_Object = MibScalar
tfrapDiagDteBerErrors = _TfrapDiagDteBerErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 8),
    _TfrapDiagDteBerErrors_Type()
)
tfrapDiagDteBerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerErrors.setStatus("mandatory")
_TfrapDiagDteBerErrSec_Type = Counter32
_TfrapDiagDteBerErrSec_Object = MibScalar
tfrapDiagDteBerErrSec = _TfrapDiagDteBerErrSec_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 9),
    _TfrapDiagDteBerErrSec_Type()
)
tfrapDiagDteBerErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerErrSec.setStatus("mandatory")
_TfrapDiagDteBerTimeElaps_Type = TimeTicks
_TfrapDiagDteBerTimeElaps_Object = MibScalar
tfrapDiagDteBerTimeElaps = _TfrapDiagDteBerTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 10),
    _TfrapDiagDteBerTimeElaps_Type()
)
tfrapDiagDteBerTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerTimeElaps.setStatus("mandatory")
_TfrapDiagDteBerResyncs_Type = Counter32
_TfrapDiagDteBerResyncs_Object = MibScalar
tfrapDiagDteBerResyncs = _TfrapDiagDteBerResyncs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 11),
    _TfrapDiagDteBerResyncs_Type()
)
tfrapDiagDteBerResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteBerResyncs.setStatus("mandatory")


class _TfrapDiagDteBerPattern_Type(Integer32):
    """Custom type tfrapDiagDteBerPattern based on Integer32"""
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


_TfrapDiagDteBerPattern_Type.__name__ = "Integer32"
_TfrapDiagDteBerPattern_Object = MibScalar
tfrapDiagDteBerPattern = _TfrapDiagDteBerPattern_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 12),
    _TfrapDiagDteBerPattern_Type()
)
tfrapDiagDteBerPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagDteBerPattern.setStatus("mandatory")
_TfrapDiagDteTimeRemaining_Type = TimeTicks
_TfrapDiagDteTimeRemaining_Object = MibScalar
tfrapDiagDteTimeRemaining = _TfrapDiagDteTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 3, 13),
    _TfrapDiagDteTimeRemaining_Type()
)
tfrapDiagDteTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagDteTimeRemaining.setStatus("mandatory")
_TfrapDiagVnipTable_Object = MibTable
tfrapDiagVnipTable = _TfrapDiagVnipTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6)
)
if mibBuilder.loadTexts:
    tfrapDiagVnipTable.setStatus("mandatory")
_TfrapDiagVnipEntry_Object = MibTableRow
tfrapDiagVnipEntry = _TfrapDiagVnipEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1)
)
tfrapDiagVnipEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapDiagVnipInterface"),
    (0, "TFRAP-MIB", "tfrapDiagVnipIndex"),
)
if mibBuilder.loadTexts:
    tfrapDiagVnipEntry.setStatus("mandatory")


class _TfrapDiagVnipInterface_Type(Integer32):
    """Custom type tfrapDiagVnipInterface based on Integer32"""
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


_TfrapDiagVnipInterface_Type.__name__ = "Integer32"
_TfrapDiagVnipInterface_Object = MibTableColumn
tfrapDiagVnipInterface = _TfrapDiagVnipInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 1),
    _TfrapDiagVnipInterface_Type()
)
tfrapDiagVnipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVnipInterface.setStatus("mandatory")
_TfrapDiagVnipIndex_Type = Integer32
_TfrapDiagVnipIndex_Object = MibTableColumn
tfrapDiagVnipIndex = _TfrapDiagVnipIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 2),
    _TfrapDiagVnipIndex_Type()
)
tfrapDiagVnipIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVnipIndex.setStatus("mandatory")
_TfrapDiagVnipDlci_Type = Integer32
_TfrapDiagVnipDlci_Object = MibTableColumn
tfrapDiagVnipDlci = _TfrapDiagVnipDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 3),
    _TfrapDiagVnipDlci_Type()
)
tfrapDiagVnipDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagVnipDlci.setStatus("mandatory")
_TfrapDiagVnipIpAddr_Type = IpAddress
_TfrapDiagVnipIpAddr_Object = MibTableColumn
tfrapDiagVnipIpAddr = _TfrapDiagVnipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 4),
    _TfrapDiagVnipIpAddr_Type()
)
tfrapDiagVnipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDiagVnipIpAddr.setStatus("mandatory")


class _TfrapDiagVLOOP_Type(Integer32):
    """Custom type tfrapDiagVLOOP based on Integer32"""
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


_TfrapDiagVLOOP_Type.__name__ = "Integer32"
_TfrapDiagVLOOP_Object = MibTableColumn
tfrapDiagVLOOP = _TfrapDiagVLOOP_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 5),
    _TfrapDiagVLOOP_Type()
)
tfrapDiagVLOOP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagVLOOP.setStatus("mandatory")


class _TfrapDiagVBERT_Type(Integer32):
    """Custom type tfrapDiagVBERT based on Integer32"""
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


_TfrapDiagVBERT_Type.__name__ = "Integer32"
_TfrapDiagVBERT_Object = MibTableColumn
tfrapDiagVBERT = _TfrapDiagVBERT_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 6),
    _TfrapDiagVBERT_Type()
)
tfrapDiagVBERT.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapDiagVBERT.setStatus("mandatory")


class _TfrapDiagVBERTRate_Type(Integer32):
    """Custom type tfrapDiagVBERTRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2048000),
    )


_TfrapDiagVBERTRate_Type.__name__ = "Integer32"
_TfrapDiagVBERTRate_Object = MibTableColumn
tfrapDiagVBERTRate = _TfrapDiagVBERTRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 7),
    _TfrapDiagVBERTRate_Type()
)
tfrapDiagVBERTRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVBERTRate.setStatus("mandatory")


class _TfrapDiagVBERTSize_Type(Integer32):
    """Custom type tfrapDiagVBERTSize based on Integer32"""
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


_TfrapDiagVBERTSize_Type.__name__ = "Integer32"
_TfrapDiagVBERTSize_Object = MibTableColumn
tfrapDiagVBERTSize = _TfrapDiagVBERTSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 8),
    _TfrapDiagVBERTSize_Type()
)
tfrapDiagVBERTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVBERTSize.setStatus("mandatory")


class _TfrapDiagVBERTPktPercent_Type(Integer32):
    """Custom type tfrapDiagVBERTPktPercent based on Integer32"""
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


_TfrapDiagVBERTPktPercent_Type.__name__ = "Integer32"
_TfrapDiagVBERTPktPercent_Object = MibTableColumn
tfrapDiagVBERTPktPercent = _TfrapDiagVBERTPktPercent_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 9),
    _TfrapDiagVBERTPktPercent_Type()
)
tfrapDiagVBERTPktPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVBERTPktPercent.setStatus("mandatory")


class _TfrapDiagVBERTTestPeriod_Type(Integer32):
    """Custom type tfrapDiagVBERTTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_TfrapDiagVBERTTestPeriod_Type.__name__ = "Integer32"
_TfrapDiagVBERTTestPeriod_Object = MibTableColumn
tfrapDiagVBERTTestPeriod = _TfrapDiagVBERTTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 3, 6, 1, 10),
    _TfrapDiagVBERTTestPeriod_Type()
)
tfrapDiagVBERTTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapDiagVBERTTestPeriod.setStatus("mandatory")
_TfrapStatus_ObjectIdentity = ObjectIdentity
tfrapStatus = _TfrapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 4)
)
_TfrapStatusIntfTable_ObjectIdentity = ObjectIdentity
tfrapStatusIntfTable = _TfrapStatusIntfTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1)
)


class _TfrapIntfDteMode_Type(Integer32):
    """Custom type tfrapIntfDteMode based on Integer32"""
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


_TfrapIntfDteMode_Type.__name__ = "Integer32"
_TfrapIntfDteMode_Object = MibScalar
tfrapIntfDteMode = _TfrapIntfDteMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 1),
    _TfrapIntfDteMode_Type()
)
tfrapIntfDteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteMode.setStatus("mandatory")


class _TfrapIntfDteRts_Type(Integer32):
    """Custom type tfrapIntfDteRts based on Integer32"""
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


_TfrapIntfDteRts_Type.__name__ = "Integer32"
_TfrapIntfDteRts_Object = MibScalar
tfrapIntfDteRts = _TfrapIntfDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 2),
    _TfrapIntfDteRts_Type()
)
tfrapIntfDteRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteRts.setStatus("mandatory")


class _TfrapIntfDteDtr_Type(Integer32):
    """Custom type tfrapIntfDteDtr based on Integer32"""
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


_TfrapIntfDteDtr_Type.__name__ = "Integer32"
_TfrapIntfDteDtr_Object = MibScalar
tfrapIntfDteDtr = _TfrapIntfDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 3),
    _TfrapIntfDteDtr_Type()
)
tfrapIntfDteDtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteDtr.setStatus("mandatory")


class _TfrapIntfT1Mode_Type(Integer32):
    """Custom type tfrapIntfT1Mode based on Integer32"""
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


_TfrapIntfT1Mode_Type.__name__ = "Integer32"
_TfrapIntfT1Mode_Object = MibScalar
tfrapIntfT1Mode = _TfrapIntfT1Mode_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 4),
    _TfrapIntfT1Mode_Type()
)
tfrapIntfT1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfT1Mode.setStatus("mandatory")


class _TfrapIntfT1Status_Type(Integer32):
    """Custom type tfrapIntfT1Status based on Integer32"""
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
        *(("not-applicable", 5),
          ("signal-not-present", 4),
          ("signal-present-without-frame-sync", 3),
          ("t1-frame-sync-okay", 1),
          ("t1-frame-sync-with-errors", 2))
    )


_TfrapIntfT1Status_Type.__name__ = "Integer32"
_TfrapIntfT1Status_Object = MibScalar
tfrapIntfT1Status = _TfrapIntfT1Status_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 5),
    _TfrapIntfT1Status_Type()
)
tfrapIntfT1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfT1Status.setStatus("mandatory")


class _TfrapIntfT1Alarms_Type(Integer32):
    """Custom type tfrapIntfT1Alarms based on Integer32"""
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
        *(("no-alarms", 1),
          ("red-alarm-declared", 2),
          ("unframed-all-ones-detected", 4),
          ("yellow-alarm-detected", 3))
    )


_TfrapIntfT1Alarms_Type.__name__ = "Integer32"
_TfrapIntfT1Alarms_Object = MibScalar
tfrapIntfT1Alarms = _TfrapIntfT1Alarms_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 6),
    _TfrapIntfT1Alarms_Type()
)
tfrapIntfT1Alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfT1Alarms.setStatus("mandatory")


class _TfrapIntfDteDcd_Type(Integer32):
    """Custom type tfrapIntfDteDcd based on Integer32"""
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


_TfrapIntfDteDcd_Type.__name__ = "Integer32"
_TfrapIntfDteDcd_Object = MibScalar
tfrapIntfDteDcd = _TfrapIntfDteDcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 7),
    _TfrapIntfDteDcd_Type()
)
tfrapIntfDteDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteDcd.setStatus("mandatory")


class _TfrapIntfDteDsr_Type(Integer32):
    """Custom type tfrapIntfDteDsr based on Integer32"""
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


_TfrapIntfDteDsr_Type.__name__ = "Integer32"
_TfrapIntfDteDsr_Object = MibScalar
tfrapIntfDteDsr = _TfrapIntfDteDsr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 8),
    _TfrapIntfDteDsr_Type()
)
tfrapIntfDteDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteDsr.setStatus("mandatory")


class _TfrapIntfDteCts_Type(Integer32):
    """Custom type tfrapIntfDteCts based on Integer32"""
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


_TfrapIntfDteCts_Type.__name__ = "Integer32"
_TfrapIntfDteCts_Object = MibScalar
tfrapIntfDteCts = _TfrapIntfDteCts_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 1, 9),
    _TfrapIntfDteCts_Type()
)
tfrapIntfDteCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIntfDteCts.setStatus("mandatory")
_TfrapVnipTopologyTable_Object = MibTable
tfrapVnipTopologyTable = _TfrapVnipTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2)
)
if mibBuilder.loadTexts:
    tfrapVnipTopologyTable.setStatus("mandatory")
_TfrapVnipTopologyEntry_Object = MibTableRow
tfrapVnipTopologyEntry = _TfrapVnipTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1)
)
tfrapVnipTopologyEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapVnipTopologyInterface"),
    (0, "TFRAP-MIB", "tfrapVnipTopologyIndex"),
)
if mibBuilder.loadTexts:
    tfrapVnipTopologyEntry.setStatus("mandatory")


class _TfrapVnipTopologyInterface_Type(Integer32):
    """Custom type tfrapVnipTopologyInterface based on Integer32"""
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


_TfrapVnipTopologyInterface_Type.__name__ = "Integer32"
_TfrapVnipTopologyInterface_Object = MibTableColumn
tfrapVnipTopologyInterface = _TfrapVnipTopologyInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 1),
    _TfrapVnipTopologyInterface_Type()
)
tfrapVnipTopologyInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyInterface.setStatus("mandatory")
_TfrapVnipTopologyIndex_Type = Integer32
_TfrapVnipTopologyIndex_Object = MibTableColumn
tfrapVnipTopologyIndex = _TfrapVnipTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 2),
    _TfrapVnipTopologyIndex_Type()
)
tfrapVnipTopologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyIndex.setStatus("mandatory")
_TfrapVnipTopologyDlci_Type = Integer32
_TfrapVnipTopologyDlci_Object = MibTableColumn
tfrapVnipTopologyDlci = _TfrapVnipTopologyDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 3),
    _TfrapVnipTopologyDlci_Type()
)
tfrapVnipTopologyDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyDlci.setStatus("mandatory")
_TfrapVnipTopologyIpAddr_Type = IpAddress
_TfrapVnipTopologyIpAddr_Object = MibTableColumn
tfrapVnipTopologyIpAddr = _TfrapVnipTopologyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 4),
    _TfrapVnipTopologyIpAddr_Type()
)
tfrapVnipTopologyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyIpAddr.setStatus("mandatory")
_TfrapVnipTopologyNumHops_Type = Integer32
_TfrapVnipTopologyNumHops_Object = MibTableColumn
tfrapVnipTopologyNumHops = _TfrapVnipTopologyNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 5),
    _TfrapVnipTopologyNumHops_Type()
)
tfrapVnipTopologyNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyNumHops.setStatus("mandatory")
_TfrapVnipTopologyLocalDlci_Type = Integer32
_TfrapVnipTopologyLocalDlci_Object = MibTableColumn
tfrapVnipTopologyLocalDlci = _TfrapVnipTopologyLocalDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 6),
    _TfrapVnipTopologyLocalDlci_Type()
)
tfrapVnipTopologyLocalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopologyLocalDlci.setStatus("mandatory")
_TfrapVnipTopoTDNumSamples_Type = Counter32
_TfrapVnipTopoTDNumSamples_Object = MibTableColumn
tfrapVnipTopoTDNumSamples = _TfrapVnipTopoTDNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 10),
    _TfrapVnipTopoTDNumSamples_Type()
)
tfrapVnipTopoTDNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoTDNumSamples.setStatus("mandatory")
_TfrapVnipTopoTDAvgDelay_Type = Counter32
_TfrapVnipTopoTDAvgDelay_Object = MibTableColumn
tfrapVnipTopoTDAvgDelay = _TfrapVnipTopoTDAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 11),
    _TfrapVnipTopoTDAvgDelay_Type()
)
tfrapVnipTopoTDAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoTDAvgDelay.setStatus("mandatory")
_TfrapVnipTopoTDMaxDelay_Type = Counter32
_TfrapVnipTopoTDMaxDelay_Object = MibTableColumn
tfrapVnipTopoTDMaxDelay = _TfrapVnipTopoTDMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 12),
    _TfrapVnipTopoTDMaxDelay_Type()
)
tfrapVnipTopoTDMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoTDMaxDelay.setStatus("mandatory")
_TfrapVnipTopoTDMinDelay_Type = Counter32
_TfrapVnipTopoTDMinDelay_Object = MibTableColumn
tfrapVnipTopoTDMinDelay = _TfrapVnipTopoTDMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 13),
    _TfrapVnipTopoTDMinDelay_Type()
)
tfrapVnipTopoTDMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoTDMinDelay.setStatus("mandatory")
_TfrapVnipTopoTDLastDelay_Type = Counter32
_TfrapVnipTopoTDLastDelay_Object = MibTableColumn
tfrapVnipTopoTDLastDelay = _TfrapVnipTopoTDLastDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 14),
    _TfrapVnipTopoTDLastDelay_Type()
)
tfrapVnipTopoTDLastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoTDLastDelay.setStatus("mandatory")


class _TfrapVnipTopoVLOOPStatus_Type(Integer32):
    """Custom type tfrapVnipTopoVLOOPStatus based on Integer32"""
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


_TfrapVnipTopoVLOOPStatus_Type.__name__ = "Integer32"
_TfrapVnipTopoVLOOPStatus_Object = MibTableColumn
tfrapVnipTopoVLOOPStatus = _TfrapVnipTopoVLOOPStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 15),
    _TfrapVnipTopoVLOOPStatus_Type()
)
tfrapVnipTopoVLOOPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVLOOPStatus.setStatus("mandatory")


class _TfrapVnipTopoVBERTStatus_Type(Integer32):
    """Custom type tfrapVnipTopoVBERTStatus based on Integer32"""
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


_TfrapVnipTopoVBERTStatus_Type.__name__ = "Integer32"
_TfrapVnipTopoVBERTStatus_Object = MibTableColumn
tfrapVnipTopoVBERTStatus = _TfrapVnipTopoVBERTStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 16),
    _TfrapVnipTopoVBERTStatus_Type()
)
tfrapVnipTopoVBERTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBERTStatus.setStatus("mandatory")
_TfrapVnipTopoVBertTxDESetFrames_Type = Counter32
_TfrapVnipTopoVBertTxDESetFrames_Object = MibTableColumn
tfrapVnipTopoVBertTxDESetFrames = _TfrapVnipTopoVBertTxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 17),
    _TfrapVnipTopoVBertTxDESetFrames_Type()
)
tfrapVnipTopoVBertTxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertTxDESetFrames.setStatus("mandatory")
_TfrapVnipTopoVBertRxDESetFrames_Type = Counter32
_TfrapVnipTopoVBertRxDESetFrames_Object = MibTableColumn
tfrapVnipTopoVBertRxDESetFrames = _TfrapVnipTopoVBertRxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 18),
    _TfrapVnipTopoVBertRxDESetFrames_Type()
)
tfrapVnipTopoVBertRxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertRxDESetFrames.setStatus("mandatory")
_TfrapVnipTopoVBertTxDEClrFrames_Type = Counter32
_TfrapVnipTopoVBertTxDEClrFrames_Object = MibTableColumn
tfrapVnipTopoVBertTxDEClrFrames = _TfrapVnipTopoVBertTxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 19),
    _TfrapVnipTopoVBertTxDEClrFrames_Type()
)
tfrapVnipTopoVBertTxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertTxDEClrFrames.setStatus("mandatory")
_TfrapVnipTopoVBertRxDEClrFrames_Type = Counter32
_TfrapVnipTopoVBertRxDEClrFrames_Object = MibTableColumn
tfrapVnipTopoVBertRxDEClrFrames = _TfrapVnipTopoVBertRxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 20),
    _TfrapVnipTopoVBertRxDEClrFrames_Type()
)
tfrapVnipTopoVBertRxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertRxDEClrFrames.setStatus("mandatory")
_TfrapVnipTopoVBertTransitDelayMax_Type = Counter32
_TfrapVnipTopoVBertTransitDelayMax_Object = MibTableColumn
tfrapVnipTopoVBertTransitDelayMax = _TfrapVnipTopoVBertTransitDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 21),
    _TfrapVnipTopoVBertTransitDelayMax_Type()
)
tfrapVnipTopoVBertTransitDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertTransitDelayMax.setStatus("mandatory")
_TfrapVnipTopoVBertTransitDelayAvg_Type = Counter32
_TfrapVnipTopoVBertTransitDelayAvg_Object = MibTableColumn
tfrapVnipTopoVBertTransitDelayAvg = _TfrapVnipTopoVBertTransitDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 22),
    _TfrapVnipTopoVBertTransitDelayAvg_Type()
)
tfrapVnipTopoVBertTransitDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertTransitDelayAvg.setStatus("mandatory")
_TfrapVnipTopoVBertTimeElapse_Type = TimeTicks
_TfrapVnipTopoVBertTimeElapse_Object = MibTableColumn
tfrapVnipTopoVBertTimeElapse = _TfrapVnipTopoVBertTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 23),
    _TfrapVnipTopoVBertTimeElapse_Type()
)
tfrapVnipTopoVBertTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertTimeElapse.setStatus("mandatory")
_TfrapVnipTopoVBertPerUtilCIR_Type = Integer32
_TfrapVnipTopoVBertPerUtilCIR_Object = MibTableColumn
tfrapVnipTopoVBertPerUtilCIR = _TfrapVnipTopoVBertPerUtilCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 24),
    _TfrapVnipTopoVBertPerUtilCIR_Type()
)
tfrapVnipTopoVBertPerUtilCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertPerUtilCIR.setStatus("mandatory")
_TfrapVnipTopoVBertPerUtilEIR_Type = Integer32
_TfrapVnipTopoVBertPerUtilEIR_Object = MibTableColumn
tfrapVnipTopoVBertPerUtilEIR = _TfrapVnipTopoVBertPerUtilEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 2, 1, 25),
    _TfrapVnipTopoVBertPerUtilEIR_Type()
)
tfrapVnipTopoVBertPerUtilEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapVnipTopoVBertPerUtilEIR.setStatus("mandatory")
_TfrapStatusMgmtTable_ObjectIdentity = ObjectIdentity
tfrapStatusMgmtTable = _TfrapStatusMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3)
)


class _TfrapStatusMgmtChannel_Type(Integer32):
    """Custom type tfrapStatusMgmtChannel based on Integer32"""
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


_TfrapStatusMgmtChannel_Type.__name__ = "Integer32"
_TfrapStatusMgmtChannel_Object = MibScalar
tfrapStatusMgmtChannel = _TfrapStatusMgmtChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3, 1),
    _TfrapStatusMgmtChannel_Type()
)
tfrapStatusMgmtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusMgmtChannel.setStatus("mandatory")


class _TfrapStatusMgmtInterface_Type(Integer32):
    """Custom type tfrapStatusMgmtInterface based on Integer32"""
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
          ("dte", 2),
          ("dte-and-t1", 4),
          ("t1", 3))
    )


_TfrapStatusMgmtInterface_Type.__name__ = "Integer32"
_TfrapStatusMgmtInterface_Object = MibScalar
tfrapStatusMgmtInterface = _TfrapStatusMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3, 2),
    _TfrapStatusMgmtInterface_Type()
)
tfrapStatusMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusMgmtInterface.setStatus("mandatory")


class _TfrapStatusMgmtInterfaceStatus_Type(Integer32):
    """Custom type tfrapStatusMgmtInterfaceStatus based on Integer32"""
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


_TfrapStatusMgmtInterfaceStatus_Type.__name__ = "Integer32"
_TfrapStatusMgmtInterfaceStatus_Object = MibScalar
tfrapStatusMgmtInterfaceStatus = _TfrapStatusMgmtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3, 3),
    _TfrapStatusMgmtInterfaceStatus_Type()
)
tfrapStatusMgmtInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusMgmtInterfaceStatus.setStatus("mandatory")
_TfrapStatusMgmtDefaultDLCINo_Type = Integer32
_TfrapStatusMgmtDefaultDLCINo_Object = MibScalar
tfrapStatusMgmtDefaultDLCINo = _TfrapStatusMgmtDefaultDLCINo_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3, 4),
    _TfrapStatusMgmtDefaultDLCINo_Type()
)
tfrapStatusMgmtDefaultDLCINo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusMgmtDefaultDLCINo.setStatus("mandatory")


class _TfrapStatusMgmtDefaultDLCIStatus_Type(Integer32):
    """Custom type tfrapStatusMgmtDefaultDLCIStatus based on Integer32"""
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


_TfrapStatusMgmtDefaultDLCIStatus_Type.__name__ = "Integer32"
_TfrapStatusMgmtDefaultDLCIStatus_Object = MibScalar
tfrapStatusMgmtDefaultDLCIStatus = _TfrapStatusMgmtDefaultDLCIStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 3, 5),
    _TfrapStatusMgmtDefaultDLCIStatus_Type()
)
tfrapStatusMgmtDefaultDLCIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusMgmtDefaultDLCIStatus.setStatus("mandatory")
_TfrapStatusLedTable_ObjectIdentity = ObjectIdentity
tfrapStatusLedTable = _TfrapStatusLedTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4)
)


class _TfrapStatusDteModeLED_Type(Integer32):
    """Custom type tfrapStatusDteModeLED based on Integer32"""
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
        *(("greenLED-normal", 2),
          ("offLED-DTE-inactive", 1),
          ("redLED-no-active-WAN-connection", 4),
          ("yellowLED-test-mode", 3))
    )


_TfrapStatusDteModeLED_Type.__name__ = "Integer32"
_TfrapStatusDteModeLED_Object = MibScalar
tfrapStatusDteModeLED = _TfrapStatusDteModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 1),
    _TfrapStatusDteModeLED_Type()
)
tfrapStatusDteModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusDteModeLED.setStatus("mandatory")


class _TfrapStatusDteStatusLED_Type(Integer32):
    """Custom type tfrapStatusDteStatusLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-active", 2),
          ("offLED-inactive", 1))
    )


_TfrapStatusDteStatusLED_Type.__name__ = "Integer32"
_TfrapStatusDteStatusLED_Object = MibScalar
tfrapStatusDteStatusLED = _TfrapStatusDteStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 2),
    _TfrapStatusDteStatusLED_Type()
)
tfrapStatusDteStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusDteStatusLED.setStatus("mandatory")


class _TfrapStatusDteTxLED_Type(Integer32):
    """Custom type tfrapStatusDteTxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-tx-data-transmitting", 2),
          ("offLED-inactive", 1),
          ("yellowLED-disabled", 3))
    )


_TfrapStatusDteTxLED_Type.__name__ = "Integer32"
_TfrapStatusDteTxLED_Object = MibScalar
tfrapStatusDteTxLED = _TfrapStatusDteTxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 3),
    _TfrapStatusDteTxLED_Type()
)
tfrapStatusDteTxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusDteTxLED.setStatus("mandatory")


class _TfrapStatusDteRxLED_Type(Integer32):
    """Custom type tfrapStatusDteRxLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenLED-rx-data-receiving", 2),
          ("offLED-inactive", 1),
          ("yellowLED-disabled", 3))
    )


_TfrapStatusDteRxLED_Type.__name__ = "Integer32"
_TfrapStatusDteRxLED_Object = MibScalar
tfrapStatusDteRxLED = _TfrapStatusDteRxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 4),
    _TfrapStatusDteRxLED_Type()
)
tfrapStatusDteRxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusDteRxLED.setStatus("mandatory")


class _TfrapStatusT1ModeLED_Type(Integer32):
    """Custom type tfrapStatusT1ModeLED based on Integer32"""
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


_TfrapStatusT1ModeLED_Type.__name__ = "Integer32"
_TfrapStatusT1ModeLED_Object = MibScalar
tfrapStatusT1ModeLED = _TfrapStatusT1ModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 5),
    _TfrapStatusT1ModeLED_Type()
)
tfrapStatusT1ModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusT1ModeLED.setStatus("mandatory")


class _TfrapStatusT1StatusLED_Type(Integer32):
    """Custom type tfrapStatusT1StatusLED based on Integer32"""
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
        *(("blinking-red-greenLED-transient-error", 6),
          ("blinking-red-yellowLED-AIS", 7),
          ("blinking-redLED-no-carrier-red-alarm", 5),
          ("greenLED-normal", 2),
          ("offLED-T1-no-signal", 1),
          ("redLED-red-alarm", 4),
          ("yellowLED-remote-alarm", 3))
    )


_TfrapStatusT1StatusLED_Type.__name__ = "Integer32"
_TfrapStatusT1StatusLED_Object = MibScalar
tfrapStatusT1StatusLED = _TfrapStatusT1StatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 6),
    _TfrapStatusT1StatusLED_Type()
)
tfrapStatusT1StatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusT1StatusLED.setStatus("mandatory")


class _TfrapStatusAllLEDs_Type(DisplayString):
    """Custom type tfrapStatusAllLEDs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TfrapStatusAllLEDs_Type.__name__ = "DisplayString"
_TfrapStatusAllLEDs_Object = MibScalar
tfrapStatusAllLEDs = _TfrapStatusAllLEDs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 4, 7),
    _TfrapStatusAllLEDs_Type()
)
tfrapStatusAllLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusAllLEDs.setStatus("mandatory")


class _TfrapVnipTransitDelayClear_Type(Integer32):
    """Custom type tfrapVnipTransitDelayClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-transit-delay", 1)
    )


_TfrapVnipTransitDelayClear_Type.__name__ = "Integer32"
_TfrapVnipTransitDelayClear_Object = MibScalar
tfrapVnipTransitDelayClear = _TfrapVnipTransitDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 5),
    _TfrapVnipTransitDelayClear_Type()
)
tfrapVnipTransitDelayClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapVnipTransitDelayClear.setStatus("mandatory")


class _TfrapLmiSourcing_Type(Integer32):
    """Custom type tfrapLmiSourcing based on Integer32"""
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
          ("network-dte", 5),
          ("network-t1", 6),
          ("passthrough", 2),
          ("user-dte", 3),
          ("user-t1", 4))
    )


_TfrapLmiSourcing_Type.__name__ = "Integer32"
_TfrapLmiSourcing_Object = MibScalar
tfrapLmiSourcing = _TfrapLmiSourcing_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 6),
    _TfrapLmiSourcing_Type()
)
tfrapLmiSourcing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapLmiSourcing.setStatus("mandatory")


class _TfrapVBertClear_Type(Integer32):
    """Custom type tfrapVBertClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-vbert", 1)
    )


_TfrapVBertClear_Type.__name__ = "Integer32"
_TfrapVBertClear_Object = MibScalar
tfrapVBertClear = _TfrapVBertClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 11),
    _TfrapVBertClear_Type()
)
tfrapVBertClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapVBertClear.setStatus("mandatory")


class _TfrapStatusLmiAutosense_Type(Integer32):
    """Custom type tfrapStatusLmiAutosense based on Integer32"""
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


_TfrapStatusLmiAutosense_Type.__name__ = "Integer32"
_TfrapStatusLmiAutosense_Object = MibScalar
tfrapStatusLmiAutosense = _TfrapStatusLmiAutosense_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 4, 12),
    _TfrapStatusLmiAutosense_Type()
)
tfrapStatusLmiAutosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapStatusLmiAutosense.setStatus("mandatory")
_TfrapPerformance_ObjectIdentity = ObjectIdentity
tfrapPerformance = _TfrapPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5)
)
_TfrapPerfPhysicalIntf_ObjectIdentity = ObjectIdentity
tfrapPerfPhysicalIntf = _TfrapPerfPhysicalIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1)
)
_TfrapPerfT1CurrentTable_Object = MibTable
tfrapPerfT1CurrentTable = _TfrapPerfT1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tfrapPerfT1CurrentTable.setStatus("mandatory")
_TfrapT1CurrentEntry_Object = MibTableRow
tfrapT1CurrentEntry = _TfrapT1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1)
)
tfrapT1CurrentEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapT1CurrentIndex"),
)
if mibBuilder.loadTexts:
    tfrapT1CurrentEntry.setStatus("mandatory")


class _TfrapT1CurrentIndex_Type(Integer32):
    """Custom type tfrapT1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TfrapT1CurrentIndex_Type.__name__ = "Integer32"
_TfrapT1CurrentIndex_Object = MibTableColumn
tfrapT1CurrentIndex = _TfrapT1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 1),
    _TfrapT1CurrentIndex_Type()
)
tfrapT1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentIndex.setStatus("mandatory")
_TfrapT1CurrentCrc6Events_Type = Gauge32
_TfrapT1CurrentCrc6Events_Object = MibTableColumn
tfrapT1CurrentCrc6Events = _TfrapT1CurrentCrc6Events_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 2),
    _TfrapT1CurrentCrc6Events_Type()
)
tfrapT1CurrentCrc6Events.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentCrc6Events.setStatus("mandatory")
_TfrapT1CurrentOofEvents_Type = Gauge32
_TfrapT1CurrentOofEvents_Object = MibTableColumn
tfrapT1CurrentOofEvents = _TfrapT1CurrentOofEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 3),
    _TfrapT1CurrentOofEvents_Type()
)
tfrapT1CurrentOofEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentOofEvents.setStatus("mandatory")
_TfrapT1CurrentESs_Type = Gauge32
_TfrapT1CurrentESs_Object = MibTableColumn
tfrapT1CurrentESs = _TfrapT1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 4),
    _TfrapT1CurrentESs_Type()
)
tfrapT1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentESs.setStatus("mandatory")
_TfrapT1CurrentSESs_Type = Gauge32
_TfrapT1CurrentSESs_Object = MibTableColumn
tfrapT1CurrentSESs = _TfrapT1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 5),
    _TfrapT1CurrentSESs_Type()
)
tfrapT1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentSESs.setStatus("mandatory")
_TfrapT1CurrentSEFSs_Type = Gauge32
_TfrapT1CurrentSEFSs_Object = MibTableColumn
tfrapT1CurrentSEFSs = _TfrapT1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 6),
    _TfrapT1CurrentSEFSs_Type()
)
tfrapT1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentSEFSs.setStatus("mandatory")
_TfrapT1CurrentUASs_Type = Gauge32
_TfrapT1CurrentUASs_Object = MibTableColumn
tfrapT1CurrentUASs = _TfrapT1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 7),
    _TfrapT1CurrentUASs_Type()
)
tfrapT1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentUASs.setStatus("mandatory")
_TfrapT1CurrentCSSs_Type = Gauge32
_TfrapT1CurrentCSSs_Object = MibTableColumn
tfrapT1CurrentCSSs = _TfrapT1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 8),
    _TfrapT1CurrentCSSs_Type()
)
tfrapT1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentCSSs.setStatus("mandatory")
_TfrapT1CurrentBESs_Type = Gauge32
_TfrapT1CurrentBESs_Object = MibTableColumn
tfrapT1CurrentBESs = _TfrapT1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 9),
    _TfrapT1CurrentBESs_Type()
)
tfrapT1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentBESs.setStatus("mandatory")
_TfrapT1CurrentLCVs_Type = Gauge32
_TfrapT1CurrentLCVs_Object = MibTableColumn
tfrapT1CurrentLCVs = _TfrapT1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 1, 1, 10),
    _TfrapT1CurrentLCVs_Type()
)
tfrapT1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1CurrentLCVs.setStatus("mandatory")
_TfrapPerfT1IntervalTable_Object = MibTable
tfrapPerfT1IntervalTable = _TfrapPerfT1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    tfrapPerfT1IntervalTable.setStatus("mandatory")
_TfrapT1IntervalEntry_Object = MibTableRow
tfrapT1IntervalEntry = _TfrapT1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1)
)
tfrapT1IntervalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapT1IntervalIndex"),
    (0, "TFRAP-MIB", "tfrapT1IntervalNumber"),
)
if mibBuilder.loadTexts:
    tfrapT1IntervalEntry.setStatus("mandatory")


class _TfrapT1IntervalIndex_Type(Integer32):
    """Custom type tfrapT1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TfrapT1IntervalIndex_Type.__name__ = "Integer32"
_TfrapT1IntervalIndex_Object = MibTableColumn
tfrapT1IntervalIndex = _TfrapT1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 1),
    _TfrapT1IntervalIndex_Type()
)
tfrapT1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalIndex.setStatus("mandatory")


class _TfrapT1IntervalNumber_Type(Integer32):
    """Custom type tfrapT1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TfrapT1IntervalNumber_Type.__name__ = "Integer32"
_TfrapT1IntervalNumber_Object = MibTableColumn
tfrapT1IntervalNumber = _TfrapT1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 2),
    _TfrapT1IntervalNumber_Type()
)
tfrapT1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalNumber.setStatus("mandatory")
_TfrapT1IntervalESs_Type = Gauge32
_TfrapT1IntervalESs_Object = MibTableColumn
tfrapT1IntervalESs = _TfrapT1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 3),
    _TfrapT1IntervalESs_Type()
)
tfrapT1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalESs.setStatus("mandatory")
_TfrapT1IntervalSESs_Type = Gauge32
_TfrapT1IntervalSESs_Object = MibTableColumn
tfrapT1IntervalSESs = _TfrapT1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 4),
    _TfrapT1IntervalSESs_Type()
)
tfrapT1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalSESs.setStatus("mandatory")
_TfrapT1IntervalSEFSs_Type = Gauge32
_TfrapT1IntervalSEFSs_Object = MibTableColumn
tfrapT1IntervalSEFSs = _TfrapT1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 5),
    _TfrapT1IntervalSEFSs_Type()
)
tfrapT1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalSEFSs.setStatus("mandatory")
_TfrapT1IntervalUASs_Type = Gauge32
_TfrapT1IntervalUASs_Object = MibTableColumn
tfrapT1IntervalUASs = _TfrapT1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 6),
    _TfrapT1IntervalUASs_Type()
)
tfrapT1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalUASs.setStatus("mandatory")
_TfrapT1IntervalCSSs_Type = Gauge32
_TfrapT1IntervalCSSs_Object = MibTableColumn
tfrapT1IntervalCSSs = _TfrapT1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 7),
    _TfrapT1IntervalCSSs_Type()
)
tfrapT1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalCSSs.setStatus("mandatory")
_TfrapT1IntervalBESs_Type = Gauge32
_TfrapT1IntervalBESs_Object = MibTableColumn
tfrapT1IntervalBESs = _TfrapT1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 8),
    _TfrapT1IntervalBESs_Type()
)
tfrapT1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalBESs.setStatus("mandatory")
_TfrapT1IntervalLCVs_Type = Gauge32
_TfrapT1IntervalLCVs_Object = MibTableColumn
tfrapT1IntervalLCVs = _TfrapT1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 2, 1, 9),
    _TfrapT1IntervalLCVs_Type()
)
tfrapT1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1IntervalLCVs.setStatus("mandatory")
_TfrapPerfT1TotalTable_Object = MibTable
tfrapPerfT1TotalTable = _TfrapPerfT1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tfrapPerfT1TotalTable.setStatus("mandatory")
_TfrapT1TotalEntry_Object = MibTableRow
tfrapT1TotalEntry = _TfrapT1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1)
)
tfrapT1TotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapT1TotalIndex"),
)
if mibBuilder.loadTexts:
    tfrapT1TotalEntry.setStatus("mandatory")


class _TfrapT1TotalIndex_Type(Integer32):
    """Custom type tfrapT1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TfrapT1TotalIndex_Type.__name__ = "Integer32"
_TfrapT1TotalIndex_Object = MibTableColumn
tfrapT1TotalIndex = _TfrapT1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 1),
    _TfrapT1TotalIndex_Type()
)
tfrapT1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalIndex.setStatus("mandatory")
_TfrapT1TotalESs_Type = Gauge32
_TfrapT1TotalESs_Object = MibTableColumn
tfrapT1TotalESs = _TfrapT1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 2),
    _TfrapT1TotalESs_Type()
)
tfrapT1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalESs.setStatus("mandatory")
_TfrapT1TotalSESs_Type = Gauge32
_TfrapT1TotalSESs_Object = MibTableColumn
tfrapT1TotalSESs = _TfrapT1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 3),
    _TfrapT1TotalSESs_Type()
)
tfrapT1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalSESs.setStatus("mandatory")
_TfrapT1TotalSEFSs_Type = Gauge32
_TfrapT1TotalSEFSs_Object = MibTableColumn
tfrapT1TotalSEFSs = _TfrapT1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 4),
    _TfrapT1TotalSEFSs_Type()
)
tfrapT1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalSEFSs.setStatus("mandatory")
_TfrapT1TotalUASs_Type = Gauge32
_TfrapT1TotalUASs_Object = MibTableColumn
tfrapT1TotalUASs = _TfrapT1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 5),
    _TfrapT1TotalUASs_Type()
)
tfrapT1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalUASs.setStatus("mandatory")
_TfrapT1TotalCSSs_Type = Gauge32
_TfrapT1TotalCSSs_Object = MibTableColumn
tfrapT1TotalCSSs = _TfrapT1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 6),
    _TfrapT1TotalCSSs_Type()
)
tfrapT1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalCSSs.setStatus("mandatory")
_TfrapT1TotalBESs_Type = Gauge32
_TfrapT1TotalBESs_Object = MibTableColumn
tfrapT1TotalBESs = _TfrapT1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 7),
    _TfrapT1TotalBESs_Type()
)
tfrapT1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalBESs.setStatus("mandatory")
_TfrapT1TotalLCVs_Type = Gauge32
_TfrapT1TotalLCVs_Object = MibTableColumn
tfrapT1TotalLCVs = _TfrapT1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 3, 1, 8),
    _TfrapT1TotalLCVs_Type()
)
tfrapT1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapT1TotalLCVs.setStatus("mandatory")
_TfrapT1PerfCmdTypeTable_ObjectIdentity = ObjectIdentity
tfrapT1PerfCmdTypeTable = _TfrapT1PerfCmdTypeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 4)
)


class _TfrapT1PerfFreezeState_Type(Integer32):
    """Custom type tfrapT1PerfFreezeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freeze-reg", 1),
          ("unfreeze-reg", 2))
    )


_TfrapT1PerfFreezeState_Type.__name__ = "Integer32"
_TfrapT1PerfFreezeState_Object = MibScalar
tfrapT1PerfFreezeState = _TfrapT1PerfFreezeState_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 4, 1),
    _TfrapT1PerfFreezeState_Type()
)
tfrapT1PerfFreezeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfrapT1PerfFreezeState.setStatus("mandatory")


class _TfrapT1PerfClearEvents_Type(Integer32):
    """Custom type tfrapT1PerfClearEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-events", 1)
    )


_TfrapT1PerfClearEvents_Type.__name__ = "Integer32"
_TfrapT1PerfClearEvents_Object = MibScalar
tfrapT1PerfClearEvents = _TfrapT1PerfClearEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 4, 2),
    _TfrapT1PerfClearEvents_Type()
)
tfrapT1PerfClearEvents.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapT1PerfClearEvents.setStatus("mandatory")


class _TfrapT1PerfClearAll_Type(Integer32):
    """Custom type tfrapT1PerfClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-all", 1)
    )


_TfrapT1PerfClearAll_Type.__name__ = "Integer32"
_TfrapT1PerfClearAll_Object = MibScalar
tfrapT1PerfClearAll = _TfrapT1PerfClearAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 1, 4, 3),
    _TfrapT1PerfClearAll_Type()
)
tfrapT1PerfClearAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapT1PerfClearAll.setStatus("mandatory")
_TfrapPerfMgmtIp_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIp = _TfrapPerfMgmtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2)
)
_TfrapPerfMgmtIpIFStatsTable_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIpIFStatsTable = _TfrapPerfMgmtIpIFStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 1)
)
_TfrapPerfMgmtIpIFInOctets_Type = Counter32
_TfrapPerfMgmtIpIFInOctets_Object = MibScalar
tfrapPerfMgmtIpIFInOctets = _TfrapPerfMgmtIpIFInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 1, 1),
    _TfrapPerfMgmtIpIFInOctets_Type()
)
tfrapPerfMgmtIpIFInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIFInOctets.setStatus("mandatory")
_TfrapPerfMgmtIpIFInErrors_Type = Counter32
_TfrapPerfMgmtIpIFInErrors_Object = MibScalar
tfrapPerfMgmtIpIFInErrors = _TfrapPerfMgmtIpIFInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 1, 2),
    _TfrapPerfMgmtIpIFInErrors_Type()
)
tfrapPerfMgmtIpIFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIFInErrors.setStatus("mandatory")
_TfrapPerfMgmtIpIFOutOctets_Type = Counter32
_TfrapPerfMgmtIpIFOutOctets_Object = MibScalar
tfrapPerfMgmtIpIFOutOctets = _TfrapPerfMgmtIpIFOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 1, 3),
    _TfrapPerfMgmtIpIFOutOctets_Type()
)
tfrapPerfMgmtIpIFOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIFOutOctets.setStatus("mandatory")


class _TfrapPerfMgmtIpIFOperStatus_Type(Integer32):
    """Custom type tfrapPerfMgmtIpIFOperStatus based on Integer32"""
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


_TfrapPerfMgmtIpIFOperStatus_Type.__name__ = "Integer32"
_TfrapPerfMgmtIpIFOperStatus_Object = MibScalar
tfrapPerfMgmtIpIFOperStatus = _TfrapPerfMgmtIpIFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 1, 4),
    _TfrapPerfMgmtIpIFOperStatus_Type()
)
tfrapPerfMgmtIpIFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIFOperStatus.setStatus("mandatory")
_TfrapPerfMgmtIpIPStatsTable_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIpIPStatsTable = _TfrapPerfMgmtIpIPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2)
)
_TfrapPerfMgmtIpIPInRcv_Type = Counter32
_TfrapPerfMgmtIpIPInRcv_Object = MibScalar
tfrapPerfMgmtIpIPInRcv = _TfrapPerfMgmtIpIPInRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 1),
    _TfrapPerfMgmtIpIPInRcv_Type()
)
tfrapPerfMgmtIpIPInRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInRcv.setStatus("mandatory")
_TfrapPerfMgmtIpIPInHdrErr_Type = Counter32
_TfrapPerfMgmtIpIPInHdrErr_Object = MibScalar
tfrapPerfMgmtIpIPInHdrErr = _TfrapPerfMgmtIpIPInHdrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 2),
    _TfrapPerfMgmtIpIPInHdrErr_Type()
)
tfrapPerfMgmtIpIPInHdrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInHdrErr.setStatus("mandatory")
_TfrapPerfMgmtIpIPInAddrErr_Type = Counter32
_TfrapPerfMgmtIpIPInAddrErr_Object = MibScalar
tfrapPerfMgmtIpIPInAddrErr = _TfrapPerfMgmtIpIPInAddrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 3),
    _TfrapPerfMgmtIpIPInAddrErr_Type()
)
tfrapPerfMgmtIpIPInAddrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInAddrErr.setStatus("mandatory")
_TfrapPerfMgmtIpIPInProtUnk_Type = Counter32
_TfrapPerfMgmtIpIPInProtUnk_Object = MibScalar
tfrapPerfMgmtIpIPInProtUnk = _TfrapPerfMgmtIpIPInProtUnk_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 4),
    _TfrapPerfMgmtIpIPInProtUnk_Type()
)
tfrapPerfMgmtIpIPInProtUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInProtUnk.setStatus("mandatory")
_TfrapPerfMgmtIpIPInDscrd_Type = Counter32
_TfrapPerfMgmtIpIPInDscrd_Object = MibScalar
tfrapPerfMgmtIpIPInDscrd = _TfrapPerfMgmtIpIPInDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 5),
    _TfrapPerfMgmtIpIPInDscrd_Type()
)
tfrapPerfMgmtIpIPInDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInDscrd.setStatus("mandatory")
_TfrapPerfMgmtIpIPInDlvrs_Type = Counter32
_TfrapPerfMgmtIpIPInDlvrs_Object = MibScalar
tfrapPerfMgmtIpIPInDlvrs = _TfrapPerfMgmtIpIPInDlvrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 6),
    _TfrapPerfMgmtIpIPInDlvrs_Type()
)
tfrapPerfMgmtIpIPInDlvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPInDlvrs.setStatus("mandatory")
_TfrapPerfMgmtIpIPOutRqst_Type = Counter32
_TfrapPerfMgmtIpIPOutRqst_Object = MibScalar
tfrapPerfMgmtIpIPOutRqst = _TfrapPerfMgmtIpIPOutRqst_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 7),
    _TfrapPerfMgmtIpIPOutRqst_Type()
)
tfrapPerfMgmtIpIPOutRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPOutRqst.setStatus("mandatory")
_TfrapPerfMgmtIpIPOutDscrd_Type = Counter32
_TfrapPerfMgmtIpIPOutDscrd_Object = MibScalar
tfrapPerfMgmtIpIPOutDscrd = _TfrapPerfMgmtIpIPOutDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 8),
    _TfrapPerfMgmtIpIPOutDscrd_Type()
)
tfrapPerfMgmtIpIPOutDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPOutDscrd.setStatus("mandatory")
_TfrapPerfMgmtIpIPOutNoRt_Type = Counter32
_TfrapPerfMgmtIpIPOutNoRt_Object = MibScalar
tfrapPerfMgmtIpIPOutNoRt = _TfrapPerfMgmtIpIPOutNoRt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 2, 9),
    _TfrapPerfMgmtIpIPOutNoRt_Type()
)
tfrapPerfMgmtIpIPOutNoRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpIPOutNoRt.setStatus("mandatory")
_TfrapPerfMgmtIpICMPStatsTable_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIpICMPStatsTable = _TfrapPerfMgmtIpICMPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3)
)
_TfrapPerfMgmtIpICMPInMsgs_Type = Counter32
_TfrapPerfMgmtIpICMPInMsgs_Object = MibScalar
tfrapPerfMgmtIpICMPInMsgs = _TfrapPerfMgmtIpICMPInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 1),
    _TfrapPerfMgmtIpICMPInMsgs_Type()
)
tfrapPerfMgmtIpICMPInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInMsgs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInErrors_Type = Counter32
_TfrapPerfMgmtIpICMPInErrors_Object = MibScalar
tfrapPerfMgmtIpICMPInErrors = _TfrapPerfMgmtIpICMPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 2),
    _TfrapPerfMgmtIpICMPInErrors_Type()
)
tfrapPerfMgmtIpICMPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInErrors.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInDestUnreachs_Type = Counter32
_TfrapPerfMgmtIpICMPInDestUnreachs_Object = MibScalar
tfrapPerfMgmtIpICMPInDestUnreachs = _TfrapPerfMgmtIpICMPInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 3),
    _TfrapPerfMgmtIpICMPInDestUnreachs_Type()
)
tfrapPerfMgmtIpICMPInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInDestUnreachs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInTimeExcds_Type = Counter32
_TfrapPerfMgmtIpICMPInTimeExcds_Object = MibScalar
tfrapPerfMgmtIpICMPInTimeExcds = _TfrapPerfMgmtIpICMPInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 4),
    _TfrapPerfMgmtIpICMPInTimeExcds_Type()
)
tfrapPerfMgmtIpICMPInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInTimeExcds.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInParmProbs_Type = Counter32
_TfrapPerfMgmtIpICMPInParmProbs_Object = MibScalar
tfrapPerfMgmtIpICMPInParmProbs = _TfrapPerfMgmtIpICMPInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 5),
    _TfrapPerfMgmtIpICMPInParmProbs_Type()
)
tfrapPerfMgmtIpICMPInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInParmProbs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInRedirects_Type = Counter32
_TfrapPerfMgmtIpICMPInRedirects_Object = MibScalar
tfrapPerfMgmtIpICMPInRedirects = _TfrapPerfMgmtIpICMPInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 6),
    _TfrapPerfMgmtIpICMPInRedirects_Type()
)
tfrapPerfMgmtIpICMPInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInRedirects.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInEchos_Type = Counter32
_TfrapPerfMgmtIpICMPInEchos_Object = MibScalar
tfrapPerfMgmtIpICMPInEchos = _TfrapPerfMgmtIpICMPInEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 7),
    _TfrapPerfMgmtIpICMPInEchos_Type()
)
tfrapPerfMgmtIpICMPInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInEchos.setStatus("mandatory")
_TfrapPerfMgmtIpICMPInEchoReps_Type = Counter32
_TfrapPerfMgmtIpICMPInEchoReps_Object = MibScalar
tfrapPerfMgmtIpICMPInEchoReps = _TfrapPerfMgmtIpICMPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 8),
    _TfrapPerfMgmtIpICMPInEchoReps_Type()
)
tfrapPerfMgmtIpICMPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPInEchoReps.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutMsgs_Type = Counter32
_TfrapPerfMgmtIpICMPOutMsgs_Object = MibScalar
tfrapPerfMgmtIpICMPOutMsgs = _TfrapPerfMgmtIpICMPOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 9),
    _TfrapPerfMgmtIpICMPOutMsgs_Type()
)
tfrapPerfMgmtIpICMPOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutMsgs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutErrors_Type = Counter32
_TfrapPerfMgmtIpICMPOutErrors_Object = MibScalar
tfrapPerfMgmtIpICMPOutErrors = _TfrapPerfMgmtIpICMPOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 10),
    _TfrapPerfMgmtIpICMPOutErrors_Type()
)
tfrapPerfMgmtIpICMPOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutErrors.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutDestUnreachs_Type = Counter32
_TfrapPerfMgmtIpICMPOutDestUnreachs_Object = MibScalar
tfrapPerfMgmtIpICMPOutDestUnreachs = _TfrapPerfMgmtIpICMPOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 11),
    _TfrapPerfMgmtIpICMPOutDestUnreachs_Type()
)
tfrapPerfMgmtIpICMPOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutDestUnreachs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutParmProbs_Type = Counter32
_TfrapPerfMgmtIpICMPOutParmProbs_Object = MibScalar
tfrapPerfMgmtIpICMPOutParmProbs = _TfrapPerfMgmtIpICMPOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 12),
    _TfrapPerfMgmtIpICMPOutParmProbs_Type()
)
tfrapPerfMgmtIpICMPOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutParmProbs.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutRedirects_Type = Counter32
_TfrapPerfMgmtIpICMPOutRedirects_Object = MibScalar
tfrapPerfMgmtIpICMPOutRedirects = _TfrapPerfMgmtIpICMPOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 13),
    _TfrapPerfMgmtIpICMPOutRedirects_Type()
)
tfrapPerfMgmtIpICMPOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutRedirects.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutEchos_Type = Counter32
_TfrapPerfMgmtIpICMPOutEchos_Object = MibScalar
tfrapPerfMgmtIpICMPOutEchos = _TfrapPerfMgmtIpICMPOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 14),
    _TfrapPerfMgmtIpICMPOutEchos_Type()
)
tfrapPerfMgmtIpICMPOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutEchos.setStatus("mandatory")
_TfrapPerfMgmtIpICMPOutEchoReps_Type = Counter32
_TfrapPerfMgmtIpICMPOutEchoReps_Object = MibScalar
tfrapPerfMgmtIpICMPOutEchoReps = _TfrapPerfMgmtIpICMPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 3, 15),
    _TfrapPerfMgmtIpICMPOutEchoReps_Type()
)
tfrapPerfMgmtIpICMPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpICMPOutEchoReps.setStatus("mandatory")
_TfrapPerfMgmtIpUDPStatsTable_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIpUDPStatsTable = _TfrapPerfMgmtIpUDPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 4)
)
_TfrapPerfMgmtIpUDPInDatagrams_Type = Counter32
_TfrapPerfMgmtIpUDPInDatagrams_Object = MibScalar
tfrapPerfMgmtIpUDPInDatagrams = _TfrapPerfMgmtIpUDPInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 4, 1),
    _TfrapPerfMgmtIpUDPInDatagrams_Type()
)
tfrapPerfMgmtIpUDPInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpUDPInDatagrams.setStatus("mandatory")
_TfrapPerfMgmtIpUDPOutDatagrams_Type = Counter32
_TfrapPerfMgmtIpUDPOutDatagrams_Object = MibScalar
tfrapPerfMgmtIpUDPOutDatagrams = _TfrapPerfMgmtIpUDPOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 4, 2),
    _TfrapPerfMgmtIpUDPOutDatagrams_Type()
)
tfrapPerfMgmtIpUDPOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpUDPOutDatagrams.setStatus("mandatory")
_TfrapPerfMgmtIpUDPNoPorts_Type = Counter32
_TfrapPerfMgmtIpUDPNoPorts_Object = MibScalar
tfrapPerfMgmtIpUDPNoPorts = _TfrapPerfMgmtIpUDPNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 4, 3),
    _TfrapPerfMgmtIpUDPNoPorts_Type()
)
tfrapPerfMgmtIpUDPNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpUDPNoPorts.setStatus("mandatory")
_TfrapPerfMgmtIpTCPStatsTable_ObjectIdentity = ObjectIdentity
tfrapPerfMgmtIpTCPStatsTable = _TfrapPerfMgmtIpTCPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5)
)
_TfrapPerfMgmtIpTCPActiveOpens_Type = Counter32
_TfrapPerfMgmtIpTCPActiveOpens_Object = MibScalar
tfrapPerfMgmtIpTCPActiveOpens = _TfrapPerfMgmtIpTCPActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 1),
    _TfrapPerfMgmtIpTCPActiveOpens_Type()
)
tfrapPerfMgmtIpTCPActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPActiveOpens.setStatus("mandatory")
_TfrapPerfMgmtIpTCPPassiveOpens_Type = Counter32
_TfrapPerfMgmtIpTCPPassiveOpens_Object = MibScalar
tfrapPerfMgmtIpTCPPassiveOpens = _TfrapPerfMgmtIpTCPPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 2),
    _TfrapPerfMgmtIpTCPPassiveOpens_Type()
)
tfrapPerfMgmtIpTCPPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPPassiveOpens.setStatus("mandatory")
_TfrapPerfMgmtIpTCPAttemptFails_Type = Counter32
_TfrapPerfMgmtIpTCPAttemptFails_Object = MibScalar
tfrapPerfMgmtIpTCPAttemptFails = _TfrapPerfMgmtIpTCPAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 3),
    _TfrapPerfMgmtIpTCPAttemptFails_Type()
)
tfrapPerfMgmtIpTCPAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPAttemptFails.setStatus("mandatory")
_TfrapPerfMgmtIpTCPCurrEstab_Type = Gauge32
_TfrapPerfMgmtIpTCPCurrEstab_Object = MibScalar
tfrapPerfMgmtIpTCPCurrEstab = _TfrapPerfMgmtIpTCPCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 4),
    _TfrapPerfMgmtIpTCPCurrEstab_Type()
)
tfrapPerfMgmtIpTCPCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPCurrEstab.setStatus("mandatory")
_TfrapPerfMgmtIpTCPInSegs_Type = Counter32
_TfrapPerfMgmtIpTCPInSegs_Object = MibScalar
tfrapPerfMgmtIpTCPInSegs = _TfrapPerfMgmtIpTCPInSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 5),
    _TfrapPerfMgmtIpTCPInSegs_Type()
)
tfrapPerfMgmtIpTCPInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPInSegs.setStatus("mandatory")
_TfrapPerfMgmtIpTCPOutSegs_Type = Counter32
_TfrapPerfMgmtIpTCPOutSegs_Object = MibScalar
tfrapPerfMgmtIpTCPOutSegs = _TfrapPerfMgmtIpTCPOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 2, 5, 6),
    _TfrapPerfMgmtIpTCPOutSegs_Type()
)
tfrapPerfMgmtIpTCPOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfMgmtIpTCPOutSegs.setStatus("mandatory")
_TfrapPerfThruput_ObjectIdentity = ObjectIdentity
tfrapPerfThruput = _TfrapPerfThruput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3)
)
_TfrapPerfThruputPerIntfTable_Object = MibTable
tfrapPerfThruputPerIntfTable = _TfrapPerfThruputPerIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfTable.setStatus("mandatory")
_TfrapPerfThruputPerIntfEntry_Object = MibTableRow
tfrapPerfThruputPerIntfEntry = _TfrapPerfThruputPerIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1)
)
tfrapPerfThruputPerIntfEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfThruputPerIntfIndex"),
)
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfEntry.setStatus("mandatory")


class _TfrapPerfThruputPerIntfIndex_Type(Integer32):
    """Custom type tfrapPerfThruputPerIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dte", 1),
          ("t1", 2))
    )


_TfrapPerfThruputPerIntfIndex_Type.__name__ = "Integer32"
_TfrapPerfThruputPerIntfIndex_Object = MibTableColumn
tfrapPerfThruputPerIntfIndex = _TfrapPerfThruputPerIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 1),
    _TfrapPerfThruputPerIntfIndex_Type()
)
tfrapPerfThruputPerIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfIndex.setStatus("mandatory")
_TfrapPerfThruputPerIntfRxByteCnt_Type = Counter32
_TfrapPerfThruputPerIntfRxByteCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfRxByteCnt = _TfrapPerfThruputPerIntfRxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 2),
    _TfrapPerfThruputPerIntfRxByteCnt_Type()
)
tfrapPerfThruputPerIntfRxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfRxByteCnt.setStatus("mandatory")
_TfrapPerfThruputPerIntfTxByteCnt_Type = Counter32
_TfrapPerfThruputPerIntfTxByteCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfTxByteCnt = _TfrapPerfThruputPerIntfTxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 3),
    _TfrapPerfThruputPerIntfTxByteCnt_Type()
)
tfrapPerfThruputPerIntfTxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfTxByteCnt.setStatus("mandatory")
_TfrapPerfThruputPerIntfRxFrameCnt_Type = Counter32
_TfrapPerfThruputPerIntfRxFrameCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfRxFrameCnt = _TfrapPerfThruputPerIntfRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 4),
    _TfrapPerfThruputPerIntfRxFrameCnt_Type()
)
tfrapPerfThruputPerIntfRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfRxFrameCnt.setStatus("mandatory")
_TfrapPerfThruputPerIntfTxFrameCnt_Type = Counter32
_TfrapPerfThruputPerIntfTxFrameCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfTxFrameCnt = _TfrapPerfThruputPerIntfTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 5),
    _TfrapPerfThruputPerIntfTxFrameCnt_Type()
)
tfrapPerfThruputPerIntfTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfTxFrameCnt.setStatus("mandatory")
_TfrapPerfThruputPerIntfRxCrcErrCnt_Type = Counter32
_TfrapPerfThruputPerIntfRxCrcErrCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfRxCrcErrCnt = _TfrapPerfThruputPerIntfRxCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 6),
    _TfrapPerfThruputPerIntfRxCrcErrCnt_Type()
)
tfrapPerfThruputPerIntfRxCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfRxCrcErrCnt.setStatus("mandatory")
_TfrapPerfThruputPerIntfRxAbortCnt_Type = Counter32
_TfrapPerfThruputPerIntfRxAbortCnt_Object = MibTableColumn
tfrapPerfThruputPerIntfRxAbortCnt = _TfrapPerfThruputPerIntfRxAbortCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 1, 1, 7),
    _TfrapPerfThruputPerIntfRxAbortCnt_Type()
)
tfrapPerfThruputPerIntfRxAbortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerIntfRxAbortCnt.setStatus("mandatory")
_TfrapPerfThruputPerDlciTable_Object = MibTable
tfrapPerfThruputPerDlciTable = _TfrapPerfThruputPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2)
)
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTable.setStatus("mandatory")
_TfrapPerfThruputPerDlciEntry_Object = MibTableRow
tfrapPerfThruputPerDlciEntry = _TfrapPerfThruputPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1)
)
tfrapPerfThruputPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfThruputPerDlciIndex"),
    (0, "TFRAP-MIB", "tfrapPerfThruputPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciEntry.setStatus("mandatory")
_TfrapPerfThruputPerDlciIndex_Type = Index
_TfrapPerfThruputPerDlciIndex_Object = MibTableColumn
tfrapPerfThruputPerDlciIndex = _TfrapPerfThruputPerDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 1),
    _TfrapPerfThruputPerDlciIndex_Type()
)
tfrapPerfThruputPerDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciIndex.setStatus("mandatory")
_TfrapPerfThruputPerDlciValue_Type = Integer32
_TfrapPerfThruputPerDlciValue_Object = MibTableColumn
tfrapPerfThruputPerDlciValue = _TfrapPerfThruputPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 2),
    _TfrapPerfThruputPerDlciValue_Type()
)
tfrapPerfThruputPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciValue.setStatus("mandatory")
_TfrapPerfThruputPerDlciCreateTime_Type = Integer32
_TfrapPerfThruputPerDlciCreateTime_Object = MibTableColumn
tfrapPerfThruputPerDlciCreateTime = _TfrapPerfThruputPerDlciCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 3),
    _TfrapPerfThruputPerDlciCreateTime_Type()
)
tfrapPerfThruputPerDlciCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciCreateTime.setStatus("mandatory")
_TfrapPerfThruputPerDlciChangeTime_Type = Integer32
_TfrapPerfThruputPerDlciChangeTime_Object = MibTableColumn
tfrapPerfThruputPerDlciChangeTime = _TfrapPerfThruputPerDlciChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 4),
    _TfrapPerfThruputPerDlciChangeTime_Type()
)
tfrapPerfThruputPerDlciChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciChangeTime.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxByte_Type = Counter32
_TfrapPerfThruputPerDlciRxByte_Object = MibTableColumn
tfrapPerfThruputPerDlciRxByte = _TfrapPerfThruputPerDlciRxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 5),
    _TfrapPerfThruputPerDlciRxByte_Type()
)
tfrapPerfThruputPerDlciRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxByte.setStatus("mandatory")
_TfrapPerfThruputPerDlciTxByte_Type = Counter32
_TfrapPerfThruputPerDlciTxByte_Object = MibTableColumn
tfrapPerfThruputPerDlciTxByte = _TfrapPerfThruputPerDlciTxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 6),
    _TfrapPerfThruputPerDlciTxByte_Type()
)
tfrapPerfThruputPerDlciTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTxByte.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxFrame_Type = Counter32
_TfrapPerfThruputPerDlciRxFrame_Object = MibTableColumn
tfrapPerfThruputPerDlciRxFrame = _TfrapPerfThruputPerDlciRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 7),
    _TfrapPerfThruputPerDlciRxFrame_Type()
)
tfrapPerfThruputPerDlciRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxFrame.setStatus("mandatory")
_TfrapPerfThruputPerDlciTxFrame_Type = Counter32
_TfrapPerfThruputPerDlciTxFrame_Object = MibTableColumn
tfrapPerfThruputPerDlciTxFrame = _TfrapPerfThruputPerDlciTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 8),
    _TfrapPerfThruputPerDlciTxFrame_Type()
)
tfrapPerfThruputPerDlciTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTxFrame.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxFecn_Type = Counter32
_TfrapPerfThruputPerDlciRxFecn_Object = MibTableColumn
tfrapPerfThruputPerDlciRxFecn = _TfrapPerfThruputPerDlciRxFecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 9),
    _TfrapPerfThruputPerDlciRxFecn_Type()
)
tfrapPerfThruputPerDlciRxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxFecn.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxBecn_Type = Counter32
_TfrapPerfThruputPerDlciRxBecn_Object = MibTableColumn
tfrapPerfThruputPerDlciRxBecn = _TfrapPerfThruputPerDlciRxBecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 10),
    _TfrapPerfThruputPerDlciRxBecn_Type()
)
tfrapPerfThruputPerDlciRxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxBecn.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxDe_Type = Counter32
_TfrapPerfThruputPerDlciRxDe_Object = MibTableColumn
tfrapPerfThruputPerDlciRxDe = _TfrapPerfThruputPerDlciRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 11),
    _TfrapPerfThruputPerDlciRxDe_Type()
)
tfrapPerfThruputPerDlciRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxDe.setStatus("mandatory")
_TfrapPerfThruputPerDlciTxDe_Type = Counter32
_TfrapPerfThruputPerDlciTxDe_Object = MibTableColumn
tfrapPerfThruputPerDlciTxDe = _TfrapPerfThruputPerDlciTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 12),
    _TfrapPerfThruputPerDlciTxDe_Type()
)
tfrapPerfThruputPerDlciTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTxDe.setStatus("mandatory")
_TfrapPerfThruputPerDlciRxThruput_Type = Integer32
_TfrapPerfThruputPerDlciRxThruput_Object = MibTableColumn
tfrapPerfThruputPerDlciRxThruput = _TfrapPerfThruputPerDlciRxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 13),
    _TfrapPerfThruputPerDlciRxThruput_Type()
)
tfrapPerfThruputPerDlciRxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxThruput.setStatus("mandatory")
_TfrapPerfThruputPerDlciTxThruput_Type = Integer32
_TfrapPerfThruputPerDlciTxThruput_Object = MibTableColumn
tfrapPerfThruputPerDlciTxThruput = _TfrapPerfThruputPerDlciTxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 14),
    _TfrapPerfThruputPerDlciTxThruput_Type()
)
tfrapPerfThruputPerDlciTxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTxThruput.setStatus("mandatory")
_TfrapPerfThruputPerDlciCIR_Type = Integer32
_TfrapPerfThruputPerDlciCIR_Object = MibTableColumn
tfrapPerfThruputPerDlciCIR = _TfrapPerfThruputPerDlciCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 15),
    _TfrapPerfThruputPerDlciCIR_Type()
)
tfrapPerfThruputPerDlciCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciCIR.setStatus("mandatory")
_TfrapPerfThruputPerDlciUptime_Type = Integer32
_TfrapPerfThruputPerDlciUptime_Object = MibTableColumn
tfrapPerfThruputPerDlciUptime = _TfrapPerfThruputPerDlciUptime_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 16),
    _TfrapPerfThruputPerDlciUptime_Type()
)
tfrapPerfThruputPerDlciUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciUptime.setStatus("mandatory")
_TfrapPerfThruputPerDlciDowntime_Type = Integer32
_TfrapPerfThruputPerDlciDowntime_Object = MibTableColumn
tfrapPerfThruputPerDlciDowntime = _TfrapPerfThruputPerDlciDowntime_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 17),
    _TfrapPerfThruputPerDlciDowntime_Type()
)
tfrapPerfThruputPerDlciDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciDowntime.setStatus("mandatory")


class _TfrapPerfThruputPerDlciCirType_Type(Integer32):
    """Custom type tfrapPerfThruputPerDlciCirType based on Integer32"""
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


_TfrapPerfThruputPerDlciCirType_Type.__name__ = "Integer32"
_TfrapPerfThruputPerDlciCirType_Object = MibTableColumn
tfrapPerfThruputPerDlciCirType = _TfrapPerfThruputPerDlciCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 18),
    _TfrapPerfThruputPerDlciCirType_Type()
)
tfrapPerfThruputPerDlciCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciCirType.setStatus("mandatory")


class _TfrapPerfThruputPerDlciPvcState_Type(Integer32):
    """Custom type tfrapPerfThruputPerDlciPvcState based on Integer32"""
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


_TfrapPerfThruputPerDlciPvcState_Type.__name__ = "Integer32"
_TfrapPerfThruputPerDlciPvcState_Object = MibTableColumn
tfrapPerfThruputPerDlciPvcState = _TfrapPerfThruputPerDlciPvcState_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 19),
    _TfrapPerfThruputPerDlciPvcState_Type()
)
tfrapPerfThruputPerDlciPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciPvcState.setStatus("mandatory")
_TfrapPerfThruputPerDlciOutageCount_Type = Counter32
_TfrapPerfThruputPerDlciOutageCount_Object = MibTableColumn
tfrapPerfThruputPerDlciOutageCount = _TfrapPerfThruputPerDlciOutageCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 20),
    _TfrapPerfThruputPerDlciOutageCount_Type()
)
tfrapPerfThruputPerDlciOutageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciOutageCount.setStatus("mandatory")
_TfrapPerfThruputPerDlciAvailability_Type = Integer32
_TfrapPerfThruputPerDlciAvailability_Object = MibTableColumn
tfrapPerfThruputPerDlciAvailability = _TfrapPerfThruputPerDlciAvailability_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 21),
    _TfrapPerfThruputPerDlciAvailability_Type()
)
tfrapPerfThruputPerDlciAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciAvailability.setStatus("mandatory")
_TfrapPerfThruputPerDlciMTBSO_Type = Integer32
_TfrapPerfThruputPerDlciMTBSO_Object = MibTableColumn
tfrapPerfThruputPerDlciMTBSO = _TfrapPerfThruputPerDlciMTBSO_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 22),
    _TfrapPerfThruputPerDlciMTBSO_Type()
)
tfrapPerfThruputPerDlciMTBSO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciMTBSO.setStatus("mandatory")
_TfrapPerfThruputPerDlciMTTSR_Type = Integer32
_TfrapPerfThruputPerDlciMTTSR_Object = MibTableColumn
tfrapPerfThruputPerDlciMTTSR = _TfrapPerfThruputPerDlciMTTSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 23),
    _TfrapPerfThruputPerDlciMTTSR_Type()
)
tfrapPerfThruputPerDlciMTTSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciMTTSR.setStatus("mandatory")


class _TfrapPerfThruputPerDlciEncapType_Type(Integer32):
    """Custom type tfrapPerfThruputPerDlciEncapType based on Integer32"""
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


_TfrapPerfThruputPerDlciEncapType_Type.__name__ = "Integer32"
_TfrapPerfThruputPerDlciEncapType_Object = MibTableColumn
tfrapPerfThruputPerDlciEncapType = _TfrapPerfThruputPerDlciEncapType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 24),
    _TfrapPerfThruputPerDlciEncapType_Type()
)
tfrapPerfThruputPerDlciEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciEncapType.setStatus("mandatory")


class _TfrapPerfThruputPerDlciRxUtilizationStatus_Type(Integer32):
    """Custom type tfrapPerfThruputPerDlciRxUtilizationStatus based on Integer32"""
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


_TfrapPerfThruputPerDlciRxUtilizationStatus_Type.__name__ = "Integer32"
_TfrapPerfThruputPerDlciRxUtilizationStatus_Object = MibTableColumn
tfrapPerfThruputPerDlciRxUtilizationStatus = _TfrapPerfThruputPerDlciRxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 25),
    _TfrapPerfThruputPerDlciRxUtilizationStatus_Type()
)
tfrapPerfThruputPerDlciRxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciRxUtilizationStatus.setStatus("mandatory")


class _TfrapPerfThruputPerDlciTxUtilizationStatus_Type(Integer32):
    """Custom type tfrapPerfThruputPerDlciTxUtilizationStatus based on Integer32"""
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


_TfrapPerfThruputPerDlciTxUtilizationStatus_Type.__name__ = "Integer32"
_TfrapPerfThruputPerDlciTxUtilizationStatus_Object = MibTableColumn
tfrapPerfThruputPerDlciTxUtilizationStatus = _TfrapPerfThruputPerDlciTxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 26),
    _TfrapPerfThruputPerDlciTxUtilizationStatus_Type()
)
tfrapPerfThruputPerDlciTxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciTxUtilizationStatus.setStatus("mandatory")
_TfrapPerfThruputPerDlciEIR_Type = Integer32
_TfrapPerfThruputPerDlciEIR_Object = MibTableColumn
tfrapPerfThruputPerDlciEIR = _TfrapPerfThruputPerDlciEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 2, 1, 27),
    _TfrapPerfThruputPerDlciEIR_Type()
)
tfrapPerfThruputPerDlciEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputPerDlciEIR.setStatus("mandatory")
_TfrapPerfThruputCommands_ObjectIdentity = ObjectIdentity
tfrapPerfThruputCommands = _TfrapPerfThruputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3)
)


class _TfrapPerfThruputCmdClearDteStats_Type(Integer32):
    """Custom type tfrapPerfThruputCmdClearDteStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfThruputCmdClearDteStats_Type.__name__ = "Integer32"
_TfrapPerfThruputCmdClearDteStats_Object = MibScalar
tfrapPerfThruputCmdClearDteStats = _TfrapPerfThruputCmdClearDteStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 1),
    _TfrapPerfThruputCmdClearDteStats_Type()
)
tfrapPerfThruputCmdClearDteStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdClearDteStats.setStatus("mandatory")


class _TfrapPerfThruputCmdClearT1Stats_Type(Integer32):
    """Custom type tfrapPerfThruputCmdClearT1Stats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfThruputCmdClearT1Stats_Type.__name__ = "Integer32"
_TfrapPerfThruputCmdClearT1Stats_Object = MibScalar
tfrapPerfThruputCmdClearT1Stats = _TfrapPerfThruputCmdClearT1Stats_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 2),
    _TfrapPerfThruputCmdClearT1Stats_Type()
)
tfrapPerfThruputCmdClearT1Stats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdClearT1Stats.setStatus("mandatory")


class _TfrapPerfThruputCmdClearAllIntfStats_Type(Integer32):
    """Custom type tfrapPerfThruputCmdClearAllIntfStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfThruputCmdClearAllIntfStats_Type.__name__ = "Integer32"
_TfrapPerfThruputCmdClearAllIntfStats_Object = MibScalar
tfrapPerfThruputCmdClearAllIntfStats = _TfrapPerfThruputCmdClearAllIntfStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 3),
    _TfrapPerfThruputCmdClearAllIntfStats_Type()
)
tfrapPerfThruputCmdClearAllIntfStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdClearAllIntfStats.setStatus("mandatory")


class _TfrapPerfThruputCmdClearDlciStats_Type(Integer32):
    """Custom type tfrapPerfThruputCmdClearDlciStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfThruputCmdClearDlciStats_Type.__name__ = "Integer32"
_TfrapPerfThruputCmdClearDlciStats_Object = MibScalar
tfrapPerfThruputCmdClearDlciStats = _TfrapPerfThruputCmdClearDlciStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 4),
    _TfrapPerfThruputCmdClearDlciStats_Type()
)
tfrapPerfThruputCmdClearDlciStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdClearDlciStats.setStatus("mandatory")


class _TfrapPerfThruputCmdClearAllStats_Type(Integer32):
    """Custom type tfrapPerfThruputCmdClearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfThruputCmdClearAllStats_Type.__name__ = "Integer32"
_TfrapPerfThruputCmdClearAllStats_Object = MibScalar
tfrapPerfThruputCmdClearAllStats = _TfrapPerfThruputCmdClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 5),
    _TfrapPerfThruputCmdClearAllStats_Type()
)
tfrapPerfThruputCmdClearAllStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdClearAllStats.setStatus("mandatory")
_TfrapPerfThruputCmdRemoveStsDlci_Type = Integer32
_TfrapPerfThruputCmdRemoveStsDlci_Object = MibScalar
tfrapPerfThruputCmdRemoveStsDlci = _TfrapPerfThruputCmdRemoveStsDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 6),
    _TfrapPerfThruputCmdRemoveStsDlci_Type()
)
tfrapPerfThruputCmdRemoveStsDlci.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdRemoveStsDlci.setStatus("mandatory")
_TfrapPerfThruputCmdReplaceDlciTable_Object = MibTable
tfrapPerfThruputCmdReplaceDlciTable = _TfrapPerfThruputCmdReplaceDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 7)
)
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdReplaceDlciTable.setStatus("mandatory")
_TfrapPerfThruputCmdReplaceDlciEntry_Object = MibTableRow
tfrapPerfThruputCmdReplaceDlciEntry = _TfrapPerfThruputCmdReplaceDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 7, 1)
)
tfrapPerfThruputCmdReplaceDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfThruputCmdReplaceDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdReplaceDlciEntry.setStatus("mandatory")
_TfrapPerfThruputCmdReplaceDlciValue_Type = Integer32
_TfrapPerfThruputCmdReplaceDlciValue_Object = MibTableColumn
tfrapPerfThruputCmdReplaceDlciValue = _TfrapPerfThruputCmdReplaceDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 7, 1, 1),
    _TfrapPerfThruputCmdReplaceDlciValue_Type()
)
tfrapPerfThruputCmdReplaceDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdReplaceDlciValue.setStatus("mandatory")
_TfrapPerfThruputCmdReplaceDlciNewValue_Type = Integer32
_TfrapPerfThruputCmdReplaceDlciNewValue_Object = MibTableColumn
tfrapPerfThruputCmdReplaceDlciNewValue = _TfrapPerfThruputCmdReplaceDlciNewValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 7, 1, 2),
    _TfrapPerfThruputCmdReplaceDlciNewValue_Type()
)
tfrapPerfThruputCmdReplaceDlciNewValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdReplaceDlciNewValue.setStatus("mandatory")
_TfrapPerfThruputCmdAvailabilityStsDlciReset_Type = Integer32
_TfrapPerfThruputCmdAvailabilityStsDlciReset_Object = MibScalar
tfrapPerfThruputCmdAvailabilityStsDlciReset = _TfrapPerfThruputCmdAvailabilityStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 8),
    _TfrapPerfThruputCmdAvailabilityStsDlciReset_Type()
)
tfrapPerfThruputCmdAvailabilityStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdAvailabilityStsDlciReset.setStatus("mandatory")
_TfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type = Integer32
_TfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object = MibScalar
tfrapPerfThruputCmdAvailabilityStsDlciResetAll = _TfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 9),
    _TfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type()
)
tfrapPerfThruputCmdAvailabilityStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdAvailabilityStsDlciResetAll.setStatus("mandatory")
_TfrapPerfThruputCmdCountsStsDlciReset_Type = Integer32
_TfrapPerfThruputCmdCountsStsDlciReset_Object = MibScalar
tfrapPerfThruputCmdCountsStsDlciReset = _TfrapPerfThruputCmdCountsStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 10),
    _TfrapPerfThruputCmdCountsStsDlciReset_Type()
)
tfrapPerfThruputCmdCountsStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdCountsStsDlciReset.setStatus("mandatory")
_TfrapPerfThruputCmdCountsStsDlciResetAll_Type = Integer32
_TfrapPerfThruputCmdCountsStsDlciResetAll_Object = MibScalar
tfrapPerfThruputCmdCountsStsDlciResetAll = _TfrapPerfThruputCmdCountsStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 11),
    _TfrapPerfThruputCmdCountsStsDlciResetAll_Type()
)
tfrapPerfThruputCmdCountsStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdCountsStsDlciResetAll.setStatus("mandatory")
_TfrapPerfThruputCmdAllStsDlciReset_Type = Integer32
_TfrapPerfThruputCmdAllStsDlciReset_Object = MibScalar
tfrapPerfThruputCmdAllStsDlciReset = _TfrapPerfThruputCmdAllStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 12),
    _TfrapPerfThruputCmdAllStsDlciReset_Type()
)
tfrapPerfThruputCmdAllStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdAllStsDlciReset.setStatus("mandatory")
_TfrapPerfThruputCmdAllStsDlciResetAll_Type = Integer32
_TfrapPerfThruputCmdAllStsDlciResetAll_Object = MibScalar
tfrapPerfThruputCmdAllStsDlciResetAll = _TfrapPerfThruputCmdAllStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 3, 3, 13),
    _TfrapPerfThruputCmdAllStsDlciResetAll_Type()
)
tfrapPerfThruputCmdAllStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfThruputCmdAllStsDlciResetAll.setStatus("mandatory")
_TfrapPerfNetworkShortTerm_ObjectIdentity = ObjectIdentity
tfrapPerfNetworkShortTerm = _TfrapPerfNetworkShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4)
)
_TfrapPerfNetwProtoPerDlciTable_Object = MibTable
tfrapPerfNetwProtoPerDlciTable = _TfrapPerfNetwProtoPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTable.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciEntry_Object = MibTableRow
tfrapPerfNetwProtoPerDlciEntry = _TfrapPerfNetwProtoPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1)
)
tfrapPerfNetwProtoPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfNetwProtoPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfNetwProtoPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciEntry.setStatus("mandatory")


class _TfrapPerfNetwProtoPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfNetwProtoPerDlciInterval based on Integer32"""
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


_TfrapPerfNetwProtoPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfNetwProtoPerDlciInterval_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciInterval = _TfrapPerfNetwProtoPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 1),
    _TfrapPerfNetwProtoPerDlciInterval_Type()
)
tfrapPerfNetwProtoPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciInterval.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciValue_Type = Integer32
_TfrapPerfNetwProtoPerDlciValue_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciValue = _TfrapPerfNetwProtoPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 2),
    _TfrapPerfNetwProtoPerDlciValue_Type()
)
tfrapPerfNetwProtoPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciValue.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxTotal_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxTotal_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxTotal = _TfrapPerfNetwProtoPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 3),
    _TfrapPerfNetwProtoPerDlciRxTotal_Type()
)
tfrapPerfNetwProtoPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxTotal_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxTotal_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxTotal = _TfrapPerfNetwProtoPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 4),
    _TfrapPerfNetwProtoPerDlciTxTotal_Type()
)
tfrapPerfNetwProtoPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxIp_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxIp_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxIp = _TfrapPerfNetwProtoPerDlciRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 5),
    _TfrapPerfNetwProtoPerDlciRxIp_Type()
)
tfrapPerfNetwProtoPerDlciRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxIp.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxIp_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxIp_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxIp = _TfrapPerfNetwProtoPerDlciTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 6),
    _TfrapPerfNetwProtoPerDlciTxIp_Type()
)
tfrapPerfNetwProtoPerDlciTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxIp.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxIpx_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxIpx_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxIpx = _TfrapPerfNetwProtoPerDlciRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 7),
    _TfrapPerfNetwProtoPerDlciRxIpx_Type()
)
tfrapPerfNetwProtoPerDlciRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxIpx.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxIpx_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxIpx_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxIpx = _TfrapPerfNetwProtoPerDlciTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 8),
    _TfrapPerfNetwProtoPerDlciTxIpx_Type()
)
tfrapPerfNetwProtoPerDlciTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxIpx.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxSna_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxSna_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxSna = _TfrapPerfNetwProtoPerDlciRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 9),
    _TfrapPerfNetwProtoPerDlciRxSna_Type()
)
tfrapPerfNetwProtoPerDlciRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxSna.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxSna_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxSna_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxSna = _TfrapPerfNetwProtoPerDlciTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 10),
    _TfrapPerfNetwProtoPerDlciTxSna_Type()
)
tfrapPerfNetwProtoPerDlciTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxSna.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxArp_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxArp_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxArp = _TfrapPerfNetwProtoPerDlciRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 11),
    _TfrapPerfNetwProtoPerDlciRxArp_Type()
)
tfrapPerfNetwProtoPerDlciRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxArp.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxArp_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxArp_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxArp = _TfrapPerfNetwProtoPerDlciTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 12),
    _TfrapPerfNetwProtoPerDlciTxArp_Type()
)
tfrapPerfNetwProtoPerDlciTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxArp.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxCisco_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxCisco_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxCisco = _TfrapPerfNetwProtoPerDlciRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 13),
    _TfrapPerfNetwProtoPerDlciRxCisco_Type()
)
tfrapPerfNetwProtoPerDlciRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxCisco.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxCisco_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxCisco_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxCisco = _TfrapPerfNetwProtoPerDlciTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 14),
    _TfrapPerfNetwProtoPerDlciTxCisco_Type()
)
tfrapPerfNetwProtoPerDlciTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxCisco.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxOther_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxOther_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxOther = _TfrapPerfNetwProtoPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 15),
    _TfrapPerfNetwProtoPerDlciRxOther_Type()
)
tfrapPerfNetwProtoPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxOther.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxOther_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxOther_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxOther = _TfrapPerfNetwProtoPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 16),
    _TfrapPerfNetwProtoPerDlciTxOther_Type()
)
tfrapPerfNetwProtoPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxOther.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxVnip_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxVnip_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxVnip = _TfrapPerfNetwProtoPerDlciRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 17),
    _TfrapPerfNetwProtoPerDlciRxVnip_Type()
)
tfrapPerfNetwProtoPerDlciRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxVnip.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxVnip_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxVnip_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxVnip = _TfrapPerfNetwProtoPerDlciTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 18),
    _TfrapPerfNetwProtoPerDlciTxVnip_Type()
)
tfrapPerfNetwProtoPerDlciTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxVnip.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciRxAnnexG_Type = Counter32
_TfrapPerfNetwProtoPerDlciRxAnnexG_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciRxAnnexG = _TfrapPerfNetwProtoPerDlciRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 19),
    _TfrapPerfNetwProtoPerDlciRxAnnexG_Type()
)
tfrapPerfNetwProtoPerDlciRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciRxAnnexG.setStatus("mandatory")
_TfrapPerfNetwProtoPerDlciTxAnnexG_Type = Counter32
_TfrapPerfNetwProtoPerDlciTxAnnexG_Object = MibTableColumn
tfrapPerfNetwProtoPerDlciTxAnnexG = _TfrapPerfNetwProtoPerDlciTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 1, 1, 20),
    _TfrapPerfNetwProtoPerDlciTxAnnexG_Type()
)
tfrapPerfNetwProtoPerDlciTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoPerDlciTxAnnexG.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTable_Object = MibTable
tfrapPerfNetwProtoTotalTable = _TfrapPerfNetwProtoTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2)
)
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTable.setStatus("mandatory")
_TfrapPerfNetwProtoTotalEntry_Object = MibTableRow
tfrapPerfNetwProtoTotalEntry = _TfrapPerfNetwProtoTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1)
)
tfrapPerfNetwProtoTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfNetwProtoTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalEntry.setStatus("mandatory")


class _TfrapPerfNetwProtoTotalInterval_Type(Integer32):
    """Custom type tfrapPerfNetwProtoTotalInterval based on Integer32"""
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


_TfrapPerfNetwProtoTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfNetwProtoTotalInterval_Object = MibTableColumn
tfrapPerfNetwProtoTotalInterval = _TfrapPerfNetwProtoTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 1),
    _TfrapPerfNetwProtoTotalInterval_Type()
)
tfrapPerfNetwProtoTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalInterval.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxTotal_Type = Counter32
_TfrapPerfNetwProtoTotalRxTotal_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxTotal = _TfrapPerfNetwProtoTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 3),
    _TfrapPerfNetwProtoTotalRxTotal_Type()
)
tfrapPerfNetwProtoTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxTotal.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxTotal_Type = Counter32
_TfrapPerfNetwProtoTotalTxTotal_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxTotal = _TfrapPerfNetwProtoTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 4),
    _TfrapPerfNetwProtoTotalTxTotal_Type()
)
tfrapPerfNetwProtoTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxTotal.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxIp_Type = Counter32
_TfrapPerfNetwProtoTotalRxIp_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxIp = _TfrapPerfNetwProtoTotalRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 5),
    _TfrapPerfNetwProtoTotalRxIp_Type()
)
tfrapPerfNetwProtoTotalRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxIp.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxIp_Type = Counter32
_TfrapPerfNetwProtoTotalTxIp_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxIp = _TfrapPerfNetwProtoTotalTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 6),
    _TfrapPerfNetwProtoTotalTxIp_Type()
)
tfrapPerfNetwProtoTotalTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxIp.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxIpx_Type = Counter32
_TfrapPerfNetwProtoTotalRxIpx_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxIpx = _TfrapPerfNetwProtoTotalRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 7),
    _TfrapPerfNetwProtoTotalRxIpx_Type()
)
tfrapPerfNetwProtoTotalRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxIpx.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxIpx_Type = Counter32
_TfrapPerfNetwProtoTotalTxIpx_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxIpx = _TfrapPerfNetwProtoTotalTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 8),
    _TfrapPerfNetwProtoTotalTxIpx_Type()
)
tfrapPerfNetwProtoTotalTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxIpx.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxSna_Type = Counter32
_TfrapPerfNetwProtoTotalRxSna_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxSna = _TfrapPerfNetwProtoTotalRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 9),
    _TfrapPerfNetwProtoTotalRxSna_Type()
)
tfrapPerfNetwProtoTotalRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxSna.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxSna_Type = Counter32
_TfrapPerfNetwProtoTotalTxSna_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxSna = _TfrapPerfNetwProtoTotalTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 10),
    _TfrapPerfNetwProtoTotalTxSna_Type()
)
tfrapPerfNetwProtoTotalTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxSna.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxArp_Type = Counter32
_TfrapPerfNetwProtoTotalRxArp_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxArp = _TfrapPerfNetwProtoTotalRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 11),
    _TfrapPerfNetwProtoTotalRxArp_Type()
)
tfrapPerfNetwProtoTotalRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxArp.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxArp_Type = Counter32
_TfrapPerfNetwProtoTotalTxArp_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxArp = _TfrapPerfNetwProtoTotalTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 12),
    _TfrapPerfNetwProtoTotalTxArp_Type()
)
tfrapPerfNetwProtoTotalTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxArp.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxCisco_Type = Counter32
_TfrapPerfNetwProtoTotalRxCisco_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxCisco = _TfrapPerfNetwProtoTotalRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 13),
    _TfrapPerfNetwProtoTotalRxCisco_Type()
)
tfrapPerfNetwProtoTotalRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxCisco.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxCisco_Type = Counter32
_TfrapPerfNetwProtoTotalTxCisco_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxCisco = _TfrapPerfNetwProtoTotalTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 14),
    _TfrapPerfNetwProtoTotalTxCisco_Type()
)
tfrapPerfNetwProtoTotalTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxCisco.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxOther_Type = Counter32
_TfrapPerfNetwProtoTotalRxOther_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxOther = _TfrapPerfNetwProtoTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 15),
    _TfrapPerfNetwProtoTotalRxOther_Type()
)
tfrapPerfNetwProtoTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxOther.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxOther_Type = Counter32
_TfrapPerfNetwProtoTotalTxOther_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxOther = _TfrapPerfNetwProtoTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 16),
    _TfrapPerfNetwProtoTotalTxOther_Type()
)
tfrapPerfNetwProtoTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxOther.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxVnip_Type = Counter32
_TfrapPerfNetwProtoTotalRxVnip_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxVnip = _TfrapPerfNetwProtoTotalRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 17),
    _TfrapPerfNetwProtoTotalRxVnip_Type()
)
tfrapPerfNetwProtoTotalRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxVnip.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxVnip_Type = Counter32
_TfrapPerfNetwProtoTotalTxVnip_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxVnip = _TfrapPerfNetwProtoTotalTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 18),
    _TfrapPerfNetwProtoTotalTxVnip_Type()
)
tfrapPerfNetwProtoTotalTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxVnip.setStatus("mandatory")
_TfrapPerfNetwProtoTotalRxAnnexG_Type = Counter32
_TfrapPerfNetwProtoTotalRxAnnexG_Object = MibTableColumn
tfrapPerfNetwProtoTotalRxAnnexG = _TfrapPerfNetwProtoTotalRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 19),
    _TfrapPerfNetwProtoTotalRxAnnexG_Type()
)
tfrapPerfNetwProtoTotalRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalRxAnnexG.setStatus("mandatory")
_TfrapPerfNetwProtoTotalTxAnnexG_Type = Counter32
_TfrapPerfNetwProtoTotalTxAnnexG_Object = MibTableColumn
tfrapPerfNetwProtoTotalTxAnnexG = _TfrapPerfNetwProtoTotalTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 2, 1, 20),
    _TfrapPerfNetwProtoTotalTxAnnexG_Type()
)
tfrapPerfNetwProtoTotalTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwProtoTotalTxAnnexG.setStatus("mandatory")
_TfrapPerfIpPerDlciTable_Object = MibTable
tfrapPerfIpPerDlciTable = _TfrapPerfIpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3)
)
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTable.setStatus("mandatory")
_TfrapPerfIpPerDlciEntry_Object = MibTableRow
tfrapPerfIpPerDlciEntry = _TfrapPerfIpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1)
)
tfrapPerfIpPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIpPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfIpPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciEntry.setStatus("mandatory")


class _TfrapPerfIpPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfIpPerDlciInterval based on Integer32"""
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


_TfrapPerfIpPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfIpPerDlciInterval_Object = MibTableColumn
tfrapPerfIpPerDlciInterval = _TfrapPerfIpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 1),
    _TfrapPerfIpPerDlciInterval_Type()
)
tfrapPerfIpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciInterval.setStatus("mandatory")
_TfrapPerfIpPerDlciValue_Type = Integer32
_TfrapPerfIpPerDlciValue_Object = MibTableColumn
tfrapPerfIpPerDlciValue = _TfrapPerfIpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 2),
    _TfrapPerfIpPerDlciValue_Type()
)
tfrapPerfIpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciValue.setStatus("mandatory")
_TfrapPerfIpPerDlciRxTotal_Type = Counter32
_TfrapPerfIpPerDlciRxTotal_Object = MibTableColumn
tfrapPerfIpPerDlciRxTotal = _TfrapPerfIpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 3),
    _TfrapPerfIpPerDlciRxTotal_Type()
)
tfrapPerfIpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfIpPerDlciTxTotal_Type = Counter32
_TfrapPerfIpPerDlciTxTotal_Object = MibTableColumn
tfrapPerfIpPerDlciTxTotal = _TfrapPerfIpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 4),
    _TfrapPerfIpPerDlciTxTotal_Type()
)
tfrapPerfIpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfIpPerDlciRxTcp_Type = Counter32
_TfrapPerfIpPerDlciRxTcp_Object = MibTableColumn
tfrapPerfIpPerDlciRxTcp = _TfrapPerfIpPerDlciRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 5),
    _TfrapPerfIpPerDlciRxTcp_Type()
)
tfrapPerfIpPerDlciRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxTcp.setStatus("mandatory")
_TfrapPerfIpPerDlciTxTcp_Type = Counter32
_TfrapPerfIpPerDlciTxTcp_Object = MibTableColumn
tfrapPerfIpPerDlciTxTcp = _TfrapPerfIpPerDlciTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 6),
    _TfrapPerfIpPerDlciTxTcp_Type()
)
tfrapPerfIpPerDlciTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxTcp.setStatus("mandatory")
_TfrapPerfIpPerDlciRxUdp_Type = Counter32
_TfrapPerfIpPerDlciRxUdp_Object = MibTableColumn
tfrapPerfIpPerDlciRxUdp = _TfrapPerfIpPerDlciRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 7),
    _TfrapPerfIpPerDlciRxUdp_Type()
)
tfrapPerfIpPerDlciRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxUdp.setStatus("mandatory")
_TfrapPerfIpPerDlciTxUdp_Type = Counter32
_TfrapPerfIpPerDlciTxUdp_Object = MibTableColumn
tfrapPerfIpPerDlciTxUdp = _TfrapPerfIpPerDlciTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 8),
    _TfrapPerfIpPerDlciTxUdp_Type()
)
tfrapPerfIpPerDlciTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxUdp.setStatus("mandatory")
_TfrapPerfIpPerDlciRxIcmp_Type = Counter32
_TfrapPerfIpPerDlciRxIcmp_Object = MibTableColumn
tfrapPerfIpPerDlciRxIcmp = _TfrapPerfIpPerDlciRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 9),
    _TfrapPerfIpPerDlciRxIcmp_Type()
)
tfrapPerfIpPerDlciRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxIcmp.setStatus("mandatory")
_TfrapPerfIpPerDlciTxIcmp_Type = Counter32
_TfrapPerfIpPerDlciTxIcmp_Object = MibTableColumn
tfrapPerfIpPerDlciTxIcmp = _TfrapPerfIpPerDlciTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 10),
    _TfrapPerfIpPerDlciTxIcmp_Type()
)
tfrapPerfIpPerDlciTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxIcmp.setStatus("mandatory")
_TfrapPerfIpPerDlciRxOther_Type = Counter32
_TfrapPerfIpPerDlciRxOther_Object = MibTableColumn
tfrapPerfIpPerDlciRxOther = _TfrapPerfIpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 11),
    _TfrapPerfIpPerDlciRxOther_Type()
)
tfrapPerfIpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxOther.setStatus("mandatory")
_TfrapPerfIpPerDlciTxOther_Type = Counter32
_TfrapPerfIpPerDlciTxOther_Object = MibTableColumn
tfrapPerfIpPerDlciTxOther = _TfrapPerfIpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 12),
    _TfrapPerfIpPerDlciTxOther_Type()
)
tfrapPerfIpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxOther.setStatus("mandatory")
_TfrapPerfIpPerDlciRxIgrp_Type = Counter32
_TfrapPerfIpPerDlciRxIgrp_Object = MibTableColumn
tfrapPerfIpPerDlciRxIgrp = _TfrapPerfIpPerDlciRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 13),
    _TfrapPerfIpPerDlciRxIgrp_Type()
)
tfrapPerfIpPerDlciRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciRxIgrp.setStatus("mandatory")
_TfrapPerfIpPerDlciTxIgrp_Type = Counter32
_TfrapPerfIpPerDlciTxIgrp_Object = MibTableColumn
tfrapPerfIpPerDlciTxIgrp = _TfrapPerfIpPerDlciTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 3, 1, 14),
    _TfrapPerfIpPerDlciTxIgrp_Type()
)
tfrapPerfIpPerDlciTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpPerDlciTxIgrp.setStatus("mandatory")
_TfrapPerfIpTotalTable_Object = MibTable
tfrapPerfIpTotalTable = _TfrapPerfIpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4)
)
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTable.setStatus("mandatory")
_TfrapPerfIpTotalEntry_Object = MibTableRow
tfrapPerfIpTotalEntry = _TfrapPerfIpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1)
)
tfrapPerfIpTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIpTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfIpTotalEntry.setStatus("mandatory")


class _TfrapPerfIpTotalInterval_Type(Integer32):
    """Custom type tfrapPerfIpTotalInterval based on Integer32"""
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


_TfrapPerfIpTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfIpTotalInterval_Object = MibTableColumn
tfrapPerfIpTotalInterval = _TfrapPerfIpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 1),
    _TfrapPerfIpTotalInterval_Type()
)
tfrapPerfIpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalInterval.setStatus("mandatory")
_TfrapPerfIpTotalRxTotal_Type = Counter32
_TfrapPerfIpTotalRxTotal_Object = MibTableColumn
tfrapPerfIpTotalRxTotal = _TfrapPerfIpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 3),
    _TfrapPerfIpTotalRxTotal_Type()
)
tfrapPerfIpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxTotal.setStatus("mandatory")
_TfrapPerfIpTotalTxTotal_Type = Counter32
_TfrapPerfIpTotalTxTotal_Object = MibTableColumn
tfrapPerfIpTotalTxTotal = _TfrapPerfIpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 4),
    _TfrapPerfIpTotalTxTotal_Type()
)
tfrapPerfIpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxTotal.setStatus("mandatory")
_TfrapPerfIpTotalRxTcp_Type = Counter32
_TfrapPerfIpTotalRxTcp_Object = MibTableColumn
tfrapPerfIpTotalRxTcp = _TfrapPerfIpTotalRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 5),
    _TfrapPerfIpTotalRxTcp_Type()
)
tfrapPerfIpTotalRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxTcp.setStatus("mandatory")
_TfrapPerfIpTotalTxTcp_Type = Counter32
_TfrapPerfIpTotalTxTcp_Object = MibTableColumn
tfrapPerfIpTotalTxTcp = _TfrapPerfIpTotalTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 6),
    _TfrapPerfIpTotalTxTcp_Type()
)
tfrapPerfIpTotalTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxTcp.setStatus("mandatory")
_TfrapPerfIpTotalRxUdp_Type = Counter32
_TfrapPerfIpTotalRxUdp_Object = MibTableColumn
tfrapPerfIpTotalRxUdp = _TfrapPerfIpTotalRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 7),
    _TfrapPerfIpTotalRxUdp_Type()
)
tfrapPerfIpTotalRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxUdp.setStatus("mandatory")
_TfrapPerfIpTotalTxUdp_Type = Counter32
_TfrapPerfIpTotalTxUdp_Object = MibTableColumn
tfrapPerfIpTotalTxUdp = _TfrapPerfIpTotalTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 8),
    _TfrapPerfIpTotalTxUdp_Type()
)
tfrapPerfIpTotalTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxUdp.setStatus("mandatory")
_TfrapPerfIpTotalRxIcmp_Type = Counter32
_TfrapPerfIpTotalRxIcmp_Object = MibTableColumn
tfrapPerfIpTotalRxIcmp = _TfrapPerfIpTotalRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 9),
    _TfrapPerfIpTotalRxIcmp_Type()
)
tfrapPerfIpTotalRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxIcmp.setStatus("mandatory")
_TfrapPerfIpTotalTxIcmp_Type = Counter32
_TfrapPerfIpTotalTxIcmp_Object = MibTableColumn
tfrapPerfIpTotalTxIcmp = _TfrapPerfIpTotalTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 10),
    _TfrapPerfIpTotalTxIcmp_Type()
)
tfrapPerfIpTotalTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxIcmp.setStatus("mandatory")
_TfrapPerfIpTotalRxOther_Type = Counter32
_TfrapPerfIpTotalRxOther_Object = MibTableColumn
tfrapPerfIpTotalRxOther = _TfrapPerfIpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 11),
    _TfrapPerfIpTotalRxOther_Type()
)
tfrapPerfIpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxOther.setStatus("mandatory")
_TfrapPerfIpTotalTxOther_Type = Counter32
_TfrapPerfIpTotalTxOther_Object = MibTableColumn
tfrapPerfIpTotalTxOther = _TfrapPerfIpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 12),
    _TfrapPerfIpTotalTxOther_Type()
)
tfrapPerfIpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxOther.setStatus("mandatory")
_TfrapPerfIpTotalRxIgrp_Type = Counter32
_TfrapPerfIpTotalRxIgrp_Object = MibTableColumn
tfrapPerfIpTotalRxIgrp = _TfrapPerfIpTotalRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 13),
    _TfrapPerfIpTotalRxIgrp_Type()
)
tfrapPerfIpTotalRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalRxIgrp.setStatus("mandatory")
_TfrapPerfIpTotalTxIgrp_Type = Counter32
_TfrapPerfIpTotalTxIgrp_Object = MibTableColumn
tfrapPerfIpTotalTxIgrp = _TfrapPerfIpTotalTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 4, 1, 14),
    _TfrapPerfIpTotalTxIgrp_Type()
)
tfrapPerfIpTotalTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpTotalTxIgrp.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTable_Object = MibTable
tfrapPerfIcmpPerDlciTable = _TfrapPerfIcmpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5)
)
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTable.setStatus("mandatory")
_TfrapPerfIcmpPerDlciEntry_Object = MibTableRow
tfrapPerfIcmpPerDlciEntry = _TfrapPerfIcmpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1)
)
tfrapPerfIcmpPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIcmpPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfIcmpPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciEntry.setStatus("mandatory")


class _TfrapPerfIcmpPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfIcmpPerDlciInterval based on Integer32"""
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


_TfrapPerfIcmpPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfIcmpPerDlciInterval_Object = MibTableColumn
tfrapPerfIcmpPerDlciInterval = _TfrapPerfIcmpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 1),
    _TfrapPerfIcmpPerDlciInterval_Type()
)
tfrapPerfIcmpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciInterval.setStatus("mandatory")
_TfrapPerfIcmpPerDlciValue_Type = Integer32
_TfrapPerfIcmpPerDlciValue_Object = MibTableColumn
tfrapPerfIcmpPerDlciValue = _TfrapPerfIcmpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 2),
    _TfrapPerfIcmpPerDlciValue_Type()
)
tfrapPerfIcmpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciValue.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxTotal_Type = Counter32
_TfrapPerfIcmpPerDlciRxTotal_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxTotal = _TfrapPerfIcmpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 3),
    _TfrapPerfIcmpPerDlciRxTotal_Type()
)
tfrapPerfIcmpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxTotal_Type = Counter32
_TfrapPerfIcmpPerDlciTxTotal_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxTotal = _TfrapPerfIcmpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 4),
    _TfrapPerfIcmpPerDlciTxTotal_Type()
)
tfrapPerfIcmpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxEchoRep_Type = Counter32
_TfrapPerfIcmpPerDlciRxEchoRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxEchoRep = _TfrapPerfIcmpPerDlciRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 5),
    _TfrapPerfIcmpPerDlciRxEchoRep_Type()
)
tfrapPerfIcmpPerDlciRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxEchoRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxEchoRep_Type = Counter32
_TfrapPerfIcmpPerDlciTxEchoRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxEchoRep = _TfrapPerfIcmpPerDlciTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 6),
    _TfrapPerfIcmpPerDlciTxEchoRep_Type()
)
tfrapPerfIcmpPerDlciTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxEchoRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxDestUnr_Type = Counter32
_TfrapPerfIcmpPerDlciRxDestUnr_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxDestUnr = _TfrapPerfIcmpPerDlciRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 7),
    _TfrapPerfIcmpPerDlciRxDestUnr_Type()
)
tfrapPerfIcmpPerDlciRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxDestUnr.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxDestUnr_Type = Counter32
_TfrapPerfIcmpPerDlciTxDestUnr_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxDestUnr = _TfrapPerfIcmpPerDlciTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 8),
    _TfrapPerfIcmpPerDlciTxDestUnr_Type()
)
tfrapPerfIcmpPerDlciTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxDestUnr.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxSrcQuench_Type = Counter32
_TfrapPerfIcmpPerDlciRxSrcQuench_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxSrcQuench = _TfrapPerfIcmpPerDlciRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 9),
    _TfrapPerfIcmpPerDlciRxSrcQuench_Type()
)
tfrapPerfIcmpPerDlciRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxSrcQuench.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxSrcQuench_Type = Counter32
_TfrapPerfIcmpPerDlciTxSrcQuench_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxSrcQuench = _TfrapPerfIcmpPerDlciTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 10),
    _TfrapPerfIcmpPerDlciTxSrcQuench_Type()
)
tfrapPerfIcmpPerDlciTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxSrcQuench.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxRedirect_Type = Counter32
_TfrapPerfIcmpPerDlciRxRedirect_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxRedirect = _TfrapPerfIcmpPerDlciRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 11),
    _TfrapPerfIcmpPerDlciRxRedirect_Type()
)
tfrapPerfIcmpPerDlciRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxRedirect.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxRedirect_Type = Counter32
_TfrapPerfIcmpPerDlciTxRedirect_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxRedirect = _TfrapPerfIcmpPerDlciTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 12),
    _TfrapPerfIcmpPerDlciTxRedirect_Type()
)
tfrapPerfIcmpPerDlciTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxRedirect.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxEchoReq_Type = Counter32
_TfrapPerfIcmpPerDlciRxEchoReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxEchoReq = _TfrapPerfIcmpPerDlciRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 13),
    _TfrapPerfIcmpPerDlciRxEchoReq_Type()
)
tfrapPerfIcmpPerDlciRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxEchoReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxEchoReq_Type = Counter32
_TfrapPerfIcmpPerDlciTxEchoReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxEchoReq = _TfrapPerfIcmpPerDlciTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 14),
    _TfrapPerfIcmpPerDlciTxEchoReq_Type()
)
tfrapPerfIcmpPerDlciTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxEchoReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxTimeExcd_Type = Counter32
_TfrapPerfIcmpPerDlciRxTimeExcd_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxTimeExcd = _TfrapPerfIcmpPerDlciRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 15),
    _TfrapPerfIcmpPerDlciRxTimeExcd_Type()
)
tfrapPerfIcmpPerDlciRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxTimeExcd.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxTimeExcd_Type = Counter32
_TfrapPerfIcmpPerDlciTxTimeExcd_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxTimeExcd = _TfrapPerfIcmpPerDlciTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 16),
    _TfrapPerfIcmpPerDlciTxTimeExcd_Type()
)
tfrapPerfIcmpPerDlciTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxTimeExcd.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxParamProb_Type = Counter32
_TfrapPerfIcmpPerDlciRxParamProb_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxParamProb = _TfrapPerfIcmpPerDlciRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 17),
    _TfrapPerfIcmpPerDlciRxParamProb_Type()
)
tfrapPerfIcmpPerDlciRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxParamProb.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxParamProb_Type = Counter32
_TfrapPerfIcmpPerDlciTxParamProb_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxParamProb = _TfrapPerfIcmpPerDlciTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 18),
    _TfrapPerfIcmpPerDlciTxParamProb_Type()
)
tfrapPerfIcmpPerDlciTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxParamProb.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxTimestpReq_Type = Counter32
_TfrapPerfIcmpPerDlciRxTimestpReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxTimestpReq = _TfrapPerfIcmpPerDlciRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 19),
    _TfrapPerfIcmpPerDlciRxTimestpReq_Type()
)
tfrapPerfIcmpPerDlciRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxTimestpReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxTimestpReq_Type = Counter32
_TfrapPerfIcmpPerDlciTxTimestpReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxTimestpReq = _TfrapPerfIcmpPerDlciTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 20),
    _TfrapPerfIcmpPerDlciTxTimestpReq_Type()
)
tfrapPerfIcmpPerDlciTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxTimestpReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxTimestpRep_Type = Counter32
_TfrapPerfIcmpPerDlciRxTimestpRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxTimestpRep = _TfrapPerfIcmpPerDlciRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 21),
    _TfrapPerfIcmpPerDlciRxTimestpRep_Type()
)
tfrapPerfIcmpPerDlciRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxTimestpRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxTimestpRep_Type = Counter32
_TfrapPerfIcmpPerDlciTxTimestpRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxTimestpRep = _TfrapPerfIcmpPerDlciTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 22),
    _TfrapPerfIcmpPerDlciTxTimestpRep_Type()
)
tfrapPerfIcmpPerDlciTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxTimestpRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxAddrMaskReq_Type = Counter32
_TfrapPerfIcmpPerDlciRxAddrMaskReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxAddrMaskReq = _TfrapPerfIcmpPerDlciRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 23),
    _TfrapPerfIcmpPerDlciRxAddrMaskReq_Type()
)
tfrapPerfIcmpPerDlciRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxAddrMaskReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxAddrMaskReq_Type = Counter32
_TfrapPerfIcmpPerDlciTxAddrMaskReq_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxAddrMaskReq = _TfrapPerfIcmpPerDlciTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 24),
    _TfrapPerfIcmpPerDlciTxAddrMaskReq_Type()
)
tfrapPerfIcmpPerDlciTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxAddrMaskReq.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxAddrMaskRep_Type = Counter32
_TfrapPerfIcmpPerDlciRxAddrMaskRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxAddrMaskRep = _TfrapPerfIcmpPerDlciRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 25),
    _TfrapPerfIcmpPerDlciRxAddrMaskRep_Type()
)
tfrapPerfIcmpPerDlciRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxAddrMaskRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxAddrMaskRep_Type = Counter32
_TfrapPerfIcmpPerDlciTxAddrMaskRep_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxAddrMaskRep = _TfrapPerfIcmpPerDlciTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 26),
    _TfrapPerfIcmpPerDlciTxAddrMaskRep_Type()
)
tfrapPerfIcmpPerDlciTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxAddrMaskRep.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxPktTooBig_Type = Counter32
_TfrapPerfIcmpPerDlciRxPktTooBig_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxPktTooBig = _TfrapPerfIcmpPerDlciRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 27),
    _TfrapPerfIcmpPerDlciRxPktTooBig_Type()
)
tfrapPerfIcmpPerDlciRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxPktTooBig.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxPktTooBig_Type = Counter32
_TfrapPerfIcmpPerDlciTxPktTooBig_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxPktTooBig = _TfrapPerfIcmpPerDlciTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 28),
    _TfrapPerfIcmpPerDlciTxPktTooBig_Type()
)
tfrapPerfIcmpPerDlciTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxPktTooBig.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxGmQuery_Type = Counter32
_TfrapPerfIcmpPerDlciRxGmQuery_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxGmQuery = _TfrapPerfIcmpPerDlciRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 29),
    _TfrapPerfIcmpPerDlciRxGmQuery_Type()
)
tfrapPerfIcmpPerDlciRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxGmQuery.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxGmQuery_Type = Counter32
_TfrapPerfIcmpPerDlciTxGmQuery_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxGmQuery = _TfrapPerfIcmpPerDlciTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 30),
    _TfrapPerfIcmpPerDlciTxGmQuery_Type()
)
tfrapPerfIcmpPerDlciTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxGmQuery.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxGmReport_Type = Counter32
_TfrapPerfIcmpPerDlciRxGmReport_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxGmReport = _TfrapPerfIcmpPerDlciRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 31),
    _TfrapPerfIcmpPerDlciRxGmReport_Type()
)
tfrapPerfIcmpPerDlciRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxGmReport.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxGmReport_Type = Counter32
_TfrapPerfIcmpPerDlciTxGmReport_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxGmReport = _TfrapPerfIcmpPerDlciTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 32),
    _TfrapPerfIcmpPerDlciTxGmReport_Type()
)
tfrapPerfIcmpPerDlciTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxGmReport.setStatus("mandatory")
_TfrapPerfIcmpPerDlciRxGmReduct_Type = Counter32
_TfrapPerfIcmpPerDlciRxGmReduct_Object = MibTableColumn
tfrapPerfIcmpPerDlciRxGmReduct = _TfrapPerfIcmpPerDlciRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 33),
    _TfrapPerfIcmpPerDlciRxGmReduct_Type()
)
tfrapPerfIcmpPerDlciRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciRxGmReduct.setStatus("mandatory")
_TfrapPerfIcmpPerDlciTxGmReduct_Type = Counter32
_TfrapPerfIcmpPerDlciTxGmReduct_Object = MibTableColumn
tfrapPerfIcmpPerDlciTxGmReduct = _TfrapPerfIcmpPerDlciTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 5, 1, 34),
    _TfrapPerfIcmpPerDlciTxGmReduct_Type()
)
tfrapPerfIcmpPerDlciTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpPerDlciTxGmReduct.setStatus("mandatory")
_TfrapPerfIcmpTotalTable_Object = MibTable
tfrapPerfIcmpTotalTable = _TfrapPerfIcmpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6)
)
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTable.setStatus("mandatory")
_TfrapPerfIcmpTotalEntry_Object = MibTableRow
tfrapPerfIcmpTotalEntry = _TfrapPerfIcmpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1)
)
tfrapPerfIcmpTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIcmpTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalEntry.setStatus("mandatory")


class _TfrapPerfIcmpTotalInterval_Type(Integer32):
    """Custom type tfrapPerfIcmpTotalInterval based on Integer32"""
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


_TfrapPerfIcmpTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfIcmpTotalInterval_Object = MibTableColumn
tfrapPerfIcmpTotalInterval = _TfrapPerfIcmpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 1),
    _TfrapPerfIcmpTotalInterval_Type()
)
tfrapPerfIcmpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalInterval.setStatus("mandatory")
_TfrapPerfIcmpTotalRxTotal_Type = Counter32
_TfrapPerfIcmpTotalRxTotal_Object = MibTableColumn
tfrapPerfIcmpTotalRxTotal = _TfrapPerfIcmpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 3),
    _TfrapPerfIcmpTotalRxTotal_Type()
)
tfrapPerfIcmpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxTotal.setStatus("mandatory")
_TfrapPerfIcmpTotalTxTotal_Type = Counter32
_TfrapPerfIcmpTotalTxTotal_Object = MibTableColumn
tfrapPerfIcmpTotalTxTotal = _TfrapPerfIcmpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 4),
    _TfrapPerfIcmpTotalTxTotal_Type()
)
tfrapPerfIcmpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxTotal.setStatus("mandatory")
_TfrapPerfIcmpTotalRxEchoRep_Type = Counter32
_TfrapPerfIcmpTotalRxEchoRep_Object = MibTableColumn
tfrapPerfIcmpTotalRxEchoRep = _TfrapPerfIcmpTotalRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 5),
    _TfrapPerfIcmpTotalRxEchoRep_Type()
)
tfrapPerfIcmpTotalRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxEchoRep.setStatus("mandatory")
_TfrapPerfIcmpTotalTxEchoRep_Type = Counter32
_TfrapPerfIcmpTotalTxEchoRep_Object = MibTableColumn
tfrapPerfIcmpTotalTxEchoRep = _TfrapPerfIcmpTotalTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 6),
    _TfrapPerfIcmpTotalTxEchoRep_Type()
)
tfrapPerfIcmpTotalTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxEchoRep.setStatus("mandatory")
_TfrapPerfIcmpTotalRxDestUnr_Type = Counter32
_TfrapPerfIcmpTotalRxDestUnr_Object = MibTableColumn
tfrapPerfIcmpTotalRxDestUnr = _TfrapPerfIcmpTotalRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 7),
    _TfrapPerfIcmpTotalRxDestUnr_Type()
)
tfrapPerfIcmpTotalRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxDestUnr.setStatus("mandatory")
_TfrapPerfIcmpTotalTxDestUnr_Type = Counter32
_TfrapPerfIcmpTotalTxDestUnr_Object = MibTableColumn
tfrapPerfIcmpTotalTxDestUnr = _TfrapPerfIcmpTotalTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 8),
    _TfrapPerfIcmpTotalTxDestUnr_Type()
)
tfrapPerfIcmpTotalTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxDestUnr.setStatus("mandatory")
_TfrapPerfIcmpTotalRxSrcQuench_Type = Counter32
_TfrapPerfIcmpTotalRxSrcQuench_Object = MibTableColumn
tfrapPerfIcmpTotalRxSrcQuench = _TfrapPerfIcmpTotalRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 9),
    _TfrapPerfIcmpTotalRxSrcQuench_Type()
)
tfrapPerfIcmpTotalRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxSrcQuench.setStatus("mandatory")
_TfrapPerfIcmpTotalTxSrcQuench_Type = Counter32
_TfrapPerfIcmpTotalTxSrcQuench_Object = MibTableColumn
tfrapPerfIcmpTotalTxSrcQuench = _TfrapPerfIcmpTotalTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 10),
    _TfrapPerfIcmpTotalTxSrcQuench_Type()
)
tfrapPerfIcmpTotalTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxSrcQuench.setStatus("mandatory")
_TfrapPerfIcmpTotalRxRedirect_Type = Counter32
_TfrapPerfIcmpTotalRxRedirect_Object = MibTableColumn
tfrapPerfIcmpTotalRxRedirect = _TfrapPerfIcmpTotalRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 11),
    _TfrapPerfIcmpTotalRxRedirect_Type()
)
tfrapPerfIcmpTotalRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxRedirect.setStatus("mandatory")
_TfrapPerfIcmpTotalTxRedirect_Type = Counter32
_TfrapPerfIcmpTotalTxRedirect_Object = MibTableColumn
tfrapPerfIcmpTotalTxRedirect = _TfrapPerfIcmpTotalTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 12),
    _TfrapPerfIcmpTotalTxRedirect_Type()
)
tfrapPerfIcmpTotalTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxRedirect.setStatus("mandatory")
_TfrapPerfIcmpTotalRxEchoReq_Type = Counter32
_TfrapPerfIcmpTotalRxEchoReq_Object = MibTableColumn
tfrapPerfIcmpTotalRxEchoReq = _TfrapPerfIcmpTotalRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 13),
    _TfrapPerfIcmpTotalRxEchoReq_Type()
)
tfrapPerfIcmpTotalRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxEchoReq.setStatus("mandatory")
_TfrapPerfIcmpTotalTxEchoReq_Type = Counter32
_TfrapPerfIcmpTotalTxEchoReq_Object = MibTableColumn
tfrapPerfIcmpTotalTxEchoReq = _TfrapPerfIcmpTotalTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 14),
    _TfrapPerfIcmpTotalTxEchoReq_Type()
)
tfrapPerfIcmpTotalTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxEchoReq.setStatus("mandatory")
_TfrapPerfIcmpTotalRxTimeExcd_Type = Counter32
_TfrapPerfIcmpTotalRxTimeExcd_Object = MibTableColumn
tfrapPerfIcmpTotalRxTimeExcd = _TfrapPerfIcmpTotalRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 15),
    _TfrapPerfIcmpTotalRxTimeExcd_Type()
)
tfrapPerfIcmpTotalRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxTimeExcd.setStatus("mandatory")
_TfrapPerfIcmpTotalTxTimeExcd_Type = Counter32
_TfrapPerfIcmpTotalTxTimeExcd_Object = MibTableColumn
tfrapPerfIcmpTotalTxTimeExcd = _TfrapPerfIcmpTotalTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 16),
    _TfrapPerfIcmpTotalTxTimeExcd_Type()
)
tfrapPerfIcmpTotalTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxTimeExcd.setStatus("mandatory")
_TfrapPerfIcmpTotalRxParamProb_Type = Counter32
_TfrapPerfIcmpTotalRxParamProb_Object = MibTableColumn
tfrapPerfIcmpTotalRxParamProb = _TfrapPerfIcmpTotalRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 17),
    _TfrapPerfIcmpTotalRxParamProb_Type()
)
tfrapPerfIcmpTotalRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxParamProb.setStatus("mandatory")
_TfrapPerfIcmpTotalTxParamProb_Type = Counter32
_TfrapPerfIcmpTotalTxParamProb_Object = MibTableColumn
tfrapPerfIcmpTotalTxParamProb = _TfrapPerfIcmpTotalTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 18),
    _TfrapPerfIcmpTotalTxParamProb_Type()
)
tfrapPerfIcmpTotalTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxParamProb.setStatus("mandatory")
_TfrapPerfIcmpTotalRxTimestpReq_Type = Counter32
_TfrapPerfIcmpTotalRxTimestpReq_Object = MibTableColumn
tfrapPerfIcmpTotalRxTimestpReq = _TfrapPerfIcmpTotalRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 19),
    _TfrapPerfIcmpTotalRxTimestpReq_Type()
)
tfrapPerfIcmpTotalRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxTimestpReq.setStatus("mandatory")
_TfrapPerfIcmpTotalTxTimestpReq_Type = Counter32
_TfrapPerfIcmpTotalTxTimestpReq_Object = MibTableColumn
tfrapPerfIcmpTotalTxTimestpReq = _TfrapPerfIcmpTotalTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 20),
    _TfrapPerfIcmpTotalTxTimestpReq_Type()
)
tfrapPerfIcmpTotalTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxTimestpReq.setStatus("mandatory")
_TfrapPerfIcmpTotalRxTimestpRep_Type = Counter32
_TfrapPerfIcmpTotalRxTimestpRep_Object = MibTableColumn
tfrapPerfIcmpTotalRxTimestpRep = _TfrapPerfIcmpTotalRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 21),
    _TfrapPerfIcmpTotalRxTimestpRep_Type()
)
tfrapPerfIcmpTotalRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxTimestpRep.setStatus("mandatory")
_TfrapPerfIcmpTotalTxTimestpRep_Type = Counter32
_TfrapPerfIcmpTotalTxTimestpRep_Object = MibTableColumn
tfrapPerfIcmpTotalTxTimestpRep = _TfrapPerfIcmpTotalTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 22),
    _TfrapPerfIcmpTotalTxTimestpRep_Type()
)
tfrapPerfIcmpTotalTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxTimestpRep.setStatus("mandatory")
_TfrapPerfIcmpTotalRxAddrMaskReq_Type = Counter32
_TfrapPerfIcmpTotalRxAddrMaskReq_Object = MibTableColumn
tfrapPerfIcmpTotalRxAddrMaskReq = _TfrapPerfIcmpTotalRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 23),
    _TfrapPerfIcmpTotalRxAddrMaskReq_Type()
)
tfrapPerfIcmpTotalRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxAddrMaskReq.setStatus("mandatory")
_TfrapPerfIcmpTotalTxAddrMaskReq_Type = Counter32
_TfrapPerfIcmpTotalTxAddrMaskReq_Object = MibTableColumn
tfrapPerfIcmpTotalTxAddrMaskReq = _TfrapPerfIcmpTotalTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 24),
    _TfrapPerfIcmpTotalTxAddrMaskReq_Type()
)
tfrapPerfIcmpTotalTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxAddrMaskReq.setStatus("mandatory")
_TfrapPerfIcmpTotalRxAddrMaskRep_Type = Counter32
_TfrapPerfIcmpTotalRxAddrMaskRep_Object = MibTableColumn
tfrapPerfIcmpTotalRxAddrMaskRep = _TfrapPerfIcmpTotalRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 25),
    _TfrapPerfIcmpTotalRxAddrMaskRep_Type()
)
tfrapPerfIcmpTotalRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxAddrMaskRep.setStatus("mandatory")
_TfrapPerfIcmpTotalTxAddrMaskRep_Type = Counter32
_TfrapPerfIcmpTotalTxAddrMaskRep_Object = MibTableColumn
tfrapPerfIcmpTotalTxAddrMaskRep = _TfrapPerfIcmpTotalTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 26),
    _TfrapPerfIcmpTotalTxAddrMaskRep_Type()
)
tfrapPerfIcmpTotalTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxAddrMaskRep.setStatus("mandatory")
_TfrapPerfIcmpTotalRxPktTooBig_Type = Counter32
_TfrapPerfIcmpTotalRxPktTooBig_Object = MibTableColumn
tfrapPerfIcmpTotalRxPktTooBig = _TfrapPerfIcmpTotalRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 27),
    _TfrapPerfIcmpTotalRxPktTooBig_Type()
)
tfrapPerfIcmpTotalRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxPktTooBig.setStatus("mandatory")
_TfrapPerfIcmpTotalTxPktTooBig_Type = Counter32
_TfrapPerfIcmpTotalTxPktTooBig_Object = MibTableColumn
tfrapPerfIcmpTotalTxPktTooBig = _TfrapPerfIcmpTotalTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 28),
    _TfrapPerfIcmpTotalTxPktTooBig_Type()
)
tfrapPerfIcmpTotalTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxPktTooBig.setStatus("mandatory")
_TfrapPerfIcmpTotalRxGmQuery_Type = Counter32
_TfrapPerfIcmpTotalRxGmQuery_Object = MibTableColumn
tfrapPerfIcmpTotalRxGmQuery = _TfrapPerfIcmpTotalRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 29),
    _TfrapPerfIcmpTotalRxGmQuery_Type()
)
tfrapPerfIcmpTotalRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxGmQuery.setStatus("mandatory")
_TfrapPerfIcmpTotalTxGmQuery_Type = Counter32
_TfrapPerfIcmpTotalTxGmQuery_Object = MibTableColumn
tfrapPerfIcmpTotalTxGmQuery = _TfrapPerfIcmpTotalTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 30),
    _TfrapPerfIcmpTotalTxGmQuery_Type()
)
tfrapPerfIcmpTotalTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxGmQuery.setStatus("mandatory")
_TfrapPerfIcmpTotalRxGmReport_Type = Counter32
_TfrapPerfIcmpTotalRxGmReport_Object = MibTableColumn
tfrapPerfIcmpTotalRxGmReport = _TfrapPerfIcmpTotalRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 31),
    _TfrapPerfIcmpTotalRxGmReport_Type()
)
tfrapPerfIcmpTotalRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxGmReport.setStatus("mandatory")
_TfrapPerfIcmpTotalTxGmReport_Type = Counter32
_TfrapPerfIcmpTotalTxGmReport_Object = MibTableColumn
tfrapPerfIcmpTotalTxGmReport = _TfrapPerfIcmpTotalTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 32),
    _TfrapPerfIcmpTotalTxGmReport_Type()
)
tfrapPerfIcmpTotalTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxGmReport.setStatus("mandatory")
_TfrapPerfIcmpTotalRxGmReduct_Type = Counter32
_TfrapPerfIcmpTotalRxGmReduct_Object = MibTableColumn
tfrapPerfIcmpTotalRxGmReduct = _TfrapPerfIcmpTotalRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 33),
    _TfrapPerfIcmpTotalRxGmReduct_Type()
)
tfrapPerfIcmpTotalRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalRxGmReduct.setStatus("mandatory")
_TfrapPerfIcmpTotalTxGmReduct_Type = Counter32
_TfrapPerfIcmpTotalTxGmReduct_Object = MibTableColumn
tfrapPerfIcmpTotalTxGmReduct = _TfrapPerfIcmpTotalTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 6, 1, 34),
    _TfrapPerfIcmpTotalTxGmReduct_Type()
)
tfrapPerfIcmpTotalTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIcmpTotalTxGmReduct.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTable_Object = MibTable
tfrapPerfApplicationPerDlciTable = _TfrapPerfApplicationPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7)
)
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTable.setStatus("mandatory")
_TfrapPerfApplicationPerDlciEntry_Object = MibTableRow
tfrapPerfApplicationPerDlciEntry = _TfrapPerfApplicationPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1)
)
tfrapPerfApplicationPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfApplicationPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfApplicationPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciEntry.setStatus("mandatory")


class _TfrapPerfApplicationPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfApplicationPerDlciInterval based on Integer32"""
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


_TfrapPerfApplicationPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfApplicationPerDlciInterval_Object = MibTableColumn
tfrapPerfApplicationPerDlciInterval = _TfrapPerfApplicationPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 1),
    _TfrapPerfApplicationPerDlciInterval_Type()
)
tfrapPerfApplicationPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciInterval.setStatus("mandatory")
_TfrapPerfApplicationPerDlciValue_Type = Integer32
_TfrapPerfApplicationPerDlciValue_Object = MibTableColumn
tfrapPerfApplicationPerDlciValue = _TfrapPerfApplicationPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 2),
    _TfrapPerfApplicationPerDlciValue_Type()
)
tfrapPerfApplicationPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciValue.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxSnmp_Type = Counter32
_TfrapPerfApplicationPerDlciRxSnmp_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxSnmp = _TfrapPerfApplicationPerDlciRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 3),
    _TfrapPerfApplicationPerDlciRxSnmp_Type()
)
tfrapPerfApplicationPerDlciRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxSnmp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxSnmp_Type = Counter32
_TfrapPerfApplicationPerDlciTxSnmp_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxSnmp = _TfrapPerfApplicationPerDlciTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 4),
    _TfrapPerfApplicationPerDlciTxSnmp_Type()
)
tfrapPerfApplicationPerDlciTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxSnmp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxSnmpTrap_Type = Counter32
_TfrapPerfApplicationPerDlciRxSnmpTrap_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxSnmpTrap = _TfrapPerfApplicationPerDlciRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 5),
    _TfrapPerfApplicationPerDlciRxSnmpTrap_Type()
)
tfrapPerfApplicationPerDlciRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxSnmpTrap.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxSnmpTrap_Type = Counter32
_TfrapPerfApplicationPerDlciTxSnmpTrap_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxSnmpTrap = _TfrapPerfApplicationPerDlciTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 6),
    _TfrapPerfApplicationPerDlciTxSnmpTrap_Type()
)
tfrapPerfApplicationPerDlciTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxSnmpTrap.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxHttp_Type = Counter32
_TfrapPerfApplicationPerDlciRxHttp_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxHttp = _TfrapPerfApplicationPerDlciRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 7),
    _TfrapPerfApplicationPerDlciRxHttp_Type()
)
tfrapPerfApplicationPerDlciRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxHttp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxHttp_Type = Counter32
_TfrapPerfApplicationPerDlciTxHttp_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxHttp = _TfrapPerfApplicationPerDlciTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 8),
    _TfrapPerfApplicationPerDlciTxHttp_Type()
)
tfrapPerfApplicationPerDlciTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxHttp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxTelnet_Type = Counter32
_TfrapPerfApplicationPerDlciRxTelnet_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxTelnet = _TfrapPerfApplicationPerDlciRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 9),
    _TfrapPerfApplicationPerDlciRxTelnet_Type()
)
tfrapPerfApplicationPerDlciRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxTelnet.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxTelnet_Type = Counter32
_TfrapPerfApplicationPerDlciTxTelnet_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxTelnet = _TfrapPerfApplicationPerDlciTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 10),
    _TfrapPerfApplicationPerDlciTxTelnet_Type()
)
tfrapPerfApplicationPerDlciTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxTelnet.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxSmtp_Type = Counter32
_TfrapPerfApplicationPerDlciRxSmtp_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxSmtp = _TfrapPerfApplicationPerDlciRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 11),
    _TfrapPerfApplicationPerDlciRxSmtp_Type()
)
tfrapPerfApplicationPerDlciRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxSmtp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxSmtp_Type = Counter32
_TfrapPerfApplicationPerDlciTxSmtp_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxSmtp = _TfrapPerfApplicationPerDlciTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 12),
    _TfrapPerfApplicationPerDlciTxSmtp_Type()
)
tfrapPerfApplicationPerDlciTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxSmtp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxFtp_Type = Counter32
_TfrapPerfApplicationPerDlciRxFtp_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxFtp = _TfrapPerfApplicationPerDlciRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 13),
    _TfrapPerfApplicationPerDlciRxFtp_Type()
)
tfrapPerfApplicationPerDlciRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxFtp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxFtp_Type = Counter32
_TfrapPerfApplicationPerDlciTxFtp_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxFtp = _TfrapPerfApplicationPerDlciTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 14),
    _TfrapPerfApplicationPerDlciTxFtp_Type()
)
tfrapPerfApplicationPerDlciTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxFtp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxTftp_Type = Counter32
_TfrapPerfApplicationPerDlciRxTftp_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxTftp = _TfrapPerfApplicationPerDlciRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 15),
    _TfrapPerfApplicationPerDlciRxTftp_Type()
)
tfrapPerfApplicationPerDlciRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxTftp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxTftp_Type = Counter32
_TfrapPerfApplicationPerDlciTxTftp_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxTftp = _TfrapPerfApplicationPerDlciTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 16),
    _TfrapPerfApplicationPerDlciTxTftp_Type()
)
tfrapPerfApplicationPerDlciTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxTftp.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxCustom1_Type = Counter32
_TfrapPerfApplicationPerDlciRxCustom1_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxCustom1 = _TfrapPerfApplicationPerDlciRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 17),
    _TfrapPerfApplicationPerDlciRxCustom1_Type()
)
tfrapPerfApplicationPerDlciRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxCustom1.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxCustom1_Type = Counter32
_TfrapPerfApplicationPerDlciTxCustom1_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxCustom1 = _TfrapPerfApplicationPerDlciTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 18),
    _TfrapPerfApplicationPerDlciTxCustom1_Type()
)
tfrapPerfApplicationPerDlciTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxCustom1.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxCustom2_Type = Counter32
_TfrapPerfApplicationPerDlciRxCustom2_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxCustom2 = _TfrapPerfApplicationPerDlciRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 19),
    _TfrapPerfApplicationPerDlciRxCustom2_Type()
)
tfrapPerfApplicationPerDlciRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxCustom2.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxCustom2_Type = Counter32
_TfrapPerfApplicationPerDlciTxCustom2_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxCustom2 = _TfrapPerfApplicationPerDlciTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 20),
    _TfrapPerfApplicationPerDlciTxCustom2_Type()
)
tfrapPerfApplicationPerDlciTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxCustom2.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxCustom3_Type = Counter32
_TfrapPerfApplicationPerDlciRxCustom3_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxCustom3 = _TfrapPerfApplicationPerDlciRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 21),
    _TfrapPerfApplicationPerDlciRxCustom3_Type()
)
tfrapPerfApplicationPerDlciRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxCustom3.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxCustom3_Type = Counter32
_TfrapPerfApplicationPerDlciTxCustom3_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxCustom3 = _TfrapPerfApplicationPerDlciTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 22),
    _TfrapPerfApplicationPerDlciTxCustom3_Type()
)
tfrapPerfApplicationPerDlciTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxCustom3.setStatus("mandatory")
_TfrapPerfApplicationPerDlciRxCustom4_Type = Counter32
_TfrapPerfApplicationPerDlciRxCustom4_Object = MibTableColumn
tfrapPerfApplicationPerDlciRxCustom4 = _TfrapPerfApplicationPerDlciRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 23),
    _TfrapPerfApplicationPerDlciRxCustom4_Type()
)
tfrapPerfApplicationPerDlciRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciRxCustom4.setStatus("mandatory")
_TfrapPerfApplicationPerDlciTxCustom4_Type = Counter32
_TfrapPerfApplicationPerDlciTxCustom4_Object = MibTableColumn
tfrapPerfApplicationPerDlciTxCustom4 = _TfrapPerfApplicationPerDlciTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 7, 1, 24),
    _TfrapPerfApplicationPerDlciTxCustom4_Type()
)
tfrapPerfApplicationPerDlciTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationPerDlciTxCustom4.setStatus("mandatory")
_TfrapPerfApplicationTotalTable_Object = MibTable
tfrapPerfApplicationTotalTable = _TfrapPerfApplicationTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8)
)
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTable.setStatus("mandatory")
_TfrapPerfApplicationTotalEntry_Object = MibTableRow
tfrapPerfApplicationTotalEntry = _TfrapPerfApplicationTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1)
)
tfrapPerfApplicationTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfApplicationTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalEntry.setStatus("mandatory")


class _TfrapPerfApplicationTotalInterval_Type(Integer32):
    """Custom type tfrapPerfApplicationTotalInterval based on Integer32"""
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


_TfrapPerfApplicationTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfApplicationTotalInterval_Object = MibTableColumn
tfrapPerfApplicationTotalInterval = _TfrapPerfApplicationTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 1),
    _TfrapPerfApplicationTotalInterval_Type()
)
tfrapPerfApplicationTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalInterval.setStatus("mandatory")
_TfrapPerfApplicationTotalRxSnmp_Type = Counter32
_TfrapPerfApplicationTotalRxSnmp_Object = MibTableColumn
tfrapPerfApplicationTotalRxSnmp = _TfrapPerfApplicationTotalRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 3),
    _TfrapPerfApplicationTotalRxSnmp_Type()
)
tfrapPerfApplicationTotalRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxSnmp.setStatus("mandatory")
_TfrapPerfApplicationTotalTxSnmp_Type = Counter32
_TfrapPerfApplicationTotalTxSnmp_Object = MibTableColumn
tfrapPerfApplicationTotalTxSnmp = _TfrapPerfApplicationTotalTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 4),
    _TfrapPerfApplicationTotalTxSnmp_Type()
)
tfrapPerfApplicationTotalTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxSnmp.setStatus("mandatory")
_TfrapPerfApplicationTotalRxSnmpTrap_Type = Counter32
_TfrapPerfApplicationTotalRxSnmpTrap_Object = MibTableColumn
tfrapPerfApplicationTotalRxSnmpTrap = _TfrapPerfApplicationTotalRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 5),
    _TfrapPerfApplicationTotalRxSnmpTrap_Type()
)
tfrapPerfApplicationTotalRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxSnmpTrap.setStatus("mandatory")
_TfrapPerfApplicationTotalTxSnmpTrap_Type = Counter32
_TfrapPerfApplicationTotalTxSnmpTrap_Object = MibTableColumn
tfrapPerfApplicationTotalTxSnmpTrap = _TfrapPerfApplicationTotalTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 6),
    _TfrapPerfApplicationTotalTxSnmpTrap_Type()
)
tfrapPerfApplicationTotalTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxSnmpTrap.setStatus("mandatory")
_TfrapPerfApplicationTotalRxHttp_Type = Counter32
_TfrapPerfApplicationTotalRxHttp_Object = MibTableColumn
tfrapPerfApplicationTotalRxHttp = _TfrapPerfApplicationTotalRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 7),
    _TfrapPerfApplicationTotalRxHttp_Type()
)
tfrapPerfApplicationTotalRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxHttp.setStatus("mandatory")
_TfrapPerfApplicationTotalTxHttp_Type = Counter32
_TfrapPerfApplicationTotalTxHttp_Object = MibTableColumn
tfrapPerfApplicationTotalTxHttp = _TfrapPerfApplicationTotalTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 8),
    _TfrapPerfApplicationTotalTxHttp_Type()
)
tfrapPerfApplicationTotalTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxHttp.setStatus("mandatory")
_TfrapPerfApplicationTotalRxTelnet_Type = Counter32
_TfrapPerfApplicationTotalRxTelnet_Object = MibTableColumn
tfrapPerfApplicationTotalRxTelnet = _TfrapPerfApplicationTotalRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 9),
    _TfrapPerfApplicationTotalRxTelnet_Type()
)
tfrapPerfApplicationTotalRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxTelnet.setStatus("mandatory")
_TfrapPerfApplicationTotalTxTelnet_Type = Counter32
_TfrapPerfApplicationTotalTxTelnet_Object = MibTableColumn
tfrapPerfApplicationTotalTxTelnet = _TfrapPerfApplicationTotalTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 10),
    _TfrapPerfApplicationTotalTxTelnet_Type()
)
tfrapPerfApplicationTotalTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxTelnet.setStatus("mandatory")
_TfrapPerfApplicationTotalRxSmtp_Type = Counter32
_TfrapPerfApplicationTotalRxSmtp_Object = MibTableColumn
tfrapPerfApplicationTotalRxSmtp = _TfrapPerfApplicationTotalRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 11),
    _TfrapPerfApplicationTotalRxSmtp_Type()
)
tfrapPerfApplicationTotalRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxSmtp.setStatus("mandatory")
_TfrapPerfApplicationTotalTxSmtp_Type = Counter32
_TfrapPerfApplicationTotalTxSmtp_Object = MibTableColumn
tfrapPerfApplicationTotalTxSmtp = _TfrapPerfApplicationTotalTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 12),
    _TfrapPerfApplicationTotalTxSmtp_Type()
)
tfrapPerfApplicationTotalTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxSmtp.setStatus("mandatory")
_TfrapPerfApplicationTotalRxFtp_Type = Counter32
_TfrapPerfApplicationTotalRxFtp_Object = MibTableColumn
tfrapPerfApplicationTotalRxFtp = _TfrapPerfApplicationTotalRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 13),
    _TfrapPerfApplicationTotalRxFtp_Type()
)
tfrapPerfApplicationTotalRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxFtp.setStatus("mandatory")
_TfrapPerfApplicationTotalTxFtp_Type = Counter32
_TfrapPerfApplicationTotalTxFtp_Object = MibTableColumn
tfrapPerfApplicationTotalTxFtp = _TfrapPerfApplicationTotalTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 14),
    _TfrapPerfApplicationTotalTxFtp_Type()
)
tfrapPerfApplicationTotalTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxFtp.setStatus("mandatory")
_TfrapPerfApplicationTotalRxTftp_Type = Counter32
_TfrapPerfApplicationTotalRxTftp_Object = MibTableColumn
tfrapPerfApplicationTotalRxTftp = _TfrapPerfApplicationTotalRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 15),
    _TfrapPerfApplicationTotalRxTftp_Type()
)
tfrapPerfApplicationTotalRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxTftp.setStatus("mandatory")
_TfrapPerfApplicationTotalTxTftp_Type = Counter32
_TfrapPerfApplicationTotalTxTftp_Object = MibTableColumn
tfrapPerfApplicationTotalTxTftp = _TfrapPerfApplicationTotalTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 16),
    _TfrapPerfApplicationTotalTxTftp_Type()
)
tfrapPerfApplicationTotalTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxTftp.setStatus("mandatory")
_TfrapPerfApplicationTotalRxCustom1_Type = Counter32
_TfrapPerfApplicationTotalRxCustom1_Object = MibTableColumn
tfrapPerfApplicationTotalRxCustom1 = _TfrapPerfApplicationTotalRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 17),
    _TfrapPerfApplicationTotalRxCustom1_Type()
)
tfrapPerfApplicationTotalRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxCustom1.setStatus("mandatory")
_TfrapPerfApplicationTotalTxCustom1_Type = Counter32
_TfrapPerfApplicationTotalTxCustom1_Object = MibTableColumn
tfrapPerfApplicationTotalTxCustom1 = _TfrapPerfApplicationTotalTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 18),
    _TfrapPerfApplicationTotalTxCustom1_Type()
)
tfrapPerfApplicationTotalTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxCustom1.setStatus("mandatory")
_TfrapPerfApplicationTotalRxCustom2_Type = Counter32
_TfrapPerfApplicationTotalRxCustom2_Object = MibTableColumn
tfrapPerfApplicationTotalRxCustom2 = _TfrapPerfApplicationTotalRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 19),
    _TfrapPerfApplicationTotalRxCustom2_Type()
)
tfrapPerfApplicationTotalRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxCustom2.setStatus("mandatory")
_TfrapPerfApplicationTotalTxCustom2_Type = Counter32
_TfrapPerfApplicationTotalTxCustom2_Object = MibTableColumn
tfrapPerfApplicationTotalTxCustom2 = _TfrapPerfApplicationTotalTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 20),
    _TfrapPerfApplicationTotalTxCustom2_Type()
)
tfrapPerfApplicationTotalTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxCustom2.setStatus("mandatory")
_TfrapPerfApplicationTotalRxCustom3_Type = Counter32
_TfrapPerfApplicationTotalRxCustom3_Object = MibTableColumn
tfrapPerfApplicationTotalRxCustom3 = _TfrapPerfApplicationTotalRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 21),
    _TfrapPerfApplicationTotalRxCustom3_Type()
)
tfrapPerfApplicationTotalRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxCustom3.setStatus("mandatory")
_TfrapPerfApplicationTotalTxCustom3_Type = Counter32
_TfrapPerfApplicationTotalTxCustom3_Object = MibTableColumn
tfrapPerfApplicationTotalTxCustom3 = _TfrapPerfApplicationTotalTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 22),
    _TfrapPerfApplicationTotalTxCustom3_Type()
)
tfrapPerfApplicationTotalTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxCustom3.setStatus("mandatory")
_TfrapPerfApplicationTotalRxCustom4_Type = Counter32
_TfrapPerfApplicationTotalRxCustom4_Object = MibTableColumn
tfrapPerfApplicationTotalRxCustom4 = _TfrapPerfApplicationTotalRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 23),
    _TfrapPerfApplicationTotalRxCustom4_Type()
)
tfrapPerfApplicationTotalRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalRxCustom4.setStatus("mandatory")
_TfrapPerfApplicationTotalTxCustom4_Type = Counter32
_TfrapPerfApplicationTotalTxCustom4_Object = MibTableColumn
tfrapPerfApplicationTotalTxCustom4 = _TfrapPerfApplicationTotalTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 8, 1, 24),
    _TfrapPerfApplicationTotalTxCustom4_Type()
)
tfrapPerfApplicationTotalTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfApplicationTotalTxCustom4.setStatus("mandatory")
_TfrapPerfRoutingPerDlciTable_Object = MibTable
tfrapPerfRoutingPerDlciTable = _TfrapPerfRoutingPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9)
)
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciTable.setStatus("mandatory")
_TfrapPerfRoutingPerDlciEntry_Object = MibTableRow
tfrapPerfRoutingPerDlciEntry = _TfrapPerfRoutingPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1)
)
tfrapPerfRoutingPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfRoutingPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfRoutingPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciEntry.setStatus("mandatory")


class _TfrapPerfRoutingPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfRoutingPerDlciInterval based on Integer32"""
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


_TfrapPerfRoutingPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfRoutingPerDlciInterval_Object = MibTableColumn
tfrapPerfRoutingPerDlciInterval = _TfrapPerfRoutingPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 1),
    _TfrapPerfRoutingPerDlciInterval_Type()
)
tfrapPerfRoutingPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciInterval.setStatus("mandatory")
_TfrapPerfRoutingPerDlciValue_Type = Integer32
_TfrapPerfRoutingPerDlciValue_Object = MibTableColumn
tfrapPerfRoutingPerDlciValue = _TfrapPerfRoutingPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 2),
    _TfrapPerfRoutingPerDlciValue_Type()
)
tfrapPerfRoutingPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciValue.setStatus("mandatory")
_TfrapPerfRoutingPerDlciRxOspf_Type = Counter32
_TfrapPerfRoutingPerDlciRxOspf_Object = MibTableColumn
tfrapPerfRoutingPerDlciRxOspf = _TfrapPerfRoutingPerDlciRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 3),
    _TfrapPerfRoutingPerDlciRxOspf_Type()
)
tfrapPerfRoutingPerDlciRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciRxOspf.setStatus("mandatory")
_TfrapPerfRoutingPerDlciTxOspf_Type = Counter32
_TfrapPerfRoutingPerDlciTxOspf_Object = MibTableColumn
tfrapPerfRoutingPerDlciTxOspf = _TfrapPerfRoutingPerDlciTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 4),
    _TfrapPerfRoutingPerDlciTxOspf_Type()
)
tfrapPerfRoutingPerDlciTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciTxOspf.setStatus("mandatory")
_TfrapPerfRoutingPerDlciRxRip_Type = Counter32
_TfrapPerfRoutingPerDlciRxRip_Object = MibTableColumn
tfrapPerfRoutingPerDlciRxRip = _TfrapPerfRoutingPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 5),
    _TfrapPerfRoutingPerDlciRxRip_Type()
)
tfrapPerfRoutingPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciRxRip.setStatus("mandatory")
_TfrapPerfRoutingPerDlciTxRip_Type = Counter32
_TfrapPerfRoutingPerDlciTxRip_Object = MibTableColumn
tfrapPerfRoutingPerDlciTxRip = _TfrapPerfRoutingPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 6),
    _TfrapPerfRoutingPerDlciTxRip_Type()
)
tfrapPerfRoutingPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciTxRip.setStatus("mandatory")
_TfrapPerfRoutingPerDlciRxNetbios_Type = Counter32
_TfrapPerfRoutingPerDlciRxNetbios_Object = MibTableColumn
tfrapPerfRoutingPerDlciRxNetbios = _TfrapPerfRoutingPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 7),
    _TfrapPerfRoutingPerDlciRxNetbios_Type()
)
tfrapPerfRoutingPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciRxNetbios.setStatus("mandatory")
_TfrapPerfRoutingPerDlciTxNetbios_Type = Counter32
_TfrapPerfRoutingPerDlciTxNetbios_Object = MibTableColumn
tfrapPerfRoutingPerDlciTxNetbios = _TfrapPerfRoutingPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 9, 1, 8),
    _TfrapPerfRoutingPerDlciTxNetbios_Type()
)
tfrapPerfRoutingPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingPerDlciTxNetbios.setStatus("mandatory")
_TfrapPerfRoutingTotalTable_Object = MibTable
tfrapPerfRoutingTotalTable = _TfrapPerfRoutingTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10)
)
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalTable.setStatus("mandatory")
_TfrapPerfRoutingTotalEntry_Object = MibTableRow
tfrapPerfRoutingTotalEntry = _TfrapPerfRoutingTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1)
)
tfrapPerfRoutingTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfRoutingTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalEntry.setStatus("mandatory")


class _TfrapPerfRoutingTotalInterval_Type(Integer32):
    """Custom type tfrapPerfRoutingTotalInterval based on Integer32"""
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


_TfrapPerfRoutingTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfRoutingTotalInterval_Object = MibTableColumn
tfrapPerfRoutingTotalInterval = _TfrapPerfRoutingTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 1),
    _TfrapPerfRoutingTotalInterval_Type()
)
tfrapPerfRoutingTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalInterval.setStatus("mandatory")
_TfrapPerfRoutingTotalRxOspf_Type = Counter32
_TfrapPerfRoutingTotalRxOspf_Object = MibTableColumn
tfrapPerfRoutingTotalRxOspf = _TfrapPerfRoutingTotalRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 3),
    _TfrapPerfRoutingTotalRxOspf_Type()
)
tfrapPerfRoutingTotalRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalRxOspf.setStatus("mandatory")
_TfrapPerfRoutingTotalTxOspf_Type = Counter32
_TfrapPerfRoutingTotalTxOspf_Object = MibTableColumn
tfrapPerfRoutingTotalTxOspf = _TfrapPerfRoutingTotalTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 4),
    _TfrapPerfRoutingTotalTxOspf_Type()
)
tfrapPerfRoutingTotalTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalTxOspf.setStatus("mandatory")
_TfrapPerfRoutingTotalRxRip_Type = Counter32
_TfrapPerfRoutingTotalRxRip_Object = MibTableColumn
tfrapPerfRoutingTotalRxRip = _TfrapPerfRoutingTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 5),
    _TfrapPerfRoutingTotalRxRip_Type()
)
tfrapPerfRoutingTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalRxRip.setStatus("mandatory")
_TfrapPerfRoutingTotalTxRip_Type = Counter32
_TfrapPerfRoutingTotalTxRip_Object = MibTableColumn
tfrapPerfRoutingTotalTxRip = _TfrapPerfRoutingTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 6),
    _TfrapPerfRoutingTotalTxRip_Type()
)
tfrapPerfRoutingTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalTxRip.setStatus("mandatory")
_TfrapPerfRoutingTotalRxNetbios_Type = Counter32
_TfrapPerfRoutingTotalRxNetbios_Object = MibTableColumn
tfrapPerfRoutingTotalRxNetbios = _TfrapPerfRoutingTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 7),
    _TfrapPerfRoutingTotalRxNetbios_Type()
)
tfrapPerfRoutingTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalRxNetbios.setStatus("mandatory")
_TfrapPerfRoutingTotalTxNetbios_Type = Counter32
_TfrapPerfRoutingTotalTxNetbios_Object = MibTableColumn
tfrapPerfRoutingTotalTxNetbios = _TfrapPerfRoutingTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 10, 1, 8),
    _TfrapPerfRoutingTotalTxNetbios_Type()
)
tfrapPerfRoutingTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfRoutingTotalTxNetbios.setStatus("mandatory")
_TfrapPerfIpxPerDlciTable_Object = MibTable
tfrapPerfIpxPerDlciTable = _TfrapPerfIpxPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11)
)
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTable.setStatus("mandatory")
_TfrapPerfIpxPerDlciEntry_Object = MibTableRow
tfrapPerfIpxPerDlciEntry = _TfrapPerfIpxPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1)
)
tfrapPerfIpxPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIpxPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfIpxPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciEntry.setStatus("mandatory")


class _TfrapPerfIpxPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfIpxPerDlciInterval based on Integer32"""
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


_TfrapPerfIpxPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfIpxPerDlciInterval_Object = MibTableColumn
tfrapPerfIpxPerDlciInterval = _TfrapPerfIpxPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 1),
    _TfrapPerfIpxPerDlciInterval_Type()
)
tfrapPerfIpxPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciInterval.setStatus("mandatory")
_TfrapPerfIpxPerDlciValue_Type = Integer32
_TfrapPerfIpxPerDlciValue_Object = MibTableColumn
tfrapPerfIpxPerDlciValue = _TfrapPerfIpxPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 2),
    _TfrapPerfIpxPerDlciValue_Type()
)
tfrapPerfIpxPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciValue.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxTotal_Type = Counter32
_TfrapPerfIpxPerDlciRxTotal_Object = MibTableColumn
tfrapPerfIpxPerDlciRxTotal = _TfrapPerfIpxPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 3),
    _TfrapPerfIpxPerDlciRxTotal_Type()
)
tfrapPerfIpxPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxTotal_Type = Counter32
_TfrapPerfIpxPerDlciTxTotal_Object = MibTableColumn
tfrapPerfIpxPerDlciTxTotal = _TfrapPerfIpxPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 4),
    _TfrapPerfIpxPerDlciTxTotal_Type()
)
tfrapPerfIpxPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxSpx_Type = Counter32
_TfrapPerfIpxPerDlciRxSpx_Object = MibTableColumn
tfrapPerfIpxPerDlciRxSpx = _TfrapPerfIpxPerDlciRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 5),
    _TfrapPerfIpxPerDlciRxSpx_Type()
)
tfrapPerfIpxPerDlciRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxSpx.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxSpx_Type = Counter32
_TfrapPerfIpxPerDlciTxSpx_Object = MibTableColumn
tfrapPerfIpxPerDlciTxSpx = _TfrapPerfIpxPerDlciTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 6),
    _TfrapPerfIpxPerDlciTxSpx_Type()
)
tfrapPerfIpxPerDlciTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxSpx.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxNcp_Type = Counter32
_TfrapPerfIpxPerDlciRxNcp_Object = MibTableColumn
tfrapPerfIpxPerDlciRxNcp = _TfrapPerfIpxPerDlciRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 7),
    _TfrapPerfIpxPerDlciRxNcp_Type()
)
tfrapPerfIpxPerDlciRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxNcp.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxNcp_Type = Counter32
_TfrapPerfIpxPerDlciTxNcp_Object = MibTableColumn
tfrapPerfIpxPerDlciTxNcp = _TfrapPerfIpxPerDlciTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 8),
    _TfrapPerfIpxPerDlciTxNcp_Type()
)
tfrapPerfIpxPerDlciTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxNcp.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxSap_Type = Counter32
_TfrapPerfIpxPerDlciRxSap_Object = MibTableColumn
tfrapPerfIpxPerDlciRxSap = _TfrapPerfIpxPerDlciRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 9),
    _TfrapPerfIpxPerDlciRxSap_Type()
)
tfrapPerfIpxPerDlciRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxSap.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxSap_Type = Counter32
_TfrapPerfIpxPerDlciTxSap_Object = MibTableColumn
tfrapPerfIpxPerDlciTxSap = _TfrapPerfIpxPerDlciTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 10),
    _TfrapPerfIpxPerDlciTxSap_Type()
)
tfrapPerfIpxPerDlciTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxSap.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxRip_Type = Counter32
_TfrapPerfIpxPerDlciRxRip_Object = MibTableColumn
tfrapPerfIpxPerDlciRxRip = _TfrapPerfIpxPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 11),
    _TfrapPerfIpxPerDlciRxRip_Type()
)
tfrapPerfIpxPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxRip.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxRip_Type = Counter32
_TfrapPerfIpxPerDlciTxRip_Object = MibTableColumn
tfrapPerfIpxPerDlciTxRip = _TfrapPerfIpxPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 12),
    _TfrapPerfIpxPerDlciTxRip_Type()
)
tfrapPerfIpxPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxRip.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxNetbios_Type = Counter32
_TfrapPerfIpxPerDlciRxNetbios_Object = MibTableColumn
tfrapPerfIpxPerDlciRxNetbios = _TfrapPerfIpxPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 13),
    _TfrapPerfIpxPerDlciRxNetbios_Type()
)
tfrapPerfIpxPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxNetbios.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxNetbios_Type = Counter32
_TfrapPerfIpxPerDlciTxNetbios_Object = MibTableColumn
tfrapPerfIpxPerDlciTxNetbios = _TfrapPerfIpxPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 14),
    _TfrapPerfIpxPerDlciTxNetbios_Type()
)
tfrapPerfIpxPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxNetbios.setStatus("mandatory")
_TfrapPerfIpxPerDlciRxOther_Type = Counter32
_TfrapPerfIpxPerDlciRxOther_Object = MibTableColumn
tfrapPerfIpxPerDlciRxOther = _TfrapPerfIpxPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 15),
    _TfrapPerfIpxPerDlciRxOther_Type()
)
tfrapPerfIpxPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciRxOther.setStatus("mandatory")
_TfrapPerfIpxPerDlciTxOther_Type = Counter32
_TfrapPerfIpxPerDlciTxOther_Object = MibTableColumn
tfrapPerfIpxPerDlciTxOther = _TfrapPerfIpxPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 11, 1, 16),
    _TfrapPerfIpxPerDlciTxOther_Type()
)
tfrapPerfIpxPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxPerDlciTxOther.setStatus("mandatory")
_TfrapPerfIpxTotalTable_Object = MibTable
tfrapPerfIpxTotalTable = _TfrapPerfIpxTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12)
)
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTable.setStatus("mandatory")
_TfrapPerfIpxTotalEntry_Object = MibTableRow
tfrapPerfIpxTotalEntry = _TfrapPerfIpxTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1)
)
tfrapPerfIpxTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfIpxTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalEntry.setStatus("mandatory")


class _TfrapPerfIpxTotalInterval_Type(Integer32):
    """Custom type tfrapPerfIpxTotalInterval based on Integer32"""
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


_TfrapPerfIpxTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfIpxTotalInterval_Object = MibTableColumn
tfrapPerfIpxTotalInterval = _TfrapPerfIpxTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 1),
    _TfrapPerfIpxTotalInterval_Type()
)
tfrapPerfIpxTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalInterval.setStatus("mandatory")
_TfrapPerfIpxTotalRxTotal_Type = Counter32
_TfrapPerfIpxTotalRxTotal_Object = MibTableColumn
tfrapPerfIpxTotalRxTotal = _TfrapPerfIpxTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 3),
    _TfrapPerfIpxTotalRxTotal_Type()
)
tfrapPerfIpxTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxTotal.setStatus("mandatory")
_TfrapPerfIpxTotalTxTotal_Type = Counter32
_TfrapPerfIpxTotalTxTotal_Object = MibTableColumn
tfrapPerfIpxTotalTxTotal = _TfrapPerfIpxTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 4),
    _TfrapPerfIpxTotalTxTotal_Type()
)
tfrapPerfIpxTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxTotal.setStatus("mandatory")
_TfrapPerfIpxTotalRxSpx_Type = Counter32
_TfrapPerfIpxTotalRxSpx_Object = MibTableColumn
tfrapPerfIpxTotalRxSpx = _TfrapPerfIpxTotalRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 5),
    _TfrapPerfIpxTotalRxSpx_Type()
)
tfrapPerfIpxTotalRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxSpx.setStatus("mandatory")
_TfrapPerfIpxTotalTxSpx_Type = Counter32
_TfrapPerfIpxTotalTxSpx_Object = MibTableColumn
tfrapPerfIpxTotalTxSpx = _TfrapPerfIpxTotalTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 6),
    _TfrapPerfIpxTotalTxSpx_Type()
)
tfrapPerfIpxTotalTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxSpx.setStatus("mandatory")
_TfrapPerfIpxTotalRxNcp_Type = Counter32
_TfrapPerfIpxTotalRxNcp_Object = MibTableColumn
tfrapPerfIpxTotalRxNcp = _TfrapPerfIpxTotalRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 7),
    _TfrapPerfIpxTotalRxNcp_Type()
)
tfrapPerfIpxTotalRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxNcp.setStatus("mandatory")
_TfrapPerfIpxTotalTxNcp_Type = Counter32
_TfrapPerfIpxTotalTxNcp_Object = MibTableColumn
tfrapPerfIpxTotalTxNcp = _TfrapPerfIpxTotalTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 8),
    _TfrapPerfIpxTotalTxNcp_Type()
)
tfrapPerfIpxTotalTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxNcp.setStatus("mandatory")
_TfrapPerfIpxTotalRxSap_Type = Counter32
_TfrapPerfIpxTotalRxSap_Object = MibTableColumn
tfrapPerfIpxTotalRxSap = _TfrapPerfIpxTotalRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 9),
    _TfrapPerfIpxTotalRxSap_Type()
)
tfrapPerfIpxTotalRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxSap.setStatus("mandatory")
_TfrapPerfIpxTotalTxSap_Type = Counter32
_TfrapPerfIpxTotalTxSap_Object = MibTableColumn
tfrapPerfIpxTotalTxSap = _TfrapPerfIpxTotalTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 10),
    _TfrapPerfIpxTotalTxSap_Type()
)
tfrapPerfIpxTotalTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxSap.setStatus("mandatory")
_TfrapPerfIpxTotalRxRip_Type = Counter32
_TfrapPerfIpxTotalRxRip_Object = MibTableColumn
tfrapPerfIpxTotalRxRip = _TfrapPerfIpxTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 11),
    _TfrapPerfIpxTotalRxRip_Type()
)
tfrapPerfIpxTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxRip.setStatus("mandatory")
_TfrapPerfIpxTotalTxRip_Type = Counter32
_TfrapPerfIpxTotalTxRip_Object = MibTableColumn
tfrapPerfIpxTotalTxRip = _TfrapPerfIpxTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 12),
    _TfrapPerfIpxTotalTxRip_Type()
)
tfrapPerfIpxTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxRip.setStatus("mandatory")
_TfrapPerfIpxTotalRxNetbios_Type = Counter32
_TfrapPerfIpxTotalRxNetbios_Object = MibTableColumn
tfrapPerfIpxTotalRxNetbios = _TfrapPerfIpxTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 13),
    _TfrapPerfIpxTotalRxNetbios_Type()
)
tfrapPerfIpxTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxNetbios.setStatus("mandatory")
_TfrapPerfIpxTotalTxNetbios_Type = Counter32
_TfrapPerfIpxTotalTxNetbios_Object = MibTableColumn
tfrapPerfIpxTotalTxNetbios = _TfrapPerfIpxTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 14),
    _TfrapPerfIpxTotalTxNetbios_Type()
)
tfrapPerfIpxTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxNetbios.setStatus("mandatory")
_TfrapPerfIpxTotalRxOther_Type = Counter32
_TfrapPerfIpxTotalRxOther_Object = MibTableColumn
tfrapPerfIpxTotalRxOther = _TfrapPerfIpxTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 15),
    _TfrapPerfIpxTotalRxOther_Type()
)
tfrapPerfIpxTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalRxOther.setStatus("mandatory")
_TfrapPerfIpxTotalTxOther_Type = Counter32
_TfrapPerfIpxTotalTxOther_Object = MibTableColumn
tfrapPerfIpxTotalTxOther = _TfrapPerfIpxTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 12, 1, 16),
    _TfrapPerfIpxTotalTxOther_Type()
)
tfrapPerfIpxTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfIpxTotalTxOther.setStatus("mandatory")
_TfrapPerfSnaPerDlciTable_Object = MibTable
tfrapPerfSnaPerDlciTable = _TfrapPerfSnaPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13)
)
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTable.setStatus("mandatory")
_TfrapPerfSnaPerDlciEntry_Object = MibTableRow
tfrapPerfSnaPerDlciEntry = _TfrapPerfSnaPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1)
)
tfrapPerfSnaPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfSnaPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfSnaPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciEntry.setStatus("mandatory")


class _TfrapPerfSnaPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfSnaPerDlciInterval based on Integer32"""
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


_TfrapPerfSnaPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfSnaPerDlciInterval_Object = MibTableColumn
tfrapPerfSnaPerDlciInterval = _TfrapPerfSnaPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 1),
    _TfrapPerfSnaPerDlciInterval_Type()
)
tfrapPerfSnaPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciInterval.setStatus("mandatory")
_TfrapPerfSnaPerDlciValue_Type = Integer32
_TfrapPerfSnaPerDlciValue_Object = MibTableColumn
tfrapPerfSnaPerDlciValue = _TfrapPerfSnaPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 2),
    _TfrapPerfSnaPerDlciValue_Type()
)
tfrapPerfSnaPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciValue.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxTotal_Type = Counter32
_TfrapPerfSnaPerDlciRxTotal_Object = MibTableColumn
tfrapPerfSnaPerDlciRxTotal = _TfrapPerfSnaPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 3),
    _TfrapPerfSnaPerDlciRxTotal_Type()
)
tfrapPerfSnaPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxTotal_Type = Counter32
_TfrapPerfSnaPerDlciTxTotal_Object = MibTableColumn
tfrapPerfSnaPerDlciTxTotal = _TfrapPerfSnaPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 4),
    _TfrapPerfSnaPerDlciTxTotal_Type()
)
tfrapPerfSnaPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxSubarea_Type = Counter32
_TfrapPerfSnaPerDlciRxSubarea_Object = MibTableColumn
tfrapPerfSnaPerDlciRxSubarea = _TfrapPerfSnaPerDlciRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 5),
    _TfrapPerfSnaPerDlciRxSubarea_Type()
)
tfrapPerfSnaPerDlciRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxSubarea.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxSubarea_Type = Counter32
_TfrapPerfSnaPerDlciTxSubarea_Object = MibTableColumn
tfrapPerfSnaPerDlciTxSubarea = _TfrapPerfSnaPerDlciTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 6),
    _TfrapPerfSnaPerDlciTxSubarea_Type()
)
tfrapPerfSnaPerDlciTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxSubarea.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxPeriph_Type = Counter32
_TfrapPerfSnaPerDlciRxPeriph_Object = MibTableColumn
tfrapPerfSnaPerDlciRxPeriph = _TfrapPerfSnaPerDlciRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 7),
    _TfrapPerfSnaPerDlciRxPeriph_Type()
)
tfrapPerfSnaPerDlciRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxPeriph.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxPeriph_Type = Counter32
_TfrapPerfSnaPerDlciTxPeriph_Object = MibTableColumn
tfrapPerfSnaPerDlciTxPeriph = _TfrapPerfSnaPerDlciTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 8),
    _TfrapPerfSnaPerDlciTxPeriph_Type()
)
tfrapPerfSnaPerDlciTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxPeriph.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxAppn_Type = Counter32
_TfrapPerfSnaPerDlciRxAppn_Object = MibTableColumn
tfrapPerfSnaPerDlciRxAppn = _TfrapPerfSnaPerDlciRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 9),
    _TfrapPerfSnaPerDlciRxAppn_Type()
)
tfrapPerfSnaPerDlciRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxAppn.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxAppn_Type = Counter32
_TfrapPerfSnaPerDlciTxAppn_Object = MibTableColumn
tfrapPerfSnaPerDlciTxAppn = _TfrapPerfSnaPerDlciTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 10),
    _TfrapPerfSnaPerDlciTxAppn_Type()
)
tfrapPerfSnaPerDlciTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxAppn.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxNetbios_Type = Counter32
_TfrapPerfSnaPerDlciRxNetbios_Object = MibTableColumn
tfrapPerfSnaPerDlciRxNetbios = _TfrapPerfSnaPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 11),
    _TfrapPerfSnaPerDlciRxNetbios_Type()
)
tfrapPerfSnaPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxNetbios.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxNetbios_Type = Counter32
_TfrapPerfSnaPerDlciTxNetbios_Object = MibTableColumn
tfrapPerfSnaPerDlciTxNetbios = _TfrapPerfSnaPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 12),
    _TfrapPerfSnaPerDlciTxNetbios_Type()
)
tfrapPerfSnaPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxNetbios.setStatus("mandatory")
_TfrapPerfSnaPerDlciRxOther_Type = Counter32
_TfrapPerfSnaPerDlciRxOther_Object = MibTableColumn
tfrapPerfSnaPerDlciRxOther = _TfrapPerfSnaPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 13),
    _TfrapPerfSnaPerDlciRxOther_Type()
)
tfrapPerfSnaPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciRxOther.setStatus("mandatory")
_TfrapPerfSnaPerDlciTxOther_Type = Counter32
_TfrapPerfSnaPerDlciTxOther_Object = MibTableColumn
tfrapPerfSnaPerDlciTxOther = _TfrapPerfSnaPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 13, 1, 14),
    _TfrapPerfSnaPerDlciTxOther_Type()
)
tfrapPerfSnaPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaPerDlciTxOther.setStatus("mandatory")
_TfrapPerfSnaTotalTable_Object = MibTable
tfrapPerfSnaTotalTable = _TfrapPerfSnaTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14)
)
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTable.setStatus("mandatory")
_TfrapPerfSnaTotalEntry_Object = MibTableRow
tfrapPerfSnaTotalEntry = _TfrapPerfSnaTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1)
)
tfrapPerfSnaTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfSnaTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalEntry.setStatus("mandatory")


class _TfrapPerfSnaTotalInterval_Type(Integer32):
    """Custom type tfrapPerfSnaTotalInterval based on Integer32"""
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


_TfrapPerfSnaTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfSnaTotalInterval_Object = MibTableColumn
tfrapPerfSnaTotalInterval = _TfrapPerfSnaTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 1),
    _TfrapPerfSnaTotalInterval_Type()
)
tfrapPerfSnaTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalInterval.setStatus("mandatory")
_TfrapPerfSnaTotalRxTotal_Type = Counter32
_TfrapPerfSnaTotalRxTotal_Object = MibTableColumn
tfrapPerfSnaTotalRxTotal = _TfrapPerfSnaTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 3),
    _TfrapPerfSnaTotalRxTotal_Type()
)
tfrapPerfSnaTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxTotal.setStatus("mandatory")
_TfrapPerfSnaTotalTxTotal_Type = Counter32
_TfrapPerfSnaTotalTxTotal_Object = MibTableColumn
tfrapPerfSnaTotalTxTotal = _TfrapPerfSnaTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 4),
    _TfrapPerfSnaTotalTxTotal_Type()
)
tfrapPerfSnaTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxTotal.setStatus("mandatory")
_TfrapPerfSnaTotalRxSubarea_Type = Counter32
_TfrapPerfSnaTotalRxSubarea_Object = MibTableColumn
tfrapPerfSnaTotalRxSubarea = _TfrapPerfSnaTotalRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 5),
    _TfrapPerfSnaTotalRxSubarea_Type()
)
tfrapPerfSnaTotalRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxSubarea.setStatus("mandatory")
_TfrapPerfSnaTotalTxSubarea_Type = Counter32
_TfrapPerfSnaTotalTxSubarea_Object = MibTableColumn
tfrapPerfSnaTotalTxSubarea = _TfrapPerfSnaTotalTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 6),
    _TfrapPerfSnaTotalTxSubarea_Type()
)
tfrapPerfSnaTotalTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxSubarea.setStatus("mandatory")
_TfrapPerfSnaTotalRxPeriph_Type = Counter32
_TfrapPerfSnaTotalRxPeriph_Object = MibTableColumn
tfrapPerfSnaTotalRxPeriph = _TfrapPerfSnaTotalRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 7),
    _TfrapPerfSnaTotalRxPeriph_Type()
)
tfrapPerfSnaTotalRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxPeriph.setStatus("mandatory")
_TfrapPerfSnaTotalTxPeriph_Type = Counter32
_TfrapPerfSnaTotalTxPeriph_Object = MibTableColumn
tfrapPerfSnaTotalTxPeriph = _TfrapPerfSnaTotalTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 8),
    _TfrapPerfSnaTotalTxPeriph_Type()
)
tfrapPerfSnaTotalTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxPeriph.setStatus("mandatory")
_TfrapPerfSnaTotalRxAppn_Type = Counter32
_TfrapPerfSnaTotalRxAppn_Object = MibTableColumn
tfrapPerfSnaTotalRxAppn = _TfrapPerfSnaTotalRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 9),
    _TfrapPerfSnaTotalRxAppn_Type()
)
tfrapPerfSnaTotalRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxAppn.setStatus("mandatory")
_TfrapPerfSnaTotalTxAppn_Type = Counter32
_TfrapPerfSnaTotalTxAppn_Object = MibTableColumn
tfrapPerfSnaTotalTxAppn = _TfrapPerfSnaTotalTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 10),
    _TfrapPerfSnaTotalTxAppn_Type()
)
tfrapPerfSnaTotalTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxAppn.setStatus("mandatory")
_TfrapPerfSnaTotalRxNetbios_Type = Counter32
_TfrapPerfSnaTotalRxNetbios_Object = MibTableColumn
tfrapPerfSnaTotalRxNetbios = _TfrapPerfSnaTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 11),
    _TfrapPerfSnaTotalRxNetbios_Type()
)
tfrapPerfSnaTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxNetbios.setStatus("mandatory")
_TfrapPerfSnaTotalTxNetbios_Type = Counter32
_TfrapPerfSnaTotalTxNetbios_Object = MibTableColumn
tfrapPerfSnaTotalTxNetbios = _TfrapPerfSnaTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 12),
    _TfrapPerfSnaTotalTxNetbios_Type()
)
tfrapPerfSnaTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxNetbios.setStatus("mandatory")
_TfrapPerfSnaTotalRxOther_Type = Counter32
_TfrapPerfSnaTotalRxOther_Object = MibTableColumn
tfrapPerfSnaTotalRxOther = _TfrapPerfSnaTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 13),
    _TfrapPerfSnaTotalRxOther_Type()
)
tfrapPerfSnaTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalRxOther.setStatus("mandatory")
_TfrapPerfSnaTotalTxOther_Type = Counter32
_TfrapPerfSnaTotalTxOther_Object = MibTableColumn
tfrapPerfSnaTotalTxOther = _TfrapPerfSnaTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 14, 1, 14),
    _TfrapPerfSnaTotalTxOther_Type()
)
tfrapPerfSnaTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfSnaTotalTxOther.setStatus("mandatory")
_TfrapPerfArpPerDlciTable_Object = MibTable
tfrapPerfArpPerDlciTable = _TfrapPerfArpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15)
)
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTable.setStatus("mandatory")
_TfrapPerfArpPerDlciEntry_Object = MibTableRow
tfrapPerfArpPerDlciEntry = _TfrapPerfArpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1)
)
tfrapPerfArpPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfArpPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfArpPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciEntry.setStatus("mandatory")


class _TfrapPerfArpPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfArpPerDlciInterval based on Integer32"""
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


_TfrapPerfArpPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfArpPerDlciInterval_Object = MibTableColumn
tfrapPerfArpPerDlciInterval = _TfrapPerfArpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 1),
    _TfrapPerfArpPerDlciInterval_Type()
)
tfrapPerfArpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciInterval.setStatus("mandatory")
_TfrapPerfArpPerDlciValue_Type = Integer32
_TfrapPerfArpPerDlciValue_Object = MibTableColumn
tfrapPerfArpPerDlciValue = _TfrapPerfArpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 2),
    _TfrapPerfArpPerDlciValue_Type()
)
tfrapPerfArpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciValue.setStatus("mandatory")
_TfrapPerfArpPerDlciRxTotal_Type = Counter32
_TfrapPerfArpPerDlciRxTotal_Object = MibTableColumn
tfrapPerfArpPerDlciRxTotal = _TfrapPerfArpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 3),
    _TfrapPerfArpPerDlciRxTotal_Type()
)
tfrapPerfArpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxTotal.setStatus("mandatory")
_TfrapPerfArpPerDlciTxTotal_Type = Counter32
_TfrapPerfArpPerDlciTxTotal_Object = MibTableColumn
tfrapPerfArpPerDlciTxTotal = _TfrapPerfArpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 4),
    _TfrapPerfArpPerDlciTxTotal_Type()
)
tfrapPerfArpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxTotal.setStatus("mandatory")
_TfrapPerfArpPerDlciRxArpReq_Type = Counter32
_TfrapPerfArpPerDlciRxArpReq_Object = MibTableColumn
tfrapPerfArpPerDlciRxArpReq = _TfrapPerfArpPerDlciRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 5),
    _TfrapPerfArpPerDlciRxArpReq_Type()
)
tfrapPerfArpPerDlciRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxArpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciTxArpReq_Type = Counter32
_TfrapPerfArpPerDlciTxArpReq_Object = MibTableColumn
tfrapPerfArpPerDlciTxArpReq = _TfrapPerfArpPerDlciTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 6),
    _TfrapPerfArpPerDlciTxArpReq_Type()
)
tfrapPerfArpPerDlciTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxArpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciRxArpRep_Type = Counter32
_TfrapPerfArpPerDlciRxArpRep_Object = MibTableColumn
tfrapPerfArpPerDlciRxArpRep = _TfrapPerfArpPerDlciRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 7),
    _TfrapPerfArpPerDlciRxArpRep_Type()
)
tfrapPerfArpPerDlciRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxArpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciTxArpRep_Type = Counter32
_TfrapPerfArpPerDlciTxArpRep_Object = MibTableColumn
tfrapPerfArpPerDlciTxArpRep = _TfrapPerfArpPerDlciTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 8),
    _TfrapPerfArpPerDlciTxArpRep_Type()
)
tfrapPerfArpPerDlciTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxArpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciRxRarpReq_Type = Counter32
_TfrapPerfArpPerDlciRxRarpReq_Object = MibTableColumn
tfrapPerfArpPerDlciRxRarpReq = _TfrapPerfArpPerDlciRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 9),
    _TfrapPerfArpPerDlciRxRarpReq_Type()
)
tfrapPerfArpPerDlciRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxRarpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciTxRarpReq_Type = Counter32
_TfrapPerfArpPerDlciTxRarpReq_Object = MibTableColumn
tfrapPerfArpPerDlciTxRarpReq = _TfrapPerfArpPerDlciTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 10),
    _TfrapPerfArpPerDlciTxRarpReq_Type()
)
tfrapPerfArpPerDlciTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxRarpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciRxRarpRep_Type = Counter32
_TfrapPerfArpPerDlciRxRarpRep_Object = MibTableColumn
tfrapPerfArpPerDlciRxRarpRep = _TfrapPerfArpPerDlciRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 11),
    _TfrapPerfArpPerDlciRxRarpRep_Type()
)
tfrapPerfArpPerDlciRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxRarpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciTxRarpRep_Type = Counter32
_TfrapPerfArpPerDlciTxRarpRep_Object = MibTableColumn
tfrapPerfArpPerDlciTxRarpRep = _TfrapPerfArpPerDlciTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 12),
    _TfrapPerfArpPerDlciTxRarpRep_Type()
)
tfrapPerfArpPerDlciTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxRarpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciRxInarpReq_Type = Counter32
_TfrapPerfArpPerDlciRxInarpReq_Object = MibTableColumn
tfrapPerfArpPerDlciRxInarpReq = _TfrapPerfArpPerDlciRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 13),
    _TfrapPerfArpPerDlciRxInarpReq_Type()
)
tfrapPerfArpPerDlciRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxInarpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciTxInarpReq_Type = Counter32
_TfrapPerfArpPerDlciTxInarpReq_Object = MibTableColumn
tfrapPerfArpPerDlciTxInarpReq = _TfrapPerfArpPerDlciTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 14),
    _TfrapPerfArpPerDlciTxInarpReq_Type()
)
tfrapPerfArpPerDlciTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxInarpReq.setStatus("mandatory")
_TfrapPerfArpPerDlciRxInarpRep_Type = Counter32
_TfrapPerfArpPerDlciRxInarpRep_Object = MibTableColumn
tfrapPerfArpPerDlciRxInarpRep = _TfrapPerfArpPerDlciRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 15),
    _TfrapPerfArpPerDlciRxInarpRep_Type()
)
tfrapPerfArpPerDlciRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxInarpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciTxInarpRep_Type = Counter32
_TfrapPerfArpPerDlciTxInarpRep_Object = MibTableColumn
tfrapPerfArpPerDlciTxInarpRep = _TfrapPerfArpPerDlciTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 16),
    _TfrapPerfArpPerDlciTxInarpRep_Type()
)
tfrapPerfArpPerDlciTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxInarpRep.setStatus("mandatory")
_TfrapPerfArpPerDlciRxOther_Type = Counter32
_TfrapPerfArpPerDlciRxOther_Object = MibTableColumn
tfrapPerfArpPerDlciRxOther = _TfrapPerfArpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 17),
    _TfrapPerfArpPerDlciRxOther_Type()
)
tfrapPerfArpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciRxOther.setStatus("mandatory")
_TfrapPerfArpPerDlciTxOther_Type = Counter32
_TfrapPerfArpPerDlciTxOther_Object = MibTableColumn
tfrapPerfArpPerDlciTxOther = _TfrapPerfArpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 15, 1, 18),
    _TfrapPerfArpPerDlciTxOther_Type()
)
tfrapPerfArpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpPerDlciTxOther.setStatus("mandatory")
_TfrapPerfArpTotalTable_Object = MibTable
tfrapPerfArpTotalTable = _TfrapPerfArpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16)
)
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTable.setStatus("mandatory")
_TfrapPerfArpTotalEntry_Object = MibTableRow
tfrapPerfArpTotalEntry = _TfrapPerfArpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1)
)
tfrapPerfArpTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfArpTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfArpTotalEntry.setStatus("mandatory")


class _TfrapPerfArpTotalInterval_Type(Integer32):
    """Custom type tfrapPerfArpTotalInterval based on Integer32"""
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


_TfrapPerfArpTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfArpTotalInterval_Object = MibTableColumn
tfrapPerfArpTotalInterval = _TfrapPerfArpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 1),
    _TfrapPerfArpTotalInterval_Type()
)
tfrapPerfArpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalInterval.setStatus("mandatory")
_TfrapPerfArpTotalRxTotal_Type = Counter32
_TfrapPerfArpTotalRxTotal_Object = MibTableColumn
tfrapPerfArpTotalRxTotal = _TfrapPerfArpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 3),
    _TfrapPerfArpTotalRxTotal_Type()
)
tfrapPerfArpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxTotal.setStatus("mandatory")
_TfrapPerfArpTotalTxTotal_Type = Counter32
_TfrapPerfArpTotalTxTotal_Object = MibTableColumn
tfrapPerfArpTotalTxTotal = _TfrapPerfArpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 4),
    _TfrapPerfArpTotalTxTotal_Type()
)
tfrapPerfArpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxTotal.setStatus("mandatory")
_TfrapPerfArpTotalRxArpReq_Type = Counter32
_TfrapPerfArpTotalRxArpReq_Object = MibTableColumn
tfrapPerfArpTotalRxArpReq = _TfrapPerfArpTotalRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 5),
    _TfrapPerfArpTotalRxArpReq_Type()
)
tfrapPerfArpTotalRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxArpReq.setStatus("mandatory")
_TfrapPerfArpTotalTxArpReq_Type = Counter32
_TfrapPerfArpTotalTxArpReq_Object = MibTableColumn
tfrapPerfArpTotalTxArpReq = _TfrapPerfArpTotalTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 6),
    _TfrapPerfArpTotalTxArpReq_Type()
)
tfrapPerfArpTotalTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxArpReq.setStatus("mandatory")
_TfrapPerfArpTotalRxArpRep_Type = Counter32
_TfrapPerfArpTotalRxArpRep_Object = MibTableColumn
tfrapPerfArpTotalRxArpRep = _TfrapPerfArpTotalRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 7),
    _TfrapPerfArpTotalRxArpRep_Type()
)
tfrapPerfArpTotalRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxArpRep.setStatus("mandatory")
_TfrapPerfArpTotalTxArpRep_Type = Counter32
_TfrapPerfArpTotalTxArpRep_Object = MibTableColumn
tfrapPerfArpTotalTxArpRep = _TfrapPerfArpTotalTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 8),
    _TfrapPerfArpTotalTxArpRep_Type()
)
tfrapPerfArpTotalTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxArpRep.setStatus("mandatory")
_TfrapPerfArpTotalRxRarpReq_Type = Counter32
_TfrapPerfArpTotalRxRarpReq_Object = MibTableColumn
tfrapPerfArpTotalRxRarpReq = _TfrapPerfArpTotalRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 9),
    _TfrapPerfArpTotalRxRarpReq_Type()
)
tfrapPerfArpTotalRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxRarpReq.setStatus("mandatory")
_TfrapPerfArpTotalTxRarpReq_Type = Counter32
_TfrapPerfArpTotalTxRarpReq_Object = MibTableColumn
tfrapPerfArpTotalTxRarpReq = _TfrapPerfArpTotalTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 10),
    _TfrapPerfArpTotalTxRarpReq_Type()
)
tfrapPerfArpTotalTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxRarpReq.setStatus("mandatory")
_TfrapPerfArpTotalRxRarpRep_Type = Counter32
_TfrapPerfArpTotalRxRarpRep_Object = MibTableColumn
tfrapPerfArpTotalRxRarpRep = _TfrapPerfArpTotalRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 11),
    _TfrapPerfArpTotalRxRarpRep_Type()
)
tfrapPerfArpTotalRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxRarpRep.setStatus("mandatory")
_TfrapPerfArpTotalTxRarpRep_Type = Counter32
_TfrapPerfArpTotalTxRarpRep_Object = MibTableColumn
tfrapPerfArpTotalTxRarpRep = _TfrapPerfArpTotalTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 12),
    _TfrapPerfArpTotalTxRarpRep_Type()
)
tfrapPerfArpTotalTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxRarpRep.setStatus("mandatory")
_TfrapPerfArpTotalRxInarpReq_Type = Counter32
_TfrapPerfArpTotalRxInarpReq_Object = MibTableColumn
tfrapPerfArpTotalRxInarpReq = _TfrapPerfArpTotalRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 13),
    _TfrapPerfArpTotalRxInarpReq_Type()
)
tfrapPerfArpTotalRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxInarpReq.setStatus("mandatory")
_TfrapPerfArpTotalTxInarpReq_Type = Counter32
_TfrapPerfArpTotalTxInarpReq_Object = MibTableColumn
tfrapPerfArpTotalTxInarpReq = _TfrapPerfArpTotalTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 14),
    _TfrapPerfArpTotalTxInarpReq_Type()
)
tfrapPerfArpTotalTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxInarpReq.setStatus("mandatory")
_TfrapPerfArpTotalRxInarpRep_Type = Counter32
_TfrapPerfArpTotalRxInarpRep_Object = MibTableColumn
tfrapPerfArpTotalRxInarpRep = _TfrapPerfArpTotalRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 15),
    _TfrapPerfArpTotalRxInarpRep_Type()
)
tfrapPerfArpTotalRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxInarpRep.setStatus("mandatory")
_TfrapPerfArpTotalTxInarpRep_Type = Counter32
_TfrapPerfArpTotalTxInarpRep_Object = MibTableColumn
tfrapPerfArpTotalTxInarpRep = _TfrapPerfArpTotalTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 16),
    _TfrapPerfArpTotalTxInarpRep_Type()
)
tfrapPerfArpTotalTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxInarpRep.setStatus("mandatory")
_TfrapPerfArpTotalRxOther_Type = Counter32
_TfrapPerfArpTotalRxOther_Object = MibTableColumn
tfrapPerfArpTotalRxOther = _TfrapPerfArpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 17),
    _TfrapPerfArpTotalRxOther_Type()
)
tfrapPerfArpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalRxOther.setStatus("mandatory")
_TfrapPerfArpTotalTxOther_Type = Counter32
_TfrapPerfArpTotalTxOther_Object = MibTableColumn
tfrapPerfArpTotalTxOther = _TfrapPerfArpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 16, 1, 18),
    _TfrapPerfArpTotalTxOther_Type()
)
tfrapPerfArpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfArpTotalTxOther.setStatus("mandatory")
_TfrapPerfLmiPerDlciTable_Object = MibTable
tfrapPerfLmiPerDlciTable = _TfrapPerfLmiPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17)
)
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTable.setStatus("mandatory")
_TfrapPerfLmiPerDlciEntry_Object = MibTableRow
tfrapPerfLmiPerDlciEntry = _TfrapPerfLmiPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1)
)
tfrapPerfLmiPerDlciEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfLmiPerDlciInterval"),
    (0, "TFRAP-MIB", "tfrapPerfLmiPerDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciEntry.setStatus("mandatory")


class _TfrapPerfLmiPerDlciInterval_Type(Integer32):
    """Custom type tfrapPerfLmiPerDlciInterval based on Integer32"""
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


_TfrapPerfLmiPerDlciInterval_Type.__name__ = "Integer32"
_TfrapPerfLmiPerDlciInterval_Object = MibTableColumn
tfrapPerfLmiPerDlciInterval = _TfrapPerfLmiPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 1),
    _TfrapPerfLmiPerDlciInterval_Type()
)
tfrapPerfLmiPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciInterval.setStatus("mandatory")
_TfrapPerfLmiPerDlciValue_Type = Integer32
_TfrapPerfLmiPerDlciValue_Object = MibTableColumn
tfrapPerfLmiPerDlciValue = _TfrapPerfLmiPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 2),
    _TfrapPerfLmiPerDlciValue_Type()
)
tfrapPerfLmiPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciValue.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxTotalByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxTotalByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxTotalByteCnt = _TfrapPerfLmiPerDlciRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 3),
    _TfrapPerfLmiPerDlciRxTotalByteCnt_Type()
)
tfrapPerfLmiPerDlciRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxTotalByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxTotalByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxTotalByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxTotalByteCnt = _TfrapPerfLmiPerDlciTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 4),
    _TfrapPerfLmiPerDlciTxTotalByteCnt_Type()
)
tfrapPerfLmiPerDlciTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxTotalByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxLivoEnqByteCnt = _TfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 5),
    _TfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type()
)
tfrapPerfLmiPerDlciRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxLivoEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxLivoEnqByteCnt = _TfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 6),
    _TfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type()
)
tfrapPerfLmiPerDlciTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxLivoEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxLivoStatByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxLivoStatByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxLivoStatByteCnt = _TfrapPerfLmiPerDlciRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 7),
    _TfrapPerfLmiPerDlciRxLivoStatByteCnt_Type()
)
tfrapPerfLmiPerDlciRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxLivoStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxLivoStatByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxLivoStatByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxLivoStatByteCnt = _TfrapPerfLmiPerDlciTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 8),
    _TfrapPerfLmiPerDlciTxLivoStatByteCnt_Type()
)
tfrapPerfLmiPerDlciTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxLivoStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxFullEnqByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxFullEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxFullEnqByteCnt = _TfrapPerfLmiPerDlciRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 9),
    _TfrapPerfLmiPerDlciRxFullEnqByteCnt_Type()
)
tfrapPerfLmiPerDlciRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxFullEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxFullEnqByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxFullEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxFullEnqByteCnt = _TfrapPerfLmiPerDlciTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 10),
    _TfrapPerfLmiPerDlciTxFullEnqByteCnt_Type()
)
tfrapPerfLmiPerDlciTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxFullEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxFullStatByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxFullStatByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxFullStatByteCnt = _TfrapPerfLmiPerDlciRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 11),
    _TfrapPerfLmiPerDlciRxFullStatByteCnt_Type()
)
tfrapPerfLmiPerDlciRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxFullStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxFullStatByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxFullStatByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxFullStatByteCnt = _TfrapPerfLmiPerDlciTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 12),
    _TfrapPerfLmiPerDlciTxFullStatByteCnt_Type()
)
tfrapPerfLmiPerDlciTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxFullStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciRxOtherByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciRxOtherByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciRxOtherByteCnt = _TfrapPerfLmiPerDlciRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 13),
    _TfrapPerfLmiPerDlciRxOtherByteCnt_Type()
)
tfrapPerfLmiPerDlciRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciRxOtherByteCnt.setStatus("mandatory")
_TfrapPerfLmiPerDlciTxOtherByteCnt_Type = Counter32
_TfrapPerfLmiPerDlciTxOtherByteCnt_Object = MibTableColumn
tfrapPerfLmiPerDlciTxOtherByteCnt = _TfrapPerfLmiPerDlciTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 17, 1, 14),
    _TfrapPerfLmiPerDlciTxOtherByteCnt_Type()
)
tfrapPerfLmiPerDlciTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiPerDlciTxOtherByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTable_Object = MibTable
tfrapPerfLmiTotalTable = _TfrapPerfLmiTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18)
)
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTable.setStatus("mandatory")
_TfrapPerfLmiTotalEntry_Object = MibTableRow
tfrapPerfLmiTotalEntry = _TfrapPerfLmiTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1)
)
tfrapPerfLmiTotalEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfLmiTotalInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalEntry.setStatus("mandatory")


class _TfrapPerfLmiTotalInterval_Type(Integer32):
    """Custom type tfrapPerfLmiTotalInterval based on Integer32"""
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


_TfrapPerfLmiTotalInterval_Type.__name__ = "Integer32"
_TfrapPerfLmiTotalInterval_Object = MibTableColumn
tfrapPerfLmiTotalInterval = _TfrapPerfLmiTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 1),
    _TfrapPerfLmiTotalInterval_Type()
)
tfrapPerfLmiTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalInterval.setStatus("mandatory")
_TfrapPerfLmiTotalDlciValue_Type = Integer32
_TfrapPerfLmiTotalDlciValue_Object = MibTableColumn
tfrapPerfLmiTotalDlciValue = _TfrapPerfLmiTotalDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 2),
    _TfrapPerfLmiTotalDlciValue_Type()
)
tfrapPerfLmiTotalDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalDlciValue.setStatus("mandatory")
_TfrapPerfLmiTotalRxTotalByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxTotalByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxTotalByteCnt = _TfrapPerfLmiTotalRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 3),
    _TfrapPerfLmiTotalRxTotalByteCnt_Type()
)
tfrapPerfLmiTotalRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxTotalByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxTotalByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxTotalByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxTotalByteCnt = _TfrapPerfLmiTotalTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 4),
    _TfrapPerfLmiTotalTxTotalByteCnt_Type()
)
tfrapPerfLmiTotalTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxTotalByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalRxLivoEnqByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxLivoEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxLivoEnqByteCnt = _TfrapPerfLmiTotalRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 5),
    _TfrapPerfLmiTotalRxLivoEnqByteCnt_Type()
)
tfrapPerfLmiTotalRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxLivoEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxLivoEnqByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxLivoEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxLivoEnqByteCnt = _TfrapPerfLmiTotalTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 6),
    _TfrapPerfLmiTotalTxLivoEnqByteCnt_Type()
)
tfrapPerfLmiTotalTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxLivoEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalRxLivoStatByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxLivoStatByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxLivoStatByteCnt = _TfrapPerfLmiTotalRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 7),
    _TfrapPerfLmiTotalRxLivoStatByteCnt_Type()
)
tfrapPerfLmiTotalRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxLivoStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxLivoStatByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxLivoStatByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxLivoStatByteCnt = _TfrapPerfLmiTotalTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 8),
    _TfrapPerfLmiTotalTxLivoStatByteCnt_Type()
)
tfrapPerfLmiTotalTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxLivoStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalRxFullEnqByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxFullEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxFullEnqByteCnt = _TfrapPerfLmiTotalRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 9),
    _TfrapPerfLmiTotalRxFullEnqByteCnt_Type()
)
tfrapPerfLmiTotalRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxFullEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxFullEnqByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxFullEnqByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxFullEnqByteCnt = _TfrapPerfLmiTotalTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 10),
    _TfrapPerfLmiTotalTxFullEnqByteCnt_Type()
)
tfrapPerfLmiTotalTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxFullEnqByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalRxFullStatByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxFullStatByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxFullStatByteCnt = _TfrapPerfLmiTotalRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 11),
    _TfrapPerfLmiTotalRxFullStatByteCnt_Type()
)
tfrapPerfLmiTotalRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxFullStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxFullStatByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxFullStatByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxFullStatByteCnt = _TfrapPerfLmiTotalTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 12),
    _TfrapPerfLmiTotalTxFullStatByteCnt_Type()
)
tfrapPerfLmiTotalTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxFullStatByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalRxOtherByteCnt_Type = Counter32
_TfrapPerfLmiTotalRxOtherByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalRxOtherByteCnt = _TfrapPerfLmiTotalRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 13),
    _TfrapPerfLmiTotalRxOtherByteCnt_Type()
)
tfrapPerfLmiTotalRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalRxOtherByteCnt.setStatus("mandatory")
_TfrapPerfLmiTotalTxOtherByteCnt_Type = Counter32
_TfrapPerfLmiTotalTxOtherByteCnt_Object = MibTableColumn
tfrapPerfLmiTotalTxOtherByteCnt = _TfrapPerfLmiTotalTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 4, 18, 1, 14),
    _TfrapPerfLmiTotalTxOtherByteCnt_Type()
)
tfrapPerfLmiTotalTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfLmiTotalTxOtherByteCnt.setStatus("mandatory")
_TfrapPerfNetworkLongTerm_ObjectIdentity = ObjectIdentity
tfrapPerfNetworkLongTerm = _TfrapPerfNetworkLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5)
)
_TfrapPerfNetwLongTermTable_Object = MibTable
tfrapPerfNetwLongTermTable = _TfrapPerfNetwLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1)
)
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermTable.setStatus("mandatory")
_TfrapPerfNetwLongTermEntry_Object = MibTableRow
tfrapPerfNetwLongTermEntry = _TfrapPerfNetwLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1, 1)
)
tfrapPerfNetwLongTermEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfNetwLongTermDlci"),
    (0, "TFRAP-MIB", "tfrapPerfNetwLongTermProtocol"),
    (0, "TFRAP-MIB", "tfrapPerfNetwLongTermInterval"),
)
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermEntry.setStatus("mandatory")
_TfrapPerfNetwLongTermDlci_Type = Integer32
_TfrapPerfNetwLongTermDlci_Object = MibTableColumn
tfrapPerfNetwLongTermDlci = _TfrapPerfNetwLongTermDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1, 1, 1),
    _TfrapPerfNetwLongTermDlci_Type()
)
tfrapPerfNetwLongTermDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermDlci.setStatus("mandatory")


class _TfrapPerfNetwLongTermProtocol_Type(Integer32):
    """Custom type tfrapPerfNetwLongTermProtocol based on Integer32"""
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
          ("thru-becn-rx-bc", 134),
          ("thru-becn-tx-bc", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-bc", 136),
          ("thru-de-tx-bc", 135),
          ("thru-fecn-rx-bc", 132),
          ("thru-fecn-tx-bc", 131),
          ("thru-frame-rx-bc", 130),
          ("thru-frame-tx-bc", 129),
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


_TfrapPerfNetwLongTermProtocol_Type.__name__ = "Integer32"
_TfrapPerfNetwLongTermProtocol_Object = MibTableColumn
tfrapPerfNetwLongTermProtocol = _TfrapPerfNetwLongTermProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1, 1, 2),
    _TfrapPerfNetwLongTermProtocol_Type()
)
tfrapPerfNetwLongTermProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermProtocol.setStatus("mandatory")
_TfrapPerfNetwLongTermInterval_Type = Integer32
_TfrapPerfNetwLongTermInterval_Object = MibTableColumn
tfrapPerfNetwLongTermInterval = _TfrapPerfNetwLongTermInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1, 1, 3),
    _TfrapPerfNetwLongTermInterval_Type()
)
tfrapPerfNetwLongTermInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermInterval.setStatus("mandatory")
_TfrapPerfNetwLongTermValue_Type = Counter32
_TfrapPerfNetwLongTermValue_Object = MibTableColumn
tfrapPerfNetwLongTermValue = _TfrapPerfNetwLongTermValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 1, 1, 4),
    _TfrapPerfNetwLongTermValue_Type()
)
tfrapPerfNetwLongTermValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermValue.setStatus("mandatory")
_TfrapPerfNetwLongTermAltTable_Object = MibTable
tfrapPerfNetwLongTermAltTable = _TfrapPerfNetwLongTermAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 2)
)
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermAltTable.setStatus("mandatory")
_TfrapPerfNetwLongTermAltEntry_Object = MibTableRow
tfrapPerfNetwLongTermAltEntry = _TfrapPerfNetwLongTermAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 2, 1)
)
tfrapPerfNetwLongTermAltEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfNetwLongTermAltDlci"),
    (0, "TFRAP-MIB", "tfrapPerfNetwLongTermAltProtocol"),
)
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermAltEntry.setStatus("mandatory")
_TfrapPerfNetwLongTermAltDlci_Type = Integer32
_TfrapPerfNetwLongTermAltDlci_Object = MibTableColumn
tfrapPerfNetwLongTermAltDlci = _TfrapPerfNetwLongTermAltDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 2, 1, 1),
    _TfrapPerfNetwLongTermAltDlci_Type()
)
tfrapPerfNetwLongTermAltDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermAltDlci.setStatus("mandatory")


class _TfrapPerfNetwLongTermAltProtocol_Type(Integer32):
    """Custom type tfrapPerfNetwLongTermAltProtocol based on Integer32"""
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
          ("thru-becn-rx-bc", 134),
          ("thru-becn-tx-bc", 133),
          ("thru-byte-rx-bc", 128),
          ("thru-byte-tx-bc", 127),
          ("thru-de-rx-bc", 136),
          ("thru-de-tx-bc", 135),
          ("thru-fecn-rx-bc", 132),
          ("thru-fecn-tx-bc", 131),
          ("thru-frame-rx-bc", 130),
          ("thru-frame-tx-bc", 129),
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


_TfrapPerfNetwLongTermAltProtocol_Type.__name__ = "Integer32"
_TfrapPerfNetwLongTermAltProtocol_Object = MibTableColumn
tfrapPerfNetwLongTermAltProtocol = _TfrapPerfNetwLongTermAltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 2, 1, 2),
    _TfrapPerfNetwLongTermAltProtocol_Type()
)
tfrapPerfNetwLongTermAltProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermAltProtocol.setStatus("mandatory")
_TfrapPerfNetwLongTermAltArray_Type = OctetString
_TfrapPerfNetwLongTermAltArray_Object = MibTableColumn
tfrapPerfNetwLongTermAltArray = _TfrapPerfNetwLongTermAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 2, 1, 3),
    _TfrapPerfNetwLongTermAltArray_Type()
)
tfrapPerfNetwLongTermAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfNetwLongTermAltArray.setStatus("mandatory")
_TfrapPerfNetworkLongTermCommands_ObjectIdentity = ObjectIdentity
tfrapPerfNetworkLongTermCommands = _TfrapPerfNetworkLongTermCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 3)
)


class _TfrapPerfNetworkLongTermCmdClear_Type(Integer32):
    """Custom type tfrapPerfNetworkLongTermCmdClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_TfrapPerfNetworkLongTermCmdClear_Type.__name__ = "Integer32"
_TfrapPerfNetworkLongTermCmdClear_Object = MibScalar
tfrapPerfNetworkLongTermCmdClear = _TfrapPerfNetworkLongTermCmdClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 5, 3, 1),
    _TfrapPerfNetworkLongTermCmdClear_Type()
)
tfrapPerfNetworkLongTermCmdClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapPerfNetworkLongTermCmdClear.setStatus("mandatory")
_TfrapPerfCirPercentUtilization_ObjectIdentity = ObjectIdentity
tfrapPerfCirPercentUtilization = _TfrapPerfCirPercentUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6)
)
_TfrapPerfCirPercentUtilizationTable_Object = MibTable
tfrapPerfCirPercentUtilizationTable = _TfrapPerfCirPercentUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1)
)
if mibBuilder.loadTexts:
    tfrapPerfCirPercentUtilizationTable.setStatus("mandatory")
_TfrapPerfCirPercentUtilizationEntry_Object = MibTableRow
tfrapPerfCirPercentUtilizationEntry = _TfrapPerfCirPercentUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1)
)
tfrapPerfCirPercentUtilizationEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfCirPercentUtilizationInterval"),
    (0, "TFRAP-MIB", "tfrapPerfCirPercentUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfCirPercentUtilizationEntry.setStatus("mandatory")


class _TfrapPerfCirPercentUtilizationInterval_Type(Integer32):
    """Custom type tfrapPerfCirPercentUtilizationInterval based on Integer32"""
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


_TfrapPerfCirPercentUtilizationInterval_Type.__name__ = "Integer32"
_TfrapPerfCirPercentUtilizationInterval_Object = MibTableColumn
tfrapPerfCirPercentUtilizationInterval = _TfrapPerfCirPercentUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 1),
    _TfrapPerfCirPercentUtilizationInterval_Type()
)
tfrapPerfCirPercentUtilizationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirPercentUtilizationInterval.setStatus("mandatory")
_TfrapPerfCirPercentUtilizationDlciValue_Type = Integer32
_TfrapPerfCirPercentUtilizationDlciValue_Object = MibTableColumn
tfrapPerfCirPercentUtilizationDlciValue = _TfrapPerfCirPercentUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 2),
    _TfrapPerfCirPercentUtilizationDlciValue_Type()
)
tfrapPerfCirPercentUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirPercentUtilizationDlciValue.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange1_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange1_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange1 = _TfrapPerfCirRxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 21),
    _TfrapPerfCirRxPercentUtilizationRange1_Type()
)
tfrapPerfCirRxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange1.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange2_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange2_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange2 = _TfrapPerfCirRxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 22),
    _TfrapPerfCirRxPercentUtilizationRange2_Type()
)
tfrapPerfCirRxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange2.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange3_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange3_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange3 = _TfrapPerfCirRxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 23),
    _TfrapPerfCirRxPercentUtilizationRange3_Type()
)
tfrapPerfCirRxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange3.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange4_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange4_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange4 = _TfrapPerfCirRxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 24),
    _TfrapPerfCirRxPercentUtilizationRange4_Type()
)
tfrapPerfCirRxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange4.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange5_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange5_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange5 = _TfrapPerfCirRxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 25),
    _TfrapPerfCirRxPercentUtilizationRange5_Type()
)
tfrapPerfCirRxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange5.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange6_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange6_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange6 = _TfrapPerfCirRxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 26),
    _TfrapPerfCirRxPercentUtilizationRange6_Type()
)
tfrapPerfCirRxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange6.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange7_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange7_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange7 = _TfrapPerfCirRxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 27),
    _TfrapPerfCirRxPercentUtilizationRange7_Type()
)
tfrapPerfCirRxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange7.setStatus("mandatory")
_TfrapPerfCirRxPercentUtilizationRange8_Type = Integer32
_TfrapPerfCirRxPercentUtilizationRange8_Object = MibTableColumn
tfrapPerfCirRxPercentUtilizationRange8 = _TfrapPerfCirRxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 28),
    _TfrapPerfCirRxPercentUtilizationRange8_Type()
)
tfrapPerfCirRxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirRxPercentUtilizationRange8.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange1_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange1_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange1 = _TfrapPerfCirTxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 41),
    _TfrapPerfCirTxPercentUtilizationRange1_Type()
)
tfrapPerfCirTxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange1.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange2_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange2_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange2 = _TfrapPerfCirTxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 42),
    _TfrapPerfCirTxPercentUtilizationRange2_Type()
)
tfrapPerfCirTxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange2.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange3_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange3_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange3 = _TfrapPerfCirTxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 43),
    _TfrapPerfCirTxPercentUtilizationRange3_Type()
)
tfrapPerfCirTxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange3.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange4_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange4_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange4 = _TfrapPerfCirTxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 44),
    _TfrapPerfCirTxPercentUtilizationRange4_Type()
)
tfrapPerfCirTxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange4.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange5_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange5_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange5 = _TfrapPerfCirTxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 45),
    _TfrapPerfCirTxPercentUtilizationRange5_Type()
)
tfrapPerfCirTxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange5.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange6_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange6_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange6 = _TfrapPerfCirTxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 46),
    _TfrapPerfCirTxPercentUtilizationRange6_Type()
)
tfrapPerfCirTxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange6.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange7_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange7_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange7 = _TfrapPerfCirTxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 47),
    _TfrapPerfCirTxPercentUtilizationRange7_Type()
)
tfrapPerfCirTxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange7.setStatus("mandatory")
_TfrapPerfCirTxPercentUtilizationRange8_Type = Integer32
_TfrapPerfCirTxPercentUtilizationRange8_Object = MibTableColumn
tfrapPerfCirTxPercentUtilizationRange8 = _TfrapPerfCirTxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 1, 1, 48),
    _TfrapPerfCirTxPercentUtilizationRange8_Type()
)
tfrapPerfCirTxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCirTxPercentUtilizationRange8.setStatus("mandatory")
_TfrapPerfCurrentPerDlciUtilizationTable_Object = MibTable
tfrapPerfCurrentPerDlciUtilizationTable = _TfrapPerfCurrentPerDlciUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2)
)
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciUtilizationTable.setStatus("mandatory")
_TfrapPerfCurrentPerDlciUtilizationEntry_Object = MibTableRow
tfrapPerfCurrentPerDlciUtilizationEntry = _TfrapPerfCurrentPerDlciUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2, 1)
)
tfrapPerfCurrentPerDlciUtilizationEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapPerfCurrentPerDlciUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciUtilizationEntry.setStatus("mandatory")
_TfrapPerfCurrentPerDlciUtilizationDlciValue_Type = Integer32
_TfrapPerfCurrentPerDlciUtilizationDlciValue_Object = MibTableColumn
tfrapPerfCurrentPerDlciUtilizationDlciValue = _TfrapPerfCurrentPerDlciUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2, 1, 1),
    _TfrapPerfCurrentPerDlciUtilizationDlciValue_Type()
)
tfrapPerfCurrentPerDlciUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciUtilizationDlciValue.setStatus("mandatory")
_TfrapPerfCurrentPerDlciRxUtilization_Type = Integer32
_TfrapPerfCurrentPerDlciRxUtilization_Object = MibTableColumn
tfrapPerfCurrentPerDlciRxUtilization = _TfrapPerfCurrentPerDlciRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2, 1, 2),
    _TfrapPerfCurrentPerDlciRxUtilization_Type()
)
tfrapPerfCurrentPerDlciRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciRxUtilization.setStatus("mandatory")
_TfrapPerfCurrentPerDlciTxUtilization_Type = Integer32
_TfrapPerfCurrentPerDlciTxUtilization_Object = MibTableColumn
tfrapPerfCurrentPerDlciTxUtilization = _TfrapPerfCurrentPerDlciTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2, 1, 3),
    _TfrapPerfCurrentPerDlciTxUtilization_Type()
)
tfrapPerfCurrentPerDlciTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciTxUtilization.setStatus("mandatory")
_TfrapPerfCurrentPerDlciAggregateUtilization_Type = Integer32
_TfrapPerfCurrentPerDlciAggregateUtilization_Object = MibTableColumn
tfrapPerfCurrentPerDlciAggregateUtilization = _TfrapPerfCurrentPerDlciAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 2, 1, 4),
    _TfrapPerfCurrentPerDlciAggregateUtilization_Type()
)
tfrapPerfCurrentPerDlciAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentPerDlciAggregateUtilization.setStatus("mandatory")
_TfrapPerfCurrentUnitUtilization_ObjectIdentity = ObjectIdentity
tfrapPerfCurrentUnitUtilization = _TfrapPerfCurrentUnitUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 3)
)
_TfrapPerfCurrentDteUtilization_Type = Integer32
_TfrapPerfCurrentDteUtilization_Object = MibScalar
tfrapPerfCurrentDteUtilization = _TfrapPerfCurrentDteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 3, 2),
    _TfrapPerfCurrentDteUtilization_Type()
)
tfrapPerfCurrentDteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentDteUtilization.setStatus("mandatory")
_TfrapPerfCurrentWanUtilization_Type = Integer32
_TfrapPerfCurrentWanUtilization_Object = MibScalar
tfrapPerfCurrentWanUtilization = _TfrapPerfCurrentWanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 3, 3),
    _TfrapPerfCurrentWanUtilization_Type()
)
tfrapPerfCurrentWanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentWanUtilization.setStatus("mandatory")
_TfrapPerfCurrentAggregateUtilization_Type = Integer32
_TfrapPerfCurrentAggregateUtilization_Object = MibScalar
tfrapPerfCurrentAggregateUtilization = _TfrapPerfCurrentAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 5, 6, 3, 4),
    _TfrapPerfCurrentAggregateUtilization_Type()
)
tfrapPerfCurrentAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPerfCurrentAggregateUtilization.setStatus("mandatory")


class _TfrapAlarmType_Type(Integer32):
    """Custom type tfrapAlarmType based on Integer32"""
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
              136,
              137,
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
          ("config-install-success", 142),
          ("config-local-update", 2),
          ("csu-loop-down-completed", 35),
          ("csu-loop-up-initiated", 34),
          ("csu-loopback-disabled-by-remote", 37),
          ("csu-loopback-enabled-by-remote", 36),
          ("csu-loopback-failure", 38),
          ("dlci-active", 47),
          ("dlci-inactive", 48),
          ("dlci-td-threshold", 49),
          ("dsu-loop-down-completed", 40),
          ("dsu-loop-up-initiated", 39),
          ("dsu-loopback-disabled-by-remote", 42),
          ("dsu-loopback-enabled-by-remote", 41),
          ("dsu-loopback-failure", 43),
          ("dte-signal-dtr-off", 58),
          ("dte-signal-dtr-on", 57),
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
          ("local-aggregate-loopback-disabled", 21),
          ("local-aggregate-loopback-enabled", 20),
          ("local-aggregate-loopback-failure", 22),
          ("local-dte-loopback-disabled", 18),
          ("local-dte-loopback-enabled", 17),
          ("local-dte-loopback-failure", 19),
          ("local-network-loopback-disabled", 27),
          ("local-network-loopback-enabled", 26),
          ("local-network-loopback-failure", 28),
          ("local-payload-loopback-disabled", 24),
          ("local-payload-loopback-enabled", 23),
          ("local-payload-loopback-failure", 25),
          ("local-payload-loopback-via-rmt-disabled", 137),
          ("local-payload-loopback-via-rmt-enabled", 136),
          ("local-unit-loopback-disabled", 15),
          ("local-unit-loopback-enabled", 14),
          ("local-unit-loopback-failure", 16),
          ("pvc-rx-utilization-cleared", 140),
          ("pvc-rx-utilization-exceeded", 138),
          ("pvc-tx-utilization-cleared", 141),
          ("pvc-tx-utilization-exceeded", 139),
          ("t1-controlled-slip", 13),
          ("t1-netw-ais-clear", 12),
          ("t1-netw-ais-detect", 11),
          ("t1-netw-carrier-detect", 4),
          ("t1-netw-carrier-loss", 3),
          ("t1-netw-red-alarm-clear", 8),
          ("t1-netw-red-alarm-declare", 7),
          ("t1-netw-sync-acquire", 6),
          ("t1-netw-sync-loss-declare", 5),
          ("t1-netw-yellow-alarm-clear", 10),
          ("t1-netw-yellow-alarm-detect", 9),
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


_TfrapAlarmType_Type.__name__ = "Integer32"
_TfrapAlarmType_Object = MibScalar
tfrapAlarmType = _TfrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 6),
    _TfrapAlarmType_Type()
)
tfrapAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapAlarmType.setStatus("mandatory")
_TfrapDLCINum_Type = Integer32
_TfrapDLCINum_Object = MibScalar
tfrapDLCINum = _TfrapDLCINum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 7),
    _TfrapDLCINum_Type()
)
tfrapDLCINum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapDLCINum.setStatus("mandatory")


class _TfrapInterface_Type(Integer32):
    """Custom type tfrapInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dte", 1),
          ("t1", 2))
    )


_TfrapInterface_Type.__name__ = "Integer32"
_TfrapInterface_Object = MibScalar
tfrapInterface = _TfrapInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 8),
    _TfrapInterface_Type()
)
tfrapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapInterface.setStatus("mandatory")
_TfrapIpAddress_Type = IpAddress
_TfrapIpAddress_Object = MibScalar
tfrapIpAddress = _TfrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 9),
    _TfrapIpAddress_Type()
)
tfrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapIpAddress.setStatus("mandatory")
_TfrapEventTrapLog_ObjectIdentity = ObjectIdentity
tfrapEventTrapLog = _TfrapEventTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 5, 10)
)
_TfrapEventTrapLogTable_Object = MibTable
tfrapEventTrapLogTable = _TfrapEventTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1)
)
if mibBuilder.loadTexts:
    tfrapEventTrapLogTable.setStatus("mandatory")
_TfrapEventTrapLogEntry_Object = MibTableRow
tfrapEventTrapLogEntry = _TfrapEventTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1)
)
tfrapEventTrapLogEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapEventTrapLogSeqNum"),
)
if mibBuilder.loadTexts:
    tfrapEventTrapLogEntry.setStatus("mandatory")
_TfrapEventTrapLogSeqNum_Type = Integer32
_TfrapEventTrapLogSeqNum_Object = MibTableColumn
tfrapEventTrapLogSeqNum = _TfrapEventTrapLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 1),
    _TfrapEventTrapLogSeqNum_Type()
)
tfrapEventTrapLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogSeqNum.setStatus("mandatory")
_TfrapEventTrapLogGenericEvent_Type = Integer32
_TfrapEventTrapLogGenericEvent_Object = MibTableColumn
tfrapEventTrapLogGenericEvent = _TfrapEventTrapLogGenericEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 2),
    _TfrapEventTrapLogGenericEvent_Type()
)
tfrapEventTrapLogGenericEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogGenericEvent.setStatus("mandatory")
_TfrapEventTrapLogSpecificEvent_Type = Integer32
_TfrapEventTrapLogSpecificEvent_Object = MibTableColumn
tfrapEventTrapLogSpecificEvent = _TfrapEventTrapLogSpecificEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 3),
    _TfrapEventTrapLogSpecificEvent_Type()
)
tfrapEventTrapLogSpecificEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogSpecificEvent.setStatus("mandatory")
_TfrapEventTrapLogTimeStamp_Type = TimeTicks
_TfrapEventTrapLogTimeStamp_Object = MibTableColumn
tfrapEventTrapLogTimeStamp = _TfrapEventTrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 4),
    _TfrapEventTrapLogTimeStamp_Type()
)
tfrapEventTrapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogTimeStamp.setStatus("mandatory")
_TfrapEventTrapLogVarBind1_Type = Integer32
_TfrapEventTrapLogVarBind1_Object = MibTableColumn
tfrapEventTrapLogVarBind1 = _TfrapEventTrapLogVarBind1_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 5),
    _TfrapEventTrapLogVarBind1_Type()
)
tfrapEventTrapLogVarBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogVarBind1.setStatus("mandatory")
_TfrapEventTrapLogVarBind2_Type = Integer32
_TfrapEventTrapLogVarBind2_Object = MibTableColumn
tfrapEventTrapLogVarBind2 = _TfrapEventTrapLogVarBind2_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 6),
    _TfrapEventTrapLogVarBind2_Type()
)
tfrapEventTrapLogVarBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogVarBind2.setStatus("mandatory")
_TfrapEventTrapLogVarBind3_Type = Integer32
_TfrapEventTrapLogVarBind3_Object = MibTableColumn
tfrapEventTrapLogVarBind3 = _TfrapEventTrapLogVarBind3_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 1, 1, 7),
    _TfrapEventTrapLogVarBind3_Type()
)
tfrapEventTrapLogVarBind3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventTrapLogVarBind3.setStatus("mandatory")
_TfrapEventLogAltTable_Object = MibTable
tfrapEventLogAltTable = _TfrapEventLogAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 2)
)
if mibBuilder.loadTexts:
    tfrapEventLogAltTable.setStatus("mandatory")
_TfrapEventLogAltEntry_Object = MibTableRow
tfrapEventLogAltEntry = _TfrapEventLogAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 2, 1)
)
tfrapEventLogAltEntry.setIndexNames(
    (0, "TFRAP-MIB", "tfrapEventLogAltSeqNum"),
)
if mibBuilder.loadTexts:
    tfrapEventLogAltEntry.setStatus("mandatory")
_TfrapEventLogAltSeqNum_Type = Integer32
_TfrapEventLogAltSeqNum_Object = MibTableColumn
tfrapEventLogAltSeqNum = _TfrapEventLogAltSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 2, 1, 1),
    _TfrapEventLogAltSeqNum_Type()
)
tfrapEventLogAltSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventLogAltSeqNum.setStatus("mandatory")
_TfrapEventLogAltArray_Type = OctetString
_TfrapEventLogAltArray_Object = MibTableColumn
tfrapEventLogAltArray = _TfrapEventLogAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 2, 1, 2),
    _TfrapEventLogAltArray_Type()
)
tfrapEventLogAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventLogAltArray.setStatus("mandatory")
_TfrapEventLogCurrentSeqNum_Type = Integer32
_TfrapEventLogCurrentSeqNum_Object = MibScalar
tfrapEventLogCurrentSeqNum = _TfrapEventLogCurrentSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 3),
    _TfrapEventLogCurrentSeqNum_Type()
)
tfrapEventLogCurrentSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapEventLogCurrentSeqNum.setStatus("mandatory")


class _TfrapEventLogFreeze_Type(Integer32):
    """Custom type tfrapEventLogFreeze based on Integer32"""
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


_TfrapEventLogFreeze_Type.__name__ = "Integer32"
_TfrapEventLogFreeze_Object = MibScalar
tfrapEventLogFreeze = _TfrapEventLogFreeze_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 4),
    _TfrapEventLogFreeze_Type()
)
tfrapEventLogFreeze.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapEventLogFreeze.setStatus("mandatory")


class _TfrapEventLogClear_Type(Integer32):
    """Custom type tfrapEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TfrapEventLogClear_Type.__name__ = "Integer32"
_TfrapEventLogClear_Object = MibScalar
tfrapEventLogClear = _TfrapEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 10, 5),
    _TfrapEventLogClear_Type()
)
tfrapEventLogClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tfrapEventLogClear.setStatus("mandatory")
_TfrapPercentUtilization_Type = Integer32
_TfrapPercentUtilization_Object = MibScalar
tfrapPercentUtilization = _TfrapPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 11),
    _TfrapPercentUtilization_Type()
)
tfrapPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapPercentUtilization.setStatus("mandatory")
_TfrapUtilizationThreshold_Type = Integer32
_TfrapUtilizationThreshold_Object = MibScalar
tfrapUtilizationThreshold = _TfrapUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 12),
    _TfrapUtilizationThreshold_Type()
)
tfrapUtilizationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapUtilizationThreshold.setStatus("mandatory")
_TfrapCfgLockIpAddress_Type = IpAddress
_TfrapCfgLockIpAddress_Object = MibScalar
tfrapCfgLockIpAddress = _TfrapCfgLockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 5, 13),
    _TfrapCfgLockIpAddress_Type()
)
tfrapCfgLockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfrapCfgLockIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tfrapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 0)
)
tfrapTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTrap.setStatus(
        ""
    )

tfrapBadConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 1)
)
tfrapBadConfigTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapBadConfigTrap.setStatus(
        ""
    )

tfrapLocalConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 2)
)
tfrapLocalConfigTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalConfigTrap.setStatus(
        ""
    )

tfrapt1netwcarrierloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 3)
)
tfrapt1netwcarrierloss.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwcarrierloss.setStatus(
        ""
    )

tfrapt1netwcarrierdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 4)
)
tfrapt1netwcarrierdetect.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwcarrierdetect.setStatus(
        ""
    )

tfrapt1netwsynclossdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 5)
)
tfrapt1netwsynclossdeclare.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwsynclossdeclare.setStatus(
        ""
    )

tfrapt1netwsyncacquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 6)
)
tfrapt1netwsyncacquire.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwsyncacquire.setStatus(
        ""
    )

tfrapt1netwredalarmdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 7)
)
tfrapt1netwredalarmdeclare.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwredalarmdeclare.setStatus(
        ""
    )

tfrapt1netwredalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 8)
)
tfrapt1netwredalarmclear.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwredalarmclear.setStatus(
        ""
    )

tfrapt1netwyellowalarmdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 9)
)
tfrapt1netwyellowalarmdetect.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwyellowalarmdetect.setStatus(
        ""
    )

tfrapt1netwyellowalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 10)
)
tfrapt1netwyellowalarmclear.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwyellowalarmclear.setStatus(
        ""
    )

tfrapt1netwaisdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 11)
)
tfrapt1netwaisdetect.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwaisdetect.setStatus(
        ""
    )

tfrapt1netwaisclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 12)
)
tfrapt1netwaisclear.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1netwaisclear.setStatus(
        ""
    )

tfrapt1controlledslip = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 13)
)
tfrapt1controlledslip.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapt1controlledslip.setStatus(
        ""
    )

tfrapLocalUnitLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 14)
)
tfrapLocalUnitLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalUnitLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapLocalUnitLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 15)
)
tfrapLocalUnitLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalUnitLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapLocalUnitLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 16)
)
tfrapLocalUnitLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalUnitLoopbackFailedTrap.setStatus(
        ""
    )

tfrapLocalDteLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 17)
)
tfrapLocalDteLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalDteLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapLocalDteLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 18)
)
tfrapLocalDteLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalDteLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapLocalDteLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 19)
)
tfrapLocalDteLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalDteLoopbackFailedTrap.setStatus(
        ""
    )

tfrapLocalAggregateLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 20)
)
tfrapLocalAggregateLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalAggregateLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapLocalAggregateLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 21)
)
tfrapLocalAggregateLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalAggregateLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapLocalAggregateLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 22)
)
tfrapLocalAggregateLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalAggregateLoopbackFailedTrap.setStatus(
        ""
    )

tfrapLocalPayloadLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 23)
)
tfrapLocalPayloadLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalPayloadLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapLocalPayloadLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 24)
)
tfrapLocalPayloadLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalPayloadLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapLocalPayloadLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 25)
)
tfrapLocalPayloadLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalPayloadLoopbackFailedTrap.setStatus(
        ""
    )

tfrapLocalNetLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 26)
)
tfrapLocalNetLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalNetLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapLocalNetLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 27)
)
tfrapLocalNetLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalNetLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapLocalNetLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 28)
)
tfrapLocalNetLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalNetLoopbackFailedTrap.setStatus(
        ""
    )

tfrapV54LoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 29)
)
tfrapV54LoopUpInitiatedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapV54LoopUpInitiatedTrap.setStatus(
        ""
    )

tfrapV54LoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 30)
)
tfrapV54LoopDownCompletedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapV54LoopDownCompletedTrap.setStatus(
        ""
    )

tfrapV54LoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 31)
)
tfrapV54LoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapV54LoopbackEnabledTrap.setStatus(
        ""
    )

tfrapV54LoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 32)
)
tfrapV54LoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapV54LoopbackDisabledTrap.setStatus(
        ""
    )

tfrapV54LoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 33)
)
tfrapV54LoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapV54LoopbackFailedTrap.setStatus(
        ""
    )

tfrapCsuLoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 34)
)
tfrapCsuLoopUpInitiatedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapCsuLoopUpInitiatedTrap.setStatus(
        ""
    )

tfrapCsuLoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 35)
)
tfrapCsuLoopDownCompletedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapCsuLoopDownCompletedTrap.setStatus(
        ""
    )

tfrapCsuLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 36)
)
tfrapCsuLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapCsuLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapCsuLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 37)
)
tfrapCsuLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapCsuLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapCsuLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 38)
)
tfrapCsuLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapCsuLoopbackFailedTrap.setStatus(
        ""
    )

tfrapDsuLoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 39)
)
tfrapDsuLoopUpInitiatedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDsuLoopUpInitiatedTrap.setStatus(
        ""
    )

tfrapDsuLoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 40)
)
tfrapDsuLoopDownCompletedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDsuLoopDownCompletedTrap.setStatus(
        ""
    )

tfrapDsuLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 41)
)
tfrapDsuLoopbackEnabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDsuLoopbackEnabledTrap.setStatus(
        ""
    )

tfrapDsuLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 42)
)
tfrapDsuLoopbackDisabledTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDsuLoopbackDisabledTrap.setStatus(
        ""
    )

tfrapDsuLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 43)
)
tfrapDsuLoopbackFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDsuLoopbackFailedTrap.setStatus(
        ""
    )

tfrapBertInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 44)
)
tfrapBertInitiatedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapBertInitiatedTrap.setStatus(
        ""
    )

tfrapBertCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 45)
)
tfrapBertCompletedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapBertCompletedTrap.setStatus(
        ""
    )

tfrapBertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 46)
)
tfrapBertFailedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapBertFailedTrap.setStatus(
        ""
    )

tfrapDLCIActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 47)
)
tfrapDLCIActiveTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"))
)
if mibBuilder.loadTexts:
    tfrapDLCIActiveTrap.setStatus(
        ""
    )

tfrapDLCIInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 48)
)
tfrapDLCIInactiveTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"))
)
if mibBuilder.loadTexts:
    tfrapDLCIInactiveTrap.setStatus(
        ""
    )

tfrapDLCITDThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 49)
)
tfrapDLCITDThresholdTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapIpAddress"))
)
if mibBuilder.loadTexts:
    tfrapDLCITDThresholdTrap.setStatus(
        ""
    )

tfrapLmiSourcingChangePassthruTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 50)
)
tfrapLmiSourcingChangePassthruTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSourcingChangePassthruTrap.setStatus(
        ""
    )

tfrapLmiSourcingChangeUserDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 51)
)
tfrapLmiSourcingChangeUserDteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSourcingChangeUserDteTrap.setStatus(
        ""
    )

tfrapLmiSourcingChangeNetDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 52)
)
tfrapLmiSourcingChangeNetDteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSourcingChangeNetDteTrap.setStatus(
        ""
    )

tfrapLmiSourcingChangeUserT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 53)
)
tfrapLmiSourcingChangeUserT1Trap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSourcingChangeUserT1Trap.setStatus(
        ""
    )

tfrapLmiSourcingChangeNetT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 54)
)
tfrapLmiSourcingChangeNetT1Trap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSourcingChangeNetT1Trap.setStatus(
        ""
    )

tfrapDteSignalRtsOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 55)
)
tfrapDteSignalRtsOnTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDteSignalRtsOnTrap.setStatus(
        ""
    )

tfrapDteSignalRtsOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 56)
)
tfrapDteSignalRtsOffTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDteSignalRtsOffTrap.setStatus(
        ""
    )

tfrapDteSignalDtrOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 57)
)
tfrapDteSignalDtrOnTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDteSignalDtrOnTrap.setStatus(
        ""
    )

tfrapDteSignalDtrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 58)
)
tfrapDteSignalDtrOffTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapDteSignalDtrOffTrap.setStatus(
        ""
    )

tfrapNonIncrLmiSeqNumDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 59)
)
tfrapNonIncrLmiSeqNumDteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapNonIncrLmiSeqNumDteTrap.setStatus(
        ""
    )

tfrapNonIncrLmiSeqNumT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 60)
)
tfrapNonIncrLmiSeqNumT1Trap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapNonIncrLmiSeqNumT1Trap.setStatus(
        ""
    )

tfrapLmiSeqNumMismatchDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 61)
)
tfrapLmiSeqNumMismatchDteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSeqNumMismatchDteTrap.setStatus(
        ""
    )

tfrapLmiSeqNumMismatchT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 62)
)
tfrapLmiSeqNumMismatchT1Trap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLmiSeqNumMismatchT1Trap.setStatus(
        ""
    )

tfrapTrapMutingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 75)
)
tfrapTrapMutingActive.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTrapMutingActive.setStatus(
        ""
    )

tfrapTrapMutingInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 76)
)
tfrapTrapMutingInactive.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTrapMutingInactive.setStatus(
        ""
    )

tfrapVloopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 90)
)
tfrapVloopUp.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVloopUp.setStatus(
        ""
    )

tfrapVloopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 91)
)
tfrapVloopDown.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVloopDown.setStatus(
        ""
    )

tfrapVloopUpViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 92)
)
tfrapVloopUpViaRemote.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVloopUpViaRemote.setStatus(
        ""
    )

tfrapVloopDownViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 93)
)
tfrapVloopDownViaRemote.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVloopDownViaRemote.setStatus(
        ""
    )

tfrapVloopRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 94)
)
tfrapVloopRequestFailed.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVloopRequestFailed.setStatus(
        ""
    )

tfrapVbertStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 95)
)
tfrapVbertStarted.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVbertStarted.setStatus(
        ""
    )

tfrapVbertStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 96)
)
tfrapVbertStopped.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVbertStopped.setStatus(
        ""
    )

tfrapVbertRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 97)
)
tfrapVbertRequestFailed.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapInterface"))
)
if mibBuilder.loadTexts:
    tfrapVbertRequestFailed.setStatus(
        ""
    )

tfrapLocalPayloadLoopbackEnabledViaRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 136)
)
tfrapLocalPayloadLoopbackEnabledViaRemoteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalPayloadLoopbackEnabledViaRemoteTrap.setStatus(
        ""
    )

tfrapLocalPayloadLoopbackDisabledViaRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 137)
)
tfrapLocalPayloadLoopbackDisabledViaRemoteTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapLocalPayloadLoopbackDisabledViaRemoteTrap.setStatus(
        ""
    )

tfrapPvcRxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 138)
)
tfrapPvcRxUtilizationExceededTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapPercentUtilization"),
        ("TFRAP-MIB", "tfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    tfrapPvcRxUtilizationExceededTrap.setStatus(
        ""
    )

tfrapPvcTxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 139)
)
tfrapPvcTxUtilizationExceededTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapPercentUtilization"),
        ("TFRAP-MIB", "tfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    tfrapPvcTxUtilizationExceededTrap.setStatus(
        ""
    )

tfrapPvcRxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 140)
)
tfrapPvcRxUtilizationClearedTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapPercentUtilization"),
        ("TFRAP-MIB", "tfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    tfrapPvcRxUtilizationClearedTrap.setStatus(
        ""
    )

tfrapPvcTxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 141)
)
tfrapPvcTxUtilizationClearedTrap.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapDLCINum"),
        ("TFRAP-MIB", "tfrapPercentUtilization"),
        ("TFRAP-MIB", "tfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    tfrapPvcTxUtilizationClearedTrap.setStatus(
        ""
    )

tfrapConfigInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 142)
)
tfrapConfigInstallSuccess.setObjects(
      *(("TFRAP-MIB", "tfrapAlarmType"),
        ("TFRAP-MIB", "tfrapCfgLockIpAddress"))
)
if mibBuilder.loadTexts:
    tfrapConfigInstallSuccess.setStatus(
        ""
    )

tfrapTftpRequestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 257)
)
tfrapTftpRequestedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpRequestedTrap.setStatus(
        ""
    )

tfrapTftpTransferringTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 258)
)
tfrapTftpTransferringTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpTransferringTrap.setStatus(
        ""
    )

tfrapTftpProgrammingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 259)
)
tfrapTftpProgrammingTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpProgrammingTrap.setStatus(
        ""
    )

tfrapTftpAbortedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 260)
)
tfrapTftpAbortedTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpAbortedTrap.setStatus(
        ""
    )

tfrapTftpSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 261)
)
tfrapTftpSuccessTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpSuccessTrap.setStatus(
        ""
    )

tfrapTftpHostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 262)
)
tfrapTftpHostUnreachableTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpHostUnreachableTrap.setStatus(
        ""
    )

tfrapTftpNoFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 263)
)
tfrapTftpNoFileTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpNoFileTrap.setStatus(
        ""
    )

tfrapTftpInvalidFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 264)
)
tfrapTftpInvalidFileTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpInvalidFileTrap.setStatus(
        ""
    )

tfrapTftpCorruptFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 5, 0, 265)
)
tfrapTftpCorruptFileTrap.setObjects(
    ("TFRAP-MIB", "tfrapAlarmType")
)
if mibBuilder.loadTexts:
    tfrapTftpCorruptFileTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TFRAP-MIB",
    **{"Index": Index,
       "private": private,
       "enterprises": enterprises,
       "sync": sync,
       "tfrap": tfrap,
       "tfrapTrap": tfrapTrap,
       "tfrapBadConfigTrap": tfrapBadConfigTrap,
       "tfrapLocalConfigTrap": tfrapLocalConfigTrap,
       "tfrapt1netwcarrierloss": tfrapt1netwcarrierloss,
       "tfrapt1netwcarrierdetect": tfrapt1netwcarrierdetect,
       "tfrapt1netwsynclossdeclare": tfrapt1netwsynclossdeclare,
       "tfrapt1netwsyncacquire": tfrapt1netwsyncacquire,
       "tfrapt1netwredalarmdeclare": tfrapt1netwredalarmdeclare,
       "tfrapt1netwredalarmclear": tfrapt1netwredalarmclear,
       "tfrapt1netwyellowalarmdetect": tfrapt1netwyellowalarmdetect,
       "tfrapt1netwyellowalarmclear": tfrapt1netwyellowalarmclear,
       "tfrapt1netwaisdetect": tfrapt1netwaisdetect,
       "tfrapt1netwaisclear": tfrapt1netwaisclear,
       "tfrapt1controlledslip": tfrapt1controlledslip,
       "tfrapLocalUnitLoopbackEnabledTrap": tfrapLocalUnitLoopbackEnabledTrap,
       "tfrapLocalUnitLoopbackDisabledTrap": tfrapLocalUnitLoopbackDisabledTrap,
       "tfrapLocalUnitLoopbackFailedTrap": tfrapLocalUnitLoopbackFailedTrap,
       "tfrapLocalDteLoopbackEnabledTrap": tfrapLocalDteLoopbackEnabledTrap,
       "tfrapLocalDteLoopbackDisabledTrap": tfrapLocalDteLoopbackDisabledTrap,
       "tfrapLocalDteLoopbackFailedTrap": tfrapLocalDteLoopbackFailedTrap,
       "tfrapLocalAggregateLoopbackEnabledTrap": tfrapLocalAggregateLoopbackEnabledTrap,
       "tfrapLocalAggregateLoopbackDisabledTrap": tfrapLocalAggregateLoopbackDisabledTrap,
       "tfrapLocalAggregateLoopbackFailedTrap": tfrapLocalAggregateLoopbackFailedTrap,
       "tfrapLocalPayloadLoopbackEnabledTrap": tfrapLocalPayloadLoopbackEnabledTrap,
       "tfrapLocalPayloadLoopbackDisabledTrap": tfrapLocalPayloadLoopbackDisabledTrap,
       "tfrapLocalPayloadLoopbackFailedTrap": tfrapLocalPayloadLoopbackFailedTrap,
       "tfrapLocalNetLoopbackEnabledTrap": tfrapLocalNetLoopbackEnabledTrap,
       "tfrapLocalNetLoopbackDisabledTrap": tfrapLocalNetLoopbackDisabledTrap,
       "tfrapLocalNetLoopbackFailedTrap": tfrapLocalNetLoopbackFailedTrap,
       "tfrapV54LoopUpInitiatedTrap": tfrapV54LoopUpInitiatedTrap,
       "tfrapV54LoopDownCompletedTrap": tfrapV54LoopDownCompletedTrap,
       "tfrapV54LoopbackEnabledTrap": tfrapV54LoopbackEnabledTrap,
       "tfrapV54LoopbackDisabledTrap": tfrapV54LoopbackDisabledTrap,
       "tfrapV54LoopbackFailedTrap": tfrapV54LoopbackFailedTrap,
       "tfrapCsuLoopUpInitiatedTrap": tfrapCsuLoopUpInitiatedTrap,
       "tfrapCsuLoopDownCompletedTrap": tfrapCsuLoopDownCompletedTrap,
       "tfrapCsuLoopbackEnabledTrap": tfrapCsuLoopbackEnabledTrap,
       "tfrapCsuLoopbackDisabledTrap": tfrapCsuLoopbackDisabledTrap,
       "tfrapCsuLoopbackFailedTrap": tfrapCsuLoopbackFailedTrap,
       "tfrapDsuLoopUpInitiatedTrap": tfrapDsuLoopUpInitiatedTrap,
       "tfrapDsuLoopDownCompletedTrap": tfrapDsuLoopDownCompletedTrap,
       "tfrapDsuLoopbackEnabledTrap": tfrapDsuLoopbackEnabledTrap,
       "tfrapDsuLoopbackDisabledTrap": tfrapDsuLoopbackDisabledTrap,
       "tfrapDsuLoopbackFailedTrap": tfrapDsuLoopbackFailedTrap,
       "tfrapBertInitiatedTrap": tfrapBertInitiatedTrap,
       "tfrapBertCompletedTrap": tfrapBertCompletedTrap,
       "tfrapBertFailedTrap": tfrapBertFailedTrap,
       "tfrapDLCIActiveTrap": tfrapDLCIActiveTrap,
       "tfrapDLCIInactiveTrap": tfrapDLCIInactiveTrap,
       "tfrapDLCITDThresholdTrap": tfrapDLCITDThresholdTrap,
       "tfrapLmiSourcingChangePassthruTrap": tfrapLmiSourcingChangePassthruTrap,
       "tfrapLmiSourcingChangeUserDteTrap": tfrapLmiSourcingChangeUserDteTrap,
       "tfrapLmiSourcingChangeNetDteTrap": tfrapLmiSourcingChangeNetDteTrap,
       "tfrapLmiSourcingChangeUserT1Trap": tfrapLmiSourcingChangeUserT1Trap,
       "tfrapLmiSourcingChangeNetT1Trap": tfrapLmiSourcingChangeNetT1Trap,
       "tfrapDteSignalRtsOnTrap": tfrapDteSignalRtsOnTrap,
       "tfrapDteSignalRtsOffTrap": tfrapDteSignalRtsOffTrap,
       "tfrapDteSignalDtrOnTrap": tfrapDteSignalDtrOnTrap,
       "tfrapDteSignalDtrOffTrap": tfrapDteSignalDtrOffTrap,
       "tfrapNonIncrLmiSeqNumDteTrap": tfrapNonIncrLmiSeqNumDteTrap,
       "tfrapNonIncrLmiSeqNumT1Trap": tfrapNonIncrLmiSeqNumT1Trap,
       "tfrapLmiSeqNumMismatchDteTrap": tfrapLmiSeqNumMismatchDteTrap,
       "tfrapLmiSeqNumMismatchT1Trap": tfrapLmiSeqNumMismatchT1Trap,
       "tfrapTrapMutingActive": tfrapTrapMutingActive,
       "tfrapTrapMutingInactive": tfrapTrapMutingInactive,
       "tfrapVloopUp": tfrapVloopUp,
       "tfrapVloopDown": tfrapVloopDown,
       "tfrapVloopUpViaRemote": tfrapVloopUpViaRemote,
       "tfrapVloopDownViaRemote": tfrapVloopDownViaRemote,
       "tfrapVloopRequestFailed": tfrapVloopRequestFailed,
       "tfrapVbertStarted": tfrapVbertStarted,
       "tfrapVbertStopped": tfrapVbertStopped,
       "tfrapVbertRequestFailed": tfrapVbertRequestFailed,
       "tfrapLocalPayloadLoopbackEnabledViaRemoteTrap": tfrapLocalPayloadLoopbackEnabledViaRemoteTrap,
       "tfrapLocalPayloadLoopbackDisabledViaRemoteTrap": tfrapLocalPayloadLoopbackDisabledViaRemoteTrap,
       "tfrapPvcRxUtilizationExceededTrap": tfrapPvcRxUtilizationExceededTrap,
       "tfrapPvcTxUtilizationExceededTrap": tfrapPvcTxUtilizationExceededTrap,
       "tfrapPvcRxUtilizationClearedTrap": tfrapPvcRxUtilizationClearedTrap,
       "tfrapPvcTxUtilizationClearedTrap": tfrapPvcTxUtilizationClearedTrap,
       "tfrapConfigInstallSuccess": tfrapConfigInstallSuccess,
       "tfrapTftpRequestedTrap": tfrapTftpRequestedTrap,
       "tfrapTftpTransferringTrap": tfrapTftpTransferringTrap,
       "tfrapTftpProgrammingTrap": tfrapTftpProgrammingTrap,
       "tfrapTftpAbortedTrap": tfrapTftpAbortedTrap,
       "tfrapTftpSuccessTrap": tfrapTftpSuccessTrap,
       "tfrapTftpHostUnreachableTrap": tfrapTftpHostUnreachableTrap,
       "tfrapTftpNoFileTrap": tfrapTftpNoFileTrap,
       "tfrapTftpInvalidFileTrap": tfrapTftpInvalidFileTrap,
       "tfrapTftpCorruptFileTrap": tfrapTftpCorruptFileTrap,
       "tfrapSystem": tfrapSystem,
       "tfrapSysTable": tfrapSysTable,
       "tfrapSysType": tfrapSysType,
       "tfrapSysSoftRev": tfrapSysSoftRev,
       "tfrapSysHardRev": tfrapSysHardRev,
       "tfrapSysNumT1Installed": tfrapSysNumT1Installed,
       "tfrapSysNumDteInstalled": tfrapSysNumDteInstalled,
       "tfrapSysNumMaintInstalled": tfrapSysNumMaintInstalled,
       "tfrapSysName": tfrapSysName,
       "tfrapSysSerialNo": tfrapSysSerialNo,
       "tfrapSysResetNode": tfrapSysResetNode,
       "tfrapSysAmtMemoryInstalled": tfrapSysAmtMemoryInstalled,
       "tfrapSysLocation": tfrapSysLocation,
       "tfrapSysContact": tfrapSysContact,
       "tfrapSysPrompt": tfrapSysPrompt,
       "tfrapSysBootRev": tfrapSysBootRev,
       "tfrapSysFeatureTable": tfrapSysFeatureTable,
       "tfrapSysSLIPSupported": tfrapSysSLIPSupported,
       "tfrapSysPPPSupported": tfrapSysPPPSupported,
       "tfrapSysRDOSupported": tfrapSysRDOSupported,
       "tfrapSysETHSupported": tfrapSysETHSupported,
       "tfrapSysTKRSupported": tfrapSysTKRSupported,
       "tfrapSysExtTimSupported": tfrapSysExtTimSupported,
       "tfrapSysBRISupported": tfrapSysBRISupported,
       "tfrapSysSelDTESupported": tfrapSysSelDTESupported,
       "tfrapSysMLSupported": tfrapSysMLSupported,
       "tfrapSysNumDlcisSupported": tfrapSysNumDlcisSupported,
       "tfrapSysLTFNumDlcis": tfrapSysLTFNumDlcis,
       "tfrapSysLTFNumProtocols": tfrapSysLTFNumProtocols,
       "tfrapSysNumUserProtocols": tfrapSysNumUserProtocols,
       "tfrapSysNumSnmpMgrs": tfrapSysNumSnmpMgrs,
       "tfrapSysNumDlciNames": tfrapSysNumDlciNames,
       "tfrapConfiguration": tfrapConfiguration,
       "tfrapCfgMgmtTable": tfrapCfgMgmtTable,
       "tfrapCfgIpTable": tfrapCfgIpTable,
       "tfrapCfgIpMyIP": tfrapCfgIpMyIP,
       "tfrapCfgIpPeerIP": tfrapCfgIpPeerIP,
       "tfrapCfgIpMask": tfrapCfgIpMask,
       "tfrapCfgIpMaxMTU": tfrapCfgIpMaxMTU,
       "tfrapCfgIpChannel": tfrapCfgIpChannel,
       "tfrapCfgIpTelnetEnable": tfrapCfgIpTelnetEnable,
       "tfrapCfgIpTelnetAutoLogOut": tfrapCfgIpTelnetAutoLogOut,
       "tfrapCfgTftpTable": tfrapCfgTftpTable,
       "tfrapCfgTftpInitiate": tfrapCfgTftpInitiate,
       "tfrapCfgTftpIpAddress": tfrapCfgTftpIpAddress,
       "tfrapCfgTftpFilename": tfrapCfgTftpFilename,
       "tfrapCfgTftpInterface": tfrapCfgTftpInterface,
       "tfrapCfgTftpDlci": tfrapCfgTftpDlci,
       "tfrapCfgTftpStatus": tfrapCfgTftpStatus,
       "tfrapCfgTftpNumBytes": tfrapCfgTftpNumBytes,
       "tfrapCfgSnmpTable": tfrapCfgSnmpTable,
       "tfrapCfgSnmpFrTrap": tfrapCfgSnmpFrTrap,
       "tfrapCfgSnmpMgrTable": tfrapCfgSnmpMgrTable,
       "tfrapCfgSnmpMgrEntry": tfrapCfgSnmpMgrEntry,
       "tfrapCfgSnmpMgrIndex": tfrapCfgSnmpMgrIndex,
       "tfrapCfgSnmpMgrIP": tfrapCfgSnmpMgrIP,
       "tfrapCfgSnmpMgrInterface": tfrapCfgSnmpMgrInterface,
       "tfrapCfgSnmpMgrDlci": tfrapCfgSnmpMgrDlci,
       "tfrapCfgSnmpTrapMuting": tfrapCfgSnmpTrapMuting,
       "tfrapCfgSnmpUtilTrapEnable": tfrapCfgSnmpUtilTrapEnable,
       "tfrapCfgSnmpMgrClearN": tfrapCfgSnmpMgrClearN,
       "tfrapCfgCommTable": tfrapCfgCommTable,
       "tfrapCfgCommMode": tfrapCfgCommMode,
       "tfrapCfgCommBaud": tfrapCfgCommBaud,
       "tfrapCfgCommDataBits": tfrapCfgCommDataBits,
       "tfrapCfgCommStopBits": tfrapCfgCommStopBits,
       "tfrapCfgCommParity": tfrapCfgCommParity,
       "tfrapCfgCommFlowCtrl": tfrapCfgCommFlowCtrl,
       "tfrapCfgFrDLCITable": tfrapCfgFrDLCITable,
       "tfrapCfgFrDLCIMode": tfrapCfgFrDLCIMode,
       "tfrapCfgFrDLCIValue": tfrapCfgFrDLCIValue,
       "tfrapCfgFrDLCIEncap": tfrapCfgFrDLCIEncap,
       "tfrapCfgFrDLCIMgmtDE": tfrapCfgFrDLCIMgmtDE,
       "tfrapCfgAppTable": tfrapCfgAppTable,
       "tfrapCfgAppClockSource": tfrapCfgAppClockSource,
       "tfrapCfgAppCircuitId": tfrapCfgAppCircuitId,
       "tfrapCfgAppType": tfrapCfgAppType,
       "tfrapCfgAppFormat": tfrapCfgAppFormat,
       "tfrapCfgAppLpbkTimeout": tfrapCfgAppLpbkTimeout,
       "tfrapCfgAppPerfBuffLimit": tfrapCfgAppPerfBuffLimit,
       "tfrapCfgT1Table": tfrapCfgT1Table,
       "tfrapCfgT1Framing": tfrapCfgT1Framing,
       "tfrapCfgT1LineEncoding": tfrapCfgT1LineEncoding,
       "tfrapCfgT1Density": tfrapCfgT1Density,
       "tfrapCfgT1Interface": tfrapCfgT1Interface,
       "tfrapCfgT1LboSetting": tfrapCfgT1LboSetting,
       "tfrapCfgDteTable": tfrapCfgDteTable,
       "tfrapCfgDteIntfType": tfrapCfgDteIntfType,
       "tfrapCfgDteDataMode": tfrapCfgDteDataMode,
       "tfrapCfgDteClockMode": tfrapCfgDteClockMode,
       "tfrapCfgDteTiming": tfrapCfgDteTiming,
       "tfrapCfgDteLineRate": tfrapCfgDteLineRate,
       "tfrapCfgDteChannelDensity": tfrapCfgDteChannelDensity,
       "tfrapCfgDteStartDs0": tfrapCfgDteStartDs0,
       "tfrapCfgDteConnStatus": tfrapCfgDteConnStatus,
       "tfrapCfgDteConnStartDs0": tfrapCfgDteConnStartDs0,
       "tfrapCfgDteConnRate": tfrapCfgDteConnRate,
       "tfrapCfgDteConnDensity": tfrapCfgDteConnDensity,
       "tfrapCfgDteConnDs0Required": tfrapCfgDteConnDs0Required,
       "tfrapCfgDteConnAutoStatus": tfrapCfgDteConnAutoStatus,
       "tfrapCfgDteConnAutoUpdate": tfrapCfgDteConnAutoUpdate,
       "tfrapCfgDteRts": tfrapCfgDteRts,
       "tfrapCfgDteDtr": tfrapCfgDteDtr,
       "tfrapCfgDteDcdOutput": tfrapCfgDteDcdOutput,
       "tfrapCfgDteDsrOutput": tfrapCfgDteDsrOutput,
       "tfrapCfgDteCtsOutput": tfrapCfgDteCtsOutput,
       "tfrapCfgFrTable": tfrapCfgFrTable,
       "tfrapCfgFrAddrLen": tfrapCfgFrAddrLen,
       "tfrapCfgFrCrcMode": tfrapCfgFrCrcMode,
       "tfrapCfgFrLmiType": tfrapCfgFrLmiType,
       "tfrapCfgFrLmiInactivityTimeout": tfrapCfgFrLmiInactivityTimeout,
       "tfrapCfgFrLmiKeepaliveTimeout": tfrapCfgFrLmiKeepaliveTimeout,
       "tfrapCfgFrAddrResMode": tfrapCfgFrAddrResMode,
       "tfrapCfgFrAddrResInarpTimer": tfrapCfgFrAddrResInarpTimer,
       "tfrapCfgFrLmiFullStatus": tfrapCfgFrLmiFullStatus,
       "tfrapCfgFrAddrResDlcis": tfrapCfgFrAddrResDlcis,
       "tfrapCfgVnipTable": tfrapCfgVnipTable,
       "tfrapCfgVnipMode": tfrapCfgVnipMode,
       "tfrapCfgVnipInitTimer": tfrapCfgVnipInitTimer,
       "tfrapCfgVnipKeepAliveTimer": tfrapCfgVnipKeepAliveTimer,
       "tfrapCfgVnipInactivityTimer": tfrapCfgVnipInactivityTimer,
       "tfrapCfgVnipTransitDelayFrequency": tfrapCfgVnipTransitDelayFrequency,
       "tfrapCfgTransitDelayTable": tfrapCfgTransitDelayTable,
       "tfrapCfgTransitDelayEntry": tfrapCfgTransitDelayEntry,
       "tfrapCfgTransitDelayInterface": tfrapCfgTransitDelayInterface,
       "tfrapCfgTransitDelayDlciValue": tfrapCfgTransitDelayDlciValue,
       "tfrapCfgTransitDelayNumHops": tfrapCfgTransitDelayNumHops,
       "tfrapCfgTransitDelayRcvSummaryCancel": tfrapCfgTransitDelayRcvSummaryCancel,
       "tfrapCfgTransitDelayThreshold": tfrapCfgTransitDelayThreshold,
       "tfrapCfgTDDeleteTable": tfrapCfgTDDeleteTable,
       "tfrapCfgTDDeleteEntry": tfrapCfgTDDeleteEntry,
       "tfrapCfgTDDeleteInterface": tfrapCfgTDDeleteInterface,
       "tfrapCfgTDDeleteDlciValue": tfrapCfgTDDeleteDlciValue,
       "tfrapCfgTransitDelayTableClear": tfrapCfgTransitDelayTableClear,
       "tfrapCfgFrPerf": tfrapCfgFrPerf,
       "tfrapCfgFrPerfDlciNamesTable": tfrapCfgFrPerfDlciNamesTable,
       "tfrapCfgFrPerfDlciNamesEntry": tfrapCfgFrPerfDlciNamesEntry,
       "tfrapCfgFrPerfDlciNamesDlciValue": tfrapCfgFrPerfDlciNamesDlciValue,
       "tfrapCfgFrPerfDlciNamesDlciName": tfrapCfgFrPerfDlciNamesDlciName,
       "tfrapCfgFrPerfDlciNamesCirValue": tfrapCfgFrPerfDlciNamesCirValue,
       "tfrapCfgFrPerfDlciNamesCirType": tfrapCfgFrPerfDlciNamesCirType,
       "tfrapCfgFrPerfDlciNamesUtilThreshold": tfrapCfgFrPerfDlciNamesUtilThreshold,
       "tfrapCfgFrPerfDlciNamesEirValue": tfrapCfgFrPerfDlciNamesEirValue,
       "tfrapCfgFrPerfDlciNamesDelete": tfrapCfgFrPerfDlciNamesDelete,
       "tfrapCfgFrPerfTimers": tfrapCfgFrPerfTimers,
       "tfrapCfgFrPerfTimersSTInterval": tfrapCfgFrPerfTimersSTInterval,
       "tfrapCfgFrPerfTimersLTInterval": tfrapCfgFrPerfTimersLTInterval,
       "tfrapCfgFrPerfUserProtocolsTable": tfrapCfgFrPerfUserProtocolsTable,
       "tfrapCfgFrPerfUserProtocolsEntry": tfrapCfgFrPerfUserProtocolsEntry,
       "tfrapCfgFrPerfUserProtocolsIndex": tfrapCfgFrPerfUserProtocolsIndex,
       "tfrapCfgFrPerfUserProtocolsPortNum": tfrapCfgFrPerfUserProtocolsPortNum,
       "tfrapCfgFrPerfLTDlciFilterTable": tfrapCfgFrPerfLTDlciFilterTable,
       "tfrapCfgFrPerfLTDlciFilterEntry": tfrapCfgFrPerfLTDlciFilterEntry,
       "tfrapCfgFrPerfLTDlciFilterIndex": tfrapCfgFrPerfLTDlciFilterIndex,
       "tfrapCfgFrPerfLTDlciFilterDlciNum": tfrapCfgFrPerfLTDlciFilterDlciNum,
       "tfrapCfgFrPerfLTProtocolFilterTable": tfrapCfgFrPerfLTProtocolFilterTable,
       "tfrapCfgFrPerfLTProtocolFilterEntry": tfrapCfgFrPerfLTProtocolFilterEntry,
       "tfrapCfgFrPerfLTProtocolFilterIndex": tfrapCfgFrPerfLTProtocolFilterIndex,
       "tfrapCfgFrPerfLTProtocolFilterProtocol": tfrapCfgFrPerfLTProtocolFilterProtocol,
       "tfrapCfgFrPerfDlciDefaultUtilThreshold": tfrapCfgFrPerfDlciDefaultUtilThreshold,
       "tfrapCfgFrPerfDlciUtilDuration": tfrapCfgFrPerfDlciUtilDuration,
       "tfrapCfgFrPerfDlciNamesTableClear": tfrapCfgFrPerfDlciNamesTableClear,
       "tfrapCfgFrPerfUserProtocolsTableClear": tfrapCfgFrPerfUserProtocolsTableClear,
       "tfrapCfgFrPerfLTDlciFilterTableClear": tfrapCfgFrPerfLTDlciFilterTableClear,
       "tfrapCfgFrPerfLTProtocolFilterTableClear": tfrapCfgFrPerfLTProtocolFilterTableClear,
       "tfrapCfgFrPerfUnprovDlcisDelete": tfrapCfgFrPerfUnprovDlcisDelete,
       "tfrapCfgSecurityTable": tfrapCfgSecurityTable,
       "tfrapCfgTelnetCliLcdPassword": tfrapCfgTelnetCliLcdPassword,
       "tfrapCfgTftpPassword": tfrapCfgTftpPassword,
       "tfrapCfgCliPassword": tfrapCfgCliPassword,
       "tfrapCfgLcdPassword": tfrapCfgLcdPassword,
       "tfrapCfgGetCommunityString": tfrapCfgGetCommunityString,
       "tfrapCfgSetCommunityString": tfrapCfgSetCommunityString,
       "tfrapCfgLcdPswdEnable": tfrapCfgLcdPswdEnable,
       "tfrapCfgLcdPswdTimeout": tfrapCfgLcdPswdTimeout,
       "tfrapCfgLock": tfrapCfgLock,
       "tfrapCfgLockID": tfrapCfgLockID,
       "tfrapCfgID": tfrapCfgID,
       "tfrapCfgStatus": tfrapCfgStatus,
       "tfrapCfgUnlock": tfrapCfgUnlock,
       "tfrapCfgUpdate": tfrapCfgUpdate,
       "tfrapDiagnostics": tfrapDiagnostics,
       "tfrapDiagUnitTable": tfrapDiagUnitTable,
       "tfrapDiagUnitLocLoop": tfrapDiagUnitLocLoop,
       "tfrapDiagUnitReset": tfrapDiagUnitReset,
       "tfrapDiagUnitTimeRemaining": tfrapDiagUnitTimeRemaining,
       "tfrapDiagT1Table": tfrapDiagT1Table,
       "tfrapDiagT1LocLineLpbk": tfrapDiagT1LocLineLpbk,
       "tfrapDiagT1LocPylLpbk": tfrapDiagT1LocPylLpbk,
       "tfrapDiagT1LocAggrLpbk": tfrapDiagT1LocAggrLpbk,
       "tfrapDiagT1RmtLpbkStatus": tfrapDiagT1RmtLpbkStatus,
       "tfrapDiagT1RmtLpbkCmd": tfrapDiagT1RmtLpbkCmd,
       "tfrapDiagT1TimeRemaining": tfrapDiagT1TimeRemaining,
       "tfrapDiagDteTable": tfrapDiagDteTable,
       "tfrapDiagDteSigRTS": tfrapDiagDteSigRTS,
       "tfrapDiagDteSigDTR": tfrapDiagDteSigDTR,
       "tfrapDiagDteLclLpbk": tfrapDiagDteLclLpbk,
       "tfrapDiagDteV54Lpbk": tfrapDiagDteV54Lpbk,
       "tfrapDiagDteRmtV54Lpbk": tfrapDiagDteRmtV54Lpbk,
       "tfrapDiagDteBerState": tfrapDiagDteBerState,
       "tfrapDiagDteBerStatus": tfrapDiagDteBerStatus,
       "tfrapDiagDteBerErrors": tfrapDiagDteBerErrors,
       "tfrapDiagDteBerErrSec": tfrapDiagDteBerErrSec,
       "tfrapDiagDteBerTimeElaps": tfrapDiagDteBerTimeElaps,
       "tfrapDiagDteBerResyncs": tfrapDiagDteBerResyncs,
       "tfrapDiagDteBerPattern": tfrapDiagDteBerPattern,
       "tfrapDiagDteTimeRemaining": tfrapDiagDteTimeRemaining,
       "tfrapDiagVnipTable": tfrapDiagVnipTable,
       "tfrapDiagVnipEntry": tfrapDiagVnipEntry,
       "tfrapDiagVnipInterface": tfrapDiagVnipInterface,
       "tfrapDiagVnipIndex": tfrapDiagVnipIndex,
       "tfrapDiagVnipDlci": tfrapDiagVnipDlci,
       "tfrapDiagVnipIpAddr": tfrapDiagVnipIpAddr,
       "tfrapDiagVLOOP": tfrapDiagVLOOP,
       "tfrapDiagVBERT": tfrapDiagVBERT,
       "tfrapDiagVBERTRate": tfrapDiagVBERTRate,
       "tfrapDiagVBERTSize": tfrapDiagVBERTSize,
       "tfrapDiagVBERTPktPercent": tfrapDiagVBERTPktPercent,
       "tfrapDiagVBERTTestPeriod": tfrapDiagVBERTTestPeriod,
       "tfrapStatus": tfrapStatus,
       "tfrapStatusIntfTable": tfrapStatusIntfTable,
       "tfrapIntfDteMode": tfrapIntfDteMode,
       "tfrapIntfDteRts": tfrapIntfDteRts,
       "tfrapIntfDteDtr": tfrapIntfDteDtr,
       "tfrapIntfT1Mode": tfrapIntfT1Mode,
       "tfrapIntfT1Status": tfrapIntfT1Status,
       "tfrapIntfT1Alarms": tfrapIntfT1Alarms,
       "tfrapIntfDteDcd": tfrapIntfDteDcd,
       "tfrapIntfDteDsr": tfrapIntfDteDsr,
       "tfrapIntfDteCts": tfrapIntfDteCts,
       "tfrapVnipTopologyTable": tfrapVnipTopologyTable,
       "tfrapVnipTopologyEntry": tfrapVnipTopologyEntry,
       "tfrapVnipTopologyInterface": tfrapVnipTopologyInterface,
       "tfrapVnipTopologyIndex": tfrapVnipTopologyIndex,
       "tfrapVnipTopologyDlci": tfrapVnipTopologyDlci,
       "tfrapVnipTopologyIpAddr": tfrapVnipTopologyIpAddr,
       "tfrapVnipTopologyNumHops": tfrapVnipTopologyNumHops,
       "tfrapVnipTopologyLocalDlci": tfrapVnipTopologyLocalDlci,
       "tfrapVnipTopoTDNumSamples": tfrapVnipTopoTDNumSamples,
       "tfrapVnipTopoTDAvgDelay": tfrapVnipTopoTDAvgDelay,
       "tfrapVnipTopoTDMaxDelay": tfrapVnipTopoTDMaxDelay,
       "tfrapVnipTopoTDMinDelay": tfrapVnipTopoTDMinDelay,
       "tfrapVnipTopoTDLastDelay": tfrapVnipTopoTDLastDelay,
       "tfrapVnipTopoVLOOPStatus": tfrapVnipTopoVLOOPStatus,
       "tfrapVnipTopoVBERTStatus": tfrapVnipTopoVBERTStatus,
       "tfrapVnipTopoVBertTxDESetFrames": tfrapVnipTopoVBertTxDESetFrames,
       "tfrapVnipTopoVBertRxDESetFrames": tfrapVnipTopoVBertRxDESetFrames,
       "tfrapVnipTopoVBertTxDEClrFrames": tfrapVnipTopoVBertTxDEClrFrames,
       "tfrapVnipTopoVBertRxDEClrFrames": tfrapVnipTopoVBertRxDEClrFrames,
       "tfrapVnipTopoVBertTransitDelayMax": tfrapVnipTopoVBertTransitDelayMax,
       "tfrapVnipTopoVBertTransitDelayAvg": tfrapVnipTopoVBertTransitDelayAvg,
       "tfrapVnipTopoVBertTimeElapse": tfrapVnipTopoVBertTimeElapse,
       "tfrapVnipTopoVBertPerUtilCIR": tfrapVnipTopoVBertPerUtilCIR,
       "tfrapVnipTopoVBertPerUtilEIR": tfrapVnipTopoVBertPerUtilEIR,
       "tfrapStatusMgmtTable": tfrapStatusMgmtTable,
       "tfrapStatusMgmtChannel": tfrapStatusMgmtChannel,
       "tfrapStatusMgmtInterface": tfrapStatusMgmtInterface,
       "tfrapStatusMgmtInterfaceStatus": tfrapStatusMgmtInterfaceStatus,
       "tfrapStatusMgmtDefaultDLCINo": tfrapStatusMgmtDefaultDLCINo,
       "tfrapStatusMgmtDefaultDLCIStatus": tfrapStatusMgmtDefaultDLCIStatus,
       "tfrapStatusLedTable": tfrapStatusLedTable,
       "tfrapStatusDteModeLED": tfrapStatusDteModeLED,
       "tfrapStatusDteStatusLED": tfrapStatusDteStatusLED,
       "tfrapStatusDteTxLED": tfrapStatusDteTxLED,
       "tfrapStatusDteRxLED": tfrapStatusDteRxLED,
       "tfrapStatusT1ModeLED": tfrapStatusT1ModeLED,
       "tfrapStatusT1StatusLED": tfrapStatusT1StatusLED,
       "tfrapStatusAllLEDs": tfrapStatusAllLEDs,
       "tfrapVnipTransitDelayClear": tfrapVnipTransitDelayClear,
       "tfrapLmiSourcing": tfrapLmiSourcing,
       "tfrapVBertClear": tfrapVBertClear,
       "tfrapStatusLmiAutosense": tfrapStatusLmiAutosense,
       "tfrapPerformance": tfrapPerformance,
       "tfrapPerfPhysicalIntf": tfrapPerfPhysicalIntf,
       "tfrapPerfT1CurrentTable": tfrapPerfT1CurrentTable,
       "tfrapT1CurrentEntry": tfrapT1CurrentEntry,
       "tfrapT1CurrentIndex": tfrapT1CurrentIndex,
       "tfrapT1CurrentCrc6Events": tfrapT1CurrentCrc6Events,
       "tfrapT1CurrentOofEvents": tfrapT1CurrentOofEvents,
       "tfrapT1CurrentESs": tfrapT1CurrentESs,
       "tfrapT1CurrentSESs": tfrapT1CurrentSESs,
       "tfrapT1CurrentSEFSs": tfrapT1CurrentSEFSs,
       "tfrapT1CurrentUASs": tfrapT1CurrentUASs,
       "tfrapT1CurrentCSSs": tfrapT1CurrentCSSs,
       "tfrapT1CurrentBESs": tfrapT1CurrentBESs,
       "tfrapT1CurrentLCVs": tfrapT1CurrentLCVs,
       "tfrapPerfT1IntervalTable": tfrapPerfT1IntervalTable,
       "tfrapT1IntervalEntry": tfrapT1IntervalEntry,
       "tfrapT1IntervalIndex": tfrapT1IntervalIndex,
       "tfrapT1IntervalNumber": tfrapT1IntervalNumber,
       "tfrapT1IntervalESs": tfrapT1IntervalESs,
       "tfrapT1IntervalSESs": tfrapT1IntervalSESs,
       "tfrapT1IntervalSEFSs": tfrapT1IntervalSEFSs,
       "tfrapT1IntervalUASs": tfrapT1IntervalUASs,
       "tfrapT1IntervalCSSs": tfrapT1IntervalCSSs,
       "tfrapT1IntervalBESs": tfrapT1IntervalBESs,
       "tfrapT1IntervalLCVs": tfrapT1IntervalLCVs,
       "tfrapPerfT1TotalTable": tfrapPerfT1TotalTable,
       "tfrapT1TotalEntry": tfrapT1TotalEntry,
       "tfrapT1TotalIndex": tfrapT1TotalIndex,
       "tfrapT1TotalESs": tfrapT1TotalESs,
       "tfrapT1TotalSESs": tfrapT1TotalSESs,
       "tfrapT1TotalSEFSs": tfrapT1TotalSEFSs,
       "tfrapT1TotalUASs": tfrapT1TotalUASs,
       "tfrapT1TotalCSSs": tfrapT1TotalCSSs,
       "tfrapT1TotalBESs": tfrapT1TotalBESs,
       "tfrapT1TotalLCVs": tfrapT1TotalLCVs,
       "tfrapT1PerfCmdTypeTable": tfrapT1PerfCmdTypeTable,
       "tfrapT1PerfFreezeState": tfrapT1PerfFreezeState,
       "tfrapT1PerfClearEvents": tfrapT1PerfClearEvents,
       "tfrapT1PerfClearAll": tfrapT1PerfClearAll,
       "tfrapPerfMgmtIp": tfrapPerfMgmtIp,
       "tfrapPerfMgmtIpIFStatsTable": tfrapPerfMgmtIpIFStatsTable,
       "tfrapPerfMgmtIpIFInOctets": tfrapPerfMgmtIpIFInOctets,
       "tfrapPerfMgmtIpIFInErrors": tfrapPerfMgmtIpIFInErrors,
       "tfrapPerfMgmtIpIFOutOctets": tfrapPerfMgmtIpIFOutOctets,
       "tfrapPerfMgmtIpIFOperStatus": tfrapPerfMgmtIpIFOperStatus,
       "tfrapPerfMgmtIpIPStatsTable": tfrapPerfMgmtIpIPStatsTable,
       "tfrapPerfMgmtIpIPInRcv": tfrapPerfMgmtIpIPInRcv,
       "tfrapPerfMgmtIpIPInHdrErr": tfrapPerfMgmtIpIPInHdrErr,
       "tfrapPerfMgmtIpIPInAddrErr": tfrapPerfMgmtIpIPInAddrErr,
       "tfrapPerfMgmtIpIPInProtUnk": tfrapPerfMgmtIpIPInProtUnk,
       "tfrapPerfMgmtIpIPInDscrd": tfrapPerfMgmtIpIPInDscrd,
       "tfrapPerfMgmtIpIPInDlvrs": tfrapPerfMgmtIpIPInDlvrs,
       "tfrapPerfMgmtIpIPOutRqst": tfrapPerfMgmtIpIPOutRqst,
       "tfrapPerfMgmtIpIPOutDscrd": tfrapPerfMgmtIpIPOutDscrd,
       "tfrapPerfMgmtIpIPOutNoRt": tfrapPerfMgmtIpIPOutNoRt,
       "tfrapPerfMgmtIpICMPStatsTable": tfrapPerfMgmtIpICMPStatsTable,
       "tfrapPerfMgmtIpICMPInMsgs": tfrapPerfMgmtIpICMPInMsgs,
       "tfrapPerfMgmtIpICMPInErrors": tfrapPerfMgmtIpICMPInErrors,
       "tfrapPerfMgmtIpICMPInDestUnreachs": tfrapPerfMgmtIpICMPInDestUnreachs,
       "tfrapPerfMgmtIpICMPInTimeExcds": tfrapPerfMgmtIpICMPInTimeExcds,
       "tfrapPerfMgmtIpICMPInParmProbs": tfrapPerfMgmtIpICMPInParmProbs,
       "tfrapPerfMgmtIpICMPInRedirects": tfrapPerfMgmtIpICMPInRedirects,
       "tfrapPerfMgmtIpICMPInEchos": tfrapPerfMgmtIpICMPInEchos,
       "tfrapPerfMgmtIpICMPInEchoReps": tfrapPerfMgmtIpICMPInEchoReps,
       "tfrapPerfMgmtIpICMPOutMsgs": tfrapPerfMgmtIpICMPOutMsgs,
       "tfrapPerfMgmtIpICMPOutErrors": tfrapPerfMgmtIpICMPOutErrors,
       "tfrapPerfMgmtIpICMPOutDestUnreachs": tfrapPerfMgmtIpICMPOutDestUnreachs,
       "tfrapPerfMgmtIpICMPOutParmProbs": tfrapPerfMgmtIpICMPOutParmProbs,
       "tfrapPerfMgmtIpICMPOutRedirects": tfrapPerfMgmtIpICMPOutRedirects,
       "tfrapPerfMgmtIpICMPOutEchos": tfrapPerfMgmtIpICMPOutEchos,
       "tfrapPerfMgmtIpICMPOutEchoReps": tfrapPerfMgmtIpICMPOutEchoReps,
       "tfrapPerfMgmtIpUDPStatsTable": tfrapPerfMgmtIpUDPStatsTable,
       "tfrapPerfMgmtIpUDPInDatagrams": tfrapPerfMgmtIpUDPInDatagrams,
       "tfrapPerfMgmtIpUDPOutDatagrams": tfrapPerfMgmtIpUDPOutDatagrams,
       "tfrapPerfMgmtIpUDPNoPorts": tfrapPerfMgmtIpUDPNoPorts,
       "tfrapPerfMgmtIpTCPStatsTable": tfrapPerfMgmtIpTCPStatsTable,
       "tfrapPerfMgmtIpTCPActiveOpens": tfrapPerfMgmtIpTCPActiveOpens,
       "tfrapPerfMgmtIpTCPPassiveOpens": tfrapPerfMgmtIpTCPPassiveOpens,
       "tfrapPerfMgmtIpTCPAttemptFails": tfrapPerfMgmtIpTCPAttemptFails,
       "tfrapPerfMgmtIpTCPCurrEstab": tfrapPerfMgmtIpTCPCurrEstab,
       "tfrapPerfMgmtIpTCPInSegs": tfrapPerfMgmtIpTCPInSegs,
       "tfrapPerfMgmtIpTCPOutSegs": tfrapPerfMgmtIpTCPOutSegs,
       "tfrapPerfThruput": tfrapPerfThruput,
       "tfrapPerfThruputPerIntfTable": tfrapPerfThruputPerIntfTable,
       "tfrapPerfThruputPerIntfEntry": tfrapPerfThruputPerIntfEntry,
       "tfrapPerfThruputPerIntfIndex": tfrapPerfThruputPerIntfIndex,
       "tfrapPerfThruputPerIntfRxByteCnt": tfrapPerfThruputPerIntfRxByteCnt,
       "tfrapPerfThruputPerIntfTxByteCnt": tfrapPerfThruputPerIntfTxByteCnt,
       "tfrapPerfThruputPerIntfRxFrameCnt": tfrapPerfThruputPerIntfRxFrameCnt,
       "tfrapPerfThruputPerIntfTxFrameCnt": tfrapPerfThruputPerIntfTxFrameCnt,
       "tfrapPerfThruputPerIntfRxCrcErrCnt": tfrapPerfThruputPerIntfRxCrcErrCnt,
       "tfrapPerfThruputPerIntfRxAbortCnt": tfrapPerfThruputPerIntfRxAbortCnt,
       "tfrapPerfThruputPerDlciTable": tfrapPerfThruputPerDlciTable,
       "tfrapPerfThruputPerDlciEntry": tfrapPerfThruputPerDlciEntry,
       "tfrapPerfThruputPerDlciIndex": tfrapPerfThruputPerDlciIndex,
       "tfrapPerfThruputPerDlciValue": tfrapPerfThruputPerDlciValue,
       "tfrapPerfThruputPerDlciCreateTime": tfrapPerfThruputPerDlciCreateTime,
       "tfrapPerfThruputPerDlciChangeTime": tfrapPerfThruputPerDlciChangeTime,
       "tfrapPerfThruputPerDlciRxByte": tfrapPerfThruputPerDlciRxByte,
       "tfrapPerfThruputPerDlciTxByte": tfrapPerfThruputPerDlciTxByte,
       "tfrapPerfThruputPerDlciRxFrame": tfrapPerfThruputPerDlciRxFrame,
       "tfrapPerfThruputPerDlciTxFrame": tfrapPerfThruputPerDlciTxFrame,
       "tfrapPerfThruputPerDlciRxFecn": tfrapPerfThruputPerDlciRxFecn,
       "tfrapPerfThruputPerDlciRxBecn": tfrapPerfThruputPerDlciRxBecn,
       "tfrapPerfThruputPerDlciRxDe": tfrapPerfThruputPerDlciRxDe,
       "tfrapPerfThruputPerDlciTxDe": tfrapPerfThruputPerDlciTxDe,
       "tfrapPerfThruputPerDlciRxThruput": tfrapPerfThruputPerDlciRxThruput,
       "tfrapPerfThruputPerDlciTxThruput": tfrapPerfThruputPerDlciTxThruput,
       "tfrapPerfThruputPerDlciCIR": tfrapPerfThruputPerDlciCIR,
       "tfrapPerfThruputPerDlciUptime": tfrapPerfThruputPerDlciUptime,
       "tfrapPerfThruputPerDlciDowntime": tfrapPerfThruputPerDlciDowntime,
       "tfrapPerfThruputPerDlciCirType": tfrapPerfThruputPerDlciCirType,
       "tfrapPerfThruputPerDlciPvcState": tfrapPerfThruputPerDlciPvcState,
       "tfrapPerfThruputPerDlciOutageCount": tfrapPerfThruputPerDlciOutageCount,
       "tfrapPerfThruputPerDlciAvailability": tfrapPerfThruputPerDlciAvailability,
       "tfrapPerfThruputPerDlciMTBSO": tfrapPerfThruputPerDlciMTBSO,
       "tfrapPerfThruputPerDlciMTTSR": tfrapPerfThruputPerDlciMTTSR,
       "tfrapPerfThruputPerDlciEncapType": tfrapPerfThruputPerDlciEncapType,
       "tfrapPerfThruputPerDlciRxUtilizationStatus": tfrapPerfThruputPerDlciRxUtilizationStatus,
       "tfrapPerfThruputPerDlciTxUtilizationStatus": tfrapPerfThruputPerDlciTxUtilizationStatus,
       "tfrapPerfThruputPerDlciEIR": tfrapPerfThruputPerDlciEIR,
       "tfrapPerfThruputCommands": tfrapPerfThruputCommands,
       "tfrapPerfThruputCmdClearDteStats": tfrapPerfThruputCmdClearDteStats,
       "tfrapPerfThruputCmdClearT1Stats": tfrapPerfThruputCmdClearT1Stats,
       "tfrapPerfThruputCmdClearAllIntfStats": tfrapPerfThruputCmdClearAllIntfStats,
       "tfrapPerfThruputCmdClearDlciStats": tfrapPerfThruputCmdClearDlciStats,
       "tfrapPerfThruputCmdClearAllStats": tfrapPerfThruputCmdClearAllStats,
       "tfrapPerfThruputCmdRemoveStsDlci": tfrapPerfThruputCmdRemoveStsDlci,
       "tfrapPerfThruputCmdReplaceDlciTable": tfrapPerfThruputCmdReplaceDlciTable,
       "tfrapPerfThruputCmdReplaceDlciEntry": tfrapPerfThruputCmdReplaceDlciEntry,
       "tfrapPerfThruputCmdReplaceDlciValue": tfrapPerfThruputCmdReplaceDlciValue,
       "tfrapPerfThruputCmdReplaceDlciNewValue": tfrapPerfThruputCmdReplaceDlciNewValue,
       "tfrapPerfThruputCmdAvailabilityStsDlciReset": tfrapPerfThruputCmdAvailabilityStsDlciReset,
       "tfrapPerfThruputCmdAvailabilityStsDlciResetAll": tfrapPerfThruputCmdAvailabilityStsDlciResetAll,
       "tfrapPerfThruputCmdCountsStsDlciReset": tfrapPerfThruputCmdCountsStsDlciReset,
       "tfrapPerfThruputCmdCountsStsDlciResetAll": tfrapPerfThruputCmdCountsStsDlciResetAll,
       "tfrapPerfThruputCmdAllStsDlciReset": tfrapPerfThruputCmdAllStsDlciReset,
       "tfrapPerfThruputCmdAllStsDlciResetAll": tfrapPerfThruputCmdAllStsDlciResetAll,
       "tfrapPerfNetworkShortTerm": tfrapPerfNetworkShortTerm,
       "tfrapPerfNetwProtoPerDlciTable": tfrapPerfNetwProtoPerDlciTable,
       "tfrapPerfNetwProtoPerDlciEntry": tfrapPerfNetwProtoPerDlciEntry,
       "tfrapPerfNetwProtoPerDlciInterval": tfrapPerfNetwProtoPerDlciInterval,
       "tfrapPerfNetwProtoPerDlciValue": tfrapPerfNetwProtoPerDlciValue,
       "tfrapPerfNetwProtoPerDlciRxTotal": tfrapPerfNetwProtoPerDlciRxTotal,
       "tfrapPerfNetwProtoPerDlciTxTotal": tfrapPerfNetwProtoPerDlciTxTotal,
       "tfrapPerfNetwProtoPerDlciRxIp": tfrapPerfNetwProtoPerDlciRxIp,
       "tfrapPerfNetwProtoPerDlciTxIp": tfrapPerfNetwProtoPerDlciTxIp,
       "tfrapPerfNetwProtoPerDlciRxIpx": tfrapPerfNetwProtoPerDlciRxIpx,
       "tfrapPerfNetwProtoPerDlciTxIpx": tfrapPerfNetwProtoPerDlciTxIpx,
       "tfrapPerfNetwProtoPerDlciRxSna": tfrapPerfNetwProtoPerDlciRxSna,
       "tfrapPerfNetwProtoPerDlciTxSna": tfrapPerfNetwProtoPerDlciTxSna,
       "tfrapPerfNetwProtoPerDlciRxArp": tfrapPerfNetwProtoPerDlciRxArp,
       "tfrapPerfNetwProtoPerDlciTxArp": tfrapPerfNetwProtoPerDlciTxArp,
       "tfrapPerfNetwProtoPerDlciRxCisco": tfrapPerfNetwProtoPerDlciRxCisco,
       "tfrapPerfNetwProtoPerDlciTxCisco": tfrapPerfNetwProtoPerDlciTxCisco,
       "tfrapPerfNetwProtoPerDlciRxOther": tfrapPerfNetwProtoPerDlciRxOther,
       "tfrapPerfNetwProtoPerDlciTxOther": tfrapPerfNetwProtoPerDlciTxOther,
       "tfrapPerfNetwProtoPerDlciRxVnip": tfrapPerfNetwProtoPerDlciRxVnip,
       "tfrapPerfNetwProtoPerDlciTxVnip": tfrapPerfNetwProtoPerDlciTxVnip,
       "tfrapPerfNetwProtoPerDlciRxAnnexG": tfrapPerfNetwProtoPerDlciRxAnnexG,
       "tfrapPerfNetwProtoPerDlciTxAnnexG": tfrapPerfNetwProtoPerDlciTxAnnexG,
       "tfrapPerfNetwProtoTotalTable": tfrapPerfNetwProtoTotalTable,
       "tfrapPerfNetwProtoTotalEntry": tfrapPerfNetwProtoTotalEntry,
       "tfrapPerfNetwProtoTotalInterval": tfrapPerfNetwProtoTotalInterval,
       "tfrapPerfNetwProtoTotalRxTotal": tfrapPerfNetwProtoTotalRxTotal,
       "tfrapPerfNetwProtoTotalTxTotal": tfrapPerfNetwProtoTotalTxTotal,
       "tfrapPerfNetwProtoTotalRxIp": tfrapPerfNetwProtoTotalRxIp,
       "tfrapPerfNetwProtoTotalTxIp": tfrapPerfNetwProtoTotalTxIp,
       "tfrapPerfNetwProtoTotalRxIpx": tfrapPerfNetwProtoTotalRxIpx,
       "tfrapPerfNetwProtoTotalTxIpx": tfrapPerfNetwProtoTotalTxIpx,
       "tfrapPerfNetwProtoTotalRxSna": tfrapPerfNetwProtoTotalRxSna,
       "tfrapPerfNetwProtoTotalTxSna": tfrapPerfNetwProtoTotalTxSna,
       "tfrapPerfNetwProtoTotalRxArp": tfrapPerfNetwProtoTotalRxArp,
       "tfrapPerfNetwProtoTotalTxArp": tfrapPerfNetwProtoTotalTxArp,
       "tfrapPerfNetwProtoTotalRxCisco": tfrapPerfNetwProtoTotalRxCisco,
       "tfrapPerfNetwProtoTotalTxCisco": tfrapPerfNetwProtoTotalTxCisco,
       "tfrapPerfNetwProtoTotalRxOther": tfrapPerfNetwProtoTotalRxOther,
       "tfrapPerfNetwProtoTotalTxOther": tfrapPerfNetwProtoTotalTxOther,
       "tfrapPerfNetwProtoTotalRxVnip": tfrapPerfNetwProtoTotalRxVnip,
       "tfrapPerfNetwProtoTotalTxVnip": tfrapPerfNetwProtoTotalTxVnip,
       "tfrapPerfNetwProtoTotalRxAnnexG": tfrapPerfNetwProtoTotalRxAnnexG,
       "tfrapPerfNetwProtoTotalTxAnnexG": tfrapPerfNetwProtoTotalTxAnnexG,
       "tfrapPerfIpPerDlciTable": tfrapPerfIpPerDlciTable,
       "tfrapPerfIpPerDlciEntry": tfrapPerfIpPerDlciEntry,
       "tfrapPerfIpPerDlciInterval": tfrapPerfIpPerDlciInterval,
       "tfrapPerfIpPerDlciValue": tfrapPerfIpPerDlciValue,
       "tfrapPerfIpPerDlciRxTotal": tfrapPerfIpPerDlciRxTotal,
       "tfrapPerfIpPerDlciTxTotal": tfrapPerfIpPerDlciTxTotal,
       "tfrapPerfIpPerDlciRxTcp": tfrapPerfIpPerDlciRxTcp,
       "tfrapPerfIpPerDlciTxTcp": tfrapPerfIpPerDlciTxTcp,
       "tfrapPerfIpPerDlciRxUdp": tfrapPerfIpPerDlciRxUdp,
       "tfrapPerfIpPerDlciTxUdp": tfrapPerfIpPerDlciTxUdp,
       "tfrapPerfIpPerDlciRxIcmp": tfrapPerfIpPerDlciRxIcmp,
       "tfrapPerfIpPerDlciTxIcmp": tfrapPerfIpPerDlciTxIcmp,
       "tfrapPerfIpPerDlciRxOther": tfrapPerfIpPerDlciRxOther,
       "tfrapPerfIpPerDlciTxOther": tfrapPerfIpPerDlciTxOther,
       "tfrapPerfIpPerDlciRxIgrp": tfrapPerfIpPerDlciRxIgrp,
       "tfrapPerfIpPerDlciTxIgrp": tfrapPerfIpPerDlciTxIgrp,
       "tfrapPerfIpTotalTable": tfrapPerfIpTotalTable,
       "tfrapPerfIpTotalEntry": tfrapPerfIpTotalEntry,
       "tfrapPerfIpTotalInterval": tfrapPerfIpTotalInterval,
       "tfrapPerfIpTotalRxTotal": tfrapPerfIpTotalRxTotal,
       "tfrapPerfIpTotalTxTotal": tfrapPerfIpTotalTxTotal,
       "tfrapPerfIpTotalRxTcp": tfrapPerfIpTotalRxTcp,
       "tfrapPerfIpTotalTxTcp": tfrapPerfIpTotalTxTcp,
       "tfrapPerfIpTotalRxUdp": tfrapPerfIpTotalRxUdp,
       "tfrapPerfIpTotalTxUdp": tfrapPerfIpTotalTxUdp,
       "tfrapPerfIpTotalRxIcmp": tfrapPerfIpTotalRxIcmp,
       "tfrapPerfIpTotalTxIcmp": tfrapPerfIpTotalTxIcmp,
       "tfrapPerfIpTotalRxOther": tfrapPerfIpTotalRxOther,
       "tfrapPerfIpTotalTxOther": tfrapPerfIpTotalTxOther,
       "tfrapPerfIpTotalRxIgrp": tfrapPerfIpTotalRxIgrp,
       "tfrapPerfIpTotalTxIgrp": tfrapPerfIpTotalTxIgrp,
       "tfrapPerfIcmpPerDlciTable": tfrapPerfIcmpPerDlciTable,
       "tfrapPerfIcmpPerDlciEntry": tfrapPerfIcmpPerDlciEntry,
       "tfrapPerfIcmpPerDlciInterval": tfrapPerfIcmpPerDlciInterval,
       "tfrapPerfIcmpPerDlciValue": tfrapPerfIcmpPerDlciValue,
       "tfrapPerfIcmpPerDlciRxTotal": tfrapPerfIcmpPerDlciRxTotal,
       "tfrapPerfIcmpPerDlciTxTotal": tfrapPerfIcmpPerDlciTxTotal,
       "tfrapPerfIcmpPerDlciRxEchoRep": tfrapPerfIcmpPerDlciRxEchoRep,
       "tfrapPerfIcmpPerDlciTxEchoRep": tfrapPerfIcmpPerDlciTxEchoRep,
       "tfrapPerfIcmpPerDlciRxDestUnr": tfrapPerfIcmpPerDlciRxDestUnr,
       "tfrapPerfIcmpPerDlciTxDestUnr": tfrapPerfIcmpPerDlciTxDestUnr,
       "tfrapPerfIcmpPerDlciRxSrcQuench": tfrapPerfIcmpPerDlciRxSrcQuench,
       "tfrapPerfIcmpPerDlciTxSrcQuench": tfrapPerfIcmpPerDlciTxSrcQuench,
       "tfrapPerfIcmpPerDlciRxRedirect": tfrapPerfIcmpPerDlciRxRedirect,
       "tfrapPerfIcmpPerDlciTxRedirect": tfrapPerfIcmpPerDlciTxRedirect,
       "tfrapPerfIcmpPerDlciRxEchoReq": tfrapPerfIcmpPerDlciRxEchoReq,
       "tfrapPerfIcmpPerDlciTxEchoReq": tfrapPerfIcmpPerDlciTxEchoReq,
       "tfrapPerfIcmpPerDlciRxTimeExcd": tfrapPerfIcmpPerDlciRxTimeExcd,
       "tfrapPerfIcmpPerDlciTxTimeExcd": tfrapPerfIcmpPerDlciTxTimeExcd,
       "tfrapPerfIcmpPerDlciRxParamProb": tfrapPerfIcmpPerDlciRxParamProb,
       "tfrapPerfIcmpPerDlciTxParamProb": tfrapPerfIcmpPerDlciTxParamProb,
       "tfrapPerfIcmpPerDlciRxTimestpReq": tfrapPerfIcmpPerDlciRxTimestpReq,
       "tfrapPerfIcmpPerDlciTxTimestpReq": tfrapPerfIcmpPerDlciTxTimestpReq,
       "tfrapPerfIcmpPerDlciRxTimestpRep": tfrapPerfIcmpPerDlciRxTimestpRep,
       "tfrapPerfIcmpPerDlciTxTimestpRep": tfrapPerfIcmpPerDlciTxTimestpRep,
       "tfrapPerfIcmpPerDlciRxAddrMaskReq": tfrapPerfIcmpPerDlciRxAddrMaskReq,
       "tfrapPerfIcmpPerDlciTxAddrMaskReq": tfrapPerfIcmpPerDlciTxAddrMaskReq,
       "tfrapPerfIcmpPerDlciRxAddrMaskRep": tfrapPerfIcmpPerDlciRxAddrMaskRep,
       "tfrapPerfIcmpPerDlciTxAddrMaskRep": tfrapPerfIcmpPerDlciTxAddrMaskRep,
       "tfrapPerfIcmpPerDlciRxPktTooBig": tfrapPerfIcmpPerDlciRxPktTooBig,
       "tfrapPerfIcmpPerDlciTxPktTooBig": tfrapPerfIcmpPerDlciTxPktTooBig,
       "tfrapPerfIcmpPerDlciRxGmQuery": tfrapPerfIcmpPerDlciRxGmQuery,
       "tfrapPerfIcmpPerDlciTxGmQuery": tfrapPerfIcmpPerDlciTxGmQuery,
       "tfrapPerfIcmpPerDlciRxGmReport": tfrapPerfIcmpPerDlciRxGmReport,
       "tfrapPerfIcmpPerDlciTxGmReport": tfrapPerfIcmpPerDlciTxGmReport,
       "tfrapPerfIcmpPerDlciRxGmReduct": tfrapPerfIcmpPerDlciRxGmReduct,
       "tfrapPerfIcmpPerDlciTxGmReduct": tfrapPerfIcmpPerDlciTxGmReduct,
       "tfrapPerfIcmpTotalTable": tfrapPerfIcmpTotalTable,
       "tfrapPerfIcmpTotalEntry": tfrapPerfIcmpTotalEntry,
       "tfrapPerfIcmpTotalInterval": tfrapPerfIcmpTotalInterval,
       "tfrapPerfIcmpTotalRxTotal": tfrapPerfIcmpTotalRxTotal,
       "tfrapPerfIcmpTotalTxTotal": tfrapPerfIcmpTotalTxTotal,
       "tfrapPerfIcmpTotalRxEchoRep": tfrapPerfIcmpTotalRxEchoRep,
       "tfrapPerfIcmpTotalTxEchoRep": tfrapPerfIcmpTotalTxEchoRep,
       "tfrapPerfIcmpTotalRxDestUnr": tfrapPerfIcmpTotalRxDestUnr,
       "tfrapPerfIcmpTotalTxDestUnr": tfrapPerfIcmpTotalTxDestUnr,
       "tfrapPerfIcmpTotalRxSrcQuench": tfrapPerfIcmpTotalRxSrcQuench,
       "tfrapPerfIcmpTotalTxSrcQuench": tfrapPerfIcmpTotalTxSrcQuench,
       "tfrapPerfIcmpTotalRxRedirect": tfrapPerfIcmpTotalRxRedirect,
       "tfrapPerfIcmpTotalTxRedirect": tfrapPerfIcmpTotalTxRedirect,
       "tfrapPerfIcmpTotalRxEchoReq": tfrapPerfIcmpTotalRxEchoReq,
       "tfrapPerfIcmpTotalTxEchoReq": tfrapPerfIcmpTotalTxEchoReq,
       "tfrapPerfIcmpTotalRxTimeExcd": tfrapPerfIcmpTotalRxTimeExcd,
       "tfrapPerfIcmpTotalTxTimeExcd": tfrapPerfIcmpTotalTxTimeExcd,
       "tfrapPerfIcmpTotalRxParamProb": tfrapPerfIcmpTotalRxParamProb,
       "tfrapPerfIcmpTotalTxParamProb": tfrapPerfIcmpTotalTxParamProb,
       "tfrapPerfIcmpTotalRxTimestpReq": tfrapPerfIcmpTotalRxTimestpReq,
       "tfrapPerfIcmpTotalTxTimestpReq": tfrapPerfIcmpTotalTxTimestpReq,
       "tfrapPerfIcmpTotalRxTimestpRep": tfrapPerfIcmpTotalRxTimestpRep,
       "tfrapPerfIcmpTotalTxTimestpRep": tfrapPerfIcmpTotalTxTimestpRep,
       "tfrapPerfIcmpTotalRxAddrMaskReq": tfrapPerfIcmpTotalRxAddrMaskReq,
       "tfrapPerfIcmpTotalTxAddrMaskReq": tfrapPerfIcmpTotalTxAddrMaskReq,
       "tfrapPerfIcmpTotalRxAddrMaskRep": tfrapPerfIcmpTotalRxAddrMaskRep,
       "tfrapPerfIcmpTotalTxAddrMaskRep": tfrapPerfIcmpTotalTxAddrMaskRep,
       "tfrapPerfIcmpTotalRxPktTooBig": tfrapPerfIcmpTotalRxPktTooBig,
       "tfrapPerfIcmpTotalTxPktTooBig": tfrapPerfIcmpTotalTxPktTooBig,
       "tfrapPerfIcmpTotalRxGmQuery": tfrapPerfIcmpTotalRxGmQuery,
       "tfrapPerfIcmpTotalTxGmQuery": tfrapPerfIcmpTotalTxGmQuery,
       "tfrapPerfIcmpTotalRxGmReport": tfrapPerfIcmpTotalRxGmReport,
       "tfrapPerfIcmpTotalTxGmReport": tfrapPerfIcmpTotalTxGmReport,
       "tfrapPerfIcmpTotalRxGmReduct": tfrapPerfIcmpTotalRxGmReduct,
       "tfrapPerfIcmpTotalTxGmReduct": tfrapPerfIcmpTotalTxGmReduct,
       "tfrapPerfApplicationPerDlciTable": tfrapPerfApplicationPerDlciTable,
       "tfrapPerfApplicationPerDlciEntry": tfrapPerfApplicationPerDlciEntry,
       "tfrapPerfApplicationPerDlciInterval": tfrapPerfApplicationPerDlciInterval,
       "tfrapPerfApplicationPerDlciValue": tfrapPerfApplicationPerDlciValue,
       "tfrapPerfApplicationPerDlciRxSnmp": tfrapPerfApplicationPerDlciRxSnmp,
       "tfrapPerfApplicationPerDlciTxSnmp": tfrapPerfApplicationPerDlciTxSnmp,
       "tfrapPerfApplicationPerDlciRxSnmpTrap": tfrapPerfApplicationPerDlciRxSnmpTrap,
       "tfrapPerfApplicationPerDlciTxSnmpTrap": tfrapPerfApplicationPerDlciTxSnmpTrap,
       "tfrapPerfApplicationPerDlciRxHttp": tfrapPerfApplicationPerDlciRxHttp,
       "tfrapPerfApplicationPerDlciTxHttp": tfrapPerfApplicationPerDlciTxHttp,
       "tfrapPerfApplicationPerDlciRxTelnet": tfrapPerfApplicationPerDlciRxTelnet,
       "tfrapPerfApplicationPerDlciTxTelnet": tfrapPerfApplicationPerDlciTxTelnet,
       "tfrapPerfApplicationPerDlciRxSmtp": tfrapPerfApplicationPerDlciRxSmtp,
       "tfrapPerfApplicationPerDlciTxSmtp": tfrapPerfApplicationPerDlciTxSmtp,
       "tfrapPerfApplicationPerDlciRxFtp": tfrapPerfApplicationPerDlciRxFtp,
       "tfrapPerfApplicationPerDlciTxFtp": tfrapPerfApplicationPerDlciTxFtp,
       "tfrapPerfApplicationPerDlciRxTftp": tfrapPerfApplicationPerDlciRxTftp,
       "tfrapPerfApplicationPerDlciTxTftp": tfrapPerfApplicationPerDlciTxTftp,
       "tfrapPerfApplicationPerDlciRxCustom1": tfrapPerfApplicationPerDlciRxCustom1,
       "tfrapPerfApplicationPerDlciTxCustom1": tfrapPerfApplicationPerDlciTxCustom1,
       "tfrapPerfApplicationPerDlciRxCustom2": tfrapPerfApplicationPerDlciRxCustom2,
       "tfrapPerfApplicationPerDlciTxCustom2": tfrapPerfApplicationPerDlciTxCustom2,
       "tfrapPerfApplicationPerDlciRxCustom3": tfrapPerfApplicationPerDlciRxCustom3,
       "tfrapPerfApplicationPerDlciTxCustom3": tfrapPerfApplicationPerDlciTxCustom3,
       "tfrapPerfApplicationPerDlciRxCustom4": tfrapPerfApplicationPerDlciRxCustom4,
       "tfrapPerfApplicationPerDlciTxCustom4": tfrapPerfApplicationPerDlciTxCustom4,
       "tfrapPerfApplicationTotalTable": tfrapPerfApplicationTotalTable,
       "tfrapPerfApplicationTotalEntry": tfrapPerfApplicationTotalEntry,
       "tfrapPerfApplicationTotalInterval": tfrapPerfApplicationTotalInterval,
       "tfrapPerfApplicationTotalRxSnmp": tfrapPerfApplicationTotalRxSnmp,
       "tfrapPerfApplicationTotalTxSnmp": tfrapPerfApplicationTotalTxSnmp,
       "tfrapPerfApplicationTotalRxSnmpTrap": tfrapPerfApplicationTotalRxSnmpTrap,
       "tfrapPerfApplicationTotalTxSnmpTrap": tfrapPerfApplicationTotalTxSnmpTrap,
       "tfrapPerfApplicationTotalRxHttp": tfrapPerfApplicationTotalRxHttp,
       "tfrapPerfApplicationTotalTxHttp": tfrapPerfApplicationTotalTxHttp,
       "tfrapPerfApplicationTotalRxTelnet": tfrapPerfApplicationTotalRxTelnet,
       "tfrapPerfApplicationTotalTxTelnet": tfrapPerfApplicationTotalTxTelnet,
       "tfrapPerfApplicationTotalRxSmtp": tfrapPerfApplicationTotalRxSmtp,
       "tfrapPerfApplicationTotalTxSmtp": tfrapPerfApplicationTotalTxSmtp,
       "tfrapPerfApplicationTotalRxFtp": tfrapPerfApplicationTotalRxFtp,
       "tfrapPerfApplicationTotalTxFtp": tfrapPerfApplicationTotalTxFtp,
       "tfrapPerfApplicationTotalRxTftp": tfrapPerfApplicationTotalRxTftp,
       "tfrapPerfApplicationTotalTxTftp": tfrapPerfApplicationTotalTxTftp,
       "tfrapPerfApplicationTotalRxCustom1": tfrapPerfApplicationTotalRxCustom1,
       "tfrapPerfApplicationTotalTxCustom1": tfrapPerfApplicationTotalTxCustom1,
       "tfrapPerfApplicationTotalRxCustom2": tfrapPerfApplicationTotalRxCustom2,
       "tfrapPerfApplicationTotalTxCustom2": tfrapPerfApplicationTotalTxCustom2,
       "tfrapPerfApplicationTotalRxCustom3": tfrapPerfApplicationTotalRxCustom3,
       "tfrapPerfApplicationTotalTxCustom3": tfrapPerfApplicationTotalTxCustom3,
       "tfrapPerfApplicationTotalRxCustom4": tfrapPerfApplicationTotalRxCustom4,
       "tfrapPerfApplicationTotalTxCustom4": tfrapPerfApplicationTotalTxCustom4,
       "tfrapPerfRoutingPerDlciTable": tfrapPerfRoutingPerDlciTable,
       "tfrapPerfRoutingPerDlciEntry": tfrapPerfRoutingPerDlciEntry,
       "tfrapPerfRoutingPerDlciInterval": tfrapPerfRoutingPerDlciInterval,
       "tfrapPerfRoutingPerDlciValue": tfrapPerfRoutingPerDlciValue,
       "tfrapPerfRoutingPerDlciRxOspf": tfrapPerfRoutingPerDlciRxOspf,
       "tfrapPerfRoutingPerDlciTxOspf": tfrapPerfRoutingPerDlciTxOspf,
       "tfrapPerfRoutingPerDlciRxRip": tfrapPerfRoutingPerDlciRxRip,
       "tfrapPerfRoutingPerDlciTxRip": tfrapPerfRoutingPerDlciTxRip,
       "tfrapPerfRoutingPerDlciRxNetbios": tfrapPerfRoutingPerDlciRxNetbios,
       "tfrapPerfRoutingPerDlciTxNetbios": tfrapPerfRoutingPerDlciTxNetbios,
       "tfrapPerfRoutingTotalTable": tfrapPerfRoutingTotalTable,
       "tfrapPerfRoutingTotalEntry": tfrapPerfRoutingTotalEntry,
       "tfrapPerfRoutingTotalInterval": tfrapPerfRoutingTotalInterval,
       "tfrapPerfRoutingTotalRxOspf": tfrapPerfRoutingTotalRxOspf,
       "tfrapPerfRoutingTotalTxOspf": tfrapPerfRoutingTotalTxOspf,
       "tfrapPerfRoutingTotalRxRip": tfrapPerfRoutingTotalRxRip,
       "tfrapPerfRoutingTotalTxRip": tfrapPerfRoutingTotalTxRip,
       "tfrapPerfRoutingTotalRxNetbios": tfrapPerfRoutingTotalRxNetbios,
       "tfrapPerfRoutingTotalTxNetbios": tfrapPerfRoutingTotalTxNetbios,
       "tfrapPerfIpxPerDlciTable": tfrapPerfIpxPerDlciTable,
       "tfrapPerfIpxPerDlciEntry": tfrapPerfIpxPerDlciEntry,
       "tfrapPerfIpxPerDlciInterval": tfrapPerfIpxPerDlciInterval,
       "tfrapPerfIpxPerDlciValue": tfrapPerfIpxPerDlciValue,
       "tfrapPerfIpxPerDlciRxTotal": tfrapPerfIpxPerDlciRxTotal,
       "tfrapPerfIpxPerDlciTxTotal": tfrapPerfIpxPerDlciTxTotal,
       "tfrapPerfIpxPerDlciRxSpx": tfrapPerfIpxPerDlciRxSpx,
       "tfrapPerfIpxPerDlciTxSpx": tfrapPerfIpxPerDlciTxSpx,
       "tfrapPerfIpxPerDlciRxNcp": tfrapPerfIpxPerDlciRxNcp,
       "tfrapPerfIpxPerDlciTxNcp": tfrapPerfIpxPerDlciTxNcp,
       "tfrapPerfIpxPerDlciRxSap": tfrapPerfIpxPerDlciRxSap,
       "tfrapPerfIpxPerDlciTxSap": tfrapPerfIpxPerDlciTxSap,
       "tfrapPerfIpxPerDlciRxRip": tfrapPerfIpxPerDlciRxRip,
       "tfrapPerfIpxPerDlciTxRip": tfrapPerfIpxPerDlciTxRip,
       "tfrapPerfIpxPerDlciRxNetbios": tfrapPerfIpxPerDlciRxNetbios,
       "tfrapPerfIpxPerDlciTxNetbios": tfrapPerfIpxPerDlciTxNetbios,
       "tfrapPerfIpxPerDlciRxOther": tfrapPerfIpxPerDlciRxOther,
       "tfrapPerfIpxPerDlciTxOther": tfrapPerfIpxPerDlciTxOther,
       "tfrapPerfIpxTotalTable": tfrapPerfIpxTotalTable,
       "tfrapPerfIpxTotalEntry": tfrapPerfIpxTotalEntry,
       "tfrapPerfIpxTotalInterval": tfrapPerfIpxTotalInterval,
       "tfrapPerfIpxTotalRxTotal": tfrapPerfIpxTotalRxTotal,
       "tfrapPerfIpxTotalTxTotal": tfrapPerfIpxTotalTxTotal,
       "tfrapPerfIpxTotalRxSpx": tfrapPerfIpxTotalRxSpx,
       "tfrapPerfIpxTotalTxSpx": tfrapPerfIpxTotalTxSpx,
       "tfrapPerfIpxTotalRxNcp": tfrapPerfIpxTotalRxNcp,
       "tfrapPerfIpxTotalTxNcp": tfrapPerfIpxTotalTxNcp,
       "tfrapPerfIpxTotalRxSap": tfrapPerfIpxTotalRxSap,
       "tfrapPerfIpxTotalTxSap": tfrapPerfIpxTotalTxSap,
       "tfrapPerfIpxTotalRxRip": tfrapPerfIpxTotalRxRip,
       "tfrapPerfIpxTotalTxRip": tfrapPerfIpxTotalTxRip,
       "tfrapPerfIpxTotalRxNetbios": tfrapPerfIpxTotalRxNetbios,
       "tfrapPerfIpxTotalTxNetbios": tfrapPerfIpxTotalTxNetbios,
       "tfrapPerfIpxTotalRxOther": tfrapPerfIpxTotalRxOther,
       "tfrapPerfIpxTotalTxOther": tfrapPerfIpxTotalTxOther,
       "tfrapPerfSnaPerDlciTable": tfrapPerfSnaPerDlciTable,
       "tfrapPerfSnaPerDlciEntry": tfrapPerfSnaPerDlciEntry,
       "tfrapPerfSnaPerDlciInterval": tfrapPerfSnaPerDlciInterval,
       "tfrapPerfSnaPerDlciValue": tfrapPerfSnaPerDlciValue,
       "tfrapPerfSnaPerDlciRxTotal": tfrapPerfSnaPerDlciRxTotal,
       "tfrapPerfSnaPerDlciTxTotal": tfrapPerfSnaPerDlciTxTotal,
       "tfrapPerfSnaPerDlciRxSubarea": tfrapPerfSnaPerDlciRxSubarea,
       "tfrapPerfSnaPerDlciTxSubarea": tfrapPerfSnaPerDlciTxSubarea,
       "tfrapPerfSnaPerDlciRxPeriph": tfrapPerfSnaPerDlciRxPeriph,
       "tfrapPerfSnaPerDlciTxPeriph": tfrapPerfSnaPerDlciTxPeriph,
       "tfrapPerfSnaPerDlciRxAppn": tfrapPerfSnaPerDlciRxAppn,
       "tfrapPerfSnaPerDlciTxAppn": tfrapPerfSnaPerDlciTxAppn,
       "tfrapPerfSnaPerDlciRxNetbios": tfrapPerfSnaPerDlciRxNetbios,
       "tfrapPerfSnaPerDlciTxNetbios": tfrapPerfSnaPerDlciTxNetbios,
       "tfrapPerfSnaPerDlciRxOther": tfrapPerfSnaPerDlciRxOther,
       "tfrapPerfSnaPerDlciTxOther": tfrapPerfSnaPerDlciTxOther,
       "tfrapPerfSnaTotalTable": tfrapPerfSnaTotalTable,
       "tfrapPerfSnaTotalEntry": tfrapPerfSnaTotalEntry,
       "tfrapPerfSnaTotalInterval": tfrapPerfSnaTotalInterval,
       "tfrapPerfSnaTotalRxTotal": tfrapPerfSnaTotalRxTotal,
       "tfrapPerfSnaTotalTxTotal": tfrapPerfSnaTotalTxTotal,
       "tfrapPerfSnaTotalRxSubarea": tfrapPerfSnaTotalRxSubarea,
       "tfrapPerfSnaTotalTxSubarea": tfrapPerfSnaTotalTxSubarea,
       "tfrapPerfSnaTotalRxPeriph": tfrapPerfSnaTotalRxPeriph,
       "tfrapPerfSnaTotalTxPeriph": tfrapPerfSnaTotalTxPeriph,
       "tfrapPerfSnaTotalRxAppn": tfrapPerfSnaTotalRxAppn,
       "tfrapPerfSnaTotalTxAppn": tfrapPerfSnaTotalTxAppn,
       "tfrapPerfSnaTotalRxNetbios": tfrapPerfSnaTotalRxNetbios,
       "tfrapPerfSnaTotalTxNetbios": tfrapPerfSnaTotalTxNetbios,
       "tfrapPerfSnaTotalRxOther": tfrapPerfSnaTotalRxOther,
       "tfrapPerfSnaTotalTxOther": tfrapPerfSnaTotalTxOther,
       "tfrapPerfArpPerDlciTable": tfrapPerfArpPerDlciTable,
       "tfrapPerfArpPerDlciEntry": tfrapPerfArpPerDlciEntry,
       "tfrapPerfArpPerDlciInterval": tfrapPerfArpPerDlciInterval,
       "tfrapPerfArpPerDlciValue": tfrapPerfArpPerDlciValue,
       "tfrapPerfArpPerDlciRxTotal": tfrapPerfArpPerDlciRxTotal,
       "tfrapPerfArpPerDlciTxTotal": tfrapPerfArpPerDlciTxTotal,
       "tfrapPerfArpPerDlciRxArpReq": tfrapPerfArpPerDlciRxArpReq,
       "tfrapPerfArpPerDlciTxArpReq": tfrapPerfArpPerDlciTxArpReq,
       "tfrapPerfArpPerDlciRxArpRep": tfrapPerfArpPerDlciRxArpRep,
       "tfrapPerfArpPerDlciTxArpRep": tfrapPerfArpPerDlciTxArpRep,
       "tfrapPerfArpPerDlciRxRarpReq": tfrapPerfArpPerDlciRxRarpReq,
       "tfrapPerfArpPerDlciTxRarpReq": tfrapPerfArpPerDlciTxRarpReq,
       "tfrapPerfArpPerDlciRxRarpRep": tfrapPerfArpPerDlciRxRarpRep,
       "tfrapPerfArpPerDlciTxRarpRep": tfrapPerfArpPerDlciTxRarpRep,
       "tfrapPerfArpPerDlciRxInarpReq": tfrapPerfArpPerDlciRxInarpReq,
       "tfrapPerfArpPerDlciTxInarpReq": tfrapPerfArpPerDlciTxInarpReq,
       "tfrapPerfArpPerDlciRxInarpRep": tfrapPerfArpPerDlciRxInarpRep,
       "tfrapPerfArpPerDlciTxInarpRep": tfrapPerfArpPerDlciTxInarpRep,
       "tfrapPerfArpPerDlciRxOther": tfrapPerfArpPerDlciRxOther,
       "tfrapPerfArpPerDlciTxOther": tfrapPerfArpPerDlciTxOther,
       "tfrapPerfArpTotalTable": tfrapPerfArpTotalTable,
       "tfrapPerfArpTotalEntry": tfrapPerfArpTotalEntry,
       "tfrapPerfArpTotalInterval": tfrapPerfArpTotalInterval,
       "tfrapPerfArpTotalRxTotal": tfrapPerfArpTotalRxTotal,
       "tfrapPerfArpTotalTxTotal": tfrapPerfArpTotalTxTotal,
       "tfrapPerfArpTotalRxArpReq": tfrapPerfArpTotalRxArpReq,
       "tfrapPerfArpTotalTxArpReq": tfrapPerfArpTotalTxArpReq,
       "tfrapPerfArpTotalRxArpRep": tfrapPerfArpTotalRxArpRep,
       "tfrapPerfArpTotalTxArpRep": tfrapPerfArpTotalTxArpRep,
       "tfrapPerfArpTotalRxRarpReq": tfrapPerfArpTotalRxRarpReq,
       "tfrapPerfArpTotalTxRarpReq": tfrapPerfArpTotalTxRarpReq,
       "tfrapPerfArpTotalRxRarpRep": tfrapPerfArpTotalRxRarpRep,
       "tfrapPerfArpTotalTxRarpRep": tfrapPerfArpTotalTxRarpRep,
       "tfrapPerfArpTotalRxInarpReq": tfrapPerfArpTotalRxInarpReq,
       "tfrapPerfArpTotalTxInarpReq": tfrapPerfArpTotalTxInarpReq,
       "tfrapPerfArpTotalRxInarpRep": tfrapPerfArpTotalRxInarpRep,
       "tfrapPerfArpTotalTxInarpRep": tfrapPerfArpTotalTxInarpRep,
       "tfrapPerfArpTotalRxOther": tfrapPerfArpTotalRxOther,
       "tfrapPerfArpTotalTxOther": tfrapPerfArpTotalTxOther,
       "tfrapPerfLmiPerDlciTable": tfrapPerfLmiPerDlciTable,
       "tfrapPerfLmiPerDlciEntry": tfrapPerfLmiPerDlciEntry,
       "tfrapPerfLmiPerDlciInterval": tfrapPerfLmiPerDlciInterval,
       "tfrapPerfLmiPerDlciValue": tfrapPerfLmiPerDlciValue,
       "tfrapPerfLmiPerDlciRxTotalByteCnt": tfrapPerfLmiPerDlciRxTotalByteCnt,
       "tfrapPerfLmiPerDlciTxTotalByteCnt": tfrapPerfLmiPerDlciTxTotalByteCnt,
       "tfrapPerfLmiPerDlciRxLivoEnqByteCnt": tfrapPerfLmiPerDlciRxLivoEnqByteCnt,
       "tfrapPerfLmiPerDlciTxLivoEnqByteCnt": tfrapPerfLmiPerDlciTxLivoEnqByteCnt,
       "tfrapPerfLmiPerDlciRxLivoStatByteCnt": tfrapPerfLmiPerDlciRxLivoStatByteCnt,
       "tfrapPerfLmiPerDlciTxLivoStatByteCnt": tfrapPerfLmiPerDlciTxLivoStatByteCnt,
       "tfrapPerfLmiPerDlciRxFullEnqByteCnt": tfrapPerfLmiPerDlciRxFullEnqByteCnt,
       "tfrapPerfLmiPerDlciTxFullEnqByteCnt": tfrapPerfLmiPerDlciTxFullEnqByteCnt,
       "tfrapPerfLmiPerDlciRxFullStatByteCnt": tfrapPerfLmiPerDlciRxFullStatByteCnt,
       "tfrapPerfLmiPerDlciTxFullStatByteCnt": tfrapPerfLmiPerDlciTxFullStatByteCnt,
       "tfrapPerfLmiPerDlciRxOtherByteCnt": tfrapPerfLmiPerDlciRxOtherByteCnt,
       "tfrapPerfLmiPerDlciTxOtherByteCnt": tfrapPerfLmiPerDlciTxOtherByteCnt,
       "tfrapPerfLmiTotalTable": tfrapPerfLmiTotalTable,
       "tfrapPerfLmiTotalEntry": tfrapPerfLmiTotalEntry,
       "tfrapPerfLmiTotalInterval": tfrapPerfLmiTotalInterval,
       "tfrapPerfLmiTotalDlciValue": tfrapPerfLmiTotalDlciValue,
       "tfrapPerfLmiTotalRxTotalByteCnt": tfrapPerfLmiTotalRxTotalByteCnt,
       "tfrapPerfLmiTotalTxTotalByteCnt": tfrapPerfLmiTotalTxTotalByteCnt,
       "tfrapPerfLmiTotalRxLivoEnqByteCnt": tfrapPerfLmiTotalRxLivoEnqByteCnt,
       "tfrapPerfLmiTotalTxLivoEnqByteCnt": tfrapPerfLmiTotalTxLivoEnqByteCnt,
       "tfrapPerfLmiTotalRxLivoStatByteCnt": tfrapPerfLmiTotalRxLivoStatByteCnt,
       "tfrapPerfLmiTotalTxLivoStatByteCnt": tfrapPerfLmiTotalTxLivoStatByteCnt,
       "tfrapPerfLmiTotalRxFullEnqByteCnt": tfrapPerfLmiTotalRxFullEnqByteCnt,
       "tfrapPerfLmiTotalTxFullEnqByteCnt": tfrapPerfLmiTotalTxFullEnqByteCnt,
       "tfrapPerfLmiTotalRxFullStatByteCnt": tfrapPerfLmiTotalRxFullStatByteCnt,
       "tfrapPerfLmiTotalTxFullStatByteCnt": tfrapPerfLmiTotalTxFullStatByteCnt,
       "tfrapPerfLmiTotalRxOtherByteCnt": tfrapPerfLmiTotalRxOtherByteCnt,
       "tfrapPerfLmiTotalTxOtherByteCnt": tfrapPerfLmiTotalTxOtherByteCnt,
       "tfrapPerfNetworkLongTerm": tfrapPerfNetworkLongTerm,
       "tfrapPerfNetwLongTermTable": tfrapPerfNetwLongTermTable,
       "tfrapPerfNetwLongTermEntry": tfrapPerfNetwLongTermEntry,
       "tfrapPerfNetwLongTermDlci": tfrapPerfNetwLongTermDlci,
       "tfrapPerfNetwLongTermProtocol": tfrapPerfNetwLongTermProtocol,
       "tfrapPerfNetwLongTermInterval": tfrapPerfNetwLongTermInterval,
       "tfrapPerfNetwLongTermValue": tfrapPerfNetwLongTermValue,
       "tfrapPerfNetwLongTermAltTable": tfrapPerfNetwLongTermAltTable,
       "tfrapPerfNetwLongTermAltEntry": tfrapPerfNetwLongTermAltEntry,
       "tfrapPerfNetwLongTermAltDlci": tfrapPerfNetwLongTermAltDlci,
       "tfrapPerfNetwLongTermAltProtocol": tfrapPerfNetwLongTermAltProtocol,
       "tfrapPerfNetwLongTermAltArray": tfrapPerfNetwLongTermAltArray,
       "tfrapPerfNetworkLongTermCommands": tfrapPerfNetworkLongTermCommands,
       "tfrapPerfNetworkLongTermCmdClear": tfrapPerfNetworkLongTermCmdClear,
       "tfrapPerfCirPercentUtilization": tfrapPerfCirPercentUtilization,
       "tfrapPerfCirPercentUtilizationTable": tfrapPerfCirPercentUtilizationTable,
       "tfrapPerfCirPercentUtilizationEntry": tfrapPerfCirPercentUtilizationEntry,
       "tfrapPerfCirPercentUtilizationInterval": tfrapPerfCirPercentUtilizationInterval,
       "tfrapPerfCirPercentUtilizationDlciValue": tfrapPerfCirPercentUtilizationDlciValue,
       "tfrapPerfCirRxPercentUtilizationRange1": tfrapPerfCirRxPercentUtilizationRange1,
       "tfrapPerfCirRxPercentUtilizationRange2": tfrapPerfCirRxPercentUtilizationRange2,
       "tfrapPerfCirRxPercentUtilizationRange3": tfrapPerfCirRxPercentUtilizationRange3,
       "tfrapPerfCirRxPercentUtilizationRange4": tfrapPerfCirRxPercentUtilizationRange4,
       "tfrapPerfCirRxPercentUtilizationRange5": tfrapPerfCirRxPercentUtilizationRange5,
       "tfrapPerfCirRxPercentUtilizationRange6": tfrapPerfCirRxPercentUtilizationRange6,
       "tfrapPerfCirRxPercentUtilizationRange7": tfrapPerfCirRxPercentUtilizationRange7,
       "tfrapPerfCirRxPercentUtilizationRange8": tfrapPerfCirRxPercentUtilizationRange8,
       "tfrapPerfCirTxPercentUtilizationRange1": tfrapPerfCirTxPercentUtilizationRange1,
       "tfrapPerfCirTxPercentUtilizationRange2": tfrapPerfCirTxPercentUtilizationRange2,
       "tfrapPerfCirTxPercentUtilizationRange3": tfrapPerfCirTxPercentUtilizationRange3,
       "tfrapPerfCirTxPercentUtilizationRange4": tfrapPerfCirTxPercentUtilizationRange4,
       "tfrapPerfCirTxPercentUtilizationRange5": tfrapPerfCirTxPercentUtilizationRange5,
       "tfrapPerfCirTxPercentUtilizationRange6": tfrapPerfCirTxPercentUtilizationRange6,
       "tfrapPerfCirTxPercentUtilizationRange7": tfrapPerfCirTxPercentUtilizationRange7,
       "tfrapPerfCirTxPercentUtilizationRange8": tfrapPerfCirTxPercentUtilizationRange8,
       "tfrapPerfCurrentPerDlciUtilizationTable": tfrapPerfCurrentPerDlciUtilizationTable,
       "tfrapPerfCurrentPerDlciUtilizationEntry": tfrapPerfCurrentPerDlciUtilizationEntry,
       "tfrapPerfCurrentPerDlciUtilizationDlciValue": tfrapPerfCurrentPerDlciUtilizationDlciValue,
       "tfrapPerfCurrentPerDlciRxUtilization": tfrapPerfCurrentPerDlciRxUtilization,
       "tfrapPerfCurrentPerDlciTxUtilization": tfrapPerfCurrentPerDlciTxUtilization,
       "tfrapPerfCurrentPerDlciAggregateUtilization": tfrapPerfCurrentPerDlciAggregateUtilization,
       "tfrapPerfCurrentUnitUtilization": tfrapPerfCurrentUnitUtilization,
       "tfrapPerfCurrentDteUtilization": tfrapPerfCurrentDteUtilization,
       "tfrapPerfCurrentWanUtilization": tfrapPerfCurrentWanUtilization,
       "tfrapPerfCurrentAggregateUtilization": tfrapPerfCurrentAggregateUtilization,
       "tfrapAlarmType": tfrapAlarmType,
       "tfrapDLCINum": tfrapDLCINum,
       "tfrapInterface": tfrapInterface,
       "tfrapIpAddress": tfrapIpAddress,
       "tfrapEventTrapLog": tfrapEventTrapLog,
       "tfrapEventTrapLogTable": tfrapEventTrapLogTable,
       "tfrapEventTrapLogEntry": tfrapEventTrapLogEntry,
       "tfrapEventTrapLogSeqNum": tfrapEventTrapLogSeqNum,
       "tfrapEventTrapLogGenericEvent": tfrapEventTrapLogGenericEvent,
       "tfrapEventTrapLogSpecificEvent": tfrapEventTrapLogSpecificEvent,
       "tfrapEventTrapLogTimeStamp": tfrapEventTrapLogTimeStamp,
       "tfrapEventTrapLogVarBind1": tfrapEventTrapLogVarBind1,
       "tfrapEventTrapLogVarBind2": tfrapEventTrapLogVarBind2,
       "tfrapEventTrapLogVarBind3": tfrapEventTrapLogVarBind3,
       "tfrapEventLogAltTable": tfrapEventLogAltTable,
       "tfrapEventLogAltEntry": tfrapEventLogAltEntry,
       "tfrapEventLogAltSeqNum": tfrapEventLogAltSeqNum,
       "tfrapEventLogAltArray": tfrapEventLogAltArray,
       "tfrapEventLogCurrentSeqNum": tfrapEventLogCurrentSeqNum,
       "tfrapEventLogFreeze": tfrapEventLogFreeze,
       "tfrapEventLogClear": tfrapEventLogClear,
       "tfrapPercentUtilization": tfrapPercentUtilization,
       "tfrapUtilizationThreshold": tfrapUtilizationThreshold,
       "tfrapCfgLockIpAddress": tfrapCfgLockIpAddress}
)
