# SNMP MIB module (NEXANS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEXANS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:23 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NexansANS_ObjectIdentity = ObjectIdentity
nexansANS = _NexansANS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1)
)
_BmSwitch_ObjectIdentity = ObjectIdentity
bmSwitch = _BmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3)
)
_FiberSwitch100Bm_ObjectIdentity = ObjectIdentity
fiberSwitch100Bm = _FiberSwitch100Bm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 1)
)
_CopperSwitch100Bm_ObjectIdentity = ObjectIdentity
copperSwitch100Bm = _CopperSwitch100Bm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 2)
)
_FiberSwitch100BmADesk_ObjectIdentity = ObjectIdentity
fiberSwitch100BmADesk = _FiberSwitch100BmADesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 3)
)
_CopperSwitch100BmADesk_ObjectIdentity = ObjectIdentity
copperSwitch100BmADesk = _CopperSwitch100BmADesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 4)
)
_FiberSwitch100BmA_ObjectIdentity = ObjectIdentity
fiberSwitch100BmA = _FiberSwitch100BmA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 5)
)
_CopperSwitch100BmA_ObjectIdentity = ObjectIdentity
copperSwitch100BmA = _CopperSwitch100BmA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 6)
)
_FiberSwitch100BmPlus_ObjectIdentity = ObjectIdentity
fiberSwitch100BmPlus = _FiberSwitch100BmPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 7)
)
_CopperSwitch100BmPlus_ObjectIdentity = ObjectIdentity
copperSwitch100BmPlus = _CopperSwitch100BmPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 8)
)
_FiberSwitch100BmPlusDesk_ObjectIdentity = ObjectIdentity
fiberSwitch100BmPlusDesk = _FiberSwitch100BmPlusDesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 9)
)
_CopperSwitch100BmPlusDesk_ObjectIdentity = ObjectIdentity
copperSwitch100BmPlusDesk = _CopperSwitch100BmPlusDesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 10)
)
_DualSwitch100BmPlusDeskFibFib_ObjectIdentity = ObjectIdentity
dualSwitch100BmPlusDeskFibFib = _DualSwitch100BmPlusDeskFibFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 11)
)
_DualSwitch100BmPlusDeskCopCop_ObjectIdentity = ObjectIdentity
dualSwitch100BmPlusDeskCopCop = _DualSwitch100BmPlusDeskCopCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 12)
)
_DualSwitch100BmPlusDeskCopFib_ObjectIdentity = ObjectIdentity
dualSwitch100BmPlusDeskCopFib = _DualSwitch100BmPlusDeskCopFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 13)
)
_FiberSwitch100BmPlusDeskVersA_ObjectIdentity = ObjectIdentity
fiberSwitch100BmPlusDeskVersA = _FiberSwitch100BmPlusDeskVersA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 14)
)
_CopperSwitch100BmPlusDeskVersA_ObjectIdentity = ObjectIdentity
copperSwitch100BmPlusDeskVersA = _CopperSwitch100BmPlusDeskVersA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 15)
)
_FiberSwitchM100Bm_ObjectIdentity = ObjectIdentity
fiberSwitchM100Bm = _FiberSwitchM100Bm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 16)
)
_CopperSwitchM100Bm_ObjectIdentity = ObjectIdentity
copperSwitchM100Bm = _CopperSwitchM100Bm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 17)
)
_FiberSwitch100BmPlusDeskVersC_ObjectIdentity = ObjectIdentity
fiberSwitch100BmPlusDeskVersC = _FiberSwitch100BmPlusDeskVersC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 18)
)
_CopperSwitch100BmPlusDeskVersC_ObjectIdentity = ObjectIdentity
copperSwitch100BmPlusDeskVersC = _CopperSwitch100BmPlusDeskVersC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 19)
)
_FiberSwitch1000BmPlus_ObjectIdentity = ObjectIdentity
fiberSwitch1000BmPlus = _FiberSwitch1000BmPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 20)
)
_DualSwitch1000BmPlusFibFib_ObjectIdentity = ObjectIdentity
dualSwitch1000BmPlusFibFib = _DualSwitch1000BmPlusFibFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 21)
)
_DualSwitch1000BmPlusDeskFibFib_ObjectIdentity = ObjectIdentity
dualSwitch1000BmPlusDeskFibFib = _DualSwitch1000BmPlusDeskFibFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 22)
)
_DualSwitch1000BmPlusCopFib_ObjectIdentity = ObjectIdentity
dualSwitch1000BmPlusCopFib = _DualSwitch1000BmPlusCopFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 23)
)
_DualSwitch1000BmPlusCopCop_ObjectIdentity = ObjectIdentity
dualSwitch1000BmPlusCopCop = _DualSwitch1000BmPlusCopCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 24)
)
_CopperSwitch1000BmPlus_ObjectIdentity = ObjectIdentity
copperSwitch1000BmPlus = _CopperSwitch1000BmPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 25)
)
_GigaSwitchG541Desk_ObjectIdentity = ObjectIdentity
gigaSwitchG541Desk = _GigaSwitchG541Desk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 27)
)
_GigaSwitchG542SfpDesk_ObjectIdentity = ObjectIdentity
gigaSwitchG542SfpDesk = _GigaSwitchG542SfpDesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 28)
)
_ISwitch740CopCop_ObjectIdentity = ObjectIdentity
iSwitch740CopCop = _ISwitch740CopCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 30)
)
_ISwitch741CopFib_ObjectIdentity = ObjectIdentity
iSwitch741CopFib = _ISwitch741CopFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 31)
)
_ISwitch742FibFib_ObjectIdentity = ObjectIdentity
iSwitch742FibFib = _ISwitch742FibFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 32)
)
_ISwitch1042FibFib_ObjectIdentity = ObjectIdentity
iSwitch1042FibFib = _ISwitch1042FibFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 33)
)
_ISwitch1043_ObjectIdentity = ObjectIdentity
iSwitch1043 = _ISwitch1043_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 34)
)
_ISwitch742SfpSfp_ObjectIdentity = ObjectIdentity
iSwitch742SfpSfp = _ISwitch742SfpSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 35)
)
_ISwitch1043Sfp3Vi_ObjectIdentity = ObjectIdentity
iSwitch1043Sfp3Vi = _ISwitch1043Sfp3Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 36)
)
_IGigaSwitch541_ObjectIdentity = ObjectIdentity
iGigaSwitch541 = _IGigaSwitch541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 37)
)
_IGigaSwitch542Sfp2Vi_ObjectIdentity = ObjectIdentity
iGigaSwitch542Sfp2Vi = _IGigaSwitch542Sfp2Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 38)
)
_IGigaSwitch1604_ObjectIdentity = ObjectIdentity
iGigaSwitch1604 = _IGigaSwitch1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 40)
)
_IGigaSwitch1608_ObjectIdentity = ObjectIdentity
iGigaSwitch1608 = _IGigaSwitch1608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 41)
)
_IGigaSwitch1612_ObjectIdentity = ObjectIdentity
iGigaSwitch1612 = _IGigaSwitch1612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 42)
)
_GigaSwitchBmFib_ObjectIdentity = ObjectIdentity
gigaSwitchBmFib = _GigaSwitchBmFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 50)
)
_GigaSwitchBmCop_ObjectIdentity = ObjectIdentity
gigaSwitchBmCop = _GigaSwitchBmCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 51)
)
_GigaSwitchV2Fib_ObjectIdentity = ObjectIdentity
gigaSwitchV2Fib = _GigaSwitchV2Fib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 52)
)
_GigaSwitchV2CopFib_ObjectIdentity = ObjectIdentity
gigaSwitchV2CopFib = _GigaSwitchV2CopFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 53)
)
_GigaSwitchV2CopCop_ObjectIdentity = ObjectIdentity
gigaSwitchV2CopCop = _GigaSwitchV2CopCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 54)
)
_GigaSwitchV2SfpFib_ObjectIdentity = ObjectIdentity
gigaSwitchV2SfpFib = _GigaSwitchV2SfpFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 55)
)
_GigaSwitchV2Cop_ObjectIdentity = ObjectIdentity
gigaSwitchV2Cop = _GigaSwitchV2Cop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 56)
)
_GigaSwitchV3FibTp_ObjectIdentity = ObjectIdentity
gigaSwitchV3FibTp = _GigaSwitchV3FibTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 60)
)
_GigaSwitchV3SfpTp_ObjectIdentity = ObjectIdentity
gigaSwitchV3SfpTp = _GigaSwitchV3SfpTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 61)
)
_GigaSwitchV3d2SfpTp_ObjectIdentity = ObjectIdentity
gigaSwitchV3d2SfpTp = _GigaSwitchV3d2SfpTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 62)
)
_GigaSwitchV3d2SfpSfp_ObjectIdentity = ObjectIdentity
gigaSwitchV3d2SfpSfp = _GigaSwitchV3d2SfpSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 63)
)
_GigaSwitchV3d2Fib_ObjectIdentity = ObjectIdentity
gigaSwitchV3d2Fib = _GigaSwitchV3d2Fib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 64)
)
_FiberSwitch1000BmV3_ObjectIdentity = ObjectIdentity
fiberSwitch1000BmV3 = _FiberSwitch1000BmV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 66)
)
_FiberSwitch100BmV3_ObjectIdentity = ObjectIdentity
fiberSwitch100BmV3 = _FiberSwitch100BmV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 67)
)
_GigaSwitch641DeskSfpTp_ObjectIdentity = ObjectIdentity
gigaSwitch641DeskSfpTp = _GigaSwitch641DeskSfpTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 70)
)
_GigaSwitch642DeskSfpSfp_ObjectIdentity = ObjectIdentity
gigaSwitch642DeskSfpSfp = _GigaSwitch642DeskSfpSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 1, 3, 71)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEXANS-MIB",
    **{"nexansANS": nexansANS,
       "products": products,
       "bmSwitch": bmSwitch,
       "fiberSwitch100Bm": fiberSwitch100Bm,
       "copperSwitch100Bm": copperSwitch100Bm,
       "fiberSwitch100BmADesk": fiberSwitch100BmADesk,
       "copperSwitch100BmADesk": copperSwitch100BmADesk,
       "fiberSwitch100BmA": fiberSwitch100BmA,
       "copperSwitch100BmA": copperSwitch100BmA,
       "fiberSwitch100BmPlus": fiberSwitch100BmPlus,
       "copperSwitch100BmPlus": copperSwitch100BmPlus,
       "fiberSwitch100BmPlusDesk": fiberSwitch100BmPlusDesk,
       "copperSwitch100BmPlusDesk": copperSwitch100BmPlusDesk,
       "dualSwitch100BmPlusDeskFibFib": dualSwitch100BmPlusDeskFibFib,
       "dualSwitch100BmPlusDeskCopCop": dualSwitch100BmPlusDeskCopCop,
       "dualSwitch100BmPlusDeskCopFib": dualSwitch100BmPlusDeskCopFib,
       "fiberSwitch100BmPlusDeskVersA": fiberSwitch100BmPlusDeskVersA,
       "copperSwitch100BmPlusDeskVersA": copperSwitch100BmPlusDeskVersA,
       "fiberSwitchM100Bm": fiberSwitchM100Bm,
       "copperSwitchM100Bm": copperSwitchM100Bm,
       "fiberSwitch100BmPlusDeskVersC": fiberSwitch100BmPlusDeskVersC,
       "copperSwitch100BmPlusDeskVersC": copperSwitch100BmPlusDeskVersC,
       "fiberSwitch1000BmPlus": fiberSwitch1000BmPlus,
       "dualSwitch1000BmPlusFibFib": dualSwitch1000BmPlusFibFib,
       "dualSwitch1000BmPlusDeskFibFib": dualSwitch1000BmPlusDeskFibFib,
       "dualSwitch1000BmPlusCopFib": dualSwitch1000BmPlusCopFib,
       "dualSwitch1000BmPlusCopCop": dualSwitch1000BmPlusCopCop,
       "copperSwitch1000BmPlus": copperSwitch1000BmPlus,
       "gigaSwitchG541Desk": gigaSwitchG541Desk,
       "gigaSwitchG542SfpDesk": gigaSwitchG542SfpDesk,
       "iSwitch740CopCop": iSwitch740CopCop,
       "iSwitch741CopFib": iSwitch741CopFib,
       "iSwitch742FibFib": iSwitch742FibFib,
       "iSwitch1042FibFib": iSwitch1042FibFib,
       "iSwitch1043": iSwitch1043,
       "iSwitch742SfpSfp": iSwitch742SfpSfp,
       "iSwitch1043Sfp3Vi": iSwitch1043Sfp3Vi,
       "iGigaSwitch541": iGigaSwitch541,
       "iGigaSwitch542Sfp2Vi": iGigaSwitch542Sfp2Vi,
       "iGigaSwitch1604": iGigaSwitch1604,
       "iGigaSwitch1608": iGigaSwitch1608,
       "iGigaSwitch1612": iGigaSwitch1612,
       "gigaSwitchBmFib": gigaSwitchBmFib,
       "gigaSwitchBmCop": gigaSwitchBmCop,
       "gigaSwitchV2Fib": gigaSwitchV2Fib,
       "gigaSwitchV2CopFib": gigaSwitchV2CopFib,
       "gigaSwitchV2CopCop": gigaSwitchV2CopCop,
       "gigaSwitchV2SfpFib": gigaSwitchV2SfpFib,
       "gigaSwitchV2Cop": gigaSwitchV2Cop,
       "gigaSwitchV3FibTp": gigaSwitchV3FibTp,
       "gigaSwitchV3SfpTp": gigaSwitchV3SfpTp,
       "gigaSwitchV3d2SfpTp": gigaSwitchV3d2SfpTp,
       "gigaSwitchV3d2SfpSfp": gigaSwitchV3d2SfpSfp,
       "gigaSwitchV3d2Fib": gigaSwitchV3d2Fib,
       "fiberSwitch1000BmV3": fiberSwitch1000BmV3,
       "fiberSwitch100BmV3": fiberSwitch100BmV3,
       "gigaSwitch641DeskSfpTp": gigaSwitch641DeskSfpTp,
       "gigaSwitch642DeskSfpSfp": gigaSwitch642DeskSfpSfp}
)
