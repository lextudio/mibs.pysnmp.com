# SNMP MIB module (EMCGATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMCGATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:24 2024
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

(connUnitEventDescr,
 connUnitEventId,
 connUnitEventObject,
 connUnitEventSeverity,
 connUnitEventType,
 connUnitId,
 connUnitName,
 connUnitState,
 connUnitStatus,
 connUnitType) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitEventDescr",
    "connUnitEventId",
    "connUnitEventObject",
    "connUnitEventSeverity",
    "connUnitEventType",
    "connUnitId",
    "connUnitName",
    "connUnitState",
    "connUnitStatus",
    "connUnitType")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emc_ObjectIdentity = ObjectIdentity
emc = _Emc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139)
)
_EccGateway_ObjectIdentity = ObjectIdentity
eccGateway = _EccGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 3)
)


class _EccGatewayRevision_Type(DisplayString):
    """Custom type eccGatewayRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EccGatewayRevision_Type.__name__ = "DisplayString"
_EccGatewayRevision_Object = MibScalar
eccGatewayRevision = _EccGatewayRevision_Object(
    (1, 3, 6, 1, 4, 1, 1139, 3, 1),
    _EccGatewayRevision_Type()
)
eccGatewayRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccGatewayRevision.setStatus("mandatory")

# Managed Objects groups


# Notification objects

eccUnitStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 3, 0, 1)
)
eccUnitStatusChange.setObjects(
      *(("FCMGMT-MIB", "connUnitStatus"),
        ("FCMGMT-MIB", "connUnitState"),
        ("FCMGMT-MIB", "connUnitName"),
        ("FCMGMT-MIB", "connUnitType"))
)
if mibBuilder.loadTexts:
    eccUnitStatusChange.setStatus(
        ""
    )

eccUnitDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 3, 0, 3)
)
eccUnitDeletedTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitId"),
        ("FCMGMT-MIB", "connUnitName"))
)
if mibBuilder.loadTexts:
    eccUnitDeletedTrap.setStatus(
        ""
    )

eccUnitEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 3, 0, 4)
)
eccUnitEventTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventObject"),
        ("FCMGMT-MIB", "connUnitEventDescr"),
        ("FCMGMT-MIB", "connUnitEventSeverity"),
        ("FCMGMT-MIB", "connUnitName"),
        ("FCMGMT-MIB", "connUnitType"))
)
if mibBuilder.loadTexts:
    eccUnitEventTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMCGATEWAY-MIB",
    **{"DisplayString": DisplayString,
       "emc": emc,
       "eccGateway": eccGateway,
       "eccUnitStatusChange": eccUnitStatusChange,
       "eccUnitDeletedTrap": eccUnitDeletedTrap,
       "eccUnitEventTrap": eccUnitEventTrap,
       "eccGatewayRevision": eccGatewayRevision}
)
