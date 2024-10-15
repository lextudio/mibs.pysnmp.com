# SNMP MIB module (CISCO-CABLE-METERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-METERING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:38 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableMeteringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424)
)
ciscoCableMeteringMIB.setRevisions(
        ("2009-10-13 00:00",
         "2009-05-18 00:00",
         "2004-03-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcmtrStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("connectionTimeout", 6),
          ("dataIncomplete", 7),
          ("deviceFull", 3),
          ("fileNotExist", 5),
          ("success", 2),
          ("unknown", 1),
          ("writeError", 4))
    )



class CcmtrCollectionServer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCableMeteringMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableMeteringMIBNotifs = _CiscoCableMeteringMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 0)
)
_CiscoCableMeteringMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableMeteringMIBObjects = _CiscoCableMeteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1)
)
_CcmtrMeteringConfig_ObjectIdentity = ObjectIdentity
ccmtrMeteringConfig = _CcmtrMeteringConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1)
)


class _CcmtrCollectionType_Type(Integer32):
    """Custom type ccmtrCollectionType based on Integer32"""
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
        *(("ipdr", 4),
          ("local", 2),
          ("none", 1),
          ("stream", 3))
    )


_CcmtrCollectionType_Type.__name__ = "Integer32"
_CcmtrCollectionType_Object = MibScalar
ccmtrCollectionType = _CcmtrCollectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 1),
    _CcmtrCollectionType_Type()
)
ccmtrCollectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionType.setStatus("current")


class _CcmtrCollectionFilesystem_Type(SnmpAdminString):
    """Custom type ccmtrCollectionFilesystem based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CcmtrCollectionFilesystem_Type.__name__ = "SnmpAdminString"
_CcmtrCollectionFilesystem_Object = MibScalar
ccmtrCollectionFilesystem = _CcmtrCollectionFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 2),
    _CcmtrCollectionFilesystem_Type()
)
ccmtrCollectionFilesystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionFilesystem.setStatus("current")
_CcmtrCollectionTable_Object = MibTable
ccmtrCollectionTable = _CcmtrCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ccmtrCollectionTable.setStatus("current")
_CcmtrCollectionEntry_Object = MibTableRow
ccmtrCollectionEntry = _CcmtrCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1)
)
ccmtrCollectionEntry.setIndexNames(
    (0, "CISCO-CABLE-METERING-MIB", "ccmtrCollectionID"),
)
if mibBuilder.loadTexts:
    ccmtrCollectionEntry.setStatus("current")
_CcmtrCollectionID_Type = CcmtrCollectionServer
_CcmtrCollectionID_Object = MibTableColumn
ccmtrCollectionID = _CcmtrCollectionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 1),
    _CcmtrCollectionID_Type()
)
ccmtrCollectionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmtrCollectionID.setStatus("current")


class _CcmtrCollectionIpAddrType_Type(InetAddressType):
    """Custom type ccmtrCollectionIpAddrType based on InetAddressType"""


_CcmtrCollectionIpAddrType_Object = MibTableColumn
ccmtrCollectionIpAddrType = _CcmtrCollectionIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 2),
    _CcmtrCollectionIpAddrType_Type()
)
ccmtrCollectionIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmtrCollectionIpAddrType.setStatus("current")
_CcmtrCollectionIpAddress_Type = InetAddress
_CcmtrCollectionIpAddress_Object = MibTableColumn
ccmtrCollectionIpAddress = _CcmtrCollectionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 3),
    _CcmtrCollectionIpAddress_Type()
)
ccmtrCollectionIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmtrCollectionIpAddress.setStatus("current")
_CcmtrCollectionPort_Type = InetPortNumber
_CcmtrCollectionPort_Object = MibTableColumn
ccmtrCollectionPort = _CcmtrCollectionPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 4),
    _CcmtrCollectionPort_Type()
)
ccmtrCollectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmtrCollectionPort.setStatus("current")
_CcmtrCollectionRowStatus_Type = RowStatus
_CcmtrCollectionRowStatus_Object = MibTableColumn
ccmtrCollectionRowStatus = _CcmtrCollectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 8),
    _CcmtrCollectionRowStatus_Type()
)
ccmtrCollectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmtrCollectionRowStatus.setStatus("current")


class _CcmtrCollectionInterval_Type(Unsigned32):
    """Custom type ccmtrCollectionInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_CcmtrCollectionInterval_Type.__name__ = "Unsigned32"
_CcmtrCollectionInterval_Object = MibScalar
ccmtrCollectionInterval = _CcmtrCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 4),
    _CcmtrCollectionInterval_Type()
)
ccmtrCollectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccmtrCollectionInterval.setUnits("minutes")


class _CcmtrCollectionRetries_Type(Unsigned32):
    """Custom type ccmtrCollectionRetries based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CcmtrCollectionRetries_Type.__name__ = "Unsigned32"
_CcmtrCollectionRetries_Object = MibScalar
ccmtrCollectionRetries = _CcmtrCollectionRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 5),
    _CcmtrCollectionRetries_Type()
)
ccmtrCollectionRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionRetries.setStatus("current")


class _CcmtrCollectionSecure_Type(TruthValue):
    """Custom type ccmtrCollectionSecure based on TruthValue"""


_CcmtrCollectionSecure_Object = MibScalar
ccmtrCollectionSecure = _CcmtrCollectionSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 6),
    _CcmtrCollectionSecure_Type()
)
ccmtrCollectionSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionSecure.setStatus("current")


class _CcmtrCollectionCpeList_Type(TruthValue):
    """Custom type ccmtrCollectionCpeList based on TruthValue"""


_CcmtrCollectionCpeList_Object = MibScalar
ccmtrCollectionCpeList = _CcmtrCollectionCpeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 7),
    _CcmtrCollectionCpeList_Type()
)
ccmtrCollectionCpeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionCpeList.setStatus("current")


class _CcmtrCollectionAggregate_Type(TruthValue):
    """Custom type ccmtrCollectionAggregate based on TruthValue"""


_CcmtrCollectionAggregate_Object = MibScalar
ccmtrCollectionAggregate = _CcmtrCollectionAggregate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 8),
    _CcmtrCollectionAggregate_Type()
)
ccmtrCollectionAggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionAggregate.setStatus("current")


class _CcmtrCollectionSrcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ccmtrCollectionSrcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcmtrCollectionSrcIfIndex_Object = MibScalar
ccmtrCollectionSrcIfIndex = _CcmtrCollectionSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 9),
    _CcmtrCollectionSrcIfIndex_Type()
)
ccmtrCollectionSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionSrcIfIndex.setStatus("current")


class _CcmtrCollectionRevInterval_Type(Unsigned32):
    """Custom type ccmtrCollectionRevInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcmtrCollectionRevInterval_Type.__name__ = "Unsigned32"
_CcmtrCollectionRevInterval_Object = MibScalar
ccmtrCollectionRevInterval = _CcmtrCollectionRevInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 10),
    _CcmtrCollectionRevInterval_Type()
)
ccmtrCollectionRevInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionRevInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccmtrCollectionRevInterval.setUnits("minutes")


class _CcmtrCollectionDataPerSession_Type(Unsigned32):
    """Custom type ccmtrCollectionDataPerSession based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_CcmtrCollectionDataPerSession_Type.__name__ = "Unsigned32"
_CcmtrCollectionDataPerSession_Object = MibScalar
ccmtrCollectionDataPerSession = _CcmtrCollectionDataPerSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 11),
    _CcmtrCollectionDataPerSession_Type()
)
ccmtrCollectionDataPerSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionDataPerSession.setStatus("current")


class _CcmtrCollectionDataTimer_Type(Unsigned32):
    """Custom type ccmtrCollectionDataTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 500),
    )


_CcmtrCollectionDataTimer_Type.__name__ = "Unsigned32"
_CcmtrCollectionDataTimer_Object = MibScalar
ccmtrCollectionDataTimer = _CcmtrCollectionDataTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 12),
    _CcmtrCollectionDataTimer_Type()
)
ccmtrCollectionDataTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrCollectionDataTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccmtrCollectionDataTimer.setUnits("milliseconds")
_CcmtrMetering_ObjectIdentity = ObjectIdentity
ccmtrMetering = _CcmtrMetering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2)
)
_CcmtrCollectionStatus_Type = CcmtrStatus
_CcmtrCollectionStatus_Object = MibScalar
ccmtrCollectionStatus = _CcmtrCollectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 1),
    _CcmtrCollectionStatus_Type()
)
ccmtrCollectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmtrCollectionStatus.setStatus("current")


class _CcmtrCollectionDestination_Type(SnmpAdminString):
    """Custom type ccmtrCollectionDestination based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CcmtrCollectionDestination_Type.__name__ = "SnmpAdminString"
_CcmtrCollectionDestination_Object = MibScalar
ccmtrCollectionDestination = _CcmtrCollectionDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 2),
    _CcmtrCollectionDestination_Type()
)
ccmtrCollectionDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmtrCollectionDestination.setStatus("current")
_CcmtrCollectionTimestamp_Type = DateAndTime
_CcmtrCollectionTimestamp_Object = MibScalar
ccmtrCollectionTimestamp = _CcmtrCollectionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 3),
    _CcmtrCollectionTimestamp_Type()
)
ccmtrCollectionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmtrCollectionTimestamp.setStatus("current")


class _CcmtrMeteringNotifEnable_Type(TruthValue):
    """Custom type ccmtrMeteringNotifEnable based on TruthValue"""


_CcmtrMeteringNotifEnable_Object = MibScalar
ccmtrMeteringNotifEnable = _CcmtrMeteringNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 4),
    _CcmtrMeteringNotifEnable_Type()
)
ccmtrMeteringNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmtrMeteringNotifEnable.setStatus("current")
_CiscoCableMeteringMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCableMeteringMIBConformance = _CiscoCableMeteringMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3)
)
_CiscoCableMeteringMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableMeteringMIBCompliances = _CiscoCableMeteringMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1)
)
_CiscoCableMeteringMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableMeteringMIBGroups = _CiscoCableMeteringMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2)
)

# Managed Objects groups

ccmtrMeteringObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 1)
)
ccmtrMeteringObjGroup.setObjects(
      *(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionType"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionFilesystem"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddrType"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddress"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionPort"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionInterval"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRetries"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSecure"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRowStatus"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionCpeList"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionAggregate"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
)
if mibBuilder.loadTexts:
    ccmtrMeteringObjGroup.setStatus("deprecated")

ccmtrMeteringNotifCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 2)
)
ccmtrMeteringNotifCtrlGroup.setObjects(
    ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifEnable")
)
if mibBuilder.loadTexts:
    ccmtrMeteringNotifCtrlGroup.setStatus("current")

ccmtrMeteringObjGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 4)
)
ccmtrMeteringObjGroupRev1.setObjects(
      *(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionType"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionFilesystem"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddrType"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddress"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionPort"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRowStatus"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRetries"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSecure"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionCpeList"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionAggregate"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRevInterval"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
)
if mibBuilder.loadTexts:
    ccmtrMeteringObjGroupRev1.setStatus("current")

ccmtrMeteringSrcIntfObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 5)
)
ccmtrMeteringSrcIntfObjGroup.setObjects(
    ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSrcIfIndex")
)
if mibBuilder.loadTexts:
    ccmtrMeteringSrcIntfObjGroup.setStatus("current")

ccmtrMeteringRateCtrlObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 6)
)
ccmtrMeteringRateCtrlObjGroup.setObjects(
      *(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDataPerSession"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDataTimer"))
)
if mibBuilder.loadTexts:
    ccmtrMeteringRateCtrlObjGroup.setStatus("current")


# Notification objects

ccmtrCollectionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 0, 1)
)
ccmtrCollectionNotification.setObjects(
      *(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"),
        ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
)
if mibBuilder.loadTexts:
    ccmtrCollectionNotification.setStatus(
        "current"
    )


# Notifications groups

ccmtrMeteringNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 3)
)
ccmtrMeteringNotifGroup.setObjects(
    ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionNotification")
)
if mibBuilder.loadTexts:
    ccmtrMeteringNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCableMeteringCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableMeteringCompliance.setStatus(
        "deprecated"
    )

ciscoCableMeteringComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCableMeteringComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-METERING-MIB",
    **{"CcmtrStatus": CcmtrStatus,
       "CcmtrCollectionServer": CcmtrCollectionServer,
       "ciscoCableMeteringMIB": ciscoCableMeteringMIB,
       "ciscoCableMeteringMIBNotifs": ciscoCableMeteringMIBNotifs,
       "ccmtrCollectionNotification": ccmtrCollectionNotification,
       "ciscoCableMeteringMIBObjects": ciscoCableMeteringMIBObjects,
       "ccmtrMeteringConfig": ccmtrMeteringConfig,
       "ccmtrCollectionType": ccmtrCollectionType,
       "ccmtrCollectionFilesystem": ccmtrCollectionFilesystem,
       "ccmtrCollectionTable": ccmtrCollectionTable,
       "ccmtrCollectionEntry": ccmtrCollectionEntry,
       "ccmtrCollectionID": ccmtrCollectionID,
       "ccmtrCollectionIpAddrType": ccmtrCollectionIpAddrType,
       "ccmtrCollectionIpAddress": ccmtrCollectionIpAddress,
       "ccmtrCollectionPort": ccmtrCollectionPort,
       "ccmtrCollectionRowStatus": ccmtrCollectionRowStatus,
       "ccmtrCollectionInterval": ccmtrCollectionInterval,
       "ccmtrCollectionRetries": ccmtrCollectionRetries,
       "ccmtrCollectionSecure": ccmtrCollectionSecure,
       "ccmtrCollectionCpeList": ccmtrCollectionCpeList,
       "ccmtrCollectionAggregate": ccmtrCollectionAggregate,
       "ccmtrCollectionSrcIfIndex": ccmtrCollectionSrcIfIndex,
       "ccmtrCollectionRevInterval": ccmtrCollectionRevInterval,
       "ccmtrCollectionDataPerSession": ccmtrCollectionDataPerSession,
       "ccmtrCollectionDataTimer": ccmtrCollectionDataTimer,
       "ccmtrMetering": ccmtrMetering,
       "ccmtrCollectionStatus": ccmtrCollectionStatus,
       "ccmtrCollectionDestination": ccmtrCollectionDestination,
       "ccmtrCollectionTimestamp": ccmtrCollectionTimestamp,
       "ccmtrMeteringNotifEnable": ccmtrMeteringNotifEnable,
       "ciscoCableMeteringMIBConformance": ciscoCableMeteringMIBConformance,
       "ciscoCableMeteringMIBCompliances": ciscoCableMeteringMIBCompliances,
       "ciscoCableMeteringCompliance": ciscoCableMeteringCompliance,
       "ciscoCableMeteringComplianceRev1": ciscoCableMeteringComplianceRev1,
       "ciscoCableMeteringMIBGroups": ciscoCableMeteringMIBGroups,
       "ccmtrMeteringObjGroup": ccmtrMeteringObjGroup,
       "ccmtrMeteringNotifCtrlGroup": ccmtrMeteringNotifCtrlGroup,
       "ccmtrMeteringNotifGroup": ccmtrMeteringNotifGroup,
       "ccmtrMeteringObjGroupRev1": ccmtrMeteringObjGroupRev1,
       "ccmtrMeteringSrcIntfObjGroup": ccmtrMeteringSrcIntfObjGroup,
       "ccmtrMeteringRateCtrlObjGroup": ccmtrMeteringRateCtrlObjGroup}
)
