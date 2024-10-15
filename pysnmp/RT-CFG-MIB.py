# SNMP MIB module (RT-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RT-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:32 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class ActionListName(DisplayString):
    """Custom type ActionListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )





class DirectionType(Integer32):
    """Custom type DirectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("other", 1))
    )





class AccountCouter(Counter32):
    """Custom type AccountCouter based on Counter32"""




class AccountCounter64(Counter64):
    """Custom type AccountCounter64 based on Counter64"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbRouterConfig_ObjectIdentity = ObjectIdentity
nbRouterConfig = _NbRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12)
)
_NbRtConfigGen_ObjectIdentity = ObjectIdentity
nbRtConfigGen = _NbRtConfigGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 1)
)


class _NbRtDevDiffServMode_Type(Integer32):
    """Custom type nbRtDevDiffServMode based on Integer32"""
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
        *(("byTOS", 3),
          ("byTag", 4),
          ("none", 2),
          ("other", 1))
    )


_NbRtDevDiffServMode_Type.__name__ = "Integer32"
_NbRtDevDiffServMode_Object = MibScalar
nbRtDevDiffServMode = _NbRtDevDiffServMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 1, 1),
    _NbRtDevDiffServMode_Type()
)
nbRtDevDiffServMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDevDiffServMode.setStatus("mandatory")


class _NbRtDevDiffServMappingSupport_Type(Integer32):
    """Custom type nbRtDevDiffServMappingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbRtDevDiffServMappingSupport_Type.__name__ = "Integer32"
_NbRtDevDiffServMappingSupport_Object = MibScalar
nbRtDevDiffServMappingSupport = _NbRtDevDiffServMappingSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 1, 2),
    _NbRtDevDiffServMappingSupport_Type()
)
nbRtDevDiffServMappingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDevDiffServMappingSupport.setStatus("mandatory")
_NbRtVifTable_Object = MibTable
nbRtVifTable = _NbRtVifTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2)
)
if mibBuilder.loadTexts:
    nbRtVifTable.setStatus("mandatory")
_NbRtVifEntry_Object = MibTableRow
nbRtVifEntry = _NbRtVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1)
)
nbRtVifEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtVifId"),
)
if mibBuilder.loadTexts:
    nbRtVifEntry.setStatus("mandatory")
_NbRtVifId_Type = DisplayString
_NbRtVifId_Object = MibTableColumn
nbRtVifId = _NbRtVifId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 1),
    _NbRtVifId_Type()
)
nbRtVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtVifId.setStatus("mandatory")
_NbRtVifIpAddress_Type = IpAddress
_NbRtVifIpAddress_Object = MibTableColumn
nbRtVifIpAddress = _NbRtVifIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 2),
    _NbRtVifIpAddress_Type()
)
nbRtVifIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifIpAddress.setStatus("mandatory")
_NbRtVifMask_Type = IpAddress
_NbRtVifMask_Object = MibTableColumn
nbRtVifMask = _NbRtVifMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 3),
    _NbRtVifMask_Type()
)
nbRtVifMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifMask.setStatus("mandatory")


class _NbRtVifProtocol_Type(Integer32):
    """Custom type nbRtVifProtocol based on Integer32"""
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
        *(("ipV4IF", 2),
          ("ipxIF", 3),
          ("other", 1),
          ("portsIF", 4))
    )


_NbRtVifProtocol_Type.__name__ = "Integer32"
_NbRtVifProtocol_Object = MibTableColumn
nbRtVifProtocol = _NbRtVifProtocol_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 4),
    _NbRtVifProtocol_Type()
)
nbRtVifProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifProtocol.setStatus("mandatory")
_NbRtVifName_Type = DisplayString
_NbRtVifName_Object = MibTableColumn
nbRtVifName = _NbRtVifName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 5),
    _NbRtVifName_Type()
)
nbRtVifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifName.setStatus("mandatory")
_NbRtVifPortList_Type = OctetString
_NbRtVifPortList_Object = MibTableColumn
nbRtVifPortList = _NbRtVifPortList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 6),
    _NbRtVifPortList_Type()
)
nbRtVifPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifPortList.setStatus("mandatory")
_NbRtVifMac_Type = MacAddress
_NbRtVifMac_Object = MibTableColumn
nbRtVifMac = _NbRtVifMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 7),
    _NbRtVifMac_Type()
)
nbRtVifMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifMac.setStatus("mandatory")


class _NbRtVifAdminStatus_Type(Integer32):
    """Custom type nbRtVifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("create", 4),
          ("invalid", 2),
          ("valid", 1))
    )


_NbRtVifAdminStatus_Type.__name__ = "Integer32"
_NbRtVifAdminStatus_Object = MibTableColumn
nbRtVifAdminStatus = _NbRtVifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 8),
    _NbRtVifAdminStatus_Type()
)
nbRtVifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifAdminStatus.setStatus("mandatory")


class _NbRtVifConfigType_Type(Integer32):
    """Custom type nbRtVifConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_NbRtVifConfigType_Type.__name__ = "Integer32"
_NbRtVifConfigType_Object = MibTableColumn
nbRtVifConfigType = _NbRtVifConfigType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 9),
    _NbRtVifConfigType_Type()
)
nbRtVifConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifConfigType.setStatus("mandatory")


class _NbRtVifSecurity_Type(Integer32):
    """Custom type nbRtVifSecurity based on Integer32"""
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
          ("secure", 3),
          ("unsecure", 2))
    )


_NbRtVifSecurity_Type.__name__ = "Integer32"
_NbRtVifSecurity_Object = MibTableColumn
nbRtVifSecurity = _NbRtVifSecurity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 10),
    _NbRtVifSecurity_Type()
)
nbRtVifSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifSecurity.setStatus("mandatory")


class _NbRtVifIsTagged_Type(Integer32):
    """Custom type nbRtVifIsTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NbRtVifIsTagged_Type.__name__ = "Integer32"
_NbRtVifIsTagged_Object = MibTableColumn
nbRtVifIsTagged = _NbRtVifIsTagged_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 15),
    _NbRtVifIsTagged_Type()
)
nbRtVifIsTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifIsTagged.setStatus("mandatory")


class _NbRtVifTag_Type(Integer32):
    """Custom type nbRtVifTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbRtVifTag_Type.__name__ = "Integer32"
_NbRtVifTag_Object = MibTableColumn
nbRtVifTag = _NbRtVifTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 2, 1, 16),
    _NbRtVifTag_Type()
)
nbRtVifTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifTag.setStatus("mandatory")
_NbRtVifGroup_ObjectIdentity = ObjectIdentity
nbRtVifGroup = _NbRtVifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3)
)
_NbVifTableSize_Type = Integer32
_NbVifTableSize_Object = MibScalar
nbVifTableSize = _NbVifTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 1),
    _NbVifTableSize_Type()
)
nbVifTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifTableSize.setStatus("mandatory")
_NbVifDeviceLimitTable_Object = MibTable
nbVifDeviceLimitTable = _NbVifDeviceLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2)
)
if mibBuilder.loadTexts:
    nbVifDeviceLimitTable.setStatus("mandatory")
_NbVifDeviceLimitEntry_Object = MibTableRow
nbVifDeviceLimitEntry = _NbVifDeviceLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2, 1)
)
nbVifDeviceLimitEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifLimitType"),
)
if mibBuilder.loadTexts:
    nbVifDeviceLimitEntry.setStatus("mandatory")


class _NbVifLimitType_Type(Integer32):
    """Custom type nbVifLimitType based on Integer32"""
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
        *(("lanEthernet", 2),
          ("other", 1),
          ("wanFrameRelay", 4),
          ("wanPPP", 3))
    )


_NbVifLimitType_Type.__name__ = "Integer32"
_NbVifLimitType_Object = MibTableColumn
nbVifLimitType = _NbVifLimitType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2, 1, 1),
    _NbVifLimitType_Type()
)
nbVifLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifLimitType.setStatus("mandatory")
_NbVifDevNoMin_Type = Integer32
_NbVifDevNoMin_Object = MibTableColumn
nbVifDevNoMin = _NbVifDevNoMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2, 1, 2),
    _NbVifDevNoMin_Type()
)
nbVifDevNoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifDevNoMin.setStatus("mandatory")
_NbVifDevNoMax_Type = Integer32
_NbVifDevNoMax_Object = MibTableColumn
nbVifDevNoMax = _NbVifDevNoMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2, 1, 3),
    _NbVifDevNoMax_Type()
)
nbVifDevNoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifDevNoMax.setStatus("mandatory")
_NbVifDevNoFirstEmpty_Type = Integer32
_NbVifDevNoFirstEmpty_Object = MibTableColumn
nbVifDevNoFirstEmpty = _NbVifDevNoFirstEmpty_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 2, 1, 4),
    _NbVifDevNoFirstEmpty_Type()
)
nbVifDevNoFirstEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifDevNoFirstEmpty.setStatus("mandatory")
_NbVifAliasDLimitTable_Object = MibTable
nbVifAliasDLimitTable = _NbVifAliasDLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3)
)
if mibBuilder.loadTexts:
    nbVifAliasDLimitTable.setStatus("mandatory")
_NbVifAliasDLimitEntry_Object = MibTableRow
nbVifAliasDLimitEntry = _NbVifAliasDLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1)
)
nbVifAliasDLimitEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifAliasLimitType"),
    (0, "RT-CFG-MIB", "nbVifAliasLimitDevNo"),
)
if mibBuilder.loadTexts:
    nbVifAliasDLimitEntry.setStatus("mandatory")


class _NbVifAliasLimitType_Type(Integer32):
    """Custom type nbVifAliasLimitType based on Integer32"""
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
        *(("lanEthernet", 2),
          ("other", 1),
          ("wanFrameRelay", 4),
          ("wanPPP", 3))
    )


_NbVifAliasLimitType_Type.__name__ = "Integer32"
_NbVifAliasLimitType_Object = MibTableColumn
nbVifAliasLimitType = _NbVifAliasLimitType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1, 1),
    _NbVifAliasLimitType_Type()
)
nbVifAliasLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasLimitType.setStatus("mandatory")
_NbVifAliasLimitDevNo_Type = Integer32
_NbVifAliasLimitDevNo_Object = MibTableColumn
nbVifAliasLimitDevNo = _NbVifAliasLimitDevNo_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1, 2),
    _NbVifAliasLimitDevNo_Type()
)
nbVifAliasLimitDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasLimitDevNo.setStatus("mandatory")
_NbVifAliasLimitDevAliasMin_Type = Integer32
_NbVifAliasLimitDevAliasMin_Object = MibTableColumn
nbVifAliasLimitDevAliasMin = _NbVifAliasLimitDevAliasMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1, 3),
    _NbVifAliasLimitDevAliasMin_Type()
)
nbVifAliasLimitDevAliasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasLimitDevAliasMin.setStatus("mandatory")
_NbVifAliasLimitDevAliasMax_Type = Integer32
_NbVifAliasLimitDevAliasMax_Object = MibTableColumn
nbVifAliasLimitDevAliasMax = _NbVifAliasLimitDevAliasMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1, 4),
    _NbVifAliasLimitDevAliasMax_Type()
)
nbVifAliasLimitDevAliasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasLimitDevAliasMax.setStatus("mandatory")
_NbVifAliasLimitDevAliasFirstEmpty_Type = Integer32
_NbVifAliasLimitDevAliasFirstEmpty_Object = MibTableColumn
nbVifAliasLimitDevAliasFirstEmpty = _NbVifAliasLimitDevAliasFirstEmpty_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 3, 1, 5),
    _NbVifAliasLimitDevAliasFirstEmpty_Type()
)
nbVifAliasLimitDevAliasFirstEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasLimitDevAliasFirstEmpty.setStatus("mandatory")
_NbVifTable_Object = MibTable
nbVifTable = _NbVifTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11)
)
if mibBuilder.loadTexts:
    nbVifTable.setStatus("mandatory")
_NbVifEntry_Object = MibTableRow
nbVifEntry = _NbVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1)
)
nbVifEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
)
if mibBuilder.loadTexts:
    nbVifEntry.setStatus("mandatory")


class _NbVifType_Type(Integer32):
    """Custom type nbVifType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 5),
          ("dummy", 7),
          ("lanEthernet", 2),
          ("logical", 8),
          ("loopback", 6),
          ("other", 1),
          ("outOfBand", 12),
          ("wanFrameRelay", 4),
          ("wanPPP", 3))
    )


_NbVifType_Type.__name__ = "Integer32"
_NbVifType_Object = MibTableColumn
nbVifType = _NbVifType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 1),
    _NbVifType_Type()
)
nbVifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifType.setStatus("mandatory")
_NbVifDevNo_Type = Integer32
_NbVifDevNo_Object = MibTableColumn
nbVifDevNo = _NbVifDevNo_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 2),
    _NbVifDevNo_Type()
)
nbVifDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifDevNo.setStatus("mandatory")


class _NbVifIsAlias_Type(Integer32):
    """Custom type nbVifIsAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alias", 3),
          ("other", 1),
          ("primary", 2))
    )


_NbVifIsAlias_Type.__name__ = "Integer32"
_NbVifIsAlias_Object = MibTableColumn
nbVifIsAlias = _NbVifIsAlias_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 3),
    _NbVifIsAlias_Type()
)
nbVifIsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifIsAlias.setStatus("mandatory")
_NbVifAliasDev_Type = Integer32
_NbVifAliasDev_Object = MibTableColumn
nbVifAliasDev = _NbVifAliasDev_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 4),
    _NbVifAliasDev_Type()
)
nbVifAliasDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifAliasDev.setStatus("mandatory")
_NbVifDevName_Type = DisplayString
_NbVifDevName_Object = MibTableColumn
nbVifDevName = _NbVifDevName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 5),
    _NbVifDevName_Type()
)
nbVifDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifDevName.setStatus("mandatory")
_NbVifIpAddress_Type = IpAddress
_NbVifIpAddress_Object = MibTableColumn
nbVifIpAddress = _NbVifIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 6),
    _NbVifIpAddress_Type()
)
nbVifIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifIpAddress.setStatus("mandatory")
_NbVifMask_Type = IpAddress
_NbVifMask_Object = MibTableColumn
nbVifMask = _NbVifMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 7),
    _NbVifMask_Type()
)
nbVifMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifMask.setStatus("mandatory")
_NbVifPeer_Type = IpAddress
_NbVifPeer_Object = MibTableColumn
nbVifPeer = _NbVifPeer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 8),
    _NbVifPeer_Type()
)
nbVifPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifPeer.setStatus("mandatory")


class _NbVifPhysType_Type(Integer32):
    """Custom type nbVifPhysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eth0", 2),
          ("other", 1),
          ("wp1", 3))
    )


_NbVifPhysType_Type.__name__ = "Integer32"
_NbVifPhysType_Object = MibTableColumn
nbVifPhysType = _NbVifPhysType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 9),
    _NbVifPhysType_Type()
)
nbVifPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifPhysType.setStatus("mandatory")


class _NbVifProtocol_Type(Integer32):
    """Custom type nbVifProtocol based on Integer32"""
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
        *(("ipV4IF", 2),
          ("ipxIF", 3),
          ("other", 1),
          ("portsIF", 4))
    )


_NbVifProtocol_Type.__name__ = "Integer32"
_NbVifProtocol_Object = MibTableColumn
nbVifProtocol = _NbVifProtocol_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 10),
    _NbVifProtocol_Type()
)
nbVifProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifProtocol.setStatus("mandatory")
_NbVifName_Type = DisplayString
_NbVifName_Object = MibTableColumn
nbVifName = _NbVifName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 11),
    _NbVifName_Type()
)
nbVifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifName.setStatus("mandatory")
_NbVifPortList_Type = OctetString
_NbVifPortList_Object = MibTableColumn
nbVifPortList = _NbVifPortList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 12),
    _NbVifPortList_Type()
)
nbVifPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifPortList.setStatus("mandatory")
_NbVifMac_Type = MacAddress
_NbVifMac_Object = MibTableColumn
nbVifMac = _NbVifMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 13),
    _NbVifMac_Type()
)
nbVifMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifMac.setStatus("mandatory")


class _NbVifState_Type(Integer32):
    """Custom type nbVifState based on Integer32"""
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
        *(("adminDown", 4),
          ("down", 3),
          ("other", 1),
          ("up", 2))
    )


_NbVifState_Type.__name__ = "Integer32"
_NbVifState_Object = MibTableColumn
nbVifState = _NbVifState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 14),
    _NbVifState_Type()
)
nbVifState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifState.setStatus("mandatory")


class _NbVifAdminStatus_Type(Integer32):
    """Custom type nbVifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("create", 4),
          ("invalid", 2),
          ("valid", 1))
    )


_NbVifAdminStatus_Type.__name__ = "Integer32"
_NbVifAdminStatus_Object = MibTableColumn
nbVifAdminStatus = _NbVifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 15),
    _NbVifAdminStatus_Type()
)
nbVifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifAdminStatus.setStatus("mandatory")


class _NbVifConfigType_Type(Integer32):
    """Custom type nbVifConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_NbVifConfigType_Type.__name__ = "Integer32"
_NbVifConfigType_Object = MibTableColumn
nbVifConfigType = _NbVifConfigType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 16),
    _NbVifConfigType_Type()
)
nbVifConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifConfigType.setStatus("mandatory")


class _NbVifSecurity_Type(Integer32):
    """Custom type nbVifSecurity based on Integer32"""
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
          ("secure", 3),
          ("unsecure", 2))
    )


_NbVifSecurity_Type.__name__ = "Integer32"
_NbVifSecurity_Object = MibTableColumn
nbVifSecurity = _NbVifSecurity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 17),
    _NbVifSecurity_Type()
)
nbVifSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifSecurity.setStatus("mandatory")


class _NbVifIsTagged_Type(Integer32):
    """Custom type nbVifIsTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NbVifIsTagged_Type.__name__ = "Integer32"
_NbVifIsTagged_Object = MibTableColumn
nbVifIsTagged = _NbVifIsTagged_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 20),
    _NbVifIsTagged_Type()
)
nbVifIsTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifIsTagged.setStatus("mandatory")


class _NbVifTag_Type(Integer32):
    """Custom type nbVifTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbVifTag_Type.__name__ = "Integer32"
_NbVifTag_Object = MibTableColumn
nbVifTag = _NbVifTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 21),
    _NbVifTag_Type()
)
nbVifTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifTag.setStatus("mandatory")


class _NbVifDescr_Type(DisplayString):
    """Custom type nbVifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NbVifDescr_Type.__name__ = "DisplayString"
_NbVifDescr_Object = MibTableColumn
nbVifDescr = _NbVifDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 22),
    _NbVifDescr_Type()
)
nbVifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifDescr.setStatus("mandatory")
_NbVifLastChange_Type = TimeTicks
_NbVifLastChange_Object = MibTableColumn
nbVifLastChange = _NbVifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 23),
    _NbVifLastChange_Type()
)
nbVifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVifLastChange.setStatus("mandatory")


class _NbVifL2SwitchingMode_Type(Integer32):
    """Custom type nbVifL2SwitchingMode based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("interfaceTagFlood", 3),
          ("unicastToLinux", 4))
    )


_NbVifL2SwitchingMode_Type.__name__ = "Integer32"
_NbVifL2SwitchingMode_Object = MibTableColumn
nbVifL2SwitchingMode = _NbVifL2SwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 24),
    _NbVifL2SwitchingMode_Type()
)
nbVifL2SwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifL2SwitchingMode.setStatus("mandatory")


class _NbVifProxyArpMode_Type(Integer32):
    """Custom type nbVifProxyArpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("enableAll", 3))
    )


_NbVifProxyArpMode_Type.__name__ = "Integer32"
_NbVifProxyArpMode_Object = MibTableColumn
nbVifProxyArpMode = _NbVifProxyArpMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 25),
    _NbVifProxyArpMode_Type()
)
nbVifProxyArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifProxyArpMode.setStatus("mandatory")


class _NbVifIpOnlyMode_Type(Integer32):
    """Custom type nbVifIpOnlyMode based on Integer32"""
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


_NbVifIpOnlyMode_Type.__name__ = "Integer32"
_NbVifIpOnlyMode_Object = MibTableColumn
nbVifIpOnlyMode = _NbVifIpOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 26),
    _NbVifIpOnlyMode_Type()
)
nbVifIpOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifIpOnlyMode.setStatus("mandatory")


class _NbVifIpForwardingMode_Type(Integer32):
    """Custom type nbVifIpForwardingMode based on Integer32"""
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


_NbVifIpForwardingMode_Type.__name__ = "Integer32"
_NbVifIpForwardingMode_Object = MibTableColumn
nbVifIpForwardingMode = _NbVifIpForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 3, 11, 1, 27),
    _NbVifIpForwardingMode_Type()
)
nbVifIpForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVifIpForwardingMode.setStatus("mandatory")
_NbRtFib_ObjectIdentity = ObjectIdentity
nbRtFib = _NbRtFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4)
)
_NbRtFibNumEntries_Type = Integer32
_NbRtFibNumEntries_Object = MibScalar
nbRtFibNumEntries = _NbRtFibNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 1),
    _NbRtFibNumEntries_Type()
)
nbRtFibNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtFibNumEntries.setStatus("mandatory")
_NbRtFibTable_Object = MibTable
nbRtFibTable = _NbRtFibTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2)
)
if mibBuilder.loadTexts:
    nbRtFibTable.setStatus("mandatory")
_NbRtFibEntry_Object = MibTableRow
nbRtFibEntry = _NbRtFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1)
)
nbRtFibEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtFibEntryIpAddress"),
    (0, "RT-CFG-MIB", "nbRtFibEntryIpMask"),
    (0, "RT-CFG-MIB", "nbRtFibEntryProtocol"),
)
if mibBuilder.loadTexts:
    nbRtFibEntry.setStatus("mandatory")
_NbRtFibEntryIpAddress_Type = IpAddress
_NbRtFibEntryIpAddress_Object = MibTableColumn
nbRtFibEntryIpAddress = _NbRtFibEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 1),
    _NbRtFibEntryIpAddress_Type()
)
nbRtFibEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtFibEntryIpAddress.setStatus("mandatory")
_NbRtFibEntryIpMask_Type = IpAddress
_NbRtFibEntryIpMask_Object = MibTableColumn
nbRtFibEntryIpMask = _NbRtFibEntryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 2),
    _NbRtFibEntryIpMask_Type()
)
nbRtFibEntryIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtFibEntryIpMask.setStatus("mandatory")


class _NbRtFibEntryProtocol_Type(Integer32):
    """Custom type nbRtFibEntryProtocol based on Integer32"""
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
        *(("arp", 15),
          ("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("direct", 2),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("larp", 16),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_NbRtFibEntryProtocol_Type.__name__ = "Integer32"
_NbRtFibEntryProtocol_Object = MibTableColumn
nbRtFibEntryProtocol = _NbRtFibEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 3),
    _NbRtFibEntryProtocol_Type()
)
nbRtFibEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtFibEntryProtocol.setStatus("mandatory")
_NbRtFibEntryNextHop_Type = IpAddress
_NbRtFibEntryNextHop_Object = MibTableColumn
nbRtFibEntryNextHop = _NbRtFibEntryNextHop_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 4),
    _NbRtFibEntryNextHop_Type()
)
nbRtFibEntryNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryNextHop.setStatus("mandatory")
_NbRtFibEntryNextPhysAddress_Type = MacAddress
_NbRtFibEntryNextPhysAddress_Object = MibTableColumn
nbRtFibEntryNextPhysAddress = _NbRtFibEntryNextPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 5),
    _NbRtFibEntryNextPhysAddress_Type()
)
nbRtFibEntryNextPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryNextPhysAddress.setStatus("mandatory")
_NbRtFibEntryNextPort_Type = Integer32
_NbRtFibEntryNextPort_Object = MibTableColumn
nbRtFibEntryNextPort = _NbRtFibEntryNextPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 6),
    _NbRtFibEntryNextPort_Type()
)
nbRtFibEntryNextPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryNextPort.setStatus("mandatory")
_NbRtFibEntryLastChTime_Type = Integer32
_NbRtFibEntryLastChTime_Object = MibTableColumn
nbRtFibEntryLastChTime = _NbRtFibEntryLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 7),
    _NbRtFibEntryLastChTime_Type()
)
nbRtFibEntryLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtFibEntryLastChTime.setStatus("mandatory")
_NbRtFibEntryAge_Type = Integer32
_NbRtFibEntryAge_Object = MibTableColumn
nbRtFibEntryAge = _NbRtFibEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 8),
    _NbRtFibEntryAge_Type()
)
nbRtFibEntryAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryAge.setStatus("mandatory")
_NbRtFibEntryMetric_Type = Integer32
_NbRtFibEntryMetric_Object = MibTableColumn
nbRtFibEntryMetric = _NbRtFibEntryMetric_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 9),
    _NbRtFibEntryMetric_Type()
)
nbRtFibEntryMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryMetric.setStatus("mandatory")


class _NbRtFibEntryAdminStatus_Type(Integer32):
    """Custom type nbRtFibEntryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbRtFibEntryAdminStatus_Type.__name__ = "Integer32"
_NbRtFibEntryAdminStatus_Object = MibTableColumn
nbRtFibEntryAdminStatus = _NbRtFibEntryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 10),
    _NbRtFibEntryAdminStatus_Type()
)
nbRtFibEntryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryAdminStatus.setStatus("mandatory")


class _NbRtFibEntryTag_Type(Integer32):
    """Custom type nbRtFibEntryTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbRtFibEntryTag_Type.__name__ = "Integer32"
_NbRtFibEntryTag_Object = MibTableColumn
nbRtFibEntryTag = _NbRtFibEntryTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 4, 2, 1, 15),
    _NbRtFibEntryTag_Type()
)
nbRtFibEntryTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtFibEntryTag.setStatus("mandatory")
_NbRtDiffServ_ObjectIdentity = ObjectIdentity
nbRtDiffServ = _NbRtDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5)
)
_NbRtDiffServTable_Object = MibTable
nbRtDiffServTable = _NbRtDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2)
)
if mibBuilder.loadTexts:
    nbRtDiffServTable.setStatus("mandatory")
_NbRtDiffServEntry_Object = MibTableRow
nbRtDiffServEntry = _NbRtDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1)
)
nbRtDiffServEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
)
if mibBuilder.loadTexts:
    nbRtDiffServEntry.setStatus("mandatory")


class _NbRtDiffServMode_Type(Integer32):
    """Custom type nbRtDiffServMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("asGlobal", 10),
          ("byTOS", 3),
          ("byTag", 4),
          ("none", 2),
          ("other", 1))
    )


_NbRtDiffServMode_Type.__name__ = "Integer32"
_NbRtDiffServMode_Object = MibTableColumn
nbRtDiffServMode = _NbRtDiffServMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1, 2),
    _NbRtDiffServMode_Type()
)
nbRtDiffServMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServMode.setStatus("mandatory")
_NbRtDiffServVptMapNameIndex_Type = Integer32
_NbRtDiffServVptMapNameIndex_Object = MibTableColumn
nbRtDiffServVptMapNameIndex = _NbRtDiffServVptMapNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1, 3),
    _NbRtDiffServVptMapNameIndex_Type()
)
nbRtDiffServVptMapNameIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapNameIndex.setStatus("mandatory")
_NbRtDiffServDscpMapNameIndex_Type = Integer32
_NbRtDiffServDscpMapNameIndex_Object = MibTableColumn
nbRtDiffServDscpMapNameIndex = _NbRtDiffServDscpMapNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1, 4),
    _NbRtDiffServDscpMapNameIndex_Type()
)
nbRtDiffServDscpMapNameIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapNameIndex.setStatus("mandatory")
_NbRtDiffServMgmtVptMapNameIndex_Type = Integer32
_NbRtDiffServMgmtVptMapNameIndex_Object = MibTableColumn
nbRtDiffServMgmtVptMapNameIndex = _NbRtDiffServMgmtVptMapNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1, 5),
    _NbRtDiffServMgmtVptMapNameIndex_Type()
)
nbRtDiffServMgmtVptMapNameIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServMgmtVptMapNameIndex.setStatus("mandatory")
_NbRtDiffServMgmtDscpMapNameIndex_Type = Integer32
_NbRtDiffServMgmtDscpMapNameIndex_Object = MibTableColumn
nbRtDiffServMgmtDscpMapNameIndex = _NbRtDiffServMgmtDscpMapNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 2, 1, 6),
    _NbRtDiffServMgmtDscpMapNameIndex_Type()
)
nbRtDiffServMgmtDscpMapNameIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServMgmtDscpMapNameIndex.setStatus("mandatory")
_NbRtVifDiffServRateLimitTable_Object = MibTable
nbRtVifDiffServRateLimitTable = _NbRtVifDiffServRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4)
)
if mibBuilder.loadTexts:
    nbRtVifDiffServRateLimitTable.setStatus("mandatory")
_NbRtVifDiffServRateLimitEntry_Object = MibTableRow
nbRtVifDiffServRateLimitEntry = _NbRtVifDiffServRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1)
)
nbRtVifDiffServRateLimitEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
    (0, "IF-MIB", "ifIndex"),
    (0, "RT-CFG-MIB", "nbRtVifDiffServDirect"),
)
if mibBuilder.loadTexts:
    nbRtVifDiffServRateLimitEntry.setStatus("mandatory")
_NbRtVifDiffServDirect_Type = DirectionType
_NbRtVifDiffServDirect_Object = MibTableColumn
nbRtVifDiffServDirect = _NbRtVifDiffServDirect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1, 1),
    _NbRtVifDiffServDirect_Type()
)
nbRtVifDiffServDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbRtVifDiffServDirect.setStatus("mandatory")
_NbRtVifDiffServBuckRate_Type = Integer32
_NbRtVifDiffServBuckRate_Object = MibTableColumn
nbRtVifDiffServBuckRate = _NbRtVifDiffServBuckRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1, 2),
    _NbRtVifDiffServBuckRate_Type()
)
nbRtVifDiffServBuckRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifDiffServBuckRate.setStatus("mandatory")
_NbRtVifDiffServBuckSize_Type = Integer32
_NbRtVifDiffServBuckSize_Object = MibTableColumn
nbRtVifDiffServBuckSize = _NbRtVifDiffServBuckSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1, 3),
    _NbRtVifDiffServBuckSize_Type()
)
nbRtVifDiffServBuckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifDiffServBuckSize.setStatus("mandatory")


class _NbRtVifDiffServREDmode_Type(Integer32):
    """Custom type nbRtVifDiffServREDmode based on Integer32"""
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


_NbRtVifDiffServREDmode_Type.__name__ = "Integer32"
_NbRtVifDiffServREDmode_Object = MibTableColumn
nbRtVifDiffServREDmode = _NbRtVifDiffServREDmode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1, 4),
    _NbRtVifDiffServREDmode_Type()
)
nbRtVifDiffServREDmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifDiffServREDmode.setStatus("mandatory")


class _NbRtVifDiffServAdminStatus_Type(Integer32):
    """Custom type nbRtVifDiffServAdminStatus based on Integer32"""
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
        *(("absent", 5),
          ("createOrModify", 2),
          ("delete", 3),
          ("exist", 4),
          ("other", 1))
    )


_NbRtVifDiffServAdminStatus_Type.__name__ = "Integer32"
_NbRtVifDiffServAdminStatus_Object = MibTableColumn
nbRtVifDiffServAdminStatus = _NbRtVifDiffServAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 4, 1, 10),
    _NbRtVifDiffServAdminStatus_Type()
)
nbRtVifDiffServAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtVifDiffServAdminStatus.setStatus("mandatory")
_NbRtDiffServVptMapTable_Object = MibTable
nbRtDiffServVptMapTable = _NbRtDiffServVptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6)
)
if mibBuilder.loadTexts:
    nbRtDiffServVptMapTable.setStatus("mandatory")
_NbRtDiffServVptMapEntry_Object = MibTableRow
nbRtDiffServVptMapEntry = _NbRtDiffServVptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6, 1)
)
nbRtDiffServVptMapEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtDiffServVptMapNameId"),
)
if mibBuilder.loadTexts:
    nbRtDiffServVptMapEntry.setStatus("mandatory")
_NbRtDiffServVptMapNameId_Type = Integer32
_NbRtDiffServVptMapNameId_Object = MibTableColumn
nbRtDiffServVptMapNameId = _NbRtDiffServVptMapNameId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6, 1, 1),
    _NbRtDiffServVptMapNameId_Type()
)
nbRtDiffServVptMapNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapNameId.setStatus("mandatory")


class _NbRtDiffServVptMapName_Type(DisplayString):
    """Custom type nbRtDiffServVptMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NbRtDiffServVptMapName_Type.__name__ = "DisplayString"
_NbRtDiffServVptMapName_Object = MibTableColumn
nbRtDiffServVptMapName = _NbRtDiffServVptMapName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6, 1, 2),
    _NbRtDiffServVptMapName_Type()
)
nbRtDiffServVptMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapName.setStatus("mandatory")


class _NbRtDiffServVptMapStatus_Type(Integer32):
    """Custom type nbRtDiffServVptMapStatus based on Integer32"""
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
          ("notActive", 3),
          ("other", 1))
    )


_NbRtDiffServVptMapStatus_Type.__name__ = "Integer32"
_NbRtDiffServVptMapStatus_Object = MibTableColumn
nbRtDiffServVptMapStatus = _NbRtDiffServVptMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6, 1, 3),
    _NbRtDiffServVptMapStatus_Type()
)
nbRtDiffServVptMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapStatus.setStatus("mandatory")


class _NbRtDiffServVptMapAdminStatus_Type(Integer32):
    """Custom type nbRtDiffServVptMapAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("restoreDefaultConfig", 3),
          ("valid", 1))
    )


_NbRtDiffServVptMapAdminStatus_Type.__name__ = "Integer32"
_NbRtDiffServVptMapAdminStatus_Object = MibTableColumn
nbRtDiffServVptMapAdminStatus = _NbRtDiffServVptMapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 6, 1, 4),
    _NbRtDiffServVptMapAdminStatus_Type()
)
nbRtDiffServVptMapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapAdminStatus.setStatus("mandatory")
_NbRtDiffServVptMapPrflTable_Object = MibTable
nbRtDiffServVptMapPrflTable = _NbRtDiffServVptMapPrflTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8)
)
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflTable.setStatus("mandatory")
_NbRtDiffServVptMapPrflEntry_Object = MibTableRow
nbRtDiffServVptMapPrflEntry = _NbRtDiffServVptMapPrflEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1)
)
nbRtDiffServVptMapPrflEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtDiffServVptMapPrflNameId"),
    (0, "RT-CFG-MIB", "nbRtDiffServVptMapPrflInValueId"),
)
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflEntry.setStatus("mandatory")
_NbRtDiffServVptMapPrflNameId_Type = Integer32
_NbRtDiffServVptMapPrflNameId_Object = MibTableColumn
nbRtDiffServVptMapPrflNameId = _NbRtDiffServVptMapPrflNameId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1, 1),
    _NbRtDiffServVptMapPrflNameId_Type()
)
nbRtDiffServVptMapPrflNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflNameId.setStatus("mandatory")
_NbRtDiffServVptMapPrflInValueId_Type = Integer32
_NbRtDiffServVptMapPrflInValueId_Object = MibTableColumn
nbRtDiffServVptMapPrflInValueId = _NbRtDiffServVptMapPrflInValueId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1, 2),
    _NbRtDiffServVptMapPrflInValueId_Type()
)
nbRtDiffServVptMapPrflInValueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflInValueId.setStatus("mandatory")
_NbRtDiffServVptMapPrflInValue_Type = Integer32
_NbRtDiffServVptMapPrflInValue_Object = MibTableColumn
nbRtDiffServVptMapPrflInValue = _NbRtDiffServVptMapPrflInValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1, 3),
    _NbRtDiffServVptMapPrflInValue_Type()
)
nbRtDiffServVptMapPrflInValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflInValue.setStatus("mandatory")
_NbRtDiffServVptMapPrflSl_Type = Integer32
_NbRtDiffServVptMapPrflSl_Object = MibTableColumn
nbRtDiffServVptMapPrflSl = _NbRtDiffServVptMapPrflSl_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1, 4),
    _NbRtDiffServVptMapPrflSl_Type()
)
nbRtDiffServVptMapPrflSl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflSl.setStatus("mandatory")
_NbRtDiffServVptMapPrflOutValue_Type = Integer32
_NbRtDiffServVptMapPrflOutValue_Object = MibTableColumn
nbRtDiffServVptMapPrflOutValue = _NbRtDiffServVptMapPrflOutValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 8, 1, 5),
    _NbRtDiffServVptMapPrflOutValue_Type()
)
nbRtDiffServVptMapPrflOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServVptMapPrflOutValue.setStatus("mandatory")
_NbRtDiffServDscpMapTable_Object = MibTable
nbRtDiffServDscpMapTable = _NbRtDiffServDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10)
)
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapTable.setStatus("mandatory")
_NbRtDiffServDscpMapEntry_Object = MibTableRow
nbRtDiffServDscpMapEntry = _NbRtDiffServDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10, 1)
)
nbRtDiffServDscpMapEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtDiffServDscpMapNameId"),
)
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapEntry.setStatus("mandatory")
_NbRtDiffServDscpMapNameId_Type = Integer32
_NbRtDiffServDscpMapNameId_Object = MibTableColumn
nbRtDiffServDscpMapNameId = _NbRtDiffServDscpMapNameId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10, 1, 1),
    _NbRtDiffServDscpMapNameId_Type()
)
nbRtDiffServDscpMapNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapNameId.setStatus("mandatory")


class _NbRtDiffServDscpMapName_Type(DisplayString):
    """Custom type nbRtDiffServDscpMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NbRtDiffServDscpMapName_Type.__name__ = "DisplayString"
_NbRtDiffServDscpMapName_Object = MibTableColumn
nbRtDiffServDscpMapName = _NbRtDiffServDscpMapName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10, 1, 2),
    _NbRtDiffServDscpMapName_Type()
)
nbRtDiffServDscpMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapName.setStatus("mandatory")


class _NbRtDiffServDscpMapStatus_Type(Integer32):
    """Custom type nbRtDiffServDscpMapStatus based on Integer32"""
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
          ("notActive", 3),
          ("other", 1))
    )


_NbRtDiffServDscpMapStatus_Type.__name__ = "Integer32"
_NbRtDiffServDscpMapStatus_Object = MibTableColumn
nbRtDiffServDscpMapStatus = _NbRtDiffServDscpMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10, 1, 3),
    _NbRtDiffServDscpMapStatus_Type()
)
nbRtDiffServDscpMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapStatus.setStatus("mandatory")


class _NbRtDiffServDscpMapAdminStatus_Type(Integer32):
    """Custom type nbRtDiffServDscpMapAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("restoreDefaultConfig", 3),
          ("valid", 1))
    )


_NbRtDiffServDscpMapAdminStatus_Type.__name__ = "Integer32"
_NbRtDiffServDscpMapAdminStatus_Object = MibTableColumn
nbRtDiffServDscpMapAdminStatus = _NbRtDiffServDscpMapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 10, 1, 4),
    _NbRtDiffServDscpMapAdminStatus_Type()
)
nbRtDiffServDscpMapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapAdminStatus.setStatus("mandatory")
_NbRtDiffServDscpMapPrflTable_Object = MibTable
nbRtDiffServDscpMapPrflTable = _NbRtDiffServDscpMapPrflTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12)
)
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflTable.setStatus("mandatory")
_NbRtDiffServDscpMapPrflEntry_Object = MibTableRow
nbRtDiffServDscpMapPrflEntry = _NbRtDiffServDscpMapPrflEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1)
)
nbRtDiffServDscpMapPrflEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtDiffServDscpMapPrflNameId"),
    (0, "RT-CFG-MIB", "nbRtDiffServDscpMapPrflInValueId"),
)
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflEntry.setStatus("mandatory")
_NbRtDiffServDscpMapPrflNameId_Type = Integer32
_NbRtDiffServDscpMapPrflNameId_Object = MibTableColumn
nbRtDiffServDscpMapPrflNameId = _NbRtDiffServDscpMapPrflNameId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1, 1),
    _NbRtDiffServDscpMapPrflNameId_Type()
)
nbRtDiffServDscpMapPrflNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflNameId.setStatus("mandatory")
_NbRtDiffServDscpMapPrflInValueId_Type = Integer32
_NbRtDiffServDscpMapPrflInValueId_Object = MibTableColumn
nbRtDiffServDscpMapPrflInValueId = _NbRtDiffServDscpMapPrflInValueId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1, 2),
    _NbRtDiffServDscpMapPrflInValueId_Type()
)
nbRtDiffServDscpMapPrflInValueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflInValueId.setStatus("mandatory")
_NbRtDiffServDscpMapPrflInValue_Type = Integer32
_NbRtDiffServDscpMapPrflInValue_Object = MibTableColumn
nbRtDiffServDscpMapPrflInValue = _NbRtDiffServDscpMapPrflInValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1, 3),
    _NbRtDiffServDscpMapPrflInValue_Type()
)
nbRtDiffServDscpMapPrflInValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflInValue.setStatus("mandatory")
_NbRtDiffServDscpMapPrflSl_Type = Integer32
_NbRtDiffServDscpMapPrflSl_Object = MibTableColumn
nbRtDiffServDscpMapPrflSl = _NbRtDiffServDscpMapPrflSl_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1, 4),
    _NbRtDiffServDscpMapPrflSl_Type()
)
nbRtDiffServDscpMapPrflSl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflSl.setStatus("mandatory")
_NbRtDiffServDscpMapPrflOutValue_Type = Integer32
_NbRtDiffServDscpMapPrflOutValue_Object = MibTableColumn
nbRtDiffServDscpMapPrflOutValue = _NbRtDiffServDscpMapPrflOutValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 5, 12, 1, 5),
    _NbRtDiffServDscpMapPrflOutValue_Type()
)
nbRtDiffServDscpMapPrflOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtDiffServDscpMapPrflOutValue.setStatus("mandatory")
_NbRtAccounting_ObjectIdentity = ObjectIdentity
nbRtAccounting = _NbRtAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6)
)
_NbRtAccVifTable_Object = MibTable
nbRtAccVifTable = _NbRtAccVifTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10)
)
if mibBuilder.loadTexts:
    nbRtAccVifTable.setStatus("mandatory")
_NbRtAccVifEntry_Object = MibTableRow
nbRtAccVifEntry = _NbRtAccVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1)
)
nbRtAccVifEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
    (0, "RT-CFG-MIB", "nbRtAccVifDirection"),
)
if mibBuilder.loadTexts:
    nbRtAccVifEntry.setStatus("mandatory")
_NbRtAccVifDirection_Type = DirectionType
_NbRtAccVifDirection_Object = MibTableColumn
nbRtAccVifDirection = _NbRtAccVifDirection_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 1),
    _NbRtAccVifDirection_Type()
)
nbRtAccVifDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifDirection.setStatus("mandatory")


class _NbRtAccVifAdminStatus_Type(Integer32):
    """Custom type nbRtAccVifAdminStatus based on Integer32"""
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
        *(("clear", 6),
          ("disable", 3),
          ("enable", 2),
          ("other", 1),
          ("pause", 4),
          ("resume", 5))
    )


_NbRtAccVifAdminStatus_Type.__name__ = "Integer32"
_NbRtAccVifAdminStatus_Object = MibTableColumn
nbRtAccVifAdminStatus = _NbRtAccVifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 3),
    _NbRtAccVifAdminStatus_Type()
)
nbRtAccVifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtAccVifAdminStatus.setStatus("mandatory")


class _NbRtAccVifOperStatus_Type(Integer32):
    """Custom type nbRtAccVifOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 4),
          ("other", 1),
          ("paused", 3))
    )


_NbRtAccVifOperStatus_Type.__name__ = "Integer32"
_NbRtAccVifOperStatus_Object = MibTableColumn
nbRtAccVifOperStatus = _NbRtAccVifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 4),
    _NbRtAccVifOperStatus_Type()
)
nbRtAccVifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifOperStatus.setStatus("mandatory")
_NbRtAccVifConformingBytes_Type = AccountCouter
_NbRtAccVifConformingBytes_Object = MibTableColumn
nbRtAccVifConformingBytes = _NbRtAccVifConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 6),
    _NbRtAccVifConformingBytes_Type()
)
nbRtAccVifConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifConformingBytes.setStatus("mandatory")
_NbRtAccVifExceedingBytes_Type = AccountCouter
_NbRtAccVifExceedingBytes_Object = MibTableColumn
nbRtAccVifExceedingBytes = _NbRtAccVifExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 7),
    _NbRtAccVifExceedingBytes_Type()
)
nbRtAccVifExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifExceedingBytes.setStatus("mandatory")
_NbRtAccVifConformingPackets_Type = AccountCouter
_NbRtAccVifConformingPackets_Object = MibTableColumn
nbRtAccVifConformingPackets = _NbRtAccVifConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 8),
    _NbRtAccVifConformingPackets_Type()
)
nbRtAccVifConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifConformingPackets.setStatus("mandatory")
_NbRtAccVifExceedingPackets_Type = AccountCouter
_NbRtAccVifExceedingPackets_Object = MibTableColumn
nbRtAccVifExceedingPackets = _NbRtAccVifExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 9),
    _NbRtAccVifExceedingPackets_Type()
)
nbRtAccVifExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifExceedingPackets.setStatus("mandatory")
_NbRtAccVifHighConformingBytes_Type = Counter32
_NbRtAccVifHighConformingBytes_Object = MibTableColumn
nbRtAccVifHighConformingBytes = _NbRtAccVifHighConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 11),
    _NbRtAccVifHighConformingBytes_Type()
)
nbRtAccVifHighConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighConformingBytes.setStatus("mandatory")
_NbRtAccVifHighExceedingBytes_Type = Counter32
_NbRtAccVifHighExceedingBytes_Object = MibTableColumn
nbRtAccVifHighExceedingBytes = _NbRtAccVifHighExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 12),
    _NbRtAccVifHighExceedingBytes_Type()
)
nbRtAccVifHighExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighExceedingBytes.setStatus("mandatory")
_NbRtAccVifHighConformingPackets_Type = Counter32
_NbRtAccVifHighConformingPackets_Object = MibTableColumn
nbRtAccVifHighConformingPackets = _NbRtAccVifHighConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 13),
    _NbRtAccVifHighConformingPackets_Type()
)
nbRtAccVifHighConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighConformingPackets.setStatus("mandatory")
_NbRtAccVifHighExceedingPackets_Type = Counter32
_NbRtAccVifHighExceedingPackets_Object = MibTableColumn
nbRtAccVifHighExceedingPackets = _NbRtAccVifHighExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 14),
    _NbRtAccVifHighExceedingPackets_Type()
)
nbRtAccVifHighExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighExceedingPackets.setStatus("mandatory")
_NbRtAccVifLowConformingBytes_Type = Counter32
_NbRtAccVifLowConformingBytes_Object = MibTableColumn
nbRtAccVifLowConformingBytes = _NbRtAccVifLowConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 15),
    _NbRtAccVifLowConformingBytes_Type()
)
nbRtAccVifLowConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowConformingBytes.setStatus("mandatory")
_NbRtAccVifLowExceedingBytes_Type = Counter32
_NbRtAccVifLowExceedingBytes_Object = MibTableColumn
nbRtAccVifLowExceedingBytes = _NbRtAccVifLowExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 16),
    _NbRtAccVifLowExceedingBytes_Type()
)
nbRtAccVifLowExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowExceedingBytes.setStatus("mandatory")
_NbRtAccVifLowConformingPackets_Type = Counter32
_NbRtAccVifLowConformingPackets_Object = MibTableColumn
nbRtAccVifLowConformingPackets = _NbRtAccVifLowConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 17),
    _NbRtAccVifLowConformingPackets_Type()
)
nbRtAccVifLowConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowConformingPackets.setStatus("mandatory")
_NbRtAccVifLowExceedingPackets_Type = Counter32
_NbRtAccVifLowExceedingPackets_Object = MibTableColumn
nbRtAccVifLowExceedingPackets = _NbRtAccVifLowExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 18),
    _NbRtAccVifLowExceedingPackets_Type()
)
nbRtAccVifLowExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowExceedingPackets.setStatus("mandatory")
_NbRtAccVif64ConformingBytes_Type = AccountCounter64
_NbRtAccVif64ConformingBytes_Object = MibTableColumn
nbRtAccVif64ConformingBytes = _NbRtAccVif64ConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 19),
    _NbRtAccVif64ConformingBytes_Type()
)
nbRtAccVif64ConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVif64ConformingBytes.setStatus("mandatory")
_NbRtAccVif64ExceedingBytes_Type = AccountCounter64
_NbRtAccVif64ExceedingBytes_Object = MibTableColumn
nbRtAccVif64ExceedingBytes = _NbRtAccVif64ExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 20),
    _NbRtAccVif64ExceedingBytes_Type()
)
nbRtAccVif64ExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVif64ExceedingBytes.setStatus("mandatory")
_NbRtAccVifConformingUcastPackets_Type = AccountCouter
_NbRtAccVifConformingUcastPackets_Object = MibTableColumn
nbRtAccVifConformingUcastPackets = _NbRtAccVifConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 21),
    _NbRtAccVifConformingUcastPackets_Type()
)
nbRtAccVifConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifConformingUcastPackets.setStatus("mandatory")
_NbRtAccVifHighConformingUcastPackets_Type = Counter32
_NbRtAccVifHighConformingUcastPackets_Object = MibTableColumn
nbRtAccVifHighConformingUcastPackets = _NbRtAccVifHighConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 22),
    _NbRtAccVifHighConformingUcastPackets_Type()
)
nbRtAccVifHighConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighConformingUcastPackets.setStatus("mandatory")
_NbRtAccVifLowConformingUcastPackets_Type = Counter32
_NbRtAccVifLowConformingUcastPackets_Object = MibTableColumn
nbRtAccVifLowConformingUcastPackets = _NbRtAccVifLowConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 23),
    _NbRtAccVifLowConformingUcastPackets_Type()
)
nbRtAccVifLowConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowConformingUcastPackets.setStatus("mandatory")
_NbRtAccVif64ConformingUcastPackets_Type = AccountCounter64
_NbRtAccVif64ConformingUcastPackets_Object = MibTableColumn
nbRtAccVif64ConformingUcastPackets = _NbRtAccVif64ConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 24),
    _NbRtAccVif64ConformingUcastPackets_Type()
)
nbRtAccVif64ConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVif64ConformingUcastPackets.setStatus("mandatory")
_NbRtAccVifConformingMcastPackets_Type = AccountCouter
_NbRtAccVifConformingMcastPackets_Object = MibTableColumn
nbRtAccVifConformingMcastPackets = _NbRtAccVifConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 25),
    _NbRtAccVifConformingMcastPackets_Type()
)
nbRtAccVifConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifConformingMcastPackets.setStatus("mandatory")
_NbRtAccVifHighConformingMcastPackets_Type = Counter32
_NbRtAccVifHighConformingMcastPackets_Object = MibTableColumn
nbRtAccVifHighConformingMcastPackets = _NbRtAccVifHighConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 26),
    _NbRtAccVifHighConformingMcastPackets_Type()
)
nbRtAccVifHighConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighConformingMcastPackets.setStatus("mandatory")
_NbRtAccVifLowConformingMcastPackets_Type = Counter32
_NbRtAccVifLowConformingMcastPackets_Object = MibTableColumn
nbRtAccVifLowConformingMcastPackets = _NbRtAccVifLowConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 27),
    _NbRtAccVifLowConformingMcastPackets_Type()
)
nbRtAccVifLowConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowConformingMcastPackets.setStatus("mandatory")
_NbRtAccVif64ConformingMcastPackets_Type = AccountCounter64
_NbRtAccVif64ConformingMcastPackets_Object = MibTableColumn
nbRtAccVif64ConformingMcastPackets = _NbRtAccVif64ConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 28),
    _NbRtAccVif64ConformingMcastPackets_Type()
)
nbRtAccVif64ConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVif64ConformingMcastPackets.setStatus("mandatory")
_NbRtAccVifConformingBcastPackets_Type = AccountCouter
_NbRtAccVifConformingBcastPackets_Object = MibTableColumn
nbRtAccVifConformingBcastPackets = _NbRtAccVifConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 29),
    _NbRtAccVifConformingBcastPackets_Type()
)
nbRtAccVifConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifConformingBcastPackets.setStatus("mandatory")
_NbRtAccVifHighConformingBcastPackets_Type = Counter32
_NbRtAccVifHighConformingBcastPackets_Object = MibTableColumn
nbRtAccVifHighConformingBcastPackets = _NbRtAccVifHighConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 30),
    _NbRtAccVifHighConformingBcastPackets_Type()
)
nbRtAccVifHighConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifHighConformingBcastPackets.setStatus("mandatory")
_NbRtAccVifLowConformingBcastPackets_Type = Counter32
_NbRtAccVifLowConformingBcastPackets_Object = MibTableColumn
nbRtAccVifLowConformingBcastPackets = _NbRtAccVifLowConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 31),
    _NbRtAccVifLowConformingBcastPackets_Type()
)
nbRtAccVifLowConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVifLowConformingBcastPackets.setStatus("mandatory")
_NbRtAccVif64ConformingBcastPackets_Type = AccountCounter64
_NbRtAccVif64ConformingBcastPackets_Object = MibTableColumn
nbRtAccVif64ConformingBcastPackets = _NbRtAccVif64ConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 10, 1, 32),
    _NbRtAccVif64ConformingBcastPackets_Type()
)
nbRtAccVif64ConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccVif64ConformingBcastPackets.setStatus("mandatory")
_NbRtAccVifPortTable_Object = MibTable
nbRtAccVifPortTable = _NbRtAccVifPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12)
)
if mibBuilder.loadTexts:
    nbRtAccVifPortTable.setStatus("mandatory")
_NbRtAccVifPortEntry_Object = MibTableRow
nbRtAccVifPortEntry = _NbRtAccVifPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1)
)
nbRtAccVifPortEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
    (0, "RT-CFG-MIB", "nbRtVifPortId"),
    (0, "RT-CFG-MIB", "nbRtAccVifDirection"),
)
if mibBuilder.loadTexts:
    nbRtAccVifPortEntry.setStatus("mandatory")
_NbRtVifPortId_Type = Integer32
_NbRtVifPortId_Object = MibTableColumn
nbRtVifPortId = _NbRtVifPortId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 1),
    _NbRtVifPortId_Type()
)
nbRtVifPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtVifPortId.setStatus("mandatory")


class _NbRtAccPortAdminStatus_Type(Integer32):
    """Custom type nbRtAccPortAdminStatus based on Integer32"""
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
        *(("clear", 6),
          ("disable", 3),
          ("enable", 2),
          ("other", 1),
          ("pause", 4),
          ("resume", 5))
    )


_NbRtAccPortAdminStatus_Type.__name__ = "Integer32"
_NbRtAccPortAdminStatus_Object = MibTableColumn
nbRtAccPortAdminStatus = _NbRtAccPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 2),
    _NbRtAccPortAdminStatus_Type()
)
nbRtAccPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtAccPortAdminStatus.setStatus("mandatory")


class _NbRtAccPortOperStatus_Type(Integer32):
    """Custom type nbRtAccPortOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 4),
          ("other", 1),
          ("paused", 3))
    )


_NbRtAccPortOperStatus_Type.__name__ = "Integer32"
_NbRtAccPortOperStatus_Object = MibTableColumn
nbRtAccPortOperStatus = _NbRtAccPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 3),
    _NbRtAccPortOperStatus_Type()
)
nbRtAccPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortOperStatus.setStatus("mandatory")
_NbRtAccPortConformingBytes_Type = AccountCouter
_NbRtAccPortConformingBytes_Object = MibTableColumn
nbRtAccPortConformingBytes = _NbRtAccPortConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 6),
    _NbRtAccPortConformingBytes_Type()
)
nbRtAccPortConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortConformingBytes.setStatus("mandatory")
_NbRtAccPortExceedingBytes_Type = AccountCouter
_NbRtAccPortExceedingBytes_Object = MibTableColumn
nbRtAccPortExceedingBytes = _NbRtAccPortExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 7),
    _NbRtAccPortExceedingBytes_Type()
)
nbRtAccPortExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortExceedingBytes.setStatus("mandatory")
_NbRtAccPortConformingPackets_Type = AccountCouter
_NbRtAccPortConformingPackets_Object = MibTableColumn
nbRtAccPortConformingPackets = _NbRtAccPortConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 8),
    _NbRtAccPortConformingPackets_Type()
)
nbRtAccPortConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortConformingPackets.setStatus("mandatory")
_NbRtAccPortExceedingPackets_Type = AccountCouter
_NbRtAccPortExceedingPackets_Object = MibTableColumn
nbRtAccPortExceedingPackets = _NbRtAccPortExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 9),
    _NbRtAccPortExceedingPackets_Type()
)
nbRtAccPortExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortExceedingPackets.setStatus("mandatory")
_NbRtAccPortHighConformingBytes_Type = Counter32
_NbRtAccPortHighConformingBytes_Object = MibTableColumn
nbRtAccPortHighConformingBytes = _NbRtAccPortHighConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 11),
    _NbRtAccPortHighConformingBytes_Type()
)
nbRtAccPortHighConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighConformingBytes.setStatus("mandatory")
_NbRtAccPortHighExceedingBytes_Type = Counter32
_NbRtAccPortHighExceedingBytes_Object = MibTableColumn
nbRtAccPortHighExceedingBytes = _NbRtAccPortHighExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 12),
    _NbRtAccPortHighExceedingBytes_Type()
)
nbRtAccPortHighExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighExceedingBytes.setStatus("mandatory")
_NbRtAccPortHighConformingPackets_Type = Counter32
_NbRtAccPortHighConformingPackets_Object = MibTableColumn
nbRtAccPortHighConformingPackets = _NbRtAccPortHighConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 13),
    _NbRtAccPortHighConformingPackets_Type()
)
nbRtAccPortHighConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighConformingPackets.setStatus("mandatory")
_NbRtAccPortHighExceedingPackets_Type = Counter32
_NbRtAccPortHighExceedingPackets_Object = MibTableColumn
nbRtAccPortHighExceedingPackets = _NbRtAccPortHighExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 14),
    _NbRtAccPortHighExceedingPackets_Type()
)
nbRtAccPortHighExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighExceedingPackets.setStatus("mandatory")
_NbRtAccPortLowConformingBytes_Type = Counter32
_NbRtAccPortLowConformingBytes_Object = MibTableColumn
nbRtAccPortLowConformingBytes = _NbRtAccPortLowConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 15),
    _NbRtAccPortLowConformingBytes_Type()
)
nbRtAccPortLowConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowConformingBytes.setStatus("mandatory")
_NbRtAccPortLowExceedingBytes_Type = Counter32
_NbRtAccPortLowExceedingBytes_Object = MibTableColumn
nbRtAccPortLowExceedingBytes = _NbRtAccPortLowExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 16),
    _NbRtAccPortLowExceedingBytes_Type()
)
nbRtAccPortLowExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowExceedingBytes.setStatus("mandatory")
_NbRtAccPortLowConformingPackets_Type = Counter32
_NbRtAccPortLowConformingPackets_Object = MibTableColumn
nbRtAccPortLowConformingPackets = _NbRtAccPortLowConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 17),
    _NbRtAccPortLowConformingPackets_Type()
)
nbRtAccPortLowConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowConformingPackets.setStatus("mandatory")
_NbRtAccPortLowExceedingPackets_Type = Counter32
_NbRtAccPortLowExceedingPackets_Object = MibTableColumn
nbRtAccPortLowExceedingPackets = _NbRtAccPortLowExceedingPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 18),
    _NbRtAccPortLowExceedingPackets_Type()
)
nbRtAccPortLowExceedingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowExceedingPackets.setStatus("mandatory")
_NbRtAccPortVif64ConformingBytes_Type = AccountCounter64
_NbRtAccPortVif64ConformingBytes_Object = MibTableColumn
nbRtAccPortVif64ConformingBytes = _NbRtAccPortVif64ConformingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 19),
    _NbRtAccPortVif64ConformingBytes_Type()
)
nbRtAccPortVif64ConformingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortVif64ConformingBytes.setStatus("mandatory")
_NbRtAccPortVif64ExceedingBytes_Type = AccountCounter64
_NbRtAccPortVif64ExceedingBytes_Object = MibTableColumn
nbRtAccPortVif64ExceedingBytes = _NbRtAccPortVif64ExceedingBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 20),
    _NbRtAccPortVif64ExceedingBytes_Type()
)
nbRtAccPortVif64ExceedingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortVif64ExceedingBytes.setStatus("mandatory")
_NbRtAccPortConformingUcastPackets_Type = AccountCouter
_NbRtAccPortConformingUcastPackets_Object = MibTableColumn
nbRtAccPortConformingUcastPackets = _NbRtAccPortConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 21),
    _NbRtAccPortConformingUcastPackets_Type()
)
nbRtAccPortConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortConformingUcastPackets.setStatus("mandatory")
_NbRtAccPortHighConformingUcastPackets_Type = Counter32
_NbRtAccPortHighConformingUcastPackets_Object = MibTableColumn
nbRtAccPortHighConformingUcastPackets = _NbRtAccPortHighConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 22),
    _NbRtAccPortHighConformingUcastPackets_Type()
)
nbRtAccPortHighConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighConformingUcastPackets.setStatus("mandatory")
_NbRtAccPortLowConformingUcastPackets_Type = Counter32
_NbRtAccPortLowConformingUcastPackets_Object = MibTableColumn
nbRtAccPortLowConformingUcastPackets = _NbRtAccPortLowConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 23),
    _NbRtAccPortLowConformingUcastPackets_Type()
)
nbRtAccPortLowConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowConformingUcastPackets.setStatus("mandatory")
_NbRtAccPort64ConformingUcastPackets_Type = AccountCounter64
_NbRtAccPort64ConformingUcastPackets_Object = MibTableColumn
nbRtAccPort64ConformingUcastPackets = _NbRtAccPort64ConformingUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 24),
    _NbRtAccPort64ConformingUcastPackets_Type()
)
nbRtAccPort64ConformingUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPort64ConformingUcastPackets.setStatus("mandatory")
_NbRtAccPortConformingMcastPackets_Type = AccountCouter
_NbRtAccPortConformingMcastPackets_Object = MibTableColumn
nbRtAccPortConformingMcastPackets = _NbRtAccPortConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 25),
    _NbRtAccPortConformingMcastPackets_Type()
)
nbRtAccPortConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortConformingMcastPackets.setStatus("mandatory")
_NbRtAccPortHighConformingMcastPackets_Type = Counter32
_NbRtAccPortHighConformingMcastPackets_Object = MibTableColumn
nbRtAccPortHighConformingMcastPackets = _NbRtAccPortHighConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 26),
    _NbRtAccPortHighConformingMcastPackets_Type()
)
nbRtAccPortHighConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighConformingMcastPackets.setStatus("mandatory")
_NbRtAccPortLowConformingMcastPackets_Type = Counter32
_NbRtAccPortLowConformingMcastPackets_Object = MibTableColumn
nbRtAccPortLowConformingMcastPackets = _NbRtAccPortLowConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 27),
    _NbRtAccPortLowConformingMcastPackets_Type()
)
nbRtAccPortLowConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowConformingMcastPackets.setStatus("mandatory")
_NbRtAccPort64ConformingMcastPackets_Type = AccountCounter64
_NbRtAccPort64ConformingMcastPackets_Object = MibTableColumn
nbRtAccPort64ConformingMcastPackets = _NbRtAccPort64ConformingMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 28),
    _NbRtAccPort64ConformingMcastPackets_Type()
)
nbRtAccPort64ConformingMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPort64ConformingMcastPackets.setStatus("mandatory")
_NbRtAccPortConformingBcastPackets_Type = AccountCouter
_NbRtAccPortConformingBcastPackets_Object = MibTableColumn
nbRtAccPortConformingBcastPackets = _NbRtAccPortConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 29),
    _NbRtAccPortConformingBcastPackets_Type()
)
nbRtAccPortConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortConformingBcastPackets.setStatus("mandatory")
_NbRtAccPortHighConformingBcastPackets_Type = Counter32
_NbRtAccPortHighConformingBcastPackets_Object = MibTableColumn
nbRtAccPortHighConformingBcastPackets = _NbRtAccPortHighConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 30),
    _NbRtAccPortHighConformingBcastPackets_Type()
)
nbRtAccPortHighConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortHighConformingBcastPackets.setStatus("mandatory")
_NbRtAccPortLowConformingBcastPackets_Type = Counter32
_NbRtAccPortLowConformingBcastPackets_Object = MibTableColumn
nbRtAccPortLowConformingBcastPackets = _NbRtAccPortLowConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 31),
    _NbRtAccPortLowConformingBcastPackets_Type()
)
nbRtAccPortLowConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPortLowConformingBcastPackets.setStatus("mandatory")
_NbRtAccPort64ConformingBcastPackets_Type = AccountCounter64
_NbRtAccPort64ConformingBcastPackets_Object = MibTableColumn
nbRtAccPort64ConformingBcastPackets = _NbRtAccPort64ConformingBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 6, 12, 1, 32),
    _NbRtAccPort64ConformingBcastPackets_Type()
)
nbRtAccPort64ConformingBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtAccPort64ConformingBcastPackets.setStatus("mandatory")
_NbRtAccessLists_ObjectIdentity = ObjectIdentity
nbRtAccessLists = _NbRtAccessLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7)
)
_NbAclVifTable_Object = MibTable
nbAclVifTable = _NbAclVifTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5)
)
if mibBuilder.loadTexts:
    nbAclVifTable.setStatus("mandatory")
_NbAclVifEntry_Object = MibTableRow
nbAclVifEntry = _NbAclVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5, 1)
)
nbAclVifEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
    (0, "RT-CFG-MIB", "nbAclVifDirection"),
    (0, "RT-CFG-MIB", "nbAclVifId"),
)
if mibBuilder.loadTexts:
    nbAclVifEntry.setStatus("mandatory")
_NbAclVifDirection_Type = DirectionType
_NbAclVifDirection_Object = MibTableColumn
nbAclVifDirection = _NbAclVifDirection_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5, 1, 5),
    _NbAclVifDirection_Type()
)
nbAclVifDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbAclVifDirection.setStatus("mandatory")
_NbAclVifId_Type = Integer32
_NbAclVifId_Object = MibTableColumn
nbAclVifId = _NbAclVifId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5, 1, 6),
    _NbAclVifId_Type()
)
nbAclVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbAclVifId.setStatus("mandatory")
_NbAclVifAccessListName_Type = DisplayString
_NbAclVifAccessListName_Object = MibTableColumn
nbAclVifAccessListName = _NbAclVifAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5, 1, 7),
    _NbAclVifAccessListName_Type()
)
nbAclVifAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbAclVifAccessListName.setStatus("mandatory")


class _NbAclVifBindingStatus_Type(Integer32):
    """Custom type nbAclVifBindingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bind", 1),
          ("unbind", 2))
    )


_NbAclVifBindingStatus_Type.__name__ = "Integer32"
_NbAclVifBindingStatus_Object = MibTableColumn
nbAclVifBindingStatus = _NbAclVifBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 7, 5, 1, 8),
    _NbAclVifBindingStatus_Type()
)
nbAclVifBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbAclVifBindingStatus.setStatus("mandatory")
_NbRtPortTagGroup_ObjectIdentity = ObjectIdentity
nbRtPortTagGroup = _NbRtPortTagGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8)
)
_NbRtPortTagTable_Object = MibTable
nbRtPortTagTable = _NbRtPortTagTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5)
)
if mibBuilder.loadTexts:
    nbRtPortTagTable.setStatus("mandatory")
_NbRtPortTagEntry_Object = MibTableRow
nbRtPortTagEntry = _NbRtPortTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1)
)
nbRtPortTagEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtPortTagId"),
)
if mibBuilder.loadTexts:
    nbRtPortTagEntry.setStatus("mandatory")
_NbRtPortTagId_Type = Integer32
_NbRtPortTagId_Object = MibTableColumn
nbRtPortTagId = _NbRtPortTagId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 1),
    _NbRtPortTagId_Type()
)
nbRtPortTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPortTagId.setStatus("mandatory")


class _NbRtPortTagAwareMode_Type(Integer32):
    """Custom type nbRtPortTagAwareMode based on Integer32"""
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
        *(("hybrid", 4),
          ("other", 1),
          ("qInQtagged", 5),
          ("qInQuntagged", 6),
          ("qInQuntagged2", 7),
          ("tagged", 2),
          ("untagged", 3))
    )


_NbRtPortTagAwareMode_Type.__name__ = "Integer32"
_NbRtPortTagAwareMode_Object = MibTableColumn
nbRtPortTagAwareMode = _NbRtPortTagAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 2),
    _NbRtPortTagAwareMode_Type()
)
nbRtPortTagAwareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPortTagAwareMode.setStatus("mandatory")


class _NbRtPortTagEtherType_Type(Integer32):
    """Custom type nbRtPortTagEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbRtPortTagEtherType_Type.__name__ = "Integer32"
_NbRtPortTagEtherType_Object = MibTableColumn
nbRtPortTagEtherType = _NbRtPortTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 3),
    _NbRtPortTagEtherType_Type()
)
nbRtPortTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPortTagEtherType.setStatus("mandatory")


class _NbRtPortTagIpDefTag_Type(Integer32):
    """Custom type nbRtPortTagIpDefTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbRtPortTagIpDefTag_Type.__name__ = "Integer32"
_NbRtPortTagIpDefTag_Object = MibTableColumn
nbRtPortTagIpDefTag = _NbRtPortTagIpDefTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 4),
    _NbRtPortTagIpDefTag_Type()
)
nbRtPortTagIpDefTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPortTagIpDefTag.setStatus("mandatory")


class _NbRtPortTagPortDefTag_Type(Integer32):
    """Custom type nbRtPortTagPortDefTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbRtPortTagPortDefTag_Type.__name__ = "Integer32"
_NbRtPortTagPortDefTag_Object = MibTableColumn
nbRtPortTagPortDefTag = _NbRtPortTagPortDefTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 5),
    _NbRtPortTagPortDefTag_Type()
)
nbRtPortTagPortDefTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPortTagPortDefTag.setStatus("mandatory")


class _NbRtPortTagVmanDefTag_Type(Integer32):
    """Custom type nbRtPortTagVmanDefTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_NbRtPortTagVmanDefTag_Type.__name__ = "Integer32"
_NbRtPortTagVmanDefTag_Object = MibTableColumn
nbRtPortTagVmanDefTag = _NbRtPortTagVmanDefTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 6),
    _NbRtPortTagVmanDefTag_Type()
)
nbRtPortTagVmanDefTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPortTagVmanDefTag.setStatus("mandatory")
_NbRtPortTagNumberOfTags_Type = Integer32
_NbRtPortTagNumberOfTags_Object = MibTableColumn
nbRtPortTagNumberOfTags = _NbRtPortTagNumberOfTags_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 7),
    _NbRtPortTagNumberOfTags_Type()
)
nbRtPortTagNumberOfTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPortTagNumberOfTags.setStatus("mandatory")


class _NbRtPortTagMplsForceMode_Type(Integer32):
    """Custom type nbRtPortTagMplsForceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mplsForceTag", 2),
          ("noMplsForceTag", 3),
          ("other", 1))
    )


_NbRtPortTagMplsForceMode_Type.__name__ = "Integer32"
_NbRtPortTagMplsForceMode_Object = MibTableColumn
nbRtPortTagMplsForceMode = _NbRtPortTagMplsForceMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 8, 5, 1, 8),
    _NbRtPortTagMplsForceMode_Type()
)
nbRtPortTagMplsForceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPortTagMplsForceMode.setStatus("mandatory")
_NbRtActionLists_ObjectIdentity = ObjectIdentity
nbRtActionLists = _NbRtActionLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9)
)


class _NbRtActionListSupport_Type(Integer32):
    """Custom type nbRtActionListSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbRtActionListSupport_Type.__name__ = "Integer32"
_NbRtActionListSupport_Object = MibScalar
nbRtActionListSupport = _NbRtActionListSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 1),
    _NbRtActionListSupport_Type()
)
nbRtActionListSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtActionListSupport.setStatus("mandatory")
_NbRtActionListTable_Object = MibTable
nbRtActionListTable = _NbRtActionListTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2)
)
if mibBuilder.loadTexts:
    nbRtActionListTable.setStatus("mandatory")
_NbRtActionListEntry_Object = MibTableRow
nbRtActionListEntry = _NbRtActionListEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1)
)
nbRtActionListEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtActionListName"),
)
if mibBuilder.loadTexts:
    nbRtActionListEntry.setStatus("mandatory")
_NbRtActionListName_Type = ActionListName
_NbRtActionListName_Object = MibTableColumn
nbRtActionListName = _NbRtActionListName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1, 1),
    _NbRtActionListName_Type()
)
nbRtActionListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtActionListName.setStatus("mandatory")


class _NbRtActionListAdminStatus_Type(Integer32):
    """Custom type nbRtActionListAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbRtActionListAdminStatus_Type.__name__ = "Integer32"
_NbRtActionListAdminStatus_Object = MibTableColumn
nbRtActionListAdminStatus = _NbRtActionListAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1, 2),
    _NbRtActionListAdminStatus_Type()
)
nbRtActionListAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtActionListAdminStatus.setStatus("mandatory")


class _NbRtActionListOperStatus_Type(Integer32):
    """Custom type nbRtActionListOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_NbRtActionListOperStatus_Type.__name__ = "Integer32"
_NbRtActionListOperStatus_Object = MibTableColumn
nbRtActionListOperStatus = _NbRtActionListOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1, 3),
    _NbRtActionListOperStatus_Type()
)
nbRtActionListOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtActionListOperStatus.setStatus("mandatory")


class _NbRtActionListPoliceType_Type(Integer32):
    """Custom type nbRtActionListPoliceType based on Integer32"""
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


_NbRtActionListPoliceType_Type.__name__ = "Integer32"
_NbRtActionListPoliceType_Object = MibTableColumn
nbRtActionListPoliceType = _NbRtActionListPoliceType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1, 4),
    _NbRtActionListPoliceType_Type()
)
nbRtActionListPoliceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtActionListPoliceType.setStatus("mandatory")


class _NbRtActionListMplsType_Type(Integer32):
    """Custom type nbRtActionListMplsType based on Integer32"""
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


_NbRtActionListMplsType_Type.__name__ = "Integer32"
_NbRtActionListMplsType_Object = MibTableColumn
nbRtActionListMplsType = _NbRtActionListMplsType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 2, 1, 5),
    _NbRtActionListMplsType_Type()
)
nbRtActionListMplsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtActionListMplsType.setStatus("mandatory")
_NbRtPoliceAction_ObjectIdentity = ObjectIdentity
nbRtPoliceAction = _NbRtPoliceAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3)
)
_NbRtPoliceActionTable_Object = MibTable
nbRtPoliceActionTable = _NbRtPoliceActionTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1)
)
if mibBuilder.loadTexts:
    nbRtPoliceActionTable.setStatus("mandatory")
_NbRtPoliceActionEntry_Object = MibTableRow
nbRtPoliceActionEntry = _NbRtPoliceActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1)
)
nbRtPoliceActionEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtPoliceActionName"),
)
if mibBuilder.loadTexts:
    nbRtPoliceActionEntry.setStatus("mandatory")
_NbRtPoliceActionName_Type = ActionListName
_NbRtPoliceActionName_Object = MibTableColumn
nbRtPoliceActionName = _NbRtPoliceActionName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 1),
    _NbRtPoliceActionName_Type()
)
nbRtPoliceActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionName.setStatus("mandatory")


class _NbRtPoliceActionOperMode_Type(Integer32):
    """Custom type nbRtPoliceActionOperMode based on Integer32"""
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
        *(("coSaware", 5),
          ("noREDnoCoS", 2),
          ("other", 1),
          ("redAllnoCoS", 4),
          ("redTCPnoCoS", 3))
    )


_NbRtPoliceActionOperMode_Type.__name__ = "Integer32"
_NbRtPoliceActionOperMode_Object = MibTableColumn
nbRtPoliceActionOperMode = _NbRtPoliceActionOperMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 2),
    _NbRtPoliceActionOperMode_Type()
)
nbRtPoliceActionOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionOperMode.setStatus("mandatory")


class _NbRtPoliceActionSharingMode_Type(Integer32):
    """Custom type nbRtPoliceActionSharingMode based on Integer32"""
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


_NbRtPoliceActionSharingMode_Type.__name__ = "Integer32"
_NbRtPoliceActionSharingMode_Object = MibTableColumn
nbRtPoliceActionSharingMode = _NbRtPoliceActionSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 3),
    _NbRtPoliceActionSharingMode_Type()
)
nbRtPoliceActionSharingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionSharingMode.setStatus("mandatory")


class _NbRtPoliceActionAdminStatus_Type(Integer32):
    """Custom type nbRtPoliceActionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbRtPoliceActionAdminStatus_Type.__name__ = "Integer32"
_NbRtPoliceActionAdminStatus_Object = MibTableColumn
nbRtPoliceActionAdminStatus = _NbRtPoliceActionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 4),
    _NbRtPoliceActionAdminStatus_Type()
)
nbRtPoliceActionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionAdminStatus.setStatus("mandatory")


class _NbRtPoliceActionExceedCntAdminStatus_Type(Integer32):
    """Custom type nbRtPoliceActionExceedCntAdminStatus based on Integer32"""
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
        *(("clear", 6),
          ("disable", 3),
          ("enable", 2),
          ("other", 1),
          ("pause", 4),
          ("resume", 5))
    )


_NbRtPoliceActionExceedCntAdminStatus_Type.__name__ = "Integer32"
_NbRtPoliceActionExceedCntAdminStatus_Object = MibTableColumn
nbRtPoliceActionExceedCntAdminStatus = _NbRtPoliceActionExceedCntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 5),
    _NbRtPoliceActionExceedCntAdminStatus_Type()
)
nbRtPoliceActionExceedCntAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionExceedCntAdminStatus.setStatus("mandatory")


class _NbRtPoliceActionExceedCntOperStatus_Type(Integer32):
    """Custom type nbRtPoliceActionExceedCntOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 4),
          ("other", 1),
          ("paused", 3))
    )


_NbRtPoliceActionExceedCntOperStatus_Type.__name__ = "Integer32"
_NbRtPoliceActionExceedCntOperStatus_Object = MibTableColumn
nbRtPoliceActionExceedCntOperStatus = _NbRtPoliceActionExceedCntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 6),
    _NbRtPoliceActionExceedCntOperStatus_Type()
)
nbRtPoliceActionExceedCntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionExceedCntOperStatus.setStatus("mandatory")
_NbRtPoliceActionTotalExceedBytesCnt_Type = AccountCounter64
_NbRtPoliceActionTotalExceedBytesCnt_Object = MibTableColumn
nbRtPoliceActionTotalExceedBytesCnt = _NbRtPoliceActionTotalExceedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 7),
    _NbRtPoliceActionTotalExceedBytesCnt_Type()
)
nbRtPoliceActionTotalExceedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalExceedBytesCnt.setStatus("mandatory")
_NbRtPoliceActionTotalExceedFramesCnt_Type = AccountCounter64
_NbRtPoliceActionTotalExceedFramesCnt_Object = MibTableColumn
nbRtPoliceActionTotalExceedFramesCnt = _NbRtPoliceActionTotalExceedFramesCnt_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 8),
    _NbRtPoliceActionTotalExceedFramesCnt_Type()
)
nbRtPoliceActionTotalExceedFramesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalExceedFramesCnt.setStatus("mandatory")
_NbRtPoliceActionTotalHighExceedBytes32_Type = Counter32
_NbRtPoliceActionTotalHighExceedBytes32_Object = MibTableColumn
nbRtPoliceActionTotalHighExceedBytes32 = _NbRtPoliceActionTotalHighExceedBytes32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 9),
    _NbRtPoliceActionTotalHighExceedBytes32_Type()
)
nbRtPoliceActionTotalHighExceedBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalHighExceedBytes32.setStatus("mandatory")
_NbRtPoliceActionTotalLowExceedBytes32_Type = Counter32
_NbRtPoliceActionTotalLowExceedBytes32_Object = MibTableColumn
nbRtPoliceActionTotalLowExceedBytes32 = _NbRtPoliceActionTotalLowExceedBytes32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 10),
    _NbRtPoliceActionTotalLowExceedBytes32_Type()
)
nbRtPoliceActionTotalLowExceedBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalLowExceedBytes32.setStatus("mandatory")
_NbRtPoliceActionTotalHighExceedFrames32_Type = Counter32
_NbRtPoliceActionTotalHighExceedFrames32_Object = MibTableColumn
nbRtPoliceActionTotalHighExceedFrames32 = _NbRtPoliceActionTotalHighExceedFrames32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 11),
    _NbRtPoliceActionTotalHighExceedFrames32_Type()
)
nbRtPoliceActionTotalHighExceedFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalHighExceedFrames32.setStatus("mandatory")
_NbRtPoliceActionTotalLowExceedFrames32_Type = Counter32
_NbRtPoliceActionTotalLowExceedFrames32_Object = MibTableColumn
nbRtPoliceActionTotalLowExceedFrames32 = _NbRtPoliceActionTotalLowExceedFrames32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 1, 1, 12),
    _NbRtPoliceActionTotalLowExceedFrames32_Type()
)
nbRtPoliceActionTotalLowExceedFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionTotalLowExceedFrames32.setStatus("mandatory")
_NbRtPoliceRateLimitTable_Object = MibTable
nbRtPoliceRateLimitTable = _NbRtPoliceRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2)
)
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitTable.setStatus("mandatory")
_NbRtPoliceRateLimitEntry_Object = MibTableRow
nbRtPoliceRateLimitEntry = _NbRtPoliceRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1)
)
nbRtPoliceRateLimitEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbRtPoliceRateLimitName"),
    (0, "RT-CFG-MIB", "nbRtPoliceRateLimitCoSlevel"),
)
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitEntry.setStatus("mandatory")
_NbRtPoliceRateLimitName_Type = ActionListName
_NbRtPoliceRateLimitName_Object = MibTableColumn
nbRtPoliceRateLimitName = _NbRtPoliceRateLimitName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 1),
    _NbRtPoliceRateLimitName_Type()
)
nbRtPoliceRateLimitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitName.setStatus("mandatory")
_NbRtPoliceRateLimitCoSlevel_Type = Integer32
_NbRtPoliceRateLimitCoSlevel_Object = MibTableColumn
nbRtPoliceRateLimitCoSlevel = _NbRtPoliceRateLimitCoSlevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 2),
    _NbRtPoliceRateLimitCoSlevel_Type()
)
nbRtPoliceRateLimitCoSlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitCoSlevel.setStatus("mandatory")
_NbRtPoliceRateLimitBuckRate_Type = Integer32
_NbRtPoliceRateLimitBuckRate_Object = MibTableColumn
nbRtPoliceRateLimitBuckRate = _NbRtPoliceRateLimitBuckRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 3),
    _NbRtPoliceRateLimitBuckRate_Type()
)
nbRtPoliceRateLimitBuckRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitBuckRate.setStatus("mandatory")
_NbRtPoliceRateLimitBuckSize_Type = Integer32
_NbRtPoliceRateLimitBuckSize_Object = MibTableColumn
nbRtPoliceRateLimitBuckSize = _NbRtPoliceRateLimitBuckSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 4),
    _NbRtPoliceRateLimitBuckSize_Type()
)
nbRtPoliceRateLimitBuckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitBuckSize.setStatus("mandatory")


class _NbRtPoliceRateLimitOperMode_Type(Integer32):
    """Custom type nbRtPoliceRateLimitOperMode based on Integer32"""
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
        *(("coSREDall", 8),
          ("coSREDtcp", 7),
          ("coSguarantee", 6),
          ("coSguaranteeREDall", 10),
          ("coSguaranteeREDtcp", 9),
          ("coSnoRED", 5),
          ("noREDnoCoS", 2),
          ("other", 1),
          ("redAllnoCoS", 4),
          ("redTCPnoCoS", 3))
    )


_NbRtPoliceRateLimitOperMode_Type.__name__ = "Integer32"
_NbRtPoliceRateLimitOperMode_Object = MibTableColumn
nbRtPoliceRateLimitOperMode = _NbRtPoliceRateLimitOperMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 5),
    _NbRtPoliceRateLimitOperMode_Type()
)
nbRtPoliceRateLimitOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitOperMode.setStatus("mandatory")
_NbRtPoliceRateLimitExceedBytesCnt_Type = AccountCounter64
_NbRtPoliceRateLimitExceedBytesCnt_Object = MibTableColumn
nbRtPoliceRateLimitExceedBytesCnt = _NbRtPoliceRateLimitExceedBytesCnt_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 6),
    _NbRtPoliceRateLimitExceedBytesCnt_Type()
)
nbRtPoliceRateLimitExceedBytesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitExceedBytesCnt.setStatus("mandatory")
_NbRtPoliceRateLimitExceedFramesCnt_Type = AccountCounter64
_NbRtPoliceRateLimitExceedFramesCnt_Object = MibTableColumn
nbRtPoliceRateLimitExceedFramesCnt = _NbRtPoliceRateLimitExceedFramesCnt_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 7),
    _NbRtPoliceRateLimitExceedFramesCnt_Type()
)
nbRtPoliceRateLimitExceedFramesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitExceedFramesCnt.setStatus("mandatory")
_NbRtPoliceRateLimitHighExceedBytes32_Type = Counter32
_NbRtPoliceRateLimitHighExceedBytes32_Object = MibTableColumn
nbRtPoliceRateLimitHighExceedBytes32 = _NbRtPoliceRateLimitHighExceedBytes32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 8),
    _NbRtPoliceRateLimitHighExceedBytes32_Type()
)
nbRtPoliceRateLimitHighExceedBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitHighExceedBytes32.setStatus("mandatory")
_NbRtPoliceRateLimitLowExceedBytes32_Type = Counter32
_NbRtPoliceRateLimitLowExceedBytes32_Object = MibTableColumn
nbRtPoliceRateLimitLowExceedBytes32 = _NbRtPoliceRateLimitLowExceedBytes32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 9),
    _NbRtPoliceRateLimitLowExceedBytes32_Type()
)
nbRtPoliceRateLimitLowExceedBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitLowExceedBytes32.setStatus("mandatory")
_NbRtPoliceRateLimitHighExceedFrames32_Type = Counter32
_NbRtPoliceRateLimitHighExceedFrames32_Object = MibTableColumn
nbRtPoliceRateLimitHighExceedFrames32 = _NbRtPoliceRateLimitHighExceedFrames32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 10),
    _NbRtPoliceRateLimitHighExceedFrames32_Type()
)
nbRtPoliceRateLimitHighExceedFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitHighExceedFrames32.setStatus("mandatory")
_NbRtPoliceRateLimitLowExceedFrames32_Type = Counter32
_NbRtPoliceRateLimitLowExceedFrames32_Object = MibTableColumn
nbRtPoliceRateLimitLowExceedFrames32 = _NbRtPoliceRateLimitLowExceedFrames32_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 3, 2, 1, 11),
    _NbRtPoliceRateLimitLowExceedFrames32_Type()
)
nbRtPoliceRateLimitLowExceedFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceRateLimitLowExceedFrames32.setStatus("mandatory")
_NbRtPoliceActionVifTable_Object = MibTable
nbRtPoliceActionVifTable = _NbRtPoliceActionVifTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4)
)
if mibBuilder.loadTexts:
    nbRtPoliceActionVifTable.setStatus("mandatory")
_NbRtPoliceActionVifEntry_Object = MibTableRow
nbRtPoliceActionVifEntry = _NbRtPoliceActionVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4, 1)
)
nbRtPoliceActionVifEntry.setIndexNames(
    (0, "RT-CFG-MIB", "nbVifType"),
    (0, "RT-CFG-MIB", "nbVifDevNo"),
    (0, "RT-CFG-MIB", "nbVifIsAlias"),
    (0, "RT-CFG-MIB", "nbVifAliasDev"),
    (0, "RT-CFG-MIB", "nbRtPoliceActionVifDirection"),
    (0, "RT-CFG-MIB", "nbRtPoliceActionVifName"),
)
if mibBuilder.loadTexts:
    nbRtPoliceActionVifEntry.setStatus("mandatory")
_NbRtPoliceActionVifDirection_Type = DirectionType
_NbRtPoliceActionVifDirection_Object = MibTableColumn
nbRtPoliceActionVifDirection = _NbRtPoliceActionVifDirection_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4, 1, 1),
    _NbRtPoliceActionVifDirection_Type()
)
nbRtPoliceActionVifDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionVifDirection.setStatus("mandatory")
_NbRtPoliceActionVifName_Type = ActionListName
_NbRtPoliceActionVifName_Object = MibTableColumn
nbRtPoliceActionVifName = _NbRtPoliceActionVifName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4, 1, 2),
    _NbRtPoliceActionVifName_Type()
)
nbRtPoliceActionVifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbRtPoliceActionVifName.setStatus("mandatory")
_NbRtPoliceActionVifPortList_Type = OctetString
_NbRtPoliceActionVifPortList_Object = MibTableColumn
nbRtPoliceActionVifPortList = _NbRtPoliceActionVifPortList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4, 1, 3),
    _NbRtPoliceActionVifPortList_Type()
)
nbRtPoliceActionVifPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionVifPortList.setStatus("mandatory")


class _NbRtPoliceActionVifBindingStatus_Type(Integer32):
    """Custom type nbRtPoliceActionVifBindingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addNewBind", 1),
          ("editExistingBind", 3),
          ("unbind", 2))
    )


_NbRtPoliceActionVifBindingStatus_Type.__name__ = "Integer32"
_NbRtPoliceActionVifBindingStatus_Object = MibTableColumn
nbRtPoliceActionVifBindingStatus = _NbRtPoliceActionVifBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 4, 1, 4),
    _NbRtPoliceActionVifBindingStatus_Type()
)
nbRtPoliceActionVifBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbRtPoliceActionVifBindingStatus.setStatus("mandatory")
_NbRtMplsAction_ObjectIdentity = ObjectIdentity
nbRtMplsAction = _NbRtMplsAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 5)
)

# Managed Objects groups


# Notification objects

nbVifModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 0, 11)
)
nbVifModify.setObjects(
      *(("RT-CFG-MIB", "nbVifDevName"),
        ("RT-CFG-MIB", "nbVifAdminStatus"),
        ("RT-CFG-MIB", "nbVifPhysType"),
        ("RT-CFG-MIB", "nbVifProtocol"),
        ("RT-CFG-MIB", "nbVifState"),
        ("RT-CFG-MIB", "nbVifName"),
        ("RT-CFG-MIB", "nbVifIpAddress"),
        ("RT-CFG-MIB", "nbVifMask"),
        ("RT-CFG-MIB", "nbVifPortList"),
        ("RT-CFG-MIB", "nbVifMac"),
        ("RT-CFG-MIB", "nbVifPeer"),
        ("RT-CFG-MIB", "nbVifConfigType"),
        ("RT-CFG-MIB", "nbVifSecurity"))
)
if mibBuilder.loadTexts:
    nbVifModify.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RT-CFG-MIB",
    **{"MacAddress": MacAddress,
       "ActionListName": ActionListName,
       "DirectionType": DirectionType,
       "AccountCouter": AccountCouter,
       "AccountCounter64": AccountCounter64,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbRouterConfig": nbRouterConfig,
       "nbVifModify": nbVifModify,
       "nbRtConfigGen": nbRtConfigGen,
       "nbRtDevDiffServMode": nbRtDevDiffServMode,
       "nbRtDevDiffServMappingSupport": nbRtDevDiffServMappingSupport,
       "nbRtVifTable": nbRtVifTable,
       "nbRtVifEntry": nbRtVifEntry,
       "nbRtVifId": nbRtVifId,
       "nbRtVifIpAddress": nbRtVifIpAddress,
       "nbRtVifMask": nbRtVifMask,
       "nbRtVifProtocol": nbRtVifProtocol,
       "nbRtVifName": nbRtVifName,
       "nbRtVifPortList": nbRtVifPortList,
       "nbRtVifMac": nbRtVifMac,
       "nbRtVifAdminStatus": nbRtVifAdminStatus,
       "nbRtVifConfigType": nbRtVifConfigType,
       "nbRtVifSecurity": nbRtVifSecurity,
       "nbRtVifIsTagged": nbRtVifIsTagged,
       "nbRtVifTag": nbRtVifTag,
       "nbRtVifGroup": nbRtVifGroup,
       "nbVifTableSize": nbVifTableSize,
       "nbVifDeviceLimitTable": nbVifDeviceLimitTable,
       "nbVifDeviceLimitEntry": nbVifDeviceLimitEntry,
       "nbVifLimitType": nbVifLimitType,
       "nbVifDevNoMin": nbVifDevNoMin,
       "nbVifDevNoMax": nbVifDevNoMax,
       "nbVifDevNoFirstEmpty": nbVifDevNoFirstEmpty,
       "nbVifAliasDLimitTable": nbVifAliasDLimitTable,
       "nbVifAliasDLimitEntry": nbVifAliasDLimitEntry,
       "nbVifAliasLimitType": nbVifAliasLimitType,
       "nbVifAliasLimitDevNo": nbVifAliasLimitDevNo,
       "nbVifAliasLimitDevAliasMin": nbVifAliasLimitDevAliasMin,
       "nbVifAliasLimitDevAliasMax": nbVifAliasLimitDevAliasMax,
       "nbVifAliasLimitDevAliasFirstEmpty": nbVifAliasLimitDevAliasFirstEmpty,
       "nbVifTable": nbVifTable,
       "nbVifEntry": nbVifEntry,
       "nbVifType": nbVifType,
       "nbVifDevNo": nbVifDevNo,
       "nbVifIsAlias": nbVifIsAlias,
       "nbVifAliasDev": nbVifAliasDev,
       "nbVifDevName": nbVifDevName,
       "nbVifIpAddress": nbVifIpAddress,
       "nbVifMask": nbVifMask,
       "nbVifPeer": nbVifPeer,
       "nbVifPhysType": nbVifPhysType,
       "nbVifProtocol": nbVifProtocol,
       "nbVifName": nbVifName,
       "nbVifPortList": nbVifPortList,
       "nbVifMac": nbVifMac,
       "nbVifState": nbVifState,
       "nbVifAdminStatus": nbVifAdminStatus,
       "nbVifConfigType": nbVifConfigType,
       "nbVifSecurity": nbVifSecurity,
       "nbVifIsTagged": nbVifIsTagged,
       "nbVifTag": nbVifTag,
       "nbVifDescr": nbVifDescr,
       "nbVifLastChange": nbVifLastChange,
       "nbVifL2SwitchingMode": nbVifL2SwitchingMode,
       "nbVifProxyArpMode": nbVifProxyArpMode,
       "nbVifIpOnlyMode": nbVifIpOnlyMode,
       "nbVifIpForwardingMode": nbVifIpForwardingMode,
       "nbRtFib": nbRtFib,
       "nbRtFibNumEntries": nbRtFibNumEntries,
       "nbRtFibTable": nbRtFibTable,
       "nbRtFibEntry": nbRtFibEntry,
       "nbRtFibEntryIpAddress": nbRtFibEntryIpAddress,
       "nbRtFibEntryIpMask": nbRtFibEntryIpMask,
       "nbRtFibEntryProtocol": nbRtFibEntryProtocol,
       "nbRtFibEntryNextHop": nbRtFibEntryNextHop,
       "nbRtFibEntryNextPhysAddress": nbRtFibEntryNextPhysAddress,
       "nbRtFibEntryNextPort": nbRtFibEntryNextPort,
       "nbRtFibEntryLastChTime": nbRtFibEntryLastChTime,
       "nbRtFibEntryAge": nbRtFibEntryAge,
       "nbRtFibEntryMetric": nbRtFibEntryMetric,
       "nbRtFibEntryAdminStatus": nbRtFibEntryAdminStatus,
       "nbRtFibEntryTag": nbRtFibEntryTag,
       "nbRtDiffServ": nbRtDiffServ,
       "nbRtDiffServTable": nbRtDiffServTable,
       "nbRtDiffServEntry": nbRtDiffServEntry,
       "nbRtDiffServMode": nbRtDiffServMode,
       "nbRtDiffServVptMapNameIndex": nbRtDiffServVptMapNameIndex,
       "nbRtDiffServDscpMapNameIndex": nbRtDiffServDscpMapNameIndex,
       "nbRtDiffServMgmtVptMapNameIndex": nbRtDiffServMgmtVptMapNameIndex,
       "nbRtDiffServMgmtDscpMapNameIndex": nbRtDiffServMgmtDscpMapNameIndex,
       "nbRtVifDiffServRateLimitTable": nbRtVifDiffServRateLimitTable,
       "nbRtVifDiffServRateLimitEntry": nbRtVifDiffServRateLimitEntry,
       "nbRtVifDiffServDirect": nbRtVifDiffServDirect,
       "nbRtVifDiffServBuckRate": nbRtVifDiffServBuckRate,
       "nbRtVifDiffServBuckSize": nbRtVifDiffServBuckSize,
       "nbRtVifDiffServREDmode": nbRtVifDiffServREDmode,
       "nbRtVifDiffServAdminStatus": nbRtVifDiffServAdminStatus,
       "nbRtDiffServVptMapTable": nbRtDiffServVptMapTable,
       "nbRtDiffServVptMapEntry": nbRtDiffServVptMapEntry,
       "nbRtDiffServVptMapNameId": nbRtDiffServVptMapNameId,
       "nbRtDiffServVptMapName": nbRtDiffServVptMapName,
       "nbRtDiffServVptMapStatus": nbRtDiffServVptMapStatus,
       "nbRtDiffServVptMapAdminStatus": nbRtDiffServVptMapAdminStatus,
       "nbRtDiffServVptMapPrflTable": nbRtDiffServVptMapPrflTable,
       "nbRtDiffServVptMapPrflEntry": nbRtDiffServVptMapPrflEntry,
       "nbRtDiffServVptMapPrflNameId": nbRtDiffServVptMapPrflNameId,
       "nbRtDiffServVptMapPrflInValueId": nbRtDiffServVptMapPrflInValueId,
       "nbRtDiffServVptMapPrflInValue": nbRtDiffServVptMapPrflInValue,
       "nbRtDiffServVptMapPrflSl": nbRtDiffServVptMapPrflSl,
       "nbRtDiffServVptMapPrflOutValue": nbRtDiffServVptMapPrflOutValue,
       "nbRtDiffServDscpMapTable": nbRtDiffServDscpMapTable,
       "nbRtDiffServDscpMapEntry": nbRtDiffServDscpMapEntry,
       "nbRtDiffServDscpMapNameId": nbRtDiffServDscpMapNameId,
       "nbRtDiffServDscpMapName": nbRtDiffServDscpMapName,
       "nbRtDiffServDscpMapStatus": nbRtDiffServDscpMapStatus,
       "nbRtDiffServDscpMapAdminStatus": nbRtDiffServDscpMapAdminStatus,
       "nbRtDiffServDscpMapPrflTable": nbRtDiffServDscpMapPrflTable,
       "nbRtDiffServDscpMapPrflEntry": nbRtDiffServDscpMapPrflEntry,
       "nbRtDiffServDscpMapPrflNameId": nbRtDiffServDscpMapPrflNameId,
       "nbRtDiffServDscpMapPrflInValueId": nbRtDiffServDscpMapPrflInValueId,
       "nbRtDiffServDscpMapPrflInValue": nbRtDiffServDscpMapPrflInValue,
       "nbRtDiffServDscpMapPrflSl": nbRtDiffServDscpMapPrflSl,
       "nbRtDiffServDscpMapPrflOutValue": nbRtDiffServDscpMapPrflOutValue,
       "nbRtAccounting": nbRtAccounting,
       "nbRtAccVifTable": nbRtAccVifTable,
       "nbRtAccVifEntry": nbRtAccVifEntry,
       "nbRtAccVifDirection": nbRtAccVifDirection,
       "nbRtAccVifAdminStatus": nbRtAccVifAdminStatus,
       "nbRtAccVifOperStatus": nbRtAccVifOperStatus,
       "nbRtAccVifConformingBytes": nbRtAccVifConformingBytes,
       "nbRtAccVifExceedingBytes": nbRtAccVifExceedingBytes,
       "nbRtAccVifConformingPackets": nbRtAccVifConformingPackets,
       "nbRtAccVifExceedingPackets": nbRtAccVifExceedingPackets,
       "nbRtAccVifHighConformingBytes": nbRtAccVifHighConformingBytes,
       "nbRtAccVifHighExceedingBytes": nbRtAccVifHighExceedingBytes,
       "nbRtAccVifHighConformingPackets": nbRtAccVifHighConformingPackets,
       "nbRtAccVifHighExceedingPackets": nbRtAccVifHighExceedingPackets,
       "nbRtAccVifLowConformingBytes": nbRtAccVifLowConformingBytes,
       "nbRtAccVifLowExceedingBytes": nbRtAccVifLowExceedingBytes,
       "nbRtAccVifLowConformingPackets": nbRtAccVifLowConformingPackets,
       "nbRtAccVifLowExceedingPackets": nbRtAccVifLowExceedingPackets,
       "nbRtAccVif64ConformingBytes": nbRtAccVif64ConformingBytes,
       "nbRtAccVif64ExceedingBytes": nbRtAccVif64ExceedingBytes,
       "nbRtAccVifConformingUcastPackets": nbRtAccVifConformingUcastPackets,
       "nbRtAccVifHighConformingUcastPackets": nbRtAccVifHighConformingUcastPackets,
       "nbRtAccVifLowConformingUcastPackets": nbRtAccVifLowConformingUcastPackets,
       "nbRtAccVif64ConformingUcastPackets": nbRtAccVif64ConformingUcastPackets,
       "nbRtAccVifConformingMcastPackets": nbRtAccVifConformingMcastPackets,
       "nbRtAccVifHighConformingMcastPackets": nbRtAccVifHighConformingMcastPackets,
       "nbRtAccVifLowConformingMcastPackets": nbRtAccVifLowConformingMcastPackets,
       "nbRtAccVif64ConformingMcastPackets": nbRtAccVif64ConformingMcastPackets,
       "nbRtAccVifConformingBcastPackets": nbRtAccVifConformingBcastPackets,
       "nbRtAccVifHighConformingBcastPackets": nbRtAccVifHighConformingBcastPackets,
       "nbRtAccVifLowConformingBcastPackets": nbRtAccVifLowConformingBcastPackets,
       "nbRtAccVif64ConformingBcastPackets": nbRtAccVif64ConformingBcastPackets,
       "nbRtAccVifPortTable": nbRtAccVifPortTable,
       "nbRtAccVifPortEntry": nbRtAccVifPortEntry,
       "nbRtVifPortId": nbRtVifPortId,
       "nbRtAccPortAdminStatus": nbRtAccPortAdminStatus,
       "nbRtAccPortOperStatus": nbRtAccPortOperStatus,
       "nbRtAccPortConformingBytes": nbRtAccPortConformingBytes,
       "nbRtAccPortExceedingBytes": nbRtAccPortExceedingBytes,
       "nbRtAccPortConformingPackets": nbRtAccPortConformingPackets,
       "nbRtAccPortExceedingPackets": nbRtAccPortExceedingPackets,
       "nbRtAccPortHighConformingBytes": nbRtAccPortHighConformingBytes,
       "nbRtAccPortHighExceedingBytes": nbRtAccPortHighExceedingBytes,
       "nbRtAccPortHighConformingPackets": nbRtAccPortHighConformingPackets,
       "nbRtAccPortHighExceedingPackets": nbRtAccPortHighExceedingPackets,
       "nbRtAccPortLowConformingBytes": nbRtAccPortLowConformingBytes,
       "nbRtAccPortLowExceedingBytes": nbRtAccPortLowExceedingBytes,
       "nbRtAccPortLowConformingPackets": nbRtAccPortLowConformingPackets,
       "nbRtAccPortLowExceedingPackets": nbRtAccPortLowExceedingPackets,
       "nbRtAccPortVif64ConformingBytes": nbRtAccPortVif64ConformingBytes,
       "nbRtAccPortVif64ExceedingBytes": nbRtAccPortVif64ExceedingBytes,
       "nbRtAccPortConformingUcastPackets": nbRtAccPortConformingUcastPackets,
       "nbRtAccPortHighConformingUcastPackets": nbRtAccPortHighConformingUcastPackets,
       "nbRtAccPortLowConformingUcastPackets": nbRtAccPortLowConformingUcastPackets,
       "nbRtAccPort64ConformingUcastPackets": nbRtAccPort64ConformingUcastPackets,
       "nbRtAccPortConformingMcastPackets": nbRtAccPortConformingMcastPackets,
       "nbRtAccPortHighConformingMcastPackets": nbRtAccPortHighConformingMcastPackets,
       "nbRtAccPortLowConformingMcastPackets": nbRtAccPortLowConformingMcastPackets,
       "nbRtAccPort64ConformingMcastPackets": nbRtAccPort64ConformingMcastPackets,
       "nbRtAccPortConformingBcastPackets": nbRtAccPortConformingBcastPackets,
       "nbRtAccPortHighConformingBcastPackets": nbRtAccPortHighConformingBcastPackets,
       "nbRtAccPortLowConformingBcastPackets": nbRtAccPortLowConformingBcastPackets,
       "nbRtAccPort64ConformingBcastPackets": nbRtAccPort64ConformingBcastPackets,
       "nbRtAccessLists": nbRtAccessLists,
       "nbAclVifTable": nbAclVifTable,
       "nbAclVifEntry": nbAclVifEntry,
       "nbAclVifDirection": nbAclVifDirection,
       "nbAclVifId": nbAclVifId,
       "nbAclVifAccessListName": nbAclVifAccessListName,
       "nbAclVifBindingStatus": nbAclVifBindingStatus,
       "nbRtPortTagGroup": nbRtPortTagGroup,
       "nbRtPortTagTable": nbRtPortTagTable,
       "nbRtPortTagEntry": nbRtPortTagEntry,
       "nbRtPortTagId": nbRtPortTagId,
       "nbRtPortTagAwareMode": nbRtPortTagAwareMode,
       "nbRtPortTagEtherType": nbRtPortTagEtherType,
       "nbRtPortTagIpDefTag": nbRtPortTagIpDefTag,
       "nbRtPortTagPortDefTag": nbRtPortTagPortDefTag,
       "nbRtPortTagVmanDefTag": nbRtPortTagVmanDefTag,
       "nbRtPortTagNumberOfTags": nbRtPortTagNumberOfTags,
       "nbRtPortTagMplsForceMode": nbRtPortTagMplsForceMode,
       "nbRtActionLists": nbRtActionLists,
       "nbRtActionListSupport": nbRtActionListSupport,
       "nbRtActionListTable": nbRtActionListTable,
       "nbRtActionListEntry": nbRtActionListEntry,
       "nbRtActionListName": nbRtActionListName,
       "nbRtActionListAdminStatus": nbRtActionListAdminStatus,
       "nbRtActionListOperStatus": nbRtActionListOperStatus,
       "nbRtActionListPoliceType": nbRtActionListPoliceType,
       "nbRtActionListMplsType": nbRtActionListMplsType,
       "nbRtPoliceAction": nbRtPoliceAction,
       "nbRtPoliceActionTable": nbRtPoliceActionTable,
       "nbRtPoliceActionEntry": nbRtPoliceActionEntry,
       "nbRtPoliceActionName": nbRtPoliceActionName,
       "nbRtPoliceActionOperMode": nbRtPoliceActionOperMode,
       "nbRtPoliceActionSharingMode": nbRtPoliceActionSharingMode,
       "nbRtPoliceActionAdminStatus": nbRtPoliceActionAdminStatus,
       "nbRtPoliceActionExceedCntAdminStatus": nbRtPoliceActionExceedCntAdminStatus,
       "nbRtPoliceActionExceedCntOperStatus": nbRtPoliceActionExceedCntOperStatus,
       "nbRtPoliceActionTotalExceedBytesCnt": nbRtPoliceActionTotalExceedBytesCnt,
       "nbRtPoliceActionTotalExceedFramesCnt": nbRtPoliceActionTotalExceedFramesCnt,
       "nbRtPoliceActionTotalHighExceedBytes32": nbRtPoliceActionTotalHighExceedBytes32,
       "nbRtPoliceActionTotalLowExceedBytes32": nbRtPoliceActionTotalLowExceedBytes32,
       "nbRtPoliceActionTotalHighExceedFrames32": nbRtPoliceActionTotalHighExceedFrames32,
       "nbRtPoliceActionTotalLowExceedFrames32": nbRtPoliceActionTotalLowExceedFrames32,
       "nbRtPoliceRateLimitTable": nbRtPoliceRateLimitTable,
       "nbRtPoliceRateLimitEntry": nbRtPoliceRateLimitEntry,
       "nbRtPoliceRateLimitName": nbRtPoliceRateLimitName,
       "nbRtPoliceRateLimitCoSlevel": nbRtPoliceRateLimitCoSlevel,
       "nbRtPoliceRateLimitBuckRate": nbRtPoliceRateLimitBuckRate,
       "nbRtPoliceRateLimitBuckSize": nbRtPoliceRateLimitBuckSize,
       "nbRtPoliceRateLimitOperMode": nbRtPoliceRateLimitOperMode,
       "nbRtPoliceRateLimitExceedBytesCnt": nbRtPoliceRateLimitExceedBytesCnt,
       "nbRtPoliceRateLimitExceedFramesCnt": nbRtPoliceRateLimitExceedFramesCnt,
       "nbRtPoliceRateLimitHighExceedBytes32": nbRtPoliceRateLimitHighExceedBytes32,
       "nbRtPoliceRateLimitLowExceedBytes32": nbRtPoliceRateLimitLowExceedBytes32,
       "nbRtPoliceRateLimitHighExceedFrames32": nbRtPoliceRateLimitHighExceedFrames32,
       "nbRtPoliceRateLimitLowExceedFrames32": nbRtPoliceRateLimitLowExceedFrames32,
       "nbRtPoliceActionVifTable": nbRtPoliceActionVifTable,
       "nbRtPoliceActionVifEntry": nbRtPoliceActionVifEntry,
       "nbRtPoliceActionVifDirection": nbRtPoliceActionVifDirection,
       "nbRtPoliceActionVifName": nbRtPoliceActionVifName,
       "nbRtPoliceActionVifPortList": nbRtPoliceActionVifPortList,
       "nbRtPoliceActionVifBindingStatus": nbRtPoliceActionVifBindingStatus,
       "nbRtMplsAction": nbRtMplsAction}
)
