# SNMP MIB module (ALCATEL-IND1-EVB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-EVB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:02 2024
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

(softentIND1EvbMib,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1EvbMib")

(TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")

(ieee8021BridgeEvbSbpPortNumber,
 ieee8021BridgeEvbVSIID,
 ieee8021BridgeEvbVSIIDType,
 ieee8021BridgeEvbVSIMvFormat,
 ieee8021BridgeEvbVSITypeVersion,
 ieee8021BridgeEvbVSIVlanId) = mibBuilder.importSymbols(
    "IEEE8021-EVBB-MIB",
    "ieee8021BridgeEvbSbpPortNumber",
    "ieee8021BridgeEvbVSIID",
    "ieee8021BridgeEvbVSIIDType",
    "ieee8021BridgeEvbVSIMvFormat",
    "ieee8021BridgeEvbVSITypeVersion",
    "ieee8021BridgeEvbVSIVlanId")

(IEEE8021BridgePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1EVBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1)
)
alcatelIND1EVBMIB.setRevisions(
        ("2011-07-11 00:00",
         "2011-07-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1EvbMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1EvbMIBObjects = _AlcatelIND1EvbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EvbMIBObjects.setStatus("current")
_EvbMIBNotifications_ObjectIdentity = ObjectIdentity
evbMIBNotifications = _EvbMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0)
)
_EvbMIBScalarObjects_ObjectIdentity = ObjectIdentity
evbMIBScalarObjects = _EvbMIBScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1)
)


class _EvbPortAutoMode_Type(Integer32):
    """Custom type evbPortAutoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EvbPortAutoMode_Type.__name__ = "Integer32"
_EvbPortAutoMode_Object = MibScalar
evbPortAutoMode = _EvbPortAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1, 1),
    _EvbPortAutoMode_Type()
)
evbPortAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evbPortAutoMode.setStatus("current")


class _EvbDefaultType_Type(Integer32):
    """Custom type evbDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceAccess", 2),
          ("undefined", 0),
          ("vlanBridging", 1))
    )


_EvbDefaultType_Type.__name__ = "Integer32"
_EvbDefaultType_Object = MibScalar
evbDefaultType = _EvbDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1, 2),
    _EvbDefaultType_Type()
)
evbDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evbDefaultType.setStatus("current")
_EvbSapMIB_ObjectIdentity = ObjectIdentity
evbSapMIB = _EvbSapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2)
)
_EvbVSISAPTable_Object = MibTable
evbVSISAPTable = _EvbVSISAPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    evbVSISAPTable.setStatus("current")
_EvbVSISAPEntry_Object = MibTableRow
evbVSISAPEntry = _EvbVSISAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1)
)
evbVSISAPEntry.setIndexNames(
    (0, "ALCATEL-IND1-EVB-MIB", "evbVSIPortNumber"),
    (0, "ALCATEL-IND1-EVB-MIB", "evbVSIID"),
    (0, "ALCATEL-IND1-EVB-MIB", "evbVSIVlanID"),
)
if mibBuilder.loadTexts:
    evbVSISAPEntry.setStatus("current")
_EvbVSIPortNumber_Type = IEEE8021BridgePortNumber
_EvbVSIPortNumber_Object = MibTableColumn
evbVSIPortNumber = _EvbVSIPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 1),
    _EvbVSIPortNumber_Type()
)
evbVSIPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evbVSIPortNumber.setStatus("current")


class _EvbVSIID_Type(OctetString):
    """Custom type evbVSIID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EvbVSIID_Type.__name__ = "OctetString"
_EvbVSIID_Object = MibTableColumn
evbVSIID = _EvbVSIID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 2),
    _EvbVSIID_Type()
)
evbVSIID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evbVSIID.setStatus("current")
_EvbVSIVlanID_Type = VlanIndex
_EvbVSIVlanID_Object = MibTableColumn
evbVSIVlanID = _EvbVSIVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 3),
    _EvbVSIVlanID_Type()
)
evbVSIVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evbVSIVlanID.setStatus("current")
_EvbSAPPortId_Type = TmnxPortID
_EvbSAPPortId_Object = MibTableColumn
evbSAPPortId = _EvbSAPPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 4),
    _EvbSAPPortId_Type()
)
evbSAPPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evbSAPPortId.setStatus("current")


class _EvbSAPServiceType_Type(Integer32):
    """Custom type evbSAPServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spb", 1),
          ("vpls", 2))
    )


_EvbSAPServiceType_Type.__name__ = "Integer32"
_EvbSAPServiceType_Object = MibTableColumn
evbSAPServiceType = _EvbSAPServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 5),
    _EvbSAPServiceType_Type()
)
evbSAPServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evbSAPServiceType.setStatus("current")
_EvbSAPEncapValue_Type = TmnxEncapVal
_EvbSAPEncapValue_Object = MibTableColumn
evbSAPEncapValue = _EvbSAPEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 6),
    _EvbSAPEncapValue_Type()
)
evbSAPEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evbSAPEncapValue.setStatus("current")
_EvbSAPServiceId_Type = TmnxServId
_EvbSAPServiceId_Object = MibTableColumn
evbSAPServiceId = _EvbSAPServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 7),
    _EvbSAPServiceId_Type()
)
evbSAPServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evbSAPServiceId.setStatus("current")
_EvbPortModeTable_Object = MibTable
evbPortModeTable = _EvbPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    evbPortModeTable.setStatus("current")
_EvbPortModeEntry_Object = MibTableRow
evbPortModeEntry = _EvbPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1)
)
evbPortModeEntry.setIndexNames(
    (0, "ALCATEL-IND1-EVB-MIB", "evbPortId"),
)
if mibBuilder.loadTexts:
    evbPortModeEntry.setStatus("current")
_EvbPortId_Type = InterfaceIndex
_EvbPortId_Object = MibTableColumn
evbPortId = _EvbPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 1),
    _EvbPortId_Type()
)
evbPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evbPortId.setStatus("current")


class _EvbPortMode_Type(Integer32):
    """Custom type evbPortMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("undefined", 0),
          ("vlan", 1))
    )


_EvbPortMode_Type.__name__ = "Integer32"
_EvbPortMode_Object = MibTableColumn
evbPortMode = _EvbPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 2),
    _EvbPortMode_Type()
)
evbPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    evbPortMode.setStatus("current")


class _EvbRowStatus_Type(RowStatus):
    """Custom type evbRowStatus based on RowStatus"""


_EvbRowStatus_Object = MibTableColumn
evbRowStatus = _EvbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 3),
    _EvbRowStatus_Type()
)
evbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    evbRowStatus.setStatus("current")
_AlcatelIND1EvbMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1EvbMIBConformance = _AlcatelIND1EvbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EvbMIBConformance.setStatus("current")
_AlcatelIND1EvbMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1EvbMIBGroups = _AlcatelIND1EvbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EvbMIBGroups.setStatus("current")
_AlcatelIND1EvbMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1EvbMIBCompliances = _AlcatelIND1EvbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EvbMIBCompliances.setStatus("current")

# Managed Objects groups

alaEvbModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1, 1)
)
alaEvbModuleGroup.setObjects(
      *(("ALCATEL-IND1-EVB-MIB", "evbPortAutoMode"),
        ("ALCATEL-IND1-EVB-MIB", "evbDefaultType"),
        ("ALCATEL-IND1-EVB-MIB", "evbSAPEncapValue"),
        ("ALCATEL-IND1-EVB-MIB", "evbSAPPortId"),
        ("ALCATEL-IND1-EVB-MIB", "evbSAPServiceType"),
        ("ALCATEL-IND1-EVB-MIB", "evbSAPServiceId"),
        ("ALCATEL-IND1-EVB-MIB", "evbPortMode"),
        ("ALCATEL-IND1-EVB-MIB", "evbRowStatus"))
)
if mibBuilder.loadTexts:
    alaEvbModuleGroup.setStatus("current")


# Notification objects

evbFailedCdcpTlvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 1)
)
evbFailedCdcpTlvTrap.setObjects(
    ("ALCATEL-IND1-EVB-MIB", "evbPortId")
)
if mibBuilder.loadTexts:
    evbFailedCdcpTlvTrap.setStatus(
        "current"
    )

evbFailedEvbTlvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 2)
)
evbFailedEvbTlvTrap.setObjects(
      *(("ALCATEL-IND1-EVB-MIB", "evbPortId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIVlanId"))
)
if mibBuilder.loadTexts:
    evbFailedEvbTlvTrap.setStatus(
        "current"
    )

evbUnknownVsiManagerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 3)
)
evbUnknownVsiManagerTrap.setObjects(
      *(("ALCATEL-IND1-EVB-MIB", "evbPortId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSbpPortNumber"))
)
if mibBuilder.loadTexts:
    evbUnknownVsiManagerTrap.setStatus(
        "current"
    )

evbVdpAssocTlvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 4)
)
evbVdpAssocTlvTrap.setObjects(
      *(("ALCATEL-IND1-EVB-MIB", "evbPortId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSbpPortNumber"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIID"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIIDType"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSITypeVersion"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIMvFormat"))
)
if mibBuilder.loadTexts:
    evbVdpAssocTlvTrap.setStatus(
        "current"
    )

evbCdcpLldpExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    evbCdcpLldpExpiredTrap.setStatus(
        "current"
    )

evbTlvExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 6)
)
if mibBuilder.loadTexts:
    evbTlvExpiredTrap.setStatus(
        "current"
    )

evbVdpKeepaliveExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 7)
)
if mibBuilder.loadTexts:
    evbVdpKeepaliveExpiredTrap.setStatus(
        "current"
    )


# Notifications groups

alaEvbNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1, 2)
)
alaEvbNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-EVB-MIB", "evbFailedEvbTlvTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbFailedCdcpTlvTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbVdpAssocTlvTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbCdcpLldpExpiredTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbTlvExpiredTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbUnknownVsiManagerTrap"),
        ("ALCATEL-IND1-EVB-MIB", "evbVdpKeepaliveExpiredTrap"))
)
if mibBuilder.loadTexts:
    alaEvbNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1EvbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EvbMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-EVB-MIB",
    **{"alcatelIND1EVBMIB": alcatelIND1EVBMIB,
       "alcatelIND1EvbMIBObjects": alcatelIND1EvbMIBObjects,
       "evbMIBNotifications": evbMIBNotifications,
       "evbFailedCdcpTlvTrap": evbFailedCdcpTlvTrap,
       "evbFailedEvbTlvTrap": evbFailedEvbTlvTrap,
       "evbUnknownVsiManagerTrap": evbUnknownVsiManagerTrap,
       "evbVdpAssocTlvTrap": evbVdpAssocTlvTrap,
       "evbCdcpLldpExpiredTrap": evbCdcpLldpExpiredTrap,
       "evbTlvExpiredTrap": evbTlvExpiredTrap,
       "evbVdpKeepaliveExpiredTrap": evbVdpKeepaliveExpiredTrap,
       "evbMIBScalarObjects": evbMIBScalarObjects,
       "evbPortAutoMode": evbPortAutoMode,
       "evbDefaultType": evbDefaultType,
       "evbSapMIB": evbSapMIB,
       "evbVSISAPTable": evbVSISAPTable,
       "evbVSISAPEntry": evbVSISAPEntry,
       "evbVSIPortNumber": evbVSIPortNumber,
       "evbVSIID": evbVSIID,
       "evbVSIVlanID": evbVSIVlanID,
       "evbSAPPortId": evbSAPPortId,
       "evbSAPServiceType": evbSAPServiceType,
       "evbSAPEncapValue": evbSAPEncapValue,
       "evbSAPServiceId": evbSAPServiceId,
       "evbPortModeTable": evbPortModeTable,
       "evbPortModeEntry": evbPortModeEntry,
       "evbPortId": evbPortId,
       "evbPortMode": evbPortMode,
       "evbRowStatus": evbRowStatus,
       "alcatelIND1EvbMIBConformance": alcatelIND1EvbMIBConformance,
       "alcatelIND1EvbMIBGroups": alcatelIND1EvbMIBGroups,
       "alaEvbModuleGroup": alaEvbModuleGroup,
       "alaEvbNotificationsGroup": alaEvbNotificationsGroup,
       "alcatelIND1EvbMIBCompliances": alcatelIND1EvbMIBCompliances,
       "alcatelIND1EvbMIBCompliance": alcatelIND1EvbMIBCompliance}
)
