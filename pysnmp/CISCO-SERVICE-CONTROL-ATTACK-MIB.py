# SNMP MIB module (CISCO-SERVICE-CONTROL-ATTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROL-ATTACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:06 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoServiceControlAttackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693)
)
ciscoServiceControlAttackMIB.setRevisions(
        ("2013-08-16 00:00",
         "2009-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CscaAttackType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_CiscoServiceControlAttackMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoServiceControlAttackMIBNotifs = _CiscoServiceControlAttackMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 0)
)
_CiscoServiceControlAttackMIBObjects_ObjectIdentity = ObjectIdentity
ciscoServiceControlAttackMIBObjects = _CiscoServiceControlAttackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1)
)
_CscaFilterMIBObjects_ObjectIdentity = ObjectIdentity
cscaFilterMIBObjects = _CscaFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1)
)
_CscaType_Type = CscaAttackType
_CscaType_Object = MibScalar
cscaType = _CscaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 1),
    _CscaType_Type()
)
cscaType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaType.setStatus("current")
_CscaSourceAddressType_Type = InetAddressType
_CscaSourceAddressType_Object = MibScalar
cscaSourceAddressType = _CscaSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 2),
    _CscaSourceAddressType_Type()
)
cscaSourceAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaSourceAddressType.setStatus("current")
_CscaSourceAddress_Type = InetAddress
_CscaSourceAddress_Object = MibScalar
cscaSourceAddress = _CscaSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 3),
    _CscaSourceAddress_Type()
)
cscaSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaSourceAddress.setStatus("current")
_CscaDestinationAddressType_Type = InetAddressType
_CscaDestinationAddressType_Object = MibScalar
cscaDestinationAddressType = _CscaDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 4),
    _CscaDestinationAddressType_Type()
)
cscaDestinationAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaDestinationAddressType.setStatus("current")
_CscaDestinationAddress_Type = InetAddress
_CscaDestinationAddress_Object = MibScalar
cscaDestinationAddress = _CscaDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 5),
    _CscaDestinationAddress_Type()
)
cscaDestinationAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaDestinationAddress.setStatus("current")
_CscaAttackedPort_Type = InetPortNumber
_CscaAttackedPort_Object = MibScalar
cscaAttackedPort = _CscaAttackedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 6),
    _CscaAttackedPort_Type()
)
cscaAttackedPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaAttackedPort.setStatus("current")


class _CscaFilterStatus_Type(Integer32):
    """Custom type cscaFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_CscaFilterStatus_Type.__name__ = "Integer32"
_CscaFilterStatus_Object = MibScalar
cscaFilterStatus = _CscaFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 7),
    _CscaFilterStatus_Type()
)
cscaFilterStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cscaFilterStatus.setStatus("current")
_CscaNotifsEnabled_Type = TruthValue
_CscaNotifsEnabled_Object = MibScalar
cscaNotifsEnabled = _CscaNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 8),
    _CscaNotifsEnabled_Type()
)
cscaNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscaNotifsEnabled.setStatus("current")
_CscaLastDiscontinuityTimeStamp_Type = TimeStamp
_CscaLastDiscontinuityTimeStamp_Object = MibScalar
cscaLastDiscontinuityTimeStamp = _CscaLastDiscontinuityTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 9),
    _CscaLastDiscontinuityTimeStamp_Type()
)
cscaLastDiscontinuityTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaLastDiscontinuityTimeStamp.setStatus("current")


class _CscaGlobalAttackType_Type(Integer32):
    """Custom type cscaGlobalAttackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("icmpAttack", 1),
          ("tcpFragmentAttack", 6),
          ("tcpNonSynAttack", 7),
          ("tcpRstAttack", 5),
          ("tcpSynAttack", 4),
          ("udpAttack", 2),
          ("udpFragmentAttack", 3))
    )


_CscaGlobalAttackType_Type.__name__ = "Integer32"
_CscaGlobalAttackType_Object = MibScalar
cscaGlobalAttackType = _CscaGlobalAttackType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 10),
    _CscaGlobalAttackType_Type()
)
cscaGlobalAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaGlobalAttackType.setStatus("current")
_CscaGlobalAttackNotifsEnabled_Type = TruthValue
_CscaGlobalAttackNotifsEnabled_Object = MibScalar
cscaGlobalAttackNotifsEnabled = _CscaGlobalAttackNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 11),
    _CscaGlobalAttackNotifsEnabled_Type()
)
cscaGlobalAttackNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscaGlobalAttackNotifsEnabled.setStatus("current")
_CscaTypeTable_Object = MibTable
cscaTypeTable = _CscaTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2)
)
if mibBuilder.loadTexts:
    cscaTypeTable.setStatus("current")
_CscaTypeEntry_Object = MibTableRow
cscaTypeEntry = _CscaTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1)
)
cscaTypeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIndex"),
)
if mibBuilder.loadTexts:
    cscaTypeEntry.setStatus("current")


class _CscaTypeIndex_Type(CscaAttackType):
    """Custom type cscaTypeIndex based on CscaAttackType"""
    subtypeSpec = CscaAttackType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CscaTypeIndex_Type.__name__ = "CscaAttackType"
_CscaTypeIndex_Object = MibTableColumn
cscaTypeIndex = _CscaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 1),
    _CscaTypeIndex_Type()
)
cscaTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscaTypeIndex.setStatus("current")
_CscaTypeCurrentNumAttacks_Type = Gauge32
_CscaTypeCurrentNumAttacks_Object = MibTableColumn
cscaTypeCurrentNumAttacks = _CscaTypeCurrentNumAttacks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 2),
    _CscaTypeCurrentNumAttacks_Type()
)
cscaTypeCurrentNumAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeCurrentNumAttacks.setStatus("current")
if mibBuilder.loadTexts:
    cscaTypeCurrentNumAttacks.setUnits("attacks")
_CscaTypeTotalNumAttacks_Type = Counter32
_CscaTypeTotalNumAttacks_Object = MibTableColumn
cscaTypeTotalNumAttacks = _CscaTypeTotalNumAttacks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 3),
    _CscaTypeTotalNumAttacks_Type()
)
cscaTypeTotalNumAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeTotalNumAttacks.setStatus("current")
if mibBuilder.loadTexts:
    cscaTypeTotalNumAttacks.setUnits("attacks")
_CscaTypeTotalNumFlows_Type = Counter64
_CscaTypeTotalNumFlows_Object = MibTableColumn
cscaTypeTotalNumFlows = _CscaTypeTotalNumFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 4),
    _CscaTypeTotalNumFlows_Type()
)
cscaTypeTotalNumFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeTotalNumFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscaTypeTotalNumFlows.setUnits("IP flows")
_CscaTypeTotalNumSeconds_Type = Counter32
_CscaTypeTotalNumSeconds_Object = MibTableColumn
cscaTypeTotalNumSeconds = _CscaTypeTotalNumSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 5),
    _CscaTypeTotalNumSeconds_Type()
)
cscaTypeTotalNumSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeTotalNumSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cscaTypeTotalNumSeconds.setUnits("seconds")
_CscaTypeOriginatedByNetworkSide_Type = TruthValue
_CscaTypeOriginatedByNetworkSide_Object = MibTableColumn
cscaTypeOriginatedByNetworkSide = _CscaTypeOriginatedByNetworkSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 6),
    _CscaTypeOriginatedByNetworkSide_Type()
)
cscaTypeOriginatedByNetworkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeOriginatedByNetworkSide.setStatus("current")
_CscaTypeProtocol_Type = Integer32
_CscaTypeProtocol_Object = MibTableColumn
cscaTypeProtocol = _CscaTypeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 7),
    _CscaTypeProtocol_Type()
)
cscaTypeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeProtocol.setStatus("current")
_CscaTypeIsPortSpecific_Type = TruthValue
_CscaTypeIsPortSpecific_Object = MibTableColumn
cscaTypeIsPortSpecific = _CscaTypeIsPortSpecific_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 8),
    _CscaTypeIsPortSpecific_Type()
)
cscaTypeIsPortSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeIsPortSpecific.setStatus("current")
_CscaTypeIPsDetected_Type = Integer32
_CscaTypeIPsDetected_Object = MibTableColumn
cscaTypeIPsDetected = _CscaTypeIPsDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 9),
    _CscaTypeIPsDetected_Type()
)
cscaTypeIPsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaTypeIPsDetected.setStatus("current")
_CscaInfoTable_Object = MibTable
cscaInfoTable = _CscaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3)
)
if mibBuilder.loadTexts:
    cscaInfoTable.setStatus("current")
_CscaInfoEntry_Object = MibTableRow
cscaInfoEntry = _CscaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1)
)
cscaInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cscaInfoEntry.setStatus("current")
_CscaInfoUpStreamAttackFilteringTime_Type = Counter32
_CscaInfoUpStreamAttackFilteringTime_Object = MibTableColumn
cscaInfoUpStreamAttackFilteringTime = _CscaInfoUpStreamAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 1),
    _CscaInfoUpStreamAttackFilteringTime_Type()
)
cscaInfoUpStreamAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaInfoUpStreamAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    cscaInfoUpStreamAttackFilteringTime.setUnits("seconds")
_CscaInfoUpStreamLastAttackFilteringTime_Type = TimeInterval
_CscaInfoUpStreamLastAttackFilteringTime_Object = MibTableColumn
cscaInfoUpStreamLastAttackFilteringTime = _CscaInfoUpStreamLastAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 2),
    _CscaInfoUpStreamLastAttackFilteringTime_Type()
)
cscaInfoUpStreamLastAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaInfoUpStreamLastAttackFilteringTime.setStatus("current")
_CscaInfoDownStreamAttackFilteringTime_Type = Counter32
_CscaInfoDownStreamAttackFilteringTime_Object = MibTableColumn
cscaInfoDownStreamAttackFilteringTime = _CscaInfoDownStreamAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 3),
    _CscaInfoDownStreamAttackFilteringTime_Type()
)
cscaInfoDownStreamAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaInfoDownStreamAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    cscaInfoDownStreamAttackFilteringTime.setUnits("seconds")
_CscaInfoDownStreamLastAttackFilteringTime_Type = TimeInterval
_CscaInfoDownStreamLastAttackFilteringTime_Object = MibTableColumn
cscaInfoDownStreamLastAttackFilteringTime = _CscaInfoDownStreamLastAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 4),
    _CscaInfoDownStreamLastAttackFilteringTime_Type()
)
cscaInfoDownStreamLastAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscaInfoDownStreamLastAttackFilteringTime.setStatus("current")
_CiscoServiceControlAttackMIBConform_ObjectIdentity = ObjectIdentity
ciscoServiceControlAttackMIBConform = _CiscoServiceControlAttackMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2)
)
_CscaMIBCompliances_ObjectIdentity = ObjectIdentity
cscaMIBCompliances = _CscaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1)
)
_CscaMIBGroups_ObjectIdentity = ObjectIdentity
cscaMIBGroups = _CscaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2)
)

# Managed Objects groups

cscaMIBAttackTypeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 1)
)
cscaMIBAttackTypeObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeCurrentNumAttacks"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumAttacks"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumFlows"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumSeconds"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeOriginatedByNetworkSide"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeProtocol"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIsPortSpecific"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIPsDetected"))
)
if mibBuilder.loadTexts:
    cscaMIBAttackTypeObjectGroup.setStatus("current")

cscaMIBAttackInfoObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 2)
)
cscaMIBAttackInfoObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoUpStreamAttackFilteringTime"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoUpStreamLastAttackFilteringTime"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoDownStreamAttackFilteringTime"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoDownStreamLastAttackFilteringTime"))
)
if mibBuilder.loadTexts:
    cscaMIBAttackInfoObjectGroup.setStatus("current")

cscaFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 4)
)
cscaFilterObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaLastDiscontinuityTimeStamp"))
)
if mibBuilder.loadTexts:
    cscaFilterObjectGroup.setStatus("deprecated")

cscaMIBNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 5)
)
cscaMIBNotifControlGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaNotifsEnabled")
)
if mibBuilder.loadTexts:
    cscaMIBNotifControlGroup.setStatus("deprecated")

cscaFilterObjectGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 7)
)
cscaFilterObjectGroupRev1.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaLastDiscontinuityTimeStamp"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackType"))
)
if mibBuilder.loadTexts:
    cscaFilterObjectGroupRev1.setStatus("current")

cscaMIBNotifControlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 8)
)
cscaMIBNotifControlGroupRev1.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaNotifsEnabled"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackNotifsEnabled"))
)
if mibBuilder.loadTexts:
    cscaMIBNotifControlGroupRev1.setStatus("current")


# Notification objects

cscaFilterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 0, 1)
)
cscaFilterChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"))
)
if mibBuilder.loadTexts:
    cscaFilterChange.setStatus(
        "current"
    )

cscaGlobalAttackFilterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 0, 2)
)
cscaGlobalAttackFilterChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackType"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeOriginatedByNetworkSide"))
)
if mibBuilder.loadTexts:
    cscaGlobalAttackFilterChange.setStatus(
        "current"
    )


# Notifications groups

cscaMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 3)
)
cscaMIBNotificationGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterChange")
)
if mibBuilder.loadTexts:
    cscaMIBNotificationGroup.setStatus(
        "deprecated"
    )

cscaMIBNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 6)
)
cscaMIBNotificationGroupRev1.setObjects(
      *(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterChange"),
        ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackFilterChange"))
)
if mibBuilder.loadTexts:
    cscaMIBNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cscaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cscaMIBCompliance.setStatus(
        "deprecated"
    )

cscaMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cscaMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROL-ATTACK-MIB",
    **{"CscaAttackType": CscaAttackType,
       "ciscoServiceControlAttackMIB": ciscoServiceControlAttackMIB,
       "ciscoServiceControlAttackMIBNotifs": ciscoServiceControlAttackMIBNotifs,
       "cscaFilterChange": cscaFilterChange,
       "cscaGlobalAttackFilterChange": cscaGlobalAttackFilterChange,
       "ciscoServiceControlAttackMIBObjects": ciscoServiceControlAttackMIBObjects,
       "cscaFilterMIBObjects": cscaFilterMIBObjects,
       "cscaType": cscaType,
       "cscaSourceAddressType": cscaSourceAddressType,
       "cscaSourceAddress": cscaSourceAddress,
       "cscaDestinationAddressType": cscaDestinationAddressType,
       "cscaDestinationAddress": cscaDestinationAddress,
       "cscaAttackedPort": cscaAttackedPort,
       "cscaFilterStatus": cscaFilterStatus,
       "cscaNotifsEnabled": cscaNotifsEnabled,
       "cscaLastDiscontinuityTimeStamp": cscaLastDiscontinuityTimeStamp,
       "cscaGlobalAttackType": cscaGlobalAttackType,
       "cscaGlobalAttackNotifsEnabled": cscaGlobalAttackNotifsEnabled,
       "cscaTypeTable": cscaTypeTable,
       "cscaTypeEntry": cscaTypeEntry,
       "cscaTypeIndex": cscaTypeIndex,
       "cscaTypeCurrentNumAttacks": cscaTypeCurrentNumAttacks,
       "cscaTypeTotalNumAttacks": cscaTypeTotalNumAttacks,
       "cscaTypeTotalNumFlows": cscaTypeTotalNumFlows,
       "cscaTypeTotalNumSeconds": cscaTypeTotalNumSeconds,
       "cscaTypeOriginatedByNetworkSide": cscaTypeOriginatedByNetworkSide,
       "cscaTypeProtocol": cscaTypeProtocol,
       "cscaTypeIsPortSpecific": cscaTypeIsPortSpecific,
       "cscaTypeIPsDetected": cscaTypeIPsDetected,
       "cscaInfoTable": cscaInfoTable,
       "cscaInfoEntry": cscaInfoEntry,
       "cscaInfoUpStreamAttackFilteringTime": cscaInfoUpStreamAttackFilteringTime,
       "cscaInfoUpStreamLastAttackFilteringTime": cscaInfoUpStreamLastAttackFilteringTime,
       "cscaInfoDownStreamAttackFilteringTime": cscaInfoDownStreamAttackFilteringTime,
       "cscaInfoDownStreamLastAttackFilteringTime": cscaInfoDownStreamLastAttackFilteringTime,
       "ciscoServiceControlAttackMIBConform": ciscoServiceControlAttackMIBConform,
       "cscaMIBCompliances": cscaMIBCompliances,
       "cscaMIBCompliance": cscaMIBCompliance,
       "cscaMIBComplianceRev1": cscaMIBComplianceRev1,
       "cscaMIBGroups": cscaMIBGroups,
       "cscaMIBAttackTypeObjectGroup": cscaMIBAttackTypeObjectGroup,
       "cscaMIBAttackInfoObjectGroup": cscaMIBAttackInfoObjectGroup,
       "cscaMIBNotificationGroup": cscaMIBNotificationGroup,
       "cscaFilterObjectGroup": cscaFilterObjectGroup,
       "cscaMIBNotifControlGroup": cscaMIBNotifControlGroup,
       "cscaMIBNotificationGroupRev1": cscaMIBNotificationGroupRev1,
       "cscaFilterObjectGroupRev1": cscaFilterObjectGroupRev1,
       "cscaMIBNotifControlGroupRev1": cscaMIBNotifControlGroupRev1}
)
