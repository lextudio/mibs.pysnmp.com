# SNMP MIB module (NBS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:45 2024
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

nbsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 250)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned16(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Unsigned64(Counter64, TextualConvention):
    status = "current"


class WritableU64(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class NbsTcTemperature(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 1000),
    )



class NbsTcMilliVolt(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )



class NbsTcMilliAmp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )



class NbsTcMicroAmp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )



class NbsTcMilliDb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 100000),
    )



class NbsTcMilliWatts(Integer32, TextualConvention):
    status = "current"


class NbsTcMHz(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NbsTcStatusSimple(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )



class NbsTcStatusLevel(Integer32, TextualConvention):
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
        *(("notSupported", 1),
          ("statusGood", 4),
          ("statusHighError", 6),
          ("statusHighWarning", 5),
          ("statusLowError", 2),
          ("statusLowWarning", 3))
    )



class NbsTcPartIndex(Unsigned32, TextualConvention):
    status = "current"


class NbsTcStagingCommit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("apply", 4),
          ("notSupported", 1),
          ("revertToCommitted", 3),
          ("supported", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Nbs_ObjectIdentity = ObjectIdentity
nbs = _Nbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
if mibBuilder.loadTexts:
    nbs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-MIB",
    **{"Unsigned16": Unsigned16,
       "Unsigned64": Unsigned64,
       "WritableU64": WritableU64,
       "NbsTcTemperature": NbsTcTemperature,
       "NbsTcMilliVolt": NbsTcMilliVolt,
       "NbsTcMilliAmp": NbsTcMilliAmp,
       "NbsTcMicroAmp": NbsTcMicroAmp,
       "NbsTcMilliDb": NbsTcMilliDb,
       "NbsTcMilliWatts": NbsTcMilliWatts,
       "NbsTcMHz": NbsTcMHz,
       "NbsTcStatusSimple": NbsTcStatusSimple,
       "NbsTcStatusLevel": NbsTcStatusLevel,
       "NbsTcPartIndex": NbsTcPartIndex,
       "NbsTcStagingCommit": NbsTcStagingCommit,
       "nbs": nbs,
       "nbsMib": nbsMib}
)
