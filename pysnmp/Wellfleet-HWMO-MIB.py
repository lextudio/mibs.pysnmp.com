# SNMP MIB module (Wellfleet-HWMO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-HWMO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:21 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfHardwareConfig,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHardwareConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMod_ObjectIdentity = ObjectIdentity
wfMod = _WfMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3)
)


class _WfModState_Type(Integer32):
    """Custom type wfModState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("init", 1)
    )


_WfModState_Type.__name__ = "Integer32"
_WfModState_Object = MibScalar
wfModState = _WfModState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 1),
    _WfModState_Type()
)
wfModState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModState.setStatus("mandatory")
_WfModSlot_Type = Integer32
_WfModSlot_Object = MibScalar
wfModSlot = _WfModSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 2),
    _WfModSlot_Type()
)
wfModSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSlot.setStatus("mandatory")
_WfModIdOpt_Type = Integer32
_WfModIdOpt_Object = MibScalar
wfModIdOpt = _WfModIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 3),
    _WfModIdOpt_Type()
)
wfModIdOpt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIdOpt.setStatus("mandatory")
_WfModRev_Type = Integer32
_WfModRev_Object = MibScalar
wfModRev = _WfModRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 4),
    _WfModRev_Type()
)
wfModRev.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModRev.setStatus("mandatory")
_WfModProm_Type = Integer32
_WfModProm_Object = MibScalar
wfModProm = _WfModProm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 5),
    _WfModProm_Type()
)
wfModProm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModProm.setStatus("mandatory")
_WfModMidr_Type = Integer32
_WfModMidr_Object = MibScalar
wfModMidr = _WfModMidr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 6),
    _WfModMidr_Type()
)
wfModMidr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMidr.setStatus("mandatory")
_WfModMled_Type = Integer32
_WfModMled_Object = MibScalar
wfModMled = _WfModMled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 7),
    _WfModMled_Type()
)
wfModMled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMled.setStatus("mandatory")
_WfModMisr_Type = Integer32
_WfModMisr_Object = MibScalar
wfModMisr = _WfModMisr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 8),
    _WfModMisr_Type()
)
wfModMisr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMisr.setStatus("mandatory")
_WfModSnprom_Type = Integer32
_WfModSnprom_Object = MibScalar
wfModSnprom = _WfModSnprom_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 9),
    _WfModSnprom_Type()
)
wfModSnprom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSnprom.setStatus("mandatory")
_WfModMadr1_Type = OctetString
_WfModMadr1_Object = MibScalar
wfModMadr1 = _WfModMadr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 10),
    _WfModMadr1_Type()
)
wfModMadr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr1.setStatus("mandatory")
_WfModMadr2_Type = OctetString
_WfModMadr2_Object = MibScalar
wfModMadr2 = _WfModMadr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 11),
    _WfModMadr2_Type()
)
wfModMadr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr2.setStatus("mandatory")
_WfModMadr3_Type = OctetString
_WfModMadr3_Object = MibScalar
wfModMadr3 = _WfModMadr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 12),
    _WfModMadr3_Type()
)
wfModMadr3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr3.setStatus("mandatory")
_WfModMadr4_Type = OctetString
_WfModMadr4_Object = MibScalar
wfModMadr4 = _WfModMadr4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 13),
    _WfModMadr4_Type()
)
wfModMadr4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr4.setStatus("mandatory")
_WfModLance1_Type = Integer32
_WfModLance1_Object = MibScalar
wfModLance1 = _WfModLance1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 14),
    _WfModLance1_Type()
)
wfModLance1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModLance1.setStatus("mandatory")
_WfModLance2_Type = Integer32
_WfModLance2_Object = MibScalar
wfModLance2 = _WfModLance2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 15),
    _WfModLance2_Type()
)
wfModLance2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModLance2.setStatus("mandatory")
_WfModMk50251_Type = Integer32
_WfModMk50251_Object = MibScalar
wfModMk50251 = _WfModMk50251_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 16),
    _WfModMk50251_Type()
)
wfModMk50251.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50251.setStatus("mandatory")
_WfModMk50252_Type = Integer32
_WfModMk50252_Object = MibScalar
wfModMk50252 = _WfModMk50252_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 17),
    _WfModMk50252_Type()
)
wfModMk50252.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50252.setStatus("mandatory")
_WfModMk50253_Type = Integer32
_WfModMk50253_Object = MibScalar
wfModMk50253 = _WfModMk50253_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 18),
    _WfModMk50253_Type()
)
wfModMk50253.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50253.setStatus("mandatory")
_WfModMk50254_Type = Integer32
_WfModMk50254_Object = MibScalar
wfModMk50254 = _WfModMk50254_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 19),
    _WfModMk50254_Type()
)
wfModMk50254.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50254.setStatus("mandatory")
_WfModSicr_Type = Integer32
_WfModSicr_Object = MibScalar
wfModSicr = _WfModSicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 20),
    _WfModSicr_Type()
)
wfModSicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSicr.setStatus("mandatory")
_WfModSbrr_Type = Integer32
_WfModSbrr_Object = MibScalar
wfModSbrr = _WfModSbrr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 21),
    _WfModSbrr_Type()
)
wfModSbrr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSbrr.setStatus("mandatory")
_WfMod8530_Type = Integer32
_WfMod8530_Object = MibScalar
wfMod8530 = _WfMod8530_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 22),
    _WfMod8530_Type()
)
wfMod8530.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfMod8530.setStatus("mandatory")
_WfModCar_Type = Integer32
_WfModCar_Object = MibScalar
wfModCar = _WfModCar_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 23),
    _WfModCar_Type()
)
wfModCar.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCar.setStatus("mandatory")
_WfModDefaA_Type = Integer32
_WfModDefaA_Object = MibScalar
wfModDefaA = _WfModDefaA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 24),
    _WfModDefaA_Type()
)
wfModDefaA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDefaA.setStatus("mandatory")
_WfModCamALock_Type = Integer32
_WfModCamALock_Object = MibScalar
wfModCamALock = _WfModCamALock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 25),
    _WfModCamALock_Type()
)
wfModCamALock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamALock.setStatus("mandatory")
_WfModCamAUnlock_Type = Integer32
_WfModCamAUnlock_Object = MibScalar
wfModCamAUnlock = _WfModCamAUnlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 26),
    _WfModCamAUnlock_Type()
)
wfModCamAUnlock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamAUnlock.setStatus("mandatory")
_WfModDefaB_Type = Integer32
_WfModDefaB_Object = MibScalar
wfModDefaB = _WfModDefaB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 27),
    _WfModDefaB_Type()
)
wfModDefaB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDefaB.setStatus("mandatory")
_WfModCamBLock_Type = Integer32
_WfModCamBLock_Object = MibScalar
wfModCamBLock = _WfModCamBLock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 28),
    _WfModCamBLock_Type()
)
wfModCamBLock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamBLock.setStatus("mandatory")
_WfModCamBUnlock_Type = Integer32
_WfModCamBUnlock_Object = MibScalar
wfModCamBUnlock = _WfModCamBUnlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 29),
    _WfModCamBUnlock_Type()
)
wfModCamBUnlock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamBUnlock.setStatus("mandatory")
_WfModIlacc1_Type = Integer32
_WfModIlacc1_Object = MibScalar
wfModIlacc1 = _WfModIlacc1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 30),
    _WfModIlacc1_Type()
)
wfModIlacc1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc1.setStatus("mandatory")
_WfModIlacc2_Type = Integer32
_WfModIlacc2_Object = MibScalar
wfModIlacc2 = _WfModIlacc2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 31),
    _WfModIlacc2_Type()
)
wfModIlacc2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc2.setStatus("mandatory")
_WfModIlacc3_Type = Integer32
_WfModIlacc3_Object = MibScalar
wfModIlacc3 = _WfModIlacc3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 32),
    _WfModIlacc3_Type()
)
wfModIlacc3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc3.setStatus("mandatory")
_WfModIlacc4_Type = Integer32
_WfModIlacc4_Object = MibScalar
wfModIlacc4 = _WfModIlacc4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 33),
    _WfModIlacc4_Type()
)
wfModIlacc4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc4.setStatus("mandatory")
_WfModTms3801_Type = Integer32
_WfModTms3801_Object = MibScalar
wfModTms3801 = _WfModTms3801_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 34),
    _WfModTms3801_Type()
)
wfModTms3801.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3801.setStatus("mandatory")
_WfModTms3802_Type = Integer32
_WfModTms3802_Object = MibScalar
wfModTms3802 = _WfModTms3802_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 35),
    _WfModTms3802_Type()
)
wfModTms3802.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3802.setStatus("mandatory")
_WfModTocr_Type = Integer32
_WfModTocr_Object = MibScalar
wfModTocr = _WfModTocr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 36),
    _WfModTocr_Type()
)
wfModTocr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTocr.setStatus("mandatory")
_WfModTsra_Type = Integer32
_WfModTsra_Object = MibScalar
wfModTsra = _WfModTsra_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 37),
    _WfModTsra_Type()
)
wfModTsra.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTsra.setStatus("mandatory")
_WfModMuxram1_Type = Integer32
_WfModMuxram1_Object = MibScalar
wfModMuxram1 = _WfModMuxram1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 38),
    _WfModMuxram1_Type()
)
wfModMuxram1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMuxram1.setStatus("mandatory")
_WfModMuxram2_Type = Integer32
_WfModMuxram2_Object = MibScalar
wfModMuxram2 = _WfModMuxram2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 39),
    _WfModMuxram2_Type()
)
wfModMuxram2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMuxram2.setStatus("mandatory")
_WfModTicr_Type = Integer32
_WfModTicr_Object = MibScalar
wfModTicr = _WfModTicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 40),
    _WfModTicr_Type()
)
wfModTicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTicr.setStatus("mandatory")
_WfModFramer1_Type = Integer32
_WfModFramer1_Object = MibScalar
wfModFramer1 = _WfModFramer1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 41),
    _WfModFramer1_Type()
)
wfModFramer1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFramer1.setStatus("mandatory")
_WfModFramer2_Type = Integer32
_WfModFramer2_Object = MibScalar
wfModFramer2 = _WfModFramer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 42),
    _WfModFramer2_Type()
)
wfModFramer2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFramer2.setStatus("mandatory")
_WfModFsi1_Type = Integer32
_WfModFsi1_Object = MibScalar
wfModFsi1 = _WfModFsi1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 43),
    _WfModFsi1_Type()
)
wfModFsi1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFsi1.setStatus("mandatory")
_WfModMac1_Type = Integer32
_WfModMac1_Object = MibScalar
wfModMac1 = _WfModMac1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 44),
    _WfModMac1_Type()
)
wfModMac1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMac1.setStatus("mandatory")
_WfModElmA1_Type = Integer32
_WfModElmA1_Object = MibScalar
wfModElmA1 = _WfModElmA1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 45),
    _WfModElmA1_Type()
)
wfModElmA1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModElmA1.setStatus("mandatory")
_WfModElmB1_Type = Integer32
_WfModElmB1_Object = MibScalar
wfModElmB1 = _WfModElmB1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 46),
    _WfModElmB1_Type()
)
wfModElmB1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModElmB1.setStatus("mandatory")
_WfModMcr1_Type = Integer32
_WfModMcr1_Object = MibScalar
wfModMcr1 = _WfModMcr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 47),
    _WfModMcr1_Type()
)
wfModMcr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMcr1.setStatus("mandatory")
_WfModHssiFsi1_Type = Integer32
_WfModHssiFsi1_Object = MibScalar
wfModHssiFsi1 = _WfModHssiFsi1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 48),
    _WfModHssiFsi1_Type()
)
wfModHssiFsi1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiFsi1.setStatus("mandatory")
_WfModHssiFsi2_Type = Integer32
_WfModHssiFsi2_Object = MibScalar
wfModHssiFsi2 = _WfModHssiFsi2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 49),
    _WfModHssiFsi2_Type()
)
wfModHssiFsi2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiFsi2.setStatus("mandatory")
_WfModHssiUga1_Type = Integer32
_WfModHssiUga1_Object = MibScalar
wfModHssiUga1 = _WfModHssiUga1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 50),
    _WfModHssiUga1_Type()
)
wfModHssiUga1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiUga1.setStatus("mandatory")
_WfModHssiUga2_Type = Integer32
_WfModHssiUga2_Object = MibScalar
wfModHssiUga2 = _WfModHssiUga2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 51),
    _WfModHssiUga2_Type()
)
wfModHssiUga2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiUga2.setStatus("mandatory")
_WfModHicr_Type = Integer32
_WfModHicr_Object = MibScalar
wfModHicr = _WfModHicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 52),
    _WfModHicr_Type()
)
wfModHicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHicr.setStatus("mandatory")
_WfModHicrData_Type = Integer32
_WfModHicrData_Object = MibScalar
wfModHicrData = _WfModHicrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 53),
    _WfModHicrData_Type()
)
wfModHicrData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHicrData.setStatus("mandatory")
_WfModHlsr_Type = Integer32
_WfModHlsr_Object = MibScalar
wfModHlsr = _WfModHlsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 54),
    _WfModHlsr_Type()
)
wfModHlsr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHlsr.setStatus("mandatory")
_WfModHlsrData_Type = Integer32
_WfModHlsrData_Object = MibScalar
wfModHlsrData = _WfModHlsrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 55),
    _WfModHlsrData_Type()
)
wfModHlsrData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHlsrData.setStatus("mandatory")
_WfModMCR0_Type = Integer32
_WfModMCR0_Object = MibScalar
wfModMCR0 = _WfModMCR0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 56),
    _WfModMCR0_Type()
)
wfModMCR0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMCR0.setStatus("mandatory")
_WfModMCR1_Type = Integer32
_WfModMCR1_Object = MibScalar
wfModMCR1 = _WfModMCR1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 57),
    _WfModMCR1_Type()
)
wfModMCR1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMCR1.setStatus("mandatory")
_WfModCcr0_Type = Integer32
_WfModCcr0_Object = MibScalar
wfModCcr0 = _WfModCcr0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 58),
    _WfModCcr0_Type()
)
wfModCcr0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCcr0.setStatus("mandatory")
_WfModCcr1_Type = Integer32
_WfModCcr1_Object = MibScalar
wfModCcr1 = _WfModCcr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 59),
    _WfModCcr1_Type()
)
wfModCcr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCcr1.setStatus("mandatory")
_WfModFcr_Type = Integer32
_WfModFcr_Object = MibScalar
wfModFcr = _WfModFcr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 60),
    _WfModFcr_Type()
)
wfModFcr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFcr.setStatus("mandatory")
_WfModMar0_Type = Integer32
_WfModMar0_Object = MibScalar
wfModMar0 = _WfModMar0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 61),
    _WfModMar0_Type()
)
wfModMar0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMar0.setStatus("mandatory")
_WfModMar1_Type = Integer32
_WfModMar1_Object = MibScalar
wfModMar1 = _WfModMar1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 62),
    _WfModMar1_Type()
)
wfModMar1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMar1.setStatus("mandatory")
_WfModBert_Type = Integer32
_WfModBert_Object = MibScalar
wfModBert = _WfModBert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 63),
    _WfModBert_Type()
)
wfModBert.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModBert.setStatus("mandatory")
_WfModMgbc_Type = Integer32
_WfModMgbc_Object = MibScalar
wfModMgbc = _WfModMgbc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 64),
    _WfModMgbc_Type()
)
wfModMgbc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMgbc.setStatus("mandatory")
_WfModClr0_Type = Integer32
_WfModClr0_Object = MibScalar
wfModClr0 = _WfModClr0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 65),
    _WfModClr0_Type()
)
wfModClr0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModClr0.setStatus("mandatory")
_WfModClr1_Type = Integer32
_WfModClr1_Object = MibScalar
wfModClr1 = _WfModClr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 66),
    _WfModClr1_Type()
)
wfModClr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModClr1.setStatus("mandatory")
_WfModCclk_Type = Integer32
_WfModCclk_Object = MibScalar
wfModCclk = _WfModCclk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 67),
    _WfModCclk_Type()
)
wfModCclk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCclk.setStatus("mandatory")
_WfModCLoopup0_Type = Integer32
_WfModCLoopup0_Object = MibScalar
wfModCLoopup0 = _WfModCLoopup0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 68),
    _WfModCLoopup0_Type()
)
wfModCLoopup0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCLoopup0.setStatus("mandatory")
_WfModCLoopup1_Type = Integer32
_WfModCLoopup1_Object = MibScalar
wfModCLoopup1 = _WfModCLoopup1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 69),
    _WfModCLoopup1_Type()
)
wfModCLoopup1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCLoopup1.setStatus("mandatory")
_WfModCLoopdn0_Type = Integer32
_WfModCLoopdn0_Object = MibScalar
wfModCLoopdn0 = _WfModCLoopdn0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 70),
    _WfModCLoopdn0_Type()
)
wfModCLoopdn0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCLoopdn0.setStatus("mandatory")
_WfModCLoopdn1_Type = Integer32
_WfModCLoopdn1_Object = MibScalar
wfModCLoopdn1 = _WfModCLoopdn1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 71),
    _WfModCLoopdn1_Type()
)
wfModCLoopdn1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCLoopdn1.setStatus("mandatory")
_WfModDuart_Type = Integer32
_WfModDuart_Object = MibScalar
wfModDuart = _WfModDuart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 72),
    _WfModDuart_Type()
)
wfModDuart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDuart.setStatus("mandatory")
_WfModLEDC_Type = Integer32
_WfModLEDC_Object = MibScalar
wfModLEDC = _WfModLEDC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 73),
    _WfModLEDC_Type()
)
wfModLEDC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModLEDC.setStatus("mandatory")
_WfModMadr5_Type = OctetString
_WfModMadr5_Object = MibScalar
wfModMadr5 = _WfModMadr5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 74),
    _WfModMadr5_Type()
)
wfModMadr5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr5.setStatus("mandatory")
_WfModDefaC_Type = Integer32
_WfModDefaC_Object = MibScalar
wfModDefaC = _WfModDefaC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 75),
    _WfModDefaC_Type()
)
wfModDefaC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDefaC.setStatus("mandatory")
_WfModCamel1_Type = Integer32
_WfModCamel1_Object = MibScalar
wfModCamel1 = _WfModCamel1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 76),
    _WfModCamel1_Type()
)
wfModCamel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamel1.setStatus("mandatory")
_WfModTms3803_Type = Integer32
_WfModTms3803_Object = MibScalar
wfModTms3803 = _WfModTms3803_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 77),
    _WfModTms3803_Type()
)
wfModTms3803.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3803.setStatus("mandatory")
_WfModTms3804_Type = Integer32
_WfModTms3804_Object = MibScalar
wfModTms3804 = _WfModTms3804_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 78),
    _WfModTms3804_Type()
)
wfModTms3804.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3804.setStatus("mandatory")
_WfModMusicSRT1_Type = Integer32
_WfModMusicSRT1_Object = MibScalar
wfModMusicSRT1 = _WfModMusicSRT1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 79),
    _WfModMusicSRT1_Type()
)
wfModMusicSRT1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMusicSRT1.setStatus("mandatory")
_WfModMusicSRT2_Type = Integer32
_WfModMusicSRT2_Object = MibScalar
wfModMusicSRT2 = _WfModMusicSRT2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 80),
    _WfModMusicSRT2_Type()
)
wfModMusicSRT2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMusicSRT2.setStatus("mandatory")
_WfModMusicSRT3_Type = Integer32
_WfModMusicSRT3_Object = MibScalar
wfModMusicSRT3 = _WfModMusicSRT3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 81),
    _WfModMusicSRT3_Type()
)
wfModMusicSRT3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMusicSRT3.setStatus("mandatory")
_WfModMusicSRT4_Type = Integer32
_WfModMusicSRT4_Object = MibScalar
wfModMusicSRT4 = _WfModMusicSRT4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 82),
    _WfModMusicSRT4_Type()
)
wfModMusicSRT4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMusicSRT4.setStatus("mandatory")
_WfModClrQ1Reset_Type = Integer32
_WfModClrQ1Reset_Object = MibScalar
wfModClrQ1Reset = _WfModClrQ1Reset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 83),
    _WfModClrQ1Reset_Type()
)
wfModClrQ1Reset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModClrQ1Reset.setStatus("mandatory")
_WfModClrQ2Reset_Type = Integer32
_WfModClrQ2Reset_Object = MibScalar
wfModClrQ2Reset = _WfModClrQ2Reset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 84),
    _WfModClrQ2Reset_Type()
)
wfModClrQ2Reset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModClrQ2Reset.setStatus("mandatory")
_WfModQ1Dram_Type = Integer32
_WfModQ1Dram_Object = MibScalar
wfModQ1Dram = _WfModQ1Dram_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 85),
    _WfModQ1Dram_Type()
)
wfModQ1Dram.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ1Dram.setStatus("mandatory")
_WfModQ2Dram_Type = Integer32
_WfModQ2Dram_Object = MibScalar
wfModQ2Dram = _WfModQ2Dram_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 86),
    _WfModQ2Dram_Type()
)
wfModQ2Dram.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ2Dram.setStatus("mandatory")
_WfModQ1DPram_Type = Integer32
_WfModQ1DPram_Object = MibScalar
wfModQ1DPram = _WfModQ1DPram_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 87),
    _WfModQ1DPram_Type()
)
wfModQ1DPram.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ1DPram.setStatus("mandatory")
_WfModQ2DPram_Type = Integer32
_WfModQ2DPram_Object = MibScalar
wfModQ2DPram = _WfModQ2DPram_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 88),
    _WfModQ2DPram_Type()
)
wfModQ2DPram.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ2DPram.setStatus("mandatory")
_WfModQ1StickyBit_Type = Integer32
_WfModQ1StickyBit_Object = MibScalar
wfModQ1StickyBit = _WfModQ1StickyBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 89),
    _WfModQ1StickyBit_Type()
)
wfModQ1StickyBit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ1StickyBit.setStatus("mandatory")
_WfModQ2StickyBit_Type = Integer32
_WfModQ2StickyBit_Object = MibScalar
wfModQ2StickyBit = _WfModQ2StickyBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 90),
    _WfModQ2StickyBit_Type()
)
wfModQ2StickyBit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ2StickyBit.setStatus("mandatory")
_WfModQ1Int7_Type = Integer32
_WfModQ1Int7_Object = MibScalar
wfModQ1Int7 = _WfModQ1Int7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 91),
    _WfModQ1Int7_Type()
)
wfModQ1Int7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ1Int7.setStatus("mandatory")
_WfModQ2Int7_Type = Integer32
_WfModQ2Int7_Object = MibScalar
wfModQ2Int7 = _WfModQ2Int7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 92),
    _WfModQ2Int7_Type()
)
wfModQ2Int7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModQ2Int7.setStatus("mandatory")
_WfModApplyQ1Reset_Type = Integer32
_WfModApplyQ1Reset_Object = MibScalar
wfModApplyQ1Reset = _WfModApplyQ1Reset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 93),
    _WfModApplyQ1Reset_Type()
)
wfModApplyQ1Reset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModApplyQ1Reset.setStatus("mandatory")
_WfModApplyQ2Reset_Type = Integer32
_WfModApplyQ2Reset_Object = MibScalar
wfModApplyQ2Reset = _WfModApplyQ2Reset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 94),
    _WfModApplyQ2Reset_Type()
)
wfModApplyQ2Reset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModApplyQ2Reset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-HWMO-MIB",
    **{"wfMod": wfMod,
       "wfModState": wfModState,
       "wfModSlot": wfModSlot,
       "wfModIdOpt": wfModIdOpt,
       "wfModRev": wfModRev,
       "wfModProm": wfModProm,
       "wfModMidr": wfModMidr,
       "wfModMled": wfModMled,
       "wfModMisr": wfModMisr,
       "wfModSnprom": wfModSnprom,
       "wfModMadr1": wfModMadr1,
       "wfModMadr2": wfModMadr2,
       "wfModMadr3": wfModMadr3,
       "wfModMadr4": wfModMadr4,
       "wfModLance1": wfModLance1,
       "wfModLance2": wfModLance2,
       "wfModMk50251": wfModMk50251,
       "wfModMk50252": wfModMk50252,
       "wfModMk50253": wfModMk50253,
       "wfModMk50254": wfModMk50254,
       "wfModSicr": wfModSicr,
       "wfModSbrr": wfModSbrr,
       "wfMod8530": wfMod8530,
       "wfModCar": wfModCar,
       "wfModDefaA": wfModDefaA,
       "wfModCamALock": wfModCamALock,
       "wfModCamAUnlock": wfModCamAUnlock,
       "wfModDefaB": wfModDefaB,
       "wfModCamBLock": wfModCamBLock,
       "wfModCamBUnlock": wfModCamBUnlock,
       "wfModIlacc1": wfModIlacc1,
       "wfModIlacc2": wfModIlacc2,
       "wfModIlacc3": wfModIlacc3,
       "wfModIlacc4": wfModIlacc4,
       "wfModTms3801": wfModTms3801,
       "wfModTms3802": wfModTms3802,
       "wfModTocr": wfModTocr,
       "wfModTsra": wfModTsra,
       "wfModMuxram1": wfModMuxram1,
       "wfModMuxram2": wfModMuxram2,
       "wfModTicr": wfModTicr,
       "wfModFramer1": wfModFramer1,
       "wfModFramer2": wfModFramer2,
       "wfModFsi1": wfModFsi1,
       "wfModMac1": wfModMac1,
       "wfModElmA1": wfModElmA1,
       "wfModElmB1": wfModElmB1,
       "wfModMcr1": wfModMcr1,
       "wfModHssiFsi1": wfModHssiFsi1,
       "wfModHssiFsi2": wfModHssiFsi2,
       "wfModHssiUga1": wfModHssiUga1,
       "wfModHssiUga2": wfModHssiUga2,
       "wfModHicr": wfModHicr,
       "wfModHicrData": wfModHicrData,
       "wfModHlsr": wfModHlsr,
       "wfModHlsrData": wfModHlsrData,
       "wfModMCR0": wfModMCR0,
       "wfModMCR1": wfModMCR1,
       "wfModCcr0": wfModCcr0,
       "wfModCcr1": wfModCcr1,
       "wfModFcr": wfModFcr,
       "wfModMar0": wfModMar0,
       "wfModMar1": wfModMar1,
       "wfModBert": wfModBert,
       "wfModMgbc": wfModMgbc,
       "wfModClr0": wfModClr0,
       "wfModClr1": wfModClr1,
       "wfModCclk": wfModCclk,
       "wfModCLoopup0": wfModCLoopup0,
       "wfModCLoopup1": wfModCLoopup1,
       "wfModCLoopdn0": wfModCLoopdn0,
       "wfModCLoopdn1": wfModCLoopdn1,
       "wfModDuart": wfModDuart,
       "wfModLEDC": wfModLEDC,
       "wfModMadr5": wfModMadr5,
       "wfModDefaC": wfModDefaC,
       "wfModCamel1": wfModCamel1,
       "wfModTms3803": wfModTms3803,
       "wfModTms3804": wfModTms3804,
       "wfModMusicSRT1": wfModMusicSRT1,
       "wfModMusicSRT2": wfModMusicSRT2,
       "wfModMusicSRT3": wfModMusicSRT3,
       "wfModMusicSRT4": wfModMusicSRT4,
       "wfModClrQ1Reset": wfModClrQ1Reset,
       "wfModClrQ2Reset": wfModClrQ2Reset,
       "wfModQ1Dram": wfModQ1Dram,
       "wfModQ2Dram": wfModQ2Dram,
       "wfModQ1DPram": wfModQ1DPram,
       "wfModQ2DPram": wfModQ2DPram,
       "wfModQ1StickyBit": wfModQ1StickyBit,
       "wfModQ2StickyBit": wfModQ2StickyBit,
       "wfModQ1Int7": wfModQ1Int7,
       "wfModQ2Int7": wfModQ2Int7,
       "wfModApplyQ1Reset": wfModApplyQ1Reset,
       "wfModApplyQ2Reset": wfModApplyQ2Reset}
)
