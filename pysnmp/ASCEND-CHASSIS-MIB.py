# SNMP MIB module (ASCEND-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:55 2024
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

(slots,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "slots")

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


# MODULE-IDENTITY


# Types definitions



class AscendSlotType(Integer32):
    """Custom type AscendSlotType based on Integer32"""
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
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              91,
              92,
              93,
              94,
              96,
              97)
        )
    )
    namedValues = NamedValues(
        *(("aim2", 12),
          ("aim6", 13),
          ("alcatel-dadsl-atm", 64),
          ("alcatel-dadsl-atm-v2", 84),
          ("analogModem", 25),
          ("analogModem2", 45),
          ("annexb-dadsl-atm", 96),
          ("apx-control-module", 97),
          ("bri", 7),
          ("cap-adsl", 41),
          ("csm3v", 65),
          ("csmx", 49),
          ("dadsl-atm-16ports", 83),
          ("dadsl-atm-16ports-v2", 86),
          ("dadsl-atm-24ports", 87),
          ("dig-12modem", 34),
          ("dig-16modem", 35),
          ("dig-48modem", 36),
          ("dig-8modem", 33),
          ("dmt-adsl", 42),
          ("ds3-atm", 52),
          ("ds3-atm2", 79),
          ("dualHost", 10),
          ("e3-atm", 92),
          ("empty", 2),
          ("ether-dual", 72),
          ("ethernet", 14),
          ("ethernet10-100", 51),
          ("ethernet2", 53),
          ("ethernet3", 61),
          ("ethernet4", 74),
          ("ethernetData", 15),
          ("ethernetData2", 54),
          ("ethernetData2ec", 69),
          ("glite-atm-48ports", 91),
          ("hdsl2", 94),
          ("hssi", 30),
          ("idsl", 43),
          ("lanModem", 18),
          ("lanModem-csmx", 77),
          ("lanModemP", 22),
          ("lanModemP12", 23),
          ("lanModemP48", 26),
          ("madd", 56),
          ("madd2", 93),
          ("maxpotsFxs", 78),
          ("oc3-atm", 60),
          ("occupied", 80),
          ("other", 1),
          ("phs-12v32modem", 38),
          ("phs-16v32modem", 39),
          ("phs-8v32modem", 37),
          ("pots", 24),
          ("primaryNailed56", 32),
          ("primaryNailedT1", 31),
          ("quadHost", 11),
          ("router", 27),
          ("s56-2", 8),
          ("s56-4", 9),
          ("sdsl", 40),
          ("sdsl-atm", 63),
          ("sdsl-atm-v2", 85),
          ("sdsl-data", 55),
          ("sdsl-voice", 57),
          ("serialWan", 19),
          ("slotBriLT", 21),
          ("slotBriNT", 17),
          ("slotBriTE", 16),
          ("slotBriTeU", 58),
          ("slotDs3Daughter", 70),
          ("slotE1", 6),
          ("slotOc3Daughter", 59),
          ("slotT1", 4),
          ("srs-ether", 62),
          ("st100-cc3-atm", 76),
          ("st100-ds3-atm", 66),
          ("st100-oc3-atm", 73),
          ("st100-sdsl16", 68),
          ("st100-sdsl8", 71),
          ("st100-uds3", 67),
          ("stinger-control-module", 81),
          ("stm0", 75),
          ("sysE1", 5),
          ("sysT1", 3),
          ("t3", 29),
          ("tnt-control-module", 82),
          ("uds3", 50),
          ("unchanE1", 44),
          ("unchanT1", 28),
          ("v110", 20),
          ("voip-12dsp", 47),
          ("voip-16dsp", 48),
          ("voip-8dsp", 46))
    )





class CntrReduAvailState(Integer32):
    """Custom type CntrReduAvailState based on Integer32"""
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
        *(("boot", 2),
          ("fullRedundancy", 3),
          ("noRedundancy", 5),
          ("other", 1),
          ("partialRedundancy", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlotNumber_Type = Integer32
_SlotNumber_Object = MibScalar
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 1),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNumber.setStatus("mandatory")
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("mandatory")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1)
)
slotEntry.setIndexNames(
    (0, "ASCEND-CHASSIS-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("mandatory")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("mandatory")
_SlotName_Type = DisplayString
_SlotName_Object = MibTableColumn
slotName = _SlotName_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 2),
    _SlotName_Type()
)
slotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotName.setStatus("mandatory")
_SlotType_Type = AscendSlotType
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 3),
    _SlotType_Type()
)
slotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotType.setStatus("mandatory")


class _SlotFixed_Type(Integer32):
    """Custom type slotFixed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("removable", 2))
    )


_SlotFixed_Type.__name__ = "Integer32"
_SlotFixed_Object = MibTableColumn
slotFixed = _SlotFixed_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 4),
    _SlotFixed_Type()
)
slotFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFixed.setStatus("mandatory")
_SlotItems_Type = Integer32
_SlotItems_Object = MibTableColumn
slotItems = _SlotItems_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 5),
    _SlotItems_Type()
)
slotItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItems.setStatus("mandatory")
_SlotSpecific_Type = ObjectIdentifier
_SlotSpecific_Object = MibTableColumn
slotSpecific = _SlotSpecific_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 6),
    _SlotSpecific_Type()
)
slotSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSpecific.setStatus("mandatory")
_SlotSerialNumber_Type = Integer32
_SlotSerialNumber_Object = MibTableColumn
slotSerialNumber = _SlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 7),
    _SlotSerialNumber_Type()
)
slotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSerialNumber.setStatus("mandatory")


class _SlotStatus_Type(Integer32):
    """Custom type slotStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("operStateCoreDump", 4),
          ("operStateDiag", 3),
          ("operStateDown", 1),
          ("operStateLoading", 5),
          ("operStateNone", 7),
          ("operStateOccupied", 8),
          ("operStatePost", 6),
          ("operStateUp", 2))
    )


_SlotStatus_Type.__name__ = "Integer32"
_SlotStatus_Object = MibTableColumn
slotStatus = _SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 8),
    _SlotStatus_Type()
)
slotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatus.setStatus("mandatory")
_SlotLastChange_Type = TimeTicks
_SlotLastChange_Object = MibTableColumn
slotLastChange = _SlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 9),
    _SlotLastChange_Type()
)
slotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLastChange.setStatus("mandatory")
_SlotHWRev_Type = DisplayString
_SlotHWRev_Object = MibTableColumn
slotHWRev = _SlotHWRev_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 10),
    _SlotHWRev_Type()
)
slotHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotHWRev.setStatus("mandatory")
_SlotSWRev_Type = DisplayString
_SlotSWRev_Object = MibTableColumn
slotSWRev = _SlotSWRev_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 11),
    _SlotSWRev_Type()
)
slotSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSWRev.setStatus("mandatory")


class _SlotAdminStatus_Type(Integer32):
    """Custom type slotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("remove", 3),
          ("up", 1))
    )


_SlotAdminStatus_Type.__name__ = "Integer32"
_SlotAdminStatus_Object = MibTableColumn
slotAdminStatus = _SlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 12),
    _SlotAdminStatus_Type()
)
slotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotAdminStatus.setStatus("mandatory")
_SlotUpTime_Type = TimeTicks
_SlotUpTime_Object = MibTableColumn
slotUpTime = _SlotUpTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 13),
    _SlotUpTime_Type()
)
slotUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotUpTime.setStatus("mandatory")
_SlotMemoryTotal_Type = Integer32
_SlotMemoryTotal_Object = MibTableColumn
slotMemoryTotal = _SlotMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 14),
    _SlotMemoryTotal_Type()
)
slotMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMemoryTotal.setStatus("mandatory")
_SlotMemoryAvail_Type = Integer32
_SlotMemoryAvail_Object = MibTableColumn
slotMemoryAvail = _SlotMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 15),
    _SlotMemoryAvail_Type()
)
slotMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMemoryAvail.setStatus("mandatory")
_SlotMemoryThreshold_Type = Integer32
_SlotMemoryThreshold_Object = MibTableColumn
slotMemoryThreshold = _SlotMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 16),
    _SlotMemoryThreshold_Type()
)
slotMemoryThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMemoryThreshold.setStatus("mandatory")
_SlotItemTable_Object = MibTable
slotItemTable = _SlotItemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3)
)
if mibBuilder.loadTexts:
    slotItemTable.setStatus("mandatory")
_SlotItemEntry_Object = MibTableRow
slotItemEntry = _SlotItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1)
)
slotItemEntry.setIndexNames(
    (0, "ASCEND-CHASSIS-MIB", "slotItemSlotIndex"),
    (0, "ASCEND-CHASSIS-MIB", "slotItemIndex"),
)
if mibBuilder.loadTexts:
    slotItemEntry.setStatus("mandatory")
_SlotItemSlotIndex_Type = Integer32
_SlotItemSlotIndex_Object = MibTableColumn
slotItemSlotIndex = _SlotItemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 1),
    _SlotItemSlotIndex_Type()
)
slotItemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemSlotIndex.setStatus("mandatory")
_SlotItemIndex_Type = Integer32
_SlotItemIndex_Object = MibTableColumn
slotItemIndex = _SlotItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 2),
    _SlotItemIndex_Type()
)
slotItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemIndex.setStatus("mandatory")
_SlotItemFirstIf_Type = Integer32
_SlotItemFirstIf_Object = MibTableColumn
slotItemFirstIf = _SlotItemFirstIf_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 3),
    _SlotItemFirstIf_Type()
)
slotItemFirstIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemFirstIf.setStatus("mandatory")
_SlotItemIfCount_Type = Integer32
_SlotItemIfCount_Object = MibTableColumn
slotItemIfCount = _SlotItemIfCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 4),
    _SlotItemIfCount_Type()
)
slotItemIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemIfCount.setStatus("mandatory")
_SlotItemSpecific_Type = ObjectIdentifier
_SlotItemSpecific_Object = MibTableColumn
slotItemSpecific = _SlotItemSpecific_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 5),
    _SlotItemSpecific_Type()
)
slotItemSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemSpecific.setStatus("mandatory")


class _SlotItemStatus_Type(Integer32):
    """Custom type slotItemStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("briDown", 5),
          ("briLinkDisabled", 4),
          ("briLinkNotStuffed", 3),
          ("briMInit", 9),
          ("briNotInit", 6),
          ("briNotInitWithL2", 7),
          ("briPInit", 8),
          ("slotItemNotRunning", 2),
          ("statusOther", 1))
    )


_SlotItemStatus_Type.__name__ = "Integer32"
_SlotItemStatus_Object = MibTableColumn
slotItemStatus = _SlotItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 6),
    _SlotItemStatus_Type()
)
slotItemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotItemStatus.setStatus("mandatory")
_SlotIfTable_Object = MibTable
slotIfTable = _SlotIfTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 4)
)
if mibBuilder.loadTexts:
    slotIfTable.setStatus("mandatory")
_SlotIfEntry_Object = MibTableRow
slotIfEntry = _SlotIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 4, 1)
)
slotIfEntry.setIndexNames(
    (0, "ASCEND-CHASSIS-MIB", "slotIfIndex"),
)
if mibBuilder.loadTexts:
    slotIfEntry.setStatus("mandatory")
_SlotIfIndex_Type = Integer32
_SlotIfIndex_Object = MibTableColumn
slotIfIndex = _SlotIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 1),
    _SlotIfIndex_Type()
)
slotIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfIndex.setStatus("mandatory")
_SlotIfSlotIndex_Type = Integer32
_SlotIfSlotIndex_Object = MibTableColumn
slotIfSlotIndex = _SlotIfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 2),
    _SlotIfSlotIndex_Type()
)
slotIfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfSlotIndex.setStatus("mandatory")
_SlotIfItemIndex_Type = Integer32
_SlotIfItemIndex_Object = MibTableColumn
slotIfItemIndex = _SlotIfItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 3),
    _SlotIfItemIndex_Type()
)
slotIfItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfItemIndex.setStatus("mandatory")
_ChassisInfo_ObjectIdentity = ObjectIdentity
chassisInfo = _ChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 2, 6)
)
_ChassisDesc_Type = DisplayString
_ChassisDesc_Object = MibScalar
chassisDesc = _ChassisDesc_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 1),
    _ChassisDesc_Type()
)
chassisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisDesc.setStatus("mandatory")
_ChassisSerialNo_Type = Integer32
_ChassisSerialNo_Object = MibScalar
chassisSerialNo = _ChassisSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 2),
    _ChassisSerialNo_Type()
)
chassisSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNo.setStatus("mandatory")
_ChassisHWRev_Type = DisplayString
_ChassisHWRev_Object = MibScalar
chassisHWRev = _ChassisHWRev_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 3),
    _ChassisHWRev_Type()
)
chassisHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHWRev.setStatus("mandatory")


class _ChassisRedundancy_Type(Integer32):
    """Custom type chassisRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedundancy", 1),
          ("redundancy", 2))
    )


_ChassisRedundancy_Type.__name__ = "Integer32"
_ChassisRedundancy_Object = MibScalar
chassisRedundancy = _ChassisRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 4),
    _ChassisRedundancy_Type()
)
chassisRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisRedundancy.setStatus("mandatory")
_ChassisMemTotal_Type = Integer32
_ChassisMemTotal_Object = MibScalar
chassisMemTotal = _ChassisMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 5),
    _ChassisMemTotal_Type()
)
chassisMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMemTotal.setStatus("mandatory")
_ChassisMemAvail_Type = Integer32
_ChassisMemAvail_Object = MibScalar
chassisMemAvail = _ChassisMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 6),
    _ChassisMemAvail_Type()
)
chassisMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMemAvail.setStatus("mandatory")
_ChassisMemThreshold_Type = Integer32
_ChassisMemThreshold_Object = MibScalar
chassisMemThreshold = _ChassisMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 7),
    _ChassisMemThreshold_Type()
)
chassisMemThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMemThreshold.setStatus("mandatory")
_CntrReduGroup_ObjectIdentity = ObjectIdentity
cntrReduGroup = _CntrReduGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 8)
)
_CntrReduSwitchLastTime_Type = TimeTicks
_CntrReduSwitchLastTime_Object = MibScalar
cntrReduSwitchLastTime = _CntrReduSwitchLastTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 1),
    _CntrReduSwitchLastTime_Type()
)
cntrReduSwitchLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduSwitchLastTime.setStatus("mandatory")


class _CntrReduSwitchReason_Type(Integer32):
    """Custom type cntrReduSwitchReason based on Integer32"""
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
        *(("failure", 2),
          ("manual", 3),
          ("scheduled", 4),
          ("unknown", 1))
    )


_CntrReduSwitchReason_Type.__name__ = "Integer32"
_CntrReduSwitchReason_Object = MibScalar
cntrReduSwitchReason = _CntrReduSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 2),
    _CntrReduSwitchReason_Type()
)
cntrReduSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduSwitchReason.setStatus("mandatory")
_CntrReduSwitchIndex_Type = Integer32
_CntrReduSwitchIndex_Object = MibScalar
cntrReduSwitchIndex = _CntrReduSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 3),
    _CntrReduSwitchIndex_Type()
)
cntrReduSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduSwitchIndex.setStatus("mandatory")
_CntrReduCurrentIndex_Type = Integer32
_CntrReduCurrentIndex_Object = MibScalar
cntrReduCurrentIndex = _CntrReduCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 4),
    _CntrReduCurrentIndex_Type()
)
cntrReduCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduCurrentIndex.setStatus("mandatory")
_CntrReduAvailGroup_ObjectIdentity = ObjectIdentity
cntrReduAvailGroup = _CntrReduAvailGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 9)
)
_CntrReduAvailLastTime_Type = TimeTicks
_CntrReduAvailLastTime_Object = MibScalar
cntrReduAvailLastTime = _CntrReduAvailLastTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 1),
    _CntrReduAvailLastTime_Type()
)
cntrReduAvailLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduAvailLastTime.setStatus("mandatory")
_CntrReduAvailPrevState_Type = CntrReduAvailState
_CntrReduAvailPrevState_Object = MibScalar
cntrReduAvailPrevState = _CntrReduAvailPrevState_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 2),
    _CntrReduAvailPrevState_Type()
)
cntrReduAvailPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduAvailPrevState.setStatus("mandatory")
_CntrReduAvailCurrState_Type = CntrReduAvailState
_CntrReduAvailCurrState_Object = MibScalar
cntrReduAvailCurrState = _CntrReduAvailCurrState_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 3),
    _CntrReduAvailCurrState_Type()
)
cntrReduAvailCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduAvailCurrState.setStatus("mandatory")
_CntrReduAvailSlotIndex_Type = Integer32
_CntrReduAvailSlotIndex_Object = MibScalar
cntrReduAvailSlotIndex = _CntrReduAvailSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 4),
    _CntrReduAvailSlotIndex_Type()
)
cntrReduAvailSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntrReduAvailSlotIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-CHASSIS-MIB",
    **{"AscendSlotType": AscendSlotType,
       "CntrReduAvailState": CntrReduAvailState,
       "slotNumber": slotNumber,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotIndex": slotIndex,
       "slotName": slotName,
       "slotType": slotType,
       "slotFixed": slotFixed,
       "slotItems": slotItems,
       "slotSpecific": slotSpecific,
       "slotSerialNumber": slotSerialNumber,
       "slotStatus": slotStatus,
       "slotLastChange": slotLastChange,
       "slotHWRev": slotHWRev,
       "slotSWRev": slotSWRev,
       "slotAdminStatus": slotAdminStatus,
       "slotUpTime": slotUpTime,
       "slotMemoryTotal": slotMemoryTotal,
       "slotMemoryAvail": slotMemoryAvail,
       "slotMemoryThreshold": slotMemoryThreshold,
       "slotItemTable": slotItemTable,
       "slotItemEntry": slotItemEntry,
       "slotItemSlotIndex": slotItemSlotIndex,
       "slotItemIndex": slotItemIndex,
       "slotItemFirstIf": slotItemFirstIf,
       "slotItemIfCount": slotItemIfCount,
       "slotItemSpecific": slotItemSpecific,
       "slotItemStatus": slotItemStatus,
       "slotIfTable": slotIfTable,
       "slotIfEntry": slotIfEntry,
       "slotIfIndex": slotIfIndex,
       "slotIfSlotIndex": slotIfSlotIndex,
       "slotIfItemIndex": slotIfItemIndex,
       "chassisInfo": chassisInfo,
       "chassisDesc": chassisDesc,
       "chassisSerialNo": chassisSerialNo,
       "chassisHWRev": chassisHWRev,
       "chassisRedundancy": chassisRedundancy,
       "chassisMemTotal": chassisMemTotal,
       "chassisMemAvail": chassisMemAvail,
       "chassisMemThreshold": chassisMemThreshold,
       "cntrReduGroup": cntrReduGroup,
       "cntrReduSwitchLastTime": cntrReduSwitchLastTime,
       "cntrReduSwitchReason": cntrReduSwitchReason,
       "cntrReduSwitchIndex": cntrReduSwitchIndex,
       "cntrReduCurrentIndex": cntrReduCurrentIndex,
       "cntrReduAvailGroup": cntrReduAvailGroup,
       "cntrReduAvailLastTime": cntrReduAvailLastTime,
       "cntrReduAvailPrevState": cntrReduAvailPrevState,
       "cntrReduAvailCurrState": cntrReduAvailCurrState,
       "cntrReduAvailSlotIndex": cntrReduAvailSlotIndex}
)
