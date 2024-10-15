# SNMP MIB module (IANAPowerStateSet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANAPowerStateSet-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:32 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ianaPowerStateSet = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 228)
)
ianaPowerStateSet.setRevisions(
        ("2015-02-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PowerStateSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255,
              256,
              257,
              258,
              259,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036)
        )
    )
    namedValues = NamedValues(
        *(("dmtf", 512),
          ("dmtfDiagnosticInterrapt", 522),
          ("dmtfHibernate", 518),
          ("dmtfMasterBusReset", 521),
          ("dmtfMasterBusResetGraceful", 525),
          ("dmtfOffHard", 516),
          ("dmtfOffHardGraceful", 524),
          ("dmtfOffSoft", 517),
          ("dmtfOffSoftGraceful", 523),
          ("dmtfOn", 513),
          ("dmtfPowerCycleHardGraceful", 527),
          ("dmtfPowerCycleOffSoftGraceful", 526),
          ("dmtfPowerOffHard", 520),
          ("dmtfPowerOffSoft", 519),
          ("dmtfSleepDeep", 515),
          ("dmtfSleepLight", 514),
          ("eman", 1024),
          ("emanHibernate", 1027),
          ("emanHigh", 1036),
          ("emanHighMinus", 1035),
          ("emanLow", 1032),
          ("emanLowMinus", 1031),
          ("emanMechOff", 1025),
          ("emanMedium", 1034),
          ("emanMediumMinus", 1033),
          ("emanReady", 1030),
          ("emanSleep", 1028),
          ("emanSoftOff", 1026),
          ("emanStandby", 1029),
          ("ieee1621", 256),
          ("ieee1621Off", 257),
          ("ieee1621On", 259),
          ("ieee1621Sleep", 258),
          ("other", 0),
          ("unknown", 255))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANAPowerStateSet-MIB",
    **{"PowerStateSet": PowerStateSet,
       "ianaPowerStateSet": ianaPowerStateSet}
)
