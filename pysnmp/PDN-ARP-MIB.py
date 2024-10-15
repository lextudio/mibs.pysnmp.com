# SNMP MIB module (PDN-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipNetToMediaEntry,
 ipNetToMediaIfIndex,
 ipNetToMediaPhysAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry",
    "ipNetToMediaIfIndex",
    "ipNetToMediaPhysAddress")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,
 VnidRange) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState",
    "VnidRange")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pdn_arp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27)
)
pdn_arp.setRevisions(
        ("2005-07-19 00:00",
         "2002-08-02 00:00",
         "2002-04-18 00:00",
         "2001-12-31 00:00",
         "2001-01-15 00:00",
         "2000-05-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnNetToMediaGenericMIBObjects_ObjectIdentity = ObjectIdentity
pdnNetToMediaGenericMIBObjects = _PdnNetToMediaGenericMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1)
)
_PdnNetToMediaParams_ObjectIdentity = ObjectIdentity
pdnNetToMediaParams = _PdnNetToMediaParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1)
)


class _PdnNetToMediaParamsCompEntryTimeout_Type(Integer32):
    """Custom type pdnNetToMediaParamsCompEntryTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnNetToMediaParamsCompEntryTimeout_Type.__name__ = "Integer32"
_PdnNetToMediaParamsCompEntryTimeout_Object = MibScalar
pdnNetToMediaParamsCompEntryTimeout = _PdnNetToMediaParamsCompEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 1),
    _PdnNetToMediaParamsCompEntryTimeout_Type()
)
pdnNetToMediaParamsCompEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsCompEntryTimeout.setStatus("current")


class _PdnNetToMediaParamsIncompEntryTimeout_Type(Integer32):
    """Custom type pdnNetToMediaParamsIncompEntryTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnNetToMediaParamsIncompEntryTimeout_Type.__name__ = "Integer32"
_PdnNetToMediaParamsIncompEntryTimeout_Object = MibScalar
pdnNetToMediaParamsIncompEntryTimeout = _PdnNetToMediaParamsIncompEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 2),
    _PdnNetToMediaParamsIncompEntryTimeout_Type()
)
pdnNetToMediaParamsIncompEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsIncompEntryTimeout.setStatus("current")


class _PdnNetToMediaParamsDefRouteEntryTimeout_Type(Integer32):
    """Custom type pdnNetToMediaParamsDefRouteEntryTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnNetToMediaParamsDefRouteEntryTimeout_Type.__name__ = "Integer32"
_PdnNetToMediaParamsDefRouteEntryTimeout_Object = MibScalar
pdnNetToMediaParamsDefRouteEntryTimeout = _PdnNetToMediaParamsDefRouteEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 3),
    _PdnNetToMediaParamsDefRouteEntryTimeout_Type()
)
pdnNetToMediaParamsDefRouteEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsDefRouteEntryTimeout.setStatus("current")
_PdnNetToMediaParamsAprTable_Object = MibTable
pdnNetToMediaParamsAprTable = _PdnNetToMediaParamsAprTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprTable.setStatus("current")
_PdnNetToMediaParamsAprEntry_Object = MibTableRow
pdnNetToMediaParamsAprEntry = _PdnNetToMediaParamsAprEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4, 1)
)
pdnNetToMediaParamsAprEntry.setIndexNames(
    (0, "PDN-ARP-MIB", "pdnNetToMediaParamsAprIpAddr"),
)
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprEntry.setStatus("current")
_PdnNetToMediaParamsAprIpAddr_Type = IpAddress
_PdnNetToMediaParamsAprIpAddr_Object = MibTableColumn
pdnNetToMediaParamsAprIpAddr = _PdnNetToMediaParamsAprIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4, 1, 1),
    _PdnNetToMediaParamsAprIpAddr_Type()
)
pdnNetToMediaParamsAprIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprIpAddr.setStatus("current")
_PdnNetToMediaParamsAprRowStatus_Type = RowStatus
_PdnNetToMediaParamsAprRowStatus_Object = MibTableColumn
pdnNetToMediaParamsAprRowStatus = _PdnNetToMediaParamsAprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4, 1, 2),
    _PdnNetToMediaParamsAprRowStatus_Type()
)
pdnNetToMediaParamsAprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprRowStatus.setStatus("current")


class _PdnNetToMediaParamsAprReqPeriod_Type(Unsigned32):
    """Custom type pdnNetToMediaParamsAprReqPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_PdnNetToMediaParamsAprReqPeriod_Type.__name__ = "Unsigned32"
_PdnNetToMediaParamsAprReqPeriod_Object = MibTableColumn
pdnNetToMediaParamsAprReqPeriod = _PdnNetToMediaParamsAprReqPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4, 1, 3),
    _PdnNetToMediaParamsAprReqPeriod_Type()
)
pdnNetToMediaParamsAprReqPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprReqPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprReqPeriod.setUnits("minutes")
_PdnNetToMediaParamsAprTimeToNext_Type = Unsigned32
_PdnNetToMediaParamsAprTimeToNext_Object = MibTableColumn
pdnNetToMediaParamsAprTimeToNext = _PdnNetToMediaParamsAprTimeToNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 1, 4, 1, 4),
    _PdnNetToMediaParamsAprTimeToNext_Type()
)
pdnNetToMediaParamsAprTimeToNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprTimeToNext.setStatus("current")
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprTimeToNext.setUnits("minutes")
_PdnNetToMediaConfig_ObjectIdentity = ObjectIdentity
pdnNetToMediaConfig = _PdnNetToMediaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2)
)
_PdnNetToMediaConfigTable_Object = MibTable
pdnNetToMediaConfigTable = _PdnNetToMediaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnNetToMediaConfigTable.setStatus("current")
_PdnNetToMediaConfigEntry_Object = MibTableRow
pdnNetToMediaConfigEntry = _PdnNetToMediaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1)
)
pdnNetToMediaConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ARP-MIB", "pdnNetToMediaConfigIpAddr"),
)
if mibBuilder.loadTexts:
    pdnNetToMediaConfigEntry.setStatus("current")
_PdnNetToMediaConfigIpAddr_Type = IpAddress
_PdnNetToMediaConfigIpAddr_Object = MibTableColumn
pdnNetToMediaConfigIpAddr = _PdnNetToMediaConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 1),
    _PdnNetToMediaConfigIpAddr_Type()
)
pdnNetToMediaConfigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigIpAddr.setStatus("current")
_PdnNetToMediaConfigMacAddr_Type = MacAddress
_PdnNetToMediaConfigMacAddr_Object = MibTableColumn
pdnNetToMediaConfigMacAddr = _PdnNetToMediaConfigMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 2),
    _PdnNetToMediaConfigMacAddr_Type()
)
pdnNetToMediaConfigMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigMacAddr.setStatus("current")


class _PdnNetToMediaConfigMin_Type(Integer32):
    """Custom type pdnNetToMediaConfigMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnNetToMediaConfigMin_Type.__name__ = "Integer32"
_PdnNetToMediaConfigMin_Object = MibTableColumn
pdnNetToMediaConfigMin = _PdnNetToMediaConfigMin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 3),
    _PdnNetToMediaConfigMin_Type()
)
pdnNetToMediaConfigMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigMin.setStatus("current")
_PdnNetToMediaConfigFlags_Type = Integer32
_PdnNetToMediaConfigFlags_Object = MibTableColumn
pdnNetToMediaConfigFlags = _PdnNetToMediaConfigFlags_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 4),
    _PdnNetToMediaConfigFlags_Type()
)
pdnNetToMediaConfigFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigFlags.setStatus("current")
_PdnNetToMediaConfigTrailer_Type = SwitchState
_PdnNetToMediaConfigTrailer_Object = MibTableColumn
pdnNetToMediaConfigTrailer = _PdnNetToMediaConfigTrailer_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 5),
    _PdnNetToMediaConfigTrailer_Type()
)
pdnNetToMediaConfigTrailer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigTrailer.setStatus("current")
_PdnNetToMediaConfigPerm_Type = TruthValue
_PdnNetToMediaConfigPerm_Object = MibTableColumn
pdnNetToMediaConfigPerm = _PdnNetToMediaConfigPerm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 6),
    _PdnNetToMediaConfigPerm_Type()
)
pdnNetToMediaConfigPerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigPerm.setStatus("current")
_PdnNetToMediaConfigRowStatus_Type = RowStatus
_PdnNetToMediaConfigRowStatus_Object = MibTableColumn
pdnNetToMediaConfigRowStatus = _PdnNetToMediaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 1, 1, 7),
    _PdnNetToMediaConfigRowStatus_Type()
)
pdnNetToMediaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaConfigRowStatus.setStatus("current")


class _PdnNetToMediaClearAllArp_Type(Integer32):
    """Custom type pdnNetToMediaClearAllArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noop", 1))
    )


_PdnNetToMediaClearAllArp_Type.__name__ = "Integer32"
_PdnNetToMediaClearAllArp_Object = MibScalar
pdnNetToMediaClearAllArp = _PdnNetToMediaClearAllArp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 2),
    _PdnNetToMediaClearAllArp_Type()
)
pdnNetToMediaClearAllArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnNetToMediaClearAllArp.setStatus("current")
_PdnNetToMediaProxyArpTable_Object = MibTable
pdnNetToMediaProxyArpTable = _PdnNetToMediaProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pdnNetToMediaProxyArpTable.setStatus("current")
_PdnNetToMediaProxyArpEntry_Object = MibTableRow
pdnNetToMediaProxyArpEntry = _PdnNetToMediaProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 3, 1)
)
pdnNetToMediaProxyArpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnNetToMediaProxyArpEntry.setStatus("current")


class _PdnNetToMediaProxyArpStatus_Type(Integer32):
    """Custom type pdnNetToMediaProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PdnNetToMediaProxyArpStatus_Type.__name__ = "Integer32"
_PdnNetToMediaProxyArpStatus_Object = MibTableColumn
pdnNetToMediaProxyArpStatus = _PdnNetToMediaProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 3, 1, 1),
    _PdnNetToMediaProxyArpStatus_Type()
)
pdnNetToMediaProxyArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetToMediaProxyArpStatus.setStatus("current")
_IpNetToMediaConfig_ObjectIdentity = ObjectIdentity
ipNetToMediaConfig = _IpNetToMediaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4)
)


class _IpNetToMediaForwardingMode_Type(Integer32):
    """Custom type ipNetToMediaForwardingMode based on Integer32"""
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
        *(("basic", 1),
          ("mux", 2),
          ("sms", 3),
          ("ult", 4),
          ("vlan", 5))
    )


_IpNetToMediaForwardingMode_Type.__name__ = "Integer32"
_IpNetToMediaForwardingMode_Object = MibScalar
ipNetToMediaForwardingMode = _IpNetToMediaForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 1),
    _IpNetToMediaForwardingMode_Type()
)
ipNetToMediaForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaForwardingMode.setStatus("current")
_IpNetToMediaDefaultNHR_Type = IpAddress
_IpNetToMediaDefaultNHR_Object = MibScalar
ipNetToMediaDefaultNHR = _IpNetToMediaDefaultNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 2),
    _IpNetToMediaDefaultNHR_Type()
)
ipNetToMediaDefaultNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaDefaultNHR.setStatus("current")
_IpNetToMediaExtTable_Object = MibTable
ipNetToMediaExtTable = _IpNetToMediaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    ipNetToMediaExtTable.setStatus("current")
_IpNetToMediaExtEntry_Object = MibTableRow
ipNetToMediaExtEntry = _IpNetToMediaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ipNetToMediaExtEntry.setStatus("current")
_IpNetToMediaNHR_Type = IpAddress
_IpNetToMediaNHR_Object = MibTableColumn
ipNetToMediaNHR = _IpNetToMediaNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 3, 1, 1),
    _IpNetToMediaNHR_Type()
)
ipNetToMediaNHR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaNHR.setStatus("current")
_IpNetToMediaLimitTable_Object = MibTable
ipNetToMediaLimitTable = _IpNetToMediaLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    ipNetToMediaLimitTable.setStatus("current")
_IpNetToMediaLimitEntry_Object = MibTableRow
ipNetToMediaLimitEntry = _IpNetToMediaLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 4, 1)
)
ipNetToMediaLimitEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
)
if mibBuilder.loadTexts:
    ipNetToMediaLimitEntry.setStatus("current")
_IpNetToMediaLimitEnabled_Type = TruthValue
_IpNetToMediaLimitEnabled_Object = MibTableColumn
ipNetToMediaLimitEnabled = _IpNetToMediaLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 4, 1, 1),
    _IpNetToMediaLimitEnabled_Type()
)
ipNetToMediaLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaLimitEnabled.setStatus("current")


class _IpNetToMediaMaxIPAddresses_Type(Integer32):
    """Custom type ipNetToMediaMaxIPAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_IpNetToMediaMaxIPAddresses_Type.__name__ = "Integer32"
_IpNetToMediaMaxIPAddresses_Object = MibTableColumn
ipNetToMediaMaxIPAddresses = _IpNetToMediaMaxIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 2, 4, 4, 1, 2),
    _IpNetToMediaMaxIPAddresses_Type()
)
ipNetToMediaMaxIPAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaMaxIPAddresses.setStatus("current")
_PdnNetTo8023MediaConfig_ObjectIdentity = ObjectIdentity
pdnNetTo8023MediaConfig = _PdnNetTo8023MediaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3)
)
_PdnNetTo8023MediaConfigTable_Object = MibTable
pdnNetTo8023MediaConfigTable = _PdnNetTo8023MediaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigTable.setStatus("current")
_PdnNetTo8023MediaConfigEntry_Object = MibTableRow
pdnNetTo8023MediaConfigEntry = _PdnNetTo8023MediaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1)
)
pdnNetTo8023MediaConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ARP-MIB", "pdnNetTo8023MediaConfigIpAddr"),
    (0, "PDN-ARP-MIB", "pdnNetTo8023MediaConfigVnidId"),
)
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigEntry.setStatus("current")
_PdnNetTo8023MediaConfigIpAddr_Type = IpAddress
_PdnNetTo8023MediaConfigIpAddr_Object = MibTableColumn
pdnNetTo8023MediaConfigIpAddr = _PdnNetTo8023MediaConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 1),
    _PdnNetTo8023MediaConfigIpAddr_Type()
)
pdnNetTo8023MediaConfigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigIpAddr.setStatus("current")
_PdnNetTo8023MediaConfigVnidId_Type = VnidRange
_PdnNetTo8023MediaConfigVnidId_Object = MibTableColumn
pdnNetTo8023MediaConfigVnidId = _PdnNetTo8023MediaConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 2),
    _PdnNetTo8023MediaConfigVnidId_Type()
)
pdnNetTo8023MediaConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigVnidId.setStatus("current")
_PdnNetTo8023MediaConfigMacAddr_Type = MacAddress
_PdnNetTo8023MediaConfigMacAddr_Object = MibTableColumn
pdnNetTo8023MediaConfigMacAddr = _PdnNetTo8023MediaConfigMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 3),
    _PdnNetTo8023MediaConfigMacAddr_Type()
)
pdnNetTo8023MediaConfigMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigMacAddr.setStatus("current")


class _PdnNetTo8023MediaConfigMin_Type(Integer32):
    """Custom type pdnNetTo8023MediaConfigMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnNetTo8023MediaConfigMin_Type.__name__ = "Integer32"
_PdnNetTo8023MediaConfigMin_Object = MibTableColumn
pdnNetTo8023MediaConfigMin = _PdnNetTo8023MediaConfigMin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 4),
    _PdnNetTo8023MediaConfigMin_Type()
)
pdnNetTo8023MediaConfigMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigMin.setStatus("current")
_PdnNetTo8023MediaConfigFlags_Type = Integer32
_PdnNetTo8023MediaConfigFlags_Object = MibTableColumn
pdnNetTo8023MediaConfigFlags = _PdnNetTo8023MediaConfigFlags_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 5),
    _PdnNetTo8023MediaConfigFlags_Type()
)
pdnNetTo8023MediaConfigFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigFlags.setStatus("current")
_PdnNetTo8023MediaConfigTrailer_Type = SwitchState
_PdnNetTo8023MediaConfigTrailer_Object = MibTableColumn
pdnNetTo8023MediaConfigTrailer = _PdnNetTo8023MediaConfigTrailer_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 6),
    _PdnNetTo8023MediaConfigTrailer_Type()
)
pdnNetTo8023MediaConfigTrailer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigTrailer.setStatus("current")
_PdnNetTo8023MediaConfigPerm_Type = TruthValue
_PdnNetTo8023MediaConfigPerm_Object = MibTableColumn
pdnNetTo8023MediaConfigPerm = _PdnNetTo8023MediaConfigPerm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 7),
    _PdnNetTo8023MediaConfigPerm_Type()
)
pdnNetTo8023MediaConfigPerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigPerm.setStatus("current")
_PdnNetTo8023MediaConfigRowStatus_Type = RowStatus
_PdnNetTo8023MediaConfigRowStatus_Object = MibTableColumn
pdnNetTo8023MediaConfigRowStatus = _PdnNetTo8023MediaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 3, 1, 1, 8),
    _PdnNetTo8023MediaConfigRowStatus_Type()
)
pdnNetTo8023MediaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnNetTo8023MediaConfigRowStatus.setStatus("current")
_PdnNetToMediaConformance_ObjectIdentity = ObjectIdentity
pdnNetToMediaConformance = _PdnNetToMediaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4)
)
_PdnNetToMediaCompliances_ObjectIdentity = ObjectIdentity
pdnNetToMediaCompliances = _PdnNetToMediaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 1)
)
_PdnNetToMediaGroups_ObjectIdentity = ObjectIdentity
pdnNetToMediaGroups = _PdnNetToMediaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2)
)
_PdnNetToMediaObjGroups_ObjectIdentity = ObjectIdentity
pdnNetToMediaObjGroups = _PdnNetToMediaObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1)
)
_PdnNetToMediaNtfyGroups_ObjectIdentity = ObjectIdentity
pdnNetToMediaNtfyGroups = _PdnNetToMediaNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 2)
)
_PdnNetToMediaMIBTraps_ObjectIdentity = ObjectIdentity
pdnNetToMediaMIBTraps = _PdnNetToMediaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 2)
)
_PdnNetToMediaMIBNotifications_ObjectIdentity = ObjectIdentity
pdnNetToMediaMIBNotifications = _PdnNetToMediaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 2, 0)
)
ipNetToMediaEntry.registerAugmentions(
    ("PDN-ARP-MIB",
     "ipNetToMediaExtEntry")
)
ipNetToMediaExtEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())

# Managed Objects groups

pdnNetToMediaParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 1)
)
pdnNetToMediaParamsGroup.setObjects(
      *(("PDN-ARP-MIB", "pdnNetToMediaParamsCompEntryTimeout"),
        ("PDN-ARP-MIB", "pdnNetToMediaParamsIncompEntryTimeout"),
        ("PDN-ARP-MIB", "pdnNetToMediaParamsDefRouteEntryTimeout"))
)
if mibBuilder.loadTexts:
    pdnNetToMediaParamsGroup.setStatus("current")

pdnNetToMediaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 2)
)
pdnNetToMediaConfigGroup.setObjects(
      *(("PDN-ARP-MIB", "pdnNetToMediaConfigMacAddr"),
        ("PDN-ARP-MIB", "pdnNetToMediaConfigMin"),
        ("PDN-ARP-MIB", "pdnNetToMediaConfigFlags"),
        ("PDN-ARP-MIB", "pdnNetToMediaConfigTrailer"),
        ("PDN-ARP-MIB", "pdnNetToMediaConfigPerm"),
        ("PDN-ARP-MIB", "pdnNetToMediaConfigRowStatus"))
)
if mibBuilder.loadTexts:
    pdnNetToMediaConfigGroup.setStatus("current")

pdnNetToMedia8023ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 3)
)
pdnNetToMedia8023ConfigGroup.setObjects(
      *(("PDN-ARP-MIB", "pdnNetTo8023MediaConfigVnidId"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigMacAddr"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigMin"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigFlags"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigTrailer"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigPerm"),
        ("PDN-ARP-MIB", "pdnNetTo8023MediaConfigRowStatus"))
)
if mibBuilder.loadTexts:
    pdnNetToMedia8023ConfigGroup.setStatus("current")

pdnNetToMediaClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 4)
)
pdnNetToMediaClearGroup.setObjects(
    ("PDN-ARP-MIB", "pdnNetToMediaClearAllArp")
)
if mibBuilder.loadTexts:
    pdnNetToMediaClearGroup.setStatus("current")

pdnNetToMediaProxyArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 5)
)
pdnNetToMediaProxyArpGroup.setObjects(
    ("PDN-ARP-MIB", "pdnNetToMediaProxyArpStatus")
)
if mibBuilder.loadTexts:
    pdnNetToMediaProxyArpGroup.setStatus("current")

pdnNetToMediaConfigProxyArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 6)
)
pdnNetToMediaConfigProxyArpGroup.setObjects(
      *(("PDN-ARP-MIB", "ipNetToMediaForwardingMode"),
        ("PDN-ARP-MIB", "ipNetToMediaDefaultNHR"))
)
if mibBuilder.loadTexts:
    pdnNetToMediaConfigProxyArpGroup.setStatus("current")

pdnNetToMediaExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 7)
)
pdnNetToMediaExtGroup.setObjects(
    ("PDN-ARP-MIB", "ipNetToMediaNHR")
)
if mibBuilder.loadTexts:
    pdnNetToMediaExtGroup.setStatus("current")

pdnNetToMediaLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 8)
)
pdnNetToMediaLimitGroup.setObjects(
      *(("PDN-ARP-MIB", "ipNetToMediaLimitEnabled"),
        ("PDN-ARP-MIB", "ipNetToMediaMaxIPAddresses"))
)
if mibBuilder.loadTexts:
    pdnNetToMediaLimitGroup.setStatus("current")

pdnNetToMediaParamsAprConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 9)
)
pdnNetToMediaParamsAprConfigGroup.setObjects(
      *(("PDN-ARP-MIB", "pdnNetToMediaParamsAprRowStatus"),
        ("PDN-ARP-MIB", "pdnNetToMediaParamsAprReqPeriod"))
)
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprConfigGroup.setStatus("current")

pdnNetToMediaParamsAprTimeToNextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 1, 10)
)
pdnNetToMediaParamsAprTimeToNextGroup.setObjects(
    ("PDN-ARP-MIB", "pdnNetToMediaParamsAprTimeToNext")
)
if mibBuilder.loadTexts:
    pdnNetToMediaParamsAprTimeToNextGroup.setStatus("current")


# Notification objects

unauthorizedUserEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 2, 0, 1)
)
unauthorizedUserEvent.setObjects(
      *(("IP-MIB", "ipNetToMediaIfIndex"),
        ("IP-MIB", "ipNetToMediaPhysAddress"))
)
if mibBuilder.loadTexts:
    unauthorizedUserEvent.setStatus(
        "current"
    )


# Notifications groups

pdnNetToMediaUnauthorizedUserEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 2, 2, 1)
)
pdnNetToMediaUnauthorizedUserEventGroup.setObjects(
    ("PDN-ARP-MIB", "unauthorizedUserEvent")
)
if mibBuilder.loadTexts:
    pdnNetToMediaUnauthorizedUserEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnNetToMediaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    pdnNetToMediaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ARP-MIB",
    **{"pdn-arp": pdn_arp,
       "pdnNetToMediaGenericMIBObjects": pdnNetToMediaGenericMIBObjects,
       "pdnNetToMediaParams": pdnNetToMediaParams,
       "pdnNetToMediaParamsCompEntryTimeout": pdnNetToMediaParamsCompEntryTimeout,
       "pdnNetToMediaParamsIncompEntryTimeout": pdnNetToMediaParamsIncompEntryTimeout,
       "pdnNetToMediaParamsDefRouteEntryTimeout": pdnNetToMediaParamsDefRouteEntryTimeout,
       "pdnNetToMediaParamsAprTable": pdnNetToMediaParamsAprTable,
       "pdnNetToMediaParamsAprEntry": pdnNetToMediaParamsAprEntry,
       "pdnNetToMediaParamsAprIpAddr": pdnNetToMediaParamsAprIpAddr,
       "pdnNetToMediaParamsAprRowStatus": pdnNetToMediaParamsAprRowStatus,
       "pdnNetToMediaParamsAprReqPeriod": pdnNetToMediaParamsAprReqPeriod,
       "pdnNetToMediaParamsAprTimeToNext": pdnNetToMediaParamsAprTimeToNext,
       "pdnNetToMediaConfig": pdnNetToMediaConfig,
       "pdnNetToMediaConfigTable": pdnNetToMediaConfigTable,
       "pdnNetToMediaConfigEntry": pdnNetToMediaConfigEntry,
       "pdnNetToMediaConfigIpAddr": pdnNetToMediaConfigIpAddr,
       "pdnNetToMediaConfigMacAddr": pdnNetToMediaConfigMacAddr,
       "pdnNetToMediaConfigMin": pdnNetToMediaConfigMin,
       "pdnNetToMediaConfigFlags": pdnNetToMediaConfigFlags,
       "pdnNetToMediaConfigTrailer": pdnNetToMediaConfigTrailer,
       "pdnNetToMediaConfigPerm": pdnNetToMediaConfigPerm,
       "pdnNetToMediaConfigRowStatus": pdnNetToMediaConfigRowStatus,
       "pdnNetToMediaClearAllArp": pdnNetToMediaClearAllArp,
       "pdnNetToMediaProxyArpTable": pdnNetToMediaProxyArpTable,
       "pdnNetToMediaProxyArpEntry": pdnNetToMediaProxyArpEntry,
       "pdnNetToMediaProxyArpStatus": pdnNetToMediaProxyArpStatus,
       "ipNetToMediaConfig": ipNetToMediaConfig,
       "ipNetToMediaForwardingMode": ipNetToMediaForwardingMode,
       "ipNetToMediaDefaultNHR": ipNetToMediaDefaultNHR,
       "ipNetToMediaExtTable": ipNetToMediaExtTable,
       "ipNetToMediaExtEntry": ipNetToMediaExtEntry,
       "ipNetToMediaNHR": ipNetToMediaNHR,
       "ipNetToMediaLimitTable": ipNetToMediaLimitTable,
       "ipNetToMediaLimitEntry": ipNetToMediaLimitEntry,
       "ipNetToMediaLimitEnabled": ipNetToMediaLimitEnabled,
       "ipNetToMediaMaxIPAddresses": ipNetToMediaMaxIPAddresses,
       "pdnNetTo8023MediaConfig": pdnNetTo8023MediaConfig,
       "pdnNetTo8023MediaConfigTable": pdnNetTo8023MediaConfigTable,
       "pdnNetTo8023MediaConfigEntry": pdnNetTo8023MediaConfigEntry,
       "pdnNetTo8023MediaConfigIpAddr": pdnNetTo8023MediaConfigIpAddr,
       "pdnNetTo8023MediaConfigVnidId": pdnNetTo8023MediaConfigVnidId,
       "pdnNetTo8023MediaConfigMacAddr": pdnNetTo8023MediaConfigMacAddr,
       "pdnNetTo8023MediaConfigMin": pdnNetTo8023MediaConfigMin,
       "pdnNetTo8023MediaConfigFlags": pdnNetTo8023MediaConfigFlags,
       "pdnNetTo8023MediaConfigTrailer": pdnNetTo8023MediaConfigTrailer,
       "pdnNetTo8023MediaConfigPerm": pdnNetTo8023MediaConfigPerm,
       "pdnNetTo8023MediaConfigRowStatus": pdnNetTo8023MediaConfigRowStatus,
       "pdnNetToMediaConformance": pdnNetToMediaConformance,
       "pdnNetToMediaCompliances": pdnNetToMediaCompliances,
       "pdnNetToMediaCompliance": pdnNetToMediaCompliance,
       "pdnNetToMediaGroups": pdnNetToMediaGroups,
       "pdnNetToMediaObjGroups": pdnNetToMediaObjGroups,
       "pdnNetToMediaParamsGroup": pdnNetToMediaParamsGroup,
       "pdnNetToMediaConfigGroup": pdnNetToMediaConfigGroup,
       "pdnNetToMedia8023ConfigGroup": pdnNetToMedia8023ConfigGroup,
       "pdnNetToMediaClearGroup": pdnNetToMediaClearGroup,
       "pdnNetToMediaProxyArpGroup": pdnNetToMediaProxyArpGroup,
       "pdnNetToMediaConfigProxyArpGroup": pdnNetToMediaConfigProxyArpGroup,
       "pdnNetToMediaExtGroup": pdnNetToMediaExtGroup,
       "pdnNetToMediaLimitGroup": pdnNetToMediaLimitGroup,
       "pdnNetToMediaParamsAprConfigGroup": pdnNetToMediaParamsAprConfigGroup,
       "pdnNetToMediaParamsAprTimeToNextGroup": pdnNetToMediaParamsAprTimeToNextGroup,
       "pdnNetToMediaNtfyGroups": pdnNetToMediaNtfyGroups,
       "pdnNetToMediaUnauthorizedUserEventGroup": pdnNetToMediaUnauthorizedUserEventGroup,
       "pdnNetToMediaMIBTraps": pdnNetToMediaMIBTraps,
       "pdnNetToMediaMIBNotifications": pdnNetToMediaMIBNotifications,
       "unauthorizedUserEvent": unauthorizedUserEvent}
)
