# SNMP MIB module (PACEMAKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACEMAKER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:59 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(netSnmp,) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmp")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

pacemaker = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32723)
)
pacemaker.setRevisions(
        ("2009-10-05 11:15",
         "2009-10-06 21:15")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PacemakerNotification_ObjectIdentity = ObjectIdentity
pacemakerNotification = _PacemakerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32723, 1)
)


class _PacemakerNotificationNode_Type(OctetString):
    """Custom type pacemakerNotificationNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PacemakerNotificationNode_Type.__name__ = "OctetString"
_PacemakerNotificationNode_Object = MibScalar
pacemakerNotificationNode = _PacemakerNotificationNode_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 1),
    _PacemakerNotificationNode_Type()
)
pacemakerNotificationNode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationNode.setStatus("current")


class _PacemakerNotificationResource_Type(OctetString):
    """Custom type pacemakerNotificationResource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PacemakerNotificationResource_Type.__name__ = "OctetString"
_PacemakerNotificationResource_Object = MibScalar
pacemakerNotificationResource = _PacemakerNotificationResource_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 2),
    _PacemakerNotificationResource_Type()
)
pacemakerNotificationResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationResource.setStatus("current")


class _PacemakerNotificationOperation_Type(OctetString):
    """Custom type pacemakerNotificationOperation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PacemakerNotificationOperation_Type.__name__ = "OctetString"
_PacemakerNotificationOperation_Object = MibScalar
pacemakerNotificationOperation = _PacemakerNotificationOperation_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 3),
    _PacemakerNotificationOperation_Type()
)
pacemakerNotificationOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationOperation.setStatus("current")


class _PacemakerNotificationDescription_Type(OctetString):
    """Custom type pacemakerNotificationDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PacemakerNotificationDescription_Type.__name__ = "OctetString"
_PacemakerNotificationDescription_Object = MibScalar
pacemakerNotificationDescription = _PacemakerNotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 4),
    _PacemakerNotificationDescription_Type()
)
pacemakerNotificationDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationDescription.setStatus("current")
_PacemakerNotificationStatus_Type = Integer32
_PacemakerNotificationStatus_Object = MibScalar
pacemakerNotificationStatus = _PacemakerNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 5),
    _PacemakerNotificationStatus_Type()
)
pacemakerNotificationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationStatus.setStatus("current")
_PacemakerNotificationReturnCode_Type = Integer32
_PacemakerNotificationReturnCode_Object = MibScalar
pacemakerNotificationReturnCode = _PacemakerNotificationReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 6),
    _PacemakerNotificationReturnCode_Type()
)
pacemakerNotificationReturnCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationReturnCode.setStatus("current")
_PacemakerNotificationTargetReturnCode_Type = Integer32
_PacemakerNotificationTargetReturnCode_Object = MibScalar
pacemakerNotificationTargetReturnCode = _PacemakerNotificationTargetReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 32723, 1, 7),
    _PacemakerNotificationTargetReturnCode_Type()
)
pacemakerNotificationTargetReturnCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pacemakerNotificationTargetReturnCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACEMAKER-MIB",
    **{"pacemaker": pacemaker,
       "pacemakerNotification": pacemakerNotification,
       "pacemakerNotificationNode": pacemakerNotificationNode,
       "pacemakerNotificationResource": pacemakerNotificationResource,
       "pacemakerNotificationOperation": pacemakerNotificationOperation,
       "pacemakerNotificationDescription": pacemakerNotificationDescription,
       "pacemakerNotificationStatus": pacemakerNotificationStatus,
       "pacemakerNotificationReturnCode": pacemakerNotificationReturnCode,
       "pacemakerNotificationTargetReturnCode": pacemakerNotificationTargetReturnCode}
)
