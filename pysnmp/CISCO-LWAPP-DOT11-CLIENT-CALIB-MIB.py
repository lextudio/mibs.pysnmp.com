# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:22 2024
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

(cLApDot11IfSlotId,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfSlotId",
    "cLApSysMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11ClientCalibMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522)
)
ciscoLwappDot11ClientCalibMIB.setRevisions(
        ("2011-11-25 00:00",
         "2007-02-12 00:00",
         "2006-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11ClientCalibMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCalibMIBNotifs = _CiscoLwappDot11ClientCalibMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 0)
)
_CiscoLwappDot11ClientCalibMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCalibMIBObjects = _CiscoLwappDot11ClientCalibMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1)
)
_CldccConfig_ObjectIdentity = ObjectIdentity
cldccConfig = _CldccConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1)
)
_CLD11ClientCalibTable_Object = MibTable
cLD11ClientCalibTable = _CLD11ClientCalibTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLD11ClientCalibTable.setStatus("current")
_CLD11ClientCalibEntry_Object = MibTableRow
cLD11ClientCalibEntry = _CLD11ClientCalibEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1)
)
cLD11ClientCalibEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibMacAddress"),
)
if mibBuilder.loadTexts:
    cLD11ClientCalibEntry.setStatus("current")
_CLD11ClientCalibMacAddress_Type = MacAddress
_CLD11ClientCalibMacAddress_Object = MibTableColumn
cLD11ClientCalibMacAddress = _CLD11ClientCalibMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 1),
    _CLD11ClientCalibMacAddress_Type()
)
cLD11ClientCalibMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLD11ClientCalibMacAddress.setStatus("current")


class _CLD11ClientCalibBeaconInterval_Type(TimeInterval):
    """Custom type cLD11ClientCalibBeaconInterval based on TimeInterval"""
    defaultValue = 60000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3240000),
    )


_CLD11ClientCalibBeaconInterval_Type.__name__ = "TimeInterval"
_CLD11ClientCalibBeaconInterval_Object = MibTableColumn
cLD11ClientCalibBeaconInterval = _CLD11ClientCalibBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 2),
    _CLD11ClientCalibBeaconInterval_Type()
)
cLD11ClientCalibBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibBeaconInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    cLD11ClientCalibBeaconInterval.setUnits("hundredths-seconds")
_CLD11ClientCalibRowStatus_Type = RowStatus
_CLD11ClientCalibRowStatus_Object = MibTableColumn
cLD11ClientCalibRowStatus = _CLD11ClientCalibRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 3),
    _CLD11ClientCalibRowStatus_Type()
)
cLD11ClientCalibRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibRowStatus.setStatus("current")
_CLD11ClientCalibNumberOfRadios_Type = Unsigned32
_CLD11ClientCalibNumberOfRadios_Object = MibTableColumn
cLD11ClientCalibNumberOfRadios = _CLD11ClientCalibNumberOfRadios_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 4),
    _CLD11ClientCalibNumberOfRadios_Type()
)
cLD11ClientCalibNumberOfRadios.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibNumberOfRadios.setStatus("current")
_CLD11ClientCalibNumberOfSamples_Type = Unsigned32
_CLD11ClientCalibNumberOfSamples_Object = MibTableColumn
cLD11ClientCalibNumberOfSamples = _CLD11ClientCalibNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 5),
    _CLD11ClientCalibNumberOfSamples_Type()
)
cLD11ClientCalibNumberOfSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibNumberOfSamples.setStatus("current")
_CLD11ClientCalibSamplesCollected_Type = Unsigned32
_CLD11ClientCalibSamplesCollected_Object = MibTableColumn
cLD11ClientCalibSamplesCollected = _CLD11ClientCalibSamplesCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 6),
    _CLD11ClientCalibSamplesCollected_Type()
)
cLD11ClientCalibSamplesCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLD11ClientCalibSamplesCollected.setStatus("current")


class _CLD11ClientCalibBeaconIntervalExt_Type(TimeInterval):
    """Custom type cLD11ClientCalibBeaconIntervalExt based on TimeInterval"""
    defaultValue = 60000


_CLD11ClientCalibBeaconIntervalExt_Object = MibTableColumn
cLD11ClientCalibBeaconIntervalExt = _CLD11ClientCalibBeaconIntervalExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 7),
    _CLD11ClientCalibBeaconIntervalExt_Type()
)
cLD11ClientCalibBeaconIntervalExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibBeaconIntervalExt.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibBeaconIntervalExt.setUnits("hundredths-seconds")


class _CLD11ClientCalibStorageType_Type(StorageType):
    """Custom type cLD11ClientCalibStorageType based on StorageType"""


_CLD11ClientCalibStorageType_Object = MibTableColumn
cLD11ClientCalibStorageType = _CLD11ClientCalibStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 8),
    _CLD11ClientCalibStorageType_Type()
)
cLD11ClientCalibStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLD11ClientCalibStorageType.setStatus("current")


class _CLD11ClientCalibTableMaxEntries_Type(Unsigned32):
    """Custom type cLD11ClientCalibTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CLD11ClientCalibTableMaxEntries_Type.__name__ = "Unsigned32"
_CLD11ClientCalibTableMaxEntries_Object = MibScalar
cLD11ClientCalibTableMaxEntries = _CLD11ClientCalibTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 2),
    _CLD11ClientCalibTableMaxEntries_Type()
)
cLD11ClientCalibTableMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibTableMaxEntries.setStatus("current")


class _CLD11ClientCalibRssiAlgorithm_Type(Integer32):
    """Custom type cLD11ClientCalibRssiAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("average", 3),
          ("simple", 2),
          ("unknown", 1))
    )


_CLD11ClientCalibRssiAlgorithm_Type.__name__ = "Integer32"
_CLD11ClientCalibRssiAlgorithm_Object = MibScalar
cLD11ClientCalibRssiAlgorithm = _CLD11ClientCalibRssiAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 3),
    _CLD11ClientCalibRssiAlgorithm_Type()
)
cLD11ClientCalibRssiAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiAlgorithm.setStatus("current")
_CLD11ClientCalibRssiClientExpiryTimeout_Type = Unsigned32
_CLD11ClientCalibRssiClientExpiryTimeout_Object = MibScalar
cLD11ClientCalibRssiClientExpiryTimeout = _CLD11ClientCalibRssiClientExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 4),
    _CLD11ClientCalibRssiClientExpiryTimeout_Type()
)
cLD11ClientCalibRssiClientExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiClientExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiClientExpiryTimeout.setUnits("seconds")
_CLD11ClientCalibRssiCalibClientExpiryTimeout_Type = Unsigned32
_CLD11ClientCalibRssiCalibClientExpiryTimeout_Object = MibScalar
cLD11ClientCalibRssiCalibClientExpiryTimeout = _CLD11ClientCalibRssiCalibClientExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 5),
    _CLD11ClientCalibRssiCalibClientExpiryTimeout_Type()
)
cLD11ClientCalibRssiCalibClientExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiCalibClientExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiCalibClientExpiryTimeout.setUnits("seconds")
_CLD11ClientCalibRssiRfidTagExpiryTimeout_Type = Unsigned32
_CLD11ClientCalibRssiRfidTagExpiryTimeout_Object = MibScalar
cLD11ClientCalibRssiRfidTagExpiryTimeout = _CLD11ClientCalibRssiRfidTagExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 6),
    _CLD11ClientCalibRssiRfidTagExpiryTimeout_Type()
)
cLD11ClientCalibRssiRfidTagExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRfidTagExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRfidTagExpiryTimeout.setUnits("seconds")
_CLD11ClientCalibRssiRogueApExpiryTimeout_Type = Unsigned32
_CLD11ClientCalibRssiRogueApExpiryTimeout_Object = MibScalar
cLD11ClientCalibRssiRogueApExpiryTimeout = _CLD11ClientCalibRssiRogueApExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 7),
    _CLD11ClientCalibRssiRogueApExpiryTimeout_Type()
)
cLD11ClientCalibRssiRogueApExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRogueApExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRogueApExpiryTimeout.setUnits("seconds")


class _CLD11ClientCalibRssiClientHalflifeTimeout_Type(Unsigned32):
    """Custom type cLD11ClientCalibRssiClientHalflifeTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(300, 300),
    )


_CLD11ClientCalibRssiClientHalflifeTimeout_Type.__name__ = "Unsigned32"
_CLD11ClientCalibRssiClientHalflifeTimeout_Object = MibScalar
cLD11ClientCalibRssiClientHalflifeTimeout = _CLD11ClientCalibRssiClientHalflifeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 8),
    _CLD11ClientCalibRssiClientHalflifeTimeout_Type()
)
cLD11ClientCalibRssiClientHalflifeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiClientHalflifeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiClientHalflifeTimeout.setUnits("seconds")


class _CLD11ClientCalibRssiCalibClientHalflifeTimeout_Type(Unsigned32):
    """Custom type cLD11ClientCalibRssiCalibClientHalflifeTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(300, 300),
    )


_CLD11ClientCalibRssiCalibClientHalflifeTimeout_Type.__name__ = "Unsigned32"
_CLD11ClientCalibRssiCalibClientHalflifeTimeout_Object = MibScalar
cLD11ClientCalibRssiCalibClientHalflifeTimeout = _CLD11ClientCalibRssiCalibClientHalflifeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 9),
    _CLD11ClientCalibRssiCalibClientHalflifeTimeout_Type()
)
cLD11ClientCalibRssiCalibClientHalflifeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiCalibClientHalflifeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiCalibClientHalflifeTimeout.setUnits("seconds")


class _CLD11ClientCalibRssiRfidTagHalflifeTimeout_Type(Unsigned32):
    """Custom type cLD11ClientCalibRssiRfidTagHalflifeTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(300, 300),
    )


_CLD11ClientCalibRssiRfidTagHalflifeTimeout_Type.__name__ = "Unsigned32"
_CLD11ClientCalibRssiRfidTagHalflifeTimeout_Object = MibScalar
cLD11ClientCalibRssiRfidTagHalflifeTimeout = _CLD11ClientCalibRssiRfidTagHalflifeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 10),
    _CLD11ClientCalibRssiRfidTagHalflifeTimeout_Type()
)
cLD11ClientCalibRssiRfidTagHalflifeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRfidTagHalflifeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRfidTagHalflifeTimeout.setUnits("seconds")


class _CLD11ClientCalibRssiRogueApHalflifeTimeout_Type(Unsigned32):
    """Custom type cLD11ClientCalibRssiRogueApHalflifeTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(300, 300),
    )


_CLD11ClientCalibRssiRogueApHalflifeTimeout_Type.__name__ = "Unsigned32"
_CLD11ClientCalibRssiRogueApHalflifeTimeout_Object = MibScalar
cLD11ClientCalibRssiRogueApHalflifeTimeout = _CLD11ClientCalibRssiRogueApHalflifeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 11),
    _CLD11ClientCalibRssiRogueApHalflifeTimeout_Type()
)
cLD11ClientCalibRssiRogueApHalflifeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRogueApHalflifeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiRogueApHalflifeTimeout.setUnits("seconds")
_CLD11ClientCalibRfidDataEnable_Type = TruthValue
_CLD11ClientCalibRfidDataEnable_Object = MibScalar
cLD11ClientCalibRfidDataEnable = _CLD11ClientCalibRfidDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 12),
    _CLD11ClientCalibRfidDataEnable_Type()
)
cLD11ClientCalibRfidDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRfidDataEnable.setStatus("current")
_CLD11ClientCalibRfidTimeout_Type = Unsigned32
_CLD11ClientCalibRfidTimeout_Object = MibScalar
cLD11ClientCalibRfidTimeout = _CLD11ClientCalibRfidTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 13),
    _CLD11ClientCalibRfidTimeout_Type()
)
cLD11ClientCalibRfidTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRfidTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRfidTimeout.setUnits("seconds")
_CLD11ClientCalibClientMultiBandEnable_Type = TruthValue
_CLD11ClientCalibClientMultiBandEnable_Object = MibScalar
cLD11ClientCalibClientMultiBandEnable = _CLD11ClientCalibClientMultiBandEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 14),
    _CLD11ClientCalibClientMultiBandEnable_Type()
)
cLD11ClientCalibClientMultiBandEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientMultiBandEnable.setStatus("current")
_CLD11ClientCalibClientRequestEnable_Type = TruthValue
_CLD11ClientCalibClientRequestEnable_Object = MibScalar
cLD11ClientCalibClientRequestEnable = _CLD11ClientCalibClientRequestEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 15),
    _CLD11ClientCalibClientRequestEnable_Type()
)
cLD11ClientCalibClientRequestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientRequestEnable.setStatus("current")
_CLD11ClientCalibClientBurstIntervalEnable_Type = TruthValue
_CLD11ClientCalibClientBurstIntervalEnable_Object = MibScalar
cLD11ClientCalibClientBurstIntervalEnable = _CLD11ClientCalibClientBurstIntervalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 16),
    _CLD11ClientCalibClientBurstIntervalEnable_Type()
)
cLD11ClientCalibClientBurstIntervalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientBurstIntervalEnable.setStatus("current")
_CLD11ClientCalibClientBurstInterval_Type = Unsigned32
_CLD11ClientCalibClientBurstInterval_Object = MibScalar
cLD11ClientCalibClientBurstInterval = _CLD11ClientCalibClientBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 17),
    _CLD11ClientCalibClientBurstInterval_Type()
)
cLD11ClientCalibClientBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientBurstInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientBurstInterval.setUnits("seconds")
_CLD11ClientCalibClientInterval_Type = Unsigned32
_CLD11ClientCalibClientInterval_Object = MibScalar
cLD11ClientCalibClientInterval = _CLD11ClientCalibClientInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 18),
    _CLD11ClientCalibClientInterval_Type()
)
cLD11ClientCalibClientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibClientInterval.setUnits("seconds")
_CLD11ClientCalibRfidInterval_Type = Unsigned32
_CLD11ClientCalibRfidInterval_Object = MibScalar
cLD11ClientCalibRfidInterval = _CLD11ClientCalibRfidInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 19),
    _CLD11ClientCalibRfidInterval_Type()
)
cLD11ClientCalibRfidInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRfidInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRfidInterval.setUnits("seconds")
_CLD11ClientCalibRogueInterval_Type = Unsigned32
_CLD11ClientCalibRogueInterval_Object = MibScalar
cLD11ClientCalibRogueInterval = _CLD11ClientCalibRogueInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 20),
    _CLD11ClientCalibRogueInterval_Type()
)
cLD11ClientCalibRogueInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLD11ClientCalibRogueInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLD11ClientCalibRogueInterval.setUnits("seconds")
_CldccStatus_ObjectIdentity = ObjectIdentity
cldccStatus = _CldccStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2)
)
_CldccRssiSamples_ObjectIdentity = ObjectIdentity
cldccRssiSamples = _CldccRssiSamples_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1)
)
_CLD11ClientCalibDataTable_Object = MibTable
cLD11ClientCalibDataTable = _CLD11ClientCalibDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cLD11ClientCalibDataTable.setStatus("current")
_CLD11ClientCalibDataEntry_Object = MibTableRow
cLD11ClientCalibDataEntry = _CLD11ClientCalibDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1)
)
cLD11ClientCalibDataEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataTimeStamp"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataAntennaIndex"),
)
if mibBuilder.loadTexts:
    cLD11ClientCalibDataEntry.setStatus("current")
_ClD11ClientCalibDataTimeStamp_Type = TimeStamp
_ClD11ClientCalibDataTimeStamp_Object = MibTableColumn
clD11ClientCalibDataTimeStamp = _ClD11ClientCalibDataTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 1),
    _ClD11ClientCalibDataTimeStamp_Type()
)
clD11ClientCalibDataTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clD11ClientCalibDataTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    clD11ClientCalibDataTimeStamp.setUnits("milliseconds")


class _ClD11ClientCalibDataAntennaIndex_Type(Integer32):
    """Custom type clD11ClientCalibDataAntennaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antenna1", 1),
          ("antenna2", 2))
    )


_ClD11ClientCalibDataAntennaIndex_Type.__name__ = "Integer32"
_ClD11ClientCalibDataAntennaIndex_Object = MibTableColumn
clD11ClientCalibDataAntennaIndex = _ClD11ClientCalibDataAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 2),
    _ClD11ClientCalibDataAntennaIndex_Type()
)
clD11ClientCalibDataAntennaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clD11ClientCalibDataAntennaIndex.setStatus("current")
_ClD11ClientCalibDataRssiValue_Type = Integer32
_ClD11ClientCalibDataRssiValue_Object = MibTableColumn
clD11ClientCalibDataRssiValue = _ClD11ClientCalibDataRssiValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 3),
    _ClD11ClientCalibDataRssiValue_Type()
)
clD11ClientCalibDataRssiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clD11ClientCalibDataRssiValue.setStatus("current")
_ClD11ClientCalibDataTransmitPower_Type = Integer32
_ClD11ClientCalibDataTransmitPower_Object = MibTableColumn
clD11ClientCalibDataTransmitPower = _ClD11ClientCalibDataTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 4),
    _ClD11ClientCalibDataTransmitPower_Type()
)
clD11ClientCalibDataTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clD11ClientCalibDataTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    clD11ClientCalibDataTransmitPower.setUnits("dbm")
_CiscoLwappDot11ClientCalibMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCalibMIBConform = _CiscoLwappDot11ClientCalibMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2)
)
_CiscoLwappDot11ClientCalibMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCalibMIBCompliances = _CiscoLwappDot11ClientCalibMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1)
)
_CiscoLwappDot11ClientCalibMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCalibMIBGroups = _CiscoLwappDot11ClientCalibMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11ClientCalibMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 1)
)
ciscoLwappDot11ClientCalibMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibBeaconInterval"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRowStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibTableMaxEntries"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCalibMIBConfigGroup.setStatus("deprecated")

cLD11ClientCalibClientConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 2)
)
cLD11ClientCalibClientConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRowStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibBeaconIntervalExt"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibNumberOfRadios"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibNumberOfSamples"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibSamplesCollected"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibStorageType"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibTableMaxEntries"))
)
if mibBuilder.loadTexts:
    cLD11ClientCalibClientConfigGroup.setStatus("current")

cLD11ClientCalibGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 3)
)
cLD11ClientCalibGlobalConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiAlgorithm"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiClientExpiryTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiCalibClientExpiryTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRfidTagExpiryTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRogueApExpiryTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiClientHalflifeTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiCalibClientHalflifeTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRfidTagHalflifeTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRogueApHalflifeTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidDataEnable"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidTimeout"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientMultiBandEnable"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientRequestEnable"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientBurstIntervalEnable"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientBurstInterval"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientInterval"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidInterval"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRogueInterval"))
)
if mibBuilder.loadTexts:
    cLD11ClientCalibGlobalConfigGroup.setStatus("current")

cLD11ClientCalibRssiDataSampleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 4)
)
cLD11ClientCalibRssiDataSampleGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataRssiValue"),
        ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataTransmitPower"))
)
if mibBuilder.loadTexts:
    cLD11ClientCalibRssiDataSampleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappDot11ClientCalibMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCalibMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11ClientCalibMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCalibMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB",
    **{"ciscoLwappDot11ClientCalibMIB": ciscoLwappDot11ClientCalibMIB,
       "ciscoLwappDot11ClientCalibMIBNotifs": ciscoLwappDot11ClientCalibMIBNotifs,
       "ciscoLwappDot11ClientCalibMIBObjects": ciscoLwappDot11ClientCalibMIBObjects,
       "cldccConfig": cldccConfig,
       "cLD11ClientCalibTable": cLD11ClientCalibTable,
       "cLD11ClientCalibEntry": cLD11ClientCalibEntry,
       "cLD11ClientCalibMacAddress": cLD11ClientCalibMacAddress,
       "cLD11ClientCalibBeaconInterval": cLD11ClientCalibBeaconInterval,
       "cLD11ClientCalibRowStatus": cLD11ClientCalibRowStatus,
       "cLD11ClientCalibNumberOfRadios": cLD11ClientCalibNumberOfRadios,
       "cLD11ClientCalibNumberOfSamples": cLD11ClientCalibNumberOfSamples,
       "cLD11ClientCalibSamplesCollected": cLD11ClientCalibSamplesCollected,
       "cLD11ClientCalibBeaconIntervalExt": cLD11ClientCalibBeaconIntervalExt,
       "cLD11ClientCalibStorageType": cLD11ClientCalibStorageType,
       "cLD11ClientCalibTableMaxEntries": cLD11ClientCalibTableMaxEntries,
       "cLD11ClientCalibRssiAlgorithm": cLD11ClientCalibRssiAlgorithm,
       "cLD11ClientCalibRssiClientExpiryTimeout": cLD11ClientCalibRssiClientExpiryTimeout,
       "cLD11ClientCalibRssiCalibClientExpiryTimeout": cLD11ClientCalibRssiCalibClientExpiryTimeout,
       "cLD11ClientCalibRssiRfidTagExpiryTimeout": cLD11ClientCalibRssiRfidTagExpiryTimeout,
       "cLD11ClientCalibRssiRogueApExpiryTimeout": cLD11ClientCalibRssiRogueApExpiryTimeout,
       "cLD11ClientCalibRssiClientHalflifeTimeout": cLD11ClientCalibRssiClientHalflifeTimeout,
       "cLD11ClientCalibRssiCalibClientHalflifeTimeout": cLD11ClientCalibRssiCalibClientHalflifeTimeout,
       "cLD11ClientCalibRssiRfidTagHalflifeTimeout": cLD11ClientCalibRssiRfidTagHalflifeTimeout,
       "cLD11ClientCalibRssiRogueApHalflifeTimeout": cLD11ClientCalibRssiRogueApHalflifeTimeout,
       "cLD11ClientCalibRfidDataEnable": cLD11ClientCalibRfidDataEnable,
       "cLD11ClientCalibRfidTimeout": cLD11ClientCalibRfidTimeout,
       "cLD11ClientCalibClientMultiBandEnable": cLD11ClientCalibClientMultiBandEnable,
       "cLD11ClientCalibClientRequestEnable": cLD11ClientCalibClientRequestEnable,
       "cLD11ClientCalibClientBurstIntervalEnable": cLD11ClientCalibClientBurstIntervalEnable,
       "cLD11ClientCalibClientBurstInterval": cLD11ClientCalibClientBurstInterval,
       "cLD11ClientCalibClientInterval": cLD11ClientCalibClientInterval,
       "cLD11ClientCalibRfidInterval": cLD11ClientCalibRfidInterval,
       "cLD11ClientCalibRogueInterval": cLD11ClientCalibRogueInterval,
       "cldccStatus": cldccStatus,
       "cldccRssiSamples": cldccRssiSamples,
       "cLD11ClientCalibDataTable": cLD11ClientCalibDataTable,
       "cLD11ClientCalibDataEntry": cLD11ClientCalibDataEntry,
       "clD11ClientCalibDataTimeStamp": clD11ClientCalibDataTimeStamp,
       "clD11ClientCalibDataAntennaIndex": clD11ClientCalibDataAntennaIndex,
       "clD11ClientCalibDataRssiValue": clD11ClientCalibDataRssiValue,
       "clD11ClientCalibDataTransmitPower": clD11ClientCalibDataTransmitPower,
       "ciscoLwappDot11ClientCalibMIBConform": ciscoLwappDot11ClientCalibMIBConform,
       "ciscoLwappDot11ClientCalibMIBCompliances": ciscoLwappDot11ClientCalibMIBCompliances,
       "ciscoLwappDot11ClientCalibMIBCompliance": ciscoLwappDot11ClientCalibMIBCompliance,
       "ciscoLwappDot11ClientCalibMIBComplianceRev1": ciscoLwappDot11ClientCalibMIBComplianceRev1,
       "ciscoLwappDot11ClientCalibMIBGroups": ciscoLwappDot11ClientCalibMIBGroups,
       "ciscoLwappDot11ClientCalibMIBConfigGroup": ciscoLwappDot11ClientCalibMIBConfigGroup,
       "cLD11ClientCalibClientConfigGroup": cLD11ClientCalibClientConfigGroup,
       "cLD11ClientCalibGlobalConfigGroup": cLD11ClientCalibGlobalConfigGroup,
       "cLD11ClientCalibRssiDataSampleGroup": cLD11ClientCalibRssiDataSampleGroup}
)
