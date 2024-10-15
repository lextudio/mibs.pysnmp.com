# SNMP MIB module (BASP-Config-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASP-Config-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:45 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadcom_ObjectIdentity = ObjectIdentity
broadcom = _Broadcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413)
)
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1)
)
_Basp_ObjectIdentity = ObjectIdentity
basp = _Basp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2)
)
_BaspConfig_ObjectIdentity = ObjectIdentity
baspConfig = _BaspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1)
)
_BaspTeam_ObjectIdentity = ObjectIdentity
baspTeam = _BaspTeam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1)
)
_BtTeamNumber_Type = Integer32
_BtTeamNumber_Object = MibScalar
btTeamNumber = _BtTeamNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 1),
    _BtTeamNumber_Type()
)
btTeamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btTeamNumber.setStatus("mandatory")
_BtTeamTable_Object = MibTable
btTeamTable = _BtTeamTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    btTeamTable.setStatus("mandatory")
_BtTeamEntry_Object = MibTableRow
btTeamEntry = _BtTeamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1)
)
btTeamEntry.setIndexNames(
    (0, "BASP-Config-MIB", "btTeamIndex"),
)
if mibBuilder.loadTexts:
    btTeamEntry.setStatus("mandatory")


class _BtTeamIndex_Type(Integer32):
    """Custom type btTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtTeamIndex_Type.__name__ = "Integer32"
_BtTeamIndex_Object = MibTableColumn
btTeamIndex = _BtTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 1),
    _BtTeamIndex_Type()
)
btTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btTeamIndex.setStatus("mandatory")
_BtTeamName_Type = DisplayString
_BtTeamName_Object = MibTableColumn
btTeamName = _BtTeamName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 2),
    _BtTeamName_Type()
)
btTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btTeamName.setStatus("mandatory")


class _BtTeamType_Type(Integer32):
    """Custom type btTeamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              104)
        )
    )
    namedValues = NamedValues(
        *(("team-802-3-AD", 102),
          ("team-FEC-GEC", 101),
          ("team-SLB", 100),
          ("team-SLB-AFD", 104))
    )


_BtTeamType_Type.__name__ = "Integer32"
_BtTeamType_Object = MibTableColumn
btTeamType = _BtTeamType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 3),
    _BtTeamType_Type()
)
btTeamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btTeamType.setStatus("mandatory")
_BtTeamMacAddress_Type = PhysAddress
_BtTeamMacAddress_Object = MibTableColumn
btTeamMacAddress = _BtTeamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 4),
    _BtTeamMacAddress_Type()
)
btTeamMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btTeamMacAddress.setStatus("mandatory")
_BtPhyNumber_Type = Integer32
_BtPhyNumber_Object = MibTableColumn
btPhyNumber = _BtPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 5),
    _BtPhyNumber_Type()
)
btPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btPhyNumber.setStatus("mandatory")
_BtVirNumber_Type = Integer32
_BtVirNumber_Object = MibTableColumn
btVirNumber = _BtVirNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 6),
    _BtVirNumber_Type()
)
btVirNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btVirNumber.setStatus("mandatory")


class _BtMode_Type(Integer32):
    """Custom type btMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryMode", 1),
          ("standby", 2))
    )


_BtMode_Type.__name__ = "Integer32"
_BtMode_Object = MibTableColumn
btMode = _BtMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 7),
    _BtMode_Type()
)
btMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btMode.setStatus("mandatory")


class _BtLiveLinkEnable_Type(Integer32):
    """Custom type btLiveLinkEnable based on Integer32"""
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


_BtLiveLinkEnable_Type.__name__ = "Integer32"
_BtLiveLinkEnable_Object = MibTableColumn
btLiveLinkEnable = _BtLiveLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 8),
    _BtLiveLinkEnable_Type()
)
btLiveLinkEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLiveLinkEnable.setStatus("mandatory")
_BtLinkPacketFrequency_Type = Integer32
_BtLinkPacketFrequency_Object = MibTableColumn
btLinkPacketFrequency = _BtLinkPacketFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 9),
    _BtLinkPacketFrequency_Type()
)
btLinkPacketFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkPacketFrequency.setStatus("mandatory")
_BtLinkMaxRetry_Type = Integer32
_BtLinkMaxRetry_Object = MibTableColumn
btLinkMaxRetry = _BtLinkMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 10),
    _BtLinkMaxRetry_Type()
)
btLinkMaxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkMaxRetry.setStatus("mandatory")
_BtLinkRetryFrequency_Type = Integer32
_BtLinkRetryFrequency_Object = MibTableColumn
btLinkRetryFrequency = _BtLinkRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 11),
    _BtLinkRetryFrequency_Type()
)
btLinkRetryFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkRetryFrequency.setStatus("mandatory")
_BtLinkTargetIpAddress1_Type = IpAddress
_BtLinkTargetIpAddress1_Object = MibTableColumn
btLinkTargetIpAddress1 = _BtLinkTargetIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 12),
    _BtLinkTargetIpAddress1_Type()
)
btLinkTargetIpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkTargetIpAddress1.setStatus("mandatory")
_BtLinkTargetIpAddress2_Type = IpAddress
_BtLinkTargetIpAddress2_Object = MibTableColumn
btLinkTargetIpAddress2 = _BtLinkTargetIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 13),
    _BtLinkTargetIpAddress2_Type()
)
btLinkTargetIpAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkTargetIpAddress2.setStatus("mandatory")
_BtLinkTargetIpAddress3_Type = IpAddress
_BtLinkTargetIpAddress3_Object = MibTableColumn
btLinkTargetIpAddress3 = _BtLinkTargetIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 14),
    _BtLinkTargetIpAddress3_Type()
)
btLinkTargetIpAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkTargetIpAddress3.setStatus("mandatory")
_BtLinkTargetIpAddress4_Type = IpAddress
_BtLinkTargetIpAddress4_Object = MibTableColumn
btLinkTargetIpAddress4 = _BtLinkTargetIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 1, 2, 1, 15),
    _BtLinkTargetIpAddress4_Type()
)
btLinkTargetIpAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btLinkTargetIpAddress4.setStatus("mandatory")
_BaspPhyAdapter_ObjectIdentity = ObjectIdentity
baspPhyAdapter = _BaspPhyAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2)
)
_BtPhyAdapterNumber_Type = Integer32
_BtPhyAdapterNumber_Object = MibScalar
btPhyAdapterNumber = _BtPhyAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 1),
    _BtPhyAdapterNumber_Type()
)
btPhyAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btPhyAdapterNumber.setStatus("mandatory")
_BtPhyAdapterTable_Object = MibTable
btPhyAdapterTable = _BtPhyAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    btPhyAdapterTable.setStatus("mandatory")
_BtPhyAdapterEntry_Object = MibTableRow
btPhyAdapterEntry = _BtPhyAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1)
)
btPhyAdapterEntry.setIndexNames(
    (0, "BASP-Config-MIB", "btpTeamIndex"),
    (0, "BASP-Config-MIB", "btpAdapterIndex"),
)
if mibBuilder.loadTexts:
    btPhyAdapterEntry.setStatus("mandatory")


class _BtpTeamIndex_Type(Integer32):
    """Custom type btpTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtpTeamIndex_Type.__name__ = "Integer32"
_BtpTeamIndex_Object = MibTableColumn
btpTeamIndex = _BtpTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 1),
    _BtpTeamIndex_Type()
)
btpTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btpTeamIndex.setStatus("mandatory")


class _BtpAdapterIndex_Type(Integer32):
    """Custom type btpAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtpAdapterIndex_Type.__name__ = "Integer32"
_BtpAdapterIndex_Object = MibTableColumn
btpAdapterIndex = _BtpAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 2),
    _BtpAdapterIndex_Type()
)
btpAdapterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btpAdapterIndex.setStatus("mandatory")
_BtpAdapterDesc_Type = DisplayString
_BtpAdapterDesc_Object = MibTableColumn
btpAdapterDesc = _BtpAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 3),
    _BtpAdapterDesc_Type()
)
btpAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpAdapterDesc.setStatus("mandatory")


class _BtpMemberType_Type(Integer32):
    """Custom type btpMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("load-balance", 100),
          ("standby", 101))
    )


_BtpMemberType_Type.__name__ = "Integer32"
_BtpMemberType_Object = MibTableColumn
btpMemberType = _BtpMemberType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 4),
    _BtpMemberType_Type()
)
btpMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpMemberType.setStatus("mandatory")
_BtpMacAddress_Type = PhysAddress
_BtpMacAddress_Object = MibTableColumn
btpMacAddress = _BtpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 5),
    _BtpMacAddress_Type()
)
btpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpMacAddress.setStatus("mandatory")


class _BtpMemberState_Type(Integer32):
    """Custom type btpMemberState based on Integer32"""
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
        *(("disable-not-join-traffic", 3),
          ("join-traffic", 4),
          ("link-up-not-join-traffic", 2),
          ("unknown", 1))
    )


_BtpMemberState_Type.__name__ = "Integer32"
_BtpMemberState_Object = MibTableColumn
btpMemberState = _BtpMemberState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 6),
    _BtpMemberState_Type()
)
btpMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpMemberState.setStatus("mandatory")
_BtpLiveLinkIp_Type = IpAddress
_BtpLiveLinkIp_Object = MibTableColumn
btpLiveLinkIp = _BtpLiveLinkIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 2, 2, 1, 7),
    _BtpLiveLinkIp_Type()
)
btpLiveLinkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpLiveLinkIp.setStatus("mandatory")
_BaspVirAdapter_ObjectIdentity = ObjectIdentity
baspVirAdapter = _BaspVirAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3)
)
_BtVirAdapterNumber_Type = Integer32
_BtVirAdapterNumber_Object = MibScalar
btVirAdapterNumber = _BtVirAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 1),
    _BtVirAdapterNumber_Type()
)
btVirAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btVirAdapterNumber.setStatus("mandatory")
_BtVirAdapterTable_Object = MibTable
btVirAdapterTable = _BtVirAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    btVirAdapterTable.setStatus("mandatory")
_BtVirAdapterEntry_Object = MibTableRow
btVirAdapterEntry = _BtVirAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1)
)
btVirAdapterEntry.setIndexNames(
    (0, "BASP-Config-MIB", "btvTeamIndex"),
    (0, "BASP-Config-MIB", "btvAdapterIndex"),
)
if mibBuilder.loadTexts:
    btVirAdapterEntry.setStatus("mandatory")


class _BtvTeamIndex_Type(Integer32):
    """Custom type btvTeamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtvTeamIndex_Type.__name__ = "Integer32"
_BtvTeamIndex_Object = MibTableColumn
btvTeamIndex = _BtvTeamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 1),
    _BtvTeamIndex_Type()
)
btvTeamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btvTeamIndex.setStatus("mandatory")


class _BtvAdapterIndex_Type(Integer32):
    """Custom type btvAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtvAdapterIndex_Type.__name__ = "Integer32"
_BtvAdapterIndex_Object = MibTableColumn
btvAdapterIndex = _BtvAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 2),
    _BtvAdapterIndex_Type()
)
btvAdapterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btvAdapterIndex.setStatus("mandatory")
_BtvAdapterDesc_Type = DisplayString
_BtvAdapterDesc_Object = MibTableColumn
btvAdapterDesc = _BtvAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 3),
    _BtvAdapterDesc_Type()
)
btvAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvAdapterDesc.setStatus("mandatory")
_BtvVlanId_Type = Integer32
_BtvVlanId_Object = MibTableColumn
btvVlanId = _BtvVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 4),
    _BtvVlanId_Type()
)
btvVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvVlanId.setStatus("mandatory")


class _BtvLinkStatus_Type(Integer32):
    """Custom type btvLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 2),
          ("link-up", 1))
    )


_BtvLinkStatus_Type.__name__ = "Integer32"
_BtvLinkStatus_Object = MibTableColumn
btvLinkStatus = _BtvLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 5),
    _BtvLinkStatus_Type()
)
btvLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvLinkStatus.setStatus("mandatory")
_BtvIPAddress_Type = IpAddress
_BtvIPAddress_Object = MibTableColumn
btvIPAddress = _BtvIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 6),
    _BtvIPAddress_Type()
)
btvIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvIPAddress.setStatus("mandatory")
_BtvSubnetMask_Type = IpAddress
_BtvSubnetMask_Object = MibTableColumn
btvSubnetMask = _BtvSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 7),
    _BtvSubnetMask_Type()
)
btvSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvSubnetMask.setStatus("mandatory")
_BtvPhysAddress_Type = PhysAddress
_BtvPhysAddress_Object = MibTableColumn
btvPhysAddress = _BtvPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 8),
    _BtvPhysAddress_Type()
)
btvPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvPhysAddress.setStatus("mandatory")
_BtvLineSpeed_Type = DisplayString
_BtvLineSpeed_Object = MibTableColumn
btvLineSpeed = _BtvLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1, 3, 2, 1, 9),
    _BtvLineSpeed_Type()
)
btvLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btvLineSpeed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASP-Config-MIB",
    **{"broadcom": broadcom,
       "enet": enet,
       "basp": basp,
       "baspConfig": baspConfig,
       "baspTeam": baspTeam,
       "btTeamNumber": btTeamNumber,
       "btTeamTable": btTeamTable,
       "btTeamEntry": btTeamEntry,
       "btTeamIndex": btTeamIndex,
       "btTeamName": btTeamName,
       "btTeamType": btTeamType,
       "btTeamMacAddress": btTeamMacAddress,
       "btPhyNumber": btPhyNumber,
       "btVirNumber": btVirNumber,
       "btMode": btMode,
       "btLiveLinkEnable": btLiveLinkEnable,
       "btLinkPacketFrequency": btLinkPacketFrequency,
       "btLinkMaxRetry": btLinkMaxRetry,
       "btLinkRetryFrequency": btLinkRetryFrequency,
       "btLinkTargetIpAddress1": btLinkTargetIpAddress1,
       "btLinkTargetIpAddress2": btLinkTargetIpAddress2,
       "btLinkTargetIpAddress3": btLinkTargetIpAddress3,
       "btLinkTargetIpAddress4": btLinkTargetIpAddress4,
       "baspPhyAdapter": baspPhyAdapter,
       "btPhyAdapterNumber": btPhyAdapterNumber,
       "btPhyAdapterTable": btPhyAdapterTable,
       "btPhyAdapterEntry": btPhyAdapterEntry,
       "btpTeamIndex": btpTeamIndex,
       "btpAdapterIndex": btpAdapterIndex,
       "btpAdapterDesc": btpAdapterDesc,
       "btpMemberType": btpMemberType,
       "btpMacAddress": btpMacAddress,
       "btpMemberState": btpMemberState,
       "btpLiveLinkIp": btpLiveLinkIp,
       "baspVirAdapter": baspVirAdapter,
       "btVirAdapterNumber": btVirAdapterNumber,
       "btVirAdapterTable": btVirAdapterTable,
       "btVirAdapterEntry": btVirAdapterEntry,
       "btvTeamIndex": btvTeamIndex,
       "btvAdapterIndex": btvAdapterIndex,
       "btvAdapterDesc": btvAdapterDesc,
       "btvVlanId": btvVlanId,
       "btvLinkStatus": btvLinkStatus,
       "btvIPAddress": btvIPAddress,
       "btvSubnetMask": btvSubnetMask,
       "btvPhysAddress": btvPhysAddress,
       "btvLineSpeed": btvLineSpeed}
)
