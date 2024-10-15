# SNMP MIB module (T1-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T1-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:25 2024
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
_Cdx6500PCTT1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PCTT1PortTable = _Cdx6500PCTT1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1)
)
_Cdx6500PPCTT1PortTable_Object = MibTable
cdx6500PPCTT1PortTable = _Cdx6500PPCTT1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTT1PortTable.setStatus("mandatory")
_Cdx6500PPCTT1PortEntry_Object = MibTable
cdx6500PPCTT1PortEntry = _Cdx6500PPCTT1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTT1PortEntry.setStatus("mandatory")
_Cdx6500T1CfgPortNumber_Type = PhysicalPortNumber
_Cdx6500T1CfgPortNumber_Object = MibTableColumn
cdx6500T1CfgPortNumber = _Cdx6500T1CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 1),
    _Cdx6500T1CfgPortNumber_Type()
)
cdx6500T1CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgPortNumber.setStatus("mandatory")


class _Cdx6500T1CfgPortType_Type(Integer32):
    """Custom type cdx6500T1CfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            44
        )
    )
    namedValues = NamedValues(
        ("t1", 44)
    )


_Cdx6500T1CfgPortType_Type.__name__ = "Integer32"
_Cdx6500T1CfgPortType_Object = MibTableColumn
cdx6500T1CfgPortType = _Cdx6500T1CfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 2),
    _Cdx6500T1CfgPortType_Type()
)
cdx6500T1CfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgPortType.setStatus("mandatory")


class _Cdx6500T1CfgFormat_Type(Integer32):
    """Custom type cdx6500T1CfgFormat based on Integer32"""
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


_Cdx6500T1CfgFormat_Type.__name__ = "Integer32"
_Cdx6500T1CfgFormat_Object = MibTableColumn
cdx6500T1CfgFormat = _Cdx6500T1CfgFormat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 3),
    _Cdx6500T1CfgFormat_Type()
)
cdx6500T1CfgFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgFormat.setStatus("mandatory")


class _Cdx6500T1CfgLineFramingType_Type(Integer32):
    """Custom type cdx6500T1CfgLineFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("esf", 1),
          ("nc", 100),
          ("sf", 4))
    )


_Cdx6500T1CfgLineFramingType_Type.__name__ = "Integer32"
_Cdx6500T1CfgLineFramingType_Object = MibTableColumn
cdx6500T1CfgLineFramingType = _Cdx6500T1CfgLineFramingType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 4),
    _Cdx6500T1CfgLineFramingType_Type()
)
cdx6500T1CfgLineFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgLineFramingType.setStatus("mandatory")


class _Cdx6500T1CfgLineCoding_Type(Integer32):
    """Custom type cdx6500T1CfgLineCoding based on Integer32"""
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
        *(("ami", 3),
          ("b7zs", 2),
          ("b8zs", 1),
          ("nc", 100))
    )


_Cdx6500T1CfgLineCoding_Type.__name__ = "Integer32"
_Cdx6500T1CfgLineCoding_Object = MibTableColumn
cdx6500T1CfgLineCoding = _Cdx6500T1CfgLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 5),
    _Cdx6500T1CfgLineCoding_Type()
)
cdx6500T1CfgLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgLineCoding.setStatus("mandatory")


class _Cdx6500T1CfgTransmitClock_Type(Integer32):
    """Custom type cdx6500T1CfgTransmitClock based on Integer32"""
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


_Cdx6500T1CfgTransmitClock_Type.__name__ = "Integer32"
_Cdx6500T1CfgTransmitClock_Object = MibTableColumn
cdx6500T1CfgTransmitClock = _Cdx6500T1CfgTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 6),
    _Cdx6500T1CfgTransmitClock_Type()
)
cdx6500T1CfgTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgTransmitClock.setStatus("mandatory")


class _Cdx6500T1CfgLineBuildOut_Type(Integer32):
    """Custom type cdx6500T1CfgLineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("lbo0", 1),
          ("lbo1", 2),
          ("lbo2", 3),
          ("lbo3", 4),
          ("lbo4", 5),
          ("nc", 100))
    )


_Cdx6500T1CfgLineBuildOut_Type.__name__ = "Integer32"
_Cdx6500T1CfgLineBuildOut_Object = MibTableColumn
cdx6500T1CfgLineBuildOut = _Cdx6500T1CfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 7),
    _Cdx6500T1CfgLineBuildOut_Type()
)
cdx6500T1CfgLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgLineBuildOut.setStatus("mandatory")


class _Cdx6500T1CfgFacilityDataLink_Type(Integer32):
    """Custom type cdx6500T1CfgFacilityDataLink based on Integer32"""
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
        *(("ansi", 3),
          ("att", 2),
          ("nc", 100),
          ("none", 1))
    )


_Cdx6500T1CfgFacilityDataLink_Type.__name__ = "Integer32"
_Cdx6500T1CfgFacilityDataLink_Object = MibTableColumn
cdx6500T1CfgFacilityDataLink = _Cdx6500T1CfgFacilityDataLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 8),
    _Cdx6500T1CfgFacilityDataLink_Type()
)
cdx6500T1CfgFacilityDataLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgFacilityDataLink.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueLES_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueLES_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueLES_Object = MibTableColumn
cdx6500T1CfgThresholdValueLES = _Cdx6500T1CfgThresholdValueLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 9),
    _Cdx6500T1CfgThresholdValueLES_Type()
)
cdx6500T1CfgThresholdValueLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueLES.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueLCV_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueLCV_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueLCV_Object = MibTableColumn
cdx6500T1CfgThresholdValueLCV = _Cdx6500T1CfgThresholdValueLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 10),
    _Cdx6500T1CfgThresholdValueLCV_Type()
)
cdx6500T1CfgThresholdValueLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueLCV.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValuePCV_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValuePCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValuePCV_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValuePCV_Object = MibTableColumn
cdx6500T1CfgThresholdValuePCV = _Cdx6500T1CfgThresholdValuePCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 11),
    _Cdx6500T1CfgThresholdValuePCV_Type()
)
cdx6500T1CfgThresholdValuePCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValuePCV.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueCSS_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueCSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueCSS_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueCSS_Object = MibTableColumn
cdx6500T1CfgThresholdValueCSS = _Cdx6500T1CfgThresholdValueCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 12),
    _Cdx6500T1CfgThresholdValueCSS_Type()
)
cdx6500T1CfgThresholdValueCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueCSS.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueES_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueES_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueES_Object = MibTableColumn
cdx6500T1CfgThresholdValueES = _Cdx6500T1CfgThresholdValueES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 13),
    _Cdx6500T1CfgThresholdValueES_Type()
)
cdx6500T1CfgThresholdValueES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueES.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueBES_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueBES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueBES_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueBES_Object = MibTableColumn
cdx6500T1CfgThresholdValueBES = _Cdx6500T1CfgThresholdValueBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 14),
    _Cdx6500T1CfgThresholdValueBES_Type()
)
cdx6500T1CfgThresholdValueBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueBES.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueSES_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueSES_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueSES_Object = MibTableColumn
cdx6500T1CfgThresholdValueSES = _Cdx6500T1CfgThresholdValueSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 15),
    _Cdx6500T1CfgThresholdValueSES_Type()
)
cdx6500T1CfgThresholdValueSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueSES.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueSEFS_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueSEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueSEFS_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueSEFS_Object = MibTableColumn
cdx6500T1CfgThresholdValueSEFS = _Cdx6500T1CfgThresholdValueSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 16),
    _Cdx6500T1CfgThresholdValueSEFS_Type()
)
cdx6500T1CfgThresholdValueSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueSEFS.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueUAS_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueUAS_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueUAS_Object = MibTableColumn
cdx6500T1CfgThresholdValueUAS = _Cdx6500T1CfgThresholdValueUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 17),
    _Cdx6500T1CfgThresholdValueUAS_Type()
)
cdx6500T1CfgThresholdValueUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueUAS.setStatus("mandatory")


class _Cdx6500T1CfgThresholdValueDM_Type(Integer32):
    """Custom type cdx6500T1CfgThresholdValueDM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1CfgThresholdValueDM_Type.__name__ = "Integer32"
_Cdx6500T1CfgThresholdValueDM_Object = MibTableColumn
cdx6500T1CfgThresholdValueDM = _Cdx6500T1CfgThresholdValueDM_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 18),
    _Cdx6500T1CfgThresholdValueDM_Type()
)
cdx6500T1CfgThresholdValueDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgThresholdValueDM.setStatus("mandatory")


class _Cdx6500T1CfgSwitchType_Type(Integer32):
    """Custom type cdx6500T1CfgSwitchType based on Integer32"""
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
          ("md110", 6),
          ("md110Us", 5),
          ("nc", 100),
          ("ntDms100", 3),
          ("ntDms250", 4),
          ("ntt", 8),
          ("siemens", 7),
          ("unknown", 9))
    )


_Cdx6500T1CfgSwitchType_Type.__name__ = "Integer32"
_Cdx6500T1CfgSwitchType_Object = MibTableColumn
cdx6500T1CfgSwitchType = _Cdx6500T1CfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 19),
    _Cdx6500T1CfgSwitchType_Type()
)
cdx6500T1CfgSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgSwitchType.setStatus("mandatory")


class _Cdx6500T1CfgVariant_Type(Integer32):
    """Custom type cdx6500T1CfgVariant based on Integer32"""
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


_Cdx6500T1CfgVariant_Type.__name__ = "Integer32"
_Cdx6500T1CfgVariant_Object = MibTableColumn
cdx6500T1CfgVariant = _Cdx6500T1CfgVariant_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 20),
    _Cdx6500T1CfgVariant_Type()
)
cdx6500T1CfgVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgVariant.setStatus("mandatory")


class _Cdx6500T1CfgUserNetworkSide_Type(Integer32):
    """Custom type cdx6500T1CfgUserNetworkSide based on Integer32"""
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


_Cdx6500T1CfgUserNetworkSide_Type.__name__ = "Integer32"
_Cdx6500T1CfgUserNetworkSide_Object = MibTableColumn
cdx6500T1CfgUserNetworkSide = _Cdx6500T1CfgUserNetworkSide_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 21),
    _Cdx6500T1CfgUserNetworkSide_Type()
)
cdx6500T1CfgUserNetworkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgUserNetworkSide.setStatus("mandatory")


class _Cdx6500T1CfgCallingIdMsbState_Type(Integer32):
    """Custom type cdx6500T1CfgCallingIdMsbState based on Integer32"""
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


_Cdx6500T1CfgCallingIdMsbState_Type.__name__ = "Integer32"
_Cdx6500T1CfgCallingIdMsbState_Object = MibTableColumn
cdx6500T1CfgCallingIdMsbState = _Cdx6500T1CfgCallingIdMsbState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 1, 1, 1, 22),
    _Cdx6500T1CfgCallingIdMsbState_Type()
)
cdx6500T1CfgCallingIdMsbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1CfgCallingIdMsbState.setStatus("mandatory")
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
_Cdx6500PPSTT1PortTable_Object = MibTable
cdx6500PPSTT1PortTable = _Cdx6500PPSTT1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTT1PortTable.setStatus("mandatory")
_Cdx6500PPSTT1PortEntry_Object = MibTableRow
cdx6500PPSTT1PortEntry = _Cdx6500PPSTT1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1)
)
cdx6500PPSTT1PortEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTT1PortEntry.setStatus("mandatory")
_Cdx6500T1StatPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatPortNumber_Object = MibTableColumn
cdx6500T1StatPortNumber = _Cdx6500T1StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 1),
    _Cdx6500T1StatPortNumber_Type()
)
cdx6500T1StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatPortNumber.setStatus("mandatory")
_Cdx6500T1StatTimeSinceLastResetType_Type = DisplayString
_Cdx6500T1StatTimeSinceLastResetType_Object = MibScalar
cdx6500T1StatTimeSinceLastResetType = _Cdx6500T1StatTimeSinceLastResetType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 2),
    _Cdx6500T1StatTimeSinceLastResetType_Type()
)
cdx6500T1StatTimeSinceLastResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTimeSinceLastResetType.setStatus("mandatory")


class _Cdx6500T1StatPortType_Type(Integer32):
    """Custom type cdx6500T1StatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            44
        )
    )
    namedValues = NamedValues(
        ("t1", 44)
    )


_Cdx6500T1StatPortType_Type.__name__ = "Integer32"
_Cdx6500T1StatPortType_Object = MibTableColumn
cdx6500T1StatPortType = _Cdx6500T1StatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 3),
    _Cdx6500T1StatPortType_Type()
)
cdx6500T1StatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatPortType.setStatus("mandatory")


class _Cdx6500T1StatInterfaceType_Type(Integer32):
    """Custom type cdx6500T1StatInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ds1Csu", 2),
          ("dsx1", 1),
          ("na", 100))
    )


_Cdx6500T1StatInterfaceType_Type.__name__ = "Integer32"
_Cdx6500T1StatInterfaceType_Object = MibTableColumn
cdx6500T1StatInterfaceType = _Cdx6500T1StatInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 4),
    _Cdx6500T1StatInterfaceType_Type()
)
cdx6500T1StatInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatInterfaceType.setStatus("mandatory")


class _Cdx6500T1StatPortState_Type(Integer32):
    """Custom type cdx6500T1StatPortState based on Integer32"""
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


_Cdx6500T1StatPortState_Type.__name__ = "Integer32"
_Cdx6500T1StatPortState_Object = MibTableColumn
cdx6500T1StatPortState = _Cdx6500T1StatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 5),
    _Cdx6500T1StatPortState_Type()
)
cdx6500T1StatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatPortState.setStatus("mandatory")


class _Cdx6500T1StatAlarmState_Type(Integer32):
    """Custom type cdx6500T1StatAlarmState based on Integer32"""
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
        *(("blue", 3),
          ("na", 100),
          ("none", 1),
          ("red", 4),
          ("yellow", 2))
    )


_Cdx6500T1StatAlarmState_Type.__name__ = "Integer32"
_Cdx6500T1StatAlarmState_Object = MibTableColumn
cdx6500T1StatAlarmState = _Cdx6500T1StatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 6),
    _Cdx6500T1StatAlarmState_Type()
)
cdx6500T1StatAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatAlarmState.setStatus("mandatory")
_Cdx6500T1BoardHWRevAndPartNumber_Type = DisplayString
_Cdx6500T1BoardHWRevAndPartNumber_Object = MibTableColumn
cdx6500T1BoardHWRevAndPartNumber = _Cdx6500T1BoardHWRevAndPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 1, 1, 7),
    _Cdx6500T1BoardHWRevAndPartNumber_Type()
)
cdx6500T1BoardHWRevAndPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1BoardHWRevAndPartNumber.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryTable_Object = MibTable
cdx6500T1StatDailyHistoryTable = _Cdx6500T1StatDailyHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3)
)
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryTable.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryEntry_Object = MibTableRow
cdx6500T1StatDailyHistoryEntry = _Cdx6500T1StatDailyHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1)
)
cdx6500T1StatDailyHistoryEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatDailyHistoryPortNumber"),
    (0, "T1-OPT-MIB", "cdx6500T1StatDailyHistoryInterval"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryEntry.setStatus("mandatory")


class _Cdx6500T1StatDailyHistoryInterval_Type(Integer32):
    """Custom type cdx6500T1StatDailyHistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Cdx6500T1StatDailyHistoryInterval_Type.__name__ = "Integer32"
_Cdx6500T1StatDailyHistoryInterval_Object = MibTableColumn
cdx6500T1StatDailyHistoryInterval = _Cdx6500T1StatDailyHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 1),
    _Cdx6500T1StatDailyHistoryInterval_Type()
)
cdx6500T1StatDailyHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryInterval.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryLES_Type = Gauge32
_Cdx6500T1StatDailyHistoryLES_Object = MibTableColumn
cdx6500T1StatDailyHistoryLES = _Cdx6500T1StatDailyHistoryLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 2),
    _Cdx6500T1StatDailyHistoryLES_Type()
)
cdx6500T1StatDailyHistoryLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryLES.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryLCV_Type = Gauge32
_Cdx6500T1StatDailyHistoryLCV_Object = MibTableColumn
cdx6500T1StatDailyHistoryLCV = _Cdx6500T1StatDailyHistoryLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 3),
    _Cdx6500T1StatDailyHistoryLCV_Type()
)
cdx6500T1StatDailyHistoryLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryLCV.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryPCV_Type = Gauge32
_Cdx6500T1StatDailyHistoryPCV_Object = MibTableColumn
cdx6500T1StatDailyHistoryPCV = _Cdx6500T1StatDailyHistoryPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 4),
    _Cdx6500T1StatDailyHistoryPCV_Type()
)
cdx6500T1StatDailyHistoryPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryPCV.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryCSS_Type = Gauge32
_Cdx6500T1StatDailyHistoryCSS_Object = MibTableColumn
cdx6500T1StatDailyHistoryCSS = _Cdx6500T1StatDailyHistoryCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 5),
    _Cdx6500T1StatDailyHistoryCSS_Type()
)
cdx6500T1StatDailyHistoryCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryCSS.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryES_Type = Gauge32
_Cdx6500T1StatDailyHistoryES_Object = MibTableColumn
cdx6500T1StatDailyHistoryES = _Cdx6500T1StatDailyHistoryES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 6),
    _Cdx6500T1StatDailyHistoryES_Type()
)
cdx6500T1StatDailyHistoryES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryES.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryBES_Type = Gauge32
_Cdx6500T1StatDailyHistoryBES_Object = MibTableColumn
cdx6500T1StatDailyHistoryBES = _Cdx6500T1StatDailyHistoryBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 7),
    _Cdx6500T1StatDailyHistoryBES_Type()
)
cdx6500T1StatDailyHistoryBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryBES.setStatus("mandatory")
_Cdx6500T1StatDailyHistorySES_Type = Gauge32
_Cdx6500T1StatDailyHistorySES_Object = MibTableColumn
cdx6500T1StatDailyHistorySES = _Cdx6500T1StatDailyHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 8),
    _Cdx6500T1StatDailyHistorySES_Type()
)
cdx6500T1StatDailyHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistorySES.setStatus("mandatory")
_Cdx6500T1StatDailyHistorySEFS_Type = Gauge32
_Cdx6500T1StatDailyHistorySEFS_Object = MibTableColumn
cdx6500T1StatDailyHistorySEFS = _Cdx6500T1StatDailyHistorySEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 9),
    _Cdx6500T1StatDailyHistorySEFS_Type()
)
cdx6500T1StatDailyHistorySEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistorySEFS.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryUAS_Type = Gauge32
_Cdx6500T1StatDailyHistoryUAS_Object = MibTableColumn
cdx6500T1StatDailyHistoryUAS = _Cdx6500T1StatDailyHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 10),
    _Cdx6500T1StatDailyHistoryUAS_Type()
)
cdx6500T1StatDailyHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryUAS.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryDM_Type = Gauge32
_Cdx6500T1StatDailyHistoryDM_Object = MibTableColumn
cdx6500T1StatDailyHistoryDM = _Cdx6500T1StatDailyHistoryDM_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 11),
    _Cdx6500T1StatDailyHistoryDM_Type()
)
cdx6500T1StatDailyHistoryDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryDM.setStatus("mandatory")
_Cdx6500T1StatDailyHistoryPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatDailyHistoryPortNumber_Object = MibTableColumn
cdx6500T1StatDailyHistoryPortNumber = _Cdx6500T1StatDailyHistoryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 3, 1, 12),
    _Cdx6500T1StatDailyHistoryPortNumber_Type()
)
cdx6500T1StatDailyHistoryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDailyHistoryPortNumber.setStatus("mandatory")
_Cdx6500T1StatABCDStateTable_Object = MibTable
cdx6500T1StatABCDStateTable = _Cdx6500T1StatABCDStateTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5)
)
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStateTable.setStatus("mandatory")
_Cdx6500T1StatABCDStateEntry_Object = MibTableRow
cdx6500T1StatABCDStateEntry = _Cdx6500T1StatABCDStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5, 1)
)
cdx6500T1StatABCDStateEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatABCDStatePortNumber"),
    (0, "T1-OPT-MIB", "cdx6500T1StatABCDStateDS0ChannelNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStateEntry.setStatus("mandatory")


class _Cdx6500T1StatABCDStateDS0ChannelNumber_Type(Integer32):
    """Custom type cdx6500T1StatABCDStateDS0ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500T1StatABCDStateDS0ChannelNumber_Type.__name__ = "Integer32"
_Cdx6500T1StatABCDStateDS0ChannelNumber_Object = MibTableColumn
cdx6500T1StatABCDStateDS0ChannelNumber = _Cdx6500T1StatABCDStateDS0ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5, 1, 1),
    _Cdx6500T1StatABCDStateDS0ChannelNumber_Type()
)
cdx6500T1StatABCDStateDS0ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStateDS0ChannelNumber.setStatus("mandatory")
_Cdx6500T1StatABCDStateCurrentTxState_Type = DisplayString
_Cdx6500T1StatABCDStateCurrentTxState_Object = MibTableColumn
cdx6500T1StatABCDStateCurrentTxState = _Cdx6500T1StatABCDStateCurrentTxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5, 1, 2),
    _Cdx6500T1StatABCDStateCurrentTxState_Type()
)
cdx6500T1StatABCDStateCurrentTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStateCurrentTxState.setStatus("deprecated")
_Cdx6500T1StatABCDStateCurrentRxState_Type = DisplayString
_Cdx6500T1StatABCDStateCurrentRxState_Object = MibTableColumn
cdx6500T1StatABCDStateCurrentRxState = _Cdx6500T1StatABCDStateCurrentRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5, 1, 3),
    _Cdx6500T1StatABCDStateCurrentRxState_Type()
)
cdx6500T1StatABCDStateCurrentRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStateCurrentRxState.setStatus("mandatory")
_Cdx6500T1StatABCDStatePortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatABCDStatePortNumber_Object = MibTableColumn
cdx6500T1StatABCDStatePortNumber = _Cdx6500T1StatABCDStatePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 5, 1, 4),
    _Cdx6500T1StatABCDStatePortNumber_Type()
)
cdx6500T1StatABCDStatePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatABCDStatePortNumber.setStatus("mandatory")
_Cdx6500T1ISDNStatusTable_Object = MibTable
cdx6500T1ISDNStatusTable = _Cdx6500T1ISDNStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7)
)
if mibBuilder.loadTexts:
    cdx6500T1ISDNStatusTable.setStatus("mandatory")
_Cdx6500T1StatISDNStatusEntry_Object = MibTableRow
cdx6500T1StatISDNStatusEntry = _Cdx6500T1StatISDNStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1)
)
cdx6500T1StatISDNStatusEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatISDNStatusPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatISDNStatusEntry.setStatus("mandatory")
_Cdx6500T1StatISDNStatusPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatISDNStatusPortNumber_Object = MibTableColumn
cdx6500T1StatISDNStatusPortNumber = _Cdx6500T1StatISDNStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 1),
    _Cdx6500T1StatISDNStatusPortNumber_Type()
)
cdx6500T1StatISDNStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNStatusPortNumber.setStatus("mandatory")
_Cdx6500T1StatNumRxCallsSinceLastReset_Type = Integer32
_Cdx6500T1StatNumRxCallsSinceLastReset_Object = MibTableColumn
cdx6500T1StatNumRxCallsSinceLastReset = _Cdx6500T1StatNumRxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 2),
    _Cdx6500T1StatNumRxCallsSinceLastReset_Type()
)
cdx6500T1StatNumRxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatNumRxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500T1StatNumRxCallsRejected_Type = Integer32
_Cdx6500T1StatNumRxCallsRejected_Object = MibTableColumn
cdx6500T1StatNumRxCallsRejected = _Cdx6500T1StatNumRxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 3),
    _Cdx6500T1StatNumRxCallsRejected_Type()
)
cdx6500T1StatNumRxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatNumRxCallsRejected.setStatus("mandatory")


class _Cdx6500T1StatRxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500T1StatRxLastCallFailureCause based on Integer32"""
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


_Cdx6500T1StatRxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500T1StatRxLastCallFailureCause_Object = MibTableColumn
cdx6500T1StatRxLastCallFailureCause = _Cdx6500T1StatRxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 4),
    _Cdx6500T1StatRxLastCallFailureCause_Type()
)
cdx6500T1StatRxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500T1StatRxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500T1StatRxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatRxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatRxLastCalledNumber_Object = MibTableColumn
cdx6500T1StatRxLastCalledNumber = _Cdx6500T1StatRxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 5),
    _Cdx6500T1StatRxLastCalledNumber_Type()
)
cdx6500T1StatRxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxLastCalledNumber.setStatus("mandatory")


class _Cdx6500T1StatRxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500T1StatRxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatRxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatRxLastCallingNumber_Object = MibTableColumn
cdx6500T1StatRxLastCallingNumber = _Cdx6500T1StatRxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 6),
    _Cdx6500T1StatRxLastCallingNumber_Type()
)
cdx6500T1StatRxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxLastCallingNumber.setStatus("mandatory")
_Cdx6500T1StatRxMinCallDuration_Type = DisplayString
_Cdx6500T1StatRxMinCallDuration_Object = MibTableColumn
cdx6500T1StatRxMinCallDuration = _Cdx6500T1StatRxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 7),
    _Cdx6500T1StatRxMinCallDuration_Type()
)
cdx6500T1StatRxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxMinCallDuration.setStatus("mandatory")
_Cdx6500T1StatRxMaxCallDuration_Type = DisplayString
_Cdx6500T1StatRxMaxCallDuration_Object = MibTableColumn
cdx6500T1StatRxMaxCallDuration = _Cdx6500T1StatRxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 8),
    _Cdx6500T1StatRxMaxCallDuration_Type()
)
cdx6500T1StatRxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxMaxCallDuration.setStatus("mandatory")
_Cdx6500T1StatRxAvgCallDuration_Type = DisplayString
_Cdx6500T1StatRxAvgCallDuration_Object = MibTableColumn
cdx6500T1StatRxAvgCallDuration = _Cdx6500T1StatRxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 9),
    _Cdx6500T1StatRxAvgCallDuration_Type()
)
cdx6500T1StatRxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatRxAvgCallDuration.setStatus("mandatory")
_Cdx6500T1StatNumTxCallsSinceLastReset_Type = Integer32
_Cdx6500T1StatNumTxCallsSinceLastReset_Object = MibTableColumn
cdx6500T1StatNumTxCallsSinceLastReset = _Cdx6500T1StatNumTxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 10),
    _Cdx6500T1StatNumTxCallsSinceLastReset_Type()
)
cdx6500T1StatNumTxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatNumTxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500T1StatNumTxCallsRejected_Type = Integer32
_Cdx6500T1StatNumTxCallsRejected_Object = MibTableColumn
cdx6500T1StatNumTxCallsRejected = _Cdx6500T1StatNumTxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 11),
    _Cdx6500T1StatNumTxCallsRejected_Type()
)
cdx6500T1StatNumTxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatNumTxCallsRejected.setStatus("mandatory")


class _Cdx6500T1StatTxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500T1StatTxLastCallFailureCause based on Integer32"""
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


_Cdx6500T1StatTxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500T1StatTxLastCallFailureCause_Object = MibTableColumn
cdx6500T1StatTxLastCallFailureCause = _Cdx6500T1StatTxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 12),
    _Cdx6500T1StatTxLastCallFailureCause_Type()
)
cdx6500T1StatTxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500T1StatTxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500T1StatTxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatTxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatTxLastCalledNumber_Object = MibTableColumn
cdx6500T1StatTxLastCalledNumber = _Cdx6500T1StatTxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 13),
    _Cdx6500T1StatTxLastCalledNumber_Type()
)
cdx6500T1StatTxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxLastCalledNumber.setStatus("mandatory")


class _Cdx6500T1StatTxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500T1StatTxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatTxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatTxLastCallingNumber_Object = MibTableColumn
cdx6500T1StatTxLastCallingNumber = _Cdx6500T1StatTxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 14),
    _Cdx6500T1StatTxLastCallingNumber_Type()
)
cdx6500T1StatTxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxLastCallingNumber.setStatus("mandatory")
_Cdx6500T1StatTxMinCallDuration_Type = DisplayString
_Cdx6500T1StatTxMinCallDuration_Object = MibTableColumn
cdx6500T1StatTxMinCallDuration = _Cdx6500T1StatTxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 15),
    _Cdx6500T1StatTxMinCallDuration_Type()
)
cdx6500T1StatTxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxMinCallDuration.setStatus("mandatory")
_Cdx6500T1StatTxMaxCallDuration_Type = DisplayString
_Cdx6500T1StatTxMaxCallDuration_Object = MibTableColumn
cdx6500T1StatTxMaxCallDuration = _Cdx6500T1StatTxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 16),
    _Cdx6500T1StatTxMaxCallDuration_Type()
)
cdx6500T1StatTxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxMaxCallDuration.setStatus("mandatory")
_Cdx6500T1StatTxAvgCallDuration_Type = DisplayString
_Cdx6500T1StatTxAvgCallDuration_Object = MibTableColumn
cdx6500T1StatTxAvgCallDuration = _Cdx6500T1StatTxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 17),
    _Cdx6500T1StatTxAvgCallDuration_Type()
)
cdx6500T1StatTxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatTxAvgCallDuration.setStatus("mandatory")


class _Cdx6500T1StatDchannelState_Type(Integer32):
    """Custom type cdx6500T1StatDchannelState based on Integer32"""
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


_Cdx6500T1StatDchannelState_Type.__name__ = "Integer32"
_Cdx6500T1StatDchannelState_Object = MibTableColumn
cdx6500T1StatDchannelState = _Cdx6500T1StatDchannelState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 7, 1, 18),
    _Cdx6500T1StatDchannelState_Type()
)
cdx6500T1StatDchannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatDchannelState.setStatus("mandatory")
_Cdx6500T1ISDNCallSummaryTable_Object = MibTable
cdx6500T1ISDNCallSummaryTable = _Cdx6500T1ISDNCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9)
)
if mibBuilder.loadTexts:
    cdx6500T1ISDNCallSummaryTable.setStatus("mandatory")
_Cdx6500T1StatISDNCallSummaryEntry_Object = MibTableRow
cdx6500T1StatISDNCallSummaryEntry = _Cdx6500T1StatISDNCallSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1)
)
cdx6500T1StatISDNCallSummaryEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatISDNPortNumber"),
    (0, "T1-OPT-MIB", "cdx6500T1StatISDNBChannelNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatISDNCallSummaryEntry.setStatus("mandatory")


class _Cdx6500T1StatISDNBChannelNumber_Type(Integer32):
    """Custom type cdx6500T1StatISDNBChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_Cdx6500T1StatISDNBChannelNumber_Type.__name__ = "Integer32"
_Cdx6500T1StatISDNBChannelNumber_Object = MibTableColumn
cdx6500T1StatISDNBChannelNumber = _Cdx6500T1StatISDNBChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 1),
    _Cdx6500T1StatISDNBChannelNumber_Type()
)
cdx6500T1StatISDNBChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNBChannelNumber.setStatus("mandatory")


class _Cdx6500T1StatISDNBChannelStatus_Type(Integer32):
    """Custom type cdx6500T1StatISDNBChannelStatus based on Integer32"""
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


_Cdx6500T1StatISDNBChannelStatus_Type.__name__ = "Integer32"
_Cdx6500T1StatISDNBChannelStatus_Object = MibTableColumn
cdx6500T1StatISDNBChannelStatus = _Cdx6500T1StatISDNBChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 2),
    _Cdx6500T1StatISDNBChannelStatus_Type()
)
cdx6500T1StatISDNBChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNBChannelStatus.setStatus("mandatory")


class _Cdx6500T1StatISDNCallDirection_Type(Integer32):
    """Custom type cdx6500T1StatISDNCallDirection based on Integer32"""
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


_Cdx6500T1StatISDNCallDirection_Type.__name__ = "Integer32"
_Cdx6500T1StatISDNCallDirection_Object = MibTableColumn
cdx6500T1StatISDNCallDirection = _Cdx6500T1StatISDNCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 3),
    _Cdx6500T1StatISDNCallDirection_Type()
)
cdx6500T1StatISDNCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNCallDirection.setStatus("mandatory")


class _Cdx6500T1StatISDNCallingNumber_Type(DisplayString):
    """Custom type cdx6500T1StatISDNCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatISDNCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatISDNCallingNumber_Object = MibTableColumn
cdx6500T1StatISDNCallingNumber = _Cdx6500T1StatISDNCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 4),
    _Cdx6500T1StatISDNCallingNumber_Type()
)
cdx6500T1StatISDNCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNCallingNumber.setStatus("mandatory")


class _Cdx6500T1StatISDNCalledNumber_Type(DisplayString):
    """Custom type cdx6500T1StatISDNCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500T1StatISDNCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500T1StatISDNCalledNumber_Object = MibTableColumn
cdx6500T1StatISDNCalledNumber = _Cdx6500T1StatISDNCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 5),
    _Cdx6500T1StatISDNCalledNumber_Type()
)
cdx6500T1StatISDNCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNCalledNumber.setStatus("mandatory")


class _Cdx6500T1StatISDNDS0Rate_Type(Integer32):
    """Custom type cdx6500T1StatISDNDS0Rate based on Integer32"""
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


_Cdx6500T1StatISDNDS0Rate_Type.__name__ = "Integer32"
_Cdx6500T1StatISDNDS0Rate_Object = MibTableColumn
cdx6500T1StatISDNDS0Rate = _Cdx6500T1StatISDNDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 6),
    _Cdx6500T1StatISDNDS0Rate_Type()
)
cdx6500T1StatISDNDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNDS0Rate.setStatus("mandatory")
_Cdx6500T1StatISDNVirtualPortNumber_Type = Integer32
_Cdx6500T1StatISDNVirtualPortNumber_Object = MibTableColumn
cdx6500T1StatISDNVirtualPortNumber = _Cdx6500T1StatISDNVirtualPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 7),
    _Cdx6500T1StatISDNVirtualPortNumber_Type()
)
cdx6500T1StatISDNVirtualPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNVirtualPortNumber.setStatus("mandatory")
_Cdx6500T1StatISDNTimeCallStarted_Type = DisplayString
_Cdx6500T1StatISDNTimeCallStarted_Object = MibTableColumn
cdx6500T1StatISDNTimeCallStarted = _Cdx6500T1StatISDNTimeCallStarted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 8),
    _Cdx6500T1StatISDNTimeCallStarted_Type()
)
cdx6500T1StatISDNTimeCallStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNTimeCallStarted.setStatus("mandatory")
_Cdx6500T1StatISDNPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatISDNPortNumber_Object = MibTableColumn
cdx6500T1StatISDNPortNumber = _Cdx6500T1StatISDNPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 9, 1, 9),
    _Cdx6500T1StatISDNPortNumber_Type()
)
cdx6500T1StatISDNPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatISDNPortNumber.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportTable_Object = MibTable
cdx6500T1StatLast24HoursReportTable = _Cdx6500T1StatLast24HoursReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11)
)
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportTable.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportEntry_Object = MibTableRow
cdx6500T1StatLast24HoursReportEntry = _Cdx6500T1StatLast24HoursReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1)
)
cdx6500T1StatLast24HoursReportEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatLast24HoursReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportEntry.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatLast24HoursReportPortNumber_Object = MibTableColumn
cdx6500T1StatLast24HoursReportPortNumber = _Cdx6500T1StatLast24HoursReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 1),
    _Cdx6500T1StatLast24HoursReportPortNumber_Type()
)
cdx6500T1StatLast24HoursReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportPortNumber.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportLES_Type = Gauge32
_Cdx6500T1StatLast24HoursReportLES_Object = MibTableColumn
cdx6500T1StatLast24HoursReportLES = _Cdx6500T1StatLast24HoursReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 2),
    _Cdx6500T1StatLast24HoursReportLES_Type()
)
cdx6500T1StatLast24HoursReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportLES.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportLCV_Type = Gauge32
_Cdx6500T1StatLast24HoursReportLCV_Object = MibTableColumn
cdx6500T1StatLast24HoursReportLCV = _Cdx6500T1StatLast24HoursReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 3),
    _Cdx6500T1StatLast24HoursReportLCV_Type()
)
cdx6500T1StatLast24HoursReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportLCV.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportPCV_Type = Gauge32
_Cdx6500T1StatLast24HoursReportPCV_Object = MibTableColumn
cdx6500T1StatLast24HoursReportPCV = _Cdx6500T1StatLast24HoursReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 4),
    _Cdx6500T1StatLast24HoursReportPCV_Type()
)
cdx6500T1StatLast24HoursReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportPCV.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportCSS_Type = Gauge32
_Cdx6500T1StatLast24HoursReportCSS_Object = MibTableColumn
cdx6500T1StatLast24HoursReportCSS = _Cdx6500T1StatLast24HoursReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 5),
    _Cdx6500T1StatLast24HoursReportCSS_Type()
)
cdx6500T1StatLast24HoursReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportCSS.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportES_Type = Gauge32
_Cdx6500T1StatLast24HoursReportES_Object = MibTableColumn
cdx6500T1StatLast24HoursReportES = _Cdx6500T1StatLast24HoursReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 6),
    _Cdx6500T1StatLast24HoursReportES_Type()
)
cdx6500T1StatLast24HoursReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportES.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportBES_Type = Gauge32
_Cdx6500T1StatLast24HoursReportBES_Object = MibTableColumn
cdx6500T1StatLast24HoursReportBES = _Cdx6500T1StatLast24HoursReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 7),
    _Cdx6500T1StatLast24HoursReportBES_Type()
)
cdx6500T1StatLast24HoursReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportBES.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportSES_Type = Gauge32
_Cdx6500T1StatLast24HoursReportSES_Object = MibTableColumn
cdx6500T1StatLast24HoursReportSES = _Cdx6500T1StatLast24HoursReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 8),
    _Cdx6500T1StatLast24HoursReportSES_Type()
)
cdx6500T1StatLast24HoursReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportSES.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportSEFS_Type = Gauge32
_Cdx6500T1StatLast24HoursReportSEFS_Object = MibTableColumn
cdx6500T1StatLast24HoursReportSEFS = _Cdx6500T1StatLast24HoursReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 9),
    _Cdx6500T1StatLast24HoursReportSEFS_Type()
)
cdx6500T1StatLast24HoursReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportSEFS.setStatus("mandatory")
_Cdx6500T1StatLast24HoursReportUAS_Type = Gauge32
_Cdx6500T1StatLast24HoursReportUAS_Object = MibTableColumn
cdx6500T1StatLast24HoursReportUAS = _Cdx6500T1StatLast24HoursReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 11, 1, 10),
    _Cdx6500T1StatLast24HoursReportUAS_Type()
)
cdx6500T1StatLast24HoursReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatLast24HoursReportUAS.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportTable_Object = MibTable
cdx6500T1StatCurrent15MinutesReportTable = _Cdx6500T1StatCurrent15MinutesReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13)
)
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportTable.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportEntry_Object = MibTableRow
cdx6500T1StatCurrent15MinutesReportEntry = _Cdx6500T1StatCurrent15MinutesReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1)
)
cdx6500T1StatCurrent15MinutesReportEntry.setIndexNames(
    (0, "T1-OPT-MIB", "cdx6500T1StatCurrent15MinutesReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportEntry.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportPortNumber_Type = PhysicalPortNumber
_Cdx6500T1StatCurrent15MinutesReportPortNumber_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportPortNumber = _Cdx6500T1StatCurrent15MinutesReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 1),
    _Cdx6500T1StatCurrent15MinutesReportPortNumber_Type()
)
cdx6500T1StatCurrent15MinutesReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportPortNumber.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportTimeElapsed_Type = DisplayString
_Cdx6500T1StatCurrent15MinutesReportTimeElapsed_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportTimeElapsed = _Cdx6500T1StatCurrent15MinutesReportTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 2),
    _Cdx6500T1StatCurrent15MinutesReportTimeElapsed_Type()
)
cdx6500T1StatCurrent15MinutesReportTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportTimeElapsed.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportLES_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportLES_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportLES = _Cdx6500T1StatCurrent15MinutesReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 3),
    _Cdx6500T1StatCurrent15MinutesReportLES_Type()
)
cdx6500T1StatCurrent15MinutesReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportLES.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportLCV_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportLCV_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportLCV = _Cdx6500T1StatCurrent15MinutesReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 4),
    _Cdx6500T1StatCurrent15MinutesReportLCV_Type()
)
cdx6500T1StatCurrent15MinutesReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportLCV.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportPCV_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportPCV_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportPCV = _Cdx6500T1StatCurrent15MinutesReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 5),
    _Cdx6500T1StatCurrent15MinutesReportPCV_Type()
)
cdx6500T1StatCurrent15MinutesReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportPCV.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportCSS_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportCSS_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportCSS = _Cdx6500T1StatCurrent15MinutesReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 6),
    _Cdx6500T1StatCurrent15MinutesReportCSS_Type()
)
cdx6500T1StatCurrent15MinutesReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportCSS.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportES_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportES_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportES = _Cdx6500T1StatCurrent15MinutesReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 7),
    _Cdx6500T1StatCurrent15MinutesReportES_Type()
)
cdx6500T1StatCurrent15MinutesReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportES.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportBES_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportBES_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportBES = _Cdx6500T1StatCurrent15MinutesReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 8),
    _Cdx6500T1StatCurrent15MinutesReportBES_Type()
)
cdx6500T1StatCurrent15MinutesReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportBES.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportSES_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportSES_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportSES = _Cdx6500T1StatCurrent15MinutesReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 9),
    _Cdx6500T1StatCurrent15MinutesReportSES_Type()
)
cdx6500T1StatCurrent15MinutesReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportSES.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportSEFS_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportSEFS_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportSEFS = _Cdx6500T1StatCurrent15MinutesReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 10),
    _Cdx6500T1StatCurrent15MinutesReportSEFS_Type()
)
cdx6500T1StatCurrent15MinutesReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportSEFS.setStatus("mandatory")
_Cdx6500T1StatCurrent15MinutesReportUAS_Type = Gauge32
_Cdx6500T1StatCurrent15MinutesReportUAS_Object = MibTableColumn
cdx6500T1StatCurrent15MinutesReportUAS = _Cdx6500T1StatCurrent15MinutesReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25, 13, 1, 11),
    _Cdx6500T1StatCurrent15MinutesReportUAS_Type()
)
cdx6500T1StatCurrent15MinutesReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1StatCurrent15MinutesReportUAS.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T1-OPT-MIB",
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
       "cdx6500PCTT1PortTable": cdx6500PCTT1PortTable,
       "cdx6500PPCTT1PortTable": cdx6500PPCTT1PortTable,
       "cdx6500PPCTT1PortEntry": cdx6500PPCTT1PortEntry,
       "cdx6500T1CfgPortNumber": cdx6500T1CfgPortNumber,
       "cdx6500T1CfgPortType": cdx6500T1CfgPortType,
       "cdx6500T1CfgFormat": cdx6500T1CfgFormat,
       "cdx6500T1CfgLineFramingType": cdx6500T1CfgLineFramingType,
       "cdx6500T1CfgLineCoding": cdx6500T1CfgLineCoding,
       "cdx6500T1CfgTransmitClock": cdx6500T1CfgTransmitClock,
       "cdx6500T1CfgLineBuildOut": cdx6500T1CfgLineBuildOut,
       "cdx6500T1CfgFacilityDataLink": cdx6500T1CfgFacilityDataLink,
       "cdx6500T1CfgThresholdValueLES": cdx6500T1CfgThresholdValueLES,
       "cdx6500T1CfgThresholdValueLCV": cdx6500T1CfgThresholdValueLCV,
       "cdx6500T1CfgThresholdValuePCV": cdx6500T1CfgThresholdValuePCV,
       "cdx6500T1CfgThresholdValueCSS": cdx6500T1CfgThresholdValueCSS,
       "cdx6500T1CfgThresholdValueES": cdx6500T1CfgThresholdValueES,
       "cdx6500T1CfgThresholdValueBES": cdx6500T1CfgThresholdValueBES,
       "cdx6500T1CfgThresholdValueSES": cdx6500T1CfgThresholdValueSES,
       "cdx6500T1CfgThresholdValueSEFS": cdx6500T1CfgThresholdValueSEFS,
       "cdx6500T1CfgThresholdValueUAS": cdx6500T1CfgThresholdValueUAS,
       "cdx6500T1CfgThresholdValueDM": cdx6500T1CfgThresholdValueDM,
       "cdx6500T1CfgSwitchType": cdx6500T1CfgSwitchType,
       "cdx6500T1CfgVariant": cdx6500T1CfgVariant,
       "cdx6500T1CfgUserNetworkSide": cdx6500T1CfgUserNetworkSide,
       "cdx6500T1CfgCallingIdMsbState": cdx6500T1CfgCallingIdMsbState,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTT1E1PortTable": cdx6500PSTT1E1PortTable,
       "cdx6500PPSTT1PortTable": cdx6500PPSTT1PortTable,
       "cdx6500PPSTT1PortEntry": cdx6500PPSTT1PortEntry,
       "cdx6500T1StatPortNumber": cdx6500T1StatPortNumber,
       "cdx6500T1StatTimeSinceLastResetType": cdx6500T1StatTimeSinceLastResetType,
       "cdx6500T1StatPortType": cdx6500T1StatPortType,
       "cdx6500T1StatInterfaceType": cdx6500T1StatInterfaceType,
       "cdx6500T1StatPortState": cdx6500T1StatPortState,
       "cdx6500T1StatAlarmState": cdx6500T1StatAlarmState,
       "cdx6500T1BoardHWRevAndPartNumber": cdx6500T1BoardHWRevAndPartNumber,
       "cdx6500T1StatDailyHistoryTable": cdx6500T1StatDailyHistoryTable,
       "cdx6500T1StatDailyHistoryEntry": cdx6500T1StatDailyHistoryEntry,
       "cdx6500T1StatDailyHistoryInterval": cdx6500T1StatDailyHistoryInterval,
       "cdx6500T1StatDailyHistoryLES": cdx6500T1StatDailyHistoryLES,
       "cdx6500T1StatDailyHistoryLCV": cdx6500T1StatDailyHistoryLCV,
       "cdx6500T1StatDailyHistoryPCV": cdx6500T1StatDailyHistoryPCV,
       "cdx6500T1StatDailyHistoryCSS": cdx6500T1StatDailyHistoryCSS,
       "cdx6500T1StatDailyHistoryES": cdx6500T1StatDailyHistoryES,
       "cdx6500T1StatDailyHistoryBES": cdx6500T1StatDailyHistoryBES,
       "cdx6500T1StatDailyHistorySES": cdx6500T1StatDailyHistorySES,
       "cdx6500T1StatDailyHistorySEFS": cdx6500T1StatDailyHistorySEFS,
       "cdx6500T1StatDailyHistoryUAS": cdx6500T1StatDailyHistoryUAS,
       "cdx6500T1StatDailyHistoryDM": cdx6500T1StatDailyHistoryDM,
       "cdx6500T1StatDailyHistoryPortNumber": cdx6500T1StatDailyHistoryPortNumber,
       "cdx6500T1StatABCDStateTable": cdx6500T1StatABCDStateTable,
       "cdx6500T1StatABCDStateEntry": cdx6500T1StatABCDStateEntry,
       "cdx6500T1StatABCDStateDS0ChannelNumber": cdx6500T1StatABCDStateDS0ChannelNumber,
       "cdx6500T1StatABCDStateCurrentTxState": cdx6500T1StatABCDStateCurrentTxState,
       "cdx6500T1StatABCDStateCurrentRxState": cdx6500T1StatABCDStateCurrentRxState,
       "cdx6500T1StatABCDStatePortNumber": cdx6500T1StatABCDStatePortNumber,
       "cdx6500T1ISDNStatusTable": cdx6500T1ISDNStatusTable,
       "cdx6500T1StatISDNStatusEntry": cdx6500T1StatISDNStatusEntry,
       "cdx6500T1StatISDNStatusPortNumber": cdx6500T1StatISDNStatusPortNumber,
       "cdx6500T1StatNumRxCallsSinceLastReset": cdx6500T1StatNumRxCallsSinceLastReset,
       "cdx6500T1StatNumRxCallsRejected": cdx6500T1StatNumRxCallsRejected,
       "cdx6500T1StatRxLastCallFailureCause": cdx6500T1StatRxLastCallFailureCause,
       "cdx6500T1StatRxLastCalledNumber": cdx6500T1StatRxLastCalledNumber,
       "cdx6500T1StatRxLastCallingNumber": cdx6500T1StatRxLastCallingNumber,
       "cdx6500T1StatRxMinCallDuration": cdx6500T1StatRxMinCallDuration,
       "cdx6500T1StatRxMaxCallDuration": cdx6500T1StatRxMaxCallDuration,
       "cdx6500T1StatRxAvgCallDuration": cdx6500T1StatRxAvgCallDuration,
       "cdx6500T1StatNumTxCallsSinceLastReset": cdx6500T1StatNumTxCallsSinceLastReset,
       "cdx6500T1StatNumTxCallsRejected": cdx6500T1StatNumTxCallsRejected,
       "cdx6500T1StatTxLastCallFailureCause": cdx6500T1StatTxLastCallFailureCause,
       "cdx6500T1StatTxLastCalledNumber": cdx6500T1StatTxLastCalledNumber,
       "cdx6500T1StatTxLastCallingNumber": cdx6500T1StatTxLastCallingNumber,
       "cdx6500T1StatTxMinCallDuration": cdx6500T1StatTxMinCallDuration,
       "cdx6500T1StatTxMaxCallDuration": cdx6500T1StatTxMaxCallDuration,
       "cdx6500T1StatTxAvgCallDuration": cdx6500T1StatTxAvgCallDuration,
       "cdx6500T1StatDchannelState": cdx6500T1StatDchannelState,
       "cdx6500T1ISDNCallSummaryTable": cdx6500T1ISDNCallSummaryTable,
       "cdx6500T1StatISDNCallSummaryEntry": cdx6500T1StatISDNCallSummaryEntry,
       "cdx6500T1StatISDNBChannelNumber": cdx6500T1StatISDNBChannelNumber,
       "cdx6500T1StatISDNBChannelStatus": cdx6500T1StatISDNBChannelStatus,
       "cdx6500T1StatISDNCallDirection": cdx6500T1StatISDNCallDirection,
       "cdx6500T1StatISDNCallingNumber": cdx6500T1StatISDNCallingNumber,
       "cdx6500T1StatISDNCalledNumber": cdx6500T1StatISDNCalledNumber,
       "cdx6500T1StatISDNDS0Rate": cdx6500T1StatISDNDS0Rate,
       "cdx6500T1StatISDNVirtualPortNumber": cdx6500T1StatISDNVirtualPortNumber,
       "cdx6500T1StatISDNTimeCallStarted": cdx6500T1StatISDNTimeCallStarted,
       "cdx6500T1StatISDNPortNumber": cdx6500T1StatISDNPortNumber,
       "cdx6500T1StatLast24HoursReportTable": cdx6500T1StatLast24HoursReportTable,
       "cdx6500T1StatLast24HoursReportEntry": cdx6500T1StatLast24HoursReportEntry,
       "cdx6500T1StatLast24HoursReportPortNumber": cdx6500T1StatLast24HoursReportPortNumber,
       "cdx6500T1StatLast24HoursReportLES": cdx6500T1StatLast24HoursReportLES,
       "cdx6500T1StatLast24HoursReportLCV": cdx6500T1StatLast24HoursReportLCV,
       "cdx6500T1StatLast24HoursReportPCV": cdx6500T1StatLast24HoursReportPCV,
       "cdx6500T1StatLast24HoursReportCSS": cdx6500T1StatLast24HoursReportCSS,
       "cdx6500T1StatLast24HoursReportES": cdx6500T1StatLast24HoursReportES,
       "cdx6500T1StatLast24HoursReportBES": cdx6500T1StatLast24HoursReportBES,
       "cdx6500T1StatLast24HoursReportSES": cdx6500T1StatLast24HoursReportSES,
       "cdx6500T1StatLast24HoursReportSEFS": cdx6500T1StatLast24HoursReportSEFS,
       "cdx6500T1StatLast24HoursReportUAS": cdx6500T1StatLast24HoursReportUAS,
       "cdx6500T1StatCurrent15MinutesReportTable": cdx6500T1StatCurrent15MinutesReportTable,
       "cdx6500T1StatCurrent15MinutesReportEntry": cdx6500T1StatCurrent15MinutesReportEntry,
       "cdx6500T1StatCurrent15MinutesReportPortNumber": cdx6500T1StatCurrent15MinutesReportPortNumber,
       "cdx6500T1StatCurrent15MinutesReportTimeElapsed": cdx6500T1StatCurrent15MinutesReportTimeElapsed,
       "cdx6500T1StatCurrent15MinutesReportLES": cdx6500T1StatCurrent15MinutesReportLES,
       "cdx6500T1StatCurrent15MinutesReportLCV": cdx6500T1StatCurrent15MinutesReportLCV,
       "cdx6500T1StatCurrent15MinutesReportPCV": cdx6500T1StatCurrent15MinutesReportPCV,
       "cdx6500T1StatCurrent15MinutesReportCSS": cdx6500T1StatCurrent15MinutesReportCSS,
       "cdx6500T1StatCurrent15MinutesReportES": cdx6500T1StatCurrent15MinutesReportES,
       "cdx6500T1StatCurrent15MinutesReportBES": cdx6500T1StatCurrent15MinutesReportBES,
       "cdx6500T1StatCurrent15MinutesReportSES": cdx6500T1StatCurrent15MinutesReportSES,
       "cdx6500T1StatCurrent15MinutesReportSEFS": cdx6500T1StatCurrent15MinutesReportSEFS,
       "cdx6500T1StatCurrent15MinutesReportUAS": cdx6500T1StatCurrent15MinutesReportUAS}
)
