# SNMP MIB module (ZHONE-GEN-SUBSCRIBER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-SUBSCRIBER
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:25 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneSubscriber,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneSubscriber")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneSubscriberRecords = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1)
)
zhoneSubscriberRecords.setRevisions(
        ("2014-10-01 10:00",
         "2012-12-19 23:04",
         "2011-12-25 23:19",
         "2011-09-12 04:05",
         "2010-06-08 02:53",
         "2010-05-04 04:08",
         "2009-06-26 03:20",
         "2009-05-26 03:02",
         "2008-05-27 17:23",
         "2008-02-21 02:24",
         "2007-12-26 14:43",
         "2007-02-28 15:11",
         "2006-02-03 10:42",
         "2005-08-23 14:00",
         "2005-05-19 16:18",
         "2005-05-03 13:26",
         "2005-02-25 17:39",
         "2004-12-02 11:46",
         "2004-05-26 12:09",
         "2004-05-12 11:10",
         "2004-04-21 11:37",
         "2004-04-16 14:58",
         "2004-03-29 11:33",
         "2004-01-21 17:05",
         "2004-01-07 09:48",
         "2003-11-06 10:17",
         "2003-07-28 11:16",
         "2003-06-27 11:19",
         "2003-05-30 14:13",
         "2003-02-17 14:10",
         "2003-02-03 13:40",
         "2003-01-22 15:01",
         "2002-06-24 17:01",
         "2001-12-07 17:49",
         "2001-10-29 15:46",
         "2001-06-29 18:28",
         "2000-11-15 12:52",
         "2000-09-12 13:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneCodecType(Integer32, TextualConvention):
    status = "current"
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
        *(("g711a", 2),
          ("g711mu", 1),
          ("g723", 5),
          ("g726", 3),
          ("g729a", 4))
    )



class T38FaxType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t38None", 3),
          ("t38Rtp", 2),
          ("t38Udptl", 1))
    )



# MIB Managed Objects in the order of their OIDs



class _NextSubId_Type(Integer32):
    """Custom type nextSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NextSubId_Type.__name__ = "Integer32"
_NextSubId_Object = MibScalar
nextSubId = _NextSubId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 1),
    _NextSubId_Type()
)
nextSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextSubId.setStatus("current")


class _NextEndPointIndex_Type(Integer32):
    """Custom type nextEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NextEndPointIndex_Type.__name__ = "Integer32"
_NextEndPointIndex_Object = MibScalar
nextEndPointIndex = _NextEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 2),
    _NextEndPointIndex_Type()
)
nextEndPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextEndPointIndex.setStatus("current")
_SubInfoTable_Object = MibTable
subInfoTable = _SubInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    subInfoTable.setStatus("current")
_SubInfoEntry_Object = MibTableRow
subInfoEntry = _SubInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1)
)
subInfoEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subId"),
    (0, "ZHONE-GEN-SUBSCRIBER", "subLgId"),
)
if mibBuilder.loadTexts:
    subInfoEntry.setStatus("current")


class _SubId_Type(Integer32):
    """Custom type subId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubId_Type.__name__ = "Integer32"
_SubId_Object = MibTableColumn
subId = _SubId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 1),
    _SubId_Type()
)
subId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subId.setStatus("current")


class _SubLgId_Type(Integer32):
    """Custom type subLgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubLgId_Type.__name__ = "Integer32"
_SubLgId_Object = MibTableColumn
subLgId = _SubLgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 2),
    _SubLgId_Type()
)
subLgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subLgId.setStatus("current")
_SubName_Type = ZhoneAdminString
_SubName_Object = MibTableColumn
subName = _SubName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 3),
    _SubName_Type()
)
subName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subName.setStatus("current")
_SubProviderId_Type = Integer32
_SubProviderId_Object = MibTableColumn
subProviderId = _SubProviderId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 4),
    _SubProviderId_Type()
)
subProviderId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subProviderId.setStatus("current")


class _SubIadType_Type(Integer32):
    """Custom type subIadType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("matP", 6),
          ("other", 1),
          ("zedge100", 5),
          ("zedge64S", 3),
          ("zedge64T", 2),
          ("zedge65", 4),
          ("zedgeBH2A", 7),
          ("zedgeH2A", 8),
          ("zedgeH2AO", 9))
    )


_SubIadType_Type.__name__ = "Integer32"
_SubIadType_Object = MibTableColumn
subIadType = _SubIadType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 5),
    _SubIadType_Type()
)
subIadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subIadType.setStatus("current")


class _SubMaxAllowedLineRate_Type(Integer32):
    """Custom type subMaxAllowedLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubMaxAllowedLineRate_Type.__name__ = "Integer32"
_SubMaxAllowedLineRate_Object = MibTableColumn
subMaxAllowedLineRate = _SubMaxAllowedLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 6),
    _SubMaxAllowedLineRate_Type()
)
subMaxAllowedLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subMaxAllowedLineRate.setStatus("current")
if mibBuilder.loadTexts:
    subMaxAllowedLineRate.setUnits("Kbits per second")


class _SubMaxCapableLineRate_Type(Integer32):
    """Custom type subMaxCapableLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubMaxCapableLineRate_Type.__name__ = "Integer32"
_SubMaxCapableLineRate_Object = MibTableColumn
subMaxCapableLineRate = _SubMaxCapableLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 7),
    _SubMaxCapableLineRate_Type()
)
subMaxCapableLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subMaxCapableLineRate.setStatus("current")
if mibBuilder.loadTexts:
    subMaxCapableLineRate.setUnits("Kbits per second")


class _SubNextVoiceConnectionIndex_Type(Integer32):
    """Custom type subNextVoiceConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubNextVoiceConnectionIndex_Type.__name__ = "Integer32"
_SubNextVoiceConnectionIndex_Object = MibTableColumn
subNextVoiceConnectionIndex = _SubNextVoiceConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 8),
    _SubNextVoiceConnectionIndex_Type()
)
subNextVoiceConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subNextVoiceConnectionIndex.setStatus("current")
_SubRowStatus_Type = ZhoneRowStatus
_SubRowStatus_Object = MibTableColumn
subRowStatus = _SubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 3, 1, 9),
    _SubRowStatus_Type()
)
subRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subRowStatus.setStatus("current")
_SubDataConnectionTable_Object = MibTable
subDataConnectionTable = _SubDataConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    subDataConnectionTable.setStatus("current")
_SubDataConnectionEntry_Object = MibTableRow
subDataConnectionEntry = _SubDataConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1)
)
subDataConnectionEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subId"),
    (0, "ZHONE-GEN-SUBSCRIBER", "subLgId"),
    (0, "ZHONE-GEN-SUBSCRIBER", "subDataIfIndex"),
)
if mibBuilder.loadTexts:
    subDataConnectionEntry.setStatus("current")
_SubDataIfIndex_Type = InterfaceIndex
_SubDataIfIndex_Object = MibTableColumn
subDataIfIndex = _SubDataIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 1),
    _SubDataIfIndex_Type()
)
subDataIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subDataIfIndex.setStatus("current")


class _SubDataIpIfOperStatus_Type(Integer32):
    """Custom type subDataIpIfOperStatus based on Integer32"""
    defaultValue = 4

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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_SubDataIpIfOperStatus_Type.__name__ = "Integer32"
_SubDataIpIfOperStatus_Object = MibTableColumn
subDataIpIfOperStatus = _SubDataIpIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 2),
    _SubDataIpIfOperStatus_Type()
)
subDataIpIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDataIpIfOperStatus.setStatus("current")
_SubDataUserLogOnId_Type = ZhoneAdminString
_SubDataUserLogOnId_Object = MibTableColumn
subDataUserLogOnId = _SubDataUserLogOnId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 3),
    _SubDataUserLogOnId_Type()
)
subDataUserLogOnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subDataUserLogOnId.setStatus("current")
_SubDataUserPassword_Type = ZhoneAdminString
_SubDataUserPassword_Object = MibTableColumn
subDataUserPassword = _SubDataUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 4),
    _SubDataUserPassword_Type()
)
subDataUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subDataUserPassword.setStatus("current")


class _SubDataMaxAddrAllowed_Type(Integer32):
    """Custom type subDataMaxAddrAllowed based on Integer32"""
    defaultValue = 1


_SubDataMaxAddrAllowed_Object = MibTableColumn
subDataMaxAddrAllowed = _SubDataMaxAddrAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 5),
    _SubDataMaxAddrAllowed_Type()
)
subDataMaxAddrAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subDataMaxAddrAllowed.setStatus("current")
_SubDataIpAddrInUse_Type = Integer32
_SubDataIpAddrInUse_Object = MibTableColumn
subDataIpAddrInUse = _SubDataIpAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 6),
    _SubDataIpAddrInUse_Type()
)
subDataIpAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDataIpAddrInUse.setStatus("current")
_SubDataCurrentIpAddr_Type = IpAddress
_SubDataCurrentIpAddr_Object = MibTableColumn
subDataCurrentIpAddr = _SubDataCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 7),
    _SubDataCurrentIpAddr_Type()
)
subDataCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDataCurrentIpAddr.setStatus("current")


class _SubDataStatsStatus_Type(Integer32):
    """Custom type subDataStatsStatus based on Integer32"""
    defaultValue = 2

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


_SubDataStatsStatus_Type.__name__ = "Integer32"
_SubDataStatsStatus_Object = MibTableColumn
subDataStatsStatus = _SubDataStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 8),
    _SubDataStatsStatus_Type()
)
subDataStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDataStatsStatus.setStatus("current")
_SubDataRowStatus_Type = ZhoneRowStatus
_SubDataRowStatus_Object = MibTableColumn
subDataRowStatus = _SubDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 4, 1, 9),
    _SubDataRowStatus_Type()
)
subDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subDataRowStatus.setStatus("current")
_SubVoiceConnectionTable_Object = MibTable
subVoiceConnectionTable = _SubVoiceConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    subVoiceConnectionTable.setStatus("current")
_SubVoiceConnectionEntry_Object = MibTableRow
subVoiceConnectionEntry = _SubVoiceConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1)
)
subVoiceConnectionEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subId"),
    (0, "ZHONE-GEN-SUBSCRIBER", "subLgId"),
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceConnectionIndex"),
)
if mibBuilder.loadTexts:
    subVoiceConnectionEntry.setStatus("current")


class _SubVoiceConnectionIndex_Type(Integer32):
    """Custom type subVoiceConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceConnectionIndex_Type.__name__ = "Integer32"
_SubVoiceConnectionIndex_Object = MibTableColumn
subVoiceConnectionIndex = _SubVoiceConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 1),
    _SubVoiceConnectionIndex_Type()
)
subVoiceConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceConnectionIndex.setStatus("current")


class _SubVoiceConnectionType_Type(Integer32):
    """Custom type subVoiceConnectionType based on Integer32"""
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
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("aal2ToGr303", 1),
          ("aal2ToV52", 2),
          ("ebsToGr303", 13),
          ("elcpAal2ToV52", 11),
          ("isdnToAal2", 5),
          ("isdnToV52", 12),
          ("isdnToVoip", 20),
          ("isdnsigToVoip", 15),
          ("potsToAal2", 4),
          ("potsToDs1", 16),
          ("potsToGr303", 6),
          ("potsToV52", 7),
          ("sipToGr303", 9),
          ("voipToDs1", 8),
          ("voipToEbs", 19),
          ("voipToGr303", 3),
          ("voipToPots", 14),
          ("voipToTr008", 18),
          ("voipToV52", 10))
    )


_SubVoiceConnectionType_Type.__name__ = "Integer32"
_SubVoiceConnectionType_Object = MibTableColumn
subVoiceConnectionType = _SubVoiceConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 2),
    _SubVoiceConnectionType_Type()
)
subVoiceConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceConnectionType.setStatus("current")


class _SubVoiceEndPoint1AddressIndex_Type(Integer32):
    """Custom type subVoiceEndPoint1AddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceEndPoint1AddressIndex_Type.__name__ = "Integer32"
_SubVoiceEndPoint1AddressIndex_Object = MibTableColumn
subVoiceEndPoint1AddressIndex = _SubVoiceEndPoint1AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 3),
    _SubVoiceEndPoint1AddressIndex_Type()
)
subVoiceEndPoint1AddressIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceEndPoint1AddressIndex.setStatus("current")


class _SubVoiceEndPoint2AddressIndex_Type(Integer32):
    """Custom type subVoiceEndPoint2AddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceEndPoint2AddressIndex_Type.__name__ = "Integer32"
_SubVoiceEndPoint2AddressIndex_Object = MibTableColumn
subVoiceEndPoint2AddressIndex = _SubVoiceEndPoint2AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 4),
    _SubVoiceEndPoint2AddressIndex_Type()
)
subVoiceEndPoint2AddressIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceEndPoint2AddressIndex.setStatus("current")
_SubVoiceConnectionDescription_Type = ZhoneAdminString
_SubVoiceConnectionDescription_Object = MibTableColumn
subVoiceConnectionDescription = _SubVoiceConnectionDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 5),
    _SubVoiceConnectionDescription_Type()
)
subVoiceConnectionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceConnectionDescription.setStatus("current")


class _SubVoiceAdminStatus_Type(Integer32):
    """Custom type subVoiceAdminStatus based on Integer32"""
    defaultValue = 2

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


_SubVoiceAdminStatus_Type.__name__ = "Integer32"
_SubVoiceAdminStatus_Object = MibTableColumn
subVoiceAdminStatus = _SubVoiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 6),
    _SubVoiceAdminStatus_Type()
)
subVoiceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceAdminStatus.setStatus("current")
_SubVoiceRowStatus_Type = ZhoneRowStatus
_SubVoiceRowStatus_Object = MibTableColumn
subVoiceRowStatus = _SubVoiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 7),
    _SubVoiceRowStatus_Type()
)
subVoiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subVoiceRowStatus.setStatus("current")
_SubVoiceHuntGroup_Type = TruthValue
_SubVoiceHuntGroup_Object = MibTableColumn
subVoiceHuntGroup = _SubVoiceHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 8),
    _SubVoiceHuntGroup_Type()
)
subVoiceHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceHuntGroup.setStatus("current")


class _SubVoiceFeatureSetOne_Type(Bits):
    """Custom type subVoiceFeatureSetOne based on Bits"""
    defaultBinValue = "11001"

    namedValues = NamedValues(
        *(("alwaysoffhook", 2),
          ("calltransfer", 5),
          ("callwait", 4),
          ("centrex", 16),
          ("cod", 14),
          ("conference", 6),
          ("dataonly", 15),
          ("dtmf-inband", 13),
          ("dtmf-rfc2833", 12),
          ("hookflash", 0),
          ("hotline", 9),
          ("lss-rb", 7),
          ("lss-tone", 11),
          ("onhooksignaling", 1),
          ("plar", 3),
          ("voiceonly", 8),
          ("warmline", 10))
    )

_SubVoiceFeatureSetOne_Type.__name__ = "Bits"
_SubVoiceFeatureSetOne_Object = MibTableColumn
subVoiceFeatureSetOne = _SubVoiceFeatureSetOne_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 5, 1, 9),
    _SubVoiceFeatureSetOne_Type()
)
subVoiceFeatureSetOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceFeatureSetOne.setStatus("current")
_SubVoiceAal2Table_Object = MibTable
subVoiceAal2Table = _SubVoiceAal2Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    subVoiceAal2Table.setStatus("current")
_SubVoiceAal2Entry_Object = MibTableRow
subVoiceAal2Entry = _SubVoiceAal2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1)
)
subVoiceAal2Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceAal2EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceAal2Entry.setStatus("current")


class _SubVoiceAal2EndPointIndex_Type(Integer32):
    """Custom type subVoiceAal2EndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceAal2EndPointIndex_Type.__name__ = "Integer32"
_SubVoiceAal2EndPointIndex_Object = MibTableColumn
subVoiceAal2EndPointIndex = _SubVoiceAal2EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1, 1),
    _SubVoiceAal2EndPointIndex_Type()
)
subVoiceAal2EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceAal2EndPointIndex.setStatus("current")
_SubVoiceAal2LineGroupId_Type = Integer32
_SubVoiceAal2LineGroupId_Object = MibTableColumn
subVoiceAal2LineGroupId = _SubVoiceAal2LineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1, 2),
    _SubVoiceAal2LineGroupId_Type()
)
subVoiceAal2LineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceAal2LineGroupId.setStatus("current")
_SubVoiceAal2Vpi_Type = AtmVpIdentifier
_SubVoiceAal2Vpi_Object = MibTableColumn
subVoiceAal2Vpi = _SubVoiceAal2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1, 3),
    _SubVoiceAal2Vpi_Type()
)
subVoiceAal2Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceAal2Vpi.setStatus("current")
_SubVoiceAal2Vci_Type = AtmVcIdentifier
_SubVoiceAal2Vci_Object = MibTableColumn
subVoiceAal2Vci = _SubVoiceAal2Vci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1, 4),
    _SubVoiceAal2Vci_Type()
)
subVoiceAal2Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceAal2Vci.setStatus("current")


class _SubVoiceAal2Cid_Type(Integer32):
    """Custom type subVoiceAal2Cid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SubVoiceAal2Cid_Type.__name__ = "Integer32"
_SubVoiceAal2Cid_Object = MibTableColumn
subVoiceAal2Cid = _SubVoiceAal2Cid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 6, 1, 5),
    _SubVoiceAal2Cid_Type()
)
subVoiceAal2Cid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceAal2Cid.setStatus("current")
_SubVoiceGr303Table_Object = MibTable
subVoiceGr303Table = _SubVoiceGr303Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    subVoiceGr303Table.setStatus("current")
_SubVoiceGr303Entry_Object = MibTableRow
subVoiceGr303Entry = _SubVoiceGr303Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 7, 1)
)
subVoiceGr303Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceGr303EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceGr303Entry.setStatus("current")


class _SubVoiceGr303EndPointIndex_Type(Integer32):
    """Custom type subVoiceGr303EndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceGr303EndPointIndex_Type.__name__ = "Integer32"
_SubVoiceGr303EndPointIndex_Object = MibTableColumn
subVoiceGr303EndPointIndex = _SubVoiceGr303EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 7, 1, 1),
    _SubVoiceGr303EndPointIndex_Type()
)
subVoiceGr303EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceGr303EndPointIndex.setStatus("current")
_SubVoiceGr303IgName_Type = ZhoneAdminString
_SubVoiceGr303IgName_Object = MibTableColumn
subVoiceGr303IgName = _SubVoiceGr303IgName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 7, 1, 2),
    _SubVoiceGr303IgName_Type()
)
subVoiceGr303IgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceGr303IgName.setStatus("current")


class _SubVoiceGr303IgCrv_Type(Integer32):
    """Custom type subVoiceGr303IgCrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_SubVoiceGr303IgCrv_Type.__name__ = "Integer32"
_SubVoiceGr303IgCrv_Object = MibTableColumn
subVoiceGr303IgCrv = _SubVoiceGr303IgCrv_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 7, 1, 3),
    _SubVoiceGr303IgCrv_Type()
)
subVoiceGr303IgCrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceGr303IgCrv.setStatus("current")
_SubVoiceV52Table_Object = MibTable
subVoiceV52Table = _SubVoiceV52Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8)
)
if mibBuilder.loadTexts:
    subVoiceV52Table.setStatus("current")
_SubVoiceV52Entry_Object = MibTableRow
subVoiceV52Entry = _SubVoiceV52Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1)
)
subVoiceV52Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceV52EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceV52Entry.setStatus("current")


class _SubVoiceV52EndPointIndex_Type(Integer32):
    """Custom type subVoiceV52EndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceV52EndPointIndex_Type.__name__ = "Integer32"
_SubVoiceV52EndPointIndex_Object = MibTableColumn
subVoiceV52EndPointIndex = _SubVoiceV52EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1, 1),
    _SubVoiceV52EndPointIndex_Type()
)
subVoiceV52EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceV52EndPointIndex.setStatus("current")
_SubVoiceV52InterfaceName_Type = ZhoneAdminString
_SubVoiceV52InterfaceName_Object = MibTableColumn
subVoiceV52InterfaceName = _SubVoiceV52InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1, 2),
    _SubVoiceV52InterfaceName_Type()
)
subVoiceV52InterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceV52InterfaceName.setStatus("current")


class _SubVoiceV52UserPortId_Type(Integer32):
    """Custom type subVoiceV52UserPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubVoiceV52UserPortId_Type.__name__ = "Integer32"
_SubVoiceV52UserPortId_Object = MibTableColumn
subVoiceV52UserPortId = _SubVoiceV52UserPortId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1, 3),
    _SubVoiceV52UserPortId_Type()
)
subVoiceV52UserPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceV52UserPortId.setStatus("current")


class _SubVoiceV52UserType_Type(Integer32):
    """Custom type subVoiceV52UserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdnBChannel", 3),
          ("isdnDChannel", 2),
          ("pots", 1))
    )


_SubVoiceV52UserType_Type.__name__ = "Integer32"
_SubVoiceV52UserType_Object = MibTableColumn
subVoiceV52UserType = _SubVoiceV52UserType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1, 4),
    _SubVoiceV52UserType_Type()
)
subVoiceV52UserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceV52UserType.setStatus("current")


class _SubVoiceV52IsdnChannelId_Type(Integer32):
    """Custom type subVoiceV52IsdnChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SubVoiceV52IsdnChannelId_Type.__name__ = "Integer32"
_SubVoiceV52IsdnChannelId_Object = MibTableColumn
subVoiceV52IsdnChannelId = _SubVoiceV52IsdnChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 8, 1, 5),
    _SubVoiceV52IsdnChannelId_Type()
)
subVoiceV52IsdnChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceV52IsdnChannelId.setStatus("current")
_SubVoicePotsTable_Object = MibTable
subVoicePotsTable = _SubVoicePotsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9)
)
if mibBuilder.loadTexts:
    subVoicePotsTable.setStatus("current")
_SubVoicePotsEntry_Object = MibTableRow
subVoicePotsEntry = _SubVoicePotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1)
)
subVoicePotsEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoicePotsEndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoicePotsEntry.setStatus("current")


class _SubVoicePotsEndPointIndex_Type(Integer32):
    """Custom type subVoicePotsEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoicePotsEndPointIndex_Type.__name__ = "Integer32"
_SubVoicePotsEndPointIndex_Object = MibTableColumn
subVoicePotsEndPointIndex = _SubVoicePotsEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1, 1),
    _SubVoicePotsEndPointIndex_Type()
)
subVoicePotsEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoicePotsEndPointIndex.setStatus("current")
_SubVoicePotsLineGroupId_Type = Integer32
_SubVoicePotsLineGroupId_Object = MibTableColumn
subVoicePotsLineGroupId = _SubVoicePotsLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1, 2),
    _SubVoicePotsLineGroupId_Type()
)
subVoicePotsLineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoicePotsLineGroupId.setStatus("current")
_SubVoicePotsHuntGrpEndPointIndex1_Type = Integer32
_SubVoicePotsHuntGrpEndPointIndex1_Object = MibTableColumn
subVoicePotsHuntGrpEndPointIndex1 = _SubVoicePotsHuntGrpEndPointIndex1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1, 3),
    _SubVoicePotsHuntGrpEndPointIndex1_Type()
)
subVoicePotsHuntGrpEndPointIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoicePotsHuntGrpEndPointIndex1.setStatus("current")
_SubVoicePotsHuntGrpEndPointIndex2_Type = Integer32
_SubVoicePotsHuntGrpEndPointIndex2_Object = MibTableColumn
subVoicePotsHuntGrpEndPointIndex2 = _SubVoicePotsHuntGrpEndPointIndex2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1, 4),
    _SubVoicePotsHuntGrpEndPointIndex2_Type()
)
subVoicePotsHuntGrpEndPointIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoicePotsHuntGrpEndPointIndex2.setStatus("current")
_SubVoicePotsHuntGrpEndPointIndex3_Type = Integer32
_SubVoicePotsHuntGrpEndPointIndex3_Object = MibTableColumn
subVoicePotsHuntGrpEndPointIndex3 = _SubVoicePotsHuntGrpEndPointIndex3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 9, 1, 5),
    _SubVoicePotsHuntGrpEndPointIndex3_Type()
)
subVoicePotsHuntGrpEndPointIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoicePotsHuntGrpEndPointIndex3.setStatus("current")
_SubVoiceIsdnTable_Object = MibTable
subVoiceIsdnTable = _SubVoiceIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10)
)
if mibBuilder.loadTexts:
    subVoiceIsdnTable.setStatus("current")
_SubVoiceIsdnEntry_Object = MibTableRow
subVoiceIsdnEntry = _SubVoiceIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10, 1)
)
subVoiceIsdnEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnEndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceIsdnEntry.setStatus("current")


class _SubVoiceIsdnEndPointIndex_Type(Integer32):
    """Custom type subVoiceIsdnEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceIsdnEndPointIndex_Type.__name__ = "Integer32"
_SubVoiceIsdnEndPointIndex_Object = MibTableColumn
subVoiceIsdnEndPointIndex = _SubVoiceIsdnEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10, 1, 1),
    _SubVoiceIsdnEndPointIndex_Type()
)
subVoiceIsdnEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceIsdnEndPointIndex.setStatus("current")
_SubVoiceIsdnLineGroupId_Type = Integer32
_SubVoiceIsdnLineGroupId_Object = MibTableColumn
subVoiceIsdnLineGroupId = _SubVoiceIsdnLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10, 1, 2),
    _SubVoiceIsdnLineGroupId_Type()
)
subVoiceIsdnLineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnLineGroupId.setStatus("current")


class _SubVoiceIsdnType_Type(Integer32):
    """Custom type subVoiceIsdnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isdnBChannel", 2),
          ("isdnDChannel", 1))
    )


_SubVoiceIsdnType_Type.__name__ = "Integer32"
_SubVoiceIsdnType_Object = MibTableColumn
subVoiceIsdnType = _SubVoiceIsdnType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10, 1, 3),
    _SubVoiceIsdnType_Type()
)
subVoiceIsdnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnType.setStatus("current")


class _SubVoiceIsdnChannelId_Type(Integer32):
    """Custom type subVoiceIsdnChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubVoiceIsdnChannelId_Type.__name__ = "Integer32"
_SubVoiceIsdnChannelId_Object = MibTableColumn
subVoiceIsdnChannelId = _SubVoiceIsdnChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 10, 1, 4),
    _SubVoiceIsdnChannelId_Type()
)
subVoiceIsdnChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnChannelId.setStatus("current")
_SubVoiceDs1Table_Object = MibTable
subVoiceDs1Table = _SubVoiceDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12)
)
if mibBuilder.loadTexts:
    subVoiceDs1Table.setStatus("current")
_SubVoiceDs1Entry_Object = MibTableRow
subVoiceDs1Entry = _SubVoiceDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1)
)
subVoiceDs1Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceDs1EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceDs1Entry.setStatus("current")


class _SubVoiceDs1EndPointIndex_Type(Integer32):
    """Custom type subVoiceDs1EndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceDs1EndPointIndex_Type.__name__ = "Integer32"
_SubVoiceDs1EndPointIndex_Object = MibTableColumn
subVoiceDs1EndPointIndex = _SubVoiceDs1EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 1),
    _SubVoiceDs1EndPointIndex_Type()
)
subVoiceDs1EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceDs1EndPointIndex.setStatus("current")


class _SubVoiceDs1Ds0ChannelID_Type(Integer32):
    """Custom type subVoiceDs1Ds0ChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubVoiceDs1Ds0ChannelID_Type.__name__ = "Integer32"
_SubVoiceDs1Ds0ChannelID_Object = MibTableColumn
subVoiceDs1Ds0ChannelID = _SubVoiceDs1Ds0ChannelID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 2),
    _SubVoiceDs1Ds0ChannelID_Type()
)
subVoiceDs1Ds0ChannelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceDs1Ds0ChannelID.setStatus("current")
_SubVoiceDs1LineGroupId_Type = InterfaceIndex
_SubVoiceDs1LineGroupId_Object = MibTableColumn
subVoiceDs1LineGroupId = _SubVoiceDs1LineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 3),
    _SubVoiceDs1LineGroupId_Type()
)
subVoiceDs1LineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceDs1LineGroupId.setStatus("current")
_SubVoiceDs1HuntGrpEndPointIndex1_Type = Integer32
_SubVoiceDs1HuntGrpEndPointIndex1_Object = MibTableColumn
subVoiceDs1HuntGrpEndPointIndex1 = _SubVoiceDs1HuntGrpEndPointIndex1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 4),
    _SubVoiceDs1HuntGrpEndPointIndex1_Type()
)
subVoiceDs1HuntGrpEndPointIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceDs1HuntGrpEndPointIndex1.setStatus("current")
_SubVoiceDs1HuntGrpEndPointIndex2_Type = Integer32
_SubVoiceDs1HuntGrpEndPointIndex2_Object = MibTableColumn
subVoiceDs1HuntGrpEndPointIndex2 = _SubVoiceDs1HuntGrpEndPointIndex2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 5),
    _SubVoiceDs1HuntGrpEndPointIndex2_Type()
)
subVoiceDs1HuntGrpEndPointIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceDs1HuntGrpEndPointIndex2.setStatus("current")
_SubVoiceDs1HuntGrpEndPointIndex3_Type = Integer32
_SubVoiceDs1HuntGrpEndPointIndex3_Object = MibTableColumn
subVoiceDs1HuntGrpEndPointIndex3 = _SubVoiceDs1HuntGrpEndPointIndex3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 12, 1, 6),
    _SubVoiceDs1HuntGrpEndPointIndex3_Type()
)
subVoiceDs1HuntGrpEndPointIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceDs1HuntGrpEndPointIndex3.setStatus("current")
_SubVoiceVoipTable_Object = MibTable
subVoiceVoipTable = _SubVoiceVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13)
)
if mibBuilder.loadTexts:
    subVoiceVoipTable.setStatus("current")
_SubVoiceVoipEntry_Object = MibTableRow
subVoiceVoipEntry = _SubVoiceVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1)
)
subVoiceVoipEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceVoipEndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceVoipEntry.setStatus("current")


class _SubVoiceVoipEndPointIndex_Type(Integer32):
    """Custom type subVoiceVoipEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceVoipEndPointIndex_Type.__name__ = "Integer32"
_SubVoiceVoipEndPointIndex_Object = MibTableColumn
subVoiceVoipEndPointIndex = _SubVoiceVoipEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 1),
    _SubVoiceVoipEndPointIndex_Type()
)
subVoiceVoipEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceVoipEndPointIndex.setStatus("current")
_SubVoiceVoipUserName_Type = SnmpAdminString
_SubVoiceVoipUserName_Object = MibTableColumn
subVoiceVoipUserName = _SubVoiceVoipUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 2),
    _SubVoiceVoipUserName_Type()
)
subVoiceVoipUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipUserName.setStatus("current")
_SubVoiceVoipDirectoryNumber_Type = ZhoneAdminString
_SubVoiceVoipDirectoryNumber_Object = MibTableColumn
subVoiceVoipDirectoryNumber = _SubVoiceVoipDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 3),
    _SubVoiceVoipDirectoryNumber_Type()
)
subVoiceVoipDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipDirectoryNumber.setStatus("current")
_SubVoiceVoipIpInterface_Type = InterfaceIndexOrZero
_SubVoiceVoipIpInterface_Object = MibTableColumn
subVoiceVoipIpInterface = _SubVoiceVoipIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 4),
    _SubVoiceVoipIpInterface_Type()
)
subVoiceVoipIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipIpInterface.setStatus("current")


class _SubVoiceVoipPreferredCodec_Type(ZhoneCodecType):
    """Custom type subVoiceVoipPreferredCodec based on ZhoneCodecType"""


_SubVoiceVoipPreferredCodec_Object = MibTableColumn
subVoiceVoipPreferredCodec = _SubVoiceVoipPreferredCodec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 5),
    _SubVoiceVoipPreferredCodec_Type()
)
subVoiceVoipPreferredCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipPreferredCodec.setStatus("current")


class _SubVoiceVoipG711Fallback_Type(TruthValue):
    """Custom type subVoiceVoipG711Fallback based on TruthValue"""


_SubVoiceVoipG711Fallback_Object = MibTableColumn
subVoiceVoipG711Fallback = _SubVoiceVoipG711Fallback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 6),
    _SubVoiceVoipG711Fallback_Type()
)
subVoiceVoipG711Fallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipG711Fallback.setStatus("current")


class _SubVoiceVoipFramesPerPacket_Type(Integer32):
    """Custom type subVoiceVoipFramesPerPacket based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SubVoiceVoipFramesPerPacket_Type.__name__ = "Integer32"
_SubVoiceVoipFramesPerPacket_Object = MibTableColumn
subVoiceVoipFramesPerPacket = _SubVoiceVoipFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 8),
    _SubVoiceVoipFramesPerPacket_Type()
)
subVoiceVoipFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipFramesPerPacket.setStatus("current")


class _SubVoiceVoipG726ByteOrder_Type(Integer32):
    """Custom type subVoiceVoipG726ByteOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bigEndian", 1),
          ("littleEndian", 2))
    )


_SubVoiceVoipG726ByteOrder_Type.__name__ = "Integer32"
_SubVoiceVoipG726ByteOrder_Object = MibTableColumn
subVoiceVoipG726ByteOrder = _SubVoiceVoipG726ByteOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 9),
    _SubVoiceVoipG726ByteOrder_Type()
)
subVoiceVoipG726ByteOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipG726ByteOrder.setStatus("current")
_SubVoiceVoipPassword_Type = ZhoneAdminString
_SubVoiceVoipPassword_Object = MibTableColumn
subVoiceVoipPassword = _SubVoiceVoipPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 10),
    _SubVoiceVoipPassword_Type()
)
subVoiceVoipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipPassword.setStatus("current")


class _SubVoiceVoipPLAR_Type(TruthValue):
    """Custom type subVoiceVoipPLAR based on TruthValue"""


_SubVoiceVoipPLAR_Object = MibTableColumn
subVoiceVoipPLAR = _SubVoiceVoipPLAR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 11),
    _SubVoiceVoipPLAR_Type()
)
subVoiceVoipPLAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subVoiceVoipPLAR.setStatus("current")


class _SubVoiceVoipPlarDestIpAddrType_Type(InetAddressType):
    """Custom type subVoiceVoipPlarDestIpAddrType based on InetAddressType"""


_SubVoiceVoipPlarDestIpAddrType_Object = MibTableColumn
subVoiceVoipPlarDestIpAddrType = _SubVoiceVoipPlarDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 12),
    _SubVoiceVoipPlarDestIpAddrType_Type()
)
subVoiceVoipPlarDestIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipPlarDestIpAddrType.setStatus("current")
_SubVoiceVoipPlarDestIpAddr_Type = InetAddress
_SubVoiceVoipPlarDestIpAddr_Object = MibTableColumn
subVoiceVoipPlarDestIpAddr = _SubVoiceVoipPlarDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 13),
    _SubVoiceVoipPlarDestIpAddr_Type()
)
subVoiceVoipPlarDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipPlarDestIpAddr.setStatus("current")


class _SubVoiceVoipPlarUdpPort_Type(Integer32):
    """Custom type subVoiceVoipPlarUdpPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SubVoiceVoipPlarUdpPort_Type.__name__ = "Integer32"
_SubVoiceVoipPlarUdpPort_Object = MibTableColumn
subVoiceVoipPlarUdpPort = _SubVoiceVoipPlarUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 14),
    _SubVoiceVoipPlarUdpPort_Type()
)
subVoiceVoipPlarUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipPlarUdpPort.setStatus("current")


class _SubVoiceVoipRegistrationServer_Type(Unsigned32):
    """Custom type subVoiceVoipRegistrationServer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SubVoiceVoipRegistrationServer_Type.__name__ = "Unsigned32"
_SubVoiceVoipRegistrationServer_Object = MibTableColumn
subVoiceVoipRegistrationServer = _SubVoiceVoipRegistrationServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 15),
    _SubVoiceVoipRegistrationServer_Type()
)
subVoiceVoipRegistrationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipRegistrationServer.setStatus("current")


class _SubVoiceVoipT38Fax_Type(T38FaxType):
    """Custom type subVoiceVoipT38Fax based on T38FaxType"""


_SubVoiceVoipT38Fax_Object = MibTableColumn
subVoiceVoipT38Fax = _SubVoiceVoipT38Fax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 16),
    _SubVoiceVoipT38Fax_Type()
)
subVoiceVoipT38Fax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipT38Fax.setStatus("current")
_SubVoiceVoipAuthUsername_Type = ZhoneAdminString
_SubVoiceVoipAuthUsername_Object = MibTableColumn
subVoiceVoipAuthUsername = _SubVoiceVoipAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 17),
    _SubVoiceVoipAuthUsername_Type()
)
subVoiceVoipAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipAuthUsername.setStatus("current")
if mibBuilder.loadTexts:
    subVoiceVoipAuthUsername.setUnits("characters")
_SubVoiceVoipHotlineDN_Type = ZhoneAdminString
_SubVoiceVoipHotlineDN_Object = MibTableColumn
subVoiceVoipHotlineDN = _SubVoiceVoipHotlineDN_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 18),
    _SubVoiceVoipHotlineDN_Type()
)
subVoiceVoipHotlineDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceVoipHotlineDN.setStatus("current")


class _SubVoiceHotlineInitialTimer_Type(Unsigned32):
    """Custom type subVoiceHotlineInitialTimer based on Unsigned32"""
    defaultValue = 4


_SubVoiceHotlineInitialTimer_Object = MibTableColumn
subVoiceHotlineInitialTimer = _SubVoiceHotlineInitialTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 13, 1, 19),
    _SubVoiceHotlineInitialTimer_Type()
)
subVoiceHotlineInitialTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceHotlineInitialTimer.setStatus("current")
if mibBuilder.loadTexts:
    subVoiceHotlineInitialTimer.setUnits("seconds")
_SubVoiceElcpAal2Table_Object = MibTable
subVoiceElcpAal2Table = _SubVoiceElcpAal2Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14)
)
if mibBuilder.loadTexts:
    subVoiceElcpAal2Table.setStatus("current")
_SubVoiceElcpAal2Entry_Object = MibTableRow
subVoiceElcpAal2Entry = _SubVoiceElcpAal2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1)
)
subVoiceElcpAal2Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceAal2EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceElcpAal2Entry.setStatus("current")


class _SubVoiceElcpAal2EndPointIndex_Type(Integer32):
    """Custom type subVoiceElcpAal2EndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceElcpAal2EndPointIndex_Type.__name__ = "Integer32"
_SubVoiceElcpAal2EndPointIndex_Object = MibTableColumn
subVoiceElcpAal2EndPointIndex = _SubVoiceElcpAal2EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 1),
    _SubVoiceElcpAal2EndPointIndex_Type()
)
subVoiceElcpAal2EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceElcpAal2EndPointIndex.setStatus("current")
_SubVoiceElcpAal2LineGroupId_Type = Integer32
_SubVoiceElcpAal2LineGroupId_Object = MibTableColumn
subVoiceElcpAal2LineGroupId = _SubVoiceElcpAal2LineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 2),
    _SubVoiceElcpAal2LineGroupId_Type()
)
subVoiceElcpAal2LineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2LineGroupId.setStatus("current")
_SubVoiceElcpAal2Vpi_Type = AtmVpIdentifier
_SubVoiceElcpAal2Vpi_Object = MibTableColumn
subVoiceElcpAal2Vpi = _SubVoiceElcpAal2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 3),
    _SubVoiceElcpAal2Vpi_Type()
)
subVoiceElcpAal2Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2Vpi.setStatus("current")
_SubVoiceElcpAal2Vci_Type = AtmVcIdentifier
_SubVoiceElcpAal2Vci_Object = MibTableColumn
subVoiceElcpAal2Vci = _SubVoiceElcpAal2Vci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 4),
    _SubVoiceElcpAal2Vci_Type()
)
subVoiceElcpAal2Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2Vci.setStatus("current")


class _SubVoiceElcpAal2PortId_Type(Integer32):
    """Custom type subVoiceElcpAal2PortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SubVoiceElcpAal2PortId_Type.__name__ = "Integer32"
_SubVoiceElcpAal2PortId_Object = MibTableColumn
subVoiceElcpAal2PortId = _SubVoiceElcpAal2PortId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 5),
    _SubVoiceElcpAal2PortId_Type()
)
subVoiceElcpAal2PortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2PortId.setStatus("current")


class _SubVoiceElcpAal2PortType_Type(Integer32):
    """Custom type subVoiceElcpAal2PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdnBChannel", 3),
          ("isdnDChannel", 2),
          ("pots", 1))
    )


_SubVoiceElcpAal2PortType_Type.__name__ = "Integer32"
_SubVoiceElcpAal2PortType_Object = MibTableColumn
subVoiceElcpAal2PortType = _SubVoiceElcpAal2PortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 6),
    _SubVoiceElcpAal2PortType_Type()
)
subVoiceElcpAal2PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2PortType.setStatus("current")


class _SubVoiceElcpAal2IsdnChannelId_Type(Integer32):
    """Custom type subVoiceElcpAal2IsdnChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SubVoiceElcpAal2IsdnChannelId_Type.__name__ = "Integer32"
_SubVoiceElcpAal2IsdnChannelId_Object = MibTableColumn
subVoiceElcpAal2IsdnChannelId = _SubVoiceElcpAal2IsdnChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 14, 1, 7),
    _SubVoiceElcpAal2IsdnChannelId_Type()
)
subVoiceElcpAal2IsdnChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceElcpAal2IsdnChannelId.setStatus("current")
_SubVoiceEbsTable_Object = MibTable
subVoiceEbsTable = _SubVoiceEbsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 15)
)
if mibBuilder.loadTexts:
    subVoiceEbsTable.setStatus("current")
_SubVoiceEbsEntry_Object = MibTableRow
subVoiceEbsEntry = _SubVoiceEbsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 15, 1)
)
subVoiceEbsEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceEbsEndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceEbsEntry.setStatus("current")


class _SubVoiceEbsEndPointIndex_Type(Integer32):
    """Custom type subVoiceEbsEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubVoiceEbsEndPointIndex_Type.__name__ = "Integer32"
_SubVoiceEbsEndPointIndex_Object = MibTableColumn
subVoiceEbsEndPointIndex = _SubVoiceEbsEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 15, 1, 1),
    _SubVoiceEbsEndPointIndex_Type()
)
subVoiceEbsEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceEbsEndPointIndex.setStatus("current")
_SubVoiceEbsLineGroupId_Type = Integer32
_SubVoiceEbsLineGroupId_Object = MibTableColumn
subVoiceEbsLineGroupId = _SubVoiceEbsLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 15, 1, 2),
    _SubVoiceEbsLineGroupId_Type()
)
subVoiceEbsLineGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceEbsLineGroupId.setStatus("current")
_SubVoiceIsdnSigTable_Object = MibTable
subVoiceIsdnSigTable = _SubVoiceIsdnSigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16)
)
if mibBuilder.loadTexts:
    subVoiceIsdnSigTable.setStatus("current")
_SubVoiceIsdnSigEntry_Object = MibTableRow
subVoiceIsdnSigEntry = _SubVoiceIsdnSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1)
)
subVoiceIsdnSigEntry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigEndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceIsdnSigEntry.setStatus("current")


class _SubVoiceIsdnSigEndPointIndex_Type(Integer32):
    """Custom type subVoiceIsdnSigEndPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceIsdnSigEndPointIndex_Type.__name__ = "Integer32"
_SubVoiceIsdnSigEndPointIndex_Object = MibTableColumn
subVoiceIsdnSigEndPointIndex = _SubVoiceIsdnSigEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 1),
    _SubVoiceIsdnSigEndPointIndex_Type()
)
subVoiceIsdnSigEndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceIsdnSigEndPointIndex.setStatus("current")


class _SubVoiceIsdnSigEntryIndex_Type(Integer32):
    """Custom type subVoiceIsdnSigEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubVoiceIsdnSigEntryIndex_Type.__name__ = "Integer32"
_SubVoiceIsdnSigEntryIndex_Object = MibTableColumn
subVoiceIsdnSigEntryIndex = _SubVoiceIsdnSigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 2),
    _SubVoiceIsdnSigEntryIndex_Type()
)
subVoiceIsdnSigEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnSigEntryIndex.setStatus("current")
_SubVoiceIsdnSigDirectoryNumber_Type = ZhoneAdminString
_SubVoiceIsdnSigDirectoryNumber_Object = MibTableColumn
subVoiceIsdnSigDirectoryNumber = _SubVoiceIsdnSigDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 3),
    _SubVoiceIsdnSigDirectoryNumber_Type()
)
subVoiceIsdnSigDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnSigDirectoryNumber.setStatus("current")
_SubVoiceIsdnSigHuntGrpEndPointIndex1_Type = Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex1_Object = MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex1 = _SubVoiceIsdnSigHuntGrpEndPointIndex1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 4),
    _SubVoiceIsdnSigHuntGrpEndPointIndex1_Type()
)
subVoiceIsdnSigHuntGrpEndPointIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnSigHuntGrpEndPointIndex1.setStatus("current")
_SubVoiceIsdnSigHuntGrpEndPointIndex2_Type = Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex2_Object = MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex2 = _SubVoiceIsdnSigHuntGrpEndPointIndex2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 5),
    _SubVoiceIsdnSigHuntGrpEndPointIndex2_Type()
)
subVoiceIsdnSigHuntGrpEndPointIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnSigHuntGrpEndPointIndex2.setStatus("current")
_SubVoiceIsdnSigHuntGrpEndPointIndex3_Type = Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex3_Object = MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex3 = _SubVoiceIsdnSigHuntGrpEndPointIndex3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 16, 1, 6),
    _SubVoiceIsdnSigHuntGrpEndPointIndex3_Type()
)
subVoiceIsdnSigHuntGrpEndPointIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceIsdnSigHuntGrpEndPointIndex3.setStatus("current")
_SubVoiceTr008Table_Object = MibTable
subVoiceTr008Table = _SubVoiceTr008Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 17)
)
if mibBuilder.loadTexts:
    subVoiceTr008Table.setStatus("current")
_SubVoiceTr008Entry_Object = MibTableRow
subVoiceTr008Entry = _SubVoiceTr008Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 17, 1)
)
subVoiceTr008Entry.setIndexNames(
    (0, "ZHONE-GEN-SUBSCRIBER", "subVoiceTr008EndPointIndex"),
)
if mibBuilder.loadTexts:
    subVoiceTr008Entry.setStatus("current")
_SubVoiceTr008EndPointIndex_Type = Integer32
_SubVoiceTr008EndPointIndex_Object = MibTableColumn
subVoiceTr008EndPointIndex = _SubVoiceTr008EndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 17, 1, 1),
    _SubVoiceTr008EndPointIndex_Type()
)
subVoiceTr008EndPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subVoiceTr008EndPointIndex.setStatus("current")
_SubVoiceTr008GroupId_Type = InterfaceIndex
_SubVoiceTr008GroupId_Object = MibTableColumn
subVoiceTr008GroupId = _SubVoiceTr008GroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 17, 1, 2),
    _SubVoiceTr008GroupId_Type()
)
subVoiceTr008GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceTr008GroupId.setStatus("current")


class _SubVoiceTr008ChanNum_Type(Integer32):
    """Custom type subVoiceTr008ChanNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SubVoiceTr008ChanNum_Type.__name__ = "Integer32"
_SubVoiceTr008ChanNum_Object = MibTableColumn
subVoiceTr008ChanNum = _SubVoiceTr008ChanNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 17, 1, 3),
    _SubVoiceTr008ChanNum_Type()
)
subVoiceTr008ChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subVoiceTr008ChanNum.setStatus("current")

# Managed Objects groups

zhoneSubscriberObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 4, 1, 11)
)
zhoneSubscriberObjectsGroup.setObjects(
      *(("ZHONE-GEN-SUBSCRIBER", "nextSubId"),
        ("ZHONE-GEN-SUBSCRIBER", "nextEndPointIndex"),
        ("ZHONE-GEN-SUBSCRIBER", "subName"),
        ("ZHONE-GEN-SUBSCRIBER", "subProviderId"),
        ("ZHONE-GEN-SUBSCRIBER", "subIadType"),
        ("ZHONE-GEN-SUBSCRIBER", "subMaxAllowedLineRate"),
        ("ZHONE-GEN-SUBSCRIBER", "subMaxCapableLineRate"),
        ("ZHONE-GEN-SUBSCRIBER", "subNextVoiceConnectionIndex"),
        ("ZHONE-GEN-SUBSCRIBER", "subRowStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataIpIfOperStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataUserLogOnId"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataUserPassword"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataMaxAddrAllowed"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataIpAddrInUse"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataCurrentIpAddr"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataStatsStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subDataRowStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceConnectionType"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceEndPoint1AddressIndex"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceEndPoint2AddressIndex"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceConnectionDescription"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceAdminStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceRowStatus"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2LineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Vpi"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Vci"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Cid"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceGr303IgName"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceGr303IgCrv"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceV52InterfaceName"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceV52UserPortId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceV52UserType"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceV52IsdnChannelId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoicePotsLineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnLineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnType"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnChannelId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceDs1Ds0ChannelID"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceDs1LineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2LineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2Vpi"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2Vci"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2PortId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2PortType"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceElcpAal2IsdnChannelId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceEbsLineGroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceHuntGroup"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceDs1HuntGrpEndPointIndex3"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceDs1HuntGrpEndPointIndex1"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoicePotsHuntGrpEndPointIndex3"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoicePotsHuntGrpEndPointIndex2"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoicePotsHuntGrpEndPointIndex1"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceDs1HuntGrpEndPointIndex2"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPassword"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipG726ByteOrder"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipFramesPerPacket"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipG711Fallback"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPreferredCodec"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipDirectoryNumber"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipIpInterface"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipUserName"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigHuntGrpEndPointIndex3"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigHuntGrpEndPointIndex2"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPlarDestIpAddr"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPLAR"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPlarUdpPort"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipPlarDestIpAddrType"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceFeatureSetOne"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceTr008ChanNum"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceTr008GroupId"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipAuthUsername"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceHotlineInitialTimer"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceVoipHotlineDN"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigHuntGrpEndPointIndex1"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigEntryIndex"),
        ("ZHONE-GEN-SUBSCRIBER", "subVoiceIsdnSigDirectoryNumber"))
)
if mibBuilder.loadTexts:
    zhoneSubscriberObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-SUBSCRIBER",
    **{"ZhoneCodecType": ZhoneCodecType,
       "T38FaxType": T38FaxType,
       "zhoneSubscriberRecords": zhoneSubscriberRecords,
       "nextSubId": nextSubId,
       "nextEndPointIndex": nextEndPointIndex,
       "subInfoTable": subInfoTable,
       "subInfoEntry": subInfoEntry,
       "subId": subId,
       "subLgId": subLgId,
       "subName": subName,
       "subProviderId": subProviderId,
       "subIadType": subIadType,
       "subMaxAllowedLineRate": subMaxAllowedLineRate,
       "subMaxCapableLineRate": subMaxCapableLineRate,
       "subNextVoiceConnectionIndex": subNextVoiceConnectionIndex,
       "subRowStatus": subRowStatus,
       "subDataConnectionTable": subDataConnectionTable,
       "subDataConnectionEntry": subDataConnectionEntry,
       "subDataIfIndex": subDataIfIndex,
       "subDataIpIfOperStatus": subDataIpIfOperStatus,
       "subDataUserLogOnId": subDataUserLogOnId,
       "subDataUserPassword": subDataUserPassword,
       "subDataMaxAddrAllowed": subDataMaxAddrAllowed,
       "subDataIpAddrInUse": subDataIpAddrInUse,
       "subDataCurrentIpAddr": subDataCurrentIpAddr,
       "subDataStatsStatus": subDataStatsStatus,
       "subDataRowStatus": subDataRowStatus,
       "subVoiceConnectionTable": subVoiceConnectionTable,
       "subVoiceConnectionEntry": subVoiceConnectionEntry,
       "subVoiceConnectionIndex": subVoiceConnectionIndex,
       "subVoiceConnectionType": subVoiceConnectionType,
       "subVoiceEndPoint1AddressIndex": subVoiceEndPoint1AddressIndex,
       "subVoiceEndPoint2AddressIndex": subVoiceEndPoint2AddressIndex,
       "subVoiceConnectionDescription": subVoiceConnectionDescription,
       "subVoiceAdminStatus": subVoiceAdminStatus,
       "subVoiceRowStatus": subVoiceRowStatus,
       "subVoiceHuntGroup": subVoiceHuntGroup,
       "subVoiceFeatureSetOne": subVoiceFeatureSetOne,
       "subVoiceAal2Table": subVoiceAal2Table,
       "subVoiceAal2Entry": subVoiceAal2Entry,
       "subVoiceAal2EndPointIndex": subVoiceAal2EndPointIndex,
       "subVoiceAal2LineGroupId": subVoiceAal2LineGroupId,
       "subVoiceAal2Vpi": subVoiceAal2Vpi,
       "subVoiceAal2Vci": subVoiceAal2Vci,
       "subVoiceAal2Cid": subVoiceAal2Cid,
       "subVoiceGr303Table": subVoiceGr303Table,
       "subVoiceGr303Entry": subVoiceGr303Entry,
       "subVoiceGr303EndPointIndex": subVoiceGr303EndPointIndex,
       "subVoiceGr303IgName": subVoiceGr303IgName,
       "subVoiceGr303IgCrv": subVoiceGr303IgCrv,
       "subVoiceV52Table": subVoiceV52Table,
       "subVoiceV52Entry": subVoiceV52Entry,
       "subVoiceV52EndPointIndex": subVoiceV52EndPointIndex,
       "subVoiceV52InterfaceName": subVoiceV52InterfaceName,
       "subVoiceV52UserPortId": subVoiceV52UserPortId,
       "subVoiceV52UserType": subVoiceV52UserType,
       "subVoiceV52IsdnChannelId": subVoiceV52IsdnChannelId,
       "subVoicePotsTable": subVoicePotsTable,
       "subVoicePotsEntry": subVoicePotsEntry,
       "subVoicePotsEndPointIndex": subVoicePotsEndPointIndex,
       "subVoicePotsLineGroupId": subVoicePotsLineGroupId,
       "subVoicePotsHuntGrpEndPointIndex1": subVoicePotsHuntGrpEndPointIndex1,
       "subVoicePotsHuntGrpEndPointIndex2": subVoicePotsHuntGrpEndPointIndex2,
       "subVoicePotsHuntGrpEndPointIndex3": subVoicePotsHuntGrpEndPointIndex3,
       "subVoiceIsdnTable": subVoiceIsdnTable,
       "subVoiceIsdnEntry": subVoiceIsdnEntry,
       "subVoiceIsdnEndPointIndex": subVoiceIsdnEndPointIndex,
       "subVoiceIsdnLineGroupId": subVoiceIsdnLineGroupId,
       "subVoiceIsdnType": subVoiceIsdnType,
       "subVoiceIsdnChannelId": subVoiceIsdnChannelId,
       "zhoneSubscriberObjectsGroup": zhoneSubscriberObjectsGroup,
       "subVoiceDs1Table": subVoiceDs1Table,
       "subVoiceDs1Entry": subVoiceDs1Entry,
       "subVoiceDs1EndPointIndex": subVoiceDs1EndPointIndex,
       "subVoiceDs1Ds0ChannelID": subVoiceDs1Ds0ChannelID,
       "subVoiceDs1LineGroupId": subVoiceDs1LineGroupId,
       "subVoiceDs1HuntGrpEndPointIndex1": subVoiceDs1HuntGrpEndPointIndex1,
       "subVoiceDs1HuntGrpEndPointIndex2": subVoiceDs1HuntGrpEndPointIndex2,
       "subVoiceDs1HuntGrpEndPointIndex3": subVoiceDs1HuntGrpEndPointIndex3,
       "subVoiceVoipTable": subVoiceVoipTable,
       "subVoiceVoipEntry": subVoiceVoipEntry,
       "subVoiceVoipEndPointIndex": subVoiceVoipEndPointIndex,
       "subVoiceVoipUserName": subVoiceVoipUserName,
       "subVoiceVoipDirectoryNumber": subVoiceVoipDirectoryNumber,
       "subVoiceVoipIpInterface": subVoiceVoipIpInterface,
       "subVoiceVoipPreferredCodec": subVoiceVoipPreferredCodec,
       "subVoiceVoipG711Fallback": subVoiceVoipG711Fallback,
       "subVoiceVoipFramesPerPacket": subVoiceVoipFramesPerPacket,
       "subVoiceVoipG726ByteOrder": subVoiceVoipG726ByteOrder,
       "subVoiceVoipPassword": subVoiceVoipPassword,
       "subVoiceVoipPLAR": subVoiceVoipPLAR,
       "subVoiceVoipPlarDestIpAddrType": subVoiceVoipPlarDestIpAddrType,
       "subVoiceVoipPlarDestIpAddr": subVoiceVoipPlarDestIpAddr,
       "subVoiceVoipPlarUdpPort": subVoiceVoipPlarUdpPort,
       "subVoiceVoipRegistrationServer": subVoiceVoipRegistrationServer,
       "subVoiceVoipT38Fax": subVoiceVoipT38Fax,
       "subVoiceVoipAuthUsername": subVoiceVoipAuthUsername,
       "subVoiceVoipHotlineDN": subVoiceVoipHotlineDN,
       "subVoiceHotlineInitialTimer": subVoiceHotlineInitialTimer,
       "subVoiceElcpAal2Table": subVoiceElcpAal2Table,
       "subVoiceElcpAal2Entry": subVoiceElcpAal2Entry,
       "subVoiceElcpAal2EndPointIndex": subVoiceElcpAal2EndPointIndex,
       "subVoiceElcpAal2LineGroupId": subVoiceElcpAal2LineGroupId,
       "subVoiceElcpAal2Vpi": subVoiceElcpAal2Vpi,
       "subVoiceElcpAal2Vci": subVoiceElcpAal2Vci,
       "subVoiceElcpAal2PortId": subVoiceElcpAal2PortId,
       "subVoiceElcpAal2PortType": subVoiceElcpAal2PortType,
       "subVoiceElcpAal2IsdnChannelId": subVoiceElcpAal2IsdnChannelId,
       "subVoiceEbsTable": subVoiceEbsTable,
       "subVoiceEbsEntry": subVoiceEbsEntry,
       "subVoiceEbsEndPointIndex": subVoiceEbsEndPointIndex,
       "subVoiceEbsLineGroupId": subVoiceEbsLineGroupId,
       "subVoiceIsdnSigTable": subVoiceIsdnSigTable,
       "subVoiceIsdnSigEntry": subVoiceIsdnSigEntry,
       "subVoiceIsdnSigEndPointIndex": subVoiceIsdnSigEndPointIndex,
       "subVoiceIsdnSigEntryIndex": subVoiceIsdnSigEntryIndex,
       "subVoiceIsdnSigDirectoryNumber": subVoiceIsdnSigDirectoryNumber,
       "subVoiceIsdnSigHuntGrpEndPointIndex1": subVoiceIsdnSigHuntGrpEndPointIndex1,
       "subVoiceIsdnSigHuntGrpEndPointIndex2": subVoiceIsdnSigHuntGrpEndPointIndex2,
       "subVoiceIsdnSigHuntGrpEndPointIndex3": subVoiceIsdnSigHuntGrpEndPointIndex3,
       "subVoiceTr008Table": subVoiceTr008Table,
       "subVoiceTr008Entry": subVoiceTr008Entry,
       "subVoiceTr008EndPointIndex": subVoiceTr008EndPointIndex,
       "subVoiceTr008GroupId": subVoiceTr008GroupId,
       "subVoiceTr008ChanNum": subVoiceTr008ChanNum}
)
