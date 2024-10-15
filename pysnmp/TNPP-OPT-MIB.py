# SNMP MIB module (TNPP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TNPP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:31 2024
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
_Cdx6500PPCTTNPPPortTable_Object = MibTable
cdx6500PPCTTNPPPortTable = _Cdx6500PPCTTNPPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32)
)
if mibBuilder.loadTexts:
    cdx6500PPCTTNPPPortTable.setStatus("mandatory")
_Cdx6500PPCTTNPPPortEntry_Object = MibTableRow
cdx6500PPCTTNPPPortEntry = _Cdx6500PPCTTNPPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1)
)
cdx6500PPCTTNPPPortEntry.setIndexNames(
    (0, "TNPP-OPT-MIB", "tnppPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTTNPPPortEntry.setStatus("mandatory")


class _TnppPCfgPortNumber_Type(Integer32):
    """Custom type tnppPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TnppPCfgPortNumber_Type.__name__ = "Integer32"
_TnppPCfgPortNumber_Object = MibTableColumn
tnppPCfgPortNumber = _TnppPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 1),
    _TnppPCfgPortNumber_Type()
)
tnppPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgPortNumber.setStatus("mandatory")


class _TnppPCfgPortType_Type(Integer32):
    """Custom type tnppPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            37
        )
    )
    namedValues = NamedValues(
        ("tnpp", 37)
    )


_TnppPCfgPortType_Type.__name__ = "Integer32"
_TnppPCfgPortType_Object = MibTableColumn
tnppPCfgPortType = _TnppPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 2),
    _TnppPCfgPortType_Type()
)
tnppPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgPortType.setStatus("mandatory")


class _TnppPCfgPortSpeed_Type(Integer32):
    """Custom type tnppPCfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed300", 3),
          ("speed4800", 14),
          ("speed9600", 15))
    )


_TnppPCfgPortSpeed_Type.__name__ = "Integer32"
_TnppPCfgPortSpeed_Object = MibTableColumn
tnppPCfgPortSpeed = _TnppPCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 3),
    _TnppPCfgPortSpeed_Type()
)
tnppPCfgPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgPortSpeed.setStatus("mandatory")


class _TnppPCfgCallControl_Type(Integer32):
    """Custom type tnppPCfgCallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dataDrv", 3),
          ("dtr", 2),
          ("nc", 100),
          ("powerOn", 4))
    )


_TnppPCfgCallControl_Type.__name__ = "Integer32"
_TnppPCfgCallControl_Object = MibTableColumn
tnppPCfgCallControl = _TnppPCfgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 4),
    _TnppPCfgCallControl_Type()
)
tnppPCfgCallControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgCallControl.setStatus("mandatory")


class _TnppPCfgCRCOption_Type(Integer32):
    """Custom type tnppPCfgCRCOption based on Integer32"""
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
          ("normal", 1),
          ("transp", 2))
    )


_TnppPCfgCRCOption_Type.__name__ = "Integer32"
_TnppPCfgCRCOption_Object = MibTableColumn
tnppPCfgCRCOption = _TnppPCfgCRCOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 5),
    _TnppPCfgCRCOption_Type()
)
tnppPCfgCRCOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgCRCOption.setStatus("mandatory")


class _TnppPCfgTANControl_Type(Integer32):
    """Custom type tnppPCfgTANControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("mps2000Mode", 1),
          ("nc", 100),
          ("unipageMode", 2))
    )


_TnppPCfgTANControl_Type.__name__ = "Integer32"
_TnppPCfgTANControl_Object = MibTableColumn
tnppPCfgTANControl = _TnppPCfgTANControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 6),
    _TnppPCfgTANControl_Type()
)
tnppPCfgTANControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgTANControl.setStatus("mandatory")


class _TnppPCfgCANReports_Type(Integer32):
    """Custom type tnppPCfgCANReports based on Integer32"""
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


_TnppPCfgCANReports_Type.__name__ = "Integer32"
_TnppPCfgCANReports_Object = MibTableColumn
tnppPCfgCANReports = _TnppPCfgCANReports_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 7),
    _TnppPCfgCANReports_Type()
)
tnppPCfgCANReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgCANReports.setStatus("mandatory")


class _TnppPCfgRSCount_Type(Integer32):
    """Custom type tnppPCfgRSCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnppPCfgRSCount_Type.__name__ = "Integer32"
_TnppPCfgRSCount_Object = MibTableColumn
tnppPCfgRSCount = _TnppPCfgRSCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 8),
    _TnppPCfgRSCount_Type()
)
tnppPCfgRSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgRSCount.setStatus("mandatory")


class _TnppPCfgMaxRSCount_Type(Integer32):
    """Custom type tnppPCfgMaxRSCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnppPCfgMaxRSCount_Type.__name__ = "Integer32"
_TnppPCfgMaxRSCount_Object = MibTableColumn
tnppPCfgMaxRSCount = _TnppPCfgMaxRSCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 9),
    _TnppPCfgMaxRSCount_Type()
)
tnppPCfgMaxRSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgMaxRSCount.setStatus("mandatory")


class _TnppPCfgRSSupport_Type(Integer32):
    """Custom type tnppPCfgRSSupport based on Integer32"""
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


_TnppPCfgRSSupport_Type.__name__ = "Integer32"
_TnppPCfgRSSupport_Object = MibTableColumn
tnppPCfgRSSupport = _TnppPCfgRSSupport_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 10),
    _TnppPCfgRSSupport_Type()
)
tnppPCfgRSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgRSSupport.setStatus("mandatory")


class _TnppPCfgAutocallMnemonic_Type(DisplayString):
    """Custom type tnppPCfgAutocallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TnppPCfgAutocallMnemonic_Type.__name__ = "DisplayString"
_TnppPCfgAutocallMnemonic_Object = MibTableColumn
tnppPCfgAutocallMnemonic = _TnppPCfgAutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 11),
    _TnppPCfgAutocallMnemonic_Type()
)
tnppPCfgAutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgAutocallMnemonic.setStatus("mandatory")


class _TnppPCfgAutocallTimeout_Type(Integer32):
    """Custom type tnppPCfgAutocallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_TnppPCfgAutocallTimeout_Type.__name__ = "Integer32"
_TnppPCfgAutocallTimeout_Object = MibTableColumn
tnppPCfgAutocallTimeout = _TnppPCfgAutocallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 12),
    _TnppPCfgAutocallTimeout_Type()
)
tnppPCfgAutocallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgAutocallTimeout.setStatus("mandatory")


class _TnppPCfgMaxAutocallAttempt_Type(Integer32):
    """Custom type tnppPCfgMaxAutocallAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TnppPCfgMaxAutocallAttempt_Type.__name__ = "Integer32"
_TnppPCfgMaxAutocallAttempt_Object = MibTableColumn
tnppPCfgMaxAutocallAttempt = _TnppPCfgMaxAutocallAttempt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 13),
    _TnppPCfgMaxAutocallAttempt_Type()
)
tnppPCfgMaxAutocallAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgMaxAutocallAttempt.setStatus("mandatory")


class _TnppPCfgProtectionLevel_Type(Integer32):
    """Custom type tnppPCfgProtectionLevel based on Integer32"""
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
        *(("cpOnly", 2),
          ("fullDcp", 3),
          ("nc", 100),
          ("none", 1))
    )


_TnppPCfgProtectionLevel_Type.__name__ = "Integer32"
_TnppPCfgProtectionLevel_Object = MibTableColumn
tnppPCfgProtectionLevel = _TnppPCfgProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 14),
    _TnppPCfgProtectionLevel_Type()
)
tnppPCfgProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgProtectionLevel.setStatus("mandatory")


class _TnppPCfgReconnTimeout_Type(Integer32):
    """Custom type tnppPCfgReconnTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnppPCfgReconnTimeout_Type.__name__ = "Integer32"
_TnppPCfgReconnTimeout_Object = MibTableColumn
tnppPCfgReconnTimeout = _TnppPCfgReconnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 15),
    _TnppPCfgReconnTimeout_Type()
)
tnppPCfgReconnTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgReconnTimeout.setStatus("mandatory")


class _TnppPCfgMaxReconnAttempt_Type(Integer32):
    """Custom type tnppPCfgMaxReconnAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TnppPCfgMaxReconnAttempt_Type.__name__ = "Integer32"
_TnppPCfgMaxReconnAttempt_Object = MibTableColumn
tnppPCfgMaxReconnAttempt = _TnppPCfgMaxReconnAttempt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 16),
    _TnppPCfgMaxReconnAttempt_Type()
)
tnppPCfgMaxReconnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgMaxReconnAttempt.setStatus("mandatory")


class _TnppPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type tnppPCfgElectricalInterfaceType based on Integer32"""
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


_TnppPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_TnppPCfgElectricalInterfaceType_Object = MibTableColumn
tnppPCfgElectricalInterfaceType = _TnppPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 17),
    _TnppPCfgElectricalInterfaceType_Type()
)
tnppPCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgElectricalInterfaceType.setStatus("mandatory")


class _TnppPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type tnppPCfgV24ElectricalInterfaceOption based on Integer32"""
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


_TnppPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_TnppPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
tnppPCfgV24ElectricalInterfaceOption = _TnppPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 18),
    _TnppPCfgV24ElectricalInterfaceOption_Type()
)
tnppPCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _TnppPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type tnppPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_TnppPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_TnppPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
tnppPCfgHighSpeedElectricalInterfaceOption = _TnppPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 19),
    _TnppPCfgHighSpeedElectricalInterfaceOption_Type()
)
tnppPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
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
_Cdx6500PPSTTNPPPStatTable_ObjectIdentity = ObjectIdentity
cdx6500PPSTTNPPPStatTable = _Cdx6500PPSTTNPPPStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33)
)
_TnppPGenStatTable_Object = MibTable
tnppPGenStatTable = _TnppPGenStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1)
)
if mibBuilder.loadTexts:
    tnppPGenStatTable.setStatus("mandatory")
_TnppPGenStatEntry_Object = MibTableRow
tnppPGenStatEntry = _TnppPGenStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1)
)
tnppPGenStatEntry.setIndexNames(
    (0, "TNPP-OPT-MIB", "tnppPGStatPortNumber"),
)
if mibBuilder.loadTexts:
    tnppPGenStatEntry.setStatus("mandatory")


class _TnppPGStatPortNumber_Type(Integer32):
    """Custom type tnppPGStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TnppPGStatPortNumber_Type.__name__ = "Integer32"
_TnppPGStatPortNumber_Object = MibTableColumn
tnppPGStatPortNumber = _TnppPGStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 1),
    _TnppPGStatPortNumber_Type()
)
tnppPGStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortNumber.setStatus("mandatory")


class _TnppPGStatPortType_Type(Integer32):
    """Custom type tnppPGStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            36
        )
    )
    namedValues = NamedValues(
        ("tnpp", 36)
    )


_TnppPGStatPortType_Type.__name__ = "Integer32"
_TnppPGStatPortType_Object = MibTableColumn
tnppPGStatPortType = _TnppPGStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 2),
    _TnppPGStatPortType_Type()
)
tnppPGStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortType.setStatus("mandatory")


class _TnppPGStatPortStatus_Type(Integer32):
    """Custom type tnppPGStatPortStatus based on Integer32"""
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
          ("na", 100),
          ("up", 2))
    )


_TnppPGStatPortStatus_Type.__name__ = "Integer32"
_TnppPGStatPortStatus_Object = MibTableColumn
tnppPGStatPortStatus = _TnppPGStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 3),
    _TnppPGStatPortStatus_Type()
)
tnppPGStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortStatus.setStatus("mandatory")
_TnppPGStatPortSpeed_Type = Integer32
_TnppPGStatPortSpeed_Object = MibTableColumn
tnppPGStatPortSpeed = _TnppPGStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 4),
    _TnppPGStatPortSpeed_Type()
)
tnppPGStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortSpeed.setStatus("mandatory")
_TnppPGStatPortUtilIn_Type = Integer32
_TnppPGStatPortUtilIn_Object = MibTableColumn
tnppPGStatPortUtilIn = _TnppPGStatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 5),
    _TnppPGStatPortUtilIn_Type()
)
tnppPGStatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortUtilIn.setStatus("mandatory")
_TnppPGStatPortUtilOut_Type = Integer32
_TnppPGStatPortUtilOut_Object = MibTableColumn
tnppPGStatPortUtilOut = _TnppPGStatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 6),
    _TnppPGStatPortUtilOut_Type()
)
tnppPGStatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatPortUtilOut.setStatus("mandatory")
_TnppPGStatParityErrors_Type = Counter32
_TnppPGStatParityErrors_Object = MibTableColumn
tnppPGStatParityErrors = _TnppPGStatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 7),
    _TnppPGStatParityErrors_Type()
)
tnppPGStatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatParityErrors.setStatus("mandatory")
_TnppPGStatOverrunErrors_Type = Counter32
_TnppPGStatOverrunErrors_Object = MibTableColumn
tnppPGStatOverrunErrors = _TnppPGStatOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 8),
    _TnppPGStatOverrunErrors_Type()
)
tnppPGStatOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatOverrunErrors.setStatus("mandatory")
_TnppPGStatFramingErrors_Type = Counter32
_TnppPGStatFramingErrors_Object = MibTableColumn
tnppPGStatFramingErrors = _TnppPGStatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 9),
    _TnppPGStatFramingErrors_Type()
)
tnppPGStatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatFramingErrors.setStatus("mandatory")


class _TnppPGStatLocalDTEState_Type(Integer32):
    """Custom type tnppPGStatLocalDTEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("down", 1),
          ("na", 100))
    )


_TnppPGStatLocalDTEState_Type.__name__ = "Integer32"
_TnppPGStatLocalDTEState_Object = MibTableColumn
tnppPGStatLocalDTEState = _TnppPGStatLocalDTEState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 10),
    _TnppPGStatLocalDTEState_Type()
)
tnppPGStatLocalDTEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatLocalDTEState.setStatus("mandatory")


class _TnppPGStatRemoteDTEState_Type(Integer32):
    """Custom type tnppPGStatRemoteDTEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("down", 1),
          ("na", 100))
    )


_TnppPGStatRemoteDTEState_Type.__name__ = "Integer32"
_TnppPGStatRemoteDTEState_Object = MibTableColumn
tnppPGStatRemoteDTEState = _TnppPGStatRemoteDTEState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 11),
    _TnppPGStatRemoteDTEState_Type()
)
tnppPGStatRemoteDTEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatRemoteDTEState.setStatus("mandatory")
_TnppPGStatRemotePadQ_Type = Integer32
_TnppPGStatRemotePadQ_Object = MibTableColumn
tnppPGStatRemotePadQ = _TnppPGStatRemotePadQ_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 12),
    _TnppPGStatRemotePadQ_Type()
)
tnppPGStatRemotePadQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatRemotePadQ.setStatus("mandatory")
_TnppPGStatLocalTerminalQ_Type = Integer32
_TnppPGStatLocalTerminalQ_Object = MibTableColumn
tnppPGStatLocalTerminalQ = _TnppPGStatLocalTerminalQ_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 13),
    _TnppPGStatLocalTerminalQ_Type()
)
tnppPGStatLocalTerminalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatLocalTerminalQ.setStatus("mandatory")
_TnppPGStatReadyQ_Type = Integer32
_TnppPGStatReadyQ_Object = MibTableColumn
tnppPGStatReadyQ = _TnppPGStatReadyQ_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 14),
    _TnppPGStatReadyQ_Type()
)
tnppPGStatReadyQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatReadyQ.setStatus("mandatory")
_TnppPGStatHoldQ_Type = Integer32
_TnppPGStatHoldQ_Object = MibTableColumn
tnppPGStatHoldQ = _TnppPGStatHoldQ_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 15),
    _TnppPGStatHoldQ_Type()
)
tnppPGStatHoldQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPGStatHoldQ.setStatus("mandatory")
_TnppPDataSummaryStatTable_Object = MibTable
tnppPDataSummaryStatTable = _TnppPDataSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2)
)
if mibBuilder.loadTexts:
    tnppPDataSummaryStatTable.setStatus("mandatory")
_TnppPDataSummaryStatEntry_Object = MibTableRow
tnppPDataSummaryStatEntry = _TnppPDataSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1)
)
tnppPDataSummaryStatEntry.setIndexNames(
    (0, "TNPP-OPT-MIB", "tnppPDSStatPortNumber"),
)
if mibBuilder.loadTexts:
    tnppPDataSummaryStatEntry.setStatus("mandatory")


class _TnppPDSStatPortNumber_Type(Integer32):
    """Custom type tnppPDSStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TnppPDSStatPortNumber_Type.__name__ = "Integer32"
_TnppPDSStatPortNumber_Object = MibTableColumn
tnppPDSStatPortNumber = _TnppPDSStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 1),
    _TnppPDSStatPortNumber_Type()
)
tnppPDSStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatPortNumber.setStatus("mandatory")
_TnppPDSStatTotalCharIn_Type = Counter32
_TnppPDSStatTotalCharIn_Object = MibTableColumn
tnppPDSStatTotalCharIn = _TnppPDSStatTotalCharIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 2),
    _TnppPDSStatTotalCharIn_Type()
)
tnppPDSStatTotalCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatTotalCharIn.setStatus("mandatory")
_TnppPDSStatTotalCharOut_Type = Counter32
_TnppPDSStatTotalCharOut_Object = MibTableColumn
tnppPDSStatTotalCharOut = _TnppPDSStatTotalCharOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 3),
    _TnppPDSStatTotalCharOut_Type()
)
tnppPDSStatTotalCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatTotalCharOut.setStatus("mandatory")
_TnppPDSStatTotalFramesIn_Type = Counter32
_TnppPDSStatTotalFramesIn_Object = MibTableColumn
tnppPDSStatTotalFramesIn = _TnppPDSStatTotalFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 4),
    _TnppPDSStatTotalFramesIn_Type()
)
tnppPDSStatTotalFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatTotalFramesIn.setStatus("mandatory")
_TnppPDSStatTotalFramesOut_Type = Counter32
_TnppPDSStatTotalFramesOut_Object = MibTableColumn
tnppPDSStatTotalFramesOut = _TnppPDSStatTotalFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 5),
    _TnppPDSStatTotalFramesOut_Type()
)
tnppPDSStatTotalFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatTotalFramesOut.setStatus("mandatory")
_TnppPDSStatCharInPerSec_Type = Integer32
_TnppPDSStatCharInPerSec_Object = MibTableColumn
tnppPDSStatCharInPerSec = _TnppPDSStatCharInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 6),
    _TnppPDSStatCharInPerSec_Type()
)
tnppPDSStatCharInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatCharInPerSec.setStatus("mandatory")
_TnppPDSStatCharOutPerSec_Type = Integer32
_TnppPDSStatCharOutPerSec_Object = MibTableColumn
tnppPDSStatCharOutPerSec = _TnppPDSStatCharOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 7),
    _TnppPDSStatCharOutPerSec_Type()
)
tnppPDSStatCharOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatCharOutPerSec.setStatus("mandatory")
_TnppPDSStatFramesInPerSec_Type = Integer32
_TnppPDSStatFramesInPerSec_Object = MibTableColumn
tnppPDSStatFramesInPerSec = _TnppPDSStatFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 8),
    _TnppPDSStatFramesInPerSec_Type()
)
tnppPDSStatFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatFramesInPerSec.setStatus("mandatory")
_TnppPDSStatFramesOutPerSec_Type = Integer32
_TnppPDSStatFramesOutPerSec_Object = MibTableColumn
tnppPDSStatFramesOutPerSec = _TnppPDSStatFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 9),
    _TnppPDSStatFramesOutPerSec_Type()
)
tnppPDSStatFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPDSStatFramesOutPerSec.setStatus("mandatory")
_TnppPFrameSummaryStatTable_Object = MibTable
tnppPFrameSummaryStatTable = _TnppPFrameSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3)
)
if mibBuilder.loadTexts:
    tnppPFrameSummaryStatTable.setStatus("mandatory")
_TnppPFrameSummaryStatEntry_Object = MibTableRow
tnppPFrameSummaryStatEntry = _TnppPFrameSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1)
)
tnppPFrameSummaryStatEntry.setIndexNames(
    (0, "TNPP-OPT-MIB", "tnppPFSStatPortNumber"),
)
if mibBuilder.loadTexts:
    tnppPFrameSummaryStatEntry.setStatus("mandatory")


class _TnppPFSStatPortNumber_Type(Integer32):
    """Custom type tnppPFSStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TnppPFSStatPortNumber_Type.__name__ = "Integer32"
_TnppPFSStatPortNumber_Object = MibTableColumn
tnppPFSStatPortNumber = _TnppPFSStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 1),
    _TnppPFSStatPortNumber_Type()
)
tnppPFSStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatPortNumber.setStatus("mandatory")


class _TnppPFSStatLinkState_Type(Integer32):
    """Custom type tnppPFSStatLinkState based on Integer32"""
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
        *(("awaitEnqResp", 2),
          ("init", 1),
          ("na", 100),
          ("ready", 3),
          ("transmitting", 4),
          ("trnsmitResponse", 5))
    )


_TnppPFSStatLinkState_Type.__name__ = "Integer32"
_TnppPFSStatLinkState_Object = MibTableColumn
tnppPFSStatLinkState = _TnppPFSStatLinkState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 2),
    _TnppPFSStatLinkState_Type()
)
tnppPFSStatLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatLinkState.setStatus("mandatory")
_TnppPFSStatCRCErrors_Type = Counter32
_TnppPFSStatCRCErrors_Object = MibTableColumn
tnppPFSStatCRCErrors = _TnppPFSStatCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 3),
    _TnppPFSStatCRCErrors_Type()
)
tnppPFSStatCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatCRCErrors.setStatus("mandatory")
_TnppPFSStatLinkFramingErrors_Type = Counter32
_TnppPFSStatLinkFramingErrors_Object = MibTableColumn
tnppPFSStatLinkFramingErrors = _TnppPFSStatLinkFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 4),
    _TnppPFSStatLinkFramingErrors_Type()
)
tnppPFSStatLinkFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatLinkFramingErrors.setStatus("mandatory")
_TnppPFSStatProtocolErrors_Type = Counter32
_TnppPFSStatProtocolErrors_Object = MibTableColumn
tnppPFSStatProtocolErrors = _TnppPFSStatProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 5),
    _TnppPFSStatProtocolErrors_Type()
)
tnppPFSStatProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatProtocolErrors.setStatus("mandatory")
_TnppPFSStatACKFramesIn_Type = Counter32
_TnppPFSStatACKFramesIn_Object = MibTableColumn
tnppPFSStatACKFramesIn = _TnppPFSStatACKFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 6),
    _TnppPFSStatACKFramesIn_Type()
)
tnppPFSStatACKFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatACKFramesIn.setStatus("mandatory")
_TnppPFSStatACKFramesOut_Type = Counter32
_TnppPFSStatACKFramesOut_Object = MibTableColumn
tnppPFSStatACKFramesOut = _TnppPFSStatACKFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 7),
    _TnppPFSStatACKFramesOut_Type()
)
tnppPFSStatACKFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatACKFramesOut.setStatus("mandatory")
_TnppPFSStatNAKFramesIn_Type = Counter32
_TnppPFSStatNAKFramesIn_Object = MibTableColumn
tnppPFSStatNAKFramesIn = _TnppPFSStatNAKFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 8),
    _TnppPFSStatNAKFramesIn_Type()
)
tnppPFSStatNAKFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatNAKFramesIn.setStatus("mandatory")
_TnppPFSStatNAKFramesOut_Type = Counter32
_TnppPFSStatNAKFramesOut_Object = MibTableColumn
tnppPFSStatNAKFramesOut = _TnppPFSStatNAKFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 9),
    _TnppPFSStatNAKFramesOut_Type()
)
tnppPFSStatNAKFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatNAKFramesOut.setStatus("mandatory")
_TnppPFSStatRSFramesIn_Type = Counter32
_TnppPFSStatRSFramesIn_Object = MibTableColumn
tnppPFSStatRSFramesIn = _TnppPFSStatRSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 10),
    _TnppPFSStatRSFramesIn_Type()
)
tnppPFSStatRSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatRSFramesIn.setStatus("mandatory")
_TnppPFSStatRSFramesOut_Type = Counter32
_TnppPFSStatRSFramesOut_Object = MibTableColumn
tnppPFSStatRSFramesOut = _TnppPFSStatRSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 11),
    _TnppPFSStatRSFramesOut_Type()
)
tnppPFSStatRSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatRSFramesOut.setStatus("mandatory")
_TnppPFSStatCANFramesIn_Type = Counter32
_TnppPFSStatCANFramesIn_Object = MibTableColumn
tnppPFSStatCANFramesIn = _TnppPFSStatCANFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 12),
    _TnppPFSStatCANFramesIn_Type()
)
tnppPFSStatCANFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatCANFramesIn.setStatus("mandatory")
_TnppPFSStatCANFramesOut_Type = Counter32
_TnppPFSStatCANFramesOut_Object = MibTableColumn
tnppPFSStatCANFramesOut = _TnppPFSStatCANFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 13),
    _TnppPFSStatCANFramesOut_Type()
)
tnppPFSStatCANFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatCANFramesOut.setStatus("mandatory")
_TnppPFSStatEOTFramesIn_Type = Counter32
_TnppPFSStatEOTFramesIn_Object = MibTableColumn
tnppPFSStatEOTFramesIn = _TnppPFSStatEOTFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 14),
    _TnppPFSStatEOTFramesIn_Type()
)
tnppPFSStatEOTFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatEOTFramesIn.setStatus("mandatory")
_TnppPFSStatEOTFramesOut_Type = Counter32
_TnppPFSStatEOTFramesOut_Object = MibTableColumn
tnppPFSStatEOTFramesOut = _TnppPFSStatEOTFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 15),
    _TnppPFSStatEOTFramesOut_Type()
)
tnppPFSStatEOTFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatEOTFramesOut.setStatus("mandatory")
_TnppPFSStatENQFramesIn_Type = Counter32
_TnppPFSStatENQFramesIn_Object = MibTableColumn
tnppPFSStatENQFramesIn = _TnppPFSStatENQFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 16),
    _TnppPFSStatENQFramesIn_Type()
)
tnppPFSStatENQFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatENQFramesIn.setStatus("mandatory")
_TnppPFSStatENQFramesOut_Type = Counter32
_TnppPFSStatENQFramesOut_Object = MibTableColumn
tnppPFSStatENQFramesOut = _TnppPFSStatENQFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 17),
    _TnppPFSStatENQFramesOut_Type()
)
tnppPFSStatENQFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatENQFramesOut.setStatus("mandatory")
_TnppPFSStatDataFramesInPassed_Type = Counter32
_TnppPFSStatDataFramesInPassed_Object = MibTableColumn
tnppPFSStatDataFramesInPassed = _TnppPFSStatDataFramesInPassed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 18),
    _TnppPFSStatDataFramesInPassed_Type()
)
tnppPFSStatDataFramesInPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatDataFramesInPassed.setStatus("mandatory")
_TnppPFSStatDataFramesOutPassed_Type = Counter32
_TnppPFSStatDataFramesOutPassed_Object = MibTableColumn
tnppPFSStatDataFramesOutPassed = _TnppPFSStatDataFramesOutPassed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 19),
    _TnppPFSStatDataFramesOutPassed_Type()
)
tnppPFSStatDataFramesOutPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatDataFramesOutPassed.setStatus("mandatory")
_TnppPFSStatDataFramesInDiscarded_Type = Counter32
_TnppPFSStatDataFramesInDiscarded_Object = MibTableColumn
tnppPFSStatDataFramesInDiscarded = _TnppPFSStatDataFramesInDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 20),
    _TnppPFSStatDataFramesInDiscarded_Type()
)
tnppPFSStatDataFramesInDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatDataFramesInDiscarded.setStatus("mandatory")
_TnppPFSStatDataFramesOutDiscarded_Type = Counter32
_TnppPFSStatDataFramesOutDiscarded_Object = MibTableColumn
tnppPFSStatDataFramesOutDiscarded = _TnppPFSStatDataFramesOutDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 21),
    _TnppPFSStatDataFramesOutDiscarded_Type()
)
tnppPFSStatDataFramesOutDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnppPFSStatDataFramesOutDiscarded.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContTNPPTable_ObjectIdentity = ObjectIdentity
cdx6500ContTNPPTable = _Cdx6500ContTNPPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15)
)
_Cdx6500ContTNPPPortTable_Object = MibTable
cdx6500ContTNPPPortTable = _Cdx6500ContTNPPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContTNPPPortTable.setStatus("mandatory")
_Cdx6500ContTNPPPortEntry_Object = MibTableRow
cdx6500ContTNPPPortEntry = _Cdx6500ContTNPPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1)
)
cdx6500ContTNPPPortEntry.setIndexNames(
    (0, "TNPP-OPT-MIB", "tnppPContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ContTNPPPortEntry.setStatus("mandatory")


class _TnppPContPortNumber_Type(Integer32):
    """Custom type tnppPContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TnppPContPortNumber_Type.__name__ = "Integer32"
_TnppPContPortNumber_Object = MibTableColumn
tnppPContPortNumber = _TnppPContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1, 1),
    _TnppPContPortNumber_Type()
)
tnppPContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnppPContPortNumber.setStatus("mandatory")


class _TnppPContPortControl_Type(Integer32):
    """Custom type tnppPContPortControl based on Integer32"""
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
        *(("boot", 1),
          ("busyout", 4),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 5))
    )


_TnppPContPortControl_Type.__name__ = "Integer32"
_TnppPContPortControl_Object = MibTableColumn
tnppPContPortControl = _TnppPContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1, 2),
    _TnppPContPortControl_Type()
)
tnppPContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tnppPContPortControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TNPP-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTTNPPPortTable": cdx6500PPCTTNPPPortTable,
       "cdx6500PPCTTNPPPortEntry": cdx6500PPCTTNPPPortEntry,
       "tnppPCfgPortNumber": tnppPCfgPortNumber,
       "tnppPCfgPortType": tnppPCfgPortType,
       "tnppPCfgPortSpeed": tnppPCfgPortSpeed,
       "tnppPCfgCallControl": tnppPCfgCallControl,
       "tnppPCfgCRCOption": tnppPCfgCRCOption,
       "tnppPCfgTANControl": tnppPCfgTANControl,
       "tnppPCfgCANReports": tnppPCfgCANReports,
       "tnppPCfgRSCount": tnppPCfgRSCount,
       "tnppPCfgMaxRSCount": tnppPCfgMaxRSCount,
       "tnppPCfgRSSupport": tnppPCfgRSSupport,
       "tnppPCfgAutocallMnemonic": tnppPCfgAutocallMnemonic,
       "tnppPCfgAutocallTimeout": tnppPCfgAutocallTimeout,
       "tnppPCfgMaxAutocallAttempt": tnppPCfgMaxAutocallAttempt,
       "tnppPCfgProtectionLevel": tnppPCfgProtectionLevel,
       "tnppPCfgReconnTimeout": tnppPCfgReconnTimeout,
       "tnppPCfgMaxReconnAttempt": tnppPCfgMaxReconnAttempt,
       "tnppPCfgElectricalInterfaceType": tnppPCfgElectricalInterfaceType,
       "tnppPCfgV24ElectricalInterfaceOption": tnppPCfgV24ElectricalInterfaceOption,
       "tnppPCfgHighSpeedElectricalInterfaceOption": tnppPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTTNPPPStatTable": cdx6500PPSTTNPPPStatTable,
       "tnppPGenStatTable": tnppPGenStatTable,
       "tnppPGenStatEntry": tnppPGenStatEntry,
       "tnppPGStatPortNumber": tnppPGStatPortNumber,
       "tnppPGStatPortType": tnppPGStatPortType,
       "tnppPGStatPortStatus": tnppPGStatPortStatus,
       "tnppPGStatPortSpeed": tnppPGStatPortSpeed,
       "tnppPGStatPortUtilIn": tnppPGStatPortUtilIn,
       "tnppPGStatPortUtilOut": tnppPGStatPortUtilOut,
       "tnppPGStatParityErrors": tnppPGStatParityErrors,
       "tnppPGStatOverrunErrors": tnppPGStatOverrunErrors,
       "tnppPGStatFramingErrors": tnppPGStatFramingErrors,
       "tnppPGStatLocalDTEState": tnppPGStatLocalDTEState,
       "tnppPGStatRemoteDTEState": tnppPGStatRemoteDTEState,
       "tnppPGStatRemotePadQ": tnppPGStatRemotePadQ,
       "tnppPGStatLocalTerminalQ": tnppPGStatLocalTerminalQ,
       "tnppPGStatReadyQ": tnppPGStatReadyQ,
       "tnppPGStatHoldQ": tnppPGStatHoldQ,
       "tnppPDataSummaryStatTable": tnppPDataSummaryStatTable,
       "tnppPDataSummaryStatEntry": tnppPDataSummaryStatEntry,
       "tnppPDSStatPortNumber": tnppPDSStatPortNumber,
       "tnppPDSStatTotalCharIn": tnppPDSStatTotalCharIn,
       "tnppPDSStatTotalCharOut": tnppPDSStatTotalCharOut,
       "tnppPDSStatTotalFramesIn": tnppPDSStatTotalFramesIn,
       "tnppPDSStatTotalFramesOut": tnppPDSStatTotalFramesOut,
       "tnppPDSStatCharInPerSec": tnppPDSStatCharInPerSec,
       "tnppPDSStatCharOutPerSec": tnppPDSStatCharOutPerSec,
       "tnppPDSStatFramesInPerSec": tnppPDSStatFramesInPerSec,
       "tnppPDSStatFramesOutPerSec": tnppPDSStatFramesOutPerSec,
       "tnppPFrameSummaryStatTable": tnppPFrameSummaryStatTable,
       "tnppPFrameSummaryStatEntry": tnppPFrameSummaryStatEntry,
       "tnppPFSStatPortNumber": tnppPFSStatPortNumber,
       "tnppPFSStatLinkState": tnppPFSStatLinkState,
       "tnppPFSStatCRCErrors": tnppPFSStatCRCErrors,
       "tnppPFSStatLinkFramingErrors": tnppPFSStatLinkFramingErrors,
       "tnppPFSStatProtocolErrors": tnppPFSStatProtocolErrors,
       "tnppPFSStatACKFramesIn": tnppPFSStatACKFramesIn,
       "tnppPFSStatACKFramesOut": tnppPFSStatACKFramesOut,
       "tnppPFSStatNAKFramesIn": tnppPFSStatNAKFramesIn,
       "tnppPFSStatNAKFramesOut": tnppPFSStatNAKFramesOut,
       "tnppPFSStatRSFramesIn": tnppPFSStatRSFramesIn,
       "tnppPFSStatRSFramesOut": tnppPFSStatRSFramesOut,
       "tnppPFSStatCANFramesIn": tnppPFSStatCANFramesIn,
       "tnppPFSStatCANFramesOut": tnppPFSStatCANFramesOut,
       "tnppPFSStatEOTFramesIn": tnppPFSStatEOTFramesIn,
       "tnppPFSStatEOTFramesOut": tnppPFSStatEOTFramesOut,
       "tnppPFSStatENQFramesIn": tnppPFSStatENQFramesIn,
       "tnppPFSStatENQFramesOut": tnppPFSStatENQFramesOut,
       "tnppPFSStatDataFramesInPassed": tnppPFSStatDataFramesInPassed,
       "tnppPFSStatDataFramesOutPassed": tnppPFSStatDataFramesOutPassed,
       "tnppPFSStatDataFramesInDiscarded": tnppPFSStatDataFramesInDiscarded,
       "tnppPFSStatDataFramesOutDiscarded": tnppPFSStatDataFramesOutDiscarded,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContTNPPTable": cdx6500ContTNPPTable,
       "cdx6500ContTNPPPortTable": cdx6500ContTNPPPortTable,
       "cdx6500ContTNPPPortEntry": cdx6500ContTNPPPortEntry,
       "tnppPContPortNumber": tnppPContPortNumber,
       "tnppPContPortControl": tnppPContPortControl}
)
