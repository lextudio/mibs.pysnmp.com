# SNMP MIB module (T11-FC-FABRIC-LOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-FABRIC-LOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:29 2024
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

(fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(T11NsGs4RejectReasonCode,) = mibBuilder.importSymbols(
    "T11-FC-NAME-SERVER-MIB",
    "T11NsGs4RejectReasonCode")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FabricLockMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 159)
)
t11FabricLockMIB.setRevisions(
        ("2007-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FLockMIBNotifications_ObjectIdentity = ObjectIdentity
t11FLockMIBNotifications = _T11FLockMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 0)
)
_T11FLockMIBObjects_ObjectIdentity = ObjectIdentity
t11FLockMIBObjects = _T11FLockMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 1)
)
_T11FLockConfiguration_ObjectIdentity = ObjectIdentity
t11FLockConfiguration = _T11FLockConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 1, 1)
)
_T11FLockTable_Object = MibTable
t11FLockTable = _T11FLockTable_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FLockTable.setStatus("current")
_T11FLockEntry_Object = MibTableRow
t11FLockEntry = _T11FLockEntry_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1)
)
t11FLockEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-LOCK-MIB", "t11FLockFabricIndex"),
    (0, "T11-FC-FABRIC-LOCK-MIB", "t11FLockApplicationID"),
)
if mibBuilder.loadTexts:
    t11FLockEntry.setStatus("current")
_T11FLockFabricIndex_Type = T11FabricIndex
_T11FLockFabricIndex_Object = MibTableColumn
t11FLockFabricIndex = _T11FLockFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 1),
    _T11FLockFabricIndex_Type()
)
t11FLockFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FLockFabricIndex.setStatus("current")


class _T11FLockApplicationID_Type(OctetString):
    """Custom type t11FLockApplicationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FLockApplicationID_Type.__name__ = "OctetString"
_T11FLockApplicationID_Object = MibTableColumn
t11FLockApplicationID = _T11FLockApplicationID_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 2),
    _T11FLockApplicationID_Type()
)
t11FLockApplicationID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FLockApplicationID.setStatus("current")


class _T11FLockInitiatorType_Type(Integer32):
    """Custom type t11FLockInitiatorType based on Integer32"""
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
        *(("cli", 3),
          ("other", 1),
          ("snmp", 4),
          ("ssb", 2))
    )


_T11FLockInitiatorType_Type.__name__ = "Integer32"
_T11FLockInitiatorType_Object = MibTableColumn
t11FLockInitiatorType = _T11FLockInitiatorType_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 3),
    _T11FLockInitiatorType_Type()
)
t11FLockInitiatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockInitiatorType.setStatus("current")


class _T11FLockInitiator_Type(OctetString):
    """Custom type t11FLockInitiator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_T11FLockInitiator_Type.__name__ = "OctetString"
_T11FLockInitiator_Object = MibTableColumn
t11FLockInitiator = _T11FLockInitiator_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 4),
    _T11FLockInitiator_Type()
)
t11FLockInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockInitiator.setStatus("current")
_T11FLockInitiatorIpAddrType_Type = InetAddressType
_T11FLockInitiatorIpAddrType_Object = MibTableColumn
t11FLockInitiatorIpAddrType = _T11FLockInitiatorIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 5),
    _T11FLockInitiatorIpAddrType_Type()
)
t11FLockInitiatorIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockInitiatorIpAddrType.setStatus("current")
_T11FLockInitiatorIpAddr_Type = InetAddress
_T11FLockInitiatorIpAddr_Object = MibTableColumn
t11FLockInitiatorIpAddr = _T11FLockInitiatorIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 6),
    _T11FLockInitiatorIpAddr_Type()
)
t11FLockInitiatorIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockInitiatorIpAddr.setStatus("current")


class _T11FLockStatus_Type(Integer32):
    """Custom type t11FLockStatus based on Integer32"""
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
        *(("active", 1),
          ("otherFailure", 4),
          ("rejectFailure", 3),
          ("settingUp", 2))
    )


_T11FLockStatus_Type.__name__ = "Integer32"
_T11FLockStatus_Object = MibTableColumn
t11FLockStatus = _T11FLockStatus_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 7),
    _T11FLockStatus_Type()
)
t11FLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockStatus.setStatus("current")
_T11FLockRejectReasonCode_Type = T11NsGs4RejectReasonCode
_T11FLockRejectReasonCode_Object = MibTableColumn
t11FLockRejectReasonCode = _T11FLockRejectReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 8),
    _T11FLockRejectReasonCode_Type()
)
t11FLockRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockRejectReasonCode.setStatus("current")


class _T11FLockRejectReasonCodeExp_Type(OctetString):
    """Custom type t11FLockRejectReasonCodeExp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_T11FLockRejectReasonCodeExp_Type.__name__ = "OctetString"
_T11FLockRejectReasonCodeExp_Object = MibTableColumn
t11FLockRejectReasonCodeExp = _T11FLockRejectReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 9),
    _T11FLockRejectReasonCodeExp_Type()
)
t11FLockRejectReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockRejectReasonCodeExp.setStatus("current")


class _T11FLockRejectReasonVendorCode_Type(OctetString):
    """Custom type t11FLockRejectReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_T11FLockRejectReasonVendorCode_Type.__name__ = "OctetString"
_T11FLockRejectReasonVendorCode_Object = MibTableColumn
t11FLockRejectReasonVendorCode = _T11FLockRejectReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 10),
    _T11FLockRejectReasonVendorCode_Type()
)
t11FLockRejectReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FLockRejectReasonVendorCode.setStatus("current")
_T11FLockRowStatus_Type = RowStatus
_T11FLockRowStatus_Object = MibTableColumn
t11FLockRowStatus = _T11FLockRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 159, 1, 1, 1, 1, 11),
    _T11FLockRowStatus_Type()
)
t11FLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FLockRowStatus.setStatus("current")
_T11FLockMIBConformance_ObjectIdentity = ObjectIdentity
t11FLockMIBConformance = _T11FLockMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 2)
)
_T11FLockMIBCompliances_ObjectIdentity = ObjectIdentity
t11FLockMIBCompliances = _T11FLockMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 2, 1)
)
_T11FLockMIBGroups_ObjectIdentity = ObjectIdentity
t11FLockMIBGroups = _T11FLockMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 159, 2, 2)
)

# Managed Objects groups

t11FLockActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 159, 2, 2, 1)
)
t11FLockActiveGroup.setObjects(
      *(("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorType"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiator"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorIpAddrType"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockInitiatorIpAddr"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockStatus"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonCode"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonCodeExp"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRejectReasonVendorCode"),
        ("T11-FC-FABRIC-LOCK-MIB", "t11FLockRowStatus"))
)
if mibBuilder.loadTexts:
    t11FLockActiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

t11FLockMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 159, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FLockMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-FABRIC-LOCK-MIB",
    **{"t11FabricLockMIB": t11FabricLockMIB,
       "t11FLockMIBNotifications": t11FLockMIBNotifications,
       "t11FLockMIBObjects": t11FLockMIBObjects,
       "t11FLockConfiguration": t11FLockConfiguration,
       "t11FLockTable": t11FLockTable,
       "t11FLockEntry": t11FLockEntry,
       "t11FLockFabricIndex": t11FLockFabricIndex,
       "t11FLockApplicationID": t11FLockApplicationID,
       "t11FLockInitiatorType": t11FLockInitiatorType,
       "t11FLockInitiator": t11FLockInitiator,
       "t11FLockInitiatorIpAddrType": t11FLockInitiatorIpAddrType,
       "t11FLockInitiatorIpAddr": t11FLockInitiatorIpAddr,
       "t11FLockStatus": t11FLockStatus,
       "t11FLockRejectReasonCode": t11FLockRejectReasonCode,
       "t11FLockRejectReasonCodeExp": t11FLockRejectReasonCodeExp,
       "t11FLockRejectReasonVendorCode": t11FLockRejectReasonVendorCode,
       "t11FLockRowStatus": t11FLockRowStatus,
       "t11FLockMIBConformance": t11FLockMIBConformance,
       "t11FLockMIBCompliances": t11FLockMIBCompliances,
       "t11FLockMIBCompliance": t11FLockMIBCompliance,
       "t11FLockMIBGroups": t11FLockMIBGroups,
       "t11FLockActiveGroup": t11FLockActiveGroup}
)
