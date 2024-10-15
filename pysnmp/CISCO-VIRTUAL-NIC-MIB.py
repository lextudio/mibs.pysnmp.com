# SNMP MIB module (CISCO-VIRTUAL-NIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VIRTUAL-NIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:42 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVirtualNicMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710)
)
ciscoVirtualNicMIB.setRevisions(
        ("2009-10-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVirtualNicMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVirtualNicMIBNotifs = _CiscoVirtualNicMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 0)
)
_CiscoVirtualNicMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVirtualNicMIBObjects = _CiscoVirtualNicMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1)
)
_CvnInterfaceObjects_ObjectIdentity = ObjectIdentity
cvnInterfaceObjects = _CvnInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1)
)
_CvnVethIfTable_Object = MibTable
cvnVethIfTable = _CvnVethIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvnVethIfTable.setStatus("current")
_CvnVethIfEntry_Object = MibTableRow
cvnVethIfEntry = _CvnVethIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1)
)
cvnVethIfEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-NIC-MIB", "cvnVethInterface"),
)
if mibBuilder.loadTexts:
    cvnVethIfEntry.setStatus("current")
_CvnVethInterface_Type = InterfaceIndex
_CvnVethInterface_Object = MibTableColumn
cvnVethInterface = _CvnVethInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 1),
    _CvnVethInterface_Type()
)
cvnVethInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvnVethInterface.setStatus("current")
_CvnVethAdapter_Type = SnmpAdminString
_CvnVethAdapter_Object = MibTableColumn
cvnVethAdapter = _CvnVethAdapter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 2),
    _CvnVethAdapter_Type()
)
cvnVethAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethAdapter.setStatus("current")
_CvnVethOwner_Type = SnmpAdminString
_CvnVethOwner_Object = MibTableColumn
cvnVethOwner = _CvnVethOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 3),
    _CvnVethOwner_Type()
)
cvnVethOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethOwner.setStatus("current")
_CvnVethHostID_Type = Unsigned32
_CvnVethHostID_Object = MibTableColumn
cvnVethHostID = _CvnVethHostID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 4),
    _CvnVethHostID_Type()
)
cvnVethHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethHostID.setStatus("current")
_CvnVethHostAddrType_Type = InetAddressType
_CvnVethHostAddrType_Object = MibTableColumn
cvnVethHostAddrType = _CvnVethHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 5),
    _CvnVethHostAddrType_Type()
)
cvnVethHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethHostAddrType.setStatus("current")
_CvnVethHostAddr_Type = InetAddress
_CvnVethHostAddr_Object = MibTableColumn
cvnVethHostAddr = _CvnVethHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 6),
    _CvnVethHostAddr_Type()
)
cvnVethHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethHostAddr.setStatus("current")
_CvnVethPortProfileUsed_Type = SnmpAdminString
_CvnVethPortProfileUsed_Object = MibTableColumn
cvnVethPortProfileUsed = _CvnVethPortProfileUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 7),
    _CvnVethPortProfileUsed_Type()
)
cvnVethPortProfileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethPortProfileUsed.setStatus("current")
_CvnVethIfProfileAlias_Type = SnmpAdminString
_CvnVethIfProfileAlias_Object = MibTableColumn
cvnVethIfProfileAlias = _CvnVethIfProfileAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 8),
    _CvnVethIfProfileAlias_Type()
)
cvnVethIfProfileAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethIfProfileAlias.setStatus("current")


class _CvnVethIfAdditionalState_Type(Integer32):
    """Custom type cvnVethIfAdditionalState based on Integer32"""
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
        *(("errDisabled", 4),
          ("nonParticipating", 5),
          ("none", 1),
          ("participating", 2),
          ("suspended", 3))
    )


_CvnVethIfAdditionalState_Type.__name__ = "Integer32"
_CvnVethIfAdditionalState_Object = MibTableColumn
cvnVethIfAdditionalState = _CvnVethIfAdditionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 9),
    _CvnVethIfAdditionalState_Type()
)
cvnVethIfAdditionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethIfAdditionalState.setStatus("current")
_CvnVethStateReason_Type = SnmpAdminString
_CvnVethStateReason_Object = MibTableColumn
cvnVethStateReason = _CvnVethStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 1, 1, 10),
    _CvnVethStateReason_Type()
)
cvnVethStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnVethStateReason.setStatus("current")
_CvnPinningTable_Object = MibTable
cvnPinningTable = _CvnPinningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvnPinningTable.setStatus("current")
_CvnPinningEntry_Object = MibTableRow
cvnPinningEntry = _CvnPinningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 2, 1)
)
cvnPinningEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-NIC-MIB", "cvnVethInterface"),
)
if mibBuilder.loadTexts:
    cvnPinningEntry.setStatus("current")


class _CvnPinnedSubGrpId_Type(Integer32):
    """Custom type cvnPinnedSubGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CvnPinnedSubGrpId_Type.__name__ = "Integer32"
_CvnPinnedSubGrpId_Object = MibTableColumn
cvnPinnedSubGrpId = _CvnPinnedSubGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 1, 2, 1, 1),
    _CvnPinnedSubGrpId_Type()
)
cvnPinnedSubGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvnPinnedSubGrpId.setStatus("current")
_CvnConnecteeObjects_ObjectIdentity = ObjectIdentity
cvnConnecteeObjects = _CvnConnecteeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2)
)
_CvnConnecteeTable_Object = MibTable
cvnConnecteeTable = _CvnConnecteeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvnConnecteeTable.setStatus("current")
_CvnConnecteeEntry_Object = MibTableRow
cvnConnecteeEntry = _CvnConnecteeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1)
)
cvnConnecteeEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-NIC-MIB", "cvnVethInterface"),
)
if mibBuilder.loadTexts:
    cvnConnecteeEntry.setStatus("current")


class _CvnConnecteeAttachType_Type(Integer32):
    """Custom type cvnConnecteeAttachType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("niv", 3),
          ("none", 1),
          ("vem", 2))
    )


_CvnConnecteeAttachType_Type.__name__ = "Integer32"
_CvnConnecteeAttachType_Object = MibTableColumn
cvnConnecteeAttachType = _CvnConnecteeAttachType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 1),
    _CvnConnecteeAttachType_Type()
)
cvnConnecteeAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeAttachType.setStatus("current")
_CvnDVSPort_Type = Unsigned32
_CvnDVSPort_Object = MibTableColumn
cvnDVSPort = _CvnDVSPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 2),
    _CvnDVSPort_Type()
)
cvnDVSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnDVSPort.setStatus("current")
_CvnConnecteeName_Type = SnmpAdminString
_CvnConnecteeName_Object = MibTableColumn
cvnConnecteeName = _CvnConnecteeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 3),
    _CvnConnecteeName_Type()
)
cvnConnecteeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeName.setStatus("current")
_CvnConnecteeUuid_Type = SnmpAdminString
_CvnConnecteeUuid_Object = MibTableColumn
cvnConnecteeUuid = _CvnConnecteeUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 4),
    _CvnConnecteeUuid_Type()
)
cvnConnecteeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeUuid.setStatus("current")


class _CvnConnecteeType_Type(Integer32):
    """Custom type cvnConnecteeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("vmwareHost", 3),
          ("vmwareVm", 2))
    )


_CvnConnecteeType_Type.__name__ = "Integer32"
_CvnConnecteeType_Object = MibTableColumn
cvnConnecteeType = _CvnConnecteeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 5),
    _CvnConnecteeType_Type()
)
cvnConnecteeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeType.setStatus("current")
_CvnConnecteeMac_Type = MacAddress
_CvnConnecteeMac_Object = MibTableColumn
cvnConnecteeMac = _CvnConnecteeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 6),
    _CvnConnecteeMac_Type()
)
cvnConnecteeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeMac.setStatus("current")
_CvnConnecteeDeviceName_Type = SnmpAdminString
_CvnConnecteeDeviceName_Object = MibTableColumn
cvnConnecteeDeviceName = _CvnConnecteeDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 7),
    _CvnConnecteeDeviceName_Type()
)
cvnConnecteeDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeDeviceName.setStatus("current")


class _CvnConnecteeDeviceType_Type(Integer32):
    """Custom type cvnConnecteeDeviceType based on Integer32"""
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
        *(("pnic", 2),
          ("unknown", 1),
          ("vmknic", 5),
          ("vnic", 3),
          ("vswif", 4))
    )


_CvnConnecteeDeviceType_Type.__name__ = "Integer32"
_CvnConnecteeDeviceType_Object = MibTableColumn
cvnConnecteeDeviceType = _CvnConnecteeDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 1, 2, 1, 1, 8),
    _CvnConnecteeDeviceType_Type()
)
cvnConnecteeDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvnConnecteeDeviceType.setStatus("current")
_CiscoVirtualNicMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVirtualNicMIBConformance = _CiscoVirtualNicMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2)
)
_CiscoVirtualNicMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVirtualNicMIBCompliances = _CiscoVirtualNicMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 1)
)
_CiscoVirtualNicMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVirtualNicMIBGroups = _CiscoVirtualNicMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 2)
)

# Managed Objects groups

cvnVethGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 2, 1)
)
cvnVethGroup.setObjects(
      *(("CISCO-VIRTUAL-NIC-MIB", "cvnVethAdapter"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethOwner"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethHostID"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethHostAddrType"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethHostAddr"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethPortProfileUsed"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethIfProfileAlias"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethIfAdditionalState"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnVethStateReason"))
)
if mibBuilder.loadTexts:
    cvnVethGroup.setStatus("current")

cvnPinningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 2, 2)
)
cvnPinningGroup.setObjects(
    ("CISCO-VIRTUAL-NIC-MIB", "cvnPinnedSubGrpId")
)
if mibBuilder.loadTexts:
    cvnPinningGroup.setStatus("current")

cvnConnecteeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 2, 3)
)
cvnConnecteeGroup.setObjects(
      *(("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeAttachType"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnDVSPort"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeName"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeUuid"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeType"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeMac"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeDeviceName"),
        ("CISCO-VIRTUAL-NIC-MIB", "cvnConnecteeDeviceType"))
)
if mibBuilder.loadTexts:
    cvnConnecteeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

virtualNicMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 710, 2, 1, 1)
)
if mibBuilder.loadTexts:
    virtualNicMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIRTUAL-NIC-MIB",
    **{"ciscoVirtualNicMIB": ciscoVirtualNicMIB,
       "ciscoVirtualNicMIBNotifs": ciscoVirtualNicMIBNotifs,
       "ciscoVirtualNicMIBObjects": ciscoVirtualNicMIBObjects,
       "cvnInterfaceObjects": cvnInterfaceObjects,
       "cvnVethIfTable": cvnVethIfTable,
       "cvnVethIfEntry": cvnVethIfEntry,
       "cvnVethInterface": cvnVethInterface,
       "cvnVethAdapter": cvnVethAdapter,
       "cvnVethOwner": cvnVethOwner,
       "cvnVethHostID": cvnVethHostID,
       "cvnVethHostAddrType": cvnVethHostAddrType,
       "cvnVethHostAddr": cvnVethHostAddr,
       "cvnVethPortProfileUsed": cvnVethPortProfileUsed,
       "cvnVethIfProfileAlias": cvnVethIfProfileAlias,
       "cvnVethIfAdditionalState": cvnVethIfAdditionalState,
       "cvnVethStateReason": cvnVethStateReason,
       "cvnPinningTable": cvnPinningTable,
       "cvnPinningEntry": cvnPinningEntry,
       "cvnPinnedSubGrpId": cvnPinnedSubGrpId,
       "cvnConnecteeObjects": cvnConnecteeObjects,
       "cvnConnecteeTable": cvnConnecteeTable,
       "cvnConnecteeEntry": cvnConnecteeEntry,
       "cvnConnecteeAttachType": cvnConnecteeAttachType,
       "cvnDVSPort": cvnDVSPort,
       "cvnConnecteeName": cvnConnecteeName,
       "cvnConnecteeUuid": cvnConnecteeUuid,
       "cvnConnecteeType": cvnConnecteeType,
       "cvnConnecteeMac": cvnConnecteeMac,
       "cvnConnecteeDeviceName": cvnConnecteeDeviceName,
       "cvnConnecteeDeviceType": cvnConnecteeDeviceType,
       "ciscoVirtualNicMIBConformance": ciscoVirtualNicMIBConformance,
       "ciscoVirtualNicMIBCompliances": ciscoVirtualNicMIBCompliances,
       "virtualNicMIBCompliance": virtualNicMIBCompliance,
       "ciscoVirtualNicMIBGroups": ciscoVirtualNicMIBGroups,
       "cvnVethGroup": cvnVethGroup,
       "cvnPinningGroup": cvnPinningGroup,
       "cvnConnecteeGroup": cvnConnecteeGroup}
)
