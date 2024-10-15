# SNMP MIB module (ACD-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-SFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:24 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdSfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4)
)
acdSfp.setRevisions(
        ("2010-11-10 01:00",
         "2008-04-22 01:00",
         "2006-08-06 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdSfpInfoTable_Object = MibTable
acdSfpInfoTable = _AcdSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1)
)
if mibBuilder.loadTexts:
    acdSfpInfoTable.setStatus("current")
_AcdSfpInfoEntry_Object = MibTableRow
acdSfpInfoEntry = _AcdSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1)
)
acdSfpInfoEntry.setIndexNames(
    (0, "ACD-SFP-MIB", "acdSfpInfoID"),
)
if mibBuilder.loadTexts:
    acdSfpInfoEntry.setStatus("current")
_AcdSfpInfoID_Type = Unsigned32
_AcdSfpInfoID_Object = MibTableColumn
acdSfpInfoID = _AcdSfpInfoID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 1),
    _AcdSfpInfoID_Type()
)
acdSfpInfoID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSfpInfoID.setStatus("current")
_AcdSfpInfoConnIdx_Type = Unsigned32
_AcdSfpInfoConnIdx_Object = MibTableColumn
acdSfpInfoConnIdx = _AcdSfpInfoConnIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 2),
    _AcdSfpInfoConnIdx_Type()
)
acdSfpInfoConnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoConnIdx.setStatus("current")


class _AcdSfpInfoConnType_Type(Integer32):
    """Custom type acdSfpInfoConnType based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("sfpBNC", 4),
          ("sfpCOPPERPIGTAIL", 33),
          ("sfpFC1COPPER", 2),
          ("sfpFC2COPPER", 3),
          ("sfpFCCOAX", 5),
          ("sfpFIBERJACK", 6),
          ("sfpHSSDCII", 32),
          ("sfpLC", 7),
          ("sfpMTRJ", 8),
          ("sfpMU", 9),
          ("sfpPIGTAIL", 11),
          ("sfpSC", 1),
          ("sfpSG", 10))
    )


_AcdSfpInfoConnType_Type.__name__ = "Integer32"
_AcdSfpInfoConnType_Object = MibTableColumn
acdSfpInfoConnType = _AcdSfpInfoConnType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 3),
    _AcdSfpInfoConnType_Type()
)
acdSfpInfoConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoConnType.setStatus("current")


class _AcdSfpInfoVendor_Type(DisplayString):
    """Custom type acdSfpInfoVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcdSfpInfoVendor_Type.__name__ = "DisplayString"
_AcdSfpInfoVendor_Object = MibTableColumn
acdSfpInfoVendor = _AcdSfpInfoVendor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 4),
    _AcdSfpInfoVendor_Type()
)
acdSfpInfoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoVendor.setStatus("current")


class _AcdSfpInfoVendorOui_Type(DisplayString):
    """Custom type acdSfpInfoVendorOui based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AcdSfpInfoVendorOui_Type.__name__ = "DisplayString"
_AcdSfpInfoVendorOui_Object = MibTableColumn
acdSfpInfoVendorOui = _AcdSfpInfoVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 5),
    _AcdSfpInfoVendorOui_Type()
)
acdSfpInfoVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoVendorOui.setStatus("current")


class _AcdSfpInfoVendorPn_Type(DisplayString):
    """Custom type acdSfpInfoVendorPn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcdSfpInfoVendorPn_Type.__name__ = "DisplayString"
_AcdSfpInfoVendorPn_Object = MibTableColumn
acdSfpInfoVendorPn = _AcdSfpInfoVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 6),
    _AcdSfpInfoVendorPn_Type()
)
acdSfpInfoVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoVendorPn.setStatus("current")


class _AcdSfpInfoVendorRev_Type(DisplayString):
    """Custom type acdSfpInfoVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcdSfpInfoVendorRev_Type.__name__ = "DisplayString"
_AcdSfpInfoVendorRev_Object = MibTableColumn
acdSfpInfoVendorRev = _AcdSfpInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 7),
    _AcdSfpInfoVendorRev_Type()
)
acdSfpInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoVendorRev.setStatus("current")
_AcdSfpInfoWavelength_Type = Unsigned32
_AcdSfpInfoWavelength_Object = MibTableColumn
acdSfpInfoWavelength = _AcdSfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 8),
    _AcdSfpInfoWavelength_Type()
)
acdSfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoWavelength.setStatus("current")


class _AcdSfpInfoSerialNum_Type(DisplayString):
    """Custom type acdSfpInfoSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcdSfpInfoSerialNum_Type.__name__ = "DisplayString"
_AcdSfpInfoSerialNum_Object = MibTableColumn
acdSfpInfoSerialNum = _AcdSfpInfoSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 9),
    _AcdSfpInfoSerialNum_Type()
)
acdSfpInfoSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoSerialNum.setStatus("current")
_AcdSfpInfoYear_Type = Unsigned32
_AcdSfpInfoYear_Object = MibTableColumn
acdSfpInfoYear = _AcdSfpInfoYear_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 10),
    _AcdSfpInfoYear_Type()
)
acdSfpInfoYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoYear.setStatus("current")
_AcdSfpInfoMonth_Type = Unsigned32
_AcdSfpInfoMonth_Object = MibTableColumn
acdSfpInfoMonth = _AcdSfpInfoMonth_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 11),
    _AcdSfpInfoMonth_Type()
)
acdSfpInfoMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoMonth.setStatus("current")
_AcdSfpInfoDay_Type = Unsigned32
_AcdSfpInfoDay_Object = MibTableColumn
acdSfpInfoDay = _AcdSfpInfoDay_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 12),
    _AcdSfpInfoDay_Type()
)
acdSfpInfoDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoDay.setStatus("current")
_AcdSfpInfoLot_Type = Unsigned32
_AcdSfpInfoLot_Object = MibTableColumn
acdSfpInfoLot = _AcdSfpInfoLot_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 13),
    _AcdSfpInfoLot_Type()
)
acdSfpInfoLot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoLot.setStatus("current")


class _AcdSfpInfoRev8472_Type(Integer32):
    """Custom type acdSfpInfoRev8472 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rev93", 1),
          ("rev94", 2),
          ("undefined", 0))
    )


_AcdSfpInfoRev8472_Type.__name__ = "Integer32"
_AcdSfpInfoRev8472_Object = MibTableColumn
acdSfpInfoRev8472 = _AcdSfpInfoRev8472_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 14),
    _AcdSfpInfoRev8472_Type()
)
acdSfpInfoRev8472.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoRev8472.setStatus("current")
_AcdSfpInfoPresent_Type = TruthValue
_AcdSfpInfoPresent_Object = MibTableColumn
acdSfpInfoPresent = _AcdSfpInfoPresent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 15),
    _AcdSfpInfoPresent_Type()
)
acdSfpInfoPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoPresent.setStatus("current")
_AcdSfpInfoDiag_Type = TruthValue
_AcdSfpInfoDiag_Object = MibTableColumn
acdSfpInfoDiag = _AcdSfpInfoDiag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 16),
    _AcdSfpInfoDiag_Type()
)
acdSfpInfoDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoDiag.setStatus("current")
_AcdSfpInfoInternal_Type = TruthValue
_AcdSfpInfoInternal_Object = MibTableColumn
acdSfpInfoInternal = _AcdSfpInfoInternal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 17),
    _AcdSfpInfoInternal_Type()
)
acdSfpInfoInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoInternal.setStatus("current")
_AcdSfpInfoAlm_Type = TruthValue
_AcdSfpInfoAlm_Object = MibTableColumn
acdSfpInfoAlm = _AcdSfpInfoAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 18),
    _AcdSfpInfoAlm_Type()
)
acdSfpInfoAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoAlm.setStatus("current")
_AcdSfpInfoIdType_Type = Unsigned32
_AcdSfpInfoIdType_Object = MibTableColumn
acdSfpInfoIdType = _AcdSfpInfoIdType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 19),
    _AcdSfpInfoIdType_Type()
)
acdSfpInfoIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoIdType.setStatus("current")
_AcdSfpInfoExtIdType_Type = Unsigned32
_AcdSfpInfoExtIdType_Object = MibTableColumn
acdSfpInfoExtIdType = _AcdSfpInfoExtIdType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 20),
    _AcdSfpInfoExtIdType_Type()
)
acdSfpInfoExtIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoExtIdType.setStatus("current")


class _AcdSfpInfoTransCode_Type(DisplayString):
    """Custom type acdSfpInfoTransCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AcdSfpInfoTransCode_Type.__name__ = "DisplayString"
_AcdSfpInfoTransCode_Object = MibTableColumn
acdSfpInfoTransCode = _AcdSfpInfoTransCode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 21),
    _AcdSfpInfoTransCode_Type()
)
acdSfpInfoTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpInfoTransCode.setStatus("current")
_AcdSfpDiagTable_Object = MibTable
acdSfpDiagTable = _AcdSfpDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2)
)
if mibBuilder.loadTexts:
    acdSfpDiagTable.setStatus("current")
_AcdSfpDiagEntry_Object = MibTableRow
acdSfpDiagEntry = _AcdSfpDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1)
)
acdSfpDiagEntry.setIndexNames(
    (0, "ACD-SFP-MIB", "acdSfpDiagID"),
)
if mibBuilder.loadTexts:
    acdSfpDiagEntry.setStatus("current")
_AcdSfpDiagID_Type = Unsigned32
_AcdSfpDiagID_Object = MibTableColumn
acdSfpDiagID = _AcdSfpDiagID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 1),
    _AcdSfpDiagID_Type()
)
acdSfpDiagID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSfpDiagID.setStatus("current")
_AcdSfpDiagConnIdx_Type = Unsigned32
_AcdSfpDiagConnIdx_Object = MibTableColumn
acdSfpDiagConnIdx = _AcdSfpDiagConnIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 2),
    _AcdSfpDiagConnIdx_Type()
)
acdSfpDiagConnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagConnIdx.setStatus("current")
_AcdSfpDiagTemp_Type = Integer32
_AcdSfpDiagTemp_Object = MibTableColumn
acdSfpDiagTemp = _AcdSfpDiagTemp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 3),
    _AcdSfpDiagTemp_Type()
)
acdSfpDiagTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagTemp.setStatus("current")
_AcdSfpDiagVcc_Type = Unsigned32
_AcdSfpDiagVcc_Object = MibTableColumn
acdSfpDiagVcc = _AcdSfpDiagVcc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 4),
    _AcdSfpDiagVcc_Type()
)
acdSfpDiagVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagVcc.setStatus("current")
_AcdSfpDiagLbc_Type = Unsigned32
_AcdSfpDiagLbc_Object = MibTableColumn
acdSfpDiagLbc = _AcdSfpDiagLbc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 5),
    _AcdSfpDiagLbc_Type()
)
acdSfpDiagLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagLbc.setStatus("current")
_AcdSfpDiagTxPwr_Type = Unsigned32
_AcdSfpDiagTxPwr_Object = MibTableColumn
acdSfpDiagTxPwr = _AcdSfpDiagTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 6),
    _AcdSfpDiagTxPwr_Type()
)
acdSfpDiagTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagTxPwr.setStatus("current")
_AcdSfpDiagRxPwr_Type = Unsigned32
_AcdSfpDiagRxPwr_Object = MibTableColumn
acdSfpDiagRxPwr = _AcdSfpDiagRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 7),
    _AcdSfpDiagRxPwr_Type()
)
acdSfpDiagRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagRxPwr.setStatus("current")
_AcdSfpDiagTxPwrdBm_Type = DisplayString
_AcdSfpDiagTxPwrdBm_Object = MibTableColumn
acdSfpDiagTxPwrdBm = _AcdSfpDiagTxPwrdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 8),
    _AcdSfpDiagTxPwrdBm_Type()
)
acdSfpDiagTxPwrdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagTxPwrdBm.setStatus("current")
_AcdSfpDiagRxPwrdBm_Type = DisplayString
_AcdSfpDiagRxPwrdBm_Object = MibTableColumn
acdSfpDiagRxPwrdBm = _AcdSfpDiagRxPwrdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 9),
    _AcdSfpDiagRxPwrdBm_Type()
)
acdSfpDiagRxPwrdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpDiagRxPwrdBm.setStatus("current")
_AcdSfpThreshTable_Object = MibTable
acdSfpThreshTable = _AcdSfpThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3)
)
if mibBuilder.loadTexts:
    acdSfpThreshTable.setStatus("current")
_AcdSfpThreshEntry_Object = MibTableRow
acdSfpThreshEntry = _AcdSfpThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1)
)
acdSfpThreshEntry.setIndexNames(
    (0, "ACD-SFP-MIB", "acdSfpThreshID"),
)
if mibBuilder.loadTexts:
    acdSfpThreshEntry.setStatus("current")
_AcdSfpThreshID_Type = Unsigned32
_AcdSfpThreshID_Object = MibTableColumn
acdSfpThreshID = _AcdSfpThreshID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 1),
    _AcdSfpThreshID_Type()
)
acdSfpThreshID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSfpThreshID.setStatus("current")
_AcdSfpThreshConnIdx_Type = Unsigned32
_AcdSfpThreshConnIdx_Object = MibTableColumn
acdSfpThreshConnIdx = _AcdSfpThreshConnIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 2),
    _AcdSfpThreshConnIdx_Type()
)
acdSfpThreshConnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshConnIdx.setStatus("current")
_AcdSfpThreshTempHighAlm_Type = Integer32
_AcdSfpThreshTempHighAlm_Object = MibTableColumn
acdSfpThreshTempHighAlm = _AcdSfpThreshTempHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 3),
    _AcdSfpThreshTempHighAlm_Type()
)
acdSfpThreshTempHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTempHighAlm.setStatus("current")
_AcdSfpThreshTempLowAlm_Type = Integer32
_AcdSfpThreshTempLowAlm_Object = MibTableColumn
acdSfpThreshTempLowAlm = _AcdSfpThreshTempLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 4),
    _AcdSfpThreshTempLowAlm_Type()
)
acdSfpThreshTempLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTempLowAlm.setStatus("current")
_AcdSfpThreshTempHighWarn_Type = Integer32
_AcdSfpThreshTempHighWarn_Object = MibTableColumn
acdSfpThreshTempHighWarn = _AcdSfpThreshTempHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 5),
    _AcdSfpThreshTempHighWarn_Type()
)
acdSfpThreshTempHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTempHighWarn.setStatus("current")
_AcdSfpThreshTempLowWarn_Type = Integer32
_AcdSfpThreshTempLowWarn_Object = MibTableColumn
acdSfpThreshTempLowWarn = _AcdSfpThreshTempLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 6),
    _AcdSfpThreshTempLowWarn_Type()
)
acdSfpThreshTempLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTempLowWarn.setStatus("current")
_AcdSfpThreshVccHighAlm_Type = Unsigned32
_AcdSfpThreshVccHighAlm_Object = MibTableColumn
acdSfpThreshVccHighAlm = _AcdSfpThreshVccHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 7),
    _AcdSfpThreshVccHighAlm_Type()
)
acdSfpThreshVccHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshVccHighAlm.setStatus("current")
_AcdSfpThreshVccLowAlm_Type = Unsigned32
_AcdSfpThreshVccLowAlm_Object = MibTableColumn
acdSfpThreshVccLowAlm = _AcdSfpThreshVccLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 8),
    _AcdSfpThreshVccLowAlm_Type()
)
acdSfpThreshVccLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshVccLowAlm.setStatus("current")
_AcdSfpThreshVccHighWarn_Type = Unsigned32
_AcdSfpThreshVccHighWarn_Object = MibTableColumn
acdSfpThreshVccHighWarn = _AcdSfpThreshVccHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 9),
    _AcdSfpThreshVccHighWarn_Type()
)
acdSfpThreshVccHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshVccHighWarn.setStatus("current")
_AcdSfpThreshVccLowWarn_Type = Unsigned32
_AcdSfpThreshVccLowWarn_Object = MibTableColumn
acdSfpThreshVccLowWarn = _AcdSfpThreshVccLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 10),
    _AcdSfpThreshVccLowWarn_Type()
)
acdSfpThreshVccLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshVccLowWarn.setStatus("current")
_AcdSfpThreshLbcHighAlm_Type = Unsigned32
_AcdSfpThreshLbcHighAlm_Object = MibTableColumn
acdSfpThreshLbcHighAlm = _AcdSfpThreshLbcHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 11),
    _AcdSfpThreshLbcHighAlm_Type()
)
acdSfpThreshLbcHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshLbcHighAlm.setStatus("current")
_AcdSfpThreshLbcLowAlm_Type = Unsigned32
_AcdSfpThreshLbcLowAlm_Object = MibTableColumn
acdSfpThreshLbcLowAlm = _AcdSfpThreshLbcLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 12),
    _AcdSfpThreshLbcLowAlm_Type()
)
acdSfpThreshLbcLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshLbcLowAlm.setStatus("current")
_AcdSfpThreshLbcHighWarn_Type = Unsigned32
_AcdSfpThreshLbcHighWarn_Object = MibTableColumn
acdSfpThreshLbcHighWarn = _AcdSfpThreshLbcHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 13),
    _AcdSfpThreshLbcHighWarn_Type()
)
acdSfpThreshLbcHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshLbcHighWarn.setStatus("current")
_AcdSfpThreshLbcLowWarn_Type = Unsigned32
_AcdSfpThreshLbcLowWarn_Object = MibTableColumn
acdSfpThreshLbcLowWarn = _AcdSfpThreshLbcLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 14),
    _AcdSfpThreshLbcLowWarn_Type()
)
acdSfpThreshLbcLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshLbcLowWarn.setStatus("current")
_AcdSfpThreshTxPwrHighAlm_Type = Unsigned32
_AcdSfpThreshTxPwrHighAlm_Object = MibTableColumn
acdSfpThreshTxPwrHighAlm = _AcdSfpThreshTxPwrHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 15),
    _AcdSfpThreshTxPwrHighAlm_Type()
)
acdSfpThreshTxPwrHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrHighAlm.setStatus("current")
_AcdSfpThreshTxPwrLowAlm_Type = Unsigned32
_AcdSfpThreshTxPwrLowAlm_Object = MibTableColumn
acdSfpThreshTxPwrLowAlm = _AcdSfpThreshTxPwrLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 16),
    _AcdSfpThreshTxPwrLowAlm_Type()
)
acdSfpThreshTxPwrLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrLowAlm.setStatus("current")
_AcdSfpThreshTxPwrHighWarn_Type = Unsigned32
_AcdSfpThreshTxPwrHighWarn_Object = MibTableColumn
acdSfpThreshTxPwrHighWarn = _AcdSfpThreshTxPwrHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 17),
    _AcdSfpThreshTxPwrHighWarn_Type()
)
acdSfpThreshTxPwrHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrHighWarn.setStatus("current")
_AcdSfpThreshTxPwrLowWarn_Type = Unsigned32
_AcdSfpThreshTxPwrLowWarn_Object = MibTableColumn
acdSfpThreshTxPwrLowWarn = _AcdSfpThreshTxPwrLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 18),
    _AcdSfpThreshTxPwrLowWarn_Type()
)
acdSfpThreshTxPwrLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrLowWarn.setStatus("current")
_AcdSfpThreshRxPwrHighAlm_Type = Unsigned32
_AcdSfpThreshRxPwrHighAlm_Object = MibTableColumn
acdSfpThreshRxPwrHighAlm = _AcdSfpThreshRxPwrHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 19),
    _AcdSfpThreshRxPwrHighAlm_Type()
)
acdSfpThreshRxPwrHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrHighAlm.setStatus("current")
_AcdSfpThreshRxPwrLowAlm_Type = Unsigned32
_AcdSfpThreshRxPwrLowAlm_Object = MibTableColumn
acdSfpThreshRxPwrLowAlm = _AcdSfpThreshRxPwrLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 20),
    _AcdSfpThreshRxPwrLowAlm_Type()
)
acdSfpThreshRxPwrLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrLowAlm.setStatus("current")
_AcdSfpThreshRxPwrHighWarn_Type = Unsigned32
_AcdSfpThreshRxPwrHighWarn_Object = MibTableColumn
acdSfpThreshRxPwrHighWarn = _AcdSfpThreshRxPwrHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 21),
    _AcdSfpThreshRxPwrHighWarn_Type()
)
acdSfpThreshRxPwrHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrHighWarn.setStatus("current")
_AcdSfpThreshRxPwrLowWarn_Type = Unsigned32
_AcdSfpThreshRxPwrLowWarn_Object = MibTableColumn
acdSfpThreshRxPwrLowWarn = _AcdSfpThreshRxPwrLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 22),
    _AcdSfpThreshRxPwrLowWarn_Type()
)
acdSfpThreshRxPwrLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrLowWarn.setStatus("current")
_AcdSfpThreshTxPwrHighAlmdBm_Type = DisplayString
_AcdSfpThreshTxPwrHighAlmdBm_Object = MibTableColumn
acdSfpThreshTxPwrHighAlmdBm = _AcdSfpThreshTxPwrHighAlmdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 23),
    _AcdSfpThreshTxPwrHighAlmdBm_Type()
)
acdSfpThreshTxPwrHighAlmdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrHighAlmdBm.setStatus("current")
_AcdSfpThreshTxPwrLowAlmdBm_Type = DisplayString
_AcdSfpThreshTxPwrLowAlmdBm_Object = MibTableColumn
acdSfpThreshTxPwrLowAlmdBm = _AcdSfpThreshTxPwrLowAlmdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 24),
    _AcdSfpThreshTxPwrLowAlmdBm_Type()
)
acdSfpThreshTxPwrLowAlmdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrLowAlmdBm.setStatus("current")
_AcdSfpThreshTxPwrHighWarndBm_Type = DisplayString
_AcdSfpThreshTxPwrHighWarndBm_Object = MibTableColumn
acdSfpThreshTxPwrHighWarndBm = _AcdSfpThreshTxPwrHighWarndBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 25),
    _AcdSfpThreshTxPwrHighWarndBm_Type()
)
acdSfpThreshTxPwrHighWarndBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrHighWarndBm.setStatus("current")
_AcdSfpThreshTxPwrLowWarndBm_Type = DisplayString
_AcdSfpThreshTxPwrLowWarndBm_Object = MibTableColumn
acdSfpThreshTxPwrLowWarndBm = _AcdSfpThreshTxPwrLowWarndBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 26),
    _AcdSfpThreshTxPwrLowWarndBm_Type()
)
acdSfpThreshTxPwrLowWarndBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshTxPwrLowWarndBm.setStatus("current")
_AcdSfpThreshRxPwrHighAlmdBm_Type = DisplayString
_AcdSfpThreshRxPwrHighAlmdBm_Object = MibTableColumn
acdSfpThreshRxPwrHighAlmdBm = _AcdSfpThreshRxPwrHighAlmdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 27),
    _AcdSfpThreshRxPwrHighAlmdBm_Type()
)
acdSfpThreshRxPwrHighAlmdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrHighAlmdBm.setStatus("current")
_AcdSfpThreshRxPwrLowAlmdBm_Type = DisplayString
_AcdSfpThreshRxPwrLowAlmdBm_Object = MibTableColumn
acdSfpThreshRxPwrLowAlmdBm = _AcdSfpThreshRxPwrLowAlmdBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 28),
    _AcdSfpThreshRxPwrLowAlmdBm_Type()
)
acdSfpThreshRxPwrLowAlmdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrLowAlmdBm.setStatus("current")
_AcdSfpThreshRxPwrHighWarndBm_Type = DisplayString
_AcdSfpThreshRxPwrHighWarndBm_Object = MibTableColumn
acdSfpThreshRxPwrHighWarndBm = _AcdSfpThreshRxPwrHighWarndBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 29),
    _AcdSfpThreshRxPwrHighWarndBm_Type()
)
acdSfpThreshRxPwrHighWarndBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrHighWarndBm.setStatus("current")
_AcdSfpThreshRxPwrLowWarndBm_Type = DisplayString
_AcdSfpThreshRxPwrLowWarndBm_Object = MibTableColumn
acdSfpThreshRxPwrLowWarndBm = _AcdSfpThreshRxPwrLowWarndBm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 30),
    _AcdSfpThreshRxPwrLowWarndBm_Type()
)
acdSfpThreshRxPwrLowWarndBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshRxPwrLowWarndBm.setStatus("current")
_AcdSfpThreshStatusTable_Object = MibTable
acdSfpThreshStatusTable = _AcdSfpThreshStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4)
)
if mibBuilder.loadTexts:
    acdSfpThreshStatusTable.setStatus("current")
_AcdSfpThreshStatusEntry_Object = MibTableRow
acdSfpThreshStatusEntry = _AcdSfpThreshStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1)
)
acdSfpThreshStatusEntry.setIndexNames(
    (0, "ACD-SFP-MIB", "acdSfpThreshStatusID"),
)
if mibBuilder.loadTexts:
    acdSfpThreshStatusEntry.setStatus("current")
_AcdSfpThreshStatusID_Type = Unsigned32
_AcdSfpThreshStatusID_Object = MibTableColumn
acdSfpThreshStatusID = _AcdSfpThreshStatusID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 1),
    _AcdSfpThreshStatusID_Type()
)
acdSfpThreshStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSfpThreshStatusID.setStatus("current")
_AcdSfpThreshStatusConnIdx_Type = Unsigned32
_AcdSfpThreshStatusConnIdx_Object = MibTableColumn
acdSfpThreshStatusConnIdx = _AcdSfpThreshStatusConnIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 2),
    _AcdSfpThreshStatusConnIdx_Type()
)
acdSfpThreshStatusConnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusConnIdx.setStatus("current")
_AcdSfpThreshStatusTempHighAlm_Type = TruthValue
_AcdSfpThreshStatusTempHighAlm_Object = MibTableColumn
acdSfpThreshStatusTempHighAlm = _AcdSfpThreshStatusTempHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 3),
    _AcdSfpThreshStatusTempHighAlm_Type()
)
acdSfpThreshStatusTempHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTempHighAlm.setStatus("current")
_AcdSfpThreshStatusTempLowAlm_Type = TruthValue
_AcdSfpThreshStatusTempLowAlm_Object = MibTableColumn
acdSfpThreshStatusTempLowAlm = _AcdSfpThreshStatusTempLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 4),
    _AcdSfpThreshStatusTempLowAlm_Type()
)
acdSfpThreshStatusTempLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTempLowAlm.setStatus("current")
_AcdSfpThreshStatusTempHighWarn_Type = TruthValue
_AcdSfpThreshStatusTempHighWarn_Object = MibTableColumn
acdSfpThreshStatusTempHighWarn = _AcdSfpThreshStatusTempHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 5),
    _AcdSfpThreshStatusTempHighWarn_Type()
)
acdSfpThreshStatusTempHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTempHighWarn.setStatus("current")
_AcdSfpThreshStatusTempLowWarn_Type = TruthValue
_AcdSfpThreshStatusTempLowWarn_Object = MibTableColumn
acdSfpThreshStatusTempLowWarn = _AcdSfpThreshStatusTempLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 6),
    _AcdSfpThreshStatusTempLowWarn_Type()
)
acdSfpThreshStatusTempLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTempLowWarn.setStatus("current")
_AcdSfpThreshStatusVccHighAlm_Type = TruthValue
_AcdSfpThreshStatusVccHighAlm_Object = MibTableColumn
acdSfpThreshStatusVccHighAlm = _AcdSfpThreshStatusVccHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 7),
    _AcdSfpThreshStatusVccHighAlm_Type()
)
acdSfpThreshStatusVccHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusVccHighAlm.setStatus("current")
_AcdSfpThreshStatusVccLowAlm_Type = TruthValue
_AcdSfpThreshStatusVccLowAlm_Object = MibTableColumn
acdSfpThreshStatusVccLowAlm = _AcdSfpThreshStatusVccLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 8),
    _AcdSfpThreshStatusVccLowAlm_Type()
)
acdSfpThreshStatusVccLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusVccLowAlm.setStatus("current")
_AcdSfpThreshStatusVccHighWarn_Type = TruthValue
_AcdSfpThreshStatusVccHighWarn_Object = MibTableColumn
acdSfpThreshStatusVccHighWarn = _AcdSfpThreshStatusVccHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 9),
    _AcdSfpThreshStatusVccHighWarn_Type()
)
acdSfpThreshStatusVccHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusVccHighWarn.setStatus("current")
_AcdSfpThreshStatusVccLowWarn_Type = TruthValue
_AcdSfpThreshStatusVccLowWarn_Object = MibTableColumn
acdSfpThreshStatusVccLowWarn = _AcdSfpThreshStatusVccLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 10),
    _AcdSfpThreshStatusVccLowWarn_Type()
)
acdSfpThreshStatusVccLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusVccLowWarn.setStatus("current")
_AcdSfpThreshStatusLbcHighAlm_Type = TruthValue
_AcdSfpThreshStatusLbcHighAlm_Object = MibTableColumn
acdSfpThreshStatusLbcHighAlm = _AcdSfpThreshStatusLbcHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 11),
    _AcdSfpThreshStatusLbcHighAlm_Type()
)
acdSfpThreshStatusLbcHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusLbcHighAlm.setStatus("current")
_AcdSfpThreshStatusLbcLowAlm_Type = TruthValue
_AcdSfpThreshStatusLbcLowAlm_Object = MibTableColumn
acdSfpThreshStatusLbcLowAlm = _AcdSfpThreshStatusLbcLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 12),
    _AcdSfpThreshStatusLbcLowAlm_Type()
)
acdSfpThreshStatusLbcLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusLbcLowAlm.setStatus("current")
_AcdSfpThreshStatusLbcHighWarn_Type = TruthValue
_AcdSfpThreshStatusLbcHighWarn_Object = MibTableColumn
acdSfpThreshStatusLbcHighWarn = _AcdSfpThreshStatusLbcHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 13),
    _AcdSfpThreshStatusLbcHighWarn_Type()
)
acdSfpThreshStatusLbcHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusLbcHighWarn.setStatus("current")
_AcdSfpThreshStatusLbcLowWarn_Type = TruthValue
_AcdSfpThreshStatusLbcLowWarn_Object = MibTableColumn
acdSfpThreshStatusLbcLowWarn = _AcdSfpThreshStatusLbcLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 14),
    _AcdSfpThreshStatusLbcLowWarn_Type()
)
acdSfpThreshStatusLbcLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusLbcLowWarn.setStatus("current")
_AcdSfpThreshStatusTxPwrHighAlm_Type = TruthValue
_AcdSfpThreshStatusTxPwrHighAlm_Object = MibTableColumn
acdSfpThreshStatusTxPwrHighAlm = _AcdSfpThreshStatusTxPwrHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 15),
    _AcdSfpThreshStatusTxPwrHighAlm_Type()
)
acdSfpThreshStatusTxPwrHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTxPwrHighAlm.setStatus("current")
_AcdSfpThreshStatusTxPwrLowAlm_Type = TruthValue
_AcdSfpThreshStatusTxPwrLowAlm_Object = MibTableColumn
acdSfpThreshStatusTxPwrLowAlm = _AcdSfpThreshStatusTxPwrLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 16),
    _AcdSfpThreshStatusTxPwrLowAlm_Type()
)
acdSfpThreshStatusTxPwrLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTxPwrLowAlm.setStatus("current")
_AcdSfpThreshStatusTxPwrHighWarn_Type = TruthValue
_AcdSfpThreshStatusTxPwrHighWarn_Object = MibTableColumn
acdSfpThreshStatusTxPwrHighWarn = _AcdSfpThreshStatusTxPwrHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 17),
    _AcdSfpThreshStatusTxPwrHighWarn_Type()
)
acdSfpThreshStatusTxPwrHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTxPwrHighWarn.setStatus("current")
_AcdSfpThreshStatusTxPwrLowWarn_Type = TruthValue
_AcdSfpThreshStatusTxPwrLowWarn_Object = MibTableColumn
acdSfpThreshStatusTxPwrLowWarn = _AcdSfpThreshStatusTxPwrLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 18),
    _AcdSfpThreshStatusTxPwrLowWarn_Type()
)
acdSfpThreshStatusTxPwrLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusTxPwrLowWarn.setStatus("current")
_AcdSfpThreshStatusRxPwrHighAlm_Type = TruthValue
_AcdSfpThreshStatusRxPwrHighAlm_Object = MibTableColumn
acdSfpThreshStatusRxPwrHighAlm = _AcdSfpThreshStatusRxPwrHighAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 19),
    _AcdSfpThreshStatusRxPwrHighAlm_Type()
)
acdSfpThreshStatusRxPwrHighAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusRxPwrHighAlm.setStatus("current")
_AcdSfpThreshStatusRxPwrLowAlm_Type = TruthValue
_AcdSfpThreshStatusRxPwrLowAlm_Object = MibTableColumn
acdSfpThreshStatusRxPwrLowAlm = _AcdSfpThreshStatusRxPwrLowAlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 20),
    _AcdSfpThreshStatusRxPwrLowAlm_Type()
)
acdSfpThreshStatusRxPwrLowAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusRxPwrLowAlm.setStatus("current")
_AcdSfpThreshStatusRxPwrHighWarn_Type = TruthValue
_AcdSfpThreshStatusRxPwrHighWarn_Object = MibTableColumn
acdSfpThreshStatusRxPwrHighWarn = _AcdSfpThreshStatusRxPwrHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 21),
    _AcdSfpThreshStatusRxPwrHighWarn_Type()
)
acdSfpThreshStatusRxPwrHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusRxPwrHighWarn.setStatus("current")
_AcdSfpThreshStatusRxPwrLowWarn_Type = TruthValue
_AcdSfpThreshStatusRxPwrLowWarn_Object = MibTableColumn
acdSfpThreshStatusRxPwrLowWarn = _AcdSfpThreshStatusRxPwrLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 22),
    _AcdSfpThreshStatusRxPwrLowWarn_Type()
)
acdSfpThreshStatusRxPwrLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSfpThreshStatusRxPwrLowWarn.setStatus("current")
_AcdSfpNotifications_ObjectIdentity = ObjectIdentity
acdSfpNotifications = _AcdSfpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 5)
)
_AcdSfpMIBObjects_ObjectIdentity = ObjectIdentity
acdSfpMIBObjects = _AcdSfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 6)
)
_AcdSfpConformance_ObjectIdentity = ObjectIdentity
acdSfpConformance = _AcdSfpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7)
)
_AcdSfpCompliances_ObjectIdentity = ObjectIdentity
acdSfpCompliances = _AcdSfpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 1)
)
_AcdSfpGroups_ObjectIdentity = ObjectIdentity
acdSfpGroups = _AcdSfpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2)
)

# Managed Objects groups

acdSfpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 1)
)
acdSfpInfoGroup.setObjects(
      *(("ACD-SFP-MIB", "acdSfpInfoConnIdx"),
        ("ACD-SFP-MIB", "acdSfpInfoConnType"),
        ("ACD-SFP-MIB", "acdSfpInfoVendor"),
        ("ACD-SFP-MIB", "acdSfpInfoVendorOui"),
        ("ACD-SFP-MIB", "acdSfpInfoVendorPn"),
        ("ACD-SFP-MIB", "acdSfpInfoVendorRev"),
        ("ACD-SFP-MIB", "acdSfpInfoWavelength"),
        ("ACD-SFP-MIB", "acdSfpInfoSerialNum"),
        ("ACD-SFP-MIB", "acdSfpInfoYear"),
        ("ACD-SFP-MIB", "acdSfpInfoMonth"),
        ("ACD-SFP-MIB", "acdSfpInfoDay"),
        ("ACD-SFP-MIB", "acdSfpInfoLot"),
        ("ACD-SFP-MIB", "acdSfpInfoRev8472"),
        ("ACD-SFP-MIB", "acdSfpInfoPresent"),
        ("ACD-SFP-MIB", "acdSfpInfoDiag"),
        ("ACD-SFP-MIB", "acdSfpInfoInternal"),
        ("ACD-SFP-MIB", "acdSfpInfoAlm"),
        ("ACD-SFP-MIB", "acdSfpInfoIdType"),
        ("ACD-SFP-MIB", "acdSfpInfoExtIdType"),
        ("ACD-SFP-MIB", "acdSfpInfoTransCode"))
)
if mibBuilder.loadTexts:
    acdSfpInfoGroup.setStatus("current")

acdSfpDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 2)
)
acdSfpDiagGroup.setObjects(
      *(("ACD-SFP-MIB", "acdSfpDiagConnIdx"),
        ("ACD-SFP-MIB", "acdSfpDiagTemp"),
        ("ACD-SFP-MIB", "acdSfpDiagVcc"),
        ("ACD-SFP-MIB", "acdSfpDiagLbc"),
        ("ACD-SFP-MIB", "acdSfpDiagTxPwr"),
        ("ACD-SFP-MIB", "acdSfpDiagRxPwr"),
        ("ACD-SFP-MIB", "acdSfpDiagTxPwrdBm"),
        ("ACD-SFP-MIB", "acdSfpDiagRxPwrdBm"))
)
if mibBuilder.loadTexts:
    acdSfpDiagGroup.setStatus("current")

acdSfpThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 3)
)
acdSfpThreshGroup.setObjects(
      *(("ACD-SFP-MIB", "acdSfpThreshConnIdx"),
        ("ACD-SFP-MIB", "acdSfpThreshTempHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshTempLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshTempHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshTempLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshVccHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshVccLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshVccHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshVccLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshLbcHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshLbcLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshLbcHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshLbcLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighAlmdBm"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowAlmdBm"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighWarndBm"),
        ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowWarndBm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighAlmdBm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowAlmdBm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighWarndBm"),
        ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowWarndBm"))
)
if mibBuilder.loadTexts:
    acdSfpThreshGroup.setStatus("current")

acdSfpThreshStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 4)
)
acdSfpThreshStatusGroup.setObjects(
      *(("ACD-SFP-MIB", "acdSfpThreshStatusConnIdx"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTempHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTempLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTempHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTempLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusVccHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusVccLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusVccHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusVccLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusLbcHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusLbcLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusLbcHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusLbcLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrLowWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrHighAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrLowAlm"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrHighWarn"),
        ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrLowWarn"))
)
if mibBuilder.loadTexts:
    acdSfpThreshStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdSfpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    acdSfpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SFP-MIB",
    **{"acdSfp": acdSfp,
       "acdSfpInfoTable": acdSfpInfoTable,
       "acdSfpInfoEntry": acdSfpInfoEntry,
       "acdSfpInfoID": acdSfpInfoID,
       "acdSfpInfoConnIdx": acdSfpInfoConnIdx,
       "acdSfpInfoConnType": acdSfpInfoConnType,
       "acdSfpInfoVendor": acdSfpInfoVendor,
       "acdSfpInfoVendorOui": acdSfpInfoVendorOui,
       "acdSfpInfoVendorPn": acdSfpInfoVendorPn,
       "acdSfpInfoVendorRev": acdSfpInfoVendorRev,
       "acdSfpInfoWavelength": acdSfpInfoWavelength,
       "acdSfpInfoSerialNum": acdSfpInfoSerialNum,
       "acdSfpInfoYear": acdSfpInfoYear,
       "acdSfpInfoMonth": acdSfpInfoMonth,
       "acdSfpInfoDay": acdSfpInfoDay,
       "acdSfpInfoLot": acdSfpInfoLot,
       "acdSfpInfoRev8472": acdSfpInfoRev8472,
       "acdSfpInfoPresent": acdSfpInfoPresent,
       "acdSfpInfoDiag": acdSfpInfoDiag,
       "acdSfpInfoInternal": acdSfpInfoInternal,
       "acdSfpInfoAlm": acdSfpInfoAlm,
       "acdSfpInfoIdType": acdSfpInfoIdType,
       "acdSfpInfoExtIdType": acdSfpInfoExtIdType,
       "acdSfpInfoTransCode": acdSfpInfoTransCode,
       "acdSfpDiagTable": acdSfpDiagTable,
       "acdSfpDiagEntry": acdSfpDiagEntry,
       "acdSfpDiagID": acdSfpDiagID,
       "acdSfpDiagConnIdx": acdSfpDiagConnIdx,
       "acdSfpDiagTemp": acdSfpDiagTemp,
       "acdSfpDiagVcc": acdSfpDiagVcc,
       "acdSfpDiagLbc": acdSfpDiagLbc,
       "acdSfpDiagTxPwr": acdSfpDiagTxPwr,
       "acdSfpDiagRxPwr": acdSfpDiagRxPwr,
       "acdSfpDiagTxPwrdBm": acdSfpDiagTxPwrdBm,
       "acdSfpDiagRxPwrdBm": acdSfpDiagRxPwrdBm,
       "acdSfpThreshTable": acdSfpThreshTable,
       "acdSfpThreshEntry": acdSfpThreshEntry,
       "acdSfpThreshID": acdSfpThreshID,
       "acdSfpThreshConnIdx": acdSfpThreshConnIdx,
       "acdSfpThreshTempHighAlm": acdSfpThreshTempHighAlm,
       "acdSfpThreshTempLowAlm": acdSfpThreshTempLowAlm,
       "acdSfpThreshTempHighWarn": acdSfpThreshTempHighWarn,
       "acdSfpThreshTempLowWarn": acdSfpThreshTempLowWarn,
       "acdSfpThreshVccHighAlm": acdSfpThreshVccHighAlm,
       "acdSfpThreshVccLowAlm": acdSfpThreshVccLowAlm,
       "acdSfpThreshVccHighWarn": acdSfpThreshVccHighWarn,
       "acdSfpThreshVccLowWarn": acdSfpThreshVccLowWarn,
       "acdSfpThreshLbcHighAlm": acdSfpThreshLbcHighAlm,
       "acdSfpThreshLbcLowAlm": acdSfpThreshLbcLowAlm,
       "acdSfpThreshLbcHighWarn": acdSfpThreshLbcHighWarn,
       "acdSfpThreshLbcLowWarn": acdSfpThreshLbcLowWarn,
       "acdSfpThreshTxPwrHighAlm": acdSfpThreshTxPwrHighAlm,
       "acdSfpThreshTxPwrLowAlm": acdSfpThreshTxPwrLowAlm,
       "acdSfpThreshTxPwrHighWarn": acdSfpThreshTxPwrHighWarn,
       "acdSfpThreshTxPwrLowWarn": acdSfpThreshTxPwrLowWarn,
       "acdSfpThreshRxPwrHighAlm": acdSfpThreshRxPwrHighAlm,
       "acdSfpThreshRxPwrLowAlm": acdSfpThreshRxPwrLowAlm,
       "acdSfpThreshRxPwrHighWarn": acdSfpThreshRxPwrHighWarn,
       "acdSfpThreshRxPwrLowWarn": acdSfpThreshRxPwrLowWarn,
       "acdSfpThreshTxPwrHighAlmdBm": acdSfpThreshTxPwrHighAlmdBm,
       "acdSfpThreshTxPwrLowAlmdBm": acdSfpThreshTxPwrLowAlmdBm,
       "acdSfpThreshTxPwrHighWarndBm": acdSfpThreshTxPwrHighWarndBm,
       "acdSfpThreshTxPwrLowWarndBm": acdSfpThreshTxPwrLowWarndBm,
       "acdSfpThreshRxPwrHighAlmdBm": acdSfpThreshRxPwrHighAlmdBm,
       "acdSfpThreshRxPwrLowAlmdBm": acdSfpThreshRxPwrLowAlmdBm,
       "acdSfpThreshRxPwrHighWarndBm": acdSfpThreshRxPwrHighWarndBm,
       "acdSfpThreshRxPwrLowWarndBm": acdSfpThreshRxPwrLowWarndBm,
       "acdSfpThreshStatusTable": acdSfpThreshStatusTable,
       "acdSfpThreshStatusEntry": acdSfpThreshStatusEntry,
       "acdSfpThreshStatusID": acdSfpThreshStatusID,
       "acdSfpThreshStatusConnIdx": acdSfpThreshStatusConnIdx,
       "acdSfpThreshStatusTempHighAlm": acdSfpThreshStatusTempHighAlm,
       "acdSfpThreshStatusTempLowAlm": acdSfpThreshStatusTempLowAlm,
       "acdSfpThreshStatusTempHighWarn": acdSfpThreshStatusTempHighWarn,
       "acdSfpThreshStatusTempLowWarn": acdSfpThreshStatusTempLowWarn,
       "acdSfpThreshStatusVccHighAlm": acdSfpThreshStatusVccHighAlm,
       "acdSfpThreshStatusVccLowAlm": acdSfpThreshStatusVccLowAlm,
       "acdSfpThreshStatusVccHighWarn": acdSfpThreshStatusVccHighWarn,
       "acdSfpThreshStatusVccLowWarn": acdSfpThreshStatusVccLowWarn,
       "acdSfpThreshStatusLbcHighAlm": acdSfpThreshStatusLbcHighAlm,
       "acdSfpThreshStatusLbcLowAlm": acdSfpThreshStatusLbcLowAlm,
       "acdSfpThreshStatusLbcHighWarn": acdSfpThreshStatusLbcHighWarn,
       "acdSfpThreshStatusLbcLowWarn": acdSfpThreshStatusLbcLowWarn,
       "acdSfpThreshStatusTxPwrHighAlm": acdSfpThreshStatusTxPwrHighAlm,
       "acdSfpThreshStatusTxPwrLowAlm": acdSfpThreshStatusTxPwrLowAlm,
       "acdSfpThreshStatusTxPwrHighWarn": acdSfpThreshStatusTxPwrHighWarn,
       "acdSfpThreshStatusTxPwrLowWarn": acdSfpThreshStatusTxPwrLowWarn,
       "acdSfpThreshStatusRxPwrHighAlm": acdSfpThreshStatusRxPwrHighAlm,
       "acdSfpThreshStatusRxPwrLowAlm": acdSfpThreshStatusRxPwrLowAlm,
       "acdSfpThreshStatusRxPwrHighWarn": acdSfpThreshStatusRxPwrHighWarn,
       "acdSfpThreshStatusRxPwrLowWarn": acdSfpThreshStatusRxPwrLowWarn,
       "acdSfpNotifications": acdSfpNotifications,
       "acdSfpMIBObjects": acdSfpMIBObjects,
       "acdSfpConformance": acdSfpConformance,
       "acdSfpCompliances": acdSfpCompliances,
       "acdSfpCompliance": acdSfpCompliance,
       "acdSfpGroups": acdSfpGroups,
       "acdSfpInfoGroup": acdSfpInfoGroup,
       "acdSfpDiagGroup": acdSfpDiagGroup,
       "acdSfpThreshGroup": acdSfpThreshGroup,
       "acdSfpThreshStatusGroup": acdSfpThreshStatusGroup}
)
