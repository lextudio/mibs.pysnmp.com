# SNMP MIB module (BLUECOAT-SG-ICAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-ICAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:20 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGICAPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14)
)
bluecoatSGICAPMIB.setRevisions(
        ("2013-02-08 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ICAPServiceEntityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("servivceGroup", 2))
    )



class ICAPServiceNotificationType(Integer32, TextualConvention):
    status = "current"
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
        *(("deferredRequestsAboveThreshold", 3),
          ("deferredRequestsBelowThreshold", 4),
          ("queuedRequestsAboveThreshold", 1),
          ("queuedRequestsBelowThreshold", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BluecoatSgICAPMIBObjects_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBObjects = _BluecoatSgICAPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1)
)
_BluecoatSgICAPValues_ObjectIdentity = ObjectIdentity
bluecoatSgICAPValues = _BluecoatSgICAPValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1)
)
_IcapService_ObjectIdentity = ObjectIdentity
icapService = _IcapService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1)
)
_IcapServiceStatsTable_Object = MibTable
icapServiceStatsTable = _IcapServiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    icapServiceStatsTable.setStatus("current")
_IcapServiceStatsTableEntry_Object = MibTableRow
icapServiceStatsTableEntry = _IcapServiceStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1)
)
icapServiceStatsTableEntry.setIndexNames(
    (0, "BLUECOAT-SG-ICAP-MIB", "icapServiceStatsIndex"),
)
if mibBuilder.loadTexts:
    icapServiceStatsTableEntry.setStatus("current")


class _IcapServiceStatsIndex_Type(Unsigned32):
    """Custom type icapServiceStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IcapServiceStatsIndex_Type.__name__ = "Unsigned32"
_IcapServiceStatsIndex_Object = MibTableColumn
icapServiceStatsIndex = _IcapServiceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 1),
    _IcapServiceStatsIndex_Type()
)
icapServiceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icapServiceStatsIndex.setStatus("current")


class _IcapServiceStatsName_Type(OctetString):
    """Custom type icapServiceStatsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IcapServiceStatsName_Type.__name__ = "OctetString"
_IcapServiceStatsName_Object = MibTableColumn
icapServiceStatsName = _IcapServiceStatsName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 2),
    _IcapServiceStatsName_Type()
)
icapServiceStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsName.setStatus("current")
_IcapServiceStatsEntityType_Type = ICAPServiceEntityType
_IcapServiceStatsEntityType_Object = MibTableColumn
icapServiceStatsEntityType = _IcapServiceStatsEntityType_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 3),
    _IcapServiceStatsEntityType_Type()
)
icapServiceStatsEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsEntityType.setStatus("current")
_IcapServiceStatsPlainConns_Type = Gauge32
_IcapServiceStatsPlainConns_Object = MibTableColumn
icapServiceStatsPlainConns = _IcapServiceStatsPlainConns_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 4),
    _IcapServiceStatsPlainConns_Type()
)
icapServiceStatsPlainConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsPlainConns.setStatus("current")
_IcapServiceStatsSecuredConns_Type = Gauge32
_IcapServiceStatsSecuredConns_Object = MibTableColumn
icapServiceStatsSecuredConns = _IcapServiceStatsSecuredConns_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 5),
    _IcapServiceStatsSecuredConns_Type()
)
icapServiceStatsSecuredConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsSecuredConns.setStatus("current")
_IcapServiceStatsPlainActvReqs_Type = Gauge32
_IcapServiceStatsPlainActvReqs_Object = MibTableColumn
icapServiceStatsPlainActvReqs = _IcapServiceStatsPlainActvReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 6),
    _IcapServiceStatsPlainActvReqs_Type()
)
icapServiceStatsPlainActvReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsPlainActvReqs.setStatus("current")
_IcapServiceStatsSecureActvReqs_Type = Gauge32
_IcapServiceStatsSecureActvReqs_Object = MibTableColumn
icapServiceStatsSecureActvReqs = _IcapServiceStatsSecureActvReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 7),
    _IcapServiceStatsSecureActvReqs_Type()
)
icapServiceStatsSecureActvReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsSecureActvReqs.setStatus("current")
_IcapServiceStatsQueuedReqs_Type = Gauge32
_IcapServiceStatsQueuedReqs_Object = MibTableColumn
icapServiceStatsQueuedReqs = _IcapServiceStatsQueuedReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 8),
    _IcapServiceStatsQueuedReqs_Type()
)
icapServiceStatsQueuedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsQueuedReqs.setStatus("current")
_IcapServiceStatsDeferredReqs_Type = Gauge32
_IcapServiceStatsDeferredReqs_Object = MibTableColumn
icapServiceStatsDeferredReqs = _IcapServiceStatsDeferredReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 9),
    _IcapServiceStatsDeferredReqs_Type()
)
icapServiceStatsDeferredReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsDeferredReqs.setStatus("current")
_IcapServiceStatsRcvdBytes_Type = Counter64
_IcapServiceStatsRcvdBytes_Object = MibTableColumn
icapServiceStatsRcvdBytes = _IcapServiceStatsRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 10),
    _IcapServiceStatsRcvdBytes_Type()
)
icapServiceStatsRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsRcvdBytes.setStatus("current")
_IcapServiceStatsSentBytes_Type = Counter64
_IcapServiceStatsSentBytes_Object = MibTableColumn
icapServiceStatsSentBytes = _IcapServiceStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 11),
    _IcapServiceStatsSentBytes_Type()
)
icapServiceStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsSentBytes.setStatus("current")
_IcapServiceStatsFailedReqs_Type = Counter64
_IcapServiceStatsFailedReqs_Object = MibTableColumn
icapServiceStatsFailedReqs = _IcapServiceStatsFailedReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 12),
    _IcapServiceStatsFailedReqs_Type()
)
icapServiceStatsFailedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsFailedReqs.setStatus("current")
_IcapServiceStatsSuccessfullReqs_Type = Counter64
_IcapServiceStatsSuccessfullReqs_Object = MibTableColumn
icapServiceStatsSuccessfullReqs = _IcapServiceStatsSuccessfullReqs_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 13),
    _IcapServiceStatsSuccessfullReqs_Type()
)
icapServiceStatsSuccessfullReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icapServiceStatsSuccessfullReqs.setStatus("current")
_SgICAPNotification_Type = ICAPServiceNotificationType
_SgICAPNotification_Object = MibScalar
sgICAPNotification = _SgICAPNotification_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 2),
    _SgICAPNotification_Type()
)
sgICAPNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgICAPNotification.setStatus("current")
_BluecoatSgICAPMIBNotifications_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBNotifications = _BluecoatSgICAPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 2)
)
_SgICAPMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sgICAPMIBNotificationsPrefix = _SgICAPMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0)
)
_BluecoatSgICAPMIBConformance_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBConformance = _BluecoatSgICAPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3)
)
_BluecoatSgICAPMIBCompliances_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBCompliances = _BluecoatSgICAPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1)
)
_BluecoatSgICAPMIBGroups_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBGroups = _BluecoatSgICAPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2)
)
_BluecoatSgICAPMIBNotifGroups_ObjectIdentity = ObjectIdentity
bluecoatSgICAPMIBNotifGroups = _BluecoatSgICAPMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3)
)

# Managed Objects groups

bluecoatSgICAPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2, 1)
)
bluecoatSgICAPMIBGroup.setObjects(
      *(("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsEntityType"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainConns"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecuredConns"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainActvReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecureActvReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsRcvdBytes"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSentBytes"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsFailedReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSuccessfullReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"))
)
if mibBuilder.loadTexts:
    bluecoatSgICAPMIBGroup.setStatus("current")


# Notification objects

sgICAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0, 1)
)
sgICAPTrap.setObjects(
      *(("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"),
        ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"))
)
if mibBuilder.loadTexts:
    sgICAPTrap.setStatus(
        "current"
    )


# Notifications groups

bluecoatSgICAPMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3, 1)
)
bluecoatSgICAPMIBNotifGroup.setObjects(
    ("BLUECOAT-SG-ICAP-MIB", "sgICAPTrap")
)
if mibBuilder.loadTexts:
    bluecoatSgICAPMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bluecoatSgICAPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bluecoatSgICAPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-ICAP-MIB",
    **{"ICAPServiceEntityType": ICAPServiceEntityType,
       "ICAPServiceNotificationType": ICAPServiceNotificationType,
       "bluecoatSGICAPMIB": bluecoatSGICAPMIB,
       "bluecoatSgICAPMIBObjects": bluecoatSgICAPMIBObjects,
       "bluecoatSgICAPValues": bluecoatSgICAPValues,
       "icapService": icapService,
       "icapServiceStatsTable": icapServiceStatsTable,
       "icapServiceStatsTableEntry": icapServiceStatsTableEntry,
       "icapServiceStatsIndex": icapServiceStatsIndex,
       "icapServiceStatsName": icapServiceStatsName,
       "icapServiceStatsEntityType": icapServiceStatsEntityType,
       "icapServiceStatsPlainConns": icapServiceStatsPlainConns,
       "icapServiceStatsSecuredConns": icapServiceStatsSecuredConns,
       "icapServiceStatsPlainActvReqs": icapServiceStatsPlainActvReqs,
       "icapServiceStatsSecureActvReqs": icapServiceStatsSecureActvReqs,
       "icapServiceStatsQueuedReqs": icapServiceStatsQueuedReqs,
       "icapServiceStatsDeferredReqs": icapServiceStatsDeferredReqs,
       "icapServiceStatsRcvdBytes": icapServiceStatsRcvdBytes,
       "icapServiceStatsSentBytes": icapServiceStatsSentBytes,
       "icapServiceStatsFailedReqs": icapServiceStatsFailedReqs,
       "icapServiceStatsSuccessfullReqs": icapServiceStatsSuccessfullReqs,
       "sgICAPNotification": sgICAPNotification,
       "bluecoatSgICAPMIBNotifications": bluecoatSgICAPMIBNotifications,
       "sgICAPMIBNotificationsPrefix": sgICAPMIBNotificationsPrefix,
       "sgICAPTrap": sgICAPTrap,
       "bluecoatSgICAPMIBConformance": bluecoatSgICAPMIBConformance,
       "bluecoatSgICAPMIBCompliances": bluecoatSgICAPMIBCompliances,
       "bluecoatSgICAPMIBCompliance": bluecoatSgICAPMIBCompliance,
       "bluecoatSgICAPMIBGroups": bluecoatSgICAPMIBGroups,
       "bluecoatSgICAPMIBGroup": bluecoatSgICAPMIBGroup,
       "bluecoatSgICAPMIBNotifGroups": bluecoatSgICAPMIBNotifGroups,
       "bluecoatSgICAPMIBNotifGroup": bluecoatSgICAPMIBNotifGroup}
)
