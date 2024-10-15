# SNMP MIB module (SYMMNTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMNTP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:54 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(EnableValue,
 symmPacketService) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "symmPacketService")


# MODULE-IDENTITY

symmNTP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_NtpStatus_ObjectIdentity = ObjectIdentity
ntpStatus = _NtpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1)
)
_NtpCommonStatusTable_Object = MibTable
ntpCommonStatusTable = _NtpCommonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntpCommonStatusTable.setStatus("current")
_NtpCommonStatusEntry_Object = MibTableRow
ntpCommonStatusEntry = _NtpCommonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1)
)
ntpCommonStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMNTP", "ntpStatusIndex"),
)
if mibBuilder.loadTexts:
    ntpCommonStatusEntry.setStatus("current")


class _NtpStatusIndex_Type(Integer32):
    """Custom type ntpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NtpStatusIndex_Type.__name__ = "Integer32"
_NtpStatusIndex_Object = MibTableColumn
ntpStatusIndex = _NtpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 1),
    _NtpStatusIndex_Type()
)
ntpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpStatusIndex.setStatus("current")
_NtpStatusEnable_Type = EnableValue
_NtpStatusEnable_Object = MibTableColumn
ntpStatusEnable = _NtpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 2),
    _NtpStatusEnable_Type()
)
ntpStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusEnable.setStatus("current")
_NtpStatusMode_Type = DisplayString
_NtpStatusMode_Object = MibTableColumn
ntpStatusMode = _NtpStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 3),
    _NtpStatusMode_Type()
)
ntpStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusMode.setStatus("current")
_NtpStatusLeapStatus_Type = DisplayString
_NtpStatusLeapStatus_Object = MibTableColumn
ntpStatusLeapStatus = _NtpStatusLeapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 4),
    _NtpStatusLeapStatus_Type()
)
ntpStatusLeapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusLeapStatus.setStatus("current")
_NtpStatusStratumLevel_Type = DisplayString
_NtpStatusStratumLevel_Object = MibTableColumn
ntpStatusStratumLevel = _NtpStatusStratumLevel_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 5),
    _NtpStatusStratumLevel_Type()
)
ntpStatusStratumLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusStratumLevel.setStatus("current")
_NtpStatusRootDispersion_Type = DisplayString
_NtpStatusRootDispersion_Object = MibTableColumn
ntpStatusRootDispersion = _NtpStatusRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 6),
    _NtpStatusRootDispersion_Type()
)
ntpStatusRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusRootDispersion.setStatus("current")
_NtpStatusPacketLoad_Type = DisplayString
_NtpStatusPacketLoad_Object = MibTableColumn
ntpStatusPacketLoad = _NtpStatusPacketLoad_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 7),
    _NtpStatusPacketLoad_Type()
)
ntpStatusPacketLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusPacketLoad.setStatus("current")
_NtpStatusVersion_Type = DisplayString
_NtpStatusVersion_Object = MibTableColumn
ntpStatusVersion = _NtpStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 8),
    _NtpStatusVersion_Type()
)
ntpStatusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatusVersion.setStatus("current")
_NtpConfig_ObjectIdentity = ObjectIdentity
ntpConfig = _NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2)
)
_NtpCommonConfigTable_Object = MibTable
ntpCommonConfigTable = _NtpCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ntpCommonConfigTable.setStatus("current")
_NtpCommonConfigEntry_Object = MibTableRow
ntpCommonConfigEntry = _NtpCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1)
)
ntpCommonConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMNTP", "ntpCommonIndex"),
)
if mibBuilder.loadTexts:
    ntpCommonConfigEntry.setStatus("current")


class _NtpCommonIndex_Type(Integer32):
    """Custom type ntpCommonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NtpCommonIndex_Type.__name__ = "Integer32"
_NtpCommonIndex_Object = MibTableColumn
ntpCommonIndex = _NtpCommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 1),
    _NtpCommonIndex_Type()
)
ntpCommonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpCommonIndex.setStatus("current")
_NtpCommonState_Type = EnableValue
_NtpCommonState_Object = MibTableColumn
ntpCommonState = _NtpCommonState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 2),
    _NtpCommonState_Type()
)
ntpCommonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonState.setStatus("current")


class _NtpCommonTTL_Type(Unsigned32):
    """Custom type ntpCommonTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtpCommonTTL_Type.__name__ = "Unsigned32"
_NtpCommonTTL_Object = MibTableColumn
ntpCommonTTL = _NtpCommonTTL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 3),
    _NtpCommonTTL_Type()
)
ntpCommonTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonTTL.setStatus("current")
_NtpCommonDSCP_Type = EnableValue
_NtpCommonDSCP_Object = MibTableColumn
ntpCommonDSCP = _NtpCommonDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 4),
    _NtpCommonDSCP_Type()
)
ntpCommonDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonDSCP.setStatus("current")


class _NtpCommonDSCPValue_Type(Unsigned32):
    """Custom type ntpCommonDSCPValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NtpCommonDSCPValue_Type.__name__ = "Unsigned32"
_NtpCommonDSCPValue_Object = MibTableColumn
ntpCommonDSCPValue = _NtpCommonDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 5),
    _NtpCommonDSCPValue_Type()
)
ntpCommonDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonDSCPValue.setStatus("current")


class _NtpCommonVlanId_Type(Integer32):
    """Custom type ntpCommonVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtpCommonVlanId_Type.__name__ = "Integer32"
_NtpCommonVlanId_Object = MibTableColumn
ntpCommonVlanId = _NtpCommonVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 6),
    _NtpCommonVlanId_Type()
)
ntpCommonVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonVlanId.setStatus("current")


class _NtpCommonServiceLoadAlarmThreshold_Type(Integer32):
    """Custom type ntpCommonServiceLoadAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_NtpCommonServiceLoadAlarmThreshold_Type.__name__ = "Integer32"
_NtpCommonServiceLoadAlarmThreshold_Object = MibTableColumn
ntpCommonServiceLoadAlarmThreshold = _NtpCommonServiceLoadAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 7),
    _NtpCommonServiceLoadAlarmThreshold_Type()
)
ntpCommonServiceLoadAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCommonServiceLoadAlarmThreshold.setStatus("current")
_NtpConformance_ObjectIdentity = ObjectIdentity
ntpConformance = _NtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ntpConformance.setStatus("current")
_NtpCompliances_ObjectIdentity = ObjectIdentity
ntpCompliances = _NtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1)
)
_NtpUocGroups_ObjectIdentity = ObjectIdentity
ntpUocGroups = _NtpUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2)
)

# Managed Objects groups

ntpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 1)
)
ntpStatusGroup.setObjects(
      *(("SYMMNTP", "ntpStatusEnable"),
        ("SYMMNTP", "ntpStatusMode"),
        ("SYMMNTP", "ntpStatusLeapStatus"),
        ("SYMMNTP", "ntpStatusStratumLevel"),
        ("SYMMNTP", "ntpStatusRootDispersion"),
        ("SYMMNTP", "ntpStatusPacketLoad"),
        ("SYMMNTP", "ntpStatusVersion"))
)
if mibBuilder.loadTexts:
    ntpStatusGroup.setStatus("current")

ntpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 2)
)
ntpConfigGroup.setObjects(
      *(("SYMMNTP", "ntpCommonState"),
        ("SYMMNTP", "ntpCommonTTL"),
        ("SYMMNTP", "ntpCommonDSCP"),
        ("SYMMNTP", "ntpCommonDSCPValue"),
        ("SYMMNTP", "ntpCommonVlanId"),
        ("SYMMNTP", "ntpCommonServiceLoadAlarmThreshold"))
)
if mibBuilder.loadTexts:
    ntpConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ntpBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMNTP",
    **{"DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmNTP": symmNTP,
       "ntpStatus": ntpStatus,
       "ntpCommonStatusTable": ntpCommonStatusTable,
       "ntpCommonStatusEntry": ntpCommonStatusEntry,
       "ntpStatusIndex": ntpStatusIndex,
       "ntpStatusEnable": ntpStatusEnable,
       "ntpStatusMode": ntpStatusMode,
       "ntpStatusLeapStatus": ntpStatusLeapStatus,
       "ntpStatusStratumLevel": ntpStatusStratumLevel,
       "ntpStatusRootDispersion": ntpStatusRootDispersion,
       "ntpStatusPacketLoad": ntpStatusPacketLoad,
       "ntpStatusVersion": ntpStatusVersion,
       "ntpConfig": ntpConfig,
       "ntpCommonConfigTable": ntpCommonConfigTable,
       "ntpCommonConfigEntry": ntpCommonConfigEntry,
       "ntpCommonIndex": ntpCommonIndex,
       "ntpCommonState": ntpCommonState,
       "ntpCommonTTL": ntpCommonTTL,
       "ntpCommonDSCP": ntpCommonDSCP,
       "ntpCommonDSCPValue": ntpCommonDSCPValue,
       "ntpCommonVlanId": ntpCommonVlanId,
       "ntpCommonServiceLoadAlarmThreshold": ntpCommonServiceLoadAlarmThreshold,
       "ntpConformance": ntpConformance,
       "ntpCompliances": ntpCompliances,
       "ntpBasicCompliance": ntpBasicCompliance,
       "ntpUocGroups": ntpUocGroups,
       "ntpStatusGroup": ntpStatusGroup,
       "ntpConfigGroup": ntpConfigGroup}
)
