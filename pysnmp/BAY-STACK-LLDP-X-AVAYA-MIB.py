# SNMP MIB module (BAY-STACK-LLDP-X-AVAYA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-LLDP-X-AVAYA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:10 2024
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackLldpXAvayaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39)
)
bayStackLldpXAvayaMib.setRevisions(
        ("2015-02-24 00:00",
         "2014-10-01 00:00",
         "2014-09-10 00:00",
         "2014-02-25 00:00",
         "2013-07-05 00:00",
         "2010-10-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsLldpXAvayaNotifications_ObjectIdentity = ObjectIdentity
bsLldpXAvayaNotifications = _BsLldpXAvayaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 0)
)
_BsLldpXAvayaObjects_ObjectIdentity = ObjectIdentity
bsLldpXAvayaObjects = _BsLldpXAvayaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1)
)
_BsLldpXAvayaConfig_ObjectIdentity = ObjectIdentity
bsLldpXAvayaConfig = _BsLldpXAvayaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 1)
)
_BsLldpXAvayaPortConfigTable_Object = MibTable
bsLldpXAvayaPortConfigTable = _BsLldpXAvayaPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaPortConfigTable.setStatus("current")
_BsLldpXAvayaPortConfigEntry_Object = MibTableRow
bsLldpXAvayaPortConfigEntry = _BsLldpXAvayaPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaPortConfigEntry.setStatus("current")


class _BsLldpXAvayaPortConfigTLVsTxEnable_Type(Bits):
    """Custom type bsLldpXAvayaPortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callServer", 1),
          ("faElementType", 4),
          ("faIsidVlanAsgns", 5),
          ("fileServer", 2),
          ("framingTlv", 3),
          ("poeConservationLevel", 0))
    )

_BsLldpXAvayaPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_BsLldpXAvayaPortConfigTLVsTxEnable_Object = MibTableColumn
bsLldpXAvayaPortConfigTLVsTxEnable = _BsLldpXAvayaPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 1, 1, 1, 1),
    _BsLldpXAvayaPortConfigTLVsTxEnable_Type()
)
bsLldpXAvayaPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLldpXAvayaPortConfigTLVsTxEnable.setStatus("current")
_BsLldpXAvayaLocalData_ObjectIdentity = ObjectIdentity
bsLldpXAvayaLocalData = _BsLldpXAvayaLocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2)
)
_BsLldpXAvayaLocPortTable_Object = MibTable
bsLldpXAvayaLocPortTable = _BsLldpXAvayaLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocPortTable.setStatus("current")
_BsLldpXAvayaLocPortEntry_Object = MibTableRow
bsLldpXAvayaLocPortEntry = _BsLldpXAvayaLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 1, 1)
)
bsLldpXAvayaLocPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocPortEntry.setStatus("current")


class _BsLldpXAvayaLocPortPoeConsLevelRequest_Type(Integer32):
    """Custom type bsLldpXAvayaLocPortPoeConsLevelRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsLldpXAvayaLocPortPoeConsLevelRequest_Type.__name__ = "Integer32"
_BsLldpXAvayaLocPortPoeConsLevelRequest_Object = MibTableColumn
bsLldpXAvayaLocPortPoeConsLevelRequest = _BsLldpXAvayaLocPortPoeConsLevelRequest_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 1, 1, 1),
    _BsLldpXAvayaLocPortPoeConsLevelRequest_Type()
)
bsLldpXAvayaLocPortPoeConsLevelRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocPortPoeConsLevelRequest.setStatus("current")


class _BsLldpXAvayaLocPortDot1QFramingRequest_Type(Integer32):
    """Custom type bsLldpXAvayaLocPortDot1QFramingRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("tagged", 1),
          ("untagged", 2))
    )


_BsLldpXAvayaLocPortDot1QFramingRequest_Type.__name__ = "Integer32"
_BsLldpXAvayaLocPortDot1QFramingRequest_Object = MibTableColumn
bsLldpXAvayaLocPortDot1QFramingRequest = _BsLldpXAvayaLocPortDot1QFramingRequest_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 1, 1, 2),
    _BsLldpXAvayaLocPortDot1QFramingRequest_Type()
)
bsLldpXAvayaLocPortDot1QFramingRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocPortDot1QFramingRequest.setStatus("current")
_BsLldpXAvayaLocCallServerTable_Object = MibTable
bsLldpXAvayaLocCallServerTable = _BsLldpXAvayaLocCallServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocCallServerTable.setStatus("current")
_BsLldpXAvayaLocCallServerEntry_Object = MibTableRow
bsLldpXAvayaLocCallServerEntry = _BsLldpXAvayaLocCallServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 2, 1)
)
bsLldpXAvayaLocCallServerEntry.setIndexNames(
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaLocCallServerNum"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocCallServerEntry.setStatus("current")


class _BsLldpXAvayaLocCallServerNum_Type(Integer32):
    """Custom type bsLldpXAvayaLocCallServerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BsLldpXAvayaLocCallServerNum_Type.__name__ = "Integer32"
_BsLldpXAvayaLocCallServerNum_Object = MibTableColumn
bsLldpXAvayaLocCallServerNum = _BsLldpXAvayaLocCallServerNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 2, 1, 1),
    _BsLldpXAvayaLocCallServerNum_Type()
)
bsLldpXAvayaLocCallServerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocCallServerNum.setStatus("current")
_BsLldpXAvayaLocCallServerAddressType_Type = InetAddressType
_BsLldpXAvayaLocCallServerAddressType_Object = MibTableColumn
bsLldpXAvayaLocCallServerAddressType = _BsLldpXAvayaLocCallServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 2, 1, 2),
    _BsLldpXAvayaLocCallServerAddressType_Type()
)
bsLldpXAvayaLocCallServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocCallServerAddressType.setStatus("current")
_BsLldpXAvayaLocCallServerAddress_Type = InetAddress
_BsLldpXAvayaLocCallServerAddress_Object = MibTableColumn
bsLldpXAvayaLocCallServerAddress = _BsLldpXAvayaLocCallServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 2, 1, 3),
    _BsLldpXAvayaLocCallServerAddress_Type()
)
bsLldpXAvayaLocCallServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocCallServerAddress.setStatus("current")
_BsLldpXAvayaLocFileServerTable_Object = MibTable
bsLldpXAvayaLocFileServerTable = _BsLldpXAvayaLocFileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 3)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFileServerTable.setStatus("current")
_BsLldpXAvayaLocFileServerEntry_Object = MibTableRow
bsLldpXAvayaLocFileServerEntry = _BsLldpXAvayaLocFileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 3, 1)
)
bsLldpXAvayaLocFileServerEntry.setIndexNames(
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaLocFileServerNum"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFileServerEntry.setStatus("current")


class _BsLldpXAvayaLocFileServerNum_Type(Integer32):
    """Custom type bsLldpXAvayaLocFileServerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BsLldpXAvayaLocFileServerNum_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFileServerNum_Object = MibTableColumn
bsLldpXAvayaLocFileServerNum = _BsLldpXAvayaLocFileServerNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 3, 1, 1),
    _BsLldpXAvayaLocFileServerNum_Type()
)
bsLldpXAvayaLocFileServerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFileServerNum.setStatus("current")
_BsLldpXAvayaLocFileServerAddressType_Type = InetAddressType
_BsLldpXAvayaLocFileServerAddressType_Object = MibTableColumn
bsLldpXAvayaLocFileServerAddressType = _BsLldpXAvayaLocFileServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 3, 1, 2),
    _BsLldpXAvayaLocFileServerAddressType_Type()
)
bsLldpXAvayaLocFileServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFileServerAddressType.setStatus("current")
_BsLldpXAvayaLocFileServerAddress_Type = InetAddress
_BsLldpXAvayaLocFileServerAddress_Object = MibTableColumn
bsLldpXAvayaLocFileServerAddress = _BsLldpXAvayaLocFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 3, 1, 3),
    _BsLldpXAvayaLocFileServerAddress_Type()
)
bsLldpXAvayaLocFileServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFileServerAddress.setStatus("current")


class _BsLldpXAvayaLocFaService_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BsLldpXAvayaLocFaService_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaService_Object = MibScalar
bsLldpXAvayaLocFaService = _BsLldpXAvayaLocFaService_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 4),
    _BsLldpXAvayaLocFaService_Type()
)
bsLldpXAvayaLocFaService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaService.setStatus("current")


class _BsLldpXAvayaLocFaElementType_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaElementType based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("faClientIpCamera", 11),
          ("faClientIpPhone", 10),
          ("faClientIpVideo", 12),
          ("faClientOnaSdn", 16),
          ("faClientOnaSpbOIp", 17),
          ("faClientRouter", 9),
          ("faClientSecurityDev", 13),
          ("faClientSrvrEndpt", 15),
          ("faClientSwitch", 8),
          ("faClientVirtSwitch", 14),
          ("faClientWapType1", 6),
          ("faClientWapType2", 7),
          ("faProxy", 3),
          ("faProxyNoAuth", 5),
          ("faServer", 2),
          ("faServerNoAuth", 4),
          ("other", 1))
    )


_BsLldpXAvayaLocFaElementType_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaElementType_Object = MibScalar
bsLldpXAvayaLocFaElementType = _BsLldpXAvayaLocFaElementType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 5),
    _BsLldpXAvayaLocFaElementType_Type()
)
bsLldpXAvayaLocFaElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaElementType.setStatus("current")


class _BsLldpXAvayaLocFaElementMgmtVlan_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaElementMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BsLldpXAvayaLocFaElementMgmtVlan_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaElementMgmtVlan_Object = MibScalar
bsLldpXAvayaLocFaElementMgmtVlan = _BsLldpXAvayaLocFaElementMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 6),
    _BsLldpXAvayaLocFaElementMgmtVlan_Type()
)
bsLldpXAvayaLocFaElementMgmtVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaElementMgmtVlan.setStatus("current")


class _BsLldpXAvayaLocFaElementPrimaryServerId_Type(OctetString):
    """Custom type bsLldpXAvayaLocFaElementPrimaryServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsLldpXAvayaLocFaElementPrimaryServerId_Type.__name__ = "OctetString"
_BsLldpXAvayaLocFaElementPrimaryServerId_Object = MibScalar
bsLldpXAvayaLocFaElementPrimaryServerId = _BsLldpXAvayaLocFaElementPrimaryServerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 7),
    _BsLldpXAvayaLocFaElementPrimaryServerId_Type()
)
bsLldpXAvayaLocFaElementPrimaryServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaElementPrimaryServerId.setStatus("current")
_BsLldpXAvayaLocFaIsidVlanAsgnsTable_Object = MibTable
bsLldpXAvayaLocFaIsidVlanAsgnsTable = _BsLldpXAvayaLocFaIsidVlanAsgnsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsTable.setStatus("current")
_BsLldpXAvayaLocFaIsidVlanAsgnsEntry_Object = MibTableRow
bsLldpXAvayaLocFaIsidVlanAsgnsEntry = _BsLldpXAvayaLocFaIsidVlanAsgnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8, 1)
)
bsLldpXAvayaLocFaIsidVlanAsgnsEntry.setIndexNames(
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex"),
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaLocFaIsidVlanAsgnsIsid"),
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaLocFaIsidVlanAsgnsVlan"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsEntry.setStatus("current")


class _BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Object = MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex = _BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8, 1, 1),
    _BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type()
)
bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex.setStatus("current")


class _BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaIsidVlanAsgnsIsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Object = MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsIsid = _BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8, 1, 2),
    _BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type()
)
bsLldpXAvayaLocFaIsidVlanAsgnsIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsIsid.setStatus("current")


class _BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaIsidVlanAsgnsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Object = MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsVlan = _BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8, 1, 3),
    _BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type()
)
bsLldpXAvayaLocFaIsidVlanAsgnsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsVlan.setStatus("current")


class _BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaIsidVlanAsgnsStatus based on Integer32"""
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
        *(("active", 3),
          ("other", 1),
          ("pending", 2),
          ("rejected", 4))
    )


_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Object = MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsStatus = _BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 8, 1, 4),
    _BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type()
)
bsLldpXAvayaLocFaIsidVlanAsgnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaIsidVlanAsgnsStatus.setStatus("current")


class _BsLldpXAvayaLocFaZeroTouchService_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaZeroTouchService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BsLldpXAvayaLocFaZeroTouchService_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaZeroTouchService_Object = MibScalar
bsLldpXAvayaLocFaZeroTouchService = _BsLldpXAvayaLocFaZeroTouchService_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 9),
    _BsLldpXAvayaLocFaZeroTouchService_Type()
)
bsLldpXAvayaLocFaZeroTouchService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaZeroTouchService.setStatus("current")


class _BsLldpXAvayaLocFaMsgAuthStatus_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaMsgAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BsLldpXAvayaLocFaMsgAuthStatus_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaMsgAuthStatus_Object = MibScalar
bsLldpXAvayaLocFaMsgAuthStatus = _BsLldpXAvayaLocFaMsgAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 10),
    _BsLldpXAvayaLocFaMsgAuthStatus_Type()
)
bsLldpXAvayaLocFaMsgAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaMsgAuthStatus.setStatus("current")


class _BsLldpXAvayaLocFaClientProxyService_Type(Integer32):
    """Custom type bsLldpXAvayaLocFaClientProxyService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BsLldpXAvayaLocFaClientProxyService_Type.__name__ = "Integer32"
_BsLldpXAvayaLocFaClientProxyService_Object = MibScalar
bsLldpXAvayaLocFaClientProxyService = _BsLldpXAvayaLocFaClientProxyService_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 2, 11),
    _BsLldpXAvayaLocFaClientProxyService_Type()
)
bsLldpXAvayaLocFaClientProxyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaLocFaClientProxyService.setStatus("current")
_BsLldpXAvayaRemoteData_ObjectIdentity = ObjectIdentity
bsLldpXAvayaRemoteData = _BsLldpXAvayaRemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3)
)
_BsLldpXAvayaRemTable_Object = MibTable
bsLldpXAvayaRemTable = _BsLldpXAvayaRemTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemTable.setStatus("current")
_BsLldpXAvayaRemEntry_Object = MibTableRow
bsLldpXAvayaRemEntry = _BsLldpXAvayaRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 1, 1)
)
bsLldpXAvayaRemEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemEntry.setStatus("current")


class _BsLldpXAvayaRemCurrentConsLevel_Type(Integer32):
    """Custom type bsLldpXAvayaRemCurrentConsLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 243),
    )


_BsLldpXAvayaRemCurrentConsLevel_Type.__name__ = "Integer32"
_BsLldpXAvayaRemCurrentConsLevel_Object = MibTableColumn
bsLldpXAvayaRemCurrentConsLevel = _BsLldpXAvayaRemCurrentConsLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 1, 1, 1),
    _BsLldpXAvayaRemCurrentConsLevel_Type()
)
bsLldpXAvayaRemCurrentConsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemCurrentConsLevel.setStatus("current")
_BsLldpXAvayaRemTypicalPower_Type = Integer32
_BsLldpXAvayaRemTypicalPower_Object = MibTableColumn
bsLldpXAvayaRemTypicalPower = _BsLldpXAvayaRemTypicalPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 1, 1, 2),
    _BsLldpXAvayaRemTypicalPower_Type()
)
bsLldpXAvayaRemTypicalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemTypicalPower.setStatus("current")
_BsLldpXAvayaRemMaxPower_Type = Integer32
_BsLldpXAvayaRemMaxPower_Object = MibTableColumn
bsLldpXAvayaRemMaxPower = _BsLldpXAvayaRemMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 1, 1, 3),
    _BsLldpXAvayaRemMaxPower_Type()
)
bsLldpXAvayaRemMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemMaxPower.setStatus("current")
_BsLldpXAvayaRemCallServerTable_Object = MibTable
bsLldpXAvayaRemCallServerTable = _BsLldpXAvayaRemCallServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemCallServerTable.setStatus("current")
_BsLldpXAvayaRemCallServerEntry_Object = MibTableRow
bsLldpXAvayaRemCallServerEntry = _BsLldpXAvayaRemCallServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 2, 1)
)
bsLldpXAvayaRemCallServerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemCallServerEntry.setStatus("current")
_BsLldpXAvayaRemPortCallServerAddressType_Type = InetAddressType
_BsLldpXAvayaRemPortCallServerAddressType_Object = MibTableColumn
bsLldpXAvayaRemPortCallServerAddressType = _BsLldpXAvayaRemPortCallServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 2, 1, 1),
    _BsLldpXAvayaRemPortCallServerAddressType_Type()
)
bsLldpXAvayaRemPortCallServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortCallServerAddressType.setStatus("current")
_BsLldpXAvayaRemPortCallServerAddress_Type = InetAddress
_BsLldpXAvayaRemPortCallServerAddress_Object = MibTableColumn
bsLldpXAvayaRemPortCallServerAddress = _BsLldpXAvayaRemPortCallServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 2, 1, 2),
    _BsLldpXAvayaRemPortCallServerAddress_Type()
)
bsLldpXAvayaRemPortCallServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortCallServerAddress.setStatus("current")
_BsLldpXAvayaRemFileServerTable_Object = MibTable
bsLldpXAvayaRemFileServerTable = _BsLldpXAvayaRemFileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 3)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFileServerTable.setStatus("current")
_BsLldpXAvayaRemFileServerEntry_Object = MibTableRow
bsLldpXAvayaRemFileServerEntry = _BsLldpXAvayaRemFileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 3, 1)
)
bsLldpXAvayaRemFileServerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFileServerEntry.setStatus("current")
_BsLldpXAvayaRemPortFileServerAddressType_Type = InetAddressType
_BsLldpXAvayaRemPortFileServerAddressType_Object = MibTableColumn
bsLldpXAvayaRemPortFileServerAddressType = _BsLldpXAvayaRemPortFileServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 3, 1, 1),
    _BsLldpXAvayaRemPortFileServerAddressType_Type()
)
bsLldpXAvayaRemPortFileServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortFileServerAddressType.setStatus("current")
_BsLldpXAvayaRemPortFileServerAddress_Type = InetAddress
_BsLldpXAvayaRemPortFileServerAddress_Object = MibTableColumn
bsLldpXAvayaRemPortFileServerAddress = _BsLldpXAvayaRemPortFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 3, 1, 2),
    _BsLldpXAvayaRemPortFileServerAddress_Type()
)
bsLldpXAvayaRemPortFileServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortFileServerAddress.setStatus("current")
_BsLldpXAvayaRemPoeConsLevelTable_Object = MibTable
bsLldpXAvayaRemPoeConsLevelTable = _BsLldpXAvayaRemPoeConsLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPoeConsLevelTable.setStatus("current")
_BsLldpXAvayaRemPoeConsLevelEntry_Object = MibTableRow
bsLldpXAvayaRemPoeConsLevelEntry = _BsLldpXAvayaRemPoeConsLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 4, 1)
)
bsLldpXAvayaRemPoeConsLevelEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaRemPoeConsLevelValue"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPoeConsLevelEntry.setStatus("current")


class _BsLldpXAvayaRemPoeConsLevelValue_Type(Integer32):
    """Custom type bsLldpXAvayaRemPoeConsLevelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_BsLldpXAvayaRemPoeConsLevelValue_Type.__name__ = "Integer32"
_BsLldpXAvayaRemPoeConsLevelValue_Object = MibTableColumn
bsLldpXAvayaRemPoeConsLevelValue = _BsLldpXAvayaRemPoeConsLevelValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 4, 1, 2),
    _BsLldpXAvayaRemPoeConsLevelValue_Type()
)
bsLldpXAvayaRemPoeConsLevelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPoeConsLevelValue.setStatus("current")
_BsLldpXAvayaRemDot1QTable_Object = MibTable
bsLldpXAvayaRemDot1QTable = _BsLldpXAvayaRemDot1QTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 5)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemDot1QTable.setStatus("current")
_BsLldpXAvayaRemDot1QEntry_Object = MibTableRow
bsLldpXAvayaRemDot1QEntry = _BsLldpXAvayaRemDot1QEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 5, 1)
)
bsLldpXAvayaRemDot1QEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemDot1QEntry.setStatus("current")


class _BsLldpXAvayaRemDot1QFraming_Type(Integer32):
    """Custom type bsLldpXAvayaRemDot1QFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("tagged", 1),
          ("untagged", 2))
    )


_BsLldpXAvayaRemDot1QFraming_Type.__name__ = "Integer32"
_BsLldpXAvayaRemDot1QFraming_Object = MibTableColumn
bsLldpXAvayaRemDot1QFraming = _BsLldpXAvayaRemDot1QFraming_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 5, 1, 1),
    _BsLldpXAvayaRemDot1QFraming_Type()
)
bsLldpXAvayaRemDot1QFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemDot1QFraming.setStatus("current")
_BsLldpXAvayaRemPhoneIpTable_Object = MibTable
bsLldpXAvayaRemPhoneIpTable = _BsLldpXAvayaRemPhoneIpTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPhoneIpTable.setStatus("current")
_BsLldpXAvayaRemPhoneIpEntry_Object = MibTableRow
bsLldpXAvayaRemPhoneIpEntry = _BsLldpXAvayaRemPhoneIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6, 1)
)
bsLldpXAvayaRemPhoneIpEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPhoneIpEntry.setStatus("current")
_BsLldpXAvayaRemPortPhoneAddressType_Type = InetAddressType
_BsLldpXAvayaRemPortPhoneAddressType_Object = MibTableColumn
bsLldpXAvayaRemPortPhoneAddressType = _BsLldpXAvayaRemPortPhoneAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6, 1, 1),
    _BsLldpXAvayaRemPortPhoneAddressType_Type()
)
bsLldpXAvayaRemPortPhoneAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortPhoneAddressType.setStatus("current")
_BsLldpXAvayaRemPortPhoneAddress_Type = InetAddress
_BsLldpXAvayaRemPortPhoneAddress_Object = MibTableColumn
bsLldpXAvayaRemPortPhoneAddress = _BsLldpXAvayaRemPortPhoneAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6, 1, 2),
    _BsLldpXAvayaRemPortPhoneAddress_Type()
)
bsLldpXAvayaRemPortPhoneAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortPhoneAddress.setStatus("current")
_BsLldpXAvayaRemPortPhoneAddressMask_Type = InetAddressPrefixLength
_BsLldpXAvayaRemPortPhoneAddressMask_Object = MibTableColumn
bsLldpXAvayaRemPortPhoneAddressMask = _BsLldpXAvayaRemPortPhoneAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6, 1, 3),
    _BsLldpXAvayaRemPortPhoneAddressMask_Type()
)
bsLldpXAvayaRemPortPhoneAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortPhoneAddressMask.setStatus("current")
_BsLldpXAvayaRemPortPhoneGatewayAddress_Type = InetAddress
_BsLldpXAvayaRemPortPhoneGatewayAddress_Object = MibTableColumn
bsLldpXAvayaRemPortPhoneGatewayAddress = _BsLldpXAvayaRemPortPhoneGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 6, 1, 4),
    _BsLldpXAvayaRemPortPhoneGatewayAddress_Type()
)
bsLldpXAvayaRemPortPhoneGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemPortPhoneGatewayAddress.setStatus("current")
_BsLldpXAvayaRemFaElementTable_Object = MibTable
bsLldpXAvayaRemFaElementTable = _BsLldpXAvayaRemFaElementTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementTable.setStatus("current")
_BsLldpXAvayaRemFaElementEntry_Object = MibTableRow
bsLldpXAvayaRemFaElementEntry = _BsLldpXAvayaRemFaElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7, 1)
)
bsLldpXAvayaRemFaElementEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementEntry.setStatus("current")


class _BsLldpXAvayaRemFaElementType_Type(Integer32):
    """Custom type bsLldpXAvayaRemFaElementType based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("faClientIpCamera", 11),
          ("faClientIpPhone", 10),
          ("faClientIpVideo", 12),
          ("faClientOnaSdn", 16),
          ("faClientOnaSpbOIp", 17),
          ("faClientRouter", 9),
          ("faClientSecurityDev", 13),
          ("faClientSrvrEndpt", 15),
          ("faClientSwitch", 8),
          ("faClientVirtSwitch", 14),
          ("faClientWapType1", 6),
          ("faClientWapType2", 7),
          ("faProxy", 3),
          ("faProxyNoAuth", 5),
          ("faServer", 2),
          ("faServerNoAuth", 4),
          ("other", 1))
    )


_BsLldpXAvayaRemFaElementType_Type.__name__ = "Integer32"
_BsLldpXAvayaRemFaElementType_Object = MibTableColumn
bsLldpXAvayaRemFaElementType = _BsLldpXAvayaRemFaElementType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7, 1, 1),
    _BsLldpXAvayaRemFaElementType_Type()
)
bsLldpXAvayaRemFaElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementType.setStatus("current")


class _BsLldpXAvayaRemFaElementMgmtVlan_Type(Integer32):
    """Custom type bsLldpXAvayaRemFaElementMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BsLldpXAvayaRemFaElementMgmtVlan_Type.__name__ = "Integer32"
_BsLldpXAvayaRemFaElementMgmtVlan_Object = MibTableColumn
bsLldpXAvayaRemFaElementMgmtVlan = _BsLldpXAvayaRemFaElementMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7, 1, 2),
    _BsLldpXAvayaRemFaElementMgmtVlan_Type()
)
bsLldpXAvayaRemFaElementMgmtVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementMgmtVlan.setStatus("current")


class _BsLldpXAvayaRemFaElementId_Type(OctetString):
    """Custom type bsLldpXAvayaRemFaElementId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsLldpXAvayaRemFaElementId_Type.__name__ = "OctetString"
_BsLldpXAvayaRemFaElementId_Object = MibTableColumn
bsLldpXAvayaRemFaElementId = _BsLldpXAvayaRemFaElementId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7, 1, 3),
    _BsLldpXAvayaRemFaElementId_Type()
)
bsLldpXAvayaRemFaElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementId.setStatus("current")


class _BsLldpXAvayaRemFaElementState_Type(Bits):
    """Custom type bsLldpXAvayaRemFaElementState based on Bits"""
    namedValues = NamedValues(
        *(("provisionModeDisabled", 2),
          ("provisionModeSpbm", 3),
          ("provisionModeVlan", 4),
          ("trafficTagged", 0),
          ("trafficTaggedAndUntagged", 1))
    )

_BsLldpXAvayaRemFaElementState_Type.__name__ = "Bits"
_BsLldpXAvayaRemFaElementState_Object = MibTableColumn
bsLldpXAvayaRemFaElementState = _BsLldpXAvayaRemFaElementState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 7, 1, 4),
    _BsLldpXAvayaRemFaElementState_Type()
)
bsLldpXAvayaRemFaElementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaElementState.setStatus("current")
_BsLldpXAvayaRemFaIsidVlanAsgnsTable_Object = MibTable
bsLldpXAvayaRemFaIsidVlanAsgnsTable = _BsLldpXAvayaRemFaIsidVlanAsgnsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 8)
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaIsidVlanAsgnsTable.setStatus("current")
_BsLldpXAvayaRemFaIsidVlanAsgnsEntry_Object = MibTableRow
bsLldpXAvayaRemFaIsidVlanAsgnsEntry = _BsLldpXAvayaRemFaIsidVlanAsgnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 8, 1)
)
bsLldpXAvayaRemFaIsidVlanAsgnsEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaRemFaIsidVlanAsgnsIsid"),
    (0, "BAY-STACK-LLDP-X-AVAYA-MIB", "bsLldpXAvayaRemFaIsidVlanAsgnsVlan"),
)
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaIsidVlanAsgnsEntry.setStatus("current")


class _BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type(Integer32):
    """Custom type bsLldpXAvayaRemFaIsidVlanAsgnsIsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type.__name__ = "Integer32"
_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Object = MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsIsid = _BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 8, 1, 1),
    _BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type()
)
bsLldpXAvayaRemFaIsidVlanAsgnsIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaIsidVlanAsgnsIsid.setStatus("current")


class _BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type(Integer32):
    """Custom type bsLldpXAvayaRemFaIsidVlanAsgnsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type.__name__ = "Integer32"
_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Object = MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsVlan = _BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 8, 1, 2),
    _BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type()
)
bsLldpXAvayaRemFaIsidVlanAsgnsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaIsidVlanAsgnsVlan.setStatus("current")


class _BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type(Integer32):
    """Custom type bsLldpXAvayaRemFaIsidVlanAsgnsStatus based on Integer32"""
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
        *(("active", 3),
          ("other", 1),
          ("pending", 2),
          ("rejected", 4))
    )


_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type.__name__ = "Integer32"
_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Object = MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsStatus = _BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 39, 1, 3, 8, 1, 3),
    _BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type()
)
bsLldpXAvayaRemFaIsidVlanAsgnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXAvayaRemFaIsidVlanAsgnsStatus.setStatus("current")
lldpPortConfigEntry.registerAugmentions(
    ("BAY-STACK-LLDP-X-AVAYA-MIB",
     "bsLldpXAvayaPortConfigEntry")
)
bsLldpXAvayaPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-LLDP-X-AVAYA-MIB",
    **{"bayStackLldpXAvayaMib": bayStackLldpXAvayaMib,
       "bsLldpXAvayaNotifications": bsLldpXAvayaNotifications,
       "bsLldpXAvayaObjects": bsLldpXAvayaObjects,
       "bsLldpXAvayaConfig": bsLldpXAvayaConfig,
       "bsLldpXAvayaPortConfigTable": bsLldpXAvayaPortConfigTable,
       "bsLldpXAvayaPortConfigEntry": bsLldpXAvayaPortConfigEntry,
       "bsLldpXAvayaPortConfigTLVsTxEnable": bsLldpXAvayaPortConfigTLVsTxEnable,
       "bsLldpXAvayaLocalData": bsLldpXAvayaLocalData,
       "bsLldpXAvayaLocPortTable": bsLldpXAvayaLocPortTable,
       "bsLldpXAvayaLocPortEntry": bsLldpXAvayaLocPortEntry,
       "bsLldpXAvayaLocPortPoeConsLevelRequest": bsLldpXAvayaLocPortPoeConsLevelRequest,
       "bsLldpXAvayaLocPortDot1QFramingRequest": bsLldpXAvayaLocPortDot1QFramingRequest,
       "bsLldpXAvayaLocCallServerTable": bsLldpXAvayaLocCallServerTable,
       "bsLldpXAvayaLocCallServerEntry": bsLldpXAvayaLocCallServerEntry,
       "bsLldpXAvayaLocCallServerNum": bsLldpXAvayaLocCallServerNum,
       "bsLldpXAvayaLocCallServerAddressType": bsLldpXAvayaLocCallServerAddressType,
       "bsLldpXAvayaLocCallServerAddress": bsLldpXAvayaLocCallServerAddress,
       "bsLldpXAvayaLocFileServerTable": bsLldpXAvayaLocFileServerTable,
       "bsLldpXAvayaLocFileServerEntry": bsLldpXAvayaLocFileServerEntry,
       "bsLldpXAvayaLocFileServerNum": bsLldpXAvayaLocFileServerNum,
       "bsLldpXAvayaLocFileServerAddressType": bsLldpXAvayaLocFileServerAddressType,
       "bsLldpXAvayaLocFileServerAddress": bsLldpXAvayaLocFileServerAddress,
       "bsLldpXAvayaLocFaService": bsLldpXAvayaLocFaService,
       "bsLldpXAvayaLocFaElementType": bsLldpXAvayaLocFaElementType,
       "bsLldpXAvayaLocFaElementMgmtVlan": bsLldpXAvayaLocFaElementMgmtVlan,
       "bsLldpXAvayaLocFaElementPrimaryServerId": bsLldpXAvayaLocFaElementPrimaryServerId,
       "bsLldpXAvayaLocFaIsidVlanAsgnsTable": bsLldpXAvayaLocFaIsidVlanAsgnsTable,
       "bsLldpXAvayaLocFaIsidVlanAsgnsEntry": bsLldpXAvayaLocFaIsidVlanAsgnsEntry,
       "bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex": bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex,
       "bsLldpXAvayaLocFaIsidVlanAsgnsIsid": bsLldpXAvayaLocFaIsidVlanAsgnsIsid,
       "bsLldpXAvayaLocFaIsidVlanAsgnsVlan": bsLldpXAvayaLocFaIsidVlanAsgnsVlan,
       "bsLldpXAvayaLocFaIsidVlanAsgnsStatus": bsLldpXAvayaLocFaIsidVlanAsgnsStatus,
       "bsLldpXAvayaLocFaZeroTouchService": bsLldpXAvayaLocFaZeroTouchService,
       "bsLldpXAvayaLocFaMsgAuthStatus": bsLldpXAvayaLocFaMsgAuthStatus,
       "bsLldpXAvayaLocFaClientProxyService": bsLldpXAvayaLocFaClientProxyService,
       "bsLldpXAvayaRemoteData": bsLldpXAvayaRemoteData,
       "bsLldpXAvayaRemTable": bsLldpXAvayaRemTable,
       "bsLldpXAvayaRemEntry": bsLldpXAvayaRemEntry,
       "bsLldpXAvayaRemCurrentConsLevel": bsLldpXAvayaRemCurrentConsLevel,
       "bsLldpXAvayaRemTypicalPower": bsLldpXAvayaRemTypicalPower,
       "bsLldpXAvayaRemMaxPower": bsLldpXAvayaRemMaxPower,
       "bsLldpXAvayaRemCallServerTable": bsLldpXAvayaRemCallServerTable,
       "bsLldpXAvayaRemCallServerEntry": bsLldpXAvayaRemCallServerEntry,
       "bsLldpXAvayaRemPortCallServerAddressType": bsLldpXAvayaRemPortCallServerAddressType,
       "bsLldpXAvayaRemPortCallServerAddress": bsLldpXAvayaRemPortCallServerAddress,
       "bsLldpXAvayaRemFileServerTable": bsLldpXAvayaRemFileServerTable,
       "bsLldpXAvayaRemFileServerEntry": bsLldpXAvayaRemFileServerEntry,
       "bsLldpXAvayaRemPortFileServerAddressType": bsLldpXAvayaRemPortFileServerAddressType,
       "bsLldpXAvayaRemPortFileServerAddress": bsLldpXAvayaRemPortFileServerAddress,
       "bsLldpXAvayaRemPoeConsLevelTable": bsLldpXAvayaRemPoeConsLevelTable,
       "bsLldpXAvayaRemPoeConsLevelEntry": bsLldpXAvayaRemPoeConsLevelEntry,
       "bsLldpXAvayaRemPoeConsLevelValue": bsLldpXAvayaRemPoeConsLevelValue,
       "bsLldpXAvayaRemDot1QTable": bsLldpXAvayaRemDot1QTable,
       "bsLldpXAvayaRemDot1QEntry": bsLldpXAvayaRemDot1QEntry,
       "bsLldpXAvayaRemDot1QFraming": bsLldpXAvayaRemDot1QFraming,
       "bsLldpXAvayaRemPhoneIpTable": bsLldpXAvayaRemPhoneIpTable,
       "bsLldpXAvayaRemPhoneIpEntry": bsLldpXAvayaRemPhoneIpEntry,
       "bsLldpXAvayaRemPortPhoneAddressType": bsLldpXAvayaRemPortPhoneAddressType,
       "bsLldpXAvayaRemPortPhoneAddress": bsLldpXAvayaRemPortPhoneAddress,
       "bsLldpXAvayaRemPortPhoneAddressMask": bsLldpXAvayaRemPortPhoneAddressMask,
       "bsLldpXAvayaRemPortPhoneGatewayAddress": bsLldpXAvayaRemPortPhoneGatewayAddress,
       "bsLldpXAvayaRemFaElementTable": bsLldpXAvayaRemFaElementTable,
       "bsLldpXAvayaRemFaElementEntry": bsLldpXAvayaRemFaElementEntry,
       "bsLldpXAvayaRemFaElementType": bsLldpXAvayaRemFaElementType,
       "bsLldpXAvayaRemFaElementMgmtVlan": bsLldpXAvayaRemFaElementMgmtVlan,
       "bsLldpXAvayaRemFaElementId": bsLldpXAvayaRemFaElementId,
       "bsLldpXAvayaRemFaElementState": bsLldpXAvayaRemFaElementState,
       "bsLldpXAvayaRemFaIsidVlanAsgnsTable": bsLldpXAvayaRemFaIsidVlanAsgnsTable,
       "bsLldpXAvayaRemFaIsidVlanAsgnsEntry": bsLldpXAvayaRemFaIsidVlanAsgnsEntry,
       "bsLldpXAvayaRemFaIsidVlanAsgnsIsid": bsLldpXAvayaRemFaIsidVlanAsgnsIsid,
       "bsLldpXAvayaRemFaIsidVlanAsgnsVlan": bsLldpXAvayaRemFaIsidVlanAsgnsVlan,
       "bsLldpXAvayaRemFaIsidVlanAsgnsStatus": bsLldpXAvayaRemFaIsidVlanAsgnsStatus}
)
