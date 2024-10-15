# SNMP MIB module (POWERHUB-CORE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POWERHUB-CORE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:25 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fore_ObjectIdentity = ObjectIdentity
fore = _Fore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_Lsd_ObjectIdentity = ObjectIdentity
lsd = _Lsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6)
)
_Lsdproducts_ObjectIdentity = ObjectIdentity
lsdproducts = _Lsdproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1)
)
_Powerhub4k6k7k_ObjectIdentity = ObjectIdentity
powerhub4k6k7k = _Powerhub4k6k7k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1)
)
_Alchassis_ObjectIdentity = ObjectIdentity
alchassis = _Alchassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1)
)
_AlSlotTable_Object = MibTable
alSlotTable = _AlSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alSlotTable.setStatus("mandatory")
_AlSlotEntry_Object = MibTableRow
alSlotEntry = _AlSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1)
)
alSlotEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alSlotNumber"),
)
if mibBuilder.loadTexts:
    alSlotEntry.setStatus("mandatory")
_AlSlotNumber_Type = Integer32
_AlSlotNumber_Object = MibTableColumn
alSlotNumber = _AlSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 1),
    _AlSlotNumber_Type()
)
alSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotNumber.setStatus("mandatory")


class _AlSlotCardType_Type(Integer32):
    """Custom type alSlotCardType based on Integer32"""
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("ph4-tenbt-utp", 23),
          ("ph4k6k-FL6x1", 12),
          ("ph4k6k-ethernet100FX", 19),
          ("ph4k6k-ethernet100FXFX", 18),
          ("ph4k6k-ethernet100FXTX", 17),
          ("ph4k6k-ethernet100TX", 15),
          ("ph4k6k-ethernet100dualTX", 16),
          ("ph4k6k-ethernet12x1FL", 21),
          ("ph4k6k-ethernet24x1", 20),
          ("ph4k6k-ethernet6x1FL", 22),
          ("ph4k6k-fddisingledas", 14),
          ("ph4k6k-utp12x1", 13),
          ("ph6-powercell600", 27),
          ("ph7-10x1FL", 26),
          ("ph7-2x8fastethernet", 28),
          ("ph7-6x1fastethernet", 25),
          ("ph7-cddiconcentrator", 11),
          ("ph7-fddiconcentrator", 10),
          ("ph7-fddidualdas", 4),
          ("ph7-fddidualuniversal", 8),
          ("ph7-fddisingledas", 5),
          ("ph7-fddisingleuniversal", 9),
          ("ph7-packetengine1", 29),
          ("ph7-packetengine2", 30),
          ("ph7-powercell700", 24),
          ("ph7-universalethernet", 1),
          ("ph7-utp13x1", 7),
          ("ph7-utp16x1", 6),
          ("ph7-utp4x4", 2),
          ("ph7-utp4x6", 3))
    )


_AlSlotCardType_Type.__name__ = "Integer32"
_AlSlotCardType_Object = MibTableColumn
alSlotCardType = _AlSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 2),
    _AlSlotCardType_Type()
)
alSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotCardType.setStatus("mandatory")


class _AlSlotStatus_Type(Integer32):
    """Custom type alSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notequipped", 1),
          ("notpresent", 2),
          ("presentequipped", 3))
    )


_AlSlotStatus_Type.__name__ = "Integer32"
_AlSlotStatus_Object = MibTableColumn
alSlotStatus = _AlSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 3),
    _AlSlotStatus_Type()
)
alSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotStatus.setStatus("mandatory")
_AlSlotModel_Type = DisplayString
_AlSlotModel_Object = MibTableColumn
alSlotModel = _AlSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 4),
    _AlSlotModel_Type()
)
alSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotModel.setStatus("mandatory")
_AlSlotRevision_Type = DisplayString
_AlSlotRevision_Object = MibTableColumn
alSlotRevision = _AlSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 5),
    _AlSlotRevision_Type()
)
alSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotRevision.setStatus("mandatory")
_AlSlotIssue_Type = DisplayString
_AlSlotIssue_Object = MibTableColumn
alSlotIssue = _AlSlotIssue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 6),
    _AlSlotIssue_Type()
)
alSlotIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotIssue.setStatus("mandatory")
_AlSlotDeviation_Type = DisplayString
_AlSlotDeviation_Object = MibTableColumn
alSlotDeviation = _AlSlotDeviation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 7),
    _AlSlotDeviation_Type()
)
alSlotDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotDeviation.setStatus("mandatory")
_AlSlotSerialNumber_Type = DisplayString
_AlSlotSerialNumber_Object = MibTableColumn
alSlotSerialNumber = _AlSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 8),
    _AlSlotSerialNumber_Type()
)
alSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotSerialNumber.setStatus("mandatory")
_AlSlotPower5_Type = Integer32
_AlSlotPower5_Object = MibTableColumn
alSlotPower5 = _AlSlotPower5_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 9),
    _AlSlotPower5_Type()
)
alSlotPower5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower5.setStatus("mandatory")
_AlSlotPower12_Type = Integer32
_AlSlotPower12_Object = MibTableColumn
alSlotPower12 = _AlSlotPower12_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 10),
    _AlSlotPower12_Type()
)
alSlotPower12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower12.setStatus("mandatory")
_AlSlotPower33_Type = Integer32
_AlSlotPower33_Object = MibTableColumn
alSlotPower33 = _AlSlotPower33_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 11),
    _AlSlotPower33_Type()
)
alSlotPower33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower33.setStatus("mandatory")
_AlSlotPowerOther_Type = Integer32
_AlSlotPowerOther_Object = MibTableColumn
alSlotPowerOther = _AlSlotPowerOther_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 1, 1, 12),
    _AlSlotPowerOther_Type()
)
alSlotPowerOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPowerOther.setStatus("mandatory")
_AlVportTable_Object = MibTable
alVportTable = _AlVportTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alVportTable.setStatus("mandatory")
_AlVportEntry_Object = MibTableRow
alVportEntry = _AlVportEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1)
)
alVportEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alVportNumber"),
)
if mibBuilder.loadTexts:
    alVportEntry.setStatus("mandatory")
_AlVportNumber_Type = Integer32
_AlVportNumber_Object = MibTableColumn
alVportNumber = _AlVportNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 1),
    _AlVportNumber_Type()
)
alVportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportNumber.setStatus("mandatory")
_AlVportSlotNumber_Type = Integer32
_AlVportSlotNumber_Object = MibTableColumn
alVportSlotNumber = _AlVportSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 2),
    _AlVportSlotNumber_Type()
)
alVportSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportSlotNumber.setStatus("mandatory")
_AlVportPortNumber_Type = Integer32
_AlVportPortNumber_Object = MibTableColumn
alVportPortNumber = _AlVportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 3),
    _AlVportPortNumber_Type()
)
alVportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportPortNumber.setStatus("mandatory")


class _AlVportPortType_Type(Integer32):
    """Custom type alVportPortType based on Integer32"""
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
              66)
        )
    )
    namedValues = NamedValues(
        *(("atm", 36),
          ("aui", 3),
          ("bnc", 1),
          ("ds3-cx", 44),
          ("ds3-lmf", 41),
          ("ds3-mf", 42),
          ("ds3-sf", 43),
          ("ds3-stp", 39),
          ("ds3-utp", 38),
          ("ds3-vmf", 40),
          ("e3-cx", 51),
          ("e3-lmf", 48),
          ("e3-mf", 49),
          ("e3-sf", 50),
          ("e3-stp", 46),
          ("e3-utp", 45),
          ("e3-vmf", 47),
          ("fasteth100fx", 34),
          ("fasteth100tx", 35),
          ("fb", 6),
          ("fddiEMPTYEMPTY", 28),
          ("fddiEMPTYLC", 31),
          ("fddiEMPTYMM", 29),
          ("fddiEMPTYSM", 30),
          ("fddiEMPTYUTP", 32),
          ("fddiLCEMPTY", 22),
          ("fddiLCLC", 20),
          ("fddiLCMM", 18),
          ("fddiLCSM", 19),
          ("fddiLCUTP", 21),
          ("fddiMMEMPTY", 12),
          ("fddiMMLC", 10),
          ("fddiMMMM", 8),
          ("fddiMMSM", 9),
          ("fddiMMUTP", 11),
          ("fddiSMEMPTY", 17),
          ("fddiSMLC", 15),
          ("fddiSMMM", 13),
          ("fddiSMSM", 14),
          ("fddiSMUTP", 16),
          ("fddiUTPEMPTY", 27),
          ("fddiUTPLC", 25),
          ("fddiUTPMM", 23),
          ("fddiUTPSM", 24),
          ("fddiUTPUTP", 26),
          ("fema-10-100", 66),
          ("fiber", 2),
          ("fx100base", 33),
          ("mauFdx", 5),
          ("mauHdx", 4),
          ("notstuffed", 7),
          ("oc12-cx", 65),
          ("oc12-lmf", 62),
          ("oc12-mf", 63),
          ("oc12-sf", 64),
          ("oc12-stp", 60),
          ("oc12-utp", 59),
          ("oc12-vmf", 61),
          ("oc3-cx", 58),
          ("oc3-lmf", 55),
          ("oc3-mf", 56),
          ("oc3-sf", 57),
          ("oc3-stp", 53),
          ("oc3-utp", 52),
          ("oc3-vmf", 54),
          ("utp", 37))
    )


_AlVportPortType_Type.__name__ = "Integer32"
_AlVportPortType_Object = MibTableColumn
alVportPortType = _AlVportPortType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 4),
    _AlVportPortType_Type()
)
alVportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportPortType.setStatus("mandatory")


class _AlVportStatus_Type(Integer32):
    """Custom type alVportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("good", 3),
          ("removed", 2))
    )


_AlVportStatus_Type.__name__ = "Integer32"
_AlVportStatus_Object = MibTableColumn
alVportStatus = _AlVportStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 5),
    _AlVportStatus_Type()
)
alVportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportStatus.setStatus("mandatory")
_AlVportControllerType_Type = Integer32
_AlVportControllerType_Object = MibTableColumn
alVportControllerType = _AlVportControllerType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 6),
    _AlVportControllerType_Type()
)
alVportControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportControllerType.setStatus("mandatory")


class _AlVportDataRateConfig_Type(Integer32):
    """Custom type alVportDataRateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("speed100Mbps", 3),
          ("speed10Mbps", 2))
    )


_AlVportDataRateConfig_Type.__name__ = "Integer32"
_AlVportDataRateConfig_Object = MibTableColumn
alVportDataRateConfig = _AlVportDataRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 7),
    _AlVportDataRateConfig_Type()
)
alVportDataRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alVportDataRateConfig.setStatus("mandatory")


class _AlVportOperModeConfig_Type(Integer32):
    """Custom type alVportOperModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("decLoopback", 7),
          ("fullDuplex", 4),
          ("fullLoopback", 6),
          ("halfDuplex", 3),
          ("loopback", 5),
          ("none", 1),
          ("normal", 2))
    )


_AlVportOperModeConfig_Type.__name__ = "Integer32"
_AlVportOperModeConfig_Object = MibTableColumn
alVportOperModeConfig = _AlVportOperModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 8),
    _AlVportOperModeConfig_Type()
)
alVportOperModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alVportOperModeConfig.setStatus("mandatory")


class _AlVportAutoNegotiateConfig_Type(Integer32):
    """Custom type alVportAutoNegotiateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_AlVportAutoNegotiateConfig_Type.__name__ = "Integer32"
_AlVportAutoNegotiateConfig_Object = MibTableColumn
alVportAutoNegotiateConfig = _AlVportAutoNegotiateConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 9),
    _AlVportAutoNegotiateConfig_Type()
)
alVportAutoNegotiateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alVportAutoNegotiateConfig.setStatus("mandatory")


class _AlVportDataRateStatus_Type(Integer32):
    """Custom type alVportDataRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100Mbps", 3),
          ("speed10Mbps", 2),
          ("undetermined", 1))
    )


_AlVportDataRateStatus_Type.__name__ = "Integer32"
_AlVportDataRateStatus_Object = MibTableColumn
alVportDataRateStatus = _AlVportDataRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 10),
    _AlVportDataRateStatus_Type()
)
alVportDataRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportDataRateStatus.setStatus("mandatory")


class _AlVportOperModeStatus_Type(Integer32):
    """Custom type alVportOperModeStatus based on Integer32"""
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
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("loopback", 4),
          ("undetermined", 1))
    )


_AlVportOperModeStatus_Type.__name__ = "Integer32"
_AlVportOperModeStatus_Object = MibTableColumn
alVportOperModeStatus = _AlVportOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 2, 1, 11),
    _AlVportOperModeStatus_Type()
)
alVportOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportOperModeStatus.setStatus("mandatory")
_AlSlotToVportTable_Object = MibTable
alSlotToVportTable = _AlSlotToVportTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alSlotToVportTable.setStatus("mandatory")
_AlSlotVportEntry_Object = MibTableRow
alSlotVportEntry = _AlSlotVportEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1)
)
alSlotVportEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alSlotVportSlotNumber"),
    (0, "POWERHUB-CORE-MIB", "alSlotVportPortNumber"),
)
if mibBuilder.loadTexts:
    alSlotVportEntry.setStatus("mandatory")
_AlSlotVportSlotNumber_Type = Integer32
_AlSlotVportSlotNumber_Object = MibTableColumn
alSlotVportSlotNumber = _AlSlotVportSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 1),
    _AlSlotVportSlotNumber_Type()
)
alSlotVportSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportSlotNumber.setStatus("mandatory")
_AlSlotVportPortNumber_Type = Integer32
_AlSlotVportPortNumber_Object = MibTableColumn
alSlotVportPortNumber = _AlSlotVportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 2),
    _AlSlotVportPortNumber_Type()
)
alSlotVportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportPortNumber.setStatus("mandatory")
_AlSlotVportNumber_Type = Integer32
_AlSlotVportNumber_Object = MibTableColumn
alSlotVportNumber = _AlSlotVportNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 3),
    _AlSlotVportNumber_Type()
)
alSlotVportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportNumber.setStatus("mandatory")


class _AlSlotVportPortType_Type(Integer32):
    """Custom type alSlotVportPortType based on Integer32"""
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
              66)
        )
    )
    namedValues = NamedValues(
        *(("atm", 36),
          ("aui", 3),
          ("bnc", 1),
          ("ds3-cx", 44),
          ("ds3-lmf", 41),
          ("ds3-mf", 42),
          ("ds3-sf", 43),
          ("ds3-stp", 39),
          ("ds3-utp", 38),
          ("ds3-vmf", 40),
          ("e3-cx", 51),
          ("e3-lmf", 48),
          ("e3-mf", 49),
          ("e3-sf", 50),
          ("e3-stp", 46),
          ("e3-utp", 45),
          ("e3-vmf", 47),
          ("fasteth100fx", 34),
          ("fasteth100tx", 35),
          ("fb", 6),
          ("fddiEMPTYEMPTY", 28),
          ("fddiEMPTYLC", 31),
          ("fddiEMPTYMM", 29),
          ("fddiEMPTYSM", 30),
          ("fddiEMPTYUTP", 32),
          ("fddiLCEMPTY", 22),
          ("fddiLCLC", 20),
          ("fddiLCMM", 18),
          ("fddiLCSM", 19),
          ("fddiLCUTP", 21),
          ("fddiMMEMPTY", 12),
          ("fddiMMLC", 10),
          ("fddiMMMM", 8),
          ("fddiMMSM", 9),
          ("fddiMMUTP", 11),
          ("fddiSMEMPTY", 17),
          ("fddiSMLC", 15),
          ("fddiSMMM", 13),
          ("fddiSMSM", 14),
          ("fddiSMUTP", 16),
          ("fddiUTPEMPTY", 27),
          ("fddiUTPLC", 25),
          ("fddiUTPMM", 23),
          ("fddiUTPSM", 24),
          ("fddiUTPUTP", 26),
          ("fema-10-100", 66),
          ("fiber", 2),
          ("fx100base", 33),
          ("mauFdx", 5),
          ("mauHdx", 4),
          ("notstuffed", 7),
          ("oc12-cx", 65),
          ("oc12-lmf", 62),
          ("oc12-mf", 63),
          ("oc12-sf", 64),
          ("oc12-stp", 60),
          ("oc12-utp", 59),
          ("oc12-vmf", 61),
          ("oc3-cx", 58),
          ("oc3-lmf", 55),
          ("oc3-mf", 56),
          ("oc3-sf", 57),
          ("oc3-stp", 53),
          ("oc3-utp", 52),
          ("oc3-vmf", 54),
          ("utp", 37))
    )


_AlSlotVportPortType_Type.__name__ = "Integer32"
_AlSlotVportPortType_Object = MibTableColumn
alSlotVportPortType = _AlSlotVportPortType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 4),
    _AlSlotVportPortType_Type()
)
alSlotVportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportPortType.setStatus("mandatory")
_AlSlotVportStatus_Type = Integer32
_AlSlotVportStatus_Object = MibTableColumn
alSlotVportStatus = _AlSlotVportStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 5),
    _AlSlotVportStatus_Type()
)
alSlotVportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportStatus.setStatus("mandatory")
_AlSlotVportControllerType_Type = Integer32
_AlSlotVportControllerType_Object = MibTableColumn
alSlotVportControllerType = _AlSlotVportControllerType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 6),
    _AlSlotVportControllerType_Type()
)
alSlotVportControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportControllerType.setStatus("mandatory")


class _AlSlotVportDataRateConfig_Type(Integer32):
    """Custom type alSlotVportDataRateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("speed100Mbps", 3),
          ("speed10Mbps", 2))
    )


_AlSlotVportDataRateConfig_Type.__name__ = "Integer32"
_AlSlotVportDataRateConfig_Object = MibTableColumn
alSlotVportDataRateConfig = _AlSlotVportDataRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 7),
    _AlSlotVportDataRateConfig_Type()
)
alSlotVportDataRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSlotVportDataRateConfig.setStatus("mandatory")


class _AlSlotVportOperModeConfig_Type(Integer32):
    """Custom type alSlotVportOperModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("decLoopback", 7),
          ("fullDuplex", 4),
          ("fullLoopback", 6),
          ("halfDuplex", 3),
          ("loopback", 5),
          ("none", 1),
          ("normal", 2))
    )


_AlSlotVportOperModeConfig_Type.__name__ = "Integer32"
_AlSlotVportOperModeConfig_Object = MibTableColumn
alSlotVportOperModeConfig = _AlSlotVportOperModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 8),
    _AlSlotVportOperModeConfig_Type()
)
alSlotVportOperModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSlotVportOperModeConfig.setStatus("mandatory")


class _AlSlotVportAutoNegotiateConfig_Type(Integer32):
    """Custom type alSlotVportAutoNegotiateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_AlSlotVportAutoNegotiateConfig_Type.__name__ = "Integer32"
_AlSlotVportAutoNegotiateConfig_Object = MibTableColumn
alSlotVportAutoNegotiateConfig = _AlSlotVportAutoNegotiateConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 9),
    _AlSlotVportAutoNegotiateConfig_Type()
)
alSlotVportAutoNegotiateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSlotVportAutoNegotiateConfig.setStatus("mandatory")


class _AlSlotVportDataRateStatus_Type(Integer32):
    """Custom type alSlotVportDataRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100Mbps", 3),
          ("speed10Mbps", 2),
          ("undetermined", 1))
    )


_AlSlotVportDataRateStatus_Type.__name__ = "Integer32"
_AlSlotVportDataRateStatus_Object = MibTableColumn
alSlotVportDataRateStatus = _AlSlotVportDataRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 10),
    _AlSlotVportDataRateStatus_Type()
)
alSlotVportDataRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportDataRateStatus.setStatus("mandatory")


class _AlSlotVportOperModeStatus_Type(Integer32):
    """Custom type alSlotVportOperModeStatus based on Integer32"""
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
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("loopback", 4),
          ("undetermined", 1))
    )


_AlSlotVportOperModeStatus_Type.__name__ = "Integer32"
_AlSlotVportOperModeStatus_Object = MibTableColumn
alSlotVportOperModeStatus = _AlSlotVportOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 3, 1, 11),
    _AlSlotVportOperModeStatus_Type()
)
alSlotVportOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportOperModeStatus.setStatus("mandatory")
_AlPSTable_Object = MibTable
alPSTable = _AlPSTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alPSTable.setStatus("mandatory")
_AlPSEntry_Object = MibTableRow
alPSEntry = _AlPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 4, 1)
)
alPSEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alPSNumber"),
)
if mibBuilder.loadTexts:
    alPSEntry.setStatus("mandatory")
_AlPSNumber_Type = Integer32
_AlPSNumber_Object = MibTableColumn
alPSNumber = _AlPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 4, 1, 1),
    _AlPSNumber_Type()
)
alPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPSNumber.setStatus("mandatory")


class _AlPSStatus_Type(Integer32):
    """Custom type alPSStatus based on Integer32"""
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
        *(("powerGood", 1),
          ("powerIntermittant", 4),
          ("powerNotPresent", 3),
          ("powerPresentButBad", 2),
          ("powerUnknown", 5))
    )


_AlPSStatus_Type.__name__ = "Integer32"
_AlPSStatus_Object = MibTableColumn
alPSStatus = _AlPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 4, 1, 2),
    _AlPSStatus_Type()
)
alPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPSStatus.setStatus("mandatory")
_AlCpuSlot_Type = Integer32
_AlCpuSlot_Object = MibScalar
alCpuSlot = _AlCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 5),
    _AlCpuSlot_Type()
)
alCpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCpuSlot.setStatus("mandatory")


class _AlSlotChassis_Type(Integer32):
    """Custom type alSlotChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slots10", 2),
          ("slots15", 3),
          ("slots5", 1))
    )


_AlSlotChassis_Type.__name__ = "Integer32"
_AlSlotChassis_Object = MibScalar
alSlotChassis = _AlSlotChassis_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 6),
    _AlSlotChassis_Type()
)
alSlotChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotChassis.setStatus("mandatory")
_Powerbits_ObjectIdentity = ObjectIdentity
powerbits = _Powerbits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 2)
)
_Asn9000_ObjectIdentity = ObjectIdentity
asn9000 = _Asn9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 3)
)
_Lsdcommon_ObjectIdentity = ObjectIdentity
lsdcommon = _Lsdcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2)
)
_Alsystem_ObjectIdentity = ObjectIdentity
alsystem = _Alsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1)
)


class _AlChassisType_Type(Integer32):
    """Custom type alChassisType based on Integer32"""
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
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("model3100", 1),
          ("model3200", 2),
          ("model3300", 3),
          ("model3401", 5),
          ("model3402", 6),
          ("model3403", 7),
          ("model3404", 8),
          ("model3405", 9),
          ("model3406", 10),
          ("model3407", 11),
          ("model3410", 12),
          ("model3411", 13),
          ("model3412", 14),
          ("model3420", 15),
          ("model3421", 16),
          ("model3422", 17),
          ("model3423", 18),
          ("model3424", 19),
          ("model3425", 20),
          ("model3500", 4),
          ("model4000", 32),
          ("model4100", 33),
          ("model5001", 21),
          ("model5002", 22),
          ("model5003", 23),
          ("model5004", 24),
          ("model5005", 25),
          ("model5006", 26),
          ("model6000", 31),
          ("model7000", 30),
          ("model8000", 34))
    )


_AlChassisType_Type.__name__ = "Integer32"
_AlChassisType_Object = MibScalar
alChassisType = _AlChassisType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 1),
    _AlChassisType_Type()
)
alChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alChassisType.setStatus("mandatory")
_AlMcpuRtVer_Type = DisplayString
_AlMcpuRtVer_Object = MibScalar
alMcpuRtVer = _AlMcpuRtVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 2),
    _AlMcpuRtVer_Type()
)
alMcpuRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMcpuRtVer.setStatus("mandatory")
_AlMcpuPromVer_Type = DisplayString
_AlMcpuPromVer_Object = MibScalar
alMcpuPromVer = _AlMcpuPromVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 3),
    _AlMcpuPromVer_Type()
)
alMcpuPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMcpuPromVer.setStatus("mandatory")
_AlFcpuOneRtVer_Type = DisplayString
_AlFcpuOneRtVer_Object = MibScalar
alFcpuOneRtVer = _AlFcpuOneRtVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 4),
    _AlFcpuOneRtVer_Type()
)
alFcpuOneRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuOneRtVer.setStatus("mandatory")
_AlFcpuTwoRtVer_Type = DisplayString
_AlFcpuTwoRtVer_Object = MibScalar
alFcpuTwoRtVer = _AlFcpuTwoRtVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 5),
    _AlFcpuTwoRtVer_Type()
)
alFcpuTwoRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuTwoRtVer.setStatus("mandatory")
_AlFcpuOnePromVer_Type = DisplayString
_AlFcpuOnePromVer_Object = MibScalar
alFcpuOnePromVer = _AlFcpuOnePromVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 6),
    _AlFcpuOnePromVer_Type()
)
alFcpuOnePromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuOnePromVer.setStatus("mandatory")
_AlFcpuTwoPromVer_Type = DisplayString
_AlFcpuTwoPromVer_Object = MibScalar
alFcpuTwoPromVer = _AlFcpuTwoPromVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 7),
    _AlFcpuTwoPromVer_Type()
)
alFcpuTwoPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuTwoPromVer.setStatus("mandatory")
_AlRcpuOneRtVer_Type = DisplayString
_AlRcpuOneRtVer_Object = MibScalar
alRcpuOneRtVer = _AlRcpuOneRtVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 8),
    _AlRcpuOneRtVer_Type()
)
alRcpuOneRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuOneRtVer.setStatus("mandatory")
_AlRcpuTwoRtVer_Type = DisplayString
_AlRcpuTwoRtVer_Object = MibScalar
alRcpuTwoRtVer = _AlRcpuTwoRtVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 9),
    _AlRcpuTwoRtVer_Type()
)
alRcpuTwoRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuTwoRtVer.setStatus("mandatory")
_AlRcpuOnePromVer_Type = DisplayString
_AlRcpuOnePromVer_Object = MibScalar
alRcpuOnePromVer = _AlRcpuOnePromVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 10),
    _AlRcpuOnePromVer_Type()
)
alRcpuOnePromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuOnePromVer.setStatus("mandatory")
_AlRcpuTwoPromVer_Type = DisplayString
_AlRcpuTwoPromVer_Object = MibScalar
alRcpuTwoPromVer = _AlRcpuTwoPromVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 11),
    _AlRcpuTwoPromVer_Type()
)
alRcpuTwoPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuTwoPromVer.setStatus("mandatory")
_AlLastLoginFailureTimeDate_Type = DisplayString
_AlLastLoginFailureTimeDate_Object = MibScalar
alLastLoginFailureTimeDate = _AlLastLoginFailureTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 12),
    _AlLastLoginFailureTimeDate_Type()
)
alLastLoginFailureTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastLoginFailureTimeDate.setStatus("mandatory")
_AlLastLoginFailureUserId_Type = DisplayString
_AlLastLoginFailureUserId_Object = MibScalar
alLastLoginFailureUserId = _AlLastLoginFailureUserId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 13),
    _AlLastLoginFailureUserId_Type()
)
alLastLoginFailureUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastLoginFailureUserId.setStatus("mandatory")


class _AlLastLoginFailureReason_Type(Integer32):
    """Custom type alLastLoginFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalidLoginId", 1),
          ("passwordMismatch", 2))
    )


_AlLastLoginFailureReason_Type.__name__ = "Integer32"
_AlLastLoginFailureReason_Object = MibScalar
alLastLoginFailureReason = _AlLastLoginFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 14),
    _AlLastLoginFailureReason_Type()
)
alLastLoginFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastLoginFailureReason.setStatus("mandatory")
_AlLastLoginSourceAddress_Type = DisplayString
_AlLastLoginSourceAddress_Object = MibScalar
alLastLoginSourceAddress = _AlLastLoginSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 15),
    _AlLastLoginSourceAddress_Type()
)
alLastLoginSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastLoginSourceAddress.setStatus("mandatory")


class _AlConsoleSyslogLevel_Type(Integer32):
    """Custom type alConsoleSyslogLevel based on Integer32"""
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
        *(("logAlert", 3),
          ("logCrit", 4),
          ("logDebug", 9),
          ("logEmerg", 2),
          ("logErr", 5),
          ("logInfo", 8),
          ("logNotice", 7),
          ("logWarning", 6),
          ("off", 1))
    )


_AlConsoleSyslogLevel_Type.__name__ = "Integer32"
_AlConsoleSyslogLevel_Object = MibScalar
alConsoleSyslogLevel = _AlConsoleSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 17),
    _AlConsoleSyslogLevel_Type()
)
alConsoleSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alConsoleSyslogLevel.setStatus("mandatory")


class _AlSnmpSyslogLevel_Type(Integer32):
    """Custom type alSnmpSyslogLevel based on Integer32"""
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
        *(("logAlert", 3),
          ("logCrit", 4),
          ("logDebug", 9),
          ("logEmerg", 2),
          ("logErr", 5),
          ("logInfo", 8),
          ("logNotice", 7),
          ("logWarning", 6),
          ("off", 1))
    )


_AlSnmpSyslogLevel_Type.__name__ = "Integer32"
_AlSnmpSyslogLevel_Object = MibScalar
alSnmpSyslogLevel = _AlSnmpSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 18),
    _AlSnmpSyslogLevel_Type()
)
alSnmpSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSnmpSyslogLevel.setStatus("mandatory")


class _AlIlmiSyslogLevel_Type(Integer32):
    """Custom type alIlmiSyslogLevel based on Integer32"""
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
        *(("logAlert", 3),
          ("logCrit", 4),
          ("logDebug", 9),
          ("logEmerg", 2),
          ("logErr", 5),
          ("logInfo", 8),
          ("logNotice", 7),
          ("logWarning", 6),
          ("off", 1))
    )


_AlIlmiSyslogLevel_Type.__name__ = "Integer32"
_AlIlmiSyslogLevel_Object = MibScalar
alIlmiSyslogLevel = _AlIlmiSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 19),
    _AlIlmiSyslogLevel_Type()
)
alIlmiSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIlmiSyslogLevel.setStatus("mandatory")


class _AlSyslogHostType_Type(Integer32):
    """Custom type alSyslogHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("local", 2),
          ("notSet", 1))
    )


_AlSyslogHostType_Type.__name__ = "Integer32"
_AlSyslogHostType_Object = MibScalar
alSyslogHostType = _AlSyslogHostType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 20),
    _AlSyslogHostType_Type()
)
alSyslogHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSyslogHostType.setStatus("mandatory")
_AlSyslogHostIp_Type = DisplayString
_AlSyslogHostIp_Object = MibScalar
alSyslogHostIp = _AlSyslogHostIp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 21),
    _AlSyslogHostIp_Type()
)
alSyslogHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSyslogHostIp.setStatus("mandatory")


class _AlSyslogHostIpFacility_Type(Integer32):
    """Custom type alSyslogHostIpFacility based on Integer32"""
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
        *(("daemon", 1),
          ("local0", 2),
          ("local1", 3),
          ("local2", 4),
          ("local3", 5),
          ("local4", 6),
          ("local5", 7),
          ("local6", 8),
          ("local7", 9))
    )


_AlSyslogHostIpFacility_Type.__name__ = "Integer32"
_AlSyslogHostIpFacility_Object = MibScalar
alSyslogHostIpFacility = _AlSyslogHostIpFacility_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 22),
    _AlSyslogHostIpFacility_Type()
)
alSyslogHostIpFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSyslogHostIpFacility.setStatus("mandatory")
_Albridge_ObjectIdentity = ObjectIdentity
albridge = _Albridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2)
)
_AlBridgeTable_Object = MibTable
alBridgeTable = _AlBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alBridgeTable.setStatus("mandatory")
_AlBridgeEntry_Object = MibTableRow
alBridgeEntry = _AlBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1)
)
alBridgeEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alBridgeEntryAddress"),
)
if mibBuilder.loadTexts:
    alBridgeEntry.setStatus("mandatory")
_AlBridgeEntryAddress_Type = MacAddress
_AlBridgeEntryAddress_Object = MibTableColumn
alBridgeEntryAddress = _AlBridgeEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1, 1),
    _AlBridgeEntryAddress_Type()
)
alBridgeEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryAddress.setStatus("mandatory")
_AlBridgeEntryPort_Type = Integer32
_AlBridgeEntryPort_Object = MibTableColumn
alBridgeEntryPort = _AlBridgeEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1, 2),
    _AlBridgeEntryPort_Type()
)
alBridgeEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryPort.setStatus("mandatory")
_AlBridgeEntryLink_Type = Integer32
_AlBridgeEntryLink_Object = MibTableColumn
alBridgeEntryLink = _AlBridgeEntryLink_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1, 3),
    _AlBridgeEntryLink_Type()
)
alBridgeEntryLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryLink.setStatus("mandatory")
_AlBridgeEntryRule_Type = Integer32
_AlBridgeEntryRule_Object = MibTableColumn
alBridgeEntryRule = _AlBridgeEntryRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1, 4),
    _AlBridgeEntryRule_Type()
)
alBridgeEntryRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryRule.setStatus("mandatory")
_AlBridgeEntryFlags_Type = Integer32
_AlBridgeEntryFlags_Object = MibTableColumn
alBridgeEntryFlags = _AlBridgeEntryFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 1, 1, 5),
    _AlBridgeEntryFlags_Type()
)
alBridgeEntryFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryFlags.setStatus("mandatory")
_AlBridgeTblClear_Type = Integer32
_AlBridgeTblClear_Object = MibScalar
alBridgeTblClear = _AlBridgeTblClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 2),
    _AlBridgeTblClear_Type()
)
alBridgeTblClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeTblClear.setStatus("mandatory")
_AlBrFlushCache_Type = Integer32
_AlBrFlushCache_Object = MibScalar
alBrFlushCache = _AlBrFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 3),
    _AlBrFlushCache_Type()
)
alBrFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBrFlushCache.setStatus("mandatory")
_AlPortStatsTable_Object = MibTable
alPortStatsTable = _AlPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4)
)
if mibBuilder.loadTexts:
    alPortStatsTable.setStatus("mandatory")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1)
)
portStatsEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portStatsPort"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("mandatory")
_PortStatsPort_Type = Integer32
_PortStatsPort_Object = MibTableColumn
portStatsPort = _PortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 1),
    _PortStatsPort_Type()
)
portStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPort.setStatus("mandatory")
_PortStatsPktsIn_Type = Counter32
_PortStatsPktsIn_Object = MibTableColumn
portStatsPktsIn = _PortStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 2),
    _PortStatsPktsIn_Type()
)
portStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsIn.setStatus("mandatory")
_PortStatsPktsOut_Type = Counter32
_PortStatsPktsOut_Object = MibTableColumn
portStatsPktsOut = _PortStatsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 3),
    _PortStatsPktsOut_Type()
)
portStatsPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsOut.setStatus("mandatory")
_PortStatsOctetsIn_Type = Counter32
_PortStatsOctetsIn_Object = MibTableColumn
portStatsOctetsIn = _PortStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 4),
    _PortStatsOctetsIn_Type()
)
portStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOctetsIn.setStatus("mandatory")
_PortStatsOctetsOut_Type = Counter32
_PortStatsOctetsOut_Object = MibTableColumn
portStatsOctetsOut = _PortStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 5),
    _PortStatsOctetsOut_Type()
)
portStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOctetsOut.setStatus("mandatory")
_PortStatsMulticastPktsIn_Type = Counter32
_PortStatsMulticastPktsIn_Object = MibTableColumn
portStatsMulticastPktsIn = _PortStatsMulticastPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 6),
    _PortStatsMulticastPktsIn_Type()
)
portStatsMulticastPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsMulticastPktsIn.setStatus("mandatory")
_PortStatsMulticastPktsOut_Type = Counter32
_PortStatsMulticastPktsOut_Object = MibTableColumn
portStatsMulticastPktsOut = _PortStatsMulticastPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 7),
    _PortStatsMulticastPktsOut_Type()
)
portStatsMulticastPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsMulticastPktsOut.setStatus("mandatory")
_PortStatsTableMisses_Type = Counter32
_PortStatsTableMisses_Object = MibTableColumn
portStatsTableMisses = _PortStatsTableMisses_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 8),
    _PortStatsTableMisses_Type()
)
portStatsTableMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsTableMisses.setStatus("mandatory")
_PortStatsRcvBuffErrs_Type = Counter32
_PortStatsRcvBuffErrs_Object = MibTableColumn
portStatsRcvBuffErrs = _PortStatsRcvBuffErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 9),
    _PortStatsRcvBuffErrs_Type()
)
portStatsRcvBuffErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsRcvBuffErrs.setStatus("mandatory")
_PortStatsXmitBuffErrs_Type = Counter32
_PortStatsXmitBuffErrs_Object = MibTableColumn
portStatsXmitBuffErrs = _PortStatsXmitBuffErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 10),
    _PortStatsXmitBuffErrs_Type()
)
portStatsXmitBuffErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitBuffErrs.setStatus("mandatory")
_PortStatsTotalCollisions_Type = Counter32
_PortStatsTotalCollisions_Object = MibTableColumn
portStatsTotalCollisions = _PortStatsTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 11),
    _PortStatsTotalCollisions_Type()
)
portStatsTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsTotalCollisions.setStatus("mandatory")
_PortStatsRcvCollisions_Type = Counter32
_PortStatsRcvCollisions_Object = MibTableColumn
portStatsRcvCollisions = _PortStatsRcvCollisions_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 12),
    _PortStatsRcvCollisions_Type()
)
portStatsRcvCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsRcvCollisions.setStatus("mandatory")
_PortStatsXmitCollisions_Type = Counter32
_PortStatsXmitCollisions_Object = MibTableColumn
portStatsXmitCollisions = _PortStatsXmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 13),
    _PortStatsXmitCollisions_Type()
)
portStatsXmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitCollisions.setStatus("mandatory")
_PortStatsXmitQLen_Type = Counter32
_PortStatsXmitQLen_Object = MibTableColumn
portStatsXmitQLen = _PortStatsXmitQLen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 14),
    _PortStatsXmitQLen_Type()
)
portStatsXmitQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitQLen.setStatus("mandatory")
_PortStatsPeakUtilization_Type = Counter32
_PortStatsPeakUtilization_Object = MibTableColumn
portStatsPeakUtilization = _PortStatsPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 15),
    _PortStatsPeakUtilization_Type()
)
portStatsPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPeakUtilization.setStatus("mandatory")
_PortStatsCurrUtilization_Type = Counter32
_PortStatsCurrUtilization_Object = MibTableColumn
portStatsCurrUtilization = _PortStatsCurrUtilization_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 16),
    _PortStatsCurrUtilization_Type()
)
portStatsCurrUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsCurrUtilization.setStatus("mandatory")
_PortStatsLossOfCarrier_Type = Counter32
_PortStatsLossOfCarrier_Object = MibTableColumn
portStatsLossOfCarrier = _PortStatsLossOfCarrier_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 17),
    _PortStatsLossOfCarrier_Type()
)
portStatsLossOfCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsLossOfCarrier.setStatus("mandatory")
_PortStatsExcessRetries_Type = Counter32
_PortStatsExcessRetries_Object = MibTableColumn
portStatsExcessRetries = _PortStatsExcessRetries_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 4, 1, 18),
    _PortStatsExcessRetries_Type()
)
portStatsExcessRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsExcessRetries.setStatus("mandatory")
_AlBridgeStatsClear_Type = Integer32
_AlBridgeStatsClear_Object = MibScalar
alBridgeStatsClear = _AlBridgeStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 5),
    _AlBridgeStatsClear_Type()
)
alBridgeStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeStatsClear.setStatus("mandatory")


class _AlBridgePPControl_Type(Integer32):
    """Custom type alBridgePPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("disable", 3),
          ("enable", 1))
    )


_AlBridgePPControl_Type.__name__ = "Integer32"
_AlBridgePPControl_Object = MibScalar
alBridgePPControl = _AlBridgePPControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 6),
    _AlBridgePPControl_Type()
)
alBridgePPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgePPControl.setStatus("mandatory")
_AlPortToPortTable_Object = MibTable
alPortToPortTable = _AlPortToPortTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7)
)
if mibBuilder.loadTexts:
    alPortToPortTable.setStatus("mandatory")
_PortToPortEntry_Object = MibTableRow
portToPortEntry = _PortToPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7, 1)
)
portToPortEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "alPPSourcePort"),
    (0, "POWERHUB-CORE-MIB", "alPPDestinationPort"),
)
if mibBuilder.loadTexts:
    portToPortEntry.setStatus("mandatory")
_AlPPSourcePort_Type = Integer32
_AlPPSourcePort_Object = MibTableColumn
alPPSourcePort = _AlPPSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7, 1, 1),
    _AlPPSourcePort_Type()
)
alPPSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPSourcePort.setStatus("mandatory")
_AlPPDestinationPort_Type = Integer32
_AlPPDestinationPort_Object = MibTableColumn
alPPDestinationPort = _AlPPDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7, 1, 2),
    _AlPPDestinationPort_Type()
)
alPPDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPDestinationPort.setStatus("mandatory")
_PortToPortPackets_Type = Integer32
_PortToPortPackets_Object = MibTableColumn
portToPortPackets = _PortToPortPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7, 1, 3),
    _PortToPortPackets_Type()
)
portToPortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToPortPackets.setStatus("mandatory")
_PortToPortOctets_Type = Integer32
_PortToPortOctets_Object = MibTableColumn
portToPortOctets = _PortToPortOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 7, 1, 4),
    _PortToPortOctets_Type()
)
portToPortOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToPortOctets.setStatus("mandatory")
_AlPortConfigTable_Object = MibTable
alPortConfigTable = _AlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8)
)
if mibBuilder.loadTexts:
    alPortConfigTable.setStatus("mandatory")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8, 1)
)
portConfigEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portConfigPort"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("mandatory")
_PortConfigPort_Type = Integer32
_PortConfigPort_Object = MibTableColumn
portConfigPort = _PortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8, 1, 1),
    _PortConfigPort_Type()
)
portConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigPort.setStatus("mandatory")
_PortConfigSrcRule_Type = Integer32
_PortConfigSrcRule_Object = MibTableColumn
portConfigSrcRule = _PortConfigSrcRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8, 1, 2),
    _PortConfigSrcRule_Type()
)
portConfigSrcRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigSrcRule.setStatus("mandatory")
_PortConfigDstRule_Type = Integer32
_PortConfigDstRule_Object = MibTableColumn
portConfigDstRule = _PortConfigDstRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8, 1, 3),
    _PortConfigDstRule_Type()
)
portConfigDstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDstRule.setStatus("mandatory")


class _PortConfigBlockLearnedEntries_Type(Integer32):
    """Custom type portConfigBlockLearnedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PortConfigBlockLearnedEntries_Type.__name__ = "Integer32"
_PortConfigBlockLearnedEntries_Object = MibTableColumn
portConfigBlockLearnedEntries = _PortConfigBlockLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 8, 1, 4),
    _PortConfigBlockLearnedEntries_Type()
)
portConfigBlockLearnedEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBlockLearnedEntries.setStatus("mandatory")


class _AlBridgeIpBridging_Type(Integer32):
    """Custom type alBridgeIpBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlBridgeIpBridging_Type.__name__ = "Integer32"
_AlBridgeIpBridging_Object = MibScalar
alBridgeIpBridging = _AlBridgeIpBridging_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 9),
    _AlBridgeIpBridging_Type()
)
alBridgeIpBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeIpBridging.setStatus("mandatory")
_AlBrTemplateTable_Object = MibTable
alBrTemplateTable = _AlBrTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10)
)
if mibBuilder.loadTexts:
    alBrTemplateTable.setStatus("mandatory")
_BrTemplateEntry_Object = MibTableRow
brTemplateEntry = _BrTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1)
)
brTemplateEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "brTemplateNumber"),
)
if mibBuilder.loadTexts:
    brTemplateEntry.setStatus("mandatory")
_BrTemplateNumber_Type = Integer32
_BrTemplateNumber_Object = MibTableColumn
brTemplateNumber = _BrTemplateNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1, 1),
    _BrTemplateNumber_Type()
)
brTemplateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTemplateNumber.setStatus("mandatory")
_BrTemplateOffset_Type = Integer32
_BrTemplateOffset_Object = MibTableColumn
brTemplateOffset = _BrTemplateOffset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1, 2),
    _BrTemplateOffset_Type()
)
brTemplateOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateOffset.setStatus("mandatory")
_BrTemplateMask_Type = DisplayString
_BrTemplateMask_Object = MibTableColumn
brTemplateMask = _BrTemplateMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1, 3),
    _BrTemplateMask_Type()
)
brTemplateMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateMask.setStatus("mandatory")
_BrTemplateComparator_Type = DisplayString
_BrTemplateComparator_Object = MibTableColumn
brTemplateComparator = _BrTemplateComparator_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1, 4),
    _BrTemplateComparator_Type()
)
brTemplateComparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateComparator.setStatus("mandatory")
_BrTemplateOption_Type = Integer32
_BrTemplateOption_Object = MibTableColumn
brTemplateOption = _BrTemplateOption_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 10, 1, 5),
    _BrTemplateOption_Type()
)
brTemplateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateOption.setStatus("mandatory")
_AlBrRuleTable_Object = MibTable
alBrRuleTable = _AlBrRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 11)
)
if mibBuilder.loadTexts:
    alBrRuleTable.setStatus("mandatory")
_BrRuleEntry_Object = MibTableRow
brRuleEntry = _BrRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 11, 1)
)
brRuleEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "brRuleNumber"),
)
if mibBuilder.loadTexts:
    brRuleEntry.setStatus("mandatory")
_BrRuleNumber_Type = Integer32
_BrRuleNumber_Object = MibTableColumn
brRuleNumber = _BrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 11, 1, 1),
    _BrRuleNumber_Type()
)
brRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brRuleNumber.setStatus("mandatory")
_BrRuleStatement_Type = DisplayString
_BrRuleStatement_Object = MibTableColumn
brRuleStatement = _BrRuleStatement_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 11, 1, 2),
    _BrRuleStatement_Type()
)
brRuleStatement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleStatement.setStatus("mandatory")
_AlBrRuleToNodeTable_Object = MibTable
alBrRuleToNodeTable = _AlBrRuleToNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 12)
)
if mibBuilder.loadTexts:
    alBrRuleToNodeTable.setStatus("mandatory")
_AlBrRuleToNodeEntry_Object = MibTableRow
alBrRuleToNodeEntry = _AlBrRuleToNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 12, 1)
)
alBrRuleToNodeEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "brRuleToNodePort"),
)
if mibBuilder.loadTexts:
    alBrRuleToNodeEntry.setStatus("mandatory")
_BrRuleToNodePort_Type = Integer32
_BrRuleToNodePort_Object = MibTableColumn
brRuleToNodePort = _BrRuleToNodePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 12, 1, 1),
    _BrRuleToNodePort_Type()
)
brRuleToNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodePort.setStatus("mandatory")
_BrRuleToNodeMacAddr_Type = PhysAddress
_BrRuleToNodeMacAddr_Object = MibTableColumn
brRuleToNodeMacAddr = _BrRuleToNodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 12, 1, 2),
    _BrRuleToNodeMacAddr_Type()
)
brRuleToNodeMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodeMacAddr.setStatus("mandatory")
_BrRuleToNodeRule_Type = Integer32
_BrRuleToNodeRule_Object = MibTableColumn
brRuleToNodeRule = _BrRuleToNodeRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 12, 1, 3),
    _BrRuleToNodeRule_Type()
)
brRuleToNodeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodeRule.setStatus("mandatory")
_AlBrGroupTable_Object = MibTable
alBrGroupTable = _AlBrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 13)
)
if mibBuilder.loadTexts:
    alBrGroupTable.setStatus("mandatory")
_AlBrGroupEntry_Object = MibTableRow
alBrGroupEntry = _AlBrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 13, 1)
)
alBrGroupEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "brGroupNumber"),
)
if mibBuilder.loadTexts:
    alBrGroupEntry.setStatus("mandatory")
_BrGroupNumber_Type = Integer32
_BrGroupNumber_Object = MibTableColumn
brGroupNumber = _BrGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 13, 1, 1),
    _BrGroupNumber_Type()
)
brGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brGroupNumber.setStatus("mandatory")
_BrGroupPortsMask_Type = DisplayString
_BrGroupPortsMask_Object = MibTableColumn
brGroupPortsMask = _BrGroupPortsMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 13, 1, 2),
    _BrGroupPortsMask_Type()
)
brGroupPortsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brGroupPortsMask.setStatus("mandatory")
_BrGroupName_Type = DisplayString
_BrGroupName_Object = MibTableColumn
brGroupName = _BrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 13, 1, 3),
    _BrGroupName_Type()
)
brGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brGroupName.setStatus("mandatory")


class _AlBridgeSTPControl_Type(Integer32):
    """Custom type alBridgeSTPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlBridgeSTPControl_Type.__name__ = "Integer32"
_AlBridgeSTPControl_Object = MibScalar
alBridgeSTPControl = _AlBridgeSTPControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 14),
    _AlBridgeSTPControl_Type()
)
alBridgeSTPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeSTPControl.setStatus("mandatory")
_AlPortStateTable_Object = MibTable
alPortStateTable = _AlPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15)
)
if mibBuilder.loadTexts:
    alPortStateTable.setStatus("mandatory")
_PortStateEntry_Object = MibTableRow
portStateEntry = _PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1)
)
portStateEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portStatePort"),
)
if mibBuilder.loadTexts:
    portStateEntry.setStatus("mandatory")
_PortStatePort_Type = Integer32
_PortStatePort_Object = MibTableColumn
portStatePort = _PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1, 1),
    _PortStatePort_Type()
)
portStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatePort.setStatus("mandatory")


class _PortStateDiag_Type(Integer32):
    """Custom type portStateDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("unknown", 3))
    )


_PortStateDiag_Type.__name__ = "Integer32"
_PortStateDiag_Object = MibTableColumn
portStateDiag = _PortStateDiag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1, 2),
    _PortStateDiag_Type()
)
portStateDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateDiag.setStatus("mandatory")


class _PortStateMgmt_Type(Integer32):
    """Custom type portStateMgmt based on Integer32"""
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


_PortStateMgmt_Type.__name__ = "Integer32"
_PortStateMgmt_Object = MibTableColumn
portStateMgmt = _PortStateMgmt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1, 3),
    _PortStateMgmt_Type()
)
portStateMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateMgmt.setStatus("mandatory")
_PortStateStp_Type = Integer32
_PortStateStp_Object = MibTableColumn
portStateStp = _PortStateStp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1, 4),
    _PortStateStp_Type()
)
portStateStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateStp.setStatus("mandatory")
_PortStatePortName_Type = DisplayString
_PortStatePortName_Object = MibTableColumn
portStatePortName = _PortStatePortName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 2, 15, 1, 5),
    _PortStatePortName_Type()
)
portStatePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatePortName.setStatus("mandatory")
_Almgmt_ObjectIdentity = ObjectIdentity
almgmt = _Almgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3)
)
_AlAutoPortStateTable_Object = MibTable
alAutoPortStateTable = _AlAutoPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    alAutoPortStateTable.setStatus("mandatory")
_AutoportStateEntry_Object = MibTableRow
autoportStateEntry = _AutoportStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 1, 1)
)
autoportStateEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "autoPortStatePort"),
)
if mibBuilder.loadTexts:
    autoportStateEntry.setStatus("mandatory")
_AutoPortStatePort_Type = Integer32
_AutoPortStatePort_Object = MibTableColumn
autoPortStatePort = _AutoPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 1, 1, 1),
    _AutoPortStatePort_Type()
)
autoPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoPortStatePort.setStatus("mandatory")


class _AutoPortState_Type(Integer32):
    """Custom type autoPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutoPortState_Type.__name__ = "Integer32"
_AutoPortState_Object = MibTableColumn
autoPortState = _AutoPortState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 1, 1, 2),
    _AutoPortState_Type()
)
autoPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoPortState.setStatus("mandatory")
_AutoPortStateThreshold_Type = Integer32
_AutoPortStateThreshold_Object = MibTableColumn
autoPortStateThreshold = _AutoPortStateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 1, 1, 3),
    _AutoPortStateThreshold_Type()
)
autoPortStateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoPortStateThreshold.setStatus("mandatory")
_AlLinkStatsCollect_Type = Integer32
_AlLinkStatsCollect_Object = MibScalar
alLinkStatsCollect = _AlLinkStatsCollect_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 2),
    _AlLinkStatsCollect_Type()
)
alLinkStatsCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLinkStatsCollect.setStatus("mandatory")
_AlLinkStatsClear_Type = Integer32
_AlLinkStatsClear_Object = MibScalar
alLinkStatsClear = _AlLinkStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 3),
    _AlLinkStatsClear_Type()
)
alLinkStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLinkStatsClear.setStatus("mandatory")
_AlLinkStatsTable_Object = MibTable
alLinkStatsTable = _AlLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4)
)
if mibBuilder.loadTexts:
    alLinkStatsTable.setStatus("mandatory")
_LinkStatsEntry_Object = MibTableRow
linkStatsEntry = _LinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1)
)
linkStatsEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "linkStatsPort"),
    (0, "POWERHUB-CORE-MIB", "linkStatsLink"),
)
if mibBuilder.loadTexts:
    linkStatsEntry.setStatus("mandatory")
_LinkStatsPort_Type = Integer32
_LinkStatsPort_Object = MibTableColumn
linkStatsPort = _LinkStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 1),
    _LinkStatsPort_Type()
)
linkStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsPort.setStatus("mandatory")
_LinkStatsLink_Type = Counter32
_LinkStatsLink_Object = MibTableColumn
linkStatsLink = _LinkStatsLink_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 2),
    _LinkStatsLink_Type()
)
linkStatsLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsLink.setStatus("mandatory")
_LinkStatsPktsIn_Type = Counter32
_LinkStatsPktsIn_Object = MibTableColumn
linkStatsPktsIn = _LinkStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 3),
    _LinkStatsPktsIn_Type()
)
linkStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsPktsIn.setStatus("mandatory")
_LinkStatsOctetsIn_Type = Counter32
_LinkStatsOctetsIn_Object = MibTableColumn
linkStatsOctetsIn = _LinkStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 4),
    _LinkStatsOctetsIn_Type()
)
linkStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsOctetsIn.setStatus("mandatory")
_LinkStatsBMCastPktsIn_Type = Counter32
_LinkStatsBMCastPktsIn_Object = MibTableColumn
linkStatsBMCastPktsIn = _LinkStatsBMCastPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 5),
    _LinkStatsBMCastPktsIn_Type()
)
linkStatsBMCastPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsBMCastPktsIn.setStatus("mandatory")
_LinkStatsGiantPkts_Type = Counter32
_LinkStatsGiantPkts_Object = MibTableColumn
linkStatsGiantPkts = _LinkStatsGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 6),
    _LinkStatsGiantPkts_Type()
)
linkStatsGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsGiantPkts.setStatus("mandatory")
_LinkStatsFrameErrs_Type = Counter32
_LinkStatsFrameErrs_Object = MibTableColumn
linkStatsFrameErrs = _LinkStatsFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 7),
    _LinkStatsFrameErrs_Type()
)
linkStatsFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsFrameErrs.setStatus("mandatory")
_LinkStatsFCSErrs_Type = Counter32
_LinkStatsFCSErrs_Object = MibTableColumn
linkStatsFCSErrs = _LinkStatsFCSErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 8),
    _LinkStatsFCSErrs_Type()
)
linkStatsFCSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsFCSErrs.setStatus("mandatory")
_LinkStatsCodingErrors_Type = Counter32
_LinkStatsCodingErrors_Object = MibTableColumn
linkStatsCodingErrors = _LinkStatsCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 9),
    _LinkStatsCodingErrors_Type()
)
linkStatsCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsCodingErrors.setStatus("mandatory")
_LinkStatsDataRateMismatch_Type = Counter32
_LinkStatsDataRateMismatch_Object = MibTableColumn
linkStatsDataRateMismatch = _LinkStatsDataRateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 10),
    _LinkStatsDataRateMismatch_Type()
)
linkStatsDataRateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsDataRateMismatch.setStatus("mandatory")
_LinkStatsJabbers_Type = Counter32
_LinkStatsJabbers_Object = MibTableColumn
linkStatsJabbers = _LinkStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 11),
    _LinkStatsJabbers_Type()
)
linkStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsJabbers.setStatus("mandatory")
_LinkStatsShortEvents_Type = Counter32
_LinkStatsShortEvents_Object = MibTableColumn
linkStatsShortEvents = _LinkStatsShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 12),
    _LinkStatsShortEvents_Type()
)
linkStatsShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsShortEvents.setStatus("mandatory")
_LinkStatsRunts_Type = Counter32
_LinkStatsRunts_Object = MibTableColumn
linkStatsRunts = _LinkStatsRunts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 13),
    _LinkStatsRunts_Type()
)
linkStatsRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsRunts.setStatus("mandatory")
_LinkStatsPortCollision_Type = Counter32
_LinkStatsPortCollision_Object = MibTableColumn
linkStatsPortCollision = _LinkStatsPortCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 14),
    _LinkStatsPortCollision_Type()
)
linkStatsPortCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsPortCollision.setStatus("mandatory")
_LinkStatsLateCollision_Type = Counter32
_LinkStatsLateCollision_Object = MibTableColumn
linkStatsLateCollision = _LinkStatsLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 15),
    _LinkStatsLateCollision_Type()
)
linkStatsLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsLateCollision.setStatus("mandatory")
_LinkStatsAutoPartition_Type = Counter32
_LinkStatsAutoPartition_Object = MibTableColumn
linkStatsAutoPartition = _LinkStatsAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 16),
    _LinkStatsAutoPartition_Type()
)
linkStatsAutoPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsAutoPartition.setStatus("mandatory")
_LinkStatsIsolates_Type = Counter32
_LinkStatsIsolates_Object = MibTableColumn
linkStatsIsolates = _LinkStatsIsolates_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 17),
    _LinkStatsIsolates_Type()
)
linkStatsIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsIsolates.setStatus("mandatory")
_LinkStatsSaFieldChanges_Type = Counter32
_LinkStatsSaFieldChanges_Object = MibTableColumn
linkStatsSaFieldChanges = _LinkStatsSaFieldChanges_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 18),
    _LinkStatsSaFieldChanges_Type()
)
linkStatsSaFieldChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsSaFieldChanges.setStatus("mandatory")
_LinkStatsLastSa_Type = MacAddress
_LinkStatsLastSa_Object = MibTableColumn
linkStatsLastSa = _LinkStatsLastSa_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 4, 1, 19),
    _LinkStatsLastSa_Type()
)
linkStatsLastSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsLastSa.setStatus("mandatory")
_AlLinkControlTable_Object = MibTable
alLinkControlTable = _AlLinkControlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5)
)
if mibBuilder.loadTexts:
    alLinkControlTable.setStatus("mandatory")
_LinkControlEntry_Object = MibTableRow
linkControlEntry = _LinkControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1)
)
linkControlEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "linkControlPort"),
    (0, "POWERHUB-CORE-MIB", "linkControlLink"),
)
if mibBuilder.loadTexts:
    linkControlEntry.setStatus("mandatory")
_LinkControlPort_Type = Integer32
_LinkControlPort_Object = MibTableColumn
linkControlPort = _LinkControlPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 1),
    _LinkControlPort_Type()
)
linkControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPort.setStatus("mandatory")
_LinkControlLink_Type = Integer32
_LinkControlLink_Object = MibTableColumn
linkControlLink = _LinkControlLink_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 2),
    _LinkControlLink_Type()
)
linkControlLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlLink.setStatus("mandatory")


class _LinkControlEnlState_Type(Integer32):
    """Custom type linkControlEnlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LinkControlEnlState_Type.__name__ = "Integer32"
_LinkControlEnlState_Object = MibTableColumn
linkControlEnlState = _LinkControlEnlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 3),
    _LinkControlEnlState_Type()
)
linkControlEnlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkControlEnlState.setStatus("mandatory")
_LinkControlLinkTest_Type = Integer32
_LinkControlLinkTest_Object = MibTableColumn
linkControlLinkTest = _LinkControlLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 4),
    _LinkControlLinkTest_Type()
)
linkControlLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlLinkTest.setStatus("mandatory")
_LinkControlPartition_Type = Integer32
_LinkControlPartition_Object = MibTableColumn
linkControlPartition = _LinkControlPartition_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 5),
    _LinkControlPartition_Type()
)
linkControlPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPartition.setStatus("mandatory")
_LinkControlPolarity_Type = Integer32
_LinkControlPolarity_Object = MibTableColumn
linkControlPolarity = _LinkControlPolarity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 5, 1, 6),
    _LinkControlPolarity_Type()
)
linkControlPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPolarity.setStatus("mandatory")
_AlPortLinkTable_Object = MibTable
alPortLinkTable = _AlPortLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 6)
)
if mibBuilder.loadTexts:
    alPortLinkTable.setStatus("mandatory")
_PortLinkEntry_Object = MibTableRow
portLinkEntry = _PortLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 6, 1)
)
portLinkEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portLinkPort"),
)
if mibBuilder.loadTexts:
    portLinkEntry.setStatus("mandatory")
_PortLinkPort_Type = Integer32
_PortLinkPort_Object = MibTableColumn
portLinkPort = _PortLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 6, 1, 1),
    _PortLinkPort_Type()
)
portLinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkPort.setStatus("mandatory")


class _PortLinkType_Type(Integer32):
    """Custom type portLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("bnc", 2),
          ("bnct", 3),
          ("fiber", 5),
          ("unknown", 6),
          ("utp", 4))
    )


_PortLinkType_Type.__name__ = "Integer32"
_PortLinkType_Object = MibTableColumn
portLinkType = _PortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 6, 1, 2),
    _PortLinkType_Type()
)
portLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkType.setStatus("mandatory")
_AlFiberStatsTable_Object = MibTable
alFiberStatsTable = _AlFiberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 7)
)
if mibBuilder.loadTexts:
    alFiberStatsTable.setStatus("mandatory")
_FiberStatsEntry_Object = MibTableRow
fiberStatsEntry = _FiberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 7, 1)
)
fiberStatsEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "fiberStatsPort"),
)
if mibBuilder.loadTexts:
    fiberStatsEntry.setStatus("mandatory")
_FiberStatsPort_Type = Integer32
_FiberStatsPort_Object = MibTableColumn
fiberStatsPort = _FiberStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 7, 1, 1),
    _FiberStatsPort_Type()
)
fiberStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberStatsPort.setStatus("mandatory")
_FiberAuiStatus_Type = Integer32
_FiberAuiStatus_Object = MibTableColumn
fiberAuiStatus = _FiberAuiStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 7, 1, 2),
    _FiberAuiStatus_Type()
)
fiberAuiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAuiStatus.setStatus("mandatory")


class _FiberSecurityViolation_Type(Integer32):
    """Custom type fiberSecurityViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("detect", 1),
          ("ignore", 2))
    )


_FiberSecurityViolation_Type.__name__ = "Integer32"
_FiberSecurityViolation_Object = MibTableColumn
fiberSecurityViolation = _FiberSecurityViolation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 7, 1, 3),
    _FiberSecurityViolation_Type()
)
fiberSecurityViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberSecurityViolation.setStatus("mandatory")
_AlPortMonitorClose_Type = Integer32
_AlPortMonitorClose_Object = MibScalar
alPortMonitorClose = _AlPortMonitorClose_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 8),
    _AlPortMonitorClose_Type()
)
alPortMonitorClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPortMonitorClose.setStatus("mandatory")
_AlPortMonitorTable_Object = MibTable
alPortMonitorTable = _AlPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 9)
)
if mibBuilder.loadTexts:
    alPortMonitorTable.setStatus("mandatory")
_PortMonitorEntry_Object = MibTableRow
portMonitorEntry = _PortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 9, 1)
)
portMonitorEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portMonSrcPort"),
    (0, "POWERHUB-CORE-MIB", "portMonDstPort"),
)
if mibBuilder.loadTexts:
    portMonitorEntry.setStatus("mandatory")
_PortMonSrcPort_Type = Integer32
_PortMonSrcPort_Object = MibTableColumn
portMonSrcPort = _PortMonSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 9, 1, 1),
    _PortMonSrcPort_Type()
)
portMonSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonSrcPort.setStatus("mandatory")
_PortMonDstPort_Type = Integer32
_PortMonDstPort_Object = MibTableColumn
portMonDstPort = _PortMonDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 9, 1, 2),
    _PortMonDstPort_Type()
)
portMonDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonDstPort.setStatus("mandatory")


class _PortMonTrafficType_Type(Integer32):
    """Custom type portMonTrafficType based on Integer32"""
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
        *(("all", 7),
          ("forwarded", 1),
          ("forwardedandgenerated", 5),
          ("forwardedandincoming", 3),
          ("generated", 4),
          ("incoming", 2),
          ("incomingandgenerated", 6),
          ("stopmonitoring", 8))
    )


_PortMonTrafficType_Type.__name__ = "Integer32"
_PortMonTrafficType_Object = MibTableColumn
portMonTrafficType = _PortMonTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 9, 1, 3),
    _PortMonTrafficType_Type()
)
portMonTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonTrafficType.setStatus("mandatory")
_AlReboot_Type = Integer32
_AlReboot_Object = MibScalar
alReboot = _AlReboot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 10),
    _AlReboot_Type()
)
alReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alReboot.setStatus("mandatory")
_AlPortMonitorViewTable_Object = MibTable
alPortMonitorViewTable = _AlPortMonitorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 11)
)
if mibBuilder.loadTexts:
    alPortMonitorViewTable.setStatus("mandatory")
_PortMonitorViewEntry_Object = MibTableRow
portMonitorViewEntry = _PortMonitorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 11, 1)
)
portMonitorViewEntry.setIndexNames(
    (0, "POWERHUB-CORE-MIB", "portMonViewSrcPort"),
    (0, "POWERHUB-CORE-MIB", "portMonViewDstPort"),
)
if mibBuilder.loadTexts:
    portMonitorViewEntry.setStatus("mandatory")
_PortMonViewSrcPort_Type = Integer32
_PortMonViewSrcPort_Object = MibTableColumn
portMonViewSrcPort = _PortMonViewSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 11, 1, 1),
    _PortMonViewSrcPort_Type()
)
portMonViewSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonViewSrcPort.setStatus("mandatory")
_PortMonViewDstPort_Type = Integer32
_PortMonViewDstPort_Object = MibTableColumn
portMonViewDstPort = _PortMonViewDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 11, 1, 2),
    _PortMonViewDstPort_Type()
)
portMonViewDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonViewDstPort.setStatus("mandatory")
_PortMonViewMonitorPort_Type = DisplayString
_PortMonViewMonitorPort_Object = MibTableColumn
portMonViewMonitorPort = _PortMonViewMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 11, 1, 3),
    _PortMonViewMonitorPort_Type()
)
portMonViewMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonViewMonitorPort.setStatus("mandatory")


class _AlCfgLocalMediaScope_Type(Integer32):
    """Custom type alCfgLocalMediaScope based on Integer32"""
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
        *(("flash", 2),
          ("floppy", 1),
          ("floppyAndFlash", 3),
          ("none", 4))
    )


_AlCfgLocalMediaScope_Type.__name__ = "Integer32"
_AlCfgLocalMediaScope_Object = MibScalar
alCfgLocalMediaScope = _AlCfgLocalMediaScope_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 12),
    _AlCfgLocalMediaScope_Type()
)
alCfgLocalMediaScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCfgLocalMediaScope.setStatus("mandatory")


class _AlCfgMediaName_Type(Integer32):
    """Custom type alCfgMediaName based on Integer32"""
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
        *(("flash", 2),
          ("floppy", 1),
          ("none", 4),
          ("tftpHost", 3))
    )


_AlCfgMediaName_Type.__name__ = "Integer32"
_AlCfgMediaName_Object = MibScalar
alCfgMediaName = _AlCfgMediaName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 13),
    _AlCfgMediaName_Type()
)
alCfgMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCfgMediaName.setStatus("mandatory")
_AlCfgTftpHostAddr_Type = IpAddress
_AlCfgTftpHostAddr_Object = MibScalar
alCfgTftpHostAddr = _AlCfgTftpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 14),
    _AlCfgTftpHostAddr_Type()
)
alCfgTftpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCfgTftpHostAddr.setStatus("mandatory")
_AlCfgFileName_Type = DisplayString
_AlCfgFileName_Object = MibScalar
alCfgFileName = _AlCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 15),
    _AlCfgFileName_Type()
)
alCfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCfgFileName.setStatus("mandatory")
_AlCfgSaveOp_Type = Integer32
_AlCfgSaveOp_Object = MibScalar
alCfgSaveOp = _AlCfgSaveOp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 3, 16),
    _AlCfgSaveOp_Type()
)
alCfgSaveOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCfgSaveOp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

powerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 0, 1)
)
powerFailure.setObjects(
    ("POWERHUB-CORE-MIB", "alPSNumber")
)
if mibBuilder.loadTexts:
    powerFailure.setStatus(
        ""
    )

boardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1, 0, 2)
)
boardFailure.setObjects(
    ("POWERHUB-CORE-MIB", "alSlotNumber")
)
if mibBuilder.loadTexts:
    boardFailure.setStatus(
        ""
    )

alLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 1, 0, 1)
)
alLoginFailure.setObjects(
      *(("POWERHUB-CORE-MIB", "alLastLoginFailureTimeDate"),
        ("POWERHUB-CORE-MIB", "alLastLoginFailureUserId"),
        ("POWERHUB-CORE-MIB", "alLastLoginFailureReason"),
        ("POWERHUB-CORE-MIB", "alLastLoginSourceAddress"))
)
if mibBuilder.loadTexts:
    alLoginFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERHUB-CORE-MIB",
    **{"MacAddress": MacAddress,
       "fore": fore,
       "systems": systems,
       "lsd": lsd,
       "lsdproducts": lsdproducts,
       "powerhub4k6k7k": powerhub4k6k7k,
       "alchassis": alchassis,
       "powerFailure": powerFailure,
       "boardFailure": boardFailure,
       "alSlotTable": alSlotTable,
       "alSlotEntry": alSlotEntry,
       "alSlotNumber": alSlotNumber,
       "alSlotCardType": alSlotCardType,
       "alSlotStatus": alSlotStatus,
       "alSlotModel": alSlotModel,
       "alSlotRevision": alSlotRevision,
       "alSlotIssue": alSlotIssue,
       "alSlotDeviation": alSlotDeviation,
       "alSlotSerialNumber": alSlotSerialNumber,
       "alSlotPower5": alSlotPower5,
       "alSlotPower12": alSlotPower12,
       "alSlotPower33": alSlotPower33,
       "alSlotPowerOther": alSlotPowerOther,
       "alVportTable": alVportTable,
       "alVportEntry": alVportEntry,
       "alVportNumber": alVportNumber,
       "alVportSlotNumber": alVportSlotNumber,
       "alVportPortNumber": alVportPortNumber,
       "alVportPortType": alVportPortType,
       "alVportStatus": alVportStatus,
       "alVportControllerType": alVportControllerType,
       "alVportDataRateConfig": alVportDataRateConfig,
       "alVportOperModeConfig": alVportOperModeConfig,
       "alVportAutoNegotiateConfig": alVportAutoNegotiateConfig,
       "alVportDataRateStatus": alVportDataRateStatus,
       "alVportOperModeStatus": alVportOperModeStatus,
       "alSlotToVportTable": alSlotToVportTable,
       "alSlotVportEntry": alSlotVportEntry,
       "alSlotVportSlotNumber": alSlotVportSlotNumber,
       "alSlotVportPortNumber": alSlotVportPortNumber,
       "alSlotVportNumber": alSlotVportNumber,
       "alSlotVportPortType": alSlotVportPortType,
       "alSlotVportStatus": alSlotVportStatus,
       "alSlotVportControllerType": alSlotVportControllerType,
       "alSlotVportDataRateConfig": alSlotVportDataRateConfig,
       "alSlotVportOperModeConfig": alSlotVportOperModeConfig,
       "alSlotVportAutoNegotiateConfig": alSlotVportAutoNegotiateConfig,
       "alSlotVportDataRateStatus": alSlotVportDataRateStatus,
       "alSlotVportOperModeStatus": alSlotVportOperModeStatus,
       "alPSTable": alPSTable,
       "alPSEntry": alPSEntry,
       "alPSNumber": alPSNumber,
       "alPSStatus": alPSStatus,
       "alCpuSlot": alCpuSlot,
       "alSlotChassis": alSlotChassis,
       "powerbits": powerbits,
       "asn9000": asn9000,
       "lsdcommon": lsdcommon,
       "alsystem": alsystem,
       "alLoginFailure": alLoginFailure,
       "alChassisType": alChassisType,
       "alMcpuRtVer": alMcpuRtVer,
       "alMcpuPromVer": alMcpuPromVer,
       "alFcpuOneRtVer": alFcpuOneRtVer,
       "alFcpuTwoRtVer": alFcpuTwoRtVer,
       "alFcpuOnePromVer": alFcpuOnePromVer,
       "alFcpuTwoPromVer": alFcpuTwoPromVer,
       "alRcpuOneRtVer": alRcpuOneRtVer,
       "alRcpuTwoRtVer": alRcpuTwoRtVer,
       "alRcpuOnePromVer": alRcpuOnePromVer,
       "alRcpuTwoPromVer": alRcpuTwoPromVer,
       "alLastLoginFailureTimeDate": alLastLoginFailureTimeDate,
       "alLastLoginFailureUserId": alLastLoginFailureUserId,
       "alLastLoginFailureReason": alLastLoginFailureReason,
       "alLastLoginSourceAddress": alLastLoginSourceAddress,
       "alConsoleSyslogLevel": alConsoleSyslogLevel,
       "alSnmpSyslogLevel": alSnmpSyslogLevel,
       "alIlmiSyslogLevel": alIlmiSyslogLevel,
       "alSyslogHostType": alSyslogHostType,
       "alSyslogHostIp": alSyslogHostIp,
       "alSyslogHostIpFacility": alSyslogHostIpFacility,
       "albridge": albridge,
       "alBridgeTable": alBridgeTable,
       "alBridgeEntry": alBridgeEntry,
       "alBridgeEntryAddress": alBridgeEntryAddress,
       "alBridgeEntryPort": alBridgeEntryPort,
       "alBridgeEntryLink": alBridgeEntryLink,
       "alBridgeEntryRule": alBridgeEntryRule,
       "alBridgeEntryFlags": alBridgeEntryFlags,
       "alBridgeTblClear": alBridgeTblClear,
       "alBrFlushCache": alBrFlushCache,
       "alPortStatsTable": alPortStatsTable,
       "portStatsEntry": portStatsEntry,
       "portStatsPort": portStatsPort,
       "portStatsPktsIn": portStatsPktsIn,
       "portStatsPktsOut": portStatsPktsOut,
       "portStatsOctetsIn": portStatsOctetsIn,
       "portStatsOctetsOut": portStatsOctetsOut,
       "portStatsMulticastPktsIn": portStatsMulticastPktsIn,
       "portStatsMulticastPktsOut": portStatsMulticastPktsOut,
       "portStatsTableMisses": portStatsTableMisses,
       "portStatsRcvBuffErrs": portStatsRcvBuffErrs,
       "portStatsXmitBuffErrs": portStatsXmitBuffErrs,
       "portStatsTotalCollisions": portStatsTotalCollisions,
       "portStatsRcvCollisions": portStatsRcvCollisions,
       "portStatsXmitCollisions": portStatsXmitCollisions,
       "portStatsXmitQLen": portStatsXmitQLen,
       "portStatsPeakUtilization": portStatsPeakUtilization,
       "portStatsCurrUtilization": portStatsCurrUtilization,
       "portStatsLossOfCarrier": portStatsLossOfCarrier,
       "portStatsExcessRetries": portStatsExcessRetries,
       "alBridgeStatsClear": alBridgeStatsClear,
       "alBridgePPControl": alBridgePPControl,
       "alPortToPortTable": alPortToPortTable,
       "portToPortEntry": portToPortEntry,
       "alPPSourcePort": alPPSourcePort,
       "alPPDestinationPort": alPPDestinationPort,
       "portToPortPackets": portToPortPackets,
       "portToPortOctets": portToPortOctets,
       "alPortConfigTable": alPortConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigPort": portConfigPort,
       "portConfigSrcRule": portConfigSrcRule,
       "portConfigDstRule": portConfigDstRule,
       "portConfigBlockLearnedEntries": portConfigBlockLearnedEntries,
       "alBridgeIpBridging": alBridgeIpBridging,
       "alBrTemplateTable": alBrTemplateTable,
       "brTemplateEntry": brTemplateEntry,
       "brTemplateNumber": brTemplateNumber,
       "brTemplateOffset": brTemplateOffset,
       "brTemplateMask": brTemplateMask,
       "brTemplateComparator": brTemplateComparator,
       "brTemplateOption": brTemplateOption,
       "alBrRuleTable": alBrRuleTable,
       "brRuleEntry": brRuleEntry,
       "brRuleNumber": brRuleNumber,
       "brRuleStatement": brRuleStatement,
       "alBrRuleToNodeTable": alBrRuleToNodeTable,
       "alBrRuleToNodeEntry": alBrRuleToNodeEntry,
       "brRuleToNodePort": brRuleToNodePort,
       "brRuleToNodeMacAddr": brRuleToNodeMacAddr,
       "brRuleToNodeRule": brRuleToNodeRule,
       "alBrGroupTable": alBrGroupTable,
       "alBrGroupEntry": alBrGroupEntry,
       "brGroupNumber": brGroupNumber,
       "brGroupPortsMask": brGroupPortsMask,
       "brGroupName": brGroupName,
       "alBridgeSTPControl": alBridgeSTPControl,
       "alPortStateTable": alPortStateTable,
       "portStateEntry": portStateEntry,
       "portStatePort": portStatePort,
       "portStateDiag": portStateDiag,
       "portStateMgmt": portStateMgmt,
       "portStateStp": portStateStp,
       "portStatePortName": portStatePortName,
       "almgmt": almgmt,
       "alAutoPortStateTable": alAutoPortStateTable,
       "autoportStateEntry": autoportStateEntry,
       "autoPortStatePort": autoPortStatePort,
       "autoPortState": autoPortState,
       "autoPortStateThreshold": autoPortStateThreshold,
       "alLinkStatsCollect": alLinkStatsCollect,
       "alLinkStatsClear": alLinkStatsClear,
       "alLinkStatsTable": alLinkStatsTable,
       "linkStatsEntry": linkStatsEntry,
       "linkStatsPort": linkStatsPort,
       "linkStatsLink": linkStatsLink,
       "linkStatsPktsIn": linkStatsPktsIn,
       "linkStatsOctetsIn": linkStatsOctetsIn,
       "linkStatsBMCastPktsIn": linkStatsBMCastPktsIn,
       "linkStatsGiantPkts": linkStatsGiantPkts,
       "linkStatsFrameErrs": linkStatsFrameErrs,
       "linkStatsFCSErrs": linkStatsFCSErrs,
       "linkStatsCodingErrors": linkStatsCodingErrors,
       "linkStatsDataRateMismatch": linkStatsDataRateMismatch,
       "linkStatsJabbers": linkStatsJabbers,
       "linkStatsShortEvents": linkStatsShortEvents,
       "linkStatsRunts": linkStatsRunts,
       "linkStatsPortCollision": linkStatsPortCollision,
       "linkStatsLateCollision": linkStatsLateCollision,
       "linkStatsAutoPartition": linkStatsAutoPartition,
       "linkStatsIsolates": linkStatsIsolates,
       "linkStatsSaFieldChanges": linkStatsSaFieldChanges,
       "linkStatsLastSa": linkStatsLastSa,
       "alLinkControlTable": alLinkControlTable,
       "linkControlEntry": linkControlEntry,
       "linkControlPort": linkControlPort,
       "linkControlLink": linkControlLink,
       "linkControlEnlState": linkControlEnlState,
       "linkControlLinkTest": linkControlLinkTest,
       "linkControlPartition": linkControlPartition,
       "linkControlPolarity": linkControlPolarity,
       "alPortLinkTable": alPortLinkTable,
       "portLinkEntry": portLinkEntry,
       "portLinkPort": portLinkPort,
       "portLinkType": portLinkType,
       "alFiberStatsTable": alFiberStatsTable,
       "fiberStatsEntry": fiberStatsEntry,
       "fiberStatsPort": fiberStatsPort,
       "fiberAuiStatus": fiberAuiStatus,
       "fiberSecurityViolation": fiberSecurityViolation,
       "alPortMonitorClose": alPortMonitorClose,
       "alPortMonitorTable": alPortMonitorTable,
       "portMonitorEntry": portMonitorEntry,
       "portMonSrcPort": portMonSrcPort,
       "portMonDstPort": portMonDstPort,
       "portMonTrafficType": portMonTrafficType,
       "alReboot": alReboot,
       "alPortMonitorViewTable": alPortMonitorViewTable,
       "portMonitorViewEntry": portMonitorViewEntry,
       "portMonViewSrcPort": portMonViewSrcPort,
       "portMonViewDstPort": portMonViewDstPort,
       "portMonViewMonitorPort": portMonViewMonitorPort,
       "alCfgLocalMediaScope": alCfgLocalMediaScope,
       "alCfgMediaName": alCfgMediaName,
       "alCfgTftpHostAddr": alCfgTftpHostAddr,
       "alCfgFileName": alCfgFileName,
       "alCfgSaveOp": alCfgSaveOp}
)
