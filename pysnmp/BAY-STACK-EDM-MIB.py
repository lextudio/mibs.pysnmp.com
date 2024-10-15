# SNMP MIB module (BAY-STACK-EDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-EDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:56 2024
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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackEdmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 36)
)
bayStackEdmMib.setRevisions(
        ("2013-10-11 00:00",
         "2013-02-13 00:00",
         "2009-08-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayStackEdmNotifications_ObjectIdentity = ObjectIdentity
bayStackEdmNotifications = _BayStackEdmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 36, 0)
)
_BayStackEdmObjects_ObjectIdentity = ObjectIdentity
bayStackEdmObjects = _BayStackEdmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 36, 1)
)
_BsEdmScalars_ObjectIdentity = ObjectIdentity
bsEdmScalars = _BsEdmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1)
)


class _BsEdmHelpFilePath_Type(OctetString):
    """Custom type bsEdmHelpFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 327),
    )


_BsEdmHelpFilePath_Type.__name__ = "OctetString"
_BsEdmHelpFilePath_Object = MibScalar
bsEdmHelpFilePath = _BsEdmHelpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 1),
    _BsEdmHelpFilePath_Type()
)
bsEdmHelpFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsEdmHelpFilePath.setStatus("current")


class _BsEdmInactivityTimeout_Type(Integer32):
    """Custom type bsEdmInactivityTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_BsEdmInactivityTimeout_Type.__name__ = "Integer32"
_BsEdmInactivityTimeout_Object = MibScalar
bsEdmInactivityTimeout = _BsEdmInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 2),
    _BsEdmInactivityTimeout_Type()
)
bsEdmInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsEdmInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bsEdmInactivityTimeout.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-EDM-MIB",
    **{"bayStackEdmMib": bayStackEdmMib,
       "bayStackEdmNotifications": bayStackEdmNotifications,
       "bayStackEdmObjects": bayStackEdmObjects,
       "bsEdmScalars": bsEdmScalars,
       "bsEdmHelpFilePath": bsEdmHelpFilePath,
       "bsEdmInactivityTimeout": bsEdmInactivityTimeout}
)
