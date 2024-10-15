# SNMP MIB module (CISCO-TCPOFFLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TCPOFFLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:35 2024
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

(cipCardDtrBrdIndex,
 cipCardEntryIndex,
 cipCardSubChannelIndex) = mibBuilder.importSymbols(
    "CISCO-CHANNEL-MIB",
    "cipCardDtrBrdIndex",
    "cipCardEntryIndex",
    "cipCardSubChannelIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "RowStatus",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTcpOffloadMIB_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMIB = _CiscoTcpOffloadMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31)
)
_TcpOffloadObjects_ObjectIdentity = ObjectIdentity
tcpOffloadObjects = _TcpOffloadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1)
)
_CipCardOffloadConfig_ObjectIdentity = ObjectIdentity
cipCardOffloadConfig = _CipCardOffloadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1)
)
_CipCardOffloadConfigTable_Object = MibTable
cipCardOffloadConfigTable = _CipCardOffloadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipCardOffloadConfigTable.setStatus("mandatory")
_CipCardOffloadConfigEntry_Object = MibTableRow
cipCardOffloadConfigEntry = _CipCardOffloadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1)
)
cipCardOffloadConfigEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardOffloadConfigEntry.setStatus("mandatory")


class _CipCardOffloadConfigPath_Type(OctetString):
    """Custom type cipCardOffloadConfigPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CipCardOffloadConfigPath_Type.__name__ = "OctetString"
_CipCardOffloadConfigPath_Object = MibTableColumn
cipCardOffloadConfigPath = _CipCardOffloadConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 1),
    _CipCardOffloadConfigPath_Type()
)
cipCardOffloadConfigPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigPath.setStatus("mandatory")


class _CipCardOffloadConfigDevice_Type(OctetString):
    """Custom type cipCardOffloadConfigDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CipCardOffloadConfigDevice_Type.__name__ = "OctetString"
_CipCardOffloadConfigDevice_Object = MibTableColumn
cipCardOffloadConfigDevice = _CipCardOffloadConfigDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 2),
    _CipCardOffloadConfigDevice_Type()
)
cipCardOffloadConfigDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigDevice.setStatus("mandatory")
_CipCardOffloadConfigIpAddr_Type = IpAddress
_CipCardOffloadConfigIpAddr_Object = MibTableColumn
cipCardOffloadConfigIpAddr = _CipCardOffloadConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 3),
    _CipCardOffloadConfigIpAddr_Type()
)
cipCardOffloadConfigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigIpAddr.setStatus("mandatory")


class _CipCardOffloadConfigHostName_Type(DisplayString):
    """Custom type cipCardOffloadConfigHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigHostName_Type.__name__ = "DisplayString"
_CipCardOffloadConfigHostName_Object = MibTableColumn
cipCardOffloadConfigHostName = _CipCardOffloadConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 4),
    _CipCardOffloadConfigHostName_Type()
)
cipCardOffloadConfigHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigHostName.setStatus("mandatory")


class _CipCardOffloadConfigRouterName_Type(DisplayString):
    """Custom type cipCardOffloadConfigRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigRouterName_Type.__name__ = "DisplayString"
_CipCardOffloadConfigRouterName_Object = MibTableColumn
cipCardOffloadConfigRouterName = _CipCardOffloadConfigRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 5),
    _CipCardOffloadConfigRouterName_Type()
)
cipCardOffloadConfigRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigRouterName.setStatus("mandatory")


class _CipCardOffloadConfigLinkHostAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigLinkHostAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigLinkHostAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigLinkHostAppl_Object = MibTableColumn
cipCardOffloadConfigLinkHostAppl = _CipCardOffloadConfigLinkHostAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 6),
    _CipCardOffloadConfigLinkHostAppl_Type()
)
cipCardOffloadConfigLinkHostAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigLinkHostAppl.setStatus("mandatory")


class _CipCardOffloadConfigLinkRouterAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigLinkRouterAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigLinkRouterAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigLinkRouterAppl_Object = MibTableColumn
cipCardOffloadConfigLinkRouterAppl = _CipCardOffloadConfigLinkRouterAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 7),
    _CipCardOffloadConfigLinkRouterAppl_Type()
)
cipCardOffloadConfigLinkRouterAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigLinkRouterAppl.setStatus("mandatory")


class _CipCardOffloadConfigAPIHostAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigAPIHostAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigAPIHostAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigAPIHostAppl_Object = MibTableColumn
cipCardOffloadConfigAPIHostAppl = _CipCardOffloadConfigAPIHostAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 8),
    _CipCardOffloadConfigAPIHostAppl_Type()
)
cipCardOffloadConfigAPIHostAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigAPIHostAppl.setStatus("mandatory")


class _CipCardOffloadConfigAPIRouterAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigAPIRouterAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigAPIRouterAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigAPIRouterAppl_Object = MibTableColumn
cipCardOffloadConfigAPIRouterAppl = _CipCardOffloadConfigAPIRouterAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 9),
    _CipCardOffloadConfigAPIRouterAppl_Type()
)
cipCardOffloadConfigAPIRouterAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigAPIRouterAppl.setStatus("mandatory")
_CipCardOffloadConfigBroadcastEnable_Type = TruthValue
_CipCardOffloadConfigBroadcastEnable_Object = MibTableColumn
cipCardOffloadConfigBroadcastEnable = _CipCardOffloadConfigBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 10),
    _CipCardOffloadConfigBroadcastEnable_Type()
)
cipCardOffloadConfigBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigBroadcastEnable.setStatus("mandatory")
_CipCardOffloadConfigRowStatus_Type = RowStatus
_CipCardOffloadConfigRowStatus_Object = MibTableColumn
cipCardOffloadConfigRowStatus = _CipCardOffloadConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 11),
    _CipCardOffloadConfigRowStatus_Type()
)
cipCardOffloadConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardOffloadConfigRowStatus.setStatus("mandatory")
_CiscoTcpOffloadMibConformance_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibConformance = _CiscoTcpOffloadMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2)
)
_CiscoTcpOffloadMibCompliances_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibCompliances = _CiscoTcpOffloadMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 1)
)
_CiscoTcpOffloadMibCompliance_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibCompliance = _CiscoTcpOffloadMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 1, 1)
)
_CiscoTcpOffloadMibGroups_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibGroups = _CiscoTcpOffloadMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 2)
)
_CiscoTcpOffloadGroup_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadGroup = _CiscoTcpOffloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TCPOFFLOAD-MIB",
    **{"ciscoTcpOffloadMIB": ciscoTcpOffloadMIB,
       "tcpOffloadObjects": tcpOffloadObjects,
       "cipCardOffloadConfig": cipCardOffloadConfig,
       "cipCardOffloadConfigTable": cipCardOffloadConfigTable,
       "cipCardOffloadConfigEntry": cipCardOffloadConfigEntry,
       "cipCardOffloadConfigPath": cipCardOffloadConfigPath,
       "cipCardOffloadConfigDevice": cipCardOffloadConfigDevice,
       "cipCardOffloadConfigIpAddr": cipCardOffloadConfigIpAddr,
       "cipCardOffloadConfigHostName": cipCardOffloadConfigHostName,
       "cipCardOffloadConfigRouterName": cipCardOffloadConfigRouterName,
       "cipCardOffloadConfigLinkHostAppl": cipCardOffloadConfigLinkHostAppl,
       "cipCardOffloadConfigLinkRouterAppl": cipCardOffloadConfigLinkRouterAppl,
       "cipCardOffloadConfigAPIHostAppl": cipCardOffloadConfigAPIHostAppl,
       "cipCardOffloadConfigAPIRouterAppl": cipCardOffloadConfigAPIRouterAppl,
       "cipCardOffloadConfigBroadcastEnable": cipCardOffloadConfigBroadcastEnable,
       "cipCardOffloadConfigRowStatus": cipCardOffloadConfigRowStatus,
       "ciscoTcpOffloadMibConformance": ciscoTcpOffloadMibConformance,
       "ciscoTcpOffloadMibCompliances": ciscoTcpOffloadMibCompliances,
       "ciscoTcpOffloadMibCompliance": ciscoTcpOffloadMibCompliance,
       "ciscoTcpOffloadMibGroups": ciscoTcpOffloadMibGroups,
       "ciscoTcpOffloadGroup": ciscoTcpOffloadGroup}
)
