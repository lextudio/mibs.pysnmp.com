# SNMP MIB module (CISCO-DIAMETER-BASE-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIAMETER-BASE-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:00 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDiameterBasePMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133)
)
ciscoDiameterBasePMIB.setRevisions(
        ("2006-08-24 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDiameterBasePMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDiameterBasePMIBNotifs = _CiscoDiameterBasePMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0)
)
_CiscoDiameterBasePMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDiameterBasePMIBObjects = _CiscoDiameterBasePMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1)
)
_CdbpLocalCfgs_ObjectIdentity = ObjectIdentity
cdbpLocalCfgs = _CdbpLocalCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1)
)
_CdbpLocalId_Type = SnmpAdminString
_CdbpLocalId_Object = MibScalar
cdbpLocalId = _CdbpLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 1),
    _CdbpLocalId_Type()
)
cdbpLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalId.setStatus("current")
_CdbpLocalIpAddrTable_Object = MibTable
cdbpLocalIpAddrTable = _CdbpLocalIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdbpLocalIpAddrTable.setStatus("current")
_CdbpLocalIpAddrEntry_Object = MibTableRow
cdbpLocalIpAddrEntry = _CdbpLocalIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 2, 1)
)
cdbpLocalIpAddrEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalIpAddrIndex"),
)
if mibBuilder.loadTexts:
    cdbpLocalIpAddrEntry.setStatus("current")


class _CdbpLocalIpAddrIndex_Type(Unsigned32):
    """Custom type cdbpLocalIpAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpLocalIpAddrIndex_Type.__name__ = "Unsigned32"
_CdbpLocalIpAddrIndex_Object = MibTableColumn
cdbpLocalIpAddrIndex = _CdbpLocalIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 2, 1, 1),
    _CdbpLocalIpAddrIndex_Type()
)
cdbpLocalIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpLocalIpAddrIndex.setStatus("current")
_CdbpLocalIpAddrType_Type = InetAddressType
_CdbpLocalIpAddrType_Object = MibTableColumn
cdbpLocalIpAddrType = _CdbpLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 2, 1, 2),
    _CdbpLocalIpAddrType_Type()
)
cdbpLocalIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalIpAddrType.setStatus("current")
_CdbpLocalIpAddress_Type = InetAddress
_CdbpLocalIpAddress_Object = MibTableColumn
cdbpLocalIpAddress = _CdbpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 2, 1, 3),
    _CdbpLocalIpAddress_Type()
)
cdbpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalIpAddress.setStatus("current")


class _CdbpLocalTcpListenPort_Type(Unsigned32):
    """Custom type cdbpLocalTcpListenPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdbpLocalTcpListenPort_Type.__name__ = "Unsigned32"
_CdbpLocalTcpListenPort_Object = MibScalar
cdbpLocalTcpListenPort = _CdbpLocalTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 3),
    _CdbpLocalTcpListenPort_Type()
)
cdbpLocalTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalTcpListenPort.setStatus("current")


class _CdbpLocalSctpListenPort_Type(Unsigned32):
    """Custom type cdbpLocalSctpListenPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdbpLocalSctpListenPort_Type.__name__ = "Unsigned32"
_CdbpLocalSctpListenPort_Object = MibScalar
cdbpLocalSctpListenPort = _CdbpLocalSctpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 4),
    _CdbpLocalSctpListenPort_Type()
)
cdbpLocalSctpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalSctpListenPort.setStatus("current")
_CdbpLocalOriginHost_Type = SnmpAdminString
_CdbpLocalOriginHost_Object = MibScalar
cdbpLocalOriginHost = _CdbpLocalOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 5),
    _CdbpLocalOriginHost_Type()
)
cdbpLocalOriginHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdbpLocalOriginHost.setStatus("current")
_CdbpLocalRealm_Type = SnmpAdminString
_CdbpLocalRealm_Object = MibScalar
cdbpLocalRealm = _CdbpLocalRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 6),
    _CdbpLocalRealm_Type()
)
cdbpLocalRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalRealm.setStatus("current")


class _CdbpRedundancyEnabled_Type(TruthValue):
    """Custom type cdbpRedundancyEnabled based on TruthValue"""


_CdbpRedundancyEnabled_Object = MibScalar
cdbpRedundancyEnabled = _CdbpRedundancyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 7),
    _CdbpRedundancyEnabled_Type()
)
cdbpRedundancyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdbpRedundancyEnabled.setStatus("current")


class _CdbpRedundancyInfraState_Type(Integer32):
    """Custom type cdbpRedundancyInfraState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("rfActive", 13),
          ("rfActiveDrain", 10),
          ("rfActiveExtraload", 14),
          ("rfActiveFast", 9),
          ("rfActivePostconfig", 12),
          ("rfActivePreconfig", 11),
          ("rfDisabled", 1),
          ("rfInitialization", 2),
          ("rfNegotiation", 3),
          ("rfStandbyBulk", 7),
          ("rfStandbyCold", 4),
          ("rfStandbyConfig", 5),
          ("rfStandbyFileSys", 6),
          ("rfStandbyHot", 8),
          ("rfUnknown", 0))
    )


_CdbpRedundancyInfraState_Type.__name__ = "Integer32"
_CdbpRedundancyInfraState_Object = MibScalar
cdbpRedundancyInfraState = _CdbpRedundancyInfraState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 8),
    _CdbpRedundancyInfraState_Type()
)
cdbpRedundancyInfraState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRedundancyInfraState.setStatus("current")
_CdbpRedundancyLastSwitchover_Type = SnmpAdminString
_CdbpRedundancyLastSwitchover_Object = MibScalar
cdbpRedundancyLastSwitchover = _CdbpRedundancyLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 9),
    _CdbpRedundancyLastSwitchover_Type()
)
cdbpRedundancyLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRedundancyLastSwitchover.setStatus("current")
_CdbpLocalApplTable_Object = MibTable
cdbpLocalApplTable = _CdbpLocalApplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cdbpLocalApplTable.setStatus("current")
_CdbpLocalApplEntry_Object = MibTableRow
cdbpLocalApplEntry = _CdbpLocalApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 10, 1)
)
cdbpLocalApplEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalApplIndex"),
)
if mibBuilder.loadTexts:
    cdbpLocalApplEntry.setStatus("current")


class _CdbpLocalApplIndex_Type(Unsigned32):
    """Custom type cdbpLocalApplIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpLocalApplIndex_Type.__name__ = "Unsigned32"
_CdbpLocalApplIndex_Object = MibTableColumn
cdbpLocalApplIndex = _CdbpLocalApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 10, 1, 1),
    _CdbpLocalApplIndex_Type()
)
cdbpLocalApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpLocalApplIndex.setStatus("current")


class _CdbpLocalApplStorageType_Type(StorageType):
    """Custom type cdbpLocalApplStorageType based on StorageType"""


_CdbpLocalApplStorageType_Object = MibTableColumn
cdbpLocalApplStorageType = _CdbpLocalApplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 10, 1, 2),
    _CdbpLocalApplStorageType_Type()
)
cdbpLocalApplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpLocalApplStorageType.setStatus("current")
_CdbpLocalApplRowStatus_Type = RowStatus
_CdbpLocalApplRowStatus_Object = MibTableColumn
cdbpLocalApplRowStatus = _CdbpLocalApplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 10, 1, 3),
    _CdbpLocalApplRowStatus_Type()
)
cdbpLocalApplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpLocalApplRowStatus.setStatus("current")
_CdbpLocalVendorTable_Object = MibTable
cdbpLocalVendorTable = _CdbpLocalVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cdbpLocalVendorTable.setStatus("current")
_CdbpLocalVendorEntry_Object = MibTableRow
cdbpLocalVendorEntry = _CdbpLocalVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11, 1)
)
cdbpLocalVendorEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalVendorIndex"),
)
if mibBuilder.loadTexts:
    cdbpLocalVendorEntry.setStatus("current")


class _CdbpLocalVendorIndex_Type(Unsigned32):
    """Custom type cdbpLocalVendorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpLocalVendorIndex_Type.__name__ = "Unsigned32"
_CdbpLocalVendorIndex_Object = MibTableColumn
cdbpLocalVendorIndex = _CdbpLocalVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11, 1, 1),
    _CdbpLocalVendorIndex_Type()
)
cdbpLocalVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpLocalVendorIndex.setStatus("current")


class _CdbpLocalVendorId_Type(Integer32):
    """Custom type cdbpLocalVendorId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              10415,
              12645)
        )
    )
    namedValues = NamedValues(
        *(("diameterVendor3gpp", 10415),
          ("diameterVendorCisco", 9),
          ("diameterVendorIetf", 0),
          ("diameterVendorVodafone", 12645))
    )


_CdbpLocalVendorId_Type.__name__ = "Integer32"
_CdbpLocalVendorId_Object = MibTableColumn
cdbpLocalVendorId = _CdbpLocalVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11, 1, 2),
    _CdbpLocalVendorId_Type()
)
cdbpLocalVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpLocalVendorId.setStatus("current")


class _CdbpLocalVendorStorageType_Type(StorageType):
    """Custom type cdbpLocalVendorStorageType based on StorageType"""


_CdbpLocalVendorStorageType_Object = MibTableColumn
cdbpLocalVendorStorageType = _CdbpLocalVendorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11, 1, 3),
    _CdbpLocalVendorStorageType_Type()
)
cdbpLocalVendorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpLocalVendorStorageType.setStatus("current")
_CdbpLocalVendorRowStatus_Type = RowStatus
_CdbpLocalVendorRowStatus_Object = MibTableColumn
cdbpLocalVendorRowStatus = _CdbpLocalVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 11, 1, 4),
    _CdbpLocalVendorRowStatus_Type()
)
cdbpLocalVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpLocalVendorRowStatus.setStatus("current")
_CdbpAppAdvToPeerTable_Object = MibTable
cdbpAppAdvToPeerTable = _CdbpAppAdvToPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerTable.setStatus("current")
_CdbpAppAdvToPeerEntry_Object = MibTableRow
cdbpAppAdvToPeerEntry = _CdbpAppAdvToPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1)
)
cdbpAppAdvToPeerEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvToPeerVendorId"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvToPeerIndex"),
)
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerEntry.setStatus("current")


class _CdbpAppAdvToPeerVendorId_Type(Unsigned32):
    """Custom type cdbpAppAdvToPeerVendorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpAppAdvToPeerVendorId_Type.__name__ = "Unsigned32"
_CdbpAppAdvToPeerVendorId_Object = MibTableColumn
cdbpAppAdvToPeerVendorId = _CdbpAppAdvToPeerVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1, 1),
    _CdbpAppAdvToPeerVendorId_Type()
)
cdbpAppAdvToPeerVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerVendorId.setStatus("current")


class _CdbpAppAdvToPeerIndex_Type(Unsigned32):
    """Custom type cdbpAppAdvToPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpAppAdvToPeerIndex_Type.__name__ = "Unsigned32"
_CdbpAppAdvToPeerIndex_Object = MibTableColumn
cdbpAppAdvToPeerIndex = _CdbpAppAdvToPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1, 2),
    _CdbpAppAdvToPeerIndex_Type()
)
cdbpAppAdvToPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerIndex.setStatus("current")


class _CdbpAppAdvToPeerServices_Type(Integer32):
    """Custom type cdbpAppAdvToPeerServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acct", 1),
          ("auth", 2),
          ("both", 3))
    )


_CdbpAppAdvToPeerServices_Type.__name__ = "Integer32"
_CdbpAppAdvToPeerServices_Object = MibTableColumn
cdbpAppAdvToPeerServices = _CdbpAppAdvToPeerServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1, 3),
    _CdbpAppAdvToPeerServices_Type()
)
cdbpAppAdvToPeerServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerServices.setStatus("current")


class _CdbpAppAdvToPeerStorageType_Type(StorageType):
    """Custom type cdbpAppAdvToPeerStorageType based on StorageType"""


_CdbpAppAdvToPeerStorageType_Object = MibTableColumn
cdbpAppAdvToPeerStorageType = _CdbpAppAdvToPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1, 4),
    _CdbpAppAdvToPeerStorageType_Type()
)
cdbpAppAdvToPeerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerStorageType.setStatus("current")
_CdbpAppAdvToPeerRowStatus_Type = RowStatus
_CdbpAppAdvToPeerRowStatus_Object = MibTableColumn
cdbpAppAdvToPeerRowStatus = _CdbpAppAdvToPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 1, 12, 1, 5),
    _CdbpAppAdvToPeerRowStatus_Type()
)
cdbpAppAdvToPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpAppAdvToPeerRowStatus.setStatus("current")
_CdbpLocalStats_ObjectIdentity = ObjectIdentity
cdbpLocalStats = _CdbpLocalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2)
)
_CdbpLocalStatsTotalPacketsIn_Type = Counter32
_CdbpLocalStatsTotalPacketsIn_Object = MibScalar
cdbpLocalStatsTotalPacketsIn = _CdbpLocalStatsTotalPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2, 1),
    _CdbpLocalStatsTotalPacketsIn_Type()
)
cdbpLocalStatsTotalPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalStatsTotalPacketsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpLocalStatsTotalPacketsIn.setUnits("packets")
_CdbpLocalStatsTotalPacketsOut_Type = Counter32
_CdbpLocalStatsTotalPacketsOut_Object = MibScalar
cdbpLocalStatsTotalPacketsOut = _CdbpLocalStatsTotalPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2, 2),
    _CdbpLocalStatsTotalPacketsOut_Type()
)
cdbpLocalStatsTotalPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalStatsTotalPacketsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpLocalStatsTotalPacketsOut.setUnits("packets")
_CdbpLocalStatsTotalUpTime_Type = TimeTicks
_CdbpLocalStatsTotalUpTime_Object = MibScalar
cdbpLocalStatsTotalUpTime = _CdbpLocalStatsTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2, 3),
    _CdbpLocalStatsTotalUpTime_Type()
)
cdbpLocalStatsTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalStatsTotalUpTime.setStatus("current")
_CdbpLocalResetTime_Type = TimeTicks
_CdbpLocalResetTime_Object = MibScalar
cdbpLocalResetTime = _CdbpLocalResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2, 4),
    _CdbpLocalResetTime_Type()
)
cdbpLocalResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpLocalResetTime.setStatus("current")


class _CdbpLocalConfigReset_Type(Integer32):
    """Custom type cdbpLocalConfigReset based on Integer32"""
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
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_CdbpLocalConfigReset_Type.__name__ = "Integer32"
_CdbpLocalConfigReset_Object = MibScalar
cdbpLocalConfigReset = _CdbpLocalConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 2, 5),
    _CdbpLocalConfigReset_Type()
)
cdbpLocalConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdbpLocalConfigReset.setStatus("current")
_CdbpPeerCfgs_ObjectIdentity = ObjectIdentity
cdbpPeerCfgs = _CdbpPeerCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3)
)
_CdbpPeerTable_Object = MibTable
cdbpPeerTable = _CdbpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdbpPeerTable.setStatus("current")
_CdbpPeerEntry_Object = MibTableRow
cdbpPeerEntry = _CdbpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1)
)
cdbpPeerEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
)
if mibBuilder.loadTexts:
    cdbpPeerEntry.setStatus("current")


class _CdbpPeerIndex_Type(Unsigned32):
    """Custom type cdbpPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpPeerIndex_Type.__name__ = "Unsigned32"
_CdbpPeerIndex_Object = MibTableColumn
cdbpPeerIndex = _CdbpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 1),
    _CdbpPeerIndex_Type()
)
cdbpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpPeerIndex.setStatus("current")
_CdbpPeerId_Type = SnmpAdminString
_CdbpPeerId_Object = MibTableColumn
cdbpPeerId = _CdbpPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 2),
    _CdbpPeerId_Type()
)
cdbpPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerId.setStatus("current")


class _CdbpPeerPortConnect_Type(Unsigned32):
    """Custom type cdbpPeerPortConnect based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdbpPeerPortConnect_Type.__name__ = "Unsigned32"
_CdbpPeerPortConnect_Object = MibTableColumn
cdbpPeerPortConnect = _CdbpPeerPortConnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 3),
    _CdbpPeerPortConnect_Type()
)
cdbpPeerPortConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerPortConnect.setStatus("current")


class _CdbpPeerPortListen_Type(Unsigned32):
    """Custom type cdbpPeerPortListen based on Unsigned32"""
    defaultValue = 3868

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdbpPeerPortListen_Type.__name__ = "Unsigned32"
_CdbpPeerPortListen_Object = MibTableColumn
cdbpPeerPortListen = _CdbpPeerPortListen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 4),
    _CdbpPeerPortListen_Type()
)
cdbpPeerPortListen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerPortListen.setStatus("current")


class _CdbpPeerProtocol_Type(Integer32):
    """Custom type cdbpPeerProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sctp", 2),
          ("tcp", 1))
    )


_CdbpPeerProtocol_Type.__name__ = "Integer32"
_CdbpPeerProtocol_Object = MibTableColumn
cdbpPeerProtocol = _CdbpPeerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 5),
    _CdbpPeerProtocol_Type()
)
cdbpPeerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerProtocol.setStatus("current")


class _CdbpPeerSecurity_Type(Integer32):
    """Custom type cdbpPeerSecurity based on Integer32"""
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
        *(("ipsec", 3),
          ("other", 1),
          ("tls", 2))
    )


_CdbpPeerSecurity_Type.__name__ = "Integer32"
_CdbpPeerSecurity_Object = MibTableColumn
cdbpPeerSecurity = _CdbpPeerSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 6),
    _CdbpPeerSecurity_Type()
)
cdbpPeerSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerSecurity.setStatus("current")


class _CdbpPeerFirmwareRevision_Type(Unsigned32):
    """Custom type cdbpPeerFirmwareRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpPeerFirmwareRevision_Type.__name__ = "Unsigned32"
_CdbpPeerFirmwareRevision_Object = MibTableColumn
cdbpPeerFirmwareRevision = _CdbpPeerFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 7),
    _CdbpPeerFirmwareRevision_Type()
)
cdbpPeerFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerFirmwareRevision.setStatus("current")


class _CdbpPeerStorageType_Type(StorageType):
    """Custom type cdbpPeerStorageType based on StorageType"""


_CdbpPeerStorageType_Object = MibTableColumn
cdbpPeerStorageType = _CdbpPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 8),
    _CdbpPeerStorageType_Type()
)
cdbpPeerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerStorageType.setStatus("current")
_CdbpPeerRowStatus_Type = RowStatus
_CdbpPeerRowStatus_Object = MibTableColumn
cdbpPeerRowStatus = _CdbpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 1, 1, 9),
    _CdbpPeerRowStatus_Type()
)
cdbpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerRowStatus.setStatus("current")
_CdbpPeerIpAddrTable_Object = MibTable
cdbpPeerIpAddrTable = _CdbpPeerIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdbpPeerIpAddrTable.setStatus("current")
_CdbpPeerIpAddrEntry_Object = MibTableRow
cdbpPeerIpAddrEntry = _CdbpPeerIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 2, 1)
)
cdbpPeerIpAddrEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIpAddressIndex"),
)
if mibBuilder.loadTexts:
    cdbpPeerIpAddrEntry.setStatus("current")


class _CdbpPeerIpAddressIndex_Type(Unsigned32):
    """Custom type cdbpPeerIpAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpPeerIpAddressIndex_Type.__name__ = "Unsigned32"
_CdbpPeerIpAddressIndex_Object = MibTableColumn
cdbpPeerIpAddressIndex = _CdbpPeerIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 2, 1, 1),
    _CdbpPeerIpAddressIndex_Type()
)
cdbpPeerIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpPeerIpAddressIndex.setStatus("current")
_CdbpPeerIpAddressType_Type = InetAddressType
_CdbpPeerIpAddressType_Object = MibTableColumn
cdbpPeerIpAddressType = _CdbpPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 2, 1, 2),
    _CdbpPeerIpAddressType_Type()
)
cdbpPeerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerIpAddressType.setStatus("current")
_CdbpPeerIpAddress_Type = IpAddress
_CdbpPeerIpAddress_Object = MibTableColumn
cdbpPeerIpAddress = _CdbpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 2, 1, 3),
    _CdbpPeerIpAddress_Type()
)
cdbpPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdbpPeerIpAddress.setStatus("current")
_CdbpAppAdvFromPeerTable_Object = MibTable
cdbpAppAdvFromPeerTable = _CdbpAppAdvFromPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdbpAppAdvFromPeerTable.setStatus("current")
_CdbpAppAdvFromPeerEntry_Object = MibTableRow
cdbpAppAdvFromPeerEntry = _CdbpAppAdvFromPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 3, 1)
)
cdbpAppAdvFromPeerEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvFromPeerVendorId"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvFromPeerIndex"),
)
if mibBuilder.loadTexts:
    cdbpAppAdvFromPeerEntry.setStatus("current")


class _CdbpAppAdvFromPeerVendorId_Type(Unsigned32):
    """Custom type cdbpAppAdvFromPeerVendorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpAppAdvFromPeerVendorId_Type.__name__ = "Unsigned32"
_CdbpAppAdvFromPeerVendorId_Object = MibTableColumn
cdbpAppAdvFromPeerVendorId = _CdbpAppAdvFromPeerVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 3, 1, 1),
    _CdbpAppAdvFromPeerVendorId_Type()
)
cdbpAppAdvFromPeerVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpAppAdvFromPeerVendorId.setStatus("current")


class _CdbpAppAdvFromPeerIndex_Type(Unsigned32):
    """Custom type cdbpAppAdvFromPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpAppAdvFromPeerIndex_Type.__name__ = "Unsigned32"
_CdbpAppAdvFromPeerIndex_Object = MibTableColumn
cdbpAppAdvFromPeerIndex = _CdbpAppAdvFromPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 3, 1, 2),
    _CdbpAppAdvFromPeerIndex_Type()
)
cdbpAppAdvFromPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpAppAdvFromPeerIndex.setStatus("current")


class _CdbpAppAdvFromPeerType_Type(Integer32):
    """Custom type cdbpAppAdvFromPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acct", 1),
          ("auth", 2),
          ("both", 3))
    )


_CdbpAppAdvFromPeerType_Type.__name__ = "Integer32"
_CdbpAppAdvFromPeerType_Object = MibTableColumn
cdbpAppAdvFromPeerType = _CdbpAppAdvFromPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 3, 1, 3),
    _CdbpAppAdvFromPeerType_Type()
)
cdbpAppAdvFromPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpAppAdvFromPeerType.setStatus("current")
_CdbpPeerVendorTable_Object = MibTable
cdbpPeerVendorTable = _CdbpPeerVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cdbpPeerVendorTable.setStatus("current")
_CdbpPeerVendorEntry_Object = MibTableRow
cdbpPeerVendorEntry = _CdbpPeerVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4, 1)
)
cdbpPeerVendorEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerVendorIndex"),
)
if mibBuilder.loadTexts:
    cdbpPeerVendorEntry.setStatus("current")


class _CdbpPeerVendorIndex_Type(Unsigned32):
    """Custom type cdbpPeerVendorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpPeerVendorIndex_Type.__name__ = "Unsigned32"
_CdbpPeerVendorIndex_Object = MibTableColumn
cdbpPeerVendorIndex = _CdbpPeerVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4, 1, 1),
    _CdbpPeerVendorIndex_Type()
)
cdbpPeerVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpPeerVendorIndex.setStatus("current")


class _CdbpPeerVendorId_Type(Integer32):
    """Custom type cdbpPeerVendorId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              10415,
              12645)
        )
    )
    namedValues = NamedValues(
        *(("diameterVendor3gpp", 10415),
          ("diameterVendorCisco", 9),
          ("diameterVendorIetf", 0),
          ("diameterVendorVodafone", 12645))
    )


_CdbpPeerVendorId_Type.__name__ = "Integer32"
_CdbpPeerVendorId_Object = MibTableColumn
cdbpPeerVendorId = _CdbpPeerVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4, 1, 2),
    _CdbpPeerVendorId_Type()
)
cdbpPeerVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerVendorId.setStatus("current")


class _CdbpPeerVendorStorageType_Type(StorageType):
    """Custom type cdbpPeerVendorStorageType based on StorageType"""


_CdbpPeerVendorStorageType_Object = MibTableColumn
cdbpPeerVendorStorageType = _CdbpPeerVendorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4, 1, 3),
    _CdbpPeerVendorStorageType_Type()
)
cdbpPeerVendorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerVendorStorageType.setStatus("current")
_CdbpPeerVendorRowStatus_Type = RowStatus
_CdbpPeerVendorRowStatus_Object = MibTableColumn
cdbpPeerVendorRowStatus = _CdbpPeerVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 3, 4, 1, 4),
    _CdbpPeerVendorRowStatus_Type()
)
cdbpPeerVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdbpPeerVendorRowStatus.setStatus("current")
_CdbpPeerStats_ObjectIdentity = ObjectIdentity
cdbpPeerStats = _CdbpPeerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4)
)
_CdbpPeerStatsTable_Object = MibTable
cdbpPeerStatsTable = _CdbpPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdbpPeerStatsTable.setStatus("current")
_CdbpPeerStatsEntry_Object = MibTableRow
cdbpPeerStatsEntry = _CdbpPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1)
)
cdbpPeerStatsEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIndex"),
)
if mibBuilder.loadTexts:
    cdbpPeerStatsEntry.setStatus("current")


class _CdbpPeerStatsState_Type(Integer32):
    """Custom type cdbpPeerStatsState based on Integer32"""
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
        *(("closed", 1),
          ("closing", 8),
          ("elect", 4),
          ("iOpen", 7),
          ("rOpen", 6),
          ("waitConnAck", 2),
          ("waitICEA", 3),
          ("waitReturns", 5))
    )


_CdbpPeerStatsState_Type.__name__ = "Integer32"
_CdbpPeerStatsState_Object = MibTableColumn
cdbpPeerStatsState = _CdbpPeerStatsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 1),
    _CdbpPeerStatsState_Type()
)
cdbpPeerStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsState.setStatus("current")
_CdbpPeerStatsStateDuration_Type = TimeTicks
_CdbpPeerStatsStateDuration_Object = MibTableColumn
cdbpPeerStatsStateDuration = _CdbpPeerStatsStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 2),
    _CdbpPeerStatsStateDuration_Type()
)
cdbpPeerStatsStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsStateDuration.setStatus("current")


class _CdbpPeerStatsLastDiscCause_Type(Integer32):
    """Custom type cdbpPeerStatsLastDiscCause based on Integer32"""
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
        *(("busy", 2),
          ("doNotWantToTalk", 3),
          ("election", 4),
          ("rebooting", 1))
    )


_CdbpPeerStatsLastDiscCause_Type.__name__ = "Integer32"
_CdbpPeerStatsLastDiscCause_Object = MibTableColumn
cdbpPeerStatsLastDiscCause = _CdbpPeerStatsLastDiscCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 3),
    _CdbpPeerStatsLastDiscCause_Type()
)
cdbpPeerStatsLastDiscCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsLastDiscCause.setStatus("current")


class _CdbpPeerStatsWhoInitDisconnect_Type(Integer32):
    """Custom type cdbpPeerStatsWhoInitDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("peer", 2))
    )


_CdbpPeerStatsWhoInitDisconnect_Type.__name__ = "Integer32"
_CdbpPeerStatsWhoInitDisconnect_Object = MibTableColumn
cdbpPeerStatsWhoInitDisconnect = _CdbpPeerStatsWhoInitDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 4),
    _CdbpPeerStatsWhoInitDisconnect_Type()
)
cdbpPeerStatsWhoInitDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsWhoInitDisconnect.setStatus("current")


class _CdbpPeerStatsDWCurrentStatus_Type(Integer32):
    """Custom type cdbpPeerStatsDWCurrentStatus based on Integer32"""
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
        *(("down", 3),
          ("okay", 1),
          ("reopen", 4),
          ("suspect", 2))
    )


_CdbpPeerStatsDWCurrentStatus_Type.__name__ = "Integer32"
_CdbpPeerStatsDWCurrentStatus_Object = MibTableColumn
cdbpPeerStatsDWCurrentStatus = _CdbpPeerStatsDWCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 5),
    _CdbpPeerStatsDWCurrentStatus_Type()
)
cdbpPeerStatsDWCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWCurrentStatus.setStatus("current")
_CdbpPeerStatsTimeoutConnAtmpts_Type = Counter32
_CdbpPeerStatsTimeoutConnAtmpts_Object = MibTableColumn
cdbpPeerStatsTimeoutConnAtmpts = _CdbpPeerStatsTimeoutConnAtmpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 6),
    _CdbpPeerStatsTimeoutConnAtmpts_Type()
)
cdbpPeerStatsTimeoutConnAtmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsTimeoutConnAtmpts.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsTimeoutConnAtmpts.setUnits("attempts")
_CdbpPeerStatsASRsIn_Type = Counter32
_CdbpPeerStatsASRsIn_Object = MibTableColumn
cdbpPeerStatsASRsIn = _CdbpPeerStatsASRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 7),
    _CdbpPeerStatsASRsIn_Type()
)
cdbpPeerStatsASRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsASRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsASRsIn.setUnits("messages")
_CdbpPeerStatsASRsOut_Type = Counter32
_CdbpPeerStatsASRsOut_Object = MibTableColumn
cdbpPeerStatsASRsOut = _CdbpPeerStatsASRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 8),
    _CdbpPeerStatsASRsOut_Type()
)
cdbpPeerStatsASRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsASRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsASRsOut.setUnits("messages")
_CdbpPeerStatsASAsIn_Type = Counter32
_CdbpPeerStatsASAsIn_Object = MibTableColumn
cdbpPeerStatsASAsIn = _CdbpPeerStatsASAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 9),
    _CdbpPeerStatsASAsIn_Type()
)
cdbpPeerStatsASAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsASAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsASAsIn.setUnits("messages")
_CdbpPeerStatsASAsOut_Type = Counter32
_CdbpPeerStatsASAsOut_Object = MibTableColumn
cdbpPeerStatsASAsOut = _CdbpPeerStatsASAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 10),
    _CdbpPeerStatsASAsOut_Type()
)
cdbpPeerStatsASAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsASAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsASAsOut.setUnits("messages")
_CdbpPeerStatsACRsIn_Type = Counter32
_CdbpPeerStatsACRsIn_Object = MibTableColumn
cdbpPeerStatsACRsIn = _CdbpPeerStatsACRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 11),
    _CdbpPeerStatsACRsIn_Type()
)
cdbpPeerStatsACRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsACRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsACRsIn.setUnits("messages")
_CdbpPeerStatsACRsOut_Type = Counter32
_CdbpPeerStatsACRsOut_Object = MibTableColumn
cdbpPeerStatsACRsOut = _CdbpPeerStatsACRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 12),
    _CdbpPeerStatsACRsOut_Type()
)
cdbpPeerStatsACRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsACRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsACRsOut.setUnits("messages")
_CdbpPeerStatsACAsIn_Type = Counter32
_CdbpPeerStatsACAsIn_Object = MibTableColumn
cdbpPeerStatsACAsIn = _CdbpPeerStatsACAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 13),
    _CdbpPeerStatsACAsIn_Type()
)
cdbpPeerStatsACAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsACAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsACAsIn.setUnits("messages")
_CdbpPeerStatsACAsOut_Type = Counter32
_CdbpPeerStatsACAsOut_Object = MibTableColumn
cdbpPeerStatsACAsOut = _CdbpPeerStatsACAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 14),
    _CdbpPeerStatsACAsOut_Type()
)
cdbpPeerStatsACAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsACAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsACAsOut.setUnits("messages")
_CdbpPeerStatsCERsIn_Type = Counter32
_CdbpPeerStatsCERsIn_Object = MibTableColumn
cdbpPeerStatsCERsIn = _CdbpPeerStatsCERsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 15),
    _CdbpPeerStatsCERsIn_Type()
)
cdbpPeerStatsCERsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsCERsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsCERsIn.setUnits("messages")
_CdbpPeerStatsCERsOut_Type = Counter32
_CdbpPeerStatsCERsOut_Object = MibTableColumn
cdbpPeerStatsCERsOut = _CdbpPeerStatsCERsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 16),
    _CdbpPeerStatsCERsOut_Type()
)
cdbpPeerStatsCERsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsCERsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsCERsOut.setUnits("messages")
_CdbpPeerStatsCEAsIn_Type = Counter32
_CdbpPeerStatsCEAsIn_Object = MibTableColumn
cdbpPeerStatsCEAsIn = _CdbpPeerStatsCEAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 17),
    _CdbpPeerStatsCEAsIn_Type()
)
cdbpPeerStatsCEAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsCEAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsCEAsIn.setUnits("messages")
_CdbpPeerStatsCEAsOut_Type = Counter32
_CdbpPeerStatsCEAsOut_Object = MibTableColumn
cdbpPeerStatsCEAsOut = _CdbpPeerStatsCEAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 18),
    _CdbpPeerStatsCEAsOut_Type()
)
cdbpPeerStatsCEAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsCEAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsCEAsOut.setUnits("messages")
_CdbpPeerStatsDWRsIn_Type = Counter32
_CdbpPeerStatsDWRsIn_Object = MibTableColumn
cdbpPeerStatsDWRsIn = _CdbpPeerStatsDWRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 19),
    _CdbpPeerStatsDWRsIn_Type()
)
cdbpPeerStatsDWRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWRsIn.setUnits("messages")
_CdbpPeerStatsDWRsOut_Type = Counter32
_CdbpPeerStatsDWRsOut_Object = MibTableColumn
cdbpPeerStatsDWRsOut = _CdbpPeerStatsDWRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 20),
    _CdbpPeerStatsDWRsOut_Type()
)
cdbpPeerStatsDWRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWRsOut.setUnits("messages")
_CdbpPeerStatsDWAsIn_Type = Counter32
_CdbpPeerStatsDWAsIn_Object = MibTableColumn
cdbpPeerStatsDWAsIn = _CdbpPeerStatsDWAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 21),
    _CdbpPeerStatsDWAsIn_Type()
)
cdbpPeerStatsDWAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWAsIn.setUnits("messages")
_CdbpPeerStatsDWAsOut_Type = Counter32
_CdbpPeerStatsDWAsOut_Object = MibTableColumn
cdbpPeerStatsDWAsOut = _CdbpPeerStatsDWAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 22),
    _CdbpPeerStatsDWAsOut_Type()
)
cdbpPeerStatsDWAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWAsOut.setUnits("messages")
_CdbpPeerStatsDPRsIn_Type = Counter32
_CdbpPeerStatsDPRsIn_Object = MibTableColumn
cdbpPeerStatsDPRsIn = _CdbpPeerStatsDPRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 23),
    _CdbpPeerStatsDPRsIn_Type()
)
cdbpPeerStatsDPRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPRsIn.setUnits("messages")
_CdbpPeerStatsDPRsOut_Type = Counter32
_CdbpPeerStatsDPRsOut_Object = MibTableColumn
cdbpPeerStatsDPRsOut = _CdbpPeerStatsDPRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 24),
    _CdbpPeerStatsDPRsOut_Type()
)
cdbpPeerStatsDPRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPRsOut.setUnits("messages")
_CdbpPeerStatsDPAsIn_Type = Counter32
_CdbpPeerStatsDPAsIn_Object = MibTableColumn
cdbpPeerStatsDPAsIn = _CdbpPeerStatsDPAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 25),
    _CdbpPeerStatsDPAsIn_Type()
)
cdbpPeerStatsDPAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPAsIn.setUnits("messages")
_CdbpPeerStatsDPAsOut_Type = Counter32
_CdbpPeerStatsDPAsOut_Object = MibTableColumn
cdbpPeerStatsDPAsOut = _CdbpPeerStatsDPAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 26),
    _CdbpPeerStatsDPAsOut_Type()
)
cdbpPeerStatsDPAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsDPAsOut.setUnits("messages")
_CdbpPeerStatsRARsIn_Type = Counter32
_CdbpPeerStatsRARsIn_Object = MibTableColumn
cdbpPeerStatsRARsIn = _CdbpPeerStatsRARsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 27),
    _CdbpPeerStatsRARsIn_Type()
)
cdbpPeerStatsRARsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsRARsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsRARsIn.setUnits("messages")
_CdbpPeerStatsRARsOut_Type = Counter32
_CdbpPeerStatsRARsOut_Object = MibTableColumn
cdbpPeerStatsRARsOut = _CdbpPeerStatsRARsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 28),
    _CdbpPeerStatsRARsOut_Type()
)
cdbpPeerStatsRARsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsRARsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsRARsOut.setUnits("messages")
_CdbpPeerStatsRAAsIn_Type = Counter32
_CdbpPeerStatsRAAsIn_Object = MibTableColumn
cdbpPeerStatsRAAsIn = _CdbpPeerStatsRAAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 29),
    _CdbpPeerStatsRAAsIn_Type()
)
cdbpPeerStatsRAAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsRAAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsRAAsIn.setUnits("messages")
_CdbpPeerStatsRAAsOut_Type = Counter32
_CdbpPeerStatsRAAsOut_Object = MibTableColumn
cdbpPeerStatsRAAsOut = _CdbpPeerStatsRAAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 30),
    _CdbpPeerStatsRAAsOut_Type()
)
cdbpPeerStatsRAAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsRAAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsRAAsOut.setUnits("messages")
_CdbpPeerStatsSTRsIn_Type = Counter32
_CdbpPeerStatsSTRsIn_Object = MibTableColumn
cdbpPeerStatsSTRsIn = _CdbpPeerStatsSTRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 31),
    _CdbpPeerStatsSTRsIn_Type()
)
cdbpPeerStatsSTRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTRsIn.setUnits("messages")
_CdbpPeerStatsSTRsOut_Type = Counter32
_CdbpPeerStatsSTRsOut_Object = MibTableColumn
cdbpPeerStatsSTRsOut = _CdbpPeerStatsSTRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 32),
    _CdbpPeerStatsSTRsOut_Type()
)
cdbpPeerStatsSTRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTRsOut.setUnits("messages")
_CdbpPeerStatsSTAsIn_Type = Counter32
_CdbpPeerStatsSTAsIn_Object = MibTableColumn
cdbpPeerStatsSTAsIn = _CdbpPeerStatsSTAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 33),
    _CdbpPeerStatsSTAsIn_Type()
)
cdbpPeerStatsSTAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTAsIn.setUnits("messages")
_CdbpPeerStatsSTAsOut_Type = Counter32
_CdbpPeerStatsSTAsOut_Object = MibTableColumn
cdbpPeerStatsSTAsOut = _CdbpPeerStatsSTAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 34),
    _CdbpPeerStatsSTAsOut_Type()
)
cdbpPeerStatsSTAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpPeerStatsSTAsOut.setUnits("messages")
_CdbpPeerStatsDWReqTimer_Type = TimeTicks
_CdbpPeerStatsDWReqTimer_Object = MibTableColumn
cdbpPeerStatsDWReqTimer = _CdbpPeerStatsDWReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 35),
    _CdbpPeerStatsDWReqTimer_Type()
)
cdbpPeerStatsDWReqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsDWReqTimer.setStatus("current")
_CdbpPeerStatsRedirectEvents_Type = Counter32
_CdbpPeerStatsRedirectEvents_Object = MibTableColumn
cdbpPeerStatsRedirectEvents = _CdbpPeerStatsRedirectEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 36),
    _CdbpPeerStatsRedirectEvents_Type()
)
cdbpPeerStatsRedirectEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsRedirectEvents.setStatus("current")
_CdbpPeerStatsAccDupRequests_Type = Counter32
_CdbpPeerStatsAccDupRequests_Object = MibTableColumn
cdbpPeerStatsAccDupRequests = _CdbpPeerStatsAccDupRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 37),
    _CdbpPeerStatsAccDupRequests_Type()
)
cdbpPeerStatsAccDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsAccDupRequests.setStatus("current")
_CdbpPeerStatsMalformedReqsts_Type = Counter32
_CdbpPeerStatsMalformedReqsts_Object = MibTableColumn
cdbpPeerStatsMalformedReqsts = _CdbpPeerStatsMalformedReqsts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 38),
    _CdbpPeerStatsMalformedReqsts_Type()
)
cdbpPeerStatsMalformedReqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsMalformedReqsts.setStatus("current")
_CdbpPeerStatsAccsNotRecorded_Type = Counter32
_CdbpPeerStatsAccsNotRecorded_Object = MibTableColumn
cdbpPeerStatsAccsNotRecorded = _CdbpPeerStatsAccsNotRecorded_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 39),
    _CdbpPeerStatsAccsNotRecorded_Type()
)
cdbpPeerStatsAccsNotRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsAccsNotRecorded.setStatus("current")
_CdbpPeerStatsAccRetrans_Type = Counter32
_CdbpPeerStatsAccRetrans_Object = MibTableColumn
cdbpPeerStatsAccRetrans = _CdbpPeerStatsAccRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 40),
    _CdbpPeerStatsAccRetrans_Type()
)
cdbpPeerStatsAccRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsAccRetrans.setStatus("current")
_CdbpPeerStatsTotalRetrans_Type = Counter32
_CdbpPeerStatsTotalRetrans_Object = MibTableColumn
cdbpPeerStatsTotalRetrans = _CdbpPeerStatsTotalRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 41),
    _CdbpPeerStatsTotalRetrans_Type()
)
cdbpPeerStatsTotalRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsTotalRetrans.setStatus("current")
_CdbpPeerStatsAccPendReqstsOut_Type = Gauge32
_CdbpPeerStatsAccPendReqstsOut_Object = MibTableColumn
cdbpPeerStatsAccPendReqstsOut = _CdbpPeerStatsAccPendReqstsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 42),
    _CdbpPeerStatsAccPendReqstsOut_Type()
)
cdbpPeerStatsAccPendReqstsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsAccPendReqstsOut.setStatus("current")
_CdbpPeerStatsAccReqstsDropped_Type = Counter32
_CdbpPeerStatsAccReqstsDropped_Object = MibTableColumn
cdbpPeerStatsAccReqstsDropped = _CdbpPeerStatsAccReqstsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 43),
    _CdbpPeerStatsAccReqstsDropped_Type()
)
cdbpPeerStatsAccReqstsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsAccReqstsDropped.setStatus("current")
_CdbpPeerStatsHByHDropMessages_Type = Counter32
_CdbpPeerStatsHByHDropMessages_Object = MibTableColumn
cdbpPeerStatsHByHDropMessages = _CdbpPeerStatsHByHDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 44),
    _CdbpPeerStatsHByHDropMessages_Type()
)
cdbpPeerStatsHByHDropMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsHByHDropMessages.setStatus("current")
_CdbpPeerStatsEToEDupMessages_Type = Counter32
_CdbpPeerStatsEToEDupMessages_Object = MibTableColumn
cdbpPeerStatsEToEDupMessages = _CdbpPeerStatsEToEDupMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 45),
    _CdbpPeerStatsEToEDupMessages_Type()
)
cdbpPeerStatsEToEDupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsEToEDupMessages.setStatus("current")
_CdbpPeerStatsUnknownTypes_Type = Counter32
_CdbpPeerStatsUnknownTypes_Object = MibTableColumn
cdbpPeerStatsUnknownTypes = _CdbpPeerStatsUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 46),
    _CdbpPeerStatsUnknownTypes_Type()
)
cdbpPeerStatsUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsUnknownTypes.setStatus("current")
_CdbpPeerStatsProtocolErrors_Type = Counter32
_CdbpPeerStatsProtocolErrors_Object = MibTableColumn
cdbpPeerStatsProtocolErrors = _CdbpPeerStatsProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 47),
    _CdbpPeerStatsProtocolErrors_Type()
)
cdbpPeerStatsProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsProtocolErrors.setStatus("current")
_CdbpPeerStatsTransientFailures_Type = Counter32
_CdbpPeerStatsTransientFailures_Object = MibTableColumn
cdbpPeerStatsTransientFailures = _CdbpPeerStatsTransientFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 48),
    _CdbpPeerStatsTransientFailures_Type()
)
cdbpPeerStatsTransientFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsTransientFailures.setStatus("current")
_CdbpPeerStatsPermanentFailures_Type = Counter32
_CdbpPeerStatsPermanentFailures_Object = MibTableColumn
cdbpPeerStatsPermanentFailures = _CdbpPeerStatsPermanentFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 49),
    _CdbpPeerStatsPermanentFailures_Type()
)
cdbpPeerStatsPermanentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsPermanentFailures.setStatus("current")
_CdbpPeerStatsTransportDown_Type = Counter32
_CdbpPeerStatsTransportDown_Object = MibTableColumn
cdbpPeerStatsTransportDown = _CdbpPeerStatsTransportDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 4, 1, 1, 50),
    _CdbpPeerStatsTransportDown_Type()
)
cdbpPeerStatsTransportDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpPeerStatsTransportDown.setStatus("current")
_CdbpRealmCfgs_ObjectIdentity = ObjectIdentity
cdbpRealmCfgs = _CdbpRealmCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5)
)
_CdbpRealmKnownPeersTable_Object = MibTable
cdbpRealmKnownPeersTable = _CdbpRealmKnownPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdbpRealmKnownPeersTable.setStatus("current")
_CdbpRealmKnownPeersEntry_Object = MibTableRow
cdbpRealmKnownPeersEntry = _CdbpRealmKnownPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5, 1, 1)
)
cdbpRealmKnownPeersEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteIndex"),
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmKnownPeersIndex"),
)
if mibBuilder.loadTexts:
    cdbpRealmKnownPeersEntry.setStatus("current")


class _CdbpRealmKnownPeersIndex_Type(Unsigned32):
    """Custom type cdbpRealmKnownPeersIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpRealmKnownPeersIndex_Type.__name__ = "Unsigned32"
_CdbpRealmKnownPeersIndex_Object = MibTableColumn
cdbpRealmKnownPeersIndex = _CdbpRealmKnownPeersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5, 1, 1, 1),
    _CdbpRealmKnownPeersIndex_Type()
)
cdbpRealmKnownPeersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpRealmKnownPeersIndex.setStatus("current")


class _CdbpRealmKnownPeers_Type(Unsigned32):
    """Custom type cdbpRealmKnownPeers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpRealmKnownPeers_Type.__name__ = "Unsigned32"
_CdbpRealmKnownPeers_Object = MibTableColumn
cdbpRealmKnownPeers = _CdbpRealmKnownPeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5, 1, 1, 2),
    _CdbpRealmKnownPeers_Type()
)
cdbpRealmKnownPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmKnownPeers.setStatus("current")


class _CdbpRealmKnownPeersChosen_Type(Integer32):
    """Custom type cdbpRealmKnownPeersChosen based on Integer32"""
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
        *(("firstPreferred", 3),
          ("loadBalance", 2),
          ("mostRecentFirst", 4),
          ("other", 5),
          ("roundRobin", 1))
    )


_CdbpRealmKnownPeersChosen_Type.__name__ = "Integer32"
_CdbpRealmKnownPeersChosen_Object = MibTableColumn
cdbpRealmKnownPeersChosen = _CdbpRealmKnownPeersChosen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 5, 1, 1, 3),
    _CdbpRealmKnownPeersChosen_Type()
)
cdbpRealmKnownPeersChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmKnownPeersChosen.setStatus("current")
_CdbpRealmStats_ObjectIdentity = ObjectIdentity
cdbpRealmStats = _CdbpRealmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6)
)
_CdbpRealmMessageRouteTable_Object = MibTable
cdbpRealmMessageRouteTable = _CdbpRealmMessageRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteTable.setStatus("current")
_CdbpRealmMessageRouteEntry_Object = MibTableRow
cdbpRealmMessageRouteEntry = _CdbpRealmMessageRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1)
)
cdbpRealmMessageRouteEntry.setIndexNames(
    (0, "CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteIndex"),
)
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteEntry.setStatus("current")


class _CdbpRealmMessageRouteIndex_Type(Unsigned32):
    """Custom type cdbpRealmMessageRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpRealmMessageRouteIndex_Type.__name__ = "Unsigned32"
_CdbpRealmMessageRouteIndex_Object = MibTableColumn
cdbpRealmMessageRouteIndex = _CdbpRealmMessageRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 1),
    _CdbpRealmMessageRouteIndex_Type()
)
cdbpRealmMessageRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteIndex.setStatus("current")
_CdbpRealmMessageRouteRealm_Type = SnmpAdminString
_CdbpRealmMessageRouteRealm_Object = MibTableColumn
cdbpRealmMessageRouteRealm = _CdbpRealmMessageRouteRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 2),
    _CdbpRealmMessageRouteRealm_Type()
)
cdbpRealmMessageRouteRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRealm.setStatus("current")


class _CdbpRealmMessageRouteApp_Type(Unsigned32):
    """Custom type cdbpRealmMessageRouteApp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdbpRealmMessageRouteApp_Type.__name__ = "Unsigned32"
_CdbpRealmMessageRouteApp_Object = MibTableColumn
cdbpRealmMessageRouteApp = _CdbpRealmMessageRouteApp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 3),
    _CdbpRealmMessageRouteApp_Type()
)
cdbpRealmMessageRouteApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteApp.setStatus("current")


class _CdbpRealmMessageRouteType_Type(Integer32):
    """Custom type cdbpRealmMessageRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acct", 1),
          ("auth", 2),
          ("both", 3))
    )


_CdbpRealmMessageRouteType_Type.__name__ = "Integer32"
_CdbpRealmMessageRouteType_Object = MibTableColumn
cdbpRealmMessageRouteType = _CdbpRealmMessageRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 4),
    _CdbpRealmMessageRouteType_Type()
)
cdbpRealmMessageRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteType.setStatus("current")


class _CdbpRealmMessageRouteAction_Type(Integer32):
    """Custom type cdbpRealmMessageRouteAction based on Integer32"""
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
        *(("local", 1),
          ("proxy", 3),
          ("redirect", 4),
          ("relay", 2))
    )


_CdbpRealmMessageRouteAction_Type.__name__ = "Integer32"
_CdbpRealmMessageRouteAction_Object = MibTableColumn
cdbpRealmMessageRouteAction = _CdbpRealmMessageRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 5),
    _CdbpRealmMessageRouteAction_Type()
)
cdbpRealmMessageRouteAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteAction.setStatus("current")
_CdbpRealmMessageRouteACRsIn_Type = Counter32
_CdbpRealmMessageRouteACRsIn_Object = MibTableColumn
cdbpRealmMessageRouteACRsIn = _CdbpRealmMessageRouteACRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 6),
    _CdbpRealmMessageRouteACRsIn_Type()
)
cdbpRealmMessageRouteACRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACRsIn.setUnits("messages")
_CdbpRealmMessageRouteACRsOut_Type = Counter32
_CdbpRealmMessageRouteACRsOut_Object = MibTableColumn
cdbpRealmMessageRouteACRsOut = _CdbpRealmMessageRouteACRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 7),
    _CdbpRealmMessageRouteACRsOut_Type()
)
cdbpRealmMessageRouteACRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACRsOut.setUnits("messages")
_CdbpRealmMessageRouteACAsIn_Type = Counter32
_CdbpRealmMessageRouteACAsIn_Object = MibTableColumn
cdbpRealmMessageRouteACAsIn = _CdbpRealmMessageRouteACAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 8),
    _CdbpRealmMessageRouteACAsIn_Type()
)
cdbpRealmMessageRouteACAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACAsIn.setUnits("messages")
_CdbpRealmMessageRouteACAsOut_Type = Counter32
_CdbpRealmMessageRouteACAsOut_Object = MibTableColumn
cdbpRealmMessageRouteACAsOut = _CdbpRealmMessageRouteACAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 9),
    _CdbpRealmMessageRouteACAsOut_Type()
)
cdbpRealmMessageRouteACAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteACAsOut.setUnits("messages")
_CdbpRealmMessageRouteRARsIn_Type = Counter32
_CdbpRealmMessageRouteRARsIn_Object = MibTableColumn
cdbpRealmMessageRouteRARsIn = _CdbpRealmMessageRouteRARsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 10),
    _CdbpRealmMessageRouteRARsIn_Type()
)
cdbpRealmMessageRouteRARsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRARsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRARsIn.setUnits("messages")
_CdbpRealmMessageRouteRARsOut_Type = Counter32
_CdbpRealmMessageRouteRARsOut_Object = MibTableColumn
cdbpRealmMessageRouteRARsOut = _CdbpRealmMessageRouteRARsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 11),
    _CdbpRealmMessageRouteRARsOut_Type()
)
cdbpRealmMessageRouteRARsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRARsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRARsOut.setUnits("messages")
_CdbpRealmMessageRouteRAAsIn_Type = Counter32
_CdbpRealmMessageRouteRAAsIn_Object = MibTableColumn
cdbpRealmMessageRouteRAAsIn = _CdbpRealmMessageRouteRAAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 12),
    _CdbpRealmMessageRouteRAAsIn_Type()
)
cdbpRealmMessageRouteRAAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRAAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRAAsIn.setUnits("messages")
_CdbpRealmMessageRouteRAAsOut_Type = Counter32
_CdbpRealmMessageRouteRAAsOut_Object = MibTableColumn
cdbpRealmMessageRouteRAAsOut = _CdbpRealmMessageRouteRAAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 13),
    _CdbpRealmMessageRouteRAAsOut_Type()
)
cdbpRealmMessageRouteRAAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRAAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteRAAsOut.setUnits("messages")
_CdbpRealmMessageRouteSTRsIn_Type = Counter32
_CdbpRealmMessageRouteSTRsIn_Object = MibTableColumn
cdbpRealmMessageRouteSTRsIn = _CdbpRealmMessageRouteSTRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 14),
    _CdbpRealmMessageRouteSTRsIn_Type()
)
cdbpRealmMessageRouteSTRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTRsIn.setUnits("messages")
_CdbpRealmMessageRouteSTRsOut_Type = Counter32
_CdbpRealmMessageRouteSTRsOut_Object = MibTableColumn
cdbpRealmMessageRouteSTRsOut = _CdbpRealmMessageRouteSTRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 15),
    _CdbpRealmMessageRouteSTRsOut_Type()
)
cdbpRealmMessageRouteSTRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTRsOut.setUnits("messages")
_CdbpRealmMessageRouteSTAsIn_Type = Counter32
_CdbpRealmMessageRouteSTAsIn_Object = MibTableColumn
cdbpRealmMessageRouteSTAsIn = _CdbpRealmMessageRouteSTAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 16),
    _CdbpRealmMessageRouteSTAsIn_Type()
)
cdbpRealmMessageRouteSTAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTAsIn.setUnits("messages")
_CdbpRealmMessageRouteSTAsOut_Type = Counter32
_CdbpRealmMessageRouteSTAsOut_Object = MibTableColumn
cdbpRealmMessageRouteSTAsOut = _CdbpRealmMessageRouteSTAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 17),
    _CdbpRealmMessageRouteSTAsOut_Type()
)
cdbpRealmMessageRouteSTAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteSTAsOut.setUnits("messages")
_CdbpRealmMessageRouteASRsIn_Type = Counter32
_CdbpRealmMessageRouteASRsIn_Object = MibTableColumn
cdbpRealmMessageRouteASRsIn = _CdbpRealmMessageRouteASRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 18),
    _CdbpRealmMessageRouteASRsIn_Type()
)
cdbpRealmMessageRouteASRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASRsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASRsIn.setUnits("messages")
_CdbpRealmMessageRouteASRsOut_Type = Counter32
_CdbpRealmMessageRouteASRsOut_Object = MibTableColumn
cdbpRealmMessageRouteASRsOut = _CdbpRealmMessageRouteASRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 19),
    _CdbpRealmMessageRouteASRsOut_Type()
)
cdbpRealmMessageRouteASRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASRsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASRsOut.setUnits("messages")
_CdbpRealmMessageRouteASAsIn_Type = Counter32
_CdbpRealmMessageRouteASAsIn_Object = MibTableColumn
cdbpRealmMessageRouteASAsIn = _CdbpRealmMessageRouteASAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 20),
    _CdbpRealmMessageRouteASAsIn_Type()
)
cdbpRealmMessageRouteASAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASAsIn.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASAsIn.setUnits("messages")
_CdbpRealmMessageRouteASAsOut_Type = Counter32
_CdbpRealmMessageRouteASAsOut_Object = MibTableColumn
cdbpRealmMessageRouteASAsOut = _CdbpRealmMessageRouteASAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 21),
    _CdbpRealmMessageRouteASAsOut_Type()
)
cdbpRealmMessageRouteASAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASAsOut.setStatus("current")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteASAsOut.setUnits("messages")
_CdbpRealmMessageRouteAccRetrans_Type = Counter32
_CdbpRealmMessageRouteAccRetrans_Object = MibTableColumn
cdbpRealmMessageRouteAccRetrans = _CdbpRealmMessageRouteAccRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 22),
    _CdbpRealmMessageRouteAccRetrans_Type()
)
cdbpRealmMessageRouteAccRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteAccRetrans.setStatus("current")
_CdbpRealmMessageRouteAccDupReqsts_Type = Counter32
_CdbpRealmMessageRouteAccDupReqsts_Object = MibTableColumn
cdbpRealmMessageRouteAccDupReqsts = _CdbpRealmMessageRouteAccDupReqsts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 23),
    _CdbpRealmMessageRouteAccDupReqsts_Type()
)
cdbpRealmMessageRouteAccDupReqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteAccDupReqsts.setStatus("current")
_CdbpRealmMessageRoutePendReqstsOut_Type = Gauge32
_CdbpRealmMessageRoutePendReqstsOut_Object = MibTableColumn
cdbpRealmMessageRoutePendReqstsOut = _CdbpRealmMessageRoutePendReqstsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 24),
    _CdbpRealmMessageRoutePendReqstsOut_Type()
)
cdbpRealmMessageRoutePendReqstsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRoutePendReqstsOut.setStatus("current")
_CdbpRealmMessageRouteReqstsDrop_Type = Counter32
_CdbpRealmMessageRouteReqstsDrop_Object = MibTableColumn
cdbpRealmMessageRouteReqstsDrop = _CdbpRealmMessageRouteReqstsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 6, 1, 1, 25),
    _CdbpRealmMessageRouteReqstsDrop_Type()
)
cdbpRealmMessageRouteReqstsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdbpRealmMessageRouteReqstsDrop.setStatus("current")
_CdbpTrapCfgs_ObjectIdentity = ObjectIdentity
cdbpTrapCfgs = _CdbpTrapCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7)
)


class _CiscoDiaBaseProtEnableProtocolErrorNotif_Type(TruthValue):
    """Custom type ciscoDiaBaseProtEnableProtocolErrorNotif based on TruthValue"""


_CiscoDiaBaseProtEnableProtocolErrorNotif_Object = MibScalar
ciscoDiaBaseProtEnableProtocolErrorNotif = _CiscoDiaBaseProtEnableProtocolErrorNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7, 1),
    _CiscoDiaBaseProtEnableProtocolErrorNotif_Type()
)
ciscoDiaBaseProtEnableProtocolErrorNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoDiaBaseProtEnableProtocolErrorNotif.setStatus("current")


class _CiscoDiaBaseProtEnableTransientFailureNotif_Type(TruthValue):
    """Custom type ciscoDiaBaseProtEnableTransientFailureNotif based on TruthValue"""


_CiscoDiaBaseProtEnableTransientFailureNotif_Object = MibScalar
ciscoDiaBaseProtEnableTransientFailureNotif = _CiscoDiaBaseProtEnableTransientFailureNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7, 2),
    _CiscoDiaBaseProtEnableTransientFailureNotif_Type()
)
ciscoDiaBaseProtEnableTransientFailureNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoDiaBaseProtEnableTransientFailureNotif.setStatus("current")


class _CiscoDiaBaseProtEnablePermanentFailureNotif_Type(TruthValue):
    """Custom type ciscoDiaBaseProtEnablePermanentFailureNotif based on TruthValue"""


_CiscoDiaBaseProtEnablePermanentFailureNotif_Object = MibScalar
ciscoDiaBaseProtEnablePermanentFailureNotif = _CiscoDiaBaseProtEnablePermanentFailureNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7, 3),
    _CiscoDiaBaseProtEnablePermanentFailureNotif_Type()
)
ciscoDiaBaseProtEnablePermanentFailureNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoDiaBaseProtEnablePermanentFailureNotif.setStatus("current")


class _CiscoDiaBaseProtEnablePeerConnectionDownNotif_Type(TruthValue):
    """Custom type ciscoDiaBaseProtEnablePeerConnectionDownNotif based on TruthValue"""


_CiscoDiaBaseProtEnablePeerConnectionDownNotif_Object = MibScalar
ciscoDiaBaseProtEnablePeerConnectionDownNotif = _CiscoDiaBaseProtEnablePeerConnectionDownNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7, 4),
    _CiscoDiaBaseProtEnablePeerConnectionDownNotif_Type()
)
ciscoDiaBaseProtEnablePeerConnectionDownNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoDiaBaseProtEnablePeerConnectionDownNotif.setStatus("current")


class _CiscoDiaBaseProtEnablePeerConnectionUpNotif_Type(TruthValue):
    """Custom type ciscoDiaBaseProtEnablePeerConnectionUpNotif based on TruthValue"""


_CiscoDiaBaseProtEnablePeerConnectionUpNotif_Object = MibScalar
ciscoDiaBaseProtEnablePeerConnectionUpNotif = _CiscoDiaBaseProtEnablePeerConnectionUpNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 1, 7, 5),
    _CiscoDiaBaseProtEnablePeerConnectionUpNotif_Type()
)
ciscoDiaBaseProtEnablePeerConnectionUpNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoDiaBaseProtEnablePeerConnectionUpNotif.setStatus("current")
_CiscoDiameterBasePMIBConform_ObjectIdentity = ObjectIdentity
ciscoDiameterBasePMIBConform = _CiscoDiameterBasePMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2)
)
_CiscoDiameterBasePMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDiameterBasePMIBCompliances = _CiscoDiameterBasePMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 1)
)
_CiscoDiameterBasePMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDiameterBasePMIBGroups = _CiscoDiameterBasePMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2)
)

# Managed Objects groups

ciscoDiameterBasePMIBLocalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 1)
)
ciscoDiameterBasePMIBLocalCfgGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalRealm"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRedundancyEnabled"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRedundancyInfraState"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRedundancyLastSwitchover"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalOriginHost"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalVendorId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalVendorStorageType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalVendorRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBLocalCfgGroup.setStatus("current")

ciscoDiameterBasePMIBPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 2)
)
ciscoDiameterBasePMIBPeerCfgGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerPortConnect"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerPortListen"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerProtocol"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerSecurity"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerFirmwareRevision"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStorageType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerRowStatus"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIpAddressType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIpAddress"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerVendorId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerVendorStorageType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerVendorRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBPeerCfgGroup.setStatus("current")

ciscoDiameterBasePMIBPeerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 3)
)
ciscoDiameterBasePMIBPeerStatsGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsState"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsStateDuration"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsLastDiscCause"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsWhoInitDisconnect"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWCurrentStatus"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsTimeoutConnAtmpts"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsASRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsASRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsASAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsASAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsACRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsACRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsACAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsACAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsCERsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsCERsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsCEAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsCEAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDPRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDPRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDPAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDPAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRARsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRARsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRAAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRAAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsSTRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsSTRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsSTAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsSTAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWReqTimer"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRedirectEvents"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccDupRequests"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsMalformedReqsts"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccsNotRecorded"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccRetrans"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsTotalRetrans"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccPendReqstsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccReqstsDropped"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsHByHDropMessages"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsEToEDupMessages"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsUnknownTypes"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsProtocolErrors"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsTransientFailures"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsPermanentFailures"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsTransportDown"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBPeerStatsGroup.setStatus("current")

ciscoDiameterBasePMIBTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 5)
)
ciscoDiameterBasePMIBTrapCfgGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtEnableProtocolErrorNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtEnableTransientFailureNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtEnablePermanentFailureNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtEnablePeerConnectionDownNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtEnablePeerConnectionUpNotif"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBTrapCfgGroup.setStatus("current")

ciscoDiameterBasePMIBLocalCfgSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 6)
)
ciscoDiameterBasePMIBLocalCfgSkippedGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalIpAddrType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalIpAddress"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalTcpListenPort"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalSctpListenPort"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalPacketsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalPacketsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalUpTime"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalResetTime"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalConfigReset"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalApplStorageType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalApplRowStatus"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvToPeerServices"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvToPeerStorageType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvToPeerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBLocalCfgSkippedGroup.setStatus("current")

ciscoDiameterBasePMIBLocalStatsSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 7)
)
ciscoDiameterBasePMIBLocalStatsSkippedGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalPacketsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalPacketsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalStatsTotalUpTime"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalResetTime"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalConfigReset"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBLocalStatsSkippedGroup.setStatus("current")

ciscoDiameterBasePMIBPeerCfgSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 8)
)
ciscoDiameterBasePMIBPeerCfgSkippedGroup.setObjects(
    ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpAppAdvFromPeerType")
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBPeerCfgSkippedGroup.setStatus("current")

ciscoDiameterBasePMIBPeerStatsSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 9)
)
ciscoDiameterBasePMIBPeerStatsSkippedGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWCurrentStatus"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsDWReqTimer"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsRedirectEvents"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsAccDupRequests"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsEToEDupMessages"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBPeerStatsSkippedGroup.setStatus("current")

ciscoDiameterBasePMIBRealmCfgSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 10)
)
ciscoDiameterBasePMIBRealmCfgSkippedGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmKnownPeers"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmKnownPeersChosen"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBRealmCfgSkippedGroup.setStatus("current")

ciscoDiameterBasePMIBRealmStatsSkippedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 11)
)
ciscoDiameterBasePMIBRealmStatsSkippedGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteRealm"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteApp"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteType"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteAction"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteACRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteACRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteACAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteACAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteRARsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteRARsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteRAAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteRAAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteSTRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteSTRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteSTAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteSTAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteASRsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteASRsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteASAsIn"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteASAsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteAccRetrans"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteAccDupReqsts"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRoutePendReqstsOut"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpRealmMessageRouteReqstsDrop"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBRealmStatsSkippedGroup.setStatus("current")


# Notification objects

ciscoDiaBaseProtProtocolErrorNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0, 1)
)
ciscoDiaBaseProtProtocolErrorNotif.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsProtocolErrors"))
)
if mibBuilder.loadTexts:
    ciscoDiaBaseProtProtocolErrorNotif.setStatus(
        "current"
    )

ciscoDiaBaseProtTransientFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0, 2)
)
ciscoDiaBaseProtTransientFailureNotif.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsTransientFailures"))
)
if mibBuilder.loadTexts:
    ciscoDiaBaseProtTransientFailureNotif.setStatus(
        "current"
    )

ciscoDiaBaseProtPermanentFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0, 3)
)
ciscoDiaBaseProtPermanentFailureNotif.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerStatsPermanentFailures"))
)
if mibBuilder.loadTexts:
    ciscoDiaBaseProtPermanentFailureNotif.setStatus(
        "current"
    )

ciscoDiaBaseProtPeerConnectionDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0, 4)
)
ciscoDiaBaseProtPeerConnectionDownNotif.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"))
)
if mibBuilder.loadTexts:
    ciscoDiaBaseProtPeerConnectionDownNotif.setStatus(
        "current"
    )

ciscoDiaBaseProtPeerConnectionUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 0, 5)
)
ciscoDiaBaseProtPeerConnectionUpNotif.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpLocalId"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerId"))
)
if mibBuilder.loadTexts:
    ciscoDiaBaseProtPeerConnectionUpNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoDiameterBasePMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 2, 4)
)
ciscoDiameterBasePMIBNotificationsGroup.setObjects(
      *(("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtProtocolErrorNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtTransientFailureNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtPermanentFailureNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtPeerConnectionDownNotif"),
        ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "ciscoDiaBaseProtPeerConnectionUpNotif"))
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDiameterBasePMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 133, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDiameterBasePMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIAMETER-BASE-PROTOCOL-MIB",
    **{"ciscoDiameterBasePMIB": ciscoDiameterBasePMIB,
       "ciscoDiameterBasePMIBNotifs": ciscoDiameterBasePMIBNotifs,
       "ciscoDiaBaseProtProtocolErrorNotif": ciscoDiaBaseProtProtocolErrorNotif,
       "ciscoDiaBaseProtTransientFailureNotif": ciscoDiaBaseProtTransientFailureNotif,
       "ciscoDiaBaseProtPermanentFailureNotif": ciscoDiaBaseProtPermanentFailureNotif,
       "ciscoDiaBaseProtPeerConnectionDownNotif": ciscoDiaBaseProtPeerConnectionDownNotif,
       "ciscoDiaBaseProtPeerConnectionUpNotif": ciscoDiaBaseProtPeerConnectionUpNotif,
       "ciscoDiameterBasePMIBObjects": ciscoDiameterBasePMIBObjects,
       "cdbpLocalCfgs": cdbpLocalCfgs,
       "cdbpLocalId": cdbpLocalId,
       "cdbpLocalIpAddrTable": cdbpLocalIpAddrTable,
       "cdbpLocalIpAddrEntry": cdbpLocalIpAddrEntry,
       "cdbpLocalIpAddrIndex": cdbpLocalIpAddrIndex,
       "cdbpLocalIpAddrType": cdbpLocalIpAddrType,
       "cdbpLocalIpAddress": cdbpLocalIpAddress,
       "cdbpLocalTcpListenPort": cdbpLocalTcpListenPort,
       "cdbpLocalSctpListenPort": cdbpLocalSctpListenPort,
       "cdbpLocalOriginHost": cdbpLocalOriginHost,
       "cdbpLocalRealm": cdbpLocalRealm,
       "cdbpRedundancyEnabled": cdbpRedundancyEnabled,
       "cdbpRedundancyInfraState": cdbpRedundancyInfraState,
       "cdbpRedundancyLastSwitchover": cdbpRedundancyLastSwitchover,
       "cdbpLocalApplTable": cdbpLocalApplTable,
       "cdbpLocalApplEntry": cdbpLocalApplEntry,
       "cdbpLocalApplIndex": cdbpLocalApplIndex,
       "cdbpLocalApplStorageType": cdbpLocalApplStorageType,
       "cdbpLocalApplRowStatus": cdbpLocalApplRowStatus,
       "cdbpLocalVendorTable": cdbpLocalVendorTable,
       "cdbpLocalVendorEntry": cdbpLocalVendorEntry,
       "cdbpLocalVendorIndex": cdbpLocalVendorIndex,
       "cdbpLocalVendorId": cdbpLocalVendorId,
       "cdbpLocalVendorStorageType": cdbpLocalVendorStorageType,
       "cdbpLocalVendorRowStatus": cdbpLocalVendorRowStatus,
       "cdbpAppAdvToPeerTable": cdbpAppAdvToPeerTable,
       "cdbpAppAdvToPeerEntry": cdbpAppAdvToPeerEntry,
       "cdbpAppAdvToPeerVendorId": cdbpAppAdvToPeerVendorId,
       "cdbpAppAdvToPeerIndex": cdbpAppAdvToPeerIndex,
       "cdbpAppAdvToPeerServices": cdbpAppAdvToPeerServices,
       "cdbpAppAdvToPeerStorageType": cdbpAppAdvToPeerStorageType,
       "cdbpAppAdvToPeerRowStatus": cdbpAppAdvToPeerRowStatus,
       "cdbpLocalStats": cdbpLocalStats,
       "cdbpLocalStatsTotalPacketsIn": cdbpLocalStatsTotalPacketsIn,
       "cdbpLocalStatsTotalPacketsOut": cdbpLocalStatsTotalPacketsOut,
       "cdbpLocalStatsTotalUpTime": cdbpLocalStatsTotalUpTime,
       "cdbpLocalResetTime": cdbpLocalResetTime,
       "cdbpLocalConfigReset": cdbpLocalConfigReset,
       "cdbpPeerCfgs": cdbpPeerCfgs,
       "cdbpPeerTable": cdbpPeerTable,
       "cdbpPeerEntry": cdbpPeerEntry,
       "cdbpPeerIndex": cdbpPeerIndex,
       "cdbpPeerId": cdbpPeerId,
       "cdbpPeerPortConnect": cdbpPeerPortConnect,
       "cdbpPeerPortListen": cdbpPeerPortListen,
       "cdbpPeerProtocol": cdbpPeerProtocol,
       "cdbpPeerSecurity": cdbpPeerSecurity,
       "cdbpPeerFirmwareRevision": cdbpPeerFirmwareRevision,
       "cdbpPeerStorageType": cdbpPeerStorageType,
       "cdbpPeerRowStatus": cdbpPeerRowStatus,
       "cdbpPeerIpAddrTable": cdbpPeerIpAddrTable,
       "cdbpPeerIpAddrEntry": cdbpPeerIpAddrEntry,
       "cdbpPeerIpAddressIndex": cdbpPeerIpAddressIndex,
       "cdbpPeerIpAddressType": cdbpPeerIpAddressType,
       "cdbpPeerIpAddress": cdbpPeerIpAddress,
       "cdbpAppAdvFromPeerTable": cdbpAppAdvFromPeerTable,
       "cdbpAppAdvFromPeerEntry": cdbpAppAdvFromPeerEntry,
       "cdbpAppAdvFromPeerVendorId": cdbpAppAdvFromPeerVendorId,
       "cdbpAppAdvFromPeerIndex": cdbpAppAdvFromPeerIndex,
       "cdbpAppAdvFromPeerType": cdbpAppAdvFromPeerType,
       "cdbpPeerVendorTable": cdbpPeerVendorTable,
       "cdbpPeerVendorEntry": cdbpPeerVendorEntry,
       "cdbpPeerVendorIndex": cdbpPeerVendorIndex,
       "cdbpPeerVendorId": cdbpPeerVendorId,
       "cdbpPeerVendorStorageType": cdbpPeerVendorStorageType,
       "cdbpPeerVendorRowStatus": cdbpPeerVendorRowStatus,
       "cdbpPeerStats": cdbpPeerStats,
       "cdbpPeerStatsTable": cdbpPeerStatsTable,
       "cdbpPeerStatsEntry": cdbpPeerStatsEntry,
       "cdbpPeerStatsState": cdbpPeerStatsState,
       "cdbpPeerStatsStateDuration": cdbpPeerStatsStateDuration,
       "cdbpPeerStatsLastDiscCause": cdbpPeerStatsLastDiscCause,
       "cdbpPeerStatsWhoInitDisconnect": cdbpPeerStatsWhoInitDisconnect,
       "cdbpPeerStatsDWCurrentStatus": cdbpPeerStatsDWCurrentStatus,
       "cdbpPeerStatsTimeoutConnAtmpts": cdbpPeerStatsTimeoutConnAtmpts,
       "cdbpPeerStatsASRsIn": cdbpPeerStatsASRsIn,
       "cdbpPeerStatsASRsOut": cdbpPeerStatsASRsOut,
       "cdbpPeerStatsASAsIn": cdbpPeerStatsASAsIn,
       "cdbpPeerStatsASAsOut": cdbpPeerStatsASAsOut,
       "cdbpPeerStatsACRsIn": cdbpPeerStatsACRsIn,
       "cdbpPeerStatsACRsOut": cdbpPeerStatsACRsOut,
       "cdbpPeerStatsACAsIn": cdbpPeerStatsACAsIn,
       "cdbpPeerStatsACAsOut": cdbpPeerStatsACAsOut,
       "cdbpPeerStatsCERsIn": cdbpPeerStatsCERsIn,
       "cdbpPeerStatsCERsOut": cdbpPeerStatsCERsOut,
       "cdbpPeerStatsCEAsIn": cdbpPeerStatsCEAsIn,
       "cdbpPeerStatsCEAsOut": cdbpPeerStatsCEAsOut,
       "cdbpPeerStatsDWRsIn": cdbpPeerStatsDWRsIn,
       "cdbpPeerStatsDWRsOut": cdbpPeerStatsDWRsOut,
       "cdbpPeerStatsDWAsIn": cdbpPeerStatsDWAsIn,
       "cdbpPeerStatsDWAsOut": cdbpPeerStatsDWAsOut,
       "cdbpPeerStatsDPRsIn": cdbpPeerStatsDPRsIn,
       "cdbpPeerStatsDPRsOut": cdbpPeerStatsDPRsOut,
       "cdbpPeerStatsDPAsIn": cdbpPeerStatsDPAsIn,
       "cdbpPeerStatsDPAsOut": cdbpPeerStatsDPAsOut,
       "cdbpPeerStatsRARsIn": cdbpPeerStatsRARsIn,
       "cdbpPeerStatsRARsOut": cdbpPeerStatsRARsOut,
       "cdbpPeerStatsRAAsIn": cdbpPeerStatsRAAsIn,
       "cdbpPeerStatsRAAsOut": cdbpPeerStatsRAAsOut,
       "cdbpPeerStatsSTRsIn": cdbpPeerStatsSTRsIn,
       "cdbpPeerStatsSTRsOut": cdbpPeerStatsSTRsOut,
       "cdbpPeerStatsSTAsIn": cdbpPeerStatsSTAsIn,
       "cdbpPeerStatsSTAsOut": cdbpPeerStatsSTAsOut,
       "cdbpPeerStatsDWReqTimer": cdbpPeerStatsDWReqTimer,
       "cdbpPeerStatsRedirectEvents": cdbpPeerStatsRedirectEvents,
       "cdbpPeerStatsAccDupRequests": cdbpPeerStatsAccDupRequests,
       "cdbpPeerStatsMalformedReqsts": cdbpPeerStatsMalformedReqsts,
       "cdbpPeerStatsAccsNotRecorded": cdbpPeerStatsAccsNotRecorded,
       "cdbpPeerStatsAccRetrans": cdbpPeerStatsAccRetrans,
       "cdbpPeerStatsTotalRetrans": cdbpPeerStatsTotalRetrans,
       "cdbpPeerStatsAccPendReqstsOut": cdbpPeerStatsAccPendReqstsOut,
       "cdbpPeerStatsAccReqstsDropped": cdbpPeerStatsAccReqstsDropped,
       "cdbpPeerStatsHByHDropMessages": cdbpPeerStatsHByHDropMessages,
       "cdbpPeerStatsEToEDupMessages": cdbpPeerStatsEToEDupMessages,
       "cdbpPeerStatsUnknownTypes": cdbpPeerStatsUnknownTypes,
       "cdbpPeerStatsProtocolErrors": cdbpPeerStatsProtocolErrors,
       "cdbpPeerStatsTransientFailures": cdbpPeerStatsTransientFailures,
       "cdbpPeerStatsPermanentFailures": cdbpPeerStatsPermanentFailures,
       "cdbpPeerStatsTransportDown": cdbpPeerStatsTransportDown,
       "cdbpRealmCfgs": cdbpRealmCfgs,
       "cdbpRealmKnownPeersTable": cdbpRealmKnownPeersTable,
       "cdbpRealmKnownPeersEntry": cdbpRealmKnownPeersEntry,
       "cdbpRealmKnownPeersIndex": cdbpRealmKnownPeersIndex,
       "cdbpRealmKnownPeers": cdbpRealmKnownPeers,
       "cdbpRealmKnownPeersChosen": cdbpRealmKnownPeersChosen,
       "cdbpRealmStats": cdbpRealmStats,
       "cdbpRealmMessageRouteTable": cdbpRealmMessageRouteTable,
       "cdbpRealmMessageRouteEntry": cdbpRealmMessageRouteEntry,
       "cdbpRealmMessageRouteIndex": cdbpRealmMessageRouteIndex,
       "cdbpRealmMessageRouteRealm": cdbpRealmMessageRouteRealm,
       "cdbpRealmMessageRouteApp": cdbpRealmMessageRouteApp,
       "cdbpRealmMessageRouteType": cdbpRealmMessageRouteType,
       "cdbpRealmMessageRouteAction": cdbpRealmMessageRouteAction,
       "cdbpRealmMessageRouteACRsIn": cdbpRealmMessageRouteACRsIn,
       "cdbpRealmMessageRouteACRsOut": cdbpRealmMessageRouteACRsOut,
       "cdbpRealmMessageRouteACAsIn": cdbpRealmMessageRouteACAsIn,
       "cdbpRealmMessageRouteACAsOut": cdbpRealmMessageRouteACAsOut,
       "cdbpRealmMessageRouteRARsIn": cdbpRealmMessageRouteRARsIn,
       "cdbpRealmMessageRouteRARsOut": cdbpRealmMessageRouteRARsOut,
       "cdbpRealmMessageRouteRAAsIn": cdbpRealmMessageRouteRAAsIn,
       "cdbpRealmMessageRouteRAAsOut": cdbpRealmMessageRouteRAAsOut,
       "cdbpRealmMessageRouteSTRsIn": cdbpRealmMessageRouteSTRsIn,
       "cdbpRealmMessageRouteSTRsOut": cdbpRealmMessageRouteSTRsOut,
       "cdbpRealmMessageRouteSTAsIn": cdbpRealmMessageRouteSTAsIn,
       "cdbpRealmMessageRouteSTAsOut": cdbpRealmMessageRouteSTAsOut,
       "cdbpRealmMessageRouteASRsIn": cdbpRealmMessageRouteASRsIn,
       "cdbpRealmMessageRouteASRsOut": cdbpRealmMessageRouteASRsOut,
       "cdbpRealmMessageRouteASAsIn": cdbpRealmMessageRouteASAsIn,
       "cdbpRealmMessageRouteASAsOut": cdbpRealmMessageRouteASAsOut,
       "cdbpRealmMessageRouteAccRetrans": cdbpRealmMessageRouteAccRetrans,
       "cdbpRealmMessageRouteAccDupReqsts": cdbpRealmMessageRouteAccDupReqsts,
       "cdbpRealmMessageRoutePendReqstsOut": cdbpRealmMessageRoutePendReqstsOut,
       "cdbpRealmMessageRouteReqstsDrop": cdbpRealmMessageRouteReqstsDrop,
       "cdbpTrapCfgs": cdbpTrapCfgs,
       "ciscoDiaBaseProtEnableProtocolErrorNotif": ciscoDiaBaseProtEnableProtocolErrorNotif,
       "ciscoDiaBaseProtEnableTransientFailureNotif": ciscoDiaBaseProtEnableTransientFailureNotif,
       "ciscoDiaBaseProtEnablePermanentFailureNotif": ciscoDiaBaseProtEnablePermanentFailureNotif,
       "ciscoDiaBaseProtEnablePeerConnectionDownNotif": ciscoDiaBaseProtEnablePeerConnectionDownNotif,
       "ciscoDiaBaseProtEnablePeerConnectionUpNotif": ciscoDiaBaseProtEnablePeerConnectionUpNotif,
       "ciscoDiameterBasePMIBConform": ciscoDiameterBasePMIBConform,
       "ciscoDiameterBasePMIBCompliances": ciscoDiameterBasePMIBCompliances,
       "ciscoDiameterBasePMIBCompliance": ciscoDiameterBasePMIBCompliance,
       "ciscoDiameterBasePMIBGroups": ciscoDiameterBasePMIBGroups,
       "ciscoDiameterBasePMIBLocalCfgGroup": ciscoDiameterBasePMIBLocalCfgGroup,
       "ciscoDiameterBasePMIBPeerCfgGroup": ciscoDiameterBasePMIBPeerCfgGroup,
       "ciscoDiameterBasePMIBPeerStatsGroup": ciscoDiameterBasePMIBPeerStatsGroup,
       "ciscoDiameterBasePMIBNotificationsGroup": ciscoDiameterBasePMIBNotificationsGroup,
       "ciscoDiameterBasePMIBTrapCfgGroup": ciscoDiameterBasePMIBTrapCfgGroup,
       "ciscoDiameterBasePMIBLocalCfgSkippedGroup": ciscoDiameterBasePMIBLocalCfgSkippedGroup,
       "ciscoDiameterBasePMIBLocalStatsSkippedGroup": ciscoDiameterBasePMIBLocalStatsSkippedGroup,
       "ciscoDiameterBasePMIBPeerCfgSkippedGroup": ciscoDiameterBasePMIBPeerCfgSkippedGroup,
       "ciscoDiameterBasePMIBPeerStatsSkippedGroup": ciscoDiameterBasePMIBPeerStatsSkippedGroup,
       "ciscoDiameterBasePMIBRealmCfgSkippedGroup": ciscoDiameterBasePMIBRealmCfgSkippedGroup,
       "ciscoDiameterBasePMIBRealmStatsSkippedGroup": ciscoDiameterBasePMIBRealmStatsSkippedGroup}
)
