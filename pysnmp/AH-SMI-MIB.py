# SNMP MIB module (AH-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AH-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:59 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

aerohive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26928)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AhString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AhNodeID(MacAddress, TextualConvention):
    status = "current"


class AhInterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ahPHYSICAL", 0),
          ("ahVIRTURAL", 1))
    )



class AhInterfaceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ahAccess", 1),
          ("ahBackhaul", 2),
          ("ahBridge", 3),
          ("ahNotUsed", 0))
    )



class AhMACProtocol(Integer32, TextualConvention):
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
        *(("ah11a", 0),
          ("ah11b", 1),
          ("ah11g", 2),
          ("ah11na", 3),
          ("ah11ng", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AhProduct_ObjectIdentity = ObjectIdentity
ahProduct = _AhProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1)
)
_AhAP_ObjectIdentity = ObjectIdentity
ahAP = _AhAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1)
)
_AhAPCommon_ObjectIdentity = ObjectIdentity
ahAPCommon = _AhAPCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1)
)
_AhAPTrap_ObjectIdentity = ObjectIdentity
ahAPTrap = _AhAPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1)
)
_AhAPInterface_ObjectIdentity = ObjectIdentity
ahAPInterface = _AhAPInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2)
)
_AhAPMRP_ObjectIdentity = ObjectIdentity
ahAPMRP = _AhAPMRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3)
)
_AhAPIDP_ObjectIdentity = ObjectIdentity
ahAPIDP = _AhAPIDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 4)
)
_AhAPHiveAP020_ag_ObjectIdentity = ObjectIdentity
ahAPHiveAP020_ag = _AhAPHiveAP020_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 2)
)
_AhAPHiveAP028_ag_ObjectIdentity = ObjectIdentity
ahAPHiveAP028_ag = _AhAPHiveAP028_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 3)
)
_AhAPHiveAP320_n_ObjectIdentity = ObjectIdentity
ahAPHiveAP320_n = _AhAPHiveAP320_n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 4)
)
_AhAPHiveAP340_n_ObjectIdentity = ObjectIdentity
ahAPHiveAP340_n = _AhAPHiveAP340_n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AH-SMI-MIB",
    **{"AhString": AhString,
       "AhNodeID": AhNodeID,
       "AhInterfaceType": AhInterfaceType,
       "AhInterfaceMode": AhInterfaceMode,
       "AhMACProtocol": AhMACProtocol,
       "aerohive": aerohive,
       "ahProduct": ahProduct,
       "ahAP": ahAP,
       "ahAPCommon": ahAPCommon,
       "ahAPTrap": ahAPTrap,
       "ahAPInterface": ahAPInterface,
       "ahAPMRP": ahAPMRP,
       "ahAPIDP": ahAPIDP,
       "ahAPHiveAP020-ag": ahAPHiveAP020_ag,
       "ahAPHiveAP028-ag": ahAPHiveAP028_ag,
       "ahAPHiveAP320-n": ahAPHiveAP320_n,
       "ahAPHiveAP340-n": ahAPHiveAP340_n}
)
