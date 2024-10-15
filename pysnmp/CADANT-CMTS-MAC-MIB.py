# SNMP MIB module (CADANT-CMTS-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-MAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:31 2024
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

(CerOfdmModBitsType,
 OfdmProfileId) = mibBuilder.importSymbols(
    "CADANT-CMTS-DOWNCHANNEL-MIB",
    "CerOfdmModBitsType",
    "OfdmProfileId")

(cadIfMacDomainIfIndex,
 cadMacChlChannelIfIndex) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadIfMacDomainIfIndex",
    "cadMacChlChannelIfIndex")

(cadLayer2,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer2")

(CadCpeDeviceTypes,
 InetAddressIPv4or6,
 OUIAddress) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadCpeDeviceTypes",
    "InetAddressIPv4or6",
    "OUIAddress")

(DocsisQosVersion,
 DocsisUpstreamType,
 DocsisVersion,
 TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsisQosVersion",
    "DocsisUpstreamType",
    "DocsisVersion",
    "TenthdB",
    "TenthdBmV")

(ChSetId,
 IfDirection,
 RcpId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId",
    "IfDirection",
    "RcpId")

(BitRate,
 docsQosServiceClassEntry,
 docsQosServiceFlowId,
 docsQosServiceFlowSidClusterId) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "BitRate",
    "docsQosServiceClassEntry",
    "docsQosServiceFlowId",
    "docsQosServiceFlowSidClusterId")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

(ipNetToMediaEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadMacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2)
)
cadMacMib.setRevisions(
        ("2015-09-08 00:00",
         "2015-06-05 00:00",
         "2015-04-14 00:00",
         "2015-04-06 00:00",
         "2015-04-01 00:00",
         "2015-03-03 00:00",
         "2014-11-25 00:00",
         "2014-09-23 00:00",
         "2014-05-31 00:00",
         "2014-02-13 00:00",
         "2013-06-20 00:00",
         "2013-06-12 00:00",
         "2013-05-14 00:00",
         "2013-05-09 00:00",
         "2013-04-29 00:00",
         "2012-11-30 00:00",
         "2012-11-26 00:00",
         "2012-08-01 00:00",
         "2012-06-27 00:00",
         "2011-05-05 00:00",
         "2010-11-23 00:00",
         "2010-10-12 00:00",
         "2010-08-31 00:00",
         "2010-05-24 00:00",
         "2010-05-13 00:00",
         "2010-02-08 00:00",
         "2009-08-26 00:00",
         "2009-08-19 00:00",
         "2009-04-08 00:00",
         "2009-03-25 00:00",
         "2009-03-04 00:00",
         "2009-02-12 00:00",
         "2009-01-26 00:00",
         "2009-01-05 00:00",
         "2008-11-17 00:00",
         "2008-02-01 00:00",
         "2007-09-06 00:00",
         "2007-08-30 00:00",
         "2007-08-08 00:00",
         "2006-09-19 00:00",
         "2006-09-12 00:00",
         "2006-08-11 00:00",
         "2006-07-17 00:00",
         "2006-04-06 00:00",
         "2006-01-30 00:00",
         "2006-01-05 00:00",
         "2006-01-03 00:00",
         "2005-12-12 00:00",
         "2005-10-19 00:00",
         "2005-10-18 00:00",
         "2005-10-14 00:00",
         "2005-10-07 00:00",
         "2005-10-05 00:00",
         "2005-10-03 00:00",
         "2005-08-10 00:00",
         "2005-07-11 00:00",
         "2005-07-01 00:00",
         "2004-12-03 00:00",
         "2004-11-12 00:00",
         "2004-02-28 00:00",
         "2003-10-16 00:00",
         "2003-09-24 00:00",
         "2003-07-29 00:00",
         "2003-06-23 00:00",
         "2003-06-20 00:00",
         "2003-04-14 00:00",
         "2003-01-06 00:00",
         "2002-11-11 00:00",
         "2002-10-10 00:00",
         "2002-09-23 00:00",
         "2002-09-19 00:00",
         "2002-08-28 00:00",
         "2002-06-05 00:00",
         "2001-05-22 00:00",
         "2001-05-03 00:00",
         "2001-04-03 00:00",
         "2001-02-05 00:00",
         "2000-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadIfCmtsCmStatusType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              20)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("configFileComplete", 15),
          ("dhcpv6Complete", 13),
          ("forwardingDisabled", 17),
          ("ipComplete", 5),
          ("netAccessDisabled", 20),
          ("operational", 8),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registeredBPIInitializing", 9),
          ("registrationComplete", 6),
          ("rfMuteAll", 18),
          ("startConfigFileDownload", 14),
          ("startDhcpv4", 11),
          ("startDhcpv6", 12),
          ("startEae", 10))
    )



# MIB Managed Objects in the order of their OIDs

_CadIfCmtsCmStatusNumber_Type = Counter32
_CadIfCmtsCmStatusNumber_Object = MibScalar
cadIfCmtsCmStatusNumber = _CadIfCmtsCmStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 1),
    _CadIfCmtsCmStatusNumber_Type()
)
cadIfCmtsCmStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusNumber.setStatus("current")
_CadIfCmtsCmStatusTable_Object = MibTable
cadIfCmtsCmStatusTable = _CadIfCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2)
)
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusTable.setStatus("current")
_CadIfCmtsCmStatusEntry_Object = MibTableRow
cadIfCmtsCmStatusEntry = _CadIfCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1)
)
cadIfCmtsCmStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusEntry.setStatus("current")
_CadIfCmtsCmStatusMacAddress_Type = MacAddress
_CadIfCmtsCmStatusMacAddress_Object = MibTableColumn
cadIfCmtsCmStatusMacAddress = _CadIfCmtsCmStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 2),
    _CadIfCmtsCmStatusMacAddress_Type()
)
cadIfCmtsCmStatusMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusMacAddress.setStatus("current")
_CadIfCmtsCmStatusDownChannelIfIndex_Type = InterfaceIndexOrZero
_CadIfCmtsCmStatusDownChannelIfIndex_Object = MibTableColumn
cadIfCmtsCmStatusDownChannelIfIndex = _CadIfCmtsCmStatusDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 4),
    _CadIfCmtsCmStatusDownChannelIfIndex_Type()
)
cadIfCmtsCmStatusDownChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDownChannelIfIndex.setStatus("current")
_CadIfCmtsCmStatusUpChannelIfIndex_Type = InterfaceIndexOrZero
_CadIfCmtsCmStatusUpChannelIfIndex_Object = MibTableColumn
cadIfCmtsCmStatusUpChannelIfIndex = _CadIfCmtsCmStatusUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 5),
    _CadIfCmtsCmStatusUpChannelIfIndex_Type()
)
cadIfCmtsCmStatusUpChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusUpChannelIfIndex.setStatus("current")
_CadIfCmtsCmStatusValue_Type = CadIfCmtsCmStatusType
_CadIfCmtsCmStatusValue_Object = MibTableColumn
cadIfCmtsCmStatusValue = _CadIfCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 9),
    _CadIfCmtsCmStatusValue_Type()
)
cadIfCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusValue.setStatus("current")


class _CadIfCmtsCmStatusDocsisVersion_Type(DocsisVersion):
    """Custom type cadIfCmtsCmStatusDocsisVersion based on DocsisVersion"""


_CadIfCmtsCmStatusDocsisVersion_Object = MibTableColumn
cadIfCmtsCmStatusDocsisVersion = _CadIfCmtsCmStatusDocsisVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 12),
    _CadIfCmtsCmStatusDocsisVersion_Type()
)
cadIfCmtsCmStatusDocsisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDocsisVersion.setStatus("deprecated")
_CadIfCmtsCmStatusRangFlaps_Type = Counter32
_CadIfCmtsCmStatusRangFlaps_Object = MibTableColumn
cadIfCmtsCmStatusRangFlaps = _CadIfCmtsCmStatusRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 13),
    _CadIfCmtsCmStatusRangFlaps_Type()
)
cadIfCmtsCmStatusRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusRangFlaps.setStatus("current")
_CadIfCmtsCmStatusProvFlaps_Type = Counter32
_CadIfCmtsCmStatusProvFlaps_Object = MibTableColumn
cadIfCmtsCmStatusProvFlaps = _CadIfCmtsCmStatusProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 14),
    _CadIfCmtsCmStatusProvFlaps_Type()
)
cadIfCmtsCmStatusProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusProvFlaps.setStatus("current")
_CadIfCmtsCmStatusRegFlaps_Type = Counter32
_CadIfCmtsCmStatusRegFlaps_Object = MibTableColumn
cadIfCmtsCmStatusRegFlaps = _CadIfCmtsCmStatusRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 15),
    _CadIfCmtsCmStatusRegFlaps_Type()
)
cadIfCmtsCmStatusRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusRegFlaps.setStatus("current")


class _CadIfCmtsCmStatusLastFlapTime_Type(TimeStamp):
    """Custom type cadIfCmtsCmStatusLastFlapTime based on TimeStamp"""
    defaultValue = 0


_CadIfCmtsCmStatusLastFlapTime_Object = MibTableColumn
cadIfCmtsCmStatusLastFlapTime = _CadIfCmtsCmStatusLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 16),
    _CadIfCmtsCmStatusLastFlapTime_Type()
)
cadIfCmtsCmStatusLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusLastFlapTime.setStatus("current")


class _CadIfCmtsCmStatusInitRangTime_Type(TimeStamp):
    """Custom type cadIfCmtsCmStatusInitRangTime based on TimeStamp"""
    defaultValue = 0


_CadIfCmtsCmStatusInitRangTime_Object = MibTableColumn
cadIfCmtsCmStatusInitRangTime = _CadIfCmtsCmStatusInitRangTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 17),
    _CadIfCmtsCmStatusInitRangTime_Type()
)
cadIfCmtsCmStatusInitRangTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusInitRangTime.setStatus("current")


class _CadIfCmtsCmStatusPreFlapStatus_Type(CadIfCmtsCmStatusType):
    """Custom type cadIfCmtsCmStatusPreFlapStatus based on CadIfCmtsCmStatusType"""
    defaultValue = 1


_CadIfCmtsCmStatusPreFlapStatus_Object = MibTableColumn
cadIfCmtsCmStatusPreFlapStatus = _CadIfCmtsCmStatusPreFlapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 18),
    _CadIfCmtsCmStatusPreFlapStatus_Type()
)
cadIfCmtsCmStatusPreFlapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusPreFlapStatus.setStatus("current")
_CadIfCmtsCmStatusConfigFilename_Type = DisplayString
_CadIfCmtsCmStatusConfigFilename_Object = MibTableColumn
cadIfCmtsCmStatusConfigFilename = _CadIfCmtsCmStatusConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 19),
    _CadIfCmtsCmStatusConfigFilename_Type()
)
cadIfCmtsCmStatusConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusConfigFilename.setStatus("current")


class _CadIfCmtsCmStatusBpiVersion_Type(Integer32):
    """Custom type cadIfCmtsCmStatusBpiVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bpi", 0),
          ("bpiPlus", 1))
    )


_CadIfCmtsCmStatusBpiVersion_Type.__name__ = "Integer32"
_CadIfCmtsCmStatusBpiVersion_Object = MibTableColumn
cadIfCmtsCmStatusBpiVersion = _CadIfCmtsCmStatusBpiVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 20),
    _CadIfCmtsCmStatusBpiVersion_Type()
)
cadIfCmtsCmStatusBpiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusBpiVersion.setStatus("current")


class _CadIfCmtsCmStatusModemType_Type(Integer32):
    """Custom type cadIfCmtsCmStatusModemType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 3),
          ("mta", 2),
          ("standalone", 1),
          ("unknown", 0))
    )


_CadIfCmtsCmStatusModemType_Type.__name__ = "Integer32"
_CadIfCmtsCmStatusModemType_Object = MibTableColumn
cadIfCmtsCmStatusModemType = _CadIfCmtsCmStatusModemType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 21),
    _CadIfCmtsCmStatusModemType_Type()
)
cadIfCmtsCmStatusModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusModemType.setStatus("current")


class _CadIfCmtsCmStatusModulationType_Type(DocsisUpstreamType):
    """Custom type cadIfCmtsCmStatusModulationType based on DocsisUpstreamType"""


_CadIfCmtsCmStatusModulationType_Object = MibTableColumn
cadIfCmtsCmStatusModulationType = _CadIfCmtsCmStatusModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 22),
    _CadIfCmtsCmStatusModulationType_Type()
)
cadIfCmtsCmStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusModulationType.setStatus("current")


class _CadIfCmtsCmStatusCmPtr_Type(Integer32):
    """Custom type cadIfCmtsCmStatusCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadIfCmtsCmStatusCmPtr_Type.__name__ = "Integer32"
_CadIfCmtsCmStatusCmPtr_Object = MibTableColumn
cadIfCmtsCmStatusCmPtr = _CadIfCmtsCmStatusCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 23),
    _CadIfCmtsCmStatusCmPtr_Type()
)
cadIfCmtsCmStatusCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusCmPtr.setStatus("current")


class _CadIfCmtsCmStatusTftpEnforceFailed_Type(TruthValue):
    """Custom type cadIfCmtsCmStatusTftpEnforceFailed based on TruthValue"""


_CadIfCmtsCmStatusTftpEnforceFailed_Object = MibTableColumn
cadIfCmtsCmStatusTftpEnforceFailed = _CadIfCmtsCmStatusTftpEnforceFailed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 24),
    _CadIfCmtsCmStatusTftpEnforceFailed_Type()
)
cadIfCmtsCmStatusTftpEnforceFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusTftpEnforceFailed.setStatus("current")


class _CadIfCmtsCmStatusDynamicSecretFailed_Type(TruthValue):
    """Custom type cadIfCmtsCmStatusDynamicSecretFailed based on TruthValue"""


_CadIfCmtsCmStatusDynamicSecretFailed_Object = MibTableColumn
cadIfCmtsCmStatusDynamicSecretFailed = _CadIfCmtsCmStatusDynamicSecretFailed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 25),
    _CadIfCmtsCmStatusDynamicSecretFailed_Type()
)
cadIfCmtsCmStatusDynamicSecretFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDynamicSecretFailed.setStatus("current")


class _CadIfCmtsCmStatusDocsCapability_Type(DocsisVersion):
    """Custom type cadIfCmtsCmStatusDocsCapability based on DocsisVersion"""


_CadIfCmtsCmStatusDocsCapability_Object = MibTableColumn
cadIfCmtsCmStatusDocsCapability = _CadIfCmtsCmStatusDocsCapability_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 26),
    _CadIfCmtsCmStatusDocsCapability_Type()
)
cadIfCmtsCmStatusDocsCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDocsCapability.setStatus("current")


class _CadIfCmtsCmStatusDocsProvisioned_Type(DocsisVersion):
    """Custom type cadIfCmtsCmStatusDocsProvisioned based on DocsisVersion"""


_CadIfCmtsCmStatusDocsProvisioned_Object = MibTableColumn
cadIfCmtsCmStatusDocsProvisioned = _CadIfCmtsCmStatusDocsProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 27),
    _CadIfCmtsCmStatusDocsProvisioned_Type()
)
cadIfCmtsCmStatusDocsProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDocsProvisioned.setStatus("current")
_CadIfHVCmtsCmStatusLastFlapTime_Type = Counter64
_CadIfHVCmtsCmStatusLastFlapTime_Object = MibTableColumn
cadIfHVCmtsCmStatusLastFlapTime = _CadIfHVCmtsCmStatusLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 28),
    _CadIfHVCmtsCmStatusLastFlapTime_Type()
)
cadIfHVCmtsCmStatusLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfHVCmtsCmStatusLastFlapTime.setStatus("current")
_CadIfHVCmtsCmStatusInitRangTime_Type = Counter64
_CadIfHVCmtsCmStatusInitRangTime_Object = MibTableColumn
cadIfHVCmtsCmStatusInitRangTime = _CadIfHVCmtsCmStatusInitRangTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 29),
    _CadIfHVCmtsCmStatusInitRangTime_Type()
)
cadIfHVCmtsCmStatusInitRangTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfHVCmtsCmStatusInitRangTime.setStatus("current")
_CadIf3CmtsCmRegStatusIPv6Addr_Type = InetAddressIPv6
_CadIf3CmtsCmRegStatusIPv6Addr_Object = MibTableColumn
cadIf3CmtsCmRegStatusIPv6Addr = _CadIf3CmtsCmRegStatusIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 30),
    _CadIf3CmtsCmRegStatusIPv6Addr_Type()
)
cadIf3CmtsCmRegStatusIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusIPv6Addr.setStatus("current")
_CadIf3CmtsCmRegStatusIPv6LinkLocal_Type = InetAddressIPv6
_CadIf3CmtsCmRegStatusIPv6LinkLocal_Object = MibTableColumn
cadIf3CmtsCmRegStatusIPv6LinkLocal = _CadIf3CmtsCmRegStatusIPv6LinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 31),
    _CadIf3CmtsCmRegStatusIPv6LinkLocal_Type()
)
cadIf3CmtsCmRegStatusIPv6LinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusIPv6LinkLocal.setStatus("current")
_CadIf3CmtsCmRegStatusMdIfIndex_Type = InterfaceIndexOrZero
_CadIf3CmtsCmRegStatusMdIfIndex_Object = MibTableColumn
cadIf3CmtsCmRegStatusMdIfIndex = _CadIf3CmtsCmRegStatusMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 32),
    _CadIf3CmtsCmRegStatusMdIfIndex_Type()
)
cadIf3CmtsCmRegStatusMdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusMdIfIndex.setStatus("current")


class _CadIf3CmtsCmRegStatusMdCmSgId_Type(Unsigned32):
    """Custom type cadIf3CmtsCmRegStatusMdCmSgId based on Unsigned32"""
    defaultValue = 0


_CadIf3CmtsCmRegStatusMdCmSgId_Object = MibTableColumn
cadIf3CmtsCmRegStatusMdCmSgId = _CadIf3CmtsCmRegStatusMdCmSgId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 33),
    _CadIf3CmtsCmRegStatusMdCmSgId_Type()
)
cadIf3CmtsCmRegStatusMdCmSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusMdCmSgId.setStatus("current")


class _CadIf3CmtsCmRegStatusRcpId_Type(RcpId):
    """Custom type cadIf3CmtsCmRegStatusRcpId based on RcpId"""
    defaultHexValue = "0000000000"


_CadIf3CmtsCmRegStatusRcpId_Object = MibTableColumn
cadIf3CmtsCmRegStatusRcpId = _CadIf3CmtsCmRegStatusRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 34),
    _CadIf3CmtsCmRegStatusRcpId_Type()
)
cadIf3CmtsCmRegStatusRcpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusRcpId.setStatus("current")


class _CadIf3CmtsCmRegStatusRccStatusId_Type(Unsigned32):
    """Custom type cadIf3CmtsCmRegStatusRccStatusId based on Unsigned32"""
    defaultValue = 0


_CadIf3CmtsCmRegStatusRccStatusId_Object = MibTableColumn
cadIf3CmtsCmRegStatusRccStatusId = _CadIf3CmtsCmRegStatusRccStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 35),
    _CadIf3CmtsCmRegStatusRccStatusId_Type()
)
cadIf3CmtsCmRegStatusRccStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusRccStatusId.setStatus("current")
_CadIf3CmtsCmRegStatusRcsId_Type = ChSetId
_CadIf3CmtsCmRegStatusRcsId_Object = MibTableColumn
cadIf3CmtsCmRegStatusRcsId = _CadIf3CmtsCmRegStatusRcsId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 36),
    _CadIf3CmtsCmRegStatusRcsId_Type()
)
cadIf3CmtsCmRegStatusRcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusRcsId.setStatus("current")
_CadIf3CmtsCmRegStatusTcsId_Type = ChSetId
_CadIf3CmtsCmRegStatusTcsId_Object = MibTableColumn
cadIf3CmtsCmRegStatusTcsId = _CadIf3CmtsCmRegStatusTcsId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 37),
    _CadIf3CmtsCmRegStatusTcsId_Type()
)
cadIf3CmtsCmRegStatusTcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusTcsId.setStatus("current")
_CadIf3CmtsCmRegStatusLastRegTime_Type = DateAndTime
_CadIf3CmtsCmRegStatusLastRegTime_Object = MibTableColumn
cadIf3CmtsCmRegStatusLastRegTime = _CadIf3CmtsCmRegStatusLastRegTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 38),
    _CadIf3CmtsCmRegStatusLastRegTime_Type()
)
cadIf3CmtsCmRegStatusLastRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusLastRegTime.setStatus("current")


class _CadIfCmtsCmStatusInetIpAddrType_Type(InetAddressType):
    """Custom type cadIfCmtsCmStatusInetIpAddrType based on InetAddressType"""


_CadIfCmtsCmStatusInetIpAddrType_Object = MibTableColumn
cadIfCmtsCmStatusInetIpAddrType = _CadIfCmtsCmStatusInetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 39),
    _CadIfCmtsCmStatusInetIpAddrType_Type()
)
cadIfCmtsCmStatusInetIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusInetIpAddrType.setStatus("current")


class _CadIfCmtsCmStatusInetIpAddress_Type(InetAddressIPv4or6):
    """Custom type cadIfCmtsCmStatusInetIpAddress based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadIfCmtsCmStatusInetIpAddress_Object = MibTableColumn
cadIfCmtsCmStatusInetIpAddress = _CadIfCmtsCmStatusInetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 40),
    _CadIfCmtsCmStatusInetIpAddress_Type()
)
cadIfCmtsCmStatusInetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusInetIpAddress.setStatus("current")
_CadIf3CmtsCmRegStatusServiceType_Type = DocsisQosVersion
_CadIf3CmtsCmRegStatusServiceType_Object = MibTableColumn
cadIf3CmtsCmRegStatusServiceType = _CadIf3CmtsCmRegStatusServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 41),
    _CadIf3CmtsCmRegStatusServiceType_Type()
)
cadIf3CmtsCmRegStatusServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusServiceType.setStatus("current")


class _CadIfCmtsCmStatusBpiEnabled_Type(TruthValue):
    """Custom type cadIfCmtsCmStatusBpiEnabled based on TruthValue"""


_CadIfCmtsCmStatusBpiEnabled_Object = MibTableColumn
cadIfCmtsCmStatusBpiEnabled = _CadIfCmtsCmStatusBpiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 42),
    _CadIfCmtsCmStatusBpiEnabled_Type()
)
cadIfCmtsCmStatusBpiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusBpiEnabled.setStatus("current")


class _CadIfCmtsCmStatuseDocsisTypes_Type(CadCpeDeviceTypes):
    """Custom type cadIfCmtsCmStatuseDocsisTypes based on CadCpeDeviceTypes"""
    defaultBinValue = "0"


_CadIfCmtsCmStatuseDocsisTypes_Object = MibTableColumn
cadIfCmtsCmStatuseDocsisTypes = _CadIfCmtsCmStatuseDocsisTypes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 43),
    _CadIfCmtsCmStatuseDocsisTypes_Type()
)
cadIfCmtsCmStatuseDocsisTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatuseDocsisTypes.setStatus("current")
_CadIfCmtsCmStatusDsPenalties_Type = Counter32
_CadIfCmtsCmStatusDsPenalties_Object = MibTableColumn
cadIfCmtsCmStatusDsPenalties = _CadIfCmtsCmStatusDsPenalties_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 44),
    _CadIfCmtsCmStatusDsPenalties_Type()
)
cadIfCmtsCmStatusDsPenalties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusDsPenalties.setStatus("current")
_CadIfCmtsCmStatusUsPenalties_Type = Counter32
_CadIfCmtsCmStatusUsPenalties_Object = MibTableColumn
cadIfCmtsCmStatusUsPenalties = _CadIfCmtsCmStatusUsPenalties_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 45),
    _CadIfCmtsCmStatusUsPenalties_Type()
)
cadIfCmtsCmStatusUsPenalties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusUsPenalties.setStatus("current")
_CadIfCmtsCmStatusLastDsPenaltyStart_Type = Counter32
_CadIfCmtsCmStatusLastDsPenaltyStart_Object = MibTableColumn
cadIfCmtsCmStatusLastDsPenaltyStart = _CadIfCmtsCmStatusLastDsPenaltyStart_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 46),
    _CadIfCmtsCmStatusLastDsPenaltyStart_Type()
)
cadIfCmtsCmStatusLastDsPenaltyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusLastDsPenaltyStart.setStatus("current")
_CadIfCmtsCmStatusLastDsPenaltyDuration_Type = Counter32
_CadIfCmtsCmStatusLastDsPenaltyDuration_Object = MibTableColumn
cadIfCmtsCmStatusLastDsPenaltyDuration = _CadIfCmtsCmStatusLastDsPenaltyDuration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 47),
    _CadIfCmtsCmStatusLastDsPenaltyDuration_Type()
)
cadIfCmtsCmStatusLastDsPenaltyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusLastDsPenaltyDuration.setStatus("current")
_CadIfCmtsCmStatusLastUsPenaltyStart_Type = Counter32
_CadIfCmtsCmStatusLastUsPenaltyStart_Object = MibTableColumn
cadIfCmtsCmStatusLastUsPenaltyStart = _CadIfCmtsCmStatusLastUsPenaltyStart_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 48),
    _CadIfCmtsCmStatusLastUsPenaltyStart_Type()
)
cadIfCmtsCmStatusLastUsPenaltyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusLastUsPenaltyStart.setStatus("current")
_CadIfCmtsCmStatusLastUsPenaltyDuration_Type = Counter32
_CadIfCmtsCmStatusLastUsPenaltyDuration_Object = MibTableColumn
cadIfCmtsCmStatusLastUsPenaltyDuration = _CadIfCmtsCmStatusLastUsPenaltyDuration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 49),
    _CadIfCmtsCmStatusLastUsPenaltyDuration_Type()
)
cadIfCmtsCmStatusLastUsPenaltyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusLastUsPenaltyDuration.setStatus("current")


class _CadIfCmtsCmStatusRxAcPowerLost_Type(TruthValue):
    """Custom type cadIfCmtsCmStatusRxAcPowerLost based on TruthValue"""


_CadIfCmtsCmStatusRxAcPowerLost_Object = MibTableColumn
cadIfCmtsCmStatusRxAcPowerLost = _CadIfCmtsCmStatusRxAcPowerLost_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 50),
    _CadIfCmtsCmStatusRxAcPowerLost_Type()
)
cadIfCmtsCmStatusRxAcPowerLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusRxAcPowerLost.setStatus("current")
_CadIfCmtsCmStatusInsertionFlaps_Type = Counter32
_CadIfCmtsCmStatusInsertionFlaps_Object = MibTableColumn
cadIfCmtsCmStatusInsertionFlaps = _CadIfCmtsCmStatusInsertionFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 51),
    _CadIfCmtsCmStatusInsertionFlaps_Type()
)
cadIfCmtsCmStatusInsertionFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmStatusInsertionFlaps.setStatus("current")


class _CadIf3CmtsCmRegStatusEnergyMgtCapability_Type(Bits):
    """Custom type cadIf3CmtsCmRegStatusEnergyMgtCapability based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("em1x1Mode", 0)
    )

_CadIf3CmtsCmRegStatusEnergyMgtCapability_Type.__name__ = "Bits"
_CadIf3CmtsCmRegStatusEnergyMgtCapability_Object = MibTableColumn
cadIf3CmtsCmRegStatusEnergyMgtCapability = _CadIf3CmtsCmRegStatusEnergyMgtCapability_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 52),
    _CadIf3CmtsCmRegStatusEnergyMgtCapability_Type()
)
cadIf3CmtsCmRegStatusEnergyMgtCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusEnergyMgtCapability.setStatus("current")


class _CadIf3CmtsCmRegStatusEnergyMgtEnabled_Type(Bits):
    """Custom type cadIf3CmtsCmRegStatusEnergyMgtEnabled based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("em1x1Mode", 0)
    )

_CadIf3CmtsCmRegStatusEnergyMgtEnabled_Type.__name__ = "Bits"
_CadIf3CmtsCmRegStatusEnergyMgtEnabled_Object = MibTableColumn
cadIf3CmtsCmRegStatusEnergyMgtEnabled = _CadIf3CmtsCmRegStatusEnergyMgtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 53),
    _CadIf3CmtsCmRegStatusEnergyMgtEnabled_Type()
)
cadIf3CmtsCmRegStatusEnergyMgtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusEnergyMgtEnabled.setStatus("current")


class _CadIf3CmtsCmRegStatusEnergyMgtOperStatus_Type(Bits):
    """Custom type cadIf3CmtsCmRegStatusEnergyMgtOperStatus based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("em1x1Mode", 0)
    )

_CadIf3CmtsCmRegStatusEnergyMgtOperStatus_Type.__name__ = "Bits"
_CadIf3CmtsCmRegStatusEnergyMgtOperStatus_Object = MibTableColumn
cadIf3CmtsCmRegStatusEnergyMgtOperStatus = _CadIf3CmtsCmRegStatusEnergyMgtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 54),
    _CadIf3CmtsCmRegStatusEnergyMgtOperStatus_Type()
)
cadIf3CmtsCmRegStatusEnergyMgtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmRegStatusEnergyMgtOperStatus.setStatus("current")


class _CadIf3CmtsCmStatsEm1x1ModeTotalDuration_Type(Unsigned32):
    """Custom type cadIf3CmtsCmStatsEm1x1ModeTotalDuration based on Unsigned32"""
    defaultValue = 0


_CadIf3CmtsCmStatsEm1x1ModeTotalDuration_Object = MibTableColumn
cadIf3CmtsCmStatsEm1x1ModeTotalDuration = _CadIf3CmtsCmStatsEm1x1ModeTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 55),
    _CadIf3CmtsCmStatsEm1x1ModeTotalDuration_Type()
)
cadIf3CmtsCmStatsEm1x1ModeTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmStatsEm1x1ModeTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    cadIf3CmtsCmStatsEm1x1ModeTotalDuration.setUnits("seconds")


class _CadIf3CmtsCmStatsEm1x1ModeEntryTime_Type(Unsigned32):
    """Custom type cadIf3CmtsCmStatsEm1x1ModeEntryTime based on Unsigned32"""
    defaultValue = 0


_CadIf3CmtsCmStatsEm1x1ModeEntryTime_Object = MibTableColumn
cadIf3CmtsCmStatsEm1x1ModeEntryTime = _CadIf3CmtsCmStatsEm1x1ModeEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 2, 1, 56),
    _CadIf3CmtsCmStatsEm1x1ModeEntryTime_Type()
)
cadIf3CmtsCmStatsEm1x1ModeEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmStatsEm1x1ModeEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    cadIf3CmtsCmStatsEm1x1ModeEntryTime.setUnits("seconds")
_CadIfCmtsCmCountsTable_Object = MibTable
cadIfCmtsCmCountsTable = _CadIfCmtsCmCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3)
)
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsTable.setStatus("current")
_CadIfCmtsCmCountsEntry_Object = MibTableRow
cadIfCmtsCmCountsEntry = _CadIfCmtsCmCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1)
)
cadIfCmtsCmCountsEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmCountsUpChIfIndex"),
)
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsEntry.setStatus("current")
_CadIfCmtsCmCountsRxPower_Type = TenthdBmV
_CadIfCmtsCmCountsRxPower_Object = MibTableColumn
cadIfCmtsCmCountsRxPower = _CadIfCmtsCmCountsRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 1),
    _CadIfCmtsCmCountsRxPower_Type()
)
cadIfCmtsCmCountsRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsRxPower.setUnits("dBmV")
_CadIfCmtsCmCountsTimingOffset_Type = Integer32
_CadIfCmtsCmCountsTimingOffset_Object = MibTableColumn
cadIfCmtsCmCountsTimingOffset = _CadIfCmtsCmCountsTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 2),
    _CadIfCmtsCmCountsTimingOffset_Type()
)
cadIfCmtsCmCountsTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsTimingOffset.setStatus("current")
_CadIfCmtsCmCountsEqualizationData_Type = OctetString
_CadIfCmtsCmCountsEqualizationData_Object = MibTableColumn
cadIfCmtsCmCountsEqualizationData = _CadIfCmtsCmCountsEqualizationData_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 3),
    _CadIfCmtsCmCountsEqualizationData_Type()
)
cadIfCmtsCmCountsEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsEqualizationData.setStatus("current")
_CadIfCmtsCmCountsRangeReqOpportunities_Type = Counter32
_CadIfCmtsCmCountsRangeReqOpportunities_Object = MibTableColumn
cadIfCmtsCmCountsRangeReqOpportunities = _CadIfCmtsCmCountsRangeReqOpportunities_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 4),
    _CadIfCmtsCmCountsRangeReqOpportunities_Type()
)
cadIfCmtsCmCountsRangeReqOpportunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsRangeReqOpportunities.setStatus("current")
_CadIfCmtsCmCountsRangeReqReceived_Type = Counter32
_CadIfCmtsCmCountsRangeReqReceived_Object = MibTableColumn
cadIfCmtsCmCountsRangeReqReceived = _CadIfCmtsCmCountsRangeReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 5),
    _CadIfCmtsCmCountsRangeReqReceived_Type()
)
cadIfCmtsCmCountsRangeReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsRangeReqReceived.setStatus("current")
_CadIfCmtsCmCountsPowerAdjExceedsThreshold_Type = Counter32
_CadIfCmtsCmCountsPowerAdjExceedsThreshold_Object = MibTableColumn
cadIfCmtsCmCountsPowerAdjExceedsThreshold = _CadIfCmtsCmCountsPowerAdjExceedsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 6),
    _CadIfCmtsCmCountsPowerAdjExceedsThreshold_Type()
)
cadIfCmtsCmCountsPowerAdjExceedsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsPowerAdjExceedsThreshold.setStatus("current")
_CadIfCmtsCmCountsUpChIfIndex_Type = InterfaceIndex
_CadIfCmtsCmCountsUpChIfIndex_Object = MibTableColumn
cadIfCmtsCmCountsUpChIfIndex = _CadIfCmtsCmCountsUpChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 7),
    _CadIfCmtsCmCountsUpChIfIndex_Type()
)
cadIfCmtsCmCountsUpChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsUpChIfIndex.setStatus("current")
_CadIfCmtsCmCountsSignalNoise_Type = TenthdB
_CadIfCmtsCmCountsSignalNoise_Object = MibTableColumn
cadIfCmtsCmCountsSignalNoise = _CadIfCmtsCmCountsSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 8),
    _CadIfCmtsCmCountsSignalNoise_Type()
)
cadIfCmtsCmCountsSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsSignalNoise.setUnits("TenthdB")
_CadIfCmtsCmCountsUnerroreds_Type = Counter32
_CadIfCmtsCmCountsUnerroreds_Object = MibTableColumn
cadIfCmtsCmCountsUnerroreds = _CadIfCmtsCmCountsUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 9),
    _CadIfCmtsCmCountsUnerroreds_Type()
)
cadIfCmtsCmCountsUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsUnerroreds.setStatus("current")
_CadIfCmtsCmCountsCorrecteds_Type = Counter32
_CadIfCmtsCmCountsCorrecteds_Object = MibTableColumn
cadIfCmtsCmCountsCorrecteds = _CadIfCmtsCmCountsCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 10),
    _CadIfCmtsCmCountsCorrecteds_Type()
)
cadIfCmtsCmCountsCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsCorrecteds.setStatus("current")
_CadIfCmtsCmCountsUncorrectables_Type = Counter32
_CadIfCmtsCmCountsUncorrectables_Object = MibTableColumn
cadIfCmtsCmCountsUncorrectables = _CadIfCmtsCmCountsUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 11),
    _CadIfCmtsCmCountsUncorrectables_Type()
)
cadIfCmtsCmCountsUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsUncorrectables.setStatus("current")
_CadIfCmtsCmCountsTxPower_Type = Counter32
_CadIfCmtsCmCountsTxPower_Object = MibTableColumn
cadIfCmtsCmCountsTxPower = _CadIfCmtsCmCountsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 3, 1, 12),
    _CadIfCmtsCmCountsTxPower_Type()
)
cadIfCmtsCmCountsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmCountsTxPower.setStatus("current")
_CadIfCmtsServiceTable_Object = MibTable
cadIfCmtsServiceTable = _CadIfCmtsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4)
)
if mibBuilder.loadTexts:
    cadIfCmtsServiceTable.setStatus("current")
_CadIfCmtsServiceEntry_Object = MibTableRow
cadIfCmtsServiceEntry = _CadIfCmtsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1)
)
cadIfCmtsServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsServiceId"),
)
if mibBuilder.loadTexts:
    cadIfCmtsServiceEntry.setStatus("current")


class _CadIfCmtsServiceId_Type(Integer32):
    """Custom type cadIfCmtsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CadIfCmtsServiceId_Type.__name__ = "Integer32"
_CadIfCmtsServiceId_Object = MibTableColumn
cadIfCmtsServiceId = _CadIfCmtsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 1),
    _CadIfCmtsServiceId_Type()
)
cadIfCmtsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsServiceId.setStatus("current")
_CadIfCmtsServiceMacAddress_Type = MacAddress
_CadIfCmtsServiceMacAddress_Object = MibTableColumn
cadIfCmtsServiceMacAddress = _CadIfCmtsServiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 2),
    _CadIfCmtsServiceMacAddress_Type()
)
cadIfCmtsServiceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsServiceMacAddress.setStatus("current")


class _CadIfCmtsServiceAdminStatus_Type(Integer32):
    """Custom type cadIfCmtsServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destroyed", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_CadIfCmtsServiceAdminStatus_Type.__name__ = "Integer32"
_CadIfCmtsServiceAdminStatus_Object = MibTableColumn
cadIfCmtsServiceAdminStatus = _CadIfCmtsServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 3),
    _CadIfCmtsServiceAdminStatus_Type()
)
cadIfCmtsServiceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsServiceAdminStatus.setStatus("current")


class _CadIfCmtsServiceQosProfile_Type(Integer32):
    """Custom type cadIfCmtsServiceQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CadIfCmtsServiceQosProfile_Type.__name__ = "Integer32"
_CadIfCmtsServiceQosProfile_Object = MibTableColumn
cadIfCmtsServiceQosProfile = _CadIfCmtsServiceQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 4),
    _CadIfCmtsServiceQosProfile_Type()
)
cadIfCmtsServiceQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsServiceQosProfile.setStatus("current")
_CadIfCmtsServiceCreateTime_Type = TimeStamp
_CadIfCmtsServiceCreateTime_Object = MibTableColumn
cadIfCmtsServiceCreateTime = _CadIfCmtsServiceCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 5),
    _CadIfCmtsServiceCreateTime_Type()
)
cadIfCmtsServiceCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsServiceCreateTime.setStatus("current")


class _CadIfQosProfPriority_Type(Integer32):
    """Custom type cadIfQosProfPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CadIfQosProfPriority_Type.__name__ = "Integer32"
_CadIfQosProfPriority_Object = MibTableColumn
cadIfQosProfPriority = _CadIfQosProfPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 8),
    _CadIfQosProfPriority_Type()
)
cadIfQosProfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfPriority.setStatus("current")


class _CadIfQosProfMaxUpBandwidth_Type(Integer32):
    """Custom type cadIfQosProfMaxUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CadIfQosProfMaxUpBandwidth_Type.__name__ = "Integer32"
_CadIfQosProfMaxUpBandwidth_Object = MibTableColumn
cadIfQosProfMaxUpBandwidth = _CadIfQosProfMaxUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 9),
    _CadIfQosProfMaxUpBandwidth_Type()
)
cadIfQosProfMaxUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfMaxUpBandwidth.setStatus("current")


class _CadIfQosProfGuarUpBandwidth_Type(Integer32):
    """Custom type cadIfQosProfGuarUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CadIfQosProfGuarUpBandwidth_Type.__name__ = "Integer32"
_CadIfQosProfGuarUpBandwidth_Object = MibTableColumn
cadIfQosProfGuarUpBandwidth = _CadIfQosProfGuarUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 10),
    _CadIfQosProfGuarUpBandwidth_Type()
)
cadIfQosProfGuarUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfGuarUpBandwidth.setStatus("current")


class _CadIfQosProfMaxDownBandwidth_Type(Integer32):
    """Custom type cadIfQosProfMaxDownBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CadIfQosProfMaxDownBandwidth_Type.__name__ = "Integer32"
_CadIfQosProfMaxDownBandwidth_Object = MibTableColumn
cadIfQosProfMaxDownBandwidth = _CadIfQosProfMaxDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 11),
    _CadIfQosProfMaxDownBandwidth_Type()
)
cadIfQosProfMaxDownBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfMaxDownBandwidth.setStatus("current")


class _CadIfQosProfMaxTxBurst_Type(Integer32):
    """Custom type cadIfQosProfMaxTxBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadIfQosProfMaxTxBurst_Type.__name__ = "Integer32"
_CadIfQosProfMaxTxBurst_Object = MibTableColumn
cadIfQosProfMaxTxBurst = _CadIfQosProfMaxTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 12),
    _CadIfQosProfMaxTxBurst_Type()
)
cadIfQosProfMaxTxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfMaxTxBurst.setStatus("current")


class _CadIfQosProfBaselinePrivacy_Type(TruthValue):
    """Custom type cadIfQosProfBaselinePrivacy based on TruthValue"""


_CadIfQosProfBaselinePrivacy_Object = MibTableColumn
cadIfQosProfBaselinePrivacy = _CadIfQosProfBaselinePrivacy_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 4, 1, 13),
    _CadIfQosProfBaselinePrivacy_Type()
)
cadIfQosProfBaselinePrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfBaselinePrivacy.setStatus("current")
_CadIfCmtsPtrToMacTable_Object = MibTable
cadIfCmtsPtrToMacTable = _CadIfCmtsPtrToMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 5)
)
if mibBuilder.loadTexts:
    cadIfCmtsPtrToMacTable.setStatus("current")
_CadIfCmtsPtrToMacEntry_Object = MibTableRow
cadIfCmtsPtrToMacEntry = _CadIfCmtsPtrToMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 5, 1)
)
cadIfCmtsPtrToMacEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmPtr"),
)
if mibBuilder.loadTexts:
    cadIfCmtsPtrToMacEntry.setStatus("current")


class _CadIfCmtsCmPtr_Type(Integer32):
    """Custom type cadIfCmtsCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadIfCmtsCmPtr_Type.__name__ = "Integer32"
_CadIfCmtsCmPtr_Object = MibTableColumn
cadIfCmtsCmPtr = _CadIfCmtsCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 5, 1, 1),
    _CadIfCmtsCmPtr_Type()
)
cadIfCmtsCmPtr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmPtr.setStatus("current")
_CadIfCmtsCmMac_Type = MacAddress
_CadIfCmtsCmMac_Object = MibTableColumn
cadIfCmtsCmMac = _CadIfCmtsCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 5, 1, 2),
    _CadIfCmtsCmMac_Type()
)
cadIfCmtsCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmMac.setStatus("current")
_CadSubMgtCpeControlTable_Object = MibTable
cadSubMgtCpeControlTable = _CadSubMgtCpeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6)
)
if mibBuilder.loadTexts:
    cadSubMgtCpeControlTable.setStatus("current")
_CadSubMgtCpeControlEntry_Object = MibTableRow
cadSubMgtCpeControlEntry = _CadSubMgtCpeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cadSubMgtCpeControlEntry.setStatus("current")


class _CadSubMgtCpeControlMaxCpeIpv4_Type(Integer32):
    """Custom type cadSubMgtCpeControlMaxCpeIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CadSubMgtCpeControlMaxCpeIpv4_Type.__name__ = "Integer32"
_CadSubMgtCpeControlMaxCpeIpv4_Object = MibTableColumn
cadSubMgtCpeControlMaxCpeIpv4 = _CadSubMgtCpeControlMaxCpeIpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 1),
    _CadSubMgtCpeControlMaxCpeIpv4_Type()
)
cadSubMgtCpeControlMaxCpeIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlMaxCpeIpv4.setStatus("current")
_CadSubMgtCpeControlActive_Type = TruthValue
_CadSubMgtCpeControlActive_Object = MibTableColumn
cadSubMgtCpeControlActive = _CadSubMgtCpeControlActive_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 2),
    _CadSubMgtCpeControlActive_Type()
)
cadSubMgtCpeControlActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlActive.setStatus("current")
_CadSubMgtCpeControlLearnable_Type = TruthValue
_CadSubMgtCpeControlLearnable_Object = MibTableColumn
cadSubMgtCpeControlLearnable = _CadSubMgtCpeControlLearnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 3),
    _CadSubMgtCpeControlLearnable_Type()
)
cadSubMgtCpeControlLearnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlLearnable.setStatus("current")
_CadSubMgtCpeControlReset_Type = TruthValue
_CadSubMgtCpeControlReset_Object = MibTableColumn
cadSubMgtCpeControlReset = _CadSubMgtCpeControlReset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 4),
    _CadSubMgtCpeControlReset_Type()
)
cadSubMgtCpeControlReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlReset.setStatus("current")


class _CadSubMgtCpeControlMaxCpeIpv6Addresses_Type(Integer32):
    """Custom type cadSubMgtCpeControlMaxCpeIpv6Addresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CadSubMgtCpeControlMaxCpeIpv6Addresses_Type.__name__ = "Integer32"
_CadSubMgtCpeControlMaxCpeIpv6Addresses_Object = MibTableColumn
cadSubMgtCpeControlMaxCpeIpv6Addresses = _CadSubMgtCpeControlMaxCpeIpv6Addresses_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 5),
    _CadSubMgtCpeControlMaxCpeIpv6Addresses_Type()
)
cadSubMgtCpeControlMaxCpeIpv6Addresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlMaxCpeIpv6Addresses.setStatus("current")
_CadSubMgtCpeControlLastReset_Type = TimeStamp
_CadSubMgtCpeControlLastReset_Object = MibTableColumn
cadSubMgtCpeControlLastReset = _CadSubMgtCpeControlLastReset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 6, 1, 6),
    _CadSubMgtCpeControlLastReset_Type()
)
cadSubMgtCpeControlLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeControlLastReset.setStatus("current")
_CadSubMgtCpeIpTable_Object = MibTable
cadSubMgtCpeIpTable = _CadSubMgtCpeIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7)
)
if mibBuilder.loadTexts:
    cadSubMgtCpeIpTable.setStatus("current")
_CadSubMgtCpeIpEntry_Object = MibTableRow
cadSubMgtCpeIpEntry = _CadSubMgtCpeIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1)
)
cadSubMgtCpeIpEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadSubMgtCpeIpIndex"),
)
if mibBuilder.loadTexts:
    cadSubMgtCpeIpEntry.setStatus("current")


class _CadSubMgtCpeIpIndex_Type(Integer32):
    """Custom type cadSubMgtCpeIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CadSubMgtCpeIpIndex_Type.__name__ = "Integer32"
_CadSubMgtCpeIpIndex_Object = MibTableColumn
cadSubMgtCpeIpIndex = _CadSubMgtCpeIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 1),
    _CadSubMgtCpeIpIndex_Type()
)
cadSubMgtCpeIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSubMgtCpeIpIndex.setStatus("current")
_CadSubMgtCpeIpAddr_Type = InetAddressIPv4or6
_CadSubMgtCpeIpAddr_Object = MibTableColumn
cadSubMgtCpeIpAddr = _CadSubMgtCpeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 2),
    _CadSubMgtCpeIpAddr_Type()
)
cadSubMgtCpeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeIpAddr.setStatus("current")
_CadSubMgtCpeIpLearned_Type = TruthValue
_CadSubMgtCpeIpLearned_Object = MibTableColumn
cadSubMgtCpeIpLearned = _CadSubMgtCpeIpLearned_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 3),
    _CadSubMgtCpeIpLearned_Type()
)
cadSubMgtCpeIpLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeIpLearned.setStatus("current")
_CadSubMgtCpeIpMacAddr_Type = MacAddress
_CadSubMgtCpeIpMacAddr_Object = MibTableColumn
cadSubMgtCpeIpMacAddr = _CadSubMgtCpeIpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 4),
    _CadSubMgtCpeIpMacAddr_Type()
)
cadSubMgtCpeIpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeIpMacAddr.setStatus("current")


class _CadSubMgtCpeFilterDownstream_Type(Integer32):
    """Custom type cadSubMgtCpeFilterDownstream based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadSubMgtCpeFilterDownstream_Type.__name__ = "Integer32"
_CadSubMgtCpeFilterDownstream_Object = MibTableColumn
cadSubMgtCpeFilterDownstream = _CadSubMgtCpeFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 5),
    _CadSubMgtCpeFilterDownstream_Type()
)
cadSubMgtCpeFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeFilterDownstream.setStatus("current")


class _CadSubMgtCpeFilterUpstream_Type(Integer32):
    """Custom type cadSubMgtCpeFilterUpstream based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadSubMgtCpeFilterUpstream_Type.__name__ = "Integer32"
_CadSubMgtCpeFilterUpstream_Object = MibTableColumn
cadSubMgtCpeFilterUpstream = _CadSubMgtCpeFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 6),
    _CadSubMgtCpeFilterUpstream_Type()
)
cadSubMgtCpeFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeFilterUpstream.setStatus("current")


class _CadSubMgtCpeCpeType_Type(Integer32):
    """Custom type cadSubMgtCpeCpeType based on Integer32"""
    defaultValue = 1

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
        *(("cpe", 1),
          ("erouter", 6),
          ("mta", 3),
          ("ps", 2),
          ("stb", 4),
          ("tea", 5))
    )


_CadSubMgtCpeCpeType_Type.__name__ = "Integer32"
_CadSubMgtCpeCpeType_Object = MibTableColumn
cadSubMgtCpeCpeType = _CadSubMgtCpeCpeType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 7),
    _CadSubMgtCpeCpeType_Type()
)
cadSubMgtCpeCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeCpeType.setStatus("current")


class _CadSubMgtCpeIpAddrType_Type(InetAddressType):
    """Custom type cadSubMgtCpeIpAddrType based on InetAddressType"""


_CadSubMgtCpeIpAddrType_Object = MibTableColumn
cadSubMgtCpeIpAddrType = _CadSubMgtCpeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 7, 1, 8),
    _CadSubMgtCpeIpAddrType_Type()
)
cadSubMgtCpeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCpeIpAddrType.setStatus("current")
_CadSubMgtCmFilterTable_Object = MibTable
cadSubMgtCmFilterTable = _CadSubMgtCmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8)
)
if mibBuilder.loadTexts:
    cadSubMgtCmFilterTable.setStatus("current")
_CadSubMgtCmFilterEntry_Object = MibTableRow
cadSubMgtCmFilterEntry = _CadSubMgtCmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1)
)
cadSubMgtCmFilterEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadSubMgtCmFilterEntry.setStatus("current")
_CadSubMgtSubFilterDownstream_Type = Integer32
_CadSubMgtSubFilterDownstream_Object = MibTableColumn
cadSubMgtSubFilterDownstream = _CadSubMgtSubFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 1),
    _CadSubMgtSubFilterDownstream_Type()
)
cadSubMgtSubFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtSubFilterDownstream.setStatus("current")
_CadSubMgtSubFilterUpstream_Type = Integer32
_CadSubMgtSubFilterUpstream_Object = MibTableColumn
cadSubMgtSubFilterUpstream = _CadSubMgtSubFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 2),
    _CadSubMgtSubFilterUpstream_Type()
)
cadSubMgtSubFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtSubFilterUpstream.setStatus("current")
_CadSubMgtCmFilterDownstream_Type = Integer32
_CadSubMgtCmFilterDownstream_Object = MibTableColumn
cadSubMgtCmFilterDownstream = _CadSubMgtCmFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 3),
    _CadSubMgtCmFilterDownstream_Type()
)
cadSubMgtCmFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCmFilterDownstream.setStatus("current")
_CadSubMgtCmFilterUpstream_Type = Integer32
_CadSubMgtCmFilterUpstream_Object = MibTableColumn
cadSubMgtCmFilterUpstream = _CadSubMgtCmFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 4),
    _CadSubMgtCmFilterUpstream_Type()
)
cadSubMgtCmFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtCmFilterUpstream.setStatus("current")
_CadSubMgtPsFilterDownstream_Type = Integer32
_CadSubMgtPsFilterDownstream_Object = MibTableColumn
cadSubMgtPsFilterDownstream = _CadSubMgtPsFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 5),
    _CadSubMgtPsFilterDownstream_Type()
)
cadSubMgtPsFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtPsFilterDownstream.setStatus("current")
_CadSubMgtPsFilterUpstream_Type = Integer32
_CadSubMgtPsFilterUpstream_Object = MibTableColumn
cadSubMgtPsFilterUpstream = _CadSubMgtPsFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 6),
    _CadSubMgtPsFilterUpstream_Type()
)
cadSubMgtPsFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtPsFilterUpstream.setStatus("current")
_CadSubMgtMtaFilterDownstream_Type = Integer32
_CadSubMgtMtaFilterDownstream_Object = MibTableColumn
cadSubMgtMtaFilterDownstream = _CadSubMgtMtaFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 7),
    _CadSubMgtMtaFilterDownstream_Type()
)
cadSubMgtMtaFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtMtaFilterDownstream.setStatus("current")
_CadSubMgtMtaFilterUpstream_Type = Integer32
_CadSubMgtMtaFilterUpstream_Object = MibTableColumn
cadSubMgtMtaFilterUpstream = _CadSubMgtMtaFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 8),
    _CadSubMgtMtaFilterUpstream_Type()
)
cadSubMgtMtaFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtMtaFilterUpstream.setStatus("current")
_CadSubMgtStbFilterDownstream_Type = Integer32
_CadSubMgtStbFilterDownstream_Object = MibTableColumn
cadSubMgtStbFilterDownstream = _CadSubMgtStbFilterDownstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 9),
    _CadSubMgtStbFilterDownstream_Type()
)
cadSubMgtStbFilterDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtStbFilterDownstream.setStatus("current")
_CadSubMgtStbFilterUpstream_Type = Integer32
_CadSubMgtStbFilterUpstream_Object = MibTableColumn
cadSubMgtStbFilterUpstream = _CadSubMgtStbFilterUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 8, 1, 10),
    _CadSubMgtStbFilterUpstream_Type()
)
cadSubMgtStbFilterUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtStbFilterUpstream.setStatus("current")
_CadTpFdbTable_Object = MibTable
cadTpFdbTable = _CadTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 9)
)
if mibBuilder.loadTexts:
    cadTpFdbTable.setStatus("current")
_CadTpFdbEntry_Object = MibTableRow
cadTpFdbEntry = _CadTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 9, 1)
)
cadTpFdbEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadTpFdbAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadTpFdbIfIndex"),
)
if mibBuilder.loadTexts:
    cadTpFdbEntry.setStatus("current")
_CadTpFdbAddress_Type = MacAddress
_CadTpFdbAddress_Object = MibTableColumn
cadTpFdbAddress = _CadTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 9, 1, 1),
    _CadTpFdbAddress_Type()
)
cadTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadTpFdbAddress.setStatus("current")
_CadTpFdbIfIndex_Type = InterfaceIndex
_CadTpFdbIfIndex_Object = MibTableColumn
cadTpFdbIfIndex = _CadTpFdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 9, 1, 2),
    _CadTpFdbIfIndex_Type()
)
cadTpFdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadTpFdbIfIndex.setStatus("current")


class _CadTpFdbStatus_Type(Integer32):
    """Custom type cadTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_CadTpFdbStatus_Type.__name__ = "Integer32"
_CadTpFdbStatus_Object = MibTableColumn
cadTpFdbStatus = _CadTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 9, 1, 3),
    _CadTpFdbStatus_Type()
)
cadTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTpFdbStatus.setStatus("current")
_CadIfQosProfileLookupTable_Object = MibTable
cadIfQosProfileLookupTable = _CadIfQosProfileLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 10)
)
if mibBuilder.loadTexts:
    cadIfQosProfileLookupTable.setStatus("current")
_CadIfQosProfileLookupEntry_Object = MibTableRow
cadIfQosProfileLookupEntry = _CadIfQosProfileLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 10, 1)
)
cadIfQosProfileLookupEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfPriority"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfMaxUpBandwidth"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfGuarUpBandwidth"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfMaxDownBandwidth"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfMaxTxBurst"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfQosProfBaselinePrivacy"),
)
if mibBuilder.loadTexts:
    cadIfQosProfileLookupEntry.setStatus("current")


class _CadIfQosProfileLookupIndex_Type(Integer32):
    """Custom type cadIfQosProfileLookupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CadIfQosProfileLookupIndex_Type.__name__ = "Integer32"
_CadIfQosProfileLookupIndex_Object = MibTableColumn
cadIfQosProfileLookupIndex = _CadIfQosProfileLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 10, 1, 1),
    _CadIfQosProfileLookupIndex_Type()
)
cadIfQosProfileLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfileLookupIndex.setStatus("current")
_CadIfQosProfileLookupRefCount_Type = Counter32
_CadIfQosProfileLookupRefCount_Object = MibTableColumn
cadIfQosProfileLookupRefCount = _CadIfQosProfileLookupRefCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 10, 1, 2),
    _CadIfQosProfileLookupRefCount_Type()
)
cadIfQosProfileLookupRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfQosProfileLookupRefCount.setStatus("current")
_CadChannelToCmTable_Object = MibTable
cadChannelToCmTable = _CadChannelToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 11)
)
if mibBuilder.loadTexts:
    cadChannelToCmTable.setStatus("current")
_CadChannelToCmEntry_Object = MibTableRow
cadChannelToCmEntry = _CadChannelToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 11, 1)
)
cadChannelToCmEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIf3CmtsCmRegStatusMdIfIndex"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadChannelToCmEntry.setStatus("current")


class _CadChannelToCmPtr_Type(Integer32):
    """Custom type cadChannelToCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadChannelToCmPtr_Type.__name__ = "Integer32"
_CadChannelToCmPtr_Object = MibTableColumn
cadChannelToCmPtr = _CadChannelToCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 11, 1, 1),
    _CadChannelToCmPtr_Type()
)
cadChannelToCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChannelToCmPtr.setStatus("current")
_CadCmtsCmStatusSummaryTable_Object = MibTable
cadCmtsCmStatusSummaryTable = _CadCmtsCmStatusSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12)
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusSummaryTable.setStatus("deprecated")
_CadCmtsCmStatusSummaryEntry_Object = MibTableRow
cadCmtsCmStatusSummaryEntry = _CadCmtsCmStatusSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1)
)
cadCmtsCmStatusSummaryEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusDownChannelIfIndex"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusUpChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusSummaryEntry.setStatus("deprecated")
_CadCmtsCmStatusNumOther_Type = Integer32
_CadCmtsCmStatusNumOther_Object = MibTableColumn
cadCmtsCmStatusNumOther = _CadCmtsCmStatusNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 1),
    _CadCmtsCmStatusNumOther_Type()
)
cadCmtsCmStatusNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumOther.setStatus("deprecated")
_CadCmtsCmStatusNumRanging_Type = Integer32
_CadCmtsCmStatusNumRanging_Object = MibTableColumn
cadCmtsCmStatusNumRanging = _CadCmtsCmStatusNumRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 2),
    _CadCmtsCmStatusNumRanging_Type()
)
cadCmtsCmStatusNumRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRanging.setStatus("deprecated")
_CadCmtsCmStatusNumRangingAborted_Type = Integer32
_CadCmtsCmStatusNumRangingAborted_Object = MibTableColumn
cadCmtsCmStatusNumRangingAborted = _CadCmtsCmStatusNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 3),
    _CadCmtsCmStatusNumRangingAborted_Type()
)
cadCmtsCmStatusNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRangingAborted.setStatus("deprecated")
_CadCmtsCmStatusNumRangingComplete_Type = Integer32
_CadCmtsCmStatusNumRangingComplete_Object = MibTableColumn
cadCmtsCmStatusNumRangingComplete = _CadCmtsCmStatusNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 4),
    _CadCmtsCmStatusNumRangingComplete_Type()
)
cadCmtsCmStatusNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRangingComplete.setStatus("deprecated")
_CadCmtsCmStatusNumIpComplete_Type = Integer32
_CadCmtsCmStatusNumIpComplete_Object = MibTableColumn
cadCmtsCmStatusNumIpComplete = _CadCmtsCmStatusNumIpComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 5),
    _CadCmtsCmStatusNumIpComplete_Type()
)
cadCmtsCmStatusNumIpComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumIpComplete.setStatus("deprecated")
_CadCmtsCmStatusNumRegistrationComplete_Type = Integer32
_CadCmtsCmStatusNumRegistrationComplete_Object = MibTableColumn
cadCmtsCmStatusNumRegistrationComplete = _CadCmtsCmStatusNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 6),
    _CadCmtsCmStatusNumRegistrationComplete_Type()
)
cadCmtsCmStatusNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRegistrationComplete.setStatus("deprecated")
_CadCmtsCmStatusNumAccessDenied_Type = Integer32
_CadCmtsCmStatusNumAccessDenied_Object = MibTableColumn
cadCmtsCmStatusNumAccessDenied = _CadCmtsCmStatusNumAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 7),
    _CadCmtsCmStatusNumAccessDenied_Type()
)
cadCmtsCmStatusNumAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumAccessDenied.setStatus("deprecated")
_CadCmtsCmStatusNumRangFlaps_Type = Counter32
_CadCmtsCmStatusNumRangFlaps_Object = MibTableColumn
cadCmtsCmStatusNumRangFlaps = _CadCmtsCmStatusNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 8),
    _CadCmtsCmStatusNumRangFlaps_Type()
)
cadCmtsCmStatusNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRangFlaps.setStatus("deprecated")
_CadCmtsCmStatusNumProvFlaps_Type = Counter32
_CadCmtsCmStatusNumProvFlaps_Object = MibTableColumn
cadCmtsCmStatusNumProvFlaps = _CadCmtsCmStatusNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 9),
    _CadCmtsCmStatusNumProvFlaps_Type()
)
cadCmtsCmStatusNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumProvFlaps.setStatus("deprecated")
_CadCmtsCmStatusNumRegFlaps_Type = Counter32
_CadCmtsCmStatusNumRegFlaps_Object = MibTableColumn
cadCmtsCmStatusNumRegFlaps = _CadCmtsCmStatusNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 10),
    _CadCmtsCmStatusNumRegFlaps_Type()
)
cadCmtsCmStatusNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRegFlaps.setStatus("deprecated")
_CadCmtsCmStatusNumOperational_Type = Integer32
_CadCmtsCmStatusNumOperational_Object = MibTableColumn
cadCmtsCmStatusNumOperational = _CadCmtsCmStatusNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 11),
    _CadCmtsCmStatusNumOperational_Type()
)
cadCmtsCmStatusNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumOperational.setStatus("deprecated")
_CadCmtsCmStatusNumRegisteredBpiInitializing_Type = Integer32
_CadCmtsCmStatusNumRegisteredBpiInitializing_Object = MibTableColumn
cadCmtsCmStatusNumRegisteredBpiInitializing = _CadCmtsCmStatusNumRegisteredBpiInitializing_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 12),
    _CadCmtsCmStatusNumRegisteredBpiInitializing_Type()
)
cadCmtsCmStatusNumRegisteredBpiInitializing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRegisteredBpiInitializing.setStatus("deprecated")
_CadCmtsCmStatusNumTotal_Type = Integer32
_CadCmtsCmStatusNumTotal_Object = MibTableColumn
cadCmtsCmStatusNumTotal = _CadCmtsCmStatusNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 13),
    _CadCmtsCmStatusNumTotal_Type()
)
cadCmtsCmStatusNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumTotal.setStatus("deprecated")
_CadCmtsCmStatusNumActive_Type = Integer32
_CadCmtsCmStatusNumActive_Object = MibTableColumn
cadCmtsCmStatusNumActive = _CadCmtsCmStatusNumActive_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 14),
    _CadCmtsCmStatusNumActive_Type()
)
cadCmtsCmStatusNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumActive.setStatus("deprecated")
_CadCmtsCmStatusNumRegistered_Type = Integer32
_CadCmtsCmStatusNumRegistered_Object = MibTableColumn
cadCmtsCmStatusNumRegistered = _CadCmtsCmStatusNumRegistered_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 12, 1, 15),
    _CadCmtsCmStatusNumRegistered_Type()
)
cadCmtsCmStatusNumRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusNumRegistered.setStatus("deprecated")
_CadArpTable_Object = MibTable
cadArpTable = _CadArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13)
)
if mibBuilder.loadTexts:
    cadArpTable.setStatus("current")
_CadArpEntry_Object = MibTableRow
cadArpEntry = _CadArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1)
)
cadArpEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadArpIfIndex"),
    (0, "CADANT-CMTS-MAC-MIB", "cadArpAddressType"),
    (0, "CADANT-CMTS-MAC-MIB", "cadArpNetAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadArpL3IfIndex"),
)
if mibBuilder.loadTexts:
    cadArpEntry.setStatus("current")
_CadArpIfIndex_Type = InterfaceIndex
_CadArpIfIndex_Object = MibTableColumn
cadArpIfIndex = _CadArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 1),
    _CadArpIfIndex_Type()
)
cadArpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadArpIfIndex.setStatus("current")
_CadArpAddressType_Type = InetAddressType
_CadArpAddressType_Object = MibTableColumn
cadArpAddressType = _CadArpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 2),
    _CadArpAddressType_Type()
)
cadArpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadArpAddressType.setStatus("current")
_CadArpNetAddress_Type = InetAddressIPv4or6
_CadArpNetAddress_Object = MibTableColumn
cadArpNetAddress = _CadArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 3),
    _CadArpNetAddress_Type()
)
cadArpNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadArpNetAddress.setStatus("current")
_CadArpMacAddress_Type = MacAddress
_CadArpMacAddress_Object = MibTableColumn
cadArpMacAddress = _CadArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 4),
    _CadArpMacAddress_Type()
)
cadArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadArpMacAddress.setStatus("current")


class _CadArpType_Type(Integer32):
    """Custom type cadArpType based on Integer32"""
    defaultValue = 4

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
        *(("dynamic", 3),
          ("invalid", 2),
          ("local", 5),
          ("other", 1),
          ("static", 4))
    )


_CadArpType_Type.__name__ = "Integer32"
_CadArpType_Object = MibTableColumn
cadArpType = _CadArpType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 5),
    _CadArpType_Type()
)
cadArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadArpType.setStatus("current")


class _CadArpState_Type(Integer32):
    """Custom type cadArpState based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("incomplete", 7),
          ("invalid", 5),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_CadArpState_Type.__name__ = "Integer32"
_CadArpState_Object = MibTableColumn
cadArpState = _CadArpState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 6),
    _CadArpState_Type()
)
cadArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadArpState.setStatus("current")
_CadArpL3IfIndex_Type = InterfaceIndexOrZero
_CadArpL3IfIndex_Object = MibTableColumn
cadArpL3IfIndex = _CadArpL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 13, 1, 7),
    _CadArpL3IfIndex_Type()
)
cadArpL3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadArpL3IfIndex.setStatus("current")
_CadMacControl_ObjectIdentity = ObjectIdentity
cadMacControl = _CadMacControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14)
)


class _CadMacClearFlapCounts_Type(TruthValue):
    """Custom type cadMacClearFlapCounts based on TruthValue"""


_CadMacClearFlapCounts_Object = MibScalar
cadMacClearFlapCounts = _CadMacClearFlapCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 1),
    _CadMacClearFlapCounts_Type()
)
cadMacClearFlapCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearFlapCounts.setStatus("current")


class _CadMacResetCMMacAddress_Type(MacAddress):
    """Custom type cadMacResetCMMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_CadMacResetCMMacAddress_Object = MibScalar
cadMacResetCMMacAddress = _CadMacResetCMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 2),
    _CadMacResetCMMacAddress_Type()
)
cadMacResetCMMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacResetCMMacAddress.setStatus("current")


class _CadMacDeleteMacAddress_Type(MacAddress):
    """Custom type cadMacDeleteMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_CadMacDeleteMacAddress_Object = MibScalar
cadMacDeleteMacAddress = _CadMacDeleteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 3),
    _CadMacDeleteMacAddress_Type()
)
cadMacDeleteMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacDeleteMacAddress.setStatus("current")


class _CadMacClearDenyCounts_Type(TruthValue):
    """Custom type cadMacClearDenyCounts based on TruthValue"""


_CadMacClearDenyCounts_Object = MibScalar
cadMacClearDenyCounts = _CadMacClearDenyCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 4),
    _CadMacClearDenyCounts_Type()
)
cadMacClearDenyCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearDenyCounts.setStatus("current")


class _CadMacClearDenyCountMacAddr_Type(MacAddress):
    """Custom type cadMacClearDenyCountMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CadMacClearDenyCountMacAddr_Object = MibScalar
cadMacClearDenyCountMacAddr = _CadMacClearDenyCountMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 5),
    _CadMacClearDenyCountMacAddr_Type()
)
cadMacClearDenyCountMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearDenyCountMacAddr.setStatus("current")


class _CadMacClearFlapCountMacAddr_Type(MacAddress):
    """Custom type cadMacClearFlapCountMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CadMacClearFlapCountMacAddr_Object = MibScalar
cadMacClearFlapCountMacAddr = _CadMacClearFlapCountMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 6),
    _CadMacClearFlapCountMacAddr_Type()
)
cadMacClearFlapCountMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearFlapCountMacAddr.setStatus("current")


class _CadMacRecalculateCmSummaryIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadMacRecalculateCmSummaryIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadMacRecalculateCmSummaryIfIndex_Object = MibScalar
cadMacRecalculateCmSummaryIfIndex = _CadMacRecalculateCmSummaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 7),
    _CadMacRecalculateCmSummaryIfIndex_Type()
)
cadMacRecalculateCmSummaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacRecalculateCmSummaryIfIndex.setStatus("current")


class _CadMacClearFlapCountsByIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadMacClearFlapCountsByIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadMacClearFlapCountsByIfIndex_Object = MibScalar
cadMacClearFlapCountsByIfIndex = _CadMacClearFlapCountsByIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 8),
    _CadMacClearFlapCountsByIfIndex_Type()
)
cadMacClearFlapCountsByIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearFlapCountsByIfIndex.setStatus("current")


class _CadMacClearPenaltyCounts_Type(TruthValue):
    """Custom type cadMacClearPenaltyCounts based on TruthValue"""


_CadMacClearPenaltyCounts_Object = MibScalar
cadMacClearPenaltyCounts = _CadMacClearPenaltyCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 9),
    _CadMacClearPenaltyCounts_Type()
)
cadMacClearPenaltyCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearPenaltyCounts.setStatus("current")


class _CadMacClearPenaltyCountsByIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadMacClearPenaltyCountsByIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadMacClearPenaltyCountsByIfIndex_Object = MibScalar
cadMacClearPenaltyCountsByIfIndex = _CadMacClearPenaltyCountsByIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 10),
    _CadMacClearPenaltyCountsByIfIndex_Type()
)
cadMacClearPenaltyCountsByIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearPenaltyCountsByIfIndex.setStatus("current")


class _CadMacClearPenaltyCountMacAddr_Type(MacAddress):
    """Custom type cadMacClearPenaltyCountMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CadMacClearPenaltyCountMacAddr_Object = MibScalar
cadMacClearPenaltyCountMacAddr = _CadMacClearPenaltyCountMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 11),
    _CadMacClearPenaltyCountMacAddr_Type()
)
cadMacClearPenaltyCountMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearPenaltyCountMacAddr.setStatus("current")


class _CadMacClearPenaltyCountScn_Type(SnmpAdminString):
    """Custom type cadMacClearPenaltyCountScn based on SnmpAdminString"""
    defaultValue = OctetString(" ")


_CadMacClearPenaltyCountScn_Object = MibScalar
cadMacClearPenaltyCountScn = _CadMacClearPenaltyCountScn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 14, 12),
    _CadMacClearPenaltyCountScn_Type()
)
cadMacClearPenaltyCountScn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMacClearPenaltyCountScn.setStatus("current")
_CadQosCmtsMacToSrvFlowTable_Object = MibTable
cadQosCmtsMacToSrvFlowTable = _CadQosCmtsMacToSrvFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 15)
)
if mibBuilder.loadTexts:
    cadQosCmtsMacToSrvFlowTable.setStatus("current")
_CadQosCmtsMacToSrvFlowEntry_Object = MibTableRow
cadQosCmtsMacToSrvFlowEntry = _CadQosCmtsMacToSrvFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 15, 1)
)
cadQosCmtsMacToSrvFlowEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadQosCmtsCmMac"),
    (0, "CADANT-CMTS-MAC-MIB", "cadQosCmtsServiceFlowId"),
)
if mibBuilder.loadTexts:
    cadQosCmtsMacToSrvFlowEntry.setStatus("current")
_CadQosCmtsCmMac_Type = MacAddress
_CadQosCmtsCmMac_Object = MibTableColumn
cadQosCmtsCmMac = _CadQosCmtsCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 15, 1, 1),
    _CadQosCmtsCmMac_Type()
)
cadQosCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadQosCmtsCmMac.setStatus("current")


class _CadQosCmtsServiceFlowId_Type(Unsigned32):
    """Custom type cadQosCmtsServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadQosCmtsServiceFlowId_Type.__name__ = "Unsigned32"
_CadQosCmtsServiceFlowId_Object = MibTableColumn
cadQosCmtsServiceFlowId = _CadQosCmtsServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 15, 1, 2),
    _CadQosCmtsServiceFlowId_Type()
)
cadQosCmtsServiceFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosCmtsServiceFlowId.setStatus("current")
_CadQosCmtsIfIndex_Type = InterfaceIndex
_CadQosCmtsIfIndex_Object = MibTableColumn
cadQosCmtsIfIndex = _CadQosCmtsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 15, 1, 3),
    _CadQosCmtsIfIndex_Type()
)
cadQosCmtsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosCmtsIfIndex.setStatus("current")
_CadQosServiceClassTable_Object = MibTable
cadQosServiceClassTable = _CadQosServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 19)
)
if mibBuilder.loadTexts:
    cadQosServiceClassTable.setStatus("current")
_CadQosServiceClassEntry_Object = MibTableRow
cadQosServiceClassEntry = _CadQosServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 19, 1)
)
if mibBuilder.loadTexts:
    cadQosServiceClassEntry.setStatus("current")


class _CadQosServiceClassPeakTrafficRate_Type(BitRate):
    """Custom type cadQosServiceClassPeakTrafficRate based on BitRate"""
    defaultValue = 0


_CadQosServiceClassPeakTrafficRate_Object = MibTableColumn
cadQosServiceClassPeakTrafficRate = _CadQosServiceClassPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 19, 1, 1),
    _CadQosServiceClassPeakTrafficRate_Type()
)
cadQosServiceClassPeakTrafficRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadQosServiceClassPeakTrafficRate.setStatus("current")


class _CadQosServiceClassLatencyControlledFlowFlag_Type(TruthValue):
    """Custom type cadQosServiceClassLatencyControlledFlowFlag based on TruthValue"""


_CadQosServiceClassLatencyControlledFlowFlag_Object = MibTableColumn
cadQosServiceClassLatencyControlledFlowFlag = _CadQosServiceClassLatencyControlledFlowFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 19, 1, 2),
    _CadQosServiceClassLatencyControlledFlowFlag_Type()
)
cadQosServiceClassLatencyControlledFlowFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadQosServiceClassLatencyControlledFlowFlag.setStatus("current")
_CadCmtsCmVendorTable_Object = MibTable
cadCmtsCmVendorTable = _CadCmtsCmVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 20)
)
if mibBuilder.loadTexts:
    cadCmtsCmVendorTable.setStatus("current")
_CadCmtsCmVendorEntry_Object = MibTableRow
cadCmtsCmVendorEntry = _CadCmtsCmVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 20, 1)
)
cadCmtsCmVendorEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadCmtsCmVendorOUI"),
)
if mibBuilder.loadTexts:
    cadCmtsCmVendorEntry.setStatus("current")
_CadCmtsCmVendorOUI_Type = OUIAddress
_CadCmtsCmVendorOUI_Object = MibTableColumn
cadCmtsCmVendorOUI = _CadCmtsCmVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 20, 1, 1),
    _CadCmtsCmVendorOUI_Type()
)
cadCmtsCmVendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmtsCmVendorOUI.setStatus("current")


class _CadCmtsCmVendorName_Type(DisplayString):
    """Custom type cadCmtsCmVendorName based on DisplayString"""
    defaultValue = OctetString("(unspecified)")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_CadCmtsCmVendorName_Type.__name__ = "DisplayString"
_CadCmtsCmVendorName_Object = MibTableColumn
cadCmtsCmVendorName = _CadCmtsCmVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 20, 1, 2),
    _CadCmtsCmVendorName_Type()
)
cadCmtsCmVendorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmVendorName.setStatus("current")
_CadCmtsCmVendorRowStatus_Type = RowStatus
_CadCmtsCmVendorRowStatus_Object = MibTableColumn
cadCmtsCmVendorRowStatus = _CadCmtsCmVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 20, 1, 3),
    _CadCmtsCmVendorRowStatus_Type()
)
cadCmtsCmVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmVendorRowStatus.setStatus("current")
_CadIfCmtsMacToIpTable_Object = MibTable
cadIfCmtsMacToIpTable = _CadIfCmtsMacToIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21)
)
if mibBuilder.loadTexts:
    cadIfCmtsMacToIpTable.setStatus("current")
_CadIfCmtsMacToIpEntry_Object = MibTableRow
cadIfCmtsMacToIpEntry = _CadIfCmtsMacToIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21, 1)
)
cadIfCmtsMacToIpEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsMacAddr"),
)
if mibBuilder.loadTexts:
    cadIfCmtsMacToIpEntry.setStatus("current")
_CadIfCmtsMacAddr_Type = MacAddress
_CadIfCmtsMacAddr_Object = MibTableColumn
cadIfCmtsMacAddr = _CadIfCmtsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21, 1, 1),
    _CadIfCmtsMacAddr_Type()
)
cadIfCmtsMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsMacAddr.setStatus("current")
_CadIfCmtsMacCmMacAddr_Type = MacAddress
_CadIfCmtsMacCmMacAddr_Object = MibTableColumn
cadIfCmtsMacCmMacAddr = _CadIfCmtsMacCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21, 1, 3),
    _CadIfCmtsMacCmMacAddr_Type()
)
cadIfCmtsMacCmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsMacCmMacAddr.setStatus("current")


class _CadIfCmtsMacInetIpAddr_Type(InetAddressIPv4or6):
    """Custom type cadIfCmtsMacInetIpAddr based on InetAddressIPv4or6"""
    defaultHexValue = "00000000"


_CadIfCmtsMacInetIpAddr_Object = MibTableColumn
cadIfCmtsMacInetIpAddr = _CadIfCmtsMacInetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21, 1, 4),
    _CadIfCmtsMacInetIpAddr_Type()
)
cadIfCmtsMacInetIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsMacInetIpAddr.setStatus("deprecated")


class _CadIfCmtsMacInetIpAddrType_Type(InetAddressType):
    """Custom type cadIfCmtsMacInetIpAddrType based on InetAddressType"""


_CadIfCmtsMacInetIpAddrType_Object = MibTableColumn
cadIfCmtsMacInetIpAddrType = _CadIfCmtsMacInetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 21, 1, 5),
    _CadIfCmtsMacInetIpAddrType_Type()
)
cadIfCmtsMacInetIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsMacInetIpAddrType.setStatus("deprecated")
_CadCmDenyTable_Object = MibTable
cadCmDenyTable = _CadCmDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 22)
)
if mibBuilder.loadTexts:
    cadCmDenyTable.setStatus("current")
_CadCmDenyEntry_Object = MibTableRow
cadCmDenyEntry = _CadCmDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 22, 1)
)
cadCmDenyEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadCmDenyMacAddress"),
)
if mibBuilder.loadTexts:
    cadCmDenyEntry.setStatus("current")
_CadCmDenyMacAddress_Type = MacAddress
_CadCmDenyMacAddress_Object = MibTableColumn
cadCmDenyMacAddress = _CadCmDenyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 22, 1, 1),
    _CadCmDenyMacAddress_Type()
)
cadCmDenyMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmDenyMacAddress.setStatus("current")
_CadCmDenyRowStatus_Type = RowStatus
_CadCmDenyRowStatus_Object = MibTableColumn
cadCmDenyRowStatus = _CadCmDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 22, 1, 2),
    _CadCmDenyRowStatus_Type()
)
cadCmDenyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmDenyRowStatus.setStatus("current")
_CadCmDenyStatusTable_Object = MibTable
cadCmDenyStatusTable = _CadCmDenyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 23)
)
if mibBuilder.loadTexts:
    cadCmDenyStatusTable.setStatus("current")
_CadCmDenyStatusEntry_Object = MibTableRow
cadCmDenyStatusEntry = _CadCmDenyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 23, 1)
)
cadCmDenyStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadCmDenyMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadCmDenyRecentIfIndex"),
)
if mibBuilder.loadTexts:
    cadCmDenyStatusEntry.setStatus("current")
_CadCmDenyRecentIfIndex_Type = InterfaceIndex
_CadCmDenyRecentIfIndex_Object = MibTableColumn
cadCmDenyRecentIfIndex = _CadCmDenyRecentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 23, 1, 1),
    _CadCmDenyRecentIfIndex_Type()
)
cadCmDenyRecentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmDenyRecentIfIndex.setStatus("current")
_CadCmDenyRecentTime_Type = DateAndTime
_CadCmDenyRecentTime_Object = MibTableColumn
cadCmDenyRecentTime = _CadCmDenyRecentTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 23, 1, 2),
    _CadCmDenyRecentTime_Type()
)
cadCmDenyRecentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmDenyRecentTime.setStatus("current")
_CadCmDenyAttempts_Type = Counter32
_CadCmDenyAttempts_Object = MibTableColumn
cadCmDenyAttempts = _CadCmDenyAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 23, 1, 3),
    _CadCmDenyAttempts_Type()
)
cadCmDenyAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmDenyAttempts.setStatus("current")
_CadCpeHostAuthorizationTable_Object = MibTable
cadCpeHostAuthorizationTable = _CadCpeHostAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24)
)
if mibBuilder.loadTexts:
    cadCpeHostAuthorizationTable.setStatus("current")
_CadCpeHostAuthorizationEntry_Object = MibTableRow
cadCpeHostAuthorizationEntry = _CadCpeHostAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24, 1)
)
cadCpeHostAuthorizationEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadCpeHostAuthCmMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadCpeHostAuthCpeMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadCpeHostAuthCpeIpAddress"),
)
if mibBuilder.loadTexts:
    cadCpeHostAuthorizationEntry.setStatus("current")
_CadCpeHostAuthCmMacAddress_Type = MacAddress
_CadCpeHostAuthCmMacAddress_Object = MibTableColumn
cadCpeHostAuthCmMacAddress = _CadCpeHostAuthCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24, 1, 1),
    _CadCpeHostAuthCmMacAddress_Type()
)
cadCpeHostAuthCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCpeHostAuthCmMacAddress.setStatus("current")
_CadCpeHostAuthCpeMacAddress_Type = MacAddress
_CadCpeHostAuthCpeMacAddress_Object = MibTableColumn
cadCpeHostAuthCpeMacAddress = _CadCpeHostAuthCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24, 1, 2),
    _CadCpeHostAuthCpeMacAddress_Type()
)
cadCpeHostAuthCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCpeHostAuthCpeMacAddress.setStatus("current")
_CadCpeHostAuthCpeIpAddress_Type = IpAddress
_CadCpeHostAuthCpeIpAddress_Object = MibTableColumn
cadCpeHostAuthCpeIpAddress = _CadCpeHostAuthCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24, 1, 3),
    _CadCpeHostAuthCpeIpAddress_Type()
)
cadCpeHostAuthCpeIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCpeHostAuthCpeIpAddress.setStatus("current")
_CadCpeHostAuthRowStatus_Type = RowStatus
_CadCpeHostAuthRowStatus_Object = MibTableColumn
cadCpeHostAuthRowStatus = _CadCpeHostAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 24, 1, 4),
    _CadCpeHostAuthRowStatus_Type()
)
cadCpeHostAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCpeHostAuthRowStatus.setStatus("current")
_CadIfCmtsInetIpToCmMacTable_Object = MibTable
cadIfCmtsInetIpToCmMacTable = _CadIfCmtsInetIpToCmMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25)
)
if mibBuilder.loadTexts:
    cadIfCmtsInetIpToCmMacTable.setStatus("current")
_CadIfCmtsInetIpToCmMacEntry_Object = MibTableRow
cadIfCmtsInetIpToCmMacEntry = _CadIfCmtsInetIpToCmMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25, 1)
)
cadIfCmtsInetIpToCmMacEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsInetIpMacAddrType"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsInetIpMac"),
)
if mibBuilder.loadTexts:
    cadIfCmtsInetIpToCmMacEntry.setStatus("current")
_CadIfCmtsInetIpMacAddrType_Type = InetAddressType
_CadIfCmtsInetIpMacAddrType_Object = MibTableColumn
cadIfCmtsInetIpMacAddrType = _CadIfCmtsInetIpMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25, 1, 1),
    _CadIfCmtsInetIpMacAddrType_Type()
)
cadIfCmtsInetIpMacAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsInetIpMacAddrType.setStatus("current")
_CadIfCmtsInetIpMac_Type = InetAddressIPv4or6
_CadIfCmtsInetIpMac_Object = MibTableColumn
cadIfCmtsInetIpMac = _CadIfCmtsInetIpMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25, 1, 2),
    _CadIfCmtsInetIpMac_Type()
)
cadIfCmtsInetIpMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsInetIpMac.setStatus("current")
_CadIfCmtsInetIpCmMac_Type = MacAddress
_CadIfCmtsInetIpCmMac_Object = MibTableColumn
cadIfCmtsInetIpCmMac = _CadIfCmtsInetIpCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25, 1, 3),
    _CadIfCmtsInetIpCmMac_Type()
)
cadIfCmtsInetIpCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsInetIpCmMac.setStatus("current")
_CadIfCmtsInetIpCpeMac_Type = MacAddress
_CadIfCmtsInetIpCpeMac_Object = MibTableColumn
cadIfCmtsInetIpCpeMac = _CadIfCmtsInetIpCpeMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 25, 1, 4),
    _CadIfCmtsInetIpCpeMac_Type()
)
cadIfCmtsInetIpCpeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsInetIpCpeMac.setStatus("current")
_CadCmtsCmStatusMacSummaryTable_Object = MibTable
cadCmtsCmStatusMacSummaryTable = _CadCmtsCmStatusMacSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26)
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacSummaryTable.setStatus("deprecated")
_CadCmtsCmStatusMacSummaryEntry_Object = MibTableRow
cadCmtsCmStatusMacSummaryEntry = _CadCmtsCmStatusMacSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1)
)
cadCmtsCmStatusMacSummaryEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacSummaryEntry.setStatus("deprecated")
_CadCmtsCmStatusMacNumOther_Type = Integer32
_CadCmtsCmStatusMacNumOther_Object = MibTableColumn
cadCmtsCmStatusMacNumOther = _CadCmtsCmStatusMacNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 1),
    _CadCmtsCmStatusMacNumOther_Type()
)
cadCmtsCmStatusMacNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumOther.setStatus("deprecated")
_CadCmtsCmStatusMacNumInitRanging_Type = Integer32
_CadCmtsCmStatusMacNumInitRanging_Object = MibTableColumn
cadCmtsCmStatusMacNumInitRanging = _CadCmtsCmStatusMacNumInitRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 2),
    _CadCmtsCmStatusMacNumInitRanging_Type()
)
cadCmtsCmStatusMacNumInitRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumInitRanging.setStatus("deprecated")
_CadCmtsCmStatusMacNumRangingComplete_Type = Integer32
_CadCmtsCmStatusMacNumRangingComplete_Object = MibTableColumn
cadCmtsCmStatusMacNumRangingComplete = _CadCmtsCmStatusMacNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 3),
    _CadCmtsCmStatusMacNumRangingComplete_Type()
)
cadCmtsCmStatusMacNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRangingComplete.setStatus("deprecated")
_CadCmtsCmStatusMacNumStartEae_Type = Integer32
_CadCmtsCmStatusMacNumStartEae_Object = MibTableColumn
cadCmtsCmStatusMacNumStartEae = _CadCmtsCmStatusMacNumStartEae_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 4),
    _CadCmtsCmStatusMacNumStartEae_Type()
)
cadCmtsCmStatusMacNumStartEae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumStartEae.setStatus("deprecated")
_CadCmtsCmStatusMacNumStartDhcpv4_Type = Integer32
_CadCmtsCmStatusMacNumStartDhcpv4_Object = MibTableColumn
cadCmtsCmStatusMacNumStartDhcpv4 = _CadCmtsCmStatusMacNumStartDhcpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 5),
    _CadCmtsCmStatusMacNumStartDhcpv4_Type()
)
cadCmtsCmStatusMacNumStartDhcpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumStartDhcpv4.setStatus("deprecated")
_CadCmtsCmStatusMacNumStartDhcpv6_Type = Integer32
_CadCmtsCmStatusMacNumStartDhcpv6_Object = MibTableColumn
cadCmtsCmStatusMacNumStartDhcpv6 = _CadCmtsCmStatusMacNumStartDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 6),
    _CadCmtsCmStatusMacNumStartDhcpv6_Type()
)
cadCmtsCmStatusMacNumStartDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumStartDhcpv6.setStatus("deprecated")
_CadCmtsCmStatusMacNumDhcpv4Complete_Type = Integer32
_CadCmtsCmStatusMacNumDhcpv4Complete_Object = MibTableColumn
cadCmtsCmStatusMacNumDhcpv4Complete = _CadCmtsCmStatusMacNumDhcpv4Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 7),
    _CadCmtsCmStatusMacNumDhcpv4Complete_Type()
)
cadCmtsCmStatusMacNumDhcpv4Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumDhcpv4Complete.setStatus("deprecated")
_CadCmtsCmStatusMacNumDhcpv6Complete_Type = Integer32
_CadCmtsCmStatusMacNumDhcpv6Complete_Object = MibTableColumn
cadCmtsCmStatusMacNumDhcpv6Complete = _CadCmtsCmStatusMacNumDhcpv6Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 8),
    _CadCmtsCmStatusMacNumDhcpv6Complete_Type()
)
cadCmtsCmStatusMacNumDhcpv6Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumDhcpv6Complete.setStatus("deprecated")
_CadCmtsCmStatusMacNumStartCfgFileDownload_Type = Integer32
_CadCmtsCmStatusMacNumStartCfgFileDownload_Object = MibTableColumn
cadCmtsCmStatusMacNumStartCfgFileDownload = _CadCmtsCmStatusMacNumStartCfgFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 9),
    _CadCmtsCmStatusMacNumStartCfgFileDownload_Type()
)
cadCmtsCmStatusMacNumStartCfgFileDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumStartCfgFileDownload.setStatus("deprecated")
_CadCmtsCmStatusMacNumCfgFileDownloadComplete_Type = Integer32
_CadCmtsCmStatusMacNumCfgFileDownloadComplete_Object = MibTableColumn
cadCmtsCmStatusMacNumCfgFileDownloadComplete = _CadCmtsCmStatusMacNumCfgFileDownloadComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 10),
    _CadCmtsCmStatusMacNumCfgFileDownloadComplete_Type()
)
cadCmtsCmStatusMacNumCfgFileDownloadComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumCfgFileDownloadComplete.setStatus("deprecated")
_CadCmtsCmStatusMacNumStartRegistration_Type = Integer32
_CadCmtsCmStatusMacNumStartRegistration_Object = MibTableColumn
cadCmtsCmStatusMacNumStartRegistration = _CadCmtsCmStatusMacNumStartRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 11),
    _CadCmtsCmStatusMacNumStartRegistration_Type()
)
cadCmtsCmStatusMacNumStartRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumStartRegistration.setStatus("deprecated")
_CadCmtsCmStatusMacNumRegistrationComplete_Type = Integer32
_CadCmtsCmStatusMacNumRegistrationComplete_Object = MibTableColumn
cadCmtsCmStatusMacNumRegistrationComplete = _CadCmtsCmStatusMacNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 12),
    _CadCmtsCmStatusMacNumRegistrationComplete_Type()
)
cadCmtsCmStatusMacNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRegistrationComplete.setStatus("deprecated")
_CadCmtsCmStatusMacNumOperational_Type = Integer32
_CadCmtsCmStatusMacNumOperational_Object = MibTableColumn
cadCmtsCmStatusMacNumOperational = _CadCmtsCmStatusMacNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 13),
    _CadCmtsCmStatusMacNumOperational_Type()
)
cadCmtsCmStatusMacNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumOperational.setStatus("deprecated")
_CadCmtsCmStatusMacNumBpiInit_Type = Integer32
_CadCmtsCmStatusMacNumBpiInit_Object = MibTableColumn
cadCmtsCmStatusMacNumBpiInit = _CadCmtsCmStatusMacNumBpiInit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 14),
    _CadCmtsCmStatusMacNumBpiInit_Type()
)
cadCmtsCmStatusMacNumBpiInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumBpiInit.setStatus("deprecated")
_CadCmtsCmStatusMacNumForwardingDisabled_Type = Integer32
_CadCmtsCmStatusMacNumForwardingDisabled_Object = MibTableColumn
cadCmtsCmStatusMacNumForwardingDisabled = _CadCmtsCmStatusMacNumForwardingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 15),
    _CadCmtsCmStatusMacNumForwardingDisabled_Type()
)
cadCmtsCmStatusMacNumForwardingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumForwardingDisabled.setStatus("deprecated")
_CadCmtsCmStatusMacNumRfMuteAll_Type = Integer32
_CadCmtsCmStatusMacNumRfMuteAll_Object = MibTableColumn
cadCmtsCmStatusMacNumRfMuteAll = _CadCmtsCmStatusMacNumRfMuteAll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 16),
    _CadCmtsCmStatusMacNumRfMuteAll_Type()
)
cadCmtsCmStatusMacNumRfMuteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRfMuteAll.setStatus("deprecated")
_CadCmtsCmStatusMacNumTotal_Type = Integer32
_CadCmtsCmStatusMacNumTotal_Object = MibTableColumn
cadCmtsCmStatusMacNumTotal = _CadCmtsCmStatusMacNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 17),
    _CadCmtsCmStatusMacNumTotal_Type()
)
cadCmtsCmStatusMacNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumTotal.setStatus("deprecated")
_CadCmtsCmStatusMacNumRangingAborted_Type = Integer32
_CadCmtsCmStatusMacNumRangingAborted_Object = MibTableColumn
cadCmtsCmStatusMacNumRangingAborted = _CadCmtsCmStatusMacNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 18),
    _CadCmtsCmStatusMacNumRangingAborted_Type()
)
cadCmtsCmStatusMacNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRangingAborted.setStatus("deprecated")
_CadCmtsCmStatusMacNumRangFlaps_Type = Integer32
_CadCmtsCmStatusMacNumRangFlaps_Object = MibTableColumn
cadCmtsCmStatusMacNumRangFlaps = _CadCmtsCmStatusMacNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 19),
    _CadCmtsCmStatusMacNumRangFlaps_Type()
)
cadCmtsCmStatusMacNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRangFlaps.setStatus("deprecated")
_CadCmtsCmStatusMacNumProvFlaps_Type = Integer32
_CadCmtsCmStatusMacNumProvFlaps_Object = MibTableColumn
cadCmtsCmStatusMacNumProvFlaps = _CadCmtsCmStatusMacNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 20),
    _CadCmtsCmStatusMacNumProvFlaps_Type()
)
cadCmtsCmStatusMacNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumProvFlaps.setStatus("deprecated")
_CadCmtsCmStatusMacNumRegFlaps_Type = Integer32
_CadCmtsCmStatusMacNumRegFlaps_Object = MibTableColumn
cadCmtsCmStatusMacNumRegFlaps = _CadCmtsCmStatusMacNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 26, 1, 21),
    _CadCmtsCmStatusMacNumRegFlaps_Type()
)
cadCmtsCmStatusMacNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacNumRegFlaps.setStatus("deprecated")
_CadCmtsCmStatusMacChSummaryTable_Object = MibTable
cadCmtsCmStatusMacChSummaryTable = _CadCmtsCmStatusMacChSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27)
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChSummaryTable.setStatus("current")
_CadCmtsCmStatusMacChSummaryEntry_Object = MibTableRow
cadCmtsCmStatusMacChSummaryEntry = _CadCmtsCmStatusMacChSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1)
)
cadCmtsCmStatusMacChSummaryEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacChlChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChSummaryEntry.setStatus("current")
_CadCmtsCmStatusMacChNumOther_Type = Integer32
_CadCmtsCmStatusMacChNumOther_Object = MibTableColumn
cadCmtsCmStatusMacChNumOther = _CadCmtsCmStatusMacChNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 1),
    _CadCmtsCmStatusMacChNumOther_Type()
)
cadCmtsCmStatusMacChNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumOther.setStatus("current")
_CadCmtsCmStatusMacChNumInitRanging_Type = Integer32
_CadCmtsCmStatusMacChNumInitRanging_Object = MibTableColumn
cadCmtsCmStatusMacChNumInitRanging = _CadCmtsCmStatusMacChNumInitRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 2),
    _CadCmtsCmStatusMacChNumInitRanging_Type()
)
cadCmtsCmStatusMacChNumInitRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumInitRanging.setStatus("current")
_CadCmtsCmStatusMacChNumRangingComplete_Type = Integer32
_CadCmtsCmStatusMacChNumRangingComplete_Object = MibTableColumn
cadCmtsCmStatusMacChNumRangingComplete = _CadCmtsCmStatusMacChNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 3),
    _CadCmtsCmStatusMacChNumRangingComplete_Type()
)
cadCmtsCmStatusMacChNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRangingComplete.setStatus("current")
_CadCmtsCmStatusMacChNumStartEae_Type = Integer32
_CadCmtsCmStatusMacChNumStartEae_Object = MibTableColumn
cadCmtsCmStatusMacChNumStartEae = _CadCmtsCmStatusMacChNumStartEae_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 4),
    _CadCmtsCmStatusMacChNumStartEae_Type()
)
cadCmtsCmStatusMacChNumStartEae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumStartEae.setStatus("current")
_CadCmtsCmStatusMacChNumStartDhcpv4_Type = Integer32
_CadCmtsCmStatusMacChNumStartDhcpv4_Object = MibTableColumn
cadCmtsCmStatusMacChNumStartDhcpv4 = _CadCmtsCmStatusMacChNumStartDhcpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 5),
    _CadCmtsCmStatusMacChNumStartDhcpv4_Type()
)
cadCmtsCmStatusMacChNumStartDhcpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumStartDhcpv4.setStatus("current")
_CadCmtsCmStatusMacChNumStartDhcpv6_Type = Integer32
_CadCmtsCmStatusMacChNumStartDhcpv6_Object = MibTableColumn
cadCmtsCmStatusMacChNumStartDhcpv6 = _CadCmtsCmStatusMacChNumStartDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 6),
    _CadCmtsCmStatusMacChNumStartDhcpv6_Type()
)
cadCmtsCmStatusMacChNumStartDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumStartDhcpv6.setStatus("current")
_CadCmtsCmStatusMacChNumDhcpv4Complete_Type = Integer32
_CadCmtsCmStatusMacChNumDhcpv4Complete_Object = MibTableColumn
cadCmtsCmStatusMacChNumDhcpv4Complete = _CadCmtsCmStatusMacChNumDhcpv4Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 7),
    _CadCmtsCmStatusMacChNumDhcpv4Complete_Type()
)
cadCmtsCmStatusMacChNumDhcpv4Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumDhcpv4Complete.setStatus("current")
_CadCmtsCmStatusMacChNumDhcpv6Complete_Type = Integer32
_CadCmtsCmStatusMacChNumDhcpv6Complete_Object = MibTableColumn
cadCmtsCmStatusMacChNumDhcpv6Complete = _CadCmtsCmStatusMacChNumDhcpv6Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 8),
    _CadCmtsCmStatusMacChNumDhcpv6Complete_Type()
)
cadCmtsCmStatusMacChNumDhcpv6Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumDhcpv6Complete.setStatus("current")
_CadCmtsCmStatusMacChNumStartCfgFileDownload_Type = Integer32
_CadCmtsCmStatusMacChNumStartCfgFileDownload_Object = MibTableColumn
cadCmtsCmStatusMacChNumStartCfgFileDownload = _CadCmtsCmStatusMacChNumStartCfgFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 9),
    _CadCmtsCmStatusMacChNumStartCfgFileDownload_Type()
)
cadCmtsCmStatusMacChNumStartCfgFileDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumStartCfgFileDownload.setStatus("current")
_CadCmtsCmStatusMacChNumCfgFileDownloadComplete_Type = Integer32
_CadCmtsCmStatusMacChNumCfgFileDownloadComplete_Object = MibTableColumn
cadCmtsCmStatusMacChNumCfgFileDownloadComplete = _CadCmtsCmStatusMacChNumCfgFileDownloadComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 10),
    _CadCmtsCmStatusMacChNumCfgFileDownloadComplete_Type()
)
cadCmtsCmStatusMacChNumCfgFileDownloadComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumCfgFileDownloadComplete.setStatus("current")
_CadCmtsCmStatusMacChNumStartRegistration_Type = Integer32
_CadCmtsCmStatusMacChNumStartRegistration_Object = MibTableColumn
cadCmtsCmStatusMacChNumStartRegistration = _CadCmtsCmStatusMacChNumStartRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 11),
    _CadCmtsCmStatusMacChNumStartRegistration_Type()
)
cadCmtsCmStatusMacChNumStartRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumStartRegistration.setStatus("current")
_CadCmtsCmStatusMacChNumRegistrationComplete_Type = Integer32
_CadCmtsCmStatusMacChNumRegistrationComplete_Object = MibTableColumn
cadCmtsCmStatusMacChNumRegistrationComplete = _CadCmtsCmStatusMacChNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 12),
    _CadCmtsCmStatusMacChNumRegistrationComplete_Type()
)
cadCmtsCmStatusMacChNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRegistrationComplete.setStatus("current")
_CadCmtsCmStatusMacChNumOperational_Type = Integer32
_CadCmtsCmStatusMacChNumOperational_Object = MibTableColumn
cadCmtsCmStatusMacChNumOperational = _CadCmtsCmStatusMacChNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 13),
    _CadCmtsCmStatusMacChNumOperational_Type()
)
cadCmtsCmStatusMacChNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumOperational.setStatus("current")
_CadCmtsCmStatusMacChNumBpiInit_Type = Integer32
_CadCmtsCmStatusMacChNumBpiInit_Object = MibTableColumn
cadCmtsCmStatusMacChNumBpiInit = _CadCmtsCmStatusMacChNumBpiInit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 14),
    _CadCmtsCmStatusMacChNumBpiInit_Type()
)
cadCmtsCmStatusMacChNumBpiInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumBpiInit.setStatus("current")
_CadCmtsCmStatusMacChNumForwardingDisabled_Type = Integer32
_CadCmtsCmStatusMacChNumForwardingDisabled_Object = MibTableColumn
cadCmtsCmStatusMacChNumForwardingDisabled = _CadCmtsCmStatusMacChNumForwardingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 15),
    _CadCmtsCmStatusMacChNumForwardingDisabled_Type()
)
cadCmtsCmStatusMacChNumForwardingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumForwardingDisabled.setStatus("current")
_CadCmtsCmStatusMacChNumRfMuteAll_Type = Integer32
_CadCmtsCmStatusMacChNumRfMuteAll_Object = MibTableColumn
cadCmtsCmStatusMacChNumRfMuteAll = _CadCmtsCmStatusMacChNumRfMuteAll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 16),
    _CadCmtsCmStatusMacChNumRfMuteAll_Type()
)
cadCmtsCmStatusMacChNumRfMuteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRfMuteAll.setStatus("current")
_CadCmtsCmStatusMacChNumTotal_Type = Integer32
_CadCmtsCmStatusMacChNumTotal_Object = MibTableColumn
cadCmtsCmStatusMacChNumTotal = _CadCmtsCmStatusMacChNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 17),
    _CadCmtsCmStatusMacChNumTotal_Type()
)
cadCmtsCmStatusMacChNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumTotal.setStatus("current")
_CadCmtsCmStatusMacChNumRangingAborted_Type = Integer32
_CadCmtsCmStatusMacChNumRangingAborted_Object = MibTableColumn
cadCmtsCmStatusMacChNumRangingAborted = _CadCmtsCmStatusMacChNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 18),
    _CadCmtsCmStatusMacChNumRangingAborted_Type()
)
cadCmtsCmStatusMacChNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRangingAborted.setStatus("current")
_CadCmtsCmStatusMacChNumRangFlaps_Type = Integer32
_CadCmtsCmStatusMacChNumRangFlaps_Object = MibTableColumn
cadCmtsCmStatusMacChNumRangFlaps = _CadCmtsCmStatusMacChNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 19),
    _CadCmtsCmStatusMacChNumRangFlaps_Type()
)
cadCmtsCmStatusMacChNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRangFlaps.setStatus("current")
_CadCmtsCmStatusMacChNumProvFlaps_Type = Integer32
_CadCmtsCmStatusMacChNumProvFlaps_Object = MibTableColumn
cadCmtsCmStatusMacChNumProvFlaps = _CadCmtsCmStatusMacChNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 20),
    _CadCmtsCmStatusMacChNumProvFlaps_Type()
)
cadCmtsCmStatusMacChNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumProvFlaps.setStatus("current")
_CadCmtsCmStatusMacChNumRegFlaps_Type = Integer32
_CadCmtsCmStatusMacChNumRegFlaps_Object = MibTableColumn
cadCmtsCmStatusMacChNumRegFlaps = _CadCmtsCmStatusMacChNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 27, 1, 21),
    _CadCmtsCmStatusMacChNumRegFlaps_Type()
)
cadCmtsCmStatusMacChNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmStatusMacChNumRegFlaps.setStatus("current")
_CadQosServiceFlowSidClusterTable_Object = MibTable
cadQosServiceFlowSidClusterTable = _CadQosServiceFlowSidClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28)
)
if mibBuilder.loadTexts:
    cadQosServiceFlowSidClusterTable.setStatus("current")
_CadQosServiceFlowSidClusterEntry_Object = MibTableRow
cadQosServiceFlowSidClusterEntry = _CadQosServiceFlowSidClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28, 1)
)
cadQosServiceFlowSidClusterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowSidClusterId"),
    (0, "CADANT-CMTS-MAC-MIB", "cadQosServiceFlowSidClusterChIfIndex"),
)
if mibBuilder.loadTexts:
    cadQosServiceFlowSidClusterEntry.setStatus("current")
_CadQosServiceFlowSidClusterChIfIndex_Type = InterfaceIndex
_CadQosServiceFlowSidClusterChIfIndex_Object = MibTableColumn
cadQosServiceFlowSidClusterChIfIndex = _CadQosServiceFlowSidClusterChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28, 1, 1),
    _CadQosServiceFlowSidClusterChIfIndex_Type()
)
cadQosServiceFlowSidClusterChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadQosServiceFlowSidClusterChIfIndex.setStatus("current")


class _CadQosServiceFlowSidClusterUcid_Type(Integer32):
    """Custom type cadQosServiceFlowSidClusterUcid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadQosServiceFlowSidClusterUcid_Type.__name__ = "Integer32"
_CadQosServiceFlowSidClusterUcid_Object = MibTableColumn
cadQosServiceFlowSidClusterUcid = _CadQosServiceFlowSidClusterUcid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28, 1, 2),
    _CadQosServiceFlowSidClusterUcid_Type()
)
cadQosServiceFlowSidClusterUcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosServiceFlowSidClusterUcid.setStatus("current")


class _CadQosServiceFlowSidClusterSid_Type(Unsigned32):
    """Custom type cadQosServiceFlowSidClusterSid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CadQosServiceFlowSidClusterSid_Type.__name__ = "Unsigned32"
_CadQosServiceFlowSidClusterSid_Object = MibTableColumn
cadQosServiceFlowSidClusterSid = _CadQosServiceFlowSidClusterSid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28, 1, 3),
    _CadQosServiceFlowSidClusterSid_Type()
)
cadQosServiceFlowSidClusterSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosServiceFlowSidClusterSid.setStatus("current")


class _CadQosServiceFlowSegHdr_Type(Integer32):
    """Custom type cadQosServiceFlowSegHdr based on Integer32"""
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


_CadQosServiceFlowSegHdr_Type.__name__ = "Integer32"
_CadQosServiceFlowSegHdr_Object = MibTableColumn
cadQosServiceFlowSegHdr = _CadQosServiceFlowSegHdr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 28, 1, 4),
    _CadQosServiceFlowSegHdr_Type()
)
cadQosServiceFlowSegHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosServiceFlowSegHdr.setStatus("current")
_CadIfCmtsMacToInetIpTable_Object = MibTable
cadIfCmtsMacToInetIpTable = _CadIfCmtsMacToInetIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 29)
)
if mibBuilder.loadTexts:
    cadIfCmtsMacToInetIpTable.setStatus("current")
_CadIfCmtsMacToInetIpEntry_Object = MibTableRow
cadIfCmtsMacToInetIpEntry = _CadIfCmtsMacToInetIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 29, 1)
)
cadIfCmtsMacToInetIpEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsMacAddr"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsMacToInetIpAddrType"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsMacToInetIpAddr"),
)
if mibBuilder.loadTexts:
    cadIfCmtsMacToInetIpEntry.setStatus("current")
_CadIfCmtsMacToInetIpAddrType_Type = InetAddressType
_CadIfCmtsMacToInetIpAddrType_Object = MibTableColumn
cadIfCmtsMacToInetIpAddrType = _CadIfCmtsMacToInetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 29, 1, 1),
    _CadIfCmtsMacToInetIpAddrType_Type()
)
cadIfCmtsMacToInetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsMacToInetIpAddrType.setStatus("current")
_CadIfCmtsMacToInetIpAddr_Type = InetAddressIPv4or6
_CadIfCmtsMacToInetIpAddr_Object = MibTableColumn
cadIfCmtsMacToInetIpAddr = _CadIfCmtsMacToInetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 29, 1, 2),
    _CadIfCmtsMacToInetIpAddr_Type()
)
cadIfCmtsMacToInetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsMacToInetIpAddr.setStatus("current")
_CadIfCmtsMacToInetIpCmMacAddr_Type = MacAddress
_CadIfCmtsMacToInetIpCmMacAddr_Object = MibTableColumn
cadIfCmtsMacToInetIpCmMacAddr = _CadIfCmtsMacToInetIpCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 29, 1, 3),
    _CadIfCmtsMacToInetIpCmMacAddr_Type()
)
cadIfCmtsMacToInetIpCmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsMacToInetIpCmMacAddr.setStatus("current")
_CadEnforceRule_ObjectIdentity = ObjectIdentity
cadEnforceRule = _CadEnforceRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30)
)
_CadEnforceRuleTableLastChange_Type = Counter32
_CadEnforceRuleTableLastChange_Object = MibScalar
cadEnforceRuleTableLastChange = _CadEnforceRuleTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 1),
    _CadEnforceRuleTableLastChange_Type()
)
cadEnforceRuleTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEnforceRuleTableLastChange.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRuleTableLastChange.setUnits("seconds")
_CadEnforceRuleTable_Object = MibTable
cadEnforceRuleTable = _CadEnforceRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2)
)
if mibBuilder.loadTexts:
    cadEnforceRuleTable.setStatus("current")
_CadEnforceRuleEntry_Object = MibTableRow
cadEnforceRuleEntry = _CadEnforceRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1)
)
cadEnforceRuleEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadEnforceRuleReferenceSCN"),
)
if mibBuilder.loadTexts:
    cadEnforceRuleEntry.setStatus("current")


class _CadEnforceRuleReferenceSCN_Type(SnmpAdminString):
    """Custom type cadEnforceRuleReferenceSCN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CadEnforceRuleReferenceSCN_Type.__name__ = "SnmpAdminString"
_CadEnforceRuleReferenceSCN_Object = MibTableColumn
cadEnforceRuleReferenceSCN = _CadEnforceRuleReferenceSCN_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 1),
    _CadEnforceRuleReferenceSCN_Type()
)
cadEnforceRuleReferenceSCN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadEnforceRuleReferenceSCN.setStatus("current")


class _CadEnforceRuleEnforceSCN_Type(SnmpAdminString):
    """Custom type cadEnforceRuleEnforceSCN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CadEnforceRuleEnforceSCN_Type.__name__ = "SnmpAdminString"
_CadEnforceRuleEnforceSCN_Object = MibTableColumn
cadEnforceRuleEnforceSCN = _CadEnforceRuleEnforceSCN_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 2),
    _CadEnforceRuleEnforceSCN_Type()
)
cadEnforceRuleEnforceSCN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRuleEnforceSCN.setStatus("current")


class _CadEnforceRuleAvgBwRateUsageTrigger_Type(Integer32):
    """Custom type cadEnforceRuleAvgBwRateUsageTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500000),
    )


_CadEnforceRuleAvgBwRateUsageTrigger_Type.__name__ = "Integer32"
_CadEnforceRuleAvgBwRateUsageTrigger_Object = MibTableColumn
cadEnforceRuleAvgBwRateUsageTrigger = _CadEnforceRuleAvgBwRateUsageTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 3),
    _CadEnforceRuleAvgBwRateUsageTrigger_Type()
)
cadEnforceRuleAvgBwRateUsageTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRuleAvgBwRateUsageTrigger.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRuleAvgBwRateUsageTrigger.setUnits("kilobits per second")


class _CadEnforceRuleAvgHistoryDuration_Type(Integer32):
    """Custom type cadEnforceRuleAvgHistoryDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_CadEnforceRuleAvgHistoryDuration_Type.__name__ = "Integer32"
_CadEnforceRuleAvgHistoryDuration_Object = MibTableColumn
cadEnforceRuleAvgHistoryDuration = _CadEnforceRuleAvgHistoryDuration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 4),
    _CadEnforceRuleAvgHistoryDuration_Type()
)
cadEnforceRuleAvgHistoryDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRuleAvgHistoryDuration.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRuleAvgHistoryDuration.setUnits("minutes")


class _CadEnforceRuleSamplingInterval_Type(Integer32):
    """Custom type cadEnforceRuleSamplingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(30, 30),
    )


_CadEnforceRuleSamplingInterval_Type.__name__ = "Integer32"
_CadEnforceRuleSamplingInterval_Object = MibTableColumn
cadEnforceRuleSamplingInterval = _CadEnforceRuleSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 5),
    _CadEnforceRuleSamplingInterval_Type()
)
cadEnforceRuleSamplingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRuleSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRuleSamplingInterval.setUnits("minutes")


class _CadEnforceRulePenaltyDuration_Type(Integer32):
    """Custom type cadEnforceRulePenaltyDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_CadEnforceRulePenaltyDuration_Type.__name__ = "Integer32"
_CadEnforceRulePenaltyDuration_Object = MibTableColumn
cadEnforceRulePenaltyDuration = _CadEnforceRulePenaltyDuration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 6),
    _CadEnforceRulePenaltyDuration_Type()
)
cadEnforceRulePenaltyDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRulePenaltyDuration.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRulePenaltyDuration.setUnits("minutes")
_CadEnforceRuleCreateTime_Type = Counter32
_CadEnforceRuleCreateTime_Object = MibTableColumn
cadEnforceRuleCreateTime = _CadEnforceRuleCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 7),
    _CadEnforceRuleCreateTime_Type()
)
cadEnforceRuleCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEnforceRuleCreateTime.setStatus("current")
if mibBuilder.loadTexts:
    cadEnforceRuleCreateTime.setUnits("seconds")
_CadEnforceRuleStatus_Type = RowStatus
_CadEnforceRuleStatus_Object = MibTableColumn
cadEnforceRuleStatus = _CadEnforceRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 2, 1, 8),
    _CadEnforceRuleStatus_Type()
)
cadEnforceRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEnforceRuleStatus.setStatus("current")
_CadEnforceRuleCountsTable_Object = MibTable
cadEnforceRuleCountsTable = _CadEnforceRuleCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 3)
)
if mibBuilder.loadTexts:
    cadEnforceRuleCountsTable.setStatus("current")
_CadEnforceRuleCountsEntry_Object = MibTableRow
cadEnforceRuleCountsEntry = _CadEnforceRuleCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 3, 1)
)
if mibBuilder.loadTexts:
    cadEnforceRuleCountsEntry.setStatus("current")
_CadEnforceRuleCountsPenalties_Type = Counter32
_CadEnforceRuleCountsPenalties_Object = MibTableColumn
cadEnforceRuleCountsPenalties = _CadEnforceRuleCountsPenalties_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 30, 3, 1, 1),
    _CadEnforceRuleCountsPenalties_Type()
)
cadEnforceRuleCountsPenalties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEnforceRuleCountsPenalties.setStatus("current")
_CadQosServiceClassControl_ObjectIdentity = ObjectIdentity
cadQosServiceClassControl = _CadQosServiceClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31)
)
_CadQosServiceClassControlTable_Object = MibTable
cadQosServiceClassControlTable = _CadQosServiceClassControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 1)
)
if mibBuilder.loadTexts:
    cadQosServiceClassControlTable.setStatus("current")
_CadQosServiceClassControlEntry_Object = MibTableRow
cadQosServiceClassControlEntry = _CadQosServiceClassControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 1, 1)
)
if mibBuilder.loadTexts:
    cadQosServiceClassControlEntry.setStatus("current")


class _CadQosServiceClassControlSendDsc_Type(TruthValue):
    """Custom type cadQosServiceClassControlSendDsc based on TruthValue"""


_CadQosServiceClassControlSendDsc_Object = MibTableColumn
cadQosServiceClassControlSendDsc = _CadQosServiceClassControlSendDsc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 1, 1, 1),
    _CadQosServiceClassControlSendDsc_Type()
)
cadQosServiceClassControlSendDsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadQosServiceClassControlSendDsc.setStatus("current")
_CadQosServiceClassControlSendDscLastUpdated_Type = TimeStamp
_CadQosServiceClassControlSendDscLastUpdated_Object = MibTableColumn
cadQosServiceClassControlSendDscLastUpdated = _CadQosServiceClassControlSendDscLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 1, 1, 2),
    _CadQosServiceClassControlSendDscLastUpdated_Type()
)
cadQosServiceClassControlSendDscLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosServiceClassControlSendDscLastUpdated.setStatus("current")
_CadQosServiceClassCmControlTable_Object = MibTable
cadQosServiceClassCmControlTable = _CadQosServiceClassCmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 2)
)
if mibBuilder.loadTexts:
    cadQosServiceClassCmControlTable.setStatus("current")
_CadQosServiceClassCmControlEntry_Object = MibTableRow
cadQosServiceClassCmControlEntry = _CadQosServiceClassCmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 2, 1)
)
if mibBuilder.loadTexts:
    cadQosServiceClassCmControlEntry.setStatus("current")


class _CadQosServiceClassCmControlSendDscMacAddr_Type(MacAddress):
    """Custom type cadQosServiceClassCmControlSendDscMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CadQosServiceClassCmControlSendDscMacAddr_Object = MibTableColumn
cadQosServiceClassCmControlSendDscMacAddr = _CadQosServiceClassCmControlSendDscMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 31, 2, 1, 1),
    _CadQosServiceClassCmControlSendDscMacAddr_Type()
)
cadQosServiceClassCmControlSendDscMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadQosServiceClassCmControlSendDscMacAddr.setStatus("current")
_CadIfCmtsCmOfdmStatusTable_Object = MibTable
cadIfCmtsCmOfdmStatusTable = _CadIfCmtsCmOfdmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32)
)
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusTable.setStatus("current")
_CadIfCmtsCmOfdmStatusEntry_Object = MibTableRow
cadIfCmtsCmOfdmStatusEntry = _CadIfCmtsCmOfdmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1)
)
cadIfCmtsCmOfdmStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmOfdmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusEntry.setStatus("current")
_CadIfCmtsCmOfdmStatusMacAddress_Type = MacAddress
_CadIfCmtsCmOfdmStatusMacAddress_Object = MibTableColumn
cadIfCmtsCmOfdmStatusMacAddress = _CadIfCmtsCmOfdmStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 1),
    _CadIfCmtsCmOfdmStatusMacAddress_Type()
)
cadIfCmtsCmOfdmStatusMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusMacAddress.setStatus("current")
_CadIfCmtsCmOfdmStatusOkOfdmMod_Type = CerOfdmModBitsType
_CadIfCmtsCmOfdmStatusOkOfdmMod_Object = MibTableColumn
cadIfCmtsCmOfdmStatusOkOfdmMod = _CadIfCmtsCmOfdmStatusOkOfdmMod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 2),
    _CadIfCmtsCmOfdmStatusOkOfdmMod_Type()
)
cadIfCmtsCmOfdmStatusOkOfdmMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusOkOfdmMod.setStatus("current")
_CadIfCmtsCmOfdmStatusOkOfdmaMod_Type = CerOfdmModBitsType
_CadIfCmtsCmOfdmStatusOkOfdmaMod_Object = MibTableColumn
cadIfCmtsCmOfdmStatusOkOfdmaMod = _CadIfCmtsCmOfdmStatusOkOfdmaMod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 3),
    _CadIfCmtsCmOfdmStatusOkOfdmaMod_Type()
)
cadIfCmtsCmOfdmStatusOkOfdmaMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusOkOfdmaMod.setStatus("current")
_CadIfCmtsCmOfdmStatusDsLowFreq_Type = Integer32
_CadIfCmtsCmOfdmStatusDsLowFreq_Object = MibTableColumn
cadIfCmtsCmOfdmStatusDsLowFreq = _CadIfCmtsCmOfdmStatusDsLowFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 4),
    _CadIfCmtsCmOfdmStatusDsLowFreq_Type()
)
cadIfCmtsCmOfdmStatusDsLowFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusDsLowFreq.setStatus("current")
_CadIfCmtsCmOfdmStatusDsHighFreq_Type = Integer32
_CadIfCmtsCmOfdmStatusDsHighFreq_Object = MibTableColumn
cadIfCmtsCmOfdmStatusDsHighFreq = _CadIfCmtsCmOfdmStatusDsHighFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 5),
    _CadIfCmtsCmOfdmStatusDsHighFreq_Type()
)
cadIfCmtsCmOfdmStatusDsHighFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusDsHighFreq.setStatus("current")
_CadIfCmtsCmOfdmStatusUsHighFreq_Type = Integer32
_CadIfCmtsCmOfdmStatusUsHighFreq_Object = MibTableColumn
cadIfCmtsCmOfdmStatusUsHighFreq = _CadIfCmtsCmOfdmStatusUsHighFreq_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 32, 1, 6),
    _CadIfCmtsCmOfdmStatusUsHighFreq_Type()
)
cadIfCmtsCmOfdmStatusUsHighFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmStatusUsHighFreq.setStatus("current")
_CadIfCmtsCmOfdmProfTable_Object = MibTable
cadIfCmtsCmOfdmProfTable = _CadIfCmtsCmOfdmProfTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33)
)
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfTable.setStatus("current")
_CadIfCmtsCmOfdmProfEntry_Object = MibTableRow
cadIfCmtsCmOfdmProfEntry = _CadIfCmtsCmOfdmProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1)
)
cadIfCmtsCmOfdmProfEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmOfdmProfMacAddress"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmOfdmProfIfIndex"),
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmOfdmProfProfId"),
)
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfEntry.setStatus("current")
_CadIfCmtsCmOfdmProfMacAddress_Type = MacAddress
_CadIfCmtsCmOfdmProfMacAddress_Object = MibTableColumn
cadIfCmtsCmOfdmProfMacAddress = _CadIfCmtsCmOfdmProfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1, 1),
    _CadIfCmtsCmOfdmProfMacAddress_Type()
)
cadIfCmtsCmOfdmProfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfMacAddress.setStatus("current")
_CadIfCmtsCmOfdmProfIfIndex_Type = InterfaceIndex
_CadIfCmtsCmOfdmProfIfIndex_Object = MibTableColumn
cadIfCmtsCmOfdmProfIfIndex = _CadIfCmtsCmOfdmProfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1, 2),
    _CadIfCmtsCmOfdmProfIfIndex_Type()
)
cadIfCmtsCmOfdmProfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfIfIndex.setStatus("current")
_CadIfCmtsCmOfdmProfProfId_Type = OfdmProfileId
_CadIfCmtsCmOfdmProfProfId_Object = MibTableColumn
cadIfCmtsCmOfdmProfProfId = _CadIfCmtsCmOfdmProfProfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1, 3),
    _CadIfCmtsCmOfdmProfProfId_Type()
)
cadIfCmtsCmOfdmProfProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfProfId.setStatus("current")
_CadIfCmtsCmOfdmProfDirection_Type = IfDirection
_CadIfCmtsCmOfdmProfDirection_Object = MibTableColumn
cadIfCmtsCmOfdmProfDirection = _CadIfCmtsCmOfdmProfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1, 4),
    _CadIfCmtsCmOfdmProfDirection_Type()
)
cadIfCmtsCmOfdmProfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfDirection.setStatus("current")


class _CadIfCmtsCmOfdmProfStatus_Type(Integer32):
    """Custom type cadIfCmtsCmOfdmProfStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("impaired", 2))
    )


_CadIfCmtsCmOfdmProfStatus_Type.__name__ = "Integer32"
_CadIfCmtsCmOfdmProfStatus_Object = MibTableColumn
cadIfCmtsCmOfdmProfStatus = _CadIfCmtsCmOfdmProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 33, 1, 5),
    _CadIfCmtsCmOfdmProfStatus_Type()
)
cadIfCmtsCmOfdmProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsCmOfdmProfStatus.setStatus("current")
_CadSubmgtFilterGrpDescTable_Object = MibTable
cadSubmgtFilterGrpDescTable = _CadSubmgtFilterGrpDescTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 34)
)
if mibBuilder.loadTexts:
    cadSubmgtFilterGrpDescTable.setStatus("current")
_CadSubmgtFilterGrpDescEntry_Object = MibTableRow
cadSubmgtFilterGrpDescEntry = _CadSubmgtFilterGrpDescEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 34, 1)
)
cadSubmgtFilterGrpDescEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadSubmgtFilterGrpId"),
)
if mibBuilder.loadTexts:
    cadSubmgtFilterGrpDescEntry.setStatus("current")


class _CadSubmgtFilterGrpId_Type(Unsigned32):
    """Custom type cadSubmgtFilterGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CadSubmgtFilterGrpId_Type.__name__ = "Unsigned32"
_CadSubmgtFilterGrpId_Object = MibTableColumn
cadSubmgtFilterGrpId = _CadSubmgtFilterGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 34, 1, 1),
    _CadSubmgtFilterGrpId_Type()
)
cadSubmgtFilterGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSubmgtFilterGrpId.setStatus("current")


class _CadSubmgtFilterGrpDescription_Type(SnmpAdminString):
    """Custom type cadSubmgtFilterGrpDescription based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadSubmgtFilterGrpDescription_Type.__name__ = "SnmpAdminString"
_CadSubmgtFilterGrpDescription_Object = MibTableColumn
cadSubmgtFilterGrpDescription = _CadSubmgtFilterGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 34, 1, 2),
    _CadSubmgtFilterGrpDescription_Type()
)
cadSubmgtFilterGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSubmgtFilterGrpDescription.setStatus("current")
_CadSubmgtFilterGrpRowStatus_Type = RowStatus
_CadSubmgtFilterGrpRowStatus_Object = MibTableColumn
cadSubmgtFilterGrpRowStatus = _CadSubmgtFilterGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 2, 34, 1, 3),
    _CadSubmgtFilterGrpRowStatus_Type()
)
cadSubmgtFilterGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSubmgtFilterGrpRowStatus.setStatus("current")
cadIfCmtsCmStatusEntry.registerAugmentions(
    ("CADANT-CMTS-MAC-MIB",
     "cadSubMgtCpeControlEntry")
)
cadSubMgtCpeControlEntry.setIndexNames(*cadIfCmtsCmStatusEntry.getIndexNames())
docsQosServiceClassEntry.registerAugmentions(
    ("CADANT-CMTS-MAC-MIB",
     "cadQosServiceClassEntry")
)
cadQosServiceClassEntry.setIndexNames(*docsQosServiceClassEntry.getIndexNames())
cadEnforceRuleEntry.registerAugmentions(
    ("CADANT-CMTS-MAC-MIB",
     "cadEnforceRuleCountsEntry")
)
cadEnforceRuleCountsEntry.setIndexNames(*cadEnforceRuleEntry.getIndexNames())
docsQosServiceClassEntry.registerAugmentions(
    ("CADANT-CMTS-MAC-MIB",
     "cadQosServiceClassControlEntry")
)
cadQosServiceClassControlEntry.setIndexNames(*docsQosServiceClassEntry.getIndexNames())
docsQosServiceClassEntry.registerAugmentions(
    ("CADANT-CMTS-MAC-MIB",
     "cadQosServiceClassCmControlEntry")
)
cadQosServiceClassCmControlEntry.setIndexNames(*docsQosServiceClassEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-MAC-MIB",
    **{"CadIfCmtsCmStatusType": CadIfCmtsCmStatusType,
       "cadMacMib": cadMacMib,
       "cadIfCmtsCmStatusNumber": cadIfCmtsCmStatusNumber,
       "cadIfCmtsCmStatusTable": cadIfCmtsCmStatusTable,
       "cadIfCmtsCmStatusEntry": cadIfCmtsCmStatusEntry,
       "cadIfCmtsCmStatusMacAddress": cadIfCmtsCmStatusMacAddress,
       "cadIfCmtsCmStatusDownChannelIfIndex": cadIfCmtsCmStatusDownChannelIfIndex,
       "cadIfCmtsCmStatusUpChannelIfIndex": cadIfCmtsCmStatusUpChannelIfIndex,
       "cadIfCmtsCmStatusValue": cadIfCmtsCmStatusValue,
       "cadIfCmtsCmStatusDocsisVersion": cadIfCmtsCmStatusDocsisVersion,
       "cadIfCmtsCmStatusRangFlaps": cadIfCmtsCmStatusRangFlaps,
       "cadIfCmtsCmStatusProvFlaps": cadIfCmtsCmStatusProvFlaps,
       "cadIfCmtsCmStatusRegFlaps": cadIfCmtsCmStatusRegFlaps,
       "cadIfCmtsCmStatusLastFlapTime": cadIfCmtsCmStatusLastFlapTime,
       "cadIfCmtsCmStatusInitRangTime": cadIfCmtsCmStatusInitRangTime,
       "cadIfCmtsCmStatusPreFlapStatus": cadIfCmtsCmStatusPreFlapStatus,
       "cadIfCmtsCmStatusConfigFilename": cadIfCmtsCmStatusConfigFilename,
       "cadIfCmtsCmStatusBpiVersion": cadIfCmtsCmStatusBpiVersion,
       "cadIfCmtsCmStatusModemType": cadIfCmtsCmStatusModemType,
       "cadIfCmtsCmStatusModulationType": cadIfCmtsCmStatusModulationType,
       "cadIfCmtsCmStatusCmPtr": cadIfCmtsCmStatusCmPtr,
       "cadIfCmtsCmStatusTftpEnforceFailed": cadIfCmtsCmStatusTftpEnforceFailed,
       "cadIfCmtsCmStatusDynamicSecretFailed": cadIfCmtsCmStatusDynamicSecretFailed,
       "cadIfCmtsCmStatusDocsCapability": cadIfCmtsCmStatusDocsCapability,
       "cadIfCmtsCmStatusDocsProvisioned": cadIfCmtsCmStatusDocsProvisioned,
       "cadIfHVCmtsCmStatusLastFlapTime": cadIfHVCmtsCmStatusLastFlapTime,
       "cadIfHVCmtsCmStatusInitRangTime": cadIfHVCmtsCmStatusInitRangTime,
       "cadIf3CmtsCmRegStatusIPv6Addr": cadIf3CmtsCmRegStatusIPv6Addr,
       "cadIf3CmtsCmRegStatusIPv6LinkLocal": cadIf3CmtsCmRegStatusIPv6LinkLocal,
       "cadIf3CmtsCmRegStatusMdIfIndex": cadIf3CmtsCmRegStatusMdIfIndex,
       "cadIf3CmtsCmRegStatusMdCmSgId": cadIf3CmtsCmRegStatusMdCmSgId,
       "cadIf3CmtsCmRegStatusRcpId": cadIf3CmtsCmRegStatusRcpId,
       "cadIf3CmtsCmRegStatusRccStatusId": cadIf3CmtsCmRegStatusRccStatusId,
       "cadIf3CmtsCmRegStatusRcsId": cadIf3CmtsCmRegStatusRcsId,
       "cadIf3CmtsCmRegStatusTcsId": cadIf3CmtsCmRegStatusTcsId,
       "cadIf3CmtsCmRegStatusLastRegTime": cadIf3CmtsCmRegStatusLastRegTime,
       "cadIfCmtsCmStatusInetIpAddrType": cadIfCmtsCmStatusInetIpAddrType,
       "cadIfCmtsCmStatusInetIpAddress": cadIfCmtsCmStatusInetIpAddress,
       "cadIf3CmtsCmRegStatusServiceType": cadIf3CmtsCmRegStatusServiceType,
       "cadIfCmtsCmStatusBpiEnabled": cadIfCmtsCmStatusBpiEnabled,
       "cadIfCmtsCmStatuseDocsisTypes": cadIfCmtsCmStatuseDocsisTypes,
       "cadIfCmtsCmStatusDsPenalties": cadIfCmtsCmStatusDsPenalties,
       "cadIfCmtsCmStatusUsPenalties": cadIfCmtsCmStatusUsPenalties,
       "cadIfCmtsCmStatusLastDsPenaltyStart": cadIfCmtsCmStatusLastDsPenaltyStart,
       "cadIfCmtsCmStatusLastDsPenaltyDuration": cadIfCmtsCmStatusLastDsPenaltyDuration,
       "cadIfCmtsCmStatusLastUsPenaltyStart": cadIfCmtsCmStatusLastUsPenaltyStart,
       "cadIfCmtsCmStatusLastUsPenaltyDuration": cadIfCmtsCmStatusLastUsPenaltyDuration,
       "cadIfCmtsCmStatusRxAcPowerLost": cadIfCmtsCmStatusRxAcPowerLost,
       "cadIfCmtsCmStatusInsertionFlaps": cadIfCmtsCmStatusInsertionFlaps,
       "cadIf3CmtsCmRegStatusEnergyMgtCapability": cadIf3CmtsCmRegStatusEnergyMgtCapability,
       "cadIf3CmtsCmRegStatusEnergyMgtEnabled": cadIf3CmtsCmRegStatusEnergyMgtEnabled,
       "cadIf3CmtsCmRegStatusEnergyMgtOperStatus": cadIf3CmtsCmRegStatusEnergyMgtOperStatus,
       "cadIf3CmtsCmStatsEm1x1ModeTotalDuration": cadIf3CmtsCmStatsEm1x1ModeTotalDuration,
       "cadIf3CmtsCmStatsEm1x1ModeEntryTime": cadIf3CmtsCmStatsEm1x1ModeEntryTime,
       "cadIfCmtsCmCountsTable": cadIfCmtsCmCountsTable,
       "cadIfCmtsCmCountsEntry": cadIfCmtsCmCountsEntry,
       "cadIfCmtsCmCountsRxPower": cadIfCmtsCmCountsRxPower,
       "cadIfCmtsCmCountsTimingOffset": cadIfCmtsCmCountsTimingOffset,
       "cadIfCmtsCmCountsEqualizationData": cadIfCmtsCmCountsEqualizationData,
       "cadIfCmtsCmCountsRangeReqOpportunities": cadIfCmtsCmCountsRangeReqOpportunities,
       "cadIfCmtsCmCountsRangeReqReceived": cadIfCmtsCmCountsRangeReqReceived,
       "cadIfCmtsCmCountsPowerAdjExceedsThreshold": cadIfCmtsCmCountsPowerAdjExceedsThreshold,
       "cadIfCmtsCmCountsUpChIfIndex": cadIfCmtsCmCountsUpChIfIndex,
       "cadIfCmtsCmCountsSignalNoise": cadIfCmtsCmCountsSignalNoise,
       "cadIfCmtsCmCountsUnerroreds": cadIfCmtsCmCountsUnerroreds,
       "cadIfCmtsCmCountsCorrecteds": cadIfCmtsCmCountsCorrecteds,
       "cadIfCmtsCmCountsUncorrectables": cadIfCmtsCmCountsUncorrectables,
       "cadIfCmtsCmCountsTxPower": cadIfCmtsCmCountsTxPower,
       "cadIfCmtsServiceTable": cadIfCmtsServiceTable,
       "cadIfCmtsServiceEntry": cadIfCmtsServiceEntry,
       "cadIfCmtsServiceId": cadIfCmtsServiceId,
       "cadIfCmtsServiceMacAddress": cadIfCmtsServiceMacAddress,
       "cadIfCmtsServiceAdminStatus": cadIfCmtsServiceAdminStatus,
       "cadIfCmtsServiceQosProfile": cadIfCmtsServiceQosProfile,
       "cadIfCmtsServiceCreateTime": cadIfCmtsServiceCreateTime,
       "cadIfQosProfPriority": cadIfQosProfPriority,
       "cadIfQosProfMaxUpBandwidth": cadIfQosProfMaxUpBandwidth,
       "cadIfQosProfGuarUpBandwidth": cadIfQosProfGuarUpBandwidth,
       "cadIfQosProfMaxDownBandwidth": cadIfQosProfMaxDownBandwidth,
       "cadIfQosProfMaxTxBurst": cadIfQosProfMaxTxBurst,
       "cadIfQosProfBaselinePrivacy": cadIfQosProfBaselinePrivacy,
       "cadIfCmtsPtrToMacTable": cadIfCmtsPtrToMacTable,
       "cadIfCmtsPtrToMacEntry": cadIfCmtsPtrToMacEntry,
       "cadIfCmtsCmPtr": cadIfCmtsCmPtr,
       "cadIfCmtsCmMac": cadIfCmtsCmMac,
       "cadSubMgtCpeControlTable": cadSubMgtCpeControlTable,
       "cadSubMgtCpeControlEntry": cadSubMgtCpeControlEntry,
       "cadSubMgtCpeControlMaxCpeIpv4": cadSubMgtCpeControlMaxCpeIpv4,
       "cadSubMgtCpeControlActive": cadSubMgtCpeControlActive,
       "cadSubMgtCpeControlLearnable": cadSubMgtCpeControlLearnable,
       "cadSubMgtCpeControlReset": cadSubMgtCpeControlReset,
       "cadSubMgtCpeControlMaxCpeIpv6Addresses": cadSubMgtCpeControlMaxCpeIpv6Addresses,
       "cadSubMgtCpeControlLastReset": cadSubMgtCpeControlLastReset,
       "cadSubMgtCpeIpTable": cadSubMgtCpeIpTable,
       "cadSubMgtCpeIpEntry": cadSubMgtCpeIpEntry,
       "cadSubMgtCpeIpIndex": cadSubMgtCpeIpIndex,
       "cadSubMgtCpeIpAddr": cadSubMgtCpeIpAddr,
       "cadSubMgtCpeIpLearned": cadSubMgtCpeIpLearned,
       "cadSubMgtCpeIpMacAddr": cadSubMgtCpeIpMacAddr,
       "cadSubMgtCpeFilterDownstream": cadSubMgtCpeFilterDownstream,
       "cadSubMgtCpeFilterUpstream": cadSubMgtCpeFilterUpstream,
       "cadSubMgtCpeCpeType": cadSubMgtCpeCpeType,
       "cadSubMgtCpeIpAddrType": cadSubMgtCpeIpAddrType,
       "cadSubMgtCmFilterTable": cadSubMgtCmFilterTable,
       "cadSubMgtCmFilterEntry": cadSubMgtCmFilterEntry,
       "cadSubMgtSubFilterDownstream": cadSubMgtSubFilterDownstream,
       "cadSubMgtSubFilterUpstream": cadSubMgtSubFilterUpstream,
       "cadSubMgtCmFilterDownstream": cadSubMgtCmFilterDownstream,
       "cadSubMgtCmFilterUpstream": cadSubMgtCmFilterUpstream,
       "cadSubMgtPsFilterDownstream": cadSubMgtPsFilterDownstream,
       "cadSubMgtPsFilterUpstream": cadSubMgtPsFilterUpstream,
       "cadSubMgtMtaFilterDownstream": cadSubMgtMtaFilterDownstream,
       "cadSubMgtMtaFilterUpstream": cadSubMgtMtaFilterUpstream,
       "cadSubMgtStbFilterDownstream": cadSubMgtStbFilterDownstream,
       "cadSubMgtStbFilterUpstream": cadSubMgtStbFilterUpstream,
       "cadTpFdbTable": cadTpFdbTable,
       "cadTpFdbEntry": cadTpFdbEntry,
       "cadTpFdbAddress": cadTpFdbAddress,
       "cadTpFdbIfIndex": cadTpFdbIfIndex,
       "cadTpFdbStatus": cadTpFdbStatus,
       "cadIfQosProfileLookupTable": cadIfQosProfileLookupTable,
       "cadIfQosProfileLookupEntry": cadIfQosProfileLookupEntry,
       "cadIfQosProfileLookupIndex": cadIfQosProfileLookupIndex,
       "cadIfQosProfileLookupRefCount": cadIfQosProfileLookupRefCount,
       "cadChannelToCmTable": cadChannelToCmTable,
       "cadChannelToCmEntry": cadChannelToCmEntry,
       "cadChannelToCmPtr": cadChannelToCmPtr,
       "cadCmtsCmStatusSummaryTable": cadCmtsCmStatusSummaryTable,
       "cadCmtsCmStatusSummaryEntry": cadCmtsCmStatusSummaryEntry,
       "cadCmtsCmStatusNumOther": cadCmtsCmStatusNumOther,
       "cadCmtsCmStatusNumRanging": cadCmtsCmStatusNumRanging,
       "cadCmtsCmStatusNumRangingAborted": cadCmtsCmStatusNumRangingAborted,
       "cadCmtsCmStatusNumRangingComplete": cadCmtsCmStatusNumRangingComplete,
       "cadCmtsCmStatusNumIpComplete": cadCmtsCmStatusNumIpComplete,
       "cadCmtsCmStatusNumRegistrationComplete": cadCmtsCmStatusNumRegistrationComplete,
       "cadCmtsCmStatusNumAccessDenied": cadCmtsCmStatusNumAccessDenied,
       "cadCmtsCmStatusNumRangFlaps": cadCmtsCmStatusNumRangFlaps,
       "cadCmtsCmStatusNumProvFlaps": cadCmtsCmStatusNumProvFlaps,
       "cadCmtsCmStatusNumRegFlaps": cadCmtsCmStatusNumRegFlaps,
       "cadCmtsCmStatusNumOperational": cadCmtsCmStatusNumOperational,
       "cadCmtsCmStatusNumRegisteredBpiInitializing": cadCmtsCmStatusNumRegisteredBpiInitializing,
       "cadCmtsCmStatusNumTotal": cadCmtsCmStatusNumTotal,
       "cadCmtsCmStatusNumActive": cadCmtsCmStatusNumActive,
       "cadCmtsCmStatusNumRegistered": cadCmtsCmStatusNumRegistered,
       "cadArpTable": cadArpTable,
       "cadArpEntry": cadArpEntry,
       "cadArpIfIndex": cadArpIfIndex,
       "cadArpAddressType": cadArpAddressType,
       "cadArpNetAddress": cadArpNetAddress,
       "cadArpMacAddress": cadArpMacAddress,
       "cadArpType": cadArpType,
       "cadArpState": cadArpState,
       "cadArpL3IfIndex": cadArpL3IfIndex,
       "cadMacControl": cadMacControl,
       "cadMacClearFlapCounts": cadMacClearFlapCounts,
       "cadMacResetCMMacAddress": cadMacResetCMMacAddress,
       "cadMacDeleteMacAddress": cadMacDeleteMacAddress,
       "cadMacClearDenyCounts": cadMacClearDenyCounts,
       "cadMacClearDenyCountMacAddr": cadMacClearDenyCountMacAddr,
       "cadMacClearFlapCountMacAddr": cadMacClearFlapCountMacAddr,
       "cadMacRecalculateCmSummaryIfIndex": cadMacRecalculateCmSummaryIfIndex,
       "cadMacClearFlapCountsByIfIndex": cadMacClearFlapCountsByIfIndex,
       "cadMacClearPenaltyCounts": cadMacClearPenaltyCounts,
       "cadMacClearPenaltyCountsByIfIndex": cadMacClearPenaltyCountsByIfIndex,
       "cadMacClearPenaltyCountMacAddr": cadMacClearPenaltyCountMacAddr,
       "cadMacClearPenaltyCountScn": cadMacClearPenaltyCountScn,
       "cadQosCmtsMacToSrvFlowTable": cadQosCmtsMacToSrvFlowTable,
       "cadQosCmtsMacToSrvFlowEntry": cadQosCmtsMacToSrvFlowEntry,
       "cadQosCmtsCmMac": cadQosCmtsCmMac,
       "cadQosCmtsServiceFlowId": cadQosCmtsServiceFlowId,
       "cadQosCmtsIfIndex": cadQosCmtsIfIndex,
       "cadQosServiceClassTable": cadQosServiceClassTable,
       "cadQosServiceClassEntry": cadQosServiceClassEntry,
       "cadQosServiceClassPeakTrafficRate": cadQosServiceClassPeakTrafficRate,
       "cadQosServiceClassLatencyControlledFlowFlag": cadQosServiceClassLatencyControlledFlowFlag,
       "cadCmtsCmVendorTable": cadCmtsCmVendorTable,
       "cadCmtsCmVendorEntry": cadCmtsCmVendorEntry,
       "cadCmtsCmVendorOUI": cadCmtsCmVendorOUI,
       "cadCmtsCmVendorName": cadCmtsCmVendorName,
       "cadCmtsCmVendorRowStatus": cadCmtsCmVendorRowStatus,
       "cadIfCmtsMacToIpTable": cadIfCmtsMacToIpTable,
       "cadIfCmtsMacToIpEntry": cadIfCmtsMacToIpEntry,
       "cadIfCmtsMacAddr": cadIfCmtsMacAddr,
       "cadIfCmtsMacCmMacAddr": cadIfCmtsMacCmMacAddr,
       "cadIfCmtsMacInetIpAddr": cadIfCmtsMacInetIpAddr,
       "cadIfCmtsMacInetIpAddrType": cadIfCmtsMacInetIpAddrType,
       "cadCmDenyTable": cadCmDenyTable,
       "cadCmDenyEntry": cadCmDenyEntry,
       "cadCmDenyMacAddress": cadCmDenyMacAddress,
       "cadCmDenyRowStatus": cadCmDenyRowStatus,
       "cadCmDenyStatusTable": cadCmDenyStatusTable,
       "cadCmDenyStatusEntry": cadCmDenyStatusEntry,
       "cadCmDenyRecentIfIndex": cadCmDenyRecentIfIndex,
       "cadCmDenyRecentTime": cadCmDenyRecentTime,
       "cadCmDenyAttempts": cadCmDenyAttempts,
       "cadCpeHostAuthorizationTable": cadCpeHostAuthorizationTable,
       "cadCpeHostAuthorizationEntry": cadCpeHostAuthorizationEntry,
       "cadCpeHostAuthCmMacAddress": cadCpeHostAuthCmMacAddress,
       "cadCpeHostAuthCpeMacAddress": cadCpeHostAuthCpeMacAddress,
       "cadCpeHostAuthCpeIpAddress": cadCpeHostAuthCpeIpAddress,
       "cadCpeHostAuthRowStatus": cadCpeHostAuthRowStatus,
       "cadIfCmtsInetIpToCmMacTable": cadIfCmtsInetIpToCmMacTable,
       "cadIfCmtsInetIpToCmMacEntry": cadIfCmtsInetIpToCmMacEntry,
       "cadIfCmtsInetIpMacAddrType": cadIfCmtsInetIpMacAddrType,
       "cadIfCmtsInetIpMac": cadIfCmtsInetIpMac,
       "cadIfCmtsInetIpCmMac": cadIfCmtsInetIpCmMac,
       "cadIfCmtsInetIpCpeMac": cadIfCmtsInetIpCpeMac,
       "cadCmtsCmStatusMacSummaryTable": cadCmtsCmStatusMacSummaryTable,
       "cadCmtsCmStatusMacSummaryEntry": cadCmtsCmStatusMacSummaryEntry,
       "cadCmtsCmStatusMacNumOther": cadCmtsCmStatusMacNumOther,
       "cadCmtsCmStatusMacNumInitRanging": cadCmtsCmStatusMacNumInitRanging,
       "cadCmtsCmStatusMacNumRangingComplete": cadCmtsCmStatusMacNumRangingComplete,
       "cadCmtsCmStatusMacNumStartEae": cadCmtsCmStatusMacNumStartEae,
       "cadCmtsCmStatusMacNumStartDhcpv4": cadCmtsCmStatusMacNumStartDhcpv4,
       "cadCmtsCmStatusMacNumStartDhcpv6": cadCmtsCmStatusMacNumStartDhcpv6,
       "cadCmtsCmStatusMacNumDhcpv4Complete": cadCmtsCmStatusMacNumDhcpv4Complete,
       "cadCmtsCmStatusMacNumDhcpv6Complete": cadCmtsCmStatusMacNumDhcpv6Complete,
       "cadCmtsCmStatusMacNumStartCfgFileDownload": cadCmtsCmStatusMacNumStartCfgFileDownload,
       "cadCmtsCmStatusMacNumCfgFileDownloadComplete": cadCmtsCmStatusMacNumCfgFileDownloadComplete,
       "cadCmtsCmStatusMacNumStartRegistration": cadCmtsCmStatusMacNumStartRegistration,
       "cadCmtsCmStatusMacNumRegistrationComplete": cadCmtsCmStatusMacNumRegistrationComplete,
       "cadCmtsCmStatusMacNumOperational": cadCmtsCmStatusMacNumOperational,
       "cadCmtsCmStatusMacNumBpiInit": cadCmtsCmStatusMacNumBpiInit,
       "cadCmtsCmStatusMacNumForwardingDisabled": cadCmtsCmStatusMacNumForwardingDisabled,
       "cadCmtsCmStatusMacNumRfMuteAll": cadCmtsCmStatusMacNumRfMuteAll,
       "cadCmtsCmStatusMacNumTotal": cadCmtsCmStatusMacNumTotal,
       "cadCmtsCmStatusMacNumRangingAborted": cadCmtsCmStatusMacNumRangingAborted,
       "cadCmtsCmStatusMacNumRangFlaps": cadCmtsCmStatusMacNumRangFlaps,
       "cadCmtsCmStatusMacNumProvFlaps": cadCmtsCmStatusMacNumProvFlaps,
       "cadCmtsCmStatusMacNumRegFlaps": cadCmtsCmStatusMacNumRegFlaps,
       "cadCmtsCmStatusMacChSummaryTable": cadCmtsCmStatusMacChSummaryTable,
       "cadCmtsCmStatusMacChSummaryEntry": cadCmtsCmStatusMacChSummaryEntry,
       "cadCmtsCmStatusMacChNumOther": cadCmtsCmStatusMacChNumOther,
       "cadCmtsCmStatusMacChNumInitRanging": cadCmtsCmStatusMacChNumInitRanging,
       "cadCmtsCmStatusMacChNumRangingComplete": cadCmtsCmStatusMacChNumRangingComplete,
       "cadCmtsCmStatusMacChNumStartEae": cadCmtsCmStatusMacChNumStartEae,
       "cadCmtsCmStatusMacChNumStartDhcpv4": cadCmtsCmStatusMacChNumStartDhcpv4,
       "cadCmtsCmStatusMacChNumStartDhcpv6": cadCmtsCmStatusMacChNumStartDhcpv6,
       "cadCmtsCmStatusMacChNumDhcpv4Complete": cadCmtsCmStatusMacChNumDhcpv4Complete,
       "cadCmtsCmStatusMacChNumDhcpv6Complete": cadCmtsCmStatusMacChNumDhcpv6Complete,
       "cadCmtsCmStatusMacChNumStartCfgFileDownload": cadCmtsCmStatusMacChNumStartCfgFileDownload,
       "cadCmtsCmStatusMacChNumCfgFileDownloadComplete": cadCmtsCmStatusMacChNumCfgFileDownloadComplete,
       "cadCmtsCmStatusMacChNumStartRegistration": cadCmtsCmStatusMacChNumStartRegistration,
       "cadCmtsCmStatusMacChNumRegistrationComplete": cadCmtsCmStatusMacChNumRegistrationComplete,
       "cadCmtsCmStatusMacChNumOperational": cadCmtsCmStatusMacChNumOperational,
       "cadCmtsCmStatusMacChNumBpiInit": cadCmtsCmStatusMacChNumBpiInit,
       "cadCmtsCmStatusMacChNumForwardingDisabled": cadCmtsCmStatusMacChNumForwardingDisabled,
       "cadCmtsCmStatusMacChNumRfMuteAll": cadCmtsCmStatusMacChNumRfMuteAll,
       "cadCmtsCmStatusMacChNumTotal": cadCmtsCmStatusMacChNumTotal,
       "cadCmtsCmStatusMacChNumRangingAborted": cadCmtsCmStatusMacChNumRangingAborted,
       "cadCmtsCmStatusMacChNumRangFlaps": cadCmtsCmStatusMacChNumRangFlaps,
       "cadCmtsCmStatusMacChNumProvFlaps": cadCmtsCmStatusMacChNumProvFlaps,
       "cadCmtsCmStatusMacChNumRegFlaps": cadCmtsCmStatusMacChNumRegFlaps,
       "cadQosServiceFlowSidClusterTable": cadQosServiceFlowSidClusterTable,
       "cadQosServiceFlowSidClusterEntry": cadQosServiceFlowSidClusterEntry,
       "cadQosServiceFlowSidClusterChIfIndex": cadQosServiceFlowSidClusterChIfIndex,
       "cadQosServiceFlowSidClusterUcid": cadQosServiceFlowSidClusterUcid,
       "cadQosServiceFlowSidClusterSid": cadQosServiceFlowSidClusterSid,
       "cadQosServiceFlowSegHdr": cadQosServiceFlowSegHdr,
       "cadIfCmtsMacToInetIpTable": cadIfCmtsMacToInetIpTable,
       "cadIfCmtsMacToInetIpEntry": cadIfCmtsMacToInetIpEntry,
       "cadIfCmtsMacToInetIpAddrType": cadIfCmtsMacToInetIpAddrType,
       "cadIfCmtsMacToInetIpAddr": cadIfCmtsMacToInetIpAddr,
       "cadIfCmtsMacToInetIpCmMacAddr": cadIfCmtsMacToInetIpCmMacAddr,
       "cadEnforceRule": cadEnforceRule,
       "cadEnforceRuleTableLastChange": cadEnforceRuleTableLastChange,
       "cadEnforceRuleTable": cadEnforceRuleTable,
       "cadEnforceRuleEntry": cadEnforceRuleEntry,
       "cadEnforceRuleReferenceSCN": cadEnforceRuleReferenceSCN,
       "cadEnforceRuleEnforceSCN": cadEnforceRuleEnforceSCN,
       "cadEnforceRuleAvgBwRateUsageTrigger": cadEnforceRuleAvgBwRateUsageTrigger,
       "cadEnforceRuleAvgHistoryDuration": cadEnforceRuleAvgHistoryDuration,
       "cadEnforceRuleSamplingInterval": cadEnforceRuleSamplingInterval,
       "cadEnforceRulePenaltyDuration": cadEnforceRulePenaltyDuration,
       "cadEnforceRuleCreateTime": cadEnforceRuleCreateTime,
       "cadEnforceRuleStatus": cadEnforceRuleStatus,
       "cadEnforceRuleCountsTable": cadEnforceRuleCountsTable,
       "cadEnforceRuleCountsEntry": cadEnforceRuleCountsEntry,
       "cadEnforceRuleCountsPenalties": cadEnforceRuleCountsPenalties,
       "cadQosServiceClassControl": cadQosServiceClassControl,
       "cadQosServiceClassControlTable": cadQosServiceClassControlTable,
       "cadQosServiceClassControlEntry": cadQosServiceClassControlEntry,
       "cadQosServiceClassControlSendDsc": cadQosServiceClassControlSendDsc,
       "cadQosServiceClassControlSendDscLastUpdated": cadQosServiceClassControlSendDscLastUpdated,
       "cadQosServiceClassCmControlTable": cadQosServiceClassCmControlTable,
       "cadQosServiceClassCmControlEntry": cadQosServiceClassCmControlEntry,
       "cadQosServiceClassCmControlSendDscMacAddr": cadQosServiceClassCmControlSendDscMacAddr,
       "cadIfCmtsCmOfdmStatusTable": cadIfCmtsCmOfdmStatusTable,
       "cadIfCmtsCmOfdmStatusEntry": cadIfCmtsCmOfdmStatusEntry,
       "cadIfCmtsCmOfdmStatusMacAddress": cadIfCmtsCmOfdmStatusMacAddress,
       "cadIfCmtsCmOfdmStatusOkOfdmMod": cadIfCmtsCmOfdmStatusOkOfdmMod,
       "cadIfCmtsCmOfdmStatusOkOfdmaMod": cadIfCmtsCmOfdmStatusOkOfdmaMod,
       "cadIfCmtsCmOfdmStatusDsLowFreq": cadIfCmtsCmOfdmStatusDsLowFreq,
       "cadIfCmtsCmOfdmStatusDsHighFreq": cadIfCmtsCmOfdmStatusDsHighFreq,
       "cadIfCmtsCmOfdmStatusUsHighFreq": cadIfCmtsCmOfdmStatusUsHighFreq,
       "cadIfCmtsCmOfdmProfTable": cadIfCmtsCmOfdmProfTable,
       "cadIfCmtsCmOfdmProfEntry": cadIfCmtsCmOfdmProfEntry,
       "cadIfCmtsCmOfdmProfMacAddress": cadIfCmtsCmOfdmProfMacAddress,
       "cadIfCmtsCmOfdmProfIfIndex": cadIfCmtsCmOfdmProfIfIndex,
       "cadIfCmtsCmOfdmProfProfId": cadIfCmtsCmOfdmProfProfId,
       "cadIfCmtsCmOfdmProfDirection": cadIfCmtsCmOfdmProfDirection,
       "cadIfCmtsCmOfdmProfStatus": cadIfCmtsCmOfdmProfStatus,
       "cadSubmgtFilterGrpDescTable": cadSubmgtFilterGrpDescTable,
       "cadSubmgtFilterGrpDescEntry": cadSubmgtFilterGrpDescEntry,
       "cadSubmgtFilterGrpId": cadSubmgtFilterGrpId,
       "cadSubmgtFilterGrpDescription": cadSubmgtFilterGrpDescription,
       "cadSubmgtFilterGrpRowStatus": cadSubmgtFilterGrpRowStatus}
)
