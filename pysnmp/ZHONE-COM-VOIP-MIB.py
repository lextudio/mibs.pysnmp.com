# SNMP MIB module (ZHONE-COM-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-VOIP-MIB
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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

(ZhoneCodecType,) = mibBuilder.importSymbols(
    "ZHONE-GEN-SUBSCRIBER",
    "ZhoneCodecType")

(zhoneVoice,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneVoice")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneVoip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4)
)
zhoneVoip.setRevisions(
        ("2014-10-16 23:33",
         "2014-08-26 10:40",
         "2014-07-03 02:40",
         "2014-06-16 21:40",
         "2014-05-22 14:09",
         "2014-01-02 22:13",
         "2012-09-17 23:42",
         "2012-09-17 23:39",
         "2011-12-22 02:24",
         "2011-10-20 12:14",
         "2011-07-25 11:44",
         "2009-10-07 01:41",
         "2009-03-21 02:08",
         "2008-10-31 01:12",
         "2008-08-27 23:02",
         "2008-06-11 17:40",
         "2007-07-16 02:45",
         "2006-04-13 15:53",
         "2005-10-11 11:46",
         "2005-07-12 10:25",
         "2005-07-07 16:06",
         "2005-07-07 15:12",
         "2005-06-01 11:09",
         "2005-05-19 15:46",
         "2005-05-14 21:24",
         "2005-02-28 10:49",
         "2004-11-01 14:34",
         "2004-03-03 17:40",
         "2004-02-24 12:36",
         "2004-01-06 15:37",
         "2003-11-06 10:08",
         "2003-10-16 14:53",
         "2003-08-27 11:30",
         "2003-08-08 17:19",
         "2003-05-28 12:00",
         "2003-03-31 18:03",
         "2003-02-18 14:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneVoipSystem_ObjectIdentity = ObjectIdentity
zhoneVoipSystem = _ZhoneVoipSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneVoipSystem.setStatus("deprecated")


class _ZhoneVoipSystemProtocol_Type(Integer32):
    """Custom type zhoneVoipSystemProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgcp", 2),
          ("sip", 1))
    )


_ZhoneVoipSystemProtocol_Type.__name__ = "Integer32"
_ZhoneVoipSystemProtocol_Object = MibScalar
zhoneVoipSystemProtocol = _ZhoneVoipSystemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 1),
    _ZhoneVoipSystemProtocol_Type()
)
zhoneVoipSystemProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVoipSystemProtocol.setStatus("deprecated")


class _ZhoneVoipSystemSendCallProceedingTone_Type(TruthValue):
    """Custom type zhoneVoipSystemSendCallProceedingTone based on TruthValue"""


_ZhoneVoipSystemSendCallProceedingTone_Object = MibScalar
zhoneVoipSystemSendCallProceedingTone = _ZhoneVoipSystemSendCallProceedingTone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 2),
    _ZhoneVoipSystemSendCallProceedingTone_Type()
)
zhoneVoipSystemSendCallProceedingTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSystemSendCallProceedingTone.setStatus("deprecated")


class _ZhoneVoipSystemRtcpEnabled_Type(TruthValue):
    """Custom type zhoneVoipSystemRtcpEnabled based on TruthValue"""


_ZhoneVoipSystemRtcpEnabled_Object = MibScalar
zhoneVoipSystemRtcpEnabled = _ZhoneVoipSystemRtcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 3),
    _ZhoneVoipSystemRtcpEnabled_Type()
)
zhoneVoipSystemRtcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSystemRtcpEnabled.setStatus("deprecated")


class _ZhoneVoipSystemRtcpPacketInterval_Type(Integer32):
    """Custom type zhoneVoipSystemRtcpPacketInterval based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 10000),
    )


_ZhoneVoipSystemRtcpPacketInterval_Type.__name__ = "Integer32"
_ZhoneVoipSystemRtcpPacketInterval_Object = MibScalar
zhoneVoipSystemRtcpPacketInterval = _ZhoneVoipSystemRtcpPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 4),
    _ZhoneVoipSystemRtcpPacketInterval_Type()
)
zhoneVoipSystemRtcpPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSystemRtcpPacketInterval.setStatus("deprecated")


class _ZhoneVoipSystemInterdigitTimeout_Type(Integer32):
    """Custom type zhoneVoipSystemInterdigitTimeout based on Integer32"""
    defaultValue = 10


_ZhoneVoipSystemInterdigitTimeout_Object = MibScalar
zhoneVoipSystemInterdigitTimeout = _ZhoneVoipSystemInterdigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 5),
    _ZhoneVoipSystemInterdigitTimeout_Type()
)
zhoneVoipSystemInterdigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSystemInterdigitTimeout.setStatus("deprecated")


class _ZhoneVoipSystemIpTos_Type(Integer32):
    """Custom type zhoneVoipSystemIpTos based on Integer32"""
    defaultValue = 0


_ZhoneVoipSystemIpTos_Object = MibScalar
zhoneVoipSystemIpTos = _ZhoneVoipSystemIpTos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 6),
    _ZhoneVoipSystemIpTos_Type()
)
zhoneVoipSystemIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSystemIpTos.setStatus("deprecated")
_ZhoneVoipSystemDomainName_Type = SnmpAdminString
_ZhoneVoipSystemDomainName_Object = MibScalar
zhoneVoipSystemDomainName = _ZhoneVoipSystemDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 1, 7),
    _ZhoneVoipSystemDomainName_Type()
)
zhoneVoipSystemDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVoipSystemDomainName.setStatus("deprecated")
_ZhoneVoipSipDialPlan_ObjectIdentity = ObjectIdentity
zhoneVoipSipDialPlan = _ZhoneVoipSipDialPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3)
)
_NextVoipSipDialPlanId_Type = Integer32
_NextVoipSipDialPlanId_Object = MibScalar
nextVoipSipDialPlanId = _NextVoipSipDialPlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 1),
    _NextVoipSipDialPlanId_Type()
)
nextVoipSipDialPlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextVoipSipDialPlanId.setStatus("current")
_ZhoneVoipSipDialPlanTable_Object = MibTable
zhoneVoipSipDialPlanTable = _ZhoneVoipSipDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanTable.setStatus("current")
_ZhoneVoipSipDialPlanEntry_Object = MibTableRow
zhoneVoipSipDialPlanEntry = _ZhoneVoipSipDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1)
)
zhoneVoipSipDialPlanEntry.setIndexNames(
    (0, "ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialPlanId"),
)
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanEntry.setStatus("current")


class _ZhoneVoipSipDialPlanId_Type(Integer32):
    """Custom type zhoneVoipSipDialPlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneVoipSipDialPlanId_Type.__name__ = "Integer32"
_ZhoneVoipSipDialPlanId_Object = MibTableColumn
zhoneVoipSipDialPlanId = _ZhoneVoipSipDialPlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 1),
    _ZhoneVoipSipDialPlanId_Type()
)
zhoneVoipSipDialPlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanId.setStatus("current")


class _ZhoneVoipSipDialString_Type(SnmpAdminString):
    """Custom type zhoneVoipSipDialString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZhoneVoipSipDialString_Type.__name__ = "SnmpAdminString"
_ZhoneVoipSipDialString_Object = MibTableColumn
zhoneVoipSipDialString = _ZhoneVoipSipDialString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 2),
    _ZhoneVoipSipDialString_Type()
)
zhoneVoipSipDialString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialString.setStatus("current")
_ZhoneVoipSipDialIpAddr_Type = IpAddress
_ZhoneVoipSipDialIpAddr_Object = MibTableColumn
zhoneVoipSipDialIpAddr = _ZhoneVoipSipDialIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 3),
    _ZhoneVoipSipDialIpAddr_Type()
)
zhoneVoipSipDialIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialIpAddr.setStatus("current")
_ZhoneVoipSipDialPlanRowStatus_Type = ZhoneRowStatus
_ZhoneVoipSipDialPlanRowStatus_Object = MibTableColumn
zhoneVoipSipDialPlanRowStatus = _ZhoneVoipSipDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 4),
    _ZhoneVoipSipDialPlanRowStatus_Type()
)
zhoneVoipSipDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanRowStatus.setStatus("current")
_ZhoneVoipSipDialDestName_Type = SnmpAdminString
_ZhoneVoipSipDialDestName_Object = MibTableColumn
zhoneVoipSipDialDestName = _ZhoneVoipSipDialDestName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 5),
    _ZhoneVoipSipDialDestName_Type()
)
zhoneVoipSipDialDestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialDestName.setStatus("current")


class _ZhoneVoipSipDialNumOfDigits_Type(Integer32):
    """Custom type zhoneVoipSipDialNumOfDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZhoneVoipSipDialNumOfDigits_Type.__name__ = "Integer32"
_ZhoneVoipSipDialNumOfDigits_Object = MibTableColumn
zhoneVoipSipDialNumOfDigits = _ZhoneVoipSipDialNumOfDigits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 6),
    _ZhoneVoipSipDialNumOfDigits_Type()
)
zhoneVoipSipDialNumOfDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialNumOfDigits.setStatus("current")


class _ZhoneVoipSipDialPrefixStrip_Type(Integer32):
    """Custom type zhoneVoipSipDialPrefixStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZhoneVoipSipDialPrefixStrip_Type.__name__ = "Integer32"
_ZhoneVoipSipDialPrefixStrip_Object = MibTableColumn
zhoneVoipSipDialPrefixStrip = _ZhoneVoipSipDialPrefixStrip_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 7),
    _ZhoneVoipSipDialPrefixStrip_Type()
)
zhoneVoipSipDialPrefixStrip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPrefixStrip.setStatus("current")
_ZhoneVoipSipDialPrefixAdd_Type = SnmpAdminString
_ZhoneVoipSipDialPrefixAdd_Object = MibTableColumn
zhoneVoipSipDialPrefixAdd = _ZhoneVoipSipDialPrefixAdd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 8),
    _ZhoneVoipSipDialPrefixAdd_Type()
)
zhoneVoipSipDialPrefixAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPrefixAdd.setStatus("current")


class _ZhoneVoipSipDialPlanType_Type(Integer32):
    """Custom type zhoneVoipSipDialPlanType based on Integer32"""
    defaultValue = 1

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
        *(("callpark", 2),
          ("esa", 3),
          ("intercom", 5),
          ("isdnsig", 4),
          ("normal", 1))
    )


_ZhoneVoipSipDialPlanType_Type.__name__ = "Integer32"
_ZhoneVoipSipDialPlanType_Object = MibTableColumn
zhoneVoipSipDialPlanType = _ZhoneVoipSipDialPlanType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 9),
    _ZhoneVoipSipDialPlanType_Type()
)
zhoneVoipSipDialPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanType.setStatus("current")


class _ZhoneVoipServerEntryIndex_Type(Integer32):
    """Custom type zhoneVoipServerEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVoipServerEntryIndex_Type.__name__ = "Integer32"
_ZhoneVoipServerEntryIndex_Object = MibTableColumn
zhoneVoipServerEntryIndex = _ZhoneVoipServerEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 10),
    _ZhoneVoipServerEntryIndex_Type()
)
zhoneVoipServerEntryIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerEntryIndex.setStatus("current")
_ZhoneVoipOverrideInterdigitTimeout_Type = Integer32
_ZhoneVoipOverrideInterdigitTimeout_Object = MibTableColumn
zhoneVoipOverrideInterdigitTimeout = _ZhoneVoipOverrideInterdigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 11),
    _ZhoneVoipOverrideInterdigitTimeout_Type()
)
zhoneVoipOverrideInterdigitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipOverrideInterdigitTimeout.setStatus("current")


class _ZhoneVoipSipDialPlanClass_Type(Bits):
    """Custom type zhoneVoipSipDialPlanClass based on Bits"""
    namedValues = NamedValues(
        ("emergency", 0)
    )

_ZhoneVoipSipDialPlanClass_Type.__name__ = "Bits"
_ZhoneVoipSipDialPlanClass_Object = MibTableColumn
zhoneVoipSipDialPlanClass = _ZhoneVoipSipDialPlanClass_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 12),
    _ZhoneVoipSipDialPlanClass_Type()
)
zhoneVoipSipDialPlanClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanClass.setStatus("current")
_ZhoneVoipSipDialPlanDescription_Type = SnmpAdminString
_ZhoneVoipSipDialPlanDescription_Object = MibTableColumn
zhoneVoipSipDialPlanDescription = _ZhoneVoipSipDialPlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 3, 2, 1, 13),
    _ZhoneVoipSipDialPlanDescription_Type()
)
zhoneVoipSipDialPlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipSipDialPlanDescription.setStatus("current")
_ZhoneVoipHuntGroup_ObjectIdentity = ObjectIdentity
zhoneVoipHuntGroup = _ZhoneVoipHuntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4)
)
_NextZhoneVoipHuntGroupId_Type = Integer32
_NextZhoneVoipHuntGroupId_Object = MibScalar
nextZhoneVoipHuntGroupId = _NextZhoneVoipHuntGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 2),
    _NextZhoneVoipHuntGroupId_Type()
)
nextZhoneVoipHuntGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextZhoneVoipHuntGroupId.setStatus("current")
_ZhoneVoipHuntGroupTable_Object = MibTable
zhoneVoipHuntGroupTable = _ZhoneVoipHuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupTable.setStatus("current")
_ZhoneVoipHuntGroupEntry_Object = MibTableRow
zhoneVoipHuntGroupEntry = _ZhoneVoipHuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1)
)
zhoneVoipHuntGroupEntry.setIndexNames(
    (0, "ZHONE-COM-VOIP-MIB", "zhoneVoipHuntGroupId"),
)
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupEntry.setStatus("current")


class _ZhoneVoipHuntGroupId_Type(Integer32):
    """Custom type zhoneVoipHuntGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneVoipHuntGroupId_Type.__name__ = "Integer32"
_ZhoneVoipHuntGroupId_Object = MibTableColumn
zhoneVoipHuntGroupId = _ZhoneVoipHuntGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1, 1),
    _ZhoneVoipHuntGroupId_Type()
)
zhoneVoipHuntGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupId.setStatus("current")


class _ZhoneVoipHuntGroupDestUri_Type(SnmpAdminString):
    """Custom type zhoneVoipHuntGroupDestUri based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZhoneVoipHuntGroupDestUri_Type.__name__ = "SnmpAdminString"
_ZhoneVoipHuntGroupDestUri_Object = MibTableColumn
zhoneVoipHuntGroupDestUri = _ZhoneVoipHuntGroupDestUri_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1, 2),
    _ZhoneVoipHuntGroupDestUri_Type()
)
zhoneVoipHuntGroupDestUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupDestUri.setStatus("current")


class _ZhoneVoipHuntGroupDefaultCodec_Type(ZhoneCodecType):
    """Custom type zhoneVoipHuntGroupDefaultCodec based on ZhoneCodecType"""


_ZhoneVoipHuntGroupDefaultCodec_Object = MibTableColumn
zhoneVoipHuntGroupDefaultCodec = _ZhoneVoipHuntGroupDefaultCodec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1, 3),
    _ZhoneVoipHuntGroupDefaultCodec_Type()
)
zhoneVoipHuntGroupDefaultCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupDefaultCodec.setStatus("current")


class _ZhoneVoipHuntGroupPortMembers_Type(Bits):
    """Custom type zhoneVoipHuntGroupPortMembers based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port2", 1),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8))
    )

_ZhoneVoipHuntGroupPortMembers_Type.__name__ = "Bits"
_ZhoneVoipHuntGroupPortMembers_Object = MibTableColumn
zhoneVoipHuntGroupPortMembers = _ZhoneVoipHuntGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1, 4),
    _ZhoneVoipHuntGroupPortMembers_Type()
)
zhoneVoipHuntGroupPortMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupPortMembers.setStatus("current")
_ZhoneVoipHuntGroupRowStatus_Type = ZhoneRowStatus
_ZhoneVoipHuntGroupRowStatus_Object = MibTableColumn
zhoneVoipHuntGroupRowStatus = _ZhoneVoipHuntGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 4, 3, 1, 5),
    _ZhoneVoipHuntGroupRowStatus_Type()
)
zhoneVoipHuntGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipHuntGroupRowStatus.setStatus("current")
_ZhoneVoipMaliciousCaller_ObjectIdentity = ObjectIdentity
zhoneVoipMaliciousCaller = _ZhoneVoipMaliciousCaller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5)
)
_NextVoipMaliciousCallerId_Type = Integer32
_NextVoipMaliciousCallerId_Object = MibScalar
nextVoipMaliciousCallerId = _NextVoipMaliciousCallerId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 1),
    _NextVoipMaliciousCallerId_Type()
)
nextVoipMaliciousCallerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextVoipMaliciousCallerId.setStatus("current")
_ZhoneVoipMaliciousCallerTable_Object = MibTable
zhoneVoipMaliciousCallerTable = _ZhoneVoipMaliciousCallerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerTable.setStatus("current")
_ZhoneVoipMaliciousCallerEntry_Object = MibTableRow
zhoneVoipMaliciousCallerEntry = _ZhoneVoipMaliciousCallerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2, 1)
)
zhoneVoipMaliciousCallerEntry.setIndexNames(
    (0, "ZHONE-COM-VOIP-MIB", "zhoneVoipMaliciousCallerId"),
)
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerEntry.setStatus("current")


class _ZhoneVoipMaliciousCallerId_Type(Integer32):
    """Custom type zhoneVoipMaliciousCallerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneVoipMaliciousCallerId_Type.__name__ = "Integer32"
_ZhoneVoipMaliciousCallerId_Object = MibTableColumn
zhoneVoipMaliciousCallerId = _ZhoneVoipMaliciousCallerId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2, 1, 1),
    _ZhoneVoipMaliciousCallerId_Type()
)
zhoneVoipMaliciousCallerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerId.setStatus("current")
_ZhoneVoipMaliciousCallerUri_Type = SnmpAdminString
_ZhoneVoipMaliciousCallerUri_Object = MibTableColumn
zhoneVoipMaliciousCallerUri = _ZhoneVoipMaliciousCallerUri_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2, 1, 2),
    _ZhoneVoipMaliciousCallerUri_Type()
)
zhoneVoipMaliciousCallerUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerUri.setStatus("current")


class _ZhoneVoipMaliciousCallerEnable_Type(TruthValue):
    """Custom type zhoneVoipMaliciousCallerEnable based on TruthValue"""


_ZhoneVoipMaliciousCallerEnable_Object = MibTableColumn
zhoneVoipMaliciousCallerEnable = _ZhoneVoipMaliciousCallerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2, 1, 3),
    _ZhoneVoipMaliciousCallerEnable_Type()
)
zhoneVoipMaliciousCallerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerEnable.setStatus("current")
_ZhoneVoipMaliciousCallerRowStatus_Type = ZhoneRowStatus
_ZhoneVoipMaliciousCallerRowStatus_Object = MibTableColumn
zhoneVoipMaliciousCallerRowStatus = _ZhoneVoipMaliciousCallerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 5, 2, 1, 4),
    _ZhoneVoipMaliciousCallerRowStatus_Type()
)
zhoneVoipMaliciousCallerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipMaliciousCallerRowStatus.setStatus("current")
_ZhoneVoipServerCfg_ObjectIdentity = ObjectIdentity
zhoneVoipServerCfg = _ZhoneVoipServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6)
)
_ZhoneVoipServerTable_Object = MibTable
zhoneVoipServerTable = _ZhoneVoipServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    zhoneVoipServerTable.setStatus("current")
_ZhoneVoipServerEntry_Object = MibTableRow
zhoneVoipServerEntry = _ZhoneVoipServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1)
)
zhoneVoipServerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ZHONE-COM-VOIP-MIB", "zhoneVoipServerAddressIndex"),
)
if mibBuilder.loadTexts:
    zhoneVoipServerEntry.setStatus("current")
_ZhoneVoipServerAddressIndex_Type = Unsigned32
_ZhoneVoipServerAddressIndex_Object = MibTableColumn
zhoneVoipServerAddressIndex = _ZhoneVoipServerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 1),
    _ZhoneVoipServerAddressIndex_Type()
)
zhoneVoipServerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVoipServerAddressIndex.setStatus("current")
_ZhoneVoipServerRowStatus_Type = ZhoneRowStatus
_ZhoneVoipServerRowStatus_Object = MibTableColumn
zhoneVoipServerRowStatus = _ZhoneVoipServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 2),
    _ZhoneVoipServerRowStatus_Type()
)
zhoneVoipServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerRowStatus.setStatus("current")


class _ZhoneVoipServerAddrType_Type(InetAddressType):
    """Custom type zhoneVoipServerAddrType based on InetAddressType"""


_ZhoneVoipServerAddrType_Object = MibTableColumn
zhoneVoipServerAddrType = _ZhoneVoipServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 3),
    _ZhoneVoipServerAddrType_Type()
)
zhoneVoipServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerAddrType.setStatus("current")
_ZhoneVoipServerAddr_Type = InetAddress
_ZhoneVoipServerAddr_Object = MibTableColumn
zhoneVoipServerAddr = _ZhoneVoipServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 4),
    _ZhoneVoipServerAddr_Type()
)
zhoneVoipServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerAddr.setStatus("current")


class _ZhoneVoipServerUdpPortNumber_Type(Integer32):
    """Custom type zhoneVoipServerUdpPortNumber based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneVoipServerUdpPortNumber_Type.__name__ = "Integer32"
_ZhoneVoipServerUdpPortNumber_Object = MibTableColumn
zhoneVoipServerUdpPortNumber = _ZhoneVoipServerUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 5),
    _ZhoneVoipServerUdpPortNumber_Type()
)
zhoneVoipServerUdpPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerUdpPortNumber.setStatus("current")


class _ZhoneVoipServerId_Type(Integer32):
    """Custom type zhoneVoipServerId based on Integer32"""
    defaultValue = 10

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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("alu-5060", 37),
          ("asterisk", 2),
          ("broadsoft", 6),
          ("broadsoft-broadworks", 32),
          ("broadsoft-m6", 33),
          ("cedarpoint-safari", 27),
          ("cirpack-utp", 21),
          ("cisco-bts", 20),
          ("cisco-pgw", 23),
          ("coppercom", 18),
          ("ericsson-apz60", 38),
          ("genband-g6", 36),
          ("genband-g9", 34),
          ("generalbandwidth", 8),
          ("generic", 10),
          ("huawei-softx3000", 28),
          ("italtel-issw", 22),
          ("longboard", 1),
          ("lucent-imerge", 17),
          ("lucent-telica", 14),
          ("metaswitch", 4),
          ("microtrol-msk10", 24),
          ("netcentrex", 35),
          ("newcross", 19),
          ("nortel-cs1500", 29),
          ("nortel-cs2000", 15),
          ("nortel-dms10", 25),
          ("nuera", 16),
          ("siemens", 12),
          ("sipexpressrouter", 3),
          ("sonus", 11),
          ("sylantro", 5),
          ("taqua-t7000", 30),
          ("tekelec-T6000", 9),
          ("tekelec-T9000", 13),
          ("ubiquity", 7),
          ("utstarcom-mswitch", 31),
          ("verso-clarent-c5cm", 26))
    )


_ZhoneVoipServerId_Type.__name__ = "Integer32"
_ZhoneVoipServerId_Object = MibTableColumn
zhoneVoipServerId = _ZhoneVoipServerId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 6),
    _ZhoneVoipServerId_Type()
)
zhoneVoipServerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerId.setStatus("current")


class _ZhoneVoipServerProtocol_Type(Integer32):
    """Custom type zhoneVoipServerProtocol based on Integer32"""
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
        *(("megaco", 3),
          ("mgcp", 2),
          ("ncs", 4),
          ("sip", 1))
    )


_ZhoneVoipServerProtocol_Type.__name__ = "Integer32"
_ZhoneVoipServerProtocol_Object = MibTableColumn
zhoneVoipServerProtocol = _ZhoneVoipServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 7),
    _ZhoneVoipServerProtocol_Type()
)
zhoneVoipServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerProtocol.setStatus("current")


class _ZhoneVoipServerSendCallProceedingTone_Type(TruthValue):
    """Custom type zhoneVoipServerSendCallProceedingTone based on TruthValue"""


_ZhoneVoipServerSendCallProceedingTone_Object = MibTableColumn
zhoneVoipServerSendCallProceedingTone = _ZhoneVoipServerSendCallProceedingTone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 8),
    _ZhoneVoipServerSendCallProceedingTone_Type()
)
zhoneVoipServerSendCallProceedingTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSendCallProceedingTone.setStatus("current")


class _ZhoneVoipServerRtcpEnabled_Type(TruthValue):
    """Custom type zhoneVoipServerRtcpEnabled based on TruthValue"""


_ZhoneVoipServerRtcpEnabled_Object = MibTableColumn
zhoneVoipServerRtcpEnabled = _ZhoneVoipServerRtcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 9),
    _ZhoneVoipServerRtcpEnabled_Type()
)
zhoneVoipServerRtcpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerRtcpEnabled.setStatus("current")


class _ZhoneVoipServerRtcpPacketInterval_Type(Integer32):
    """Custom type zhoneVoipServerRtcpPacketInterval based on Integer32"""
    defaultValue = 5000


_ZhoneVoipServerRtcpPacketInterval_Object = MibTableColumn
zhoneVoipServerRtcpPacketInterval = _ZhoneVoipServerRtcpPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 10),
    _ZhoneVoipServerRtcpPacketInterval_Type()
)
zhoneVoipServerRtcpPacketInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerRtcpPacketInterval.setStatus("current")


class _ZhoneVoipServerInterDigitTimeout_Type(Integer32):
    """Custom type zhoneVoipServerInterDigitTimeout based on Integer32"""
    defaultValue = 10


_ZhoneVoipServerInterDigitTimeout_Object = MibTableColumn
zhoneVoipServerInterDigitTimeout = _ZhoneVoipServerInterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 11),
    _ZhoneVoipServerInterDigitTimeout_Type()
)
zhoneVoipServerInterDigitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerInterDigitTimeout.setStatus("current")


class _ZhoneVoipServerIpTos_Type(Integer32):
    """Custom type zhoneVoipServerIpTos based on Integer32"""
    defaultValue = 0


_ZhoneVoipServerIpTos_Object = MibTableColumn
zhoneVoipServerIpTos = _ZhoneVoipServerIpTos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 12),
    _ZhoneVoipServerIpTos_Type()
)
zhoneVoipServerIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerIpTos.setStatus("current")
_ZhoneVoipServerDomainName_Type = SnmpAdminString
_ZhoneVoipServerDomainName_Object = MibTableColumn
zhoneVoipServerDomainName = _ZhoneVoipServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 13),
    _ZhoneVoipServerDomainName_Type()
)
zhoneVoipServerDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerDomainName.setStatus("current")
_ZhoneVoipServerExpiresInvite_Type = Unsigned32
_ZhoneVoipServerExpiresInvite_Object = MibTableColumn
zhoneVoipServerExpiresInvite = _ZhoneVoipServerExpiresInvite_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 14),
    _ZhoneVoipServerExpiresInvite_Type()
)
zhoneVoipServerExpiresInvite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerExpiresInvite.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerExpiresInvite.setUnits("seconds")
_ZhoneVoipServerExpiresRegister_Type = Unsigned32
_ZhoneVoipServerExpiresRegister_Object = MibTableColumn
zhoneVoipServerExpiresRegister = _ZhoneVoipServerExpiresRegister_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 15),
    _ZhoneVoipServerExpiresRegister_Type()
)
zhoneVoipServerExpiresRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerExpiresRegister.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerExpiresRegister.setUnits("seconds")


class _ZhoneVoipServerHeaderMethod_Type(Bits):
    """Custom type zhoneVoipServerHeaderMethod based on Bits"""
    namedValues = NamedValues(
        *(("invite", 0),
          ("register", 1))
    )

_ZhoneVoipServerHeaderMethod_Type.__name__ = "Bits"
_ZhoneVoipServerHeaderMethod_Object = MibTableColumn
zhoneVoipServerHeaderMethod = _ZhoneVoipServerHeaderMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 16),
    _ZhoneVoipServerHeaderMethod_Type()
)
zhoneVoipServerHeaderMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerHeaderMethod.setStatus("current")


class _ZhoneVoipServerSessionTimer_Type(Integer32):
    """Custom type zhoneVoipServerSessionTimer based on Integer32"""
    defaultValue = 2

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


_ZhoneVoipServerSessionTimer_Type.__name__ = "Integer32"
_ZhoneVoipServerSessionTimer_Object = MibTableColumn
zhoneVoipServerSessionTimer = _ZhoneVoipServerSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 17),
    _ZhoneVoipServerSessionTimer_Type()
)
zhoneVoipServerSessionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionTimer.setStatus("current")


class _ZhoneVoipServerSessionExpiration_Type(Unsigned32):
    """Custom type zhoneVoipServerSessionExpiration based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 2147483647),
    )


_ZhoneVoipServerSessionExpiration_Type.__name__ = "Unsigned32"
_ZhoneVoipServerSessionExpiration_Object = MibTableColumn
zhoneVoipServerSessionExpiration = _ZhoneVoipServerSessionExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 18),
    _ZhoneVoipServerSessionExpiration_Type()
)
zhoneVoipServerSessionExpiration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionExpiration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionExpiration.setUnits("seconds")


class _ZhoneVoipServerSessionMinSE_Type(Unsigned32):
    """Custom type zhoneVoipServerSessionMinSE based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 2147483647),
    )


_ZhoneVoipServerSessionMinSE_Type.__name__ = "Unsigned32"
_ZhoneVoipServerSessionMinSE_Object = MibTableColumn
zhoneVoipServerSessionMinSE = _ZhoneVoipServerSessionMinSE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 19),
    _ZhoneVoipServerSessionMinSE_Type()
)
zhoneVoipServerSessionMinSE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionMinSE.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionMinSE.setUnits("seconds")


class _ZhoneVoipServerSessionCallerReqTimer_Type(Integer32):
    """Custom type zhoneVoipServerSessionCallerReqTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ZhoneVoipServerSessionCallerReqTimer_Type.__name__ = "Integer32"
_ZhoneVoipServerSessionCallerReqTimer_Object = MibTableColumn
zhoneVoipServerSessionCallerReqTimer = _ZhoneVoipServerSessionCallerReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 20),
    _ZhoneVoipServerSessionCallerReqTimer_Type()
)
zhoneVoipServerSessionCallerReqTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionCallerReqTimer.setStatus("current")


class _ZhoneVoipServerSessionCalleeReqTimer_Type(Integer32):
    """Custom type zhoneVoipServerSessionCalleeReqTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ZhoneVoipServerSessionCalleeReqTimer_Type.__name__ = "Integer32"
_ZhoneVoipServerSessionCalleeReqTimer_Object = MibTableColumn
zhoneVoipServerSessionCalleeReqTimer = _ZhoneVoipServerSessionCalleeReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 21),
    _ZhoneVoipServerSessionCalleeReqTimer_Type()
)
zhoneVoipServerSessionCalleeReqTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionCalleeReqTimer.setStatus("current")


class _ZhoneVoipServerSessionCallerSpecifyRefresher_Type(Integer32):
    """Custom type zhoneVoipServerSessionCallerSpecifyRefresher based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("omit", 3),
          ("uac", 1),
          ("uas", 2))
    )


_ZhoneVoipServerSessionCallerSpecifyRefresher_Type.__name__ = "Integer32"
_ZhoneVoipServerSessionCallerSpecifyRefresher_Object = MibTableColumn
zhoneVoipServerSessionCallerSpecifyRefresher = _ZhoneVoipServerSessionCallerSpecifyRefresher_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 22),
    _ZhoneVoipServerSessionCallerSpecifyRefresher_Type()
)
zhoneVoipServerSessionCallerSpecifyRefresher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionCallerSpecifyRefresher.setStatus("current")


class _ZhoneVoipServerSessionCalleeSpecifyRefresher_Type(Integer32):
    """Custom type zhoneVoipServerSessionCalleeSpecifyRefresher based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uac", 1),
          ("uas", 2))
    )


_ZhoneVoipServerSessionCalleeSpecifyRefresher_Type.__name__ = "Integer32"
_ZhoneVoipServerSessionCalleeSpecifyRefresher_Object = MibTableColumn
zhoneVoipServerSessionCalleeSpecifyRefresher = _ZhoneVoipServerSessionCalleeSpecifyRefresher_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 23),
    _ZhoneVoipServerSessionCalleeSpecifyRefresher_Type()
)
zhoneVoipServerSessionCalleeSpecifyRefresher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSessionCalleeSpecifyRefresher.setStatus("current")


class _ZhoneVoipServerDtmfMode_Type(Integer32):
    """Custom type zhoneVoipServerDtmfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("rfc2833", 2),
          ("rfc2833only", 3))
    )


_ZhoneVoipServerDtmfMode_Type.__name__ = "Integer32"
_ZhoneVoipServerDtmfMode_Object = MibTableColumn
zhoneVoipServerDtmfMode = _ZhoneVoipServerDtmfMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 24),
    _ZhoneVoipServerDtmfMode_Type()
)
zhoneVoipServerDtmfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerDtmfMode.setStatus("current")


class _ZhoneVoipServerBehaviorStringOne_Type(OctetString):
    """Custom type zhoneVoipServerBehaviorStringOne based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ZhoneVoipServerBehaviorStringOne_Type.__name__ = "OctetString"
_ZhoneVoipServerBehaviorStringOne_Object = MibTableColumn
zhoneVoipServerBehaviorStringOne = _ZhoneVoipServerBehaviorStringOne_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 25),
    _ZhoneVoipServerBehaviorStringOne_Type()
)
zhoneVoipServerBehaviorStringOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVoipServerBehaviorStringOne.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerBehaviorStringOne.setUnits("characters")


class _ZhoneVoipServerRtpTermIdSyntax_Type(OctetString):
    """Custom type zhoneVoipServerRtpTermIdSyntax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_ZhoneVoipServerRtpTermIdSyntax_Type.__name__ = "OctetString"
_ZhoneVoipServerRtpTermIdSyntax_Object = MibTableColumn
zhoneVoipServerRtpTermIdSyntax = _ZhoneVoipServerRtpTermIdSyntax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 26),
    _ZhoneVoipServerRtpTermIdSyntax_Type()
)
zhoneVoipServerRtpTermIdSyntax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipServerRtpTermIdSyntax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerRtpTermIdSyntax.setUnits("characters")


class _ZhoneVoipServerRtpDSCP_Type(OctetString):
    """Custom type zhoneVoipServerRtpDSCP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneVoipServerRtpDSCP_Type.__name__ = "OctetString"
_ZhoneVoipServerRtpDSCP_Object = MibTableColumn
zhoneVoipServerRtpDSCP = _ZhoneVoipServerRtpDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 27),
    _ZhoneVoipServerRtpDSCP_Type()
)
zhoneVoipServerRtpDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerRtpDSCP.setStatus("current")


class _ZhoneVoipServerSignalingDSCP_Type(OctetString):
    """Custom type zhoneVoipServerSignalingDSCP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneVoipServerSignalingDSCP_Type.__name__ = "OctetString"
_ZhoneVoipServerSignalingDSCP_Object = MibTableColumn
zhoneVoipServerSignalingDSCP = _ZhoneVoipServerSignalingDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 28),
    _ZhoneVoipServerSignalingDSCP_Type()
)
zhoneVoipServerSignalingDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerSignalingDSCP.setStatus("current")


class _ZhoneVoipServerDtmfPayloadId_Type(Integer32):
    """Custom type zhoneVoipServerDtmfPayloadId based on Integer32"""
    defaultValue = 101

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_ZhoneVoipServerDtmfPayloadId_Type.__name__ = "Integer32"
_ZhoneVoipServerDtmfPayloadId_Object = MibTableColumn
zhoneVoipServerDtmfPayloadId = _ZhoneVoipServerDtmfPayloadId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 29),
    _ZhoneVoipServerDtmfPayloadId_Type()
)
zhoneVoipServerDtmfPayloadId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVoipServerDtmfPayloadId.setStatus("current")


class _ZhoneVoipServerRegisterReadyTimeout_Type(Unsigned32):
    """Custom type zhoneVoipServerRegisterReadyTimeout based on Unsigned32"""
    defaultValue = 10


_ZhoneVoipServerRegisterReadyTimeout_Object = MibTableColumn
zhoneVoipServerRegisterReadyTimeout = _ZhoneVoipServerRegisterReadyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 30),
    _ZhoneVoipServerRegisterReadyTimeout_Type()
)
zhoneVoipServerRegisterReadyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerRegisterReadyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVoipServerRegisterReadyTimeout.setUnits("seconds")


class _ZhoneVoipServerMessageRetryCount_Type(Integer32):
    """Custom type zhoneVoipServerMessageRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneVoipServerMessageRetryCount_Type.__name__ = "Integer32"
_ZhoneVoipServerMessageRetryCount_Object = MibTableColumn
zhoneVoipServerMessageRetryCount = _ZhoneVoipServerMessageRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 31),
    _ZhoneVoipServerMessageRetryCount_Type()
)
zhoneVoipServerMessageRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerMessageRetryCount.setStatus("current")


class _ZhoneVoipServerFeatures_Type(Bits):
    """Custom type zhoneVoipServerFeatures based on Bits"""
    namedValues = NamedValues(
        *(("gruu", 1),
          ("sip-outbound", 0))
    )

_ZhoneVoipServerFeatures_Type.__name__ = "Bits"
_ZhoneVoipServerFeatures_Object = MibTableColumn
zhoneVoipServerFeatures = _ZhoneVoipServerFeatures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 32),
    _ZhoneVoipServerFeatures_Type()
)
zhoneVoipServerFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerFeatures.setStatus("current")


class _ZhoneVoipServerTransportProtocol_Type(Integer32):
    """Custom type zhoneVoipServerTransportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_ZhoneVoipServerTransportProtocol_Type.__name__ = "Integer32"
_ZhoneVoipServerTransportProtocol_Object = MibTableColumn
zhoneVoipServerTransportProtocol = _ZhoneVoipServerTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 33),
    _ZhoneVoipServerTransportProtocol_Type()
)
zhoneVoipServerTransportProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipServerTransportProtocol.setStatus("current")


class _ZhoneVoipSigLocalPortNumber_Type(Integer32):
    """Custom type zhoneVoipSigLocalPortNumber based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneVoipSigLocalPortNumber_Type.__name__ = "Integer32"
_ZhoneVoipSigLocalPortNumber_Object = MibTableColumn
zhoneVoipSigLocalPortNumber = _ZhoneVoipSigLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 6, 1, 1, 34),
    _ZhoneVoipSigLocalPortNumber_Type()
)
zhoneVoipSigLocalPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVoipSigLocalPortNumber.setStatus("current")

# Managed Objects groups

zhoneVoipObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 4, 2)
)
zhoneVoipObjects.setObjects(
      *(("ZHONE-COM-VOIP-MIB", "nextVoipSipDialPlanId"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialString"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialIpAddr"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialPlanRowStatus"),
        ("ZHONE-COM-VOIP-MIB", "nextZhoneVoipHuntGroupId"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipHuntGroupDestUri"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipHuntGroupRowStatus"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialPrefixAdd"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialPrefixStrip"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialNumOfDigits"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialDestName"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipHuntGroupPortMembers"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipHuntGroupDefaultCodec"),
        ("ZHONE-COM-VOIP-MIB", "nextVoipMaliciousCallerId"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipMaliciousCallerUri"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerId"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerUdpPortNumber"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerAddr"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerAddrType"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerRowStatus"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipSipDialPlanType"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionTimer"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionExpiration"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionMinSE"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionCallerReqTimer"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionCalleeReqTimer"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionCallerSpecifyRefresher"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerSessionCalleeSpecifyRefresher"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerExpiresInvite"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerExpiresRegister"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerHeaderMethod"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipMaliciousCallerRowStatus"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipMaliciousCallerEnable"),
        ("ZHONE-COM-VOIP-MIB", "zhoneVoipServerBehaviorStringOne"))
)
if mibBuilder.loadTexts:
    zhoneVoipObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-VOIP-MIB",
    **{"zhoneVoip": zhoneVoip,
       "zhoneVoipSystem": zhoneVoipSystem,
       "zhoneVoipSystemProtocol": zhoneVoipSystemProtocol,
       "zhoneVoipSystemSendCallProceedingTone": zhoneVoipSystemSendCallProceedingTone,
       "zhoneVoipSystemRtcpEnabled": zhoneVoipSystemRtcpEnabled,
       "zhoneVoipSystemRtcpPacketInterval": zhoneVoipSystemRtcpPacketInterval,
       "zhoneVoipSystemInterdigitTimeout": zhoneVoipSystemInterdigitTimeout,
       "zhoneVoipSystemIpTos": zhoneVoipSystemIpTos,
       "zhoneVoipSystemDomainName": zhoneVoipSystemDomainName,
       "zhoneVoipObjects": zhoneVoipObjects,
       "zhoneVoipSipDialPlan": zhoneVoipSipDialPlan,
       "nextVoipSipDialPlanId": nextVoipSipDialPlanId,
       "zhoneVoipSipDialPlanTable": zhoneVoipSipDialPlanTable,
       "zhoneVoipSipDialPlanEntry": zhoneVoipSipDialPlanEntry,
       "zhoneVoipSipDialPlanId": zhoneVoipSipDialPlanId,
       "zhoneVoipSipDialString": zhoneVoipSipDialString,
       "zhoneVoipSipDialIpAddr": zhoneVoipSipDialIpAddr,
       "zhoneVoipSipDialPlanRowStatus": zhoneVoipSipDialPlanRowStatus,
       "zhoneVoipSipDialDestName": zhoneVoipSipDialDestName,
       "zhoneVoipSipDialNumOfDigits": zhoneVoipSipDialNumOfDigits,
       "zhoneVoipSipDialPrefixStrip": zhoneVoipSipDialPrefixStrip,
       "zhoneVoipSipDialPrefixAdd": zhoneVoipSipDialPrefixAdd,
       "zhoneVoipSipDialPlanType": zhoneVoipSipDialPlanType,
       "zhoneVoipServerEntryIndex": zhoneVoipServerEntryIndex,
       "zhoneVoipOverrideInterdigitTimeout": zhoneVoipOverrideInterdigitTimeout,
       "zhoneVoipSipDialPlanClass": zhoneVoipSipDialPlanClass,
       "zhoneVoipSipDialPlanDescription": zhoneVoipSipDialPlanDescription,
       "zhoneVoipHuntGroup": zhoneVoipHuntGroup,
       "nextZhoneVoipHuntGroupId": nextZhoneVoipHuntGroupId,
       "zhoneVoipHuntGroupTable": zhoneVoipHuntGroupTable,
       "zhoneVoipHuntGroupEntry": zhoneVoipHuntGroupEntry,
       "zhoneVoipHuntGroupId": zhoneVoipHuntGroupId,
       "zhoneVoipHuntGroupDestUri": zhoneVoipHuntGroupDestUri,
       "zhoneVoipHuntGroupDefaultCodec": zhoneVoipHuntGroupDefaultCodec,
       "zhoneVoipHuntGroupPortMembers": zhoneVoipHuntGroupPortMembers,
       "zhoneVoipHuntGroupRowStatus": zhoneVoipHuntGroupRowStatus,
       "zhoneVoipMaliciousCaller": zhoneVoipMaliciousCaller,
       "nextVoipMaliciousCallerId": nextVoipMaliciousCallerId,
       "zhoneVoipMaliciousCallerTable": zhoneVoipMaliciousCallerTable,
       "zhoneVoipMaliciousCallerEntry": zhoneVoipMaliciousCallerEntry,
       "zhoneVoipMaliciousCallerId": zhoneVoipMaliciousCallerId,
       "zhoneVoipMaliciousCallerUri": zhoneVoipMaliciousCallerUri,
       "zhoneVoipMaliciousCallerEnable": zhoneVoipMaliciousCallerEnable,
       "zhoneVoipMaliciousCallerRowStatus": zhoneVoipMaliciousCallerRowStatus,
       "zhoneVoipServerCfg": zhoneVoipServerCfg,
       "zhoneVoipServerTable": zhoneVoipServerTable,
       "zhoneVoipServerEntry": zhoneVoipServerEntry,
       "zhoneVoipServerAddressIndex": zhoneVoipServerAddressIndex,
       "zhoneVoipServerRowStatus": zhoneVoipServerRowStatus,
       "zhoneVoipServerAddrType": zhoneVoipServerAddrType,
       "zhoneVoipServerAddr": zhoneVoipServerAddr,
       "zhoneVoipServerUdpPortNumber": zhoneVoipServerUdpPortNumber,
       "zhoneVoipServerId": zhoneVoipServerId,
       "zhoneVoipServerProtocol": zhoneVoipServerProtocol,
       "zhoneVoipServerSendCallProceedingTone": zhoneVoipServerSendCallProceedingTone,
       "zhoneVoipServerRtcpEnabled": zhoneVoipServerRtcpEnabled,
       "zhoneVoipServerRtcpPacketInterval": zhoneVoipServerRtcpPacketInterval,
       "zhoneVoipServerInterDigitTimeout": zhoneVoipServerInterDigitTimeout,
       "zhoneVoipServerIpTos": zhoneVoipServerIpTos,
       "zhoneVoipServerDomainName": zhoneVoipServerDomainName,
       "zhoneVoipServerExpiresInvite": zhoneVoipServerExpiresInvite,
       "zhoneVoipServerExpiresRegister": zhoneVoipServerExpiresRegister,
       "zhoneVoipServerHeaderMethod": zhoneVoipServerHeaderMethod,
       "zhoneVoipServerSessionTimer": zhoneVoipServerSessionTimer,
       "zhoneVoipServerSessionExpiration": zhoneVoipServerSessionExpiration,
       "zhoneVoipServerSessionMinSE": zhoneVoipServerSessionMinSE,
       "zhoneVoipServerSessionCallerReqTimer": zhoneVoipServerSessionCallerReqTimer,
       "zhoneVoipServerSessionCalleeReqTimer": zhoneVoipServerSessionCalleeReqTimer,
       "zhoneVoipServerSessionCallerSpecifyRefresher": zhoneVoipServerSessionCallerSpecifyRefresher,
       "zhoneVoipServerSessionCalleeSpecifyRefresher": zhoneVoipServerSessionCalleeSpecifyRefresher,
       "zhoneVoipServerDtmfMode": zhoneVoipServerDtmfMode,
       "zhoneVoipServerBehaviorStringOne": zhoneVoipServerBehaviorStringOne,
       "zhoneVoipServerRtpTermIdSyntax": zhoneVoipServerRtpTermIdSyntax,
       "zhoneVoipServerRtpDSCP": zhoneVoipServerRtpDSCP,
       "zhoneVoipServerSignalingDSCP": zhoneVoipServerSignalingDSCP,
       "zhoneVoipServerDtmfPayloadId": zhoneVoipServerDtmfPayloadId,
       "zhoneVoipServerRegisterReadyTimeout": zhoneVoipServerRegisterReadyTimeout,
       "zhoneVoipServerMessageRetryCount": zhoneVoipServerMessageRetryCount,
       "zhoneVoipServerFeatures": zhoneVoipServerFeatures,
       "zhoneVoipServerTransportProtocol": zhoneVoipServerTransportProtocol,
       "zhoneVoipSigLocalPortNumber": zhoneVoipSigLocalPortNumber}
)
