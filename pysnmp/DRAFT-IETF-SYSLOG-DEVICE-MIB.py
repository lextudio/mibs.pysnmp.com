# SNMP MIB module (DRAFT-IETF-SYSLOG-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DRAFT-IETF-SYSLOG-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:27 2024
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

(rlSyslog,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rlSyslog")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

snmpSyslogDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1)
)
snmpSyslogDeviceMIB.setRevisions(
        ("2002-06-06 18:41",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogUdpPort(Unsigned32, TextualConvention):
    status = "current"


class SyslogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("no-map", 24))
    )



class SyslogSeverity(Integer32, TextualConvention):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_SnmpSyslogDevice_ObjectIdentity = ObjectIdentity
snmpSyslogDevice = _SnmpSyslogDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 1)
)
_SnmpSyslogDeviceMessages_Type = Counter32
_SnmpSyslogDeviceMessages_Object = MibScalar
snmpSyslogDeviceMessages = _SnmpSyslogDeviceMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 1, 1),
    _SnmpSyslogDeviceMessages_Type()
)
snmpSyslogDeviceMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogDeviceMessages.setStatus("current")
_SnmpSyslogDeviceMessagesDropped_Type = Counter32
_SnmpSyslogDeviceMessagesDropped_Object = MibScalar
snmpSyslogDeviceMessagesDropped = _SnmpSyslogDeviceMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 1, 2),
    _SnmpSyslogDeviceMessagesDropped_Type()
)
snmpSyslogDeviceMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogDeviceMessagesDropped.setStatus("current")
_SnmpSyslogDeviceLastMessageTime_Type = TimeStamp
_SnmpSyslogDeviceLastMessageTime_Object = MibScalar
snmpSyslogDeviceLastMessageTime = _SnmpSyslogDeviceLastMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 1, 3),
    _SnmpSyslogDeviceLastMessageTime_Type()
)
snmpSyslogDeviceLastMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogDeviceLastMessageTime.setStatus("current")


class _SnmpSyslogDeviceControl_Type(Bits):
    """Custom type snmpSyslogDeviceControl based on Bits"""
    namedValues = NamedValues(
        ("snmpSyslogDeviceControlConsoleLogging", 0)
    )

_SnmpSyslogDeviceControl_Type.__name__ = "Bits"
_SnmpSyslogDeviceControl_Object = MibScalar
snmpSyslogDeviceControl = _SnmpSyslogDeviceControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 1, 4),
    _SnmpSyslogDeviceControl_Type()
)
snmpSyslogDeviceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslogDeviceControl.setStatus("current")
_SnmpSyslogCollector_ObjectIdentity = ObjectIdentity
snmpSyslogCollector = _SnmpSyslogCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2)
)


class _SnmpSyslogCollectorMaxEntries_Type(Unsigned32):
    """Custom type snmpSyslogCollectorMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpSyslogCollectorMaxEntries_Type.__name__ = "Unsigned32"
_SnmpSyslogCollectorMaxEntries_Object = MibScalar
snmpSyslogCollectorMaxEntries = _SnmpSyslogCollectorMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 1),
    _SnmpSyslogCollectorMaxEntries_Type()
)
snmpSyslogCollectorMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogCollectorMaxEntries.setStatus("current")
_SnmpSyslogCollectorNumEntries_Type = Gauge32
_SnmpSyslogCollectorNumEntries_Object = MibScalar
snmpSyslogCollectorNumEntries = _SnmpSyslogCollectorNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 2),
    _SnmpSyslogCollectorNumEntries_Type()
)
snmpSyslogCollectorNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogCollectorNumEntries.setStatus("current")


class _SnmpSyslogCollectorTableNextAvailableIndex_Type(Unsigned32):
    """Custom type snmpSyslogCollectorTableNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnmpSyslogCollectorTableNextAvailableIndex_Type.__name__ = "Unsigned32"
_SnmpSyslogCollectorTableNextAvailableIndex_Object = MibScalar
snmpSyslogCollectorTableNextAvailableIndex = _SnmpSyslogCollectorTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 3),
    _SnmpSyslogCollectorTableNextAvailableIndex_Type()
)
snmpSyslogCollectorTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogCollectorTableNextAvailableIndex.setStatus("current")
_SnmpSyslogCollectorTable_Object = MibTable
snmpSyslogCollectorTable = _SnmpSyslogCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4)
)
if mibBuilder.loadTexts:
    snmpSyslogCollectorTable.setStatus("current")
_SnmpSyslogCollectorEntry_Object = MibTableRow
snmpSyslogCollectorEntry = _SnmpSyslogCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1)
)
snmpSyslogCollectorEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorIndex"),
)
if mibBuilder.loadTexts:
    snmpSyslogCollectorEntry.setStatus("current")


class _SnmpSyslogCollectorIndex_Type(Unsigned32):
    """Custom type snmpSyslogCollectorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpSyslogCollectorIndex_Type.__name__ = "Unsigned32"
_SnmpSyslogCollectorIndex_Object = MibTableColumn
snmpSyslogCollectorIndex = _SnmpSyslogCollectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 1),
    _SnmpSyslogCollectorIndex_Type()
)
snmpSyslogCollectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpSyslogCollectorIndex.setStatus("current")


class _SnmpSyslogCollectorDescription_Type(SnmpAdminString):
    """Custom type snmpSyslogCollectorDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnmpSyslogCollectorDescription_Type.__name__ = "SnmpAdminString"
_SnmpSyslogCollectorDescription_Object = MibTableColumn
snmpSyslogCollectorDescription = _SnmpSyslogCollectorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 2),
    _SnmpSyslogCollectorDescription_Type()
)
snmpSyslogCollectorDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorDescription.setStatus("current")
_SnmpSyslogCollectorAddressType_Type = InetAddressType
_SnmpSyslogCollectorAddressType_Object = MibTableColumn
snmpSyslogCollectorAddressType = _SnmpSyslogCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 3),
    _SnmpSyslogCollectorAddressType_Type()
)
snmpSyslogCollectorAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorAddressType.setStatus("current")
_SnmpSyslogCollectorAddress_Type = InetAddress
_SnmpSyslogCollectorAddress_Object = MibTableColumn
snmpSyslogCollectorAddress = _SnmpSyslogCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 4),
    _SnmpSyslogCollectorAddress_Type()
)
snmpSyslogCollectorAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorAddress.setStatus("current")
_SnmpSyslogCollectorUdpPort_Type = SyslogUdpPort
_SnmpSyslogCollectorUdpPort_Object = MibTableColumn
snmpSyslogCollectorUdpPort = _SnmpSyslogCollectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 5),
    _SnmpSyslogCollectorUdpPort_Type()
)
snmpSyslogCollectorUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorUdpPort.setStatus("current")
_SnmpSyslogCollectorFacility_Type = SyslogFacility
_SnmpSyslogCollectorFacility_Object = MibTableColumn
snmpSyslogCollectorFacility = _SnmpSyslogCollectorFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 6),
    _SnmpSyslogCollectorFacility_Type()
)
snmpSyslogCollectorFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorFacility.setStatus("current")
_SnmpSyslogCollectorSeverity_Type = SyslogSeverity
_SnmpSyslogCollectorSeverity_Object = MibTableColumn
snmpSyslogCollectorSeverity = _SnmpSyslogCollectorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 7),
    _SnmpSyslogCollectorSeverity_Type()
)
snmpSyslogCollectorSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorSeverity.setStatus("current")
_SnmpSyslogCollectorMessagesIgnored_Type = Counter32
_SnmpSyslogCollectorMessagesIgnored_Object = MibTableColumn
snmpSyslogCollectorMessagesIgnored = _SnmpSyslogCollectorMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 8),
    _SnmpSyslogCollectorMessagesIgnored_Type()
)
snmpSyslogCollectorMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogCollectorMessagesIgnored.setStatus("current")
_SnmpSyslogCollectorRowStatus_Type = RowStatus
_SnmpSyslogCollectorRowStatus_Object = MibTableColumn
snmpSyslogCollectorRowStatus = _SnmpSyslogCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 4, 1, 9),
    _SnmpSyslogCollectorRowStatus_Type()
)
snmpSyslogCollectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpSyslogCollectorRowStatus.setStatus("current")


class _SnmpSyslogCollectorDefaultUdpPort_Type(SyslogUdpPort):
    """Custom type snmpSyslogCollectorDefaultUdpPort based on SyslogUdpPort"""
    defaultValue = 514


_SnmpSyslogCollectorDefaultUdpPort_Object = MibScalar
snmpSyslogCollectorDefaultUdpPort = _SnmpSyslogCollectorDefaultUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 5),
    _SnmpSyslogCollectorDefaultUdpPort_Type()
)
snmpSyslogCollectorDefaultUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslogCollectorDefaultUdpPort.setStatus("current")


class _SnmpSyslogCollectorDefaultFacility_Type(SyslogFacility):
    """Custom type snmpSyslogCollectorDefaultFacility based on SyslogFacility"""


_SnmpSyslogCollectorDefaultFacility_Object = MibScalar
snmpSyslogCollectorDefaultFacility = _SnmpSyslogCollectorDefaultFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 6),
    _SnmpSyslogCollectorDefaultFacility_Type()
)
snmpSyslogCollectorDefaultFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslogCollectorDefaultFacility.setStatus("current")


class _SnmpSyslogCollectorDefaultSeverity_Type(SyslogSeverity):
    """Custom type snmpSyslogCollectorDefaultSeverity based on SyslogSeverity"""


_SnmpSyslogCollectorDefaultSeverity_Object = MibScalar
snmpSyslogCollectorDefaultSeverity = _SnmpSyslogCollectorDefaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 2, 7),
    _SnmpSyslogCollectorDefaultSeverity_Type()
)
snmpSyslogCollectorDefaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslogCollectorDefaultSeverity.setStatus("current")
_SnmpSyslogApplication_ObjectIdentity = ObjectIdentity
snmpSyslogApplication = _SnmpSyslogApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3)
)
_SnmpSyslogApplicationTable_Object = MibTable
snmpSyslogApplicationTable = _SnmpSyslogApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snmpSyslogApplicationTable.setStatus("current")
_SnmpSyslogApplicationEntry_Object = MibTableRow
snmpSyslogApplicationEntry = _SnmpSyslogApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1, 1)
)
snmpSyslogApplicationEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogApplicationIndex"),
)
if mibBuilder.loadTexts:
    snmpSyslogApplicationEntry.setStatus("current")
_SnmpSyslogApplicationIndex_Type = Unsigned32
_SnmpSyslogApplicationIndex_Object = MibTableColumn
snmpSyslogApplicationIndex = _SnmpSyslogApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1, 1, 1),
    _SnmpSyslogApplicationIndex_Type()
)
snmpSyslogApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpSyslogApplicationIndex.setStatus("current")


class _SnmpSyslogApplicationDescription_Type(SnmpAdminString):
    """Custom type snmpSyslogApplicationDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnmpSyslogApplicationDescription_Type.__name__ = "SnmpAdminString"
_SnmpSyslogApplicationDescription_Object = MibTableColumn
snmpSyslogApplicationDescription = _SnmpSyslogApplicationDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1, 1, 2),
    _SnmpSyslogApplicationDescription_Type()
)
snmpSyslogApplicationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogApplicationDescription.setStatus("current")


class _SnmpSyslogApplicationMnemonic_Type(SnmpAdminString):
    """Custom type snmpSyslogApplicationMnemonic based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SnmpSyslogApplicationMnemonic_Type.__name__ = "SnmpAdminString"
_SnmpSyslogApplicationMnemonic_Object = MibTableColumn
snmpSyslogApplicationMnemonic = _SnmpSyslogApplicationMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1, 1, 3),
    _SnmpSyslogApplicationMnemonic_Type()
)
snmpSyslogApplicationMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSyslogApplicationMnemonic.setStatus("current")


class _SnmpSyslogApplicationSeverity_Type(SyslogSeverity):
    """Custom type snmpSyslogApplicationSeverity based on SyslogSeverity"""


_SnmpSyslogApplicationSeverity_Object = MibTableColumn
snmpSyslogApplicationSeverity = _SnmpSyslogApplicationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 3, 1, 1, 4),
    _SnmpSyslogApplicationSeverity_Type()
)
snmpSyslogApplicationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslogApplicationSeverity.setStatus("current")
_SnmpSyslogDeviceConformance_ObjectIdentity = ObjectIdentity
snmpSyslogDeviceConformance = _SnmpSyslogDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4)
)
_SnmpSyslogDeviceGroups_ObjectIdentity = ObjectIdentity
snmpSyslogDeviceGroups = _SnmpSyslogDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 1)
)
_SnmpSyslogDeviceCompliances_ObjectIdentity = ObjectIdentity
snmpSyslogDeviceCompliances = _SnmpSyslogDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 2)
)

# Managed Objects groups

snmpSyslogDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 1, 1)
)
snmpSyslogDeviceGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogDeviceMessages"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogDeviceMessagesDropped"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogDeviceLastMessageTime"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogDeviceControl"))
)
if mibBuilder.loadTexts:
    snmpSyslogDeviceGroup.setStatus("current")

snmpSyslogCollectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 1, 2)
)
snmpSyslogCollectorGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorMaxEntries"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorNumEntries"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorTableNextAvailableIndex"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorDescription"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorAddressType"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorAddress"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorUdpPort"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorFacility"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorSeverity"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorMessagesIgnored"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorRowStatus"))
)
if mibBuilder.loadTexts:
    snmpSyslogCollectorGroup.setStatus("current")

snmpSyslogApplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 1, 3)
)
snmpSyslogApplicationGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogApplicationDescription"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogApplicationMnemonic"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogApplicationSeverity"))
)
if mibBuilder.loadTexts:
    snmpSyslogApplicationGroup.setStatus("current")

snmpSyslogCollectorDefaultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 1, 4)
)
snmpSyslogCollectorDefaultsGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorDefaultUdpPort"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorDefaultFacility"),
        ("DRAFT-IETF-SYSLOG-DEVICE-MIB", "snmpSyslogCollectorDefaultSeverity"))
)
if mibBuilder.loadTexts:
    snmpSyslogCollectorDefaultsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpSyslogDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    snmpSyslogDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAFT-IETF-SYSLOG-DEVICE-MIB",
    **{"SyslogUdpPort": SyslogUdpPort,
       "SyslogFacility": SyslogFacility,
       "SyslogSeverity": SyslogSeverity,
       "snmpSyslogDeviceMIB": snmpSyslogDeviceMIB,
       "snmpSyslogDevice": snmpSyslogDevice,
       "snmpSyslogDeviceMessages": snmpSyslogDeviceMessages,
       "snmpSyslogDeviceMessagesDropped": snmpSyslogDeviceMessagesDropped,
       "snmpSyslogDeviceLastMessageTime": snmpSyslogDeviceLastMessageTime,
       "snmpSyslogDeviceControl": snmpSyslogDeviceControl,
       "snmpSyslogCollector": snmpSyslogCollector,
       "snmpSyslogCollectorMaxEntries": snmpSyslogCollectorMaxEntries,
       "snmpSyslogCollectorNumEntries": snmpSyslogCollectorNumEntries,
       "snmpSyslogCollectorTableNextAvailableIndex": snmpSyslogCollectorTableNextAvailableIndex,
       "snmpSyslogCollectorTable": snmpSyslogCollectorTable,
       "snmpSyslogCollectorEntry": snmpSyslogCollectorEntry,
       "snmpSyslogCollectorIndex": snmpSyslogCollectorIndex,
       "snmpSyslogCollectorDescription": snmpSyslogCollectorDescription,
       "snmpSyslogCollectorAddressType": snmpSyslogCollectorAddressType,
       "snmpSyslogCollectorAddress": snmpSyslogCollectorAddress,
       "snmpSyslogCollectorUdpPort": snmpSyslogCollectorUdpPort,
       "snmpSyslogCollectorFacility": snmpSyslogCollectorFacility,
       "snmpSyslogCollectorSeverity": snmpSyslogCollectorSeverity,
       "snmpSyslogCollectorMessagesIgnored": snmpSyslogCollectorMessagesIgnored,
       "snmpSyslogCollectorRowStatus": snmpSyslogCollectorRowStatus,
       "snmpSyslogCollectorDefaultUdpPort": snmpSyslogCollectorDefaultUdpPort,
       "snmpSyslogCollectorDefaultFacility": snmpSyslogCollectorDefaultFacility,
       "snmpSyslogCollectorDefaultSeverity": snmpSyslogCollectorDefaultSeverity,
       "snmpSyslogApplication": snmpSyslogApplication,
       "snmpSyslogApplicationTable": snmpSyslogApplicationTable,
       "snmpSyslogApplicationEntry": snmpSyslogApplicationEntry,
       "snmpSyslogApplicationIndex": snmpSyslogApplicationIndex,
       "snmpSyslogApplicationDescription": snmpSyslogApplicationDescription,
       "snmpSyslogApplicationMnemonic": snmpSyslogApplicationMnemonic,
       "snmpSyslogApplicationSeverity": snmpSyslogApplicationSeverity,
       "snmpSyslogDeviceConformance": snmpSyslogDeviceConformance,
       "snmpSyslogDeviceGroups": snmpSyslogDeviceGroups,
       "snmpSyslogDeviceGroup": snmpSyslogDeviceGroup,
       "snmpSyslogCollectorGroup": snmpSyslogCollectorGroup,
       "snmpSyslogApplicationGroup": snmpSyslogApplicationGroup,
       "snmpSyslogCollectorDefaultsGroup": snmpSyslogCollectorDefaultsGroup,
       "snmpSyslogDeviceCompliances": snmpSyslogDeviceCompliances,
       "snmpSyslogDeviceCompliance": snmpSyslogDeviceCompliance}
)
