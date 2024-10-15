# SNMP MIB module (BLUECOAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:20 2024
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

blueCoat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417)
)
blueCoat.setRevisions(
        ("2015-04-24 03:00",
         "2014-03-04 03:00",
         "2013-12-12 03:00",
         "2013-11-12 03:00",
         "2013-09-24 03:00",
         "2013-06-27 03:00",
         "2011-04-15 03:00",
         "2011-04-01 03:00",
         "2007-11-05 03:00",
         "2002-08-28 03:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1)
)
_Sg1000_ObjectIdentity = ObjectIdentity
sg1000 = _Sg1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 1)
)
_Sg100_ObjectIdentity = ObjectIdentity
sg100 = _Sg100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 2)
)
_Sg500_ObjectIdentity = ObjectIdentity
sg500 = _Sg500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 3)
)
_Sg2000_ObjectIdentity = ObjectIdentity
sg2000 = _Sg2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 4)
)
_Sg5000_ObjectIdentity = ObjectIdentity
sg5000 = _Sg5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 5)
)
_Sg500A_ObjectIdentity = ObjectIdentity
sg500A = _Sg500A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 6)
)
_Sg3000_ObjectIdentity = ObjectIdentity
sg3000 = _Sg3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 7)
)
_Sg5x5_ObjectIdentity = ObjectIdentity
sg5x5 = _Sg5x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 8)
)
_Sg110_ObjectIdentity = ObjectIdentity
sg110 = _Sg110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 9)
)
_Sg6000_ObjectIdentity = ObjectIdentity
sg6000 = _Sg6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 11)
)
_Sg610_ObjectIdentity = ObjectIdentity
sg610 = _Sg610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 12)
)
_Sg6x5_ObjectIdentity = ObjectIdentity
sg6x5 = _Sg6x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 13)
)
_Sg3000s_ObjectIdentity = ObjectIdentity
sg3000s = _Sg3000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 14)
)
_Sg5000s_ObjectIdentity = ObjectIdentity
sg5000s = _Sg5000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 15)
)
_Sg7x5_ObjectIdentity = ObjectIdentity
sg7x5 = _Sg7x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 16)
)
_Sg710_ObjectIdentity = ObjectIdentity
sg710 = _Sg710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 17)
)
_Sg7000_ObjectIdentity = ObjectIdentity
sg7000 = _Sg7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 18)
)
_Sg611_ObjectIdentity = ObjectIdentity
sg611 = _Sg611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 19)
)
_Sg800_ObjectIdentity = ObjectIdentity
sg800 = _Sg800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 20)
)
_Sg400_ObjectIdentity = ObjectIdentity
sg400 = _Sg400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 22)
)
_Sg8000_ObjectIdentity = ObjectIdentity
sg8000 = _Sg8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 23)
)
_Sg200_ObjectIdentity = ObjectIdentity
sg200 = _Sg200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 24)
)
_Sg810_ObjectIdentity = ObjectIdentity
sg810 = _Sg810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 25)
)
_Sg210_ObjectIdentity = ObjectIdentity
sg210 = _Sg210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 26)
)
_Sg510_ObjectIdentity = ObjectIdentity
sg510 = _Sg510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 27)
)
_Sg8100_ObjectIdentity = ObjectIdentity
sg8100 = _Sg8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 28)
)
_Sg9000_ObjectIdentity = ObjectIdentity
sg9000 = _Sg9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 29)
)
_Sgvmwareesx_ObjectIdentity = ObjectIdentity
sgvmwareesx = _Sgvmwareesx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 30)
)
_Sg600_ObjectIdentity = ObjectIdentity
sg600 = _Sg600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 31)
)
_Sg300_ObjectIdentity = ObjectIdentity
sg300 = _Sg300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 32)
)
_Sg900_ObjectIdentity = ObjectIdentity
sg900 = _Sg900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 34)
)
_Sgs500_ObjectIdentity = ObjectIdentity
sgs500 = _Sgs500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 36)
)
_Sgs400_ObjectIdentity = ObjectIdentity
sgs400 = _Sgs400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 37)
)
_Sgs200_ObjectIdentity = ObjectIdentity
sgs200 = _Sgs200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 38)
)
_Sghyperv_ObjectIdentity = ObjectIdentity
sghyperv = _Sghyperv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 42)
)
_Director_ObjectIdentity = ObjectIdentity
director = _Director_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 2)
)
_Sgme710_ObjectIdentity = ObjectIdentity
sgme710 = _Sgme710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 2, 1)
)
_Sgme800_ObjectIdentity = ObjectIdentity
sgme800 = _Sgme800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 2, 2)
)
_Av_ObjectIdentity = ObjectIdentity
av = _Av_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3)
)
_Av2000_ObjectIdentity = ObjectIdentity
av2000 = _Av2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 1)
)
_Av400_ObjectIdentity = ObjectIdentity
av400 = _Av400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 2)
)
_Av810_ObjectIdentity = ObjectIdentity
av810 = _Av810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 3)
)
_Av510_ObjectIdentity = ObjectIdentity
av510 = _Av510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 4)
)
_Av1400_ObjectIdentity = ObjectIdentity
av1400 = _Av1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 5)
)
_Av2400_ObjectIdentity = ObjectIdentity
av2400 = _Av2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 6)
)
_Av1200_ObjectIdentity = ObjectIdentity
av1200 = _Av1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 7)
)
_Av210_ObjectIdentity = ObjectIdentity
av210 = _Av210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 3, 8)
)
_Cas_ObjectIdentity = ObjectIdentity
cas = _Cas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 4)
)
_Cass400_ObjectIdentity = ObjectIdentity
cass400 = _Cass400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 4, 1)
)
_Cass500_ObjectIdentity = ObjectIdentity
cass500 = _Cass500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 4, 2)
)
_Cass200_ObjectIdentity = ObjectIdentity
cass200 = _Cass200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 4, 3)
)
_Sslv_ObjectIdentity = ObjectIdentity
sslv = _Sslv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 5)
)
_Sslv800_ObjectIdentity = ObjectIdentity
sslv800 = _Sslv800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 5, 1)
)
_Sslv1800_ObjectIdentity = ObjectIdentity
sslv1800 = _Sslv1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 5, 2)
)
_Sslv2800_ObjectIdentity = ObjectIdentity
sslv2800 = _Sslv2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 5, 3)
)
_Sslv3800_ObjectIdentity = ObjectIdentity
sslv3800 = _Sslv3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 5, 4)
)
_Asg_ObjectIdentity = ObjectIdentity
asg = _Asg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 6)
)
_Asgs500_ObjectIdentity = ObjectIdentity
asgs500 = _Asgs500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 6, 1)
)
_Asgs400_ObjectIdentity = ObjectIdentity
asgs400 = _Asgs400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 6, 2)
)
_Asgs200_ObjectIdentity = ObjectIdentity
asgs200 = _Asgs200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 6, 3)
)
_BlueCoatMgmt_ObjectIdentity = ObjectIdentity
blueCoatMgmt = _BlueCoatMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-MIB",
    **{"blueCoat": blueCoat,
       "products": products,
       "device": device,
       "sg1000": sg1000,
       "sg100": sg100,
       "sg500": sg500,
       "sg2000": sg2000,
       "sg5000": sg5000,
       "sg500A": sg500A,
       "sg3000": sg3000,
       "sg5x5": sg5x5,
       "sg110": sg110,
       "sg6000": sg6000,
       "sg610": sg610,
       "sg6x5": sg6x5,
       "sg3000s": sg3000s,
       "sg5000s": sg5000s,
       "sg7x5": sg7x5,
       "sg710": sg710,
       "sg7000": sg7000,
       "sg611": sg611,
       "sg800": sg800,
       "sg400": sg400,
       "sg8000": sg8000,
       "sg200": sg200,
       "sg810": sg810,
       "sg210": sg210,
       "sg510": sg510,
       "sg8100": sg8100,
       "sg9000": sg9000,
       "sgvmwareesx": sgvmwareesx,
       "sg600": sg600,
       "sg300": sg300,
       "sg900": sg900,
       "sgs500": sgs500,
       "sgs400": sgs400,
       "sgs200": sgs200,
       "sghyperv": sghyperv,
       "director": director,
       "sgme710": sgme710,
       "sgme800": sgme800,
       "av": av,
       "av2000": av2000,
       "av400": av400,
       "av810": av810,
       "av510": av510,
       "av1400": av1400,
       "av2400": av2400,
       "av1200": av1200,
       "av210": av210,
       "cas": cas,
       "cass400": cass400,
       "cass500": cass500,
       "cass200": cass200,
       "sslv": sslv,
       "sslv800": sslv800,
       "sslv1800": sslv1800,
       "sslv2800": sslv2800,
       "sslv3800": sslv3800,
       "asg": asg,
       "asgs500": asgs500,
       "asgs400": asgs400,
       "asgs200": asgs200,
       "blueCoatMgmt": blueCoatMgmt}
)
