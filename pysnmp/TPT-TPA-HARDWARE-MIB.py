# SNMP MIB module (TPT-TPA-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-TPA-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:13 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_tpa_hardware_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3)
)
tpt_tpa_hardware_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ManagedElementType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 2),
          ("chassis", 1),
          ("controller", 3),
          ("fan-controller", 19),
          ("fan-sub-unit", 20),
          ("feature-card", 7),
          ("forty-gige-port", 24),
          ("gige-port", 8),
          ("hundred-base-t-port", 10),
          ("network-interface", 4),
          ("network-interface-bcomm", 5),
          ("network-processor", 6),
          ("power-entry-module", 21),
          ("power-supply", 17),
          ("power-supply-sub-unit", 18),
          ("sdh-atm-port", 14),
          ("sdh-pos-port", 15),
          ("sdh-pos-srp-port", 16),
          ("sonet-atm-port", 11),
          ("sonet-pos-port", 12),
          ("sonet-pos-srp-port", 13),
          ("ten-base-t-port", 9),
          ("ten-gige-port", 23),
          ("unequip", 0),
          ("vnam-port", 22))
    )



class ConfigRedundancy(Integer32, TextualConvention):
    status = "current"
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
        *(("autonomous", 4),
          ("duplex", 2),
          ("loadshare", 3),
          ("simplex", 1),
          ("unconfigured", 0))
    )



class HardwareState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("act", 2),
          ("act-dgrd", 8),
          ("act-faf", 6),
          ("dgn", 4),
          ("initialize", 1),
          ("lpbk", 5),
          ("oos", 0),
          ("stby", 3),
          ("stby-dgrd", 9),
          ("stby-faf", 7))
    )



class HardwareStateQual(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("blade-insert", 19),
          ("blade-pull", 18),
          ("blade-slot-mismatch", 20),
          ("crc-err", 16),
          ("degraded", 1),
          ("inhibit", 29),
          ("init-failure", 21),
          ("no-info", 24),
          ("over-temp-alarm", 25),
          ("parent-oos", 22),
          ("parity-err", 15),
          ("port-ais-l", 9),
          ("port-ais-p", 8),
          ("port-clear", 0),
          ("port-forced", 11),
          ("port-lockout", 12),
          ("port-lof", 3),
          ("port-lop", 5),
          ("port-los", 2),
          ("port-oof", 4),
          ("port-ool", 27),
          ("port-ool-clear", 28),
          ("port-rdi", 10),
          ("port-signal-degrade", 6),
          ("port-signal-failure", 7),
          ("red-alarm", 14),
          ("removed", 23),
          ("under-temp-alarm", 26),
          ("unequipped-slot", 17),
          ("yellow-alarm", 13))
    )



class ExtendedSlot(Integer32, TextualConvention):
    status = "current"
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
        *(("fan", 12),
          ("pem", 10),
          ("power-supply", 11),
          ("shelf", 9),
          ("slot1", 1),
          ("slot11", 13),
          ("slot12", 14),
          ("slot13", 15),
          ("slot14", 16),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8))
    )



class LineType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("copper", 21),
          ("copper-sfp", 23),
          ("optical", 22),
          ("undefined", 0))
    )



class DuplexState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unknown", 0))
    )



class SfpQualifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("qsfp-plus-absent", 26),
          ("sfp-1000base-cx", 10),
          ("sfp-1000base-lx", 11),
          ("sfp-1000base-sx", 12),
          ("sfp-1000base-t", 9),
          ("sfp-100base-fx", 7),
          ("sfp-100base-lx-lx10", 8),
          ("sfp-10g-base-er", 1),
          ("sfp-10g-base-lr", 3),
          ("sfp-10g-base-lrm", 2),
          ("sfp-10g-base-sr", 4),
          ("sfp-10g-dac", 28),
          ("sfp-10g-dao", 29),
          ("sfp-1310-nm-dfb", 17),
          ("sfp-1310-nm-eml", 19),
          ("sfp-1310-nm-fp", 16),
          ("sfp-1310-nm-vcsel", 14),
          ("sfp-1490-nm-dfb", 22),
          ("sfp-1550-nm-dfb", 18),
          ("sfp-1550-nm-eml", 20),
          ("sfp-1550-nm-vcsel", 15),
          ("sfp-850-nm-vcsel", 13),
          ("sfp-absent", 24),
          ("sfp-base-bx10", 6),
          ("sfp-base-px", 5),
          ("sfp-copper-cable-unequalized", 23),
          ("sfp-copper-or-others", 21),
          ("sfp-not-applicable", 0),
          ("sfp-plus-absent", 25),
          ("sfp-xfp-absent", 27))
    )



# MIB Managed Objects in the order of their OIDs

_Hw_slotTable_Object = MibTable
hw_slotTable = _Hw_slotTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hw_slotTable.setStatus("current")
_Hw_slotEntry_Object = MibTableRow
hw_slotEntry = _Hw_slotEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1)
)
hw_slotEntry.setIndexNames(
    (0, "TPT-TPA-HARDWARE-MIB", "slotNumber"),
    (0, "TPT-TPA-HARDWARE-MIB", "slotPort"),
)
if mibBuilder.loadTexts:
    hw_slotEntry.setStatus("current")
_SlotNumber_Type = Unsigned32
_SlotNumber_Object = MibTableColumn
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 1),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNumber.setStatus("current")
_SlotPort_Type = Unsigned32
_SlotPort_Object = MibTableColumn
slotPort = _SlotPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 2),
    _SlotPort_Type()
)
slotPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPort.setStatus("current")
_SlotType_Type = ManagedElementType
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 3),
    _SlotType_Type()
)
slotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotType.setStatus("current")
_SlotCfgType_Type = ConfigRedundancy
_SlotCfgType_Object = MibTableColumn
slotCfgType = _SlotCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 4),
    _SlotCfgType_Type()
)
slotCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCfgType.setStatus("current")
_SlotRunState_Type = HardwareState
_SlotRunState_Object = MibTableColumn
slotRunState = _SlotRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 5),
    _SlotRunState_Type()
)
slotRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotRunState.setStatus("current")
_SlotQualifier1_Type = HardwareStateQual
_SlotQualifier1_Object = MibTableColumn
slotQualifier1 = _SlotQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 6),
    _SlotQualifier1_Type()
)
slotQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotQualifier1.setStatus("current")
_SlotQualifier2_Type = HardwareStateQual
_SlotQualifier2_Object = MibTableColumn
slotQualifier2 = _SlotQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 7),
    _SlotQualifier2_Type()
)
slotQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotQualifier2.setStatus("current")
_SlotQualifier3_Type = HardwareStateQual
_SlotQualifier3_Object = MibTableColumn
slotQualifier3 = _SlotQualifier3_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 8),
    _SlotQualifier3_Type()
)
slotQualifier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotQualifier3.setStatus("current")
_SlotQualifier4_Type = HardwareStateQual
_SlotQualifier4_Object = MibTableColumn
slotQualifier4 = _SlotQualifier4_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 9),
    _SlotQualifier4_Type()
)
slotQualifier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotQualifier4.setStatus("current")
_SlotStartTime_Type = Unsigned32
_SlotStartTime_Object = MibTableColumn
slotStartTime = _SlotStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 10),
    _SlotStartTime_Type()
)
slotStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStartTime.setStatus("current")
_SlotVendorID_Type = Unsigned32
_SlotVendorID_Object = MibTableColumn
slotVendorID = _SlotVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 11),
    _SlotVendorID_Type()
)
slotVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotVendorID.setStatus("current")
_SlotDeviceID_Type = Unsigned32
_SlotDeviceID_Object = MibTableColumn
slotDeviceID = _SlotDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 12),
    _SlotDeviceID_Type()
)
slotDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotDeviceID.setStatus("current")


class _SlotProductID_Type(OctetString):
    """Custom type slotProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlotProductID_Type.__name__ = "OctetString"
_SlotProductID_Object = MibTableColumn
slotProductID = _SlotProductID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 13),
    _SlotProductID_Type()
)
slotProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotProductID.setStatus("current")
_SlotFPGAVersion_Type = Unsigned32
_SlotFPGAVersion_Object = MibTableColumn
slotFPGAVersion = _SlotFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 14),
    _SlotFPGAVersion_Type()
)
slotFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFPGAVersion.setStatus("current")
_SlotInterface_Type = InterfaceIndex
_SlotInterface_Object = MibTableColumn
slotInterface = _SlotInterface_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 15),
    _SlotInterface_Type()
)
slotInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInterface.setStatus("current")
_SlotLineType_Type = LineType
_SlotLineType_Object = MibTableColumn
slotLineType = _SlotLineType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 16),
    _SlotLineType_Type()
)
slotLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLineType.setStatus("current")
_SlotDuplexState_Type = DuplexState
_SlotDuplexState_Object = MibTableColumn
slotDuplexState = _SlotDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 17),
    _SlotDuplexState_Type()
)
slotDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotDuplexState.setStatus("current")
_SlotPhysical_Type = Unsigned32
_SlotPhysical_Object = MibTableColumn
slotPhysical = _SlotPhysical_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 18),
    _SlotPhysical_Type()
)
slotPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPhysical.setStatus("current")
_SlotSfpQualifier1_Type = SfpQualifier
_SlotSfpQualifier1_Object = MibTableColumn
slotSfpQualifier1 = _SlotSfpQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 19),
    _SlotSfpQualifier1_Type()
)
slotSfpQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSfpQualifier1.setStatus("current")
_SlotSfpQualifier2_Type = SfpQualifier
_SlotSfpQualifier2_Object = MibTableColumn
slotSfpQualifier2 = _SlotSfpQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 1, 1, 20),
    _SlotSfpQualifier2_Type()
)
slotSfpQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSfpQualifier2.setStatus("current")
_Hw_chasTable_Object = MibTable
hw_chasTable = _Hw_chasTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hw_chasTable.setStatus("current")
_Hw_chasEntry_Object = MibTableRow
hw_chasEntry = _Hw_chasEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1)
)
hw_chasEntry.setIndexNames(
    (0, "TPT-TPA-HARDWARE-MIB", "chasNumber"),
)
if mibBuilder.loadTexts:
    hw_chasEntry.setStatus("current")
_ChasNumber_Type = Unsigned32
_ChasNumber_Object = MibTableColumn
chasNumber = _ChasNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 1),
    _ChasNumber_Type()
)
chasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNumber.setStatus("current")
_ChasType_Type = ManagedElementType
_ChasType_Object = MibTableColumn
chasType = _ChasType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 3),
    _ChasType_Type()
)
chasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasType.setStatus("current")
_ChasCfgType_Type = ConfigRedundancy
_ChasCfgType_Object = MibTableColumn
chasCfgType = _ChasCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 4),
    _ChasCfgType_Type()
)
chasCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCfgType.setStatus("current")
_ChasRunState_Type = HardwareState
_ChasRunState_Object = MibTableColumn
chasRunState = _ChasRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 5),
    _ChasRunState_Type()
)
chasRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRunState.setStatus("current")
_ChasQualifier1_Type = HardwareStateQual
_ChasQualifier1_Object = MibTableColumn
chasQualifier1 = _ChasQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 6),
    _ChasQualifier1_Type()
)
chasQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasQualifier1.setStatus("current")
_ChasQualifier2_Type = HardwareStateQual
_ChasQualifier2_Object = MibTableColumn
chasQualifier2 = _ChasQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 7),
    _ChasQualifier2_Type()
)
chasQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasQualifier2.setStatus("current")
_ChasQualifier3_Type = HardwareStateQual
_ChasQualifier3_Object = MibTableColumn
chasQualifier3 = _ChasQualifier3_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 8),
    _ChasQualifier3_Type()
)
chasQualifier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasQualifier3.setStatus("current")
_ChasQualifier4_Type = HardwareStateQual
_ChasQualifier4_Object = MibTableColumn
chasQualifier4 = _ChasQualifier4_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 9),
    _ChasQualifier4_Type()
)
chasQualifier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasQualifier4.setStatus("current")
_ChasStartTime_Type = Unsigned32
_ChasStartTime_Object = MibTableColumn
chasStartTime = _ChasStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 10),
    _ChasStartTime_Type()
)
chasStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasStartTime.setStatus("current")
_ChasVendorID_Type = Unsigned32
_ChasVendorID_Object = MibTableColumn
chasVendorID = _ChasVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 11),
    _ChasVendorID_Type()
)
chasVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasVendorID.setStatus("current")
_ChasDeviceID_Type = Unsigned32
_ChasDeviceID_Object = MibTableColumn
chasDeviceID = _ChasDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 12),
    _ChasDeviceID_Type()
)
chasDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasDeviceID.setStatus("current")


class _ChasProductID_Type(OctetString):
    """Custom type chasProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasProductID_Type.__name__ = "OctetString"
_ChasProductID_Object = MibTableColumn
chasProductID = _ChasProductID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 13),
    _ChasProductID_Type()
)
chasProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasProductID.setStatus("current")
_ChasFPGAVersion_Type = Unsigned32
_ChasFPGAVersion_Object = MibTableColumn
chasFPGAVersion = _ChasFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 2, 1, 14),
    _ChasFPGAVersion_Type()
)
chasFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFPGAVersion.setStatus("current")
_Hw_fanTable_Object = MibTable
hw_fanTable = _Hw_fanTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    hw_fanTable.setStatus("current")
_Hw_fanEntry_Object = MibTableRow
hw_fanEntry = _Hw_fanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1)
)
hw_fanEntry.setIndexNames(
    (0, "TPT-TPA-HARDWARE-MIB", "fanSubunit"),
)
if mibBuilder.loadTexts:
    hw_fanEntry.setStatus("current")
_FanSubunit_Type = Unsigned32
_FanSubunit_Object = MibTableColumn
fanSubunit = _FanSubunit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 1),
    _FanSubunit_Type()
)
fanSubunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSubunit.setStatus("current")
_FanType_Type = ManagedElementType
_FanType_Object = MibTableColumn
fanType = _FanType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 3),
    _FanType_Type()
)
fanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanType.setStatus("current")
_FanCfgType_Type = ConfigRedundancy
_FanCfgType_Object = MibTableColumn
fanCfgType = _FanCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 4),
    _FanCfgType_Type()
)
fanCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCfgType.setStatus("current")
_FanRunState_Type = HardwareState
_FanRunState_Object = MibTableColumn
fanRunState = _FanRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 5),
    _FanRunState_Type()
)
fanRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRunState.setStatus("current")
_FanQualifier1_Type = HardwareStateQual
_FanQualifier1_Object = MibTableColumn
fanQualifier1 = _FanQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 6),
    _FanQualifier1_Type()
)
fanQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanQualifier1.setStatus("current")
_FanQualifier2_Type = HardwareStateQual
_FanQualifier2_Object = MibTableColumn
fanQualifier2 = _FanQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 7),
    _FanQualifier2_Type()
)
fanQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanQualifier2.setStatus("current")
_FanQualifier3_Type = HardwareStateQual
_FanQualifier3_Object = MibTableColumn
fanQualifier3 = _FanQualifier3_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 8),
    _FanQualifier3_Type()
)
fanQualifier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanQualifier3.setStatus("current")
_FanQualifier4_Type = HardwareStateQual
_FanQualifier4_Object = MibTableColumn
fanQualifier4 = _FanQualifier4_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 9),
    _FanQualifier4_Type()
)
fanQualifier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanQualifier4.setStatus("current")
_FanStartTime_Type = Unsigned32
_FanStartTime_Object = MibTableColumn
fanStartTime = _FanStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 10),
    _FanStartTime_Type()
)
fanStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStartTime.setStatus("current")
_FanVendorID_Type = Unsigned32
_FanVendorID_Object = MibTableColumn
fanVendorID = _FanVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 11),
    _FanVendorID_Type()
)
fanVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanVendorID.setStatus("current")
_FanDeviceID_Type = Unsigned32
_FanDeviceID_Object = MibTableColumn
fanDeviceID = _FanDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 12),
    _FanDeviceID_Type()
)
fanDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDeviceID.setStatus("current")


class _FanProductID_Type(OctetString):
    """Custom type fanProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FanProductID_Type.__name__ = "OctetString"
_FanProductID_Object = MibTableColumn
fanProductID = _FanProductID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 13),
    _FanProductID_Type()
)
fanProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProductID.setStatus("current")
_FanFPGAVersion_Type = Unsigned32
_FanFPGAVersion_Object = MibTableColumn
fanFPGAVersion = _FanFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 3, 1, 14),
    _FanFPGAVersion_Type()
)
fanFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFPGAVersion.setStatus("current")
_Hw_psTable_Object = MibTable
hw_psTable = _Hw_psTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    hw_psTable.setStatus("current")
_Hw_psEntry_Object = MibTableRow
hw_psEntry = _Hw_psEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1)
)
hw_psEntry.setIndexNames(
    (0, "TPT-TPA-HARDWARE-MIB", "psSubunit"),
)
if mibBuilder.loadTexts:
    hw_psEntry.setStatus("current")
_PsSubunit_Type = Unsigned32
_PsSubunit_Object = MibTableColumn
psSubunit = _PsSubunit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 1),
    _PsSubunit_Type()
)
psSubunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSubunit.setStatus("current")
_PsType_Type = ManagedElementType
_PsType_Object = MibTableColumn
psType = _PsType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 3),
    _PsType_Type()
)
psType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psType.setStatus("current")
_PsCfgType_Type = ConfigRedundancy
_PsCfgType_Object = MibTableColumn
psCfgType = _PsCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 4),
    _PsCfgType_Type()
)
psCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psCfgType.setStatus("current")
_PsRunState_Type = HardwareState
_PsRunState_Object = MibTableColumn
psRunState = _PsRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 5),
    _PsRunState_Type()
)
psRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRunState.setStatus("current")
_PsQualifier1_Type = HardwareStateQual
_PsQualifier1_Object = MibTableColumn
psQualifier1 = _PsQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 6),
    _PsQualifier1_Type()
)
psQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psQualifier1.setStatus("current")
_PsQualifier2_Type = HardwareStateQual
_PsQualifier2_Object = MibTableColumn
psQualifier2 = _PsQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 7),
    _PsQualifier2_Type()
)
psQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psQualifier2.setStatus("current")
_PsQualifier3_Type = HardwareStateQual
_PsQualifier3_Object = MibTableColumn
psQualifier3 = _PsQualifier3_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 8),
    _PsQualifier3_Type()
)
psQualifier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psQualifier3.setStatus("current")
_PsQualifier4_Type = HardwareStateQual
_PsQualifier4_Object = MibTableColumn
psQualifier4 = _PsQualifier4_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 9),
    _PsQualifier4_Type()
)
psQualifier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psQualifier4.setStatus("current")
_PsStartTime_Type = Unsigned32
_PsStartTime_Object = MibTableColumn
psStartTime = _PsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 10),
    _PsStartTime_Type()
)
psStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStartTime.setStatus("current")
_PsVendorID_Type = Unsigned32
_PsVendorID_Object = MibTableColumn
psVendorID = _PsVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 11),
    _PsVendorID_Type()
)
psVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVendorID.setStatus("current")
_PsDeviceID_Type = Unsigned32
_PsDeviceID_Object = MibTableColumn
psDeviceID = _PsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 12),
    _PsDeviceID_Type()
)
psDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceID.setStatus("current")


class _PsProductID_Type(OctetString):
    """Custom type psProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PsProductID_Type.__name__ = "OctetString"
_PsProductID_Object = MibTableColumn
psProductID = _PsProductID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 13),
    _PsProductID_Type()
)
psProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProductID.setStatus("current")
_PsFPGAVersion_Type = Unsigned32
_PsFPGAVersion_Object = MibTableColumn
psFPGAVersion = _PsFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 4, 1, 14),
    _PsFPGAVersion_Type()
)
psFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFPGAVersion.setStatus("current")
_Hw_pemTable_Object = MibTable
hw_pemTable = _Hw_pemTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    hw_pemTable.setStatus("current")
_Hw_pemEntry_Object = MibTableRow
hw_pemEntry = _Hw_pemEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1)
)
hw_pemEntry.setIndexNames(
    (0, "TPT-TPA-HARDWARE-MIB", "pemSubunit"),
)
if mibBuilder.loadTexts:
    hw_pemEntry.setStatus("current")
_PemSubunit_Type = Unsigned32
_PemSubunit_Object = MibTableColumn
pemSubunit = _PemSubunit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 1),
    _PemSubunit_Type()
)
pemSubunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemSubunit.setStatus("current")
_PemType_Type = ManagedElementType
_PemType_Object = MibTableColumn
pemType = _PemType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 3),
    _PemType_Type()
)
pemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemType.setStatus("current")
_PemCfgType_Type = ConfigRedundancy
_PemCfgType_Object = MibTableColumn
pemCfgType = _PemCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 4),
    _PemCfgType_Type()
)
pemCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemCfgType.setStatus("current")
_PemRunState_Type = HardwareState
_PemRunState_Object = MibTableColumn
pemRunState = _PemRunState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 5),
    _PemRunState_Type()
)
pemRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemRunState.setStatus("current")
_PemQualifier1_Type = HardwareStateQual
_PemQualifier1_Object = MibTableColumn
pemQualifier1 = _PemQualifier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 6),
    _PemQualifier1_Type()
)
pemQualifier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemQualifier1.setStatus("current")
_PemQualifier2_Type = HardwareStateQual
_PemQualifier2_Object = MibTableColumn
pemQualifier2 = _PemQualifier2_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 7),
    _PemQualifier2_Type()
)
pemQualifier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemQualifier2.setStatus("current")
_PemQualifier3_Type = HardwareStateQual
_PemQualifier3_Object = MibTableColumn
pemQualifier3 = _PemQualifier3_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 8),
    _PemQualifier3_Type()
)
pemQualifier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemQualifier3.setStatus("current")
_PemQualifier4_Type = HardwareStateQual
_PemQualifier4_Object = MibTableColumn
pemQualifier4 = _PemQualifier4_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 9),
    _PemQualifier4_Type()
)
pemQualifier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemQualifier4.setStatus("current")
_PemStartTime_Type = Unsigned32
_PemStartTime_Object = MibTableColumn
pemStartTime = _PemStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 10),
    _PemStartTime_Type()
)
pemStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemStartTime.setStatus("current")
_PemVendorID_Type = Unsigned32
_PemVendorID_Object = MibTableColumn
pemVendorID = _PemVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 11),
    _PemVendorID_Type()
)
pemVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemVendorID.setStatus("current")
_PemDeviceID_Type = Unsigned32
_PemDeviceID_Object = MibTableColumn
pemDeviceID = _PemDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 12),
    _PemDeviceID_Type()
)
pemDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemDeviceID.setStatus("current")


class _PemProductID_Type(OctetString):
    """Custom type pemProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PemProductID_Type.__name__ = "OctetString"
_PemProductID_Object = MibTableColumn
pemProductID = _PemProductID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 13),
    _PemProductID_Type()
)
pemProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemProductID.setStatus("current")
_PemFPGAVersion_Type = Unsigned32
_PemFPGAVersion_Object = MibTableColumn
pemFPGAVersion = _PemFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 5, 1, 14),
    _PemFPGAVersion_Type()
)
pemFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemFPGAVersion.setStatus("current")
_Hw_numSlots_Type = Unsigned32
_Hw_numSlots_Object = MibScalar
hw_numSlots = _Hw_numSlots_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 6),
    _Hw_numSlots_Type()
)
hw_numSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_numSlots.setStatus("current")
_Hw_numFans_Type = Unsigned32
_Hw_numFans_Object = MibScalar
hw_numFans = _Hw_numFans_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 7),
    _Hw_numFans_Type()
)
hw_numFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_numFans.setStatus("current")
_Hw_numPowerSupplies_Type = Unsigned32
_Hw_numPowerSupplies_Object = MibScalar
hw_numPowerSupplies = _Hw_numPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 8),
    _Hw_numPowerSupplies_Type()
)
hw_numPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_numPowerSupplies.setStatus("current")
_Hw_numPEMs_Type = Unsigned32
_Hw_numPEMs_Object = MibScalar
hw_numPEMs = _Hw_numPEMs_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 9),
    _Hw_numPEMs_Type()
)
hw_numPEMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_numPEMs.setStatus("current")


class _Hw_certificateNumber_Type(OctetString):
    """Custom type hw_certificateNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Hw_certificateNumber_Type.__name__ = "OctetString"
_Hw_certificateNumber_Object = MibScalar
hw_certificateNumber = _Hw_certificateNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 10),
    _Hw_certificateNumber_Type()
)
hw_certificateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_certificateNumber.setStatus("current")


class _Hw_serialNumber_Type(OctetString):
    """Custom type hw_serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Hw_serialNumber_Type.__name__ = "OctetString"
_Hw_serialNumber_Object = MibScalar
hw_serialNumber = _Hw_serialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 3, 11),
    _Hw_serialNumber_Type()
)
hw_serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw_serialNumber.setStatus("current")


class _TptHardwareNotifyDeviceID_Type(OctetString):
    """Custom type tptHardwareNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptHardwareNotifyDeviceID_Type.__name__ = "OctetString"
_TptHardwareNotifyDeviceID_Object = MibScalar
tptHardwareNotifyDeviceID = _TptHardwareNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 1),
    _TptHardwareNotifyDeviceID_Type()
)
tptHardwareNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyDeviceID.setStatus("current")
_TptHardwareNotifySlot_Type = ExtendedSlot
_TptHardwareNotifySlot_Object = MibScalar
tptHardwareNotifySlot = _TptHardwareNotifySlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 2),
    _TptHardwareNotifySlot_Type()
)
tptHardwareNotifySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifySlot.setStatus("current")
_TptHardwareNotifyPort_Type = Unsigned32
_TptHardwareNotifyPort_Object = MibScalar
tptHardwareNotifyPort = _TptHardwareNotifyPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 3),
    _TptHardwareNotifyPort_Type()
)
tptHardwareNotifyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyPort.setStatus("current")
_TptHardwareNotifyMeType_Type = ManagedElementType
_TptHardwareNotifyMeType_Object = MibScalar
tptHardwareNotifyMeType = _TptHardwareNotifyMeType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 4),
    _TptHardwareNotifyMeType_Type()
)
tptHardwareNotifyMeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyMeType.setStatus("current")
_TptHardwareNotifyCfgType_Type = ConfigRedundancy
_TptHardwareNotifyCfgType_Object = MibScalar
tptHardwareNotifyCfgType = _TptHardwareNotifyCfgType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 5),
    _TptHardwareNotifyCfgType_Type()
)
tptHardwareNotifyCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyCfgType.setStatus("current")
_TptHardwareNotifyHlState_Type = HardwareState
_TptHardwareNotifyHlState_Object = MibScalar
tptHardwareNotifyHlState = _TptHardwareNotifyHlState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 6),
    _TptHardwareNotifyHlState_Type()
)
tptHardwareNotifyHlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyHlState.setStatus("current")
_TptHardwareNotifyHlStateQual_Type = HardwareStateQual
_TptHardwareNotifyHlStateQual_Object = MibScalar
tptHardwareNotifyHlStateQual = _TptHardwareNotifyHlStateQual_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 7),
    _TptHardwareNotifyHlStateQual_Type()
)
tptHardwareNotifyHlStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptHardwareNotifyHlStateQual.setStatus("current")

# Managed Objects groups


# Notification objects

tptHardwareNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 7)
)
tptHardwareNotify.setObjects(
      *(("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyDeviceID"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifySlot"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyPort"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyMeType"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyCfgType"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyHlState"),
        ("TPT-TPA-HARDWARE-MIB", "tptHardwareNotifyHlStateQual"))
)
if mibBuilder.loadTexts:
    tptHardwareNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TPA-HARDWARE-MIB",
    **{"ManagedElementType": ManagedElementType,
       "ConfigRedundancy": ConfigRedundancy,
       "HardwareState": HardwareState,
       "HardwareStateQual": HardwareStateQual,
       "ExtendedSlot": ExtendedSlot,
       "LineType": LineType,
       "DuplexState": DuplexState,
       "SfpQualifier": SfpQualifier,
       "tpt-tpa-hardware-objs": tpt_tpa_hardware_objs,
       "hw-slotTable": hw_slotTable,
       "hw-slotEntry": hw_slotEntry,
       "slotNumber": slotNumber,
       "slotPort": slotPort,
       "slotType": slotType,
       "slotCfgType": slotCfgType,
       "slotRunState": slotRunState,
       "slotQualifier1": slotQualifier1,
       "slotQualifier2": slotQualifier2,
       "slotQualifier3": slotQualifier3,
       "slotQualifier4": slotQualifier4,
       "slotStartTime": slotStartTime,
       "slotVendorID": slotVendorID,
       "slotDeviceID": slotDeviceID,
       "slotProductID": slotProductID,
       "slotFPGAVersion": slotFPGAVersion,
       "slotInterface": slotInterface,
       "slotLineType": slotLineType,
       "slotDuplexState": slotDuplexState,
       "slotPhysical": slotPhysical,
       "slotSfpQualifier1": slotSfpQualifier1,
       "slotSfpQualifier2": slotSfpQualifier2,
       "hw-chasTable": hw_chasTable,
       "hw-chasEntry": hw_chasEntry,
       "chasNumber": chasNumber,
       "chasType": chasType,
       "chasCfgType": chasCfgType,
       "chasRunState": chasRunState,
       "chasQualifier1": chasQualifier1,
       "chasQualifier2": chasQualifier2,
       "chasQualifier3": chasQualifier3,
       "chasQualifier4": chasQualifier4,
       "chasStartTime": chasStartTime,
       "chasVendorID": chasVendorID,
       "chasDeviceID": chasDeviceID,
       "chasProductID": chasProductID,
       "chasFPGAVersion": chasFPGAVersion,
       "hw-fanTable": hw_fanTable,
       "hw-fanEntry": hw_fanEntry,
       "fanSubunit": fanSubunit,
       "fanType": fanType,
       "fanCfgType": fanCfgType,
       "fanRunState": fanRunState,
       "fanQualifier1": fanQualifier1,
       "fanQualifier2": fanQualifier2,
       "fanQualifier3": fanQualifier3,
       "fanQualifier4": fanQualifier4,
       "fanStartTime": fanStartTime,
       "fanVendorID": fanVendorID,
       "fanDeviceID": fanDeviceID,
       "fanProductID": fanProductID,
       "fanFPGAVersion": fanFPGAVersion,
       "hw-psTable": hw_psTable,
       "hw-psEntry": hw_psEntry,
       "psSubunit": psSubunit,
       "psType": psType,
       "psCfgType": psCfgType,
       "psRunState": psRunState,
       "psQualifier1": psQualifier1,
       "psQualifier2": psQualifier2,
       "psQualifier3": psQualifier3,
       "psQualifier4": psQualifier4,
       "psStartTime": psStartTime,
       "psVendorID": psVendorID,
       "psDeviceID": psDeviceID,
       "psProductID": psProductID,
       "psFPGAVersion": psFPGAVersion,
       "hw-pemTable": hw_pemTable,
       "hw-pemEntry": hw_pemEntry,
       "pemSubunit": pemSubunit,
       "pemType": pemType,
       "pemCfgType": pemCfgType,
       "pemRunState": pemRunState,
       "pemQualifier1": pemQualifier1,
       "pemQualifier2": pemQualifier2,
       "pemQualifier3": pemQualifier3,
       "pemQualifier4": pemQualifier4,
       "pemStartTime": pemStartTime,
       "pemVendorID": pemVendorID,
       "pemDeviceID": pemDeviceID,
       "pemProductID": pemProductID,
       "pemFPGAVersion": pemFPGAVersion,
       "hw-numSlots": hw_numSlots,
       "hw-numFans": hw_numFans,
       "hw-numPowerSupplies": hw_numPowerSupplies,
       "hw-numPEMs": hw_numPEMs,
       "hw-certificateNumber": hw_certificateNumber,
       "hw-serialNumber": hw_serialNumber,
       "tptHardwareNotify": tptHardwareNotify,
       "tptHardwareNotifyDeviceID": tptHardwareNotifyDeviceID,
       "tptHardwareNotifySlot": tptHardwareNotifySlot,
       "tptHardwareNotifyPort": tptHardwareNotifyPort,
       "tptHardwareNotifyMeType": tptHardwareNotifyMeType,
       "tptHardwareNotifyCfgType": tptHardwareNotifyCfgType,
       "tptHardwareNotifyHlState": tptHardwareNotifyHlState,
       "tptHardwareNotifyHlStateQual": tptHardwareNotifyHlStateQual}
)
