# SNMP MIB module (IB-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:14 2024
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

infoblox = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779)
)
infoblox.setRevisions(
        ("2008-01-14 00:00",
         "2005-01-10 00:00",
         "2004-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IbString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class IbNode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class IbIpAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class IbIpv6Addr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )



# MIB Managed Objects in the order of their OIDs

_InfobloxProducts_ObjectIdentity = ObjectIdentity
infobloxProducts = _InfobloxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1)
)
_IbDefault_ObjectIdentity = ObjectIdentity
ibDefault = _IbDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1000)
)
_IbRsp2_ObjectIdentity = ObjectIdentity
ibRsp2 = _IbRsp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1001)
)
_IbCisco_ObjectIdentity = ObjectIdentity
ibCisco = _IbCisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1002)
)
_IbVm_ObjectIdentity = ObjectIdentity
ibVm = _IbVm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1003)
)
_IbVnios_ObjectIdentity = ObjectIdentity
ibVnios = _IbVnios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1004)
)
_Ib1000_ObjectIdentity = ObjectIdentity
ib1000 = _Ib1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1101)
)
_Ib1200_ObjectIdentity = ObjectIdentity
ib1200 = _Ib1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1102)
)
_Ib500_ObjectIdentity = ObjectIdentity
ib500 = _Ib500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1103)
)
_Ib550_ObjectIdentity = ObjectIdentity
ib550 = _Ib550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1201)
)
_Ib1050_ObjectIdentity = ObjectIdentity
ib1050 = _Ib1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1202)
)
_Ib1550_ObjectIdentity = ObjectIdentity
ib1550 = _Ib1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1203)
)
_Ib1552_ObjectIdentity = ObjectIdentity
ib1552 = _Ib1552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1204)
)
_Ib2000_ObjectIdentity = ObjectIdentity
ib2000 = _Ib2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1205)
)
_Ib250_ObjectIdentity = ObjectIdentity
ib250 = _Ib250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1206)
)
_Ib1220_ObjectIdentity = ObjectIdentity
ib1220 = _Ib1220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1207)
)
_Ib550a_ObjectIdentity = ObjectIdentity
ib550a = _Ib550a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1301)
)
_Ib1050a_ObjectIdentity = ObjectIdentity
ib1050a = _Ib1050a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1302)
)
_Ib1550a_ObjectIdentity = ObjectIdentity
ib1550a = _Ib1550a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1303)
)
_Ib1552a_ObjectIdentity = ObjectIdentity
ib1552a = _Ib1552a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1304)
)
_Ib1852a_ObjectIdentity = ObjectIdentity
ib1852a = _Ib1852a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1305)
)
_Ib250a_ObjectIdentity = ObjectIdentity
ib250a = _Ib250a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1306)
)
_Ib2000a_ObjectIdentity = ObjectIdentity
ib2000a = _Ib2000a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1307)
)
_Ib4000_ObjectIdentity = ObjectIdentity
ib4000 = _Ib4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1420)
)
_Ib4010_ObjectIdentity = ObjectIdentity
ib4010 = _Ib4010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1421)
)
_Ib4020_ObjectIdentity = ObjectIdentity
ib4020 = _Ib4020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1422)
)
_IbSNMP_ObjectIdentity = ObjectIdentity
ibSNMP = _IbSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3)
)
_IbProduct_ObjectIdentity = ObjectIdentity
ibProduct = _IbProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1)
)
_IbOne_ObjectIdentity = ObjectIdentity
ibOne = _IbOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1)
)
_IbTrapOne_ObjectIdentity = ObjectIdentity
ibTrapOne = _IbTrapOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1)
)
_IbPlatformOne_ObjectIdentity = ObjectIdentity
ibPlatformOne = _IbPlatformOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2)
)
_IbDNSOne_ObjectIdentity = ObjectIdentity
ibDNSOne = _IbDNSOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3)
)
_IbDHCPOne_ObjectIdentity = ObjectIdentity
ibDHCPOne = _IbDHCPOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-SMI-MIB",
    **{"IbString": IbString,
       "IbNode": IbNode,
       "IbIpAddr": IbIpAddr,
       "IbIpv6Addr": IbIpv6Addr,
       "infoblox": infoblox,
       "infobloxProducts": infobloxProducts,
       "ibDefault": ibDefault,
       "ibRsp2": ibRsp2,
       "ibCisco": ibCisco,
       "ibVm": ibVm,
       "ibVnios": ibVnios,
       "ib1000": ib1000,
       "ib1200": ib1200,
       "ib500": ib500,
       "ib550": ib550,
       "ib1050": ib1050,
       "ib1550": ib1550,
       "ib1552": ib1552,
       "ib2000": ib2000,
       "ib250": ib250,
       "ib1220": ib1220,
       "ib550a": ib550a,
       "ib1050a": ib1050a,
       "ib1550a": ib1550a,
       "ib1552a": ib1552a,
       "ib1852a": ib1852a,
       "ib250a": ib250a,
       "ib2000a": ib2000a,
       "ib4000": ib4000,
       "ib4010": ib4010,
       "ib4020": ib4020,
       "ibSNMP": ibSNMP,
       "ibProduct": ibProduct,
       "ibOne": ibOne,
       "ibTrapOne": ibTrapOne,
       "ibPlatformOne": ibPlatformOne,
       "ibDNSOne": ibDNSOne,
       "ibDHCPOne": ibDHCPOne}
)
