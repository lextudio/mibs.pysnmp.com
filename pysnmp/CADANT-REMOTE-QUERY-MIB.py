# SNMP MIB module (CADANT-REMOTE-QUERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-REMOTE-QUERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:11 2024
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

(cadIfCmtsCmStatusEntry,) = mibBuilder.importSymbols(
    "CADANT-CMTS-MAC-MIB",
    "cadIfCmtsCmStatusEntry")

(cadCmRemoteQuery,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadCmRemoteQuery")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadCmRemoteQueryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1)
)
cadCmRemoteQueryMib.setRevisions(
        ("2004-08-31 00:00",
         "2006-09-27 00:00",
         "2009-01-15 00:00",
         "2009-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadCmRemoteQueryPoller_ObjectIdentity = ObjectIdentity
cadCmRemoteQueryPoller = _CadCmRemoteQueryPoller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1)
)


class _CadCmRemoteQueryPollerEnable_Type(TruthValue):
    """Custom type cadCmRemoteQueryPollerEnable based on TruthValue"""


_CadCmRemoteQueryPollerEnable_Object = MibScalar
cadCmRemoteQueryPollerEnable = _CadCmRemoteQueryPollerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 1),
    _CadCmRemoteQueryPollerEnable_Type()
)
cadCmRemoteQueryPollerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerEnable.setStatus("current")


class _CadCmRemoteQueryPollerInterval_Type(Unsigned32):
    """Custom type cadCmRemoteQueryPollerInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_CadCmRemoteQueryPollerInterval_Type.__name__ = "Unsigned32"
_CadCmRemoteQueryPollerInterval_Object = MibScalar
cadCmRemoteQueryPollerInterval = _CadCmRemoteQueryPollerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 2),
    _CadCmRemoteQueryPollerInterval_Type()
)
cadCmRemoteQueryPollerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerInterval.setUnits("seconds")
_CadCmRemoteQueryPollerStartTime_Type = Unsigned32
_CadCmRemoteQueryPollerStartTime_Object = MibScalar
cadCmRemoteQueryPollerStartTime = _CadCmRemoteQueryPollerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 3),
    _CadCmRemoteQueryPollerStartTime_Type()
)
cadCmRemoteQueryPollerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerStartTime.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerStartTime.setUnits("seconds")
_CadCmRemoteQueryPollerStopTime_Type = Unsigned32
_CadCmRemoteQueryPollerStopTime_Object = MibScalar
cadCmRemoteQueryPollerStopTime = _CadCmRemoteQueryPollerStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 4),
    _CadCmRemoteQueryPollerStopTime_Type()
)
cadCmRemoteQueryPollerStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerStopTime.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerStopTime.setUnits("seconds")


class _CadCmRemoteQueryPollerCommunity_Type(OctetString):
    """Custom type cadCmRemoteQueryPollerCommunity based on OctetString"""
    defaultValue = OctetString("public")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadCmRemoteQueryPollerCommunity_Type.__name__ = "OctetString"
_CadCmRemoteQueryPollerCommunity_Object = MibScalar
cadCmRemoteQueryPollerCommunity = _CadCmRemoteQueryPollerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 5),
    _CadCmRemoteQueryPollerCommunity_Type()
)
cadCmRemoteQueryPollerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerCommunity.setStatus("current")


class _CadCmRemoteQueryMacAddress_Type(MacAddress):
    """Custom type cadCmRemoteQueryMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_CadCmRemoteQueryMacAddress_Object = MibScalar
cadCmRemoteQueryMacAddress = _CadCmRemoteQueryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 6),
    _CadCmRemoteQueryMacAddress_Type()
)
cadCmRemoteQueryMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmRemoteQueryMacAddress.setStatus("current")


class _CadCmRemoteQuerySourceIpAddrType_Type(InetAddressType):
    """Custom type cadCmRemoteQuerySourceIpAddrType based on InetAddressType"""


_CadCmRemoteQuerySourceIpAddrType_Object = MibScalar
cadCmRemoteQuerySourceIpAddrType = _CadCmRemoteQuerySourceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 7),
    _CadCmRemoteQuerySourceIpAddrType_Type()
)
cadCmRemoteQuerySourceIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySourceIpAddrType.setStatus("current")


class _CadCmRemoteQuerySourceIpAddr_Type(InetAddress):
    """Custom type cadCmRemoteQuerySourceIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_CadCmRemoteQuerySourceIpAddr_Object = MibScalar
cadCmRemoteQuerySourceIpAddr = _CadCmRemoteQuerySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 1, 8),
    _CadCmRemoteQuerySourceIpAddr_Type()
)
cadCmRemoteQuerySourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySourceIpAddr.setStatus("current")
_CadCmRemoteQueryStatusTable_Object = MibTable
cadCmRemoteQueryStatusTable = _CadCmRemoteQueryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2)
)
if mibBuilder.loadTexts:
    cadCmRemoteQueryStatusTable.setStatus("current")
_CadCmRemoteQueryStatusEntry_Object = MibTableRow
cadCmRemoteQueryStatusEntry = _CadCmRemoteQueryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cadCmRemoteQueryStatusEntry.setStatus("current")
_CadCmRemoteQueryPollTime_Type = Unsigned32
_CadCmRemoteQueryPollTime_Object = MibTableColumn
cadCmRemoteQueryPollTime = _CadCmRemoteQueryPollTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 1),
    _CadCmRemoteQueryPollTime_Type()
)
cadCmRemoteQueryPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollTime.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollTime.setUnits("seconds")
_CadCmRemoteQueryDownChannelPower_Type = TenthdBmV
_CadCmRemoteQueryDownChannelPower_Object = MibTableColumn
cadCmRemoteQueryDownChannelPower = _CadCmRemoteQueryDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 2),
    _CadCmRemoteQueryDownChannelPower_Type()
)
cadCmRemoteQueryDownChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryDownChannelPower.setUnits("dBmV")
_CadCmRemoteQueryStatusTxPower_Type = TenthdBmV
_CadCmRemoteQueryStatusTxPower_Object = MibTableColumn
cadCmRemoteQueryStatusTxPower = _CadCmRemoteQueryStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 3),
    _CadCmRemoteQueryStatusTxPower_Type()
)
cadCmRemoteQueryStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryStatusTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQueryStatusTxPower.setUnits("dBmV")
_CadCmRemoteQueryUpChnlTxTimingOffset_Type = Unsigned32
_CadCmRemoteQueryUpChnlTxTimingOffset_Object = MibTableColumn
cadCmRemoteQueryUpChnlTxTimingOffset = _CadCmRemoteQueryUpChnlTxTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 4),
    _CadCmRemoteQueryUpChnlTxTimingOffset_Type()
)
cadCmRemoteQueryUpChnlTxTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQueryUpChnlTxTimingOffset.setStatus("current")
_CadCmRemoteQuerySigQSignalNoise_Type = TenthdB
_CadCmRemoteQuerySigQSignalNoise_Object = MibTableColumn
cadCmRemoteQuerySigQSignalNoise = _CadCmRemoteQuerySigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 5),
    _CadCmRemoteQuerySigQSignalNoise_Type()
)
cadCmRemoteQuerySigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySigQSignalNoise.setUnits("dB")


class _CadCmRemoteQuerySigQMicroreflections_Type(Integer32):
    """Custom type cadCmRemoteQuerySigQMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadCmRemoteQuerySigQMicroreflections_Type.__name__ = "Integer32"
_CadCmRemoteQuerySigQMicroreflections_Object = MibTableColumn
cadCmRemoteQuerySigQMicroreflections = _CadCmRemoteQuerySigQMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 6),
    _CadCmRemoteQuerySigQMicroreflections_Type()
)
cadCmRemoteQuerySigQMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySigQMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySigQMicroreflections.setUnits("dBc")


class _CadCmRemoteQuerySysDescr_Type(DisplayString):
    """Custom type cadCmRemoteQuerySysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadCmRemoteQuerySysDescr_Type.__name__ = "DisplayString"
_CadCmRemoteQuerySysDescr_Object = MibTableColumn
cadCmRemoteQuerySysDescr = _CadCmRemoteQuerySysDescr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 2, 1, 7),
    _CadCmRemoteQuerySysDescr_Type()
)
cadCmRemoteQuerySysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmRemoteQuerySysDescr.setStatus("current")
_CadCmRemoteQueryConformance_ObjectIdentity = ObjectIdentity
cadCmRemoteQueryConformance = _CadCmRemoteQueryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3)
)
_CadCmRemoteQueryDocsRemoteQueryCompliances_ObjectIdentity = ObjectIdentity
cadCmRemoteQueryDocsRemoteQueryCompliances = _CadCmRemoteQueryDocsRemoteQueryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3, 1)
)
_CadCmRemoteQueryDocsRemoteQueryGroups_ObjectIdentity = ObjectIdentity
cadCmRemoteQueryDocsRemoteQueryGroups = _CadCmRemoteQueryDocsRemoteQueryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3, 2)
)
cadIfCmtsCmStatusEntry.registerAugmentions(
    ("CADANT-REMOTE-QUERY-MIB",
     "cadCmRemoteQueryStatusEntry")
)
cadCmRemoteQueryStatusEntry.setIndexNames(*cadIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

cadCmRemoteQueryPollerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3, 2, 1)
)
cadCmRemoteQueryPollerGroup.setObjects(
      *(("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollerEnable"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollerInterval"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollerStartTime"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollerStopTime"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollerCommunity"))
)
if mibBuilder.loadTexts:
    cadCmRemoteQueryPollerGroup.setStatus("current")

cadCmRemoteQueryStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3, 2, 2)
)
cadCmRemoteQueryStatusGroup.setObjects(
      *(("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryPollTime"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryDownChannelPower"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryStatusTxPower"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQueryUpChnlTxTimingOffset"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQuerySigQSignalNoise"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQuerySigQMicroreflections"),
        ("CADANT-REMOTE-QUERY-MIB", "cadCmRemoteQuerySysDescr"))
)
if mibBuilder.loadTexts:
    cadCmRemoteQueryStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadCmRemoteQueryDocsRemoteQueryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cadCmRemoteQueryDocsRemoteQueryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-REMOTE-QUERY-MIB",
    **{"cadCmRemoteQueryMib": cadCmRemoteQueryMib,
       "cadCmRemoteQueryPoller": cadCmRemoteQueryPoller,
       "cadCmRemoteQueryPollerEnable": cadCmRemoteQueryPollerEnable,
       "cadCmRemoteQueryPollerInterval": cadCmRemoteQueryPollerInterval,
       "cadCmRemoteQueryPollerStartTime": cadCmRemoteQueryPollerStartTime,
       "cadCmRemoteQueryPollerStopTime": cadCmRemoteQueryPollerStopTime,
       "cadCmRemoteQueryPollerCommunity": cadCmRemoteQueryPollerCommunity,
       "cadCmRemoteQueryMacAddress": cadCmRemoteQueryMacAddress,
       "cadCmRemoteQuerySourceIpAddrType": cadCmRemoteQuerySourceIpAddrType,
       "cadCmRemoteQuerySourceIpAddr": cadCmRemoteQuerySourceIpAddr,
       "cadCmRemoteQueryStatusTable": cadCmRemoteQueryStatusTable,
       "cadCmRemoteQueryStatusEntry": cadCmRemoteQueryStatusEntry,
       "cadCmRemoteQueryPollTime": cadCmRemoteQueryPollTime,
       "cadCmRemoteQueryDownChannelPower": cadCmRemoteQueryDownChannelPower,
       "cadCmRemoteQueryStatusTxPower": cadCmRemoteQueryStatusTxPower,
       "cadCmRemoteQueryUpChnlTxTimingOffset": cadCmRemoteQueryUpChnlTxTimingOffset,
       "cadCmRemoteQuerySigQSignalNoise": cadCmRemoteQuerySigQSignalNoise,
       "cadCmRemoteQuerySigQMicroreflections": cadCmRemoteQuerySigQMicroreflections,
       "cadCmRemoteQuerySysDescr": cadCmRemoteQuerySysDescr,
       "cadCmRemoteQueryConformance": cadCmRemoteQueryConformance,
       "cadCmRemoteQueryDocsRemoteQueryCompliances": cadCmRemoteQueryDocsRemoteQueryCompliances,
       "cadCmRemoteQueryDocsRemoteQueryCompliance": cadCmRemoteQueryDocsRemoteQueryCompliance,
       "cadCmRemoteQueryDocsRemoteQueryGroups": cadCmRemoteQueryDocsRemoteQueryGroups,
       "cadCmRemoteQueryPollerGroup": cadCmRemoteQueryPollerGroup,
       "cadCmRemoteQueryStatusGroup": cadCmRemoteQueryStatusGroup}
)
