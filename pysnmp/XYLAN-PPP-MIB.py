# SNMP MIB module (XYLAN-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:12 2024
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

(xylanPppArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPppArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppxConfigGroup_ObjectIdentity = ObjectIdentity
pppxConfigGroup = _PppxConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1)
)
_PppxConfigTable_Object = MibTable
pppxConfigTable = _PppxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    pppxConfigTable.setStatus("mandatory")
_PppxConfigEntry_Object = MibTableRow
pppxConfigEntry = _PppxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1)
)
pppxConfigEntry.setIndexNames(
    (0, "XYLAN-PPP-MIB", "pppxConfigPeerID"),
)
if mibBuilder.loadTexts:
    pppxConfigEntry.setStatus("mandatory")
_PppxConfigPeerID_Type = Integer32
_PppxConfigPeerID_Object = MibTableColumn
pppxConfigPeerID = _PppxConfigPeerID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 1),
    _PppxConfigPeerID_Type()
)
pppxConfigPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxConfigPeerID.setStatus("mandatory")


class _PppxConfigDescription_Type(DisplayString):
    """Custom type pppxConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxConfigDescription_Type.__name__ = "DisplayString"
_PppxConfigDescription_Object = MibTableColumn
pppxConfigDescription = _PppxConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 2),
    _PppxConfigDescription_Type()
)
pppxConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigDescription.setStatus("mandatory")


class _PppxConfigAdminStatus_Type(Integer32):
    """Custom type pppxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_PppxConfigAdminStatus_Type.__name__ = "Integer32"
_PppxConfigAdminStatus_Object = MibTableColumn
pppxConfigAdminStatus = _PppxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 3),
    _PppxConfigAdminStatus_Type()
)
pppxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigAdminStatus.setStatus("mandatory")


class _PppxConfigMode_Type(Integer32):
    """Custom type pppxConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multilink", 2),
          ("normal", 1))
    )


_PppxConfigMode_Type.__name__ = "Integer32"
_PppxConfigMode_Object = MibTableColumn
pppxConfigMode = _PppxConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 4),
    _PppxConfigMode_Type()
)
pppxConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigMode.setStatus("mandatory")


class _PppxConfigBridgingVLAN_Type(Integer32):
    """Custom type pppxConfigBridgingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PppxConfigBridgingVLAN_Type.__name__ = "Integer32"
_PppxConfigBridgingVLAN_Object = MibTableColumn
pppxConfigBridgingVLAN = _PppxConfigBridgingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 5),
    _PppxConfigBridgingVLAN_Type()
)
pppxConfigBridgingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigBridgingVLAN.setStatus("mandatory")


class _PppxConfigRoutingVLAN_Type(Integer32):
    """Custom type pppxConfigRoutingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PppxConfigRoutingVLAN_Type.__name__ = "Integer32"
_PppxConfigRoutingVLAN_Object = MibTableColumn
pppxConfigRoutingVLAN = _PppxConfigRoutingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 6),
    _PppxConfigRoutingVLAN_Type()
)
pppxConfigRoutingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigRoutingVLAN.setStatus("mandatory")


class _PppxConfigCompressionType_Type(Integer32):
    """Custom type pppxConfigCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lzsDcp", 2),
          ("none", 1))
    )


_PppxConfigCompressionType_Type.__name__ = "Integer32"
_PppxConfigCompressionType_Object = MibTableColumn
pppxConfigCompressionType = _PppxConfigCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 7),
    _PppxConfigCompressionType_Type()
)
pppxConfigCompressionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigCompressionType.setStatus("mandatory")


class _PppxConfigBridgingMode_Type(Integer32):
    """Custom type pppxConfigBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PppxConfigBridgingMode_Type.__name__ = "Integer32"
_PppxConfigBridgingMode_Object = MibTableColumn
pppxConfigBridgingMode = _PppxConfigBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 8),
    _PppxConfigBridgingMode_Type()
)
pppxConfigBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigBridgingMode.setStatus("mandatory")


class _PppxConfigIpConfigAdminStatus_Type(Integer32):
    """Custom type pppxConfigIpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxConfigIpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxConfigIpConfigAdminStatus_Object = MibTableColumn
pppxConfigIpConfigAdminStatus = _PppxConfigIpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 9),
    _PppxConfigIpConfigAdminStatus_Type()
)
pppxConfigIpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigIpConfigAdminStatus.setStatus("mandatory")


class _PppxConfigBcpConfigAdminStatus_Type(Integer32):
    """Custom type pppxConfigBcpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxConfigBcpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxConfigBcpConfigAdminStatus_Object = MibTableColumn
pppxConfigBcpConfigAdminStatus = _PppxConfigBcpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 10),
    _PppxConfigBcpConfigAdminStatus_Type()
)
pppxConfigBcpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigBcpConfigAdminStatus.setStatus("mandatory")


class _PppxConfigIpxConfigAdminStatus_Type(Integer32):
    """Custom type pppxConfigIpxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxConfigIpxConfigAdminStatus_Type.__name__ = "Integer32"
_PppxConfigIpxConfigAdminStatus_Object = MibTableColumn
pppxConfigIpxConfigAdminStatus = _PppxConfigIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 11),
    _PppxConfigIpxConfigAdminStatus_Type()
)
pppxConfigIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigIpxConfigAdminStatus.setStatus("mandatory")


class _PppxConfigCcpConfigAdminStatus_Type(Integer32):
    """Custom type pppxConfigCcpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxConfigCcpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxConfigCcpConfigAdminStatus_Object = MibTableColumn
pppxConfigCcpConfigAdminStatus = _PppxConfigCcpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 12),
    _PppxConfigCcpConfigAdminStatus_Type()
)
pppxConfigCcpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigCcpConfigAdminStatus.setStatus("mandatory")
_PppxConfigRemoteIpAddress_Type = IpAddress
_PppxConfigRemoteIpAddress_Object = MibTableColumn
pppxConfigRemoteIpAddress = _PppxConfigRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 13),
    _PppxConfigRemoteIpAddress_Type()
)
pppxConfigRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigRemoteIpAddress.setStatus("mandatory")


class _PppxConfigAuthenticationType_Type(Integer32):
    """Custom type pppxConfigAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_PppxConfigAuthenticationType_Type.__name__ = "Integer32"
_PppxConfigAuthenticationType_Object = MibTableColumn
pppxConfigAuthenticationType = _PppxConfigAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 14),
    _PppxConfigAuthenticationType_Type()
)
pppxConfigAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigAuthenticationType.setStatus("mandatory")


class _PppxConfigUserIdToRemote_Type(DisplayString):
    """Custom type pppxConfigUserIdToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxConfigUserIdToRemote_Type.__name__ = "DisplayString"
_PppxConfigUserIdToRemote_Object = MibTableColumn
pppxConfigUserIdToRemote = _PppxConfigUserIdToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 15),
    _PppxConfigUserIdToRemote_Type()
)
pppxConfigUserIdToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigUserIdToRemote.setStatus("mandatory")


class _PppxConfigPasswordToRemote_Type(DisplayString):
    """Custom type pppxConfigPasswordToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxConfigPasswordToRemote_Type.__name__ = "DisplayString"
_PppxConfigPasswordToRemote_Object = MibTableColumn
pppxConfigPasswordToRemote = _PppxConfigPasswordToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 16),
    _PppxConfigPasswordToRemote_Type()
)
pppxConfigPasswordToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigPasswordToRemote.setStatus("mandatory")


class _PppxConfigUserIdFromRemote_Type(DisplayString):
    """Custom type pppxConfigUserIdFromRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxConfigUserIdFromRemote_Type.__name__ = "DisplayString"
_PppxConfigUserIdFromRemote_Object = MibTableColumn
pppxConfigUserIdFromRemote = _PppxConfigUserIdFromRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 17),
    _PppxConfigUserIdFromRemote_Type()
)
pppxConfigUserIdFromRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigUserIdFromRemote.setStatus("mandatory")


class _PppxConfigPasswordFromRemote_Type(DisplayString):
    """Custom type pppxConfigPasswordFromRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxConfigPasswordFromRemote_Type.__name__ = "DisplayString"
_PppxConfigPasswordFromRemote_Object = MibTableColumn
pppxConfigPasswordFromRemote = _PppxConfigPasswordFromRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 18),
    _PppxConfigPasswordFromRemote_Type()
)
pppxConfigPasswordFromRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigPasswordFromRemote.setStatus("mandatory")


class _PppxConfigMaxFailureCount_Type(Integer32):
    """Custom type pppxConfigMaxFailureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppxConfigMaxFailureCount_Type.__name__ = "Integer32"
_PppxConfigMaxFailureCount_Object = MibTableColumn
pppxConfigMaxFailureCount = _PppxConfigMaxFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 19),
    _PppxConfigMaxFailureCount_Type()
)
pppxConfigMaxFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigMaxFailureCount.setStatus("mandatory")


class _PppxConfigMaxConfigureCount_Type(Integer32):
    """Custom type pppxConfigMaxConfigureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppxConfigMaxConfigureCount_Type.__name__ = "Integer32"
_PppxConfigMaxConfigureCount_Object = MibTableColumn
pppxConfigMaxConfigureCount = _PppxConfigMaxConfigureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 20),
    _PppxConfigMaxConfigureCount_Type()
)
pppxConfigMaxConfigureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigMaxConfigureCount.setStatus("mandatory")


class _PppxConfigMaxTerminateCount_Type(Integer32):
    """Custom type pppxConfigMaxTerminateCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppxConfigMaxTerminateCount_Type.__name__ = "Integer32"
_PppxConfigMaxTerminateCount_Object = MibTableColumn
pppxConfigMaxTerminateCount = _PppxConfigMaxTerminateCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 21),
    _PppxConfigMaxTerminateCount_Type()
)
pppxConfigMaxTerminateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigMaxTerminateCount.setStatus("mandatory")


class _PppxConfigRetryTimeout_Type(Integer32):
    """Custom type pppxConfigRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppxConfigRetryTimeout_Type.__name__ = "Integer32"
_PppxConfigRetryTimeout_Object = MibTableColumn
pppxConfigRetryTimeout = _PppxConfigRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 1, 1, 1, 22),
    _PppxConfigRetryTimeout_Type()
)
pppxConfigRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxConfigRetryTimeout.setStatus("mandatory")
_PppxCpGroup_ObjectIdentity = ObjectIdentity
pppxCpGroup = _PppxCpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2)
)
_PppxCpTable_Object = MibTable
pppxCpTable = _PppxCpTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1)
)
if mibBuilder.loadTexts:
    pppxCpTable.setStatus("mandatory")
_PppxCpEntry_Object = MibTableRow
pppxCpEntry = _PppxCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1)
)
pppxCpEntry.setIndexNames(
    (0, "XYLAN-PPP-MIB", "pppxCpPeerID"),
)
if mibBuilder.loadTexts:
    pppxCpEntry.setStatus("mandatory")
_PppxCpPeerID_Type = Integer32
_PppxCpPeerID_Object = MibTableColumn
pppxCpPeerID = _PppxCpPeerID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 1),
    _PppxCpPeerID_Type()
)
pppxCpPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpPeerID.setStatus("mandatory")


class _PppxCpSlotIndex_Type(Integer32):
    """Custom type pppxCpSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PppxCpSlotIndex_Type.__name__ = "Integer32"
_PppxCpSlotIndex_Object = MibTableColumn
pppxCpSlotIndex = _PppxCpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 2),
    _PppxCpSlotIndex_Type()
)
pppxCpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpSlotIndex.setStatus("mandatory")


class _PppxCpPortIndex_Type(Integer32):
    """Custom type pppxCpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppxCpPortIndex_Type.__name__ = "Integer32"
_PppxCpPortIndex_Object = MibTableColumn
pppxCpPortIndex = _PppxCpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 3),
    _PppxCpPortIndex_Type()
)
pppxCpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpPortIndex.setStatus("mandatory")


class _PppxCpIpOperStatus_Type(Integer32):
    """Custom type pppxCpIpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_PppxCpIpOperStatus_Type.__name__ = "Integer32"
_PppxCpIpOperStatus_Object = MibTableColumn
pppxCpIpOperStatus = _PppxCpIpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 4),
    _PppxCpIpOperStatus_Type()
)
pppxCpIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpIpOperStatus.setStatus("mandatory")


class _PppxCpIpxOperStatus_Type(Integer32):
    """Custom type pppxCpIpxOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_PppxCpIpxOperStatus_Type.__name__ = "Integer32"
_PppxCpIpxOperStatus_Object = MibTableColumn
pppxCpIpxOperStatus = _PppxCpIpxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 5),
    _PppxCpIpxOperStatus_Type()
)
pppxCpIpxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpIpxOperStatus.setStatus("mandatory")


class _PppxCpBcpOperStatus_Type(Integer32):
    """Custom type pppxCpBcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_PppxCpBcpOperStatus_Type.__name__ = "Integer32"
_PppxCpBcpOperStatus_Object = MibTableColumn
pppxCpBcpOperStatus = _PppxCpBcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 6),
    _PppxCpBcpOperStatus_Type()
)
pppxCpBcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpBcpOperStatus.setStatus("mandatory")


class _PppxCpCcpOperStatus_Type(Integer32):
    """Custom type pppxCpCcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_PppxCpCcpOperStatus_Type.__name__ = "Integer32"
_PppxCpCcpOperStatus_Object = MibTableColumn
pppxCpCcpOperStatus = _PppxCpCcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 7),
    _PppxCpCcpOperStatus_Type()
)
pppxCpCcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpCcpOperStatus.setStatus("mandatory")
_PppxCpTxLcpPackets_Type = Counter32
_PppxCpTxLcpPackets_Object = MibTableColumn
pppxCpTxLcpPackets = _PppxCpTxLcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 8),
    _PppxCpTxLcpPackets_Type()
)
pppxCpTxLcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpTxLcpPackets.setStatus("mandatory")
_PppxCpRxLcpPackets_Type = Counter32
_PppxCpRxLcpPackets_Object = MibTableColumn
pppxCpRxLcpPackets = _PppxCpRxLcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 9),
    _PppxCpRxLcpPackets_Type()
)
pppxCpRxLcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpRxLcpPackets.setStatus("mandatory")
_PppxCpTxIpcpPackets_Type = Counter32
_PppxCpTxIpcpPackets_Object = MibTableColumn
pppxCpTxIpcpPackets = _PppxCpTxIpcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 10),
    _PppxCpTxIpcpPackets_Type()
)
pppxCpTxIpcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpTxIpcpPackets.setStatus("mandatory")
_PppxCpRxIpcpPackets_Type = Counter32
_PppxCpRxIpcpPackets_Object = MibTableColumn
pppxCpRxIpcpPackets = _PppxCpRxIpcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 11),
    _PppxCpRxIpcpPackets_Type()
)
pppxCpRxIpcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpRxIpcpPackets.setStatus("mandatory")
_PppxCpTxIpxcpPackets_Type = Counter32
_PppxCpTxIpxcpPackets_Object = MibTableColumn
pppxCpTxIpxcpPackets = _PppxCpTxIpxcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 12),
    _PppxCpTxIpxcpPackets_Type()
)
pppxCpTxIpxcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpTxIpxcpPackets.setStatus("mandatory")
_PppxCpRxIpxcpPackets_Type = Counter32
_PppxCpRxIpxcpPackets_Object = MibTableColumn
pppxCpRxIpxcpPackets = _PppxCpRxIpxcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 13),
    _PppxCpRxIpxcpPackets_Type()
)
pppxCpRxIpxcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpRxIpxcpPackets.setStatus("mandatory")
_PppxCpTxBcpPackets_Type = Counter32
_PppxCpTxBcpPackets_Object = MibTableColumn
pppxCpTxBcpPackets = _PppxCpTxBcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 14),
    _PppxCpTxBcpPackets_Type()
)
pppxCpTxBcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpTxBcpPackets.setStatus("mandatory")
_PppxCpRxBcpPackets_Type = Counter32
_PppxCpRxBcpPackets_Object = MibTableColumn
pppxCpRxBcpPackets = _PppxCpRxBcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 15),
    _PppxCpRxBcpPackets_Type()
)
pppxCpRxBcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpRxBcpPackets.setStatus("mandatory")
_PppxCpTxCcpPackets_Type = Counter32
_PppxCpTxCcpPackets_Object = MibTableColumn
pppxCpTxCcpPackets = _PppxCpTxCcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 16),
    _PppxCpTxCcpPackets_Type()
)
pppxCpTxCcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpTxCcpPackets.setStatus("mandatory")
_PppxCpRxCcpPackets_Type = Counter32
_PppxCpRxCcpPackets_Object = MibTableColumn
pppxCpRxCcpPackets = _PppxCpRxCcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 2, 1, 1, 17),
    _PppxCpRxCcpPackets_Type()
)
pppxCpRxCcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxCpRxCcpPackets.setStatus("mandatory")
_PppxStatsGroup_ObjectIdentity = ObjectIdentity
pppxStatsGroup = _PppxStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3)
)
_PppxStatsTable_Object = MibTable
pppxStatsTable = _PppxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1)
)
if mibBuilder.loadTexts:
    pppxStatsTable.setStatus("mandatory")
_PppxStatsEntry_Object = MibTableRow
pppxStatsEntry = _PppxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1)
)
pppxStatsEntry.setIndexNames(
    (0, "XYLAN-PPP-MIB", "pppxStatsIfIndex"),
)
if mibBuilder.loadTexts:
    pppxStatsEntry.setStatus("mandatory")
_PppxStatsPeerID_Type = Integer32
_PppxStatsPeerID_Object = MibTableColumn
pppxStatsPeerID = _PppxStatsPeerID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 1),
    _PppxStatsPeerID_Type()
)
pppxStatsPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsPeerID.setStatus("mandatory")
_PppxStatsIfIndex_Type = Integer32
_PppxStatsIfIndex_Object = MibTableColumn
pppxStatsIfIndex = _PppxStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 2),
    _PppxStatsIfIndex_Type()
)
pppxStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsIfIndex.setStatus("mandatory")


class _PppxStatsSlotIndex_Type(Integer32):
    """Custom type pppxStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PppxStatsSlotIndex_Type.__name__ = "Integer32"
_PppxStatsSlotIndex_Object = MibTableColumn
pppxStatsSlotIndex = _PppxStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 3),
    _PppxStatsSlotIndex_Type()
)
pppxStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsSlotIndex.setStatus("mandatory")


class _PppxStatsPortIndex_Type(Integer32):
    """Custom type pppxStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppxStatsPortIndex_Type.__name__ = "Integer32"
_PppxStatsPortIndex_Object = MibTableColumn
pppxStatsPortIndex = _PppxStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 4),
    _PppxStatsPortIndex_Type()
)
pppxStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsPortIndex.setStatus("mandatory")


class _PppxStatsSubIndex_Type(Integer32):
    """Custom type pppxStatsSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PppxStatsSubIndex_Type.__name__ = "Integer32"
_PppxStatsSubIndex_Object = MibTableColumn
pppxStatsSubIndex = _PppxStatsSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 5),
    _PppxStatsSubIndex_Type()
)
pppxStatsSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsSubIndex.setStatus("mandatory")
_PppxStatsTxIPOctets_Type = Counter32
_PppxStatsTxIPOctets_Object = MibTableColumn
pppxStatsTxIPOctets = _PppxStatsTxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 6),
    _PppxStatsTxIPOctets_Type()
)
pppxStatsTxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxIPOctets.setStatus("mandatory")
_PppxStatsTxIPPackets_Type = Counter32
_PppxStatsTxIPPackets_Object = MibTableColumn
pppxStatsTxIPPackets = _PppxStatsTxIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 7),
    _PppxStatsTxIPPackets_Type()
)
pppxStatsTxIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxIPPackets.setStatus("mandatory")
_PppxStatsRxIPOctets_Type = Counter32
_PppxStatsRxIPOctets_Object = MibTableColumn
pppxStatsRxIPOctets = _PppxStatsRxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 8),
    _PppxStatsRxIPOctets_Type()
)
pppxStatsRxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxIPOctets.setStatus("mandatory")
_PppxStatsRxIPPackets_Type = Counter32
_PppxStatsRxIPPackets_Object = MibTableColumn
pppxStatsRxIPPackets = _PppxStatsRxIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 9),
    _PppxStatsRxIPPackets_Type()
)
pppxStatsRxIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxIPPackets.setStatus("mandatory")
_PppxStatsTxIPXOctets_Type = Counter32
_PppxStatsTxIPXOctets_Object = MibTableColumn
pppxStatsTxIPXOctets = _PppxStatsTxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 10),
    _PppxStatsTxIPXOctets_Type()
)
pppxStatsTxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxIPXOctets.setStatus("mandatory")
_PppxStatsTxIPXPackets_Type = Counter32
_PppxStatsTxIPXPackets_Object = MibTableColumn
pppxStatsTxIPXPackets = _PppxStatsTxIPXPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 11),
    _PppxStatsTxIPXPackets_Type()
)
pppxStatsTxIPXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxIPXPackets.setStatus("mandatory")
_PppxStatsRxIPXOctets_Type = Counter32
_PppxStatsRxIPXOctets_Object = MibTableColumn
pppxStatsRxIPXOctets = _PppxStatsRxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 12),
    _PppxStatsRxIPXOctets_Type()
)
pppxStatsRxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxIPXOctets.setStatus("mandatory")
_PppxStatsRxIPXPackets_Type = Counter32
_PppxStatsRxIPXPackets_Object = MibTableColumn
pppxStatsRxIPXPackets = _PppxStatsRxIPXPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 13),
    _PppxStatsRxIPXPackets_Type()
)
pppxStatsRxIPXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxIPXPackets.setStatus("mandatory")
_PppxStatsTxBPDUOctets_Type = Counter32
_PppxStatsTxBPDUOctets_Object = MibTableColumn
pppxStatsTxBPDUOctets = _PppxStatsTxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 14),
    _PppxStatsTxBPDUOctets_Type()
)
pppxStatsTxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxBPDUOctets.setStatus("mandatory")
_PppxStatsTxBPDUPackets_Type = Counter32
_PppxStatsTxBPDUPackets_Object = MibTableColumn
pppxStatsTxBPDUPackets = _PppxStatsTxBPDUPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 15),
    _PppxStatsTxBPDUPackets_Type()
)
pppxStatsTxBPDUPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxBPDUPackets.setStatus("mandatory")
_PppxStatsRxBPDUOctets_Type = Counter32
_PppxStatsRxBPDUOctets_Object = MibTableColumn
pppxStatsRxBPDUOctets = _PppxStatsRxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 16),
    _PppxStatsRxBPDUOctets_Type()
)
pppxStatsRxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxBPDUOctets.setStatus("mandatory")
_PppxStatsRxBPDUPackets_Type = Counter32
_PppxStatsRxBPDUPackets_Object = MibTableColumn
pppxStatsRxBPDUPackets = _PppxStatsRxBPDUPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 17),
    _PppxStatsRxBPDUPackets_Type()
)
pppxStatsRxBPDUPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxBPDUPackets.setStatus("mandatory")
_PppxStatsTxEthernetOctets_Type = Counter32
_PppxStatsTxEthernetOctets_Object = MibTableColumn
pppxStatsTxEthernetOctets = _PppxStatsTxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 18),
    _PppxStatsTxEthernetOctets_Type()
)
pppxStatsTxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxEthernetOctets.setStatus("mandatory")
_PppxStatsTxEthernetPackets_Type = Counter32
_PppxStatsTxEthernetPackets_Object = MibTableColumn
pppxStatsTxEthernetPackets = _PppxStatsTxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 19),
    _PppxStatsTxEthernetPackets_Type()
)
pppxStatsTxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxEthernetPackets.setStatus("mandatory")
_PppxStatsRxEthernetOctets_Type = Counter32
_PppxStatsRxEthernetOctets_Object = MibTableColumn
pppxStatsRxEthernetOctets = _PppxStatsRxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 20),
    _PppxStatsRxEthernetOctets_Type()
)
pppxStatsRxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxEthernetOctets.setStatus("mandatory")
_PppxStatsRxEthernetPackets_Type = Counter32
_PppxStatsRxEthernetPackets_Object = MibTableColumn
pppxStatsRxEthernetPackets = _PppxStatsRxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 21),
    _PppxStatsRxEthernetPackets_Type()
)
pppxStatsRxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxEthernetPackets.setStatus("mandatory")
_PppxStatsTx8025Octets_Type = Counter32
_PppxStatsTx8025Octets_Object = MibTableColumn
pppxStatsTx8025Octets = _PppxStatsTx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 22),
    _PppxStatsTx8025Octets_Type()
)
pppxStatsTx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTx8025Octets.setStatus("mandatory")
_PppxStatsTx8025Packets_Type = Counter32
_PppxStatsTx8025Packets_Object = MibTableColumn
pppxStatsTx8025Packets = _PppxStatsTx8025Packets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 23),
    _PppxStatsTx8025Packets_Type()
)
pppxStatsTx8025Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTx8025Packets.setStatus("mandatory")
_PppxStatsRx8025Octets_Type = Counter32
_PppxStatsRx8025Octets_Object = MibTableColumn
pppxStatsRx8025Octets = _PppxStatsRx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 24),
    _PppxStatsRx8025Octets_Type()
)
pppxStatsRx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRx8025Octets.setStatus("mandatory")
_PppxStatsRx8025Packets_Type = Counter32
_PppxStatsRx8025Packets_Object = MibTableColumn
pppxStatsRx8025Packets = _PppxStatsRx8025Packets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 25),
    _PppxStatsRx8025Packets_Type()
)
pppxStatsRx8025Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRx8025Packets.setStatus("mandatory")
_PppxStatsTxFDDIOctets_Type = Counter32
_PppxStatsTxFDDIOctets_Object = MibTableColumn
pppxStatsTxFDDIOctets = _PppxStatsTxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 26),
    _PppxStatsTxFDDIOctets_Type()
)
pppxStatsTxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxFDDIOctets.setStatus("mandatory")
_PppxStatsTxFDDIPackets_Type = Counter32
_PppxStatsTxFDDIPackets_Object = MibTableColumn
pppxStatsTxFDDIPackets = _PppxStatsTxFDDIPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 27),
    _PppxStatsTxFDDIPackets_Type()
)
pppxStatsTxFDDIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxFDDIPackets.setStatus("mandatory")
_PppxStatsRxFDDIOctets_Type = Counter32
_PppxStatsRxFDDIOctets_Object = MibTableColumn
pppxStatsRxFDDIOctets = _PppxStatsRxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 28),
    _PppxStatsRxFDDIOctets_Type()
)
pppxStatsRxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxFDDIOctets.setStatus("mandatory")
_PppxStatsRxFDDIPackets_Type = Counter32
_PppxStatsRxFDDIPackets_Object = MibTableColumn
pppxStatsRxFDDIPackets = _PppxStatsRxFDDIPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 29),
    _PppxStatsRxFDDIPackets_Type()
)
pppxStatsRxFDDIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxFDDIPackets.setStatus("mandatory")
_PppxStatsTxCompressedOctets_Type = Counter32
_PppxStatsTxCompressedOctets_Object = MibTableColumn
pppxStatsTxCompressedOctets = _PppxStatsTxCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 30),
    _PppxStatsTxCompressedOctets_Type()
)
pppxStatsTxCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxCompressedOctets.setStatus("mandatory")
_PppxStatsTxCompressedPackets_Type = Counter32
_PppxStatsTxCompressedPackets_Object = MibTableColumn
pppxStatsTxCompressedPackets = _PppxStatsTxCompressedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 31),
    _PppxStatsTxCompressedPackets_Type()
)
pppxStatsTxCompressedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxCompressedPackets.setStatus("mandatory")
_PppxStatsRxCompressedOctets_Type = Counter32
_PppxStatsRxCompressedOctets_Object = MibTableColumn
pppxStatsRxCompressedOctets = _PppxStatsRxCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 32),
    _PppxStatsRxCompressedOctets_Type()
)
pppxStatsRxCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxCompressedOctets.setStatus("mandatory")
_PppxStatsRxCompressedPackets_Type = Counter32
_PppxStatsRxCompressedPackets_Object = MibTableColumn
pppxStatsRxCompressedPackets = _PppxStatsRxCompressedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 33),
    _PppxStatsRxCompressedPackets_Type()
)
pppxStatsRxCompressedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxCompressedPackets.setStatus("mandatory")
_PppxStatsTxPrecompressedOctets_Type = Counter32
_PppxStatsTxPrecompressedOctets_Object = MibTableColumn
pppxStatsTxPrecompressedOctets = _PppxStatsTxPrecompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 34),
    _PppxStatsTxPrecompressedOctets_Type()
)
pppxStatsTxPrecompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsTxPrecompressedOctets.setStatus("mandatory")
_PppxStatsRxDecompressedOctets_Type = Counter32
_PppxStatsRxDecompressedOctets_Object = MibTableColumn
pppxStatsRxDecompressedOctets = _PppxStatsRxDecompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 35),
    _PppxStatsRxDecompressedOctets_Type()
)
pppxStatsRxDecompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxDecompressedOctets.setStatus("mandatory")
_PppxStatsRxCompressedDiscards_Type = Counter32
_PppxStatsRxCompressedDiscards_Object = MibTableColumn
pppxStatsRxCompressedDiscards = _PppxStatsRxCompressedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 3, 1, 1, 36),
    _PppxStatsRxCompressedDiscards_Type()
)
pppxStatsRxCompressedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxStatsRxCompressedDiscards.setStatus("mandatory")
_PppxIncomingGroup_ObjectIdentity = ObjectIdentity
pppxIncomingGroup = _PppxIncomingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4)
)
_PppxIncomingTable_Object = MibTable
pppxIncomingTable = _PppxIncomingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1)
)
if mibBuilder.loadTexts:
    pppxIncomingTable.setStatus("mandatory")
_PppxIncomingEntry_Object = MibTableRow
pppxIncomingEntry = _PppxIncomingEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1)
)
pppxIncomingEntry.setIndexNames(
    (0, "XYLAN-PPP-MIB", "pppxIncomingIndex"),
)
if mibBuilder.loadTexts:
    pppxIncomingEntry.setStatus("mandatory")
_PppxIncomingIndex_Type = Integer32
_PppxIncomingIndex_Object = MibTableColumn
pppxIncomingIndex = _PppxIncomingIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 1),
    _PppxIncomingIndex_Type()
)
pppxIncomingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppxIncomingIndex.setStatus("mandatory")


class _PppxIncomingAdminStatus_Type(Integer32):
    """Custom type pppxIncomingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_PppxIncomingAdminStatus_Type.__name__ = "Integer32"
_PppxIncomingAdminStatus_Object = MibTableColumn
pppxIncomingAdminStatus = _PppxIncomingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 2),
    _PppxIncomingAdminStatus_Type()
)
pppxIncomingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingAdminStatus.setStatus("mandatory")


class _PppxIncomingAuthenticationType_Type(Integer32):
    """Custom type pppxIncomingAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_PppxIncomingAuthenticationType_Type.__name__ = "Integer32"
_PppxIncomingAuthenticationType_Object = MibTableColumn
pppxIncomingAuthenticationType = _PppxIncomingAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 3),
    _PppxIncomingAuthenticationType_Type()
)
pppxIncomingAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingAuthenticationType.setStatus("mandatory")


class _PppxIncomingUserIdToRemote_Type(DisplayString):
    """Custom type pppxIncomingUserIdToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxIncomingUserIdToRemote_Type.__name__ = "DisplayString"
_PppxIncomingUserIdToRemote_Object = MibTableColumn
pppxIncomingUserIdToRemote = _PppxIncomingUserIdToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 4),
    _PppxIncomingUserIdToRemote_Type()
)
pppxIncomingUserIdToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingUserIdToRemote.setStatus("mandatory")


class _PppxIncomingPasswordToRemote_Type(DisplayString):
    """Custom type pppxIncomingPasswordToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PppxIncomingPasswordToRemote_Type.__name__ = "DisplayString"
_PppxIncomingPasswordToRemote_Object = MibTableColumn
pppxIncomingPasswordToRemote = _PppxIncomingPasswordToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 5),
    _PppxIncomingPasswordToRemote_Type()
)
pppxIncomingPasswordToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingPasswordToRemote.setStatus("mandatory")


class _PppxIncomingBridgingVLAN_Type(Integer32):
    """Custom type pppxIncomingBridgingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PppxIncomingBridgingVLAN_Type.__name__ = "Integer32"
_PppxIncomingBridgingVLAN_Object = MibTableColumn
pppxIncomingBridgingVLAN = _PppxIncomingBridgingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 6),
    _PppxIncomingBridgingVLAN_Type()
)
pppxIncomingBridgingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingBridgingVLAN.setStatus("mandatory")


class _PppxIncomingRoutingVLAN_Type(Integer32):
    """Custom type pppxIncomingRoutingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PppxIncomingRoutingVLAN_Type.__name__ = "Integer32"
_PppxIncomingRoutingVLAN_Object = MibTableColumn
pppxIncomingRoutingVLAN = _PppxIncomingRoutingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 7),
    _PppxIncomingRoutingVLAN_Type()
)
pppxIncomingRoutingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingRoutingVLAN.setStatus("mandatory")


class _PppxIncomingCompressionType_Type(Integer32):
    """Custom type pppxIncomingCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lzsDcp", 2),
          ("none", 1))
    )


_PppxIncomingCompressionType_Type.__name__ = "Integer32"
_PppxIncomingCompressionType_Object = MibTableColumn
pppxIncomingCompressionType = _PppxIncomingCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 8),
    _PppxIncomingCompressionType_Type()
)
pppxIncomingCompressionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingCompressionType.setStatus("mandatory")


class _PppxIncomingIpConfigAdminStatus_Type(Integer32):
    """Custom type pppxIncomingIpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxIncomingIpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxIncomingIpConfigAdminStatus_Object = MibTableColumn
pppxIncomingIpConfigAdminStatus = _PppxIncomingIpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 9),
    _PppxIncomingIpConfigAdminStatus_Type()
)
pppxIncomingIpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingIpConfigAdminStatus.setStatus("mandatory")


class _PppxIncomingBcpConfigAdminStatus_Type(Integer32):
    """Custom type pppxIncomingBcpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxIncomingBcpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxIncomingBcpConfigAdminStatus_Object = MibTableColumn
pppxIncomingBcpConfigAdminStatus = _PppxIncomingBcpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 10),
    _PppxIncomingBcpConfigAdminStatus_Type()
)
pppxIncomingBcpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingBcpConfigAdminStatus.setStatus("mandatory")


class _PppxIncomingIpxConfigAdminStatus_Type(Integer32):
    """Custom type pppxIncomingIpxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxIncomingIpxConfigAdminStatus_Type.__name__ = "Integer32"
_PppxIncomingIpxConfigAdminStatus_Object = MibTableColumn
pppxIncomingIpxConfigAdminStatus = _PppxIncomingIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 11),
    _PppxIncomingIpxConfigAdminStatus_Type()
)
pppxIncomingIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingIpxConfigAdminStatus.setStatus("mandatory")


class _PppxIncomingCcpConfigAdminStatus_Type(Integer32):
    """Custom type pppxIncomingCcpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppxIncomingCcpConfigAdminStatus_Type.__name__ = "Integer32"
_PppxIncomingCcpConfigAdminStatus_Object = MibTableColumn
pppxIncomingCcpConfigAdminStatus = _PppxIncomingCcpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 17, 4, 1, 1, 12),
    _PppxIncomingCcpConfigAdminStatus_Type()
)
pppxIncomingCcpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppxIncomingCcpConfigAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-PPP-MIB",
    **{"pppxConfigGroup": pppxConfigGroup,
       "pppxConfigTable": pppxConfigTable,
       "pppxConfigEntry": pppxConfigEntry,
       "pppxConfigPeerID": pppxConfigPeerID,
       "pppxConfigDescription": pppxConfigDescription,
       "pppxConfigAdminStatus": pppxConfigAdminStatus,
       "pppxConfigMode": pppxConfigMode,
       "pppxConfigBridgingVLAN": pppxConfigBridgingVLAN,
       "pppxConfigRoutingVLAN": pppxConfigRoutingVLAN,
       "pppxConfigCompressionType": pppxConfigCompressionType,
       "pppxConfigBridgingMode": pppxConfigBridgingMode,
       "pppxConfigIpConfigAdminStatus": pppxConfigIpConfigAdminStatus,
       "pppxConfigBcpConfigAdminStatus": pppxConfigBcpConfigAdminStatus,
       "pppxConfigIpxConfigAdminStatus": pppxConfigIpxConfigAdminStatus,
       "pppxConfigCcpConfigAdminStatus": pppxConfigCcpConfigAdminStatus,
       "pppxConfigRemoteIpAddress": pppxConfigRemoteIpAddress,
       "pppxConfigAuthenticationType": pppxConfigAuthenticationType,
       "pppxConfigUserIdToRemote": pppxConfigUserIdToRemote,
       "pppxConfigPasswordToRemote": pppxConfigPasswordToRemote,
       "pppxConfigUserIdFromRemote": pppxConfigUserIdFromRemote,
       "pppxConfigPasswordFromRemote": pppxConfigPasswordFromRemote,
       "pppxConfigMaxFailureCount": pppxConfigMaxFailureCount,
       "pppxConfigMaxConfigureCount": pppxConfigMaxConfigureCount,
       "pppxConfigMaxTerminateCount": pppxConfigMaxTerminateCount,
       "pppxConfigRetryTimeout": pppxConfigRetryTimeout,
       "pppxCpGroup": pppxCpGroup,
       "pppxCpTable": pppxCpTable,
       "pppxCpEntry": pppxCpEntry,
       "pppxCpPeerID": pppxCpPeerID,
       "pppxCpSlotIndex": pppxCpSlotIndex,
       "pppxCpPortIndex": pppxCpPortIndex,
       "pppxCpIpOperStatus": pppxCpIpOperStatus,
       "pppxCpIpxOperStatus": pppxCpIpxOperStatus,
       "pppxCpBcpOperStatus": pppxCpBcpOperStatus,
       "pppxCpCcpOperStatus": pppxCpCcpOperStatus,
       "pppxCpTxLcpPackets": pppxCpTxLcpPackets,
       "pppxCpRxLcpPackets": pppxCpRxLcpPackets,
       "pppxCpTxIpcpPackets": pppxCpTxIpcpPackets,
       "pppxCpRxIpcpPackets": pppxCpRxIpcpPackets,
       "pppxCpTxIpxcpPackets": pppxCpTxIpxcpPackets,
       "pppxCpRxIpxcpPackets": pppxCpRxIpxcpPackets,
       "pppxCpTxBcpPackets": pppxCpTxBcpPackets,
       "pppxCpRxBcpPackets": pppxCpRxBcpPackets,
       "pppxCpTxCcpPackets": pppxCpTxCcpPackets,
       "pppxCpRxCcpPackets": pppxCpRxCcpPackets,
       "pppxStatsGroup": pppxStatsGroup,
       "pppxStatsTable": pppxStatsTable,
       "pppxStatsEntry": pppxStatsEntry,
       "pppxStatsPeerID": pppxStatsPeerID,
       "pppxStatsIfIndex": pppxStatsIfIndex,
       "pppxStatsSlotIndex": pppxStatsSlotIndex,
       "pppxStatsPortIndex": pppxStatsPortIndex,
       "pppxStatsSubIndex": pppxStatsSubIndex,
       "pppxStatsTxIPOctets": pppxStatsTxIPOctets,
       "pppxStatsTxIPPackets": pppxStatsTxIPPackets,
       "pppxStatsRxIPOctets": pppxStatsRxIPOctets,
       "pppxStatsRxIPPackets": pppxStatsRxIPPackets,
       "pppxStatsTxIPXOctets": pppxStatsTxIPXOctets,
       "pppxStatsTxIPXPackets": pppxStatsTxIPXPackets,
       "pppxStatsRxIPXOctets": pppxStatsRxIPXOctets,
       "pppxStatsRxIPXPackets": pppxStatsRxIPXPackets,
       "pppxStatsTxBPDUOctets": pppxStatsTxBPDUOctets,
       "pppxStatsTxBPDUPackets": pppxStatsTxBPDUPackets,
       "pppxStatsRxBPDUOctets": pppxStatsRxBPDUOctets,
       "pppxStatsRxBPDUPackets": pppxStatsRxBPDUPackets,
       "pppxStatsTxEthernetOctets": pppxStatsTxEthernetOctets,
       "pppxStatsTxEthernetPackets": pppxStatsTxEthernetPackets,
       "pppxStatsRxEthernetOctets": pppxStatsRxEthernetOctets,
       "pppxStatsRxEthernetPackets": pppxStatsRxEthernetPackets,
       "pppxStatsTx8025Octets": pppxStatsTx8025Octets,
       "pppxStatsTx8025Packets": pppxStatsTx8025Packets,
       "pppxStatsRx8025Octets": pppxStatsRx8025Octets,
       "pppxStatsRx8025Packets": pppxStatsRx8025Packets,
       "pppxStatsTxFDDIOctets": pppxStatsTxFDDIOctets,
       "pppxStatsTxFDDIPackets": pppxStatsTxFDDIPackets,
       "pppxStatsRxFDDIOctets": pppxStatsRxFDDIOctets,
       "pppxStatsRxFDDIPackets": pppxStatsRxFDDIPackets,
       "pppxStatsTxCompressedOctets": pppxStatsTxCompressedOctets,
       "pppxStatsTxCompressedPackets": pppxStatsTxCompressedPackets,
       "pppxStatsRxCompressedOctets": pppxStatsRxCompressedOctets,
       "pppxStatsRxCompressedPackets": pppxStatsRxCompressedPackets,
       "pppxStatsTxPrecompressedOctets": pppxStatsTxPrecompressedOctets,
       "pppxStatsRxDecompressedOctets": pppxStatsRxDecompressedOctets,
       "pppxStatsRxCompressedDiscards": pppxStatsRxCompressedDiscards,
       "pppxIncomingGroup": pppxIncomingGroup,
       "pppxIncomingTable": pppxIncomingTable,
       "pppxIncomingEntry": pppxIncomingEntry,
       "pppxIncomingIndex": pppxIncomingIndex,
       "pppxIncomingAdminStatus": pppxIncomingAdminStatus,
       "pppxIncomingAuthenticationType": pppxIncomingAuthenticationType,
       "pppxIncomingUserIdToRemote": pppxIncomingUserIdToRemote,
       "pppxIncomingPasswordToRemote": pppxIncomingPasswordToRemote,
       "pppxIncomingBridgingVLAN": pppxIncomingBridgingVLAN,
       "pppxIncomingRoutingVLAN": pppxIncomingRoutingVLAN,
       "pppxIncomingCompressionType": pppxIncomingCompressionType,
       "pppxIncomingIpConfigAdminStatus": pppxIncomingIpConfigAdminStatus,
       "pppxIncomingBcpConfigAdminStatus": pppxIncomingBcpConfigAdminStatus,
       "pppxIncomingIpxConfigAdminStatus": pppxIncomingIpxConfigAdminStatus,
       "pppxIncomingCcpConfigAdminStatus": pppxIncomingCcpConfigAdminStatus}
)
