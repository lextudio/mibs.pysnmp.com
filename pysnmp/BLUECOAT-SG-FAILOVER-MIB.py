# SNMP MIB module (BLUECOAT-SG-FAILOVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:19 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGFailoverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13)
)
bluecoatSGFailoverMIB.setRevisions(
        ("2011-12-20 03:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FailoverMessageString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_BluecoatSgFailoverMIBObjects_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBObjects = _BluecoatSgFailoverMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1)
)
_BluecoatSgFailoverValues_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverValues = _BluecoatSgFailoverValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1)
)
_BluecoatSgFailoverMessage_Type = FailoverMessageString
_BluecoatSgFailoverMessage_Object = MibScalar
bluecoatSgFailoverMessage = _BluecoatSgFailoverMessage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1, 1),
    _BluecoatSgFailoverMessage_Type()
)
bluecoatSgFailoverMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bluecoatSgFailoverMessage.setStatus("current")
_BluecoatSgFailoverMIBNotifications_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBNotifications = _BluecoatSgFailoverMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2)
)
_BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBNotificationsPrefix = _BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0)
)

# Managed Objects groups


# Notification objects

bluecoatSgFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0, 1)
)
bluecoatSgFailoverTrap.setObjects(
    ("BLUECOAT-SG-FAILOVER-MIB", "bluecoatSgFailoverMessage")
)
if mibBuilder.loadTexts:
    bluecoatSgFailoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-FAILOVER-MIB",
    **{"FailoverMessageString": FailoverMessageString,
       "bluecoatSGFailoverMIB": bluecoatSGFailoverMIB,
       "bluecoatSgFailoverMIBObjects": bluecoatSgFailoverMIBObjects,
       "bluecoatSgFailoverValues": bluecoatSgFailoverValues,
       "bluecoatSgFailoverMessage": bluecoatSgFailoverMessage,
       "bluecoatSgFailoverMIBNotifications": bluecoatSgFailoverMIBNotifications,
       "bluecoatSgFailoverMIBNotificationsPrefix": bluecoatSgFailoverMIBNotificationsPrefix,
       "bluecoatSgFailoverTrap": bluecoatSgFailoverTrap}
)
