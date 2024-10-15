# SNMP MIB module (BROADCOM-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROADCOM-REF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:17 2024
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

(dellLan,
 dellLanExtension) = mibBuilder.importSymbols(
    "Dell-Vendor-MIB",
    "dellLan",
    "dellLanExtension")

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

lvl7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132)
)
lvl7.setRevisions(
        ("2013-04-12 00:00",
         "2013-03-27 00:00",
         "2011-04-14 00:00",
         "2003-11-21 00:00",
         "2003-02-06 12:00",
         "2013-07-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentPortMask(OctetString, TextualConvention):
    status = "current"
    displayHint = "255x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Dell6224Switch_ObjectIdentity = ObjectIdentity
dell6224Switch = _Dell6224Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3010)
)
_Dell6248Switch_ObjectIdentity = ObjectIdentity
dell6248Switch = _Dell6248Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3011)
)
_Dell6224PSwitch_ObjectIdentity = ObjectIdentity
dell6224PSwitch = _Dell6224PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3012)
)
_Dell6248PSwitch_ObjectIdentity = ObjectIdentity
dell6248PSwitch = _Dell6248PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3013)
)
_Dell6224FSwitch_ObjectIdentity = ObjectIdentity
dell6224FSwitch = _Dell6224FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3014)
)
_DellM6220Switch_ObjectIdentity = ObjectIdentity
dellM6220Switch = _DellM6220Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3015)
)
_DellM8024Switch_ObjectIdentity = ObjectIdentity
dellM8024Switch = _DellM8024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3022)
)
_Dell8024Switch_ObjectIdentity = ObjectIdentity
dell8024Switch = _Dell8024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3023)
)
_Dell8024FSwitch_ObjectIdentity = ObjectIdentity
dell8024FSwitch = _Dell8024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3024)
)
_DellM6384Switch_ObjectIdentity = ObjectIdentity
dellM6384Switch = _DellM6384Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3025)
)
_Dell7024Switch_ObjectIdentity = ObjectIdentity
dell7024Switch = _Dell7024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3034)
)
_Dell7048Switch_ObjectIdentity = ObjectIdentity
dell7048Switch = _Dell7048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3035)
)
_Dell7024PSwitch_ObjectIdentity = ObjectIdentity
dell7024PSwitch = _Dell7024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3036)
)
_Dell7048PSwitch_ObjectIdentity = ObjectIdentity
dell7048PSwitch = _Dell7048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3037)
)
_Dell7024FSwitch_ObjectIdentity = ObjectIdentity
dell7024FSwitch = _Dell7024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3038)
)
_Dell7048RSwitch_ObjectIdentity = ObjectIdentity
dell7048RSwitch = _Dell7048RSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3039)
)
_Dell7048RRASwitch_ObjectIdentity = ObjectIdentity
dell7048RRASwitch = _Dell7048RRASwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3040)
)
_DellM8024KSwitch_ObjectIdentity = ObjectIdentity
dellM8024KSwitch = _DellM8024KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3041)
)
_DellN4032Switch_ObjectIdentity = ObjectIdentity
dellN4032Switch = _DellN4032Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3042)
)
_DellN4032FSwitch_ObjectIdentity = ObjectIdentity
dellN4032FSwitch = _DellN4032FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3044)
)
_DellN4064Switch_ObjectIdentity = ObjectIdentity
dellN4064Switch = _DellN4064Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3045)
)
_DellN4064FSwitch_ObjectIdentity = ObjectIdentity
dellN4064FSwitch = _DellN4064FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3046)
)
_DellN2024Switch_ObjectIdentity = ObjectIdentity
dellN2024Switch = _DellN2024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3053)
)
_DellN2048Switch_ObjectIdentity = ObjectIdentity
dellN2048Switch = _DellN2048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3054)
)
_DellN2024PSwitch_ObjectIdentity = ObjectIdentity
dellN2024PSwitch = _DellN2024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3055)
)
_DellN2048PSwitch_ObjectIdentity = ObjectIdentity
dellN2048PSwitch = _DellN2048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3056)
)
_DellN3024Switch_ObjectIdentity = ObjectIdentity
dellN3024Switch = _DellN3024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3057)
)
_DellN3048Switch_ObjectIdentity = ObjectIdentity
dellN3048Switch = _DellN3048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3058)
)
_DellN3024PSwitch_ObjectIdentity = ObjectIdentity
dellN3024PSwitch = _DellN3024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3059)
)
_DellN3048PSwitch_ObjectIdentity = ObjectIdentity
dellN3048PSwitch = _DellN3048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3060)
)
_DellN3024FSwitch_ObjectIdentity = ObjectIdentity
dellN3024FSwitch = _DellN3024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3061)
)
_Lvl7Products_ObjectIdentity = ObjectIdentity
lvl7Products = _Lvl7Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1)
)
_FastPath_ObjectIdentity = ObjectIdentity
fastPath = _FastPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADCOM-REF-MIB",
    **{"AgentPortMask": AgentPortMask,
       "dell6224Switch": dell6224Switch,
       "dell6248Switch": dell6248Switch,
       "dell6224PSwitch": dell6224PSwitch,
       "dell6248PSwitch": dell6248PSwitch,
       "dell6224FSwitch": dell6224FSwitch,
       "dellM6220Switch": dellM6220Switch,
       "dellM8024Switch": dellM8024Switch,
       "dell8024Switch": dell8024Switch,
       "dell8024FSwitch": dell8024FSwitch,
       "dellM6384Switch": dellM6384Switch,
       "dell7024Switch": dell7024Switch,
       "dell7048Switch": dell7048Switch,
       "dell7024PSwitch": dell7024PSwitch,
       "dell7048PSwitch": dell7048PSwitch,
       "dell7024FSwitch": dell7024FSwitch,
       "dell7048RSwitch": dell7048RSwitch,
       "dell7048RRASwitch": dell7048RRASwitch,
       "dellM8024KSwitch": dellM8024KSwitch,
       "dellN4032Switch": dellN4032Switch,
       "dellN4032FSwitch": dellN4032FSwitch,
       "dellN4064Switch": dellN4064Switch,
       "dellN4064FSwitch": dellN4064FSwitch,
       "dellN2024Switch": dellN2024Switch,
       "dellN2048Switch": dellN2048Switch,
       "dellN2024PSwitch": dellN2024PSwitch,
       "dellN2048PSwitch": dellN2048PSwitch,
       "dellN3024Switch": dellN3024Switch,
       "dellN3048Switch": dellN3048Switch,
       "dellN3024PSwitch": dellN3024PSwitch,
       "dellN3048PSwitch": dellN3048PSwitch,
       "dellN3024FSwitch": dellN3024FSwitch,
       "lvl7": lvl7,
       "lvl7Products": lvl7Products,
       "fastPath": fastPath}
)
