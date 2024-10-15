# SNMP MIB module (H3C-HPEOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-HPEOC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:27 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cHPEOC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cHPEOCSystem_ObjectIdentity = ObjectIdentity
h3cHPEOCSystem = _H3cHPEOCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1)
)


class _H3cHPEOCCltVlanType_Type(Integer32):
    """Custom type h3cHPEOCCltVlanType based on Integer32"""
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


_H3cHPEOCCltVlanType_Type.__name__ = "Integer32"
_H3cHPEOCCltVlanType_Object = MibScalar
h3cHPEOCCltVlanType = _H3cHPEOCCltVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 1),
    _H3cHPEOCCltVlanType_Type()
)
h3cHPEOCCltVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanType.setStatus("current")
_H3cHPEOCCltVlanManTable_Object = MibTable
h3cHPEOCCltVlanManTable = _H3cHPEOCCltVlanManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanManTable.setStatus("current")
_H3cHPEOCCltVlanManEntry_Object = MibTableRow
h3cHPEOCCltVlanManEntry = _H3cHPEOCCltVlanManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2, 1)
)
h3cHPEOCCltVlanManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanManEntry.setStatus("current")


class _H3cHPEOCCltEthPortType_Type(Integer32):
    """Custom type h3cHPEOCCltEthPortType based on Integer32"""
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


_H3cHPEOCCltEthPortType_Type.__name__ = "Integer32"
_H3cHPEOCCltEthPortType_Object = MibTableColumn
h3cHPEOCCltEthPortType = _H3cHPEOCCltEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2, 1, 1),
    _H3cHPEOCCltEthPortType_Type()
)
h3cHPEOCCltEthPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltEthPortType.setStatus("current")
_H3cHPEOCCltSysManTable_Object = MibTable
h3cHPEOCCltSysManTable = _H3cHPEOCCltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3)
)
if mibBuilder.loadTexts:
    h3cHPEOCCltSysManTable.setStatus("current")
_H3cHPEOCCltSysManEntry_Object = MibTableRow
h3cHPEOCCltSysManEntry = _H3cHPEOCCltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1)
)
h3cHPEOCCltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCltSysManEntry.setStatus("current")


class _H3cHPEOCCltDescr_Type(DisplayString):
    """Custom type h3cHPEOCCltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_H3cHPEOCCltDescr_Type.__name__ = "DisplayString"
_H3cHPEOCCltDescr_Object = MibTableColumn
h3cHPEOCCltDescr = _H3cHPEOCCltDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1, 1),
    _H3cHPEOCCltDescr_Type()
)
h3cHPEOCCltDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltDescr.setStatus("current")
_H3cHPEOCCltFwVersion_Type = DisplayString
_H3cHPEOCCltFwVersion_Object = MibTableColumn
h3cHPEOCCltFwVersion = _H3cHPEOCCltFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1, 2),
    _H3cHPEOCCltFwVersion_Type()
)
h3cHPEOCCltFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCltFwVersion.setStatus("current")
_H3cHPEOCCnuSysManTable_Object = MibTable
h3cHPEOCCnuSysManTable = _H3cHPEOCCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuSysManTable.setStatus("current")
_H3cHPEOCCnuSysManEntry_Object = MibTableRow
h3cHPEOCCnuSysManEntry = _H3cHPEOCCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1)
)
h3cHPEOCCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuSysManEntry.setStatus("current")
_H3cHPEOCCnuBcastControl_Type = TruthValue
_H3cHPEOCCnuBcastControl_Object = MibTableColumn
h3cHPEOCCnuBcastControl = _H3cHPEOCCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 1),
    _H3cHPEOCCnuBcastControl_Type()
)
h3cHPEOCCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuBcastControl.setStatus("current")
_H3cHPEOCCnuAnonymStatus_Type = TruthValue
_H3cHPEOCCnuAnonymStatus_Object = MibTableColumn
h3cHPEOCCnuAnonymStatus = _H3cHPEOCCnuAnonymStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 2),
    _H3cHPEOCCnuAnonymStatus_Type()
)
h3cHPEOCCnuAnonymStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCnuAnonymStatus.setStatus("current")
_H3cHPEOCCnuMacLimit_Type = Unsigned32
_H3cHPEOCCnuMacLimit_Object = MibTableColumn
h3cHPEOCCnuMacLimit = _H3cHPEOCCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 3),
    _H3cHPEOCCnuMacLimit_Type()
)
h3cHPEOCCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuMacLimit.setStatus("current")


class _H3cHPEOCCltAutoUpgrade_Type(TruthValue):
    """Custom type h3cHPEOCCltAutoUpgrade based on TruthValue"""


_H3cHPEOCCltAutoUpgrade_Object = MibScalar
h3cHPEOCCltAutoUpgrade = _H3cHPEOCCltAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 5),
    _H3cHPEOCCltAutoUpgrade_Type()
)
h3cHPEOCCltAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltAutoUpgrade.setStatus("current")
_H3cHPEOCOnLineCnuNumber_Type = Integer32
_H3cHPEOCOnLineCnuNumber_Object = MibScalar
h3cHPEOCOnLineCnuNumber = _H3cHPEOCOnLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 6),
    _H3cHPEOCOnLineCnuNumber_Type()
)
h3cHPEOCOnLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOnLineCnuNumber.setStatus("current")
_H3cHPEOCCpuMacAddress_Type = MacAddress
_H3cHPEOCCpuMacAddress_Object = MibScalar
h3cHPEOCCpuMacAddress = _H3cHPEOCCpuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 7),
    _H3cHPEOCCpuMacAddress_Type()
)
h3cHPEOCCpuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCpuMacAddress.setStatus("current")
_H3cHPEOCOffLineCnuNumber_Type = Integer32
_H3cHPEOCOffLineCnuNumber_Object = MibScalar
h3cHPEOCOffLineCnuNumber = _H3cHPEOCOffLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 8),
    _H3cHPEOCOffLineCnuNumber_Type()
)
h3cHPEOCOffLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOffLineCnuNumber.setStatus("current")
_H3cHPEOCDownLoadCNUFWResult_Type = DisplayString
_H3cHPEOCDownLoadCNUFWResult_Object = MibScalar
h3cHPEOCDownLoadCNUFWResult = _H3cHPEOCDownLoadCNUFWResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 9),
    _H3cHPEOCDownLoadCNUFWResult_Type()
)
h3cHPEOCDownLoadCNUFWResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cHPEOCDownLoadCNUFWResult.setStatus("current")


class _H3cHPEOCCltAutoUpgradeType_Type(Integer32):
    """Custom type h3cHPEOCCltAutoUpgradeType based on Integer32"""
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


_H3cHPEOCCltAutoUpgradeType_Type.__name__ = "Integer32"
_H3cHPEOCCltAutoUpgradeType_Object = MibScalar
h3cHPEOCCltAutoUpgradeType = _H3cHPEOCCltAutoUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 10),
    _H3cHPEOCCltAutoUpgradeType_Type()
)
h3cHPEOCCltAutoUpgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltAutoUpgradeType.setStatus("current")
_H3cHPEOCAutoUpObjects_ObjectIdentity = ObjectIdentity
h3cHPEOCAutoUpObjects = _H3cHPEOCAutoUpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11)
)
_H3cHPEOCServerAddress_Type = IpAddress
_H3cHPEOCServerAddress_Object = MibScalar
h3cHPEOCServerAddress = _H3cHPEOCServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 1),
    _H3cHPEOCServerAddress_Type()
)
h3cHPEOCServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerAddress.setStatus("current")
_H3cHPEOCServerUser_Type = DisplayString
_H3cHPEOCServerUser_Object = MibScalar
h3cHPEOCServerUser = _H3cHPEOCServerUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 2),
    _H3cHPEOCServerUser_Type()
)
h3cHPEOCServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerUser.setStatus("current")
_H3cHPEOCServerPassword_Type = DisplayString
_H3cHPEOCServerPassword_Object = MibScalar
h3cHPEOCServerPassword = _H3cHPEOCServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 3),
    _H3cHPEOCServerPassword_Type()
)
h3cHPEOCServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerPassword.setStatus("current")
_H3cHPEOCCableInfo_ObjectIdentity = ObjectIdentity
h3cHPEOCCableInfo = _H3cHPEOCCableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2)
)
_H3cHPEOCCableInfoTable_Object = MibTable
h3cHPEOCCableInfoTable = _H3cHPEOCCableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1)
)
if mibBuilder.loadTexts:
    h3cHPEOCCableInfoTable.setStatus("current")
_H3cHPEOCCableInfoEntry_Object = MibTableRow
h3cHPEOCCableInfoEntry = _H3cHPEOCCableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1)
)
h3cHPEOCCableInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCableInfoEntry.setStatus("current")
_H3cHPEOCFECErrors_Type = Counter64
_H3cHPEOCFECErrors_Object = MibTableColumn
h3cHPEOCFECErrors = _H3cHPEOCFECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 1),
    _H3cHPEOCFECErrors_Type()
)
h3cHPEOCFECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCFECErrors.setStatus("current")
_H3cHPEOCAvgBitsPerCarrier_Type = Unsigned32
_H3cHPEOCAvgBitsPerCarrier_Object = MibTableColumn
h3cHPEOCAvgBitsPerCarrier = _H3cHPEOCAvgBitsPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 2),
    _H3cHPEOCAvgBitsPerCarrier_Type()
)
h3cHPEOCAvgBitsPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgBitsPerCarrier.setStatus("current")
_H3cHPEOCAvgSNRPerCarrier_Type = Integer32
_H3cHPEOCAvgSNRPerCarrier_Object = MibTableColumn
h3cHPEOCAvgSNRPerCarrier = _H3cHPEOCAvgSNRPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 3),
    _H3cHPEOCAvgSNRPerCarrier_Type()
)
h3cHPEOCAvgSNRPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgSNRPerCarrier.setStatus("current")
_H3cHPEOCAvgInPBCRCErrors_Type = Unsigned32
_H3cHPEOCAvgInPBCRCErrors_Object = MibTableColumn
h3cHPEOCAvgInPBCRCErrors = _H3cHPEOCAvgInPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 4),
    _H3cHPEOCAvgInPBCRCErrors_Type()
)
h3cHPEOCAvgInPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgInPBCRCErrors.setStatus("current")
_H3cHPEOCInTotalPkts_Type = Counter64
_H3cHPEOCInTotalPkts_Object = MibTableColumn
h3cHPEOCInTotalPkts = _H3cHPEOCInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 5),
    _H3cHPEOCInTotalPkts_Type()
)
h3cHPEOCInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCInTotalPkts.setStatus("current")
_H3cHPEOCAvgOutPower_Type = Integer32
_H3cHPEOCAvgOutPower_Object = MibTableColumn
h3cHPEOCAvgOutPower = _H3cHPEOCAvgOutPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 6),
    _H3cHPEOCAvgOutPower_Type()
)
h3cHPEOCAvgOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgOutPower.setStatus("current")
_H3cHPEOCAvgOutPBCRCErrors_Type = Unsigned32
_H3cHPEOCAvgOutPBCRCErrors_Object = MibTableColumn
h3cHPEOCAvgOutPBCRCErrors = _H3cHPEOCAvgOutPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 7),
    _H3cHPEOCAvgOutPBCRCErrors_Type()
)
h3cHPEOCAvgOutPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgOutPBCRCErrors.setStatus("current")
_H3cHPEOCOutTotalPkts_Type = Counter64
_H3cHPEOCOutTotalPkts_Object = MibTableColumn
h3cHPEOCOutTotalPkts = _H3cHPEOCOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 8),
    _H3cHPEOCOutTotalPkts_Type()
)
h3cHPEOCOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOutTotalPkts.setStatus("current")
_H3cHPEOCBitPerSymbolTable_Object = MibTable
h3cHPEOCBitPerSymbolTable = _H3cHPEOCBitPerSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2)
)
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolTable.setStatus("current")
_H3cHPEOCBitPerSymbolEntry_Object = MibTableRow
h3cHPEOCBitPerSymbolEntry = _H3cHPEOCBitPerSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1)
)
h3cHPEOCBitPerSymbolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-HPEOC-MIB", "h3cHPEOCBitPerSymbolIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolEntry.setStatus("current")
_H3cHPEOCBitPerSymbolIndex_Type = Unsigned32
_H3cHPEOCBitPerSymbolIndex_Object = MibTableColumn
h3cHPEOCBitPerSymbolIndex = _H3cHPEOCBitPerSymbolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1, 1),
    _H3cHPEOCBitPerSymbolIndex_Type()
)
h3cHPEOCBitPerSymbolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolIndex.setStatus("current")
_H3cHPEOCBitPerSymbol_Type = OctetString
_H3cHPEOCBitPerSymbol_Object = MibTableColumn
h3cHPEOCBitPerSymbol = _H3cHPEOCBitPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1, 2),
    _H3cHPEOCBitPerSymbol_Type()
)
h3cHPEOCBitPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-HPEOC-MIB",
    **{"h3cHPEOC": h3cHPEOC,
       "h3cHPEOCSystem": h3cHPEOCSystem,
       "h3cHPEOCCltVlanType": h3cHPEOCCltVlanType,
       "h3cHPEOCCltVlanManTable": h3cHPEOCCltVlanManTable,
       "h3cHPEOCCltVlanManEntry": h3cHPEOCCltVlanManEntry,
       "h3cHPEOCCltEthPortType": h3cHPEOCCltEthPortType,
       "h3cHPEOCCltSysManTable": h3cHPEOCCltSysManTable,
       "h3cHPEOCCltSysManEntry": h3cHPEOCCltSysManEntry,
       "h3cHPEOCCltDescr": h3cHPEOCCltDescr,
       "h3cHPEOCCltFwVersion": h3cHPEOCCltFwVersion,
       "h3cHPEOCCnuSysManTable": h3cHPEOCCnuSysManTable,
       "h3cHPEOCCnuSysManEntry": h3cHPEOCCnuSysManEntry,
       "h3cHPEOCCnuBcastControl": h3cHPEOCCnuBcastControl,
       "h3cHPEOCCnuAnonymStatus": h3cHPEOCCnuAnonymStatus,
       "h3cHPEOCCnuMacLimit": h3cHPEOCCnuMacLimit,
       "h3cHPEOCCltAutoUpgrade": h3cHPEOCCltAutoUpgrade,
       "h3cHPEOCOnLineCnuNumber": h3cHPEOCOnLineCnuNumber,
       "h3cHPEOCCpuMacAddress": h3cHPEOCCpuMacAddress,
       "h3cHPEOCOffLineCnuNumber": h3cHPEOCOffLineCnuNumber,
       "h3cHPEOCDownLoadCNUFWResult": h3cHPEOCDownLoadCNUFWResult,
       "h3cHPEOCCltAutoUpgradeType": h3cHPEOCCltAutoUpgradeType,
       "h3cHPEOCAutoUpObjects": h3cHPEOCAutoUpObjects,
       "h3cHPEOCServerAddress": h3cHPEOCServerAddress,
       "h3cHPEOCServerUser": h3cHPEOCServerUser,
       "h3cHPEOCServerPassword": h3cHPEOCServerPassword,
       "h3cHPEOCCableInfo": h3cHPEOCCableInfo,
       "h3cHPEOCCableInfoTable": h3cHPEOCCableInfoTable,
       "h3cHPEOCCableInfoEntry": h3cHPEOCCableInfoEntry,
       "h3cHPEOCFECErrors": h3cHPEOCFECErrors,
       "h3cHPEOCAvgBitsPerCarrier": h3cHPEOCAvgBitsPerCarrier,
       "h3cHPEOCAvgSNRPerCarrier": h3cHPEOCAvgSNRPerCarrier,
       "h3cHPEOCAvgInPBCRCErrors": h3cHPEOCAvgInPBCRCErrors,
       "h3cHPEOCInTotalPkts": h3cHPEOCInTotalPkts,
       "h3cHPEOCAvgOutPower": h3cHPEOCAvgOutPower,
       "h3cHPEOCAvgOutPBCRCErrors": h3cHPEOCAvgOutPBCRCErrors,
       "h3cHPEOCOutTotalPkts": h3cHPEOCOutTotalPkts,
       "h3cHPEOCBitPerSymbolTable": h3cHPEOCBitPerSymbolTable,
       "h3cHPEOCBitPerSymbolEntry": h3cHPEOCBitPerSymbolEntry,
       "h3cHPEOCBitPerSymbolIndex": h3cHPEOCBitPerSymbolIndex,
       "h3cHPEOCBitPerSymbol": h3cHPEOCBitPerSymbol}
)
