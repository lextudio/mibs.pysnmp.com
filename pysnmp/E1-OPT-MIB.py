# SNMP MIB module (E1-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E1-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:00 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysicalPortNumber(Integer32):
    """Custom type PhysicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49, 50),
    )





class VirtualPortNumber(Integer32):
    """Custom type VirtualPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTT1E1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PCTT1E1PortTable = _Cdx6500PCTT1E1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24)
)
_Cdx6500PCTE1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PCTE1PortTable = _Cdx6500PCTE1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2)
)
_Cdx6500PPCTE1PortTable_Object = MibTable
cdx6500PPCTE1PortTable = _Cdx6500PPCTE1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTE1PortTable.setStatus("mandatory")
_Cdx6500PPCTE1PortEntry_Object = MibTableRow
cdx6500PPCTE1PortEntry = _Cdx6500PPCTE1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1)
)
cdx6500PPCTE1PortEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1CfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTE1PortEntry.setStatus("mandatory")
_Cdx6500E1CfgPortNumber_Type = PhysicalPortNumber
_Cdx6500E1CfgPortNumber_Object = MibTableColumn
cdx6500E1CfgPortNumber = _Cdx6500E1CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 1),
    _Cdx6500E1CfgPortNumber_Type()
)
cdx6500E1CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgPortNumber.setStatus("mandatory")


class _Cdx6500E1CfgPortType_Type(Integer32):
    """Custom type cdx6500E1CfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            45
        )
    )
    namedValues = NamedValues(
        ("e1", 45)
    )


_Cdx6500E1CfgPortType_Type.__name__ = "Integer32"
_Cdx6500E1CfgPortType_Object = MibTableColumn
cdx6500E1CfgPortType = _Cdx6500E1CfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 2),
    _Cdx6500E1CfgPortType_Type()
)
cdx6500E1CfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgPortType.setStatus("mandatory")


class _Cdx6500E1CfgFormat_Type(Integer32):
    """Custom type cdx6500E1CfgFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("channelize", 1),
          ("isdn", 2),
          ("nc", 100))
    )


_Cdx6500E1CfgFormat_Type.__name__ = "Integer32"
_Cdx6500E1CfgFormat_Object = MibTableColumn
cdx6500E1CfgFormat = _Cdx6500E1CfgFormat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 3),
    _Cdx6500E1CfgFormat_Type()
)
cdx6500E1CfgFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgFormat.setStatus("mandatory")


class _Cdx6500E1CfgLineFramingType_Type(Integer32):
    """Custom type cdx6500E1CfgLineFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("e1Cas", 6),
          ("e1CasCrc", 5),
          ("e1CasFebe", 4),
          ("e1Ccs", 3),
          ("e1CcsCrc", 2),
          ("e1CcsFebe", 1),
          ("nc", 100))
    )


_Cdx6500E1CfgLineFramingType_Type.__name__ = "Integer32"
_Cdx6500E1CfgLineFramingType_Object = MibTableColumn
cdx6500E1CfgLineFramingType = _Cdx6500E1CfgLineFramingType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 4),
    _Cdx6500E1CfgLineFramingType_Type()
)
cdx6500E1CfgLineFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgLineFramingType.setStatus("mandatory")


class _Cdx6500E1CfgLineCoding_Type(Integer32):
    """Custom type cdx6500E1CfgLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ami", 3),
          ("hdb3", 1),
          ("nc", 100))
    )


_Cdx6500E1CfgLineCoding_Type.__name__ = "Integer32"
_Cdx6500E1CfgLineCoding_Object = MibTableColumn
cdx6500E1CfgLineCoding = _Cdx6500E1CfgLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 5),
    _Cdx6500E1CfgLineCoding_Type()
)
cdx6500E1CfgLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgLineCoding.setStatus("mandatory")


class _Cdx6500E1CfgLineImpedence_Type(Integer32):
    """Custom type cdx6500E1CfgLineImpedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("li120", 1),
          ("li75", 2),
          ("nc", 100))
    )


_Cdx6500E1CfgLineImpedence_Type.__name__ = "Integer32"
_Cdx6500E1CfgLineImpedence_Object = MibTableColumn
cdx6500E1CfgLineImpedence = _Cdx6500E1CfgLineImpedence_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 6),
    _Cdx6500E1CfgLineImpedence_Type()
)
cdx6500E1CfgLineImpedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgLineImpedence.setStatus("mandatory")


class _Cdx6500E1CfgTransmitClock_Type(Integer32):
    """Custom type cdx6500E1CfgTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              129,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("int", 131),
          ("nc", 100),
          ("node", 129),
          ("rec", 130))
    )


_Cdx6500E1CfgTransmitClock_Type.__name__ = "Integer32"
_Cdx6500E1CfgTransmitClock_Object = MibTableColumn
cdx6500E1CfgTransmitClock = _Cdx6500E1CfgTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 7),
    _Cdx6500E1CfgTransmitClock_Type()
)
cdx6500E1CfgTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgTransmitClock.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueLES_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueLES_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueLES_Object = MibTableColumn
cdx6500E1CfgThresholdValueLES = _Cdx6500E1CfgThresholdValueLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 8),
    _Cdx6500E1CfgThresholdValueLES_Type()
)
cdx6500E1CfgThresholdValueLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueLES.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueLCV_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueLCV_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueLCV_Object = MibTableColumn
cdx6500E1CfgThresholdValueLCV = _Cdx6500E1CfgThresholdValueLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 9),
    _Cdx6500E1CfgThresholdValueLCV_Type()
)
cdx6500E1CfgThresholdValueLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueLCV.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValuePCV_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValuePCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValuePCV_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValuePCV_Object = MibTableColumn
cdx6500E1CfgThresholdValuePCV = _Cdx6500E1CfgThresholdValuePCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 10),
    _Cdx6500E1CfgThresholdValuePCV_Type()
)
cdx6500E1CfgThresholdValuePCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValuePCV.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueCSS_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueCSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueCSS_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueCSS_Object = MibTableColumn
cdx6500E1CfgThresholdValueCSS = _Cdx6500E1CfgThresholdValueCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 11),
    _Cdx6500E1CfgThresholdValueCSS_Type()
)
cdx6500E1CfgThresholdValueCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueCSS.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueES_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueES_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueES_Object = MibTableColumn
cdx6500E1CfgThresholdValueES = _Cdx6500E1CfgThresholdValueES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 12),
    _Cdx6500E1CfgThresholdValueES_Type()
)
cdx6500E1CfgThresholdValueES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueES.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueBES_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueBES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueBES_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueBES_Object = MibTableColumn
cdx6500E1CfgThresholdValueBES = _Cdx6500E1CfgThresholdValueBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 13),
    _Cdx6500E1CfgThresholdValueBES_Type()
)
cdx6500E1CfgThresholdValueBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueBES.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueSES_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueSES_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueSES_Object = MibTableColumn
cdx6500E1CfgThresholdValueSES = _Cdx6500E1CfgThresholdValueSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 14),
    _Cdx6500E1CfgThresholdValueSES_Type()
)
cdx6500E1CfgThresholdValueSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueSES.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueSEFS_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueSEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueSEFS_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueSEFS_Object = MibTableColumn
cdx6500E1CfgThresholdValueSEFS = _Cdx6500E1CfgThresholdValueSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 15),
    _Cdx6500E1CfgThresholdValueSEFS_Type()
)
cdx6500E1CfgThresholdValueSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueSEFS.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueUAS_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueUAS_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueUAS_Object = MibTableColumn
cdx6500E1CfgThresholdValueUAS = _Cdx6500E1CfgThresholdValueUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 16),
    _Cdx6500E1CfgThresholdValueUAS_Type()
)
cdx6500E1CfgThresholdValueUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueUAS.setStatus("mandatory")


class _Cdx6500E1CfgThresholdValueDM_Type(Integer32):
    """Custom type cdx6500E1CfgThresholdValueDM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500E1CfgThresholdValueDM_Type.__name__ = "Integer32"
_Cdx6500E1CfgThresholdValueDM_Object = MibTableColumn
cdx6500E1CfgThresholdValueDM = _Cdx6500E1CfgThresholdValueDM_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 17),
    _Cdx6500E1CfgThresholdValueDM_Type()
)
cdx6500E1CfgThresholdValueDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgThresholdValueDM.setStatus("mandatory")


class _Cdx6500E1CfgSwitchType_Type(Integer32):
    """Custom type cdx6500E1CfgSwitchType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("att4ess", 1),
          ("att5ess", 2),
          ("general", 9),
          ("md110", 6),
          ("md110Us", 5),
          ("nc", 100),
          ("ntDms100", 3),
          ("ntDms250", 4),
          ("ntt", 8),
          ("siemens", 7))
    )


_Cdx6500E1CfgSwitchType_Type.__name__ = "Integer32"
_Cdx6500E1CfgSwitchType_Object = MibTableColumn
cdx6500E1CfgSwitchType = _Cdx6500E1CfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 18),
    _Cdx6500E1CfgSwitchType_Type()
)
cdx6500E1CfgSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgSwitchType.setStatus("mandatory")


class _Cdx6500E1CfgVariant_Type(Integer32):
    """Custom type cdx6500E1CfgVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7,
              9,
              10,
              11,
              14,
              100)
        )
    )
    namedValues = NamedValues(
        *(("att", 1),
          ("ccitt", 11),
          ("isdn2", 4),
          ("jate", 5),
          ("nc", 100),
          ("net5", 7),
          ("nt", 2),
          ("oneTr6", 9),
          ("ts014", 14),
          ("vn3", 10))
    )


_Cdx6500E1CfgVariant_Type.__name__ = "Integer32"
_Cdx6500E1CfgVariant_Object = MibTableColumn
cdx6500E1CfgVariant = _Cdx6500E1CfgVariant_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 19),
    _Cdx6500E1CfgVariant_Type()
)
cdx6500E1CfgVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgVariant.setStatus("mandatory")


class _Cdx6500E1CfgUserNetworkSide_Type(Integer32):
    """Custom type cdx6500E1CfgUserNetworkSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("network", 2),
          ("user", 1))
    )


_Cdx6500E1CfgUserNetworkSide_Type.__name__ = "Integer32"
_Cdx6500E1CfgUserNetworkSide_Object = MibTableColumn
cdx6500E1CfgUserNetworkSide = _Cdx6500E1CfgUserNetworkSide_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 20),
    _Cdx6500E1CfgUserNetworkSide_Type()
)
cdx6500E1CfgUserNetworkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgUserNetworkSide.setStatus("mandatory")


class _Cdx6500E1CfgCallingIdMsbState_Type(Integer32):
    """Custom type cdx6500E1CfgCallingIdMsbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500E1CfgCallingIdMsbState_Type.__name__ = "Integer32"
_Cdx6500E1CfgCallingIdMsbState_Object = MibTableColumn
cdx6500E1CfgCallingIdMsbState = _Cdx6500E1CfgCallingIdMsbState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 21),
    _Cdx6500E1CfgCallingIdMsbState_Type()
)
cdx6500E1CfgCallingIdMsbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1CfgCallingIdMsbState.setStatus("mandatory")


class _Cdx6500E1BchannelNumbering_Type(Integer32):
    """Custom type cdx6500E1BchannelNumbering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("oneTo30", 2),
          ("oneTo31", 1))
    )


_Cdx6500E1BchannelNumbering_Type.__name__ = "Integer32"
_Cdx6500E1BchannelNumbering_Object = MibTableColumn
cdx6500E1BchannelNumbering = _Cdx6500E1BchannelNumbering_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 2, 1, 1, 22),
    _Cdx6500E1BchannelNumbering_Type()
)
cdx6500E1BchannelNumbering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1BchannelNumbering.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PSTT1E1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PSTT1E1PortTable = _Cdx6500PSTT1E1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25)
)
_Cdx6500PPSTE1PortTable_Object = MibTable
cdx6500PPSTE1PortTable = _Cdx6500PPSTE1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTE1PortTable.setStatus("mandatory")
_Cdx6500PPSTE1PortEntry_Object = MibTableRow
cdx6500PPSTE1PortEntry = _Cdx6500PPSTE1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1)
)
cdx6500PPSTE1PortEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTE1PortEntry.setStatus("mandatory")
_Cdx6500E1StatPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatPortNumber_Object = MibTableColumn
cdx6500E1StatPortNumber = _Cdx6500E1StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 1),
    _Cdx6500E1StatPortNumber_Type()
)
cdx6500E1StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatPortNumber.setStatus("mandatory")
_Cdx6500E1StatTimeSinceLastResetType_Type = DisplayString
_Cdx6500E1StatTimeSinceLastResetType_Object = MibScalar
cdx6500E1StatTimeSinceLastResetType = _Cdx6500E1StatTimeSinceLastResetType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 2),
    _Cdx6500E1StatTimeSinceLastResetType_Type()
)
cdx6500E1StatTimeSinceLastResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTimeSinceLastResetType.setStatus("mandatory")


class _Cdx6500E1StatPortType_Type(Integer32):
    """Custom type cdx6500E1StatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            45
        )
    )
    namedValues = NamedValues(
        ("e1", 45)
    )


_Cdx6500E1StatPortType_Type.__name__ = "Integer32"
_Cdx6500E1StatPortType_Object = MibTableColumn
cdx6500E1StatPortType = _Cdx6500E1StatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 3),
    _Cdx6500E1StatPortType_Type()
)
cdx6500E1StatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatPortType.setStatus("mandatory")


class _Cdx6500E1StatInterfaceType_Type(Integer32):
    """Custom type cdx6500E1StatInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("it120", 1),
          ("it75", 2),
          ("na", 100))
    )


_Cdx6500E1StatInterfaceType_Type.__name__ = "Integer32"
_Cdx6500E1StatInterfaceType_Object = MibTableColumn
cdx6500E1StatInterfaceType = _Cdx6500E1StatInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 4),
    _Cdx6500E1StatInterfaceType_Type()
)
cdx6500E1StatInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatInterfaceType.setStatus("mandatory")


class _Cdx6500E1StatPortState_Type(Integer32):
    """Custom type cdx6500E1StatPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("na", 100))
    )


_Cdx6500E1StatPortState_Type.__name__ = "Integer32"
_Cdx6500E1StatPortState_Object = MibTableColumn
cdx6500E1StatPortState = _Cdx6500E1StatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 5),
    _Cdx6500E1StatPortState_Type()
)
cdx6500E1StatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatPortState.setStatus("mandatory")


class _Cdx6500E1StatAlarmState_Type(Integer32):
    """Custom type cdx6500E1StatAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ais", 3),
          ("fas", 5),
          ("lof", 6),
          ("los", 4),
          ("na", 100),
          ("none", 1),
          ("rai", 2))
    )


_Cdx6500E1StatAlarmState_Type.__name__ = "Integer32"
_Cdx6500E1StatAlarmState_Object = MibTableColumn
cdx6500E1StatAlarmState = _Cdx6500E1StatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 6),
    _Cdx6500E1StatAlarmState_Type()
)
cdx6500E1StatAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatAlarmState.setStatus("mandatory")
_Cdx6500E1BoardHWRevAndPartNumber_Type = DisplayString
_Cdx6500E1BoardHWRevAndPartNumber_Object = MibTableColumn
cdx6500E1BoardHWRevAndPartNumber = _Cdx6500E1BoardHWRevAndPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 2, 1, 7),
    _Cdx6500E1BoardHWRevAndPartNumber_Type()
)
cdx6500E1BoardHWRevAndPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1BoardHWRevAndPartNumber.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryTable_Object = MibTable
cdx6500E1StatDailyHistoryTable = _Cdx6500E1StatDailyHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4)
)
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryTable.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryEntry_Object = MibTableRow
cdx6500E1StatDailyHistoryEntry = _Cdx6500E1StatDailyHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1)
)
cdx6500E1StatDailyHistoryEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatDailyHistoryPortNumber"),
    (0, "E1-OPT-MIB", "cdx6500E1StatDailyHistoryInterval"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryEntry.setStatus("mandatory")


class _Cdx6500E1StatDailyHistoryInterval_Type(Integer32):
    """Custom type cdx6500E1StatDailyHistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Cdx6500E1StatDailyHistoryInterval_Type.__name__ = "Integer32"
_Cdx6500E1StatDailyHistoryInterval_Object = MibTableColumn
cdx6500E1StatDailyHistoryInterval = _Cdx6500E1StatDailyHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 1),
    _Cdx6500E1StatDailyHistoryInterval_Type()
)
cdx6500E1StatDailyHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryInterval.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryLES_Type = Gauge32
_Cdx6500E1StatDailyHistoryLES_Object = MibTableColumn
cdx6500E1StatDailyHistoryLES = _Cdx6500E1StatDailyHistoryLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 2),
    _Cdx6500E1StatDailyHistoryLES_Type()
)
cdx6500E1StatDailyHistoryLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryLES.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryLCV_Type = Gauge32
_Cdx6500E1StatDailyHistoryLCV_Object = MibTableColumn
cdx6500E1StatDailyHistoryLCV = _Cdx6500E1StatDailyHistoryLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 3),
    _Cdx6500E1StatDailyHistoryLCV_Type()
)
cdx6500E1StatDailyHistoryLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryLCV.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryPCV_Type = Gauge32
_Cdx6500E1StatDailyHistoryPCV_Object = MibTableColumn
cdx6500E1StatDailyHistoryPCV = _Cdx6500E1StatDailyHistoryPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 4),
    _Cdx6500E1StatDailyHistoryPCV_Type()
)
cdx6500E1StatDailyHistoryPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryPCV.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryCSS_Type = Gauge32
_Cdx6500E1StatDailyHistoryCSS_Object = MibTableColumn
cdx6500E1StatDailyHistoryCSS = _Cdx6500E1StatDailyHistoryCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 5),
    _Cdx6500E1StatDailyHistoryCSS_Type()
)
cdx6500E1StatDailyHistoryCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryCSS.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryES_Type = Gauge32
_Cdx6500E1StatDailyHistoryES_Object = MibTableColumn
cdx6500E1StatDailyHistoryES = _Cdx6500E1StatDailyHistoryES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 6),
    _Cdx6500E1StatDailyHistoryES_Type()
)
cdx6500E1StatDailyHistoryES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryES.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryBES_Type = Gauge32
_Cdx6500E1StatDailyHistoryBES_Object = MibTableColumn
cdx6500E1StatDailyHistoryBES = _Cdx6500E1StatDailyHistoryBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 7),
    _Cdx6500E1StatDailyHistoryBES_Type()
)
cdx6500E1StatDailyHistoryBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryBES.setStatus("mandatory")
_Cdx6500E1StatDailyHistorySES_Type = Gauge32
_Cdx6500E1StatDailyHistorySES_Object = MibTableColumn
cdx6500E1StatDailyHistorySES = _Cdx6500E1StatDailyHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 8),
    _Cdx6500E1StatDailyHistorySES_Type()
)
cdx6500E1StatDailyHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistorySES.setStatus("mandatory")
_Cdx6500E1StatDailyHistorySEFS_Type = Gauge32
_Cdx6500E1StatDailyHistorySEFS_Object = MibTableColumn
cdx6500E1StatDailyHistorySEFS = _Cdx6500E1StatDailyHistorySEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 9),
    _Cdx6500E1StatDailyHistorySEFS_Type()
)
cdx6500E1StatDailyHistorySEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistorySEFS.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryUAS_Type = Gauge32
_Cdx6500E1StatDailyHistoryUAS_Object = MibTableColumn
cdx6500E1StatDailyHistoryUAS = _Cdx6500E1StatDailyHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 10),
    _Cdx6500E1StatDailyHistoryUAS_Type()
)
cdx6500E1StatDailyHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryUAS.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryDM_Type = Gauge32
_Cdx6500E1StatDailyHistoryDM_Object = MibTableColumn
cdx6500E1StatDailyHistoryDM = _Cdx6500E1StatDailyHistoryDM_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 11),
    _Cdx6500E1StatDailyHistoryDM_Type()
)
cdx6500E1StatDailyHistoryDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryDM.setStatus("mandatory")
_Cdx6500E1StatDailyHistoryPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatDailyHistoryPortNumber_Object = MibTableColumn
cdx6500E1StatDailyHistoryPortNumber = _Cdx6500E1StatDailyHistoryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 4, 1, 12),
    _Cdx6500E1StatDailyHistoryPortNumber_Type()
)
cdx6500E1StatDailyHistoryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDailyHistoryPortNumber.setStatus("mandatory")
_Cdx6500E1StatABCDStateTable_Object = MibTable
cdx6500E1StatABCDStateTable = _Cdx6500E1StatABCDStateTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6)
)
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStateTable.setStatus("mandatory")
_Cdx6500E1StatABCDStateEntry_Object = MibTableRow
cdx6500E1StatABCDStateEntry = _Cdx6500E1StatABCDStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6, 1)
)
cdx6500E1StatABCDStateEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatABCDStatePortNumber"),
    (0, "E1-OPT-MIB", "cdx6500E1StatABCDStateDS0ChannelNumber"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStateEntry.setStatus("mandatory")


class _Cdx6500E1StatABCDStateDS0ChannelNumber_Type(Integer32):
    """Custom type cdx6500E1StatABCDStateDS0ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500E1StatABCDStateDS0ChannelNumber_Type.__name__ = "Integer32"
_Cdx6500E1StatABCDStateDS0ChannelNumber_Object = MibTableColumn
cdx6500E1StatABCDStateDS0ChannelNumber = _Cdx6500E1StatABCDStateDS0ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6, 1, 1),
    _Cdx6500E1StatABCDStateDS0ChannelNumber_Type()
)
cdx6500E1StatABCDStateDS0ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStateDS0ChannelNumber.setStatus("mandatory")
_Cdx6500E1StatABCDStateCurrentTxState_Type = DisplayString
_Cdx6500E1StatABCDStateCurrentTxState_Object = MibTableColumn
cdx6500E1StatABCDStateCurrentTxState = _Cdx6500E1StatABCDStateCurrentTxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6, 1, 2),
    _Cdx6500E1StatABCDStateCurrentTxState_Type()
)
cdx6500E1StatABCDStateCurrentTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStateCurrentTxState.setStatus("deprecated")
_Cdx6500E1StatABCDStateCurrentRxState_Type = DisplayString
_Cdx6500E1StatABCDStateCurrentRxState_Object = MibTableColumn
cdx6500E1StatABCDStateCurrentRxState = _Cdx6500E1StatABCDStateCurrentRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6, 1, 3),
    _Cdx6500E1StatABCDStateCurrentRxState_Type()
)
cdx6500E1StatABCDStateCurrentRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStateCurrentRxState.setStatus("mandatory")
_Cdx6500E1StatABCDStatePortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatABCDStatePortNumber_Object = MibTableColumn
cdx6500E1StatABCDStatePortNumber = _Cdx6500E1StatABCDStatePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 6, 1, 4),
    _Cdx6500E1StatABCDStatePortNumber_Type()
)
cdx6500E1StatABCDStatePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatABCDStatePortNumber.setStatus("mandatory")
_Cdx6500E1ISDNStatusTable_Object = MibTable
cdx6500E1ISDNStatusTable = _Cdx6500E1ISDNStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8)
)
if mibBuilder.loadTexts:
    cdx6500E1ISDNStatusTable.setStatus("mandatory")
_Cdx6500E1StatISDNStatusEntry_Object = MibTableRow
cdx6500E1StatISDNStatusEntry = _Cdx6500E1StatISDNStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1)
)
cdx6500E1StatISDNStatusEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatISDNStatusPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatISDNStatusEntry.setStatus("mandatory")
_Cdx6500E1StatISDNStatusPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatISDNStatusPortNumber_Object = MibTableColumn
cdx6500E1StatISDNStatusPortNumber = _Cdx6500E1StatISDNStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 1),
    _Cdx6500E1StatISDNStatusPortNumber_Type()
)
cdx6500E1StatISDNStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNStatusPortNumber.setStatus("mandatory")
_Cdx6500E1StatNumRxCallsSinceLastReset_Type = Integer32
_Cdx6500E1StatNumRxCallsSinceLastReset_Object = MibTableColumn
cdx6500E1StatNumRxCallsSinceLastReset = _Cdx6500E1StatNumRxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 2),
    _Cdx6500E1StatNumRxCallsSinceLastReset_Type()
)
cdx6500E1StatNumRxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatNumRxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500E1StatNumRxCallsRejected_Type = Integer32
_Cdx6500E1StatNumRxCallsRejected_Object = MibTableColumn
cdx6500E1StatNumRxCallsRejected = _Cdx6500E1StatNumRxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 3),
    _Cdx6500E1StatNumRxCallsRejected_Type()
)
cdx6500E1StatNumRxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatNumRxCallsRejected.setStatus("mandatory")


class _Cdx6500E1StatRxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500E1StatRxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              255)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("na", 255),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_Cdx6500E1StatRxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500E1StatRxLastCallFailureCause_Object = MibTableColumn
cdx6500E1StatRxLastCallFailureCause = _Cdx6500E1StatRxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 4),
    _Cdx6500E1StatRxLastCallFailureCause_Type()
)
cdx6500E1StatRxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500E1StatRxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500E1StatRxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatRxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatRxLastCalledNumber_Object = MibTableColumn
cdx6500E1StatRxLastCalledNumber = _Cdx6500E1StatRxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 5),
    _Cdx6500E1StatRxLastCalledNumber_Type()
)
cdx6500E1StatRxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxLastCalledNumber.setStatus("mandatory")


class _Cdx6500E1StatRxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500E1StatRxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatRxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatRxLastCallingNumber_Object = MibTableColumn
cdx6500E1StatRxLastCallingNumber = _Cdx6500E1StatRxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 6),
    _Cdx6500E1StatRxLastCallingNumber_Type()
)
cdx6500E1StatRxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxLastCallingNumber.setStatus("mandatory")
_Cdx6500E1StatRxMinCallDuration_Type = DisplayString
_Cdx6500E1StatRxMinCallDuration_Object = MibTableColumn
cdx6500E1StatRxMinCallDuration = _Cdx6500E1StatRxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 7),
    _Cdx6500E1StatRxMinCallDuration_Type()
)
cdx6500E1StatRxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxMinCallDuration.setStatus("mandatory")
_Cdx6500E1StatRxMaxCallDuration_Type = DisplayString
_Cdx6500E1StatRxMaxCallDuration_Object = MibTableColumn
cdx6500E1StatRxMaxCallDuration = _Cdx6500E1StatRxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 8),
    _Cdx6500E1StatRxMaxCallDuration_Type()
)
cdx6500E1StatRxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxMaxCallDuration.setStatus("mandatory")
_Cdx6500E1StatRxAvgCallDuration_Type = DisplayString
_Cdx6500E1StatRxAvgCallDuration_Object = MibTableColumn
cdx6500E1StatRxAvgCallDuration = _Cdx6500E1StatRxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 9),
    _Cdx6500E1StatRxAvgCallDuration_Type()
)
cdx6500E1StatRxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatRxAvgCallDuration.setStatus("mandatory")
_Cdx6500E1StatNumTxCallsSinceLastReset_Type = Integer32
_Cdx6500E1StatNumTxCallsSinceLastReset_Object = MibTableColumn
cdx6500E1StatNumTxCallsSinceLastReset = _Cdx6500E1StatNumTxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 10),
    _Cdx6500E1StatNumTxCallsSinceLastReset_Type()
)
cdx6500E1StatNumTxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatNumTxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500E1StatNumTxCallsRejected_Type = Integer32
_Cdx6500E1StatNumTxCallsRejected_Object = MibTableColumn
cdx6500E1StatNumTxCallsRejected = _Cdx6500E1StatNumTxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 11),
    _Cdx6500E1StatNumTxCallsRejected_Type()
)
cdx6500E1StatNumTxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatNumTxCallsRejected.setStatus("mandatory")


class _Cdx6500E1StatTxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500E1StatTxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              255)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("na", 255),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_Cdx6500E1StatTxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500E1StatTxLastCallFailureCause_Object = MibTableColumn
cdx6500E1StatTxLastCallFailureCause = _Cdx6500E1StatTxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 12),
    _Cdx6500E1StatTxLastCallFailureCause_Type()
)
cdx6500E1StatTxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500E1StatTxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500E1StatTxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatTxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatTxLastCalledNumber_Object = MibTableColumn
cdx6500E1StatTxLastCalledNumber = _Cdx6500E1StatTxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 13),
    _Cdx6500E1StatTxLastCalledNumber_Type()
)
cdx6500E1StatTxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxLastCalledNumber.setStatus("mandatory")


class _Cdx6500E1StatTxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500E1StatTxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatTxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatTxLastCallingNumber_Object = MibTableColumn
cdx6500E1StatTxLastCallingNumber = _Cdx6500E1StatTxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 14),
    _Cdx6500E1StatTxLastCallingNumber_Type()
)
cdx6500E1StatTxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxLastCallingNumber.setStatus("mandatory")
_Cdx6500E1StatTxMinCallDuration_Type = DisplayString
_Cdx6500E1StatTxMinCallDuration_Object = MibTableColumn
cdx6500E1StatTxMinCallDuration = _Cdx6500E1StatTxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 15),
    _Cdx6500E1StatTxMinCallDuration_Type()
)
cdx6500E1StatTxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxMinCallDuration.setStatus("mandatory")
_Cdx6500E1StatTxMaxCallDuration_Type = DisplayString
_Cdx6500E1StatTxMaxCallDuration_Object = MibTableColumn
cdx6500E1StatTxMaxCallDuration = _Cdx6500E1StatTxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 16),
    _Cdx6500E1StatTxMaxCallDuration_Type()
)
cdx6500E1StatTxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxMaxCallDuration.setStatus("mandatory")
_Cdx6500E1StatTxAvgCallDuration_Type = DisplayString
_Cdx6500E1StatTxAvgCallDuration_Object = MibTableColumn
cdx6500E1StatTxAvgCallDuration = _Cdx6500E1StatTxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 17),
    _Cdx6500E1StatTxAvgCallDuration_Type()
)
cdx6500E1StatTxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatTxAvgCallDuration.setStatus("mandatory")


class _Cdx6500E1StatDchannelState_Type(Integer32):
    """Custom type cdx6500E1StatDchannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("na", 100),
          ("up", 1))
    )


_Cdx6500E1StatDchannelState_Type.__name__ = "Integer32"
_Cdx6500E1StatDchannelState_Object = MibTableColumn
cdx6500E1StatDchannelState = _Cdx6500E1StatDchannelState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 8, 1, 18),
    _Cdx6500E1StatDchannelState_Type()
)
cdx6500E1StatDchannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatDchannelState.setStatus("mandatory")
_Cdx6500E1StatISDNCallSummaryTable_Object = MibTable
cdx6500E1StatISDNCallSummaryTable = _Cdx6500E1StatISDNCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10)
)
if mibBuilder.loadTexts:
    cdx6500E1StatISDNCallSummaryTable.setStatus("mandatory")
_Cdx6500E1StatISDNCallSummaryEntry_Object = MibTableRow
cdx6500E1StatISDNCallSummaryEntry = _Cdx6500E1StatISDNCallSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1)
)
cdx6500E1StatISDNCallSummaryEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatISDNPortNumber"),
    (0, "E1-OPT-MIB", "cdx6500E1StatISDNBChannelNumber"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatISDNCallSummaryEntry.setStatus("mandatory")


class _Cdx6500E1StatISDNBChannelNumber_Type(Integer32):
    """Custom type cdx6500E1StatISDNBChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Cdx6500E1StatISDNBChannelNumber_Type.__name__ = "Integer32"
_Cdx6500E1StatISDNBChannelNumber_Object = MibTableColumn
cdx6500E1StatISDNBChannelNumber = _Cdx6500E1StatISDNBChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 1),
    _Cdx6500E1StatISDNBChannelNumber_Type()
)
cdx6500E1StatISDNBChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNBChannelNumber.setStatus("mandatory")


class _Cdx6500E1StatISDNBChannelStatus_Type(Integer32):
    """Custom type cdx6500E1StatISDNBChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("idle", 1),
          ("na", 100),
          ("outOfService", 4),
          ("ringing", 2))
    )


_Cdx6500E1StatISDNBChannelStatus_Type.__name__ = "Integer32"
_Cdx6500E1StatISDNBChannelStatus_Object = MibTableColumn
cdx6500E1StatISDNBChannelStatus = _Cdx6500E1StatISDNBChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 2),
    _Cdx6500E1StatISDNBChannelStatus_Type()
)
cdx6500E1StatISDNBChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNBChannelStatus.setStatus("mandatory")


class _Cdx6500E1StatISDNCallDirection_Type(Integer32):
    """Custom type cdx6500E1StatISDNCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("invalid", 3),
          ("na", 100),
          ("outbound", 2))
    )


_Cdx6500E1StatISDNCallDirection_Type.__name__ = "Integer32"
_Cdx6500E1StatISDNCallDirection_Object = MibTableColumn
cdx6500E1StatISDNCallDirection = _Cdx6500E1StatISDNCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 3),
    _Cdx6500E1StatISDNCallDirection_Type()
)
cdx6500E1StatISDNCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNCallDirection.setStatus("mandatory")


class _Cdx6500E1StatISDNCallingNumber_Type(DisplayString):
    """Custom type cdx6500E1StatISDNCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatISDNCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatISDNCallingNumber_Object = MibTableColumn
cdx6500E1StatISDNCallingNumber = _Cdx6500E1StatISDNCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 4),
    _Cdx6500E1StatISDNCallingNumber_Type()
)
cdx6500E1StatISDNCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNCallingNumber.setStatus("mandatory")


class _Cdx6500E1StatISDNCalledNumber_Type(DisplayString):
    """Custom type cdx6500E1StatISDNCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500E1StatISDNCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500E1StatISDNCalledNumber_Object = MibTableColumn
cdx6500E1StatISDNCalledNumber = _Cdx6500E1StatISDNCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 5),
    _Cdx6500E1StatISDNCalledNumber_Type()
)
cdx6500E1StatISDNCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNCalledNumber.setStatus("mandatory")


class _Cdx6500E1StatISDNDS0Rate_Type(Integer32):
    """Custom type cdx6500E1StatISDNDS0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ds056k", 1),
          ("ds064k", 2),
          ("na", 100))
    )


_Cdx6500E1StatISDNDS0Rate_Type.__name__ = "Integer32"
_Cdx6500E1StatISDNDS0Rate_Object = MibTableColumn
cdx6500E1StatISDNDS0Rate = _Cdx6500E1StatISDNDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 6),
    _Cdx6500E1StatISDNDS0Rate_Type()
)
cdx6500E1StatISDNDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNDS0Rate.setStatus("mandatory")
_Cdx6500E1StatISDNVirtualPortNumber_Type = Integer32
_Cdx6500E1StatISDNVirtualPortNumber_Object = MibTableColumn
cdx6500E1StatISDNVirtualPortNumber = _Cdx6500E1StatISDNVirtualPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 7),
    _Cdx6500E1StatISDNVirtualPortNumber_Type()
)
cdx6500E1StatISDNVirtualPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNVirtualPortNumber.setStatus("mandatory")
_Cdx6500E1StatISDNTimeCallStarted_Type = DisplayString
_Cdx6500E1StatISDNTimeCallStarted_Object = MibTableColumn
cdx6500E1StatISDNTimeCallStarted = _Cdx6500E1StatISDNTimeCallStarted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 8),
    _Cdx6500E1StatISDNTimeCallStarted_Type()
)
cdx6500E1StatISDNTimeCallStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNTimeCallStarted.setStatus("mandatory")
_Cdx6500E1StatISDNPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatISDNPortNumber_Object = MibTableColumn
cdx6500E1StatISDNPortNumber = _Cdx6500E1StatISDNPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 10, 1, 9),
    _Cdx6500E1StatISDNPortNumber_Type()
)
cdx6500E1StatISDNPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatISDNPortNumber.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportTable_Object = MibTable
cdx6500E1StatLast24HoursReportTable = _Cdx6500E1StatLast24HoursReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12)
)
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportTable.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportEntry_Object = MibTableRow
cdx6500E1StatLast24HoursReportEntry = _Cdx6500E1StatLast24HoursReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1)
)
cdx6500E1StatLast24HoursReportEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatLast24HoursReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportEntry.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatLast24HoursReportPortNumber_Object = MibTableColumn
cdx6500E1StatLast24HoursReportPortNumber = _Cdx6500E1StatLast24HoursReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 1),
    _Cdx6500E1StatLast24HoursReportPortNumber_Type()
)
cdx6500E1StatLast24HoursReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportPortNumber.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportLES_Type = Gauge32
_Cdx6500E1StatLast24HoursReportLES_Object = MibTableColumn
cdx6500E1StatLast24HoursReportLES = _Cdx6500E1StatLast24HoursReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 2),
    _Cdx6500E1StatLast24HoursReportLES_Type()
)
cdx6500E1StatLast24HoursReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportLES.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportLCV_Type = Gauge32
_Cdx6500E1StatLast24HoursReportLCV_Object = MibTableColumn
cdx6500E1StatLast24HoursReportLCV = _Cdx6500E1StatLast24HoursReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 3),
    _Cdx6500E1StatLast24HoursReportLCV_Type()
)
cdx6500E1StatLast24HoursReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportLCV.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportPCV_Type = Gauge32
_Cdx6500E1StatLast24HoursReportPCV_Object = MibTableColumn
cdx6500E1StatLast24HoursReportPCV = _Cdx6500E1StatLast24HoursReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 4),
    _Cdx6500E1StatLast24HoursReportPCV_Type()
)
cdx6500E1StatLast24HoursReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportPCV.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportCSS_Type = Gauge32
_Cdx6500E1StatLast24HoursReportCSS_Object = MibTableColumn
cdx6500E1StatLast24HoursReportCSS = _Cdx6500E1StatLast24HoursReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 5),
    _Cdx6500E1StatLast24HoursReportCSS_Type()
)
cdx6500E1StatLast24HoursReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportCSS.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportES_Type = Gauge32
_Cdx6500E1StatLast24HoursReportES_Object = MibTableColumn
cdx6500E1StatLast24HoursReportES = _Cdx6500E1StatLast24HoursReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 6),
    _Cdx6500E1StatLast24HoursReportES_Type()
)
cdx6500E1StatLast24HoursReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportES.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportBES_Type = Gauge32
_Cdx6500E1StatLast24HoursReportBES_Object = MibTableColumn
cdx6500E1StatLast24HoursReportBES = _Cdx6500E1StatLast24HoursReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 7),
    _Cdx6500E1StatLast24HoursReportBES_Type()
)
cdx6500E1StatLast24HoursReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportBES.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportSES_Type = Gauge32
_Cdx6500E1StatLast24HoursReportSES_Object = MibTableColumn
cdx6500E1StatLast24HoursReportSES = _Cdx6500E1StatLast24HoursReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 8),
    _Cdx6500E1StatLast24HoursReportSES_Type()
)
cdx6500E1StatLast24HoursReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportSES.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportSEFS_Type = Gauge32
_Cdx6500E1StatLast24HoursReportSEFS_Object = MibTableColumn
cdx6500E1StatLast24HoursReportSEFS = _Cdx6500E1StatLast24HoursReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 9),
    _Cdx6500E1StatLast24HoursReportSEFS_Type()
)
cdx6500E1StatLast24HoursReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportSEFS.setStatus("mandatory")
_Cdx6500E1StatLast24HoursReportUAS_Type = Gauge32
_Cdx6500E1StatLast24HoursReportUAS_Object = MibTableColumn
cdx6500E1StatLast24HoursReportUAS = _Cdx6500E1StatLast24HoursReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 12, 1, 10),
    _Cdx6500E1StatLast24HoursReportUAS_Type()
)
cdx6500E1StatLast24HoursReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatLast24HoursReportUAS.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportTable_Object = MibTable
cdx6500E1StatCurrent15MinutesReportTable = _Cdx6500E1StatCurrent15MinutesReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14)
)
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportTable.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportEntry_Object = MibTableRow
cdx6500E1StatCurrent15MinutesReportEntry = _Cdx6500E1StatCurrent15MinutesReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1)
)
cdx6500E1StatCurrent15MinutesReportEntry.setIndexNames(
    (0, "E1-OPT-MIB", "cdx6500E1StatCurrent15MinutesReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportEntry.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportPortNumber_Type = PhysicalPortNumber
_Cdx6500E1StatCurrent15MinutesReportPortNumber_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportPortNumber = _Cdx6500E1StatCurrent15MinutesReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 1),
    _Cdx6500E1StatCurrent15MinutesReportPortNumber_Type()
)
cdx6500E1StatCurrent15MinutesReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportPortNumber.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportTimeElapsed_Type = DisplayString
_Cdx6500E1StatCurrent15MinutesReportTimeElapsed_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportTimeElapsed = _Cdx6500E1StatCurrent15MinutesReportTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 2),
    _Cdx6500E1StatCurrent15MinutesReportTimeElapsed_Type()
)
cdx6500E1StatCurrent15MinutesReportTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportTimeElapsed.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportLES_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportLES_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportLES = _Cdx6500E1StatCurrent15MinutesReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 3),
    _Cdx6500E1StatCurrent15MinutesReportLES_Type()
)
cdx6500E1StatCurrent15MinutesReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportLES.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportLCV_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportLCV_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportLCV = _Cdx6500E1StatCurrent15MinutesReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 4),
    _Cdx6500E1StatCurrent15MinutesReportLCV_Type()
)
cdx6500E1StatCurrent15MinutesReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportLCV.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportPCV_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportPCV_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportPCV = _Cdx6500E1StatCurrent15MinutesReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 5),
    _Cdx6500E1StatCurrent15MinutesReportPCV_Type()
)
cdx6500E1StatCurrent15MinutesReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportPCV.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportCSS_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportCSS_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportCSS = _Cdx6500E1StatCurrent15MinutesReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 6),
    _Cdx6500E1StatCurrent15MinutesReportCSS_Type()
)
cdx6500E1StatCurrent15MinutesReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportCSS.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportES_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportES_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportES = _Cdx6500E1StatCurrent15MinutesReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 7),
    _Cdx6500E1StatCurrent15MinutesReportES_Type()
)
cdx6500E1StatCurrent15MinutesReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportES.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportBES_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportBES_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportBES = _Cdx6500E1StatCurrent15MinutesReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 8),
    _Cdx6500E1StatCurrent15MinutesReportBES_Type()
)
cdx6500E1StatCurrent15MinutesReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportBES.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportSES_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportSES_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportSES = _Cdx6500E1StatCurrent15MinutesReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 9),
    _Cdx6500E1StatCurrent15MinutesReportSES_Type()
)
cdx6500E1StatCurrent15MinutesReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportSES.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportSEFS_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportSEFS_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportSEFS = _Cdx6500E1StatCurrent15MinutesReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 10),
    _Cdx6500E1StatCurrent15MinutesReportSEFS_Type()
)
cdx6500E1StatCurrent15MinutesReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportSEFS.setStatus("mandatory")
_Cdx6500E1StatCurrent15MinutesReportUAS_Type = Gauge32
_Cdx6500E1StatCurrent15MinutesReportUAS_Object = MibTableColumn
cdx6500E1StatCurrent15MinutesReportUAS = _Cdx6500E1StatCurrent15MinutesReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 14, 1, 11),
    _Cdx6500E1StatCurrent15MinutesReportUAS_Type()
)
cdx6500E1StatCurrent15MinutesReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500E1StatCurrent15MinutesReportUAS.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E1-OPT-MIB",
    **{"DisplayString": DisplayString,
       "PhysicalPortNumber": PhysicalPortNumber,
       "VirtualPortNumber": VirtualPortNumber,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTT1E1PortTable": cdx6500PCTT1E1PortTable,
       "cdx6500PCTE1PortTable": cdx6500PCTE1PortTable,
       "cdx6500PPCTE1PortTable": cdx6500PPCTE1PortTable,
       "cdx6500PPCTE1PortEntry": cdx6500PPCTE1PortEntry,
       "cdx6500E1CfgPortNumber": cdx6500E1CfgPortNumber,
       "cdx6500E1CfgPortType": cdx6500E1CfgPortType,
       "cdx6500E1CfgFormat": cdx6500E1CfgFormat,
       "cdx6500E1CfgLineFramingType": cdx6500E1CfgLineFramingType,
       "cdx6500E1CfgLineCoding": cdx6500E1CfgLineCoding,
       "cdx6500E1CfgLineImpedence": cdx6500E1CfgLineImpedence,
       "cdx6500E1CfgTransmitClock": cdx6500E1CfgTransmitClock,
       "cdx6500E1CfgThresholdValueLES": cdx6500E1CfgThresholdValueLES,
       "cdx6500E1CfgThresholdValueLCV": cdx6500E1CfgThresholdValueLCV,
       "cdx6500E1CfgThresholdValuePCV": cdx6500E1CfgThresholdValuePCV,
       "cdx6500E1CfgThresholdValueCSS": cdx6500E1CfgThresholdValueCSS,
       "cdx6500E1CfgThresholdValueES": cdx6500E1CfgThresholdValueES,
       "cdx6500E1CfgThresholdValueBES": cdx6500E1CfgThresholdValueBES,
       "cdx6500E1CfgThresholdValueSES": cdx6500E1CfgThresholdValueSES,
       "cdx6500E1CfgThresholdValueSEFS": cdx6500E1CfgThresholdValueSEFS,
       "cdx6500E1CfgThresholdValueUAS": cdx6500E1CfgThresholdValueUAS,
       "cdx6500E1CfgThresholdValueDM": cdx6500E1CfgThresholdValueDM,
       "cdx6500E1CfgSwitchType": cdx6500E1CfgSwitchType,
       "cdx6500E1CfgVariant": cdx6500E1CfgVariant,
       "cdx6500E1CfgUserNetworkSide": cdx6500E1CfgUserNetworkSide,
       "cdx6500E1CfgCallingIdMsbState": cdx6500E1CfgCallingIdMsbState,
       "cdx6500E1BchannelNumbering": cdx6500E1BchannelNumbering,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTT1E1PortTable": cdx6500PSTT1E1PortTable,
       "cdx6500PPSTE1PortTable": cdx6500PPSTE1PortTable,
       "cdx6500PPSTE1PortEntry": cdx6500PPSTE1PortEntry,
       "cdx6500E1StatPortNumber": cdx6500E1StatPortNumber,
       "cdx6500E1StatTimeSinceLastResetType": cdx6500E1StatTimeSinceLastResetType,
       "cdx6500E1StatPortType": cdx6500E1StatPortType,
       "cdx6500E1StatInterfaceType": cdx6500E1StatInterfaceType,
       "cdx6500E1StatPortState": cdx6500E1StatPortState,
       "cdx6500E1StatAlarmState": cdx6500E1StatAlarmState,
       "cdx6500E1BoardHWRevAndPartNumber": cdx6500E1BoardHWRevAndPartNumber,
       "cdx6500E1StatDailyHistoryTable": cdx6500E1StatDailyHistoryTable,
       "cdx6500E1StatDailyHistoryEntry": cdx6500E1StatDailyHistoryEntry,
       "cdx6500E1StatDailyHistoryInterval": cdx6500E1StatDailyHistoryInterval,
       "cdx6500E1StatDailyHistoryLES": cdx6500E1StatDailyHistoryLES,
       "cdx6500E1StatDailyHistoryLCV": cdx6500E1StatDailyHistoryLCV,
       "cdx6500E1StatDailyHistoryPCV": cdx6500E1StatDailyHistoryPCV,
       "cdx6500E1StatDailyHistoryCSS": cdx6500E1StatDailyHistoryCSS,
       "cdx6500E1StatDailyHistoryES": cdx6500E1StatDailyHistoryES,
       "cdx6500E1StatDailyHistoryBES": cdx6500E1StatDailyHistoryBES,
       "cdx6500E1StatDailyHistorySES": cdx6500E1StatDailyHistorySES,
       "cdx6500E1StatDailyHistorySEFS": cdx6500E1StatDailyHistorySEFS,
       "cdx6500E1StatDailyHistoryUAS": cdx6500E1StatDailyHistoryUAS,
       "cdx6500E1StatDailyHistoryDM": cdx6500E1StatDailyHistoryDM,
       "cdx6500E1StatDailyHistoryPortNumber": cdx6500E1StatDailyHistoryPortNumber,
       "cdx6500E1StatABCDStateTable": cdx6500E1StatABCDStateTable,
       "cdx6500E1StatABCDStateEntry": cdx6500E1StatABCDStateEntry,
       "cdx6500E1StatABCDStateDS0ChannelNumber": cdx6500E1StatABCDStateDS0ChannelNumber,
       "cdx6500E1StatABCDStateCurrentTxState": cdx6500E1StatABCDStateCurrentTxState,
       "cdx6500E1StatABCDStateCurrentRxState": cdx6500E1StatABCDStateCurrentRxState,
       "cdx6500E1StatABCDStatePortNumber": cdx6500E1StatABCDStatePortNumber,
       "cdx6500E1ISDNStatusTable": cdx6500E1ISDNStatusTable,
       "cdx6500E1StatISDNStatusEntry": cdx6500E1StatISDNStatusEntry,
       "cdx6500E1StatISDNStatusPortNumber": cdx6500E1StatISDNStatusPortNumber,
       "cdx6500E1StatNumRxCallsSinceLastReset": cdx6500E1StatNumRxCallsSinceLastReset,
       "cdx6500E1StatNumRxCallsRejected": cdx6500E1StatNumRxCallsRejected,
       "cdx6500E1StatRxLastCallFailureCause": cdx6500E1StatRxLastCallFailureCause,
       "cdx6500E1StatRxLastCalledNumber": cdx6500E1StatRxLastCalledNumber,
       "cdx6500E1StatRxLastCallingNumber": cdx6500E1StatRxLastCallingNumber,
       "cdx6500E1StatRxMinCallDuration": cdx6500E1StatRxMinCallDuration,
       "cdx6500E1StatRxMaxCallDuration": cdx6500E1StatRxMaxCallDuration,
       "cdx6500E1StatRxAvgCallDuration": cdx6500E1StatRxAvgCallDuration,
       "cdx6500E1StatNumTxCallsSinceLastReset": cdx6500E1StatNumTxCallsSinceLastReset,
       "cdx6500E1StatNumTxCallsRejected": cdx6500E1StatNumTxCallsRejected,
       "cdx6500E1StatTxLastCallFailureCause": cdx6500E1StatTxLastCallFailureCause,
       "cdx6500E1StatTxLastCalledNumber": cdx6500E1StatTxLastCalledNumber,
       "cdx6500E1StatTxLastCallingNumber": cdx6500E1StatTxLastCallingNumber,
       "cdx6500E1StatTxMinCallDuration": cdx6500E1StatTxMinCallDuration,
       "cdx6500E1StatTxMaxCallDuration": cdx6500E1StatTxMaxCallDuration,
       "cdx6500E1StatTxAvgCallDuration": cdx6500E1StatTxAvgCallDuration,
       "cdx6500E1StatDchannelState": cdx6500E1StatDchannelState,
       "cdx6500E1StatISDNCallSummaryTable": cdx6500E1StatISDNCallSummaryTable,
       "cdx6500E1StatISDNCallSummaryEntry": cdx6500E1StatISDNCallSummaryEntry,
       "cdx6500E1StatISDNBChannelNumber": cdx6500E1StatISDNBChannelNumber,
       "cdx6500E1StatISDNBChannelStatus": cdx6500E1StatISDNBChannelStatus,
       "cdx6500E1StatISDNCallDirection": cdx6500E1StatISDNCallDirection,
       "cdx6500E1StatISDNCallingNumber": cdx6500E1StatISDNCallingNumber,
       "cdx6500E1StatISDNCalledNumber": cdx6500E1StatISDNCalledNumber,
       "cdx6500E1StatISDNDS0Rate": cdx6500E1StatISDNDS0Rate,
       "cdx6500E1StatISDNVirtualPortNumber": cdx6500E1StatISDNVirtualPortNumber,
       "cdx6500E1StatISDNTimeCallStarted": cdx6500E1StatISDNTimeCallStarted,
       "cdx6500E1StatISDNPortNumber": cdx6500E1StatISDNPortNumber,
       "cdx6500E1StatLast24HoursReportTable": cdx6500E1StatLast24HoursReportTable,
       "cdx6500E1StatLast24HoursReportEntry": cdx6500E1StatLast24HoursReportEntry,
       "cdx6500E1StatLast24HoursReportPortNumber": cdx6500E1StatLast24HoursReportPortNumber,
       "cdx6500E1StatLast24HoursReportLES": cdx6500E1StatLast24HoursReportLES,
       "cdx6500E1StatLast24HoursReportLCV": cdx6500E1StatLast24HoursReportLCV,
       "cdx6500E1StatLast24HoursReportPCV": cdx6500E1StatLast24HoursReportPCV,
       "cdx6500E1StatLast24HoursReportCSS": cdx6500E1StatLast24HoursReportCSS,
       "cdx6500E1StatLast24HoursReportES": cdx6500E1StatLast24HoursReportES,
       "cdx6500E1StatLast24HoursReportBES": cdx6500E1StatLast24HoursReportBES,
       "cdx6500E1StatLast24HoursReportSES": cdx6500E1StatLast24HoursReportSES,
       "cdx6500E1StatLast24HoursReportSEFS": cdx6500E1StatLast24HoursReportSEFS,
       "cdx6500E1StatLast24HoursReportUAS": cdx6500E1StatLast24HoursReportUAS,
       "cdx6500E1StatCurrent15MinutesReportTable": cdx6500E1StatCurrent15MinutesReportTable,
       "cdx6500E1StatCurrent15MinutesReportEntry": cdx6500E1StatCurrent15MinutesReportEntry,
       "cdx6500E1StatCurrent15MinutesReportPortNumber": cdx6500E1StatCurrent15MinutesReportPortNumber,
       "cdx6500E1StatCurrent15MinutesReportTimeElapsed": cdx6500E1StatCurrent15MinutesReportTimeElapsed,
       "cdx6500E1StatCurrent15MinutesReportLES": cdx6500E1StatCurrent15MinutesReportLES,
       "cdx6500E1StatCurrent15MinutesReportLCV": cdx6500E1StatCurrent15MinutesReportLCV,
       "cdx6500E1StatCurrent15MinutesReportPCV": cdx6500E1StatCurrent15MinutesReportPCV,
       "cdx6500E1StatCurrent15MinutesReportCSS": cdx6500E1StatCurrent15MinutesReportCSS,
       "cdx6500E1StatCurrent15MinutesReportES": cdx6500E1StatCurrent15MinutesReportES,
       "cdx6500E1StatCurrent15MinutesReportBES": cdx6500E1StatCurrent15MinutesReportBES,
       "cdx6500E1StatCurrent15MinutesReportSES": cdx6500E1StatCurrent15MinutesReportSES,
       "cdx6500E1StatCurrent15MinutesReportSEFS": cdx6500E1StatCurrent15MinutesReportSEFS,
       "cdx6500E1StatCurrent15MinutesReportUAS": cdx6500E1StatCurrent15MinutesReportUAS}
)
