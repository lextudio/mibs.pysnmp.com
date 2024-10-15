# SNMP MIB module (FNC-COMMON-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNC-COMMON-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:15 2024
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

fnc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3861)
)
fnc.setRevisions(
        ("2004-01-28 15:00",
         "2003-10-06 15:00",
         "2003-08-12 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FncTraps_ObjectIdentity = ObjectIdentity
fncTraps = _FncTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 0)
)
_Fastlane_ObjectIdentity = ObjectIdentity
fastlane = _Fastlane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 1)
)
_Flash_ObjectIdentity = ObjectIdentity
flash = _Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 2)
)
_FlashBase_ObjectIdentity = ObjectIdentity
flashBase = _FlashBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 2, 1)
)
_Stm_ObjectIdentity = ObjectIdentity
stm = _Stm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 2, 1, 7)
)
_Sonet_ObjectIdentity = ObjectIdentity
sonet = _Sonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 2, 1, 7, 1)
)
_Flashwave_ObjectIdentity = ObjectIdentity
flashwave = _Flashwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3)
)
_FwCommon_ObjectIdentity = ObjectIdentity
fwCommon = _FwCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 1)
)
_Fw4020_ObjectIdentity = ObjectIdentity
fw4020 = _Fw4020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 4020)
)
_Fw4100_ObjectIdentity = ObjectIdentity
fw4100 = _Fw4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 4100)
)
_Fw4300_ObjectIdentity = ObjectIdentity
fw4300 = _Fw4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 4300)
)
_Fw4500_ObjectIdentity = ObjectIdentity
fw4500 = _Fw4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 4500)
)
_Fw7500_ObjectIdentity = ObjectIdentity
fw7500 = _Fw7500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 3, 7500)
)
_Netsmart_ObjectIdentity = ObjectIdentity
netsmart = _Netsmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNC-COMMON-SMI",
    **{"fnc": fnc,
       "fncTraps": fncTraps,
       "fastlane": fastlane,
       "flash": flash,
       "flashBase": flashBase,
       "stm": stm,
       "sonet": sonet,
       "flashwave": flashwave,
       "fwCommon": fwCommon,
       "fw4020": fw4020,
       "fw4100": fw4100,
       "fw4300": fw4300,
       "fw4500": fw4500,
       "fw7500": fw7500,
       "netsmart": netsmart}
)
