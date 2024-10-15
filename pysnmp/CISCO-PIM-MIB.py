# SNMP MIB module (CISCO-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(pimInterfaceStatus,
 pimRPSetHoldTime) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimInterfaceStatus",
    "pimRPSetHoldTime")

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

ciscoPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184)
)
ciscoPimMIB.setRevisions(
        ("2000-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPimMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPimMIBObjects = _CiscoPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1)
)
_Cpim_ObjectIdentity = ObjectIdentity
cpim = _Cpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1)
)
_CpimInvalidRegisterMsgsRcvd_Type = Counter32
_CpimInvalidRegisterMsgsRcvd_Object = MibScalar
cpimInvalidRegisterMsgsRcvd = _CpimInvalidRegisterMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 1),
    _CpimInvalidRegisterMsgsRcvd_Type()
)
cpimInvalidRegisterMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimInvalidRegisterMsgsRcvd.setStatus("current")
_CpimInvalidJoinPruneMsgsRcvd_Type = Counter32
_CpimInvalidJoinPruneMsgsRcvd_Object = MibScalar
cpimInvalidJoinPruneMsgsRcvd = _CpimInvalidJoinPruneMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 2),
    _CpimInvalidJoinPruneMsgsRcvd_Type()
)
cpimInvalidJoinPruneMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimInvalidJoinPruneMsgsRcvd.setStatus("current")


class _CpimLastErrorType_Type(Integer32):
    """Custom type cpimLastErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalidJoinPrune", 3),
          ("invalidRegister", 2),
          ("none", 1))
    )


_CpimLastErrorType_Type.__name__ = "Integer32"
_CpimLastErrorType_Object = MibScalar
cpimLastErrorType = _CpimLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 3),
    _CpimLastErrorType_Type()
)
cpimLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorType.setStatus("current")
_CpimLastErrorOriginType_Type = InetAddressType
_CpimLastErrorOriginType_Object = MibScalar
cpimLastErrorOriginType = _CpimLastErrorOriginType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 4),
    _CpimLastErrorOriginType_Type()
)
cpimLastErrorOriginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorOriginType.setStatus("current")
_CpimLastErrorOrigin_Type = InetAddress
_CpimLastErrorOrigin_Object = MibScalar
cpimLastErrorOrigin = _CpimLastErrorOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 5),
    _CpimLastErrorOrigin_Type()
)
cpimLastErrorOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorOrigin.setStatus("current")
_CpimLastErrorGroupType_Type = InetAddressType
_CpimLastErrorGroupType_Object = MibScalar
cpimLastErrorGroupType = _CpimLastErrorGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 6),
    _CpimLastErrorGroupType_Type()
)
cpimLastErrorGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorGroupType.setStatus("current")
_CpimLastErrorGroup_Type = InetAddress
_CpimLastErrorGroup_Object = MibScalar
cpimLastErrorGroup = _CpimLastErrorGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 7),
    _CpimLastErrorGroup_Type()
)
cpimLastErrorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorGroup.setStatus("current")
_CpimLastErrorRPType_Type = InetAddressType
_CpimLastErrorRPType_Object = MibScalar
cpimLastErrorRPType = _CpimLastErrorRPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 8),
    _CpimLastErrorRPType_Type()
)
cpimLastErrorRPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorRPType.setStatus("current")
_CpimLastErrorRP_Type = InetAddress
_CpimLastErrorRP_Object = MibScalar
cpimLastErrorRP = _CpimLastErrorRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 1, 1, 9),
    _CpimLastErrorRP_Type()
)
cpimLastErrorRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimLastErrorRP.setStatus("current")
_CiscoPimMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoPimMIBNotificationPrefix = _CiscoPimMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2)
)
_CiscoPimMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoPimMIBNotifications = _CiscoPimMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0)
)
_CiscoPimMIBNotificationObjects_ObjectIdentity = ObjectIdentity
ciscoPimMIBNotificationObjects = _CiscoPimMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 1)
)


class _CpimRPMappingChangeType_Type(Integer32):
    """Custom type cpimRPMappingChangeType based on Integer32"""
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
        *(("deletedMapping", 2),
          ("modifiedNewMapping", 4),
          ("modifiedOldMapping", 3),
          ("newMapping", 1))
    )


_CpimRPMappingChangeType_Type.__name__ = "Integer32"
_CpimRPMappingChangeType_Object = MibScalar
cpimRPMappingChangeType = _CpimRPMappingChangeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 1, 1),
    _CpimRPMappingChangeType_Type()
)
cpimRPMappingChangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimRPMappingChangeType.setStatus("current")
_CiscoPimMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPimMIBConformance = _CiscoPimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3)
)
_CiscoPimMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPimMIBCompliances = _CiscoPimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3, 1)
)
_CiscoPimMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPimMIBGroups = _CiscoPimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3, 2)
)

# Managed Objects groups

ciscoPimSparseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3, 2, 1)
)
ciscoPimSparseMIBGroup.setObjects(
      *(("CISCO-PIM-MIB", "cpimInvalidRegisterMsgsRcvd"),
        ("CISCO-PIM-MIB", "cpimInvalidJoinPruneMsgsRcvd"),
        ("CISCO-PIM-MIB", "cpimLastErrorType"),
        ("CISCO-PIM-MIB", "cpimLastErrorOriginType"),
        ("CISCO-PIM-MIB", "cpimLastErrorOrigin"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroupType"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroup"),
        ("CISCO-PIM-MIB", "cpimLastErrorRPType"),
        ("CISCO-PIM-MIB", "cpimLastErrorRP"))
)
if mibBuilder.loadTexts:
    ciscoPimSparseMIBGroup.setStatus("current")

ciscoPimNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3, 2, 2)
)
ciscoPimNotificationObjectGroup.setObjects(
    ("CISCO-PIM-MIB", "cpimRPMappingChangeType")
)
if mibBuilder.loadTexts:
    ciscoPimNotificationObjectGroup.setStatus("current")


# Notification objects

ciscoPimInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0, 1)
)
ciscoPimInterfaceUp.setObjects(
    ("PIM-MIB", "pimInterfaceStatus")
)
if mibBuilder.loadTexts:
    ciscoPimInterfaceUp.setStatus(
        "current"
    )

ciscoPimInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0, 2)
)
ciscoPimInterfaceDown.setObjects(
    ("PIM-MIB", "pimInterfaceStatus")
)
if mibBuilder.loadTexts:
    ciscoPimInterfaceDown.setStatus(
        "current"
    )

ciscoPimRPMappingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0, 3)
)
ciscoPimRPMappingChange.setObjects(
      *(("PIM-MIB", "pimRPSetHoldTime"),
        ("CISCO-PIM-MIB", "cpimRPMappingChangeType"))
)
if mibBuilder.loadTexts:
    ciscoPimRPMappingChange.setStatus(
        "current"
    )

ciscoPimInvalidRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0, 4)
)
ciscoPimInvalidRegister.setObjects(
      *(("CISCO-PIM-MIB", "cpimLastErrorOriginType"),
        ("CISCO-PIM-MIB", "cpimLastErrorOrigin"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroupType"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroup"),
        ("CISCO-PIM-MIB", "cpimLastErrorRPType"),
        ("CISCO-PIM-MIB", "cpimLastErrorRP"),
        ("CISCO-PIM-MIB", "cpimInvalidRegisterMsgsRcvd"))
)
if mibBuilder.loadTexts:
    ciscoPimInvalidRegister.setStatus(
        "current"
    )

ciscoPimInvalidJoinPrune = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 2, 0, 5)
)
ciscoPimInvalidJoinPrune.setObjects(
      *(("CISCO-PIM-MIB", "cpimLastErrorOriginType"),
        ("CISCO-PIM-MIB", "cpimLastErrorOrigin"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroupType"),
        ("CISCO-PIM-MIB", "cpimLastErrorGroup"),
        ("CISCO-PIM-MIB", "cpimLastErrorRPType"),
        ("CISCO-PIM-MIB", "cpimLastErrorRP"),
        ("CISCO-PIM-MIB", "cpimInvalidJoinPruneMsgsRcvd"))
)
if mibBuilder.loadTexts:
    ciscoPimInvalidJoinPrune.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPimSparseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 184, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPimSparseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PIM-MIB",
    **{"ciscoPimMIB": ciscoPimMIB,
       "ciscoPimMIBObjects": ciscoPimMIBObjects,
       "cpim": cpim,
       "cpimInvalidRegisterMsgsRcvd": cpimInvalidRegisterMsgsRcvd,
       "cpimInvalidJoinPruneMsgsRcvd": cpimInvalidJoinPruneMsgsRcvd,
       "cpimLastErrorType": cpimLastErrorType,
       "cpimLastErrorOriginType": cpimLastErrorOriginType,
       "cpimLastErrorOrigin": cpimLastErrorOrigin,
       "cpimLastErrorGroupType": cpimLastErrorGroupType,
       "cpimLastErrorGroup": cpimLastErrorGroup,
       "cpimLastErrorRPType": cpimLastErrorRPType,
       "cpimLastErrorRP": cpimLastErrorRP,
       "ciscoPimMIBNotificationPrefix": ciscoPimMIBNotificationPrefix,
       "ciscoPimMIBNotifications": ciscoPimMIBNotifications,
       "ciscoPimInterfaceUp": ciscoPimInterfaceUp,
       "ciscoPimInterfaceDown": ciscoPimInterfaceDown,
       "ciscoPimRPMappingChange": ciscoPimRPMappingChange,
       "ciscoPimInvalidRegister": ciscoPimInvalidRegister,
       "ciscoPimInvalidJoinPrune": ciscoPimInvalidJoinPrune,
       "ciscoPimMIBNotificationObjects": ciscoPimMIBNotificationObjects,
       "cpimRPMappingChangeType": cpimRPMappingChangeType,
       "ciscoPimMIBConformance": ciscoPimMIBConformance,
       "ciscoPimMIBCompliances": ciscoPimMIBCompliances,
       "ciscoPimSparseMIBCompliance": ciscoPimSparseMIBCompliance,
       "ciscoPimMIBGroups": ciscoPimMIBGroups,
       "ciscoPimSparseMIBGroup": ciscoPimSparseMIBGroup,
       "ciscoPimNotificationObjectGroup": ciscoPimNotificationObjectGroup}
)
