# SNMP MIB module (ALVARION-TOOLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-TOOLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:46 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionNotificationEnable,) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionNotificationEnable")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

alvarionToolsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionToolsMIBObjects_ObjectIdentity = ObjectIdentity
alvarionToolsMIBObjects = _AlvarionToolsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1)
)
_TraceToolConfig_ObjectIdentity = ObjectIdentity
traceToolConfig = _TraceToolConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1)
)
_TraceInterface_Type = InterfaceIndex
_TraceInterface_Object = MibScalar
traceInterface = _TraceInterface_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 1),
    _TraceInterface_Type()
)
traceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceInterface.setStatus("current")


class _TraceCaptureDestination_Type(Integer32):
    """Custom type traceCaptureDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TraceCaptureDestination_Type.__name__ = "Integer32"
_TraceCaptureDestination_Object = MibScalar
traceCaptureDestination = _TraceCaptureDestination_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 2),
    _TraceCaptureDestination_Type()
)
traceCaptureDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCaptureDestination.setStatus("current")
_TraceCaptureDestinationURL_Type = DisplayString
_TraceCaptureDestinationURL_Object = MibScalar
traceCaptureDestinationURL = _TraceCaptureDestinationURL_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 3),
    _TraceCaptureDestinationURL_Type()
)
traceCaptureDestinationURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCaptureDestinationURL.setStatus("current")


class _TraceTimeout_Type(Unsigned32):
    """Custom type traceTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TraceTimeout_Type.__name__ = "Unsigned32"
_TraceTimeout_Object = MibScalar
traceTimeout = _TraceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 4),
    _TraceTimeout_Type()
)
traceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    traceTimeout.setUnits("seconds")


class _TraceNumberOfPackets_Type(Unsigned32):
    """Custom type traceNumberOfPackets based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TraceNumberOfPackets_Type.__name__ = "Unsigned32"
_TraceNumberOfPackets_Object = MibScalar
traceNumberOfPackets = _TraceNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 5),
    _TraceNumberOfPackets_Type()
)
traceNumberOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceNumberOfPackets.setStatus("current")
if mibBuilder.loadTexts:
    traceNumberOfPackets.setUnits("packets")


class _TracePacketSize_Type(Unsigned32):
    """Custom type tracePacketSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 4096),
    )


_TracePacketSize_Type.__name__ = "Unsigned32"
_TracePacketSize_Object = MibScalar
tracePacketSize = _TracePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 6),
    _TracePacketSize_Type()
)
tracePacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tracePacketSize.setStatus("current")
if mibBuilder.loadTexts:
    tracePacketSize.setUnits("bytes")
_TraceCaptureFilter_Type = DisplayString
_TraceCaptureFilter_Object = MibScalar
traceCaptureFilter = _TraceCaptureFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 7),
    _TraceCaptureFilter_Type()
)
traceCaptureFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCaptureFilter.setStatus("current")


class _TraceCaptureStatus_Type(Integer32):
    """Custom type traceCaptureStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_TraceCaptureStatus_Type.__name__ = "Integer32"
_TraceCaptureStatus_Object = MibScalar
traceCaptureStatus = _TraceCaptureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 8),
    _TraceCaptureStatus_Type()
)
traceCaptureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCaptureStatus.setStatus("current")


class _TraceNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type traceNotificationEnabled based on AlvarionNotificationEnable"""


_TraceNotificationEnabled_Object = MibScalar
traceNotificationEnabled = _TraceNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 9),
    _TraceNotificationEnabled_Type()
)
traceNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceNotificationEnabled.setStatus("current")
_AlvarionToolsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionToolsMIBNotificationPrefix = _AlvarionToolsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2)
)
_AlvarionToolsMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionToolsMIBNotifications = _AlvarionToolsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2, 0)
)
_AlvarionToolsMIBConformance_ObjectIdentity = ObjectIdentity
alvarionToolsMIBConformance = _AlvarionToolsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3)
)
_AlvarionToolsMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionToolsMIBCompliances = _AlvarionToolsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 1)
)
_AlvarionToolsMIBGroups_ObjectIdentity = ObjectIdentity
alvarionToolsMIBGroups = _AlvarionToolsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2)
)

# Managed Objects groups

alvarionToolsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2, 1)
)
alvarionToolsMIBGroup.setObjects(
      *(("ALVARION-TOOLS-MIB", "traceInterface"),
        ("ALVARION-TOOLS-MIB", "traceCaptureDestination"),
        ("ALVARION-TOOLS-MIB", "traceCaptureDestinationURL"),
        ("ALVARION-TOOLS-MIB", "traceTimeout"),
        ("ALVARION-TOOLS-MIB", "traceNumberOfPackets"),
        ("ALVARION-TOOLS-MIB", "tracePacketSize"),
        ("ALVARION-TOOLS-MIB", "traceCaptureFilter"),
        ("ALVARION-TOOLS-MIB", "traceCaptureStatus"),
        ("ALVARION-TOOLS-MIB", "traceNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionToolsMIBGroup.setStatus("current")


# Notification objects

traceStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2, 0, 1)
)
traceStatusNotification.setObjects(
    ("ALVARION-TOOLS-MIB", "traceCaptureStatus")
)
if mibBuilder.loadTexts:
    traceStatusNotification.setStatus(
        "current"
    )


# Notifications groups

alvarionToolsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2, 2)
)
alvarionToolsNotificationGroup.setObjects(
    ("ALVARION-TOOLS-MIB", "traceStatusNotification")
)
if mibBuilder.loadTexts:
    alvarionToolsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionToolsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionToolsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-TOOLS-MIB",
    **{"alvarionToolsMIB": alvarionToolsMIB,
       "alvarionToolsMIBObjects": alvarionToolsMIBObjects,
       "traceToolConfig": traceToolConfig,
       "traceInterface": traceInterface,
       "traceCaptureDestination": traceCaptureDestination,
       "traceCaptureDestinationURL": traceCaptureDestinationURL,
       "traceTimeout": traceTimeout,
       "traceNumberOfPackets": traceNumberOfPackets,
       "tracePacketSize": tracePacketSize,
       "traceCaptureFilter": traceCaptureFilter,
       "traceCaptureStatus": traceCaptureStatus,
       "traceNotificationEnabled": traceNotificationEnabled,
       "alvarionToolsMIBNotificationPrefix": alvarionToolsMIBNotificationPrefix,
       "alvarionToolsMIBNotifications": alvarionToolsMIBNotifications,
       "traceStatusNotification": traceStatusNotification,
       "alvarionToolsMIBConformance": alvarionToolsMIBConformance,
       "alvarionToolsMIBCompliances": alvarionToolsMIBCompliances,
       "alvarionToolsMIBCompliance": alvarionToolsMIBCompliance,
       "alvarionToolsMIBGroups": alvarionToolsMIBGroups,
       "alvarionToolsMIBGroup": alvarionToolsMIBGroup,
       "alvarionToolsNotificationGroup": alvarionToolsNotificationGroup}
)
