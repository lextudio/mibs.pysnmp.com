# SNMP MIB module (ASKEY-DSLAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASKEY-DSLAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:48 2024
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

askey = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3646)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AskeyVendorTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              458759,
              458762,
              458763,
              458764,
              458765,
              458767,
              458768,
              458769,
              458770,
              458771,
              458772,
              458773,
              458774)
        )
    )
    namedValues = NamedValues(
        *(("alarmRelayModule", 17),
          ("alarmRelayPort", 18),
          ("am0021AdslModule", 458763),
          ("am0021AdslPort", 458767),
          ("am0021AlarmRelayModule", 458769),
          ("am0021AlarmRelayPort", 458770),
          ("am0021Chassis", 458759),
          ("am0021CpuModuleX2GE", 458762),
          ("am0021CpuModuleX4GE", 458774),
          ("am0021FanModule", 458765),
          ("am0021GePort", 458768),
          ("am0021PowerModule", 458764),
          ("am0021ShdslModule", 458772),
          ("am0021ShdslPort", 458773),
          ("am0021VdslModule", 458771),
          ("am0031AdslModule", 11),
          ("am0031BackPlane", 4),
          ("am0031Chassis", 3),
          ("am0031CpuModule", 10),
          ("am0031FanModule", 13),
          ("am0031PowerModule", 12),
          ("am0031ShdslModule", 20),
          ("am0031ShdslPort", 21),
          ("am0031VdslModule", 19),
          ("bcm6430fAdslPort", 15),
          ("cpuSlot", 6),
          ("fanSlot", 9),
          ("gePort", 16),
          ("genericAdslPort", 14),
          ("genericEmptySlot", 5),
          ("lineCardSlot", 7),
          ("noEntity", 1),
          ("other", 2),
          ("powerSlot", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Asd300_ObjectIdentity = ObjectIdentity
asd300 = _Asd300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300)
)
_IpDslam_ObjectIdentity = ObjectIdentity
ipDslam = _IpDslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2)
)
_Swv011_ObjectIdentity = ObjectIdentity
swv011 = _Swv011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 1)
)
_Swt011_ObjectIdentity = ObjectIdentity
swt011 = _Swt011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 2)
)
_Swv031_ObjectIdentity = ObjectIdentity
swv031 = _Swv031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 3)
)
_Swf011_ObjectIdentity = ObjectIdentity
swf011 = _Swf011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 4)
)
_Swt012_ObjectIdentity = ObjectIdentity
swt012 = _Swt012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 5)
)
_Am0031_ObjectIdentity = ObjectIdentity
am0031 = _Am0031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 6)
)
_Am0021_ObjectIdentity = ObjectIdentity
am0021 = _Am0021_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 7)
)
_Ama1011_ObjectIdentity = ObjectIdentity
ama1011 = _Ama1011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 8)
)
_Ams1011_ObjectIdentity = ObjectIdentity
ams1011 = _Ams1011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 9)
)
_UnDefinedDevice_ObjectIdentity = ObjectIdentity
unDefinedDevice = _UnDefinedDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 300, 999)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASKEY-DSLAM-MIB",
    **{"AskeyVendorTypeEnum": AskeyVendorTypeEnum,
       "askey": askey,
       "asd300": asd300,
       "ipDslam": ipDslam,
       "swv011": swv011,
       "swt011": swt011,
       "swv031": swv031,
       "swf011": swf011,
       "swt012": swt012,
       "am0031": am0031,
       "am0021": am0021,
       "ama1011": ama1011,
       "ams1011": ams1011,
       "unDefinedDevice": unDefinedDevice}
)
