# SNMP MIB module (HH3C-HPEOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-HPEOC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:07 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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


# MODULE-IDENTITY

hh3cHPEOC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cHPEOCSystem_ObjectIdentity = ObjectIdentity
hh3cHPEOCSystem = _Hh3cHPEOCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1)
)


class _Hh3cHPEOCCltVlanType_Type(Integer32):
    """Custom type hh3cHPEOCCltVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021q", 1),
          ("portbased", 2))
    )


_Hh3cHPEOCCltVlanType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltVlanType_Object = MibScalar
hh3cHPEOCCltVlanType = _Hh3cHPEOCCltVlanType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 1),
    _Hh3cHPEOCCltVlanType_Type()
)
hh3cHPEOCCltVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanType.setStatus("current")
_Hh3cHPEOCCltVlanManTable_Object = MibTable
hh3cHPEOCCltVlanManTable = _Hh3cHPEOCCltVlanManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanManTable.setStatus("current")
_Hh3cHPEOCCltVlanManEntry_Object = MibTableRow
hh3cHPEOCCltVlanManEntry = _Hh3cHPEOCCltVlanManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2, 1)
)
hh3cHPEOCCltVlanManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanManEntry.setStatus("current")


class _Hh3cHPEOCCltEthPortType_Type(Integer32):
    """Custom type hh3cHPEOCCltEthPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debug", 2),
          ("normal", 1))
    )


_Hh3cHPEOCCltEthPortType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltEthPortType_Object = MibTableColumn
hh3cHPEOCCltEthPortType = _Hh3cHPEOCCltEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2, 1, 1),
    _Hh3cHPEOCCltEthPortType_Type()
)
hh3cHPEOCCltEthPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltEthPortType.setStatus("current")
_Hh3cHPEOCCltSysManTable_Object = MibTable
hh3cHPEOCCltSysManTable = _Hh3cHPEOCCltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltSysManTable.setStatus("current")
_Hh3cHPEOCCltSysManEntry_Object = MibTableRow
hh3cHPEOCCltSysManEntry = _Hh3cHPEOCCltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1)
)
hh3cHPEOCCltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltSysManEntry.setStatus("current")


class _Hh3cHPEOCCltDescr_Type(DisplayString):
    """Custom type hh3cHPEOCCltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Hh3cHPEOCCltDescr_Type.__name__ = "DisplayString"
_Hh3cHPEOCCltDescr_Object = MibTableColumn
hh3cHPEOCCltDescr = _Hh3cHPEOCCltDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1, 1),
    _Hh3cHPEOCCltDescr_Type()
)
hh3cHPEOCCltDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltDescr.setStatus("current")
_Hh3cHPEOCCltFwVersion_Type = DisplayString
_Hh3cHPEOCCltFwVersion_Object = MibTableColumn
hh3cHPEOCCltFwVersion = _Hh3cHPEOCCltFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1, 2),
    _Hh3cHPEOCCltFwVersion_Type()
)
hh3cHPEOCCltFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCltFwVersion.setStatus("current")
_Hh3cHPEOCCnuSysManTable_Object = MibTable
hh3cHPEOCCnuSysManTable = _Hh3cHPEOCCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuSysManTable.setStatus("current")
_Hh3cHPEOCCnuSysManEntry_Object = MibTableRow
hh3cHPEOCCnuSysManEntry = _Hh3cHPEOCCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1)
)
hh3cHPEOCCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuSysManEntry.setStatus("current")
_Hh3cHPEOCCnuBcastControl_Type = TruthValue
_Hh3cHPEOCCnuBcastControl_Object = MibTableColumn
hh3cHPEOCCnuBcastControl = _Hh3cHPEOCCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 1),
    _Hh3cHPEOCCnuBcastControl_Type()
)
hh3cHPEOCCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuBcastControl.setStatus("current")
_Hh3cHPEOCCnuAnonymStatus_Type = TruthValue
_Hh3cHPEOCCnuAnonymStatus_Object = MibTableColumn
hh3cHPEOCCnuAnonymStatus = _Hh3cHPEOCCnuAnonymStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 2),
    _Hh3cHPEOCCnuAnonymStatus_Type()
)
hh3cHPEOCCnuAnonymStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAnonymStatus.setStatus("current")
_Hh3cHPEOCCnuMacLimit_Type = Unsigned32
_Hh3cHPEOCCnuMacLimit_Object = MibTableColumn
hh3cHPEOCCnuMacLimit = _Hh3cHPEOCCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 3),
    _Hh3cHPEOCCnuMacLimit_Type()
)
hh3cHPEOCCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuMacLimit.setStatus("current")


class _Hh3cHPEOCCltAutoUpgrade_Type(TruthValue):
    """Custom type hh3cHPEOCCltAutoUpgrade based on TruthValue"""


_Hh3cHPEOCCltAutoUpgrade_Object = MibScalar
hh3cHPEOCCltAutoUpgrade = _Hh3cHPEOCCltAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 5),
    _Hh3cHPEOCCltAutoUpgrade_Type()
)
hh3cHPEOCCltAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltAutoUpgrade.setStatus("current")
_Hh3cHPEOCOnLineCnuNumber_Type = Integer32
_Hh3cHPEOCOnLineCnuNumber_Object = MibScalar
hh3cHPEOCOnLineCnuNumber = _Hh3cHPEOCOnLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 6),
    _Hh3cHPEOCOnLineCnuNumber_Type()
)
hh3cHPEOCOnLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOnLineCnuNumber.setStatus("current")
_Hh3cHPEOCCpuMacAddress_Type = MacAddress
_Hh3cHPEOCCpuMacAddress_Object = MibScalar
hh3cHPEOCCpuMacAddress = _Hh3cHPEOCCpuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 7),
    _Hh3cHPEOCCpuMacAddress_Type()
)
hh3cHPEOCCpuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCpuMacAddress.setStatus("current")
_Hh3cHPEOCOffLineCnuNumber_Type = Integer32
_Hh3cHPEOCOffLineCnuNumber_Object = MibScalar
hh3cHPEOCOffLineCnuNumber = _Hh3cHPEOCOffLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 8),
    _Hh3cHPEOCOffLineCnuNumber_Type()
)
hh3cHPEOCOffLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOffLineCnuNumber.setStatus("current")
_Hh3cHPEOCDownLoadCNUFWResult_Type = DisplayString
_Hh3cHPEOCDownLoadCNUFWResult_Object = MibScalar
hh3cHPEOCDownLoadCNUFWResult = _Hh3cHPEOCDownLoadCNUFWResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 9),
    _Hh3cHPEOCDownLoadCNUFWResult_Type()
)
hh3cHPEOCDownLoadCNUFWResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cHPEOCDownLoadCNUFWResult.setStatus("current")


class _Hh3cHPEOCCltAutoUpgradeType_Type(Integer32):
    """Custom type hh3cHPEOCCltAutoUpgradeType based on Integer32"""
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
          ("ftp", 2),
          ("tftp", 3))
    )


_Hh3cHPEOCCltAutoUpgradeType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltAutoUpgradeType_Object = MibScalar
hh3cHPEOCCltAutoUpgradeType = _Hh3cHPEOCCltAutoUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 10),
    _Hh3cHPEOCCltAutoUpgradeType_Type()
)
hh3cHPEOCCltAutoUpgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltAutoUpgradeType.setStatus("current")
_Hh3cHPEOCAutoUpObjects_ObjectIdentity = ObjectIdentity
hh3cHPEOCAutoUpObjects = _Hh3cHPEOCAutoUpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11)
)
_Hh3cHPEOCServerAddress_Type = IpAddress
_Hh3cHPEOCServerAddress_Object = MibScalar
hh3cHPEOCServerAddress = _Hh3cHPEOCServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 1),
    _Hh3cHPEOCServerAddress_Type()
)
hh3cHPEOCServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerAddress.setStatus("current")
_Hh3cHPEOCServerUser_Type = DisplayString
_Hh3cHPEOCServerUser_Object = MibScalar
hh3cHPEOCServerUser = _Hh3cHPEOCServerUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 2),
    _Hh3cHPEOCServerUser_Type()
)
hh3cHPEOCServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerUser.setStatus("current")
_Hh3cHPEOCServerPassword_Type = DisplayString
_Hh3cHPEOCServerPassword_Object = MibScalar
hh3cHPEOCServerPassword = _Hh3cHPEOCServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 3),
    _Hh3cHPEOCServerPassword_Type()
)
hh3cHPEOCServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerPassword.setStatus("current")
_Hh3cHPEOCCableInfo_ObjectIdentity = ObjectIdentity
hh3cHPEOCCableInfo = _Hh3cHPEOCCableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2)
)
_Hh3cHPEOCCableInfoTable_Object = MibTable
hh3cHPEOCCableInfoTable = _Hh3cHPEOCCableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCableInfoTable.setStatus("current")
_Hh3cHPEOCCableInfoEntry_Object = MibTableRow
hh3cHPEOCCableInfoEntry = _Hh3cHPEOCCableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1)
)
hh3cHPEOCCableInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCableInfoEntry.setStatus("current")
_Hh3cHPEOCFECErrors_Type = Counter64
_Hh3cHPEOCFECErrors_Object = MibTableColumn
hh3cHPEOCFECErrors = _Hh3cHPEOCFECErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 1),
    _Hh3cHPEOCFECErrors_Type()
)
hh3cHPEOCFECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCFECErrors.setStatus("current")
_Hh3cHPEOCAvgBitsPerCarrier_Type = Unsigned32
_Hh3cHPEOCAvgBitsPerCarrier_Object = MibTableColumn
hh3cHPEOCAvgBitsPerCarrier = _Hh3cHPEOCAvgBitsPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 2),
    _Hh3cHPEOCAvgBitsPerCarrier_Type()
)
hh3cHPEOCAvgBitsPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgBitsPerCarrier.setStatus("current")
_Hh3cHPEOCAvgSNRPerCarrier_Type = Integer32
_Hh3cHPEOCAvgSNRPerCarrier_Object = MibTableColumn
hh3cHPEOCAvgSNRPerCarrier = _Hh3cHPEOCAvgSNRPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 3),
    _Hh3cHPEOCAvgSNRPerCarrier_Type()
)
hh3cHPEOCAvgSNRPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgSNRPerCarrier.setStatus("current")
_Hh3cHPEOCAvgInPBCRCErrors_Type = Unsigned32
_Hh3cHPEOCAvgInPBCRCErrors_Object = MibTableColumn
hh3cHPEOCAvgInPBCRCErrors = _Hh3cHPEOCAvgInPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 4),
    _Hh3cHPEOCAvgInPBCRCErrors_Type()
)
hh3cHPEOCAvgInPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgInPBCRCErrors.setStatus("current")
_Hh3cHPEOCInTotalPkts_Type = Counter64
_Hh3cHPEOCInTotalPkts_Object = MibTableColumn
hh3cHPEOCInTotalPkts = _Hh3cHPEOCInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 5),
    _Hh3cHPEOCInTotalPkts_Type()
)
hh3cHPEOCInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCInTotalPkts.setStatus("current")
_Hh3cHPEOCAvgOutPower_Type = Integer32
_Hh3cHPEOCAvgOutPower_Object = MibTableColumn
hh3cHPEOCAvgOutPower = _Hh3cHPEOCAvgOutPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 6),
    _Hh3cHPEOCAvgOutPower_Type()
)
hh3cHPEOCAvgOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgOutPower.setStatus("current")
_Hh3cHPEOCAvgOutPBCRCErrors_Type = Unsigned32
_Hh3cHPEOCAvgOutPBCRCErrors_Object = MibTableColumn
hh3cHPEOCAvgOutPBCRCErrors = _Hh3cHPEOCAvgOutPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 7),
    _Hh3cHPEOCAvgOutPBCRCErrors_Type()
)
hh3cHPEOCAvgOutPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgOutPBCRCErrors.setStatus("current")
_Hh3cHPEOCOutTotalPkts_Type = Counter64
_Hh3cHPEOCOutTotalPkts_Object = MibTableColumn
hh3cHPEOCOutTotalPkts = _Hh3cHPEOCOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 8),
    _Hh3cHPEOCOutTotalPkts_Type()
)
hh3cHPEOCOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOutTotalPkts.setStatus("current")
_Hh3cHPEOCBitPerSymbolTable_Object = MibTable
hh3cHPEOCBitPerSymbolTable = _Hh3cHPEOCBitPerSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolTable.setStatus("current")
_Hh3cHPEOCBitPerSymbolEntry_Object = MibTableRow
hh3cHPEOCBitPerSymbolEntry = _Hh3cHPEOCBitPerSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1)
)
hh3cHPEOCBitPerSymbolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCBitPerSymbolIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolEntry.setStatus("current")
_Hh3cHPEOCBitPerSymbolIndex_Type = Unsigned32
_Hh3cHPEOCBitPerSymbolIndex_Object = MibTableColumn
hh3cHPEOCBitPerSymbolIndex = _Hh3cHPEOCBitPerSymbolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1, 1),
    _Hh3cHPEOCBitPerSymbolIndex_Type()
)
hh3cHPEOCBitPerSymbolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolIndex.setStatus("current")
_Hh3cHPEOCBitPerSymbol_Type = OctetString
_Hh3cHPEOCBitPerSymbol_Object = MibTableColumn
hh3cHPEOCBitPerSymbol = _Hh3cHPEOCBitPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1, 2),
    _Hh3cHPEOCBitPerSymbol_Type()
)
hh3cHPEOCBitPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-HPEOC-MIB",
    **{"hh3cHPEOC": hh3cHPEOC,
       "hh3cHPEOCSystem": hh3cHPEOCSystem,
       "hh3cHPEOCCltVlanType": hh3cHPEOCCltVlanType,
       "hh3cHPEOCCltVlanManTable": hh3cHPEOCCltVlanManTable,
       "hh3cHPEOCCltVlanManEntry": hh3cHPEOCCltVlanManEntry,
       "hh3cHPEOCCltEthPortType": hh3cHPEOCCltEthPortType,
       "hh3cHPEOCCltSysManTable": hh3cHPEOCCltSysManTable,
       "hh3cHPEOCCltSysManEntry": hh3cHPEOCCltSysManEntry,
       "hh3cHPEOCCltDescr": hh3cHPEOCCltDescr,
       "hh3cHPEOCCltFwVersion": hh3cHPEOCCltFwVersion,
       "hh3cHPEOCCnuSysManTable": hh3cHPEOCCnuSysManTable,
       "hh3cHPEOCCnuSysManEntry": hh3cHPEOCCnuSysManEntry,
       "hh3cHPEOCCnuBcastControl": hh3cHPEOCCnuBcastControl,
       "hh3cHPEOCCnuAnonymStatus": hh3cHPEOCCnuAnonymStatus,
       "hh3cHPEOCCnuMacLimit": hh3cHPEOCCnuMacLimit,
       "hh3cHPEOCCltAutoUpgrade": hh3cHPEOCCltAutoUpgrade,
       "hh3cHPEOCOnLineCnuNumber": hh3cHPEOCOnLineCnuNumber,
       "hh3cHPEOCCpuMacAddress": hh3cHPEOCCpuMacAddress,
       "hh3cHPEOCOffLineCnuNumber": hh3cHPEOCOffLineCnuNumber,
       "hh3cHPEOCDownLoadCNUFWResult": hh3cHPEOCDownLoadCNUFWResult,
       "hh3cHPEOCCltAutoUpgradeType": hh3cHPEOCCltAutoUpgradeType,
       "hh3cHPEOCAutoUpObjects": hh3cHPEOCAutoUpObjects,
       "hh3cHPEOCServerAddress": hh3cHPEOCServerAddress,
       "hh3cHPEOCServerUser": hh3cHPEOCServerUser,
       "hh3cHPEOCServerPassword": hh3cHPEOCServerPassword,
       "hh3cHPEOCCableInfo": hh3cHPEOCCableInfo,
       "hh3cHPEOCCableInfoTable": hh3cHPEOCCableInfoTable,
       "hh3cHPEOCCableInfoEntry": hh3cHPEOCCableInfoEntry,
       "hh3cHPEOCFECErrors": hh3cHPEOCFECErrors,
       "hh3cHPEOCAvgBitsPerCarrier": hh3cHPEOCAvgBitsPerCarrier,
       "hh3cHPEOCAvgSNRPerCarrier": hh3cHPEOCAvgSNRPerCarrier,
       "hh3cHPEOCAvgInPBCRCErrors": hh3cHPEOCAvgInPBCRCErrors,
       "hh3cHPEOCInTotalPkts": hh3cHPEOCInTotalPkts,
       "hh3cHPEOCAvgOutPower": hh3cHPEOCAvgOutPower,
       "hh3cHPEOCAvgOutPBCRCErrors": hh3cHPEOCAvgOutPBCRCErrors,
       "hh3cHPEOCOutTotalPkts": hh3cHPEOCOutTotalPkts,
       "hh3cHPEOCBitPerSymbolTable": hh3cHPEOCBitPerSymbolTable,
       "hh3cHPEOCBitPerSymbolEntry": hh3cHPEOCBitPerSymbolEntry,
       "hh3cHPEOCBitPerSymbolIndex": hh3cHPEOCBitPerSymbolIndex,
       "hh3cHPEOCBitPerSymbol": hh3cHPEOCBitPerSymbol}
)
