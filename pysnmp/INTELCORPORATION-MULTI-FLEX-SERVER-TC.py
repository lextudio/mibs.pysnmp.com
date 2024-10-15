# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:05 2024
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

(regModule,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "regModule")

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

multiFlexServerTcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 2)
)
multiFlexServerTcModule.setRevisions(
        ("2008-05-28 02:00",
         "2008-05-07 02:40",
         "2007-08-16 13:30",
         "2007-08-15 19:00",
         "2007-07-10 17:00",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-23 19:00",
         "2007-05-21 12:00",
         "2007-03-12 18:30",
         "2007-02-22 17:00",
         "2007-01-05 10:50",
         "2006-12-28 13:10",
         "2006-11-07 07:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Index(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class INT32withException(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("unknown", -16))
    )



class PowerLedStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -4,
              -1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dataNotAvailable", -1),
          ("forcedOff", 3),
          ("hardReset", 4),
          ("identify", -4),
          ("notApplicable", -32),
          ("off", 0),
          ("on", 2),
          ("standby", 1),
          ("unknown", -16))
    )



class FaultLedStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -4,
              -1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataNotAvailable", -1),
          ("degraded", 1),
          ("fault", 2),
          ("identify", -4),
          ("normal", 0),
          ("notApplicable", -32),
          ("unknown", -16))
    )



class PresenceLedStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -3,
              -1,
              0,
              15,
              30,
              60,
              120)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn", -3),
          ("dataNotAvailable", -1),
          ("fifteenSeconds", 15),
          ("notApplicable", -32),
          ("off", 0),
          ("sixtySeconds", 60),
          ("thirtySeconds", 30),
          ("twoMinutes", 120),
          ("unknown", -16))
    )



class FeatureSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("supported", 1),
          ("unknown", -16),
          ("unsupported", 0))
    )



class Presence(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -4,
              -2,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("identify", -4),
          ("notApplicable", -32),
          ("present", 1),
          ("timedout", -2),
          ("unknown", -16))
    )



class Power(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("unknown", -1))
    )



class IdromBinary16(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class JackType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 5),
          ("db9", 4),
          ("fAUI", 6),
          ("fiberLC", 14),
          ("fiberMIC", 9),
          ("fiberSC", 8),
          ("fiberST", 10),
          ("hssdc", 13),
          ("mAUI", 7),
          ("mtrj", 12),
          ("other", 1),
          ("rj45", 2),
          ("rj45S", 3),
          ("telco", 11))
    )



class TimeFilter(TimeTicks, TextualConvention):
    status = "current"


class PortList(OctetString, TextualConvention):
    status = "current"


class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    **{"Index": Index,
       "INT32withException": INT32withException,
       "PowerLedStates": PowerLedStates,
       "FaultLedStates": FaultLedStates,
       "PresenceLedStates": PresenceLedStates,
       "FeatureSet": FeatureSet,
       "Presence": Presence,
       "Power": Power,
       "IdromBinary16": IdromBinary16,
       "JackType": JackType,
       "TimeFilter": TimeFilter,
       "PortList": PortList,
       "VlanIndex": VlanIndex,
       "EnabledStatus": EnabledStatus,
       "multiFlexServerTcModule": multiFlexServerTcModule}
)
