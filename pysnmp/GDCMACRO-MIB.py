# SNMP MIB module (GDCMACRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCMACRO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:29 2024
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



class SCinstance(Integer32):
    """Custom type SCinstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16842752,
              33619968,
              50397184,
              67174400,
              83951616,
              100728832,
              117506048,
              134283264,
              151060480,
              167837696,
              184614912,
              201392128,
              218169344,
              234946560,
              251723776,
              258500992,
              285278208,
              302055424,
              318832640,
              335609856,
              352387072,
              369164288,
              385941504,
              402718720,
              419495936,
              436273152,
              453050368,
              469827584,
              486604800,
              503382016,
              520159232,
              536936448)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 16842752),
          ("slot10", 167837696),
          ("slot11", 184614912),
          ("slot12", 201392128),
          ("slot13", 218169344),
          ("slot14", 234946560),
          ("slot15", 251723776),
          ("slot16", 258500992),
          ("slot17", 285278208),
          ("slot18", 302055424),
          ("slot19", 318832640),
          ("slot2", 33619968),
          ("slot20", 335609856),
          ("slot21", 352387072),
          ("slot22", 369164288),
          ("slot23", 385941504),
          ("slot24", 402718720),
          ("slot25", 419495936),
          ("slot26", 436273152),
          ("slot27", 453050368),
          ("slot28", 469827584),
          ("slot29", 486604800),
          ("slot3", 50397184),
          ("slot30", 503382016),
          ("slot31", 520159232),
          ("slot32", 536936448),
          ("slot4", 67174400),
          ("slot5", 83951616),
          ("slot6", 100728832),
          ("slot7", 117506048),
          ("slot8", 134283264),
          ("slot9", 151060480))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCMACRO-MIB",
    **{"SCinstance": SCinstance,
       "gdc": gdc}
)
