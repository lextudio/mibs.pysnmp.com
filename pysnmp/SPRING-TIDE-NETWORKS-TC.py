# SNMP MIB module (SPRING-TIDE-NETWORKS-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPRING-TIDE-NETWORKS-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:25 2024
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

(stnMibModules,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnMibModules")


# MODULE-IDENTITY

stnTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NSAPAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class CountryCode(OctetString, TextualConvention):
    status = "current"
    displayHint = "2a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class StnHardwareModuleType(Integer32, TextualConvention):
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
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("atmDS3-12", 20),
          ("atmOC12-MMF-1", 18),
          ("atmOC12-SMF-1", 17),
          ("atmOC3-MMF-4", 16),
          ("atmOC3-SMF-4", 15),
          ("cpm", 3),
          ("e100BT-4", 11),
          ("e100BT-8", 13),
          ("e100BT-FX-4", 12),
          ("e100BT-FX-8", 14),
          ("empty", 2),
          ("fan", 8),
          ("fan2", 25),
          ("fcc", 7),
          ("gigE-1-e100BT-4", 23),
          ("gigE-1-e100BT-FX-4", 24),
          ("midplane", 10),
          ("posOC12-SMF-2", 19),
          ("powersupply", 9),
          ("rim", 6),
          ("sfx-5G", 22),
          ("swfm-5G", 5),
          ("tsm", 4),
          ("tsm2", 21),
          ("unknown", 1))
    )



class StnHardwareSubModuleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("encryption", 3),
          ("unknown", 1))
    )



class StnModuleAdminStatus(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("booting", 4),
          ("down", 3),
          ("not-present", 2),
          ("testing", 5),
          ("unknown", 1),
          ("up-primary", 8),
          ("up-standalone", 6),
          ("up-standby", 7))
    )



class StnModuleOperStatus(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("booting", 4),
          ("down", 3),
          ("not-present", 2),
          ("testing", 5),
          ("unknown", 1),
          ("up-primary", 8),
          ("up-standalone", 6),
          ("up-standby", 7))
    )



class StnEngineAdminStatus(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("configured", 5),
          ("detected", 4),
          ("down", 3),
          ("not-present", 2),
          ("unknown", 1),
          ("up-primary", 8),
          ("up-standalone", 6),
          ("up-standby", 7))
    )



class StnEngineOperStatus(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("configured", 5),
          ("detected", 4),
          ("down", 3),
          ("not-present", 2),
          ("unknown", 1),
          ("up-primary", 8),
          ("up-standalone", 6),
          ("up-standby", 7))
    )



class StnLedStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("blink-green", 8),
          ("blink-orange", 11),
          ("blink-red", 10),
          ("blink-yellow", 9),
          ("green", 4),
          ("off", 2),
          ("on", 3),
          ("orange", 7),
          ("red", 6),
          ("unknown", 1),
          ("yellow", 5))
    )



class StnPowerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 3),
          ("present", 2),
          ("unknown", 1))
    )



class StnBatteryStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 3),
          ("ok", 2),
          ("unknown", 1))
    )



class StnFlashStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cannot-write", 5),
          ("full", 4),
          ("general-failure", 1),
          ("not-present", 3),
          ("ok", 2))
    )



class StnResourceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("low-memory", 3),
          ("no-buffers-available", 5),
          ("no-semaphores-available", 4),
          ("no-sockets-available", 6),
          ("ok", 2),
          ("unknown", 1))
    )



class StnUserFailureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authentication-failure", 1),
          ("authorization-failure", 2),
          ("resource-failure", 3))
    )



class StnConfigFailureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access-failure", 1),
          ("unexpected-change", 2))
    )



class StnDomainMapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapatm", 2),
          ("mapip", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    **{"NSAPAddress": NSAPAddress,
       "CountryCode": CountryCode,
       "StnHardwareModuleType": StnHardwareModuleType,
       "StnHardwareSubModuleType": StnHardwareSubModuleType,
       "StnModuleAdminStatus": StnModuleAdminStatus,
       "StnModuleOperStatus": StnModuleOperStatus,
       "StnEngineAdminStatus": StnEngineAdminStatus,
       "StnEngineOperStatus": StnEngineOperStatus,
       "StnLedStatus": StnLedStatus,
       "StnPowerStatus": StnPowerStatus,
       "StnBatteryStatus": StnBatteryStatus,
       "StnFlashStatus": StnFlashStatus,
       "StnResourceStatus": StnResourceStatus,
       "StnUserFailureType": StnUserFailureType,
       "StnConfigFailureType": StnConfigFailureType,
       "StnDomainMapType": StnDomainMapType,
       "stnTextualConventions": stnTextualConventions}
)
