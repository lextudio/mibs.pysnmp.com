# SNMP MIB module (WHISP-GLOBAL-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-GLOBAL-REG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:51 2024
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

whispGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mot_ObjectIdentity = ObjectIdentity
mot = _Mot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161)
)
_WhispRoot_ObjectIdentity = ObjectIdentity
whispRoot = _WhispRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19)
)
_WhispReg_ObjectIdentity = ObjectIdentity
whispReg = _WhispReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1)
)
_WhispModules_ObjectIdentity = ObjectIdentity
whispModules = _WhispModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1)
)
_WhispGeneric_ObjectIdentity = ObjectIdentity
whispGeneric = _WhispGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 2)
)
_WhispProducts_ObjectIdentity = ObjectIdentity
whispProducts = _WhispProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3)
)
_WhispAps_ObjectIdentity = ObjectIdentity
whispAps = _WhispAps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1)
)
_WhispSm_ObjectIdentity = ObjectIdentity
whispSm = _WhispSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2)
)
_WhispBox_ObjectIdentity = ObjectIdentity
whispBox = _WhispBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3)
)
_WhispCMM_ObjectIdentity = ObjectIdentity
whispCMM = _WhispCMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4)
)
_WhispPlv_ObjectIdentity = ObjectIdentity
whispPlv = _WhispPlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 5)
)
_WhispCMM4_ObjectIdentity = ObjectIdentity
whispCMM4 = _WhispCMM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6)
)
_WhispPlvModem_ObjectIdentity = ObjectIdentity
whispPlvModem = _WhispPlvModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7)
)
_WhispPlvGateway_ObjectIdentity = ObjectIdentity
whispPlvGateway = _WhispPlvGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8)
)
_WhispPlvRepeater_ObjectIdentity = ObjectIdentity
whispPlvRepeater = _WhispPlvRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 9)
)
_WhispPlvBridge_ObjectIdentity = ObjectIdentity
whispPlvBridge = _WhispPlvBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 10)
)
_CanopySnmpAgent_ObjectIdentity = ObjectIdentity
canopySnmpAgent = _CanopySnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 250)
)
_Ucos_ObjectIdentity = ObjectIdentity
ucos = _Ucos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 250, 256)
)
_Prizm_ObjectIdentity = ObjectIdentity
prizm = _Prizm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1000)
)
_PrizmSnmpAgent_ObjectIdentity = ObjectIdentity
prizmSnmpAgent = _PrizmSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1250)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-GLOBAL-REG-MIB",
    **{"mot": mot,
       "whispRoot": whispRoot,
       "whispReg": whispReg,
       "whispModules": whispModules,
       "whispGlobalRegModule": whispGlobalRegModule,
       "whispGeneric": whispGeneric,
       "whispProducts": whispProducts,
       "whispAps": whispAps,
       "whispSm": whispSm,
       "whispBox": whispBox,
       "whispCMM": whispCMM,
       "whispPlv": whispPlv,
       "whispCMM4": whispCMM4,
       "whispPlvModem": whispPlvModem,
       "whispPlvGateway": whispPlvGateway,
       "whispPlvRepeater": whispPlvRepeater,
       "whispPlvBridge": whispPlvBridge,
       "canopySnmpAgent": canopySnmpAgent,
       "ucos": ucos,
       "prizm": prizm,
       "prizmSnmpAgent": prizmSnmpAgent}
)
