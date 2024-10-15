# SNMP MIB module (NORTEL-NMI-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NMI-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:51 2024
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

(nortelNetworkManagementInterfaceMIBs,) = mibBuilder.importSymbols(
    "NORTEL-GENERIC-MIB",
    "nortelNetworkManagementInterfaceMIBs")

(NortelNMIadminState,
 NortelNMIneType,
 NortelNMIoperState,
 NortelNMIunknownStatusValue) = mibBuilder.importSymbols(
    "NORTEL-NMI-TC-MIB",
    "NortelNMIadminState",
    "NortelNMIneType",
    "NortelNMIoperState",
    "NortelNMIunknownStatusValue")

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

nortelNMInotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6)
)
nortelNMInotificationsMIB.setRevisions(
        ("1999-07-19 00:00",
         "1999-06-24 00:00",
         "1999-05-31 00:00",
         "1999-04-12 00:00",
         "1999-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NortelNMIcurrentTxNotificationSequenceNum_Type = Unsigned32
_NortelNMIcurrentTxNotificationSequenceNum_Object = MibScalar
nortelNMIcurrentTxNotificationSequenceNum = _NortelNMIcurrentTxNotificationSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 1),
    _NortelNMIcurrentTxNotificationSequenceNum_Type()
)
nortelNMIcurrentTxNotificationSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nortelNMIcurrentTxNotificationSequenceNum.setStatus("current")
_NortelNMIcommonNotiVarbinds_ObjectIdentity = ObjectIdentity
nortelNMIcommonNotiVarbinds = _NortelNMIcommonNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2)
)
if mibBuilder.loadTexts:
    nortelNMIcommonNotiVarbinds.setStatus("current")
_NortelNMInotifyNeType_Type = NortelNMIneType
_NortelNMInotifyNeType_Object = MibScalar
nortelNMInotifyNeType = _NortelNMInotifyNeType_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 1),
    _NortelNMInotifyNeType_Type()
)
nortelNMInotifyNeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeType.setStatus("current")


class _NortelNMInotifyNeName_Type(DisplayString):
    """Custom type nortelNMInotifyNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NortelNMInotifyNeName_Type.__name__ = "DisplayString"
_NortelNMInotifyNeName_Object = MibScalar
nortelNMInotifyNeName = _NortelNMInotifyNeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 2),
    _NortelNMInotifyNeName_Type()
)
nortelNMInotifyNeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeName.setStatus("current")
_NortelNMInotifyNeAdminState_Type = NortelNMIadminState
_NortelNMInotifyNeAdminState_Object = MibScalar
nortelNMInotifyNeAdminState = _NortelNMInotifyNeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 3),
    _NortelNMInotifyNeAdminState_Type()
)
nortelNMInotifyNeAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeAdminState.setStatus("current")
_NortelNMInotifyNeOperState_Type = NortelNMIoperState
_NortelNMInotifyNeOperState_Object = MibScalar
nortelNMInotifyNeOperState = _NortelNMInotifyNeOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 4),
    _NortelNMInotifyNeOperState_Type()
)
nortelNMInotifyNeOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeOperState.setStatus("current")
_NortelNMInotifyNeUnknownStatus_Type = NortelNMIunknownStatusValue
_NortelNMInotifyNeUnknownStatus_Object = MibScalar
nortelNMInotifyNeUnknownStatus = _NortelNMInotifyNeUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 5),
    _NortelNMInotifyNeUnknownStatus_Type()
)
nortelNMInotifyNeUnknownStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeUnknownStatus.setStatus("current")
_NortelNMIconfigNotiMIB_ObjectIdentity = ObjectIdentity
nortelNMIconfigNotiMIB = _NortelNMIconfigNotiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3)
)
if mibBuilder.loadTexts:
    nortelNMIconfigNotiMIB.setStatus("current")
_NortelNMIfaultNotiMIB_ObjectIdentity = ObjectIdentity
nortelNMIfaultNotiMIB = _NortelNMIfaultNotiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4)
)
if mibBuilder.loadTexts:
    nortelNMIfaultNotiMIB.setStatus("current")
_NortelNMIinfoNotiMIB_ObjectIdentity = ObjectIdentity
nortelNMIinfoNotiMIB = _NortelNMIinfoNotiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5)
)
if mibBuilder.loadTexts:
    nortelNMIinfoNotiMIB.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NMI-NOTIFICATIONS-MIB",
    **{"nortelNMInotificationsMIB": nortelNMInotificationsMIB,
       "nortelNMIcurrentTxNotificationSequenceNum": nortelNMIcurrentTxNotificationSequenceNum,
       "nortelNMIcommonNotiVarbinds": nortelNMIcommonNotiVarbinds,
       "nortelNMInotifyNeType": nortelNMInotifyNeType,
       "nortelNMInotifyNeName": nortelNMInotifyNeName,
       "nortelNMInotifyNeAdminState": nortelNMInotifyNeAdminState,
       "nortelNMInotifyNeOperState": nortelNMInotifyNeOperState,
       "nortelNMInotifyNeUnknownStatus": nortelNMInotifyNeUnknownStatus,
       "nortelNMIconfigNotiMIB": nortelNMIconfigNotiMIB,
       "nortelNMIfaultNotiMIB": nortelNMIfaultNotiMIB,
       "nortelNMIinfoNotiMIB": nortelNMIinfoNotiMIB}
)
