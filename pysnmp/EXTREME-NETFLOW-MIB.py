# SNMP MIB module (EXTREME-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeNetFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeNetFlowConfigPort_ObjectIdentity = ObjectIdentity
extremeNetFlowConfigPort = _ExtremeNetFlowConfigPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1)
)
_ExtremeNetFlowPortConfigTable_Object = MibTable
extremeNetFlowPortConfigTable = _ExtremeNetFlowPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigTable.setStatus("current")
_ExtremeNetFlowPortConfigEntry_Object = MibTableRow
extremeNetFlowPortConfigEntry = _ExtremeNetFlowPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1, 1)
)
extremeNetFlowPortConfigEntry.setIndexNames(
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigEntry.setStatus("current")


class _ExtremeNetFlowPortConfigPortIndex_Type(Integer32):
    """Custom type extremeNetFlowPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowPortConfigPortIndex_Type.__name__ = "Integer32"
_ExtremeNetFlowPortConfigPortIndex_Object = MibTableColumn
extremeNetFlowPortConfigPortIndex = _ExtremeNetFlowPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1, 1, 1),
    _ExtremeNetFlowPortConfigPortIndex_Type()
)
extremeNetFlowPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigPortIndex.setStatus("current")
_ExtremeNetFlowPortConfigEnabled_Type = TruthValue
_ExtremeNetFlowPortConfigEnabled_Object = MibTableColumn
extremeNetFlowPortConfigEnabled = _ExtremeNetFlowPortConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1, 1, 2),
    _ExtremeNetFlowPortConfigEnabled_Type()
)
extremeNetFlowPortConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigEnabled.setStatus("current")


class _ExtremeNetFlowPortConfigTimout_Type(Integer32):
    """Custom type extremeNetFlowPortConfigTimout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowPortConfigTimout_Type.__name__ = "Integer32"
_ExtremeNetFlowPortConfigTimout_Object = MibTableColumn
extremeNetFlowPortConfigTimout = _ExtremeNetFlowPortConfigTimout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1, 1, 3),
    _ExtremeNetFlowPortConfigTimout_Type()
)
extremeNetFlowPortConfigTimout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigTimout.setStatus("current")


class _ExtremeNetFlowPortOverFlowPackets_Type(Integer32):
    """Custom type extremeNetFlowPortOverFlowPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowPortOverFlowPackets_Type.__name__ = "Integer32"
_ExtremeNetFlowPortOverFlowPackets_Object = MibTableColumn
extremeNetFlowPortOverFlowPackets = _ExtremeNetFlowPortOverFlowPackets_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 1, 1, 4),
    _ExtremeNetFlowPortOverFlowPackets_Type()
)
extremeNetFlowPortOverFlowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowPortOverFlowPackets.setStatus("current")
_ExtremeNetFlowPortFilterConfigTable_Object = MibTable
extremeNetFlowPortFilterConfigTable = _ExtremeNetFlowPortFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    extremeNetFlowPortFilterConfigTable.setStatus("current")
_ExtremeNetFlowPortFilterConfigEntry_Object = MibTableRow
extremeNetFlowPortFilterConfigEntry = _ExtremeNetFlowPortFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1)
)
extremeNetFlowPortFilterConfigEntry.setIndexNames(
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowPortConfigPortNumber"),
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowPortConfigFilterEgress"),
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowPortConfigFilterNumber"),
)
if mibBuilder.loadTexts:
    extremeNetFlowPortFilterConfigEntry.setStatus("current")


class _ExtremeNetFlowPortConfigPortNumber_Type(Integer32):
    """Custom type extremeNetFlowPortConfigPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowPortConfigPortNumber_Type.__name__ = "Integer32"
_ExtremeNetFlowPortConfigPortNumber_Object = MibTableColumn
extremeNetFlowPortConfigPortNumber = _ExtremeNetFlowPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 1),
    _ExtremeNetFlowPortConfigPortNumber_Type()
)
extremeNetFlowPortConfigPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigPortNumber.setStatus("current")
_ExtremeNetFlowPortConfigFilterEgress_Type = TruthValue
_ExtremeNetFlowPortConfigFilterEgress_Object = MibTableColumn
extremeNetFlowPortConfigFilterEgress = _ExtremeNetFlowPortConfigFilterEgress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 2),
    _ExtremeNetFlowPortConfigFilterEgress_Type()
)
extremeNetFlowPortConfigFilterEgress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigFilterEgress.setStatus("current")


class _ExtremeNetFlowPortConfigFilterNumber_Type(Integer32):
    """Custom type extremeNetFlowPortConfigFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeNetFlowPortConfigFilterNumber_Type.__name__ = "Integer32"
_ExtremeNetFlowPortConfigFilterNumber_Object = MibTableColumn
extremeNetFlowPortConfigFilterNumber = _ExtremeNetFlowPortConfigFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 3),
    _ExtremeNetFlowPortConfigFilterNumber_Type()
)
extremeNetFlowPortConfigFilterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowPortConfigFilterNumber.setStatus("current")
_ExtremeNetFlowPortEnabled_Type = TruthValue
_ExtremeNetFlowPortEnabled_Object = MibTableColumn
extremeNetFlowPortEnabled = _ExtremeNetFlowPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 4),
    _ExtremeNetFlowPortEnabled_Type()
)
extremeNetFlowPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowPortEnabled.setStatus("current")
_ExtremeNetFlowFilterEnabled_Type = TruthValue
_ExtremeNetFlowFilterEnabled_Object = MibTableColumn
extremeNetFlowFilterEnabled = _ExtremeNetFlowFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 5),
    _ExtremeNetFlowFilterEnabled_Type()
)
extremeNetFlowFilterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowFilterEnabled.setStatus("current")
_ExtremeNetFlowDestIpAddress_Type = IpAddress
_ExtremeNetFlowDestIpAddress_Object = MibTableColumn
extremeNetFlowDestIpAddress = _ExtremeNetFlowDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 6),
    _ExtremeNetFlowDestIpAddress_Type()
)
extremeNetFlowDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowDestIpAddress.setStatus("current")
_ExtremeNetFlowDestIpAddressMask_Type = IpAddress
_ExtremeNetFlowDestIpAddressMask_Object = MibTableColumn
extremeNetFlowDestIpAddressMask = _ExtremeNetFlowDestIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 7),
    _ExtremeNetFlowDestIpAddressMask_Type()
)
extremeNetFlowDestIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowDestIpAddressMask.setStatus("current")
_ExtremeNetFlowSourceIpAddress_Type = IpAddress
_ExtremeNetFlowSourceIpAddress_Object = MibTableColumn
extremeNetFlowSourceIpAddress = _ExtremeNetFlowSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 8),
    _ExtremeNetFlowSourceIpAddress_Type()
)
extremeNetFlowSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowSourceIpAddress.setStatus("current")
_ExtremeNetFlowSourceIpAddressMask_Type = IpAddress
_ExtremeNetFlowSourceIpAddressMask_Object = MibTableColumn
extremeNetFlowSourceIpAddressMask = _ExtremeNetFlowSourceIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 9),
    _ExtremeNetFlowSourceIpAddressMask_Type()
)
extremeNetFlowSourceIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowSourceIpAddressMask.setStatus("current")


class _ExtremeNetFlowDestPort_Type(Integer32):
    """Custom type extremeNetFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowDestPort_Type.__name__ = "Integer32"
_ExtremeNetFlowDestPort_Object = MibTableColumn
extremeNetFlowDestPort = _ExtremeNetFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 10),
    _ExtremeNetFlowDestPort_Type()
)
extremeNetFlowDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowDestPort.setStatus("current")


class _ExtremeNetFlowDestPortMask_Type(Integer32):
    """Custom type extremeNetFlowDestPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowDestPortMask_Type.__name__ = "Integer32"
_ExtremeNetFlowDestPortMask_Object = MibTableColumn
extremeNetFlowDestPortMask = _ExtremeNetFlowDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 11),
    _ExtremeNetFlowDestPortMask_Type()
)
extremeNetFlowDestPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowDestPortMask.setStatus("current")


class _ExtremeNetFlowSourcePort_Type(Integer32):
    """Custom type extremeNetFlowSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowSourcePort_Type.__name__ = "Integer32"
_ExtremeNetFlowSourcePort_Object = MibTableColumn
extremeNetFlowSourcePort = _ExtremeNetFlowSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 12),
    _ExtremeNetFlowSourcePort_Type()
)
extremeNetFlowSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowSourcePort.setStatus("current")


class _ExtremeNetFlowSourcePortMask_Type(Integer32):
    """Custom type extremeNetFlowSourcePortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowSourcePortMask_Type.__name__ = "Integer32"
_ExtremeNetFlowSourcePortMask_Object = MibTableColumn
extremeNetFlowSourcePortMask = _ExtremeNetFlowSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 13),
    _ExtremeNetFlowSourcePortMask_Type()
)
extremeNetFlowSourcePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowSourcePortMask.setStatus("current")


class _ExtremeNetFlowProtocol_Type(Integer32):
    """Custom type extremeNetFlowProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowProtocol_Type.__name__ = "Integer32"
_ExtremeNetFlowProtocol_Object = MibTableColumn
extremeNetFlowProtocol = _ExtremeNetFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 14),
    _ExtremeNetFlowProtocol_Type()
)
extremeNetFlowProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowProtocol.setStatus("current")


class _ExtremeNetFlowProtocolMask_Type(Integer32):
    """Custom type extremeNetFlowProtocolMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowProtocolMask_Type.__name__ = "Integer32"
_ExtremeNetFlowProtocolMask_Object = MibTableColumn
extremeNetFlowProtocolMask = _ExtremeNetFlowProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 15),
    _ExtremeNetFlowProtocolMask_Type()
)
extremeNetFlowProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowProtocolMask.setStatus("current")


class _ExtremeNetFlowFilterGroupNumber_Type(Integer32):
    """Custom type extremeNetFlowFilterGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ExtremeNetFlowFilterGroupNumber_Type.__name__ = "Integer32"
_ExtremeNetFlowFilterGroupNumber_Object = MibTableColumn
extremeNetFlowFilterGroupNumber = _ExtremeNetFlowFilterGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 16),
    _ExtremeNetFlowFilterGroupNumber_Type()
)
extremeNetFlowFilterGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowFilterGroupNumber.setStatus("current")
_ExtremeNetFlowMatchAllFlag_Type = TruthValue
_ExtremeNetFlowMatchAllFlag_Object = MibTableColumn
extremeNetFlowMatchAllFlag = _ExtremeNetFlowMatchAllFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 17),
    _ExtremeNetFlowMatchAllFlag_Type()
)
extremeNetFlowMatchAllFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowMatchAllFlag.setStatus("current")
_ExtremeNetFlowMatchNoneFlag_Type = TruthValue
_ExtremeNetFlowMatchNoneFlag_Object = MibTableColumn
extremeNetFlowMatchNoneFlag = _ExtremeNetFlowMatchNoneFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 1, 2, 1, 18),
    _ExtremeNetFlowMatchNoneFlag_Type()
)
extremeNetFlowMatchNoneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowMatchNoneFlag.setStatus("current")
_ExtremeNetFlowConfigGroup_ObjectIdentity = ObjectIdentity
extremeNetFlowConfigGroup = _ExtremeNetFlowConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2)
)
_ExtremeNetFlowGroupCollectorTable_Object = MibTable
extremeNetFlowGroupCollectorTable = _ExtremeNetFlowGroupCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2)
)
if mibBuilder.loadTexts:
    extremeNetFlowGroupCollectorTable.setStatus("current")
_ExtremeNetFlowGroupCollectorEntry_Object = MibTableRow
extremeNetFlowGroupCollectorEntry = _ExtremeNetFlowGroupCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1)
)
extremeNetFlowGroupCollectorEntry.setIndexNames(
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowGroupNumber"),
    (0, "EXTREME-NETFLOW-MIB", "extremeNetFlowCollectorId"),
)
if mibBuilder.loadTexts:
    extremeNetFlowGroupCollectorEntry.setStatus("current")


class _ExtremeNetFlowGroupNumber_Type(Integer32):
    """Custom type extremeNetFlowGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ExtremeNetFlowGroupNumber_Type.__name__ = "Integer32"
_ExtremeNetFlowGroupNumber_Object = MibTableColumn
extremeNetFlowGroupNumber = _ExtremeNetFlowGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 1),
    _ExtremeNetFlowGroupNumber_Type()
)
extremeNetFlowGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowGroupNumber.setStatus("current")


class _ExtremeNetFlowCollectorId_Type(Integer32):
    """Custom type extremeNetFlowCollectorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeNetFlowCollectorId_Type.__name__ = "Integer32"
_ExtremeNetFlowCollectorId_Object = MibTableColumn
extremeNetFlowCollectorId = _ExtremeNetFlowCollectorId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 2),
    _ExtremeNetFlowCollectorId_Type()
)
extremeNetFlowCollectorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorId.setStatus("current")
_ExtremeNetFlowGroupPingEnabled_Type = TruthValue
_ExtremeNetFlowGroupPingEnabled_Object = MibTableColumn
extremeNetFlowGroupPingEnabled = _ExtremeNetFlowGroupPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 3),
    _ExtremeNetFlowGroupPingEnabled_Type()
)
extremeNetFlowGroupPingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowGroupPingEnabled.setStatus("current")
_ExtremeNetFlowGroupSourceIp_Type = IpAddress
_ExtremeNetFlowGroupSourceIp_Object = MibTableColumn
extremeNetFlowGroupSourceIp = _ExtremeNetFlowGroupSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 4),
    _ExtremeNetFlowGroupSourceIp_Type()
)
extremeNetFlowGroupSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowGroupSourceIp.setStatus("current")
_ExtremeNetFlowCollectorIpAddress_Type = IpAddress
_ExtremeNetFlowCollectorIpAddress_Object = MibTableColumn
extremeNetFlowCollectorIpAddress = _ExtremeNetFlowCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 5),
    _ExtremeNetFlowCollectorIpAddress_Type()
)
extremeNetFlowCollectorIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorIpAddress.setStatus("current")


class _ExtremeNetFlowCollectorUdpPort_Type(Integer32):
    """Custom type extremeNetFlowCollectorUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowCollectorUdpPort_Type.__name__ = "Integer32"
_ExtremeNetFlowCollectorUdpPort_Object = MibTableColumn
extremeNetFlowCollectorUdpPort = _ExtremeNetFlowCollectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 6),
    _ExtremeNetFlowCollectorUdpPort_Type()
)
extremeNetFlowCollectorUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorUdpPort.setStatus("current")
_ExtremeNetFlowCollectorStatusUp_Type = TruthValue
_ExtremeNetFlowCollectorStatusUp_Object = MibTableColumn
extremeNetFlowCollectorStatusUp = _ExtremeNetFlowCollectorStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 7),
    _ExtremeNetFlowCollectorStatusUp_Type()
)
extremeNetFlowCollectorStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorStatusUp.setStatus("current")


class _ExtremeNetFlowCollectorDowntime_Type(Integer32):
    """Custom type extremeNetFlowCollectorDowntime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowCollectorDowntime_Type.__name__ = "Integer32"
_ExtremeNetFlowCollectorDowntime_Object = MibTableColumn
extremeNetFlowCollectorDowntime = _ExtremeNetFlowCollectorDowntime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 8),
    _ExtremeNetFlowCollectorDowntime_Type()
)
extremeNetFlowCollectorDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorDowntime.setStatus("current")


class _ExtremeNetFlowCollectorPacketsTx_Type(Integer32):
    """Custom type extremeNetFlowCollectorPacketsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeNetFlowCollectorPacketsTx_Type.__name__ = "Integer32"
_ExtremeNetFlowCollectorPacketsTx_Object = MibTableColumn
extremeNetFlowCollectorPacketsTx = _ExtremeNetFlowCollectorPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22, 2, 2, 1, 9),
    _ExtremeNetFlowCollectorPacketsTx_Type()
)
extremeNetFlowCollectorPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNetFlowCollectorPacketsTx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-NETFLOW-MIB",
    **{"extremeNetFlow": extremeNetFlow,
       "extremeNetFlowConfigPort": extremeNetFlowConfigPort,
       "extremeNetFlowPortConfigTable": extremeNetFlowPortConfigTable,
       "extremeNetFlowPortConfigEntry": extremeNetFlowPortConfigEntry,
       "extremeNetFlowPortConfigPortIndex": extremeNetFlowPortConfigPortIndex,
       "extremeNetFlowPortConfigEnabled": extremeNetFlowPortConfigEnabled,
       "extremeNetFlowPortConfigTimout": extremeNetFlowPortConfigTimout,
       "extremeNetFlowPortOverFlowPackets": extremeNetFlowPortOverFlowPackets,
       "extremeNetFlowPortFilterConfigTable": extremeNetFlowPortFilterConfigTable,
       "extremeNetFlowPortFilterConfigEntry": extremeNetFlowPortFilterConfigEntry,
       "extremeNetFlowPortConfigPortNumber": extremeNetFlowPortConfigPortNumber,
       "extremeNetFlowPortConfigFilterEgress": extremeNetFlowPortConfigFilterEgress,
       "extremeNetFlowPortConfigFilterNumber": extremeNetFlowPortConfigFilterNumber,
       "extremeNetFlowPortEnabled": extremeNetFlowPortEnabled,
       "extremeNetFlowFilterEnabled": extremeNetFlowFilterEnabled,
       "extremeNetFlowDestIpAddress": extremeNetFlowDestIpAddress,
       "extremeNetFlowDestIpAddressMask": extremeNetFlowDestIpAddressMask,
       "extremeNetFlowSourceIpAddress": extremeNetFlowSourceIpAddress,
       "extremeNetFlowSourceIpAddressMask": extremeNetFlowSourceIpAddressMask,
       "extremeNetFlowDestPort": extremeNetFlowDestPort,
       "extremeNetFlowDestPortMask": extremeNetFlowDestPortMask,
       "extremeNetFlowSourcePort": extremeNetFlowSourcePort,
       "extremeNetFlowSourcePortMask": extremeNetFlowSourcePortMask,
       "extremeNetFlowProtocol": extremeNetFlowProtocol,
       "extremeNetFlowProtocolMask": extremeNetFlowProtocolMask,
       "extremeNetFlowFilterGroupNumber": extremeNetFlowFilterGroupNumber,
       "extremeNetFlowMatchAllFlag": extremeNetFlowMatchAllFlag,
       "extremeNetFlowMatchNoneFlag": extremeNetFlowMatchNoneFlag,
       "extremeNetFlowConfigGroup": extremeNetFlowConfigGroup,
       "extremeNetFlowGroupCollectorTable": extremeNetFlowGroupCollectorTable,
       "extremeNetFlowGroupCollectorEntry": extremeNetFlowGroupCollectorEntry,
       "extremeNetFlowGroupNumber": extremeNetFlowGroupNumber,
       "extremeNetFlowCollectorId": extremeNetFlowCollectorId,
       "extremeNetFlowGroupPingEnabled": extremeNetFlowGroupPingEnabled,
       "extremeNetFlowGroupSourceIp": extremeNetFlowGroupSourceIp,
       "extremeNetFlowCollectorIpAddress": extremeNetFlowCollectorIpAddress,
       "extremeNetFlowCollectorUdpPort": extremeNetFlowCollectorUdpPort,
       "extremeNetFlowCollectorStatusUp": extremeNetFlowCollectorStatusUp,
       "extremeNetFlowCollectorDowntime": extremeNetFlowCollectorDowntime,
       "extremeNetFlowCollectorPacketsTx": extremeNetFlowCollectorPacketsTx}
)
