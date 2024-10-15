# SNMP MIB module (CISCO-VOICE-CONNECTIVITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-CONNECTIVITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:21 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVoiceConnectivityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393)
)
ciscoVoiceConnectivityMIB.setRevisions(
        ("2005-09-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceConnectivityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVoiceConnectivityMIBNotifs = _CiscoVoiceConnectivityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 0)
)
_CiscoVoiceConnectivityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceConnectivityMIBObjects = _CiscoVoiceConnectivityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1)
)
_CvcCallAgent_ObjectIdentity = ObjectIdentity
cvcCallAgent = _CvcCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1)
)
_CvcCallAgentTable_Object = MibTable
cvcCallAgentTable = _CvcCallAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvcCallAgentTable.setStatus("current")
_CvcCallAgentEntry_Object = MibTableRow
cvcCallAgentEntry = _CvcCallAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1)
)
cvcCallAgentEntry.setIndexNames(
    (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"),
)
if mibBuilder.loadTexts:
    cvcCallAgentEntry.setStatus("current")


class _CvcCallAgentIndex_Type(Unsigned32):
    """Custom type cvcCallAgentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvcCallAgentIndex_Type.__name__ = "Unsigned32"
_CvcCallAgentIndex_Object = MibTableColumn
cvcCallAgentIndex = _CvcCallAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 1),
    _CvcCallAgentIndex_Type()
)
cvcCallAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcCallAgentIndex.setStatus("current")


class _CvcCallAgentName_Type(SnmpAdminString):
    """Custom type cvcCallAgentName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvcCallAgentName_Type.__name__ = "SnmpAdminString"
_CvcCallAgentName_Object = MibTableColumn
cvcCallAgentName = _CvcCallAgentName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 2),
    _CvcCallAgentName_Type()
)
cvcCallAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcCallAgentName.setStatus("current")
_CvcCallAgentInetAddressType_Type = InetAddressType
_CvcCallAgentInetAddressType_Object = MibTableColumn
cvcCallAgentInetAddressType = _CvcCallAgentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 3),
    _CvcCallAgentInetAddressType_Type()
)
cvcCallAgentInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcCallAgentInetAddressType.setStatus("current")
_CvcCallAgentInetAddress_Type = InetAddress
_CvcCallAgentInetAddress_Object = MibTableColumn
cvcCallAgentInetAddress = _CvcCallAgentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 4),
    _CvcCallAgentInetAddress_Type()
)
cvcCallAgentInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcCallAgentInetAddress.setStatus("current")
_CvcCallAgentType_Type = AutonomousType
_CvcCallAgentType_Object = MibTableColumn
cvcCallAgentType = _CvcCallAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 5),
    _CvcCallAgentType_Type()
)
cvcCallAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcCallAgentType.setStatus("current")
_CvcPort_ObjectIdentity = ObjectIdentity
cvcPort = _CvcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2)
)
_CvcPortTable_Object = MibTable
cvcPortTable = _CvcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvcPortTable.setStatus("current")
_CvcPortEntry_Object = MibTableRow
cvcPortEntry = _CvcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1)
)
cvcPortEntry.setIndexNames(
    (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"),
)
if mibBuilder.loadTexts:
    cvcPortEntry.setStatus("current")


class _CvcPortIndex_Type(Unsigned32):
    """Custom type cvcPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CvcPortIndex_Type.__name__ = "Unsigned32"
_CvcPortIndex_Object = MibTableColumn
cvcPortIndex = _CvcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 1),
    _CvcPortIndex_Type()
)
cvcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcPortIndex.setStatus("current")
_CvcPortAssociation_Type = RowPointer
_CvcPortAssociation_Object = MibTableColumn
cvcPortAssociation = _CvcPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 2),
    _CvcPortAssociation_Type()
)
cvcPortAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortAssociation.setStatus("current")
_CvcPortDeviceName_Type = SnmpAdminString
_CvcPortDeviceName_Object = MibTableColumn
cvcPortDeviceName = _CvcPortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 3),
    _CvcPortDeviceName_Type()
)
cvcPortDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortDeviceName.setStatus("current")
_CvcPortInetAddressType_Type = InetAddressType
_CvcPortInetAddressType_Object = MibTableColumn
cvcPortInetAddressType = _CvcPortInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 4),
    _CvcPortInetAddressType_Type()
)
cvcPortInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortInetAddressType.setStatus("current")
_CvcPortInetAddress_Type = InetAddress
_CvcPortInetAddress_Object = MibTableColumn
cvcPortInetAddress = _CvcPortInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 5),
    _CvcPortInetAddress_Type()
)
cvcPortInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortInetAddress.setStatus("current")
_CvcPortMACAddress_Type = MacAddress
_CvcPortMACAddress_Object = MibTableColumn
cvcPortMACAddress = _CvcPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 6),
    _CvcPortMACAddress_Type()
)
cvcPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortMACAddress.setStatus("current")
_CvcPortType_Type = IANAifType
_CvcPortType_Object = MibTableColumn
cvcPortType = _CvcPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 7),
    _CvcPortType_Type()
)
cvcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcPortType.setStatus("current")


class _CvcProductCategory_Type(Integer32):
    """Custom type cvcProductCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ctiDevice", 4),
          ("gateway", 2),
          ("h323Device", 3),
          ("huntListDevice", 7),
          ("mediaResourceDevice", 6),
          ("phone", 1),
          ("sipDevice", 8),
          ("voiceMailDevice", 5))
    )


_CvcProductCategory_Type.__name__ = "Integer32"
_CvcProductCategory_Object = MibTableColumn
cvcProductCategory = _CvcProductCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 8),
    _CvcProductCategory_Type()
)
cvcProductCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcProductCategory.setStatus("current")


class _CvcProtocol_Type(Integer32):
    """Custom type cvcProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("h323", 4),
          ("mgcp", 3),
          ("sccp", 1),
          ("sgcp", 2),
          ("sip", 5))
    )


_CvcProtocol_Type.__name__ = "Integer32"
_CvcProtocol_Object = MibTableColumn
cvcProtocol = _CvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 9),
    _CvcProtocol_Type()
)
cvcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcProtocol.setStatus("current")
_CvcVirtualInterfaceDN_Type = SnmpAdminString
_CvcVirtualInterfaceDN_Object = MibTableColumn
cvcVirtualInterfaceDN = _CvcVirtualInterfaceDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 10),
    _CvcVirtualInterfaceDN_Type()
)
cvcVirtualInterfaceDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcVirtualInterfaceDN.setStatus("current")
_CvcCallAgentConnection_ObjectIdentity = ObjectIdentity
cvcCallAgentConnection = _CvcCallAgentConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3)
)
_CvcCallAgentConnectionTable_Object = MibTable
cvcCallAgentConnectionTable = _CvcCallAgentConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvcCallAgentConnectionTable.setStatus("current")
_CvcCallAgentConnectionEntry_Object = MibTableRow
cvcCallAgentConnectionEntry = _CvcCallAgentConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1)
)
cvcCallAgentConnectionEntry.setIndexNames(
    (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"),
    (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"),
)
if mibBuilder.loadTexts:
    cvcCallAgentConnectionEntry.setStatus("current")
_CvcCallAgentPriority_Type = Unsigned32
_CvcCallAgentPriority_Object = MibTableColumn
cvcCallAgentPriority = _CvcCallAgentPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 1),
    _CvcCallAgentPriority_Type()
)
cvcCallAgentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcCallAgentPriority.setStatus("current")


class _CvcRegistrationStatus_Type(Integer32):
    """Custom type cvcRegistrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notapplicable", 2),
          ("registered", 3),
          ("rejected", 5),
          ("unknown", 1),
          ("unregistered", 4))
    )


_CvcRegistrationStatus_Type.__name__ = "Integer32"
_CvcRegistrationStatus_Object = MibTableColumn
cvcRegistrationStatus = _CvcRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 2),
    _CvcRegistrationStatus_Type()
)
cvcRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcRegistrationStatus.setStatus("current")


class _CvcStatusReason_Type(Integer32):
    """Custom type cvcStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("configurationError", 3),
          ("connectivityError", 6),
          ("deviceNameUnresolveable", 4),
          ("deviceReset", 8),
          ("initializationError", 7),
          ("maxDevRegReached", 5),
          ("noError", 1),
          ("unknown", 2))
    )


_CvcStatusReason_Type.__name__ = "Integer32"
_CvcStatusReason_Object = MibTableColumn
cvcStatusReason = _CvcStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 3),
    _CvcStatusReason_Type()
)
cvcStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcStatusReason.setStatus("current")
_CvcLastStatusChangeTime_Type = DateAndTime
_CvcLastStatusChangeTime_Object = MibTableColumn
cvcLastStatusChangeTime = _CvcLastStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 4),
    _CvcLastStatusChangeTime_Type()
)
cvcLastStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcLastStatusChangeTime.setStatus("current")
_CvcLastRegisteredTime_Type = DateAndTime
_CvcLastRegisteredTime_Object = MibTableColumn
cvcLastRegisteredTime = _CvcLastRegisteredTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 5),
    _CvcLastRegisteredTime_Type()
)
cvcLastRegisteredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcLastRegisteredTime.setStatus("current")
_CvcNotif_ObjectIdentity = ObjectIdentity
cvcNotif = _CvcNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4)
)


class _CvcNotifEnable_Type(TruthValue):
    """Custom type cvcNotifEnable based on TruthValue"""


_CvcNotifEnable_Object = MibScalar
cvcNotifEnable = _CvcNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4, 1),
    _CvcNotifEnable_Type()
)
cvcNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvcNotifEnable.setStatus("current")
_CiscoVoiceConnectivityMIBConform_ObjectIdentity = ObjectIdentity
ciscoVoiceConnectivityMIBConform = _CiscoVoiceConnectivityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2)
)
_CvcMIBCompliances_ObjectIdentity = ObjectIdentity
cvcMIBCompliances = _CvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1)
)
_CvcMIBGroups_ObjectIdentity = ObjectIdentity
cvcMIBGroups = _CvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2)
)

# Managed Objects groups

cvcCallAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 1)
)
cvcCallAgentGroup.setObjects(
      *(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentName"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddressType"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentType"))
)
if mibBuilder.loadTexts:
    cvcCallAgentGroup.setStatus("current")

cvcPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 2)
)
cvcPortGroup.setObjects(
      *(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortAssociation"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddressType"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddress"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortMACAddress"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortType"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProductCategory"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProtocol"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcVirtualInterfaceDN"))
)
if mibBuilder.loadTexts:
    cvcPortGroup.setStatus("current")

cvcCallAgentConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 3)
)
cvcCallAgentConnectionGroup.setObjects(
      *(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
)
if mibBuilder.loadTexts:
    cvcCallAgentConnectionGroup.setStatus("current")

cvcNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 4)
)
cvcNotifGroup.setObjects(
    ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotifEnable")
)
if mibBuilder.loadTexts:
    cvcNotifGroup.setStatus("current")


# Notification objects

cvcPortRegistrationStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 0, 1)
)
cvcPortRegistrationStatusChange.setObjects(
      *(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"),
        ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
)
if mibBuilder.loadTexts:
    cvcPortRegistrationStatusChange.setStatus(
        "current"
    )


# Notifications groups

cvcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 5)
)
cvcNotificationsGroup.setObjects(
    ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortRegistrationStatusChange")
)
if mibBuilder.loadTexts:
    cvcNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-CONNECTIVITY-MIB",
    **{"ciscoVoiceConnectivityMIB": ciscoVoiceConnectivityMIB,
       "ciscoVoiceConnectivityMIBNotifs": ciscoVoiceConnectivityMIBNotifs,
       "cvcPortRegistrationStatusChange": cvcPortRegistrationStatusChange,
       "ciscoVoiceConnectivityMIBObjects": ciscoVoiceConnectivityMIBObjects,
       "cvcCallAgent": cvcCallAgent,
       "cvcCallAgentTable": cvcCallAgentTable,
       "cvcCallAgentEntry": cvcCallAgentEntry,
       "cvcCallAgentIndex": cvcCallAgentIndex,
       "cvcCallAgentName": cvcCallAgentName,
       "cvcCallAgentInetAddressType": cvcCallAgentInetAddressType,
       "cvcCallAgentInetAddress": cvcCallAgentInetAddress,
       "cvcCallAgentType": cvcCallAgentType,
       "cvcPort": cvcPort,
       "cvcPortTable": cvcPortTable,
       "cvcPortEntry": cvcPortEntry,
       "cvcPortIndex": cvcPortIndex,
       "cvcPortAssociation": cvcPortAssociation,
       "cvcPortDeviceName": cvcPortDeviceName,
       "cvcPortInetAddressType": cvcPortInetAddressType,
       "cvcPortInetAddress": cvcPortInetAddress,
       "cvcPortMACAddress": cvcPortMACAddress,
       "cvcPortType": cvcPortType,
       "cvcProductCategory": cvcProductCategory,
       "cvcProtocol": cvcProtocol,
       "cvcVirtualInterfaceDN": cvcVirtualInterfaceDN,
       "cvcCallAgentConnection": cvcCallAgentConnection,
       "cvcCallAgentConnectionTable": cvcCallAgentConnectionTable,
       "cvcCallAgentConnectionEntry": cvcCallAgentConnectionEntry,
       "cvcCallAgentPriority": cvcCallAgentPriority,
       "cvcRegistrationStatus": cvcRegistrationStatus,
       "cvcStatusReason": cvcStatusReason,
       "cvcLastStatusChangeTime": cvcLastStatusChangeTime,
       "cvcLastRegisteredTime": cvcLastRegisteredTime,
       "cvcNotif": cvcNotif,
       "cvcNotifEnable": cvcNotifEnable,
       "ciscoVoiceConnectivityMIBConform": ciscoVoiceConnectivityMIBConform,
       "cvcMIBCompliances": cvcMIBCompliances,
       "cvcMIBCompliance": cvcMIBCompliance,
       "cvcMIBGroups": cvcMIBGroups,
       "cvcCallAgentGroup": cvcCallAgentGroup,
       "cvcPortGroup": cvcPortGroup,
       "cvcCallAgentConnectionGroup": cvcCallAgentConnectionGroup,
       "cvcNotifGroup": cvcNotifGroup,
       "cvcNotificationsGroup": cvcNotificationsGroup}
)
