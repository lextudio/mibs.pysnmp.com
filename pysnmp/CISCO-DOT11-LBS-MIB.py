# SNMP MIB module (CISCO-DOT11-LBS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-LBS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:54 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11LbsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454)
)
ciscoDot11LbsMIB.setRevisions(
        ("2004-11-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cdot11LbsTrackMethodType(Bits, TextualConvention):
    status = "current"


class Cdot11LbsPsPacketType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("short", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDot11LbsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11LbsMIBNotifs = _CiscoDot11LbsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 0)
)
_CiscoDot11LbsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11LbsMIBObjects = _CiscoDot11LbsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1)
)
_CiscoDot11LbsConfigInfo_ObjectIdentity = ObjectIdentity
ciscoDot11LbsConfigInfo = _CiscoDot11LbsConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1)
)
_Cdot11LbsProfileTable_Object = MibTable
cdot11LbsProfileTable = _Cdot11LbsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdot11LbsProfileTable.setStatus("current")
_Cdot11LbsProfileEntry_Object = MibTableRow
cdot11LbsProfileEntry = _Cdot11LbsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1)
)
cdot11LbsProfileEntry.setIndexNames(
    (0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"),
)
if mibBuilder.loadTexts:
    cdot11LbsProfileEntry.setStatus("current")


class _Cdot11LbsProfileName_Type(SnmpAdminString):
    """Custom type cdot11LbsProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Cdot11LbsProfileName_Type.__name__ = "SnmpAdminString"
_Cdot11LbsProfileName_Object = MibTableColumn
cdot11LbsProfileName = _Cdot11LbsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 1),
    _Cdot11LbsProfileName_Type()
)
cdot11LbsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11LbsProfileName.setStatus("current")


class _Cdot11LbsServerAddressType_Type(InetAddressType):
    """Custom type cdot11LbsServerAddressType based on InetAddressType"""


_Cdot11LbsServerAddressType_Object = MibTableColumn
cdot11LbsServerAddressType = _Cdot11LbsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 2),
    _Cdot11LbsServerAddressType_Type()
)
cdot11LbsServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsServerAddressType.setStatus("current")
_Cdot11LbsServerAddress_Type = InetAddress
_Cdot11LbsServerAddress_Object = MibTableColumn
cdot11LbsServerAddress = _Cdot11LbsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 3),
    _Cdot11LbsServerAddress_Type()
)
cdot11LbsServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsServerAddress.setStatus("current")
_Cdot11LbsServerUdpPort_Type = InetPortNumber
_Cdot11LbsServerUdpPort_Object = MibTableColumn
cdot11LbsServerUdpPort = _Cdot11LbsServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 4),
    _Cdot11LbsServerUdpPort_Type()
)
cdot11LbsServerUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsServerUdpPort.setStatus("current")


class _Cdot11LbsTrackMethod_Type(Cdot11LbsTrackMethodType):
    """Custom type cdot11LbsTrackMethod based on Cdot11LbsTrackMethodType"""
    defaultBinValue = "1"


_Cdot11LbsTrackMethod_Object = MibTableColumn
cdot11LbsTrackMethod = _Cdot11LbsTrackMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 5),
    _Cdot11LbsTrackMethod_Type()
)
cdot11LbsTrackMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsTrackMethod.setStatus("current")


class _Cdot11LbsPsPacketType_Type(Cdot11LbsPsPacketType):
    """Custom type cdot11LbsPsPacketType based on Cdot11LbsPsPacketType"""


_Cdot11LbsPsPacketType_Object = MibTableColumn
cdot11LbsPsPacketType = _Cdot11LbsPsPacketType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 6),
    _Cdot11LbsPsPacketType_Type()
)
cdot11LbsPsPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsPsPacketType.setStatus("current")


class _Cdot11LbsTrackMulticast_Type(MacAddress):
    """Custom type cdot11LbsTrackMulticast based on MacAddress"""
    defaultHexValue = "014096000010"


_Cdot11LbsTrackMulticast_Object = MibTableColumn
cdot11LbsTrackMulticast = _Cdot11LbsTrackMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 7),
    _Cdot11LbsTrackMulticast_Type()
)
cdot11LbsTrackMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsTrackMulticast.setStatus("current")


class _Cdot11LbsMatchChannel_Type(TruthValue):
    """Custom type cdot11LbsMatchChannel based on TruthValue"""


_Cdot11LbsMatchChannel_Object = MibTableColumn
cdot11LbsMatchChannel = _Cdot11LbsMatchChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 8),
    _Cdot11LbsMatchChannel_Type()
)
cdot11LbsMatchChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsMatchChannel.setStatus("current")
_Cdot11LbsProfileRowStatus_Type = RowStatus
_Cdot11LbsProfileRowStatus_Object = MibTableColumn
cdot11LbsProfileRowStatus = _Cdot11LbsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 9),
    _Cdot11LbsProfileRowStatus_Type()
)
cdot11LbsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsProfileRowStatus.setStatus("current")
_Cdot11LbsProfInterfaceTable_Object = MibTable
cdot11LbsProfInterfaceTable = _Cdot11LbsProfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdot11LbsProfInterfaceTable.setStatus("current")
_Cdot11LbsProfInterfaceEntry_Object = MibTableRow
cdot11LbsProfInterfaceEntry = _Cdot11LbsProfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1)
)
cdot11LbsProfInterfaceEntry.setIndexNames(
    (0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot11LbsProfInterfaceEntry.setStatus("current")
_Cdot11LbsProfInterfaceRowStatus_Type = RowStatus
_Cdot11LbsProfInterfaceRowStatus_Object = MibTableColumn
cdot11LbsProfInterfaceRowStatus = _Cdot11LbsProfInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1, 1),
    _Cdot11LbsProfInterfaceRowStatus_Type()
)
cdot11LbsProfInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11LbsProfInterfaceRowStatus.setStatus("current")
_CiscoDot11LbsStatistics_ObjectIdentity = ObjectIdentity
ciscoDot11LbsStatistics = _CiscoDot11LbsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 2)
)
_CiscoDot11LbsMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11LbsMIBConformance = _CiscoDot11LbsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 2)
)
_CiscoDot11LbsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11LbsMIBCompliances = _CiscoDot11LbsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1)
)
_CiscoDot11LbsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11LbsMIBGroups = _CiscoDot11LbsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2)
)

# Managed Objects groups

ciscoDot11LbsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2, 1)
)
ciscoDot11LbsConfigGroup.setObjects(
      *(("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddressType"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddress"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerUdpPort"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMethod"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsPsPacketType"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMulticast"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsMatchChannel"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfileRowStatus"),
        ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDot11LbsConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11LbsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11LbsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-LBS-MIB",
    **{"Cdot11LbsTrackMethodType": Cdot11LbsTrackMethodType,
       "Cdot11LbsPsPacketType": Cdot11LbsPsPacketType,
       "ciscoDot11LbsMIB": ciscoDot11LbsMIB,
       "ciscoDot11LbsMIBNotifs": ciscoDot11LbsMIBNotifs,
       "ciscoDot11LbsMIBObjects": ciscoDot11LbsMIBObjects,
       "ciscoDot11LbsConfigInfo": ciscoDot11LbsConfigInfo,
       "cdot11LbsProfileTable": cdot11LbsProfileTable,
       "cdot11LbsProfileEntry": cdot11LbsProfileEntry,
       "cdot11LbsProfileName": cdot11LbsProfileName,
       "cdot11LbsServerAddressType": cdot11LbsServerAddressType,
       "cdot11LbsServerAddress": cdot11LbsServerAddress,
       "cdot11LbsServerUdpPort": cdot11LbsServerUdpPort,
       "cdot11LbsTrackMethod": cdot11LbsTrackMethod,
       "cdot11LbsPsPacketType": cdot11LbsPsPacketType,
       "cdot11LbsTrackMulticast": cdot11LbsTrackMulticast,
       "cdot11LbsMatchChannel": cdot11LbsMatchChannel,
       "cdot11LbsProfileRowStatus": cdot11LbsProfileRowStatus,
       "cdot11LbsProfInterfaceTable": cdot11LbsProfInterfaceTable,
       "cdot11LbsProfInterfaceEntry": cdot11LbsProfInterfaceEntry,
       "cdot11LbsProfInterfaceRowStatus": cdot11LbsProfInterfaceRowStatus,
       "ciscoDot11LbsStatistics": ciscoDot11LbsStatistics,
       "ciscoDot11LbsMIBConformance": ciscoDot11LbsMIBConformance,
       "ciscoDot11LbsMIBCompliances": ciscoDot11LbsMIBCompliances,
       "ciscoDot11LbsMIBCompliance": ciscoDot11LbsMIBCompliance,
       "ciscoDot11LbsMIBGroups": ciscoDot11LbsMIBGroups,
       "ciscoDot11LbsConfigGroup": ciscoDot11LbsConfigGroup}
)
