# SNMP MIB module (BAS-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:23 2024
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

(basExtEvent,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basExtEvent")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasEvent_ObjectIdentity = ObjectIdentity
basEvent = _BasEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1)
)
_BasTrapRecipientTable_Object = MibTable
basTrapRecipientTable = _BasTrapRecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basTrapRecipientTable.setStatus("current")
_BasTrapRecipientEntry_Object = MibTableRow
basTrapRecipientEntry = _BasTrapRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1)
)
basTrapRecipientEntry.setIndexNames(
    (0, "BAS-EVENT-MIB", "basTrapRecipientIndex"),
)
if mibBuilder.loadTexts:
    basTrapRecipientEntry.setStatus("current")
_BasTrapRecipientIndex_Type = Integer32
_BasTrapRecipientIndex_Object = MibTableColumn
basTrapRecipientIndex = _BasTrapRecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 1),
    _BasTrapRecipientIndex_Type()
)
basTrapRecipientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrapRecipientIndex.setStatus("current")
_BasTrapRecipientIpAddr_Type = IpAddress
_BasTrapRecipientIpAddr_Object = MibTableColumn
basTrapRecipientIpAddr = _BasTrapRecipientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 2),
    _BasTrapRecipientIpAddr_Type()
)
basTrapRecipientIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapRecipientIpAddr.setStatus("current")


class _BasTrapRecipientUdpPort_Type(Integer32):
    """Custom type basTrapRecipientUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasTrapRecipientUdpPort_Type.__name__ = "Integer32"
_BasTrapRecipientUdpPort_Object = MibTableColumn
basTrapRecipientUdpPort = _BasTrapRecipientUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 3),
    _BasTrapRecipientUdpPort_Type()
)
basTrapRecipientUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapRecipientUdpPort.setStatus("current")


class _BasTrapRecipientCommName_Type(OctetString):
    """Custom type basTrapRecipientCommName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasTrapRecipientCommName_Type.__name__ = "OctetString"
_BasTrapRecipientCommName_Object = MibTableColumn
basTrapRecipientCommName = _BasTrapRecipientCommName_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 4),
    _BasTrapRecipientCommName_Type()
)
basTrapRecipientCommName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapRecipientCommName.setStatus("current")
_BasTrapRecipientRowStatus_Type = RowStatus
_BasTrapRecipientRowStatus_Object = MibTableColumn
basTrapRecipientRowStatus = _BasTrapRecipientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 5),
    _BasTrapRecipientRowStatus_Type()
)
basTrapRecipientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapRecipientRowStatus.setStatus("current")


class _BasTrapRecipientSnmpVersion_Type(Integer32):
    """Custom type basTrapRecipientSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BasTrapRecipientSnmpVersion_Type.__name__ = "Integer32"
_BasTrapRecipientSnmpVersion_Object = MibTableColumn
basTrapRecipientSnmpVersion = _BasTrapRecipientSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 6),
    _BasTrapRecipientSnmpVersion_Type()
)
basTrapRecipientSnmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapRecipientSnmpVersion.setStatus("current")
_BasTrapNotificationTable_Object = MibTable
basTrapNotificationTable = _BasTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basTrapNotificationTable.setStatus("current")
_BasTrapNotificationEntry_Object = MibTableRow
basTrapNotificationEntry = _BasTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1)
)
basTrapNotificationEntry.setIndexNames(
    (0, "BAS-EVENT-MIB", "basTrapNotificationId"),
    (0, "BAS-EVENT-MIB", "basTrapNotificationIndex"),
)
if mibBuilder.loadTexts:
    basTrapNotificationEntry.setStatus("current")
_BasTrapNotificationId_Type = ObjectIdentifier
_BasTrapNotificationId_Object = MibTableColumn
basTrapNotificationId = _BasTrapNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 1),
    _BasTrapNotificationId_Type()
)
basTrapNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapNotificationId.setStatus("current")
_BasTrapNotificationIndex_Type = Integer32
_BasTrapNotificationIndex_Object = MibTableColumn
basTrapNotificationIndex = _BasTrapNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 2),
    _BasTrapNotificationIndex_Type()
)
basTrapNotificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTrapNotificationIndex.setStatus("current")
_BasTrapNotificationRowStatus_Type = RowStatus
_BasTrapNotificationRowStatus_Object = MibTableColumn
basTrapNotificationRowStatus = _BasTrapNotificationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 3),
    _BasTrapNotificationRowStatus_Type()
)
basTrapNotificationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basTrapNotificationRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-EVENT-MIB",
    **{"basEventMib": basEventMib,
       "basEvent": basEvent,
       "basTrapRecipientTable": basTrapRecipientTable,
       "basTrapRecipientEntry": basTrapRecipientEntry,
       "basTrapRecipientIndex": basTrapRecipientIndex,
       "basTrapRecipientIpAddr": basTrapRecipientIpAddr,
       "basTrapRecipientUdpPort": basTrapRecipientUdpPort,
       "basTrapRecipientCommName": basTrapRecipientCommName,
       "basTrapRecipientRowStatus": basTrapRecipientRowStatus,
       "basTrapRecipientSnmpVersion": basTrapRecipientSnmpVersion,
       "basTrapNotificationTable": basTrapNotificationTable,
       "basTrapNotificationEntry": basTrapNotificationEntry,
       "basTrapNotificationId": basTrapNotificationId,
       "basTrapNotificationIndex": basTrapNotificationIndex,
       "basTrapNotificationRowStatus": basTrapNotificationRowStatus}
)
