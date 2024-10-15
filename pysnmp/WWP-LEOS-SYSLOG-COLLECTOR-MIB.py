# SNMP MIB module (WWP-LEOS-SYSLOG-COLLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-SYSLOG-COLLECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:10 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosSyslogCollectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21)
)
wwpLeosSyslogCollectorMIB.setRevisions(
        ("2012-04-05 00:00",
         "2006-04-18 10:12",
         "2003-01-21 10:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(Integer32, TextualConvention):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 4),
          ("authPriv", 10),
          ("clockd2", 15),
          ("console", 14),
          ("cron", 9),
          ("daemon", 3),
          ("ftp", 11),
          ("kernel", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("noMap", 24),
          ("ntp", 12),
          ("security", 13),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
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
              7,
              99)
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
          ("other", 99),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosSyslogCollMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBObjects = _WwpLeosSyslogCollMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1)
)
_WwpLeosSyslogSystem_ObjectIdentity = ObjectIdentity
wwpLeosSyslogSystem = _WwpLeosSyslogSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 1)
)


class _WwpLeosSyslogEnable_Type(TruthValue):
    """Custom type wwpLeosSyslogEnable based on TruthValue"""


_WwpLeosSyslogEnable_Object = MibScalar
wwpLeosSyslogEnable = _WwpLeosSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 1, 1),
    _WwpLeosSyslogEnable_Type()
)
wwpLeosSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSyslogEnable.setStatus("current")
_WwpLeosSyslogColl_ObjectIdentity = ObjectIdentity
wwpLeosSyslogColl = _WwpLeosSyslogColl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2)
)
_WwpLeosSyslogCollectorTable_Object = MibTable
wwpLeosSyslogCollectorTable = _WwpLeosSyslogCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorTable.setStatus("current")
_WwpLeosSyslogCollectorEntry_Object = MibTableRow
wwpLeosSyslogCollectorEntry = _WwpLeosSyslogCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1)
)
wwpLeosSyslogCollectorEntry.setIndexNames(
    (0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorEntry.setStatus("current")


class _WwpLeosSyslogIndex_Type(Integer32):
    """Custom type wwpLeosSyslogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosSyslogIndex_Type.__name__ = "Integer32"
_WwpLeosSyslogIndex_Object = MibTableColumn
wwpLeosSyslogIndex = _WwpLeosSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 1),
    _WwpLeosSyslogIndex_Type()
)
wwpLeosSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSyslogIndex.setStatus("current")
_WwpLeosSyslogCollectorAddr_Type = DisplayString
_WwpLeosSyslogCollectorAddr_Object = MibTableColumn
wwpLeosSyslogCollectorAddr = _WwpLeosSyslogCollectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 2),
    _WwpLeosSyslogCollectorAddr_Type()
)
wwpLeosSyslogCollectorAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorAddr.setStatus("current")
_WwpLeosSyslogCollectorResolvedAddr_Type = IpAddress
_WwpLeosSyslogCollectorResolvedAddr_Object = MibTableColumn
wwpLeosSyslogCollectorResolvedAddr = _WwpLeosSyslogCollectorResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 3),
    _WwpLeosSyslogCollectorResolvedAddr_Type()
)
wwpLeosSyslogCollectorResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorResolvedAddr.setStatus("current")


class _WwpLeosSyslogCollectorUDPPort_Type(Integer32):
    """Custom type wwpLeosSyslogCollectorUDPPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSyslogCollectorUDPPort_Type.__name__ = "Integer32"
_WwpLeosSyslogCollectorUDPPort_Object = MibTableColumn
wwpLeosSyslogCollectorUDPPort = _WwpLeosSyslogCollectorUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 4),
    _WwpLeosSyslogCollectorUDPPort_Type()
)
wwpLeosSyslogCollectorUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorUDPPort.setStatus("current")


class _WwpLeosSyslogCollectorFacility_Type(SyslogFacility):
    """Custom type wwpLeosSyslogCollectorFacility based on SyslogFacility"""


_WwpLeosSyslogCollectorFacility_Object = MibTableColumn
wwpLeosSyslogCollectorFacility = _WwpLeosSyslogCollectorFacility_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 5),
    _WwpLeosSyslogCollectorFacility_Type()
)
wwpLeosSyslogCollectorFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorFacility.setStatus("current")


class _WwpLeosSyslogCollectorMinSeverity_Type(SyslogSeverity):
    """Custom type wwpLeosSyslogCollectorMinSeverity based on SyslogSeverity"""


_WwpLeosSyslogCollectorMinSeverity_Object = MibTableColumn
wwpLeosSyslogCollectorMinSeverity = _WwpLeosSyslogCollectorMinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 6),
    _WwpLeosSyslogCollectorMinSeverity_Type()
)
wwpLeosSyslogCollectorMinSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorMinSeverity.setStatus("deprecated")


class _WwpLeosSyslogCollectorMaxSeverity_Type(SyslogSeverity):
    """Custom type wwpLeosSyslogCollectorMaxSeverity based on SyslogSeverity"""


_WwpLeosSyslogCollectorMaxSeverity_Object = MibTableColumn
wwpLeosSyslogCollectorMaxSeverity = _WwpLeosSyslogCollectorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 7),
    _WwpLeosSyslogCollectorMaxSeverity_Type()
)
wwpLeosSyslogCollectorMaxSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorMaxSeverity.setStatus("deprecated")


class _WwpLeosSyslogCollectorUserAdminState_Type(Integer32):
    """Custom type wwpLeosSyslogCollectorUserAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosSyslogCollectorUserAdminState_Type.__name__ = "Integer32"
_WwpLeosSyslogCollectorUserAdminState_Object = MibTableColumn
wwpLeosSyslogCollectorUserAdminState = _WwpLeosSyslogCollectorUserAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 8),
    _WwpLeosSyslogCollectorUserAdminState_Type()
)
wwpLeosSyslogCollectorUserAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorUserAdminState.setStatus("current")


class _WwpLeosSyslogCollectorDhcpAdminState_Type(Integer32):
    """Custom type wwpLeosSyslogCollectorDhcpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosSyslogCollectorDhcpAdminState_Type.__name__ = "Integer32"
_WwpLeosSyslogCollectorDhcpAdminState_Object = MibTableColumn
wwpLeosSyslogCollectorDhcpAdminState = _WwpLeosSyslogCollectorDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 9),
    _WwpLeosSyslogCollectorDhcpAdminState_Type()
)
wwpLeosSyslogCollectorDhcpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorDhcpAdminState.setStatus("current")


class _WwpLeosSyslogCollectorOperState_Type(Integer32):
    """Custom type wwpLeosSyslogCollectorOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosSyslogCollectorOperState_Type.__name__ = "Integer32"
_WwpLeosSyslogCollectorOperState_Object = MibTableColumn
wwpLeosSyslogCollectorOperState = _WwpLeosSyslogCollectorOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 10),
    _WwpLeosSyslogCollectorOperState_Type()
)
wwpLeosSyslogCollectorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorOperState.setStatus("current")
_WwpLeosSyslogCollectorStatus_Type = RowStatus
_WwpLeosSyslogCollectorStatus_Object = MibTableColumn
wwpLeosSyslogCollectorStatus = _WwpLeosSyslogCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 11),
    _WwpLeosSyslogCollectorStatus_Type()
)
wwpLeosSyslogCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorStatus.setStatus("current")


class _WwpLeosSyslogCollectorCustomPrefix_Type(DisplayString):
    """Custom type wwpLeosSyslogCollectorCustomPrefix based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosSyslogCollectorCustomPrefix_Type.__name__ = "DisplayString"
_WwpLeosSyslogCollectorCustomPrefix_Object = MibTableColumn
wwpLeosSyslogCollectorCustomPrefix = _WwpLeosSyslogCollectorCustomPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 12),
    _WwpLeosSyslogCollectorCustomPrefix_Type()
)
wwpLeosSyslogCollectorCustomPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorCustomPrefix.setStatus("current")
_WwpLeosSyslogCollectorResolvedInetAddrType_Type = InetAddressType
_WwpLeosSyslogCollectorResolvedInetAddrType_Object = MibTableColumn
wwpLeosSyslogCollectorResolvedInetAddrType = _WwpLeosSyslogCollectorResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 13),
    _WwpLeosSyslogCollectorResolvedInetAddrType_Type()
)
wwpLeosSyslogCollectorResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorResolvedInetAddrType.setStatus("current")
_WwpLeosSyslogCollectorResolvedInetAddress_Type = InetAddress
_WwpLeosSyslogCollectorResolvedInetAddress_Object = MibTableColumn
wwpLeosSyslogCollectorResolvedInetAddress = _WwpLeosSyslogCollectorResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 1, 1, 14),
    _WwpLeosSyslogCollectorResolvedInetAddress_Type()
)
wwpLeosSyslogCollectorResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorResolvedInetAddress.setStatus("current")
_WwpLeosSyslogCollectorSeverityTable_Object = MibTable
wwpLeosSyslogCollectorSeverityTable = _WwpLeosSyslogCollectorSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorSeverityTable.setStatus("current")
_WwpLeosSyslogCollectorSeverityEntry_Object = MibTableRow
wwpLeosSyslogCollectorSeverityEntry = _WwpLeosSyslogCollectorSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1)
)
wwpLeosSyslogCollectorSeverityEntry.setIndexNames(
    (0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogIndex"),
    (0, "WWP-LEOS-SYSLOG-COLLECTOR-MIB", "wwpLeosSyslogCollectorSeverity"),
)
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorSeverityEntry.setStatus("current")
_WwpLeosSyslogCollectorSeverity_Type = SyslogSeverity
_WwpLeosSyslogCollectorSeverity_Object = MibTableColumn
wwpLeosSyslogCollectorSeverity = _WwpLeosSyslogCollectorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1, 1),
    _WwpLeosSyslogCollectorSeverity_Type()
)
wwpLeosSyslogCollectorSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorSeverity.setStatus("current")
_WwpLeosSyslogCollectorSeverityRowStatus_Type = RowStatus
_WwpLeosSyslogCollectorSeverityRowStatus_Object = MibTableColumn
wwpLeosSyslogCollectorSeverityRowStatus = _WwpLeosSyslogCollectorSeverityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 1, 2, 2, 1, 2),
    _WwpLeosSyslogCollectorSeverityRowStatus_Type()
)
wwpLeosSyslogCollectorSeverityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSyslogCollectorSeverityRowStatus.setStatus("current")
_WwpLeosSyslogCollMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBNotificationPrefix = _WwpLeosSyslogCollMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 2)
)
_WwpLeosSyslogCollMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBNotifications = _WwpLeosSyslogCollMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 2, 0)
)
_WwpLeosSyslogCollMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBConformance = _WwpLeosSyslogCollMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3)
)
_WwpLeosSyslogCollMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBCompliances = _WwpLeosSyslogCollMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3, 1)
)
_WwpLeosSyslogCollMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosSyslogCollMIBGroups = _WwpLeosSyslogCollMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 21, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-SYSLOG-COLLECTOR-MIB",
    **{"SyslogFacility": SyslogFacility,
       "SyslogSeverity": SyslogSeverity,
       "wwpLeosSyslogCollectorMIB": wwpLeosSyslogCollectorMIB,
       "wwpLeosSyslogCollMIBObjects": wwpLeosSyslogCollMIBObjects,
       "wwpLeosSyslogSystem": wwpLeosSyslogSystem,
       "wwpLeosSyslogEnable": wwpLeosSyslogEnable,
       "wwpLeosSyslogColl": wwpLeosSyslogColl,
       "wwpLeosSyslogCollectorTable": wwpLeosSyslogCollectorTable,
       "wwpLeosSyslogCollectorEntry": wwpLeosSyslogCollectorEntry,
       "wwpLeosSyslogIndex": wwpLeosSyslogIndex,
       "wwpLeosSyslogCollectorAddr": wwpLeosSyslogCollectorAddr,
       "wwpLeosSyslogCollectorResolvedAddr": wwpLeosSyslogCollectorResolvedAddr,
       "wwpLeosSyslogCollectorUDPPort": wwpLeosSyslogCollectorUDPPort,
       "wwpLeosSyslogCollectorFacility": wwpLeosSyslogCollectorFacility,
       "wwpLeosSyslogCollectorMinSeverity": wwpLeosSyslogCollectorMinSeverity,
       "wwpLeosSyslogCollectorMaxSeverity": wwpLeosSyslogCollectorMaxSeverity,
       "wwpLeosSyslogCollectorUserAdminState": wwpLeosSyslogCollectorUserAdminState,
       "wwpLeosSyslogCollectorDhcpAdminState": wwpLeosSyslogCollectorDhcpAdminState,
       "wwpLeosSyslogCollectorOperState": wwpLeosSyslogCollectorOperState,
       "wwpLeosSyslogCollectorStatus": wwpLeosSyslogCollectorStatus,
       "wwpLeosSyslogCollectorCustomPrefix": wwpLeosSyslogCollectorCustomPrefix,
       "wwpLeosSyslogCollectorResolvedInetAddrType": wwpLeosSyslogCollectorResolvedInetAddrType,
       "wwpLeosSyslogCollectorResolvedInetAddress": wwpLeosSyslogCollectorResolvedInetAddress,
       "wwpLeosSyslogCollectorSeverityTable": wwpLeosSyslogCollectorSeverityTable,
       "wwpLeosSyslogCollectorSeverityEntry": wwpLeosSyslogCollectorSeverityEntry,
       "wwpLeosSyslogCollectorSeverity": wwpLeosSyslogCollectorSeverity,
       "wwpLeosSyslogCollectorSeverityRowStatus": wwpLeosSyslogCollectorSeverityRowStatus,
       "wwpLeosSyslogCollMIBNotificationPrefix": wwpLeosSyslogCollMIBNotificationPrefix,
       "wwpLeosSyslogCollMIBNotifications": wwpLeosSyslogCollMIBNotifications,
       "wwpLeosSyslogCollMIBConformance": wwpLeosSyslogCollMIBConformance,
       "wwpLeosSyslogCollMIBCompliances": wwpLeosSyslogCollMIBCompliances,
       "wwpLeosSyslogCollMIBGroups": wwpLeosSyslogCollMIBGroups}
)
