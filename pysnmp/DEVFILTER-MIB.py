# SNMP MIB module (DEVFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVFILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:07 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aniDevFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevFilterTable_Object = MibTable
aniDevFilterTable = _AniDevFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1)
)
if mibBuilder.loadTexts:
    aniDevFilterTable.setStatus("current")
_AniDevFilterEntry_Object = MibTableRow
aniDevFilterEntry = _AniDevFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1)
)
aniDevFilterEntry.setIndexNames(
    (0, "DEVFILTER-MIB", "aniDevFilterIfIndex"),
    (0, "DEVFILTER-MIB", "aniDevFilterIdentifier"),
)
if mibBuilder.loadTexts:
    aniDevFilterEntry.setStatus("current")


class _AniDevFilterIfIndex_Type(Integer32):
    """Custom type aniDevFilterIfIndex based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("wireless-port1", 2),
          ("wireless-port2", 3),
          ("wireless-port3", 4),
          ("wireless-port4", 5),
          ("wireless-port5", 6),
          ("wireless-port6", 7))
    )


_AniDevFilterIfIndex_Type.__name__ = "Integer32"
_AniDevFilterIfIndex_Object = MibTableColumn
aniDevFilterIfIndex = _AniDevFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 1),
    _AniDevFilterIfIndex_Type()
)
aniDevFilterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIfIndex.setStatus("current")


class _AniDevFilterIdentifier_Type(Integer32):
    """Custom type aniDevFilterIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AniDevFilterIdentifier_Type.__name__ = "Integer32"
_AniDevFilterIdentifier_Object = MibTableColumn
aniDevFilterIdentifier = _AniDevFilterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 2),
    _AniDevFilterIdentifier_Type()
)
aniDevFilterIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIdentifier.setStatus("current")


class _AniDevFilterName_Type(DisplayString):
    """Custom type aniDevFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniDevFilterName_Type.__name__ = "DisplayString"
_AniDevFilterName_Object = MibTableColumn
aniDevFilterName = _AniDevFilterName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 3),
    _AniDevFilterName_Type()
)
aniDevFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterName.setStatus("current")


class _AniDevFilterPriority_Type(Integer32):
    """Custom type aniDevFilterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AniDevFilterPriority_Type.__name__ = "Integer32"
_AniDevFilterPriority_Object = MibTableColumn
aniDevFilterPriority = _AniDevFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 4),
    _AniDevFilterPriority_Type()
)
aniDevFilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterPriority.setStatus("current")


class _AniDevFilterActivationState_Type(Integer32):
    """Custom type aniDevFilterActivationState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AniDevFilterActivationState_Type.__name__ = "Integer32"
_AniDevFilterActivationState_Object = MibTableColumn
aniDevFilterActivationState = _AniDevFilterActivationState_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 5),
    _AniDevFilterActivationState_Type()
)
aniDevFilterActivationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterActivationState.setStatus("current")


class _AniDevFilterPermission_Type(Integer32):
    """Custom type aniDevFilterPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_AniDevFilterPermission_Type.__name__ = "Integer32"
_AniDevFilterPermission_Object = MibTableColumn
aniDevFilterPermission = _AniDevFilterPermission_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 6),
    _AniDevFilterPermission_Type()
)
aniDevFilterPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterPermission.setStatus("current")


class _AniDevFilterIpProtocol_Type(Integer32):
    """Custom type aniDevFilterIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_AniDevFilterIpProtocol_Type.__name__ = "Integer32"
_AniDevFilterIpProtocol_Object = MibTableColumn
aniDevFilterIpProtocol = _AniDevFilterIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 7),
    _AniDevFilterIpProtocol_Type()
)
aniDevFilterIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpProtocol.setStatus("current")
_AniDevFilterIpSaddr_Type = IpAddress
_AniDevFilterIpSaddr_Object = MibTableColumn
aniDevFilterIpSaddr = _AniDevFilterIpSaddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 8),
    _AniDevFilterIpSaddr_Type()
)
aniDevFilterIpSaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpSaddr.setStatus("current")
_AniDevFilterIpSmask_Type = IpAddress
_AniDevFilterIpSmask_Object = MibTableColumn
aniDevFilterIpSmask = _AniDevFilterIpSmask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 9),
    _AniDevFilterIpSmask_Type()
)
aniDevFilterIpSmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpSmask.setStatus("current")
_AniDevFilterIpDaddr_Type = IpAddress
_AniDevFilterIpDaddr_Object = MibTableColumn
aniDevFilterIpDaddr = _AniDevFilterIpDaddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 10),
    _AniDevFilterIpDaddr_Type()
)
aniDevFilterIpDaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpDaddr.setStatus("current")
_AniDevFilterIpDmask_Type = IpAddress
_AniDevFilterIpDmask_Object = MibTableColumn
aniDevFilterIpDmask = _AniDevFilterIpDmask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 11),
    _AniDevFilterIpDmask_Type()
)
aniDevFilterIpDmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpDmask.setStatus("current")


class _AniDevFilterIpSourceStart_Type(Integer32):
    """Custom type aniDevFilterIpSourceStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AniDevFilterIpSourceStart_Type.__name__ = "Integer32"
_AniDevFilterIpSourceStart_Object = MibTableColumn
aniDevFilterIpSourceStart = _AniDevFilterIpSourceStart_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 12),
    _AniDevFilterIpSourceStart_Type()
)
aniDevFilterIpSourceStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpSourceStart.setStatus("current")


class _AniDevFilterIpSourceEnd_Type(Integer32):
    """Custom type aniDevFilterIpSourceEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AniDevFilterIpSourceEnd_Type.__name__ = "Integer32"
_AniDevFilterIpSourceEnd_Object = MibTableColumn
aniDevFilterIpSourceEnd = _AniDevFilterIpSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 13),
    _AniDevFilterIpSourceEnd_Type()
)
aniDevFilterIpSourceEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpSourceEnd.setStatus("current")


class _AniDevFilterIpDestStart_Type(Integer32):
    """Custom type aniDevFilterIpDestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AniDevFilterIpDestStart_Type.__name__ = "Integer32"
_AniDevFilterIpDestStart_Object = MibTableColumn
aniDevFilterIpDestStart = _AniDevFilterIpDestStart_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 14),
    _AniDevFilterIpDestStart_Type()
)
aniDevFilterIpDestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpDestStart.setStatus("current")


class _AniDevFilterIpDestEnd_Type(Integer32):
    """Custom type aniDevFilterIpDestEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AniDevFilterIpDestEnd_Type.__name__ = "Integer32"
_AniDevFilterIpDestEnd_Object = MibTableColumn
aniDevFilterIpDestEnd = _AniDevFilterIpDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 15),
    _AniDevFilterIpDestEnd_Type()
)
aniDevFilterIpDestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpDestEnd.setStatus("current")
_AniDevFilterIpOptions_Type = Integer32
_AniDevFilterIpOptions_Object = MibTableColumn
aniDevFilterIpOptions = _AniDevFilterIpOptions_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 16),
    _AniDevFilterIpOptions_Type()
)
aniDevFilterIpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpOptions.setStatus("current")


class _AniDevFilterIpSecOptions_Type(Integer32):
    """Custom type aniDevFilterIpSecOptions based on Integer32"""
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
        *(("confidential", 3),
          ("secret", 2),
          ("top-secret", 1),
          ("unclassified", 4))
    )


_AniDevFilterIpSecOptions_Type.__name__ = "Integer32"
_AniDevFilterIpSecOptions_Object = MibTableColumn
aniDevFilterIpSecOptions = _AniDevFilterIpSecOptions_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 17),
    _AniDevFilterIpSecOptions_Type()
)
aniDevFilterIpSecOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIpSecOptions.setStatus("current")
_AniDevFilterIcmpMsgType_Type = Integer32
_AniDevFilterIcmpMsgType_Object = MibTableColumn
aniDevFilterIcmpMsgType = _AniDevFilterIcmpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 18),
    _AniDevFilterIcmpMsgType_Type()
)
aniDevFilterIcmpMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIcmpMsgType.setStatus("current")
_AniDevFilterIcmpSubcode_Type = Integer32
_AniDevFilterIcmpSubcode_Object = MibTableColumn
aniDevFilterIcmpSubcode = _AniDevFilterIcmpSubcode_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 19),
    _AniDevFilterIcmpSubcode_Type()
)
aniDevFilterIcmpSubcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIcmpSubcode.setStatus("current")
_AniDevFilterTcpFlags_Type = Integer32
_AniDevFilterTcpFlags_Object = MibTableColumn
aniDevFilterTcpFlags = _AniDevFilterTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 20),
    _AniDevFilterTcpFlags_Type()
)
aniDevFilterTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterTcpFlags.setStatus("current")


class _AniDevFilterDestMacMask_Type(OctetString):
    """Custom type aniDevFilterDestMacMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AniDevFilterDestMacMask_Type.__name__ = "OctetString"
_AniDevFilterDestMacMask_Object = MibTableColumn
aniDevFilterDestMacMask = _AniDevFilterDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 21),
    _AniDevFilterDestMacMask_Type()
)
aniDevFilterDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterDestMacMask.setStatus("current")
_AniDevFilterSourceMac_Type = MacAddress
_AniDevFilterSourceMac_Object = MibTableColumn
aniDevFilterSourceMac = _AniDevFilterSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 22),
    _AniDevFilterSourceMac_Type()
)
aniDevFilterSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterSourceMac.setStatus("current")
_AniDevFilterEnetType_Type = DisplayString
_AniDevFilterEnetType_Object = MibTableColumn
aniDevFilterEnetType = _AniDevFilterEnetType_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 23),
    _AniDevFilterEnetType_Type()
)
aniDevFilterEnetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterEnetType.setStatus("current")
_AniDevFilterLlcDSAP_Type = DisplayString
_AniDevFilterLlcDSAP_Object = MibTableColumn
aniDevFilterLlcDSAP = _AniDevFilterLlcDSAP_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 24),
    _AniDevFilterLlcDSAP_Type()
)
aniDevFilterLlcDSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterLlcDSAP.setStatus("current")
_AniDevFilterLlcSSAP_Type = DisplayString
_AniDevFilterLlcSSAP_Object = MibTableColumn
aniDevFilterLlcSSAP = _AniDevFilterLlcSSAP_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 25),
    _AniDevFilterLlcSSAP_Type()
)
aniDevFilterLlcSSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterLlcSSAP.setStatus("current")
_AniDevFilterLlcControl_Type = DisplayString
_AniDevFilterLlcControl_Object = MibTableColumn
aniDevFilterLlcControl = _AniDevFilterLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 26),
    _AniDevFilterLlcControl_Type()
)
aniDevFilterLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterLlcControl.setStatus("current")
_AniDevFilterLocalCode_Type = DisplayString
_AniDevFilterLocalCode_Object = MibTableColumn
aniDevFilterLocalCode = _AniDevFilterLocalCode_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 27),
    _AniDevFilterLocalCode_Type()
)
aniDevFilterLocalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterLocalCode.setStatus("current")
_AniDevFilterRowStatus_Type = RowStatus
_AniDevFilterRowStatus_Object = MibTableColumn
aniDevFilterRowStatus = _AniDevFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 28),
    _AniDevFilterRowStatus_Type()
)
aniDevFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterRowStatus.setStatus("current")


class _AniDevFilterUserPriorityHi_Type(Integer32):
    """Custom type aniDevFilterUserPriorityHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AniDevFilterUserPriorityHi_Type.__name__ = "Integer32"
_AniDevFilterUserPriorityHi_Object = MibTableColumn
aniDevFilterUserPriorityHi = _AniDevFilterUserPriorityHi_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 29),
    _AniDevFilterUserPriorityHi_Type()
)
aniDevFilterUserPriorityHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterUserPriorityHi.setStatus("current")


class _AniDevFilterUserPriorityLo_Type(Integer32):
    """Custom type aniDevFilterUserPriorityLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AniDevFilterUserPriorityLo_Type.__name__ = "Integer32"
_AniDevFilterUserPriorityLo_Object = MibTableColumn
aniDevFilterUserPriorityLo = _AniDevFilterUserPriorityLo_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 30),
    _AniDevFilterUserPriorityLo_Type()
)
aniDevFilterUserPriorityLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterUserPriorityLo.setStatus("current")


class _AniDevFilterVlanIdStart_Type(Integer32):
    """Custom type aniDevFilterVlanIdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AniDevFilterVlanIdStart_Type.__name__ = "Integer32"
_AniDevFilterVlanIdStart_Object = MibTableColumn
aniDevFilterVlanIdStart = _AniDevFilterVlanIdStart_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 31),
    _AniDevFilterVlanIdStart_Type()
)
aniDevFilterVlanIdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterVlanIdStart.setStatus("current")


class _AniDevFilterVlanIdEnd_Type(Integer32):
    """Custom type aniDevFilterVlanIdEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AniDevFilterVlanIdEnd_Type.__name__ = "Integer32"
_AniDevFilterVlanIdEnd_Object = MibTableColumn
aniDevFilterVlanIdEnd = _AniDevFilterVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 1, 1, 32),
    _AniDevFilterVlanIdEnd_Type()
)
aniDevFilterVlanIdEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterVlanIdEnd.setStatus("current")
_AniDevFilterIfTable_Object = MibTable
aniDevFilterIfTable = _AniDevFilterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 2)
)
if mibBuilder.loadTexts:
    aniDevFilterIfTable.setStatus("current")
_AniDevFilterIfEntry_Object = MibTableRow
aniDevFilterIfEntry = _AniDevFilterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 2, 1)
)
aniDevFilterIfEntry.setIndexNames(
    (0, "DEVFILTER-MIB", "aniDevFilterIfIdentifier"),
)
if mibBuilder.loadTexts:
    aniDevFilterIfEntry.setStatus("current")


class _AniDevFilterIfIdentifier_Type(Integer32):
    """Custom type aniDevFilterIfIdentifier based on Integer32"""
    defaultValue = 1

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
        *(("ethernet", 1),
          ("wireless-port1", 2),
          ("wireless-port2", 3),
          ("wireless-port3", 4),
          ("wireless-port4", 5),
          ("wireless-port5", 6),
          ("wireless-port6", 7))
    )


_AniDevFilterIfIdentifier_Type.__name__ = "Integer32"
_AniDevFilterIfIdentifier_Object = MibTableColumn
aniDevFilterIfIdentifier = _AniDevFilterIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 2, 1, 1),
    _AniDevFilterIfIdentifier_Type()
)
aniDevFilterIfIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIfIdentifier.setStatus("current")


class _AniDevFilterIfFlag_Type(Integer32):
    """Custom type aniDevFilterIfFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AniDevFilterIfFlag_Type.__name__ = "Integer32"
_AniDevFilterIfFlag_Object = MibTableColumn
aniDevFilterIfFlag = _AniDevFilterIfFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8, 2, 1, 2),
    _AniDevFilterIfFlag_Type()
)
aniDevFilterIfFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevFilterIfFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVFILTER-MIB",
    **{"aniDevFilter": aniDevFilter,
       "aniDevFilterTable": aniDevFilterTable,
       "aniDevFilterEntry": aniDevFilterEntry,
       "aniDevFilterIfIndex": aniDevFilterIfIndex,
       "aniDevFilterIdentifier": aniDevFilterIdentifier,
       "aniDevFilterName": aniDevFilterName,
       "aniDevFilterPriority": aniDevFilterPriority,
       "aniDevFilterActivationState": aniDevFilterActivationState,
       "aniDevFilterPermission": aniDevFilterPermission,
       "aniDevFilterIpProtocol": aniDevFilterIpProtocol,
       "aniDevFilterIpSaddr": aniDevFilterIpSaddr,
       "aniDevFilterIpSmask": aniDevFilterIpSmask,
       "aniDevFilterIpDaddr": aniDevFilterIpDaddr,
       "aniDevFilterIpDmask": aniDevFilterIpDmask,
       "aniDevFilterIpSourceStart": aniDevFilterIpSourceStart,
       "aniDevFilterIpSourceEnd": aniDevFilterIpSourceEnd,
       "aniDevFilterIpDestStart": aniDevFilterIpDestStart,
       "aniDevFilterIpDestEnd": aniDevFilterIpDestEnd,
       "aniDevFilterIpOptions": aniDevFilterIpOptions,
       "aniDevFilterIpSecOptions": aniDevFilterIpSecOptions,
       "aniDevFilterIcmpMsgType": aniDevFilterIcmpMsgType,
       "aniDevFilterIcmpSubcode": aniDevFilterIcmpSubcode,
       "aniDevFilterTcpFlags": aniDevFilterTcpFlags,
       "aniDevFilterDestMacMask": aniDevFilterDestMacMask,
       "aniDevFilterSourceMac": aniDevFilterSourceMac,
       "aniDevFilterEnetType": aniDevFilterEnetType,
       "aniDevFilterLlcDSAP": aniDevFilterLlcDSAP,
       "aniDevFilterLlcSSAP": aniDevFilterLlcSSAP,
       "aniDevFilterLlcControl": aniDevFilterLlcControl,
       "aniDevFilterLocalCode": aniDevFilterLocalCode,
       "aniDevFilterRowStatus": aniDevFilterRowStatus,
       "aniDevFilterUserPriorityHi": aniDevFilterUserPriorityHi,
       "aniDevFilterUserPriorityLo": aniDevFilterUserPriorityLo,
       "aniDevFilterVlanIdStart": aniDevFilterVlanIdStart,
       "aniDevFilterVlanIdEnd": aniDevFilterVlanIdEnd,
       "aniDevFilterIfTable": aniDevFilterIfTable,
       "aniDevFilterIfEntry": aniDevFilterIfEntry,
       "aniDevFilterIfIdentifier": aniDevFilterIfIdentifier,
       "aniDevFilterIfFlag": aniDevFilterIfFlag}
)
