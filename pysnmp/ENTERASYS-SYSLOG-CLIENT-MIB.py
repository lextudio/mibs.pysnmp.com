# SNMP MIB module (ENTERASYS-SYSLOG-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SYSLOG-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:37 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

etsysSyslogClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14)
)
etsysSyslogClientMIB.setRevisions(
        ("2011-03-08 20:15",
         "2009-07-17 14:38",
         "2009-02-17 20:53",
         "2009-01-16 18:59",
         "2003-11-06 15:15",
         "2003-07-31 14:19",
         "2001-12-03 19:55",
         "2001-08-08 00:00")
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
              23)
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
          ("local7", 23))
    )



class SyslogSeverity(Integer32, TextualConvention):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysSyslogClient_ObjectIdentity = ObjectIdentity
etsysSyslogClient = _EtsysSyslogClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1)
)
_EtsysSyslogClientMessages_Type = Counter32
_EtsysSyslogClientMessages_Object = MibScalar
etsysSyslogClientMessages = _EtsysSyslogClientMessages_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 1),
    _EtsysSyslogClientMessages_Type()
)
etsysSyslogClientMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogClientMessages.setStatus("current")
_EtsysSyslogClientMessagesDropped_Type = Counter32
_EtsysSyslogClientMessagesDropped_Object = MibScalar
etsysSyslogClientMessagesDropped = _EtsysSyslogClientMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 2),
    _EtsysSyslogClientMessagesDropped_Type()
)
etsysSyslogClientMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogClientMessagesDropped.setStatus("current")
_EtsysSyslogClientLastMessageTime_Type = TimeStamp
_EtsysSyslogClientLastMessageTime_Object = MibScalar
etsysSyslogClientLastMessageTime = _EtsysSyslogClientLastMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 3),
    _EtsysSyslogClientLastMessageTime_Type()
)
etsysSyslogClientLastMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogClientLastMessageTime.setStatus("current")


class _EtsysSyslogClientControl_Type(Bits):
    """Custom type etsysSyslogClientControl based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("etsysSyslogClientControlConsoleLogging", 0),
          ("etsysSyslogClientControlPersistentLogging", 1),
          ("etsysSyslogClientControlSecurePersistentLogging", 2))
    )

_EtsysSyslogClientControl_Type.__name__ = "Bits"
_EtsysSyslogClientControl_Object = MibScalar
etsysSyslogClientControl = _EtsysSyslogClientControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 4),
    _EtsysSyslogClientControl_Type()
)
etsysSyslogClientControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogClientControl.setStatus("current")
_EtsysSyslogClientSecureMessagesDropped_Type = Counter32
_EtsysSyslogClientSecureMessagesDropped_Object = MibScalar
etsysSyslogClientSecureMessagesDropped = _EtsysSyslogClientSecureMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 5),
    _EtsysSyslogClientSecureMessagesDropped_Type()
)
etsysSyslogClientSecureMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogClientSecureMessagesDropped.setStatus("current")
_EtsysSyslogServer_ObjectIdentity = ObjectIdentity
etsysSyslogServer = _EtsysSyslogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2)
)


class _EtsysSyslogServerMaxEntries_Type(Unsigned32):
    """Custom type etsysSyslogServerMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EtsysSyslogServerMaxEntries_Type.__name__ = "Unsigned32"
_EtsysSyslogServerMaxEntries_Object = MibScalar
etsysSyslogServerMaxEntries = _EtsysSyslogServerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 1),
    _EtsysSyslogServerMaxEntries_Type()
)
etsysSyslogServerMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogServerMaxEntries.setStatus("current")
_EtsysSyslogServerNumEntries_Type = Gauge32
_EtsysSyslogServerNumEntries_Object = MibScalar
etsysSyslogServerNumEntries = _EtsysSyslogServerNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 2),
    _EtsysSyslogServerNumEntries_Type()
)
etsysSyslogServerNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogServerNumEntries.setStatus("current")


class _EtsysSyslogServerTableNextAvailableIndex_Type(Unsigned32):
    """Custom type etsysSyslogServerTableNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_EtsysSyslogServerTableNextAvailableIndex_Type.__name__ = "Unsigned32"
_EtsysSyslogServerTableNextAvailableIndex_Object = MibScalar
etsysSyslogServerTableNextAvailableIndex = _EtsysSyslogServerTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 3),
    _EtsysSyslogServerTableNextAvailableIndex_Type()
)
etsysSyslogServerTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogServerTableNextAvailableIndex.setStatus("current")
_EtsysSyslogServerTable_Object = MibTable
etsysSyslogServerTable = _EtsysSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4)
)
if mibBuilder.loadTexts:
    etsysSyslogServerTable.setStatus("current")
_EtsysSyslogServerEntry_Object = MibTableRow
etsysSyslogServerEntry = _EtsysSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1)
)
etsysSyslogServerEntry.setIndexNames(
    (0, "ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    etsysSyslogServerEntry.setStatus("current")


class _EtsysSyslogServerIndex_Type(Unsigned32):
    """Custom type etsysSyslogServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EtsysSyslogServerIndex_Type.__name__ = "Unsigned32"
_EtsysSyslogServerIndex_Object = MibTableColumn
etsysSyslogServerIndex = _EtsysSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 1),
    _EtsysSyslogServerIndex_Type()
)
etsysSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSyslogServerIndex.setStatus("current")


class _EtsysSyslogServerDescription_Type(SnmpAdminString):
    """Custom type etsysSyslogServerDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysSyslogServerDescription_Type.__name__ = "SnmpAdminString"
_EtsysSyslogServerDescription_Object = MibTableColumn
etsysSyslogServerDescription = _EtsysSyslogServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 2),
    _EtsysSyslogServerDescription_Type()
)
etsysSyslogServerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerDescription.setStatus("current")
_EtsysSyslogServerAddressType_Type = InetAddressType
_EtsysSyslogServerAddressType_Object = MibTableColumn
etsysSyslogServerAddressType = _EtsysSyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 3),
    _EtsysSyslogServerAddressType_Type()
)
etsysSyslogServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerAddressType.setStatus("current")
_EtsysSyslogServerAddress_Type = InetAddress
_EtsysSyslogServerAddress_Object = MibTableColumn
etsysSyslogServerAddress = _EtsysSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 4),
    _EtsysSyslogServerAddress_Type()
)
etsysSyslogServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerAddress.setStatus("current")
_EtsysSyslogServerUdpPort_Type = SyslogUdpPort
_EtsysSyslogServerUdpPort_Object = MibTableColumn
etsysSyslogServerUdpPort = _EtsysSyslogServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 5),
    _EtsysSyslogServerUdpPort_Type()
)
etsysSyslogServerUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerUdpPort.setStatus("current")
_EtsysSyslogServerFacility_Type = SyslogFacility
_EtsysSyslogServerFacility_Object = MibTableColumn
etsysSyslogServerFacility = _EtsysSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 6),
    _EtsysSyslogServerFacility_Type()
)
etsysSyslogServerFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerFacility.setStatus("current")
_EtsysSyslogServerSeverity_Type = SyslogSeverity
_EtsysSyslogServerSeverity_Object = MibTableColumn
etsysSyslogServerSeverity = _EtsysSyslogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 7),
    _EtsysSyslogServerSeverity_Type()
)
etsysSyslogServerSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerSeverity.setStatus("current")
_EtsysSyslogServerMessagesIgnored_Type = Counter32
_EtsysSyslogServerMessagesIgnored_Object = MibTableColumn
etsysSyslogServerMessagesIgnored = _EtsysSyslogServerMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 8),
    _EtsysSyslogServerMessagesIgnored_Type()
)
etsysSyslogServerMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogServerMessagesIgnored.setStatus("current")
_EtsysSyslogServerRowStatus_Type = RowStatus
_EtsysSyslogServerRowStatus_Object = MibTableColumn
etsysSyslogServerRowStatus = _EtsysSyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 9),
    _EtsysSyslogServerRowStatus_Type()
)
etsysSyslogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSyslogServerRowStatus.setStatus("current")


class _EtsysSyslogServerDefaultUdpPort_Type(SyslogUdpPort):
    """Custom type etsysSyslogServerDefaultUdpPort based on SyslogUdpPort"""
    defaultValue = 514


_EtsysSyslogServerDefaultUdpPort_Object = MibScalar
etsysSyslogServerDefaultUdpPort = _EtsysSyslogServerDefaultUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 5),
    _EtsysSyslogServerDefaultUdpPort_Type()
)
etsysSyslogServerDefaultUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogServerDefaultUdpPort.setStatus("current")


class _EtsysSyslogServerDefaultFacility_Type(SyslogFacility):
    """Custom type etsysSyslogServerDefaultFacility based on SyslogFacility"""


_EtsysSyslogServerDefaultFacility_Object = MibScalar
etsysSyslogServerDefaultFacility = _EtsysSyslogServerDefaultFacility_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 6),
    _EtsysSyslogServerDefaultFacility_Type()
)
etsysSyslogServerDefaultFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogServerDefaultFacility.setStatus("current")


class _EtsysSyslogServerDefaultSeverity_Type(SyslogSeverity):
    """Custom type etsysSyslogServerDefaultSeverity based on SyslogSeverity"""


_EtsysSyslogServerDefaultSeverity_Object = MibScalar
etsysSyslogServerDefaultSeverity = _EtsysSyslogServerDefaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 7),
    _EtsysSyslogServerDefaultSeverity_Type()
)
etsysSyslogServerDefaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogServerDefaultSeverity.setStatus("current")
_EtsysSyslogApplication_ObjectIdentity = ObjectIdentity
etsysSyslogApplication = _EtsysSyslogApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3)
)
_EtsysSyslogApplicationTable_Object = MibTable
etsysSyslogApplicationTable = _EtsysSyslogApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    etsysSyslogApplicationTable.setStatus("current")
_EtsysSyslogApplicationEntry_Object = MibTableRow
etsysSyslogApplicationEntry = _EtsysSyslogApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1)
)
etsysSyslogApplicationEntry.setIndexNames(
    (0, "ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationIndex"),
)
if mibBuilder.loadTexts:
    etsysSyslogApplicationEntry.setStatus("current")
_EtsysSyslogApplicationIndex_Type = Unsigned32
_EtsysSyslogApplicationIndex_Object = MibTableColumn
etsysSyslogApplicationIndex = _EtsysSyslogApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 1),
    _EtsysSyslogApplicationIndex_Type()
)
etsysSyslogApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSyslogApplicationIndex.setStatus("current")


class _EtsysSyslogApplicationDescription_Type(SnmpAdminString):
    """Custom type etsysSyslogApplicationDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysSyslogApplicationDescription_Type.__name__ = "SnmpAdminString"
_EtsysSyslogApplicationDescription_Object = MibTableColumn
etsysSyslogApplicationDescription = _EtsysSyslogApplicationDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 2),
    _EtsysSyslogApplicationDescription_Type()
)
etsysSyslogApplicationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogApplicationDescription.setStatus("current")


class _EtsysSyslogApplicationMnemonic_Type(SnmpAdminString):
    """Custom type etsysSyslogApplicationMnemonic based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EtsysSyslogApplicationMnemonic_Type.__name__ = "SnmpAdminString"
_EtsysSyslogApplicationMnemonic_Object = MibTableColumn
etsysSyslogApplicationMnemonic = _EtsysSyslogApplicationMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 3),
    _EtsysSyslogApplicationMnemonic_Type()
)
etsysSyslogApplicationMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSyslogApplicationMnemonic.setStatus("current")


class _EtsysSyslogApplicationSeverity_Type(SyslogSeverity):
    """Custom type etsysSyslogApplicationSeverity based on SyslogSeverity"""


_EtsysSyslogApplicationSeverity_Object = MibTableColumn
etsysSyslogApplicationSeverity = _EtsysSyslogApplicationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 4),
    _EtsysSyslogApplicationSeverity_Type()
)
etsysSyslogApplicationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogApplicationSeverity.setStatus("current")


class _EtsysSyslogApplicationAllowedServers_Type(Bits):
    """Custom type etsysSyslogApplicationAllowedServers based on Bits"""
    defaultBinValue = "1111111111"

    namedValues = NamedValues(
        *(("etsysSyslogServerConsole", 8),
          ("etsysSyslogServerFile", 9),
          ("etsysSyslogServerIndex1", 0),
          ("etsysSyslogServerIndex2", 1),
          ("etsysSyslogServerIndex3", 2),
          ("etsysSyslogServerIndex4", 3),
          ("etsysSyslogServerIndex5", 4),
          ("etsysSyslogServerIndex6", 5),
          ("etsysSyslogServerIndex7", 6),
          ("etsysSyslogServerIndex8", 7),
          ("etsysSyslogServerSecureFile", 10))
    )

_EtsysSyslogApplicationAllowedServers_Type.__name__ = "Bits"
_EtsysSyslogApplicationAllowedServers_Object = MibTableColumn
etsysSyslogApplicationAllowedServers = _EtsysSyslogApplicationAllowedServers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 5),
    _EtsysSyslogApplicationAllowedServers_Type()
)
etsysSyslogApplicationAllowedServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSyslogApplicationAllowedServers.setStatus("current")
_EtsysSyslogClientConformance_ObjectIdentity = ObjectIdentity
etsysSyslogClientConformance = _EtsysSyslogClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4)
)
_EtsysSyslogClientGroups_ObjectIdentity = ObjectIdentity
etsysSyslogClientGroups = _EtsysSyslogClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1)
)
_EtsysSyslogClientCompliances_ObjectIdentity = ObjectIdentity
etsysSyslogClientCompliances = _EtsysSyslogClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2)
)
_EtsysSyslogNotification_ObjectIdentity = ObjectIdentity
etsysSyslogNotification = _EtsysSyslogNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5)
)

# Managed Objects groups

etsysSyslogClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 1)
)
etsysSyslogClientGroup.setObjects(
      *(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientMessages"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientMessagesDropped"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientLastMessageTime"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientControl"))
)
if mibBuilder.loadTexts:
    etsysSyslogClientGroup.setStatus("current")

etsysSyslogServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 2)
)
etsysSyslogServerGroup.setObjects(
      *(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerMaxEntries"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerNumEntries"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerTableNextAvailableIndex"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDescription"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerAddressType"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerAddress"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerUdpPort"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerFacility"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerSeverity"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerMessagesIgnored"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerRowStatus"))
)
if mibBuilder.loadTexts:
    etsysSyslogServerGroup.setStatus("current")

etsysSyslogApplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 3)
)
etsysSyslogApplicationGroup.setObjects(
      *(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationDescription"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationMnemonic"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationSeverity"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationAllowedServers"))
)
if mibBuilder.loadTexts:
    etsysSyslogApplicationGroup.setStatus("current")

etsysSyslogServerDefaultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 4)
)
etsysSyslogServerDefaultsGroup.setObjects(
      *(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultUdpPort"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultFacility"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultSeverity"))
)
if mibBuilder.loadTexts:
    etsysSyslogServerDefaultsGroup.setStatus("current")

etsysSyslogSecureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 6)
)
etsysSyslogSecureGroup.setObjects(
    ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientSecureMessagesDropped")
)
if mibBuilder.loadTexts:
    etsysSyslogSecureGroup.setStatus("current")


# Notification objects

etsysSyslogSecureLogArchiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5, 1)
)
if mibBuilder.loadTexts:
    etsysSyslogSecureLogArchiveNotification.setStatus(
        "current"
    )

etsysSyslogSecureLogDroppedMsgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5, 2)
)
etsysSyslogSecureLogDroppedMsgNotification.setObjects(
    ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientSecureMessagesDropped")
)
if mibBuilder.loadTexts:
    etsysSyslogSecureLogDroppedMsgNotification.setStatus(
        "current"
    )


# Notifications groups

etsysSyslogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 5)
)
etsysSyslogNotificationGroup.setObjects(
      *(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogSecureLogArchiveNotification"),
        ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogSecureLogDroppedMsgNotification"))
)
if mibBuilder.loadTexts:
    etsysSyslogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysSyslogClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSyslogClientCompliance.setStatus(
        "current"
    )

etsysSyslogNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 2)
)
if mibBuilder.loadTexts:
    etsysSyslogNotificationCompliance.setStatus(
        "current"
    )

etsysSyslogSecureCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 3)
)
if mibBuilder.loadTexts:
    etsysSyslogSecureCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SYSLOG-CLIENT-MIB",
    **{"SyslogUdpPort": SyslogUdpPort,
       "SyslogFacility": SyslogFacility,
       "SyslogSeverity": SyslogSeverity,
       "etsysSyslogClientMIB": etsysSyslogClientMIB,
       "etsysSyslogClient": etsysSyslogClient,
       "etsysSyslogClientMessages": etsysSyslogClientMessages,
       "etsysSyslogClientMessagesDropped": etsysSyslogClientMessagesDropped,
       "etsysSyslogClientLastMessageTime": etsysSyslogClientLastMessageTime,
       "etsysSyslogClientControl": etsysSyslogClientControl,
       "etsysSyslogClientSecureMessagesDropped": etsysSyslogClientSecureMessagesDropped,
       "etsysSyslogServer": etsysSyslogServer,
       "etsysSyslogServerMaxEntries": etsysSyslogServerMaxEntries,
       "etsysSyslogServerNumEntries": etsysSyslogServerNumEntries,
       "etsysSyslogServerTableNextAvailableIndex": etsysSyslogServerTableNextAvailableIndex,
       "etsysSyslogServerTable": etsysSyslogServerTable,
       "etsysSyslogServerEntry": etsysSyslogServerEntry,
       "etsysSyslogServerIndex": etsysSyslogServerIndex,
       "etsysSyslogServerDescription": etsysSyslogServerDescription,
       "etsysSyslogServerAddressType": etsysSyslogServerAddressType,
       "etsysSyslogServerAddress": etsysSyslogServerAddress,
       "etsysSyslogServerUdpPort": etsysSyslogServerUdpPort,
       "etsysSyslogServerFacility": etsysSyslogServerFacility,
       "etsysSyslogServerSeverity": etsysSyslogServerSeverity,
       "etsysSyslogServerMessagesIgnored": etsysSyslogServerMessagesIgnored,
       "etsysSyslogServerRowStatus": etsysSyslogServerRowStatus,
       "etsysSyslogServerDefaultUdpPort": etsysSyslogServerDefaultUdpPort,
       "etsysSyslogServerDefaultFacility": etsysSyslogServerDefaultFacility,
       "etsysSyslogServerDefaultSeverity": etsysSyslogServerDefaultSeverity,
       "etsysSyslogApplication": etsysSyslogApplication,
       "etsysSyslogApplicationTable": etsysSyslogApplicationTable,
       "etsysSyslogApplicationEntry": etsysSyslogApplicationEntry,
       "etsysSyslogApplicationIndex": etsysSyslogApplicationIndex,
       "etsysSyslogApplicationDescription": etsysSyslogApplicationDescription,
       "etsysSyslogApplicationMnemonic": etsysSyslogApplicationMnemonic,
       "etsysSyslogApplicationSeverity": etsysSyslogApplicationSeverity,
       "etsysSyslogApplicationAllowedServers": etsysSyslogApplicationAllowedServers,
       "etsysSyslogClientConformance": etsysSyslogClientConformance,
       "etsysSyslogClientGroups": etsysSyslogClientGroups,
       "etsysSyslogClientGroup": etsysSyslogClientGroup,
       "etsysSyslogServerGroup": etsysSyslogServerGroup,
       "etsysSyslogApplicationGroup": etsysSyslogApplicationGroup,
       "etsysSyslogServerDefaultsGroup": etsysSyslogServerDefaultsGroup,
       "etsysSyslogNotificationGroup": etsysSyslogNotificationGroup,
       "etsysSyslogSecureGroup": etsysSyslogSecureGroup,
       "etsysSyslogClientCompliances": etsysSyslogClientCompliances,
       "etsysSyslogClientCompliance": etsysSyslogClientCompliance,
       "etsysSyslogNotificationCompliance": etsysSyslogNotificationCompliance,
       "etsysSyslogSecureCompliance": etsysSyslogSecureCompliance,
       "etsysSyslogNotification": etsysSyslogNotification,
       "etsysSyslogSecureLogArchiveNotification": etsysSyslogSecureLogArchiveNotification,
       "etsysSyslogSecureLogDroppedMsgNotification": etsysSyslogSecureLogDroppedMsgNotification}
)
