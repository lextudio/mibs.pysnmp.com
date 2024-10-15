# SNMP MIB module (CISCO-VOICE-ENABLED-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-ENABLED-LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:24 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoVoiceEnabledLinkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvenabledlinkMIBObjects_ObjectIdentity = ObjectIdentity
cvenabledlinkMIBObjects = _CvenabledlinkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1)
)
_CvEnabledLink_ObjectIdentity = ObjectIdentity
cvEnabledLink = _CvEnabledLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1)
)
_CvEnabledDefaultMacAddr_Type = MacAddress
_CvEnabledDefaultMacAddr_Object = MibScalar
cvEnabledDefaultMacAddr = _CvEnabledDefaultMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 1),
    _CvEnabledDefaultMacAddr_Type()
)
cvEnabledDefaultMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledDefaultMacAddr.setStatus("current")
_CvEnabledLinkTable_Object = MibTable
cvEnabledLinkTable = _CvEnabledLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvEnabledLinkTable.setStatus("current")
_CvEnabledLinkEntry_Object = MibTableRow
cvEnabledLinkEntry = _CvEnabledLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1)
)
cvEnabledLinkEntry.setIndexNames(
    (0, "CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"),
)
if mibBuilder.loadTexts:
    cvEnabledLinkEntry.setStatus("current")


class _CvEnabledLinkIndex_Type(Integer32):
    """Custom type cvEnabledLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_CvEnabledLinkIndex_Type.__name__ = "Integer32"
_CvEnabledLinkIndex_Object = MibTableColumn
cvEnabledLinkIndex = _CvEnabledLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 1),
    _CvEnabledLinkIndex_Type()
)
cvEnabledLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkIndex.setStatus("current")


class _CvEnabledLinkType_Type(Integer32):
    """Custom type cvEnabledLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("framerelay", 2))
    )


_CvEnabledLinkType_Type.__name__ = "Integer32"
_CvEnabledLinkType_Object = MibTableColumn
cvEnabledLinkType = _CvEnabledLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 2),
    _CvEnabledLinkType_Type()
)
cvEnabledLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkType.setStatus("current")
_CvEnabledLinkInterfaceName_Type = DisplayString
_CvEnabledLinkInterfaceName_Object = MibTableColumn
cvEnabledLinkInterfaceName = _CvEnabledLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 3),
    _CvEnabledLinkInterfaceName_Type()
)
cvEnabledLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkInterfaceName.setStatus("current")


class _CvEnabledLinkVpiDlci_Type(Integer32):
    """Custom type cvEnabledLinkVpiDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CvEnabledLinkVpiDlci_Type.__name__ = "Integer32"
_CvEnabledLinkVpiDlci_Object = MibTableColumn
cvEnabledLinkVpiDlci = _CvEnabledLinkVpiDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 4),
    _CvEnabledLinkVpiDlci_Type()
)
cvEnabledLinkVpiDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkVpiDlci.setStatus("current")


class _CvEnabledLinkVci_Type(Integer32):
    """Custom type cvEnabledLinkVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvEnabledLinkVci_Type.__name__ = "Integer32"
_CvEnabledLinkVci_Object = MibTableColumn
cvEnabledLinkVci = _CvEnabledLinkVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 5),
    _CvEnabledLinkVci_Type()
)
cvEnabledLinkVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkVci.setStatus("current")
_CvEnabledLinkRemoteMacAddr_Type = MacAddress
_CvEnabledLinkRemoteMacAddr_Object = MibTableColumn
cvEnabledLinkRemoteMacAddr = _CvEnabledLinkRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 6),
    _CvEnabledLinkRemoteMacAddr_Type()
)
cvEnabledLinkRemoteMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvEnabledLinkRemoteMacAddr.setStatus("current")
_CiscoVoiceEnabledLinkMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoVoiceEnabledLinkMIBNotificationPrefix = _CiscoVoiceEnabledLinkMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 2)
)
_CiscoVoiceEnabledLinkMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoVoiceEnabledLinkMIBNotifications = _CiscoVoiceEnabledLinkMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 2, 0)
)
_CiscoVoiceEnabledlinkMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVoiceEnabledlinkMIBConformance = _CiscoVoiceEnabledlinkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3)
)
_CiscoVoiceEnabledlinkMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVoiceEnabledlinkMIBCompliances = _CiscoVoiceEnabledlinkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1)
)
_CiscoVoiceEnabledlinkMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVoiceEnabledlinkMIBGroups = _CiscoVoiceEnabledlinkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2)
)

# Managed Objects groups

cvEnabledMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 1)
)
cvEnabledMacAddrGroup.setObjects(
    ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledDefaultMacAddr")
)
if mibBuilder.loadTexts:
    cvEnabledMacAddrGroup.setStatus("current")

cvEnabledLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 2)
)
cvEnabledLinkGroup.setObjects(
      *(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"),
        ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkType"),
        ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkInterfaceName"),
        ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVpiDlci"),
        ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVci"),
        ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkRemoteMacAddr"))
)
if mibBuilder.loadTexts:
    cvEnabledLinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVoiceEnabledlinkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVoiceEnabledlinkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-ENABLED-LINK-MIB",
    **{"ciscoVoiceEnabledLinkMIB": ciscoVoiceEnabledLinkMIB,
       "cvenabledlinkMIBObjects": cvenabledlinkMIBObjects,
       "cvEnabledLink": cvEnabledLink,
       "cvEnabledDefaultMacAddr": cvEnabledDefaultMacAddr,
       "cvEnabledLinkTable": cvEnabledLinkTable,
       "cvEnabledLinkEntry": cvEnabledLinkEntry,
       "cvEnabledLinkIndex": cvEnabledLinkIndex,
       "cvEnabledLinkType": cvEnabledLinkType,
       "cvEnabledLinkInterfaceName": cvEnabledLinkInterfaceName,
       "cvEnabledLinkVpiDlci": cvEnabledLinkVpiDlci,
       "cvEnabledLinkVci": cvEnabledLinkVci,
       "cvEnabledLinkRemoteMacAddr": cvEnabledLinkRemoteMacAddr,
       "ciscoVoiceEnabledLinkMIBNotificationPrefix": ciscoVoiceEnabledLinkMIBNotificationPrefix,
       "ciscoVoiceEnabledLinkMIBNotifications": ciscoVoiceEnabledLinkMIBNotifications,
       "ciscoVoiceEnabledlinkMIBConformance": ciscoVoiceEnabledlinkMIBConformance,
       "ciscoVoiceEnabledlinkMIBCompliances": ciscoVoiceEnabledlinkMIBCompliances,
       "ciscoVoiceEnabledlinkMIBCompliance": ciscoVoiceEnabledlinkMIBCompliance,
       "ciscoVoiceEnabledlinkMIBGroups": ciscoVoiceEnabledlinkMIBGroups,
       "cvEnabledMacAddrGroup": cvEnabledMacAddrGroup,
       "cvEnabledLinkGroup": cvEnabledLinkGroup}
)
