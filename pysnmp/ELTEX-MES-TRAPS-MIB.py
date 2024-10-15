# SNMP MIB module (ELTEX-MES-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:03 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(rldot1dStpTrapVrblVID,
 rldot1dStpTrapVrblifIndex) = mibBuilder.importSymbols(
    "RADLAN-BRIDGEMIBOBJECTS-MIB",
    "rldot1dStpTrapVrblVID",
    "rldot1dStpTrapVrblifIndex")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

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

eltMesNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0)
)
eltMesNotifications.setRevisions(
        ("2012-07-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

i2cBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 3)
)
i2cBusFailure.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    i2cBusFailure.setStatus(
        "current"
    )

i2cBusOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 4)
)
i2cBusOperational.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    i2cBusOperational.setStatus(
        "current"
    )

transThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 5)
)
transThresholdWarning.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    transThresholdWarning.setStatus(
        "current"
    )

transThresholdOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 6)
)
transThresholdOK.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    transThresholdOK.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-TRAPS-MIB",
    **{"eltMesNotifications": eltMesNotifications,
       "i2cBusFailure": i2cBusFailure,
       "i2cBusOperational": i2cBusOperational,
       "transThresholdWarning": transThresholdWarning,
       "transThresholdOK": transThresholdOK}
)
