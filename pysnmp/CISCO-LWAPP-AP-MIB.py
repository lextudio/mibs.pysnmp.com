# SNMP MIB module (CISCO-LWAPP-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:11 2024
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

(cldRegulatoryDomain,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-MIB",
    "cldRegulatoryDomain")

(CLApAssocFailureReason,
 CLApDot11RadioRole,
 CLApDot11RadioSubband,
 CLApIfType,
 CLDot11Channel) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApAssocFailureReason",
    "CLApDot11RadioRole",
    "CLApDot11RadioSubband",
    "CLApIfType",
    "CLDot11Channel")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513)
)
ciscoLwappApMIB.setRevisions(
        ("2012-06-13 00:00",
         "2011-02-07 00:00",
         "2011-01-21 00:00",
         "2011-01-10 00:00",
         "2010-12-13 00:00",
         "2010-08-19 00:00",
         "2007-01-03 00:00",
         "2006-07-18 00:00",
         "2006-03-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappApMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBNotifs = _CiscoLwappApMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0)
)
_CiscoLwappApMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBObjects = _CiscoLwappApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1)
)
_CiscoLwappAp_ObjectIdentity = ObjectIdentity
ciscoLwappAp = _CiscoLwappAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1)
)
_CLApTable_Object = MibTable
cLApTable = _CLApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLApTable.setStatus("current")
_CLApEntry_Object = MibTableRow
cLApEntry = _CLApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1)
)
cLApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApEntry.setStatus("current")
_CLApSysMacAddress_Type = MacAddress
_CLApSysMacAddress_Object = MibTableColumn
cLApSysMacAddress = _CLApSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 1),
    _CLApSysMacAddress_Type()
)
cLApSysMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApSysMacAddress.setStatus("current")
_CLApIfMacAddress_Type = MacAddress
_CLApIfMacAddress_Object = MibTableColumn
cLApIfMacAddress = _CLApIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 2),
    _CLApIfMacAddress_Type()
)
cLApIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIfMacAddress.setStatus("current")
_CLApMaxNumberOfDot11Slots_Type = Unsigned32
_CLApMaxNumberOfDot11Slots_Object = MibTableColumn
cLApMaxNumberOfDot11Slots = _CLApMaxNumberOfDot11Slots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 3),
    _CLApMaxNumberOfDot11Slots_Type()
)
cLApMaxNumberOfDot11Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxNumberOfDot11Slots.setStatus("current")
_CLApEntPhysicalIndex_Type = PhysicalIndex
_CLApEntPhysicalIndex_Object = MibTableColumn
cLApEntPhysicalIndex = _CLApEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 4),
    _CLApEntPhysicalIndex_Type()
)
cLApEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEntPhysicalIndex.setStatus("current")


class _CLApName_Type(SnmpAdminString):
    """Custom type cLApName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApName_Type.__name__ = "SnmpAdminString"
_CLApName_Object = MibTableColumn
cLApName = _CLApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 5),
    _CLApName_Type()
)
cLApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApName.setStatus("current")
_CLApUpTime_Type = TimeTicks
_CLApUpTime_Object = MibTableColumn
cLApUpTime = _CLApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 6),
    _CLApUpTime_Type()
)
cLApUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUpTime.setStatus("current")
_CLLwappUpTime_Type = TimeTicks
_CLLwappUpTime_Object = MibTableColumn
cLLwappUpTime = _CLLwappUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 7),
    _CLLwappUpTime_Type()
)
cLLwappUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLwappUpTime.setStatus("current")
_CLLwappJoinTakenTime_Type = TimeTicks
_CLLwappJoinTakenTime_Object = MibTableColumn
cLLwappJoinTakenTime = _CLLwappJoinTakenTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 8),
    _CLLwappJoinTakenTime_Type()
)
cLLwappJoinTakenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLwappJoinTakenTime.setStatus("current")
_CLApMaxNumberOfEthernetSlots_Type = Unsigned32
_CLApMaxNumberOfEthernetSlots_Object = MibTableColumn
cLApMaxNumberOfEthernetSlots = _CLApMaxNumberOfEthernetSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 9),
    _CLApMaxNumberOfEthernetSlots_Type()
)
cLApMaxNumberOfEthernetSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxNumberOfEthernetSlots.setStatus("current")
_CLApPrimaryControllerAddressType_Type = InetAddressType
_CLApPrimaryControllerAddressType_Object = MibTableColumn
cLApPrimaryControllerAddressType = _CLApPrimaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 10),
    _CLApPrimaryControllerAddressType_Type()
)
cLApPrimaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryControllerAddressType.setStatus("current")
_CLApPrimaryControllerAddress_Type = InetAddress
_CLApPrimaryControllerAddress_Object = MibTableColumn
cLApPrimaryControllerAddress = _CLApPrimaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 11),
    _CLApPrimaryControllerAddress_Type()
)
cLApPrimaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryControllerAddress.setStatus("current")
_CLApSecondaryControllerAddressType_Type = InetAddressType
_CLApSecondaryControllerAddressType_Object = MibTableColumn
cLApSecondaryControllerAddressType = _CLApSecondaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 12),
    _CLApSecondaryControllerAddressType_Type()
)
cLApSecondaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSecondaryControllerAddressType.setStatus("current")
_CLApSecondaryControllerAddress_Type = InetAddress
_CLApSecondaryControllerAddress_Object = MibTableColumn
cLApSecondaryControllerAddress = _CLApSecondaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 13),
    _CLApSecondaryControllerAddress_Type()
)
cLApSecondaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSecondaryControllerAddress.setStatus("current")
_CLApTertiaryControllerAddressType_Type = InetAddressType
_CLApTertiaryControllerAddressType_Object = MibTableColumn
cLApTertiaryControllerAddressType = _CLApTertiaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 14),
    _CLApTertiaryControllerAddressType_Type()
)
cLApTertiaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTertiaryControllerAddressType.setStatus("current")
_CLApTertiaryControllerAddress_Type = InetAddress
_CLApTertiaryControllerAddress_Object = MibTableColumn
cLApTertiaryControllerAddress = _CLApTertiaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 15),
    _CLApTertiaryControllerAddress_Type()
)
cLApTertiaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTertiaryControllerAddress.setStatus("current")


class _CLApLastRebootReason_Type(Integer32):
    """Custom type cLApLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("componentFailure", 24),
          ("configController", 10),
          ("configFileInvalid", 15),
          ("crash", 20),
          ("denyJoin", 8),
          ("dhcpFallbackFail", 5),
          ("discoveryFail", 6),
          ("dot11gModeChange", 1),
          ("imageCheckSumInvalid", 13),
          ("imageDataTimeout", 14),
          ("imageDownloadError", 16),
          ("imageOpcodeInvalid", 12),
          ("imageUpgradeSuccess", 11),
          ("ipAddressReset", 3),
          ("ipAddressSet", 2),
          ("noConfigResponse", 9),
          ("noJoinResponse", 7),
          ("none", 0),
          ("powerChange", 23),
          ("powerHigh", 21),
          ("powerLoss", 22),
          ("powerLow", 19),
          ("rapOverAir", 18),
          ("rebootFromConsole", 17),
          ("rebootFromController", 4),
          ("watchdog", 25))
    )


_CLApLastRebootReason_Type.__name__ = "Integer32"
_CLApLastRebootReason_Object = MibTableColumn
cLApLastRebootReason = _CLApLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 16),
    _CLApLastRebootReason_Type()
)
cLApLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLastRebootReason.setStatus("current")


class _CLApEncryptionEnable_Type(TruthValue):
    """Custom type cLApEncryptionEnable based on TruthValue"""


_CLApEncryptionEnable_Object = MibTableColumn
cLApEncryptionEnable = _CLApEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 18),
    _CLApEncryptionEnable_Type()
)
cLApEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEncryptionEnable.setStatus("current")


class _CLApFailoverPriority_Type(Integer32):
    """Custom type cLApFailoverPriority based on Integer32"""
    defaultValue = 1

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
        *(("critical", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_CLApFailoverPriority_Type.__name__ = "Integer32"
_CLApFailoverPriority_Object = MibTableColumn
cLApFailoverPriority = _CLApFailoverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 19),
    _CLApFailoverPriority_Type()
)
cLApFailoverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFailoverPriority.setStatus("current")


class _CLApPowerStatus_Type(Integer32):
    """Custom type cLApPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("external", 5),
          ("fifteendotfour", 2),
          ("full", 4),
          ("low", 1),
          ("mixedmode", 6),
          ("sixteendoteight", 3))
    )


_CLApPowerStatus_Type.__name__ = "Integer32"
_CLApPowerStatus_Object = MibTableColumn
cLApPowerStatus = _CLApPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 20),
    _CLApPowerStatus_Type()
)
cLApPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPowerStatus.setStatus("current")


class _CLApTelnetEnable_Type(TruthValue):
    """Custom type cLApTelnetEnable based on TruthValue"""


_CLApTelnetEnable_Object = MibTableColumn
cLApTelnetEnable = _CLApTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 21),
    _CLApTelnetEnable_Type()
)
cLApTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTelnetEnable.setStatus("current")


class _CLApSshEnable_Type(TruthValue):
    """Custom type cLApSshEnable based on TruthValue"""


_CLApSshEnable_Object = MibTableColumn
cLApSshEnable = _CLApSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 22),
    _CLApSshEnable_Type()
)
cLApSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSshEnable.setStatus("current")
_CLApPreStdStateEnabled_Type = TruthValue
_CLApPreStdStateEnabled_Object = MibTableColumn
cLApPreStdStateEnabled = _CLApPreStdStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 23),
    _CLApPreStdStateEnabled_Type()
)
cLApPreStdStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPreStdStateEnabled.setStatus("current")
_CLApPwrInjectorStateEnabled_Type = TruthValue
_CLApPwrInjectorStateEnabled_Object = MibTableColumn
cLApPwrInjectorStateEnabled = _CLApPwrInjectorStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 24),
    _CLApPwrInjectorStateEnabled_Type()
)
cLApPwrInjectorStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorStateEnabled.setStatus("current")


class _CLApPwrInjectorSelection_Type(Integer32):
    """Custom type cLApPwrInjectorSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("override", 3),
          ("unknown", 1))
    )


_CLApPwrInjectorSelection_Type.__name__ = "Integer32"
_CLApPwrInjectorSelection_Object = MibTableColumn
cLApPwrInjectorSelection = _CLApPwrInjectorSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 25),
    _CLApPwrInjectorSelection_Type()
)
cLApPwrInjectorSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorSelection.setStatus("current")
_CLApPwrInjectorSwMacAddr_Type = MacAddress
_CLApPwrInjectorSwMacAddr_Object = MibTableColumn
cLApPwrInjectorSwMacAddr = _CLApPwrInjectorSwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 26),
    _CLApPwrInjectorSwMacAddr_Type()
)
cLApPwrInjectorSwMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorSwMacAddr.setStatus("current")


class _CLApWipsEnable_Type(TruthValue):
    """Custom type cLApWipsEnable based on TruthValue"""


_CLApWipsEnable_Object = MibTableColumn
cLApWipsEnable = _CLApWipsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 27),
    _CLApWipsEnable_Type()
)
cLApWipsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApWipsEnable.setStatus("current")


class _CLApMonitorModeOptimization_Type(Integer32):
    """Custom type cLApMonitorModeOptimization based on Integer32"""
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
        *(("all", 1),
          ("none", 4),
          ("tracking", 2),
          ("wips", 3))
    )


_CLApMonitorModeOptimization_Type.__name__ = "Integer32"
_CLApMonitorModeOptimization_Object = MibTableColumn
cLApMonitorModeOptimization = _CLApMonitorModeOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 28),
    _CLApMonitorModeOptimization_Type()
)
cLApMonitorModeOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApMonitorModeOptimization.setStatus("current")
_CLApDomainName_Type = SnmpAdminString
_CLApDomainName_Object = MibTableColumn
cLApDomainName = _CLApDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 29),
    _CLApDomainName_Type()
)
cLApDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDomainName.setStatus("current")
_CLApNameServerAddressType_Type = InetAddressType
_CLApNameServerAddressType_Object = MibTableColumn
cLApNameServerAddressType = _CLApNameServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 30),
    _CLApNameServerAddressType_Type()
)
cLApNameServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNameServerAddressType.setStatus("current")
_CLApNameServerAddress_Type = InetAddress
_CLApNameServerAddress_Object = MibTableColumn
cLApNameServerAddress = _CLApNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 31),
    _CLApNameServerAddress_Type()
)
cLApNameServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNameServerAddress.setStatus("current")


class _CLApAMSDUEnable_Type(TruthValue):
    """Custom type cLApAMSDUEnable based on TruthValue"""


_CLApAMSDUEnable_Object = MibTableColumn
cLApAMSDUEnable = _CLApAMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 32),
    _CLApAMSDUEnable_Type()
)
cLApAMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAMSDUEnable.setStatus("current")


class _CLApEncryptionSupported_Type(TruthValue):
    """Custom type cLApEncryptionSupported based on TruthValue"""


_CLApEncryptionSupported_Object = MibTableColumn
cLApEncryptionSupported = _CLApEncryptionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 33),
    _CLApEncryptionSupported_Type()
)
cLApEncryptionSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEncryptionSupported.setStatus("current")


class _CLApRogueDetectionEnabled_Type(TruthValue):
    """Custom type cLApRogueDetectionEnabled based on TruthValue"""


_CLApRogueDetectionEnabled_Object = MibTableColumn
cLApRogueDetectionEnabled = _CLApRogueDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 34),
    _CLApRogueDetectionEnabled_Type()
)
cLApRogueDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRogueDetectionEnabled.setStatus("current")


class _CLApTcpMss_Type(Integer32):
    """Custom type cLApTcpMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(536, 1363),
    )


_CLApTcpMss_Type.__name__ = "Integer32"
_CLApTcpMss_Object = MibTableColumn
cLApTcpMss = _CLApTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 35),
    _CLApTcpMss_Type()
)
cLApTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTcpMss.setStatus("current")


class _CLApDataEncryptionStatus_Type(TruthValue):
    """Custom type cLApDataEncryptionStatus based on TruthValue"""


_CLApDataEncryptionStatus_Object = MibTableColumn
cLApDataEncryptionStatus = _CLApDataEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 36),
    _CLApDataEncryptionStatus_Type()
)
cLApDataEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataEncryptionStatus.setStatus("current")


class _CLApNsiKey_Type(DisplayString):
    """Custom type cLApNsiKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApNsiKey_Type.__name__ = "DisplayString"
_CLApNsiKey_Object = MibTableColumn
cLApNsiKey = _CLApNsiKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 37),
    _CLApNsiKey_Type()
)
cLApNsiKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApNsiKey.setStatus("current")


class _CLApAdminStatus_Type(TruthValue):
    """Custom type cLApAdminStatus based on TruthValue"""


_CLApAdminStatus_Object = MibTableColumn
cLApAdminStatus = _CLApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 38),
    _CLApAdminStatus_Type()
)
cLApAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAdminStatus.setStatus("current")
_CLApPortNumber_Type = InetPortNumber
_CLApPortNumber_Object = MibTableColumn
cLApPortNumber = _CLApPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 39),
    _CLApPortNumber_Type()
)
cLApPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPortNumber.setStatus("current")
_CLApRetransmitCount_Type = Unsigned32
_CLApRetransmitCount_Object = MibTableColumn
cLApRetransmitCount = _CLApRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 40),
    _CLApRetransmitCount_Type()
)
cLApRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApRetransmitCount.setUnits("retries")
_CLApRetransmitTimeout_Type = Unsigned32
_CLApRetransmitTimeout_Object = MibTableColumn
cLApRetransmitTimeout = _CLApRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 41),
    _CLApRetransmitTimeout_Type()
)
cLApRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRetransmitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApRetransmitTimeout.setUnits("seconds")
_CLApIfSmtParamTable_Object = MibTable
cLApIfSmtParamTable = _CLApIfSmtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLApIfSmtParamTable.setStatus("current")
_CLApIfSmtParamEntry_Object = MibTableRow
cLApIfSmtParamEntry = _CLApIfSmtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2, 1)
)
cLApIfSmtParamEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApIfSmtParamEntry.setStatus("current")
_CLApIfSmtDot11Bssid_Type = MacAddress
_CLApIfSmtDot11Bssid_Object = MibTableColumn
cLApIfSmtDot11Bssid = _CLApIfSmtDot11Bssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2, 1, 1),
    _CLApIfSmtDot11Bssid_Type()
)
cLApIfSmtDot11Bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIfSmtDot11Bssid.setStatus("current")
_CLApCountryTable_Object = MibTable
cLApCountryTable = _CLApCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLApCountryTable.setStatus("current")
_CLApCountryEntry_Object = MibTableRow
cLApCountryEntry = _CLApCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1)
)
cLApCountryEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCountryEntry.setStatus("current")


class _CLApCountryCode_Type(DisplayString):
    """Custom type cLApCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApCountryCode_Type.__name__ = "DisplayString"
_CLApCountryCode_Object = MibTableColumn
cLApCountryCode = _CLApCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1, 1),
    _CLApCountryCode_Type()
)
cLApCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCountryCode.setStatus("current")


class _CLApCountryAllowed_Type(DisplayString):
    """Custom type cLApCountryAllowed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApCountryAllowed_Type.__name__ = "DisplayString"
_CLApCountryAllowed_Object = MibTableColumn
cLApCountryAllowed = _CLApCountryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1, 2),
    _CLApCountryAllowed_Type()
)
cLApCountryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCountryAllowed.setStatus("current")


class _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Type(TruthValue):
    """Custom type ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled based on TruthValue"""


_CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Object = MibScalar
ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled = _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 4),
    _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Type()
)
ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled.setStatus("current")


class _CiscoLwappApCrashEnabled_Type(TruthValue):
    """Custom type ciscoLwappApCrashEnabled based on TruthValue"""


_CiscoLwappApCrashEnabled_Object = MibScalar
ciscoLwappApCrashEnabled = _CiscoLwappApCrashEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 5),
    _CiscoLwappApCrashEnabled_Type()
)
ciscoLwappApCrashEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApCrashEnabled.setStatus("current")


class _CiscoLwappApUnsupportedEnabled_Type(TruthValue):
    """Custom type ciscoLwappApUnsupportedEnabled based on TruthValue"""


_CiscoLwappApUnsupportedEnabled_Object = MibScalar
ciscoLwappApUnsupportedEnabled = _CiscoLwappApUnsupportedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 6),
    _CiscoLwappApUnsupportedEnabled_Type()
)
ciscoLwappApUnsupportedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApUnsupportedEnabled.setStatus("current")


class _CiscoLwappApAssociatedEnabled_Type(TruthValue):
    """Custom type ciscoLwappApAssociatedEnabled based on TruthValue"""


_CiscoLwappApAssociatedEnabled_Object = MibScalar
ciscoLwappApAssociatedEnabled = _CiscoLwappApAssociatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 7),
    _CiscoLwappApAssociatedEnabled_Type()
)
ciscoLwappApAssociatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApAssociatedEnabled.setStatus("current")
_CiscoLwappApIf_ObjectIdentity = ObjectIdentity
ciscoLwappApIf = _CiscoLwappApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2)
)
_CLApDot11IfTable_Object = MibTable
cLApDot11IfTable = _CLApDot11IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLApDot11IfTable.setStatus("current")
_CLApDot11IfEntry_Object = MibTableRow
cLApDot11IfEntry = _CLApDot11IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1)
)
cLApDot11IfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApDot11IfEntry.setStatus("current")
_CLApDot11IfSlotId_Type = Unsigned32
_CLApDot11IfSlotId_Object = MibTableColumn
cLApDot11IfSlotId = _CLApDot11IfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 1),
    _CLApDot11IfSlotId_Type()
)
cLApDot11IfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApDot11IfSlotId.setStatus("current")
_CLApDot11IfType_Type = CLApIfType
_CLApDot11IfType_Object = MibTableColumn
cLApDot11IfType = _CLApDot11IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 2),
    _CLApDot11IfType_Type()
)
cLApDot11IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfType.setStatus("current")


class _CLApDot11IfRegDomain_Type(DisplayString):
    """Custom type cLApDot11IfRegDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApDot11IfRegDomain_Type.__name__ = "DisplayString"
_CLApDot11IfRegDomain_Object = MibTableColumn
cLApDot11IfRegDomain = _CLApDot11IfRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 3),
    _CLApDot11IfRegDomain_Type()
)
cLApDot11IfRegDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfRegDomain.setStatus("current")
_CLApDot11nSupport_Type = TruthValue
_CLApDot11nSupport_Object = MibTableColumn
cLApDot11nSupport = _CLApDot11nSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 4),
    _CLApDot11nSupport_Type()
)
cLApDot11nSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11nSupport.setStatus("current")


class _CLAp11nChannelBandwidth_Type(Integer32):
    """Custom type cLAp11nChannelBandwidth based on Integer32"""
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
        *(("five", 1),
          ("forty", 4),
          ("ten", 2),
          ("twenty", 3))
    )


_CLAp11nChannelBandwidth_Type.__name__ = "Integer32"
_CLAp11nChannelBandwidth_Object = MibTableColumn
cLAp11nChannelBandwidth = _CLAp11nChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 5),
    _CLAp11nChannelBandwidth_Type()
)
cLAp11nChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11nChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLAp11nChannelBandwidth.setUnits("mhz")


class _CLApLomEnabled_Type(TruthValue):
    """Custom type cLApLomEnabled based on TruthValue"""


_CLApLomEnabled_Object = MibTableColumn
cLApLomEnabled = _CLApLomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 6),
    _CLApLomEnabled_Type()
)
cLApLomEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomEnabled.setStatus("deprecated")
_CLApLomFirstChannel_Type = CLDot11Channel
_CLApLomFirstChannel_Object = MibTableColumn
cLApLomFirstChannel = _CLApLomFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 7),
    _CLApLomFirstChannel_Type()
)
cLApLomFirstChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomFirstChannel.setStatus("current")
_CLApLomSecondChannel_Type = CLDot11Channel
_CLApLomSecondChannel_Object = MibTableColumn
cLApLomSecondChannel = _CLApLomSecondChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 8),
    _CLApLomSecondChannel_Type()
)
cLApLomSecondChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomSecondChannel.setStatus("current")
_CLApLomThirdChannel_Type = CLDot11Channel
_CLApLomThirdChannel_Object = MibTableColumn
cLApLomThirdChannel = _CLApLomThirdChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 9),
    _CLApLomThirdChannel_Type()
)
cLApLomThirdChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomThirdChannel.setStatus("current")
_CLApLomFourthChannel_Type = CLDot11Channel
_CLApLomFourthChannel_Object = MibTableColumn
cLApLomFourthChannel = _CLApLomFourthChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 10),
    _CLApLomFourthChannel_Type()
)
cLApLomFourthChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomFourthChannel.setStatus("current")
_CLApExtensionChannel_Type = CLDot11Channel
_CLApExtensionChannel_Object = MibTableColumn
cLApExtensionChannel = _CLApExtensionChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 11),
    _CLApExtensionChannel_Type()
)
cLApExtensionChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApExtensionChannel.setStatus("current")


class _CLApLegacyBeamForming_Type(Integer32):
    """Custom type cLApLegacyBeamForming based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 3))
    )


_CLApLegacyBeamForming_Type.__name__ = "Integer32"
_CLApLegacyBeamForming_Object = MibTableColumn
cLApLegacyBeamForming = _CLApLegacyBeamForming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 12),
    _CLApLegacyBeamForming_Type()
)
cLApLegacyBeamForming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLegacyBeamForming.setStatus("current")
_CLApCdpOverAirEnabled_Type = TruthValue
_CLApCdpOverAirEnabled_Object = MibTableColumn
cLApCdpOverAirEnabled = _CLApCdpOverAirEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 13),
    _CLApCdpOverAirEnabled_Type()
)
cLApCdpOverAirEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCdpOverAirEnabled.setStatus("current")
_CLApDot11IfAdminStatus_Type = TruthValue
_CLApDot11IfAdminStatus_Object = MibTableColumn
cLApDot11IfAdminStatus = _CLApDot11IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 14),
    _CLApDot11IfAdminStatus_Type()
)
cLApDot11IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAdminStatus.setStatus("current")
_CLApEthernetIfTable_Object = MibTable
cLApEthernetIfTable = _CLApEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLApEthernetIfTable.setStatus("current")
_CLApEthernetIfEntry_Object = MibTableRow
cLApEthernetIfEntry = _CLApEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1)
)
cLApEthernetIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
)
if mibBuilder.loadTexts:
    cLApEthernetIfEntry.setStatus("current")
_CLApEthernetIfSlotId_Type = Unsigned32
_CLApEthernetIfSlotId_Object = MibTableColumn
cLApEthernetIfSlotId = _CLApEthernetIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 1),
    _CLApEthernetIfSlotId_Type()
)
cLApEthernetIfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApEthernetIfSlotId.setStatus("current")


class _CLApEthernetIfName_Type(SnmpAdminString):
    """Custom type cLApEthernetIfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApEthernetIfName_Type.__name__ = "SnmpAdminString"
_CLApEthernetIfName_Object = MibTableColumn
cLApEthernetIfName = _CLApEthernetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 2),
    _CLApEthernetIfName_Type()
)
cLApEthernetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfName.setStatus("current")
_CLApEthernetIfMacAddress_Type = MacAddress
_CLApEthernetIfMacAddress_Object = MibTableColumn
cLApEthernetIfMacAddress = _CLApEthernetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 3),
    _CLApEthernetIfMacAddress_Type()
)
cLApEthernetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfMacAddress.setStatus("current")


class _CLApEthernetIfAdminStatus_Type(Integer32):
    """Custom type cLApEthernetIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CLApEthernetIfAdminStatus_Type.__name__ = "Integer32"
_CLApEthernetIfAdminStatus_Object = MibTableColumn
cLApEthernetIfAdminStatus = _CLApEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 4),
    _CLApEthernetIfAdminStatus_Type()
)
cLApEthernetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEthernetIfAdminStatus.setStatus("current")


class _CLApEthernetIfOperStatus_Type(Integer32):
    """Custom type cLApEthernetIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CLApEthernetIfOperStatus_Type.__name__ = "Integer32"
_CLApEthernetIfOperStatus_Object = MibTableColumn
cLApEthernetIfOperStatus = _CLApEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 5),
    _CLApEthernetIfOperStatus_Type()
)
cLApEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOperStatus.setStatus("current")
_CLApEthernetIfRxUcastPkts_Type = Counter32
_CLApEthernetIfRxUcastPkts_Object = MibTableColumn
cLApEthernetIfRxUcastPkts = _CLApEthernetIfRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 6),
    _CLApEthernetIfRxUcastPkts_Type()
)
cLApEthernetIfRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxUcastPkts.setUnits("packets")
_CLApEthernetIfRxNUcastPkts_Type = Counter32
_CLApEthernetIfRxNUcastPkts_Object = MibTableColumn
cLApEthernetIfRxNUcastPkts = _CLApEthernetIfRxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 7),
    _CLApEthernetIfRxNUcastPkts_Type()
)
cLApEthernetIfRxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxNUcastPkts.setUnits("packets")
_CLApEthernetIfTxUcastPkts_Type = Counter32
_CLApEthernetIfTxUcastPkts_Object = MibTableColumn
cLApEthernetIfTxUcastPkts = _CLApEthernetIfTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 8),
    _CLApEthernetIfTxUcastPkts_Type()
)
cLApEthernetIfTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxUcastPkts.setUnits("packets")
_CLApEthernetIfTxNUcastPkts_Type = Counter32
_CLApEthernetIfTxNUcastPkts_Object = MibTableColumn
cLApEthernetIfTxNUcastPkts = _CLApEthernetIfTxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 9),
    _CLApEthernetIfTxNUcastPkts_Type()
)
cLApEthernetIfTxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxNUcastPkts.setUnits("packets")


class _CLApEthernetIfDuplex_Type(Integer32):
    """Custom type cLApEthernetIfDuplex based on Integer32"""
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
        *(("auto", 4),
          ("fullduplex", 3),
          ("halfduplex", 2),
          ("unknown", 1))
    )


_CLApEthernetIfDuplex_Type.__name__ = "Integer32"
_CLApEthernetIfDuplex_Object = MibTableColumn
cLApEthernetIfDuplex = _CLApEthernetIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 10),
    _CLApEthernetIfDuplex_Type()
)
cLApEthernetIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfDuplex.setStatus("current")
_CLApEthernetIfLinkSpeed_Type = Gauge32
_CLApEthernetIfLinkSpeed_Object = MibTableColumn
cLApEthernetIfLinkSpeed = _CLApEthernetIfLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 11),
    _CLApEthernetIfLinkSpeed_Type()
)
cLApEthernetIfLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfLinkSpeed.setStatus("current")


class _CLApEthernetIfPOEPower_Type(Integer32):
    """Custom type cLApEthernetIfPOEPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drawn", 2),
          ("none", 1),
          ("notdrawn", 3))
    )


_CLApEthernetIfPOEPower_Type.__name__ = "Integer32"
_CLApEthernetIfPOEPower_Object = MibTableColumn
cLApEthernetIfPOEPower = _CLApEthernetIfPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 12),
    _CLApEthernetIfPOEPower_Type()
)
cLApEthernetIfPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfPOEPower.setStatus("current")
_CLApEthernetIfRxTotalBytes_Type = Counter32
_CLApEthernetIfRxTotalBytes_Object = MibTableColumn
cLApEthernetIfRxTotalBytes = _CLApEthernetIfRxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 13),
    _CLApEthernetIfRxTotalBytes_Type()
)
cLApEthernetIfRxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxTotalBytes.setUnits("Bytes")
_CLApEthernetIfTxTotalBytes_Type = Counter32
_CLApEthernetIfTxTotalBytes_Object = MibTableColumn
cLApEthernetIfTxTotalBytes = _CLApEthernetIfTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 14),
    _CLApEthernetIfTxTotalBytes_Type()
)
cLApEthernetIfTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxTotalBytes.setUnits("Bytes")
_CLApEthernetIfInputCrc_Type = Counter32
_CLApEthernetIfInputCrc_Object = MibTableColumn
cLApEthernetIfInputCrc = _CLApEthernetIfInputCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 15),
    _CLApEthernetIfInputCrc_Type()
)
cLApEthernetIfInputCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputCrc.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputCrc.setUnits("packets")
_CLApEthernetIfInputAborts_Type = Counter32
_CLApEthernetIfInputAborts_Object = MibTableColumn
cLApEthernetIfInputAborts = _CLApEthernetIfInputAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 16),
    _CLApEthernetIfInputAborts_Type()
)
cLApEthernetIfInputAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputAborts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputAborts.setUnits("packets")
_CLApEthernetIfInputErrors_Type = Counter32
_CLApEthernetIfInputErrors_Object = MibTableColumn
cLApEthernetIfInputErrors = _CLApEthernetIfInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 17),
    _CLApEthernetIfInputErrors_Type()
)
cLApEthernetIfInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputErrors.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputErrors.setUnits("packets")
_CLApEthernetIfInputFrames_Type = Counter32
_CLApEthernetIfInputFrames_Object = MibTableColumn
cLApEthernetIfInputFrames = _CLApEthernetIfInputFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 18),
    _CLApEthernetIfInputFrames_Type()
)
cLApEthernetIfInputFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputFrames.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputFrames.setUnits("packets")
_CLApEthernetIfInputOverrun_Type = Counter32
_CLApEthernetIfInputOverrun_Object = MibTableColumn
cLApEthernetIfInputOverrun = _CLApEthernetIfInputOverrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 19),
    _CLApEthernetIfInputOverrun_Type()
)
cLApEthernetIfInputOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputOverrun.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputOverrun.setUnits("packets")
_CLApEthernetIfInputDrops_Type = Counter32
_CLApEthernetIfInputDrops_Object = MibTableColumn
cLApEthernetIfInputDrops = _CLApEthernetIfInputDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 20),
    _CLApEthernetIfInputDrops_Type()
)
cLApEthernetIfInputDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputDrops.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputDrops.setUnits("packets")
_CLApEthernetIfInputResource_Type = Counter32
_CLApEthernetIfInputResource_Object = MibTableColumn
cLApEthernetIfInputResource = _CLApEthernetIfInputResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 21),
    _CLApEthernetIfInputResource_Type()
)
cLApEthernetIfInputResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputResource.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputResource.setUnits("packets")
_CLApEthernetIfUnknownProtocol_Type = Counter32
_CLApEthernetIfUnknownProtocol_Object = MibTableColumn
cLApEthernetIfUnknownProtocol = _CLApEthernetIfUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 22),
    _CLApEthernetIfUnknownProtocol_Type()
)
cLApEthernetIfUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfUnknownProtocol.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfUnknownProtocol.setUnits("packets")
_CLApEthernetIfRunts_Type = Counter32
_CLApEthernetIfRunts_Object = MibTableColumn
cLApEthernetIfRunts = _CLApEthernetIfRunts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 23),
    _CLApEthernetIfRunts_Type()
)
cLApEthernetIfRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRunts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRunts.setUnits("packets")
_CLApEthernetIfGiants_Type = Counter32
_CLApEthernetIfGiants_Object = MibTableColumn
cLApEthernetIfGiants = _CLApEthernetIfGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 24),
    _CLApEthernetIfGiants_Type()
)
cLApEthernetIfGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfGiants.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfGiants.setUnits("packets")
_CLApEthernetIfThrottle_Type = Counter32
_CLApEthernetIfThrottle_Object = MibTableColumn
cLApEthernetIfThrottle = _CLApEthernetIfThrottle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 25),
    _CLApEthernetIfThrottle_Type()
)
cLApEthernetIfThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfThrottle.setStatus("current")
_CLApEthernetIfResets_Type = Counter32
_CLApEthernetIfResets_Object = MibTableColumn
cLApEthernetIfResets = _CLApEthernetIfResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 26),
    _CLApEthernetIfResets_Type()
)
cLApEthernetIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfResets.setStatus("current")
_CLApEthernetIfOutputCollision_Type = Counter32
_CLApEthernetIfOutputCollision_Object = MibTableColumn
cLApEthernetIfOutputCollision = _CLApEthernetIfOutputCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 27),
    _CLApEthernetIfOutputCollision_Type()
)
cLApEthernetIfOutputCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputCollision.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputCollision.setUnits("packets")
_CLApEthernetIfOutputNoBuffer_Type = Counter32
_CLApEthernetIfOutputNoBuffer_Object = MibTableColumn
cLApEthernetIfOutputNoBuffer = _CLApEthernetIfOutputNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 28),
    _CLApEthernetIfOutputNoBuffer_Type()
)
cLApEthernetIfOutputNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputNoBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputNoBuffer.setUnits("packets")
_CLApEthernetIfOutputResource_Type = Counter32
_CLApEthernetIfOutputResource_Object = MibTableColumn
cLApEthernetIfOutputResource = _CLApEthernetIfOutputResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 29),
    _CLApEthernetIfOutputResource_Type()
)
cLApEthernetIfOutputResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputResource.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputResource.setUnits("packets")
_CLApEthernetIfOutputUnderrun_Type = Counter32
_CLApEthernetIfOutputUnderrun_Object = MibTableColumn
cLApEthernetIfOutputUnderrun = _CLApEthernetIfOutputUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 30),
    _CLApEthernetIfOutputUnderrun_Type()
)
cLApEthernetIfOutputUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputUnderrun.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputUnderrun.setUnits("packets")
_CLApEthernetIfOutputErrors_Type = Counter32
_CLApEthernetIfOutputErrors_Object = MibTableColumn
cLApEthernetIfOutputErrors = _CLApEthernetIfOutputErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 31),
    _CLApEthernetIfOutputErrors_Type()
)
cLApEthernetIfOutputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputErrors.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputErrors.setUnits("packets")
_CLApEthernetIfOutputTotalDrops_Type = Counter32
_CLApEthernetIfOutputTotalDrops_Object = MibTableColumn
cLApEthernetIfOutputTotalDrops = _CLApEthernetIfOutputTotalDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 32),
    _CLApEthernetIfOutputTotalDrops_Type()
)
cLApEthernetIfOutputTotalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputTotalDrops.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputTotalDrops.setUnits("packets")


class _CLApEthernetIfCdpEnabled_Type(TruthValue):
    """Custom type cLApEthernetIfCdpEnabled based on TruthValue"""


_CLApEthernetIfCdpEnabled_Object = MibTableColumn
cLApEthernetIfCdpEnabled = _CLApEthernetIfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 33),
    _CLApEthernetIfCdpEnabled_Type()
)
cLApEthernetIfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEthernetIfCdpEnabled.setStatus("current")
_CLApDot11RadioTable_Object = MibTable
cLApDot11RadioTable = _CLApDot11RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLApDot11RadioTable.setStatus("current")
_CLApDot11RadioEntry_Object = MibTableRow
cLApDot11RadioEntry = _CLApDot11RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1)
)
cLApDot11RadioEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioEntry.setStatus("current")
_CLApDot11RadioMACAddress_Type = MacAddress
_CLApDot11RadioMACAddress_Object = MibTableColumn
cLApDot11RadioMACAddress = _CLApDot11RadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 1),
    _CLApDot11RadioMACAddress_Type()
)
cLApDot11RadioMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioMACAddress.setStatus("current")
_CLApDot11RadioSubBand_Type = CLApDot11RadioSubband
_CLApDot11RadioSubBand_Object = MibTableColumn
cLApDot11RadioSubBand = _CLApDot11RadioSubBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 2),
    _CLApDot11RadioSubBand_Type()
)
cLApDot11RadioSubBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioSubBand.setStatus("current")


class _CLApDot11RadioVersion_Type(DisplayString):
    """Custom type cLApDot11RadioVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CLApDot11RadioVersion_Type.__name__ = "DisplayString"
_CLApDot11RadioVersion_Object = MibTableColumn
cLApDot11RadioVersion = _CLApDot11RadioVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 3),
    _CLApDot11RadioVersion_Type()
)
cLApDot11RadioVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioVersion.setStatus("current")
_CLApDot11IsBackhaul_Type = TruthValue
_CLApDot11IsBackhaul_Object = MibTableColumn
cLApDot11IsBackhaul = _CLApDot11IsBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 4),
    _CLApDot11IsBackhaul_Type()
)
cLApDot11IsBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IsBackhaul.setStatus("current")
_CLApDot11RadioRole_Type = CLApDot11RadioRole
_CLApDot11RadioRole_Object = MibTableColumn
cLApDot11RadioRole = _CLApDot11RadioRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 5),
    _CLApDot11RadioRole_Type()
)
cLApDot11RadioRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRole.setStatus("current")
_CLApDot11IfAntennaTable_Object = MibTable
cLApDot11IfAntennaTable = _CLApDot11IfAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLApDot11IfAntennaTable.setStatus("current")
_CLApDot11IfAntennaEntry_Object = MibTableRow
cLApDot11IfAntennaEntry = _CLApDot11IfAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1)
)
cLApDot11IfAntennaEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaId"),
)
if mibBuilder.loadTexts:
    cLApDot11IfAntennaEntry.setStatus("current")


class _CLApDot11IfAntennaId_Type(Unsigned32):
    """Custom type cLApDot11IfAntennaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CLApDot11IfAntennaId_Type.__name__ = "Unsigned32"
_CLApDot11IfAntennaId_Object = MibTableColumn
cLApDot11IfAntennaId = _CLApDot11IfAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 1),
    _CLApDot11IfAntennaId_Type()
)
cLApDot11IfAntennaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaId.setStatus("current")


class _CLApDot11IfAntennaTxEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaTxEnable based on TruthValue"""


_CLApDot11IfAntennaTxEnable_Object = MibTableColumn
cLApDot11IfAntennaTxEnable = _CLApDot11IfAntennaTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 2),
    _CLApDot11IfAntennaTxEnable_Type()
)
cLApDot11IfAntennaTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaTxEnable.setStatus("current")


class _CLApDot11IfAntennaRxEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaRxEnable based on TruthValue"""


_CLApDot11IfAntennaRxEnable_Object = MibTableColumn
cLApDot11IfAntennaRxEnable = _CLApDot11IfAntennaRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 3),
    _CLApDot11IfAntennaRxEnable_Type()
)
cLApDot11IfAntennaRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaRxEnable.setStatus("current")


class _CLApDot11IfAntennaEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaEnable based on TruthValue"""


_CLApDot11IfAntennaEnable_Object = MibTableColumn
cLApDot11IfAntennaEnable = _CLApDot11IfAntennaEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 4),
    _CLApDot11IfAntennaEnable_Type()
)
cLApDot11IfAntennaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaEnable.setStatus("current")
_CLApVlanIfTable_Object = MibTable
cLApVlanIfTable = _CLApVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLApVlanIfTable.setStatus("current")
_CLApVlanIfEntry_Object = MibTableRow
cLApVlanIfEntry = _CLApVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1)
)
cLApVlanIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanIfEthernetId"),
)
if mibBuilder.loadTexts:
    cLApVlanIfEntry.setStatus("current")


class _CLApVlanIfEthernetId_Type(Unsigned32):
    """Custom type cLApVlanIfEthernetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CLApVlanIfEthernetId_Type.__name__ = "Unsigned32"
_CLApVlanIfEthernetId_Object = MibTableColumn
cLApVlanIfEthernetId = _CLApVlanIfEthernetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 1),
    _CLApVlanIfEthernetId_Type()
)
cLApVlanIfEthernetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApVlanIfEthernetId.setStatus("current")


class _CLApVlanIfMode_Type(Integer32):
    """Custom type cLApVlanIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("normal", 1),
          ("trunk", 3))
    )


_CLApVlanIfMode_Type.__name__ = "Integer32"
_CLApVlanIfMode_Object = MibTableColumn
cLApVlanIfMode = _CLApVlanIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 2),
    _CLApVlanIfMode_Type()
)
cLApVlanIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfMode.setStatus("current")


class _CLApVlanIfEnable_Type(TruthValue):
    """Custom type cLApVlanIfEnable based on TruthValue"""


_CLApVlanIfEnable_Object = MibTableColumn
cLApVlanIfEnable = _CLApVlanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 3),
    _CLApVlanIfEnable_Type()
)
cLApVlanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfEnable.setStatus("current")
_CLApVlanIfNativeVlanId_Type = Unsigned32
_CLApVlanIfNativeVlanId_Object = MibTableColumn
cLApVlanIfNativeVlanId = _CLApVlanIfNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 4),
    _CLApVlanIfNativeVlanId_Type()
)
cLApVlanIfNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfNativeVlanId.setStatus("current")
_CLApVlanListTable_Object = MibTable
cLApVlanListTable = _CLApVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLApVlanListTable.setStatus("current")
_CLApVlanListEntry_Object = MibTableRow
cLApVlanListEntry = _CLApVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1)
)
cLApVlanListEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanIfEthernetId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanListVlanId"),
)
if mibBuilder.loadTexts:
    cLApVlanListEntry.setStatus("current")
_CLApVlanListVlanId_Type = Unsigned32
_CLApVlanListVlanId_Object = MibTableColumn
cLApVlanListVlanId = _CLApVlanListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1, 1),
    _CLApVlanListVlanId_Type()
)
cLApVlanListVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApVlanListVlanId.setStatus("current")
_CLApVlanListRowStatus_Type = RowStatus
_CLApVlanListRowStatus_Object = MibTableColumn
cLApVlanListRowStatus = _CLApVlanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1, 2),
    _CLApVlanListRowStatus_Type()
)
cLApVlanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApVlanListRowStatus.setStatus("current")
_CLApDot11GlobalConfigTable_Object = MibTable
cLApDot11GlobalConfigTable = _CLApDot11GlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cLApDot11GlobalConfigTable.setStatus("current")
_CLApDot11GlobalConfigEntry_Object = MibTableRow
cLApDot11GlobalConfigEntry = _CLApDot11GlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1)
)
cLApDot11GlobalConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLApDot11GlobalConfigEntry.setStatus("current")


class _CLApNwLegacyBeamForming_Type(Integer32):
    """Custom type cLApNwLegacyBeamForming based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 3))
    )


_CLApNwLegacyBeamForming_Type.__name__ = "Integer32"
_CLApNwLegacyBeamForming_Object = MibTableColumn
cLApNwLegacyBeamForming = _CLApNwLegacyBeamForming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1, 1),
    _CLApNwLegacyBeamForming_Type()
)
cLApNwLegacyBeamForming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNwLegacyBeamForming.setStatus("current")


class _CLApNwTxPowerThreshold_Type(Integer32):
    """Custom type cLApNwTxPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -50),
    )


_CLApNwTxPowerThreshold_Type.__name__ = "Integer32"
_CLApNwTxPowerThreshold_Object = MibTableColumn
cLApNwTxPowerThreshold = _CLApNwTxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1, 2),
    _CLApNwTxPowerThreshold_Type()
)
cLApNwTxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNwTxPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLApNwTxPowerThreshold.setUnits("dbm")
_CiscoLwappApGlobal_ObjectIdentity = ObjectIdentity
ciscoLwappApGlobal = _CiscoLwappApGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3)
)
_CLApFastHbTimerTable_Object = MibTable
cLApFastHbTimerTable = _CLApFastHbTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLApFastHbTimerTable.setStatus("current")
_CLApFastHbTimerEntry_Object = MibTableRow
cLApFastHbTimerEntry = _CLApFastHbTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1)
)
cLApFastHbTimerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApFastHbTimerApType"),
)
if mibBuilder.loadTexts:
    cLApFastHbTimerEntry.setStatus("current")


class _CLApFastHbTimerApType_Type(Integer32):
    """Custom type cLApFastHbTimerApType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hreap", 2),
          ("local", 1))
    )


_CLApFastHbTimerApType_Type.__name__ = "Integer32"
_CLApFastHbTimerApType_Object = MibTableColumn
cLApFastHbTimerApType = _CLApFastHbTimerApType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 1),
    _CLApFastHbTimerApType_Type()
)
cLApFastHbTimerApType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApFastHbTimerApType.setStatus("current")


class _CLApFastHbTimerTimeout_Type(Unsigned32):
    """Custom type cLApFastHbTimerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CLApFastHbTimerTimeout_Type.__name__ = "Unsigned32"
_CLApFastHbTimerTimeout_Object = MibTableColumn
cLApFastHbTimerTimeout = _CLApFastHbTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 2),
    _CLApFastHbTimerTimeout_Type()
)
cLApFastHbTimerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFastHbTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApFastHbTimerTimeout.setUnits("seconds")
_CLApFastHbTimerEnabled_Type = TruthValue
_CLApFastHbTimerEnabled_Object = MibTableColumn
cLApFastHbTimerEnabled = _CLApFastHbTimerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 3),
    _CLApFastHbTimerEnabled_Type()
)
cLApFastHbTimerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFastHbTimerEnabled.setStatus("current")


class _CLApPrimaryDiscoveryTimeout_Type(Unsigned32):
    """Custom type cLApPrimaryDiscoveryTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_CLApPrimaryDiscoveryTimeout_Type.__name__ = "Unsigned32"
_CLApPrimaryDiscoveryTimeout_Object = MibScalar
cLApPrimaryDiscoveryTimeout = _CLApPrimaryDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 3),
    _CLApPrimaryDiscoveryTimeout_Type()
)
cLApPrimaryDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryDiscoveryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApPrimaryDiscoveryTimeout.setUnits("seconds")
_CLApGlobalPrimaryControllerAddressType_Type = InetAddressType
_CLApGlobalPrimaryControllerAddressType_Object = MibScalar
cLApGlobalPrimaryControllerAddressType = _CLApGlobalPrimaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 4),
    _CLApGlobalPrimaryControllerAddressType_Type()
)
cLApGlobalPrimaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerAddressType.setStatus("current")
_CLApGlobalPrimaryControllerAddress_Type = InetAddress
_CLApGlobalPrimaryControllerAddress_Object = MibScalar
cLApGlobalPrimaryControllerAddress = _CLApGlobalPrimaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 5),
    _CLApGlobalPrimaryControllerAddress_Type()
)
cLApGlobalPrimaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerAddress.setStatus("current")


class _CLApGlobalPrimaryControllerName_Type(SnmpAdminString):
    """Custom type cLApGlobalPrimaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApGlobalPrimaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApGlobalPrimaryControllerName_Object = MibScalar
cLApGlobalPrimaryControllerName = _CLApGlobalPrimaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 6),
    _CLApGlobalPrimaryControllerName_Type()
)
cLApGlobalPrimaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerName.setStatus("current")
_CLApGlobalSecondaryControllerAddressType_Type = InetAddressType
_CLApGlobalSecondaryControllerAddressType_Object = MibScalar
cLApGlobalSecondaryControllerAddressType = _CLApGlobalSecondaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 7),
    _CLApGlobalSecondaryControllerAddressType_Type()
)
cLApGlobalSecondaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerAddressType.setStatus("current")
_CLApGlobalSecondaryControllerAddress_Type = InetAddress
_CLApGlobalSecondaryControllerAddress_Object = MibScalar
cLApGlobalSecondaryControllerAddress = _CLApGlobalSecondaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 8),
    _CLApGlobalSecondaryControllerAddress_Type()
)
cLApGlobalSecondaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerAddress.setStatus("current")


class _CLApGlobalSecondaryControllerName_Type(SnmpAdminString):
    """Custom type cLApGlobalSecondaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApGlobalSecondaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApGlobalSecondaryControllerName_Object = MibScalar
cLApGlobalSecondaryControllerName = _CLApGlobalSecondaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 9),
    _CLApGlobalSecondaryControllerName_Type()
)
cLApGlobalSecondaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerName.setStatus("current")


class _CLApGlobalFailoverPriority_Type(TruthValue):
    """Custom type cLApGlobalFailoverPriority based on TruthValue"""


_CLApGlobalFailoverPriority_Object = MibScalar
cLApGlobalFailoverPriority = _CLApGlobalFailoverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 10),
    _CLApGlobalFailoverPriority_Type()
)
cLApGlobalFailoverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalFailoverPriority.setStatus("current")


class _CLApGlobalTcpMss_Type(Integer32):
    """Custom type cLApGlobalTcpMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(536, 1363),
    )


_CLApGlobalTcpMss_Type.__name__ = "Integer32"
_CLApGlobalTcpMss_Object = MibScalar
cLApGlobalTcpMss = _CLApGlobalTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 11),
    _CLApGlobalTcpMss_Type()
)
cLApGlobalTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalTcpMss.setStatus("current")
_CLApGlobalDot11IfTable_Object = MibTable
cLApGlobalDot11IfTable = _CLApGlobalDot11IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cLApGlobalDot11IfTable.setStatus("current")
_CLApGlobalDot11IfEntry_Object = MibTableRow
cLApGlobalDot11IfEntry = _CLApGlobalDot11IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12, 1)
)
cLApGlobalDot11IfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApGlobalDot11IfEntry.setStatus("current")
_CLApGlobalDot11IfCdpEnabled_Type = TruthValue
_CLApGlobalDot11IfCdpEnabled_Object = MibTableColumn
cLApGlobalDot11IfCdpEnabled = _CLApGlobalDot11IfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12, 1, 1),
    _CLApGlobalDot11IfCdpEnabled_Type()
)
cLApGlobalDot11IfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalDot11IfCdpEnabled.setStatus("current")
_CLApGlobalEthernetIfTable_Object = MibTable
cLApGlobalEthernetIfTable = _CLApGlobalEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfTable.setStatus("current")
_CLApGlobalEthernetIfEntry_Object = MibTableRow
cLApGlobalEthernetIfEntry = _CLApGlobalEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13, 1)
)
cLApGlobalEthernetIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
)
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfEntry.setStatus("current")
_CLApGlobalEthernetIfCdpEnabled_Type = TruthValue
_CLApGlobalEthernetIfCdpEnabled_Object = MibTableColumn
cLApGlobalEthernetIfCdpEnabled = _CLApGlobalEthernetIfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13, 1, 1),
    _CLApGlobalEthernetIfCdpEnabled_Type()
)
cLApGlobalEthernetIfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfCdpEnabled.setStatus("current")
_CLApGlobalRetransmitCount_Type = Unsigned32
_CLApGlobalRetransmitCount_Object = MibScalar
cLApGlobalRetransmitCount = _CLApGlobalRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 14),
    _CLApGlobalRetransmitCount_Type()
)
cLApGlobalRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitCount.setUnits("retries")
_CLApGlobalRetransmitTimeout_Type = Unsigned32
_CLApGlobalRetransmitTimeout_Object = MibScalar
cLApGlobalRetransmitTimeout = _CLApGlobalRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 15),
    _CLApGlobalRetransmitTimeout_Type()
)
cLApGlobalRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitTimeout.setUnits("seconds")
_CiscoLwappApCredentials_ObjectIdentity = ObjectIdentity
ciscoLwappApCredentials = _CiscoLwappApCredentials_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4)
)
_CLApCredentialGlobalUserName_Type = SnmpAdminString
_CLApCredentialGlobalUserName_Object = MibScalar
cLApCredentialGlobalUserName = _CLApCredentialGlobalUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 1),
    _CLApCredentialGlobalUserName_Type()
)
cLApCredentialGlobalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalUserName.setStatus("current")
_CLApCredentialGlobalPassword_Type = SnmpAdminString
_CLApCredentialGlobalPassword_Object = MibScalar
cLApCredentialGlobalPassword = _CLApCredentialGlobalPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 2),
    _CLApCredentialGlobalPassword_Type()
)
cLApCredentialGlobalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalPassword.setStatus("current")
_CLApCredentialGlobalSecret_Type = SnmpAdminString
_CLApCredentialGlobalSecret_Object = MibScalar
cLApCredentialGlobalSecret = _CLApCredentialGlobalSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 3),
    _CLApCredentialGlobalSecret_Type()
)
cLApCredentialGlobalSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalSecret.setStatus("current")
_CLApCredentialsTable_Object = MibTable
cLApCredentialsTable = _CLApCredentialsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cLApCredentialsTable.setStatus("current")
_CLApCredentialsEntry_Object = MibTableRow
cLApCredentialsEntry = _CLApCredentialsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1)
)
cLApCredentialsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCredentialsEntry.setStatus("current")
_CLApCredentialUserName_Type = SnmpAdminString
_CLApCredentialUserName_Object = MibTableColumn
cLApCredentialUserName = _CLApCredentialUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 1),
    _CLApCredentialUserName_Type()
)
cLApCredentialUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialUserName.setStatus("current")
_CLApCredentialPassword_Type = SnmpAdminString
_CLApCredentialPassword_Object = MibTableColumn
cLApCredentialPassword = _CLApCredentialPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 2),
    _CLApCredentialPassword_Type()
)
cLApCredentialPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialPassword.setStatus("current")
_CLApCredentialSecret_Type = SnmpAdminString
_CLApCredentialSecret_Object = MibTableColumn
cLApCredentialSecret = _CLApCredentialSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 3),
    _CLApCredentialSecret_Type()
)
cLApCredentialSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialSecret.setStatus("current")
_CLApCredentialEnableGlobalCredentials_Type = TruthValue
_CLApCredentialEnableGlobalCredentials_Object = MibTableColumn
cLApCredentialEnableGlobalCredentials = _CLApCredentialEnableGlobalCredentials_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 4),
    _CLApCredentialEnableGlobalCredentials_Type()
)
cLApCredentialEnableGlobalCredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialEnableGlobalCredentials.setStatus("current")
_CiscoLwappLinkLatency_ObjectIdentity = ObjectIdentity
ciscoLwappLinkLatency = _CiscoLwappLinkLatency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5)
)
_CLApLinkLatencyTable_Object = MibTable
cLApLinkLatencyTable = _CLApLinkLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cLApLinkLatencyTable.setStatus("current")
_CLApLinkLatencyEntry_Object = MibTableRow
cLApLinkLatencyEntry = _CLApLinkLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1)
)
cLApLinkLatencyEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApLinkLatencyEntry.setStatus("current")


class _CLApLinkLatencyEnable_Type(TruthValue):
    """Custom type cLApLinkLatencyEnable based on TruthValue"""


_CLApLinkLatencyEnable_Object = MibTableColumn
cLApLinkLatencyEnable = _CLApLinkLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1, 1),
    _CLApLinkLatencyEnable_Type()
)
cLApLinkLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLinkLatencyEnable.setStatus("current")


class _CLApLinkLatencyReset_Type(TruthValue):
    """Custom type cLApLinkLatencyReset based on TruthValue"""


_CLApLinkLatencyReset_Object = MibTableColumn
cLApLinkLatencyReset = _CLApLinkLatencyReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1, 2),
    _CLApLinkLatencyReset_Type()
)
cLApLinkLatencyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLinkLatencyReset.setStatus("current")
_CLApLinkLatencyStatsTable_Object = MibTable
cLApLinkLatencyStatsTable = _CLApLinkLatencyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsTable.setStatus("current")
_CLApLinkLatencyStatsEntry_Object = MibTableRow
cLApLinkLatencyStatsEntry = _CLApLinkLatencyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1)
)
cLApLinkLatencyStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsEntry.setStatus("current")
_CLApLinkLatencyStatsCurrent_Type = TimeInterval
_CLApLinkLatencyStatsCurrent_Object = MibTableColumn
cLApLinkLatencyStatsCurrent = _CLApLinkLatencyStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 1),
    _CLApLinkLatencyStatsCurrent_Type()
)
cLApLinkLatencyStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsCurrent.setUnits("milliseconds")
_CLApLinkLatencyStatsMin_Type = TimeInterval
_CLApLinkLatencyStatsMin_Object = MibTableColumn
cLApLinkLatencyStatsMin = _CLApLinkLatencyStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 2),
    _CLApLinkLatencyStatsMin_Type()
)
cLApLinkLatencyStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMin.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMin.setUnits("milliseconds")
_CLApLinkLatencyStatsMax_Type = TimeInterval
_CLApLinkLatencyStatsMax_Object = MibTableColumn
cLApLinkLatencyStatsMax = _CLApLinkLatencyStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 3),
    _CLApLinkLatencyStatsMax_Type()
)
cLApLinkLatencyStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMax.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMax.setUnits("milliseconds")
_CLApLinkLatencyTimeStamp_Type = TimeStamp
_CLApLinkLatencyTimeStamp_Object = MibTableColumn
cLApLinkLatencyTimeStamp = _CLApLinkLatencyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 4),
    _CLApLinkLatencyTimeStamp_Type()
)
cLApLinkLatencyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyTimeStamp.setUnits("seconds")
_CLApDataLinkLatencyStatsCurrent_Type = TimeInterval
_CLApDataLinkLatencyStatsCurrent_Object = MibTableColumn
cLApDataLinkLatencyStatsCurrent = _CLApDataLinkLatencyStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 5),
    _CLApDataLinkLatencyStatsCurrent_Type()
)
cLApDataLinkLatencyStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsCurrent.setUnits("milliseconds")
_CLApDataLinkLatencyStatsMin_Type = TimeInterval
_CLApDataLinkLatencyStatsMin_Object = MibTableColumn
cLApDataLinkLatencyStatsMin = _CLApDataLinkLatencyStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 6),
    _CLApDataLinkLatencyStatsMin_Type()
)
cLApDataLinkLatencyStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMin.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMin.setUnits("milliseconds")
_CLApDataLinkLatencyStatsMax_Type = TimeInterval
_CLApDataLinkLatencyStatsMax_Object = MibTableColumn
cLApDataLinkLatencyStatsMax = _CLApDataLinkLatencyStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 7),
    _CLApDataLinkLatencyStatsMax_Type()
)
cLApDataLinkLatencyStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMax.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMax.setUnits("milliseconds")
_CLApDataLinkLatencyTimeStamp_Type = TimeStamp
_CLApDataLinkLatencyTimeStamp_Object = MibTableColumn
cLApDataLinkLatencyTimeStamp = _CLApDataLinkLatencyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 8),
    _CLApDataLinkLatencyTimeStamp_Type()
)
cLApDataLinkLatencyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyTimeStamp.setUnits("seconds")
_CiscoLwappSpectrum_ObjectIdentity = ObjectIdentity
ciscoLwappSpectrum = _CiscoLwappSpectrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6)
)
_CiscoLwappAp802dot1xSupplicant_ObjectIdentity = ObjectIdentity
ciscoLwappAp802dot1xSupplicant = _CiscoLwappAp802dot1xSupplicant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7)
)


class _CLApGlobal802dot1xAuthenticationEnabled_Type(TruthValue):
    """Custom type cLApGlobal802dot1xAuthenticationEnabled based on TruthValue"""


_CLApGlobal802dot1xAuthenticationEnabled_Object = MibScalar
cLApGlobal802dot1xAuthenticationEnabled = _CLApGlobal802dot1xAuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 1),
    _CLApGlobal802dot1xAuthenticationEnabled_Type()
)
cLApGlobal802dot1xAuthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xAuthenticationEnabled.setStatus("current")
_CLApGlobal802dot1xSupplicantUsername_Type = SnmpAdminString
_CLApGlobal802dot1xSupplicantUsername_Object = MibScalar
cLApGlobal802dot1xSupplicantUsername = _CLApGlobal802dot1xSupplicantUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 2),
    _CLApGlobal802dot1xSupplicantUsername_Type()
)
cLApGlobal802dot1xSupplicantUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xSupplicantUsername.setStatus("current")
_CLApGlobal802dot1xSupplicantPassword_Type = SnmpAdminString
_CLApGlobal802dot1xSupplicantPassword_Object = MibScalar
cLApGlobal802dot1xSupplicantPassword = _CLApGlobal802dot1xSupplicantPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 3),
    _CLApGlobal802dot1xSupplicantPassword_Type()
)
cLApGlobal802dot1xSupplicantPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xSupplicantPassword.setStatus("current")
_CLAp802dot1xSupplicantTable_Object = MibTable
cLAp802dot1xSupplicantTable = _CLAp802dot1xSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantTable.setStatus("current")
_CLAp802dot1xSupplicantEntry_Object = MibTableRow
cLAp802dot1xSupplicantEntry = _CLAp802dot1xSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1)
)
cLAp802dot1xSupplicantEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantEntry.setStatus("current")


class _CLAp802dot1xSupplicantOverrideEnabled_Type(TruthValue):
    """Custom type cLAp802dot1xSupplicantOverrideEnabled based on TruthValue"""


_CLAp802dot1xSupplicantOverrideEnabled_Object = MibTableColumn
cLAp802dot1xSupplicantOverrideEnabled = _CLAp802dot1xSupplicantOverrideEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 1),
    _CLAp802dot1xSupplicantOverrideEnabled_Type()
)
cLAp802dot1xSupplicantOverrideEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverrideEnabled.setStatus("current")
_CLAp802dot1xSupplicantOverrideUsername_Type = SnmpAdminString
_CLAp802dot1xSupplicantOverrideUsername_Object = MibTableColumn
cLAp802dot1xSupplicantOverrideUsername = _CLAp802dot1xSupplicantOverrideUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 2),
    _CLAp802dot1xSupplicantOverrideUsername_Type()
)
cLAp802dot1xSupplicantOverrideUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverrideUsername.setStatus("current")
_CLAp802dot1xSupplicantOverridePassword_Type = SnmpAdminString
_CLAp802dot1xSupplicantOverridePassword_Object = MibTableColumn
cLAp802dot1xSupplicantOverridePassword = _CLAp802dot1xSupplicantOverridePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 3),
    _CLAp802dot1xSupplicantOverridePassword_Type()
)
cLAp802dot1xSupplicantOverridePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverridePassword.setStatus("current")
_CLApSeClientTable_Object = MibTable
cLApSeClientTable = _CLApSeClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8)
)
if mibBuilder.loadTexts:
    cLApSeClientTable.setStatus("current")
_CLApSeClientEntry_Object = MibTableRow
cLApSeClientEntry = _CLApSeClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1)
)
cLApSeClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSeIndex"),
)
if mibBuilder.loadTexts:
    cLApSeClientEntry.setStatus("current")
_CLApSeIndex_Type = Integer32
_CLApSeIndex_Object = MibTableColumn
cLApSeIndex = _CLApSeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 1),
    _CLApSeIndex_Type()
)
cLApSeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApSeIndex.setStatus("current")
_CLApSeClientUserName_Type = SnmpAdminString
_CLApSeClientUserName_Object = MibTableColumn
cLApSeClientUserName = _CLApSeClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 2),
    _CLApSeClientUserName_Type()
)
cLApSeClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientUserName.setStatus("current")
_CLApSeClientIPAddrType_Type = InetAddressType
_CLApSeClientIPAddrType_Object = MibTableColumn
cLApSeClientIPAddrType = _CLApSeClientIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 3),
    _CLApSeClientIPAddrType_Type()
)
cLApSeClientIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientIPAddrType.setStatus("current")
_CLApSeClientIPAddr_Type = InetAddress
_CLApSeClientIPAddr_Object = MibTableColumn
cLApSeClientIPAddr = _CLApSeClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 4),
    _CLApSeClientIPAddr_Type()
)
cLApSeClientIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientIPAddr.setStatus("current")
_CLApSeClientDuration_Type = TimeInterval
_CLApSeClientDuration_Object = MibTableColumn
cLApSeClientDuration = _CLApSeClientDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 5),
    _CLApSeClientDuration_Type()
)
cLApSeClientDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientDuration.setStatus("current")
_CLApSeClientPort_Type = InetPortNumber
_CLApSeClientPort_Object = MibTableColumn
cLApSeClientPort = _CLApSeClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 6),
    _CLApSeClientPort_Type()
)
cLApSeClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientPort.setStatus("current")
_CiscoLwappApMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBConform = _CiscoLwappApMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2)
)
_CiscoLwappApMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBCompliances = _CiscoLwappApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1)
)
_CiscoLwappApMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBGroups = _CiscoLwappApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2)
)
_CiscoLwappApMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBNotifObjects = _CiscoLwappApMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3)
)
_CLApAssocFailureReason_Type = CLApAssocFailureReason
_CLApAssocFailureReason_Object = MibScalar
cLApAssocFailureReason = _CLApAssocFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 1),
    _CLApAssocFailureReason_Type()
)
cLApAssocFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApAssocFailureReason.setStatus("current")
_CLApRogueApMacAddress_Type = MacAddress
_CLApRogueApMacAddress_Object = MibScalar
cLApRogueApMacAddress = _CLApRogueApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 2),
    _CLApRogueApMacAddress_Type()
)
cLApRogueApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueApMacAddress.setStatus("current")
_CLApDot11RadioChannelNumber_Type = CLDot11Channel
_CLApDot11RadioChannelNumber_Object = MibScalar
cLApDot11RadioChannelNumber = _CLApDot11RadioChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 3),
    _CLApDot11RadioChannelNumber_Type()
)
cLApDot11RadioChannelNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11RadioChannelNumber.setStatus("current")
_CLApRogueApSsid_Type = SnmpAdminString
_CLApRogueApSsid_Object = MibScalar
cLApRogueApSsid = _CLApRogueApSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 4),
    _CLApRogueApSsid_Type()
)
cLApRogueApSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueApSsid.setStatus("current")


class _CLApRogueType_Type(Integer32):
    """Custom type cLApRogueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asleap", 1),
          ("honeypot", 2),
          ("other", 3))
    )


_CLApRogueType_Type.__name__ = "Integer32"
_CLApRogueType_Object = MibScalar
cLApRogueType = _CLApRogueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 5),
    _CLApRogueType_Type()
)
cLApRogueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueType.setStatus("current")


class _CLApWipsReason_Type(Integer32):
    """Custom type cLApWipsReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noMonitoringDevice", 1)
    )


_CLApWipsReason_Type.__name__ = "Integer32"
_CLApWipsReason_Object = MibScalar
cLApWipsReason = _CLApWipsReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 6),
    _CLApWipsReason_Type()
)
cLApWipsReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApWipsReason.setStatus("current")
_CLApWipsClear_Type = TruthValue
_CLApWipsClear_Object = MibScalar
cLApWipsClear = _CLApWipsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 7),
    _CLApWipsClear_Type()
)
cLApWipsClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApWipsClear.setStatus("current")


class _CLApIfUpDownFailureType_Type(Integer32):
    """Custom type cLApIfUpDownFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuredReset", 2),
          ("detectedFailure", 1))
    )


_CLApIfUpDownFailureType_Type.__name__ = "Integer32"
_CLApIfUpDownFailureType_Object = MibScalar
cLApIfUpDownFailureType = _CLApIfUpDownFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 8),
    _CLApIfUpDownFailureType_Type()
)
cLApIfUpDownFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownFailureType.setStatus("current")
_CLApIfUpDownCause_Type = DisplayString
_CLApIfUpDownCause_Object = MibScalar
cLApIfUpDownCause = _CLApIfUpDownCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 9),
    _CLApIfUpDownCause_Type()
)
cLApIfUpDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownCause.setStatus("current")
_CLApIfUpDownFailureCode_Type = DisplayString
_CLApIfUpDownFailureCode_Object = MibScalar
cLApIfUpDownFailureCode = _CLApIfUpDownFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 10),
    _CLApIfUpDownFailureCode_Type()
)
cLApIfUpDownFailureCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownFailureCode.setStatus("current")

# Managed Objects groups

ciscoLwappApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 1)
)
ciscoLwappApGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfDot11Slots"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroup.setStatus("current")

ciscoLwappApIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 2)
)
ciscoLwappApIfGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType")
)
if mibBuilder.loadTexts:
    ciscoLwappApIfGroup.setStatus("current")

ciscoLwappApGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 3)
)
ciscoLwappApGroupSup1.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApEntPhysicalIndex")
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup1.setStatus("current")

ciscoLwappApGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 4)
)
ciscoLwappApGroupSup2.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup2.setStatus("current")

ciscoLwappApGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 5)
)
ciscoLwappApGroupSup3.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11IfRegDomain"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11nSupport"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11nChannelBandwidth"),
        ("CISCO-LWAPP-AP-MIB", "cLApCountryCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApCountryAllowed"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup3.setStatus("current")

ciscoLwappApNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 6)
)
ciscoLwappApNotifObjsGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApAssocFailureReason")
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifObjsGroup.setStatus("current")

ciscoLwappApGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 8)
)
ciscoLwappApGroupSup4.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappJoinTakenTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfEthernetSlots"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFirstChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomSecondChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomThirdChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFourthChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialEnableGlobalCredentials"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrashEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupportedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociatedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup4.setStatus("deprecated")

ciscoLwappApEthernetIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 9)
)
ciscoLwappApEthernetIfGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApEthernetIfName"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOperStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxNUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxNUcastPkts"))
)
if mibBuilder.loadTexts:
    ciscoLwappApEthernetIfGroup.setStatus("current")

ciscoLwappApRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 10)
)
ciscoLwappApRadioGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSubBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IsBackhaul"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRole"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRadioGroup.setStatus("current")

ciscoLwappApGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 11)
)
ciscoLwappApGroupSup5.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApGlobalFailoverPriority"),
        ("CISCO-LWAPP-AP-MIB", "cLApFailoverPriority"),
        ("CISCO-LWAPP-AP-MIB", "cLApEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyReset"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsCurrent"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsMin"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsMax"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup5.setStatus("current")

ciscoLwappSeClientSup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 12)
)
ciscoLwappSeClientSup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSeClientUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientIPAddrType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientIPAddr"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientPort"))
)
if mibBuilder.loadTexts:
    ciscoLwappSeClientSup.setStatus("current")

ciscoLwappDot11IfAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 13)
)
ciscoLwappDot11IfAntennaGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaEnable")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11IfAntennaGroup.setStatus("current")

ciscoLwappRetransmitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 14)
)
ciscoLwappRetransmitGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApRetransmitTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalRetransmitTimeout"))
)
if mibBuilder.loadTexts:
    ciscoLwappRetransmitGroup.setStatus("current")

ciscoLwappApGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 15)
)
ciscoLwappApGroupSup6.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappJoinTakenTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfEthernetSlots"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFirstChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomSecondChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomThirdChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFourthChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialEnableGlobalCredentials"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrashEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupportedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociatedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup6.setStatus("current")

ciscoLwappApGroupSup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 17)
)
ciscoLwappApGroupSup7.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApTelnetEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApSshEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreStdStateEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorStateEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorSelection"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorSwMacAddr"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApMonitorModeOptimization"),
        ("CISCO-LWAPP-AP-MIB", "cLApDomainName"),
        ("CISCO-LWAPP-AP-MIB", "cLApNameServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApAMSDUEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApEncryptionSupported"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectionEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApCdpOverAirEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalDot11IfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalEthernetIfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfNativeVlanId"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xAuthenticationEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xSupplicantPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xSupplicantUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverrideEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverrideUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverridePassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwTxPowerThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanListRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup7.setStatus("current")


# Notification objects

ciscoLwappApIfRegulatoryDomainMismatchNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 1)
)
ciscoLwappApIfRegulatoryDomainMismatchNotif.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRegDomain"),
        ("CISCO-LWAPP-DOT11-MIB", "cldRegulatoryDomain"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfRegulatoryDomainMismatchNotif.setStatus(
        "current"
    )

ciscoLwappApCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 2)
)
ciscoLwappApCrash.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApCrash.setStatus(
        "obsolete"
    )

ciscoLwappApUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 3)
)
ciscoLwappApUnsupported.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApUnsupported.setStatus(
        "current"
    )

ciscoLwappApAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 4)
)
ciscoLwappApAssociated.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAssociated.setStatus(
        "current"
    )

ciscoLwappApPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 5)
)
ciscoLwappApPower.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPowerStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApPower.setStatus(
        "current"
    )

ciscoLwappApRogueApDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 6)
)
ciscoLwappApRogueApDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRogueApDetected.setStatus(
        "current"
    )

ciscoLwappApRogueApCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 7)
)
ciscoLwappApRogueApCleared.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRogueApCleared.setStatus(
        "current"
    )

ciscoLwappApWipsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 8)
)
ciscoLwappApWipsNotification.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappApWipsNotification.setStatus(
        "current"
    )

ciscoLwappApNoDownlinkChannelNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 9)
)
ciscoLwappApNoDownlinkChannelNotify.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApNoDownlinkChannelNotify.setStatus(
        "current"
    )

ciscoLwappApIfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 10)
)
ciscoLwappApIfUpNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApPortNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfUpNotify.setStatus(
        "current"
    )

ciscoLwappApIfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 11)
)
ciscoLwappApIfDownNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfDownNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappApNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 7)
)
ciscoLwappApNotifsGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotif"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrash"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupported"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociated"))
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsGroup.setStatus(
        "deprecated"
    )

ciscoLwappApNotifsGroupVer1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 16)
)
ciscoLwappApNotifsGroupVer1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotif"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupported"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociated"))
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsGroupVer1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-AP-MIB",
    **{"ciscoLwappApMIB": ciscoLwappApMIB,
       "ciscoLwappApMIBNotifs": ciscoLwappApMIBNotifs,
       "ciscoLwappApIfRegulatoryDomainMismatchNotif": ciscoLwappApIfRegulatoryDomainMismatchNotif,
       "ciscoLwappApCrash": ciscoLwappApCrash,
       "ciscoLwappApUnsupported": ciscoLwappApUnsupported,
       "ciscoLwappApAssociated": ciscoLwappApAssociated,
       "ciscoLwappApPower": ciscoLwappApPower,
       "ciscoLwappApRogueApDetected": ciscoLwappApRogueApDetected,
       "ciscoLwappApRogueApCleared": ciscoLwappApRogueApCleared,
       "ciscoLwappApWipsNotification": ciscoLwappApWipsNotification,
       "ciscoLwappApNoDownlinkChannelNotify": ciscoLwappApNoDownlinkChannelNotify,
       "ciscoLwappApIfUpNotify": ciscoLwappApIfUpNotify,
       "ciscoLwappApIfDownNotify": ciscoLwappApIfDownNotify,
       "ciscoLwappApMIBObjects": ciscoLwappApMIBObjects,
       "ciscoLwappAp": ciscoLwappAp,
       "cLApTable": cLApTable,
       "cLApEntry": cLApEntry,
       "cLApSysMacAddress": cLApSysMacAddress,
       "cLApIfMacAddress": cLApIfMacAddress,
       "cLApMaxNumberOfDot11Slots": cLApMaxNumberOfDot11Slots,
       "cLApEntPhysicalIndex": cLApEntPhysicalIndex,
       "cLApName": cLApName,
       "cLApUpTime": cLApUpTime,
       "cLLwappUpTime": cLLwappUpTime,
       "cLLwappJoinTakenTime": cLLwappJoinTakenTime,
       "cLApMaxNumberOfEthernetSlots": cLApMaxNumberOfEthernetSlots,
       "cLApPrimaryControllerAddressType": cLApPrimaryControllerAddressType,
       "cLApPrimaryControllerAddress": cLApPrimaryControllerAddress,
       "cLApSecondaryControllerAddressType": cLApSecondaryControllerAddressType,
       "cLApSecondaryControllerAddress": cLApSecondaryControllerAddress,
       "cLApTertiaryControllerAddressType": cLApTertiaryControllerAddressType,
       "cLApTertiaryControllerAddress": cLApTertiaryControllerAddress,
       "cLApLastRebootReason": cLApLastRebootReason,
       "cLApEncryptionEnable": cLApEncryptionEnable,
       "cLApFailoverPriority": cLApFailoverPriority,
       "cLApPowerStatus": cLApPowerStatus,
       "cLApTelnetEnable": cLApTelnetEnable,
       "cLApSshEnable": cLApSshEnable,
       "cLApPreStdStateEnabled": cLApPreStdStateEnabled,
       "cLApPwrInjectorStateEnabled": cLApPwrInjectorStateEnabled,
       "cLApPwrInjectorSelection": cLApPwrInjectorSelection,
       "cLApPwrInjectorSwMacAddr": cLApPwrInjectorSwMacAddr,
       "cLApWipsEnable": cLApWipsEnable,
       "cLApMonitorModeOptimization": cLApMonitorModeOptimization,
       "cLApDomainName": cLApDomainName,
       "cLApNameServerAddressType": cLApNameServerAddressType,
       "cLApNameServerAddress": cLApNameServerAddress,
       "cLApAMSDUEnable": cLApAMSDUEnable,
       "cLApEncryptionSupported": cLApEncryptionSupported,
       "cLApRogueDetectionEnabled": cLApRogueDetectionEnabled,
       "cLApTcpMss": cLApTcpMss,
       "cLApDataEncryptionStatus": cLApDataEncryptionStatus,
       "cLApNsiKey": cLApNsiKey,
       "cLApAdminStatus": cLApAdminStatus,
       "cLApPortNumber": cLApPortNumber,
       "cLApRetransmitCount": cLApRetransmitCount,
       "cLApRetransmitTimeout": cLApRetransmitTimeout,
       "cLApIfSmtParamTable": cLApIfSmtParamTable,
       "cLApIfSmtParamEntry": cLApIfSmtParamEntry,
       "cLApIfSmtDot11Bssid": cLApIfSmtDot11Bssid,
       "cLApCountryTable": cLApCountryTable,
       "cLApCountryEntry": cLApCountryEntry,
       "cLApCountryCode": cLApCountryCode,
       "cLApCountryAllowed": cLApCountryAllowed,
       "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled": ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled,
       "ciscoLwappApCrashEnabled": ciscoLwappApCrashEnabled,
       "ciscoLwappApUnsupportedEnabled": ciscoLwappApUnsupportedEnabled,
       "ciscoLwappApAssociatedEnabled": ciscoLwappApAssociatedEnabled,
       "ciscoLwappApIf": ciscoLwappApIf,
       "cLApDot11IfTable": cLApDot11IfTable,
       "cLApDot11IfEntry": cLApDot11IfEntry,
       "cLApDot11IfSlotId": cLApDot11IfSlotId,
       "cLApDot11IfType": cLApDot11IfType,
       "cLApDot11IfRegDomain": cLApDot11IfRegDomain,
       "cLApDot11nSupport": cLApDot11nSupport,
       "cLAp11nChannelBandwidth": cLAp11nChannelBandwidth,
       "cLApLomEnabled": cLApLomEnabled,
       "cLApLomFirstChannel": cLApLomFirstChannel,
       "cLApLomSecondChannel": cLApLomSecondChannel,
       "cLApLomThirdChannel": cLApLomThirdChannel,
       "cLApLomFourthChannel": cLApLomFourthChannel,
       "cLApExtensionChannel": cLApExtensionChannel,
       "cLApLegacyBeamForming": cLApLegacyBeamForming,
       "cLApCdpOverAirEnabled": cLApCdpOverAirEnabled,
       "cLApDot11IfAdminStatus": cLApDot11IfAdminStatus,
       "cLApEthernetIfTable": cLApEthernetIfTable,
       "cLApEthernetIfEntry": cLApEthernetIfEntry,
       "cLApEthernetIfSlotId": cLApEthernetIfSlotId,
       "cLApEthernetIfName": cLApEthernetIfName,
       "cLApEthernetIfMacAddress": cLApEthernetIfMacAddress,
       "cLApEthernetIfAdminStatus": cLApEthernetIfAdminStatus,
       "cLApEthernetIfOperStatus": cLApEthernetIfOperStatus,
       "cLApEthernetIfRxUcastPkts": cLApEthernetIfRxUcastPkts,
       "cLApEthernetIfRxNUcastPkts": cLApEthernetIfRxNUcastPkts,
       "cLApEthernetIfTxUcastPkts": cLApEthernetIfTxUcastPkts,
       "cLApEthernetIfTxNUcastPkts": cLApEthernetIfTxNUcastPkts,
       "cLApEthernetIfDuplex": cLApEthernetIfDuplex,
       "cLApEthernetIfLinkSpeed": cLApEthernetIfLinkSpeed,
       "cLApEthernetIfPOEPower": cLApEthernetIfPOEPower,
       "cLApEthernetIfRxTotalBytes": cLApEthernetIfRxTotalBytes,
       "cLApEthernetIfTxTotalBytes": cLApEthernetIfTxTotalBytes,
       "cLApEthernetIfInputCrc": cLApEthernetIfInputCrc,
       "cLApEthernetIfInputAborts": cLApEthernetIfInputAborts,
       "cLApEthernetIfInputErrors": cLApEthernetIfInputErrors,
       "cLApEthernetIfInputFrames": cLApEthernetIfInputFrames,
       "cLApEthernetIfInputOverrun": cLApEthernetIfInputOverrun,
       "cLApEthernetIfInputDrops": cLApEthernetIfInputDrops,
       "cLApEthernetIfInputResource": cLApEthernetIfInputResource,
       "cLApEthernetIfUnknownProtocol": cLApEthernetIfUnknownProtocol,
       "cLApEthernetIfRunts": cLApEthernetIfRunts,
       "cLApEthernetIfGiants": cLApEthernetIfGiants,
       "cLApEthernetIfThrottle": cLApEthernetIfThrottle,
       "cLApEthernetIfResets": cLApEthernetIfResets,
       "cLApEthernetIfOutputCollision": cLApEthernetIfOutputCollision,
       "cLApEthernetIfOutputNoBuffer": cLApEthernetIfOutputNoBuffer,
       "cLApEthernetIfOutputResource": cLApEthernetIfOutputResource,
       "cLApEthernetIfOutputUnderrun": cLApEthernetIfOutputUnderrun,
       "cLApEthernetIfOutputErrors": cLApEthernetIfOutputErrors,
       "cLApEthernetIfOutputTotalDrops": cLApEthernetIfOutputTotalDrops,
       "cLApEthernetIfCdpEnabled": cLApEthernetIfCdpEnabled,
       "cLApDot11RadioTable": cLApDot11RadioTable,
       "cLApDot11RadioEntry": cLApDot11RadioEntry,
       "cLApDot11RadioMACAddress": cLApDot11RadioMACAddress,
       "cLApDot11RadioSubBand": cLApDot11RadioSubBand,
       "cLApDot11RadioVersion": cLApDot11RadioVersion,
       "cLApDot11IsBackhaul": cLApDot11IsBackhaul,
       "cLApDot11RadioRole": cLApDot11RadioRole,
       "cLApDot11IfAntennaTable": cLApDot11IfAntennaTable,
       "cLApDot11IfAntennaEntry": cLApDot11IfAntennaEntry,
       "cLApDot11IfAntennaId": cLApDot11IfAntennaId,
       "cLApDot11IfAntennaTxEnable": cLApDot11IfAntennaTxEnable,
       "cLApDot11IfAntennaRxEnable": cLApDot11IfAntennaRxEnable,
       "cLApDot11IfAntennaEnable": cLApDot11IfAntennaEnable,
       "cLApVlanIfTable": cLApVlanIfTable,
       "cLApVlanIfEntry": cLApVlanIfEntry,
       "cLApVlanIfEthernetId": cLApVlanIfEthernetId,
       "cLApVlanIfMode": cLApVlanIfMode,
       "cLApVlanIfEnable": cLApVlanIfEnable,
       "cLApVlanIfNativeVlanId": cLApVlanIfNativeVlanId,
       "cLApVlanListTable": cLApVlanListTable,
       "cLApVlanListEntry": cLApVlanListEntry,
       "cLApVlanListVlanId": cLApVlanListVlanId,
       "cLApVlanListRowStatus": cLApVlanListRowStatus,
       "cLApDot11GlobalConfigTable": cLApDot11GlobalConfigTable,
       "cLApDot11GlobalConfigEntry": cLApDot11GlobalConfigEntry,
       "cLApNwLegacyBeamForming": cLApNwLegacyBeamForming,
       "cLApNwTxPowerThreshold": cLApNwTxPowerThreshold,
       "ciscoLwappApGlobal": ciscoLwappApGlobal,
       "cLApFastHbTimerTable": cLApFastHbTimerTable,
       "cLApFastHbTimerEntry": cLApFastHbTimerEntry,
       "cLApFastHbTimerApType": cLApFastHbTimerApType,
       "cLApFastHbTimerTimeout": cLApFastHbTimerTimeout,
       "cLApFastHbTimerEnabled": cLApFastHbTimerEnabled,
       "cLApPrimaryDiscoveryTimeout": cLApPrimaryDiscoveryTimeout,
       "cLApGlobalPrimaryControllerAddressType": cLApGlobalPrimaryControllerAddressType,
       "cLApGlobalPrimaryControllerAddress": cLApGlobalPrimaryControllerAddress,
       "cLApGlobalPrimaryControllerName": cLApGlobalPrimaryControllerName,
       "cLApGlobalSecondaryControllerAddressType": cLApGlobalSecondaryControllerAddressType,
       "cLApGlobalSecondaryControllerAddress": cLApGlobalSecondaryControllerAddress,
       "cLApGlobalSecondaryControllerName": cLApGlobalSecondaryControllerName,
       "cLApGlobalFailoverPriority": cLApGlobalFailoverPriority,
       "cLApGlobalTcpMss": cLApGlobalTcpMss,
       "cLApGlobalDot11IfTable": cLApGlobalDot11IfTable,
       "cLApGlobalDot11IfEntry": cLApGlobalDot11IfEntry,
       "cLApGlobalDot11IfCdpEnabled": cLApGlobalDot11IfCdpEnabled,
       "cLApGlobalEthernetIfTable": cLApGlobalEthernetIfTable,
       "cLApGlobalEthernetIfEntry": cLApGlobalEthernetIfEntry,
       "cLApGlobalEthernetIfCdpEnabled": cLApGlobalEthernetIfCdpEnabled,
       "cLApGlobalRetransmitCount": cLApGlobalRetransmitCount,
       "cLApGlobalRetransmitTimeout": cLApGlobalRetransmitTimeout,
       "ciscoLwappApCredentials": ciscoLwappApCredentials,
       "cLApCredentialGlobalUserName": cLApCredentialGlobalUserName,
       "cLApCredentialGlobalPassword": cLApCredentialGlobalPassword,
       "cLApCredentialGlobalSecret": cLApCredentialGlobalSecret,
       "cLApCredentialsTable": cLApCredentialsTable,
       "cLApCredentialsEntry": cLApCredentialsEntry,
       "cLApCredentialUserName": cLApCredentialUserName,
       "cLApCredentialPassword": cLApCredentialPassword,
       "cLApCredentialSecret": cLApCredentialSecret,
       "cLApCredentialEnableGlobalCredentials": cLApCredentialEnableGlobalCredentials,
       "ciscoLwappLinkLatency": ciscoLwappLinkLatency,
       "cLApLinkLatencyTable": cLApLinkLatencyTable,
       "cLApLinkLatencyEntry": cLApLinkLatencyEntry,
       "cLApLinkLatencyEnable": cLApLinkLatencyEnable,
       "cLApLinkLatencyReset": cLApLinkLatencyReset,
       "cLApLinkLatencyStatsTable": cLApLinkLatencyStatsTable,
       "cLApLinkLatencyStatsEntry": cLApLinkLatencyStatsEntry,
       "cLApLinkLatencyStatsCurrent": cLApLinkLatencyStatsCurrent,
       "cLApLinkLatencyStatsMin": cLApLinkLatencyStatsMin,
       "cLApLinkLatencyStatsMax": cLApLinkLatencyStatsMax,
       "cLApLinkLatencyTimeStamp": cLApLinkLatencyTimeStamp,
       "cLApDataLinkLatencyStatsCurrent": cLApDataLinkLatencyStatsCurrent,
       "cLApDataLinkLatencyStatsMin": cLApDataLinkLatencyStatsMin,
       "cLApDataLinkLatencyStatsMax": cLApDataLinkLatencyStatsMax,
       "cLApDataLinkLatencyTimeStamp": cLApDataLinkLatencyTimeStamp,
       "ciscoLwappSpectrum": ciscoLwappSpectrum,
       "ciscoLwappAp802dot1xSupplicant": ciscoLwappAp802dot1xSupplicant,
       "cLApGlobal802dot1xAuthenticationEnabled": cLApGlobal802dot1xAuthenticationEnabled,
       "cLApGlobal802dot1xSupplicantUsername": cLApGlobal802dot1xSupplicantUsername,
       "cLApGlobal802dot1xSupplicantPassword": cLApGlobal802dot1xSupplicantPassword,
       "cLAp802dot1xSupplicantTable": cLAp802dot1xSupplicantTable,
       "cLAp802dot1xSupplicantEntry": cLAp802dot1xSupplicantEntry,
       "cLAp802dot1xSupplicantOverrideEnabled": cLAp802dot1xSupplicantOverrideEnabled,
       "cLAp802dot1xSupplicantOverrideUsername": cLAp802dot1xSupplicantOverrideUsername,
       "cLAp802dot1xSupplicantOverridePassword": cLAp802dot1xSupplicantOverridePassword,
       "cLApSeClientTable": cLApSeClientTable,
       "cLApSeClientEntry": cLApSeClientEntry,
       "cLApSeIndex": cLApSeIndex,
       "cLApSeClientUserName": cLApSeClientUserName,
       "cLApSeClientIPAddrType": cLApSeClientIPAddrType,
       "cLApSeClientIPAddr": cLApSeClientIPAddr,
       "cLApSeClientDuration": cLApSeClientDuration,
       "cLApSeClientPort": cLApSeClientPort,
       "ciscoLwappApMIBConform": ciscoLwappApMIBConform,
       "ciscoLwappApMIBCompliances": ciscoLwappApMIBCompliances,
       "ciscoLwappApMIBCompliance": ciscoLwappApMIBCompliance,
       "ciscoLwappApMIBComplianceRev1": ciscoLwappApMIBComplianceRev1,
       "ciscoLwappApMIBComplianceRev2": ciscoLwappApMIBComplianceRev2,
       "ciscoLwappApMIBComplianceRev3": ciscoLwappApMIBComplianceRev3,
       "ciscoLwappApMIBComplianceRev4": ciscoLwappApMIBComplianceRev4,
       "ciscoLwappApMIBComplianceRev5": ciscoLwappApMIBComplianceRev5,
       "ciscoLwappApMIBComplianceRev6": ciscoLwappApMIBComplianceRev6,
       "ciscoLwappApMIBComplianceRev7": ciscoLwappApMIBComplianceRev7,
       "ciscoLwappApMIBGroups": ciscoLwappApMIBGroups,
       "ciscoLwappApGroup": ciscoLwappApGroup,
       "ciscoLwappApIfGroup": ciscoLwappApIfGroup,
       "ciscoLwappApGroupSup1": ciscoLwappApGroupSup1,
       "ciscoLwappApGroupSup2": ciscoLwappApGroupSup2,
       "ciscoLwappApGroupSup3": ciscoLwappApGroupSup3,
       "ciscoLwappApNotifObjsGroup": ciscoLwappApNotifObjsGroup,
       "ciscoLwappApNotifsGroup": ciscoLwappApNotifsGroup,
       "ciscoLwappApGroupSup4": ciscoLwappApGroupSup4,
       "ciscoLwappApEthernetIfGroup": ciscoLwappApEthernetIfGroup,
       "ciscoLwappApRadioGroup": ciscoLwappApRadioGroup,
       "ciscoLwappApGroupSup5": ciscoLwappApGroupSup5,
       "ciscoLwappSeClientSup": ciscoLwappSeClientSup,
       "ciscoLwappDot11IfAntennaGroup": ciscoLwappDot11IfAntennaGroup,
       "ciscoLwappRetransmitGroup": ciscoLwappRetransmitGroup,
       "ciscoLwappApGroupSup6": ciscoLwappApGroupSup6,
       "ciscoLwappApNotifsGroupVer1": ciscoLwappApNotifsGroupVer1,
       "ciscoLwappApGroupSup7": ciscoLwappApGroupSup7,
       "ciscoLwappApMIBNotifObjects": ciscoLwappApMIBNotifObjects,
       "cLApAssocFailureReason": cLApAssocFailureReason,
       "cLApRogueApMacAddress": cLApRogueApMacAddress,
       "cLApDot11RadioChannelNumber": cLApDot11RadioChannelNumber,
       "cLApRogueApSsid": cLApRogueApSsid,
       "cLApRogueType": cLApRogueType,
       "cLApWipsReason": cLApWipsReason,
       "cLApWipsClear": cLApWipsClear,
       "cLApIfUpDownFailureType": cLApIfUpDownFailureType,
       "cLApIfUpDownCause": cLApIfUpDownCause,
       "cLApIfUpDownFailureCode": cLApIfUpDownFailureCode}
)
