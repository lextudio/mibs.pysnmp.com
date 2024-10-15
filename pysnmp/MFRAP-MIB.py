# SNMP MIB module (MFRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MFRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:21 2024
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
_Mfrap_ObjectIdentity = ObjectIdentity
mfrap = _Mfrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8)
)
_MfrapSystem_ObjectIdentity = ObjectIdentity
mfrapSystem = _MfrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 1)
)
_MfrapSysTable_ObjectIdentity = ObjectIdentity
mfrapSysTable = _MfrapSysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1)
)


class _MfrapSysType_Type(DisplayString):
    """Custom type mfrapSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MfrapSysType_Type.__name__ = "DisplayString"
_MfrapSysType_Object = MibScalar
mfrapSysType = _MfrapSysType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 1),
    _MfrapSysType_Type()
)
mfrapSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysType.setStatus("mandatory")


class _MfrapSysSoftRev_Type(DisplayString):
    """Custom type mfrapSysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysSoftRev_Type.__name__ = "DisplayString"
_MfrapSysSoftRev_Object = MibScalar
mfrapSysSoftRev = _MfrapSysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 2),
    _MfrapSysSoftRev_Type()
)
mfrapSysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysSoftRev.setStatus("mandatory")


class _MfrapSysHardRev_Type(DisplayString):
    """Custom type mfrapSysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysHardRev_Type.__name__ = "DisplayString"
_MfrapSysHardRev_Object = MibScalar
mfrapSysHardRev = _MfrapSysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 3),
    _MfrapSysHardRev_Type()
)
mfrapSysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysHardRev.setStatus("mandatory")


class _MfrapSysNumT1Installed_Type(Integer32):
    """Custom type mfrapSysNumT1Installed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MfrapSysNumT1Installed_Type.__name__ = "Integer32"
_MfrapSysNumT1Installed_Object = MibScalar
mfrapSysNumT1Installed = _MfrapSysNumT1Installed_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 4),
    _MfrapSysNumT1Installed_Type()
)
mfrapSysNumT1Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumT1Installed.setStatus("mandatory")


class _MfrapSysNumDteInstalled_Type(Integer32):
    """Custom type mfrapSysNumDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MfrapSysNumDteInstalled_Type.__name__ = "Integer32"
_MfrapSysNumDteInstalled_Object = MibScalar
mfrapSysNumDteInstalled = _MfrapSysNumDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 5),
    _MfrapSysNumDteInstalled_Type()
)
mfrapSysNumDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumDteInstalled.setStatus("mandatory")


class _MfrapSysNumMaintInstalled_Type(Integer32):
    """Custom type mfrapSysNumMaintInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MfrapSysNumMaintInstalled_Type.__name__ = "Integer32"
_MfrapSysNumMaintInstalled_Object = MibScalar
mfrapSysNumMaintInstalled = _MfrapSysNumMaintInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 6),
    _MfrapSysNumMaintInstalled_Type()
)
mfrapSysNumMaintInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumMaintInstalled.setStatus("mandatory")


class _MfrapSysName_Type(DisplayString):
    """Custom type mfrapSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MfrapSysName_Type.__name__ = "DisplayString"
_MfrapSysName_Object = MibScalar
mfrapSysName = _MfrapSysName_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 7),
    _MfrapSysName_Type()
)
mfrapSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapSysName.setStatus("mandatory")


class _MfrapSysSerialNo_Type(DisplayString):
    """Custom type mfrapSysSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MfrapSysSerialNo_Type.__name__ = "DisplayString"
_MfrapSysSerialNo_Object = MibScalar
mfrapSysSerialNo = _MfrapSysSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 8),
    _MfrapSysSerialNo_Type()
)
mfrapSysSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysSerialNo.setStatus("mandatory")


class _MfrapSysResetNode_Type(Integer32):
    """Custom type mfrapSysResetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            321
        )
    )
    namedValues = NamedValues(
        ("reset-node", 321)
    )


_MfrapSysResetNode_Type.__name__ = "Integer32"
_MfrapSysResetNode_Object = MibScalar
mfrapSysResetNode = _MfrapSysResetNode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 9),
    _MfrapSysResetNode_Type()
)
mfrapSysResetNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapSysResetNode.setStatus("mandatory")
_MfrapSysAmtMemoryInstalled_Type = Integer32
_MfrapSysAmtMemoryInstalled_Object = MibScalar
mfrapSysAmtMemoryInstalled = _MfrapSysAmtMemoryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 10),
    _MfrapSysAmtMemoryInstalled_Type()
)
mfrapSysAmtMemoryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysAmtMemoryInstalled.setStatus("mandatory")


class _MfrapSysLocation_Type(DisplayString):
    """Custom type mfrapSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MfrapSysLocation_Type.__name__ = "DisplayString"
_MfrapSysLocation_Object = MibScalar
mfrapSysLocation = _MfrapSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 12),
    _MfrapSysLocation_Type()
)
mfrapSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapSysLocation.setStatus("mandatory")


class _MfrapSysContact_Type(DisplayString):
    """Custom type mfrapSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MfrapSysContact_Type.__name__ = "DisplayString"
_MfrapSysContact_Object = MibScalar
mfrapSysContact = _MfrapSysContact_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 13),
    _MfrapSysContact_Type()
)
mfrapSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapSysContact.setStatus("mandatory")


class _MfrapSysPrompt_Type(DisplayString):
    """Custom type mfrapSysPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapSysPrompt_Type.__name__ = "DisplayString"
_MfrapSysPrompt_Object = MibScalar
mfrapSysPrompt = _MfrapSysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 15),
    _MfrapSysPrompt_Type()
)
mfrapSysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapSysPrompt.setStatus("mandatory")


class _MfrapSysBootRev_Type(DisplayString):
    """Custom type mfrapSysBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysBootRev_Type.__name__ = "DisplayString"
_MfrapSysBootRev_Object = MibScalar
mfrapSysBootRev = _MfrapSysBootRev_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 16),
    _MfrapSysBootRev_Type()
)
mfrapSysBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysBootRev.setStatus("mandatory")


class _MfrapSysNestId_Type(DisplayString):
    """Custom type mfrapSysNestId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MfrapSysNestId_Type.__name__ = "DisplayString"
_MfrapSysNestId_Object = MibScalar
mfrapSysNestId = _MfrapSysNestId_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 1, 17),
    _MfrapSysNestId_Type()
)
mfrapSysNestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapSysNestId.setStatus("mandatory")
_MfrapSysFeatureTable_ObjectIdentity = ObjectIdentity
mfrapSysFeatureTable = _MfrapSysFeatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2)
)


class _MfrapSysSLIPSupported_Type(DisplayString):
    """Custom type mfrapSysSLIPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysSLIPSupported_Type.__name__ = "DisplayString"
_MfrapSysSLIPSupported_Object = MibScalar
mfrapSysSLIPSupported = _MfrapSysSLIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 1),
    _MfrapSysSLIPSupported_Type()
)
mfrapSysSLIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysSLIPSupported.setStatus("mandatory")


class _MfrapSysPPPSupported_Type(DisplayString):
    """Custom type mfrapSysPPPSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysPPPSupported_Type.__name__ = "DisplayString"
_MfrapSysPPPSupported_Object = MibScalar
mfrapSysPPPSupported = _MfrapSysPPPSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 2),
    _MfrapSysPPPSupported_Type()
)
mfrapSysPPPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysPPPSupported.setStatus("mandatory")


class _MfrapSysRDOSupported_Type(DisplayString):
    """Custom type mfrapSysRDOSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysRDOSupported_Type.__name__ = "DisplayString"
_MfrapSysRDOSupported_Object = MibScalar
mfrapSysRDOSupported = _MfrapSysRDOSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 3),
    _MfrapSysRDOSupported_Type()
)
mfrapSysRDOSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysRDOSupported.setStatus("mandatory")


class _MfrapSysETHSupported_Type(DisplayString):
    """Custom type mfrapSysETHSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysETHSupported_Type.__name__ = "DisplayString"
_MfrapSysETHSupported_Object = MibScalar
mfrapSysETHSupported = _MfrapSysETHSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 4),
    _MfrapSysETHSupported_Type()
)
mfrapSysETHSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysETHSupported.setStatus("mandatory")


class _MfrapSysTKRSupported_Type(DisplayString):
    """Custom type mfrapSysTKRSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysTKRSupported_Type.__name__ = "DisplayString"
_MfrapSysTKRSupported_Object = MibScalar
mfrapSysTKRSupported = _MfrapSysTKRSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 5),
    _MfrapSysTKRSupported_Type()
)
mfrapSysTKRSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysTKRSupported.setStatus("mandatory")


class _MfrapSysExtTimSupported_Type(DisplayString):
    """Custom type mfrapSysExtTimSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysExtTimSupported_Type.__name__ = "DisplayString"
_MfrapSysExtTimSupported_Object = MibScalar
mfrapSysExtTimSupported = _MfrapSysExtTimSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 6),
    _MfrapSysExtTimSupported_Type()
)
mfrapSysExtTimSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysExtTimSupported.setStatus("mandatory")


class _MfrapSysBRISupported_Type(DisplayString):
    """Custom type mfrapSysBRISupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysBRISupported_Type.__name__ = "DisplayString"
_MfrapSysBRISupported_Object = MibScalar
mfrapSysBRISupported = _MfrapSysBRISupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 7),
    _MfrapSysBRISupported_Type()
)
mfrapSysBRISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysBRISupported.setStatus("mandatory")


class _MfrapSysSelDTESupported_Type(DisplayString):
    """Custom type mfrapSysSelDTESupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysSelDTESupported_Type.__name__ = "DisplayString"
_MfrapSysSelDTESupported_Object = MibScalar
mfrapSysSelDTESupported = _MfrapSysSelDTESupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 8),
    _MfrapSysSelDTESupported_Type()
)
mfrapSysSelDTESupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysSelDTESupported.setStatus("mandatory")


class _MfrapSysMLSupported_Type(DisplayString):
    """Custom type mfrapSysMLSupported based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MfrapSysMLSupported_Type.__name__ = "DisplayString"
_MfrapSysMLSupported_Object = MibScalar
mfrapSysMLSupported = _MfrapSysMLSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 9),
    _MfrapSysMLSupported_Type()
)
mfrapSysMLSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysMLSupported.setStatus("mandatory")
_MfrapSysNumDlcisSupported_Type = Integer32
_MfrapSysNumDlcisSupported_Object = MibScalar
mfrapSysNumDlcisSupported = _MfrapSysNumDlcisSupported_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 10),
    _MfrapSysNumDlcisSupported_Type()
)
mfrapSysNumDlcisSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumDlcisSupported.setStatus("mandatory")
_MfrapSysLTFNumDlcis_Type = Integer32
_MfrapSysLTFNumDlcis_Object = MibScalar
mfrapSysLTFNumDlcis = _MfrapSysLTFNumDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 11),
    _MfrapSysLTFNumDlcis_Type()
)
mfrapSysLTFNumDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysLTFNumDlcis.setStatus("mandatory")
_MfrapSysLTFNumProtocols_Type = Integer32
_MfrapSysLTFNumProtocols_Object = MibScalar
mfrapSysLTFNumProtocols = _MfrapSysLTFNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 12),
    _MfrapSysLTFNumProtocols_Type()
)
mfrapSysLTFNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysLTFNumProtocols.setStatus("mandatory")
_MfrapSysNumUserProtocols_Type = Integer32
_MfrapSysNumUserProtocols_Object = MibScalar
mfrapSysNumUserProtocols = _MfrapSysNumUserProtocols_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 13),
    _MfrapSysNumUserProtocols_Type()
)
mfrapSysNumUserProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumUserProtocols.setStatus("mandatory")
_MfrapSysNumSnmpMgrs_Type = Integer32
_MfrapSysNumSnmpMgrs_Object = MibScalar
mfrapSysNumSnmpMgrs = _MfrapSysNumSnmpMgrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 14),
    _MfrapSysNumSnmpMgrs_Type()
)
mfrapSysNumSnmpMgrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumSnmpMgrs.setStatus("mandatory")
_MfrapSysNumDlciNames_Type = Integer32
_MfrapSysNumDlciNames_Object = MibScalar
mfrapSysNumDlciNames = _MfrapSysNumDlciNames_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 1, 2, 15),
    _MfrapSysNumDlciNames_Type()
)
mfrapSysNumDlciNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapSysNumDlciNames.setStatus("mandatory")
_MfrapConfiguration_ObjectIdentity = ObjectIdentity
mfrapConfiguration = _MfrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2)
)
_MfrapCfgMgmtTable_ObjectIdentity = ObjectIdentity
mfrapCfgMgmtTable = _MfrapCfgMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1)
)
_MfrapCfgIpTable_ObjectIdentity = ObjectIdentity
mfrapCfgIpTable = _MfrapCfgIpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1)
)
_MfrapCfgIpMyIP_Type = IpAddress
_MfrapCfgIpMyIP_Object = MibScalar
mfrapCfgIpMyIP = _MfrapCfgIpMyIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 1),
    _MfrapCfgIpMyIP_Type()
)
mfrapCfgIpMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpMyIP.setStatus("mandatory")
_MfrapCfgIpPeerIP_Type = IpAddress
_MfrapCfgIpPeerIP_Object = MibScalar
mfrapCfgIpPeerIP = _MfrapCfgIpPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 2),
    _MfrapCfgIpPeerIP_Type()
)
mfrapCfgIpPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpPeerIP.setStatus("mandatory")
_MfrapCfgIpMask_Type = IpAddress
_MfrapCfgIpMask_Object = MibScalar
mfrapCfgIpMask = _MfrapCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 3),
    _MfrapCfgIpMask_Type()
)
mfrapCfgIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpMask.setStatus("mandatory")


class _MfrapCfgIpMaxMTU_Type(Integer32):
    """Custom type mfrapCfgIpMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MfrapCfgIpMaxMTU_Type.__name__ = "Integer32"
_MfrapCfgIpMaxMTU_Object = MibScalar
mfrapCfgIpMaxMTU = _MfrapCfgIpMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 4),
    _MfrapCfgIpMaxMTU_Type()
)
mfrapCfgIpMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpMaxMTU.setStatus("mandatory")


class _MfrapCfgIpChannel_Type(Integer32):
    """Custom type mfrapCfgIpChannel based on Integer32"""
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


_MfrapCfgIpChannel_Type.__name__ = "Integer32"
_MfrapCfgIpChannel_Object = MibScalar
mfrapCfgIpChannel = _MfrapCfgIpChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 5),
    _MfrapCfgIpChannel_Type()
)
mfrapCfgIpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgIpChannel.setStatus("mandatory")


class _MfrapCfgIpTelnetEnable_Type(Integer32):
    """Custom type mfrapCfgIpTelnetEnable based on Integer32"""
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


_MfrapCfgIpTelnetEnable_Type.__name__ = "Integer32"
_MfrapCfgIpTelnetEnable_Object = MibScalar
mfrapCfgIpTelnetEnable = _MfrapCfgIpTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 6),
    _MfrapCfgIpTelnetEnable_Type()
)
mfrapCfgIpTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpTelnetEnable.setStatus("mandatory")


class _MfrapCfgIpTelnetAutoLogOut_Type(Integer32):
    """Custom type mfrapCfgIpTelnetAutoLogOut based on Integer32"""
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


_MfrapCfgIpTelnetAutoLogOut_Type.__name__ = "Integer32"
_MfrapCfgIpTelnetAutoLogOut_Object = MibScalar
mfrapCfgIpTelnetAutoLogOut = _MfrapCfgIpTelnetAutoLogOut_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 1, 7),
    _MfrapCfgIpTelnetAutoLogOut_Type()
)
mfrapCfgIpTelnetAutoLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgIpTelnetAutoLogOut.setStatus("mandatory")
_MfrapCfgTftpTable_ObjectIdentity = ObjectIdentity
mfrapCfgTftpTable = _MfrapCfgTftpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2)
)


class _MfrapCfgTftpInitiate_Type(DisplayString):
    """Custom type mfrapCfgTftpInitiate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgTftpInitiate_Type.__name__ = "DisplayString"
_MfrapCfgTftpInitiate_Object = MibScalar
mfrapCfgTftpInitiate = _MfrapCfgTftpInitiate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 1),
    _MfrapCfgTftpInitiate_Type()
)
mfrapCfgTftpInitiate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgTftpInitiate.setStatus("mandatory")
_MfrapCfgTftpIpAddress_Type = IpAddress
_MfrapCfgTftpIpAddress_Object = MibScalar
mfrapCfgTftpIpAddress = _MfrapCfgTftpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 2),
    _MfrapCfgTftpIpAddress_Type()
)
mfrapCfgTftpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpIpAddress.setStatus("mandatory")


class _MfrapCfgTftpFilename_Type(DisplayString):
    """Custom type mfrapCfgTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MfrapCfgTftpFilename_Type.__name__ = "DisplayString"
_MfrapCfgTftpFilename_Object = MibScalar
mfrapCfgTftpFilename = _MfrapCfgTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 3),
    _MfrapCfgTftpFilename_Type()
)
mfrapCfgTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpFilename.setStatus("mandatory")


class _MfrapCfgTftpInterface_Type(Integer32):
    """Custom type mfrapCfgTftpInterface based on Integer32"""
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


_MfrapCfgTftpInterface_Type.__name__ = "Integer32"
_MfrapCfgTftpInterface_Object = MibScalar
mfrapCfgTftpInterface = _MfrapCfgTftpInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 4),
    _MfrapCfgTftpInterface_Type()
)
mfrapCfgTftpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpInterface.setStatus("mandatory")


class _MfrapCfgTftpDlci_Type(Integer32):
    """Custom type mfrapCfgTftpDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63487),
    )


_MfrapCfgTftpDlci_Type.__name__ = "Integer32"
_MfrapCfgTftpDlci_Object = MibScalar
mfrapCfgTftpDlci = _MfrapCfgTftpDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 5),
    _MfrapCfgTftpDlci_Type()
)
mfrapCfgTftpDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpDlci.setStatus("mandatory")


class _MfrapCfgTftpStatus_Type(Integer32):
    """Custom type mfrapCfgTftpStatus based on Integer32"""
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


_MfrapCfgTftpStatus_Type.__name__ = "Integer32"
_MfrapCfgTftpStatus_Object = MibScalar
mfrapCfgTftpStatus = _MfrapCfgTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 6),
    _MfrapCfgTftpStatus_Type()
)
mfrapCfgTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpStatus.setStatus("mandatory")
_MfrapCfgTftpNumBytes_Type = Counter32
_MfrapCfgTftpNumBytes_Object = MibScalar
mfrapCfgTftpNumBytes = _MfrapCfgTftpNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 2, 7),
    _MfrapCfgTftpNumBytes_Type()
)
mfrapCfgTftpNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgTftpNumBytes.setStatus("mandatory")
_MfrapCfgSnmpTable_ObjectIdentity = ObjectIdentity
mfrapCfgSnmpTable = _MfrapCfgSnmpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3)
)


class _MfrapCfgSnmpFrTrap_Type(Integer32):
    """Custom type mfrapCfgSnmpFrTrap based on Integer32"""
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


_MfrapCfgSnmpFrTrap_Type.__name__ = "Integer32"
_MfrapCfgSnmpFrTrap_Object = MibScalar
mfrapCfgSnmpFrTrap = _MfrapCfgSnmpFrTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 1),
    _MfrapCfgSnmpFrTrap_Type()
)
mfrapCfgSnmpFrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpFrTrap.setStatus("mandatory")
_MfrapCfgSnmpMgrTable_Object = MibTable
mfrapCfgSnmpMgrTable = _MfrapCfgSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrTable.setStatus("mandatory")
_MfrapCfgSnmpMgrEntry_Object = MibTableRow
mfrapCfgSnmpMgrEntry = _MfrapCfgSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2, 1)
)
mfrapCfgSnmpMgrEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgSnmpMgrIndex"),
)
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrEntry.setStatus("mandatory")
_MfrapCfgSnmpMgrIndex_Type = Integer32
_MfrapCfgSnmpMgrIndex_Object = MibTableColumn
mfrapCfgSnmpMgrIndex = _MfrapCfgSnmpMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2, 1, 1),
    _MfrapCfgSnmpMgrIndex_Type()
)
mfrapCfgSnmpMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrIndex.setStatus("mandatory")
_MfrapCfgSnmpMgrIP_Type = IpAddress
_MfrapCfgSnmpMgrIP_Object = MibTableColumn
mfrapCfgSnmpMgrIP = _MfrapCfgSnmpMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2, 1, 2),
    _MfrapCfgSnmpMgrIP_Type()
)
mfrapCfgSnmpMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrIP.setStatus("mandatory")


class _MfrapCfgSnmpMgrInterface_Type(Integer32):
    """Custom type mfrapCfgSnmpMgrInterface based on Integer32"""
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


_MfrapCfgSnmpMgrInterface_Type.__name__ = "Integer32"
_MfrapCfgSnmpMgrInterface_Object = MibTableColumn
mfrapCfgSnmpMgrInterface = _MfrapCfgSnmpMgrInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2, 1, 3),
    _MfrapCfgSnmpMgrInterface_Type()
)
mfrapCfgSnmpMgrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrInterface.setStatus("mandatory")
_MfrapCfgSnmpMgrDlci_Type = Integer32
_MfrapCfgSnmpMgrDlci_Object = MibTableColumn
mfrapCfgSnmpMgrDlci = _MfrapCfgSnmpMgrDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 2, 1, 4),
    _MfrapCfgSnmpMgrDlci_Type()
)
mfrapCfgSnmpMgrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrDlci.setStatus("mandatory")


class _MfrapCfgSnmpTrapMuting_Type(Integer32):
    """Custom type mfrapCfgSnmpTrapMuting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_MfrapCfgSnmpTrapMuting_Type.__name__ = "Integer32"
_MfrapCfgSnmpTrapMuting_Object = MibScalar
mfrapCfgSnmpTrapMuting = _MfrapCfgSnmpTrapMuting_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 3),
    _MfrapCfgSnmpTrapMuting_Type()
)
mfrapCfgSnmpTrapMuting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpTrapMuting.setStatus("mandatory")


class _MfrapCfgSnmpNestAlarmTrapEnable_Type(Integer32):
    """Custom type mfrapCfgSnmpNestAlarmTrapEnable based on Integer32"""
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


_MfrapCfgSnmpNestAlarmTrapEnable_Type.__name__ = "Integer32"
_MfrapCfgSnmpNestAlarmTrapEnable_Object = MibScalar
mfrapCfgSnmpNestAlarmTrapEnable = _MfrapCfgSnmpNestAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 4),
    _MfrapCfgSnmpNestAlarmTrapEnable_Type()
)
mfrapCfgSnmpNestAlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpNestAlarmTrapEnable.setStatus("mandatory")


class _MfrapCfgSnmpDandIPortTrapEnable_Type(Integer32):
    """Custom type mfrapCfgSnmpDandIPortTrapEnable based on Integer32"""
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


_MfrapCfgSnmpDandIPortTrapEnable_Type.__name__ = "Integer32"
_MfrapCfgSnmpDandIPortTrapEnable_Object = MibScalar
mfrapCfgSnmpDandIPortTrapEnable = _MfrapCfgSnmpDandIPortTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 5),
    _MfrapCfgSnmpDandIPortTrapEnable_Type()
)
mfrapCfgSnmpDandIPortTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpDandIPortTrapEnable.setStatus("mandatory")


class _MfrapCfgSnmpUtilTrapEnable_Type(Integer32):
    """Custom type mfrapCfgSnmpUtilTrapEnable based on Integer32"""
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


_MfrapCfgSnmpUtilTrapEnable_Type.__name__ = "Integer32"
_MfrapCfgSnmpUtilTrapEnable_Object = MibScalar
mfrapCfgSnmpUtilTrapEnable = _MfrapCfgSnmpUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 6),
    _MfrapCfgSnmpUtilTrapEnable_Type()
)
mfrapCfgSnmpUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSnmpUtilTrapEnable.setStatus("mandatory")
_MfrapCfgSnmpMgrClearN_Type = Integer32
_MfrapCfgSnmpMgrClearN_Object = MibScalar
mfrapCfgSnmpMgrClearN = _MfrapCfgSnmpMgrClearN_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 3, 7),
    _MfrapCfgSnmpMgrClearN_Type()
)
mfrapCfgSnmpMgrClearN.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgSnmpMgrClearN.setStatus("mandatory")
_MfrapCfgCommTable_ObjectIdentity = ObjectIdentity
mfrapCfgCommTable = _MfrapCfgCommTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4)
)


class _MfrapCfgCommMode_Type(Integer32):
    """Custom type mfrapCfgCommMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modem", 3),
          ("slip", 2),
          ("vt100", 1))
    )


_MfrapCfgCommMode_Type.__name__ = "Integer32"
_MfrapCfgCommMode_Object = MibScalar
mfrapCfgCommMode = _MfrapCfgCommMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 1),
    _MfrapCfgCommMode_Type()
)
mfrapCfgCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommMode.setStatus("mandatory")


class _MfrapCfgCommBaud_Type(Integer32):
    """Custom type mfrapCfgCommBaud based on Integer32"""
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


_MfrapCfgCommBaud_Type.__name__ = "Integer32"
_MfrapCfgCommBaud_Object = MibScalar
mfrapCfgCommBaud = _MfrapCfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 2),
    _MfrapCfgCommBaud_Type()
)
mfrapCfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommBaud.setStatus("mandatory")


class _MfrapCfgCommDataBits_Type(Integer32):
    """Custom type mfrapCfgCommDataBits based on Integer32"""
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


_MfrapCfgCommDataBits_Type.__name__ = "Integer32"
_MfrapCfgCommDataBits_Object = MibScalar
mfrapCfgCommDataBits = _MfrapCfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 3),
    _MfrapCfgCommDataBits_Type()
)
mfrapCfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommDataBits.setStatus("mandatory")


class _MfrapCfgCommStopBits_Type(Integer32):
    """Custom type mfrapCfgCommStopBits based on Integer32"""
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


_MfrapCfgCommStopBits_Type.__name__ = "Integer32"
_MfrapCfgCommStopBits_Object = MibScalar
mfrapCfgCommStopBits = _MfrapCfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 4),
    _MfrapCfgCommStopBits_Type()
)
mfrapCfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommStopBits.setStatus("mandatory")


class _MfrapCfgCommParity_Type(Integer32):
    """Custom type mfrapCfgCommParity based on Integer32"""
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


_MfrapCfgCommParity_Type.__name__ = "Integer32"
_MfrapCfgCommParity_Object = MibScalar
mfrapCfgCommParity = _MfrapCfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 5),
    _MfrapCfgCommParity_Type()
)
mfrapCfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommParity.setStatus("mandatory")


class _MfrapCfgCommFlowCtrl_Type(Integer32):
    """Custom type mfrapCfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("no-flow-control", 1)
    )


_MfrapCfgCommFlowCtrl_Type.__name__ = "Integer32"
_MfrapCfgCommFlowCtrl_Object = MibScalar
mfrapCfgCommFlowCtrl = _MfrapCfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 6),
    _MfrapCfgCommFlowCtrl_Type()
)
mfrapCfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommFlowCtrl.setStatus("mandatory")


class _MfrapCfgCommModeAutoDetect_Type(Integer32):
    """Custom type mfrapCfgCommModeAutoDetect based on Integer32"""
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


_MfrapCfgCommModeAutoDetect_Type.__name__ = "Integer32"
_MfrapCfgCommModeAutoDetect_Object = MibScalar
mfrapCfgCommModeAutoDetect = _MfrapCfgCommModeAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 4, 7),
    _MfrapCfgCommModeAutoDetect_Type()
)
mfrapCfgCommModeAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCommModeAutoDetect.setStatus("mandatory")
_MfrapCfgFrDLCITable_ObjectIdentity = ObjectIdentity
mfrapCfgFrDLCITable = _MfrapCfgFrDLCITable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 5)
)


class _MfrapCfgFrDLCIMode_Type(Integer32):
    """Custom type mfrapCfgFrDLCIMode based on Integer32"""
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


_MfrapCfgFrDLCIMode_Type.__name__ = "Integer32"
_MfrapCfgFrDLCIMode_Object = MibScalar
mfrapCfgFrDLCIMode = _MfrapCfgFrDLCIMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 5, 1),
    _MfrapCfgFrDLCIMode_Type()
)
mfrapCfgFrDLCIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrDLCIMode.setStatus("mandatory")


class _MfrapCfgFrDLCIValue_Type(Integer32):
    """Custom type mfrapCfgFrDLCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 63487),
    )


_MfrapCfgFrDLCIValue_Type.__name__ = "Integer32"
_MfrapCfgFrDLCIValue_Object = MibScalar
mfrapCfgFrDLCIValue = _MfrapCfgFrDLCIValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 5, 2),
    _MfrapCfgFrDLCIValue_Type()
)
mfrapCfgFrDLCIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrDLCIValue.setStatus("mandatory")


class _MfrapCfgFrDLCIEncap_Type(Integer32):
    """Custom type mfrapCfgFrDLCIEncap based on Integer32"""
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


_MfrapCfgFrDLCIEncap_Type.__name__ = "Integer32"
_MfrapCfgFrDLCIEncap_Object = MibScalar
mfrapCfgFrDLCIEncap = _MfrapCfgFrDLCIEncap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 5, 3),
    _MfrapCfgFrDLCIEncap_Type()
)
mfrapCfgFrDLCIEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrDLCIEncap.setStatus("mandatory")


class _MfrapCfgFrDLCIMgmtDE_Type(Integer32):
    """Custom type mfrapCfgFrDLCIMgmtDE based on Integer32"""
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


_MfrapCfgFrDLCIMgmtDE_Type.__name__ = "Integer32"
_MfrapCfgFrDLCIMgmtDE_Object = MibScalar
mfrapCfgFrDLCIMgmtDE = _MfrapCfgFrDLCIMgmtDE_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 1, 5, 4),
    _MfrapCfgFrDLCIMgmtDE_Type()
)
mfrapCfgFrDLCIMgmtDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrDLCIMgmtDE.setStatus("mandatory")
_MfrapCfgAppTable_ObjectIdentity = ObjectIdentity
mfrapCfgAppTable = _MfrapCfgAppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2)
)


class _MfrapCfgAppClockSource_Type(Integer32):
    """Custom type mfrapCfgAppClockSource based on Integer32"""
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
        *(("drop-and-insert", 4),
          ("dte", 3),
          ("internal", 1),
          ("network", 2))
    )


_MfrapCfgAppClockSource_Type.__name__ = "Integer32"
_MfrapCfgAppClockSource_Object = MibScalar
mfrapCfgAppClockSource = _MfrapCfgAppClockSource_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 1),
    _MfrapCfgAppClockSource_Type()
)
mfrapCfgAppClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppClockSource.setStatus("mandatory")


class _MfrapCfgAppCircuitId_Type(DisplayString):
    """Custom type mfrapCfgAppCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MfrapCfgAppCircuitId_Type.__name__ = "DisplayString"
_MfrapCfgAppCircuitId_Object = MibScalar
mfrapCfgAppCircuitId = _MfrapCfgAppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 2),
    _MfrapCfgAppCircuitId_Type()
)
mfrapCfgAppCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppCircuitId.setStatus("mandatory")


class _MfrapCfgAppType_Type(Integer32):
    """Custom type mfrapCfgAppType based on Integer32"""
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


_MfrapCfgAppType_Type.__name__ = "Integer32"
_MfrapCfgAppType_Object = MibScalar
mfrapCfgAppType = _MfrapCfgAppType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 3),
    _MfrapCfgAppType_Type()
)
mfrapCfgAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppType.setStatus("mandatory")


class _MfrapCfgAppFormat_Type(Integer32):
    """Custom type mfrapCfgAppFormat based on Integer32"""
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


_MfrapCfgAppFormat_Type.__name__ = "Integer32"
_MfrapCfgAppFormat_Object = MibScalar
mfrapCfgAppFormat = _MfrapCfgAppFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 4),
    _MfrapCfgAppFormat_Type()
)
mfrapCfgAppFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppFormat.setStatus("mandatory")


class _MfrapCfgAppLpbkTimeout_Type(Integer32):
    """Custom type mfrapCfgAppLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_MfrapCfgAppLpbkTimeout_Type.__name__ = "Integer32"
_MfrapCfgAppLpbkTimeout_Object = MibScalar
mfrapCfgAppLpbkTimeout = _MfrapCfgAppLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 5),
    _MfrapCfgAppLpbkTimeout_Type()
)
mfrapCfgAppLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppLpbkTimeout.setStatus("mandatory")


class _MfrapCfgAppPerfBuffLimit_Type(Integer32):
    """Custom type mfrapCfgAppPerfBuffLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_MfrapCfgAppPerfBuffLimit_Type.__name__ = "Integer32"
_MfrapCfgAppPerfBuffLimit_Object = MibScalar
mfrapCfgAppPerfBuffLimit = _MfrapCfgAppPerfBuffLimit_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 2, 10),
    _MfrapCfgAppPerfBuffLimit_Type()
)
mfrapCfgAppPerfBuffLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgAppPerfBuffLimit.setStatus("mandatory")
_MfrapCfgT1Table_ObjectIdentity = ObjectIdentity
mfrapCfgT1Table = _MfrapCfgT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3)
)


class _MfrapCfgT1Framing_Type(Integer32):
    """Custom type mfrapCfgT1Framing based on Integer32"""
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


_MfrapCfgT1Framing_Type.__name__ = "Integer32"
_MfrapCfgT1Framing_Object = MibScalar
mfrapCfgT1Framing = _MfrapCfgT1Framing_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3, 1),
    _MfrapCfgT1Framing_Type()
)
mfrapCfgT1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgT1Framing.setStatus("mandatory")


class _MfrapCfgT1LineEncoding_Type(Integer32):
    """Custom type mfrapCfgT1LineEncoding based on Integer32"""
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


_MfrapCfgT1LineEncoding_Type.__name__ = "Integer32"
_MfrapCfgT1LineEncoding_Object = MibScalar
mfrapCfgT1LineEncoding = _MfrapCfgT1LineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3, 2),
    _MfrapCfgT1LineEncoding_Type()
)
mfrapCfgT1LineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgT1LineEncoding.setStatus("mandatory")


class _MfrapCfgT1Density_Type(Integer32):
    """Custom type mfrapCfgT1Density based on Integer32"""
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


_MfrapCfgT1Density_Type.__name__ = "Integer32"
_MfrapCfgT1Density_Object = MibScalar
mfrapCfgT1Density = _MfrapCfgT1Density_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3, 3),
    _MfrapCfgT1Density_Type()
)
mfrapCfgT1Density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgT1Density.setStatus("mandatory")


class _MfrapCfgT1Interface_Type(Integer32):
    """Custom type mfrapCfgT1Interface based on Integer32"""
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


_MfrapCfgT1Interface_Type.__name__ = "Integer32"
_MfrapCfgT1Interface_Object = MibScalar
mfrapCfgT1Interface = _MfrapCfgT1Interface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3, 4),
    _MfrapCfgT1Interface_Type()
)
mfrapCfgT1Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgT1Interface.setStatus("mandatory")


class _MfrapCfgT1LboSetting_Type(Integer32):
    """Custom type mfrapCfgT1LboSetting based on Integer32"""
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


_MfrapCfgT1LboSetting_Type.__name__ = "Integer32"
_MfrapCfgT1LboSetting_Object = MibScalar
mfrapCfgT1LboSetting = _MfrapCfgT1LboSetting_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 3, 5),
    _MfrapCfgT1LboSetting_Type()
)
mfrapCfgT1LboSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgT1LboSetting.setStatus("mandatory")
_MfrapCfgDteTable_ObjectIdentity = ObjectIdentity
mfrapCfgDteTable = _MfrapCfgDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4)
)


class _MfrapCfgDteIntfType_Type(Integer32):
    """Custom type mfrapCfgDteIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("intf-v35", 3)
    )


_MfrapCfgDteIntfType_Type.__name__ = "Integer32"
_MfrapCfgDteIntfType_Object = MibScalar
mfrapCfgDteIntfType = _MfrapCfgDteIntfType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 1),
    _MfrapCfgDteIntfType_Type()
)
mfrapCfgDteIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteIntfType.setStatus("mandatory")


class _MfrapCfgDteDataMode_Type(Integer32):
    """Custom type mfrapCfgDteDataMode based on Integer32"""
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


_MfrapCfgDteDataMode_Type.__name__ = "Integer32"
_MfrapCfgDteDataMode_Object = MibScalar
mfrapCfgDteDataMode = _MfrapCfgDteDataMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 2),
    _MfrapCfgDteDataMode_Type()
)
mfrapCfgDteDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteDataMode.setStatus("mandatory")


class _MfrapCfgDteClockMode_Type(Integer32):
    """Custom type mfrapCfgDteClockMode based on Integer32"""
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


_MfrapCfgDteClockMode_Type.__name__ = "Integer32"
_MfrapCfgDteClockMode_Object = MibScalar
mfrapCfgDteClockMode = _MfrapCfgDteClockMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 3),
    _MfrapCfgDteClockMode_Type()
)
mfrapCfgDteClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteClockMode.setStatus("mandatory")


class _MfrapCfgDteTiming_Type(Integer32):
    """Custom type mfrapCfgDteTiming based on Integer32"""
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


_MfrapCfgDteTiming_Type.__name__ = "Integer32"
_MfrapCfgDteTiming_Object = MibScalar
mfrapCfgDteTiming = _MfrapCfgDteTiming_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 4),
    _MfrapCfgDteTiming_Type()
)
mfrapCfgDteTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteTiming.setStatus("mandatory")


class _MfrapCfgDteLineRate_Type(Integer32):
    """Custom type mfrapCfgDteLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_MfrapCfgDteLineRate_Type.__name__ = "Integer32"
_MfrapCfgDteLineRate_Object = MibScalar
mfrapCfgDteLineRate = _MfrapCfgDteLineRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 5),
    _MfrapCfgDteLineRate_Type()
)
mfrapCfgDteLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteLineRate.setStatus("mandatory")


class _MfrapCfgDteChannelDensity_Type(Integer32):
    """Custom type mfrapCfgDteChannelDensity based on Integer32"""
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


_MfrapCfgDteChannelDensity_Type.__name__ = "Integer32"
_MfrapCfgDteChannelDensity_Object = MibScalar
mfrapCfgDteChannelDensity = _MfrapCfgDteChannelDensity_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 6),
    _MfrapCfgDteChannelDensity_Type()
)
mfrapCfgDteChannelDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteChannelDensity.setStatus("mandatory")


class _MfrapCfgDteStartDs0_Type(Integer32):
    """Custom type mfrapCfgDteStartDs0 based on Integer32"""
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


_MfrapCfgDteStartDs0_Type.__name__ = "Integer32"
_MfrapCfgDteStartDs0_Object = MibScalar
mfrapCfgDteStartDs0 = _MfrapCfgDteStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 7),
    _MfrapCfgDteStartDs0_Type()
)
mfrapCfgDteStartDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteStartDs0.setStatus("mandatory")


class _MfrapCfgDteConnStatus_Type(Integer32):
    """Custom type mfrapCfgDteConnStatus based on Integer32"""
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


_MfrapCfgDteConnStatus_Type.__name__ = "Integer32"
_MfrapCfgDteConnStatus_Object = MibScalar
mfrapCfgDteConnStatus = _MfrapCfgDteConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 8),
    _MfrapCfgDteConnStatus_Type()
)
mfrapCfgDteConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteConnStatus.setStatus("mandatory")


class _MfrapCfgDteConnStartDs0_Type(Integer32):
    """Custom type mfrapCfgDteConnStartDs0 based on Integer32"""
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


_MfrapCfgDteConnStartDs0_Type.__name__ = "Integer32"
_MfrapCfgDteConnStartDs0_Object = MibScalar
mfrapCfgDteConnStartDs0 = _MfrapCfgDteConnStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 9),
    _MfrapCfgDteConnStartDs0_Type()
)
mfrapCfgDteConnStartDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteConnStartDs0.setStatus("mandatory")


class _MfrapCfgDteConnRate_Type(Integer32):
    """Custom type mfrapCfgDteConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_MfrapCfgDteConnRate_Type.__name__ = "Integer32"
_MfrapCfgDteConnRate_Object = MibScalar
mfrapCfgDteConnRate = _MfrapCfgDteConnRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 10),
    _MfrapCfgDteConnRate_Type()
)
mfrapCfgDteConnRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteConnRate.setStatus("mandatory")


class _MfrapCfgDteConnDensity_Type(Integer32):
    """Custom type mfrapCfgDteConnDensity based on Integer32"""
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


_MfrapCfgDteConnDensity_Type.__name__ = "Integer32"
_MfrapCfgDteConnDensity_Object = MibScalar
mfrapCfgDteConnDensity = _MfrapCfgDteConnDensity_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 11),
    _MfrapCfgDteConnDensity_Type()
)
mfrapCfgDteConnDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteConnDensity.setStatus("mandatory")


class _MfrapCfgDteConnDs0Required_Type(Integer32):
    """Custom type mfrapCfgDteConnDs0Required based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_MfrapCfgDteConnDs0Required_Type.__name__ = "Integer32"
_MfrapCfgDteConnDs0Required_Object = MibScalar
mfrapCfgDteConnDs0Required = _MfrapCfgDteConnDs0Required_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 12),
    _MfrapCfgDteConnDs0Required_Type()
)
mfrapCfgDteConnDs0Required.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteConnDs0Required.setStatus("mandatory")


class _MfrapCfgDteConnAutoStatus_Type(Integer32):
    """Custom type mfrapCfgDteConnAutoStatus based on Integer32"""
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


_MfrapCfgDteConnAutoStatus_Type.__name__ = "Integer32"
_MfrapCfgDteConnAutoStatus_Object = MibScalar
mfrapCfgDteConnAutoStatus = _MfrapCfgDteConnAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 13),
    _MfrapCfgDteConnAutoStatus_Type()
)
mfrapCfgDteConnAutoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgDteConnAutoStatus.setStatus("mandatory")


class _MfrapCfgDteConnAutoUpdate_Type(Integer32):
    """Custom type mfrapCfgDteConnAutoUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("config-and-connect", 1)
    )


_MfrapCfgDteConnAutoUpdate_Type.__name__ = "Integer32"
_MfrapCfgDteConnAutoUpdate_Object = MibScalar
mfrapCfgDteConnAutoUpdate = _MfrapCfgDteConnAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 14),
    _MfrapCfgDteConnAutoUpdate_Type()
)
mfrapCfgDteConnAutoUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgDteConnAutoUpdate.setStatus("mandatory")


class _MfrapCfgDteRts_Type(Integer32):
    """Custom type mfrapCfgDteRts based on Integer32"""
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


_MfrapCfgDteRts_Type.__name__ = "Integer32"
_MfrapCfgDteRts_Object = MibScalar
mfrapCfgDteRts = _MfrapCfgDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 15),
    _MfrapCfgDteRts_Type()
)
mfrapCfgDteRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteRts.setStatus("mandatory")


class _MfrapCfgDteDtr_Type(Integer32):
    """Custom type mfrapCfgDteDtr based on Integer32"""
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


_MfrapCfgDteDtr_Type.__name__ = "Integer32"
_MfrapCfgDteDtr_Object = MibScalar
mfrapCfgDteDtr = _MfrapCfgDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 16),
    _MfrapCfgDteDtr_Type()
)
mfrapCfgDteDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteDtr.setStatus("mandatory")


class _MfrapCfgDteDcdOutput_Type(Integer32):
    """Custom type mfrapCfgDteDcdOutput based on Integer32"""
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


_MfrapCfgDteDcdOutput_Type.__name__ = "Integer32"
_MfrapCfgDteDcdOutput_Object = MibScalar
mfrapCfgDteDcdOutput = _MfrapCfgDteDcdOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 18),
    _MfrapCfgDteDcdOutput_Type()
)
mfrapCfgDteDcdOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteDcdOutput.setStatus("mandatory")


class _MfrapCfgDteDsrOutput_Type(Integer32):
    """Custom type mfrapCfgDteDsrOutput based on Integer32"""
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


_MfrapCfgDteDsrOutput_Type.__name__ = "Integer32"
_MfrapCfgDteDsrOutput_Object = MibScalar
mfrapCfgDteDsrOutput = _MfrapCfgDteDsrOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 19),
    _MfrapCfgDteDsrOutput_Type()
)
mfrapCfgDteDsrOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteDsrOutput.setStatus("mandatory")


class _MfrapCfgDteCtsOutput_Type(Integer32):
    """Custom type mfrapCfgDteCtsOutput based on Integer32"""
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


_MfrapCfgDteCtsOutput_Type.__name__ = "Integer32"
_MfrapCfgDteCtsOutput_Object = MibScalar
mfrapCfgDteCtsOutput = _MfrapCfgDteCtsOutput_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 4, 20),
    _MfrapCfgDteCtsOutput_Type()
)
mfrapCfgDteCtsOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDteCtsOutput.setStatus("mandatory")
_MfrapCfgFrTable_ObjectIdentity = ObjectIdentity
mfrapCfgFrTable = _MfrapCfgFrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5)
)


class _MfrapCfgFrAddrLen_Type(Integer32):
    """Custom type mfrapCfgFrAddrLen based on Integer32"""
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


_MfrapCfgFrAddrLen_Type.__name__ = "Integer32"
_MfrapCfgFrAddrLen_Object = MibScalar
mfrapCfgFrAddrLen = _MfrapCfgFrAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 1),
    _MfrapCfgFrAddrLen_Type()
)
mfrapCfgFrAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrAddrLen.setStatus("mandatory")


class _MfrapCfgFrCrcMode_Type(Integer32):
    """Custom type mfrapCfgFrCrcMode based on Integer32"""
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


_MfrapCfgFrCrcMode_Type.__name__ = "Integer32"
_MfrapCfgFrCrcMode_Object = MibScalar
mfrapCfgFrCrcMode = _MfrapCfgFrCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 2),
    _MfrapCfgFrCrcMode_Type()
)
mfrapCfgFrCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrCrcMode.setStatus("mandatory")


class _MfrapCfgFrLmiType_Type(Integer32):
    """Custom type mfrapCfgFrLmiType based on Integer32"""
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


_MfrapCfgFrLmiType_Type.__name__ = "Integer32"
_MfrapCfgFrLmiType_Object = MibScalar
mfrapCfgFrLmiType = _MfrapCfgFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 3),
    _MfrapCfgFrLmiType_Type()
)
mfrapCfgFrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrLmiType.setStatus("mandatory")


class _MfrapCfgFrLmiInactivityTimeout_Type(Integer32):
    """Custom type mfrapCfgFrLmiInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MfrapCfgFrLmiInactivityTimeout_Type.__name__ = "Integer32"
_MfrapCfgFrLmiInactivityTimeout_Object = MibScalar
mfrapCfgFrLmiInactivityTimeout = _MfrapCfgFrLmiInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 4),
    _MfrapCfgFrLmiInactivityTimeout_Type()
)
mfrapCfgFrLmiInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrLmiInactivityTimeout.setStatus("mandatory")


class _MfrapCfgFrLmiKeepaliveTimeout_Type(Integer32):
    """Custom type mfrapCfgFrLmiKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_MfrapCfgFrLmiKeepaliveTimeout_Type.__name__ = "Integer32"
_MfrapCfgFrLmiKeepaliveTimeout_Object = MibScalar
mfrapCfgFrLmiKeepaliveTimeout = _MfrapCfgFrLmiKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 5),
    _MfrapCfgFrLmiKeepaliveTimeout_Type()
)
mfrapCfgFrLmiKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrLmiKeepaliveTimeout.setStatus("mandatory")


class _MfrapCfgFrAddrResMode_Type(Integer32):
    """Custom type mfrapCfgFrAddrResMode based on Integer32"""
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


_MfrapCfgFrAddrResMode_Type.__name__ = "Integer32"
_MfrapCfgFrAddrResMode_Object = MibScalar
mfrapCfgFrAddrResMode = _MfrapCfgFrAddrResMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 6),
    _MfrapCfgFrAddrResMode_Type()
)
mfrapCfgFrAddrResMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrAddrResMode.setStatus("mandatory")


class _MfrapCfgFrAddrResInarpTimer_Type(Integer32):
    """Custom type mfrapCfgFrAddrResInarpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_MfrapCfgFrAddrResInarpTimer_Type.__name__ = "Integer32"
_MfrapCfgFrAddrResInarpTimer_Object = MibScalar
mfrapCfgFrAddrResInarpTimer = _MfrapCfgFrAddrResInarpTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 7),
    _MfrapCfgFrAddrResInarpTimer_Type()
)
mfrapCfgFrAddrResInarpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrAddrResInarpTimer.setStatus("mandatory")


class _MfrapCfgFrLmiFullStatus_Type(Integer32):
    """Custom type mfrapCfgFrLmiFullStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MfrapCfgFrLmiFullStatus_Type.__name__ = "Integer32"
_MfrapCfgFrLmiFullStatus_Object = MibScalar
mfrapCfgFrLmiFullStatus = _MfrapCfgFrLmiFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 8),
    _MfrapCfgFrLmiFullStatus_Type()
)
mfrapCfgFrLmiFullStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrLmiFullStatus.setStatus("mandatory")


class _MfrapCfgFrAddrResDlcis_Type(Integer32):
    """Custom type mfrapCfgFrAddrResDlcis based on Integer32"""
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


_MfrapCfgFrAddrResDlcis_Type.__name__ = "Integer32"
_MfrapCfgFrAddrResDlcis_Object = MibScalar
mfrapCfgFrAddrResDlcis = _MfrapCfgFrAddrResDlcis_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 5, 9),
    _MfrapCfgFrAddrResDlcis_Type()
)
mfrapCfgFrAddrResDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrAddrResDlcis.setStatus("mandatory")
_MfrapCfgVnipTable_ObjectIdentity = ObjectIdentity
mfrapCfgVnipTable = _MfrapCfgVnipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6)
)


class _MfrapCfgVnipMode_Type(Integer32):
    """Custom type mfrapCfgVnipMode based on Integer32"""
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


_MfrapCfgVnipMode_Type.__name__ = "Integer32"
_MfrapCfgVnipMode_Object = MibScalar
mfrapCfgVnipMode = _MfrapCfgVnipMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 1),
    _MfrapCfgVnipMode_Type()
)
mfrapCfgVnipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgVnipMode.setStatus("mandatory")


class _MfrapCfgVnipInitTimer_Type(Integer32):
    """Custom type mfrapCfgVnipInitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_MfrapCfgVnipInitTimer_Type.__name__ = "Integer32"
_MfrapCfgVnipInitTimer_Object = MibScalar
mfrapCfgVnipInitTimer = _MfrapCfgVnipInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 2),
    _MfrapCfgVnipInitTimer_Type()
)
mfrapCfgVnipInitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgVnipInitTimer.setStatus("mandatory")


class _MfrapCfgVnipKeepAliveTimer_Type(Integer32):
    """Custom type mfrapCfgVnipKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_MfrapCfgVnipKeepAliveTimer_Type.__name__ = "Integer32"
_MfrapCfgVnipKeepAliveTimer_Object = MibScalar
mfrapCfgVnipKeepAliveTimer = _MfrapCfgVnipKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 3),
    _MfrapCfgVnipKeepAliveTimer_Type()
)
mfrapCfgVnipKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgVnipKeepAliveTimer.setStatus("mandatory")


class _MfrapCfgVnipInactivityTimer_Type(Integer32):
    """Custom type mfrapCfgVnipInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_MfrapCfgVnipInactivityTimer_Type.__name__ = "Integer32"
_MfrapCfgVnipInactivityTimer_Object = MibScalar
mfrapCfgVnipInactivityTimer = _MfrapCfgVnipInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 4),
    _MfrapCfgVnipInactivityTimer_Type()
)
mfrapCfgVnipInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgVnipInactivityTimer.setStatus("mandatory")


class _MfrapCfgVnipTransitDelayFrequency_Type(Integer32):
    """Custom type mfrapCfgVnipTransitDelayFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_MfrapCfgVnipTransitDelayFrequency_Type.__name__ = "Integer32"
_MfrapCfgVnipTransitDelayFrequency_Object = MibScalar
mfrapCfgVnipTransitDelayFrequency = _MfrapCfgVnipTransitDelayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 5),
    _MfrapCfgVnipTransitDelayFrequency_Type()
)
mfrapCfgVnipTransitDelayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgVnipTransitDelayFrequency.setStatus("mandatory")
_MfrapCfgTransitDelayTable_Object = MibTable
mfrapCfgTransitDelayTable = _MfrapCfgTransitDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20)
)
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayTable.setStatus("mandatory")
_MfrapCfgTransitDelayEntry_Object = MibTableRow
mfrapCfgTransitDelayEntry = _MfrapCfgTransitDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1)
)
mfrapCfgTransitDelayEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgTransitDelayInterface"),
    (0, "MFRAP-MIB", "mfrapCfgTransitDelayDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayEntry.setStatus("mandatory")


class _MfrapCfgTransitDelayInterface_Type(Integer32):
    """Custom type mfrapCfgTransitDelayInterface based on Integer32"""
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


_MfrapCfgTransitDelayInterface_Type.__name__ = "Integer32"
_MfrapCfgTransitDelayInterface_Object = MibTableColumn
mfrapCfgTransitDelayInterface = _MfrapCfgTransitDelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1, 1),
    _MfrapCfgTransitDelayInterface_Type()
)
mfrapCfgTransitDelayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayInterface.setStatus("mandatory")
_MfrapCfgTransitDelayDlciValue_Type = Integer32
_MfrapCfgTransitDelayDlciValue_Object = MibTableColumn
mfrapCfgTransitDelayDlciValue = _MfrapCfgTransitDelayDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1, 2),
    _MfrapCfgTransitDelayDlciValue_Type()
)
mfrapCfgTransitDelayDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayDlciValue.setStatus("mandatory")


class _MfrapCfgTransitDelayNumHops_Type(Integer32):
    """Custom type mfrapCfgTransitDelayNumHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MfrapCfgTransitDelayNumHops_Type.__name__ = "Integer32"
_MfrapCfgTransitDelayNumHops_Object = MibTableColumn
mfrapCfgTransitDelayNumHops = _MfrapCfgTransitDelayNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1, 4),
    _MfrapCfgTransitDelayNumHops_Type()
)
mfrapCfgTransitDelayNumHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayNumHops.setStatus("mandatory")


class _MfrapCfgTransitDelayRcvSummaryCancel_Type(Integer32):
    """Custom type mfrapCfgTransitDelayRcvSummaryCancel based on Integer32"""
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


_MfrapCfgTransitDelayRcvSummaryCancel_Type.__name__ = "Integer32"
_MfrapCfgTransitDelayRcvSummaryCancel_Object = MibTableColumn
mfrapCfgTransitDelayRcvSummaryCancel = _MfrapCfgTransitDelayRcvSummaryCancel_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1, 5),
    _MfrapCfgTransitDelayRcvSummaryCancel_Type()
)
mfrapCfgTransitDelayRcvSummaryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayRcvSummaryCancel.setStatus("mandatory")


class _MfrapCfgTransitDelayThreshold_Type(Integer32):
    """Custom type mfrapCfgTransitDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_MfrapCfgTransitDelayThreshold_Type.__name__ = "Integer32"
_MfrapCfgTransitDelayThreshold_Object = MibTableColumn
mfrapCfgTransitDelayThreshold = _MfrapCfgTransitDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 20, 1, 6),
    _MfrapCfgTransitDelayThreshold_Type()
)
mfrapCfgTransitDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayThreshold.setStatus("mandatory")
_MfrapCfgTDDeleteTable_Object = MibTable
mfrapCfgTDDeleteTable = _MfrapCfgTDDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 21)
)
if mibBuilder.loadTexts:
    mfrapCfgTDDeleteTable.setStatus("mandatory")
_MfrapCfgTDDeleteEntry_Object = MibTableRow
mfrapCfgTDDeleteEntry = _MfrapCfgTDDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 21, 1)
)
mfrapCfgTDDeleteEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgTDDeleteInterface"),
)
if mibBuilder.loadTexts:
    mfrapCfgTDDeleteEntry.setStatus("mandatory")


class _MfrapCfgTDDeleteInterface_Type(Integer32):
    """Custom type mfrapCfgTDDeleteInterface based on Integer32"""
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


_MfrapCfgTDDeleteInterface_Type.__name__ = "Integer32"
_MfrapCfgTDDeleteInterface_Object = MibTableColumn
mfrapCfgTDDeleteInterface = _MfrapCfgTDDeleteInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 21, 1, 1),
    _MfrapCfgTDDeleteInterface_Type()
)
mfrapCfgTDDeleteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mfrapCfgTDDeleteInterface.setStatus("mandatory")
_MfrapCfgTDDeleteDlciValue_Type = Integer32
_MfrapCfgTDDeleteDlciValue_Object = MibTableColumn
mfrapCfgTDDeleteDlciValue = _MfrapCfgTDDeleteDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 21, 1, 2),
    _MfrapCfgTDDeleteDlciValue_Type()
)
mfrapCfgTDDeleteDlciValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgTDDeleteDlciValue.setStatus("mandatory")


class _MfrapCfgTransitDelayTableClear_Type(Integer32):
    """Custom type mfrapCfgTransitDelayTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_MfrapCfgTransitDelayTableClear_Type.__name__ = "Integer32"
_MfrapCfgTransitDelayTableClear_Object = MibScalar
mfrapCfgTransitDelayTableClear = _MfrapCfgTransitDelayTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 6, 22),
    _MfrapCfgTransitDelayTableClear_Type()
)
mfrapCfgTransitDelayTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgTransitDelayTableClear.setStatus("mandatory")
_MfrapCfgFrPerf_ObjectIdentity = ObjectIdentity
mfrapCfgFrPerf = _MfrapCfgFrPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7)
)
_MfrapCfgFrPerfDlciNamesTable_Object = MibTable
mfrapCfgFrPerfDlciNamesTable = _MfrapCfgFrPerfDlciNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesTable.setStatus("mandatory")
_MfrapCfgFrPerfDlciNamesEntry_Object = MibTableRow
mfrapCfgFrPerfDlciNamesEntry = _MfrapCfgFrPerfDlciNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1)
)
mfrapCfgFrPerfDlciNamesEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgFrPerfDlciNamesDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesEntry.setStatus("mandatory")
_MfrapCfgFrPerfDlciNamesDlciValue_Type = Integer32
_MfrapCfgFrPerfDlciNamesDlciValue_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesDlciValue = _MfrapCfgFrPerfDlciNamesDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 1),
    _MfrapCfgFrPerfDlciNamesDlciValue_Type()
)
mfrapCfgFrPerfDlciNamesDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesDlciValue.setStatus("mandatory")


class _MfrapCfgFrPerfDlciNamesDlciName_Type(DisplayString):
    """Custom type mfrapCfgFrPerfDlciNamesDlciName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MfrapCfgFrPerfDlciNamesDlciName_Type.__name__ = "DisplayString"
_MfrapCfgFrPerfDlciNamesDlciName_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesDlciName = _MfrapCfgFrPerfDlciNamesDlciName_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 2),
    _MfrapCfgFrPerfDlciNamesDlciName_Type()
)
mfrapCfgFrPerfDlciNamesDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesDlciName.setStatus("mandatory")
_MfrapCfgFrPerfDlciNamesCirValue_Type = Integer32
_MfrapCfgFrPerfDlciNamesCirValue_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesCirValue = _MfrapCfgFrPerfDlciNamesCirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 3),
    _MfrapCfgFrPerfDlciNamesCirValue_Type()
)
mfrapCfgFrPerfDlciNamesCirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesCirValue.setStatus("mandatory")


class _MfrapCfgFrPerfDlciNamesCirType_Type(Integer32):
    """Custom type mfrapCfgFrPerfDlciNamesCirType based on Integer32"""
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


_MfrapCfgFrPerfDlciNamesCirType_Type.__name__ = "Integer32"
_MfrapCfgFrPerfDlciNamesCirType_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesCirType = _MfrapCfgFrPerfDlciNamesCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 4),
    _MfrapCfgFrPerfDlciNamesCirType_Type()
)
mfrapCfgFrPerfDlciNamesCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesCirType.setStatus("mandatory")


class _MfrapCfgFrPerfDlciNamesUtilThreshold_Type(Integer32):
    """Custom type mfrapCfgFrPerfDlciNamesUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MfrapCfgFrPerfDlciNamesUtilThreshold_Type.__name__ = "Integer32"
_MfrapCfgFrPerfDlciNamesUtilThreshold_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesUtilThreshold = _MfrapCfgFrPerfDlciNamesUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 5),
    _MfrapCfgFrPerfDlciNamesUtilThreshold_Type()
)
mfrapCfgFrPerfDlciNamesUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesUtilThreshold.setStatus("mandatory")
_MfrapCfgFrPerfDlciNamesEirValue_Type = Integer32
_MfrapCfgFrPerfDlciNamesEirValue_Object = MibTableColumn
mfrapCfgFrPerfDlciNamesEirValue = _MfrapCfgFrPerfDlciNamesEirValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 1, 1, 6),
    _MfrapCfgFrPerfDlciNamesEirValue_Type()
)
mfrapCfgFrPerfDlciNamesEirValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesEirValue.setStatus("mandatory")
_MfrapCfgFrPerfDlciNamesDelete_Type = Integer32
_MfrapCfgFrPerfDlciNamesDelete_Object = MibScalar
mfrapCfgFrPerfDlciNamesDelete = _MfrapCfgFrPerfDlciNamesDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 2),
    _MfrapCfgFrPerfDlciNamesDelete_Type()
)
mfrapCfgFrPerfDlciNamesDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesDelete.setStatus("mandatory")
_MfrapCfgFrPerfTimers_ObjectIdentity = ObjectIdentity
mfrapCfgFrPerfTimers = _MfrapCfgFrPerfTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 3)
)


class _MfrapCfgFrPerfTimersSTInterval_Type(Integer32):
    """Custom type mfrapCfgFrPerfTimersSTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_MfrapCfgFrPerfTimersSTInterval_Type.__name__ = "Integer32"
_MfrapCfgFrPerfTimersSTInterval_Object = MibScalar
mfrapCfgFrPerfTimersSTInterval = _MfrapCfgFrPerfTimersSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 3, 1),
    _MfrapCfgFrPerfTimersSTInterval_Type()
)
mfrapCfgFrPerfTimersSTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfTimersSTInterval.setStatus("mandatory")


class _MfrapCfgFrPerfTimersLTInterval_Type(Integer32):
    """Custom type mfrapCfgFrPerfTimersLTInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_MfrapCfgFrPerfTimersLTInterval_Type.__name__ = "Integer32"
_MfrapCfgFrPerfTimersLTInterval_Object = MibScalar
mfrapCfgFrPerfTimersLTInterval = _MfrapCfgFrPerfTimersLTInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 3, 2),
    _MfrapCfgFrPerfTimersLTInterval_Type()
)
mfrapCfgFrPerfTimersLTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfTimersLTInterval.setStatus("mandatory")
_MfrapCfgFrPerfUserProtocolsTable_Object = MibTable
mfrapCfgFrPerfUserProtocolsTable = _MfrapCfgFrPerfUserProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 4)
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUserProtocolsTable.setStatus("mandatory")
_MfrapCfgFrPerfUserProtocolsEntry_Object = MibTableRow
mfrapCfgFrPerfUserProtocolsEntry = _MfrapCfgFrPerfUserProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 4, 1)
)
mfrapCfgFrPerfUserProtocolsEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgFrPerfUserProtocolsIndex"),
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUserProtocolsEntry.setStatus("mandatory")
_MfrapCfgFrPerfUserProtocolsIndex_Type = Integer32
_MfrapCfgFrPerfUserProtocolsIndex_Object = MibTableColumn
mfrapCfgFrPerfUserProtocolsIndex = _MfrapCfgFrPerfUserProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 4, 1, 1),
    _MfrapCfgFrPerfUserProtocolsIndex_Type()
)
mfrapCfgFrPerfUserProtocolsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUserProtocolsIndex.setStatus("mandatory")
_MfrapCfgFrPerfUserProtocolsPortNum_Type = Integer32
_MfrapCfgFrPerfUserProtocolsPortNum_Object = MibTableColumn
mfrapCfgFrPerfUserProtocolsPortNum = _MfrapCfgFrPerfUserProtocolsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 4, 1, 2),
    _MfrapCfgFrPerfUserProtocolsPortNum_Type()
)
mfrapCfgFrPerfUserProtocolsPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUserProtocolsPortNum.setStatus("mandatory")
_MfrapCfgFrPerfLTDlciFilterTable_Object = MibTable
mfrapCfgFrPerfLTDlciFilterTable = _MfrapCfgFrPerfLTDlciFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 5)
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTDlciFilterTable.setStatus("mandatory")
_MfrapCfgFrPerfLTDlciFilterEntry_Object = MibTableRow
mfrapCfgFrPerfLTDlciFilterEntry = _MfrapCfgFrPerfLTDlciFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 5, 1)
)
mfrapCfgFrPerfLTDlciFilterEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgFrPerfLTDlciFilterIndex"),
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTDlciFilterEntry.setStatus("mandatory")
_MfrapCfgFrPerfLTDlciFilterIndex_Type = Integer32
_MfrapCfgFrPerfLTDlciFilterIndex_Object = MibTableColumn
mfrapCfgFrPerfLTDlciFilterIndex = _MfrapCfgFrPerfLTDlciFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 5, 1, 1),
    _MfrapCfgFrPerfLTDlciFilterIndex_Type()
)
mfrapCfgFrPerfLTDlciFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTDlciFilterIndex.setStatus("mandatory")
_MfrapCfgFrPerfLTDlciFilterDlciNum_Type = Integer32
_MfrapCfgFrPerfLTDlciFilterDlciNum_Object = MibTableColumn
mfrapCfgFrPerfLTDlciFilterDlciNum = _MfrapCfgFrPerfLTDlciFilterDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 5, 1, 2),
    _MfrapCfgFrPerfLTDlciFilterDlciNum_Type()
)
mfrapCfgFrPerfLTDlciFilterDlciNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTDlciFilterDlciNum.setStatus("mandatory")
_MfrapCfgFrPerfLTProtocolFilterTable_Object = MibTable
mfrapCfgFrPerfLTProtocolFilterTable = _MfrapCfgFrPerfLTProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 6)
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTProtocolFilterTable.setStatus("mandatory")
_MfrapCfgFrPerfLTProtocolFilterEntry_Object = MibTableRow
mfrapCfgFrPerfLTProtocolFilterEntry = _MfrapCfgFrPerfLTProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 6, 1)
)
mfrapCfgFrPerfLTProtocolFilterEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgFrPerfLTProtocolFilterIndex"),
)
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTProtocolFilterEntry.setStatus("mandatory")
_MfrapCfgFrPerfLTProtocolFilterIndex_Type = Integer32
_MfrapCfgFrPerfLTProtocolFilterIndex_Object = MibTableColumn
mfrapCfgFrPerfLTProtocolFilterIndex = _MfrapCfgFrPerfLTProtocolFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 6, 1, 1),
    _MfrapCfgFrPerfLTProtocolFilterIndex_Type()
)
mfrapCfgFrPerfLTProtocolFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTProtocolFilterIndex.setStatus("mandatory")


class _MfrapCfgFrPerfLTProtocolFilterProtocol_Type(Integer32):
    """Custom type mfrapCfgFrPerfLTProtocolFilterProtocol based on Integer32"""
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


_MfrapCfgFrPerfLTProtocolFilterProtocol_Type.__name__ = "Integer32"
_MfrapCfgFrPerfLTProtocolFilterProtocol_Object = MibTableColumn
mfrapCfgFrPerfLTProtocolFilterProtocol = _MfrapCfgFrPerfLTProtocolFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 6, 1, 2),
    _MfrapCfgFrPerfLTProtocolFilterProtocol_Type()
)
mfrapCfgFrPerfLTProtocolFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTProtocolFilterProtocol.setStatus("mandatory")


class _MfrapCfgFrPerfDlciDefaultUtilThreshold_Type(Integer32):
    """Custom type mfrapCfgFrPerfDlciDefaultUtilThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MfrapCfgFrPerfDlciDefaultUtilThreshold_Type.__name__ = "Integer32"
_MfrapCfgFrPerfDlciDefaultUtilThreshold_Object = MibScalar
mfrapCfgFrPerfDlciDefaultUtilThreshold = _MfrapCfgFrPerfDlciDefaultUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 7),
    _MfrapCfgFrPerfDlciDefaultUtilThreshold_Type()
)
mfrapCfgFrPerfDlciDefaultUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciDefaultUtilThreshold.setStatus("mandatory")


class _MfrapCfgFrPerfDlciUtilDuration_Type(Integer32):
    """Custom type mfrapCfgFrPerfDlciUtilDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfrapCfgFrPerfDlciUtilDuration_Type.__name__ = "Integer32"
_MfrapCfgFrPerfDlciUtilDuration_Object = MibScalar
mfrapCfgFrPerfDlciUtilDuration = _MfrapCfgFrPerfDlciUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 8),
    _MfrapCfgFrPerfDlciUtilDuration_Type()
)
mfrapCfgFrPerfDlciUtilDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciUtilDuration.setStatus("mandatory")


class _MfrapCfgFrPerfDlciNamesTableClear_Type(Integer32):
    """Custom type mfrapCfgFrPerfDlciNamesTableClear based on Integer32"""
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


_MfrapCfgFrPerfDlciNamesTableClear_Type.__name__ = "Integer32"
_MfrapCfgFrPerfDlciNamesTableClear_Object = MibScalar
mfrapCfgFrPerfDlciNamesTableClear = _MfrapCfgFrPerfDlciNamesTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 9),
    _MfrapCfgFrPerfDlciNamesTableClear_Type()
)
mfrapCfgFrPerfDlciNamesTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfDlciNamesTableClear.setStatus("mandatory")


class _MfrapCfgFrPerfUserProtocolsTableClear_Type(Integer32):
    """Custom type mfrapCfgFrPerfUserProtocolsTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_MfrapCfgFrPerfUserProtocolsTableClear_Type.__name__ = "Integer32"
_MfrapCfgFrPerfUserProtocolsTableClear_Object = MibScalar
mfrapCfgFrPerfUserProtocolsTableClear = _MfrapCfgFrPerfUserProtocolsTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 10),
    _MfrapCfgFrPerfUserProtocolsTableClear_Type()
)
mfrapCfgFrPerfUserProtocolsTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUserProtocolsTableClear.setStatus("mandatory")


class _MfrapCfgFrPerfLTDlciFilterTableClear_Type(Integer32):
    """Custom type mfrapCfgFrPerfLTDlciFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_MfrapCfgFrPerfLTDlciFilterTableClear_Type.__name__ = "Integer32"
_MfrapCfgFrPerfLTDlciFilterTableClear_Object = MibScalar
mfrapCfgFrPerfLTDlciFilterTableClear = _MfrapCfgFrPerfLTDlciFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 11),
    _MfrapCfgFrPerfLTDlciFilterTableClear_Type()
)
mfrapCfgFrPerfLTDlciFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTDlciFilterTableClear.setStatus("mandatory")


class _MfrapCfgFrPerfLTProtocolFilterTableClear_Type(Integer32):
    """Custom type mfrapCfgFrPerfLTProtocolFilterTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-table", 1)
    )


_MfrapCfgFrPerfLTProtocolFilterTableClear_Type.__name__ = "Integer32"
_MfrapCfgFrPerfLTProtocolFilterTableClear_Object = MibScalar
mfrapCfgFrPerfLTProtocolFilterTableClear = _MfrapCfgFrPerfLTProtocolFilterTableClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 12),
    _MfrapCfgFrPerfLTProtocolFilterTableClear_Type()
)
mfrapCfgFrPerfLTProtocolFilterTableClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfLTProtocolFilterTableClear.setStatus("mandatory")


class _MfrapCfgFrPerfUnprovDlcisDelete_Type(Integer32):
    """Custom type mfrapCfgFrPerfUnprovDlcisDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete-unprov", 1)
    )


_MfrapCfgFrPerfUnprovDlcisDelete_Type.__name__ = "Integer32"
_MfrapCfgFrPerfUnprovDlcisDelete_Object = MibScalar
mfrapCfgFrPerfUnprovDlcisDelete = _MfrapCfgFrPerfUnprovDlcisDelete_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 7, 13),
    _MfrapCfgFrPerfUnprovDlcisDelete_Type()
)
mfrapCfgFrPerfUnprovDlcisDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgFrPerfUnprovDlcisDelete.setStatus("mandatory")
_MfrapCfgSecurityTable_ObjectIdentity = ObjectIdentity
mfrapCfgSecurityTable = _MfrapCfgSecurityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8)
)


class _MfrapCfgTelnetCliLcdPassword_Type(DisplayString):
    """Custom type mfrapCfgTelnetCliLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgTelnetCliLcdPassword_Type.__name__ = "DisplayString"
_MfrapCfgTelnetCliLcdPassword_Object = MibScalar
mfrapCfgTelnetCliLcdPassword = _MfrapCfgTelnetCliLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 1),
    _MfrapCfgTelnetCliLcdPassword_Type()
)
mfrapCfgTelnetCliLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTelnetCliLcdPassword.setStatus("mandatory")


class _MfrapCfgTftpPassword_Type(DisplayString):
    """Custom type mfrapCfgTftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgTftpPassword_Type.__name__ = "DisplayString"
_MfrapCfgTftpPassword_Object = MibScalar
mfrapCfgTftpPassword = _MfrapCfgTftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 2),
    _MfrapCfgTftpPassword_Type()
)
mfrapCfgTftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgTftpPassword.setStatus("mandatory")


class _MfrapCfgCliPassword_Type(DisplayString):
    """Custom type mfrapCfgCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgCliPassword_Type.__name__ = "DisplayString"
_MfrapCfgCliPassword_Object = MibScalar
mfrapCfgCliPassword = _MfrapCfgCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 3),
    _MfrapCfgCliPassword_Type()
)
mfrapCfgCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgCliPassword.setStatus("mandatory")


class _MfrapCfgLcdPassword_Type(DisplayString):
    """Custom type mfrapCfgLcdPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgLcdPassword_Type.__name__ = "DisplayString"
_MfrapCfgLcdPassword_Object = MibScalar
mfrapCfgLcdPassword = _MfrapCfgLcdPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 4),
    _MfrapCfgLcdPassword_Type()
)
mfrapCfgLcdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgLcdPassword.setStatus("mandatory")


class _MfrapCfgGetCommunityString_Type(DisplayString):
    """Custom type mfrapCfgGetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MfrapCfgGetCommunityString_Type.__name__ = "DisplayString"
_MfrapCfgGetCommunityString_Object = MibScalar
mfrapCfgGetCommunityString = _MfrapCfgGetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 5),
    _MfrapCfgGetCommunityString_Type()
)
mfrapCfgGetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgGetCommunityString.setStatus("mandatory")


class _MfrapCfgSetCommunityString_Type(DisplayString):
    """Custom type mfrapCfgSetCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MfrapCfgSetCommunityString_Type.__name__ = "DisplayString"
_MfrapCfgSetCommunityString_Object = MibScalar
mfrapCfgSetCommunityString = _MfrapCfgSetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 6),
    _MfrapCfgSetCommunityString_Type()
)
mfrapCfgSetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgSetCommunityString.setStatus("mandatory")


class _MfrapCfgLcdPswdEnable_Type(Integer32):
    """Custom type mfrapCfgLcdPswdEnable based on Integer32"""
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


_MfrapCfgLcdPswdEnable_Type.__name__ = "Integer32"
_MfrapCfgLcdPswdEnable_Object = MibScalar
mfrapCfgLcdPswdEnable = _MfrapCfgLcdPswdEnable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 7),
    _MfrapCfgLcdPswdEnable_Type()
)
mfrapCfgLcdPswdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgLcdPswdEnable.setStatus("mandatory")
_MfrapCfgLcdPswdTimeout_Type = Integer32
_MfrapCfgLcdPswdTimeout_Object = MibScalar
mfrapCfgLcdPswdTimeout = _MfrapCfgLcdPswdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 8, 8),
    _MfrapCfgLcdPswdTimeout_Type()
)
mfrapCfgLcdPswdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgLcdPswdTimeout.setStatus("mandatory")
_MfrapCfgConnectionTable_ObjectIdentity = ObjectIdentity
mfrapCfgConnectionTable = _MfrapCfgConnectionTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10)
)
_MfrapCfgCurrentConnTable_Object = MibTable
mfrapCfgCurrentConnTable = _MfrapCfgCurrentConnTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1)
)
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnTable.setStatus("mandatory")
_MfrapCfgCurrentConnEntry_Object = MibTableRow
mfrapCfgCurrentConnEntry = _MfrapCfgCurrentConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1)
)
mfrapCfgCurrentConnEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgCurrentConnDestPort"),
    (0, "MFRAP-MIB", "mfrapCfgCurrentConnDestDs0"),
)
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnEntry.setStatus("mandatory")


class _MfrapCfgCurrentConnDestPort_Type(Integer32):
    """Custom type mfrapCfgCurrentConnDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port1-t1", 1)
    )


_MfrapCfgCurrentConnDestPort_Type.__name__ = "Integer32"
_MfrapCfgCurrentConnDestPort_Object = MibTableColumn
mfrapCfgCurrentConnDestPort = _MfrapCfgCurrentConnDestPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1, 1),
    _MfrapCfgCurrentConnDestPort_Type()
)
mfrapCfgCurrentConnDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnDestPort.setStatus("mandatory")


class _MfrapCfgCurrentConnDestDs0_Type(Integer32):
    """Custom type mfrapCfgCurrentConnDestDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MfrapCfgCurrentConnDestDs0_Type.__name__ = "Integer32"
_MfrapCfgCurrentConnDestDs0_Object = MibTableColumn
mfrapCfgCurrentConnDestDs0 = _MfrapCfgCurrentConnDestDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1, 2),
    _MfrapCfgCurrentConnDestDs0_Type()
)
mfrapCfgCurrentConnDestDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnDestDs0.setStatus("mandatory")


class _MfrapCfgCurrentConnSrcPort_Type(Integer32):
    """Custom type mfrapCfgCurrentConnSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port2-dandi", 2),
          ("port3-dte", 3))
    )


_MfrapCfgCurrentConnSrcPort_Type.__name__ = "Integer32"
_MfrapCfgCurrentConnSrcPort_Object = MibTableColumn
mfrapCfgCurrentConnSrcPort = _MfrapCfgCurrentConnSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1, 3),
    _MfrapCfgCurrentConnSrcPort_Type()
)
mfrapCfgCurrentConnSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnSrcPort.setStatus("mandatory")


class _MfrapCfgCurrentConnSrcDs0_Type(Integer32):
    """Custom type mfrapCfgCurrentConnSrcDs0 based on Integer32"""
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
              40)
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
          ("no-connection", 40))
    )


_MfrapCfgCurrentConnSrcDs0_Type.__name__ = "Integer32"
_MfrapCfgCurrentConnSrcDs0_Object = MibTableColumn
mfrapCfgCurrentConnSrcDs0 = _MfrapCfgCurrentConnSrcDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1, 4),
    _MfrapCfgCurrentConnSrcDs0_Type()
)
mfrapCfgCurrentConnSrcDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnSrcDs0.setStatus("mandatory")


class _MfrapCfgCurrentConnType_Type(Integer32):
    """Custom type mfrapCfgCurrentConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              33)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 3),
          ("not-connected", 33),
          ("transparent", 2),
          ("voice", 1))
    )


_MfrapCfgCurrentConnType_Type.__name__ = "Integer32"
_MfrapCfgCurrentConnType_Object = MibTableColumn
mfrapCfgCurrentConnType = _MfrapCfgCurrentConnType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 1, 1, 5),
    _MfrapCfgCurrentConnType_Type()
)
mfrapCfgCurrentConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgCurrentConnType.setStatus("mandatory")
_MfrapCfgEditConnections_ObjectIdentity = ObjectIdentity
mfrapCfgEditConnections = _MfrapCfgEditConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2)
)


class _MfrapCfgEditConnCopyCurrtoEdit_Type(Integer32):
    """Custom type mfrapCfgEditConnCopyCurrtoEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("copy-current", 1)
    )


_MfrapCfgEditConnCopyCurrtoEdit_Type.__name__ = "Integer32"
_MfrapCfgEditConnCopyCurrtoEdit_Object = MibScalar
mfrapCfgEditConnCopyCurrtoEdit = _MfrapCfgEditConnCopyCurrtoEdit_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 1),
    _MfrapCfgEditConnCopyCurrtoEdit_Type()
)
mfrapCfgEditConnCopyCurrtoEdit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgEditConnCopyCurrtoEdit.setStatus("mandatory")


class _MfrapCfgEditClearEdit_Type(Integer32):
    """Custom type mfrapCfgEditClearEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-edit", 1)
    )


_MfrapCfgEditClearEdit_Type.__name__ = "Integer32"
_MfrapCfgEditClearEdit_Object = MibScalar
mfrapCfgEditClearEdit = _MfrapCfgEditClearEdit_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 2),
    _MfrapCfgEditClearEdit_Type()
)
mfrapCfgEditClearEdit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgEditClearEdit.setStatus("mandatory")
_MfrapCfgEditConnTable_Object = MibTable
mfrapCfgEditConnTable = _MfrapCfgEditConnTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3)
)
if mibBuilder.loadTexts:
    mfrapCfgEditConnTable.setStatus("mandatory")
_MfrapCfgEditConnEntry_Object = MibTableRow
mfrapCfgEditConnEntry = _MfrapCfgEditConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1)
)
mfrapCfgEditConnEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapCfgEditConnDestPort"),
    (0, "MFRAP-MIB", "mfrapCfgEditConnDestDs0"),
)
if mibBuilder.loadTexts:
    mfrapCfgEditConnEntry.setStatus("mandatory")


class _MfrapCfgEditConnDestPort_Type(Integer32):
    """Custom type mfrapCfgEditConnDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port1-t1", 1)
    )


_MfrapCfgEditConnDestPort_Type.__name__ = "Integer32"
_MfrapCfgEditConnDestPort_Object = MibTableColumn
mfrapCfgEditConnDestPort = _MfrapCfgEditConnDestPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 1),
    _MfrapCfgEditConnDestPort_Type()
)
mfrapCfgEditConnDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgEditConnDestPort.setStatus("mandatory")


class _MfrapCfgEditConnDestDs0_Type(Integer32):
    """Custom type mfrapCfgEditConnDestDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MfrapCfgEditConnDestDs0_Type.__name__ = "Integer32"
_MfrapCfgEditConnDestDs0_Object = MibTableColumn
mfrapCfgEditConnDestDs0 = _MfrapCfgEditConnDestDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 2),
    _MfrapCfgEditConnDestDs0_Type()
)
mfrapCfgEditConnDestDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgEditConnDestDs0.setStatus("mandatory")


class _MfrapCfgEditConnSrcPort_Type(Integer32):
    """Custom type mfrapCfgEditConnSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port2-dandi", 2),
          ("port3-dte", 3))
    )


_MfrapCfgEditConnSrcPort_Type.__name__ = "Integer32"
_MfrapCfgEditConnSrcPort_Object = MibTableColumn
mfrapCfgEditConnSrcPort = _MfrapCfgEditConnSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 3),
    _MfrapCfgEditConnSrcPort_Type()
)
mfrapCfgEditConnSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgEditConnSrcPort.setStatus("mandatory")


class _MfrapCfgEditConnSrcDs0_Type(Integer32):
    """Custom type mfrapCfgEditConnSrcDs0 based on Integer32"""
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
              40)
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
          ("no-connection", 40))
    )


_MfrapCfgEditConnSrcDs0_Type.__name__ = "Integer32"
_MfrapCfgEditConnSrcDs0_Object = MibTableColumn
mfrapCfgEditConnSrcDs0 = _MfrapCfgEditConnSrcDs0_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 4),
    _MfrapCfgEditConnSrcDs0_Type()
)
mfrapCfgEditConnSrcDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgEditConnSrcDs0.setStatus("mandatory")


class _MfrapCfgEditConnType_Type(Integer32):
    """Custom type mfrapCfgEditConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              33)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 3),
          ("not-connected", 33),
          ("transparent", 2),
          ("voice", 1))
    )


_MfrapCfgEditConnType_Type.__name__ = "Integer32"
_MfrapCfgEditConnType_Object = MibTableColumn
mfrapCfgEditConnType = _MfrapCfgEditConnType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 5),
    _MfrapCfgEditConnType_Type()
)
mfrapCfgEditConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgEditConnType.setStatus("mandatory")


class _MfrapCfgEditDisconnect_Type(Integer32):
    """Custom type mfrapCfgEditDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnect", 1)
    )


_MfrapCfgEditDisconnect_Type.__name__ = "Integer32"
_MfrapCfgEditDisconnect_Object = MibTableColumn
mfrapCfgEditDisconnect = _MfrapCfgEditDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 3, 1, 6),
    _MfrapCfgEditDisconnect_Type()
)
mfrapCfgEditDisconnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgEditDisconnect.setStatus("mandatory")


class _MfrapCfgEditLastSetStatus_Type(Integer32):
    """Custom type mfrapCfgEditLastSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-conflict", 3),
          ("ds0s-not-ascending", 4),
          ("illegal-value", 8),
          ("invalid-dte-bandwidth", 2),
          ("set-valid", 1))
    )


_MfrapCfgEditLastSetStatus_Type.__name__ = "Integer32"
_MfrapCfgEditLastSetStatus_Object = MibScalar
mfrapCfgEditLastSetStatus = _MfrapCfgEditLastSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 4),
    _MfrapCfgEditLastSetStatus_Type()
)
mfrapCfgEditLastSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgEditLastSetStatus.setStatus("mandatory")


class _MfrapCfgEditConnStatus_Type(Integer32):
    """Custom type mfrapCfgEditConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bad-connection-type", 7),
          ("connections-valid", 1),
          ("ds0s-not-ascending", 4),
          ("incomplete-entry", 5),
          ("inconsistent-edit-buff", 6),
          ("invalid-dte-bandwidth", 2),
          ("no-current-connections", 99))
    )


_MfrapCfgEditConnStatus_Type.__name__ = "Integer32"
_MfrapCfgEditConnStatus_Object = MibScalar
mfrapCfgEditConnStatus = _MfrapCfgEditConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 5),
    _MfrapCfgEditConnStatus_Type()
)
mfrapCfgEditConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgEditConnStatus.setStatus("mandatory")


class _MfrapCfgConnUpdateCmd_Type(Integer32):
    """Custom type mfrapCfgConnUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("config-and-connect", 1)
    )


_MfrapCfgConnUpdateCmd_Type.__name__ = "Integer32"
_MfrapCfgConnUpdateCmd_Object = MibScalar
mfrapCfgConnUpdateCmd = _MfrapCfgConnUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 10, 2, 6),
    _MfrapCfgConnUpdateCmd_Type()
)
mfrapCfgConnUpdateCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgConnUpdateCmd.setStatus("mandatory")
_MfrapCfgDandiTable_ObjectIdentity = ObjectIdentity
mfrapCfgDandiTable = _MfrapCfgDandiTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 11)
)


class _MfrapCfgDandiFraming_Type(Integer32):
    """Custom type mfrapCfgDandiFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_MfrapCfgDandiFraming_Type.__name__ = "Integer32"
_MfrapCfgDandiFraming_Object = MibScalar
mfrapCfgDandiFraming = _MfrapCfgDandiFraming_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 11, 1),
    _MfrapCfgDandiFraming_Type()
)
mfrapCfgDandiFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDandiFraming.setStatus("mandatory")


class _MfrapCfgDandiLineEncoding_Type(Integer32):
    """Custom type mfrapCfgDandiLineEncoding based on Integer32"""
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


_MfrapCfgDandiLineEncoding_Type.__name__ = "Integer32"
_MfrapCfgDandiLineEncoding_Object = MibScalar
mfrapCfgDandiLineEncoding = _MfrapCfgDandiLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 11, 2),
    _MfrapCfgDandiLineEncoding_Type()
)
mfrapCfgDandiLineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgDandiLineEncoding.setStatus("mandatory")


class _MfrapCfgLock_Type(Integer32):
    """Custom type mfrapCfgLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_MfrapCfgLock_Type.__name__ = "Integer32"
_MfrapCfgLock_Object = MibScalar
mfrapCfgLock = _MfrapCfgLock_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 12),
    _MfrapCfgLock_Type()
)
mfrapCfgLock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgLock.setStatus("mandatory")
_MfrapCfgLockID_Type = IpAddress
_MfrapCfgLockID_Object = MibScalar
mfrapCfgLockID = _MfrapCfgLockID_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 13),
    _MfrapCfgLockID_Type()
)
mfrapCfgLockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgLockID.setStatus("mandatory")


class _MfrapCfgID_Type(DisplayString):
    """Custom type mfrapCfgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MfrapCfgID_Type.__name__ = "DisplayString"
_MfrapCfgID_Object = MibScalar
mfrapCfgID = _MfrapCfgID_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 14),
    _MfrapCfgID_Type()
)
mfrapCfgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapCfgID.setStatus("mandatory")


class _MfrapCfgStatus_Type(Integer32):
    """Custom type mfrapCfgStatus based on Integer32"""
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


_MfrapCfgStatus_Type.__name__ = "Integer32"
_MfrapCfgStatus_Object = MibScalar
mfrapCfgStatus = _MfrapCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 15),
    _MfrapCfgStatus_Type()
)
mfrapCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgStatus.setStatus("mandatory")


class _MfrapCfgUnlock_Type(Integer32):
    """Custom type mfrapCfgUnlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("un-lock", 1)
    )


_MfrapCfgUnlock_Type.__name__ = "Integer32"
_MfrapCfgUnlock_Object = MibScalar
mfrapCfgUnlock = _MfrapCfgUnlock_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 16),
    _MfrapCfgUnlock_Type()
)
mfrapCfgUnlock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgUnlock.setStatus("mandatory")


class _MfrapCfgUpdate_Type(Integer32):
    """Custom type mfrapCfgUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_MfrapCfgUpdate_Type.__name__ = "Integer32"
_MfrapCfgUpdate_Object = MibScalar
mfrapCfgUpdate = _MfrapCfgUpdate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 2, 17),
    _MfrapCfgUpdate_Type()
)
mfrapCfgUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapCfgUpdate.setStatus("mandatory")
_MfrapDiagnostics_ObjectIdentity = ObjectIdentity
mfrapDiagnostics = _MfrapDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3)
)
_MfrapDiagUnitTable_ObjectIdentity = ObjectIdentity
mfrapDiagUnitTable = _MfrapDiagUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 1)
)


class _MfrapDiagUnitLocLoop_Type(Integer32):
    """Custom type mfrapDiagUnitLocLoop based on Integer32"""
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


_MfrapDiagUnitLocLoop_Type.__name__ = "Integer32"
_MfrapDiagUnitLocLoop_Object = MibScalar
mfrapDiagUnitLocLoop = _MfrapDiagUnitLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 1, 1),
    _MfrapDiagUnitLocLoop_Type()
)
mfrapDiagUnitLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagUnitLocLoop.setStatus("mandatory")


class _MfrapDiagUnitReset_Type(Integer32):
    """Custom type mfrapDiagUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-unit", 1)
    )


_MfrapDiagUnitReset_Type.__name__ = "Integer32"
_MfrapDiagUnitReset_Object = MibScalar
mfrapDiagUnitReset = _MfrapDiagUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 1, 2),
    _MfrapDiagUnitReset_Type()
)
mfrapDiagUnitReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagUnitReset.setStatus("mandatory")
_MfrapDiagUnitTimeRemaining_Type = TimeTicks
_MfrapDiagUnitTimeRemaining_Object = MibScalar
mfrapDiagUnitTimeRemaining = _MfrapDiagUnitTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 1, 3),
    _MfrapDiagUnitTimeRemaining_Type()
)
mfrapDiagUnitTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagUnitTimeRemaining.setStatus("mandatory")
_MfrapDiagT1Table_ObjectIdentity = ObjectIdentity
mfrapDiagT1Table = _MfrapDiagT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2)
)


class _MfrapDiagT1LocLineLpbk_Type(Integer32):
    """Custom type mfrapDiagT1LocLineLpbk based on Integer32"""
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


_MfrapDiagT1LocLineLpbk_Type.__name__ = "Integer32"
_MfrapDiagT1LocLineLpbk_Object = MibScalar
mfrapDiagT1LocLineLpbk = _MfrapDiagT1LocLineLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 1),
    _MfrapDiagT1LocLineLpbk_Type()
)
mfrapDiagT1LocLineLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagT1LocLineLpbk.setStatus("mandatory")


class _MfrapDiagT1LocPylLpbk_Type(Integer32):
    """Custom type mfrapDiagT1LocPylLpbk based on Integer32"""
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


_MfrapDiagT1LocPylLpbk_Type.__name__ = "Integer32"
_MfrapDiagT1LocPylLpbk_Object = MibScalar
mfrapDiagT1LocPylLpbk = _MfrapDiagT1LocPylLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 2),
    _MfrapDiagT1LocPylLpbk_Type()
)
mfrapDiagT1LocPylLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagT1LocPylLpbk.setStatus("mandatory")


class _MfrapDiagT1LocAggrLpbk_Type(Integer32):
    """Custom type mfrapDiagT1LocAggrLpbk based on Integer32"""
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


_MfrapDiagT1LocAggrLpbk_Type.__name__ = "Integer32"
_MfrapDiagT1LocAggrLpbk_Object = MibScalar
mfrapDiagT1LocAggrLpbk = _MfrapDiagT1LocAggrLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 3),
    _MfrapDiagT1LocAggrLpbk_Type()
)
mfrapDiagT1LocAggrLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagT1LocAggrLpbk.setStatus("mandatory")


class _MfrapDiagT1RmtLpbkStatus_Type(Integer32):
    """Custom type mfrapDiagT1RmtLpbkStatus based on Integer32"""
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


_MfrapDiagT1RmtLpbkStatus_Type.__name__ = "Integer32"
_MfrapDiagT1RmtLpbkStatus_Object = MibScalar
mfrapDiagT1RmtLpbkStatus = _MfrapDiagT1RmtLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 4),
    _MfrapDiagT1RmtLpbkStatus_Type()
)
mfrapDiagT1RmtLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagT1RmtLpbkStatus.setStatus("mandatory")


class _MfrapDiagT1RmtLpbkCmd_Type(Integer32):
    """Custom type mfrapDiagT1RmtLpbkCmd based on Integer32"""
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


_MfrapDiagT1RmtLpbkCmd_Type.__name__ = "Integer32"
_MfrapDiagT1RmtLpbkCmd_Object = MibScalar
mfrapDiagT1RmtLpbkCmd = _MfrapDiagT1RmtLpbkCmd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 5),
    _MfrapDiagT1RmtLpbkCmd_Type()
)
mfrapDiagT1RmtLpbkCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagT1RmtLpbkCmd.setStatus("mandatory")
_MfrapDiagT1TimeRemaining_Type = TimeTicks
_MfrapDiagT1TimeRemaining_Object = MibScalar
mfrapDiagT1TimeRemaining = _MfrapDiagT1TimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 2, 6),
    _MfrapDiagT1TimeRemaining_Type()
)
mfrapDiagT1TimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagT1TimeRemaining.setStatus("mandatory")
_MfrapDiagDteTable_ObjectIdentity = ObjectIdentity
mfrapDiagDteTable = _MfrapDiagDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3)
)


class _MfrapDiagDteSigRTS_Type(Integer32):
    """Custom type mfrapDiagDteSigRTS based on Integer32"""
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


_MfrapDiagDteSigRTS_Type.__name__ = "Integer32"
_MfrapDiagDteSigRTS_Object = MibScalar
mfrapDiagDteSigRTS = _MfrapDiagDteSigRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 1),
    _MfrapDiagDteSigRTS_Type()
)
mfrapDiagDteSigRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagDteSigRTS.setStatus("mandatory")


class _MfrapDiagDteSigDTR_Type(Integer32):
    """Custom type mfrapDiagDteSigDTR based on Integer32"""
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


_MfrapDiagDteSigDTR_Type.__name__ = "Integer32"
_MfrapDiagDteSigDTR_Object = MibScalar
mfrapDiagDteSigDTR = _MfrapDiagDteSigDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 2),
    _MfrapDiagDteSigDTR_Type()
)
mfrapDiagDteSigDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagDteSigDTR.setStatus("mandatory")


class _MfrapDiagDteLclLpbk_Type(Integer32):
    """Custom type mfrapDiagDteLclLpbk based on Integer32"""
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


_MfrapDiagDteLclLpbk_Type.__name__ = "Integer32"
_MfrapDiagDteLclLpbk_Object = MibScalar
mfrapDiagDteLclLpbk = _MfrapDiagDteLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 3),
    _MfrapDiagDteLclLpbk_Type()
)
mfrapDiagDteLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagDteLclLpbk.setStatus("mandatory")


class _MfrapDiagDteV54Lpbk_Type(Integer32):
    """Custom type mfrapDiagDteV54Lpbk based on Integer32"""
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


_MfrapDiagDteV54Lpbk_Type.__name__ = "Integer32"
_MfrapDiagDteV54Lpbk_Object = MibScalar
mfrapDiagDteV54Lpbk = _MfrapDiagDteV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 4),
    _MfrapDiagDteV54Lpbk_Type()
)
mfrapDiagDteV54Lpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagDteV54Lpbk.setStatus("mandatory")


class _MfrapDiagDteRmtV54Lpbk_Type(Integer32):
    """Custom type mfrapDiagDteRmtV54Lpbk based on Integer32"""
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


_MfrapDiagDteRmtV54Lpbk_Type.__name__ = "Integer32"
_MfrapDiagDteRmtV54Lpbk_Object = MibScalar
mfrapDiagDteRmtV54Lpbk = _MfrapDiagDteRmtV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 5),
    _MfrapDiagDteRmtV54Lpbk_Type()
)
mfrapDiagDteRmtV54Lpbk.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagDteRmtV54Lpbk.setStatus("mandatory")
_MfrapDiagDteTimeRemaining_Type = TimeTicks
_MfrapDiagDteTimeRemaining_Object = MibScalar
mfrapDiagDteTimeRemaining = _MfrapDiagDteTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 3, 13),
    _MfrapDiagDteTimeRemaining_Type()
)
mfrapDiagDteTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagDteTimeRemaining.setStatus("mandatory")
_MfrapDiagBertTable_ObjectIdentity = ObjectIdentity
mfrapDiagBertTable = _MfrapDiagBertTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5)
)


class _MfrapDiagBertState_Type(Integer32):
    """Custom type mfrapDiagBertState based on Integer32"""
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
        *(("clear-error-bert-test", 5),
          ("inject-error-bert-test", 4),
          ("start-bert-test-dandi", 6),
          ("start-bert-test-dte", 2),
          ("start-bert-test-fractional-t1", 7),
          ("start-bert-test-t1", 1),
          ("stop-bert-test", 3))
    )


_MfrapDiagBertState_Type.__name__ = "Integer32"
_MfrapDiagBertState_Object = MibScalar
mfrapDiagBertState = _MfrapDiagBertState_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 1),
    _MfrapDiagBertState_Type()
)
mfrapDiagBertState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagBertState.setStatus("mandatory")


class _MfrapDiagBertStatus_Type(Integer32):
    """Custom type mfrapDiagBertStatus based on Integer32"""
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


_MfrapDiagBertStatus_Type.__name__ = "Integer32"
_MfrapDiagBertStatus_Object = MibScalar
mfrapDiagBertStatus = _MfrapDiagBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 2),
    _MfrapDiagBertStatus_Type()
)
mfrapDiagBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagBertStatus.setStatus("mandatory")
_MfrapDiagBertErrors_Type = Counter32
_MfrapDiagBertErrors_Object = MibScalar
mfrapDiagBertErrors = _MfrapDiagBertErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 3),
    _MfrapDiagBertErrors_Type()
)
mfrapDiagBertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagBertErrors.setStatus("mandatory")
_MfrapDiagBertErrSec_Type = Counter32
_MfrapDiagBertErrSec_Object = MibScalar
mfrapDiagBertErrSec = _MfrapDiagBertErrSec_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 4),
    _MfrapDiagBertErrSec_Type()
)
mfrapDiagBertErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagBertErrSec.setStatus("mandatory")
_MfrapDiagBertTimeElaps_Type = TimeTicks
_MfrapDiagBertTimeElaps_Object = MibScalar
mfrapDiagBertTimeElaps = _MfrapDiagBertTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 5),
    _MfrapDiagBertTimeElaps_Type()
)
mfrapDiagBertTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagBertTimeElaps.setStatus("mandatory")
_MfrapDiagBertResyncs_Type = Counter32
_MfrapDiagBertResyncs_Object = MibScalar
mfrapDiagBertResyncs = _MfrapDiagBertResyncs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 6),
    _MfrapDiagBertResyncs_Type()
)
mfrapDiagBertResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagBertResyncs.setStatus("mandatory")


class _MfrapDiagBertPattern_Type(Integer32):
    """Custom type mfrapDiagBertPattern based on Integer32"""
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


_MfrapDiagBertPattern_Type.__name__ = "Integer32"
_MfrapDiagBertPattern_Object = MibScalar
mfrapDiagBertPattern = _MfrapDiagBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 5, 7),
    _MfrapDiagBertPattern_Type()
)
mfrapDiagBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagBertPattern.setStatus("mandatory")
_MfrapDiagVnipTable_Object = MibTable
mfrapDiagVnipTable = _MfrapDiagVnipTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6)
)
if mibBuilder.loadTexts:
    mfrapDiagVnipTable.setStatus("mandatory")
_MfrapDiagVnipEntry_Object = MibTableRow
mfrapDiagVnipEntry = _MfrapDiagVnipEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1)
)
mfrapDiagVnipEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapDiagVnipInterface"),
    (0, "MFRAP-MIB", "mfrapDiagVnipIndex"),
)
if mibBuilder.loadTexts:
    mfrapDiagVnipEntry.setStatus("mandatory")


class _MfrapDiagVnipInterface_Type(Integer32):
    """Custom type mfrapDiagVnipInterface based on Integer32"""
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


_MfrapDiagVnipInterface_Type.__name__ = "Integer32"
_MfrapDiagVnipInterface_Object = MibTableColumn
mfrapDiagVnipInterface = _MfrapDiagVnipInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 1),
    _MfrapDiagVnipInterface_Type()
)
mfrapDiagVnipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVnipInterface.setStatus("mandatory")
_MfrapDiagVnipIndex_Type = Integer32
_MfrapDiagVnipIndex_Object = MibTableColumn
mfrapDiagVnipIndex = _MfrapDiagVnipIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 2),
    _MfrapDiagVnipIndex_Type()
)
mfrapDiagVnipIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVnipIndex.setStatus("mandatory")
_MfrapDiagVnipDlci_Type = Integer32
_MfrapDiagVnipDlci_Object = MibTableColumn
mfrapDiagVnipDlci = _MfrapDiagVnipDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 3),
    _MfrapDiagVnipDlci_Type()
)
mfrapDiagVnipDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagVnipDlci.setStatus("mandatory")
_MfrapDiagVnipIpAddr_Type = IpAddress
_MfrapDiagVnipIpAddr_Object = MibTableColumn
mfrapDiagVnipIpAddr = _MfrapDiagVnipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 4),
    _MfrapDiagVnipIpAddr_Type()
)
mfrapDiagVnipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagVnipIpAddr.setStatus("mandatory")


class _MfrapDiagVLOOP_Type(Integer32):
    """Custom type mfrapDiagVLOOP based on Integer32"""
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


_MfrapDiagVLOOP_Type.__name__ = "Integer32"
_MfrapDiagVLOOP_Object = MibTableColumn
mfrapDiagVLOOP = _MfrapDiagVLOOP_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 5),
    _MfrapDiagVLOOP_Type()
)
mfrapDiagVLOOP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagVLOOP.setStatus("mandatory")


class _MfrapDiagVBERT_Type(Integer32):
    """Custom type mfrapDiagVBERT based on Integer32"""
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


_MfrapDiagVBERT_Type.__name__ = "Integer32"
_MfrapDiagVBERT_Object = MibTableColumn
mfrapDiagVBERT = _MfrapDiagVBERT_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 6),
    _MfrapDiagVBERT_Type()
)
mfrapDiagVBERT.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDiagVBERT.setStatus("mandatory")


class _MfrapDiagVBERTRate_Type(Integer32):
    """Custom type mfrapDiagVBERTRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2048000),
    )


_MfrapDiagVBERTRate_Type.__name__ = "Integer32"
_MfrapDiagVBERTRate_Object = MibTableColumn
mfrapDiagVBERTRate = _MfrapDiagVBERTRate_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 7),
    _MfrapDiagVBERTRate_Type()
)
mfrapDiagVBERTRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVBERTRate.setStatus("mandatory")


class _MfrapDiagVBERTSize_Type(Integer32):
    """Custom type mfrapDiagVBERTSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2048),
    )


_MfrapDiagVBERTSize_Type.__name__ = "Integer32"
_MfrapDiagVBERTSize_Object = MibTableColumn
mfrapDiagVBERTSize = _MfrapDiagVBERTSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 8),
    _MfrapDiagVBERTSize_Type()
)
mfrapDiagVBERTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVBERTSize.setStatus("mandatory")


class _MfrapDiagVBERTPktPercent_Type(Integer32):
    """Custom type mfrapDiagVBERTPktPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fifty-percent", 2),
          ("oneHundred-percent", 4),
          ("seventyFive-percent", 3),
          ("twentyFive-percent", 1),
          ("zero-percent", 0))
    )


_MfrapDiagVBERTPktPercent_Type.__name__ = "Integer32"
_MfrapDiagVBERTPktPercent_Object = MibTableColumn
mfrapDiagVBERTPktPercent = _MfrapDiagVBERTPktPercent_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 9),
    _MfrapDiagVBERTPktPercent_Type()
)
mfrapDiagVBERTPktPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVBERTPktPercent.setStatus("mandatory")


class _MfrapDiagVBERTTestPeriod_Type(Integer32):
    """Custom type mfrapDiagVBERTTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_MfrapDiagVBERTTestPeriod_Type.__name__ = "Integer32"
_MfrapDiagVBERTTestPeriod_Object = MibTableColumn
mfrapDiagVBERTTestPeriod = _MfrapDiagVBERTTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 6, 1, 10),
    _MfrapDiagVBERTTestPeriod_Type()
)
mfrapDiagVBERTTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagVBERTTestPeriod.setStatus("mandatory")
_MfrapDiagDandiTable_ObjectIdentity = ObjectIdentity
mfrapDiagDandiTable = _MfrapDiagDandiTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 8)
)


class _MfrapDiagDandiLocLineLpbk_Type(Integer32):
    """Custom type mfrapDiagDandiLocLineLpbk based on Integer32"""
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


_MfrapDiagDandiLocLineLpbk_Type.__name__ = "Integer32"
_MfrapDiagDandiLocLineLpbk_Object = MibScalar
mfrapDiagDandiLocLineLpbk = _MfrapDiagDandiLocLineLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 8, 1),
    _MfrapDiagDandiLocLineLpbk_Type()
)
mfrapDiagDandiLocLineLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagDandiLocLineLpbk.setStatus("mandatory")


class _MfrapDiagDandiLocPylLpbk_Type(Integer32):
    """Custom type mfrapDiagDandiLocPylLpbk based on Integer32"""
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


_MfrapDiagDandiLocPylLpbk_Type.__name__ = "Integer32"
_MfrapDiagDandiLocPylLpbk_Object = MibScalar
mfrapDiagDandiLocPylLpbk = _MfrapDiagDandiLocPylLpbk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 8, 2),
    _MfrapDiagDandiLocPylLpbk_Type()
)
mfrapDiagDandiLocPylLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDiagDandiLocPylLpbk.setStatus("mandatory")
_MfrapDiagDandiTimeRemaining_Type = TimeTicks
_MfrapDiagDandiTimeRemaining_Object = MibScalar
mfrapDiagDandiTimeRemaining = _MfrapDiagDandiTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 3, 8, 6),
    _MfrapDiagDandiTimeRemaining_Type()
)
mfrapDiagDandiTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDiagDandiTimeRemaining.setStatus("mandatory")
_MfrapStatus_ObjectIdentity = ObjectIdentity
mfrapStatus = _MfrapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4)
)
_MfrapStatusT1Table_ObjectIdentity = ObjectIdentity
mfrapStatusT1Table = _MfrapStatusT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 1)
)


class _MfrapStatusT1Mode_Type(Integer32):
    """Custom type mfrapStatusT1Mode based on Integer32"""
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


_MfrapStatusT1Mode_Type.__name__ = "Integer32"
_MfrapStatusT1Mode_Object = MibScalar
mfrapStatusT1Mode = _MfrapStatusT1Mode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 1, 4),
    _MfrapStatusT1Mode_Type()
)
mfrapStatusT1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusT1Mode.setStatus("mandatory")


class _MfrapStatusT1Status_Type(Integer32):
    """Custom type mfrapStatusT1Status based on Integer32"""
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


_MfrapStatusT1Status_Type.__name__ = "Integer32"
_MfrapStatusT1Status_Object = MibScalar
mfrapStatusT1Status = _MfrapStatusT1Status_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 1, 5),
    _MfrapStatusT1Status_Type()
)
mfrapStatusT1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusT1Status.setStatus("mandatory")


class _MfrapStatusT1Alarms_Type(Integer32):
    """Custom type mfrapStatusT1Alarms based on Integer32"""
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


_MfrapStatusT1Alarms_Type.__name__ = "Integer32"
_MfrapStatusT1Alarms_Object = MibScalar
mfrapStatusT1Alarms = _MfrapStatusT1Alarms_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 1, 6),
    _MfrapStatusT1Alarms_Type()
)
mfrapStatusT1Alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusT1Alarms.setStatus("mandatory")
_MfrapVnipTopologyTable_Object = MibTable
mfrapVnipTopologyTable = _MfrapVnipTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2)
)
if mibBuilder.loadTexts:
    mfrapVnipTopologyTable.setStatus("mandatory")
_MfrapVnipTopologyEntry_Object = MibTableRow
mfrapVnipTopologyEntry = _MfrapVnipTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1)
)
mfrapVnipTopologyEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapVnipTopologyInterface"),
    (0, "MFRAP-MIB", "mfrapVnipTopologyIndex"),
)
if mibBuilder.loadTexts:
    mfrapVnipTopologyEntry.setStatus("mandatory")


class _MfrapVnipTopologyInterface_Type(Integer32):
    """Custom type mfrapVnipTopologyInterface based on Integer32"""
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


_MfrapVnipTopologyInterface_Type.__name__ = "Integer32"
_MfrapVnipTopologyInterface_Object = MibTableColumn
mfrapVnipTopologyInterface = _MfrapVnipTopologyInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 1),
    _MfrapVnipTopologyInterface_Type()
)
mfrapVnipTopologyInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyInterface.setStatus("mandatory")
_MfrapVnipTopologyIndex_Type = Integer32
_MfrapVnipTopologyIndex_Object = MibTableColumn
mfrapVnipTopologyIndex = _MfrapVnipTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 2),
    _MfrapVnipTopologyIndex_Type()
)
mfrapVnipTopologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyIndex.setStatus("mandatory")
_MfrapVnipTopologyDlci_Type = Integer32
_MfrapVnipTopologyDlci_Object = MibTableColumn
mfrapVnipTopologyDlci = _MfrapVnipTopologyDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 3),
    _MfrapVnipTopologyDlci_Type()
)
mfrapVnipTopologyDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyDlci.setStatus("mandatory")
_MfrapVnipTopologyIpAddr_Type = IpAddress
_MfrapVnipTopologyIpAddr_Object = MibTableColumn
mfrapVnipTopologyIpAddr = _MfrapVnipTopologyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 4),
    _MfrapVnipTopologyIpAddr_Type()
)
mfrapVnipTopologyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyIpAddr.setStatus("mandatory")
_MfrapVnipTopologyNumHops_Type = Integer32
_MfrapVnipTopologyNumHops_Object = MibTableColumn
mfrapVnipTopologyNumHops = _MfrapVnipTopologyNumHops_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 5),
    _MfrapVnipTopologyNumHops_Type()
)
mfrapVnipTopologyNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyNumHops.setStatus("mandatory")
_MfrapVnipTopologyLocalDlci_Type = Integer32
_MfrapVnipTopologyLocalDlci_Object = MibTableColumn
mfrapVnipTopologyLocalDlci = _MfrapVnipTopologyLocalDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 6),
    _MfrapVnipTopologyLocalDlci_Type()
)
mfrapVnipTopologyLocalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopologyLocalDlci.setStatus("mandatory")
_MfrapVnipTopoTDNumSamples_Type = Counter32
_MfrapVnipTopoTDNumSamples_Object = MibTableColumn
mfrapVnipTopoTDNumSamples = _MfrapVnipTopoTDNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 10),
    _MfrapVnipTopoTDNumSamples_Type()
)
mfrapVnipTopoTDNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoTDNumSamples.setStatus("mandatory")
_MfrapVnipTopoTDAvgDelay_Type = Counter32
_MfrapVnipTopoTDAvgDelay_Object = MibTableColumn
mfrapVnipTopoTDAvgDelay = _MfrapVnipTopoTDAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 11),
    _MfrapVnipTopoTDAvgDelay_Type()
)
mfrapVnipTopoTDAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoTDAvgDelay.setStatus("mandatory")
_MfrapVnipTopoTDMaxDelay_Type = Counter32
_MfrapVnipTopoTDMaxDelay_Object = MibTableColumn
mfrapVnipTopoTDMaxDelay = _MfrapVnipTopoTDMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 12),
    _MfrapVnipTopoTDMaxDelay_Type()
)
mfrapVnipTopoTDMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoTDMaxDelay.setStatus("mandatory")
_MfrapVnipTopoTDMinDelay_Type = Counter32
_MfrapVnipTopoTDMinDelay_Object = MibTableColumn
mfrapVnipTopoTDMinDelay = _MfrapVnipTopoTDMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 13),
    _MfrapVnipTopoTDMinDelay_Type()
)
mfrapVnipTopoTDMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoTDMinDelay.setStatus("mandatory")
_MfrapVnipTopoTDLastDelay_Type = Counter32
_MfrapVnipTopoTDLastDelay_Object = MibTableColumn
mfrapVnipTopoTDLastDelay = _MfrapVnipTopoTDLastDelay_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 14),
    _MfrapVnipTopoTDLastDelay_Type()
)
mfrapVnipTopoTDLastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoTDLastDelay.setStatus("mandatory")


class _MfrapVnipTopoVLOOPStatus_Type(Integer32):
    """Custom type mfrapVnipTopoVLOOPStatus based on Integer32"""
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


_MfrapVnipTopoVLOOPStatus_Type.__name__ = "Integer32"
_MfrapVnipTopoVLOOPStatus_Object = MibTableColumn
mfrapVnipTopoVLOOPStatus = _MfrapVnipTopoVLOOPStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 15),
    _MfrapVnipTopoVLOOPStatus_Type()
)
mfrapVnipTopoVLOOPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVLOOPStatus.setStatus("mandatory")


class _MfrapVnipTopoVBERTStatus_Type(Integer32):
    """Custom type mfrapVnipTopoVBERTStatus based on Integer32"""
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


_MfrapVnipTopoVBERTStatus_Type.__name__ = "Integer32"
_MfrapVnipTopoVBERTStatus_Object = MibTableColumn
mfrapVnipTopoVBERTStatus = _MfrapVnipTopoVBERTStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 16),
    _MfrapVnipTopoVBERTStatus_Type()
)
mfrapVnipTopoVBERTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBERTStatus.setStatus("mandatory")
_MfrapVnipTopoVBertTxDESetFrames_Type = Counter32
_MfrapVnipTopoVBertTxDESetFrames_Object = MibTableColumn
mfrapVnipTopoVBertTxDESetFrames = _MfrapVnipTopoVBertTxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 17),
    _MfrapVnipTopoVBertTxDESetFrames_Type()
)
mfrapVnipTopoVBertTxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertTxDESetFrames.setStatus("mandatory")
_MfrapVnipTopoVBertRxDESetFrames_Type = Counter32
_MfrapVnipTopoVBertRxDESetFrames_Object = MibTableColumn
mfrapVnipTopoVBertRxDESetFrames = _MfrapVnipTopoVBertRxDESetFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 18),
    _MfrapVnipTopoVBertRxDESetFrames_Type()
)
mfrapVnipTopoVBertRxDESetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertRxDESetFrames.setStatus("mandatory")
_MfrapVnipTopoVBertTxDEClrFrames_Type = Counter32
_MfrapVnipTopoVBertTxDEClrFrames_Object = MibTableColumn
mfrapVnipTopoVBertTxDEClrFrames = _MfrapVnipTopoVBertTxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 19),
    _MfrapVnipTopoVBertTxDEClrFrames_Type()
)
mfrapVnipTopoVBertTxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertTxDEClrFrames.setStatus("mandatory")
_MfrapVnipTopoVBertRxDEClrFrames_Type = Counter32
_MfrapVnipTopoVBertRxDEClrFrames_Object = MibTableColumn
mfrapVnipTopoVBertRxDEClrFrames = _MfrapVnipTopoVBertRxDEClrFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 20),
    _MfrapVnipTopoVBertRxDEClrFrames_Type()
)
mfrapVnipTopoVBertRxDEClrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertRxDEClrFrames.setStatus("mandatory")
_MfrapVnipTopoVBertTransitDelayMax_Type = Counter32
_MfrapVnipTopoVBertTransitDelayMax_Object = MibTableColumn
mfrapVnipTopoVBertTransitDelayMax = _MfrapVnipTopoVBertTransitDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 21),
    _MfrapVnipTopoVBertTransitDelayMax_Type()
)
mfrapVnipTopoVBertTransitDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertTransitDelayMax.setStatus("mandatory")
_MfrapVnipTopoVBertTransitDelayAvg_Type = Counter32
_MfrapVnipTopoVBertTransitDelayAvg_Object = MibTableColumn
mfrapVnipTopoVBertTransitDelayAvg = _MfrapVnipTopoVBertTransitDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 22),
    _MfrapVnipTopoVBertTransitDelayAvg_Type()
)
mfrapVnipTopoVBertTransitDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertTransitDelayAvg.setStatus("mandatory")
_MfrapVnipTopoVBertTimeElapse_Type = TimeTicks
_MfrapVnipTopoVBertTimeElapse_Object = MibTableColumn
mfrapVnipTopoVBertTimeElapse = _MfrapVnipTopoVBertTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 23),
    _MfrapVnipTopoVBertTimeElapse_Type()
)
mfrapVnipTopoVBertTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertTimeElapse.setStatus("mandatory")
_MfrapVnipTopoVBertPerUtilCIR_Type = Integer32
_MfrapVnipTopoVBertPerUtilCIR_Object = MibTableColumn
mfrapVnipTopoVBertPerUtilCIR = _MfrapVnipTopoVBertPerUtilCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 24),
    _MfrapVnipTopoVBertPerUtilCIR_Type()
)
mfrapVnipTopoVBertPerUtilCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertPerUtilCIR.setStatus("mandatory")
_MfrapVnipTopoVBertPerUtilEIR_Type = Integer32
_MfrapVnipTopoVBertPerUtilEIR_Object = MibTableColumn
mfrapVnipTopoVBertPerUtilEIR = _MfrapVnipTopoVBertPerUtilEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 2, 1, 25),
    _MfrapVnipTopoVBertPerUtilEIR_Type()
)
mfrapVnipTopoVBertPerUtilEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapVnipTopoVBertPerUtilEIR.setStatus("mandatory")
_MfrapStatusMgmtTable_ObjectIdentity = ObjectIdentity
mfrapStatusMgmtTable = _MfrapStatusMgmtTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3)
)


class _MfrapStatusMgmtChannel_Type(Integer32):
    """Custom type mfrapStatusMgmtChannel based on Integer32"""
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


_MfrapStatusMgmtChannel_Type.__name__ = "Integer32"
_MfrapStatusMgmtChannel_Object = MibScalar
mfrapStatusMgmtChannel = _MfrapStatusMgmtChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3, 1),
    _MfrapStatusMgmtChannel_Type()
)
mfrapStatusMgmtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusMgmtChannel.setStatus("mandatory")


class _MfrapStatusMgmtInterface_Type(Integer32):
    """Custom type mfrapStatusMgmtInterface based on Integer32"""
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


_MfrapStatusMgmtInterface_Type.__name__ = "Integer32"
_MfrapStatusMgmtInterface_Object = MibScalar
mfrapStatusMgmtInterface = _MfrapStatusMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3, 2),
    _MfrapStatusMgmtInterface_Type()
)
mfrapStatusMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusMgmtInterface.setStatus("mandatory")


class _MfrapStatusMgmtInterfaceStatus_Type(Integer32):
    """Custom type mfrapStatusMgmtInterfaceStatus based on Integer32"""
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


_MfrapStatusMgmtInterfaceStatus_Type.__name__ = "Integer32"
_MfrapStatusMgmtInterfaceStatus_Object = MibScalar
mfrapStatusMgmtInterfaceStatus = _MfrapStatusMgmtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3, 3),
    _MfrapStatusMgmtInterfaceStatus_Type()
)
mfrapStatusMgmtInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusMgmtInterfaceStatus.setStatus("mandatory")
_MfrapStatusMgmtDefaultDLCINo_Type = Integer32
_MfrapStatusMgmtDefaultDLCINo_Object = MibScalar
mfrapStatusMgmtDefaultDLCINo = _MfrapStatusMgmtDefaultDLCINo_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3, 4),
    _MfrapStatusMgmtDefaultDLCINo_Type()
)
mfrapStatusMgmtDefaultDLCINo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusMgmtDefaultDLCINo.setStatus("mandatory")


class _MfrapStatusMgmtDefaultDLCIStatus_Type(Integer32):
    """Custom type mfrapStatusMgmtDefaultDLCIStatus based on Integer32"""
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


_MfrapStatusMgmtDefaultDLCIStatus_Type.__name__ = "Integer32"
_MfrapStatusMgmtDefaultDLCIStatus_Object = MibScalar
mfrapStatusMgmtDefaultDLCIStatus = _MfrapStatusMgmtDefaultDLCIStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 3, 5),
    _MfrapStatusMgmtDefaultDLCIStatus_Type()
)
mfrapStatusMgmtDefaultDLCIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusMgmtDefaultDLCIStatus.setStatus("mandatory")
_MfrapStatusLedTable_ObjectIdentity = ObjectIdentity
mfrapStatusLedTable = _MfrapStatusLedTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4)
)


class _MfrapStatusDteModeLED_Type(Integer32):
    """Custom type mfrapStatusDteModeLED based on Integer32"""
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


_MfrapStatusDteModeLED_Type.__name__ = "Integer32"
_MfrapStatusDteModeLED_Object = MibScalar
mfrapStatusDteModeLED = _MfrapStatusDteModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 1),
    _MfrapStatusDteModeLED_Type()
)
mfrapStatusDteModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteModeLED.setStatus("mandatory")


class _MfrapStatusDteStatusLED_Type(Integer32):
    """Custom type mfrapStatusDteStatusLED based on Integer32"""
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


_MfrapStatusDteStatusLED_Type.__name__ = "Integer32"
_MfrapStatusDteStatusLED_Object = MibScalar
mfrapStatusDteStatusLED = _MfrapStatusDteStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 2),
    _MfrapStatusDteStatusLED_Type()
)
mfrapStatusDteStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteStatusLED.setStatus("mandatory")


class _MfrapStatusDteTxLED_Type(Integer32):
    """Custom type mfrapStatusDteTxLED based on Integer32"""
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


_MfrapStatusDteTxLED_Type.__name__ = "Integer32"
_MfrapStatusDteTxLED_Object = MibScalar
mfrapStatusDteTxLED = _MfrapStatusDteTxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 3),
    _MfrapStatusDteTxLED_Type()
)
mfrapStatusDteTxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteTxLED.setStatus("mandatory")


class _MfrapStatusDteRxLED_Type(Integer32):
    """Custom type mfrapStatusDteRxLED based on Integer32"""
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


_MfrapStatusDteRxLED_Type.__name__ = "Integer32"
_MfrapStatusDteRxLED_Object = MibScalar
mfrapStatusDteRxLED = _MfrapStatusDteRxLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 4),
    _MfrapStatusDteRxLED_Type()
)
mfrapStatusDteRxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteRxLED.setStatus("mandatory")


class _MfrapStatusT1ModeLED_Type(Integer32):
    """Custom type mfrapStatusT1ModeLED based on Integer32"""
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


_MfrapStatusT1ModeLED_Type.__name__ = "Integer32"
_MfrapStatusT1ModeLED_Object = MibScalar
mfrapStatusT1ModeLED = _MfrapStatusT1ModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 5),
    _MfrapStatusT1ModeLED_Type()
)
mfrapStatusT1ModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusT1ModeLED.setStatus("mandatory")


class _MfrapStatusT1StatusLED_Type(Integer32):
    """Custom type mfrapStatusT1StatusLED based on Integer32"""
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


_MfrapStatusT1StatusLED_Type.__name__ = "Integer32"
_MfrapStatusT1StatusLED_Object = MibScalar
mfrapStatusT1StatusLED = _MfrapStatusT1StatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 6),
    _MfrapStatusT1StatusLED_Type()
)
mfrapStatusT1StatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusT1StatusLED.setStatus("mandatory")


class _MfrapStatusAllLEDs_Type(DisplayString):
    """Custom type mfrapStatusAllLEDs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MfrapStatusAllLEDs_Type.__name__ = "DisplayString"
_MfrapStatusAllLEDs_Object = MibScalar
mfrapStatusAllLEDs = _MfrapStatusAllLEDs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 7),
    _MfrapStatusAllLEDs_Type()
)
mfrapStatusAllLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusAllLEDs.setStatus("mandatory")


class _MfrapStatusDandiModeLED_Type(Integer32):
    """Custom type mfrapStatusDandiModeLED based on Integer32"""
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


_MfrapStatusDandiModeLED_Type.__name__ = "Integer32"
_MfrapStatusDandiModeLED_Object = MibScalar
mfrapStatusDandiModeLED = _MfrapStatusDandiModeLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 8),
    _MfrapStatusDandiModeLED_Type()
)
mfrapStatusDandiModeLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDandiModeLED.setStatus("mandatory")


class _MfrapStatusDandiStatusLED_Type(Integer32):
    """Custom type mfrapStatusDandiStatusLED based on Integer32"""
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
          ("offLED-Dandi-no-signal", 1),
          ("redLED-red-alarm", 4),
          ("yellowLED-remote-alarm", 3))
    )


_MfrapStatusDandiStatusLED_Type.__name__ = "Integer32"
_MfrapStatusDandiStatusLED_Object = MibScalar
mfrapStatusDandiStatusLED = _MfrapStatusDandiStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 4, 9),
    _MfrapStatusDandiStatusLED_Type()
)
mfrapStatusDandiStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDandiStatusLED.setStatus("mandatory")


class _MfrapVnipTransitDelayClear_Type(Integer32):
    """Custom type mfrapVnipTransitDelayClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-transit-delay", 1)
    )


_MfrapVnipTransitDelayClear_Type.__name__ = "Integer32"
_MfrapVnipTransitDelayClear_Object = MibScalar
mfrapVnipTransitDelayClear = _MfrapVnipTransitDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 5),
    _MfrapVnipTransitDelayClear_Type()
)
mfrapVnipTransitDelayClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapVnipTransitDelayClear.setStatus("mandatory")


class _MfrapLmiSourcing_Type(Integer32):
    """Custom type mfrapLmiSourcing based on Integer32"""
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


_MfrapLmiSourcing_Type.__name__ = "Integer32"
_MfrapLmiSourcing_Object = MibScalar
mfrapLmiSourcing = _MfrapLmiSourcing_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 6),
    _MfrapLmiSourcing_Type()
)
mfrapLmiSourcing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapLmiSourcing.setStatus("mandatory")
_MfrapStatusDteTable_ObjectIdentity = ObjectIdentity
mfrapStatusDteTable = _MfrapStatusDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7)
)


class _MfrapStatusDteMode_Type(Integer32):
    """Custom type mfrapStatusDteMode based on Integer32"""
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


_MfrapStatusDteMode_Type.__name__ = "Integer32"
_MfrapStatusDteMode_Object = MibScalar
mfrapStatusDteMode = _MfrapStatusDteMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 1),
    _MfrapStatusDteMode_Type()
)
mfrapStatusDteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteMode.setStatus("mandatory")


class _MfrapStatusDteRts_Type(Integer32):
    """Custom type mfrapStatusDteRts based on Integer32"""
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


_MfrapStatusDteRts_Type.__name__ = "Integer32"
_MfrapStatusDteRts_Object = MibScalar
mfrapStatusDteRts = _MfrapStatusDteRts_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 2),
    _MfrapStatusDteRts_Type()
)
mfrapStatusDteRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteRts.setStatus("mandatory")


class _MfrapStatusDteDtr_Type(Integer32):
    """Custom type mfrapStatusDteDtr based on Integer32"""
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


_MfrapStatusDteDtr_Type.__name__ = "Integer32"
_MfrapStatusDteDtr_Object = MibScalar
mfrapStatusDteDtr = _MfrapStatusDteDtr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 3),
    _MfrapStatusDteDtr_Type()
)
mfrapStatusDteDtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteDtr.setStatus("mandatory")


class _MfrapStatusDteDcd_Type(Integer32):
    """Custom type mfrapStatusDteDcd based on Integer32"""
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


_MfrapStatusDteDcd_Type.__name__ = "Integer32"
_MfrapStatusDteDcd_Object = MibScalar
mfrapStatusDteDcd = _MfrapStatusDteDcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 4),
    _MfrapStatusDteDcd_Type()
)
mfrapStatusDteDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteDcd.setStatus("mandatory")


class _MfrapStatusDteDsr_Type(Integer32):
    """Custom type mfrapStatusDteDsr based on Integer32"""
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


_MfrapStatusDteDsr_Type.__name__ = "Integer32"
_MfrapStatusDteDsr_Object = MibScalar
mfrapStatusDteDsr = _MfrapStatusDteDsr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 5),
    _MfrapStatusDteDsr_Type()
)
mfrapStatusDteDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteDsr.setStatus("mandatory")


class _MfrapStatusDteCts_Type(Integer32):
    """Custom type mfrapStatusDteCts based on Integer32"""
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


_MfrapStatusDteCts_Type.__name__ = "Integer32"
_MfrapStatusDteCts_Object = MibScalar
mfrapStatusDteCts = _MfrapStatusDteCts_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 7, 6),
    _MfrapStatusDteCts_Type()
)
mfrapStatusDteCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDteCts.setStatus("mandatory")


class _MfrapStatusLmiAutosense_Type(Integer32):
    """Custom type mfrapStatusLmiAutosense based on Integer32"""
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


_MfrapStatusLmiAutosense_Type.__name__ = "Integer32"
_MfrapStatusLmiAutosense_Object = MibScalar
mfrapStatusLmiAutosense = _MfrapStatusLmiAutosense_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 12),
    _MfrapStatusLmiAutosense_Type()
)
mfrapStatusLmiAutosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusLmiAutosense.setStatus("mandatory")
_MfrapStatusNestTable_ObjectIdentity = ObjectIdentity
mfrapStatusNestTable = _MfrapStatusNestTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 14)
)


class _MfrapStatusNestFanOne_Type(Integer32):
    """Custom type mfrapStatusNestFanOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fan-alarm", 2),
          ("fan-ok", 1),
          ("na", 3))
    )


_MfrapStatusNestFanOne_Type.__name__ = "Integer32"
_MfrapStatusNestFanOne_Object = MibScalar
mfrapStatusNestFanOne = _MfrapStatusNestFanOne_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 14, 1),
    _MfrapStatusNestFanOne_Type()
)
mfrapStatusNestFanOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusNestFanOne.setStatus("mandatory")


class _MfrapStatusNestFanTwo_Type(Integer32):
    """Custom type mfrapStatusNestFanTwo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fan-alarm", 2),
          ("fan-ok", 1),
          ("na", 3))
    )


_MfrapStatusNestFanTwo_Type.__name__ = "Integer32"
_MfrapStatusNestFanTwo_Object = MibScalar
mfrapStatusNestFanTwo = _MfrapStatusNestFanTwo_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 14, 2),
    _MfrapStatusNestFanTwo_Type()
)
mfrapStatusNestFanTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusNestFanTwo.setStatus("mandatory")


class _MfrapStatusNestPowerSupply_Type(Integer32):
    """Custom type mfrapStatusNestPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("power-supply-alarm", 2),
          ("power-supply-na", 3),
          ("power-supply-ok", 1))
    )


_MfrapStatusNestPowerSupply_Type.__name__ = "Integer32"
_MfrapStatusNestPowerSupply_Object = MibScalar
mfrapStatusNestPowerSupply = _MfrapStatusNestPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 14, 3),
    _MfrapStatusNestPowerSupply_Type()
)
mfrapStatusNestPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusNestPowerSupply.setStatus("mandatory")


class _MfrapStatusNestSlotId_Type(Integer32):
    """Custom type mfrapStatusNestSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MfrapStatusNestSlotId_Type.__name__ = "Integer32"
_MfrapStatusNestSlotId_Object = MibScalar
mfrapStatusNestSlotId = _MfrapStatusNestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 14, 4),
    _MfrapStatusNestSlotId_Type()
)
mfrapStatusNestSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusNestSlotId.setStatus("mandatory")
_MfrapStatusDandiTable_ObjectIdentity = ObjectIdentity
mfrapStatusDandiTable = _MfrapStatusDandiTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 15)
)


class _MfrapStatusDandiMode_Type(Integer32):
    """Custom type mfrapStatusDandiMode based on Integer32"""
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


_MfrapStatusDandiMode_Type.__name__ = "Integer32"
_MfrapStatusDandiMode_Object = MibScalar
mfrapStatusDandiMode = _MfrapStatusDandiMode_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 15, 4),
    _MfrapStatusDandiMode_Type()
)
mfrapStatusDandiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDandiMode.setStatus("mandatory")


class _MfrapStatusDandiStatus_Type(Integer32):
    """Custom type mfrapStatusDandiStatus based on Integer32"""
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


_MfrapStatusDandiStatus_Type.__name__ = "Integer32"
_MfrapStatusDandiStatus_Object = MibScalar
mfrapStatusDandiStatus = _MfrapStatusDandiStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 15, 5),
    _MfrapStatusDandiStatus_Type()
)
mfrapStatusDandiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDandiStatus.setStatus("mandatory")


class _MfrapStatusDandiAlarms_Type(Integer32):
    """Custom type mfrapStatusDandiAlarms based on Integer32"""
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


_MfrapStatusDandiAlarms_Type.__name__ = "Integer32"
_MfrapStatusDandiAlarms_Object = MibScalar
mfrapStatusDandiAlarms = _MfrapStatusDandiAlarms_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 4, 15, 6),
    _MfrapStatusDandiAlarms_Type()
)
mfrapStatusDandiAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapStatusDandiAlarms.setStatus("mandatory")
_MfrapPerformance_ObjectIdentity = ObjectIdentity
mfrapPerformance = _MfrapPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5)
)
_MfrapPerfPhysicalIntf_ObjectIdentity = ObjectIdentity
mfrapPerfPhysicalIntf = _MfrapPerfPhysicalIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1)
)
_MfrapPerfT1CurrentTable_Object = MibTable
mfrapPerfT1CurrentTable = _MfrapPerfT1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mfrapPerfT1CurrentTable.setStatus("mandatory")
_MfrapT1CurrentEntry_Object = MibTableRow
mfrapT1CurrentEntry = _MfrapT1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1)
)
mfrapT1CurrentEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapT1CurrentIndex"),
)
if mibBuilder.loadTexts:
    mfrapT1CurrentEntry.setStatus("mandatory")


class _MfrapT1CurrentIndex_Type(Integer32):
    """Custom type mfrapT1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MfrapT1CurrentIndex_Type.__name__ = "Integer32"
_MfrapT1CurrentIndex_Object = MibTableColumn
mfrapT1CurrentIndex = _MfrapT1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 1),
    _MfrapT1CurrentIndex_Type()
)
mfrapT1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentIndex.setStatus("mandatory")
_MfrapT1CurrentCrc6Events_Type = Gauge32
_MfrapT1CurrentCrc6Events_Object = MibTableColumn
mfrapT1CurrentCrc6Events = _MfrapT1CurrentCrc6Events_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 2),
    _MfrapT1CurrentCrc6Events_Type()
)
mfrapT1CurrentCrc6Events.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentCrc6Events.setStatus("mandatory")
_MfrapT1CurrentOofEvents_Type = Gauge32
_MfrapT1CurrentOofEvents_Object = MibTableColumn
mfrapT1CurrentOofEvents = _MfrapT1CurrentOofEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 3),
    _MfrapT1CurrentOofEvents_Type()
)
mfrapT1CurrentOofEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentOofEvents.setStatus("mandatory")
_MfrapT1CurrentESs_Type = Gauge32
_MfrapT1CurrentESs_Object = MibTableColumn
mfrapT1CurrentESs = _MfrapT1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 4),
    _MfrapT1CurrentESs_Type()
)
mfrapT1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentESs.setStatus("mandatory")
_MfrapT1CurrentSESs_Type = Gauge32
_MfrapT1CurrentSESs_Object = MibTableColumn
mfrapT1CurrentSESs = _MfrapT1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 5),
    _MfrapT1CurrentSESs_Type()
)
mfrapT1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentSESs.setStatus("mandatory")
_MfrapT1CurrentSEFSs_Type = Gauge32
_MfrapT1CurrentSEFSs_Object = MibTableColumn
mfrapT1CurrentSEFSs = _MfrapT1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 6),
    _MfrapT1CurrentSEFSs_Type()
)
mfrapT1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentSEFSs.setStatus("mandatory")
_MfrapT1CurrentUASs_Type = Gauge32
_MfrapT1CurrentUASs_Object = MibTableColumn
mfrapT1CurrentUASs = _MfrapT1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 7),
    _MfrapT1CurrentUASs_Type()
)
mfrapT1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentUASs.setStatus("mandatory")
_MfrapT1CurrentCSSs_Type = Gauge32
_MfrapT1CurrentCSSs_Object = MibTableColumn
mfrapT1CurrentCSSs = _MfrapT1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 8),
    _MfrapT1CurrentCSSs_Type()
)
mfrapT1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentCSSs.setStatus("mandatory")
_MfrapT1CurrentBESs_Type = Gauge32
_MfrapT1CurrentBESs_Object = MibTableColumn
mfrapT1CurrentBESs = _MfrapT1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 9),
    _MfrapT1CurrentBESs_Type()
)
mfrapT1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentBESs.setStatus("mandatory")
_MfrapT1CurrentLCVs_Type = Gauge32
_MfrapT1CurrentLCVs_Object = MibTableColumn
mfrapT1CurrentLCVs = _MfrapT1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 1, 1, 10),
    _MfrapT1CurrentLCVs_Type()
)
mfrapT1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1CurrentLCVs.setStatus("mandatory")
_MfrapPerfT1IntervalTable_Object = MibTable
mfrapPerfT1IntervalTable = _MfrapPerfT1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mfrapPerfT1IntervalTable.setStatus("mandatory")
_MfrapT1IntervalEntry_Object = MibTableRow
mfrapT1IntervalEntry = _MfrapT1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1)
)
mfrapT1IntervalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapT1IntervalIndex"),
    (0, "MFRAP-MIB", "mfrapT1IntervalNumber"),
)
if mibBuilder.loadTexts:
    mfrapT1IntervalEntry.setStatus("mandatory")


class _MfrapT1IntervalIndex_Type(Integer32):
    """Custom type mfrapT1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MfrapT1IntervalIndex_Type.__name__ = "Integer32"
_MfrapT1IntervalIndex_Object = MibTableColumn
mfrapT1IntervalIndex = _MfrapT1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 1),
    _MfrapT1IntervalIndex_Type()
)
mfrapT1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalIndex.setStatus("mandatory")


class _MfrapT1IntervalNumber_Type(Integer32):
    """Custom type mfrapT1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MfrapT1IntervalNumber_Type.__name__ = "Integer32"
_MfrapT1IntervalNumber_Object = MibTableColumn
mfrapT1IntervalNumber = _MfrapT1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 2),
    _MfrapT1IntervalNumber_Type()
)
mfrapT1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalNumber.setStatus("mandatory")
_MfrapT1IntervalESs_Type = Gauge32
_MfrapT1IntervalESs_Object = MibTableColumn
mfrapT1IntervalESs = _MfrapT1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 3),
    _MfrapT1IntervalESs_Type()
)
mfrapT1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalESs.setStatus("mandatory")
_MfrapT1IntervalSESs_Type = Gauge32
_MfrapT1IntervalSESs_Object = MibTableColumn
mfrapT1IntervalSESs = _MfrapT1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 4),
    _MfrapT1IntervalSESs_Type()
)
mfrapT1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalSESs.setStatus("mandatory")
_MfrapT1IntervalSEFSs_Type = Gauge32
_MfrapT1IntervalSEFSs_Object = MibTableColumn
mfrapT1IntervalSEFSs = _MfrapT1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 5),
    _MfrapT1IntervalSEFSs_Type()
)
mfrapT1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalSEFSs.setStatus("mandatory")
_MfrapT1IntervalUASs_Type = Gauge32
_MfrapT1IntervalUASs_Object = MibTableColumn
mfrapT1IntervalUASs = _MfrapT1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 6),
    _MfrapT1IntervalUASs_Type()
)
mfrapT1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalUASs.setStatus("mandatory")
_MfrapT1IntervalCSSs_Type = Gauge32
_MfrapT1IntervalCSSs_Object = MibTableColumn
mfrapT1IntervalCSSs = _MfrapT1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 7),
    _MfrapT1IntervalCSSs_Type()
)
mfrapT1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalCSSs.setStatus("mandatory")
_MfrapT1IntervalBESs_Type = Gauge32
_MfrapT1IntervalBESs_Object = MibTableColumn
mfrapT1IntervalBESs = _MfrapT1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 8),
    _MfrapT1IntervalBESs_Type()
)
mfrapT1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalBESs.setStatus("mandatory")
_MfrapT1IntervalLCVs_Type = Gauge32
_MfrapT1IntervalLCVs_Object = MibTableColumn
mfrapT1IntervalLCVs = _MfrapT1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 2, 1, 9),
    _MfrapT1IntervalLCVs_Type()
)
mfrapT1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1IntervalLCVs.setStatus("mandatory")
_MfrapPerfT1TotalTable_Object = MibTable
mfrapPerfT1TotalTable = _MfrapPerfT1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3)
)
if mibBuilder.loadTexts:
    mfrapPerfT1TotalTable.setStatus("mandatory")
_MfrapT1TotalEntry_Object = MibTableRow
mfrapT1TotalEntry = _MfrapT1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1)
)
mfrapT1TotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapT1TotalIndex"),
)
if mibBuilder.loadTexts:
    mfrapT1TotalEntry.setStatus("mandatory")


class _MfrapT1TotalIndex_Type(Integer32):
    """Custom type mfrapT1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MfrapT1TotalIndex_Type.__name__ = "Integer32"
_MfrapT1TotalIndex_Object = MibTableColumn
mfrapT1TotalIndex = _MfrapT1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 1),
    _MfrapT1TotalIndex_Type()
)
mfrapT1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalIndex.setStatus("mandatory")
_MfrapT1TotalESs_Type = Gauge32
_MfrapT1TotalESs_Object = MibTableColumn
mfrapT1TotalESs = _MfrapT1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 2),
    _MfrapT1TotalESs_Type()
)
mfrapT1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalESs.setStatus("mandatory")
_MfrapT1TotalSESs_Type = Gauge32
_MfrapT1TotalSESs_Object = MibTableColumn
mfrapT1TotalSESs = _MfrapT1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 3),
    _MfrapT1TotalSESs_Type()
)
mfrapT1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalSESs.setStatus("mandatory")
_MfrapT1TotalSEFSs_Type = Gauge32
_MfrapT1TotalSEFSs_Object = MibTableColumn
mfrapT1TotalSEFSs = _MfrapT1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 4),
    _MfrapT1TotalSEFSs_Type()
)
mfrapT1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalSEFSs.setStatus("mandatory")
_MfrapT1TotalUASs_Type = Gauge32
_MfrapT1TotalUASs_Object = MibTableColumn
mfrapT1TotalUASs = _MfrapT1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 5),
    _MfrapT1TotalUASs_Type()
)
mfrapT1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalUASs.setStatus("mandatory")
_MfrapT1TotalCSSs_Type = Gauge32
_MfrapT1TotalCSSs_Object = MibTableColumn
mfrapT1TotalCSSs = _MfrapT1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 6),
    _MfrapT1TotalCSSs_Type()
)
mfrapT1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalCSSs.setStatus("mandatory")
_MfrapT1TotalBESs_Type = Gauge32
_MfrapT1TotalBESs_Object = MibTableColumn
mfrapT1TotalBESs = _MfrapT1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 7),
    _MfrapT1TotalBESs_Type()
)
mfrapT1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalBESs.setStatus("mandatory")
_MfrapT1TotalLCVs_Type = Gauge32
_MfrapT1TotalLCVs_Object = MibTableColumn
mfrapT1TotalLCVs = _MfrapT1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 3, 1, 8),
    _MfrapT1TotalLCVs_Type()
)
mfrapT1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapT1TotalLCVs.setStatus("mandatory")
_MfrapT1PerfCmdTypeTable_ObjectIdentity = ObjectIdentity
mfrapT1PerfCmdTypeTable = _MfrapT1PerfCmdTypeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 4)
)


class _MfrapT1PerfFreezeState_Type(Integer32):
    """Custom type mfrapT1PerfFreezeState based on Integer32"""
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


_MfrapT1PerfFreezeState_Type.__name__ = "Integer32"
_MfrapT1PerfFreezeState_Object = MibScalar
mfrapT1PerfFreezeState = _MfrapT1PerfFreezeState_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 4, 1),
    _MfrapT1PerfFreezeState_Type()
)
mfrapT1PerfFreezeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapT1PerfFreezeState.setStatus("mandatory")


class _MfrapT1PerfClearEvents_Type(Integer32):
    """Custom type mfrapT1PerfClearEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-events", 1)
    )


_MfrapT1PerfClearEvents_Type.__name__ = "Integer32"
_MfrapT1PerfClearEvents_Object = MibScalar
mfrapT1PerfClearEvents = _MfrapT1PerfClearEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 4, 2),
    _MfrapT1PerfClearEvents_Type()
)
mfrapT1PerfClearEvents.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapT1PerfClearEvents.setStatus("mandatory")


class _MfrapT1PerfClearAll_Type(Integer32):
    """Custom type mfrapT1PerfClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-all", 1)
    )


_MfrapT1PerfClearAll_Type.__name__ = "Integer32"
_MfrapT1PerfClearAll_Object = MibScalar
mfrapT1PerfClearAll = _MfrapT1PerfClearAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 4, 3),
    _MfrapT1PerfClearAll_Type()
)
mfrapT1PerfClearAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapT1PerfClearAll.setStatus("mandatory")
_MfrapPerfDandiCurrentTable_Object = MibTable
mfrapPerfDandiCurrentTable = _MfrapPerfDandiCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5)
)
if mibBuilder.loadTexts:
    mfrapPerfDandiCurrentTable.setStatus("mandatory")
_MfrapDandiCurrentEntry_Object = MibTableRow
mfrapDandiCurrentEntry = _MfrapDandiCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1)
)
mfrapDandiCurrentEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapDandiCurrentIndex"),
)
if mibBuilder.loadTexts:
    mfrapDandiCurrentEntry.setStatus("mandatory")


class _MfrapDandiCurrentIndex_Type(Integer32):
    """Custom type mfrapDandiCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dandi-port1", 2)
    )


_MfrapDandiCurrentIndex_Type.__name__ = "Integer32"
_MfrapDandiCurrentIndex_Object = MibTableColumn
mfrapDandiCurrentIndex = _MfrapDandiCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 1),
    _MfrapDandiCurrentIndex_Type()
)
mfrapDandiCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentIndex.setStatus("mandatory")
_MfrapDandiCurrentCrc6Events_Type = Gauge32
_MfrapDandiCurrentCrc6Events_Object = MibTableColumn
mfrapDandiCurrentCrc6Events = _MfrapDandiCurrentCrc6Events_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 2),
    _MfrapDandiCurrentCrc6Events_Type()
)
mfrapDandiCurrentCrc6Events.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentCrc6Events.setStatus("mandatory")
_MfrapDandiCurrentOofEvents_Type = Gauge32
_MfrapDandiCurrentOofEvents_Object = MibTableColumn
mfrapDandiCurrentOofEvents = _MfrapDandiCurrentOofEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 3),
    _MfrapDandiCurrentOofEvents_Type()
)
mfrapDandiCurrentOofEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentOofEvents.setStatus("mandatory")
_MfrapDandiCurrentESs_Type = Gauge32
_MfrapDandiCurrentESs_Object = MibTableColumn
mfrapDandiCurrentESs = _MfrapDandiCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 4),
    _MfrapDandiCurrentESs_Type()
)
mfrapDandiCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentESs.setStatus("mandatory")
_MfrapDandiCurrentSESs_Type = Gauge32
_MfrapDandiCurrentSESs_Object = MibTableColumn
mfrapDandiCurrentSESs = _MfrapDandiCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 5),
    _MfrapDandiCurrentSESs_Type()
)
mfrapDandiCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentSESs.setStatus("mandatory")
_MfrapDandiCurrentSEFSs_Type = Gauge32
_MfrapDandiCurrentSEFSs_Object = MibTableColumn
mfrapDandiCurrentSEFSs = _MfrapDandiCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 6),
    _MfrapDandiCurrentSEFSs_Type()
)
mfrapDandiCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentSEFSs.setStatus("mandatory")
_MfrapDandiCurrentUASs_Type = Gauge32
_MfrapDandiCurrentUASs_Object = MibTableColumn
mfrapDandiCurrentUASs = _MfrapDandiCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 7),
    _MfrapDandiCurrentUASs_Type()
)
mfrapDandiCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentUASs.setStatus("mandatory")
_MfrapDandiCurrentCSSs_Type = Gauge32
_MfrapDandiCurrentCSSs_Object = MibTableColumn
mfrapDandiCurrentCSSs = _MfrapDandiCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 8),
    _MfrapDandiCurrentCSSs_Type()
)
mfrapDandiCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentCSSs.setStatus("mandatory")
_MfrapDandiCurrentBESs_Type = Gauge32
_MfrapDandiCurrentBESs_Object = MibTableColumn
mfrapDandiCurrentBESs = _MfrapDandiCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 9),
    _MfrapDandiCurrentBESs_Type()
)
mfrapDandiCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentBESs.setStatus("mandatory")
_MfrapDandiCurrentLCVs_Type = Gauge32
_MfrapDandiCurrentLCVs_Object = MibTableColumn
mfrapDandiCurrentLCVs = _MfrapDandiCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 5, 1, 10),
    _MfrapDandiCurrentLCVs_Type()
)
mfrapDandiCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiCurrentLCVs.setStatus("mandatory")
_MfrapPerfDandiIntervalTable_Object = MibTable
mfrapPerfDandiIntervalTable = _MfrapPerfDandiIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6)
)
if mibBuilder.loadTexts:
    mfrapPerfDandiIntervalTable.setStatus("mandatory")
_MfrapDandiIntervalEntry_Object = MibTableRow
mfrapDandiIntervalEntry = _MfrapDandiIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1)
)
mfrapDandiIntervalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapDandiIntervalIndex"),
    (0, "MFRAP-MIB", "mfrapDandiIntervalNumber"),
)
if mibBuilder.loadTexts:
    mfrapDandiIntervalEntry.setStatus("mandatory")


class _MfrapDandiIntervalIndex_Type(Integer32):
    """Custom type mfrapDandiIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dandi-port1", 2)
    )


_MfrapDandiIntervalIndex_Type.__name__ = "Integer32"
_MfrapDandiIntervalIndex_Object = MibTableColumn
mfrapDandiIntervalIndex = _MfrapDandiIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 1),
    _MfrapDandiIntervalIndex_Type()
)
mfrapDandiIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalIndex.setStatus("mandatory")


class _MfrapDandiIntervalNumber_Type(Integer32):
    """Custom type mfrapDandiIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_MfrapDandiIntervalNumber_Type.__name__ = "Integer32"
_MfrapDandiIntervalNumber_Object = MibTableColumn
mfrapDandiIntervalNumber = _MfrapDandiIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 2),
    _MfrapDandiIntervalNumber_Type()
)
mfrapDandiIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalNumber.setStatus("mandatory")
_MfrapDandiIntervalESs_Type = Gauge32
_MfrapDandiIntervalESs_Object = MibTableColumn
mfrapDandiIntervalESs = _MfrapDandiIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 3),
    _MfrapDandiIntervalESs_Type()
)
mfrapDandiIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalESs.setStatus("mandatory")
_MfrapDandiIntervalSESs_Type = Gauge32
_MfrapDandiIntervalSESs_Object = MibTableColumn
mfrapDandiIntervalSESs = _MfrapDandiIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 4),
    _MfrapDandiIntervalSESs_Type()
)
mfrapDandiIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalSESs.setStatus("mandatory")
_MfrapDandiIntervalSEFSs_Type = Gauge32
_MfrapDandiIntervalSEFSs_Object = MibTableColumn
mfrapDandiIntervalSEFSs = _MfrapDandiIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 5),
    _MfrapDandiIntervalSEFSs_Type()
)
mfrapDandiIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalSEFSs.setStatus("mandatory")
_MfrapDandiIntervalUASs_Type = Gauge32
_MfrapDandiIntervalUASs_Object = MibTableColumn
mfrapDandiIntervalUASs = _MfrapDandiIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 6),
    _MfrapDandiIntervalUASs_Type()
)
mfrapDandiIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalUASs.setStatus("mandatory")
_MfrapDandiIntervalCSSs_Type = Gauge32
_MfrapDandiIntervalCSSs_Object = MibTableColumn
mfrapDandiIntervalCSSs = _MfrapDandiIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 7),
    _MfrapDandiIntervalCSSs_Type()
)
mfrapDandiIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalCSSs.setStatus("mandatory")
_MfrapDandiIntervalBESs_Type = Gauge32
_MfrapDandiIntervalBESs_Object = MibTableColumn
mfrapDandiIntervalBESs = _MfrapDandiIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 8),
    _MfrapDandiIntervalBESs_Type()
)
mfrapDandiIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalBESs.setStatus("mandatory")
_MfrapDandiIntervalLCVs_Type = Gauge32
_MfrapDandiIntervalLCVs_Object = MibTableColumn
mfrapDandiIntervalLCVs = _MfrapDandiIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 6, 1, 9),
    _MfrapDandiIntervalLCVs_Type()
)
mfrapDandiIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiIntervalLCVs.setStatus("mandatory")
_MfrapPerfDandiTotalTable_Object = MibTable
mfrapPerfDandiTotalTable = _MfrapPerfDandiTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7)
)
if mibBuilder.loadTexts:
    mfrapPerfDandiTotalTable.setStatus("mandatory")
_MfrapDandiTotalEntry_Object = MibTableRow
mfrapDandiTotalEntry = _MfrapDandiTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1)
)
mfrapDandiTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapDandiTotalIndex"),
)
if mibBuilder.loadTexts:
    mfrapDandiTotalEntry.setStatus("mandatory")


class _MfrapDandiTotalIndex_Type(Integer32):
    """Custom type mfrapDandiTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dandi-port1", 2)
    )


_MfrapDandiTotalIndex_Type.__name__ = "Integer32"
_MfrapDandiTotalIndex_Object = MibTableColumn
mfrapDandiTotalIndex = _MfrapDandiTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 1),
    _MfrapDandiTotalIndex_Type()
)
mfrapDandiTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalIndex.setStatus("mandatory")
_MfrapDandiTotalESs_Type = Gauge32
_MfrapDandiTotalESs_Object = MibTableColumn
mfrapDandiTotalESs = _MfrapDandiTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 2),
    _MfrapDandiTotalESs_Type()
)
mfrapDandiTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalESs.setStatus("mandatory")
_MfrapDandiTotalSESs_Type = Gauge32
_MfrapDandiTotalSESs_Object = MibTableColumn
mfrapDandiTotalSESs = _MfrapDandiTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 3),
    _MfrapDandiTotalSESs_Type()
)
mfrapDandiTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalSESs.setStatus("mandatory")
_MfrapDandiTotalSEFSs_Type = Gauge32
_MfrapDandiTotalSEFSs_Object = MibTableColumn
mfrapDandiTotalSEFSs = _MfrapDandiTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 4),
    _MfrapDandiTotalSEFSs_Type()
)
mfrapDandiTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalSEFSs.setStatus("mandatory")
_MfrapDandiTotalUASs_Type = Gauge32
_MfrapDandiTotalUASs_Object = MibTableColumn
mfrapDandiTotalUASs = _MfrapDandiTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 5),
    _MfrapDandiTotalUASs_Type()
)
mfrapDandiTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalUASs.setStatus("mandatory")
_MfrapDandiTotalCSSs_Type = Gauge32
_MfrapDandiTotalCSSs_Object = MibTableColumn
mfrapDandiTotalCSSs = _MfrapDandiTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 6),
    _MfrapDandiTotalCSSs_Type()
)
mfrapDandiTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalCSSs.setStatus("mandatory")
_MfrapDandiTotalBESs_Type = Gauge32
_MfrapDandiTotalBESs_Object = MibTableColumn
mfrapDandiTotalBESs = _MfrapDandiTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 7),
    _MfrapDandiTotalBESs_Type()
)
mfrapDandiTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalBESs.setStatus("mandatory")
_MfrapDandiTotalLCVs_Type = Gauge32
_MfrapDandiTotalLCVs_Object = MibTableColumn
mfrapDandiTotalLCVs = _MfrapDandiTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 7, 1, 8),
    _MfrapDandiTotalLCVs_Type()
)
mfrapDandiTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDandiTotalLCVs.setStatus("mandatory")
_MfrapDandiPerfCmdTypeTable_ObjectIdentity = ObjectIdentity
mfrapDandiPerfCmdTypeTable = _MfrapDandiPerfCmdTypeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 8)
)


class _MfrapDandiPerfFreezeState_Type(Integer32):
    """Custom type mfrapDandiPerfFreezeState based on Integer32"""
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


_MfrapDandiPerfFreezeState_Type.__name__ = "Integer32"
_MfrapDandiPerfFreezeState_Object = MibScalar
mfrapDandiPerfFreezeState = _MfrapDandiPerfFreezeState_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 8, 1),
    _MfrapDandiPerfFreezeState_Type()
)
mfrapDandiPerfFreezeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrapDandiPerfFreezeState.setStatus("mandatory")


class _MfrapDandiPerfClearEvents_Type(Integer32):
    """Custom type mfrapDandiPerfClearEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-events", 1)
    )


_MfrapDandiPerfClearEvents_Type.__name__ = "Integer32"
_MfrapDandiPerfClearEvents_Object = MibScalar
mfrapDandiPerfClearEvents = _MfrapDandiPerfClearEvents_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 8, 2),
    _MfrapDandiPerfClearEvents_Type()
)
mfrapDandiPerfClearEvents.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDandiPerfClearEvents.setStatus("mandatory")


class _MfrapDandiPerfClearAll_Type(Integer32):
    """Custom type mfrapDandiPerfClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-all", 1)
    )


_MfrapDandiPerfClearAll_Type.__name__ = "Integer32"
_MfrapDandiPerfClearAll_Object = MibScalar
mfrapDandiPerfClearAll = _MfrapDandiPerfClearAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 1, 8, 3),
    _MfrapDandiPerfClearAll_Type()
)
mfrapDandiPerfClearAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapDandiPerfClearAll.setStatus("mandatory")
_MfrapPerfMgmtIp_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIp = _MfrapPerfMgmtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2)
)
_MfrapPerfMgmtIpIFStatsTable_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIpIFStatsTable = _MfrapPerfMgmtIpIFStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 1)
)
_MfrapPerfMgmtIpIFInOctets_Type = Counter32
_MfrapPerfMgmtIpIFInOctets_Object = MibScalar
mfrapPerfMgmtIpIFInOctets = _MfrapPerfMgmtIpIFInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 1, 1),
    _MfrapPerfMgmtIpIFInOctets_Type()
)
mfrapPerfMgmtIpIFInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIFInOctets.setStatus("mandatory")
_MfrapPerfMgmtIpIFInErrors_Type = Counter32
_MfrapPerfMgmtIpIFInErrors_Object = MibScalar
mfrapPerfMgmtIpIFInErrors = _MfrapPerfMgmtIpIFInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 1, 2),
    _MfrapPerfMgmtIpIFInErrors_Type()
)
mfrapPerfMgmtIpIFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIFInErrors.setStatus("mandatory")
_MfrapPerfMgmtIpIFOutOctets_Type = Counter32
_MfrapPerfMgmtIpIFOutOctets_Object = MibScalar
mfrapPerfMgmtIpIFOutOctets = _MfrapPerfMgmtIpIFOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 1, 3),
    _MfrapPerfMgmtIpIFOutOctets_Type()
)
mfrapPerfMgmtIpIFOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIFOutOctets.setStatus("mandatory")


class _MfrapPerfMgmtIpIFOperStatus_Type(Integer32):
    """Custom type mfrapPerfMgmtIpIFOperStatus based on Integer32"""
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


_MfrapPerfMgmtIpIFOperStatus_Type.__name__ = "Integer32"
_MfrapPerfMgmtIpIFOperStatus_Object = MibScalar
mfrapPerfMgmtIpIFOperStatus = _MfrapPerfMgmtIpIFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 1, 4),
    _MfrapPerfMgmtIpIFOperStatus_Type()
)
mfrapPerfMgmtIpIFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIFOperStatus.setStatus("mandatory")
_MfrapPerfMgmtIpIPStatsTable_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIpIPStatsTable = _MfrapPerfMgmtIpIPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2)
)
_MfrapPerfMgmtIpIPInRcv_Type = Counter32
_MfrapPerfMgmtIpIPInRcv_Object = MibScalar
mfrapPerfMgmtIpIPInRcv = _MfrapPerfMgmtIpIPInRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 1),
    _MfrapPerfMgmtIpIPInRcv_Type()
)
mfrapPerfMgmtIpIPInRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInRcv.setStatus("mandatory")
_MfrapPerfMgmtIpIPInHdrErr_Type = Counter32
_MfrapPerfMgmtIpIPInHdrErr_Object = MibScalar
mfrapPerfMgmtIpIPInHdrErr = _MfrapPerfMgmtIpIPInHdrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 2),
    _MfrapPerfMgmtIpIPInHdrErr_Type()
)
mfrapPerfMgmtIpIPInHdrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInHdrErr.setStatus("mandatory")
_MfrapPerfMgmtIpIPInAddrErr_Type = Counter32
_MfrapPerfMgmtIpIPInAddrErr_Object = MibScalar
mfrapPerfMgmtIpIPInAddrErr = _MfrapPerfMgmtIpIPInAddrErr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 3),
    _MfrapPerfMgmtIpIPInAddrErr_Type()
)
mfrapPerfMgmtIpIPInAddrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInAddrErr.setStatus("mandatory")
_MfrapPerfMgmtIpIPInProtUnk_Type = Counter32
_MfrapPerfMgmtIpIPInProtUnk_Object = MibScalar
mfrapPerfMgmtIpIPInProtUnk = _MfrapPerfMgmtIpIPInProtUnk_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 4),
    _MfrapPerfMgmtIpIPInProtUnk_Type()
)
mfrapPerfMgmtIpIPInProtUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInProtUnk.setStatus("mandatory")
_MfrapPerfMgmtIpIPInDscrd_Type = Counter32
_MfrapPerfMgmtIpIPInDscrd_Object = MibScalar
mfrapPerfMgmtIpIPInDscrd = _MfrapPerfMgmtIpIPInDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 5),
    _MfrapPerfMgmtIpIPInDscrd_Type()
)
mfrapPerfMgmtIpIPInDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInDscrd.setStatus("mandatory")
_MfrapPerfMgmtIpIPInDlvrs_Type = Counter32
_MfrapPerfMgmtIpIPInDlvrs_Object = MibScalar
mfrapPerfMgmtIpIPInDlvrs = _MfrapPerfMgmtIpIPInDlvrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 6),
    _MfrapPerfMgmtIpIPInDlvrs_Type()
)
mfrapPerfMgmtIpIPInDlvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPInDlvrs.setStatus("mandatory")
_MfrapPerfMgmtIpIPOutRqst_Type = Counter32
_MfrapPerfMgmtIpIPOutRqst_Object = MibScalar
mfrapPerfMgmtIpIPOutRqst = _MfrapPerfMgmtIpIPOutRqst_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 7),
    _MfrapPerfMgmtIpIPOutRqst_Type()
)
mfrapPerfMgmtIpIPOutRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPOutRqst.setStatus("mandatory")
_MfrapPerfMgmtIpIPOutDscrd_Type = Counter32
_MfrapPerfMgmtIpIPOutDscrd_Object = MibScalar
mfrapPerfMgmtIpIPOutDscrd = _MfrapPerfMgmtIpIPOutDscrd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 8),
    _MfrapPerfMgmtIpIPOutDscrd_Type()
)
mfrapPerfMgmtIpIPOutDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPOutDscrd.setStatus("mandatory")
_MfrapPerfMgmtIpIPOutNoRt_Type = Counter32
_MfrapPerfMgmtIpIPOutNoRt_Object = MibScalar
mfrapPerfMgmtIpIPOutNoRt = _MfrapPerfMgmtIpIPOutNoRt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 2, 9),
    _MfrapPerfMgmtIpIPOutNoRt_Type()
)
mfrapPerfMgmtIpIPOutNoRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpIPOutNoRt.setStatus("mandatory")
_MfrapPerfMgmtIpICMPStatsTable_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIpICMPStatsTable = _MfrapPerfMgmtIpICMPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3)
)
_MfrapPerfMgmtIpICMPInMsgs_Type = Counter32
_MfrapPerfMgmtIpICMPInMsgs_Object = MibScalar
mfrapPerfMgmtIpICMPInMsgs = _MfrapPerfMgmtIpICMPInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 1),
    _MfrapPerfMgmtIpICMPInMsgs_Type()
)
mfrapPerfMgmtIpICMPInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInMsgs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInErrors_Type = Counter32
_MfrapPerfMgmtIpICMPInErrors_Object = MibScalar
mfrapPerfMgmtIpICMPInErrors = _MfrapPerfMgmtIpICMPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 2),
    _MfrapPerfMgmtIpICMPInErrors_Type()
)
mfrapPerfMgmtIpICMPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInErrors.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInDestUnreachs_Type = Counter32
_MfrapPerfMgmtIpICMPInDestUnreachs_Object = MibScalar
mfrapPerfMgmtIpICMPInDestUnreachs = _MfrapPerfMgmtIpICMPInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 3),
    _MfrapPerfMgmtIpICMPInDestUnreachs_Type()
)
mfrapPerfMgmtIpICMPInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInDestUnreachs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInTimeExcds_Type = Counter32
_MfrapPerfMgmtIpICMPInTimeExcds_Object = MibScalar
mfrapPerfMgmtIpICMPInTimeExcds = _MfrapPerfMgmtIpICMPInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 4),
    _MfrapPerfMgmtIpICMPInTimeExcds_Type()
)
mfrapPerfMgmtIpICMPInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInTimeExcds.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInParmProbs_Type = Counter32
_MfrapPerfMgmtIpICMPInParmProbs_Object = MibScalar
mfrapPerfMgmtIpICMPInParmProbs = _MfrapPerfMgmtIpICMPInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 5),
    _MfrapPerfMgmtIpICMPInParmProbs_Type()
)
mfrapPerfMgmtIpICMPInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInParmProbs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInRedirects_Type = Counter32
_MfrapPerfMgmtIpICMPInRedirects_Object = MibScalar
mfrapPerfMgmtIpICMPInRedirects = _MfrapPerfMgmtIpICMPInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 6),
    _MfrapPerfMgmtIpICMPInRedirects_Type()
)
mfrapPerfMgmtIpICMPInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInRedirects.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInEchos_Type = Counter32
_MfrapPerfMgmtIpICMPInEchos_Object = MibScalar
mfrapPerfMgmtIpICMPInEchos = _MfrapPerfMgmtIpICMPInEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 7),
    _MfrapPerfMgmtIpICMPInEchos_Type()
)
mfrapPerfMgmtIpICMPInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInEchos.setStatus("mandatory")
_MfrapPerfMgmtIpICMPInEchoReps_Type = Counter32
_MfrapPerfMgmtIpICMPInEchoReps_Object = MibScalar
mfrapPerfMgmtIpICMPInEchoReps = _MfrapPerfMgmtIpICMPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 8),
    _MfrapPerfMgmtIpICMPInEchoReps_Type()
)
mfrapPerfMgmtIpICMPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPInEchoReps.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutMsgs_Type = Counter32
_MfrapPerfMgmtIpICMPOutMsgs_Object = MibScalar
mfrapPerfMgmtIpICMPOutMsgs = _MfrapPerfMgmtIpICMPOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 9),
    _MfrapPerfMgmtIpICMPOutMsgs_Type()
)
mfrapPerfMgmtIpICMPOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutMsgs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutErrors_Type = Counter32
_MfrapPerfMgmtIpICMPOutErrors_Object = MibScalar
mfrapPerfMgmtIpICMPOutErrors = _MfrapPerfMgmtIpICMPOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 10),
    _MfrapPerfMgmtIpICMPOutErrors_Type()
)
mfrapPerfMgmtIpICMPOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutErrors.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutDestUnreachs_Type = Counter32
_MfrapPerfMgmtIpICMPOutDestUnreachs_Object = MibScalar
mfrapPerfMgmtIpICMPOutDestUnreachs = _MfrapPerfMgmtIpICMPOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 11),
    _MfrapPerfMgmtIpICMPOutDestUnreachs_Type()
)
mfrapPerfMgmtIpICMPOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutDestUnreachs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutParmProbs_Type = Counter32
_MfrapPerfMgmtIpICMPOutParmProbs_Object = MibScalar
mfrapPerfMgmtIpICMPOutParmProbs = _MfrapPerfMgmtIpICMPOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 12),
    _MfrapPerfMgmtIpICMPOutParmProbs_Type()
)
mfrapPerfMgmtIpICMPOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutParmProbs.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutRedirects_Type = Counter32
_MfrapPerfMgmtIpICMPOutRedirects_Object = MibScalar
mfrapPerfMgmtIpICMPOutRedirects = _MfrapPerfMgmtIpICMPOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 13),
    _MfrapPerfMgmtIpICMPOutRedirects_Type()
)
mfrapPerfMgmtIpICMPOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutRedirects.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutEchos_Type = Counter32
_MfrapPerfMgmtIpICMPOutEchos_Object = MibScalar
mfrapPerfMgmtIpICMPOutEchos = _MfrapPerfMgmtIpICMPOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 14),
    _MfrapPerfMgmtIpICMPOutEchos_Type()
)
mfrapPerfMgmtIpICMPOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutEchos.setStatus("mandatory")
_MfrapPerfMgmtIpICMPOutEchoReps_Type = Counter32
_MfrapPerfMgmtIpICMPOutEchoReps_Object = MibScalar
mfrapPerfMgmtIpICMPOutEchoReps = _MfrapPerfMgmtIpICMPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 3, 15),
    _MfrapPerfMgmtIpICMPOutEchoReps_Type()
)
mfrapPerfMgmtIpICMPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpICMPOutEchoReps.setStatus("mandatory")
_MfrapPerfMgmtIpUDPStatsTable_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIpUDPStatsTable = _MfrapPerfMgmtIpUDPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 4)
)
_MfrapPerfMgmtIpUDPInDatagrams_Type = Counter32
_MfrapPerfMgmtIpUDPInDatagrams_Object = MibScalar
mfrapPerfMgmtIpUDPInDatagrams = _MfrapPerfMgmtIpUDPInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 4, 1),
    _MfrapPerfMgmtIpUDPInDatagrams_Type()
)
mfrapPerfMgmtIpUDPInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpUDPInDatagrams.setStatus("mandatory")
_MfrapPerfMgmtIpUDPOutDatagrams_Type = Counter32
_MfrapPerfMgmtIpUDPOutDatagrams_Object = MibScalar
mfrapPerfMgmtIpUDPOutDatagrams = _MfrapPerfMgmtIpUDPOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 4, 2),
    _MfrapPerfMgmtIpUDPOutDatagrams_Type()
)
mfrapPerfMgmtIpUDPOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpUDPOutDatagrams.setStatus("mandatory")
_MfrapPerfMgmtIpUDPNoPorts_Type = Counter32
_MfrapPerfMgmtIpUDPNoPorts_Object = MibScalar
mfrapPerfMgmtIpUDPNoPorts = _MfrapPerfMgmtIpUDPNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 4, 3),
    _MfrapPerfMgmtIpUDPNoPorts_Type()
)
mfrapPerfMgmtIpUDPNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpUDPNoPorts.setStatus("mandatory")
_MfrapPerfMgmtIpTCPStatsTable_ObjectIdentity = ObjectIdentity
mfrapPerfMgmtIpTCPStatsTable = _MfrapPerfMgmtIpTCPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5)
)
_MfrapPerfMgmtIpTCPActiveOpens_Type = Counter32
_MfrapPerfMgmtIpTCPActiveOpens_Object = MibScalar
mfrapPerfMgmtIpTCPActiveOpens = _MfrapPerfMgmtIpTCPActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 1),
    _MfrapPerfMgmtIpTCPActiveOpens_Type()
)
mfrapPerfMgmtIpTCPActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPActiveOpens.setStatus("mandatory")
_MfrapPerfMgmtIpTCPPassiveOpens_Type = Counter32
_MfrapPerfMgmtIpTCPPassiveOpens_Object = MibScalar
mfrapPerfMgmtIpTCPPassiveOpens = _MfrapPerfMgmtIpTCPPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 2),
    _MfrapPerfMgmtIpTCPPassiveOpens_Type()
)
mfrapPerfMgmtIpTCPPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPPassiveOpens.setStatus("mandatory")
_MfrapPerfMgmtIpTCPAttemptFails_Type = Counter32
_MfrapPerfMgmtIpTCPAttemptFails_Object = MibScalar
mfrapPerfMgmtIpTCPAttemptFails = _MfrapPerfMgmtIpTCPAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 3),
    _MfrapPerfMgmtIpTCPAttemptFails_Type()
)
mfrapPerfMgmtIpTCPAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPAttemptFails.setStatus("mandatory")
_MfrapPerfMgmtIpTCPCurrEstab_Type = Gauge32
_MfrapPerfMgmtIpTCPCurrEstab_Object = MibScalar
mfrapPerfMgmtIpTCPCurrEstab = _MfrapPerfMgmtIpTCPCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 4),
    _MfrapPerfMgmtIpTCPCurrEstab_Type()
)
mfrapPerfMgmtIpTCPCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPCurrEstab.setStatus("mandatory")
_MfrapPerfMgmtIpTCPInSegs_Type = Counter32
_MfrapPerfMgmtIpTCPInSegs_Object = MibScalar
mfrapPerfMgmtIpTCPInSegs = _MfrapPerfMgmtIpTCPInSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 5),
    _MfrapPerfMgmtIpTCPInSegs_Type()
)
mfrapPerfMgmtIpTCPInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPInSegs.setStatus("mandatory")
_MfrapPerfMgmtIpTCPOutSegs_Type = Counter32
_MfrapPerfMgmtIpTCPOutSegs_Object = MibScalar
mfrapPerfMgmtIpTCPOutSegs = _MfrapPerfMgmtIpTCPOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 2, 5, 6),
    _MfrapPerfMgmtIpTCPOutSegs_Type()
)
mfrapPerfMgmtIpTCPOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfMgmtIpTCPOutSegs.setStatus("mandatory")
_MfrapPerfThruput_ObjectIdentity = ObjectIdentity
mfrapPerfThruput = _MfrapPerfThruput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3)
)
_MfrapPerfThruputPerIntfTable_Object = MibTable
mfrapPerfThruputPerIntfTable = _MfrapPerfThruputPerIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfTable.setStatus("mandatory")
_MfrapPerfThruputPerIntfEntry_Object = MibTableRow
mfrapPerfThruputPerIntfEntry = _MfrapPerfThruputPerIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1)
)
mfrapPerfThruputPerIntfEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfThruputPerIntfIndex"),
)
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfEntry.setStatus("mandatory")


class _MfrapPerfThruputPerIntfIndex_Type(Integer32):
    """Custom type mfrapPerfThruputPerIntfIndex based on Integer32"""
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


_MfrapPerfThruputPerIntfIndex_Type.__name__ = "Integer32"
_MfrapPerfThruputPerIntfIndex_Object = MibTableColumn
mfrapPerfThruputPerIntfIndex = _MfrapPerfThruputPerIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 1),
    _MfrapPerfThruputPerIntfIndex_Type()
)
mfrapPerfThruputPerIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfIndex.setStatus("mandatory")
_MfrapPerfThruputPerIntfRxByteCnt_Type = Counter32
_MfrapPerfThruputPerIntfRxByteCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfRxByteCnt = _MfrapPerfThruputPerIntfRxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 2),
    _MfrapPerfThruputPerIntfRxByteCnt_Type()
)
mfrapPerfThruputPerIntfRxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfRxByteCnt.setStatus("mandatory")
_MfrapPerfThruputPerIntfTxByteCnt_Type = Counter32
_MfrapPerfThruputPerIntfTxByteCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfTxByteCnt = _MfrapPerfThruputPerIntfTxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 3),
    _MfrapPerfThruputPerIntfTxByteCnt_Type()
)
mfrapPerfThruputPerIntfTxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfTxByteCnt.setStatus("mandatory")
_MfrapPerfThruputPerIntfRxFrameCnt_Type = Counter32
_MfrapPerfThruputPerIntfRxFrameCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfRxFrameCnt = _MfrapPerfThruputPerIntfRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 4),
    _MfrapPerfThruputPerIntfRxFrameCnt_Type()
)
mfrapPerfThruputPerIntfRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfRxFrameCnt.setStatus("mandatory")
_MfrapPerfThruputPerIntfTxFrameCnt_Type = Counter32
_MfrapPerfThruputPerIntfTxFrameCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfTxFrameCnt = _MfrapPerfThruputPerIntfTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 5),
    _MfrapPerfThruputPerIntfTxFrameCnt_Type()
)
mfrapPerfThruputPerIntfTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfTxFrameCnt.setStatus("mandatory")
_MfrapPerfThruputPerIntfRxCrcErrCnt_Type = Counter32
_MfrapPerfThruputPerIntfRxCrcErrCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfRxCrcErrCnt = _MfrapPerfThruputPerIntfRxCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 6),
    _MfrapPerfThruputPerIntfRxCrcErrCnt_Type()
)
mfrapPerfThruputPerIntfRxCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfRxCrcErrCnt.setStatus("mandatory")
_MfrapPerfThruputPerIntfRxAbortCnt_Type = Counter32
_MfrapPerfThruputPerIntfRxAbortCnt_Object = MibTableColumn
mfrapPerfThruputPerIntfRxAbortCnt = _MfrapPerfThruputPerIntfRxAbortCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 1, 1, 7),
    _MfrapPerfThruputPerIntfRxAbortCnt_Type()
)
mfrapPerfThruputPerIntfRxAbortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerIntfRxAbortCnt.setStatus("mandatory")
_MfrapPerfThruputPerDlciTable_Object = MibTable
mfrapPerfThruputPerDlciTable = _MfrapPerfThruputPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2)
)
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTable.setStatus("mandatory")
_MfrapPerfThruputPerDlciEntry_Object = MibTableRow
mfrapPerfThruputPerDlciEntry = _MfrapPerfThruputPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1)
)
mfrapPerfThruputPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfThruputPerDlciIndex"),
    (0, "MFRAP-MIB", "mfrapPerfThruputPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciEntry.setStatus("mandatory")
_MfrapPerfThruputPerDlciIndex_Type = Index
_MfrapPerfThruputPerDlciIndex_Object = MibTableColumn
mfrapPerfThruputPerDlciIndex = _MfrapPerfThruputPerDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 1),
    _MfrapPerfThruputPerDlciIndex_Type()
)
mfrapPerfThruputPerDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciIndex.setStatus("mandatory")
_MfrapPerfThruputPerDlciValue_Type = Integer32
_MfrapPerfThruputPerDlciValue_Object = MibTableColumn
mfrapPerfThruputPerDlciValue = _MfrapPerfThruputPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 2),
    _MfrapPerfThruputPerDlciValue_Type()
)
mfrapPerfThruputPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciValue.setStatus("mandatory")
_MfrapPerfThruputPerDlciCreateTime_Type = Integer32
_MfrapPerfThruputPerDlciCreateTime_Object = MibTableColumn
mfrapPerfThruputPerDlciCreateTime = _MfrapPerfThruputPerDlciCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 3),
    _MfrapPerfThruputPerDlciCreateTime_Type()
)
mfrapPerfThruputPerDlciCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciCreateTime.setStatus("mandatory")
_MfrapPerfThruputPerDlciChangeTime_Type = Integer32
_MfrapPerfThruputPerDlciChangeTime_Object = MibTableColumn
mfrapPerfThruputPerDlciChangeTime = _MfrapPerfThruputPerDlciChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 4),
    _MfrapPerfThruputPerDlciChangeTime_Type()
)
mfrapPerfThruputPerDlciChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciChangeTime.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxByte_Type = Counter32
_MfrapPerfThruputPerDlciRxByte_Object = MibTableColumn
mfrapPerfThruputPerDlciRxByte = _MfrapPerfThruputPerDlciRxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 5),
    _MfrapPerfThruputPerDlciRxByte_Type()
)
mfrapPerfThruputPerDlciRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxByte.setStatus("mandatory")
_MfrapPerfThruputPerDlciTxByte_Type = Counter32
_MfrapPerfThruputPerDlciTxByte_Object = MibTableColumn
mfrapPerfThruputPerDlciTxByte = _MfrapPerfThruputPerDlciTxByte_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 6),
    _MfrapPerfThruputPerDlciTxByte_Type()
)
mfrapPerfThruputPerDlciTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTxByte.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxFrame_Type = Counter32
_MfrapPerfThruputPerDlciRxFrame_Object = MibTableColumn
mfrapPerfThruputPerDlciRxFrame = _MfrapPerfThruputPerDlciRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 7),
    _MfrapPerfThruputPerDlciRxFrame_Type()
)
mfrapPerfThruputPerDlciRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxFrame.setStatus("mandatory")
_MfrapPerfThruputPerDlciTxFrame_Type = Counter32
_MfrapPerfThruputPerDlciTxFrame_Object = MibTableColumn
mfrapPerfThruputPerDlciTxFrame = _MfrapPerfThruputPerDlciTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 8),
    _MfrapPerfThruputPerDlciTxFrame_Type()
)
mfrapPerfThruputPerDlciTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTxFrame.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxFecn_Type = Counter32
_MfrapPerfThruputPerDlciRxFecn_Object = MibTableColumn
mfrapPerfThruputPerDlciRxFecn = _MfrapPerfThruputPerDlciRxFecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 9),
    _MfrapPerfThruputPerDlciRxFecn_Type()
)
mfrapPerfThruputPerDlciRxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxFecn.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxBecn_Type = Counter32
_MfrapPerfThruputPerDlciRxBecn_Object = MibTableColumn
mfrapPerfThruputPerDlciRxBecn = _MfrapPerfThruputPerDlciRxBecn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 10),
    _MfrapPerfThruputPerDlciRxBecn_Type()
)
mfrapPerfThruputPerDlciRxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxBecn.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxDe_Type = Counter32
_MfrapPerfThruputPerDlciRxDe_Object = MibTableColumn
mfrapPerfThruputPerDlciRxDe = _MfrapPerfThruputPerDlciRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 11),
    _MfrapPerfThruputPerDlciRxDe_Type()
)
mfrapPerfThruputPerDlciRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxDe.setStatus("mandatory")
_MfrapPerfThruputPerDlciTxDe_Type = Counter32
_MfrapPerfThruputPerDlciTxDe_Object = MibTableColumn
mfrapPerfThruputPerDlciTxDe = _MfrapPerfThruputPerDlciTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 12),
    _MfrapPerfThruputPerDlciTxDe_Type()
)
mfrapPerfThruputPerDlciTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTxDe.setStatus("mandatory")
_MfrapPerfThruputPerDlciRxThruput_Type = Integer32
_MfrapPerfThruputPerDlciRxThruput_Object = MibTableColumn
mfrapPerfThruputPerDlciRxThruput = _MfrapPerfThruputPerDlciRxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 13),
    _MfrapPerfThruputPerDlciRxThruput_Type()
)
mfrapPerfThruputPerDlciRxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxThruput.setStatus("mandatory")
_MfrapPerfThruputPerDlciTxThruput_Type = Integer32
_MfrapPerfThruputPerDlciTxThruput_Object = MibTableColumn
mfrapPerfThruputPerDlciTxThruput = _MfrapPerfThruputPerDlciTxThruput_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 14),
    _MfrapPerfThruputPerDlciTxThruput_Type()
)
mfrapPerfThruputPerDlciTxThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTxThruput.setStatus("mandatory")
_MfrapPerfThruputPerDlciCIR_Type = Integer32
_MfrapPerfThruputPerDlciCIR_Object = MibTableColumn
mfrapPerfThruputPerDlciCIR = _MfrapPerfThruputPerDlciCIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 15),
    _MfrapPerfThruputPerDlciCIR_Type()
)
mfrapPerfThruputPerDlciCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciCIR.setStatus("mandatory")
_MfrapPerfThruputPerDlciUptime_Type = Integer32
_MfrapPerfThruputPerDlciUptime_Object = MibTableColumn
mfrapPerfThruputPerDlciUptime = _MfrapPerfThruputPerDlciUptime_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 16),
    _MfrapPerfThruputPerDlciUptime_Type()
)
mfrapPerfThruputPerDlciUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciUptime.setStatus("mandatory")
_MfrapPerfThruputPerDlciDowntime_Type = Integer32
_MfrapPerfThruputPerDlciDowntime_Object = MibTableColumn
mfrapPerfThruputPerDlciDowntime = _MfrapPerfThruputPerDlciDowntime_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 17),
    _MfrapPerfThruputPerDlciDowntime_Type()
)
mfrapPerfThruputPerDlciDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciDowntime.setStatus("mandatory")


class _MfrapPerfThruputPerDlciCirType_Type(Integer32):
    """Custom type mfrapPerfThruputPerDlciCirType based on Integer32"""
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


_MfrapPerfThruputPerDlciCirType_Type.__name__ = "Integer32"
_MfrapPerfThruputPerDlciCirType_Object = MibTableColumn
mfrapPerfThruputPerDlciCirType = _MfrapPerfThruputPerDlciCirType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 18),
    _MfrapPerfThruputPerDlciCirType_Type()
)
mfrapPerfThruputPerDlciCirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciCirType.setStatus("mandatory")


class _MfrapPerfThruputPerDlciPvcState_Type(Integer32):
    """Custom type mfrapPerfThruputPerDlciPvcState based on Integer32"""
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


_MfrapPerfThruputPerDlciPvcState_Type.__name__ = "Integer32"
_MfrapPerfThruputPerDlciPvcState_Object = MibTableColumn
mfrapPerfThruputPerDlciPvcState = _MfrapPerfThruputPerDlciPvcState_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 19),
    _MfrapPerfThruputPerDlciPvcState_Type()
)
mfrapPerfThruputPerDlciPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciPvcState.setStatus("mandatory")
_MfrapPerfThruputPerDlciOutageCount_Type = Counter32
_MfrapPerfThruputPerDlciOutageCount_Object = MibTableColumn
mfrapPerfThruputPerDlciOutageCount = _MfrapPerfThruputPerDlciOutageCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 20),
    _MfrapPerfThruputPerDlciOutageCount_Type()
)
mfrapPerfThruputPerDlciOutageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciOutageCount.setStatus("mandatory")
_MfrapPerfThruputPerDlciAvailability_Type = Integer32
_MfrapPerfThruputPerDlciAvailability_Object = MibTableColumn
mfrapPerfThruputPerDlciAvailability = _MfrapPerfThruputPerDlciAvailability_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 21),
    _MfrapPerfThruputPerDlciAvailability_Type()
)
mfrapPerfThruputPerDlciAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciAvailability.setStatus("mandatory")
_MfrapPerfThruputPerDlciMTBSO_Type = Integer32
_MfrapPerfThruputPerDlciMTBSO_Object = MibTableColumn
mfrapPerfThruputPerDlciMTBSO = _MfrapPerfThruputPerDlciMTBSO_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 22),
    _MfrapPerfThruputPerDlciMTBSO_Type()
)
mfrapPerfThruputPerDlciMTBSO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciMTBSO.setStatus("mandatory")
_MfrapPerfThruputPerDlciMTTSR_Type = Integer32
_MfrapPerfThruputPerDlciMTTSR_Object = MibTableColumn
mfrapPerfThruputPerDlciMTTSR = _MfrapPerfThruputPerDlciMTTSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 23),
    _MfrapPerfThruputPerDlciMTTSR_Type()
)
mfrapPerfThruputPerDlciMTTSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciMTTSR.setStatus("mandatory")


class _MfrapPerfThruputPerDlciEncapType_Type(Integer32):
    """Custom type mfrapPerfThruputPerDlciEncapType based on Integer32"""
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


_MfrapPerfThruputPerDlciEncapType_Type.__name__ = "Integer32"
_MfrapPerfThruputPerDlciEncapType_Object = MibTableColumn
mfrapPerfThruputPerDlciEncapType = _MfrapPerfThruputPerDlciEncapType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 24),
    _MfrapPerfThruputPerDlciEncapType_Type()
)
mfrapPerfThruputPerDlciEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciEncapType.setStatus("mandatory")


class _MfrapPerfThruputPerDlciRxUtilizationStatus_Type(Integer32):
    """Custom type mfrapPerfThruputPerDlciRxUtilizationStatus based on Integer32"""
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


_MfrapPerfThruputPerDlciRxUtilizationStatus_Type.__name__ = "Integer32"
_MfrapPerfThruputPerDlciRxUtilizationStatus_Object = MibTableColumn
mfrapPerfThruputPerDlciRxUtilizationStatus = _MfrapPerfThruputPerDlciRxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 25),
    _MfrapPerfThruputPerDlciRxUtilizationStatus_Type()
)
mfrapPerfThruputPerDlciRxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciRxUtilizationStatus.setStatus("mandatory")


class _MfrapPerfThruputPerDlciTxUtilizationStatus_Type(Integer32):
    """Custom type mfrapPerfThruputPerDlciTxUtilizationStatus based on Integer32"""
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


_MfrapPerfThruputPerDlciTxUtilizationStatus_Type.__name__ = "Integer32"
_MfrapPerfThruputPerDlciTxUtilizationStatus_Object = MibTableColumn
mfrapPerfThruputPerDlciTxUtilizationStatus = _MfrapPerfThruputPerDlciTxUtilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 26),
    _MfrapPerfThruputPerDlciTxUtilizationStatus_Type()
)
mfrapPerfThruputPerDlciTxUtilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciTxUtilizationStatus.setStatus("mandatory")
_MfrapPerfThruputPerDlciEIR_Type = Integer32
_MfrapPerfThruputPerDlciEIR_Object = MibTableColumn
mfrapPerfThruputPerDlciEIR = _MfrapPerfThruputPerDlciEIR_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 2, 1, 27),
    _MfrapPerfThruputPerDlciEIR_Type()
)
mfrapPerfThruputPerDlciEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputPerDlciEIR.setStatus("mandatory")
_MfrapPerfThruputCommands_ObjectIdentity = ObjectIdentity
mfrapPerfThruputCommands = _MfrapPerfThruputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3)
)


class _MfrapPerfThruputCmdClearDteStats_Type(Integer32):
    """Custom type mfrapPerfThruputCmdClearDteStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfThruputCmdClearDteStats_Type.__name__ = "Integer32"
_MfrapPerfThruputCmdClearDteStats_Object = MibScalar
mfrapPerfThruputCmdClearDteStats = _MfrapPerfThruputCmdClearDteStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 1),
    _MfrapPerfThruputCmdClearDteStats_Type()
)
mfrapPerfThruputCmdClearDteStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdClearDteStats.setStatus("mandatory")


class _MfrapPerfThruputCmdClearT1Stats_Type(Integer32):
    """Custom type mfrapPerfThruputCmdClearT1Stats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfThruputCmdClearT1Stats_Type.__name__ = "Integer32"
_MfrapPerfThruputCmdClearT1Stats_Object = MibScalar
mfrapPerfThruputCmdClearT1Stats = _MfrapPerfThruputCmdClearT1Stats_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 2),
    _MfrapPerfThruputCmdClearT1Stats_Type()
)
mfrapPerfThruputCmdClearT1Stats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdClearT1Stats.setStatus("mandatory")


class _MfrapPerfThruputCmdClearAllIntfStats_Type(Integer32):
    """Custom type mfrapPerfThruputCmdClearAllIntfStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfThruputCmdClearAllIntfStats_Type.__name__ = "Integer32"
_MfrapPerfThruputCmdClearAllIntfStats_Object = MibScalar
mfrapPerfThruputCmdClearAllIntfStats = _MfrapPerfThruputCmdClearAllIntfStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 3),
    _MfrapPerfThruputCmdClearAllIntfStats_Type()
)
mfrapPerfThruputCmdClearAllIntfStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdClearAllIntfStats.setStatus("mandatory")


class _MfrapPerfThruputCmdClearDlciStats_Type(Integer32):
    """Custom type mfrapPerfThruputCmdClearDlciStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfThruputCmdClearDlciStats_Type.__name__ = "Integer32"
_MfrapPerfThruputCmdClearDlciStats_Object = MibScalar
mfrapPerfThruputCmdClearDlciStats = _MfrapPerfThruputCmdClearDlciStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 4),
    _MfrapPerfThruputCmdClearDlciStats_Type()
)
mfrapPerfThruputCmdClearDlciStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdClearDlciStats.setStatus("mandatory")


class _MfrapPerfThruputCmdClearAllStats_Type(Integer32):
    """Custom type mfrapPerfThruputCmdClearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfThruputCmdClearAllStats_Type.__name__ = "Integer32"
_MfrapPerfThruputCmdClearAllStats_Object = MibScalar
mfrapPerfThruputCmdClearAllStats = _MfrapPerfThruputCmdClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 5),
    _MfrapPerfThruputCmdClearAllStats_Type()
)
mfrapPerfThruputCmdClearAllStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdClearAllStats.setStatus("mandatory")
_MfrapPerfThruputCmdRemoveStsDlci_Type = Integer32
_MfrapPerfThruputCmdRemoveStsDlci_Object = MibScalar
mfrapPerfThruputCmdRemoveStsDlci = _MfrapPerfThruputCmdRemoveStsDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 6),
    _MfrapPerfThruputCmdRemoveStsDlci_Type()
)
mfrapPerfThruputCmdRemoveStsDlci.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdRemoveStsDlci.setStatus("mandatory")
_MfrapPerfThruputCmdReplaceDlciTable_Object = MibTable
mfrapPerfThruputCmdReplaceDlciTable = _MfrapPerfThruputCmdReplaceDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 7)
)
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdReplaceDlciTable.setStatus("mandatory")
_MfrapPerfThruputCmdReplaceDlciEntry_Object = MibTableRow
mfrapPerfThruputCmdReplaceDlciEntry = _MfrapPerfThruputCmdReplaceDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 7, 1)
)
mfrapPerfThruputCmdReplaceDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfThruputCmdReplaceDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdReplaceDlciEntry.setStatus("mandatory")
_MfrapPerfThruputCmdReplaceDlciValue_Type = Integer32
_MfrapPerfThruputCmdReplaceDlciValue_Object = MibTableColumn
mfrapPerfThruputCmdReplaceDlciValue = _MfrapPerfThruputCmdReplaceDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 7, 1, 1),
    _MfrapPerfThruputCmdReplaceDlciValue_Type()
)
mfrapPerfThruputCmdReplaceDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdReplaceDlciValue.setStatus("mandatory")
_MfrapPerfThruputCmdReplaceDlciNewValue_Type = Integer32
_MfrapPerfThruputCmdReplaceDlciNewValue_Object = MibTableColumn
mfrapPerfThruputCmdReplaceDlciNewValue = _MfrapPerfThruputCmdReplaceDlciNewValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 7, 1, 2),
    _MfrapPerfThruputCmdReplaceDlciNewValue_Type()
)
mfrapPerfThruputCmdReplaceDlciNewValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdReplaceDlciNewValue.setStatus("mandatory")
_MfrapPerfThruputCmdAvailabilityStsDlciReset_Type = Integer32
_MfrapPerfThruputCmdAvailabilityStsDlciReset_Object = MibScalar
mfrapPerfThruputCmdAvailabilityStsDlciReset = _MfrapPerfThruputCmdAvailabilityStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 8),
    _MfrapPerfThruputCmdAvailabilityStsDlciReset_Type()
)
mfrapPerfThruputCmdAvailabilityStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdAvailabilityStsDlciReset.setStatus("mandatory")
_MfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type = Integer32
_MfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object = MibScalar
mfrapPerfThruputCmdAvailabilityStsDlciResetAll = _MfrapPerfThruputCmdAvailabilityStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 9),
    _MfrapPerfThruputCmdAvailabilityStsDlciResetAll_Type()
)
mfrapPerfThruputCmdAvailabilityStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdAvailabilityStsDlciResetAll.setStatus("mandatory")
_MfrapPerfThruputCmdCountsStsDlciReset_Type = Integer32
_MfrapPerfThruputCmdCountsStsDlciReset_Object = MibScalar
mfrapPerfThruputCmdCountsStsDlciReset = _MfrapPerfThruputCmdCountsStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 10),
    _MfrapPerfThruputCmdCountsStsDlciReset_Type()
)
mfrapPerfThruputCmdCountsStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdCountsStsDlciReset.setStatus("mandatory")
_MfrapPerfThruputCmdCountsStsDlciResetAll_Type = Integer32
_MfrapPerfThruputCmdCountsStsDlciResetAll_Object = MibScalar
mfrapPerfThruputCmdCountsStsDlciResetAll = _MfrapPerfThruputCmdCountsStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 11),
    _MfrapPerfThruputCmdCountsStsDlciResetAll_Type()
)
mfrapPerfThruputCmdCountsStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdCountsStsDlciResetAll.setStatus("mandatory")
_MfrapPerfThruputCmdAllStsDlciReset_Type = Integer32
_MfrapPerfThruputCmdAllStsDlciReset_Object = MibScalar
mfrapPerfThruputCmdAllStsDlciReset = _MfrapPerfThruputCmdAllStsDlciReset_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 12),
    _MfrapPerfThruputCmdAllStsDlciReset_Type()
)
mfrapPerfThruputCmdAllStsDlciReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdAllStsDlciReset.setStatus("mandatory")
_MfrapPerfThruputCmdAllStsDlciResetAll_Type = Integer32
_MfrapPerfThruputCmdAllStsDlciResetAll_Object = MibScalar
mfrapPerfThruputCmdAllStsDlciResetAll = _MfrapPerfThruputCmdAllStsDlciResetAll_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 3, 3, 13),
    _MfrapPerfThruputCmdAllStsDlciResetAll_Type()
)
mfrapPerfThruputCmdAllStsDlciResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfThruputCmdAllStsDlciResetAll.setStatus("mandatory")
_MfrapPerfNetworkShortTerm_ObjectIdentity = ObjectIdentity
mfrapPerfNetworkShortTerm = _MfrapPerfNetworkShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4)
)
_MfrapPerfNetwProtoPerDlciTable_Object = MibTable
mfrapPerfNetwProtoPerDlciTable = _MfrapPerfNetwProtoPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTable.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciEntry_Object = MibTableRow
mfrapPerfNetwProtoPerDlciEntry = _MfrapPerfNetwProtoPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1)
)
mfrapPerfNetwProtoPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfNetwProtoPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfNetwProtoPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciEntry.setStatus("mandatory")


class _MfrapPerfNetwProtoPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfNetwProtoPerDlciInterval based on Integer32"""
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


_MfrapPerfNetwProtoPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfNetwProtoPerDlciInterval_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciInterval = _MfrapPerfNetwProtoPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 1),
    _MfrapPerfNetwProtoPerDlciInterval_Type()
)
mfrapPerfNetwProtoPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciInterval.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciValue_Type = Integer32
_MfrapPerfNetwProtoPerDlciValue_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciValue = _MfrapPerfNetwProtoPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 2),
    _MfrapPerfNetwProtoPerDlciValue_Type()
)
mfrapPerfNetwProtoPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciValue.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxTotal_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxTotal_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxTotal = _MfrapPerfNetwProtoPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 3),
    _MfrapPerfNetwProtoPerDlciRxTotal_Type()
)
mfrapPerfNetwProtoPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxTotal_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxTotal_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxTotal = _MfrapPerfNetwProtoPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 4),
    _MfrapPerfNetwProtoPerDlciTxTotal_Type()
)
mfrapPerfNetwProtoPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxIp_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxIp_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxIp = _MfrapPerfNetwProtoPerDlciRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 5),
    _MfrapPerfNetwProtoPerDlciRxIp_Type()
)
mfrapPerfNetwProtoPerDlciRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxIp.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxIp_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxIp_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxIp = _MfrapPerfNetwProtoPerDlciTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 6),
    _MfrapPerfNetwProtoPerDlciTxIp_Type()
)
mfrapPerfNetwProtoPerDlciTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxIp.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxIpx_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxIpx_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxIpx = _MfrapPerfNetwProtoPerDlciRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 7),
    _MfrapPerfNetwProtoPerDlciRxIpx_Type()
)
mfrapPerfNetwProtoPerDlciRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxIpx.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxIpx_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxIpx_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxIpx = _MfrapPerfNetwProtoPerDlciTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 8),
    _MfrapPerfNetwProtoPerDlciTxIpx_Type()
)
mfrapPerfNetwProtoPerDlciTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxIpx.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxSna_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxSna_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxSna = _MfrapPerfNetwProtoPerDlciRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 9),
    _MfrapPerfNetwProtoPerDlciRxSna_Type()
)
mfrapPerfNetwProtoPerDlciRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxSna.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxSna_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxSna_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxSna = _MfrapPerfNetwProtoPerDlciTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 10),
    _MfrapPerfNetwProtoPerDlciTxSna_Type()
)
mfrapPerfNetwProtoPerDlciTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxSna.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxArp_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxArp_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxArp = _MfrapPerfNetwProtoPerDlciRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 11),
    _MfrapPerfNetwProtoPerDlciRxArp_Type()
)
mfrapPerfNetwProtoPerDlciRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxArp.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxArp_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxArp_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxArp = _MfrapPerfNetwProtoPerDlciTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 12),
    _MfrapPerfNetwProtoPerDlciTxArp_Type()
)
mfrapPerfNetwProtoPerDlciTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxArp.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxCisco_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxCisco_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxCisco = _MfrapPerfNetwProtoPerDlciRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 13),
    _MfrapPerfNetwProtoPerDlciRxCisco_Type()
)
mfrapPerfNetwProtoPerDlciRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxCisco.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxCisco_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxCisco_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxCisco = _MfrapPerfNetwProtoPerDlciTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 14),
    _MfrapPerfNetwProtoPerDlciTxCisco_Type()
)
mfrapPerfNetwProtoPerDlciTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxCisco.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxOther_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxOther_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxOther = _MfrapPerfNetwProtoPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 15),
    _MfrapPerfNetwProtoPerDlciRxOther_Type()
)
mfrapPerfNetwProtoPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxOther.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxOther_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxOther_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxOther = _MfrapPerfNetwProtoPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 16),
    _MfrapPerfNetwProtoPerDlciTxOther_Type()
)
mfrapPerfNetwProtoPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxOther.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxVnip_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxVnip_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxVnip = _MfrapPerfNetwProtoPerDlciRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 17),
    _MfrapPerfNetwProtoPerDlciRxVnip_Type()
)
mfrapPerfNetwProtoPerDlciRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxVnip.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxVnip_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxVnip_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxVnip = _MfrapPerfNetwProtoPerDlciTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 18),
    _MfrapPerfNetwProtoPerDlciTxVnip_Type()
)
mfrapPerfNetwProtoPerDlciTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxVnip.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciRxAnnexG_Type = Counter32
_MfrapPerfNetwProtoPerDlciRxAnnexG_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciRxAnnexG = _MfrapPerfNetwProtoPerDlciRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 19),
    _MfrapPerfNetwProtoPerDlciRxAnnexG_Type()
)
mfrapPerfNetwProtoPerDlciRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciRxAnnexG.setStatus("mandatory")
_MfrapPerfNetwProtoPerDlciTxAnnexG_Type = Counter32
_MfrapPerfNetwProtoPerDlciTxAnnexG_Object = MibTableColumn
mfrapPerfNetwProtoPerDlciTxAnnexG = _MfrapPerfNetwProtoPerDlciTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 1, 1, 20),
    _MfrapPerfNetwProtoPerDlciTxAnnexG_Type()
)
mfrapPerfNetwProtoPerDlciTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoPerDlciTxAnnexG.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTable_Object = MibTable
mfrapPerfNetwProtoTotalTable = _MfrapPerfNetwProtoTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2)
)
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTable.setStatus("mandatory")
_MfrapPerfNetwProtoTotalEntry_Object = MibTableRow
mfrapPerfNetwProtoTotalEntry = _MfrapPerfNetwProtoTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1)
)
mfrapPerfNetwProtoTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfNetwProtoTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalEntry.setStatus("mandatory")


class _MfrapPerfNetwProtoTotalInterval_Type(Integer32):
    """Custom type mfrapPerfNetwProtoTotalInterval based on Integer32"""
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


_MfrapPerfNetwProtoTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfNetwProtoTotalInterval_Object = MibTableColumn
mfrapPerfNetwProtoTotalInterval = _MfrapPerfNetwProtoTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 1),
    _MfrapPerfNetwProtoTotalInterval_Type()
)
mfrapPerfNetwProtoTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalInterval.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxTotal_Type = Counter32
_MfrapPerfNetwProtoTotalRxTotal_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxTotal = _MfrapPerfNetwProtoTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 3),
    _MfrapPerfNetwProtoTotalRxTotal_Type()
)
mfrapPerfNetwProtoTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxTotal.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxTotal_Type = Counter32
_MfrapPerfNetwProtoTotalTxTotal_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxTotal = _MfrapPerfNetwProtoTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 4),
    _MfrapPerfNetwProtoTotalTxTotal_Type()
)
mfrapPerfNetwProtoTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxTotal.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxIp_Type = Counter32
_MfrapPerfNetwProtoTotalRxIp_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxIp = _MfrapPerfNetwProtoTotalRxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 5),
    _MfrapPerfNetwProtoTotalRxIp_Type()
)
mfrapPerfNetwProtoTotalRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxIp.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxIp_Type = Counter32
_MfrapPerfNetwProtoTotalTxIp_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxIp = _MfrapPerfNetwProtoTotalTxIp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 6),
    _MfrapPerfNetwProtoTotalTxIp_Type()
)
mfrapPerfNetwProtoTotalTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxIp.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxIpx_Type = Counter32
_MfrapPerfNetwProtoTotalRxIpx_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxIpx = _MfrapPerfNetwProtoTotalRxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 7),
    _MfrapPerfNetwProtoTotalRxIpx_Type()
)
mfrapPerfNetwProtoTotalRxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxIpx.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxIpx_Type = Counter32
_MfrapPerfNetwProtoTotalTxIpx_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxIpx = _MfrapPerfNetwProtoTotalTxIpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 8),
    _MfrapPerfNetwProtoTotalTxIpx_Type()
)
mfrapPerfNetwProtoTotalTxIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxIpx.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxSna_Type = Counter32
_MfrapPerfNetwProtoTotalRxSna_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxSna = _MfrapPerfNetwProtoTotalRxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 9),
    _MfrapPerfNetwProtoTotalRxSna_Type()
)
mfrapPerfNetwProtoTotalRxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxSna.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxSna_Type = Counter32
_MfrapPerfNetwProtoTotalTxSna_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxSna = _MfrapPerfNetwProtoTotalTxSna_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 10),
    _MfrapPerfNetwProtoTotalTxSna_Type()
)
mfrapPerfNetwProtoTotalTxSna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxSna.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxArp_Type = Counter32
_MfrapPerfNetwProtoTotalRxArp_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxArp = _MfrapPerfNetwProtoTotalRxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 11),
    _MfrapPerfNetwProtoTotalRxArp_Type()
)
mfrapPerfNetwProtoTotalRxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxArp.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxArp_Type = Counter32
_MfrapPerfNetwProtoTotalTxArp_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxArp = _MfrapPerfNetwProtoTotalTxArp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 12),
    _MfrapPerfNetwProtoTotalTxArp_Type()
)
mfrapPerfNetwProtoTotalTxArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxArp.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxCisco_Type = Counter32
_MfrapPerfNetwProtoTotalRxCisco_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxCisco = _MfrapPerfNetwProtoTotalRxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 13),
    _MfrapPerfNetwProtoTotalRxCisco_Type()
)
mfrapPerfNetwProtoTotalRxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxCisco.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxCisco_Type = Counter32
_MfrapPerfNetwProtoTotalTxCisco_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxCisco = _MfrapPerfNetwProtoTotalTxCisco_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 14),
    _MfrapPerfNetwProtoTotalTxCisco_Type()
)
mfrapPerfNetwProtoTotalTxCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxCisco.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxOther_Type = Counter32
_MfrapPerfNetwProtoTotalRxOther_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxOther = _MfrapPerfNetwProtoTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 15),
    _MfrapPerfNetwProtoTotalRxOther_Type()
)
mfrapPerfNetwProtoTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxOther.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxOther_Type = Counter32
_MfrapPerfNetwProtoTotalTxOther_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxOther = _MfrapPerfNetwProtoTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 16),
    _MfrapPerfNetwProtoTotalTxOther_Type()
)
mfrapPerfNetwProtoTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxOther.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxVnip_Type = Counter32
_MfrapPerfNetwProtoTotalRxVnip_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxVnip = _MfrapPerfNetwProtoTotalRxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 17),
    _MfrapPerfNetwProtoTotalRxVnip_Type()
)
mfrapPerfNetwProtoTotalRxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxVnip.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxVnip_Type = Counter32
_MfrapPerfNetwProtoTotalTxVnip_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxVnip = _MfrapPerfNetwProtoTotalTxVnip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 18),
    _MfrapPerfNetwProtoTotalTxVnip_Type()
)
mfrapPerfNetwProtoTotalTxVnip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxVnip.setStatus("mandatory")
_MfrapPerfNetwProtoTotalRxAnnexG_Type = Counter32
_MfrapPerfNetwProtoTotalRxAnnexG_Object = MibTableColumn
mfrapPerfNetwProtoTotalRxAnnexG = _MfrapPerfNetwProtoTotalRxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 19),
    _MfrapPerfNetwProtoTotalRxAnnexG_Type()
)
mfrapPerfNetwProtoTotalRxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalRxAnnexG.setStatus("mandatory")
_MfrapPerfNetwProtoTotalTxAnnexG_Type = Counter32
_MfrapPerfNetwProtoTotalTxAnnexG_Object = MibTableColumn
mfrapPerfNetwProtoTotalTxAnnexG = _MfrapPerfNetwProtoTotalTxAnnexG_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 2, 1, 20),
    _MfrapPerfNetwProtoTotalTxAnnexG_Type()
)
mfrapPerfNetwProtoTotalTxAnnexG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwProtoTotalTxAnnexG.setStatus("mandatory")
_MfrapPerfIpPerDlciTable_Object = MibTable
mfrapPerfIpPerDlciTable = _MfrapPerfIpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3)
)
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTable.setStatus("mandatory")
_MfrapPerfIpPerDlciEntry_Object = MibTableRow
mfrapPerfIpPerDlciEntry = _MfrapPerfIpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1)
)
mfrapPerfIpPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIpPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfIpPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciEntry.setStatus("mandatory")


class _MfrapPerfIpPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfIpPerDlciInterval based on Integer32"""
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


_MfrapPerfIpPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfIpPerDlciInterval_Object = MibTableColumn
mfrapPerfIpPerDlciInterval = _MfrapPerfIpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 1),
    _MfrapPerfIpPerDlciInterval_Type()
)
mfrapPerfIpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciInterval.setStatus("mandatory")
_MfrapPerfIpPerDlciValue_Type = Integer32
_MfrapPerfIpPerDlciValue_Object = MibTableColumn
mfrapPerfIpPerDlciValue = _MfrapPerfIpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 2),
    _MfrapPerfIpPerDlciValue_Type()
)
mfrapPerfIpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciValue.setStatus("mandatory")
_MfrapPerfIpPerDlciRxTotal_Type = Counter32
_MfrapPerfIpPerDlciRxTotal_Object = MibTableColumn
mfrapPerfIpPerDlciRxTotal = _MfrapPerfIpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 3),
    _MfrapPerfIpPerDlciRxTotal_Type()
)
mfrapPerfIpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfIpPerDlciTxTotal_Type = Counter32
_MfrapPerfIpPerDlciTxTotal_Object = MibTableColumn
mfrapPerfIpPerDlciTxTotal = _MfrapPerfIpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 4),
    _MfrapPerfIpPerDlciTxTotal_Type()
)
mfrapPerfIpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfIpPerDlciRxTcp_Type = Counter32
_MfrapPerfIpPerDlciRxTcp_Object = MibTableColumn
mfrapPerfIpPerDlciRxTcp = _MfrapPerfIpPerDlciRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 5),
    _MfrapPerfIpPerDlciRxTcp_Type()
)
mfrapPerfIpPerDlciRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxTcp.setStatus("mandatory")
_MfrapPerfIpPerDlciTxTcp_Type = Counter32
_MfrapPerfIpPerDlciTxTcp_Object = MibTableColumn
mfrapPerfIpPerDlciTxTcp = _MfrapPerfIpPerDlciTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 6),
    _MfrapPerfIpPerDlciTxTcp_Type()
)
mfrapPerfIpPerDlciTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxTcp.setStatus("mandatory")
_MfrapPerfIpPerDlciRxUdp_Type = Counter32
_MfrapPerfIpPerDlciRxUdp_Object = MibTableColumn
mfrapPerfIpPerDlciRxUdp = _MfrapPerfIpPerDlciRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 7),
    _MfrapPerfIpPerDlciRxUdp_Type()
)
mfrapPerfIpPerDlciRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxUdp.setStatus("mandatory")
_MfrapPerfIpPerDlciTxUdp_Type = Counter32
_MfrapPerfIpPerDlciTxUdp_Object = MibTableColumn
mfrapPerfIpPerDlciTxUdp = _MfrapPerfIpPerDlciTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 8),
    _MfrapPerfIpPerDlciTxUdp_Type()
)
mfrapPerfIpPerDlciTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxUdp.setStatus("mandatory")
_MfrapPerfIpPerDlciRxIcmp_Type = Counter32
_MfrapPerfIpPerDlciRxIcmp_Object = MibTableColumn
mfrapPerfIpPerDlciRxIcmp = _MfrapPerfIpPerDlciRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 9),
    _MfrapPerfIpPerDlciRxIcmp_Type()
)
mfrapPerfIpPerDlciRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxIcmp.setStatus("mandatory")
_MfrapPerfIpPerDlciTxIcmp_Type = Counter32
_MfrapPerfIpPerDlciTxIcmp_Object = MibTableColumn
mfrapPerfIpPerDlciTxIcmp = _MfrapPerfIpPerDlciTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 10),
    _MfrapPerfIpPerDlciTxIcmp_Type()
)
mfrapPerfIpPerDlciTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxIcmp.setStatus("mandatory")
_MfrapPerfIpPerDlciRxOther_Type = Counter32
_MfrapPerfIpPerDlciRxOther_Object = MibTableColumn
mfrapPerfIpPerDlciRxOther = _MfrapPerfIpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 11),
    _MfrapPerfIpPerDlciRxOther_Type()
)
mfrapPerfIpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxOther.setStatus("mandatory")
_MfrapPerfIpPerDlciTxOther_Type = Counter32
_MfrapPerfIpPerDlciTxOther_Object = MibTableColumn
mfrapPerfIpPerDlciTxOther = _MfrapPerfIpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 12),
    _MfrapPerfIpPerDlciTxOther_Type()
)
mfrapPerfIpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxOther.setStatus("mandatory")
_MfrapPerfIpPerDlciRxIgrp_Type = Counter32
_MfrapPerfIpPerDlciRxIgrp_Object = MibTableColumn
mfrapPerfIpPerDlciRxIgrp = _MfrapPerfIpPerDlciRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 13),
    _MfrapPerfIpPerDlciRxIgrp_Type()
)
mfrapPerfIpPerDlciRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciRxIgrp.setStatus("mandatory")
_MfrapPerfIpPerDlciTxIgrp_Type = Counter32
_MfrapPerfIpPerDlciTxIgrp_Object = MibTableColumn
mfrapPerfIpPerDlciTxIgrp = _MfrapPerfIpPerDlciTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 3, 1, 14),
    _MfrapPerfIpPerDlciTxIgrp_Type()
)
mfrapPerfIpPerDlciTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpPerDlciTxIgrp.setStatus("mandatory")
_MfrapPerfIpTotalTable_Object = MibTable
mfrapPerfIpTotalTable = _MfrapPerfIpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4)
)
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTable.setStatus("mandatory")
_MfrapPerfIpTotalEntry_Object = MibTableRow
mfrapPerfIpTotalEntry = _MfrapPerfIpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1)
)
mfrapPerfIpTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIpTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfIpTotalEntry.setStatus("mandatory")


class _MfrapPerfIpTotalInterval_Type(Integer32):
    """Custom type mfrapPerfIpTotalInterval based on Integer32"""
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


_MfrapPerfIpTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfIpTotalInterval_Object = MibTableColumn
mfrapPerfIpTotalInterval = _MfrapPerfIpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 1),
    _MfrapPerfIpTotalInterval_Type()
)
mfrapPerfIpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalInterval.setStatus("mandatory")
_MfrapPerfIpTotalRxTotal_Type = Counter32
_MfrapPerfIpTotalRxTotal_Object = MibTableColumn
mfrapPerfIpTotalRxTotal = _MfrapPerfIpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 3),
    _MfrapPerfIpTotalRxTotal_Type()
)
mfrapPerfIpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxTotal.setStatus("mandatory")
_MfrapPerfIpTotalTxTotal_Type = Counter32
_MfrapPerfIpTotalTxTotal_Object = MibTableColumn
mfrapPerfIpTotalTxTotal = _MfrapPerfIpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 4),
    _MfrapPerfIpTotalTxTotal_Type()
)
mfrapPerfIpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxTotal.setStatus("mandatory")
_MfrapPerfIpTotalRxTcp_Type = Counter32
_MfrapPerfIpTotalRxTcp_Object = MibTableColumn
mfrapPerfIpTotalRxTcp = _MfrapPerfIpTotalRxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 5),
    _MfrapPerfIpTotalRxTcp_Type()
)
mfrapPerfIpTotalRxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxTcp.setStatus("mandatory")
_MfrapPerfIpTotalTxTcp_Type = Counter32
_MfrapPerfIpTotalTxTcp_Object = MibTableColumn
mfrapPerfIpTotalTxTcp = _MfrapPerfIpTotalTxTcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 6),
    _MfrapPerfIpTotalTxTcp_Type()
)
mfrapPerfIpTotalTxTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxTcp.setStatus("mandatory")
_MfrapPerfIpTotalRxUdp_Type = Counter32
_MfrapPerfIpTotalRxUdp_Object = MibTableColumn
mfrapPerfIpTotalRxUdp = _MfrapPerfIpTotalRxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 7),
    _MfrapPerfIpTotalRxUdp_Type()
)
mfrapPerfIpTotalRxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxUdp.setStatus("mandatory")
_MfrapPerfIpTotalTxUdp_Type = Counter32
_MfrapPerfIpTotalTxUdp_Object = MibTableColumn
mfrapPerfIpTotalTxUdp = _MfrapPerfIpTotalTxUdp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 8),
    _MfrapPerfIpTotalTxUdp_Type()
)
mfrapPerfIpTotalTxUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxUdp.setStatus("mandatory")
_MfrapPerfIpTotalRxIcmp_Type = Counter32
_MfrapPerfIpTotalRxIcmp_Object = MibTableColumn
mfrapPerfIpTotalRxIcmp = _MfrapPerfIpTotalRxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 9),
    _MfrapPerfIpTotalRxIcmp_Type()
)
mfrapPerfIpTotalRxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxIcmp.setStatus("mandatory")
_MfrapPerfIpTotalTxIcmp_Type = Counter32
_MfrapPerfIpTotalTxIcmp_Object = MibTableColumn
mfrapPerfIpTotalTxIcmp = _MfrapPerfIpTotalTxIcmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 10),
    _MfrapPerfIpTotalTxIcmp_Type()
)
mfrapPerfIpTotalTxIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxIcmp.setStatus("mandatory")
_MfrapPerfIpTotalRxOther_Type = Counter32
_MfrapPerfIpTotalRxOther_Object = MibTableColumn
mfrapPerfIpTotalRxOther = _MfrapPerfIpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 11),
    _MfrapPerfIpTotalRxOther_Type()
)
mfrapPerfIpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxOther.setStatus("mandatory")
_MfrapPerfIpTotalTxOther_Type = Counter32
_MfrapPerfIpTotalTxOther_Object = MibTableColumn
mfrapPerfIpTotalTxOther = _MfrapPerfIpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 12),
    _MfrapPerfIpTotalTxOther_Type()
)
mfrapPerfIpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxOther.setStatus("mandatory")
_MfrapPerfIpTotalRxIgrp_Type = Counter32
_MfrapPerfIpTotalRxIgrp_Object = MibTableColumn
mfrapPerfIpTotalRxIgrp = _MfrapPerfIpTotalRxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 13),
    _MfrapPerfIpTotalRxIgrp_Type()
)
mfrapPerfIpTotalRxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalRxIgrp.setStatus("mandatory")
_MfrapPerfIpTotalTxIgrp_Type = Counter32
_MfrapPerfIpTotalTxIgrp_Object = MibTableColumn
mfrapPerfIpTotalTxIgrp = _MfrapPerfIpTotalTxIgrp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 4, 1, 14),
    _MfrapPerfIpTotalTxIgrp_Type()
)
mfrapPerfIpTotalTxIgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpTotalTxIgrp.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTable_Object = MibTable
mfrapPerfIcmpPerDlciTable = _MfrapPerfIcmpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5)
)
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTable.setStatus("mandatory")
_MfrapPerfIcmpPerDlciEntry_Object = MibTableRow
mfrapPerfIcmpPerDlciEntry = _MfrapPerfIcmpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1)
)
mfrapPerfIcmpPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIcmpPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfIcmpPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciEntry.setStatus("mandatory")


class _MfrapPerfIcmpPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfIcmpPerDlciInterval based on Integer32"""
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


_MfrapPerfIcmpPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfIcmpPerDlciInterval_Object = MibTableColumn
mfrapPerfIcmpPerDlciInterval = _MfrapPerfIcmpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 1),
    _MfrapPerfIcmpPerDlciInterval_Type()
)
mfrapPerfIcmpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciInterval.setStatus("mandatory")
_MfrapPerfIcmpPerDlciValue_Type = Integer32
_MfrapPerfIcmpPerDlciValue_Object = MibTableColumn
mfrapPerfIcmpPerDlciValue = _MfrapPerfIcmpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 2),
    _MfrapPerfIcmpPerDlciValue_Type()
)
mfrapPerfIcmpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciValue.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxTotal_Type = Counter32
_MfrapPerfIcmpPerDlciRxTotal_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxTotal = _MfrapPerfIcmpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 3),
    _MfrapPerfIcmpPerDlciRxTotal_Type()
)
mfrapPerfIcmpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxTotal_Type = Counter32
_MfrapPerfIcmpPerDlciTxTotal_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxTotal = _MfrapPerfIcmpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 4),
    _MfrapPerfIcmpPerDlciTxTotal_Type()
)
mfrapPerfIcmpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxEchoRep_Type = Counter32
_MfrapPerfIcmpPerDlciRxEchoRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxEchoRep = _MfrapPerfIcmpPerDlciRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 5),
    _MfrapPerfIcmpPerDlciRxEchoRep_Type()
)
mfrapPerfIcmpPerDlciRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxEchoRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxEchoRep_Type = Counter32
_MfrapPerfIcmpPerDlciTxEchoRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxEchoRep = _MfrapPerfIcmpPerDlciTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 6),
    _MfrapPerfIcmpPerDlciTxEchoRep_Type()
)
mfrapPerfIcmpPerDlciTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxEchoRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxDestUnr_Type = Counter32
_MfrapPerfIcmpPerDlciRxDestUnr_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxDestUnr = _MfrapPerfIcmpPerDlciRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 7),
    _MfrapPerfIcmpPerDlciRxDestUnr_Type()
)
mfrapPerfIcmpPerDlciRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxDestUnr.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxDestUnr_Type = Counter32
_MfrapPerfIcmpPerDlciTxDestUnr_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxDestUnr = _MfrapPerfIcmpPerDlciTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 8),
    _MfrapPerfIcmpPerDlciTxDestUnr_Type()
)
mfrapPerfIcmpPerDlciTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxDestUnr.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxSrcQuench_Type = Counter32
_MfrapPerfIcmpPerDlciRxSrcQuench_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxSrcQuench = _MfrapPerfIcmpPerDlciRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 9),
    _MfrapPerfIcmpPerDlciRxSrcQuench_Type()
)
mfrapPerfIcmpPerDlciRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxSrcQuench.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxSrcQuench_Type = Counter32
_MfrapPerfIcmpPerDlciTxSrcQuench_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxSrcQuench = _MfrapPerfIcmpPerDlciTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 10),
    _MfrapPerfIcmpPerDlciTxSrcQuench_Type()
)
mfrapPerfIcmpPerDlciTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxSrcQuench.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxRedirect_Type = Counter32
_MfrapPerfIcmpPerDlciRxRedirect_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxRedirect = _MfrapPerfIcmpPerDlciRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 11),
    _MfrapPerfIcmpPerDlciRxRedirect_Type()
)
mfrapPerfIcmpPerDlciRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxRedirect.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxRedirect_Type = Counter32
_MfrapPerfIcmpPerDlciTxRedirect_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxRedirect = _MfrapPerfIcmpPerDlciTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 12),
    _MfrapPerfIcmpPerDlciTxRedirect_Type()
)
mfrapPerfIcmpPerDlciTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxRedirect.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxEchoReq_Type = Counter32
_MfrapPerfIcmpPerDlciRxEchoReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxEchoReq = _MfrapPerfIcmpPerDlciRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 13),
    _MfrapPerfIcmpPerDlciRxEchoReq_Type()
)
mfrapPerfIcmpPerDlciRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxEchoReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxEchoReq_Type = Counter32
_MfrapPerfIcmpPerDlciTxEchoReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxEchoReq = _MfrapPerfIcmpPerDlciTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 14),
    _MfrapPerfIcmpPerDlciTxEchoReq_Type()
)
mfrapPerfIcmpPerDlciTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxEchoReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxTimeExcd_Type = Counter32
_MfrapPerfIcmpPerDlciRxTimeExcd_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxTimeExcd = _MfrapPerfIcmpPerDlciRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 15),
    _MfrapPerfIcmpPerDlciRxTimeExcd_Type()
)
mfrapPerfIcmpPerDlciRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxTimeExcd.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxTimeExcd_Type = Counter32
_MfrapPerfIcmpPerDlciTxTimeExcd_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxTimeExcd = _MfrapPerfIcmpPerDlciTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 16),
    _MfrapPerfIcmpPerDlciTxTimeExcd_Type()
)
mfrapPerfIcmpPerDlciTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxTimeExcd.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxParamProb_Type = Counter32
_MfrapPerfIcmpPerDlciRxParamProb_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxParamProb = _MfrapPerfIcmpPerDlciRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 17),
    _MfrapPerfIcmpPerDlciRxParamProb_Type()
)
mfrapPerfIcmpPerDlciRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxParamProb.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxParamProb_Type = Counter32
_MfrapPerfIcmpPerDlciTxParamProb_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxParamProb = _MfrapPerfIcmpPerDlciTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 18),
    _MfrapPerfIcmpPerDlciTxParamProb_Type()
)
mfrapPerfIcmpPerDlciTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxParamProb.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxTimestpReq_Type = Counter32
_MfrapPerfIcmpPerDlciRxTimestpReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxTimestpReq = _MfrapPerfIcmpPerDlciRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 19),
    _MfrapPerfIcmpPerDlciRxTimestpReq_Type()
)
mfrapPerfIcmpPerDlciRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxTimestpReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxTimestpReq_Type = Counter32
_MfrapPerfIcmpPerDlciTxTimestpReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxTimestpReq = _MfrapPerfIcmpPerDlciTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 20),
    _MfrapPerfIcmpPerDlciTxTimestpReq_Type()
)
mfrapPerfIcmpPerDlciTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxTimestpReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxTimestpRep_Type = Counter32
_MfrapPerfIcmpPerDlciRxTimestpRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxTimestpRep = _MfrapPerfIcmpPerDlciRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 21),
    _MfrapPerfIcmpPerDlciRxTimestpRep_Type()
)
mfrapPerfIcmpPerDlciRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxTimestpRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxTimestpRep_Type = Counter32
_MfrapPerfIcmpPerDlciTxTimestpRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxTimestpRep = _MfrapPerfIcmpPerDlciTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 22),
    _MfrapPerfIcmpPerDlciTxTimestpRep_Type()
)
mfrapPerfIcmpPerDlciTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxTimestpRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxAddrMaskReq_Type = Counter32
_MfrapPerfIcmpPerDlciRxAddrMaskReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxAddrMaskReq = _MfrapPerfIcmpPerDlciRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 23),
    _MfrapPerfIcmpPerDlciRxAddrMaskReq_Type()
)
mfrapPerfIcmpPerDlciRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxAddrMaskReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxAddrMaskReq_Type = Counter32
_MfrapPerfIcmpPerDlciTxAddrMaskReq_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxAddrMaskReq = _MfrapPerfIcmpPerDlciTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 24),
    _MfrapPerfIcmpPerDlciTxAddrMaskReq_Type()
)
mfrapPerfIcmpPerDlciTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxAddrMaskReq.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxAddrMaskRep_Type = Counter32
_MfrapPerfIcmpPerDlciRxAddrMaskRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxAddrMaskRep = _MfrapPerfIcmpPerDlciRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 25),
    _MfrapPerfIcmpPerDlciRxAddrMaskRep_Type()
)
mfrapPerfIcmpPerDlciRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxAddrMaskRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxAddrMaskRep_Type = Counter32
_MfrapPerfIcmpPerDlciTxAddrMaskRep_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxAddrMaskRep = _MfrapPerfIcmpPerDlciTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 26),
    _MfrapPerfIcmpPerDlciTxAddrMaskRep_Type()
)
mfrapPerfIcmpPerDlciTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxAddrMaskRep.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxPktTooBig_Type = Counter32
_MfrapPerfIcmpPerDlciRxPktTooBig_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxPktTooBig = _MfrapPerfIcmpPerDlciRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 27),
    _MfrapPerfIcmpPerDlciRxPktTooBig_Type()
)
mfrapPerfIcmpPerDlciRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxPktTooBig.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxPktTooBig_Type = Counter32
_MfrapPerfIcmpPerDlciTxPktTooBig_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxPktTooBig = _MfrapPerfIcmpPerDlciTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 28),
    _MfrapPerfIcmpPerDlciTxPktTooBig_Type()
)
mfrapPerfIcmpPerDlciTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxPktTooBig.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxGmQuery_Type = Counter32
_MfrapPerfIcmpPerDlciRxGmQuery_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxGmQuery = _MfrapPerfIcmpPerDlciRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 29),
    _MfrapPerfIcmpPerDlciRxGmQuery_Type()
)
mfrapPerfIcmpPerDlciRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxGmQuery.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxGmQuery_Type = Counter32
_MfrapPerfIcmpPerDlciTxGmQuery_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxGmQuery = _MfrapPerfIcmpPerDlciTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 30),
    _MfrapPerfIcmpPerDlciTxGmQuery_Type()
)
mfrapPerfIcmpPerDlciTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxGmQuery.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxGmReport_Type = Counter32
_MfrapPerfIcmpPerDlciRxGmReport_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxGmReport = _MfrapPerfIcmpPerDlciRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 31),
    _MfrapPerfIcmpPerDlciRxGmReport_Type()
)
mfrapPerfIcmpPerDlciRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxGmReport.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxGmReport_Type = Counter32
_MfrapPerfIcmpPerDlciTxGmReport_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxGmReport = _MfrapPerfIcmpPerDlciTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 32),
    _MfrapPerfIcmpPerDlciTxGmReport_Type()
)
mfrapPerfIcmpPerDlciTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxGmReport.setStatus("mandatory")
_MfrapPerfIcmpPerDlciRxGmReduct_Type = Counter32
_MfrapPerfIcmpPerDlciRxGmReduct_Object = MibTableColumn
mfrapPerfIcmpPerDlciRxGmReduct = _MfrapPerfIcmpPerDlciRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 33),
    _MfrapPerfIcmpPerDlciRxGmReduct_Type()
)
mfrapPerfIcmpPerDlciRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciRxGmReduct.setStatus("mandatory")
_MfrapPerfIcmpPerDlciTxGmReduct_Type = Counter32
_MfrapPerfIcmpPerDlciTxGmReduct_Object = MibTableColumn
mfrapPerfIcmpPerDlciTxGmReduct = _MfrapPerfIcmpPerDlciTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 5, 1, 34),
    _MfrapPerfIcmpPerDlciTxGmReduct_Type()
)
mfrapPerfIcmpPerDlciTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpPerDlciTxGmReduct.setStatus("mandatory")
_MfrapPerfIcmpTotalTable_Object = MibTable
mfrapPerfIcmpTotalTable = _MfrapPerfIcmpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6)
)
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTable.setStatus("mandatory")
_MfrapPerfIcmpTotalEntry_Object = MibTableRow
mfrapPerfIcmpTotalEntry = _MfrapPerfIcmpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1)
)
mfrapPerfIcmpTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIcmpTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalEntry.setStatus("mandatory")


class _MfrapPerfIcmpTotalInterval_Type(Integer32):
    """Custom type mfrapPerfIcmpTotalInterval based on Integer32"""
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


_MfrapPerfIcmpTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfIcmpTotalInterval_Object = MibTableColumn
mfrapPerfIcmpTotalInterval = _MfrapPerfIcmpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 1),
    _MfrapPerfIcmpTotalInterval_Type()
)
mfrapPerfIcmpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalInterval.setStatus("mandatory")
_MfrapPerfIcmpTotalRxTotal_Type = Counter32
_MfrapPerfIcmpTotalRxTotal_Object = MibTableColumn
mfrapPerfIcmpTotalRxTotal = _MfrapPerfIcmpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 3),
    _MfrapPerfIcmpTotalRxTotal_Type()
)
mfrapPerfIcmpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxTotal.setStatus("mandatory")
_MfrapPerfIcmpTotalTxTotal_Type = Counter32
_MfrapPerfIcmpTotalTxTotal_Object = MibTableColumn
mfrapPerfIcmpTotalTxTotal = _MfrapPerfIcmpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 4),
    _MfrapPerfIcmpTotalTxTotal_Type()
)
mfrapPerfIcmpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxTotal.setStatus("mandatory")
_MfrapPerfIcmpTotalRxEchoRep_Type = Counter32
_MfrapPerfIcmpTotalRxEchoRep_Object = MibTableColumn
mfrapPerfIcmpTotalRxEchoRep = _MfrapPerfIcmpTotalRxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 5),
    _MfrapPerfIcmpTotalRxEchoRep_Type()
)
mfrapPerfIcmpTotalRxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxEchoRep.setStatus("mandatory")
_MfrapPerfIcmpTotalTxEchoRep_Type = Counter32
_MfrapPerfIcmpTotalTxEchoRep_Object = MibTableColumn
mfrapPerfIcmpTotalTxEchoRep = _MfrapPerfIcmpTotalTxEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 6),
    _MfrapPerfIcmpTotalTxEchoRep_Type()
)
mfrapPerfIcmpTotalTxEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxEchoRep.setStatus("mandatory")
_MfrapPerfIcmpTotalRxDestUnr_Type = Counter32
_MfrapPerfIcmpTotalRxDestUnr_Object = MibTableColumn
mfrapPerfIcmpTotalRxDestUnr = _MfrapPerfIcmpTotalRxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 7),
    _MfrapPerfIcmpTotalRxDestUnr_Type()
)
mfrapPerfIcmpTotalRxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxDestUnr.setStatus("mandatory")
_MfrapPerfIcmpTotalTxDestUnr_Type = Counter32
_MfrapPerfIcmpTotalTxDestUnr_Object = MibTableColumn
mfrapPerfIcmpTotalTxDestUnr = _MfrapPerfIcmpTotalTxDestUnr_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 8),
    _MfrapPerfIcmpTotalTxDestUnr_Type()
)
mfrapPerfIcmpTotalTxDestUnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxDestUnr.setStatus("mandatory")
_MfrapPerfIcmpTotalRxSrcQuench_Type = Counter32
_MfrapPerfIcmpTotalRxSrcQuench_Object = MibTableColumn
mfrapPerfIcmpTotalRxSrcQuench = _MfrapPerfIcmpTotalRxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 9),
    _MfrapPerfIcmpTotalRxSrcQuench_Type()
)
mfrapPerfIcmpTotalRxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxSrcQuench.setStatus("mandatory")
_MfrapPerfIcmpTotalTxSrcQuench_Type = Counter32
_MfrapPerfIcmpTotalTxSrcQuench_Object = MibTableColumn
mfrapPerfIcmpTotalTxSrcQuench = _MfrapPerfIcmpTotalTxSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 10),
    _MfrapPerfIcmpTotalTxSrcQuench_Type()
)
mfrapPerfIcmpTotalTxSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxSrcQuench.setStatus("mandatory")
_MfrapPerfIcmpTotalRxRedirect_Type = Counter32
_MfrapPerfIcmpTotalRxRedirect_Object = MibTableColumn
mfrapPerfIcmpTotalRxRedirect = _MfrapPerfIcmpTotalRxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 11),
    _MfrapPerfIcmpTotalRxRedirect_Type()
)
mfrapPerfIcmpTotalRxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxRedirect.setStatus("mandatory")
_MfrapPerfIcmpTotalTxRedirect_Type = Counter32
_MfrapPerfIcmpTotalTxRedirect_Object = MibTableColumn
mfrapPerfIcmpTotalTxRedirect = _MfrapPerfIcmpTotalTxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 12),
    _MfrapPerfIcmpTotalTxRedirect_Type()
)
mfrapPerfIcmpTotalTxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxRedirect.setStatus("mandatory")
_MfrapPerfIcmpTotalRxEchoReq_Type = Counter32
_MfrapPerfIcmpTotalRxEchoReq_Object = MibTableColumn
mfrapPerfIcmpTotalRxEchoReq = _MfrapPerfIcmpTotalRxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 13),
    _MfrapPerfIcmpTotalRxEchoReq_Type()
)
mfrapPerfIcmpTotalRxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxEchoReq.setStatus("mandatory")
_MfrapPerfIcmpTotalTxEchoReq_Type = Counter32
_MfrapPerfIcmpTotalTxEchoReq_Object = MibTableColumn
mfrapPerfIcmpTotalTxEchoReq = _MfrapPerfIcmpTotalTxEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 14),
    _MfrapPerfIcmpTotalTxEchoReq_Type()
)
mfrapPerfIcmpTotalTxEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxEchoReq.setStatus("mandatory")
_MfrapPerfIcmpTotalRxTimeExcd_Type = Counter32
_MfrapPerfIcmpTotalRxTimeExcd_Object = MibTableColumn
mfrapPerfIcmpTotalRxTimeExcd = _MfrapPerfIcmpTotalRxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 15),
    _MfrapPerfIcmpTotalRxTimeExcd_Type()
)
mfrapPerfIcmpTotalRxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxTimeExcd.setStatus("mandatory")
_MfrapPerfIcmpTotalTxTimeExcd_Type = Counter32
_MfrapPerfIcmpTotalTxTimeExcd_Object = MibTableColumn
mfrapPerfIcmpTotalTxTimeExcd = _MfrapPerfIcmpTotalTxTimeExcd_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 16),
    _MfrapPerfIcmpTotalTxTimeExcd_Type()
)
mfrapPerfIcmpTotalTxTimeExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxTimeExcd.setStatus("mandatory")
_MfrapPerfIcmpTotalRxParamProb_Type = Counter32
_MfrapPerfIcmpTotalRxParamProb_Object = MibTableColumn
mfrapPerfIcmpTotalRxParamProb = _MfrapPerfIcmpTotalRxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 17),
    _MfrapPerfIcmpTotalRxParamProb_Type()
)
mfrapPerfIcmpTotalRxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxParamProb.setStatus("mandatory")
_MfrapPerfIcmpTotalTxParamProb_Type = Counter32
_MfrapPerfIcmpTotalTxParamProb_Object = MibTableColumn
mfrapPerfIcmpTotalTxParamProb = _MfrapPerfIcmpTotalTxParamProb_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 18),
    _MfrapPerfIcmpTotalTxParamProb_Type()
)
mfrapPerfIcmpTotalTxParamProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxParamProb.setStatus("mandatory")
_MfrapPerfIcmpTotalRxTimestpReq_Type = Counter32
_MfrapPerfIcmpTotalRxTimestpReq_Object = MibTableColumn
mfrapPerfIcmpTotalRxTimestpReq = _MfrapPerfIcmpTotalRxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 19),
    _MfrapPerfIcmpTotalRxTimestpReq_Type()
)
mfrapPerfIcmpTotalRxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxTimestpReq.setStatus("mandatory")
_MfrapPerfIcmpTotalTxTimestpReq_Type = Counter32
_MfrapPerfIcmpTotalTxTimestpReq_Object = MibTableColumn
mfrapPerfIcmpTotalTxTimestpReq = _MfrapPerfIcmpTotalTxTimestpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 20),
    _MfrapPerfIcmpTotalTxTimestpReq_Type()
)
mfrapPerfIcmpTotalTxTimestpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxTimestpReq.setStatus("mandatory")
_MfrapPerfIcmpTotalRxTimestpRep_Type = Counter32
_MfrapPerfIcmpTotalRxTimestpRep_Object = MibTableColumn
mfrapPerfIcmpTotalRxTimestpRep = _MfrapPerfIcmpTotalRxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 21),
    _MfrapPerfIcmpTotalRxTimestpRep_Type()
)
mfrapPerfIcmpTotalRxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxTimestpRep.setStatus("mandatory")
_MfrapPerfIcmpTotalTxTimestpRep_Type = Counter32
_MfrapPerfIcmpTotalTxTimestpRep_Object = MibTableColumn
mfrapPerfIcmpTotalTxTimestpRep = _MfrapPerfIcmpTotalTxTimestpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 22),
    _MfrapPerfIcmpTotalTxTimestpRep_Type()
)
mfrapPerfIcmpTotalTxTimestpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxTimestpRep.setStatus("mandatory")
_MfrapPerfIcmpTotalRxAddrMaskReq_Type = Counter32
_MfrapPerfIcmpTotalRxAddrMaskReq_Object = MibTableColumn
mfrapPerfIcmpTotalRxAddrMaskReq = _MfrapPerfIcmpTotalRxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 23),
    _MfrapPerfIcmpTotalRxAddrMaskReq_Type()
)
mfrapPerfIcmpTotalRxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxAddrMaskReq.setStatus("mandatory")
_MfrapPerfIcmpTotalTxAddrMaskReq_Type = Counter32
_MfrapPerfIcmpTotalTxAddrMaskReq_Object = MibTableColumn
mfrapPerfIcmpTotalTxAddrMaskReq = _MfrapPerfIcmpTotalTxAddrMaskReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 24),
    _MfrapPerfIcmpTotalTxAddrMaskReq_Type()
)
mfrapPerfIcmpTotalTxAddrMaskReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxAddrMaskReq.setStatus("mandatory")
_MfrapPerfIcmpTotalRxAddrMaskRep_Type = Counter32
_MfrapPerfIcmpTotalRxAddrMaskRep_Object = MibTableColumn
mfrapPerfIcmpTotalRxAddrMaskRep = _MfrapPerfIcmpTotalRxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 25),
    _MfrapPerfIcmpTotalRxAddrMaskRep_Type()
)
mfrapPerfIcmpTotalRxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxAddrMaskRep.setStatus("mandatory")
_MfrapPerfIcmpTotalTxAddrMaskRep_Type = Counter32
_MfrapPerfIcmpTotalTxAddrMaskRep_Object = MibTableColumn
mfrapPerfIcmpTotalTxAddrMaskRep = _MfrapPerfIcmpTotalTxAddrMaskRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 26),
    _MfrapPerfIcmpTotalTxAddrMaskRep_Type()
)
mfrapPerfIcmpTotalTxAddrMaskRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxAddrMaskRep.setStatus("mandatory")
_MfrapPerfIcmpTotalRxPktTooBig_Type = Counter32
_MfrapPerfIcmpTotalRxPktTooBig_Object = MibTableColumn
mfrapPerfIcmpTotalRxPktTooBig = _MfrapPerfIcmpTotalRxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 27),
    _MfrapPerfIcmpTotalRxPktTooBig_Type()
)
mfrapPerfIcmpTotalRxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxPktTooBig.setStatus("mandatory")
_MfrapPerfIcmpTotalTxPktTooBig_Type = Counter32
_MfrapPerfIcmpTotalTxPktTooBig_Object = MibTableColumn
mfrapPerfIcmpTotalTxPktTooBig = _MfrapPerfIcmpTotalTxPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 28),
    _MfrapPerfIcmpTotalTxPktTooBig_Type()
)
mfrapPerfIcmpTotalTxPktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxPktTooBig.setStatus("mandatory")
_MfrapPerfIcmpTotalRxGmQuery_Type = Counter32
_MfrapPerfIcmpTotalRxGmQuery_Object = MibTableColumn
mfrapPerfIcmpTotalRxGmQuery = _MfrapPerfIcmpTotalRxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 29),
    _MfrapPerfIcmpTotalRxGmQuery_Type()
)
mfrapPerfIcmpTotalRxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxGmQuery.setStatus("mandatory")
_MfrapPerfIcmpTotalTxGmQuery_Type = Counter32
_MfrapPerfIcmpTotalTxGmQuery_Object = MibTableColumn
mfrapPerfIcmpTotalTxGmQuery = _MfrapPerfIcmpTotalTxGmQuery_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 30),
    _MfrapPerfIcmpTotalTxGmQuery_Type()
)
mfrapPerfIcmpTotalTxGmQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxGmQuery.setStatus("mandatory")
_MfrapPerfIcmpTotalRxGmReport_Type = Counter32
_MfrapPerfIcmpTotalRxGmReport_Object = MibTableColumn
mfrapPerfIcmpTotalRxGmReport = _MfrapPerfIcmpTotalRxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 31),
    _MfrapPerfIcmpTotalRxGmReport_Type()
)
mfrapPerfIcmpTotalRxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxGmReport.setStatus("mandatory")
_MfrapPerfIcmpTotalTxGmReport_Type = Counter32
_MfrapPerfIcmpTotalTxGmReport_Object = MibTableColumn
mfrapPerfIcmpTotalTxGmReport = _MfrapPerfIcmpTotalTxGmReport_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 32),
    _MfrapPerfIcmpTotalTxGmReport_Type()
)
mfrapPerfIcmpTotalTxGmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxGmReport.setStatus("mandatory")
_MfrapPerfIcmpTotalRxGmReduct_Type = Counter32
_MfrapPerfIcmpTotalRxGmReduct_Object = MibTableColumn
mfrapPerfIcmpTotalRxGmReduct = _MfrapPerfIcmpTotalRxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 33),
    _MfrapPerfIcmpTotalRxGmReduct_Type()
)
mfrapPerfIcmpTotalRxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalRxGmReduct.setStatus("mandatory")
_MfrapPerfIcmpTotalTxGmReduct_Type = Counter32
_MfrapPerfIcmpTotalTxGmReduct_Object = MibTableColumn
mfrapPerfIcmpTotalTxGmReduct = _MfrapPerfIcmpTotalTxGmReduct_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 6, 1, 34),
    _MfrapPerfIcmpTotalTxGmReduct_Type()
)
mfrapPerfIcmpTotalTxGmReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIcmpTotalTxGmReduct.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTable_Object = MibTable
mfrapPerfApplicationPerDlciTable = _MfrapPerfApplicationPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7)
)
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTable.setStatus("mandatory")
_MfrapPerfApplicationPerDlciEntry_Object = MibTableRow
mfrapPerfApplicationPerDlciEntry = _MfrapPerfApplicationPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1)
)
mfrapPerfApplicationPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfApplicationPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfApplicationPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciEntry.setStatus("mandatory")


class _MfrapPerfApplicationPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfApplicationPerDlciInterval based on Integer32"""
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


_MfrapPerfApplicationPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfApplicationPerDlciInterval_Object = MibTableColumn
mfrapPerfApplicationPerDlciInterval = _MfrapPerfApplicationPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 1),
    _MfrapPerfApplicationPerDlciInterval_Type()
)
mfrapPerfApplicationPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciInterval.setStatus("mandatory")
_MfrapPerfApplicationPerDlciValue_Type = Integer32
_MfrapPerfApplicationPerDlciValue_Object = MibTableColumn
mfrapPerfApplicationPerDlciValue = _MfrapPerfApplicationPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 2),
    _MfrapPerfApplicationPerDlciValue_Type()
)
mfrapPerfApplicationPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciValue.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxSnmp_Type = Counter32
_MfrapPerfApplicationPerDlciRxSnmp_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxSnmp = _MfrapPerfApplicationPerDlciRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 3),
    _MfrapPerfApplicationPerDlciRxSnmp_Type()
)
mfrapPerfApplicationPerDlciRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxSnmp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxSnmp_Type = Counter32
_MfrapPerfApplicationPerDlciTxSnmp_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxSnmp = _MfrapPerfApplicationPerDlciTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 4),
    _MfrapPerfApplicationPerDlciTxSnmp_Type()
)
mfrapPerfApplicationPerDlciTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxSnmp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxSnmpTrap_Type = Counter32
_MfrapPerfApplicationPerDlciRxSnmpTrap_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxSnmpTrap = _MfrapPerfApplicationPerDlciRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 5),
    _MfrapPerfApplicationPerDlciRxSnmpTrap_Type()
)
mfrapPerfApplicationPerDlciRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxSnmpTrap.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxSnmpTrap_Type = Counter32
_MfrapPerfApplicationPerDlciTxSnmpTrap_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxSnmpTrap = _MfrapPerfApplicationPerDlciTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 6),
    _MfrapPerfApplicationPerDlciTxSnmpTrap_Type()
)
mfrapPerfApplicationPerDlciTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxSnmpTrap.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxHttp_Type = Counter32
_MfrapPerfApplicationPerDlciRxHttp_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxHttp = _MfrapPerfApplicationPerDlciRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 7),
    _MfrapPerfApplicationPerDlciRxHttp_Type()
)
mfrapPerfApplicationPerDlciRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxHttp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxHttp_Type = Counter32
_MfrapPerfApplicationPerDlciTxHttp_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxHttp = _MfrapPerfApplicationPerDlciTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 8),
    _MfrapPerfApplicationPerDlciTxHttp_Type()
)
mfrapPerfApplicationPerDlciTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxHttp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxTelnet_Type = Counter32
_MfrapPerfApplicationPerDlciRxTelnet_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxTelnet = _MfrapPerfApplicationPerDlciRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 9),
    _MfrapPerfApplicationPerDlciRxTelnet_Type()
)
mfrapPerfApplicationPerDlciRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxTelnet.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxTelnet_Type = Counter32
_MfrapPerfApplicationPerDlciTxTelnet_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxTelnet = _MfrapPerfApplicationPerDlciTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 10),
    _MfrapPerfApplicationPerDlciTxTelnet_Type()
)
mfrapPerfApplicationPerDlciTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxTelnet.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxSmtp_Type = Counter32
_MfrapPerfApplicationPerDlciRxSmtp_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxSmtp = _MfrapPerfApplicationPerDlciRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 11),
    _MfrapPerfApplicationPerDlciRxSmtp_Type()
)
mfrapPerfApplicationPerDlciRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxSmtp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxSmtp_Type = Counter32
_MfrapPerfApplicationPerDlciTxSmtp_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxSmtp = _MfrapPerfApplicationPerDlciTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 12),
    _MfrapPerfApplicationPerDlciTxSmtp_Type()
)
mfrapPerfApplicationPerDlciTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxSmtp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxFtp_Type = Counter32
_MfrapPerfApplicationPerDlciRxFtp_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxFtp = _MfrapPerfApplicationPerDlciRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 13),
    _MfrapPerfApplicationPerDlciRxFtp_Type()
)
mfrapPerfApplicationPerDlciRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxFtp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxFtp_Type = Counter32
_MfrapPerfApplicationPerDlciTxFtp_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxFtp = _MfrapPerfApplicationPerDlciTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 14),
    _MfrapPerfApplicationPerDlciTxFtp_Type()
)
mfrapPerfApplicationPerDlciTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxFtp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxTftp_Type = Counter32
_MfrapPerfApplicationPerDlciRxTftp_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxTftp = _MfrapPerfApplicationPerDlciRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 15),
    _MfrapPerfApplicationPerDlciRxTftp_Type()
)
mfrapPerfApplicationPerDlciRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxTftp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxTftp_Type = Counter32
_MfrapPerfApplicationPerDlciTxTftp_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxTftp = _MfrapPerfApplicationPerDlciTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 16),
    _MfrapPerfApplicationPerDlciTxTftp_Type()
)
mfrapPerfApplicationPerDlciTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxTftp.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxCustom1_Type = Counter32
_MfrapPerfApplicationPerDlciRxCustom1_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxCustom1 = _MfrapPerfApplicationPerDlciRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 17),
    _MfrapPerfApplicationPerDlciRxCustom1_Type()
)
mfrapPerfApplicationPerDlciRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxCustom1.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxCustom1_Type = Counter32
_MfrapPerfApplicationPerDlciTxCustom1_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxCustom1 = _MfrapPerfApplicationPerDlciTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 18),
    _MfrapPerfApplicationPerDlciTxCustom1_Type()
)
mfrapPerfApplicationPerDlciTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxCustom1.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxCustom2_Type = Counter32
_MfrapPerfApplicationPerDlciRxCustom2_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxCustom2 = _MfrapPerfApplicationPerDlciRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 19),
    _MfrapPerfApplicationPerDlciRxCustom2_Type()
)
mfrapPerfApplicationPerDlciRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxCustom2.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxCustom2_Type = Counter32
_MfrapPerfApplicationPerDlciTxCustom2_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxCustom2 = _MfrapPerfApplicationPerDlciTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 20),
    _MfrapPerfApplicationPerDlciTxCustom2_Type()
)
mfrapPerfApplicationPerDlciTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxCustom2.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxCustom3_Type = Counter32
_MfrapPerfApplicationPerDlciRxCustom3_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxCustom3 = _MfrapPerfApplicationPerDlciRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 21),
    _MfrapPerfApplicationPerDlciRxCustom3_Type()
)
mfrapPerfApplicationPerDlciRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxCustom3.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxCustom3_Type = Counter32
_MfrapPerfApplicationPerDlciTxCustom3_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxCustom3 = _MfrapPerfApplicationPerDlciTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 22),
    _MfrapPerfApplicationPerDlciTxCustom3_Type()
)
mfrapPerfApplicationPerDlciTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxCustom3.setStatus("mandatory")
_MfrapPerfApplicationPerDlciRxCustom4_Type = Counter32
_MfrapPerfApplicationPerDlciRxCustom4_Object = MibTableColumn
mfrapPerfApplicationPerDlciRxCustom4 = _MfrapPerfApplicationPerDlciRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 23),
    _MfrapPerfApplicationPerDlciRxCustom4_Type()
)
mfrapPerfApplicationPerDlciRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciRxCustom4.setStatus("mandatory")
_MfrapPerfApplicationPerDlciTxCustom4_Type = Counter32
_MfrapPerfApplicationPerDlciTxCustom4_Object = MibTableColumn
mfrapPerfApplicationPerDlciTxCustom4 = _MfrapPerfApplicationPerDlciTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 7, 1, 24),
    _MfrapPerfApplicationPerDlciTxCustom4_Type()
)
mfrapPerfApplicationPerDlciTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationPerDlciTxCustom4.setStatus("mandatory")
_MfrapPerfApplicationTotalTable_Object = MibTable
mfrapPerfApplicationTotalTable = _MfrapPerfApplicationTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8)
)
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTable.setStatus("mandatory")
_MfrapPerfApplicationTotalEntry_Object = MibTableRow
mfrapPerfApplicationTotalEntry = _MfrapPerfApplicationTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1)
)
mfrapPerfApplicationTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfApplicationTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalEntry.setStatus("mandatory")


class _MfrapPerfApplicationTotalInterval_Type(Integer32):
    """Custom type mfrapPerfApplicationTotalInterval based on Integer32"""
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


_MfrapPerfApplicationTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfApplicationTotalInterval_Object = MibTableColumn
mfrapPerfApplicationTotalInterval = _MfrapPerfApplicationTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 1),
    _MfrapPerfApplicationTotalInterval_Type()
)
mfrapPerfApplicationTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalInterval.setStatus("mandatory")
_MfrapPerfApplicationTotalRxSnmp_Type = Counter32
_MfrapPerfApplicationTotalRxSnmp_Object = MibTableColumn
mfrapPerfApplicationTotalRxSnmp = _MfrapPerfApplicationTotalRxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 3),
    _MfrapPerfApplicationTotalRxSnmp_Type()
)
mfrapPerfApplicationTotalRxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxSnmp.setStatus("mandatory")
_MfrapPerfApplicationTotalTxSnmp_Type = Counter32
_MfrapPerfApplicationTotalTxSnmp_Object = MibTableColumn
mfrapPerfApplicationTotalTxSnmp = _MfrapPerfApplicationTotalTxSnmp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 4),
    _MfrapPerfApplicationTotalTxSnmp_Type()
)
mfrapPerfApplicationTotalTxSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxSnmp.setStatus("mandatory")
_MfrapPerfApplicationTotalRxSnmpTrap_Type = Counter32
_MfrapPerfApplicationTotalRxSnmpTrap_Object = MibTableColumn
mfrapPerfApplicationTotalRxSnmpTrap = _MfrapPerfApplicationTotalRxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 5),
    _MfrapPerfApplicationTotalRxSnmpTrap_Type()
)
mfrapPerfApplicationTotalRxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxSnmpTrap.setStatus("mandatory")
_MfrapPerfApplicationTotalTxSnmpTrap_Type = Counter32
_MfrapPerfApplicationTotalTxSnmpTrap_Object = MibTableColumn
mfrapPerfApplicationTotalTxSnmpTrap = _MfrapPerfApplicationTotalTxSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 6),
    _MfrapPerfApplicationTotalTxSnmpTrap_Type()
)
mfrapPerfApplicationTotalTxSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxSnmpTrap.setStatus("mandatory")
_MfrapPerfApplicationTotalRxHttp_Type = Counter32
_MfrapPerfApplicationTotalRxHttp_Object = MibTableColumn
mfrapPerfApplicationTotalRxHttp = _MfrapPerfApplicationTotalRxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 7),
    _MfrapPerfApplicationTotalRxHttp_Type()
)
mfrapPerfApplicationTotalRxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxHttp.setStatus("mandatory")
_MfrapPerfApplicationTotalTxHttp_Type = Counter32
_MfrapPerfApplicationTotalTxHttp_Object = MibTableColumn
mfrapPerfApplicationTotalTxHttp = _MfrapPerfApplicationTotalTxHttp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 8),
    _MfrapPerfApplicationTotalTxHttp_Type()
)
mfrapPerfApplicationTotalTxHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxHttp.setStatus("mandatory")
_MfrapPerfApplicationTotalRxTelnet_Type = Counter32
_MfrapPerfApplicationTotalRxTelnet_Object = MibTableColumn
mfrapPerfApplicationTotalRxTelnet = _MfrapPerfApplicationTotalRxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 9),
    _MfrapPerfApplicationTotalRxTelnet_Type()
)
mfrapPerfApplicationTotalRxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxTelnet.setStatus("mandatory")
_MfrapPerfApplicationTotalTxTelnet_Type = Counter32
_MfrapPerfApplicationTotalTxTelnet_Object = MibTableColumn
mfrapPerfApplicationTotalTxTelnet = _MfrapPerfApplicationTotalTxTelnet_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 10),
    _MfrapPerfApplicationTotalTxTelnet_Type()
)
mfrapPerfApplicationTotalTxTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxTelnet.setStatus("mandatory")
_MfrapPerfApplicationTotalRxSmtp_Type = Counter32
_MfrapPerfApplicationTotalRxSmtp_Object = MibTableColumn
mfrapPerfApplicationTotalRxSmtp = _MfrapPerfApplicationTotalRxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 11),
    _MfrapPerfApplicationTotalRxSmtp_Type()
)
mfrapPerfApplicationTotalRxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxSmtp.setStatus("mandatory")
_MfrapPerfApplicationTotalTxSmtp_Type = Counter32
_MfrapPerfApplicationTotalTxSmtp_Object = MibTableColumn
mfrapPerfApplicationTotalTxSmtp = _MfrapPerfApplicationTotalTxSmtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 12),
    _MfrapPerfApplicationTotalTxSmtp_Type()
)
mfrapPerfApplicationTotalTxSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxSmtp.setStatus("mandatory")
_MfrapPerfApplicationTotalRxFtp_Type = Counter32
_MfrapPerfApplicationTotalRxFtp_Object = MibTableColumn
mfrapPerfApplicationTotalRxFtp = _MfrapPerfApplicationTotalRxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 13),
    _MfrapPerfApplicationTotalRxFtp_Type()
)
mfrapPerfApplicationTotalRxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxFtp.setStatus("mandatory")
_MfrapPerfApplicationTotalTxFtp_Type = Counter32
_MfrapPerfApplicationTotalTxFtp_Object = MibTableColumn
mfrapPerfApplicationTotalTxFtp = _MfrapPerfApplicationTotalTxFtp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 14),
    _MfrapPerfApplicationTotalTxFtp_Type()
)
mfrapPerfApplicationTotalTxFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxFtp.setStatus("mandatory")
_MfrapPerfApplicationTotalRxTftp_Type = Counter32
_MfrapPerfApplicationTotalRxTftp_Object = MibTableColumn
mfrapPerfApplicationTotalRxTftp = _MfrapPerfApplicationTotalRxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 15),
    _MfrapPerfApplicationTotalRxTftp_Type()
)
mfrapPerfApplicationTotalRxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxTftp.setStatus("mandatory")
_MfrapPerfApplicationTotalTxTftp_Type = Counter32
_MfrapPerfApplicationTotalTxTftp_Object = MibTableColumn
mfrapPerfApplicationTotalTxTftp = _MfrapPerfApplicationTotalTxTftp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 16),
    _MfrapPerfApplicationTotalTxTftp_Type()
)
mfrapPerfApplicationTotalTxTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxTftp.setStatus("mandatory")
_MfrapPerfApplicationTotalRxCustom1_Type = Counter32
_MfrapPerfApplicationTotalRxCustom1_Object = MibTableColumn
mfrapPerfApplicationTotalRxCustom1 = _MfrapPerfApplicationTotalRxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 17),
    _MfrapPerfApplicationTotalRxCustom1_Type()
)
mfrapPerfApplicationTotalRxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxCustom1.setStatus("mandatory")
_MfrapPerfApplicationTotalTxCustom1_Type = Counter32
_MfrapPerfApplicationTotalTxCustom1_Object = MibTableColumn
mfrapPerfApplicationTotalTxCustom1 = _MfrapPerfApplicationTotalTxCustom1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 18),
    _MfrapPerfApplicationTotalTxCustom1_Type()
)
mfrapPerfApplicationTotalTxCustom1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxCustom1.setStatus("mandatory")
_MfrapPerfApplicationTotalRxCustom2_Type = Counter32
_MfrapPerfApplicationTotalRxCustom2_Object = MibTableColumn
mfrapPerfApplicationTotalRxCustom2 = _MfrapPerfApplicationTotalRxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 19),
    _MfrapPerfApplicationTotalRxCustom2_Type()
)
mfrapPerfApplicationTotalRxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxCustom2.setStatus("mandatory")
_MfrapPerfApplicationTotalTxCustom2_Type = Counter32
_MfrapPerfApplicationTotalTxCustom2_Object = MibTableColumn
mfrapPerfApplicationTotalTxCustom2 = _MfrapPerfApplicationTotalTxCustom2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 20),
    _MfrapPerfApplicationTotalTxCustom2_Type()
)
mfrapPerfApplicationTotalTxCustom2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxCustom2.setStatus("mandatory")
_MfrapPerfApplicationTotalRxCustom3_Type = Counter32
_MfrapPerfApplicationTotalRxCustom3_Object = MibTableColumn
mfrapPerfApplicationTotalRxCustom3 = _MfrapPerfApplicationTotalRxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 21),
    _MfrapPerfApplicationTotalRxCustom3_Type()
)
mfrapPerfApplicationTotalRxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxCustom3.setStatus("mandatory")
_MfrapPerfApplicationTotalTxCustom3_Type = Counter32
_MfrapPerfApplicationTotalTxCustom3_Object = MibTableColumn
mfrapPerfApplicationTotalTxCustom3 = _MfrapPerfApplicationTotalTxCustom3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 22),
    _MfrapPerfApplicationTotalTxCustom3_Type()
)
mfrapPerfApplicationTotalTxCustom3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxCustom3.setStatus("mandatory")
_MfrapPerfApplicationTotalRxCustom4_Type = Counter32
_MfrapPerfApplicationTotalRxCustom4_Object = MibTableColumn
mfrapPerfApplicationTotalRxCustom4 = _MfrapPerfApplicationTotalRxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 23),
    _MfrapPerfApplicationTotalRxCustom4_Type()
)
mfrapPerfApplicationTotalRxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalRxCustom4.setStatus("mandatory")
_MfrapPerfApplicationTotalTxCustom4_Type = Counter32
_MfrapPerfApplicationTotalTxCustom4_Object = MibTableColumn
mfrapPerfApplicationTotalTxCustom4 = _MfrapPerfApplicationTotalTxCustom4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 8, 1, 24),
    _MfrapPerfApplicationTotalTxCustom4_Type()
)
mfrapPerfApplicationTotalTxCustom4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfApplicationTotalTxCustom4.setStatus("mandatory")
_MfrapPerfRoutingPerDlciTable_Object = MibTable
mfrapPerfRoutingPerDlciTable = _MfrapPerfRoutingPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9)
)
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciTable.setStatus("mandatory")
_MfrapPerfRoutingPerDlciEntry_Object = MibTableRow
mfrapPerfRoutingPerDlciEntry = _MfrapPerfRoutingPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1)
)
mfrapPerfRoutingPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfRoutingPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfRoutingPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciEntry.setStatus("mandatory")


class _MfrapPerfRoutingPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfRoutingPerDlciInterval based on Integer32"""
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


_MfrapPerfRoutingPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfRoutingPerDlciInterval_Object = MibTableColumn
mfrapPerfRoutingPerDlciInterval = _MfrapPerfRoutingPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 1),
    _MfrapPerfRoutingPerDlciInterval_Type()
)
mfrapPerfRoutingPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciInterval.setStatus("mandatory")
_MfrapPerfRoutingPerDlciValue_Type = Integer32
_MfrapPerfRoutingPerDlciValue_Object = MibTableColumn
mfrapPerfRoutingPerDlciValue = _MfrapPerfRoutingPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 2),
    _MfrapPerfRoutingPerDlciValue_Type()
)
mfrapPerfRoutingPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciValue.setStatus("mandatory")
_MfrapPerfRoutingPerDlciRxOspf_Type = Counter32
_MfrapPerfRoutingPerDlciRxOspf_Object = MibTableColumn
mfrapPerfRoutingPerDlciRxOspf = _MfrapPerfRoutingPerDlciRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 3),
    _MfrapPerfRoutingPerDlciRxOspf_Type()
)
mfrapPerfRoutingPerDlciRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciRxOspf.setStatus("mandatory")
_MfrapPerfRoutingPerDlciTxOspf_Type = Counter32
_MfrapPerfRoutingPerDlciTxOspf_Object = MibTableColumn
mfrapPerfRoutingPerDlciTxOspf = _MfrapPerfRoutingPerDlciTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 4),
    _MfrapPerfRoutingPerDlciTxOspf_Type()
)
mfrapPerfRoutingPerDlciTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciTxOspf.setStatus("mandatory")
_MfrapPerfRoutingPerDlciRxRip_Type = Counter32
_MfrapPerfRoutingPerDlciRxRip_Object = MibTableColumn
mfrapPerfRoutingPerDlciRxRip = _MfrapPerfRoutingPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 5),
    _MfrapPerfRoutingPerDlciRxRip_Type()
)
mfrapPerfRoutingPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciRxRip.setStatus("mandatory")
_MfrapPerfRoutingPerDlciTxRip_Type = Counter32
_MfrapPerfRoutingPerDlciTxRip_Object = MibTableColumn
mfrapPerfRoutingPerDlciTxRip = _MfrapPerfRoutingPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 6),
    _MfrapPerfRoutingPerDlciTxRip_Type()
)
mfrapPerfRoutingPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciTxRip.setStatus("mandatory")
_MfrapPerfRoutingPerDlciRxNetbios_Type = Counter32
_MfrapPerfRoutingPerDlciRxNetbios_Object = MibTableColumn
mfrapPerfRoutingPerDlciRxNetbios = _MfrapPerfRoutingPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 7),
    _MfrapPerfRoutingPerDlciRxNetbios_Type()
)
mfrapPerfRoutingPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciRxNetbios.setStatus("mandatory")
_MfrapPerfRoutingPerDlciTxNetbios_Type = Counter32
_MfrapPerfRoutingPerDlciTxNetbios_Object = MibTableColumn
mfrapPerfRoutingPerDlciTxNetbios = _MfrapPerfRoutingPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 9, 1, 8),
    _MfrapPerfRoutingPerDlciTxNetbios_Type()
)
mfrapPerfRoutingPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingPerDlciTxNetbios.setStatus("mandatory")
_MfrapPerfRoutingTotalTable_Object = MibTable
mfrapPerfRoutingTotalTable = _MfrapPerfRoutingTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalTable.setStatus("mandatory")
_MfrapPerfRoutingTotalEntry_Object = MibTableRow
mfrapPerfRoutingTotalEntry = _MfrapPerfRoutingTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1)
)
mfrapPerfRoutingTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfRoutingTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalEntry.setStatus("mandatory")


class _MfrapPerfRoutingTotalInterval_Type(Integer32):
    """Custom type mfrapPerfRoutingTotalInterval based on Integer32"""
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


_MfrapPerfRoutingTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfRoutingTotalInterval_Object = MibTableColumn
mfrapPerfRoutingTotalInterval = _MfrapPerfRoutingTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 1),
    _MfrapPerfRoutingTotalInterval_Type()
)
mfrapPerfRoutingTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalInterval.setStatus("mandatory")
_MfrapPerfRoutingTotalRxOspf_Type = Counter32
_MfrapPerfRoutingTotalRxOspf_Object = MibTableColumn
mfrapPerfRoutingTotalRxOspf = _MfrapPerfRoutingTotalRxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 3),
    _MfrapPerfRoutingTotalRxOspf_Type()
)
mfrapPerfRoutingTotalRxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalRxOspf.setStatus("mandatory")
_MfrapPerfRoutingTotalTxOspf_Type = Counter32
_MfrapPerfRoutingTotalTxOspf_Object = MibTableColumn
mfrapPerfRoutingTotalTxOspf = _MfrapPerfRoutingTotalTxOspf_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 4),
    _MfrapPerfRoutingTotalTxOspf_Type()
)
mfrapPerfRoutingTotalTxOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalTxOspf.setStatus("mandatory")
_MfrapPerfRoutingTotalRxRip_Type = Counter32
_MfrapPerfRoutingTotalRxRip_Object = MibTableColumn
mfrapPerfRoutingTotalRxRip = _MfrapPerfRoutingTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 5),
    _MfrapPerfRoutingTotalRxRip_Type()
)
mfrapPerfRoutingTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalRxRip.setStatus("mandatory")
_MfrapPerfRoutingTotalTxRip_Type = Counter32
_MfrapPerfRoutingTotalTxRip_Object = MibTableColumn
mfrapPerfRoutingTotalTxRip = _MfrapPerfRoutingTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 6),
    _MfrapPerfRoutingTotalTxRip_Type()
)
mfrapPerfRoutingTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalTxRip.setStatus("mandatory")
_MfrapPerfRoutingTotalRxNetbios_Type = Counter32
_MfrapPerfRoutingTotalRxNetbios_Object = MibTableColumn
mfrapPerfRoutingTotalRxNetbios = _MfrapPerfRoutingTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 7),
    _MfrapPerfRoutingTotalRxNetbios_Type()
)
mfrapPerfRoutingTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalRxNetbios.setStatus("mandatory")
_MfrapPerfRoutingTotalTxNetbios_Type = Counter32
_MfrapPerfRoutingTotalTxNetbios_Object = MibTableColumn
mfrapPerfRoutingTotalTxNetbios = _MfrapPerfRoutingTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 10, 1, 8),
    _MfrapPerfRoutingTotalTxNetbios_Type()
)
mfrapPerfRoutingTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfRoutingTotalTxNetbios.setStatus("mandatory")
_MfrapPerfIpxPerDlciTable_Object = MibTable
mfrapPerfIpxPerDlciTable = _MfrapPerfIpxPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTable.setStatus("mandatory")
_MfrapPerfIpxPerDlciEntry_Object = MibTableRow
mfrapPerfIpxPerDlciEntry = _MfrapPerfIpxPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1)
)
mfrapPerfIpxPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIpxPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfIpxPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciEntry.setStatus("mandatory")


class _MfrapPerfIpxPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfIpxPerDlciInterval based on Integer32"""
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


_MfrapPerfIpxPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfIpxPerDlciInterval_Object = MibTableColumn
mfrapPerfIpxPerDlciInterval = _MfrapPerfIpxPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 1),
    _MfrapPerfIpxPerDlciInterval_Type()
)
mfrapPerfIpxPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciInterval.setStatus("mandatory")
_MfrapPerfIpxPerDlciValue_Type = Integer32
_MfrapPerfIpxPerDlciValue_Object = MibTableColumn
mfrapPerfIpxPerDlciValue = _MfrapPerfIpxPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 2),
    _MfrapPerfIpxPerDlciValue_Type()
)
mfrapPerfIpxPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciValue.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxTotal_Type = Counter32
_MfrapPerfIpxPerDlciRxTotal_Object = MibTableColumn
mfrapPerfIpxPerDlciRxTotal = _MfrapPerfIpxPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 3),
    _MfrapPerfIpxPerDlciRxTotal_Type()
)
mfrapPerfIpxPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxTotal_Type = Counter32
_MfrapPerfIpxPerDlciTxTotal_Object = MibTableColumn
mfrapPerfIpxPerDlciTxTotal = _MfrapPerfIpxPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 4),
    _MfrapPerfIpxPerDlciTxTotal_Type()
)
mfrapPerfIpxPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxSpx_Type = Counter32
_MfrapPerfIpxPerDlciRxSpx_Object = MibTableColumn
mfrapPerfIpxPerDlciRxSpx = _MfrapPerfIpxPerDlciRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 5),
    _MfrapPerfIpxPerDlciRxSpx_Type()
)
mfrapPerfIpxPerDlciRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxSpx.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxSpx_Type = Counter32
_MfrapPerfIpxPerDlciTxSpx_Object = MibTableColumn
mfrapPerfIpxPerDlciTxSpx = _MfrapPerfIpxPerDlciTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 6),
    _MfrapPerfIpxPerDlciTxSpx_Type()
)
mfrapPerfIpxPerDlciTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxSpx.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxNcp_Type = Counter32
_MfrapPerfIpxPerDlciRxNcp_Object = MibTableColumn
mfrapPerfIpxPerDlciRxNcp = _MfrapPerfIpxPerDlciRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 7),
    _MfrapPerfIpxPerDlciRxNcp_Type()
)
mfrapPerfIpxPerDlciRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxNcp.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxNcp_Type = Counter32
_MfrapPerfIpxPerDlciTxNcp_Object = MibTableColumn
mfrapPerfIpxPerDlciTxNcp = _MfrapPerfIpxPerDlciTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 8),
    _MfrapPerfIpxPerDlciTxNcp_Type()
)
mfrapPerfIpxPerDlciTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxNcp.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxSap_Type = Counter32
_MfrapPerfIpxPerDlciRxSap_Object = MibTableColumn
mfrapPerfIpxPerDlciRxSap = _MfrapPerfIpxPerDlciRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 9),
    _MfrapPerfIpxPerDlciRxSap_Type()
)
mfrapPerfIpxPerDlciRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxSap.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxSap_Type = Counter32
_MfrapPerfIpxPerDlciTxSap_Object = MibTableColumn
mfrapPerfIpxPerDlciTxSap = _MfrapPerfIpxPerDlciTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 10),
    _MfrapPerfIpxPerDlciTxSap_Type()
)
mfrapPerfIpxPerDlciTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxSap.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxRip_Type = Counter32
_MfrapPerfIpxPerDlciRxRip_Object = MibTableColumn
mfrapPerfIpxPerDlciRxRip = _MfrapPerfIpxPerDlciRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 11),
    _MfrapPerfIpxPerDlciRxRip_Type()
)
mfrapPerfIpxPerDlciRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxRip.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxRip_Type = Counter32
_MfrapPerfIpxPerDlciTxRip_Object = MibTableColumn
mfrapPerfIpxPerDlciTxRip = _MfrapPerfIpxPerDlciTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 12),
    _MfrapPerfIpxPerDlciTxRip_Type()
)
mfrapPerfIpxPerDlciTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxRip.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxNetbios_Type = Counter32
_MfrapPerfIpxPerDlciRxNetbios_Object = MibTableColumn
mfrapPerfIpxPerDlciRxNetbios = _MfrapPerfIpxPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 13),
    _MfrapPerfIpxPerDlciRxNetbios_Type()
)
mfrapPerfIpxPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxNetbios.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxNetbios_Type = Counter32
_MfrapPerfIpxPerDlciTxNetbios_Object = MibTableColumn
mfrapPerfIpxPerDlciTxNetbios = _MfrapPerfIpxPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 14),
    _MfrapPerfIpxPerDlciTxNetbios_Type()
)
mfrapPerfIpxPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxNetbios.setStatus("mandatory")
_MfrapPerfIpxPerDlciRxOther_Type = Counter32
_MfrapPerfIpxPerDlciRxOther_Object = MibTableColumn
mfrapPerfIpxPerDlciRxOther = _MfrapPerfIpxPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 15),
    _MfrapPerfIpxPerDlciRxOther_Type()
)
mfrapPerfIpxPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciRxOther.setStatus("mandatory")
_MfrapPerfIpxPerDlciTxOther_Type = Counter32
_MfrapPerfIpxPerDlciTxOther_Object = MibTableColumn
mfrapPerfIpxPerDlciTxOther = _MfrapPerfIpxPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 11, 1, 16),
    _MfrapPerfIpxPerDlciTxOther_Type()
)
mfrapPerfIpxPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxPerDlciTxOther.setStatus("mandatory")
_MfrapPerfIpxTotalTable_Object = MibTable
mfrapPerfIpxTotalTable = _MfrapPerfIpxTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12)
)
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTable.setStatus("mandatory")
_MfrapPerfIpxTotalEntry_Object = MibTableRow
mfrapPerfIpxTotalEntry = _MfrapPerfIpxTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1)
)
mfrapPerfIpxTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfIpxTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalEntry.setStatus("mandatory")


class _MfrapPerfIpxTotalInterval_Type(Integer32):
    """Custom type mfrapPerfIpxTotalInterval based on Integer32"""
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


_MfrapPerfIpxTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfIpxTotalInterval_Object = MibTableColumn
mfrapPerfIpxTotalInterval = _MfrapPerfIpxTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 1),
    _MfrapPerfIpxTotalInterval_Type()
)
mfrapPerfIpxTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalInterval.setStatus("mandatory")
_MfrapPerfIpxTotalRxTotal_Type = Counter32
_MfrapPerfIpxTotalRxTotal_Object = MibTableColumn
mfrapPerfIpxTotalRxTotal = _MfrapPerfIpxTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 3),
    _MfrapPerfIpxTotalRxTotal_Type()
)
mfrapPerfIpxTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxTotal.setStatus("mandatory")
_MfrapPerfIpxTotalTxTotal_Type = Counter32
_MfrapPerfIpxTotalTxTotal_Object = MibTableColumn
mfrapPerfIpxTotalTxTotal = _MfrapPerfIpxTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 4),
    _MfrapPerfIpxTotalTxTotal_Type()
)
mfrapPerfIpxTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxTotal.setStatus("mandatory")
_MfrapPerfIpxTotalRxSpx_Type = Counter32
_MfrapPerfIpxTotalRxSpx_Object = MibTableColumn
mfrapPerfIpxTotalRxSpx = _MfrapPerfIpxTotalRxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 5),
    _MfrapPerfIpxTotalRxSpx_Type()
)
mfrapPerfIpxTotalRxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxSpx.setStatus("mandatory")
_MfrapPerfIpxTotalTxSpx_Type = Counter32
_MfrapPerfIpxTotalTxSpx_Object = MibTableColumn
mfrapPerfIpxTotalTxSpx = _MfrapPerfIpxTotalTxSpx_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 6),
    _MfrapPerfIpxTotalTxSpx_Type()
)
mfrapPerfIpxTotalTxSpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxSpx.setStatus("mandatory")
_MfrapPerfIpxTotalRxNcp_Type = Counter32
_MfrapPerfIpxTotalRxNcp_Object = MibTableColumn
mfrapPerfIpxTotalRxNcp = _MfrapPerfIpxTotalRxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 7),
    _MfrapPerfIpxTotalRxNcp_Type()
)
mfrapPerfIpxTotalRxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxNcp.setStatus("mandatory")
_MfrapPerfIpxTotalTxNcp_Type = Counter32
_MfrapPerfIpxTotalTxNcp_Object = MibTableColumn
mfrapPerfIpxTotalTxNcp = _MfrapPerfIpxTotalTxNcp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 8),
    _MfrapPerfIpxTotalTxNcp_Type()
)
mfrapPerfIpxTotalTxNcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxNcp.setStatus("mandatory")
_MfrapPerfIpxTotalRxSap_Type = Counter32
_MfrapPerfIpxTotalRxSap_Object = MibTableColumn
mfrapPerfIpxTotalRxSap = _MfrapPerfIpxTotalRxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 9),
    _MfrapPerfIpxTotalRxSap_Type()
)
mfrapPerfIpxTotalRxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxSap.setStatus("mandatory")
_MfrapPerfIpxTotalTxSap_Type = Counter32
_MfrapPerfIpxTotalTxSap_Object = MibTableColumn
mfrapPerfIpxTotalTxSap = _MfrapPerfIpxTotalTxSap_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 10),
    _MfrapPerfIpxTotalTxSap_Type()
)
mfrapPerfIpxTotalTxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxSap.setStatus("mandatory")
_MfrapPerfIpxTotalRxRip_Type = Counter32
_MfrapPerfIpxTotalRxRip_Object = MibTableColumn
mfrapPerfIpxTotalRxRip = _MfrapPerfIpxTotalRxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 11),
    _MfrapPerfIpxTotalRxRip_Type()
)
mfrapPerfIpxTotalRxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxRip.setStatus("mandatory")
_MfrapPerfIpxTotalTxRip_Type = Counter32
_MfrapPerfIpxTotalTxRip_Object = MibTableColumn
mfrapPerfIpxTotalTxRip = _MfrapPerfIpxTotalTxRip_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 12),
    _MfrapPerfIpxTotalTxRip_Type()
)
mfrapPerfIpxTotalTxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxRip.setStatus("mandatory")
_MfrapPerfIpxTotalRxNetbios_Type = Counter32
_MfrapPerfIpxTotalRxNetbios_Object = MibTableColumn
mfrapPerfIpxTotalRxNetbios = _MfrapPerfIpxTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 13),
    _MfrapPerfIpxTotalRxNetbios_Type()
)
mfrapPerfIpxTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxNetbios.setStatus("mandatory")
_MfrapPerfIpxTotalTxNetbios_Type = Counter32
_MfrapPerfIpxTotalTxNetbios_Object = MibTableColumn
mfrapPerfIpxTotalTxNetbios = _MfrapPerfIpxTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 14),
    _MfrapPerfIpxTotalTxNetbios_Type()
)
mfrapPerfIpxTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxNetbios.setStatus("mandatory")
_MfrapPerfIpxTotalRxOther_Type = Counter32
_MfrapPerfIpxTotalRxOther_Object = MibTableColumn
mfrapPerfIpxTotalRxOther = _MfrapPerfIpxTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 15),
    _MfrapPerfIpxTotalRxOther_Type()
)
mfrapPerfIpxTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalRxOther.setStatus("mandatory")
_MfrapPerfIpxTotalTxOther_Type = Counter32
_MfrapPerfIpxTotalTxOther_Object = MibTableColumn
mfrapPerfIpxTotalTxOther = _MfrapPerfIpxTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 12, 1, 16),
    _MfrapPerfIpxTotalTxOther_Type()
)
mfrapPerfIpxTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfIpxTotalTxOther.setStatus("mandatory")
_MfrapPerfSnaPerDlciTable_Object = MibTable
mfrapPerfSnaPerDlciTable = _MfrapPerfSnaPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13)
)
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTable.setStatus("mandatory")
_MfrapPerfSnaPerDlciEntry_Object = MibTableRow
mfrapPerfSnaPerDlciEntry = _MfrapPerfSnaPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1)
)
mfrapPerfSnaPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfSnaPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfSnaPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciEntry.setStatus("mandatory")


class _MfrapPerfSnaPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfSnaPerDlciInterval based on Integer32"""
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


_MfrapPerfSnaPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfSnaPerDlciInterval_Object = MibTableColumn
mfrapPerfSnaPerDlciInterval = _MfrapPerfSnaPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 1),
    _MfrapPerfSnaPerDlciInterval_Type()
)
mfrapPerfSnaPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciInterval.setStatus("mandatory")
_MfrapPerfSnaPerDlciValue_Type = Integer32
_MfrapPerfSnaPerDlciValue_Object = MibTableColumn
mfrapPerfSnaPerDlciValue = _MfrapPerfSnaPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 2),
    _MfrapPerfSnaPerDlciValue_Type()
)
mfrapPerfSnaPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciValue.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxTotal_Type = Counter32
_MfrapPerfSnaPerDlciRxTotal_Object = MibTableColumn
mfrapPerfSnaPerDlciRxTotal = _MfrapPerfSnaPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 3),
    _MfrapPerfSnaPerDlciRxTotal_Type()
)
mfrapPerfSnaPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxTotal_Type = Counter32
_MfrapPerfSnaPerDlciTxTotal_Object = MibTableColumn
mfrapPerfSnaPerDlciTxTotal = _MfrapPerfSnaPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 4),
    _MfrapPerfSnaPerDlciTxTotal_Type()
)
mfrapPerfSnaPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxSubarea_Type = Counter32
_MfrapPerfSnaPerDlciRxSubarea_Object = MibTableColumn
mfrapPerfSnaPerDlciRxSubarea = _MfrapPerfSnaPerDlciRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 5),
    _MfrapPerfSnaPerDlciRxSubarea_Type()
)
mfrapPerfSnaPerDlciRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxSubarea.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxSubarea_Type = Counter32
_MfrapPerfSnaPerDlciTxSubarea_Object = MibTableColumn
mfrapPerfSnaPerDlciTxSubarea = _MfrapPerfSnaPerDlciTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 6),
    _MfrapPerfSnaPerDlciTxSubarea_Type()
)
mfrapPerfSnaPerDlciTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxSubarea.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxPeriph_Type = Counter32
_MfrapPerfSnaPerDlciRxPeriph_Object = MibTableColumn
mfrapPerfSnaPerDlciRxPeriph = _MfrapPerfSnaPerDlciRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 7),
    _MfrapPerfSnaPerDlciRxPeriph_Type()
)
mfrapPerfSnaPerDlciRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxPeriph.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxPeriph_Type = Counter32
_MfrapPerfSnaPerDlciTxPeriph_Object = MibTableColumn
mfrapPerfSnaPerDlciTxPeriph = _MfrapPerfSnaPerDlciTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 8),
    _MfrapPerfSnaPerDlciTxPeriph_Type()
)
mfrapPerfSnaPerDlciTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxPeriph.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxAppn_Type = Counter32
_MfrapPerfSnaPerDlciRxAppn_Object = MibTableColumn
mfrapPerfSnaPerDlciRxAppn = _MfrapPerfSnaPerDlciRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 9),
    _MfrapPerfSnaPerDlciRxAppn_Type()
)
mfrapPerfSnaPerDlciRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxAppn.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxAppn_Type = Counter32
_MfrapPerfSnaPerDlciTxAppn_Object = MibTableColumn
mfrapPerfSnaPerDlciTxAppn = _MfrapPerfSnaPerDlciTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 10),
    _MfrapPerfSnaPerDlciTxAppn_Type()
)
mfrapPerfSnaPerDlciTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxAppn.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxNetbios_Type = Counter32
_MfrapPerfSnaPerDlciRxNetbios_Object = MibTableColumn
mfrapPerfSnaPerDlciRxNetbios = _MfrapPerfSnaPerDlciRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 11),
    _MfrapPerfSnaPerDlciRxNetbios_Type()
)
mfrapPerfSnaPerDlciRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxNetbios.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxNetbios_Type = Counter32
_MfrapPerfSnaPerDlciTxNetbios_Object = MibTableColumn
mfrapPerfSnaPerDlciTxNetbios = _MfrapPerfSnaPerDlciTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 12),
    _MfrapPerfSnaPerDlciTxNetbios_Type()
)
mfrapPerfSnaPerDlciTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxNetbios.setStatus("mandatory")
_MfrapPerfSnaPerDlciRxOther_Type = Counter32
_MfrapPerfSnaPerDlciRxOther_Object = MibTableColumn
mfrapPerfSnaPerDlciRxOther = _MfrapPerfSnaPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 13),
    _MfrapPerfSnaPerDlciRxOther_Type()
)
mfrapPerfSnaPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciRxOther.setStatus("mandatory")
_MfrapPerfSnaPerDlciTxOther_Type = Counter32
_MfrapPerfSnaPerDlciTxOther_Object = MibTableColumn
mfrapPerfSnaPerDlciTxOther = _MfrapPerfSnaPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 13, 1, 14),
    _MfrapPerfSnaPerDlciTxOther_Type()
)
mfrapPerfSnaPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaPerDlciTxOther.setStatus("mandatory")
_MfrapPerfSnaTotalTable_Object = MibTable
mfrapPerfSnaTotalTable = _MfrapPerfSnaTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14)
)
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTable.setStatus("mandatory")
_MfrapPerfSnaTotalEntry_Object = MibTableRow
mfrapPerfSnaTotalEntry = _MfrapPerfSnaTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1)
)
mfrapPerfSnaTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfSnaTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalEntry.setStatus("mandatory")


class _MfrapPerfSnaTotalInterval_Type(Integer32):
    """Custom type mfrapPerfSnaTotalInterval based on Integer32"""
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


_MfrapPerfSnaTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfSnaTotalInterval_Object = MibTableColumn
mfrapPerfSnaTotalInterval = _MfrapPerfSnaTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 1),
    _MfrapPerfSnaTotalInterval_Type()
)
mfrapPerfSnaTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalInterval.setStatus("mandatory")
_MfrapPerfSnaTotalRxTotal_Type = Counter32
_MfrapPerfSnaTotalRxTotal_Object = MibTableColumn
mfrapPerfSnaTotalRxTotal = _MfrapPerfSnaTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 3),
    _MfrapPerfSnaTotalRxTotal_Type()
)
mfrapPerfSnaTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxTotal.setStatus("mandatory")
_MfrapPerfSnaTotalTxTotal_Type = Counter32
_MfrapPerfSnaTotalTxTotal_Object = MibTableColumn
mfrapPerfSnaTotalTxTotal = _MfrapPerfSnaTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 4),
    _MfrapPerfSnaTotalTxTotal_Type()
)
mfrapPerfSnaTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxTotal.setStatus("mandatory")
_MfrapPerfSnaTotalRxSubarea_Type = Counter32
_MfrapPerfSnaTotalRxSubarea_Object = MibTableColumn
mfrapPerfSnaTotalRxSubarea = _MfrapPerfSnaTotalRxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 5),
    _MfrapPerfSnaTotalRxSubarea_Type()
)
mfrapPerfSnaTotalRxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxSubarea.setStatus("mandatory")
_MfrapPerfSnaTotalTxSubarea_Type = Counter32
_MfrapPerfSnaTotalTxSubarea_Object = MibTableColumn
mfrapPerfSnaTotalTxSubarea = _MfrapPerfSnaTotalTxSubarea_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 6),
    _MfrapPerfSnaTotalTxSubarea_Type()
)
mfrapPerfSnaTotalTxSubarea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxSubarea.setStatus("mandatory")
_MfrapPerfSnaTotalRxPeriph_Type = Counter32
_MfrapPerfSnaTotalRxPeriph_Object = MibTableColumn
mfrapPerfSnaTotalRxPeriph = _MfrapPerfSnaTotalRxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 7),
    _MfrapPerfSnaTotalRxPeriph_Type()
)
mfrapPerfSnaTotalRxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxPeriph.setStatus("mandatory")
_MfrapPerfSnaTotalTxPeriph_Type = Counter32
_MfrapPerfSnaTotalTxPeriph_Object = MibTableColumn
mfrapPerfSnaTotalTxPeriph = _MfrapPerfSnaTotalTxPeriph_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 8),
    _MfrapPerfSnaTotalTxPeriph_Type()
)
mfrapPerfSnaTotalTxPeriph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxPeriph.setStatus("mandatory")
_MfrapPerfSnaTotalRxAppn_Type = Counter32
_MfrapPerfSnaTotalRxAppn_Object = MibTableColumn
mfrapPerfSnaTotalRxAppn = _MfrapPerfSnaTotalRxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 9),
    _MfrapPerfSnaTotalRxAppn_Type()
)
mfrapPerfSnaTotalRxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxAppn.setStatus("mandatory")
_MfrapPerfSnaTotalTxAppn_Type = Counter32
_MfrapPerfSnaTotalTxAppn_Object = MibTableColumn
mfrapPerfSnaTotalTxAppn = _MfrapPerfSnaTotalTxAppn_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 10),
    _MfrapPerfSnaTotalTxAppn_Type()
)
mfrapPerfSnaTotalTxAppn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxAppn.setStatus("mandatory")
_MfrapPerfSnaTotalRxNetbios_Type = Counter32
_MfrapPerfSnaTotalRxNetbios_Object = MibTableColumn
mfrapPerfSnaTotalRxNetbios = _MfrapPerfSnaTotalRxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 11),
    _MfrapPerfSnaTotalRxNetbios_Type()
)
mfrapPerfSnaTotalRxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxNetbios.setStatus("mandatory")
_MfrapPerfSnaTotalTxNetbios_Type = Counter32
_MfrapPerfSnaTotalTxNetbios_Object = MibTableColumn
mfrapPerfSnaTotalTxNetbios = _MfrapPerfSnaTotalTxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 12),
    _MfrapPerfSnaTotalTxNetbios_Type()
)
mfrapPerfSnaTotalTxNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxNetbios.setStatus("mandatory")
_MfrapPerfSnaTotalRxOther_Type = Counter32
_MfrapPerfSnaTotalRxOther_Object = MibTableColumn
mfrapPerfSnaTotalRxOther = _MfrapPerfSnaTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 13),
    _MfrapPerfSnaTotalRxOther_Type()
)
mfrapPerfSnaTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalRxOther.setStatus("mandatory")
_MfrapPerfSnaTotalTxOther_Type = Counter32
_MfrapPerfSnaTotalTxOther_Object = MibTableColumn
mfrapPerfSnaTotalTxOther = _MfrapPerfSnaTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 14, 1, 14),
    _MfrapPerfSnaTotalTxOther_Type()
)
mfrapPerfSnaTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfSnaTotalTxOther.setStatus("mandatory")
_MfrapPerfArpPerDlciTable_Object = MibTable
mfrapPerfArpPerDlciTable = _MfrapPerfArpPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15)
)
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTable.setStatus("mandatory")
_MfrapPerfArpPerDlciEntry_Object = MibTableRow
mfrapPerfArpPerDlciEntry = _MfrapPerfArpPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1)
)
mfrapPerfArpPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfArpPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfArpPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciEntry.setStatus("mandatory")


class _MfrapPerfArpPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfArpPerDlciInterval based on Integer32"""
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


_MfrapPerfArpPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfArpPerDlciInterval_Object = MibTableColumn
mfrapPerfArpPerDlciInterval = _MfrapPerfArpPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 1),
    _MfrapPerfArpPerDlciInterval_Type()
)
mfrapPerfArpPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciInterval.setStatus("mandatory")
_MfrapPerfArpPerDlciValue_Type = Integer32
_MfrapPerfArpPerDlciValue_Object = MibTableColumn
mfrapPerfArpPerDlciValue = _MfrapPerfArpPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 2),
    _MfrapPerfArpPerDlciValue_Type()
)
mfrapPerfArpPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciValue.setStatus("mandatory")
_MfrapPerfArpPerDlciRxTotal_Type = Counter32
_MfrapPerfArpPerDlciRxTotal_Object = MibTableColumn
mfrapPerfArpPerDlciRxTotal = _MfrapPerfArpPerDlciRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 3),
    _MfrapPerfArpPerDlciRxTotal_Type()
)
mfrapPerfArpPerDlciRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxTotal.setStatus("mandatory")
_MfrapPerfArpPerDlciTxTotal_Type = Counter32
_MfrapPerfArpPerDlciTxTotal_Object = MibTableColumn
mfrapPerfArpPerDlciTxTotal = _MfrapPerfArpPerDlciTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 4),
    _MfrapPerfArpPerDlciTxTotal_Type()
)
mfrapPerfArpPerDlciTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxTotal.setStatus("mandatory")
_MfrapPerfArpPerDlciRxArpReq_Type = Counter32
_MfrapPerfArpPerDlciRxArpReq_Object = MibTableColumn
mfrapPerfArpPerDlciRxArpReq = _MfrapPerfArpPerDlciRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 5),
    _MfrapPerfArpPerDlciRxArpReq_Type()
)
mfrapPerfArpPerDlciRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxArpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciTxArpReq_Type = Counter32
_MfrapPerfArpPerDlciTxArpReq_Object = MibTableColumn
mfrapPerfArpPerDlciTxArpReq = _MfrapPerfArpPerDlciTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 6),
    _MfrapPerfArpPerDlciTxArpReq_Type()
)
mfrapPerfArpPerDlciTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxArpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciRxArpRep_Type = Counter32
_MfrapPerfArpPerDlciRxArpRep_Object = MibTableColumn
mfrapPerfArpPerDlciRxArpRep = _MfrapPerfArpPerDlciRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 7),
    _MfrapPerfArpPerDlciRxArpRep_Type()
)
mfrapPerfArpPerDlciRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxArpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciTxArpRep_Type = Counter32
_MfrapPerfArpPerDlciTxArpRep_Object = MibTableColumn
mfrapPerfArpPerDlciTxArpRep = _MfrapPerfArpPerDlciTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 8),
    _MfrapPerfArpPerDlciTxArpRep_Type()
)
mfrapPerfArpPerDlciTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxArpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciRxRarpReq_Type = Counter32
_MfrapPerfArpPerDlciRxRarpReq_Object = MibTableColumn
mfrapPerfArpPerDlciRxRarpReq = _MfrapPerfArpPerDlciRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 9),
    _MfrapPerfArpPerDlciRxRarpReq_Type()
)
mfrapPerfArpPerDlciRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxRarpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciTxRarpReq_Type = Counter32
_MfrapPerfArpPerDlciTxRarpReq_Object = MibTableColumn
mfrapPerfArpPerDlciTxRarpReq = _MfrapPerfArpPerDlciTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 10),
    _MfrapPerfArpPerDlciTxRarpReq_Type()
)
mfrapPerfArpPerDlciTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxRarpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciRxRarpRep_Type = Counter32
_MfrapPerfArpPerDlciRxRarpRep_Object = MibTableColumn
mfrapPerfArpPerDlciRxRarpRep = _MfrapPerfArpPerDlciRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 11),
    _MfrapPerfArpPerDlciRxRarpRep_Type()
)
mfrapPerfArpPerDlciRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxRarpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciTxRarpRep_Type = Counter32
_MfrapPerfArpPerDlciTxRarpRep_Object = MibTableColumn
mfrapPerfArpPerDlciTxRarpRep = _MfrapPerfArpPerDlciTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 12),
    _MfrapPerfArpPerDlciTxRarpRep_Type()
)
mfrapPerfArpPerDlciTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxRarpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciRxInarpReq_Type = Counter32
_MfrapPerfArpPerDlciRxInarpReq_Object = MibTableColumn
mfrapPerfArpPerDlciRxInarpReq = _MfrapPerfArpPerDlciRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 13),
    _MfrapPerfArpPerDlciRxInarpReq_Type()
)
mfrapPerfArpPerDlciRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxInarpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciTxInarpReq_Type = Counter32
_MfrapPerfArpPerDlciTxInarpReq_Object = MibTableColumn
mfrapPerfArpPerDlciTxInarpReq = _MfrapPerfArpPerDlciTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 14),
    _MfrapPerfArpPerDlciTxInarpReq_Type()
)
mfrapPerfArpPerDlciTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxInarpReq.setStatus("mandatory")
_MfrapPerfArpPerDlciRxInarpRep_Type = Counter32
_MfrapPerfArpPerDlciRxInarpRep_Object = MibTableColumn
mfrapPerfArpPerDlciRxInarpRep = _MfrapPerfArpPerDlciRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 15),
    _MfrapPerfArpPerDlciRxInarpRep_Type()
)
mfrapPerfArpPerDlciRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxInarpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciTxInarpRep_Type = Counter32
_MfrapPerfArpPerDlciTxInarpRep_Object = MibTableColumn
mfrapPerfArpPerDlciTxInarpRep = _MfrapPerfArpPerDlciTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 16),
    _MfrapPerfArpPerDlciTxInarpRep_Type()
)
mfrapPerfArpPerDlciTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxInarpRep.setStatus("mandatory")
_MfrapPerfArpPerDlciRxOther_Type = Counter32
_MfrapPerfArpPerDlciRxOther_Object = MibTableColumn
mfrapPerfArpPerDlciRxOther = _MfrapPerfArpPerDlciRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 17),
    _MfrapPerfArpPerDlciRxOther_Type()
)
mfrapPerfArpPerDlciRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciRxOther.setStatus("mandatory")
_MfrapPerfArpPerDlciTxOther_Type = Counter32
_MfrapPerfArpPerDlciTxOther_Object = MibTableColumn
mfrapPerfArpPerDlciTxOther = _MfrapPerfArpPerDlciTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 15, 1, 18),
    _MfrapPerfArpPerDlciTxOther_Type()
)
mfrapPerfArpPerDlciTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpPerDlciTxOther.setStatus("mandatory")
_MfrapPerfArpTotalTable_Object = MibTable
mfrapPerfArpTotalTable = _MfrapPerfArpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16)
)
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTable.setStatus("mandatory")
_MfrapPerfArpTotalEntry_Object = MibTableRow
mfrapPerfArpTotalEntry = _MfrapPerfArpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1)
)
mfrapPerfArpTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfArpTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfArpTotalEntry.setStatus("mandatory")


class _MfrapPerfArpTotalInterval_Type(Integer32):
    """Custom type mfrapPerfArpTotalInterval based on Integer32"""
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


_MfrapPerfArpTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfArpTotalInterval_Object = MibTableColumn
mfrapPerfArpTotalInterval = _MfrapPerfArpTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 1),
    _MfrapPerfArpTotalInterval_Type()
)
mfrapPerfArpTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalInterval.setStatus("mandatory")
_MfrapPerfArpTotalRxTotal_Type = Counter32
_MfrapPerfArpTotalRxTotal_Object = MibTableColumn
mfrapPerfArpTotalRxTotal = _MfrapPerfArpTotalRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 3),
    _MfrapPerfArpTotalRxTotal_Type()
)
mfrapPerfArpTotalRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxTotal.setStatus("mandatory")
_MfrapPerfArpTotalTxTotal_Type = Counter32
_MfrapPerfArpTotalTxTotal_Object = MibTableColumn
mfrapPerfArpTotalTxTotal = _MfrapPerfArpTotalTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 4),
    _MfrapPerfArpTotalTxTotal_Type()
)
mfrapPerfArpTotalTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxTotal.setStatus("mandatory")
_MfrapPerfArpTotalRxArpReq_Type = Counter32
_MfrapPerfArpTotalRxArpReq_Object = MibTableColumn
mfrapPerfArpTotalRxArpReq = _MfrapPerfArpTotalRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 5),
    _MfrapPerfArpTotalRxArpReq_Type()
)
mfrapPerfArpTotalRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxArpReq.setStatus("mandatory")
_MfrapPerfArpTotalTxArpReq_Type = Counter32
_MfrapPerfArpTotalTxArpReq_Object = MibTableColumn
mfrapPerfArpTotalTxArpReq = _MfrapPerfArpTotalTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 6),
    _MfrapPerfArpTotalTxArpReq_Type()
)
mfrapPerfArpTotalTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxArpReq.setStatus("mandatory")
_MfrapPerfArpTotalRxArpRep_Type = Counter32
_MfrapPerfArpTotalRxArpRep_Object = MibTableColumn
mfrapPerfArpTotalRxArpRep = _MfrapPerfArpTotalRxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 7),
    _MfrapPerfArpTotalRxArpRep_Type()
)
mfrapPerfArpTotalRxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxArpRep.setStatus("mandatory")
_MfrapPerfArpTotalTxArpRep_Type = Counter32
_MfrapPerfArpTotalTxArpRep_Object = MibTableColumn
mfrapPerfArpTotalTxArpRep = _MfrapPerfArpTotalTxArpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 8),
    _MfrapPerfArpTotalTxArpRep_Type()
)
mfrapPerfArpTotalTxArpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxArpRep.setStatus("mandatory")
_MfrapPerfArpTotalRxRarpReq_Type = Counter32
_MfrapPerfArpTotalRxRarpReq_Object = MibTableColumn
mfrapPerfArpTotalRxRarpReq = _MfrapPerfArpTotalRxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 9),
    _MfrapPerfArpTotalRxRarpReq_Type()
)
mfrapPerfArpTotalRxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxRarpReq.setStatus("mandatory")
_MfrapPerfArpTotalTxRarpReq_Type = Counter32
_MfrapPerfArpTotalTxRarpReq_Object = MibTableColumn
mfrapPerfArpTotalTxRarpReq = _MfrapPerfArpTotalTxRarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 10),
    _MfrapPerfArpTotalTxRarpReq_Type()
)
mfrapPerfArpTotalTxRarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxRarpReq.setStatus("mandatory")
_MfrapPerfArpTotalRxRarpRep_Type = Counter32
_MfrapPerfArpTotalRxRarpRep_Object = MibTableColumn
mfrapPerfArpTotalRxRarpRep = _MfrapPerfArpTotalRxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 11),
    _MfrapPerfArpTotalRxRarpRep_Type()
)
mfrapPerfArpTotalRxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxRarpRep.setStatus("mandatory")
_MfrapPerfArpTotalTxRarpRep_Type = Counter32
_MfrapPerfArpTotalTxRarpRep_Object = MibTableColumn
mfrapPerfArpTotalTxRarpRep = _MfrapPerfArpTotalTxRarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 12),
    _MfrapPerfArpTotalTxRarpRep_Type()
)
mfrapPerfArpTotalTxRarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxRarpRep.setStatus("mandatory")
_MfrapPerfArpTotalRxInarpReq_Type = Counter32
_MfrapPerfArpTotalRxInarpReq_Object = MibTableColumn
mfrapPerfArpTotalRxInarpReq = _MfrapPerfArpTotalRxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 13),
    _MfrapPerfArpTotalRxInarpReq_Type()
)
mfrapPerfArpTotalRxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxInarpReq.setStatus("mandatory")
_MfrapPerfArpTotalTxInarpReq_Type = Counter32
_MfrapPerfArpTotalTxInarpReq_Object = MibTableColumn
mfrapPerfArpTotalTxInarpReq = _MfrapPerfArpTotalTxInarpReq_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 14),
    _MfrapPerfArpTotalTxInarpReq_Type()
)
mfrapPerfArpTotalTxInarpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxInarpReq.setStatus("mandatory")
_MfrapPerfArpTotalRxInarpRep_Type = Counter32
_MfrapPerfArpTotalRxInarpRep_Object = MibTableColumn
mfrapPerfArpTotalRxInarpRep = _MfrapPerfArpTotalRxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 15),
    _MfrapPerfArpTotalRxInarpRep_Type()
)
mfrapPerfArpTotalRxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxInarpRep.setStatus("mandatory")
_MfrapPerfArpTotalTxInarpRep_Type = Counter32
_MfrapPerfArpTotalTxInarpRep_Object = MibTableColumn
mfrapPerfArpTotalTxInarpRep = _MfrapPerfArpTotalTxInarpRep_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 16),
    _MfrapPerfArpTotalTxInarpRep_Type()
)
mfrapPerfArpTotalTxInarpRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxInarpRep.setStatus("mandatory")
_MfrapPerfArpTotalRxOther_Type = Counter32
_MfrapPerfArpTotalRxOther_Object = MibTableColumn
mfrapPerfArpTotalRxOther = _MfrapPerfArpTotalRxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 17),
    _MfrapPerfArpTotalRxOther_Type()
)
mfrapPerfArpTotalRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalRxOther.setStatus("mandatory")
_MfrapPerfArpTotalTxOther_Type = Counter32
_MfrapPerfArpTotalTxOther_Object = MibTableColumn
mfrapPerfArpTotalTxOther = _MfrapPerfArpTotalTxOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 16, 1, 18),
    _MfrapPerfArpTotalTxOther_Type()
)
mfrapPerfArpTotalTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfArpTotalTxOther.setStatus("mandatory")
_MfrapPerfLmiPerDlciTable_Object = MibTable
mfrapPerfLmiPerDlciTable = _MfrapPerfLmiPerDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17)
)
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTable.setStatus("mandatory")
_MfrapPerfLmiPerDlciEntry_Object = MibTableRow
mfrapPerfLmiPerDlciEntry = _MfrapPerfLmiPerDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1)
)
mfrapPerfLmiPerDlciEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfLmiPerDlciInterval"),
    (0, "MFRAP-MIB", "mfrapPerfLmiPerDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciEntry.setStatus("mandatory")


class _MfrapPerfLmiPerDlciInterval_Type(Integer32):
    """Custom type mfrapPerfLmiPerDlciInterval based on Integer32"""
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


_MfrapPerfLmiPerDlciInterval_Type.__name__ = "Integer32"
_MfrapPerfLmiPerDlciInterval_Object = MibTableColumn
mfrapPerfLmiPerDlciInterval = _MfrapPerfLmiPerDlciInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 1),
    _MfrapPerfLmiPerDlciInterval_Type()
)
mfrapPerfLmiPerDlciInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciInterval.setStatus("mandatory")
_MfrapPerfLmiPerDlciValue_Type = Integer32
_MfrapPerfLmiPerDlciValue_Object = MibTableColumn
mfrapPerfLmiPerDlciValue = _MfrapPerfLmiPerDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 2),
    _MfrapPerfLmiPerDlciValue_Type()
)
mfrapPerfLmiPerDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciValue.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxTotalByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxTotalByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxTotalByteCnt = _MfrapPerfLmiPerDlciRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 3),
    _MfrapPerfLmiPerDlciRxTotalByteCnt_Type()
)
mfrapPerfLmiPerDlciRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxTotalByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxTotalByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxTotalByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxTotalByteCnt = _MfrapPerfLmiPerDlciTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 4),
    _MfrapPerfLmiPerDlciTxTotalByteCnt_Type()
)
mfrapPerfLmiPerDlciTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxTotalByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxLivoEnqByteCnt = _MfrapPerfLmiPerDlciRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 5),
    _MfrapPerfLmiPerDlciRxLivoEnqByteCnt_Type()
)
mfrapPerfLmiPerDlciRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxLivoEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxLivoEnqByteCnt = _MfrapPerfLmiPerDlciTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 6),
    _MfrapPerfLmiPerDlciTxLivoEnqByteCnt_Type()
)
mfrapPerfLmiPerDlciTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxLivoEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxLivoStatByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxLivoStatByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxLivoStatByteCnt = _MfrapPerfLmiPerDlciRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 7),
    _MfrapPerfLmiPerDlciRxLivoStatByteCnt_Type()
)
mfrapPerfLmiPerDlciRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxLivoStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxLivoStatByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxLivoStatByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxLivoStatByteCnt = _MfrapPerfLmiPerDlciTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 8),
    _MfrapPerfLmiPerDlciTxLivoStatByteCnt_Type()
)
mfrapPerfLmiPerDlciTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxLivoStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxFullEnqByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxFullEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxFullEnqByteCnt = _MfrapPerfLmiPerDlciRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 9),
    _MfrapPerfLmiPerDlciRxFullEnqByteCnt_Type()
)
mfrapPerfLmiPerDlciRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxFullEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxFullEnqByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxFullEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxFullEnqByteCnt = _MfrapPerfLmiPerDlciTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 10),
    _MfrapPerfLmiPerDlciTxFullEnqByteCnt_Type()
)
mfrapPerfLmiPerDlciTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxFullEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxFullStatByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxFullStatByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxFullStatByteCnt = _MfrapPerfLmiPerDlciRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 11),
    _MfrapPerfLmiPerDlciRxFullStatByteCnt_Type()
)
mfrapPerfLmiPerDlciRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxFullStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxFullStatByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxFullStatByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxFullStatByteCnt = _MfrapPerfLmiPerDlciTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 12),
    _MfrapPerfLmiPerDlciTxFullStatByteCnt_Type()
)
mfrapPerfLmiPerDlciTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxFullStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciRxOtherByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciRxOtherByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciRxOtherByteCnt = _MfrapPerfLmiPerDlciRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 13),
    _MfrapPerfLmiPerDlciRxOtherByteCnt_Type()
)
mfrapPerfLmiPerDlciRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciRxOtherByteCnt.setStatus("mandatory")
_MfrapPerfLmiPerDlciTxOtherByteCnt_Type = Counter32
_MfrapPerfLmiPerDlciTxOtherByteCnt_Object = MibTableColumn
mfrapPerfLmiPerDlciTxOtherByteCnt = _MfrapPerfLmiPerDlciTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 17, 1, 14),
    _MfrapPerfLmiPerDlciTxOtherByteCnt_Type()
)
mfrapPerfLmiPerDlciTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiPerDlciTxOtherByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTable_Object = MibTable
mfrapPerfLmiTotalTable = _MfrapPerfLmiTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18)
)
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTable.setStatus("mandatory")
_MfrapPerfLmiTotalEntry_Object = MibTableRow
mfrapPerfLmiTotalEntry = _MfrapPerfLmiTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1)
)
mfrapPerfLmiTotalEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfLmiTotalInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalEntry.setStatus("mandatory")


class _MfrapPerfLmiTotalInterval_Type(Integer32):
    """Custom type mfrapPerfLmiTotalInterval based on Integer32"""
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


_MfrapPerfLmiTotalInterval_Type.__name__ = "Integer32"
_MfrapPerfLmiTotalInterval_Object = MibTableColumn
mfrapPerfLmiTotalInterval = _MfrapPerfLmiTotalInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 1),
    _MfrapPerfLmiTotalInterval_Type()
)
mfrapPerfLmiTotalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalInterval.setStatus("mandatory")
_MfrapPerfLmiTotalDlciValue_Type = Integer32
_MfrapPerfLmiTotalDlciValue_Object = MibTableColumn
mfrapPerfLmiTotalDlciValue = _MfrapPerfLmiTotalDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 2),
    _MfrapPerfLmiTotalDlciValue_Type()
)
mfrapPerfLmiTotalDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalDlciValue.setStatus("mandatory")
_MfrapPerfLmiTotalRxTotalByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxTotalByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxTotalByteCnt = _MfrapPerfLmiTotalRxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 3),
    _MfrapPerfLmiTotalRxTotalByteCnt_Type()
)
mfrapPerfLmiTotalRxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxTotalByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxTotalByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxTotalByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxTotalByteCnt = _MfrapPerfLmiTotalTxTotalByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 4),
    _MfrapPerfLmiTotalTxTotalByteCnt_Type()
)
mfrapPerfLmiTotalTxTotalByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxTotalByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalRxLivoEnqByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxLivoEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxLivoEnqByteCnt = _MfrapPerfLmiTotalRxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 5),
    _MfrapPerfLmiTotalRxLivoEnqByteCnt_Type()
)
mfrapPerfLmiTotalRxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxLivoEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxLivoEnqByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxLivoEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxLivoEnqByteCnt = _MfrapPerfLmiTotalTxLivoEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 6),
    _MfrapPerfLmiTotalTxLivoEnqByteCnt_Type()
)
mfrapPerfLmiTotalTxLivoEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxLivoEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalRxLivoStatByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxLivoStatByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxLivoStatByteCnt = _MfrapPerfLmiTotalRxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 7),
    _MfrapPerfLmiTotalRxLivoStatByteCnt_Type()
)
mfrapPerfLmiTotalRxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxLivoStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxLivoStatByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxLivoStatByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxLivoStatByteCnt = _MfrapPerfLmiTotalTxLivoStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 8),
    _MfrapPerfLmiTotalTxLivoStatByteCnt_Type()
)
mfrapPerfLmiTotalTxLivoStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxLivoStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalRxFullEnqByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxFullEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxFullEnqByteCnt = _MfrapPerfLmiTotalRxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 9),
    _MfrapPerfLmiTotalRxFullEnqByteCnt_Type()
)
mfrapPerfLmiTotalRxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxFullEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxFullEnqByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxFullEnqByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxFullEnqByteCnt = _MfrapPerfLmiTotalTxFullEnqByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 10),
    _MfrapPerfLmiTotalTxFullEnqByteCnt_Type()
)
mfrapPerfLmiTotalTxFullEnqByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxFullEnqByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalRxFullStatByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxFullStatByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxFullStatByteCnt = _MfrapPerfLmiTotalRxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 11),
    _MfrapPerfLmiTotalRxFullStatByteCnt_Type()
)
mfrapPerfLmiTotalRxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxFullStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxFullStatByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxFullStatByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxFullStatByteCnt = _MfrapPerfLmiTotalTxFullStatByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 12),
    _MfrapPerfLmiTotalTxFullStatByteCnt_Type()
)
mfrapPerfLmiTotalTxFullStatByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxFullStatByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalRxOtherByteCnt_Type = Counter32
_MfrapPerfLmiTotalRxOtherByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalRxOtherByteCnt = _MfrapPerfLmiTotalRxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 13),
    _MfrapPerfLmiTotalRxOtherByteCnt_Type()
)
mfrapPerfLmiTotalRxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalRxOtherByteCnt.setStatus("mandatory")
_MfrapPerfLmiTotalTxOtherByteCnt_Type = Counter32
_MfrapPerfLmiTotalTxOtherByteCnt_Object = MibTableColumn
mfrapPerfLmiTotalTxOtherByteCnt = _MfrapPerfLmiTotalTxOtherByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 4, 18, 1, 14),
    _MfrapPerfLmiTotalTxOtherByteCnt_Type()
)
mfrapPerfLmiTotalTxOtherByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfLmiTotalTxOtherByteCnt.setStatus("mandatory")
_MfrapPerfNetworkLongTerm_ObjectIdentity = ObjectIdentity
mfrapPerfNetworkLongTerm = _MfrapPerfNetworkLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5)
)
_MfrapPerfNetwLongTermTable_Object = MibTable
mfrapPerfNetwLongTermTable = _MfrapPerfNetwLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermTable.setStatus("mandatory")
_MfrapPerfNetwLongTermEntry_Object = MibTableRow
mfrapPerfNetwLongTermEntry = _MfrapPerfNetwLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1, 1)
)
mfrapPerfNetwLongTermEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfNetwLongTermDlci"),
    (0, "MFRAP-MIB", "mfrapPerfNetwLongTermProtocol"),
    (0, "MFRAP-MIB", "mfrapPerfNetwLongTermInterval"),
)
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermEntry.setStatus("mandatory")
_MfrapPerfNetwLongTermDlci_Type = Integer32
_MfrapPerfNetwLongTermDlci_Object = MibTableColumn
mfrapPerfNetwLongTermDlci = _MfrapPerfNetwLongTermDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1, 1, 1),
    _MfrapPerfNetwLongTermDlci_Type()
)
mfrapPerfNetwLongTermDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermDlci.setStatus("mandatory")


class _MfrapPerfNetwLongTermProtocol_Type(Integer32):
    """Custom type mfrapPerfNetwLongTermProtocol based on Integer32"""
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


_MfrapPerfNetwLongTermProtocol_Type.__name__ = "Integer32"
_MfrapPerfNetwLongTermProtocol_Object = MibTableColumn
mfrapPerfNetwLongTermProtocol = _MfrapPerfNetwLongTermProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1, 1, 2),
    _MfrapPerfNetwLongTermProtocol_Type()
)
mfrapPerfNetwLongTermProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermProtocol.setStatus("mandatory")
_MfrapPerfNetwLongTermInterval_Type = Integer32
_MfrapPerfNetwLongTermInterval_Object = MibTableColumn
mfrapPerfNetwLongTermInterval = _MfrapPerfNetwLongTermInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1, 1, 3),
    _MfrapPerfNetwLongTermInterval_Type()
)
mfrapPerfNetwLongTermInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermInterval.setStatus("mandatory")
_MfrapPerfNetwLongTermValue_Type = Counter32
_MfrapPerfNetwLongTermValue_Object = MibTableColumn
mfrapPerfNetwLongTermValue = _MfrapPerfNetwLongTermValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 1, 1, 4),
    _MfrapPerfNetwLongTermValue_Type()
)
mfrapPerfNetwLongTermValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermValue.setStatus("mandatory")
_MfrapPerfNetwLongTermAltTable_Object = MibTable
mfrapPerfNetwLongTermAltTable = _MfrapPerfNetwLongTermAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 2)
)
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermAltTable.setStatus("mandatory")
_MfrapPerfNetwLongTermAltEntry_Object = MibTableRow
mfrapPerfNetwLongTermAltEntry = _MfrapPerfNetwLongTermAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 2, 1)
)
mfrapPerfNetwLongTermAltEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfNetwLongTermAltDlci"),
    (0, "MFRAP-MIB", "mfrapPerfNetwLongTermAltProtocol"),
)
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermAltEntry.setStatus("mandatory")
_MfrapPerfNetwLongTermAltDlci_Type = Integer32
_MfrapPerfNetwLongTermAltDlci_Object = MibTableColumn
mfrapPerfNetwLongTermAltDlci = _MfrapPerfNetwLongTermAltDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 2, 1, 1),
    _MfrapPerfNetwLongTermAltDlci_Type()
)
mfrapPerfNetwLongTermAltDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermAltDlci.setStatus("mandatory")


class _MfrapPerfNetwLongTermAltProtocol_Type(Integer32):
    """Custom type mfrapPerfNetwLongTermAltProtocol based on Integer32"""
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


_MfrapPerfNetwLongTermAltProtocol_Type.__name__ = "Integer32"
_MfrapPerfNetwLongTermAltProtocol_Object = MibTableColumn
mfrapPerfNetwLongTermAltProtocol = _MfrapPerfNetwLongTermAltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 2, 1, 2),
    _MfrapPerfNetwLongTermAltProtocol_Type()
)
mfrapPerfNetwLongTermAltProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermAltProtocol.setStatus("mandatory")
_MfrapPerfNetwLongTermAltArray_Type = OctetString
_MfrapPerfNetwLongTermAltArray_Object = MibTableColumn
mfrapPerfNetwLongTermAltArray = _MfrapPerfNetwLongTermAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 2, 1, 3),
    _MfrapPerfNetwLongTermAltArray_Type()
)
mfrapPerfNetwLongTermAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfNetwLongTermAltArray.setStatus("mandatory")
_MfrapPerfNetworkLongTermCommands_ObjectIdentity = ObjectIdentity
mfrapPerfNetworkLongTermCommands = _MfrapPerfNetworkLongTermCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 3)
)


class _MfrapPerfNetworkLongTermCmdClear_Type(Integer32):
    """Custom type mfrapPerfNetworkLongTermCmdClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_MfrapPerfNetworkLongTermCmdClear_Type.__name__ = "Integer32"
_MfrapPerfNetworkLongTermCmdClear_Object = MibScalar
mfrapPerfNetworkLongTermCmdClear = _MfrapPerfNetworkLongTermCmdClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 5, 3, 1),
    _MfrapPerfNetworkLongTermCmdClear_Type()
)
mfrapPerfNetworkLongTermCmdClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapPerfNetworkLongTermCmdClear.setStatus("mandatory")
_MfrapPerfCirPercentUtilization_ObjectIdentity = ObjectIdentity
mfrapPerfCirPercentUtilization = _MfrapPerfCirPercentUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6)
)
_MfrapPerfCirPercentUtilizationTable_Object = MibTable
mfrapPerfCirPercentUtilizationTable = _MfrapPerfCirPercentUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mfrapPerfCirPercentUtilizationTable.setStatus("mandatory")
_MfrapPerfCirPercentUtilizationEntry_Object = MibTableRow
mfrapPerfCirPercentUtilizationEntry = _MfrapPerfCirPercentUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1)
)
mfrapPerfCirPercentUtilizationEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfCirPercentUtilizationInterval"),
    (0, "MFRAP-MIB", "mfrapPerfCirPercentUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfCirPercentUtilizationEntry.setStatus("mandatory")


class _MfrapPerfCirPercentUtilizationInterval_Type(Integer32):
    """Custom type mfrapPerfCirPercentUtilizationInterval based on Integer32"""
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


_MfrapPerfCirPercentUtilizationInterval_Type.__name__ = "Integer32"
_MfrapPerfCirPercentUtilizationInterval_Object = MibTableColumn
mfrapPerfCirPercentUtilizationInterval = _MfrapPerfCirPercentUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 1),
    _MfrapPerfCirPercentUtilizationInterval_Type()
)
mfrapPerfCirPercentUtilizationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirPercentUtilizationInterval.setStatus("mandatory")
_MfrapPerfCirPercentUtilizationDlciValue_Type = Integer32
_MfrapPerfCirPercentUtilizationDlciValue_Object = MibTableColumn
mfrapPerfCirPercentUtilizationDlciValue = _MfrapPerfCirPercentUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 2),
    _MfrapPerfCirPercentUtilizationDlciValue_Type()
)
mfrapPerfCirPercentUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirPercentUtilizationDlciValue.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange1_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange1_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange1 = _MfrapPerfCirRxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 21),
    _MfrapPerfCirRxPercentUtilizationRange1_Type()
)
mfrapPerfCirRxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange1.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange2_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange2_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange2 = _MfrapPerfCirRxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 22),
    _MfrapPerfCirRxPercentUtilizationRange2_Type()
)
mfrapPerfCirRxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange2.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange3_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange3_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange3 = _MfrapPerfCirRxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 23),
    _MfrapPerfCirRxPercentUtilizationRange3_Type()
)
mfrapPerfCirRxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange3.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange4_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange4_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange4 = _MfrapPerfCirRxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 24),
    _MfrapPerfCirRxPercentUtilizationRange4_Type()
)
mfrapPerfCirRxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange4.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange5_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange5_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange5 = _MfrapPerfCirRxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 25),
    _MfrapPerfCirRxPercentUtilizationRange5_Type()
)
mfrapPerfCirRxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange5.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange6_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange6_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange6 = _MfrapPerfCirRxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 26),
    _MfrapPerfCirRxPercentUtilizationRange6_Type()
)
mfrapPerfCirRxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange6.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange7_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange7_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange7 = _MfrapPerfCirRxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 27),
    _MfrapPerfCirRxPercentUtilizationRange7_Type()
)
mfrapPerfCirRxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange7.setStatus("mandatory")
_MfrapPerfCirRxPercentUtilizationRange8_Type = Integer32
_MfrapPerfCirRxPercentUtilizationRange8_Object = MibTableColumn
mfrapPerfCirRxPercentUtilizationRange8 = _MfrapPerfCirRxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 28),
    _MfrapPerfCirRxPercentUtilizationRange8_Type()
)
mfrapPerfCirRxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirRxPercentUtilizationRange8.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange1_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange1_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange1 = _MfrapPerfCirTxPercentUtilizationRange1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 41),
    _MfrapPerfCirTxPercentUtilizationRange1_Type()
)
mfrapPerfCirTxPercentUtilizationRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange1.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange2_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange2_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange2 = _MfrapPerfCirTxPercentUtilizationRange2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 42),
    _MfrapPerfCirTxPercentUtilizationRange2_Type()
)
mfrapPerfCirTxPercentUtilizationRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange2.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange3_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange3_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange3 = _MfrapPerfCirTxPercentUtilizationRange3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 43),
    _MfrapPerfCirTxPercentUtilizationRange3_Type()
)
mfrapPerfCirTxPercentUtilizationRange3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange3.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange4_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange4_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange4 = _MfrapPerfCirTxPercentUtilizationRange4_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 44),
    _MfrapPerfCirTxPercentUtilizationRange4_Type()
)
mfrapPerfCirTxPercentUtilizationRange4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange4.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange5_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange5_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange5 = _MfrapPerfCirTxPercentUtilizationRange5_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 45),
    _MfrapPerfCirTxPercentUtilizationRange5_Type()
)
mfrapPerfCirTxPercentUtilizationRange5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange5.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange6_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange6_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange6 = _MfrapPerfCirTxPercentUtilizationRange6_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 46),
    _MfrapPerfCirTxPercentUtilizationRange6_Type()
)
mfrapPerfCirTxPercentUtilizationRange6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange6.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange7_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange7_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange7 = _MfrapPerfCirTxPercentUtilizationRange7_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 47),
    _MfrapPerfCirTxPercentUtilizationRange7_Type()
)
mfrapPerfCirTxPercentUtilizationRange7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange7.setStatus("mandatory")
_MfrapPerfCirTxPercentUtilizationRange8_Type = Integer32
_MfrapPerfCirTxPercentUtilizationRange8_Object = MibTableColumn
mfrapPerfCirTxPercentUtilizationRange8 = _MfrapPerfCirTxPercentUtilizationRange8_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 1, 1, 48),
    _MfrapPerfCirTxPercentUtilizationRange8_Type()
)
mfrapPerfCirTxPercentUtilizationRange8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCirTxPercentUtilizationRange8.setStatus("mandatory")
_MfrapPerfCurrentPerDlciUtilizationTable_Object = MibTable
mfrapPerfCurrentPerDlciUtilizationTable = _MfrapPerfCurrentPerDlciUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2)
)
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciUtilizationTable.setStatus("mandatory")
_MfrapPerfCurrentPerDlciUtilizationEntry_Object = MibTableRow
mfrapPerfCurrentPerDlciUtilizationEntry = _MfrapPerfCurrentPerDlciUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2, 1)
)
mfrapPerfCurrentPerDlciUtilizationEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapPerfCurrentPerDlciUtilizationDlciValue"),
)
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciUtilizationEntry.setStatus("mandatory")
_MfrapPerfCurrentPerDlciUtilizationDlciValue_Type = Integer32
_MfrapPerfCurrentPerDlciUtilizationDlciValue_Object = MibTableColumn
mfrapPerfCurrentPerDlciUtilizationDlciValue = _MfrapPerfCurrentPerDlciUtilizationDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2, 1, 1),
    _MfrapPerfCurrentPerDlciUtilizationDlciValue_Type()
)
mfrapPerfCurrentPerDlciUtilizationDlciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciUtilizationDlciValue.setStatus("mandatory")
_MfrapPerfCurrentPerDlciRxUtilization_Type = Integer32
_MfrapPerfCurrentPerDlciRxUtilization_Object = MibTableColumn
mfrapPerfCurrentPerDlciRxUtilization = _MfrapPerfCurrentPerDlciRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2, 1, 2),
    _MfrapPerfCurrentPerDlciRxUtilization_Type()
)
mfrapPerfCurrentPerDlciRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciRxUtilization.setStatus("mandatory")
_MfrapPerfCurrentPerDlciTxUtilization_Type = Integer32
_MfrapPerfCurrentPerDlciTxUtilization_Object = MibTableColumn
mfrapPerfCurrentPerDlciTxUtilization = _MfrapPerfCurrentPerDlciTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2, 1, 3),
    _MfrapPerfCurrentPerDlciTxUtilization_Type()
)
mfrapPerfCurrentPerDlciTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciTxUtilization.setStatus("mandatory")
_MfrapPerfCurrentPerDlciAggregateUtilization_Type = Integer32
_MfrapPerfCurrentPerDlciAggregateUtilization_Object = MibTableColumn
mfrapPerfCurrentPerDlciAggregateUtilization = _MfrapPerfCurrentPerDlciAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 2, 1, 4),
    _MfrapPerfCurrentPerDlciAggregateUtilization_Type()
)
mfrapPerfCurrentPerDlciAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentPerDlciAggregateUtilization.setStatus("mandatory")
_MfrapPerfCurrentUnitUtilization_ObjectIdentity = ObjectIdentity
mfrapPerfCurrentUnitUtilization = _MfrapPerfCurrentUnitUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 3)
)
_MfrapPerfCurrentDteUtilization_Type = Integer32
_MfrapPerfCurrentDteUtilization_Object = MibScalar
mfrapPerfCurrentDteUtilization = _MfrapPerfCurrentDteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 3, 2),
    _MfrapPerfCurrentDteUtilization_Type()
)
mfrapPerfCurrentDteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentDteUtilization.setStatus("mandatory")
_MfrapPerfCurrentWanUtilization_Type = Integer32
_MfrapPerfCurrentWanUtilization_Object = MibScalar
mfrapPerfCurrentWanUtilization = _MfrapPerfCurrentWanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 3, 3),
    _MfrapPerfCurrentWanUtilization_Type()
)
mfrapPerfCurrentWanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentWanUtilization.setStatus("mandatory")
_MfrapPerfCurrentAggregateUtilization_Type = Integer32
_MfrapPerfCurrentAggregateUtilization_Object = MibScalar
mfrapPerfCurrentAggregateUtilization = _MfrapPerfCurrentAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 5, 6, 3, 4),
    _MfrapPerfCurrentAggregateUtilization_Type()
)
mfrapPerfCurrentAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPerfCurrentAggregateUtilization.setStatus("mandatory")


class _MfrapAlarmType_Type(Integer32):
    """Custom type mfrapAlarmType based on Integer32"""
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
          ("dandi-ais-clear", 119),
          ("dandi-ais-detect", 118),
          ("dandi-carrier-detect", 111),
          ("dandi-carrier-loss", 110),
          ("dandi-controlled-slip", 120),
          ("dandi-red-alarm-clear", 115),
          ("dandi-red-alarm-declare", 114),
          ("dandi-sync-acquire", 113),
          ("dandi-sync-loss-declare", 112),
          ("dandi-yellow-alarm-clear", 117),
          ("dandi-yellow-alarm-detect", 116),
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
          ("local-dandi-line-loopback-disabled", 125),
          ("local-dandi-line-loopback-enabled", 124),
          ("local-dandi-line-loopback-failure", 126),
          ("local-dandi-payload-loopback-disabled", 122),
          ("local-dandi-payload-loopback-enabled", 121),
          ("local-dandi-payload-loopback-failure", 123),
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
          ("nest-fan-one-alarm", 130),
          ("nest-fan-one-alarm-clear", 131),
          ("nest-fan-two-alarm", 132),
          ("nest-fan-two-alarm-clear", 133),
          ("nest-power-supply-alarm", 134),
          ("nest-power-supply-alarm-clear", 135),
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


_MfrapAlarmType_Type.__name__ = "Integer32"
_MfrapAlarmType_Object = MibScalar
mfrapAlarmType = _MfrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 6),
    _MfrapAlarmType_Type()
)
mfrapAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapAlarmType.setStatus("mandatory")
_MfrapDLCINum_Type = Integer32
_MfrapDLCINum_Object = MibScalar
mfrapDLCINum = _MfrapDLCINum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 7),
    _MfrapDLCINum_Type()
)
mfrapDLCINum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapDLCINum.setStatus("mandatory")


class _MfrapInterface_Type(Integer32):
    """Custom type mfrapInterface based on Integer32"""
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


_MfrapInterface_Type.__name__ = "Integer32"
_MfrapInterface_Object = MibScalar
mfrapInterface = _MfrapInterface_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 8),
    _MfrapInterface_Type()
)
mfrapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapInterface.setStatus("mandatory")
_MfrapIpAddress_Type = IpAddress
_MfrapIpAddress_Object = MibScalar
mfrapIpAddress = _MfrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 9),
    _MfrapIpAddress_Type()
)
mfrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapIpAddress.setStatus("mandatory")
_MfrapEventTrapLog_ObjectIdentity = ObjectIdentity
mfrapEventTrapLog = _MfrapEventTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 8, 10)
)
_MfrapEventTrapLogTable_Object = MibTable
mfrapEventTrapLogTable = _MfrapEventTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1)
)
if mibBuilder.loadTexts:
    mfrapEventTrapLogTable.setStatus("mandatory")
_MfrapEventTrapLogEntry_Object = MibTableRow
mfrapEventTrapLogEntry = _MfrapEventTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1)
)
mfrapEventTrapLogEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapEventTrapLogSeqNum"),
)
if mibBuilder.loadTexts:
    mfrapEventTrapLogEntry.setStatus("mandatory")
_MfrapEventTrapLogSeqNum_Type = Integer32
_MfrapEventTrapLogSeqNum_Object = MibTableColumn
mfrapEventTrapLogSeqNum = _MfrapEventTrapLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 1),
    _MfrapEventTrapLogSeqNum_Type()
)
mfrapEventTrapLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogSeqNum.setStatus("mandatory")
_MfrapEventTrapLogGenericEvent_Type = Integer32
_MfrapEventTrapLogGenericEvent_Object = MibTableColumn
mfrapEventTrapLogGenericEvent = _MfrapEventTrapLogGenericEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 2),
    _MfrapEventTrapLogGenericEvent_Type()
)
mfrapEventTrapLogGenericEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogGenericEvent.setStatus("mandatory")
_MfrapEventTrapLogSpecificEvent_Type = Integer32
_MfrapEventTrapLogSpecificEvent_Object = MibTableColumn
mfrapEventTrapLogSpecificEvent = _MfrapEventTrapLogSpecificEvent_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 3),
    _MfrapEventTrapLogSpecificEvent_Type()
)
mfrapEventTrapLogSpecificEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogSpecificEvent.setStatus("mandatory")
_MfrapEventTrapLogTimeStamp_Type = TimeTicks
_MfrapEventTrapLogTimeStamp_Object = MibTableColumn
mfrapEventTrapLogTimeStamp = _MfrapEventTrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 4),
    _MfrapEventTrapLogTimeStamp_Type()
)
mfrapEventTrapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogTimeStamp.setStatus("mandatory")
_MfrapEventTrapLogVarBind1_Type = Integer32
_MfrapEventTrapLogVarBind1_Object = MibTableColumn
mfrapEventTrapLogVarBind1 = _MfrapEventTrapLogVarBind1_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 5),
    _MfrapEventTrapLogVarBind1_Type()
)
mfrapEventTrapLogVarBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogVarBind1.setStatus("mandatory")
_MfrapEventTrapLogVarBind2_Type = Integer32
_MfrapEventTrapLogVarBind2_Object = MibTableColumn
mfrapEventTrapLogVarBind2 = _MfrapEventTrapLogVarBind2_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 6),
    _MfrapEventTrapLogVarBind2_Type()
)
mfrapEventTrapLogVarBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogVarBind2.setStatus("mandatory")
_MfrapEventTrapLogVarBind3_Type = Integer32
_MfrapEventTrapLogVarBind3_Object = MibTableColumn
mfrapEventTrapLogVarBind3 = _MfrapEventTrapLogVarBind3_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 1, 1, 7),
    _MfrapEventTrapLogVarBind3_Type()
)
mfrapEventTrapLogVarBind3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventTrapLogVarBind3.setStatus("mandatory")
_MfrapEventLogAltTable_Object = MibTable
mfrapEventLogAltTable = _MfrapEventLogAltTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 2)
)
if mibBuilder.loadTexts:
    mfrapEventLogAltTable.setStatus("mandatory")
_MfrapEventLogAltEntry_Object = MibTableRow
mfrapEventLogAltEntry = _MfrapEventLogAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 2, 1)
)
mfrapEventLogAltEntry.setIndexNames(
    (0, "MFRAP-MIB", "mfrapEventLogAltSeqNum"),
)
if mibBuilder.loadTexts:
    mfrapEventLogAltEntry.setStatus("mandatory")
_MfrapEventLogAltSeqNum_Type = Integer32
_MfrapEventLogAltSeqNum_Object = MibTableColumn
mfrapEventLogAltSeqNum = _MfrapEventLogAltSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 2, 1, 1),
    _MfrapEventLogAltSeqNum_Type()
)
mfrapEventLogAltSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventLogAltSeqNum.setStatus("mandatory")
_MfrapEventLogAltArray_Type = OctetString
_MfrapEventLogAltArray_Object = MibTableColumn
mfrapEventLogAltArray = _MfrapEventLogAltArray_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 2, 1, 2),
    _MfrapEventLogAltArray_Type()
)
mfrapEventLogAltArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventLogAltArray.setStatus("mandatory")
_MfrapEventLogCurrentSeqNum_Type = Integer32
_MfrapEventLogCurrentSeqNum_Object = MibScalar
mfrapEventLogCurrentSeqNum = _MfrapEventLogCurrentSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 3),
    _MfrapEventLogCurrentSeqNum_Type()
)
mfrapEventLogCurrentSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapEventLogCurrentSeqNum.setStatus("mandatory")


class _MfrapEventLogFreeze_Type(Integer32):
    """Custom type mfrapEventLogFreeze based on Integer32"""
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


_MfrapEventLogFreeze_Type.__name__ = "Integer32"
_MfrapEventLogFreeze_Object = MibScalar
mfrapEventLogFreeze = _MfrapEventLogFreeze_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 4),
    _MfrapEventLogFreeze_Type()
)
mfrapEventLogFreeze.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapEventLogFreeze.setStatus("mandatory")


class _MfrapEventLogClear_Type(Integer32):
    """Custom type mfrapEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_MfrapEventLogClear_Type.__name__ = "Integer32"
_MfrapEventLogClear_Object = MibScalar
mfrapEventLogClear = _MfrapEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 10, 5),
    _MfrapEventLogClear_Type()
)
mfrapEventLogClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mfrapEventLogClear.setStatus("mandatory")
_MfrapPercentUtilization_Type = Integer32
_MfrapPercentUtilization_Object = MibScalar
mfrapPercentUtilization = _MfrapPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 11),
    _MfrapPercentUtilization_Type()
)
mfrapPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapPercentUtilization.setStatus("mandatory")
_MfrapUtilizationThreshold_Type = Integer32
_MfrapUtilizationThreshold_Object = MibScalar
mfrapUtilizationThreshold = _MfrapUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 12),
    _MfrapUtilizationThreshold_Type()
)
mfrapUtilizationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapUtilizationThreshold.setStatus("mandatory")
_MfrapCfgLockIpAddress_Type = IpAddress
_MfrapCfgLockIpAddress_Object = MibScalar
mfrapCfgLockIpAddress = _MfrapCfgLockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 8, 13),
    _MfrapCfgLockIpAddress_Type()
)
mfrapCfgLockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrapCfgLockIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mfrapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 0)
)
mfrapTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTrap.setStatus(
        ""
    )

mfrapBadConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 1)
)
mfrapBadConfigTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapBadConfigTrap.setStatus(
        ""
    )

mfrapLocalConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 2)
)
mfrapLocalConfigTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalConfigTrap.setStatus(
        ""
    )

mfrapt1netwcarrierloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 3)
)
mfrapt1netwcarrierloss.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwcarrierloss.setStatus(
        ""
    )

mfrapt1netwcarrierdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 4)
)
mfrapt1netwcarrierdetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwcarrierdetect.setStatus(
        ""
    )

mfrapt1netwsynclossdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 5)
)
mfrapt1netwsynclossdeclare.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwsynclossdeclare.setStatus(
        ""
    )

mfrapt1netwsyncacquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 6)
)
mfrapt1netwsyncacquire.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwsyncacquire.setStatus(
        ""
    )

mfrapt1netwredalarmdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 7)
)
mfrapt1netwredalarmdeclare.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwredalarmdeclare.setStatus(
        ""
    )

mfrapt1netwredalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 8)
)
mfrapt1netwredalarmclear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwredalarmclear.setStatus(
        ""
    )

mfrapt1netwyellowalarmdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 9)
)
mfrapt1netwyellowalarmdetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwyellowalarmdetect.setStatus(
        ""
    )

mfrapt1netwyellowalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 10)
)
mfrapt1netwyellowalarmclear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwyellowalarmclear.setStatus(
        ""
    )

mfrapt1netwaisdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 11)
)
mfrapt1netwaisdetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwaisdetect.setStatus(
        ""
    )

mfrapt1netwaisclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 12)
)
mfrapt1netwaisclear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1netwaisclear.setStatus(
        ""
    )

mfrapt1controlledslip = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 13)
)
mfrapt1controlledslip.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapt1controlledslip.setStatus(
        ""
    )

mfrapLocalUnitLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 14)
)
mfrapLocalUnitLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalUnitLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalUnitLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 15)
)
mfrapLocalUnitLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalUnitLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalUnitLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 16)
)
mfrapLocalUnitLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalUnitLoopbackFailedTrap.setStatus(
        ""
    )

mfrapLocalDteLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 17)
)
mfrapLocalDteLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDteLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalDteLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 18)
)
mfrapLocalDteLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDteLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalDteLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 19)
)
mfrapLocalDteLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDteLoopbackFailedTrap.setStatus(
        ""
    )

mfrapLocalAggregateLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 20)
)
mfrapLocalAggregateLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalAggregateLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalAggregateLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 21)
)
mfrapLocalAggregateLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalAggregateLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalAggregateLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 22)
)
mfrapLocalAggregateLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalAggregateLoopbackFailedTrap.setStatus(
        ""
    )

mfrapLocalPayloadLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 23)
)
mfrapLocalPayloadLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalPayloadLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalPayloadLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 24)
)
mfrapLocalPayloadLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalPayloadLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalPayloadLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 25)
)
mfrapLocalPayloadLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalPayloadLoopbackFailedTrap.setStatus(
        ""
    )

mfrapLocalNetLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 26)
)
mfrapLocalNetLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalNetLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalNetLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 27)
)
mfrapLocalNetLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalNetLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalNetLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 28)
)
mfrapLocalNetLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalNetLoopbackFailedTrap.setStatus(
        ""
    )

mfrapV54LoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 29)
)
mfrapV54LoopUpInitiatedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapV54LoopUpInitiatedTrap.setStatus(
        ""
    )

mfrapV54LoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 30)
)
mfrapV54LoopDownCompletedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapV54LoopDownCompletedTrap.setStatus(
        ""
    )

mfrapV54LoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 31)
)
mfrapV54LoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapV54LoopbackEnabledTrap.setStatus(
        ""
    )

mfrapV54LoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 32)
)
mfrapV54LoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapV54LoopbackDisabledTrap.setStatus(
        ""
    )

mfrapV54LoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 33)
)
mfrapV54LoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapV54LoopbackFailedTrap.setStatus(
        ""
    )

mfrapCsuLoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 34)
)
mfrapCsuLoopUpInitiatedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapCsuLoopUpInitiatedTrap.setStatus(
        ""
    )

mfrapCsuLoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 35)
)
mfrapCsuLoopDownCompletedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapCsuLoopDownCompletedTrap.setStatus(
        ""
    )

mfrapCsuLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 36)
)
mfrapCsuLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapCsuLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapCsuLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 37)
)
mfrapCsuLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapCsuLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapCsuLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 38)
)
mfrapCsuLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapCsuLoopbackFailedTrap.setStatus(
        ""
    )

mfrapDsuLoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 39)
)
mfrapDsuLoopUpInitiatedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDsuLoopUpInitiatedTrap.setStatus(
        ""
    )

mfrapDsuLoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 40)
)
mfrapDsuLoopDownCompletedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDsuLoopDownCompletedTrap.setStatus(
        ""
    )

mfrapDsuLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 41)
)
mfrapDsuLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDsuLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapDsuLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 42)
)
mfrapDsuLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDsuLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapDsuLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 43)
)
mfrapDsuLoopbackFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDsuLoopbackFailedTrap.setStatus(
        ""
    )

mfrapBertInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 44)
)
mfrapBertInitiatedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapBertInitiatedTrap.setStatus(
        ""
    )

mfrapBertCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 45)
)
mfrapBertCompletedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapBertCompletedTrap.setStatus(
        ""
    )

mfrapBertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 46)
)
mfrapBertFailedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapBertFailedTrap.setStatus(
        ""
    )

mfrapDLCIActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 47)
)
mfrapDLCIActiveTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"))
)
if mibBuilder.loadTexts:
    mfrapDLCIActiveTrap.setStatus(
        ""
    )

mfrapDLCIInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 48)
)
mfrapDLCIInactiveTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"))
)
if mibBuilder.loadTexts:
    mfrapDLCIInactiveTrap.setStatus(
        ""
    )

mfrapDLCITDThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 49)
)
mfrapDLCITDThresholdTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapIpAddress"))
)
if mibBuilder.loadTexts:
    mfrapDLCITDThresholdTrap.setStatus(
        ""
    )

mfrapLmiSourcingChangePassthruTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 50)
)
mfrapLmiSourcingChangePassthruTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSourcingChangePassthruTrap.setStatus(
        ""
    )

mfrapLmiSourcingChangeUserDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 51)
)
mfrapLmiSourcingChangeUserDteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSourcingChangeUserDteTrap.setStatus(
        ""
    )

mfrapLmiSourcingChangeNetDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 52)
)
mfrapLmiSourcingChangeNetDteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSourcingChangeNetDteTrap.setStatus(
        ""
    )

mfrapLmiSourcingChangeUserT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 53)
)
mfrapLmiSourcingChangeUserT1Trap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSourcingChangeUserT1Trap.setStatus(
        ""
    )

mfrapLmiSourcingChangeNetT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 54)
)
mfrapLmiSourcingChangeNetT1Trap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSourcingChangeNetT1Trap.setStatus(
        ""
    )

mfrapDteSignalRtsOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 55)
)
mfrapDteSignalRtsOnTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDteSignalRtsOnTrap.setStatus(
        ""
    )

mfrapDteSignalRtsOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 56)
)
mfrapDteSignalRtsOffTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDteSignalRtsOffTrap.setStatus(
        ""
    )

mfrapDteSignalDtrOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 57)
)
mfrapDteSignalDtrOnTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDteSignalDtrOnTrap.setStatus(
        ""
    )

mfrapDteSignalDtrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 58)
)
mfrapDteSignalDtrOffTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDteSignalDtrOffTrap.setStatus(
        ""
    )

mfrapNonIncrLmiSeqNumDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 59)
)
mfrapNonIncrLmiSeqNumDteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNonIncrLmiSeqNumDteTrap.setStatus(
        ""
    )

mfrapNonIncrLmiSeqNumT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 60)
)
mfrapNonIncrLmiSeqNumT1Trap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNonIncrLmiSeqNumT1Trap.setStatus(
        ""
    )

mfrapLmiSeqNumMismatchDteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 61)
)
mfrapLmiSeqNumMismatchDteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSeqNumMismatchDteTrap.setStatus(
        ""
    )

mfrapLmiSeqNumMismatchT1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 62)
)
mfrapLmiSeqNumMismatchT1Trap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLmiSeqNumMismatchT1Trap.setStatus(
        ""
    )

mfrapTrapMutingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 75)
)
mfrapTrapMutingActive.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTrapMutingActive.setStatus(
        ""
    )

mfrapTrapMutingInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 76)
)
mfrapTrapMutingInactive.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTrapMutingInactive.setStatus(
        ""
    )

mfrapVloopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 90)
)
mfrapVloopUp.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVloopUp.setStatus(
        ""
    )

mfrapVloopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 91)
)
mfrapVloopDown.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVloopDown.setStatus(
        ""
    )

mfrapVloopUpViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 92)
)
mfrapVloopUpViaRemote.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVloopUpViaRemote.setStatus(
        ""
    )

mfrapVloopDownViaRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 93)
)
mfrapVloopDownViaRemote.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVloopDownViaRemote.setStatus(
        ""
    )

mfrapVloopRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 94)
)
mfrapVloopRequestFailed.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVloopRequestFailed.setStatus(
        ""
    )

mfrapVbertStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 95)
)
mfrapVbertStarted.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVbertStarted.setStatus(
        ""
    )

mfrapVbertStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 96)
)
mfrapVbertStopped.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVbertStopped.setStatus(
        ""
    )

mfrapVbertRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 97)
)
mfrapVbertRequestFailed.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapInterface"))
)
if mibBuilder.loadTexts:
    mfrapVbertRequestFailed.setStatus(
        ""
    )

mfrapDandiCarrierLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 110)
)
mfrapDandiCarrierLoss.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiCarrierLoss.setStatus(
        ""
    )

mfrapDandiCarrierDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 111)
)
mfrapDandiCarrierDetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiCarrierDetect.setStatus(
        ""
    )

mfrapDandiSyncLossDeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 112)
)
mfrapDandiSyncLossDeclare.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiSyncLossDeclare.setStatus(
        ""
    )

mfrapDandiSyncAcquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 113)
)
mfrapDandiSyncAcquire.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiSyncAcquire.setStatus(
        ""
    )

mfrapDandiRedAlarmDeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 114)
)
mfrapDandiRedAlarmDeclare.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiRedAlarmDeclare.setStatus(
        ""
    )

mfrapDandiRedalArmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 115)
)
mfrapDandiRedalArmclear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiRedalArmclear.setStatus(
        ""
    )

mfrapDandiYellowAlarmDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 116)
)
mfrapDandiYellowAlarmDetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiYellowAlarmDetect.setStatus(
        ""
    )

mfrapDandiYellowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 117)
)
mfrapDandiYellowAlarmClear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiYellowAlarmClear.setStatus(
        ""
    )

mfrapDandIaisDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 118)
)
mfrapDandIaisDetect.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandIaisDetect.setStatus(
        ""
    )

mfrapDandiAisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 119)
)
mfrapDandiAisClear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiAisClear.setStatus(
        ""
    )

mfrapDandiControlledSlip = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 120)
)
mfrapDandiControlledSlip.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapDandiControlledSlip.setStatus(
        ""
    )

mfrapLocalDandiPayloadLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 121)
)
mfrapLocalDandiPayloadLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiPayloadLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalDandiPayloadLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 122)
)
mfrapLocalDandiPayloadLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiPayloadLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalDandiPayloadLoopbackFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 123)
)
mfrapLocalDandiPayloadLoopbackFailureTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiPayloadLoopbackFailureTrap.setStatus(
        ""
    )

mfrapLocalDandiLineLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 124)
)
mfrapLocalDandiLineLoopbackEnabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiLineLoopbackEnabledTrap.setStatus(
        ""
    )

mfrapLocalDandiLineLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 125)
)
mfrapLocalDandiLineLoopbackDisabledTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiLineLoopbackDisabledTrap.setStatus(
        ""
    )

mfrapLocalDandiLineLoopbackFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 126)
)
mfrapLocalDandiLineLoopbackFailureTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalDandiLineLoopbackFailureTrap.setStatus(
        ""
    )

mfrapNestFanOneAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 130)
)
mfrapNestFanOneAlarm.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestFanOneAlarm.setStatus(
        ""
    )

mfrapNestFanOneAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 131)
)
mfrapNestFanOneAlarmClear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestFanOneAlarmClear.setStatus(
        ""
    )

mfrapNestFanTwoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 132)
)
mfrapNestFanTwoAlarm.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestFanTwoAlarm.setStatus(
        ""
    )

mfrapNestFanTwoAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 133)
)
mfrapNestFanTwoAlarmClear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestFanTwoAlarmClear.setStatus(
        ""
    )

mfrapNestPowerSupplyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 134)
)
mfrapNestPowerSupplyAlarm.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestPowerSupplyAlarm.setStatus(
        ""
    )

mfrapNestPowerSupplyAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 135)
)
mfrapNestPowerSupplyAlarmClear.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapNestPowerSupplyAlarmClear.setStatus(
        ""
    )

mfrapLocalPayloadLoopbackEnabledViaRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 136)
)
mfrapLocalPayloadLoopbackEnabledViaRemoteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalPayloadLoopbackEnabledViaRemoteTrap.setStatus(
        ""
    )

mfrapLocalPayloadLoopbackDisabledViaRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 137)
)
mfrapLocalPayloadLoopbackDisabledViaRemoteTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapLocalPayloadLoopbackDisabledViaRemoteTrap.setStatus(
        ""
    )

mfrapPvcRxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 138)
)
mfrapPvcRxUtilizationExceededTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapPercentUtilization"),
        ("MFRAP-MIB", "mfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    mfrapPvcRxUtilizationExceededTrap.setStatus(
        ""
    )

mfrapPvcTxUtilizationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 139)
)
mfrapPvcTxUtilizationExceededTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapPercentUtilization"),
        ("MFRAP-MIB", "mfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    mfrapPvcTxUtilizationExceededTrap.setStatus(
        ""
    )

mfrapPvcRxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 140)
)
mfrapPvcRxUtilizationClearedTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapPercentUtilization"),
        ("MFRAP-MIB", "mfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    mfrapPvcRxUtilizationClearedTrap.setStatus(
        ""
    )

mfrapPvcTxUtilizationClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 141)
)
mfrapPvcTxUtilizationClearedTrap.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapDLCINum"),
        ("MFRAP-MIB", "mfrapPercentUtilization"),
        ("MFRAP-MIB", "mfrapUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    mfrapPvcTxUtilizationClearedTrap.setStatus(
        ""
    )

mfrapConfigInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 142)
)
mfrapConfigInstallSuccess.setObjects(
      *(("MFRAP-MIB", "mfrapAlarmType"),
        ("MFRAP-MIB", "mfrapCfgLockIpAddress"))
)
if mibBuilder.loadTexts:
    mfrapConfigInstallSuccess.setStatus(
        ""
    )

mfrapTftpRequestedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 257)
)
mfrapTftpRequestedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpRequestedTrap.setStatus(
        ""
    )

mfrapTftpTransferringTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 258)
)
mfrapTftpTransferringTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpTransferringTrap.setStatus(
        ""
    )

mfrapTftpProgrammingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 259)
)
mfrapTftpProgrammingTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpProgrammingTrap.setStatus(
        ""
    )

mfrapTftpAbortedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 260)
)
mfrapTftpAbortedTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpAbortedTrap.setStatus(
        ""
    )

mfrapTftpSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 261)
)
mfrapTftpSuccessTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpSuccessTrap.setStatus(
        ""
    )

mfrapTftpHostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 262)
)
mfrapTftpHostUnreachableTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpHostUnreachableTrap.setStatus(
        ""
    )

mfrapTftpNoFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 263)
)
mfrapTftpNoFileTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpNoFileTrap.setStatus(
        ""
    )

mfrapTftpInvalidFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 264)
)
mfrapTftpInvalidFileTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpInvalidFileTrap.setStatus(
        ""
    )

mfrapTftpCorruptFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 8, 0, 265)
)
mfrapTftpCorruptFileTrap.setObjects(
    ("MFRAP-MIB", "mfrapAlarmType")
)
if mibBuilder.loadTexts:
    mfrapTftpCorruptFileTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MFRAP-MIB",
    **{"Index": Index,
       "private": private,
       "enterprises": enterprises,
       "sync": sync,
       "mfrap": mfrap,
       "mfrapTrap": mfrapTrap,
       "mfrapBadConfigTrap": mfrapBadConfigTrap,
       "mfrapLocalConfigTrap": mfrapLocalConfigTrap,
       "mfrapt1netwcarrierloss": mfrapt1netwcarrierloss,
       "mfrapt1netwcarrierdetect": mfrapt1netwcarrierdetect,
       "mfrapt1netwsynclossdeclare": mfrapt1netwsynclossdeclare,
       "mfrapt1netwsyncacquire": mfrapt1netwsyncacquire,
       "mfrapt1netwredalarmdeclare": mfrapt1netwredalarmdeclare,
       "mfrapt1netwredalarmclear": mfrapt1netwredalarmclear,
       "mfrapt1netwyellowalarmdetect": mfrapt1netwyellowalarmdetect,
       "mfrapt1netwyellowalarmclear": mfrapt1netwyellowalarmclear,
       "mfrapt1netwaisdetect": mfrapt1netwaisdetect,
       "mfrapt1netwaisclear": mfrapt1netwaisclear,
       "mfrapt1controlledslip": mfrapt1controlledslip,
       "mfrapLocalUnitLoopbackEnabledTrap": mfrapLocalUnitLoopbackEnabledTrap,
       "mfrapLocalUnitLoopbackDisabledTrap": mfrapLocalUnitLoopbackDisabledTrap,
       "mfrapLocalUnitLoopbackFailedTrap": mfrapLocalUnitLoopbackFailedTrap,
       "mfrapLocalDteLoopbackEnabledTrap": mfrapLocalDteLoopbackEnabledTrap,
       "mfrapLocalDteLoopbackDisabledTrap": mfrapLocalDteLoopbackDisabledTrap,
       "mfrapLocalDteLoopbackFailedTrap": mfrapLocalDteLoopbackFailedTrap,
       "mfrapLocalAggregateLoopbackEnabledTrap": mfrapLocalAggregateLoopbackEnabledTrap,
       "mfrapLocalAggregateLoopbackDisabledTrap": mfrapLocalAggregateLoopbackDisabledTrap,
       "mfrapLocalAggregateLoopbackFailedTrap": mfrapLocalAggregateLoopbackFailedTrap,
       "mfrapLocalPayloadLoopbackEnabledTrap": mfrapLocalPayloadLoopbackEnabledTrap,
       "mfrapLocalPayloadLoopbackDisabledTrap": mfrapLocalPayloadLoopbackDisabledTrap,
       "mfrapLocalPayloadLoopbackFailedTrap": mfrapLocalPayloadLoopbackFailedTrap,
       "mfrapLocalNetLoopbackEnabledTrap": mfrapLocalNetLoopbackEnabledTrap,
       "mfrapLocalNetLoopbackDisabledTrap": mfrapLocalNetLoopbackDisabledTrap,
       "mfrapLocalNetLoopbackFailedTrap": mfrapLocalNetLoopbackFailedTrap,
       "mfrapV54LoopUpInitiatedTrap": mfrapV54LoopUpInitiatedTrap,
       "mfrapV54LoopDownCompletedTrap": mfrapV54LoopDownCompletedTrap,
       "mfrapV54LoopbackEnabledTrap": mfrapV54LoopbackEnabledTrap,
       "mfrapV54LoopbackDisabledTrap": mfrapV54LoopbackDisabledTrap,
       "mfrapV54LoopbackFailedTrap": mfrapV54LoopbackFailedTrap,
       "mfrapCsuLoopUpInitiatedTrap": mfrapCsuLoopUpInitiatedTrap,
       "mfrapCsuLoopDownCompletedTrap": mfrapCsuLoopDownCompletedTrap,
       "mfrapCsuLoopbackEnabledTrap": mfrapCsuLoopbackEnabledTrap,
       "mfrapCsuLoopbackDisabledTrap": mfrapCsuLoopbackDisabledTrap,
       "mfrapCsuLoopbackFailedTrap": mfrapCsuLoopbackFailedTrap,
       "mfrapDsuLoopUpInitiatedTrap": mfrapDsuLoopUpInitiatedTrap,
       "mfrapDsuLoopDownCompletedTrap": mfrapDsuLoopDownCompletedTrap,
       "mfrapDsuLoopbackEnabledTrap": mfrapDsuLoopbackEnabledTrap,
       "mfrapDsuLoopbackDisabledTrap": mfrapDsuLoopbackDisabledTrap,
       "mfrapDsuLoopbackFailedTrap": mfrapDsuLoopbackFailedTrap,
       "mfrapBertInitiatedTrap": mfrapBertInitiatedTrap,
       "mfrapBertCompletedTrap": mfrapBertCompletedTrap,
       "mfrapBertFailedTrap": mfrapBertFailedTrap,
       "mfrapDLCIActiveTrap": mfrapDLCIActiveTrap,
       "mfrapDLCIInactiveTrap": mfrapDLCIInactiveTrap,
       "mfrapDLCITDThresholdTrap": mfrapDLCITDThresholdTrap,
       "mfrapLmiSourcingChangePassthruTrap": mfrapLmiSourcingChangePassthruTrap,
       "mfrapLmiSourcingChangeUserDteTrap": mfrapLmiSourcingChangeUserDteTrap,
       "mfrapLmiSourcingChangeNetDteTrap": mfrapLmiSourcingChangeNetDteTrap,
       "mfrapLmiSourcingChangeUserT1Trap": mfrapLmiSourcingChangeUserT1Trap,
       "mfrapLmiSourcingChangeNetT1Trap": mfrapLmiSourcingChangeNetT1Trap,
       "mfrapDteSignalRtsOnTrap": mfrapDteSignalRtsOnTrap,
       "mfrapDteSignalRtsOffTrap": mfrapDteSignalRtsOffTrap,
       "mfrapDteSignalDtrOnTrap": mfrapDteSignalDtrOnTrap,
       "mfrapDteSignalDtrOffTrap": mfrapDteSignalDtrOffTrap,
       "mfrapNonIncrLmiSeqNumDteTrap": mfrapNonIncrLmiSeqNumDteTrap,
       "mfrapNonIncrLmiSeqNumT1Trap": mfrapNonIncrLmiSeqNumT1Trap,
       "mfrapLmiSeqNumMismatchDteTrap": mfrapLmiSeqNumMismatchDteTrap,
       "mfrapLmiSeqNumMismatchT1Trap": mfrapLmiSeqNumMismatchT1Trap,
       "mfrapTrapMutingActive": mfrapTrapMutingActive,
       "mfrapTrapMutingInactive": mfrapTrapMutingInactive,
       "mfrapVloopUp": mfrapVloopUp,
       "mfrapVloopDown": mfrapVloopDown,
       "mfrapVloopUpViaRemote": mfrapVloopUpViaRemote,
       "mfrapVloopDownViaRemote": mfrapVloopDownViaRemote,
       "mfrapVloopRequestFailed": mfrapVloopRequestFailed,
       "mfrapVbertStarted": mfrapVbertStarted,
       "mfrapVbertStopped": mfrapVbertStopped,
       "mfrapVbertRequestFailed": mfrapVbertRequestFailed,
       "mfrapDandiCarrierLoss": mfrapDandiCarrierLoss,
       "mfrapDandiCarrierDetect": mfrapDandiCarrierDetect,
       "mfrapDandiSyncLossDeclare": mfrapDandiSyncLossDeclare,
       "mfrapDandiSyncAcquire": mfrapDandiSyncAcquire,
       "mfrapDandiRedAlarmDeclare": mfrapDandiRedAlarmDeclare,
       "mfrapDandiRedalArmclear": mfrapDandiRedalArmclear,
       "mfrapDandiYellowAlarmDetect": mfrapDandiYellowAlarmDetect,
       "mfrapDandiYellowAlarmClear": mfrapDandiYellowAlarmClear,
       "mfrapDandIaisDetect": mfrapDandIaisDetect,
       "mfrapDandiAisClear": mfrapDandiAisClear,
       "mfrapDandiControlledSlip": mfrapDandiControlledSlip,
       "mfrapLocalDandiPayloadLoopbackEnabledTrap": mfrapLocalDandiPayloadLoopbackEnabledTrap,
       "mfrapLocalDandiPayloadLoopbackDisabledTrap": mfrapLocalDandiPayloadLoopbackDisabledTrap,
       "mfrapLocalDandiPayloadLoopbackFailureTrap": mfrapLocalDandiPayloadLoopbackFailureTrap,
       "mfrapLocalDandiLineLoopbackEnabledTrap": mfrapLocalDandiLineLoopbackEnabledTrap,
       "mfrapLocalDandiLineLoopbackDisabledTrap": mfrapLocalDandiLineLoopbackDisabledTrap,
       "mfrapLocalDandiLineLoopbackFailureTrap": mfrapLocalDandiLineLoopbackFailureTrap,
       "mfrapNestFanOneAlarm": mfrapNestFanOneAlarm,
       "mfrapNestFanOneAlarmClear": mfrapNestFanOneAlarmClear,
       "mfrapNestFanTwoAlarm": mfrapNestFanTwoAlarm,
       "mfrapNestFanTwoAlarmClear": mfrapNestFanTwoAlarmClear,
       "mfrapNestPowerSupplyAlarm": mfrapNestPowerSupplyAlarm,
       "mfrapNestPowerSupplyAlarmClear": mfrapNestPowerSupplyAlarmClear,
       "mfrapLocalPayloadLoopbackEnabledViaRemoteTrap": mfrapLocalPayloadLoopbackEnabledViaRemoteTrap,
       "mfrapLocalPayloadLoopbackDisabledViaRemoteTrap": mfrapLocalPayloadLoopbackDisabledViaRemoteTrap,
       "mfrapPvcRxUtilizationExceededTrap": mfrapPvcRxUtilizationExceededTrap,
       "mfrapPvcTxUtilizationExceededTrap": mfrapPvcTxUtilizationExceededTrap,
       "mfrapPvcRxUtilizationClearedTrap": mfrapPvcRxUtilizationClearedTrap,
       "mfrapPvcTxUtilizationClearedTrap": mfrapPvcTxUtilizationClearedTrap,
       "mfrapConfigInstallSuccess": mfrapConfigInstallSuccess,
       "mfrapTftpRequestedTrap": mfrapTftpRequestedTrap,
       "mfrapTftpTransferringTrap": mfrapTftpTransferringTrap,
       "mfrapTftpProgrammingTrap": mfrapTftpProgrammingTrap,
       "mfrapTftpAbortedTrap": mfrapTftpAbortedTrap,
       "mfrapTftpSuccessTrap": mfrapTftpSuccessTrap,
       "mfrapTftpHostUnreachableTrap": mfrapTftpHostUnreachableTrap,
       "mfrapTftpNoFileTrap": mfrapTftpNoFileTrap,
       "mfrapTftpInvalidFileTrap": mfrapTftpInvalidFileTrap,
       "mfrapTftpCorruptFileTrap": mfrapTftpCorruptFileTrap,
       "mfrapSystem": mfrapSystem,
       "mfrapSysTable": mfrapSysTable,
       "mfrapSysType": mfrapSysType,
       "mfrapSysSoftRev": mfrapSysSoftRev,
       "mfrapSysHardRev": mfrapSysHardRev,
       "mfrapSysNumT1Installed": mfrapSysNumT1Installed,
       "mfrapSysNumDteInstalled": mfrapSysNumDteInstalled,
       "mfrapSysNumMaintInstalled": mfrapSysNumMaintInstalled,
       "mfrapSysName": mfrapSysName,
       "mfrapSysSerialNo": mfrapSysSerialNo,
       "mfrapSysResetNode": mfrapSysResetNode,
       "mfrapSysAmtMemoryInstalled": mfrapSysAmtMemoryInstalled,
       "mfrapSysLocation": mfrapSysLocation,
       "mfrapSysContact": mfrapSysContact,
       "mfrapSysPrompt": mfrapSysPrompt,
       "mfrapSysBootRev": mfrapSysBootRev,
       "mfrapSysNestId": mfrapSysNestId,
       "mfrapSysFeatureTable": mfrapSysFeatureTable,
       "mfrapSysSLIPSupported": mfrapSysSLIPSupported,
       "mfrapSysPPPSupported": mfrapSysPPPSupported,
       "mfrapSysRDOSupported": mfrapSysRDOSupported,
       "mfrapSysETHSupported": mfrapSysETHSupported,
       "mfrapSysTKRSupported": mfrapSysTKRSupported,
       "mfrapSysExtTimSupported": mfrapSysExtTimSupported,
       "mfrapSysBRISupported": mfrapSysBRISupported,
       "mfrapSysSelDTESupported": mfrapSysSelDTESupported,
       "mfrapSysMLSupported": mfrapSysMLSupported,
       "mfrapSysNumDlcisSupported": mfrapSysNumDlcisSupported,
       "mfrapSysLTFNumDlcis": mfrapSysLTFNumDlcis,
       "mfrapSysLTFNumProtocols": mfrapSysLTFNumProtocols,
       "mfrapSysNumUserProtocols": mfrapSysNumUserProtocols,
       "mfrapSysNumSnmpMgrs": mfrapSysNumSnmpMgrs,
       "mfrapSysNumDlciNames": mfrapSysNumDlciNames,
       "mfrapConfiguration": mfrapConfiguration,
       "mfrapCfgMgmtTable": mfrapCfgMgmtTable,
       "mfrapCfgIpTable": mfrapCfgIpTable,
       "mfrapCfgIpMyIP": mfrapCfgIpMyIP,
       "mfrapCfgIpPeerIP": mfrapCfgIpPeerIP,
       "mfrapCfgIpMask": mfrapCfgIpMask,
       "mfrapCfgIpMaxMTU": mfrapCfgIpMaxMTU,
       "mfrapCfgIpChannel": mfrapCfgIpChannel,
       "mfrapCfgIpTelnetEnable": mfrapCfgIpTelnetEnable,
       "mfrapCfgIpTelnetAutoLogOut": mfrapCfgIpTelnetAutoLogOut,
       "mfrapCfgTftpTable": mfrapCfgTftpTable,
       "mfrapCfgTftpInitiate": mfrapCfgTftpInitiate,
       "mfrapCfgTftpIpAddress": mfrapCfgTftpIpAddress,
       "mfrapCfgTftpFilename": mfrapCfgTftpFilename,
       "mfrapCfgTftpInterface": mfrapCfgTftpInterface,
       "mfrapCfgTftpDlci": mfrapCfgTftpDlci,
       "mfrapCfgTftpStatus": mfrapCfgTftpStatus,
       "mfrapCfgTftpNumBytes": mfrapCfgTftpNumBytes,
       "mfrapCfgSnmpTable": mfrapCfgSnmpTable,
       "mfrapCfgSnmpFrTrap": mfrapCfgSnmpFrTrap,
       "mfrapCfgSnmpMgrTable": mfrapCfgSnmpMgrTable,
       "mfrapCfgSnmpMgrEntry": mfrapCfgSnmpMgrEntry,
       "mfrapCfgSnmpMgrIndex": mfrapCfgSnmpMgrIndex,
       "mfrapCfgSnmpMgrIP": mfrapCfgSnmpMgrIP,
       "mfrapCfgSnmpMgrInterface": mfrapCfgSnmpMgrInterface,
       "mfrapCfgSnmpMgrDlci": mfrapCfgSnmpMgrDlci,
       "mfrapCfgSnmpTrapMuting": mfrapCfgSnmpTrapMuting,
       "mfrapCfgSnmpNestAlarmTrapEnable": mfrapCfgSnmpNestAlarmTrapEnable,
       "mfrapCfgSnmpDandIPortTrapEnable": mfrapCfgSnmpDandIPortTrapEnable,
       "mfrapCfgSnmpUtilTrapEnable": mfrapCfgSnmpUtilTrapEnable,
       "mfrapCfgSnmpMgrClearN": mfrapCfgSnmpMgrClearN,
       "mfrapCfgCommTable": mfrapCfgCommTable,
       "mfrapCfgCommMode": mfrapCfgCommMode,
       "mfrapCfgCommBaud": mfrapCfgCommBaud,
       "mfrapCfgCommDataBits": mfrapCfgCommDataBits,
       "mfrapCfgCommStopBits": mfrapCfgCommStopBits,
       "mfrapCfgCommParity": mfrapCfgCommParity,
       "mfrapCfgCommFlowCtrl": mfrapCfgCommFlowCtrl,
       "mfrapCfgCommModeAutoDetect": mfrapCfgCommModeAutoDetect,
       "mfrapCfgFrDLCITable": mfrapCfgFrDLCITable,
       "mfrapCfgFrDLCIMode": mfrapCfgFrDLCIMode,
       "mfrapCfgFrDLCIValue": mfrapCfgFrDLCIValue,
       "mfrapCfgFrDLCIEncap": mfrapCfgFrDLCIEncap,
       "mfrapCfgFrDLCIMgmtDE": mfrapCfgFrDLCIMgmtDE,
       "mfrapCfgAppTable": mfrapCfgAppTable,
       "mfrapCfgAppClockSource": mfrapCfgAppClockSource,
       "mfrapCfgAppCircuitId": mfrapCfgAppCircuitId,
       "mfrapCfgAppType": mfrapCfgAppType,
       "mfrapCfgAppFormat": mfrapCfgAppFormat,
       "mfrapCfgAppLpbkTimeout": mfrapCfgAppLpbkTimeout,
       "mfrapCfgAppPerfBuffLimit": mfrapCfgAppPerfBuffLimit,
       "mfrapCfgT1Table": mfrapCfgT1Table,
       "mfrapCfgT1Framing": mfrapCfgT1Framing,
       "mfrapCfgT1LineEncoding": mfrapCfgT1LineEncoding,
       "mfrapCfgT1Density": mfrapCfgT1Density,
       "mfrapCfgT1Interface": mfrapCfgT1Interface,
       "mfrapCfgT1LboSetting": mfrapCfgT1LboSetting,
       "mfrapCfgDteTable": mfrapCfgDteTable,
       "mfrapCfgDteIntfType": mfrapCfgDteIntfType,
       "mfrapCfgDteDataMode": mfrapCfgDteDataMode,
       "mfrapCfgDteClockMode": mfrapCfgDteClockMode,
       "mfrapCfgDteTiming": mfrapCfgDteTiming,
       "mfrapCfgDteLineRate": mfrapCfgDteLineRate,
       "mfrapCfgDteChannelDensity": mfrapCfgDteChannelDensity,
       "mfrapCfgDteStartDs0": mfrapCfgDteStartDs0,
       "mfrapCfgDteConnStatus": mfrapCfgDteConnStatus,
       "mfrapCfgDteConnStartDs0": mfrapCfgDteConnStartDs0,
       "mfrapCfgDteConnRate": mfrapCfgDteConnRate,
       "mfrapCfgDteConnDensity": mfrapCfgDteConnDensity,
       "mfrapCfgDteConnDs0Required": mfrapCfgDteConnDs0Required,
       "mfrapCfgDteConnAutoStatus": mfrapCfgDteConnAutoStatus,
       "mfrapCfgDteConnAutoUpdate": mfrapCfgDteConnAutoUpdate,
       "mfrapCfgDteRts": mfrapCfgDteRts,
       "mfrapCfgDteDtr": mfrapCfgDteDtr,
       "mfrapCfgDteDcdOutput": mfrapCfgDteDcdOutput,
       "mfrapCfgDteDsrOutput": mfrapCfgDteDsrOutput,
       "mfrapCfgDteCtsOutput": mfrapCfgDteCtsOutput,
       "mfrapCfgFrTable": mfrapCfgFrTable,
       "mfrapCfgFrAddrLen": mfrapCfgFrAddrLen,
       "mfrapCfgFrCrcMode": mfrapCfgFrCrcMode,
       "mfrapCfgFrLmiType": mfrapCfgFrLmiType,
       "mfrapCfgFrLmiInactivityTimeout": mfrapCfgFrLmiInactivityTimeout,
       "mfrapCfgFrLmiKeepaliveTimeout": mfrapCfgFrLmiKeepaliveTimeout,
       "mfrapCfgFrAddrResMode": mfrapCfgFrAddrResMode,
       "mfrapCfgFrAddrResInarpTimer": mfrapCfgFrAddrResInarpTimer,
       "mfrapCfgFrLmiFullStatus": mfrapCfgFrLmiFullStatus,
       "mfrapCfgFrAddrResDlcis": mfrapCfgFrAddrResDlcis,
       "mfrapCfgVnipTable": mfrapCfgVnipTable,
       "mfrapCfgVnipMode": mfrapCfgVnipMode,
       "mfrapCfgVnipInitTimer": mfrapCfgVnipInitTimer,
       "mfrapCfgVnipKeepAliveTimer": mfrapCfgVnipKeepAliveTimer,
       "mfrapCfgVnipInactivityTimer": mfrapCfgVnipInactivityTimer,
       "mfrapCfgVnipTransitDelayFrequency": mfrapCfgVnipTransitDelayFrequency,
       "mfrapCfgTransitDelayTable": mfrapCfgTransitDelayTable,
       "mfrapCfgTransitDelayEntry": mfrapCfgTransitDelayEntry,
       "mfrapCfgTransitDelayInterface": mfrapCfgTransitDelayInterface,
       "mfrapCfgTransitDelayDlciValue": mfrapCfgTransitDelayDlciValue,
       "mfrapCfgTransitDelayNumHops": mfrapCfgTransitDelayNumHops,
       "mfrapCfgTransitDelayRcvSummaryCancel": mfrapCfgTransitDelayRcvSummaryCancel,
       "mfrapCfgTransitDelayThreshold": mfrapCfgTransitDelayThreshold,
       "mfrapCfgTDDeleteTable": mfrapCfgTDDeleteTable,
       "mfrapCfgTDDeleteEntry": mfrapCfgTDDeleteEntry,
       "mfrapCfgTDDeleteInterface": mfrapCfgTDDeleteInterface,
       "mfrapCfgTDDeleteDlciValue": mfrapCfgTDDeleteDlciValue,
       "mfrapCfgTransitDelayTableClear": mfrapCfgTransitDelayTableClear,
       "mfrapCfgFrPerf": mfrapCfgFrPerf,
       "mfrapCfgFrPerfDlciNamesTable": mfrapCfgFrPerfDlciNamesTable,
       "mfrapCfgFrPerfDlciNamesEntry": mfrapCfgFrPerfDlciNamesEntry,
       "mfrapCfgFrPerfDlciNamesDlciValue": mfrapCfgFrPerfDlciNamesDlciValue,
       "mfrapCfgFrPerfDlciNamesDlciName": mfrapCfgFrPerfDlciNamesDlciName,
       "mfrapCfgFrPerfDlciNamesCirValue": mfrapCfgFrPerfDlciNamesCirValue,
       "mfrapCfgFrPerfDlciNamesCirType": mfrapCfgFrPerfDlciNamesCirType,
       "mfrapCfgFrPerfDlciNamesUtilThreshold": mfrapCfgFrPerfDlciNamesUtilThreshold,
       "mfrapCfgFrPerfDlciNamesEirValue": mfrapCfgFrPerfDlciNamesEirValue,
       "mfrapCfgFrPerfDlciNamesDelete": mfrapCfgFrPerfDlciNamesDelete,
       "mfrapCfgFrPerfTimers": mfrapCfgFrPerfTimers,
       "mfrapCfgFrPerfTimersSTInterval": mfrapCfgFrPerfTimersSTInterval,
       "mfrapCfgFrPerfTimersLTInterval": mfrapCfgFrPerfTimersLTInterval,
       "mfrapCfgFrPerfUserProtocolsTable": mfrapCfgFrPerfUserProtocolsTable,
       "mfrapCfgFrPerfUserProtocolsEntry": mfrapCfgFrPerfUserProtocolsEntry,
       "mfrapCfgFrPerfUserProtocolsIndex": mfrapCfgFrPerfUserProtocolsIndex,
       "mfrapCfgFrPerfUserProtocolsPortNum": mfrapCfgFrPerfUserProtocolsPortNum,
       "mfrapCfgFrPerfLTDlciFilterTable": mfrapCfgFrPerfLTDlciFilterTable,
       "mfrapCfgFrPerfLTDlciFilterEntry": mfrapCfgFrPerfLTDlciFilterEntry,
       "mfrapCfgFrPerfLTDlciFilterIndex": mfrapCfgFrPerfLTDlciFilterIndex,
       "mfrapCfgFrPerfLTDlciFilterDlciNum": mfrapCfgFrPerfLTDlciFilterDlciNum,
       "mfrapCfgFrPerfLTProtocolFilterTable": mfrapCfgFrPerfLTProtocolFilterTable,
       "mfrapCfgFrPerfLTProtocolFilterEntry": mfrapCfgFrPerfLTProtocolFilterEntry,
       "mfrapCfgFrPerfLTProtocolFilterIndex": mfrapCfgFrPerfLTProtocolFilterIndex,
       "mfrapCfgFrPerfLTProtocolFilterProtocol": mfrapCfgFrPerfLTProtocolFilterProtocol,
       "mfrapCfgFrPerfDlciDefaultUtilThreshold": mfrapCfgFrPerfDlciDefaultUtilThreshold,
       "mfrapCfgFrPerfDlciUtilDuration": mfrapCfgFrPerfDlciUtilDuration,
       "mfrapCfgFrPerfDlciNamesTableClear": mfrapCfgFrPerfDlciNamesTableClear,
       "mfrapCfgFrPerfUserProtocolsTableClear": mfrapCfgFrPerfUserProtocolsTableClear,
       "mfrapCfgFrPerfLTDlciFilterTableClear": mfrapCfgFrPerfLTDlciFilterTableClear,
       "mfrapCfgFrPerfLTProtocolFilterTableClear": mfrapCfgFrPerfLTProtocolFilterTableClear,
       "mfrapCfgFrPerfUnprovDlcisDelete": mfrapCfgFrPerfUnprovDlcisDelete,
       "mfrapCfgSecurityTable": mfrapCfgSecurityTable,
       "mfrapCfgTelnetCliLcdPassword": mfrapCfgTelnetCliLcdPassword,
       "mfrapCfgTftpPassword": mfrapCfgTftpPassword,
       "mfrapCfgCliPassword": mfrapCfgCliPassword,
       "mfrapCfgLcdPassword": mfrapCfgLcdPassword,
       "mfrapCfgGetCommunityString": mfrapCfgGetCommunityString,
       "mfrapCfgSetCommunityString": mfrapCfgSetCommunityString,
       "mfrapCfgLcdPswdEnable": mfrapCfgLcdPswdEnable,
       "mfrapCfgLcdPswdTimeout": mfrapCfgLcdPswdTimeout,
       "mfrapCfgConnectionTable": mfrapCfgConnectionTable,
       "mfrapCfgCurrentConnTable": mfrapCfgCurrentConnTable,
       "mfrapCfgCurrentConnEntry": mfrapCfgCurrentConnEntry,
       "mfrapCfgCurrentConnDestPort": mfrapCfgCurrentConnDestPort,
       "mfrapCfgCurrentConnDestDs0": mfrapCfgCurrentConnDestDs0,
       "mfrapCfgCurrentConnSrcPort": mfrapCfgCurrentConnSrcPort,
       "mfrapCfgCurrentConnSrcDs0": mfrapCfgCurrentConnSrcDs0,
       "mfrapCfgCurrentConnType": mfrapCfgCurrentConnType,
       "mfrapCfgEditConnections": mfrapCfgEditConnections,
       "mfrapCfgEditConnCopyCurrtoEdit": mfrapCfgEditConnCopyCurrtoEdit,
       "mfrapCfgEditClearEdit": mfrapCfgEditClearEdit,
       "mfrapCfgEditConnTable": mfrapCfgEditConnTable,
       "mfrapCfgEditConnEntry": mfrapCfgEditConnEntry,
       "mfrapCfgEditConnDestPort": mfrapCfgEditConnDestPort,
       "mfrapCfgEditConnDestDs0": mfrapCfgEditConnDestDs0,
       "mfrapCfgEditConnSrcPort": mfrapCfgEditConnSrcPort,
       "mfrapCfgEditConnSrcDs0": mfrapCfgEditConnSrcDs0,
       "mfrapCfgEditConnType": mfrapCfgEditConnType,
       "mfrapCfgEditDisconnect": mfrapCfgEditDisconnect,
       "mfrapCfgEditLastSetStatus": mfrapCfgEditLastSetStatus,
       "mfrapCfgEditConnStatus": mfrapCfgEditConnStatus,
       "mfrapCfgConnUpdateCmd": mfrapCfgConnUpdateCmd,
       "mfrapCfgDandiTable": mfrapCfgDandiTable,
       "mfrapCfgDandiFraming": mfrapCfgDandiFraming,
       "mfrapCfgDandiLineEncoding": mfrapCfgDandiLineEncoding,
       "mfrapCfgLock": mfrapCfgLock,
       "mfrapCfgLockID": mfrapCfgLockID,
       "mfrapCfgID": mfrapCfgID,
       "mfrapCfgStatus": mfrapCfgStatus,
       "mfrapCfgUnlock": mfrapCfgUnlock,
       "mfrapCfgUpdate": mfrapCfgUpdate,
       "mfrapDiagnostics": mfrapDiagnostics,
       "mfrapDiagUnitTable": mfrapDiagUnitTable,
       "mfrapDiagUnitLocLoop": mfrapDiagUnitLocLoop,
       "mfrapDiagUnitReset": mfrapDiagUnitReset,
       "mfrapDiagUnitTimeRemaining": mfrapDiagUnitTimeRemaining,
       "mfrapDiagT1Table": mfrapDiagT1Table,
       "mfrapDiagT1LocLineLpbk": mfrapDiagT1LocLineLpbk,
       "mfrapDiagT1LocPylLpbk": mfrapDiagT1LocPylLpbk,
       "mfrapDiagT1LocAggrLpbk": mfrapDiagT1LocAggrLpbk,
       "mfrapDiagT1RmtLpbkStatus": mfrapDiagT1RmtLpbkStatus,
       "mfrapDiagT1RmtLpbkCmd": mfrapDiagT1RmtLpbkCmd,
       "mfrapDiagT1TimeRemaining": mfrapDiagT1TimeRemaining,
       "mfrapDiagDteTable": mfrapDiagDteTable,
       "mfrapDiagDteSigRTS": mfrapDiagDteSigRTS,
       "mfrapDiagDteSigDTR": mfrapDiagDteSigDTR,
       "mfrapDiagDteLclLpbk": mfrapDiagDteLclLpbk,
       "mfrapDiagDteV54Lpbk": mfrapDiagDteV54Lpbk,
       "mfrapDiagDteRmtV54Lpbk": mfrapDiagDteRmtV54Lpbk,
       "mfrapDiagDteTimeRemaining": mfrapDiagDteTimeRemaining,
       "mfrapDiagBertTable": mfrapDiagBertTable,
       "mfrapDiagBertState": mfrapDiagBertState,
       "mfrapDiagBertStatus": mfrapDiagBertStatus,
       "mfrapDiagBertErrors": mfrapDiagBertErrors,
       "mfrapDiagBertErrSec": mfrapDiagBertErrSec,
       "mfrapDiagBertTimeElaps": mfrapDiagBertTimeElaps,
       "mfrapDiagBertResyncs": mfrapDiagBertResyncs,
       "mfrapDiagBertPattern": mfrapDiagBertPattern,
       "mfrapDiagVnipTable": mfrapDiagVnipTable,
       "mfrapDiagVnipEntry": mfrapDiagVnipEntry,
       "mfrapDiagVnipInterface": mfrapDiagVnipInterface,
       "mfrapDiagVnipIndex": mfrapDiagVnipIndex,
       "mfrapDiagVnipDlci": mfrapDiagVnipDlci,
       "mfrapDiagVnipIpAddr": mfrapDiagVnipIpAddr,
       "mfrapDiagVLOOP": mfrapDiagVLOOP,
       "mfrapDiagVBERT": mfrapDiagVBERT,
       "mfrapDiagVBERTRate": mfrapDiagVBERTRate,
       "mfrapDiagVBERTSize": mfrapDiagVBERTSize,
       "mfrapDiagVBERTPktPercent": mfrapDiagVBERTPktPercent,
       "mfrapDiagVBERTTestPeriod": mfrapDiagVBERTTestPeriod,
       "mfrapDiagDandiTable": mfrapDiagDandiTable,
       "mfrapDiagDandiLocLineLpbk": mfrapDiagDandiLocLineLpbk,
       "mfrapDiagDandiLocPylLpbk": mfrapDiagDandiLocPylLpbk,
       "mfrapDiagDandiTimeRemaining": mfrapDiagDandiTimeRemaining,
       "mfrapStatus": mfrapStatus,
       "mfrapStatusT1Table": mfrapStatusT1Table,
       "mfrapStatusT1Mode": mfrapStatusT1Mode,
       "mfrapStatusT1Status": mfrapStatusT1Status,
       "mfrapStatusT1Alarms": mfrapStatusT1Alarms,
       "mfrapVnipTopologyTable": mfrapVnipTopologyTable,
       "mfrapVnipTopologyEntry": mfrapVnipTopologyEntry,
       "mfrapVnipTopologyInterface": mfrapVnipTopologyInterface,
       "mfrapVnipTopologyIndex": mfrapVnipTopologyIndex,
       "mfrapVnipTopologyDlci": mfrapVnipTopologyDlci,
       "mfrapVnipTopologyIpAddr": mfrapVnipTopologyIpAddr,
       "mfrapVnipTopologyNumHops": mfrapVnipTopologyNumHops,
       "mfrapVnipTopologyLocalDlci": mfrapVnipTopologyLocalDlci,
       "mfrapVnipTopoTDNumSamples": mfrapVnipTopoTDNumSamples,
       "mfrapVnipTopoTDAvgDelay": mfrapVnipTopoTDAvgDelay,
       "mfrapVnipTopoTDMaxDelay": mfrapVnipTopoTDMaxDelay,
       "mfrapVnipTopoTDMinDelay": mfrapVnipTopoTDMinDelay,
       "mfrapVnipTopoTDLastDelay": mfrapVnipTopoTDLastDelay,
       "mfrapVnipTopoVLOOPStatus": mfrapVnipTopoVLOOPStatus,
       "mfrapVnipTopoVBERTStatus": mfrapVnipTopoVBERTStatus,
       "mfrapVnipTopoVBertTxDESetFrames": mfrapVnipTopoVBertTxDESetFrames,
       "mfrapVnipTopoVBertRxDESetFrames": mfrapVnipTopoVBertRxDESetFrames,
       "mfrapVnipTopoVBertTxDEClrFrames": mfrapVnipTopoVBertTxDEClrFrames,
       "mfrapVnipTopoVBertRxDEClrFrames": mfrapVnipTopoVBertRxDEClrFrames,
       "mfrapVnipTopoVBertTransitDelayMax": mfrapVnipTopoVBertTransitDelayMax,
       "mfrapVnipTopoVBertTransitDelayAvg": mfrapVnipTopoVBertTransitDelayAvg,
       "mfrapVnipTopoVBertTimeElapse": mfrapVnipTopoVBertTimeElapse,
       "mfrapVnipTopoVBertPerUtilCIR": mfrapVnipTopoVBertPerUtilCIR,
       "mfrapVnipTopoVBertPerUtilEIR": mfrapVnipTopoVBertPerUtilEIR,
       "mfrapStatusMgmtTable": mfrapStatusMgmtTable,
       "mfrapStatusMgmtChannel": mfrapStatusMgmtChannel,
       "mfrapStatusMgmtInterface": mfrapStatusMgmtInterface,
       "mfrapStatusMgmtInterfaceStatus": mfrapStatusMgmtInterfaceStatus,
       "mfrapStatusMgmtDefaultDLCINo": mfrapStatusMgmtDefaultDLCINo,
       "mfrapStatusMgmtDefaultDLCIStatus": mfrapStatusMgmtDefaultDLCIStatus,
       "mfrapStatusLedTable": mfrapStatusLedTable,
       "mfrapStatusDteModeLED": mfrapStatusDteModeLED,
       "mfrapStatusDteStatusLED": mfrapStatusDteStatusLED,
       "mfrapStatusDteTxLED": mfrapStatusDteTxLED,
       "mfrapStatusDteRxLED": mfrapStatusDteRxLED,
       "mfrapStatusT1ModeLED": mfrapStatusT1ModeLED,
       "mfrapStatusT1StatusLED": mfrapStatusT1StatusLED,
       "mfrapStatusAllLEDs": mfrapStatusAllLEDs,
       "mfrapStatusDandiModeLED": mfrapStatusDandiModeLED,
       "mfrapStatusDandiStatusLED": mfrapStatusDandiStatusLED,
       "mfrapVnipTransitDelayClear": mfrapVnipTransitDelayClear,
       "mfrapLmiSourcing": mfrapLmiSourcing,
       "mfrapStatusDteTable": mfrapStatusDteTable,
       "mfrapStatusDteMode": mfrapStatusDteMode,
       "mfrapStatusDteRts": mfrapStatusDteRts,
       "mfrapStatusDteDtr": mfrapStatusDteDtr,
       "mfrapStatusDteDcd": mfrapStatusDteDcd,
       "mfrapStatusDteDsr": mfrapStatusDteDsr,
       "mfrapStatusDteCts": mfrapStatusDteCts,
       "mfrapStatusLmiAutosense": mfrapStatusLmiAutosense,
       "mfrapStatusNestTable": mfrapStatusNestTable,
       "mfrapStatusNestFanOne": mfrapStatusNestFanOne,
       "mfrapStatusNestFanTwo": mfrapStatusNestFanTwo,
       "mfrapStatusNestPowerSupply": mfrapStatusNestPowerSupply,
       "mfrapStatusNestSlotId": mfrapStatusNestSlotId,
       "mfrapStatusDandiTable": mfrapStatusDandiTable,
       "mfrapStatusDandiMode": mfrapStatusDandiMode,
       "mfrapStatusDandiStatus": mfrapStatusDandiStatus,
       "mfrapStatusDandiAlarms": mfrapStatusDandiAlarms,
       "mfrapPerformance": mfrapPerformance,
       "mfrapPerfPhysicalIntf": mfrapPerfPhysicalIntf,
       "mfrapPerfT1CurrentTable": mfrapPerfT1CurrentTable,
       "mfrapT1CurrentEntry": mfrapT1CurrentEntry,
       "mfrapT1CurrentIndex": mfrapT1CurrentIndex,
       "mfrapT1CurrentCrc6Events": mfrapT1CurrentCrc6Events,
       "mfrapT1CurrentOofEvents": mfrapT1CurrentOofEvents,
       "mfrapT1CurrentESs": mfrapT1CurrentESs,
       "mfrapT1CurrentSESs": mfrapT1CurrentSESs,
       "mfrapT1CurrentSEFSs": mfrapT1CurrentSEFSs,
       "mfrapT1CurrentUASs": mfrapT1CurrentUASs,
       "mfrapT1CurrentCSSs": mfrapT1CurrentCSSs,
       "mfrapT1CurrentBESs": mfrapT1CurrentBESs,
       "mfrapT1CurrentLCVs": mfrapT1CurrentLCVs,
       "mfrapPerfT1IntervalTable": mfrapPerfT1IntervalTable,
       "mfrapT1IntervalEntry": mfrapT1IntervalEntry,
       "mfrapT1IntervalIndex": mfrapT1IntervalIndex,
       "mfrapT1IntervalNumber": mfrapT1IntervalNumber,
       "mfrapT1IntervalESs": mfrapT1IntervalESs,
       "mfrapT1IntervalSESs": mfrapT1IntervalSESs,
       "mfrapT1IntervalSEFSs": mfrapT1IntervalSEFSs,
       "mfrapT1IntervalUASs": mfrapT1IntervalUASs,
       "mfrapT1IntervalCSSs": mfrapT1IntervalCSSs,
       "mfrapT1IntervalBESs": mfrapT1IntervalBESs,
       "mfrapT1IntervalLCVs": mfrapT1IntervalLCVs,
       "mfrapPerfT1TotalTable": mfrapPerfT1TotalTable,
       "mfrapT1TotalEntry": mfrapT1TotalEntry,
       "mfrapT1TotalIndex": mfrapT1TotalIndex,
       "mfrapT1TotalESs": mfrapT1TotalESs,
       "mfrapT1TotalSESs": mfrapT1TotalSESs,
       "mfrapT1TotalSEFSs": mfrapT1TotalSEFSs,
       "mfrapT1TotalUASs": mfrapT1TotalUASs,
       "mfrapT1TotalCSSs": mfrapT1TotalCSSs,
       "mfrapT1TotalBESs": mfrapT1TotalBESs,
       "mfrapT1TotalLCVs": mfrapT1TotalLCVs,
       "mfrapT1PerfCmdTypeTable": mfrapT1PerfCmdTypeTable,
       "mfrapT1PerfFreezeState": mfrapT1PerfFreezeState,
       "mfrapT1PerfClearEvents": mfrapT1PerfClearEvents,
       "mfrapT1PerfClearAll": mfrapT1PerfClearAll,
       "mfrapPerfDandiCurrentTable": mfrapPerfDandiCurrentTable,
       "mfrapDandiCurrentEntry": mfrapDandiCurrentEntry,
       "mfrapDandiCurrentIndex": mfrapDandiCurrentIndex,
       "mfrapDandiCurrentCrc6Events": mfrapDandiCurrentCrc6Events,
       "mfrapDandiCurrentOofEvents": mfrapDandiCurrentOofEvents,
       "mfrapDandiCurrentESs": mfrapDandiCurrentESs,
       "mfrapDandiCurrentSESs": mfrapDandiCurrentSESs,
       "mfrapDandiCurrentSEFSs": mfrapDandiCurrentSEFSs,
       "mfrapDandiCurrentUASs": mfrapDandiCurrentUASs,
       "mfrapDandiCurrentCSSs": mfrapDandiCurrentCSSs,
       "mfrapDandiCurrentBESs": mfrapDandiCurrentBESs,
       "mfrapDandiCurrentLCVs": mfrapDandiCurrentLCVs,
       "mfrapPerfDandiIntervalTable": mfrapPerfDandiIntervalTable,
       "mfrapDandiIntervalEntry": mfrapDandiIntervalEntry,
       "mfrapDandiIntervalIndex": mfrapDandiIntervalIndex,
       "mfrapDandiIntervalNumber": mfrapDandiIntervalNumber,
       "mfrapDandiIntervalESs": mfrapDandiIntervalESs,
       "mfrapDandiIntervalSESs": mfrapDandiIntervalSESs,
       "mfrapDandiIntervalSEFSs": mfrapDandiIntervalSEFSs,
       "mfrapDandiIntervalUASs": mfrapDandiIntervalUASs,
       "mfrapDandiIntervalCSSs": mfrapDandiIntervalCSSs,
       "mfrapDandiIntervalBESs": mfrapDandiIntervalBESs,
       "mfrapDandiIntervalLCVs": mfrapDandiIntervalLCVs,
       "mfrapPerfDandiTotalTable": mfrapPerfDandiTotalTable,
       "mfrapDandiTotalEntry": mfrapDandiTotalEntry,
       "mfrapDandiTotalIndex": mfrapDandiTotalIndex,
       "mfrapDandiTotalESs": mfrapDandiTotalESs,
       "mfrapDandiTotalSESs": mfrapDandiTotalSESs,
       "mfrapDandiTotalSEFSs": mfrapDandiTotalSEFSs,
       "mfrapDandiTotalUASs": mfrapDandiTotalUASs,
       "mfrapDandiTotalCSSs": mfrapDandiTotalCSSs,
       "mfrapDandiTotalBESs": mfrapDandiTotalBESs,
       "mfrapDandiTotalLCVs": mfrapDandiTotalLCVs,
       "mfrapDandiPerfCmdTypeTable": mfrapDandiPerfCmdTypeTable,
       "mfrapDandiPerfFreezeState": mfrapDandiPerfFreezeState,
       "mfrapDandiPerfClearEvents": mfrapDandiPerfClearEvents,
       "mfrapDandiPerfClearAll": mfrapDandiPerfClearAll,
       "mfrapPerfMgmtIp": mfrapPerfMgmtIp,
       "mfrapPerfMgmtIpIFStatsTable": mfrapPerfMgmtIpIFStatsTable,
       "mfrapPerfMgmtIpIFInOctets": mfrapPerfMgmtIpIFInOctets,
       "mfrapPerfMgmtIpIFInErrors": mfrapPerfMgmtIpIFInErrors,
       "mfrapPerfMgmtIpIFOutOctets": mfrapPerfMgmtIpIFOutOctets,
       "mfrapPerfMgmtIpIFOperStatus": mfrapPerfMgmtIpIFOperStatus,
       "mfrapPerfMgmtIpIPStatsTable": mfrapPerfMgmtIpIPStatsTable,
       "mfrapPerfMgmtIpIPInRcv": mfrapPerfMgmtIpIPInRcv,
       "mfrapPerfMgmtIpIPInHdrErr": mfrapPerfMgmtIpIPInHdrErr,
       "mfrapPerfMgmtIpIPInAddrErr": mfrapPerfMgmtIpIPInAddrErr,
       "mfrapPerfMgmtIpIPInProtUnk": mfrapPerfMgmtIpIPInProtUnk,
       "mfrapPerfMgmtIpIPInDscrd": mfrapPerfMgmtIpIPInDscrd,
       "mfrapPerfMgmtIpIPInDlvrs": mfrapPerfMgmtIpIPInDlvrs,
       "mfrapPerfMgmtIpIPOutRqst": mfrapPerfMgmtIpIPOutRqst,
       "mfrapPerfMgmtIpIPOutDscrd": mfrapPerfMgmtIpIPOutDscrd,
       "mfrapPerfMgmtIpIPOutNoRt": mfrapPerfMgmtIpIPOutNoRt,
       "mfrapPerfMgmtIpICMPStatsTable": mfrapPerfMgmtIpICMPStatsTable,
       "mfrapPerfMgmtIpICMPInMsgs": mfrapPerfMgmtIpICMPInMsgs,
       "mfrapPerfMgmtIpICMPInErrors": mfrapPerfMgmtIpICMPInErrors,
       "mfrapPerfMgmtIpICMPInDestUnreachs": mfrapPerfMgmtIpICMPInDestUnreachs,
       "mfrapPerfMgmtIpICMPInTimeExcds": mfrapPerfMgmtIpICMPInTimeExcds,
       "mfrapPerfMgmtIpICMPInParmProbs": mfrapPerfMgmtIpICMPInParmProbs,
       "mfrapPerfMgmtIpICMPInRedirects": mfrapPerfMgmtIpICMPInRedirects,
       "mfrapPerfMgmtIpICMPInEchos": mfrapPerfMgmtIpICMPInEchos,
       "mfrapPerfMgmtIpICMPInEchoReps": mfrapPerfMgmtIpICMPInEchoReps,
       "mfrapPerfMgmtIpICMPOutMsgs": mfrapPerfMgmtIpICMPOutMsgs,
       "mfrapPerfMgmtIpICMPOutErrors": mfrapPerfMgmtIpICMPOutErrors,
       "mfrapPerfMgmtIpICMPOutDestUnreachs": mfrapPerfMgmtIpICMPOutDestUnreachs,
       "mfrapPerfMgmtIpICMPOutParmProbs": mfrapPerfMgmtIpICMPOutParmProbs,
       "mfrapPerfMgmtIpICMPOutRedirects": mfrapPerfMgmtIpICMPOutRedirects,
       "mfrapPerfMgmtIpICMPOutEchos": mfrapPerfMgmtIpICMPOutEchos,
       "mfrapPerfMgmtIpICMPOutEchoReps": mfrapPerfMgmtIpICMPOutEchoReps,
       "mfrapPerfMgmtIpUDPStatsTable": mfrapPerfMgmtIpUDPStatsTable,
       "mfrapPerfMgmtIpUDPInDatagrams": mfrapPerfMgmtIpUDPInDatagrams,
       "mfrapPerfMgmtIpUDPOutDatagrams": mfrapPerfMgmtIpUDPOutDatagrams,
       "mfrapPerfMgmtIpUDPNoPorts": mfrapPerfMgmtIpUDPNoPorts,
       "mfrapPerfMgmtIpTCPStatsTable": mfrapPerfMgmtIpTCPStatsTable,
       "mfrapPerfMgmtIpTCPActiveOpens": mfrapPerfMgmtIpTCPActiveOpens,
       "mfrapPerfMgmtIpTCPPassiveOpens": mfrapPerfMgmtIpTCPPassiveOpens,
       "mfrapPerfMgmtIpTCPAttemptFails": mfrapPerfMgmtIpTCPAttemptFails,
       "mfrapPerfMgmtIpTCPCurrEstab": mfrapPerfMgmtIpTCPCurrEstab,
       "mfrapPerfMgmtIpTCPInSegs": mfrapPerfMgmtIpTCPInSegs,
       "mfrapPerfMgmtIpTCPOutSegs": mfrapPerfMgmtIpTCPOutSegs,
       "mfrapPerfThruput": mfrapPerfThruput,
       "mfrapPerfThruputPerIntfTable": mfrapPerfThruputPerIntfTable,
       "mfrapPerfThruputPerIntfEntry": mfrapPerfThruputPerIntfEntry,
       "mfrapPerfThruputPerIntfIndex": mfrapPerfThruputPerIntfIndex,
       "mfrapPerfThruputPerIntfRxByteCnt": mfrapPerfThruputPerIntfRxByteCnt,
       "mfrapPerfThruputPerIntfTxByteCnt": mfrapPerfThruputPerIntfTxByteCnt,
       "mfrapPerfThruputPerIntfRxFrameCnt": mfrapPerfThruputPerIntfRxFrameCnt,
       "mfrapPerfThruputPerIntfTxFrameCnt": mfrapPerfThruputPerIntfTxFrameCnt,
       "mfrapPerfThruputPerIntfRxCrcErrCnt": mfrapPerfThruputPerIntfRxCrcErrCnt,
       "mfrapPerfThruputPerIntfRxAbortCnt": mfrapPerfThruputPerIntfRxAbortCnt,
       "mfrapPerfThruputPerDlciTable": mfrapPerfThruputPerDlciTable,
       "mfrapPerfThruputPerDlciEntry": mfrapPerfThruputPerDlciEntry,
       "mfrapPerfThruputPerDlciIndex": mfrapPerfThruputPerDlciIndex,
       "mfrapPerfThruputPerDlciValue": mfrapPerfThruputPerDlciValue,
       "mfrapPerfThruputPerDlciCreateTime": mfrapPerfThruputPerDlciCreateTime,
       "mfrapPerfThruputPerDlciChangeTime": mfrapPerfThruputPerDlciChangeTime,
       "mfrapPerfThruputPerDlciRxByte": mfrapPerfThruputPerDlciRxByte,
       "mfrapPerfThruputPerDlciTxByte": mfrapPerfThruputPerDlciTxByte,
       "mfrapPerfThruputPerDlciRxFrame": mfrapPerfThruputPerDlciRxFrame,
       "mfrapPerfThruputPerDlciTxFrame": mfrapPerfThruputPerDlciTxFrame,
       "mfrapPerfThruputPerDlciRxFecn": mfrapPerfThruputPerDlciRxFecn,
       "mfrapPerfThruputPerDlciRxBecn": mfrapPerfThruputPerDlciRxBecn,
       "mfrapPerfThruputPerDlciRxDe": mfrapPerfThruputPerDlciRxDe,
       "mfrapPerfThruputPerDlciTxDe": mfrapPerfThruputPerDlciTxDe,
       "mfrapPerfThruputPerDlciRxThruput": mfrapPerfThruputPerDlciRxThruput,
       "mfrapPerfThruputPerDlciTxThruput": mfrapPerfThruputPerDlciTxThruput,
       "mfrapPerfThruputPerDlciCIR": mfrapPerfThruputPerDlciCIR,
       "mfrapPerfThruputPerDlciUptime": mfrapPerfThruputPerDlciUptime,
       "mfrapPerfThruputPerDlciDowntime": mfrapPerfThruputPerDlciDowntime,
       "mfrapPerfThruputPerDlciCirType": mfrapPerfThruputPerDlciCirType,
       "mfrapPerfThruputPerDlciPvcState": mfrapPerfThruputPerDlciPvcState,
       "mfrapPerfThruputPerDlciOutageCount": mfrapPerfThruputPerDlciOutageCount,
       "mfrapPerfThruputPerDlciAvailability": mfrapPerfThruputPerDlciAvailability,
       "mfrapPerfThruputPerDlciMTBSO": mfrapPerfThruputPerDlciMTBSO,
       "mfrapPerfThruputPerDlciMTTSR": mfrapPerfThruputPerDlciMTTSR,
       "mfrapPerfThruputPerDlciEncapType": mfrapPerfThruputPerDlciEncapType,
       "mfrapPerfThruputPerDlciRxUtilizationStatus": mfrapPerfThruputPerDlciRxUtilizationStatus,
       "mfrapPerfThruputPerDlciTxUtilizationStatus": mfrapPerfThruputPerDlciTxUtilizationStatus,
       "mfrapPerfThruputPerDlciEIR": mfrapPerfThruputPerDlciEIR,
       "mfrapPerfThruputCommands": mfrapPerfThruputCommands,
       "mfrapPerfThruputCmdClearDteStats": mfrapPerfThruputCmdClearDteStats,
       "mfrapPerfThruputCmdClearT1Stats": mfrapPerfThruputCmdClearT1Stats,
       "mfrapPerfThruputCmdClearAllIntfStats": mfrapPerfThruputCmdClearAllIntfStats,
       "mfrapPerfThruputCmdClearDlciStats": mfrapPerfThruputCmdClearDlciStats,
       "mfrapPerfThruputCmdClearAllStats": mfrapPerfThruputCmdClearAllStats,
       "mfrapPerfThruputCmdRemoveStsDlci": mfrapPerfThruputCmdRemoveStsDlci,
       "mfrapPerfThruputCmdReplaceDlciTable": mfrapPerfThruputCmdReplaceDlciTable,
       "mfrapPerfThruputCmdReplaceDlciEntry": mfrapPerfThruputCmdReplaceDlciEntry,
       "mfrapPerfThruputCmdReplaceDlciValue": mfrapPerfThruputCmdReplaceDlciValue,
       "mfrapPerfThruputCmdReplaceDlciNewValue": mfrapPerfThruputCmdReplaceDlciNewValue,
       "mfrapPerfThruputCmdAvailabilityStsDlciReset": mfrapPerfThruputCmdAvailabilityStsDlciReset,
       "mfrapPerfThruputCmdAvailabilityStsDlciResetAll": mfrapPerfThruputCmdAvailabilityStsDlciResetAll,
       "mfrapPerfThruputCmdCountsStsDlciReset": mfrapPerfThruputCmdCountsStsDlciReset,
       "mfrapPerfThruputCmdCountsStsDlciResetAll": mfrapPerfThruputCmdCountsStsDlciResetAll,
       "mfrapPerfThruputCmdAllStsDlciReset": mfrapPerfThruputCmdAllStsDlciReset,
       "mfrapPerfThruputCmdAllStsDlciResetAll": mfrapPerfThruputCmdAllStsDlciResetAll,
       "mfrapPerfNetworkShortTerm": mfrapPerfNetworkShortTerm,
       "mfrapPerfNetwProtoPerDlciTable": mfrapPerfNetwProtoPerDlciTable,
       "mfrapPerfNetwProtoPerDlciEntry": mfrapPerfNetwProtoPerDlciEntry,
       "mfrapPerfNetwProtoPerDlciInterval": mfrapPerfNetwProtoPerDlciInterval,
       "mfrapPerfNetwProtoPerDlciValue": mfrapPerfNetwProtoPerDlciValue,
       "mfrapPerfNetwProtoPerDlciRxTotal": mfrapPerfNetwProtoPerDlciRxTotal,
       "mfrapPerfNetwProtoPerDlciTxTotal": mfrapPerfNetwProtoPerDlciTxTotal,
       "mfrapPerfNetwProtoPerDlciRxIp": mfrapPerfNetwProtoPerDlciRxIp,
       "mfrapPerfNetwProtoPerDlciTxIp": mfrapPerfNetwProtoPerDlciTxIp,
       "mfrapPerfNetwProtoPerDlciRxIpx": mfrapPerfNetwProtoPerDlciRxIpx,
       "mfrapPerfNetwProtoPerDlciTxIpx": mfrapPerfNetwProtoPerDlciTxIpx,
       "mfrapPerfNetwProtoPerDlciRxSna": mfrapPerfNetwProtoPerDlciRxSna,
       "mfrapPerfNetwProtoPerDlciTxSna": mfrapPerfNetwProtoPerDlciTxSna,
       "mfrapPerfNetwProtoPerDlciRxArp": mfrapPerfNetwProtoPerDlciRxArp,
       "mfrapPerfNetwProtoPerDlciTxArp": mfrapPerfNetwProtoPerDlciTxArp,
       "mfrapPerfNetwProtoPerDlciRxCisco": mfrapPerfNetwProtoPerDlciRxCisco,
       "mfrapPerfNetwProtoPerDlciTxCisco": mfrapPerfNetwProtoPerDlciTxCisco,
       "mfrapPerfNetwProtoPerDlciRxOther": mfrapPerfNetwProtoPerDlciRxOther,
       "mfrapPerfNetwProtoPerDlciTxOther": mfrapPerfNetwProtoPerDlciTxOther,
       "mfrapPerfNetwProtoPerDlciRxVnip": mfrapPerfNetwProtoPerDlciRxVnip,
       "mfrapPerfNetwProtoPerDlciTxVnip": mfrapPerfNetwProtoPerDlciTxVnip,
       "mfrapPerfNetwProtoPerDlciRxAnnexG": mfrapPerfNetwProtoPerDlciRxAnnexG,
       "mfrapPerfNetwProtoPerDlciTxAnnexG": mfrapPerfNetwProtoPerDlciTxAnnexG,
       "mfrapPerfNetwProtoTotalTable": mfrapPerfNetwProtoTotalTable,
       "mfrapPerfNetwProtoTotalEntry": mfrapPerfNetwProtoTotalEntry,
       "mfrapPerfNetwProtoTotalInterval": mfrapPerfNetwProtoTotalInterval,
       "mfrapPerfNetwProtoTotalRxTotal": mfrapPerfNetwProtoTotalRxTotal,
       "mfrapPerfNetwProtoTotalTxTotal": mfrapPerfNetwProtoTotalTxTotal,
       "mfrapPerfNetwProtoTotalRxIp": mfrapPerfNetwProtoTotalRxIp,
       "mfrapPerfNetwProtoTotalTxIp": mfrapPerfNetwProtoTotalTxIp,
       "mfrapPerfNetwProtoTotalRxIpx": mfrapPerfNetwProtoTotalRxIpx,
       "mfrapPerfNetwProtoTotalTxIpx": mfrapPerfNetwProtoTotalTxIpx,
       "mfrapPerfNetwProtoTotalRxSna": mfrapPerfNetwProtoTotalRxSna,
       "mfrapPerfNetwProtoTotalTxSna": mfrapPerfNetwProtoTotalTxSna,
       "mfrapPerfNetwProtoTotalRxArp": mfrapPerfNetwProtoTotalRxArp,
       "mfrapPerfNetwProtoTotalTxArp": mfrapPerfNetwProtoTotalTxArp,
       "mfrapPerfNetwProtoTotalRxCisco": mfrapPerfNetwProtoTotalRxCisco,
       "mfrapPerfNetwProtoTotalTxCisco": mfrapPerfNetwProtoTotalTxCisco,
       "mfrapPerfNetwProtoTotalRxOther": mfrapPerfNetwProtoTotalRxOther,
       "mfrapPerfNetwProtoTotalTxOther": mfrapPerfNetwProtoTotalTxOther,
       "mfrapPerfNetwProtoTotalRxVnip": mfrapPerfNetwProtoTotalRxVnip,
       "mfrapPerfNetwProtoTotalTxVnip": mfrapPerfNetwProtoTotalTxVnip,
       "mfrapPerfNetwProtoTotalRxAnnexG": mfrapPerfNetwProtoTotalRxAnnexG,
       "mfrapPerfNetwProtoTotalTxAnnexG": mfrapPerfNetwProtoTotalTxAnnexG,
       "mfrapPerfIpPerDlciTable": mfrapPerfIpPerDlciTable,
       "mfrapPerfIpPerDlciEntry": mfrapPerfIpPerDlciEntry,
       "mfrapPerfIpPerDlciInterval": mfrapPerfIpPerDlciInterval,
       "mfrapPerfIpPerDlciValue": mfrapPerfIpPerDlciValue,
       "mfrapPerfIpPerDlciRxTotal": mfrapPerfIpPerDlciRxTotal,
       "mfrapPerfIpPerDlciTxTotal": mfrapPerfIpPerDlciTxTotal,
       "mfrapPerfIpPerDlciRxTcp": mfrapPerfIpPerDlciRxTcp,
       "mfrapPerfIpPerDlciTxTcp": mfrapPerfIpPerDlciTxTcp,
       "mfrapPerfIpPerDlciRxUdp": mfrapPerfIpPerDlciRxUdp,
       "mfrapPerfIpPerDlciTxUdp": mfrapPerfIpPerDlciTxUdp,
       "mfrapPerfIpPerDlciRxIcmp": mfrapPerfIpPerDlciRxIcmp,
       "mfrapPerfIpPerDlciTxIcmp": mfrapPerfIpPerDlciTxIcmp,
       "mfrapPerfIpPerDlciRxOther": mfrapPerfIpPerDlciRxOther,
       "mfrapPerfIpPerDlciTxOther": mfrapPerfIpPerDlciTxOther,
       "mfrapPerfIpPerDlciRxIgrp": mfrapPerfIpPerDlciRxIgrp,
       "mfrapPerfIpPerDlciTxIgrp": mfrapPerfIpPerDlciTxIgrp,
       "mfrapPerfIpTotalTable": mfrapPerfIpTotalTable,
       "mfrapPerfIpTotalEntry": mfrapPerfIpTotalEntry,
       "mfrapPerfIpTotalInterval": mfrapPerfIpTotalInterval,
       "mfrapPerfIpTotalRxTotal": mfrapPerfIpTotalRxTotal,
       "mfrapPerfIpTotalTxTotal": mfrapPerfIpTotalTxTotal,
       "mfrapPerfIpTotalRxTcp": mfrapPerfIpTotalRxTcp,
       "mfrapPerfIpTotalTxTcp": mfrapPerfIpTotalTxTcp,
       "mfrapPerfIpTotalRxUdp": mfrapPerfIpTotalRxUdp,
       "mfrapPerfIpTotalTxUdp": mfrapPerfIpTotalTxUdp,
       "mfrapPerfIpTotalRxIcmp": mfrapPerfIpTotalRxIcmp,
       "mfrapPerfIpTotalTxIcmp": mfrapPerfIpTotalTxIcmp,
       "mfrapPerfIpTotalRxOther": mfrapPerfIpTotalRxOther,
       "mfrapPerfIpTotalTxOther": mfrapPerfIpTotalTxOther,
       "mfrapPerfIpTotalRxIgrp": mfrapPerfIpTotalRxIgrp,
       "mfrapPerfIpTotalTxIgrp": mfrapPerfIpTotalTxIgrp,
       "mfrapPerfIcmpPerDlciTable": mfrapPerfIcmpPerDlciTable,
       "mfrapPerfIcmpPerDlciEntry": mfrapPerfIcmpPerDlciEntry,
       "mfrapPerfIcmpPerDlciInterval": mfrapPerfIcmpPerDlciInterval,
       "mfrapPerfIcmpPerDlciValue": mfrapPerfIcmpPerDlciValue,
       "mfrapPerfIcmpPerDlciRxTotal": mfrapPerfIcmpPerDlciRxTotal,
       "mfrapPerfIcmpPerDlciTxTotal": mfrapPerfIcmpPerDlciTxTotal,
       "mfrapPerfIcmpPerDlciRxEchoRep": mfrapPerfIcmpPerDlciRxEchoRep,
       "mfrapPerfIcmpPerDlciTxEchoRep": mfrapPerfIcmpPerDlciTxEchoRep,
       "mfrapPerfIcmpPerDlciRxDestUnr": mfrapPerfIcmpPerDlciRxDestUnr,
       "mfrapPerfIcmpPerDlciTxDestUnr": mfrapPerfIcmpPerDlciTxDestUnr,
       "mfrapPerfIcmpPerDlciRxSrcQuench": mfrapPerfIcmpPerDlciRxSrcQuench,
       "mfrapPerfIcmpPerDlciTxSrcQuench": mfrapPerfIcmpPerDlciTxSrcQuench,
       "mfrapPerfIcmpPerDlciRxRedirect": mfrapPerfIcmpPerDlciRxRedirect,
       "mfrapPerfIcmpPerDlciTxRedirect": mfrapPerfIcmpPerDlciTxRedirect,
       "mfrapPerfIcmpPerDlciRxEchoReq": mfrapPerfIcmpPerDlciRxEchoReq,
       "mfrapPerfIcmpPerDlciTxEchoReq": mfrapPerfIcmpPerDlciTxEchoReq,
       "mfrapPerfIcmpPerDlciRxTimeExcd": mfrapPerfIcmpPerDlciRxTimeExcd,
       "mfrapPerfIcmpPerDlciTxTimeExcd": mfrapPerfIcmpPerDlciTxTimeExcd,
       "mfrapPerfIcmpPerDlciRxParamProb": mfrapPerfIcmpPerDlciRxParamProb,
       "mfrapPerfIcmpPerDlciTxParamProb": mfrapPerfIcmpPerDlciTxParamProb,
       "mfrapPerfIcmpPerDlciRxTimestpReq": mfrapPerfIcmpPerDlciRxTimestpReq,
       "mfrapPerfIcmpPerDlciTxTimestpReq": mfrapPerfIcmpPerDlciTxTimestpReq,
       "mfrapPerfIcmpPerDlciRxTimestpRep": mfrapPerfIcmpPerDlciRxTimestpRep,
       "mfrapPerfIcmpPerDlciTxTimestpRep": mfrapPerfIcmpPerDlciTxTimestpRep,
       "mfrapPerfIcmpPerDlciRxAddrMaskReq": mfrapPerfIcmpPerDlciRxAddrMaskReq,
       "mfrapPerfIcmpPerDlciTxAddrMaskReq": mfrapPerfIcmpPerDlciTxAddrMaskReq,
       "mfrapPerfIcmpPerDlciRxAddrMaskRep": mfrapPerfIcmpPerDlciRxAddrMaskRep,
       "mfrapPerfIcmpPerDlciTxAddrMaskRep": mfrapPerfIcmpPerDlciTxAddrMaskRep,
       "mfrapPerfIcmpPerDlciRxPktTooBig": mfrapPerfIcmpPerDlciRxPktTooBig,
       "mfrapPerfIcmpPerDlciTxPktTooBig": mfrapPerfIcmpPerDlciTxPktTooBig,
       "mfrapPerfIcmpPerDlciRxGmQuery": mfrapPerfIcmpPerDlciRxGmQuery,
       "mfrapPerfIcmpPerDlciTxGmQuery": mfrapPerfIcmpPerDlciTxGmQuery,
       "mfrapPerfIcmpPerDlciRxGmReport": mfrapPerfIcmpPerDlciRxGmReport,
       "mfrapPerfIcmpPerDlciTxGmReport": mfrapPerfIcmpPerDlciTxGmReport,
       "mfrapPerfIcmpPerDlciRxGmReduct": mfrapPerfIcmpPerDlciRxGmReduct,
       "mfrapPerfIcmpPerDlciTxGmReduct": mfrapPerfIcmpPerDlciTxGmReduct,
       "mfrapPerfIcmpTotalTable": mfrapPerfIcmpTotalTable,
       "mfrapPerfIcmpTotalEntry": mfrapPerfIcmpTotalEntry,
       "mfrapPerfIcmpTotalInterval": mfrapPerfIcmpTotalInterval,
       "mfrapPerfIcmpTotalRxTotal": mfrapPerfIcmpTotalRxTotal,
       "mfrapPerfIcmpTotalTxTotal": mfrapPerfIcmpTotalTxTotal,
       "mfrapPerfIcmpTotalRxEchoRep": mfrapPerfIcmpTotalRxEchoRep,
       "mfrapPerfIcmpTotalTxEchoRep": mfrapPerfIcmpTotalTxEchoRep,
       "mfrapPerfIcmpTotalRxDestUnr": mfrapPerfIcmpTotalRxDestUnr,
       "mfrapPerfIcmpTotalTxDestUnr": mfrapPerfIcmpTotalTxDestUnr,
       "mfrapPerfIcmpTotalRxSrcQuench": mfrapPerfIcmpTotalRxSrcQuench,
       "mfrapPerfIcmpTotalTxSrcQuench": mfrapPerfIcmpTotalTxSrcQuench,
       "mfrapPerfIcmpTotalRxRedirect": mfrapPerfIcmpTotalRxRedirect,
       "mfrapPerfIcmpTotalTxRedirect": mfrapPerfIcmpTotalTxRedirect,
       "mfrapPerfIcmpTotalRxEchoReq": mfrapPerfIcmpTotalRxEchoReq,
       "mfrapPerfIcmpTotalTxEchoReq": mfrapPerfIcmpTotalTxEchoReq,
       "mfrapPerfIcmpTotalRxTimeExcd": mfrapPerfIcmpTotalRxTimeExcd,
       "mfrapPerfIcmpTotalTxTimeExcd": mfrapPerfIcmpTotalTxTimeExcd,
       "mfrapPerfIcmpTotalRxParamProb": mfrapPerfIcmpTotalRxParamProb,
       "mfrapPerfIcmpTotalTxParamProb": mfrapPerfIcmpTotalTxParamProb,
       "mfrapPerfIcmpTotalRxTimestpReq": mfrapPerfIcmpTotalRxTimestpReq,
       "mfrapPerfIcmpTotalTxTimestpReq": mfrapPerfIcmpTotalTxTimestpReq,
       "mfrapPerfIcmpTotalRxTimestpRep": mfrapPerfIcmpTotalRxTimestpRep,
       "mfrapPerfIcmpTotalTxTimestpRep": mfrapPerfIcmpTotalTxTimestpRep,
       "mfrapPerfIcmpTotalRxAddrMaskReq": mfrapPerfIcmpTotalRxAddrMaskReq,
       "mfrapPerfIcmpTotalTxAddrMaskReq": mfrapPerfIcmpTotalTxAddrMaskReq,
       "mfrapPerfIcmpTotalRxAddrMaskRep": mfrapPerfIcmpTotalRxAddrMaskRep,
       "mfrapPerfIcmpTotalTxAddrMaskRep": mfrapPerfIcmpTotalTxAddrMaskRep,
       "mfrapPerfIcmpTotalRxPktTooBig": mfrapPerfIcmpTotalRxPktTooBig,
       "mfrapPerfIcmpTotalTxPktTooBig": mfrapPerfIcmpTotalTxPktTooBig,
       "mfrapPerfIcmpTotalRxGmQuery": mfrapPerfIcmpTotalRxGmQuery,
       "mfrapPerfIcmpTotalTxGmQuery": mfrapPerfIcmpTotalTxGmQuery,
       "mfrapPerfIcmpTotalRxGmReport": mfrapPerfIcmpTotalRxGmReport,
       "mfrapPerfIcmpTotalTxGmReport": mfrapPerfIcmpTotalTxGmReport,
       "mfrapPerfIcmpTotalRxGmReduct": mfrapPerfIcmpTotalRxGmReduct,
       "mfrapPerfIcmpTotalTxGmReduct": mfrapPerfIcmpTotalTxGmReduct,
       "mfrapPerfApplicationPerDlciTable": mfrapPerfApplicationPerDlciTable,
       "mfrapPerfApplicationPerDlciEntry": mfrapPerfApplicationPerDlciEntry,
       "mfrapPerfApplicationPerDlciInterval": mfrapPerfApplicationPerDlciInterval,
       "mfrapPerfApplicationPerDlciValue": mfrapPerfApplicationPerDlciValue,
       "mfrapPerfApplicationPerDlciRxSnmp": mfrapPerfApplicationPerDlciRxSnmp,
       "mfrapPerfApplicationPerDlciTxSnmp": mfrapPerfApplicationPerDlciTxSnmp,
       "mfrapPerfApplicationPerDlciRxSnmpTrap": mfrapPerfApplicationPerDlciRxSnmpTrap,
       "mfrapPerfApplicationPerDlciTxSnmpTrap": mfrapPerfApplicationPerDlciTxSnmpTrap,
       "mfrapPerfApplicationPerDlciRxHttp": mfrapPerfApplicationPerDlciRxHttp,
       "mfrapPerfApplicationPerDlciTxHttp": mfrapPerfApplicationPerDlciTxHttp,
       "mfrapPerfApplicationPerDlciRxTelnet": mfrapPerfApplicationPerDlciRxTelnet,
       "mfrapPerfApplicationPerDlciTxTelnet": mfrapPerfApplicationPerDlciTxTelnet,
       "mfrapPerfApplicationPerDlciRxSmtp": mfrapPerfApplicationPerDlciRxSmtp,
       "mfrapPerfApplicationPerDlciTxSmtp": mfrapPerfApplicationPerDlciTxSmtp,
       "mfrapPerfApplicationPerDlciRxFtp": mfrapPerfApplicationPerDlciRxFtp,
       "mfrapPerfApplicationPerDlciTxFtp": mfrapPerfApplicationPerDlciTxFtp,
       "mfrapPerfApplicationPerDlciRxTftp": mfrapPerfApplicationPerDlciRxTftp,
       "mfrapPerfApplicationPerDlciTxTftp": mfrapPerfApplicationPerDlciTxTftp,
       "mfrapPerfApplicationPerDlciRxCustom1": mfrapPerfApplicationPerDlciRxCustom1,
       "mfrapPerfApplicationPerDlciTxCustom1": mfrapPerfApplicationPerDlciTxCustom1,
       "mfrapPerfApplicationPerDlciRxCustom2": mfrapPerfApplicationPerDlciRxCustom2,
       "mfrapPerfApplicationPerDlciTxCustom2": mfrapPerfApplicationPerDlciTxCustom2,
       "mfrapPerfApplicationPerDlciRxCustom3": mfrapPerfApplicationPerDlciRxCustom3,
       "mfrapPerfApplicationPerDlciTxCustom3": mfrapPerfApplicationPerDlciTxCustom3,
       "mfrapPerfApplicationPerDlciRxCustom4": mfrapPerfApplicationPerDlciRxCustom4,
       "mfrapPerfApplicationPerDlciTxCustom4": mfrapPerfApplicationPerDlciTxCustom4,
       "mfrapPerfApplicationTotalTable": mfrapPerfApplicationTotalTable,
       "mfrapPerfApplicationTotalEntry": mfrapPerfApplicationTotalEntry,
       "mfrapPerfApplicationTotalInterval": mfrapPerfApplicationTotalInterval,
       "mfrapPerfApplicationTotalRxSnmp": mfrapPerfApplicationTotalRxSnmp,
       "mfrapPerfApplicationTotalTxSnmp": mfrapPerfApplicationTotalTxSnmp,
       "mfrapPerfApplicationTotalRxSnmpTrap": mfrapPerfApplicationTotalRxSnmpTrap,
       "mfrapPerfApplicationTotalTxSnmpTrap": mfrapPerfApplicationTotalTxSnmpTrap,
       "mfrapPerfApplicationTotalRxHttp": mfrapPerfApplicationTotalRxHttp,
       "mfrapPerfApplicationTotalTxHttp": mfrapPerfApplicationTotalTxHttp,
       "mfrapPerfApplicationTotalRxTelnet": mfrapPerfApplicationTotalRxTelnet,
       "mfrapPerfApplicationTotalTxTelnet": mfrapPerfApplicationTotalTxTelnet,
       "mfrapPerfApplicationTotalRxSmtp": mfrapPerfApplicationTotalRxSmtp,
       "mfrapPerfApplicationTotalTxSmtp": mfrapPerfApplicationTotalTxSmtp,
       "mfrapPerfApplicationTotalRxFtp": mfrapPerfApplicationTotalRxFtp,
       "mfrapPerfApplicationTotalTxFtp": mfrapPerfApplicationTotalTxFtp,
       "mfrapPerfApplicationTotalRxTftp": mfrapPerfApplicationTotalRxTftp,
       "mfrapPerfApplicationTotalTxTftp": mfrapPerfApplicationTotalTxTftp,
       "mfrapPerfApplicationTotalRxCustom1": mfrapPerfApplicationTotalRxCustom1,
       "mfrapPerfApplicationTotalTxCustom1": mfrapPerfApplicationTotalTxCustom1,
       "mfrapPerfApplicationTotalRxCustom2": mfrapPerfApplicationTotalRxCustom2,
       "mfrapPerfApplicationTotalTxCustom2": mfrapPerfApplicationTotalTxCustom2,
       "mfrapPerfApplicationTotalRxCustom3": mfrapPerfApplicationTotalRxCustom3,
       "mfrapPerfApplicationTotalTxCustom3": mfrapPerfApplicationTotalTxCustom3,
       "mfrapPerfApplicationTotalRxCustom4": mfrapPerfApplicationTotalRxCustom4,
       "mfrapPerfApplicationTotalTxCustom4": mfrapPerfApplicationTotalTxCustom4,
       "mfrapPerfRoutingPerDlciTable": mfrapPerfRoutingPerDlciTable,
       "mfrapPerfRoutingPerDlciEntry": mfrapPerfRoutingPerDlciEntry,
       "mfrapPerfRoutingPerDlciInterval": mfrapPerfRoutingPerDlciInterval,
       "mfrapPerfRoutingPerDlciValue": mfrapPerfRoutingPerDlciValue,
       "mfrapPerfRoutingPerDlciRxOspf": mfrapPerfRoutingPerDlciRxOspf,
       "mfrapPerfRoutingPerDlciTxOspf": mfrapPerfRoutingPerDlciTxOspf,
       "mfrapPerfRoutingPerDlciRxRip": mfrapPerfRoutingPerDlciRxRip,
       "mfrapPerfRoutingPerDlciTxRip": mfrapPerfRoutingPerDlciTxRip,
       "mfrapPerfRoutingPerDlciRxNetbios": mfrapPerfRoutingPerDlciRxNetbios,
       "mfrapPerfRoutingPerDlciTxNetbios": mfrapPerfRoutingPerDlciTxNetbios,
       "mfrapPerfRoutingTotalTable": mfrapPerfRoutingTotalTable,
       "mfrapPerfRoutingTotalEntry": mfrapPerfRoutingTotalEntry,
       "mfrapPerfRoutingTotalInterval": mfrapPerfRoutingTotalInterval,
       "mfrapPerfRoutingTotalRxOspf": mfrapPerfRoutingTotalRxOspf,
       "mfrapPerfRoutingTotalTxOspf": mfrapPerfRoutingTotalTxOspf,
       "mfrapPerfRoutingTotalRxRip": mfrapPerfRoutingTotalRxRip,
       "mfrapPerfRoutingTotalTxRip": mfrapPerfRoutingTotalTxRip,
       "mfrapPerfRoutingTotalRxNetbios": mfrapPerfRoutingTotalRxNetbios,
       "mfrapPerfRoutingTotalTxNetbios": mfrapPerfRoutingTotalTxNetbios,
       "mfrapPerfIpxPerDlciTable": mfrapPerfIpxPerDlciTable,
       "mfrapPerfIpxPerDlciEntry": mfrapPerfIpxPerDlciEntry,
       "mfrapPerfIpxPerDlciInterval": mfrapPerfIpxPerDlciInterval,
       "mfrapPerfIpxPerDlciValue": mfrapPerfIpxPerDlciValue,
       "mfrapPerfIpxPerDlciRxTotal": mfrapPerfIpxPerDlciRxTotal,
       "mfrapPerfIpxPerDlciTxTotal": mfrapPerfIpxPerDlciTxTotal,
       "mfrapPerfIpxPerDlciRxSpx": mfrapPerfIpxPerDlciRxSpx,
       "mfrapPerfIpxPerDlciTxSpx": mfrapPerfIpxPerDlciTxSpx,
       "mfrapPerfIpxPerDlciRxNcp": mfrapPerfIpxPerDlciRxNcp,
       "mfrapPerfIpxPerDlciTxNcp": mfrapPerfIpxPerDlciTxNcp,
       "mfrapPerfIpxPerDlciRxSap": mfrapPerfIpxPerDlciRxSap,
       "mfrapPerfIpxPerDlciTxSap": mfrapPerfIpxPerDlciTxSap,
       "mfrapPerfIpxPerDlciRxRip": mfrapPerfIpxPerDlciRxRip,
       "mfrapPerfIpxPerDlciTxRip": mfrapPerfIpxPerDlciTxRip,
       "mfrapPerfIpxPerDlciRxNetbios": mfrapPerfIpxPerDlciRxNetbios,
       "mfrapPerfIpxPerDlciTxNetbios": mfrapPerfIpxPerDlciTxNetbios,
       "mfrapPerfIpxPerDlciRxOther": mfrapPerfIpxPerDlciRxOther,
       "mfrapPerfIpxPerDlciTxOther": mfrapPerfIpxPerDlciTxOther,
       "mfrapPerfIpxTotalTable": mfrapPerfIpxTotalTable,
       "mfrapPerfIpxTotalEntry": mfrapPerfIpxTotalEntry,
       "mfrapPerfIpxTotalInterval": mfrapPerfIpxTotalInterval,
       "mfrapPerfIpxTotalRxTotal": mfrapPerfIpxTotalRxTotal,
       "mfrapPerfIpxTotalTxTotal": mfrapPerfIpxTotalTxTotal,
       "mfrapPerfIpxTotalRxSpx": mfrapPerfIpxTotalRxSpx,
       "mfrapPerfIpxTotalTxSpx": mfrapPerfIpxTotalTxSpx,
       "mfrapPerfIpxTotalRxNcp": mfrapPerfIpxTotalRxNcp,
       "mfrapPerfIpxTotalTxNcp": mfrapPerfIpxTotalTxNcp,
       "mfrapPerfIpxTotalRxSap": mfrapPerfIpxTotalRxSap,
       "mfrapPerfIpxTotalTxSap": mfrapPerfIpxTotalTxSap,
       "mfrapPerfIpxTotalRxRip": mfrapPerfIpxTotalRxRip,
       "mfrapPerfIpxTotalTxRip": mfrapPerfIpxTotalTxRip,
       "mfrapPerfIpxTotalRxNetbios": mfrapPerfIpxTotalRxNetbios,
       "mfrapPerfIpxTotalTxNetbios": mfrapPerfIpxTotalTxNetbios,
       "mfrapPerfIpxTotalRxOther": mfrapPerfIpxTotalRxOther,
       "mfrapPerfIpxTotalTxOther": mfrapPerfIpxTotalTxOther,
       "mfrapPerfSnaPerDlciTable": mfrapPerfSnaPerDlciTable,
       "mfrapPerfSnaPerDlciEntry": mfrapPerfSnaPerDlciEntry,
       "mfrapPerfSnaPerDlciInterval": mfrapPerfSnaPerDlciInterval,
       "mfrapPerfSnaPerDlciValue": mfrapPerfSnaPerDlciValue,
       "mfrapPerfSnaPerDlciRxTotal": mfrapPerfSnaPerDlciRxTotal,
       "mfrapPerfSnaPerDlciTxTotal": mfrapPerfSnaPerDlciTxTotal,
       "mfrapPerfSnaPerDlciRxSubarea": mfrapPerfSnaPerDlciRxSubarea,
       "mfrapPerfSnaPerDlciTxSubarea": mfrapPerfSnaPerDlciTxSubarea,
       "mfrapPerfSnaPerDlciRxPeriph": mfrapPerfSnaPerDlciRxPeriph,
       "mfrapPerfSnaPerDlciTxPeriph": mfrapPerfSnaPerDlciTxPeriph,
       "mfrapPerfSnaPerDlciRxAppn": mfrapPerfSnaPerDlciRxAppn,
       "mfrapPerfSnaPerDlciTxAppn": mfrapPerfSnaPerDlciTxAppn,
       "mfrapPerfSnaPerDlciRxNetbios": mfrapPerfSnaPerDlciRxNetbios,
       "mfrapPerfSnaPerDlciTxNetbios": mfrapPerfSnaPerDlciTxNetbios,
       "mfrapPerfSnaPerDlciRxOther": mfrapPerfSnaPerDlciRxOther,
       "mfrapPerfSnaPerDlciTxOther": mfrapPerfSnaPerDlciTxOther,
       "mfrapPerfSnaTotalTable": mfrapPerfSnaTotalTable,
       "mfrapPerfSnaTotalEntry": mfrapPerfSnaTotalEntry,
       "mfrapPerfSnaTotalInterval": mfrapPerfSnaTotalInterval,
       "mfrapPerfSnaTotalRxTotal": mfrapPerfSnaTotalRxTotal,
       "mfrapPerfSnaTotalTxTotal": mfrapPerfSnaTotalTxTotal,
       "mfrapPerfSnaTotalRxSubarea": mfrapPerfSnaTotalRxSubarea,
       "mfrapPerfSnaTotalTxSubarea": mfrapPerfSnaTotalTxSubarea,
       "mfrapPerfSnaTotalRxPeriph": mfrapPerfSnaTotalRxPeriph,
       "mfrapPerfSnaTotalTxPeriph": mfrapPerfSnaTotalTxPeriph,
       "mfrapPerfSnaTotalRxAppn": mfrapPerfSnaTotalRxAppn,
       "mfrapPerfSnaTotalTxAppn": mfrapPerfSnaTotalTxAppn,
       "mfrapPerfSnaTotalRxNetbios": mfrapPerfSnaTotalRxNetbios,
       "mfrapPerfSnaTotalTxNetbios": mfrapPerfSnaTotalTxNetbios,
       "mfrapPerfSnaTotalRxOther": mfrapPerfSnaTotalRxOther,
       "mfrapPerfSnaTotalTxOther": mfrapPerfSnaTotalTxOther,
       "mfrapPerfArpPerDlciTable": mfrapPerfArpPerDlciTable,
       "mfrapPerfArpPerDlciEntry": mfrapPerfArpPerDlciEntry,
       "mfrapPerfArpPerDlciInterval": mfrapPerfArpPerDlciInterval,
       "mfrapPerfArpPerDlciValue": mfrapPerfArpPerDlciValue,
       "mfrapPerfArpPerDlciRxTotal": mfrapPerfArpPerDlciRxTotal,
       "mfrapPerfArpPerDlciTxTotal": mfrapPerfArpPerDlciTxTotal,
       "mfrapPerfArpPerDlciRxArpReq": mfrapPerfArpPerDlciRxArpReq,
       "mfrapPerfArpPerDlciTxArpReq": mfrapPerfArpPerDlciTxArpReq,
       "mfrapPerfArpPerDlciRxArpRep": mfrapPerfArpPerDlciRxArpRep,
       "mfrapPerfArpPerDlciTxArpRep": mfrapPerfArpPerDlciTxArpRep,
       "mfrapPerfArpPerDlciRxRarpReq": mfrapPerfArpPerDlciRxRarpReq,
       "mfrapPerfArpPerDlciTxRarpReq": mfrapPerfArpPerDlciTxRarpReq,
       "mfrapPerfArpPerDlciRxRarpRep": mfrapPerfArpPerDlciRxRarpRep,
       "mfrapPerfArpPerDlciTxRarpRep": mfrapPerfArpPerDlciTxRarpRep,
       "mfrapPerfArpPerDlciRxInarpReq": mfrapPerfArpPerDlciRxInarpReq,
       "mfrapPerfArpPerDlciTxInarpReq": mfrapPerfArpPerDlciTxInarpReq,
       "mfrapPerfArpPerDlciRxInarpRep": mfrapPerfArpPerDlciRxInarpRep,
       "mfrapPerfArpPerDlciTxInarpRep": mfrapPerfArpPerDlciTxInarpRep,
       "mfrapPerfArpPerDlciRxOther": mfrapPerfArpPerDlciRxOther,
       "mfrapPerfArpPerDlciTxOther": mfrapPerfArpPerDlciTxOther,
       "mfrapPerfArpTotalTable": mfrapPerfArpTotalTable,
       "mfrapPerfArpTotalEntry": mfrapPerfArpTotalEntry,
       "mfrapPerfArpTotalInterval": mfrapPerfArpTotalInterval,
       "mfrapPerfArpTotalRxTotal": mfrapPerfArpTotalRxTotal,
       "mfrapPerfArpTotalTxTotal": mfrapPerfArpTotalTxTotal,
       "mfrapPerfArpTotalRxArpReq": mfrapPerfArpTotalRxArpReq,
       "mfrapPerfArpTotalTxArpReq": mfrapPerfArpTotalTxArpReq,
       "mfrapPerfArpTotalRxArpRep": mfrapPerfArpTotalRxArpRep,
       "mfrapPerfArpTotalTxArpRep": mfrapPerfArpTotalTxArpRep,
       "mfrapPerfArpTotalRxRarpReq": mfrapPerfArpTotalRxRarpReq,
       "mfrapPerfArpTotalTxRarpReq": mfrapPerfArpTotalTxRarpReq,
       "mfrapPerfArpTotalRxRarpRep": mfrapPerfArpTotalRxRarpRep,
       "mfrapPerfArpTotalTxRarpRep": mfrapPerfArpTotalTxRarpRep,
       "mfrapPerfArpTotalRxInarpReq": mfrapPerfArpTotalRxInarpReq,
       "mfrapPerfArpTotalTxInarpReq": mfrapPerfArpTotalTxInarpReq,
       "mfrapPerfArpTotalRxInarpRep": mfrapPerfArpTotalRxInarpRep,
       "mfrapPerfArpTotalTxInarpRep": mfrapPerfArpTotalTxInarpRep,
       "mfrapPerfArpTotalRxOther": mfrapPerfArpTotalRxOther,
       "mfrapPerfArpTotalTxOther": mfrapPerfArpTotalTxOther,
       "mfrapPerfLmiPerDlciTable": mfrapPerfLmiPerDlciTable,
       "mfrapPerfLmiPerDlciEntry": mfrapPerfLmiPerDlciEntry,
       "mfrapPerfLmiPerDlciInterval": mfrapPerfLmiPerDlciInterval,
       "mfrapPerfLmiPerDlciValue": mfrapPerfLmiPerDlciValue,
       "mfrapPerfLmiPerDlciRxTotalByteCnt": mfrapPerfLmiPerDlciRxTotalByteCnt,
       "mfrapPerfLmiPerDlciTxTotalByteCnt": mfrapPerfLmiPerDlciTxTotalByteCnt,
       "mfrapPerfLmiPerDlciRxLivoEnqByteCnt": mfrapPerfLmiPerDlciRxLivoEnqByteCnt,
       "mfrapPerfLmiPerDlciTxLivoEnqByteCnt": mfrapPerfLmiPerDlciTxLivoEnqByteCnt,
       "mfrapPerfLmiPerDlciRxLivoStatByteCnt": mfrapPerfLmiPerDlciRxLivoStatByteCnt,
       "mfrapPerfLmiPerDlciTxLivoStatByteCnt": mfrapPerfLmiPerDlciTxLivoStatByteCnt,
       "mfrapPerfLmiPerDlciRxFullEnqByteCnt": mfrapPerfLmiPerDlciRxFullEnqByteCnt,
       "mfrapPerfLmiPerDlciTxFullEnqByteCnt": mfrapPerfLmiPerDlciTxFullEnqByteCnt,
       "mfrapPerfLmiPerDlciRxFullStatByteCnt": mfrapPerfLmiPerDlciRxFullStatByteCnt,
       "mfrapPerfLmiPerDlciTxFullStatByteCnt": mfrapPerfLmiPerDlciTxFullStatByteCnt,
       "mfrapPerfLmiPerDlciRxOtherByteCnt": mfrapPerfLmiPerDlciRxOtherByteCnt,
       "mfrapPerfLmiPerDlciTxOtherByteCnt": mfrapPerfLmiPerDlciTxOtherByteCnt,
       "mfrapPerfLmiTotalTable": mfrapPerfLmiTotalTable,
       "mfrapPerfLmiTotalEntry": mfrapPerfLmiTotalEntry,
       "mfrapPerfLmiTotalInterval": mfrapPerfLmiTotalInterval,
       "mfrapPerfLmiTotalDlciValue": mfrapPerfLmiTotalDlciValue,
       "mfrapPerfLmiTotalRxTotalByteCnt": mfrapPerfLmiTotalRxTotalByteCnt,
       "mfrapPerfLmiTotalTxTotalByteCnt": mfrapPerfLmiTotalTxTotalByteCnt,
       "mfrapPerfLmiTotalRxLivoEnqByteCnt": mfrapPerfLmiTotalRxLivoEnqByteCnt,
       "mfrapPerfLmiTotalTxLivoEnqByteCnt": mfrapPerfLmiTotalTxLivoEnqByteCnt,
       "mfrapPerfLmiTotalRxLivoStatByteCnt": mfrapPerfLmiTotalRxLivoStatByteCnt,
       "mfrapPerfLmiTotalTxLivoStatByteCnt": mfrapPerfLmiTotalTxLivoStatByteCnt,
       "mfrapPerfLmiTotalRxFullEnqByteCnt": mfrapPerfLmiTotalRxFullEnqByteCnt,
       "mfrapPerfLmiTotalTxFullEnqByteCnt": mfrapPerfLmiTotalTxFullEnqByteCnt,
       "mfrapPerfLmiTotalRxFullStatByteCnt": mfrapPerfLmiTotalRxFullStatByteCnt,
       "mfrapPerfLmiTotalTxFullStatByteCnt": mfrapPerfLmiTotalTxFullStatByteCnt,
       "mfrapPerfLmiTotalRxOtherByteCnt": mfrapPerfLmiTotalRxOtherByteCnt,
       "mfrapPerfLmiTotalTxOtherByteCnt": mfrapPerfLmiTotalTxOtherByteCnt,
       "mfrapPerfNetworkLongTerm": mfrapPerfNetworkLongTerm,
       "mfrapPerfNetwLongTermTable": mfrapPerfNetwLongTermTable,
       "mfrapPerfNetwLongTermEntry": mfrapPerfNetwLongTermEntry,
       "mfrapPerfNetwLongTermDlci": mfrapPerfNetwLongTermDlci,
       "mfrapPerfNetwLongTermProtocol": mfrapPerfNetwLongTermProtocol,
       "mfrapPerfNetwLongTermInterval": mfrapPerfNetwLongTermInterval,
       "mfrapPerfNetwLongTermValue": mfrapPerfNetwLongTermValue,
       "mfrapPerfNetwLongTermAltTable": mfrapPerfNetwLongTermAltTable,
       "mfrapPerfNetwLongTermAltEntry": mfrapPerfNetwLongTermAltEntry,
       "mfrapPerfNetwLongTermAltDlci": mfrapPerfNetwLongTermAltDlci,
       "mfrapPerfNetwLongTermAltProtocol": mfrapPerfNetwLongTermAltProtocol,
       "mfrapPerfNetwLongTermAltArray": mfrapPerfNetwLongTermAltArray,
       "mfrapPerfNetworkLongTermCommands": mfrapPerfNetworkLongTermCommands,
       "mfrapPerfNetworkLongTermCmdClear": mfrapPerfNetworkLongTermCmdClear,
       "mfrapPerfCirPercentUtilization": mfrapPerfCirPercentUtilization,
       "mfrapPerfCirPercentUtilizationTable": mfrapPerfCirPercentUtilizationTable,
       "mfrapPerfCirPercentUtilizationEntry": mfrapPerfCirPercentUtilizationEntry,
       "mfrapPerfCirPercentUtilizationInterval": mfrapPerfCirPercentUtilizationInterval,
       "mfrapPerfCirPercentUtilizationDlciValue": mfrapPerfCirPercentUtilizationDlciValue,
       "mfrapPerfCirRxPercentUtilizationRange1": mfrapPerfCirRxPercentUtilizationRange1,
       "mfrapPerfCirRxPercentUtilizationRange2": mfrapPerfCirRxPercentUtilizationRange2,
       "mfrapPerfCirRxPercentUtilizationRange3": mfrapPerfCirRxPercentUtilizationRange3,
       "mfrapPerfCirRxPercentUtilizationRange4": mfrapPerfCirRxPercentUtilizationRange4,
       "mfrapPerfCirRxPercentUtilizationRange5": mfrapPerfCirRxPercentUtilizationRange5,
       "mfrapPerfCirRxPercentUtilizationRange6": mfrapPerfCirRxPercentUtilizationRange6,
       "mfrapPerfCirRxPercentUtilizationRange7": mfrapPerfCirRxPercentUtilizationRange7,
       "mfrapPerfCirRxPercentUtilizationRange8": mfrapPerfCirRxPercentUtilizationRange8,
       "mfrapPerfCirTxPercentUtilizationRange1": mfrapPerfCirTxPercentUtilizationRange1,
       "mfrapPerfCirTxPercentUtilizationRange2": mfrapPerfCirTxPercentUtilizationRange2,
       "mfrapPerfCirTxPercentUtilizationRange3": mfrapPerfCirTxPercentUtilizationRange3,
       "mfrapPerfCirTxPercentUtilizationRange4": mfrapPerfCirTxPercentUtilizationRange4,
       "mfrapPerfCirTxPercentUtilizationRange5": mfrapPerfCirTxPercentUtilizationRange5,
       "mfrapPerfCirTxPercentUtilizationRange6": mfrapPerfCirTxPercentUtilizationRange6,
       "mfrapPerfCirTxPercentUtilizationRange7": mfrapPerfCirTxPercentUtilizationRange7,
       "mfrapPerfCirTxPercentUtilizationRange8": mfrapPerfCirTxPercentUtilizationRange8,
       "mfrapPerfCurrentPerDlciUtilizationTable": mfrapPerfCurrentPerDlciUtilizationTable,
       "mfrapPerfCurrentPerDlciUtilizationEntry": mfrapPerfCurrentPerDlciUtilizationEntry,
       "mfrapPerfCurrentPerDlciUtilizationDlciValue": mfrapPerfCurrentPerDlciUtilizationDlciValue,
       "mfrapPerfCurrentPerDlciRxUtilization": mfrapPerfCurrentPerDlciRxUtilization,
       "mfrapPerfCurrentPerDlciTxUtilization": mfrapPerfCurrentPerDlciTxUtilization,
       "mfrapPerfCurrentPerDlciAggregateUtilization": mfrapPerfCurrentPerDlciAggregateUtilization,
       "mfrapPerfCurrentUnitUtilization": mfrapPerfCurrentUnitUtilization,
       "mfrapPerfCurrentDteUtilization": mfrapPerfCurrentDteUtilization,
       "mfrapPerfCurrentWanUtilization": mfrapPerfCurrentWanUtilization,
       "mfrapPerfCurrentAggregateUtilization": mfrapPerfCurrentAggregateUtilization,
       "mfrapAlarmType": mfrapAlarmType,
       "mfrapDLCINum": mfrapDLCINum,
       "mfrapInterface": mfrapInterface,
       "mfrapIpAddress": mfrapIpAddress,
       "mfrapEventTrapLog": mfrapEventTrapLog,
       "mfrapEventTrapLogTable": mfrapEventTrapLogTable,
       "mfrapEventTrapLogEntry": mfrapEventTrapLogEntry,
       "mfrapEventTrapLogSeqNum": mfrapEventTrapLogSeqNum,
       "mfrapEventTrapLogGenericEvent": mfrapEventTrapLogGenericEvent,
       "mfrapEventTrapLogSpecificEvent": mfrapEventTrapLogSpecificEvent,
       "mfrapEventTrapLogTimeStamp": mfrapEventTrapLogTimeStamp,
       "mfrapEventTrapLogVarBind1": mfrapEventTrapLogVarBind1,
       "mfrapEventTrapLogVarBind2": mfrapEventTrapLogVarBind2,
       "mfrapEventTrapLogVarBind3": mfrapEventTrapLogVarBind3,
       "mfrapEventLogAltTable": mfrapEventLogAltTable,
       "mfrapEventLogAltEntry": mfrapEventLogAltEntry,
       "mfrapEventLogAltSeqNum": mfrapEventLogAltSeqNum,
       "mfrapEventLogAltArray": mfrapEventLogAltArray,
       "mfrapEventLogCurrentSeqNum": mfrapEventLogCurrentSeqNum,
       "mfrapEventLogFreeze": mfrapEventLogFreeze,
       "mfrapEventLogClear": mfrapEventLogClear,
       "mfrapPercentUtilization": mfrapPercentUtilization,
       "mfrapUtilizationThreshold": mfrapUtilizationThreshold,
       "mfrapCfgLockIpAddress": mfrapCfgLockIpAddress}
)
