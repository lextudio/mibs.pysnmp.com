# SNMP MIB module (CISCO-SDLLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SDLLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:00 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSnaSdllcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28)
)
ciscoSnaSdllcMIB.setRevisions(
        ("1995-08-21 00:00",
         "1998-12-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConvSdllcObjects_ObjectIdentity = ObjectIdentity
convSdllcObjects = _ConvSdllcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1)
)
_ConvSdllcPorts_ObjectIdentity = ObjectIdentity
convSdllcPorts = _ConvSdllcPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1)
)
_ConvSdllcPortTable_Object = MibTable
convSdllcPortTable = _ConvSdllcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    convSdllcPortTable.setStatus("current")
_ConvSdllcPortEntry_Object = MibTableRow
convSdllcPortEntry = _ConvSdllcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1)
)
convSdllcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    convSdllcPortEntry.setStatus("current")
_ConvSdllcPortVirtMacAddr_Type = MacAddress
_ConvSdllcPortVirtMacAddr_Object = MibTableColumn
convSdllcPortVirtMacAddr = _ConvSdllcPortVirtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 1),
    _ConvSdllcPortVirtMacAddr_Type()
)
convSdllcPortVirtMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortVirtMacAddr.setStatus("current")
_ConvSdllcPortVirtRing_Type = Integer32
_ConvSdllcPortVirtRing_Object = MibTableColumn
convSdllcPortVirtRing = _ConvSdllcPortVirtRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 2),
    _ConvSdllcPortVirtRing_Type()
)
convSdllcPortVirtRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortVirtRing.setStatus("current")
_ConvSdllcPortBridge_Type = Integer32
_ConvSdllcPortBridge_Object = MibTableColumn
convSdllcPortBridge = _ConvSdllcPortBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 3),
    _ConvSdllcPortBridge_Type()
)
convSdllcPortBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortBridge.setStatus("current")
_ConvSdllcPortLlc2Ring_Type = Integer32
_ConvSdllcPortLlc2Ring_Object = MibTableColumn
convSdllcPortLlc2Ring = _ConvSdllcPortLlc2Ring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 4),
    _ConvSdllcPortLlc2Ring_Type()
)
convSdllcPortLlc2Ring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortLlc2Ring.setStatus("current")
_ConvSdllcPortLocalAck_Type = TruthValue
_ConvSdllcPortLocalAck_Object = MibTableColumn
convSdllcPortLocalAck = _ConvSdllcPortLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 5),
    _ConvSdllcPortLocalAck_Type()
)
convSdllcPortLocalAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortLocalAck.setStatus("current")


class _ConvSdllcPortLocalAckState_Type(Integer32):
    """Custom type convSdllcPortLocalAckState based on Integer32"""
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
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connectPending", 6),
          ("connected", 7),
          ("disconnected", 1),
          ("localDiscWait", 2),
          ("localWait", 5),
          ("quenched", 10),
          ("remDiscWait", 3),
          ("remQOffWait", 9),
          ("remQOnWait", 8),
          ("remWait", 4),
          ("unknown", 255))
    )


_ConvSdllcPortLocalAckState_Type.__name__ = "Integer32"
_ConvSdllcPortLocalAckState_Object = MibTableColumn
convSdllcPortLocalAckState = _ConvSdllcPortLocalAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 6),
    _ConvSdllcPortLocalAckState_Type()
)
convSdllcPortLocalAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortLocalAckState.setStatus("current")
_ConvSdllcPortMaxLlc2FrameSize_Type = Integer32
_ConvSdllcPortMaxLlc2FrameSize_Object = MibTableColumn
convSdllcPortMaxLlc2FrameSize = _ConvSdllcPortMaxLlc2FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 7),
    _ConvSdllcPortMaxLlc2FrameSize_Type()
)
convSdllcPortMaxLlc2FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcPortMaxLlc2FrameSize.setStatus("current")
_ConvSdllcAddrs_ObjectIdentity = ObjectIdentity
convSdllcAddrs = _ConvSdllcAddrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2)
)
_ConvSdllcAddrTable_Object = MibTable
convSdllcAddrTable = _ConvSdllcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    convSdllcAddrTable.setStatus("current")
_ConvSdllcAddrEntry_Object = MibTableRow
convSdllcAddrEntry = _ConvSdllcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1)
)
convSdllcAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SDLLC-MIB", "convSdllcAddrSdlcAddr"),
)
if mibBuilder.loadTexts:
    convSdllcAddrEntry.setStatus("current")


class _ConvSdllcAddrSdlcAddr_Type(Integer32):
    """Custom type convSdllcAddrSdlcAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConvSdllcAddrSdlcAddr_Type.__name__ = "Integer32"
_ConvSdllcAddrSdlcAddr_Object = MibTableColumn
convSdllcAddrSdlcAddr = _ConvSdllcAddrSdlcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 1),
    _ConvSdllcAddrSdlcAddr_Type()
)
convSdllcAddrSdlcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSdllcAddrSdlcAddr.setStatus("current")
_ConvSdllcAddrPartnerMacAddr_Type = MacAddress
_ConvSdllcAddrPartnerMacAddr_Object = MibTableColumn
convSdllcAddrPartnerMacAddr = _ConvSdllcAddrPartnerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 2),
    _ConvSdllcAddrPartnerMacAddr_Type()
)
convSdllcAddrPartnerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcAddrPartnerMacAddr.setStatus("current")


class _ConvSdllcAddrXID_Type(OctetString):
    """Custom type convSdllcAddrXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ConvSdllcAddrXID_Type.__name__ = "OctetString"
_ConvSdllcAddrXID_Object = MibTableColumn
convSdllcAddrXID = _ConvSdllcAddrXID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 3),
    _ConvSdllcAddrXID_Type()
)
convSdllcAddrXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcAddrXID.setStatus("current")


class _ConvSdllcAddrState_Type(Integer32):
    """Custom type convSdllcAddrState based on Integer32"""
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
        *(("connected", 7),
          ("disconnected", 1),
          ("netConnecting", 5),
          ("netDisconnecting", 4),
          ("sdlcDisconnecting", 2),
          ("sdlcPriConnecting", 3),
          ("sdlcSecConnecting", 6))
    )


_ConvSdllcAddrState_Type.__name__ = "Integer32"
_ConvSdllcAddrState_Object = MibTableColumn
convSdllcAddrState = _ConvSdllcAddrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 4),
    _ConvSdllcAddrState_Type()
)
convSdllcAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcAddrState.setStatus("current")
_ConvSdllcAddrMaxSdlcFrameSize_Type = Integer32
_ConvSdllcAddrMaxSdlcFrameSize_Object = MibTableColumn
convSdllcAddrMaxSdlcFrameSize = _ConvSdllcAddrMaxSdlcFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 5),
    _ConvSdllcAddrMaxSdlcFrameSize_Type()
)
convSdllcAddrMaxSdlcFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSdllcAddrMaxSdlcFrameSize.setStatus("current")
_ConvSdllcNotificationPrefix_ObjectIdentity = ObjectIdentity
convSdllcNotificationPrefix = _ConvSdllcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 2)
)
_ConvSdllcNotifications_ObjectIdentity = ObjectIdentity
convSdllcNotifications = _ConvSdllcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0)
)
_SdllcMibConformance_ObjectIdentity = ObjectIdentity
sdllcMibConformance = _SdllcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3)
)
_SdllcMibCompliances_ObjectIdentity = ObjectIdentity
sdllcMibCompliances = _SdllcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 1)
)
_SdllcMibGroups_ObjectIdentity = ObjectIdentity
sdllcMibGroups = _SdllcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2)
)

# Managed Objects groups

convSdllcPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 1)
)
convSdllcPortGroup.setObjects(
      *(("CISCO-SDLLC-MIB", "convSdllcPortVirtMacAddr"),
        ("CISCO-SDLLC-MIB", "convSdllcPortVirtRing"),
        ("CISCO-SDLLC-MIB", "convSdllcPortBridge"),
        ("CISCO-SDLLC-MIB", "convSdllcPortLlc2Ring"),
        ("CISCO-SDLLC-MIB", "convSdllcPortLocalAck"),
        ("CISCO-SDLLC-MIB", "convSdllcPortLocalAckState"),
        ("CISCO-SDLLC-MIB", "convSdllcPortMaxLlc2FrameSize"))
)
if mibBuilder.loadTexts:
    convSdllcPortGroup.setStatus("current")

convSdllcAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 2)
)
convSdllcAddrGroup.setObjects(
      *(("CISCO-SDLLC-MIB", "convSdllcAddrPartnerMacAddr"),
        ("CISCO-SDLLC-MIB", "convSdllcAddrXID"),
        ("CISCO-SDLLC-MIB", "convSdllcAddrState"),
        ("CISCO-SDLLC-MIB", "convSdllcAddrMaxSdlcFrameSize"))
)
if mibBuilder.loadTexts:
    convSdllcAddrGroup.setStatus("current")


# Notification objects

convSdllcPeerStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0, 1)
)
convSdllcPeerStateChangeNotification.setObjects(
    ("CISCO-SDLLC-MIB", "convSdllcAddrState")
)
if mibBuilder.loadTexts:
    convSdllcPeerStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

sdllcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sdllcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDLLC-MIB",
    **{"ciscoSnaSdllcMIB": ciscoSnaSdllcMIB,
       "convSdllcObjects": convSdllcObjects,
       "convSdllcPorts": convSdllcPorts,
       "convSdllcPortTable": convSdllcPortTable,
       "convSdllcPortEntry": convSdllcPortEntry,
       "convSdllcPortVirtMacAddr": convSdllcPortVirtMacAddr,
       "convSdllcPortVirtRing": convSdllcPortVirtRing,
       "convSdllcPortBridge": convSdllcPortBridge,
       "convSdllcPortLlc2Ring": convSdllcPortLlc2Ring,
       "convSdllcPortLocalAck": convSdllcPortLocalAck,
       "convSdllcPortLocalAckState": convSdllcPortLocalAckState,
       "convSdllcPortMaxLlc2FrameSize": convSdllcPortMaxLlc2FrameSize,
       "convSdllcAddrs": convSdllcAddrs,
       "convSdllcAddrTable": convSdllcAddrTable,
       "convSdllcAddrEntry": convSdllcAddrEntry,
       "convSdllcAddrSdlcAddr": convSdllcAddrSdlcAddr,
       "convSdllcAddrPartnerMacAddr": convSdllcAddrPartnerMacAddr,
       "convSdllcAddrXID": convSdllcAddrXID,
       "convSdllcAddrState": convSdllcAddrState,
       "convSdllcAddrMaxSdlcFrameSize": convSdllcAddrMaxSdlcFrameSize,
       "convSdllcNotificationPrefix": convSdllcNotificationPrefix,
       "convSdllcNotifications": convSdllcNotifications,
       "convSdllcPeerStateChangeNotification": convSdllcPeerStateChangeNotification,
       "sdllcMibConformance": sdllcMibConformance,
       "sdllcMibCompliances": sdllcMibCompliances,
       "sdllcMibCompliance": sdllcMibCompliance,
       "sdllcMibGroups": sdllcMibGroups,
       "convSdllcPortGroup": convSdllcPortGroup,
       "convSdllcAddrGroup": convSdllcAddrGroup}
)
