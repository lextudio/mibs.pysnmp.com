# SNMP MIB module (CIENA-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:52 2024
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

ciena = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
ciena.setRevisions(
        ("2013-04-22 00:00",
         "2012-12-26 00:00",
         "2010-09-27 23:17")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCommon_ObjectIdentity = ObjectIdentity
cienaCommon = _CienaCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1)
)
if mibBuilder.loadTexts:
    cienaCommon.setStatus("current")
_CienaProducts_ObjectIdentity = ObjectIdentity
cienaProducts = _CienaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2)
)
if mibBuilder.loadTexts:
    cienaProducts.setStatus("current")
_CienaCes_ObjectIdentity = ObjectIdentity
cienaCes = _CienaCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2)
)
if mibBuilder.loadTexts:
    cienaCes.setStatus("current")
_CienaCesConfig_ObjectIdentity = ObjectIdentity
cienaCesConfig = _CienaCesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesConfig.setStatus("current")
_CienaCesNotifications_ObjectIdentity = ObjectIdentity
cienaCesNotifications = _CienaCesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesNotifications.setStatus("current")
_CienaCesNotificationsControlModule_ObjectIdentity = ObjectIdentity
cienaCesNotificationsControlModule = _CienaCesNotificationsControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesNotificationsControlModule.setStatus("current")
_CienaCesStatistics_ObjectIdentity = ObjectIdentity
cienaCesStatistics = _CienaCesStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-SMI",
    **{"ciena": ciena,
       "cienaCommon": cienaCommon,
       "cienaProducts": cienaProducts,
       "cienaCes": cienaCes,
       "cienaCesConfig": cienaCesConfig,
       "cienaCesNotifications": cienaCesNotifications,
       "cienaCesNotificationsControlModule": cienaCesNotificationsControlModule,
       "cienaCesStatistics": cienaCesStatistics}
)
