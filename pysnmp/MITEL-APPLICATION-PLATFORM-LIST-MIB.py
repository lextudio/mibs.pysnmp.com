# SNMP MIB module (MITEL-APPLICATION-PLATFORM-LIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-APPLICATION-PLATFORM-LIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:10 2024
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

(mitelIdentification,) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelIdentification")

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

mitelIdApplicationPlatforms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6)
)
mitelIdApplicationPlatforms.setRevisions(
        ("2006-08-10 00:00",
         "2005-08-24 21:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MitelIdAppPlatManagementApplicationServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatManagementApplicationServer = _MitelIdAppPlatManagementApplicationServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatManagementApplicationServer.setStatus("current")
_MitelIdAppPlatLXTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatLXTelephonyServer = _MitelIdAppPlatLXTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatLXTelephonyServer.setStatus("current")
_MitelIdAppPlatMXTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatMXTelephonyServer = _MitelIdAppPlatMXTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 3)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatMXTelephonyServer.setStatus("current")
_MitelIdAppPlatCXTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatCXTelephonyServer = _MitelIdAppPlatCXTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 4)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatCXTelephonyServer.setStatus("current")
_MitelIdAppPlatCXiTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatCXiTelephonyServer = _MitelIdAppPlatCXiTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 5)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatCXiTelephonyServer.setStatus("current")
_MitelIdAppPlatLiteTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatLiteTelephonyServer = _MitelIdAppPlatLiteTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 6)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatLiteTelephonyServer.setStatus("current")
_MitelIdAppPlatMXeTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatMXeTelephonyServer = _MitelIdAppPlatMXeTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 7)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatMXeTelephonyServer.setStatus("current")
_MitelIdAppPlatAXTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatAXTelephonyServer = _MitelIdAppPlatAXTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 8)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatAXTelephonyServer.setStatus("current")
_MitelIdAppPlatMXTTelephonyServer_ObjectIdentity = ObjectIdentity
mitelIdAppPlatMXTTelephonyServer = _MitelIdAppPlatMXTTelephonyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6, 9)
)
if mibBuilder.loadTexts:
    mitelIdAppPlatMXTTelephonyServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-APPLICATION-PLATFORM-LIST-MIB",
    **{"mitelIdApplicationPlatforms": mitelIdApplicationPlatforms,
       "mitelIdAppPlatManagementApplicationServer": mitelIdAppPlatManagementApplicationServer,
       "mitelIdAppPlatLXTelephonyServer": mitelIdAppPlatLXTelephonyServer,
       "mitelIdAppPlatMXTelephonyServer": mitelIdAppPlatMXTelephonyServer,
       "mitelIdAppPlatCXTelephonyServer": mitelIdAppPlatCXTelephonyServer,
       "mitelIdAppPlatCXiTelephonyServer": mitelIdAppPlatCXiTelephonyServer,
       "mitelIdAppPlatLiteTelephonyServer": mitelIdAppPlatLiteTelephonyServer,
       "mitelIdAppPlatMXeTelephonyServer": mitelIdAppPlatMXeTelephonyServer,
       "mitelIdAppPlatAXTelephonyServer": mitelIdAppPlatAXTelephonyServer,
       "mitelIdAppPlatMXTTelephonyServer": mitelIdAppPlatMXTTelephonyServer}
)
