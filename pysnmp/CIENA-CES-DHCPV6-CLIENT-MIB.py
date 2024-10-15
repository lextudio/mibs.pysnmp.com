# SNMP MIB module (CIENA-CES-DHCPV6-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-DHCPV6-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:57 2024
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

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaStatsClear")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesDhcpv6ClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30)
)
cienaCesDhcpv6ClientMIB.setRevisions(
        ("2016-06-21 00:00",
         "2016-01-19 00:00",
         "2015-11-02 00:00",
         "2015-08-06 00:00",
         "2013-10-17 00:00",
         "2013-09-24 00:00",
         "2013-07-19 00:00",
         "2013-02-11 19:00",
         "2013-02-11 00:00",
         "2013-02-08 00:00",
         "2012-11-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesDhcpv6ClientMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBObjects = _CienaCesDhcpv6ClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1)
)
_CienaCesDhcpv6Client_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6Client = _CienaCesDhcpv6Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1)
)
_CienaCesDhcpv6AdminState_Type = CienaGlobalState
_CienaCesDhcpv6AdminState_Object = MibScalar
cienaCesDhcpv6AdminState = _CienaCesDhcpv6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 1),
    _CienaCesDhcpv6AdminState_Type()
)
cienaCesDhcpv6AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6AdminState.setStatus("current")


class _CienaCesDhcpv6IfName_Type(DisplayString):
    """Custom type cienaCesDhcpv6IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesDhcpv6IfName_Type.__name__ = "DisplayString"
_CienaCesDhcpv6IfName_Object = MibScalar
cienaCesDhcpv6IfName = _CienaCesDhcpv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 2),
    _CienaCesDhcpv6IfName_Type()
)
cienaCesDhcpv6IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6IfName.setStatus("current")
_CienaCesDhcpv6RapidCommitState_Type = CienaGlobalState
_CienaCesDhcpv6RapidCommitState_Object = MibScalar
cienaCesDhcpv6RapidCommitState = _CienaCesDhcpv6RapidCommitState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 3),
    _CienaCesDhcpv6RapidCommitState_Type()
)
cienaCesDhcpv6RapidCommitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6RapidCommitState.setStatus("current")


class _CienaCesDhcpv6PrefLifetimeReq_Type(Integer32):
    """Custom type cienaCesDhcpv6PrefLifetimeReq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CienaCesDhcpv6PrefLifetimeReq_Type.__name__ = "Integer32"
_CienaCesDhcpv6PrefLifetimeReq_Object = MibScalar
cienaCesDhcpv6PrefLifetimeReq = _CienaCesDhcpv6PrefLifetimeReq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 5),
    _CienaCesDhcpv6PrefLifetimeReq_Type()
)
cienaCesDhcpv6PrefLifetimeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6PrefLifetimeReq.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6PrefLifetimeReq.setUnits("seconds")


class _CienaCesDhcpv6ValidLifetimeReq_Type(Integer32):
    """Custom type cienaCesDhcpv6ValidLifetimeReq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CienaCesDhcpv6ValidLifetimeReq_Type.__name__ = "Integer32"
_CienaCesDhcpv6ValidLifetimeReq_Object = MibScalar
cienaCesDhcpv6ValidLifetimeReq = _CienaCesDhcpv6ValidLifetimeReq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 6),
    _CienaCesDhcpv6ValidLifetimeReq_Type()
)
cienaCesDhcpv6ValidLifetimeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ValidLifetimeReq.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ValidLifetimeReq.setUnits("seconds")
_CienaCesDhcpv6ClientOptionTable_Object = MibTable
cienaCesDhcpv6ClientOptionTable = _CienaCesDhcpv6ClientOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientOptionTable.setStatus("current")
_CienaCesDhcpv6ClientOptionEntry_Object = MibTableRow
cienaCesDhcpv6ClientOptionEntry = _CienaCesDhcpv6ClientOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7, 1)
)
cienaCesDhcpv6ClientOptionEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6OptionCodeIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientOptionEntry.setStatus("current")


class _CienaCesDhcpv6OptionCodeIndex_Type(Integer32):
    """Custom type cienaCesDhcpv6OptionCodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6OptionCodeIndex_Type.__name__ = "Integer32"
_CienaCesDhcpv6OptionCodeIndex_Object = MibTableColumn
cienaCesDhcpv6OptionCodeIndex = _CienaCesDhcpv6OptionCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7, 1, 1),
    _CienaCesDhcpv6OptionCodeIndex_Type()
)
cienaCesDhcpv6OptionCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6OptionCodeIndex.setStatus("current")
_CienaCesDhcpv6OptionDesc_Type = DisplayString
_CienaCesDhcpv6OptionDesc_Object = MibTableColumn
cienaCesDhcpv6OptionDesc = _CienaCesDhcpv6OptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7, 1, 2),
    _CienaCesDhcpv6OptionDesc_Type()
)
cienaCesDhcpv6OptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6OptionDesc.setStatus("current")


class _CienaCesDhcpv6OptionCode_Type(Integer32):
    """Custom type cienaCesDhcpv6OptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CienaCesDhcpv6OptionCode_Type.__name__ = "Integer32"
_CienaCesDhcpv6OptionCode_Object = MibTableColumn
cienaCesDhcpv6OptionCode = _CienaCesDhcpv6OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7, 1, 3),
    _CienaCesDhcpv6OptionCode_Type()
)
cienaCesDhcpv6OptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6OptionCode.setStatus("current")
_CienaCesDhcpv6OptionState_Type = CienaGlobalState
_CienaCesDhcpv6OptionState_Object = MibTableColumn
cienaCesDhcpv6OptionState = _CienaCesDhcpv6OptionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 7, 1, 4),
    _CienaCesDhcpv6OptionState_Type()
)
cienaCesDhcpv6OptionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6OptionState.setStatus("current")
_CienaCesDhcpv6ClientSessTable_Object = MibTable
cienaCesDhcpv6ClientSessTable = _CienaCesDhcpv6ClientSessTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessTable.setStatus("current")
_CienaCesDhcpv6ClientSessEntry_Object = MibTableRow
cienaCesDhcpv6ClientSessEntry = _CienaCesDhcpv6ClientSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1)
)
cienaCesDhcpv6ClientSessEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6ClientSessMgmtIntfIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessEntry.setStatus("current")


class _CienaCesDhcpv6ClientSessMgmtIntfIndex_Type(Integer32):
    """Custom type cienaCesDhcpv6ClientSessMgmtIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6ClientSessMgmtIntfIndex_Type.__name__ = "Integer32"
_CienaCesDhcpv6ClientSessMgmtIntfIndex_Object = MibTableColumn
cienaCesDhcpv6ClientSessMgmtIntfIndex = _CienaCesDhcpv6ClientSessMgmtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 1),
    _CienaCesDhcpv6ClientSessMgmtIntfIndex_Type()
)
cienaCesDhcpv6ClientSessMgmtIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessMgmtIntfIndex.setStatus("current")


class _CienaCesDhcpv6ClientSessState_Type(Integer32):
    """Custom type cienaCesDhcpv6ClientSessState based on Integer32"""
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
              8,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("disabled", 1),
          ("init", 2),
          ("rebinding", 5),
          ("reconfigure", 8),
          ("renewing", 4),
          ("request", 7),
          ("solicit", 6),
          ("unknown", 99))
    )


_CienaCesDhcpv6ClientSessState_Type.__name__ = "Integer32"
_CienaCesDhcpv6ClientSessState_Object = MibTableColumn
cienaCesDhcpv6ClientSessState = _CienaCesDhcpv6ClientSessState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 2),
    _CienaCesDhcpv6ClientSessState_Type()
)
cienaCesDhcpv6ClientSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessState.setStatus("current")


class _CienaCesDhcpv6ClientSessAutoConfigState_Type(Integer32):
    """Custom type cienaCesDhcpv6ClientSessAutoConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("stateful", 3),
          ("stateless", 2),
          ("unknown", 99))
    )


_CienaCesDhcpv6ClientSessAutoConfigState_Type.__name__ = "Integer32"
_CienaCesDhcpv6ClientSessAutoConfigState_Object = MibTableColumn
cienaCesDhcpv6ClientSessAutoConfigState = _CienaCesDhcpv6ClientSessAutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 3),
    _CienaCesDhcpv6ClientSessAutoConfigState_Type()
)
cienaCesDhcpv6ClientSessAutoConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessAutoConfigState.setStatus("current")
_CienaCesDhcpv6ClientSessUpTime_Type = Integer32
_CienaCesDhcpv6ClientSessUpTime_Object = MibTableColumn
cienaCesDhcpv6ClientSessUpTime = _CienaCesDhcpv6ClientSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 4),
    _CienaCesDhcpv6ClientSessUpTime_Type()
)
cienaCesDhcpv6ClientSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessUpTime.setStatus("current")
_CienaCesDhcpv6ClientSessPrefLifetime_Type = Integer32
_CienaCesDhcpv6ClientSessPrefLifetime_Object = MibTableColumn
cienaCesDhcpv6ClientSessPrefLifetime = _CienaCesDhcpv6ClientSessPrefLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 5),
    _CienaCesDhcpv6ClientSessPrefLifetime_Type()
)
cienaCesDhcpv6ClientSessPrefLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessPrefLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessPrefLifetime.setUnits("seconds")
_CienaCesDhcpv6ClientSessValidLifetime_Type = Integer32
_CienaCesDhcpv6ClientSessValidLifetime_Object = MibTableColumn
cienaCesDhcpv6ClientSessValidLifetime = _CienaCesDhcpv6ClientSessValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 6),
    _CienaCesDhcpv6ClientSessValidLifetime_Type()
)
cienaCesDhcpv6ClientSessValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessValidLifetime.setUnits("seconds")
_CienaCesDhcpv6ClientSessLeaseExpire_Type = Integer32
_CienaCesDhcpv6ClientSessLeaseExpire_Object = MibTableColumn
cienaCesDhcpv6ClientSessLeaseExpire = _CienaCesDhcpv6ClientSessLeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 7),
    _CienaCesDhcpv6ClientSessLeaseExpire_Type()
)
cienaCesDhcpv6ClientSessLeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessLeaseExpire.setStatus("current")
_CienaCesDhcpv6ClientSessClientId_Type = DisplayString
_CienaCesDhcpv6ClientSessClientId_Object = MibTableColumn
cienaCesDhcpv6ClientSessClientId = _CienaCesDhcpv6ClientSessClientId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 8),
    _CienaCesDhcpv6ClientSessClientId_Type()
)
cienaCesDhcpv6ClientSessClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessClientId.setStatus("current")
_CienaCesDhcpv6ClientSessServerIpAddrType_Type = InetAddressType
_CienaCesDhcpv6ClientSessServerIpAddrType_Object = MibTableColumn
cienaCesDhcpv6ClientSessServerIpAddrType = _CienaCesDhcpv6ClientSessServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 9),
    _CienaCesDhcpv6ClientSessServerIpAddrType_Type()
)
cienaCesDhcpv6ClientSessServerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessServerIpAddrType.setStatus("current")
_CienaCesDhcpv6ClientSessServerIpAddr_Type = InetAddress
_CienaCesDhcpv6ClientSessServerIpAddr_Object = MibTableColumn
cienaCesDhcpv6ClientSessServerIpAddr = _CienaCesDhcpv6ClientSessServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 10),
    _CienaCesDhcpv6ClientSessServerIpAddr_Type()
)
cienaCesDhcpv6ClientSessServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessServerIpAddr.setStatus("current")
_CienaCesDhcpv6ClientSessServerId_Type = DisplayString
_CienaCesDhcpv6ClientSessServerId_Object = MibTableColumn
cienaCesDhcpv6ClientSessServerId = _CienaCesDhcpv6ClientSessServerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 11),
    _CienaCesDhcpv6ClientSessServerId_Type()
)
cienaCesDhcpv6ClientSessServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessServerId.setStatus("current")
_CienaCesDhcpv6ClientSessT1Time_Type = Integer32
_CienaCesDhcpv6ClientSessT1Time_Object = MibTableColumn
cienaCesDhcpv6ClientSessT1Time = _CienaCesDhcpv6ClientSessT1Time_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 12),
    _CienaCesDhcpv6ClientSessT1Time_Type()
)
cienaCesDhcpv6ClientSessT1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessT1Time.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessT1Time.setUnits("seconds")
_CienaCesDhcpv6ClientSessT2Time_Type = Integer32
_CienaCesDhcpv6ClientSessT2Time_Object = MibTableColumn
cienaCesDhcpv6ClientSessT2Time = _CienaCesDhcpv6ClientSessT2Time_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 8, 1, 13),
    _CienaCesDhcpv6ClientSessT2Time_Type()
)
cienaCesDhcpv6ClientSessT2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessT2Time.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessT2Time.setUnits("seconds")
_CienaCesDhcpv6ClientSessStatsTable_Object = MibTable
cienaCesDhcpv6ClientSessStatsTable = _CienaCesDhcpv6ClientSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsTable.setStatus("current")
_CienaCesDhcpv6ClientSessStatsEntry_Object = MibTableRow
cienaCesDhcpv6ClientSessStatsEntry = _CienaCesDhcpv6ClientSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1)
)
cienaCesDhcpv6ClientSessStatsEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6ClientSessStatsMgmtIntfIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsEntry.setStatus("current")


class _CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type(Integer32):
    """Custom type cienaCesDhcpv6ClientSessStatsMgmtIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type.__name__ = "Integer32"
_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsMgmtIntfIndex = _CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 1),
    _CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type()
)
cienaCesDhcpv6ClientSessStatsMgmtIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsMgmtIntfIndex.setStatus("current")


class _CienaCesDhcpv6ClientSessStatsClear_Type(CienaStatsClear):
    """Custom type cienaCesDhcpv6ClientSessStatsClear based on CienaStatsClear"""
    defaultValue = 0


_CienaCesDhcpv6ClientSessStatsClear_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsClear = _CienaCesDhcpv6ClientSessStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 2),
    _CienaCesDhcpv6ClientSessStatsClear_Type()
)
cienaCesDhcpv6ClientSessStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsClear.setStatus("current")
_CienaCesDhcpv6ClientSessStatsPktsRx_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsPktsRx_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsPktsRx = _CienaCesDhcpv6ClientSessStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 3),
    _CienaCesDhcpv6ClientSessStatsPktsRx_Type()
)
cienaCesDhcpv6ClientSessStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsPktsRx.setStatus("current")
_CienaCesDhcpv6ClientSessStatsReply_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsReply_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsReply = _CienaCesDhcpv6ClientSessStatsReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 4),
    _CienaCesDhcpv6ClientSessStatsReply_Type()
)
cienaCesDhcpv6ClientSessStatsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsReply.setStatus("current")
_CienaCesDhcpv6ClientSessStatsAdvert_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsAdvert_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsAdvert = _CienaCesDhcpv6ClientSessStatsAdvert_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 5),
    _CienaCesDhcpv6ClientSessStatsAdvert_Type()
)
cienaCesDhcpv6ClientSessStatsAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsAdvert.setStatus("current")
_CienaCesDhcpv6ClientSessStatsRecfg_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsRecfg_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsRecfg = _CienaCesDhcpv6ClientSessStatsRecfg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 6),
    _CienaCesDhcpv6ClientSessStatsRecfg_Type()
)
cienaCesDhcpv6ClientSessStatsRecfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsRecfg.setStatus("current")
_CienaCesDhcpv6ClientSessStatsInvalid_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsInvalid_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsInvalid = _CienaCesDhcpv6ClientSessStatsInvalid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 7),
    _CienaCesDhcpv6ClientSessStatsInvalid_Type()
)
cienaCesDhcpv6ClientSessStatsInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsInvalid.setStatus("current")
_CienaCesDhcpv6ClientSessStatsPktsTx_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsPktsTx_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsPktsTx = _CienaCesDhcpv6ClientSessStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 8),
    _CienaCesDhcpv6ClientSessStatsPktsTx_Type()
)
cienaCesDhcpv6ClientSessStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsPktsTx.setStatus("current")
_CienaCesDhcpv6ClientSessStatsSolicit_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsSolicit_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsSolicit = _CienaCesDhcpv6ClientSessStatsSolicit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 9),
    _CienaCesDhcpv6ClientSessStatsSolicit_Type()
)
cienaCesDhcpv6ClientSessStatsSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsSolicit.setStatus("current")
_CienaCesDhcpv6ClientSessStatsRequest_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsRequest_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsRequest = _CienaCesDhcpv6ClientSessStatsRequest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 10),
    _CienaCesDhcpv6ClientSessStatsRequest_Type()
)
cienaCesDhcpv6ClientSessStatsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsRequest.setStatus("current")
_CienaCesDhcpv6ClientSessStatsConfirm_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsConfirm_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsConfirm = _CienaCesDhcpv6ClientSessStatsConfirm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 11),
    _CienaCesDhcpv6ClientSessStatsConfirm_Type()
)
cienaCesDhcpv6ClientSessStatsConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsConfirm.setStatus("current")
_CienaCesDhcpv6ClientSessStatsRenew_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsRenew_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsRenew = _CienaCesDhcpv6ClientSessStatsRenew_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 12),
    _CienaCesDhcpv6ClientSessStatsRenew_Type()
)
cienaCesDhcpv6ClientSessStatsRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsRenew.setStatus("current")
_CienaCesDhcpv6ClientSessStatsRebind_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsRebind_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsRebind = _CienaCesDhcpv6ClientSessStatsRebind_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 13),
    _CienaCesDhcpv6ClientSessStatsRebind_Type()
)
cienaCesDhcpv6ClientSessStatsRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsRebind.setStatus("current")
_CienaCesDhcpv6ClientSessStatsInfoReq_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsInfoReq_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsInfoReq = _CienaCesDhcpv6ClientSessStatsInfoReq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 14),
    _CienaCesDhcpv6ClientSessStatsInfoReq_Type()
)
cienaCesDhcpv6ClientSessStatsInfoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsInfoReq.setStatus("current")
_CienaCesDhcpv6ClientSessStatsRelease_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsRelease_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsRelease = _CienaCesDhcpv6ClientSessStatsRelease_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 15),
    _CienaCesDhcpv6ClientSessStatsRelease_Type()
)
cienaCesDhcpv6ClientSessStatsRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsRelease.setStatus("current")
_CienaCesDhcpv6ClientSessStatsDecline_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsDecline_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsDecline = _CienaCesDhcpv6ClientSessStatsDecline_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 16),
    _CienaCesDhcpv6ClientSessStatsDecline_Type()
)
cienaCesDhcpv6ClientSessStatsDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsDecline.setStatus("current")
_CienaCesDhcpv6ClientSessStatsTxFail_Type = Gauge32
_CienaCesDhcpv6ClientSessStatsTxFail_Object = MibTableColumn
cienaCesDhcpv6ClientSessStatsTxFail = _CienaCesDhcpv6ClientSessStatsTxFail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 1, 9, 1, 17),
    _CienaCesDhcpv6ClientSessStatsTxFail_Type()
)
cienaCesDhcpv6ClientSessStatsTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6ClientSessStatsTxFail.setStatus("current")
_CienaCesDhcpv6RelayAgent_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6RelayAgent = _CienaCesDhcpv6RelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2)
)
_CienaCesDhcpv6RelayAgentGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6RelayAgentGlobalAttrs = _CienaCesDhcpv6RelayAgentGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1)
)
_CienaCesDhcpv6LdraState_Type = CienaGlobalState
_CienaCesDhcpv6LdraState_Object = MibScalar
cienaCesDhcpv6LdraState = _CienaCesDhcpv6LdraState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 1),
    _CienaCesDhcpv6LdraState_Type()
)
cienaCesDhcpv6LdraState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraState.setStatus("current")


class _CienaCesDhcpv6LdraInterfaceId_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intidString", 3),
          ("slotAndPort", 1),
          ("slotAndPortAndVlan", 2))
    )


_CienaCesDhcpv6LdraInterfaceId_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraInterfaceId_Object = MibScalar
cienaCesDhcpv6LdraInterfaceId = _CienaCesDhcpv6LdraInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 2),
    _CienaCesDhcpv6LdraInterfaceId_Type()
)
cienaCesDhcpv6LdraInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraInterfaceId.setStatus("current")


class _CienaCesDhcpv6LdraRemoteId_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraRemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hostName", 2),
          ("macAddress", 1),
          ("ridString", 3))
    )


_CienaCesDhcpv6LdraRemoteId_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraRemoteId_Object = MibScalar
cienaCesDhcpv6LdraRemoteId = _CienaCesDhcpv6LdraRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 3),
    _CienaCesDhcpv6LdraRemoteId_Type()
)
cienaCesDhcpv6LdraRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRemoteId.setStatus("current")


class _CienaCesDhcpv6LdraRemoteIdOption_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraRemoteIdOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesDhcpv6LdraRemoteIdOption_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraRemoteIdOption_Object = MibScalar
cienaCesDhcpv6LdraRemoteIdOption = _CienaCesDhcpv6LdraRemoteIdOption_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 4),
    _CienaCesDhcpv6LdraRemoteIdOption_Type()
)
cienaCesDhcpv6LdraRemoteIdOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRemoteIdOption.setStatus("current")


class _CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type(Unsigned32):
    """Custom type cienaCesDhcpv6LdraRemoteIdEnterpriseNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type.__name__ = "Unsigned32"
_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Object = MibScalar
cienaCesDhcpv6LdraRemoteIdEnterpriseNo = _CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 5),
    _CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type()
)
cienaCesDhcpv6LdraRemoteIdEnterpriseNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRemoteIdEnterpriseNo.setStatus("current")
_CienaCesDhcpv6LdraForward_Type = Counter32
_CienaCesDhcpv6LdraForward_Object = MibScalar
cienaCesDhcpv6LdraForward = _CienaCesDhcpv6LdraForward_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 6),
    _CienaCesDhcpv6LdraForward_Type()
)
cienaCesDhcpv6LdraForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraForward.setStatus("current")
_CienaCesDhcpv6LdraRelayed_Type = Counter32
_CienaCesDhcpv6LdraRelayed_Object = MibScalar
cienaCesDhcpv6LdraRelayed = _CienaCesDhcpv6LdraRelayed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 7),
    _CienaCesDhcpv6LdraRelayed_Type()
)
cienaCesDhcpv6LdraRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRelayed.setStatus("current")
_CienaCesDhcpv6LdraDropped_Type = Counter32
_CienaCesDhcpv6LdraDropped_Object = MibScalar
cienaCesDhcpv6LdraDropped = _CienaCesDhcpv6LdraDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 8),
    _CienaCesDhcpv6LdraDropped_Type()
)
cienaCesDhcpv6LdraDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraDropped.setStatus("current")


class _CienaCesDhcpv6LdraGlobalStatsClear_Type(CienaStatsClear):
    """Custom type cienaCesDhcpv6LdraGlobalStatsClear based on CienaStatsClear"""
    defaultValue = 0


_CienaCesDhcpv6LdraGlobalStatsClear_Object = MibScalar
cienaCesDhcpv6LdraGlobalStatsClear = _CienaCesDhcpv6LdraGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 9),
    _CienaCesDhcpv6LdraGlobalStatsClear_Type()
)
cienaCesDhcpv6LdraGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraGlobalStatsClear.setStatus("current")
_CienaCesDhcpv6LdraNotForRelay_Type = Counter32
_CienaCesDhcpv6LdraNotForRelay_Object = MibScalar
cienaCesDhcpv6LdraNotForRelay = _CienaCesDhcpv6LdraNotForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 1, 10),
    _CienaCesDhcpv6LdraNotForRelay_Type()
)
cienaCesDhcpv6LdraNotForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraNotForRelay.setStatus("current")
_CienaCesDhcpv6LdraStateTable_Object = MibTable
cienaCesDhcpv6LdraStateTable = _CienaCesDhcpv6LdraStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraStateTable.setStatus("current")
_CienaCesDhcpv6LdraStateEntry_Object = MibTableRow
cienaCesDhcpv6LdraStateEntry = _CienaCesDhcpv6LdraStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2, 1)
)
cienaCesDhcpv6LdraStateEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraStateEntry.setStatus("current")


class _CienaCesDhcpv6LdraVlan_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_CienaCesDhcpv6LdraVlan_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVlan_Object = MibTableColumn
cienaCesDhcpv6LdraVlan = _CienaCesDhcpv6LdraVlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2, 1, 1),
    _CienaCesDhcpv6LdraVlan_Type()
)
cienaCesDhcpv6LdraVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVlan.setStatus("current")
_CienaCesDhcpv6LdraAdminState_Type = CienaGlobalState
_CienaCesDhcpv6LdraAdminState_Object = MibTableColumn
cienaCesDhcpv6LdraAdminState = _CienaCesDhcpv6LdraAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2, 1, 2),
    _CienaCesDhcpv6LdraAdminState_Type()
)
cienaCesDhcpv6LdraAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraAdminState.setStatus("current")
_CienaCesDhcpv6LdraOperState_Type = CienaGlobalState
_CienaCesDhcpv6LdraOperState_Object = MibTableColumn
cienaCesDhcpv6LdraOperState = _CienaCesDhcpv6LdraOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2, 1, 3),
    _CienaCesDhcpv6LdraOperState_Type()
)
cienaCesDhcpv6LdraOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraOperState.setStatus("current")
_CienaCesDhcpv6LdraRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraRowStatus = _CienaCesDhcpv6LdraRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 2, 1, 4),
    _CienaCesDhcpv6LdraRowStatus_Type()
)
cienaCesDhcpv6LdraRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRowStatus.setStatus("current")
_CienaCesDhcpv6LdraTrustTable_Object = MibTable
cienaCesDhcpv6LdraTrustTable = _CienaCesDhcpv6LdraTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraTrustTable.setStatus("deprecated")
_CienaCesDhcpv6LdraTrustEntry_Object = MibTableRow
cienaCesDhcpv6LdraTrustEntry = _CienaCesDhcpv6LdraTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 3, 1)
)
cienaCesDhcpv6LdraTrustEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraTrustEntry.setStatus("deprecated")


class _CienaCesDhcpv6LdraPort_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6LdraPort_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraPort_Object = MibTableColumn
cienaCesDhcpv6LdraPort = _CienaCesDhcpv6LdraPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 3, 1, 1),
    _CienaCesDhcpv6LdraPort_Type()
)
cienaCesDhcpv6LdraPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraPort.setStatus("current")


class _CienaCesDhcpv6LdraTrustMode_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("clientTrust", 2),
          ("dualRoleTrust", 4),
          ("serverTrust", 3),
          ("unTrust", 5))
    )


_CienaCesDhcpv6LdraTrustMode_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraTrustMode_Object = MibTableColumn
cienaCesDhcpv6LdraTrustMode = _CienaCesDhcpv6LdraTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 3, 1, 2),
    _CienaCesDhcpv6LdraTrustMode_Type()
)
cienaCesDhcpv6LdraTrustMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraTrustMode.setStatus("deprecated")
_CienaCesDhcpv6LdraStatsTable_Object = MibTable
cienaCesDhcpv6LdraStatsTable = _CienaCesDhcpv6LdraStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraStatsTable.setStatus("current")
_CienaCesDhcpv6LdraStatsEntry_Object = MibTableRow
cienaCesDhcpv6LdraStatsEntry = _CienaCesDhcpv6LdraStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1)
)
cienaCesDhcpv6LdraStatsEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraStatsEntry.setStatus("current")
_CienaCesDhcpv6LdraPktsForRelay_Type = Counter32
_CienaCesDhcpv6LdraPktsForRelay_Object = MibTableColumn
cienaCesDhcpv6LdraPktsForRelay = _CienaCesDhcpv6LdraPktsForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 1),
    _CienaCesDhcpv6LdraPktsForRelay_Type()
)
cienaCesDhcpv6LdraPktsForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraPktsForRelay.setStatus("current")
_CienaCesDhcpv6LdraRelayedClient_Type = Counter32
_CienaCesDhcpv6LdraRelayedClient_Object = MibTableColumn
cienaCesDhcpv6LdraRelayedClient = _CienaCesDhcpv6LdraRelayedClient_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 2),
    _CienaCesDhcpv6LdraRelayedClient_Type()
)
cienaCesDhcpv6LdraRelayedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRelayedClient.setStatus("current")
_CienaCesDhcpv6LdraRelayedServer_Type = Counter32
_CienaCesDhcpv6LdraRelayedServer_Object = MibTableColumn
cienaCesDhcpv6LdraRelayedServer = _CienaCesDhcpv6LdraRelayedServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 3),
    _CienaCesDhcpv6LdraRelayedServer_Type()
)
cienaCesDhcpv6LdraRelayedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRelayedServer.setStatus("current")
_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Type = Counter32
_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraUntrustedClientPortPktsRx = _CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 4),
    _CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Type()
)
cienaCesDhcpv6LdraUntrustedClientPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraUntrustedClientPortPktsRx.setStatus("current")
_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Type = Counter32
_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraUntrustedServerPortPktsRx = _CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 5),
    _CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Type()
)
cienaCesDhcpv6LdraUntrustedServerPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraUntrustedServerPortPktsRx.setStatus("current")
_CienaCesDhcpv6LdraFailedValidationPktDrop_Type = Counter32
_CienaCesDhcpv6LdraFailedValidationPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraFailedValidationPktDrop = _CienaCesDhcpv6LdraFailedValidationPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 6),
    _CienaCesDhcpv6LdraFailedValidationPktDrop_Type()
)
cienaCesDhcpv6LdraFailedValidationPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraFailedValidationPktDrop.setStatus("current")
_CienaCesDhcpv6LdraInvalidConfigPktDrop_Type = Counter32
_CienaCesDhcpv6LdraInvalidConfigPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraInvalidConfigPktDrop = _CienaCesDhcpv6LdraInvalidConfigPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 7),
    _CienaCesDhcpv6LdraInvalidConfigPktDrop_Type()
)
cienaCesDhcpv6LdraInvalidConfigPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraInvalidConfigPktDrop.setStatus("current")
_CienaCesDhcpv6LdraExceededHopCountPktDrop_Type = Counter32
_CienaCesDhcpv6LdraExceededHopCountPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraExceededHopCountPktDrop = _CienaCesDhcpv6LdraExceededHopCountPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 8),
    _CienaCesDhcpv6LdraExceededHopCountPktDrop_Type()
)
cienaCesDhcpv6LdraExceededHopCountPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExceededHopCountPktDrop.setStatus("current")
_CienaCesDhcpv6LdraExceedMTUPktDrop_Type = Counter32
_CienaCesDhcpv6LdraExceedMTUPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraExceedMTUPktDrop = _CienaCesDhcpv6LdraExceedMTUPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 9),
    _CienaCesDhcpv6LdraExceedMTUPktDrop_Type()
)
cienaCesDhcpv6LdraExceedMTUPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExceedMTUPktDrop.setStatus("current")
_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Type = Counter32
_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraNoTrustedServerPktDrop = _CienaCesDhcpv6LdraNoTrustedServerPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 10),
    _CienaCesDhcpv6LdraNoTrustedServerPktDrop_Type()
)
cienaCesDhcpv6LdraNoTrustedServerPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraNoTrustedServerPktDrop.setStatus("current")
_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Type = Counter32
_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraNoTrustedClientPktDrop = _CienaCesDhcpv6LdraNoTrustedClientPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 11),
    _CienaCesDhcpv6LdraNoTrustedClientPktDrop_Type()
)
cienaCesDhcpv6LdraNoTrustedClientPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraNoTrustedClientPktDrop.setStatus("current")
_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Type = Counter32
_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop = _CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 12),
    _CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Type()
)
cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop.setStatus("current")
_CienaCesDhcpv6LdraGeneralErrors_Type = Counter32
_CienaCesDhcpv6LdraGeneralErrors_Object = MibTableColumn
cienaCesDhcpv6LdraGeneralErrors = _CienaCesDhcpv6LdraGeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 13),
    _CienaCesDhcpv6LdraGeneralErrors_Type()
)
cienaCesDhcpv6LdraGeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraGeneralErrors.setStatus("current")


class _CienaCesDhcpv6LdraStatsClear_Type(CienaStatsClear):
    """Custom type cienaCesDhcpv6LdraStatsClear based on CienaStatsClear"""
    defaultValue = 0


_CienaCesDhcpv6LdraStatsClear_Object = MibTableColumn
cienaCesDhcpv6LdraStatsClear = _CienaCesDhcpv6LdraStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 4, 1, 14),
    _CienaCesDhcpv6LdraStatsClear_Type()
)
cienaCesDhcpv6LdraStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraStatsClear.setStatus("current")
_CienaCesDhcpv6LdraIntidStringTable_Object = MibTable
cienaCesDhcpv6LdraIntidStringTable = _CienaCesDhcpv6LdraIntidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIntidStringTable.setStatus("current")
_CienaCesDhcpv6LdraIntidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraIntidStringEntry = _CienaCesDhcpv6LdraIntidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 5, 1)
)
cienaCesDhcpv6LdraIntidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraIntidStringPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIntidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraIntidStringPort_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraIntidStringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6LdraIntidStringPort_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraIntidStringPort_Object = MibTableColumn
cienaCesDhcpv6LdraIntidStringPort = _CienaCesDhcpv6LdraIntidStringPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 5, 1, 1),
    _CienaCesDhcpv6LdraIntidStringPort_Type()
)
cienaCesDhcpv6LdraIntidStringPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIntidStringPort.setStatus("current")


class _CienaCesDhcpv6LdraIntidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraIntidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraIntidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraIntidString_Object = MibTableColumn
cienaCesDhcpv6LdraIntidString = _CienaCesDhcpv6LdraIntidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 5, 1, 2),
    _CienaCesDhcpv6LdraIntidString_Type()
)
cienaCesDhcpv6LdraIntidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIntidString.setStatus("current")
_CienaCesDhcpv6LdraIntidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraIntidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraIntidStringRowStatus = _CienaCesDhcpv6LdraIntidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 5, 1, 3),
    _CienaCesDhcpv6LdraIntidStringRowStatus_Type()
)
cienaCesDhcpv6LdraIntidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraIntidStringRowStatus.setStatus("current")
_CienaCesDhcpv6LdraRidStringTable_Object = MibTable
cienaCesDhcpv6LdraRidStringTable = _CienaCesDhcpv6LdraRidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRidStringTable.setStatus("current")
_CienaCesDhcpv6LdraRidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraRidStringEntry = _CienaCesDhcpv6LdraRidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 6, 1)
)
cienaCesDhcpv6LdraRidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraRidStringPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraRidStringPort_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraRidStringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6LdraRidStringPort_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraRidStringPort_Object = MibTableColumn
cienaCesDhcpv6LdraRidStringPort = _CienaCesDhcpv6LdraRidStringPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 6, 1, 1),
    _CienaCesDhcpv6LdraRidStringPort_Type()
)
cienaCesDhcpv6LdraRidStringPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRidStringPort.setStatus("current")


class _CienaCesDhcpv6LdraRidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraRidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraRidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraRidString_Object = MibTableColumn
cienaCesDhcpv6LdraRidString = _CienaCesDhcpv6LdraRidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 6, 1, 2),
    _CienaCesDhcpv6LdraRidString_Type()
)
cienaCesDhcpv6LdraRidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRidString.setStatus("current")
_CienaCesDhcpv6LdraRidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraRidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraRidStringRowStatus = _CienaCesDhcpv6LdraRidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 6, 1, 3),
    _CienaCesDhcpv6LdraRidStringRowStatus_Type()
)
cienaCesDhcpv6LdraRidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraRidStringRowStatus.setStatus("current")
_CienaCesDhcpv6LdraExtTrustTable_Object = MibTable
cienaCesDhcpv6LdraExtTrustTable = _CienaCesDhcpv6LdraExtTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExtTrustTable.setStatus("current")
_CienaCesDhcpv6LdraExtTrustEntry_Object = MibTableRow
cienaCesDhcpv6LdraExtTrustEntry = _CienaCesDhcpv6LdraExtTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 7, 1)
)
cienaCesDhcpv6LdraExtTrustEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExtTrustEntry.setStatus("current")


class _CienaCesDhcpv6LdraExtPortState_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraExtPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CienaCesDhcpv6LdraExtPortState_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraExtPortState_Object = MibTableColumn
cienaCesDhcpv6LdraExtPortState = _CienaCesDhcpv6LdraExtPortState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 7, 1, 1),
    _CienaCesDhcpv6LdraExtPortState_Type()
)
cienaCesDhcpv6LdraExtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExtPortState.setStatus("current")


class _CienaCesDhcpv6LdraExtTrustMode_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraExtTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("clientTrust", 2),
          ("dualRoleTrust", 4),
          ("serverTrust", 3),
          ("unTrust", 5))
    )


_CienaCesDhcpv6LdraExtTrustMode_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraExtTrustMode_Object = MibTableColumn
cienaCesDhcpv6LdraExtTrustMode = _CienaCesDhcpv6LdraExtTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 7, 1, 2),
    _CienaCesDhcpv6LdraExtTrustMode_Type()
)
cienaCesDhcpv6LdraExtTrustMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraExtTrustMode.setStatus("current")
_CienaCesDhcpv6LdraVsStateTable_Object = MibTable
cienaCesDhcpv6LdraVsStateTable = _CienaCesDhcpv6LdraVsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsStateTable.setStatus("current")
_CienaCesDhcpv6LdraVsStateEntry_Object = MibTableRow
cienaCesDhcpv6LdraVsStateEntry = _CienaCesDhcpv6LdraVsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1)
)
cienaCesDhcpv6LdraVsStateEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsVlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsStateEntry.setStatus("current")


class _CienaCesDhcpv6LdraVsVlan_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_CienaCesDhcpv6LdraVsVlan_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVsVlan_Object = MibTableColumn
cienaCesDhcpv6LdraVsVlan = _CienaCesDhcpv6LdraVsVlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1, 1),
    _CienaCesDhcpv6LdraVsVlan_Type()
)
cienaCesDhcpv6LdraVsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsVlan.setStatus("current")


class _CienaCesDhcpv6LdraVsName_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraVsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesDhcpv6LdraVsName_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraVsName_Object = MibTableColumn
cienaCesDhcpv6LdraVsName = _CienaCesDhcpv6LdraVsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1, 2),
    _CienaCesDhcpv6LdraVsName_Type()
)
cienaCesDhcpv6LdraVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsName.setStatus("current")
_CienaCesDhcpv6LdraVsAdminState_Type = CienaGlobalState
_CienaCesDhcpv6LdraVsAdminState_Object = MibTableColumn
cienaCesDhcpv6LdraVsAdminState = _CienaCesDhcpv6LdraVsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1, 3),
    _CienaCesDhcpv6LdraVsAdminState_Type()
)
cienaCesDhcpv6LdraVsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsAdminState.setStatus("current")
_CienaCesDhcpv6LdraVsOperState_Type = CienaGlobalState
_CienaCesDhcpv6LdraVsOperState_Object = MibTableColumn
cienaCesDhcpv6LdraVsOperState = _CienaCesDhcpv6LdraVsOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1, 4),
    _CienaCesDhcpv6LdraVsOperState_Type()
)
cienaCesDhcpv6LdraVsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsOperState.setStatus("current")
_CienaCesDhcpv6LdraVsRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraVsRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraVsRowStatus = _CienaCesDhcpv6LdraVsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 8, 1, 5),
    _CienaCesDhcpv6LdraVsRowStatus_Type()
)
cienaCesDhcpv6LdraVsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRowStatus.setStatus("current")
_CienaCesDhcpv6LdraVsTrustTable_Object = MibTable
cienaCesDhcpv6LdraVsTrustTable = _CienaCesDhcpv6LdraVsTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsTrustTable.setStatus("current")
_CienaCesDhcpv6LdraVsTrustEntry_Object = MibTableRow
cienaCesDhcpv6LdraVsTrustEntry = _CienaCesDhcpv6LdraVsTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9, 1)
)
cienaCesDhcpv6LdraVsTrustEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsPort"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsSubVlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsTrustEntry.setStatus("current")


class _CienaCesDhcpv6LdraVsPort_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDhcpv6LdraVsPort_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVsPort_Object = MibTableColumn
cienaCesDhcpv6LdraVsPort = _CienaCesDhcpv6LdraVsPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9, 1, 1),
    _CienaCesDhcpv6LdraVsPort_Type()
)
cienaCesDhcpv6LdraVsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsPort.setStatus("current")


class _CienaCesDhcpv6LdraVsSubVlan_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVsSubVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_CienaCesDhcpv6LdraVsSubVlan_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVsSubVlan_Object = MibTableColumn
cienaCesDhcpv6LdraVsSubVlan = _CienaCesDhcpv6LdraVsSubVlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9, 1, 2),
    _CienaCesDhcpv6LdraVsSubVlan_Type()
)
cienaCesDhcpv6LdraVsSubVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsSubVlan.setStatus("current")


class _CienaCesDhcpv6LdraVsPortState_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CienaCesDhcpv6LdraVsPortState_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVsPortState_Object = MibTableColumn
cienaCesDhcpv6LdraVsPortState = _CienaCesDhcpv6LdraVsPortState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9, 1, 3),
    _CienaCesDhcpv6LdraVsPortState_Type()
)
cienaCesDhcpv6LdraVsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsPortState.setStatus("current")


class _CienaCesDhcpv6LdraVsTrustMode_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraVsTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("clientTrust", 2),
          ("dualRoleTrust", 4),
          ("serverTrust", 3),
          ("unTrust", 5))
    )


_CienaCesDhcpv6LdraVsTrustMode_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraVsTrustMode_Object = MibTableColumn
cienaCesDhcpv6LdraVsTrustMode = _CienaCesDhcpv6LdraVsTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 9, 1, 4),
    _CienaCesDhcpv6LdraVsTrustMode_Type()
)
cienaCesDhcpv6LdraVsTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsTrustMode.setStatus("current")
_CienaCesDhcpv6LdraVsStatsTable_Object = MibTable
cienaCesDhcpv6LdraVsStatsTable = _CienaCesDhcpv6LdraVsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsStatsTable.setStatus("current")
_CienaCesDhcpv6LdraVsStatsEntry_Object = MibTableRow
cienaCesDhcpv6LdraVsStatsEntry = _CienaCesDhcpv6LdraVsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1)
)
cienaCesDhcpv6LdraVsStatsEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsVlan"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsStatsEntry.setStatus("current")
_CienaCesDhcpv6LdraVsPktsForRelay_Type = Counter32
_CienaCesDhcpv6LdraVsPktsForRelay_Object = MibTableColumn
cienaCesDhcpv6LdraVsPktsForRelay = _CienaCesDhcpv6LdraVsPktsForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 1),
    _CienaCesDhcpv6LdraVsPktsForRelay_Type()
)
cienaCesDhcpv6LdraVsPktsForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsPktsForRelay.setStatus("current")
_CienaCesDhcpv6LdraVsRelayedClient_Type = Counter32
_CienaCesDhcpv6LdraVsRelayedClient_Object = MibTableColumn
cienaCesDhcpv6LdraVsRelayedClient = _CienaCesDhcpv6LdraVsRelayedClient_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 2),
    _CienaCesDhcpv6LdraVsRelayedClient_Type()
)
cienaCesDhcpv6LdraVsRelayedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRelayedClient.setStatus("current")
_CienaCesDhcpv6LdraVsRelayedServer_Type = Counter32
_CienaCesDhcpv6LdraVsRelayedServer_Object = MibTableColumn
cienaCesDhcpv6LdraVsRelayedServer = _CienaCesDhcpv6LdraVsRelayedServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 3),
    _CienaCesDhcpv6LdraVsRelayedServer_Type()
)
cienaCesDhcpv6LdraVsRelayedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRelayedServer.setStatus("current")
_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Type = Counter32
_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx = _CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 4),
    _CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Type()
)
cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx.setStatus("current")
_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Type = Counter32
_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx = _CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 5),
    _CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Type()
)
cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx.setStatus("current")
_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsFailedValidationPktDrop = _CienaCesDhcpv6LdraVsFailedValidationPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 6),
    _CienaCesDhcpv6LdraVsFailedValidationPktDrop_Type()
)
cienaCesDhcpv6LdraVsFailedValidationPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsFailedValidationPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsInvalidConfigPktDrop = _CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 7),
    _CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Type()
)
cienaCesDhcpv6LdraVsInvalidConfigPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsInvalidConfigPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsExceededHopCountPktDrop = _CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 8),
    _CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Type()
)
cienaCesDhcpv6LdraVsExceededHopCountPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsExceededHopCountPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsExceedMTUPktDrop = _CienaCesDhcpv6LdraVsExceedMTUPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 9),
    _CienaCesDhcpv6LdraVsExceedMTUPktDrop_Type()
)
cienaCesDhcpv6LdraVsExceedMTUPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsExceedMTUPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsNoTrustedServerPktDrop = _CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 10),
    _CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Type()
)
cienaCesDhcpv6LdraVsNoTrustedServerPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsNoTrustedServerPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsNoTrustedClientPktDrop = _CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 11),
    _CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Type()
)
cienaCesDhcpv6LdraVsNoTrustedClientPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsNoTrustedClientPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Type = Counter32
_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop = _CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 12),
    _CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Type()
)
cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop.setStatus("current")
_CienaCesDhcpv6LdraVsGeneralErrors_Type = Counter32
_CienaCesDhcpv6LdraVsGeneralErrors_Object = MibTableColumn
cienaCesDhcpv6LdraVsGeneralErrors = _CienaCesDhcpv6LdraVsGeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 13),
    _CienaCesDhcpv6LdraVsGeneralErrors_Type()
)
cienaCesDhcpv6LdraVsGeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsGeneralErrors.setStatus("current")


class _CienaCesDhcpv6LdraVsStatsClear_Type(CienaStatsClear):
    """Custom type cienaCesDhcpv6LdraVsStatsClear based on CienaStatsClear"""


_CienaCesDhcpv6LdraVsStatsClear_Object = MibTableColumn
cienaCesDhcpv6LdraVsStatsClear = _CienaCesDhcpv6LdraVsStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 10, 1, 14),
    _CienaCesDhcpv6LdraVsStatsClear_Type()
)
cienaCesDhcpv6LdraVsStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsStatsClear.setStatus("current")
_CienaCesDhcpv6LdraVsIntidStringTable_Object = MibTable
cienaCesDhcpv6LdraVsIntidStringTable = _CienaCesDhcpv6LdraVsIntidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsIntidStringTable.setStatus("current")
_CienaCesDhcpv6LdraVsIntidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraVsIntidStringEntry = _CienaCesDhcpv6LdraVsIntidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 11, 1)
)
cienaCesDhcpv6LdraVsIntidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsIntidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraVsIntidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraVsIntidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraVsIntidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraVsIntidString_Object = MibTableColumn
cienaCesDhcpv6LdraVsIntidString = _CienaCesDhcpv6LdraVsIntidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 11, 1, 1),
    _CienaCesDhcpv6LdraVsIntidString_Type()
)
cienaCesDhcpv6LdraVsIntidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsIntidString.setStatus("current")
_CienaCesDhcpv6LdraVsIntidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraVsIntidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraVsIntidStringRowStatus = _CienaCesDhcpv6LdraVsIntidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 11, 1, 2),
    _CienaCesDhcpv6LdraVsIntidStringRowStatus_Type()
)
cienaCesDhcpv6LdraVsIntidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsIntidStringRowStatus.setStatus("current")
_CienaCesDhcpv6LdraVsRidStringTable_Object = MibTable
cienaCesDhcpv6LdraVsRidStringTable = _CienaCesDhcpv6LdraVsRidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRidStringTable.setStatus("current")
_CienaCesDhcpv6LdraVsRidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraVsRidStringEntry = _CienaCesDhcpv6LdraVsRidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 12, 1)
)
cienaCesDhcpv6LdraVsRidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVlan"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraVsPort"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraVsRidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraVsRidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraVsRidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraVsRidString_Object = MibTableColumn
cienaCesDhcpv6LdraVsRidString = _CienaCesDhcpv6LdraVsRidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 12, 1, 1),
    _CienaCesDhcpv6LdraVsRidString_Type()
)
cienaCesDhcpv6LdraVsRidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRidString.setStatus("current")
_CienaCesDhcpv6LdraVsRidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraVsRidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraVsRidStringRowStatus = _CienaCesDhcpv6LdraVsRidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 12, 1, 2),
    _CienaCesDhcpv6LdraVsRidStringRowStatus_Type()
)
cienaCesDhcpv6LdraVsRidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraVsRidStringRowStatus.setStatus("current")
_CienaCesDhcpv6LdraMplsStateTable_Object = MibTable
cienaCesDhcpv6LdraMplsStateTable = _CienaCesDhcpv6LdraMplsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsStateTable.setStatus("current")
_CienaCesDhcpv6LdraMplsStateEntry_Object = MibTableRow
cienaCesDhcpv6LdraMplsStateEntry = _CienaCesDhcpv6LdraMplsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1)
)
cienaCesDhcpv6LdraMplsStateEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsId"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsStateEntry.setStatus("current")


class _CienaCesDhcpv6LdraMplsId_Type(Unsigned32):
    """Custom type cienaCesDhcpv6LdraMplsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1677215),
    )


_CienaCesDhcpv6LdraMplsId_Type.__name__ = "Unsigned32"
_CienaCesDhcpv6LdraMplsId_Object = MibTableColumn
cienaCesDhcpv6LdraMplsId = _CienaCesDhcpv6LdraMplsId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1, 1),
    _CienaCesDhcpv6LdraMplsId_Type()
)
cienaCesDhcpv6LdraMplsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsId.setStatus("current")


class _CienaCesDhcpv6LdraMplsName_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraMplsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesDhcpv6LdraMplsName_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraMplsName_Object = MibTableColumn
cienaCesDhcpv6LdraMplsName = _CienaCesDhcpv6LdraMplsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1, 2),
    _CienaCesDhcpv6LdraMplsName_Type()
)
cienaCesDhcpv6LdraMplsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsName.setStatus("current")
_CienaCesDhcpv6LdraMplsAdminState_Type = CienaGlobalState
_CienaCesDhcpv6LdraMplsAdminState_Object = MibTableColumn
cienaCesDhcpv6LdraMplsAdminState = _CienaCesDhcpv6LdraMplsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1, 3),
    _CienaCesDhcpv6LdraMplsAdminState_Type()
)
cienaCesDhcpv6LdraMplsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsAdminState.setStatus("current")
_CienaCesDhcpv6LdraMplsOperState_Type = CienaGlobalState
_CienaCesDhcpv6LdraMplsOperState_Object = MibTableColumn
cienaCesDhcpv6LdraMplsOperState = _CienaCesDhcpv6LdraMplsOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1, 4),
    _CienaCesDhcpv6LdraMplsOperState_Type()
)
cienaCesDhcpv6LdraMplsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsOperState.setStatus("current")
_CienaCesDhcpv6LdraMplsRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraMplsRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraMplsRowStatus = _CienaCesDhcpv6LdraMplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 13, 1, 5),
    _CienaCesDhcpv6LdraMplsRowStatus_Type()
)
cienaCesDhcpv6LdraMplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRowStatus.setStatus("current")
_CienaCesDhcpv6LdraMplsTrustTable_Object = MibTable
cienaCesDhcpv6LdraMplsTrustTable = _CienaCesDhcpv6LdraMplsTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsTrustTable.setStatus("current")
_CienaCesDhcpv6LdraMplsTrustEntry_Object = MibTableRow
cienaCesDhcpv6LdraMplsTrustEntry = _CienaCesDhcpv6LdraMplsTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14, 1)
)
cienaCesDhcpv6LdraMplsTrustEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsId"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsInterface"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsTrustEntry.setStatus("current")


class _CienaCesDhcpv6LdraMplsInterface_Type(Unsigned32):
    """Custom type cienaCesDhcpv6LdraMplsInterface based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesDhcpv6LdraMplsInterface_Type.__name__ = "Unsigned32"
_CienaCesDhcpv6LdraMplsInterface_Object = MibTableColumn
cienaCesDhcpv6LdraMplsInterface = _CienaCesDhcpv6LdraMplsInterface_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14, 1, 1),
    _CienaCesDhcpv6LdraMplsInterface_Type()
)
cienaCesDhcpv6LdraMplsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsInterface.setStatus("current")


class _CienaCesDhcpv6LdraMplsVcName_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraMplsVcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesDhcpv6LdraMplsVcName_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraMplsVcName_Object = MibTableColumn
cienaCesDhcpv6LdraMplsVcName = _CienaCesDhcpv6LdraMplsVcName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14, 1, 2),
    _CienaCesDhcpv6LdraMplsVcName_Type()
)
cienaCesDhcpv6LdraMplsVcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsVcName.setStatus("current")


class _CienaCesDhcpv6LdraMplsInterfaceState_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraMplsInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CienaCesDhcpv6LdraMplsInterfaceState_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraMplsInterfaceState_Object = MibTableColumn
cienaCesDhcpv6LdraMplsInterfaceState = _CienaCesDhcpv6LdraMplsInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14, 1, 3),
    _CienaCesDhcpv6LdraMplsInterfaceState_Type()
)
cienaCesDhcpv6LdraMplsInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsInterfaceState.setStatus("current")


class _CienaCesDhcpv6LdraMplsTrustMode_Type(Integer32):
    """Custom type cienaCesDhcpv6LdraMplsTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("clientTrust", 2),
          ("dualRoleTrust", 4),
          ("serverTrust", 3),
          ("unTrust", 5))
    )


_CienaCesDhcpv6LdraMplsTrustMode_Type.__name__ = "Integer32"
_CienaCesDhcpv6LdraMplsTrustMode_Object = MibTableColumn
cienaCesDhcpv6LdraMplsTrustMode = _CienaCesDhcpv6LdraMplsTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 14, 1, 4),
    _CienaCesDhcpv6LdraMplsTrustMode_Type()
)
cienaCesDhcpv6LdraMplsTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsTrustMode.setStatus("current")
_CienaCesDhcpv6LdraMplsStatsTable_Object = MibTable
cienaCesDhcpv6LdraMplsStatsTable = _CienaCesDhcpv6LdraMplsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsStatsTable.setStatus("current")
_CienaCesDhcpv6LdraMplsStatsEntry_Object = MibTableRow
cienaCesDhcpv6LdraMplsStatsEntry = _CienaCesDhcpv6LdraMplsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1)
)
cienaCesDhcpv6LdraMplsStatsEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsId"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsStatsEntry.setStatus("current")
_CienaCesDhcpv6LdraMplsPktsForRelay_Type = Counter32
_CienaCesDhcpv6LdraMplsPktsForRelay_Object = MibTableColumn
cienaCesDhcpv6LdraMplsPktsForRelay = _CienaCesDhcpv6LdraMplsPktsForRelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 1),
    _CienaCesDhcpv6LdraMplsPktsForRelay_Type()
)
cienaCesDhcpv6LdraMplsPktsForRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsPktsForRelay.setStatus("current")
_CienaCesDhcpv6LdraMplsRelayedClient_Type = Counter32
_CienaCesDhcpv6LdraMplsRelayedClient_Object = MibTableColumn
cienaCesDhcpv6LdraMplsRelayedClient = _CienaCesDhcpv6LdraMplsRelayedClient_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 2),
    _CienaCesDhcpv6LdraMplsRelayedClient_Type()
)
cienaCesDhcpv6LdraMplsRelayedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRelayedClient.setStatus("current")
_CienaCesDhcpv6LdraMplsRelayedServer_Type = Counter32
_CienaCesDhcpv6LdraMplsRelayedServer_Object = MibTableColumn
cienaCesDhcpv6LdraMplsRelayedServer = _CienaCesDhcpv6LdraMplsRelayedServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 3),
    _CienaCesDhcpv6LdraMplsRelayedServer_Type()
)
cienaCesDhcpv6LdraMplsRelayedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRelayedServer.setStatus("current")
_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Type = Counter32
_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx = _CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 4),
    _CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Type()
)
cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx.setStatus("current")
_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Type = Counter32
_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Object = MibTableColumn
cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx = _CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 5),
    _CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Type()
)
cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx.setStatus("current")
_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsFailedValidationPktDrop = _CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 6),
    _CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Type()
)
cienaCesDhcpv6LdraMplsFailedValidationPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsFailedValidationPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsInvalidConfigPktDrop = _CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 7),
    _CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Type()
)
cienaCesDhcpv6LdraMplsInvalidConfigPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsInvalidConfigPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsExceededHopCountPktDrop = _CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 8),
    _CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Type()
)
cienaCesDhcpv6LdraMplsExceededHopCountPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsExceededHopCountPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsExceedMTUPktDrop = _CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 9),
    _CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Type()
)
cienaCesDhcpv6LdraMplsExceedMTUPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsExceedMTUPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop = _CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 10),
    _CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Type()
)
cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop = _CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 11),
    _CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Type()
)
cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Type = Counter32
_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Object = MibTableColumn
cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop = _CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 12),
    _CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Type()
)
cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop.setStatus("current")
_CienaCesDhcpv6LdraMplsGeneralErrors_Type = Counter32
_CienaCesDhcpv6LdraMplsGeneralErrors_Object = MibTableColumn
cienaCesDhcpv6LdraMplsGeneralErrors = _CienaCesDhcpv6LdraMplsGeneralErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 13),
    _CienaCesDhcpv6LdraMplsGeneralErrors_Type()
)
cienaCesDhcpv6LdraMplsGeneralErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsGeneralErrors.setStatus("current")


class _CienaCesDhcpv6LdraMplsStatsClear_Type(CienaStatsClear):
    """Custom type cienaCesDhcpv6LdraMplsStatsClear based on CienaStatsClear"""


_CienaCesDhcpv6LdraMplsStatsClear_Object = MibTableColumn
cienaCesDhcpv6LdraMplsStatsClear = _CienaCesDhcpv6LdraMplsStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 15, 1, 14),
    _CienaCesDhcpv6LdraMplsStatsClear_Type()
)
cienaCesDhcpv6LdraMplsStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsStatsClear.setStatus("current")
_CienaCesDhcpv6LdraMplsIntidStringTable_Object = MibTable
cienaCesDhcpv6LdraMplsIntidStringTable = _CienaCesDhcpv6LdraMplsIntidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsIntidStringTable.setStatus("current")
_CienaCesDhcpv6LdraMplsIntidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraMplsIntidStringEntry = _CienaCesDhcpv6LdraMplsIntidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 16, 1)
)
cienaCesDhcpv6LdraMplsIntidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsId"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsInterface"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsIntidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraMplsIntidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraMplsIntidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraMplsIntidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraMplsIntidString_Object = MibTableColumn
cienaCesDhcpv6LdraMplsIntidString = _CienaCesDhcpv6LdraMplsIntidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 16, 1, 1),
    _CienaCesDhcpv6LdraMplsIntidString_Type()
)
cienaCesDhcpv6LdraMplsIntidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsIntidString.setStatus("current")
_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraMplsIntidStringRowStatus = _CienaCesDhcpv6LdraMplsIntidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 16, 1, 2),
    _CienaCesDhcpv6LdraMplsIntidStringRowStatus_Type()
)
cienaCesDhcpv6LdraMplsIntidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsIntidStringRowStatus.setStatus("current")
_CienaCesDhcpv6LdraMplsRidStringTable_Object = MibTable
cienaCesDhcpv6LdraMplsRidStringTable = _CienaCesDhcpv6LdraMplsRidStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRidStringTable.setStatus("current")
_CienaCesDhcpv6LdraMplsRidStringEntry_Object = MibTableRow
cienaCesDhcpv6LdraMplsRidStringEntry = _CienaCesDhcpv6LdraMplsRidStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 17, 1)
)
cienaCesDhcpv6LdraMplsRidStringEntry.setIndexNames(
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsId"),
    (0, "CIENA-CES-DHCPV6-CLIENT-MIB", "cienaCesDhcpv6LdraMplsInterface"),
)
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRidStringEntry.setStatus("current")


class _CienaCesDhcpv6LdraMplsRidString_Type(DisplayString):
    """Custom type cienaCesDhcpv6LdraMplsRidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CienaCesDhcpv6LdraMplsRidString_Type.__name__ = "DisplayString"
_CienaCesDhcpv6LdraMplsRidString_Object = MibTableColumn
cienaCesDhcpv6LdraMplsRidString = _CienaCesDhcpv6LdraMplsRidString_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 17, 1, 1),
    _CienaCesDhcpv6LdraMplsRidString_Type()
)
cienaCesDhcpv6LdraMplsRidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRidString.setStatus("current")
_CienaCesDhcpv6LdraMplsRidStringRowStatus_Type = RowStatus
_CienaCesDhcpv6LdraMplsRidStringRowStatus_Object = MibTableColumn
cienaCesDhcpv6LdraMplsRidStringRowStatus = _CienaCesDhcpv6LdraMplsRidStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 1, 2, 17, 1, 2),
    _CienaCesDhcpv6LdraMplsRidStringRowStatus_Type()
)
cienaCesDhcpv6LdraMplsRidStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesDhcpv6LdraMplsRidStringRowStatus.setStatus("current")
_CienaCesDhcpv6ClientMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBConformance = _CienaCesDhcpv6ClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 2)
)
_CienaCesDhcpv6ClientMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBCompliances = _CienaCesDhcpv6ClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 2, 1)
)
_CienaCesDhcpv6ClientMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBGroups = _CienaCesDhcpv6ClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 30, 2, 2)
)
_CienaCesDhcpv6ClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBNotificationPrefix = _CienaCesDhcpv6ClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 30)
)
_CienaCesDhcpv6ClientMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesDhcpv6ClientMIBNotifications = _CienaCesDhcpv6ClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 30, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-DHCPV6-CLIENT-MIB",
    **{"cienaCesDhcpv6ClientMIB": cienaCesDhcpv6ClientMIB,
       "cienaCesDhcpv6ClientMIBObjects": cienaCesDhcpv6ClientMIBObjects,
       "cienaCesDhcpv6Client": cienaCesDhcpv6Client,
       "cienaCesDhcpv6AdminState": cienaCesDhcpv6AdminState,
       "cienaCesDhcpv6IfName": cienaCesDhcpv6IfName,
       "cienaCesDhcpv6RapidCommitState": cienaCesDhcpv6RapidCommitState,
       "cienaCesDhcpv6PrefLifetimeReq": cienaCesDhcpv6PrefLifetimeReq,
       "cienaCesDhcpv6ValidLifetimeReq": cienaCesDhcpv6ValidLifetimeReq,
       "cienaCesDhcpv6ClientOptionTable": cienaCesDhcpv6ClientOptionTable,
       "cienaCesDhcpv6ClientOptionEntry": cienaCesDhcpv6ClientOptionEntry,
       "cienaCesDhcpv6OptionCodeIndex": cienaCesDhcpv6OptionCodeIndex,
       "cienaCesDhcpv6OptionDesc": cienaCesDhcpv6OptionDesc,
       "cienaCesDhcpv6OptionCode": cienaCesDhcpv6OptionCode,
       "cienaCesDhcpv6OptionState": cienaCesDhcpv6OptionState,
       "cienaCesDhcpv6ClientSessTable": cienaCesDhcpv6ClientSessTable,
       "cienaCesDhcpv6ClientSessEntry": cienaCesDhcpv6ClientSessEntry,
       "cienaCesDhcpv6ClientSessMgmtIntfIndex": cienaCesDhcpv6ClientSessMgmtIntfIndex,
       "cienaCesDhcpv6ClientSessState": cienaCesDhcpv6ClientSessState,
       "cienaCesDhcpv6ClientSessAutoConfigState": cienaCesDhcpv6ClientSessAutoConfigState,
       "cienaCesDhcpv6ClientSessUpTime": cienaCesDhcpv6ClientSessUpTime,
       "cienaCesDhcpv6ClientSessPrefLifetime": cienaCesDhcpv6ClientSessPrefLifetime,
       "cienaCesDhcpv6ClientSessValidLifetime": cienaCesDhcpv6ClientSessValidLifetime,
       "cienaCesDhcpv6ClientSessLeaseExpire": cienaCesDhcpv6ClientSessLeaseExpire,
       "cienaCesDhcpv6ClientSessClientId": cienaCesDhcpv6ClientSessClientId,
       "cienaCesDhcpv6ClientSessServerIpAddrType": cienaCesDhcpv6ClientSessServerIpAddrType,
       "cienaCesDhcpv6ClientSessServerIpAddr": cienaCesDhcpv6ClientSessServerIpAddr,
       "cienaCesDhcpv6ClientSessServerId": cienaCesDhcpv6ClientSessServerId,
       "cienaCesDhcpv6ClientSessT1Time": cienaCesDhcpv6ClientSessT1Time,
       "cienaCesDhcpv6ClientSessT2Time": cienaCesDhcpv6ClientSessT2Time,
       "cienaCesDhcpv6ClientSessStatsTable": cienaCesDhcpv6ClientSessStatsTable,
       "cienaCesDhcpv6ClientSessStatsEntry": cienaCesDhcpv6ClientSessStatsEntry,
       "cienaCesDhcpv6ClientSessStatsMgmtIntfIndex": cienaCesDhcpv6ClientSessStatsMgmtIntfIndex,
       "cienaCesDhcpv6ClientSessStatsClear": cienaCesDhcpv6ClientSessStatsClear,
       "cienaCesDhcpv6ClientSessStatsPktsRx": cienaCesDhcpv6ClientSessStatsPktsRx,
       "cienaCesDhcpv6ClientSessStatsReply": cienaCesDhcpv6ClientSessStatsReply,
       "cienaCesDhcpv6ClientSessStatsAdvert": cienaCesDhcpv6ClientSessStatsAdvert,
       "cienaCesDhcpv6ClientSessStatsRecfg": cienaCesDhcpv6ClientSessStatsRecfg,
       "cienaCesDhcpv6ClientSessStatsInvalid": cienaCesDhcpv6ClientSessStatsInvalid,
       "cienaCesDhcpv6ClientSessStatsPktsTx": cienaCesDhcpv6ClientSessStatsPktsTx,
       "cienaCesDhcpv6ClientSessStatsSolicit": cienaCesDhcpv6ClientSessStatsSolicit,
       "cienaCesDhcpv6ClientSessStatsRequest": cienaCesDhcpv6ClientSessStatsRequest,
       "cienaCesDhcpv6ClientSessStatsConfirm": cienaCesDhcpv6ClientSessStatsConfirm,
       "cienaCesDhcpv6ClientSessStatsRenew": cienaCesDhcpv6ClientSessStatsRenew,
       "cienaCesDhcpv6ClientSessStatsRebind": cienaCesDhcpv6ClientSessStatsRebind,
       "cienaCesDhcpv6ClientSessStatsInfoReq": cienaCesDhcpv6ClientSessStatsInfoReq,
       "cienaCesDhcpv6ClientSessStatsRelease": cienaCesDhcpv6ClientSessStatsRelease,
       "cienaCesDhcpv6ClientSessStatsDecline": cienaCesDhcpv6ClientSessStatsDecline,
       "cienaCesDhcpv6ClientSessStatsTxFail": cienaCesDhcpv6ClientSessStatsTxFail,
       "cienaCesDhcpv6RelayAgent": cienaCesDhcpv6RelayAgent,
       "cienaCesDhcpv6RelayAgentGlobalAttrs": cienaCesDhcpv6RelayAgentGlobalAttrs,
       "cienaCesDhcpv6LdraState": cienaCesDhcpv6LdraState,
       "cienaCesDhcpv6LdraInterfaceId": cienaCesDhcpv6LdraInterfaceId,
       "cienaCesDhcpv6LdraRemoteId": cienaCesDhcpv6LdraRemoteId,
       "cienaCesDhcpv6LdraRemoteIdOption": cienaCesDhcpv6LdraRemoteIdOption,
       "cienaCesDhcpv6LdraRemoteIdEnterpriseNo": cienaCesDhcpv6LdraRemoteIdEnterpriseNo,
       "cienaCesDhcpv6LdraForward": cienaCesDhcpv6LdraForward,
       "cienaCesDhcpv6LdraRelayed": cienaCesDhcpv6LdraRelayed,
       "cienaCesDhcpv6LdraDropped": cienaCesDhcpv6LdraDropped,
       "cienaCesDhcpv6LdraGlobalStatsClear": cienaCesDhcpv6LdraGlobalStatsClear,
       "cienaCesDhcpv6LdraNotForRelay": cienaCesDhcpv6LdraNotForRelay,
       "cienaCesDhcpv6LdraStateTable": cienaCesDhcpv6LdraStateTable,
       "cienaCesDhcpv6LdraStateEntry": cienaCesDhcpv6LdraStateEntry,
       "cienaCesDhcpv6LdraVlan": cienaCesDhcpv6LdraVlan,
       "cienaCesDhcpv6LdraAdminState": cienaCesDhcpv6LdraAdminState,
       "cienaCesDhcpv6LdraOperState": cienaCesDhcpv6LdraOperState,
       "cienaCesDhcpv6LdraRowStatus": cienaCesDhcpv6LdraRowStatus,
       "cienaCesDhcpv6LdraTrustTable": cienaCesDhcpv6LdraTrustTable,
       "cienaCesDhcpv6LdraTrustEntry": cienaCesDhcpv6LdraTrustEntry,
       "cienaCesDhcpv6LdraPort": cienaCesDhcpv6LdraPort,
       "cienaCesDhcpv6LdraTrustMode": cienaCesDhcpv6LdraTrustMode,
       "cienaCesDhcpv6LdraStatsTable": cienaCesDhcpv6LdraStatsTable,
       "cienaCesDhcpv6LdraStatsEntry": cienaCesDhcpv6LdraStatsEntry,
       "cienaCesDhcpv6LdraPktsForRelay": cienaCesDhcpv6LdraPktsForRelay,
       "cienaCesDhcpv6LdraRelayedClient": cienaCesDhcpv6LdraRelayedClient,
       "cienaCesDhcpv6LdraRelayedServer": cienaCesDhcpv6LdraRelayedServer,
       "cienaCesDhcpv6LdraUntrustedClientPortPktsRx": cienaCesDhcpv6LdraUntrustedClientPortPktsRx,
       "cienaCesDhcpv6LdraUntrustedServerPortPktsRx": cienaCesDhcpv6LdraUntrustedServerPortPktsRx,
       "cienaCesDhcpv6LdraFailedValidationPktDrop": cienaCesDhcpv6LdraFailedValidationPktDrop,
       "cienaCesDhcpv6LdraInvalidConfigPktDrop": cienaCesDhcpv6LdraInvalidConfigPktDrop,
       "cienaCesDhcpv6LdraExceededHopCountPktDrop": cienaCesDhcpv6LdraExceededHopCountPktDrop,
       "cienaCesDhcpv6LdraExceedMTUPktDrop": cienaCesDhcpv6LdraExceedMTUPktDrop,
       "cienaCesDhcpv6LdraNoTrustedServerPktDrop": cienaCesDhcpv6LdraNoTrustedServerPktDrop,
       "cienaCesDhcpv6LdraNoTrustedClientPktDrop": cienaCesDhcpv6LdraNoTrustedClientPktDrop,
       "cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop": cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop,
       "cienaCesDhcpv6LdraGeneralErrors": cienaCesDhcpv6LdraGeneralErrors,
       "cienaCesDhcpv6LdraStatsClear": cienaCesDhcpv6LdraStatsClear,
       "cienaCesDhcpv6LdraIntidStringTable": cienaCesDhcpv6LdraIntidStringTable,
       "cienaCesDhcpv6LdraIntidStringEntry": cienaCesDhcpv6LdraIntidStringEntry,
       "cienaCesDhcpv6LdraIntidStringPort": cienaCesDhcpv6LdraIntidStringPort,
       "cienaCesDhcpv6LdraIntidString": cienaCesDhcpv6LdraIntidString,
       "cienaCesDhcpv6LdraIntidStringRowStatus": cienaCesDhcpv6LdraIntidStringRowStatus,
       "cienaCesDhcpv6LdraRidStringTable": cienaCesDhcpv6LdraRidStringTable,
       "cienaCesDhcpv6LdraRidStringEntry": cienaCesDhcpv6LdraRidStringEntry,
       "cienaCesDhcpv6LdraRidStringPort": cienaCesDhcpv6LdraRidStringPort,
       "cienaCesDhcpv6LdraRidString": cienaCesDhcpv6LdraRidString,
       "cienaCesDhcpv6LdraRidStringRowStatus": cienaCesDhcpv6LdraRidStringRowStatus,
       "cienaCesDhcpv6LdraExtTrustTable": cienaCesDhcpv6LdraExtTrustTable,
       "cienaCesDhcpv6LdraExtTrustEntry": cienaCesDhcpv6LdraExtTrustEntry,
       "cienaCesDhcpv6LdraExtPortState": cienaCesDhcpv6LdraExtPortState,
       "cienaCesDhcpv6LdraExtTrustMode": cienaCesDhcpv6LdraExtTrustMode,
       "cienaCesDhcpv6LdraVsStateTable": cienaCesDhcpv6LdraVsStateTable,
       "cienaCesDhcpv6LdraVsStateEntry": cienaCesDhcpv6LdraVsStateEntry,
       "cienaCesDhcpv6LdraVsVlan": cienaCesDhcpv6LdraVsVlan,
       "cienaCesDhcpv6LdraVsName": cienaCesDhcpv6LdraVsName,
       "cienaCesDhcpv6LdraVsAdminState": cienaCesDhcpv6LdraVsAdminState,
       "cienaCesDhcpv6LdraVsOperState": cienaCesDhcpv6LdraVsOperState,
       "cienaCesDhcpv6LdraVsRowStatus": cienaCesDhcpv6LdraVsRowStatus,
       "cienaCesDhcpv6LdraVsTrustTable": cienaCesDhcpv6LdraVsTrustTable,
       "cienaCesDhcpv6LdraVsTrustEntry": cienaCesDhcpv6LdraVsTrustEntry,
       "cienaCesDhcpv6LdraVsPort": cienaCesDhcpv6LdraVsPort,
       "cienaCesDhcpv6LdraVsSubVlan": cienaCesDhcpv6LdraVsSubVlan,
       "cienaCesDhcpv6LdraVsPortState": cienaCesDhcpv6LdraVsPortState,
       "cienaCesDhcpv6LdraVsTrustMode": cienaCesDhcpv6LdraVsTrustMode,
       "cienaCesDhcpv6LdraVsStatsTable": cienaCesDhcpv6LdraVsStatsTable,
       "cienaCesDhcpv6LdraVsStatsEntry": cienaCesDhcpv6LdraVsStatsEntry,
       "cienaCesDhcpv6LdraVsPktsForRelay": cienaCesDhcpv6LdraVsPktsForRelay,
       "cienaCesDhcpv6LdraVsRelayedClient": cienaCesDhcpv6LdraVsRelayedClient,
       "cienaCesDhcpv6LdraVsRelayedServer": cienaCesDhcpv6LdraVsRelayedServer,
       "cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx": cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx,
       "cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx": cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx,
       "cienaCesDhcpv6LdraVsFailedValidationPktDrop": cienaCesDhcpv6LdraVsFailedValidationPktDrop,
       "cienaCesDhcpv6LdraVsInvalidConfigPktDrop": cienaCesDhcpv6LdraVsInvalidConfigPktDrop,
       "cienaCesDhcpv6LdraVsExceededHopCountPktDrop": cienaCesDhcpv6LdraVsExceededHopCountPktDrop,
       "cienaCesDhcpv6LdraVsExceedMTUPktDrop": cienaCesDhcpv6LdraVsExceedMTUPktDrop,
       "cienaCesDhcpv6LdraVsNoTrustedServerPktDrop": cienaCesDhcpv6LdraVsNoTrustedServerPktDrop,
       "cienaCesDhcpv6LdraVsNoTrustedClientPktDrop": cienaCesDhcpv6LdraVsNoTrustedClientPktDrop,
       "cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop": cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop,
       "cienaCesDhcpv6LdraVsGeneralErrors": cienaCesDhcpv6LdraVsGeneralErrors,
       "cienaCesDhcpv6LdraVsStatsClear": cienaCesDhcpv6LdraVsStatsClear,
       "cienaCesDhcpv6LdraVsIntidStringTable": cienaCesDhcpv6LdraVsIntidStringTable,
       "cienaCesDhcpv6LdraVsIntidStringEntry": cienaCesDhcpv6LdraVsIntidStringEntry,
       "cienaCesDhcpv6LdraVsIntidString": cienaCesDhcpv6LdraVsIntidString,
       "cienaCesDhcpv6LdraVsIntidStringRowStatus": cienaCesDhcpv6LdraVsIntidStringRowStatus,
       "cienaCesDhcpv6LdraVsRidStringTable": cienaCesDhcpv6LdraVsRidStringTable,
       "cienaCesDhcpv6LdraVsRidStringEntry": cienaCesDhcpv6LdraVsRidStringEntry,
       "cienaCesDhcpv6LdraVsRidString": cienaCesDhcpv6LdraVsRidString,
       "cienaCesDhcpv6LdraVsRidStringRowStatus": cienaCesDhcpv6LdraVsRidStringRowStatus,
       "cienaCesDhcpv6LdraMplsStateTable": cienaCesDhcpv6LdraMplsStateTable,
       "cienaCesDhcpv6LdraMplsStateEntry": cienaCesDhcpv6LdraMplsStateEntry,
       "cienaCesDhcpv6LdraMplsId": cienaCesDhcpv6LdraMplsId,
       "cienaCesDhcpv6LdraMplsName": cienaCesDhcpv6LdraMplsName,
       "cienaCesDhcpv6LdraMplsAdminState": cienaCesDhcpv6LdraMplsAdminState,
       "cienaCesDhcpv6LdraMplsOperState": cienaCesDhcpv6LdraMplsOperState,
       "cienaCesDhcpv6LdraMplsRowStatus": cienaCesDhcpv6LdraMplsRowStatus,
       "cienaCesDhcpv6LdraMplsTrustTable": cienaCesDhcpv6LdraMplsTrustTable,
       "cienaCesDhcpv6LdraMplsTrustEntry": cienaCesDhcpv6LdraMplsTrustEntry,
       "cienaCesDhcpv6LdraMplsInterface": cienaCesDhcpv6LdraMplsInterface,
       "cienaCesDhcpv6LdraMplsVcName": cienaCesDhcpv6LdraMplsVcName,
       "cienaCesDhcpv6LdraMplsInterfaceState": cienaCesDhcpv6LdraMplsInterfaceState,
       "cienaCesDhcpv6LdraMplsTrustMode": cienaCesDhcpv6LdraMplsTrustMode,
       "cienaCesDhcpv6LdraMplsStatsTable": cienaCesDhcpv6LdraMplsStatsTable,
       "cienaCesDhcpv6LdraMplsStatsEntry": cienaCesDhcpv6LdraMplsStatsEntry,
       "cienaCesDhcpv6LdraMplsPktsForRelay": cienaCesDhcpv6LdraMplsPktsForRelay,
       "cienaCesDhcpv6LdraMplsRelayedClient": cienaCesDhcpv6LdraMplsRelayedClient,
       "cienaCesDhcpv6LdraMplsRelayedServer": cienaCesDhcpv6LdraMplsRelayedServer,
       "cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx": cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx,
       "cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx": cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx,
       "cienaCesDhcpv6LdraMplsFailedValidationPktDrop": cienaCesDhcpv6LdraMplsFailedValidationPktDrop,
       "cienaCesDhcpv6LdraMplsInvalidConfigPktDrop": cienaCesDhcpv6LdraMplsInvalidConfigPktDrop,
       "cienaCesDhcpv6LdraMplsExceededHopCountPktDrop": cienaCesDhcpv6LdraMplsExceededHopCountPktDrop,
       "cienaCesDhcpv6LdraMplsExceedMTUPktDrop": cienaCesDhcpv6LdraMplsExceedMTUPktDrop,
       "cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop": cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop,
       "cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop": cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop,
       "cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop": cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop,
       "cienaCesDhcpv6LdraMplsGeneralErrors": cienaCesDhcpv6LdraMplsGeneralErrors,
       "cienaCesDhcpv6LdraMplsStatsClear": cienaCesDhcpv6LdraMplsStatsClear,
       "cienaCesDhcpv6LdraMplsIntidStringTable": cienaCesDhcpv6LdraMplsIntidStringTable,
       "cienaCesDhcpv6LdraMplsIntidStringEntry": cienaCesDhcpv6LdraMplsIntidStringEntry,
       "cienaCesDhcpv6LdraMplsIntidString": cienaCesDhcpv6LdraMplsIntidString,
       "cienaCesDhcpv6LdraMplsIntidStringRowStatus": cienaCesDhcpv6LdraMplsIntidStringRowStatus,
       "cienaCesDhcpv6LdraMplsRidStringTable": cienaCesDhcpv6LdraMplsRidStringTable,
       "cienaCesDhcpv6LdraMplsRidStringEntry": cienaCesDhcpv6LdraMplsRidStringEntry,
       "cienaCesDhcpv6LdraMplsRidString": cienaCesDhcpv6LdraMplsRidString,
       "cienaCesDhcpv6LdraMplsRidStringRowStatus": cienaCesDhcpv6LdraMplsRidStringRowStatus,
       "cienaCesDhcpv6ClientMIBConformance": cienaCesDhcpv6ClientMIBConformance,
       "cienaCesDhcpv6ClientMIBCompliances": cienaCesDhcpv6ClientMIBCompliances,
       "cienaCesDhcpv6ClientMIBGroups": cienaCesDhcpv6ClientMIBGroups,
       "cienaCesDhcpv6ClientMIBNotificationPrefix": cienaCesDhcpv6ClientMIBNotificationPrefix,
       "cienaCesDhcpv6ClientMIBNotifications": cienaCesDhcpv6ClientMIBNotifications}
)
