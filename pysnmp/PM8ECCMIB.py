# SNMP MIB module (PM8ECCMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PM8ECCMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:02 2024
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
 NotificationType,
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
    "NotificationType",
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



class AlarmType(Integer32):
    """Custom type AlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              20,
              21,
              51,
              52,
              53,
              54,
              55,
              60,
              61,
              70,
              80,
              90,
              100,
              101,
              102,
              103,
              104,
              105,
              1280)
        )
    )
    namedValues = NamedValues(
        *(("combinatorialAND", 100),
          ("combinatorialNAND", 101),
          ("combinatorialNOR", 103),
          ("combinatorialNOT", 105),
          ("combinatorialOR", 102),
          ("combinatorialXOR", 104),
          ("diagnostic", 1280),
          ("digitalInputOFFtoON", 60),
          ("digitalInputONtoOFF", 61),
          ("overPower", 11),
          ("overReversePower", 12),
          ("overValue", 10),
          ("phaseLossCurrent", 53),
          ("phaseLossVoltage", 52),
          ("phaseRotationReversal", 51),
          ("powerFactorLagging", 55),
          ("powerFactorLeading", 54),
          ("unaryEvent", 70),
          ("underPower", 21),
          ("underValue", 20),
          ("voltageOrCurrentSag", 90),
          ("voltageOrCurrentSwell", 80))
    )





class IOPointType(Integer32):
    """Custom type IOPointType based on Integer32"""
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
        *(("analogInput", 3),
          ("analogOutput", 4),
          ("digitalInput", 1),
          ("digitalOutput", 2))
    )





class IOPointLabel(OctetString):
    """Custom type IOPointLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class AlarmLabel(OctetString):
    """Custom type AlarmLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SchneiderElectric_ObjectIdentity = ObjectIdentity
schneiderElectric = _SchneiderElectric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833)
)
_TransparentFactoryEthernet_ObjectIdentity = ObjectIdentity
transparentFactoryEthernet = _TransparentFactoryEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1)
)
_EquipmentProfile_ObjectIdentity = ObjectIdentity
equipmentProfile = _EquipmentProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7)
)
_TfProducts_ObjectIdentity = ObjectIdentity
tfProducts = _TfProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255)
)
_Ecc_ObjectIdentity = ObjectIdentity
ecc = _Ecc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15)
)
_Pm8ecc_ObjectIdentity = ObjectIdentity
pm8ecc = _Pm8ecc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1)
)
_Metering_ObjectIdentity = ObjectIdentity
metering = _Metering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1)
)
_SystemWiringTypeTable_Object = MibTable
systemWiringTypeTable = _SystemWiringTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    systemWiringTypeTable.setStatus("mandatory")
_SystemWiringTypeEntry_Object = MibTableRow
systemWiringTypeEntry = _SystemWiringTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 1, 1)
)
systemWiringTypeEntry.setIndexNames(
    (0, "PM8ECCMIB", "swtIndex"),
)
if mibBuilder.loadTexts:
    systemWiringTypeEntry.setStatus("mandatory")


class _SwtIndex_Type(Integer32):
    """Custom type swtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwtIndex_Type.__name__ = "Integer32"
_SwtIndex_Object = MibTableColumn
swtIndex = _SwtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 1, 1, 1),
    _SwtIndex_Type()
)
swtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swtIndex.setStatus("mandatory")


class _SwtWiringType_Type(Integer32):
    """Custom type swtWiringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(31, 31),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
    )


_SwtWiringType_Type.__name__ = "Integer32"
_SwtWiringType_Object = MibTableColumn
swtWiringType = _SwtWiringType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 1, 1, 2),
    _SwtWiringType_Type()
)
swtWiringType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swtWiringType.setStatus("mandatory")
_LoadCurrentTable_Object = MibTable
loadCurrentTable = _LoadCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    loadCurrentTable.setStatus("mandatory")
_LoadCurrentEntry_Object = MibTableRow
loadCurrentEntry = _LoadCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1)
)
loadCurrentEntry.setIndexNames(
    (0, "PM8ECCMIB", "lcIndex"),
)
if mibBuilder.loadTexts:
    loadCurrentEntry.setStatus("mandatory")


class _LcIndex_Type(Integer32):
    """Custom type lcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LcIndex_Type.__name__ = "Integer32"
_LcIndex_Object = MibTableColumn
lcIndex = _LcIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1, 1),
    _LcIndex_Type()
)
lcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIndex.setStatus("mandatory")
_LcIa_Type = OctetString
_LcIa_Object = MibTableColumn
lcIa = _LcIa_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1, 2),
    _LcIa_Type()
)
lcIa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIa.setStatus("mandatory")
_LcIb_Type = OctetString
_LcIb_Object = MibTableColumn
lcIb = _LcIb_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1, 3),
    _LcIb_Type()
)
lcIb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIb.setStatus("mandatory")
_LcIc_Type = OctetString
_LcIc_Object = MibTableColumn
lcIc = _LcIc_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1, 4),
    _LcIc_Type()
)
lcIc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIc.setStatus("mandatory")
_LcIAvg_Type = OctetString
_LcIAvg_Object = MibTableColumn
lcIAvg = _LcIAvg_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 2, 1, 5),
    _LcIAvg_Type()
)
lcIAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIAvg.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3, 1)
)
powerEntry.setIndexNames(
    (0, "PM8ECCMIB", "pIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")


class _PIndex_Type(Integer32):
    """Custom type pIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PIndex_Type.__name__ = "Integer32"
_PIndex_Object = MibTableColumn
pIndex = _PIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3, 1, 1),
    _PIndex_Type()
)
pIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIndex.setStatus("mandatory")
_PReal_Type = OctetString
_PReal_Object = MibTableColumn
pReal = _PReal_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3, 1, 2),
    _PReal_Type()
)
pReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pReal.setStatus("mandatory")
_PReactive_Type = OctetString
_PReactive_Object = MibTableColumn
pReactive = _PReactive_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3, 1, 3),
    _PReactive_Type()
)
pReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pReactive.setStatus("mandatory")
_PApparent_Type = OctetString
_PApparent_Object = MibTableColumn
pApparent = _PApparent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 3, 1, 4),
    _PApparent_Type()
)
pApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pApparent.setStatus("mandatory")
_PowerFactorTable_Object = MibTable
powerFactorTable = _PowerFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    powerFactorTable.setStatus("mandatory")
_PowerFactorEntry_Object = MibTableRow
powerFactorEntry = _PowerFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 4, 1)
)
powerFactorEntry.setIndexNames(
    (0, "PM8ECCMIB", "pfIndex"),
)
if mibBuilder.loadTexts:
    powerFactorEntry.setStatus("mandatory")


class _PfIndex_Type(Integer32):
    """Custom type pfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PfIndex_Type.__name__ = "Integer32"
_PfIndex_Object = MibTableColumn
pfIndex = _PfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 4, 1, 1),
    _PfIndex_Type()
)
pfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIndex.setStatus("mandatory")
_PfPowerFactorTotal_Type = OctetString
_PfPowerFactorTotal_Object = MibTableColumn
pfPowerFactorTotal = _PfPowerFactorTotal_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 4, 1, 2),
    _PfPowerFactorTotal_Type()
)
pfPowerFactorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfPowerFactorTotal.setStatus("mandatory")
_PfPowerFactorDescription_Type = OctetString
_PfPowerFactorDescription_Object = MibTableColumn
pfPowerFactorDescription = _PfPowerFactorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 4, 1, 3),
    _PfPowerFactorDescription_Type()
)
pfPowerFactorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfPowerFactorDescription.setStatus("mandatory")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("mandatory")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1)
)
voltageEntry.setIndexNames(
    (0, "PM8ECCMIB", "vIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("mandatory")


class _VIndex_Type(Integer32):
    """Custom type vIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VIndex_Type.__name__ = "Integer32"
_VIndex_Object = MibTableColumn
vIndex = _VIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 1),
    _VIndex_Type()
)
vIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vIndex.setStatus("mandatory")
_VVab_Type = OctetString
_VVab_Object = MibTableColumn
vVab = _VVab_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 2),
    _VVab_Type()
)
vVab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVab.setStatus("mandatory")
_VVbc_Type = OctetString
_VVbc_Object = MibTableColumn
vVbc = _VVbc_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 3),
    _VVbc_Type()
)
vVbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVbc.setStatus("mandatory")
_VVca_Type = OctetString
_VVca_Object = MibTableColumn
vVca = _VVca_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 4),
    _VVca_Type()
)
vVca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVca.setStatus("mandatory")
_VVllAvg_Type = OctetString
_VVllAvg_Object = MibTableColumn
vVllAvg = _VVllAvg_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 5),
    _VVllAvg_Type()
)
vVllAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVllAvg.setStatus("mandatory")
_VVan_Type = OctetString
_VVan_Object = MibTableColumn
vVan = _VVan_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 6),
    _VVan_Type()
)
vVan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVan.setStatus("mandatory")
_VVbn_Type = OctetString
_VVbn_Object = MibTableColumn
vVbn = _VVbn_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 7),
    _VVbn_Type()
)
vVbn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVbn.setStatus("mandatory")
_VVcn_Type = OctetString
_VVcn_Object = MibTableColumn
vVcn = _VVcn_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 8),
    _VVcn_Type()
)
vVcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVcn.setStatus("mandatory")
_VVlnAvg_Type = OctetString
_VVlnAvg_Object = MibTableColumn
vVlnAvg = _VVlnAvg_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 5, 1, 9),
    _VVlnAvg_Type()
)
vVlnAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVlnAvg.setStatus("mandatory")
_FrequencyTable_Object = MibTable
frequencyTable = _FrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 6)
)
if mibBuilder.loadTexts:
    frequencyTable.setStatus("mandatory")
_FrequencyEntry_Object = MibTableRow
frequencyEntry = _FrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 6, 1)
)
frequencyEntry.setIndexNames(
    (0, "PM8ECCMIB", "fIndex"),
)
if mibBuilder.loadTexts:
    frequencyEntry.setStatus("mandatory")


class _FIndex_Type(Integer32):
    """Custom type fIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FIndex_Type.__name__ = "Integer32"
_FIndex_Object = MibTableColumn
fIndex = _FIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 6, 1, 1),
    _FIndex_Type()
)
fIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fIndex.setStatus("mandatory")
_FFrequency_Type = OctetString
_FFrequency_Object = MibTableColumn
fFrequency = _FFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 6, 1, 2),
    _FFrequency_Type()
)
fFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fFrequency.setStatus("mandatory")
_CurrentDemandTable_Object = MibTable
currentDemandTable = _CurrentDemandTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7)
)
if mibBuilder.loadTexts:
    currentDemandTable.setStatus("mandatory")
_CurrentDemandEntry_Object = MibTableRow
currentDemandEntry = _CurrentDemandEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1)
)
currentDemandEntry.setIndexNames(
    (0, "PM8ECCMIB", "cdPhase"),
    (0, "PM8ECCMIB", "cdIndex"),
)
if mibBuilder.loadTexts:
    currentDemandEntry.setStatus("mandatory")


class _CdIndex_Type(Integer32):
    """Custom type cdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CdIndex_Type.__name__ = "Integer32"
_CdIndex_Object = MibTableColumn
cdIndex = _CdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 1),
    _CdIndex_Type()
)
cdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdIndex.setStatus("mandatory")


class _CdPhase_Type(OctetString):
    """Custom type cdPhase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CdPhase_Type.__name__ = "OctetString"
_CdPhase_Object = MibTableColumn
cdPhase = _CdPhase_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 2),
    _CdPhase_Type()
)
cdPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdPhase.setStatus("mandatory")
_CdPresentCurrentDemand_Type = OctetString
_CdPresentCurrentDemand_Object = MibTableColumn
cdPresentCurrentDemand = _CdPresentCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 3),
    _CdPresentCurrentDemand_Type()
)
cdPresentCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdPresentCurrentDemand.setStatus("mandatory")
_CdPeakCurrentDemand_Type = OctetString
_CdPeakCurrentDemand_Object = MibTableColumn
cdPeakCurrentDemand = _CdPeakCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 4),
    _CdPeakCurrentDemand_Type()
)
cdPeakCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdPeakCurrentDemand.setStatus("mandatory")
_CdLastCurrentDemand_Type = OctetString
_CdLastCurrentDemand_Object = MibTableColumn
cdLastCurrentDemand = _CdLastCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 5),
    _CdLastCurrentDemand_Type()
)
cdLastCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdLastCurrentDemand.setStatus("mandatory")
_CdPeakDateTime_Type = OctetString
_CdPeakDateTime_Object = MibTableColumn
cdPeakDateTime = _CdPeakDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 6),
    _CdPeakDateTime_Type()
)
cdPeakDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdPeakDateTime.setStatus("mandatory")
_CdResetDateTime_Type = OctetString
_CdResetDateTime_Object = MibTableColumn
cdResetDateTime = _CdResetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 7),
    _CdResetDateTime_Type()
)
cdResetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdResetDateTime.setStatus("mandatory")


class _CdPhaseEnum_Type(Integer32):
    """Custom type cdPhaseEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentPhaseA", 1),
          ("currentPhaseB", 2),
          ("currentPhaseC", 3))
    )


_CdPhaseEnum_Type.__name__ = "Integer32"
_CdPhaseEnum_Object = MibTableColumn
cdPhaseEnum = _CdPhaseEnum_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 7, 1, 8),
    _CdPhaseEnum_Type()
)
cdPhaseEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdPhaseEnum.setStatus("mandatory")
_PowerDemandTable_Object = MibTable
powerDemandTable = _PowerDemandTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8)
)
if mibBuilder.loadTexts:
    powerDemandTable.setStatus("mandatory")
_PowerDemandEntry_Object = MibTableRow
powerDemandEntry = _PowerDemandEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1)
)
powerDemandEntry.setIndexNames(
    (0, "PM8ECCMIB", "pdComponent"),
    (0, "PM8ECCMIB", "pdIndex"),
)
if mibBuilder.loadTexts:
    powerDemandEntry.setStatus("mandatory")


class _PdIndex_Type(Integer32):
    """Custom type pdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PdIndex_Type.__name__ = "Integer32"
_PdIndex_Object = MibTableColumn
pdIndex = _PdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 1),
    _PdIndex_Type()
)
pdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdIndex.setStatus("mandatory")


class _PdComponent_Type(OctetString):
    """Custom type pdComponent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_PdComponent_Type.__name__ = "OctetString"
_PdComponent_Object = MibTableColumn
pdComponent = _PdComponent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 2),
    _PdComponent_Type()
)
pdComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdComponent.setStatus("mandatory")
_PdPresentPowerDemand_Type = OctetString
_PdPresentPowerDemand_Object = MibTableColumn
pdPresentPowerDemand = _PdPresentPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 3),
    _PdPresentPowerDemand_Type()
)
pdPresentPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdPresentPowerDemand.setStatus("mandatory")
_PdPeakPowerDemand_Type = OctetString
_PdPeakPowerDemand_Object = MibTableColumn
pdPeakPowerDemand = _PdPeakPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 4),
    _PdPeakPowerDemand_Type()
)
pdPeakPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdPeakPowerDemand.setStatus("mandatory")
_PdLastPowerDemand_Type = OctetString
_PdLastPowerDemand_Object = MibTableColumn
pdLastPowerDemand = _PdLastPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 5),
    _PdLastPowerDemand_Type()
)
pdLastPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdLastPowerDemand.setStatus("mandatory")
_PdPeakDateTime_Type = OctetString
_PdPeakDateTime_Object = MibTableColumn
pdPeakDateTime = _PdPeakDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 6),
    _PdPeakDateTime_Type()
)
pdPeakDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdPeakDateTime.setStatus("mandatory")
_PdResetDateTime_Type = OctetString
_PdResetDateTime_Object = MibTableColumn
pdResetDateTime = _PdResetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 7),
    _PdResetDateTime_Type()
)
pdResetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdResetDateTime.setStatus("mandatory")


class _PdComponentEnum_Type(Integer32):
    """Custom type pdComponentEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apparentPower", 3),
          ("reactivePower", 2),
          ("realPower", 1))
    )


_PdComponentEnum_Type.__name__ = "Integer32"
_PdComponentEnum_Object = MibTableColumn
pdComponentEnum = _PdComponentEnum_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 8, 1, 8),
    _PdComponentEnum_Type()
)
pdComponentEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdComponentEnum.setStatus("mandatory")
_EnergyTable_Object = MibTable
energyTable = _EnergyTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9)
)
if mibBuilder.loadTexts:
    energyTable.setStatus("mandatory")
_EnergyEntry_Object = MibTableRow
energyEntry = _EnergyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1)
)
energyEntry.setIndexNames(
    (0, "PM8ECCMIB", "eIndex"),
)
if mibBuilder.loadTexts:
    energyEntry.setStatus("mandatory")


class _EIndex_Type(Integer32):
    """Custom type eIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EIndex_Type.__name__ = "Integer32"
_EIndex_Object = MibTableColumn
eIndex = _EIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 1),
    _EIndex_Type()
)
eIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIndex.setStatus("mandatory")
_ERealEnergy_Type = OctetString
_ERealEnergy_Object = MibTableColumn
eRealEnergy = _ERealEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 2),
    _ERealEnergy_Type()
)
eRealEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRealEnergy.setStatus("mandatory")
_EDateTimeRealEnergyReset_Type = OctetString
_EDateTimeRealEnergyReset_Object = MibTableColumn
eDateTimeRealEnergyReset = _EDateTimeRealEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 3),
    _EDateTimeRealEnergyReset_Type()
)
eDateTimeRealEnergyReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDateTimeRealEnergyReset.setStatus("mandatory")
_EReactiveEnergy_Type = OctetString
_EReactiveEnergy_Object = MibTableColumn
eReactiveEnergy = _EReactiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 4),
    _EReactiveEnergy_Type()
)
eReactiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eReactiveEnergy.setStatus("mandatory")
_EDateTimeReactiveEnergyReset_Type = OctetString
_EDateTimeReactiveEnergyReset_Object = MibTableColumn
eDateTimeReactiveEnergyReset = _EDateTimeReactiveEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 5),
    _EDateTimeReactiveEnergyReset_Type()
)
eDateTimeReactiveEnergyReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDateTimeReactiveEnergyReset.setStatus("mandatory")
_EApparentEnergy_Type = OctetString
_EApparentEnergy_Object = MibTableColumn
eApparentEnergy = _EApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 6),
    _EApparentEnergy_Type()
)
eApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eApparentEnergy.setStatus("mandatory")
_EDateTimeApparentEnergyReset_Type = OctetString
_EDateTimeApparentEnergyReset_Object = MibTableColumn
eDateTimeApparentEnergyReset = _EDateTimeApparentEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 1, 9, 1, 7),
    _EDateTimeApparentEnergyReset_Type()
)
eDateTimeApparentEnergyReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDateTimeApparentEnergyReset.setStatus("mandatory")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2)
)
_AlarmConfigurationTable_Object = MibTable
alarmConfigurationTable = _AlarmConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alarmConfigurationTable.setStatus("mandatory")
_AlarmConfigurationEntry_Object = MibTableRow
alarmConfigurationEntry = _AlarmConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1)
)
alarmConfigurationEntry.setIndexNames(
    (0, "PM8ECCMIB", "acIndex"),
    (0, "PM8ECCMIB", "acPosition"),
)
if mibBuilder.loadTexts:
    alarmConfigurationEntry.setStatus("mandatory")


class _AcIndex_Type(Integer32):
    """Custom type acIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AcIndex_Type.__name__ = "Integer32"
_AcIndex_Object = MibTableColumn
acIndex = _AcIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 1),
    _AcIndex_Type()
)
acIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIndex.setStatus("mandatory")


class _AcPosition_Type(Integer32):
    """Custom type acPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 74),
    )


_AcPosition_Type.__name__ = "Integer32"
_AcPosition_Object = MibTableColumn
acPosition = _AcPosition_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 2),
    _AcPosition_Type()
)
acPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPosition.setStatus("mandatory")
_AcAlarmLabel_Type = AlarmLabel
_AcAlarmLabel_Object = MibTableColumn
acAlarmLabel = _AcAlarmLabel_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 3),
    _AcAlarmLabel_Type()
)
acAlarmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmLabel.setStatus("mandatory")


class _AcEnabled_Type(Integer32):
    """Custom type acEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(255, 255),
    )


_AcEnabled_Type.__name__ = "Integer32"
_AcEnabled_Object = MibTableColumn
acEnabled = _AcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 4),
    _AcEnabled_Type()
)
acEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnabled.setStatus("mandatory")


class _AcStatus_Type(Integer32):
    """Custom type acStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcStatus_Type.__name__ = "Integer32"
_AcStatus_Object = MibTableColumn
acStatus = _AcStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 5),
    _AcStatus_Type()
)
acStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStatus.setStatus("mandatory")


class _AcCounter_Type(Integer32):
    """Custom type acCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AcCounter_Type.__name__ = "Integer32"
_AcCounter_Object = MibTableColumn
acCounter = _AcCounter_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 6),
    _AcCounter_Type()
)
acCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCounter.setStatus("mandatory")


class _AcPriority_Type(Integer32):
    """Custom type acPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcPriority_Type.__name__ = "Integer32"
_AcPriority_Object = MibTableColumn
acPriority = _AcPriority_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 7),
    _AcPriority_Type()
)
acPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPriority.setStatus("mandatory")
_AcType_Type = AlarmType
_AcType_Object = MibTableColumn
acType = _AcType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 8),
    _AcType_Type()
)
acType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acType.setStatus("mandatory")
_AcAlarmList1_Type = Integer32
_AcAlarmList1_Object = MibTableColumn
acAlarmList1 = _AcAlarmList1_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 9),
    _AcAlarmList1_Type()
)
acAlarmList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmList1.setStatus("mandatory")
_AcAlarmList2_Type = Integer32
_AcAlarmList2_Object = MibTableColumn
acAlarmList2 = _AcAlarmList2_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 10),
    _AcAlarmList2_Type()
)
acAlarmList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmList2.setStatus("mandatory")
_AcAlarmList3_Type = Integer32
_AcAlarmList3_Object = MibTableColumn
acAlarmList3 = _AcAlarmList3_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 11),
    _AcAlarmList3_Type()
)
acAlarmList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmList3.setStatus("mandatory")
_AcAlarmList4_Type = Integer32
_AcAlarmList4_Object = MibTableColumn
acAlarmList4 = _AcAlarmList4_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 1, 1, 12),
    _AcAlarmList4_Type()
)
acAlarmList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmList4.setStatus("mandatory")
_AlarmSummaryBitmapsTable_Object = MibTable
alarmSummaryBitmapsTable = _AlarmSummaryBitmapsTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alarmSummaryBitmapsTable.setStatus("mandatory")
_AlarmSummaryBitmapsEntry_Object = MibTableRow
alarmSummaryBitmapsEntry = _AlarmSummaryBitmapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1)
)
alarmSummaryBitmapsEntry.setIndexNames(
    (0, "PM8ECCMIB", "alSumIndex"),
)
if mibBuilder.loadTexts:
    alarmSummaryBitmapsEntry.setStatus("mandatory")


class _AlSumIndex_Type(Integer32):
    """Custom type alSumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlSumIndex_Type.__name__ = "Integer32"
_AlSumIndex_Object = MibTableColumn
alSumIndex = _AlSumIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 1),
    _AlSumIndex_Type()
)
alSumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumIndex.setStatus("mandatory")


class _AlSumAlarms1to16_Type(OctetString):
    """Custom type alSumAlarms1to16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlSumAlarms1to16_Type.__name__ = "OctetString"
_AlSumAlarms1to16_Object = MibTableColumn
alSumAlarms1to16 = _AlSumAlarms1to16_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 2),
    _AlSumAlarms1to16_Type()
)
alSumAlarms1to16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumAlarms1to16.setStatus("mandatory")


class _AlSumAlarms17to32_Type(OctetString):
    """Custom type alSumAlarms17to32 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlSumAlarms17to32_Type.__name__ = "OctetString"
_AlSumAlarms17to32_Object = MibTableColumn
alSumAlarms17to32 = _AlSumAlarms17to32_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 3),
    _AlSumAlarms17to32_Type()
)
alSumAlarms17to32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumAlarms17to32.setStatus("mandatory")


class _AlSumAlarms33to48_Type(OctetString):
    """Custom type alSumAlarms33to48 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlSumAlarms33to48_Type.__name__ = "OctetString"
_AlSumAlarms33to48_Object = MibTableColumn
alSumAlarms33to48 = _AlSumAlarms33to48_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 4),
    _AlSumAlarms33to48_Type()
)
alSumAlarms33to48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumAlarms33to48.setStatus("mandatory")


class _AlSumAlarms49to64_Type(OctetString):
    """Custom type alSumAlarms49to64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlSumAlarms49to64_Type.__name__ = "OctetString"
_AlSumAlarms49to64_Object = MibTableColumn
alSumAlarms49to64 = _AlSumAlarms49to64_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 5),
    _AlSumAlarms49to64_Type()
)
alSumAlarms49to64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumAlarms49to64.setStatus("mandatory")


class _AlSumAlarms65to74_Type(OctetString):
    """Custom type alSumAlarms65to74 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlSumAlarms65to74_Type.__name__ = "OctetString"
_AlSumAlarms65to74_Object = MibTableColumn
alSumAlarms65to74 = _AlSumAlarms65to74_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 2, 1, 6),
    _AlSumAlarms65to74_Type()
)
alSumAlarms65to74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSumAlarms65to74.setStatus("mandatory")
_AlarmCountersTable_Object = MibTable
alarmCountersTable = _AlarmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCountersTable.setStatus("mandatory")
_AlarmCountersEntry_Object = MibTableRow
alarmCountersEntry = _AlarmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 3, 1)
)
alarmCountersEntry.setIndexNames(
    (0, "PM8ECCMIB", "alCntAlarmPosition"),
    (0, "PM8ECCMIB", "alCntIndex"),
)
if mibBuilder.loadTexts:
    alarmCountersEntry.setStatus("mandatory")


class _AlCntIndex_Type(Integer32):
    """Custom type alCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlCntIndex_Type.__name__ = "Integer32"
_AlCntIndex_Object = MibTableColumn
alCntIndex = _AlCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 3, 1, 1),
    _AlCntIndex_Type()
)
alCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCntIndex.setStatus("mandatory")


class _AlCntAlarmPosition_Type(Integer32):
    """Custom type alCntAlarmPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 74),
    )


_AlCntAlarmPosition_Type.__name__ = "Integer32"
_AlCntAlarmPosition_Object = MibTableColumn
alCntAlarmPosition = _AlCntAlarmPosition_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 3, 1, 2),
    _AlCntAlarmPosition_Type()
)
alCntAlarmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCntAlarmPosition.setStatus("mandatory")


class _AlCntCount_Type(Integer32):
    """Custom type alCntCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlCntCount_Type.__name__ = "Integer32"
_AlCntCount_Object = MibTableColumn
alCntCount = _AlCntCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 2, 3, 1, 3),
    _AlCntCount_Type()
)
alCntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCntCount.setStatus("mandatory")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3)
)
_IoOptionIDTable_Object = MibTable
ioOptionIDTable = _IoOptionIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ioOptionIDTable.setStatus("mandatory")
_IoOptionIDEntry_Object = MibTableRow
ioOptionIDEntry = _IoOptionIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 1, 1)
)
ioOptionIDEntry.setIndexNames(
    (0, "PM8ECCMIB", "ioIDIndex"),
)
if mibBuilder.loadTexts:
    ioOptionIDEntry.setStatus("mandatory")


class _IoIDIndex_Type(Integer32):
    """Custom type ioIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IoIDIndex_Type.__name__ = "Integer32"
_IoIDIndex_Object = MibTableColumn
ioIDIndex = _IoIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 1, 1, 1),
    _IoIDIndex_Type()
)
ioIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioIDIndex.setStatus("mandatory")


class _IoIDInstalledOptionSlot1_Type(Integer32):
    """Custom type ioIDInstalledOptionSlot1 based on Integer32"""
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
        *(("io-22", 2),
          ("io-2222", 4),
          ("io-26", 3),
          ("unused", 1))
    )


_IoIDInstalledOptionSlot1_Type.__name__ = "Integer32"
_IoIDInstalledOptionSlot1_Object = MibTableColumn
ioIDInstalledOptionSlot1 = _IoIDInstalledOptionSlot1_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 1, 1, 2),
    _IoIDInstalledOptionSlot1_Type()
)
ioIDInstalledOptionSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioIDInstalledOptionSlot1.setStatus("mandatory")


class _IoIDInstalledOptionSlot2_Type(Integer32):
    """Custom type ioIDInstalledOptionSlot2 based on Integer32"""
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
        *(("io-22", 2),
          ("io-2222", 4),
          ("io-26", 3),
          ("unused", 1))
    )


_IoIDInstalledOptionSlot2_Type.__name__ = "Integer32"
_IoIDInstalledOptionSlot2_Object = MibTableColumn
ioIDInstalledOptionSlot2 = _IoIDInstalledOptionSlot2_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 1, 1, 3),
    _IoIDInstalledOptionSlot2_Type()
)
ioIDInstalledOptionSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioIDInstalledOptionSlot2.setStatus("mandatory")
_IoConfigurationTable_Object = MibTable
ioConfigurationTable = _IoConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ioConfigurationTable.setStatus("mandatory")
_IoConfigurationEntry_Object = MibTableRow
ioConfigurationEntry = _IoConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1)
)
ioConfigurationEntry.setIndexNames(
    (0, "PM8ECCMIB", "iocIndex"),
    (0, "PM8ECCMIB", "iocPointNumber"),
)
if mibBuilder.loadTexts:
    ioConfigurationEntry.setStatus("mandatory")


class _IocIndex_Type(Integer32):
    """Custom type iocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IocIndex_Type.__name__ = "Integer32"
_IocIndex_Object = MibTableColumn
iocIndex = _IocIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 1),
    _IocIndex_Type()
)
iocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocIndex.setStatus("mandatory")


class _IocPointNumber_Type(Integer32):
    """Custom type iocPointNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_IocPointNumber_Type.__name__ = "Integer32"
_IocPointNumber_Object = MibTableColumn
iocPointNumber = _IocPointNumber_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 2),
    _IocPointNumber_Type()
)
iocPointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocPointNumber.setStatus("mandatory")
_IocLabel_Type = IOPointLabel
_IocLabel_Object = MibTableColumn
iocLabel = _IocLabel_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 3),
    _IocLabel_Type()
)
iocLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocLabel.setStatus("mandatory")
_IocStateOrValue_Type = OctetString
_IocStateOrValue_Object = MibTableColumn
iocStateOrValue = _IocStateOrValue_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 4),
    _IocStateOrValue_Type()
)
iocStateOrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocStateOrValue.setStatus("mandatory")
_IocPointType_Type = IOPointType
_IocPointType_Object = MibTableColumn
iocPointType = _IocPointType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 5),
    _IocPointType_Type()
)
iocPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocPointType.setStatus("mandatory")


class _IocMode_Type(Integer32):
    """Custom type iocMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_IocMode_Type.__name__ = "Integer32"
_IocMode_Object = MibTableColumn
iocMode = _IocMode_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 6),
    _IocMode_Type()
)
iocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocMode.setStatus("mandatory")
_IocType_Type = Integer32
_IocType_Object = MibTableColumn
iocType = _IocType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 7),
    _IocType_Type()
)
iocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocType.setStatus("mandatory")


class _IocCount_Type(OctetString):
    """Custom type iocCount based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IocCount_Type.__name__ = "OctetString"
_IocCount_Object = MibTableColumn
iocCount = _IocCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 2, 1, 8),
    _IocCount_Type()
)
iocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iocCount.setStatus("mandatory")
_IoStatusBitmapsTable_Object = MibTable
ioStatusBitmapsTable = _IoStatusBitmapsTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ioStatusBitmapsTable.setStatus("mandatory")
_IoStatusBitmapsEntry_Object = MibTableRow
ioStatusBitmapsEntry = _IoStatusBitmapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 3, 1)
)
ioStatusBitmapsEntry.setIndexNames(
    (0, "PM8ECCMIB", "ioStatIndex"),
)
if mibBuilder.loadTexts:
    ioStatusBitmapsEntry.setStatus("mandatory")


class _IoStatIndex_Type(Integer32):
    """Custom type ioStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IoStatIndex_Type.__name__ = "Integer32"
_IoStatIndex_Object = MibTableColumn
ioStatIndex = _IoStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 3, 1, 1),
    _IoStatIndex_Type()
)
ioStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioStatIndex.setStatus("mandatory")


class _IoStatSummaryBitmap_Type(OctetString):
    """Custom type ioStatSummaryBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_IoStatSummaryBitmap_Type.__name__ = "OctetString"
_IoStatSummaryBitmap_Object = MibTableColumn
ioStatSummaryBitmap = _IoStatSummaryBitmap_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 3, 3, 1, 2),
    _IoStatSummaryBitmap_Type()
)
ioStatSummaryBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioStatSummaryBitmap.setStatus("mandatory")
_MeterSystem_ObjectIdentity = ObjectIdentity
meterSystem = _MeterSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4)
)
_MeterIdentificationTable_Object = MibTable
meterIdentificationTable = _MeterIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    meterIdentificationTable.setStatus("mandatory")
_MeterIdentificationEntry_Object = MibTableRow
meterIdentificationEntry = _MeterIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1)
)
meterIdentificationEntry.setIndexNames(
    (0, "PM8ECCMIB", "midIndex"),
)
if mibBuilder.loadTexts:
    meterIdentificationEntry.setStatus("mandatory")


class _MidIndex_Type(Integer32):
    """Custom type midIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MidIndex_Type.__name__ = "Integer32"
_MidIndex_Object = MibTableColumn
midIndex = _MidIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1, 1),
    _MidIndex_Type()
)
midIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midIndex.setStatus("mandatory")
_MidSerialNumber_Type = Integer32
_MidSerialNumber_Object = MibTableColumn
midSerialNumber = _MidSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1, 2),
    _MidSerialNumber_Type()
)
midSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midSerialNumber.setStatus("mandatory")
_MidFirmwareVersion_Type = OctetString
_MidFirmwareVersion_Object = MibTableColumn
midFirmwareVersion = _MidFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1, 3),
    _MidFirmwareVersion_Type()
)
midFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midFirmwareVersion.setStatus("mandatory")
_MidModelNumber_Type = OctetString
_MidModelNumber_Object = MibTableColumn
midModelNumber = _MidModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1, 4),
    _MidModelNumber_Type()
)
midModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midModelNumber.setStatus("mandatory")
_MidDeviceName_Type = OctetString
_MidDeviceName_Object = MibTableColumn
midDeviceName = _MidDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 4, 1, 1, 5),
    _MidDeviceName_Type()
)
midDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midDeviceName.setStatus("mandatory")
_TrapVariables_ObjectIdentity = ObjectIdentity
trapVariables = _TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5)
)
_AlarmDateAndTime_Type = OctetString
_AlarmDateAndTime_Object = MibScalar
alarmDateAndTime = _AlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5, 1),
    _AlarmDateAndTime_Type()
)
alarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDateAndTime.setStatus("mandatory")
_AlarmLabel_Type = OctetString
_AlarmLabel_Object = MibScalar
alarmLabel = _AlarmLabel_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5, 2),
    _AlarmLabel_Type()
)
alarmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLabel.setStatus("mandatory")
_AlarmState_Type = OctetString
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5, 3),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("mandatory")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibScalar
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5, 4),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("mandatory")


class _AlarmPriority_Type(Integer32):
    """Custom type alarmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 3),
          ("mediumPriority", 2))
    )


_AlarmPriority_Type.__name__ = "Integer32"
_AlarmPriority_Object = MibScalar
alarmPriority = _AlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 5, 5),
    _AlarmPriority_Type()
)
alarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPriority.setStatus("mandatory")
_MibVersion_Type = OctetString
_MibVersion_Object = MibScalar
mibVersion = _MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 6),
    _MibVersion_Type()
)
mibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pm8OnBoardAlarmP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 0, 1)
)
pm8OnBoardAlarmP1.setObjects(
      *(("PM8ECCMIB", "alarmDateAndTime"),
        ("PM8ECCMIB", "alarmLabel"),
        ("PM8ECCMIB", "alarmState"),
        ("PM8ECCMIB", "alarmValue"),
        ("PM8ECCMIB", "alarmPriority"))
)
if mibBuilder.loadTexts:
    pm8OnBoardAlarmP1.setStatus(
        ""
    )

pm8OnBoardAlarmP2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 0, 2)
)
pm8OnBoardAlarmP2.setObjects(
      *(("PM8ECCMIB", "alarmDateAndTime"),
        ("PM8ECCMIB", "alarmLabel"),
        ("PM8ECCMIB", "alarmState"),
        ("PM8ECCMIB", "alarmValue"),
        ("PM8ECCMIB", "alarmPriority"))
)
if mibBuilder.loadTexts:
    pm8OnBoardAlarmP2.setStatus(
        ""
    )

pm8OnBoardAlarmP3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 7, 255, 15, 1, 0, 3)
)
pm8OnBoardAlarmP3.setObjects(
      *(("PM8ECCMIB", "alarmDateAndTime"),
        ("PM8ECCMIB", "alarmLabel"),
        ("PM8ECCMIB", "alarmState"),
        ("PM8ECCMIB", "alarmValue"),
        ("PM8ECCMIB", "alarmPriority"))
)
if mibBuilder.loadTexts:
    pm8OnBoardAlarmP3.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PM8ECCMIB",
    **{"AlarmType": AlarmType,
       "IOPointType": IOPointType,
       "IOPointLabel": IOPointLabel,
       "AlarmLabel": AlarmLabel,
       "schneiderElectric": schneiderElectric,
       "transparentFactoryEthernet": transparentFactoryEthernet,
       "equipmentProfile": equipmentProfile,
       "tfProducts": tfProducts,
       "ecc": ecc,
       "pm8ecc": pm8ecc,
       "pm8OnBoardAlarmP1": pm8OnBoardAlarmP1,
       "pm8OnBoardAlarmP2": pm8OnBoardAlarmP2,
       "pm8OnBoardAlarmP3": pm8OnBoardAlarmP3,
       "metering": metering,
       "systemWiringTypeTable": systemWiringTypeTable,
       "systemWiringTypeEntry": systemWiringTypeEntry,
       "swtIndex": swtIndex,
       "swtWiringType": swtWiringType,
       "loadCurrentTable": loadCurrentTable,
       "loadCurrentEntry": loadCurrentEntry,
       "lcIndex": lcIndex,
       "lcIa": lcIa,
       "lcIb": lcIb,
       "lcIc": lcIc,
       "lcIAvg": lcIAvg,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "pIndex": pIndex,
       "pReal": pReal,
       "pReactive": pReactive,
       "pApparent": pApparent,
       "powerFactorTable": powerFactorTable,
       "powerFactorEntry": powerFactorEntry,
       "pfIndex": pfIndex,
       "pfPowerFactorTotal": pfPowerFactorTotal,
       "pfPowerFactorDescription": pfPowerFactorDescription,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "vIndex": vIndex,
       "vVab": vVab,
       "vVbc": vVbc,
       "vVca": vVca,
       "vVllAvg": vVllAvg,
       "vVan": vVan,
       "vVbn": vVbn,
       "vVcn": vVcn,
       "vVlnAvg": vVlnAvg,
       "frequencyTable": frequencyTable,
       "frequencyEntry": frequencyEntry,
       "fIndex": fIndex,
       "fFrequency": fFrequency,
       "currentDemandTable": currentDemandTable,
       "currentDemandEntry": currentDemandEntry,
       "cdIndex": cdIndex,
       "cdPhase": cdPhase,
       "cdPresentCurrentDemand": cdPresentCurrentDemand,
       "cdPeakCurrentDemand": cdPeakCurrentDemand,
       "cdLastCurrentDemand": cdLastCurrentDemand,
       "cdPeakDateTime": cdPeakDateTime,
       "cdResetDateTime": cdResetDateTime,
       "cdPhaseEnum": cdPhaseEnum,
       "powerDemandTable": powerDemandTable,
       "powerDemandEntry": powerDemandEntry,
       "pdIndex": pdIndex,
       "pdComponent": pdComponent,
       "pdPresentPowerDemand": pdPresentPowerDemand,
       "pdPeakPowerDemand": pdPeakPowerDemand,
       "pdLastPowerDemand": pdLastPowerDemand,
       "pdPeakDateTime": pdPeakDateTime,
       "pdResetDateTime": pdResetDateTime,
       "pdComponentEnum": pdComponentEnum,
       "energyTable": energyTable,
       "energyEntry": energyEntry,
       "eIndex": eIndex,
       "eRealEnergy": eRealEnergy,
       "eDateTimeRealEnergyReset": eDateTimeRealEnergyReset,
       "eReactiveEnergy": eReactiveEnergy,
       "eDateTimeReactiveEnergyReset": eDateTimeReactiveEnergyReset,
       "eApparentEnergy": eApparentEnergy,
       "eDateTimeApparentEnergyReset": eDateTimeApparentEnergyReset,
       "alarms": alarms,
       "alarmConfigurationTable": alarmConfigurationTable,
       "alarmConfigurationEntry": alarmConfigurationEntry,
       "acIndex": acIndex,
       "acPosition": acPosition,
       "acAlarmLabel": acAlarmLabel,
       "acEnabled": acEnabled,
       "acStatus": acStatus,
       "acCounter": acCounter,
       "acPriority": acPriority,
       "acType": acType,
       "acAlarmList1": acAlarmList1,
       "acAlarmList2": acAlarmList2,
       "acAlarmList3": acAlarmList3,
       "acAlarmList4": acAlarmList4,
       "alarmSummaryBitmapsTable": alarmSummaryBitmapsTable,
       "alarmSummaryBitmapsEntry": alarmSummaryBitmapsEntry,
       "alSumIndex": alSumIndex,
       "alSumAlarms1to16": alSumAlarms1to16,
       "alSumAlarms17to32": alSumAlarms17to32,
       "alSumAlarms33to48": alSumAlarms33to48,
       "alSumAlarms49to64": alSumAlarms49to64,
       "alSumAlarms65to74": alSumAlarms65to74,
       "alarmCountersTable": alarmCountersTable,
       "alarmCountersEntry": alarmCountersEntry,
       "alCntIndex": alCntIndex,
       "alCntAlarmPosition": alCntAlarmPosition,
       "alCntCount": alCntCount,
       "io": io,
       "ioOptionIDTable": ioOptionIDTable,
       "ioOptionIDEntry": ioOptionIDEntry,
       "ioIDIndex": ioIDIndex,
       "ioIDInstalledOptionSlot1": ioIDInstalledOptionSlot1,
       "ioIDInstalledOptionSlot2": ioIDInstalledOptionSlot2,
       "ioConfigurationTable": ioConfigurationTable,
       "ioConfigurationEntry": ioConfigurationEntry,
       "iocIndex": iocIndex,
       "iocPointNumber": iocPointNumber,
       "iocLabel": iocLabel,
       "iocStateOrValue": iocStateOrValue,
       "iocPointType": iocPointType,
       "iocMode": iocMode,
       "iocType": iocType,
       "iocCount": iocCount,
       "ioStatusBitmapsTable": ioStatusBitmapsTable,
       "ioStatusBitmapsEntry": ioStatusBitmapsEntry,
       "ioStatIndex": ioStatIndex,
       "ioStatSummaryBitmap": ioStatSummaryBitmap,
       "meterSystem": meterSystem,
       "meterIdentificationTable": meterIdentificationTable,
       "meterIdentificationEntry": meterIdentificationEntry,
       "midIndex": midIndex,
       "midSerialNumber": midSerialNumber,
       "midFirmwareVersion": midFirmwareVersion,
       "midModelNumber": midModelNumber,
       "midDeviceName": midDeviceName,
       "trapVariables": trapVariables,
       "alarmDateAndTime": alarmDateAndTime,
       "alarmLabel": alarmLabel,
       "alarmState": alarmState,
       "alarmValue": alarmValue,
       "alarmPriority": alarmPriority,
       "mibVersion": mibVersion}
)
