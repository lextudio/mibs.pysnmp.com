# SNMP MIB module (FRDCE-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRDCE-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:22 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



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
_Cdx6500PCTFRDCEPortTable_Object = MibTable
cdx6500PCTFRDCEPortTable = _Cdx6500PCTFRDCEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cdx6500PCTFRDCEPortTable.setStatus("mandatory")
_Cdx6500PCTFRDCEPortEntry_Object = MibTableRow
cdx6500PCTFRDCEPortEntry = _Cdx6500PCTFRDCEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1)
)
cdx6500PCTFRDCEPortEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcepCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PCTFRDCEPortEntry.setStatus("mandatory")


class _Cdx6500frdcepCfgPortNum_Type(Integer32):
    """Custom type cdx6500frdcepCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500frdcepCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500frdcepCfgPortNum_Object = MibTableColumn
cdx6500frdcepCfgPortNum = _Cdx6500frdcepCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 1),
    _Cdx6500frdcepCfgPortNum_Type()
)
cdx6500frdcepCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCfgPortNum.setStatus("mandatory")


class _Cdx6500frdcepConnectionType_Type(Integer32):
    """Custom type cdx6500frdcepConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalSimp", 50),
          ("simp", 0))
    )


_Cdx6500frdcepConnectionType_Type.__name__ = "Integer32"
_Cdx6500frdcepConnectionType_Object = MibTableColumn
cdx6500frdcepConnectionType = _Cdx6500frdcepConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 2),
    _Cdx6500frdcepConnectionType_Type()
)
cdx6500frdcepConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepConnectionType.setStatus("mandatory")


class _Cdx6500frdcepClockSource_Type(Integer32):
    """Custom type cdx6500frdcepClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("ext", 1),
          ("extint", 2),
          ("extlp", 3),
          ("int", 0),
          ("newvalInt", 50))
    )


_Cdx6500frdcepClockSource_Type.__name__ = "Integer32"
_Cdx6500frdcepClockSource_Object = MibTableColumn
cdx6500frdcepClockSource = _Cdx6500frdcepClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 3),
    _Cdx6500frdcepClockSource_Type()
)
cdx6500frdcepClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepClockSource.setStatus("mandatory")


class _Cdx6500frdcepClockSpeed_Type(Integer32):
    """Custom type cdx6500frdcepClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 2048000),
    )


_Cdx6500frdcepClockSpeed_Type.__name__ = "Integer32"
_Cdx6500frdcepClockSpeed_Object = MibTableColumn
cdx6500frdcepClockSpeed = _Cdx6500frdcepClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 4),
    _Cdx6500frdcepClockSpeed_Type()
)
cdx6500frdcepClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepClockSpeed.setStatus("mandatory")
_Cdx6500frdcepMaxStations_Type = Integer32
_Cdx6500frdcepMaxStations_Object = MibTableColumn
cdx6500frdcepMaxStations = _Cdx6500frdcepMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 5),
    _Cdx6500frdcepMaxStations_Type()
)
cdx6500frdcepMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepMaxStations.setStatus("deprecated")


class _Cdx6500frdcepCtrlProtocol_Type(Integer32):
    """Custom type cdx6500frdcepCtrlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexD", 0),
          ("lmi", 2),
          ("newvalAnnexD", 50),
          ("none", 1))
    )


_Cdx6500frdcepCtrlProtocol_Type.__name__ = "Integer32"
_Cdx6500frdcepCtrlProtocol_Object = MibTableColumn
cdx6500frdcepCtrlProtocol = _Cdx6500frdcepCtrlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 6),
    _Cdx6500frdcepCtrlProtocol_Type()
)
cdx6500frdcepCtrlProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCtrlProtocol.setStatus("mandatory")
_Cdx6500frdcepT391_Type = Integer32
_Cdx6500frdcepT391_Object = MibTableColumn
cdx6500frdcepT391 = _Cdx6500frdcepT391_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 7),
    _Cdx6500frdcepT391_Type()
)
cdx6500frdcepT391.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepT391.setStatus("mandatory")
_Cdx6500frdcepT392_Type = Integer32
_Cdx6500frdcepT392_Object = MibTableColumn
cdx6500frdcepT392 = _Cdx6500frdcepT392_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 8),
    _Cdx6500frdcepT392_Type()
)
cdx6500frdcepT392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepT392.setStatus("mandatory")
_Cdx6500frdcepN391_Type = Integer32
_Cdx6500frdcepN391_Object = MibTableColumn
cdx6500frdcepN391 = _Cdx6500frdcepN391_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 9),
    _Cdx6500frdcepN391_Type()
)
cdx6500frdcepN391.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepN391.setStatus("mandatory")
_Cdx6500frdcepN392_Type = Integer32
_Cdx6500frdcepN392_Object = MibTableColumn
cdx6500frdcepN392 = _Cdx6500frdcepN392_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 10),
    _Cdx6500frdcepN392_Type()
)
cdx6500frdcepN392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepN392.setStatus("mandatory")
_Cdx6500frdcepN393_Type = Integer32
_Cdx6500frdcepN393_Object = MibTableColumn
cdx6500frdcepN393 = _Cdx6500frdcepN393_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 11),
    _Cdx6500frdcepN393_Type()
)
cdx6500frdcepN393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepN393.setStatus("mandatory")
_Cdx6500frdcepNT1_Type = Integer32
_Cdx6500frdcepNT1_Object = MibTableColumn
cdx6500frdcepNT1 = _Cdx6500frdcepNT1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 12),
    _Cdx6500frdcepNT1_Type()
)
cdx6500frdcepNT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepNT1.setStatus("mandatory")
_Cdx6500frdcepNT2_Type = Integer32
_Cdx6500frdcepNT2_Object = MibTableColumn
cdx6500frdcepNT2 = _Cdx6500frdcepNT2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 13),
    _Cdx6500frdcepNT2_Type()
)
cdx6500frdcepNT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepNT2.setStatus("mandatory")
_Cdx6500frdcepNN1_Type = Integer32
_Cdx6500frdcepNN1_Object = MibTableColumn
cdx6500frdcepNN1 = _Cdx6500frdcepNN1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 14),
    _Cdx6500frdcepNN1_Type()
)
cdx6500frdcepNN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepNN1.setStatus("mandatory")
_Cdx6500frdcepNN2_Type = Integer32
_Cdx6500frdcepNN2_Object = MibTableColumn
cdx6500frdcepNN2 = _Cdx6500frdcepNN2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 15),
    _Cdx6500frdcepNN2_Type()
)
cdx6500frdcepNN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepNN2.setStatus("mandatory")
_Cdx6500frdcepNN3_Type = Integer32
_Cdx6500frdcepNN3_Object = MibTableColumn
cdx6500frdcepNN3 = _Cdx6500frdcepNN3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 16),
    _Cdx6500frdcepNN3_Type()
)
cdx6500frdcepNN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepNN3.setStatus("mandatory")


class _Cdx6500frdcepSubaddress_Type(DisplayString):
    """Custom type cdx6500frdcepSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500frdcepSubaddress_Type.__name__ = "DisplayString"
_Cdx6500frdcepSubaddress_Object = MibTableColumn
cdx6500frdcepSubaddress = _Cdx6500frdcepSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 17),
    _Cdx6500frdcepSubaddress_Type()
)
cdx6500frdcepSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepSubaddress.setStatus("mandatory")


class _Cdx6500frdcepBiDirAnnexD_Type(Integer32):
    """Custom type cdx6500frdcepBiDirAnnexD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("bi", 0),
          ("newvalBi", 50),
          ("uni", 1))
    )


_Cdx6500frdcepBiDirAnnexD_Type.__name__ = "Integer32"
_Cdx6500frdcepBiDirAnnexD_Object = MibTableColumn
cdx6500frdcepBiDirAnnexD = _Cdx6500frdcepBiDirAnnexD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 18),
    _Cdx6500frdcepBiDirAnnexD_Type()
)
cdx6500frdcepBiDirAnnexD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepBiDirAnnexD.setStatus("mandatory")


class _Cdx6500frdcepInvertTXClock_Type(Integer32):
    """Custom type cdx6500frdcepInvertTXClock based on Integer32"""
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
          ("no", 1),
          ("yes", 2))
    )


_Cdx6500frdcepInvertTXClock_Type.__name__ = "Integer32"
_Cdx6500frdcepInvertTXClock_Object = MibTableColumn
cdx6500frdcepInvertTXClock = _Cdx6500frdcepInvertTXClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 19),
    _Cdx6500frdcepInvertTXClock_Type()
)
cdx6500frdcepInvertTXClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepInvertTXClock.setStatus("mandatory")


class _Cdx6500frdcepControlProtocolOptions_Type(DisplayString):
    """Custom type cdx6500frdcepControlProtocolOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500frdcepControlProtocolOptions_Type.__name__ = "DisplayString"
_Cdx6500frdcepControlProtocolOptions_Object = MibTableColumn
cdx6500frdcepControlProtocolOptions = _Cdx6500frdcepControlProtocolOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 20),
    _Cdx6500frdcepControlProtocolOptions_Type()
)
cdx6500frdcepControlProtocolOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepControlProtocolOptions.setStatus("mandatory")


class _Cdx6500frdcepDiscardControlOptions_Type(Integer32):
    """Custom type cdx6500frdcepDiscardControlOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debit", 2),
          ("none", 1))
    )


_Cdx6500frdcepDiscardControlOptions_Type.__name__ = "Integer32"
_Cdx6500frdcepDiscardControlOptions_Object = MibTableColumn
cdx6500frdcepDiscardControlOptions = _Cdx6500frdcepDiscardControlOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 21),
    _Cdx6500frdcepDiscardControlOptions_Type()
)
cdx6500frdcepDiscardControlOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepDiscardControlOptions.setStatus("mandatory")


class _Cdx6500frdcepElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500frdcepElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500frdcepElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500frdcepElectricalInterfaceType_Object = MibTableColumn
cdx6500frdcepElectricalInterfaceType = _Cdx6500frdcepElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 22),
    _Cdx6500frdcepElectricalInterfaceType_Type()
)
cdx6500frdcepElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500frdcepV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500frdcepV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500frdcepV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500frdcepV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500frdcepV24ElectricalInterfaceOption = _Cdx6500frdcepV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 23),
    _Cdx6500frdcepV24ElectricalInterfaceOption_Type()
)
cdx6500frdcepV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500frdcepHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500frdcepHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500frdcepHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500frdcepHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500frdcepHighSpeedElectricalInterfaceOption = _Cdx6500frdcepHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 6, 1, 24),
    _Cdx6500frdcepHighSpeedElectricalInterfaceOption_Type()
)
cdx6500frdcepHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTFRDCEStationTable_Object = MibTable
cdx6500SPCTFRDCEStationTable = _Cdx6500SPCTFRDCEStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRDCEStationTable.setStatus("mandatory")
_Cdx6500SPCTFRDCEStationEntry_Object = MibTableRow
cdx6500SPCTFRDCEStationEntry = _Cdx6500SPCTFRDCEStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1)
)
cdx6500SPCTFRDCEStationEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesCfgPortNum"),
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesCfgDLCI"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRDCEStationEntry.setStatus("mandatory")


class _Cdx6500frdcesCfgPortNum_Type(Integer32):
    """Custom type cdx6500frdcesCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500frdcesCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500frdcesCfgPortNum_Object = MibTableColumn
cdx6500frdcesCfgPortNum = _Cdx6500frdcesCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 1),
    _Cdx6500frdcesCfgPortNum_Type()
)
cdx6500frdcesCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCfgPortNum.setStatus("mandatory")


class _Cdx6500frdcesCfgDLCI_Type(Integer32):
    """Custom type cdx6500frdcesCfgDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Cdx6500frdcesCfgDLCI_Type.__name__ = "Integer32"
_Cdx6500frdcesCfgDLCI_Object = MibTableColumn
cdx6500frdcesCfgDLCI = _Cdx6500frdcesCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 2),
    _Cdx6500frdcesCfgDLCI_Type()
)
cdx6500frdcesCfgDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCfgDLCI.setStatus("mandatory")


class _Cdx6500frdcesAutocallMnem_Type(DisplayString):
    """Custom type cdx6500frdcesAutocallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500frdcesAutocallMnem_Type.__name__ = "DisplayString"
_Cdx6500frdcesAutocallMnem_Object = MibTableColumn
cdx6500frdcesAutocallMnem = _Cdx6500frdcesAutocallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 3),
    _Cdx6500frdcesAutocallMnem_Type()
)
cdx6500frdcesAutocallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesAutocallMnem.setStatus("mandatory")
_Cdx6500frdcesAutocallTimeout_Type = Integer32
_Cdx6500frdcesAutocallTimeout_Object = MibTableColumn
cdx6500frdcesAutocallTimeout = _Cdx6500frdcesAutocallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 4),
    _Cdx6500frdcesAutocallTimeout_Type()
)
cdx6500frdcesAutocallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesAutocallTimeout.setStatus("mandatory")
_Cdx6500frdcesMaxAutocalls_Type = Integer32
_Cdx6500frdcesMaxAutocalls_Object = MibTableColumn
cdx6500frdcesMaxAutocalls = _Cdx6500frdcesMaxAutocalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 5),
    _Cdx6500frdcesMaxAutocalls_Type()
)
cdx6500frdcesMaxAutocalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesMaxAutocalls.setStatus("mandatory")
_Cdx6500frdcesRemoteConnID_Type = Integer32
_Cdx6500frdcesRemoteConnID_Object = MibTableColumn
cdx6500frdcesRemoteConnID = _Cdx6500frdcesRemoteConnID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 6),
    _Cdx6500frdcesRemoteConnID_Type()
)
cdx6500frdcesRemoteConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesRemoteConnID.setStatus("mandatory")


class _Cdx6500frdcesPriority_Type(Integer32):
    """Custom type cdx6500frdcesPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("expedite", 3),
          ("high", 2),
          ("low", 0),
          ("medium", 1),
          ("newvalLow", 50))
    )


_Cdx6500frdcesPriority_Type.__name__ = "Integer32"
_Cdx6500frdcesPriority_Object = MibTableColumn
cdx6500frdcesPriority = _Cdx6500frdcesPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 7),
    _Cdx6500frdcesPriority_Type()
)
cdx6500frdcesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPriority.setStatus("mandatory")


class _Cdx6500frdcesBillingRecords_Type(Integer32):
    """Custom type cdx6500frdcesBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500frdcesBillingRecords_Type.__name__ = "Integer32"
_Cdx6500frdcesBillingRecords_Object = MibTableColumn
cdx6500frdcesBillingRecords = _Cdx6500frdcesBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 8),
    _Cdx6500frdcesBillingRecords_Type()
)
cdx6500frdcesBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesBillingRecords.setStatus("mandatory")
_Cdx6500frdcesStationNum_Type = Integer32
_Cdx6500frdcesStationNum_Object = MibTableColumn
cdx6500frdcesStationNum = _Cdx6500frdcesStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 9),
    _Cdx6500frdcesStationNum_Type()
)
cdx6500frdcesStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesStationNum.setStatus("mandatory")


class _Cdx6500frdcesMaxInboundQueue_Type(Integer32):
    """Custom type cdx6500frdcesMaxInboundQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2500),
    )


_Cdx6500frdcesMaxInboundQueue_Type.__name__ = "Integer32"
_Cdx6500frdcesMaxInboundQueue_Object = MibTableColumn
cdx6500frdcesMaxInboundQueue = _Cdx6500frdcesMaxInboundQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 3, 1, 10),
    _Cdx6500frdcesMaxInboundQueue_Type()
)
cdx6500frdcesMaxInboundQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesMaxInboundQueue.setStatus("mandatory")
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
_Cdx6500PPSTFRDCEPortTable_Object = MibTable
cdx6500PPSTFRDCEPortTable = _Cdx6500PPSTFRDCEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRDCEPortTable.setStatus("mandatory")
_Cdx6500PPSTFRDCEPortEntry_Object = MibTableRow
cdx6500PPSTFRDCEPortEntry = _Cdx6500PPSTFRDCEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1)
)
cdx6500PPSTFRDCEPortEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcepStatsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRDCEPortEntry.setStatus("mandatory")


class _Cdx6500frdcepStatsPortNum_Type(Integer32):
    """Custom type cdx6500frdcepStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500frdcepStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500frdcepStatsPortNum_Object = MibTableColumn
cdx6500frdcepStatsPortNum = _Cdx6500frdcepStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 1),
    _Cdx6500frdcepStatsPortNum_Type()
)
cdx6500frdcepStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepStatsPortNum.setStatus("mandatory")


class _Cdx6500frdcepPortStatus_Type(Integer32):
    """Custom type cdx6500frdcepPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500frdcepPortStatus_Type.__name__ = "Integer32"
_Cdx6500frdcepPortStatus_Object = MibTableColumn
cdx6500frdcepPortStatus = _Cdx6500frdcepPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 2),
    _Cdx6500frdcepPortStatus_Type()
)
cdx6500frdcepPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepPortStatus.setStatus("mandatory")
_Cdx6500frdcepPortSpeed_Type = Integer32
_Cdx6500frdcepPortSpeed_Object = MibTableColumn
cdx6500frdcepPortSpeed = _Cdx6500frdcepPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 3),
    _Cdx6500frdcepPortSpeed_Type()
)
cdx6500frdcepPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepPortSpeed.setStatus("mandatory")


class _Cdx6500frdcepUtilizationIn_Type(Integer32):
    """Custom type cdx6500frdcepUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdcepUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500frdcepUtilizationIn_Object = MibTableColumn
cdx6500frdcepUtilizationIn = _Cdx6500frdcepUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 4),
    _Cdx6500frdcepUtilizationIn_Type()
)
cdx6500frdcepUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepUtilizationIn.setStatus("mandatory")


class _Cdx6500frdcepUtilizationOut_Type(Integer32):
    """Custom type cdx6500frdcepUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdcepUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500frdcepUtilizationOut_Object = MibTableColumn
cdx6500frdcepUtilizationOut = _Cdx6500frdcepUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 5),
    _Cdx6500frdcepUtilizationOut_Type()
)
cdx6500frdcepUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepUtilizationOut.setStatus("mandatory")
_Cdx6500frdcepCharInTotal_Type = Counter32
_Cdx6500frdcepCharInTotal_Object = MibTableColumn
cdx6500frdcepCharInTotal = _Cdx6500frdcepCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 6),
    _Cdx6500frdcepCharInTotal_Type()
)
cdx6500frdcepCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCharInTotal.setStatus("mandatory")
_Cdx6500frdcepCharOutTotal_Type = Counter32
_Cdx6500frdcepCharOutTotal_Object = MibTableColumn
cdx6500frdcepCharOutTotal = _Cdx6500frdcepCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 7),
    _Cdx6500frdcepCharOutTotal_Type()
)
cdx6500frdcepCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCharOutTotal.setStatus("mandatory")
_Cdx6500frdcepCharsInPerSec_Type = Integer32
_Cdx6500frdcepCharsInPerSec_Object = MibTableColumn
cdx6500frdcepCharsInPerSec = _Cdx6500frdcepCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 8),
    _Cdx6500frdcepCharsInPerSec_Type()
)
cdx6500frdcepCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCharsInPerSec.setStatus("mandatory")
_Cdx6500frdcepCharsOutPerSec_Type = Integer32
_Cdx6500frdcepCharsOutPerSec_Object = MibTableColumn
cdx6500frdcepCharsOutPerSec = _Cdx6500frdcepCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 9),
    _Cdx6500frdcepCharsOutPerSec_Type()
)
cdx6500frdcepCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCharsOutPerSec.setStatus("mandatory")
_Cdx6500frdcepFrameInTotal_Type = Counter32
_Cdx6500frdcepFrameInTotal_Object = MibTableColumn
cdx6500frdcepFrameInTotal = _Cdx6500frdcepFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 10),
    _Cdx6500frdcepFrameInTotal_Type()
)
cdx6500frdcepFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepFrameInTotal.setStatus("mandatory")
_Cdx6500frdcepFrameOutTotal_Type = Counter32
_Cdx6500frdcepFrameOutTotal_Object = MibTableColumn
cdx6500frdcepFrameOutTotal = _Cdx6500frdcepFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 11),
    _Cdx6500frdcepFrameOutTotal_Type()
)
cdx6500frdcepFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepFrameOutTotal.setStatus("mandatory")
_Cdx6500frdcepFramesInPerSec_Type = Integer32
_Cdx6500frdcepFramesInPerSec_Object = MibTableColumn
cdx6500frdcepFramesInPerSec = _Cdx6500frdcepFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 12),
    _Cdx6500frdcepFramesInPerSec_Type()
)
cdx6500frdcepFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepFramesInPerSec.setStatus("mandatory")
_Cdx6500frdcepFramesOutPerSec_Type = Integer32
_Cdx6500frdcepFramesOutPerSec_Object = MibTableColumn
cdx6500frdcepFramesOutPerSec = _Cdx6500frdcepFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 13),
    _Cdx6500frdcepFramesOutPerSec_Type()
)
cdx6500frdcepFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepFramesOutPerSec.setStatus("mandatory")
_Cdx6500frdcepOverrunErrors_Type = Counter16
_Cdx6500frdcepOverrunErrors_Object = MibTableColumn
cdx6500frdcepOverrunErrors = _Cdx6500frdcepOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 14),
    _Cdx6500frdcepOverrunErrors_Type()
)
cdx6500frdcepOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepOverrunErrors.setStatus("mandatory")
_Cdx6500frdcepUnderrunErrors_Type = Counter16
_Cdx6500frdcepUnderrunErrors_Object = MibTableColumn
cdx6500frdcepUnderrunErrors = _Cdx6500frdcepUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 15),
    _Cdx6500frdcepUnderrunErrors_Type()
)
cdx6500frdcepUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepUnderrunErrors.setStatus("mandatory")
_Cdx6500frdcepCRCErrors_Type = Counter16
_Cdx6500frdcepCRCErrors_Object = MibTableColumn
cdx6500frdcepCRCErrors = _Cdx6500frdcepCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 6, 1, 16),
    _Cdx6500frdcepCRCErrors_Type()
)
cdx6500frdcepCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcepCRCErrors.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTFRDCEStationTable_Object = MibTable
cdx6500SPSTFRDCEStationTable = _Cdx6500SPSTFRDCEStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdx6500SPSTFRDCEStationTable.setStatus("mandatory")
_Cdx6500SPSTFRDCEStationEntry_Object = MibTableRow
cdx6500SPSTFRDCEStationEntry = _Cdx6500SPSTFRDCEStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1)
)
cdx6500SPSTFRDCEStationEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesStatsPortNum"),
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesStatsDLCI"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTFRDCEStationEntry.setStatus("mandatory")


class _Cdx6500frdcesStatsPortNum_Type(Integer32):
    """Custom type cdx6500frdcesStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500frdcesStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500frdcesStatsPortNum_Object = MibTableColumn
cdx6500frdcesStatsPortNum = _Cdx6500frdcesStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 1),
    _Cdx6500frdcesStatsPortNum_Type()
)
cdx6500frdcesStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesStatsPortNum.setStatus("mandatory")


class _Cdx6500frdcesStatsDLCI_Type(Integer32):
    """Custom type cdx6500frdcesStatsDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Cdx6500frdcesStatsDLCI_Type.__name__ = "Integer32"
_Cdx6500frdcesStatsDLCI_Object = MibTableColumn
cdx6500frdcesStatsDLCI = _Cdx6500frdcesStatsDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 2),
    _Cdx6500frdcesStatsDLCI_Type()
)
cdx6500frdcesStatsDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesStatsDLCI.setStatus("mandatory")


class _Cdx6500frdcesUtilizationIn_Type(Integer32):
    """Custom type cdx6500frdcesUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdcesUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500frdcesUtilizationIn_Object = MibTableColumn
cdx6500frdcesUtilizationIn = _Cdx6500frdcesUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 3),
    _Cdx6500frdcesUtilizationIn_Type()
)
cdx6500frdcesUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesUtilizationIn.setStatus("mandatory")


class _Cdx6500frdcesUtilizationOut_Type(Integer32):
    """Custom type cdx6500frdcesUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdcesUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500frdcesUtilizationOut_Object = MibTableColumn
cdx6500frdcesUtilizationOut = _Cdx6500frdcesUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 4),
    _Cdx6500frdcesUtilizationOut_Type()
)
cdx6500frdcesUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesUtilizationOut.setStatus("mandatory")
_Cdx6500frdcesMaxSVCCount_Type = Integer32
_Cdx6500frdcesMaxSVCCount_Object = MibTableColumn
cdx6500frdcesMaxSVCCount = _Cdx6500frdcesMaxSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 5),
    _Cdx6500frdcesMaxSVCCount_Type()
)
cdx6500frdcesMaxSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesMaxSVCCount.setStatus("deprecated")
_Cdx6500frdcesCurrentSVCCount_Type = Integer32
_Cdx6500frdcesCurrentSVCCount_Object = MibTableColumn
cdx6500frdcesCurrentSVCCount = _Cdx6500frdcesCurrentSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 6),
    _Cdx6500frdcesCurrentSVCCount_Type()
)
cdx6500frdcesCurrentSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCurrentSVCCount.setStatus("deprecated")
_Cdx6500frdcesCharInTotal_Type = Counter32
_Cdx6500frdcesCharInTotal_Object = MibTableColumn
cdx6500frdcesCharInTotal = _Cdx6500frdcesCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 7),
    _Cdx6500frdcesCharInTotal_Type()
)
cdx6500frdcesCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCharInTotal.setStatus("mandatory")
_Cdx6500frdcesCharOutTotal_Type = Counter32
_Cdx6500frdcesCharOutTotal_Object = MibTableColumn
cdx6500frdcesCharOutTotal = _Cdx6500frdcesCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 8),
    _Cdx6500frdcesCharOutTotal_Type()
)
cdx6500frdcesCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCharOutTotal.setStatus("mandatory")
_Cdx6500frdcesCharsInPerSec_Type = Integer32
_Cdx6500frdcesCharsInPerSec_Object = MibTableColumn
cdx6500frdcesCharsInPerSec = _Cdx6500frdcesCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 9),
    _Cdx6500frdcesCharsInPerSec_Type()
)
cdx6500frdcesCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCharsInPerSec.setStatus("mandatory")
_Cdx6500frdcesCharsOutPerSec_Type = Integer32
_Cdx6500frdcesCharsOutPerSec_Object = MibTableColumn
cdx6500frdcesCharsOutPerSec = _Cdx6500frdcesCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 10),
    _Cdx6500frdcesCharsOutPerSec_Type()
)
cdx6500frdcesCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesCharsOutPerSec.setStatus("mandatory")
_Cdx6500frdcesPktInTotal_Type = Counter32
_Cdx6500frdcesPktInTotal_Object = MibTableColumn
cdx6500frdcesPktInTotal = _Cdx6500frdcesPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 11),
    _Cdx6500frdcesPktInTotal_Type()
)
cdx6500frdcesPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPktInTotal.setStatus("mandatory")
_Cdx6500frdcesPktOutTotal_Type = Counter32
_Cdx6500frdcesPktOutTotal_Object = MibTableColumn
cdx6500frdcesPktOutTotal = _Cdx6500frdcesPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 12),
    _Cdx6500frdcesPktOutTotal_Type()
)
cdx6500frdcesPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPktOutTotal.setStatus("mandatory")
_Cdx6500frdcesPktsInPerSec_Type = Integer32
_Cdx6500frdcesPktsInPerSec_Object = MibTableColumn
cdx6500frdcesPktsInPerSec = _Cdx6500frdcesPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 13),
    _Cdx6500frdcesPktsInPerSec_Type()
)
cdx6500frdcesPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPktsInPerSec.setStatus("mandatory")
_Cdx6500frdcesPktsOutPerSec_Type = Integer32
_Cdx6500frdcesPktsOutPerSec_Object = MibTableColumn
cdx6500frdcesPktsOutPerSec = _Cdx6500frdcesPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 14),
    _Cdx6500frdcesPktsOutPerSec_Type()
)
cdx6500frdcesPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPktsOutPerSec.setStatus("mandatory")
_Cdx6500frdcesPacketsQueued_Type = Integer32
_Cdx6500frdcesPacketsQueued_Object = MibTableColumn
cdx6500frdcesPacketsQueued = _Cdx6500frdcesPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 15),
    _Cdx6500frdcesPacketsQueued_Type()
)
cdx6500frdcesPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesPacketsQueued.setStatus("mandatory")
_Cdx6500frdcesFrameInTotal_Type = Counter32
_Cdx6500frdcesFrameInTotal_Object = MibTableColumn
cdx6500frdcesFrameInTotal = _Cdx6500frdcesFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 16),
    _Cdx6500frdcesFrameInTotal_Type()
)
cdx6500frdcesFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesFrameInTotal.setStatus("mandatory")
_Cdx6500frdcesFrameOutTotal_Type = Counter32
_Cdx6500frdcesFrameOutTotal_Object = MibTableColumn
cdx6500frdcesFrameOutTotal = _Cdx6500frdcesFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 17),
    _Cdx6500frdcesFrameOutTotal_Type()
)
cdx6500frdcesFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesFrameOutTotal.setStatus("mandatory")
_Cdx6500frdcesFramesInPerSec_Type = Integer32
_Cdx6500frdcesFramesInPerSec_Object = MibTableColumn
cdx6500frdcesFramesInPerSec = _Cdx6500frdcesFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 18),
    _Cdx6500frdcesFramesInPerSec_Type()
)
cdx6500frdcesFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesFramesInPerSec.setStatus("mandatory")
_Cdx6500frdcesFramesOutPerSec_Type = Integer32
_Cdx6500frdcesFramesOutPerSec_Object = MibTableColumn
cdx6500frdcesFramesOutPerSec = _Cdx6500frdcesFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 19),
    _Cdx6500frdcesFramesOutPerSec_Type()
)
cdx6500frdcesFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesFramesOutPerSec.setStatus("mandatory")
_Cdx6500frdcesInfoFramesIn_Type = Counter32
_Cdx6500frdcesInfoFramesIn_Object = MibTableColumn
cdx6500frdcesInfoFramesIn = _Cdx6500frdcesInfoFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 20),
    _Cdx6500frdcesInfoFramesIn_Type()
)
cdx6500frdcesInfoFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesInfoFramesIn.setStatus("deprecated")
_Cdx6500frdcesInfoFramesOut_Type = Counter32
_Cdx6500frdcesInfoFramesOut_Object = MibTableColumn
cdx6500frdcesInfoFramesOut = _Cdx6500frdcesInfoFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 21),
    _Cdx6500frdcesInfoFramesOut_Type()
)
cdx6500frdcesInfoFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesInfoFramesOut.setStatus("deprecated")
_Cdx6500frdcesRNRFramesIn_Type = Counter32
_Cdx6500frdcesRNRFramesIn_Object = MibTableColumn
cdx6500frdcesRNRFramesIn = _Cdx6500frdcesRNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 22),
    _Cdx6500frdcesRNRFramesIn_Type()
)
cdx6500frdcesRNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesRNRFramesIn.setStatus("deprecated")
_Cdx6500frdcesRNRFramesOut_Type = Counter32
_Cdx6500frdcesRNRFramesOut_Object = MibTableColumn
cdx6500frdcesRNRFramesOut = _Cdx6500frdcesRNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 23),
    _Cdx6500frdcesRNRFramesOut_Type()
)
cdx6500frdcesRNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesRNRFramesOut.setStatus("deprecated")
_Cdx6500frdcesRRFramesIn_Type = Counter32
_Cdx6500frdcesRRFramesIn_Object = MibTableColumn
cdx6500frdcesRRFramesIn = _Cdx6500frdcesRRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 24),
    _Cdx6500frdcesRRFramesIn_Type()
)
cdx6500frdcesRRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesRRFramesIn.setStatus("deprecated")
_Cdx6500frdcesRRFramesOut_Type = Counter32
_Cdx6500frdcesRRFramesOut_Object = MibTableColumn
cdx6500frdcesRRFramesOut = _Cdx6500frdcesRRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 25),
    _Cdx6500frdcesRRFramesOut_Type()
)
cdx6500frdcesRRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesRRFramesOut.setStatus("deprecated")
_Cdx6500frdcesREJFramesIn_Type = Counter32
_Cdx6500frdcesREJFramesIn_Object = MibTableColumn
cdx6500frdcesREJFramesIn = _Cdx6500frdcesREJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 26),
    _Cdx6500frdcesREJFramesIn_Type()
)
cdx6500frdcesREJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesREJFramesIn.setStatus("deprecated")
_Cdx6500frdcesREJFramesOut_Type = Counter32
_Cdx6500frdcesREJFramesOut_Object = MibTableColumn
cdx6500frdcesREJFramesOut = _Cdx6500frdcesREJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 27),
    _Cdx6500frdcesREJFramesOut_Type()
)
cdx6500frdcesREJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesREJFramesOut.setStatus("deprecated")
_Cdx6500frdcesDataPktsIn_Type = Counter32
_Cdx6500frdcesDataPktsIn_Object = MibTableColumn
cdx6500frdcesDataPktsIn = _Cdx6500frdcesDataPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 28),
    _Cdx6500frdcesDataPktsIn_Type()
)
cdx6500frdcesDataPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesDataPktsIn.setStatus("mandatory")
_Cdx6500frdcesDataPktsOut_Type = Counter32
_Cdx6500frdcesDataPktsOut_Object = MibTableColumn
cdx6500frdcesDataPktsOut = _Cdx6500frdcesDataPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 29),
    _Cdx6500frdcesDataPktsOut_Type()
)
cdx6500frdcesDataPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdcesDataPktsOut.setStatus("mandatory")


class _Cdx6500frdcesResetStats_Type(Integer32):
    """Custom type cdx6500frdcesResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500frdcesResetStats_Type.__name__ = "Integer32"
_Cdx6500frdcesResetStats_Object = MibTableColumn
cdx6500frdcesResetStats = _Cdx6500frdcesResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 30),
    _Cdx6500frdcesResetStats_Type()
)
cdx6500frdcesResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcesResetStats.setStatus("obsolete")


class _Cdx6500frdcesBoot_Type(Integer32):
    """Custom type cdx6500frdcesBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Cdx6500frdcesBoot_Type.__name__ = "Integer32"
_Cdx6500frdcesBoot_Object = MibTableColumn
cdx6500frdcesBoot = _Cdx6500frdcesBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 31),
    _Cdx6500frdcesBoot_Type()
)
cdx6500frdcesBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcesBoot.setStatus("obsolete")


class _Cdx6500frdcesDisable_Type(Integer32):
    """Custom type cdx6500frdcesDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_Cdx6500frdcesDisable_Type.__name__ = "Integer32"
_Cdx6500frdcesDisable_Object = MibTableColumn
cdx6500frdcesDisable = _Cdx6500frdcesDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 32),
    _Cdx6500frdcesDisable_Type()
)
cdx6500frdcesDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcesDisable.setStatus("obsolete")


class _Cdx6500frdcesEnable_Type(Integer32):
    """Custom type cdx6500frdcesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_Cdx6500frdcesEnable_Type.__name__ = "Integer32"
_Cdx6500frdcesEnable_Object = MibTableColumn
cdx6500frdcesEnable = _Cdx6500frdcesEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 3, 1, 33),
    _Cdx6500frdcesEnable_Type()
)
cdx6500frdcesEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcesEnable.setStatus("obsolete")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContFRATable_ObjectIdentity = ObjectIdentity
cdx6500ContFRATable = _Cdx6500ContFRATable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17)
)
_Cdx6500frdcepPContTable_Object = MibTable
cdx6500frdcepPContTable = _Cdx6500frdcepPContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 1)
)
if mibBuilder.loadTexts:
    cdx6500frdcepPContTable.setStatus("mandatory")
_Cdx6500frdcepPContEntry_Object = MibTableRow
cdx6500frdcepPContEntry = _Cdx6500frdcepPContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 1, 1)
)
cdx6500frdcepPContEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcepContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500frdcepPContEntry.setStatus("mandatory")


class _Cdx6500frdcepContPortNumber_Type(Integer32):
    """Custom type cdx6500frdcepContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdcepContPortNumber_Type.__name__ = "Integer32"
_Cdx6500frdcepContPortNumber_Object = MibTableColumn
cdx6500frdcepContPortNumber = _Cdx6500frdcepContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 1, 1, 1),
    _Cdx6500frdcepContPortNumber_Type()
)
cdx6500frdcepContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500frdcepContPortNumber.setStatus("mandatory")


class _Cdx6500frdcepContPortControl_Type(Integer32):
    """Custom type cdx6500frdcepContPortControl based on Integer32"""
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
        *(("boot", 1),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 4))
    )


_Cdx6500frdcepContPortControl_Type.__name__ = "Integer32"
_Cdx6500frdcepContPortControl_Object = MibTableColumn
cdx6500frdcepContPortControl = _Cdx6500frdcepContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 1, 1, 2),
    _Cdx6500frdcepContPortControl_Type()
)
cdx6500frdcepContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcepContPortControl.setStatus("mandatory")
_Cdx6500frdcesSContTable_Object = MibTable
cdx6500frdcesSContTable = _Cdx6500frdcesSContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 2)
)
if mibBuilder.loadTexts:
    cdx6500frdcesSContTable.setStatus("mandatory")
_Cdx6500frdcesSContEntry_Object = MibTableRow
cdx6500frdcesSContEntry = _Cdx6500frdcesSContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 2, 1)
)
cdx6500frdcesSContEntry.setIndexNames(
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesStationPortNumber"),
    (0, "FRDCE-OPT-MIB", "cdx6500frdcesStationDLCI"),
)
if mibBuilder.loadTexts:
    cdx6500frdcesSContEntry.setStatus("mandatory")


class _Cdx6500frdcesStationPortNumber_Type(Integer32):
    """Custom type cdx6500frdcesStationPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdcesStationPortNumber_Type.__name__ = "Integer32"
_Cdx6500frdcesStationPortNumber_Object = MibTableColumn
cdx6500frdcesStationPortNumber = _Cdx6500frdcesStationPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 2, 1, 1),
    _Cdx6500frdcesStationPortNumber_Type()
)
cdx6500frdcesStationPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500frdcesStationPortNumber.setStatus("mandatory")


class _Cdx6500frdcesStationDLCI_Type(Integer32):
    """Custom type cdx6500frdcesStationDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Cdx6500frdcesStationDLCI_Type.__name__ = "Integer32"
_Cdx6500frdcesStationDLCI_Object = MibTableColumn
cdx6500frdcesStationDLCI = _Cdx6500frdcesStationDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 2, 1, 2),
    _Cdx6500frdcesStationDLCI_Type()
)
cdx6500frdcesStationDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500frdcesStationDLCI.setStatus("mandatory")


class _Cdx6500frdcesStationControl_Type(Integer32):
    """Custom type cdx6500frdcesStationControl based on Integer32"""
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
        *(("boot", 1),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 4))
    )


_Cdx6500frdcesStationControl_Type.__name__ = "Integer32"
_Cdx6500frdcesStationControl_Object = MibTableColumn
cdx6500frdcesStationControl = _Cdx6500frdcesStationControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 17, 2, 1, 3),
    _Cdx6500frdcesStationControl_Type()
)
cdx6500frdcesStationControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdcesStationControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRDCE-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTFRDCEPortTable": cdx6500PCTFRDCEPortTable,
       "cdx6500PCTFRDCEPortEntry": cdx6500PCTFRDCEPortEntry,
       "cdx6500frdcepCfgPortNum": cdx6500frdcepCfgPortNum,
       "cdx6500frdcepConnectionType": cdx6500frdcepConnectionType,
       "cdx6500frdcepClockSource": cdx6500frdcepClockSource,
       "cdx6500frdcepClockSpeed": cdx6500frdcepClockSpeed,
       "cdx6500frdcepMaxStations": cdx6500frdcepMaxStations,
       "cdx6500frdcepCtrlProtocol": cdx6500frdcepCtrlProtocol,
       "cdx6500frdcepT391": cdx6500frdcepT391,
       "cdx6500frdcepT392": cdx6500frdcepT392,
       "cdx6500frdcepN391": cdx6500frdcepN391,
       "cdx6500frdcepN392": cdx6500frdcepN392,
       "cdx6500frdcepN393": cdx6500frdcepN393,
       "cdx6500frdcepNT1": cdx6500frdcepNT1,
       "cdx6500frdcepNT2": cdx6500frdcepNT2,
       "cdx6500frdcepNN1": cdx6500frdcepNN1,
       "cdx6500frdcepNN2": cdx6500frdcepNN2,
       "cdx6500frdcepNN3": cdx6500frdcepNN3,
       "cdx6500frdcepSubaddress": cdx6500frdcepSubaddress,
       "cdx6500frdcepBiDirAnnexD": cdx6500frdcepBiDirAnnexD,
       "cdx6500frdcepInvertTXClock": cdx6500frdcepInvertTXClock,
       "cdx6500frdcepControlProtocolOptions": cdx6500frdcepControlProtocolOptions,
       "cdx6500frdcepDiscardControlOptions": cdx6500frdcepDiscardControlOptions,
       "cdx6500frdcepElectricalInterfaceType": cdx6500frdcepElectricalInterfaceType,
       "cdx6500frdcepV24ElectricalInterfaceOption": cdx6500frdcepV24ElectricalInterfaceOption,
       "cdx6500frdcepHighSpeedElectricalInterfaceOption": cdx6500frdcepHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTFRDCEStationTable": cdx6500SPCTFRDCEStationTable,
       "cdx6500SPCTFRDCEStationEntry": cdx6500SPCTFRDCEStationEntry,
       "cdx6500frdcesCfgPortNum": cdx6500frdcesCfgPortNum,
       "cdx6500frdcesCfgDLCI": cdx6500frdcesCfgDLCI,
       "cdx6500frdcesAutocallMnem": cdx6500frdcesAutocallMnem,
       "cdx6500frdcesAutocallTimeout": cdx6500frdcesAutocallTimeout,
       "cdx6500frdcesMaxAutocalls": cdx6500frdcesMaxAutocalls,
       "cdx6500frdcesRemoteConnID": cdx6500frdcesRemoteConnID,
       "cdx6500frdcesPriority": cdx6500frdcesPriority,
       "cdx6500frdcesBillingRecords": cdx6500frdcesBillingRecords,
       "cdx6500frdcesStationNum": cdx6500frdcesStationNum,
       "cdx6500frdcesMaxInboundQueue": cdx6500frdcesMaxInboundQueue,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTFRDCEPortTable": cdx6500PPSTFRDCEPortTable,
       "cdx6500PPSTFRDCEPortEntry": cdx6500PPSTFRDCEPortEntry,
       "cdx6500frdcepStatsPortNum": cdx6500frdcepStatsPortNum,
       "cdx6500frdcepPortStatus": cdx6500frdcepPortStatus,
       "cdx6500frdcepPortSpeed": cdx6500frdcepPortSpeed,
       "cdx6500frdcepUtilizationIn": cdx6500frdcepUtilizationIn,
       "cdx6500frdcepUtilizationOut": cdx6500frdcepUtilizationOut,
       "cdx6500frdcepCharInTotal": cdx6500frdcepCharInTotal,
       "cdx6500frdcepCharOutTotal": cdx6500frdcepCharOutTotal,
       "cdx6500frdcepCharsInPerSec": cdx6500frdcepCharsInPerSec,
       "cdx6500frdcepCharsOutPerSec": cdx6500frdcepCharsOutPerSec,
       "cdx6500frdcepFrameInTotal": cdx6500frdcepFrameInTotal,
       "cdx6500frdcepFrameOutTotal": cdx6500frdcepFrameOutTotal,
       "cdx6500frdcepFramesInPerSec": cdx6500frdcepFramesInPerSec,
       "cdx6500frdcepFramesOutPerSec": cdx6500frdcepFramesOutPerSec,
       "cdx6500frdcepOverrunErrors": cdx6500frdcepOverrunErrors,
       "cdx6500frdcepUnderrunErrors": cdx6500frdcepUnderrunErrors,
       "cdx6500frdcepCRCErrors": cdx6500frdcepCRCErrors,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTFRDCEStationTable": cdx6500SPSTFRDCEStationTable,
       "cdx6500SPSTFRDCEStationEntry": cdx6500SPSTFRDCEStationEntry,
       "cdx6500frdcesStatsPortNum": cdx6500frdcesStatsPortNum,
       "cdx6500frdcesStatsDLCI": cdx6500frdcesStatsDLCI,
       "cdx6500frdcesUtilizationIn": cdx6500frdcesUtilizationIn,
       "cdx6500frdcesUtilizationOut": cdx6500frdcesUtilizationOut,
       "cdx6500frdcesMaxSVCCount": cdx6500frdcesMaxSVCCount,
       "cdx6500frdcesCurrentSVCCount": cdx6500frdcesCurrentSVCCount,
       "cdx6500frdcesCharInTotal": cdx6500frdcesCharInTotal,
       "cdx6500frdcesCharOutTotal": cdx6500frdcesCharOutTotal,
       "cdx6500frdcesCharsInPerSec": cdx6500frdcesCharsInPerSec,
       "cdx6500frdcesCharsOutPerSec": cdx6500frdcesCharsOutPerSec,
       "cdx6500frdcesPktInTotal": cdx6500frdcesPktInTotal,
       "cdx6500frdcesPktOutTotal": cdx6500frdcesPktOutTotal,
       "cdx6500frdcesPktsInPerSec": cdx6500frdcesPktsInPerSec,
       "cdx6500frdcesPktsOutPerSec": cdx6500frdcesPktsOutPerSec,
       "cdx6500frdcesPacketsQueued": cdx6500frdcesPacketsQueued,
       "cdx6500frdcesFrameInTotal": cdx6500frdcesFrameInTotal,
       "cdx6500frdcesFrameOutTotal": cdx6500frdcesFrameOutTotal,
       "cdx6500frdcesFramesInPerSec": cdx6500frdcesFramesInPerSec,
       "cdx6500frdcesFramesOutPerSec": cdx6500frdcesFramesOutPerSec,
       "cdx6500frdcesInfoFramesIn": cdx6500frdcesInfoFramesIn,
       "cdx6500frdcesInfoFramesOut": cdx6500frdcesInfoFramesOut,
       "cdx6500frdcesRNRFramesIn": cdx6500frdcesRNRFramesIn,
       "cdx6500frdcesRNRFramesOut": cdx6500frdcesRNRFramesOut,
       "cdx6500frdcesRRFramesIn": cdx6500frdcesRRFramesIn,
       "cdx6500frdcesRRFramesOut": cdx6500frdcesRRFramesOut,
       "cdx6500frdcesREJFramesIn": cdx6500frdcesREJFramesIn,
       "cdx6500frdcesREJFramesOut": cdx6500frdcesREJFramesOut,
       "cdx6500frdcesDataPktsIn": cdx6500frdcesDataPktsIn,
       "cdx6500frdcesDataPktsOut": cdx6500frdcesDataPktsOut,
       "cdx6500frdcesResetStats": cdx6500frdcesResetStats,
       "cdx6500frdcesBoot": cdx6500frdcesBoot,
       "cdx6500frdcesDisable": cdx6500frdcesDisable,
       "cdx6500frdcesEnable": cdx6500frdcesEnable,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContFRATable": cdx6500ContFRATable,
       "cdx6500frdcepPContTable": cdx6500frdcepPContTable,
       "cdx6500frdcepPContEntry": cdx6500frdcepPContEntry,
       "cdx6500frdcepContPortNumber": cdx6500frdcepContPortNumber,
       "cdx6500frdcepContPortControl": cdx6500frdcepContPortControl,
       "cdx6500frdcesSContTable": cdx6500frdcesSContTable,
       "cdx6500frdcesSContEntry": cdx6500frdcesSContEntry,
       "cdx6500frdcesStationPortNumber": cdx6500frdcesStationPortNumber,
       "cdx6500frdcesStationDLCI": cdx6500frdcesStationDLCI,
       "cdx6500frdcesStationControl": cdx6500frdcesStationControl}
)
