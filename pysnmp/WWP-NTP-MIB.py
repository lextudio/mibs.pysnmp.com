# SNMP MIB module (WWP-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:17 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5)
)
wwpNtpMIB.setRevisions(
        ("2003-03-11 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpNtpMIBObjects_ObjectIdentity = ObjectIdentity
wwpNtpMIBObjects = _WwpNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1)
)
_WwpNtp_ObjectIdentity = ObjectIdentity
wwpNtp = _WwpNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1)
)


class _WwpNtpRcvBroadcasts_Type(Integer32):
    """Custom type wwpNtpRcvBroadcasts based on Integer32"""
    defaultValue = 1

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


_WwpNtpRcvBroadcasts_Type.__name__ = "Integer32"
_WwpNtpRcvBroadcasts_Object = MibScalar
wwpNtpRcvBroadcasts = _WwpNtpRcvBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 1),
    _WwpNtpRcvBroadcasts_Type()
)
wwpNtpRcvBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpNtpRcvBroadcasts.setStatus("current")


class _WwpNtpEnablePolling_Type(Integer32):
    """Custom type wwpNtpEnablePolling based on Integer32"""
    defaultValue = 0

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


_WwpNtpEnablePolling_Type.__name__ = "Integer32"
_WwpNtpEnablePolling_Object = MibScalar
wwpNtpEnablePolling = _WwpNtpEnablePolling_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 2),
    _WwpNtpEnablePolling_Type()
)
wwpNtpEnablePolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpNtpEnablePolling.setStatus("current")


class _WwpNtpPollFreq_Type(Integer32):
    """Custom type wwpNtpPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpNtpPollFreq_Type.__name__ = "Integer32"
_WwpNtpPollFreq_Object = MibScalar
wwpNtpPollFreq = _WwpNtpPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 3),
    _WwpNtpPollFreq_Type()
)
wwpNtpPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpNtpPollFreq.setStatus("current")
_WwpNtpServerTable_Object = MibTable
wwpNtpServerTable = _WwpNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpNtpServerTable.setStatus("current")
_WwpNtpServerEntry_Object = MibTableRow
wwpNtpServerEntry = _WwpNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1)
)
wwpNtpServerEntry.setIndexNames(
    (0, "WWP-NTP-MIB", "wwpNtpServerIpAddr"),
)
if mibBuilder.loadTexts:
    wwpNtpServerEntry.setStatus("current")
_WwpNtpServerIpAddr_Type = IpAddress
_WwpNtpServerIpAddr_Object = MibTableColumn
wwpNtpServerIpAddr = _WwpNtpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1, 1),
    _WwpNtpServerIpAddr_Type()
)
wwpNtpServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpNtpServerIpAddr.setStatus("current")
_WwpNtpServerRowStatus_Type = RowStatus
_WwpNtpServerRowStatus_Object = MibTableColumn
wwpNtpServerRowStatus = _WwpNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1, 2),
    _WwpNtpServerRowStatus_Type()
)
wwpNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpNtpServerRowStatus.setStatus("current")
_WwpNtpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpNtpMIBNotificationPrefix = _WwpNtpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 2)
)
_WwpNtpMIBNotifications_ObjectIdentity = ObjectIdentity
wwpNtpMIBNotifications = _WwpNtpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 2, 0)
)
_WwpNtpMIBConformance_ObjectIdentity = ObjectIdentity
wwpNtpMIBConformance = _WwpNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 3)
)
_WwpNtpMIBCompliances_ObjectIdentity = ObjectIdentity
wwpNtpMIBCompliances = _WwpNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 3, 1)
)
_WwpNtpMIBGroups_ObjectIdentity = ObjectIdentity
wwpNtpMIBGroups = _WwpNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 5, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-NTP-MIB",
    **{"wwpNtpMIB": wwpNtpMIB,
       "wwpNtpMIBObjects": wwpNtpMIBObjects,
       "wwpNtp": wwpNtp,
       "wwpNtpRcvBroadcasts": wwpNtpRcvBroadcasts,
       "wwpNtpEnablePolling": wwpNtpEnablePolling,
       "wwpNtpPollFreq": wwpNtpPollFreq,
       "wwpNtpServerTable": wwpNtpServerTable,
       "wwpNtpServerEntry": wwpNtpServerEntry,
       "wwpNtpServerIpAddr": wwpNtpServerIpAddr,
       "wwpNtpServerRowStatus": wwpNtpServerRowStatus,
       "wwpNtpMIBNotificationPrefix": wwpNtpMIBNotificationPrefix,
       "wwpNtpMIBNotifications": wwpNtpMIBNotifications,
       "wwpNtpMIBConformance": wwpNtpMIBConformance,
       "wwpNtpMIBCompliances": wwpNtpMIBCompliances,
       "wwpNtpMIBGroups": wwpNtpMIBGroups}
)
