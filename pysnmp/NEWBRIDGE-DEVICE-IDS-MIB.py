# SNMP MIB module (NEWBRIDGE-DEVICE-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEWBRIDGE-DEVICE-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:21 2024
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

(nncDeviceIDs,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncDeviceIDs")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncStandalone_ObjectIdentity = ObjectIdentity
nncStandalone = _NncStandalone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1)
)
_Nnc8230_ObjectIdentity = ObjectIdentity
nnc8230 = _Nnc8230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 1)
)
_Nnc3604_ObjectIdentity = ObjectIdentity
nnc3604 = _Nnc3604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 2)
)
_Nnc8231_ObjectIdentity = ObjectIdentity
nnc8231 = _Nnc8231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 3)
)
_Nnc8251_ObjectIdentity = ObjectIdentity
nnc8251 = _Nnc8251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 4)
)
_Nnc3601_ObjectIdentity = ObjectIdentity
nnc3601 = _Nnc3601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 5)
)
_NncWGS_ObjectIdentity = ObjectIdentity
nncWGS = _NncWGS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 6)
)
_NncYRidge_ObjectIdentity = ObjectIdentity
nncYRidge = _NncYRidge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 7)
)
_NncSystemManager_ObjectIdentity = ObjectIdentity
nncSystemManager = _NncSystemManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 8)
)
_NncRouteServer_ObjectIdentity = ObjectIdentity
nncRouteServer = _NncRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 9)
)
_Nnc36170_ObjectIdentity = ObjectIdentity
nnc36170 = _Nnc36170_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 10)
)
_Nnc36150_ObjectIdentity = ObjectIdentity
nnc36150 = _Nnc36150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 11)
)
_NncNicSbus_ObjectIdentity = ObjectIdentity
nncNicSbus = _NncNicSbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 12)
)
_NncNicIr5x_ObjectIdentity = ObjectIdentity
nncNicIr5x = _NncNicIr5x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 13)
)
_Nnc48020_ObjectIdentity = ObjectIdentity
nnc48020 = _Nnc48020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 14)
)
_NncBRidge_ObjectIdentity = ObjectIdentity
nncBRidge = _NncBRidge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 15)
)
_NncELSU_ObjectIdentity = ObjectIdentity
nncELSU = _NncELSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 16)
)
_NncTRLSU_ObjectIdentity = ObjectIdentity
nncTRLSU = _NncTRLSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 17)
)
_Nnc3620_ObjectIdentity = ObjectIdentity
nnc3620 = _Nnc3620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 18)
)
_Nnc3624_ObjectIdentity = ObjectIdentity
nnc3624 = _Nnc3624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 19)
)
_NncOrangeRi_ObjectIdentity = ObjectIdentity
nncOrangeRi = _NncOrangeRi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 20)
)
_NncRedRidge_ObjectIdentity = ObjectIdentity
nncRedRidge = _NncRedRidge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 21)
)
_Nnc38010_ObjectIdentity = ObjectIdentity
nnc38010 = _Nnc38010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 22)
)
_NncNicPci_ObjectIdentity = ObjectIdentity
nncNicPci = _NncNicPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 23)
)
_Nnc10BFLRid_ObjectIdentity = ObjectIdentity
nnc10BFLRid = _Nnc10BFLRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 24)
)
_NncXcellys_ObjectIdentity = ObjectIdentity
nncXcellys = _NncXcellys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 25)
)
_NncCampusSwitch_ObjectIdentity = ObjectIdentity
nncCampusSwitch = _NncCampusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 26)
)
_NncIntegral_ObjectIdentity = ObjectIdentity
nncIntegral = _NncIntegral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 2)
)
_NncITB_ObjectIdentity = ObjectIdentity
nncITB = _NncITB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWBRIDGE-DEVICE-IDS-MIB",
    **{"nncStandalone": nncStandalone,
       "nnc8230": nnc8230,
       "nnc3604": nnc3604,
       "nnc8231": nnc8231,
       "nnc8251": nnc8251,
       "nnc3601": nnc3601,
       "nncWGS": nncWGS,
       "nncYRidge": nncYRidge,
       "nncSystemManager": nncSystemManager,
       "nncRouteServer": nncRouteServer,
       "nnc36170": nnc36170,
       "nnc36150": nnc36150,
       "nncNicSbus": nncNicSbus,
       "nncNicIr5x": nncNicIr5x,
       "nnc48020": nnc48020,
       "nncBRidge": nncBRidge,
       "nncELSU": nncELSU,
       "nncTRLSU": nncTRLSU,
       "nnc3620": nnc3620,
       "nnc3624": nnc3624,
       "nncOrangeRi": nncOrangeRi,
       "nncRedRidge": nncRedRidge,
       "nnc38010": nnc38010,
       "nncNicPci": nncNicPci,
       "nnc10BFLRid": nnc10BFLRid,
       "nncXcellys": nncXcellys,
       "nncCampusSwitch": nncCampusSwitch,
       "nncIntegral": nncIntegral,
       "nncITB": nncITB}
)
