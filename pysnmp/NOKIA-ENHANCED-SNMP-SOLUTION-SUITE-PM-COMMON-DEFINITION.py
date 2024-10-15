# SNMP MIB module (NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:38 2024
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

(noiOpenInterfaceModule,) = mibBuilder.importSymbols(
    "NOKIA-NE3S-REGISTRATION-MIB",
    "noiOpenInterfaceModule")

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

noiSnmpPMIrpCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 3)
)
noiSnmpPMIrpCommon.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NoiMeasurementActivationError(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("activationError", 10),
          ("complexityLimitationError", 12),
          ("corruptedFileError", 4),
          ("internalError", 11),
          ("intervalError", 8),
          ("invalidDurationError", 15),
          ("invalidHourError", 13),
          ("invalidMinutesError", 14),
          ("noError", 1),
          ("noMeasurementScheduleFileCreatedError", 2),
          ("startDateError", 6),
          ("stopDateError", 7),
          ("syntaxErrorInMeasurementScheduleFileError", 3),
          ("unknowDNError", 9),
          ("unknownMeasurementTypeError", 5))
    )



class NoiMeasurementFileName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 150),
    )



class NoiMeasurementFileDirectory(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class NoiMeasurementResultIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NoiMeasurementFileTransfer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )



class NoiMeasurementJobStatus(Integer32, TextualConvention):
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
        *(("activating", 2),
          ("activationFailed", 3),
          ("active", 4),
          ("idle", 1))
    )



class NoiMeasurementResultTransfer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notificationBased", 1),
          ("pollingBased", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION",
    **{"NoiMeasurementActivationError": NoiMeasurementActivationError,
       "NoiMeasurementFileName": NoiMeasurementFileName,
       "NoiMeasurementFileDirectory": NoiMeasurementFileDirectory,
       "NoiMeasurementResultIdentifier": NoiMeasurementResultIdentifier,
       "NoiMeasurementFileTransfer": NoiMeasurementFileTransfer,
       "NoiMeasurementJobStatus": NoiMeasurementJobStatus,
       "NoiMeasurementResultTransfer": NoiMeasurementResultTransfer,
       "noiSnmpPMIrpCommon": noiSnmpPMIrpCommon}
)
