# SNMP MIB module (WWP-LEOS-PORT-XCVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-PORT-XCVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:05 2024
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

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosPortXcvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4)
)
wwpLeosPortXcvrMIB.setRevisions(
        ("2011-07-06 00:00",
         "2011-05-24 00:00",
         "2011-03-08 00:00",
         "2010-02-01 00:00",
         "2006-03-15 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosPortXcvrMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBObjects = _WwpLeosPortXcvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1)
)
_WwpLeosPortXcvr_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvr = _WwpLeosPortXcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1)
)
_WwpLeosPortXcvrTable_Object = MibTable
wwpLeosPortXcvrTable = _WwpLeosPortXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTable.setStatus("current")
_WwpLeosPortXcvrEntry_Object = MibTableRow
wwpLeosPortXcvrEntry = _WwpLeosPortXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1)
)
wwpLeosPortXcvrEntry.setIndexNames(
    (0, "WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId"),
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEntry.setStatus("current")


class _WwpLeosPortXcvrId_Type(Integer32):
    """Custom type wwpLeosPortXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrId_Type.__name__ = "Integer32"
_WwpLeosPortXcvrId_Object = MibTableColumn
wwpLeosPortXcvrId = _WwpLeosPortXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 1),
    _WwpLeosPortXcvrId_Type()
)
wwpLeosPortXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrId.setStatus("current")


class _WwpLeosPortXcvrOperState_Type(Integer32):
    """Custom type wwpLeosPortXcvrOperState based on Integer32"""
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
          ("enabled", 2),
          ("faulted", 5),
          ("loopback", 3),
          ("notPresent", 4))
    )


_WwpLeosPortXcvrOperState_Type.__name__ = "Integer32"
_WwpLeosPortXcvrOperState_Object = MibTableColumn
wwpLeosPortXcvrOperState = _WwpLeosPortXcvrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 2),
    _WwpLeosPortXcvrOperState_Type()
)
wwpLeosPortXcvrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrOperState.setStatus("current")


class _WwpLeosPortXcvrIdentiferType_Type(Integer32):
    """Custom type wwpLeosPortXcvrIdentiferType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("gbic", 2),
          ("reserved", 5),
          ("sfp", 4),
          ("solderedType", 3),
          ("unknown", 1),
          ("vendorSpecific", 6),
          ("x2", 13),
          ("xbi", 7),
          ("xenpak", 8),
          ("xff", 10),
          ("xfp", 9),
          ("xfpe", 11),
          ("xpak", 12))
    )


_WwpLeosPortXcvrIdentiferType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrIdentiferType_Object = MibTableColumn
wwpLeosPortXcvrIdentiferType = _WwpLeosPortXcvrIdentiferType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 3),
    _WwpLeosPortXcvrIdentiferType_Type()
)
wwpLeosPortXcvrIdentiferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrIdentiferType.setStatus("current")


class _WwpLeosPortXcvrExtIdentiferType_Type(Integer32):
    """Custom type wwpLeosPortXcvrExtIdentiferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfp-gbic", 2),
          ("unknown", 1))
    )


_WwpLeosPortXcvrExtIdentiferType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrExtIdentiferType_Object = MibTableColumn
wwpLeosPortXcvrExtIdentiferType = _WwpLeosPortXcvrExtIdentiferType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 4),
    _WwpLeosPortXcvrExtIdentiferType_Type()
)
wwpLeosPortXcvrExtIdentiferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrExtIdentiferType.setStatus("current")


class _WwpLeosPortXcvrConnectorType_Type(Integer32):
    """Custom type wwpLeosPortXcvrConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrConnectorType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrConnectorType_Object = MibTableColumn
wwpLeosPortXcvrConnectorType = _WwpLeosPortXcvrConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 5),
    _WwpLeosPortXcvrConnectorType_Type()
)
wwpLeosPortXcvrConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrConnectorType.setStatus("current")


class _WwpLeosPortXcvrType_Type(Integer32):
    """Custom type wwpLeosPortXcvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrType_Object = MibTableColumn
wwpLeosPortXcvrType = _WwpLeosPortXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 6),
    _WwpLeosPortXcvrType_Type()
)
wwpLeosPortXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrType.setStatus("current")
_WwpLeosPortXcvrVendorName_Type = DisplayString
_WwpLeosPortXcvrVendorName_Object = MibTableColumn
wwpLeosPortXcvrVendorName = _WwpLeosPortXcvrVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 7),
    _WwpLeosPortXcvrVendorName_Type()
)
wwpLeosPortXcvrVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVendorName.setStatus("current")


class _WwpLeosPortXcvrVendorOUI_Type(OctetString):
    """Custom type wwpLeosPortXcvrVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosPortXcvrVendorOUI_Type.__name__ = "OctetString"
_WwpLeosPortXcvrVendorOUI_Object = MibTableColumn
wwpLeosPortXcvrVendorOUI = _WwpLeosPortXcvrVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 8),
    _WwpLeosPortXcvrVendorOUI_Type()
)
wwpLeosPortXcvrVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVendorOUI.setStatus("current")
_WwpLeosPortXcvrVendorPN_Type = DisplayString
_WwpLeosPortXcvrVendorPN_Object = MibTableColumn
wwpLeosPortXcvrVendorPN = _WwpLeosPortXcvrVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 9),
    _WwpLeosPortXcvrVendorPN_Type()
)
wwpLeosPortXcvrVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVendorPN.setStatus("current")
_WwpLeosPortXcvrRevNum_Type = DisplayString
_WwpLeosPortXcvrRevNum_Object = MibTableColumn
wwpLeosPortXcvrRevNum = _WwpLeosPortXcvrRevNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 10),
    _WwpLeosPortXcvrRevNum_Type()
)
wwpLeosPortXcvrRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRevNum.setStatus("current")
_WwpLeosPortXcvrSerialNum_Type = DisplayString
_WwpLeosPortXcvrSerialNum_Object = MibTableColumn
wwpLeosPortXcvrSerialNum = _WwpLeosPortXcvrSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 11),
    _WwpLeosPortXcvrSerialNum_Type()
)
wwpLeosPortXcvrSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrSerialNum.setStatus("current")


class _WwpLeosPortXcvrEncodingType_Type(Integer32):
    """Custom type wwpLeosPortXcvrEncodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrEncodingType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrEncodingType_Object = MibTableColumn
wwpLeosPortXcvrEncodingType = _WwpLeosPortXcvrEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 12),
    _WwpLeosPortXcvrEncodingType_Type()
)
wwpLeosPortXcvrEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEncodingType.setStatus("current")
_WwpLeosPortXcvrMfgDate_Type = DisplayString
_WwpLeosPortXcvrMfgDate_Object = MibTableColumn
wwpLeosPortXcvrMfgDate = _WwpLeosPortXcvrMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 13),
    _WwpLeosPortXcvrMfgDate_Type()
)
wwpLeosPortXcvrMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrMfgDate.setStatus("current")


class _WwpLeosPortXcvrComplianceVer_Type(Integer32):
    """Custom type wwpLeosPortXcvrComplianceVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WwpLeosPortXcvrComplianceVer_Type.__name__ = "Integer32"
_WwpLeosPortXcvrComplianceVer_Object = MibTableColumn
wwpLeosPortXcvrComplianceVer = _WwpLeosPortXcvrComplianceVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 14),
    _WwpLeosPortXcvrComplianceVer_Type()
)
wwpLeosPortXcvrComplianceVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrComplianceVer.setStatus("current")


class _WwpLeosPortXcvrWaveLength_Type(Integer32):
    """Custom type wwpLeosPortXcvrWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrWaveLength_Type.__name__ = "Integer32"
_WwpLeosPortXcvrWaveLength_Object = MibTableColumn
wwpLeosPortXcvrWaveLength = _WwpLeosPortXcvrWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 15),
    _WwpLeosPortXcvrWaveLength_Type()
)
wwpLeosPortXcvrWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrWaveLength.setStatus("current")


class _WwpLeosPortXcvrTemperature_Type(Integer32):
    """Custom type wwpLeosPortXcvrTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrTemperature_Type.__name__ = "Integer32"
_WwpLeosPortXcvrTemperature_Object = MibTableColumn
wwpLeosPortXcvrTemperature = _WwpLeosPortXcvrTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 16),
    _WwpLeosPortXcvrTemperature_Type()
)
wwpLeosPortXcvrTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTemperature.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTemperature.setUnits("centigrade")


class _WwpLeosPortXcvrVcc_Type(Integer32):
    """Custom type wwpLeosPortXcvrVcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrVcc_Type.__name__ = "Integer32"
_WwpLeosPortXcvrVcc_Object = MibTableColumn
wwpLeosPortXcvrVcc = _WwpLeosPortXcvrVcc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 17),
    _WwpLeosPortXcvrVcc_Type()
)
wwpLeosPortXcvrVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVcc.setStatus("current")


class _WwpLeosPortXcvrBias_Type(Integer32):
    """Custom type wwpLeosPortXcvrBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrBias_Type.__name__ = "Integer32"
_WwpLeosPortXcvrBias_Object = MibTableColumn
wwpLeosPortXcvrBias = _WwpLeosPortXcvrBias_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 18),
    _WwpLeosPortXcvrBias_Type()
)
wwpLeosPortXcvrBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBias.setStatus("current")


class _WwpLeosPortXcvrRxPower_Type(Integer32):
    """Custom type wwpLeosPortXcvrRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrRxPower_Type.__name__ = "Integer32"
_WwpLeosPortXcvrRxPower_Object = MibTableColumn
wwpLeosPortXcvrRxPower = _WwpLeosPortXcvrRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 19),
    _WwpLeosPortXcvrRxPower_Type()
)
wwpLeosPortXcvrRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPower.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPower.setUnits("uW")


class _WwpLeosPortXcvrTxState_Type(Integer32):
    """Custom type wwpLeosPortXcvrTxState based on Integer32"""
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


_WwpLeosPortXcvrTxState_Type.__name__ = "Integer32"
_WwpLeosPortXcvrTxState_Object = MibTableColumn
wwpLeosPortXcvrTxState = _WwpLeosPortXcvrTxState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 20),
    _WwpLeosPortXcvrTxState_Type()
)
wwpLeosPortXcvrTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxState.setStatus("current")


class _WwpLeosPortXcvrTxFaultStatus_Type(Integer32):
    """Custom type wwpLeosPortXcvrTxFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("noFault", 2))
    )


_WwpLeosPortXcvrTxFaultStatus_Type.__name__ = "Integer32"
_WwpLeosPortXcvrTxFaultStatus_Object = MibTableColumn
wwpLeosPortXcvrTxFaultStatus = _WwpLeosPortXcvrTxFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 21),
    _WwpLeosPortXcvrTxFaultStatus_Type()
)
wwpLeosPortXcvrTxFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxFaultStatus.setStatus("current")


class _WwpLeosPortXcvrRxRateStatus_Type(Integer32):
    """Custom type wwpLeosPortXcvrRxRateStatus based on Integer32"""
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


_WwpLeosPortXcvrRxRateStatus_Type.__name__ = "Integer32"
_WwpLeosPortXcvrRxRateStatus_Object = MibTableColumn
wwpLeosPortXcvrRxRateStatus = _WwpLeosPortXcvrRxRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 22),
    _WwpLeosPortXcvrRxRateStatus_Type()
)
wwpLeosPortXcvrRxRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxRateStatus.setStatus("current")


class _WwpLeosPortXcvr9by125um_Type(Integer32):
    """Custom type wwpLeosPortXcvr9by125um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvr9by125um_Type.__name__ = "Integer32"
_WwpLeosPortXcvr9by125um_Object = MibTableColumn
wwpLeosPortXcvr9by125um = _WwpLeosPortXcvr9by125um_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 23),
    _WwpLeosPortXcvr9by125um_Type()
)
wwpLeosPortXcvr9by125um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvr9by125um.setStatus("current")


class _WwpLeosPortXcvr50by125um_Type(Integer32):
    """Custom type wwpLeosPortXcvr50by125um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvr50by125um_Type.__name__ = "Integer32"
_WwpLeosPortXcvr50by125um_Object = MibTableColumn
wwpLeosPortXcvr50by125um = _WwpLeosPortXcvr50by125um_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 24),
    _WwpLeosPortXcvr50by125um_Type()
)
wwpLeosPortXcvr50by125um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvr50by125um.setStatus("current")


class _WwpLeosPortXcvr62dot5by125um_Type(Integer32):
    """Custom type wwpLeosPortXcvr62dot5by125um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvr62dot5by125um_Type.__name__ = "Integer32"
_WwpLeosPortXcvr62dot5by125um_Object = MibTableColumn
wwpLeosPortXcvr62dot5by125um = _WwpLeosPortXcvr62dot5by125um_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 25),
    _WwpLeosPortXcvr62dot5by125um_Type()
)
wwpLeosPortXcvr62dot5by125um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvr62dot5by125um.setStatus("current")


class _WwpLeosPortXcvrCu_Type(Integer32):
    """Custom type wwpLeosPortXcvrCu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrCu_Type.__name__ = "Integer32"
_WwpLeosPortXcvrCu_Object = MibTableColumn
wwpLeosPortXcvrCu = _WwpLeosPortXcvrCu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 26),
    _WwpLeosPortXcvrCu_Type()
)
wwpLeosPortXcvrCu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrCu.setStatus("current")


class _WwpLeosPortXcvrTxOutputPw_Type(Integer32):
    """Custom type wwpLeosPortXcvrTxOutputPw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrTxOutputPw_Type.__name__ = "Integer32"
_WwpLeosPortXcvrTxOutputPw_Object = MibTableColumn
wwpLeosPortXcvrTxOutputPw = _WwpLeosPortXcvrTxOutputPw_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 27),
    _WwpLeosPortXcvrTxOutputPw_Type()
)
wwpLeosPortXcvrTxOutputPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxOutputPw.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxOutputPw.setUnits("uW")
_WwpLeosPortXcvrLosState_Type = TruthValue
_WwpLeosPortXcvrLosState_Object = MibTableColumn
wwpLeosPortXcvrLosState = _WwpLeosPortXcvrLosState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 28),
    _WwpLeosPortXcvrLosState_Type()
)
wwpLeosPortXcvrLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLosState.setStatus("current")
_WwpLeosPortXcvrDiagSupported_Type = TruthValue
_WwpLeosPortXcvrDiagSupported_Object = MibTableColumn
wwpLeosPortXcvrDiagSupported = _WwpLeosPortXcvrDiagSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 29),
    _WwpLeosPortXcvrDiagSupported_Type()
)
wwpLeosPortXcvrDiagSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrDiagSupported.setStatus("current")
_WwpLeosPortXcvrEnhDiagAlarmSupported_Type = TruthValue
_WwpLeosPortXcvrEnhDiagAlarmSupported_Object = MibTableColumn
wwpLeosPortXcvrEnhDiagAlarmSupported = _WwpLeosPortXcvrEnhDiagAlarmSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 30),
    _WwpLeosPortXcvrEnhDiagAlarmSupported_Type()
)
wwpLeosPortXcvrEnhDiagAlarmSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEnhDiagAlarmSupported.setStatus("current")
_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Type = TruthValue
_WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Object = MibTableColumn
wwpLeosPortXcvrEnhDiagSoftTxDisableSupported = _WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 31),
    _WwpLeosPortXcvrEnhDiagSoftTxDisableSupported_Type()
)
wwpLeosPortXcvrEnhDiagSoftTxDisableSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEnhDiagSoftTxDisableSupported.setStatus("current")
_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Type = TruthValue
_WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Object = MibTableColumn
wwpLeosPortXcvrEnhDiagSoftTxFaultSupported = _WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 32),
    _WwpLeosPortXcvrEnhDiagSoftTxFaultSupported_Type()
)
wwpLeosPortXcvrEnhDiagSoftTxFaultSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEnhDiagSoftTxFaultSupported.setStatus("current")
_WwpLeosPortXcvrEnhDiagRxLosSupported_Type = TruthValue
_WwpLeosPortXcvrEnhDiagRxLosSupported_Object = MibTableColumn
wwpLeosPortXcvrEnhDiagRxLosSupported = _WwpLeosPortXcvrEnhDiagRxLosSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 33),
    _WwpLeosPortXcvrEnhDiagRxLosSupported_Type()
)
wwpLeosPortXcvrEnhDiagRxLosSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEnhDiagRxLosSupported.setStatus("current")
_WwpLeosPortXcvrHighTempAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighTempAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighTempAlarmThreshold = _WwpLeosPortXcvrHighTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 34),
    _WwpLeosPortXcvrHighTempAlarmThreshold_Type()
)
wwpLeosPortXcvrHighTempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighTempAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrLowTempAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowTempAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowTempAlarmThreshold = _WwpLeosPortXcvrLowTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 35),
    _WwpLeosPortXcvrLowTempAlarmThreshold_Type()
)
wwpLeosPortXcvrLowTempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowTempAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrHighVccAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighVccAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighVccAlarmThreshold = _WwpLeosPortXcvrHighVccAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 36),
    _WwpLeosPortXcvrHighVccAlarmThreshold_Type()
)
wwpLeosPortXcvrHighVccAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighVccAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrLowVccAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowVccAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowVccAlarmThreshold = _WwpLeosPortXcvrLowVccAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 37),
    _WwpLeosPortXcvrLowVccAlarmThreshold_Type()
)
wwpLeosPortXcvrLowVccAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowVccAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrHighBiasAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighBiasAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighBiasAlarmThreshold = _WwpLeosPortXcvrHighBiasAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 38),
    _WwpLeosPortXcvrHighBiasAlarmThreshold_Type()
)
wwpLeosPortXcvrHighBiasAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighBiasAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrLowBiasAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowBiasAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowBiasAlarmThreshold = _WwpLeosPortXcvrLowBiasAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 39),
    _WwpLeosPortXcvrLowBiasAlarmThreshold_Type()
)
wwpLeosPortXcvrLowBiasAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowBiasAlarmThreshold.setStatus("current")
_WwpLeosPortXcvrHighTxPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighTxPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighTxPwAlarmThreshold = _WwpLeosPortXcvrHighTxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 40),
    _WwpLeosPortXcvrHighTxPwAlarmThreshold_Type()
)
wwpLeosPortXcvrHighTxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighTxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighTxPwAlarmThreshold.setUnits("uW")
_WwpLeosPortXcvrLowTxPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowTxPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowTxPwAlarmThreshold = _WwpLeosPortXcvrLowTxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 41),
    _WwpLeosPortXcvrLowTxPwAlarmThreshold_Type()
)
wwpLeosPortXcvrLowTxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowTxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowTxPwAlarmThreshold.setUnits("uW")
_WwpLeosPortXcvrHighRxPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighRxPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighRxPwAlarmThreshold = _WwpLeosPortXcvrHighRxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 42),
    _WwpLeosPortXcvrHighRxPwAlarmThreshold_Type()
)
wwpLeosPortXcvrHighRxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighRxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighRxPwAlarmThreshold.setUnits("uW")
_WwpLeosPortXcvrLowRxPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowRxPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowRxPwAlarmThreshold = _WwpLeosPortXcvrLowRxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 43),
    _WwpLeosPortXcvrLowRxPwAlarmThreshold_Type()
)
wwpLeosPortXcvrLowRxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowRxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowRxPwAlarmThreshold.setUnits("uW")
_WwpLeosPortXcvrEnhDiagRateSelectSupported_Type = TruthValue
_WwpLeosPortXcvrEnhDiagRateSelectSupported_Object = MibTableColumn
wwpLeosPortXcvrEnhDiagRateSelectSupported = _WwpLeosPortXcvrEnhDiagRateSelectSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 44),
    _WwpLeosPortXcvrEnhDiagRateSelectSupported_Type()
)
wwpLeosPortXcvrEnhDiagRateSelectSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEnhDiagRateSelectSupported.setStatus("current")


class _WwpLeosPortXcvrAdminState_Type(Integer32):
    """Custom type wwpLeosPortXcvrAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("loopback", 3))
    )


_WwpLeosPortXcvrAdminState_Type.__name__ = "Integer32"
_WwpLeosPortXcvrAdminState_Object = MibTableColumn
wwpLeosPortXcvrAdminState = _WwpLeosPortXcvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 45),
    _WwpLeosPortXcvrAdminState_Type()
)
wwpLeosPortXcvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrAdminState.setStatus("current")


class _WwpLeosPortXcvrXfpMinBitRate_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMinBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMinBitRate_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMinBitRate_Object = MibTableColumn
wwpLeosPortXcvrXfpMinBitRate = _WwpLeosPortXcvrXfpMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 70),
    _WwpLeosPortXcvrXfpMinBitRate_Type()
)
wwpLeosPortXcvrXfpMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMinBitRate.setStatus("current")


class _WwpLeosPortXcvrXfpMaxBitRate_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMaxBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMaxBitRate_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMaxBitRate_Object = MibTableColumn
wwpLeosPortXcvrXfpMaxBitRate = _WwpLeosPortXcvrXfpMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 71),
    _WwpLeosPortXcvrXfpMaxBitRate_Type()
)
wwpLeosPortXcvrXfpMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMaxBitRate.setStatus("current")


class _WwpLeosPortXcvrXfpLinkLenSmf1km_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpLinkLenSmf1km based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpLinkLenSmf1km_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpLinkLenSmf1km_Object = MibTableColumn
wwpLeosPortXcvrXfpLinkLenSmf1km = _WwpLeosPortXcvrXfpLinkLenSmf1km_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 72),
    _WwpLeosPortXcvrXfpLinkLenSmf1km_Type()
)
wwpLeosPortXcvrXfpLinkLenSmf1km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLinkLenSmf1km.setStatus("current")


class _WwpLeosPortXcvrXfpLinkLenE50u2m_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpLinkLenE50u2m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpLinkLenE50u2m_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpLinkLenE50u2m_Object = MibTableColumn
wwpLeosPortXcvrXfpLinkLenE50u2m = _WwpLeosPortXcvrXfpLinkLenE50u2m_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 73),
    _WwpLeosPortXcvrXfpLinkLenE50u2m_Type()
)
wwpLeosPortXcvrXfpLinkLenE50u2m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLinkLenE50u2m.setStatus("current")


class _WwpLeosPortXcvrXfpLinkLen50u1m_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpLinkLen50u1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpLinkLen50u1m_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpLinkLen50u1m_Object = MibTableColumn
wwpLeosPortXcvrXfpLinkLen50u1m = _WwpLeosPortXcvrXfpLinkLen50u1m_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 74),
    _WwpLeosPortXcvrXfpLinkLen50u1m_Type()
)
wwpLeosPortXcvrXfpLinkLen50u1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLinkLen50u1m.setStatus("current")


class _WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpLinkLen62dot5u1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpLinkLen62dot5u1m_Object = MibTableColumn
wwpLeosPortXcvrXfpLinkLen62dot5u1m = _WwpLeosPortXcvrXfpLinkLen62dot5u1m_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 75),
    _WwpLeosPortXcvrXfpLinkLen62dot5u1m_Type()
)
wwpLeosPortXcvrXfpLinkLen62dot5u1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLinkLen62dot5u1m.setStatus("current")


class _WwpLeosPortXcvrXfpLinkLenCopper1m_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpLinkLenCopper1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpLinkLenCopper1m_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpLinkLenCopper1m_Object = MibTableColumn
wwpLeosPortXcvrXfpLinkLenCopper1m = _WwpLeosPortXcvrXfpLinkLenCopper1m_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 76),
    _WwpLeosPortXcvrXfpLinkLenCopper1m_Type()
)
wwpLeosPortXcvrXfpLinkLenCopper1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLinkLenCopper1m.setStatus("current")


class _WwpLeosPortXcvrXfpDevTech_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpDevTech based on Integer32"""
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
        *(("copperOrOther", 9),
          ("dfb1310nm", 5),
          ("dfb1550nm", 6),
          ("eml1310nm", 7),
          ("eml1550nm", 8),
          ("fp1310nm", 4),
          ("reserved", 11),
          ("tunable1550nm", 10),
          ("vcsel1310nm", 2),
          ("vcsel1550nm", 3),
          ("vcsel850nm", 1))
    )


_WwpLeosPortXcvrXfpDevTech_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpDevTech_Object = MibTableColumn
wwpLeosPortXcvrXfpDevTech = _WwpLeosPortXcvrXfpDevTech_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 77),
    _WwpLeosPortXcvrXfpDevTech_Type()
)
wwpLeosPortXcvrXfpDevTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpDevTech.setStatus("current")


class _WwpLeosPortXcvrXfpTransmitterTech_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpTransmitterTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpTransmitterTech_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpTransmitterTech_Object = MibTableColumn
wwpLeosPortXcvrXfpTransmitterTech = _WwpLeosPortXcvrXfpTransmitterTech_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 78),
    _WwpLeosPortXcvrXfpTransmitterTech_Type()
)
wwpLeosPortXcvrXfpTransmitterTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpTransmitterTech.setStatus("current")


class _WwpLeosPortXcvrXfpCdrSupport_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpCdrSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpCdrSupport_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpCdrSupport_Object = MibTableColumn
wwpLeosPortXcvrXfpCdrSupport = _WwpLeosPortXcvrXfpCdrSupport_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 79),
    _WwpLeosPortXcvrXfpCdrSupport_Type()
)
wwpLeosPortXcvrXfpCdrSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpCdrSupport.setStatus("current")


class _WwpLeosPortXcvrXfpWaveLengthTol_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpWaveLengthTol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpWaveLengthTol_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpWaveLengthTol_Object = MibTableColumn
wwpLeosPortXcvrXfpWaveLengthTol = _WwpLeosPortXcvrXfpWaveLengthTol_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 80),
    _WwpLeosPortXcvrXfpWaveLengthTol_Type()
)
wwpLeosPortXcvrXfpWaveLengthTol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpWaveLengthTol.setStatus("current")


class _WwpLeosPortXcvrXfpMaxCaseTemp_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMaxCaseTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMaxCaseTemp_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMaxCaseTemp_Object = MibTableColumn
wwpLeosPortXcvrXfpMaxCaseTemp = _WwpLeosPortXcvrXfpMaxCaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 81),
    _WwpLeosPortXcvrXfpMaxCaseTemp_Type()
)
wwpLeosPortXcvrXfpMaxCaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMaxCaseTemp.setStatus("current")


class _WwpLeosPortXcvrXfpMaxPower_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMaxPower_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMaxPower_Object = MibTableColumn
wwpLeosPortXcvrXfpMaxPower = _WwpLeosPortXcvrXfpMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 82),
    _WwpLeosPortXcvrXfpMaxPower_Type()
)
wwpLeosPortXcvrXfpMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMaxPower.setStatus("current")


class _WwpLeosPortXcvrXfpMax5vCurrent_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMax5vCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMax5vCurrent_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMax5vCurrent_Object = MibTableColumn
wwpLeosPortXcvrXfpMax5vCurrent = _WwpLeosPortXcvrXfpMax5vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 83),
    _WwpLeosPortXcvrXfpMax5vCurrent_Type()
)
wwpLeosPortXcvrXfpMax5vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMax5vCurrent.setStatus("current")


class _WwpLeosPortXcvrXfpMax3p3vCurrent_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMax3p3vCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMax3p3vCurrent_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMax3p3vCurrent_Object = MibTableColumn
wwpLeosPortXcvrXfpMax3p3vCurrent = _WwpLeosPortXcvrXfpMax3p3vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 84),
    _WwpLeosPortXcvrXfpMax3p3vCurrent_Type()
)
wwpLeosPortXcvrXfpMax3p3vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMax3p3vCurrent.setStatus("current")


class _WwpLeosPortXcvrXfpMax1p8vCurrent_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMax1p8vCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMax1p8vCurrent_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMax1p8vCurrent_Object = MibTableColumn
wwpLeosPortXcvrXfpMax1p8vCurrent = _WwpLeosPortXcvrXfpMax1p8vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 85),
    _WwpLeosPortXcvrXfpMax1p8vCurrent_Type()
)
wwpLeosPortXcvrXfpMax1p8vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMax1p8vCurrent.setStatus("current")


class _WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMaxNeg5p2vCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Object = MibTableColumn
wwpLeosPortXcvrXfpMaxNeg5p2vCurrent = _WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 86),
    _WwpLeosPortXcvrXfpMaxNeg5p2vCurrent_Type()
)
wwpLeosPortXcvrXfpMaxNeg5p2vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMaxNeg5p2vCurrent.setStatus("current")


class _WwpLeosPortXcvrXfpDiagMonitorType_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpDiagMonitorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpDiagMonitorType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpDiagMonitorType_Object = MibTableColumn
wwpLeosPortXcvrXfpDiagMonitorType = _WwpLeosPortXcvrXfpDiagMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 87),
    _WwpLeosPortXcvrXfpDiagMonitorType_Type()
)
wwpLeosPortXcvrXfpDiagMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpDiagMonitorType.setStatus("current")


class _WwpLeosPortXcvrXfpEnhancedOptions_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpEnhancedOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpEnhancedOptions_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpEnhancedOptions_Object = MibTableColumn
wwpLeosPortXcvrXfpEnhancedOptions = _WwpLeosPortXcvrXfpEnhancedOptions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 88),
    _WwpLeosPortXcvrXfpEnhancedOptions_Type()
)
wwpLeosPortXcvrXfpEnhancedOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpEnhancedOptions.setStatus("current")


class _WwpLeosPortXcvrXfpAuxMonitoringInput1_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpAuxMonitoringInput1 based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("aPDBiasVoltage", 2),
          ("laserTemp", 5),
          ("laserWavelength", 6),
          ("none", 1),
          ("reserved", 3),
          ("tECCurrentMa", 4),
          ("unknown", 15),
          ("voltage1p8V", 9),
          ("voltage1p8VCurrent", 13),
          ("voltage3p3V", 8),
          ("voltage3p3VCurrent", 12),
          ("voltage5V", 7),
          ("voltage5VCurrent", 11),
          ("voltageNeg5p2V", 10),
          ("voltageNeg5p2VCurrent", 14))
    )


_WwpLeosPortXcvrXfpAuxMonitoringInput1_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpAuxMonitoringInput1_Object = MibTableColumn
wwpLeosPortXcvrXfpAuxMonitoringInput1 = _WwpLeosPortXcvrXfpAuxMonitoringInput1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 89),
    _WwpLeosPortXcvrXfpAuxMonitoringInput1_Type()
)
wwpLeosPortXcvrXfpAuxMonitoringInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpAuxMonitoringInput1.setStatus("current")


class _WwpLeosPortXcvrXfpAuxMonitoringInput2_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpAuxMonitoringInput2 based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("aPDBiasVoltage", 2),
          ("laserTemp", 5),
          ("laserWavelength", 6),
          ("none", 1),
          ("reserved", 3),
          ("tECCurrentMa", 4),
          ("unknown", 15),
          ("voltage1p8V", 9),
          ("voltage1p8VCurrent", 13),
          ("voltage3p3V", 8),
          ("voltage3p3VCurrent", 12),
          ("voltage5V", 7),
          ("voltage5VCurrent", 11),
          ("voltageNeg5p2V", 10),
          ("voltageNeg5p2VCurrent", 14))
    )


_WwpLeosPortXcvrXfpAuxMonitoringInput2_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpAuxMonitoringInput2_Object = MibTableColumn
wwpLeosPortXcvrXfpAuxMonitoringInput2 = _WwpLeosPortXcvrXfpAuxMonitoringInput2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 90),
    _WwpLeosPortXcvrXfpAuxMonitoringInput2_Type()
)
wwpLeosPortXcvrXfpAuxMonitoringInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpAuxMonitoringInput2.setStatus("current")


class _WwpLeosPortXcvrAdminFrequency_Type(Unsigned32):
    """Custom type wwpLeosPortXcvrAdminFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwpLeosPortXcvrAdminFrequency_Type.__name__ = "Unsigned32"
_WwpLeosPortXcvrAdminFrequency_Object = MibTableColumn
wwpLeosPortXcvrAdminFrequency = _WwpLeosPortXcvrAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 91),
    _WwpLeosPortXcvrAdminFrequency_Type()
)
wwpLeosPortXcvrAdminFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrAdminFrequency.setStatus("current")


class _WwpLeosPortXcvrXfpLaserFirstFrequency_Type(Unsigned32):
    """Custom type wwpLeosPortXcvrXfpLaserFirstFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwpLeosPortXcvrXfpLaserFirstFrequency_Type.__name__ = "Unsigned32"
_WwpLeosPortXcvrXfpLaserFirstFrequency_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserFirstFrequency = _WwpLeosPortXcvrXfpLaserFirstFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 92),
    _WwpLeosPortXcvrXfpLaserFirstFrequency_Type()
)
wwpLeosPortXcvrXfpLaserFirstFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserFirstFrequency.setStatus("current")


class _WwpLeosPortXcvrXfpLaserLastFrquency_Type(Unsigned32):
    """Custom type wwpLeosPortXcvrXfpLaserLastFrquency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwpLeosPortXcvrXfpLaserLastFrquency_Type.__name__ = "Unsigned32"
_WwpLeosPortXcvrXfpLaserLastFrquency_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserLastFrquency = _WwpLeosPortXcvrXfpLaserLastFrquency_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 93),
    _WwpLeosPortXcvrXfpLaserLastFrquency_Type()
)
wwpLeosPortXcvrXfpLaserLastFrquency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserLastFrquency.setStatus("current")


class _WwpLeosPortXcvrXfpMaxGridScacing_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpMaxGridScacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosPortXcvrXfpMaxGridScacing_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpMaxGridScacing_Object = MibTableColumn
wwpLeosPortXcvrXfpMaxGridScacing = _WwpLeosPortXcvrXfpMaxGridScacing_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 94),
    _WwpLeosPortXcvrXfpMaxGridScacing_Type()
)
wwpLeosPortXcvrXfpMaxGridScacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpMaxGridScacing.setStatus("current")


class _WwpLeosPortXcvrXfpChannelNum_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortXcvrXfpChannelNum_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpChannelNum_Object = MibTableColumn
wwpLeosPortXcvrXfpChannelNum = _WwpLeosPortXcvrXfpChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 95),
    _WwpLeosPortXcvrXfpChannelNum_Type()
)
wwpLeosPortXcvrXfpChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpChannelNum.setStatus("current")


class _WwpLeosPortXcvrXfpFrequencyError_Type(Integer32):
    """Custom type wwpLeosPortXcvrXfpFrequencyError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WwpLeosPortXcvrXfpFrequencyError_Type.__name__ = "Integer32"
_WwpLeosPortXcvrXfpFrequencyError_Object = MibTableColumn
wwpLeosPortXcvrXfpFrequencyError = _WwpLeosPortXcvrXfpFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 96),
    _WwpLeosPortXcvrXfpFrequencyError_Type()
)
wwpLeosPortXcvrXfpFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpFrequencyError.setStatus("current")
_WwpLeosPortXcvrAdminWavelength_Type = Unsigned32
_WwpLeosPortXcvrAdminWavelength_Object = MibTableColumn
wwpLeosPortXcvrAdminWavelength = _WwpLeosPortXcvrAdminWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 97),
    _WwpLeosPortXcvrAdminWavelength_Type()
)
wwpLeosPortXcvrAdminWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrAdminWavelength.setStatus("current")
_WwpLeosPortXcvrAdminChannel_Type = Unsigned32
_WwpLeosPortXcvrAdminChannel_Object = MibTableColumn
wwpLeosPortXcvrAdminChannel = _WwpLeosPortXcvrAdminChannel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 98),
    _WwpLeosPortXcvrAdminChannel_Type()
)
wwpLeosPortXcvrAdminChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrAdminChannel.setStatus("current")
_WwpLeosPortXcvrXfpLaserFirstWavelenth_Type = Unsigned32
_WwpLeosPortXcvrXfpLaserFirstWavelenth_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserFirstWavelenth = _WwpLeosPortXcvrXfpLaserFirstWavelenth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 99),
    _WwpLeosPortXcvrXfpLaserFirstWavelenth_Type()
)
wwpLeosPortXcvrXfpLaserFirstWavelenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserFirstWavelenth.setStatus("current")
_WwpLeosPortXcvrXfpLaserLastWavelength_Type = Unsigned32
_WwpLeosPortXcvrXfpLaserLastWavelength_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserLastWavelength = _WwpLeosPortXcvrXfpLaserLastWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 100),
    _WwpLeosPortXcvrXfpLaserLastWavelength_Type()
)
wwpLeosPortXcvrXfpLaserLastWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserLastWavelength.setStatus("current")
_WwpLeosPortXcvrXfpLaserFirstChannel_Type = Unsigned32
_WwpLeosPortXcvrXfpLaserFirstChannel_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserFirstChannel = _WwpLeosPortXcvrXfpLaserFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 101),
    _WwpLeosPortXcvrXfpLaserFirstChannel_Type()
)
wwpLeosPortXcvrXfpLaserFirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserFirstChannel.setStatus("current")
_WwpLeosPortXcvrXfpLaserLastChannel_Type = Unsigned32
_WwpLeosPortXcvrXfpLaserLastChannel_Object = MibTableColumn
wwpLeosPortXcvrXfpLaserLastChannel = _WwpLeosPortXcvrXfpLaserLastChannel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 102),
    _WwpLeosPortXcvrXfpLaserLastChannel_Type()
)
wwpLeosPortXcvrXfpLaserLastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrXfpLaserLastChannel.setStatus("current")
_WwpLeosPortXcvrOperFrequency_Type = Unsigned32
_WwpLeosPortXcvrOperFrequency_Object = MibTableColumn
wwpLeosPortXcvrOperFrequency = _WwpLeosPortXcvrOperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 103),
    _WwpLeosPortXcvrOperFrequency_Type()
)
wwpLeosPortXcvrOperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrOperFrequency.setStatus("current")
_WwpLeosPortXcvrOperWavelength_Type = Unsigned32
_WwpLeosPortXcvrOperWavelength_Object = MibTableColumn
wwpLeosPortXcvrOperWavelength = _WwpLeosPortXcvrOperWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 104),
    _WwpLeosPortXcvrOperWavelength_Type()
)
wwpLeosPortXcvrOperWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrOperWavelength.setStatus("current")
_WwpLeosPortXcvrRxDbmPower_Type = Integer32
_WwpLeosPortXcvrRxDbmPower_Object = MibTableColumn
wwpLeosPortXcvrRxDbmPower = _WwpLeosPortXcvrRxDbmPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 105),
    _WwpLeosPortXcvrRxDbmPower_Type()
)
wwpLeosPortXcvrRxDbmPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxDbmPower.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxDbmPower.setUnits("dBm")
_WwpLeosPortXcvrTxDbmPower_Type = Integer32
_WwpLeosPortXcvrTxDbmPower_Object = MibTableColumn
wwpLeosPortXcvrTxDbmPower = _WwpLeosPortXcvrTxDbmPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 106),
    _WwpLeosPortXcvrTxDbmPower_Type()
)
wwpLeosPortXcvrTxDbmPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxDbmPower.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxDbmPower.setUnits("dBm")
_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighTxDbmPwAlarmThreshold = _WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 107),
    _WwpLeosPortXcvrHighTxDbmPwAlarmThreshold_Type()
)
wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighTxDbmPwAlarmThreshold.setUnits("dBm")
_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowTxDbmPwAlarmThreshold = _WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 108),
    _WwpLeosPortXcvrLowTxDbmPwAlarmThreshold_Type()
)
wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowTxDbmPwAlarmThreshold.setUnits("dBm")
_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrHighRxDbmPwAlarmThreshold = _WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 109),
    _WwpLeosPortXcvrHighRxDbmPwAlarmThreshold_Type()
)
wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrHighRxDbmPwAlarmThreshold.setUnits("dBm")
_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Type = Integer32
_WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Object = MibTableColumn
wwpLeosPortXcvrLowRxDbmPwAlarmThreshold = _WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 1, 1, 1, 110),
    _WwpLeosPortXcvrLowRxDbmPwAlarmThreshold_Type()
)
wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLowRxDbmPwAlarmThreshold.setUnits("dBm")
_WwpLeosPortXcvrNotif_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrNotif = _WwpLeosPortXcvrNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 2)
)


class _WwpLeosPortXcvrEventType_Type(Integer32):
    """Custom type wwpLeosPortXcvrEventType based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("inserted", 1),
          ("removed", 2))
    )


_WwpLeosPortXcvrEventType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrEventType_Object = MibScalar
wwpLeosPortXcvrEventType = _WwpLeosPortXcvrEventType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 2, 1),
    _WwpLeosPortXcvrEventType_Type()
)
wwpLeosPortXcvrEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrEventType.setStatus("current")


class _WwpLeosPortXcvrErrorType_Type(Integer32):
    """Custom type wwpLeosPortXcvrErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chksumFailed", 1),
          ("none", 0),
          ("opticalFault", 2))
    )


_WwpLeosPortXcvrErrorType_Type.__name__ = "Integer32"
_WwpLeosPortXcvrErrorType_Object = MibScalar
wwpLeosPortXcvrErrorType = _WwpLeosPortXcvrErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 1, 2, 2),
    _WwpLeosPortXcvrErrorType_Type()
)
wwpLeosPortXcvrErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortXcvrErrorType.setStatus("current")
_WwpLeosPortXcvrMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBNotificationPrefix = _WwpLeosPortXcvrMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2)
)
_WwpLeosPortXcvrMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBNotifications = _WwpLeosPortXcvrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0)
)
_WwpLeosPortXcvrMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBConformance = _WwpLeosPortXcvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 3)
)
_WwpLeosPortXcvrMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBCompliances = _WwpLeosPortXcvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 3, 1)
)
_WwpLeosPortXcvrMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosPortXcvrMIBGroups = _WwpLeosPortXcvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosPortXcvrLinkStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 4)
)
wwpLeosPortXcvrLinkStateChangeNotification.setObjects(
      *(("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId"),
        ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrEventType"))
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrLinkStateChangeNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrErrorTypeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 5)
)
wwpLeosPortXcvrErrorTypeNotification.setObjects(
      *(("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId"),
        ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrErrorType"))
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrErrorTypeNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTempHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 6)
)
wwpLeosPortXcvrTempHighNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTempHighNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTempLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 7)
)
wwpLeosPortXcvrTempLowNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTempLowNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTempNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 8)
)
wwpLeosPortXcvrTempNormalNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTempNormalNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrVoltageHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 9)
)
wwpLeosPortXcvrVoltageHighNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVoltageHighNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrVoltageLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 10)
)
wwpLeosPortXcvrVoltageLowNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVoltageLowNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrVoltageNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 11)
)
wwpLeosPortXcvrVoltageNormalNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVoltageNormalNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrBiasHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 12)
)
wwpLeosPortXcvrBiasHighNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBiasHighNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrBiasLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 13)
)
wwpLeosPortXcvrBiasLowNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBiasLowNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrBiasNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 14)
)
wwpLeosPortXcvrBiasNormalNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBiasNormalNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTxPowerHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 15)
)
wwpLeosPortXcvrTxPowerHighNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxPowerHighNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTxPowerLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 16)
)
wwpLeosPortXcvrTxPowerLowNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxPowerLowNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTxPowerNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 17)
)
wwpLeosPortXcvrTxPowerNormalNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxPowerNormalNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrRxPowerHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 18)
)
wwpLeosPortXcvrRxPowerHighNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPowerHighNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrRxPowerLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 19)
)
wwpLeosPortXcvrRxPowerLowNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPowerLowNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrRxPowerNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 20)
)
wwpLeosPortXcvrRxPowerNormalNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPowerNormalNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrSpeedInfoMissingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 21)
)
wwpLeosPortXcvrSpeedInfoMissingNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrSpeedInfoMissingNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrBiasHighWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 22)
)
wwpLeosPortXcvrBiasHighWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBiasHighWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrBiasLowWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 23)
)
wwpLeosPortXcvrBiasLowWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrBiasLowWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTempHighWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 24)
)
wwpLeosPortXcvrTempHighWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTempHighWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTempLowWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 25)
)
wwpLeosPortXcvrTempLowWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTempLowWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrVoltageHighWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 26)
)
wwpLeosPortXcvrVoltageHighWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVoltageHighWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrVoltageLowWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 27)
)
wwpLeosPortXcvrVoltageLowWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrVoltageLowWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTxPowerHighWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 28)
)
wwpLeosPortXcvrTxPowerHighWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxPowerHighWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrTxPowerLowWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 29)
)
wwpLeosPortXcvrTxPowerLowWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrTxPowerLowWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrRxPowerHighWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 30)
)
wwpLeosPortXcvrRxPowerHighWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPowerHighWarningNotification.setStatus(
        "current"
    )

wwpLeosPortXcvrRxPowerLowWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 4, 2, 0, 31)
)
wwpLeosPortXcvrRxPowerLowWarningNotification.setObjects(
    ("WWP-LEOS-PORT-XCVR-MIB", "wwpLeosPortXcvrId")
)
if mibBuilder.loadTexts:
    wwpLeosPortXcvrRxPowerLowWarningNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-PORT-XCVR-MIB",
    **{"wwpLeosPortXcvrMIB": wwpLeosPortXcvrMIB,
       "wwpLeosPortXcvrMIBObjects": wwpLeosPortXcvrMIBObjects,
       "wwpLeosPortXcvr": wwpLeosPortXcvr,
       "wwpLeosPortXcvrTable": wwpLeosPortXcvrTable,
       "wwpLeosPortXcvrEntry": wwpLeosPortXcvrEntry,
       "wwpLeosPortXcvrId": wwpLeosPortXcvrId,
       "wwpLeosPortXcvrOperState": wwpLeosPortXcvrOperState,
       "wwpLeosPortXcvrIdentiferType": wwpLeosPortXcvrIdentiferType,
       "wwpLeosPortXcvrExtIdentiferType": wwpLeosPortXcvrExtIdentiferType,
       "wwpLeosPortXcvrConnectorType": wwpLeosPortXcvrConnectorType,
       "wwpLeosPortXcvrType": wwpLeosPortXcvrType,
       "wwpLeosPortXcvrVendorName": wwpLeosPortXcvrVendorName,
       "wwpLeosPortXcvrVendorOUI": wwpLeosPortXcvrVendorOUI,
       "wwpLeosPortXcvrVendorPN": wwpLeosPortXcvrVendorPN,
       "wwpLeosPortXcvrRevNum": wwpLeosPortXcvrRevNum,
       "wwpLeosPortXcvrSerialNum": wwpLeosPortXcvrSerialNum,
       "wwpLeosPortXcvrEncodingType": wwpLeosPortXcvrEncodingType,
       "wwpLeosPortXcvrMfgDate": wwpLeosPortXcvrMfgDate,
       "wwpLeosPortXcvrComplianceVer": wwpLeosPortXcvrComplianceVer,
       "wwpLeosPortXcvrWaveLength": wwpLeosPortXcvrWaveLength,
       "wwpLeosPortXcvrTemperature": wwpLeosPortXcvrTemperature,
       "wwpLeosPortXcvrVcc": wwpLeosPortXcvrVcc,
       "wwpLeosPortXcvrBias": wwpLeosPortXcvrBias,
       "wwpLeosPortXcvrRxPower": wwpLeosPortXcvrRxPower,
       "wwpLeosPortXcvrTxState": wwpLeosPortXcvrTxState,
       "wwpLeosPortXcvrTxFaultStatus": wwpLeosPortXcvrTxFaultStatus,
       "wwpLeosPortXcvrRxRateStatus": wwpLeosPortXcvrRxRateStatus,
       "wwpLeosPortXcvr9by125um": wwpLeosPortXcvr9by125um,
       "wwpLeosPortXcvr50by125um": wwpLeosPortXcvr50by125um,
       "wwpLeosPortXcvr62dot5by125um": wwpLeosPortXcvr62dot5by125um,
       "wwpLeosPortXcvrCu": wwpLeosPortXcvrCu,
       "wwpLeosPortXcvrTxOutputPw": wwpLeosPortXcvrTxOutputPw,
       "wwpLeosPortXcvrLosState": wwpLeosPortXcvrLosState,
       "wwpLeosPortXcvrDiagSupported": wwpLeosPortXcvrDiagSupported,
       "wwpLeosPortXcvrEnhDiagAlarmSupported": wwpLeosPortXcvrEnhDiagAlarmSupported,
       "wwpLeosPortXcvrEnhDiagSoftTxDisableSupported": wwpLeosPortXcvrEnhDiagSoftTxDisableSupported,
       "wwpLeosPortXcvrEnhDiagSoftTxFaultSupported": wwpLeosPortXcvrEnhDiagSoftTxFaultSupported,
       "wwpLeosPortXcvrEnhDiagRxLosSupported": wwpLeosPortXcvrEnhDiagRxLosSupported,
       "wwpLeosPortXcvrHighTempAlarmThreshold": wwpLeosPortXcvrHighTempAlarmThreshold,
       "wwpLeosPortXcvrLowTempAlarmThreshold": wwpLeosPortXcvrLowTempAlarmThreshold,
       "wwpLeosPortXcvrHighVccAlarmThreshold": wwpLeosPortXcvrHighVccAlarmThreshold,
       "wwpLeosPortXcvrLowVccAlarmThreshold": wwpLeosPortXcvrLowVccAlarmThreshold,
       "wwpLeosPortXcvrHighBiasAlarmThreshold": wwpLeosPortXcvrHighBiasAlarmThreshold,
       "wwpLeosPortXcvrLowBiasAlarmThreshold": wwpLeosPortXcvrLowBiasAlarmThreshold,
       "wwpLeosPortXcvrHighTxPwAlarmThreshold": wwpLeosPortXcvrHighTxPwAlarmThreshold,
       "wwpLeosPortXcvrLowTxPwAlarmThreshold": wwpLeosPortXcvrLowTxPwAlarmThreshold,
       "wwpLeosPortXcvrHighRxPwAlarmThreshold": wwpLeosPortXcvrHighRxPwAlarmThreshold,
       "wwpLeosPortXcvrLowRxPwAlarmThreshold": wwpLeosPortXcvrLowRxPwAlarmThreshold,
       "wwpLeosPortXcvrEnhDiagRateSelectSupported": wwpLeosPortXcvrEnhDiagRateSelectSupported,
       "wwpLeosPortXcvrAdminState": wwpLeosPortXcvrAdminState,
       "wwpLeosPortXcvrXfpMinBitRate": wwpLeosPortXcvrXfpMinBitRate,
       "wwpLeosPortXcvrXfpMaxBitRate": wwpLeosPortXcvrXfpMaxBitRate,
       "wwpLeosPortXcvrXfpLinkLenSmf1km": wwpLeosPortXcvrXfpLinkLenSmf1km,
       "wwpLeosPortXcvrXfpLinkLenE50u2m": wwpLeosPortXcvrXfpLinkLenE50u2m,
       "wwpLeosPortXcvrXfpLinkLen50u1m": wwpLeosPortXcvrXfpLinkLen50u1m,
       "wwpLeosPortXcvrXfpLinkLen62dot5u1m": wwpLeosPortXcvrXfpLinkLen62dot5u1m,
       "wwpLeosPortXcvrXfpLinkLenCopper1m": wwpLeosPortXcvrXfpLinkLenCopper1m,
       "wwpLeosPortXcvrXfpDevTech": wwpLeosPortXcvrXfpDevTech,
       "wwpLeosPortXcvrXfpTransmitterTech": wwpLeosPortXcvrXfpTransmitterTech,
       "wwpLeosPortXcvrXfpCdrSupport": wwpLeosPortXcvrXfpCdrSupport,
       "wwpLeosPortXcvrXfpWaveLengthTol": wwpLeosPortXcvrXfpWaveLengthTol,
       "wwpLeosPortXcvrXfpMaxCaseTemp": wwpLeosPortXcvrXfpMaxCaseTemp,
       "wwpLeosPortXcvrXfpMaxPower": wwpLeosPortXcvrXfpMaxPower,
       "wwpLeosPortXcvrXfpMax5vCurrent": wwpLeosPortXcvrXfpMax5vCurrent,
       "wwpLeosPortXcvrXfpMax3p3vCurrent": wwpLeosPortXcvrXfpMax3p3vCurrent,
       "wwpLeosPortXcvrXfpMax1p8vCurrent": wwpLeosPortXcvrXfpMax1p8vCurrent,
       "wwpLeosPortXcvrXfpMaxNeg5p2vCurrent": wwpLeosPortXcvrXfpMaxNeg5p2vCurrent,
       "wwpLeosPortXcvrXfpDiagMonitorType": wwpLeosPortXcvrXfpDiagMonitorType,
       "wwpLeosPortXcvrXfpEnhancedOptions": wwpLeosPortXcvrXfpEnhancedOptions,
       "wwpLeosPortXcvrXfpAuxMonitoringInput1": wwpLeosPortXcvrXfpAuxMonitoringInput1,
       "wwpLeosPortXcvrXfpAuxMonitoringInput2": wwpLeosPortXcvrXfpAuxMonitoringInput2,
       "wwpLeosPortXcvrAdminFrequency": wwpLeosPortXcvrAdminFrequency,
       "wwpLeosPortXcvrXfpLaserFirstFrequency": wwpLeosPortXcvrXfpLaserFirstFrequency,
       "wwpLeosPortXcvrXfpLaserLastFrquency": wwpLeosPortXcvrXfpLaserLastFrquency,
       "wwpLeosPortXcvrXfpMaxGridScacing": wwpLeosPortXcvrXfpMaxGridScacing,
       "wwpLeosPortXcvrXfpChannelNum": wwpLeosPortXcvrXfpChannelNum,
       "wwpLeosPortXcvrXfpFrequencyError": wwpLeosPortXcvrXfpFrequencyError,
       "wwpLeosPortXcvrAdminWavelength": wwpLeosPortXcvrAdminWavelength,
       "wwpLeosPortXcvrAdminChannel": wwpLeosPortXcvrAdminChannel,
       "wwpLeosPortXcvrXfpLaserFirstWavelenth": wwpLeosPortXcvrXfpLaserFirstWavelenth,
       "wwpLeosPortXcvrXfpLaserLastWavelength": wwpLeosPortXcvrXfpLaserLastWavelength,
       "wwpLeosPortXcvrXfpLaserFirstChannel": wwpLeosPortXcvrXfpLaserFirstChannel,
       "wwpLeosPortXcvrXfpLaserLastChannel": wwpLeosPortXcvrXfpLaserLastChannel,
       "wwpLeosPortXcvrOperFrequency": wwpLeosPortXcvrOperFrequency,
       "wwpLeosPortXcvrOperWavelength": wwpLeosPortXcvrOperWavelength,
       "wwpLeosPortXcvrRxDbmPower": wwpLeosPortXcvrRxDbmPower,
       "wwpLeosPortXcvrTxDbmPower": wwpLeosPortXcvrTxDbmPower,
       "wwpLeosPortXcvrHighTxDbmPwAlarmThreshold": wwpLeosPortXcvrHighTxDbmPwAlarmThreshold,
       "wwpLeosPortXcvrLowTxDbmPwAlarmThreshold": wwpLeosPortXcvrLowTxDbmPwAlarmThreshold,
       "wwpLeosPortXcvrHighRxDbmPwAlarmThreshold": wwpLeosPortXcvrHighRxDbmPwAlarmThreshold,
       "wwpLeosPortXcvrLowRxDbmPwAlarmThreshold": wwpLeosPortXcvrLowRxDbmPwAlarmThreshold,
       "wwpLeosPortXcvrNotif": wwpLeosPortXcvrNotif,
       "wwpLeosPortXcvrEventType": wwpLeosPortXcvrEventType,
       "wwpLeosPortXcvrErrorType": wwpLeosPortXcvrErrorType,
       "wwpLeosPortXcvrMIBNotificationPrefix": wwpLeosPortXcvrMIBNotificationPrefix,
       "wwpLeosPortXcvrMIBNotifications": wwpLeosPortXcvrMIBNotifications,
       "wwpLeosPortXcvrLinkStateChangeNotification": wwpLeosPortXcvrLinkStateChangeNotification,
       "wwpLeosPortXcvrErrorTypeNotification": wwpLeosPortXcvrErrorTypeNotification,
       "wwpLeosPortXcvrTempHighNotification": wwpLeosPortXcvrTempHighNotification,
       "wwpLeosPortXcvrTempLowNotification": wwpLeosPortXcvrTempLowNotification,
       "wwpLeosPortXcvrTempNormalNotification": wwpLeosPortXcvrTempNormalNotification,
       "wwpLeosPortXcvrVoltageHighNotification": wwpLeosPortXcvrVoltageHighNotification,
       "wwpLeosPortXcvrVoltageLowNotification": wwpLeosPortXcvrVoltageLowNotification,
       "wwpLeosPortXcvrVoltageNormalNotification": wwpLeosPortXcvrVoltageNormalNotification,
       "wwpLeosPortXcvrBiasHighNotification": wwpLeosPortXcvrBiasHighNotification,
       "wwpLeosPortXcvrBiasLowNotification": wwpLeosPortXcvrBiasLowNotification,
       "wwpLeosPortXcvrBiasNormalNotification": wwpLeosPortXcvrBiasNormalNotification,
       "wwpLeosPortXcvrTxPowerHighNotification": wwpLeosPortXcvrTxPowerHighNotification,
       "wwpLeosPortXcvrTxPowerLowNotification": wwpLeosPortXcvrTxPowerLowNotification,
       "wwpLeosPortXcvrTxPowerNormalNotification": wwpLeosPortXcvrTxPowerNormalNotification,
       "wwpLeosPortXcvrRxPowerHighNotification": wwpLeosPortXcvrRxPowerHighNotification,
       "wwpLeosPortXcvrRxPowerLowNotification": wwpLeosPortXcvrRxPowerLowNotification,
       "wwpLeosPortXcvrRxPowerNormalNotification": wwpLeosPortXcvrRxPowerNormalNotification,
       "wwpLeosPortXcvrSpeedInfoMissingNotification": wwpLeosPortXcvrSpeedInfoMissingNotification,
       "wwpLeosPortXcvrBiasHighWarningNotification": wwpLeosPortXcvrBiasHighWarningNotification,
       "wwpLeosPortXcvrBiasLowWarningNotification": wwpLeosPortXcvrBiasLowWarningNotification,
       "wwpLeosPortXcvrTempHighWarningNotification": wwpLeosPortXcvrTempHighWarningNotification,
       "wwpLeosPortXcvrTempLowWarningNotification": wwpLeosPortXcvrTempLowWarningNotification,
       "wwpLeosPortXcvrVoltageHighWarningNotification": wwpLeosPortXcvrVoltageHighWarningNotification,
       "wwpLeosPortXcvrVoltageLowWarningNotification": wwpLeosPortXcvrVoltageLowWarningNotification,
       "wwpLeosPortXcvrTxPowerHighWarningNotification": wwpLeosPortXcvrTxPowerHighWarningNotification,
       "wwpLeosPortXcvrTxPowerLowWarningNotification": wwpLeosPortXcvrTxPowerLowWarningNotification,
       "wwpLeosPortXcvrRxPowerHighWarningNotification": wwpLeosPortXcvrRxPowerHighWarningNotification,
       "wwpLeosPortXcvrRxPowerLowWarningNotification": wwpLeosPortXcvrRxPowerLowWarningNotification,
       "wwpLeosPortXcvrMIBConformance": wwpLeosPortXcvrMIBConformance,
       "wwpLeosPortXcvrMIBCompliances": wwpLeosPortXcvrMIBCompliances,
       "wwpLeosPortXcvrMIBGroups": wwpLeosPortXcvrMIBGroups}
)
