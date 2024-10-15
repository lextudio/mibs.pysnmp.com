# SNMP MIB module (CISCO-LWAPP-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:09 2024
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

(CLSecKeyFormat,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLSecKeyFormat")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 StorageType,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598)
)
ciscoLwappAAAMIB.setRevisions(
        ("2010-07-25 00:00",
         "2006-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappAAAMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBNotifs = _CiscoLwappAAAMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0)
)
_CiscoLwappAAAMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBObjects = _CiscoLwappAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1)
)
_ClaConfigObjects_ObjectIdentity = ObjectIdentity
claConfigObjects = _ClaConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1)
)
_ClaPriorityTable_Object = MibTable
claPriorityTable = _ClaPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1)
)
if mibBuilder.loadTexts:
    claPriorityTable.setStatus("current")
_ClaPriorityEntry_Object = MibTableRow
claPriorityEntry = _ClaPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1)
)
claPriorityEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claPriorityAuth"),
)
if mibBuilder.loadTexts:
    claPriorityEntry.setStatus("current")


class _ClaPriorityAuth_Type(Integer32):
    """Custom type claPriorityAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_ClaPriorityAuth_Type.__name__ = "Integer32"
_ClaPriorityAuth_Object = MibTableColumn
claPriorityAuth = _ClaPriorityAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 1),
    _ClaPriorityAuth_Type()
)
claPriorityAuth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claPriorityAuth.setStatus("current")


class _ClaPriorityOrder_Type(Unsigned32):
    """Custom type claPriorityOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ClaPriorityOrder_Type.__name__ = "Unsigned32"
_ClaPriorityOrder_Object = MibTableColumn
claPriorityOrder = _ClaPriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 2),
    _ClaPriorityOrder_Type()
)
claPriorityOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claPriorityOrder.setStatus("current")
_ClaTacacsServerTable_Object = MibTable
claTacacsServerTable = _ClaTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2)
)
if mibBuilder.loadTexts:
    claTacacsServerTable.setStatus("current")
_ClaTacacsServerEntry_Object = MibTableRow
claTacacsServerEntry = _ClaTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1)
)
claTacacsServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerType"),
    (0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerPriority"),
)
if mibBuilder.loadTexts:
    claTacacsServerEntry.setStatus("current")


class _ClaTacacsServerType_Type(Integer32):
    """Custom type claTacacsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 3),
          ("authentication", 1),
          ("authorization", 2))
    )


_ClaTacacsServerType_Type.__name__ = "Integer32"
_ClaTacacsServerType_Object = MibTableColumn
claTacacsServerType = _ClaTacacsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 1),
    _ClaTacacsServerType_Type()
)
claTacacsServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claTacacsServerType.setStatus("current")
_ClaTacacsServerPriority_Type = Unsigned32
_ClaTacacsServerPriority_Object = MibTableColumn
claTacacsServerPriority = _ClaTacacsServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 2),
    _ClaTacacsServerPriority_Type()
)
claTacacsServerPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claTacacsServerPriority.setStatus("current")
_ClaTacacsServerAddressType_Type = InetAddressType
_ClaTacacsServerAddressType_Object = MibTableColumn
claTacacsServerAddressType = _ClaTacacsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 3),
    _ClaTacacsServerAddressType_Type()
)
claTacacsServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerAddressType.setStatus("current")
_ClaTacacsServerAddress_Type = InetAddress
_ClaTacacsServerAddress_Object = MibTableColumn
claTacacsServerAddress = _ClaTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 4),
    _ClaTacacsServerAddress_Type()
)
claTacacsServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerAddress.setStatus("current")
_ClaTacacsServerPortNum_Type = InetPortNumber
_ClaTacacsServerPortNum_Object = MibTableColumn
claTacacsServerPortNum = _ClaTacacsServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 5),
    _ClaTacacsServerPortNum_Type()
)
claTacacsServerPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerPortNum.setStatus("current")


class _ClaTacacsServerEnabled_Type(TruthValue):
    """Custom type claTacacsServerEnabled based on TruthValue"""


_ClaTacacsServerEnabled_Object = MibTableColumn
claTacacsServerEnabled = _ClaTacacsServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 6),
    _ClaTacacsServerEnabled_Type()
)
claTacacsServerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerEnabled.setStatus("current")
_ClaTacacsServerSecretType_Type = CLSecKeyFormat
_ClaTacacsServerSecretType_Object = MibTableColumn
claTacacsServerSecretType = _ClaTacacsServerSecretType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 7),
    _ClaTacacsServerSecretType_Type()
)
claTacacsServerSecretType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerSecretType.setStatus("current")
_ClaTacacsServerSecret_Type = DisplayString
_ClaTacacsServerSecret_Object = MibTableColumn
claTacacsServerSecret = _ClaTacacsServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 8),
    _ClaTacacsServerSecret_Type()
)
claTacacsServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerSecret.setStatus("current")


class _ClaTacacsServerTimeout_Type(Unsigned32):
    """Custom type claTacacsServerTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ClaTacacsServerTimeout_Type.__name__ = "Unsigned32"
_ClaTacacsServerTimeout_Object = MibTableColumn
claTacacsServerTimeout = _ClaTacacsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 9),
    _ClaTacacsServerTimeout_Type()
)
claTacacsServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    claTacacsServerTimeout.setUnits("seconds")


class _ClaTacacsServerStorageType_Type(StorageType):
    """Custom type claTacacsServerStorageType based on StorageType"""


_ClaTacacsServerStorageType_Object = MibTableColumn
claTacacsServerStorageType = _ClaTacacsServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 10),
    _ClaTacacsServerStorageType_Type()
)
claTacacsServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerStorageType.setStatus("current")
_ClaTacacsServerRowStatus_Type = RowStatus
_ClaTacacsServerRowStatus_Object = MibTableColumn
claTacacsServerRowStatus = _ClaTacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 11),
    _ClaTacacsServerRowStatus_Type()
)
claTacacsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerRowStatus.setStatus("current")
_ClaWlanTable_Object = MibTable
claWlanTable = _ClaWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3)
)
if mibBuilder.loadTexts:
    claWlanTable.setStatus("current")
_ClaWlanEntry_Object = MibTableRow
claWlanEntry = _ClaWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1)
)
claWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    claWlanEntry.setStatus("current")


class _ClaWlanAcctServerEnabled_Type(TruthValue):
    """Custom type claWlanAcctServerEnabled based on TruthValue"""


_ClaWlanAcctServerEnabled_Object = MibTableColumn
claWlanAcctServerEnabled = _ClaWlanAcctServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 1),
    _ClaWlanAcctServerEnabled_Type()
)
claWlanAcctServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanAcctServerEnabled.setStatus("current")


class _ClaWlanAuthServerEnabled_Type(TruthValue):
    """Custom type claWlanAuthServerEnabled based on TruthValue"""


_ClaWlanAuthServerEnabled_Object = MibTableColumn
claWlanAuthServerEnabled = _ClaWlanAuthServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 2),
    _ClaWlanAuthServerEnabled_Type()
)
claWlanAuthServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanAuthServerEnabled.setStatus("current")


class _ClaRadiusServerGlobalActivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerGlobalActivatedEnabled based on TruthValue"""


_ClaRadiusServerGlobalActivatedEnabled_Object = MibScalar
claRadiusServerGlobalActivatedEnabled = _ClaRadiusServerGlobalActivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 4),
    _ClaRadiusServerGlobalActivatedEnabled_Type()
)
claRadiusServerGlobalActivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerGlobalActivatedEnabled.setStatus("current")


class _ClaRadiusServerGlobalDeactivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerGlobalDeactivatedEnabled based on TruthValue"""


_ClaRadiusServerGlobalDeactivatedEnabled_Object = MibScalar
claRadiusServerGlobalDeactivatedEnabled = _ClaRadiusServerGlobalDeactivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 5),
    _ClaRadiusServerGlobalDeactivatedEnabled_Type()
)
claRadiusServerGlobalDeactivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerGlobalDeactivatedEnabled.setStatus("current")


class _ClaRadiusServerWlanActivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerWlanActivatedEnabled based on TruthValue"""


_ClaRadiusServerWlanActivatedEnabled_Object = MibScalar
claRadiusServerWlanActivatedEnabled = _ClaRadiusServerWlanActivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 6),
    _ClaRadiusServerWlanActivatedEnabled_Type()
)
claRadiusServerWlanActivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerWlanActivatedEnabled.setStatus("current")


class _ClaRadiusServerWlanDeactivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerWlanDeactivatedEnabled based on TruthValue"""


_ClaRadiusServerWlanDeactivatedEnabled_Object = MibScalar
claRadiusServerWlanDeactivatedEnabled = _ClaRadiusServerWlanDeactivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 7),
    _ClaRadiusServerWlanDeactivatedEnabled_Type()
)
claRadiusServerWlanDeactivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerWlanDeactivatedEnabled.setStatus("current")


class _ClaRadiusReqTimedOutEnabled_Type(TruthValue):
    """Custom type claRadiusReqTimedOutEnabled based on TruthValue"""


_ClaRadiusReqTimedOutEnabled_Object = MibScalar
claRadiusReqTimedOutEnabled = _ClaRadiusReqTimedOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 8),
    _ClaRadiusReqTimedOutEnabled_Type()
)
claRadiusReqTimedOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusReqTimedOutEnabled.setStatus("current")


class _ClaSaveUserData_Type(TruthValue):
    """Custom type claSaveUserData based on TruthValue"""


_ClaSaveUserData_Object = MibScalar
claSaveUserData = _ClaSaveUserData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 9),
    _ClaSaveUserData_Type()
)
claSaveUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claSaveUserData.setStatus("current")


class _ClaWebRadiusAuthentication_Type(Integer32):
    """Custom type claWebRadiusAuthentication based on Integer32"""
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
        *(("chap", 2),
          ("md5-chap", 3),
          ("pap", 1))
    )


_ClaWebRadiusAuthentication_Type.__name__ = "Integer32"
_ClaWebRadiusAuthentication_Object = MibScalar
claWebRadiusAuthentication = _ClaWebRadiusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 10),
    _ClaWebRadiusAuthentication_Type()
)
claWebRadiusAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWebRadiusAuthentication.setStatus("current")


class _ClaRadiusFallbackMode_Type(Integer32):
    """Custom type claRadiusFallbackMode based on Integer32"""
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
        *(("active", 3),
          ("off", 1),
          ("passive", 2))
    )


_ClaRadiusFallbackMode_Type.__name__ = "Integer32"
_ClaRadiusFallbackMode_Object = MibScalar
claRadiusFallbackMode = _ClaRadiusFallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 11),
    _ClaRadiusFallbackMode_Type()
)
claRadiusFallbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackMode.setStatus("current")
_ClaRadiusFallbackUsername_Type = SnmpAdminString
_ClaRadiusFallbackUsername_Object = MibScalar
claRadiusFallbackUsername = _ClaRadiusFallbackUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 12),
    _ClaRadiusFallbackUsername_Type()
)
claRadiusFallbackUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackUsername.setStatus("current")


class _ClaRadiusFallbackInterval_Type(TimeInterval):
    """Custom type claRadiusFallbackInterval based on TimeInterval"""
    defaultValue = 300

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_ClaRadiusFallbackInterval_Type.__name__ = "TimeInterval"
_ClaRadiusFallbackInterval_Object = MibScalar
claRadiusFallbackInterval = _ClaRadiusFallbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 13),
    _ClaRadiusFallbackInterval_Type()
)
claRadiusFallbackInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackInterval.setStatus("current")
if mibBuilder.loadTexts:
    claRadiusFallbackInterval.setUnits("seconds")


class _ClaRadiusAuthMacDelimiter_Type(Integer32):
    """Custom type claRadiusAuthMacDelimiter based on Integer32"""
    defaultValue = 3

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
        *(("colon", 2),
          ("hyphen", 3),
          ("noDelimiter", 1),
          ("singleHyphen", 4))
    )


_ClaRadiusAuthMacDelimiter_Type.__name__ = "Integer32"
_ClaRadiusAuthMacDelimiter_Object = MibScalar
claRadiusAuthMacDelimiter = _ClaRadiusAuthMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 14),
    _ClaRadiusAuthMacDelimiter_Type()
)
claRadiusAuthMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusAuthMacDelimiter.setStatus("current")


class _ClaRadiusAcctMacDelimiter_Type(Integer32):
    """Custom type claRadiusAcctMacDelimiter based on Integer32"""
    defaultValue = 3

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
        *(("colon", 2),
          ("hyphen", 3),
          ("noDelimiter", 1),
          ("singleHyphen", 4))
    )


_ClaRadiusAcctMacDelimiter_Type.__name__ = "Integer32"
_ClaRadiusAcctMacDelimiter_Object = MibScalar
claRadiusAcctMacDelimiter = _ClaRadiusAcctMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 15),
    _ClaRadiusAcctMacDelimiter_Type()
)
claRadiusAcctMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusAcctMacDelimiter.setStatus("current")


class _ClaAcceptMICertificate_Type(TruthValue):
    """Custom type claAcceptMICertificate based on TruthValue"""


_ClaAcceptMICertificate_Object = MibScalar
claAcceptMICertificate = _ClaAcceptMICertificate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 16),
    _ClaAcceptMICertificate_Type()
)
claAcceptMICertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAcceptMICertificate.setStatus("current")


class _ClaAcceptLSCertificate_Type(TruthValue):
    """Custom type claAcceptLSCertificate based on TruthValue"""


_ClaAcceptLSCertificate_Object = MibScalar
claAcceptLSCertificate = _ClaAcceptLSCertificate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 17),
    _ClaAcceptLSCertificate_Type()
)
claAcceptLSCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAcceptLSCertificate.setStatus("current")


class _ClaAllowAuthorizeLscApAgainstAAA_Type(TruthValue):
    """Custom type claAllowAuthorizeLscApAgainstAAA based on TruthValue"""


_ClaAllowAuthorizeLscApAgainstAAA_Object = MibScalar
claAllowAuthorizeLscApAgainstAAA = _ClaAllowAuthorizeLscApAgainstAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 18),
    _ClaAllowAuthorizeLscApAgainstAAA_Type()
)
claAllowAuthorizeLscApAgainstAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAllowAuthorizeLscApAgainstAAA.setStatus("current")
_ClaStatusObjects_ObjectIdentity = ObjectIdentity
claStatusObjects = _ClaStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2)
)
_ClaRadiusServerTable_Object = MibTable
claRadiusServerTable = _ClaRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1)
)
if mibBuilder.loadTexts:
    claRadiusServerTable.setStatus("current")
_ClaRadiusServerEntry_Object = MibTableRow
claRadiusServerEntry = _ClaRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1)
)
claRadiusServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusReqId"),
)
if mibBuilder.loadTexts:
    claRadiusServerEntry.setStatus("current")
_ClaRadiusReqId_Type = Unsigned32
_ClaRadiusReqId_Object = MibTableColumn
claRadiusReqId = _ClaRadiusReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 1),
    _ClaRadiusReqId_Type()
)
claRadiusReqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claRadiusReqId.setStatus("current")
_ClaRadiusAddressType_Type = InetAddressType
_ClaRadiusAddressType_Object = MibTableColumn
claRadiusAddressType = _ClaRadiusAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 2),
    _ClaRadiusAddressType_Type()
)
claRadiusAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAddressType.setStatus("current")
_ClaRadiusAddress_Type = InetAddress
_ClaRadiusAddress_Object = MibTableColumn
claRadiusAddress = _ClaRadiusAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 3),
    _ClaRadiusAddress_Type()
)
claRadiusAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAddress.setStatus("current")
_ClaRadiusPortNum_Type = InetPortNumber
_ClaRadiusPortNum_Object = MibTableColumn
claRadiusPortNum = _ClaRadiusPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 4),
    _ClaRadiusPortNum_Type()
)
claRadiusPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusPortNum.setStatus("current")


class _ClaRadiusWlanIdx_Type(Unsigned32):
    """Custom type claRadiusWlanIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ClaRadiusWlanIdx_Type.__name__ = "Unsigned32"
_ClaRadiusWlanIdx_Object = MibTableColumn
claRadiusWlanIdx = _ClaRadiusWlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 5),
    _ClaRadiusWlanIdx_Type()
)
claRadiusWlanIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusWlanIdx.setStatus("current")
_ClaRadiusClientMacAddress_Type = MacAddress
_ClaRadiusClientMacAddress_Object = MibTableColumn
claRadiusClientMacAddress = _ClaRadiusClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 6),
    _ClaRadiusClientMacAddress_Type()
)
claRadiusClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusClientMacAddress.setStatus("current")
_ClaRadiusUserName_Type = DisplayString
_ClaRadiusUserName_Object = MibTableColumn
claRadiusUserName = _ClaRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 7),
    _ClaRadiusUserName_Type()
)
claRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusUserName.setStatus("current")
_ClaDBCurrentUsedEntries_Type = Gauge32
_ClaDBCurrentUsedEntries_Object = MibScalar
claDBCurrentUsedEntries = _ClaDBCurrentUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 2),
    _ClaDBCurrentUsedEntries_Type()
)
claDBCurrentUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claDBCurrentUsedEntries.setStatus("current")
_CiscoLwappAAAMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBConform = _CiscoLwappAAAMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2)
)
_CiscoLwappAAAMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBCompliances = _CiscoLwappAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1)
)
_CiscoLwappAAAMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBGroups = _CiscoLwappAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2)
)

# Managed Objects groups

ciscoLwappAAAMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 1)
)
ciscoLwappAAAMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claPriorityOrder"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecretType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecret"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerStorageType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerRowStatus"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalActivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalDeactivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanActivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanDeactivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusReqTimedOutEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBConfigGroup.setStatus("current")

ciscoLwappAAAMIBSaveUserConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 2)
)
ciscoLwappAAAMIBSaveUserConfigGroup.setObjects(
    ("CISCO-LWAPP-AAA-MIB", "claSaveUserData")
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBSaveUserConfigGroup.setStatus("current")

ciscoLwappAAAMIBStatusObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 4)
)
ciscoLwappAAAMIBStatusObjsGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBStatusObjsGroup.setStatus("current")

ciscoLwappAAAMIBDBEntriesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 5)
)
ciscoLwappAAAMIBDBEntriesGroup.setObjects(
    ("CISCO-LWAPP-AAA-MIB", "claDBCurrentUsedEntries")
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBDBEntriesGroup.setStatus("current")

ciscoLwappAAAMIBRadiusConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 6)
)
ciscoLwappAAAMIBRadiusConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claWebRadiusAuthentication"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackMode"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackUsername"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackInterval"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthMacDelimiter"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAcctMacDelimiter"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBRadiusConfigGroup.setStatus("current")

ciscoLwappAAAMIBAPPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 7)
)
ciscoLwappAAAMIBAPPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claAcceptMICertificate"),
        ("CISCO-LWAPP-AAA-MIB", "claAcceptLSCertificate"),
        ("CISCO-LWAPP-AAA-MIB", "claAllowAuthorizeLscApAgainstAAA"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBAPPolicyConfigGroup.setStatus("current")

ciscoLwappAAAMIBWlanAuthAccServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 8)
)
ciscoLwappAAAMIBWlanAuthAccServerConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claWlanAuthServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanAcctServerEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBWlanAuthAccServerConfigGroup.setStatus("current")


# Notification objects

ciscoLwappAAARadiusServerGlobalActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 1)
)
ciscoLwappAAARadiusServerGlobalActivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerGlobalActivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerGlobalDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 2)
)
ciscoLwappAAARadiusServerGlobalDeactivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerGlobalDeactivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerWlanActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 3)
)
ciscoLwappAAARadiusServerWlanActivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerWlanActivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerWlanDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 4)
)
ciscoLwappAAARadiusServerWlanDeactivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerWlanDeactivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusReqTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 5)
)
ciscoLwappAAARadiusReqTimedOut.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusReqTimedOut.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappAAAMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 3)
)
ciscoLwappAAAMIBNotifsGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalActivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalDeactivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanActivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanDeactivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusReqTimedOut"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappAAAMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-AAA-MIB",
    **{"ciscoLwappAAAMIB": ciscoLwappAAAMIB,
       "ciscoLwappAAAMIBNotifs": ciscoLwappAAAMIBNotifs,
       "ciscoLwappAAARadiusServerGlobalActivated": ciscoLwappAAARadiusServerGlobalActivated,
       "ciscoLwappAAARadiusServerGlobalDeactivated": ciscoLwappAAARadiusServerGlobalDeactivated,
       "ciscoLwappAAARadiusServerWlanActivated": ciscoLwappAAARadiusServerWlanActivated,
       "ciscoLwappAAARadiusServerWlanDeactivated": ciscoLwappAAARadiusServerWlanDeactivated,
       "ciscoLwappAAARadiusReqTimedOut": ciscoLwappAAARadiusReqTimedOut,
       "ciscoLwappAAAMIBObjects": ciscoLwappAAAMIBObjects,
       "claConfigObjects": claConfigObjects,
       "claPriorityTable": claPriorityTable,
       "claPriorityEntry": claPriorityEntry,
       "claPriorityAuth": claPriorityAuth,
       "claPriorityOrder": claPriorityOrder,
       "claTacacsServerTable": claTacacsServerTable,
       "claTacacsServerEntry": claTacacsServerEntry,
       "claTacacsServerType": claTacacsServerType,
       "claTacacsServerPriority": claTacacsServerPriority,
       "claTacacsServerAddressType": claTacacsServerAddressType,
       "claTacacsServerAddress": claTacacsServerAddress,
       "claTacacsServerPortNum": claTacacsServerPortNum,
       "claTacacsServerEnabled": claTacacsServerEnabled,
       "claTacacsServerSecretType": claTacacsServerSecretType,
       "claTacacsServerSecret": claTacacsServerSecret,
       "claTacacsServerTimeout": claTacacsServerTimeout,
       "claTacacsServerStorageType": claTacacsServerStorageType,
       "claTacacsServerRowStatus": claTacacsServerRowStatus,
       "claWlanTable": claWlanTable,
       "claWlanEntry": claWlanEntry,
       "claWlanAcctServerEnabled": claWlanAcctServerEnabled,
       "claWlanAuthServerEnabled": claWlanAuthServerEnabled,
       "claRadiusServerGlobalActivatedEnabled": claRadiusServerGlobalActivatedEnabled,
       "claRadiusServerGlobalDeactivatedEnabled": claRadiusServerGlobalDeactivatedEnabled,
       "claRadiusServerWlanActivatedEnabled": claRadiusServerWlanActivatedEnabled,
       "claRadiusServerWlanDeactivatedEnabled": claRadiusServerWlanDeactivatedEnabled,
       "claRadiusReqTimedOutEnabled": claRadiusReqTimedOutEnabled,
       "claSaveUserData": claSaveUserData,
       "claWebRadiusAuthentication": claWebRadiusAuthentication,
       "claRadiusFallbackMode": claRadiusFallbackMode,
       "claRadiusFallbackUsername": claRadiusFallbackUsername,
       "claRadiusFallbackInterval": claRadiusFallbackInterval,
       "claRadiusAuthMacDelimiter": claRadiusAuthMacDelimiter,
       "claRadiusAcctMacDelimiter": claRadiusAcctMacDelimiter,
       "claAcceptMICertificate": claAcceptMICertificate,
       "claAcceptLSCertificate": claAcceptLSCertificate,
       "claAllowAuthorizeLscApAgainstAAA": claAllowAuthorizeLscApAgainstAAA,
       "claStatusObjects": claStatusObjects,
       "claRadiusServerTable": claRadiusServerTable,
       "claRadiusServerEntry": claRadiusServerEntry,
       "claRadiusReqId": claRadiusReqId,
       "claRadiusAddressType": claRadiusAddressType,
       "claRadiusAddress": claRadiusAddress,
       "claRadiusPortNum": claRadiusPortNum,
       "claRadiusWlanIdx": claRadiusWlanIdx,
       "claRadiusClientMacAddress": claRadiusClientMacAddress,
       "claRadiusUserName": claRadiusUserName,
       "claDBCurrentUsedEntries": claDBCurrentUsedEntries,
       "ciscoLwappAAAMIBConform": ciscoLwappAAAMIBConform,
       "ciscoLwappAAAMIBCompliances": ciscoLwappAAAMIBCompliances,
       "ciscoLwappAAAMIBCompliance": ciscoLwappAAAMIBCompliance,
       "ciscoLwappAAAMIBComplianceRev1": ciscoLwappAAAMIBComplianceRev1,
       "ciscoLwappAAAMIBGroups": ciscoLwappAAAMIBGroups,
       "ciscoLwappAAAMIBConfigGroup": ciscoLwappAAAMIBConfigGroup,
       "ciscoLwappAAAMIBSaveUserConfigGroup": ciscoLwappAAAMIBSaveUserConfigGroup,
       "ciscoLwappAAAMIBNotifsGroup": ciscoLwappAAAMIBNotifsGroup,
       "ciscoLwappAAAMIBStatusObjsGroup": ciscoLwappAAAMIBStatusObjsGroup,
       "ciscoLwappAAAMIBDBEntriesGroup": ciscoLwappAAAMIBDBEntriesGroup,
       "ciscoLwappAAAMIBRadiusConfigGroup": ciscoLwappAAAMIBRadiusConfigGroup,
       "ciscoLwappAAAMIBAPPolicyConfigGroup": ciscoLwappAAAMIBAPPolicyConfigGroup,
       "ciscoLwappAAAMIBWlanAuthAccServerConfigGroup": ciscoLwappAAAMIBWlanAuthAccServerConfigGroup}
)
